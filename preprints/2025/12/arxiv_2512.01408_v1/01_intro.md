---
authors:
- Jose Blanchet
- Jiayi Cheng
- Hao Liu
- Yang Liu
doc_id: arxiv:2512.01408v1
family_id: arxiv:2512.01408
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein
  Projections
url_abs: http://arxiv.org/abs/2512.01408v1
url_html: https://arxiv.org/html/2512.01408v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jose Blanchet
Stanford University, CA 94305, US. Email: jose.blanchet@stanford.edu
  
Jiayi Cheng
New York University, NY 10003, US. Email: jiayicheng@nyu.edu
  
Hao Liu
Stanford University, CA 94305, US. Email: haoliu20@stanford.edu
  
Yang Liu
The Chinese University of Hong Kong, Shenzhen, Guangdong 518172, China. Email: yangliu16@cuhk.edu.cn

###### Abstract

We revisit Merton’s continuous-time portfolio selection through a data-driven, distributionally robust lens. Our aim is to tap the benefits of frequent trading over short horizons while acknowledging that drift is hard to pin down, whereas volatility can be screened using realized or implied measures for appropriately selected assets. Rather than time-rectangular distributional robust control—which replenishes adversarial power at every instant and induces over-pessimism—we place a single ambiguity set on the drift prior within a Bayesian Merton model. This prior-level ambiguity preserves learning and tractability: a minimax swap reduces the robust control to optimizing a nonlinear functional of the prior, enabling Karatzas and Zhao [KZ98]-type’s closed-form evaluation for each candidate prior. We then characterize small-radius worst-case priors under Wasserstein uncertainty via an explicit asymptotically optimal pushforward of the nominal prior, and we calibrate the ambiguity radius through a nonlinear Wasserstein projection tailored to the Merton functional. Synthetic and real-data studies demonstrate reduced pessimism relative to DRC and improved performance over myopic DRO–Markowitz under frequent rebalancing.

MSC 2020 subject classifications:
Primary 49K45; Secondary 49Q22, 91G10, 90C31.

Keywords: Portfolio selection, distributionally robust stochastic control, reduction of over-pessimism, constrained distributional optimization, nonlinear Wasserstein projection

## 1 Introduction

This paper revisits Merton’s classical continuous-time portfolio selection model through a data-driven, distributionally robust lens. Our goal is to tap the benefits of frequent trading over short horizons (days to weeks) while acknowledging that drift is difficult to pin down over such horizons. In contrast, volatility can often be stabilized by screening via realized or implied measures appropriately chosen assets111We acknowledge that this screening can limit the investing universe; we discuss ways to incorporate volatility uncertainty in the conclusion.. We therefore focus on the robustness of the drift and explicitly separate uncertainty modeling: we treat volatility as pre-estimated (e.g., realized/implied volatility) within the Bayesian filtering setup, and we robustify only the drift by placing a single ambiguity set on the drift prior.

Our starting point is the observation that, while data-driven robust portfolio selection performs competitively, it is static and myopic; it does not leverage the value of frequent rebalancing that Merton’s continuous-time model affords. In particular, for example, myopic DRO–Markowitz policies do not capitalize on information revealed over time except through rolling re-estimation. At first sight, it may be surprising that DRO–Markowitz often outperforms dynamic investment strategies in practice (as illustrated in [BlanchetChenZhou2021]). As explained there, sophisticated dynamic decisions rely heavily on model assumptions; when these are violated, errors compound over time, undermining dynamic strategies—especially under unpredictable non-stationarities. By contrast, the Merton framework provides a principled way to exploit frequent trading—provided we handle model uncertainty in a way that does not induce excessive pessimism.

The robust control literature (DRC/DRMDP) places time-rectangular ambiguity on the data-generating process and derives policies via dynamic programming; see, e.g., [HansenSargent2001, hansen2008robustness, RB1, RB2] and subsequent developments in DRMDP/DRRL [NianSi, wang2022policy, Wang2023, Liu2022, Zhou2021, lu2024drrl]. Rectangularity replenishes the adversary’s power at every time step, often yielding over-conservative allocations when applied to portfolio choice with short horizons. Intuitively, in a one-dimensional drift-shift toy example, a rectangular adversary can depress the drift at each instant, compounding pessimism over time; by contrast, a prior-level ambiguity perturbs the drift distribution once. Nevertheless, rectangularity is widely used because it preserves time consistency and the dynamic-programming structure (Bellman equations), which confers strong tractability and algorithmic scalability—the very benefit delivered by the “replenishing” mechanism. Our design choice is different: instead of time-rectangular uncertainty, we adopt a  *prior-level* ambiguity in a Bayesian Merton model. We place a single ambiguity set around the drift prior - primarily a Wasserstein ball, though KL balls are also covered. The volatility is assumed to be constant and therefore easy to estimate in continuous-time. This *distributionally robust Bayesian control* (DRBC) design reduces pessimism and preserves the learning structure of the Bayesian Merton formulation.

Technically, an important tractability lever is a minimax swap (Sion-type) that holds for broad prior-level ambiguity sets (including Wasserstein and KL). This swap allows us to evaluate, for any fixed prior in the ambiguity set, the optimal Bayesian Merton value and policy in closed form using the formulas of [KZ98]. As a result, the DRBC game reduces to a constrained distributional optimization over the drift prior: we optimize a nonlinear functional of the prior that arises from Karatzas and Zhao [KZ98]’s expression. The reduction holds under mild conditions standard in the Bayesian Merton literature. 222Even if the minimax swap is difficult to justify, one may start with the formulation in which the adversary moves first. While this is not the most natural formulation (because the adversary typically models an environment that occurs after the manager makes its decision), still, it may still be a pragmatic way to induce robustness while mitigate overconservative policies.

Optimizing over a Wasserstein ball is subtle here because the resulting objective is highly nonlinear in the prior; standard Wasserstein DRO tools do not apply off-the-shelf. We derive small-radius asymptotics for non-linear functionals and apply these results to the worst-case prior. We obtain a *constructive* approximation: an explicit asymptotically optimal pushforward perturbation of the nominal prior that realizes the first-order effect. Beyond optimization, we also address calibration: we select the ambiguity radius by general *nonlinear Wasserstein projections*. Then, we tailor these general results to the Merton functional, extending linear RWPI-style projection ideas to this nonlinear setting. We highlight that this nonlinear projection perspective may be of independent interest, given the broad and growing use of Wasserstein projections [SiMurthyBlanchetNguyen2021, Blanchet2021WassersteinDRO].

We complement the theory with evidence in synthetic and real-data settings. In synthetic experiments, we simulate an environment consistent with Merton’s assumptions: volatilities are known (or well-estimated), while asset drifts are unknown but deterministic and time-varying, generated from sinusoidal bases spanning a wide range of oscillatory frequencies. We compare two empirical strategies to construct the nominal drift prior from data: (i) batched, disjoint time windows (e.g., days or weeks) that form an empirical prior from window-level average returns; and (ii) day-of-week aggregation within larger windows (e.g., averages of “Mondays,” “Tuesdays,” etc.). Perhaps surprisingly, the batched-window prior performs slightly better even under periodic drifts, and we adopt it in our real-data study. Across both synthetic and real data, DRBC exhibits reduced pessimism compared to DRC under matched radii and improves performance over myopic DRO–Markowitz when frequent rebalancing is possible.

##### Contributions.

Our main contributions are as follows.

* •

  Duality for prior-level ambiguity. We prove a minimax swap for drift-prior ambiguity sets (Wasserstein and KL), reducing DRBC–Merton to optimizing a nonlinear functional of the prior while preserving closed-form evaluation via [KZ98].
* •

  Constructive worst-case prior sensitivity under Wasserstein and non-linear functionals. For small ambiguity radii, we derive a first-order expansion of the robust objective and give an explicit asymptotically optimal push-forward perturbation of the nominal prior. These results are of independent interest since they are derived for the evaluation of worst-case non-linear functions of probabilities.
* •

  Calibration via nonlinear Wasserstein projection. We introduce a projection-based, data-driven method to select the ambiguity radius tailored to the Merton functional, generalizing linear RWPI-style projections to a nonlinear manifold. Again, the results involve general nonlinear projections in Wasserstein geometry which are of independent interest.
* •

  Empirical validation and reduced pessimism. Synthetic and real-data experiments demonstrate reduced over-conservatism relative to DRC and improved performance over myopic DRO–Markowitz under frequent rebalancing.

In the end, we emphasize that our contributions can still be interpreted within a Bayesian lens. What we offer is a systematic approach to infuse robustness and tractability in the choice of the prior, situating our framework within the scope of contemporary tools of distributionally robust decision making. From this perspective, the statistician may note that the prior’s choice may induce a bias that is relatively small as time increases. But this is not the environment we have in mind. In our setting, the investment horizon (which we denote as TT) is fixed. This time horizon is long enough so that the manager may take advantage of multi-stage, even frequent, decisions but short enough that the volatility and drift are roughly constant. With this in mind, volatility can be set fixed and drift is unknown, so a Bayesian setting is natural but with a prior that requires robust calibration. This is precisely the mindset that motivates our development.

##### Related work.

Distributionally robust optimization (DRO) has been extensively studied in statistics and machine learning, including Wasserstein DRO [Blanchet2021WassersteinDRO, Blanchet2024DRO] and surveys [rahimian2019distributionally, Bayraksan2015, ksw\_2024\_dro]. In control, DRC or DRMDP (Distributionally Robust Markov Decision Processes) typically adopt a time-rectangular ambiguity that preserves Bellman dynamic programming and tractability, but can be conservative because the adversary constantly replenishes its power [HansenSargent2001, hansen2008robustness, wkr\_2013\_rmdp, RB1, RB2, NianSi, wang2022policy, Wang2023, Liu2022, Zhou2021, lu2024drrl]. We instead place a single ambiguity set on the drift prior in a Bayesian Merton model, enabling closed-form evaluation while tempering pessimism. Our approach relates to Bayesian DRO in static settings [doi:10.1137/21M1465548] and differs from DRBO [pmlr-v108-kirschner20a]: beyond being online and discrete-time, DRBO does not robustify within a stochastic control framework (it is closer to rolling-horizon risk minimization) and provides limited guidance for selecting the ambiguity size.

On the sensitivity-analysis side, our work builds on the Wasserstein-DRO expansions of [BartlDrapeauOblojWiesel2021], who develop first-order asymptotics and optimal perturbations under Wasserstein balls, and to subsequent statistical analyses of Wasserstein estimators such as [BKW19, Blanchet2021WassersteinDRO, BMZ21]. A parallel line of work studies divergence-based robustness, most notably the KL- and ϕ\phi-divergence sensitivity framework of [Lam2016] and the Rényi-divergence bounds of [AtarChowdharyDupuis2015]. In contrast to these approaches—which focus on linear or convex performance measures—we analyze the sensitivity of a highly non-linear Merton value functional in Wasserstein geometry and use its first-order expansion to construct problem-specific worst-case priors in continuous-time Bayesian control models. A broader robustness and sensitivity literature, ranging from ambiguity-averse portfolio selection [PflugWozabal2007] to distributionally robust SAA, stochastic programming, and adversarial training and hedging [AndersonPhilpott2019, Dupacova1990, BonnansShapiro2013, ArmacostFiacco1974, AraujoEtAl2019, GaoKleywegt2016, sauldubois\_touzi\_2024], provides useful context but tackles problems of a different structural form.

On the projection side, most existing results focus on linear or convex functionals and thus differ from the non-linear, Merton-specific projection problem studied here. Linear optimal transport projections have been extensively analyzed in the optimal-transport DRO literature, including recent developments on small-sample behavior [LinBlanchetGlynnNguyen2024], unifying OT-based DRO reformulations [BlanchetKuhnLiTaskesen2023], and stability evaluations via distributional perturbations [BlanchetCuiLiLiu2024]. Related projection methodologies also arise in confidence-region construction [BlanchetMurthySi2022], fairness testing through OT projections [SiMurthyBlanchetNguyen2021, TaskesenBlanchetKuhnNguyen2021], and martingale projections under adapted Wasserstein distances [BlanchetWieselZhangZhang2024]. Unlike these works—which center on linear expectation functionals or convex risk measures—we analyze a fully non-linear projection defined by the Merton value functional and derive a problem-specific first-order expansion that yields constructive worst-case priors tailored to continuous-time Bayesian control.

##### Organization.

Section [2](https://arxiv.org/html/2512.01408v1#S2 "2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") reviews the classical and Bayesian Merton formulations. Section [3](https://arxiv.org/html/2512.01408v1#S3 "3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") introduces the DRBC model, establishes the minimax swap enabling closed-form evaluation, and gives the small-radius Wasserstein approximations for worst-case priors. Section [4](https://arxiv.org/html/2512.01408v1#S4 "4 Data-Driven Formulation and Choice of Model Parameters ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") presents our data-driven construction of the drift prior and develops a nonlinear Wasserstein projection for ambiguity calibration. Sections [5](https://arxiv.org/html/2512.01408v1#S5 "5 Synthetic Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and [6](https://arxiv.org/html/2512.01408v1#S6 "6 Real-data Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") report synthetic and real-data experiments, respectively. Additional experimental details are deferred to the Appendix. Due to space constraints and to ease the exposition, we focus on compactly supported adversarial priors. We provide an online supplementary section dealing with more general priors in the important power-utility setting.

## 2 Preliminaries

In this section we review the classical and Bayesian formulations of Merton’s portfolio selection problem and set the notation used throughout. W=(W1,…,Wd)⊤W=\left(W\_{1},\ldots,W\_{d}\right)^{\top} is an ℝd\mathbb{R}^{d}-valued Brownian motion under a complete filtered probability space (Ω,ℱ,{ℱ​(t)}t∈[0,T],ℙ)(\Omega,\mathcal{F},\{\mathcal{F}(t)\}\_{t\in[0,T]},\mathbb{P}). The risk-free asset is given by S0​(0)=s0>0S\_{0}(0)=s\_{0}>0 and

|  |  |  |
| --- | --- | --- |
|  | d​S0​(t)=r​S0​(t)​d​t,  0≤t≤T,dS\_{0}(t)=rS\_{0}(t)dt,\;\;0\leq t\leq T, |  |

with risk-free rate r>0r>0 and dd risky assets are represented by the vector S=(S1,…,Sd)⊤S=\left(S\_{1},\ldots,S\_{d}\right)^{\top}. The dynamics of the risky assets follow the geometric Brownian motion: for i=1,…,di=1,\ldots,d, Si​(0)>0S\_{i}(0)>0 and

|  |  |  |
| --- | --- | --- |
|  | d​Si​(t)=Si​(t)​[bi​d​t+∑j=1dσi​j​d​Wj​(t)],  0≤t≤T.dS\_{i}(t)=S\_{i}(t)\left[b\_{i}dt+\sum\_{j=1}^{d}\sigma\_{ij}dW\_{j}(t)\right],\;\;0\leq t\leq T. |  |

A portfolio (or control, or policy) is a stochastic process π={π​(t)}t∈[0,T]\pi=\{\pi(t)\}\_{t\in[0,T]} such that for a fixed t∈[0,T]t\in[0,T], π​(t)=(π1​(t),…,πd​(t))⊤\pi(t)=\left(\pi\_{1}(t),\ldots,\pi\_{d}(t)\right)^{\top} and πi​(t)\pi\_{i}(t) represents the amount of money invested in the iith stock at time tt. This induces the dynamics of a controlled wealth process with X​(0)=x0X(0)=x\_{0} (we simplify the notation so that XπX^{\pi} is written as XX)

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​X​(t)=r​X​(t)​d​t+π​(t)⊤​(b−r​𝟏)​d​t+π​(t)⊤​σ​d​W​(t),dX(t)=rX(t)dt+\pi(t)^{\top}\left(b-r\mathbf{1}\right)dt+\pi(t)^{\top}\sigma dW(t), |  | (1) |

where 𝟏=(1,…,1)⊤\mathbf{1}=\left(1,\ldots,1\right)^{\top} is the vector of all 1.
We call an ℱ\mathcal{F}-progressively measurable (under ℙ\mathbb{P} up to ℙ\mathbb{P}-null sets) stochastic processes (control) π={π​(t)}t∈[0,T]\pi=\{\pi(t)\}\_{t\in[0,T]} admissible if X​(0)=x0X(0)=x\_{0}, ∫0T‖π​(t)‖22​𝑑t<∞\int\_{0}^{T}\left\|\pi(t)\right\|\_{2}^{2}dt<\infty ℙ\mathbb{P}-almost surely, and
Equation ([1](https://arxiv.org/html/2512.01408v1#S2.E1 "In 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) admits a unique strong solution with X​(t)>0X(t)>0 for any t∈[0,T]t\in[0,T]. The collection of all admissible controls is denoted by 𝒜​(x0)\mathcal{A}(x\_{0}).

The objective function of Merton’s problem is V​(x0)=supπ∈𝒜​(x0)𝔼ℙ​[U​(X​(T))],V(x\_{0})=\sup\_{\pi\in\mathcal{A}(x\_{0})}\mathbb{E}\_{\mathbb{P}}\left[U(X(T))\right],
where UU is the utility function. We will specify the utility in Assumption [1](https://arxiv.org/html/2512.01408v1#Thmassumption1 "Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") later. Using techniques from dynamic programming, Merton’s problem admits a closed-form formula of the optimal strategy π\pi. In practice, the parameters bb and σ\sigma are estimated from the market data with statistical techniques (e.g., maximum likelihood estimation), and then these estimations are plugged into the closed-form solutions.

However, in practice, estimating bb is difficult at the horizons of interest. To address this, [KZ98] introduces a partially observed Bayesian variant: we keep the same probability space but model the instantaneous return as an unobservable random vector B:Ω→ℝdB:\Omega\to\mathbb{R}^{d}, independent of WW under ℙ\mathbb{P}, with prior distribution μ\mu. The price dynamics become the same SDE with bb replaced by BB:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Si​(t)=Si​(t)​[Bi​d​t+∑j=1dσi​j​d​Wj​(t)],  0≤t≤T,dS\_{i}(t)=S\_{i}(t)\left[B\_{i}dt+\sum\_{j=1}^{d}\sigma\_{ij}dW\_{j}(t)\right],\;\;0\leq t\leq T, |  | (2) |

Equivalently, under ℙ\mathbb{P}, B∼μB\sim\mu (some probability measure) and BB is independent of WW; we refer to μ\mu as the prior. We write 𝒩​(m,Σ)\mathcal{N}(m,\Sigma) for a Gaussian law with mean mm and covariance Σ\Sigma, and φs\varphi\_{s} for the density of 𝒩​(0,s​Id)\mathcal{N}(0,sI\_{d}).

We denote the natural filtration of the process SS by ℱS\mathcal{F}^{S} and denote the ℙ\mathbb{P}-augmentation of ℱS\mathcal{F}^{S} by ℱℙS\mathcal{F}^{S}\_{\mathbb{P}} and this right-continuous and completion is the observation filtration. The decisions are made based on only information from stocks. That is, in this case, the admissible controls are restricted to those that are ℱℙS\mathcal{F}^{S}\_{\mathbb{P}}-progressively measurable and satisfy the same assumptions of integrability and SDE as before.

The full information of the Brownian motion and the random vector is encoded in the ℙ\mathbb{P}-augmentation of the enlarged filtration 𝒢B,W={𝒢B,W​(t)}t≥0\mathcal{G}^{B,W}=\{\mathcal{G}^{B,W}(t)\}\_{t\geq 0} with

|  |  |  |
| --- | --- | --- |
|  | 𝒢B,W​(t)=σ​(B,W​(s),0≤s≤t)=σ​(B)∨ℱW​(t),\mathcal{G}^{B,W}(t)=\sigma\left(B,W(s),0\leq s\leq t\right)=\sigma(B)\vee\mathcal{F}^{W}(t), |  |

where we denote this augmentation as 𝒢\mathcal{G}.
Therefore, for each t≥0,ℱℙS​(t)⊂𝒢​(t)t\geq 0,\mathcal{F}^{S}\_{\mathbb{P}}(t)\subset\mathcal{G}(t), where the inclusion can be strict. The wealth dynamic is

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​X​(t)=r​X​(t)​d​t+π​(t)⊤​(B−r​𝟏)​d​t+π​(t)⊤​σ​d​W​(t).dX(t)=rX(t)dt+\pi(t)^{\top}\left(B-r\mathbf{1}\right)dt+\pi(t)^{\top}\sigma dW(t). |  | (3) |

We call an ℱℙS\mathcal{F}^{S}\_{\mathbb{P}}-progressively measurable (under ℙ\mathbb{P} up to ℙ\mathbb{P}-null sets) stochastic processes (control) π={π​(t)}t∈[0,T]\pi=\{\pi(t)\}\_{t\in[0,T]} admissible if X​(0)=x0X(0)=x\_{0}, ∫0T‖π​(t)‖22​𝑑t<∞\int\_{0}^{T}\left\|\pi(t)\right\|\_{2}^{2}dt<\infty ℙ\mathbb{P}-almost surely, and
Equation ([3](https://arxiv.org/html/2512.01408v1#S2.E3 "In 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) admits a unique strong solution with X​(t)>0X(t)>0 for any t∈[0,T]t\in[0,T]. The collection of all admissible controls is denoted as 𝒜​(x0)\mathcal{A}(x\_{0}).
The Bayesian diffusion control problem is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x0)=supπ∈𝒜​(x0)𝔼ℙ​[U​(X​(T))].V(x\_{0})=\sup\_{\pi\in\mathcal{A}(x\_{0})}\mathbb{E}\_{\mathbb{P}}\left[U(X(T))\right]. |  | (4) |

We will study a general utility family shown in Assumption [1](https://arxiv.org/html/2512.01408v1#Thmassumption1 "Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections").

###### Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]).

(1) The utility function U:(0,∞)→ℝU:(0,\infty)\to\mathbb{R} is twice continuously differentiable,
strictly concave, strictly increasing, and satisfies a polynomial growth condition:
there exist constants CU>0C\_{U}>0 and pU>0p\_{U}>0 such that

|  |  |  |
| --- | --- | --- |
|  | |U(x)|≤CU(1+max{x,x−1}pU),x>0.|U(x)|\;\leq\;C\_{U}\Bigl(1+\max\{x,\,x^{-1}\}^{p\_{U}}\Bigr),\qquad x>0. |  |

(2) Define the conjugate function I​(⋅)=(U′)−1​(⋅)I(\cdot)=(U^{\prime})^{-1}(\cdot), which is strictly convex and decreasing.
We assume that II and its derivative satisfy a two–sided polynomial growth bound, and that
II does not decay too fast at infinity: there exist constants CI>0C\_{I}>0, cI>0c\_{I}>0, and pI>0p\_{I}>0 such that

|  |  |  |
| --- | --- | --- |
|  | |I(y)|+|I′(y)|≤CI(1+max{y,y−1}pI),y>0,|I(y)|+|I^{\prime}(y)|\;\leq\;C\_{I}\Bigl(1+\max\{y,\,y^{-1}\}^{p\_{I}}\Bigr),\qquad y>0, |  |

and

|  |  |  |
| --- | --- | --- |
|  | I​(y)≥cI​y−pI,y>0.I(y)\;\geq\;c\_{I}\,y^{-p\_{I}},\qquad y>0. |  |

###### Remark 1.

The growth conditions for UU and for I=(U′)−1I=(U^{\prime})^{-1} are stated separately because
bounds on UU do not in general imply corresponding bounds on U′U^{\prime} or on II.
Nevertheless, for all standard utility functions used in applications
(such as power/CRRA and logarithmic utility), both parts of
Assumption [1](https://arxiv.org/html/2512.01408v1#Thmassumption1 "Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") are satisfied.

We now introduce the objects needed to state the Bayesian solution. Define
F​(t,y):=Fμ​(t,y):=∫ℝdLt​(b,y)​μ​(d​b)=𝔼μ​[LT​(B,y)]F(t,y):=F\_{\mu}(t,y):=\int\_{\mathbb{R}^{d}}L\_{t}(b,y)\mu(db)=\mathbb{E}\_{\mu}[L\_{T}(B,y)]
with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt​(b,y)=exp⁡(⟨σ−1​(b−r​𝟏),y⟩−12​‖σ−1​(b−r​𝟏)‖2​t),t∈(0,∞),b∈ℝd,y∈ℝd.L\_{t}(b,y)=\exp\left(\langle\sigma^{-1}(b-r\mathbf{1}),y\rangle-\frac{1}{2}\|\sigma^{-1}(b-r\mathbf{1})\|^{2}t\right),\;\;t\in(0,\infty),\;b\in\mathbb{R}^{d},\;y\in\mathbb{R}^{d}. |  | (5) |

For k>0k>0, s∈[0,T]s\in[0,T], and y∈ℝdy\in\mathbb{R}^{d}, set

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(k;s,y):={e−r​s​∫ℝdI​(k​e−r​TF​(T,y+z))​φs​(z)​𝑑z,s>0,I​(k​e−r​TF​(T,y)),s=0.L(k;s,y):=\begin{cases}e^{-rs}\displaystyle\int\_{\mathbb{R}^{d}}I\!\left(\frac{ke^{-rT}}{F(T,y+z)}\right)\varphi\_{s}(z)\,dz,&s>0,\\[11.99998pt] I\!\left(\frac{ke^{-rT}}{F(T,y)}\right),&s=0.\end{cases} |  | (6) |

To simplify tedious technical discussions, we assume that the drift variable BB is compactly supported (Assumption [2](https://arxiv.org/html/2512.01408v1#Thmassumption2 "Assumption 2 (Compact Support for 𝐵). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")). We provide more technical discussions under specific utilities with relaxed concentration assumptions of BB in supplementary materials.

###### Assumption 2 (Compact Support for BB).

The random variable BB is compactly supported in Merton’s model. Specifically, there exists a compact set K⊂ℝdK\subset\mathbb{R}^{d} such that μ​(B∈K)=1\mu(B\in K)=1 for all possible μ\mu.

Under this setting, a standard Gaussian integral computation yields the following lemma.

###### Lemma 1.

Under Assumptions [1](https://arxiv.org/html/2512.01408v1#Thmassumption1 "Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and [2](https://arxiv.org/html/2512.01408v1#Thmassumption2 "Assumption 2 (Compact Support for 𝐵). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), the map LL in ([6](https://arxiv.org/html/2512.01408v1#S2.E6 "In 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) is finite for all (k,s,y)∈(0,∞)×[0,T]×ℝd(k,s,y)\in(0,\infty)\times[0,T]\times\mathbb{R}^{d}, continuously differentiable in (k,s,y)(k,s,y) on (0,∞)×(0,T]×ℝd(0,\infty)\times(0,T]\times\mathbb{R}^{d}, and twice continuously differentiable in (k,y)(k,y) on (0,∞)×[0,T]×ℝd(0,\infty)\times[0,T]\times\mathbb{R}^{d}.

According to [KZ98], under Assumption [1](https://arxiv.org/html/2512.01408v1#Thmassumption1 "Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), the strictly decreasing function

|  |  |  |  |
| --- | --- | --- | --- |
|  | k↦e−r​T​∫ℝdI​(k​e−r​TF​(T,z))​φT​(z)​𝑑z=L​(k;T,0)\displaystyle k\mapsto e^{-rT}\int\_{\mathbb{R}^{d}}I\left(\frac{ke^{-rT}}{F(T,z)}\right)\varphi\_{T}(z)dz=L(k;T,0) |  | (7) |

is continuous and maps (0,∞)(0,\infty) onto itself. Thus, the equation L​(k;T,0)=x0L(k;T,0)=x\_{0} is satisfied for a unique constant 𝒦​(x0)∈(0,∞)\mathcal{K}(x\_{0})\in(0,\infty).

The optimal solution is summarized in the following two results, first for the value function and later for the optimal strategy (i.e., the portfolio weights at every point in time); these results restate the characterization in [KZ98] in our notation and compact form, and will be used repeatedly in our development.

###### Theorem 1 (Karatzas–Zhao [KZ98]’s Solution).

Suppose that Assumptions [1](https://arxiv.org/html/2512.01408v1#Thmassumption1 "Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and [2](https://arxiv.org/html/2512.01408v1#Thmassumption2 "Assumption 2 (Compact Support for 𝐵). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") hold.

(1) The optimal value function of Problem ([4](https://arxiv.org/html/2512.01408v1#S2.E4 "In 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) is given by

|  |  |  |
| --- | --- | --- |
|  | V​(x0)=∫ℝdF​(T,z)​U​(I​(𝒦​(x0)​e−r​TF​(T,z)))​φT​(z)​𝑑z,V(x\_{0})=\int\_{\mathbb{R}^{d}}F(T,z)U\left(I\left(\frac{\mathcal{K}(x\_{0})e^{-rT}}{F(T,z)}\right)\right)\varphi\_{T}(z)dz, |  |

where 𝒦​(x0)>0\mathcal{K}(x\_{0})>0 is the unique solution to the budget constraint:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x0​er​T=∫ℝdI​(𝒦​(x0)​e−r​TF​(T,z))​φT​(z)​𝑑z.x\_{0}e^{rT}=\int\_{\mathbb{R}^{d}}I\left(\frac{\mathcal{K}(x\_{0})e^{-rT}}{F(T,z)}\right)\varphi\_{T}(z)dz. |  | (8) |

In particular, for power utility U​(x)=xα/αU(x)=x^{\alpha}/\alpha, this reduces to the classical Karatzas–Zhao [KZ98]’s formula:

|  |  |  |
| --- | --- | --- |
|  | V​(x0)=(x0​er​T)αα​(∫ℝdF​(T,z)11−α​φT​(z)​𝑑z)1−α.V(x\_{0})=\frac{(x\_{0}e^{rT})^{\alpha}}{\alpha}\left(\int\_{\mathbb{R}^{d}}F(T,z)^{\frac{1}{1-\alpha}}\varphi\_{T}(z)dz\right)^{1-\alpha}. |  |

(2) The optimal fractions invested in each stock at time t∈[0,T]t\in[0,T] are given by the vector

|  |  |  |
| --- | --- | --- |
|  | π∗​(t)X∗​(t)=(σ⊤)−1​(−𝒦​(x0))​e−r​T⋅∫ℝd∇zF​(T,z+Y​(t))F​(T,z+Y​(t))2⋅I′​(𝒦​(x0)​e−r​TF​(T,z+Y​(t)))​φT−t​(z)​𝑑z∫ℝdI​(𝒦​(x0)​e−r​TF​(T,z+Y​(t)))​φT−t​(z)​𝑑z,\frac{\pi^{\*}(t)}{X^{\*}(t)}={\left(\sigma^{\top}\right)}^{-1}(-\mathcal{K}(x\_{0}))e^{-rT}\cdot\frac{\int\_{\mathbb{R}^{d}}\frac{\nabla\_{z}F\left(T,z+Y(t)\right)}{F\left(T,z+Y(t)\right)^{2}}\cdot I^{\prime}\left(\frac{\mathcal{K}(x\_{0})e^{-rT}}{F(T,z+Y(t))}\right)\varphi\_{T-t}(z)dz}{\int\_{\mathbb{R}^{d}}I\left(\frac{\mathcal{K}(x\_{0})e^{-rT}}{F(T,z+Y(t))}\right)\varphi\_{T-t}(z)dz}, |  |

where Y​(t)=σ−1​(B−r​𝟏)​t+W​(t)Y(t)=\sigma^{-1}(B-r\mathbf{1})t+W(t), t∈[0,T]t\in[0,T]. Note that the filtration generated by {Y​(t)}t∈[0,T]\{Y(t)\}\_{t\in[0,T]} is equal to ℱS\mathcal{F}^{S} under ℙ\mathbb{P}.

In particular, for power utility U​(x)=xα/αU(x)=x^{\alpha}/\alpha, this reduces to the classical formula:

|  |  |  |
| --- | --- | --- |
|  | π∗​(t)X∗​(t)=(σ⊤)−1⋅∫ℝd∇zF​(T,z+Y​(t))⋅F​(T,z+Y​(t))α1−α​φT−t​(z)​𝑑z(1−α)​∫ℝdF​(T,z+Y​(t))11−α​φT−t​(z)​𝑑z.\frac{\pi^{\*}(t)}{X^{\*}(t)}={\left(\sigma^{\top}\right)}^{-1}\cdot\frac{\int\_{\mathbb{R}^{d}}\nabla\_{z}F\left(T,z+Y(t)\right)\cdot F\left(T,z+Y(t)\right)^{\frac{\alpha}{1-\alpha}}\varphi\_{T-t}(z)dz}{(1-\alpha)\int\_{\mathbb{R}^{d}}F\left(T,z+Y(t)\right)^{\frac{1}{1-\alpha}}\varphi\_{T-t}(z)dz}. |  |

In practice, the prior distribution is chosen by experts and other available information, and the fraction of investment into risky assets is computed via the formula provided by Theorem [1](https://arxiv.org/html/2512.01408v1#Thmtheorem1 "Theorem 1 (Karatzas–Zhao [KZ98]’s Solution). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") plugging in the observations of stock prices, normalizing the weight to maintain self-financing.

## 3 Formulation and Main Structural Results

In this section, we introduce our formulation of distributionally robust Bayesian control (DRBC) of Merton’s problem, compare it with the classical distributionally robust control (DRC) methods, and show the tractability of the DRBC formulation. We focus on optimal transport based uncertainty sets and, as mentioned in the Introduction, we will revisit ϕ\phi-divergence extensions in a later section. The work of [Blanchet2025Duality] considers duality results for DRBC with ϕ\phi-divergence uncertainty. In this setting, the admissible controls are still defined as ℱℙ0S\mathcal{F}^{S}\_{\mathbb{P}\_{0}}-progressively measurable since all other probability measures ℚ\mathbb{Q} in the uncertainty set are absolutely continuous to ℙ0\mathbb{P}\_{0}, and thus the formulation is still well-defined. However, this is not immediate in the Wasserstein uncertainty case that we study here, so some care is needed to handle this.

We use DcD\_{c} to denote the optimal transport discrepancy generated by cc (equivalent to the Wasserstein distance when cc is a metric), as we now describe. Precisely, let
𝒫​(ℝd×ℝd)\mathcal{P}(\mathbb{R}^{d}\times\mathbb{R}^{d}) be the space of Borel
probability measures supported on ℝd×ℝd\mathbb{R}^{d}\times\mathbb{R}^{d}. A
given element υ∈𝒫​(ℝd×ℝd)\upsilon\in\mathcal{P}(\mathbb{R}^{d}\times\mathbb{R}^{d}) is
associated to a random vector (U,V)\left(U,V\right), where U∈ℝdU\in\mathbb{R}^{d} and V∈ℝdV\in\mathbb{R}^{d}, in the following way: υU​(A)=υ​(A×ℝd)\upsilon\_{U}\left(A\right)=\upsilon\left(A\times\mathbb{R}^{d}\right) and υV​(A)=υ​(ℝd×A)\upsilon\_{V}\left(A\right)=\upsilon\left(\mathbb{R}^{d}\times A\right) for every
Borel set A⊂ℝdA\subset\mathbb{R}^{d}, where υU\upsilon\_{U} and υV\upsilon\_{V}
respectively denote the mariginal distributions of UU and VV under υ\upsilon.

To define DcD\_{c}, we need to introduce a cost function c:ℝd×ℝd→[0,∞]c:\mathbb{R}^{d}\times\mathbb{R}^{d}\rightarrow[0,\infty], which we shall assume to be lower
semicontinuous and such that c​(u,u)=0c\left(u,u\right)=0 for any u∈ℝdu\in\mathbb{R}^{d}. Finally, given two probability distribution ℙ\mathbb{P} and ℚ\mathbb{Q} supported on
ℝd\mathbb{R}^{d} and a cost function cc, define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dc​(ℙ,ℚ):=inf{𝔼υ​[c​(U,V)]:υ∈𝒫​(ℝd×ℝd),υU=ℙ,υV=ℚ},D\_{c}(\mathbb{P},\mathbb{Q}):=\inf\{\mathbb{E}\_{\upsilon}[c(U,V)]:\upsilon\in\mathcal{P}(\mathbb{R}^{d}\times\mathbb{R}^{d}),\upsilon\_{U}=\mathbb{P},\upsilon\_{V}=\mathbb{Q}\}, |  | (9) |

which can be interpreted as the optimal (minimal) transportation cost of
moving the mass from ℙ\mathbb{P} into the mass of ℚ\mathbb{Q} under a cost c​(x,y)c\left(x,y\right) per unit of mass transported from xx to yy. If for a given
ρ≥1\rho\geq 1, c1/ρ​(⋅)c^{1/\rho}\left(\cdot\right) is a metric, then Dc1/ρD\_{c}^{1/\rho} defines a metric on probability measures (the Wasserstein distance of order ρ\rho); see [villani2008optimal].
Throughout the rest of the paper, we will choose cost
function c​(u,v)=‖v−u‖22c(u,v)=||v-u||\_{2}^{2} when BB is compactly supported. The discussion of other choices of the cost functions will be discussed in supplementary materials.

To rigorously define the DRBC formulation, we need to make sure only the distribution of BB is changed and all other problem structures (e.g., the adaptedness of the controls, the distribution of the other sources of randomness, independence structures, and integrability conditions) are kept the same.
To preserve the structure of the original partial observation problem, we keep track only of the joint law of (B,W)(B,W) and maintain their independence. We place the model on the canonical product space Ω=ℝd×C​([0,T];ℝd)\Omega=\mathbb{R}^{d}\times C([0,T];\mathbb{R}^{d}) equipped with the Borel σ\sigma-algebra ℬ​(Ω)\mathcal{B}(\Omega), with canonical coordinates (B,W)(B,W) and write S=S​(B,W)S=S(B,W) for the price process. We let ℙW\mathbb{P}\_{W} be the Wiener measure on the space C​([0,T];ℝd)C\left([0,T];\mathbb{R}^{d}\right) and denote the prior distribution of BB as ℙ0\mathbb{P}\_{0} (satisfying Assumption [2](https://arxiv.org/html/2512.01408v1#Thmassumption2 "Assumption 2 (Compact Support for 𝐵). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")). The observation filtration is fixed once and for all as

|  |  |  |
| --- | --- | --- |
|  | ℱS(t):=σ(S(u):0≤u≤t)∨𝒩,\mathcal{F}^{S}(t):=\sigma\big(S(u):0\leq u\leq t\big)\vee\mathcal{N}, |  |

where 𝒩\mathcal{N} collects the null sets, and it does not depend on the choice of the nominal prior ℙ0\mathbb{P}\_{0} (nor on μ\mu in the ambiguity set). The reason is that the distributions of Y​(t;b)=b​t+σ−1​W​(t)Y(t;b)=bt+\sigma^{-1}W(t) share the same sets of measure zero for each bb in the canonical space. Admissible controls are processes that are progressively measurable with respect to {ℱS​(t)}t∈[0,T]\{\mathcal{F}^{S}(t)\}\_{t\in[0,T]} and satisfy the usual integrability/positivity conditions. This setup ensures that robustness only changes the prior on BB while leaving the information structure unchanged.

Now we define ℙ:=ℙ0⊗ℙW\mathbb{P}:=\mathbb{P}\_{0}\otimes\mathbb{P}\_{W}.
The Wasserstein uncertainty set with a radius δ>0\delta>0 is defined as:

|  |  |  |
| --- | --- | --- |
|  | 𝒰δOT​(ℙ0):={ℚ=μ⊗ℙW:Dc​(μ,ℙ0)≤δ​ and μ satisfies Assumption [2](https://arxiv.org/html/2512.01408v1#Thmassumption2 "Assumption 2 (Compact Support for 𝐵). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")},\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0}):=\left\{\mathbb{Q}=\mu\otimes\mathbb{P}\_{W}:D\_{c}(\mu,\mathbb{P}\_{0})\leq\delta\text{ and $\mu$ satisfies Assumption \ref{ass:compact\_B}}\right\}, |  |

where we assume in the following that the prior measure and all adversarial measures have a compact support.
We now define the admissible controls by the stochastic process π:[0,T]×Ω→ℝd\pi:[0,T]\times\Omega\to\mathbb{R}^{d} such that

* •

  (a) π\pi is ℱS\mathcal{F}^{S}-progressively measurable with càdlàg paths.
* •

  (b) The SDE

  |  |  |  |
  | --- | --- | --- |
  |  | d​X​(t)=r​X​(t)​d​t+π​(t)⊤​(B−r​𝟏)​d​t+π​(t)⊤​σ​d​W​(t)dX(t)=rX(t)dt+\pi(t)^{\top}\left(B-r\mathbf{1}\right)dt+\pi(t)^{\top}\sigma dW(t) |  |

  admits a unique weak solution such that X​(t)>0X(t)>0 for any t∈[0,T]t\in[0,T].
* •

  (c) ∫0T‖π​(t)‖22​𝑑t<∞\int\_{0}^{T}\|\pi(t)\|\_{2}^{2}dt<\infty ℙ\mathbb{P}-a.s.

The collection of all admissible controls is denoted as 𝒜​(x0)\mathcal{A}(x\_{0}) for the case when X​(0)=x0X(0)=x\_{0}. The DRBC problem is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x0)=supπ∈𝒜​(x0)infℚ∈𝒰δOT​(ℙ0)𝔼ℚ​[Uπ​(X​(T))]V(x\_{0})=\sup\_{\pi\in\mathcal{A}(x\_{0})}\inf\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}\mathbb{E}\_{\mathbb{Q}}\left[U^{\pi}(X(T))\right] |  | (10) |

and denote the optimal solution of Problem ([10](https://arxiv.org/html/2512.01408v1#S3.E10 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) as πDRBC\pi\_{\text{DRBC}}.

As discussed in [Blanchet2025Duality], Problem ([10](https://arxiv.org/html/2512.01408v1#S3.E10 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) is typically not directly tractable in its original form. To solve the problem, [Blanchet2025Duality] discusses several techniques, such as discretizing the prior distribution in the context of KL-uncertainty sets or applying simulation techniques that may be time-consuming. However, exploiting the special structure of the Merton problem, under reasonable assumptions, we can derive the following theorem, which will significantly simplify approximating the solution to Problem ([10](https://arxiv.org/html/2512.01408v1#S3.E10 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")).

###### Theorem 2 (Min-Max Equality).

Under Assumptions [1](https://arxiv.org/html/2512.01408v1#Thmassumption1 "Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and [2](https://arxiv.org/html/2512.01408v1#Thmassumption2 "Assumption 2 (Compact Support for 𝐵). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), for any initial wealth x0>0x\_{0}>0, the following min-max equality holds:

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒜​(x0)infℚ∈𝒰δOT​(ℙ0)𝔼ℚ​[U​(Xπ​(T))]=infℚ∈𝒰δOT​(ℙ0)supπ∈𝒜​(x0)𝔼ℚ​[U​(Xπ​(T))].\sup\_{\pi\in\mathcal{A}(x\_{0})}\inf\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi}(T))]=\inf\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}\sup\_{\pi\in\mathcal{A}(x\_{0})}\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi}(T))]. |  |

###### Proof.

We prove the theorem in four steps, leveraging the compact support of BB and the structure of the utility function.

Step 1: Weak duality. The inequality supπinfℚ≤infℚsupπ\sup\_{\pi}\inf\_{\mathbb{Q}}\leq\inf\_{\mathbb{Q}}\sup\_{\pi} holds by definition (weak duality). To upgrade the reverse inequality, we introduce the subset

|  |  |  |
| --- | --- | --- |
|  | 𝒜′​(x0):={π∈𝒜​(x0):d​(π,0)<∞}, where ​d​(π,π′):=supℚ∈𝒰δOT​(ℙ0)(𝔼ℚ​[∫0T‖π​(t)−π′​(t)‖2​𝑑t])1/2,\mathcal{A}^{\prime}(x\_{0}):=\Big\{\pi\in\mathcal{A}(x\_{0}):d(\pi,0)<\infty\Big\},\text{ where }d(\pi,\pi^{\prime}):=\sup\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}\left(\mathbb{E}\_{\mathbb{Q}}\left[\int\_{0}^{T}\|\pi(t)-\pi^{\prime}(t)\|^{2}dt\right]\right)^{1/2}, |  |

which equips the class of L2L^{2}-admissible policies with the topology induced by the L2L^{2}-norm. As 𝒜′​(x0)⊂𝒜​(x0)\mathcal{A}^{\prime}(x\_{0})\subset\mathcal{A}(x\_{0}), we have

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒜​(x0)infℚ∈𝒰δOT​(ℙ0)𝔼ℚ​[U​(Xπ​(T))]≥supπ∈𝒜′​(x0)infℚ∈𝒰δOT​(ℙ0)𝔼ℚ​[U​(Xπ​(T))].\sup\_{\pi\in\mathcal{A}(x\_{0})}\inf\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi}(T))]\;\geq\;\sup\_{\pi\in\mathcal{A}^{\prime}(x\_{0})}\inf\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi}(T))]. |  |

In the next steps, we establish the corresponding reverse inequality for 𝒜′​(x0)\mathcal{A}^{\prime}(x\_{0}). The final step (discussed later) will verify that the optimizer obtained at the end of the analysis belongs to 𝒜′​(x0)\mathcal{A}^{\prime}(x\_{0}), thereby closing the gap.

Step 2: Variation of constants and continuity in the model.
Let K⊂ℝdK\subset\mathbb{R}^{d} be the compact support guaranteed by Assumption [2](https://arxiv.org/html/2512.01408v1#Thmassumption2 "Assumption 2 (Compact Support for 𝐵). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), fix π∈𝒜′​(x0)\pi\in\mathcal{A}^{\prime}(x\_{0}), and note that the linear wealth dynamics yield the variation-of-constants formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xπ​(T;b,W)=x0​er​T+er​T​∫0Te−r​s​π​(s)⊤​(b−r​𝟏)​𝑑s+er​T​∫0Te−r​s​π​(s)⊤​σ​𝑑W​(s),X^{\pi}(T;b,W)=x\_{0}e^{rT}+e^{rT}\int\_{0}^{T}e^{-rs}\pi(s)^{\top}(b-r\mathbf{1})\,ds+e^{rT}\int\_{0}^{T}e^{-rs}\pi(s)^{\top}\sigma\,dW(s), |  | (11) |

which is affine in bb for every realization of WW.
For b∈Kb\in K, define

|  |  |  |
| --- | --- | --- |
|  | gπ​(b):=𝔼ℙW​[U​(Xπ​(T))∣B=b],g\_{\pi}(b):=\mathbb{E}\_{\mathbb{P}^{W}}\left[U\left(X^{\pi}(T)\right)\mid B=b\right], |  |

where the conditional expectation is taken only with respect to the Brownian motion WW.
Equation ([11](https://arxiv.org/html/2512.01408v1#S3.E11 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) shows b↦Xπ​(T;b,W​(ω))b\mapsto X^{\pi}(T;b,W(\omega)) is continuous for every ω\omega, and therefore the same holds for b↦U​(Xπ​(T;b,W​(ω)))b\mapsto U(X^{\pi}(T;b,W(\omega))).

We now justify interchanging limit and expectation. Because π∈𝒜′​(x0)\pi\in\mathcal{A}^{\prime}(x\_{0}), there exists Mπ<∞M\_{\pi}<\infty such that supℚ∈𝒰δOT​(ℙ0)𝔼ℚ​[∫0T‖π​(s)‖2​𝑑s]≤Mπ.\sup\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}\mathbb{E}\_{\mathbb{Q}}\!\left[\int\_{0}^{T}\|\pi(s)\|^{2}ds\right]\leq M\_{\pi}.
Using the variation-of-constants formula ([11](https://arxiv.org/html/2512.01408v1#S3.E11 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")), Jensen’s inequality, and Itô’s isometry, we obtain a constant Cπ>0C\_{\pi}>0, independent of b∈Kb\in K, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​[|Xπ​(T;b,W)|2+ε]≤Cπfor some ​ε>0,\mathbb{E}\_{\mathbb{Q}}\!\left[\left|X^{\pi}(T;b,W)\right|^{2+\varepsilon}\right]\leq C\_{\pi}\qquad\text{for some }\varepsilon>0, |  | (12) |

uniformly over ℚ∈𝒰δOT​(ℙ0)\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0}) and b∈Kb\in K. The compactness of KK ensures
supb∈K‖b−r​𝟏‖<∞\sup\_{b\in K}\|b-r\mathbf{1}\|<\infty, so the deterministic term in ([11](https://arxiv.org/html/2512.01408v1#S3.E11 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) is uniformly controlled in bb, while the stochastic integral does not depend on bb. Moreover, since the wealth dynamics are linear with bounded coefficients (in view of Assumption [2](https://arxiv.org/html/2512.01408v1#Thmassumption2 "Assumption 2 (Compact Support for 𝐵). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")), standard estimates for linear SDEs imply that, for any m>0m>0, there exists Cπ,m<∞C\_{\pi,m}<\infty such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supℚ∈𝒰δOT​(ℙ0)supb∈K𝔼ℚ​[(Xπ​(T;b,W))−m]≤Cπ,m.\sup\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}\ \sup\_{b\in K}\ \mathbb{E}\_{\mathbb{Q}}\!\left[\bigl(X^{\pi}(T;b,W)\bigr)^{-m}\right]\leq C\_{\pi,m}. |  | (13) |

In particular, combining ([12](https://arxiv.org/html/2512.01408v1#S3.E12 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) and ([13](https://arxiv.org/html/2512.01408v1#S3.E13 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) with the max-type growth in Assumption [1](https://arxiv.org/html/2512.01408v1#Thmassumption1 "Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), we may choose p>0p>0 and a constant CU>0C\_{U}>0 such that

|  |  |  |
| --- | --- | --- |
|  | |U​(x)|≤CU​(1+xp+x−p),x>0,|U(x)|\leq C\_{U}\bigl(1+x^{p}+x^{-p}\bigr),\qquad x>0, |  |

and hence there exists an integrable random variable YπY\_{\pi} (depending on π\pi but not on bb) with

|  |  |  |
| --- | --- | --- |
|  | |U​(Xπ​(T;b,W))|≤Yπfor all ​b∈K,ℚ∈𝒰δOT​(ℙ0).|U\bigl(X^{\pi}(T;b,W)\bigr)|\leq Y\_{\pi}\qquad\text{for all }b\in K,\ \mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0}). |  |

Therefore, if bn→bb\_{n}\to b in KK, the pointwise continuity of b↦Xπ​(T;b,W)b\mapsto X^{\pi}(T;b,W) and the dominated convergence theorem yield

|  |  |  |
| --- | --- | --- |
|  | gπ​(bn)=𝔼ℚ​[U​(Xπ​(T;bn,W))∣B=bn]⟶gπ​(b)=𝔼ℚ​[U​(Xπ​(T;b,W))∣B=b].g\_{\pi}(b\_{n})\;=\;\mathbb{E}\_{\mathbb{Q}}\!\left[U\bigl(X^{\pi}(T;b\_{n},W)\bigr)\mid B=b\_{n}\right]\;\longrightarrow\;g\_{\pi}(b)\;=\;\mathbb{E}\_{\mathbb{Q}}\!\left[U\bigl(X^{\pi}(T;b,W)\bigr)\mid B=b\right]. |  |

Thus gπg\_{\pi} is continuous on the compact set KK.
Every ℚ∈𝒰δOT​(ℙ0)\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0}) shares the same law for WW and has a marginal distribution of BB supported in KK. Hence, for fixed π\pi,

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ​[U​(Xπ​(T))]=∫Kgπ​(b)​ℚB​(d​b),\mathbb{E}\_{\mathbb{Q}}\!\left[U(X^{\pi}(T))\right]=\int\_{K}g\_{\pi}(b)\,\mathbb{Q}\_{B}(db), |  |

and the right-hand side depends continuously on ℚB\mathbb{Q}\_{B} under the weak topology because gπg\_{\pi} is continuous and bounded on KK.
This proves the desired continuity in the model variable.

Step 3: Concavity and continuity in the control.
For fixed ℚ∈𝒰δOT​(ℙ0)\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0}), the map
π↦𝔼ℚ​[U​(Xπ​(T))]\pi\mapsto\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi}(T))] is concave because UU is concave
and the state equation is affine in π\pi.

To show continuity on (𝒜′​(x0),d)(\mathcal{A}^{\prime}(x\_{0}),d), let πn→π\pi\_{n}\to\pi in the topology
induced by dd, and set Δ​π​(t)=πn​(t)−π​(t)\Delta\pi(t)=\pi\_{n}(t)-\pi(t). Subtracting the
representations ([11](https://arxiv.org/html/2512.01408v1#S3.E11 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) for πn\pi\_{n} and π\pi, taking quadratic moments,
and using (a1+a2)2≤2​a12+2​a22(a\_{1}+a\_{2})^{2}\leq 2a\_{1}^{2}+2a\_{2}^{2}, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ​[|Xπn​(T)−Xπ​(T)|2]≤C​𝔼ℚ​[∫0T‖Δ​π​(s)‖2​𝑑s],\mathbb{E}\_{\mathbb{Q}}\!\big[|X^{\pi\_{n}}(T)-X^{\pi}(T)|^{2}\big]\;\leq\;C\,\mathbb{E}\_{\mathbb{Q}}\!\left[\int\_{0}^{T}\|\Delta\pi(s)\|^{2}ds\right], |  |

where C=2​e2​r​T​(T​supb∈K‖b−r​𝟏‖2+‖σ​σ⊤‖op)C=2e^{2rT}\Big(T\sup\_{b\in K}\|b-r\mathbf{1}\|^{2}\;+\;\|\sigma\sigma^{\top}\|\_{\mathrm{op}}\Big)
is independent of ℚ\mathbb{Q}. Since d​(πn,π)→0d(\pi\_{n},\pi)\to 0, the right-hand side
converges to zero uniformly over ℚ∈𝒰δOT​(ℙ0)\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0}).
Hence Xπn​(T)→Xπ​(T)in ​L2​(ℚ)X^{\pi\_{n}}(T)\to X^{\pi}(T)\quad\text{in }L^{2}(\mathbb{Q}) (and thus in probability)
uniformly over ℚ∈𝒰δOT​(ℙ0)\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0}).

Next we establish uniform integrability.
Because π∈𝒜′​(x0)\pi\in\mathcal{A}^{\prime}(x\_{0}) and d​(πn,π)→0d(\pi\_{n},\pi)\to 0, there exists
M<∞M<\infty such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supn≥1supℚ∈𝒰δOT​(ℙ0)𝔼ℚ​[∫0T‖πn​(s)‖2​𝑑s]≤M.\sup\_{n\geq 1}\ \sup\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}\mathbb{E}\_{\mathbb{Q}}\!\left[\int\_{0}^{T}\|\pi\_{n}(s)\|^{2}ds\right]\leq M. |  | (14) |

Indeed, for each nn,

|  |  |  |
| --- | --- | --- |
|  | ∫0T‖πn​(s)‖2​𝑑s≤ 2​∫0T‖π​(s)‖2​𝑑s+ 2​∫0T‖Δ​π​(s)‖2​𝑑s,\int\_{0}^{T}\|\pi\_{n}(s)\|^{2}ds\;\leq\;2\int\_{0}^{T}\|\pi(s)\|^{2}ds\;+\;2\int\_{0}^{T}\|\Delta\pi(s)\|^{2}ds, |  |

and the two terms on the right-hand side are uniformly bounded in ℚ\mathbb{Q},
with the second one vanishing as n→∞n\to\infty by the definition of dd.
Using ([14](https://arxiv.org/html/2512.01408v1#S3.E14 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")), the compactness of KK, and the linear
wealth dynamics ([11](https://arxiv.org/html/2512.01408v1#S3.E11 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")), standard estimates for linear SDEs with bounded
coefficients yield the existence of ε>0\varepsilon>0 and, for each m>0m>0,
constants C+,m,C−,m<∞C\_{+,m},C\_{-,m}<\infty such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supn≥1supℚ∈𝒰δOT​(ℙ0)supb∈K𝔼ℚ​[|Xπn​(T;b,W)|2+ε]\displaystyle\sup\_{n\geq 1}\ \sup\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}\ \sup\_{b\in K}\mathbb{E}\_{\mathbb{Q}}\!\big[|X^{\pi\_{n}}(T;b,W)|^{2+\varepsilon}\big] | ≤C+,2+ε,\displaystyle\leq C\_{+,2+\varepsilon}, |  | (15) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | supn≥1supℚ∈𝒰δOT​(ℙ0)supb∈K𝔼ℚ​[(Xπn​(T;b,W))−m]\displaystyle\sup\_{n\geq 1}\ \sup\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}\ \sup\_{b\in K}\mathbb{E}\_{\mathbb{Q}}\!\big[(X^{\pi\_{n}}(T;b,W))^{-m}\big] | ≤C−,m.\displaystyle\leq C\_{-,m}. |  | (16) |

In particular, by the max-type growth in Assumption [1](https://arxiv.org/html/2512.01408v1#Thmassumption1 "Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), there
exist p>0p>0 and CU>0C\_{U}>0 such that

|  |  |  |
| --- | --- | --- |
|  | |U​(x)|≤CU​(1+xp+x−p),x>0,|U(x)|\leq C\_{U}\big(1+x^{p}+x^{-p}\big),\qquad x>0, |  |

and combining this with ([15](https://arxiv.org/html/2512.01408v1#S3.E15 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"))–([16](https://arxiv.org/html/2512.01408v1#S3.E16 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"))
shows that the family {U​(Xπn​(T)):n≥1}\{U(X^{\pi\_{n}}(T)):n\geq 1\} is uniformly integrable
under every ℚ∈𝒰δOT​(ℙ0)\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0}).
Since Xπn​(T)→Xπ​(T)X^{\pi\_{n}}(T)\to X^{\pi}(T) in probability and {U​(Xπn​(T))}n≥1\{U(X^{\pi\_{n}}(T))\}\_{n\geq 1}
is uniformly integrable, the continuity of UU implies
𝔼ℚ​[U​(Xπn​(T))]⟶𝔼ℚ​[U​(Xπ​(T))]\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi\_{n}}(T))]\;\longrightarrow\;\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi}(T))], ∀ℚ∈𝒰δOT​(ℙ0).\forall\,\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0}).
Thus, for each fixed ℚ\mathbb{Q}, the map
π↦𝔼ℚ​[U​(Xπ​(T))]\pi\mapsto\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi}(T))] is continuous on
(𝒜′​(x0),d)(\mathcal{A}^{\prime}(x\_{0}),d).

Step 4: Apply Sion’s min-max theorem on 𝒜′​(x0)\mathcal{A}^{\prime}(x\_{0}). The space 𝒜′​(x0)\mathcal{A}^{\prime}(x\_{0}) is convex because the wealth dynamics are linear in π\pi, and 𝒰δOT​(ℙ0)\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0}) is weakly compact since each admissible BB-marginal is supported in the compact set KK and the Wasserstein/KL balls are weakly closed (Prokhorov’s theorem).
Moreover, the map (π,ℚ)↦𝔼ℚ​[U​(Xπ​(T))](\pi,\mathbb{Q})\mapsto\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi}(T))] satisfies:

* •

  Concavity in π\pi: For fixed ℚ\mathbb{Q}, π↦𝔼ℚ​[U​(Xπ​(T))]\pi\mapsto\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi}(T))] is concave by the previous step.
* •

  Convexity in ℚ\mathbb{Q}: For fixed π\pi, ℚ↦𝔼ℚ​[U​(Xπ​(T))]\mathbb{Q}\mapsto\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi}(T))] is linear (hence convex).
* •

  Continuity in π\pi: For fixed ℚ\mathbb{Q}, π↦𝔼ℚ​[U​(Xπ​(T))]\pi\mapsto\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi}(T))] is continuous on (𝒜′​(x0),d)(\mathcal{A}^{\prime}(x\_{0}),d) (Step 3).
* •

  Continuity in ℚ\mathbb{Q}: For fixed π\pi, ℚ↦𝔼ℚ​[U​(Xπ​(T))]\mathbb{Q}\mapsto\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi}(T))] is continuous under the weak topology on 𝒰δOT​(ℙ0)\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0}) by the argument in Step 2.

By Sion’s min-max theorem applied to 𝒜′​(x0)×𝒰δOT​(ℙ0)\mathcal{A}^{\prime}(x\_{0})\times\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0}), we conclude:

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒜′​(x0)infℚ∈𝒰δOT​(ℙ0)𝔼ℚ​[U​(Xπ​(T))]=infℚ∈𝒰δOT​(ℙ0)supπ∈𝒜′​(x0)𝔼ℚ​[U​(Xπ​(T))].\sup\_{\pi\in\mathcal{A}^{\prime}(x\_{0})}\inf\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi}(T))]=\inf\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}\sup\_{\pi\in\mathcal{A}^{\prime}(x\_{0})}\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi}(T))]. |  |

Step 5: Return to 𝒜​(x0)\mathcal{A}(x\_{0}).
Fix b∈Kb\in K and consider the optimal policy π∗,b\pi^{\*,b} supplied by
Theorem [1](https://arxiv.org/html/2512.01408v1#Thmtheorem1 "Theorem 1 (Karatzas–Zhao [KZ98]’s Solution). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") when the prior is the Dirac mass at bb.
Writing Yb​(t)=σ−1​(b−r​𝟏)​t+W​(t)Y^{b}(t)=\sigma^{-1}(b-r\mathbf{1})t+W(t) and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Θ​(t,y)\displaystyle\Theta(t,y) | =∫ℝdI​(𝒦​(x0)​e−r​TF​(T,z+y))​φT−t​(z)​𝑑z,\displaystyle=\int\_{\mathbb{R}^{d}}I\!\left(\frac{\mathcal{K}(x\_{0})e^{-rT}}{F(T,z+y)}\right)\,\varphi\_{T-t}(z)\,dz, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ξ​(t,y)\displaystyle\Xi(t,y) | =∫ℝd∇zF​(T,z+y)F​(T,z+y)2​I′​(𝒦​(x0)​e−r​TF​(T,z+y))​φT−t​(z)​𝑑z,\displaystyle=\int\_{\mathbb{R}^{d}}\frac{\nabla\_{z}F(T,z+y)}{F(T,z+y)^{2}}\,I^{\prime}\!\left(\frac{\mathcal{K}(x\_{0})e^{-rT}}{F(T,z+y)}\right)\,\varphi\_{T-t}(z)\,dz, |  |

the optimal fraction from Theorem [1](https://arxiv.org/html/2512.01408v1#Thmtheorem1 "Theorem 1 (Karatzas–Zhao [KZ98]’s Solution). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") reads

|  |  |  |
| --- | --- | --- |
|  | π∗,b​(t)X∗,b​(t)=(σ⊤)−1​(−𝒦​(x0)​e−r​T)​Ξ​(t,Yb​(t))Θ​(t,Yb​(t)).\frac{\pi^{\*,b}(t)}{X^{\*,b}(t)}=\left(\sigma^{\top}\right)^{-1}(-\mathcal{K}(x\_{0})e^{-rT})\,\frac{\Xi(t,Y^{b}(t))}{\Theta(t,Y^{b}(t))}. |  |

To bound the ratio, note that for any u∈ℝdu\in\mathbb{R}^{d},

|  |  |  |
| --- | --- | --- |
|  | F​(T,u)=∫KLT​(b~,u)​μ​(d​b~),∇uF​(T,u)=∫Kσ−⊤​(b~−r​𝟏)​LT​(b~,u)​μ​(d​b~).F(T,u)=\int\_{K}L\_{T}(\tilde{b},u)\,\mu(d\tilde{b}),\qquad\nabla\_{u}F(T,u)=\int\_{K}\sigma^{-\top}(\tilde{b}-r\mathbf{1})L\_{T}(\tilde{b},u)\,\mu(d\tilde{b}). |  |

Because KK is compact and σ−⊤​(b~−r​𝟏)\sigma^{-\top}(\tilde{b}-r\mathbf{1}) is continuous in b~\tilde{b},
there exists CK>0C\_{K}>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖∇uF​(T,u)F​(T,u)‖≤CK∀u∈ℝd.\left\|\frac{\nabla\_{u}F(T,u)}{F(T,u)}\right\|\leq C\_{K}\qquad\forall u\in\mathbb{R}^{d}. |  | (17) |

Moreover, LT​(b~,u)L\_{T}(\tilde{b},u) is bounded from above and below by two-sided exponentials in
‖u‖\|u\|, uniformly in b~∈K\tilde{b}\in K, so there exists c0>0c\_{0}>0 with

|  |  |  |  |
| --- | --- | --- | --- |
|  | c0−1​e−c0​‖u‖≤F​(T,u)≤c0​ec0​‖u‖,|1F​(T,u)|≤c0​ec0​‖u‖.c\_{0}^{-1}e^{-c\_{0}\|u\|}\;\leq\;F(T,u)\;\leq\;c\_{0}e^{c\_{0}\|u\|},\qquad\left|\frac{1}{F(T,u)}\right|\leq c\_{0}e^{c\_{0}\|u\|}. |  | (18) |

Recall that
Assumption [1](https://arxiv.org/html/2512.01408v1#Thmassumption1 "Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") guarantees that for some CI,pI>0C\_{I},p\_{I}>0 and cI>0c\_{I}>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |I​(x)|+|I′​(x)|≤CI​(1+xpI+x−pI),I​(x)≥cI​x−pI,x>0.|I(x)|+|I^{\prime}(x)|\;\leq\;C\_{I}\bigl(1+x^{p\_{I}}+x^{-p\_{I}}\bigr),\qquad I(x)\;\geq\;c\_{I}x^{-p\_{I}},\qquad x>0. |  | (19) |

Applying ([19](https://arxiv.org/html/2512.01408v1#S3.E19 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) to
x=𝒦​(x0)​e−r​T/F​(T,z+y)x=\mathcal{K}(x\_{0})e^{-rT}/F(T,z+y)
and using ([18](https://arxiv.org/html/2512.01408v1#S3.E18 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) yields exponential bounds

|  |  |  |
| --- | --- | --- |
|  | |I​(𝒦​(x0)​e−r​TF​(T,z+y))|+|I′​(𝒦​(x0)​e−r​TF​(T,z+y))|≤C′​ec′​‖z+y‖,\Big|I\!\left(\tfrac{\mathcal{K}(x\_{0})e^{-rT}}{F(T,z+y)}\right)\Big|+\Big|I^{\prime}\!\left(\tfrac{\mathcal{K}(x\_{0})e^{-rT}}{F(T,z+y)}\right)\Big|\;\leq\;C^{\prime}e^{c^{\prime}\|z+y\|}, |  |

and crucially, the *lower bound*

|  |  |  |  |
| --- | --- | --- | --- |
|  | Θ​(t,y)=∫ℝdI​(𝒦​(x0)​e−r​TF​(T,z+y))​φT−t​(z)​𝑑z≥c′​exp⁡(−c′′​‖y‖)\Theta(t,y)=\int\_{\mathbb{R}^{d}}I\!\left(\tfrac{\mathcal{K}(x\_{0})e^{-rT}}{F(T,z+y)}\right)\varphi\_{T-t}(z)\,dz\;\geq\;c^{\prime}\,\exp\!\bigl(-c^{\prime\prime}\|y\|\bigr) |  | (20) |

for suitable constants c′,c′′>0c^{\prime},c^{\prime\prime}>0 (using I​(x)≥cI​x−pII(x)\geq c\_{I}x^{-p\_{I}} and the Gaussian tail of φT−t\varphi\_{T-t}).

Similarly,

|  |  |  |
| --- | --- | --- |
|  | |Ξ​(t,y)|≤C2​ec2​‖y‖|\Xi(t,y)|\leq C\_{2}e^{c\_{2}\|y\|} |  |

for constants C2,c2>0C\_{2},c\_{2}>0.

Combining these,

|  |  |  |
| --- | --- | --- |
|  | ‖Ξ​(t,y)Θ​(t,y)‖≤a​ec​‖y‖(t,y)∈[0,T]×ℝd.\left\|\frac{\Xi(t,y)}{\Theta(t,y)}\right\|\;\leq\;a\,e^{c\|y\|}\qquad(t,y)\in[0,T]\times\mathbb{R}^{d}. |  |

Because YbY^{b} has continuous paths,
sup0≤t≤T‖Yb​(t)‖<∞\sup\_{0\leq t\leq T}\|Y^{b}(t)\|<\infty
a.s. Since YbY^{b} is a Brownian motion with bounded drift,
sup0≤t≤T‖Yb​(t)‖\sup\_{0\leq t\leq T}\|Y^{b}(t)\|
admits finite exponential moments. Therefore,

|  |  |  |
| --- | --- | --- |
|  | sup0≤t≤T‖π∗,b​(t)X∗,b​(t)‖≤a​exp⁡(c​sup0≤t≤T‖Yb​(t)‖)<∞ℙ​-a.s.\sup\_{0\leq t\leq T}\left\|\frac{\pi^{\*,b}(t)}{X^{\*,b}(t)}\right\|\;\leq\;a\exp\!\left(c\sup\_{0\leq t\leq T}\|Y^{b}(t)\|\right)<\infty\qquad\mathbb{P}\text{-a.s.} |  |

Finally, X∗,bX^{\*,b} has continuous paths and is strictly positive, so
sup0≤t≤T‖π∗,b​(t)‖<∞\sup\_{0\leq t\leq T}\|\pi^{\*,b}(t)\|<\infty
a.s., and hence
∫0T‖π∗,b​(t)‖2​𝑑t<∞\int\_{0}^{T}\|\pi^{\*,b}(t)\|^{2}dt<\infty
a.s.
The constants above are uniform in b∈Kb\in K, and thus for every
ℚ∈𝒰δOT​(ℙ0)\mathbb{Q}\in\mathcal{U}\_{\delta}^{\mathrm{OT}}(\mathbb{P}\_{0}),

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ​[(∫0T‖π∗​(t)‖2​𝑑t)1/2]<∞.\mathbb{E}\_{\mathbb{Q}}\left[\left(\int\_{0}^{T}\|\pi^{\*}(t)\|^{2}dt\right)^{1/2}\right]<\infty. |  |

This proves π∗∈𝒜′​(x0)⊂𝒜​(x0)\pi^{\*}\in\mathcal{A}^{\prime}(x\_{0})\subset\mathcal{A}(x\_{0}).
Together with the inequalities at the beginning of the proof, this yields the
desired min–max equality on 𝒜​(x0)\mathcal{A}(x\_{0}).

∎

The value of Theorem [2](https://arxiv.org/html/2512.01408v1#Thmtheorem2 "Theorem 2 (Min-Max Equality). ‣ 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") is that for a fixed probability measure ℚ\mathbb{Q}, by Theorem [1](https://arxiv.org/html/2512.01408v1#Thmtheorem1 "Theorem 1 (Karatzas–Zhao [KZ98]’s Solution). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), the inner problem supπ∈𝒜​(x0)𝔼ℚ​[U​(X​(T))]\sup\_{\pi\in\mathcal{A}(x\_{0})}\mathbb{E}\_{\mathbb{Q}}\left[U(X(T))\right] has a closed-form solution in terms of the distribution of the drift BB.
In other words, the DRBC problem is equivalent to solving a constrained distributional optimization problem

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | infℚ∈𝒰δOT​(ℙ0)supπ∈𝒜​(x0)𝔼ℚ​[U​(Xπ​(T))]=infℚ∈𝒰δOT​(ℙ0)∫ℝdF​(T,z)​U​(I​(𝒦​(x0)​e−r​TF​(T,z)))​φT​(z)​𝑑z,\displaystyle\inf\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}\sup\_{\pi\in\mathcal{A}(x\_{0})}\mathbb{E}\_{\mathbb{Q}}\left[U(X^{\pi}(T))\right]=\inf\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}\int\_{\mathbb{R}^{d}}F(T,z)U\left(I\left(\frac{\mathcal{K}(x\_{0})e^{-rT}}{F(T,z)}\right)\right)\varphi\_{T}(z)dz, |  | (21) |

where
𝒰δOT​(ℙ0)\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})
is the uncertainty set that is only concerned with the distribution of BB since the objective function in ([21](https://arxiv.org/html/2512.01408v1#S3.E21 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) no longer contains the Brownian motion WW. Hence, it suffices to optimize over the nonlinear functional and obtain the extreme probability measure ℚ∗\mathbb{Q}^{\*} (denote the functional on the right-hand side of Eq. ([21](https://arxiv.org/html/2512.01408v1#S3.E21 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) by a specific J​(ℚ)J(\mathbb{Q}); see Corollary [1](https://arxiv.org/html/2512.01408v1#Thmcorollary1 "Corollary 1 (Asymptotic non-linear optimal perturbation under Wasserstein distance). ‣ 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") for details):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℚ∗=arg⁡minℚ∈𝒰δOT​(ℙ0)⁡J​(ℚ).\displaystyle\mathbb{Q}^{\*}=\arg\min\_{\mathbb{Q}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{0})}{J}(\mathbb{Q}). |  | (22) |

We will first give a sensitivity analysis of this distributional optimization problem in greater generality for JJ, and then Problem ([22](https://arxiv.org/html/2512.01408v1#S3.E22 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) can be solved easily in an approximate sense by the following Corollary [1](https://arxiv.org/html/2512.01408v1#Thmcorollary1 "Corollary 1 (Asymptotic non-linear optimal perturbation under Wasserstein distance). ‣ 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections").

###### Theorem 3 (Nonlinear optimal perturbations).

Fix 1<q<∞1<q<\infty and let pp be its Hölder conjugate.
Let ∥⋅∥q\|\cdot\|\_{q} be a norm on ℝd\mathbb{R}^{d} and ∥⋅∥p\|\cdot\|\_{p} be its dual norm.
Consider the quadratic transport cost c​(x′−x):=τ​‖x′−x‖q2c(x^{\prime}-x):=\tau\,\|x^{\prime}-x\|\_{q}^{2} with τ>0\tau>0
and let DcD\_{c} denote the corresponding optimal-transport divergence

|  |  |  |
| --- | --- | --- |
|  | Dc​(μ,ν):=infπ∈Π​(μ,ν)𝔼π​[c​(X′−X)].D\_{c}(\mu,\nu):=\inf\_{\pi\in\Pi(\mu,\nu)}\mathbb{E}\_{\pi}\big[c(X^{\prime}-X)\big]. |  |

For δ>0\delta>0, set Vδ:=supDc​(μ,ν)≤δJ​(μ)V\_{\delta}:=\sup\_{D\_{c}(\mu,\nu)\leq\delta}J(\mu), where the functional
J:𝒫​(ℝd)→ℝJ:\mathcal{P}(\mathbb{R}^{d})\to\mathbb{R} satisfies:

* (i)

  For all μ\mu in a neighbourhood of ν\nu, there exists a measurable
  Jμ′:ℝd→ℝJ^{\prime}\_{\mu}:\mathbb{R}^{d}\to\mathbb{R}, differentiable in xx with gradient ∇Jμ′​(x)\nabla J^{\prime}\_{\mu}(x),
  such that for every coupling π\pi of (X′,X)∼(μ,ν)(X^{\prime},X)\sim(\mu,\nu) and
  νt:=(1−t)​ν+t​μ\nu\_{t}:=(1-t)\nu+t\mu,

  |  |  |  |
  | --- | --- | --- |
  |  | J​(μ)−J​(ν)=∫01𝔼π​[Jνt′​(X′)−Jνt′​(X)]​𝑑t.J(\mu)-J(\nu)=\int\_{0}^{1}\mathbb{E}\_{\pi}\big[J^{\prime}\_{\nu\_{t}}(X^{\prime})-J^{\prime}\_{\nu\_{t}}(X)\big]\,dt. |  |
* (ii)

  (Regularity and growth of the Wasserstein gradient)
  The map (μ,x)↦∇Jμ′​(x)(\mu,x)\mapsto\nabla J^{\prime}\_{\mu}(x) is jointly continuous in the product
  topology (weak topology on μ\mu, Euclidean on xx) in a neighbourhood
  of (ν,⋅)(\nu,\cdot).
  Moreover, there exist 1≤r≤21\leq r\leq 2 and C>0C>0 such that for all such μ\mu and all x∈ℝdx\in\mathbb{R}^{d},

  |  |  |  |
  | --- | --- | --- |
  |  | ‖∇Jμ′​(x)‖p≤C​(1+‖x‖r−1),\|\nabla J^{\prime}\_{\mu}(x)\|\_{p}\leq C\big(1+\|x\|^{r-1}\big), |  |

  and the reference law ν\nu has finite 2​r2r-moment:

  |  |  |  |
  | --- | --- | --- |
  |  | 𝔼ν​‖X‖2​r<∞.\mathbb{E}\_{\nu}\|X\|^{2r}<\infty. |  |

Let g​(x):=∇Jν′​(x)g(x):=\nabla J^{\prime}\_{\nu}(x) and assume
𝔼ν​‖g​(X)‖p2<∞\mathbb{E}\_{\nu}\|g(X)\|\_{p}^{2}<\infty.
Then, as δ↓0\delta\downarrow 0,

|  |  |  |
| --- | --- | --- |
|  | Vδ=J​(ν)+δτ​(𝔼ν​[‖g​(X)‖p2])1/2+o​(δ).V\_{\delta}=J(\nu)+\sqrt{\frac{\delta}{\tau}}\,\Big(\mathbb{E}\_{\nu}\big[\|g(X)\|\_{p}^{2}\big]\Big)^{1/2}+o(\sqrt{\delta}). |  |

Moreover, there exists an asymptotically optimal Monge-type perturbation
TδT\_{\delta} of the form

|  |  |  |
| --- | --- | --- |
|  | Tδ​(X)=X+δτ​Δ¯​(X)​(1+op​(1)),T\_{\delta}(X)=X+\sqrt{\frac{\delta}{\tau}}\,\bar{\Delta}(X)\,\big(1+o\_{p}(1)\big), |  |

where for each xx with g​(x)≠0g(x)\neq 0, we choose

|  |  |  |
| --- | --- | --- |
|  | u​(x)∈arg⁡max‖u‖q=1⁡g​(x)⋅u,u(x)\in\arg\max\_{\|u\|\_{q}=1}g(x)\cdot u, |  |

and define

|  |  |  |
| --- | --- | --- |
|  | Δ¯​(x):=‖g​(x)‖pK​u​(x),K:=(𝔼ν​‖g​(X)‖p2)1/2,\bar{\Delta}(x):=\frac{\|g(x)\|\_{p}}{K}\,u(x),\qquad K:=\Big(\mathbb{E}\_{\nu}\|g(X)\|\_{p}^{2}\Big)^{1/2}, |  |

with Δ¯​(x):=0\bar{\Delta}(x):=0 when g​(x)=0g(x)=0.

###### Proof.

Write g​(x):=∇Jν′​(x)g(x):=\nabla J^{\prime}\_{\nu}(x) and

|  |  |  |
| --- | --- | --- |
|  | K:=(𝔼ν​‖g​(X)‖p2)1/2.K:=\Big(\mathbb{E}\_{\nu}\|g(X)\|\_{p}^{2}\Big)^{1/2}. |  |

If K=0K=0, then g​(X)=0g(X)=0 ν\nu-a.s. and ([27](https://arxiv.org/html/2512.01408v1#S3.E27 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) below implies
Vδ−J​(ν)=o​(δ)V\_{\delta}-J(\nu)=o(\sqrt{\delta}), so the claim holds with the identity map.
Hence we henceforth assume K>0K>0.
We will mimic the proof of [BartlDrapeauOblojWiesel2021].

Step 1: Coupling class 𝒞δ\mathcal{C}\_{\delta} and L2L^{2}–scaling.
For δ>0\delta>0, define the class of couplings

|  |  |  |
| --- | --- | --- |
|  | 𝒞δ:={π∈𝒫​(ℝd×ℝd):π​(ℝd,⋅)=ν,𝔼π​[c​(X′−X)]≤δ}.\mathcal{C}\_{\delta}:=\Big\{\pi\in\mathcal{P}(\mathbb{R}^{d}\times\mathbb{R}^{d}):\pi(\mathbb{R}^{d},\cdot)=\nu,\;\mathbb{E}\_{\pi}\big[c(X^{\prime}-X)\big]\leq\delta\Big\}. |  |

Write Δ:=X′−X\Delta:=X^{\prime}-X and note that for π∈𝒞δ\pi\in\mathcal{C}\_{\delta},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼π​‖Δ‖q2≤δτ,‖Δ‖L2​(π):=(𝔼π​‖Δ‖q2)1/2≤δτ.\mathbb{E}\_{\pi}\|\Delta\|\_{q}^{2}\;\leq\;\frac{\delta}{\tau},\qquad\|\Delta\|\_{L^{2}(\pi)}:=\big(\mathbb{E}\_{\pi}\|\Delta\|\_{q}^{2}\big)^{1/2}\;\leq\;\sqrt{\frac{\delta}{\tau}}. |  | (23) |

In particular, if δn↓0\delta\_{n}\downarrow 0 and πn∈𝒞δn\pi\_{n}\in\mathcal{C}\_{\delta\_{n}}, then
‖Δn‖L2​(πn)→0\|\Delta\_{n}\|\_{L^{2}(\pi\_{n})}\to 0, and since ‖Δn‖q2≥0\|\Delta\_{n}\|\_{q}^{2}\geq 0 and
𝔼​‖Δn‖q2→0\mathbb{E}\|\Delta\_{n}\|\_{q}^{2}\to 0, the family {‖Δn‖q2}n\{\|\Delta\_{n}\|\_{q}^{2}\}\_{n} is uniformly integrable.

Moreover, for any μ\mu with Dc​(μ,ν)≤δD\_{c}(\mu,\nu)\leq\delta, there exists at least one coupling
π∈𝒞δ\pi\in\mathcal{C}\_{\delta} with first marginal μ\mu (an optimal transport plan);
conversely, every π∈𝒞δ\pi\in\mathcal{C}\_{\delta}
has some first marginal μ\mu with Dc​(μ,ν)≤δD\_{c}(\mu,\nu)\leq\delta.
Thus

|  |  |  |
| --- | --- | --- |
|  | Vδ−J​(ν)=supμ:Dc​(μ,ν)≤δ(J​(μ)−J​(ν))=supπ∈𝒞δ(J​(μπ)−J​(ν)),V\_{\delta}-J(\nu)=\sup\_{\begin{subarray}{c}\mu:\,D\_{c}(\mu,\nu)\leq\delta\end{subarray}}\big(J(\mu)-J(\nu)\big)=\sup\_{\pi\in\mathcal{C}\_{\delta}}\big(J(\mu\_{\pi})-J(\nu)\big), |  |

where μπ\mu\_{\pi} denotes the first marginal of π\pi.

Step 2: Path identity, Taylor expansion, and linearization.
Fix π∈𝒞δ\pi\in\mathcal{C}\_{\delta} with first marginal μ\mu and displacement Δ=X′−X\Delta=X^{\prime}-X.
For t∈[0,1]t\in[0,1], set νt:=(1−t)​ν+t​μ\nu\_{t}:=(1-t)\nu+t\mu. By Assumption (i),

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(μ)−J​(ν)=∫01𝔼π​[Jνt′​(X′)−Jνt′​(X)]​𝑑t.J(\mu)-J(\nu)=\int\_{0}^{1}\mathbb{E}\_{\pi}\big[J^{\prime}\_{\nu\_{t}}(X^{\prime})-J^{\prime}\_{\nu\_{t}}(X)\big]\,dt. |  | (24) |

For each fixed tt, the map x↦Jνt′​(x)x\mapsto J^{\prime}\_{\nu\_{t}}(x) is differentiable with gradient
∇Jνt′​(x)\nabla J^{\prime}\_{\nu\_{t}}(x). Using the fundamental theorem of calculus along the segment
X+s​ΔX+s\Delta, s∈[0,1]s\in[0,1], we obtain

|  |  |  |
| --- | --- | --- |
|  | Jνt′​(X+Δ)−Jνt′​(X)=∫01∇Jνt′​(X+s​Δ)⋅Δ​𝑑s.J^{\prime}\_{\nu\_{t}}(X+\Delta)-J^{\prime}\_{\nu\_{t}}(X)=\int\_{0}^{1}\nabla J^{\prime}\_{\nu\_{t}}(X+s\Delta)\cdot\Delta\,ds. |  |

Subtract ∇Jνt′​(X)⋅Δ\nabla J^{\prime}\_{\nu\_{t}}(X)\cdot\Delta and define the remainder

|  |  |  |
| --- | --- | --- |
|  | Rδ,t:=∫01(∇Jνt′​(X+s​Δ)−∇Jνt′​(X))⋅Δ​𝑑s.R\_{\delta,t}:=\int\_{0}^{1}\big(\nabla J^{\prime}\_{\nu\_{t}}(X+s\Delta)-\nabla J^{\prime}\_{\nu\_{t}}(X)\big)\cdot\Delta\,ds. |  |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(μ)−J​(ν)=∫01𝔼π​[∇Jνt′​(X)⋅Δ]​𝑑t+∫01𝔼π​[Rδ,t]​𝑑t.J(\mu)-J(\nu)=\int\_{0}^{1}\mathbb{E}\_{\pi}\big[\nabla J^{\prime}\_{\nu\_{t}}(X)\cdot\Delta\big]\,dt\;+\;\int\_{0}^{1}\mathbb{E}\_{\pi}\big[R\_{\delta,t}\big]\,dt. |  | (25) |

We now show that the remainder term is o​(δ)o(\sqrt{\delta}), *uniformly* over
π∈𝒞δ\pi\in\mathcal{C}\_{\delta} and t∈[0,1]t\in[0,1].

By Cauchy–Schwarz in L2​(π)L^{2}(\pi) and Hölder in ℝd\mathbb{R}^{d},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼π​|Rδ,t|\displaystyle\mathbb{E}\_{\pi}|R\_{\delta,t}| | ≤∫01𝔼π​[‖∇Jνt′​(X+s​Δ)−∇Jνt′​(X)‖p​‖Δ‖q]​𝑑s\displaystyle\leq\int\_{0}^{1}\mathbb{E}\_{\pi}\big[\|\nabla J^{\prime}\_{\nu\_{t}}(X+s\Delta)-\nabla J^{\prime}\_{\nu\_{t}}(X)\|\_{p}\,\|\Delta\|\_{q}\big]\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫01‖∇Jνt′​(X+s​Δ)−∇Jνt′​(X)‖L2​(π)​‖Δ‖L2​(π)​𝑑s.\displaystyle\leq\int\_{0}^{1}\big\|\nabla J^{\prime}\_{\nu\_{t}}(X+s\Delta)-\nabla J^{\prime}\_{\nu\_{t}}(X)\big\|\_{L^{2}(\pi)}\,\|\Delta\|\_{L^{2}(\pi)}\,ds. |  |

Using ([23](https://arxiv.org/html/2512.01408v1#S3.E23 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")),

|  |  |  |
| --- | --- | --- |
|  | 𝔼π​|Rδ,t|≤δτ​sups∈[0,1]‖∇Jνt′​(X+s​Δ)−∇Jνt′​(X)‖L2​(π).\mathbb{E}\_{\pi}|R\_{\delta,t}|\leq\sqrt{\frac{\delta}{\tau}}\,\sup\_{s\in[0,1]}\big\|\nabla J^{\prime}\_{\nu\_{t}}(X+s\Delta)-\nabla J^{\prime}\_{\nu\_{t}}(X)\big\|\_{L^{2}(\pi)}. |  |

*Uniform L2L^{2} bounds via polynomial growth.*
By Assumption (ii), there exist 1≤r≤21\leq r\leq 2 and C>0C>0 such that

|  |  |  |
| --- | --- | --- |
|  | ‖∇Jνt′​(x)‖p≤C​(1+‖x‖r−1),x∈ℝd,t∈[0,1],\|\nabla J^{\prime}\_{\nu\_{t}}(x)\|\_{p}\leq C\big(1+\|x\|^{r-1}\big),\qquad x\in\mathbb{R}^{d},\ t\in[0,1], |  |

for all μ\mu in a neighbourhood of ν\nu; in particular this holds for all interpolants
νt=(1−t)​ν+t​μ\nu\_{t}=(1-t)\nu+t\mu with Dc​(μ,ν)D\_{c}(\mu,\nu) small. Let (X′,X)∼π∈𝒞δ0(X^{\prime},X)\sim\pi\in\mathcal{C}\_{\delta\_{0}}.
Then, by the triangle inequality and the fact that 2​(r−1)≤22(r-1)\leq 2,

|  |  |  |
| --- | --- | --- |
|  | ‖X+s​Δ‖2​(r−1)≤C′​(‖X‖2​(r−1)+‖Δ‖2​(r−1)),s∈[0,1],\|X+s\Delta\|^{2(r-1)}\leq C^{\prime}\big(\|X\|^{2(r-1)}+\|\Delta\|^{2(r-1)}\big),\qquad s\in[0,1], |  |

for some C′>0C^{\prime}>0. Since 2​(r−1)≤22(r-1)\leq 2 and 𝔼π​‖Δ‖2≤δ0/τ\mathbb{E}\_{\pi}\|\Delta\|^{2}\leq\delta\_{0}/\tau, Jensen’s
inequality yields

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒞δ0𝔼π​‖Δ‖2​(r−1)<∞,\sup\_{\pi\in\mathcal{C}\_{\delta\_{0}}}\mathbb{E}\_{\pi}\|\Delta\|^{2(r-1)}<\infty, |  |

and 𝔼ν​‖X‖2​r<∞\mathbb{E}\_{\nu}\|X\|^{2r}<\infty implies 𝔼ν​‖X‖2​(r−1)<∞\mathbb{E}\_{\nu}\|X\|^{2(r-1)}<\infty, so

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒞δ0sups∈[0,1]𝔼π​‖X+s​Δ‖2​(r−1)<∞.\sup\_{\pi\in\mathcal{C}\_{\delta\_{0}}}\sup\_{s\in[0,1]}\mathbb{E}\_{\pi}\|X+s\Delta\|^{2(r-1)}<\infty. |  |

Using the growth bound

|  |  |  |
| --- | --- | --- |
|  | ‖∇Jνt′​(X+s​Δ)‖p2≤C′′​(1+‖X+s​Δ‖2​(r−1)),\|\nabla J^{\prime}\_{\nu\_{t}}(X+s\Delta)\|\_{p}^{2}\leq C^{\prime\prime}\big(1+\|X+s\Delta\|^{2(r-1)}\big), |  |

we obtain

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒞δ0supt∈[0,1],s∈[0,1]𝔼π​[‖∇Jνt′​(X+s​Δ)‖p2]<∞,\sup\_{\pi\in\mathcal{C}\_{\delta\_{0}}}\sup\_{t\in[0,1],\,s\in[0,1]}\mathbb{E}\_{\pi}\big[\|\nabla J^{\prime}\_{\nu\_{t}}(X+s\Delta)\|\_{p}^{2}\big]<\infty, |  |

and likewise

|  |  |  |
| --- | --- | --- |
|  | supt∈[0,1]𝔼ν​[‖∇Jνt′​(X)‖p2]<∞.\sup\_{t\in[0,1]}\mathbb{E}\_{\nu}\big[\|\nabla J^{\prime}\_{\nu\_{t}}(X)\|\_{p}^{2}\big]<\infty. |  |

Thus the family {∇Jνt′​(X+s​Δ):π∈𝒞δ0,t,s∈[0,1]}\{\nabla J^{\prime}\_{\nu\_{t}}(X+s\Delta):\pi\in\mathcal{C}\_{\delta\_{0}},t,s\in[0,1]\}
is uniformly square-integrable.

*Spatial term.*
For the spatial part, set

|  |  |  |
| --- | --- | --- |
|  | Aδ,t,s:=‖∇Jνt′​(X+s​Δ)−∇Jνt′​(X)‖L2​(π).A\_{\delta,t,s}:=\big\|\nabla J^{\prime}\_{\nu\_{t}}(X+s\Delta)-\nabla J^{\prime}\_{\nu\_{t}}(X)\big\|\_{L^{2}(\pi)}. |  |

By joint continuity of (μ,x)↦∇Jμ′​(x)(\mu,x)\mapsto\nabla J^{\prime}\_{\mu}(x) and the fact that
‖Δ‖L2​(π)→0\|\Delta\|\_{L^{2}(\pi)}\to 0 uniformly over π∈𝒞δ\pi\in\mathcal{C}\_{\delta} as δ↓0\delta\downarrow 0,
we have ∇Jνt′​(X+s​Δ)→∇Jνt′​(X)\nabla J^{\prime}\_{\nu\_{t}}(X+s\Delta)\to\nabla J^{\prime}\_{\nu\_{t}}(X) in probability.
Together with the uniform L2L^{2}-bound just proved and uniform integrability of
‖∇Jνt′​(X+s​Δ)‖p2\|\nabla J^{\prime}\_{\nu\_{t}}(X+s\Delta)\|\_{p}^{2}, Vitali’s theorem yields

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒞δsupt∈[0,1],s∈[0,1]Aδ,t,s=o​(1),δ↓0.\sup\_{\pi\in\mathcal{C}\_{\delta}}\sup\_{t\in[0,1],\,s\in[0,1]}A\_{\delta,t,s}\;=\;o(1),\qquad\delta\downarrow 0. |  |

*Measure term.*
For the measure part, consider

|  |  |  |
| --- | --- | --- |
|  | Bδ,t:=∥∇Jνt′(X)−g(X)∥L2​(π).B\_{\delta,t}:=\big\|\nabla J^{\prime}\_{\nu\_{t}}(X)-g(X)\big\|\_{L^{2}(\pi)}. |  |

Since XX has law ν\nu under any π∈𝒞δ\pi\in\mathcal{C}\_{\delta}, this is

|  |  |  |
| --- | --- | --- |
|  | Bδ,t=(𝔼ν​[‖∇Jνt′​(X)−g​(X)‖p2])1/2.B\_{\delta,t}=\Big(\mathbb{E}\_{\nu}\big[\|\nabla J^{\prime}\_{\nu\_{t}}(X)-g(X)\|\_{p}^{2}\big]\Big)^{1/2}. |  |

By joint continuity of (μ,x)↦∇Jμ′​(x)(\mu,x)\mapsto\nabla J^{\prime}\_{\mu}(x) and the uniform L2L^{2}-bound
from the growth condition, the map
μ↦∇Jμ′\mu\mapsto\nabla J^{\prime}\_{\mu} is continuous in L2​(ν)L^{2}(\nu) near ν\nu.
Moreover, for μ\mu with Dc​(μ,ν)≤δ0D\_{c}(\mu,\nu)\leq\delta\_{0}, all interpolants
νt=(1−t)​ν+t​μ\nu\_{t}=(1-t)\nu+t\mu also satisfy Dc​(νt,ν)≤δ0D\_{c}(\nu\_{t},\nu)\leq\delta\_{0}, so the same
uniform bound applies. Since νt→ν\nu\_{t}\to\nu weakly and the family is uniformly
square-integrable, Vitali’s theorem yields

|  |  |  |
| --- | --- | --- |
|  | supμ:Dc​(μ,ν)≤δ0,t∈[0,1]Bδ,t=o​(1),\sup\_{\begin{subarray}{c}\mu:D\_{c}(\mu,\nu)\leq\delta\_{0},\\ t\in[0,1]\end{subarray}}B\_{\delta,t}=o(1), |  |

as μ→ν\mu\to\nu (hence νt→ν\nu\_{t}\to\nu in the weak topology). Since here
we are only considering μ\mu with Dc​(μ,ν)≤δD\_{c}(\mu,\nu)\leq\delta and δ↓0\delta\downarrow 0,
this implies

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒞δsupt∈[0,1]Bδ,t=o​(1).\sup\_{\pi\in\mathcal{C}\_{\delta}}\sup\_{t\in[0,1]}B\_{\delta,t}\;=\;o(1). |  |

Putting the spatial and measure parts together and using the triangle inequality, we obtain

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒞δsupt∈[0,1]sups∈[0,1]‖∇Jνt′​(X+s​Δ)−g​(X)‖L2​(π)=o​(1),δ↓0.\sup\_{\pi\in\mathcal{C}\_{\delta}}\sup\_{t\in[0,1]}\sup\_{s\in[0,1]}\big\|\nabla J^{\prime}\_{\nu\_{t}}(X+s\Delta)-g(X)\big\|\_{L^{2}(\pi)}=o(1),\qquad\delta\downarrow 0. |  |

In particular,

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒞δsupt∈[0,1]sups∈[0,1]‖∇Jνt′​(X+s​Δ)−∇Jνt′​(X)‖L2​(π)=o​(1),δ↓0.\sup\_{\pi\in\mathcal{C}\_{\delta}}\sup\_{t\in[0,1]}\sup\_{s\in[0,1]}\big\|\nabla J^{\prime}\_{\nu\_{t}}(X+s\Delta)-\nabla J^{\prime}\_{\nu\_{t}}(X)\big\|\_{L^{2}(\pi)}=o(1),\qquad\delta\downarrow 0. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒞δsupt∈[0,1]𝔼π​|Rδ,t|≤δτ⋅o​(1)=o​(δ),\sup\_{\pi\in\mathcal{C}\_{\delta}}\sup\_{t\in[0,1]}\mathbb{E}\_{\pi}|R\_{\delta,t}|\;\leq\;\sqrt{\frac{\delta}{\tau}}\cdot o(1)=o(\sqrt{\delta}), |  |

and integrating over t∈[0,1]t\in[0,1],

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒞δ|∫01𝔼π​[Rδ,t]​𝑑t|=o​(δ),δ↓0.\sup\_{\pi\in\mathcal{C}\_{\delta}}\left|\int\_{0}^{1}\mathbb{E}\_{\pi}[R\_{\delta,t}]\,dt\right|=o(\sqrt{\delta}),\qquad\delta\downarrow 0. |  |

Next, by the same Vitali-type argument (now without the ss-shift),

|  |  |  |
| --- | --- | --- |
|  | ∫01𝔼π​[∇Jνt′​(X)⋅Δ]​𝑑t=𝔼π​[g​(X)⋅Δ]+o​(δ),\int\_{0}^{1}\mathbb{E}\_{\pi}\big[\nabla J^{\prime}\_{\nu\_{t}}(X)\cdot\Delta\big]\,dt=\mathbb{E}\_{\pi}[g(X)\cdot\Delta]+o(\sqrt{\delta}), |  |

uniformly over π∈𝒞δ\pi\in\mathcal{C}\_{\delta}. Combining this with
([25](https://arxiv.org/html/2512.01408v1#S3.E25 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")), we conclude that

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(μ)−J​(ν)=𝔼π​[g​(X)⋅Δ]+o​(δ),J(\mu)-J(\nu)=\mathbb{E}\_{\pi}[g(X)\cdot\Delta]+o(\sqrt{\delta}), |  | (26) |

with the o​(δ)o(\sqrt{\delta}) term uniform over π∈𝒞δ\pi\in\mathcal{C}\_{\delta} (hence over all
feasible μ\mu with Dc​(μ,ν)≤δD\_{c}(\mu,\nu)\leq\delta).

Taking the supremum over π∈𝒞δ\pi\in\mathcal{C}\_{\delta},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vδ−J​(ν)=supπ∈𝒞δ𝔼π​[g​(X)⋅Δ]+o​(δ),δ↓0.V\_{\delta}-J(\nu)=\sup\_{\pi\in\mathcal{C}\_{\delta}}\mathbb{E}\_{\pi}[g(X)\cdot\Delta]\;+\;o(\sqrt{\delta}),\qquad\delta\downarrow 0. |  | (27) |

Step 3: Upper bound via Hölder and Cauchy–Schwarz.
For any π∈𝒞δ\pi\in\mathcal{C}\_{\delta},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼π​[g​(X)⋅Δ]\displaystyle\mathbb{E}\_{\pi}[g(X)\cdot\Delta] | ≤𝔼π​[‖g​(X)‖p​‖Δ‖q]​(𝔼ν​‖g​(X)‖p2)1/2​(𝔼π​‖Δ‖q2)1/2≤K​δτ,\displaystyle\leq\mathbb{E}\_{\pi}\big[\|g(X)\|\_{p}\,\|\Delta\|\_{q}\big]\Big(\mathbb{E}\_{\nu}\|g(X)\|\_{p}^{2}\Big)^{1/2}\Big(\mathbb{E}\_{\pi}\|\Delta\|\_{q}^{2}\Big)^{1/2}\leq K\,\sqrt{\frac{\delta}{\tau}}, |  |

where we used that X∼νX\sim\nu under π\pi and ([23](https://arxiv.org/html/2512.01408v1#S3.E23 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")).
Thus,

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒞δ𝔼π​[g​(X)⋅Δ]≤K​δτ,\sup\_{\pi\in\mathcal{C}\_{\delta}}\mathbb{E}\_{\pi}[g(X)\cdot\Delta]\leq K\,\sqrt{\frac{\delta}{\tau}}, |  |

and ([27](https://arxiv.org/html/2512.01408v1#S3.E27 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) yields

|  |  |  |
| --- | --- | --- |
|  | Vδ−J​(ν)≤δτ​K+o​(δ).V\_{\delta}-J(\nu)\leq\sqrt{\frac{\delta}{\tau}}\,K+o(\sqrt{\delta}). |  |

Step 4: Lower bound via a deterministic extremal Monge map.
For each xx with g​(x)≠0g(x)\neq 0, choose

|  |  |  |
| --- | --- | --- |
|  | u​(x)∈arg⁡max‖u‖q=1⁡g​(x)⋅u,u(x)\in\arg\max\_{\|u\|\_{q}=1}g(x)\cdot u, |  |

and define

|  |  |  |
| --- | --- | --- |
|  | Δ¯​(x):=‖g​(x)‖pK​u​(x),Δ¯​(x):=0​ if ​g​(x)=0.\bar{\Delta}(x):=\frac{\|g(x)\|\_{p}}{K}\,u(x),\qquad\bar{\Delta}(x):=0\text{ if }g(x)=0. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | 𝔼ν​‖Δ¯​(X)‖q2=1K2​𝔼ν​‖g​(X)‖p2=1,\mathbb{E}\_{\nu}\|\bar{\Delta}(X)\|\_{q}^{2}=\frac{1}{K^{2}}\,\mathbb{E}\_{\nu}\|g(X)\|\_{p}^{2}=1, |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝔼ν​[g​(X)⋅Δ¯​(X)]=1K​𝔼ν​[‖g​(X)‖p​g​(X)⋅u​(X)]=1K​𝔼ν​‖g​(X)‖p2=K.\mathbb{E}\_{\nu}[g(X)\cdot\bar{\Delta}(X)]=\frac{1}{K}\,\mathbb{E}\_{\nu}\big[\|g(X)\|\_{p}\,g(X)\cdot u(X)\big]=\frac{1}{K}\,\mathbb{E}\_{\nu}\|g(X)\|\_{p}^{2}=K. |  |

Define the Monge map

|  |  |  |
| --- | --- | --- |
|  | Tδ​(x):=x+δτ​Δ¯​(x),μδ:=Tδ​#​ν,T\_{\delta}(x):=x+\sqrt{\frac{\delta}{\tau}}\,\bar{\Delta}(x),\qquad\mu\_{\delta}:=T\_{\delta\#}\nu, |  |

and let πδ\pi\_{\delta} be the coupling (X′,X)=(Tδ​(X),X)(X^{\prime},X)=(T\_{\delta}(X),X) with X∼νX\sim\nu.
Then

|  |  |  |
| --- | --- | --- |
|  | 𝔼πδ​‖X′−X‖q2=δτ​𝔼ν​‖Δ¯​(X)‖q2=δτ,\mathbb{E}\_{\pi\_{\delta}}\|X^{\prime}-X\|\_{q}^{2}=\frac{\delta}{\tau}\,\mathbb{E}\_{\nu}\|\bar{\Delta}(X)\|\_{q}^{2}=\frac{\delta}{\tau}, |  |

so

|  |  |  |
| --- | --- | --- |
|  | Dc​(μδ,ν)≤𝔼πδ​c​(X′−X)=τ​𝔼πδ​‖X′−X‖q2=δ,D\_{c}(\mu\_{\delta},\nu)\leq\mathbb{E}\_{\pi\_{\delta}}c(X^{\prime}-X)=\tau\,\mathbb{E}\_{\pi\_{\delta}}\|X^{\prime}-X\|\_{q}^{2}=\delta, |  |

and hence πδ∈𝒞δ\pi\_{\delta}\in\mathcal{C}\_{\delta} and μδ\mu\_{\delta} is feasible.

Applying ([26](https://arxiv.org/html/2512.01408v1#S3.E26 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) with πδ\pi\_{\delta},

|  |  |  |
| --- | --- | --- |
|  | J​(μδ)−J​(ν)=𝔼πδ​[g​(X)⋅Δ]+o​(δ)=δτ​𝔼ν​[g​(X)⋅Δ¯​(X)]+o​(δ)=δτ​K+o​(δ).J(\mu\_{\delta})-J(\nu)=\mathbb{E}\_{\pi\_{\delta}}[g(X)\cdot\Delta]+o(\sqrt{\delta})=\sqrt{\frac{\delta}{\tau}}\,\mathbb{E}\_{\nu}[g(X)\cdot\bar{\Delta}(X)]+o(\sqrt{\delta})=\sqrt{\frac{\delta}{\tau}}\,K+o(\sqrt{\delta}). |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | lim infδ↓0Vδ−J​(ν)δ≥1τ​K.\liminf\_{\delta\downarrow 0}\frac{V\_{\delta}-J(\nu)}{\sqrt{\delta}}\geq\sqrt{\frac{1}{\tau}}\,K. |  |

Step 5: Conclusion.
Combining the upper bound from Step 3 with the lower bound from Step 4,

|  |  |  |
| --- | --- | --- |
|  | 1τ​K≤lim infδ↓0Vδ−J​(ν)δ≤lim supδ↓0Vδ−J​(ν)δ≤1τ​K.\sqrt{\frac{1}{\tau}}\,K\leq\liminf\_{\delta\downarrow 0}\frac{V\_{\delta}-J(\nu)}{\sqrt{\delta}}\leq\limsup\_{\delta\downarrow 0}\frac{V\_{\delta}-J(\nu)}{\sqrt{\delta}}\leq\sqrt{\frac{1}{\tau}}\,K. |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | Vδ=J​(ν)+δτ​K+o​(δ)=J​(ν)+δτ​(𝔼ν​‖g​(X)‖p2)1/2+o​(δ),V\_{\delta}=J(\nu)+\sqrt{\frac{\delta}{\tau}}\,K+o(\sqrt{\delta})=J(\nu)+\sqrt{\frac{\delta}{\tau}}\,\Big(\mathbb{E}\_{\nu}\|g(X)\|\_{p}^{2}\Big)^{1/2}+o(\sqrt{\delta}), |  |

and the Monge map TδT\_{\delta} constructed in Step 4 is asymptotically optimal
and of the stated form.
∎

When applied to the specific Problem ([22](https://arxiv.org/html/2512.01408v1#S3.E22 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")), the proof reduces to explicitly computing the Wasserstein derivative and the checking the regularity conditions.

###### Corollary 1 (Asymptotic non-linear optimal perturbation under Wasserstein distance).

Suppose Assumptions [1](https://arxiv.org/html/2512.01408v1#Thmassumption1 "Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and [2](https://arxiv.org/html/2512.01408v1#Thmassumption2 "Assumption 2 (Compact Support for 𝐵). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") hold. Define the functional

|  |  |  |
| --- | --- | --- |
|  | J​(ℚ)=∫ℝdFℚ​(T,z)​U​(I​(𝒦ℚ​(x0)​e−r​TFℚ​(T,z)))​φT​(z)​𝑑z,ℚ∈𝒰δOT​(ℙ0),J(\mathbb{Q})=\int\_{\mathbb{R}^{d}}F\_{\mathbb{Q}}(T,z)\,U\!\left(I\!\left(\frac{\mathcal{K}\_{\mathbb{Q}}(x\_{0})e^{-rT}}{F\_{\mathbb{Q}}(T,z)}\right)\right)\varphi\_{T}(z)\,dz,\qquad\mathbb{Q}\in\mathcal{U}^{\mathrm{OT}}\_{\delta}(\mathbb{P}\_{0}), |  |

where Fℚ​(T,z)=𝔼ℚ​[LT​(B,z)]F\_{\mathbb{Q}}(T,z)=\mathbb{E}\_{\mathbb{Q}}[L\_{T}(B,z)] and the uncertainty set
𝒰δOT​(ℙ0)={ℚ:Dc​(ℚ,ℙ0)≤δ}\mathcal{U}^{\mathrm{OT}}\_{\delta}(\mathbb{P}\_{0})=\{\mathbb{Q}:D\_{c}(\mathbb{Q},\mathbb{P}\_{0})\leq\delta\}
is the 2-Wasserstein ball with quadratic cost c​(b′−b)=‖b′−b‖22c(b^{\prime}-b)=\|b^{\prime}-b\|\_{2}^{2}.
Define the influence function H:ℝd→ℝdH:\mathbb{R}^{d}\to\mathbb{R}^{d} by

|  |  |  |
| --- | --- | --- |
|  | H​(b):=∇Jℙ0′​(b)=∫ℝd∇bLT​(b,z)​(𝒦ℙ0​(x0)​e−r​TFℙ0​(T,z))2​φT​(z)​𝑑z,H(b):=\nabla J^{\prime}\_{\mathbb{P}\_{0}}(b)=\int\_{\mathbb{R}^{d}}\nabla\_{b}L\_{T}(b,z)\,\left(\frac{\mathcal{K}\_{\mathbb{P}\_{0}}(x\_{0})e^{-rT}}{F\_{\mathbb{P}\_{0}}(T,z)}\right)^{2}\varphi\_{T}(z)\,dz, |  |

where 𝒦ℙ0​(x0)\mathcal{K}\_{\mathbb{P}\_{0}}(x\_{0}) is the unique solution to the budget constraint under ℙ0\mathbb{P}\_{0}. Let

|  |  |  |
| --- | --- | --- |
|  | ‖H‖L2​(ℙ0):=(𝔼ℙ0​[‖H​(B)‖22])1/2.\|H\|\_{L^{2}(\mathbb{P}\_{0})}:=\left(\mathbb{E}\_{\mathbb{P}\_{0}}\big[\|H(B)\|\_{2}^{2}\big]\right)^{1/2}. |  |

Then, as δ→0\delta\to 0, an asymptotically optimal adversarial perturbation is given by the pushforward ℚδ∗=(I+Δδ∗)#​ℙ0\mathbb{Q}^{\*}\_{\delta}=(I+\Delta^{\*}\_{\delta})\_{\#}\mathbb{P}\_{0}, where

|  |  |  |
| --- | --- | --- |
|  | Δδ∗​(b)=−δ​H​(b)‖H‖L2​(ℙ0)+o​(δ)in ​L2​(ℙ0).\Delta\_{\delta}^{\*}(b)=-\sqrt{\delta}\,\frac{H(b)}{\|H\|\_{L^{2}(\mathbb{P}\_{0})}}+o(\sqrt{\delta})\quad\text{in }L^{2}(\mathbb{P}\_{0}). |  |

Furthermore, the corresponding asymptotically optimal value is

|  |  |  |
| --- | --- | --- |
|  | infℚ∈𝒰δOT​(ℙ0)J​(ℚ)=J​(ℙ0)−δ​‖H‖L2​(ℙ0)+o​(δ).\inf\_{\mathbb{Q}\in\mathcal{U}^{\mathrm{OT}}\_{\delta}(\mathbb{P}\_{0})}J(\mathbb{Q})=J(\mathbb{P}\_{0})-\sqrt{\delta}\,\|H\|\_{L^{2}(\mathbb{P}\_{0})}+o(\sqrt{\delta}). |  |

###### Proof.

We show that JJ satisfies the assumptions of Theorem [3](https://arxiv.org/html/2512.01408v1#Thmtheorem3 "Theorem 3 (Nonlinear optimal perturbations). ‣ 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")
with q=p=2q=p=2, compute the Wasserstein gradient at ℙ0\mathbb{P}\_{0}, and then apply the theorem
to the functional −J-J to obtain the stated expansion.

Step 1: Computation of the Wasserstein derivative at ℙ0\mathbb{P}\_{0}.
Consider the perturbation ℙϵ=(1−ϵ)​ℙ0+ϵ​δb\mathbb{P}^{\epsilon}=(1-\epsilon)\mathbb{P}\_{0}+\epsilon\delta\_{b} and write
kϵ=𝒦ℙϵ​(x0)k^{\epsilon}=\mathcal{K}\_{\mathbb{P}^{\epsilon}}(x\_{0}), Fϵ​(z)=Fℙϵ​(T,z)F^{\epsilon}(z)=F\_{\mathbb{P}^{\epsilon}}(T,z), and

|  |  |  |
| --- | --- | --- |
|  | J​(ℙϵ)=∫ℝdFϵ​(z)​U​(I​(kϵ​e−r​TFϵ​(z)))​φT​(z)​𝑑z.J(\mathbb{P}^{\epsilon})=\int\_{\mathbb{R}^{d}}F^{\epsilon}(z)\,U\!\left(I\!\left(\frac{k^{\epsilon}e^{-rT}}{F^{\epsilon}(z)}\right)\right)\varphi\_{T}(z)\,dz. |  |

Since Fϵ​(z)=(1−ϵ)​F0​(z)+ϵ​LT​(b,z)F^{\epsilon}(z)=(1-\epsilon)F\_{0}(z)+\epsilon L\_{T}(b,z) and all integrands are dominated by
exp⁡(c​‖z‖)​φT​(z)\exp(c\|z\|)\varphi\_{T}(z) (by Assumption [1](https://arxiv.org/html/2512.01408v1#Thmassumption1 "Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and compactness of BB),
the dominated convergence theorem applies, allowing differentiation under the integral.

Differentiating J​(ℙϵ)J(\mathbb{P}^{\epsilon}) at ϵ=0\epsilon=0, and using
U′​(I​(y))=yU^{\prime}(I(y))=y, I′​(y)=1/U′′​(I​(y))I^{\prime}(y)=1/U^{\prime\prime}(I(y)), and the fact that the term containing
k˙=d​kϵd​ϵ|ϵ=0\dot{k}=\frac{dk^{\epsilon}}{d\epsilon}|\_{\epsilon=0} cancels by an envelope-theorem argument,
one obtains the first variation

|  |  |  |
| --- | --- | --- |
|  | δ​Jδ​ℙ0​(b)=(k0​e−r​T)2​∫ℝdLT​(b,z)F0​(z)2​φT​(z)​𝑑z.\frac{\delta J}{\delta\mathbb{P}\_{0}}(b)=(k^{0}e^{-rT})^{2}\int\_{\mathbb{R}^{d}}\frac{L\_{T}(b,z)}{F\_{0}(z)^{2}}\varphi\_{T}(z)\,dz. |  |

Taking the spatial gradient yields the Wasserstein gradient

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇Jℙ0′(b)=∫ℝd∇bLT(b,z)(𝒦ℙ0​(x0)​e−r​TFℙ0​(T,z))2φT(z)dz=:H(b),\nabla J^{\prime}\_{\mathbb{P}\_{0}}(b)=\int\_{\mathbb{R}^{d}}\nabla\_{b}L\_{T}(b,z)\left(\frac{\mathcal{K}\_{\mathbb{P}\_{0}}(x\_{0})e^{-rT}}{F\_{\mathbb{P}\_{0}}(T,z)}\right)^{2}\varphi\_{T}(z)\,dz=:H(b), |  | (28) |

matching exactly the influence function stated in the corollary.

Step 2: Verifying regularity and applying Theorem [3](https://arxiv.org/html/2512.01408v1#Thmtheorem3 "Theorem 3 (Nonlinear optimal perturbations). ‣ 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections").
All remaining assumptions of Theorem [3](https://arxiv.org/html/2512.01408v1#Thmtheorem3 "Theorem 3 (Nonlinear optimal perturbations). ‣ 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") follow immediately
from the compact support of BB (Assumption [2](https://arxiv.org/html/2512.01408v1#Thmassumption2 "Assumption 2 (Compact Support for 𝐵). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")), the exponential bounds
on LTL\_{T} and ∇bLT\nabla\_{b}L\_{T} from Assumption [1](https://arxiv.org/html/2512.01408v1#Thmassumption1 "Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), and the continuity of
ℚ↦Fℚ\mathbb{Q}\mapsto F\_{\mathbb{Q}} and ℚ↦𝒦ℚ​(x0)\mathbb{Q}\mapsto\mathcal{K}\_{\mathbb{Q}}(x\_{0}) under weak convergence.
In particular:

(i) H∈L2​(ℙ0)H\in L^{2}(\mathbb{P}\_{0}) by the uniform exponential bound in ([28](https://arxiv.org/html/2512.01408v1#S3.E28 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"));
(ii) (ℚ,b)↦∇Jℚ′​(b)(\mathbb{Q},b)\mapsto\nabla J^{\prime}\_{\mathbb{Q}}(b) is jointly continuous, again by dominated convergence;
(iii) JJ is Gâteaux differentiable along quadratic-cost interpolations, so the linearization formula required by the theorem holds.

Thus, the hypotheses of Theorem [3](https://arxiv.org/html/2512.01408v1#Thmtheorem3 "Theorem 3 (Nonlinear optimal perturbations). ‣ 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") hold with q=p=2q=p=2 and r=1r=1.

Applying the theorem to J~​(ℚ)=−J​(ℚ)\widetilde{J}(\mathbb{Q})=-J(\mathbb{Q}) (so that ∇J~ℙ0′=−H\nabla\widetilde{J}^{\prime}\_{\mathbb{P}\_{0}}=-H)
gives, as δ→0\delta\to 0,

|  |  |  |
| --- | --- | --- |
|  | supℚ:Dc​(ℚ,ℙ0)≤δJ~​(ℚ)=J~​(ℙ0)+δ​‖H‖L2​(ℙ0)+o​(δ),\sup\_{\mathbb{Q}:D\_{c}(\mathbb{Q},\mathbb{P}\_{0})\leq\delta}\widetilde{J}(\mathbb{Q})=\widetilde{J}(\mathbb{P}\_{0})+\sqrt{\delta}\,\|H\|\_{L^{2}(\mathbb{P}\_{0})}+o(\sqrt{\delta}), |  |

which is equivalent to

|  |  |  |
| --- | --- | --- |
|  | infℚ:Dc​(ℚ,ℙ0)≤δJ​(ℚ)=J​(ℙ0)−δ​‖H‖L2​(ℙ0)+o​(δ).\inf\_{\mathbb{Q}:D\_{c}(\mathbb{Q},\mathbb{P}\_{0})\leq\delta}J(\mathbb{Q})=J(\mathbb{P}\_{0})-\sqrt{\delta}\,\|H\|\_{L^{2}(\mathbb{P}\_{0})}+o(\sqrt{\delta}). |  |

The optimal perturbation is the Monge map

|  |  |  |
| --- | --- | --- |
|  | Δδ​(b)=−δ​H​(b)‖H‖L2​(ℙ0)+o​(δ)in ​L2​(ℙ0),\Delta\_{\delta}(b)=-\sqrt{\delta}\,\frac{H(b)}{\|H\|\_{L^{2}(\mathbb{P}\_{0})}}+o(\sqrt{\delta})\quad\text{in }L^{2}(\mathbb{P}\_{0}), |  |

as asserted. This completes the proof.
∎

###### Remark 2 (Connection to Dual Problem).

The conjugate function I​(y)=(U′)−1​(y)I(y)=(U^{\prime})^{-1}(y) appears naturally in the dual formulation of the robust optimization problem. In particular, the optimal density tilt under
KL divergence is proportional to I​(λ​LT​(b,y))I(\lambda L\_{T}(b,y)) for some Lagrange multiplier λ\lambda. However, under Wasserstein distance and compact support, we do not need to solve the dual — the first-order condition suffices.

If ℙ0=ℙn\mathbb{P}\_{0}=\mathbb{P}\_{n} for some empirical measure, then we can compute Δ∗\Delta^{\*} by replacing ℙ0\mathbb{P}\_{0} by ℙn\mathbb{P}\_{n} conditioned on these samples, rather than viewing them as random measures. We are going to construct i.i.d. samples of B(k)B^{(k)} in Section [4](https://arxiv.org/html/2512.01408v1#S4 "4 Data-Driven Formulation and Choice of Model Parameters ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), and then we construct the optimal measure for the original problem via the perturbed empirical measure

|  |  |  |
| --- | --- | --- |
|  | ℙn​(d​x)=1n​∑k=1nδC(k)​(d​x),\mathbb{P}\_{n}(dx)\;=\;\frac{1}{n}\sum\_{k=1}^{n}\delta\_{C^{(k)}}(dx), |  |

where for each kk, C(k)=B(k)+Δ∗C^{(k)}=B^{(k)}+\Delta^{\*}. Therefore, this gives a way of solving the Wasserstein constrained distributional optimization problem when δ>0\delta>0 is small.

## 4 Data-Driven Formulation and Choice of Model Parameters

In this section, we first describe the data-driven version of the DRBC formulation of the stochastic control problem since it is natural to inform the choice of the prior ℙ0\mathbb{P}\_{0} from the data, and an appropriate empirical measure is the natural candidate. Next, we provide the prescription to choose an uncertainty radius δ\delta using an asymptotically optimal (as data collected increases) approach. The idea is that this choice should also be based on observed data. We calibrate the distributional ambiguity set to the smallest size that makes the oracle-optimal portfolio (i.e., the one chosen if the true distribution were known) statistically plausible at the desired confidence level. The prescription is then obtained from an asymptotical statistical result with projecting Wasserstein distance on a nonlinear manifold.

Recall that we assume each asset follows a geometric Brownian motion with random drift:

|  |  |  |
| --- | --- | --- |
|  | d​Si​(t)Si​(t)=Bi​d​t+∑j=1dσi​j​d​Wj​(t),i=1,…,d.\frac{dS\_{i}(t)}{S\_{i}(t)}\;=\;B\_{i}\,dt\;+\;\sum\_{j=1}^{d}\sigma\_{ij}\,dW\_{j}(t),\qquad i=1,\dots,d. |  |

Therefore, we have the explicit closed-form formula

|  |  |  |
| --- | --- | --- |
|  | log⁡Si​(t)−log⁡Si​(0)=(Bi−12​‖σi⁣⋅‖2)​t+∑j=1dσi​j​Wj​(t),\log S\_{i}(t)-\log S\_{i}(0)=\Big(B\_{i}-\tfrac{1}{2}\|\sigma\_{i\cdot}\|^{2}\Big)\,t\;+\;\sum\_{j=1}^{d}\sigma\_{ij}\,W\_{j}(t), |  |

where ‖σi⁣⋅‖2:=∑j=1dσi​j2\|\sigma\_{i\cdot}\|^{2}:=\sum\_{j=1}^{d}\sigma\_{ij}^{2}.

We adopt a data-driven approximation in which the ground-truth distribution of BB is fixed, but at the beginning of the kk-th nonoverlapping window of length t~\tilde{t}, the realization B(k)B^{(k)} of return vectors is redrawn i.i.d. from such ground-truth distribution and constant during the window. Within the kk-th window, we observe prices of the stock SS on a grid 0,h,2​h,…,m​h=t~0,h,2h,\dots,mh=\tilde{t}.

Asset ii in window kk has return Bi(k)B\_{i}^{(k)}. An unbiased estimator of Bi(k)B\_{i}^{(k)} (conditional on B(k)B^{(k)}) is obtained from the endpoint log-return:

|  |  |  |
| --- | --- | --- |
|  | B^i(k)=log⁡Si(k)​(t~)−log⁡Si(k)​(0)t~+12∥σi⁣⋅∥2,𝔼[B^i(k)|B(k)]=Bi(k).\widehat{B}^{(k)}\_{i}\;=\;\frac{\log S\_{i}^{(k)}(\tilde{t})-\log S\_{i}^{(k)}(0)}{\tilde{t}}\;+\;\tfrac{1}{2}\|\sigma\_{i\cdot}\|^{2},\qquad\mathbb{E}\!\left[\widehat{B}^{(k)}\_{i}\,\middle|\,B^{(k)}\right]=B^{(k)}\_{i}. |  |

Equivalently, averaging one-step log-returns over the window yields

|  |  |  |
| --- | --- | --- |
|  | B^i(k)=1m​h​∑ℓ=0m−1log⁡(Si(k)​((ℓ+1)​h)Si(k)​(ℓ​h))+12​‖σi⁣⋅‖2.\widehat{B}^{(k)}\_{i}\;=\;\frac{1}{mh}\sum\_{\ell=0}^{m-1}\log\!\left(\frac{S\_{i}^{(k)}((\ell+1)h)}{S\_{i}^{(k)}(\ell h)}\right)\;+\;\tfrac{1}{2}\|\sigma\_{i\cdot}\|^{2}. |  |

Collecting k∈{1,…,n}k\in\{1,...,n\} windows yields i.i.d. estimates B(1),…,B(n)∈ℝdB^{(1)},\dots,B^{(n)}\in\mathbb{R}^{d}. We are abusing notation here because the estimates that we obtained are not exactly the realized B(k)B^{(k)}’s but noisy versions. Strictly speaking, we should apply a deconvolution method, which we did but the results did not change significantly and this approach is much easier to implement. The distributional robustness should absorb the noise that is still present in our estimate of B(k)B^{(k)} and in case t~\tilde{t} is hard to estimate. So, ultimately, we take the nominal prior as the empirical measure

|  |  |  |
| --- | --- | --- |
|  | ℙn​(d​x)=1n​∑k=1nδB(k)​(d​x).\mathbb{P}\_{n}(dx)\;=\;\frac{1}{n}\sum\_{k=1}^{n}\delta\_{B^{(k)}}(dx). |  |

The choice of the key parameter δ\delta is crucial. If δ\delta is too large, there is too much model ambiguity, and the available data becomes less relevant. If δ\delta is too small, the effect of robustification is negligible. Therefore, the choice of δ\delta should not be exogenously defined; rather, it should be endogenously informed by the data. Before presenting the methodology, we first present some technical assumptions. We denote k∗=𝒦​(x0)k^{\*}=\mathcal{K}(x\_{0}) as the optimal Lagrangian multiplier in Eq. ([8](https://arxiv.org/html/2512.01408v1#S2.E8 "In Theorem 1 (Karatzas–Zhao [KZ98]’s Solution). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")).

In order to choose an appropriate δ=δn\delta=\delta\_{n}, here we follow the idea behind the RWPI approach introduced in [BKW19]. Intuitively, δ\delta should be chosen such that the set 𝒰δOT​(ℙn)\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{n}) contains all the probability measures that are plausible variations of the data represented by ℙn\mathbb{P}\_{n}.
According to Theorem [1](https://arxiv.org/html/2512.01408v1#Thmtheorem1 "Theorem 1 (Karatzas–Zhao [KZ98]’s Solution). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and the assumption that the real underlying ground-truth is ℙ∗\mathbb{P}^{\*}, we have that the formula for such an optimal policy is unique with a Lagrangian multiplier k∗k^{\*} as a pre-committed strategy. We restate here (real optimal policy π∗\pi^{\*} and X∗​(T)X^{\*}(T) has one-to-one correspondence)

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ∗​[Λ^​(T)​X∗​(T)]=∫ℝdI​(k∗​e−r​T𝔼ℙ∗​[LT​(B,y)])​φT​(y)​𝑑y=x0​er​T.\mathbb{E}\_{\mathbb{P}^{\*}}\left[\hat{\Lambda}(T)X^{\*}(T)\right]=\int\_{\mathbb{R}^{d}}I\left(\frac{k^{\*}e^{-rT}}{\mathbb{E}\_{\mathbb{P}^{\*}}\left[L\_{T}(B,y)\right]}\right)\varphi\_{T}(y)dy=x\_{0}e^{rT}. |  |

We can see that the optimal policy π∗\pi^{\*} and the Lagrangian multiplier k∗k^{\*} also have a one-to-one correspondence. Thus, without loss of generality, we assume k>0k>0 is the decision variable and choose the optimal δ\delta based on whether the optimal k∗k^{\*} is covered. Similar to the notation in [BKW19], we define

|  |  |  |
| --- | --- | --- |
|  | ℱk={ℙ:∫ℝdI​(k​e−r​T𝔼ℙ​[LT​(B,y)])​φT​(y)​𝑑y=x0​er​T}.\mathcal{F}\_{k}=\left\{\mathbb{P}:\int\_{\mathbb{R}^{d}}I\left(\frac{ke^{-rT}}{\mathbb{E}\_{\mathbb{P}}\left[L\_{T}(B,y)\right]}\right)\varphi\_{T}(y)dy=x\_{0}e^{rT}\right\}. |  |

Now, for a fixed ℙ∈𝒰δOT​(ℙn)\mathbb{P}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{n}), the set {k>0:ℙ∈ℱk}\left\{k>0:\mathbb{P}\in\mathcal{F}\_{k}\right\} contains all parameter choices that are optimal from the decision maker’s point of view. This motivates the definition of the following set

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λδ​(ℙn)\displaystyle\Lambda\_{\delta}(\mathbb{P}\_{n}) | ={k>0:ℱk∩𝒰δOT​(ℙn)≠∅}\displaystyle=\left\{k>0:\mathcal{F}\_{k}\cap\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{n})\neq\varnothing\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ={k>0:there exists ​ℙ∈𝒰δOT​(ℙn)​ such that ​∫ℝdI​(k​e−r​T𝔼ℙ​[LT​(B,y)])​φT​(y)​𝑑y=x0​er​T},\displaystyle=\left\{k>0:\text{there exists }\mathbb{P}\in\mathcal{U}^{\text{OT}}\_{\delta}(\mathbb{P}\_{n})\text{ such that }\int\_{\mathbb{R}^{d}}I\left(\frac{ke^{-rT}}{\mathbb{E}\_{\mathbb{P}}\left[L\_{T}(B,y)\right]}\right)\varphi\_{T}(y)dy=x\_{0}e^{rT}\right\}, |  |

which corresponds to all the plausible estimates of k∗k^{\*}. Thus, it includes all the parameter choices that are collected by the decision maker as optimal for some distribution in the uncertainty set. As a result, Λδ​(ℙn)\Lambda\_{\delta}(\mathbb{P}\_{n}) is a natural confidence region for k∗k^{\*}. Therefore, δ>0\delta>0 should be chosen as the smallest δn∗\delta^{\*}\_{n} such that k∗k^{\*} belongs to this region with a given confidence interval. Namely,

|  |  |  |
| --- | --- | --- |
|  | δn∗=min⁡{δ>0:ℙ∗​(k∗∈Λδ​(ℙn))≥1−δ0},\delta^{\*}\_{n}=\min\left\{\delta>0:\mathbb{P}^{\*}\left(k^{\*}\in\Lambda\_{\delta}(\mathbb{P}\_{n})\right)\geq 1-\delta\_{0}\right\}, |  |

where δ0\delta\_{0} is the user-defined confidence level (typically δ0=0.05\delta\_{0}=0.05).

However, by the mere definition, it is hard to compute δn∗\delta^{\*}\_{n}. We now provide a simpler representation for δn∗\delta^{\*}\_{n} via an auxiliary function called the robust Wasserstein profile (RWP) function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rn​(k)\displaystyle R\_{n}(k) | :=infℙ∈ℱkDc​(ℙ,ℙn)\displaystyle:=\inf\_{\mathbb{P}\in\mathcal{F}\_{k}}D\_{c}(\mathbb{P},\mathbb{P}\_{n}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =inf{Dc​(ℙ,ℙn):∫ℝdI​(k​e−r​T𝔼ℙ​[LT​(B,y)])​φT​(y)​𝑑y=x0​er​T}.\displaystyle=\inf\left\{D\_{c}(\mathbb{P},\mathbb{P}\_{n}):\int\_{\mathbb{R}^{d}}I\left(\frac{ke^{-rT}}{\mathbb{E}\_{\mathbb{P}}\left[L\_{T}(B,y)\right]}\right)\varphi\_{T}(y)dy=x\_{0}e^{rT}\right\}. |  |

Compared with the linear projection in [BKW19], here the RWP function is defined as a projection of the empirical measure to a nonlinear manifold, so the behavior of the nonlinear RWP function is much complicated.

In the following theorem, we derive the nonlinear projection asymptotics with great generality, and the specific choice of the uncertainty radius can be obtained by a corollary.

###### Theorem 4 (Non-linear projection asymptotics).

Let ν\nu be a probability measure on ℝd\mathbb{R}^{d}, and let
κ:𝒫2​(ℝd)→ℝ\kappa:\mathcal{P}\_{2}(\mathbb{R}^{d})\to\mathbb{R} be a functional with κ​(ν)=0\kappa(\nu)=0.
Assume that κ\kappa admits a first variation κμ′:ℝd→ℝ\kappa^{\prime}\_{\mu}:\mathbb{R}^{d}\to\mathbb{R}
such that:

* •

  For any probability measure μ\mu and any coupling
  (X′,X)∼(μ,ν)(X^{\prime},X)\sim(\mu,\nu), with the linear interpolation
  νt:=(1−t)​ν+t​μ\nu\_{t}:=(1-t)\nu+t\mu, we have

  |  |  |  |
  | --- | --- | --- |
  |  | κ​(μ)−κ​(ν)=∫01𝔼​[κνt′​(X′)−κνt′​(X)]​𝑑t.\kappa(\mu)-\kappa(\nu)=\int\_{0}^{1}\mathbb{E}\!\left[\kappa^{\prime}\_{\nu\_{t}}(X^{\prime})-\kappa^{\prime}\_{\nu\_{t}}(X)\right]\,dt. |  |
* •

  For μ\mu in a neighborhood of ν\nu, the map
  x↦κμ′​(x)x\mapsto\kappa^{\prime}\_{\mu}(x) is C1C^{1}, and its gradient
  gμ​(x):=∇xκμ′​(x)g\_{\mu}(x):=\nabla\_{x}\kappa^{\prime}\_{\mu}(x) is jointly continuous
  in (μ,x)(\mu,x) near (ν,⋅)(\nu,\cdot). Moreover, there exists
  an envelope G∈L2​(ν)G\in L^{2}(\nu) such that

  |  |  |  |
  | --- | --- | --- |
  |  | ‖gμ​(x)‖2≤G​(x)for all μ in a neighborhood of ν and all ​x∈ℝd,\|g\_{\mu}(x)\|\_{2}\leq G(x)\quad\text{for all $\mu$ in a neighborhood of $\nu$ and all }x\in\mathbb{R}^{d}, |  |

  and

  |  |  |  |
  | --- | --- | --- |
  |  | gν∈L2​(ν;ℝd),‖gν‖L2​(ν)>0.g\_{\nu}\in L^{2}(\nu;\mathbb{R}^{d}),\qquad\|g\_{\nu}\|\_{L^{2}(\nu)}>0. |  |

Let c:ℝd×ℝd→[0,∞]c:\mathbb{R}^{d}\times\mathbb{R}^{d}\to[0,\infty] be a transport cost satisfying:

* (i)

  There exist τ>0\tau>0, r0>0r\_{0}>0
  and a function η:(0,r0]→[0,∞)\eta:(0,r\_{0}]\to[0,\infty) with η​(r)→0\eta(r)\to 0 as r→0r\to 0 such that

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | |c​(x,y)−τ​‖x−y‖22|≤η​(‖x−y‖2)​‖x−y‖22whenever ​‖x−y‖2≤r0.\bigl|c(x,y)-\tau\|x-y\|\_{2}^{2}\bigr|\;\leq\;\eta(\|x-y\|\_{2})\,\|x-y\|\_{2}^{2}\qquad\text{whenever }\|x-y\|\_{2}\leq r\_{0}. |  | (29) |
* (ii)

  There exist constants C1>0C\_{1}>0, C2≥0C\_{2}\geq 0, R>0R>0
  such that

  |  |  |  |
  | --- | --- | --- |
  |  | c​(x,y)≥C1​‖x−y‖22−C2whenever ​‖x−y‖2≥R.c(x,y)\;\geq\;C\_{1}\|x-y\|\_{2}^{2}-C\_{2}\qquad\text{whenever }\|x-y\|\_{2}\geq R. |  |

Let

|  |  |  |
| --- | --- | --- |
|  | Dc​(ν,μ):=infπ∈Π​(ν,μ)∫ℝd×ℝdc​(x,y)​π​(d​x,d​y)D\_{c}(\nu,\mu):=\inf\_{\pi\in\Pi(\nu,\mu)}\int\_{\mathbb{R}^{d}\times\mathbb{R}^{d}}c(x,y)\,\pi(dx,dy) |  |

denote the optimal transport divergence induced by cc. For zz in a neighborhood
of 0, define the projection cost

|  |  |  |
| --- | --- | --- |
|  | R​(z):=infμ:κ​(μ)=zDc​(ν,μ).R(z):=\inf\_{\mu:\kappa(\mu)=z}D\_{c}(\nu,\mu). |  |

Then, as z→0z\to 0,

|  |  |  |
| --- | --- | --- |
|  | R​(z)=τ​z2𝔼ν​[‖gν​(X)‖22]+o​(z2)=τ​z2𝔼ν​[‖∇κν′​(X)‖22]+o​(z2).R(z)=\frac{\tau z^{2}}{\mathbb{E}\_{\nu}[\|g\_{\nu}(X)\|\_{2}^{2}]}+o(z^{2})=\frac{\tau z^{2}}{\mathbb{E}\_{\nu}[\|\nabla\kappa^{\prime}\_{\nu}(X)\|\_{2}^{2}]}+o(z^{2}). |  |

Moreover, there exists an asymptotically optimal Monge-type perturbation
of the form

|  |  |  |
| --- | --- | --- |
|  | Tz​(x)=x+Δz​(x),Δz​(x)=z𝔼ν​[‖gν​(X)‖22]​gν​(x)+o​(z)in ​L2​(ν),T\_{z}(x)=x+\Delta\_{z}(x),\qquad\Delta\_{z}(x)=\frac{z}{\mathbb{E}\_{\nu}[\|g\_{\nu}(X)\|\_{2}^{2}]}\,g\_{\nu}(x)+o(z)\quad\text{in }L^{2}(\nu), |  |

which satisfies κ​(Tz​#​ν)=z+o​(z)\kappa(T\_{z\#}\nu)=z+o(z) and attains the above
cost up to o​(z2)o(z^{2}).

###### Proof.

Fix ν\nu with κ​(ν)=0\kappa(\nu)=0. For zz small, we seek μ\mu such that
κ​(μ)=z\kappa(\mu)=z and Dc​(ν,μ)D\_{c}(\nu,\mu) is minimal.

Step 1: Linearization of the constraint.
By the assumptions on the first variation and the regularity of
κμ′\kappa^{\prime}\_{\mu}, one obtains that κ\kappa is W2W\_{2}–differentiable
at ν\nu with derivative gνg\_{\nu}. In particular, for any small
Δ∈L2​(ν)\Delta\in L^{2}(\nu), letting μ=(I+Δ)#​ν\mu=(I+\Delta)\_{\#}\nu,

|  |  |  |
| --- | --- | --- |
|  | κ​(μ)−κ​(ν)=𝔼ν​[⟨gν​(X),Δ​(X)⟩]+o​(‖Δ‖L2​(ν)).\kappa(\mu)-\kappa(\nu)=\mathbb{E}\_{\nu}\!\left[\langle g\_{\nu}(X),\Delta(X)\rangle\right]+o\bigl(\|\Delta\|\_{L^{2}(\nu)}\bigr). |  |

Imposing the constraint κ​(μ)=z\kappa(\mu)=z and recalling κ​(ν)=0\kappa(\nu)=0, we
obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ν​[⟨gν​(X),Δ​(X)⟩]=z+o​(‖Δ‖L2​(ν)).\mathbb{E}\_{\nu}\!\left[\langle g\_{\nu}(X),\Delta(X)\rangle\right]=z+o\bigl(\|\Delta\|\_{L^{2}(\nu)}\bigr). |  | (30) |

In particular, any admissible perturbation satisfies
‖Δ‖L2​(ν)=O​(|z|)\|\Delta\|\_{L^{2}(\nu)}=O(|z|) as z→0z\to 0.

Step 2: Quadratic approximation of the cost.
For μ=(I+Δ)#​ν\mu=(I+\Delta)\_{\#}\nu, consider the coupling
(X′,X)=(X+Δ​(X),X)(X^{\prime},X)=(X+\Delta(X),X) with X∼νX\sim\nu. Then

|  |  |  |
| --- | --- | --- |
|  | Dc​(ν,μ)≤𝔼ν​[c​(X,X+Δ​(X))].D\_{c}(\nu,\mu)\leq\mathbb{E}\_{\nu}\!\big[c\big(X,X+\Delta(X)\big)\big]. |  |

By the uniform local expansion ([29](https://arxiv.org/html/2512.01408v1#S4.E29 "In item (i) ‣ Theorem 4 (Non-linear projection asymptotics). ‣ 4 Data-Driven Formulation and Choice of Model Parameters ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")),

|  |  |  |
| --- | --- | --- |
|  | c​(X,X+Δ​(X))=τ​‖Δ​(X)‖22+r​(Δ​(X)),c\big(X,X+\Delta(X)\big)=\tau\|\Delta(X)\|\_{2}^{2}+r(\Delta(X)), |  |

where

|  |  |  |
| --- | --- | --- |
|  | |r​(h)|≤η​(‖h‖2)​‖h‖22,η​(r)→0​ as ​r→0.|r(h)|\leq\eta(\|h\|\_{2})\,\|h\|\_{2}^{2},\qquad\eta(r)\to 0\text{ as }r\to 0. |  |

Since ‖Δ‖L2​(ν)=O​(|z|)\|\Delta\|\_{L^{2}(\nu)}=O(|z|), we have
𝔼ν​[‖Δ​(X)‖22]=O​(z2)\mathbb{E}\_{\nu}[\|\Delta(X)\|\_{2}^{2}]=O(z^{2}) and ‖Δ​(X)‖→0\|\Delta(X)\|\to 0 in probability.
Using the uniform bound, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝔼ν​[|r​(Δ​(X))|]≤(sup‖h‖≤r0η​(‖h‖))​𝔼ν​‖Δ​(X)‖22=o​(𝔼ν​‖Δ​(X)‖22)=o​(z2).\mathbb{E}\_{\nu}[\,|r(\Delta(X))|\,]\;\leq\;\left(\sup\_{\|h\|\leq r\_{0}}\eta(\|h\|)\right)\mathbb{E}\_{\nu}\|\Delta(X)\|\_{2}^{2}=o\bigl(\mathbb{E}\_{\nu}\|\Delta(X)\|\_{2}^{2}\bigr)=o(z^{2}). |  |

Thus

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dc​(ν,μ)≤τ​𝔼ν​‖Δ​(X)‖22+o​(z2).D\_{c}(\nu,\mu)\leq\tau\,\mathbb{E}\_{\nu}\|\Delta(X)\|\_{2}^{2}+o(z^{2}). |  | (31) |

Next, we prove the lower bound.
Let μ\mu satisfy κ​(μ)=z\kappa(\mu)=z, and let π\pi be an optimal coupling
between ν\nu and μ\mu, with (X,Y)∼π(X,Y)\sim\pi and displacement D:=Y−XD:=Y-X.
By the first-variation representation and the envelope bound on gμg\_{\mu},

|  |  |  |
| --- | --- | --- |
|  | z=𝔼π​[⟨gν​(X),D⟩]+o​(‖D‖L2​(π)).z=\mathbb{E}\_{\pi}\!\left[\langle g\_{\nu}(X),D\rangle\right]+o\bigl(\|D\|\_{L^{2}(\pi)}\bigr). |  |

Hence ‖D‖L2​(π)=O​(|z|)\|D\|\_{L^{2}(\pi)}=O(|z|).

By the local expansion ([29](https://arxiv.org/html/2512.01408v1#S4.E29 "In item (i) ‣ Theorem 4 (Non-linear projection asymptotics). ‣ 4 Data-Driven Formulation and Choice of Model Parameters ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")), for ‖D‖≤r0\|D\|\leq r\_{0},

|  |  |  |
| --- | --- | --- |
|  | c​(X,Y)=τ​‖D‖22+r​(D),|r​(D)|≤η​(‖D‖)​‖D‖22,c(X,Y)=\tau\|D\|\_{2}^{2}+r(D),\qquad|r(D)|\leq\eta(\|D\|)\|D\|\_{2}^{2}, |  |

while for ‖D‖>r0\|D\|>r\_{0}, the quadratic coercivity (ii) yields

|  |  |  |
| --- | --- | --- |
|  | c​(X,Y)≥C1​‖D‖22−C2.c(X,Y)\;\geq\;C\_{1}\|D\|\_{2}^{2}-C\_{2}. |  |

As ‖D‖L2=O​(|z|)\|D\|\_{L^{2}}=O(|z|), the region {‖D‖>r0}\{\|D\|>r\_{0}\} has probability
O​(z2)O(z^{2}) by Markov’s inequality. Combining these bounds,

|  |  |  |
| --- | --- | --- |
|  | Dc​(ν,μ)=𝔼π​[c​(X,Y)]≥τ​𝔼π​‖D‖22−o​(𝔼π​‖D‖22)=τ​𝔼π​‖D‖22+o​(z2).D\_{c}(\nu,\mu)=\mathbb{E}\_{\pi}[c(X,Y)]\;\geq\;\tau\,\mathbb{E}\_{\pi}\|D\|\_{2}^{2}-o\!\bigl(\mathbb{E}\_{\pi}\|D\|\_{2}^{2}\bigr)=\tau\,\mathbb{E}\_{\pi}\|D\|\_{2}^{2}+o(z^{2}). |  |

Next define the conditional mean displacement
Δ​(x):=𝔼​[D∣X=x]\Delta(x):=\mathbb{E}[D\mid X=x]. Then

|  |  |  |
| --- | --- | --- |
|  | 𝔼π​⟨gν​(X),D⟩=𝔼ν​⟨gν​(X),Δ​(X)⟩,𝔼π​‖D‖22≥𝔼ν​‖Δ​(X)‖22.\mathbb{E}\_{\pi}\langle g\_{\nu}(X),D\rangle=\mathbb{E}\_{\nu}\langle g\_{\nu}(X),\Delta(X)\rangle,\qquad\mathbb{E}\_{\pi}\|D\|\_{2}^{2}\;\geq\;\mathbb{E}\_{\nu}\|\Delta(X)\|\_{2}^{2}. |  |

Thus every admissible μ\mu induces a perturbation
Δ∈L2​(ν)\Delta\in L^{2}(\nu) with

|  |  |  |
| --- | --- | --- |
|  | 𝔼ν​⟨gν​(X),Δ​(X)⟩=z+o​(z),Dc​(ν,μ)≥τ​𝔼ν​‖Δ​(X)‖22+o​(z2).\mathbb{E}\_{\nu}\langle g\_{\nu}(X),\Delta(X)\rangle=z+o(z),\qquad D\_{c}(\nu,\mu)\geq\tau\,\mathbb{E}\_{\nu}\|\Delta(X)\|\_{2}^{2}+o(z^{2}). |  |

Hence we conclude that
for admissible μ\mu,

|  |  |  |
| --- | --- | --- |
|  | Dc​(ν,μ)=τ​𝔼ν​‖Δ​(X)‖22+o​(z2).D\_{c}(\nu,\mu)=\tau\,\mathbb{E}\_{\nu}\|\Delta(X)\|\_{2}^{2}+o(z^{2}). |  |

Step 3: Solving the quadratic optimization problem.
The leading-order problem is therefore

|  |  |  |
| --- | --- | --- |
|  | infΔ∈L2​(ν;ℝd){τ𝔼ν[∥Δ(X)∥22]:𝔼ν[⟨gν(X),Δ(X)⟩]=z},\inf\_{\Delta\in L^{2}(\nu;\mathbb{R}^{d})}\Bigl\{\tau\,\mathbb{E}\_{\nu}[\|\Delta(X)\|\_{2}^{2}]:\mathbb{E}\_{\nu}[\langle g\_{\nu}(X),\Delta(X)\rangle]=z\Bigr\}, |  |

where we may ignore the o​(‖Δ‖L2)o(\|\Delta\|\_{L^{2}}) term in
([30](https://arxiv.org/html/2512.01408v1#S4.E30 "In 4 Data-Driven Formulation and Choice of Model Parameters ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) at order z2z^{2}. This is a convex quadratic
optimization with a single linear constraint in the Hilbert space
L2​(ν;ℝd)L^{2}(\nu;\mathbb{R}^{d}). The Lagrangian is

|  |  |  |
| --- | --- | --- |
|  | ℒ​(Δ,λ)=τ​𝔼ν​[‖Δ​(X)‖22]+λ​(z−𝔼ν​[⟨gν​(X),Δ​(X)⟩]).\mathcal{L}(\Delta,\lambda)=\tau\,\mathbb{E}\_{\nu}[\|\Delta(X)\|\_{2}^{2}]+\lambda\Bigl(z-\mathbb{E}\_{\nu}[\langle g\_{\nu}(X),\Delta(X)\rangle]\Bigr). |  |

Taking the variational derivative with respect to Δ\Delta and setting
it to zero gives, for ν\nu-a.e. xx,

|  |  |  |
| --- | --- | --- |
|  | 2​τ​Δ​(x)−λ​gν​(x)=0⟹Δ​(x)=λ2​τ​gν​(x).2\tau\,\Delta(x)-\lambda g\_{\nu}(x)=0\quad\Longrightarrow\quad\Delta(x)=\frac{\lambda}{2\tau}\,g\_{\nu}(x). |  |

Substituting into the constraint,

|  |  |  |
| --- | --- | --- |
|  | 𝔼ν​[⟨gν​(X),λ2​τ​gν​(X)⟩]=λ2​τ​𝔼ν​[‖gν​(X)‖22]=z,\mathbb{E}\_{\nu}\!\left[\Big\langle g\_{\nu}(X),\frac{\lambda}{2\tau}g\_{\nu}(X)\Big\rangle\right]=\frac{\lambda}{2\tau}\mathbb{E}\_{\nu}[\|g\_{\nu}(X)\|\_{2}^{2}]=z, |  |

so

|  |  |  |
| --- | --- | --- |
|  | λ=2​τ​z𝔼ν​[‖gν​(X)‖22].\lambda=\frac{2\tau z}{\mathbb{E}\_{\nu}[\|g\_{\nu}(X)\|\_{2}^{2}]}. |  |

Thus the optimal perturbation at leading order is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δz​(x)=λ2​τ​gν​(x)=z𝔼ν​[‖gν​(X)‖22]​gν​(x).\Delta\_{z}(x)=\frac{\lambda}{2\tau}\,g\_{\nu}(x)=\frac{z}{\mathbb{E}\_{\nu}[\|g\_{\nu}(X)\|\_{2}^{2}]}\,g\_{\nu}(x). |  | (32) |

Clearly ‖Δz‖L2​(ν)=O​(|z|)\|\Delta\_{z}\|\_{L^{2}(\nu)}=O(|z|), so the linearization error in
([30](https://arxiv.org/html/2512.01408v1#S4.E30 "In 4 Data-Driven Formulation and Choice of Model Parameters ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) is o​(|z|)o(|z|), and
κ​((I+Δz)#​ν)=z+o​(z)\kappa((I+\Delta\_{z})\_{\#}\nu)=z+o(z).

Step 4: Computing the minimal cost.
Plugging ([32](https://arxiv.org/html/2512.01408v1#S4.E32 "In 4 Data-Driven Formulation and Choice of Model Parameters ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) into the quadratic cost term,

|  |  |  |
| --- | --- | --- |
|  | 𝔼ν​[‖Δz​(X)‖22]=z2(𝔼ν​[‖gν​(X)‖22])2​𝔼ν​[‖gν​(X)‖22]=z2𝔼ν​[‖gν​(X)‖22].\mathbb{E}\_{\nu}[\|\Delta\_{z}(X)\|\_{2}^{2}]=\frac{z^{2}}{\bigl(\mathbb{E}\_{\nu}[\|g\_{\nu}(X)\|\_{2}^{2}]\bigr)^{2}}\mathbb{E}\_{\nu}[\|g\_{\nu}(X)\|\_{2}^{2}]=\frac{z^{2}}{\mathbb{E}\_{\nu}[\|g\_{\nu}(X)\|\_{2}^{2}]}. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | R​(z)=τ​𝔼ν​[‖Δz​(X)‖22]+o​(z2)=τ​z2𝔼ν​[‖gν​(X)‖22]+o​(z2),R(z)=\tau\,\mathbb{E}\_{\nu}[\|\Delta\_{z}(X)\|\_{2}^{2}]+o(z^{2})=\frac{\tau z^{2}}{\mathbb{E}\_{\nu}[\|g\_{\nu}(X)\|\_{2}^{2}]}+o(z^{2}), |  |

which is the desired expansion. The Monge map Tz​(x)=x+Δz​(x)T\_{z}(x)=x+\Delta\_{z}(x)
is asymptotically optimal and satisfies κ​(Tz​#​ν)=z+o​(z)\kappa(T\_{z\#}\nu)=z+o(z),
as claimed.
∎

In the following corollary, we provide an asymptotic result n​Rn​(k∗)⇒ΥnR\_{n}(k^{\*})\Rightarrow\Upsilon, so that

|  |  |  |
| --- | --- | --- |
|  | limn→∞ℙ∗​(Rn​(k∗)≤η1−δ0n)=limn→∞ℙ∗​(n​Rn​(k∗)≤η1−δ0)=ℙ∗​(Υ≤η1−δ0)=1−δ0,\lim\_{n\to\infty}\mathbb{P}^{\*}\left(R\_{n}(k^{\*})\leq\frac{\eta\_{1-\delta\_{0}}}{n}\right)=\lim\_{n\to\infty}\mathbb{P}^{\*}\left(nR\_{n}(k^{\*})\leq\eta\_{1-\delta\_{0}}\right)=\mathbb{P}^{\*}\left(\Upsilon\leq\eta\_{1-\delta\_{0}}\right)=1-\delta\_{0}, |  |

where we define η1−δ0\eta\_{1-\delta\_{0}} is the (1−δ0)(1-\delta\_{0})-quantile of Υ\Upsilon.

###### Corollary 2.

Suppose Assumption [1](https://arxiv.org/html/2512.01408v1#Thmassumption1 "Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and [2](https://arxiv.org/html/2512.01408v1#Thmassumption2 "Assumption 2 (Compact Support for 𝐵). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") hold. Define the RWP function for the Merton budget constraint as

|  |  |  |
| --- | --- | --- |
|  | Rn​(k)=inf{Dc​(ℙn,ℙ):∫ℝdI​(k​e−r​T𝔼ℙ​[LT​(B,y)])​φT​(y)​𝑑y=x0​er​T}.R\_{n}(k)=\inf\left\{D\_{c}(\mathbb{P}\_{n},\mathbb{P}):\int\_{\mathbb{R}^{d}}I\left(\frac{ke^{-rT}}{\mathbb{E}\_{\mathbb{P}}[L\_{T}(B,y)]}\right)\varphi\_{T}(y)dy=x\_{0}e^{rT}\right\}. |  |

Then with the cost function c​(x,y)=‖x−y‖22c(x,y)=||x-y||\_{2}^{2},

|  |  |  |
| --- | --- | --- |
|  | n​Rn​(k∗)⇒Υ,as ​n→∞,nR\_{n}(k^{\*})\Rightarrow\Upsilon,\quad\text{as }n\to\infty, |  |

where Υ\Upsilon is a non-negative random variable given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Υ=Z2𝔼ℙ∗​[‖∇κℙ∗′​(B)‖22],\Upsilon=\frac{Z^{2}}{\mathbb{E}\_{\mathbb{P}^{\*}}[\|\nabla\kappa^{\prime}\_{\mathbb{P}^{\*}}(B)\|\_{2}^{2}]}, |  | (33) |

with Z∼𝒩​(0,σ2)Z\sim\mathcal{N}(0,\sigma^{2}) and

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2=Varℙ∗​(∫ℝdg′​(F​(y))​LT​(B,y)​φT​(y)​𝑑y),\sigma^{2}=\text{Var}\_{\mathbb{P}^{\*}}\left(\int\_{\mathbb{R}^{d}}g^{\prime}(F(y))L\_{T}(B,y)\varphi\_{T}(y)dy\right), |  | (34) |

where F​(y)=𝔼ℙ∗​[LT​(B,y)]F(y)=\mathbb{E}\_{\mathbb{P}^{\*}}[L\_{T}(B,y)],

|  |  |  |
| --- | --- | --- |
|  | g′​(F)=−I′​(k∗​e−r​TF)​k∗​e−r​TF2,g^{\prime}(F)=-I^{\prime}\!\left(\frac{k^{\*}e^{-rT}}{F}\right)\frac{k^{\*}e^{-rT}}{F^{2}}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ∇κℙ∗′​(b)=−∫ℝdI′​(k∗​e−r​TF​(y))⋅k∗​e−r​TF​(y)2⋅∇bLT​(b,y)​φT​(y)​𝑑y.\nabla\kappa^{\prime}\_{\mathbb{P}^{\*}}(b)=-\int\_{\mathbb{R}^{d}}I^{\prime}\left(\frac{k^{\*}e^{-rT}}{F(y)}\right)\cdot\frac{k^{\*}e^{-rT}}{F(y)^{2}}\cdot\nabla\_{b}L\_{T}(b,y)\varphi\_{T}(y)dy. |  |

###### Proof.

We apply Theorem [4](https://arxiv.org/html/2512.01408v1#Thmtheorem4 "Theorem 4 (Non-linear projection asymptotics). ‣ 4 Data-Driven Formulation and Choice of Model Parameters ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") to the DRBC Merton setting.
Recall

|  |  |  |
| --- | --- | --- |
|  | κk​(ℙ)=∫ℝdI​(k​e−r​T𝔼ℙ​[LT​(B,y)])​φT​(y)​𝑑y−x0​er​T,ℱk={ℙ:κk​(ℙ)=0},\kappa\_{k}(\mathbb{P})=\int\_{\mathbb{R}^{d}}I\!\left(\frac{ke^{-rT}}{\mathbb{E}\_{\mathbb{P}}[L\_{T}(B,y)]}\right)\varphi\_{T}(y)\,dy-x\_{0}e^{rT},\qquad\mathcal{F}\_{k}=\{\mathbb{P}:\kappa\_{k}(\mathbb{P})=0\}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | Rn​(k)=inf{Dc​(ℙn,ℙ):ℙ∈ℱk}.R\_{n}(k)=\inf\{D\_{c}(\mathbb{P}\_{n},\mathbb{P}):\mathbb{P}\in\mathcal{F}\_{k}\}. |  |

Let ℙ∗\mathbb{P}^{\*} be the true model and k∗k^{\*} the associated multiplier with
κk∗​(ℙ∗)=0\kappa\_{k^{\*}}(\mathbb{P}^{\*})=0.

Step 1: Wasserstein derivative of κk∗\kappa\_{k^{\*}}.
As in Corollary 1, consider ℙϵ=(1−ϵ)​ℙ∗+ϵ​δb\mathbb{P}^{\epsilon}=(1-\epsilon)\mathbb{P}^{\*}+\epsilon\delta\_{b} and write
F​(y)=𝔼ℙ∗​[LT​(B,y)]F(y)=\mathbb{E}\_{\mathbb{P}^{\*}}[L\_{T}(B,y)].
Differentiating under the integral (justified by Assumptions [1](https://arxiv.org/html/2512.01408v1#Thmassumption1 "Assumption 1 (Utility Function; refinement of Assumption 3.1 of [KZ98]). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")–[2](https://arxiv.org/html/2512.01408v1#Thmassumption2 "Assumption 2 (Compact Support for 𝐵). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) yields

|  |  |  |
| --- | --- | --- |
|  | δ​κk∗δ​ℙ∗​(b)=−∫ℝdI′​(k∗​e−r​TF​(y))​k∗​e−r​TF​(y)2​LT​(b,y)​φT​(y)​𝑑y,\frac{\delta\kappa\_{k^{\*}}}{\delta\mathbb{P}^{\*}}(b)=-\int\_{\mathbb{R}^{d}}I^{\prime}\!\left(\frac{k^{\*}e^{-rT}}{F(y)}\right)\frac{k^{\*}e^{-rT}}{F(y)^{2}}L\_{T}(b,y)\,\varphi\_{T}(y)\,dy, |  |

and therefore the Wasserstein gradient is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇κℙ∗′​(b)=−∫ℝdI′​(k∗​e−r​TF​(y))​k∗​e−r​TF​(y)2​∇bLT​(b,y)​φT​(y)​𝑑y.\nabla\kappa^{\prime}\_{\mathbb{P}^{\*}}(b)=-\int\_{\mathbb{R}^{d}}I^{\prime}\!\left(\frac{k^{\*}e^{-rT}}{F(y)}\right)\frac{k^{\*}e^{-rT}}{F(y)^{2}}\,\nabla\_{b}L\_{T}(b,y)\,\varphi\_{T}(y)\,dy. |  | (35) |

Step 2: Linearization and CLT for κk∗​(ℙn)\kappa\_{k^{\*}}(\mathbb{P}\_{n}).
Since ℙ↦κk∗​(ℙ)\mathbb{P}\mapsto\kappa\_{k^{\*}}(\mathbb{P}) is Wasserstein differentiable at ℙ∗\mathbb{P}^{\*}, the
functional delta method gives

|  |  |  |
| --- | --- | --- |
|  | n​(κk∗​(ℙn)−κk∗​(ℙ∗))=1n​∑i=1nδ​κk∗δ​ℙ∗​(B(i))+oP​(1)⇒Z,\sqrt{n}\big(\kappa\_{k^{\*}}(\mathbb{P}\_{n})-\kappa\_{k^{\*}}(\mathbb{P}^{\*})\big)=\frac{1}{\sqrt{n}}\sum\_{i=1}^{n}\frac{\delta\kappa\_{k^{\*}}}{\delta\mathbb{P}^{\*}}(B^{(i)})+o\_{P}(1)\Rightarrow Z, |  |

where Z∼𝒩​(0,σ2)Z\sim\mathcal{N}(0,\sigma^{2}) with

|  |  |  |
| --- | --- | --- |
|  | σ2=Varℙ∗​(∫ℝdg′​(F​(y))​LT​(B,y)​φT​(y)​𝑑y),g′​(F)=−I′​(k∗​e−r​TF)​k∗​e−r​TF2.\sigma^{2}=\text{Var}\_{\mathbb{P}^{\*}}\!\left(\int\_{\mathbb{R}^{d}}g^{\prime}(F(y))\,L\_{T}(B,y)\,\varphi\_{T}(y)\,dy\right),\qquad g^{\prime}(F)=-I^{\prime}\!\left(\frac{k^{\*}e^{-rT}}{F}\right)\frac{k^{\*}e^{-rT}}{F^{2}}. |  |

Write

|  |  |  |
| --- | --- | --- |
|  | zn:=κk∗​(ℙn)=Zn+oP​(1/n).z\_{n}:=\kappa\_{k^{\*}}(\mathbb{P}\_{n})=\frac{Z}{\sqrt{n}}+o\_{P}(1/\sqrt{n}). |  |

Step 3: Application of the local projection law.
Theorem [4](https://arxiv.org/html/2512.01408v1#Thmtheorem4 "Theorem 4 (Non-linear projection asymptotics). ‣ 4 Data-Driven Formulation and Choice of Model Parameters ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") gives, for any ν\nu near ℙ∗\mathbb{P}^{\*} with κk∗​(ν)=z\kappa\_{k^{\*}}(\nu)=z,

|  |  |  |
| --- | --- | --- |
|  | R​(z)=z2𝔼ℙ∗​[‖∇κℙ∗′​(B)‖22]+o​(z2).R(z)=\frac{z^{2}}{\mathbb{E}\_{\mathbb{P}^{\*}}\!\big[\|\nabla\kappa^{\prime}\_{\mathbb{P}^{\*}}(B)\|\_{2}^{2}\big]}+o(z^{2}). |  |

Taking ν=ℙn\nu=\mathbb{P}\_{n} and substituting znz\_{n},

|  |  |  |
| --- | --- | --- |
|  | n​Rn​(k∗)=n​R​(zn)=Z2𝔼ℙ∗​[‖∇κℙ∗′​(B)‖22]+oP​(1),nR\_{n}(k^{\*})=nR(z\_{n})=\frac{Z^{2}}{\mathbb{E}\_{\mathbb{P}^{\*}}\!\big[\|\nabla\kappa^{\prime}\_{\mathbb{P}^{\*}}(B)\|\_{2}^{2}\big]}+o\_{P}(1), |  |

hence

|  |  |  |
| --- | --- | --- |
|  | n​Rn​(k∗)⇒Υ:=Z2𝔼ℙ∗​[‖∇κℙ∗′​(B)‖22].nR\_{n}(k^{\*})\Rightarrow\Upsilon:=\frac{Z^{2}}{\mathbb{E}\_{\mathbb{P}^{\*}}\!\big[\|\nabla\kappa^{\prime}\_{\mathbb{P}^{\*}}(B)\|\_{2}^{2}\big]}. |  |

Since Z2Z^{2} is a scaled χ12\chi^{2}\_{1} variable, Υ\Upsilon is nonnegative.
This completes the proof.
∎

Based on the above discussion, we can give the following recipe for computing the optimal DRBC policies with Wasserstein uncertainty set with choosing the optimal δ\delta based on the data (for a certain time window). This can be viewed as a nonlinear extension of the RWPI method (e.g. see [BlanchetChenZhou2021, Blanchet2021WassersteinDRO]).

* •

  (1) Collect return data {B(i)}i=1,…​n\{B^{(i)}\}\_{i=1,\ldots n}.
* •

  (2) Use the collected data {B(i)}i=1,…​n\{B^{(i)}\}\_{i=1,\ldots n} to solve the equation ∫ℝdI​(k​e−r​T𝔼ℙn​[LT​(B,y)])​φT​(y)​𝑑y=x0​er​T\int\_{\mathbb{R}^{d}}I\left(\frac{ke^{-rT}}{\mathbb{E}\_{\mathbb{P}\_{n}}\left[L\_{T}(B,y)\right]}\right)\varphi\_{T}(y)dy=x\_{0}e^{rT} (this corresponds to estimating 𝒦​(x0)\mathcal{K}(x\_{0})). Denote the solution as k^\hat{k}.
* •

  (3) Obtain independent samples Y1,…,YNY\_{1},\ldots,Y\_{N} from 𝒩​(0,T​Id)\mathcal{N}(0,TI\_{d}). Compute F^​(Yi)=𝔼ℙn​[LT​(B,Yi)]\hat{F}(Y\_{i})=\mathbb{E}\_{\mathbb{P}\_{n}}[L\_{T}(B,Y\_{i})] for each sample using the collected data {B(i)}i=1,…​n\{B^{(i)}\}\_{i=1,\ldots n}, and then compute 𝔼ℙn​[‖∇κℙ∗′​(B)‖22]\mathbb{E}\_{\mathbb{P}\_{n}}[\|\nabla\kappa^{\prime}\_{\mathbb{P}^{\*}}(B)\|\_{2}^{2}] as an estimate of the denominator of Υ,\Upsilon, where ∇κℙ∗′​(b)\nabla\kappa^{\prime}\_{\mathbb{P}^{\*}}(b) is computed by Monte Carlo method with F^​(Yi)\hat{F}(Y\_{i}), LT​(b,Yi)L\_{T}(b,Y\_{i}), and k^\hat{k} derived in Step (2).
* •

  (4): Estimate ([34](https://arxiv.org/html/2512.01408v1#S4.E34 "In Corollary 2. ‣ 4 Data-Driven Formulation and Choice of Model Parameters ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) by the same Monte Carlo method as in Step (3) and denote the estimated variance as σ^\hat{\sigma}. Define Υ^=Z^2𝔼ℙn​[‖∇κℙ∗′​(B)‖22]\hat{\Upsilon}=\frac{\hat{Z}^{2}}{\mathbb{E}\_{\mathbb{P}\_{n}}[\|\nabla\kappa^{\prime}\_{\mathbb{P}^{\*}}(B)\|\_{2}^{2}]}, where Z^∼𝒩​(0,σ^2)\hat{Z}\sim\mathcal{N}(0,\hat{\sigma}^{2}).
* •

  (5) Obtain independent samples Υ1,…​ΥK\Upsilon\_{1},\ldots\Upsilon\_{K} from Υ^\hat{\Upsilon}. Let η^.95\hat{\eta}\_{.95} be the 95%95\% quantile of the sample collections Υ1,…​ΥK\Upsilon\_{1},\ldots\Upsilon\_{K}. (KK is a sequence such that K→∞K\to\infty as n→∞n\to\infty, for example, K=log⁡nK=\log n; see Algorithm 1 in [Blanchet2021WassersteinDRO]).
* •

  (6) Set δ=η^.95n\delta=\frac{\hat{\eta}\_{.95}}{n} and approximate the solution to problem ([21](https://arxiv.org/html/2512.01408v1#S3.E21 "In 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) using Corollary [1](https://arxiv.org/html/2512.01408v1#Thmcorollary1 "Corollary 1 (Asymptotic non-linear optimal perturbation under Wasserstein distance). ‣ 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and get a worst case probability ℚ∗\mathbb{Q}^{\*} for the drift BB.
* •

  (7) Plug in this ℚ∗\mathbb{Q}^{\*} into the closed form formula of the optimal fraction with the observed stock prices and interest rates in Theorem [1](https://arxiv.org/html/2512.01408v1#Thmtheorem1 "Theorem 1 (Karatzas–Zhao [KZ98]’s Solution). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") replacing μ\mu by ℚ∗\mathbb{Q}^{\*}.

## 5 Synthetic Experiment

### 5.1 Understanding Model Parameters

In this section, we generate synthetic data in a high-dimensional setting and understand how parameters affect the performance of different models. We let the ground-truth drift to be

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bi​t=B02​(1+2​cos⁡(2​π​κi​t))B\_{it}=\frac{B\_{0}}{2}\left(1+2\cos(2\pi\kappa\_{i}t)\right) |  | (36) |

where ii represents the stock number. Each stock’s κi\kappa\_{i} is sampled from the same Gaussian distribution. We set the total number of stocks to be 20. The synthetic stock data is generated using ([2](https://arxiv.org/html/2512.01408v1#S2.E2 "In 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) with drift ([36](https://arxiv.org/html/2512.01408v1#S5.E36 "In 5.1 Understanding Model Parameters ‣ 5 Synthetic Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")), and we set the volatility matrix to be diagonal for simplicity. Throughout the paper, we always assume time 1 to be 1 year, and the unit time is d​tdt. Given our model is a continuous-time model, d​tdt should be very granular. The trading rule is simple: for every 22 d​tdt, calculate data-driven parameters and portfolio weights based on data of the previous 2520 d​tdt on a rolling basis and trade. The Bayesian Merton and DRBC have different portfolio weights for every d​tdt, yet others are static. We evaluate the performance using the Sharpe ratio with interest rate r=1%r=1\% on the last 252 d​tdt’s wealth. We vary B0,d​tB\_{0},dt and the distribution to sample κ\kappa to understand the models better, and we would like to use the intuition here to guide our experiments on real data.

All experiment procedures follow algorithm in [4](https://arxiv.org/html/2512.01408v1#S4 "4 Data-Driven Formulation and Choice of Model Parameters ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"). To be more precise, we estimate ℙ0\mathbb{P}\_{0} from the data using Consecutive Drift approach. Then, use the projection method to estimate δ\delta. After that, we compute Δ​(B)\Delta(B), which is not a projection, but rather a perturbation according to Theorem [3](https://arxiv.org/html/2512.01408v1#Thmtheorem3 "Theorem 3 (Nonlinear optimal perturbations). ‣ 3 Formulation and Main Structural Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"). Then we get the modified prior B∗=B+Δ​(B)B^{\*}=B+\Delta(B), then apply Formulae in [1](https://arxiv.org/html/2512.01408v1#Thmtheorem1 "Theorem 1 (Karatzas–Zhao [KZ98]’s Solution). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") with the modified prior distributions to get portfolio weights. Experiment results are shown in Table [1](https://arxiv.org/html/2512.01408v1#S5.T1 "Table 1 ‣ 5.1 Understanding Model Parameters ‣ 5 Synthetic Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), which is the average of 100 simulations (We use Sharpe Ratio here as performance metric. Table with terminal utility can be found in appendix [3](https://arxiv.org/html/2512.01408v1#Sx3.T3 "Table 3 ‣ Appendix: Additional Experiment Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")). Every simulation we use a different seed to sample both κi\kappa\_{i} and all the random numbers used in Theorem [1](https://arxiv.org/html/2512.01408v1#Thmtheorem1 "Theorem 1 (Karatzas–Zhao [KZ98]’s Solution). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"). Value for 1/(d​t×252)1/(dt\times 252) means how many periods we divide a day into. Notice the ground-truth drift is a periodic function with periodicity 1κ\frac{1}{\kappa}. The drift distribution is estimated as follows: update of drift estimation happens every 30 d​tdt, each time we use previous 2520 d​tdt to estimate drift distribution with batched, disjoint time windows. Specifically, we split the 2520 d​tdt into 10 no-overlapping periods, and estimate annualized return with each stock’s period cumulative return as in Section [4](https://arxiv.org/html/2512.01408v1#S4 "4 Data-Driven Formulation and Choice of Model Parameters ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"). We call this "Consecutive Drift". We call the market condition smooth when κ∼𝒩​(0,1)\kappa\sim\mathcal{N}(0,1) and is volatile when κ∼𝒩​(12,10)\kappa\sim\mathcal{N}(12,10). During smooth market conditions, models with frequent rebalancing, like Bayesian Merton, DRBC, and DRC, benefit from finer time trading resolution, while DRMV shows worse results. During volatile times, such benefits are not significant. In other words, if one believes the economy will grow steadily with no crisis for a long time, yet they also wants to avoid huge downside risk caused by noise, DRBC could be a reasonable choice.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Parameters | | | Average Sharpe Ratio | | | | |
| B0B\_{0} | 1/(d​t×252)1/(dt\times 252) | κ\kappa | Bayesian Merton | DRBC | DRMV\_no\_rf | DRMV\_rf | DRC |
| 0.2 | 6 | 𝒩​(0,1)\mathcal{N}(0,1) | 0.855 | 0.868 | 1.040 | 1.017 | 0.528 |
|  |  |  | (2.340) | (2.339) | (2.719) | (2.721) | (2.609) |
| 0.2 | 11 | 𝒩​(0,1)\mathcal{N}(0,1) | 0.880 | 0.893 | 0.887 | 0.861 | 0.641 |
|  |  |  | (3.128) | (3.126) | (3.474) | (3.585) | (3.479) |
| 0.4 | 6 | 𝒩​(0,1)\mathcal{N}(0,1) | 2.050 | 2.058 | 2.282 | 2.363 | 1.657 |
|  |  |  | (2.481) | (2.483) | (2.788) | (2.837) | (2.567) |
| 0.4 | 11 | 𝓝​(𝟎,𝟏)\bm{\mathcal{N}(0,1)} | 2.132 | 2.137 | 1.989 | 2.104 | 1.978 |
|  |  |  | (3.120) | (3.126) | (3.547) | (3.607) | (3.402) |
| 0.2 | 6 | 𝒩​(12,10)\mathcal{N}(12,10) | 0.720 | 0.728 | 0.922 | 0.902 | 0.422 |
|  |  |  | (2.312) | (2.310) | (2.645) | (2.683) | (2.608) |
| 0.2 | 11 | 𝒩​(12,10)\mathcal{N}(12,10) | 0.720 | 0.739 | 0.870 | 0.840 | 0.366 |
|  |  |  | (3.267) | (3.267) | (3.500) | (3.637) | (3.576) |
| 0.4 | 6 | 𝒩​(12,10)\mathcal{N}(12,10) | 1.796 | 1.801 | 2.034 | 2.106 | 1.399 |
|  |  |  | (2.398) | (2.398) | (2.654) | (2.702) | (2.622) |
| 0.4 | 11 | 𝒩​(12,10)\mathcal{N}(12,10) | 1.809 | 1.829 | 1.953 | 2.012 | 1.334 |
|  |  |  | (3.403) | (3.412) | (3.631) | (3.640) | (3.640) |

Table 1: Sharpe Ratio comparison across parameter settings over 100 simulations. Means reported with standard deviations in parentheses.

We also try different ways to estimate the drift distribution and how projection works in DRBC and benchmark methods. Details of DRMV and DRC are discussed in Section [6.1.1](https://arxiv.org/html/2512.01408v1#S6.SS1.SSS1 "6.1.1 DRMV ‣ 6.1 Experiment Design and Data Preparation ‣ 6 Real-data Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and [6.1.2](https://arxiv.org/html/2512.01408v1#S6.SS1.SSS2 "6.1.2 DRC ‣ 6.1 Experiment Design and Data Preparation ‣ 6 Real-data Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"). For drift estimation, we try day-of-week aggregation within larger windows (e.g., averages of “Mondays,” “Tuesdays,” etc.), we call it "Type Drift". In the experiments, all d​tdt are divided into 10 types to make a more fair comparison with the Consecutive Drift approach. For the perturbation Δ\Delta, we have two choices: change Δ\Delta every d​tdt by changing the plan time, or keep Δ\Delta static and make plan time the same as drift update frequency. The average Sharpe Ratio results are shown in Table [2](https://arxiv.org/html/2512.01408v1#S5.T2 "Table 2 ‣ 5.1 Understanding Model Parameters ‣ 5 Synthetic Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") (terminal utility results can be found in appendix [3](https://arxiv.org/html/2512.01408v1#Sx3.T3 "Table 3 ‣ Appendix: Additional Experiment Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")). We use B0=0.4,d​t=1252×11,κ∼𝒩​(0,1)B\_{0}=0.4,dt=\frac{1}{252\times 11},\kappa\sim\mathcal{N}(0,1) suggested by Section [5.1](https://arxiv.org/html/2512.01408v1#S5.SS1 "5.1 Understanding Model Parameters ‣ 5 Synthetic Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"). Consecutive drift and static projection achieves the best performance. A reasonable explanation for the Consecutive approach better than the Type approach is that the implicit number of "types" appears difficult to estimate (e.g. if we think that there is weakly seasonality the number of types should be around 5-7, but likely there are other time-patterns that do not align for all stocks). Only if type number perfectly echoes with Bi​tB\_{it}’s period we can get better drift estimation, yet it’s a rare case in practice. The Consecutive approach smooths the drift within the time batch and has better empirical practice overall. Regarding the use of the stating Projection, since here we use very small d​tdt, time-varying projection is likely influenced by extreme values at the end of drift update period. Simulation results follow our intuition, though the difference is small.

Table 2: Sharpe Ratios on different drift estimation and projection methods over 100 simulations (means on first line; standard deviations in parentheses on the next line)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Drift | Projection | Bayesian Merton | DRBC | DRMV\_no\_rf | DRMV\_rf | DRC |
| Consecutive | Static | 2.1319 | 2.1374 | 1.9890 | 2.1037 | 1.9778 |
| (3.1203) | (3.1261) | (3.5466) | (3.6072) | (3.4019) |
| Consecutive | Time-varying | 2.1319 | 2.1331 | 1.9890 | 2.1037 | 1.9778 |
| (3.1203) | (3.1268) | (3.5466) | (3.6072) | (3.4019) |
| Type | Static | 1.9815 | 1.9835 | 1.9890 | 2.1037 | 1.9995 |
| (3.4129) | (3.4132) | (3.5466) | (3.6072) | (3.4382) |
| Type | Time-varying | 1.9815 | 1.9814 | 1.9890 | 2.1037 | 1.9995 |
| (3.4129) | (3.4142) | (3.5466) | (3.6072) | (3.4382) |

### 5.2 Role of Radius

In this synthetic experiment, we show how different radii change the performance for DRC and DRBC comparing to optimal strategy, which implicitly proves the importance of data driven radius determination in Section [4](https://arxiv.org/html/2512.01408v1#S4 "4 Data-Driven Formulation and Choice of Model Parameters ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"). The experiment is a multi-dimensional setting with Wasserstein ball as the uncertainty set and we use the projection approach in Corollary [2](https://arxiv.org/html/2512.01408v1#Thmcorollary2 "Corollary 2. ‣ 4 Data-Driven Formulation and Choice of Model Parameters ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections").

The data generation part is similar to Section [5.1](https://arxiv.org/html/2512.01408v1#S5.SS1 "5.1 Understanding Model Parameters ‣ 5 Synthetic Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"). The drift terms are sampled from ([36](https://arxiv.org/html/2512.01408v1#S5.E36 "In 5.1 Understanding Model Parameters ‣ 5 Synthetic Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")), and the synthetic stock data is sampled using ([2](https://arxiv.org/html/2512.01408v1#S2.E2 "In 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) with 3024 d​tdt. We use Merton’s formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | πt=11−α​(σ​σT)−1​(Bt−r)\pi\_{t}=\frac{1}{1-\alpha}(\sigma\sigma^{T})^{-1}(B\_{t}-r) |  | (37) |

to calculate the optimal high dimensional portfolio strategy (policy) and calculate the oracle average terminal utility over one hundred simulated paths. The drift distribution is estimated with batched, disjoint time windows. In this way we have 10 support vectors of the drift distribution, and we assume the drift is uniform on these 10 supports. Here we use Wasserstein uncertainty and algorithm in [4](https://arxiv.org/html/2512.01408v1#S4 "4 Data-Driven Formulation and Choice of Model Parameters ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") to get the portfolio weights. We do not manually set δ\delta levels, but use a scale factor to scale up the data driven base δ\delta to explore the best radius since the data driven δ\delta is rough. Since every point in Figure [1](https://arxiv.org/html/2512.01408v1#S5.F1 "Figure 1 ‣ 5.2 Role of Radius ‣ 5 Synthetic Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") is an average of one hundred simulations, and our data driven δ\delta calculation gives different base δ\delta every simulation, we do not show exact δ\delta in use but show the scaling factor instead, with the average base δ\delta at the level of 10−310^{-3}. According to Figure [1](https://arxiv.org/html/2512.01408v1#S5.F1 "Figure 1 ‣ 5.2 Role of Radius ‣ 5 Synthetic Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), we observe that for DRBC, radius δ\delta needs to be carefully calibrated to achieve best terminal utility. For DRC, larger δ\delta always lead to worse performance.

![Refer to caption](gap_highdim.png)


Figure 1: Expectation of terminal utility gap versus δ\delta scaling factor for DRC and DRBC in high dimensional case with Wasserstein uncertainty

## 6 Real-data Experiment

For now, we use the same set of data and settings as [BlanchetChenZhou2021], to compare with the overall performance.

### 6.1 Experiment Design and Data Preparation

Inspired by the synthetic data experiment, which shows more granular time period helps continuous time models, we choose to set the trading frequency daily, which is more granular than monthly in [BlanchetChenZhou2021]. We get real data from Wharton Research Database Service (WRDS). The dataset contains all Standard and Pool’s 500 constituents data from 2017-01-01 to 2024-12-31. We choose this time period for two reasons: timeliness and variety of market events. During this period, the market experiences stable uptrend, COVID-19, inflation concerns, market recovery and the boom of Artificial Intelligence, making it very unpredictable and great to test the ability of different strategies in dealing with changes.

The experiment is done with rolling time window of one month. We use 5 years of previous data as the training set for DRBC to get uncertainty radius δ^\hat{\delta}, empirical distribution B^\hat{B} and values needed for benchmark strategies like DRC and Bayesian Merton. Here for simplicity, we let the δ\delta scaling factor to be 1. For stocks selection, we randomly sample 20 stocks from S&P 500 constituents in the past 5 years. The real trading period starts from 2022-01-01. DRBC and Bayesian Merton strategies trade daily and follow trading rules in Theorem [1](https://arxiv.org/html/2512.01408v1#Thmtheorem1 "Theorem 1 (Karatzas–Zhao [KZ98]’s Solution). ‣ 2 Preliminaries ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), with TT to be two months. Other strategies get static portfolio weights for one month. To avoid future information, specifically in YtY\_{t}, we do not trade on the first day of every month and then start using YtY\_{t} of the previous day. Since the interest rate changes much during our trading period, increases rapidly from about 0 percent to 5 percent and stays at that level, we do a simplification to assume all trades in the trading period with interest rate 5%. For evaluation, we report annualized return, standard deviation and sharpe ratio for the whole time series, and assume the interest rate to be 4%.

#### 6.1.1 DRMV

We include the Wasserstein-robust mean-variance model of [BlanchetChenZhou2021].
Given empirical distribution
Pn=1n​∑i=1nδRiP\_{n}=\frac{1}{n}\sum\_{i=1}^{n}\delta\_{R\_{i}},
they consider all return distributions inside the Wasserstein ball

|  |  |  |
| --- | --- | --- |
|  | 𝒰δ​(Pn)={P:Dc​(P,Pn)≤δ},c​(u,v)=‖u−v‖q2.\mathcal{U}\_{\delta}(P\_{n})=\{P:D\_{c}(P,P\_{n})\leq\delta\},\qquad c(u,v)=\|u-v\|\_{q}^{2}. |  |

The robust Markowitz problem is

|  |  |  |  |
| --- | --- | --- | --- |
|  | minϕ⁡maxP∈𝒰δ​(Pn)⁡ϕ⊤​VarP⁡(R)​ϕs.t. ​ 1⊤​ϕ=1,minP∈𝒰δ​(Pn)⁡𝔼P​[R]⊤​ϕ≥α¯.\min\_{\phi}\;\;\max\_{P\in\mathcal{U}\_{\delta}(P\_{n})}\phi^{\top}\operatorname{Var}\_{P}(R)\phi\quad\text{s.t. }\;\mathbf{1}^{\top}\phi=1,\;\min\_{P\in\mathcal{U}\_{\delta}(P\_{n})}\mathbb{E}\_{P}[R]^{\top}\phi\geq\bar{\alpha}. |  | (38) |

A key result is that ([38](https://arxiv.org/html/2512.01408v1#S6.E38 "In 6.1.1 DRMV ‣ 6.1 Experiment Design and Data Preparation ‣ 6 Real-data Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) is *exactly equivalent* to a regularized empirical problem:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | minϕ\displaystyle\min\_{\phi} | ϕ⊤​Σ^​ϕ+δ​‖ϕ‖p,\displaystyle\phi^{\top}\hat{\Sigma}\,\phi+\sqrt{\delta}\,\|\phi\|\_{p}, |  | (39) |
|  | s.t. | 𝟏⊤​ϕ=1,μ^⊤​ϕ≥α¯+δ​‖ϕ‖p,\displaystyle\mathbf{1}^{\top}\phi=1,\qquad\hat{\mu}^{\top}\phi\geq\bar{\alpha}+\sqrt{\delta}\,\|\phi\|\_{p}, |  |

where μ^=𝔼Pn​[R]\hat{\mu}=\mathbb{E}\_{P\_{n}}[R], Σ^=VarPn⁡(R)\hat{\Sigma}=\operatorname{Var}\_{P\_{n}}(R), and 1/p+1/q=11/p+1/q=1.

Thus, Wasserstein robustness leads to a theoretically justified norm penalty ‖ϕ‖p\|\phi\|\_{p}, and the ambiguity radius δ\delta and target α¯\bar{\alpha} are chosen via data-driven Wasserstein profile inference.

We use two sets of DRMV algorithm, the original one in [BlanchetChenZhou2021] and the one with risk free asset. For the second one, we view the interest rate as the last entry of the return vector, and choose the δ\delta in the same way as [BlanchetChenZhou2021], and change the annual target return ρ\rho from 10%10\% to 10.5%10.5\%. To avoid trivial results, we manually add a small noise to the interest rate.

#### 6.1.2 DRC

Classical DRC formulations [HansenSargent2001, hansen2008robustness] introduce an adversary who, at every time tt, perturbs the model by selecting a worst–case probability measure within a ϕ\phi–divergence ball.
Given a baseline model PP, at each time step the adversary selects Q≪PQ\ll P satisfying

|  |  |  |
| --- | --- | --- |
|  | Dϕ​(Q∥P)≤δ,D\_{\phi}(Q\|P)\;\leq\;\delta, |  |

where DϕD\_{\phi} is the ϕ\phi–divergence generated by a convex function ϕ\phi with ϕ​(1)=0\phi(1)=0.
The controller then solves the dynamic game

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπ∈𝒜​(x0)infQ∈𝒰δDRC𝔼Q​[u​(XT)],\sup\_{\pi\in\mathcal{A}(x\_{0})}\inf\_{Q\in\mathcal{U}\_{\delta}^{\text{DRC}}}\;\mathbb{E}\_{Q}\!\left[u(X\_{T})\right], |  | (40) |

where 𝒰δDRC\mathcal{U}\_{\delta}^{\text{DRC}} denotes the time replenished uncertainty set: the adversary is allowed to choose a new worst–case distribution at every instant.

Here, DRC is a high-dimensional implementation of [Blanchet2025Duality], where an optimization problem induced by the Hamilton-Jacobi-Bellman-Isaacs (HJBI) equation is solved to get the drift estimation, and then the Merton portfolio weight formula ([37](https://arxiv.org/html/2512.01408v1#S5.E37 "In 5.2 Role of Radius ‣ 5 Synthetic Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) is used to get the portfolio weights. For the same practical concern in shorting stocks as in DRBC, we also assume that the short position of each stock cannot surpass half of the wealth. For the radius in DRC, we directly use the radius from DRBC for simplicity. Note that this is not the optimal radius for DRC.

#### 6.1.3 DRBC

To calculate empirical B^\hat{B} and δ^\hat{\delta}, we use the previous 5 years of data. We use Ledoit-Wolf [ledoit2004well] algorithm to estimate the covariance matrix, and we calibrate the items in the inverse of the volatility matrix to be within a range for numerical stability. As directly scaling up the daily return to annually might lead to unreasonable values, we also calibrate on the empirical center to keep outliers in a limit. Since BB can be roughly regarded as log return plus volatility, the limit is chosen based on knowledge of financial markets. Besides, given the difficulty to naked short a stock in practice, we assume that the short position of each stock cannot surpass half of wealth.

### 6.2 Comparison and Discussions

We compare the histogram of Sharpe Ratio for aforementioned methods. Figure [2](https://arxiv.org/html/2512.01408v1#S6.F2 "Figure 2 ‣ 6.2 Comparison and Discussions ‣ 6 Real-data Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") shows the distribution of Sharpe Ratio for Bayes Merton and DRBC. It’s clear the DRBC distribution shifts rightward and more concentrated on positive Sharpe Ratio. It certifies that true priors in financial markets are high unpredictable and distributionally robust methods are necessary.

Comparison between DRBC and two types of DRMV appear in Figure [4](https://arxiv.org/html/2512.01408v1#S6.F4 "Figure 4 ‣ 6.2 Comparison and Discussions ‣ 6 Real-data Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and [3](https://arxiv.org/html/2512.01408v1#S6.F3 "Figure 3 ‣ 6.2 Comparison and Discussions ‣ 6 Real-data Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"). Both DRMV methods have more concentrated distributions than DRBC, which is reasonable since DRMV implementations do not allow short selling and borrowing money, thus are more stable than DRBC. Despite not concentrated, DRBC achieves larger average Sharpe Ratio than DRMV during our volatile test period. It is also worth noting that DRBC is a continuous time model while DRMV is not. According to [BlanchetChenZhou2021], continuous time models tend to perform worse than discrete time model, which further ensures the effectiveness of DRBC.

Likewise, as in Figure [5](https://arxiv.org/html/2512.01408v1#S6.F5 "Figure 5 ‣ 6.2 Comparison and Discussions ‣ 6 Real-data Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), DRBC outperforms DRC with a more right shifted distribution, with both larger maximum and minimum Sharpe Ratio. Figure [5](https://arxiv.org/html/2512.01408v1#S6.F5 "Figure 5 ‣ 6.2 Comparison and Discussions ‣ 6 Real-data Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") also prevails our claim that DRBC can reduce over-pesimissm in DRC.

![Refer to caption](hist_drbc_kara.png)


Figure 2: Histogram of Sharpe Ratios for Bayesian Merton and DRBC

![Refer to caption](hist_drbc_drmvrf.png)


Figure 3: Histogram of Sharpe Ratios for DRMV with riskless asset and DRBC

![Refer to caption](hist_drbc_drmv.png)


Figure 4: Histogram of Sharpe Ratios for DRMV without riskless asset and DRBC

![Refer to caption](hist_drbc_drc.png)


Figure 5: Histogram of Sharpe Ratios for DRC and DRBC

## 7 Conclusions and Future Work

In this paper, we revisited Merton’s continuous-time portfolio selection problem through a distributionally robust Bayesian control lens. By placing a single ambiguity set on the drift prior, rather than adopting time-rectangular uncertainty on the data-generating process, which tends to be too pessimistic. We preserved the Bayesian learning structure intended to mitigate the over-pessimism often induced by dynamic robust control. A Sion-type minimax swap reduced the DRBC game to a non-linear distributional optimization problem over the drift prior, allowing us to retain the Karatzas–Zhao [KZ98]’s closed-form characterization of the value function and optimal policy for each candidate prior. Even if the Sion minimax swap induces a duality gap, weak duality still generates a valid bound which we believe is useful specially in dynamic optimization settings, in which over-pessimism tends to arise more often compared to static adversarial formulations. Therefore, the approach that we propose in this paper, we believe, could be broadly applicable to Bayesian control formulations in which the prior is imposed on certain model parameters.

There are natural directions for future work. One of them is precisely to investigate our proposed approach, as we hinted in the previous paragraph, in distributionally robust Bayesian control settings. This paper provides a blue-print in the setting of Merton’s model because it is both elegant and of significant interest (both academically and practically). A broader extension would need to be more algorithmic, dealing with efficient methods for solving the Bayesian control problem jointly with the evaluation of the required sensitivities (which we characterize in this paper). However, we believe that such an extension is worth pursuing.

## Supplementary Material

Generalizations of the results to non-compact priors are furnished in the supplementary materials.

## Acknowledgement

J. Blanchet gratefully acknowledges support from DoD through ONR N000142412655, also support from NSF via grants 2312204, 2403007 is gratefully acknowledged. Y. Liu acknowledges financial support from the National Natural Science Foundation of China (Grant No. 12401624), The Chinese University of Hong Kong (Shenzhen) University
Development Fund (Grant No. UDF01003336) and Shenzhen Science and Technology Program (Grant
No. RCBS20231211090814028, JCYJ20250604141203005, 2025TC0010) and is partly supported by the
Guangdong Provincial Key Laboratory of Mathematical Foundations for Artificial Intelligence (Grant No.
2023B1212010001).

## Appendix: Additional Experiment Results

In this section, we show additional experiment results in Section [5](https://arxiv.org/html/2512.01408v1#S5 "5 Synthetic Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and Section [6](https://arxiv.org/html/2512.01408v1#S6 "6 Real-data Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections").

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Parameters | | | Average Terminal Utility | | | | |
| B0B\_{0} | 1/(d​t×252)1/(dt\times 252) | κ\kappa | Bayesian Merton | DRBC | DRMV\_no\_rf | DRMV\_rf | DRC |
| 0.2 | 6 | 𝒩​(0,1)\mathcal{N}(0,1) | -0.389 | -0.383 | -0.319 | -0.320 | -0.787 |
|  |  |  | (0.386) | (0.373) | (0.033) | (0.030) | (1.396) |
| 0.2 | 11 | 𝒩​(0,1)\mathcal{N}(0,1) | -0.356 | -0.353 | -0.327 | -0.327 | -0.400 |
|  |  |  | (0.225) | (0.218) | (0.024) | (0.022) | (0.298) |
| 0.4 | 6 | 𝒩​(0,1)\mathcal{N}(0,1) | -0.277 | -0.275 | -0.303 | -0.305 | -0.769 |
|  |  |  | (0.345) | (0.338) | (0.033) | (0.030) | (1.975) |
| 0.4 | 11 | 𝓝​(𝟎,𝟏)\bm{\mathcal{N}(0,1)} | -0.289 | -0.288 | -0.319 | -0.319 | -0.322 |
|  |  |  | (0.216) | (0.209) | (0.023) | (0.022) | (0.308) |
| 0.2 | 6 | 𝒩​(12,10)\mathcal{N}(12,10) | -0.403 | -0.397 | -0.321 | -0.322 | -0.773 |
|  |  |  | (0.390) | (0.376) | (0.033) | (0.030) | (1.267) |
| 0.2 | 11 | 𝒩​(12,10)\mathcal{N}(12,10) | -0.365 | -0.361 | -0.327 | -0.327 | -0.417 |
|  |  |  | (0.229) | (0.221) | (0.024) | (0.022) | (0.306) |
| 0.4 | 6 | 𝒩​(12,10)\mathcal{N}(12,10) | -0.304 | -0.300 | -0.306 | -0.308 | -0.708 |
|  |  |  | (0.358) | (0.347) | (0.031) | (0.029) | (1.660) |
| 0.4 | 11 | 𝒩​(12,10)\mathcal{N}(12,10) | -0.313 | -0.311 | -0.319 | -0.319 | -0.372 |
|  |  |  | (0.236) | (0.230) | (0.024) | (0.022) | (0.338) |

Table 3: Terminal utility comparison across parameter settings over 100 simulations. Means reported with standard deviations in parentheses.




Table 4: Terminal utility on different drift estimation and projection methods over 100 simulations (means on first line; standard deviations in parentheses on the next line)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Drift | Projection | Bayesian Merton | DRBC | DRMV\_no\_rf | DRMV\_rf | DRC |
| Consecutive | Static | -0.2893 | -0.2883 | -0.3186 | -0.3189 | -0.3224 |
| (0.2156) | (0.2092) | (0.0234) | (0.0216) | (0.3077) |
| Consecutive | Time-varying | -0.2893 | -0.2889 | -0.3186 | -0.3189 | -0.3224 |
| (0.2156) | (0.2113) | (0.0234) | (0.0216) | (0.3077) |
| Type | Static | -0.2986 | -0.2982 | -0.3186 | -0.3189 | -0.3287 |
| (0.2204) | (0.2192) | (0.0234) | (0.0216) | (0.3351) |
| Type | Time-varying | -0.2986 | -0.2984 | -0.3186 | -0.3189 | -0.3287 |
| (0.2204) | (0.2196) | (0.0234) | (0.0216) | (0.3351) |

### 7.1 Discussions for Real Data Experiment

In Section [6](https://arxiv.org/html/2512.01408v1#S6 "6 Real-data Experiment ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), we mention the short constraint we add to make sure every single stock’s short position cannot exceed half of the wealth. This is reasonable in practice, yet we want to investigate how many times this constraint is triggered in DRC, DRBC and Bayesian methods, as well as the leverage condition among these methods.

Across all simulations with different data generating parameters, the short constraint happens in more than 90% of trades for DRC method, which is a common disadvantage for Merton-like problems since it always gives extreme values due to the estimation error of average return and variance matrix and the unconstrained optimization. Short constraint appears in about 70% trades in Bayesian setting and about 40% in DRBC setting, illustrating Bayesian methods by [KZ98] can mitigate extreme weights in Merton-like problems and DRBC can further decrease extreme weights.

We also check the overall leverage ratio for three algorithms. DRC on average uses about 13x leverage, with outliers like 31x. Bayesian uses about 7x and DRBC 5x in average. The leverage ratio highly depend on how drift B is estimated, which depends on the training period. If finer constraints on both short and long positions are added, it will give you results with less leverage, yet cannot fully reveal the strength of DRBC method.

## Supplementary Material: Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections

This material is companion to the paper main body of the paper Distributionally Robust Merton Problem Via Nonlinear Wasserstein Projection. In these sections we adapt the results developed in the main body to the case of non-compactly supported prior distributions for power utilities.” And then just present the development.

## Appendix A Sub-Gaussian Extensions of the Main Results

In Sections [B](https://arxiv.org/html/2512.01408v1#A2 "Appendix B Generalization of Minimax Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), [C](https://arxiv.org/html/2512.01408v1#A3 "Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), and [D](https://arxiv.org/html/2512.01408v1#A4 "Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), we study a commonly used
utility function in the case where the random drift BB is no longer
compactly supported. This shows that the compactness assumption in the
main text is not essential for the validity of our results; it is
imposed there mainly to avoid lengthy technical arguments involving
exponential moment bounds and Gaussian integrals.

Throughout these sections we fix a CRRA utility

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(x)=xαα,x>0,α<1,α≠0,u(x)=\frac{x^{\alpha}}{\alpha},\qquad x>0,\quad\alpha<1,\ \alpha\neq 0, |  | (41) |

and work under a sub-Gaussian assumption on the prior distribution of
BB. More precisely, we assume:

###### Assumption 3 (Sub-Gaussian prior on BB).

There exists γ0>0\gamma\_{0}>0 such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ0​[exp⁡(γ2​‖B‖22)]<∞for all ​γ<γ0.\mathbb{E}\_{\mathbb{P}\_{0}}\!\left[\exp\bigl(\gamma^{2}\|B\|\_{2}^{2}\bigr)\right]<\infty\qquad\text{for all }\gamma<\gamma\_{0}. |  |

This condition is standard: it requires finite exponential moments of
‖B‖2\|B\|^{2} and will be used repeatedly to control various Gaussian
integrals arising from the likelihood ratio LT​(B,y)L\_{T}(B,y) and its
derivatives.

## Appendix B Generalization of Minimax Theorem with Non-compact Support

We first explain how the Minimax Theorem extends to the sub-Gaussian setting when the utility is given by
([41](https://arxiv.org/html/2512.01408v1#A1.E41 "In Appendix A Sub-Gaussian Extensions of the Main Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")). The goal of this subsection is *only* to
highlight where compactness is used and how Assumption [3](https://arxiv.org/html/2512.01408v1#Thmassumption3 "Assumption 3 (Sub-Gaussian prior on 𝐵). ‣ Appendix A Sub-Gaussian Extensions of the Main Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")
replaces it; the detailed sub-Gaussian estimates are of the same style
as those developed later in Sections [C](https://arxiv.org/html/2512.01408v1#A3 "Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and [D](https://arxiv.org/html/2512.01408v1#A4 "Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), and we
do not repeat them here.

Recall that in the compact case the proof proceeds in five
steps. Steps 2 and 3 establish continuity and concavity properties of
the map

|  |  |  |
| --- | --- | --- |
|  | (π,ℚ)↦𝔼ℚ​[U​(Xπ​(T))],(\pi,\mathbb{Q})\mapsto\mathbb{E}\_{\mathbb{Q}}[U(X^{\pi}(T))], |  |

while Step 5 uses the closed-form structure of the Karatzas–Zhao
solution to construct an optimal feedback control and to verify that it
lies in the admissible set 𝒜′​(x0)\mathcal{A}^{\prime}(x\_{0}).

Step 2 and Step 3 (moment bounds and continuity).
In the compact-support proof, compactness assumption is used to obtain uniform
bounds on the drift term in the wealth process and on the likelihood
ratio LT​(b,y)L\_{T}(b,y), uniformly over b∈Kb\in K. These bounds, together with
the polynomial growth utility, yield
uniform positive and negative moment bounds for Xπ​(T)X^{\pi}(T) and hence
integrability of U​(Xπ​(T))U(X^{\pi}(T)); dominated convergence then gives the
required continuity in the model and in the control.

Under Assumption [3](https://arxiv.org/html/2512.01408v1#Thmassumption3 "Assumption 3 (Sub-Gaussian prior on 𝐵). ‣ Appendix A Sub-Gaussian Extensions of the Main Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), these arguments remain
valid after replacing compactness by exponential moment estimates. The
key observation is that the Gaussian likelihood LT​(B,y)L\_{T}(B,y) and its
derivatives grow at most exponentially in ‖B‖\|B\| and ‖y‖\|y\|. Combined
with Assumption [3](https://arxiv.org/html/2512.01408v1#Thmassumption3 "Assumption 3 (Sub-Gaussian prior on 𝐵). ‣ Appendix A Sub-Gaussian Extensions of the Main Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), one can bound the relevant
expectations by standard Gaussian integrals and show that

|  |  |  |
| --- | --- | --- |
|  | supℚ∈𝒰δOT​(ℙ0)𝔼ℚ​[|Xπ​(T)|2+ε]<∞,supℚ∈𝒰δOT​(ℙ0)𝔼ℚ​[|Xπ​(T)|−m]<∞\sup\_{\mathbb{Q}\in\mathcal{U}^{\mathrm{OT}}\_{\delta}(\mathbb{P}\_{0})}\mathbb{E}\_{\mathbb{Q}}\bigl[|X^{\pi}(T)|^{2+\varepsilon}\bigr]<\infty,\qquad\sup\_{\mathbb{Q}\in\mathcal{U}^{\mathrm{OT}}\_{\delta}(\mathbb{P}\_{0})}\mathbb{E}\_{\mathbb{Q}}\bigl[|X^{\pi}(T)|^{-m}\bigr]<\infty |  |

for suitable ε,m>0\varepsilon,m>0 and all π∈𝒜′​(x0)\pi\in\mathcal{A}^{\prime}(x\_{0}). The
rest of Steps 2 and 3 (continuity in ℚ\mathbb{Q} and in π\pi) then
follow exactly as in the compact-support proof; only the bounds used to
justify dominated convergence change, and these are handled by the same
type of sub-Gaussian computations that we carry out in detail for nonlinear perturbation and projection theorems in Sections [C](https://arxiv.org/html/2512.01408v1#A3 "Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and [D](https://arxiv.org/html/2512.01408v1#A4 "Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), respectively.

Step 4 (use of Sion’s Theorem).
In the sub-Gaussian extension in Section [C](https://arxiv.org/html/2512.01408v1#A3 "Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and
[D](https://arxiv.org/html/2512.01408v1#A4 "Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") (as shown later), the optimal transport cost is no longer the quadratic cost
‖Δ‖22\|\Delta\|\_{2}^{2} used in the main text.
Instead, following the Gaussian-integrability estimates derived in this
appendix, the natural cost becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | cτ​(Δ):=eτ​‖Δ‖22− 1,c\_{\tau}(\Delta)\;:=\;e^{\,\tau\,\|\Delta\|\_{2}^{2}}\;-\;1, |  | (42) |

where the parameter τ>0\tau>0 depends explicitly on
α\alpha, TT, and ‖σ−1‖F2\|\sigma^{-1}\|\_{F}^{2} through the sub-Gaussian
tail bounds of the prior distribution of BB.

We emphasize that this change of transport cost does *not* affect
the minimax argument.
The function Δ↦cτ​(Δ)\Delta\mapsto c\_{\tau}(\Delta) is convex, and therefore
the divergence ball

|  |  |  |
| --- | --- | --- |
|  | 𝒰δcτ:={ℚ:Dcτ​(ℚ∥P0)≤δ}\mathcal{U}\_{\delta}^{c\_{\tau}}:=\bigl\{\mathbb{Q}:D\_{c\_{\tau}}(\mathbb{Q}\,\|\,P\_{0})\leq\delta\bigr\} |  |

is convex.
Moreover, because cτ​(Δ)c\_{\tau}(\Delta) grows superlinearly in
‖Δ‖2\|\Delta\|\_{2}, the corresponding OT balls are tight and relatively
compact under the topology induced by optimal transport.
Since the payoff functional is linear in ℚ\mathbb{Q} and concave in the
control π\pi, all assumptions of Sion’s minimax theorem remain valid.
Hence the change of cost from ‖Δ‖22\|\Delta\|\_{2}^{2} to cτ​(Δ)c\_{\tau}(\Delta) does
not alter the validity of the min–max swap in
Theorem [B](https://arxiv.org/html/2512.01408v1#A2 "Appendix B Generalization of Minimax Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections").

Step 5 (feedback form and admissibility).
In Step 5 of the main-text proof, the compactness of KK was used to
obtain two-sided exponential bounds on the function F​(T,u)F(T,u) and its
gradient, and polynomial growth condition on the utility function was used to control the
ratio

|  |  |  |
| --- | --- | --- |
|  | Ξ​(t,y)Θ​(t,y)\frac{\Xi(t,y)}{\Theta(t,y)} |  |

in terms of exp⁡{c​‖y‖}\exp\{c\|y\|\}. In the present CRRA setting
([41](https://arxiv.org/html/2512.01408v1#A1.E41 "In Appendix A Sub-Gaussian Extensions of the Main Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")), the inverse marginal utility I=(U′)−1I=(U^{\prime})^{-1} and
its derivative admit explicit power-type bounds, so the lower bound on
II required in Step 5 is automatic. Under
Assumption [3](https://arxiv.org/html/2512.01408v1#Thmassumption3 "Assumption 3 (Sub-Gaussian prior on 𝐵). ‣ Appendix A Sub-Gaussian Extensions of the Main Results ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), the same exponential estimates for
F​(T,u)F(T,u) and 1/F​(T,u)1/F(T,u) as in the compact case are recovered by
computing Gaussian integrals involving LT​(B,u)L\_{T}(B,u) and using the
sub-Gaussian tails of BB. Consequently, the ratio
Ξ​(t,y)/Θ​(t,y)\Xi(t,y)/\Theta(t,y) is again controlled by an exponential in
‖y‖\|y\|, and the feedback control π∗,b\pi^{\*,b} satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ​(∫0T‖π∗,b​(t)‖2​𝑑t)1/2<∞,∀ℚ∈𝒰δOT​(ℙ0),\mathbb{E}\_{\mathbb{Q}}\Biggl(\int\_{0}^{T}\|\pi^{\*,b}(t)\|^{2}\,dt\Biggr)^{1/2}<\infty,\qquad\forall\,\mathbb{Q}\in\mathcal{U}^{\mathrm{OT}}\_{\delta}(\mathbb{P}\_{0}), |  |

so that π∗,b∈𝒜′​(x0)\pi^{\*,b}\in\mathcal{A}^{\prime}(x\_{0}).

## Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support

In this section, we give a full detailed analysis of how the proofs of the Nonlinear Perturbation Theorem goes without the compact assumption. The proof skills used here are the same as those estimates for Section [B](https://arxiv.org/html/2512.01408v1#A2 "Appendix B Generalization of Minimax Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections").

After the swapping theorem, with the specific power utility, the distributional optimization problem becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℚ∗={arg⁡minℚ∈𝒰δ,BD​(ℙ0)⁡𝒥​(ℚ),if ​α∈(0,1);arg⁡maxℚ∈𝒰δ,BD​(ℙ0)⁡𝒥​(ℚ),if ​α<0,\displaystyle\mathbb{Q}^{\*}=\begin{cases}\arg\min\_{\mathbb{Q}\in\mathcal{U}\_{\delta,B}^{D}(\mathbb{P}\_{0})}\mathcal{J}(\mathbb{Q}),&\text{if }\alpha\in(0,1);\\ \arg\max\_{\mathbb{Q}\in\mathcal{U}\_{\delta,B}^{D}(\mathbb{P}\_{0})}\mathcal{J}(\mathbb{Q}),&\text{if }\alpha<0,\end{cases} |  | (43) |

where

|  |  |  |
| --- | --- | --- |
|  | 𝒥​(ℚ)=∫ℝd(𝔼ℚ​[LT​(B,z)])11−α​φT​(z)​𝑑z.\mathcal{J}(\mathbb{Q})=\int\_{\mathbb{R}^{d}}\left(\mathbb{E}\_{\mathbb{Q}}\left[L\_{T}(B,z)\right]\right)^{\frac{1}{1-\alpha}}\varphi\_{T}(z)dz. |  |

We impose a natural sub-Gaussian assumption on BB, and interestingly, the cost function for the optimal transport uncertainty set should be changed to the following: for a displacement Δ∈ℝd\Delta\in\mathbb{R}^{d} and scale τ>0\tau>0, the cost function for the optimal transport is defined via

|  |  |  |
| --- | --- | --- |
|  | cτ​(Δ):=eτ​‖Δ‖22− 1.\ c\_{\tau}(\Delta)\;:=\;e^{\,\tau\,\|\Delta\|\_{2}^{2}}\;-\;1. |  |

The main reason of this definition is to ensure the integrability conditions and the use of swapping orders of integration, differentiation, or limit, etc, which are easy to achieve in the compact case.

We remark that the parameter τ\tau depends on α,T,‖σ−1‖F2\alpha,T,\left\|\sigma^{-1}\right\|\_{F}^{2}. We also assume that

|  |  |  |
| --- | --- | --- |
|  | τ>max⁡{4​T​‖σ−1‖F2,2​T​(4​β2−2​β)​‖σ−1‖F2},\tau>\max\left\{4T\left\|\sigma^{-1}\right\|\_{F}^{2},2T\,(4\beta^{2}-2\beta)\,\|\sigma^{-1}\|\_{F}^{2}\right\}, |  |

where β=α1−α\beta=\frac{\alpha}{1-\alpha}. The precise sub-Gaussian assumption is given below.

###### Assumption 4.

Suppose there exists γ0>0\gamma\_{0}>0 such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ0​[exp⁡(γ2​‖B‖22)]<∞for every ​γ<γ0.\mathbb{E}\_{\mathbb{P}\_{0}}\big[\exp(\gamma^{2}\|B\|\_{2}^{2})\big]<\infty\quad\text{for every }\gamma<\gamma\_{0}. |  |

with

|  |  |  |
| --- | --- | --- |
|  | γ02‖σ−1‖F2>T​max⁡{12​(β2−β+2+(β2−β+2)2+8​(β2+β)),8,τ⋅2​T​(4​β2−2​β)τ−2​T​(4​β2−2​β)​‖σ−1‖F2}.\frac{\gamma\_{0}^{2}}{\|\sigma^{-1}\|\_{F}^{2}}\;>\;T\max\left\{\frac{1}{2}\Big(\beta^{2}-\beta+2\;+\;\sqrt{\,(\beta^{2}-\beta+2)^{2}+8(\beta^{2}+\beta)\,}\Big)\;,8,\frac{\tau\cdot 2T\,(4\beta^{2}-2\beta)\,}{\tau-2T\,(4\beta^{2}-2\beta)\,\|\sigma^{-1}\|\_{F}^{2}}\right\}. |  |

We begin with the nonlinear perturbation theorem in this setting and stating several technical lemmas.

###### Theorem 5.

Assume that for the fixed α\alpha, we have the corresponding cost function and τ\tau as in the definition. We define

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(b):=11−α​∫ℝd∇bLT​(b,y)​𝔼ℙ0​[LT​(B,y)]α1−α​φT​(y)​𝑑yH(b)\;:=\;\frac{1}{1-\alpha}\int\_{\mathbb{R}^{d}}\nabla\_{b}L\_{T}(b,y)\,\mathbb{E}\_{\mathbb{P}\_{0}}[L\_{T}(B,y)]^{\frac{\alpha}{1-\alpha}}\;\varphi\_{T}(y)\,dy |  | (44) |

and

|  |  |  |
| --- | --- | --- |
|  | ‖H‖L22​(ℙ0):=(𝔼ℙ0​‖H​(B)‖22)1/2.\|H\|\_{L^{2}\_{2}(\mathbb{P}\_{0})}:=\Big(\mathbb{E}\_{\mathbb{P}\_{0}}\|H(B)\|\_{2}^{2}\Big)^{1/2}. |  |

Then under Assumption [4](https://arxiv.org/html/2512.01408v1#Thmassumption4 "Assumption 4. ‣ Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), when α∈(0,1)\alpha\in(0,1), as δ→0\delta\to 0, an asymptotically optimal perturbation is the deterministic pushforward

|  |  |  |
| --- | --- | --- |
|  | Δδ∗​(b)=−δτ​H​(b)‖H‖L22​(ℙ0)+o​(δ)\Delta^{\*}\_{\delta}(b)\;=-\;\sqrt{\frac{\delta}{\tau}}\,\frac{H(b)}{\|H\|\_{L^{2}\_{2}(\mathbb{P}\_{0})}}+o(\sqrt{\delta}) |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | infℚ∈𝒰δ,BOT​(ℙ0)𝒥​(ℚ)=𝒥​(ℙ0)−δτ​‖H‖L22​(ℙ0)+o​(δ).\inf\_{\mathbb{Q}\in\mathcal{U}\_{\delta,B}^{\text{OT}}(\mathbb{P}\_{0})}\mathcal{J}(\mathbb{Q})=\mathcal{J}(\mathbb{P}\_{0})-\sqrt{\frac{\delta}{\tau}}\|H\|\_{L^{2}\_{2}(\mathbb{P}\_{0})}+o(\sqrt{\delta}). |  | (45) |

When α<0\alpha<0, as δ→0\delta\to 0, an asymptotically optimal perturbation is the deterministic pushforward

|  |  |  |
| --- | --- | --- |
|  | Δδ∗​(b)=δτ​H​(b)‖H‖L22​(ℙ0)+o​(δ)\Delta^{\*}\_{\delta}(b)\;=\;\sqrt{\frac{\delta}{\tau}}\,\frac{H(b)}{\|H\|\_{L^{2}\_{2}(\mathbb{P}\_{0})}}+o(\sqrt{\delta}) |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | supℚ∈𝒰δ,BOT​(ℙ0)𝒥​(ℚ)=𝒥​(ℙ0)+δτ​‖H‖L22​(ℙ0)+o​(δ).\sup\_{\mathbb{Q}\in\mathcal{U}\_{\delta,B}^{\text{OT}}(\mathbb{P}\_{0})}\mathcal{J}(\mathbb{Q})=\mathcal{J}(\mathbb{P}\_{0})+\sqrt{\frac{\delta}{\tau}}\|H\|\_{L^{2}\_{2}(\mathbb{P}\_{0})}+o(\sqrt{\delta}). |  | (46) |

The proof essentially contains two parts. The first part is Lemma [2](https://arxiv.org/html/2512.01408v1#Thmlemma2 "Lemma 2. ‣ Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), giving the required integrability conditions, and the second part is to linearize the problem and then solve the constrained linear problem, similar to the case in the main body.

###### Lemma 2.

Under Assumption [4](https://arxiv.org/html/2512.01408v1#Thmassumption4 "Assumption 4. ‣ Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), then

* •

  (1) for any α<1\alpha<1 and α≠0\alpha\neq 0,
  the vector field of Eq. ([44](https://arxiv.org/html/2512.01408v1#A3.E44 "In Theorem 5. ‣ Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) is well-defined ℙ0\mathbb{P}\_{0} almost surely and satisfies 𝔼ℙ0​[‖H​(B)‖22]<∞\mathbb{E}\_{\mathbb{P}\_{0}}[\left\|H(B)\right\|\_{2}^{2}]<\infty.
* •

  (2) for any s∈[0,1]s\in[0,1], set

  |  |  |  |
  | --- | --- | --- |
  |  | Fs​(B,Δ):=∫ℝd∇bLT​(B+s​Δ,y)​(𝔼​[LT​(B+s​Δ,y)])α1−α​φT​(y)​𝑑y.F\_{s}(B,\Delta)\;:=\int\_{\mathbb{R}^{d}}\nabla\_{b}L\_{T}(B+s\Delta,y)\;\Big(\mathbb{E}\big[L\_{T}(B+s\Delta,y)\big]\Big)^{\frac{\alpha}{1-\alpha}}\;\varphi\_{T}(y)\,dy. |  |

  Then there exist constants C​(B)>0C(B)>0 and finite ℙ0\mathbb{P}\_{0} almost surely and C1≤τC\_{1}\leq\tau (τ\tau depends on α\alpha) such that, ℙ0\mathbb{P}\_{0} almost surely,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ‖Fs​(B,Δ)‖22≤C​(B)​exp⁡(C1​‖Δ‖22).\|F\_{s}(B,\Delta)\|\_{2}^{2}\;\leq C(B)\exp(C\_{1}\left\|\Delta\right\|\_{2}^{2}). |  | (47) |

###### Proof.

We first prove part (1) and assume α<0\alpha<0 and denote β:=α1−α\beta:=\frac{\alpha}{1-\alpha}. Define A​(y):=𝔼ℙ0​[LT​(B,y)]A(y):=\mathbb{E}\_{\mathbb{P}\_{0}}[L\_{T}(B,y)] where BB is a random vector on ℝd\mathbb{R}^{d} with law ℙ0\mathbb{P}\_{0}.
Direct computations give

|  |  |  |
| --- | --- | --- |
|  | ∇bLT​(b,y)=LT​(b,y)​σ−T​(y−T​a​(b)).\nabla\_{b}L\_{T}(b,y)\;=\;L\_{T}(b,y)\,\sigma^{-T}\!\big(y-T\,a(b)\big). |  |

and

|  |  |  |
| --- | --- | --- |
|  | LT​(b,y)2​φT​(y)=exp⁡(T​‖a​(b)‖22)​φT​(y−2​T​a​(b)).L\_{T}(b,y)^{2}\,\varphi\_{T}(y)\;=\;\exp\!\big(T\|a(b)\|\_{2}^{2}\big)\;\varphi\_{T}\!\big(y-2T\,a(b)\big). |  |

By the Jensen inequality,

|  |  |  |
| --- | --- | --- |
|  | A​(y)=𝔼ℙ0​[e⟨a​(B),y⟩−T2​‖a​(B)‖22]≥exp⁡(⟨𝔼ℙ0​[a​(B)],y⟩−T2​𝔼ℙ0​[‖a​(B)‖22]).A(y)\;=\;\mathbb{E}\_{\mathbb{P}\_{0}}\big[e^{\langle a(B),y\rangle-\frac{T}{2}\|a(B)\|\_{2}^{2}}\big]\;\geq\;\exp\!\Big(\langle\mathbb{E}\_{\mathbb{P}\_{0}}[a(B)],y\rangle-\tfrac{T}{2}\,\mathbb{E}\_{\mathbb{P}\_{0}}\left[\|a(B)\|\_{2}^{2}\right]\Big). |  |

Raising to the negative power β<0\beta<0 reverses the inequality and gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(y)β≤Ca​exp⁡(β​⟨v,y⟩),Ca:=exp⁡(−β​T2​𝔼ℙ0​[‖a​(B)‖22]),v:=𝔼ℙ0​[a​(B)].A(y)^{\beta}\;\leq\;C\_{a}\,\exp\!\big(\beta\,\langle v,y\rangle\big),\qquad C\_{a}:=\exp\!\Big(-\tfrac{\beta T}{2}\,\mathbb{E}\_{\mathbb{P}\_{0}}\left[\|a(B)\|\_{2}^{2}\right]\Big),\ \ v:=\mathbb{E}\_{\mathbb{P}\_{0}}[a(B)]. |  | (48) |

Since

|  |  |  |
| --- | --- | --- |
|  | ‖∇bLT​(B,y)‖22=LT​(B,y)2​‖σ−T​(y−T​a​(B))‖22≤‖σ−1‖F2​LT​(B,y)2​‖y−T​a​(B)‖22,\|\nabla\_{b}L\_{T}(B,y)\|\_{2}^{2}=L\_{T}(B,y)^{2}\,\|\sigma^{-T}(y-Ta(B))\|\_{2}^{2}\leq\,\|\sigma^{-1}\|\_{F}^{2}\,L\_{T}(B,y)^{2}\,\|y-Ta(B)\|\_{2}^{2}, |  |

we use ‖u+v‖22≤2​(‖u‖22+‖v‖22)\|u+v\|\_{2}^{2}\leq 2(\|u\|\_{2}^{2}+\|v\|\_{2}^{2}) and have

|  |  |  |
| --- | --- | --- |
|  | ‖∇bLT​(B,y)‖22≤C​‖σ−1‖F2​LT​(B,y)2​(1+‖y‖22+T2​‖a​(B)‖22),\|\nabla\_{b}L\_{T}(B,y)\|\_{2}^{2}\;\leq\;C\,\|\sigma^{-1}\|\_{F}^{2}\,L\_{T}(B,y)^{2}\,\big(1+\|y\|\_{2}^{2}+T^{2}\|a(B)\|\_{2}^{2}\big), |  |

where C>0C>0 is a constant (we use CC to absorb constants if there is no confusion). Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∫ℝdA​(y)β​𝔼ℙ0​[‖∇bLT​(B,y)‖22]​φT​(y)​𝑑y\displaystyle\int\_{\mathbb{R}^{d}}A(y)^{\beta}\,\mathbb{E}\_{\mathbb{P}\_{0}}\big[\|\nabla\_{b}L\_{T}(B,y)\|\_{2}^{2}\big]\;\varphi\_{T}(y)\,dy |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​‖σ−1‖F2​𝔼ℙ0​[∫ℝdLT​(B,y)2​(1+‖y‖22+T2​‖a​(B)‖22)​eβ​⟨v,y⟩​φT​(y)​𝑑y]\displaystyle\ \ \leq\ C\,\|\sigma^{-1}\|\_{F}^{2}\,\mathbb{E}\_{\mathbb{P}\_{0}}\!\Big[\int\_{\mathbb{R}^{d}}L\_{T}(B,y)^{2}\,(1+\|y\|\_{2}^{2}+T^{2}\|a(B)\|\_{2}^{2})\,e^{\beta\langle v,y\rangle}\,\varphi\_{T}(y)\,dy\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =C​‖σ−1‖F2​𝔼ℙ0​[eT​‖a​(B)‖22​∫ℝd(1+‖y‖22+T2​‖a​(B)‖22)​eβ​⟨v,y⟩​φT​(y−2​T​a​(B))​𝑑y].\displaystyle\ \ =\ C\,\|\sigma^{-1}\|\_{F}^{2}\,\mathbb{E}\_{\mathbb{P}\_{0}}\!\Big[e^{T\|a(B)\|\_{2}^{2}}\int\_{\mathbb{R}^{d}}(1+\|y\|\_{2}^{2}+T^{2}\|a(B)\|\_{2}^{2})\,e^{\beta\langle v,y\rangle}\,\varphi\_{T}\!\big(y-2Ta(B)\big)\,dy\Big]. |  |

The inner integral is

|  |  |  |
| --- | --- | --- |
|  | ∫ℝd(1+‖y‖22+T2​‖a​(B)‖22)​eβ​⟨v,y⟩​φT​(y−2​T​a​(B))​𝑑y\displaystyle\int\_{\mathbb{R}^{d}}\bigl(1+\|y\|\_{2}^{2}+T^{2}\|a(B)\|\_{2}^{2}\bigr)\,e^{\beta\langle v,y\rangle}\,\varphi\_{T}\bigl(y-2T\,a(B)\bigr)\,dy |  |
|  |  |  |
| --- | --- | --- |
|  | =exp⁡(2​T​β​⟨v,a​(B)⟩+T2​‖β​v‖22)​[ 1+T​d+‖2​T​a​(B)+T​β​v‖22+T2​‖a​(B)‖22].\displaystyle=\exp\!\Big(2T\beta\,\langle v,a(B)\rangle+\tfrac{T}{2}\|\beta v\|\_{2}^{2}\Big)\,\Big[\,1+Td+\|2Ta(B)+T\beta v\|\_{2}^{2}+T^{2}\|a(B)\|\_{2}^{2}\,\Big]. |  |

For a fixed ε>0\varepsilon>0 (which will be chosen later), by the Young inequality,

|  |  |  |
| --- | --- | --- |
|  | 2​T​β​⟨v,a​(B)⟩≤2​T​β​|⟨v,a​(B)⟩|≤ε​‖a​(B)‖22+T2​β2​‖v‖22ε.2T\beta\,\langle v,a(B)\rangle\leq 2T\beta\,\left|\langle v,a(B)\rangle\right|\leq\varepsilon\left\|a(B)\right\|\_{2}^{2}+\frac{T^{2}\beta^{2}\left\|v\right\|\_{2}^{2}}{\varepsilon}. |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | e 2​T​β​⟨v,a​(B)⟩+T2​‖β​v‖22≤Ctilt​(ε)​eε​‖a​(B)‖22,e^{\,2T\beta\langle v,a(B)\rangle+\frac{T}{2}\|\beta v\|\_{2}^{2}}\leq C\_{\mathrm{tilt}}(\varepsilon)\,e^{\,\varepsilon\|a(B)\|\_{2}^{2}}, |  |

with

|  |  |  |
| --- | --- | --- |
|  | Ctilt​(ε):=exp⁡(T2​‖β​v‖22+T2​β2​‖v‖22ε).C\_{\mathrm{tilt}}(\varepsilon):=\exp\!\Big(\tfrac{T}{2}\|\beta v\|\_{2}^{2}+\tfrac{T^{2}\beta^{2}\|v\|\_{2}^{2}}{\varepsilon}\Big). |  |

Using the Young inequality in the quadratic bracket, we have

|  |  |  |
| --- | --- | --- |
|  | ‖2​T​a+T​β​v‖22≤(1+ε)​(2​T)2​‖a‖22+(1+1ε)​T2​β2​‖v‖22,\|2Ta+T\beta v\|\_{2}^{2}\leq(1+\varepsilon)\,(2T)^{2}\|a\|\_{2}^{2}+\Big(1+\tfrac{1}{\varepsilon}\Big)T^{2}\beta^{2}\|v\|\_{2}^{2}, |  |

and further get

|  |  |  |
| --- | --- | --- |
|  | 1+T​d+‖2​T​a​(B)+T​β​v‖22+T2​‖a​(B)‖22≤C0​(ε)+C1​(ε)​‖a​(B)‖22,1+Td+\|2Ta(B)+T\beta v\|\_{2}^{2}+T^{2}\|a(B)\|\_{2}^{2}\leq C\_{0}(\varepsilon)+C\_{1}(\varepsilon)\,\|a(B)\|\_{2}^{2}, |  |

where C0​(ε):=1+T​d+(1+1ε)​T2​β2​‖v‖22,C\_{0}(\varepsilon):=1+Td+\Big(1+\tfrac{1}{\varepsilon}\Big)T^{2}\beta^{2}\|v\|\_{2}^{2}, and C1​(ε):=T2​(5+4​ε).C\_{1}(\varepsilon):=T^{2}\big(5+4\varepsilon\big).
Therefore, the inner integral is upper bounded by
Ctilt​(ε)​(C0​(ε)+C1​(ε)​‖a​(B)‖22)​eε​‖a​(B)‖22.C\_{\mathrm{tilt}}(\varepsilon)\,\bigl(C\_{0}(\varepsilon)+C\_{1}(\varepsilon)\,\|a(B)\|\_{2}^{2}\bigr)\,e^{\,\varepsilon\|a(B)\|\_{2}^{2}}.

Therefore, there exists a constant C>0C>0 such that

|  |  |  |
| --- | --- | --- |
|  | ∫ℝdA​(y)β​𝔼ℙ0​[‖∇bLT​(B,y)‖22]​φT​(y)​𝑑y\displaystyle\int\_{\mathbb{R}^{d}}A(y)^{\beta}\,\mathbb{E}\_{\mathbb{P}\_{0}}\big[\|\nabla\_{b}L\_{T}(B,y)\|\_{2}^{2}\big]\;\varphi\_{T}(y)\,dy |  |
|  |  |  |
| --- | --- | --- |
|  | ≤C​‖σ−1‖F2​Ctilt​(ε)​𝔼ℙ0​[(C0​(ε)+C1​(ε)​‖a​(B)‖22)​e(T+ε)​‖a​(B)‖22].\displaystyle\leq C\,\|\sigma^{-1}\|\_{F}^{2}\,C\_{\mathrm{tilt}}(\varepsilon)\;\mathbb{E}\_{\mathbb{P}\_{0}}\!\Big[\bigl(C\_{0}(\varepsilon)+C\_{1}(\varepsilon)\|a(B)\|\_{2}^{2}\bigr)\,e^{\,(T+\varepsilon)\|a(B)\|\_{2}^{2}}\Big]. |  |

Let

|  |  |  |
| --- | --- | --- |
|  | ε∗:=12(γ022​‖σ−1‖F2−T)(well-defined and >0 if γ02>2T∥σ−1∥F2).\varepsilon\_{\*}:=\tfrac{1}{2}\!\left(\frac{\gamma\_{0}^{2}}{2\|\sigma^{-1}\|\_{F}^{2}}-T\right)\quad\text{(well-defined and $>0$ if }\penalty 10000\ \gamma\_{0}^{2}>2T\|\sigma^{-1}\|\_{F}^{2}). |  |

Since a​(B)=σ−1​B−ma(B)=\sigma^{-1}B-m, we have ‖a​(B)‖22≤2​‖σ−1‖F2​‖B‖22+2​‖m‖22\|a(B)\|\_{2}^{2}\leq 2\|\sigma^{-1}\|\_{F}^{2}\|B\|\_{2}^{2}+2\|m\|\_{2}^{2}. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | (C0​(ε∗)+C1​(ε∗)​‖a​(B)‖22)​e(T+ε∗)​‖a​(B)‖22≤Km​(1+c​‖B‖22)​eC′​‖B‖22,\bigl(C\_{0}(\varepsilon\_{\*})+C\_{1}(\varepsilon\_{\*})\|a(B)\|\_{2}^{2}\bigr)\,e^{\,(T+\varepsilon\_{\*})\|a(B)\|\_{2}^{2}}\;\leq\;K\_{m}\,(1+c\|B\|\_{2}^{2})\,e^{\,C^{\prime}\|B\|\_{2}^{2}}, |  | (49) |

for constants Km,c>0K\_{m},c>0 and

|  |  |  |
| --- | --- | --- |
|  | C′:=2​(T+ε∗)​‖σ−1‖F2=T​‖σ−1‖F2+γ022<γ02.C^{\prime}:=2\,(T+\varepsilon\_{\*})\,\|\sigma^{-1}\|\_{F}^{2}=T\|\sigma^{-1}\|\_{F}^{2}+\frac{\gamma\_{0}^{2}}{2}\;<\gamma\_{0}^{2}. |  |

To see ([49](https://arxiv.org/html/2512.01408v1#A3.E49 "In Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")), recall that a​(B)=σ−1​B−ma(B)=\sigma^{-1}B-m, and denote

|  |  |  |
| --- | --- | --- |
|  | κ1:=2​‖σ−1‖F2,κ0:=2​‖m‖22.\kappa\_{1}:=2\,\|\sigma^{-1}\|\_{F}^{2},\qquad\kappa\_{0}:=2\,\|m\|\_{2}^{2}. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | ‖a​(B)‖22=‖σ−1​B−m‖22≤ 2​‖σ−1​B‖22+2​‖m‖22≤κ1​‖B‖22+κ0,\|a(B)\|\_{2}^{2}\;=\;\|\sigma^{-1}B-m\|\_{2}^{2}\;\leq\;2\|\sigma^{-1}B\|\_{2}^{2}+2\|m\|\_{2}^{2}\;\leq\;\kappa\_{1}\|B\|\_{2}^{2}+\kappa\_{0}, |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | (T+ε∗)​‖a​(B)‖22\displaystyle(T+\varepsilon\_{\*})\|a(B)\|\_{2}^{2} | ≤(T+ε∗)​(κ1​‖B‖22+κ0)=2​(T+ε∗)​‖σ−1‖F2⏟=⁣:C′​‖B‖22+ 2​(T+ε∗)​‖m‖22,\displaystyle\leq(T+\varepsilon\_{\*})\big(\kappa\_{1}\|B\|\_{2}^{2}+\kappa\_{0}\big)=\underbrace{2(T+\varepsilon\_{\*})\|\sigma^{-1}\|\_{F}^{2}}\_{=:\penalty 10000\ C^{\prime}}\|B\|\_{2}^{2}\;+\;2(T+\varepsilon\_{\*})\|m\|\_{2}^{2}, |  |

where
C′=2​(T+ε∗)​‖σ−1‖F2=T​‖σ−1‖F2+γ022<γ02.C^{\prime}=2(T+\varepsilon\_{\*})\|\sigma^{-1}\|\_{F}^{2}=T\|\sigma^{-1}\|\_{F}^{2}+\frac{\gamma\_{0}^{2}}{2}\;<\;\gamma\_{0}^{2}.
Hence,

|  |  |  |
| --- | --- | --- |
|  | e(T+ε∗)​‖a​(B)‖22≤e 2​(T+ε∗)​‖m‖22​eC′​‖B‖22.e^{(T+\varepsilon\_{\*})\|a(B)\|\_{2}^{2}}\;\leq\;e^{\,2(T+\varepsilon\_{\*})\|m\|\_{2}^{2}}\;e^{\,C^{\prime}\|B\|\_{2}^{2}}. |  |

For the polynomial prefactor,

|  |  |  |  |
| --- | --- | --- | --- |
|  | C0​(ε∗)+C1​(ε∗)​‖a​(B)‖22\displaystyle C\_{0}(\varepsilon\_{\*})+C\_{1}(\varepsilon\_{\*})\|a(B)\|\_{2}^{2} | ≤C0​(ε∗)+C1​(ε∗)​(κ1​‖B‖22+κ0)\displaystyle\leq C\_{0}(\varepsilon\_{\*})+C\_{1}(\varepsilon\_{\*})\big(\kappa\_{1}\|B\|\_{2}^{2}+\kappa\_{0}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(C0​(ε∗)+C1​(ε∗)​κ0)⏟=⁣:K1+C1​(ε∗)​κ1⏟=⁣:K2​‖B‖22\displaystyle=\underbrace{\big(C\_{0}(\varepsilon\_{\*})+C\_{1}(\varepsilon\_{\*})\kappa\_{0}\big)}\_{=:\penalty 10000\ K\_{1}}\;+\;\underbrace{C\_{1}(\varepsilon\_{\*})\kappa\_{1}}\_{=:\penalty 10000\ K\_{2}}\,\|B\|\_{2}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =K1​(1+K2K1​‖B‖22)=K1​(1+c​‖B‖22),\displaystyle=K\_{1}\Big(1+\frac{K\_{2}}{K\_{1}}\,\|B\|\_{2}^{2}\Big)=K\_{1}\big(1+c\,\|B\|\_{2}^{2}\big), |  |

where

|  |  |  |
| --- | --- | --- |
|  | c:=C1​(ε∗)​κ1C0​(ε∗)+C1​(ε∗)​κ0> 0.c:=\frac{C\_{1}(\varepsilon\_{\*})\kappa\_{1}}{C\_{0}(\varepsilon\_{\*})+C\_{1}(\varepsilon\_{\*})\kappa\_{0}}\;>\;0. |  |

Therefore, we get ([49](https://arxiv.org/html/2512.01408v1#A3.E49 "In Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) with

|  |  |  |
| --- | --- | --- |
|  | Km:=K1​e 2​(T+ε∗)​‖m‖22=(C0​(ε∗)+C1​(ε∗)​κ0)​e 2​(T+ε∗)​‖m‖22.K\_{m}\;:=\;K\_{1}\,e^{\,2(T+\varepsilon\_{\*})\|m\|\_{2}^{2}}\;=\;\big(C\_{0}(\varepsilon\_{\*})+C\_{1}(\varepsilon\_{\*})\kappa\_{0}\big)\,e^{\,2(T+\varepsilon\_{\*})\|m\|\_{2}^{2}}. |  |

Since C′<γ02C^{\prime}<\gamma\_{0}^{2}, we pick any γ\gamma such that C′<γ2<γ02C^{\prime}<\gamma^{2}<\gamma\_{0}^{2}.
For t≥0t\geq 0 and δ:=γ2−C′>0\delta:=\gamma^{2}-C^{\prime}>0, the elementary bound

|  |  |  |
| --- | --- | --- |
|  | 1+c​t≤(1+ce​δ)​eδ​t1+ct\;\leq\;\Big(1+\frac{c}{e\,\delta}\Big)\,e^{\delta t} |  |

implies

|  |  |  |
| --- | --- | --- |
|  | (1+c​‖B‖22)​eC′​‖B‖22≤K​eγ2​‖B‖22,K:=1+ce​(γ2−C′).(1+c\,\|B\|\_{2}^{2})\,e^{\,C^{\prime}\|B\|\_{2}^{2}}\;\leq\;K\,e^{\,\gamma^{2}\|B\|\_{2}^{2}},\qquad K:=1+\frac{c}{e(\gamma^{2}-C^{\prime})}. |  |

Therefore, under the sub-Gaussian assumption
𝔼ℙ0​[eγ2​‖B‖22]<∞\mathbb{E}\_{\mathbb{P}\_{0}}\big[e^{\gamma^{2}\|B\|\_{2}^{2}}\big]<\infty for all γ<γ0\gamma<\gamma\_{0},

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ0​[(C0​(ε∗)+C1​(ε∗)​‖a​(B)‖22)​e(T+ε∗)​‖a​(B)‖22]≤Km​K​𝔼ℙ0​[eγ2​‖B‖22]<∞.\mathbb{E}\_{\mathbb{P}\_{0}}\!\Big[\bigl(C\_{0}(\varepsilon\_{\*})+C\_{1}(\varepsilon\_{\*})\|a(B)\|\_{2}^{2}\bigr)\,e^{(T+\varepsilon\_{\*})\|a(B)\|\_{2}^{2}}\Big]\;\leq\;K\_{m}\,K\,\mathbb{E}\_{\mathbb{P}\_{0}}\big[e^{\gamma^{2}\|B\|\_{2}^{2}}\big]\;<\;\infty. |  |

In order to show the well-definedness of HH, we need to show

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝdA​(y)β​φT​(y)​𝑑y<∞\int\_{\mathbb{R}^{d}}A(y)^{\beta}\varphi\_{T}(y)dy<\infty |  | (50) |

since from the Cauchy-Schwarz inequality, for ℙ0\mathbb{P}\_{0} almost every bb,

|  |  |  |
| --- | --- | --- |
|  | ‖H​(b)‖2≤11−α​∫ℝdA​(y)β​‖∇bLT​(b,y)‖2​φT​(y)​𝑑y\displaystyle\left\|H(b)\right\|\_{2}\leq\frac{1}{1-\alpha}\int\_{\mathbb{R}^{d}}A(y)^{\beta}\left\|\nabla\_{b}L\_{T}(b,y)\right\|\_{2}\,\,\varphi\_{T}(y)\,dy |  |
|  |  |  |
| --- | --- | --- |
|  | ≤11−α​(∫ℝd‖∇bLT​(b,y)‖22​A​(y)β​φT​(y)​𝑑y)12​(∫ℝdA​(y)β​φT​(y)​𝑑y)12,\displaystyle\leq\frac{1}{1-\alpha}\left(\int\_{\mathbb{R}^{d}}\left\|\nabla\_{b}L\_{T}(b,y)\right\|\_{2}^{2}A(y)^{\beta}\,\varphi\_{T}(y)dy\right)^{\frac{1}{2}}\left(\int\_{\mathbb{R}^{d}}A(y)^{\beta}\,\varphi\_{T}(y)dy\right)^{\frac{1}{2}}, |  |

where the first term is finite ℙ0\mathbb{P}\_{0} almost surely. If we take square and then take expectation with respect to ℙ0\mathbb{P}\_{0} and use Tonelli’s theorem, then the proof is complete.

When α<0\alpha<0, we recall Eq. ([48](https://arxiv.org/html/2512.01408v1#A3.E48 "In Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) and have

|  |  |  |
| --- | --- | --- |
|  | ∫ℝdA​(y)β​φT​(y)​𝑑y≤Ca​∫ℝdeβ​⟨v,y⟩​φT​(y)​𝑑y.\int\_{\mathbb{R}^{d}}A(y)^{\beta}\,\varphi\_{T}(y)\,dy\;\leq\;C\_{a}\int\_{\mathbb{R}^{d}}e^{\beta\langle v,y\rangle}\,\varphi\_{T}(y)\,dy. |  |

Completion of squares gives

|  |  |  |
| --- | --- | --- |
|  | ∫ℝdeβ​⟨v,y⟩​φT​(y)​𝑑y=(2​π​T)−d/2​∫ℝdexp⁡(β​⟨v,y⟩−‖y‖222​T)​𝑑y=exp⁡(T2​‖β​v‖22).\int\_{\mathbb{R}^{d}}e^{\beta\langle v,y\rangle}\,\varphi\_{T}(y)\,dy=(2\pi T)^{-d/2}\!\!\int\_{\mathbb{R}^{d}}\exp\!\left(\beta\langle v,y\rangle-\frac{\|y\|\_{2}^{2}}{2T}\right)dy=\exp\!\left(\frac{T}{2}\|\beta v\|\_{2}^{2}\right). |  |

Indeed,

|  |  |  |
| --- | --- | --- |
|  | β​⟨v,y⟩−‖y‖222​T=−12​T​‖y−T​β​v‖22+T2​‖β​v‖22.\beta\langle v,y\rangle-\frac{\|y\|\_{2}^{2}}{2T}=-\frac{1}{2T}\Big\|\,y-T\beta v\,\Big\|\_{2}^{2}+\frac{T}{2}\|\beta v\|\_{2}^{2}. |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | ∫ℝdA​(y)β​φT​(y)​𝑑y≤Ca​exp⁡(T2​‖β​v‖22)<∞,∎\int\_{\mathbb{R}^{d}}A(y)^{\beta}\,\varphi\_{T}(y)\,dy\;\leq\;C\_{a}\,\exp\!\left(\frac{T}{2}\|\beta v\|\_{2}^{2}\right)<\infty,\qed |  |

which finishes the proof of the case when α<0\alpha<0.
Next we divide the positive α\alpha into two cases.

*Case 1: 0<β≤10<\beta\leq 1 (equivalently 0<α≤120<\alpha\leq\tfrac{1}{2}).*
Let μ​(d​y):=φT​(y)​d​y\mu(dy):=\varphi\_{T}(y)\,dy; then μ\mu is a probability measure since
∫ℝdφT​(y)​𝑑y=1\int\_{\mathbb{R}^{d}}\varphi\_{T}(y)\,dy=1. Set f​(y):=A​(y)=𝔼​[LT​(B,y)]≥0f(y):=A(y)=\mathbb{E}[L\_{T}(B,y)]\geq 0 and

|  |  |  |
| --- | --- | --- |
|  | ϕ​(x):=xβ,x≥0.\phi(x):=x^{\beta},\qquad x\geq 0. |  |

For 0<β≤10<\beta\leq 1, the map ϕ\phi is concave and increasing, so the Jensen
inequality for concave functions gives

|  |  |  |
| --- | --- | --- |
|  | ϕ​(∫ℝdf​(y)​μ​(d​y))≥∫ℝdϕ​(f​(y))​μ​(d​y),\phi\!\left(\int\_{\mathbb{R}^{d}}f(y)\,\mu(dy)\right)\;\geq\;\int\_{\mathbb{R}^{d}}\phi(f(y))\,\mu(dy), |  |

i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝdA​(y)β​φT​(y)​𝑑y≤(∫ℝdA​(y)​φT​(y)​𝑑y)β.\int\_{\mathbb{R}^{d}}A(y)^{\beta}\,\varphi\_{T}(y)\,dy\;\leq\;\Big(\int\_{\mathbb{R}^{d}}A(y)\,\varphi\_{T}(y)\,dy\Big)^{\beta}. |  | (51) |

It remains to compute ∫ℝdA​(y)​φT​(y)​𝑑y\int\_{\mathbb{R}^{d}}A(y)\,\varphi\_{T}(y)\,dy. By the Fubini theorem,

|  |  |  |
| --- | --- | --- |
|  | ∫ℝdA​(y)​φT​(y)​𝑑y=𝔼ℙ0​[∫ℝdLT​(B,y)​φT​(y)​𝑑y]=1\int\_{\mathbb{R}^{d}}A(y)\,\varphi\_{T}(y)\,dy=\mathbb{E}\_{\mathbb{P}\_{0}}\!\left[\int\_{\mathbb{R}^{d}}L\_{T}(B,y)\,\varphi\_{T}(y)\,dy\right]=1 |  |

from a completion of squares argument. Thus, plugging into ([51](https://arxiv.org/html/2512.01408v1#A3.E51 "In Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) yields the bound

|  |  |  |
| --- | --- | --- |
|  | ∫ℝdA​(y)β​φT​(y)​𝑑y≤ 1,0<β≤1.\ \int\_{\mathbb{R}^{d}}A(y)^{\beta}\,\varphi\_{T}(y)\,dy\;\leq\;1,\qquad 0<\beta\leq 1.\ |  |

*Case 2: β>1\beta>1 (equivalently 12<α<1\tfrac{1}{2}<\alpha<1).*
Since the map x↦xβx\mapsto x^{\beta} is convex on (0,∞)(0,\infty), the Jensen inequality yields

|  |  |  |
| --- | --- | --- |
|  | A​(y)β=(𝔼ℙ0​[LT​(B,y)])β≤𝔼ℙ0​[LT​(B,y)β].A(y)^{\beta}=\big(\mathbb{E}\_{\mathbb{P}\_{0}}[L\_{T}(B,y)]\big)^{\beta}\leq\mathbb{E}\_{\mathbb{P}\_{0}}\big[L\_{T}(B,y)^{\beta}\big]. |  |

Integrating and exchanging expectation and integral,

|  |  |  |
| --- | --- | --- |
|  | ∫ℝdA​(y)β​φT​(y)​𝑑y≤𝔼ℙ0​[∫ℝdLT​(B,y)β​φT​(y)​𝑑y].\int\_{\mathbb{R}^{d}}A(y)^{\beta}\,\varphi\_{T}(y)\,dy\;\leq\;\mathbb{E}\_{\mathbb{P}\_{0}}\!\left[\int\_{\mathbb{R}^{d}}L\_{T}(B,y)^{\beta}\,\varphi\_{T}(y)\,dy\right]. |  |

For fixed bb, completing the square gives

|  |  |  |
| --- | --- | --- |
|  | ∫ℝdLT​(b,y)β​φT​(y)​𝑑y=exp⁡(T2​(β2−β)​‖a​(b)‖22).\int\_{\mathbb{R}^{d}}L\_{T}(b,y)^{\beta}\,\varphi\_{T}(y)\,dy=\exp\!\left(\frac{T}{2}(\beta^{2}-\beta)\,\|a(b)\|\_{2}^{2}\right). |  |

Therefore

|  |  |  |
| --- | --- | --- |
|  | ∫ℝdA​(y)β​φT​(y)​𝑑y≤𝔼ℙ0​[exp⁡(T2​(β2−β)​‖a​(B)‖22)].\int\_{\mathbb{R}^{d}}A(y)^{\beta}\,\varphi\_{T}(y)\,dy\;\leq\;\mathbb{E}\_{\mathbb{P}\_{0}}\!\left[\exp\!\left(\frac{T}{2}(\beta^{2}-\beta)\,\|a(B)\|\_{2}^{2}\right)\right]. |  |

Using ‖a​(B)‖22≤2​‖σ−1‖F2​‖B‖22+2​‖m‖22\|a(B)\|\_{2}^{2}\leq 2\|\sigma^{-1}\|\_{F}^{2}\,\|B\|\_{2}^{2}+2\|m\|\_{2}^{2}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝdA​(y)β​φT​(y)​𝑑y≤exp⁡(T​(β2−β)​‖m‖22)​𝔼ℙ0​[exp⁡(T​(β2−β)​‖σ−1‖F2​‖B‖22)].\int\_{\mathbb{R}^{d}}A(y)^{\beta}\,\varphi\_{T}(y)\,dy\;\leq\;\exp\!\Big(T(\beta^{2}-\beta)\,\|m\|\_{2}^{2}\Big)\;\mathbb{E}\_{\mathbb{P}\_{0}}\!\left[\exp\!\Big(T(\beta^{2}-\beta)\,\|\sigma^{-1}\|\_{F}^{2}\,\|B\|\_{2}^{2}\Big)\right]. |  | (52) |

Hence, under the sub-Gaussian moment assumption

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ0​[eγ2​‖B‖22]<∞for all ​γ<γ0,\mathbb{E}\_{\mathbb{P}\_{0}}\!\left[e^{\gamma^{2}\|B\|\_{2}^{2}}\right]<\infty\quad\text{for all }\gamma<\gamma\_{0}, |  |

the right-hand side of Eq. ([52](https://arxiv.org/html/2512.01408v1#A3.E52 "In Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) is finite whenever

|  |  |  |  |
| --- | --- | --- | --- |
|  | T​(β2−β)​‖σ−1‖F2<γ02.\ T(\beta^{2}-\beta)\,\|\sigma^{-1}\|\_{F}^{2}\;<\;\gamma\_{0}^{2}. |  | (53) |

Next, we focus on the bound when α∈(0,1)\alpha\in(0,1).
Define

|  |  |  |
| --- | --- | --- |
|  | ℐβ:=∫ℝdA​(y)β​𝔼ℙ0​[‖∇bLT​(B,y)‖22]​φT​(y)​𝑑y.\mathcal{I}\_{\beta}\;:=\;\int\_{\mathbb{R}^{d}}A(y)^{\beta}\,\mathbb{E}\_{\mathbb{P}\_{0}}\!\big[\|\nabla\_{b}L\_{T}(B,y)\|\_{2}^{2}\big]\;\varphi\_{T}(y)\,dy. |  |

We first consider the case when β∈(0,1)\beta\in(0,1).
Write
G​(y):=𝔼ℙ0​[‖∇bLT​(B,y)‖22].G(y):=\mathbb{E}\_{\mathbb{P}\_{0}}\!\big[\|\nabla\_{b}L\_{T}(B,y)\|\_{2}^{2}\big].
Then
ℐβ=∫ℝdA​(y)β​G​(y)​φT​(y)​𝑑y.\mathcal{I}\_{\beta}=\int\_{\mathbb{R}^{d}}A(y)^{\beta}\,G(y)\,\varphi\_{T}(y)\,dy.
By the Hölder inequality with exponents p=1βp=\frac{1}{\beta} and q=11−βq=\frac{1}{1-\beta}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐβ=∫ℝd(A​(y)​G​(y))β​G​(y)1−β​φT​(y)​𝑑y≤(∫ℝdA​(y)​G​(y)​φT​(y)​𝑑y)β​(∫ℝdG​(y)​φT​(y)​𝑑y)1−β.\mathcal{I}\_{\beta}=\int\_{\mathbb{R}^{d}}\big(A(y)G(y)\big)^{\beta}\,G(y)^{1-\beta}\,\varphi\_{T}(y)\,dy\;\leq\;\Big(\int\_{\mathbb{R}^{d}}A(y)\,G(y)\,\varphi\_{T}(y)\,dy\Big)^{\!\beta}\Big(\int\_{\mathbb{R}^{d}}G(y)\,\varphi\_{T}(y)\,dy\Big)^{\!1-\beta}. |  | (54) |

Set

|  |  |  |
| --- | --- | --- |
|  | I0:=∫ℝdG​(y)​φT​(y)​𝑑y,I1:=∫ℝdA​(y)​G​(y)​φT​(y)​𝑑y.I\_{0}:=\int\_{\mathbb{R}^{d}}G(y)\,\varphi\_{T}(y)\,dy,\qquad I\_{1}:=\int\_{\mathbb{R}^{d}}A(y)\,G(y)\,\varphi\_{T}(y)\,dy. |  |

It suffices to show I0<∞I\_{0}<\infty and I1<∞I\_{1}<\infty under some sub-Gaussian assumptions.

Recall that there exists a constant C>0C>0 such that

|  |  |  |
| --- | --- | --- |
|  | ‖∇bLT​(B,y)‖22≤C​‖σ−1‖F2​LT​(B,y)2​(1+‖y‖22+T2​‖a​(B)‖22).\|\nabla\_{b}L\_{T}(B,y)\|\_{2}^{2}\;\leq\;C\,\|\sigma^{-1}\|\_{F}^{2}\,L\_{T}(B,y)^{2}\,(1+\|y\|\_{2}^{2}+T^{2}\|a(B)\|\_{2}^{2}). |  |

Using the Tonelli theorem,

|  |  |  |  |
| --- | --- | --- | --- |
|  | I0\displaystyle I\_{0} | ≤C​‖σ−1‖F2​𝔼ℙ0​[eT​‖a​(B)‖22​∫ℝd(1+‖y‖22+T2​‖a​(B)‖22)​φT​(y−2​T​a​(B))​𝑑y].\displaystyle\leq C\,\|\sigma^{-1}\|\_{F}^{2}\,\mathbb{E}^{\mathbb{P}\_{0}}\!\Big[e^{T\|a(B)\|\_{2}^{2}}\!\!\int\_{\mathbb{R}^{d}}\!(1+\|y\|\_{2}^{2}+T^{2}\|a(B)\|\_{2}^{2})\,\varphi\_{T}(y-2Ta(B))\,dy\Big]. |  |

For the inner integral,
fix a∈ℝda\in\mathbb{R}^{d} and set the notation

|  |  |  |
| --- | --- | --- |
|  | J​(a):=∫ℝd(1+‖y‖22+T2​‖a‖22)​φT​(y−2​T​a)​𝑑y.J(a):=\int\_{\mathbb{R}^{d}}\bigl(1+\|y\|\_{2}^{2}+T^{2}\|a\|\_{2}^{2}\bigr)\,\varphi\_{T}(y-2Ta)\,dy. |  |

Let Z∼𝒩​(0,T​Id)Z\sim\mathcal{N}(0,TI\_{d}). Since φT​(y−2​T​a)​d​y\varphi\_{T}(y-2Ta)\,dy is the law of Y:=Z+2​T​aY:=Z+2Ta, we have

|  |  |  |
| --- | --- | --- |
|  | J​(a)=𝔼​[1+‖Y‖22+T2​‖a‖22]=1+𝔼​[‖Z+2​T​a‖22]+T2​‖a‖22=1+d​T+5​T2​‖a‖22.J(a)=\mathbb{E}\!\left[1+\|Y\|\_{2}^{2}+T^{2}\|a\|\_{2}^{2}\right]=1+\mathbb{E}\left[\|Z+2Ta\|\_{2}^{2}\right]+T^{2}\|a\|\_{2}^{2}=1+dT+5T^{2}\|a\|\_{2}^{2}. |  |

With a=a​(B)a=a(B), the inner integral in I0I\_{0} equals 1+d​T+5​T2​‖a​(B)‖221+dT+5T^{2}\|a(B)\|\_{2}^{2}, and therefore

|  |  |  |
| --- | --- | --- |
|  | I0≤C​‖σ−1‖F2​𝔼ℙ0​[eT​‖a​(B)‖22​(1+d​T+5​T2​‖a​(B)‖22)].I\_{0}\leq C\,\|\sigma^{-1}\|\_{F}^{2}\,\mathbb{E}\_{\mathbb{P}\_{0}}\!\Big[e^{T\|a(B)\|\_{2}^{2}}\big(1+dT+5T^{2}\|a(B)\|\_{2}^{2}\big)\Big]. |  |

The estimate for I0I\_{0} requires

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ0​[exp⁡(T​‖a​(B)‖22)]<∞,\mathbb{E}\_{\mathbb{P}\_{0}}\!\left[\exp\!\big(T\|a(B)\|\_{2}^{2}\big)\right]<\infty, |  |

which is actually a sub-Gaussian assumption on BB with condition

|  |  |  |
| --- | --- | --- |
|  | 2​T​‖σ−1‖F2<γ02.2T\,\|\sigma^{-1}\|\_{F}^{2}\;<\;\gamma\_{0}^{2}. |  |

Next, we upper bound I1I\_{1}. By the Young inequality ⟨u,v⟩≤ε2​‖u‖22+12​ε​‖v‖22\langle u,v\rangle\leq\tfrac{\varepsilon}{2}\|u\|\_{2}^{2}+\tfrac{1}{2\varepsilon}\|v\|\_{2}^{2} with a fixed ε>0\varepsilon>0 (which will be chosen later),

|  |  |  |
| --- | --- | --- |
|  | A​(y)≤𝔼ℙ0​[e−T−ε2​‖a​(B)‖22]​exp⁡(‖y‖222​ε)=CA​(ε)​ec​‖y‖22,c:=12​ε∈(0,12​T).A(y)\;\leq\;\mathbb{E}\_{\mathbb{P}\_{0}}\!\Big[e^{-\frac{T-\varepsilon}{2}\|a(B)\|\_{2}^{2}}\Big]\;\exp\!\Big(\frac{\|y\|\_{2}^{2}}{2\varepsilon}\Big)\;=\;C\_{A}(\varepsilon)\,e^{c\|y\|\_{2}^{2}},\qquad c:=\frac{1}{2\varepsilon}\in\Big(0,\frac{1}{2T}\Big). |  |

Here CA​(ε)=𝔼ℙ0​[eε−T2​‖a​(B)‖22]C\_{A}(\varepsilon)=\mathbb{E}\_{\mathbb{P}\_{0}}\!\big[e^{\frac{\varepsilon-T}{2}\|a(B)\|\_{2}^{2}}\big].
Hence, by the Tonelli theorem,

|  |  |  |  |
| --- | --- | --- | --- |
|  | I1\displaystyle I\_{1} | ≤C​‖σ−1‖F2​CA​(ε)​𝔼ℙ0​[eT​‖a​(B)‖22​∫ℝd(1+‖y‖22+T2​‖a​(B)‖22)​ec​‖y‖22​φT​(y−2​T​a​(B))​𝑑y].\displaystyle\leq C\,\|\sigma^{-1}\|\_{F}^{2}\,C\_{A}(\varepsilon)\,\mathbb{E}^{\mathbb{P}\_{0}}\!\Big[e^{T\|a(B)\|\_{2}^{2}}\!\int\_{\mathbb{R}^{d}}(1+\|y\|\_{2}^{2}+T^{2}\|a(B)\|\_{2}^{2})e^{c\|y\|\_{2}^{2}}\varphi\_{T}(y-2Ta(B))\,dy\Big]. |  |

Fix a∈ℝda\in\mathbb{R}^{d} and c∈(0,12​T)c\in(0,\frac{1}{2T}). Let

|  |  |  |
| --- | --- | --- |
|  | Kc​(a):=∫ℝd(1+‖y‖22+T2​‖a‖22)​ec​‖y‖22​φT​(y−2​T​a)​𝑑y.K\_{c}(a):=\int\_{\mathbb{R}^{d}}\bigl(1+\|y\|\_{2}^{2}+T^{2}\|a\|\_{2}^{2}\bigr)\,e^{c\|y\|\_{2}^{2}}\,\varphi\_{T}(y-2Ta)\,dy. |  |

With Y∼𝒩​(2​T​a,T​Id)Y\sim\mathcal{N}(2Ta,TI\_{d}) we have Kc​(a)=𝔼​[(1+‖Y‖22+T2​‖a‖22)​ec​‖Y‖22]K\_{c}(a)=\mathbb{E}[(1+\|Y\|\_{2}^{2}+T^{2}\|a\|\_{2}^{2})e^{c\|Y\|\_{2}^{2}}].
Define

|  |  |  |
| --- | --- | --- |
|  | F​(c,a):=∫ℝdec​‖y‖22​φT​(y−2​T​a)​𝑑y=(1−2​c​T)−d/2​exp⁡(4​T2​c1−2​c​T​‖a‖22).F(c,a):=\int\_{\mathbb{R}^{d}}e^{c\|y\|\_{2}^{2}}\,\varphi\_{T}(y-2Ta)\,dy=(1-2cT)^{-d/2}\exp\!\Big(\frac{4T^{2}c}{1-2cT}\,\|a\|\_{2}^{2}\Big). |  |

Then

|  |  |  |
| --- | --- | --- |
|  | ∂∂c​F​(c,a)=∫ℝd‖y‖22​ec​‖y‖22​φT​(y−2​T​a)​𝑑y=F​(c,a)​(d​T1−2​c​T+4​T2​‖a‖22(1−2​c​T)2),\frac{\partial}{\partial c}F(c,a)=\int\_{\mathbb{R}^{d}}\|y\|\_{2}^{2}e^{c\|y\|\_{2}^{2}}\varphi\_{T}(y-2Ta)\,dy=F(c,a)\!\left(\frac{dT}{1-2cT}+\frac{4T^{2}\|a\|\_{2}^{2}}{(1-2cT)^{2}}\right), |  |

so

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kc​(a)\displaystyle K\_{c}(a) | =(1+T2​‖a‖22)​F​(c,a)+∂∂c​F​(c,a)\displaystyle=(1+T^{2}\|a\|\_{2}^{2})\,F(c,a)+\frac{\partial}{\partial c}F(c,a) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =F​(c,a)​[1+T2​‖a‖22+d​T1−2​c​T+4​T2​‖a‖22(1−2​c​T)2]≤C1​(c,T,d)​(1+‖a‖22)​F​(c,a).\displaystyle=F(c,a)\!\left[1+T^{2}\|a\|\_{2}^{2}+\frac{dT}{1-2cT}+\frac{4T^{2}\|a\|\_{2}^{2}}{(1-2cT)^{2}}\right]\;\leq\;C\_{1}(c,T,d)\,\bigl(1+\|a\|\_{2}^{2}\bigr)\,F(c,a). |  |

Therefore, with c=12​ε∈(0,12​T)c=\frac{1}{2\varepsilon}\in(0,\frac{1}{2T}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | I1\displaystyle I\_{1} | ≤C​‖σ−1‖F2​CA​(ε)​𝔼ℙ0​[eT​‖a​(B)‖22​Kc​(a​(B))]\displaystyle\leq C\,\|\sigma^{-1}\|\_{F}^{2}\,C\_{A}(\varepsilon)\,\mathbb{E}\_{\mathbb{P}\_{0}}\!\Big[e^{T\|a(B)\|\_{2}^{2}}\,K\_{c}\big(a(B)\big)\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​(ε,T,d,σ)​𝔼ℙ0​[(1+‖a​(B)‖22)​exp⁡((T+2​T2ε−T)​‖a​(B)‖22)],\displaystyle\leq C(\varepsilon,T,d,\sigma)\,\mathbb{E}\_{\mathbb{P}\_{0}}\!\Big[(1+\|a(B)\|\_{2}^{2})\,\exp\!\Big(\Big(T+\frac{2T^{2}}{\varepsilon-T}\Big)\|a(B)\|\_{2}^{2}\Big)\Big], |  |

where

|  |  |  |
| --- | --- | --- |
|  | C​(ε,T,d,σ)=C​‖σ−1‖F2​CA​(ε)​(1−Tε)−d/2​(1+d​T1−Tε+T2+4​T2(1−Tε)2).C(\varepsilon,T,d,\sigma)=C\;\|\sigma^{-1}\|\_{F}^{2}\;C\_{A}(\varepsilon)\;\Big(1-\tfrac{T}{\varepsilon}\Big)^{-d/2}\left(1+\frac{dT}{1-\tfrac{T}{\varepsilon}}+T^{2}+\frac{4T^{2}}{\big(1-\tfrac{T}{\varepsilon}\big)^{2}}\right). |  |

To make the bound for I1I\_{1} finite, we only need an ε>T\varepsilon>T such that

|  |  |  |
| --- | --- | --- |
|  | ε−T2<γ022​‖σ−1‖F2andT+2​T2ε−T<γ022​‖σ−1‖F2.\frac{\varepsilon-T}{2}\;<\;\frac{\gamma\_{0}^{2}}{2\|\sigma^{-1}\|\_{F}^{2}}\qquad\text{and}\qquad T+\frac{2T^{2}}{\varepsilon-T}\;<\;\frac{\gamma\_{0}^{2}}{2\|\sigma^{-1}\|\_{F}^{2}}. |  |

These two inequalities simultaneously hold whenever

|  |  |  |
| --- | --- | --- |
|  | 4​T2​‖σ−1‖F4+ 2​T​‖σ−1‖F2​γ02<γ04,4T^{2}\,\|\sigma^{-1}\|\_{F}^{4}\;+\;2T\,\|\sigma^{-1}\|\_{F}^{2}\,\gamma\_{0}^{2}\;<\;\gamma\_{0}^{4}, |  |

which is equivalent to

|  |  |  |
| --- | --- | --- |
|  | γ02>(1+5)​T​‖σ−1‖F2.\gamma\_{0}^{2}\;>\;(1+\sqrt{5})\,T\,\|\sigma^{-1}\|\_{F}^{2}. |  |

Under this condition, an explicit admissible choice is

|  |  |  |
| --- | --- | --- |
|  | ε∗:=T+12​(2​T2γ022​‖σ−1‖F2−T+γ02‖σ−1‖F2)>T.\varepsilon^{\*}\;:=\;T+\frac{1}{2}\left(\frac{2T^{2}}{\frac{\gamma\_{0}^{2}}{2\|\sigma^{-1}\|\_{F}^{2}}-T}+\frac{\gamma\_{0}^{2}}{\|\sigma^{-1}\|\_{F}^{2}}\right)\;>\;T. |  |

For this ε∗\varepsilon^{\*} we have

|  |  |  |
| --- | --- | --- |
|  | CA​(ε∗)=𝔼ℙ0​[exp⁡(ε∗−T2​‖a​(B)‖22)]<∞,𝔼ℙ0​[(1+‖a​(B)‖22)​exp⁡((T+2​T2ε∗−T)​‖a​(B)‖22)]<∞,C\_{A}(\varepsilon^{\*})=\mathbb{E}\_{\mathbb{P}\_{0}}\!\left[\exp\!\left(\frac{\varepsilon^{\*}-T}{2}\,\|a(B)\|\_{2}^{2}\right)\right]<\infty,\qquad\mathbb{E}\_{\mathbb{P}\_{0}}\!\left[(1+\|a(B)\|\_{2}^{2})\,\exp\!\left(\Big(T+\frac{2T^{2}}{\varepsilon^{\*}-T}\Big)\|a(B)\|\_{2}^{2}\right)\right]<\infty, |  |

by the sub-Gaussian integrability above. Hence, I1<∞I\_{1}<\infty.

Finally, we upper bound ℐβ\mathcal{I}\_{\beta} when β>1\beta>1.
By convexity of the map x↦xβx\mapsto x^{\beta} when β>1\beta>1 and the Jensen inequality,

|  |  |  |
| --- | --- | --- |
|  | A​(y)β=(𝔼ℙ0​[LT​(B,y)])β≤𝔼ℙ0​[LT​(B,y)β].A(y)^{\beta}\;=\;\big(\mathbb{E}\_{\mathbb{P}\_{0}}[L\_{T}(B,y)]\big)^{\beta}\;\leq\;\mathbb{E}\_{\mathbb{P}\_{0}}\!\big[L\_{T}(B,y)^{\beta}\big]. |  |

Fix ε>β2​T\varepsilon>\beta^{2}T and use the Young inequality
⟨u,v⟩≤ε2​‖u‖22+12​ε​‖v‖22\langle u,v\rangle\leq\tfrac{\varepsilon}{2}\|u\|\_{2}^{2}+\tfrac{1}{2\varepsilon}\|v\|\_{2}^{2} with u=β​a​(B)u=\beta a(B), v=yv=y:

|  |  |  |
| --- | --- | --- |
|  | LT​(B,y)β=exp⁡(β​⟨a​(B),y⟩−β​T2​‖a​(B)‖22)≤exp⁡(ε−β​T2​‖a​(B)‖22)​ec​‖y‖22,c:=β22​ε∈(0,12​T).L\_{T}(B,y)^{\beta}=\exp\!\Big(\beta\langle a(B),y\rangle-\tfrac{\beta T}{2}\|a(B)\|\_{2}^{2}\Big)\leq\exp\!\Big(\tfrac{\varepsilon-\beta T}{2}\|a(B)\|\_{2}^{2}\Big)\,e^{c\|y\|\_{2}^{2}},\quad c:=\frac{\beta^{2}}{2\varepsilon}\in\Big(0,\frac{1}{2T}\Big). |  |

Taking expectation in BB yields

|  |  |  |
| --- | --- | --- |
|  | A​(y)β≤Cβ​(ε)​ec​‖y‖22,Cβ​(ε):=𝔼ℙ0​[exp⁡(ε−β​T2​‖a​(B)‖22)].A(y)^{\beta}\;\leq\;C\_{\beta}(\varepsilon)\,e^{c\|y\|\_{2}^{2}},\quad C\_{\beta}(\varepsilon):=\mathbb{E}\_{\mathbb{P}\_{0}}\!\Big[\exp\!\Big(\tfrac{\varepsilon-\beta T}{2}\|a(B)\|\_{2}^{2}\Big)\Big]. |  |

Thus, exactly as in the I1I\_{1} bound for β∈(0,1)\beta\in(0,1), we obtain

|  |  |  |
| --- | --- | --- |
|  | ℐβ≤C​(ε,T,d,σ)​𝔼ℙ0​[(1+‖a​(B)‖22)​exp⁡((T+2​T2​β2ε−β2​T)​‖a​(B)‖22)],\mathcal{I}\_{\beta}\;\leq\;C(\varepsilon,T,d,\sigma)\;\mathbb{E}\_{\mathbb{P}\_{0}}\!\Big[(1+\|a(B)\|\_{2}^{2})\,\exp\!\Big(\Big(T+\frac{2T^{2}\beta^{2}}{\varepsilon-\beta^{2}T}\Big)\|a(B)\|\_{2}^{2}\Big)\Big], |  |

for some finite constant C​(ε,T,d,σ)C(\varepsilon,T,d,\sigma) whenever c∈(0,1/(2​T))c\in(0,1/(2T)).
Therefore, to have ℐβ<∞\mathcal{I}\_{\beta}<\infty it suffices to pick ε>β2​T\varepsilon>\beta^{2}T such that

|  |  |  |
| --- | --- | --- |
|  | ε−β​T2<γ022​‖σ−1‖F2andT+2​T2​β2ε−β2​T<γ022​‖σ−1‖F2.\frac{\varepsilon-\beta T}{2}\;<\;\frac{\gamma\_{0}^{2}}{2\|\sigma^{-1}\|\_{F}^{2}}\qquad\text{and}\qquad T+\frac{2T^{2}\beta^{2}}{\varepsilon-\beta^{2}T}\;<\;\frac{\gamma\_{0}^{2}}{2\|\sigma^{-1}\|\_{F}^{2}}. |  |

These two inequalities simultaneously hold precisely when

|  |  |  |
| --- | --- | --- |
|  | γ02‖σ−1‖F2>T2​(β2−β+2+(β2−β+2)2+8​(β2+β)).\frac{\gamma\_{0}^{2}}{\|\sigma^{-1}\|\_{F}^{2}}\;>\;\frac{T}{2}\Big(\beta^{2}-\beta+2\;+\;\sqrt{\,(\beta^{2}-\beta+2)^{2}+8(\beta^{2}+\beta)\,}\Big)\;. |  |

Under the displayed condition, choose any

|  |  |  |
| --- | --- | --- |
|  | ε∈(β2​T+2​T2​β2γ022​‖σ−1‖F2−T,β​T+γ02‖σ−1‖F2),\varepsilon\in\Big(\,\beta^{2}T+\frac{2T^{2}\beta^{2}}{\frac{\gamma\_{0}^{2}}{2\|\sigma^{-1}\|\_{F}^{2}}-T}\,,\;\beta T+\frac{\gamma\_{0}^{2}}{\|\sigma^{-1}\|\_{F}^{2}}\,\Big), |  |

which is a nonempty interval; then both parts of (⋆)(\star) hold and the expectation above is finite. Hence ℐβ<∞\mathcal{I}\_{\beta}<\infty for all β>1\beta>1 under the stated sub-Gaussian slack.

For the proof of part (2), we first notice that there exists

|  |  |  |
| --- | --- | --- |
|  | γ0 2>τ⋅2​T​(4​β2−2​β)​‖σ−1‖F2τ−2​T​(4​β2−2​β)​‖σ−1‖F2.\gamma\_{0}^{\,2}\;>\;\frac{\tau\cdot 2T\,(4\beta^{2}-2\beta)\,\|\sigma^{-1}\|\_{F}^{2}}{\tau-2T\,(4\beta^{2}-2\beta)\,\|\sigma^{-1}\|\_{F}^{2}}. |  |

such that
𝔼ℙ0​[eγ2​‖B‖22]<∞\mathbb{E}\_{\mathbb{P}\_{0}}[e^{\gamma^{2}\|B\|\_{2}^{2}}]<\infty for all γ<γ0\gamma<\gamma\_{0} by Assumption [4](https://arxiv.org/html/2512.01408v1#Thmassumption4 "Assumption 4. ‣ Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections").
By Cauchy–Schwarz inequality in yy and β=α1−α\beta=\frac{\alpha}{1-\alpha},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Fs​(B,Δ)‖2\displaystyle\|F\_{s}(B,\Delta)\|\_{2} | =sup‖u‖2=1⟨u,∫ℝd∇bLT​(B+s​Δ,y)​(𝔼​[LT​(B+s​Δ,y)])β​φT​(y)​𝑑y⟩\displaystyle=\sup\_{\|u\|\_{2}=1}\left\langle u,\;\int\_{\mathbb{R}^{d}}\nabla\_{b}L\_{T}(B+s\Delta,y)\,\big(\mathbb{E}[L\_{T}(B+s\Delta,y)]\big)^{\beta}\,\varphi\_{T}(y)\,dy\right\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =sup‖u‖2=1∫ℝd⟨u,∇bLT​(B+s​Δ,y)⟩​(𝔼​[LT​(B+s​Δ,y)])β​φT​(y)​𝑑y\displaystyle=\sup\_{\|u\|\_{2}=1}\int\_{\mathbb{R}^{d}}\langle u,\nabla\_{b}L\_{T}(B+s\Delta,y)\rangle\,\big(\mathbb{E}[L\_{T}(B+s\Delta,y)]\big)^{\beta}\,\varphi\_{T}(y)\,dy |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤sup‖u‖2=1(∫ℝd⟨u,∇bLT​(B+s​Δ,y)⟩2​φT​(y)​𝑑y)1/2​(∫ℝd(𝔼​[LT​(B+s​Δ,y)])2​β​φT​(y)​𝑑y)1/2\displaystyle\leq\sup\_{\|u\|\_{2}=1}\Bigg(\int\_{\mathbb{R}^{d}}\langle u,\nabla\_{b}L\_{T}(B+s\Delta,y)\rangle^{2}\,\varphi\_{T}(y)\,dy\Bigg)^{\!1/2}\Bigg(\int\_{\mathbb{R}^{d}}\big(\mathbb{E}[L\_{T}(B+s\Delta,y)]\big)^{2\beta}\,\varphi\_{T}(y)\,dy\Bigg)^{\!1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(∫ℝd‖∇bLT​(B+s​Δ,y)‖22​φT​(y)​𝑑y)1/2​(∫ℝd(𝔼​[LT​(B+s​Δ,y)])2​β​φT​(y)​𝑑y)1/2.\displaystyle\leq\Bigg(\int\_{\mathbb{R}^{d}}\|\nabla\_{b}L\_{T}(B+s\Delta,y)\|\_{2}^{2}\,\varphi\_{T}(y)\,dy\Bigg)^{\!1/2}\Bigg(\int\_{\mathbb{R}^{d}}\big(\mathbb{E}[L\_{T}(B+s\Delta,y)]\big)^{2\beta}\,\varphi\_{T}(y)\,dy\Bigg)^{\!1/2}. |  |

Recall that

|  |  |  |
| --- | --- | --- |
|  | ‖∇bLT​(b,y)‖22≤‖σ−1‖F2​LT​(b,y)2​(1+‖y‖22+T2​‖a​(b)‖22).\|\nabla\_{b}L\_{T}(b,y)\|\_{2}^{2}\;\leq\;\|\sigma^{-1}\|\_{F}^{2}\,L\_{T}(b,y)^{2}\big(1+\|y\|\_{2}^{2}+T^{2}\|a(b)\|\_{2}^{2}\big). |  |

With the identity LT​(b,y)2​φT​(y)=eT​‖a​(b)‖22​φT​(y−2​T​a​(b))L\_{T}(b,y)^{2}\varphi\_{T}(y)=e^{T\|a(b)\|\_{2}^{2}}\,\varphi\_{T}(y-2Ta(b)) and a Gaussian
moment bound,

|  |  |  |
| --- | --- | --- |
|  | ∫ℝd‖∇bLT​(B+s​Δ,y)‖22​φT​(y)​𝑑y≤C​(1+‖a​(B+s​Δ)‖22)​eT​‖a​(B+s​Δ)‖22.\int\_{\mathbb{R}^{d}}\|\nabla\_{b}L\_{T}(B+s\Delta,y)\|\_{2}^{2}\,\varphi\_{T}(y)\,dy\;\leq\;C\,\big(1+\|a(B+s\Delta)\|\_{2}^{2}\big)\,e^{T\|a(B+s\Delta)\|\_{2}^{2}}. |  |

Since a​(B+s​Δ)=a​(B)+s​σ−1​Δa(B+s\Delta)=a(B)+s\,\sigma^{-1}\Delta,

|  |  |  |
| --- | --- | --- |
|  | ‖a​(B+s​Δ)‖22≤2​‖a​(B)‖22+2​‖σ−1‖F2​‖Δ‖22,\|a(B+s\Delta)\|\_{2}^{2}\leq 2\|a(B)\|\_{2}^{2}+2\|\sigma^{-1}\|\_{F}^{2}\,\|\Delta\|\_{2}^{2}, |  |

we have

|  |  |  |
| --- | --- | --- |
|  | ∫ℝd‖∇bLT​(B+s​Δ,y)‖22​φT​(y)​𝑑y≤C​(B)​exp⁡(C1​‖Δ‖22),\int\_{\mathbb{R}^{d}}\|\nabla\_{b}L\_{T}(B+s\Delta,y)\|\_{2}^{2}\,\varphi\_{T}(y)\,dy\;\leq\;C(B)\,\exp\!\big(C\_{1}\,\|\Delta\|\_{2}^{2}\big), |  |

with C1:=2​T​‖σ−1‖F2C\_{1}:=2T\,\|\sigma^{-1}\|\_{F}^{2} and
C​(B):=C​(1+2​‖a​(B)‖22)​e2​T​‖a​(B)‖22C(B):=C\,(1+2\|a(B)\|\_{2}^{2})\,e^{2T\|a(B)\|\_{2}^{2}}.
With a sub-Gaussian assumption
4​T​‖σ−1‖F2<γ024T\|\sigma^{-1}\|\_{F}^{2}<\gamma\_{0}^{2}
and
𝔼​[exp⁡(γ2​‖B‖22)]<∞\mathbb{E}[\exp(\gamma^{2}\|B\|\_{2}^{2})]<\infty for all γ<γ0\gamma<\gamma\_{0}.
Using ‖a​(B)‖22≤2​‖σ−1‖F2​‖B‖22+2​‖m‖22\|a(B)\|\_{2}^{2}\leq 2\|\sigma^{-1}\|\_{F}^{2}\|B\|\_{2}^{2}+2\|m\|\_{2}^{2},
we obtain

|  |  |  |
| --- | --- | --- |
|  | C​(B)≤K​(1+‖B‖22)​exp⁡(κ​‖B‖22),K:=C​c0​e4​T​‖m‖22,κ:=4​T​‖σ−1‖F2.C(B)\;\leq\;K\,(1+\|B\|\_{2}^{2})\,\exp\!\big(\kappa\|B\|\_{2}^{2}\big),\qquad K:=C\,c\_{0}\,e^{4T\|m\|\_{2}^{2}},\ \ \kappa:=4T\|\sigma^{-1}\|\_{F}^{2}. |  |

Hence C​(B)C(B) is finite ℙ0\mathbb{P}\_{0} almost surely.

Next, we upper bound the second term. We define

|  |  |  |
| --- | --- | --- |
|  | Iβ​(s):=∫ℝd(𝔼​[LT​(B+s​Δ,y)])2​β​φT​(y)​𝑑y.I\_{\beta}(s)\;:=\;\int\_{\mathbb{R}^{d}}\Big(\mathbb{E}\big[L\_{T}(B+s\Delta,y)\big]\Big)^{2\beta}\,\varphi\_{T}(y)\,dy. |  |

When β<0\beta<0 (i.e. α<0\alpha<0), set

|  |  |  |
| --- | --- | --- |
|  | as​(B):=σ−1​(B+s​Δ)−m.a\_{s}(B):=\sigma^{-1}(B+s\Delta)-m. |  |

By the Jensen inequality,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[LT​(B+s​Δ,y)]\displaystyle\mathbb{E}\big[L\_{T}(B+s\Delta,y)\big] | =𝔼​[exp⁡(⟨as​(B),y⟩−T2​‖as​(B)‖22)]\displaystyle=\mathbb{E}\!\left[\exp\!\Big(\langle a\_{s}(B),y\rangle-\frac{T}{2}\|a\_{s}(B)\|\_{2}^{2}\Big)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥exp⁡(⟨𝔼​[as​(B)],y⟩−T2​𝔼​[‖as​(B)‖22]).\displaystyle\geq\exp\!\Big(\langle\mathbb{E}[a\_{s}(B)],y\rangle-\frac{T}{2}\,\mathbb{E}\left[\|a\_{s}(B)\|\_{2}^{2}\right]\Big). |  |

Since 2​β<02\beta<0, raising both sides to the power 2​β2\beta reverses the inequality:

|  |  |  |
| --- | --- | --- |
|  | (𝔼​[LT​(B+s​Δ,y)])2​β≤exp⁡(2​β​⟨𝔼​[as​(B)],y⟩−β​T​𝔼​[‖as​(B)‖22]).\Big(\mathbb{E}[L\_{T}(B+s\Delta,y)]\Big)^{2\beta}\;\leq\;\exp\!\Big(2\beta\,\langle\mathbb{E}[a\_{s}(B)],y\rangle-\beta T\,\mathbb{E}\left[\|a\_{s}(B)\|\_{2}^{2}\right]\Big). |  |

Integrating against φT\varphi\_{T}, we obtain

|  |  |  |
| --- | --- | --- |
|  | Iβ​(s)≤exp⁡((2​β2−β)​T​𝔼​[‖as​(B)‖22])<∞.I\_{\beta}(s)\;\leq\;\exp\!\Big(\big(2\beta^{2}-\beta\big)\,T\,\mathbb{E}\left[\|a\_{s}(B)\|\_{2}^{2}\right]\Big)<\infty. |  |

When β>0\beta>0, we first fix r>1r>1 with r≥2​βr\geq 2\beta. By the Lyapunov and Jensen inequalities,

|  |  |  |
| --- | --- | --- |
|  | Iβ​(s)≤(𝔼​[∫ℝdLT​(B+s​Δ,y)r​φT​(y)​𝑑y])2​β/r.I\_{\beta}(s)\;\leq\;\Bigg(\mathbb{E}\Big[\int\_{\mathbb{R}^{d}}L\_{T}(B+s\Delta,y)^{\,r}\,\varphi\_{T}(y)\,dy\Big]\Bigg)^{\!2\beta/r}. |  |

Completing the square in yy gives the closed form

|  |  |  |
| --- | --- | --- |
|  | ∫ℝdLT​(b,y)r​φT​(y)​𝑑y=exp⁡(T2​(r2−r)​‖σ−1​b−m‖22).\int\_{\mathbb{R}^{d}}L\_{T}(b,y)^{\,r}\,\varphi\_{T}(y)\,dy\;=\;\exp\!\Big(\tfrac{T}{2}\,(r^{2}-r)\,\|\sigma^{-1}b-m\|\_{2}^{2}\Big). |  |

Therefore, with

|  |  |  |
| --- | --- | --- |
|  | cr:=T2​(r2−r)>0,c\_{r}\;:=\;\frac{T}{2}\,(r^{2}-r)>0, |  |

we obtain

|  |  |  |
| --- | --- | --- |
|  | Iβ​(s)≤(𝔼​[ecr​‖as​(B)‖22])2​β/r.I\_{\beta}(s)\;\leq\;\Big(\mathbb{E}\left[\,e^{\,c\_{r}\,\|a\_{s}(B)\|\_{2}^{2}}\right]\Big)^{2\beta/r}. |  |

Since

|  |  |  |
| --- | --- | --- |
|  | ‖as​(B)‖22=‖σ−1​(B+s​Δ)−m‖22≤2​‖σ−1​(B+s​Δ)‖22+2​‖m‖22≤4​‖σ−1‖F2​(‖B‖22+‖Δ‖22)+2​‖m‖22,\|a\_{s}(B)\|\_{2}^{2}=\|\sigma^{-1}(B+s\Delta)-m\|\_{2}^{2}\leq 2\|\sigma^{-1}(B+s\Delta)\|\_{2}^{2}+2\|m\|\_{2}^{2}\leq 4\|\sigma^{-1}\|\_{F}^{2}\big(\|B\|\_{2}^{2}+\|\Delta\|\_{2}^{2}\big)+2\|m\|\_{2}^{2}, |  |

then

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ecr​‖as​(B)‖22]≤e 2​cr​‖m‖22​𝔼​[exp⁡(4​cr​‖σ−1‖F2​(‖B‖22+‖Δ‖22))].\mathbb{E}\left[\,e^{\,c\_{r}\,\|a\_{s}(B)\|\_{2}^{2}}\right]\;\leq\;e^{\,2c\_{r}\|m\|\_{2}^{2}}\,\mathbb{E}\left[\exp\!\left(4c\_{r}\|\sigma^{-1}\|\_{F}^{2}\big(\|B\|\_{2}^{2}+\|\Delta\|\_{2}^{2}\big)\right)\right]. |  |

Let p>1p>1 and q:=pp−1q:=\frac{p}{p-1}. By the Hölder inequality,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[exp⁡(4​cr​‖σ−1‖F2​(‖B‖22+‖Δ‖22))]≤(𝔼​[ea​p​‖B‖22])1/p​(𝔼​[ea​q​‖Δ‖22])1/q,\mathbb{E}\left[\exp\!\left(4c\_{r}\|\sigma^{-1}\|\_{F}^{2}\big(\|B\|\_{2}^{2}+\|\Delta\|\_{2}^{2}\big)\right)\right]\;\leq\;\Big(\mathbb{E}\left[e^{\,ap\,\|B\|\_{2}^{2}}\right]\Big)^{\!1/p}\;\Big(\mathbb{E}\left[e^{\,aq\,\|\Delta\|\_{2}^{2}}\right]\Big)^{\!1/q}, |  |

where a:=4​cr​‖σ−1‖F2=2​T​(r2−r)​‖σ−1‖F2.a:=4c\_{r}\|\sigma^{-1}\|\_{F}^{2}=2T(r^{2}-r)\|\sigma^{-1}\|\_{F}^{2}.
Putting the pieces together,

|  |  |  |
| --- | --- | --- |
|  | Iβ​(s)≤exp⁡(2​β​T​(r−1)​‖m‖22)​(𝔼​[ea​p​‖B‖22])2​β/(r​p)⏟=⁣:Cβ,r,p⋅(𝔼​[ea​q​‖Δ‖22])2​β/(r​q)⏟=⁣:MΔ​(θ) 2​β/(r​q),I\_{\beta}(s)\;\leq\;\underbrace{\exp\!\big(2\beta T(r-1)\|m\|\_{2}^{2}\big)\;\Big(\mathbb{E}\left[e^{\,ap\,\|B\|\_{2}^{2}}\right]\Big)^{\!2\beta/(rp)}}\_{=:\penalty 10000\ C\_{\beta,r,p}}\;\cdot\;\underbrace{\Big(\mathbb{E}\left[e^{\,aq\,\|\Delta\|\_{2}^{2}}\right]\Big)^{\!2\beta/(rq)}}\_{=:\penalty 10000\ M\_{\Delta}(\theta)^{\,2\beta/(rq)}}, |  |

where θ:=a​q=2​T​(r2−r)​‖σ−1‖F2​q.\theta:=aq=2T(r^{2}-r)\|\sigma^{-1}\|\_{F}^{2}\,q.
Recall the sub-Gaussian assumption: there exists γ0>0\gamma\_{0}>0 such that
𝔼​[eγ2​‖B‖22]<∞\mathbb{E}[e^{\gamma^{2}\|B\|\_{2}^{2}}]<\infty for all γ<γ0\gamma<\gamma\_{0}. Then Cβ,r,p<∞C\_{\beta,r,p}<\infty implies

|  |  |  |
| --- | --- | --- |
|  | a​p= 2​T​(r2−r)​‖σ−1‖F2​p<γ0 2\;ap\;=\;2T(r^{2}-r)\,\|\sigma^{-1}\|\_{F}^{2}\,p\;<\;\gamma\_{0}^{\,2}\; |  |

and MΔ​(θ) 2​β/(r​q)<∞M\_{\Delta}(\theta)^{\,2\beta/(rq)}<\infty implies
θ≤τ\theta\leq\tau.

Let S:=‖σ−1‖F2S:=\|\sigma^{-1}\|\_{F}^{2}. Taking the minimal admissible r=2​βr=2\beta, we have

|  |  |  |
| --- | --- | --- |
|  | a​(β):= 2​T​(r2−r)​S= 2​T​(4​β2−2​β)​S.a(\beta)\;:=\;2T\,(r^{2}-r)\,S\;=\;2T\,(4\beta^{2}-2\beta)\,S. |  |

For a fixed cost scale τ>0\tau>0, the Hölder coefficients q=τa​(β)q=\dfrac{\tau}{a(\beta)} and p=qq−1=ττ−a​(β)p=\dfrac{q}{q-1}=\dfrac{\tau}{\tau-a(\beta)} (valid when τ>a​(β)\tau>a(\beta)) yield the BB-side requirement

|  |  |  |
| --- | --- | --- |
|  | τ>a​(β)andγ0 2>τ​a​(β)τ−a​(β).\ \tau\;>\;a(\beta)\qquad\text{and}\qquad\gamma\_{0}^{\,2}\;>\;\frac{\tau\,a(\beta)}{\tau-a(\beta)}. |  |

Equivalently, in terms of β\beta,

|  |  |  |
| --- | --- | --- |
|  | τ> 2​T​(4​β2−2​β)​Sandγ0 2>τ⋅2​T​(4​β2−2​β)​Sτ−2​T​(4​β2−2​β)​S.\ \tau\;>\;2T\,(4\beta^{2}-2\beta)\,S\qquad\text{and}\qquad\gamma\_{0}^{\,2}\;>\;\frac{\tau\cdot 2T\,(4\beta^{2}-2\beta)\,S}{\tau-2T\,(4\beta^{2}-2\beta)\,S}. |  |

###### Proof of Theorem [5](https://arxiv.org/html/2512.01408v1#Thmtheorem5 "Theorem 5. ‣ Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections").

Now we are ready to prove Theorem [5](https://arxiv.org/html/2512.01408v1#Thmtheorem5 "Theorem 5. ‣ Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections").
We recall that the cost function is c​(u,v)=eτ​‖u−v‖22−1c(u,v)=e^{\tau||u-v||\_{2}^{2}}-1 and first do the case when α<0\alpha<0 and solve the concave optimization problem

|  |  |  |
| --- | --- | --- |
|  | arg⁡maxℚ∈𝒰δ,BOT​(ℙ0)⁡𝒥​(ℚ).\arg\max\_{\mathbb{Q}\in\mathcal{U}\_{\delta,B}^{\text{OT}}(\mathbb{P}\_{0})}\mathcal{J}(\mathbb{Q}). |  |

To begin with, we define, for fixed δ\delta and qq, the collection of couplings

|  |  |  |
| --- | --- | --- |
|  | Cδ:={π∈𝒫(ℝd×ℝd):π(.,ℝd)=ℙ0,∫(eτ​‖x−y‖22−1)π(dx,dy)≤δ}.C\_{\delta}:=\left\{\pi\in\mathcal{P}(\mathbb{R}^{d}\times\mathbb{R}^{d}):\pi(.,\mathbb{R}^{d})=\mathbb{P}\_{0},\int\left(e^{\tau||x-y||\_{2}^{2}}-1\right)\pi(dx,dy)\leq\delta\right\}. |  |

These couplings play an important role.
In our case, we can write BB and B+ΔB+\Delta as the couplings, and Δ\Delta is the non-deterministic transport (may have randomness that is not from BB, and we write only 𝔼\mathbb{E} to represent the non-deterministic coupling).

From the Jensen inequality,

|  |  |  |
| --- | --- | --- |
|  | exp⁡(𝔼​[τ​‖Δ‖22])≤𝔼​[exp⁡(τ​‖Δ‖22)]≤δ+1.\exp\left(\mathbb{E}\left[\tau\left\|\Delta\right\|\_{2}^{2}\right]\right)\leq\mathbb{E}\left[\exp\left(\tau\left\|\Delta\right\|\_{2}^{2}\right)\right]\leq\delta+1. |  |

Therefore, as δ→0\delta\to 0,

|  |  |  |
| --- | --- | --- |
|  | ‖Δ‖L22=𝔼​[‖Δ‖22]≤1τ​log⁡(1+δ)=δτ+o​(δ).\left\|\Delta\right\|\_{L^{2}}^{2}=\mathbb{E}\left[\left\|\Delta\right\|\_{2}^{2}\right]\leq\tfrac{1}{\tau}\log(1+\delta)=\frac{\delta}{\tau}+o(\delta). |  |

With the Taylor expansion and the Fubini theorem (valid by Lemma [2](https://arxiv.org/html/2512.01408v1#Thmlemma2 "Lemma 2. ‣ Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")), for δ>0\delta>0,

|  |  |  |
| --- | --- | --- |
|  | supℚ∈𝒰δ,BOT​(ℙ0)𝒥​(ℚ)−𝒥​(ℙ0)\displaystyle\sup\_{\mathbb{Q}\in\mathcal{U}\_{\delta,B}^{\text{OT}}(\mathbb{P}\_{0})}\mathcal{J}(\mathbb{Q})-\mathcal{J}(\mathbb{P}\_{0}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤supΔ:π∈Cδ∫ℝd(𝔼​[LT​(B+Δ,y)]11−α−𝔼​[LT​(B,y)]11−α)​φT​(y)​𝑑y\displaystyle\leq\sup\_{\Delta:\pi\in C\_{\delta}}\int\_{\mathbb{R}^{d}}\left(\mathbb{E}\left[L\_{T}(B+\Delta,y)\right]^{\frac{1}{1-\alpha}}-\mathbb{E}\left[L\_{T}(B,y)\right]^{\frac{1}{1-\alpha}}\right)\varphi\_{T}(y)dy |  |
|  |  |  |
| --- | --- | --- |
|  | =supΔ:π∈Cδ∫ℝd11−α​∫01𝔼​[LT​(B+s​Δ,y)]α1−α​𝔼​[⟨∇bLT​(B+s​Δ,y),Δ⟩]​𝑑s​φT​(y)​𝑑y\displaystyle=\sup\_{\Delta:\pi\in C\_{\delta}}\int\_{\mathbb{R}^{d}}\frac{1}{1-\alpha}\int\_{0}^{1}\mathbb{E}\left[L\_{T}(B+s\Delta,y)\right]^{\frac{\alpha}{1-\alpha}}\mathbb{E}\left[\left\langle\nabla\_{b}L\_{T}(B+s\Delta,y),\Delta\right\rangle\right]ds\varphi\_{T}(y)dy |  |
|  |  |  |
| --- | --- | --- |
|  | ≤δτ+o​(δ)​supΔ:π∈Cδ∫01(𝔼​[‖11−α​∫ℝd∇bLT​(B+s​Δ,y)​𝔼​[LT​(B+s​Δ,y)]α1−α​φT​(y)​𝑑y‖22])12​𝑑s,\displaystyle\leq\sqrt{\frac{\delta}{\tau}+o(\delta)}\sup\_{\Delta:\pi\in C\_{\delta}}\int\_{0}^{1}\left(\mathbb{E}\left[\left\|\frac{1}{1-\alpha}\int\_{\mathbb{R}^{d}}\nabla\_{b}L\_{T}(B+s\Delta,y)\mathbb{E}\left[L\_{T}(B+s\Delta,y)\right]^{\frac{\alpha}{1-\alpha}}\varphi\_{T}(y)dy\right\|\_{2}^{2}\right]\right)^{\frac{1}{2}}ds, |  |

where the last step is by the Hölder inequality.

Any choice of πδ∈Cδ\pi^{\delta}\in C\_{\delta} (and the corresponding Δδ\Delta\_{\delta}) converges to the pushforward measure of ℙ0\mathbb{P}\_{0} under the map x↦(x,x)x\mapsto(x,x) on 𝒫​(ℝd×ℝd)\mathcal{P}(\mathbb{R}^{d}\times\mathbb{R}^{d}) in the topology induced by the map (x,y)↦eτ​‖x−y‖22−1(x,y)\mapsto e^{\tau||x-y||\_{2}^{2}}-1.

By Lemma [2](https://arxiv.org/html/2512.01408v1#Thmlemma2 "Lemma 2. ‣ Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), there exists constants C​(B)>0C(B)>0 and finite ℙ0\mathbb{P}\_{0} almost surely and C1≤τC\_{1}\leq\tau such that

|  |  |  |
| --- | --- | --- |
|  | ‖11−α​∫ℝd∇bLT​(B+s​Δ,y)​𝔼​[LT​(B+s​Δ,y)]α1−α​φT​(y)​𝑑y‖22≤C​(B)​exp⁡(C1​‖Δ‖22).\left\|\frac{1}{1-\alpha}\int\_{\mathbb{R}^{d}}\nabla\_{b}L\_{T}(B+s\Delta,y)\mathbb{E}\left[L\_{T}(B+s\Delta,y)\right]^{\frac{\alpha}{1-\alpha}}\varphi\_{T}(y)dy\right\|\_{2}^{2}\leq C(B)\exp(C\_{1}\left\|\Delta\right\|\_{2}^{2}). |  |

for all fixed s∈[0,1]s\in[0,1], small δ\delta, and almost every BB and yy.

Fix a sequence δn↓0\delta\_{n}\downarrow 0 and pick any πδn∈Cδn\pi^{\delta\_{n}}\in C\_{\delta\_{n}} with a
law of (B,B+Δδn)(B,B+\Delta\_{\delta\_{n}}). Define, for s∈[0,1]s\in[0,1],

|  |  |  |
| --- | --- | --- |
|  | Xδn​(s):=‖11−α​∫ℝd∇bLT​(B+s​Δδn,y)​(𝔼​[LT​(B+s​Δδn,y)])α1−α​φT​(y)​𝑑y‖22.X\_{\delta\_{n}}(s)\ :=\ \Big\|\frac{1}{1-\alpha}\int\_{\mathbb{R}^{d}}\nabla\_{b}L\_{T}(B+s\Delta\_{\delta\_{n}},y)\Big(\mathbb{E}[L\_{T}(B+s\Delta\_{\delta\_{n}},y)]\Big)^{\frac{\alpha}{1-\alpha}}\varphi\_{T}(y)\,dy\Big\|\_{2}^{2}. |  |

By Lemma [2](https://arxiv.org/html/2512.01408v1#Thmlemma2 "Lemma 2. ‣ Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), there exist C​(B)>0C(B)>0 and finite ℙ0\mathbb{P}\_{0} almost surely and C1≤τC\_{1}\leq\tau such that, for all s∈[0,1]s\in[0,1] and all admissible Δ\Delta,

|  |  |  |
| --- | --- | --- |
|  | Xδn​(s)≤C​(B)​exp⁡(C1​‖Δδn‖22)ℙ0​-a.s..X\_{\delta\_{n}}(s)\ \leq\ C(B)\,\exp\!\big(C\_{1}\|\Delta\_{\delta\_{n}}\|\_{2}^{2}\big)\qquad\mathbb{P}\_{0}\text{-a.s.}. |  |

Moreover, 𝔼​[eτ​‖Δδn‖22]≤1+δn\mathbb{E}[e^{\tau\|\Delta\_{\delta\_{n}}\|\_{2}^{2}}]\leq 1+\delta\_{n} as n→∞n\to\infty.

Choose any η>0\eta>0 with 2​(1+η)​C1≤τ2(1+\eta)C\_{1}\leq\tau (possible since C1<τ2C\_{1}<\frac{\tau}{2}).
Using the Hölder inequality,

|  |  |  |
| --- | --- | --- |
|  | supn𝔼​[Xδn​(s)1+η]≤(𝔼ℙ0​[C​(B) 2​(1+η)])12​(supn𝔼​exp⁡(2​(1+η)​C1​‖Δδn‖22))12<∞,\sup\_{n}\mathbb{E}\big[X\_{\delta\_{n}}(s)^{1+\eta}\big]\ \leq\ \left(\mathbb{E}\_{\mathbb{P}\_{0}}\big[C(B)^{\,2(1+\eta)}\big]\,\right)^{\frac{1}{2}}\left(\sup\_{n}\mathbb{E}\exp\!\big(2(1+\eta)C\_{1}\|\Delta\_{\delta\_{n}}\|\_{2}^{2}\big)\right)^{\frac{1}{2}}<\ \infty, |  |

where 𝔼ℙ0​[C​(B)2​(1+η)]<∞\mathbb{E}\_{\mathbb{P}\_{0}}[C(B)^{2(1+\eta)}]<\infty holds under the sub-Gaussian assumption (recall the proof of Lemma [2](https://arxiv.org/html/2512.01408v1#Thmlemma2 "Lemma 2. ‣ Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")). Hence, {Xδn​(s)}n\{X\_{\delta\_{n}}(s)\}\_{n} is uniformly integrable.
Since Δδn→0\Delta\_{\delta\_{n}}\to 0 in L2L^{2} (hence in probability) and
b↦∇bLT​(b,y)b\mapsto\nabla\_{b}L\_{T}(b,y) is continuous, we have
Xδn​(s)→X0​(s)X\_{\delta\_{n}}(s)\to X\_{0}(s) in probability, where

|  |  |  |
| --- | --- | --- |
|  | X0​(s)=‖11−α​∫ℝd∇bLT​(B,y)​(𝔼ℙ0​[LT​(B,y)])α1−α​φT​(y)​𝑑y‖22.X\_{0}(s)\ =\ \Big\|\frac{1}{1-\alpha}\int\_{\mathbb{R}^{d}}\nabla\_{b}L\_{T}(B,y)\Big(\mathbb{E}\_{\mathbb{P}\_{0}}[L\_{T}(B,y)]\Big)^{\frac{\alpha}{1-\alpha}}\varphi\_{T}(y)\,dy\Big\|\_{2}^{2}. |  |

Thus, by Vitali’s theorem,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Xδn​(s)]⟶𝔼ℙ0​[X0​(s)]for every ​s∈[0,1].\mathbb{E}\big[X\_{\delta\_{n}}(s)\big]\ \longrightarrow\ \mathbb{E}\_{\mathbb{P}\_{0}}\big[X\_{0}(s)\big]\qquad\text{for every }s\in[0,1]. |  |

We also have the ss–uniform integrable bound

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Xδn​(s)]≤(𝔼ℙ0​[C​(B)1+η])11+η​(𝔼​eτ​‖Δδn‖22)η1+η≤(𝔼ℙ0​[C​(B)1+η])11+η​(1+δn)η1+η,\mathbb{E}\big[X\_{\delta\_{n}}(s)\big]\ \leq\ \Big(\mathbb{E}\_{\mathbb{P}\_{0}}[C(B)^{1+\eta}]\Big)^{\frac{1}{1+\eta}}\Big(\mathbb{E}e^{\tau\|\Delta\_{\delta\_{n}}\|\_{2}^{2}}\Big)^{\frac{\eta}{1+\eta}}\ \leq\ \Big(\mathbb{E}\_{\mathbb{P}\_{0}}[C(B)^{1+\eta}]\Big)^{\frac{1}{1+\eta}}(1+\delta\_{n})^{\frac{\eta}{1+\eta}}, |  |

independent of ss. Therefore, by dominated convergence theorem in ss,

|  |  |  |
| --- | --- | --- |
|  | ∫01𝔼​[Xδn​(s)]1/2​𝑑s⟶∫01𝔼ℙ0​[X0​(s)]1/2​𝑑s,\int\_{0}^{1}\mathbb{E}\big[X\_{\delta\_{n}}(s)\big]^{1/2}\,ds\ \longrightarrow\ \int\_{0}^{1}\mathbb{E}\_{\mathbb{P}\_{0}}\big[X\_{0}(s)\big]^{1/2}\,ds, |  |

which completes the upper bound argument and gives

|  |  |  |
| --- | --- | --- |
|  | supℚ∈𝒰δ,BOT​(ℙ0)𝒥​(ℚ)≤𝒥​(ℙ0)+δτ​‖H‖L22​(ℙ0)+o​(δ).\sup\_{\mathbb{Q}\in\mathcal{U}\_{\delta,B}^{\text{OT}}(\mathbb{P}\_{0})}\mathcal{J}(\mathbb{Q})\leq\mathcal{J}(\mathbb{P}\_{0})+\sqrt{\frac{\delta}{\tau}}\|H\|\_{L^{2}\_{2}(\mathbb{P}\_{0})}+o(\sqrt{\delta}). |  |

Next we prove the lower bound by a deterministic coupling. From Lemma [2](https://arxiv.org/html/2512.01408v1#Thmlemma2 "Lemma 2. ‣ Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), fix a deterministic function hh. Then by the integral form of Taylor expansion, we have

|  |  |  |
| --- | --- | --- |
|  | 𝒥​((Id+h)#​ℙ0)−𝒥​(ℙ0)\displaystyle\mathcal{J}((\mathrm{Id}+h)\_{\#}\mathbb{P}\_{0})-\mathcal{J}(\mathbb{P}\_{0}) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫ℝd(𝔼ℙ0​[LT​(B+h​(B),y)]11−α−𝔼ℙ0​[LT​(B,y)]11−α)​φT​(y)​𝑑y\displaystyle=\int\_{\mathbb{R}^{d}}\left(\mathbb{E}^{\mathbb{P}\_{0}}\left[L\_{T}(B+h(B),y)\right]^{\frac{1}{1-\alpha}}-\mathbb{E}\_{\mathbb{P}\_{0}}\left[L\_{T}(B,y)\right]^{\frac{1}{1-\alpha}}\right)\varphi\_{T}(y)dy |  |
|  |  |  |
| --- | --- | --- |
|  | =∫ℝd11−α​∫01𝔼ℙ0​[LT​(B+s​h​(B),y)]α1−α​𝔼ℙ0​[⟨∇bLT​(B+s​h​(B),y),h​(B)⟩]​𝑑s​φT​(y)​𝑑y.\displaystyle=\int\_{\mathbb{R}^{d}}\frac{1}{1-\alpha}\int\_{0}^{1}\mathbb{E}\_{\mathbb{P}\_{0}}\left[L\_{T}(B+sh(B),y)\right]^{\frac{\alpha}{1-\alpha}}\mathbb{E}\_{\mathbb{P}\_{0}}\left[\left\langle\nabla\_{b}L\_{T}(B+sh(B),y),h(B)\right\rangle\right]ds\varphi\_{T}(y)dy. |  |

Define the deterministic map

|  |  |  |
| --- | --- | --- |
|  | hδ​(b)=tδ​H​(b),tδ=δτ​‖H‖L22​(ℙ0)2​(1+o​(1))(δ↓0).h\_{\delta}(b)\;=\;t\_{\delta}\,H(b),\qquad t\_{\delta}\;=\;\sqrt{\frac{\delta}{\tau\,\|H\|\_{L^{2}\_{2}(\mathbb{P}\_{0})}^{2}}}\,(1+o(1))\quad(\delta\downarrow 0). |  |

Then hδh\_{\delta} is feasible for the exponential cost budget
𝔼​[eτ​‖hδ​(B)‖22−1]≤δ\mathbb{E}\big[e^{\tau\|h\_{\delta}(B)\|\_{2}^{2}}-1\big]\leq\delta for all sufficiently small δ\delta, and

|  |  |  |
| --- | --- | --- |
|  | 𝒥​((Id+hδ)#​ℙ0)−𝒥​(ℙ0)=δτ​‖H‖L22​(ℙ0)+o​(δ).\mathcal{J}\big((\mathrm{Id}+h\_{\delta})\_{\#}\mathbb{P}\_{0}\big)-\mathcal{J}(\mathbb{P}\_{0})\;=\;\sqrt{\frac{\delta}{\tau}}\|H\|\_{L^{2}\_{2}(\mathbb{P}\_{0})}\,\;+\;o\!\big(\sqrt{\delta}\big). |  |

Consequently, the deterministic class yields the sharp lower bound matching the upper bound’s rate and constant.
To see this, set ht​(b):=t​H​(b)h\_{t}(b):=t\,H(b). For fixed yy, let

|  |  |  |
| --- | --- | --- |
|  | ψy​(t):=(𝔼ℙ0​[LT​(B+ht​(B),y)])11−α.\psi\_{y}(t)\;:=\;\Big(\mathbb{E}\_{\mathbb{P}\_{0}}[L\_{T}(B+h\_{t}(B),y)]\Big)^{\frac{1}{1-\alpha}}. |  |

Then the above Taylor expansion becomes

|  |  |  |
| --- | --- | --- |
|  | 𝒥​((Id+ht)#​ℙ0)−𝒥​(ℙ0)=t​‖H‖L22​(ℙ0)2+o​(t)(t↓0).\mathcal{J}\big((\mathrm{Id}+h\_{t})\_{\#}\mathbb{P}\_{0}\big)-\mathcal{J}(\mathbb{P}\_{0})\;=\;t\,\|H\|\_{L^{2}\_{2}(\mathbb{P}\_{0})}^{2}\;+\;o(t)\qquad(t\downarrow 0). |  |

Since ‖ht​(B)‖22=t2​‖H​(B)‖22\|h\_{t}(B)\|\_{2}^{2}=t^{2}\|H(B)\|\_{2}^{2} and 𝔼ℙ0​[‖H​(B)‖22]<∞\mathbb{E}^{\mathbb{P}\_{0}}\left[\|H(B)\|\_{2}^{2}\right]<\infty, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[eτ​‖ht​(B)‖22]= 1+τ​t2​‖H‖L22​(ℙ0)2+o​(t2)(t↓0).\mathbb{E}\big[e^{\tau\|h\_{t}(B)\|\_{2}^{2}}\big]\;=\;1+\tau t^{2}\,\|H\|\_{L^{2}\_{2}(\mathbb{P}\_{0})}^{2}+o(t^{2})\qquad(t\downarrow 0). |  |

Thus there exists tδ=δ/(τ​‖H‖L22​(ℙ0)2)​(1+o​(1))t\_{\delta}=\sqrt{\delta/(\tau\|H\|\_{L^{2}\_{2}(\mathbb{P}\_{0})}^{2})}\,(1+o(1)) such that
𝔼​[eτ​‖htδ​(B)‖22]≤1+δ\mathbb{E}[e^{\tau\|h\_{t\_{\delta}}(B)\|\_{2}^{2}}]\leq 1+\delta for all sufficiently small δ\delta.
Plugging t=tδt=t\_{\delta} into the expansion above yields

|  |  |  |
| --- | --- | --- |
|  | 𝒥​((Id+htδ)#​ℙ0)−𝒥​(ℙ0)=‖H‖L22​(ℙ0)2​tδ+o​(tδ)=‖H‖L22​(ℙ0)​δτ+o​(δ),\mathcal{J}\big((\mathrm{Id}+h\_{t\_{\delta}})\_{\#}\mathbb{P}\_{0}\big)-\mathcal{J}(\mathbb{P}\_{0})\;=\;\|H\|\_{L^{2}\_{2}(\mathbb{P}\_{0})}^{2}\,t\_{\delta}+o(t\_{\delta})\;=\;\|H\|\_{L^{2}\_{2}(\mathbb{P}\_{0})}\,\sqrt{\frac{\delta}{\tau}}\;+\;o\!\big(\sqrt{\delta}\big), |  |

as claimed.

Since Lemma [2](https://arxiv.org/html/2512.01408v1#Thmlemma2 "Lemma 2. ‣ Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") provides the estimates needed for the case when α∈(0,1)\alpha\in(0,1), the proof of the case when α∈(0,1)\alpha\in(0,1) and the solution of the convex optimization problem

|  |  |  |
| --- | --- | --- |
|  | arg⁡minℚ∈𝒰δ,BOT​(ℙ0)⁡𝒥​(ℚ)\arg\min\_{\mathbb{Q}\in\mathcal{U}\_{\delta,B}^{\text{OT}}(\mathbb{P}\_{0})}\mathcal{J}(\mathbb{Q}) |  |

is almost verbatim and we only need to notice that the optimal direction is on the opposite of the previous case.
∎

## Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support

In this section, we derive a stochastic asymptotic upper bound of the RWPI under the nonlinear projection when BB is not compactly supported. We will use a method that does not depend on Wasserstein geometry. Several technical lemmas are presented at the end of this section. Recall that we consider the case when α<1\alpha<1 and α≠0\alpha\neq 0 with the cost function cτ​(Δ):=eτ​‖Δ‖22− 1c\_{\tau}(\Delta)\;:=\;e^{\,\tau\,\|\Delta\|\_{2}^{2}}\;-\;1 for a displacement Δ\Delta. B(i)B^{(i)} are i.i.d. (calibrated) samples of BB from a distribution ℙ∗\mathbb{P}^{\*}, and they are used to constitute an empirical measure ℙn\mathbb{P}\_{n}, where nn is the sample size. For a fixed k>0k>0,

|  |  |  |
| --- | --- | --- |
|  | gk​(x)=(er​Tk)11−α​x11−α,g\_{k}(x)=\left(\frac{e^{rT}}{k}\right)^{\frac{1}{1-\alpha}}x^{\frac{1}{1-\alpha}}, |  |

and k∗k^{\*} represents the optimal Lagrangian multiplier. We still make a sub-Gaussian assumption on BB. Many computational details are similar to those in Section [C](https://arxiv.org/html/2512.01408v1#A3 "Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") (only the sub-Gaussian parameters are different), thus we omit some proofs for simplicity.

###### Assumption 5.

Suppose there exists γ0>0\gamma\_{0}>0 such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ∗​[exp⁡(γ2​‖B‖22)]<∞for every ​γ<γ0.\mathbb{E}\_{\mathbb{P}^{\*}}\big[\exp(\gamma^{2}\|B\|\_{2}^{2})\big]<\infty\quad\text{for every }\gamma<\gamma\_{0}. |  |

with

|  |  |  |
| --- | --- | --- |
|  | γ02‖σ−1‖F2>T​max⁡{ 4​β2−2​β,2β−2, 16, 8​β+8}\frac{\gamma\_{0}^{2}}{\left\|\sigma^{-1}\right\|\_{F}^{2}}>T\max\Big\{\,4\beta^{2}-2\beta,\ \tfrac{2}{\beta-2},\ 16,\ 8\beta+8\,\Big\} |  |

and β=α1−α\beta=\frac{\alpha}{1-\alpha}.

###### Theorem 6.

We denote α​(y)=𝔼ℙ∗​[LT​(B,y)]\alpha(y)=\mathbb{E}\_{\mathbb{P}^{\*}}\left[L\_{T}(B,y)\right] for each fixed y∈ℝdy\in\mathbb{R}^{d}. Under Assumption [5](https://arxiv.org/html/2512.01408v1#Thmassumption5 "Assumption 5. ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), as n→∞n\to\infty, we have the asymptotic stochastic upper bound:

|  |  |  |
| --- | --- | --- |
|  | n​Rn​(k∗)≲DL:=τ​Z2𝔼ℙ∗​[‖∫ℝdgk∗′​(α​(y))​∇bLT​(B,y)​φT​(y)​𝑑y‖22],nR\_{n}(k^{\*})\lesssim\_{D}L:=\frac{\tau Z^{2}}{\mathbb{E}\_{\mathbb{P}^{\*}}\left[\left\lVert\int\_{\mathbb{R}^{d}}g\_{k^{\*}}^{\prime}(\alpha(y))\nabla\_{b}L\_{T}(B,y)\varphi\_{T}(y)dy\right\rVert\_{2}^{2}\right]}, |  |

where
Z∼𝒩​(0,h​(ℙ∗))Z\sim\mathcal{N}(0,h(\mathbb{P}^{\*}))
and the functional hh is defined by

|  |  |  |
| --- | --- | --- |
|  | h​(ℙ∗)=∫∫gk∗′​(α​(y1))​gk∗′​(α​(y2))​Covℙ∗​(LT​(B,y1),LT​(B,y2))​φT​(y1)​φT​(y2)​𝑑y1​𝑑y2<∞.h(\mathbb{P}^{\*})=\int\int g\_{k^{\*}}^{\prime}(\alpha(y\_{1}))g\_{k^{\*}}^{\prime}(\alpha(y\_{2}))\text{Cov}\_{\mathbb{P}^{\*}}\left(L\_{T}(B,y\_{1}),L\_{T}(B,y\_{2})\right)\varphi\_{T}(y\_{1})\varphi\_{T}(y\_{2})dy\_{1}dy\_{2}<\infty. |  |

The proof of Theorem [6](https://arxiv.org/html/2512.01408v1#Thmtheorem6 "Theorem 6. ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") consists of six parts. First, we use Taylor expansions to separate terms in Rn​(k∗)R\_{n}(k^{\*}) and obtain Eq. ([54](https://arxiv.org/html/2512.01408v1#A4.E54 "In D.1 Part I ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")). Second, we estimate some remainder terms (R1R\_{1} and R2R\_{2} in Eq. ([54](https://arxiv.org/html/2512.01408v1#A4.E54 "In D.1 Part I ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"))). Third, we compute the optimal deterministic coupling in Eq. ([55](https://arxiv.org/html/2512.01408v1#A4.E55 "In D.3 Part III ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")). Fourth, we establish various senses of convergence to be used in the main statement. Fifth, we continue to compute the remainder term. Sixth, we summarize all the required assumptions and conclude the asymptotic result.

### D.1 Part I

To begin with, the uniqueness of k∗k^{\*} is easy to see. In order to prove Theorem [6](https://arxiv.org/html/2512.01408v1#Thmtheorem6 "Theorem 6. ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), we define a functional JJ on the space of probability measures such that (for notational convenience) g​(x)=gk∗​(x)g(x)=g\_{k^{\*}}(x) and

|  |  |  |
| --- | --- | --- |
|  | J​(ℙ)=∫ℝdg​(𝔼ℙ​[LT​(B,y)])​φT​(y)​𝑑y.J(\mathbb{P})=\int\_{\mathbb{R}^{d}}g\left(\mathbb{E}\_{\mathbb{P}}\left[L\_{T}(B,y)\right]\right)\varphi\_{T}(y)dy. |  |

In particular,

|  |  |  |
| --- | --- | --- |
|  | g′​(x)=11−α​(er​Tk∗)11−α​xα1−α,g^{\prime}(x)=\frac{1}{1-\alpha}\left(\frac{e^{rT}}{k^{\*}}\right)^{\frac{1}{1-\alpha}}x^{\frac{\alpha}{1-\alpha}}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | g′′​(x)=α(1−α)2​(er​Tk∗)11−α​x2​α−11−α,g^{\prime\prime}(x)=\frac{\alpha}{(1-\alpha)^{2}}\left(\frac{e^{rT}}{k^{\*}}\right)^{\frac{1}{1-\alpha}}x^{\frac{2\alpha-1}{1-\alpha}}, |  |

We notice that LTL\_{T} and gg are both twice continuously differentiable functions in each argument. Therefore, the RWP function becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rn​(k∗)\displaystyle R\_{n}(k^{\*}) | :=infℙ∈ℱk∗Dc​(ℙn,ℙ)\displaystyle:=\inf\_{\mathbb{P}\in\mathcal{F}\_{k^{\*}}}D\_{c}(\mathbb{P}\_{n},\mathbb{P}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =inf{Dc​(ℙ,ℙn):∫ℝdI​(k∗​e−r​T𝔼ℙ​[LT​(B,y)])​φT​(y)​𝑑y=x0​er​T}\displaystyle=\inf\left\{D\_{c}(\mathbb{P},\mathbb{P}\_{n}):\int\_{\mathbb{R}^{d}}I\left(\frac{k^{\*}e^{-rT}}{\mathbb{E}\_{\mathbb{P}}\left[L\_{T}(B,y)\right]}\right)\varphi\_{T}(y)dy=x\_{0}e^{rT}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =inf{Dc​(ℙ,ℙn):J​(ℙ)=J​(ℙ∗)}.\displaystyle=\inf\left\{D\_{c}(\mathbb{P},\mathbb{P}\_{n}):J(\mathbb{P})=J(\mathbb{P}^{\*})\right\}. |  |

Given the empirical measure ℙn\mathbb{P}\_{n}, we define the perturbed empirical measure ℙnΔ\mathbb{P}\_{n}^{\Delta} by pushing each atom B(i)B^{(i)} to B(i)+Δi​n−1/2B^{(i)}+\Delta\_{i}n^{-1/2} for Δi∈ℝd\Delta\_{i}\in\mathbb{R}^{d}. We want to show that for any fixed ε>0\varepsilon>0, for all sufficiently large nn, with probability at least 1−ε1-\varepsilon, there exists a correction Δ\Delta with ‖Δ‖n=Op​(1)\left\|\Delta\right\|\_{n}=O\_{p}(1) and J​(ℙnΔ)=J​(ℙ∗)J(\mathbb{P}\_{n}^{\Delta})=J(\mathbb{P}^{\*}), where we use the notation for γ∈ℤ\gamma\in\mathbb{Z}, ‖Δ‖nγ:=1n​∑i=1n‖Δi‖γ.\left\|\Delta\right\|\_{n}^{\gamma}:=\frac{1}{n}\sum\_{i=1}^{n}\left\|\Delta\_{i}\right\|^{\gamma}.

For each yy and ii, set hi:=Δi/nh\_{i}:=\Delta\_{i}/\sqrt{n}.
the Taylor theorem in the bb–variable gives

|  |  |  |
| --- | --- | --- |
|  | LT​(B(i)+hi,y)=LT​(B(i),y)+∇bLT​(B(i),y)⋅hi+∫01(1−t)​hi⊤​∇b2LT​(B(i)+t​hi,y)​hi​𝑑t.L\_{T}(B^{(i)}+h\_{i},y)=L\_{T}(B^{(i)},y)+\nabla\_{b}L\_{T}(B^{(i)},y)\!\cdot\!h\_{i}+\int\_{0}^{1}(1-t)\,h\_{i}^{\top}\nabla\_{b}^{2}L\_{T}(B^{(i)}+th\_{i},y)\,h\_{i}\,dt. |  |

Defining mℙ​(y)=𝔼ℙ​[LT​(B,y)]m\_{\mathbb{P}}(y)=\mathbb{E}\_{\mathbb{P}}\left[L\_{T}(B,y)\right] for a probability measure ℙ\mathbb{P} yields

|  |  |  |
| --- | --- | --- |
|  | mℙnΔ​(y)=mℙn​(y)+A1​(y)+A2​(y),m\_{\mathbb{P}\_{n}^{\Delta}}(y)=m\_{\mathbb{P}\_{n}}(y)\;+\;A\_{1}(y)\;+\;A\_{2}(y), |  |

with

|  |  |  |
| --- | --- | --- |
|  | A1​(y)=1n⋅1n​∑i=1n∇bLT​(B(i),y)⋅ΔiA\_{1}(y)=\frac{1}{\sqrt{n}}\cdot\frac{1}{n}\sum\_{i=1}^{n}\nabla\_{b}L\_{T}(B^{(i)},y)\cdot\Delta\_{i} |  |

and

|  |  |  |
| --- | --- | --- |
|  | A2​(y)=1n​∑i=1n∫01(1−t)​Δi⊤n​∇b2LT​(B(i)+t​Δin,y)​Δin​𝑑t.A\_{2}(y)=\frac{1}{n}\sum\_{i=1}^{n}\int\_{0}^{1}(1-t)\,\frac{\Delta\_{i}^{\top}}{\sqrt{n}}\,\nabla\_{b}^{2}L\_{T}\!\Big(B^{(i)}+t\tfrac{\Delta\_{i}}{\sqrt{n}},y\Big)\,\frac{\Delta\_{i}}{\sqrt{n}}\,dt. |  |

Another Taylor expansion gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(mℙnΔ​(y))\displaystyle g(m\_{\mathbb{P}\_{n}^{\Delta}}(y)) | =g​(mℙn​(y))+g′​(mℙn​(y))​(A1​(y)+A2​(y))\displaystyle=g(m\_{\mathbb{P}\_{n}}(y))+g^{\prime}(m\_{\mathbb{P}\_{n}}(y))(A\_{1}(y)+A\_{2}(y)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫01(1−t)​g′′​(mℙn​(y)+t​(A1​(y)+A2​(y)))​(A1​(y)+A2​(y))2​𝑑t,\displaystyle+\int\_{0}^{1}(1-t)g^{\prime\prime}(m\_{\mathbb{P}\_{n}}(y)+t(A\_{1}(y)+A\_{2}(y)))(A\_{1}(y)+A\_{2}(y))^{2}dt, |  |

which implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(ℙnΔ)−J​(ℙ∗)=J​(ℙn)−J​(ℙ∗)+∫g′​(mℙn​(y))​A1​(y)​φT​(y)​𝑑y+R1+R2,J(\mathbb{P}\_{n}^{\Delta})-J(\mathbb{P}^{\*})=J(\mathbb{P}\_{n})-J(\mathbb{P}^{\*})+\int g^{\prime}(m\_{\mathbb{P}\_{n}}(y))A\_{1}(y)\varphi\_{T}(y)dy+R\_{1}+R\_{2}, |  | (54) |

where

|  |  |  |
| --- | --- | --- |
|  | R1=∫g′​(mℙn​(y))​A2​(y)​φT​(y)​𝑑y,R\_{1}=\int g^{\prime}(m\_{\mathbb{P}\_{n}}(y))A\_{2}(y)\varphi\_{T}(y)dy, |  |

and

|  |  |  |
| --- | --- | --- |
|  | R2=∫01(1−t)​∫g′′​(mℙn​(y)+t​(A1​(y)+A2​(y)))​(A1​(y)+A2​(y))2​φT​(y)​𝑑y​𝑑t.R\_{2}=\int\_{0}^{1}(1-t)\int g^{\prime\prime}(m\_{\mathbb{P}\_{n}}(y)+t(A\_{1}(y)+A\_{2}(y)))(A\_{1}(y)+A\_{2}(y))^{2}\varphi\_{T}(y)dydt. |  |

If we define

|  |  |  |
| --- | --- | --- |
|  | Ci​(n)=∫g′​(mℙn​(y))​∇bLT​(B(i),y)​φT​(y)​𝑑y,C\_{i}(n)=\int g^{\prime}(m\_{\mathbb{P}\_{n}}(y))\nabla\_{b}L\_{T}(B^{(i)},y)\varphi\_{T}(y)dy, |  |

then

|  |  |  |
| --- | --- | --- |
|  | ∫g′​(mℙn​(y))​A1​(y)​φT​(y)​𝑑y=1n1/2​1n​∑i=1nCi​(n)⋅Δi.\int g^{\prime}(m\_{\mathbb{P}\_{n}}(y))A\_{1}(y)\varphi\_{T}(y)dy=\frac{1}{n^{1/2}}\frac{1}{n}\sum\_{i=1}^{n}C\_{i}(n)\cdot\Delta\_{i}. |  |

### D.2 Part II

In this part, we will present Lemmas [3](https://arxiv.org/html/2512.01408v1#Thmlemma3 "Lemma 3. ‣ D.2.1 Part II-i ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")-[6](https://arxiv.org/html/2512.01408v1#Thmlemma6 "Lemma 6. ‣ D.2.2 Part II-ii ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") to estimate R1R\_{1} and R2R\_{2}. Proofs of [3](https://arxiv.org/html/2512.01408v1#Thmlemma3 "Lemma 3. ‣ D.2.1 Part II-i ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")-[5](https://arxiv.org/html/2512.01408v1#Thmlemma5 "Lemma 5. ‣ D.2.2 Part II-ii ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") are similar to the estimates in Section [C](https://arxiv.org/html/2512.01408v1#A3 "Appendix C Generalization of Nonlinear Perturbation Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), where the sub-Gaussian assumptions are used to bound integrability conditions after standard Gaussian integral computations. We only give the proof details of the most complicated term of Lemma [4](https://arxiv.org/html/2512.01408v1#Thmlemma4 "Lemma 4. ‣ D.2.1 Part II-i ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections").

#### D.2.1 Part II-i

We propose the following sub-Gaussian assumption.

###### Assumption 6.

Suppose there exists γ0>0\gamma\_{0}>0 such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ∗​[exp⁡(γ2​‖B‖22)]<∞for every ​γ<γ0.\mathbb{E}\_{\mathbb{P}^{\*}}\big[\exp(\gamma^{2}\|B\|\_{2}^{2})\big]<\infty\quad\text{for every }\gamma<\gamma\_{0}. |  |

with

|  |  |  |
| --- | --- | --- |
|  | γ02‖σ−1‖F2>T​max⁡{2​(2​β2−β),4}\frac{\gamma\_{0}^{2}}{\left\|\sigma^{-1}\right\|\_{F}^{2}}>T\max\left\{2(2\beta^{2}-\beta),4\right\} |  |

and β=α1−α\beta=\frac{\alpha}{1-\alpha}.

###### Lemma 3.

In the context of the proof of Theorem [6](https://arxiv.org/html/2512.01408v1#Thmtheorem6 "Theorem 6. ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), under Assumption [6](https://arxiv.org/html/2512.01408v1#Thmassumption6 "Assumption 6. ‣ D.2.1 Part II-i ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), when α<1\alpha<1 and α≠0\alpha\neq 0, then there exists a constant C>0C>0 such that

|  |  |  |
| --- | --- | --- |
|  | |R1|=Op​(1n​(1n​∑i=1n‖Δi‖4)1/2​[1+‖Δ‖nn+1n​(1n​∑i=1n‖Δi‖4)1/2]​exp⁡(C′​max1≤i≤n⁡‖Δi‖2n)).|R\_{1}|=O\_{p}\!\left(\frac{1}{n}\Big(\frac{1}{n}\sum\_{i=1}^{n}\|\Delta\_{i}\|^{4}\Big)^{\!1/2}\,\Big[1+\frac{\|\Delta\|\_{n}}{\sqrt{n}}+\frac{1}{n}\Big(\frac{1}{n}\sum\_{i=1}^{n}\|\Delta\_{i}\|^{4}\Big)^{\!1/2}\Big]\,\exp\!\Big(C^{\prime}\,\max\_{1\leq i\leq n}\frac{\|\Delta\_{i}\|^{2}}{n}\Big)\right). |  |

###### Assumption 7.

Suppose there exists γ0>0\gamma\_{0}>0 such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ∗​[exp⁡(γ2​‖B‖22)]<∞for every ​γ<γ0.\mathbb{E}\_{\mathbb{P}^{\*}}\big[\exp(\gamma^{2}\|B\|\_{2}^{2})\big]<\infty\quad\text{for every }\gamma<\gamma\_{0}. |  |

with

|  |  |  |
| --- | --- | --- |
|  | γ02‖σ−1‖F2>T​max⁡{2​s​(2−1),6,2​p2−p},\frac{\gamma\_{0}^{2}}{\left\|\sigma^{-1}\right\|\_{F}^{2}}>T\max\left\{2s(2-1),6,2p^{2}-p\right\}, |  |

where s=1p−1s=\frac{1}{p-1} and p=β−1p=\beta-1 with β=α1−α\beta=\frac{\alpha}{1-\alpha}.

###### Lemma 4.

In the context of proof of Theorem [6](https://arxiv.org/html/2512.01408v1#Thmtheorem6 "Theorem 6. ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), under Assumption [7](https://arxiv.org/html/2512.01408v1#Thmassumption7 "Assumption 7. ‣ D.2.1 Part II-i ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), when α<1\alpha<1 and α≠0\alpha\neq 0, then there exists a constant C>0C>0 such that

|  |  |  |
| --- | --- | --- |
|  | |R2|=Op​(‖Δ‖n2n​exp⁡(C​max1≤i≤n⁡‖Δi‖2n))+Op​(‖Δ‖n2n⋅max1≤i≤n⁡‖Δi‖2n​exp⁡(C​max1≤i≤n⁡‖Δi‖2n)).|R\_{2}|=O\_{p}\left(\frac{\left\|\Delta\right\|\_{n}^{2}}{n}\exp\left(C\max\_{1\ \leq i\leq n}\frac{\left\|\Delta\_{i}\right\|^{2}}{n}\right)\right)+O\_{p}\!\left(\frac{\|\Delta\|\_{n}^{2}}{n}\cdot\frac{\max\_{1\leq i\leq n}\|\Delta\_{i}\|^{2}}{n}\;\exp\!\Big(C\,\max\_{1\leq i\leq n}\frac{\|\Delta\_{i}\|^{2}}{n}\Big)\right). |  |

###### Proof.

Bounding R2R\_{2} is equivalent to bound these two terms:

|  |  |  |
| --- | --- | --- |
|  | |R2|≤I1+I2,|R\_{2}|\leq I\_{1}+I\_{2}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | I1=2​∫01(1−t)​∫|g′′​(mℙn​(y)+t​(A1​(y)+A2​(y)))|​A1​(y)2​φT​(y)​𝑑y​𝑑tI\_{1}=2\int\_{0}^{1}(1-t)\int\left|g^{\prime\prime}(m\_{\mathbb{P}\_{n}}(y)+t(A\_{1}(y)+A\_{2}(y)))\right|A\_{1}(y)^{2}\varphi\_{T}(y)dydt |  |

and

|  |  |  |
| --- | --- | --- |
|  | I2=2​∫01(1−t)​∫|g′′​(mℙn​(y)+t​(A1​(y)+A2​(y)))|​A2​(y)2​φT​(y)​𝑑y​𝑑t.I\_{2}=2\int\_{0}^{1}(1-t)\int\left|g^{\prime\prime}(m\_{\mathbb{P}\_{n}}(y)+t(A\_{1}(y)+A\_{2}(y)))\right|A\_{2}(y)^{2}\varphi\_{T}(y)dydt. |  |

Recall that β=α1−α\beta=\frac{\alpha}{1-\alpha} and g′′​(x)=Cα​xβ−1g^{\prime\prime}(x)=C\_{\alpha}\,x^{\beta-1} for a constant CαC\_{\alpha}. Cauchy–Schwarz inequality yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | |A1​(y)|\displaystyle|A\_{1}(y)| | ≤1n⋅1n​(∑i=1n‖∇bLT​(B(i),y)‖22)1/2​(∑i=1n‖Δi‖22)1/2=‖Δ‖n 2n​(Ξ2¯​(y))1/2,\displaystyle\leq\frac{1}{\sqrt{n}}\cdot\frac{1}{n}\Big(\sum\_{i=1}^{n}\|\nabla\_{b}L\_{T}(B^{(i)},y)\|\_{2}^{2}\Big)^{\!1/2}\!\Big(\sum\_{i=1}^{n}\|\Delta\_{i}\|\_{2}^{2}\Big)^{\!1/2}=\sqrt{\frac{\|\Delta\|\_{n}^{\,2}}{n}}\;\Big(\overline{\Xi^{2}}(y)\Big)^{\!1/2}, |  |

with

|  |  |  |
| --- | --- | --- |
|  | Ξ2¯​(y):=1n​∑i=1n‖∇bLT​(B(i),y)‖22≤C1​(‖y‖22​L2¯​(y)+T2​A2​L2¯​(y)),\overline{\Xi^{2}}(y):=\frac{1}{n}\sum\_{i=1}^{n}\|\nabla\_{b}L\_{T}(B^{(i)},y)\|\_{2}^{2}\ \leq\ C\_{1}\Big(\|y\|\_{2}^{2}\,\overline{L^{2}}(y)\;+\;T^{2}\,\overline{A^{2}L^{2}}(y)\Big), |  |

where

|  |  |  |
| --- | --- | --- |
|  | L2¯​(y):=1n​∑i=1nLT​(B(i),y)2,A2​L2¯​(y):=1n​∑i=1n‖a​(B(i))‖22​LT​(B(i),y)2,\overline{L^{2}}(y):=\frac{1}{n}\sum\_{i=1}^{n}L\_{T}(B^{(i)},y)^{2},\qquad\overline{A^{2}L^{2}}(y):=\frac{1}{n}\sum\_{i=1}^{n}\|a(B^{(i)})\|\_{2}^{2}\,L\_{T}(B^{(i)},y)^{2}, |  |

and therefore,

|  |  |  |
| --- | --- | --- |
|  | |A1​(y)|2≤‖Δ‖n 2n​C1​(‖y‖22​L2¯​(y)+T2​A2​L2¯​(y)).|A\_{1}(y)|^{2}\;\leq\;\frac{\|\Delta\|\_{n}^{\,2}}{n}\;C\_{1}\Big(\|y\|\_{2}^{2}\,\overline{L^{2}}(y)\;+\;T^{2}\,\overline{A^{2}L^{2}}(y)\Big). |  |

Recall that hi:=Δi/nh\_{i}:=\Delta\_{i}/\sqrt{n}. Define the shifted mixture

|  |  |  |
| --- | --- | --- |
|  | mℙn(h)​(y):=1n​∑i=1nLT​(B(i)+hi,y).m\_{\mathbb{P}\_{n}}^{(h)}(y):=\frac{1}{n}\sum\_{i=1}^{n}L\_{T}(B^{(i)}+h\_{i},y). |  |

Therefore

|  |  |  |
| --- | --- | --- |
|  | xt​(y):=(1−t)​mℙn​(y)+t​mℙn(h)​(y)=mℙn​(y)+t​(A1​(y)+A2​(y)).x\_{t}(y):=(1-t)\,m\_{\mathbb{P}\_{n}}(y)+t\,m\_{\mathbb{P}\_{n}}^{(h)}(y)=m\_{\mathbb{P}\_{n}}(y)+t\big(A\_{1}(y)+A\_{2}(y)\big). |  |

Let p:=β−1=α1−α−1p:=\beta-1=\frac{\alpha}{1-\alpha}-1.
We write m:=mℙn​(y)>0m:=m\_{\mathbb{P}\_{n}}(y)>0 and m(h):=mℙn(h)​(y)>0m^{(h)}:=m\_{\mathbb{P}\_{n}}^{(h)}(y)>0 to lighten notation, so
xt=(1−t)​m+t​m(h)x\_{t}=(1-t)m+tm^{(h)}.

When p<0p<0 or p≥1p\geq 1,
the function f​(x)=xpf(x)=x^{p} on (0,∞)(0,\infty) is convex. Therefore

|  |  |  |
| --- | --- | --- |
|  | xtp=f​((1−t)​m+t​m(h))≤(1−t)​f​(m)+t​f​(m(h))=(1−t)​mp+t​(m(h))p≤mp+(m(h))p.x\_{t}^{p}=f\big((1-t)m+tm^{(h)}\big)\;\leq\;(1-t)f(m)+tf(m^{(h)})=(1-t)m^{p}+t(m^{(h)})^{p}\;\leq\;m^{p}+(m^{(h)})^{p}. |  |

When p∈(0,1)p\in(0,1), the map f​(x)=xpf(x)=x^{p} is increasing and concave. Since xt≤m+m(h)x\_{t}\leq m+m^{(h)} and ff is increasing, then

|  |  |  |
| --- | --- | --- |
|  | xtp≤(m+m(h))p≤mp+(m(h))p,x\_{t}^{p}\ \leq\ (m+m^{(h)})^{p}\ \leq\ m^{p}+(m^{(h)})^{p}, |  |

where the last step uses the subadditivity (a+b)p≤ap+bp(a+b)^{p}\leq a^{p}+b^{p} for a,b≥0a,b\geq 0 and 0<p≤10<p\leq 1.

Therefore,

|  |  |  |
| --- | --- | --- |
|  | |g′′​(xt)|=|Cα|​xtp≤|Cα|​(mβ−1+(m(h))β−1).|g^{\prime\prime}(x\_{t})|=|C\_{\alpha}|\,x\_{t}^{p}\leq|C\_{\alpha}|\big(m^{\beta-1}+(m^{(h)})^{\beta-1}\big). |  |

Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | I1\displaystyle I\_{1} | =2​∫01(1−t)​∫|g′′​(xt)|​A12​(y)​φT​(y)​𝑑y≤Cn​‖Δ‖n 2​(J1+J2+J1(h)+J2(h)),\displaystyle=2\!\int\_{0}^{1}(1-t)\!\int|g^{\prime\prime}(x\_{t})|\,A\_{1}^{2}(y)\,\varphi\_{T}(y)dy\ \leq\ \frac{C}{n}\,\|\Delta\|\_{n}^{\,2}\,\Big(J\_{1}+J\_{2}+J\_{1}^{(h)}+J\_{2}^{(h)}\Big), |  |

where

|  |  |  |
| --- | --- | --- |
|  | J1:=∫‖y‖2​mℙnβ−1​L2¯​φT,J2:=∫mℙnβ−1​A2​L2¯​φT,J\_{1}:=\int\|y\|^{2}m\_{\mathbb{P}\_{n}}^{\beta-1}\,\overline{L^{2}}\,\varphi\_{T},\qquad J\_{2}:=\int m\_{\mathbb{P}\_{n}}^{\beta-1}\,\overline{A^{2}L^{2}}\,\varphi\_{T}, |  |

|  |  |  |
| --- | --- | --- |
|  | J1(h):=∫‖y‖2​(mℙn(h))β−1​L2¯​φT,J2(h):=∫(mℙn(h))β−1​A2​L2¯​φT.J\_{1}^{(h)}:=\int\|y\|^{2}(m\_{\mathbb{P}\_{n}}^{(h)})^{\beta-1}\,\overline{L^{2}}\,\varphi\_{T},\qquad J\_{2}^{(h)}:=\int(m\_{\mathbb{P}\_{n}}^{(h)})^{\beta-1}\,\overline{A^{2}L^{2}}\,\varphi\_{T}. |  |

We first focus on the case when p:=β−1<0p:=\beta-1<0, by the Jensen inequality,

|  |  |  |
| --- | --- | --- |
|  | mℙn​(y)=𝔼ℙn​[e⟨a​(B),y⟩−T2​‖a​(B)‖22]≥exp⁡(⟨𝔼ℙn​[a​(B)],y⟩−T2​𝔼ℙn​[‖a​(B)‖22]).m\_{\mathbb{P}\_{n}}(y)\;=\;\mathbb{E}\_{\mathbb{P}\_{n}}\big[e^{\langle a(B),y\rangle-\frac{T}{2}\|a(B)\|\_{2}^{2}}\big]\;\geq\;\exp\!\Big(\langle\mathbb{E}\_{\mathbb{P}\_{n}}[a(B)],y\rangle-\tfrac{T}{2}\,\mathbb{E}\_{\mathbb{P}\_{n}}\left[\|a(B)\|\_{2}^{2}\right]\Big). |  |

Raising to the negative power p<0p<0 reverses the inequality, giving

|  |  |  |
| --- | --- | --- |
|  | mℙn​(y)p≤Ca​exp⁡(p​⟨v,y⟩),Ca:=exp⁡(−p​T2​𝔼ℙn​[‖a​(B)‖22]),v:=𝔼ℙn​[a​(B)].m\_{\mathbb{P}\_{n}}(y)^{p}\;\leq\;C\_{a}\,\exp\!\big(p\,\langle v,y\rangle\big),\qquad C\_{a}:=\exp\!\Big(-\tfrac{pT}{2}\,\mathbb{E}\_{\mathbb{P}\_{n}}\left[\|a(B)\|\_{2}^{2}\right]\Big),\ \ v:=\mathbb{E}\_{\mathbb{P}\_{n}}[a(B)]. |  |

We denote ci:=σ−1​hic\_{i}:=\sigma^{-1}h\_{i}, then

|  |  |  |
| --- | --- | --- |
|  | mℙn(h)​(y)=1n​∑i=1nLT​(B(i)+hi,y)=1n​∑i=1nexp⁡(⟨a​(B(i))+ci,y⟩−T2​‖a​(B(i))+ci‖22).m\_{\mathbb{P}\_{n}}^{(h)}(y)=\frac{1}{n}\sum\_{i=1}^{n}L\_{T}(B^{(i)}+h\_{i},y)=\frac{1}{n}\sum\_{i=1}^{n}\exp\!\Big(\,\big\langle a(B^{(i)})+c\_{i},\,y\big\rangle-\tfrac{T}{2}\|a(B^{(i)})+c\_{i}\|\_{2}^{2}\Big). |  |

Introduce the notations

|  |  |  |
| --- | --- | --- |
|  | vh:=1n​∑i=1n(a​(B(i))+ci),s2,h:=1n​∑i=1n‖a​(B(i))+ci‖22,Hn:=max1≤i≤n⁡‖ci‖2.v\_{h}:=\frac{1}{n}\sum\_{i=1}^{n}\big(a(B^{(i)})+c\_{i}\big),\qquad s\_{2,h}:=\frac{1}{n}\sum\_{i=1}^{n}\|a(B^{(i)})+c\_{i}\|\_{2}^{2},\qquad H\_{n}:=\max\_{1\leq i\leq n}\|c\_{i}\|\_{2}. |  |

By Jensen’s inequality,

|  |  |  |
| --- | --- | --- |
|  | mℙn(h)​(y)≥exp⁡(⟨vh,y⟩−T2​s2,h).m\_{\mathbb{P}\_{n}}^{(h)}(y)\ \geq\ \exp\!\Big(\,\langle v\_{h},y\rangle-\tfrac{T}{2}\,s\_{2,h}\Big). |  |

Since p<0p<0, raising both sides to the power pp reverses the inequality:

|  |  |  |
| --- | --- | --- |
|  | (mℙn(h)​(y))p≤exp⁡(p​⟨vh,y⟩−p​T2​s2,h).\big(m\_{\mathbb{P}\_{n}}^{(h)}(y)\big)^{p}\ \leq\ \exp\!\Big(\,p\,\langle v\_{h},y\rangle-\tfrac{pT}{2}\,s\_{2,h}\Big). |  |

Set

|  |  |  |
| --- | --- | --- |
|  | s2:=𝔼ℙn​[‖a​(B)‖22],Ca:=exp⁡(−p​T2​s2).s\_{2}:=\mathbb{E}\_{\mathbb{P}\_{n}}\!\big[\|a(B)\|\_{2}^{2}\big],\qquad C\_{a}:=\exp\!\Big(-\tfrac{pT}{2}\,s\_{2}\Big). |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | J1≤Can​∑i=1n∫‖y‖22​ep​⟨v,y⟩​LT​(B(i),y)2​φT​(y)​𝑑y.J\_{1}\ \leq\ \frac{C\_{a}}{n}\sum\_{i=1}^{n}\int\|y\|\_{2}^{2}\,e^{\,p\langle v,y\rangle}\,L\_{T}(B^{(i)},y)^{2}\,\varphi\_{T}(y)\,dy. |  |

Write ai:=a​(B(i))a\_{i}:=a(B^{(i)}) and note LT​(B(i),y)2=exp⁡(2​⟨ai,y⟩−T​‖ai‖22)L\_{T}(B^{(i)},y)^{2}=\exp(2\langle a\_{i},y\rangle-T\|a\_{i}\|\_{2}^{2}).
Let Y∼N​(0,T​Id)Y\sim N(0,TI\_{d}) so φT\varphi\_{T} is its density. Then, with

|  |  |  |
| --- | --- | --- |
|  | λi:=2​ai+p​v∈ℝd,\lambda\_{i}:=2a\_{i}+p\,v\in\mathbb{R}^{d}, |  |

|  |  |  |
| --- | --- | --- |
|  | ∫‖y‖22​ep​⟨v,y⟩​LT​(B(i),y)2​φT​(y)​𝑑y=e−T​‖ai‖22​(T​d+T2​‖λi‖22)​eT2​‖λi‖22.\int\|y\|\_{2}^{2}\,e^{\,p\langle v,y\rangle}\,L\_{T}(B^{(i)},y)^{2}\,\varphi\_{T}(y)\,dy=e^{-T\|a\_{i}\|\_{2}^{2}}\,(Td+T^{2}\|\lambda\_{i}\|\_{2}^{2})\,e^{\frac{T}{2}\|\lambda\_{i}\|\_{2}^{2}}. |  |

Therefore

|  |  |  |
| --- | --- | --- |
|  | J1≤Can​∑i=1n(T​d+T2​‖λi‖22)​exp⁡(T2​‖λi‖22−T​‖ai‖22).J\_{1}\ \leq\ \frac{C\_{a}}{n}\sum\_{i=1}^{n}\Big(Td+T^{2}\|\lambda\_{i}\|\_{2}^{2}\Big)\,\exp\!\Big(\tfrac{T}{2}\|\lambda\_{i}\|\_{2}^{2}-T\|a\_{i}\|\_{2}^{2}\Big). |  |

By the inequality (‖u+z‖22≤2​‖u‖22+2​‖z‖22)(\|u+z\|\_{2}^{2}\leq 2\|u\|\_{2}^{2}+2\|z\|\_{2}^{2}) with u=2​aiu=2a\_{i}, z=p​vz=pv:

|  |  |  |
| --- | --- | --- |
|  | ‖λi‖22=‖2​ai+p​v‖22≤ 8​‖ai‖22+2​p2​‖v‖22,\|\lambda\_{i}\|\_{2}^{2}=\|2a\_{i}+pv\|\_{2}^{2}\ \leq\ 8\|a\_{i}\|\_{2}^{2}+2p^{2}\|v\|\_{2}^{2}, |  |

hence

|  |  |  |
| --- | --- | --- |
|  | T2​‖λi‖22−T​‖ai‖22≤ 3​T​‖ai‖22+T​p2​‖v‖22.\frac{T}{2}\|\lambda\_{i}\|\_{2}^{2}-T\|a\_{i}\|\_{2}^{2}\ \leq\ 3T\|a\_{i}\|\_{2}^{2}+Tp^{2}\|v\|\_{2}^{2}. |  |

Also ‖λi‖22≤8​‖ai‖22+2​p2​‖v‖22\|\lambda\_{i}\|\_{2}^{2}\leq 8\|a\_{i}\|\_{2}^{2}+2p^{2}\|v\|\_{2}^{2} implies
T​d+T2​‖λi‖22≤C​(1+‖ai‖22+‖v‖22)Td+T^{2}\|\lambda\_{i}\|\_{2}^{2}\leq C\big(1+\|a\_{i}\|\_{2}^{2}+\|v\|\_{2}^{2}\big)
for a constant C=C​(T,p,d)C=C(T,p,d).
Therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | J1\displaystyle J\_{1}\ | ≤C​Ca​eT​p2​‖v‖22​1n​∑i=1n(1+‖ai‖22+‖v‖22)​e3​T​‖ai‖22.\displaystyle\leq\ C\,C\_{a}\,e^{Tp^{2}\|v\|\_{2}^{2}}\,\frac{1}{n}\sum\_{i=1}^{n}\big(1+\|a\_{i}\|\_{2}^{2}+\|v\|\_{2}^{2}\big)\,e^{3T\|a\_{i}\|\_{2}^{2}}. |  |

Set

|  |  |  |
| --- | --- | --- |
|  | An:=1n​∑i=1ne3​T​‖ai‖22,Bn:=1n​∑i=1n‖ai‖22​e3​T​‖ai‖22.A\_{n}:=\frac{1}{n}\sum\_{i=1}^{n}e^{3T\|a\_{i}\|\_{2}^{2}},\qquad B\_{n}:=\frac{1}{n}\sum\_{i=1}^{n}\|a\_{i}\|\_{2}^{2}\,e^{3T\|a\_{i}\|\_{2}^{2}}. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | J1≤C​Ca​eT​p2​‖v‖22​[(1+‖v‖22)​An+Bn].J\_{1}\ \leq\ C\,C\_{a}\,e^{Tp^{2}\|v\|\_{2}^{2}}\,\Big[(1+\|v\|\_{2}^{2})\,A\_{n}+B\_{n}\Big]. |  |

Since a​(B)=σ−1​B−ma(B)=\sigma^{-1}B-m, we have
‖a​(B)‖22≤2​‖σ−1​B‖22+2​‖m‖22\|a(B)\|\_{2}^{2}\leq 2\|\sigma^{-1}B\|\_{2}^{2}+2\|m\|\_{2}^{2},
and thus

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[e3​T​‖a​(B)‖22]≤e6​T​‖m‖22​𝔼​[e6​T​‖σ−1​B‖22]≤e6​T​‖m‖22​𝔼​[e6​T​‖σ−1‖F2​‖B‖22].\mathbb{E}\big[e^{3T\|a(B)\|\_{2}^{2}}\big]\ \leq\ e^{6T\|m\|\_{2}^{2}}\,\mathbb{E}\big[e^{6T\|\sigma^{-1}B\|\_{2}^{2}}\big]\ \leq\ e^{6T\|m\|\_{2}^{2}}\,\mathbb{E}\big[e^{6T\|\sigma^{-1}\|\_{F}^{2}\|B\|\_{2}^{2}}\big]. |  |

Hence 𝔼​[e3​T​‖a​(B)‖22]<∞\,\mathbb{E}[e^{3T\|a(B)\|\_{2}^{2}}]<\infty\, if the sub Gaussian parameter satisfies γ02‖σ−1‖F2> 6​T.\frac{\gamma\_{0}^{2}}{\|\sigma^{-1}\|\_{F}^{2}}\;>\;6T. The same argument with a polynomial prefactor yields
𝔼​[‖a​(B)‖22​e3​T​‖a​(B)‖22]<∞\mathbb{E}[\|a(B)\|\_{2}^{2}e^{3T\|a(B)\|\_{2}^{2}}]<\infty.
By the law of large numbers, An=Op​(1)A\_{n}=O\_{p}(1) and Bn=Op​(1)B\_{n}=O\_{p}(1). Also, by Jensen inequality,
‖v‖22=‖1n​∑ai‖22≤1n​∑‖ai‖22\|v\|\_{2}^{2}=\big\|\tfrac{1}{n}\sum a\_{i}\big\|\_{2}^{2}\leq\tfrac{1}{n}\sum\|a\_{i}\|\_{2}^{2},
so ‖v‖22=Op​(1)\|v\|\_{2}^{2}=O\_{p}(1) and therefore Ca​eT​p2​‖v‖22=Op​(1)C\_{a}e^{Tp^{2}\|v\|\_{2}^{2}}=O\_{p}(1).
Thus J1=Op​(1)J\_{1}=O\_{p}(1). The bound of J2=Op​(1)J\_{2}=O\_{p}(1) is almost verbatim since there is no additional term on the exponential.

Similarly, it suffices to upper bound J1(h)J\_{1}^{(h)}.
We introduce new analogous notation

|  |  |  |
| --- | --- | --- |
|  | Ca(h):=exp⁡(−p​T2​s2,h).C\_{a}^{(h)}:=\exp\!\Big(-\tfrac{pT}{2}\,s\_{2,h}\Big). |  |

Therefore

|  |  |  |
| --- | --- | --- |
|  | J1(h)≤Ca(h)n​∑i=1n∫‖y‖22​ep​⟨vh,y⟩​LT​(B(i),y)2​φT​(y)​𝑑y.J\_{1}^{(h)}\ \leq\ \frac{C\_{a}^{(h)}}{n}\sum\_{i=1}^{n}\int\|y\|\_{2}^{2}\,e^{\,p\langle v\_{h},y\rangle}\,L\_{T}(B^{(i)},y)^{2}\,\varphi\_{T}(y)\,dy. |  |

An analogous computation of the case of J1J\_{1} shows that

|  |  |  |
| --- | --- | --- |
|  | J1(h)≤C​Ca(h)​eT​p2​‖vh‖22​1n​∑i=1n(1+‖ai‖22+‖vh‖22)​e3​T​‖ai‖22.J\_{1}^{(h)}\ \leq\ C\,C\_{a}^{(h)}\,e^{Tp^{2}\|v\_{h}\|\_{2}^{2}}\,\frac{1}{n}\sum\_{i=1}^{n}\big(1+\|a\_{i}\|\_{2}^{2}+\|v\_{h}\|\_{2}^{2}\big)\,e^{3T\|a\_{i}\|\_{2}^{2}}. |  |

Set

|  |  |  |
| --- | --- | --- |
|  | An:=1n​∑i=1ne3​T​‖ai‖22,Bn:=1n​∑i=1n‖ai‖22​e3​T​‖ai‖22.A\_{n}:=\frac{1}{n}\sum\_{i=1}^{n}e^{3T\|a\_{i}\|\_{2}^{2}},\qquad B\_{n}:=\frac{1}{n}\sum\_{i=1}^{n}\|a\_{i}\|\_{2}^{2}\,e^{3T\|a\_{i}\|\_{2}^{2}}. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | J1(h)≤C​Ca(h)​eT​p2​‖vh‖22​[(1+‖vh‖22)​An+Bn].J\_{1}^{(h)}\ \leq\ C\,C\_{a}^{(h)}\,e^{Tp^{2}\|v\_{h}\|\_{2}^{2}}\,\Big[(1+\|v\_{h}\|\_{2}^{2})\,A\_{n}+B\_{n}\Big]. |  |

Note
‖vh‖2≤‖v‖2+c¯,c¯:=1n​∑i‖ci‖2≤Hn,\|v\_{h}\|\_{2}\leq\|v\|\_{2}+\bar{c},\ \bar{c}:=\tfrac{1}{n}\sum\_{i}\|c\_{i}\|\_{2}\leq H\_{n},
so ‖vh‖22≤2​‖v‖22+2​Hn2\|v\_{h}\|\_{2}^{2}\leq 2\|v\|\_{2}^{2}+2H\_{n}^{2}. Also
s2,h≤2​s2+2​Hn2,s2:=1n​∑i‖ai‖22,s\_{2,h}\leq 2\,s\_{2}+2\,H\_{n}^{2},\ \ s\_{2}:=\tfrac{1}{n}\sum\_{i}\|a\_{i}\|\_{2}^{2},
hence

|  |  |  |
| --- | --- | --- |
|  | Ca(h)​eT​p2​‖vh‖22≤eC​Hn2​exp⁡(−p​T2​s2)⏟=⁣:Ca​exp⁡(T​p2​‖v‖22).C\_{a}^{(h)}\,e^{Tp^{2}\|v\_{h}\|\_{2}^{2}}\ \leq\ e^{C\,H\_{n}^{2}}\,\underbrace{\exp\!\Big(-\tfrac{pT}{2}\,s\_{2}\Big)}\_{=:C\_{a}}\,\exp\!\big(Tp^{2}\|v\|\_{2}^{2}\big). |  |

Under the same sub-Gaussian condition as for J1J\_{1},

|  |  |  |
| --- | --- | --- |
|  | An=Op​(1),Bn=Op​(1),‖v‖2=Op​(1),A\_{n}=O\_{p}(1),\quad B\_{n}=O\_{p}(1),\quad\|v\|\_{2}=O\_{p}(1), |  |

so for a constant C>0C>0,

|  |  |  |
| --- | --- | --- |
|  | J1(h)=Op​(eC​Hn2)=Op​(exp⁡(C​max1≤i≤n⁡‖Δ‖2n)).\ J\_{1}^{(h)}\ =\ O\_{p}\!\big(e^{CH\_{n}^{2}}\big)=O\_{p}\left(\exp\left(C\max\_{1\leq i\leq n}\frac{\left\|\Delta\right\|^{2}}{n}\right)\right). |  |

Therefore, when p<0p<0,

|  |  |  |
| --- | --- | --- |
|  | I1=Op​(‖Δ‖n2n​exp⁡(C​max1≤i≤n⁡‖Δ‖2n)).I\_{1}=O\_{p}\left(\frac{\left\|\Delta\right\|^{2}\_{n}}{n}\exp\left(C\max\_{1\leq i\leq n}\frac{\left\|\Delta\right\|^{2}}{n}\right)\right). |  |

Next we bound I1I\_{1} in the case when p≥0p\geq 0. It suffices to consider J1J\_{1} and J1(h)J\_{1}^{(h)} here again.
First we assume p∈(0,1)p\in(0,1), then
by Hölder ineqaulity with exponents r=1pr=\frac{1}{p}, s=11−ps=\frac{1}{1-p},

|  |  |  |
| --- | --- | --- |
|  | J1=∫‖y‖2​mℙn​(y)p​L2¯​(y)​φT​(y)​𝑑y≤(∫mℙn​(y)​φT​(y)​𝑑y)p​(∫‖y‖2​s​L2¯​(y)s​φT​(y)​𝑑y)1/s.J\_{1}=\int\|y\|^{2}\,m\_{\mathbb{P}\_{n}}(y)^{p}\,\overline{L^{2}}(y)\,\varphi\_{T}(y)\,dy\ \leq\ \Big(\int m\_{\mathbb{P}\_{n}}(y)\,\varphi\_{T}(y)\,dy\Big)^{\!p}\Big(\int\|y\|^{2s}\,\overline{L^{2}}(y)^{\,s}\,\varphi\_{T}(y)\,dy\Big)^{\!1/s}. |  |

Since ∫LT​(b,y)​φT​(y)​𝑑y=1\int L\_{T}(b,y)\varphi\_{T}(y)dy=1 for all bb, Fubini gives ∫mℙn​φT=1\int m\_{\mathbb{P}\_{n}}\varphi\_{T}=1,
so the first factor is 11. For the second term, by convexity of x↦xsx\mapsto x^{s} (s>1s>1),

|  |  |  |  |
| --- | --- | --- | --- |
|  | J1\displaystyle J\_{1}\ | ≤(1n​∑i=1n∫‖y‖2​s​LT​(B(i),y)2​s​φT​(y)​𝑑y)1/s\displaystyle\leq\ \Big(\tfrac{1}{n}\sum\_{i=1}^{n}\int\|y\|^{2s}L\_{T}(B^{(i)},y)^{2s}\varphi\_{T}(y)dy\Big)^{\!1/s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​(1n​∑i=1n(1+‖ai‖2​s)​eT​s​(2​s−1)​‖ai‖2)1/s.\displaystyle\leq\ C\,\Big(\tfrac{1}{n}\sum\_{i=1}^{n}\big(1+\|a\_{i}\|^{2s}\big)\,e^{\,Ts(2s-1)\,\|a\_{i}\|^{2}}\Big)^{\!1/s}. |  |

Therefore a sufficient sub-Gaussian condition ensuring J1=Op​(1)J\_{1}=O\_{p}(1) is

|  |  |  |
| --- | --- | --- |
|  | γ02‖σ−1‖F2>2​T​s​(2​s−1).\frac{\gamma\_{0}^{2}}{\|\sigma^{-1}\|\_{F}^{2}}>2\,T\,s(2s-1). |  |

Similarly,

|  |  |  |
| --- | --- | --- |
|  | J1(h)=∫‖y‖2​(mℙn(h)​(y))p​L2¯​(y)​φT​(y)​𝑑y≤(∫mℙn(h)​(y)​φT​(y)​𝑑y)p​(∫‖y‖2​s​L2¯​(y)s​φT​(y)​𝑑y)1/s.J\_{1}^{(h)}=\int\|y\|^{2}\,(m\_{\mathbb{P}\_{n}}^{(h)}(y))^{p}\,\overline{L^{2}}(y)\,\varphi\_{T}(y)\,dy\ \leq\ \Big(\int m\_{\mathbb{P}\_{n}}^{(h)}(y)\,\varphi\_{T}(y)\,dy\Big)^{\!p}\Big(\int\|y\|^{2s}\,\overline{L^{2}}(y)^{\,s}\,\varphi\_{T}(y)\,dy\Big)^{\!1/s}. |  |

Since ∫LT​(b,y)​φT​(y)​𝑑y=1\int L\_{T}(b,y)\varphi\_{T}(y)dy=1 for every bb, we have

|  |  |  |
| --- | --- | --- |
|  | ∫mℙn(h)​(y)​φT​(y)​𝑑y=1n​∑j=1n∫LT​(B(j)+hj,y)​φT​(y)​𝑑y=1,\int m\_{\mathbb{P}\_{n}}^{(h)}(y)\,\varphi\_{T}(y)\,dy=\frac{1}{n}\sum\_{j=1}^{n}\int L\_{T}(B^{(j)}+h\_{j},y)\varphi\_{T}(y)\,dy=1, |  |

so with the same sub Gaussian assumption J1(h)=Op​(1)J\_{1}^{(h)}=O\_{p}(1). when p∈(0,1)p\in(0,1),

|  |  |  |
| --- | --- | --- |
|  | I1=Op​(‖Δ‖n2n).I\_{1}=O\_{p}\left(\frac{\left\|\Delta\right\|^{2}\_{n}}{n}\right). |  |

When p≥1p\geq 1, then Jensen inequality gives mℙn​(y)p≤𝔼ℙn​[LT​(B,y)p]m\_{\mathbb{P}\_{n}}(y)^{p}\leq\mathbb{E}\_{\mathbb{P}\_{n}}[L\_{T}(B,y)^{p}]. Thus

|  |  |  |
| --- | --- | --- |
|  | J1≤1n​∑i=1n𝔼ℙn​[∫‖y‖2​LT​(B,y)p​LT​(B(i),y)2​φT​(y)​𝑑y].J\_{1}\ \leq\ \frac{1}{n}\sum\_{i=1}^{n}\mathbb{E}\_{\mathbb{P}\_{n}}\!\left[\int\|y\|^{2}\,L\_{T}(B,y)^{p}\,L\_{T}(B^{(i)},y)^{2}\,\varphi\_{T}(y)\,dy\right]. |  |

For fixed (B,B(i))(B,B^{(i)}), write λ:=p​a​(B)+2​ai\lambda:=p\,a(B)+2\,a\_{i}.
Completing the square (as in the J1J\_{1} computation) yields

|  |  |  |
| --- | --- | --- |
|  | ∫‖y‖2​LT​(B,y)p​LT​(B(i),y)2​φT​(y)​𝑑y=(T​d+T2​‖λ‖2)​exp⁡{T2​‖λ‖2−T2​p​‖a​(B)‖2−T​‖ai‖2}.\int\|y\|^{2}\,L\_{T}(B,y)^{p}L\_{T}(B^{(i)},y)^{2}\varphi\_{T}(y)dy=(Td+T^{2}\|\lambda\|^{2})\,\exp\!\Big\{\tfrac{T}{2}\|\lambda\|^{2}-\tfrac{T}{2}p\|a(B)\|^{2}-T\|a\_{i}\|^{2}\Big\}. |  |

Using ‖λ‖2≤2​p2​‖a​(B)‖2+8​‖ai‖2\|\lambda\|^{2}\leq 2p^{2}\|a(B)\|^{2}+8\|a\_{i}\|^{2},

|  |  |  |
| --- | --- | --- |
|  | T2​‖λ‖2−T2​p​‖a​(B)‖2−T​‖ai‖2≤T2​(2​p2−p)​‖a​(B)‖2+ 3​T​‖ai‖2.\frac{T}{2}\|\lambda\|^{2}-\tfrac{T}{2}p\|a(B)\|^{2}-T\|a\_{i}\|^{2}\ \leq\ \tfrac{T}{2}\,(2p^{2}-p)\,\|a(B)\|^{2}\ +\ 3T\,\|a\_{i}\|^{2}. |  |

Taking expectation in BB,

|  |  |  |
| --- | --- | --- |
|  | J1≤C​1n​∑i=1n(1+‖ai‖2)​e3​T​‖ai‖2​𝔼ℙn​[eT2​(2​p2−p)​‖a​(B)‖2].J\_{1}\ \leq\ C\,\frac{1}{n}\sum\_{i=1}^{n}\big(1+\|a\_{i}\|^{2}\big)\,e^{3T\|a\_{i}\|^{2}}\;\mathbb{E}\_{\mathbb{P}\_{n}}\!\left[e^{\frac{T}{2}(2p^{2}-p)\,\|a(B)\|^{2}}\right]. |  |

Hence a sufficient sub-Gaussian condition (thus J1=Op​(1)J\_{1}=O\_{p}(1)) is

|  |  |  |
| --- | --- | --- |
|  | γ02‖σ−1‖F2>T​max⁡{(2​p2−p),6}.\frac{\gamma\_{0}^{2}}{\|\sigma^{-1}\|\_{F}^{2}}>T\max\left\{\,(2p^{2}-p),6\right\}. |  |

A similar computation gives

|  |  |  |
| --- | --- | --- |
|  | J1(h)≤C​eC​p​Hn2​(1n​∑i=1n(1+‖ai‖2)​e3​T​‖ai‖2)​(1n​∑j=1ne[T​(2​p2−p)+ε]​‖aj‖2),\quad J\_{1}^{(h)}\ \leq\ C\,e^{Cp\,H\_{n}^{2}}\,\Big(\frac{1}{n}\sum\_{i=1}^{n}(1+\|a\_{i}\|^{2})\,e^{3T\|a\_{i}\|^{2}}\Big)\,\Big(\frac{1}{n}\sum\_{j=1}^{n}e^{\,[\,T(2p^{2}-p)+\varepsilon\,]\|a\_{j}\|^{2}}\Big),\quad |  |

where the bound is finite under
the same sub Gaussian assumption

|  |  |  |
| --- | --- | --- |
|  | γ02‖σ−1‖F2>max⁡{6​T,T​(2​p2−p)}.\ \frac{\gamma\_{0}^{2}}{\|\sigma^{-1}\|\_{F}^{2}}\ >\ \max\!\big\{6T,\;T(2p^{2}-p)\big\}. |  |

Therefore, when p≥1p\geq 1,

|  |  |  |
| --- | --- | --- |
|  | I1=Op​(‖Δ‖n2n​exp⁡(C​max1≤i≤n⁡‖Δ‖2n)).I\_{1}=O\_{p}\left(\frac{\left\|\Delta\right\|^{2}\_{n}}{n}\exp\left(C\max\_{1\leq i\leq n}\frac{\left\|\Delta\right\|^{2}}{n}\right)\right). |  |

Next, we focus on the bound of I2I\_{2} and begin with a bound for A2​(y)2A\_{2}(y)^{2}.
To begin with, direct computations show that there exists a constant CF=CF​(d,T,‖σ−1‖F)>0C\_{F}=C\_{F}(d,T,\|\sigma^{-1}\|\_{F})>0 such that

|  |  |  |
| --- | --- | --- |
|  | ‖∇b2LT​(b,y)‖F≤CF​LT​(b,y)​(1+‖y‖22+T2​‖a​(b)‖22).\big\|\nabla\_{b}^{2}L\_{T}(b,y)\big\|\_{F}\;\leq\;C\_{F}\,L\_{T}(b,y)\,\Big(1+\|y\|\_{2}^{2}+T^{2}\|a(b)\|\_{2}^{2}\Big). |  |

Recall that ci:=σ−1​hic\_{i}:=\sigma^{-1}h\_{i} and fix any ηy>0\eta\_{y}>0, ηa>0\eta\_{a}>0. Then

|  |  |  |
| --- | --- | --- |
|  | LT​(B(i)+t​hi,y)=LT​(B(i),y)​exp⁡{t​⟨ci,y⟩−T​t​⟨ai,ci⟩−T2​t2​‖ci‖22}.L\_{T}(B^{(i)}+th\_{i},y)=L\_{T}(B^{(i)},y)\,\exp\!\Big\{t\langle c\_{i},y\rangle-Tt\langle a\_{i},c\_{i}\rangle-\tfrac{T}{2}t^{2}\|c\_{i}\|\_{2}^{2}\Big\}. |  |

By the Young inequalities,

|  |  |  |
| --- | --- | --- |
|  | t​⟨ci,y⟩≤‖y‖224​ηy+ηy​t2​‖ci‖22,−T​t​⟨ai,ci⟩≤T2​t24​ηa​‖ai‖22+ηa​‖ci‖22.t\langle c\_{i},y\rangle\leq\frac{\|y\|\_{2}^{2}}{4\eta\_{y}}+\eta\_{y}t^{2}\|c\_{i}\|\_{2}^{2},\qquad-\,Tt\langle a\_{i},c\_{i}\rangle\leq\frac{T^{2}t^{2}}{4\eta\_{a}}\|a\_{i}\|\_{2}^{2}+\eta\_{a}\|c\_{i}\|\_{2}^{2}. |  |

Since t∈[0,1]t\in[0,1], the t2t^{2}’s are ≤1\leq 1, and the negative −T2​t2​‖ci‖2-\tfrac{T}{2}t^{2}\|c\_{i}\|^{2} can be dropped. Thus,
for a constant C=C​(T,ηy,ηa)C=C(T,\eta\_{y},\eta\_{a}),

|  |  |  |
| --- | --- | --- |
|  | LT​(B(i)+t​hi,y)≤exp⁡{‖y‖224​ηy}​exp⁡{C​‖ci‖22}​exp⁡{T24​ηa​‖ai‖22}​LT​(B(i),y).L\_{T}(B^{(i)}+th\_{i},y)\ \leq\ \exp\!\Big\{\tfrac{\|y\|\_{2}^{2}}{4\eta\_{y}}\Big\}\,\exp\!\Big\{C\,\|c\_{i}\|\_{2}^{2}\Big\}\,\exp\!\Big\{\tfrac{T^{2}}{4\eta\_{a}}\,\|a\_{i}\|\_{2}^{2}\Big\}\,L\_{T}(B^{(i)},y). |  |

Also ‖a​(B(i)+t​hi)‖2≤‖ai‖2+‖ci‖2\|a(B^{(i)}+th\_{i})\|\_{2}\leq\|a\_{i}\|\_{2}+\|c\_{i}\|\_{2}, hence

|  |  |  |
| --- | --- | --- |
|  | ‖a​(B(i)+t​hi)‖22≤2​‖ai‖22+2​‖ci‖22.\|a(B^{(i)}+th\_{i})\|\_{2}^{2}\leq 2\|a\_{i}\|\_{2}^{2}+2\|c\_{i}\|\_{2}^{2}. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | |A2​(y)|=1n​∑i=1n∫01(1−t)​|hi⊤​∇b2LT​(B(i)+t​hi,y)​hi|​𝑑t≤1n​∑i=1n‖hi‖22​∫01‖∇b2LT​(B(i)+t​hi,y)‖F​𝑑t.|A\_{2}(y)|=\frac{1}{n}\sum\_{i=1}^{n}\int\_{0}^{1}(1-t)\,\big|h\_{i}^{\top}\nabla\_{b}^{2}L\_{T}(B^{(i)}+th\_{i},y)\,h\_{i}\big|\,dt\leq\frac{1}{n}\sum\_{i=1}^{n}\|h\_{i}\|\_{2}^{2}\int\_{0}^{1}\big\|\nabla\_{b}^{2}L\_{T}(B^{(i)}+th\_{i},y)\big\|\_{F}\,dt. |  |

Recall that Hn:=maxi⁡‖ci‖2H\_{n}:=\max\_{i}\|c\_{i}\|\_{2} and
L¯​(y):=1n​∑iLT​(B(i),y)\overline{L}(y):=\tfrac{1}{n}\sum\_{i}L\_{T}(B^{(i)},y), A2​L¯​(y):=1n​∑i‖ai‖22​LT​(B(i),y)\overline{A^{2}L}(y):=\tfrac{1}{n}\sum\_{i}\|a\_{i}\|\_{2}^{2}L\_{T}(B^{(i)},y), then

|  |  |  |
| --- | --- | --- |
|  | |A2​(y)|≤C​(1n​∑i=1n‖ci‖22)⏟≤Hn2​‖σ‖F2​exp⁡{‖y‖224​ηy}​eC​Hn2​[(1+‖y‖22+T2​Hn2)​L¯​(y)+T2​A2​L¯​(y)],|A\_{2}(y)|\ \leq\ C\,\underbrace{\Big(\tfrac{1}{n}\sum\_{i=1}^{n}\|c\_{i}\|\_{2}^{2}\Big)}\_{\leq\,H\_{n}^{2}}\,\|\sigma\|\_{F}^{2}\;\exp\!\Big\{\tfrac{\|y\|\_{2}^{2}}{4\eta\_{y}}\Big\}\,e^{CH\_{n}^{2}}\,\Big[\,(1+\|y\|\_{2}^{2}+T^{2}H\_{n}^{2})\,\overline{L}(y)\ +\ T^{2}\,\overline{A^{2}L}(y)\Big], |  |

where C=C​(d,T,‖σ−1‖F,ηy,ηa)C=C(d,T,\|\sigma^{-1}\|\_{F},\eta\_{y},\eta\_{a}). By Cauchy–Schwarz inequality,

|  |  |  |
| --- | --- | --- |
|  | L¯​(y)≤L2¯​(y)1/2,A2​L¯​(y)≤A2​L2¯​(y)1/2​A2¯1/2.\overline{L}(y)\leq\overline{L^{2}}(y)^{1/2},\qquad\overline{A^{2}L}(y)\leq\overline{A^{2}L^{2}}(y)^{1/2}\overline{A^{2}}^{1/2}. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | A2​(y)2≤C​‖σ‖F4​Hn4​exp⁡{‖y‖222​ηy}​eC​Hn2​[(1+‖y‖22+T2​Hn2)2​L2¯​(y)+T4​A2​L2¯​(y)​A2¯].A\_{2}(y)^{2}\ \leq\ C\,\|\sigma\|\_{F}^{4}\,H\_{n}^{4}\ \exp\!\Big\{\tfrac{\|y\|\_{2}^{2}}{2\eta\_{y}}\Big\}\,e^{CH\_{n}^{2}}\,\Big[\,(1+\|y\|\_{2}^{2}+T^{2}H\_{n}^{2})^{2}\,\overline{L^{2}}(y)\ +\ T^{4}\,\overline{A^{2}L^{2}}(y)\overline{A^{2}}\,\Big]. |  |

Similarly as in the bound for I1I\_{1}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | I2\displaystyle I\_{2} | =2​∫01(1−t)​∫|g′′​(xt)|​A2​(y)2​φT​(y)​𝑑y​𝑑t\displaystyle=2\!\int\_{0}^{1}\!(1-t)\int|g^{\prime\prime}(x\_{t})|\,A\_{2}(y)^{2}\,\varphi\_{T}(y)\,dy\,dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​‖σ‖F4​Hn4​eC​Hn2​(J~1+J~2+J~1(h)+J~2(h)),\displaystyle\leq C\,\|\sigma\|\_{F}^{4}\,H\_{n}^{4}\,e^{CH\_{n}^{2}}\Big(\widetilde{J}\_{1}+\widetilde{J}\_{2}+\widetilde{J}\_{1}^{(h)}+\widetilde{J}\_{2}^{(h)}\Big), |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | J~1\displaystyle\widetilde{J}\_{1} | :=∫(1+‖y‖22+T2​Hn2)2​e‖y‖22/(2​ηy)​mℙn​(y)β−1​L2¯​(y)​φT​(y)​𝑑y,\displaystyle:=\int(1+\|y\|\_{2}^{2}+T^{2}H\_{n}^{2})^{2}\,e^{\|y\|\_{2}^{2}/(2\eta\_{y})}\,m\_{\mathbb{P}\_{n}}(y)^{\beta-1}\,\overline{L^{2}}(y)\,\varphi\_{T}(y)\,dy, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | J~2\displaystyle\widetilde{J}\_{2} | :=T4​∫e‖y‖22/(2​ηy)​mℙn​(y)β−1​A2​L2¯​(y)​A2¯​φT​(y)​𝑑y,\displaystyle:=T^{4}\int e^{\|y\|\_{2}^{2}/(2\eta\_{y})}\,m\_{\mathbb{P}\_{n}}(y)^{\beta-1}\,\overline{A^{2}L^{2}}(y)\,\overline{A^{2}}\,\varphi\_{T}(y)\,dy, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | J~1(h)\displaystyle\widetilde{J}\_{1}^{(h)} | :=∫(1+‖y‖22+T2​Hn2)2​e‖y‖22/(2​ηy)​(mℙn(h)​(y))β−1​L2¯​(y)​φT​(y)​𝑑y,\displaystyle:=\int(1+\|y\|\_{2}^{2}+T^{2}H\_{n}^{2})^{2}\,e^{\|y\|\_{2}^{2}/(2\eta\_{y})}\,\big(m\_{\mathbb{P}\_{n}}^{(h)}(y)\big)^{\beta-1}\,\overline{L^{2}}(y)\,\varphi\_{T}(y)\,dy, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | J~2(h)\displaystyle\widetilde{J}\_{2}^{(h)} | :=T4​∫e‖y‖22/(2​ηy)​(mℙn(h)​(y))β−1​A2​L2¯​(y)​A2¯​φT​(y)​𝑑y.\displaystyle:=T^{4}\int e^{\|y\|\_{2}^{2}/(2\eta\_{y})}\,\big(m\_{\mathbb{P}\_{n}}^{(h)}(y)\big)^{\beta-1}\,\overline{A^{2}L^{2}}(y)\,\overline{A^{2}}\,\varphi\_{T}(y)\,dy. |  |

Each J~\widetilde{J}-term is handled exactly as its I1I\_{1} analogue (J1,J2,J1(h),J2(h)J\_{1},J\_{2},J\_{1}^{(h)},J\_{2}^{(h)}).
When 0<p<10<p<1, use Hölder inequality with s=11−p>1s=\frac{1}{1-p}>1; the Gaussian factor e‖y‖2/(2​ηy)e^{\|y\|^{2}/(2\eta\_{y})} only changes the yy-moment (choose ηy>T\eta\_{y}>T so the Gaussian integrals remain finite). One obtains J~1,J~2=Op​(1)\widetilde{J}\_{1},\widetilde{J}\_{2}=O\_{p}(1) and J~1(h),J~2(h)=Op​(1)\widetilde{J}\_{1}^{(h)},\widetilde{J}\_{2}^{(h)}=O\_{p}(1) under

|  |  |  |
| --- | --- | --- |
|  | γ02‖σ−1‖F2> 2​T​s​(2​s−1),s=11−p.\frac{\gamma\_{0}^{2}}{\|\sigma^{-1}\|\_{F}^{2}}\;>\;2T\,s(2s-1),\qquad s=\frac{1}{1-p}. |  |

The HnH\_{n}-dependence inside (1+‖y‖2+T2​Hn2)2​s(1+\|y\|^{2}+T^{2}H\_{n}^{2})^{2s} contributes only a polynomial prefactor (1+T4​Hn4)\big(1+T^{4}H\_{n}^{4}\big), which is harmless relative to the A2A\_{2} prefactor outside the J~\widetilde{J}’s. And this is the case for the rest cases.

When p<0p<0, then by Jensen inequality (the same use),
choosing ηy>T\eta\_{y}>T, and completing the square in the yy–integrals (with e‖y‖2/(2​ηy)e^{\|y\|^{2}/(2\eta\_{y})}) gives that under

|  |  |  |
| --- | --- | --- |
|  | γ02‖σ−1‖F2>6​T\frac{\gamma\_{0}^{2}}{\|\sigma^{-1}\|\_{F}^{2}}>6T\, |  |

we have

|  |  |  |
| --- | --- | --- |
|  | J~1,J~2=Op​(1),J~1(h),J~2(h)=Op​(eC​Hn2).\widetilde{J}\_{1},\widetilde{J}\_{2}=O\_{p}(1),\qquad\widetilde{J}\_{1}^{(h)},\widetilde{J}\_{2}^{(h)}=O\_{p}(e^{CH\_{n}^{2}}). |  |

When p≥1p\geq 1, use Jensen inequality on mℙnpm\_{\mathbb{P}\_{n}}^{p} (and on (mℙn(h))p(m\_{\mathbb{P}\_{n}}^{(h)})^{p}), then complete the square in yy, as in I1I\_{1}, this yields the condition

|  |  |  |
| --- | --- | --- |
|  | γ02‖σ−1‖F2>max⁡{ 6​T,T​(2​p2−p)}.\frac{\gamma\_{0}^{2}}{\|\sigma^{-1}\|\_{F}^{2}}\;>\;\max\{\,6T,\ T(2p^{2}-p)\,\}. |  |

Under these (same) thresholds, all four J~\widetilde{J}-terms are Op​(1)O\_{p}(1).

Therefore,

|  |  |  |
| --- | --- | --- |
|  | I2=Op​(‖σ‖F4​Hn4​eC​Hn2),Hn2=1n​max1≤i≤n⁡‖σ−1​Δi‖22.\quad I\_{2}\ =\ O\_{p}\!\big(\|\sigma\|\_{F}^{4}\,H\_{n}^{4}\,e^{CH\_{n}^{2}}\big),\qquad H\_{n}^{2}=\frac{1}{n}\max\_{1\leq i\leq n}\big\|\sigma^{-1}\Delta\_{i}\big\|\_{2}^{2}.\quad |  |

Equivalently, absorbing ‖σ‖F,‖σ−1‖F\|\sigma\|\_{F},\|\sigma^{-1}\|\_{F} into CC,

|  |  |  |
| --- | --- | --- |
|  | I2=Op​(‖Δ‖n2n⋅max1≤i≤n⁡‖Δi‖2n​exp⁡(C​max1≤i≤n⁡‖Δi‖2n)).I\_{2}\ =O\_{p}\!\left(\frac{\|\Delta\|\_{n}^{2}}{n}\cdot\frac{\max\_{1\leq i\leq n}\|\Delta\_{i}\|^{2}}{n}\;\exp\!\Big(C\,\max\_{1\leq i\leq n}\frac{\|\Delta\_{i}\|^{2}}{n}\Big)\right). |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | |R2|=Op​(‖Δ‖n2n​exp⁡(C​max1≤i≤n⁡‖Δi‖2n))+Op​(‖Δ‖n2n⋅max1≤i≤n⁡‖Δi‖2n​exp⁡(C​max1≤i≤n⁡‖Δi‖2n)).|R\_{2}|=O\_{p}\left(\frac{\left\|\Delta\right\|\_{n}^{2}}{n}\exp\left(C\max\_{1\ \leq i\leq n}\frac{\left\|\Delta\_{i}\right\|^{2}}{n}\right)\right)+O\_{p}\!\left(\frac{\|\Delta\|\_{n}^{2}}{n}\cdot\frac{\max\_{1\leq i\leq n}\|\Delta\_{i}\|^{2}}{n}\;\exp\!\Big(C\,\max\_{1\leq i\leq n}\frac{\|\Delta\_{i}\|^{2}}{n}\Big)\right). |  |

∎

By Lemmas [3](https://arxiv.org/html/2512.01408v1#Thmlemma3 "Lemma 3. ‣ D.2.1 Part II-i ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and [4](https://arxiv.org/html/2512.01408v1#Thmlemma4 "Lemma 4. ‣ D.2.1 Part II-i ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), we have the bounds for the remainder terms with a constant C,C∗>0C,C^{\*}>0:

|  |  |  |
| --- | --- | --- |
|  | |R1|+|R2|\displaystyle|R\_{1}|+|R\_{2}| |  |
|  |  |  |
| --- | --- | --- |
|  | =Op​(1n​(1n​∑i=1n‖Δi‖4)1/2​[1+‖Δ‖nn+1n​(1n​∑i=1n‖Δi‖4)1/2]​exp⁡(C′​max1≤i≤n⁡‖Δi‖2n))\displaystyle=O\_{p}\!\left(\frac{1}{n}\Big(\frac{1}{n}\sum\_{i=1}^{n}\|\Delta\_{i}\|^{4}\Big)^{\!1/2}\,\Big[1+\frac{\|\Delta\|\_{n}}{\sqrt{n}}+\frac{1}{n}\Big(\frac{1}{n}\sum\_{i=1}^{n}\|\Delta\_{i}\|^{4}\Big)^{\!1/2}\Big]\,\exp\!\Big(C^{\prime}\,\max\_{1\leq i\leq n}\frac{\|\Delta\_{i}\|^{2}}{n}\Big)\right) |  |
|  |  |  |
| --- | --- | --- |
|  | +Op​(‖Δ‖n2n​exp⁡(C​max1≤i≤n⁡‖Δi‖2n))+Op​(‖Δ‖n2n⋅max1≤i≤n⁡‖Δi‖2n​exp⁡(C​max1≤i≤n⁡‖Δi‖2n)).\displaystyle+O\_{p}\left(\frac{\left\|\Delta\right\|\_{n}^{2}}{n}\exp\left(C\max\_{1\ \leq i\leq n}\frac{\left\|\Delta\_{i}\right\|^{2}}{n}\right)\right)+O\_{p}\!\left(\frac{\|\Delta\|\_{n}^{2}}{n}\cdot\frac{\max\_{1\leq i\leq n}\|\Delta\_{i}\|^{2}}{n}\;\exp\!\Big(C\,\max\_{1\leq i\leq n}\frac{\|\Delta\_{i}\|^{2}}{n}\Big)\right). |  |

#### D.2.2 Part II-ii

We propose the following sub-Gaussian assumption.

###### Assumption 8.

Suppose there exists γ0>0\gamma\_{0}>0 such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ∗​[exp⁡(γ2​‖B‖22)]<∞for every ​γ<γ0.\mathbb{E}\_{\mathbb{P}^{\*}}\big[\exp(\gamma^{2}\|B\|\_{2}^{2})\big]<\infty\quad\text{for every }\gamma<\gamma\_{0}. |  |

with

|  |  |  |
| --- | --- | --- |
|  | γ02>8​T​‖σ−1‖F2​max⁡{ 1+β, 2}.\gamma\_{0}^{2}\;>8\,T\,\|\sigma^{-1}\|\_{F}^{2}\,\max\{\,1+\beta,\,2\,\}. |  |

and β=α1−α\beta=\frac{\alpha}{1-\alpha}.

###### Lemma 5.

Let

|  |  |  |
| --- | --- | --- |
|  | Ci​(n):=κα​∫ℝdmℙn​(y)β​∇bLT​(B(i),y)​φT​(y)​𝑑y,β=α1−α,mℙn​(y)=1n​∑j=1nLT​(B(j),y).C\_{i}(n):=\kappa\_{\alpha}\int\_{\mathbb{R}^{d}}m\_{\mathbb{P}\_{n}}(y)^{\beta}\,\nabla\_{b}L\_{T}(B^{(i)},y)\,\varphi\_{T}(y)\,dy,\qquad\beta=\tfrac{\alpha}{1-\alpha},\quad m\_{\mathbb{P}\_{n}}(y)=\tfrac{1}{n}\sum\_{j=1}^{n}L\_{T}(B^{(j)},y). |  |

Under Assumption [8](https://arxiv.org/html/2512.01408v1#Thmassumption8 "Assumption 8. ‣ D.2.2 Part II-ii ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), there exists K4<∞K\_{4}<\infty, independent of nn, such that

|  |  |  |
| --- | --- | --- |
|  | supn≥1𝔼​[‖C1​(n)‖4]≤K4.\sup\_{n\geq 1}\ \mathbb{E}\big[\|C\_{1}(n)\|^{4}\big]\ \leq\ K\_{4}. |  |

###### Lemma 6.

Under Assumption [8](https://arxiv.org/html/2512.01408v1#Thmassumption8 "Assumption 8. ‣ D.2.2 Part II-ii ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), in the context of Proof of Theorem [6](https://arxiv.org/html/2512.01408v1#Thmtheorem6 "Theorem 6. ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), for directions Δi=λ​Ci​(n)\Delta\_{i}=\lambda\,C\_{i}(n) with fixed |λ|=O​(1)|\lambda|=O(1),
we have

|  |  |  |
| --- | --- | --- |
|  | |R1|+|R2|=Op​(‖Δ‖n2n),‖Δ‖n2=1n​∑i=1n‖Δi‖2.|R\_{1}|+|R\_{2}|\;=\;O\_{p}\!\Big(\frac{\|\Delta\|\_{n}^{2}}{n}\Big),\qquad\|\Delta\|\_{n}^{2}=\frac{1}{n}\sum\_{i=1}^{n}\|\Delta\_{i}\|^{2}. |  |

###### Proof.

With Δi=λ​Ci​(n)\Delta\_{i}=\lambda C\_{i}(n) and fixed |λ|=O​(1)|\lambda|=O(1), Lemma [5](https://arxiv.org/html/2512.01408v1#Thmlemma5 "Lemma 5. ‣ D.2.2 Part II-ii ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") implies

|  |  |  |
| --- | --- | --- |
|  | 1n​∑i=1n‖Δi‖4=λ4​1n​∑i=1n‖Ci​(n)‖4=Op​(1),‖Δ‖n2=1n​∑i=1n‖Δi‖2=Θp​(1).\frac{1}{n}\sum\_{i=1}^{n}\|\Delta\_{i}\|^{4}=\lambda^{4}\,\frac{1}{n}\sum\_{i=1}^{n}\|C\_{i}(n)\|^{4}=O\_{p}(1),\qquad\|\Delta\|\_{n}^{2}=\frac{1}{n}\sum\_{i=1}^{n}\|\Delta\_{i}\|^{2}\;=\;\Theta\_{p}(1). |  |

Moreover, by Markov inequality and a union bound,

|  |  |  |
| --- | --- | --- |
|  | Pr⁡(max1≤i≤n⁡‖Δi‖>t)≤n​𝔼​‖Δ1‖4t4⟹max1≤i≤n⁡‖Δi‖2n=Op​(n−1/2)=op​(1),\Pr\!\Big(\max\_{1\leq i\leq n}\|\Delta\_{i}\|>t\Big)\leq\frac{n\,\mathbb{E}\|\Delta\_{1}\|^{4}}{t^{4}}\quad\Longrightarrow\quad\max\_{1\leq i\leq n}\frac{\|\Delta\_{i}\|^{2}}{n}=O\_{p}(n^{-1/2})=o\_{p}(1), |  |

so exp⁡(C∗​maxi⁡‖Δi‖2/n)=1+op​(1)\exp\!\big(C\_{\ast}\max\_{i}\|\Delta\_{i}\|^{2}/n\big)=1+o\_{p}(1) for any fixed C∗>0C\_{\ast}>0.

Insert these in the general bound:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |R1|\displaystyle|R\_{1}| | =Op​(1n​(1n​∑‖Δi‖4)1/2​[1+‖Δ‖nn+1n​(1n​∑‖Δi‖4)1/2]​eC′​maxi⁡‖Δi‖2/n)\displaystyle=O\_{p}\!\left(\frac{1}{n}\Big(\tfrac{1}{n}\sum\|\Delta\_{i}\|^{4}\Big)^{1/2}\Big[1+\tfrac{\|\Delta\|\_{n}}{\sqrt{n}}+\tfrac{1}{n}\Big(\tfrac{1}{n}\sum\|\Delta\_{i}\|^{4}\Big)^{1/2}\Big]\,e^{\,C^{\prime}\max\_{i}\|\Delta\_{i}\|^{2}/n}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Op​(1n)=Op​(‖Δ‖n2n),\displaystyle=O\_{p}\!\left(\frac{1}{n}\right)=O\_{p}\!\left(\frac{\|\Delta\|\_{n}^{2}}{n}\right), |  |

since the bracket is 1+op​(1)1+o\_{p}(1) and ‖Δ‖n2=Θp​(1)\|\Delta\|\_{n}^{2}=\Theta\_{p}(1). For R2R\_{2},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |R2|\displaystyle|R\_{2}| | =Op​(‖Δ‖n2n​eC​maxi⁡‖Δi‖2/n)+Op​(‖Δ‖n2n⋅maxi⁡‖Δi‖2n​eC​maxi⁡‖Δi‖2/n)\displaystyle=O\_{p}\!\left(\frac{\|\Delta\|\_{n}^{2}}{n}\,e^{\,C\max\_{i}\|\Delta\_{i}\|^{2}/n}\right)+O\_{p}\!\left(\frac{\|\Delta\|\_{n}^{2}}{n}\cdot\frac{\max\_{i}\|\Delta\_{i}\|^{2}}{n}\,e^{\,C\max\_{i}\|\Delta\_{i}\|^{2}/n}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Op​(‖Δ‖n2n)+op​(‖Δ‖n2n),\displaystyle=O\_{p}\!\left(\frac{\|\Delta\|\_{n}^{2}}{n}\right)+o\_{p}\!\left(\frac{\|\Delta\|\_{n}^{2}}{n}\right), |  |

again because maxi⁡‖Δi‖2/n=op​(1)\max\_{i}\|\Delta\_{i}\|^{2}/n=o\_{p}(1). Summing,

|  |  |  |
| --- | --- | --- |
|  | |R1|+|R2|=Op​(‖Δ‖n2n).|R\_{1}|+|R\_{2}|\;=\;O\_{p}\!\Big(\tfrac{\|\Delta\|\_{n}^{2}}{n}\Big). |  |

∎

### D.3 Part III

By Lemma [6](https://arxiv.org/html/2512.01408v1#Thmlemma6 "Lemma 6. ‣ D.2.2 Part II-ii ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), if we consider the minimum-norm direction (defined below), then the remainder bounds |R1|+|R2||R\_{1}|+|R\_{2}| becomes

|  |  |  |
| --- | --- | --- |
|  | |R​(Δ)|:=|R1|+|R2|=Op​(‖Δ‖n2n).|R(\Delta)|:=|R\_{1}|+|R\_{2}|=O\_{p}\left(\frac{\left\|\Delta\right\|\_{n}^{2}}{n}\right). |  |

Therefore, we have

|  |  |  |
| --- | --- | --- |
|  | F​(Δ):=J​(ℙnΔ)−J​(ℙ∗)=F​(0)+D​F​(0)​[Δ]+R​(Δ),F(\Delta):=J(\mathbb{P}\_{n}^{\Delta})-J(\mathbb{P}^{\*})=F(0)+DF(0)[\Delta]+R(\Delta), |  |

where D​F​(0)​[Δ]=1n1/2​1n​∑i=1nCi​(n)⋅ΔiDF(0)[\Delta]=\frac{1}{n^{1/2}}\frac{1}{n}\sum\_{i=1}^{n}C\_{i}(n)\cdot\Delta\_{i}, F​(0)=J​(ℙn)−J​(ℙ∗)F(0)=J(\mathbb{P}\_{n})-J(\mathbb{P}^{\*}), and |R​(Δ)|=Op​(‖Δ‖n2n).|R(\Delta)|=O\_{p}\left(\frac{\left\|\Delta\right\|\_{n}^{2}}{n}\right).
To solve F​(Δ)=0F(\Delta)=0, consider the minimum-norm direction: Δi=λ​Ci​(n)\Delta\_{i}=\lambda C\_{i}(n)
for a scalar λ\lambda to be determined. By substituting,
D​F​(0)​[Δ]=λn1/2⋅1n​∑i=1n‖Ci​(n)‖2.DF(0)[\Delta]=\frac{\lambda}{n^{1/2}}\cdot\frac{1}{n}\sum\_{i=1}^{n}\|C\_{i}(n)\|^{2}.
Plug this and R​(Δ)R(\Delta) into the equation:

|  |  |  |
| --- | --- | --- |
|  | F​(0)+λn1/2⋅1n​∑i=1n‖Ci​(n)‖2+R​(Δ)=0F(0)+\frac{\lambda}{n^{1/2}}\cdot\frac{1}{n}\sum\_{i=1}^{n}\|C\_{i}(n)\|^{2}+R(\Delta)=0 |  |

Solving for λ\lambda (ignoring R​(Δ)R(\Delta) for a moment, which is justified for small ‖Δ‖n\|\Delta\|\_{n}), we have

|  |  |  |
| --- | --- | --- |
|  | λ∗=−n1/2​F​(0)1n​∑i=1n‖Ci​(n)‖2.\lambda^{\*}=-\frac{n^{1/2}F(0)}{\frac{1}{n}\sum\_{i=1}^{n}\|C\_{i}(n)\|^{2}}. |  |

Thus, the correction is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δi∗=−n1/2​F​(0)1n​∑j=1n‖Cj​(n)‖2​Ci​(n).\Delta\_{i}^{\*}=-\frac{n^{1/2}F(0)}{\frac{1}{n}\sum\_{j=1}^{n}\|C\_{j}(n)\|^{2}}C\_{i}(n). |  | (55) |

Compute the squared average norm:

|  |  |  |
| --- | --- | --- |
|  | ‖Δ∗‖n2=1n​∑i=1n‖Δi∗‖2=(λ∗)2⋅1n​∑i=1n‖Ci​(n)‖2.\|\Delta^{\*}\|\_{n}^{2}=\frac{1}{n}\sum\_{i=1}^{n}\|\Delta\_{i}^{\*}\|^{2}=(\lambda^{\*})^{2}\cdot\frac{1}{n}\sum\_{i=1}^{n}\|C\_{i}(n)\|^{2}. |  |

So, using the formula for λ∗\lambda^{\*}:

|  |  |  |
| --- | --- | --- |
|  | ‖Δ∗‖n2=(n1/2​F​(0)1n​∑j=1n‖Cj​(n)‖2)2⋅1n​∑i=1n‖Ci​(n)‖2=n​F​(0)2/(1n​∑j=1n‖Cj​(n)‖2).\|\Delta^{\*}\|\_{n}^{2}=\left(\frac{n^{1/2}F(0)}{\frac{1}{n}\sum\_{j=1}^{n}\|C\_{j}(n)\|^{2}}\right)^{2}\cdot\frac{1}{n}\sum\_{i=1}^{n}\|C\_{i}(n)\|^{2}=nF(0)^{2}/\left(\frac{1}{n}\sum\_{j=1}^{n}\|C\_{j}(n)\|^{2}\right). |  |

### D.4 Part IV

In this part, we will present Lemmas [7](https://arxiv.org/html/2512.01408v1#Thmlemma7 "Lemma 7. ‣ D.4 Part IV ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), [8](https://arxiv.org/html/2512.01408v1#Thmlemma8 "Lemma 8. ‣ D.4 Part IV ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and [9](https://arxiv.org/html/2512.01408v1#Thmlemma9 "Lemma 9. ‣ D.4 Part IV ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") to establish various senses of convergence.

###### Lemma 7.

Define

|  |  |  |
| --- | --- | --- |
|  | C⋆​(b):=κα​∫ℝdmℙ∗​(y)β​∇bLT​(b,y)​φT​(y)​𝑑y,C^{\star}(b):=\kappa\_{\alpha}\int\_{\mathbb{R}^{d}}m\_{\mathbb{P}^{\*}}(y)^{\beta}\,\nabla\_{b}L\_{T}(b,y)\,\varphi\_{T}(y)\,dy, |  |

where κα=11−α​(er​Tk∗)11−α\kappa\_{\alpha}=\frac{1}{1-\alpha}\left(\frac{e^{rT}}{k^{\*}}\right)^{\frac{1}{1-\alpha}}, then under Assumption [8](https://arxiv.org/html/2512.01408v1#Thmassumption8 "Assumption 8. ‣ D.2.2 Part II-ii ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), we have the convergence in probability

|  |  |  |
| --- | --- | --- |
|  | 1n​∑i=1n‖Ci​(n)‖2→𝑝c,c:=𝔼​[‖C⋆​(B)‖2]∈(0,∞).\frac{1}{n}\sum\_{i=1}^{n}\|C\_{i}(n)\|^{2}\;\xrightarrow{p}\;c,\qquad c:=\mathbb{E}\big[\|C^{\star}(B)\|^{2}\big]\in(0,\infty). |  |

###### Proof.

Since mℙn​(y)→mℙ∗​(y)m\_{\mathbb{P}\_{n}}(y)\to m\_{\mathbb{P}^{\*}}(y) a.s. for each yy and the sub-Gaussian condition furnishes an
integrable upper bound for the map
y↦mℙn​(y)β​∇bLT​(B(i),y)​φT​(y)y\mapsto m\_{\mathbb{P}\_{n}}(y)^{\beta}\,\nabla\_{b}L\_{T}(B^{(i)},y)\,\varphi\_{T}(y)
(see the derivation in Lemma [5](https://arxiv.org/html/2512.01408v1#Thmlemma5 "Lemma 5. ‣ D.2.2 Part II-ii ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")),
dominated convergence theorem yields 𝔼​‖C⋆​(B)‖2<∞\mathbb{E}\|C^{\star}(B)\|^{2}<\infty and

|  |  |  |
| --- | --- | --- |
|  | ‖Ci​(n)−C⋆​(B(i))‖→n→∞ 0in ​L2.\|C\_{i}(n)-C^{\star}(B^{(i)})\|\ \xrightarrow[n\to\infty]{}\ 0\quad\text{in }L^{2}\ . |  |

Write

|  |  |  |
| --- | --- | --- |
|  | 1n∑i=1n∥Ci(n)∥2=1n∑i=1n∥C⋆(B(i))∥2+1n∑i=1n(∥Ci(n)∥2−∥C⋆(B(i))∥2)=:An+Rn.\frac{1}{n}\sum\_{i=1}^{n}\|C\_{i}(n)\|^{2}=\frac{1}{n}\sum\_{i=1}^{n}\|C^{\star}(B^{(i)})\|^{2}\;+\;\frac{1}{n}\sum\_{i=1}^{n}\Big(\|C\_{i}(n)\|^{2}-\|C^{\star}(B^{(i)})\|^{2}\Big)=:A\_{n}+R\_{n}. |  |

Then by strong law of large numbers, we have An→cA\_{n}\to c a.s.

For RnR\_{n}, by Cauchy–Schwarz and the uniform fourth-moment bound from
Lemma [5](https://arxiv.org/html/2512.01408v1#Thmlemma5 "Lemma 5. ‣ D.2.2 Part II-ii ‣ D.2 Part II ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"),

|  |  |  |
| --- | --- | --- |
|  | 𝔼​|Rn|≤1n​∑i=1n𝔼​[‖Ci​(n)−C⋆​(B(i))‖​(‖Ci​(n)‖+‖C⋆​(B(i))‖)]≤K​(𝔼​‖C1​(n)−C⋆​(B(1))‖2)1/2,\mathbb{E}|R\_{n}|\;\leq\;\frac{1}{n}\sum\_{i=1}^{n}\mathbb{E}\Big[\|C\_{i}(n)-C^{\star}(B^{(i)})\|\,\big(\|C\_{i}(n)\|+\|C^{\star}(B^{(i)})\|\big)\Big]\;\leq\;K\,\Big(\mathbb{E}\|C\_{1}(n)-C^{\star}(B^{(1)})\|^{2}\Big)^{\!1/2}, |  |

for a constant K<∞K<\infty independent of nn. Since the right-hand side →0\to 0, then
Rn→0R\_{n}\to 0 in L1L^{1} and therefore in probability. Hence the proof is completed.
∎

###### Lemma 8.

As n→∞n\to\infty, J​(ℙn)−J​(ℙ∗)=Op​(n−1/2)J(\mathbb{P}\_{n})-J(\mathbb{P}^{\*})=O\_{p}(n^{-1/2}), and

|  |  |  |
| --- | --- | --- |
|  | n​(J​(ℙn)−J​(ℙ∗))⇒𝒩​(0,h​(ℙ∗)),\sqrt{n}\left(J(\mathbb{P}\_{n})-J(\mathbb{P}^{\*})\right)\Rightarrow\mathcal{N}(0,h(\mathbb{P}^{\*})), |  |

where

|  |  |  |
| --- | --- | --- |
|  | h​(ℙ∗)=∫∫g′​(α​(y1))​g′​(α​(y2))​Covℙ∗​(LT​(B,y1),LT​(B,y2))​φT​(y1)​φT​(y2)​𝑑y1​𝑑y2<∞.h(\mathbb{P}^{\*})=\int\int g^{\prime}(\alpha(y\_{1}))g^{\prime}(\alpha(y\_{2}))\text{Cov}\_{\mathbb{P}^{\*}}\left(L\_{T}(B,y\_{1}),L\_{T}(B,y\_{2})\right)\varphi\_{T}(y\_{1})\varphi\_{T}(y\_{2})dy\_{1}dy\_{2}<\infty. |  |

###### Proof.

We define a separable Hilbert space H=L2​(φT)H=L^{2}(\varphi\_{T}) with the norm h∈Hh\in H, ‖h‖2=∫ℝdh2​(y)​φT​(y)​𝑑y\left\|h\right\|^{2}=\int\_{\mathbb{R}^{d}}h^{2}(y)\varphi\_{T}(y)dy, and Zi(.)=LT(B,.)Z\_{i}(.)=L\_{T}(B,.) as an element of HH. From a similar computation of the Gaussian bounds above, there exist constants 0<K<∞0<K<\infty and u2:=2​T​‖σ−1‖F2u\_{2}:=2T\,\|\sigma^{-1}\|\_{F}^{2} such that

|  |  |  |
| --- | --- | --- |
|  | ∫ℝdLT​(b,y)2​φT​(y)​dy≤K​exp⁡(u2​‖b‖2)for all ​b∈ℝd,\int\_{\mathbb{R}^{d}}L\_{T}(b,y)^{2}\,\varphi\_{T}(y)\,\mathrm{d}y\;\leq\;K\,\exp\!\big(u\_{2}\,\|b\|^{2}\big)\quad\text{for all }b\in\mathbb{R}^{d}, |  |

and therefore

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ∗[∥LT(B,.)∥2]≤K𝔼ℙ∗exp(u2∥B∥2).\mathbb{E}\_{\mathbb{P}^{\*}}\left[\left\|L\_{T}(B,.)\right\|^{2}\right]\;\leq\;K\,\mathbb{E}\_{\mathbb{P}^{\*}}\exp\!\big(u\_{2}\,\|B\|^{2}\big). |  |

it suffices to assume the sub Gaussian parameter

|  |  |  |
| --- | --- | --- |
|  | γ02> 2​T​‖σ−1‖F2.\gamma\_{0}^{2}\;>\;2T\,\|\sigma^{-1}\|\_{F}^{2}. |  |

to make this norm finite.
Hence, the central limit theorem for Hilbert space valued random elements gives the following: as n→∞n\to\infty,

|  |  |  |
| --- | --- | --- |
|  | n(𝔼ℙn[LT(B,.)]−𝔼ℙ∗[LT(B,.)])⇒G,\sqrt{n}\left(\mathbb{E}\_{\mathbb{P}\_{n}}\left[L\_{T}(B,.)\right]-\mathbb{E}\_{\mathbb{P}^{\*}}\left[L\_{T}(B,.)\right]\right)\Rightarrow G, |  |

where GG is distributed as a Gaussian measure in HH with a covariance operator such that for any h∈Hh\in H with the Bochner integral

|  |  |  |
| --- | --- | --- |
|  | Ch=Covℙ∗(⟨LT(B,.),h⟩H,LT(B,.)).Ch=\mathrm{Cov}\_{\mathbb{P}^{\*}}\big(\langle L\_{T}(B,.),h\rangle\_{H},L\_{T}(B,.)\big). |  |

This limit is enough for the case when β<1\beta<1. When β>1\beta>1, we want to show that G∈L1+β​(φT)G\in L^{1+\beta}(\varphi\_{T}) a.s. under certain sub Gaussian assumption.
Let p:=1+β>2p:=1+\beta>2. Using the similar Gaussian-tilt computation (as above), there exist
constants Kp<∞K\_{p}<\infty and up>0u\_{p}>0 (depending on T,σ,mT,\sigma,m and pp) such that for all bb,

|  |  |  |
| --- | --- | --- |
|  | ∫ℝdLT​(b,y)p​φT​(y)​𝑑y≤Kp​exp⁡(up​‖b‖2).\int\_{\mathbb{R}^{d}}L\_{T}(b,y)^{p}\,\varphi\_{T}(y)\,dy\;\leq\;K\_{p}\,\exp\!\big(u\_{p}\,\|b\|^{2}\big). |  |

A safe explicit choice is

|  |  |  |
| --- | --- | --- |
|  | up=C​p​(1+p)​T​‖σ−1‖F2,e.g.u1+β≤ 2​(1+β)​T​‖σ−1‖F2,u\_{p}\;=\;C\,p(1+p)\,T\,\|\sigma^{-1}\|\_{F}^{2},\qquad\text{e.g.}\quad u\_{1+\beta}\;\leq\;2(1+\beta)\,T\,\|\sigma^{-1}\|\_{F}^{2}, |  |

where the constant CC absorbs the drift terms (cf. the bounds already used earlier).
Assume the sub-Gaussian radius γ0\gamma\_{0} of BB satisfies

|  |  |  |
| --- | --- | --- |
|  | γ02>u1+β⟹𝔼ℙ∗​exp⁡(u1+β​‖B‖2)<∞.\gamma\_{0}^{2}\;>\;u\_{1+\beta}\ \quad\Longrightarrow\quad\mathbb{E}\_{\mathbb{P}^{\*}}\exp\!\big(u\_{1+\beta}\,\|B\|^{2}\big)<\infty. |  |

Then, by Tonelli,

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ∗​∫LT​(B,y)1+β​φT​(y)​𝑑y≤K1+β​𝔼ℙ∗​exp⁡(u1+β​‖B‖2)<∞.\mathbb{E}\_{\mathbb{P}^{\*}}\!\int L\_{T}(B,y)^{1+\beta}\,\varphi\_{T}(y)\,dy\;\leq\;K\_{1+\beta}\,\mathbb{E}\_{\mathbb{P}^{\*}}\exp\!\big(u\_{1+\beta}\,\|B\|^{2}\big)\;<\;\infty. |  |

For X​(y):=LT​(B,y)−μ​(y)X(y):=L\_{T}(B,y)-\mu(y) with μ​(y)=𝔼ℙ∗​[LT​(B,y)]\mu(y)=\mathbb{E}\_{\mathbb{P}^{\*}}[L\_{T}(B,y)], we have

|  |  |  |
| --- | --- | --- |
|  | ‖X‖L1+β​(φT) 2=(∫|X​(y)|1+β​φT​(y)​𝑑y)21+β.\|X\|\_{L^{1+\beta}(\varphi\_{T})}^{\,2}=\Big(\int|X(y)|^{1+\beta}\,\varphi\_{T}(y)\,dy\Big)^{\frac{2}{1+\beta}}. |  |

Since 21+β∈(0,1)\frac{2}{1+\beta}\in(0,1), the map x↦x21+βx\mapsto x^{\frac{2}{1+\beta}} is concave on ℝ+\mathbb{R}\_{+},
hence Jensen yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖X‖L1+β2]≤(𝔼​∫|X​(y)|1+β​φT​(d​y))21+β≤(21+β​𝔼​∫LT​(B,y)1+β​φT​(d​y))21+β<∞,\mathbb{E}\big[\|X\|\_{L^{1+\beta}}^{2}\big]\;\leq\;\Big(\mathbb{E}\int|X(y)|^{1+\beta}\,\varphi\_{T}(dy)\Big)^{\!\frac{2}{1+\beta}}\;\leq\;\Big(2^{1+\beta}\,\mathbb{E}\int L\_{T}(B,y)^{1+\beta}\,\varphi\_{T}(dy)\Big)^{\!\frac{2}{1+\beta}}\;<\;\infty, |  |

thus
𝔼​‖X‖L1+β2<∞\mathbb{E}\|X\|\_{L^{1+\beta}}^{2}<\infty.
The space L1+β​(φT)L^{1+\beta}(\varphi\_{T}) with 1+β>21+\beta>2 is a type-2 Banach space.
Therefore, by the CLT for i.i.d. Banach-valued random variables,
the averages mℙn=1n​∑i=1nLT​(B(i),⋅)m\_{\mathbb{P}\_{n}}=\frac{1}{n}\sum\_{i=1}^{n}L\_{T}(B^{(i)},\cdot) satisfy

|  |  |  |
| --- | --- | --- |
|  | n​(mℙn−mℙ∗)⇒Gin ​L1+β​(φT),\sqrt{n}\,\big(m\_{\mathbb{P}\_{n}}-m\_{\mathbb{P}^{\*}}\big)\ \Rightarrow\ G\quad\text{in }L^{1+\beta}(\varphi\_{T}), |  |

where GG is a centered Gaussian measure on L1+β​(φT)L^{1+\beta}(\varphi\_{T}).
In particular, G∈L1+β​(φT)G\in L^{1+\beta}(\varphi\_{T}) a.s.
Since φT\varphi\_{T} is a probability measure, the continuous embedding
L1+β​(φT)↪L2​(φT)L^{1+\beta}(\varphi\_{T})\hookrightarrow L^{2}(\varphi\_{T}) implies the same CLT in L2L^{2}.

Next, we show h​(ℙ∗)<∞h(\mathbb{P}^{\*})<\infty.
By Cauchy Schwartz inequality, we have |Cov​(X,Y)|≤Var​(X)​Var​(Y)≤𝔼​[X2]​𝔼​[Y2]|\text{Cov}(X,Y)|\leq\sqrt{\text{Var}(X)\text{Var}(Y)}\leq\sqrt{\mathbb{E}[X^{2}]\mathbb{E}[Y^{2}]}, thus

|  |  |  |
| --- | --- | --- |
|  | |h​(ℙ∗)|≤(∫|g′​(α​(y))|​𝔼ℙ∗​[LT​(B,y)2]​φT​(y)​𝑑y)2.|h(\mathbb{P}^{\*})|\;\leq\;\Bigg(\int|g^{\prime}\!\big(\alpha(y)\big)|\,\sqrt{\mathbb{E}\_{\mathbb{P}^{\*}}\!\big[L\_{T}(B,y)^{2}\big]}\;\varphi\_{T}(y)\,dy\Bigg)^{\!2}. |  |

Another application of Cauchy–Schwarz inequality gives

|  |  |  |
| --- | --- | --- |
|  | |h​(ℙ∗)|≤(∫g′​(α​(y))2​φT​(y)​𝑑y)​(∫𝔼ℙ∗​[LT​(B,y)2]​φT​(y)​𝑑y).|h(\mathbb{P}^{\*})|\;\leq\;\Bigg(\int g^{\prime}\!\big(\alpha(y)\big)^{2}\,\varphi\_{T}(y)\,dy\Bigg)\Bigg(\int\mathbb{E}\_{\mathbb{P}^{\*}}\!\big[L\_{T}(B,y)^{2}\big]\;\varphi\_{T}(y)\,dy\Bigg). |  |

Hence it suffices to show that the first integral is finite.

Recall that g′​(α)=κα​αβg^{\prime}(\alpha)=\kappa\_{\alpha}\,\alpha^{\beta} with β=α1−α\beta=\frac{\alpha}{1-\alpha}, then

|  |  |  |
| --- | --- | --- |
|  | ∫g′​(α​(y))2​φT​(y)​𝑑y=κα2​∫α​(y)2​β​φT​(y)​𝑑y.\int g^{\prime}(\alpha(y))^{2}\,\varphi\_{T}(y)\,dy=\kappa\_{\alpha}^{2}\int\alpha(y)^{2\beta}\,\varphi\_{T}(y)\,dy. |  |

For β≥12\beta\geq\tfrac{1}{2}, the Jensen inequality yields α​(y)2​β≤𝔼ℙ∗​[LT​(B,y)2​β]\alpha(y)^{2\beta}\leq\mathbb{E}\_{\mathbb{P}^{\*}}[L\_{T}(B,y)^{2\beta}].
For 0<β<120<\beta<\tfrac{1}{2}, use x2​β≤Cβ​(1+x2​β+x2)x^{2\beta}\leq C\_{\beta}\,(1+x^{2\beta}+x^{2}) for x≥0x\geq 0.
In both cases,

|  |  |  |
| --- | --- | --- |
|  | ∫α​(y)2​β​φT​(y)​𝑑y≤Cβ​(1+𝔼ℙ∗​∫LT​(B,y)2​β​φT​(y)​𝑑y+𝔼ℙ∗​∫LT​(B,y)2​φT​(y)​𝑑y).\int\alpha(y)^{2\beta}\,\varphi\_{T}(y)\,dy\;\leq\;C\_{\beta}\Bigg(1+\mathbb{E}\_{\mathbb{P}^{\*}}\!\int L\_{T}(B,y)^{2\beta}\varphi\_{T}(y)\,dy\;+\;\mathbb{E}\_{\mathbb{P}^{\*}}\!\int L\_{T}(B,y)^{2}\varphi\_{T}(y)\,dy\Bigg). |  |

Again by the Gaussian-tilt bound, for all bb,

|  |  |  |
| --- | --- | --- |
|  | ∫LT​(b,y)2​β​φT​(y)​𝑑y≤K2​β​exp⁡(u2​β​‖b‖2),\int L\_{T}(b,y)^{2\beta}\varphi\_{T}(y)\,dy\;\leq\;K\_{2\beta}\,\exp\!\big(u\_{2\beta}\|b\|^{2}\big), |  |

with K2​β<∞K\_{2\beta}<\infty and u2​β>0u\_{2\beta}>0 depending on T,σ,m,βT,\sigma,m,\beta
(a safe choice is u2​β=2​(1+β)​T​‖σ−1‖F2u\_{2\beta}=2(1+\beta)T\|\sigma^{-1}\|\_{F}^{2}).
Therefore

|  |  |  |
| --- | --- | --- |
|  | ∫g′​(α​(y))2​φT​(y)​𝑑y≤κα2​Cβ​(1+K2​β​𝔼ℙ∗​eu2​β​‖B‖2+K2​𝔼ℙ∗​eu2​‖B‖2),\int g^{\prime}(\alpha(y))^{2}\,\varphi\_{T}(y)\,dy\;\leq\;\kappa\_{\alpha}^{2}\,C\_{\beta}\Big(1+K\_{2\beta}\,\mathbb{E}\_{\mathbb{P}^{\*}}e^{u\_{2\beta}\|B\|^{2}}+K\_{2}\,\mathbb{E}\_{\mathbb{P}^{\*}}e^{u\_{2}\|B\|^{2}}\Big), |  |

which is finite provided u2​β<γ02u\_{2\beta}<\gamma\_{0}^{2} and u2<γ02u\_{2}<\gamma\_{0}^{2}.
Combining above cases yields h​(ℙ∗)<∞h(\mathbb{P}^{\*})<\infty.
A convenient single sufficient condition is

|  |  |  |
| --- | --- | --- |
|  | γ02> 8​T​‖σ−1‖F2​max⁡{ 1+β, 2},\gamma\_{0}^{2}\;>\;8\,T\,\|\sigma^{-1}\|\_{F}^{2}\,\max\{\,1+\beta,\,2\,\}, |  |

which ensures u2​β<γ02u\_{2\beta}<\gamma\_{0}^{2} and u2<γ02u\_{2}<\gamma\_{0}^{2}.

Denote μ=𝔼ℙ∗[LT(B,.)]∈H\mu=\mathbb{E}\_{\mathbb{P}^{\*}}\left[L\_{T}(B,.)\right]\in H. By Lemma [9](https://arxiv.org/html/2512.01408v1#Thmlemma9 "Lemma 9. ‣ D.4 Part IV ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), the map 𝒯:H→ℝ\mathcal{T}:H\to\mathbb{R} such that 𝒯​(h)=∫g​(h​(y))​φT​(y)​𝑑y\mathcal{T}(h)=\int g(h(y))\varphi\_{T}(y)dy is Hadamard differentiable at μ\mu if β≤1\beta\leq 1 and is Hadamard differentiable at μ\mu tangential to L1+βL^{1+\beta} if β>1\beta>1. Thus, from the functional Delta theorem and its weaker version with tangential Hadamard differentiability, we have

|  |  |  |
| --- | --- | --- |
|  | n(𝒯(𝔼ℙn[LT(B,.)])−𝒯(μ))\displaystyle\sqrt{n}\left(\mathcal{T}\left(\mathbb{E}\_{\mathbb{P}\_{n}}\left[L\_{T}(B,.)\right]\right)-\mathcal{T}(\mu)\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =n​(∫g​(𝔼ℙn​[LT​(B,y)])​φT​(y)​𝑑y−∫g​(𝔼ℙ∗​[LT​(B,y)])​φT​(y)​𝑑y)\displaystyle=\sqrt{n}\left(\int g(\mathbb{E}\_{\mathbb{P}\_{n}}\left[L\_{T}(B,y)\right])\varphi\_{T}(y)dy-\int g(\mathbb{E}\_{\mathbb{P}^{\*}}\left[L\_{T}(B,y)\right])\varphi\_{T}(y)dy\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =J​(ℙn)−J​(ℙ∗)⇒𝒯μ′​(G),\displaystyle=J(\mathbb{P}\_{n})-J(\mathbb{P}^{\*})\Rightarrow\mathcal{T}^{\prime}\_{\mu}(G), |  |

where 𝒯μ′\mathcal{T}^{\prime}\_{\mu} is the Hadamard derivative at μ\mu. By Lemma [9](https://arxiv.org/html/2512.01408v1#Thmlemma9 "Lemma 9. ‣ D.4 Part IV ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), the limiting distribution becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯μ′​(G)\displaystyle\mathcal{T}^{\prime}\_{\mu}(G) | =∫g′​(α​(y))​G​(y)​φT​(y)​𝑑y∼𝒩​(0,h​(ℙ∗)).\displaystyle=\int g^{\prime}(\alpha(y))G(y)\varphi\_{T}(y)dy\sim\mathcal{N}(0,h(\mathbb{P}^{\*})). |  |

∎

###### Lemma 9.

In the context of Lemma [8](https://arxiv.org/html/2512.01408v1#Thmlemma8 "Lemma 8. ‣ D.4 Part IV ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), the map 𝒯\mathcal{T} is Hadamard differentiable at μ\mu if β≤1\beta\leq 1 and is Hadamard differentiable at μ\mu tangential to L1+βL^{1+\beta} if β>1\beta>1. In particular, for a fixed direction v∈Hv\in H (or v∈L1+βv\in L^{1+\beta} in the tangential case),

|  |  |  |
| --- | --- | --- |
|  | 𝒯μ′​(v)=∫g′​(α​(y))​v​(y)​φT​(y)​𝑑y.\mathcal{T}^{\prime}\_{\mu}(v)=\int g^{\prime}(\alpha(y))v(y)\varphi\_{T}(y)dy. |  |

###### Proof.

We first focus on the case when β>0\beta>0 and fix v∈Hv\in H and any perturbations vt∈Hv\_{t}\in H with vt→vv\_{t}\to v in HH as t↓0t\downarrow 0.
We must show

|  |  |  |
| --- | --- | --- |
|  | 𝒯​(α+t​vt)−𝒯​(α)t⟶∫g′​(α)​v​φTas ​t↓0.\frac{\mathcal{T}(\alpha+tv\_{t})-\mathcal{T}(\alpha)}{t}\;\longrightarrow\;\int g^{\prime}(\alpha)\,v\,\varphi\_{T}\quad\text{as }t\downarrow 0. |  |

By the fundamental theorem of calculus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯​(μ+t​vt)−𝒯​(μ)t\displaystyle\frac{\mathcal{T}(\mu+tv\_{t})-\mathcal{T}(\mu)}{t} | =∫ℝdg​(μ​(y)+t​vt​(y))−g​(μ​(y))t​φT​(y)​𝑑y\displaystyle=\int\_{\mathbb{R}^{d}}\frac{g(\mu(y)+tv\_{t}(y))-g(\mu(y))}{t}\,\varphi\_{T}(y)\,dy |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01∫ℝdg′​(μ​(y)+s​t​vt​(y))​vt​(y)​φT​(y)​𝑑y​𝑑s.\displaystyle=\int\_{0}^{1}\!\int\_{\mathbb{R}^{d}}g^{\prime}\big(\mu(y)+stv\_{t}(y)\big)\,v\_{t}(y)\,\varphi\_{T}(y)\,dy\,ds. |  |

Add and subtract ∫ℝdg′​(μ​(y))​v​(y)​φT​(y)​𝑑y\int\_{\mathbb{R}^{d}}g^{\prime}(\mu(y))\,v(y)\,\varphi\_{T}(y)\,dy:

|  |  |  |
| --- | --- | --- |
|  | 𝒯​(μ+t​vt)−𝒯​(μ)t−∫ℝdg′​(μ)​v​φT=∫ℝdg′​(μ)​(vt−v)​φT⏟=⁣:At+∫01∫ℝd[g′​(μ+s​t​vt)−g′​(μ)]​vt​φT​𝑑y​𝑑s⏟=⁣:Bt.\frac{\mathcal{T}(\mu+tv\_{t})-\mathcal{T}(\mu)}{t}-\int\_{\mathbb{R}^{d}}g^{\prime}(\mu)\,v\,\varphi\_{T}=\underbrace{\int\_{\mathbb{R}^{d}}g^{\prime}(\mu)\,(v\_{t}-v)\,\varphi\_{T}}\_{=:A\_{t}}+\underbrace{\int\_{0}^{1}\!\int\_{\mathbb{R}^{d}}\!\big[g^{\prime}(\mu+stv\_{t})-g^{\prime}(\mu)\big]\,v\_{t}\,\varphi\_{T}\,dy\,ds}\_{=:B\_{t}}. |  |

By Cauchy–Schwarz inequality,

|  |  |  |
| --- | --- | --- |
|  | |At|≤‖g′​(μ)‖L2​(φT)​‖vt−v‖L2​(φT)⟶ 0,|A\_{t}|\;\leq\;\|g^{\prime}(\mu)\|\_{L^{2}(\varphi\_{T})}\,\|v\_{t}-v\|\_{L^{2}(\varphi\_{T})}\;\longrightarrow\;0, |  |

since g′​(μ)∈L2​(φT)g^{\prime}(\mu)\in L^{2}(\varphi\_{T}) (see the estimate in proof of Lemma [8](https://arxiv.org/html/2512.01408v1#Thmlemma8 "Lemma 8. ‣ D.4 Part IV ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) and vt→vv\_{t}\to v in L2​(φT)L^{2}(\varphi\_{T}). Hence At→0A\_{t}\to 0.

Fix δ∈(0,min⁡{β,1})\delta\in(0,\min\{\beta,1\}). Using the elementary inequality

|  |  |  |
| --- | --- | --- |
|  | |xβ−yβ|≤βδ​|x−y|δ​(xβ−δ+yβ−δ)(x,y≥0),|x^{\beta}-y^{\beta}|\;\leq\;\frac{\beta}{\delta}\,|x-y|^{\delta}\,\big(x^{\beta-\delta}+y^{\beta-\delta}\big)\qquad(x,y\geq 0), |  |

applied with x=μ​(y)+s​t​|vt​(y)|x=\mu(y)+st|v\_{t}(y)|, y=μ​(y)y=\mu(y) and g′​(m)=κα​mβg^{\prime}(m)=\kappa\_{\alpha}m^{\beta}, we obtain

|  |  |  |
| --- | --- | --- |
|  | |Bt|≤C​|t|δ​∫ℝd(μ​(y)β−δ+(μ​(y)+s​t​|vt​(y)|)β−δ)​|vt​(y)|1+δ​φT​(y)​𝑑y.|B\_{t}|\;\leq\;C\,|t|^{\delta}\!\int\_{\mathbb{R}^{d}}\!\Big(\mu(y)^{\beta-\delta}+(\mu(y)+st|v\_{t}(y)|)^{\beta-\delta}\Big)\,|v\_{t}(y)|^{1+\delta}\,\varphi\_{T}(y)\,dy. |  |

Using (a+b)β−δ≤C​(aβ−δ+bβ−δ)(a+b)^{\beta-\delta}\leq C\,(a^{\beta-\delta}+b^{\beta-\delta}) and |t|β−δ≤1|t|^{\beta-\delta}\leq 1 for small tt,

|  |  |  |
| --- | --- | --- |
|  | |Bt|≤C​|t|δ​{∫ℝdμ​(y)β−δ​|vt​(y)|1+δ​φT​(y)​𝑑y⏟It,1+|t|β−δ​∫ℝd|vt​(y)|1+β​φT​(y)​𝑑y⏟It,2}.|B\_{t}|\;\leq\;C\,|t|^{\delta}\!\left\{\underbrace{\int\_{\mathbb{R}^{d}}\mu(y)^{\beta-\delta}\,|v\_{t}(y)|^{1+\delta}\,\varphi\_{T}(y)\,dy}\_{I\_{t,1}}\;+\;\underbrace{|t|^{\beta-\delta}\int\_{\mathbb{R}^{d}}|v\_{t}(y)|^{1+\beta}\,\varphi\_{T}(y)\,dy}\_{I\_{t,2}}\right\}. |  |

For the first term, apply the Hölder inequality with p=21+δp=\tfrac{2}{1+\delta} and q=21−δq=\tfrac{2}{1-\delta}:

|  |  |  |
| --- | --- | --- |
|  | It,1≤‖μβ−δ‖Lq​(φT)​‖vt‖L2​(φT).I\_{t,1}\;\leq\;\|\mu^{\beta-\delta}\|\_{L^{q}(\varphi\_{T})}\,\|v\_{t}\|\_{L^{2}(\varphi\_{T})}. |  |

Under the sub-Gaussian parameter

|  |  |  |
| --- | --- | --- |
|  | γ02> 2​(1+β)​T​‖σ−1‖F2,\gamma\_{0}^{2}\;>\;2(1+\beta)\,T\,\|\sigma^{-1}\|\_{F}^{2}, |  |

we have
‖μβ−δ‖Lq​(φT)<∞\|\mu^{\beta-\delta}\|\_{L^{q}(\varphi\_{T})}<\infty for any small δ∈(0,1)\delta\in(0,1), and since vt→vv\_{t}\to v in L2​(φT)L^{2}(\varphi\_{T}),
‖vt‖L2​(φT)\|v\_{t}\|\_{L^{2}(\varphi\_{T})} is uniformly bounded. Hence It,1≤CI\_{t,1}\leq C uniformly in tt.

For the second term, we consider two cases.
When 0<β≤10<\beta\leq 1, because 1+β≤21+\beta\leq 2,

|  |  |  |
| --- | --- | --- |
|  | ∫ℝd|vt|1+β​φT≤ 1+∫ℝd|vt|2​φT≤C,\int\_{\mathbb{R}^{d}}|v\_{t}|^{1+\beta}\,\varphi\_{T}\;\leq\;1+\int\_{\mathbb{R}^{d}}|v\_{t}|^{2}\,\varphi\_{T}\;\leq\;C, |  |

uniformly in tt. Choose δ=β\delta=\beta (so δ≤1\delta\leq 1). Then

|  |  |  |
| --- | --- | --- |
|  | |Bt|≤C​(|t|δ+|t|δ)=C​|t|β⟶ 0.|B\_{t}|\;\leq\;C\,\big(|t|^{\delta}+|t|^{\delta}\big)\;=\;C\,|t|^{\beta}\ \longrightarrow\ 0. |  |

When β>1\beta>1, suppose that v∈L1+β​(φT)​and ​vt→v​ in ​L1+βv\in L^{1+\beta}(\varphi\_{T})\ \text{and }v\_{t}\to v\text{ in }L^{1+\beta}, then

|  |  |  |
| --- | --- | --- |
|  | sup0<t≤1‖vt‖L1+β​(φT)<∞.\sup\_{0<t\leq 1}\ \|v\_{t}\|\_{L^{1+\beta}(\varphi\_{T})}\ <\ \infty. |  |

Therefore It,2≤C​|t|β−δ=C​|t|β−1+ε→0I\_{t,2}\leq C\,|t|^{\beta-\delta}=C\,|t|^{\beta-1+\varepsilon}\to 0 as t↓0t\downarrow 0. Hence

|  |  |  |
| --- | --- | --- |
|  | |Bt|≤C​|t|δ​It,1+C​|t|δ​It,2≤C​|t|δ+C​|t|β−1+ε→t↓0 0,|B\_{t}|\ \leq\ C\,|t|^{\delta}\,I\_{t,1}\;+\;C\,|t|^{\delta}\,I\_{t,2}\ \leq\ C\,|t|^{\delta}\;+\;C\,|t|^{\beta-1+\varepsilon}\ \xrightarrow[t\downarrow 0]{}\ 0, |  |

since δ=1−ε∈(0,1)\delta=1-\varepsilon\in(0,1) and β−1+ε>0\beta-1+\varepsilon>0.

When β<0\beta<0, let t:=σ−T​Bt:=\sigma^{-T}B and pick any R>0R>0; then

|  |  |  |
| --- | --- | --- |
|  | μ(y)=𝔼[exp(⟨t,y⟩−T2∥t∥2)]≥ℙ(∥t∥≤R)exp(−R∥y∥−T2R2)=:c0e−R​‖y‖.\mu(y)=\mathbb{E}\!\left[\exp\!\left(\langle t,y\rangle-\tfrac{T}{2}\|t\|^{2}\right)\right]\;\geq\;\mathbb{P}(\|t\|\leq R)\,\exp\!\left(-R\|y\|-\tfrac{T}{2}R^{2}\right)=:c\_{0}\,e^{-R\|y\|}. |  |

Hence, for ε∈(0,c0)\varepsilon\in(0,c\_{0}),

|  |  |  |
| --- | --- | --- |
|  | {μ<ε}⊂{‖y‖>1R​log⁡c0ε}.\{\mu<\varepsilon\}\ \subset\ \Big\{\|y\|>\tfrac{1}{R}\log\!\tfrac{c\_{0}}{\varepsilon}\Big\}. |  |

Since φT\varphi\_{T} is a nondegenerate Gaussian measure, there are C1,C2>0C\_{1},C\_{2}>0 such that

|  |  |  |
| --- | --- | --- |
|  | φT​{μ<ε}≤φT​(‖y‖>1R​log⁡c0ε)≤C1​exp⁡(−C2​(log⁡(1/ε))2).\varphi\_{T}\{\mu<\varepsilon\}\ \leq\ \varphi\_{T}\!\Big(\|y\|>\tfrac{1}{R}\log\!\tfrac{c\_{0}}{\varepsilon}\Big)\ \leq\ C\_{1}\,\exp\!\Big(-C\_{2}\,(\log(1/\varepsilon))^{2}\Big). |  |

We will also use that for any a>0a>0,

|  |  |  |
| --- | --- | --- |
|  | ∫{‖y‖>L}ea​‖y‖​φT​(y)​𝑑y→L→∞ 0,since ​ea​‖y‖≪ec​‖y‖2​for Gaussian tails.\int\_{\{\|y\|>L\}}e^{a\|y\|}\,\varphi\_{T}(y)\,dy\ \xrightarrow[L\to\infty]{}\ 0,\quad\text{since }\ e^{a\|y\|}\ll e^{c\|y\|^{2}}\ \text{for Gaussian tails}. |  |

For ε>0\varepsilon>0 define

|  |  |  |
| --- | --- | --- |
|  | gε′​(m):=κα​(m∨ε)β,gε​(0):=g​(0),gε​(m):=g​(0)+∫0mgε′​(u)​𝑑u,g^{\prime}\_{\varepsilon}(m):=\kappa\_{\alpha}\,(m\vee\varepsilon)^{\beta},\qquad g\_{\varepsilon}(0):=g(0),\quad g\_{\varepsilon}(m):=g(0)+\int\_{0}^{m}g^{\prime}\_{\varepsilon}(u)\,du, |  |

and set 𝒯ε​(h):=∫gε​(h)​φT\mathcal{T}\_{\varepsilon}(h):=\int g\_{\varepsilon}(h)\,\varphi\_{T}.
For fixed ε>0\varepsilon>0, gε′g^{\prime}\_{\varepsilon} is bounded and Lipschitz on [0,∞)[0,\infty), so the standard L2L^{2} chain rule gives

|  |  |  |
| --- | --- | --- |
|  | 𝒯ε​(μ+t​vt)−𝒯ε​(μ)t⟶∫ℝdgε′(μ(y))v(y)φT(y)dy=:𝒯ε′(μ)[v]as t↓0,vt→v in H.\frac{\mathcal{T}\_{\varepsilon}(\mu+tv\_{t})-\mathcal{T}\_{\varepsilon}(\mu)}{t}\ \longrightarrow\ \int\_{\mathbb{R}^{d}}g^{\prime}\_{\varepsilon}(\mu(y))\,v(y)\,\varphi\_{T}(y)\,dy=:\mathcal{T}^{\prime}\_{\varepsilon}(\mu)[v]\quad\text{as }t\downarrow 0,\ \ v\_{t}\to v\text{ in }H. |  |

For any vt→vv\_{t}\to v in HH as t↓0t\downarrow 0,

|  |  |  |
| --- | --- | --- |
|  | 𝒯​(μ+t​vt)−𝒯​(μ)t−∫g′​(μ)​v​φT=E1,ε,t+E2,ε,t+E3,ε,\frac{\mathcal{T}(\mu+tv\_{t})-\mathcal{T}(\mu)}{t}-\int g^{\prime}(\mu)\,v\,\varphi\_{T}=E\_{1,\varepsilon,t}+E\_{2,\varepsilon,t}+E\_{3,\varepsilon}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | E1,ε,t:=𝒯​(μ+t​vt)−𝒯ε​(μ+t​vt)t,E2,ε,t:=𝒯ε​(μ+t​vt)−𝒯ε​(μ)t−𝒯ε′​(μ)​[v],E3,ε:=𝒯ε′​(μ)​[v]−𝒯′​(μ)​[v].E\_{1,\varepsilon,t}:=\frac{\mathcal{T}(\mu+tv\_{t})-\mathcal{T}\_{\varepsilon}(\mu+tv\_{t})}{t},\ \ E\_{2,\varepsilon,t}:=\frac{\mathcal{T}\_{\varepsilon}(\mu+tv\_{t})-\mathcal{T}\_{\varepsilon}(\mu)}{t}-\mathcal{T}^{\prime}\_{\varepsilon}(\mu)[v],\ \ E\_{3,\varepsilon}:=\mathcal{T}^{\prime}\_{\varepsilon}(\mu)[v]-\mathcal{T}^{\prime}(\mu)[v]. |  |

For fixed ε>0\varepsilon>0, E2,ε,t→0E\_{2,\varepsilon,t}\to 0 as t↓0t\downarrow 0.

On {μ+t​vt≥ε}\{\mu+tv\_{t}\geq\varepsilon\}, gε=gg\_{\varepsilon}=g; on {μ+t​vt<ε}\{\mu+tv\_{t}<\varepsilon\} and for m≤εm\leq\varepsilon,
a direct computation shows |g​(m)−gε​(m)|≤C​εβ+1|g(m)-g\_{\varepsilon}(m)|\leq C\,\varepsilon^{\beta+1}.
Hence

|  |  |  |
| --- | --- | --- |
|  | |E1,ε,t|≤C​εβ+1|t|​φT​(μ+t​|vt|<ε).|E\_{1,\varepsilon,t}|\ \leq\ \frac{C\,\varepsilon^{\beta+1}}{|t|}\,\varphi\_{T}(\mu+t|v\_{t}|<\varepsilon). |  |

Using {μ+t​|vt|<ε}⊂{μ<2​ε}∪{|t|​|vt|>ε}\{\mu+t|v\_{t}|<\varepsilon\}\subset\{\mu<2\varepsilon\}\cup\{|t|\,|v\_{t}|>\varepsilon\} and Chebyshev,

|  |  |  |
| --- | --- | --- |
|  | φT​(μ+t​|vt|<ε)≤φT​(μ<2​ε)+|t|2ε2​‖vt‖22.\varphi\_{T}(\mu+t|v\_{t}|<\varepsilon)\ \leq\ \varphi\_{T}(\mu<2\varepsilon)+\frac{|t|^{2}}{\varepsilon^{2}}\,\|v\_{t}\|\_{2}^{2}. |  |

Therefore

|  |  |  |
| --- | --- | --- |
|  | |E1,ε,t|≤C​{εβ+1|t|​e−C2​(log⁡(1/ε))2+|t|ε1−β}+o​(1)(t↓0).|E\_{1,\varepsilon,t}|\ \leq\ C\left\{\frac{\varepsilon^{\beta+1}}{|t|}\,e^{-C\_{2}(\log(1/\varepsilon))^{2}}+\frac{|t|}{\varepsilon^{1-\beta}}\right\}+o(1)\qquad(t\downarrow 0). |  |

Choose ε=ε​(t):=|t|k\varepsilon=\varepsilon(t):=|t|^{k} with any k∈(0,11−β)k\in\big(0,\,\tfrac{1}{1-\beta}\big) (possible since β<0\beta<0).
Then |t|ε1−β=|t| 1−k​(1−β)→0\frac{|t|}{\varepsilon^{1-\beta}}=|t|^{\,1-k(1-\beta)}\to 0, and the term with e−C2​(log⁡(1/ε))2e^{-C\_{2}(\log(1/\varepsilon))^{2}} also vanishes.

Next,

|  |  |  |
| --- | --- | --- |
|  | |E3,ε|=|∫((μ∨ε)β−μβ)​v​φT|≤‖v‖2​‖((μ∨ε)β−μβ)​𝟏{μ<ε}‖2.|E\_{3,\varepsilon}|=\left|\int\big((\mu\vee\varepsilon)^{\beta}-\mu^{\beta}\big)\,v\,\varphi\_{T}\right|\ \leq\ \|v\|\_{2}\,\Big\|\big((\mu\vee\varepsilon)^{\beta}-\mu^{\beta}\big)\mathbf{1}\_{\{\mu<\varepsilon\}}\Big\|\_{2}. |  |

On {μ<ε}\{\mu<\varepsilon\} we have (μ∨ε)β=εβ≤μβ(\mu\vee\varepsilon)^{\beta}=\varepsilon^{\beta}\leq\mu^{\beta} (since β<0\beta<0), so

|  |  |  |
| --- | --- | --- |
|  | ‖((μ∨ε)β−μβ)​𝟏{μ<ε}‖2≤‖μβ​ 1{μ<ε}‖2=(∫{μ<ε}μ​(y)2​β​φT​(y)​𝑑y)1/2.\Big\|\big((\mu\vee\varepsilon)^{\beta}-\mu^{\beta}\big)\mathbf{1}\_{\{\mu<\varepsilon\}}\Big\|\_{2}\ \leq\ \|\mu^{\beta}\,\mathbf{1}\_{\{\mu<\varepsilon\}}\|\_{2}=\left(\int\_{\{\mu<\varepsilon\}}\mu(y)^{2\beta}\,\varphi\_{T}(y)\,dy\right)^{\!1/2}. |  |

Using μ​(y)≥c0​e−R​‖y‖\mu(y)\geq c\_{0}e^{-R\|y\|}, we get μ​(y)2​β≤c02​β​e|2​β|​R​‖y‖\mu(y)^{2\beta}\leq c\_{0}^{2\beta}\,e^{\,|2\beta|R\|y\|}.
Together with {μ<ε}⊂{‖y‖>(1/R)​log⁡(c0/ε)}\{\mu<\varepsilon\}\subset\{\|y\|>(1/R)\log(c\_{0}/\varepsilon)\},

|  |  |  |
| --- | --- | --- |
|  | ∫{μ<ε}μ2​β​φT⟶ 0(ε↓0),\int\_{\{\mu<\varepsilon\}}\mu^{2\beta}\,\varphi\_{T}\ \longrightarrow\ 0\qquad(\varepsilon\downarrow 0), |  |

hence E3,ε→0E\_{3,\varepsilon}\to 0.

Therefore with all cases,

|  |  |  |
| --- | --- | --- |
|  | 𝒯​(μ+t​vt)−𝒯​(μ)t⟶∫ℝdg′​(μ​(y))​v​(y)​φT​(y)​𝑑y,\frac{\mathcal{T}(\mu+tv\_{t})-\mathcal{T}(\mu)}{t}\ \longrightarrow\ \int\_{\mathbb{R}^{d}}g^{\prime}(\mu(y))\,v(y)\,\varphi\_{T}(y)\,dy, |  |

which proves Hadamard differentiability of 𝒯\mathcal{T} at μ\mu with derivative 𝒯μ′​(v)\mathcal{T}^{\prime}\_{\mu}(v) as claimed.
∎

By Lemmas [7](https://arxiv.org/html/2512.01408v1#Thmlemma7 "Lemma 7. ‣ D.4 Part IV ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") and [8](https://arxiv.org/html/2512.01408v1#Thmlemma8 "Lemma 8. ‣ D.4 Part IV ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), we have F​(0)=Op​(n−1/2)F(0)=O\_{p}(n^{-1/2}) and the denominator converges to c>0c>0 in probability, and hence

|  |  |  |
| --- | --- | --- |
|  | ‖Δ∗‖n=Op​(1).\|\Delta^{\*}\|\_{n}=O\_{p}(1). |  |

### D.5 Part V

Now we solve the equation for a λ\lambda with the remainder term R​(Δ)R(\Delta). We first redefine some notations for convenience.
Let

|  |  |  |
| --- | --- | --- |
|  | c¯n:=1n​∑i=1n‖Ci​(n)‖2,Δ​(λ)i:=λ​Ci​(n),Gn​(λ):=F​(0)+c¯nn​λ+Rn​(λ),\bar{c}\_{n}:=\frac{1}{n}\sum\_{i=1}^{n}\|C\_{i}(n)\|^{2},\qquad\Delta(\lambda)\_{i}:=\lambda\,C\_{i}(n),\qquad G\_{n}(\lambda):=F(0)+\frac{\bar{c}\_{n}}{\sqrt{n}}\,\lambda+R\_{n}(\lambda), |  |

where Rn​(λ)R\_{n}(\lambda) is the Taylor remainder term. Therefore, c¯n→𝑝c>0\bar{c}\_{n}\xrightarrow{p}c>0, n​F​(0)=Op​(1)\sqrt{n}\,F(0)=O\_{p}(1), and for any fixed M≥1M\geq 1 there exist random constants
K1,n,K2,n,K1,n′=Op​(1)K\_{1,n},K\_{2,n},K^{\prime}\_{1,n}=O\_{p}(1) such that for all |λ|≤M|\lambda|\leq M,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |Rn​(λ)|\displaystyle|R\_{n}(\lambda)| | ≤K1,n​‖Δ​(λ)‖n2n+K2,n​(‖Δ​(λ)‖n2n)2,\displaystyle\leq K\_{1,n}\,\frac{\|\Delta(\lambda)\|\_{n}^{2}}{n}+K\_{2,n}\,\Big(\frac{\|\Delta(\lambda)\|\_{n}^{2}}{n}\Big)^{2}, |  | (56) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |Rn​(λ1)−Rn​(λ2)|\displaystyle|R\_{n}(\lambda\_{1})-R\_{n}(\lambda\_{2})| | ≤K1,n′​c¯nn​(|λ1|+|λ2|)​|λ1−λ2|for all ​|λ1|,|λ2|≤M,\displaystyle\leq K^{\prime}\_{1,n}\,\frac{\bar{c}\_{n}}{n}\,(\,|\lambda\_{1}|+|\lambda\_{2}|\,)\,|\lambda\_{1}-\lambda\_{2}|\qquad\text{for all }|\lambda\_{1}|,|\lambda\_{2}|\leq M, |  | (57) |

where ‖Δ​(λ)‖n2=λ2​c¯n\|\Delta(\lambda)\|\_{n}^{2}=\lambda^{2}\,\bar{c}\_{n}.
Define Tn​(λ):=−n​F​(0)+n​Rn​(λ)c¯nT\_{n}(\lambda):=-\dfrac{\sqrt{n}\,F(0)+\sqrt{n}\,R\_{n}(\lambda)}{\bar{c}\_{n}}. Since c¯n→𝑝c>0\bar{c}\_{n}\xrightarrow{p}c>0 and n​F​(0)=Op​(1)\sqrt{n}\,F(0)=O\_{p}(1), choose c0∈(0,c)c\_{0}\in(0,c) and K0>0K\_{0}>0 so that, for large nn, with probability ≥1−ε\geq 1-\varepsilon,
c¯n≥c0\bar{c}\_{n}\geq c\_{0} and n​|F​(0)|≤K0\sqrt{n}\,|F(0)|\leq K\_{0}. For |λ1|,|λ2|≤M|\lambda\_{1}|,|\lambda\_{2}|\leq M, by ([57](https://arxiv.org/html/2512.01408v1#A4.E57 "In D.5 Part V ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")),

|  |  |  |
| --- | --- | --- |
|  | |Tn(λ1)−Tn(λ2)|=nc¯n|Rn(λ1)−Rn(λ2)|≤2​K1,n′​Mn|λ1−λ2|=:qn(M)|λ1−λ2|.|T\_{n}(\lambda\_{1})-T\_{n}(\lambda\_{2})|=\frac{\sqrt{n}}{\bar{c}\_{n}}|R\_{n}(\lambda\_{1})-R\_{n}(\lambda\_{2})|\leq\frac{2K^{\prime}\_{1,n}M}{\sqrt{n}}\,|\lambda\_{1}-\lambda\_{2}|=:q\_{n}(M)\,|\lambda\_{1}-\lambda\_{2}|. |  |

Since K1,n′=Op​(1)K^{\prime}\_{1,n}=O\_{p}(1), qn​(M)→0q\_{n}(M)\to 0 in probability; hence for nn large enough, qn​(M)≤12q\_{n}(M)\leq\tfrac{1}{2}, so TnT\_{n} is a contraction on [−M,M][-M,M].

Next, we show that TnT\_{n} maps [−M,M][-M,M] into itself with high probability. For |λ|≤M|\lambda|\leq M, using ([56](https://arxiv.org/html/2512.01408v1#A4.E56 "In D.5 Part V ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) and ‖Δ​(λ)‖n2=λ2​c¯n\|\Delta(\lambda)\|\_{n}^{2}=\lambda^{2}\bar{c}\_{n},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Tn​(λ)|\displaystyle|T\_{n}(\lambda)| | ≤n​|F​(0)|c¯n+nc¯n​|Rn​(λ)|\displaystyle\leq\frac{\sqrt{n}\,|F(0)|}{\bar{c}\_{n}}+\frac{\sqrt{n}}{\bar{c}\_{n}}|R\_{n}(\lambda)| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K0c0+K1,n​M2n+K2,n​M4​c¯nn3/2=K0c0+op​(1).\displaystyle\leq\frac{K\_{0}}{c\_{0}}+\frac{K\_{1,n}M^{2}}{\sqrt{n}}+\frac{K\_{2,n}M^{4}\,\bar{c}\_{n}}{n^{3/2}}=\frac{K\_{0}}{c\_{0}}+o\_{p}(1). |  |

Choose M≥2​K0/c0M\geq 2K\_{0}/c\_{0}. Then Tn​([−M,M])⊆[−M,M]T\_{n}([-M,M])\subseteq[-M,M]. By Banach fixed point theorem, a unique fixed point λn∗∈[−M,M]\lambda\_{n}^{\*}\in[-M,M] exists with Tn​(λn∗)=λn∗T\_{n}(\lambda\_{n}^{\*})=\lambda\_{n}^{\*}.
Hence ‖Δ∗‖n=|λn∗|​c¯n1/2=Op​(1)\|\Delta^{\*}\|\_{n}=|\lambda\_{n}^{\*}|\,\bar{c}\_{n}^{1/2}=O\_{p}(1). Let

|  |  |  |
| --- | --- | --- |
|  | λnlin:=−n​F​(0)/c¯n,\lambda\_{n}^{\mathrm{lin}}:=-\sqrt{n}\,F(0)/\bar{c}\_{n}, |  |

then

|  |  |  |
| --- | --- | --- |
|  | λn∗−λnlin=−n​Rn​(λn∗)c¯n=Op​(nc¯n⋅(λn∗)2​c¯nn)=Op​(n−1/2).\lambda\_{n}^{\*}-\lambda\_{n}^{\mathrm{lin}}=-\frac{\sqrt{n}\,R\_{n}(\lambda\_{n}^{\*})}{\bar{c}\_{n}}=O\_{p}\!\Big(\frac{\sqrt{n}}{\bar{c}\_{n}}\cdot\frac{(\lambda\_{n}^{\*})^{2}\bar{c}\_{n}}{n}\Big)=O\_{p}(n^{-1/2}). |  |

Hence, we have shown that for any fixed ε>0\varepsilon>0, there exists NεN\_{\varepsilon} such that for all n≥Nεn\geq N\_{\varepsilon}, with probability at least 1−ε1-\varepsilon, there is a correction Δ=Δn\Delta=\Delta\_{n} satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Δ‖n=Op​(1)andJ​(ℙnΔ)=J​(ℙ∗).\|\Delta\|\_{n}=O\_{p}(1)\qquad\text{and}\qquad J(\mathbb{P}\_{n}^{\Delta})=J(\mathbb{P}^{\*}). |  | (58) |

Let EnE\_{n} be the event in ([58](https://arxiv.org/html/2512.01408v1#A4.E58 "In D.5 Part V ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")). We define a measurable choice to work on EnE\_{n} by

|  |  |  |
| --- | --- | --- |
|  | Δ^n:={Δnon ​En,0on ​Enc.\widehat{\Delta}\_{n}\;:=\;\begin{cases}\Delta\_{n}&\text{on }E\_{n},\\ 0&\text{on }E\_{n}^{c}.\end{cases} |  |

By construction, ‖Δ^n‖n=Op​(1)\|\widehat{\Delta}\_{n}\|\_{n}=O\_{p}(1) and J​(ℙnΔ^n)=J​(ℙ∗)J(\mathbb{P}\_{n}^{\widehat{\Delta}\_{n}})=J(\mathbb{P}^{\*}) on EnE\_{n}.
With the cost function cτ​(Δ):=eτ​‖x−y‖22− 1c\_{\tau}(\Delta)\;:=\;e^{\,\tau\,\|x-y\|\_{2}^{2}}\;-\;1, couple BiB\_{i} with Bi+Δ^n,i/nB\_{i}+\widehat{\Delta}\_{n,i}/\sqrt{n}. Then with the notation mn=max1≤i≤n⁡‖Δ^n,i‖22nm\_{n}=\max\_{1\leq i\leq n}\frac{\|\widehat{\Delta}\_{n,i}\|\_{2}^{2}}{n}, we have

|  |  |  |
| --- | --- | --- |
|  | Dc​(ℙn,ℙnΔ^n)≤τn​∑i=1n‖Δ^n,in‖22​eτ​mn=τ​‖Δ^n‖n2n​eτ​mn=op​(1),D\_{c}(\mathbb{P}\_{n},\mathbb{P}\_{n}^{\widehat{\Delta}\_{n}})\;\leq\;\frac{\tau}{n}\sum\_{i=1}^{n}\Big\|\frac{\widehat{\Delta}\_{n,i}}{\sqrt{n}}\Big\|\_{2}^{2}e^{\tau m\_{n}}=\frac{\tau\|\widehat{\Delta}\_{n}\|\_{n}^{2}}{n}e^{\tau m\_{n}}=o\_{p}(1), |  |

since ‖Δ^n‖n=Op​(1)\|\widehat{\Delta}\_{n}\|\_{n}=O\_{p}(1) and max1≤i≤n⁡‖Δ^n‖2=Op​(n1/4)\max\_{1\leq i\leq n}\|\widehat{\Delta}\_{n}\|\_{2}=O\_{p}(n^{1/4}).

Then

|  |  |  |
| --- | --- | --- |
|  | Rn​(k∗)≤Dc​(ℙn,ℙnΔ^n)and hencen​Rn​(k∗)≤τ​‖Δ^n‖n2​(1+op​(1))=Op​(1).R\_{n}(k^{\*})\ \leq\ D\_{c}(\mathbb{P}\_{n},\mathbb{P}\_{n}^{\widehat{\Delta}\_{n}})\qquad\text{and hence}\qquad n\,R\_{n}(k^{\*})\ \leq\ \tau\|\widehat{\Delta}\_{n}\|\_{n}^{2}(1+o\_{p}(1))\;=\;O\_{p}(1). |  |

Write

|  |  |  |
| --- | --- | --- |
|  | Gi:=∫g′​(α​(y))​∇bLT​(Bi,y)​φT​(y)​𝑑y,gn:=1n​∑i=1n‖Gi‖22.G\_{i}\ :=\ \int g^{\prime}(\alpha(y))\,\nabla\_{b}L\_{T}(B\_{i},y)\,\varphi\_{T}(y)\,dy,\qquad g\_{n}:=\frac{1}{n}\sum\_{i=1}^{n}\|G\_{i}\|\_{2}^{2}. |  |

Since

|  |  |  |
| --- | --- | --- |
|  | 1n​∑i=1nGi⋅Δi=1n​∑i=1nCi​(n)⋅Δi+1n​∑i=1n(Gi−Ci​(n))⋅Δi,\frac{1}{n}\sum\_{i=1}^{n}G\_{i}\cdot\Delta\_{i}=\frac{1}{n}\sum\_{i=1}^{n}C\_{i}(n)\cdot\Delta\_{i}\;+\;\frac{1}{n}\sum\_{i=1}^{n}\bigl(G\_{i}-C\_{i}(n)\bigr)\cdot\Delta\_{i}, |  |

we have

|  |  |  |
| --- | --- | --- |
|  | |1n​∑i=1n(Gi−Ci​(n))⋅Δi|≤1n​∑i=1n‖Δi‖2​‖∫(g′​(mPn​(y))−g′​(α​(y)))​∇bLT​(Bi,y)​φT​(y)​𝑑y‖2=op​(1).\Bigl|\frac{1}{n}\sum\_{i=1}^{n}\bigl(G\_{i}-C\_{i}(n)\bigr)\cdot\Delta\_{i}\Bigr|\leq\frac{1}{n}\sum\_{i=1}^{n}\|\Delta\_{i}\|\_{2}\,\Bigl\|\int\!\bigl(g^{\prime}(m\_{P\_{n}}(y))-g^{\prime}(\alpha(y))\bigr)\,\nabla\_{b}L\_{T}(B\_{i},y)\,\varphi\_{T}(y)\,dy\Bigr\|\_{2}=o\_{p}(1). |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | 1n​∑i=1nGi⋅Δi=−n​F​(0)+op​(1).\frac{1}{n}\sum\_{i=1}^{n}G\_{i}\cdot\Delta\_{i}=-\,\sqrt{n}\,F(0)\;+\;o\_{p}(1). |  |

By the Hölder inequality, the feasibility constraint is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1n​∑i=1nGi⋅Δi=−n​F​(0)+op​(1),\frac{1}{n}\sum\_{i=1}^{n}G\_{i}\cdot\Delta\_{i}\;=\;-\sqrt{n}\,F(0)\ +\ o\_{p}(1), |  | (59) |

and minimizing the quadratic surrogate cost 1n​∑‖Δi/n‖22\frac{1}{n}\sum\|\Delta\_{i}/\sqrt{n}\|\_{2}^{2} subject to ([59](https://arxiv.org/html/2512.01408v1#A4.E59 "In D.5 Part V ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections")) yields the candidate

|  |  |  |
| --- | --- | --- |
|  | Δilin:=−n​F​(0)gn​Gi,i=1,…,n.\;\;\Delta\_{i}^{\mathrm{lin}}\;:=\;-\,\frac{\sqrt{n}\,F(0)}{\,g\_{n}\,}\;G\_{i}\;,\;\;i=1,\dots,n. |  |

Then the feasibility constraint holds exactly:

|  |  |  |
| --- | --- | --- |
|  | 1n​∑i=1nGi⋅Δilin=−n​F​(0)gn​1n​∑i=1nGi⋅Gi=−n​F​(0)gn​1n​∑i=1n‖Gi‖22=−n​F​(0).\frac{1}{n}\sum\_{i=1}^{n}G\_{i}\cdot\Delta\_{i}^{\mathrm{lin}}=-\,\frac{\sqrt{n}\,F(0)}{g\_{n}}\,\frac{1}{n}\sum\_{i=1}^{n}G\_{i}\cdot G\_{i}=-\,\frac{\sqrt{n}\,F(0)}{g\_{n}}\,\frac{1}{n}\sum\_{i=1}^{n}\|G\_{i}\|\_{2}^{2}=-\,\sqrt{n}\,F(0). |  |

Moreover,

|  |  |  |
| --- | --- | --- |
|  | ‖Δlin‖n2:=1n​∑i=1n‖Δilin‖22=n​F​(0)2gn2⋅1n​∑i=1n‖Gi‖22=n​F​(0)2gn.\bigl\|\Delta^{\mathrm{lin}}\bigr\|\_{n}^{2}:=\frac{1}{n}\sum\_{i=1}^{n}\bigl\|\Delta\_{i}^{\mathrm{lin}}\bigr\|\_{2}^{2}=\frac{nF(0)^{2}}{g\_{n}^{2}}\cdot\frac{1}{n}\sum\_{i=1}^{n}\|G\_{i}\|\_{2}^{2}=\frac{nF(0)^{2}}{g\_{n}}. |  |

Using the remainder bounds from the Taylor expansion and the contraction mapping argument proved earlier,
the exact correction Δ^n\widehat{\Delta}\_{n} differs from Δlin\Delta^{\mathrm{lin}} by op​(1)o\_{p}(1) in ∥⋅∥n\|\cdot\|\_{n},
and hence

|  |  |  |
| --- | --- | --- |
|  | n​Rn​(k∗)≤n​Dc​(ℙn,ℙnΔ^n)=τ​n​F​(0)2gn+op​(1).n\,R\_{n}(k^{\*})\ \leq\ n\,D\_{c}(\mathbb{P}\_{n},\mathbb{P}\_{n}^{\widehat{\Delta}\_{n}})\ =\tau\frac{n\,F(0)^{2}}{g\_{n}}\ +\ o\_{p}(1). |  |

Then an application of Lemma [8](https://arxiv.org/html/2512.01408v1#Thmlemma8 "Lemma 8. ‣ D.4 Part IV ‣ Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections"), weak law of large numbers, and the continuous mapping theorem shows the asymptotic result on EnE\_{n}.

### D.6 Part VI

###### Lemma 10.

We define β=α1−α\beta=\frac{\alpha}{1-\alpha}, then the sub-Gaussian assumption to make all the lemmas in Section [D](https://arxiv.org/html/2512.01408v1#A4 "Appendix D Generalization of Nonlinear Projection Theorem with Non-compact Support ‣ Bayesian Distributionally Robust Merton Problem with Nonlinear Wasserstein Projections") all hold is there exists γ0>0\gamma\_{0}>0 such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ∗​[exp⁡(γ2​‖B‖22)]<∞for every ​γ<γ0.\mathbb{E}\_{\mathbb{P}^{\*}}\big[\exp(\gamma^{2}\|B\|\_{2}^{2})\big]<\infty\quad\text{for every }\gamma<\gamma\_{0}. |  |

with

|  |  |  |
| --- | --- | --- |
|  | γ02‖σ−1‖F2>T​max⁡{ 4​β2−2​β,2β−2, 16, 8​β+8}.\frac{\gamma\_{0}^{2}}{\left\|\sigma^{-1}\right\|\_{F}^{2}}>T\max\Big\{\,4\beta^{2}-2\beta,\ \tfrac{2}{\beta-2},\ 16,\ 8\beta+8\,\Big\}. |  |

###### Proof.

It suffices to reduce the maximum

|  |  |  |
| --- | --- | --- |
|  | max⁡{2​(2​β2−β),2​s​(2−1),2​p2−p,16,8​(1+β)}\max\left\{2(2\beta^{2}-\beta),2s(2-1),2p^{2}-p,16,8(1+\beta)\right\} |  |

with s=1p−1s=\frac{1}{p-1} and p=β−1p=\beta-1, where β=α1−α\beta=\frac{\alpha}{1-\alpha}.

Rewrite each term in β\beta:

|  |  |  |
| --- | --- | --- |
|  | 2​(2​β2−β)=4​β2−2​β,2​s​(2−1)=2β−2,2​p2−p=2​(β−1)2−(β−1)=2​β2−5​β+3,2(2\beta^{2}-\beta)=4\beta^{2}-2\beta,\qquad 2s(2-1)=\frac{2}{\beta-2},\qquad 2p^{2}-p=2(\beta-1)^{2}-(\beta-1)=2\beta^{2}-5\beta+3, |  |

|  |  |  |
| --- | --- | --- |
|  | 8​(1+β)=8​β+8.\qquad 8(1+\beta)=8\beta+8. |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | M​(β)=max⁡{ 4​β2−2​β,2β−2, 2​β2−5​β+3, 16, 8​β+8}.M(\beta)=\max\Big\{\,4\beta^{2}-2\beta,\ \tfrac{2}{\beta-2},\ 2\beta^{2}-5\beta+3,\ 16,\ 8\beta+8\,\Big\}. |  |

Note that

|  |  |  |
| --- | --- | --- |
|  | (4​β2−2​β)−(2​β2−5​β+3)=2​β2+3​β−3.(4\beta^{2}-2\beta)-(2\beta^{2}-5\beta+3)=2\beta^{2}+3\beta-3. |  |

The RHS is ≥0\geq 0 for β≥β0:=−3+334≈0.686\beta\geq\beta\_{0}:=\frac{-3+\sqrt{33}}{4}\approx 0.686. For 0<β≤β00<\beta\leq\beta\_{0},
2​β2−5​β+3≤3<162\beta^{2}-5\beta+3\leq 3<16
(since 2​β2−5​β+32\beta^{2}-5\beta+3 is strictly decreasing on (0,β0](0,\beta\_{0}]).
Therefore 2​β2−5​β+32\beta^{2}-5\beta+3 never attains the maximum on β>0\beta>0, and we may simplify to

|  |  |  |
| --- | --- | --- |
|  | M​(β)=max⁡{ 4​β2−2​β,2β−2, 16, 8​β+8}.M(\beta)=\max\Big\{\,4\beta^{2}-2\beta,\ \tfrac{2}{\beta-2},\ 16,\ 8\beta+8\,\Big\}. |  |

∎

Finally, suppose XnX\_{n} and YnY\_{n} are sequences of random variables such that
0≤Xn≤Yn0\leq X\_{n}\leq Y\_{n} on the events EnE\_{n} which is true with probability 1 as n→∞n\to\infty. Hence, for any fixed ε>0\varepsilon>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(Xn≥ε)\displaystyle\mathbb{P}\left(X\_{n}\geq\varepsilon\right) | =ℙ​(Xn≥ε,En)+ℙ​(Xn≥ε,Enc)\displaystyle=\mathbb{P}\left(X\_{n}\geq\varepsilon,E\_{n}\right)+\mathbb{P}\left(X\_{n}\geq\varepsilon,E\_{n}^{c}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ℙ​(Yn≥ε,En)+ℙ​(Enc).\displaystyle\leq\mathbb{P}\left(Y\_{n}\geq\varepsilon,E\_{n}\right)+\mathbb{P}\left(E\_{n}^{c}\right). |  |

Hence, Yn=op​(1)Y\_{n}=o\_{p}(1) implies Xn=op​(1)X\_{n}=o\_{p}(1) and the same is for Op​(1)O\_{p}(1). If we let Xn=n​Rn​(k∗)X\_{n}=n\,R\_{n}(k^{\*}) and Yn=τ​n​F​(0)2gn+op​(1)Y\_{n}=\tau\ \frac{n\,F(0)^{2}}{g\_{n}}\ +\ o\_{p}(1), then for any t≥0t\geq 0,

|  |  |  |
| --- | --- | --- |
|  | lim supn→∞ℙ​(Xn>t)≤ℙ​(Yn>t).\limsup\_{n\to\infty}\mathbb{P}\left(X\_{n}>t\right)\leq\mathbb{P}\left(Y\_{n}>t\right). |  |

Hence, the proof of the asymptotic stochastic upper bound is completed.