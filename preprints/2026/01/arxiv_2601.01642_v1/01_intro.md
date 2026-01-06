---
authors:
- Dohyun Ahn
- Huiyi Chen
- Lewen Zheng
doc_id: arxiv:2601.01642v1
family_id: arxiv:2601.01642
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Wasserstein Distributionally Robust Rare-Event Simulation
url_abs: http://arxiv.org/abs/2601.01642v1
url_html: https://arxiv.org/html/2601.01642v1
venue: arXiv q-fin
version: 1
year: 2026
---


Dohyun Ahn,   Huiyi Chen
  
The Chinese University of Hong Kong
  
Lewen Zheng
  
Huawei Hong Kong Research Center
Corresponding author, E-mail: [dohyun.ahn@cuhk.edu.hk](mailto:dohyun.ahn@cuhk.edu.hk)

(January 2026)

###### Abstract

Standard rare-event simulation techniques require exact distributional specifications, which limits their effectiveness in the presence of distributional
uncertainty. To address this, we develop a novel framework for estimating rare-event probabilities subject to such distributional model risk. Specifically,
we focus on computing worst-case rare-event probabilities, defined as a distributionally robust bound against a Wasserstein ambiguity set centered at a specific nominal
distribution. By exploiting a dual characterization of this bound, we propose Distributionally Robust Importance Sampling (DRIS), a computationally tractable methodology designed to substantially reduce the variance associated with estimating the dual components. The proposed method is simple to implement and requires low sampling costs. Most importantly, it achieves *vanishing relative error*—the strongest efficiency guarantee that is notoriously difficult to establish in rare-event simulation. Our numerical studies confirm the superior performance of DRIS against existing
benchmarks.

## 1.  Introduction

From managing financial tail risk to predicting extreme climate events, quantifying the likelihood of rare events is critical for system stability and safety (Glasserman2003-MCFE; Asmussen2007; Rubino2009).
The fundamental mathematical task involves estimating the probability that a random vector falls into a critical rare-event set. Since standard Monte Carlo methods are computationally inefficient for such tasks, sophisticated variance reduction techniques—such
as importance sampling, conditional Monte Carlo, splitting, and stratification—have been developed for various models and problems; see, e.g., Glasserman2000-var-red; Glasserman2008; Juneja:02; bassamboo\_portfolio\_2008; Blanchet2014-queue; bai\_rare-event\_2022; Ahn2023; deo2025achieving and references therein.

However, a significant theoretical gap persists: these classical methods assume precise knowledge of the underlying probability distributions, making them vulnerable to model misspecification. In real-world scenarios, such granular information is rarely available—particularly when data are scarce or noisy—resulting in distributional uncertainty. To overcome this limitation, we employ *a distributionally robust approach to rare-event simulation*. To be more specific, we focus on efficiently computing worst-case rare-event probabilities over a family of plausible distributions, mathematically formalized as a Wasserstein ball surrounding a nominal distributional model. To the best of our knowledge, this is the first study to introduce an efficient Monte Carlo approach for rare-event probability estimation in the presence of distributional model risk.

In terms of developing simulation methods for worst-case expectations under model uncertainty, our approach is closely related to those of Glasserman2014 and Blanchet2017. The former proposes the so-called robust Monte Carlo to estimate risk measures over distributional ambiguity sets defined by relative entropy and α\alpha-divergence, while the latter focuses on computing worst-case expectations of two random vectors with fixed marginals but unknown dependence structures. Despite such methodological developments, neither of these prior studies specifically target variance reduction for rare-event simulation; consequently, their efficacy in this regime remains unestablished.

Regarding distributional robustness specifically for rare-events, existing literature has predominantly relied on optimization-based or extreme-value-theory-based approaches rather than simulation methodologies; see, for instance,
Lam2017-robust-tail; BlanchetHM2020 and Bai2023.
Concurrently, a recent study by
Huang2023
utilizes random walk tail probabilities to analyze the vulnerability of rare-event probabilities to tail uncertainty, arguing that heavy-tailed cases exhibit a higher sensitivity to model misspecification than light-tailed cases. In contrast, we put an emphasis on simulation and bridge the gap by proposing a variance reduction technique for estimating worst-case rare-event probabilities.

Specifically, this paper develops a novel importance sampling method, which we call *Distributionally Robust Importance Sampling (DRIS)*, to estimate the aforementioned worst-case rare-event probabilities for convex target sets. Leveraging a general duality result for Wasserstein distributionally robust optimization, the probability of interest can be reformulated as the probability of a neighborhood of the target set under the nominal distribution. From a computational viewpoint, this dual reformulation requires a two-step process: first estimating the neighborhood and then incorporating it into the final probability computation. Since both steps involve rare-event simulation, our DRIS method is designed to address these requirements via a cohesive, computationally efficient, and easy-to-implement algorithm.

