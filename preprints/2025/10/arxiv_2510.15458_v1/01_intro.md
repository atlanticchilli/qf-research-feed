---
authors:
- Gabriele Visentin
- Patrick Cheridito
doc_id: arxiv:2510.15458v1
family_id: arxiv:2510.15458
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: "Robust Optimization in Causal Models and \U0001D43A-Causal Normalizing Flows"
url_abs: http://arxiv.org/abs/2510.15458v1
url_html: https://arxiv.org/html/2510.15458v1
venue: arXiv q-fin
version: 1
year: 2025
---


Gabriele Visentin
  
Department of Mathematics
  
ETH Zurich
  
Zurich, Switzerland
  
gabriele.visentin@math.ethz.ch
  
&Patrick Cheridito
  
Department of Mathematics
  
ETH Zurich
  
Zurich, Switzerland
  
patrick.cheridito@math.ethz.ch

###### Abstract

In this paper, we show that interventionally robust optimization problems in causal models are continuous under the GG-causal Wasserstein distance, but may be discontinuous under the standard Wasserstein distance. This highlights the importance of using generative models that respect the causal structure when augmenting data for such tasks. To this end, we propose a new normalizing flow architecture that satisfies a universal approximation property for causal structural models and can be efficiently trained to minimize the GG-causal Wasserstein distance. Empirically, we demonstrate that our model outperforms standard (non-causal) generative models in data augmentation for causal regression and mean-variance portfolio optimization in causal factor models.

## 1 Introduction

