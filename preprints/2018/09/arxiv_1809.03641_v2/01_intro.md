---
authors:
- Yu Feng
- Erik Schlögl
doc_id: arxiv:1809.03641v2
family_id: arxiv:1809.03641
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[1809.03641] Model Risk Measurement under Wasserstein Distance'
url_abs: http://arxiv.org/abs/1809.03641v2
url_html: https://ar5iv.org/html/1809.03641v2
venue: arXiv q-fin
version: 2
year: 2018
---


Yu Feng


Erik Schlögl

###### Abstract

The paper proposes a new approach to model risk measurement based on the Wasserstein distance between two probability measures. It formulates the theoretical motivation resulting from the interpretation of fictitious adversary of robust risk management. The proposed approach accounts for equivalent and non-equivalent probability measures and incorporates the economic reality of the fictitious adversary.
It provides practically feasible results that overcome the restriction of considering only models implying probability measures equivalent to
the reference model. The Wasserstein approach suits for various types of model risk problems, ranging from the single-asset hedging risk problem to the multi-asset allocation problem. The robust capital market line, accounting for the correlation risk, is not achievable with other non-parametric approaches.

## 1 Introduction

Most current work on robust risk management either focuses on parameter uncertainty or relies on comparison between models. To go beyond that, Glasserman and Xu recently proposed a non-parametric approach [[7](#bib.bib7)]. Under this framework, a worst-case model is found among all alternative models in a neighborhood of the reference model. Glasserman and Xu adopted the Kullback-Leibler divergence (i.e. relative entropy) to measure the distance between an alternative model and the reference model. They also proposed the use of the α𝛼\alpha-divergence to avoid heavy tails that causes integrability issues under the Kullback-Leibler divergence.

Both the Kullback-Leibler divergence and the α𝛼\alpha-divergence are special examples of the f𝑓f-divergence [[1](#bib.bib1), [2](#bib.bib2), [3](#bib.bib3)].
A big problem of using f𝑓f-divergence is that it is well-defined only when the alternative measure is absolutely continuous with respect to the reference measure. This limits the range of the alternative models under consideration. In some cases, we may want to search over all possible probability measures, whether they are absolutely continuous or not. This is especially true when we apply this approach to volatility, which corresponds to the quadratic variation of a process. If the process is driven by a Brownian motion, then searching over absolutely continuous measures rules out any model risk with respect to volatility. In Fig. [1](#S1.F1 "Fig 1 ‣ 1 Introduction ‣ Model Risk Measurement under Wasserstein Distance")(a), the distribution of the volatility is a Dirac-δ𝛿\delta function under the reference model. The worst-case scenario that accounts for the volatility risk has a widely spread distribution of the volatility. However, f𝑓f-divergence is not well-defined in this case, and therefore the worst-case scenario simply gets ignored.

![Refer to caption](/html/1809.03641/assets/delta_function1.png)

![Refer to caption](/html/1809.03641/assets/metric1.png)

Fig 1: (a) Dirac measure has a support of a single point. An alternative model with a widespread distribution cannot be related to the reference model using f𝑓f-divergence. (b) State transition in a metric space. f𝑓f-divergence does not involve the metric, so the transition from State 1 to 2 takes the same amount of cost as the transition from 1 to 3.

Furthermore, the state space considered by financial practitioners is usually equipped with a natural metric. For instance, the price of a security takes value from the set of positive real numbers, and thus naturally inherits the Euclidean metric. Assuming a diffusion process, the price of the security moves along a continuous path. This means that a large price change is less probable than a small price change, implying a stronger deviation from the reference model. However, the distance of the move, measured by the natural metric, is not explicitly taken into account when using f𝑓f-divergence. Fig. [1](#S1.F1 "Fig 1 ‣ 1 Introduction ‣ Model Risk Measurement under Wasserstein Distance")(b) shows three models corresponding to three distributions of the security price. Assuming the Model 1 is adopted as the reference model, then Model 2 as an alternative model is apparently more probable than Model 3. However, one cannot tell the difference using any type of f𝑓f-divergence, as the models have disjoint support.

As an attempt to solve these issues, we suggest to adopt the Wasserstein metric to measure the distance between probability measures. Relying on the metric equipped in the state space, the Wasserstein metric works for any two measures, even if their supports are mutually exclusive. As a result, the proposed Wassertein approach accounts for all alternative measures instead of merely the absolutely continuous ones. These features allow us to resolve the two issues of the f𝑓f-divergence as mentioned above. For financial practitioners, the proposed approach is especially useful when dealing with reference measures with a subspace support (such as a Dirac measure).

This paper is organized in the following manner. Sec. [2.1](#S2.SS1 "2.1 Motivation and Adversary Interpretation ‣ 2 Basic Concepts ‣ Model Risk Measurement under Wasserstein Distance") offers a conceptual introduction including the intuitive motivation and the basics about the Wasserstein metric and its associated transportation theory. Sec. [3.1](#S3.SS1 "3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") is the theoretical part that provides the problem formulation and main results. It also includes practical considerations and comparison between different approaches. Sec. [4](#S4 "4 Application ‣ Model Risk Measurement under Wasserstein Distance") gives a few interesting applications in mathematical finance, ranging from the volatility risk in option pricing and hedging to robust portfolio optimisation.

## 2 Basic Concepts

### 2.1 Motivation and Adversary Interpretation

To illustrate the idea of model risk in an intuitive way, we start from a simple discrete-state space. An example is the credit rating which is ordinal, e.g. A+, A, A-, BBB+, etc. Assuming we have a reference model that states that in a month the credit rating of an institution could be A+, A- or BBB+. The reference model assigns probabilities of 25%, 50% and 25% to the three states. Since we do not possess complete information, model risk exists either because the actual probabilities of the three states are different or because other ratings are still possible. Glasserman and Xu proposed the so-called “adversary” interpretation which suggests a fictitious adversary that perturbs the probabilities against us [[7](#bib.bib7)]. By perturbing the probabilities essentially the adversary adds new information, limited by its information entropy budget. For example, if the adversary would like to move 5% chance from A+ to BBB+, its consumption of relative entropy is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0.2​ln⁡(0.20.25)+0.3​ln⁡(0.30.25)=0.010.20.20.250.30.30.250.01\displaystyle 0.2\ln\left(\frac{0.2}{0.25}\right)+0.3\ln\left(\frac{0.3}{0.25}\right)=0.01 |  | (1) |

Now suppose the adversary would like to move the 5% chance to BBB, which is a state of 0 probability under the reference measure. The consumption of relative entropy

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0.2​ln⁡(0.20.25)+0.05​ln⁡(0.050)0.20.20.250.050.050\displaystyle 0.2\ln\left(\frac{0.2}{0.25}\right)+0.05\ln\left(\frac{0.05}{0}\right) |  | (2) |

becomes infinite. This simply means that such perturbation is impossible no matter how much control the adversary has. In the language of probability theory, relative entropy is well-defined only when the new measure is absolutely continuous with respect to the nominal one.

To allow for a more generic quantification of model risk, we may re-define the requested cost of perturbation. Instead of using the relative entropy, we consider about the cost of a state transition (termed as the transportation cost). This transportation cost is usually given by some metric on the state space. For simplicity we assume that the distance between two credit ratings is given by the number of ratings in between, e.g. d(d(A+, A-)))=2 and d(d(A+, BBB+)))=3. We calculate the weighted average transportation costs for the two types of perturbations discussed in the last paragraph:
  
1. shift 5% chance from A+ to BBB+: transportation cost=5%×\times3=0.15
  
2. shift 5% chance from A+ to BBB: transportation cost=5%×\times4=0.2
  
The second-type perturbation only involves a cost slighter larger than the first type, instead of being infinite.

Using the transportation cost described above, one can measure the adversary’s cost for all alternative measures rather than merely the absolutely continuous ones. It may provide state transitions that are highly concentrated. To illustrate this point, think about the transition from state A+. The fictitious adversary would push the rating only in one direction. This implies that the transportation performed by the fictitious agent can be represented by a (deterministic) map on the state space T:Ω→Ω:𝑇→ΩΩT:\Omega\to\Omega. T𝑇T is called a transportation map [[4](#bib.bib4)]. In fact, suppose it is optimal for the fictitious agent (thus the worst case scenario) to transit the state A+ to a state, say BBB+. There is no motivation for the agent to transport any probability mass from A+ to other states. This results from the linearity of the transportation cost, and will be illustrated further in the next section.

Glasserman and Xu’s interpretation of model risk involves an fictitious adversary but without explicit consideration of its economic nature. They assume that the adversary performs uniformly aiming to maximise our expected loss. In reality, such an adversary can only be achieved by a single agent or institution. The actual market structure, however, is usually more competitive. In economic terms, the fictitious adversary may consist of heterogeneous agents who act independently. This asks for approaches that quantify the model risk based on the actual market structure.

Now get back to the credit rating example. In reality there might be multiple agents that are capable of impacting the rating, among which some prefer to upgrade the rating while others prefer to dowgrade the rating. This asks for a different formulation of state transitions, for the final state transited from a given initial state becomes a random variable. All we know is a probability measure conditional to the given initial state (or a transition density). Overall, the transportation is described by a joint probability density γ:Ω×Ω→ℝ+:𝛾→ΩΩsuperscriptℝ\gamma:\Omega\times\Omega\to\mathbb{R}^{+} instead of a deterministic map. The joint density (or the corresponding measure on Ω×ΩΩΩ\Omega\times\Omega) is refered as the transportation plan[[5](#bib.bib5)]. This allows us to formulate the optimisation problem w.r.t the transportation plan instead of the transportation map. Such formulation leads to more general results capable of accounting for different types of market structure.

From a practical perspective, the main advantage of using the Wasserstein metric is to deal with reference measures supported by strict subspaces. Still in the example of credit rating, the reference measure is supported by {A+,A−,B​B​B+}limit-from𝐴limit-from𝐴limit-from𝐵𝐵𝐵\{A+,A-,BBB+\}, which is a strict subspace of the entire state space (of rating). Approaches based on f𝑓f-divergence are only capable of incorporating alternative measures with the same support. Using the Wasserstein approach, on the other hand, does allow us to alter the support. In particular, if we formulate the problem using a transportation map T𝑇T, then the new support is {T​(A+),T​(A−),T​(B​B​B+)}𝑇limit-from𝐴𝑇limit-from𝐴𝑇limit-from𝐵𝐵𝐵\{T(A+),T(A-),T(BBB+)\}, still a strict subspace. Therefore, although different transportation maps provide us with different supports, none of them is capable of spreading to the entire state space. On the other hand, by formulating the problem with a transportation plan, we indeed account for alternative measures that are supported by the entire space. Now regarding the fictitious adversary as a class of hetergenuous agents, it is reasonable to believe that the distribution is widely spread under the perturbation of the adversary.

Thus, we are interested in an approach to model risk measurement that formulates the transportation cost based on a transportation plan. We will see that this approach is capable of account for actual market structure by parametrising an entropy constraint (Sec. [3.2](#S3.SS2 "3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance")). In the remaining part of this section, we will review the Wasserstein metric and its associated transportation theory.

### 2.2 Transportation Theory and Wasserstein Metric

Starting from this point, we will always assume a continuous-state space unless otherwise stated. The approach for discrete-state spaces follows the same routine and therefore is omitted.
Now let the state space (ΩΩ\Omega, d𝑑d) be a Polish metric space, we may define the transportation cost c:Ω×Ω→ℝ+:𝑐→ΩΩsubscriptℝc:\Omega\times\Omega\to\mathbb{R}\_{+} by the n𝑛n-th power of the metric, i.e. c​(x,y)=d​(x,y)n𝑐𝑥𝑦𝑑superscript𝑥𝑦𝑛c(x,y)=d(x,y)^{n}, where n∈[1,∞)𝑛1n\in[1,\infty).
Given two probability measures P𝑃P and Q𝑄Q on (ΩΩ\Omega, d𝑑d), we may formulate the optimal transportation problem using either a transportation map or a transportation plan. For the former approach, we aim to find the transportation map T:Ω→Ω:𝑇→ΩΩT:\Omega\to\Omega that realizes the infimum

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | infTsubscriptinfimum𝑇\displaystyle\inf\_{T} | ∫Ωp​(x)​c​(x,T​(x))​𝑑xsubscriptΩ𝑝𝑥𝑐𝑥𝑇𝑥differential-d𝑥\displaystyle\int\_{\Omega}p(x)c\left(x,T(x)\right)dx |  | (3) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t.formulae-sequence𝑠𝑡\displaystyle s.t. | |JT​(x)|​q​(T​(x))=p​(x),∀x∈Ωformulae-sequencesubscript𝐽𝑇𝑥𝑞𝑇𝑥𝑝𝑥for-all𝑥Ω\displaystyle~{}\left|J\_{T}(x)\right|q\left(T(x)\right)=p(x),~{}\forall x\in\Omega |  |

where p​(x)𝑝𝑥p(x) and q​(x)𝑞𝑥q(x) are the probability density functions of the two measures P𝑃P and Q𝑄Q, respectively.
JTsubscript𝐽𝑇J\_{T} is the Jacobian of the map T𝑇T. It is part of the constraint that enforces the map T𝑇T to be measure-preserving.
Eq. [3](#S2.E3 "In 2.2 Transportation Theory and Wasserstein Metric ‣ 2 Basic Concepts ‣ Model Risk Measurement under Wasserstein Distance") is refered as the Monge’s formulation of the optimal transportation problem.

The problem of Monge’s formulation is that the existence of a measure-preserving map T𝑇T is not guaranteed. Examples in the last section provide a discrete-state illustration of this issue: s​u​p​p​(Q)={T​(A+),T​(A−),T​(B​B​B+)}𝑠𝑢𝑝𝑝𝑄𝑇limit-from𝐴𝑇limit-from𝐴𝑇limit-from𝐵𝐵𝐵supp(Q)=\{T(A+),T(A-),T(BBB+)\} has at most three elements. As a result, there is no measure-preserving map if |s​u​p​p​(Q)|>|s​u​p​p​(P)|𝑠𝑢𝑝𝑝𝑄𝑠𝑢𝑝𝑝𝑃|supp(Q)|>|supp(P)|. In a continuous-state space, a measure-preserving map sends a Dirac measure to another Dirac measure. Therefore, measure-preserving map does not exist if P𝑃P is a Dirac measure while Q𝑄Q is not. The ill-posed Monge’s formulation can be improved by adopting a transportation plan γ:Ω×Ω→ℝ+:𝛾→ΩΩsubscriptℝ\gamma:\Omega\times\Omega\to\mathbb{R}\_{+}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | infγsubscriptinfimum𝛾\displaystyle\inf\_{\gamma} | ∫Ω×Ωγ​(x,y)​c​(x,y)​𝑑x​𝑑ysubscriptΩΩ𝛾𝑥𝑦𝑐𝑥𝑦differential-d𝑥differential-d𝑦\displaystyle\int\_{\Omega\times\Omega}\gamma(x,y)c(x,y)dxdy |  | (4) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t.formulae-sequence𝑠𝑡\displaystyle s.t. | ∫Ωγ​(x,y)​𝑑y=p​(x)subscriptΩ𝛾𝑥𝑦differential-d𝑦𝑝𝑥\displaystyle\int\_{\Omega}\gamma(x,y)dy=p(x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∫Ωγ​(x,y)​𝑑x=q​(y)subscriptΩ𝛾𝑥𝑦differential-d𝑥𝑞𝑦\displaystyle\int\_{\Omega}\gamma(x,y)dx=q(y) |  |

Eq. [4](#S2.E4 "In 2.2 Transportation Theory and Wasserstein Metric ‣ 2 Basic Concepts ‣ Model Risk Measurement under Wasserstein Distance") is refered as the Kantorovich’s formulation of the optimal transportation problem.
It is clear that every transportation map T𝑇T can be given by a transportation plan

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ​(x,y)=|JT​(x)|​q​(y)​δ​(y−T​(x))𝛾𝑥𝑦subscript𝐽𝑇𝑥𝑞𝑦𝛿𝑦𝑇𝑥\displaystyle\gamma(x,y)=\left|J\_{T}(x)\right|q\left(y\right)\delta\left(y-T(x)\right) |  | (5) |

where δ​(⋅)𝛿⋅\delta(\cdot) is the Dirac-δ𝛿\delta function. In addition, the existence of a transportation plan is guaranteed as γ​(x,y)=p​(x)​q​(y)𝛾𝑥𝑦𝑝𝑥𝑞𝑦\gamma(x,y)=p(x)q(y) always satisfies the constraints in Eq. [4](#S2.E4 "In 2.2 Transportation Theory and Wasserstein Metric ‣ 2 Basic Concepts ‣ Model Risk Measurement under Wasserstein Distance"). According to these observations, the Kantorovich’s formulation is preferred over the Monge’s formulation.
Remember that the transportation cost c​(x,y)𝑐𝑥𝑦c(x,y) is the n𝑛n-th power of the metric c​(x,y)𝑐𝑥𝑦c(x,y). The n𝑛n-th Wasserstein matric, denoted by Wnsubscript𝑊𝑛W\_{n}, is defined as the infimum in Eq. [4](#S2.E4 "In 2.2 Transportation Theory and Wasserstein Metric ‣ 2 Basic Concepts ‣ Model Risk Measurement under Wasserstein Distance"), raised to the power of 1/n1𝑛1/n. In the next section, the theoretical formulation and the main results of this paper will be presented with the help of the Kantorovich’s formulation. The transportation cost function c​(x,y)𝑐𝑥𝑦c(x,y) will be regarded as a generic non-negative function, without reference to its specific form or the power n𝑛n.

## 3 Theory

### 3.1 Wasserstein Formulation of the Model Risk Problem

The core part of model risk measurement is to determine the alternative model under the worst-case scenario. In the language of probability theory, we need to determine the alternative probability measure that maximizes our expected loss.
We may formulate the problem in the following way. Given a nominal probability measure P𝑃P on the state space ΩΩ\Omega, we would like to find a worst-case measure Q∗superscript𝑄Q^{\*} that realizes the following supremum:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supQsubscriptsupremum𝑄\displaystyle\sup\_{Q}\, | 𝖤Q​[V​(X)]superscript𝖤𝑄delimited-[]𝑉𝑋\displaystyle\mathsf{E}^{Q}[V(X)] |  | (6) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t.formulae-sequence𝑠𝑡\displaystyle s.t.\, | D(P||Q)≤η\displaystyle D(P||Q)\leq\eta |  |

The expectation is taken under the alternative measure Q𝑄Q, on a loss function V:Ω→ℝ:𝑉→ΩℝV:\Omega\to\mathbb{R}.
Only alternative measures that are close enough to the reference measure are deemed as legitimate. This restriction is formulated by constraining the statistical distance D(P||Q)D(P||Q) to be equal to or less than a constant η𝜂\eta.

Glasserman and Xu suggest using the relative entropy (or Kullback-Leibler divergence) for D​(P,Q)𝐷𝑃𝑄D(P,Q). Like any f𝑓f-divergence, relative entropy has limited feasibility as only equivalent measures are legitimate. Based on the discussion in the last section, we suggest to apply the Wasserstein metric instead.
The actual formulation of the model risk problem, on the other hand, has a slightly different form than Eq. [6](#S3.E6 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"). Specifically, instead of optimizing the expectation w.r.t the alternative measure Q𝑄Q (or its density function q:Ω→ℝ+:𝑞→Ωsuperscriptℝq:\Omega\to\mathbb{R}^{+}), we optimize the expectation w.r.t the transportation plan γ:Ω×Ω→ℝ+:𝛾→ΩΩsuperscriptℝ\gamma:\Omega\times\Omega\to\mathbb{R}^{+} directly. The single constraint on q𝑞q is replaced by two constraints applied to γ𝛾\gamma, including the marginalisation condition given in Eq. [4](#S2.E4 "In 2.2 Transportation Theory and Wasserstein Metric ‣ 2 Basic Concepts ‣ Model Risk Measurement under Wasserstein Distance"). This formulation is based on the idea of state transition and is illustrated below.

Based on the discussion in the last section, for any pair of states x,y∈Ω

𝑥𝑦
Ωx,y\in\Omega all we need to find is the transition density from x𝑥x to y𝑦y, pY|X​(y|x)subscript𝑝conditional𝑌𝑋conditional𝑦𝑥p\_{Y|X}(y|x). Given a function of transportation cost from x𝑥x to y𝑦y, c​(x,y)𝑐𝑥𝑦c(x,y), the expected transportation cost conditional to an initial state x𝑥x is

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​(x)=∫ΩpY|X​(y|x)​c​(x,y)​𝑑y𝑊𝑥subscriptΩsubscript𝑝conditional𝑌𝑋conditional𝑦𝑥𝑐𝑥𝑦differential-d𝑦\displaystyle W(x)=\int\_{\Omega}p\_{Y|X}(y|x)c(x,y)dy |  | (7) |

The initial state x𝑥x follows a distribution pX​(x)subscript𝑝𝑋𝑥p\_{X}(x) given by the reference model. Take expectation under the reference measure, we get the unconditional transportation cost

|  |  |  |  |
| --- | --- | --- | --- |
|  | W=∫ΩpX​(x)​W​(x)​𝑑x=∫Ω×ΩpX,Y​(x,y)​c​(x,y)​𝑑x​𝑑y𝑊subscriptΩsubscript𝑝𝑋𝑥𝑊𝑥differential-d𝑥subscriptΩΩsubscript𝑝  𝑋𝑌𝑥𝑦𝑐𝑥𝑦differential-d𝑥differential-d𝑦\displaystyle W=\int\_{\Omega}p\_{X}(x)W(x)dx=\int\_{\Omega\times\Omega}p\_{X,Y}(x,y)c(x,y)dxdy |  | (8) |

where the joint distribution pX,Y​(x,y)=pX​(x)​pY|X​(y|x)subscript𝑝

𝑋𝑌𝑥𝑦subscript𝑝𝑋𝑥subscript𝑝conditional𝑌𝑋conditional𝑦𝑥p\_{X,Y}(x,y)=p\_{X}(x)p\_{Y|X}(y|x). To be consistent with the notation used previously, we denote the marginal distributions pXsubscript𝑝𝑋p\_{X}, pYsubscript𝑝𝑌p\_{Y} by p𝑝p, q𝑞q, and the joint distribution pX,Ysubscript𝑝

𝑋𝑌p\_{X,Y} by the transportation plan γ𝛾\gamma. It is noted that the transition converts the initial distribution p​(x)𝑝𝑥p(x) to a final distribution q​(y)𝑞𝑦q(y), inducing a change of measure on the state space ΩΩ\Omega.

One of the key tasks of the model risk measurement is to solve for the worst-case model under certain constraints. These constraints set the criteria for legitimate alternative models. Now denote the loss function by V​(x)𝑉𝑥V(x) (x∈Ω𝑥Ωx\in\Omega), the probability density function of the reference model by p​(x)𝑝𝑥p(x), and the probability density function of an alternative model by q​(x)𝑞𝑥q(x).
We formulate the problem by the supremum of the expected loss over all legitimate models:

|  |  |  |  |
| --- | --- | --- | --- |
|  | supq​(y)∫Ωq​(y)​V​(y)​𝑑ysubscriptsupremum𝑞𝑦subscriptΩ𝑞𝑦𝑉𝑦differential-d𝑦\displaystyle\sup\_{q(y)}\int\_{\Omega}q(y)V(y)dy |  | (9) |

According to the discussion in the last section, we regard the change of measure as probabilistic state transitions. The probability density function q​(y)𝑞𝑦q(y) of the alternative model is merely the marginalisation of a joint density (or transportation plan) γ​(x,y)𝛾𝑥𝑦\gamma(x,y), i.e. q​(y)=∫Ωγ​(x,y)​𝑑x𝑞𝑦subscriptΩ𝛾𝑥𝑦differential-d𝑥q(y)=\int\_{\Omega}\gamma(x,y)dx.
This allows us to take the supremum over γ​(x,y)𝛾𝑥𝑦\gamma(x,y) instead of q​(y)𝑞𝑦q(y):

|  |  |  |  |
| --- | --- | --- | --- |
|  | supγ​(x,y)∫Ω×Ωγ​(x,y)​V​(y)​𝑑x​𝑑ysubscriptsupremum𝛾𝑥𝑦subscriptΩΩ𝛾𝑥𝑦𝑉𝑦differential-d𝑥differential-d𝑦\displaystyle\sup\_{\gamma(x,y)}\int\_{\Omega\times\Omega}\gamma(x,y)V(y)dxdy |  | (10) |

The first constraint of the supremum problem comes from the marginalisation of the joint density w.r.t x𝑥x, as it is given by the reference model:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ωγ​(x,y)​𝑑y=p​(x)subscriptΩ𝛾𝑥𝑦differential-d𝑦𝑝𝑥\displaystyle\int\_{\Omega}\gamma(x,y)dy=p(x) |  | (11) |

In a similar way to Glasserman and Xu’s work, we restrict all alternative measures by their distances from the reference model. The distance is now measured by the average transportation cost given in Eq. [8](#S3.E8 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"). It reflects the expected cost paid by a fictitious adversary who attempts to transit a state x𝑥x to an alternative state y𝑦y according to the transportation plan γ​(x,y)𝛾𝑥𝑦\gamma(x,y). This results in the following constraint which defines the set of legitimate measures:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∫Ω×Ωγ​(x,y)​c​(x,y)​𝑑x​𝑑y≤subscriptΩΩ𝛾𝑥𝑦𝑐𝑥𝑦differential-d𝑥differential-d𝑦absent\displaystyle\int\_{\Omega\times\Omega}\gamma(x,y)c(x,y)dxdy\leq | η𝜂\displaystyle\eta |  | (12) |

The constant η𝜂\eta in Eq. [12](#S3.E12 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") is termed as the Wasserstein distance budget, just as the relative entropy budget in Glasserman and Xu’s approach. In order to account for a specific density function q∗​(y)superscript𝑞𝑦q^{\*}(y) in the constrained supremum problem given by Eq. [9](#S3.E9 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance")-[12](#S3.E12 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), the Wasserstein distance, defined in Eq. [4](#S2.E4 "In 2.2 Transportation Theory and Wasserstein Metric ‣ 2 Basic Concepts ‣ Model Risk Measurement under Wasserstein Distance"), between q∗​(y)superscript𝑞𝑦q^{\*}(y) and the nominal density p​(x)𝑝𝑥p(x) cannot exceed η𝜂\eta. In fact, if q∗​(y)superscript𝑞𝑦q^{\*}(y) can be obtained by marginalizing a transportation cost γ∗​(x,y)superscript𝛾𝑥𝑦\gamma^{\*}(x,y) that satisfies Eq. [11](#S3.E11 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance")-[12](#S3.E12 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), then according to Eq. [4](#S2.E4 "In 2.2 Transportation Theory and Wasserstein Metric ‣ 2 Basic Concepts ‣ Model Risk Measurement under Wasserstein Distance") its Wasserstein distance with the nominal density function p​(x)𝑝𝑥p(x) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​(p,q∗)=𝑊𝑝superscript𝑞absent\displaystyle W(p,q^{\*})= | infγ∫Ω×Ωγ​(x,y)​c​(x,y)​𝑑x​𝑑ysubscriptinfimum𝛾subscriptΩΩ𝛾𝑥𝑦𝑐𝑥𝑦differential-d𝑥differential-d𝑦\displaystyle\inf\_{\gamma}\int\_{\Omega\times\Omega}\gamma(x,y)c(x,y)dxdy |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ∫Ω×Ωγ∗​(x,y)​c​(x,y)​𝑑x​𝑑y≤ηsubscriptΩΩsuperscript𝛾𝑥𝑦𝑐𝑥𝑦differential-d𝑥differential-d𝑦𝜂\displaystyle\int\_{\Omega\times\Omega}\gamma^{\*}(x,y)c(x,y)dxdy\leq\eta |  | (13) |

On the other hand, if W​(p,q∗)<η𝑊𝑝superscript𝑞𝜂W(p,q^{\*})<\eta, then the density function q∗​(y)superscript𝑞𝑦q^{\*}(y) can always be expressed by the marginalisation of a transportation plan γ∗​(x,y)superscript𝛾𝑥𝑦\gamma^{\*}(x,y) that satisfies Eq. [11](#S3.E11 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance")-[12](#S3.E12 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"). Otherwise, in the definition of the Wasserstein distance, Eq. [4](#S2.E4 "In 2.2 Transportation Theory and Wasserstein Metric ‣ 2 Basic Concepts ‣ Model Risk Measurement under Wasserstein Distance"), η𝜂\eta sets a lower bound for the term

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ω×Ωγ​(x,y)​c​(x,y)​𝑑x​𝑑ysubscriptΩΩ𝛾𝑥𝑦𝑐𝑥𝑦differential-d𝑥differential-d𝑦\displaystyle\int\_{\Omega\times\Omega}\gamma(x,y)c(x,y)dxdy |  | (14) |

Therefore the Wasserstein distance, as the infimum of the term above, is equal to or larger than η𝜂\eta. This immediately violates the assumption W​(p,q∗)<η𝑊𝑝superscript𝑞𝜂W(p,q^{\*})<\eta.
In summary, η𝜂\eta sets the maximum level (budget) of Wasserstein distance for an alternative measure to be legitimate.

Remarkably, even though the problem (Eq. [10](#S3.E10 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance")-[12](#S3.E12 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance")) is formulated using the transportation plan (Kantorovich’s formulation), its solution can be expressed by a transportation map T∗:Ω→Ω:superscript𝑇→ΩΩT^{\*}:\Omega\to\Omega,

|  |  |  |  |
| --- | --- | --- | --- |
|  | T∗​(x)=arg⁡maxy∈Ω⁡[V​(y)−c​(x,y)β]superscript𝑇𝑥subscript𝑦Ω𝑉𝑦𝑐𝑥𝑦𝛽\displaystyle T^{\*}(x)=\arg\max\_{y\in\Omega}\left[V(y)-\frac{c(x,y)}{\beta}\right] |  | (15) |

where β∈ℝ++𝛽subscriptℝabsent\beta\in\mathbb{R}\_{++} is a constant. The underlying reason is the linearity of Eq. [14](#S3.E14 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") w.r.t the transportation plan γ𝛾\gamma. Suppose the worst case scenario is to transit a state x𝑥x to another state T∗​(x)superscript𝑇𝑥T^{\*}(x). Then there is no motivation for the fictitious adversary to transit x𝑥x to states other than T∗​(x)superscript𝑇𝑥T^{\*}(x), say T′​(x)superscript𝑇′𝑥T^{\prime}(x), for the adversary could continue improving the target by increasing γ​(x,T∗​(x))𝛾𝑥superscript𝑇𝑥\gamma(x,T^{\*}(x)) while reducing γ​(x,T′​(x))𝛾𝑥superscript𝑇′𝑥\gamma(x,T^{\prime}(x)) (by the same amount). See Appendix A for a sketch of the derivation of Eq. [15](#S3.E15 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance").

### 3.2 Entropy Constraint on Transportation Plan

Eq. [15](#S3.E15 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") provides the worst-case transportation map for the problem formulated in Eq. [10](#S3.E10 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance")-[12](#S3.E12 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"). This formulation in fact assumes a zero-sum game between two parties, in which our counterparty attempts to shift a state x𝑥x to y∗​(x)superscript𝑦𝑥y^{\*}(x) (deterministically) so that its profit (thus our loss) can be maximized. In Sec. [2.1](#S2.SS1 "2.1 Motivation and Adversary Interpretation ‣ 2 Basic Concepts ‣ Model Risk Measurement under Wasserstein Distance"), we mentioned that the actual market structure may be more competitive consisting of heterogeous agents that act more or less independently. This calls for a widespread transition density pY|X​(y|x)subscript𝑝conditional𝑌𝑋conditional𝑦𝑥p\_{Y|X}(y|x) (instead of being a δ𝛿\delta-function).

In practice, it is also advantageous of having a widely distributed transition density.
For the purpose of risk management, we need to consider a wide range of alternative measures due to model ambiguity. As a result a widespread distribution is usually more representative than a narrow distribution. From the information-theoretic point of view, a widespread distribution contains less information (more entropy) thus more appropriately representing the model ambiguity.
Now have a think about the practical situations where the approaches based on f𝑓f-divergence are not applicable. They usually have reference measures that are too restrictive in the sense that they are supported by merely subspaces (of the state space).
To correctly quantify the model risk one should consider widespread distributions supported by the entire state space. However, these distributions do not have well-defined f𝑓f-divergence w.r.t the reference measure, providing an inherent issue of these approaches.

One of the primary purposes of using Wasserstein metric instead of f𝑓f-divergence is to tackle this issue. Specifically, we would like to include all measures regardless of their support. This purpose is achieved by using the Kantorovich’s formulation as illustrated in Sec. [2.2](#S2.SS2 "2.2 Transportation Theory and Wasserstein Metric ‣ 2 Basic Concepts ‣ Model Risk Measurement under Wasserstein Distance").
However, without further constraint the worst-case model can still be achieved with a transportation map, as illustrated by Eq. [15](#S3.E15 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"). This causes the worst-case measure to be restrictive if the reference measure is supported by merely a subspace. To achieve a widespread worst-case distribution, one may need to impose further constraints to Eq. [10](#S3.E10 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance")-[12](#S3.E12 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance").

A Dirac reference measure, denoted by P𝑃P, provides a special example where Eq. [15](#S3.E15 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") is not suitable for characterizing the worst-case scenario. Applying the transportation map T∗superscript𝑇T^{\*} results in the worst-case measure supported by {T​(x)}𝑇𝑥\{T(x)\} where x𝑥x is the sole element in s​u​p​p​(P)𝑠𝑢𝑝𝑝𝑃supp(P). The worst-case measure is Dirac as well.
In most cases, this worst-case measure inappropriately accounts for model ambiguity.
To resolve this issue, we may further impose an entropy constraint that guarantees the worst-case measure to be supported by the entire state space:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∫Ω×Ωγ​(x,y)​ln⁡γ​(x,y)​𝑑x​𝑑y≥μsubscriptΩΩ𝛾𝑥𝑦𝛾𝑥𝑦differential-d𝑥differential-d𝑦𝜇\displaystyle-\int\_{\Omega\times\Omega}\gamma(x,y)\ln\gamma(x,y)dxdy\geq\mu |  | (16) |

The LHS is the (differential) entropy [[6](#bib.bib6)] of the joint distribution (transportation plan) γ​(x,y)𝛾𝑥𝑦\gamma(x,y), and the RHS is a constant μ∈ℝ𝜇ℝ\mu\in\mathbb{R} (or a positive constant μ∈ℝ++𝜇subscriptℝabsent\mu\in\mathbb{R}\_{++} for discrete-state space). This constraint excludes every transportation plan that is equivalent to a transportation map. In fact, every transportation map T𝑇T gives a transportation plan with a δ𝛿\delta-function transition density (see Eq. [5](#S2.E5 "In 2.2 Transportation Theory and Wasserstein Metric ‣ 2 Basic Concepts ‣ Model Risk Measurement under Wasserstein Distance")). For such transportation plan, the δ𝛿\delta-function makes the LHS of Eq. [16](#S3.E16 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance")
approaching negative infinity (or zero for discrete-state space), and is therefore excluded.

Alternatively, Eq. [16](#S3.E16 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") can be interpreted with respect to the transition density function pY|X​(y|x)subscript𝑝conditional𝑌𝑋conditional𝑦𝑥p\_{Y|X}(y|x). We may rewrite Eq. [16](#S3.E16 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") by

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∫Ω×Ωγ​(x,y)​ln⁡pY|X​(y|x)​𝑑x​𝑑y≥μ+∫Ωp​(x)​ln⁡p​(x)​𝑑xsubscriptΩΩ𝛾𝑥𝑦subscript𝑝conditional𝑌𝑋conditional𝑦𝑥differential-d𝑥differential-d𝑦𝜇subscriptΩ𝑝𝑥𝑝𝑥differential-d𝑥\displaystyle-\int\_{\Omega\times\Omega}\gamma(x,y)\ln p\_{Y|X}(y|x)dxdy\geq\mu+\int\_{\Omega}p(x)\ln p(x)dx |  | (17) |

Eq. [17](#S3.E17 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") imposes a restriction on the transition density function.
A tighter restriction (with a larger μ𝜇\mu) implies a wider transition density, reflecting a market structure that is more competitive. On the other hand, if we relax the constraint completely by shifting μ𝜇\mu towards negative infinity (or zero for discrete-state space), then we permit transition densities to take the form of δ𝛿\delta-functions, corresponding to the single-agent adversary.

We may further introduce terms from information theory, and rewrite Eq. [17](#S3.E17 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ωp​(x)​H​(Y|X=x)​𝑑x≥μ−H​(X)subscriptΩ𝑝𝑥𝐻conditional𝑌𝑋𝑥differential-d𝑥𝜇𝐻𝑋\displaystyle\int\_{\Omega}p(x)H(Y|X=x)dx\geq\mu-H(X) |  | (18) |

where H​(X)𝐻𝑋H(X) denotes the entropy of the random variable X𝑋X [[6](#bib.bib6)]. Since its distribution p​(x)𝑝𝑥p(x) is given by the reference model, H​(X)𝐻𝑋H(X) is deemed as a constant. H​(Y|X=x)𝐻conditional𝑌𝑋𝑥H(Y|X=x), on the other hand, is the information entropy w.r.t the transition density pY|X​(y|x)subscript𝑝conditional𝑌𝑋conditional𝑦𝑥p\_{Y|X}(y|x). It is interpreted as the entropy of the random variable Y𝑌Y, conditional to X𝑋X taking a given value x𝑥x. H​(Y|X=x)𝐻conditional𝑌𝑋𝑥H(Y|X=x) quantifies the uncertainty of the transportation from a given state x𝑥x. Generally a more competitive market that involves more independent decision-makers leads to a more uncertain state transition, thus a larger H​(Y|X=x)𝐻conditional𝑌𝑋𝑥H(Y|X=x).
As a result, Eq. [18](#S3.E18 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") allows us to incorporate the actual market structure by parametrising μ𝜇\mu.
It is noted that in information theory, the LHS of Eq. [19](#S3.E19 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") is termed as the conditional (differential) entropy and is denoted by H​(Y|X)𝐻conditional𝑌𝑋H(Y|X) [[6](#bib.bib6)].
This leads to an equivalent information-theoretic version of the constraint Eq. [16](#S3.E16 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(Y|X)≥μ−H​(X)𝐻conditional𝑌𝑋𝜇𝐻𝑋\displaystyle H(Y|X)\geq\mu-H(X) |  | (19) |

### 3.3 Main Result and Discussion

The supremum problem Eq. [10](#S3.E10 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), subject to the three constraints Eq. [11](#S3.E11 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), [12](#S3.E12 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") and [16](#S3.E16 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), formulates the complete version of the Wasserstein approach to model risk measurement.
Now suppose there exists a joint distribution γ∗​(x,y)superscript𝛾𝑥𝑦\gamma^{\*}(x,y) that solves the problem. Then the worst-case model is characterised by a probability density function

|  |  |  |  |
| --- | --- | --- | --- |
|  | q∗​(y)=∫x∈Ωγ∗​(x,y)​𝑑x,∀y∈Ωformulae-sequencesuperscript𝑞𝑦subscript𝑥Ωsuperscript𝛾𝑥𝑦differential-d𝑥for-all𝑦Ω\displaystyle q^{\*}(y)=\int\_{x\in\Omega}\gamma^{\*}(x,y)dx,~{}~{}\forall y\in\Omega |  | (20) |

To solve the constrained supremum problem, we introduce two multipliers α∈ℝ+𝛼subscriptℝ\alpha\in\mathbb{R}\_{+} and β∈ℝ+𝛽subscriptℝ\beta\in\mathbb{R}\_{+}, and transform the original problem to a dual problem. Solving the inner part of the dual problem leads to our main result (see Appendix B for derivation):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | q∗​(y)=superscript𝑞𝑦absent\displaystyle q^{\*}(y)= | ∫Ω𝑑x​p​(x)​exp⁡(V​(y)α−c​(x,y)α​β)∫Ωexp⁡(V​(z)α−c​(x,z)α​β)​𝑑zsubscriptΩdifferential-d𝑥𝑝𝑥𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽subscriptΩ𝑉𝑧𝛼𝑐𝑥𝑧𝛼𝛽differential-d𝑧\displaystyle\int\_{\Omega}dx\frac{p(x)\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right)}{\int\_{\Omega}\exp\left(\frac{V(z)}{\alpha}-\frac{c(x,z)}{\alpha\beta}\right)dz} |  | (21) |

It is noted that the multipliers α𝛼\alpha and β𝛽\beta are in fact controlling variables that determine the levels of restriction, of the entropy constraint Eq. [16](#S3.E16 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") and the transportation constraint Eq. [12](#S3.E12 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), respectively.

The limit when α𝛼\alpha approaches zero corresponds to complete relaxation of the entropy constraint Eq. [16](#S3.E16 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"). In this limit Eq. [20](#S3.E20 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") degenerates to the probability density function induced by the transportation map given by Eq. [15](#S3.E15 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"). On the other side of the spectrum, Eq. [20](#S3.E20 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") approaches a uniform distribution when α𝛼\alpha approaches infinity, as a result of the tight entropy constraint.

In the extreme case of β=0𝛽0\beta=0, Eq. [20](#S3.E20 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") leads to a simple result q∗​(x)=p​(x)superscript𝑞𝑥𝑝𝑥q^{\*}(x)=p(x). This is because the transportation constraint Eq. [12](#S3.E12 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") reaches its tightest limit (η=0𝜂0\eta=0). No state transition is allowed thus preserving the reference model. On the other hand, when β𝛽\beta approaches infinity, the worst-case distribution q∗​(y)∼exp⁡(V​(y)/α)similar-tosuperscript𝑞𝑦𝑉𝑦𝛼q^{\*}(y)\sim\exp(V(y)/\alpha) is exponentially distributed. In this case, the transportation cost is essentially zero. As a result, the worst-case measure is the one that maximises the expected value of V​(Y)𝑉𝑌V(Y) with a reasonably large entropy (the maximum expected value is given by a Dirac measure at arg⁡maxy⁡V​(y)subscript𝑦𝑉𝑦\arg\max\_{y}V(y) but this results in a very low entropy). Special cases of Eq. [21](#S3.E21 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") are tabulated in Tab. [1](#S3.T1 "Table 1 ‣ 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") for different values of α𝛼\alpha and β𝛽\beta.

Table 1: Worst-case probability density function at different (α,β)𝛼𝛽(\alpha,\beta) combinations. p𝑝p is the nominal distribution and u𝑢u is the uniform distribution. δ𝛿\delta denotes the Dirac δ𝛿\delta-function and T∗superscript𝑇T^{\*} is the transportation map given by Eq. [15](#S3.E15 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance").

|  | α=0𝛼0\alpha=0 | α𝛼\alpha | α→∞→𝛼\alpha\to\infty |
| --- | --- | --- | --- |
| β=0𝛽0\beta=0 | p​(x)𝑝𝑥p(x) | | |
| β𝛽\beta | p​(T−∗1​(x))/|JT|p(T^{{}^{\*}-1}(x))/|J\_{T}| | given by Eq. [20](#S3.E20 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") | →u​(x)→absent𝑢𝑥\to u(x) |
| β→∞→𝛽\beta\to\infty | δ​(x−arg⁡max⁡V​(x))𝛿𝑥𝑉𝑥\delta(x-\arg\max V(x)) | ∝eV​(x)/αproportional-toabsentsuperscript𝑒𝑉𝑥𝛼\propto e^{V(x)/\alpha} |

### 3.4 Practical Considerations

According to Table. [1](#S3.T1 "Table 1 ‣ 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), the worst-case measure approaches a uniform distribution when α𝛼\alpha approaches infinity (i.e. under the most restrictive entropy constraint). In practice, we may want the worst-case distribution to converge to a given density function q0subscript𝑞0q\_{0} instead of being uniform. This requires modification on the formulation of the problem, by generalising the entropy constraint Eq. [19](#S3.E19 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") to

|  |  |  |  |
| --- | --- | --- | --- |
|  | −DK​L(P(Y|X)||Q0(Y))≥μ−H(X)−H(Y)\displaystyle-D\_{KL}\left(P(Y|X)||Q\_{0}(Y)\right)\geq\mu-H(X)-H(Y) |  | (22) |

DK​L(P(Y|X)||Q0(Y))D\_{KL}\left(P(Y|X)||Q\_{0}(Y)\right) denotes the conditional relative entropy, given by the expected value of the KL divergence, DK​L(P(Y|X=x)||Q0(Y))D\_{KL}(P(Y|X=x)||Q\_{0}(Y)), of the two probability density functions w.r.t y𝑦y, pY|X(⋅|x)p\_{Y|X}(\cdot|x) and q0​(⋅)subscript𝑞0⋅q\_{0}(\cdot). Written explicitly, the conditional relative entropy takes the form of

|  |  |  |  |
| --- | --- | --- | --- |
|  | DK​L(P(Y|X)||Q0(Y))=\displaystyle D\_{KL}\left(P(Y|X)||Q\_{0}(Y)\right)= | ∫Ωp​(x)​(∫ΩpY|X​(y|x)​ln⁡(pY|X​(y|x)q0​(y))​𝑑y)​𝑑xsubscriptΩ𝑝𝑥subscriptΩsubscript𝑝conditional𝑌𝑋conditional𝑦𝑥subscript𝑝conditional𝑌𝑋conditional𝑦𝑥subscript𝑞0𝑦differential-d𝑦differential-d𝑥\displaystyle\int\_{\Omega}p(x)\left(\int\_{\Omega}p\_{Y|X}(y|x)\ln\left(\frac{p\_{Y|X}(y|x)}{q\_{0}(y)}\right)dy\right)dx |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | ∫Ω×Ωγ​(x,y)​ln⁡γ​(x,y)q0​(y)​d​x​d​y−∫Ωp​(x)​ln⁡p​(x)​𝑑xsubscriptΩΩ𝛾𝑥𝑦𝛾𝑥𝑦subscript𝑞0𝑦𝑑𝑥𝑑𝑦subscriptΩ𝑝𝑥𝑝𝑥differential-d𝑥\displaystyle\int\_{\Omega\times\Omega}\gamma(x,y)\ln\frac{\gamma(x,y)}{q\_{0}(y)}dxdy-\int\_{\Omega}p(x)\ln p(x)dx |  | (23) |

Substituting Eq. [3.4](#S3.Ex6 "3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") into Eq. [22](#S3.E22 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") allows us to obtain the explicit version of the constraint:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∫Ω×Ωγ​(x,y)​ln⁡γ​(x,y)q0​(y)​d​x​d​y−∫Ωq0​(y)​ln⁡q0​(y)​𝑑y≥μsubscriptΩΩ𝛾𝑥𝑦𝛾𝑥𝑦subscript𝑞0𝑦𝑑𝑥𝑑𝑦subscriptΩsubscript𝑞0𝑦subscript𝑞0𝑦differential-d𝑦𝜇\displaystyle-\int\_{\Omega\times\Omega}\gamma(x,y)\ln\frac{\gamma(x,y)}{q\_{0}(y)}dxdy-\int\_{\Omega}q\_{0}(y)\ln q\_{0}(y)dy\geq\mu |  | (24) |

It is clear that the previous entropy constraint Eq. [16](#S3.E16 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") is merely a special case of Eq. [24](#S3.E24 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") in which q0subscript𝑞0q\_{0} is a uniform distribution. Under this formulation, the problem that we need to solve consists of Eq. [10](#S3.E10 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), [11](#S3.E11 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), [12](#S3.E12 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") and [24](#S3.E24 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"). The result differs from Eq. [21](#S3.E21 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") by a weighting function q0subscript𝑞0q\_{0} (see Appendix B for derivation):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | q∗​(y)=superscript𝑞𝑦absent\displaystyle q^{\*}(y)= | ∫Ω𝑑x​p​(x)​q0​(y)​exp⁡(V​(y)α−c​(x,y)α​β)∫Ωq0​(z)​exp⁡(V​(z)α−c​(x,z)α​β)​𝑑zsubscriptΩdifferential-d𝑥𝑝𝑥subscript𝑞0𝑦𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽subscriptΩsubscript𝑞0𝑧𝑉𝑧𝛼𝑐𝑥𝑧𝛼𝛽differential-d𝑧\displaystyle\int\_{\Omega}dx\frac{p(x)q\_{0}(y)\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right)}{\int\_{\Omega}q\_{0}(z)\exp\left(\frac{V(z)}{\alpha}-\frac{c(x,z)}{\alpha\beta}\right)dz} |  | (25) |

It is noted that Eq. [25](#S3.E25 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") takes a similar form to the Bayes’ theorem and q0subscript𝑞0q\_{0} serves as the prior distribution. In fact, if the conditional distribution takes the following form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pX|Y∗​(x|y)∝exp⁡(V​(y)α−c​(x,y)α​β)proportional-tosuperscriptsubscript𝑝conditional𝑋𝑌conditional𝑥𝑦𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽\displaystyle p\_{X|Y}^{\*}(x|y)\propto\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right) |  | (26) |

Then the Bayes’ theorem states that

|  |  |  |  |
| --- | --- | --- | --- |
|  | pY|X∗​(y|x)=superscriptsubscript𝑝conditional𝑌𝑋conditional𝑦𝑥absent\displaystyle p\_{Y|X}^{\*}(y|x)= | pX|Y∗​(x|y)​q0​(y)𝖤Y​(pX|Y∗​(x|⋅)​q0​(⋅))superscriptsubscript𝑝conditional𝑋𝑌conditional𝑥𝑦subscript𝑞0𝑦subscript𝖤𝑌superscriptsubscript𝑝conditional𝑋𝑌conditional𝑥⋅subscript𝑞0⋅\displaystyle\frac{p\_{X|Y}^{\*}(x|y)q\_{0}(y)}{\mathsf{E}\_{Y}\left(p\_{X|Y}^{\*}(x|\cdot)q\_{0}(\cdot)\right)} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | q0​(y)​exp⁡(V​(y)α−c​(x,y)α​β)∫Ωq0​(z)​exp⁡(V​(z)α−c​(x,z)α​β)​𝑑zsubscript𝑞0𝑦𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽subscriptΩsubscript𝑞0𝑧𝑉𝑧𝛼𝑐𝑥𝑧𝛼𝛽differential-d𝑧\displaystyle\frac{q\_{0}(y)\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right)}{\int\_{\Omega}q\_{0}(z)\exp\left(\frac{V(z)}{\alpha}-\frac{c(x,z)}{\alpha\beta}\right)dz} |  | (27) |

which is the posterior distribution of Y𝑌Y given the observation X=x𝑋𝑥X=x. Now if we observe a distribution p​(x)𝑝𝑥p(x) over X𝑋X, then we may infer the distribution of Y𝑌Y to be

|  |  |  |  |
| --- | --- | --- | --- |
|  | q∗​(y)=superscript𝑞𝑦absent\displaystyle q^{\*}(y)= | ∫Ωp​(x)​pY|X∗​(y|x)​𝑑xsubscriptΩ𝑝𝑥superscriptsubscript𝑝conditional𝑌𝑋conditional𝑦𝑥differential-d𝑥\displaystyle\int\_{\Omega}p(x)p\_{Y|X}^{\*}(y|x)dx |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | ∫Ω𝑑x​p​(x)​q0​(z)​exp⁡(V​(y)α−c​(x,y)α​β)∫Ωq0​(y)​exp⁡(V​(z)α−c​(x,z)α​β)​𝑑zsubscriptΩdifferential-d𝑥𝑝𝑥subscript𝑞0𝑧𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽subscriptΩsubscript𝑞0𝑦𝑉𝑧𝛼𝑐𝑥𝑧𝛼𝛽differential-d𝑧\displaystyle\int\_{\Omega}dx\frac{p(x)q\_{0}(z)\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right)}{\int\_{\Omega}q\_{0}(y)\exp\left(\frac{V(z)}{\alpha}-\frac{c(x,z)}{\alpha\beta}\right)dz} |  | (28) |

which is exactly the worst-case distribution given in Eq. [25](#S3.E25 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance").

The connection between the Bayes’ theorem and Eq. [25](#S3.E25 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") is not just a coincidence.
In fact, the worst-case distribution of Y𝑌Y, given in Eq. [3.4](#S3.Ex8 "3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), can be regarded as the posterior distribution of a latent variable. On the other hand, the reference model of X𝑋X, given by p​(x)𝑝𝑥p(x), is considered as the distribution that is actually observed.
Assuming no reference model exists (i.e. no observation on X𝑋X has been made), then our best guess on the latent variable Y𝑌Y is given solely by its prior distribution q0​(y)subscript𝑞0𝑦q\_{0}(y). Now if the observable variable X𝑋X does take a particular value x𝑥x, then we need to update our estimation according to the Bayes’ theorem (Eq. [3.4](#S3.Ex7 "3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance")). The conditional probability density pX|Y∗​(x|y)superscriptsubscript𝑝conditional𝑋𝑌conditional𝑥𝑦p\_{X|Y}^{\*}(x|y) takes the form of Eq. [26](#S3.E26 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), reflecting the fact that the observable variable X𝑋X and the latent variable Y𝑌Y are not far apart. Imagining that we generate a sampling set {xi}subscript𝑥𝑖\{x\_{i}\} following the nominal distribution p​(x)𝑝𝑥p(x), then for each xisubscript𝑥𝑖x\_{i} we get a posterior distribution pY|X∗​(y|xi)superscriptsubscript𝑝conditional𝑌𝑋conditional𝑦subscript𝑥𝑖p\_{Y|X}^{\*}(y|x\_{i}) from Eq. [3.4](#S3.Ex7 "3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"). Overall, the best estimation of the distribution over the latent variable Y𝑌Y results from the aggregation of these posterior distributions. This is achieved by averaging them weighted by their probabilities p​(xi)𝑝subscript𝑥𝑖p(x\_{i}), as given in Eq. [3.4](#S3.Ex8 "3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"). This leads to the Bayesian interpretation of the model risk measurement, which concludes that by “observing” the reference model p​(x)𝑝𝑥p(x) over the observable variable X𝑋X, the worst-case model is given by updating the distribution of the latent variable Y𝑌Y, from the prior distribution q0​(y)subscript𝑞0𝑦q\_{0}(y) to the posterior distribution q∗​(y)superscript𝑞𝑦q^{\*}(y).

Table 2: Worst-case density function with prior q0subscript𝑞0q\_{0} at different (α,β)𝛼𝛽(\alpha,\beta) combinations. p𝑝p is the nominal distribution. δ𝛿\delta denotes the Dirac δ𝛿\delta-function and T∗superscript𝑇T^{\*} is the transportation map given by Eq. [15](#S3.E15 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance").

|  | α=0𝛼0\alpha=0 | α𝛼\alpha | α→∞→𝛼\alpha\to\infty |
| --- | --- | --- | --- |
| β=0𝛽0\beta=0 | p​(x)𝑝𝑥p(x) | | |
| β𝛽\beta | p​(T−∗1​(x))/|JT|p(T^{{}^{\*}-1}(x))/|J\_{T}| | given by Eq. [25](#S3.E25 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") | →q0​(x)→absentsubscript𝑞0𝑥\to q\_{0}(x) |
| β→∞→𝛽\beta\to\infty | δ​(x−arg⁡max⁡V​(x))𝛿𝑥𝑉𝑥\delta(x-\arg\max V(x)) | ∝q0​(x)​eV​(x)/αproportional-toabsentsubscript𝑞0𝑥superscript𝑒𝑉𝑥𝛼\propto q\_{0}(x)e^{V(x)/\alpha} |

If we know nothing about the reference model, setting the prior q0subscript𝑞0q\_{0} to a uniform distribution seems to make the most sense (because a uniform distribution maximizes the entropy thus containing least information). This leads to the main result given by Eq. [21](#S3.E21 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"). However, it is sometimes much more convenient to choose a prior other than the uniform distribution.
A particular interesting case is to set q0subscript𝑞0q\_{0} the same as the nominal distribution p𝑝p. In this case, the limit of β→∞→𝛽\beta\to\infty (complete relaxation of the transportation constraint) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | q∗​(x)=p​(x)​eθ​V​(x)∫Ωp​(x)​eθ​V​(x)​𝑑xsuperscript𝑞𝑥𝑝𝑥superscript𝑒𝜃𝑉𝑥subscriptΩ𝑝𝑥superscript𝑒𝜃𝑉𝑥differential-d𝑥\displaystyle q^{\*}(x)=\frac{p(x)e^{\theta V(x)}}{\int\_{\Omega}p(x)e^{\theta V(x)}dx} |  | (29) |

where we replace the parameter α−1superscript𝛼1\alpha^{-1} by θ𝜃\theta. This limit is exactly the worst-case distribution given by the relative entropy approach [[7](#bib.bib7)]. Despite of the simplicity of Eq. [29](#S3.E29 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), it is not recommended to set q0=psubscript𝑞0𝑝q\_{0}=p because by doing so we lose the capability of altering the support of the reference measure.

In practice, a common problem of the relative entropy approach is that the denominator in Eq. [21](#S3.E21 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") may not be integrable. To see this point, we examine the worst-case density function under the relative entropy approach:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qK​L∗​(x)∝p​(x)​eθ​V​(x)proportional-tosubscriptsuperscript𝑞𝐾𝐿𝑥𝑝𝑥superscript𝑒𝜃𝑉𝑥\displaystyle q^{\*}\_{KL}(x)\propto p(x)e^{\theta V(x)} |  | (30) |

The RHS of Eq. [30](#S3.E30 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") may not be integrable if V​(x)𝑉𝑥V(x) increases too fast (or p​(x)𝑝𝑥p(x) decays too slowly as in the cases of heavy tails). As an example, we consider the worst-case variance problem where V​(x)=x2𝑉𝑥superscript𝑥2V(x)=x^{2}. If the reference model follows an exponential distribution, then Eq. [30](#S3.E30 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") is not integrable.

Using the proposed Wasserstein approach, however, the flexibility of choosing a proper prior q0subscript𝑞0q\_{0} helps us to bypass this issue. In fact, one may choose a prior distribution q0subscript𝑞0q\_{0}, different from the nominal distribution p𝑝p, to guarantee that it decays sufficiently fast.
According to Eq. [3.4](#S3.Ex7 "3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), all we need to guarantee is that

|  |  |  |  |
| --- | --- | --- | --- |
|  | q0​(y)​exp⁡(V​(y)α−c​(x,y)α​β)subscript𝑞0𝑦𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽\displaystyle q\_{0}(y)\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right) |  | (31) |

is integrable w.r.t y𝑦y.
Fortunately, it is always possible to find some q0subscript𝑞0q\_{0} that satisfies this criteria.
As a simple choice, we may set q0​(y)∝e−V​(y)/αproportional-tosubscript𝑞0𝑦superscript𝑒𝑉𝑦𝛼q\_{0}(y)\propto e^{-V(y)/\alpha} to ensure the integrability. Such choice makes Eq. [31](#S3.E31 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") proportional to

|  |  |  |  |
| --- | --- | --- | --- |
|  | exp⁡(−c​(x,y)α​β)𝑐𝑥𝑦𝛼𝛽\displaystyle\exp\left(-\frac{c(x,y)}{\alpha\beta}\right) |  | (32) |

We suppose that the state space ΩΩ\Omega is an Euclidean space with finite dimension and the transportation cost c​(x,y)𝑐𝑥𝑦c(x,y) is given by its Euclidean distance. Then for all x∈Ω𝑥Ωx\in\Omega Eq. [32](#S3.E32 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") is integrable w.r.t y𝑦y, for the integrand diminishes exponentially when y𝑦y moves away from x𝑥x.

In summary, formulating the problem using the relative entropy constraint Eq. [24](#S3.E24 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") allows for flexibility of choosing a prior distribution q0subscript𝑞0q\_{0}. This is practically useful as one can avoid integrability issue by selecting a proper prior. This flexibility is not shared by the relative entropy approach as in Glasserman and Xu [[7](#bib.bib7)], which is regarded as a special case where the prior q0subscript𝑞0q\_{0} equals the nominal distribution p𝑝p.

## 4 Application

### 4.1 Jump risk under a diffusive reference model

We start from a price process that takes the form of a geometric Brownian motion

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=μ​St​d​t+σ​St​d​Wt𝑑subscript𝑆𝑡𝜇subscript𝑆𝑡𝑑𝑡𝜎subscript𝑆𝑡𝑑subscript𝑊𝑡\displaystyle dS\_{t}=\mu S\_{t}dt+\sigma S\_{t}dW\_{t} |  | (33) |

The logarithmic return at time T𝑇T follows a normal distribution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x:=ln⁡(STS0)∼𝒩​((μ−σ22)​T,σ2​T)assign𝑥subscript𝑆𝑇subscript𝑆0similar-to𝒩𝜇superscript𝜎22𝑇superscript𝜎2𝑇\displaystyle x:=\ln\left(\frac{S\_{T}}{S\_{0}}\right)\sim\mathcal{N}\left(\left(\mu-\frac{\sigma^{2}}{2}\right)T,\sigma^{2}T\right) |  | (34) |

When the volatility reaches zero, the return becomes deterministic and the distribution density is

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(x)=limσ→012​π​T​σ​e−[x−(μ−σ2/2)​T]22​σ2​T=δ​(x−μ​T)𝑝𝑥subscript→𝜎012𝜋𝑇𝜎superscript𝑒superscriptdelimited-[]𝑥𝜇superscript𝜎22𝑇22superscript𝜎2𝑇𝛿𝑥𝜇𝑇\displaystyle p(x)=\lim\_{\sigma\to 0}\frac{1}{\sqrt{2\pi T}\sigma}e^{-\frac{[x-(\mu-\sigma^{2}/2)T]^{2}}{2\sigma^{2}T}}=\delta(x-\mu T) |  | (35) |

In the case, model risk cannot be quantified using f𝑓f-divergence. In fact, the reference measure is a Dirac measure therefore no equivalent alternative measure exists. Under the KL divergence in particular, the worst-case measure is calculated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(x)​eθ​V​(x)∫Ωp​(x)​eθ​V​(x)​𝑑x=δ​(x−μ​T)𝑝𝑥superscript𝑒𝜃𝑉𝑥subscriptΩ𝑝𝑥superscript𝑒𝜃𝑉𝑥differential-d𝑥𝛿𝑥𝜇𝑇\displaystyle\frac{p(x)e^{\theta V(x)}}{\int\_{\Omega}p(x)e^{\theta V(x)}dx}=\delta(x-\mu T) |  | (36) |

which is the same as the reference measure. This is consistent with the Girsanov theorem for diffusion processes which states that the drift term is altered by some amount proportional to the volatility, i.e. μ~=μ−λ​σ~𝜇𝜇𝜆𝜎\tilde{\mu}=\mu-\lambda\sigma. When the volatility under the reference model decreases to zero, the alternative measure becomes identical to the reference measure.

Approaches based on f𝑓f-divergence excludes the existence of model risk given a zero volatility. This is, however, not true in practice, as the nominal diffusion process may still “regime-switch” to some discontinuous process. In fact, to quantify risks, one usually take into account the possibility of discontinuous changes of state variables (i.e. “jumps”). Using the Wasserstein approach, quantifying such jump risk becomes possible, even if the reference model is based on a pure diffusion process. Substituting Eq. [35](#S4.E35 "In 4.1 Jump risk under a diffusive reference model ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") into Eq. [21](#S3.E21 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") gives the worst-case distribution (see Appendix C for details)

|  |  |  |  |
| --- | --- | --- | --- |
|  | qW​(x)=exp⁡(V​(x)α−c​(x,μ​T)α​β)∫Ωexp⁡(V​(y)α−c​(y,μ​T)α​β)​𝑑ysubscript𝑞𝑊𝑥𝑉𝑥𝛼𝑐𝑥𝜇𝑇𝛼𝛽subscriptΩ𝑉𝑦𝛼𝑐𝑦𝜇𝑇𝛼𝛽differential-d𝑦\displaystyle q\_{W}(x)=\frac{\exp\left(\frac{V(x)}{\alpha}-\frac{c(x,\mu T)}{\alpha\beta}\right)}{\int\_{\Omega}\exp\left(\frac{V(y)}{\alpha}-\frac{c(y,\mu T)}{\alpha\beta}\right)dy} |  | (37) |

Notice that Eq. [37](#S4.E37 "In 4.1 Jump risk under a diffusive reference model ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") is suitable for any application where the reference model is given by a Dirac measure. Under f𝑓f-divergence, the limitation to equivalent measures keeps the reference model unchanged. The Wasserstein approach, on the other hand, relaxes such limitation, allowing for a worst-case model that differs from a Dirac measure. This allows us to measure risk in variables assumed to be deterministic in the reference model. A particularly interesting example is the quadratic variation process, which is deemed as deterministic under the Black-Scholes model. We will discuss this in detail later with regard to the model risk in dynamic hedging.

To illustrate Eq. [37](#S4.E37 "In 4.1 Jump risk under a diffusive reference model ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"), we consider the expected value of x𝑥x under the worst-case scenario. This problem is formulated using Eq. [6](#S3.E6 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") with a linear loss function V​(x)=x𝑉𝑥𝑥V(x)=x. We further assume a quadratic transportation cost function c​(x,y)=(x−y)2𝑐𝑥𝑦superscript𝑥𝑦2c(x,y)=(x-y)^{2}. The worst-case distribution given by Eq. [37](#S4.E37 "In 4.1 Jump risk under a diffusive reference model ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") turns out to be

|  |  |  |  |
| --- | --- | --- | --- |
|  | qW​(x)=1π​α​β​e−(x−μ​T−β/2)2α​βsubscript𝑞𝑊𝑥1𝜋𝛼𝛽superscript𝑒superscript𝑥𝜇𝑇𝛽22𝛼𝛽\displaystyle q\_{W}(x)=\frac{1}{\sqrt{\pi\alpha\beta}}e^{-\frac{\left(x-\mu T-\beta/2\right)^{2}}{\alpha\beta}} |  | (38) |

One can see that the worst-case scenario is associated with a constant shift of the mean (by −β/2𝛽2-\beta/2), even if the reference measure is deterministic (i.e. Dirac). The change in mean is also associated with a proportional variance (i.e. α​β/2𝛼𝛽2\alpha\beta/2), if α𝛼\alpha is assigned a positive value. The resulting normal distribution, with a finite variance, is a reflection of model ambiguity. This is in contrast with approaches based on f𝑓f-divergences, which are incapable of altering the reference model in this case, as its support includes only a single point.

### 4.2 Volatility Risk and Variance Risk

In this section, we consider the risk of volatility uncertainty given the nominal Black-Scholes model. When an option approaches maturity, the reference measure (on the price of its underlying asset) becomes close to a Dirac measure. This is visualised by the normal distribution of return narrowing in a rate of t𝑡\sqrt{t}. When the time to maturity t→0→𝑡0t\to 0, the normal distribution shifts to a Dirac distribution with zero variance.

Under the Kullback-Leibler divergence (or any f𝑓f-divergence), any model risk vanishes when the reference model converges to a Dirac measure. As a result, on a short time to maturity a sufficient amount of variance uncertainty can only be produced with a large cost (parametrised by θ𝜃\theta). To illustrate this point, consider a normal distribution (say Eq. [35](#S4.E35 "In 4.1 Jump risk under a diffusive reference model ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") before taking the limit).
For the purpose of measuring the variance risk, we need to adopt a quadratic loss function V​(x)=x2𝑉𝑥superscript𝑥2V(x)=x^{2}. Under the Kullback-Leibler divergence, the variance of the worst-case distribution is given by [[7](#bib.bib7)]

|  |  |  |  |
| --- | --- | --- | --- |
|  | σK​L2​T=σ2​T1−2​θ​σ2​Tsuperscriptsubscript𝜎𝐾𝐿2𝑇superscript𝜎2𝑇12𝜃superscript𝜎2𝑇\displaystyle\sigma\_{KL}^{2}T=\frac{\sigma^{2}T}{1-2\theta\sigma^{2}T} |  | (39) |

When time to maturity T→0→𝑇0T\to 0, the worst-case volatility σK​L→σ→subscript𝜎𝐾𝐿𝜎\sigma\_{KL}\to\sigma with a fixed θ𝜃\theta.
This is not consistent with what we see in the market. In fact, with short time to maturity the fear of jumps can play an important role. Such fear of risks is priced into options and variance swaps termed as the volatility (or variance) risk premium.

![Refer to caption](/html/1809.03641/assets/empirical.png)


Fig 2: Worst-case volatility as a function of time under the (a) Wasserstein approach, (b) KL divergence.

The volatility (or variance) risk premium can be considered as the compensation paid to option sellers for bearing the volatility risks [[8](#bib.bib8), [9](#bib.bib9)]. It is practically quantified as the difference between the implied volatility (or variance) and the realised volatilty (or variance). As it is priced based on the volatility risk, its quantity is directly linked to the risk associated with the reference measure used to model the underlying asset. Therefore by analyzing the term structure of such premium, one can get some insight into the worst-case volatility risk. Under the assumption of diffusive price dynamics, Carr and Wu developed a formula for the at-the-money implied variance [[10](#bib.bib10)]. Illustrated in Fig. [2](#S4.F2 "Fig 2 ‣ 4.2 Volatility Risk and Variance Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"), the formula matches well with the empirical data [[11](#bib.bib11)] for maturities longer than 3 months. For maturities shorter than 3 months, however, the formula seems to underestimate the variance risk premium. Other empirical work also shows that option buyers consistently pay higher risk premium for shorter maturity options [[9](#bib.bib9)].

The underestimation of volatility risk premium on short maturity is an intrinsic problem with diffusive models. Indeed, the work mentioned above reveals the importance of quantifying jumps when time to maturity remains short. Other work shows that the risk premium due to jumps is fairly constant across different maturities [[12](#bib.bib12)]. This implies a very different time dependency from that due to continuous price moves (Eq. [39](#S4.E39 "In 4.2 Volatility Risk and Variance Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance")). In fact, any approach based on f𝑓f-divergence is incapable of producing sufficient model risk on t→0→𝑡0t\to 0, suggesting a decaying term structure of risk premium. On the other hand, the Wasserstein approach does not suffer from this issue. In fact, it produces a worst-case volatility that has little time dependence (Fig. [2](#S4.F2 "Fig 2 ‣ 4.2 Volatility Risk and Variance Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance")). Therefore, the Wasserstein approach provides a particularly useful tool for managing the variance risk and quantifying its risk premium on short time to maturity.

With the Wasserstein approach, the worst-case variance takes the form of (see Appendix B)

|  |  |  |  |
| --- | --- | --- | --- |
|  | σW2​T=σ2​T(1−β)2+α​β2​(1−β)superscriptsubscript𝜎𝑊2𝑇superscript𝜎2𝑇superscript1𝛽2𝛼𝛽21𝛽\displaystyle\sigma\_{W}^{2}T=\frac{\sigma^{2}T}{(1-\beta)^{2}}+\frac{\alpha\beta}{2(1-\beta)} |  | (40) |

The Wasserstein approach provides a worst-case variance that is independent of the time to maturity. It scales the nominal variance by a constant factor (1−β)−2superscript1𝛽2(1-\beta)^{-2}. In addition, it introduces a constant extra variance α​β/(1−β)𝛼𝛽1𝛽\alpha\beta/(1-\beta). The extra variance term is modulated by the parameter α𝛼\alpha. If we set α𝛼\alpha to zero, then the worst-case volatility σWsubscript𝜎𝑊\sigma\_{W} is merely a constant amplification of the nominal volatility σ𝜎\sigma.
This model risk measure, however, may not be sufficient if the nominal volatility is very close to zero. The extra variance term serves to account for the extra risks (e.g. jumps) that are not captured by the nominal volatility.

### 4.3 Model Risk in Portfolio Variance

The Wasserstein approach can be applied to quantify the risk associated with modelling the variance of a portfolio, assuming the asset returns follow a multivariate normal distribution. Suppose there are n𝑛n assets under consideration and their returns are reflected by a state vector x𝑥x: x∈𝒱𝑥𝒱x\in\mathcal{V} where 𝒱𝒱\mathcal{V} is a n-dimensional vector space. For generality, we consider the following target function V:𝒱→ℝ+:𝑉→𝒱subscriptℝV:\mathcal{V}\to\mathbb{R}\_{+}

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x)=xT​A​x𝑉𝑥superscript𝑥𝑇𝐴𝑥\displaystyle V(x)=x^{T}Ax |  | (41) |

where A𝐴A is a positive-definite symmetric matrix. If we replace x𝑥x by x′=x−𝖤​(x)superscript𝑥′𝑥𝖤𝑥x^{\prime}=x-\mathsf{E}(x) and A𝐴A by w​wT𝑤superscript𝑤𝑇ww^{T}, then the expected value of the target function reflects the portfolio variance:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤​[V​(x)]=𝖤​(xT​w​wT​x)=wT​Σ​w𝖤delimited-[]𝑉𝑥𝖤superscript𝑥𝑇𝑤superscript𝑤𝑇𝑥superscript𝑤𝑇Σ𝑤\displaystyle\mathsf{E}[V(x)]=\mathsf{E}(x^{T}ww^{T}x)=w^{T}\Sigma w |  | (42) |

where w𝑤w is the vector of compositions in the portfolio. ΣΣ\Sigma is the covariance matrix of the normally distributed asset returns (under the reference model).

To find the worst-case model using the Wasserstein approach, we need to first define a metric in the vector space 𝒱𝒱\mathcal{V}. Suppose the vector space is equipped by a norm ‖x‖norm𝑥||x|| then the metric is naturally defined by c​(x,y)=‖x−y‖𝑐𝑥𝑦norm𝑥𝑦c(x,y)=||x-y||. Here we focus on the kind of norm that has an inner-product structure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖x‖=xT​B​x,∀x∈𝒱formulae-sequencenorm𝑥superscript𝑥𝑇𝐵𝑥for-all𝑥𝒱\displaystyle||x||=\sqrt{x^{T}Bx},~{}\forall x\in\mathcal{V} |  | (43) |

where B𝐵B is a positive-definite symmetric matrix (constant metric tensor). The resulting worst-case distribution is still multivariate normal, with the vector of means and covariance matrix replaced by (see Appendix D for derivation)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μW=subscript𝜇𝑊absent\displaystyle\mu\_{W}= | (B−β​A)−1​B​μsuperscript𝐵𝛽𝐴1𝐵𝜇\displaystyle(B-\beta A)^{-1}B\mu |  | (44) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΣW=subscriptΣ𝑊absent\displaystyle\Sigma\_{W}= | (B−β​A)−1​B​Σ​B​(B−β​A)−1+α​β2​(B−β​A)−1superscript𝐵𝛽𝐴1𝐵Σ𝐵superscript𝐵𝛽𝐴1𝛼𝛽2superscript𝐵𝛽𝐴1\displaystyle(B-\beta A)^{-1}B\Sigma B(B-\beta A)^{-1}+\frac{\alpha\beta}{2}(B-\beta A)^{-1} |  | (45) |

Apart from a constant term that vanishes if assigning zero to the parameter α𝛼\alpha, the worst-case distribution is transformed from the nominal distribution via a measure-preserving linear map (see Appendix D). This result is more intuitive than the result obtained using the KL divergence, given by [[7](#bib.bib7)]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μK​L=subscript𝜇𝐾𝐿absent\displaystyle\mu\_{KL}= | (I−2​θ​Σ​A)−1​μsuperscript𝐼2𝜃Σ𝐴1𝜇\displaystyle(I-2\theta\Sigma A)^{-1}\mu |  | (46) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΣK​L=subscriptΣ𝐾𝐿absent\displaystyle\Sigma\_{KL}= | (I−2​θ​Σ​A)−1​Σsuperscript𝐼2𝜃Σ𝐴1Σ\displaystyle(I-2\theta\Sigma A)^{-1}\Sigma |  | (47) |

Fig. [3](#S4.F3 "Fig 3 ‣ 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") provides an example illustrating that the worst-case distribution is indeed a measure-preserving transform with the Wasserstein approach.

![Refer to caption](/html/1809.03641/assets/nominaltwo.png)

![Refer to caption](/html/1809.03641/assets/kltwo.png)

![Refer to caption](/html/1809.03641/assets/wtwo.png)

Fig 3: Multivariate nominal distributions (a) reference model, (b) worst case under the KL divergence, (c) worst case under the Wasserstein approach (as a measure-preserving transform).

The constant term reflects residual uncertainty when the reference model has vanishing variances. This term is especially useful when some of the assets are perfectly correlated (either 1 or -1) and the vector space 𝒱𝒱\mathcal{V} is not fully supported by the reference measure. In this case, the Wasserstein approach provides results that differ significantly from the f𝑓f-divergence approach. In particular, approaches based on KL divergence (or any f-divergences) cannot alter the support, they merely reweight the states within the support. This is illustrated in Fig. [4](#S4.F4 "Fig 4 ‣ 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"), where two assets are perfectly correlated. The reference model shown in (a) provides a measure supported by a one-dimensional vector subspace of 𝒱𝒱\mathcal{V}. The worst-case measure under the KL divergence is supported by the same subspace, as illustrated in (b). This conclusion can actually be derived from the worst-case measure given by Eq. [47](#S4.E47 "In 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") (see Appendix E for proof).

On the other hand, the Wasserstein approach is capable of examining measures supported by other vector subspaces. We first ignore the constant variance term by setting α𝛼\alpha to zero in Eq. [45](#S4.E45 "In 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"). The Wasserstein approach “rotates” the original support by applying linear maps to the reference measure. In the case illustrated by Fig. [4](#S4.F4 "Fig 4 ‣ 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance")(c), essentially all measures supported by a one-dimensional vector subspace are within the scope of the approach (see Appendix F for proof). Among those measures the Wasserstein approach picks the worst one, supported by a vector subspace different from the original one. It essentially searches for the optimal transform over the entire space. In practice, we may want to account for the risk associated with the assumption of perfect correlation. This is accomplished by assigning positive value to α𝛼\alpha, allowing the distribution to “diffuse” into the entire vector space as illustrated in Fig. [4](#S4.F4 "Fig 4 ‣ 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance")(d).

![Refer to caption](/html/1809.03641/assets/nominallow.png)

![Refer to caption](/html/1809.03641/assets/kllow.png)

![Refer to caption](/html/1809.03641/assets/wlow.png)

![Refer to caption](/html/1809.03641/assets/wlowdiff.png)

Fig 4: Multivariate nominal distributions (a) reference model, (b) worst case under the KL divergence, when the support is a low-dimensional subspace. Worst-case multivariate nominal distributions under the Wasserstein approach (c) θ=0𝜃0\theta=0 (d) θ=0.5𝜃0.5\theta=0.5.

It is worthwhile noting that the Wasserstein approach also has a practical advantage over the approach based on KL divergence. If we examine the worst-case variances resulting from the two approaches, Eq. [45](#S4.E45 "In 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") and [47](#S4.E47 "In 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"), we can find that their positive definiteness is not guaranteed. This requires practitioners to carefully parametrise either approach to ensure the positive definiteness. However, under KL divergence the positive definiteness is dependent on the original covariance matrix. This makes it harder to parametrise and generalise the approach. In cases where the asset returns have time-varying correlations, one may need to switch parameters (θ𝜃\theta) to ensure a positive definite matrix. On the other hand, the Wasserstein approach only requires B−β​A𝐵𝛽𝐴B-\beta A to be positive-definite, independent of the covariance matrix ΣΣ\Sigma. The reference probability measure thus no longer affects the feasibility of quantifying the worst-case risk.

### 4.4 Robust Portfolio Optimisation and Correlation Risk

In modern portfolio theory, one considers n𝑛n securities with the excess logarithmic returns following a multivariate normally distribution, i.e. X∼𝒩​(μ,Σ)similar-to𝑋𝒩𝜇ΣX\sim\mathcal{N}(\mu,\Sigma). The standard mean-variance optimisation is formulated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | mina⁡aT​Σ​asubscript𝑎superscript𝑎𝑇Σ𝑎\displaystyle\min\_{a}a^{T}\Sigma a |  | (48) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t.μT​a=Cformulae-sequence𝑠𝑡superscript𝜇𝑇𝑎𝐶\displaystyle s.t.\mu^{T}a=C |  | (49) |

where a∈ℝn𝑎superscriptℝ𝑛a\in\mathbb{R}^{n} is the vector of portfolio weights. It can take any values assuming it is always possible to borrow or lend at the risk-free rate, and to short sell any asset. The problem is solved by introducing a Lagrange multiplier λ𝜆\lambda:

|  |  |  |  |
| --- | --- | --- | --- |
|  | a∗=λ2​Σ−1​μsuperscript𝑎𝜆2superscriptΣ1𝜇\displaystyle a^{\*}=\frac{\lambda}{2}\Sigma^{-1}\mu |  | (50) |

The optimal portfolio weight a∗superscript𝑎a^{\*} depends on λ𝜆\lambda. However, the Sharpe ratio of the optimal portfolio is independent of λ𝜆\lambda:

|  |  |  |  |
| --- | --- | --- | --- |
|  | a∗T​μa∗T​Σ​a∗=μT​Σ−1​μsuperscript𝑎absent𝑇𝜇superscript𝑎absent𝑇Σsuperscript𝑎superscript𝜇𝑇superscriptΣ1𝜇\displaystyle\frac{a^{\*T}\mu}{\sqrt{a^{\*T}\Sigma a^{\*}}}=\sqrt{\mu^{T}\Sigma^{-1}\mu} |  | (51) |

The reference model assumes a multivariate normal distribution 𝒩​(μ,Σ)𝒩𝜇Σ\mathcal{N}(\mu,\Sigma). The worst-case model is an alternative measure dependent on the security positions a𝑎a. To formulate the problem of worst-case measure, we may first express the mean-variance optimisation problem by

|  |  |  |  |
| --- | --- | --- | --- |
|  | mina⁡E​[(x−μ)T​a​aT​(x−μ)−λ​xT​a]subscript𝑎𝐸delimited-[]superscript𝑥𝜇𝑇𝑎superscript𝑎𝑇𝑥𝜇𝜆superscript𝑥𝑇𝑎\displaystyle\min\_{a}E\left[(x-\mu)^{T}aa^{T}(x-\mu)-\lambda x^{T}a\right] |  | (52) |

where the expectation is taken under the reference measure. Taking into account the model risk, we may formulate a robust version of Eq. [52](#S4.E52 "In 4.4 Robust Portfolio Optimisation and Correlation Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") that is consistent with literature work [[7](#bib.bib7)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | mina⁡maxQ∈ℳ⁡EQ​[(X−μ)T​a​aT​(X−μ)−λ​XT​a]subscript𝑎subscript𝑄ℳsuperscript𝐸𝑄delimited-[]superscript𝑋𝜇𝑇𝑎superscript𝑎𝑇𝑋𝜇𝜆superscript𝑋𝑇𝑎\displaystyle\min\_{a}\max\_{Q\in\mathscr{M}}E^{Q}\left[(X-\mu)^{T}aa^{T}(X-\mu)-\lambda X^{T}a\right] |  | (53) |

where ℳℳ\mathscr{M} is the space of alternative measures constrained by different criteria. For the approached based on the Kullback-Leibler divergence, the constraint is given by a maximum amount of relative entropy w.r.t the reference model (i.e. relative entropy budget). Under the Wasserstein approach, the constraints are given by Eq. [12](#S3.E12 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") and [16](#S3.E16 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance").

To solve the inner problem of Eq. [53](#S4.E53 "In 4.4 Robust Portfolio Optimisation and Correlation Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"), we may further simplify the problem to

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | maxQ∈ℳ⁡EQ​[(X−μ)T​a​aT​(X−μ)−λ​XT​a]subscript𝑄ℳsuperscript𝐸𝑄delimited-[]superscript𝑋𝜇𝑇𝑎superscript𝑎𝑇𝑋𝜇𝜆superscript𝑋𝑇𝑎\displaystyle\max\_{Q\in\mathscr{M}}E^{Q}\left[(X-\mu)^{T}aa^{T}(X-\mu)-\lambda X^{T}a\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | maxQ∈ℳ⁡EQ​[(X−μ−k)T​a​aT​(X−μ−k)]−λ​μT​a−λ4subscript𝑄ℳsuperscript𝐸𝑄delimited-[]superscript𝑋𝜇𝑘𝑇𝑎superscript𝑎𝑇𝑋𝜇𝑘𝜆superscript𝜇𝑇𝑎𝜆4\displaystyle\max\_{Q\in\mathscr{M}}E^{Q}\left[(X-\mu-k)^{T}aa^{T}(X-\mu-k)\right]-\lambda\mu^{T}a-\frac{\lambda}{4} |  | (54) |

where k𝑘k is a vector that satisfies aT​k=λ/2superscript𝑎𝑇𝑘𝜆2a^{T}k=\lambda/2. It is noted that this is an approximation as the change of measure would also alter the mean from μ𝜇\mu to μ′superscript𝜇′\mu^{\prime}. The variance should be calculated by EQ​(m)​[(X−μ′)T​a​aT​(X−μ′)]superscript𝐸𝑄𝑚delimited-[]superscript𝑋superscript𝜇′𝑇𝑎superscript𝑎𝑇𝑋superscript𝜇′E^{Q(m)}\left[(X-\mu^{\prime})^{T}aa^{T}(X-\mu^{\prime})\right]. However, the difference is proportional to (μ′−μ)2superscriptsuperscript𝜇′𝜇2(\mu^{\prime}-\mu)^{2} and is thus secondary on a small change of measure (i.e. β≪1much-less-than𝛽1\beta\ll 1). The solution to Eq. [53](#S4.E53 "In 4.4 Robust Portfolio Optimisation and Correlation Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") is also multivariate normal under both KL divergence (see Appendix G) and under the Wasserstein metric (see Appendix H).
The two approaches result in robust MVO portfolios with different weights (up to the first order w.r.t θ𝜃\theta or β𝛽\beta):

|  |  |  |  |
| --- | --- | --- | --- |
|  | aK​L∗=subscriptsuperscript𝑎𝐾𝐿absent\displaystyle a^{\*}\_{KL}= | (λ2−θ​λ32​(1+μT​Σ−1​μ))​Σ−1​μ𝜆2𝜃superscript𝜆321superscript𝜇𝑇superscriptΣ1𝜇superscriptΣ1𝜇\displaystyle\left(\frac{\lambda}{2}-\frac{\theta\lambda^{3}}{2}\left(1+\mu^{T}\Sigma^{-1}\mu\right)\right)\Sigma^{-1}\mu |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | aW∗=subscriptsuperscript𝑎𝑊absent\displaystyle a^{\*}\_{W}= | (λ2−β​λ34​μT​Σ−1​B−1​Σ−1​μ)​Σ−1​μ−β​λ34​(1+μT​Σ−1​μ)​Σ−1​B−1​Σ−1​μ𝜆2𝛽superscript𝜆34superscript𝜇𝑇superscriptΣ1superscript𝐵1superscriptΣ1𝜇superscriptΣ1𝜇𝛽superscript𝜆341superscript𝜇𝑇superscriptΣ1𝜇superscriptΣ1superscript𝐵1superscriptΣ1𝜇\displaystyle\left(\frac{\lambda}{2}-\frac{\beta\lambda^{3}}{4}\mu^{T}\Sigma^{-1}B^{-1}\Sigma^{-1}\mu\right)\Sigma^{-1}\mu-\frac{\beta\lambda^{3}}{4}\left(1+\mu^{T}\Sigma^{-1}\mu\right)\Sigma^{-1}B^{-1}\Sigma^{-1}\mu |  | (55) |

Comparing Eq. [4.4](#S4.Ex10 "4.4 Robust Portfolio Optimisation and Correlation Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") with the standard MVO portfolio given by Eq. [50](#S4.E50 "In 4.4 Robust Portfolio Optimisation and Correlation Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"), we can see that the robust MVO portfolios provide first-order corrections, resulting in more conservative asset allocation in general.

Despite of being more conservative, aK​L∗subscriptsuperscript𝑎𝐾𝐿a^{\*}\_{KL} is in fact parallel to the standard MVO portfolio a∗superscript𝑎a^{\*}. As a result, the robust MVO portfolio does not change the relative weights of component assets. In fact, all the weights are reduced by the same proportion (c<1𝑐1c<1) to account for model risk. This is, however, inappropriately accounts for the correlation risk. For example, two highly-correlated assets have extremely high weights in the nominal MVO portfolio. Because of the correlation risk, we would expect the robust MVO portfolio to assign them lower weights relative to other assets.
This is the case for aW∗subscriptsuperscript𝑎𝑊a^{\*}\_{W}. In fact, aW∗subscriptsuperscript𝑎𝑊a^{\*}\_{W} not only reduces the overall portfolio weights in order to be more conservative, but also adjusts the relative weights of component assets for a less extreme allocation. One may notice that the term inside the bracket of the expression for aW∗subscriptsuperscript𝑎𝑊a^{\*}\_{W} is a square matrix (see Eq. [4.4](#S4.Ex10 "4.4 Robust Portfolio Optimisation and Correlation Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance")), which serves to linearly transform the vector of portfolio weights. By adjusting their relative weights, Eq. [6.8](#S6.Ex66 "6.8 H. Robust MVO Portfolio (Wasserstein approach) ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") correctly accounts for the correlation risk (see Appendix H for details).

The robust optimal portfolio parametrised by λ𝜆\lambda allows us to plot the robust capital market line (CML). Unlike the standard CML, it is no longer a straight line and the Sharpe ratio is now dependent on λ𝜆\lambda.

![Refer to caption](/html/1809.03641/assets/composition.png)

![Refer to caption](/html/1809.03641/assets/klmv.png)

![Refer to caption](/html/1809.03641/assets/wasser.png)

Fig 5: The normalised optimal composition of a portfolio consisting of two securities, calculated by a∗superscript𝑎a^{\*} divided by λ/2𝜆2\lambda/2. The normalised optimal composition under the reference model is give by a constant vector Σ−1​μsuperscriptΣ1𝜇\Sigma^{-1}\mu, while those under the worst-case models are dependent on λ𝜆\lambda. In particular, the Kullback-Leibler approach reduces both compositions proportionally, while the Wasserstein approach reduces compositions in a nonlinear way.



![Refer to caption](/html/1809.03641/assets/klmv.png)

![Refer to caption](/html/1809.03641/assets/wasser.png)

Fig 6: Robust capital market lines (CMLs) using (a) the Kullback-Leibler divergence and (b) the Wasserstein approach.

Under the reference model, the optimal composition of a portfolio is given by λ​Σ−1​μ/2𝜆superscriptΣ1𝜇2\lambda\Sigma^{-1}\mu/2. The proportionality of this solution suggests that we should double the weights if the expected excess return doubles. However, this may end up with excessive risk due to increase of leverage. Model risk is the major source of risks here, as we are unsure if the expected excess return and the covariance matrix correctly reflects the return distribution in the future (for a given holding period). Since higher leverage implies more severe model risk, increasing leverage proportionally is in fact sub-optimal under the worst-case model.

Eq. [4.4](#S4.Ex10 "4.4 Robust Portfolio Optimisation and Correlation Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"), on the other hand, provides the optimal solutions under the respective model risk approaches. The robustness of these solutions allow the practitioners to allocate assets in a safer way. It is shown in Fig. [5](#S4.F5 "Fig 5 ‣ 4.4 Robust Portfolio Optimisation and Correlation Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") that the normalised optimal compositions reduce with λ𝜆\lambda. This is because a larger λ𝜆\lambda indicates higher leverage, and hence the optimal composition is reduced further away from that of the reference model. The normalised optimal compositions approach zero on the increase of λ𝜆\lambda.
In Fig. [5](#S4.F5 "Fig 5 ‣ 4.4 Robust Portfolio Optimisation and Correlation Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"), the compositions of both securities get reduced proportionally under the KL approach. Using the Wasserstein approach, on the other hand, allows the compositions to move in a non-parallel way.

In this example, we have two highly correlated (ρ=0.5𝜌0.5\rho=0.5) stocks but with very different expected excess returns (Stock 1 0.650.650.65 and Stock 2 −0.10.1-0.1). Because of the high correlation we can profit from taking the spread (long Stock 1 and short Stock 2). Under the reference model, taking the spread of a highly correlated pair does not add too much risk. However, the true risk could be underestimated due to the existence of model risk. The spread is more sensitive to model risk than an overall long position, and thus requires reduction when optimising with model risk. This point is well reflected by the non-linearity of the capital market line under the Wasserstein approach, showing sub-linear increase in excess return as risk (standard deviation) increases. We reduce the position of the spread more than the long position of Stock 1 (or the overall long position). In the KL approach, however, we reduce the spread position and the overall long position at the same pace.

The effect of robust optimality under the worst-case model is most significant when the reference model is close to having a low-dimensional support. A low-dimensional support means that the covariance matrix does not have the full rank. Put in a practical way, there exists a risk-free portfolio with non-zero compositions in risky assets. In this case, there is arbitrage opportunity that has close-to-zero risk but high excess returns. The optimal portfolio under the reference model could be unrealistically optimistic, i.e. the arbitrage opportunity might disappear in the face of model risk.

Fig. [5](#S4.F5 "Fig 5 ‣ 4.4 Robust Portfolio Optimisation and Correlation Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") illustrates an example of two securities with a high correlation. Under the reference model, the Sharpe ratio (slope of the excess return vs risk line) increases quickly with the correlation coefficient, demonstrated by the dashed lines in Fig. [6](#S4.F6 "Fig 6 ‣ 4.4 Robust Portfolio Optimisation and Correlation Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"). This results from taking excessive positions in the spread (long the one with higher Sharpe ratio and short the other). It is clear from Fig. [6](#S4.F6 "Fig 6 ‣ 4.4 Robust Portfolio Optimisation and Correlation Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") that the approach based on the Kullback-Leibler divergence cannot solve this issue systematically. In fact, when the correlation increases, the capital market line under the worst-case model is even closer to the nominal one. On the other hand, the Wasserstein approach does provide a more plausible adjustment. The robust capital market line given by the Wasserstein approach deviates more from the nominal straight line on an increasing correlation.

This difference is a direct result in their capabilities of altering the support of the reference measure. The KL approach cannot alter the support. So a spurious arbitrage relation under the reference measure may persist under the worst-case measure. On the other hand, the Wasserstein approach breaks the ostensible arbitrage opportunity by transforming the support to a different vector subspace.

### 4.5 Model Risk in Dynamic Hedging

The hedging error is measured by the absolute profit-and-loss (PnL) of a dynamically hedged option until its maturity. Using the Black-Scholes model as the reference model, the hedging risk decreases with the hedging frequency. Ideally if hedging is done continuously, then the hedging error is zero almost surely. This is true even under alternative measures, as long as they are equivalent to the reference model. The underlying reason is that the quadratic variation does not change under all equivalent measures. In fact, if we consider a geometric Brownian motion:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=μ​St​d​t+σ​St​d​Wt𝑑subscript𝑆𝑡𝜇subscript𝑆𝑡𝑑𝑡𝜎subscript𝑆𝑡𝑑subscript𝑊𝑡\displaystyle dS\_{t}=\mu S\_{t}dt+\sigma S\_{t}dW\_{t} |  | (56) |

The quadratic variation [ln⁡S]t=∫0tσs2​𝑑ssubscriptdelimited-[]𝑆𝑡superscriptsubscript0𝑡subscriptsuperscript𝜎2𝑠differential-d𝑠[\ln S]\_{t}=\int\_{0}^{t}\sigma^{2}\_{s}ds almost surely. Therefore the equation holds under all equivalent measures. Given the Black-Scholes price of an option Ct=C​(t,St)subscript𝐶𝑡𝐶𝑡subscript𝑆𝑡C\_{t}=C(t,S\_{t}), the PnL of a continuously hedged portfolio between time 00 and T𝑇T is

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∫0T𝑑Ct−∫0T∂Ct∂St​𝑑Stsuperscriptsubscript0𝑇differential-dsubscript𝐶𝑡superscriptsubscript0𝑇subscript𝐶𝑡subscript𝑆𝑡differential-dsubscript𝑆𝑡\displaystyle\int\_{0}^{T}dC\_{t}-\int\_{0}^{T}\frac{\partial C\_{t}}{\partial S\_{t}}dS\_{t} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | ∫0T(∂Ct∂t​d​t+St22​∂2Ct∂St2​d​[ln⁡S]t)=0superscriptsubscript0𝑇subscript𝐶𝑡𝑡𝑑𝑡superscriptsubscript𝑆𝑡22superscript2subscript𝐶𝑡superscriptsubscript𝑆𝑡2𝑑subscriptdelimited-[]𝑆𝑡0\displaystyle\int\_{0}^{T}\left(\frac{\partial C\_{t}}{\partial t}dt+\frac{S\_{t}^{2}}{2}\frac{\partial^{2}C\_{t}}{\partial S\_{t}^{2}}d[\ln S]\_{t}\right)=0 |  | (57) |

where the last equality results from the Black-Scholes partial differential equation.

Since any f𝑓f-divergence is only capable of searching over equivalent alternative measures, the worst-case hedging error given by these approaches has to be zero on continuous hedging frequency.
One can image that as hedging frequency increases, the worst-case hedging risk decreases towards zero (Fig. [7](#S4.F7 "Fig 7 ‣ 4.5 Model Risk in Dynamic Hedging ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance")(b)). This is, however, inconsistent with practitioners’ demand for risk management. In fact, if the volatility of the underlying asset differs from the nominal volatility, then Eq. [4.5](#S4.Ex11 "4.5 Model Risk in Dynamic Hedging ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") no longer holds. Such volatility uncertainty is a major source of hedging risk, and thus has to be measured and managed properly. The most straightforward way of doing that is to assume a distribution of volatility, and then run a Monte Carlo simulation to quantify the hedging error (Fig. [7](#S4.F7 "Fig 7 ‣ 4.5 Model Risk in Dynamic Hedging ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance")(a)).

![Refer to caption](/html/1809.03641/assets/volhedge.png)

![Refer to caption](/html/1809.03641/assets/klhedge.png)

Fig 7: (a) Worst-case hedging risk under the KL divergence, and (b) hedging risk simulated by randomly sampling volatilities.

Despite of its simplicity, volatility sampling is a parametric approach, for it is only capable of generating alternative Black-Scholes models with different parameter. This approach cannot account for alternatives such as local volatility models or stochastic volatility models. This calls for a non-parametric approach relying on the formulation given in Eq. [6](#S3.E6 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance").

We have already seen that using approaches based on f𝑓f-divergence one cannot correctly quantify the hedging risk.
The Wasserstein approach, on the other hand, does not have this issue, for it is capable of searching over non-equivalent measures.
Using Monte Carlo simulation, we obtain the worst-case hedging risk under the Wasserstein approach (see Fig. [8](#S4.F8 "Fig 8 ‣ 4.5 Model Risk in Dynamic Hedging ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance")). Compared to the approach based on Kullback-Leibler divergence (Fig. [7](#S4.F7 "Fig 7 ‣ 4.5 Model Risk in Dynamic Hedging ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance")(b)), the hedging risk given by the Wasserstein approach is more consistent with the simulated results using volatility sampling (Fig. [7](#S4.F7 "Fig 7 ‣ 4.5 Model Risk in Dynamic Hedging ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance")(a)). In the limit of continuous hedging, the Wasserstein approach results in a worst-case risk slightly higher than volatility sampling, for it may involve jumps that cannot be hedged.

![Refer to caption](/html/1809.03641/assets/whedge.png)


Fig 8: (a) Worst-case hedging risk under the Wasserstein approach.

In practice, the Wasserstein approach requires some tricks as fully sampling the infinite-dimensional path space is impossible. Therefore only paths close to the sampled paths (under the reference measure) are sampled, as the importance of an alternative path decays exponentially with its distance to these sampled paths. This point is shown in Fig. [9](#S4.F9 "Fig 9 ‣ 4.5 Model Risk in Dynamic Hedging ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance")(a), in which the alternative paths are illustrated by the crosses close to the nominal sampled paths (dots). By increasing the average distance of the alternative paths to the nominal paths, the hedging risk is increased until convergence (Fig. [9](#S4.F9 "Fig 9 ‣ 4.5 Model Risk in Dynamic Hedging ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance")(b)).

![Refer to caption](/html/1809.03641/assets/samplehedge.png)

![Refer to caption](/html/1809.03641/assets/convhedge.png)

Fig 9: (a) Sample paths generated for the Wasserstein approach, (b) convergence of the worst-case hedging risk.

Here we list the procedure of the Monte Carlo simulation described in the last paragraph:
  
1. create N𝑁N sample paths from the reference model
  
2. For each sample paths, create M𝑀M sample paths by deviating Xtsubscript𝑋𝑡X\_{t} by a normally distributed random variable 𝒩​(0,σ2)𝒩0superscript𝜎2\mathcal{N}(0,\sigma^{2})
  
3. collect all M​N𝑀𝑁MN sample paths and the original N𝑁N paths, we have N​(M+1)𝑁𝑀1N(M+1) points in the path space. Calculate the hedging error for each of the N​(M+1)𝑁𝑀1N(M+1) paths.
  
4. Apply Eq. [21](#S3.E21 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") to calculate the worst-case probability of each path where d​(X,Y)=[X−Y]𝑑𝑋𝑌delimited-[]𝑋𝑌d(X,Y)=[X-Y].
  
5. To find the (worst-case) hedging risk, we average the hedging errors of all N​(M+1)𝑁𝑀1N(M+1) paths, weighted by their worst-case probabilities.
  
6. Repeat steps 2-5 with a larger σ2superscript𝜎2\sigma^{2}. Continue to increase the deviation until the calculated hedging risk converges (Fig. [9](#S4.F9 "Fig 9 ‣ 4.5 Model Risk in Dynamic Hedging ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance")(b)).

## 5 Conclusion

Non-parametric approaches to model risk measurement are theoretically sound and practically feasible. Adopting the Wasserstein distance allows us to further extend the range of legitimate measures from merely the absolutely continuous ones. This Wasserstein approach roots in optimal transport theory and is well suited for the adversary interpretation of model risk. In particular, it specifies the economic reality of the fictitious adversary with the capacity of parametrising the actual market structure. The Wasserstein approach may result in the worst-case model that is more robust, in the sense that it is no longer restricted by the support of the reference measure. This is especially useful when the reference measure is supported only by a subspace (for instance the volatility of a diffusion process or the prices of perfectly correlated assets). This approach has additional practical advantage due to its ability of guaranteeing integrability.

To further illustrate the Wasserstein approach, we presented four applications ranging from single-asset variance risk and hedging risk to the multi-asset allocation problem. All the applications are connected in the sense that their reference measures are (or close to) supported by merely a subspace. In the example of single-asset variance risk, we look at the limit of small variance, i.e. when the time to maturity is close to zero (or the volatility close to zero). The Wasserstein approach is capable of jumping out of the family of diffusion processes, and accounts for the possibility of jumps. In the application of portfolio variance risk, the Wasserstein approach provides us with worst-case measure induced by a linear map, thus altering the support. Its advantage of dealing with multi-asset problems is even more apparent when treating the asset allocation problem, in which the Wasserstein approach accounts for the correlation risk. This approach results in a robust mean-variance optimal portfolio that adjusts the relative weights of the assets according to their correlations. It produces a curved capital allocation line, with the Sharpe ratio reduced by a larger amount on a higher standard deviation or a higher asset correlation. The final application is related to the hedging risk of a vanilla option. f𝑓f-divergence is incapable of quantifying the risk associated with a continuously hedged position because its profit-and-loss is zero almost surely. The Wasserstein approach, on the other hand, leads to a positive hedging error and therefore a more realistic assessment of model risk. In conclusion, the Wasserstein approach provides a useful tool to practitioners who aim to manage risks and optimize positions accounting for model ambiguity.

## 6 Appendix

### 6.1 A. Derivation of Eq. [15](#S3.E15 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance")

In this part, we derive the solution Eq. [15](#S3.E15 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") to the problem expressed by Eq. [10](#S3.E10 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance")-[12](#S3.E12 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance").
For simplicity, we denote the transition density pY|X​(y|x)subscript𝑝conditional𝑌𝑋conditional𝑦𝑥p\_{Y|X}(y|x) by γx​(y):=γ​(x,y)/p​(x)assignsubscript𝛾𝑥𝑦𝛾𝑥𝑦𝑝𝑥\gamma\_{x}(y):=\gamma(x,y)/p(x). This transforms the problem into

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supγx∈Γsubscriptsupremumsubscript𝛾𝑥Γ\displaystyle\sup\_{\gamma\_{x}\in\Gamma} | ∫Ωp​(x)​[∫Ωγx​(y)​V​(y)​𝑑y]​𝑑xsubscriptΩ𝑝𝑥delimited-[]subscriptΩsubscript𝛾𝑥𝑦𝑉𝑦differential-d𝑦differential-d𝑥\displaystyle\int\_{\Omega}p(x)\left[\int\_{\Omega}\gamma\_{x}(y)V(y)dy\right]dx |  | (58) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t.formulae-sequence𝑠𝑡\displaystyle s.t. | ∫Ωp​(x)​[∫Ωγx​(y)​c​(x,y)​𝑑y]​𝑑x≤ηsubscriptΩ𝑝𝑥delimited-[]subscriptΩsubscript𝛾𝑥𝑦𝑐𝑥𝑦differential-d𝑦differential-d𝑥𝜂\displaystyle\int\_{\Omega}p(x)\left[\int\_{\Omega}\gamma\_{x}(y)c(x,y)dy\right]dx\leq\eta |  |

where ΓΓ\Gamma is the space of probability density functions. The Karush-Kuhn-Tucker (KKT) condition in convex optimisation ensures the existence of a KKT multiplier λ𝜆\lambda such that the solution to Eq. [58](#S6.E58 "In 6.1 A. Derivation of Eq. 15 ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") also solves

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supγx∈Γsubscriptsupremumsubscript𝛾𝑥Γ\displaystyle\sup\_{\gamma\_{x}\in\Gamma} | ∫Ωp​(x)​{∫Ωγx​(y)​[V​(y)−λ​c​(x,y)]​𝑑y}​𝑑xsubscriptΩ𝑝𝑥subscriptΩsubscript𝛾𝑥𝑦delimited-[]𝑉𝑦𝜆𝑐𝑥𝑦differential-d𝑦differential-d𝑥\displaystyle\int\_{\Omega}p(x)\left\{\int\_{\Omega}\gamma\_{x}(y)\left[V(y)-\lambda c(x,y)\right]dy\right\}dx |  | (59) |

The solution to Eq. [59](#S6.E59 "In 6.1 A. Derivation of Eq. 15 ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") is a δ𝛿\delta-function transition density γx∗​(y)=δ​(y−y∗​(x))superscriptsubscript𝛾𝑥𝑦𝛿𝑦superscript𝑦𝑥\gamma\_{x}^{\*}(y)=\delta\left(y-y^{\*}(x)\right), resulting in a transportation plan

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ∗​(x,y)=p​(x)​δ​(y−y∗​(x))superscript𝛾𝑥𝑦𝑝𝑥𝛿𝑦superscript𝑦𝑥\displaystyle\gamma^{\*}(x,y)=p(x)\delta\left(y-y^{\*}(x)\right) |  | (60) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | y∗​(x)=arg⁡maxy∈Ω⁡[V​(y)−λ​c​(x,y)]superscript𝑦𝑥subscript𝑦Ω𝑉𝑦𝜆𝑐𝑥𝑦\displaystyle y^{\*}(x)=\arg\max\_{y\in\Omega}\left[V(y)-\lambda c(x,y)\right] |  | (61) |

The solution to the model risk problem is expressed either by a transportation plan (Eq. [60](#S6.E60 "In 6.1 A. Derivation of Eq. 15 ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance")) or a transportation map (Eq. [61](#S6.E61 "In 6.1 A. Derivation of Eq. 15 ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance")). It is noted that λ=0𝜆0\lambda=0 is a trivial case that we will not consider. To be consistent with the main result Eq. [21](#S3.E21 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), we replace λ𝜆\lambda by its inverse β=λ−1𝛽superscript𝜆1\beta=\lambda^{-1}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y∗​(x)=arg⁡maxy∈Ω⁡[V​(y)−c​(x,y)β]superscript𝑦𝑥subscript𝑦Ω𝑉𝑦𝑐𝑥𝑦𝛽\displaystyle y^{\*}(x)=\arg\max\_{y\in\Omega}\left[V(y)-\frac{c(x,y)}{\beta}\right] |  | (62) |

### 6.2 B. Derivation of Eq. [21](#S3.E21 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") and [25](#S3.E25 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance")

Eq. [21](#S3.E21 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") is the solution of the problem formulated by Eq. [10](#S3.E10 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance")-[12](#S3.E12 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") plus the additional entropy constraint Eq. [16](#S3.E16 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"). As in Appendix A,
we introduce KKT multipliers λ𝜆\lambda and α𝛼\alpha. This converts the original constrained supremum problem to the following dual problem (same as in Appendix A we denote the transition density by γx​(y)subscript𝛾𝑥𝑦\gamma\_{x}(y)):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | infβ,θ∈ℝ+supγ∫Ω×Ωγ​(x,y)​(V​(y)−λ​[c​(x,y)−η]−α​[ln⁡γ​(x,y)−μ])​𝑑x​𝑑ysubscriptinfimum  𝛽𝜃 superscriptℝsubscriptsupremum𝛾subscriptΩΩ𝛾𝑥𝑦𝑉𝑦𝜆delimited-[]𝑐𝑥𝑦𝜂𝛼delimited-[]𝛾𝑥𝑦𝜇differential-d𝑥differential-d𝑦\displaystyle\inf\_{\beta,\theta\in\mathbb{R}^{+}}\sup\_{\gamma}\int\_{\Omega\times\Omega}\gamma(x,y)\left(V(y)-\lambda\left[c(x,y)-\eta\right]-\alpha\left[\ln\gamma(x,y)-\mu\right]\right)dxdy |  | (63) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | infβ,θ∈ℝ+(∫Ωp(x)dx[supγx∫Ωγx(y)(V(y)−λc(x,y)−αlnγx(y))dy]\displaystyle\inf\_{\beta,\theta\in\mathbb{R}^{+}}\left(\int\_{\Omega}p(x)dx\left[\sup\_{\gamma\_{x}}\int\_{\Omega}\gamma\_{x}(y)\left(V(y)-\lambda c(x,y)-\alpha\ln\gamma\_{x}(y)\right)dy\right]\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λη+α[μ−∫Ωlnp(x)dx])\displaystyle~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}\left.+\lambda\eta+\alpha\left[\mu-\int\_{\Omega}\ln p(x)dx\right]\right) |  |

Same as the relative entropy approach proposed by Glasserman and Xu [[7](#bib.bib7)], we derive a closed-form solution to the inner part of the problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | supγx∫Ωγx​(y)​(V​(y)−λ​c​(x,y)−α​ln⁡γx​(y))​𝑑ysubscriptsupremumsubscript𝛾𝑥subscriptΩsubscript𝛾𝑥𝑦𝑉𝑦𝜆𝑐𝑥𝑦𝛼subscript𝛾𝑥𝑦differential-d𝑦\displaystyle\sup\_{\gamma\_{x}}\int\_{\Omega}\gamma\_{x}(y)\left(V(y)-\lambda c(x,y)-\alpha\ln\gamma\_{x}(y)\right)dy |  | (64) |

It is noted that Eq. [64](#S6.E64 "In 6.2 B. Derivation of Eq. 21 and 25 ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") asks for the supremum w.r.t the density function pxsubscript𝑝𝑥p\_{x} for a given x∈Ω𝑥Ωx\in\Omega. The solution to this problem is given by (for consistency we replace λ𝜆\lambda by its inverse γ𝛾\gamma):

|  |  |  |  |
| --- | --- | --- | --- |
|  | γx∗​(y)=exp⁡(V​(y)α−c​(x,y)α​β)∫Ωexp⁡(V​(z)α−c​(x,z)α​β)​𝑑zsuperscriptsubscript𝛾𝑥𝑦𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽subscriptΩ𝑉𝑧𝛼𝑐𝑥𝑧𝛼𝛽differential-d𝑧\displaystyle\gamma\_{x}^{\*}(y)=\frac{\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right)}{\int\_{\Omega}\exp\left(\frac{V(z)}{\alpha}-\frac{c(x,z)}{\alpha\beta}\right)dz} |  | (65) |

The worst-case probability density function is the marginal distribution of y𝑦y, induced by the transition density function γx∗​(y)subscriptsuperscript𝛾𝑥𝑦\gamma^{\*}\_{x}(y):

|  |  |  |  |
| --- | --- | --- | --- |
|  | p∗​(y)=superscript𝑝𝑦absent\displaystyle p^{\*}(y)= | ∫Ωp​(x)​γx∗​(y)​𝑑xsubscriptΩ𝑝𝑥superscriptsubscript𝛾𝑥𝑦differential-d𝑥\displaystyle\int\_{\Omega}p(x)\gamma\_{x}^{\*}(y)dx |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | ∫Ω𝑑x​p​(x)​exp⁡(V​(y)α−c​(x,y)α​β)∫Ωexp⁡(V​(z)α−c​(x,z)α​β)​𝑑zsubscriptΩdifferential-d𝑥𝑝𝑥𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽subscriptΩ𝑉𝑧𝛼𝑐𝑥𝑧𝛼𝛽differential-d𝑧\displaystyle\int\_{\Omega}dx\frac{p(x)\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right)}{\int\_{\Omega}\exp\left(\frac{V(z)}{\alpha}-\frac{c(x,z)}{\alpha\beta}\right)dz} |  | (66) |

Eq. [25](#S3.E25 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") is derived in a similar way. Since we lift the entropy constraint Eq. [16](#S3.E16 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") into a relative entropy constraint Eq. [19](#S3.E19 "In 3.2 Entropy Constraint on Transportation Plan ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), the inner problem Eq. [64](#S6.E64 "In 6.2 B. Derivation of Eq. 21 and 25 ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") requires slight modification:

|  |  |  |  |
| --- | --- | --- | --- |
|  | supγx∫Ωγx​(y)​(V​(y)−λ​c​(x,y)−α​ln⁡γx​(y)q0​(y))​𝑑ysubscriptsupremumsubscript𝛾𝑥subscriptΩsubscript𝛾𝑥𝑦𝑉𝑦𝜆𝑐𝑥𝑦𝛼subscript𝛾𝑥𝑦subscript𝑞0𝑦differential-d𝑦\displaystyle\sup\_{\gamma\_{x}}\int\_{\Omega}\gamma\_{x}(y)\left(V(y)-\lambda c(x,y)-\alpha\ln\frac{\gamma\_{x}(y)}{q\_{0}(y)}\right)dy |  | (67) |

This problem has the same formulation as the supremum problem given in Glasserman and Xu’s work, and therefore shares the same solution

|  |  |  |  |
| --- | --- | --- | --- |
|  | γx∗​(y)=q0​(y)​exp⁡(V​(y)α−c​(x,y)α​β)∫Ωq0​(z)​exp⁡(V​(z)α−c​(x,z)α​β)​𝑑zsuperscriptsubscript𝛾𝑥𝑦subscript𝑞0𝑦𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽subscriptΩsubscript𝑞0𝑧𝑉𝑧𝛼𝑐𝑥𝑧𝛼𝛽differential-d𝑧\displaystyle\gamma\_{x}^{\*}(y)=\frac{q\_{0}(y)\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right)}{\int\_{\Omega}q\_{0}(z)\exp\left(\frac{V(z)}{\alpha}-\frac{c(x,z)}{\alpha\beta}\right)dz} |  | (68) |

This equation differs from Eq. [65](#S6.E65 "In 6.2 B. Derivation of Eq. 21 and 25 ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") merely by a prior distribution q0subscript𝑞0q\_{0}. It takes Eq. [65](#S6.E65 "In 6.2 B. Derivation of Eq. 21 and 25 ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") as its special case where q0subscript𝑞0q\_{0} is a uniform distribution. Marginalizing the transition density Eq. [68](#S6.E68 "In 6.2 B. Derivation of Eq. 21 and 25 ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") gives the worst-case distribution shown in Eq. [25](#S3.E25 "In 3.4 Practical Considerations ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance").

### 6.3 C. Jump Risk and Variance Risk

Under a diffusive model, the logarithmic return of an asset follows a normal distribution with mean of μ​T𝜇𝑇\mu T and variance of σ2​Tsuperscript𝜎2𝑇\sigma^{2}T, where σ𝜎\sigma is the volatility and T𝑇T is the time to maturity, and the drift coefficient of this process is assumed to be μ+σ2/2𝜇superscript𝜎22\mu+\sigma^{2}/2. The probability density function of the return x𝑥x is

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(x)=12​π​σ​e−((x−μ​T)22​σ2​T)2𝑝𝑥12𝜋𝜎superscript𝑒superscriptsuperscript𝑥𝜇𝑇22superscript𝜎2𝑇2\displaystyle p(x)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\left(\frac{(x-\mu T)^{2}}{2\sigma^{2}T}\right)^{2}} |  | (69) |

Applying Eq. [21](#S3.E21 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), one may obtain the probability density function of the worst-case measure, assuming a linear loss function V​(x)=x𝑉𝑥𝑥V(x)=x and a quadratic transportation cost function c​(x,y)=(x−y)2𝑐𝑥𝑦superscript𝑥𝑦2c(x,y)=(x-y)^{2},

|  |  |  |  |
| --- | --- | --- | --- |
|  | q∗​(y)∝proportional-tosuperscript𝑞𝑦absent\displaystyle q^{\*}(y)\propto | ∫Ω[p​(x)​exp⁡(yα−(x−y)2α​β)/exp⁡(xα)]​𝑑xsubscriptΩdelimited-[]/𝑝𝑥𝑦𝛼superscript𝑥𝑦2𝛼𝛽𝑥𝛼differential-d𝑥\displaystyle\int\_{\Omega}\left[p(x)\left.\exp\left(\frac{y}{\alpha}-\frac{(x-y)^{2}}{\alpha\beta}\right)\right/\exp\left(\frac{x}{\alpha}\right)\right]dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∫Ωexp⁡(y−xα−(x−y)2α​β−(x−μ​T)22​σ2​T)​𝑑xsubscriptΩ𝑦𝑥𝛼superscript𝑥𝑦2𝛼𝛽superscript𝑥𝜇𝑇22superscript𝜎2𝑇differential-d𝑥\displaystyle\int\_{\Omega}\exp\left(\frac{y-x}{\alpha}-\frac{(x-y)^{2}}{\alpha\beta}-\frac{(x-\mu T)^{2}}{2\sigma^{2}T}\right)dx |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∝proportional-to\displaystyle\propto | exp⁡(−(y−μ​T−β/2)22​σ2​T+α​β)superscript𝑦𝜇𝑇𝛽222superscript𝜎2𝑇𝛼𝛽\displaystyle\exp\left(-\frac{\left(y-\mu T-\beta/2\right)^{2}}{2\sigma^{2}T+\alpha\beta}\right) |  | (70) |

Unlike the result given by the KL divergence, Eq. [6.3](#S6.Ex16 "6.3 C. Jump Risk and Variance Risk ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") not only shifts the mean the distribution but also enlarges the variance as a result of additional uncertainty. On σ→0→𝜎0\sigma\to 0, the worst-case measure is no longer a Dirac measure, showing consideration of jump risks:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limσ→0q∗​(y)∝exp⁡(−(y−μ​T−β/2)2α​β)proportional-tosubscript→𝜎0superscript𝑞𝑦superscript𝑦𝜇𝑇𝛽22𝛼𝛽\displaystyle\lim\_{\sigma\to 0}q^{\*}(y)\propto\exp\left(-\frac{\left(y-\mu T-\beta/2\right)^{2}}{\alpha\beta}\right) |  | (71) |

This gives Eq. [38](#S4.E38 "In 4.1 Jump risk under a diffusive reference model ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"). Alternatively, one may first derive Eq. [37](#S4.E37 "In 4.1 Jump risk under a diffusive reference model ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") followed by substituting V​(x)=x𝑉𝑥𝑥V(x)=x to get Eq. [38](#S4.E38 "In 4.1 Jump risk under a diffusive reference model ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"). Eq. [37](#S4.E37 "In 4.1 Jump risk under a diffusive reference model ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") is derived by substituting p​(x)=δ​(x−μ​T)𝑝𝑥𝛿𝑥𝜇𝑇p(x)=\delta(x-\mu T) into Eq. [21](#S3.E21 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | q∗​(y)=superscript𝑞𝑦absent\displaystyle q^{\*}(y)= | ∫Ωδ​(x−μ​T)​exp⁡(V​(y)α−(x−y)2α​β)∫Ωexp⁡(V​(z)α−(x−z)2α​β)​𝑑z​𝑑xsubscriptΩ𝛿𝑥𝜇𝑇𝑉𝑦𝛼superscript𝑥𝑦2𝛼𝛽subscriptΩ𝑉𝑧𝛼superscript𝑥𝑧2𝛼𝛽differential-d𝑧differential-d𝑥\displaystyle\int\_{\Omega}\delta(x-\mu T)\frac{\exp\left(\frac{V(y)}{\alpha}-\frac{(x-y)^{2}}{\alpha\beta}\right)}{\int\_{\Omega}\exp\left(\frac{V(z)}{\alpha}-\frac{(x-z)^{2}}{\alpha\beta}\right)dz}dx |  | (72) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | exp⁡(V​(y)α−(y−μ​T)2α​β)∫Ωexp⁡(V​(z)α−(z−μ​T)2α​β)​𝑑z𝑉𝑦𝛼superscript𝑦𝜇𝑇2𝛼𝛽subscriptΩ𝑉𝑧𝛼superscript𝑧𝜇𝑇2𝛼𝛽differential-d𝑧\displaystyle\frac{\exp\left(\frac{V(y)}{\alpha}-\frac{(y-\mu T)^{2}}{\alpha\beta}\right)}{\int\_{\Omega}\exp\left(\frac{V(z)}{\alpha}-\frac{(z-\mu T)^{2}}{\alpha\beta}\right)dz} |  | (73) |

Now we adopt a quadratic type of loss function, V​(x)=(x−μ​T)2𝑉𝑥superscript𝑥𝜇𝑇2V(x)=(x-\mu T)^{2}, following a procedure similar to Eq. [6.3](#S6.Ex16 "6.3 C. Jump Risk and Variance Risk ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | q∗​(y)∝exp⁡(−(y−μ​T)22​σ2​T(1−β)2+α​β(1−β))proportional-tosuperscript𝑞𝑦superscript𝑦𝜇𝑇22superscript𝜎2𝑇superscript1𝛽2𝛼𝛽1𝛽\displaystyle q^{\*}(y)\propto\exp\left(-\frac{\left(y-\mu T\right)^{2}}{\frac{2\sigma^{2}T}{(1-\beta)^{2}}+\frac{\alpha\beta}{(1-\beta)}}\right) |  | (74) |

the variance of the worst-case measure is

|  |  |  |  |
| --- | --- | --- | --- |
|  | σW2​T=σ2​T(1−β)2+α​β2​(1−β)superscriptsubscript𝜎𝑊2𝑇superscript𝜎2𝑇superscript1𝛽2𝛼𝛽21𝛽\displaystyle\sigma\_{W}^{2}T=\frac{\sigma^{2}T}{(1-\beta)^{2}}+\frac{\alpha\beta}{2(1-\beta)} |  | (75) |

as provided in Eq. [40](#S4.E40 "In 4.2 Volatility Risk and Variance Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance").
We may verify that the measure Q∗superscript𝑄Q^{\*} given by Eq. [74](#S6.E74 "In 6.3 C. Jump Risk and Variance Risk ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") does provide the largest variance among all the legitimate alternative measures. In fact, the variance of x𝑥x under Q∗superscript𝑄Q^{\*} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | EQ∗​[(x−EQ∗​(x))2]=EQ∗​[(x−μ​T)2]superscript𝐸superscript𝑄delimited-[]superscript𝑥superscript𝐸superscript𝑄𝑥2superscript𝐸superscript𝑄delimited-[]superscript𝑥𝜇𝑇2\displaystyle E^{Q^{\*}}\left[\left(x-E^{Q^{\*}}(x)\right)^{2}\right]=E^{Q^{\*}}\left[\left(x-\mu T\right)^{2}\right] |  | (76) |

According to the definition of the worst-case model, for all Q∈ℳ𝑄ℳQ\in\mathscr{M} (the space of legitimate alternative measures) we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | EQ∗​[(x−μ​T)2]≥superscript𝐸superscript𝑄delimited-[]superscript𝑥𝜇𝑇2absent\displaystyle E^{Q^{\*}}\left[\left(x-\mu T\right)^{2}\right]\geq | EQ​[(x−μ​T)2]superscript𝐸𝑄delimited-[]superscript𝑥𝜇𝑇2\displaystyle E^{Q}\left[\left(x-\mu T\right)^{2}\right] |  | (77) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | EQ​[(x−EQ​(x))2]+(EQ​(x)−μ​T)2superscript𝐸𝑄delimited-[]superscript𝑥superscript𝐸𝑄𝑥2superscriptsuperscript𝐸𝑄𝑥𝜇𝑇2\displaystyle E^{Q}\left[\left(x-E^{Q}(x)\right)^{2}\right]+\left(E^{Q}(x)-\mu T\right)^{2} |  | (78) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≥\displaystyle\geq | EQ​[(x−EQ​(x))2]superscript𝐸𝑄delimited-[]superscript𝑥superscript𝐸𝑄𝑥2\displaystyle E^{Q}\left[\left(x-E^{Q}(x)\right)^{2}\right] |  | (79) |

This confirms that Eq. [75](#S6.E75 "In 6.3 C. Jump Risk and Variance Risk ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") is indeed the worst-case (maximum) variance.

### 6.4 D. Worst-case Portfolio Variance

To find the portfolio variance under the worst-case scenario, we need to formulate the problem using Eq. [6](#S3.E6 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance") with a loss (target) function given by Eq. [41](#S4.E41 "In 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"). The worst-case measure may be evaluated by substituting the loss function into Eq. [21](#S3.E21 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"). In this section we will show the calculation step by step. First, we need to specify the transport cost function c​(x,y)𝑐𝑥𝑦c(x,y) as the inner product introduced in Eq. [43](#S4.E43 "In 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(x,y)=‖y−x‖2=(y−x)T​B​(y−x)𝑐𝑥𝑦superscriptnorm𝑦𝑥2superscript𝑦𝑥𝑇𝐵𝑦𝑥\displaystyle c(x,y)=||y-x||^{2}=(y-x)^{T}B(y-x) |  | (80) |

Then we evaluate the following part in Eq. [21](#S3.E21 "In 3.3 Main Result and Discussion ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"):

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | exp⁡(V​(y)α−c​(x,y)α​β)𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽\displaystyle\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | exp⁡(yT​A​yα−(y−x)T​B​(y−x)α​β)superscript𝑦𝑇𝐴𝑦𝛼superscript𝑦𝑥𝑇𝐵𝑦𝑥𝛼𝛽\displaystyle\exp\left(\frac{y^{T}Ay}{\alpha}-\frac{(y-x)^{T}B(y-x)}{\alpha\beta}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | exp(1α​βxTB((B−βA)−1−I)Bx\displaystyle\exp\left(\frac{1}{\alpha\beta}x^{T}B\left((B-\beta A)^{-1}-I\right)Bx\right. |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −1α​β(y−(B−βA)−1Bx)T(B−βA)(y−(B−βA)−1Bx))\displaystyle~{}~{}~{}~{}~{}~{}~{}~{}\left.-\frac{1}{\alpha\beta}\left(y-(B-\beta A)^{-1}Bx\right)^{T}\left(B-\beta A\right)\left(y-(B-\beta A)^{-1}Bx\right)\right) |  | (81) |

Remember that both A𝐴A and B𝐵B are symmetric, positive-definite matrices. Fixing x𝑥x, Eq. [6.4](#S6.Ex18 "6.4 D. Worst-case Portfolio Variance ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") is proportional to the probability density function of a multivariate normal variable Y𝑌Y, with its mean and covariance matrix

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝖤​(Y)=𝖤𝑌absent\displaystyle\mathsf{E}(Y)= | (B−β​A)−1​B​xsuperscript𝐵𝛽𝐴1𝐵𝑥\displaystyle(B-\beta A)^{-1}Bx |  | (82) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Σ​(Y)=Σ𝑌absent\displaystyle\Sigma(Y)= | α​β2​(B−β​A)−1𝛼𝛽2superscript𝐵𝛽𝐴1\displaystyle\frac{\alpha\beta}{2}(B-\beta A)^{-1} |  | (83) |

This means that after normalization w.r.t y𝑦y, Eq. [6.4](#S6.Ex18 "6.4 D. Worst-case Portfolio Variance ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") gives exactly the probability density function of Y𝑌Y. We may write this down explicitly by noting that y𝑦y lives in the n𝑛n-dimensional vector space, i.e. Ω=𝒱Ω𝒱\Omega=\mathcal{V}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | exp⁡(V​(y)α−c​(x,y)α​β)∫𝒱exp⁡(V​(y)α−c​(x,y)α​β)​𝑑y𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽subscript𝒱𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽differential-d𝑦\displaystyle\frac{\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right)}{\int\_{\mathcal{V}}\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right)dy} |  | (84) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (2​π)−n2​α​β2​|B−β​A|​exp⁡(−(y−(B−β​A)−1​B​x)T​(B−β​A)α​β​(y−(B−β​A)−1​B​x))superscript2𝜋𝑛2𝛼𝛽2𝐵𝛽𝐴superscript𝑦superscript𝐵𝛽𝐴1𝐵𝑥𝑇𝐵𝛽𝐴𝛼𝛽𝑦superscript𝐵𝛽𝐴1𝐵𝑥\displaystyle(2\pi)^{-\frac{n}{2}}\sqrt{\frac{\alpha\beta}{2}|B-\beta A|}\exp\left(-\left(y-(B-\beta A)^{-1}Bx\right)^{T}\frac{\left(B-\beta A\right)}{\alpha\beta}\left(y-(B-\beta A)^{-1}Bx\right)\right) |  |

Now we need to evaluate the product of Eq. [84](#S6.E84 "In 6.4 D. Worst-case Portfolio Variance ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") and the nominal distribution p​(x)𝑝𝑥p(x). The nominal distribution is multivariate normal with mean μ𝜇\mu and covariance matrix ΣΣ\Sigma:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(x)=(2​π)−n2|Σ|​exp⁡(−12​(x−μ)T​Σ−1​(x−μ))𝑝𝑥superscript2𝜋𝑛2Σ12superscript𝑥𝜇𝑇superscriptΣ1𝑥𝜇\displaystyle p(x)=\frac{(2\pi)^{-\frac{n}{2}}}{|\Sigma|}\exp\left(-\frac{1}{2}(x-\mu)^{T}\Sigma^{-1}(x-\mu)\right) |  | (85) |

The product contains many terms of x𝑥x and y𝑦y. One may re-arrange the terms to isolate quadratic and linear terms of x𝑥x:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | p​(x)​exp⁡(V​(y)α−c​(x,y)α​β)∫𝒱exp⁡(V​(y)α−c​(x,y)α​β)​𝑑y𝑝𝑥𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽subscript𝒱𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽differential-d𝑦\displaystyle\frac{p(x)\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right)}{\int\_{\mathcal{V}}\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right)dy} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∝proportional-to\displaystyle\propto | exp(−1α​β(y−(B−βA)−1Bx)T(B−βA)(y−(B−βA)−1Bx)\displaystyle\exp\left(-\frac{1}{\alpha\beta}\left(y-(B-\beta A)^{-1}Bx\right)^{T}\left(B-\beta A\right)\left(y-(B-\beta A)^{-1}Bx\right)\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −12(x−μ)TΣ−1(x−μ))\displaystyle~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}\left.-\frac{1}{2}(x-\mu)^{T}\Sigma^{-1}(x-\mu)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∝proportional-to\displaystyle\propto | exp(−1α​β[(x−Kμ−Ly)TM(x−Kμ−Ly)−(Kμ+Ly)TM(Kμ+Ly)]\displaystyle\exp\left(-\frac{1}{\alpha\beta}\left[(x-K\mu-Ly)^{T}M(x-K\mu-Ly)-(K\mu+Ly)^{T}M(K\mu+Ly)\right]\right. |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −1α​βyT(B−βA)y)\displaystyle~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}~{}\left.-\frac{1}{\alpha\beta}y^{T}(B-\beta A)y\right) |  | (86) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | M:=B​(B−β​A)−1​B+α​β2​Σ−1K:=α​β2​M−1​Σ−1L:=M−1​Bassign𝑀absent𝐵superscript𝐵𝛽𝐴1𝐵𝛼𝛽2superscriptΣ1assign𝐾absent𝛼𝛽2superscript𝑀1superscriptΣ1assign𝐿absentsuperscript𝑀1𝐵\displaystyle\begin{aligned} M:=&B(B-\beta A)^{-1}B+\frac{\alpha\beta}{2}\Sigma^{-1}\\ K:=&\frac{\alpha\beta}{2}M^{-1}\Sigma^{-1}\\ L:=&M^{-1}B\end{aligned} |  | (87) |

Fixing y𝑦y, Eq. [6.4](#S6.Ex22 "6.4 D. Worst-case Portfolio Variance ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") is proportional to the probability density function of a multivariate normal variable X𝑋X where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝖤​(X)=𝖤𝑋absent\displaystyle\mathsf{E}(X)= | K​μ+L​y𝐾𝜇𝐿𝑦\displaystyle K\mu+Ly |  | (88) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Σ​(X)=Σ𝑋absent\displaystyle\Sigma(X)= | α​β2​M−1𝛼𝛽2superscript𝑀1\displaystyle\frac{\alpha\beta}{2}M^{-1} |  | (89) |

The following integral

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫𝒱exp⁡(−1α​β​(x−K​μ−L​y)T​M​(x−K​μ−L​y))​𝑑y=2α​β​(2​π)−n2​|M|−1subscript𝒱1𝛼𝛽superscript𝑥𝐾𝜇𝐿𝑦𝑇𝑀𝑥𝐾𝜇𝐿𝑦differential-d𝑦2𝛼𝛽superscript2𝜋𝑛2superscript𝑀1\displaystyle\int\_{\mathcal{V}}\exp\left(-\frac{1}{\alpha\beta}(x-K\mu-Ly)^{T}M(x-K\mu-Ly)\right)dy=\frac{2}{\alpha\beta}(2\pi)^{-\frac{n}{2}}|M|^{-1} |  | (90) |

is constant irrespective of y𝑦y. Integrating Eq. [6.4](#S6.Ex22 "6.4 D. Worst-case Portfolio Variance ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") over x gives the worst-case probability density function q∗​(y)superscript𝑞𝑦q^{\*}(y):

|  |  |  |  |
| --- | --- | --- | --- |
|  | q∗​(y)=superscript𝑞𝑦absent\displaystyle q^{\*}(y)= | ∫𝒱𝑑x​p​(x)​exp⁡(V​(y)α−c​(x,y)α​β)∫Ωexp⁡(V​(y)α−c​(x,y)α​β)​𝑑ysubscript𝒱differential-d𝑥𝑝𝑥𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽subscriptΩ𝑉𝑦𝛼𝑐𝑥𝑦𝛼𝛽differential-d𝑦\displaystyle\int\_{\mathcal{V}}dx\frac{p(x)\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right)}{\int\_{\Omega}\exp\left(\frac{V(y)}{\alpha}-\frac{c(x,y)}{\alpha\beta}\right)dy} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∝proportional-to\displaystyle\propto | ∫𝒱exp⁡(−1α​β​(x−K​μ−L​y)T​M​(x−K​μ−L​y))​𝑑xsubscript𝒱1𝛼𝛽superscript𝑥𝐾𝜇𝐿𝑦𝑇𝑀𝑥𝐾𝜇𝐿𝑦differential-d𝑥\displaystyle\int\_{\mathcal{V}}\exp\left(-\frac{1}{\alpha\beta}(x-K\mu-Ly)^{T}M(x-K\mu-Ly)\right)dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp⁡[1α​β​(K​μ+L​y)T​M​(K​μ+L​y)−1α​β​yT​(B−β​A)​y]absent1𝛼𝛽superscript𝐾𝜇𝐿𝑦𝑇𝑀𝐾𝜇𝐿𝑦1𝛼𝛽superscript𝑦𝑇𝐵𝛽𝐴𝑦\displaystyle\times\exp\left[\frac{1}{\alpha\beta}(K\mu+Ly)^{T}M(K\mu+Ly)-\frac{1}{\alpha\beta}y^{T}(B-\beta A)y\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∝proportional-to\displaystyle\propto | exp⁡[1α​β​(K​μ+L​y)T​M​(K​μ+L​y)−1α​β​yT​(B−β​A)​y]1𝛼𝛽superscript𝐾𝜇𝐿𝑦𝑇𝑀𝐾𝜇𝐿𝑦1𝛼𝛽superscript𝑦𝑇𝐵𝛽𝐴𝑦\displaystyle\exp\left[\frac{1}{\alpha\beta}(K\mu+Ly)^{T}M(K\mu+Ly)-\frac{1}{\alpha\beta}y^{T}(B-\beta A)y\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | exp⁡[1α​β​((α​β2​Σ−1​μ+B​y)T​M−1​(α​β2​Σ−1​μ+B​y)−yT​(B−β​A)​y)]1𝛼𝛽superscript𝛼𝛽2superscriptΣ1𝜇𝐵𝑦𝑇superscript𝑀1𝛼𝛽2superscriptΣ1𝜇𝐵𝑦superscript𝑦𝑇𝐵𝛽𝐴𝑦\displaystyle\exp\left[\frac{1}{\alpha\beta}\left(\left(\frac{\alpha\beta}{2}\Sigma^{-1}\mu+By\right)^{T}M^{-1}\left(\frac{\alpha\beta}{2}\Sigma^{-1}\mu+By\right)-y^{T}(B-\beta A)y\right)\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∝proportional-to\displaystyle\propto | exp⁡[−12​(y−B​(B−β​A)−1​μ)T​Σ∗−1​(y−B​(B−β​A)−1​μ)]12superscript𝑦𝐵superscript𝐵𝛽𝐴1𝜇𝑇superscriptΣabsent1𝑦𝐵superscript𝐵𝛽𝐴1𝜇\displaystyle\exp\left[-\frac{1}{2}\left(y-B(B-\beta A)^{-1}\mu\right)^{T}\Sigma^{\*-1}\left(y-B(B-\beta A)^{-1}\mu\right)\right] |  | (91) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ∗−1=superscriptΣabsent1absent\displaystyle\Sigma^{\*-1}= | 2α​β​(BT​M−1​B−(B−β​A))2𝛼𝛽superscript𝐵𝑇superscript𝑀1𝐵𝐵𝛽𝐴\displaystyle\frac{2}{\alpha\beta}\left(B^{T}M^{-1}B-(B-\beta A)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 2α​β​(((B−β​A)−1+α​β2​B−1​Σ−1​B−1)−1−(B−β​A))2𝛼𝛽superscriptsuperscript𝐵𝛽𝐴1𝛼𝛽2superscript𝐵1superscriptΣ1superscript𝐵11𝐵𝛽𝐴\displaystyle\frac{2}{\alpha\beta}\left(\left((B-\beta A)^{-1}+\frac{\alpha\beta}{2}B^{-1}\Sigma^{-1}B^{-1}\right)^{-1}-(B-\beta A)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 2α​β​(((B−β​A)−1+α​β2​B−1​Σ−1​B−1)−1​(I−(I+α​β2​B−1​Σ−1​B−1​(B−β​A))))2𝛼𝛽superscriptsuperscript𝐵𝛽𝐴1𝛼𝛽2superscript𝐵1superscriptΣ1superscript𝐵11𝐼𝐼𝛼𝛽2superscript𝐵1superscriptΣ1superscript𝐵1𝐵𝛽𝐴\displaystyle\frac{2}{\alpha\beta}\left(\left((B-\beta A)^{-1}+\frac{\alpha\beta}{2}B^{-1}\Sigma^{-1}B^{-1}\right)^{-1}\left(I-\left(I+\frac{\alpha\beta}{2}B^{-1}\Sigma^{-1}B^{-1}(B-\beta A)\right)\right)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ((B−β​A)−1+α​β2​B−1​Σ−1​B−1)−1​((B−β​A)−1​B​Σ​B)−1superscriptsuperscript𝐵𝛽𝐴1𝛼𝛽2superscript𝐵1superscriptΣ1superscript𝐵11superscriptsuperscript𝐵𝛽𝐴1𝐵Σ𝐵1\displaystyle\left((B-\beta A)^{-1}+\frac{\alpha\beta}{2}B^{-1}\Sigma^{-1}B^{-1}\right)^{-1}\left((B-\beta A)^{-1}B\Sigma B\right)^{-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ((B−β​A)−1​B​Σ​B​(B−β​A)−1+α​β2​(B−β​A)−1)−1superscriptsuperscript𝐵𝛽𝐴1𝐵Σ𝐵superscript𝐵𝛽𝐴1𝛼𝛽2superscript𝐵𝛽𝐴11\displaystyle\left((B-\beta A)^{-1}B\Sigma B(B-\beta A)^{-1}+\frac{\alpha\beta}{2}(B-\beta A)^{-1}\right)^{-1} |  |

Eq. [6.4](#S6.Ex26 "6.4 D. Worst-case Portfolio Variance ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") shows that the worst-case distribution is still multivariate normal. The vector of means and the covariance matrix are given respectively by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μW=subscript𝜇𝑊absent\displaystyle\mu\_{W}= | (B−β​A)−1​B​μsuperscript𝐵𝛽𝐴1𝐵𝜇\displaystyle(B-\beta A)^{-1}B\mu |  | (92) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΣW=subscriptΣ𝑊absent\displaystyle\Sigma\_{W}= | (B−β​A)−1​B​Σ​B​(B−β​A)−1+α​β2​(B−β​A)−1superscript𝐵𝛽𝐴1𝐵Σ𝐵superscript𝐵𝛽𝐴1𝛼𝛽2superscript𝐵𝛽𝐴1\displaystyle(B-\beta A)^{-1}B\Sigma B(B-\beta A)^{-1}+\frac{\alpha\beta}{2}(B-\beta A)^{-1} |  | (93) |

An interesting observation on Eq. [92](#S6.E92 "In 6.4 D. Worst-case Portfolio Variance ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") is that the worst-case measure can be generated by a measure-preserving linear map. In fact, for any vector v𝑣v of asset returns, the linear map g𝑔g gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(v)=𝑔𝑣absent\displaystyle g(v)= | (B−β​A)−1​B​vsuperscript𝐵𝛽𝐴1𝐵𝑣\displaystyle(B-\beta A)^{-1}Bv |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | (I−β​B−1​A)−1​vsuperscript𝐼𝛽superscript𝐵1𝐴1𝑣\displaystyle(I-\beta B^{-1}A)^{-1}v |  | (94) |

We write down the probability density function for the reference measure by

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(v)∝exp⁡(−12​(v−μ)T​Σ−1​(v−μ))proportional-to𝑓𝑣12superscript𝑣𝜇𝑇superscriptΣ1𝑣𝜇\displaystyle f(v)\propto\exp\left(-\frac{1}{2}\left(v-\mu\right)^{T}\Sigma^{-1}\left(v-\mu\right)\right) |  | (95) |

The measure given by the measure-preserving map g𝑔g has a probability density function that is proportional to f​(g−1​(v))𝑓superscript𝑔1𝑣f(g^{-1}(v)),

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | f​(g−1​(v))𝑓superscript𝑔1𝑣\displaystyle f(g^{-1}(v)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∝proportional-to\displaystyle\propto | exp⁡(−12​((I−β​B−1​A)​v−μ)T​Σ−1​((I−β​B−1​A)​v−μ))12superscript𝐼𝛽superscript𝐵1𝐴𝑣𝜇𝑇superscriptΣ1𝐼𝛽superscript𝐵1𝐴𝑣𝜇\displaystyle\exp\left(-\frac{1}{2}\left((I-\beta B^{-1}A)v-\mu\right)^{T}\Sigma^{-1}\left((I-\beta B^{-1}A)v-\mu\right)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | exp⁡(−12​(v−(I−β​B−1​A)−1​μ)T​(I−β​B−1​A)​Σ−1​(I−β​B−1​A)​((I−β​B−1​A)​v−μ))12superscript𝑣superscript𝐼𝛽superscript𝐵1𝐴1𝜇𝑇𝐼𝛽superscript𝐵1𝐴superscriptΣ1𝐼𝛽superscript𝐵1𝐴𝐼𝛽superscript𝐵1𝐴𝑣𝜇\displaystyle\exp\left(-\frac{1}{2}\left(v-(I-\beta B^{-1}A)^{-1}\mu\right)^{T}(I-\beta B^{-1}A)\Sigma^{-1}(I-\beta B^{-1}A)\left((I-\beta B^{-1}A)v-\mu\right)\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | exp⁡(−12​(v−μ~)T​Σ~−1​(v−μ~))12superscript𝑣~𝜇𝑇superscript~Σ1𝑣~𝜇\displaystyle\exp\left(-\frac{1}{2}\left(v-\tilde{\mu}\right)^{T}\tilde{\Sigma}^{-1}\left(v-\tilde{\mu}\right)\right) |  | (96) |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μ~:=assign~𝜇absent\displaystyle\tilde{\mu}:= | (I−β​B−1​A)−1​μsuperscript𝐼𝛽superscript𝐵1𝐴1𝜇\displaystyle\left(I-\beta B^{-1}A\right)^{-1}\mu |  | (97) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Σ~:=assign~Σabsent\displaystyle\tilde{\Sigma}:= | (I−β​B−1​A)−1​Σ​(I−β​B−1​A)−1superscript𝐼𝛽superscript𝐵1𝐴1Σsuperscript𝐼𝛽superscript𝐵1𝐴1\displaystyle\left(I-\beta B^{-1}A\right)^{-1}\Sigma\left(I-\beta B^{-1}A\right)^{-1} |  | (98) |

that are precisely the mean and covariance matrix given in Eq. [92](#S6.E92 "In 6.4 D. Worst-case Portfolio Variance ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") (with α=0𝛼0\alpha=0). As a result, we generate the worst-case measure by applying the measure-preserving map g𝑔g.

### 6.5 E. The support of a multivariate normal distribution

In this section, we discuss the support of the reference measure P𝑃P assuming the asset returns follow a multivariate normal distribution. In addition, we want see how it is altered by different approaches to model risk measurement. Clearly, approaches based on f𝑓f-divergence cannot alter the support as they only account for measures that are equivalent to the nominal one. But this conclusion does not tell us explicitly what the support is. In the following work we aim to find the linear subspace that supports the measure.

Formally speaking, returns of the n𝑛n assets form a n𝑛n-dimensional vector that lives in a n𝑛n-dimensional topological vector space 𝒱𝒱\mathcal{V}. If the asset returns follow a multivariate normal distribution with a non-singular covariance matrix, then the support is the entire space 𝒱𝒱\mathcal{V}. However, if the covariance matrix is singular, the support can only be part of 𝒱𝒱\mathcal{V}. We will find this support and show that it is a m𝑚m-dimensional linear subspace, where m𝑚m is the rank of the covariance matrix.

The reference model of asset returns defines a probability space (𝒱,ℱ,P)𝒱ℱ𝑃(\mathcal{V},\mathcal{F},P), where ℱℱ\mathcal{F} is the Borel σ𝜎\sigma-algebra on 𝒱𝒱\mathcal{V}.
Since 𝒱𝒱\mathcal{V} is a vector space, we may consider its dual space 𝒱∗superscript𝒱\mathcal{V}^{\*}, i.e. the space of linear maps a:𝒱→ℝ:𝑎→𝒱ℝa:\mathcal{V}\to\mathbb{R}. Any element of the dual space is regarded as a vector of portfolio weights. To see this, suppose the asset returns are v=(v1,v2,⋯,vn)∈𝒱𝑣subscript𝑣1subscript𝑣2⋯subscript𝑣𝑛𝒱v=(v\_{1},v\_{2},\cdots,v\_{n})\in\mathcal{V}, and the portfolio weights are a=(a1,a2,⋯,an)∈𝒱∗𝑎subscript𝑎1subscript𝑎2⋯subscript𝑎𝑛superscript𝒱a=(a\_{1},a\_{2},\cdots,a\_{n})\in\mathcal{V}^{\*}. The pairing of a𝑎a and v𝑣v results in a real number, which is exactly the portfolio return:

|  |  |  |  |
| --- | --- | --- | --- |
|  | a​(v)=∑j=1naj​vj𝑎𝑣superscriptsubscript𝑗1𝑛subscript𝑎𝑗subscript𝑣𝑗\displaystyle a(v)=\sum\_{j=1}^{n}a\_{j}v\_{j} |  | (99) |

If we treat the asset returns visubscript𝑣𝑖v\_{i} as random variables, we may calculate of portfolio variance on a given vector of weights a∈𝒱𝑎𝒱a\in\mathcal{V} by Var​(a​(v))=aT​Σ​aVar𝑎𝑣superscript𝑎𝑇Σ𝑎\mathrm{Var}(a(v))=a^{T}\Sigma a, where ΣΣ\Sigma is the covariance matrix of the asset returns. For convenience, we use the same symbol v𝑣v for both the vector of random variables (random vector) and its realization (i.e. a specific element in 𝒱𝒱\mathcal{V}).
Now take the positive semi-definite matrix ΣΣ\Sigma as a linear map Σ:𝒱∗→𝒱:Σ→superscript𝒱𝒱\Sigma:\mathcal{V}^{\*}\to\mathcal{V}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ​(a)=Σ​a∈𝒱,∀a∈𝒱∗formulae-sequenceΣ𝑎Σ𝑎𝒱for-all𝑎superscript𝒱\displaystyle\Sigma(a)=\Sigma a\in\mathcal{V},~{}\forall a\in\mathcal{V}^{\*} |  | (100) |

The portfolio variance is formed by applying the linear map a:𝒱→ℝ:𝑎→𝒱ℝa:\mathcal{V}\to\mathbb{R} to Σ​(a)∈𝒱Σ𝑎𝒱\Sigma(a)\in\mathcal{V}: Var​(a​(v))=a​(Σ​(a))Var𝑎𝑣𝑎Σ𝑎\mathrm{Var}(a(v))=a(\Sigma(a)).
If the square matrix ΣΣ\Sigma is singular, then its kernel ker​ΣkerΣ\mathrm{ker}\Sigma is not trivial (i.e. contains elements other than the zero vector). 𝒱∗superscript𝒱\mathcal{V}^{\*} can therefore be decomposed into two subspaces:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱∗=ker​Σ⊕ker​Σ⟂superscript𝒱direct-sumkerΣkersuperscriptΣperpendicular-to\displaystyle\mathcal{V}^{\*}=\mathrm{ker}\Sigma\oplus\mathrm{ker}\Sigma^{\perp} |  | (101) |

Suppose ker​Σ⟂kersuperscriptΣperpendicular-to\mathrm{ker}\Sigma^{\perp} has dimension n𝑛n. ker​ΣkerΣ\mathrm{ker}\Sigma has dimension m−n𝑚𝑛m-n for the dimensions of subspaces sum up to the dimension of 𝒱∗superscript𝒱\mathcal{V}^{\*}. We may switch to a new orthonormal basis {e1∗,e2∗,⋯,em∗,k1∗,k2∗,⋯,km−n∗}subscriptsuperscript𝑒1subscriptsuperscript𝑒2⋯subscriptsuperscript𝑒𝑚subscriptsuperscript𝑘1subscriptsuperscript𝑘2⋯subscriptsuperscript𝑘𝑚𝑛\{e^{\*}\_{1},e^{\*}\_{2},\cdots,e^{\*}\_{m},k^{\*}\_{1},k^{\*}\_{2},\cdots,k^{\*}\_{m-n}\} in consistency with the decomposition Eq. [101](#S6.E101 "In 6.5 E. The support of a multivariate normal distribution ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance"), in the sense that e1∗,e2∗,⋯,em∗

subscriptsuperscript𝑒1subscriptsuperscript𝑒2⋯subscriptsuperscript𝑒𝑚e^{\*}\_{1},e^{\*}\_{2},\cdots,e^{\*}\_{m} span ker​Σ⟂kersuperscriptΣperpendicular-to\mathrm{ker}\Sigma^{\perp} and k1∗,k2∗,⋯,km−n∗

subscriptsuperscript𝑘1subscriptsuperscript𝑘2⋯subscriptsuperscript𝑘𝑚𝑛k^{\*}\_{1},k^{\*}\_{2},\cdots,k^{\*}\_{m-n} span ker​ΣkerΣ\mathrm{ker}\Sigma. Now get back the original space of asset returns 𝒱𝒱\mathcal{V}, we may select a new basis
  
{e1,e2,⋯,em,k1,k2,⋯,km−n}subscript𝑒1subscript𝑒2⋯subscript𝑒𝑚subscript𝑘1subscript𝑘2⋯subscript𝑘𝑚𝑛\{e\_{1},e\_{2},\cdots,e\_{m},k\_{1},k\_{2},\cdots,k\_{m-n}\}, dual to {e1∗,e2∗,⋯,em∗,k1∗,k2∗,⋯,km−n∗}subscriptsuperscript𝑒1subscriptsuperscript𝑒2⋯subscriptsuperscript𝑒𝑚subscriptsuperscript𝑘1subscriptsuperscript𝑘2⋯subscriptsuperscript𝑘𝑚𝑛\{e^{\*}\_{1},e^{\*}\_{2},\cdots,e^{\*}\_{m},k^{\*}\_{1},k^{\*}\_{2},\cdots,k^{\*}\_{m-n}\}, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ei∗​(ej)=subscriptsuperscript𝑒𝑖subscript𝑒𝑗absent\displaystyle e^{\*}\_{i}(e\_{j})= | δi−jsubscript𝛿𝑖𝑗\displaystyle\delta\_{i-j} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ki∗​(kj)=subscriptsuperscript𝑘𝑖subscript𝑘𝑗absent\displaystyle k^{\*}\_{i}(k\_{j})= | δi−jsubscript𝛿𝑖𝑗\displaystyle\delta\_{i-j} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ei∗​(kj)=subscriptsuperscript𝑒𝑖subscript𝑘𝑗absent\displaystyle e^{\*}\_{i}(k\_{j})= | 00\displaystyle 0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ki∗​(ej)=subscriptsuperscript𝑘𝑖subscript𝑒𝑗absent\displaystyle k^{\*}\_{i}(e\_{j})= | 00\displaystyle 0 |  |

Any v∈𝒱𝑣𝒱v\in\mathcal{V} can be expressed by

|  |  |  |  |
| --- | --- | --- | --- |
|  | v=∑i=1mui​ei+∑i=1m−nwi​ki𝑣superscriptsubscript𝑖1𝑚subscript𝑢𝑖subscript𝑒𝑖superscriptsubscript𝑖1𝑚𝑛subscript𝑤𝑖subscript𝑘𝑖\displaystyle v=\sum\_{i=1}^{m}u\_{i}e\_{i}+\sum\_{i=1}^{m-n}w\_{i}k\_{i} |  | (102) |

Suppose 𝒰𝒰\mathcal{U} denotes the linear subspace spanned by e1,e2,⋯,em

subscript𝑒1subscript𝑒2⋯subscript𝑒𝑚e\_{1},e\_{2},\cdots,e\_{m}. 𝒰𝒰\mathcal{U} is in fact the dual space of ker​Σ⟂kersuperscriptΣperpendicular-to\mathrm{ker}\Sigma^{\perp}. We will show that the support of the reference measure P𝑃P is indeed the linear subspace 𝒰𝒰\mathcal{U} shifted by the vector of average asset returns μ𝜇\mu:

Theorem *Given a finite-dimensional topological vector space 𝒱𝒱\mathcal{V} and its Borel α𝛼\alpha-algebra ℱℱ\mathcal{F}, the support of a measure P𝑃P on (𝒱,ℱ)𝒱ℱ(\mathcal{V},\mathcal{F}) is {v∈𝒱:v−μ∈𝒰}conditional-set𝑣𝒱𝑣𝜇𝒰\{v\in\mathcal{V}:v-\mu\in\mathcal{U}\} if P𝑃P provides a multivariate distribution 𝒩​(μ,Σ)𝒩𝜇Σ\mathcal{N}(\mu,\Sigma).*
  
  
*Proof*
For every v∈ker​Σ𝑣kerΣv\in\mathrm{ker}\Sigma, consider the variance of a​(v)𝑎𝑣a(v) (v𝑣v is a random vector here):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​(a​(v))=aT​Σ​a=0Var𝑎𝑣superscript𝑎𝑇Σ𝑎0\displaystyle\mathrm{Var}(a(v))=a^{T}\Sigma a=0 |  | (103) |

The zero variance implies that a𝑎a carries the measure P𝑃P on 𝒱𝒱\mathcal{V} to a Dirac measure Pasubscript𝑃𝑎{P\_{a}} on ℝℝ\mathbb{R}

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pa​(A)=P​(a−1​(A)),∀A∈{A⊆ℝ:a−1​(A)∈ℱ}formulae-sequencesubscript𝑃𝑎𝐴𝑃superscript𝑎1𝐴for-all𝐴conditional-set𝐴ℝsuperscript𝑎1𝐴ℱ\displaystyle{P\_{a}}(A)=P(a^{-1}(A)),~{}\forall A\in\{A\subseteq\mathbb{R}:a^{-1}(A)\in\mathcal{F}\} |  | (104) |

Suppose s​u​p​p​(Pa)={sa}𝑠𝑢𝑝𝑝subscript𝑃𝑎subscript𝑠𝑎supp(P\_{a})=\{s\_{a}\} where sa∈ℝsubscript𝑠𝑎ℝs\_{a}\in\mathbb{R}. We can show that s​u​p​p​(P)𝑠𝑢𝑝𝑝𝑃supp(P) should only include elements in 𝒱𝒱\mathcal{V} that is projected to sasubscript𝑠𝑎s\_{a}. More formally, with the projection map 𝒫:𝒱→ker​Σ:𝒫→𝒱kerΣ\mathcal{P}:\mathcal{V}\to\mathrm{ker}\Sigma, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | {v∈𝒱:∃a∈ker​Σ,a​(v)≠sa}∩s​u​p​p​(P)=∅conditional-set𝑣𝒱formulae-sequence𝑎kerΣ𝑎𝑣subscript𝑠𝑎𝑠𝑢𝑝𝑝𝑃\displaystyle\{v\in\mathcal{V}:\exists a\in\mathrm{ker}\Sigma,a(v)\neq s\_{a}\}\cap supp(P)=\emptyset |  | (105) |

In fact, for a given v∈𝒱𝑣𝒱v\in\mathcal{V}, suppose there exists a∈ker​Σ𝑎kerΣa\in\mathrm{ker}\Sigma such that a​(v)≠s0𝑎𝑣subscript𝑠0a(v)\neq s\_{0}. a​(v)𝑎𝑣a(v) is not in the s​u​p​p​(P~)𝑠𝑢𝑝𝑝~𝑃supp(\tilde{P}), suggesting the existence of an open neighborhood Na​(v)⊆ℝsubscript𝑁𝑎𝑣ℝN\_{a(v)}\subseteq\mathbb{R} such that Pa​(Na​(v))=0subscript𝑃𝑎subscript𝑁𝑎𝑣0{P\_{a}}(N\_{a(v)})=0. Since the linear map a𝑎a is continuous, a−1​(Na​(v))superscript𝑎1subscript𝑁𝑎𝑣a^{-1}(N\_{a(v)}) is an open neighborhood of v𝑣v and

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(a−1​(Na​(v)))=Pa​(Na​(v))=0𝑃superscript𝑎1subscript𝑁𝑎𝑣subscript𝑃𝑎subscript𝑁𝑎𝑣0\displaystyle P(a^{-1}(N\_{a(v)}))={P\_{a}}(N\_{a(v)})=0 |  | (106) |

As a result, v∉s​u​p​p​(P)𝑣𝑠𝑢𝑝𝑝𝑃v\not\in supp(P) which proves Eq. [105](#S6.E105 "In 6.5 E. The support of a multivariate normal distribution ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance").

Now we consider the set S:={v∈𝒱:a​(v)=sa,∀a∈ker​Σ}assign𝑆conditional-set𝑣𝒱formulae-sequence𝑎𝑣subscript𝑠𝑎for-all𝑎kerΣS:=\{v\in\mathcal{V}:a(v)=s\_{a},\forall a\in\mathrm{ker}\Sigma\}. For a given vs∈Ssubscript𝑣𝑠𝑆v\_{s}\in S, every v∈S𝑣𝑆v\in S satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | a​(v−vs)=a​(v)−a​(vs)=0,∀a∈ker​Σformulae-sequence𝑎𝑣subscript𝑣𝑠𝑎𝑣𝑎subscript𝑣𝑠0for-all𝑎kerΣ\displaystyle a(v-v\_{s})=a(v)-a(v\_{s})=0,~{}\forall a\in\mathrm{ker}\Sigma |  | (107) |

suggesting that v−vs∈𝒰𝑣subscript𝑣𝑠𝒰v-v\_{s}\in\mathcal{U}. Therefore S={v∈𝒱:v−vs∈𝒰}𝑆conditional-set𝑣𝒱𝑣subscript𝑣𝑠𝒰S=\{v\in\mathcal{V}:v-v\_{s}\in\mathcal{U}\}.
Regard 𝒰𝒰\mathcal{U} as a topological linear subspace of 𝒱𝒱\mathcal{V} equipped with the relative topology. ℱ~~ℱ\tilde{\mathcal{F}} is the Borel σ𝜎\sigma-algebra on 𝒰𝒰\mathcal{U}. We may define a new probability space (𝒰,ℱ~,P~)𝒰~ℱ~𝑃(\mathcal{U},\tilde{\mathcal{F}},\tilde{P}) by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P~​(A∩𝒰)=~𝑃𝐴𝒰absent\displaystyle\tilde{P}(A\cap\mathcal{U})= | P​(A),∀A∈ℱ  𝑃𝐴for-all𝐴 ℱ\displaystyle P(A),~{}~{}\forall A\in\mathcal{F} |  | (108) |

One can verify that this probability space is well defined. Now we would like to show that s​u​p​p​(P~)=𝒰𝑠𝑢𝑝𝑝~𝑃𝒰supp(\tilde{P})=\mathcal{U}. In fact, assuming this is true, then for arbitrary v∈S𝑣𝑆v\in S every open neigborhood N​(v)𝑁𝑣N(v) has positive measure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(N​(v))=P~​(N​(v)∩𝒰)>0𝑃𝑁𝑣~𝑃𝑁𝑣𝒰0\displaystyle P(N(v))=\tilde{P}(N(v)\cap\mathcal{U})>0 |  | (109) |

This immediately leads to the result s​u​p​p​(P)=S𝑠𝑢𝑝𝑝𝑃𝑆supp(P)=S. In particular, from the property of the multivariate normal distribution, s​u​p​p​(P)𝑠𝑢𝑝𝑝𝑃supp(P) includes the vector μ𝜇\mu of average asset returns. This means that μ∈S𝜇𝑆\mu\in S, and thus the support of P𝑃P can be written as s​u​p​p​(P)=S={v∈𝒱:v−μ∈𝒰}𝑠𝑢𝑝𝑝𝑃𝑆conditional-set𝑣𝒱𝑣𝜇𝒰supp(P)=S=\{v\in\mathcal{V}:v-\mu\in\mathcal{U}\}.

Now we only need to show that s​u​p​p​(P~)=𝒰𝑠𝑢𝑝𝑝~𝑃𝒰supp(\tilde{P})=\mathcal{U}.
Consider the projection map 𝒫:𝒱→𝒰:𝒫→𝒱𝒰\mathcal{P}:\mathcal{V}\to\mathcal{U} that sends v=(u1,u2,⋯,um,w1,w2,⋯,wm−n)𝑣subscript𝑢1subscript𝑢2⋯subscript𝑢𝑚subscript𝑤1subscript𝑤2⋯subscript𝑤𝑚𝑛v=(u\_{1},u\_{2},\cdots,u\_{m},w\_{1},w\_{2},\cdots,w\_{m-n}) to u=(u1,u2,⋯,um)𝑢subscript𝑢1subscript𝑢2⋯subscript𝑢𝑚u=(u\_{1},u\_{2},\cdots,u\_{m}). The projection results in the marginal distribution w.r.t u1,u2,⋯,um

subscript𝑢1subscript𝑢2⋯subscript𝑢𝑚u\_{1},u\_{2},\cdots,u\_{m}. This marginal distribution characterises a measure P′superscript𝑃′P^{\prime} on the subspace 𝒰𝒰\mathcal{U}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P′​(A)=P​(𝒫−1​(A)),∀A∈{A⊆𝒰:𝒫−1​(A)∈ℱ}formulae-sequencesuperscript𝑃′𝐴𝑃superscript𝒫1𝐴for-all𝐴conditional-set𝐴𝒰superscript𝒫1𝐴ℱ\displaystyle P^{\prime}(A)=P(\mathcal{P}^{-1}(A)),~{}\forall A\in\{A\subseteq\mathcal{U}:\mathcal{P}^{-1}(A)\in\mathcal{F}\} |  | (110) |

For any A∈ℱ𝐴ℱA\in\mathcal{F},

|  |  |  |  |
| --- | --- | --- | --- |
|  | P′​(A∩𝒰)=superscript𝑃′𝐴𝒰absent\displaystyle P^{\prime}(A\cap\mathcal{U})= | P​(𝒫−1​(A∩𝒰))𝑃superscript𝒫1𝐴𝒰\displaystyle P(\mathcal{P}^{-1}(A\cap\mathcal{U})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | P~​(𝒫−1​(A∩𝒰)∩𝒰)~𝑃superscript𝒫1𝐴𝒰𝒰\displaystyle\tilde{P}(\mathcal{P}^{-1}(A\cap\mathcal{U})\cap\mathcal{U}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | P~​(A∩𝒰)~𝑃𝐴𝒰\displaystyle\tilde{P}(A\cap\mathcal{U}) |  | (111) |

Therefore, the two measures P~~𝑃\tilde{P} and P′superscript𝑃′P^{\prime} coincide, and we only need to prove s​u​p​p​(P′)=𝒰𝑠𝑢𝑝𝑝superscript𝑃′𝒰supp(P^{\prime})=\mathcal{U}. The marginal distribution from projection 𝒫𝒫\mathcal{P} is apparently multivariate normal (every linear combination of the elements in u𝑢u is also a linear combination of the elements in v∈𝒫−1​(u)𝑣superscript𝒫1𝑢v\in\mathcal{P}^{-1}(u) thus normally distributed).

The covariance matrix Σ~~Σ\tilde{\Sigma} of the truncated random vector u𝑢u is invertible.
In fact, because Σ​(a)Σ𝑎\Sigma(a) is not a zero vector for every non-zero a∈ker​Σ⟂𝑎kersuperscriptΣperpendicular-toa\in\mathrm{ker}\Sigma^{\perp}, the linear map between two m𝑚m-dimensional vector spaces Σ|ker​Σ⟂:ker​Σ⟂→Σ​(ker​Σ⟂):evaluated-atΣkersuperscriptΣperpendicular-to→kersuperscriptΣperpendicular-toΣkersuperscriptΣperpendicular-to\Sigma|\_{\mathrm{ker}\Sigma^{\perp}}:\mathrm{ker}\Sigma^{\perp}\to\Sigma(\mathrm{ker}\Sigma^{\perp}) is invertible. Represented by a m×m𝑚𝑚m\times m matrix, Σ|ker​Σ⟂evaluated-atΣkersuperscriptΣperpendicular-to\Sigma|\_{\mathrm{ker}\Sigma^{\perp}} has only non-zero eigenvalues. Since it is also positive semi-definite (for Var​(a​(v))=a​(Σ​(a))≥0,∀a∈ker​Σ⟂⊆𝒱∗formulae-sequenceVar𝑎𝑣𝑎Σ𝑎0for-all𝑎kersuperscriptΣperpendicular-tosuperscript𝒱\mathrm{Var}(a(v))=a(\Sigma(a))\geq 0,~{}\forall a\in\mathrm{ker}\Sigma^{\perp}\subseteq\mathcal{V}^{\*}), it must be positive definite. We conclude that for every non-zero a∈ker​Σ⟂𝑎kersuperscriptΣperpendicular-toa\in\mathrm{ker}\Sigma^{\perp}, Var​(a​(v))=a​(Σ|ker​Σ⟂​(a))>0Var𝑎𝑣𝑎evaluated-atΣkersuperscriptΣperpendicular-to𝑎0\mathrm{Var}(a(v))=a(\Sigma|\_{\mathrm{ker}\Sigma^{\perp}}(a))>0. If we expand a​(v)𝑎𝑣a(v) component-wise according to Eq. [102](#S6.E102 "In 6.5 E. The support of a multivariate normal distribution ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | a​(v)=𝑎𝑣absent\displaystyle a(v)= | ∑i=1mui​a​(ei)+∑i=1m−nwi​a​(ki)superscriptsubscript𝑖1𝑚subscript𝑢𝑖𝑎subscript𝑒𝑖superscriptsubscript𝑖1𝑚𝑛subscript𝑤𝑖𝑎subscript𝑘𝑖\displaystyle\sum\_{i=1}^{m}u\_{i}a(e\_{i})+\sum\_{i=1}^{m-n}w\_{i}a(k\_{i}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | a​(∑i=1mui​ei)=a​(u)𝑎superscriptsubscript𝑖1𝑚subscript𝑢𝑖subscript𝑒𝑖𝑎𝑢\displaystyle a\left(\sum\_{i=1}^{m}u\_{i}e\_{i}\right)=a(u) |  | (112) |

Therefore aT​Σ~​a=Var​(a​(u))=Var​(a​(v))>0superscript𝑎𝑇~Σ𝑎Var𝑎𝑢Var𝑎𝑣0a^{T}\tilde{\Sigma}a=\mathrm{Var}(a(u))=\mathrm{Var}(a(v))>0 for every nonzero a∈ker​Σ⟂𝑎kersuperscriptΣperpendicular-toa\in\mathrm{ker}\Sigma^{\perp}. As a result, Σ~​a~Σ𝑎\tilde{\Sigma}a is positive-definite and thus invertible. Under the measure P′superscript𝑃′P^{\prime}, the random vector u𝑢u follows a multivariate normal distribution with a non-singular covariance matrix. It is supported by the entire subspace 𝒰𝒰\mathcal{U}, i.e. s​u​p​p​(P′)=𝒰𝑠𝑢𝑝𝑝superscript𝑃′𝒰supp(P^{\prime})=\mathcal{U}. □□\square

For a multivariate distribution 𝒩​(μ,Σ)𝒩𝜇Σ\mathcal{N}(\mu,\Sigma),
the support s​u​p​p​(P)={v∈𝒱:v−μ∈𝒰}𝑠𝑢𝑝𝑝𝑃conditional-set𝑣𝒱𝑣𝜇𝒰supp(P)=\{v\in\mathcal{V}:v-\mu\in\mathcal{U}\} only depends on the vector μ𝜇\mu and the kernel of ΣΣ\Sigma. It is clear that under the Kullback-Leibler divergence the worst-case measure shares the same support.
In fact, the worst-case distribution is 𝒩​(μK​L,ΣK​L)𝒩subscript𝜇𝐾𝐿subscriptΣ𝐾𝐿\mathcal{N}(\mu\_{KL},\Sigma\_{KL}) where μK​Lsubscript𝜇𝐾𝐿\mu\_{KL} and ΣK​LsubscriptΣ𝐾𝐿\Sigma\_{KL} are given in Eq. [46](#S4.E46 "In 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"). Assuming θ𝜃\theta is sufficiently small so that I−2​θ​Σ​A𝐼2𝜃Σ𝐴I-2\theta\Sigma A is invertible, ΣK​L​a=0subscriptΣ𝐾𝐿𝑎0\Sigma\_{KL}a=0 if and only if ΣK​L=0subscriptΣ𝐾𝐿0\Sigma\_{KL}=0 for every a∈𝒱∗𝑎superscript𝒱a\in\mathcal{V}^{\*}. Therefore, ΣK​LsubscriptΣ𝐾𝐿\Sigma\_{KL} and ΣΣ\Sigma share the same kernel and therefore the same subspace 𝒰⊆𝒱𝒰𝒱\mathcal{U}\subseteq\mathcal{V}. In addition, μK​L−μ∈𝒰subscript𝜇𝐾𝐿𝜇𝒰\mu\_{KL}-\mu\in\mathcal{U} because for every a∈ker​Σ𝑎kerΣa\in\mathrm{ker}\Sigma we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | a​(μK​L−μ)=𝑎subscript𝜇𝐾𝐿𝜇absent\displaystyle a(\mu\_{KL}-\mu)= | a​(2​θ​Σ​A​(I−2​θ​Σ​A)−1​μ)𝑎2𝜃Σ𝐴superscript𝐼2𝜃Σ𝐴1𝜇\displaystyle a\left(2\theta\Sigma A(I-2\theta\Sigma A)^{-1}\mu\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 2​θ​(Σ​a)T​A​(I−2​θ​Σ​A)−1​μ2𝜃superscriptΣ𝑎𝑇𝐴superscript𝐼2𝜃Σ𝐴1𝜇\displaystyle 2\theta(\Sigma a)^{T}A(I-2\theta\Sigma A)^{-1}\mu |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 00\displaystyle 0 |  | (113) |

As a result, the support of the worst-case measure is {v∈𝒱:v−μK​L∈𝒰}={v∈𝒱:v−μ∈𝒰}conditional-set𝑣𝒱𝑣subscript𝜇𝐾𝐿𝒰conditional-set𝑣𝒱𝑣𝜇𝒰\{v\in\mathcal{V}:v-\mu\_{KL}\in\mathcal{U}\}=\{v\in\mathcal{V}:v-\mu\in\mathcal{U}\}, same as the support of the reference measure.

On the other hand, the worst-case measured resulted from the Wasserstein approach can have different support. According to Eq. [44](#S4.E44 "In 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"), the worst-case covariance matrix ΣWsubscriptΣ𝑊\Sigma\_{W} has a different kernel in general. In addition, μW−μ=β​A​(B−β​A)−1​μsubscript𝜇𝑊𝜇𝛽𝐴superscript𝐵𝛽𝐴1𝜇\mu\_{W}-\mu=\beta A(B-\beta A)^{-1}\mu is not dependent on ΣΣ\Sigma, thus not linked to the subspace 𝒰𝒰\mathcal{U}. Setting α=0𝛼0\alpha=0 in Eq. [44](#S4.E44 "In 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") provides a particularly interesting case, where the worst-case measure is given by a measure-preserving linear map g:𝒱→𝒱:𝑔→𝒱𝒱g:\mathcal{V}\to\mathcal{V} given by Eq. [6.4](#S6.Ex37 "6.4 D. Worst-case Portfolio Variance ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance").
As a result, the support of the worst-case measure can be obtained using the same map, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | {v∈𝒱:g−1​(v)−μ∈𝒰}conditional-set𝑣𝒱superscript𝑔1𝑣𝜇𝒰\displaystyle\left\{v\in\mathcal{V}:g^{-1}(v)-\mu\in\mathcal{U}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | {v∈𝒱:(I−β​B−1​A)​v−μ∈𝒰}conditional-set𝑣𝒱𝐼𝛽superscript𝐵1𝐴𝑣𝜇𝒰\displaystyle\left\{v\in\mathcal{V}:(I-\beta B^{-1}A)v-\mu\in\mathcal{U}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | {v∈𝒱:v−(I−β​B−1​A)−1​μ∈{(I−β​B−1​A)−1​u:u∈𝒰}}conditional-set𝑣𝒱𝑣superscript𝐼𝛽superscript𝐵1𝐴1𝜇conditional-setsuperscript𝐼𝛽superscript𝐵1𝐴1𝑢𝑢𝒰\displaystyle\left\{v\in\mathcal{V}:v-(I-\beta B^{-1}A)^{-1}\mu\in\{(I-\beta B^{-1}A)^{-1}u:u\in\mathcal{U}\}\right\} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | {v∈𝒱:v−μW∈𝒰W}conditional-set𝑣𝒱𝑣subscript𝜇𝑊subscript𝒰𝑊\displaystyle\left\{v\in\mathcal{V}:v-\mu\_{W}\in\mathcal{U}\_{W}\right\} |  | (114) |

𝒰W:={(I−β​B−1​A)−1​u:u∈𝒰}⊆𝒱assignsubscript𝒰𝑊conditional-setsuperscript𝐼𝛽superscript𝐵1𝐴1𝑢𝑢𝒰𝒱\mathcal{U}\_{W}:=\{(I-\beta B^{-1}A)^{-1}u:u\in\mathcal{U}\}\subseteq\mathcal{V} is the linear subspace (perpendicular to ker​ΣWkersubscriptΣ𝑊\mathrm{ker}\Sigma\_{W}) that corresponds to the worst-case scenario under the Wasserstein approach.

### 6.6 F. Verification of the Wasserstein approach

Sec. [6.5](#S6.SS5 "6.5 E. The support of a multivariate normal distribution ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") shows that under the Wasserstein approach the worst-case measure does alter the support. Now the question is whether the approach searches over all alternative measures. Unlike f𝑓f-divergence that is only capable of measuring distance between equivalent measures, the Wasserstein metric provides a finite distance between non-equivalent measures as well. Therefore the Wasserstein approach should be able to find out the worst-case measure from all equivalent and non-equivalent measures. In this section, we will verify it for the example of portfolio variance. In particular, we will find out a worst-case linear map g∗:𝒱→𝒱:superscript𝑔→𝒱𝒱g^{\*}:\mathcal{V}\to\mathcal{V} by searching over the entire space of linear maps. We will verify that Eq. [46](#S4.E46 "In 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") (with α=0𝛼0\alpha=0) can be given by the worst-case linear map.

Theorem *Given a probability space (𝒱,ℱ,P)𝒱ℱ𝑃(\mathcal{V},\mathcal{F},P) where 𝒱𝒱\mathcal{V} is a finite-dimensional vector space and P𝑃P provides a multivariate distribution 𝒩​(μ,Σ)𝒩𝜇Σ\mathcal{N}(\mu,\Sigma), there exists a worst-case linear map g∗:𝒱→𝒱:superscript𝑔→𝒱𝒱g^{\*}:\mathcal{V}\to\mathcal{V} in the sense of Eq. [15](#S3.E15 "In 3.1 Wasserstein Formulation of the Model Risk Problem ‣ 3 Theory ‣ Model Risk Measurement under Wasserstein Distance"), i.e.*

|  |  |  |  |
| --- | --- | --- | --- |
|  | g∗​(x)=arg⁡maxy∈𝒱⁡[yT​A​y−(x−y)T​B​(x−y)β]superscript𝑔𝑥subscript𝑦𝒱superscript𝑦𝑇𝐴𝑦superscript𝑥𝑦𝑇𝐵𝑥𝑦𝛽\displaystyle g^{\*}(x)=\arg\max\_{y\in\mathcal{V}}\left[y^{T}Ay-\frac{(x-y)^{T}B(x-y)}{\beta}\right] |  | (115) |

for every non-zero x∈𝒱𝑥𝒱x\in\mathcal{V}, as long as B−β​A𝐵𝛽𝐴B-\beta A is positive definite.
  
*Proof*
Given a non-zero x∈𝒱𝑥𝒱x\in\mathcal{V}, every non-zero y∈𝒱𝑦𝒱y\in\mathcal{V} can be expressed by y=g​(x)𝑦𝑔𝑥y=g(x) where g𝑔g is some linear map (not unique) g:𝒱→𝒱:𝑔→𝒱𝒱g:\mathcal{V}\to\mathcal{V}. The problem Eq. [115](#S6.E115 "In 6.6 F. Verification of the Wasserstein approach ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") is therefore equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | g∗​(x)=arg⁡maxg∈𝔏​(𝒱,𝒱)⁡[g​(x)T​A​g​(x)−(x−g​(x))T​B​(x−g​(x))β]​(x)superscript𝑔𝑥subscript𝑔𝔏𝒱𝒱𝑔superscript𝑥𝑇𝐴𝑔𝑥superscript𝑥𝑔𝑥𝑇𝐵𝑥𝑔𝑥𝛽𝑥\displaystyle g^{\*}(x)=\arg\max\_{g\in\mathfrak{L}(\mathcal{V},\mathcal{V})}\left[g(x)^{T}Ag(x)-\frac{\left(x-g(x)\right)^{T}B\left(x-g(x)\right)}{\beta}\right](x) |  | (116) |

where 𝔏​(𝒱,𝒱)𝔏𝒱𝒱\mathfrak{L}(\mathcal{V},\mathcal{V}) is the space of all linear maps from 𝒱𝒱\mathcal{V} to 𝒱𝒱\mathcal{V}.
Choosing a orthonormal basis for 𝒱𝒱\mathcal{V} allows us to represent g𝑔g by a square matrix, and the linear map g​(x)𝑔𝑥g(x) by matrix multiplication g​x𝑔𝑥gx. The expression inside the square bracket in Eq. [116](#S6.E116 "In 6.6 F. Verification of the Wasserstein approach ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") is then transformed into

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (g​x)T​A​g​x−(x−g​x)T​B​(x−g​x)βsuperscript𝑔𝑥𝑇𝐴𝑔𝑥superscript𝑥𝑔𝑥𝑇𝐵𝑥𝑔𝑥𝛽\displaystyle(gx)^{T}Agx-\frac{\left(x-gx\right)^{T}B\left(x-gx\right)}{\beta} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | −1β​xT​(gT−B​(B−β​A)−1)​(B−β​A)​(g−(B−β​A)−1​B)​x1𝛽superscript𝑥𝑇superscript𝑔𝑇𝐵superscript𝐵𝛽𝐴1𝐵𝛽𝐴𝑔superscript𝐵𝛽𝐴1𝐵𝑥\displaystyle-\frac{1}{\beta}x^{T}\left(g^{T}-B(B-\beta A)^{-1}\right)(B-\beta A)\left(g-(B-\beta A)^{-1}B\right)x |  | (117) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −1β​xT​(B−B​(B−β​A)−1​B)​x1𝛽superscript𝑥𝑇𝐵𝐵superscript𝐵𝛽𝐴1𝐵𝑥\displaystyle-\frac{1}{\beta}x^{T}\left(B-B(B-\beta A)^{-1}B\right)x |  |

Since B−β​A𝐵𝛽𝐴B-\beta A is positive-definite, the first term in Eq. [6.6](#S6.Ex53 "6.6 F. Verification of the Wasserstein approach ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") is either zero or negative. It reaches zero (and hence Eq. [6.6](#S6.Ex53 "6.6 F. Verification of the Wasserstein approach ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") reaches its maximum value) if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | (g−(B−β​A)−1​B)​x=0𝑔superscript𝐵𝛽𝐴1𝐵𝑥0\displaystyle\left(g-(B-\beta A)^{-1}B\right)x=0 |  | (118) |

or equivalently

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(x)=(B−β​A)−1​B​x𝑔𝑥superscript𝐵𝛽𝐴1𝐵𝑥\displaystyle g(x)=(B-\beta A)^{-1}Bx |  | (119) |

This allows to rewrite Eq. [116](#S6.E116 "In 6.6 F. Verification of the Wasserstein approach ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") by

|  |  |  |  |
| --- | --- | --- | --- |
|  | g∗​(x)=(B−β​A)−1​B​xsuperscript𝑔𝑥superscript𝐵𝛽𝐴1𝐵𝑥\displaystyle g^{\*}(x)=(B-\beta A)^{-1}Bx |  | (120) |

The linear map g∗superscript𝑔g^{\*} given by the square matrix (B−β​A)−1​Bsuperscript𝐵𝛽𝐴1𝐵(B-\beta A)^{-1}B satisfies Eq. [120](#S6.E120 "In 6.6 F. Verification of the Wasserstein approach ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") and thus solves Eq. [116](#S6.E116 "In 6.6 F. Verification of the Wasserstein approach ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") for every non-zero x∈𝒱𝑥𝒱x\in\mathcal{V}.
□□\square

It is noted that in the problem of portfolio variance risk, both square matrices A𝐴A and B𝐵B are symmetric and positive definite. Therefore if the positive multiplier β𝛽\beta is sufficiently small, B−β​A𝐵𝛽𝐴B-\beta A is also positive definite satisfying the condition assumed in the theorem above.
Now the worst-case linear map g∗superscript𝑔g^{\*} transforms the vector of asset returns from μ𝜇\mu to (B−β​A)−1​B​μsuperscript𝐵𝛽𝐴1𝐵𝜇(B-\beta A)^{-1}B\mu, and the covariance matrix from ΣΣ\Sigma to (B−β​A)−1​B​Σ​B​(B−β​A)−1superscript𝐵𝛽𝐴1𝐵Σ𝐵superscript𝐵𝛽𝐴1(B-\beta A)^{-1}B\Sigma B(B-\beta A)^{-1}, same as the expressions given in Eq. [46](#S4.E46 "In 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") (with α=0𝛼0\alpha=0). This verifies that the Wasserstein approach indeed searches over the entire space 𝔏​(𝒱,𝒱)𝔏𝒱𝒱\mathfrak{L}(\mathcal{V},\mathcal{V}) of linear maps. It results in a measure that corresponds to the worst-case linear map g∗superscript𝑔g^{\*}.

### 6.7 G. Robust MVO Portfolio (Kullback-Leibler divergence)

According to Eq. [4.4](#S4.Ex9 "4.4 Robust Portfolio Optimisation and Correlation Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"), we consider the problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxQ∈ℳ⁡EQ​((X−μ−k)T​a​aT​(X−μ−k))subscript𝑄ℳsuperscript𝐸𝑄superscript𝑋𝜇𝑘𝑇𝑎superscript𝑎𝑇𝑋𝜇𝑘\displaystyle\max\_{Q\in\mathscr{M}}E^{Q}\left((X-\mu-k)^{T}aa^{T}(X-\mu-k)\right) |  | (121) |

Since X−μ−k∼𝒩​(−k,Σ)similar-to𝑋𝜇𝑘𝒩𝑘ΣX-\mu-k\sim\mathcal{N}(-k,\Sigma), under the Kullback-Leibler divergence the covariance matrix and the mean of the worst-case measure are given according to Eq. [46](#S4.E46 "In 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance") (remember aT​k=λ/2superscript𝑎𝑇𝑘𝜆2a^{T}k=\lambda/2):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΣK​L=subscriptΣ𝐾𝐿absent\displaystyle\Sigma\_{KL}= | (I−2​θ​Σ​A)−1​Σsuperscript𝐼2𝜃Σ𝐴1Σ\displaystyle(I-2\theta\Sigma A)^{-1}\Sigma |  | (122) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | μK​L=subscript𝜇𝐾𝐿absent\displaystyle\mu\_{KL}= | (μ+k)−(I−2​θ​Σ​A)−1​k𝜇𝑘superscript𝐼2𝜃Σ𝐴1𝑘\displaystyle(\mu+k)-\left(I-2\theta\Sigma A\right)^{-1}k |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | μ−λ​θ​(I−2​θ​Σ​A)−1​Σ​a𝜇𝜆𝜃superscript𝐼2𝜃Σ𝐴1Σ𝑎\displaystyle\mu-\lambda\theta(I-2\theta\Sigma A)^{-1}\Sigma a |  |

Using the Wassertein approach, however, the worst-case measure has different covariance matrix and mean (Eq. [44](#S4.E44 "In 4.3 Model Risk in Portfolio Variance ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance")):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΣW=subscriptΣ𝑊absent\displaystyle\Sigma\_{W}= | (I−β​B−1​A)−1​Σ​(I−β​A​B−1)−1superscript𝐼𝛽superscript𝐵1𝐴1Σsuperscript𝐼𝛽𝐴superscript𝐵11\displaystyle(I-\beta B^{-1}A)^{-1}\Sigma(I-\beta AB^{-1})^{-1} |  | (123) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | μW=subscript𝜇𝑊absent\displaystyle\mu\_{W}= | (μ+k)−(I−β​B−1​A)−1​k𝜇𝑘superscript𝐼𝛽superscript𝐵1𝐴1𝑘\displaystyle(\mu+k)-(I-\beta B^{-1}A)^{-1}k |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | μ−λ2​β​(I−β​B−1​A)−1​B−1​a𝜇𝜆2𝛽superscript𝐼𝛽superscript𝐵1𝐴1superscript𝐵1𝑎\displaystyle\mu-\frac{\lambda}{2}\beta(I-\beta B^{-1}A)^{-1}B^{-1}a |  |

We may then formulate the optimal asset allocation a∗superscript𝑎a^{\*} under the worst-case measure. According to Eq. [52](#S4.E52 "In 4.4 Robust Portfolio Optimisation and Correlation Risk ‣ 4 Application ‣ Model Risk Measurement under Wasserstein Distance"), the problem is formulated in the following form under the Kullback-Leibler divergence.

|  |  |  |  |
| --- | --- | --- | --- |
|  | minasubscript𝑎\displaystyle\min\_{a}\, | aT​ΣK​L​a−λ​aT​μK​Lsuperscript𝑎𝑇subscriptΣ𝐾𝐿𝑎𝜆superscript𝑎𝑇subscript𝜇𝐾𝐿\displaystyle a^{T}\Sigma\_{KL}a-\lambda a^{T}\mu\_{KL} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | aT​(I−2​θ​Σ​A)−1​Σ​a−λ​aT​(μ−λ​θ​(I−2​θ​Σ​A)−1​Σ​a)superscript𝑎𝑇superscript𝐼2𝜃Σ𝐴1Σ𝑎𝜆superscript𝑎𝑇𝜇𝜆𝜃superscript𝐼2𝜃Σ𝐴1Σ𝑎\displaystyle a^{T}(I-2\theta\Sigma A)^{-1}\Sigma a-\lambda a^{T}(\mu-\lambda\theta(I-2\theta\Sigma A)^{-1}\Sigma a) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | aT​Σ​a−λ​aT​μ+θ​aT​Σ​a​(λ2+2​aT​Σ​a)+O​(θ2)superscript𝑎𝑇Σ𝑎𝜆superscript𝑎𝑇𝜇𝜃superscript𝑎𝑇Σ𝑎superscript𝜆22superscript𝑎𝑇Σ𝑎𝑂superscript𝜃2\displaystyle a^{T}\Sigma a-\lambda a^{T}\mu+\theta a^{T}\Sigma a\left(\lambda^{2}+2a^{T}\Sigma a\right)+O(\theta^{2}) |  | (124) |

Note that in the last equality we apply the Taylor expansion (I−2​θ​Σ​A)−1=I+2​θ​Σ​A+4​θ2​Σ​A​Σ​A+⋯=I+2​θ​Σ​A+O​(θ2)superscript𝐼2𝜃Σ𝐴1𝐼2𝜃Σ𝐴4superscript𝜃2Σ𝐴Σ𝐴⋯𝐼2𝜃Σ𝐴𝑂superscript𝜃2(I-2\theta\Sigma A)^{-1}=I+2\theta\Sigma A+4\theta^{2}\Sigma A\Sigma A+\cdots=I+2\theta\Sigma A+O(\theta^{2}).
To find out a closed-form solution, we need to ignore the higher order terms O​(θ2)𝑂superscript𝜃2O(\theta^{2}). Then the stationary condition of the minimisation problem is given by a non-linear equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​Σ​a−λ​μ+2​θ​(λ2+4​aT​Σ​a)​Σ​a=02Σ𝑎𝜆𝜇2𝜃superscript𝜆24superscript𝑎𝑇Σ𝑎Σ𝑎0\displaystyle 2\Sigma a-\lambda\mu+2\theta\left(\lambda^{2}+4a^{T}\Sigma a\right)\Sigma a=0 |  | (125) |

Notice that

|  |  |  |  |
| --- | --- | --- | --- |
|  | a∗:=λ2​Σ−1​μassignsuperscript𝑎𝜆2superscriptΣ1𝜇\displaystyle a^{\*}:=\frac{\lambda}{2}\Sigma^{-1}\mu |  | (126) |

is the MVO portfolio weight under the reference measure. For the robust MVO portfolio, we may consider its first-order deviation from a∗superscript𝑎a^{\*}. To do that, we substitute a=a∗+θ​b𝑎superscript𝑎𝜃𝑏a=a^{\*}+\theta b into Eq. [125](#S6.E125 "In 6.7 G. Robust MVO Portfolio (Kullback-Leibler divergence) ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") allowing us to cancel the term λ​μ𝜆𝜇\lambda\mu.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​θ​Σ​b+θ​λ​(λ2+λ2​μT​Σ−1​μ)​μ+O​(θ2)=02𝜃Σ𝑏𝜃𝜆superscript𝜆2superscript𝜆2superscript𝜇𝑇superscriptΣ1𝜇𝜇𝑂superscript𝜃20\displaystyle 2\theta\Sigma b+\theta\lambda\left(\lambda^{2}+\lambda^{2}\mu^{T}\Sigma^{-1}\mu\right)\mu+O(\theta^{2})=0 |  | (127) |

By matching the first-order term w.r.t θ𝜃\theta, we find the expression for b𝑏b:

|  |  |  |  |
| --- | --- | --- | --- |
|  | b=−λ32​(1+μT​Σ−1​μ)​Σ−1​μ𝑏superscript𝜆321superscript𝜇𝑇superscriptΣ1𝜇superscriptΣ1𝜇\displaystyle b=-\frac{\lambda^{3}}{2}\left(1+\mu^{T}\Sigma^{-1}\mu\right)\Sigma^{-1}\mu |  | (128) |

Therefore the optimal MVO portfolio under the worst-case scenario is

|  |  |  |  |
| --- | --- | --- | --- |
|  | aK​L∗=subscriptsuperscript𝑎𝐾𝐿absent\displaystyle a^{\*}\_{KL}= | (λ2−θ​λ32​(1+μT​Σ−1​μ))​Σ−1​μ𝜆2𝜃superscript𝜆321superscript𝜇𝑇superscriptΣ1𝜇superscriptΣ1𝜇\displaystyle\left(\frac{\lambda}{2}-\frac{\theta\lambda^{3}}{2}\left(1+\mu^{T}\Sigma^{-1}\mu\right)\right)\Sigma^{-1}\mu |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | c​a∗𝑐superscript𝑎\displaystyle ca^{\*} |  | (129) |

where the coefficient c𝑐c is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | c:=1−θ​λ2​(1+μT​Σ−1​μ)assign𝑐1𝜃superscript𝜆21superscript𝜇𝑇superscriptΣ1𝜇\displaystyle c:=1-\theta\lambda^{2}\left(1+\mu^{T}\Sigma^{-1}\mu\right) |  | (130) |

The robust MVO portfolio, as a vector aK​L∗subscriptsuperscript𝑎𝐾𝐿a^{\*}\_{KL}, is parallel to the normal MVO portfolio a∗superscript𝑎a^{\*}. As a result, the robust MVO portfolio does not change the relative weights of component assets. In fact, all the weights are reduced by the same proportion (c<1𝑐1c<1) to account for model risk. This is, however, inappropriately account for the correlation risk. For example, two highly-correlated assets have extremely high weights in the nominal MVO portfolio. Because of the correlation risk, we would expect the robust MVO portfolio to assign them lower weights relative to other assets.

The Sharpe ratio of the robust MVO portfolio obviously equals the Sharpe ratio under the reference measure, denoted by S𝑆S (S=μT​Σ−1​μ𝑆superscript𝜇𝑇superscriptΣ1𝜇S=\sqrt{\mu^{T}\Sigma^{-1}\mu}). Sometimes we may be interested in the Sharpe ratio under the worst-case measure.
This requires us to examine the mean and variance of the robust MVO portfolio given by Eq. [6.7](#S6.Ex61 "6.7 G. Robust MVO Portfolio (Kullback-Leibler divergence) ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance"). Assuming that we are under the worst-case scenario given by Eq. [122](#S6.E122 "In 6.7 G. Robust MVO Portfolio (Kullback-Leibler divergence) ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance"), the portfolio mean and variance can be obtained by substituting aK​L∗=c​λ​Σ−1​μ/2subscriptsuperscript𝑎𝐾𝐿𝑐𝜆superscriptΣ1𝜇2a^{\*}\_{KL}=c\lambda\Sigma^{-1}\mu/2:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μK​LT​aK​L∗=superscriptsubscript𝜇𝐾𝐿𝑇subscriptsuperscript𝑎𝐾𝐿absent\displaystyle\mu\_{KL}^{T}a^{\*}\_{KL}= | (μ−λ​θ​(I−2​θ​Σ​aK​L∗​aK​L∗T)−1​Σ​aK​L∗)T​aK​L∗superscript𝜇𝜆𝜃superscript𝐼2𝜃Σsubscriptsuperscript𝑎𝐾𝐿subscriptsuperscript𝑎absent𝑇𝐾𝐿1Σsubscriptsuperscript𝑎𝐾𝐿𝑇subscriptsuperscript𝑎𝐾𝐿\displaystyle\left(\mu-\lambda\theta\left(I-2\theta\Sigma a^{\*}\_{KL}a^{\*T}\_{KL}\right)^{-1}\Sigma a^{\*}\_{KL}\right)^{T}a^{\*}\_{KL} |  | (131) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | λ​c2​μT​Σ−1​μ−θ​λ3​c24​μT​Σ−1​μ+O​(θ2)𝜆𝑐2superscript𝜇𝑇superscriptΣ1𝜇𝜃superscript𝜆3superscript𝑐24superscript𝜇𝑇superscriptΣ1𝜇𝑂superscript𝜃2\displaystyle\frac{\lambda c}{2}\mu^{T}\Sigma^{-1}\mu-\theta\frac{\lambda^{3}c^{2}}{4}\mu^{T}\Sigma^{-1}\mu+O(\theta^{2}) |  | (132) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | aK​L∗T​ΣK​L​aK​L∗=subscriptsuperscript𝑎absent𝑇𝐾𝐿subscriptΣ𝐾𝐿subscriptsuperscript𝑎𝐾𝐿absent\displaystyle a^{\*T}\_{KL}\Sigma\_{KL}a^{\*}\_{KL}= | aK​L∗T​(I−2​θ​Σ​aK​L∗​aK​L∗T)−1​Σ​aK​L∗subscriptsuperscript𝑎absent𝑇𝐾𝐿superscript𝐼2𝜃Σsubscriptsuperscript𝑎𝐾𝐿subscriptsuperscript𝑎absent𝑇𝐾𝐿1Σsubscriptsuperscript𝑎𝐾𝐿\displaystyle a^{\*T}\_{KL}\left(I-2\theta\Sigma a^{\*}\_{KL}a^{\*T}\_{KL}\right)^{-1}\Sigma a^{\*}\_{KL} |  | (133) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | λ2​c24​μT​Σ−1​μ+θ​λ4​c48​(μT​Σ−1​μ)2+O​(θ2)superscript𝜆2superscript𝑐24superscript𝜇𝑇superscriptΣ1𝜇𝜃superscript𝜆4superscript𝑐48superscriptsuperscript𝜇𝑇superscriptΣ1𝜇2𝑂superscript𝜃2\displaystyle\frac{\lambda^{2}c^{2}}{4}\mu^{T}\Sigma^{-1}\mu+\theta\frac{\lambda^{4}c^{4}}{8}(\mu^{T}\Sigma^{-1}\mu)^{2}+O(\theta^{2}) |  | (134) |

By using the portfolio mean and variance given in Eq. [131](#S6.E131 "In 6.7 G. Robust MVO Portfolio (Kullback-Leibler divergence) ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance"), we may calculate the Sharpe ratio of the robust MVO portfolio (under the worst-case scenario):

|  |  |  |  |
| --- | --- | --- | --- |
|  | SK​L=subscript𝑆𝐾𝐿absent\displaystyle S\_{KL}= | μK​LT​aK​L∗aK​L∗T​ΣK​L​aK​L∗superscriptsubscript𝜇𝐾𝐿𝑇subscriptsuperscript𝑎𝐾𝐿subscriptsuperscript𝑎absent𝑇𝐾𝐿subscriptΣ𝐾𝐿subscriptsuperscript𝑎𝐾𝐿\displaystyle\frac{\mu\_{KL}^{T}a^{\*}\_{KL}}{\sqrt{a^{\*T}\_{KL}\Sigma\_{KL}a^{\*}\_{KL}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 2−θ​λ2​c+O​(θ2)2+θ2​λ2​c2​μT​Σ−1​μ+O​(θ2)​μT​Σ−1​μ2𝜃superscript𝜆2𝑐𝑂superscript𝜃22𝜃2superscript𝜆2superscript𝑐2superscript𝜇𝑇superscriptΣ1𝜇𝑂superscript𝜃2superscript𝜇𝑇superscriptΣ1𝜇\displaystyle\frac{2-\theta\lambda^{2}c+O(\theta^{2})}{2+\frac{\theta}{2}\lambda^{2}c^{2}\mu^{T}\Sigma^{-1}\mu+O(\theta^{2})}\sqrt{\mu^{T}\Sigma^{-1}\mu} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | (1−θ4​λ2​c​(c​S2+2)+O​(θ2))​S1𝜃4superscript𝜆2𝑐𝑐superscript𝑆22𝑂superscript𝜃2𝑆\displaystyle\left(1-\frac{\theta}{4}\lambda^{2}c\left(cS^{2}+2\right)+O(\theta^{2})\right)S |  | (135) |

We can see that the robust Sharpe ratio (defined as the Sharpe ratio of the robust MVO portfolio under the worst-case model) is a function of the nominal Sharpe ratio S𝑆S. The MVO portfolio corresponds to c=1𝑐1c=1, suffering from more reduction in Sharpe ratio than the robust MVO portfolio (c<1𝑐1c<1) under the worst-case measure. This simple relation, however, no longer holds for the Wasserstein approach.

### 6.8 H. Robust MVO Portfolio (Wasserstein approach)

In this section, we will switch to the Wasserstein approach to model risk measurement. We will derive the robust MVO portfolio with the Wasserstein approach. Using Eq. [123](#S6.E123 "In 6.7 G. Robust MVO Portfolio (Kullback-Leibler divergence) ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance"), we may formulate the robust portfolio optimisation problem in the following form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minasubscript𝑎\displaystyle\min\_{a}\, | aT​ΣW​a−λ​aT​μWsuperscript𝑎𝑇subscriptΣ𝑊𝑎𝜆superscript𝑎𝑇subscript𝜇𝑊\displaystyle a^{T}\Sigma\_{W}a-\lambda a^{T}\mu\_{W} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | aT​(I−β​B−1​A)−1​Σ​(I−β​A​B−1)−1​a−λ​aT​(μ−λ2​β​(I−β​B−1​A)−1​B−1​a)superscript𝑎𝑇superscript𝐼𝛽superscript𝐵1𝐴1Σsuperscript𝐼𝛽𝐴superscript𝐵11𝑎𝜆superscript𝑎𝑇𝜇𝜆2𝛽superscript𝐼𝛽superscript𝐵1𝐴1superscript𝐵1𝑎\displaystyle a^{T}(I-\beta B^{-1}A)^{-1}\Sigma(I-\beta AB^{-1})^{-1}a-\lambda a^{T}\left(\mu-\frac{\lambda}{2}\beta(I-\beta B^{-1}A)^{-1}B^{-1}a\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | aT​Σ​a−λ​aT​μ+β​(2​aT​B−1​a​aT​Σ​a+λ22​aT​B−1​a)+O​(β2)superscript𝑎𝑇Σ𝑎𝜆superscript𝑎𝑇𝜇𝛽2superscript𝑎𝑇superscript𝐵1𝑎superscript𝑎𝑇Σ𝑎superscript𝜆22superscript𝑎𝑇superscript𝐵1𝑎𝑂superscript𝛽2\displaystyle a^{T}\Sigma a-\lambda a^{T}\mu+\beta\left(2a^{T}B^{-1}aa^{T}\Sigma a+\frac{\lambda^{2}}{2}a^{T}B^{-1}a\right)+O(\beta^{2}) |  | (136) |

Ignoring the higher order terms, the minimisation problem is solved using

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​Σ​a−λ​μ+β​(4​aT​B−1​a​Σ​a+(4​aT​Σ​a+λ2)​B−1​a)=02Σ𝑎𝜆𝜇𝛽4superscript𝑎𝑇superscript𝐵1𝑎Σ𝑎4superscript𝑎𝑇Σ𝑎superscript𝜆2superscript𝐵1𝑎0\displaystyle 2\Sigma a-\lambda\mu+\beta\left(4a^{T}B^{-1}a\Sigma a+(4a^{T}\Sigma a+\lambda^{2})B^{-1}a\right)=0 |  | (137) |

Substituting a=a∗+β​b𝑎superscript𝑎𝛽𝑏a=a^{\*}+\beta b into Eq. [137](#S6.E137 "In 6.8 H. Robust MVO Portfolio (Wasserstein approach) ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance"), we find the expression for the perturbation b𝑏b by matching the first-order terms of β𝛽\beta:

|  |  |  |  |
| --- | --- | --- | --- |
|  | b=−λ34​(μT​Σ−1​B−1​Σ−1​μ+(1+μT​Σ−1​μ)​Σ−1​B−1)​Σ−1​μ𝑏superscript𝜆34superscript𝜇𝑇superscriptΣ1superscript𝐵1superscriptΣ1𝜇1superscript𝜇𝑇superscriptΣ1𝜇superscriptΣ1superscript𝐵1superscriptΣ1𝜇\displaystyle b=-\frac{\lambda^{3}}{4}\left(\mu^{T}\Sigma^{-1}B^{-1}\Sigma^{-1}\mu+\left(1+\mu^{T}\Sigma^{-1}\mu\right)\Sigma^{-1}B^{-1}\right)\Sigma^{-1}\mu |  | (138) |

Therefore, the Wasserstein approach results in a robust MVO portfolio with weights

|  |  |  |  |
| --- | --- | --- | --- |
|  | aW∗=subscriptsuperscript𝑎𝑊absent\displaystyle a^{\*}\_{W}= | (λ2−β​λ34​μT​Σ−1​B−1​Σ−1​μ−β​λ34​(1+μT​Σ−1​μ)​Σ−1​B−1)​Σ−1​μ𝜆2𝛽superscript𝜆34superscript𝜇𝑇superscriptΣ1superscript𝐵1superscriptΣ1𝜇𝛽superscript𝜆341superscript𝜇𝑇superscriptΣ1𝜇superscriptΣ1superscript𝐵1superscriptΣ1𝜇\displaystyle\left(\frac{\lambda}{2}-\frac{\beta\lambda^{3}}{4}\mu^{T}\Sigma^{-1}B^{-1}\Sigma^{-1}\mu-\frac{\beta\lambda^{3}}{4}\left(1+\mu^{T}\Sigma^{-1}\mu\right)\Sigma^{-1}B^{-1}\right)\Sigma^{-1}\mu |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | c​a∗−D​a∗𝑐superscript𝑎𝐷superscript𝑎\displaystyle ca^{\*}-Da^{\*} |  | (139) |

where c𝑐c is a coefficient while C𝐶C is a square matrix defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | c:=assign𝑐absent\displaystyle c:= | 1−β​λ22​μT​Σ−1​B−1​Σ−1​μ1𝛽superscript𝜆22superscript𝜇𝑇superscriptΣ1superscript𝐵1superscriptΣ1𝜇\displaystyle 1-\frac{\beta\lambda^{2}}{2}\mu^{T}\Sigma^{-1}B^{-1}\Sigma^{-1}\mu |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | D:=assign𝐷absent\displaystyle D:= | β​λ22​(1+μT​Σ−1​μ)​Σ−1​B−1:=d​Σ−1​B−1assign𝛽superscript𝜆221superscript𝜇𝑇superscriptΣ1𝜇superscriptΣ1superscript𝐵1𝑑superscriptΣ1superscript𝐵1\displaystyle\frac{\beta\lambda^{2}}{2}\left(1+\mu^{T}\Sigma^{-1}\mu\right)\Sigma^{-1}B^{-1}:=d\Sigma^{-1}B^{-1} |  | (140) |

c𝑐c serves just as the coefficient under the Kullback-Leibler divergence, reducing the portfolio weights by the same fraction. D𝐷D is a matrix that serves to linearly transform the normal MVO portfolio weights.

Eq. [6.8](#S6.Ex66 "6.8 H. Robust MVO Portfolio (Wasserstein approach) ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") correctly accounts for the correlation risk. When two assets are highly correlated, ΣΣ\Sigma is close to be singular. This results in extremely large weights under the normal MVO portfolio. Eq. [6.8](#S6.Ex66 "6.8 H. Robust MVO Portfolio (Wasserstein approach) ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance"), on the other hand, not only scales the weights down simultaneously by the coefficient c𝑐c, but also reduces the relative weights of the highly-correlated assets by the linear map D𝐷D. To see how the linear map D𝐷D changes the relative weights, we may re-arrange
Eq. [6.8](#S6.Ex66 "6.8 H. Robust MVO Portfolio (Wasserstein approach) ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance") to the following form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | aW∗=λ2​(Σ​(c​I−D)−1)−1​μsuperscriptsubscript𝑎𝑊𝜆2superscriptΣsuperscript𝑐𝐼𝐷11𝜇\displaystyle a\_{W}^{\*}=\frac{\lambda}{2}\left(\Sigma(cI-D)^{-1}\right)^{-1}\mu |  | (141) |

Therefore, the robust MVO portfolio has the same weights as a normal MVO portfolio with an effective covariance matrix

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ∗=Σ​(c​I−d​Σ−1​B−1)−1superscriptΣΣsuperscript𝑐𝐼𝑑superscriptΣ1superscript𝐵11\displaystyle\Sigma^{\*}=\Sigma(cI-d\Sigma^{-1}B^{-1})^{-1} |  | (142) |

One can show by induction that Σ​v=x​vΣ𝑣𝑥𝑣\Sigma v=xv (x𝑥x and v𝑣v are respectively the eigenvalue and the eigenvector) leads to Σn​v=x​vsuperscriptΣ𝑛𝑣𝑥𝑣\Sigma^{n}v=xv for every integer n𝑛n. This is to say, x𝑥x is an eigenvalue of ΣΣ\Sigma only if xnsuperscript𝑥𝑛x^{n} is an eigenvalue of ΣnsuperscriptΣ𝑛\Sigma^{n} corresponding to the same eigenvector. As a result, for every eigenvalue x>0𝑥0x>0 of the positive-definite covariance matrix, there exists a corresponding eigenvalue of the effective covariance matrix (here we only consider the special case where B𝐵B is the identity matrix I𝐼I):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ∗​v=superscriptΣ𝑣absent\displaystyle\Sigma^{\*}v= | Σ​(c​I−d​Σ−1)−1​vΣsuperscript𝑐𝐼𝑑superscriptΣ11𝑣\displaystyle\Sigma(cI-d\Sigma^{-1})^{-1}v |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 1c​∑i=0∞(dc)i​Σ1−i​v1𝑐superscriptsubscript𝑖0superscript𝑑𝑐𝑖superscriptΣ1𝑖𝑣\displaystyle\frac{1}{c}\sum\_{i=0}^{\infty}\left(\frac{d}{c}\right)^{i}\Sigma^{1-i}v |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 1c​∑i=0∞(dc)i​x1−i​v1𝑐superscriptsubscript𝑖0superscript𝑑𝑐𝑖superscript𝑥1𝑖𝑣\displaystyle\frac{1}{c}\sum\_{i=0}^{\infty}\left(\frac{d}{c}\right)^{i}x^{1-i}v |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | xc−d/x​v𝑥𝑐𝑑𝑥𝑣\displaystyle\frac{x}{c-{d}/{x}}v |  | (143) |

The corresponding eigenvalue

|  |  |  |  |
| --- | --- | --- | --- |
|  | x∗:=assignsuperscript𝑥absent\displaystyle x^{\*}:= | xc−d/x𝑥𝑐𝑑𝑥\displaystyle\frac{x}{c-{d}/{x}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | x+β​λ22​(1+μT​Σ−1​μ+μT​Σ−1​B−1​Σ−1​μ)+O​(β2)𝑥𝛽superscript𝜆221superscript𝜇𝑇superscriptΣ1𝜇superscript𝜇𝑇superscriptΣ1superscript𝐵1superscriptΣ1𝜇𝑂superscript𝛽2\displaystyle x+\frac{\beta\lambda^{2}}{2}\left(1+\mu^{T}\Sigma^{-1}\mu+\mu^{T}\Sigma^{-1}B^{-1}\Sigma^{-1}\mu\right)+O(\beta^{2}) |  | (144) |

Any eigenvalue x𝑥x close to zero is adjusted according to Eq. [6.8](#S6.Ex71 "6.8 H. Robust MVO Portfolio (Wasserstein approach) ‣ 6 Appendix ‣ Model Risk Measurement under Wasserstein Distance"), resulting in a corresponding eigenvalue x∗superscript𝑥x^{\*} that is at least as large as β​λ2/2𝛽superscript𝜆22\beta\lambda^{2}/2. This results in an effective matrix Σ∗superscriptΣ\Sigma^{\*} that is less ”singular” than ΣΣ\Sigma, and therefore a robust MVO portfolio that accounts for the correlation risk.

![Refer to caption](/html/1809.03641/assets/eigenvalue.png)


Fig 10: Eigenvalue x∗superscript𝑥x^{\*} of the effective covariance matrix Σ∗superscriptΣ\Sigma^{\*} increases by a greater amount when the original eigenvalue x𝑥x gets closer to zero.

## References

* [1]

  Syed Mumtaz Ali and Samuel D Silvey.
  A general class of coefficients of divergence of one distribution
  from another.
  Journal of the Royal Statistical Society. Series B
  (Methodological), pages 131–142, 1966.
* [2]

  I Csisz et al.
  Information-type measures of difference of probability distributions
  and indirect observations.
  Studia Sci. Math. Hungar., 2:299–318, 1967.
* [3]

  Amir Ahmadi-Javid.
  Entropic value-at-risk: A new coherent risk measure.
  Journal of Optimization Theory and Applications,
  155(3):1105–1123, 2012.
* [4]

  C Villani.
  Optimal transport – Old and new, volume 338, page 18.
  01 2008.
* [5]

  C Villani.
  Optimal transport – Old and new, volume 338, page 22.
  01 2008.
* [6]

  Thomas M Cover and Joy A Thomas.
  Elements of information theory.
  John Wiley & Sons, 2012.
* [7]

  Paul Glasserman and Xingbo Xu.
  Robust risk measurement and model risk.
  Quantitative Finance, 14(1):29–58, 2014.
* [8]

  Gurdip Bakshi and Nikunj Kapadia.
  Delta-hedged gains and the negative market volatility risk premium.
  The Review of Financial Studies, 16(2):527–566, 2003.
* [9]

  Buen Sin Low and Shaojun Zhang.
  The volatility risk premium embedded in currency options.
  Journal of Financial and Quantitative Analysis, 40(4):803–832,
  2005.
* [10]

  Peter Carr and Liuren Wu.
  Analyzing volatility risk and risk premium in option contracts: A new
  theory.
  Journal of Financial Economics, 120(1):1–20, 2016.
* [11]

  Tim Bollerslev, George Tauchen, and Hao Zhou.
  Expected stock returns and variance risk premia.
  The Review of Financial Studies, 22(11):4463–4492, 2009.
* [12]

  Yacine Ait-Sahalia, Mustafa Karaman, and Loriano Mancini.
  The term structure of variance swaps and risk premia.
  2015.

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/1809.03641)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1809.03641)
[View original  
on arXiv](https://arxiv.org/abs/1809.03641)[►](javascript: void(0))