Most importantly, we establish that the DRIS estimator admits a central limit theorem and exhibits *vanishing relative error* (Theorems [2](https://arxiv.org/html/2601.01642v1#Thmtheorem2 "Theorem 2 (Central Limit Theorem). ‣ 4.2. Efficiency of DRIS ‣ 4. Main Algorithm and Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation") and [3](https://arxiv.org/html/2601.01642v1#Thmtheorem3 "Theorem 3 (Vanishing Relative Error). ‣ 4.2. Efficiency of DRIS ‣ 4. Main Algorithm and Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")). These main theoretical results are built upon (i) empirical process theory with Vapnik–Chervonenkis-type arguments and (ii) rare-event analysis in simulation. It is worth emphasizing that the property of vanishing relative error, which ensures the relative error decays to zero as the target event becomes increasingly rare, is arguably the highest notion of efficiency in rare-event simulation and is seldom achieved in prior studies.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2601.01642v1#S2 "2. Problem Formulation ‣ Wasserstein Distributionally Robust Rare-Event Simulation") formulates the main problem. In Section [3](https://arxiv.org/html/2601.01642v1#S3 "3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation"), we review strong duality for Wasserstein distributionally robust optimization in the context of worst-case probabilities and present preliminary theoretical results. Section [4](https://arxiv.org/html/2601.01642v1#S4 "4. Main Algorithm and Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation") introduces the proposed DRIS procedure and establishes its theoretical performance guarantees in the rare-event regime. In Section [5](https://arxiv.org/html/2601.01642v1#S5 "5. Numerical Experiments ‣ Wasserstein Distributionally Robust Rare-Event Simulation"), we numerically validate the effectiveness of the algorithm. Section [6](https://arxiv.org/html/2601.01642v1#S6 "6. Concluding Remarks ‣ Wasserstein Distributionally Robust Rare-Event Simulation") concludes the paper. All proofs are deferred to the appendices.

## 2.  Problem Formulation

Let 𝒫{\cal P} denote the set of all probability distributions supported on the nn-dimensional Euclidean space. Then, the 2-Wasserstein distance between 𝖯0,𝖯∈𝒫{\sf P}\_{0},{\sf P}\in{\cal P} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒲2​(𝖯0,𝖯)=infπ∈Π​(𝖯0,𝖯)(𝖤(𝐗0,𝐗)∼π​[‖𝐗0−𝐗‖2])1/2,{\cal W}\_{2}({\sf P}\_{0},{\sf P})=\inf\_{\pi\in\Pi({\sf P}\_{0},{\sf P})}\left({\sf E}\_{({\mathbf{X}}\_{0},{\mathbf{X}})\sim\pi}\big[\|{\mathbf{X}}\_{0}-{\mathbf{X}}\|^{2}\big]\right)^{1/2}, |  | (1) |

where Π​(𝖯0,𝖯)\Pi({\sf P}\_{0},{\sf P}) is the set of all couplings of 𝖯0{\sf P}\_{0} and 𝖯{\sf P}, that is, the set of all joint distributions with marginals 𝖯0{\sf P}\_{0} and 𝖯{\sf P}, respectively. Accordingly, the 2-Wasserstein ball of radius δ>0\delta>0 centered at the nominal distribution 𝖯0{\sf P}\_{0} is given by

|  |  |  |
| --- | --- | --- |
|  | ℬδ​(𝖯0)={𝖯∈𝒫:𝒲2​(𝖯0,𝖯)≤δ}.{\cal B}\_{\delta}({\sf P}\_{0})=\{{\sf P}\in{\cal P}:{\cal W}\_{2}({\sf P}\_{0},{\sf P})\leq\delta\}. |  |

In this paper, we investigate the estimation of the worst-case probability defined by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p∗=sup𝖯∈ℬδ​(𝖯0)𝖯​(𝐗∈ℰ),p\_{\*}=\sup\_{{\sf P}\in{\cal B}\_{\delta}({\sf P}\_{0})}{\sf P}({\mathbf{X}}\in{\cal E}), |  | (2) |

where δ∈(0,∞)\delta\in(0,\infty) is a fixed constant, ℰ{\cal E} is a nonempty, full-dimensional, closed, and convex set that does not contain the origin, and 𝖯0{\sf P}\_{0} is the nn-dimensional standard normal distribution. This quantity corresponds to a version of the inner worst-case problem
in Wasserstein distributionally robust optimization, which has received considerable attention in recent literature (zhangYG2025).
Although we focus on Gaussian nominal distributions, the proposed methodology extends naturally to other multivariate elliptical families. We prioritize the Gaussian setting due to its prevalence in the OR/MS literature, where critical metrics often correspond to rare-event probabilities governed by standard normal distributions (Bucklew2004, Chapter 9). Below is one of such examples in finance:

###### Example 1.

According to Glasserman2000-var-red, the loss of a portfolio of European call/put options over the time interval [t,t+d​t][t,t+{\rm d}t] can be approximated by

|  |  |  |
| --- | --- | --- |
|  | L≔V​(𝐒t,t)−V​(𝐒t+d​𝐒,t+d​t)≈−∂V∂t​d​t−Δ⊤​d​𝐒−12​d​𝐒⊤​Γ​d​𝐒≕L~,L\coloneqq V({\mathbf{S}}\_{t},t)-V({\mathbf{S}}\_{t}+{\rm d}{\mathbf{S}},t+{\rm d}t)\approx-\frac{\partial V}{\partial t}{\rm d}t-\Delta^{\top}{\rm d}{\mathbf{S}}-\frac{1}{2}{\rm d}{\mathbf{S}}^{\top}\Gamma{\rm d}{\mathbf{S}}\eqqcolon\tilde{L}, |  |

where 𝐒t{\mathbf{S}}\_{t} and V​(𝐒t,t)V({\mathbf{S}}\_{t},t) denote the values of nn risk factors and the portfolio value, respectively, d​𝐒=𝐒t+d​t−𝐒t{\rm d}{\mathbf{S}}={\mathbf{S}}\_{t+{\rm d}t}-{\mathbf{S}}\_{t}, Δ=∇𝐒V⊤\Delta=\nabla\_{{\mathbf{S}}}V^{\top}, Γ=∇𝐒2V\Gamma=\nabla^{2}\_{{\mathbf{S}}}V, and “≈\approx” holds by the delta-gamma approximation.
If d​𝐒=𝐒t+d​t−𝐒t{\rm d}{\mathbf{S}}={\mathbf{S}}\_{t+{\rm d}t}-{\mathbf{S}}\_{t} follows a multivariate normal and the approximation is exact (i.e., L=L~L=\tilde{L}),

|  |  |  |
| --- | --- | --- |
|  | 𝖯​(L>ℓ)=𝖯​(a+∑i=1n(bi​Xi+ci​Xi2)>ℓ),{\sf P}(L>\ell)={\sf P}\left(a+\sum\_{i=1}^{n}\left(b\_{i}X\_{i}+c\_{i}X\_{i}^{2}\right)>\ell\right), |  |

for a loss threshold ℓ>0\ell>0, fixed constants a,b1,…,bn,c1,…,cna,b\_{1},\ldots,b\_{n},c\_{1},\ldots,c\_{n} with c1,…,cn≤0c\_{1},\ldots,c\_{n}\leq 0, and X1,…,Xn∼𝗂𝗂𝖽𝒩​(0,1)X\_{1},\ldots,X\_{n}\stackrel{{\scriptstyle{\sf iid}}}{{\sim}}{\cal N}(0,1).
This quantity is commonly used to define a portfolio risk measure, and when ℓ\ell is large, it becomes a probability that independent standard normals belong to a convex rare-event set.

In addition to this example, many continuous-time stochastic models, such as geometric Brownian motion and Gaussian Markov processes, can be simulated as weighted sums of standard normal variables via the Euler scheme, which is essential not only for financial modeling but also for analyzing system stability in other domains: heavy-traffic approximations in queueing theory rely on diffusion processes driven by Brownian motion, and demand processes in supply chain management are often modeled as Gaussian random walks.

It is worth noting that if 𝐗{\mathbf{X}} follows an nn-dimensional non-standard normal distribution, one can find 𝝁∈ℝn\boldsymbol{\mu}\in\mathbb{R}^{n} and 𝚲∈ℝn×m{\boldsymbol{\Lambda}}\in\mathbb{R}^{n\times m} with n≥mn\geq m such that 𝐗{\mathbf{X}} has that same distribution as 𝝁+𝚲​𝐗~\boldsymbol{\mu}+{\boldsymbol{\Lambda}}\widetilde{\mathbf{X}}, where 𝐗~\widetilde{\mathbf{X}} follows an mm-dimensional standard normal distribution. Accordingly, the probability 𝖯​(𝐗∈ℰ){\sf P}({\mathbf{X}}\in{\cal E}) coincides with the probability that 𝐗~\widetilde{\mathbf{X}} belongs to another convex set given by {𝐱:𝝁+𝚲​𝐱∈ℰ}\{{\mathbf{x}}:\boldsymbol{\mu}+{\boldsymbol{\Lambda}}{\mathbf{x}}\in{\cal E}\}. Consequently, restricting the analysis to the standard normal distribution suffices for all Gaussian models.

Without loss of any generality, we assume that 𝐱∗≔arg⁡min𝐱∈ℰ⁡‖𝐱‖{\mathbf{x}}^{\*}\coloneqq\arg\min\_{{\mathbf{x}}\in{\cal E}}\|{\mathbf{x}}\| lies on the x1x\_{1}-axis. It can be satisfied through a suitable rotation of the coordinates and a rearrangement of the variables, which does not affect ([2](https://arxiv.org/html/2601.01642v1#S2.E2 "In 2. Problem Formulation ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) because the standard normal distribution is invariant under such transformations. Furthermore, we focus on a situation where {𝐗∈ℰ}\{{\mathbf{X}}\in{\cal E}\} is a rare event in the sense that its likelihood is close to zero. We study this mathematically by
considering a sequence of sets indexed by a rarity parameter r>0r>0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰr={r‖𝐱∗‖​𝐱:𝐱∈ℰ},{\cal E}\_{r}=\left\{\frac{r}{\|{\mathbf{x}}^{\*}\|}{\mathbf{x}}:{\mathbf{x}}\in{\cal E}\right\}, |  | (3) |

in which case (r,0,…,0)=arg⁡min𝐱∈ℰr⁡‖𝐱‖(r,0,\ldots,0)=\arg\min\_{{\mathbf{x}}\in{\cal E}\_{r}}\|{\mathbf{x}}\|. Hence, the set ℰr{\cal E}\_{r} moves away from the origin as r→∞r\to\infty, leading to limr→∞𝖯0​(𝐗∈ℰr)=0\lim\_{r\to\infty}{\sf P}\_{0}({\mathbf{X}}\in{\cal E}\_{r})=0.

To analyze the efficiency of the proposed estimator, we adopt the following performance criterion widely used in the rare-event simulation literature (see, e.g., bassamboo\_portfolio\_2008; NakayamaT2023):

###### Definition 1.

Let qrq\_{r} denote a quantity of interest satisfying qr→0q\_{r}\to 0 as r→∞r\to\infty. Suppose that an unbiased estimator QN,rQ\_{N,r} for qrq\_{r}, constructed by NN iid samples, admits a central limit theorem with asymptotic variance ξr2\xi\_{r}^{2} for any r>0r>0; that is,
N​(QN,r−qr)⇒𝒩​(0,ξr2)\sqrt{N}(Q\_{N,r}-q\_{r})\Rightarrow{\cal N}(0,\xi\_{r}^{2}) as N→∞N\to\infty, where ⇒\Rightarrow represents convergence in distribution, and 𝒩​(γ,ν2){\cal N}(\gamma,\nu^{2}) means a normal random variable with mean γ\gamma and variance ν2\nu^{2}.
Then, we say that QN,rQ\_{N,r} has vanishing relative error if

|  |  |  |
| --- | --- | --- |
|  | lim supr→∞ξrqr=0.\limsup\_{r\to\infty}\frac{\xi\_{r}}{q\_{r}}=0. |  |

Vanishing relative error is often regarded as the highest efficiency notion in the context of rare-event simulation. As noted in botev\_normal\_2017, Monte Carlo estimators for light-tailed distributions seldom exhibit vanishing relative error. This property ensures that, given a fixed large sample size, the accuracy of the associated estimator improves as the target event becomes rarer.

## 3.  Preliminaries

In this section, we review a strong duality result for our target quantity in ([2](https://arxiv.org/html/2601.01642v1#S2.E2 "In 2. Problem Formulation ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) and introduce our preliminary theoretical analysis. Both play a crucial role in making the problem tractable and facilitating the main analysis in Section [4](https://arxiv.org/html/2601.01642v1#S4 "4. Main Algorithm and Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation"). Before delving into the details, let us briefly introduce our notational conventions used throughout the paper. We denote by 𝖤0{\sf E}\_{0} the expectation under the nominal distribution 𝖯0{\sf P}\_{0}, and we use d​(𝐱,𝒮)=min𝐲∈𝒮⁡‖𝐱−𝐲‖d({\mathbf{x}},{\cal S})=\min\_{{\mathbf{y}}\in{\cal S}}\|{\mathbf{x}}-{\mathbf{y}}\| to represent the distance between a point 𝐱∈ℝn{\mathbf{x}}\in\mathbb{R}^{n} and a set 𝒮⊂ℝn{\cal S}\subset\mathbb{R}^{n}. Also, for brevity, we write 𝖤0​[g​(𝐗);𝒜]≔𝖤0​[g​(𝐗)​𝟙​{𝒜}]{\sf E}\_{0}[g({\mathbf{X}});{\cal A}]\coloneqq{\sf E}\_{0}[g({\mathbf{X}})\mathds{1}\{{\cal A}\}] for any function gg and any event 𝒜{\cal A}.

Strong duality for ([2](https://arxiv.org/html/2601.01642v1#S2.E2 "In 2. Problem Formulation ‣ Wasserstein Distributionally Robust Rare-Event Simulation")).
The optimization problem in ([2](https://arxiv.org/html/2601.01642v1#S2.E2 "In 2. Problem Formulation ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) is infinite-dimensional and thus intractable to solve directly. Fortunately, established results in the literature on Wasserstein distributionally robust optimization demonstrate that the dual formulation of ([2](https://arxiv.org/html/2601.01642v1#S2.E2 "In 2. Problem Formulation ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) is computationally tractable. We restate a version of these results in our framework and discuss its implications for rare-event simulation.

###### Lemma 1 (Theorem 2 of Blanchet2019-DRO).

Let h​(u)=𝖤0​[d​(𝐗,ℰ)2;d​(𝐗,ℰ)≤u]h(u)={\sf E}\_{0}[d({\mathbf{X}},{\cal E})^{2};d({\mathbf{X}},{\cal E})\leq u] and p​(u)=𝖯0​(d​(𝐗,ℰ)≤u)p(u)={\sf P}\_{0}(d({\mathbf{X}},{\cal E})\leq u). Then, the probability p∗p\_{\*}
in ([2](https://arxiv.org/html/2601.01642v1#S2.E2 "In 2. Problem Formulation ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) is equal to p​(u∗)p({u\_{\*}}), where u∗=h−1​(δ2){u\_{\*}}=h^{-1}(\delta^{2}).

Figure 1: A graphical illustration of the relationship between the target set and its inflated version based on the duality result

u∗u\_{\*}x1∗x\_{1}^{\*}𝟎{\bf 0}𝐱∗{\mathbf{x}}^{\*}ℰ\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}{{\cal E}}{𝐱:d​(𝐱,ℰ)≤u∗}\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}{\{{\mathbf{x}}:d({\mathbf{x}},{\cal E})\leq u\_{\*}\}}

The significance of this duality result lies in expressing the worst-case probability p∗p\_{\*} as the probability, under the nominal distribution 𝖯0{\sf P}\_{0}, of an inflated superset of the target event, given by {𝐱:d​(𝐱,ℰ)≤u∗}\{{\mathbf{x}}:d({\mathbf{x}},{\cal E})\leq{u\_{\*}}\}. Figure [1](https://arxiv.org/html/2601.01642v1#S3.F1 "Figure 1 ‣ 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation") illustrates the connection between the target set and its inflated counterpart: the blue slashed region depicts the target set ℰ{\cal E}, while the red shaded area corresponds to its inflated version {𝐱:d​(𝐱,ℰ)≤u∗}\{{\mathbf{x}}:d({\mathbf{x}},{\cal E})\leq{u\_{\*}}\}. The dotted circles represent a radius of u∗u\_{\*}; the union of such circles centered at all points in ℰ{\cal E} characterizes the inflated superset. Based on the assumption in Section [2](https://arxiv.org/html/2601.01642v1#S2 "2. Problem Formulation ‣ Wasserstein Distributionally Robust Rare-Event Simulation"), 𝐱∗{\mathbf{x}}^{\*} lies on the x1x\_{1}-axis, and hence, its distance from the origin is x1∗x\_{1}^{\*}.

Since Lemma [1](https://arxiv.org/html/2601.01642v1#Thmlemma1 "Lemma 1 (Theorem 2 of Blanchet2019-DRO). ‣ 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation") holds for any set ℰ{\cal E}, the function h​(⋅)h(\cdot) and the value u∗u\_{\*} in the lemma are similarly defined for the sequence of sets {ℰr}r>0\{{\cal E}\_{r}\}\_{r>0} in ([3](https://arxiv.org/html/2601.01642v1#S2.E3 "In 2. Problem Formulation ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) as follows: for r>0r>0 and δ,u≥0\delta,u\geq 0, we let

|  |  |  |
| --- | --- | --- |
|  | hr​(u)=𝖤0​[d​(𝐗,ℰr)2;d​(𝐗,ℰr)≤u]​and​ur=hr−1​(δ2).h\_{r}(u)={\sf E}\_{0}[d({\mathbf{X}},{\cal E}\_{r})^{2};d({\mathbf{X}},{\cal E}\_{r})\leq u]~~\text{and}~~u\_{r}=h\_{r}^{-1}(\delta^{2}). |  |

Then, by the above lemma, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | pr≔sup𝖯∈ℬδ​(𝖯0)𝖯​(𝐗∈ℰr)=𝖯0​(d​(𝐗,ℰr)≤ur).p\_{r}\coloneqq\sup\_{{\sf P}\in{\cal B}\_{\delta}({\sf P}\_{0})}{\sf P}({\mathbf{X}}\in{\cal E}\_{r})={\sf P}\_{0}(d({\mathbf{X}},{\cal E}\_{r})\leq u\_{r}). |  | (4) |

Although uru\_{r} and prp\_{r} depend on the radius δ\delta of the 2-Wasserstein ball, this dependence is suppressed in the notation.

Preliminary theoretical results. Given our rare-event regime where rr tends to ∞\infty, we analyze how uru\_{r} and prp\_{r} behave as rr grows. Firstly, the following lemma describes the behavior of uru\_{r}:

###### Lemma 2 (Asymptotic Behavior of uru\_{r}).

For any δ,M>0\delta,M>0, there exists r0>0r\_{0}>0 such that for all r≥r0r\geq r\_{0},

|  |  |  |  |
| --- | --- | --- | --- |
|  | M<r−ur<Φ¯−1​(δ2r2),M<r-u\_{r}<\bar{\Phi}^{-1}\left(\frac{\delta^{2}}{r^{2}}\right), |  | (5) |

where Φ¯​(⋅)\bar{\Phi}(\cdot) denotes the standard normal complementary cumulative distribution function.

Observe that r−urr-u\_{r} represents the distance between the origin and the inflated version of ℰr{\cal E}\_{r}. Hence, by the first inequality in ([5](https://arxiv.org/html/2601.01642v1#S3.E5 "In Lemma 2 (Asymptotic Behavior of 𝑢_𝑟). ‣ 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation")), Lemma [2](https://arxiv.org/html/2601.01642v1#Thmlemma2 "Lemma 2 (Asymptotic Behavior of 𝑢_𝑟). ‣ 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation") confirms that the inflated superset moves away from the origin as rr increases, which suggests that *prp\_{r} in ([4](https://arxiv.org/html/2601.01642v1#S3.E4 "In 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) is again a rare-event probability*. This motivates us to develop an efficient rare-event simulation algorithm for estimating this probability.

Furthermore, as shown in Appendix [A](https://arxiv.org/html/2601.01642v1#A1 "Appendix A Proofs of the Theoretical Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation"), Φ¯−1​(δ2/r2)\bar{\Phi}^{-1}(\delta^{2}/r^{2}) in ([5](https://arxiv.org/html/2601.01642v1#S3.E5 "In Lemma 2 (Asymptotic Behavior of 𝑢_𝑟). ‣ 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) grows sublinearly as r→∞r\to\infty. Consequently, the second inequality in ([5](https://arxiv.org/html/2601.01642v1#S3.E5 "In Lemma 2 (Asymptotic Behavior of 𝑢_𝑟). ‣ 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) implies that this distance diverges at a sublinear rate. This indicates that the worst-case probability prp\_{r} decays slower than the exponential rate of the nominal probability 𝖯0​(𝐗∈ℰr){\sf P}\_{0}({\mathbf{X}}\in{\cal E}\_{r}). We formalize this observation in the following theorem, which characterizes the asymptotic lower bound for prp\_{r} as r→∞r\to\infty.

###### Theorem 1 (Asymptotic Behavior of prp\_{r}).

For any δ>0\delta>0, lim infr→∞r2​pr≥δ2\liminf\_{r\to\infty}r^{2}p\_{r}\geq\delta^{2}.

According to this theorem, achieving vanishing relative error (Definition [1](https://arxiv.org/html/2601.01642v1#Thmdefinition1 "Definition 1. ‣ 2. Problem Formulation ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) for the estimation of prp\_{r} requires the construction of an NN-sample-based unbiased estimator whose asymptotic variance decays at a rate faster than r−4r^{-4}. In the next section, we propose a novel importance sampling estimator that satisfies this condition.

## 4.  Main Algorithm and Results

Lemma [1](https://arxiv.org/html/2601.01642v1#Thmlemma1 "Lemma 1 (Theorem 2 of Blanchet2019-DRO). ‣ 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation") allows us to compute the worst-case probability p∗p\_{\*} in two steps: (a) solving h​(u)=δ2h(u)=\delta^{2} to obtain u∗{u\_{\*}} and (b) evaluating p​(u∗)p({u\_{\*}}). Both tasks involve the estimation of expectations under the nominal distribution 𝖯0{\sf P}\_{0} defined over the rare-event sets of the form {𝐱:d​(𝐱,ℰ)≤u}\{{\mathbf{x}}:d({\mathbf{x}},{\cal E})\leq u\} (see Section [3](https://arxiv.org/html/2601.01642v1#S3 "3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation")). Accordingly, in this section, we propose a comprehensive and tractable algorithm that addresses these two rare-event estimation steps and demonstrate that it achieves vanishing relative error.

### 4.1.  DRIS Algorithm

For the above-mentioned tasks, sampling 𝐗{\mathbf{X}} in the vicinity of the rare-event set {𝐱:d​(𝐱,ℰ)≤u}\{{\mathbf{x}}:d({\mathbf{x}},{\cal E})\leq u\} is essential for any feasible uu. We identify X1X\_{1} as the primary driver of the said rare event since {𝐱:d​(𝐱,ℰ)≤u}⊆{𝐱:x1≥x1∗−u}\{{\mathbf{x}}:d({\mathbf{x}},{\cal E})\leq u\}\subseteq\{{\mathbf{x}}:x\_{1}\geq x\_{1}^{\*}-u\} holds for all uu.
Moreover, the rare-event set {𝐱:d​(𝐱,ℰ)≤u}\{{\mathbf{x}}:d({\mathbf{x}},{\cal E})\leq u\} is the Minkowski sum of two convex sets ℰ{\cal E} and {𝐱:‖𝐱‖≤u}\{{\mathbf{x}}:\|{\mathbf{x}}\|\leq u\}, and therefore, is also convex.
Consequently, inspired by the conditional importance sampling method in ahnZwsc:23, our importance sampling approach involves: (a) generating X1X\_{1} via X1=x1∗−u+Y/(x1∗−u)X\_{1}=x\_{1}^{\*}-u+Y/(x\_{1}^{\*}-u), with YY drawn from the standard exponential distribution; and (b) sampling (X2,…,Xn)(X\_{2},\ldots,X\_{n}) from the standard normal distribution.

We then define 𝐙=(Y,X2,⋯,Xn)⊤{\mathbf{Z}}=(Y,X\_{2},\cdots,X\_{n})^{\top} and denote the expectation with respect to its distribution by 𝖤{\sf E}. We also define a transformation fu:ℝn→ℝnf\_{u}:\mathbb{R}^{n}\rightarrow\mathbb{R}^{n} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | fu​(𝐳)=(x1∗−u+z1x1∗−u,z2,⋯,zd)⊤,f\_{u}({\mathbf{z}})=\left(x\_{1}^{\*}-u+\frac{z\_{1}}{x\_{1}^{\*}-u},z\_{2},\cdots,z\_{d}\right)^{\top}, |  | (6) |

which maps 𝐙{\mathbf{Z}} to 𝐗{\mathbf{X}}. Finally, let

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lu​(𝐳)≔exp⁡(−z12/(2​(x1∗−u)2)−(x1∗−u)2/2)(x1∗−u)​2​π​𝟙​{z1≥0}L\_{u}({\mathbf{z}})\coloneqq\frac{\exp(-z\_{1}^{2}/(2(x\_{1}^{\*}-u)^{2})-(x\_{1}^{\*}-u)^{2}/2)}{(x\_{1}^{\*}-u)\sqrt{2\pi}}\mathds{1}\{z\_{1}\geq 0\} |  | (7) |

be the likelihood ratio associated with our importance sampling approach.
In this setup, it is easy to see that

|  |  |  |  |
| --- | --- | --- | --- |
|  | {h​(u)=𝖤​[d​(fu​(𝐙),ℰ)2​𝟙​{d​(fu​(𝐙),ℰ)≤u}​Lu​(𝐙)];p​(u)=𝖤​[𝟙​{d​(fu​(𝐙),ℰ)≤u}​Lu​(𝐙)].\left\{~\begin{aligned} h(u)&={\sf E}[d(f\_{u}({\mathbf{Z}}),{\cal E})^{2}\mathds{1}\{d(f\_{u}({\mathbf{Z}}),{\cal E})\leq u\}L\_{u}({\mathbf{Z}})];\\ p(u)&={\sf E}[\mathds{1}\{d(f\_{u}({\mathbf{Z}}),{\cal E})\leq u\}L\_{u}({\mathbf{Z}})].\end{aligned}\right. |  | (8) |

This forms unbiased estimators for h​(u)h(u) and p​(u)p(u) and enables us to develop the following estimation procedure for p∗p\_{\*}:

1. (i)

   Take NN iid copies of 𝐙{\mathbf{Z}}, denoted by {𝐙i}i=1n\{{\mathbf{Z}}\_{i}\}\_{i=1}^{n};
2. (ii)

   Let H​(⋅,u)≔d​(fu​(⋅),ℰ)2​𝟙​{d​(fu​(⋅),ℰ)≤u}​Lu​(⋅)H(\cdot,u)\coloneqq d(f\_{u}(\cdot),{\cal E})^{2}\mathds{1}\{d(f\_{u}(\cdot),{\cal E})\leq u\}L\_{u}(\cdot) for u≥0u\geq 0 and define an estimate of h​(⋅)h(\cdot) as

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | h^N​(u)=1N​∑i=1NH​(𝐙i,u)​for​u≥0;\widehat{h}\_{N}(u)=\frac{1}{N}\sum\_{i=1}^{N}H({\mathbf{Z}}\_{i},u)~~\text{for}~u\geq 0; |  | (9) |
3. (iii)

   Compute the estimate u^N≔inf{u:h^N​(u)>δ2}\widehat{u}\_{N}\coloneqq\inf\{u:\widehat{h}\_{N}(u)>\delta^{2}\} for u∗u\_{\*};
4. (iv)

   Let P​(⋅,u)≔𝟙​{d​(fu​(⋅),ℰ)≤u}​Lu​(⋅)P(\cdot,u)\coloneqq\mathds{1}\{d(f\_{u}(\cdot),{\cal E})\leq u\}L\_{u}(\cdot) and define an estimate of p​(u)p(u) as

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | p^N​(u)=1N​∑i=1NP​(𝐙i,u)​for​u≥0;\widehat{p}\_{N}(u)=\frac{1}{N}\sum\_{i=1}^{N}P({\mathbf{Z}}\_{i},u)~~\text{for}~u\geq 0; |  | (10) |
5. (v)

   Calculate the estimate of the worst-case probability p∗p\_{\*} by evaluating p^N​(u^N)\widehat{p}\_{N}(\widehat{u}\_{N}).

We refer to this method and the estimator p^N​(u^N)\widehat{p}\_{N}(\widehat{u}\_{N}) as *Distributionally Robust Importance Sampling (DRIS)* and the DRIS estimator, respectively. We detail its procedure in Algorithm [1](https://arxiv.org/html/2601.01642v1#alg1 "Algorithm 1 ‣ 4.1. DRIS Algorithm ‣ 4. Main Algorithm and Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation"). It is important to highlight that while Step (iii) involves root-finding, it requires no additional sampling costs, in contrast to typical root-finding procedures coupled with importance sampling (HeJLF2024). Moreover, the implementation of the DRIS method is computationally cheap: although it involves a root-finding procedure, the algorithm avoids costly operations elsewhere. Particularly, our sampling distributions (i.e., exponential and normal distributions) are straightforward to simulate, ensuring low sampling costs.

Algorithm 1  Distributionally Robust Importance Sampling (DRIS)

1:Input: NN, x1∗x\_{1}^{\*}, and δ\delta

2:Generate NN samples {yi}i=1N\{y\_{i}\}\_{i=1}^{N} of YY from the standard exponential distribution

3:Take NN samples {(x2,i,…,xn,i)}i=1N\{(x\_{2,i},\ldots,x\_{n,i})\}\_{i=1}^{N} of (X2,…,Xn)(X\_{2},\ldots,X\_{n}) from the (n−1)(n-1)-dimensional standard normal distribution

4:Set 𝐳i=(z1,i,…,zn,i){\mathbf{z}}\_{i}=(z\_{1,i},\ldots,z\_{n,i}) for i=1,…,Ni=1,\ldots,N, where z1,i=yiz\_{1,i}=y\_{i} and zj,i=xj,iz\_{j,i}=x\_{j,i} for j=2,…,nj=2,\ldots,n

5:Set hN​(u)=N−1​∑i=1Nd​(fu​(𝐳i),ℰ)2​𝟙​{d​(fu​(𝐳i),ℰ)≤u}​Lu​(𝐳i)h\_{N}(u)=N^{-1}\sum\_{i=1}^{N}d(f\_{u}({\mathbf{z}}\_{i}),{\cal E})^{2}\mathds{1}\{d(f\_{u}({\mathbf{z}}\_{i}),{\cal E})\leq u\}L\_{u}({\mathbf{z}}\_{i}) for any u≥0u\geq 0, where fu​(⋅)f\_{u}(\cdot) and Lu​(⋅)L\_{u}(\cdot) are defined as in ([6](https://arxiv.org/html/2601.01642v1#S4.E6 "In 4.1. DRIS Algorithm ‣ 4. Main Algorithm and Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) and ([7](https://arxiv.org/html/2601.01642v1#S4.E7 "In 4.1. DRIS Algorithm ‣ 4. Main Algorithm and Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")), respectively

6:Find uN=inf{u:hN​(u)>δ2}u\_{N}=\inf\{u:h\_{N}(u)>\delta^{2}\} via a (deterministic) root-finding procedure

7:Return: pN=N−1​∑i=1N𝟙​{d​(fuN​(𝐳i),ℰ)≤uN}​LuN​(𝐳i)p\_{N}=N^{-1}\sum\_{i=1}^{N}\mathds{1}\{d(f\_{u\_{N}}({\mathbf{z}}\_{i}),{\cal E})\leq u\_{N}\}L\_{u\_{N}}({\mathbf{z}}\_{i})

### 4.2.  Efficiency of DRIS

We now show that our proposed methodology has strong theoretical performance guarantees, satisfying the efficiency criterion in Definition [1](https://arxiv.org/html/2601.01642v1#Thmdefinition1 "Definition 1. ‣ 2. Problem Formulation ‣ Wasserstein Distributionally Robust Rare-Event Simulation"). To that end, we first characterize the central limit theorem for the DRIS estimator p^N​(u^N)\widehat{p}\_{N}(\widehat{u}\_{N}) in the following result:

###### Theorem 2 (Central Limit Theorem).

Suppose that there exist uL,uU∈(0,x1∗)u\_{L},u\_{U}\in(0,x\_{1}^{\*}) such that u∗,u^N∈[uL,uU]{u\_{\*}},\widehat{u}\_{N}\in[u\_{L},u\_{U}] for all sufficiently large NN. Then,

|  |  |  |  |
| --- | --- | --- | --- |
|  | N​(p^N​(u^N)−p∗)⇒𝒩​(0,𝖵𝖺𝗋​(P​(𝐙,u∗)−H​(𝐙,u∗)u∗2))​as​N→∞.\sqrt{N}(\widehat{p}\_{N}(\widehat{u}\_{N})-p\_{\*})\Rightarrow{\cal N}\left(0,{\sf Var}\left(P({\mathbf{Z}},{u\_{\*}})-\frac{H({\mathbf{Z}},{u\_{\*}})}{u\_{\*}^{2}}\right)\right)~~\text{as}~N\to\infty. |  | (11) |

It is straightforward to verify that the central limit theorem stated above holds in our asymptotic regime with the sequence of sets {ℰr}r>0\{{\cal E}\_{r}\}\_{r>0}. Specifically, for all r>0r>0, the DRIS estimator for prp\_{r} in ([4](https://arxiv.org/html/2601.01642v1#S3.E4 "In 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) has asymptotic variance

|  |  |  |
| --- | --- | --- |
|  | σr2≔𝖵𝖺𝗋​(𝟙​{d​(fur​(𝐙),ℰr)≤ur}​Lur​(𝐙)​(1−d​(fur​(𝐙),ℰr)2ur2)).\sigma\_{r}^{2}\coloneqq{\sf Var}\left(\mathds{1}\{d(f\_{u\_{r}}({\mathbf{Z}}),{\cal E}\_{r})\leq u\_{r}\}L\_{u\_{r}}({\mathbf{Z}})\left(1-\frac{d(f\_{u\_{r}}({\mathbf{Z}}),{\cal E}\_{r})^{2}}{u\_{r}^{2}}\right)\right). |  |

Based on this asymptotic variance, the following theorem presents the main finding of this paper: a characterization of the asymptotic efficiency of our DRIS estimator. This result demonstrates the effectiveness of using a fixed set of samples for estimating both h​(⋅)h(\cdot) and p​(⋅)p(\cdot).

###### Theorem 3 (Vanishing Relative Error).

For any δ>0\delta>0, lim supr→∞r2​(r−ur)2​σr2/pr2<∞\limsup\_{r\to\infty}r^{2}(r-u\_{r})^{2}\sigma\_{r}^{2}/p\_{r}^{2}<\infty.

Since r−ur→∞r-u\_{r}\to\infty as r→∞r\to\infty (Lemma [2](https://arxiv.org/html/2601.01642v1#Thmlemma2 "Lemma 2 (Asymptotic Behavior of 𝑢_𝑟). ‣ 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation")), the preceding theorem shows that the relative error of the DRIS estimator asymptotically changes at a rate at most r−1​(r−ur)−1r^{-1}(r-u\_{r})^{-1} as r→∞r\to\infty, implying that the DRIS estimator achieves vanishing relative error.

## 5.  Numerical Experiments

In this section, we conduct numerical experiments to validate the performance of the proposed method. To numerically compare the DRIS method with the application of existing Monte Carlo methods, we report two performance indicators for each experiment conducted below: variance ratio (VR) and efficiency ratio (ER). For a crude Monte Carlo estimator Z𝙼𝙲Z^{\tt MC} with runtime τ𝙼𝙲\tau^{\tt MC} and a target estimator ZZ with runtime τ\tau, we define VR≔𝖵𝖺𝗋​(Z𝙼𝙲)/𝖵𝖺𝗋​(Z)\text{VR}\coloneqq{\sf Var}(Z^{\tt MC})/{\sf Var}(Z) and ER≔VR×τ𝙼𝙲/τ\text{ER}\coloneqq\text{VR}\times\tau^{\tt MC}/\tau. We also report the relative error of an estimator ZZ at the 95% confidence level defined as 1.96​𝖵𝖺𝗋​(Z)/𝖤​[Z]1.96\sqrt{{\sf Var}(Z)}/{\sf E}[Z]. While ER is often considered a more comprehensive measure of efficiency, computation time is sensitive to hardware performance and implementation details; therefore, we present VR as a critical complementary metric.

### 5.1.  Experimental Setups

We use the following two examples for our numerical experiments.

A toy example. We first consider a simple two-dimensional setup where the target set is given by
ℰr={𝐱∈ℝ2:x1−5​x2≥r,x1+5​x2≥r}{\cal E}\_{r}=\{{\mathbf{x}}\in\mathbb{R}^{2}:x\_{1}-5x\_{2}\geq r,x\_{1}+5x\_{2}\geq r\}
and the radius of the 2-Wasserstein ball is set as δ=0.001\delta=0.001.
We obtain the estimates of u^N\widehat{u}\_{N} and p^N​(u^N)\widehat{p}\_{N}(\widehat{u}\_{N}) using the sample size of 10710^{7} and replicate the entire procedure for 100100 times to calculate the average runtime and variance for each algorithm. To the
best of our knowledge, there are no particular simulation methods developed to estimate Wasserstein distributionally robust rare-event probabilities. Hence, we compare the performance of the DRIS method with those of crude Monte Carlo (MC) and classical exponential twisting (ET) schemes, both of which are applied to estimate h​(⋅)h(\cdot) and p​(⋅)p(\cdot) analogously to the DRIS method in ([9](https://arxiv.org/html/2601.01642v1#S4.E9 "In item (ii) ‣ 4.1. DRIS Algorithm ‣ 4. Main Algorithm and Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) and ([10](https://arxiv.org/html/2601.01642v1#S4.E10 "In item (iv) ‣ 4.1. DRIS Algorithm ‣ 4. Main Algorithm and Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")).

Portfolio loss probabilities. We next revisit Example [1](https://arxiv.org/html/2601.01642v1#Thmexample1 "Example 1. ‣ 2. Problem Formulation ‣ Wasserstein Distributionally Robust Rare-Event Simulation") in Section [2](https://arxiv.org/html/2601.01642v1#S2 "2. Problem Formulation ‣ Wasserstein Distributionally Robust Rare-Event Simulation") to estimate portfolio loss probabilities. We construct a portfolio consisting of n=5n=5 uncorrelated underlying assets, adopting the parameter settings from Glasserman2000-var-red. Specifically, we assume 250 trading days per year, a risk-free rate of 5%, and d​t=0.04{\rm d}t=0.04. Each underlying asset has an initial value S0=100S\_{0}=100 and volatility σ=0.3\sigma=0.3. For each asset, the portfolio holds long positions in 10 at-the-money call options and 5 at-the-money put options. All options have a half-year maturity. The loss threshold ℓ\ell is set to 120 in all cases. To align with our rare-event setting, we scale the risk factor 𝐗{\mathbf{X}} by r−1r^{-1} for various values of rr.
Finally, we set δ=0.01\delta=0.01 and use the same benchmarks, sample size, and number of macroreplications as in the previous toy example.

### 5.2.  Summary of the Numerical Results

Tables [1](https://arxiv.org/html/2601.01642v1#S5.T1 "Table 1 ‣ 5.2. Summary of the Numerical Results ‣ 5. Numerical Experiments ‣ Wasserstein Distributionally Robust Rare-Event Simulation") and [2](https://arxiv.org/html/2601.01642v1#S5.T2 "Table 2 ‣ 5.2. Summary of the Numerical Results ‣ 5. Numerical Experiments ‣ Wasserstein Distributionally Robust Rare-Event Simulation") report the estimates of uru\_{r} and prp\_{r} and the runtimes of the algorithms, along with the corresponding 95% relative error, VR and ER, for the two examples described in Section [5.1](https://arxiv.org/html/2601.01642v1#S5.SS1 "5.1. Experimental Setups ‣ 5. Numerical Experiments ‣ Wasserstein Distributionally Robust Rare-Event Simulation").
In all cases we consider, our proposed method completely dominates the two benchmarks, demonstrating greater variance reduction and higher efficiency. This significant performance gap between DRIS and the other two methods, which widens as rr increases, validates our theoretical results. Although ET performs competitively in our numerical experiments, its performance in these problems lacks theoretical justification, and more importantly, DRIS consistently yields superior results. The increased runtimes for ET and DRIS, compared to MC, arise because the root-finding procedure embedded in these algorithms requires transforming samples and solving the distance dependent on the evaluated uu; in contrast, samples in the crude Monte Carlo algorithm remain unchanged.

Table 1: Numerical results for the toy example in Section [5.1](https://arxiv.org/html/2601.01642v1#S5.SS1 "5.1. Experimental Setups ‣ 5. Numerical Experiments ‣ Wasserstein Distributionally Robust Rare-Event Simulation")

| Method | rr | uru\_{r} (95% rel. err.) | prp\_{r} (95% rel. err.) | Time (sec) | VR | ER |
| --- | --- | --- | --- | --- | --- | --- |
| MC | 22 | 0.00270.0027 (1.62%1.62\%) | 2.40×10−32.40\times 10^{-3} (1.13%1.13\%) | 1111 | – | – |
| 33 | 0.01410.0141 (3.29%3.29\%) | 2.39×10−42.39\times 10^{-4} (2.97%2.97\%) | 1212 | – | – |
| 44 | 0.09310.0931 (8.11%8.11\%) | 2.36×10−52.36\times 10^{-5} (7.80%7.80\%) | 1212 | – | – |
| 55 | 0.52450.5245 (12.43%12.43\%) | 3.10×10−63.10\times 10^{-6} (19.91%19.91\%) | 13 | – | – |
| ET | 22 | 0.00270.0027 (0.42%0.42\%) | 2.40×10−32.40\times 10^{-3} (0.29%0.29\%) | 144144 | 1616 | 1.31.3 |
| 33 | 0.01470.0147 (0.30%0.30\%) | 2.40×10−42.40\times 10^{-4} (0.27%0.27\%) | 151151 | 125125 | 9.89.8 |
| 44 | 0.09650.0965 (0.18%0.18\%) | 2.31×10−52.31\times 10^{-5} (0.15%0.15\%) | 144144 | 2,6002,600 | 225225 |
| 55 | 0.51630.5163 (0.08%0.08\%) | 3.08×10−63.08\times 10^{-6} (0.07%0.07\%) | 112112 | 78,03678,036 | 9,1079,107 |
| DRIS | 22 | 0.00270.0027 (0.24%0.24\%) | 2.41×10−32.41\times 10^{-3} (0.16%0.16\%) | 149149 | 4848 | 3.73.7 |
| 33 | 0.01460.0146 (0.15%0.15\%) | 2.40×10−42.40\times 10^{-4} (0.13%0.13\%) | 148148 | 559559 | 4545 |
| 44 | 0.09650.0965 (0.08%0.08\%) | 2.31×10−52.31\times 10^{-5} (0.08%0.08\%) | 163163 | 10,10810,108 | 772772 |
| 55 | 0.51620.5162 (0.04%0.04\%) | 3.08×10−63.08\times 10^{-6} (0.04%) | 116116 | 220,943220,943 | 24,97824,978 |




Table 2: Numerical results for estimating portfolio loss probabilities in Example [1](https://arxiv.org/html/2601.01642v1#Thmexample1 "Example 1. ‣ 2. Problem Formulation ‣ Wasserstein Distributionally Robust Rare-Event Simulation")

| Method | rr | uru\_{r} (95% rel. err.) | prp\_{r} (95% rel. err.) | Time (sec) | VR | ER |
| --- | --- | --- | --- | --- | --- | --- |
| MC | 22 | 1.421.42 (1.865%1.865\%) | 1.05×10−41.05\times 10^{-4} (2.499%2.499\%) | 77 | – | – |
| 33 | 8.468.46 (2.278%2.278\%) | 1.37×10−51.37\times 10^{-5} (3.482%3.482\%) | 77 | – | – |
| 44 | 24.5024.50 (2.512%2.512\%) | 4.40×10−64.40\times 10^{-6} (3.362%3.362\%) | 77 | – | – |
| ET | 22 | 1.401.40 (0.056%0.056\%) | 1.05×10−41.05\times 10^{-4} (0.042%0.042\%) | 4848 | 3,6153,615 | 526526 |
| 33 | 8.608.60 (0.023%0.023\%) | 1.35×10−51.35\times 10^{-5} (0.016%0.016\%) | 5050 | 48,12048,120 | 6,6206,620 |
| 44 | 24.7324.73 (0.013%0.013\%) | 4.39×10−64.39\times 10^{-6} (0.009%0.009\%) | 5151 | 145,230145,230 | 19,18219,182 |
| DRIS | 22 | 1.401.40 (0.024%0.024\%) | 1.05×10−41.05\times 10^{-4} (0.034%0.034\%) | 5353 | 5,2695,269 | 691691 |
| 33 | 8.608.60 (0.009%0.009\%) | 1.35×10−51.35\times 10^{-5} (0.013%0.013\%) | 5454 | 71,80671,806 | 9,2129,212 |
| 44 | 24.7324.73 (0.004%0.004\%) | 4.39×10−64.39\times 10^{-6} (0.007%0.007\%) | 5151 | 227,647227,647 | 30,14330,143 |

## 6.  Concluding Remarks

In this paper, we address the problem of efficiently estimating rare-event probabilities under distributional model risk. Leveraging strong duality results in Wasserstein distributionally robust optimization, we formulate a novel, computationally tractable importance sampling procedure called DRIS, which yields significant variance reduction in estimating the said probabilities. We rigorously prove that the proposed DRIS estimator achieves vanishing relative error, which is regarded as the strongest notion of efficiency in the context of rare-event simulation. All our numerical experiments support these theoretical findings.

As the first methodological framework specifically designed to estimate rare-event probabilities under distributional uncertainty, our proposed approach relies on specific modeling assumptions that suggest several interesting avenues for future research. Firstly, we focus on convex sets as target events, motivated by several examples in the relevant literature. Nevertheless, extending our methodology to non-convex target sets, while challenging, would substantially expand its practical applicability. Secondly, we restrict our focus to the case with Gaussian nominal distributions. While the framework extends to other elliptical nominal distributions as alluded to earlier, the theoretical performance in those cases remains to be verified. It would also be interesting to explore the cases with non-elliptical nominal distributions. Lastly, to ensure the tractability of our theoretical analysis, we use the 2-Wasserstein ball to define the distributional uncertainty set. Relaxing this constraint would be a promising direction, as the duality result in Lemma [1](https://arxiv.org/html/2601.01642v1#Thmlemma1 "Lemma 1 (Theorem 2 of Blanchet2019-DRO). ‣ 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation") generalizes to a broader class of uncertainty sets, including pp-Wasserstein balls with p≥1p\geq 1.

## Appendix A Proofs of the Theoretical Results

###### Proof of Lemma [2](https://arxiv.org/html/2601.01642v1#Thmlemma2 "Lemma 2 (Asymptotic Behavior of 𝑢_𝑟). ‣ 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation")..

Fix K>M>0K>M>0. Assume by contradiction that ur≥r−Mu\_{r}\geq r-M for some r>Mr>M. Then, we observe that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | δ2r2=hr​(ur)r2\displaystyle\frac{\delta^{2}}{r^{2}}=\frac{h\_{r}(u\_{r})}{r^{2}} | ≥𝖤[d​(𝐗,ℰr)2r2;d(𝐗,ℰr)≤r−M,∥𝐗∥≤K].\displaystyle\geq{\sf E}\left[\frac{d({\mathbf{X}},{\cal E}\_{r})^{2}}{r^{2}};d({\mathbf{X}},{\cal E}\_{r})\leq r-M,\|{\mathbf{X}}\|\leq K\right]. |  | (12) |

Since d​(⋅,ℰr)d(\cdot,{\cal E}\_{r}) is 11-Lipschitz, we have d​(𝐱,ℰr)≥d​(𝟎,ℰr)−‖𝐱‖≥r−Kd({\mathbf{x}},{\cal E}\_{r})\geq d(\mathbf{0},{\cal E}\_{r})-\|{\mathbf{x}}\|\geq r-K for any 𝐱{\mathbf{x}} satisfying ‖𝐱‖≤K\|{\mathbf{x}}\|\leq K.
This implies that lim infr→∞d​(𝐱,ℰr)2/r2=1\liminf\_{r\to\infty}{d({\mathbf{x}},{\cal E}\_{r})^{2}}/{r^{2}}=1.

Fix 𝐱∈ℝn{\mathbf{x}}\in\mathbb{R}^{n} such that x1>Mx\_{1}>M. Then,
by letting tr≔(‖𝐱‖2−M2)/(2​r​x1−2​r​M)>0t\_{r}\coloneqq{(\|{\mathbf{x}}\|^{2}-M^{2})}/{(2rx\_{1}-2rM)}>0, a straightforward calculation yields
‖𝐱−r​tr​𝐞1‖=r​tr−M\|{\mathbf{x}}-rt\_{r}{\mathbf{e}}\_{1}\|=rt\_{r}-M.
Thus, since d​(⋅,ℰr)d(\cdot,{\cal E}\_{r}) is 11-Lipschitz, we have
d​(𝐱,ℰr)≤d​(r​tr​𝐞1,ℰr)+‖𝐱−r​tr​𝐞1‖=r−r​tr+r​tr−M=r−Md({\mathbf{x}},{\cal E}\_{r})\leq d(rt\_{r}{\mathbf{e}}\_{1},{\cal E}\_{r})+\|{\mathbf{x}}-rt\_{r}{\mathbf{e}}\_{1}\|=r-rt\_{r}+rt\_{r}-M=r-M for all sufficiently large rr such that tr∈(0,1)t\_{r}\in(0,1).
Accordingly, by applying Fatou’s lemma on ([12](https://arxiv.org/html/2601.01642v1#A1.E12 "In Proof of Lemma 2.. ‣ Appendix A Proofs of the Theoretical Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")), we obtain

|  |  |  |
| --- | --- | --- |
|  | lim infr→∞δ2r2≥𝖤0[lim infr→∞d​(𝐗,ℰr)2r2;d(𝐗,ℰr)≤r−M,∥𝐗∥≤K]≥𝖯(X1>M,∥𝐗∥≤K)>0.\liminf\_{r\to\infty}\frac{\delta^{2}}{r^{2}}\geq{\sf E}\_{0}\left[\liminf\_{r\to\infty}\frac{d({\mathbf{X}},{\cal E}\_{r})^{2}}{r^{2}};d({\mathbf{X}},{\cal E}\_{r})\leq r-M,\|{\mathbf{X}}\|\leq K\right]\geq{\sf P}(X\_{1}>M,\|{\mathbf{X}}\|\leq K)>0. |  |

This contradicts the fact that δ\delta is a constant. Therefore, ur<r−Mu\_{r}<r-M for all sufficiently large rr.

Furthermore, it is straightforward that pr=𝖯​(d​(𝐗,ℰr)≤ur)≤𝖯​(X1≥r−ur)=Φ¯​(r−ur)p\_{r}={\sf P}(d({\mathbf{X}},{\cal E}\_{r})\leq u\_{r})\leq{\sf P}(X\_{1}\geq r-u\_{r})=\bar{\Phi}(r-u\_{r}). Hence, we get δ2=hr​(ur)=𝖤​[d​(𝐗,ℰr)2;d​(𝐗,ℰr)≤ur]≤ur2​pr≤r2​Φ¯​(r−ur)\delta^{2}=h\_{r}(u\_{r})={\sf E}[d({\mathbf{X}},{\cal E}\_{r})^{2};d({\mathbf{X}},{\cal E}\_{r})\leq u\_{r}]\leq u\_{r}^{2}p\_{r}\leq r^{2}\bar{\Phi}(r-u\_{r}) for all sufficiently large rr. Consequently, the result follows. ∎

###### Proof of Theorem [1](https://arxiv.org/html/2601.01642v1#Thmtheorem1 "Theorem 1 (Asymptotic Behavior of 𝑝_𝑟). ‣ 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation")..

By the asymptotic behavior of the Mills ratio for a standard normal distribution, we have 2​π​x​Φ¯​(x)/exp⁡(−x2/2)→1\sqrt{2\pi}x\bar{\Phi}(x)/\exp(-x^{2}/2)\to 1 as x→∞x\to\infty (see, e.g., Bartoszynski2021). This implies that x2​Φ¯​(x)→0x^{2}\bar{\Phi}(x)\to 0 as x→∞x\to\infty. Thus, by letting x=Φ¯−1​(δ2/r2)x=\bar{\Phi}^{-1}(\delta^{2}/r^{2}), we have r−1​Φ¯−1​(δ2/r2)→0r^{-1}\bar{\Phi}^{-1}(\delta^{2}/r^{2})\to 0 as rr grows. Then, dividing both sides of ([5](https://arxiv.org/html/2601.01642v1#S3.E5 "In Lemma 2 (Asymptotic Behavior of 𝑢_𝑟). ‣ 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) by rr and letting r→∞r\to\infty yields limr→∞ur/r=1\lim\_{r\to\infty}u\_{r}/r=1.
Furthermore, we observe that

|  |  |  |
| --- | --- | --- |
|  | hr​(ur)=𝖤0​[d​(𝐗,ℰr)2;d​(𝐗,ℰr)≤ur]≤ur2​𝖯0​(d​(𝐗,ℰr)≤ur)=ur2​pr.h\_{r}(u\_{r})={\sf E}\_{0}[d({\mathbf{X}},{\cal E}\_{r})^{2};d({\mathbf{X}},{\cal E}\_{r})\leq u\_{r}]\leq u\_{r}^{2}{\sf P}\_{0}(d({\mathbf{X}},{\cal E}\_{r})\leq u\_{r})=u\_{r}^{2}p\_{r}. |  |

Consequently, lim infr→∞r2​pr≥δ2/limr→∞(ur/r)2=δ2\liminf\_{r\to\infty}r^{2}p\_{r}\geq\delta^{2}/\lim\_{r\to\infty}(u\_{r}/r)^{2}=\delta^{2}.
∎

###### Proof of Theorem [2](https://arxiv.org/html/2601.01642v1#Thmtheorem2 "Theorem 2 (Central Limit Theorem). ‣ 4.2. Efficiency of DRIS ‣ 4. Main Algorithm and Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")..

We prove the statement in four steps. In this proof, we denote by ∥⋅∥2\|\cdot\|\_{2} the L2L^{2} norm under the sampling distribution, i.e., ‖A‖2=𝖤​[A​(𝐙)2]\|A\|\_{2}=\sqrt{{\sf E}[A({\mathbf{Z}})^{2}]} for any function A:ℝn→ℝA:\mathbb{R}^{n}\to\mathbb{R}.

*Step 1: Uniform Convergence of h^N\widehat{h}\_{N}.*
In this step, we aim to prove the uniform convergence of h^N\widehat{h}\_{N} in ([9](https://arxiv.org/html/2601.01642v1#S4.E9 "In item (ii) ‣ 4.1. DRIS Algorithm ‣ 4. Main Algorithm and Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) over Θ≔[uL,uU]\Theta\coloneqq[u\_{L},u\_{U}].
Since every Donsker class satisfies the uniform law of large numbers (van1996weak, page 130), it suffices to show that ℋ≔{H​(⋅,u):u∈Θ}{\cal H}\coloneqq\{H(\cdot,u):u\in\Theta\} is Donsker.

We define two function classes ℋ1{\cal H}\_{1} and ℋ2{\cal H}\_{2} as ℋ1≔{𝐳↦(d​(fu​(𝐳),ℰ)∧uU)2​Lu​(𝐳):u∈Θ}{\cal H}\_{1}\coloneqq\{{\mathbf{z}}\mapsto\left(d(f\_{u}({\mathbf{z}}),{\cal E})\wedge u\_{U}\right)^{2}L\_{u}({\mathbf{z}}):u\in\Theta\} and ℋ2≔{𝐳↦𝟙​{d​(fu​(𝐳),ℰ)≤u}:u∈Θ}{\cal H}\_{2}\coloneqq\{{\mathbf{z}}\mapsto\mathds{1}\{d(f\_{u}({\mathbf{z}}),{\cal E})\leq u\}:u\in\Theta\}. We observe that for any u,v∈Θu,v\in\Theta,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | |(d​(fu​(𝐳),ℰ)∧uU)2​Lu​(𝐳)−(d​(fv​(𝐳),ℰ)∧uU)2​Lv​(𝐳)|\displaystyle\left|\left(d(f\_{u}({\mathbf{z}}),{\cal E})\wedge u\_{U}\right)^{2}L\_{u}({\mathbf{z}})-\left(d(f\_{v}({\mathbf{z}}),{\cal E})\wedge u\_{U}\right)^{2}L\_{v}({\mathbf{z}})\right| |  | (13) |
|  |  | ≤(d​(fu​(𝐳),ℰ)∧uU)2​|Lu​(𝐳)−Lv​(𝐳)|+|Lv​(𝐳)|​|(d​(fu​(𝐳),ℰ)∧uU)2−(d​(fv​(𝐳),ℰ)∧uU)2|\displaystyle\leq\left(d(f\_{u}({\mathbf{z}}),{\cal E})\wedge u\_{U}\right)^{2}\left|L\_{u}({\mathbf{z}})-L\_{v}({\mathbf{z}})\right|+|L\_{v}({\mathbf{z}})|\left|\left(d(f\_{u}({\mathbf{z}}),{\cal E})\wedge u\_{U}\right)^{2}-\left(d(f\_{v}({\mathbf{z}}),{\cal E})\wedge u\_{U}\right)^{2}\right| |  |
|  |  | ≤uU2​|Lu​(𝐳)−Lv​(𝐳)|+L¯​|(d​(fu​(𝐳),ℰ)∧uU)2−(d​(fv​(𝐳),ℰ)∧uU)2|\displaystyle\leq u\_{U}^{2}\left|L\_{u}({\mathbf{z}})-L\_{v}({\mathbf{z}})\right|+\bar{L}\left|\left(d(f\_{u}({\mathbf{z}}),{\cal E})\wedge u\_{U}\right)^{2}-\left(d(f\_{v}({\mathbf{z}}),{\cal E})\wedge u\_{U}\right)^{2}\right| |  |
|  |  | ≤uU2​|Lu​(𝐳)−Lv​(𝐳)|+2​uU​L¯​‖fu​(𝐳)−fv​(𝐳)‖,\displaystyle\leq u\_{U}^{2}\left|L\_{u}({\mathbf{z}})-L\_{v}({\mathbf{z}})\right|+2u\_{U}\bar{L}\left\|f\_{u}({\mathbf{z}})-f\_{v}({\mathbf{z}})\right\|, |  |

where the first inequality follows from the triangular inequality, the second inequality holds since L¯≔sup𝐳∈ℝn,u∈ΘLu​(𝐳)<∞\bar{L}\coloneqq\sup\_{{\mathbf{z}}\in\mathbb{R}^{n},u\in\Theta}L\_{u}({\mathbf{z}})<\infty, and the last one is straightforward because |a2−b2|≤2​c​|a−b||a^{2}-b^{2}|\leq 2c|a-b| for a,b∈[0,c]a,b\in[0,c] and c≥0c\geq 0, and d​(⋅,ℰ)d(\cdot,{\cal E}) is 11-Lipschitz. It can be easily checked that there exists a polynomial function GG satisfying uU2​|Lu​(𝐳)−Lv​(𝐳)|+2​uU​L¯​‖fu​(𝐳)−fv​(𝐳)‖≤G​(𝐳)​|u−v|u\_{U}^{2}\left|L\_{u}({\mathbf{z}})-L\_{v}({\mathbf{z}})\right|+2u\_{U}\bar{L}\left\|f\_{u}({\mathbf{z}})-f\_{v}({\mathbf{z}})\right\|\leq G({\mathbf{z}})|u-v| for all 𝐳∈ℝn{\mathbf{z}}\in\mathbb{R}^{n} and u,v∈Θu,v\in\Theta. Since ‖G‖2<∞\|G\|\_{2}<\infty and Θ\Theta is compact, ℋ1{\cal H}\_{1} is Donsker by Theorems 2.7.17 and 2.5.6 of van1996weak.

Given a collection 𝒞{\cal C} of sets, its VC-dimension, denoted by V​(𝒞)V({\cal C}), is the cardinality of the largest set XX such that |{X∩C:C∈𝒞}|=2|X|\left|\{X\cap C:C\in{\cal C}\}\right|=2^{|X|}. A function class ℱ{\cal F} is called a VC-class if the collection of all subgraphs
{{(𝐳,t):t<f​(𝐳)}:f∈ℱ}\{\{({\mathbf{z}},t):t<f({\mathbf{z}})\}:f\in{\cal F}\} has a finite VC-dimension.
Suppose that |{{(𝐳1,t1),…,(𝐳m,tm)}∩{(𝐳,t):t<𝟙​{d​(fu​(𝐳),ℰ)≤u}}:u∈Θ}|=2m|\{\{({\mathbf{z}}\_{1},t\_{1}),\dots,({\mathbf{z}}\_{m},t\_{m})\}\cap\{({\mathbf{z}},t):t<\mathds{1}\{d(f\_{u}({\mathbf{z}}),{\cal E})\leq u\}\}:u\in\Theta\}|=2^{m} for some mm points (𝐳1,t1),…,(𝐳m,tm)∈(0,∞)×ℝn−1×ℝ({\mathbf{z}}\_{1},t\_{1}),\dots,({\mathbf{z}}\_{m},t\_{m})\in(0,\infty)\times\mathbb{R}^{n-1}\times\mathbb{R}. Since the condition t<𝟙​{d​(fu​(𝐳),ℰ)≤u}t<\mathds{1}\{d(f\_{u}({\mathbf{z}}),{\cal E})\leq u\} is nontrivial only when t∈[0,1)t\in[0,1), we may choose t1=⋯=tm=0t\_{1}=\cdots=t\_{m}=0 without loss of generality. In this case, the shattering condition on subgraphs is equivalent to shattering the points 𝐳1,…,𝐳m{\mathbf{z}}\_{1},\dots,{\mathbf{z}}\_{m} directly using the function values, i.e., |{(𝟙​{d​(fu​(𝐳1),ℰ)≤u},…,𝟙​{d​(fu​(𝐳m),ℰ)≤u}):u∈Θ}|=2m\left|\{(\mathds{1}\{d(f\_{u}({\mathbf{z}}\_{1}),{\cal E})\leq u\},\ldots,\mathds{1}\{d(f\_{u}({\mathbf{z}}\_{m}),{\cal E})\leq u\}):u\in\Theta\}\right|=2^{m}.

On the other hand, by Lemma [3](https://arxiv.org/html/2601.01642v1#Thmlemma3 "Lemma 3. ‣ Appendix B Technical Lemmas ‣ Wasserstein Distributionally Robust Rare-Event Simulation") in Appendix [B](https://arxiv.org/html/2601.01642v1#A2 "Appendix B Technical Lemmas ‣ Wasserstein Distributionally Robust Rare-Event Simulation"), the set {u∈Θ:d​(fu​(𝐳i),ℰ)≤u}\{u\in\Theta:d(f\_{u}({\mathbf{z}}\_{i}),{\cal E})\leq u\} is defined by at most 2 boundary points in Θ\Theta. Hence, there exist at most 2​m2m points in Θ\Theta, denoted by u1,u2,…,u2​mu\_{1},u\_{2},\ldots,u\_{2m}, such that uL=u0≤u1≤⋯≤u2​m≤u2​m+1=uUu\_{L}=u\_{0}\leq u\_{1}\leq\cdots\leq u\_{2m}\leq u\_{2m+1}=u\_{U} and the vector (𝟙​{d​(fu​(𝐳1),ℰ)2≤u},…,𝟙​{d​(fu​(𝐳m),ℰ)2≤u})(\mathds{1}\{d(f\_{u}({\mathbf{z}}\_{1}),{\cal E})^{2}\leq u\},\ldots,\mathds{1}\{d(f\_{u}({\mathbf{z}}\_{m}),{\cal E})^{2}\leq u\}) remains constant for any u∈(ui,ui+1)u\in(u\_{i},u\_{i+1}) with i=0,…,2​mi=0,\ldots,2m. Thus, |{(𝟙​{d​(fu​(𝐳1),ℰ)≤u},…,𝟙​{d​(fu​(𝐳m),ℰ)≤u}):u∈Θ}|≤2​m+1\left|\{(\mathds{1}\{d(f\_{u}({\mathbf{z}}\_{1}),{\cal E})\leq u\},\ldots,\mathds{1}\{d(f\_{u}({\mathbf{z}}\_{m}),{\cal E})\leq u\}):u\in\Theta\}\right|\leq 2m+1. Combining this with the above shattering condition leads to 2m≤2​m+12^{m}\leq 2m+1. Therefore, mm must be finite, proving that ℋ2{\cal H}\_{2} is a VC-class. Furthermore, ℋ2{\cal H}\_{2} is uniformly bounded by 11. Consequently, Theorems 2.6.7 and 2.5.2 of van1996weak imply that ℋ2{\cal H}\_{2} is Donsker.

Let ϕ​(x,y)=x​y\phi(x,y)=xy for all x,y∈ℝx,y\in\mathbb{R}. Since ℋ1{\cal H}\_{1} and ℋ2{\cal H}\_{2} are uniformly bounded and Donsker and ℋ⊂ϕ∘(ℋ1,ℋ2)≔{𝐳↦ϕ​(g1​(𝐳),g2​(𝐳)):g1∈ℋ1,g2∈ℋ2}{\cal H}\subset\phi\circ({\cal H}\_{1},{\cal H}\_{2})\coloneqq\{{\mathbf{z}}\mapsto\phi(g\_{1}({\mathbf{z}}),g\_{2}({\mathbf{z}})):g\_{1}\in{\cal H}\_{1},g\_{2}\in{\cal H}\_{2}\}, ℋ{\cal H} is also Donsker by Corollary 2.10.15 and Theorem 2.10.1 of van1996weak.

*Step 2. Convergence of u^N\widehat{u}\_{N}.* Since h​(⋅)h(\cdot) is a strictly increasing function satisfying h​(u∗)=δ2h(u\_{\*})=\delta^{2}, we have c​(ε)≔inf|u−u∗|>ε|h​(u)−δ2|/2>0c(\varepsilon)\coloneqq\inf\_{|u-{u\_{\*}}|>\varepsilon}|h(u)-\delta^{2}|/2>0 for any ε>0\varepsilon>0. Fix ε>0\varepsilon>0. If supu∈Θ|h​(u)−h^N​(u)|≤c​(ε)\sup\_{u\in\Theta}|h(u)-\widehat{h}\_{N}(u)|\leq c(\varepsilon), then |h​(u^N)−δ2|≤max⁡{limu↑u^N|h​(u)−h^N​(u)|,limu↓u^N|h​(u)−h^N​(u)|}≤c​(ε)|h(\widehat{u}\_{N})-\delta^{2}|\leq\max\{\lim\_{u\uparrow\widehat{u}\_{N}}|h(u)-\widehat{h}\_{N}(u)|,\lim\_{u\downarrow\widehat{u}\_{N}}|h(u)-\widehat{h}\_{N}(u)|\}\leq c(\varepsilon),
which implies that |u^N−u∗|≤ε|\widehat{u}\_{N}-{u\_{\*}}|\leq\varepsilon. Accordingly,
𝖯​(supu∈Θ|h​(u)−h^N​(u)|≤c​(ε))≤𝖯​(|u^N−u∗|≤ε){\sf P}(\sup\_{u\in\Theta}|h(u)-\widehat{h}\_{N}(u)|\leq c(\varepsilon))\leq{\sf P}(|\widehat{u}\_{N}-{u\_{\*}}|\leq\varepsilon). By the uniform convergence of h^N\widehat{h}\_{N} in Step 1, limN→∞𝖯​(supu∈Θ|h​(u)−h^N​(u)|≤c​(ε))=1\lim\_{N\to\infty}{\sf P}(\sup\_{u\in\Theta}|h(u)-\widehat{h}\_{N}(u)|\leq c(\varepsilon))=1.
Hence, u^N→u∗\widehat{u}\_{N}\rightarrow{u\_{\*}} in probability as N→∞N\to\infty.

*Step 3. Asymptotic Normality for u^N\widehat{u}\_{N}.*
We define H1​(𝐳,u)=(d​(fu​(𝐳),ℰ)∧uU)2​Lu​(𝐳)H\_{1}({\mathbf{z}},u)=(d(f\_{u}({\mathbf{z}}),{\cal E})\wedge u\_{U})^{2}L\_{u}({\mathbf{z}}) and H2​(𝐳,u)=𝟙​{d​(fu​(𝐳),ℰ)≤u}H\_{2}({\mathbf{z}},u)=\mathds{1}\{d(f\_{u}({\mathbf{z}}),{\cal E})\leq u\}, implying that
H​(𝐳,u)=H1​(𝐳,u)​H2​(𝐳,u)H({\mathbf{z}},u)=H\_{1}({\mathbf{z}},u)H\_{2}({\mathbf{z}},u) for 𝐳∈(0,∞)×ℝn−1{\mathbf{z}}\in(0,\infty)\times\mathbb{R}^{n-1} and u∈Θu\in\Theta.
We observe that d​(fu∗​(𝐳),ℰ)=u∗d(f\_{{u\_{\*}}}({\mathbf{z}}),{\cal E})={u\_{\*}} if and only if fu∗​(𝐳)f\_{{u\_{\*}}}({\mathbf{z}}) lies on the boundary of {𝐳:d​(𝐳,ℰ)≤u∗}\{{\mathbf{z}}:d({\mathbf{z}},{\cal E})\leq{u\_{\*}}\}. Additionally, since fu∗f\_{{u\_{\*}}} is an invertible affine transformation, it can be checked that 𝖯​(d​(fu∗​(𝐙),ℰ)=u∗)=0{\sf P}(d(f\_{{u\_{\*}}}({\mathbf{Z}}),{\cal E})={u\_{\*}})=0.

Fix ω\omega in the sample space such that d​(fu∗​(𝐙​(ω)),ℰ)≠u∗d(f\_{{u\_{\*}}}({\mathbf{Z}}(\omega)),{\cal E})\neq{u\_{\*}}. Then, since u↦d​(fu​(𝐙​(ω)),ℰ)−uu\mapsto d(f\_{u}({\mathbf{Z}}(\omega)),{\cal E})-u is continuous, there exists δ>0\delta>0 such that H2​(𝐙​(ω),u)=H2​(𝐙​(ω),u∗)H\_{2}({\mathbf{Z}}(\omega),u)=H\_{2}({\mathbf{Z}}(\omega),{u\_{\*}}) for any |u−u∗|<δ|u-{u\_{\*}}|<\delta. Therefore, H2​(𝐙,u)→H2​(𝐙,u∗)H\_{2}({\mathbf{Z}},u)\to H\_{2}({\mathbf{Z}},{u\_{\*}}) almost surely as u→u∗u\rightarrow{u\_{\*}}.
Thus, by the continuity of H1​(𝐳,⋅)H\_{1}({\mathbf{z}},\cdot) and the continuous mapping theorem, ‖H​(⋅,u)−H​(⋅,u∗)‖22=‖H1​(⋅,u)​H2​(⋅,u)−H1​(⋅,u∗)​H2​(⋅,u∗)‖22→0\|H(\cdot,u)-H(\cdot,{u\_{\*}})\|\_{2}^{2}=\|H\_{1}(\cdot,u)H\_{2}(\cdot,u)-H\_{1}(\cdot,{u\_{\*}})H\_{2}(\cdot,{u\_{\*}})\|\_{2}^{2}\to 0
as u→u∗u\rightarrow{u\_{\*}}.
We also note that {H​(⋅,u)−H​(⋅,u∗):|u−u∗|<δ,u∈Θ}\{H(\cdot,u)-H(\cdot,{u\_{\*}}):|u-{u\_{\*}}|<\delta,u\in\Theta\} is Donsker for some δ>0\delta>0 since ℋ{\cal H} is Donsker and by Theorem 2.10.8 of van1996weak.

Let ΨN​(u)≔h^N​(u)−δ2\Psi\_{N}(u)\coloneqq\widehat{h}\_{N}(u)-\delta^{2} and Ψ​(u)≔h​(u)−δ2\Psi(u)\coloneqq h(u)-\delta^{2}. Then, by the central limit theorem, we have
N​(ΨN−Ψ)​(u∗)=N−1/2​∑i=1N(H​(𝐙i,u∗)−𝖤​[H​(𝐙,u∗)])⇒𝒩​(0,𝖵𝖺𝗋​(H​(𝐙,u∗))).\sqrt{N}(\Psi\_{N}-\Psi)({u\_{\*}})=N^{-1/2}\sum\_{i=1}^{N}(H({\mathbf{Z}}\_{i},{u\_{\*}})-{\sf E}[H({\mathbf{Z}},{u\_{\*}})])\Rightarrow{\cal N}(0,{\sf Var}(H({\mathbf{Z}},{u\_{\*}}))). Furthermore, Ψ′​(u∗)=h′​(u∗)≠0\Psi^{\prime}({u\_{\*}})=h^{\prime}({u\_{\*}})\neq 0 by Lemma [4](https://arxiv.org/html/2601.01642v1#Thmlemma4 "Lemma 4. ‣ Appendix B Technical Lemmas ‣ Wasserstein Distributionally Robust Rare-Event Simulation") in Appendix [B](https://arxiv.org/html/2601.01642v1#A2 "Appendix B Technical Lemmas ‣ Wasserstein Distributionally Robust Rare-Event Simulation"). Moreover, since H​(𝐳,u)H({\mathbf{z}},u) is uniformly bounded, it can be verified that ΨN​(u^N)=oP​(N−1/2)\Psi\_{N}(\widehat{u}\_{N})=o\_{P}(N^{-1/2}) using the definition of u^N\widehat{u}\_{N} and 𝐙i{\mathbf{Z}}\_{i} is continuously distributed. Combining all these results with Lemma 3.3.5 and Theorem 3.3.1 of van1996weak, we conclude that N​h′​(u∗)​(u^N−u∗)=−N​(h^N−h)​(u∗)+oP​(1)\sqrt{N}h^{\prime}({u\_{\*}})(\widehat{u}\_{N}-{u\_{\*}})=-\sqrt{N}(\widehat{h}\_{N}-h)({u\_{\*}})+o\_{P}(1).

*Step 4. Asymptotic Normality for the Estimator.* Using the same arguments as in Steps 1 to 3, it can be shown that {P​(⋅,u)−P​(⋅,u∗):|u−u∗|<δ,u∈Θ}\{P(\cdot,u)-P(\cdot,{u\_{\*}}):|u-{u\_{\*}}|<\delta,u\in\Theta\} is Donsker for some δ>0\delta>0, and ‖P​(⋅,u)−P​(⋅,u∗)‖22→0\|P(\cdot,u)-P(\cdot,{u\_{\*}})\|\_{2}^{2}\rightarrow 0 as u→u∗u\rightarrow{u\_{\*}}. Thus, by using Lemma 3.3.5 of van1996weak again, we have N​(p^N​(u^N)−p​(u^N))=N​(p^N​(u∗)−p​(u∗))+oP​(1)\sqrt{N}\left(\widehat{p}\_{N}(\widehat{u}\_{N})-p(\widehat{u}\_{N})\right)=\sqrt{N}\left(\widehat{p}\_{N}({u\_{\*}})-p({u\_{\*}})\right)+o\_{P}(1).
Since p​(⋅)p(\cdot) is differentiable at u∗{u\_{\*}}, the Taylor expansion implies that N​(p​(u^N)−p​(u∗))=N​p′​(u∗)​(u^N−u∗)+oP​(N​|u^N−u∗|)\sqrt{N}(p(\widehat{u}\_{N})-p({u\_{\*}}))=\sqrt{N}p^{\prime}({u\_{\*}})(\widehat{u}\_{N}-{u\_{\*}})+o\_{P}(\sqrt{N}|\widehat{u}\_{N}-{u\_{\*}}|).
Combining these findings with the result of Step 3 and Lemma [4](https://arxiv.org/html/2601.01642v1#Thmlemma4 "Lemma 4. ‣ Appendix B Technical Lemmas ‣ Wasserstein Distributionally Robust Rare-Event Simulation") in Appendix [B](https://arxiv.org/html/2601.01642v1#A2 "Appendix B Technical Lemmas ‣ Wasserstein Distributionally Robust Rare-Event Simulation"), we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | N​(p^N​(u^N)−p​(u∗))\displaystyle\sqrt{N}(\widehat{p}\_{N}(\widehat{u}\_{N})-p({u\_{\*}})) | =N​(p^N−p)​(u∗)+N​p′​(u∗)​(u^N−u∗)+oP​(N​|u^N−u∗|)+oP​(1)\displaystyle=\sqrt{N}(\widehat{p}\_{N}-p)({u\_{\*}})+\sqrt{N}p^{\prime}({u\_{\*}})(\widehat{u}\_{N}-{u\_{\*}})+o\_{P}(\sqrt{N}|\widehat{u}\_{N}-{u\_{\*}}|)+o\_{P}(1) |  | (14) |
|  |  | =N​(p^N−p)​(u∗)−Nu∗2​(h^N−h)​(u∗)+oP​(1),\displaystyle=\sqrt{N}(\widehat{p}\_{N}-p)({u\_{\*}})-\frac{\sqrt{N}}{u\_{\*}^{2}}(\widehat{h}\_{N}-h)({u\_{\*}})+o\_{P}(1), |  |

where the last equality holds since N​(u^N−u∗)\sqrt{N}(\widehat{u}\_{N}-{u\_{\*}}) is bounded in probability by Step 3. Hence, by the central limit theorem and Slutsky’s theorem, the desired result in ([11](https://arxiv.org/html/2601.01642v1#S4.E11 "In Theorem 2 (Central Limit Theorem). ‣ 4.2. Efficiency of DRIS ‣ 4. Main Algorithm and Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) follows.
∎

###### Proof of Theorem [3](https://arxiv.org/html/2601.01642v1#Thmtheorem3 "Theorem 3 (Vanishing Relative Error). ‣ 4.2. Efficiency of DRIS ‣ 4. Main Algorithm and Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")..

Since 𝐱∗=arg⁡min𝐱∈ℰr⁡‖𝐱‖2=r​𝐞1{\mathbf{x}}^{\*}=\arg\min\_{{\mathbf{x}}\in{\cal E}\_{r}}\|{\mathbf{x}}\|^{2}=r{\mathbf{e}}\_{1} and x1∗=rx\_{1}^{\*}=r, we observe that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | σr2\displaystyle\sigma\_{r}^{2} | =𝖵𝖺𝗋​(𝟙​{d​(fur​(𝐙),ℰr)≤ur}​Lur​(𝐙)​(1−d​(fur​(𝐙),ℰr)2ur2))\displaystyle={\sf Var}\left(\mathds{1}\{d(f\_{u\_{r}}({\mathbf{Z}}),{\cal E}\_{r})\leq u\_{r}\}L\_{u\_{r}}({\mathbf{Z}})\left(1-\frac{d(f\_{u\_{r}}({\mathbf{Z}}),{\cal E}\_{r})^{2}}{u\_{r}^{2}}\right)\right) |  | (15) |
|  |  | ≤𝖤​[Lur​(𝐙)2​(1−d​(fur​(𝐙),ℰr)2ur2)2;d​(fur​(𝐙),ℰr)≤ur]\displaystyle\leq{\sf E}\left[L\_{u\_{r}}({\mathbf{Z}})^{2}\left(1-\frac{d(f\_{u\_{r}}({\mathbf{Z}}),{\cal E}\_{r})^{2}}{u\_{r}^{2}}\right)^{2};d(f\_{u\_{r}}({\mathbf{Z}}),{\cal E}\_{r})\leq u\_{r}\right] |  |
|  |  | =𝖤0​[ℓur​(X1)​(1−d​(𝐗,ℰr)2ur2)2;d​(𝐗,ℰr)≤ur]\displaystyle={\sf E}\_{0}\Bigg[\ell\_{u\_{r}}(X\_{1})\left(1-\frac{d({\mathbf{X}},{\cal E}\_{r})^{2}}{u\_{r}^{2}}\right)^{2};d({\mathbf{X}},{\cal E}\_{r})\leq u\_{r}\Bigg] |  |
|  |  | ≤(𝖤0[ℓur(X1)2:d(𝐗,ℰr)≤ur]𝖤0[(1−d​(𝐗,ℰr)2ur2)4:d(𝐗,ℰr)≤ur])1/2,\displaystyle\leq\left({\sf E}\_{0}\big[\ell\_{u\_{r}}(X\_{1})^{2}:d({\mathbf{X}},{\cal E}\_{r})\leq u\_{r}\big]{\sf E}\_{0}\Bigg[\left(1-\frac{d({\mathbf{X}},{\cal E}\_{r})^{2}}{u\_{r}^{2}}\right)^{4}:d({\mathbf{X}},{\cal E}\_{r})\leq u\_{r}\Bigg]\right)^{1/2}, |  |

where ℓu​(x)≔e−x2/2+(r−u)​(x−(r−u))/((r−u)​2​π)​𝟙​{x≥r−u}\ell\_{u}(x)\coloneqq e^{-x^{2}/2+(r-u)(x-(r-u))}/((r-u)\sqrt{2\pi})\mathds{1}{\{x\geq r-u\}} and the last inequality holds by the Cauchy–Schwarz inequality.
A simple calculation yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤0​[ℓur​(X1)2;d​(𝐗,ℰr)≤ur]≤𝖤0​[ℓur​(X1)2;X1≥r−ur]≤e−3​(r−ur)2/2(2​π)3/2​(r−ur)3.{\sf E}\_{0}\big[\ell\_{u\_{r}}(X\_{1})^{2};d({\mathbf{X}},{\cal E}\_{r})\leq u\_{r}\big]\leq{\sf E}\_{0}[\ell\_{u\_{r}}(X\_{1})^{2};X\_{1}\geq r-u\_{r}]\leq\frac{e^{-3(r-u\_{r})^{2}/2}}{(2\pi)^{3/2}(r-u\_{r})^{3}}. |  | (16) |

Also, by using integration by parts, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝖤0[(1−d​(𝐗,ℰr)2ur2)4:d(𝐗,ℰr)≤ur]\displaystyle{\sf E}\_{0}\left[\left(1-\frac{d({\mathbf{X}},{\cal E}\_{r})^{2}}{u\_{r}^{2}}\right)^{4}:d({\mathbf{X}},{\cal E}\_{r})\leq u\_{r}\right] | ≤8ur2​∫0urt​(1−t2ur2)3​𝖯0​(d​(𝐗,ℰr)≤t)​dt\displaystyle\leq\frac{8}{u\_{r}^{2}}\int\_{0}^{u\_{r}}t\left(1-\frac{t^{2}}{u\_{r}^{2}}\right)^{3}{\sf P}\_{0}(d({\mathbf{X}},{\cal E}\_{r})\leq t){\rm d}t |  | (17) |
|  |  | ≤8ur2​∫0urt​(1−t2ur2)3​e−(r−t)2/22​π​(r−t)​dt\displaystyle\leq\frac{8}{u\_{r}^{2}}\int\_{0}^{u\_{r}}t\left(1-\frac{t^{2}}{u\_{r}^{2}}\right)^{3}\frac{e^{-(r-t)^{2}/2}}{\sqrt{2\pi}(r-t)}{\rm d}t |  |
|  |  | ≤64​e−(r−ur)2/22​π​(r−ur)​ur4​∫0ur(ur−t)3​e−(r−ur)​(ur−t)​dt\displaystyle\leq\frac{64e^{-(r-u\_{r})^{2}/2}}{\sqrt{2\pi}(r-u\_{r})u\_{r}^{4}}\int\_{0}^{u\_{r}}(u\_{r}-t)^{3}e^{-(r-u\_{r})(u\_{r}-t)}{\rm d}t |  |
|  |  | ≤64​e−(r−ur)2/22​π​(r−ur)​ur4​∫0∞y3​e−(r−ur)​y​dy\displaystyle\leq\frac{64e^{-(r-u\_{r})^{2}/2}}{\sqrt{2\pi}(r-u\_{r})u\_{r}^{4}}\int\_{0}^{\infty}y^{3}e^{-(r-u\_{r})y}{\rm d}y |  |
|  |  | ≤384​e−(r−ur)2/22​π​(r−ur)5​ur4,\displaystyle\leq\frac{384e^{-(r-u\_{r})^{2}/2}}{\sqrt{2\pi}(r-u\_{r})^{5}u\_{r}^{4}}, |  |

where the second inequality holds since 𝖯0​(d​(𝐗,ℰr)≤t)≤Φ¯​(r−t)≤(2​π)−1/2​e−(r−t)2/2/(r−t){\sf P}\_{0}(d({\mathbf{X}},{\cal E}\_{r})\leq t)\leq\bar{\Phi}(r-t)\leq(2\pi)^{-1/2}e^{-(r-t)^{2}/2}/(r-t) for any t∈[0,r]t\in[0,r], and the third inequality follows because t​(1−t2/ur2)3≤8​(ur−t)3/ur2t(1-t^{2}/u\_{r}^{2})^{3}\leq 8(u\_{r}-t)^{3}/u\_{r}^{2} and e−(r−t)2/2/(r−t)≤e−(r−ur)2/2−(r−ur)​(ur−t)/(r−ur)e^{-(r-t)^{2}/2}/(r-t)\leq e^{-(r-u\_{r})^{2}/2-(r-u\_{r})(u\_{r}-t)}/(r-u\_{r}) for all t∈[0,ur]t\in[0,u\_{r}].
By ([15](https://arxiv.org/html/2601.01642v1#A1.E15 "In Proof of Theorem 3.. ‣ Appendix A Proofs of the Theoretical Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")), ([16](https://arxiv.org/html/2601.01642v1#A1.E16 "In Proof of Theorem 3.. ‣ Appendix A Proofs of the Theoretical Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")), and ([17](https://arxiv.org/html/2601.01642v1#A1.E17 "In Proof of Theorem 3.. ‣ Appendix A Proofs of the Theoretical Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | σr2≤(e−3​(r−ur)2/2(2​π)3/2​(r−ur)3​384​e−(r−ur)2/22​π​(r−ur)5​ur4)1/2=4​6​e−(r−ur)2π​(r−ur)4​ur2.\displaystyle\sigma\_{r}^{2}\leq\left(\frac{e^{-3(r-u\_{r})^{2}/2}}{(2\pi)^{3/2}(r-u\_{r})^{3}}\frac{384e^{-(r-u\_{r})^{2}/2}}{\sqrt{2\pi}(r-u\_{r})^{5}u\_{r}^{4}}\right)^{1/2}=\frac{4\sqrt{6}e^{-(r-u\_{r})^{2}}}{\pi(r-u\_{r})^{4}u\_{r}^{2}}. |  | (18) |

Suppose that n≥2n\geq 2. Fix w,u>0w,u>0 satisfying w<u2w<u^{2}.
Assume that r−u<x1<r−wr-u<x\_{1}<r-\sqrt{w} and ‖𝐱−r​𝐞1‖≤u\|{\mathbf{x}}-r{\mathbf{e}}\_{1}\|\leq u for some 𝐱∈ℝn{\mathbf{x}}\in\mathbb{R}^{n}. Since r​𝐞1∈ℰrr{\mathbf{e}}\_{1}\in{\cal E}\_{r}, we have d​(𝐱,ℰr)≤ud({\mathbf{x}},{\cal E}\_{r})\leq u. Let 𝐱¯=arg⁡min𝐲∈ℰr⁡‖𝐱−𝐲‖\bar{\mathbf{x}}=\arg\min\_{{\mathbf{y}}\in{\cal E}\_{r}}\|{\mathbf{x}}-{\mathbf{y}}\|. Then, x¯1≥r\bar{x}\_{1}\geq r, and thus, d​(𝐱,ℰr)≥x¯1−x1>wd({\mathbf{x}},{\cal E}\_{r})\geq\bar{x}\_{1}-x\_{1}>\sqrt{w}. Furthermore, 𝖯0​(‖𝐗−r​𝐞1‖≤u|X1=x){\sf P}\_{0}(\|{\mathbf{X}}-r{\mathbf{e}}\_{1}\|\leq u\,|\,X\_{1}=x) is equal to the probability of a chi-squared random variable with n−1n-1 degree of freedom not exceeding u2−(x−r)2u^{2}-(x-r)^{2} since ‖𝐱−r​𝐞1‖2=(x1−r)2+∑i=2nxi2\|{\mathbf{x}}-r{\mathbf{e}}\_{1}\|^{2}=(x\_{1}-r)^{2}+\sum\_{i=2}^{n}x\_{i}^{2} for any 𝐱∈ℝn{\mathbf{x}}\in\mathbb{R}^{n}. Accordingly, there exists C>0C>0 such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝖯0​(w<d​(𝐗,ℰr)2≤u2)\displaystyle{\sf P}\_{0}(w<d({\mathbf{X}},{\cal E}\_{r})^{2}\leq u^{2}) | ≥𝖯0(r−u<X1<r−w,∥𝐗−r𝐞1∥≤u)\displaystyle\geq{\sf P}\_{0}(r-u<X\_{1}<r-\sqrt{w},\|{\mathbf{X}}-r{\mathbf{e}}\_{1}\|\leq u) |  | (19) |
|  |  | =∫r−ur−w𝖯0​(‖𝐗−r​𝐞1‖≤u|X1=x)​e−x2/22​π​dx\displaystyle=\int\_{r-u}^{r-\sqrt{w}}{\sf P}\_{0}(\|{\mathbf{X}}-r{\mathbf{e}}\_{1}\|\leq u\,|\,X\_{1}=x)\frac{e^{-x^{2}/2}}{\sqrt{2\pi}}{\rm d}x |  |
|  |  | =C​∫r−ur−w∫0u2−(x−r)2t(n−3)/2​e−t/2​e−x2/2​dt​dx.\displaystyle=C\int\_{r-u}^{r-\sqrt{w}}\int\_{0}^{u^{2}-(x-r)^{2}}t^{(n-3)/2}e^{-t/2}e^{-x^{2}/2}{\rm d}t{\rm d}x. |  |

Using integration by parts, one can show that hr​(u)=∫0u2𝖯​(w<d​(𝐗,ℰr)2≤u2)​dwh\_{r}(u)=\int\_{0}^{u^{2}}{\sf P}(w<d({\mathbf{X}},{\cal E}\_{r})^{2}\leq u^{2}){\rm d}w. Then, by ([19](https://arxiv.org/html/2601.01642v1#A1.E19 "In Proof of Theorem 3.. ‣ Appendix A Proofs of the Theoretical Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | hr​(u)\displaystyle h\_{r}(u) | ≥C​∫0u2∫r−ur−w∫0u2−(x−r)2t(n−3)/2​e−t/2​e−x2/2​dt​dx​dw\displaystyle\geq C\int\_{0}^{u^{2}}\int\_{r-u}^{r-\sqrt{w}}\int\_{0}^{u^{2}-(x-r)^{2}}t^{(n-3)/2}e^{-t/2}e^{-x^{2}/2}{\rm d}t{\rm d}x{\rm d}w |  | (20) |
|  |  | =2​C​∫0u∫0y2∫0(u2−y2)1/2sn−2​e−s2/2​e−(r−y)2/2​ds​dw​dy\displaystyle=2C\int\_{0}^{u}\int\_{0}^{y^{2}}\int\_{0}^{(u^{2}-y^{2})^{1/2}}s^{n-2}e^{-s^{2}/2}e^{-(r-y)^{2}/2}{\rm d}s{\rm d}w{\rm d}y |  |
|  |  | =2​C​∫0uy2​∫0(u2−y2)1/2sn−2​e−s2/2​e−(r−y)2/2​ds​dy\displaystyle=2C\int\_{0}^{u}y^{2}\int\_{0}^{(u^{2}-y^{2})^{1/2}}s^{n-2}e^{-s^{2}/2}e^{-(r-y)^{2}/2}{\rm d}s{\rm d}y |  |
|  |  | =2C∫0uρn+1e−(r−ρ)2/2∫0π/2cos(θ)2sin(θ)n−2e−r​ρ​(1−cos⁡(θ))dθdρ,\displaystyle=2C\int\_{0}^{u}\rho^{n+1}e^{-(r-\rho)^{2}/2}\int\_{0}^{\pi/2}\cos(\theta)^{2}\sin(\theta)^{n-2}e^{-r\rho(1-\cos(\theta))}{\rm d}\theta{\rm d}\rho, |  |

where the first equality holds by interchanging the first two integrals and setting s=ts=\sqrt{t} and y=r−xy=r-x, and the last equality follows from setting s=ρ​sin⁡(θ)s=\rho\sin(\theta) and y=ρ​cos⁡(θ)y=\rho\cos(\theta).

Let εr=1/ur\varepsilon\_{r}=1/u\_{r}. Then, 0≤εr/r≤10\leq\varepsilon\_{r}/r\leq 1 for all sufficiently large rr. Thus, for all ρ∈(0,u)\rho\in(0,u), the inner integral of the last expression in ([20](https://arxiv.org/html/2601.01642v1#A1.E20 "In Proof of Theorem 3.. ‣ Appendix A Proofs of the Theoretical Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) satisfies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∫0π/2cos(θ)2sin(θ)n−2e−r​ρ​(1−cos⁡(θ))dθ\displaystyle\int\_{0}^{\pi/2}\cos(\theta)^{2}\sin(\theta)^{n-2}e^{-r\rho(1-\cos(\theta))}{\rm d}\theta | ≥∫0arccos⁡(1−εr/r)cos(θ)2sin(θ)n−2e−r​ρ​(1−cos⁡(θ))dθ\displaystyle\geq\int\_{0}^{\arccos(1-\varepsilon\_{r}/r)}\cos(\theta)^{2}\sin(\theta)^{n-2}e^{-r\rho(1-\cos(\theta))}{\rm d}\theta |  | (21) |
|  |  | ≥(1−εrr)2e−εr​ρ∫0arccos⁡(1−εr/r)sin(θ)n−2dθ\displaystyle\geq\left(1-\frac{\varepsilon\_{r}}{r}\right)^{2}e^{-\varepsilon\_{r}\rho}\int\_{0}^{\arccos(1-\varepsilon\_{r}/r)}\sin(\theta)^{n-2}{\rm d}\theta |  |
|  |  | =(1−εrr)2​e−εr​ρ​∫0εr/r(2​α)(n−3)/2​(1−α/2)(n−3)/2​dα\displaystyle=\left(1-\frac{\varepsilon\_{r}}{r}\right)^{2}e^{-\varepsilon\_{r}\rho}\int\_{0}^{\varepsilon\_{r}/r}{(2\alpha)}^{(n-3)/2}{(1-\alpha/2)}^{(n-3)/2}{\rm d}\alpha |  |
|  |  | ≥κr​e−εr​ρ,\displaystyle\geq\kappa\_{r}e^{-\varepsilon\_{r}\rho}, |  |

where κr=(1−εr/r)2​(1−εr/(2​r))(n−3)/2​(2​εr/r)(n−1)/2/(n−1)\kappa\_{r}=(1-{\varepsilon\_{r}}/{r})^{2}({1-{\varepsilon\_{r}}/{(2r)}})^{(n-3)/2}({2\varepsilon\_{r}}/{r})^{(n-1)/2}/(n-1), and the equality stems from setting θ=arccos⁡(1−α)\theta=\arccos(1-\alpha).
Hence, by ([20](https://arxiv.org/html/2601.01642v1#A1.E20 "In Proof of Theorem 3.. ‣ Appendix A Proofs of the Theoretical Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) and using integration by parts twice, we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | hr​(ur)\displaystyle h\_{r}(u\_{r}) | ≥2​C​κr​∫0urρn+1​e−(r−ρ)2/2−εr​ρ​dρ\displaystyle\geq 2C\kappa\_{r}\int\_{0}^{u\_{r}}\rho^{n+1}e^{-(r-\rho)^{2}/2-\varepsilon\_{r}\rho}{\rm d}\rho |  | (22) |
|  |  | =2​C​κr​(Ir​(ur)+∫0ure−(r−ρ)2/2−εr​ρ(r−εr−ρ)2​ρn−1​(n​(n+1)+3​(n+1)​ρr−εr−ρ+3​ρ2(r−εr−ρ)2)​dρ)\displaystyle=2C\kappa\_{r}\left(I\_{r}(u\_{r})+\int\_{0}^{u\_{r}}\frac{e^{-(r-\rho)^{2}/2-\varepsilon\_{r}\rho}}{(r-\varepsilon\_{r}-\rho)^{2}}\rho^{n-1}\left(n(n+1)+\frac{3(n+1)\rho}{r-\varepsilon\_{r}-\rho}+\frac{3\rho^{2}}{(r-\varepsilon\_{r}-\rho)^{2}}\right){\rm d}\rho\right) |  |
|  |  | ≥2​C​κr​Ir​(ur),\displaystyle\geq 2C\kappa\_{r}I\_{r}(u\_{r}), |  |

where

|  |  |  |
| --- | --- | --- |
|  | Ir​(ur)≔e−(r−ur)2/2−1r−ur−1−ur​urn+1​(1−n+1ur​(r−ur−1−ur)−1(r−ur−1−ur)2).I\_{r}(u\_{r})\coloneqq\frac{e^{-(r-u\_{r})^{2}/2-1}}{r-u\_{r}^{-1}-u\_{r}}u\_{r}^{n+1}\left(1-\frac{n+1}{u\_{r}(r-u\_{r}^{-1}-u\_{r})}-\frac{1}{(r-u\_{r}^{-1}-u\_{r})^{2}}\right). |  |

Recall that r−ur→∞r-u\_{r}\to\infty and ur/r→1u\_{r}/r\to 1 as r→∞r\to\infty by Lemma [2](https://arxiv.org/html/2601.01642v1#Thmlemma2 "Lemma 2 (Asymptotic Behavior of 𝑢_𝑟). ‣ 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation") and the proof of Theorem [1](https://arxiv.org/html/2601.01642v1#Thmtheorem1 "Theorem 1 (Asymptotic Behavior of 𝑝_𝑟). ‣ 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation"). Thus, we have κr∼r−n+1​2(n−1)/2/(n−1)\kappa\_{r}\sim r^{-n+1}2^{(n-1)/2}/(n-1) and Ir​(ur)∼rn+1​e−(r−ur)2/2−1/(r−ur−1−ur)I\_{r}(u\_{r})\sim{r^{n+1}e^{-(r-u\_{r})^{2}/2-1}}/({r-u\_{r}^{-1}-u\_{r}}), where ∼\sim represents asymptotic equivalence as r→∞r\to\infty.
Since δ2=hr​(ur)\delta^{2}=h\_{r}(u\_{r}) for all rr, the above inequality implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supr→∞r2​e−(r−ur)2/2−1r−ur−1−ur≤C∗​δ2,\displaystyle\limsup\_{r\to\infty}r^{2}\frac{e^{-(r-u\_{r})^{2}/2-1}}{r-u\_{r}^{-1}-u\_{r}}\leq C\_{\*}\delta^{2}, |  | (23) |

where C∗=(n−1)/(2(n+1)/2​C)C\_{\*}=(n-1)/({2^{(n+1)/2}C}). Finally, combining this result with ([18](https://arxiv.org/html/2601.01642v1#A1.E18 "In Proof of Theorem 3.. ‣ Appendix A Proofs of the Theoretical Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")) and Theorem [1](https://arxiv.org/html/2601.01642v1#Thmtheorem1 "Theorem 1 (Asymptotic Behavior of 𝑝_𝑟). ‣ 3. Preliminaries ‣ Wasserstein Distributionally Robust Rare-Event Simulation"), we get

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | lim supr→∞r2​(r−ur)2​σr2pr2\displaystyle\limsup\_{r\to\infty}r^{2}(r-u\_{r})^{2}\frac{\sigma\_{r}^{2}}{p\_{r}^{2}} | ≤4​6π​1lim infr→∞r4​pr2​lim supr→∞r4​e−(r−ur)2(r−ur)2\displaystyle\leq\frac{4\sqrt{6}}{\pi}\frac{1}{\liminf\_{r\to\infty}r^{4}p\_{r}^{2}}\limsup\_{r\to\infty}r^{4}\frac{e^{-(r-u\_{r})^{2}}}{(r-u\_{r})^{2}} |  | (24) |
|  |  | ≤4​e2​6π​δ4​(lim supr→∞r2​e−(r−ur)2/2−1r−ur−1−ur)2\displaystyle\leq\frac{4e^{2}\sqrt{6}}{\pi\delta^{4}}\left(\limsup\_{r\to\infty}r^{2}\frac{e^{-(r-u\_{r})^{2}/2-1}}{r-u\_{r}^{-1}-u\_{r}}\right)^{2} |  |
|  |  | ≤4​C∗2​e2​6π<∞.\displaystyle\leq\frac{4C\_{\*}^{2}e^{2}\sqrt{6}}{\pi}<\infty. |  |

When n=1n=1, we obtain the following relationship using the same argument as in ([20](https://arxiv.org/html/2601.01642v1#A1.E20 "In Proof of Theorem 3.. ‣ Appendix A Proofs of the Theoretical Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | hr​(ur)\displaystyle h\_{r}(u\_{r}) | =∫0ur2𝖯​(w<d​(𝐗,ℰr)2≤ur2)​dz\displaystyle=\int\_{0}^{u\_{r}^{2}}{\sf P}(w<d({\mathbf{X}},{\cal E}\_{r})^{2}\leq u\_{r}^{2}){\rm d}z |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(2​π)−1/2​∫0ur2∫r−urr−we−x2/2​dx​dw\displaystyle=(2\pi)^{-1/2}\int\_{0}^{u\_{r}^{2}}\int\_{r-u\_{r}}^{r-\sqrt{w}}e^{-x^{2}/2}{\rm d}x{\rm d}w |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(2​π)−1/2​∫0ury2​e−(r−y)2/2​𝑑y.\displaystyle=(2\pi)^{-1/2}\int\_{0}^{u\_{r}}y^{2}e^{-(r-y)^{2}/2}dy. |  |

Using integration by parts, the right-hand side is bounded from below by

|  |  |  |
| --- | --- | --- |
|  | 12​π​e−(r−ur)2/2r−ur​(urr)2​r2​(1−2ur​(r−ur)−1(r−ur)2)∼r2​e−(r−ur)2/22​π​(r−ur).\frac{1}{\sqrt{2\pi}}\frac{e^{-(r-u\_{r})^{2}/2}}{r-u\_{r}}\left(\frac{u\_{r}}{r}\right)^{2}r^{2}\left(1-\frac{2}{u\_{r}(r-u\_{r})}-\frac{1}{(r-u\_{r})^{2}}\right)\sim\frac{r^{2}e^{-(r-u\_{r})^{2}/2}}{\sqrt{2\pi}(r-u\_{r})}. |  |

Analogous to ([24](https://arxiv.org/html/2601.01642v1#A1.E24 "In Proof of Theorem 3.. ‣ Appendix A Proofs of the Theoretical Results ‣ Wasserstein Distributionally Robust Rare-Event Simulation")), we apply δ2=hr​(ur)\delta^{2}=h\_{r}(u\_{r}) and arrive at

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | lim supr→∞r2​(r−ur)2​σr2pr2≤\displaystyle\limsup\_{r\to\infty}r^{2}(r-u\_{r})^{2}\frac{\sigma\_{r}^{2}}{p\_{r}^{2}}\leq | 4​6π​1lim infr→∞r4​pr2​lim supr→∞r4​e−(r−ur)2(r−ur)2≤8​6<∞.\displaystyle\frac{4\sqrt{6}}{\pi}\frac{1}{\liminf\_{r\to\infty}r^{4}p\_{r}^{2}}\limsup\_{r\to\infty}r^{4}\frac{e^{-(r-u\_{r})^{2}}}{(r-u\_{r})^{2}}\leq 8\sqrt{6}<\infty. |  | (25) |

This completes the proof.
∎

## Appendix B Technical Lemmas

###### Lemma 3.

Fix 𝐳∈(0,∞)×ℝn−1{\mathbf{z}}\in(0,\infty)\times\mathbb{R}^{n-1} and let g​(u)=d​(fu​(𝐳),ℰ)−ug(u)=d(f\_{u}({\mathbf{z}}),{\cal E})-u for any uu in a compact interval Θ\Theta of (0,x1∗)(0,x\_{1}^{\*}). We say that vv is a zero-crossing if it is in the interior of Θ\Theta and there exists δ>0\delta>0 such that 𝟙​{g​(v−t)≤0}≠𝟙​{g​(v+t)≤0}\mathds{1}\{g(v-t)\leq 0\}\neq\mathds{1}\{g(v+t)\leq 0\} for all t∈(0,δ)t\in(0,\delta). Then, there are at most two zero-crossings.

###### Proof.

Let z1​(u)=x1∗−u+z1/(x1∗−u)z\_{1}(u)=x\_{1}^{\*}-u+z\_{1}/(x\_{1}^{\*}-u) be the first coordinate of fu​(𝐳)f\_{u}({\mathbf{z}}) for u∈Θu\in\Theta. We write Θ=[uL,uU]\Theta=[u\_{L},u\_{U}] for some 0<uL≤uU<x1∗0<u\_{L}\leq u\_{U}<x\_{1}^{\*}.

Let u∗=min⁡{max⁡{uL,x1∗−z1},uU}u\_{\*}=\min\{\max\{u\_{L},x\_{1}^{\*}-\sqrt{z\_{1}}\},u\_{U}\}, I1≔[uL,u∗]I\_{1}\coloneqq[u\_{L},u\_{\*}], and I2≔(u∗,uU]I\_{2}\coloneqq(u\_{\*},u\_{U}]. Since d​(⋅,ℰ)d(\cdot,{\cal E}) is 1-Lipschitz and |z1′​(⋅)|≤1|z\_{1}^{\prime}(\cdot)|\leq 1 on I1I\_{1}, we have |g​(u)+u−g​(v)−v|≤|z1​(u)−z1​(v)|≤|u−v||g(u)+u-g(v)-v|\leq|z\_{1}(u)-z\_{1}(v)|\leq|u-v|, which implies that g​(u)≤g​(v)+v−u+|u−v|g(u)\leq g(v)+v-u+|u-v|
for any u,v∈I1u,v\in I\_{1}. Thus, if g​(v)≤0g(v)\leq 0 for some v∈I1v\in I\_{1}, then g​(u)≤0g(u)\leq 0 for all u∈[v,u∗]u\in[v,u\_{\*}].

On the other hand, z1​(⋅)z\_{1}(\cdot) is strictly increasing and convex on I2I\_{2}. Moreover, it can be easily verified that d​(𝐲,ℰ)d({\mathbf{y}},{\cal E}) is convex in y1y\_{1}.
Thus, d​(fu​(𝐳),ℰ)d(f\_{u}({\mathbf{z}}),{\cal E}) is decreasing with respect to uu on (u∗,w](u\_{\*},w] and increasing on (w,uU](w,u\_{U}] for some w∈(u∗,uU]w\in(u\_{\*},u\_{U}]. This suggests that g​(⋅)g(\cdot) is also decreasing on (u∗,w](u\_{\*},w]. Furthermore, g​(⋅)g(\cdot) is convex on (w,uU](w,u\_{U}].
Therefore, there are at most two zero-crossings in Θ\Theta.
∎

###### Lemma 4.

h​(⋅)h(\cdot) and p​(⋅)p(\cdot) are differentiable at u∗{u\_{\*}} with h′​(u∗)=u∗2​p′​(u∗)≠0h^{\prime}({u\_{\*}})=u\_{\*}^{2}p^{\prime}({u\_{\*}})\neq 0.

###### Proof.

Recall that p​(u)=𝖯​(d​(𝐗,ℰ)≤u)p(u)={\sf P}(d({\mathbf{X}},{\cal E})\leq u).
It is straightforward to check that d​(⋅,ℰ)d(\cdot,{\cal E}) is 1-Lipschitz and differentiable almost everywhere with ‖∇d​(⋅,ℰ)‖=1\|\nabla d(\cdot,{\cal E})\|=1. Then, by the coarea formula (EvansGariepy1992, Theorem 3.4.2), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | p​(u∗+δ)−p​(u∗)\displaystyle p({u\_{\*}}+\delta)-p({u\_{\*}}) | =𝖯​(u∗<d​(𝐗,ℰ)≤u∗+δ)\displaystyle={\sf P}({u\_{\*}}<d({\mathbf{X}},{\cal E})\leq{u\_{\*}}+\delta) |  | (26) |
|  |  | =∫ℝdϕ​(𝐱)​𝟙​{u∗<d​(𝐱,ℰ)≤u∗+δ}​‖∇d​(𝐱,ℰ)‖​d𝐱\displaystyle=\int\_{\mathbb{R}^{d}}\phi({\mathbf{x}})\mathds{1}{\{{u\_{\*}}<d({\mathbf{x}},{\cal E})\leq{u\_{\*}}+\delta\}}\|\nabla d({\mathbf{x}},{\cal E})\|{\rm d}{\mathbf{x}} |  |
|  |  | =∫ℝ(∫∂(ℰ+B​(u∗+t))ϕ​(𝐳)​𝟙​{u∗<d​(𝐳,ℰ)≤u∗+δ}​dℋ​(𝐳))​dt\displaystyle=\int\_{\mathbb{R}}\left(\int\_{\partial({\cal E}+B({u\_{\*}}+t))}\phi({\mathbf{z}})\mathds{1}{\{{u\_{\*}}<d({\mathbf{z}},{\cal E})\leq{u\_{\*}}+\delta\}}{\rm d}{\cal H}({\mathbf{z}})\right){\rm d}t |  |
|  |  | =∫0δ(∫∂(ℰ+B​(u∗+t))ϕ​(𝐳)​dℋ​(𝐳))​dt,\displaystyle=\int\_{0}^{\delta}\left(\int\_{\partial({\cal E}+B({u\_{\*}}+t))}\phi({\mathbf{z}}){\rm d}{\cal H}({\mathbf{z}})\right){\rm d}t, |  |

where ϕ​(𝐳)=(2​π)−n/2​e−‖𝐳‖2/2\phi({\mathbf{z}})=(2\pi)^{-n/2}e^{-\|{\mathbf{z}}\|^{2}/2} is the density of the nn-dimensional standard Gaussian distribution, and ℋ{\cal H} is the (n−1)(n-1)-dimensional Hausdorff measure.

We write ℰu≔{𝐱:d​(𝐱,ℰ)≤u}{\cal E}\_{u}\coloneqq\{{\mathbf{x}}:d({\mathbf{x}},{\cal E})\leq u\}. By the fundamental theorem of calculus, it suffices to show that
g​(u)≔∫∂ℰuϕ​(𝐳)​dℋ​(𝐳)g(u)\coloneqq\int\_{\partial{\cal E}\_{u}}\phi({\mathbf{z}}){\rm d}{\cal H}({\mathbf{z}})
is continuous on (0,∞)(0,\infty).
To that end, we fix u>0u>0 arbitrarily and denote by n​(𝐳)n({\mathbf{z}}) the outer unit normal vector at 𝐳∈∂ℰu{\mathbf{z}}\in\partial{\cal E}\_{u}. Then, by the change of variables,

|  |  |  |
| --- | --- | --- |
|  | g​(u+t)=∫∂ℰuϕ​(𝐳+t​n​(𝐳))​Jt​(𝐳)​dℋ​(𝐳),g(u+t)=\int\_{\partial{\cal E}\_{u}}\phi({\mathbf{z}}+tn({\mathbf{z}}))J\_{t}({\mathbf{z}}){\rm d}{\cal H}({\mathbf{z}}), |  |

where Jt​(𝐳)J\_{t}({\mathbf{z}}) denotes the Jacobian of the mapping 𝐳↦𝐳+t​n​(𝐳){\mathbf{z}}\mapsto{\mathbf{z}}+tn({\mathbf{z}}) for each t≥0t\geq 0.
By the smoothness of ∂ℰu\partial{\cal E}\_{u} and the convexity of ℰu{\cal E}\_{u}, it is not difficult to check that the Jacobian Jt​(𝐳)J\_{t}({\mathbf{z}}) is nonnegative and continuous in both 𝐳{\mathbf{z}} and tt; see, e.g., Schneider:13 and Cecil:15.

Fix ϵ>0\epsilon>0 small enough.
Let η​(𝐳,t)=ϕ​(𝐳+t​n​(𝐳))​Jt​(𝐳)\eta({\mathbf{z}},t)=\phi({\mathbf{z}}+tn({\mathbf{z}}))J\_{t}({\mathbf{z}}) for (𝐳,t)∈∂ℰu×[0,∞)({\mathbf{z}},t)\in\partial{\cal E}\_{u}\times[0,\infty). Then, we can choose a compact set K⊂∂ℰuK\subset\partial{\cal E}\_{u} and a constant tK>0t\_{K}>0 such that for all t∈[0,tK]t\in[0,t\_{K}],
|∫Kη​(𝐳,t)​dℋ​(𝐳)−∫Kη​(𝐳,0)​dℋ​(𝐳)|<ϵ/3|\int\_{K}\eta({\mathbf{z}},t){\rm d}{\cal H}({\mathbf{z}})-\int\_{K}\eta({\mathbf{z}},0){\rm d}{\cal H}({\mathbf{z}})|<{\epsilon}/{3} and ∫∂ℰu∖Kη​(𝐳,t)​dℋ​(𝐳)<ϵ/3\int\_{\partial{\cal E}\_{u}\setminus K}\eta({\mathbf{z}},t){\rm d}{\cal H}({\mathbf{z}})<{\epsilon}/{3}.
This is feasible due to the uniform continuity of η\eta on K×[0,tK]K\times[0,t\_{K}], the nonnegativity of η\eta on ∂ℰu×[0,∞)\partial{\cal E}\_{u}\times[0,\infty), and the uniform boundedness of gg by Ball:93. Hence, for all t∈[0,tk]t\in[0,t\_{k}],

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | |g​(u+t)−g​(u)|\displaystyle|g(u+t)-g(u)| |  | (27) |
|  |  | ≤|∫Kη​(𝐳,t)​dℋ​(𝐳)−∫Kη​(𝐳,0)​dℋ​(𝐳)|+∫∂ℰu∖Kη​(𝐳,t)​dℋ​(𝐳)+∫∂ℰu∖Kη​(𝐳,0)​dℋ​(𝐳)\displaystyle\leq\left|\int\_{K}\eta({\mathbf{z}},t){\rm d}{\cal H}({\mathbf{z}})-\int\_{K}\eta({\mathbf{z}},0){\rm d}{\cal H}({\mathbf{z}})\right|+\int\_{\partial{\cal E}\_{u}\setminus K}\eta({\mathbf{z}},t){\rm d}{\cal H}({\mathbf{z}})+\int\_{\partial{\cal E}\_{u}\setminus K}\eta({\mathbf{z}},0){\rm d}{\cal H}({\mathbf{z}}) |  |
|  |  | <ϵ.\displaystyle<\epsilon. |  |

Consequently, p′​(u∗)=g​(u∗)>0p^{\prime}({u\_{\*}})=g({u\_{\*}})>0.
By the definition of hh, for any ε>0\varepsilon>0 small enough, we have
u∗2​(p​(u∗+ε)−p​(u∗))≤h​(u∗+ε)−h​(u∗)≤(u∗+ε)2​(p​(u∗+ε)−p​(u∗))u\_{\*}^{2}(p({u\_{\*}}+\varepsilon)-p({u\_{\*}}))\leq h({u\_{\*}}+\varepsilon)-h({u\_{\*}})\leq({u\_{\*}}+\varepsilon)^{2}(p({u\_{\*}}+\varepsilon)-p({u\_{\*}})).
Dividing all expressions by ε\varepsilon and sending ε→0\varepsilon\to 0 result in h′​(u∗)=u∗2​p′​(u∗)>0h^{\prime}({u\_{\*}})=u\_{\*}^{2}p^{\prime}({u\_{\*}})>0.
∎