Solving optimization problems often requires generative data augmentation (Chen et al., [2024](https://arxiv.org/html/2510.15458v1#bib.bib8); Zheng et al., [2023](https://arxiv.org/html/2510.15458v1#bib.bib26)), particularly when out-of-sample distributional shifts are expected to be frequent and severe, as in the case of financial applications. In such cases, only the most recent data points are representative enough to be used in solving downstream tasks (such as hedging, regression or portfolio selection), resulting in small datasets that require generative data augmentation to avoid overfitting (Bailey et al., [2017](https://arxiv.org/html/2510.15458v1#bib.bib4)). However, when using generative models for data augmentation, it is essential to choose their training loss in a way that is compatible with the downstream tasks, so as to guarantee good and stable performance.

It is well-known, for instance, that multi-stage stochastic optimization problems are continuous under the *adapted* Wasserstein distance, while they may be discontinuous under the standard Wasserstein distance (Pflug & Pichler, [2012](https://arxiv.org/html/2510.15458v1#bib.bib19); [2014](https://arxiv.org/html/2510.15458v1#bib.bib20); Backhoff-Veraguas et al., [2020](https://arxiv.org/html/2510.15458v1#bib.bib3)). This insight prompted several authors to propose new time-series generative models that attempt to minimize the adapted Wasserstein distance, either partially (Xu et al., [2020](https://arxiv.org/html/2510.15458v1#bib.bib24)) or its one-sided111Also known in the literature as the causal Wasserstein distance, because it respects the temporal flow of information in the causal direction (from past to present). This terminology conflicts with the way the term “causal” is used in causal modelling. To avoid misunderstandings we talk of the “GG-causal” Wasserstein distance and refer to the causal Wasserstein distance as the “one-sided” adapted Wasserstein distance. version (Acciaio et al., [2024](https://arxiv.org/html/2510.15458v1#bib.bib1)).

In this paper we prove a generalization of this result for causal models. Specifically, we show that causal optimization problems (i.e. problems in which the control variables can depend only on the parents of the state variables in the underlying causal DAG GG) are continuous with respect to the GG-causal Wasserstein distance (Cheridito & Eckstein, [2025](https://arxiv.org/html/2510.15458v1#bib.bib9)).

Furthermore, we prove that solutions to GG-causal optimization problems are always interventionally robust. This means that causal optimization can be understood as a way of performing Distributionally Robust Optimization (DRO) (Chen et al., [2020](https://arxiv.org/html/2510.15458v1#bib.bib7); Kuhn et al., [2025](https://arxiv.org/html/2510.15458v1#bib.bib14)) by taking into account the problem’s causal structure.

Next, we address the challenge of designing a generative model capable of good approximations under the GG-causal Wasserstein distance. We radically depart from existing approaches for the adapted Wasserstein distance and propose a novel GG-causal normalizing flow model based on invertible neural couplings that respect the causal structure of the data. We prove a universal approximation property for this model class and that maximum likelihood training indeed leads to distributions that are close to the target distribution in the GG-causal Wasserstein distance. Since the standard, adapted and CO-OT Wasserstein distances are all special cases of the GG-causal Wasserstein distance, this model family provides optimal generative augmentation models for a vast class of empirical applications.

Contributions. Our main contributions are the following:

* •

  We prove that causal optimization problems (i.e. problems in which optimizers must be functions of the state variables’ parents in the causal DAG GG) are continuous under the GG-causal Wasserstein distance, but may be discontinuous under the standard Wasserstein distance.
* •

  We prove that solutions to GG-causal optimization problems are always interventionally robust.
* •

  We introduce GG-causal normalizing flows and we prove that they satisfy a universal approximation property for causal structural models under very mild conditions.
* •

  We prove that GG-causal normalizing flows minimize the GG-causal Wasserstein distance between data and model distribution by simple likelihood maximization.
* •

  We show empirically that GG-causal normalizing flows outperform non-causal generative models (such as variational auto-encoders, standard normalizing flows, and nearest-neighbor KDE) when used to perform generative data augmentation in two empirical setups: causal regression and mean-variance portfolio optimization in causal factor models.

## 2 Background

Notation. We denote by ∥⋅∥\|\cdot\| the Euclidean norm on ℝd\mathbb{R}^{d} and by Lp​(μ)L^{p}(\mu) the space Lp​(ℝd,ℬ​(ℝd),μ)L^{p}(\mathbb{R}^{d},\mathcal{B}(\mathbb{R}^{d}),\mu) equipped with the norm ‖f‖Lp​(μ):=(∫ℝd‖f​(z)‖p​μ​(d​z))1/p\|f\|\_{L^{p}(\mu)}:=\left(\int\_{\mathbb{R}^{d}}\|f(z)\|^{p}\mu(dz)\right)^{1/p}. 𝒫​(ℝd)\mathcal{P}(\mathbb{R}^{d}) denotes the space of all Borel probability measures on ℝd\mathbb{R}^{d}. 𝒩​(μ,Σ)\mathcal{N}(\mu,\Sigma) is the multivariate Gaussian distribution with mean μ\mu and covariance matrix Σ\Sigma, 𝒰​([0,1]d)\mathcal{U}([0,1]^{d}) is the uniform distribution on the dd-dimensional hypercube, IdI\_{d} denotes the d×dd\times d identity matrix.

We use set-indices to slice vectors, i.e. if x=(x1,…,xd)∈ℝdx=(x\_{1},\ldots,x\_{d})\in\mathbb{R}^{d} and A⊆{1,…,d}A\subseteq\{1,\ldots,d\}, then xA:=(xi,i∈A)∈ℝ|A|x\_{A}:=(x\_{i},i\in A)\in\mathbb{R}^{|A|}. If μ∈𝒫​(ℝd)\mu\in\mathcal{P}(\mathbb{R}^{d}) and X=(X1,…,Xd)∼μX=(X\_{1},\ldots,X\_{d})\sim\mu, then the regular conditional distribution of XAX\_{A} given XBX\_{B} is denoted by μ​(d​xA|xB)\mu(dx\_{A}|x\_{B}), for all A,B⊆{1,…,d}A,B\subseteq\{1,\ldots,d\} with A∩B=∅A\cap B=\emptyset.

### 2.1 Structural Causal Models

We assume throughout that G=(V,E)G=(V,E) is a given directed acyclic graph (DAG) with a finite index set V={1,…,d}V=\{1,\ldots,d\}, which we assume, without loss of generality, to be sorted (i.e. (i,j)∈E(i,j)\in E, then i<ji<j). If A⊆VA\subseteq V, we denote by PA​(A):={i∈V∖A|∃j∈A|(i,j)∈E}\text{PA}(A):=\{i\in V\setminus A\>|\>\exists j\in A\>|\>(i,j)\in E\} the set of parents of the vertices in AA (notice that PA​(A)⊆V∖A\text{PA}(A)\subseteq V\setminus A by definition).

In this paper, we work with structural causal models, as presented in Peters et al. ([2017](https://arxiv.org/html/2510.15458v1#bib.bib18)).

###### Definition 2.1 (Structural Causal Model (SCM)).

Given a DAG G=(V,E)G=(V,E), a Structural Causal Model (SCM) is a collection of assignments

|  |  |  |
| --- | --- | --- |
|  | Xi:=fi​(XPA​(i),Ui),for all i=1,…,d,X\_{i}:=f\_{i}(X\_{\text{PA}(i)},U\_{i}),\quad\text{for all $i=1,\ldots,d$}, |  |

where the noise variables (Ui,i=1,…,d)(U\_{i},i=1,\ldots,d) are mutually independent.

### 2.2 GG-causal Wasserstein distance

###### Definition 2.2 (G-compatible distribution).

A distribution μ∈𝒫​(ℝd)\mu\in\mathcal{P}(\mathbb{R}^{d}) is said to be GG-compatible, and we denote it by μ∈𝒫G​(ℝd)\mu\in\mathcal{P}\_{G}(\mathbb{R}^{d}), if any of the following equivalent conditions holds:

1. 1.

   there exist a random vector X=(X1,…,Xd)∼μX=(X\_{1},\ldots,X\_{d})\sim\mu together with measurable functions fi:ℝ|PA​(i)|×ℝ→ℝf\_{i}:\mathbb{R}^{|\text{PA}(i)|}\times\mathbb{R}\to\mathbb{R}, (i=1,…,ni=1,\ldots,n), and mutually independent random variables (Ui,i=1,…,d)(U\_{i},i=1,\ldots,d) such that
   X\_i = f\_i(X\_PA(i), U\_i),  for all i=1,…,di=1,\ldots,d.
2. 2.

   For every X∼μX\sim\mu, one has
   X\_i ⟂​​​ ⟂X\_1:i-1   —  X\_PA(i),  for all i=2,…,di=2,\ldots,d.
3. 3.

   The distribution μ\mu admits the following disintegration:
   μ(dx\_1, …, dx\_d) = ∏\_i=1^d μ(dx\_i   —  x\_PA(i)).

For a proof of the equivalence of these three conditions, see Cheridito & Eckstein ([2025](https://arxiv.org/html/2510.15458v1#bib.bib9), Remark 3.2).

###### Definition 2.3 (GG-bicausal couplings).

A coupling π∈Π​(μ,ν)\pi\in\Pi(\mu,\nu) between two distributions μ,ν∈𝒫G​(ℝd)\mu,\nu\in\mathcal{P}\_{G}(\mathbb{R}^{d}) is GG-causal if there exist (X,X′)∼π(X,X^{\prime})\sim\pi such that

|  |  |  |
| --- | --- | --- |
|  | Xi′=gi​(Xi,XPA​(i),XPA​(i)′,Ui)X^{\prime}\_{i}=g\_{i}(X\_{i},X\_{\text{PA}(i)},X^{\prime}\_{\text{PA}(i)},U\_{i}) |  |

for some measurable mappings (gi)i=1d(g\_{i})\_{i=1}^{d} and mutually independent random variables (Ui)i=1d(U\_{i})\_{i=1}^{d}. If also the distribution of (X′,X)(X^{\prime},X) is GG-causal, then we say that π\pi is GG-bicausal. We denote by ΠGbc​(μ,ν)\Pi\_{G}^{\text{bc}}(\mu,\nu) the set of all GG-bicausal couplings between μ\mu and ν\nu.

###### Definition 2.4 (GG-causal Wasserstein distance).

Denote by 𝒫G,1​(ℝd)\mathcal{P}\_{G,1}(\mathbb{R}^{d}) the space of all GG-compatible distributions with finite first moments. Then the GG-causal Wasserstein distance between μ,ν∈𝒫G,1​(ℝd)\mu,\nu\in\mathcal{P}\_{G,1}(\mathbb{R}^{d}) is defined as:

|  |  |  |
| --- | --- | --- |
|  | WG​(μ,ν):=infπ∈ΠGbc​(μ,ν)∫ℝd×ℝd‖x−x′‖​π​(d​x,d​x′).W\_{G}(\mu,\nu):=\inf\_{\pi\in\Pi\_{G}^{\text{bc}}(\mu,\nu)}\int\_{\mathbb{R}^{d}\times\mathbb{R}^{d}}\|x-x^{\prime}\|\,\pi(dx,dx^{\prime}). |  |

Furthermore, WGW\_{G} defines a semi-metric on the space 𝒫G,1​(ℝd)\mathcal{P}\_{G,1}(\mathbb{R}^{d}) (Cheridito & Eckstein, [2025](https://arxiv.org/html/2510.15458v1#bib.bib9), Proposition 4.3).

## 3 Robust optimization in Structural Causal Models

Suppose we are given an SCM X∼μ∈𝒫G​(ℝd)X\sim\mu\in\mathcal{P}\_{G}(\mathbb{R}^{d}) on a DAG G=(V,E)G=(V,E) and we want to solve a stochastic optimization problem in which the state variables XTX\_{T} are specified by a vertex subset T⊆VT\subseteq V (called the *target set*) and the control variables can potentially be all remaining vertices in the graph, i.e. XV∖TX\_{V\setminus T}. To avoid feedback loops between state and control variables, we will need the following technical assumption.

###### Assumption 3.1.

The DAG G=(V,E)G=(V,E) and the target set T⊆VT\subseteq V are such that GG quotiened by the partition {T}∪{{i},i∈V∖T}\{T\}\cup\{\{i\},i\in V\setminus T\} is a DAG.

###### Remark 3.2.

[3.1](https://arxiv.org/html/2510.15458v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3 Robust optimization in Structural Causal Models ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") is quite mild and is equivalent to asking that if i,j∈Ti,j\in T, then XiX\_{i} cannot be the parent of a parent of XjX\_{j}. This guarantees that PA​(T)∩CH​(T)=∅\text{PA}(T)\cap\text{CH}(T)=\emptyset, which is nothing but asking that XTX\_{T} be part of a valid SCM *as a random vector*, see [Fig. 2](https://arxiv.org/html/2510.15458v1#S3.F2 "In 3 Robust optimization in Structural Causal Models ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") and [2](https://arxiv.org/html/2510.15458v1#S3.F2 "Figure 2 ‣ 3 Robust optimization in Structural Causal Models ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows").

![Refer to caption](x1.png)


Figure 1: DAG GG before quotienting (target set TT highlighted).

![Refer to caption](x2.png)


Figure 2: DAG GG after quotienting (vertex set PA​(T)\text{PA}(T) highlighted).

###### Definition 3.3 (GG-causal function).

Given a target set T⊆VT\subseteq V, we say that a function h:ℝ|V∖T|→ℝ|T|h:\mathbb{R}^{|V\setminus T|}\to\mathbb{R}^{|T|} is GG-causal (with respect to TT) if hh depends only on the parents of XTX\_{T}, i.e. h​(x)=h​(xPA​(T))h(x)=h(x\_{\text{PA}(T)}), for all x∈ℝ|V∖T|x\in\mathbb{R}^{|V\setminus T|}.

###### Definition 3.4 (GG-causal optimization problem).

Let G=(V,E)G=(V,E) be a sorted DAG, X∼μ∈𝒫G​(ℝd)X\sim\mu\in\mathcal{P}\_{G}(\mathbb{R}^{d}) and let T⊆VT\subseteq V be a target set.
If Q:ℝ|T|×ℝ|V∖T|→ℝ¯Q:\mathbb{R}^{|T|}\times\mathbb{R}^{|V\setminus T|}\to\overline{\mathbb{R}} is a function to be optimized, then a GG-causal optimization problem (with respect to TT) is an optimization problem of the following form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minh:ℝ|V∖T|→ℝ|T|h is G-causal⁡𝔼μ​[Q​(XT,h​(XV∖T))].\min\_{\begin{subarray}{c}h:\mathbb{R}^{|V\setminus T|}\to\mathbb{R}^{|T|}\\ \text{$h$ is $G$-causal}\end{subarray}}\mathbb{E}^{\mu}\left[Q(X\_{T},h(X\_{V\setminus T}))\right]. |  | (1) |

Any minimizer of ([1](https://arxiv.org/html/2510.15458v1#S3.E1 "Equation 1 ‣ Definition 3.4 (𝐺-causal optimization problem). ‣ 3 Robust optimization in Structural Causal Models ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows")) is called a GG-causal optimizer.

The following result shows that GG-causal optimizers are always interventionally robust. This underscores the desirability of GG-causal optimizers when we expect the data distribution to undergo distributional shifts due to interventions between training and testing time.

###### Theorem 3.5 (Robustness of GG-causal optimizers).

Let h∗h^{\*} be a solution of the problem in [Eq. 1](https://arxiv.org/html/2510.15458v1#S3.E1 "In Definition 3.4 (𝐺-causal optimization problem). ‣ 3 Robust optimization in Structural Causal Models ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows"). Then:

|  |  |  |
| --- | --- | --- |
|  | h∗∈arg​minh:ℝ|V∖T|→ℝ|T|​supν∈ℐ​(μ)𝔼ν​[Q​(XT,h​(XV∖T))],h^{\*}\in\operatorname\*{arg\,min}\_{h:\mathbb{R}^{|V\setminus T|}\to\mathbb{R}^{|T|}}\sup\_{\nu\in\mathcal{I}(\mu)}\mathbb{E}^{\nu}\left[Q(X\_{T},h(X\_{V\setminus T}))\right], |  |

where

|  |  |  |
| --- | --- | --- |
|  | ℐ​(μ):={ν∈𝒫​(ℝd)|ν​(d​xT|xPA​(T))=μ​(d​xT|xPA​(T)) and supp​(ν​(d​xPA​(T)))⊆supp​(μ​(d​xPA​(T)))}\mathcal{I}(\mu):=\{\nu\in\mathcal{P}(\mathbb{R}^{d})\;\>|\>\;\text{$\nu(dx\_{T}|x\_{\text{PA}(T)})=\mu(dx\_{T}|x\_{\text{PA}(T)})$ and $\mathrm{supp}(\nu(dx\_{\text{PA}(T)}))\subseteq\mathrm{supp}(\mu(dx\_{\text{PA}(T)}))$}\} |  |

is the set of all interventional distributions that leave the causal mechanism of XTX\_{T} unchanged.

###### Proof.

It’s enough to show that for any h:ℝ|V∖T|→ℝ|T|h:\mathbb{R}^{|V\setminus T|}\to\mathbb{R}^{|T|} and any ν∈ℐ​(μ)\nu\in\mathcal{I}(\mu), there exists a ν′∈ℐ​(μ)\nu^{\prime}\in\mathcal{I}(\mu) such that 𝔼ν′​[Q​(XT,h​(XV∖T))]≥𝔼ν​[Q​(XT,h∗​(XPA​(T)))]\mathbb{E}^{\nu^{\prime}}\left[Q(X\_{T},h(X\_{V\setminus T}))\right]\geq\mathbb{E}^{\nu}\left[Q(X\_{T},h^{\*}(X\_{\text{PA}(T)}))\right].

Given ν∈ℐ​(μ)\nu\in\mathcal{I}(\mu), define ν′​(d​x):=ν​(d​xV∖(T∪PA​(T)))​ν​(d​xPA​(T),d​xT)\nu^{\prime}(dx):=\nu(dx\_{V\setminus(T\cup\text{PA}(T))})\nu(dx\_{\text{PA}(T)},dx\_{T}). Then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ν′​[Q​(XT,h​(XV∖T))]\displaystyle\mathbb{E}^{\nu^{\prime}}\left[Q(X\_{T},h(X\_{V\setminus T}))\right] | =∫ν​(d​xV∖(T∪PA​(T)))​∫ν​(d​xPA​(T),d​xT)​Q​(xT,h​(xV∖T))\displaystyle=\int\nu(dx\_{V\setminus(T\cup\text{PA}(T))})\int\nu(dx\_{\text{PA}(T)},dx\_{T})Q(x\_{T},h(x\_{V\setminus T})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫ν​(d​xV∖(T∪PA​(T)))​∫ν​(xPA​(T))​∫μ​(d​xT|xPA​(T))​Q​(xT,h​(xV∖T))\displaystyle=\int\nu(dx\_{V\setminus(T\cup\text{PA}(T))})\int\nu(x\_{\text{PA}(T)})\int\mu(dx\_{T}\>|\>x\_{\text{PA}(T)})Q(x\_{T},h(x\_{V\setminus T})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥∫ν​(d​xV∖(T∪PA​(T)))​∫ν​(xPA​(T))​∫μ​(d​xT|xPA​(T))​Q​(xT,h∗​(xPA​(T)))\displaystyle\geq\int\nu(dx\_{V\setminus(T\cup\text{PA}(T))})\int\nu(x\_{\text{PA}(T)})\int\mu(dx\_{T}\>|\>x\_{\text{PA}(T)})Q(x\_{T},h^{\*}(x\_{\text{PA}(T)})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ν​[Q​(XT,h∗​(XPA​(T)))]\displaystyle=\mathbb{E}^{\nu}\left[Q(X\_{T},h^{\*}(X\_{\text{PA}(T)}))\right] |  |

where the second equality follows from ν∈ℐ​(μ)\nu\in\mathcal{I}(\mu) and the inequality follows from [Eq. 1](https://arxiv.org/html/2510.15458v1#S3.E1 "In Definition 3.4 (𝐺-causal optimization problem). ‣ 3 Robust optimization in Structural Causal Models ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows"), [Lemma A.1](https://arxiv.org/html/2510.15458v1#A1.Thmtheorem1 "Lemma A.1 (Interchangeability principle). ‣ Appendix A Auxiliary results ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows"), and supp​(ν​(d​xPA​(Y)))⊆supp​(μ​(d​xPA​(Y)))\mathrm{supp}(\nu(dx\_{\text{PA}(Y)}))\subseteq\mathrm{supp}(\mu(dx\_{\text{PA}(Y)})).
∎

###### Remark 3.6.

The theorem above is a generalization of (Rojas-Carulla et al., [2018](https://arxiv.org/html/2510.15458v1#bib.bib22), Theorem 4), which covered the mean squared loss only. We explicitly added the assumption supp​(ν​(d​xPA​(Y)))⊆supp​(μ​(d​xPA​(Y)))\mathrm{supp}(\nu(dx\_{\text{PA}(Y)}))\subseteq\mathrm{supp}(\mu(dx\_{\text{PA}(Y)})), for all ν∈ℐ​(μ)\nu\in\mathcal{I}(\mu), which is needed also for their theorem to hold.

The next theorem shows that the value functionals of GG-causal optimization problems are continuous with respect to the GG-causal Wasserstein distance, while they may fail to be continuous with respect to the standard Wasserstein distance (as we show in [Example 3.8](https://arxiv.org/html/2510.15458v1#S3.Thmtheorem8 "Example 3.8. ‣ 3 Robust optimization in Structural Causal Models ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") below). This proves that the GG-causal Wasserstein distance is the right distance to control errors in causal optimization problems and, in particular, interventionally robust optimization problems.

###### Theorem 3.7 (Continuity of GG-causal optimization problems).

Let G=(V,E)G=(V,E) be a sorted DAG, X∼μ∈𝒫G​(ℝd)X\sim\mu\in\mathcal{P}\_{G}(\mathbb{R}^{d}) and let T⊆VT\subseteq V be a target set, such that [3.1](https://arxiv.org/html/2510.15458v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3 Robust optimization in Structural Causal Models ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") holds. If Q:ℝ|T|×ℝ|V∖T|→ℝ¯Q:\mathbb{R}^{|T|}\times\mathbb{R}^{|V\setminus T|}\to\overline{\mathbb{R}} is such that x↦Q​(x,h)x\mapsto Q(x,h) is locally LL-Lipschitz (uniformly in hh) and h↦Q​(x,h)h\mapsto Q(x,h) is convex, then the value functional

|  |  |  |
| --- | --- | --- |
|  | μ↦𝒱​(μ):=minh:ℝ|V∖T|→ℝ|T|h is G-causal⁡𝔼μ​[Q​(XT,h​(XV∖T))]\displaystyle\mu\mapsto\mathcal{V}(\mu):=\min\_{\begin{subarray}{c}h:\mathbb{R}^{|V\setminus T|}\to\mathbb{R}^{|T|}\\ \text{$h$ is $G$-causal}\end{subarray}}\mathbb{E}^{\mu}\left[Q(X\_{T},h(X\_{V\setminus T}))\right] |  |

is continuous with respect to the GG-causal Wasserstein distance.

###### Proof.

See proof in [Section B.1](https://arxiv.org/html/2510.15458v1#A2.SS1 "B.1 Proof of Theorem 3.7 ‣ Appendix B Proofs ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows").
∎

###### Example 3.8.

Define με∈𝒫G​(ℝ2)\mu\_{\varepsilon}\in\mathcal{P}\_{G}(\mathbb{R}^{2}) as the following SCM:

|  |  |  |
| --- | --- | --- |
|  | {Y:=sgn​(X),X:=ε⋅U,where U∼Ra​(1/2),\begin{cases}Y:=\text{sgn}(X),\\ X:=\varepsilon\cdot U,\end{cases}\quad\text{where $U\sim\text{Ra}(1/2)$}, |  |

where Ra​(p)\text{Ra}(p) denoted the Rademacher distribution p​δ1+(1−p)​δ−1p\delta\_{1}+(1-p)\delta\_{-1}, and consider the following GG-causal regression problem:

|  |  |  |
| --- | --- | --- |
|  | 𝒱​(μ)=infh:ℝ→ℝh G-causal𝔼μ​[(Y−h​(X))2].\mathcal{V}(\mu)=\inf\_{\begin{subarray}{c}h:\mathbb{R}\to\mathbb{R}\\ \text{$h$ $G$-causal}\end{subarray}}\mathbb{E}^{\mu}\left[(Y-h(X))^{2}\right]. |  |

Then as ε→0\varepsilon\to 0 we have that με=12​δ(ε,1)+12​δ(−ε,−1)\mu\_{\varepsilon}=\frac{1}{2}\delta\_{(\varepsilon,1)}+\frac{1}{2}\delta\_{(-\varepsilon,-1)} converges to μ:=12​δ(0,1)+12​δ(0,−1)=δ0⊗Ra​(1/2)\mu:=\frac{1}{2}\delta\_{(0,1)}+\frac{1}{2}\delta\_{(0,-1)}=\delta\_{0}\otimes\text{Ra}(1/2) under the standard Wasserstein distance, but limε→0𝒱​(με)=0≠1=𝒱​(μ)\lim\_{\varepsilon\to 0}\mathcal{V}(\mu\_{\varepsilon})=0\neq 1=\mathcal{V}(\mu).

## 4 Proposed method: GG-causal normalizing flows

[Theorem 3.7](https://arxiv.org/html/2510.15458v1#S3.Thmtheorem7 "Theorem 3.7 (Continuity of 𝐺-causal optimization problems). ‣ 3 Robust optimization in Structural Causal Models ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") and [Example 3.8](https://arxiv.org/html/2510.15458v1#S3.Thmtheorem8 "Example 3.8. ‣ 3 Robust optimization in Structural Causal Models ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") imply that generative augmentation models that are not trained under the GG-causal Wasserstein distance may lead to optimizers that severely underperform on GG-causal downstream tasks. To solve this issue, we propose a novel normalizing flow architecture capable of minimizing the GG-causal Wasserstein distance from any data distribution μ∈𝒫G​(ℝd)\mu\in\mathcal{P}\_{G}(\mathbb{R}^{d}). Since the standard, adapted and CO-OT Wasserstein distances are all special cases of the GG-causal Wasserstein distance, this model family provides optimal generative augmentation models for a vast class of empirical applications.

A GG-causal normalizing flow T^=T^(d)∘⋯∘T^(1)\hat{T}=\hat{T}^{(d)}\circ\cdots\circ\hat{T}^{(1)} is a composition of dd neural coupling flows T^(k):ℝd→ℝd\hat{T}^{(k)}:\mathbb{R}^{d}\to\mathbb{R}^{d} of the following form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | T^i(k)​(x)={g​(xi;θ​(xPA​(i)))if i=kidif i≠k\hat{T}^{(k)}\_{i}(x)=\begin{cases}g(x\_{i};\theta(x\_{\text{PA}(i)}))&\text{if $i=k$}\\ \text{id}&\text{if $i\neq k$}\end{cases} |  | (2) |

where g:ℝ×Θ​(n)→ℝg:\mathbb{R}\times\Theta(n)\to\mathbb{R} is a shallow MLP of the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(x,θ)=∑i=1nwi(2)​ρ​(wi(1)​x+bi(1))+b(2)g(x,\theta)=\sum\_{i=1}^{n}w^{(2)}\_{i}\rho(w^{(1)}\_{i}x+b^{(1)}\_{i})+b^{(2)} |  | (3) |

with parameters θ:=(w(1),b(1),w(2),b(2))∈Θ​(n):=ℝ>0n×ℝn×ℝ>0n×ℝ\theta:=(w^{(1)},b^{(1)},w^{(2)},b^{(2)})\in\Theta(n):=\mathbb{R}\_{>0}^{n}\times\mathbb{R}^{n}\times\mathbb{R}\_{>0}^{n}\times\mathbb{R} and custom activation function222Recall that the LeakyReLU activation function is defined as LeakyReLUα​(x):=x​𝟙{x≥0}+α​x​𝟙{x<0}\text{LeakyReLU}\_{\alpha}(x):=x\mathds{1}\_{\{x\geq 0\}}+\alpha x\mathds{1}\_{\{x<0\}}.:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(x)=12​LeakyReLUα−1​(1+x)−12​LeakyReLUα−1​(1−x),α∈(0,1).\rho(x)=\frac{1}{2}\text{LeakyReLU}\_{\alpha-1}(1+x)-\frac{1}{2}\text{LeakyReLU}\_{\alpha-1}(1-x),\quad\alpha\in(0,1). |  | (4) |

We denote by IncrMLP(nn) the class of all MLPs with nn hidden neurons and parameter space Θ​(n)\Theta(n). It is easy to see that IncrMLP​(n)\text{IncrMLP}(n) contains only continuous, piecewise linear, strictly increasing (and, therefore, *invertible*) functions, thanks to the choice of activation function333One cannot just take ρ​(x)=ReLU​(x)\rho(x)=\text{ReLU}(x), because gg could fail to be strictly increasing, nor ρ​(x)=LeakyReLUα​(x)\rho(x)=\text{LeakyReLU}\_{\alpha}(x), because then gg would be constrained to be convex, which harms model capacity. and parameter space. The inverse of gg and its derivative can be computed efficiently, which allows the coupling flow in [Eq. 2](https://arxiv.org/html/2510.15458v1#S4.E2 "In 4 Proposed method: 𝐺-causal normalizing flows ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") to be easily implemented in a normalizing flow model (see code in the supplementary material).

In [Eq. 2](https://arxiv.org/html/2510.15458v1#S4.E2 "In 4 Proposed method: 𝐺-causal normalizing flows ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") we specify the parameters of gg in terms of a function θ​(xPA​(i))\theta(x\_{\text{PA}(i)}), which we take to be an MLP444In practice, we enforce θ​(xPA​(i))∈Θ​(n)\theta(x\_{\text{PA}(i)})\in\Theta(n) by constraining its outputs corresponding to the weights w(1)w^{(1)} and w(2)w^{(2)} to be strictly positive, either by using a ReLU activation function or by taking their absolute value.. The particular choice of MLP class does not matter, as long as the assumptions of (Leshno et al., [1993](https://arxiv.org/html/2510.15458v1#bib.bib15), Theorem 1) are satisfied555The activation function must be non-polynomial and locally essentially bounded on ℝ\mathbb{R}. All commonly used activation functions (including ReLU) satisfy this. and we denote by MLP any such class. Since the outputs of θ​(⋅)∈MLP\theta(\cdot)\in\text{MLP} are used as parameters for another MLP, g​(⋅)g(\cdot), it is common to say that θ​(⋅)\theta(\cdot) is a *hypernetwork* (Chauhan et al., [2024](https://arxiv.org/html/2510.15458v1#bib.bib6)). Therefore we say that the coupling flow in [Eq. 2](https://arxiv.org/html/2510.15458v1#S4.E2 "In 4 Proposed method: 𝐺-causal normalizing flows ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") is a hypercoupling flow and we denote by HyperCpl​(n,θ​(⋅))\text{HyperCpl}(n,\theta(\cdot)) the class of hypercoupling flows with g​(⋅)∈IncrMLP​(n)g(\cdot)\in\text{IncrMLP}(n) and parameter hypernetwork θ​(⋅)∈MLP\theta(\cdot)\in\text{MLP}.

Since each hypercoupling flow in a GG-causal normalizing flow acts only on a subset of the input coordinates it effectively functions as a scale in a multi-scale architecture, thus reducing the computational burden by exploiting our a priori knowledge of the causal DAG GG.

###### Remark 4.1.

We emphasize that the DAG GG is an *input* of our model, not an output. We assume, therefore, that the modeler has estimated the causal skeleton GG, using any of the available methods for causal discovery Nogueira et al. ([2022](https://arxiv.org/html/2510.15458v1#bib.bib17)); Zanga et al. ([2022](https://arxiv.org/html/2510.15458v1#bib.bib25)). On the other hand, we do not require any knowledge of the functional form of the causal mechanisms, which our model will learn directly from data.

Next, we turn to the task of proving that GG-causal normalizing flows are universal approximators for structural causal models.

###### Definition 4.2 (GG-compatible transformation.).

Let GG be a sorted DAG. A map T:ℝd→ℝdT:\mathbb{R}^{d}\to\mathbb{R}^{d} is a GG-compatible transformation if each coordinate Ti​(x)T\_{i}(x) is a function of (xi,xPA​(i))(x\_{i},x\_{\text{PA}(i)}), for all i=1,…,di=1,\ldots,d. Furthermore, a GG-compatible transformation TT is called (strictly) increasing if each coordinate TiT\_{i} is (strictly) increasing in xix\_{i}.

###### Theorem 4.3.

Let μ∈𝒫G​(ℝd)\mu\in\mathcal{P}\_{G}(\mathbb{R}^{d}) be an absolutely continuous distribution. Then there exists a GG-compatible, strictly increasing transformation T:ℝd→ℝdT:\mathbb{R}^{d}\to\mathbb{R}^{d}, such that T#​𝒰​([0,1]d)=μ{T}\_{\#}\mathcal{U}([0,1]^{d})=\mu.

Furthermore, TT is of the form T:=T(d)∘⋯∘T(1)T:=T^{(d)}\circ\cdots\circ T^{(1)}, where each T(k):ℝd→ℝdT^{(k)}:\mathbb{R}^{d}\to\mathbb{R}^{d} is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ti(k)​(x)={Fi−1​(xi|xPA​(i))i=k,idi≠k.(k=1,…,d)T^{(k)}\_{i}(x)=\begin{cases}F^{-1}\_{i}(x\_{i}\>|\>x\_{\text{PA}(i)})&i=k,\\ \text{id}&i\neq k.\end{cases}\quad(k=1,\ldots,d) |  | (5) |

where Fi−1F^{-1}\_{i} is the (conditional) quantile function of the random variable Xi∼μ​(d​xi)X\_{i}\sim\mu(dx\_{i}) given its parents XPA​(i)∼μ​(d​xPA​(i))X\_{\text{PA}(i)}\sim\mu(dx\_{\text{PA}(i)}).

###### Proof.

It is easy to check that TT, as defined, is indeed a GG-compatible, increasing transformation. The absolute continuity of μ\mu implies that all conditional distributions admit a density (Jacod & Protter, [2004](https://arxiv.org/html/2510.15458v1#bib.bib13), Theorem 12.2), therefore a continuous cdf and a strictly monotone quantile function (McNeil et al., [2015](https://arxiv.org/html/2510.15458v1#bib.bib16), Proposition A.3 (ii)).

Next, we show that T#​𝒰​([0,1]d)=μ{T}\_{\#}\mathcal{U}([0,1]^{d})=\mu. By [Definition 2.2](https://arxiv.org/html/2510.15458v1#S2.Thmtheorem2 "Definition 2.2 (G-compatible distribution). ‣ 2.2 𝐺-causal Wasserstein distance ‣ 2 Background ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") we know that there exists X∼μX\sim\mu and measurable functions fif\_{i} such that Xi=fi​(XPA​(i),Ui)X\_{i}=f\_{i}(X\_{\text{PA}}(i),U\_{i}) where U=(U1,…,Ud)U=(U\_{1},\ldots,U\_{d}) is a random vector of mutually independent random variables. Without loss of generality, we can take U∼𝒰​([0,1]d)U\sim\mathcal{U}([0,1]^{d}) and set Xi=Fi−1​(Ui|XPA​(i))X\_{i}=F^{-1}\_{i}(U\_{i}|X\_{\text{PA}}(i)) (McNeil et al., [2015](https://arxiv.org/html/2510.15458v1#bib.bib16), Proposition A.6)).
∎

###### Theorem 4.4 (Universal Approximation Property (UAP) for GG-causal normalizing flows).

Let μ∈𝒫G,1​(ℝd)\mu\in\mathcal{P}\_{G,1}(\mathbb{R}^{d}) be an absolutely continuous distribution with compact support and assume that the conditional cdfs (xk,xPA​(k))↦Fk​(xk|xPA​(k))(x\_{k},x\_{\text{PA}(k)})\mapsto F\_{k}(x\_{k}\>|\>x\_{\text{PA}(k)}) belong to C1​(ℝ×ℝ|PA​(k)|)C^{1}(\mathbb{R}\times\mathbb{R}^{|\text{PA}(k)|}), for all k=1,…,dk=1,\ldots,d.

Then GG-causal normalizing flows with base distribution 𝒰​([0,1]d)\mathcal{U}([0,1]^{d}) are dense in the semi-metric space (𝒫G,1​(ℝd),WG)(\mathcal{P}\_{G,1}(\mathbb{R}^{d}),W\_{G}), i.e. for every ε>0\varepsilon>0, there exists a GG-causal normalizing flow T^\hat{T} such that

|  |  |  |
| --- | --- | --- |
|  | WG(μ,T^#𝒰([0,1]d)≤ε.W\_{G}(\mu,{\hat{T}}\_{\#}\mathcal{U}([0,1]^{d})\leq\varepsilon. |  |

###### Proof.

See proof in [Section B.2](https://arxiv.org/html/2510.15458v1#A2.SS2 "B.2 Proof of Theorem 4.4 ‣ Appendix B Proofs ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows").
∎

###### Remark 4.5.

The theorem holds for base distributions other than 𝒰​([0,1]d)\mathcal{U}([0,1]^{d}). In fact any absolutely continuous distribution on ℝd\mathbb{R}^{d} with mutually independent coordinates (such as the standard multivariate Gaussian 𝒩​(0,Id)\mathcal{N}(0,I\_{d})) would work, provided we add a non-trainable layer between the base distribution and the first flow that maps ℝd\mathbb{R}^{d} into the base distribution’s quantiles (for 𝒩​(0,Id)\mathcal{N}(0,I\_{d}), such a map is just Φ⊗d\Phi^{\otimes d}, where Φ\Phi is the standard Gaussian cdf).

In practice GG-causal normalizing flows are trained using likelihood maximization (or, equivalently, KL minimization), so it is important to make sure that minimizing this loss guarantees that the GG-causal Wasserstein distance between data and model distribution is also minimized. The following result proves exactly this and is a generalization of Acciaio et al. ([2024](https://arxiv.org/html/2510.15458v1#bib.bib1), Lemma 2.3) and Eckstein & Pammer ([2024](https://arxiv.org/html/2510.15458v1#bib.bib11), Lemma 3.5), which established an analogous claim for the adapted Wasserstein distance.

###### Theorem 4.6 (WGW\_{G} training via KL minimization).

Let μ,ν∈𝒫G​(K)\mu,\nu\in\mathcal{P}\_{G}(K) for some compact K⊆ℝdK\subseteq\mathbb{R}^{d}. Then:

|  |  |  |
| --- | --- | --- |
|  | WG​(μ,ν)≤C​12​𝒟K​L​(μ|ν),W\_{G}(\mu,\nu)\leq C\sqrt{\frac{1}{2}\mathcal{D}\_{KL}(\mu\>|\>\nu)}, |  |

for a constant C>0C>0.

###### Proof.

See proof in [Section B.3](https://arxiv.org/html/2510.15458v1#A2.SS3 "B.3 Proof of Theorem 4.6 ‣ Appendix B Proofs ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows").
∎

## 5 Numerical experiments

### 5.1 Causal regression

We study a multivariate causal regression problem of the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minh:ℝ|V∖T|→ℝ|T|h is G-causal⁡𝔼μ​[(XT−h​(XV∖T))2],\min\_{\begin{subarray}{c}h:\mathbb{R}^{|V\setminus T|}\to\mathbb{R}^{|T|}\\ \text{$h$ is $G$-causal}\end{subarray}}\mathbb{E}^{\mu}\left[(X\_{T}-h(X\_{V\setminus T}))^{2}\right], |  | (6) |

where μ∈𝒫G​(ℝd)\mu\in\mathcal{P}\_{G}(\mathbb{R}^{d}) is a randomly generated linear Gaussian SCM (Peters et al., [2017](https://arxiv.org/html/2510.15458v1#bib.bib18), Section 7.1.3) with coefficients uniformly sampled in (−1,1)(-1,1) and homoscedastic noise with unit variance. The sorted DAG GG is obtained by randomly sampling an Erdos-Renyi graph on dd vertices with edge probability pp and eliminating all edges (i,j)(i,j) with i>ji>j.

According to [Theorem 3.5](https://arxiv.org/html/2510.15458v1#S3.Thmtheorem5 "Theorem 3.5 (Robustness of 𝐺-causal optimizers). ‣ 3 Robust optimization in Structural Causal Models ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows"), any solution to problem ([6](https://arxiv.org/html/2510.15458v1#S5.E6 "Equation 6 ‣ 5.1 Causal regression ‣ 5 Numerical experiments ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows")) is interventionally robust. In order to showcase this robustness property of the GG-causal regressor, we compare its performance with that of a standard (i.e. non-causal) regressor when tested out-of-sample on a large number of random soft666A soft intervention at a node i∈Vi\in V leaves its parents and noise distribution unaltered, but changes the functional form of its causal mechanism. interventions. Each intervention is obtained by randomly sampling a node i∈V∖Ti\in V\setminus T and substituting its causal mechanism, f​(XPA​(i),Ui)f(X\_{\text{PA}(i)},U\_{i}), with a new one, f~​(X|PA(i),Ui)\tilde{f}(X\_{|\text{PA}(i)},U\_{i}). We consider only linear interventions and quantify their interventional strength by computing the following L1L^{1}-norm:

|  |  |  |
| --- | --- | --- |
|  | ∫∫|f​(xPA​(i),u)−f~​(xPA​(i),u)|​μ​(d​xPA​(i))​λ​(d​u),\int\int|f(x\_{\text{PA}(i)},u)-\tilde{f}(x\_{\text{PA}(i)},u)|\mu(dx\_{\text{PA}(i)})\lambda(du), |  |

where μ\mu is the original distribution (before intervention) and λ\lambda is the noise distribution. Interventional strength, therefore, quantifies the out-of-sample variation of the regressor’s inputs under the intervention.

We implement a multivariate regression with d=10d=10, p=0.5p=0.5 and T={5,6}T=\{5,6\}. We report in [Fig. 8](https://arxiv.org/html/2510.15458v1#S5.F8 "In 5.1 Causal regression ‣ 5 Numerical experiments ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") and [Fig. 8](https://arxiv.org/html/2510.15458v1#S5.F8 "In 5.1 Causal regression ‣ 5 Numerical experiments ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") the worst-case performance of a GG-causal regressor and of a non-causal regressor (in terms of MSE and R2R^{2}, respectively) as a function of the interventional strength. At small interventional strengths the non-causal regressor benefits from the information contained in non-parent nodes (which are not available as inputs to the GG-causal optimizer). These non-parent nodes may belong to the Markov blanket of the target nodes in GG and therefore be statistically informative, but their usefulness crucially depends on the stability of their causal mechanisms. As the interventional strength is increased the worst-case performance of the non-causal regressor rapidly deteriorates, while that of the GG-causal regressor remains stable, as shown in the figures.

![Refer to caption](x3.png)


Figure 3: Worst-case MSE vs interventional strength.

![Refer to caption](x4.png)


Figure 4: Worst-case R2R^{2} vs interventional strength.

In [Fig. 6](https://arxiv.org/html/2510.15458v1#S5.F6 "In 5.1 Causal regression ‣ 5 Numerical experiments ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") and [Fig. 6](https://arxiv.org/html/2510.15458v1#S5.F6 "In 5.1 Causal regression ‣ 5 Numerical experiments ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") we deepen the comparison by plotting the distribution of the performance metrics (MSE and R2R^{2}, respectively) for both estimators. Notice how interventions deteriorate the performance of the non-causal regressor starting from the least favorable quantiles, while the entire distribution of the performance metrics of the GG-causal remains stable. These figures also show that the median performance of the causal regressor is, after all, not strongly affected by the linear random interventions we consider. In this sense, non-causal optimizers can still be approximately optimal in applications where distributional shifts are expected to be mild.

![Refer to caption](x5.png)


Figure 5: Median and (75%-95%) CI of MSE vs interventional strength.

![Refer to caption](x6.png)


Figure 6: Median and (75%-95%) CI of R2R^{2} vs interventional strength.

Finally, we investigate the performance of our GG-causal normalizing flow model when used for generative data augmentation. We therefore train several augmentation models (both non-causal and GG-causal) on a training set of n=10000n=10000 samples from μ\mu. We then use them to generate of synthetic training set of n=10000n=10000 samples and we train a causal optimizer on it.

As shown in [Fig. 8](https://arxiv.org/html/2510.15458v1#S5.F8 "In 5.1 Causal regression ‣ 5 Numerical experiments ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") and [Fig. 8](https://arxiv.org/html/2510.15458v1#S5.F8 "In 5.1 Causal regression ‣ 5 Numerical experiments ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows"), causal optimizers trained using non-causal augmentation models (e.g. RealNVP and VAE) are indeed robust under interventions, but their worst-case metrics are significantly worse than when causal augmentation is used. This is an empirical validation of the fact that the loss used for training the augmentation model plays a crucial role in downstream performance.

![Refer to caption](x7.png)


Figure 7: Worst-case MSE after generative data augmentation vs interventional strength.

![Refer to caption](x8.png)


Figure 8: Worst-case R2R^{2} after generative data augmentation vs interventional strength.

### 5.2 Conditional mean-variance portfolio optimization

We look at the following conditional mean-variance portfolio optimization problem:

|  |  |  |
| --- | --- | --- |
|  | 𝒱​(μ)=infh:ℝ|V∖T|→ℝ|T|h is G-causal{−𝔼μ​[⟨XT,h​(XV∖T)⟩]+γ2​Varμ​(⟨XT,h​(XV∖T)⟩)},\mathcal{V}(\mu)=\inf\_{\begin{subarray}{c}h:\mathbb{R}^{|V\setminus T|}\to\mathbb{R}^{|T|}\\ \text{$h$ is $G$-causal}\end{subarray}}\left\{-\mathbb{E}^{\mu}\left[\langle X\_{T},h(X\_{V\setminus T})\rangle\right]+\frac{\gamma}{2}\mathrm{Var}^{\mu}\left(\langle X\_{T},h(X\_{V\setminus T})\rangle\right)\right\}, |  |

where X∼μ∈𝒫G​(ℝd)X\sim\mu\in\mathcal{P}\_{G}(\mathbb{R}^{d}) is a linear Gaussian SCM, with bipartite DAG GG with partition {T,V∖T}\{T,V\setminus T\} and random uniform coefficients in (−1,1)(-1,1), and γ\gamma is a given risk aversion parameter. The target variables XTX\_{T} represent stock returns, while XV∖TX\_{V\setminus T} are market factors or trading signals. We present the results for a high-dimensional example with |T|=100|T|=100 stocks and |V∖T|=20|V\setminus T|=20 factors.

We sample random linear interventions exactly as done in the case of causal regression and study empirically the robustness of the GG-causal portfolio in terms of its Sharpe ratio as the interventional strength increases.

[Fig. 10](https://arxiv.org/html/2510.15458v1#S5.F10 "In 5.2 Conditional mean-variance portfolio optimization ‣ 5 Numerical experiments ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") and [Fig. 10](https://arxiv.org/html/2510.15458v1#S5.F10 "In 5.2 Conditional mean-variance portfolio optimization ‣ 5 Numerical experiments ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") show that the Sharpe ratio of the GG-causal portfolio is indeed robust to a wide range of interventions, while the performance of non-causal portfolios deteriorates rapidly, starting from the least favorable quantiles.

![Refer to caption](x9.png)


Figure 9: Worst-case Sharpe ratio vs interventional strength

![Refer to caption](x10.png)


Figure 10: Median and (75%-95%) CI of Sharpe ratio vs interventional strength

Reproducibility statement. All results can be reproduced using the source code provided in the Supplimentary Materials. Demo notebooks of the numerical experiments will be made available in a paper-related GitHub repository upon publication.

## References

* Acciaio et al. (2024)

  Beatrice Acciaio, Stephan Eckstein, and Songyan Hou.
  Time-Causal VAE: Robust Financial Time Series Generator.
  *arXiv preprint arXiv:2411.02947*, 2024.
* Aubin & Frankowska (2009)

  Jean-Pierre Aubin and Hélène Frankowska.
  Set-Valued Analysis, 2009.
* Backhoff-Veraguas et al. (2020)

  Julio Backhoff-Veraguas, Daniel Bartl, Mathias Beiglböck, and Manu Eder.
  Adapted wasserstein distances and stability in mathematical finance.
  *Finance and Stochastics*, 24(3):601–632,
  2020.
* Bailey et al. (2017)

  David Bailey, Jonathan Borwein, Marcos Lopez de Prado, and Qiji Jim Zhu.
  The probability of backtest overfitting.
  *The Journal of Computational Finance*, 20(4):39–69, 2017.
* Bogachev (2007)

  Vladimir I Bogachev.
  *Measure theory*.
  Springer, 2007.
* Chauhan et al. (2024)

  Vinod Kumar Chauhan, Jiandong Zhou, Ping Lu, Soheila Molaei, and David A
  Clifton.
  A brief review of hypernetworks in deep learning.
  *Artificial Intelligence Review*, 57(9):250,
  2024.
* Chen et al. (2020)

  Ruidi Chen, Ioannis Ch Paschalidis, et al.
  Distributionally robust learning.
  *Foundations and Trends® in Optimization*,
  4(1-2):1–243, 2020.
* Chen et al. (2024)

  Yunhao Chen, Zihui Yan, and Yunjie Zhu.
  A comprehensive survey for generative data augmentation.
  *Neurocomputing*, 600:128167, 2024.
* Cheridito & Eckstein (2025)

  Patrick Cheridito and Stephan Eckstein.
  Optimal transport and Wasserstein distances for causal models.
  *Bernoulli*, 31(2):1351–1376, 2025.
* Eckstein & Nutz (2022)

  Stephan Eckstein and Marcel Nutz.
  Quantitative stability of regularized optimal transport and
  convergence of sinkhorn’s algorithm.
  *SIAM Journal on Mathematical Analysis*, 54(6):5922–5948, 2022.
* Eckstein & Pammer (2024)

  Stephan Eckstein and Gudmund Pammer.
  Computational methods for adapted optimal transport.
  *The Annals of Applied Probability*, 34(1A):675–713, 2024.
* Folland (1999)

  Gerald B. Folland.
  *Real Analysis: Modern Techniques and their Applications*.
  John Wiley & Sons, 1999.
* Jacod & Protter (2004)

  Jean Jacod and Philip Protter.
  *Probability Essentials*.
  Springer Science & Business Media, 2004.
* Kuhn et al. (2025)

  Daniel Kuhn, Soroosh Shafiee, and Wolfram Wiesemann.
  Distributionally robust optimization.
  *Acta Numerica*, 34:579–804, 2025.
* Leshno et al. (1993)

  Moshe Leshno, Vladimir Ya Lin, Allan Pinkus, and Shimon Schocken.
  Multilayer feedforward networks with a nonpolynomial activation
  function can approximate any function.
  *Neural networks*, 6(6):861–867, 1993.
* McNeil et al. (2015)

  Alexander J McNeil, Rüdiger Frey, and Paul Embrechts.
  *Quantitative Risk Management: Concepts, Techniques and Tools
  (Revised Edition)*.
  Princeton university press, 2015.
* Nogueira et al. (2022)

  Ana Rita Nogueira, Andrea Pugnana, Salvatore Ruggieri, Dino Pedreschi, and
  João Gama.
  Methods and tools for causal discovery and causal inference.
  *Wiley interdisciplinary reviews: data mining and knowledge
  discovery*, 12(2):e1449, 2022.
* Peters et al. (2017)

  Jonas Peters, Dominik Janzing, and Bernhard Schölkopf.
  *Elements of Causal Inference: Foundations and Learning
  Algorithms*.
  The MIT press, 2017.
* Pflug & Pichler (2012)

  Georg Ch Pflug and Alois Pichler.
  A distance for multistage stochastic optimization models.
  *SIAM Journal on Optimization*, 22(1):1–23,
  2012.
* Pflug & Pichler (2014)

  Georg Ch Pflug and Alois Pichler.
  *Multistage Stochastic Optimization*, volume 1104.
  Springer, 2014.
* Rockafellar & Wets (1998)

  R. Tyrrell Rockafellar and Roger J. B. Wets.
  *Variational Analysis*.
  Springer, 1998.
* Rojas-Carulla et al. (2018)

  Mateo Rojas-Carulla, Bernhard Schölkopf, Richard Turner, and Jonas Peters.
  Invariant Models for Causal Transfer Learning.
  *Journal of Machine Learning Research*, 19(36):1–34, 2018.
* Schumaker (2007)

  Larry Schumaker.
  *Spline Functions: Basic Theory*.
  Cambridge University Press, 2007.
* Xu et al. (2020)

  Tianlin Xu, Li Kevin Wenliang, Michael Munn, and Beatrice Acciaio.
  Cot-gan: Generating sequential data via causal optimal transport.
  *Advances in neural information processing systems*,
  33:8798–8809, 2020.
* Zanga et al. (2022)

  Alessio Zanga, Elif Ozkirimli, and Fabio Stella.
  A survey on causal discovery: theory and practice.
  *International Journal of Approximate Reasoning*, 151:101–129, 2022.
* Zheng et al. (2023)

  Chenyu Zheng, Guoqiang Wu, and Chongxuan Li.
  Toward understanding generative data augmentation.
  *Advances in neural information processing systems*,
  36:54046–54060, 2023.

## Appendix A Auxiliary results

###### Lemma A.1 (Interchangeability principle).

Let (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) be a probability space and let f:Ω×ℝd→ℝ¯f:\Omega\times\mathbb{R}^{d}\to\overline{\mathbb{R}} be an ℱ\mathcal{F}-measurable normal integrand. Then:

|  |  |  |
| --- | --- | --- |
|  | ∫minx∈ℝd⁡f​(ω,x)​ℙ​(d​ω)=minX∈m​ℱ​∫f​(ω,X​(ω))​ℙ​(d​ω),\int\min\_{x\in\mathbb{R}^{d}}f(\omega,x)\mathbb{P}(d\omega)=\min\_{X\in m\mathcal{F}}\int f(\omega,X(\omega))\mathbb{P}(d\omega), |  |

provided that the right-hand side is not ∞\infty.

Furthermore, if both sides are not −∞-\infty, then:

|  |  |  |
| --- | --- | --- |
|  | X∗∈arg​minX∈m​ℱ​∫f​(ω,X​(ω))​ℙ​(d​ω)⟺X∗​(ω)∈arg​minx∈ℝd⁡f​(ω,x),(μ-almost surely)X^{\*}\in\operatorname\*{arg\,min}\_{X\in m\mathcal{F}}\int f(\omega,X(\omega))\mathbb{P}(d\omega)\Longleftrightarrow X^{\*}(\omega)\in\operatorname\*{arg\,min}\_{x\in\mathbb{R}^{d}}f(\omega,x),\>\>\text{($\mu$-almost surely)} |  |

###### Proof.

See Rockafellar & Wets ([1998](https://arxiv.org/html/2510.15458v1#bib.bib21), Theorem 14.60).
∎

###### Lemma A.2 (Composition lemma).

Let (𝒳,∥⋅∥)(\mathcal{X},\|\cdot\|) be a Banach space with its Borel σ\sigma-algebra and let μ(0),…,μ(d)\mu^{(0)},\ldots,\mu^{(d)} be measures defined on it. Given measurable maps T^(k):𝒳→𝒳\hat{T}^{(k)}:\mathcal{X}\to\mathcal{X} and T(k):𝒳→𝒳T^{(k)}:\mathcal{X}\to\mathcal{X} such that T(k)#​μ(k−1)=μ(k){T^{(k)}}\_{\#}\mu^{(k-1)}=\mu^{(k)} (for k=1,…,dk=1,\ldots,d), if the following two conditions hold:

1. i)

   T^(k)\hat{T}^{(k)} is LkL\_{k}-Lipschitz,
2. ii)

   ‖T(k)−T^(k)‖Lp​(μ(k−1))≤εk\|T^{(k)}-\hat{T}^{(k)}\|\_{L^{p}(\mu^{(k-1)})}\leq\varepsilon\_{k},

then:

|  |  |  |
| --- | --- | --- |
|  | ‖T(d)∘⋯∘T(1)−T^(d)∘⋯∘T^(1)‖Lp​(λ)≤∑k=1dεk​∏j=k+1dLj,\|T^{(d)}\circ\cdots\circ T^{(1)}-\hat{T}^{(d)}\circ\cdots\circ\hat{T}^{(1)}\|\_{L^{p}(\lambda)}\leq\sum\_{k=1}^{d}\varepsilon\_{k}\prod\_{j=k+1}^{d}L\_{j}, |  |

with the convention that ∏j∈∅Lj:=1.\prod\_{j\in\emptyset}L\_{j}:=1.

###### Proof.

The claim follows by induction. It is obviously true for d=1d=1. Assume that it holds for d−1d-1, then for dd:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ‖T(d)∘⋯∘T(1)−T^(d)∘⋯∘T^(1)‖Lp​(μ(0))\displaystyle\|T^{(d)}\circ\cdots\circ T^{(1)}-\hat{T}^{(d)}\circ\cdots\circ\hat{T}^{(1)}\|\_{L^{p}(\mu^{(0)})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ‖T(d)∘T(d−1)∘⋯∘T(1)−T^(d)∘T(d−1)∘⋯∘T(1)‖Lp​(μ(0))+\displaystyle\|T^{(d)}\circ T^{(d-1)}\circ\cdots\circ T^{(1)}-\hat{T}^{(d)}\circ T^{(d-1)}\circ\cdots\circ T^{(1)}\|\_{L^{p}(\mu^{(0)})}+ |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ‖T^(d)∘T(d−1)∘⋯∘T(1)−T^(d)∘T^(d−1)∘⋯∘T^(1)‖Lp​(μ(0))\displaystyle\|\hat{T}^{(d)}\circ T^{(d-1)}\circ\cdots\circ T^{(1)}-\hat{T}^{(d)}\circ\hat{T}^{(d-1)}\circ\cdots\circ\hat{T}^{(1)}\|\_{L^{p}(\mu^{(0)})} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ‖T(d)−T^(d)‖Lp​(μ(d−1))+Ld​‖T(d−1)∘⋯∘T(1)−T^(d−1)∘⋯∘T^(1)‖Lp​(μ(0))\displaystyle\|T^{(d)}-\hat{T}^{(d)}\|\_{L^{p}(\mu^{(d-1)})}+L\_{d}\|T^{(d-1)}\circ\cdots\circ T^{(1)}-\hat{T}^{(d-1)}\circ\cdots\circ\hat{T}^{(1)}\|\_{L^{p}(\mu^{(0)})} |  | (Change of variable + Lipschitz) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | εd+Ld⋅∑k=1d−1εk​∏j=k+1d−1Lj\displaystyle\varepsilon\_{d}+L\_{d}\cdot\sum\_{k=1}^{d-1}\varepsilon\_{k}\prod\_{j=k+1}^{d-1}L\_{j} |  | (claim holds of d−1d-1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑k=1dεk​∏j=k+1dLj\displaystyle\sum\_{k=1}^{d}\varepsilon\_{k}\prod\_{j=k+1}^{d}L\_{j} |  |

∎

###### Lemma A.3.

Let g∈IncrMLP​(n)g\in\text{IncrMLP}(n) with parameter space Θ​(n)\Theta(n). Then the map θ↦g​(⋅;θ)\theta\mapsto g(\cdot;\theta) from Θ​(n)\Theta(n) to L1​([0,1])L^{1}([0,1]) is continuous.

###### Proof.

It is a direct application of Lebesgue’s dominated convergence theorem (Bogachev, [2007](https://arxiv.org/html/2510.15458v1#bib.bib5), Theorem 2.8.1), so we just verify that the assumptions of the theorem hold. Let θk→θ∈Θ\theta\_{k}\to\theta\in\Theta be any convergent sequence. Since θ↦g​(u;θ)\theta\mapsto g(u;\theta) is continuous, we have that g​(u;θk)→g​(u;θ)g(u;\theta\_{k})\to g(u;\theta) for all u∈[0,1]u\in[0,1]. Furthermore, the functions g​(⋅;θk)g(\cdot;\theta\_{k}) are uniformly bounded:

|  |  |  |  |
| --- | --- | --- | --- |
|  | supk∈ℕ|g​(u;θk)|\displaystyle\sup\_{k\in\mathbb{N}}|g(u;\theta\_{k})| | ≤supk∈ℕsupu∈[0,1]|g​(u;θk)|\displaystyle\leq\sup\_{k\in\mathbb{N}}\sup\_{u\in[0,1]}|g(u;\theta\_{k})| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤supk∈ℕmax⁡{|g​(0;θk)|,|g​(1;θk)|}\displaystyle\leq\sup\_{k\in\mathbb{N}}\max\{|g(0;\theta\_{k})|,|g(1;\theta\_{k})|\} |  | (u↦g​(u;θ)u\mapsto g(u;\theta) is increasing) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤supθ∈Kmax⁡{|g​(0;θ)|,|g​(1;θ)|}\displaystyle\leq\sup\_{\theta\in K}\max\{|g(0;\theta)|,|g(1;\theta)|\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <+∞\displaystyle<+\infty |  |

where K⊆ΘK\subseteq\Theta is any compact containing the sequence {θk,k∈ℕ}\{\theta\_{k},k\in\mathbb{N}\} (which exists because the sequence is convergent) and the last inequality follows from the fact that θ↦max⁡{|g​(0;θ)|,|g​(1;θ)|}\theta\mapsto\max\{|g(0;\theta)|,|g(1;\theta)|\} is continuous (it’s the minimum of two continuous functions) and therefore bounded on KK.
∎

###### Lemma A.4.

Let R⊆ℝkR\subseteq\mathbb{R}^{k} be a compact set and let the functions f​(⋅,x):[a,b]→ℝf(\cdot,x):[a,b]\to\mathbb{R} be continuous, linear splines on a common grid a=u1<…<un+1=ba=u\_{1}<\ldots<u\_{n+1}=b, for every x∈Rx\in R. Then there exists a subset Θ⊆Θ​(n)\Theta\subseteq\Theta(n) (which depends only on the grid) such that the set-valued function θ~:R⇉Θ\tilde{\theta}:R\rightrightarrows\Theta, defined by

|  |  |  |
| --- | --- | --- |
|  | θ~(xPA​(k)):=arg​minθ′∈Θ∥f^(⋅,xPA​(k))−g(⋅,θ′))∥L1​([0,1]),∀xPA​(k)∈R\tilde{\theta}(x\_{\text{PA}(k)}):=\operatorname\*{arg\,min}\_{\theta^{\prime}\in\Theta}\;\|\hat{f}(\cdot,x\_{\text{PA}(k)})-g(\cdot,\theta^{\prime}))\|\_{L^{1}([0,1])},\quad\forall x\_{\text{PA}(k)}\in R |  |

admits a continuous selection θ:R→Θ\theta:R\to\Theta, such that g​(u,θ​(x))=f^​(u,x)g(u,\theta(x))=\hat{f}(u,x) for all u∈[0,1]u\in[0,1].

###### Proof.

The existence of a continuous selection follows from Michael’s theorem (Aubin & Frankowska, [2009](https://arxiv.org/html/2510.15458v1#bib.bib2), Theorem 9.1.2), provided we can show that θ~\tilde{\theta} is lower semi-continuous with closed and convex values.

Lower-semicontinuity actually holds regardless of the choice of the set Θ\Theta, so we prove it first. It follows from the fact that that (xPA​(k),θ)↦∥f^(u,xPA​(k))−g(u;θ′))∥L1​([0,1])(x\_{\text{PA}(k)},\theta)\mapsto\|\hat{f}(u,x\_{\text{PA}(k)})-g(u;\theta^{\prime}))\|\_{L^{1}([0,1])} is a Carathéodory function (for a definition, see Rockafellar & Wets ([1998](https://arxiv.org/html/2510.15458v1#bib.bib21), Example 14.29)) and therefore a normal integrand (Rockafellar & Wets, [1998](https://arxiv.org/html/2510.15458v1#bib.bib21), Definition 14.27, Proposition 14.28). Indeed:

* •

  Since (u,xPA​(k))↦|f^(u,xPA​(k))−g(u;θ))|(u,x\_{\text{PA}(k)})\mapsto|\hat{f}(u,x\_{\text{PA}(k)})-g(u;\theta))| is measurable (even continuous) for all θ∈Θ\theta\in\Theta, Tonelli’s theorem (Folland, [1999](https://arxiv.org/html/2510.15458v1#bib.bib12), Theorem 2.37) implies that x↦∥f^(⋅,x)−g(⋅;θ))∥L1​([0,1])x\mapsto\|\hat{f}(\cdot,x)-g(\cdot;\theta))\|\_{L^{1}([0,1])} is measurable.
* •

  The map θ↦h​(xPA​(k),θ)\theta\mapsto h(x\_{\text{PA}(k)},\theta) is continuous for all xPA​(k)∈ℝ|PA​(k)|x\_{\text{PA}(k)}\in\mathbb{R}^{|\text{PA}(k)|} because it’s the composition of two continuous maps: θ↦g​(⋅;θ)∈L1​([0,1])\theta\mapsto g(\cdot;\theta)\in L^{1}([0,1]), which is continuous by [Lemma A.3](https://arxiv.org/html/2510.15458v1#A1.Thmtheorem3 "Lemma A.3. ‣ Appendix A Auxiliary results ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows"), and g(⋅;θ)↦∥f^(⋅,x)−g(⋅;θ))∥L1​([0,1])g(\cdot;\theta)\mapsto\|\hat{f}(\cdot,x)-g(\cdot;\theta))\|\_{L^{1}([0,1])}, which is continuous because the norm is a continuous function.

We will now show that θ~\tilde{\theta} is actually singleton valued (which, of course, implies that it is closed and convex valued), by constructing a suitable set Θ⊆Θ​(n)\Theta\subseteq\Theta(n). The main strategy is to realize that the weights and biases of the first layer (w(1)w^{(1)} and b(1)b^{(1)}) can be used to fully specify the segments on which the function u↦g​(u,θ)u\mapsto g(u,\theta) is piecewise linear and that, once this choice is made, the weights and the bias of the second layer (w(2)w^{(2)} and b(2)b^{(2)}) determine *uniquely* the slope and intercepts on each segment.

More specifically, given the grid a=u1<u2<…<un+1=ba=u\_{1}<u\_{2}<\ldots<u\_{n+1}=b, denote by

|  |  |  |
| --- | --- | --- |
|  | Δ​ui:=ui+1−ui\Delta u\_{i}:=u\_{i+1}-u\_{i} and mi:=12​(ui+1+ui)m\_{i}:=\frac{1}{2}(u\_{i+1}+u\_{i}),  (i=1,…,ni=1,\ldots,n) |  |

the width and the midpoint of each grid segment, respectively. If we set

|  |  |  |
| --- | --- | --- |
|  | w¯i(1)=2/Δ​ui\bar{w}^{(1)}\_{i}=2/\Delta u\_{i},  b¯i(1)=−mi​Δ​ui\bar{b}^{(1)}\_{i}=-m\_{i}\Delta u\_{i},  (i=1,…,ni=1,\ldots,n) |  |

and define Θ:={w¯(1)}×{b¯(1)}×ℝ>0n×ℝ⊆Θ​(n)\Theta:=\{\bar{w}^{(1)}\}\times\{\bar{b}^{(1)}\}\times\mathbb{R}\_{>0}^{n}\times\mathbb{R}\subseteq\Theta(n), then g​(⋅,θ)g(\cdot,\theta) is piecewise linear exactly on the grid {ui}i=1n+1\{u\_{i}\}\_{i=1}^{n+1}, for any θ∈Θ\theta\in\Theta. Additionally on each segment [ui,ui+1][u\_{i},u\_{i+1}], the function g​(⋅,θ)g(\cdot,\theta) has slope

|  |  |  |
| --- | --- | --- |
|  | wi(2)​(w¯i(1)+α2​∑j≠iw¯j(1))w^{(2)}\_{i}\left(\bar{w}^{(1)}\_{i}+\frac{\alpha}{2}\sum\_{j\neq i}\bar{w}^{(1)}\_{j}\right) |  |

and bias

|  |  |  |
| --- | --- | --- |
|  | wi(2)​b¯i(1)+n​b(2)+(n−1)​α2​wj(2)​b¯j(1)+(α2−1)​(∑j<iwj(2)−∑j>iwj(2)).w^{(2)}\_{i}\bar{b}^{(1)}\_{i}+nb^{(2)}+(n-1)\frac{\alpha}{2}w^{(2)}\_{j}\bar{b}^{(1)}\_{j}+\left(\frac{\alpha}{2}-1\right)\left(\sum\_{j<i}w^{(2)}\_{j}-\sum\_{j>i}w^{(2)}\_{j}\right). |  |

We can therefore exactly match any continuous, strictly increasing, piecewise linear function on the grid {ui}i=1n+1\{u\_{i}\}\_{i=1}^{n+1} by matching the slope and intercept on [u1,u2][u\_{1},u\_{2}], together with the slopes on each of the remaining segments (the intercepts will be automatically matched by continuity). This is a linear system of n+1n+1 equations in n+1n+1 unknowns and it always admits a unique solution (as can be readily checked), which implies that for every x∈Rx\in R we can find a θ∈Θ\theta\in\Theta such that g​(u,θ)=f^​(u,x)g(u,\theta)=\hat{f}(u,x) for all u∈[a,b]u\in[a,b].
∎

###### Lemma A.5.

Let g∈IncrMLP​(n)g\in\text{IncrMLP}(n). Then θ↦g​(u,θ)\theta\mapsto g(u,\theta) is locally Lipschitz uniformly in u∈[0,1]u\in[0,1], i.e. for every compact K⊆Θ​(n)K\subseteq\Theta(n) there exists an L>0L>0 such that:

|  |  |  |
| --- | --- | --- |
|  | |g​(u,θ)−g​(u,θ′)|≤L​‖θ−θ^‖,∀θ,θ^∈K,∀u∈[0,1].|g(u,\theta)-g(u,\theta^{\prime})|\leq L\|\theta-\hat{\theta}\|,\quad\forall\theta,\hat{\theta}\in K,\;\forall u\in[0,1]. |  |

###### Proof.

The proof follows by direct computation. We use repeatedly the Cauchy-Schwartz inequality, the fact that the activation ρ\rho is 1-Lipschitz and that ‖u‖≤1\|u\|\leq 1:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |g​(u,θ)−g​(u,θ^)|≤\displaystyle|g(u,\theta)-g(u,\hat{\theta})|\leq | |⟨w(2),ρ⊗n​(u​w(1)+b(1))⟩+b(2)−⟨w^(2),ρ⊗n​(u​w^(1)+b^(1))⟩−b^(2)|\displaystyle|\langle w^{(2)},\rho^{\otimes n}(uw^{(1)}+b^{(1)})\rangle+b^{(2)}-\langle\hat{w}^{(2)},\rho^{\otimes n}(u\hat{w}^{(1)}+\hat{b}^{(1)})\rangle-\hat{b}^{(2)}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | |⟨w(2),ρ⊗n​(u​w(1)+b(1))⟩−⟨w^(2),ρ⊗n​(u​w(1)+b(1))⟩|\displaystyle|\langle w^{(2)},\rho^{\otimes n}(uw^{(1)}+b^{(1)})\rangle-\langle\hat{w}^{(2)},\rho^{\otimes n}(uw^{(1)}+b^{(1)})\rangle| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +|⟨w^(2),ρ⊗n​(u​w(1)+b(1))⟩−⟨w^(2),ρ⊗n​(u​w^(1)+b^(1))⟩|+|b(2)−b^(2)|\displaystyle+|\langle\hat{w}^{(2)},\rho^{\otimes n}(uw^{(1)}+b^{(1)})\rangle-\langle\hat{w}^{(2)},\rho^{\otimes n}(u\hat{w}^{(1)}+\hat{b}^{(1)})\rangle|+|b^{(2)}-\hat{b}^{(2)}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | |⟨w(2)−w^(2),ρ⊗n​(u​w(1)+b(1))⟩|\displaystyle|\langle w^{(2)}-\hat{w}^{(2)},\rho^{\otimes n}(uw^{(1)}+b^{(1)})\rangle| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +|⟨w^(2),ρ⊗n​(u​w(1)+b(1))−ρ⊗n​(u​w^(1)+b^(1))⟩|+|b(2)−b^(2)|\displaystyle+|\langle\hat{w}^{(2)},\rho^{\otimes n}(uw^{(1)}+b^{(1)})-\rho^{\otimes n}(u\hat{w}^{(1)}+\hat{b}^{(1)})\rangle|+|b^{(2)}-\hat{b}^{(2)}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ‖w(2)−w^(2)‖​‖ρ⊗n​(u​w(1)+b(1))‖\displaystyle\|w^{(2)}-\hat{w}^{(2)}\|\|\rho^{\otimes n}(uw^{(1)}+b^{(1)})\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +‖w^(2)‖​‖ρ⊗n​(u​w(1)+b(1))−ρ⊗n​(u​w^(1)+b^(1))‖+|b(2)−b^(2)|\displaystyle+\|\hat{w}^{(2)}\|\|\rho^{\otimes n}(uw^{(1)}+b^{(1)})-\rho^{\otimes n}(u\hat{w}^{(1)}+\hat{b}^{(1)})\|+|b^{(2)}-\hat{b}^{(2)}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ∥w(2)−w^(2)∥(∥w(1)∥+∥b(1))∥)+∥w^(2)∥(∥w(1)−w^(1)∥+∥b(1)−b^(1)∥+|b(2)−b^(2)|)\displaystyle\|w^{(2)}-\hat{w}^{(2)}\|(\|w^{(1)}\|+\|b^{(1)})\|)+\|\hat{w}^{(2)}\|(\|w^{(1)}-\hat{w}^{(1)}\|+\|b^{(1)}-\hat{b}^{(1)}\|+|b^{(2)}-\hat{b}^{(2)}|) |  |

Since the parameters are contained in a compact KK, their norms are bounded by a constant, say M>0M>0, so that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |g​(u,θ)−g​(u,θ^)|\displaystyle|g(u,\theta)-g(u,\hat{\theta})| | ≤2​M​(‖w(2)−w^(2)‖+‖w(1)−w^(1)‖+‖b(1)−b^(1)‖+|b(2)−b^(2)|)\displaystyle\leq 2M(\|w^{(2)}-\hat{w}^{(2)}\|+\|w^{(1)}-\hat{w}^{(1)}\|+\|b^{(1)}-\hat{b}^{(1)}\|+|b^{(2)}-\hat{b}^{(2)}|) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​M​4​‖θ−θ^‖\displaystyle\leq 2M\sqrt{4}\|\theta-\hat{\theta}\| |  |

where the last inequality is due to Cauchy-Schwartz (this time applied to the (four-dimensional) vector of parameters’ norms and the four-dimensional unit vector).
∎

###### Lemma A.6.

Let (u,xPA​(k))↦Fk−1​(u|xPA​(k))(u,x\_{\text{PA}}(k))\mapsto F^{-1}\_{k}(u\>|\>x\_{\text{PA}(k)}) be as in [Theorem 4.4](https://arxiv.org/html/2510.15458v1#S4.Thmtheorem4 "Theorem 4.4 (Universal Approximation Property (UAP) for 𝐺-causal normalizing flows). ‣ 4 Proposed method: 𝐺-causal normalizing flows ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows"). Then:

1. i)

   Fk−1​(u|xPA​(k))∈L1​(d​u⊗μ​(d​xPA​(k)))F\_{k}^{-1}(u\>|\>x\_{\text{PA}(k)})\in L^{1}(du\otimes\mu(dx\_{\text{PA}(k)})),
2. ii)

   ∂uFk−1​(u|xPA​(k))∈L1​(d​u⊗μ​(d​xPA​(k)))\partial\_{u}F\_{k}^{-1}(u\>|\>x\_{\text{PA}(k)})\in L^{1}(du\otimes\mu(dx\_{\text{PA}(k)})),
3. iii)

   ∂xjFk−1​(u|xPA​(k))∈L1​(d​u⊗μ​(d​xPA​(k)))\partial\_{x\_{j}}F\_{k}^{-1}(u\>|\>x\_{\text{PA}(k)})\in L^{1}(du\otimes\mu(dx\_{\text{PA}(k)})), for all j∈PA​(k)j\in\text{PA}(k).

###### Proof.

1. i)

   By direct integration:

   |  |  |  |
   | --- | --- | --- |
   |  | ∫ℝ|PA​(k)|μ(dxPA​(k))∫[0,1]du|Fk−1(u|xPA​(k))|\displaystyle\int\_{\mathbb{R}^{|\text{PA}(k)|}}\mu(dx\_{\text{PA}(k)})\int\_{[0,1]}du|F\_{k}^{-1}(u\>|\>x\_{\text{PA}(k)})| |  |
   |  |  |  |
   | --- | --- | --- |
   |  | =∫ℝ|PA​(k)|μ​(d​xPA​(k))​∫ℝμ​(d​xk|xPA​(k))​|xk|\displaystyle=\int\_{\mathbb{R}^{|\text{PA}(k)|}}\mu(dx\_{\text{PA}(k)})\int\_{\mathbb{R}}\mu(dx\_{k}\>|\>x\_{\text{PA}(k)})|x\_{k}| |  |
   |  |  |  |
   | --- | --- | --- |
   |  | =∫ℝμ​(d​xk)​|xk|≤+∞\displaystyle=\int\_{\mathbb{R}}\mu(dx\_{k})|x\_{k}|\leq+\infty |  |

   where we have first used the change-of-variable formula (Bogachev, [2007](https://arxiv.org/html/2510.15458v1#bib.bib5), Theorem 3.6.1) with Fk−1(⋅|xPA​(k))#𝒰[0,1]=μ(dxk|xPA​(k)){F\_{k}^{-1}(\cdot\>|\>x\_{\text{PA}(k)})}\_{\#}\mathcal{U}[0,1]=\mu(dx\_{k}\>|\>x\_{\text{PA}(k)}) (McNeil et al., [2015](https://arxiv.org/html/2510.15458v1#bib.bib16), Proposition A.6) and then used the fact that μ\mu has finite first moments.
2. ii)

   u↦F−1​(u|x)u\mapsto F^{-1}(u\>|\>x) is increasing on the closed interval [0,1][0,1], therefore by Bogachev ([2007](https://arxiv.org/html/2510.15458v1#bib.bib5), Corollary 5.2.7) it is almost everywhere differentiable and:
   ∫\_[0,1] —∂\_u F\_k^-1(u   —  x\_PA(k))— du ≤F\_k^-1(1   —  x\_PA(k)) - F\_k^-1(0   —  x\_PA(k)).
   The right-hand side is just diam​(supp​(μ​(d​xk|xPA​(k))))\text{diam}(\mathrm{supp}(\mu(dx\_{k}\>|\>x\_{\text{PA}(k)}))), which is finite, since μ\mu is compactly supported.
3. iii)

   Continuity of u↦Fk​(u|xPA​(k))u\mapsto F\_{k}(u\>|\>x\_{\text{PA}(k)}) implies that Fk​(Fk−1​(u|xPA​(k)))=uF\_{k}(F\_{k}^{-1}(u\>|\>x\_{\text{PA}(k)}))=u (McNeil et al., [2015](https://arxiv.org/html/2510.15458v1#bib.bib16), Proposition A.3 (viii)). Differentiating this expression on both sides and using the chain rule yields:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∫[0,1]|∂xjFk−1(u|xPA​(k))|du\displaystyle\int\_{[0,1]}\left|\partial\_{x\_{j}}F\_{k}^{-1}(u\>|\>x\_{\text{PA}(k)})\right|du | =∫[0,1]𝑑u​|−∂xjFk​(Fk−1​(u|xPA​(k))|xPA​(k))∂uFk​(Fk−1​(u|xPA​(k))|xPA​(k))|\displaystyle=\int\_{[0,1]}du\left|-\frac{\partial\_{x\_{j}}F\_{k}(F\_{k}^{-1}(u\>|\>x\_{\text{PA}(k)})\>|\>x\_{\text{PA}(k)})}{\partial\_{u}F\_{k}(F\_{k}^{-1}(u\>|\>x\_{\text{PA}(k)})\>|\>x\_{\text{PA}(k)})}\right| |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =∫ℝdx′|−∂xjFk(x′|xPA​(k))|,\displaystyle=\int\_{\mathbb{R}}dx^{\prime}\left|-\partial\_{x\_{j}}F\_{k}(x^{\prime}\>|\>x\_{\text{PA}(k)})\right|, |  |

   where the second equality follows from the same change-of-variable as in part (i) and by simplifying the conditional density.
   The claim now follows by integrating over ℝPA​(k)\mathbb{R}^{\text{PA}(k)} with respect to μ​(d​xPA​(k))\mu(dx\_{\text{PA}(k)}) and using the assumption that (xk,xPA​(k))↦Fk​(xk|xPA​(k))(x\_{k},x\_{\text{PA}(k)})\mapsto F\_{k}(x\_{k}\>|\>x\_{\text{PA}(k)}) is a C1C^{1} map and therefore admits bounded partial derivatives on compacts.

∎

## Appendix B Proofs

### B.1 Proof of [Theorem 3.7](https://arxiv.org/html/2510.15458v1#S3.Thmtheorem7 "Theorem 3.7 (Continuity of 𝐺-causal optimization problems). ‣ 3 Robust optimization in Structural Causal Models ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows")

###### Proof.

We generalize the proof by Acciaio et al. ([2024](https://arxiv.org/html/2510.15458v1#bib.bib1)) to our GG-causal setting. Given μ,ν∈𝒫G​(ℝd)\mu,\nu\in\mathcal{P}\_{G}(\mathbb{R}^{d}), let gg be a GG-causal function and let π\pi be the optimal GG-bicausal coupling between μ\mu and ν\nu. Then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −𝔼ν​[Q​(XT,g​(XV∖T))]\displaystyle-\mathbb{E}^{\nu}\left[Q(X\_{T},g(X\_{V\setminus T}))\right] | =−∫Q​(xT′,g​(xV∖T′))​ν​(d​x′)\displaystyle=-\int Q(x^{\prime}\_{T},g(x^{\prime}\_{V\setminus T}))\nu(dx^{\prime}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∫Q​(xT′,g​(xV∖T′))​π​(d​x,d​x′)\displaystyle=-\int Q(x^{\prime}\_{T},g(x^{\prime}\_{V\setminus T}))\pi(dx,dx^{\prime}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫(Q​(xT,g​(xV∖T′))−Q​(xT′,g​(xV∖T′)))​π​(d​x,d​x′)−∫Q​(xT,g​(xV∖T′))​π​(d​x,d​x′)\displaystyle=\int\left(Q(x\_{T},g(x^{\prime}\_{V\setminus T}))-Q(x^{\prime}\_{T},g(x^{\prime}\_{V\setminus T}))\right)\pi(dx,dx^{\prime})-\int Q(x\_{T},g(x^{\prime}\_{V\setminus T}))\pi(dx,dx^{\prime}) |  |

Since x↦Q​(x,g)x\mapsto Q(x,g) is uniformly locally LL-Lipschitz, the first integral satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫(Q​(xT,g​(xV∖T′))−Q​(xT′,g​(xV∖T′)))​π​(d​x,d​x′)\displaystyle\int\left(Q(x\_{T},g(x^{\prime}\_{V\setminus T}))-Q(x^{\prime}\_{T},g(x^{\prime}\_{V\setminus T}))\right)\pi(dx,dx^{\prime}) | ≤L​∫‖xT−xT′‖​π​(d​x,d​x′)\displaystyle\leq L\int\|x\_{T}-x^{\prime}\_{T}\|\pi(dx,dx^{\prime}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤L​∫‖x−x′‖​π​(d​x,d​x′)\displaystyle\leq L\int\|x-x^{\prime}\|\pi(dx,dx^{\prime}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =L⋅WG​(μ,ν)\displaystyle=L\cdot W\_{G}(\mu,\nu) |  |

For the second integral, we notice that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∫Q​(xT,g​(xV∖T′))​π​(d​x,d​x′)\displaystyle-\int Q(x\_{T},g(x^{\prime}\_{V\setminus T}))\pi(dx,dx^{\prime}) | ≤−∫Q​(xT,∫g​(xV∖T′)​π​(d​x′|x))​μ​(d​x)\displaystyle\leq-\int Q\bigg(x\_{T},\int g(x^{\prime}\_{V\setminus T})\pi(dx^{\prime}\>|\>x)\bigg)\mu(dx) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∫Q​(xT,∫g​(xPA​(T)′)​π​(d​x′|x)⏟h​(x))​μ​(d​x)\displaystyle=-\int Q\bigg(x\_{T},\underbrace{\int g(x^{\prime}\_{\text{PA}(T)})\pi(dx^{\prime}\>|\>x)}\_{h(x)}\bigg)\mu(dx) |  |

where we first applied Jensen’s inequality and then the fact that gg is GG-causal. Furthermore, since π\pi is GG-causal, the function h​(x):=∫g​(xV∖T′)​π​(d​x′|x)h(x):=\int g(x^{\prime}\_{V\setminus T})\pi(dx^{\prime}\>|\>x) actually depends only on xPA​(T)∪PA​(PA​(T))x\_{\text{PA}(T)\cup\text{PA}(\text{PA}(T))}. To ease the notation, denote A:=PA​(T)∪PA​(PA​(T))A:=\text{PA}(T)\cup\text{PA}(\text{PA}(T)). Then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∫Q​(xT,h​(xA))​μ​(d​x)\displaystyle-\int Q\left(x\_{T},h(x\_{A})\right)\mu(dx) | =−∫μ​(d​xA)​∫μ​(d​xT|xA)​Q​(xT,h​(xA))\displaystyle=-\int\mu(dx\_{A})\int\mu(dx\_{T}\>|\>x\_{A})Q(x\_{T},h(x\_{A})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∫μ​(d​xA)​∫μ​(d​xT|xPA​(T))​Q​(xT,h​(xA))\displaystyle=-\int\mu(dx\_{A})\int\mu(dx\_{T}\>|\>x\_{\text{PA}(T)})Q(x\_{T},h(x\_{A})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤−∫μ​(d​xA)​∫μ​(d​xT|xPA​(T))​Q​(xT,h∗​(xPA​(T)))\displaystyle\leq-\int\mu(dx\_{A})\int\mu(dx\_{T}\>|\>x\_{\text{PA}(T)})Q(x\_{T},h^{\*}(x\_{\text{PA}(T)})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−𝒱​(μ)\displaystyle=-\mathcal{V}(\mu) |  |

where in the second equality we have used the fact that XT⟂⟂XA|XPA​(T)X\_{T}\perp\!\!\!\perp X\_{A}\>|\>X\_{\text{PA}(T)} (see condition (ii) in [Definition 2.2](https://arxiv.org/html/2510.15458v1#S2.Thmtheorem2 "Definition 2.2 (G-compatible distribution). ‣ 2.2 𝐺-causal Wasserstein distance ‣ 2 Background ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") or simply notice that XPA​(T)X\_{\text{PA}(T)} dd-separates XTX\_{T} and XPA​(PA​(T))X\_{\text{PA}(\text{PA}(T))}), while the inequality is due to [Eq. 1](https://arxiv.org/html/2510.15458v1#S3.E1 "In Definition 3.4 (𝐺-causal optimization problem). ‣ 3 Robust optimization in Structural Causal Models ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows").

Putting everything together:

|  |  |  |
| --- | --- | --- |
|  | −𝔼ν​[Q​(Y,g​(X))]≤L⋅WG​(μ,ν)−𝒱​(μ)-\mathbb{E}^{\nu}\left[Q(Y,g(X))\right]\leq L\cdot W\_{G}(\mu,\nu)-\mathcal{V}(\mu) |  |

and, since gg is arbitrary, we obtain:

|  |  |  |
| --- | --- | --- |
|  | 𝒱​(μ)−𝒱​(ν)≤L⋅WG​(μ,ν).\mathcal{V}(\mu)-\mathcal{V}(\nu)\leq L\cdot W\_{G}(\mu,\nu). |  |

By symmetry, exchanging μ\mu and ν\nu yields the same inequality for the term 𝒱​(ν)−𝒱​(μ)\mathcal{V}(\nu)-\mathcal{V}(\mu), therefore

|  |  |  |
| --- | --- | --- |
|  | |𝒱​(μ)−𝒱​(ν)|≤L⋅WG​(μ,ν).|\mathcal{V}(\mu)-\mathcal{V}(\nu)|\leq L\cdot W\_{G}(\mu,\nu). |  |

∎

### B.2 Proof of [Theorem 4.4](https://arxiv.org/html/2510.15458v1#S4.Thmtheorem4 "Theorem 4.4 (Universal Approximation Property (UAP) for 𝐺-causal normalizing flows). ‣ 4 Proposed method: 𝐺-causal normalizing flows ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows")

###### Proof.

We know that μ=T#​𝒩​(0,Id)\mu={T}\_{\#}\mathcal{N}(0,I\_{d}), where T=T(d)∘⋯∘T(1)T=T^{(d)}\circ\cdots\circ T^{(1)} is the GG-compatible, increasing transformation in the statement of [Theorem 4.3](https://arxiv.org/html/2510.15458v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4 Proposed method: 𝐺-causal normalizing flows ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows"). Now, let T^=T^(d)∘⋯∘T^(1)∈G​-NF​(d)\hat{T}=\hat{T}^{(d)}\circ\cdots\circ\hat{T}^{(1)}\in G\text{-}\text{NF}(d) be a G-NFwith flows as in [Eq. 2](https://arxiv.org/html/2510.15458v1#S4.E2 "In 4 Proposed method: 𝐺-causal normalizing flows ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") and define the GG-bicausal coupling π:=(T,T^)#​𝒩​(0,1)\pi:={(T,\hat{T})}\_{\#}\mathcal{N}(0,1), then we have that:

|  |  |  |
| --- | --- | --- |
|  | WG​(μ,T^#​λ)≤∫ℝd×ℝd‖x−x′‖​π​(d​x,d​x′)=∫[0,1]d‖T​(u)−T^​(u)‖​𝑑u.W\_{G}(\mu,{\hat{T}}\_{\#}\lambda)\leq\int\_{\mathbb{R}^{d}\times\mathbb{R}^{d}}\|x-x^{\prime}\|\pi(dx,dx^{\prime})=\int\_{[0,1]^{d}}\|T(u)-\hat{T}(u)\|du. |  |

We can make the right-hand side smaller than any ε>0\varepsilon>0 by using [Lemma A.2](https://arxiv.org/html/2510.15458v1#A1.Thmtheorem2 "Lemma A.2 (Composition lemma). ‣ Appendix A Auxiliary results ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") (with 𝒳:=[0,1]d\mathcal{X}:=[0,1]^{d}, μ(0):=𝒰​([0,1]d)\mu^{(0)}:=\mathcal{U}([0,1]^{d}) and μ(k):=μ1:k⊗𝒰​([0,1]d−k)\mu^{(k)}:=\mu\_{1:k}\otimes\mathcal{U}([0,1]^{d-k}), for k=1,…,dk=1,\ldots,d), provided that we can show that conditions (i) and (ii) therein hold.

Condition (i). Each hypercoupling flow T^(k)\hat{T}^{(k)} differs from the identity only at its kk-th coordinate, which is the output of a shallow MLP (see [Eq. 2](https://arxiv.org/html/2510.15458v1#S4.E2 "In 4 Proposed method: 𝐺-causal normalizing flows ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows")) . But shallow MLPs are Lipschitz functions of their input, therefore each T^(k)\hat{T}^{(k)} is a Lipschitz function.

Condition (ii). We need to show that for every ε>0\varepsilon>0, there exists an n∈ℕn\in\mathbb{N}, a θ^​(⋅)∈MLP\hat{\theta}(\cdot)\in\text{MLP} and a g​(⋅,θ^​(xPA​(k)))∈IncrMLP​(n)g(\cdot,\hat{\theta}(x\_{\text{PA}(k)}))\in\text{IncrMLP}(n) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫[0,1]du∫ℝ|PA​(k)|μ(dxPA​(k))|Fk−1(u|xPA​(k))−g(u;θ^(xPA​(k)))|≤ε.\int\_{[0,1]}du\int\_{\mathbb{R}^{|\text{PA}(k)|}}\mu(dx\_{\text{PA}(k)})|F^{-1}\_{k}(u\>|\>x\_{\text{PA}(k)})-g(u;\hat{\theta}(x\_{\text{PA}(k)}))|\leq\varepsilon. |  | (7) |

We will prove this bound by splitting the error into three terms and bounding each one separately.

Term 1. First we approximate (u,xPA​(k))↦Fk−1​(u|xPA​(k))(u,x\_{\text{PA}}(k))\mapsto F^{-1}\_{k}(u\>|\>x\_{\text{PA}(k)}) with a continuous tensor-product linear spline, f^​(u,xPA​(k))\hat{f}(u,x\_{\text{PA}(k)}), on the rectangle [0,1]×R[0,1]\times R, where R=∏j=1|PA​(k)|[aj,bj]R=\prod\_{j=1}^{|\text{PA}(k)|}[a\_{j},b\_{j}] is a rectangle large enough to contain the compact support of μ​(d​xPA​(k))\mu(dx\_{\text{PA}(k)}). We choose the approximation grid fine enough to satisfy:

|  |  |  |
| --- | --- | --- |
|  | ∫[0,1]du∫ℝ|PA​(k)|μ(dxPA​(k))|Fk−1(u|xPA​(k))−f^(u,xPA​(k))|≤ε/2,\int\_{[0,1]}du\int\_{\mathbb{R}^{|\text{PA}(k)|}}\mu(dx\_{\text{PA}(k)})|F^{-1}\_{k}(u\>|\>x\_{\text{PA}(k)})-\hat{f}(u,x\_{\text{PA}(k)})|\leq\varepsilon/2, |  |

and let n+1n+1 be the number of gridpoints in the uu-axis (i.e. the grid on [0,1][0,1] has gridpoints 0=u1<…<un+1=1)0=u\_{1}<\ldots<u\_{n+1}=1).

The validity of this approximation follows from (Schumaker, [2007](https://arxiv.org/html/2510.15458v1#bib.bib23), Theorem 12.7) and requires that (u,x)↦F−1​(u|x)(u,x)\mapsto F^{-1}(u|x) belong to a suitable tensor Sobolev space (Schumaker, [2007](https://arxiv.org/html/2510.15458v1#bib.bib23), Example 13.5), as we verify in [Lemma A.6](https://arxiv.org/html/2510.15458v1#A1.Thmtheorem6 "Lemma A.6. ‣ Appendix A Auxiliary results ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows").

Term 2. Next, we approximate the univariate functions u↦f^​(u,xPA​(k))u\mapsto\hat{f}(u,x\_{\text{PA}(k)}), for each xPA​(k)∈Rx\_{\text{PA}(k)}\in R, with neural networks g​(⋅;θ​(xPA​(k)))∈IncrMLP​(n)g(\cdot;\theta(x\_{\text{PA}(k)}))\in\text{IncrMLP}(n), by judiciously choosing the function θ:R→Θ​(n)\theta:R\to\Theta(n).

Since all the functions f^​(⋅,xPA​(k))\hat{f}(\cdot,x\_{\text{PA}(k)}) share the same grid on [0,1][0,1], by [Lemma A.4](https://arxiv.org/html/2510.15458v1#A1.Thmtheorem4 "Lemma A.4. ‣ Appendix A Auxiliary results ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows") there exists a parameter subset Θ⊆Θ​(n)\Theta\subseteq\Theta(n) (which depends only on this grid) such that the set-valued map θ~:R⇉Θ\tilde{\theta}:R\rightrightarrows\Theta, defined as

|  |  |  |
| --- | --- | --- |
|  | θ~(xPA​(k)):=arg​minθ′∈Θ∥f^(⋅,xPA​(k))−g(⋅,θ′))∥L1​([0,1]),\tilde{\theta}(x\_{\text{PA}(k)}):=\operatorname\*{arg\,min}\_{\theta^{\prime}\in\Theta}\;\|\hat{f}(\cdot,x\_{\text{PA}(k)})-g(\cdot,\theta^{\prime}))\|\_{L^{1}([0,1])}, |  |

admits a continuous selection θ:R→Θ\theta:R\rightarrow\Theta. We then use this function θ\theta to parametrize the neural networks g​(⋅,θ​(xPA​(k)))g(\cdot,\theta(x\_{\text{PA}(k)})) and, as implied by [Lemma A.4](https://arxiv.org/html/2510.15458v1#A1.Thmtheorem4 "Lemma A.4. ‣ Appendix A Auxiliary results ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows"), this parametrization is optimal, in the sense that g​(u,θ​(xPA​(k)))=f^​(u,xPA​(k))g(u,\theta(x\_{\text{PA}(k)}))=\hat{f}(u,x\_{\text{PA}(k)}) for all u∈[0,1]u\in[0,1], thus achieving zero approximation zero, i.e.

|  |  |  |
| --- | --- | --- |
|  | ∫[0,1]𝑑u​∫ℝ|PA​(k)|μ​(d​xPA​(k))​|f^​(u,xPA​(k))−g​(u,θ​(xPA​(k)))|=0.\int\_{[0,1]}du\int\_{\mathbb{R}^{|\text{PA}(k)|}}\mu(dx\_{\text{PA}(k)})|\hat{f}(u,x\_{\text{PA}(k)})-g(u,\theta(x\_{\text{PA}(k)}))|=0. |  |

Term 3. Finally, we approximate g​(u;θ​(xPA​(k)))g(u;\theta(x\_{\text{PA}(k)})) with g​(u;θ^​(xPA​(k)))g(u;\hat{\theta}(x\_{\text{PA}(k)})), where θ^​(⋅)\hat{\theta}(\cdot) is a suitable MLP.

Since θ:R→Θ\theta:R\to\Theta is a continuous function on a compact, we have that θ∈L1​(μ)\theta\in L^{1}(\mu), therefore for every ε′>0\varepsilon^{\prime}>0 there is an MLP777For the theorem to hold we only need the activation function to be non-polynomial and locally essentially bounded (such as ReLU). θ^\hat{\theta} such that ‖θ−θ^‖L1​(μ)≤ε′\|\theta-\hat{\theta}\|\_{L^{1}(\mu)}\leq\varepsilon^{\prime} (Leshno et al., [1993](https://arxiv.org/html/2510.15458v1#bib.bib15), Proposition 1).

Therefore:

|  |  |  |
| --- | --- | --- |
|  | ∫[0,1]𝑑u​∫ℝ|PA​(k)|μ​(d​xPA​(k))​|g​(u;θ​(xPA​(k)))−g​(u;θ^​(xPA​(k)))|\displaystyle\int\_{[0,1]}du\int\_{\mathbb{R}^{|\text{PA}(k)|}}\mu(dx\_{\text{PA}(k)})|g(u;\theta(x\_{\text{PA}(k)}))-g(u;\hat{\theta}(x\_{\text{PA}(k)}))| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫[0,1]du∫ℝ|PA​(k)|μ(dxPA​(k))L||θ(xPA​(k))−θ^(xPA​(k))∥\displaystyle\leq\int\_{[0,1]}du\int\_{\mathbb{R}^{|\text{PA}(k)|}}\mu(dx\_{\text{PA}(k)})L\>||\theta(x\_{\text{PA}(k)})-\hat{\theta}(x\_{\text{PA}(k)})\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤L​ε′≤ε/2\displaystyle\leq L\varepsilon^{\prime}\leq\varepsilon/2 |  | (choose ε′=ε/2​L\varepsilon^{\prime}=\varepsilon/2L) |

where the first inequality follows from the uniform local Lipschitz property on the compact θ​(supp​(μ))∪θ^​(supp​(μ))\theta(\mathrm{supp}(\mu))\cup\hat{\theta}(\mathrm{supp}(\mu)) proved in [Lemma A.5](https://arxiv.org/html/2510.15458v1#A1.Thmtheorem5 "Lemma A.5. ‣ Appendix A Auxiliary results ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows").

Summing all three approximation errors together, we obtain the bound in [Eq. 7](https://arxiv.org/html/2510.15458v1#A2.E7 "In B.2 Proof of Theorem 4.4 ‣ Appendix B Proofs ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows").
∎

### B.3 Proof of [Theorem 4.6](https://arxiv.org/html/2510.15458v1#S4.Thmtheorem6 "Theorem 4.6 (𝑊_𝐺 training via KL minimization). ‣ 4 Proposed method: 𝐺-causal normalizing flows ‣ Robust Optimization in Causal Models and 𝐺-Causal Normalizing Flows")

###### Proof.

First we notice that

|  |  |  |  |
| --- | --- | --- | --- |
|  | WG​(μ,ν)\displaystyle W\_{G}(\mu,\nu) | =minπ∈ΠGbc​(μ,ν)​∫ℝd×ℝd‖x−x′‖​π​(d​x,d​x′)\displaystyle=\min\_{\pi\in\Pi\_{G}^{\text{bc}}(\mu,\nu)}\int\_{\mathbb{R}^{d}\times\mathbb{R}^{d}}\|x-x^{\prime}\|\,\pi(dx,dx^{\prime}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤minπ∈ΠGbc​(μ,ν)​∫ℝd×ℝddiam​(K)⋅𝟏{x≠x′},π​(d​x,d​x′)\displaystyle\leq\min\_{\pi\in\Pi\_{G}^{\text{bc}}(\mu,\nu)}\int\_{\mathbb{R}^{d}\times\mathbb{R}^{d}}\textrm{diam}(K)\cdot\mathbf{1}\_{\{x\neq x^{\prime}\}},\pi(dx,dx^{\prime}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =:diam(K)⋅dG​-​T​V(μ,ν)\displaystyle=:\textrm{diam}(K)\cdot d\_{G\text{-}TV}(\mu,\nu) |  |

where in the last equality we have introduced the GG-causal total variation distance, dG​-​T​V​(⋅,⋅)d\_{G\text{-}TV}(\cdot,\cdot), as a suitable generalization of the total variation distance for GG-bicausal couplings.

The claim then follows by showing that dG​-​T​V​(μ,ν)≤(2d−1)​dT​V​(μ,ν)d\_{G\text{-}TV}(\mu,\nu)\leq(2^{d}-1)d\_{TV}(\mu,\nu) for all sorted DAGs GG by induction on the number of vertices, which is a straightfoward but tedious generalization of Eckstein & Pammer ([2024](https://arxiv.org/html/2510.15458v1#bib.bib11), Lemma 3.5) to our GG-causal setting.

The claim holds trivially if GG has only one vertex (all couplings are GG-bicausal). Suppose now the claim is true for all sorted DAGs on nn vertices. Then for a sorted DAG GG on n+1n+1 vertices, denote by GnG\_{n} its subgraph on vertices {1,…,n}\{1,\ldots,n\}. We start with some definitions. Define:

|  |  |  |
| --- | --- | --- |
|  | η​(d​xn+1|xPA​(n+1)):=μ​(d​xn+1|xPA​(n+1))∧ν​(d​xn+1|xPA​(n+1)),\eta(dx\_{n+1}|x\_{\text{PA}(n+1)}):=\mu(dx\_{n+1}|x\_{\text{PA}(n+1)})\wedge\nu(dx\_{n+1}|x\_{\text{PA}(n+1)}), |  |

|  |  |  |
| --- | --- | --- |
|  | π∈ΠGbc​(μ,ν)​as​π:=πn⊗π​(d​xn+1,d​xn+1′|xPA​(n+1),xPA​(n+1)′),\pi\in\Pi\_{G}^{\text{bc}}(\mu,\nu)\;\text{as}\;\pi:=\pi\_{n}\otimes\pi(dx\_{n+1},dx^{\prime}\_{n+1}\>|\>x\_{\text{PA}(n+1)},x^{\prime}\_{\text{PA}(n+1)}), |  |

where πn∈ΠGnbc​(μ​(d​x1:n),ν​(d​x1:n′))\pi\_{n}\in\Pi\_{G\_{n}}^{\text{bc}}(\mu(dx\_{1:n}),\nu(dx^{\prime}\_{1:n})), and:

|  |  |  |
| --- | --- | --- |
|  | π​(d​xn+1,d​xn+1′|xPA​(n+1),xPA​(n+1)′):={σ​(d​xn+1,d​xn+1′|xPA​(n+1),xPA​(n+1)′)if xPA​(n+1)=xPA​(n+1)′μ​(d​xn+1|xPA​(n+1))⊗ν​(d′​xn+1|xPA​(n+1)′)otherwise\pi(dx\_{n+1},dx^{\prime}\_{n+1}\>|\>x\_{\text{PA}(n+1)},x^{\prime}\_{\text{PA}(n+1)}):=\begin{cases}\sigma(dx\_{n+1},dx^{\prime}\_{n+1}|x\_{\text{PA}(n+1)},x^{\prime}\_{\text{PA}(n+1)})&\text{if $x\_{\text{PA}(n+1)}=x^{\prime}\_{\text{PA}(n+1)}$}\\ \mu(dx\_{n+1}\>|\>x\_{\text{PA}(n+1)})\otimes\nu(d^{\prime}x\_{n+1}\>|\>x^{\prime}\_{\text{PA}(n+1)})&\text{otherwise}\end{cases} |  |

where σ\sigma is the optimal coupling for the (conditional) total variation distance, i.e.:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ​(d​xn+1,d​xn+1′|xPA​(n+1),xPA​(n+1)′):=\displaystyle\sigma(dx\_{n+1},dx^{\prime}\_{n+1}|x\_{\text{PA}(n+1)},x^{\prime}\_{\text{PA}(n+1)}):= | (id,id)#η(dxn+1|xPA​(n+1))+(μ(dxn+1|xPA​(n+1))\displaystyle(\text{id},\text{id})\_{\#}\eta(dx\_{n+1}|x\_{\text{PA}(n+1)})+(\mu(dx\_{n+1}|x\_{\text{PA}(n+1)}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −η(dxn+1|xPA​(n+1)))⊗(ν(dxn+1|xPA​(n+1))−η(dxn+1|xPA​(n+1)))\displaystyle-\eta(dx\_{n+1}|x\_{\text{PA}(n+1)}))\otimes(\nu(dx\_{n+1}\>|\>x\_{\text{PA}(n+1)})-\eta(dx\_{n+1}|x\_{\text{PA}(n+1)})) |  |

Then the following bounds can be established (see Eckstein & Pammer ([2024](https://arxiv.org/html/2510.15458v1#bib.bib11), Lemma 3.5) for step-by-step details):

|  |  |  |  |
| --- | --- | --- | --- |
|  | dG​-​T​V​(μ,ν)≤\displaystyle d\_{G\text{-}TV}(\mu,\nu)\leq | ∫𝟏{x≠x′}​π​(d​x,d​x′)\displaystyle\int\mathbf{1}\_{\{x\neq x^{\prime}\}}\pi(dx,dx^{\prime}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∫𝟏{x1:n≠x1:n′}​πn​(d​x1:n,d​x1:n′)\displaystyle\int\mathbf{1}\_{\{x\_{1:n}\neq x^{\prime}\_{1:n}\}}\pi\_{n}(dx\_{1:n},dx^{\prime}\_{1:n}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫dT​V​(μ​(d​xn+1|xPA​(n+1)),ν​(d​xn+1|xPA​(n+1)))​𝟏{x1:n=x1:n′}​πn​(d​x1:n,d​x1:n′)\displaystyle+\int d\_{TV}(\mu(dx\_{n+1}|x\_{\text{PA}(n+1)}),\nu(dx\_{n+1}|x\_{\text{PA}(n+1)}))\mathbf{1}\_{\{x\_{1:n}=x^{\prime}\_{1:n}\}}\pi\_{n}(dx\_{1:n},dx^{\prime}\_{1:n}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∫𝟏{x1:n≠x1:n′}πn(dx1:n,dx1:n′)+∥η⊗(μ(dxn+1|xPA​(n+1))−ν(dxn+1|xPA​(n+1)))∥T​V\displaystyle\int\mathbf{1}\_{\{x\_{1:n}\neq x^{\prime}\_{1:n}\}}\pi\_{n}(dx\_{1:n},dx^{\prime}\_{1:n})+\|\eta\otimes(\mu(dx\_{n+1}|x\_{\text{PA}(n+1)})-\nu(dx\_{n+1}|x\_{\text{PA}(n+1)}))\|\_{TV} |  |

For all A∈ℝn+1A\in\mathbb{R}^{n+1}, one has:

|  |  |  |  |
| --- | --- | --- | --- |
|  | η⊗(μ​(d​xn+1|xPA​(n+1))−ν​(d​xn+1|xPA​(n+1)))​(A)≤\displaystyle\eta\otimes(\mu(dx\_{n+1}|x\_{\text{PA}(n+1)})-\nu(dx\_{n+1}|x\_{\text{PA}(n+1)}))(A)\leq | ∥μ(dxn+1|xPA​(n+1))−ν(dxn+1|xPA​(n+1))∥T​V\displaystyle\|\mu(dx\_{n+1}|x\_{\text{PA}(n+1)})-\nu(dx\_{n+1}|x\_{\text{PA}(n+1)})\|\_{TV} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫𝟏{x1:n≠x1:n′}​πn​(d​x1:n,d​x1:n′)\displaystyle+\int\mathbf{1}\_{\{x\_{1:n}\neq x^{\prime}\_{1:n}\}}\pi\_{n}(dx\_{1:n},dx^{\prime}\_{1:n}) |  |

Putting the two bounds together and minimizing over all GnG\_{n}-bicausal couplings πn\pi\_{n}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dG​-​T​V​(μ,ν)≤\displaystyle d\_{G\text{-}TV}(\mu,\nu)\leq | 2​dGn-TV​(μ1:n,ν1:n)+dT​V​(μ,ν)\displaystyle 2d\_{\text{$G\_{n}$-TV}}(\mu\_{1:n},\nu\_{1:n})+d\_{TV}(\mu,\nu) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (2n+1−2+1)​dT​V​(μ,ν)\displaystyle(2^{n+1}-2+1)d\_{TV}(\mu,\nu) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (2n+1−1)​dT​V​(μ,ν)\displaystyle(2^{n+1}-1)d\_{TV}(\mu,\nu) |  |

where we have used:

|  |  |  |
| --- | --- | --- |
|  | dGn-TV​(μ1:n,ν1:n)≤(2n−1)​dT​V​(μ1:n,ν1:n)≤(2n−1)​dT​V​(μ,ν),d\_{\text{$G\_{n}$-TV}}(\mu\_{1:n},\nu\_{1:n})\leq(2^{n}-1)d\_{TV}(\mu\_{1:n},\nu\_{1:n})\leq(2^{n}-1)d\_{TV}(\mu,\nu), |  |

which follows from the induction hypothesis and the data pre-processing inequality for the total variation distance (Eckstein & Nutz, [2022](https://arxiv.org/html/2510.15458v1#bib.bib10), Lemma 4.1).
∎