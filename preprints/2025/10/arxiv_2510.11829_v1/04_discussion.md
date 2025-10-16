---
authors:
- Jin Ma
- Ying Tan
- Renyuan Xu
doc_id: arxiv:2510.11829v1
family_id: arxiv:2510.11829
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Schrödinger bridge for generative AI: Soft-constrained formulation and convergence
  analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama
  Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s
  60th birthday'
url_abs: http://arxiv.org/abs/2510.11829v1
url_html: https://arxiv.org/html/2510.11829v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jin Ma,  Ying Tan,  and
Renyuan Xu
Department of Mathematics, University of Southern California, Los Angeles, CA, 90089.
Email: jinma@usc.edu. This author is supported in part by US NSF grants DMS#2205972 and #2510403.
Department of Statistics and Applied Probability, University of California, Santa Barbara, CA 93106. Email: yingtan@ucsb.edu.Department of Management of Science & Engineering, Stanford University, Stanford, CA 94305. Email: renyuanxu@stanford.edu. This author is supported in part by the NSF CAREER Award DMS-2524465.

(October 13, 2025)

###### Abstract

Generative AI can be framed as the problem of learning a model that maps simple reference measures into complex data distributions, and it has recently found a strong connection to the classical theory of the Schrödinger bridge problems (SBPs)
due partly to their common nature of interpolating between prescribed marginals via entropy-regularized stochastic dynamics. However, the classical SBP enforces hard terminal constraints, which often leads to instability in practical implementations, especially in high-dimensional or data-scarce regimes.
To address this challenge, we follow the idea of the so-called soft-constrained Schrödinger bridge problem(SCSBP), in which the terminal constraint is replaced by a general penalty function. This relaxation leads to a more flexible stochastic control formulation of McKean–Vlasov type.

We establish the existence of optimal solutions for all penalty levels and prove that, as the penalty grows, both the controls and value functions converge to those of the classical SBP at a linear rate. Our analysis builds on Doob’s hh-transform representations, the stability results of Schrödinger potentials, Γ\Gamma-convergence, and a novel fixed-point argument that couples an optimization problem over the space of measures with an auxiliary entropic optimal transport problem. These results not only provide the first quantitative convergence guarantees for soft-constrained bridges but also shed light on how penalty regularization enables robust generative modeling, fine-tuning, and transfer learning.

Keywords. Schrödinger bridge, soft-constrained Schrödinger bridge, entropic optimal transport stability, Schrödinger potentials, generative AI, hh-transform, converse of Scheffé’s Theorem, Γ\Gamma-convergence, Schauder’s fixed-point.

2020 AMS Mathematics subject classification: 60H10, 60J60, 49J21, 68T01, 93E20.

## 1 Introduction

Generative modeling provides a powerful framework for synthesizing data that preserves the statistical structure of real-world samples while introducing controlled variability. Among the most prominent approaches, diffusion models — such as those introduced by [[55](https://arxiv.org/html/2510.11829v1#bib.bib55), [57](https://arxiv.org/html/2510.11829v1#bib.bib57), [58](https://arxiv.org/html/2510.11829v1#bib.bib58), [36](https://arxiv.org/html/2510.11829v1#bib.bib36)] — have achieved remarkable success, underpinning state-of-the-art systems like DALL·E 2 and 3 [[51](https://arxiv.org/html/2510.11829v1#bib.bib51), [6](https://arxiv.org/html/2510.11829v1#bib.bib6)], Stable Diffusion [[53](https://arxiv.org/html/2510.11829v1#bib.bib53)], and Sora [[47](https://arxiv.org/html/2510.11829v1#bib.bib47)]. These models learn to reverse a diffusion process that gradually adds noise to data, enabling the generation of realistic samples from pure noise. Such a structure, namely, transforming a noise distribution into a data distribution, closely mirrors the Schrödinger bridge problem (or dynamic optimal transport), which has recently gained renewed attention as a principled framework for generative modeling due to its structural parallels with diffusion models and its ability to interpolate between distributions in a statistically grounded manner.

The Schrödinger bridge problem (SBP for short), originally proposed as an entropy-regularized variant of optimal transport, seeks the most likely evolution of a process, subject to a reference diffusion process, that matches prescribed marginal distributions μini,μtar{\mu\_{\rm ini}},{\mu\_{\rm tar}} at two endpoints. Under suitable regularity conditions, the optimally controlled process remains a diffusion but with an additional drift term added to the reference process. This result has been established through various approaches and levels of generality, with seminal contributions by [[26](https://arxiv.org/html/2510.11829v1#bib.bib26), [7](https://arxiv.org/html/2510.11829v1#bib.bib7), [37](https://arxiv.org/html/2510.11829v1#bib.bib37), [25](https://arxiv.org/html/2510.11829v1#bib.bib25), [18](https://arxiv.org/html/2510.11829v1#bib.bib18)].

The recent generative modeling literature has seen a surge in the use of Schrödinger bridges. In these applications, one typically starts or chooses some distribution μini{\mu\_{\rm ini}} that is easy to sample from, and tries to "learn" an unknown distribution μtar{\mu\_{\rm tar}} of a given data set. By numerically approximating the solution to the Schrödinger bridge problem, one can generate unlimited samples (i.e., synthetic data points that resemble the original data set). One such algorithm is presented by De Bortoli et al. [[20](https://arxiv.org/html/2510.11829v1#bib.bib20)] and Vargas et al. [[64](https://arxiv.org/html/2510.11829v1#bib.bib64)], who approximate the iterative proportional fitting procedure (Deming-Stephan [[21](https://arxiv.org/html/2510.11829v1#bib.bib21)]), using score matching with neural networks and maximum likelihood, respectively.
Concurrently, Wang et al. [[66](https://arxiv.org/html/2510.11829v1#bib.bib66)] proposed a two-stage method with an auxiliary bridge handling possible non-smooth μtar{\mu\_{\rm tar}}. Some more recent developments include
[[13](https://arxiv.org/html/2510.11829v1#bib.bib13), [56](https://arxiv.org/html/2510.11829v1#bib.bib56), [49](https://arxiv.org/html/2510.11829v1#bib.bib49), [52](https://arxiv.org/html/2510.11829v1#bib.bib52), [67](https://arxiv.org/html/2510.11829v1#bib.bib67), [32](https://arxiv.org/html/2510.11829v1#bib.bib32), [63](https://arxiv.org/html/2510.11829v1#bib.bib63), [54](https://arxiv.org/html/2510.11829v1#bib.bib54), [62](https://arxiv.org/html/2510.11829v1#bib.bib62), [2](https://arxiv.org/html/2510.11829v1#bib.bib2)] as well as developing optimal transport techniques for generative AI tasks [[44](https://arxiv.org/html/2510.11829v1#bib.bib44), [5](https://arxiv.org/html/2510.11829v1#bib.bib5), [42](https://arxiv.org/html/2510.11829v1#bib.bib42), [68](https://arxiv.org/html/2510.11829v1#bib.bib68), [1](https://arxiv.org/html/2510.11829v1#bib.bib1)].

However, the classical SBP imposes hard terminal constraints on the marginal distributions, which can result in computational difficulties, instability in high-dimensional settings, and limited adaptability when aligning with empirical data in generative tasks. In practice, most numerical schemes for solving the SBP rely on iterative procedures that alternately relax the initial and terminal constraints. These algorithms can exhibit instability, particularly when the two constraints differ significantly, and their convergence guarantees for general target distributions remain an open problem in the literature.

In this paper, in light of Garg et al. [[29](https://arxiv.org/html/2510.11829v1#bib.bib29)], we study a soft-constrained Schrödinger bridge problem (SCSBP).
Mathematically, we consider a (smooth) penalty function G:𝒫2​(ℝd)↦ℝ+G:\mathscr{P}\_{2}(\mathbb{R}^{d})\mapsto\mathbb{R}\_{+}, satisfying G​(μ;μtar)=0G(\mu;{\mu\_{\rm tar}})=0,
where 𝒫2​(ℝd)\mathscr{P}\_{2}(\mathbb{R}^{d}) denotes the 2-Wasserstein space on ℝd\mathbb{R}^{d}, and μtar∈𝒫2​(ℝd){\mu\_{\rm tar}}\in\mathscr{P}\_{2}(\mathbb{R}^{d}) is some given “target” distribution. For each k∈ℕk\in\mathbb{N} and a given initial distribution μini∈𝒫2​(ℝd){\mu\_{\rm ini}}\in\mathscr{P}\_{2}(\mathbb{R}^{d}), we consider the following stochastic control problem with dynamics:

|  |  |  |
| --- | --- | --- |
|  | d​Xtα=(b​(t,Xtα)+σ​(t)​αt)​d​t+σ​(t)​d​Wt,ℙ∘(X0α)−1=μini,dX^{\alpha}\_{t}=\big(b(t,X^{\alpha}\_{t})+\sigma(t)\alpha\_{t}\big)dt+\sigma(t)dW\_{t},\quad\mathbb{P}\circ(X\_{0}^{\alpha})^{-1}={\mu\_{\rm ini}}, |  |

and cost functional

|  |  |  |
| --- | --- | --- |
|  | Jk​(α)=𝔼​[12​∫0T|αs|2​𝑑s+k​G​(ℙXTα)],J^{k}(\alpha)=\mathbb{E}\left[\frac{1}{2}\int\_{0}^{T}|\alpha\_{s}|^{2}ds+kG(\mathbb{P}\_{X^{\alpha}\_{T}})\right], |  |

where ℙXTα\mathbb{P}\_{X^{\alpha}\_{T}} is the law of XTαX^{\alpha}\_{T} and the control α\alpha is chosen from a square-integrable progressively measurable admissible control set 𝒜{\cal A}. The goal is to find Vk:=infα∈𝒜Jk​(α)V^{k}:=\inf\_{\alpha\in{\cal A}}J^{k}(\alpha) and optimal control αk\alpha^{k}, for each k∈ℕk\in\mathbb{N}, and study the limiting behavior of {αk}\{\alpha^{k}\} and {Vk}\{V^{k}\}.
Clearly, the dependence of the terminal cost on ℙXTα\mathbb{P}\_{X^{\alpha}\_{T}} renders this relaxed formulation a non-standard stochastic control problem, leading to a McKean-Vlasov type of stochastic control. In contrast to Garg et al. [[29](https://arxiv.org/html/2510.11829v1#bib.bib29)], which focuses on the case where the penalty
GG is given by the KL divergence and
μini\mu\_{\rm ini} is a delta measure, we investigate the problem under more general cost functions and initial distributions.

Compared to existing methods using SBP under hard constraints, there are several advantages to considering SCSBP. First, when the KL divergence between μtar{\mu\_{\rm tar}} and ℙXTα\mathbb{P}\_{X^{\alpha}\_{T}} is infinite, the Schrödinger bridge does not admit a solution, whereas SCSBP always does Garg et al. [[29](https://arxiv.org/html/2510.11829v1#bib.bib29)]. More importantly, the penalty parameter kk acts as a regularization factor, preventing the algorithm from overfitting to μtar\mu\_{\rm tar}, which is crucial for certain generative modeling tasks with limited data [[30](https://arxiv.org/html/2510.11829v1#bib.bib30), [45](https://arxiv.org/html/2510.11829v1#bib.bib45)]. In addition, SCSBP provides a more general framework in generative AI, with applications beyond pre-training in data generation, and can be applied to fine-tuning and transfer learning (see Examples [2.6](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem6 "Example 2.6 (Fine-tuning under a reward signal). ‣ Applications in Generative AI. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and [2.7](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem7 "Example 2.7 (Transfer learning). ‣ Applications in Generative AI. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")).

### 1.1 Outline of the Main Results and Contributions

The soft-constrained Schrödinger bridge problem (SCSBP) studied in this paper replaces the terminal distribution constraint by a general penalty function, which leads to a McKean–Vlasov type stochastic control problem. The main results include the existence of the optimal solution to the SCSBP at each penalty level kk, and the convergence of the solutions to the SCSBP to that of the SBP, in terms
of both the optimal policy and the corresponding value function, as k→∞k\to\infty.

More precisely, we begin with the special case where the initial measure is a delta measure. In this setting, we derive the explicit form of the optimal control policy for SCSBP via Doob’s hh-transform (Proposition [3.6](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem6 "Proposition 3.6. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) and more importantly, we establish a linear convergence rate for the optimal control (Theorem [4.1](https://arxiv.org/html/2510.11829v1#S4.ThmTheorem1 "Theorem 4.1. ‣ 4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). To the best of our knowledge, such a rate of convergence is novel in the literature. Moreover, by applying the so-called early stopping, we are able to obtain the linear convergence results for the corresponding value functions (Proposition [4.4](https://arxiv.org/html/2510.11829v1#S4.ThmTheorem4 "Proposition 4.4. ‣ 4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) as well as the Wasserstein distance between the target distribution and the output distribution of the SCSBP (Proposition [4.5](https://arxiv.org/html/2510.11829v1#S4.ThmTheorem5 "Proposition 4.5. ‣ 4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")).

The similar results in the case of a general initial distribution is much more involved. Among other things, we establish and/or extend some recently observed stability results of the solutions to the SBP, as the foundation for a fixed-point argument. A key element in our argument is the continuous dependence (or stability) of a mapping that is well known in the (static) optimal transport literature. Specifically, for any (μini,μtar)∈𝒫2​(ℝd)×𝒫2​(ℝd)({\mu\_{\rm ini}},{\mu\_{\rm tar}})\in\mathscr{P}\_{2}(\mathbb{R}^{d})\times\mathscr{P}\_{2}(\mathbb{R}^{d}), it is known (cf. e.g., [[7](https://arxiv.org/html/2510.11829v1#bib.bib7)]) that there exists a unique pair of σ\sigma-finite measures (ν0,ν):=𝒯​(μini,μtar)(\nu\_{0},\nu):={\cal T}({\mu\_{\rm ini}},{\mu\_{\rm tar}}) such that the measure π∈𝒫2​(ℝd×ℝd)\pi\in\mathscr{P}\_{2}(\mathbb{R}^{d}\times\mathbb{R}^{d}) defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(E)=∫Ep​(T,y;0,x)​ν0​(d​x)​ν​(d​y),E∈ℬ​(ℝd×ℝd)\displaystyle\pi(E)=\int\_{E}p(T,y;0,x)\nu\_{0}(dx)\nu(dy),\qquad E\in\mathscr{B}(\mathbb{R}^{d}\times\mathbb{R}^{d}) |  | (1.1) |

has the marginals μini{\mu\_{\rm ini}} and μ\mu, where p​(⋅,⋅;⋅,⋅)p(\cdot,\cdot;\cdot,\cdot) is the transition density of a given diffusion process. If we fix μini{\mu\_{\rm ini}}, and denote ρμ\rho^{\mu} to be the density of the measure ν=𝒯​(μ)\nu={\cal T}(\mu), μ∈𝒫2​(ℝd)\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d}), then it turns out that the solution to the SCSBP is the fixed-point of the mapping Γ:𝒫2​(ℝd)↦𝒫2​(ℝd)\Gamma:\mathscr{P}\_{2}(\mathbb{R}^{d})\mapsto\mathscr{P}\_{2}(\mathbb{R}^{d}), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ​(μ):=arg​minν∈𝒫2​(ℝd)⁡{k​G​(ν)+𝔼X∼ν​[log⁡ρμ​(X)]}.\displaystyle\Gamma(\mu):={\operatorname\*{arg\,min}}\_{\nu\in\mathscr{P}\_{2}(\mathbb{R}^{d})}\left\{kG(\nu)+\mathbb{E}\_{X\sim\nu}[\log\rho^{\mu}(X)]\right\}. |  | (1.2) |

The successful application of Schauder’s fixed-point theorem on the Wasserstein space relies on several key elements, in particular a crucial continuous dependence result of the mapping μ↦ρμ\mu\mapsto\rho^{\mu}, for which we introduce an auxiliary entropic optimal transport problem, and identify its solution to the measure π\pi in ([1.1](https://arxiv.org/html/2510.11829v1#S1.E1 "In 1.1 Outline of the Main Results and Contributions ‣ 1 Introduction ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")).
By utilizing some important stability results of the corresponding Schrödinger potentials (Proposition [5.8](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem8 "Proposition 5.8. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), together with some arguments in the spirit of the converse of Scheffé’s theorem (i.e., the weak convergence in Prohorov metric vs. the convergence in densities) as well as the so-called Γ\Gamma-convergence of the minimizers of the optimization problem ([1.2](https://arxiv.org/html/2510.11829v1#S1.E2 "In 1.1 Outline of the Main Results and Contributions ‣ 1 Introduction ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), we are able to verify the required properties so the mapping Γ\Gamma has a fixed-point (Theorem [6.1](https://arxiv.org/html/2510.11829v1#S6.ThmTheorem1 "Theorem 6.1. ‣ 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")).
As a direct consequence, we establish that the optimal control of the SCSBP converges linearly with respect to the penalty parameter kk (Theorem [4.1](https://arxiv.org/html/2510.11829v1#S4.ThmTheorem1 "Theorem 4.1. ‣ 4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). We believe that such a fixed-point perspective is novel in the literature, as it not only offers a constructive framework for characterizing solutions in the general case but also yields insights into how the penalty parameter affects the convergence rate.

### 1.2 Closely Related Literature

Our general formulation is largely inspired by Garg et al. [[29](https://arxiv.org/html/2510.11829v1#bib.bib29)], which investigates the SCSBP with the KL divergence as the penalty function GG. Within that framework, the authors established the asymptotic convergence of the optimal policies as the penalty parameter kk tends to infinity, under the assumption that the initial measure is a delta measure. However, the use of KL divergence presents practical difficulties: if the model distribution μ\mu assigns zero probability to any region where the data distribution μtar\mu\_{\rm tar} has positive mass, then KL​(μtar∥μ)=+∞\mathrm{KL}(\mu\_{\rm tar}\|\mu)=+\infty, rendering the divergence ill-posed under support mismatch [[15](https://arxiv.org/html/2510.11829v1#bib.bib15), [38](https://arxiv.org/html/2510.11829v1#bib.bib38)]. Moreover, a delta initial measure is rarely employed in generative tasks, as it lacks the diversity and randomness required for effective training. Finally, no convergence rate is quantified therein.

On a technical level, our formulation is closely related to Hernández-Tangpi [[35](https://arxiv.org/html/2510.11829v1#bib.bib35)], in which
the authors use a probabilistic approach to recast a mean-field Schrödinger bridge into a stochastic optimization problem with McKean-Vlasov dynamics, and connect the optimal control to a solution to a forward backward SDE of McKean-Vlasov type (MKV FBSDE). However, given the generality of the drift, diffusion, and running cost functions, the associated MKV FBSDE is derived without a discussion of uniqueness. In fact, it is not completely obvious that a McKean-Vlasov-type SBP can be converted to a McKean-Vlasov stochastic control problem via the usual Girsanov theorem argument, as we show in Remark [2.1](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem1 "Remark 2.1 (Subtlety in formulating the McKean-Vlasov version of the problem). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") below. Moreover, the conditions imposed on the penalty function
GG are abstract and can be difficult to verify in common examples. By contrast, our framework leverages the PDE formulation and Doob’s hh-transform representation, requiring only mild growth conditions on
GG and control of density gaps (see Assumption ([3.2](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"))). Several concrete examples of admissible
GG are provided in Example [3.4](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem4 "Example 3.4. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and [3.5](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem5 "Example 3.5. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday").

The rest of the paper is organized as follows. Section [2](https://arxiv.org/html/2510.11829v1#S2 "2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") introduces the necessary concepts and notations. In particular, we present the connection between the underlying SBP and its stochastic control formulation, and introduce the notion of the SCSBP together with some potential applications. Section [3](https://arxiv.org/html/2510.11829v1#S3 "3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") is devoted to the existence of optimal policies for the SCSBP at each penalty parameter kk, while Section [4.1](https://arxiv.org/html/2510.11829v1#S4.SS1 "4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") establishes that the penalized optimal policies converge to those of the original SBP as k→∞k\to\infty, with a linear rate of convergence. In addition, we prove convergence of the corresponding value functions and quantify the distance between the terminal distribution and the target distribution in terms of the Wasserstein distance. Sections [5](https://arxiv.org/html/2510.11829v1#S5 "5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and [6](https://arxiv.org/html/2510.11829v1#S6 "6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") are devoted to the case with a general initial distribution. A crucial stability result is established in Section [5](https://arxiv.org/html/2510.11829v1#S5 "5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), via the stability of Schrödinger potentials of an auxiliary entropy optimal transport problem, and in Section [6](https://arxiv.org/html/2510.11829v1#S6 "6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") we complete the fixed-point argument.

## 2 Preliminary

Throughout this paper, we consider a generic Euclidean space 𝕏\mathbb{X}, and regardless of its dimension, we denote (⋅,⋅)(\cdot,\cdot) and |⋅||\cdot| be its inner product and norm, respectively. We denote ℂ​([0,T];𝕏)\mathbb{C}([0,T];\mathbb{X}) to be the space of 𝕏\mathbb{X}-valued continuous functions defined on [0,T][0,T] with the usual sup-norm, and in particular, we denote ℂTd:=ℂ​([0,T];ℝd)\mathbb{C}^{d}\_{T}:=\mathbb{C}([0,T];\mathbb{R}^{d}), and let ℬ​(ℂTd)\mathscr{B}(\mathbb{C}\_{T}^{d}) be its topological Borel field.
We shall consider the following
canonical probabilistic space: (Ω,ℱ,ℙ)(\Omega,{\cal F},\mathbb{P}), where (Ω,ℱ):=(ℂTd,ℬ​(ℂTd))(\Omega,{\cal F}):=(\mathbb{C}^{d}\_{T},\mathscr{B}(\mathbb{C}^{d}\_{T})) and ℙ∈𝒫​(Ω)\mathbb{P}\in\mathscr{P}(\Omega), the space of all probability measures defined on (Ω,ℱ)(\Omega,{\cal F}). Finally, we let ℙ0∈𝒫​(Ω)\mathbb{P}^{0}\in\mathscr{P}(\Omega) be
the Wiener measure on (Ω,ℱ)(\Omega,{\cal F}); Wt​(ω):=ω​(t)W\_{t}(\omega):=\omega(t), ω∈Ω\omega\in\Omega, the canonical process; and 𝔽0:={ℱt0}t∈[0,T]\mathbb{F}^{0}:=\{{\cal F}^{0}\_{t}\}\_{t\in[0,T]}, where ℱt0:=ℬt(ℂTd):=σ{ω(⋅∧t):ω∈ℂTd}{\cal F}^{0}\_{t}:=\mathscr{B}\_{t}(\mathbb{C}\_{T}^{d}):=\sigma\{\omega(\cdot\wedge t):\omega\in\mathbb{C}^{d}\_{T}\}, t∈[0,T]t\in[0,T]. We assume that 𝔽0\mathbb{F}^{0} has the usual ℙ0\mathbb{P}^{0}-augmentation so that it satisfies the usual hypotheses (cf. e.g., [[50](https://arxiv.org/html/2510.11829v1#bib.bib50)]), and for p≥1p\geq 1, we denote 𝕃𝔽0p​([0,T];𝕏)\mathbb{L}^{p}\_{\mathbb{F}^{0}}([0,T];\mathbb{X}) to be all 𝕏\mathbb{X}-valued, pp-integrable, 𝔽0\mathbb{F}^{0}-adapted processes. Finally, we denote ℳ​(ℝd)\mathscr{M}(\mathbb{R}^{d}) to be all σ\sigma-finite measures on ℝd\mathbb{R}^{d} and 𝒫p​(ℝd)\mathscr{P}\_{p}(\mathbb{R}^{d}) to be all probability measures with finite pp-th moment on ℝd\mathbb{R}^{d} equipped with pp-Wasserstein metric, denoted by Wp​(⋅,⋅)W\_{p}(\cdot,\cdot).

We recall that a classical Schrödinger Bridge Problem (SBP) amounts to finding, for
ℙ∈𝒫​(Ω)\mathbb{P}\in\mathscr{P}(\Omega),

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(ℙ):=infℚ∈𝒫′DKL​(ℚ∥ℙ),\displaystyle V(\mathbb{P}):=\inf\_{\mathbb{Q}\in\mathscr{P}^{\prime}}D\_{\rm KL}(\mathbb{Q}\|\mathbb{P}), |  | (2.1) |

where 𝒫′⊂𝒫​(Ω)\mathscr{P}^{\prime}\subset\mathscr{P}(\Omega) is a given admissible set, and DKL(⋅∥⋅)D\_{\rm KL}(\,\cdot\,\|\,\cdot\,) is the so-called Kullback-Leibler Divergence or the Relative Entropy (cf. [[39](https://arxiv.org/html/2510.11829v1#bib.bib39)]), defined by

|  |  |  |
| --- | --- | --- |
|  | DKL(ℚ∥ℙ):={𝔼ℚ​[log⁡(d​ℚd​ℙ)],if ​d​ℚ≪d​ℙ;∞,other wise.\displaystyle D\_{\rm KL}(\mathbb{Q}\|\mathbb{P}):=\begin{cases}\mathbb{E}^{\mathbb{Q}}\big[\log\big(\frac{d\mathbb{Q}}{d\mathbb{P}}\big)\big],&{\text{if }}d\mathbb{Q}\ll d\mathbb{P};\\ \infty,&\text{other wise}.\end{cases} |  |

We remark here that the KL-divergence DKL(⋅∥⋅)D\_{\rm KL}(\,\cdot\,\|\,\cdot\,) can be easily extended to any σ\sigma-finite measures222In this case DKL​(ℚ∥ℙ):=∫log⁡(ℚ​(d​x)ℙ​(d​x))​ℚ​(d​x)D\_{\rm KL}(\mathbb{Q}\|\mathbb{P}):=\int\log\big(\frac{\mathbb{Q}(dx)}{\mathbb{P}(dx)}\big)\mathbb{Q}(dx), if d​ℚ≪d​ℙd\mathbb{Q}\ll d\mathbb{P}.. In what follows, we shall focus on the case when
ℚ=ℙ∘X−1\mathbb{Q}=\mathbb{P}\,\circ\,X^{-1} for some ℝd\mathbb{R}^{d}-valued continuous process XX defined on the canonical space with some ℙ∈𝒫​(Ω)\mathbb{P}\in\mathscr{P}(\Omega), such that ℚ0:=ℙ∘X0−1=μini\mathbb{Q}\_{0}\negthinspace:=\negthinspace\mathbb{P}\circ{X\_{0}}^{-1}={\mu\_{\rm ini}}, ℚT:=ℙ∘XT−1=μtar\mathbb{Q}\_{T}\negthinspace:=\negthinspace\mathbb{P}\circ{X\_{T}}^{-1}\negthinspace=\negthinspace{\mu\_{\rm tar}}\negthinspace, and denote 𝒫′:=𝒫​(μini,μtar)⊆𝒫​(Ω)\mathscr{P}^{\prime}:=\mathscr{P}({\mu\_{\rm ini}},{\mu\_{\rm tar}})\subseteq\mathscr{P}(\Omega) be all such “path measures”.

We note that if ℙ=ℙ0\mathbb{P}=\mathbb{P}^{0} is Wiener measure and ℚ\mathbb{Q} is equivalent to ℙ0\mathbb{P}^{0}, then by the Cameron-Martin-Girsanov theorem, there exists α∈𝕃𝔽02​([0,T];ℝd×d)\alpha\in\mathbb{L}^{2}\_{\mathbb{F}^{0}}([0,T];\mathbb{R}^{d\times d}), such that

|  |  |  |
| --- | --- | --- |
|  | d​ℚd​ℙ0|ℱt:=ℰt​(α)=exp⁡{∫0tαs​𝑑Ws−12​∫0t|αs|2​𝑑s},t∈[0,T],\frac{d\mathbb{Q}}{d\mathbb{P}^{0}}\Big|\_{{\cal F}\_{t}}:=\mathscr{E}\_{t}(\alpha)=\exp\Big\{\int\_{0}^{t}\alpha\_{s}dW\_{s}-\frac{1}{2}\int\_{0}^{t}|\alpha\_{s}|^{2}ds\Big\},\quad t\in[0,T], |  |

is a ℙ0\mathbb{P}^{0}-martingale, and W~t:=Wt−∫0tαs​𝑑s\widetilde{W}\_{t}:=W\_{t}-\int\_{0}^{t}\alpha\_{s}ds, t∈[0,T]t\in[0,T], is a ℚ\mathbb{Q}-Brownian motion. It can then be easily calculated that

|  |  |  |  |
| --- | --- | --- | --- |
|  | DKL​(ℚ∥ℙ0)=12​𝔼ℚ​[∫0T|αt|2​𝑑t].\displaystyle D\_{\rm KL}(\mathbb{Q}\|\mathbb{P}^{0})=\frac{1}{2}\mathbb{E}^{\mathbb{Q}}\Big[\int\_{0}^{T}|\alpha\_{t}|^{2}dt\Big]. |  | (2.2) |

#### Schrödinger Bridge and Related Control Problem.

In light of ([2.2](https://arxiv.org/html/2510.11829v1#S2.E2 "In 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), one can easily associate a SBP to a stochastic control problem (see, e.g., [[14](https://arxiv.org/html/2510.11829v1#bib.bib14), §4.4], [[17](https://arxiv.org/html/2510.11829v1#bib.bib17), §1] and [[40](https://arxiv.org/html/2510.11829v1#bib.bib40), p36]). Consider, for example, a standard SDE
on (Ω,ℱ,ℙ0)(\Omega,{\cal F},\mathbb{P}^{0}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=b​(t,Xt)​d​t+d​Wt,X0∼μini.\displaystyle dX\_{t}=b(t,X\_{t})dt+dW\_{t},\quad X\_{0}\sim{\mu\_{\rm ini}}. |  | (2.3) |

Denote ℙ=ℙX:=ℙ0∘X−1∈𝒫​(Ω)\mathbb{P}=\mathbb{P}\_{X}:=\mathbb{P}^{0}\circ X^{-1}\in\mathscr{P}(\Omega).
Then we consider the following SBP:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(μini,μtar):=infℚ∈𝒫​(μini,μtar)DKL​(ℚ∥ℙ).V({\mu\_{\rm ini}},{\mu\_{\rm tar}}):=\inf\_{\mathbb{Q}\in\mathscr{P}({\mu\_{\rm ini}},{\mu\_{\rm tar}})}D\_{\rm KL}(\mathbb{Q}\|\mathbb{P}). |  | (2.4) |

Similar to ([2.2](https://arxiv.org/html/2510.11829v1#S2.E2 "In 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), we can recast ([2.4](https://arxiv.org/html/2510.11829v1#S2.E4 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) as the following stochastic control problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(μini,μtar)=infα∈𝒜J​(α)=infα∈𝒜𝔼ℚ​[12​∫0T|αs|2​𝑑s],\displaystyle V({\mu\_{\rm ini}},{\mu\_{\rm tar}})=\inf\_{\alpha\in\mathcal{A}}J(\alpha)=\inf\_{\alpha\in\mathcal{A}}\mathbb{E}^{\mathbb{Q}}\Big[\frac{1}{2}\int\_{0}^{T}|\alpha\_{s}|^{2}ds\Big], |  | (2.5) |

where ℚ∈𝒫​(Ω)\mathbb{Q}\in\mathscr{P}(\Omega) is such that d​ℚd​ℙ=ℰ​(α)\frac{d\mathbb{Q}}{d\mathbb{P}}=\mathscr{E}(\alpha) for some α∈𝒜⊆𝕃𝔽02​([0,T])\alpha\in\mathcal{A}\subseteq\mathbb{L}^{2}\_{\mathbb{F}^{0}}([0,T]), under which the underlying controlled dynamics takes the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xtα=[b​(t,Xtα)+αt]​d​t+d​W~t,ℚ∘(X0α)−1=μini,ℚ∘(XTα)−1=μtar,\displaystyle dX^{\alpha}\_{t}=[b(t,X^{\alpha}\_{t})+\alpha\_{t}]dt+d\widetilde{W}\_{t},\quad\mathbb{Q}\circ(X\_{0}^{\alpha})^{-1}={\mu\_{\rm ini}},\quad\mathbb{Q}\circ(X\_{T}^{\alpha})^{-1}={\mu\_{\rm tar}}, |  | (2.6) |

where W~\widetilde{W} is a ℚ\mathbb{Q}-Brownian motion.

###### Remark 2.1 (Subtlety in formulating the McKean-Vlasov version of the problem).

It is rather tempting to apply the idea above to the so-called McKean-Vlasov SBP (MVSBP). Consider, for example,
the following McKean-Vlasov SDE on (Ω,ℱ,ℙ0)(\Omega,{\cal F},\mathbb{P}^{0}):

|  |  |  |
| --- | --- | --- |
|  | d​Xt=b​(t,Xt,ℙt)​d​t+d​Wt,X0∼μini.\displaystyle dX\_{t}=b(t,X\_{t},\mathbb{P}\_{t})dt+dW\_{t},\quad X\_{0}\sim{\mu\_{\rm ini}}. |  |

where, again, we denote ℙ=ℙ0∘X−1∈𝒫2​(Ω)\mathbb{P}=\mathbb{P}^{0}\circ X^{-1}\in\mathscr{P}\_{2}(\Omega), and ℙt:=ℙ0∘Xt−1∈𝒫2​(ℝd)\mathbb{P}\_{t}:=\mathbb{P}^{0}\circ X^{-1}\_{t}\in\mathscr{P}\_{2}(\mathbb{R}^{d}), t∈[0,T]t\in[0,T].
Similar to ([2.4](https://arxiv.org/html/2510.11829v1#S2.E4 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) we can define an SBP, and let us
refer to it as an MVSBP. Again, by ([2.2](https://arxiv.org/html/2510.11829v1#S2.E2 "In 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), we can recast such MVSBP as the following (weak form) stochastic control problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(μini,μtar):=infα𝔼ℚ​[∫0T12​|αt|2​d⁡t],\displaystyle V({\mu\_{\rm ini}},{\mu\_{\rm tar}}):=\inf\_{\alpha}\mathbb{E}^{\mathbb{Q}}\Big[\int\_{0}^{T}\frac{1}{2}|\alpha\_{t}|^{2}\operatorname{{\rm d}}t\Big], |  | (2.7) |

where ℚ∈𝒫​(Ω)\mathbb{Q}\in\mathscr{P}(\Omega) is such that the underlying controlled process X=XαX=X^{\alpha} satisfies, under ℚ\mathbb{Q}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=[αt+b​(t,Xt,ℙt)]​d​t+d​W~t,X0∼μini,XT∼μtar,\displaystyle dX\_{t}=[\alpha\_{t}+b(t,X\_{t},\mathbb{P}\_{t})]dt+d\widetilde{W}\_{t},\quad X\_{0}\sim{\mu\_{\rm ini}},\quad X\_{T}\sim{\mu\_{\rm tar}}, |  | (2.8) |

where W~\widetilde{W} is a ℚ\mathbb{Q}-Brownian motion, and we can assume that α∈𝕃𝔽02​([0,T])\alpha\in\mathbb{L}^{2}\_{\mathbb{F}^{0}}([0,T]). However, by looking at ([2.8](https://arxiv.org/html/2510.11829v1#S2.E8 "In Remark 2.1 (Subtlety in formulating the McKean-Vlasov version of the problem). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) more closely we see that the problem ([2.7](https://arxiv.org/html/2510.11829v1#S2.E7 "In Remark 2.1 (Subtlety in formulating the McKean-Vlasov version of the problem). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) and ([2.8](https://arxiv.org/html/2510.11829v1#S2.E8 "In Remark 2.1 (Subtlety in formulating the McKean-Vlasov version of the problem). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) do not form a McKean-Vlasov control problem, since ℙt≠ℚ∘(Xt)−1\mathbb{P}\_{t}\neq\mathbb{Q}\circ(X\_{t})^{-1}(!). Therefore, an MVSBP should be formulated more carefully so as to connect to an McKean-Vlasov stochastic control problem.
∎

Ideally, the optimal solution to the Schrödinger bridge problem ([2.5](https://arxiv.org/html/2510.11829v1#S2.E5 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"))-([2.6](https://arxiv.org/html/2510.11829v1#S2.E6 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) provides a transport map from the initial distribution μini{\mu\_{\rm ini}} to the target distribution μtar{\mu\_{\rm tar}}. This transport is interpolated by a diffusion process that most closely resembles the canonical Brownian motion in the space of path measures. However, designing training algorithms to (approximately) learn the optimal solution to ([2.5](https://arxiv.org/html/2510.11829v1#S2.E5 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"))–([2.6](https://arxiv.org/html/2510.11829v1#S2.E6 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) typically involves an iterative scheme that alternately relaxes the initial and terminal constraints [[20](https://arxiv.org/html/2510.11829v1#bib.bib20), [64](https://arxiv.org/html/2510.11829v1#bib.bib64), [66](https://arxiv.org/html/2510.11829v1#bib.bib66), [54](https://arxiv.org/html/2510.11829v1#bib.bib54)], and whose convergence rate and computational complexity in high-dimensional settings remain unclear.

While there could be techniques in stochastic control theory to deal with such a constraint, we shall follow the idea of [[35](https://arxiv.org/html/2510.11829v1#bib.bib35)], by approximating the original control problem by a family of unconstrained
McKean-Vlasov stochastic control problems with terminal penalties. More precisely, we shall allow the law of XTαX^{\alpha}\_{T} in ([2.6](https://arxiv.org/html/2510.11829v1#S2.E6 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) to be different from μtar{\mu\_{\rm tar}}, but add a corresponding penalty function to it in the cost functional J​(⋅)J(\cdot).

To this end, let us still denote 𝒜⊆𝒫​(Ω){\cal A}\subseteq\mathscr{P}(\Omega) to be the set of all ℚ∈𝒫​(Ω)\mathbb{Q}\in\mathscr{P}(\Omega) such that

(i) d​ℚd​ℙ|ℱT=ℰ​(α)=exp⁡{∫0Tαs​𝑑Ws−12​∫0T|αs|2​𝑑s}\frac{d\mathbb{Q}}{d\mathbb{P}}\Big|\_{{\cal F}\_{T}}=\mathscr{E}(\alpha)=\exp\big\{\int\_{0}^{T}\alpha\_{s}dW\_{s}-\frac{1}{2}\int\_{0}^{T}|\alpha\_{s}|^{2}ds\big\}, α∈𝕃𝔽02​([0,T];ℝd×d)\alpha\in\mathbb{L}^{2}\_{\mathbb{F}^{0}}([0,T];\mathbb{R}^{d\times d});

(ii) Under ℚ\mathbb{Q}, the underlying state process XX follows the dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xtα=[b​(t,Xtα)+σ​(t)​αt]​d​t+σ​(t)​d​W~t,ℚ∘(X0α)−1=μini,\displaystyle dX^{\alpha}\_{t}=[b(t,X^{\alpha}\_{t})+\sigma(t)\alpha\_{t}]dt+\sigma(t)d\widetilde{W}\_{t},\quad\mathbb{Q}\circ(X\_{0}^{\alpha})^{-1}={\mu\_{\rm ini}}, |  | (2.9) |

where W~\widetilde{W} is a ℚ\mathbb{Q}-Brownian motion.

Throughout this paper, we shall make the following Standing Assumption on the coefficients bb and σ\sigma.

###### Assumption 2.2.

The coefficients b:[0,T]×ℝd↦ℝdb:[0,T]\times\mathbb{R}^{d}\mapsto\mathbb{R}^{d} and σ:[0,T]↦ℝd×d\sigma:[0,T]\mapsto\mathbb{R}^{d\times d} are given deterministic continuous functions, such that there exists L>0L>0, it holds that

|  |  |  |
| --- | --- | --- |
|  | |b​(t,x)−b​(t,y)|≤L​|x−y|,t∈[0,T],x,y∈ℝd.|b(t,x)-b(t,y)|\leq L|x-y|,\qquad t\in[0,T],~x,y\in\mathbb{R}^{d}. |  |

Clearly, under Assumption [2.2](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem2 "Assumption 2.2. ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), the SDE ([2.9](https://arxiv.org/html/2510.11829v1#S2.E9 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) has a unique strong solution XαX^{\alpha} on (Ω,ℱ,ℙ0)(\Omega,{\cal F},\mathbb{P}^{0}) for any given α∈𝕃𝔽01​([0,T];ℝd×d)\alpha\in\mathbb{L}^{1}\_{\mathbb{F}^{0}}([0,T];\mathbb{R}^{d\times d}) (see [[50](https://arxiv.org/html/2510.11829v1#bib.bib50), [69](https://arxiv.org/html/2510.11829v1#bib.bib69)]). We shall often identify ℚ∈𝒜\mathbb{Q}\in{\cal A} with its associated process α\alpha, and denote ℚ∼α\mathbb{Q}\sim\alpha and α∈𝒜\alpha\in{\cal A} when the context is clear. The key element of the soft-constrained Schrödinger Bridge Problem is the following penalty function.

###### Definition 2.3.

A smooth function G​(⋅)=G​(⋅;μtar):𝒫2​(ℝd)→[0,∞)G(\cdot)=G(\cdot;{\mu\_{\rm tar}}):\mathscr{P}\_{2}(\mathbb{R}^{d})\to[0,\infty) is called a smooth penalty function associated to μtar∈𝒫2​(ℝd){\mu\_{\rm tar}}\in\mathscr{P}\_{2}(\mathbb{R}^{d}) if:
G​(μ;μtar)=0G(\mu;{\mu\_{\rm tar}})=0 if and only if μ=μtar\mu={\mu\_{\rm tar}}.
∎

Now let us introduce the following family of McKean-Vlasov-type stochastic control problems:

###### Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)).

For k∈ℕk\in\mathbb{N}, find αk∈𝒜\alpha^{k}\in{\cal A} such that Vk:=Jk​(α^k)=infα∈𝒜Jk​(α)V^{k}:=J^{k}(\widehat{\alpha}^{k})=\inf\_{\alpha\in{\cal A}}J^{k}(\alpha), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jk​(α)=𝔼ℚ​[12​∫0T|αs|2​𝑑s+k​G​(ℚXTα)],\displaystyle J^{k}(\alpha)=\mathbb{E}^{\mathbb{Q}}\left[\frac{1}{2}\int\_{0}^{T}|\alpha\_{s}|^{2}ds+kG(\mathbb{Q}\_{X^{\alpha}\_{T}})\right], |  | (2.10) |

and G​(⋅)=G​(⋅;μtar)G(\cdot)=G(\cdot;{\mu\_{\rm tar}}) is the given penalty function satisfying Definition [2.3](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem3 "Definition 2.3. ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and ℚ∼α\mathbb{Q}\sim\alpha.
∎

#### Applications in Generative AI.

We remark that the SCSBP Problem [2.4](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem4 "Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")
offers a general framework that can be applied to address multiple problems in generative AI. We briefly mention a few motivational examples.

###### Example 2.5 (Data generation).

The goal of generative AI is to train a data generation procedure using a finite number of iid. data samples {x1,⋯,xN}\{x\_{1},\cdots,x\_{N}\} under a (unknown) target distribution μtar{\mu\_{\rm tar}}, in order to simulate unlimited number of data samples whose underlying distribution is close to μtar{\mu\_{\rm tar}} [[58](https://arxiv.org/html/2510.11829v1#bib.bib58), [36](https://arxiv.org/html/2510.11829v1#bib.bib36), [33](https://arxiv.org/html/2510.11829v1#bib.bib33)].

To cast this problem into our framework, we can take, for example, μini=𝒩​(0,I){\mu\_{\rm ini}}=\mathcal{N}(0,I) and μtar=pdata{\mu\_{\rm tar}}=p\_{\rm data} in the theoretical framework (or μtar=1N​∑i=1Nδxi{\mu\_{\rm tar}}=\frac{1}{N}\sum\_{i=1}^{N}\delta\_{x\_{i}} in the practical implementation). Then the optimal control α∗\alpha^{\*} of SCSBP leads to a controlled process (Xtα∗)0≤t≤T(X\_{t}^{\alpha^{\*}})\_{0\leq t\leq T} that simulates the data output XTα∗X\_{T}^{\alpha^{\*}}. Our key results (see Theorem [4.1](https://arxiv.org/html/2510.11829v1#S4.ThmTheorem1 "Theorem 4.1. ‣ 4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and Theorem [6.4](https://arxiv.org/html/2510.11829v1#S6.ThmTheorem4 "Theorem 6.4. ‣ 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") below) show that the terminal measure ℚXTα∗\mathbb{Q}\_{X\_{T}^{\alpha^{\*}}} is close to μtar{\mu\_{\rm tar}}, when kk is sufficiently large.
∎

###### Example 2.6 (Fine-tuning under a reward signal).

Fine-tuning a diffusion model means taking a pre-trained model and training it further on a smaller, task-specific dataset so it learns to generate outputs more suited to that new context [[60](https://arxiv.org/html/2510.11829v1#bib.bib60), [70](https://arxiv.org/html/2510.11829v1#bib.bib70), [62](https://arxiv.org/html/2510.11829v1#bib.bib62), [34](https://arxiv.org/html/2510.11829v1#bib.bib34)]. For example, a diffusion model trained on general images can be fine-tuned to generate a specific style (evaluated via a reward function). This process updates the model’s parameters just enough to adapt to the new data, without starting training from scratch.

In terms of our framework, we can consider ([2.3](https://arxiv.org/html/2510.11829v1#S2.E3 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) as a pre-trained model with the drift b​(t,x):=sθ^​(t,x)b(t,x):=s\_{\widehat{\theta}}(t,x) being a well-trained score function, and θ^\widehat{\theta} is the trained parameter. Note that, as the result of pre-training, the output measure ℚXT\mathbb{Q}\_{X\_{T}} is sufficiently close to some data distribution μtar{\mu\_{\rm tar}}. We then introduce a fine-tuning procedure through a reference measure prefp\_{\rm ref} with density exp⁡(r​(x))∫ℝdexp⁡(r​(x))​𝑑x\frac{\exp(r(x))}{\int\_{\mathbb{R}^{d}}\exp(r(x))dx}, where r:ℝd→ℝr:\mathbb{R}^{d}\rightarrow\mathbb{R} is a given reward function satisfying ∫ℝdexp⁡(r​(x))​𝑑x<∞\int\_{\mathbb{R}^{d}}\exp(r(x))dx<\infty. Now replacing μtar=pref{\mu\_{\rm tar}}=p\_{\rm ref}, the optimal control α∗\alpha^{\*} of the corresponding SCSBP can then serve as the fine-tuning score function; and consequently, the new drift term b​(t,Xtα⁣∗)+σ​(t)​α∗b(t,X^{\alpha\*}\_{t})+\sigma(t)\alpha^{\*} acts as a combined score function.

Clearly, in this application the penalty parameter kk should not be chosen too large; otherwise, the effect of the preference function may dominate the fidelity to the original data distribution. With an appropriately selected kk, the resulting measure ℚXTα∗\mathbb{Q}\_{X^{\alpha^{\*}}\_{T}} not only reflects pdatap\_{\rm data} but also integrates the reward function rr. In contrast, we remark that the classic SBP ([2.1](https://arxiv.org/html/2510.11829v1#S2.E1 "In 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) is not capable of handling this application as it has a pre-fixed target distribution.
∎

###### Example 2.7 (Transfer learning).

Transfer learning is a machine learning approach where knowledge gained from a “source task" is reused to improve learning in a related but different “target task" [[9](https://arxiv.org/html/2510.11829v1#bib.bib9), [61](https://arxiv.org/html/2510.11829v1#bib.bib61), [48](https://arxiv.org/html/2510.11829v1#bib.bib48)]. In what follows we shall consider transfer learning in the context of data generation.

Let us consider a source task (Ysou)(Y\_{\rm sou}), characterized by a distribution psoup\_{\rm sou}, and a target task (Ytar)(Y\_{\rm tar}) with distribution ptarp\_{\rm tar}. Typically, psoup\_{\rm sou} and ptarp\_{\rm tar} are assumed to be close under a certain divergence or distance function G​(ptar;psou)G(p\_{\rm tar};p\_{\rm sou}) (assuming G≥0G\geq 0), such as the Wasserstein distance [[48](https://arxiv.org/html/2510.11829v1#bib.bib48)].

To fit the transfer learning into our framework, we can take μini=psou{\mu\_{\rm ini}}=p\_{\rm sou}, μtar=ptar{\mu\_{\rm tar}}=p\_{\rm tar}, and set b≡0b\equiv 0 for simplicity. In this case, if we choose α=0\alpha=0, and X0∼psouX\_{0}\sim p\_{\rm sou}, then XT0=X0+WT∼psou∗𝒩​(0,T​𝕀d)X^{0}\_{T}=X\_{0}+W\_{T}\sim p\_{\rm sou}\*\mathcal{N}(0,T\mathbb{I}\_{d}), where 𝒩​(0,T​𝕀d)=ℙ0∘WT−1\mathcal{N}(0,T{\mathbb{I}\_{d}})=\mathbb{P}^{0}\circ W\_{T}^{-1} and 𝕀d\mathbb{I}\_{d} denotes the d×dd\times d identity matrix. Thus, denoting the optimal control by α^\widehat{\alpha} and noting that α≡0\alpha\equiv 0 is sub-optimal, we must have

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ​[12​∫0T|α^s|2​𝑑s]≤𝔼ℚ​[12​∫0T|α^s|2​𝑑s+k​G​(ℚXTα^)]≤k​G​(psou∗𝒩​(0,T​𝕀d);ptar).\displaystyle\mathbb{E}^{\mathbb{Q}}\left[\frac{1}{2}\int\_{0}^{T}|\widehat{\alpha}\_{s}|^{2}ds\right]\leq\mathbb{E}^{\mathbb{Q}}\left[\frac{1}{2}\int\_{0}^{T}|\widehat{\alpha}\_{s}|^{2}ds+kG(\mathbb{Q}\_{X^{\widehat{\alpha}}\_{T}})\right]\leq kG(p\_{\rm sou}\*\mathcal{N}(0,T{\mathbb{I}\_{d}});p\_{\rm tar}). |  |

This implies that the optimal control α^\widehat{\alpha} has a small L2L^{2}-norm, indicating only minor adjustments are required during sampling—provided kk is not too large.
∎

## 3 Existence of Optimal Policies for SCSBP’s

In this section we study the stochastic control problem ([2.9](https://arxiv.org/html/2510.11829v1#S2.E9 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"))-([2.10](https://arxiv.org/html/2510.11829v1#S2.E10 "In Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) and the associated soft-constrained SBP. In particular, we shall prove that the optimal control for each k∈ℕk\in\mathbb{N} exists and in next section we will show that these optimal policies will converge to the solution of the original SBP, with a linear rate of convergence. We shall assume that the target distribution for the SCSBP has a
density ftar∈𝕃1​(ℝd)f\_{\rm tar}\in\mathbb{L}^{1}(\mathbb{R}^{d}). Also, we shall assume
σ​(⋅)=Id\sigma(\cdot)=I\_{d}, that is, in what follows we assume that the underlying diffusion takes the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=b​(t,Xt)​d​t+d​Wt,X0∼μini,t∈[0,T],\displaystyle dX\_{t}=b(t,X\_{t})dt+dW\_{t},\quad X\_{0}\sim{\mu\_{\rm ini}},\quad t\in[0,T], |  | (3.1) |

where WW is the canonical Brownian motion under ℙ0\mathbb{P}^{0}. Let p​(⋅,⋅;⋅,⋅)p(\cdot,\cdot;\cdot,\cdot) denote the transition density of the solution XX, so that ℙ0​{Xs∈d​z|Xt=x}=p​(s,z;t,x)​d​z\mathbb{P}^{0}\{X\_{s}\in dz|X\_{t}=x\}=p(s,z;t,x)dz, 0≤t<s≤T0\leq t<s\leq T, z,x∈ℝdz,x\in\mathbb{R}^{d}. Then, it is well known that p​(⋅,⋅;⋅,⋅)p(\cdot,\cdot;\cdot,\cdot) is the fundamental solution to Kolmogorov backward (parabolic) PDE, and under mild conditions (see, e.g., [[3](https://arxiv.org/html/2510.11829v1#bib.bib3)]), there exist c1c\_{1}, c2c\_{2}, λ\lambda, Λ>0\Lambda>0, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | c1​(s−t)−d2​e−λ​|z−x|2s−t<p​(s,z;t,x)<c2​(s−t)−d2​e−Λ​|z−x|24​(s−t).c\_{1}(s-t)^{-\frac{d}{2}}e^{-\frac{\lambda|z-x|^{2}}{s-t}}<p(s,z;t,x)<c\_{2}(s-t)^{-\frac{d}{2}}e^{-\frac{\Lambda|z-x|^{2}}{4(s-t)}}. |  | (3.2) |

Keeping the original SBP ([2.4](https://arxiv.org/html/2510.11829v1#S2.E4 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) and ([2.5](https://arxiv.org/html/2510.11829v1#S2.E5 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) associated with ([3.1](https://arxiv.org/html/2510.11829v1#S3.E1 "In 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) in mind, let us now recall the Problem [2.4](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem4 "Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and the cost functional Jk​(α)J^{k}(\alpha) defined by ([2.10](https://arxiv.org/html/2510.11829v1#S2.E10 "In Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). For notational simplicity in what follows we shall identify ℚ∈𝒜\mathbb{Q}\in{\cal A} by ℚ=ℙXα=ℙ0∘(Xα)−1\mathbb{Q}=\mathbb{P}\_{X^{\alpha}}=\mathbb{P}^{0}\circ(X^{\alpha})^{-1}. Clearly, we have ℙX0=ℙX\mathbb{P}\_{X^{0}}=\mathbb{P}\_{X}, where XX solves ([3.1](https://arxiv.org/html/2510.11829v1#S3.E1 "In 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). Furthermore, we shall denote 𝔼​[⋅]=𝔼ℙ0​[⋅]\mathbb{E}[\cdot]=\mathbb{E}^{\mathbb{P}^{0}}[\cdot] when context is clear, and for each k∈ℕk\in\mathbb{N} we can easily check that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jk​(α)=𝔼​[12​∫0T|αs|2​𝑑s+k​G​(ℙXTα)]=DKL​(ℙXα∥ℙX)+k​G​(ℙXTα).\displaystyle J^{k}(\alpha)=\mathbb{E}\Big[\frac{1}{2}\int\_{0}^{T}|\alpha\_{s}|^{2}ds+kG(\mathbb{P}\_{X^{\alpha}\_{T}})\Big]=D\_{\rm KL}(\mathbb{P}\_{X^{\alpha}}\|\mathbb{P}\_{X})+kG(\mathbb{P}\_{X^{\alpha}\_{T}}). |  | (3.3) |

Now let us define, for each k∈ℕk\in\mathbb{N}, a mapping Dk​(⋅):𝒫2​(ℝd)→ℝD\_{k}(\cdot):\mathscr{P}\_{2}(\mathbb{R}^{d})\to\mathbb{R} by

|  |  |  |
| --- | --- | --- |
|  | Dk​(μ)=DKL​(μ∥ℙXT)+k​G​(μ),D\_{k}(\mu)=D\_{\rm KL}(\mu\|\mathbb{P}\_{X\_{T}})+kG(\mu), |  |

and note that DKL​(ℙXα∥ℙX)≥DKL​(ℙXTα∥ℙXT)D\_{\rm KL}(\mathbb{P}\_{X^{\alpha}}\|\mathbb{P}\_{X})\geq D\_{\rm KL}(\mathbb{P}\_{X^{\alpha}\_{T}}\|\mathbb{P}\_{X\_{T}}),
we deduce from ([3.3](https://arxiv.org/html/2510.11829v1#S3.E3 "In 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jk​(α)≥DKL​(ℙXTα∥ℙXT)+k​G​(ℙXTα)=Dk​(ℙXTα).\displaystyle J^{k}(\alpha)\geq D\_{\rm KL}(\mathbb{P}\_{X^{\alpha}\_{T}}\|\mathbb{P}\_{X\_{T}})+kG(\mathbb{P}\_{X^{\alpha}\_{T}})=D\_{k}(\mathbb{P}\_{X^{\alpha}\_{T}}). |  | (3.4) |

If α^\widehat{\alpha} is the optimal control corresponding to the original SBP, that is, ℙXTα^=μtar\mathbb{P}\_{X^{\widehat{\alpha}}\_{T}}={\mu\_{\rm tar}}, then by definition of the penalty function G​(⋅)G(\cdot), we should have G​(μtar)=0G({\mu\_{\rm tar}})=0, and therefore,

|  |  |  |
| --- | --- | --- |
|  | Dk​(ℙXTα^)=Dk​(μtar)=DKL​(μtar∥ℙXT)+k​G​(μtar)=DKL​(μtar∥ℙXT).\displaystyle D\_{k}(\mathbb{P}\_{X^{\widehat{\alpha}}\_{T}})=D\_{k}({\mu\_{\rm tar}})=D\_{\rm KL}({\mu\_{\rm tar}}\|\mathbb{P}\_{X\_{T}})+kG({\mu\_{\rm tar}})=D\_{\rm KL}({\mu\_{\rm tar}}\|\mathbb{P}\_{X\_{T}}). |  |

Throughout the rest of this section, we shall focus on the special case: μini=δx0{\mu\_{\rm ini}}=\delta\_{x\_{0}} for some x0∈ℝdx\_{0}\in\mathbb{R}^{d}. The case with general initial distribution μini{\mu\_{\rm ini}} will be studied in Sections [5](https://arxiv.org/html/2510.11829v1#S5 "5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and [6](https://arxiv.org/html/2510.11829v1#S6 "6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"). We begin with the following well-known
result from [[18](https://arxiv.org/html/2510.11829v1#bib.bib18)], which will play an important role in our discussion.

###### Lemma 3.1 ( [[18](https://arxiv.org/html/2510.11829v1#bib.bib18), Theorem 3.1]).

Let XX be a weak solution to ([3.1](https://arxiv.org/html/2510.11829v1#S3.E1 "In 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) with X0=x0∈ℝdX\_{0}=x\_{0}\in\mathbb{R}^{d} (i.e., μini=δx0{\mu\_{\rm ini}}=\delta\_{x\_{0}}). Assume that DKL​(μtar∥ℙXT)<∞D\_{\rm KL}({\mu\_{\rm tar}}\|\mathbb{P}\_{X\_{T}})<\infty. Then, the optimal solution to the SBP ([2.4](https://arxiv.org/html/2510.11829v1#S2.E4 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"))-([2.5](https://arxiv.org/html/2510.11829v1#S2.E5 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) is given by α^t=∇log⁡h​(t,Xtα^)\widehat{\alpha}\_{t}=\nabla\log h(t,X^{\widehat{\alpha}}\_{t}), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(t,x)=∫ℝdp​(T,z;t,x)​ftar​(z)p​(T,z;0,x0)​𝑑z:=𝔼​[ftar​(XT)p​(T,XT;0,x0)|Xt=x],\displaystyle h(t,x)=\int\_{\mathbb{R}^{d}}p(T,z;t,x)\frac{f\_{\rm tar}(z)}{p(T,z;0,x\_{0})}dz:=\mathbb{E}\Big[\frac{f\_{\rm tar}(X\_{T})}{p(T,X\_{T};0,x\_{0})}\Big|X\_{t}=x\Big], |  | (3.5) |

for (t,x)∈[0,T]×ℝd(t,x)\in[0,T]\times\mathbb{R}^{d}.
∎

Next, we make the following assumptions on the penalty function GG:

###### Assumption 3.2.

(i) There exists some small constant ε>0\varepsilon>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(μ)→+∞,as​‖μ‖2+ε→+∞.G(\mu)\rightarrow+\infty,\quad\mathrm{as}\,\,\|\mu\|^{2+\varepsilon}\rightarrow+\infty. |  | (3.6) |

where ‖μ‖p:=∫ℝd|x|p​μ​(d​x)\|\mu\|^{p}:=\int\_{\mathbb{R}^{d}}|x|^{p}\mu(dx) for any p>0p>0.

(ii) There exist C,λ>0C,\lambda>0, and a function ϕ:ℝd→(0,1]\phi:\mathbb{R}^{d}\to(0,1] satisfying ϕ​(x)​eλ​|x−x0|2≤C\phi(x)e^{\lambda|x-x\_{0}|^{2}}\leq C, such that for any μ∈𝒫2​(ℝd)\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d}) with density function fμf\_{\mu}, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |fμ​(x)−ftar​(x)|≤C​ϕ​(x)​G​(μ),x∈ℝd.\displaystyle|f\_{\mu}(x)-f\_{\rm tar}(x)|\leq C\phi(x)G(\mu),\quad x\in\mathbb{R}^{d}. |  | (3.7) |

###### Remark 3.3.

(i) The function G​(μ)G(\mu) on the right hand side of ([3.7](https://arxiv.org/html/2510.11829v1#S3.E7 "In Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) should read |G​(μ)−G​(μtar)||G(\mu)-G({\mu\_{\rm tar}})|, as G​(μtar)=0G({\mu\_{\rm tar}})=0, which essentially states that if μ\mu is close to μtar{\mu\_{\rm tar}} in terms of GG, then fμf\_{\mu} is close to ftarf\_{\rm tar} in 𝕃1\mathbb{L}^{1}.

(ii) A slightly stronger consequence of ([3.7](https://arxiv.org/html/2510.11829v1#S3.E7 "In Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) is the following. Recall the (generalized) Kantorovich and Rubinstein dual representation (cf. e.g., [[23](https://arxiv.org/html/2510.11829v1#bib.bib23)]): denoting Lip(1)(1) to be all Lipschitz functions φ:ℝd→ℝ\varphi:\mathbb{R}^{d}\to\mathbb{R} with Lipschitz constant Lip≤φ1{}\_{\varphi}\leq 1 (hence |φ​(x)|≤C​(1+|x|)|\varphi(x)|\leq C(1+|x|)), then it holds that

|  |  |  |
| --- | --- | --- |
|  | W1​(μ,μtar)=supφ∈L​i​p​(1){∫ℝdφ​(x)​(fμ​(x)−ftar​(x))​𝑑x}≤C​G​(μ)​∫ℝd(1+|x|)​ϕ​(x)​𝑑x.\displaystyle W\_{1}(\mu,{\mu\_{\rm tar}})=\sup\_{\varphi\in Lip(1)}\left\{\int\_{\mathbb{R}^{d}}\varphi(x)(f\_{\mu}(x)-f\_{\rm tar}(x))dx\right\}\leq CG(\mu)\int\_{\mathbb{R}^{d}}(1+|x|)\phi(x)dx. |  |

This suggests that G​(μ)∼0G(\mu)\sim 0 implies that μ\mu is close to μtar{\mu\_{\rm tar}} in the sense of W1W\_{1}.
∎

Before we proceed, let us give two examples that justify Assumption [3.2](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday").

###### Example 3.4.

We consider the class of μ\mu and μtar{\mu\_{\rm tar}} such that

|  |  |  |
| --- | --- | --- |
|  | G​(μ):=∫ℝ|x|p​|fμ​(x)−ftar​(x)|​𝑑x,G(\mu):=\int\_{\mathbb{R}}|x|^{p}|f\_{\mu}(x)-f\_{\rm tar}(x)|dx, |  |

is well-defined for a given pp.
Clearly, Definition [2.3](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem3 "Definition 2.3. ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(i) and Assumption [3.2](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(i) are satisfied when p>2p>2. Assumption [3.2](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(i) holds when

|  |  |  |
| --- | --- | --- |
|  | ϕ​(x)≤|fμ​(x)−ftar​(x)|c​∫ℝ|x|p​|fμ​(x)−ftar​(x)|​𝑑x,\displaystyle\phi(x)\leq\frac{|f\_{\mu}(x)-f\_{\rm tar}(x)|}{c\int\_{\mathbb{R}}|x|^{p}|f\_{\mu}(x)-f\_{\rm tar}(x)|dx}, |  |

for all μ\mu in the collection one may consider.
∎

Another natural example of GG satisfying Assumption [3.2](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") would be the Wasserstein distance or the KL divergence, augmented with a small “guardrail” term that enforces the uniform (weighted) pointwise control in ([3.7](https://arxiv.org/html/2510.11829v1#S3.E7 "In Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). This guardrail can be taken as a weighted L∞L\_{\infty} norm, a Hölder ℂα\mathbb{C}^{\alpha} seminorm, or an RKHS norm (e.g., with kernel k​(x,y)=ϕ​(x)​ϕ​(y)​κ​(x−y)k(x,y)=\phi(x)\phi(y)\kappa(x-y)). In next example we illustrate such a choice with the Wasserstein distance plus an L∞L\_{\infty} guardrail.

###### Example 3.5.

Consider the case that μtar∈𝒫p​(ℝd){\mu\_{\rm tar}}\in\mathscr{P}\_{p}(\mathbb{R}^{d}) with p>2p>2.
We define, for c>0c>0 and ϕ​(x)=exp⁡(−λ​|x−x0|2)\phi(x)=\exp(-\lambda|x-x\_{0}|^{2}) with some x0∈ℝdx\_{0}\in\mathbb{R}^{d},

|  |  |  |
| --- | --- | --- |
|  | G​(μ):=W2​(μ,μtar)+c​‖fμ−ftarϕ‖L∞.\displaystyle G(\mu):=W\_{2}(\mu,{\mu\_{\rm tar}})+c\Big\|\frac{f\_{\mu}-f\_{\rm tar}}{\phi}\Big\|\_{L^{\infty}}. |  |

Then, it is easy to check that

|  |  |  |
| --- | --- | --- |
|  | |fμ​(x)−ftar​(x)|≤‖fμ−ftarϕ‖L∞​ϕ​(x)≤1c​ϕ​(x)​G​(μ).\displaystyle|f\_{\mu}(x)-f\_{\rm tar}(x)|\leq\Big\|\frac{f\_{\mu}-f\_{\rm tar}}{\phi}\Big\|\_{L^{\infty}}\phi(x)\leq\frac{1}{c}\phi(x)G(\mu). |  |

Thus ([3.7](https://arxiv.org/html/2510.11829v1#S3.E7 "In Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) holds and ϕ​(x)​eλ​|x−x0|2≤C\phi(x)e^{\lambda|x-x\_{0}|^{2}}\leq C holds with C=max⁡{1,1c}C=\max\{1,\frac{1}{c}\}.

Let {μn}n≥1⊂𝒫2​(ℝd)\{\mu\_{n}\}\_{n\geq 1}\subset\mathscr{P}\_{2}(\mathbb{R}^{d}) with ‖μn‖2+ε→∞\|\mu\_{n}\|^{2+\varepsilon}\rightarrow\infty. We claim that G​(μn)G(\mu\_{n}) must be unbounded. Indeed, suppose not. Then there exists M,M′>0M,M^{\prime}>0 such that
W22​(μn,μtar)≤MW\_{2}^{2}(\mu\_{n},{\mu\_{\rm tar}})\leq M and ‖ϕ−1​(fμn−ftar)‖L∞<M′\|\phi^{-1}(f\_{\mu\_{n}}-f\_{\rm tar})\|\_{L^{\infty}}<M^{\prime} for all n∈ℕ+n\in\mathbb{N}\_{+}. Hence fμn​(x)≤ftar​(x)+M′​ϕ​(x)f\_{\mu\_{n}}(x)\leq f\_{\rm tar}(x)+M^{\prime}\phi(x), x∈ℝdx\in\mathbb{R}^{d}.
Integrating against |x|2+ε|x|^{2+\varepsilon} and using the facts that μtar∈𝒫2+ε​(ℝd){\mu\_{\rm tar}}\in\mathscr{P}\_{2+\varepsilon}(\mathbb{R}^{d}) with ε=p−2>0\varepsilon=p-2>0 and ∫|x|2+ε​ϕ​(x)​𝑑x<∞\int|x|^{2+\varepsilon}\phi(x)dx<\infty, we have

|  |  |  |
| --- | --- | --- |
|  | ‖μn‖2+ε≤‖μtar‖2+ε+M′​∫|x|2+ε​ϕ​(x)​𝑑x<∞,n∈ℕ.\displaystyle\|\mu\_{n}\|^{2+\varepsilon}\leq\|{\mu\_{\rm tar}}\|^{2+\varepsilon}+M^{\prime}\int|x|^{2+\varepsilon}\phi(x)dx<\infty,\qquad n\in\mathbb{N}. |  |

This contradicts the fact that ‖μn‖2+ε→∞\|\mu\_{n}\|^{2+\varepsilon}\rightarrow\infty, proving the claim. Hence
([3.6](https://arxiv.org/html/2510.11829v1#S3.E6 "In Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) holds.
∎

We are now ready to investigate the existence of optimal control of Problem [2.4](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem4 "Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") for each k∈ℕk\in\mathbb{N}, which would be essential for our approximation scheme. Recall that in the rest of the section we assume that μini=δx0{\mu\_{\rm ini}}=\delta\_{x\_{0}} for some x0∈ℝdx\_{0}\in\mathbb{R}^{d}.
To begin with, we first claim that for each k∈ℕk\in\mathbb{N}, there exists μ^k∈𝒫2​(ℝd)\widehat{\mu}\_{k}\in\mathscr{P}\_{2}(\mathbb{R}^{d}) such that the static optimization problem on the measure space has a solution

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dk​(μ^k)=infμ∈𝒫2​(ℝd)Dk​(μ).\displaystyle D\_{k}(\widehat{\mu}\_{k})=\inf\_{\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d})}D\_{k}(\mu). |  | (3.8) |

Indeed, let XX be the solution to uncontrolled SDE ([2.6](https://arxiv.org/html/2510.11829v1#S2.E6 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), and μtar{\mu\_{\rm tar}} be given such that DKL​(μtar∥ℙXT)<∞D\_{\rm KL}({\mu\_{\rm tar}}\|\mathbb{P}\_{X\_{T}})<\infty. Since G​(μtar)=0G({\mu\_{\rm tar}})=0, we have

|  |  |  |
| --- | --- | --- |
|  | m:=Dk​(μtar)=DKL​(μtar∥ℙXT)+k​G​(μtar)=DKL​(μtar∥ℙXT)<∞.\displaystyle m:=D\_{k}({\mu\_{\rm tar}})=D\_{\rm KL}({\mu\_{\rm tar}}\|\mathbb{P}\_{X\_{T}})+kG({\mu\_{\rm tar}})=D\_{\rm KL}({\mu\_{\rm tar}}\|\mathbb{P}\_{X\_{T}})<\infty. |  |

Next, let us define, for fixed k∈ℕk\in\mathbb{N}, a set

|  |  |  |
| --- | --- | --- |
|  | 𝒮k:={μ∈𝒫2​(ℝd):Dk​(μ)≤m}.\displaystyle\mathcal{S}\_{k}:=\Big\{\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d}):D\_{k}(\mu)\leq m\Big\}. |  |

Clearly, 𝒮k≠∅\mathcal{S}\_{k}\neq\emptyset since μtar∈𝒮k{\mu\_{\rm tar}}\in\mathcal{S}\_{k}, and by ([3.6](https://arxiv.org/html/2510.11829v1#S3.E6 "In Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), there exists Mk>0M\_{k}>0 such that
‖μ‖2+ε≤Mk\|\mu\|^{2+\varepsilon}\leq M\_{k}, for all μ∈𝒮k\mu\in\mathcal{S}\_{k}. Thus 𝒮k{\cal S}\_{k} is uniformly integrable in 𝕃2\mathbb{L}^{2}. Now let {μk(i)}i=1∞⊂𝒫2​(ℝd)\{\mu\_{k}^{(i)}\}\_{i=1}^{\infty}\subset\mathscr{P}\_{2}(\mathbb{R}^{d}) be a minimizing sequence, namely,

|  |  |  |
| --- | --- | --- |
|  | limi→∞Dk​(μk(i))=infμ∈𝒫2​(ℝd)Dk​(μ).\displaystyle\lim\_{i\rightarrow\infty}D\_{k}(\mu\_{k}^{(i)})=\inf\_{\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d})}D\_{k}(\mu). |  |

Since infμ∈𝒫2​(ℝd)Dk​(μ)≤Dk​(μtar)=m\inf\_{\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d})}D\_{k}(\mu)\leq D\_{k}({\mu\_{\rm tar}})=m, we may assume without loss of generality that

{μk(i)}i=1∞⊂𝒮k\{\mu\_{k}^{(i)}\}\_{i=1}^{\infty}\subset\mathcal{S}\_{k}. Since 𝒮k\mathcal{S}\_{k} is uniformly integrable and is tight
in 𝒫2​(ℝd)\mathscr{P}\_{2}(\mathbb{R}^{d}), there exists subsequence {μk(il)}l=1∞\{\mu\_{k}^{(i\_{l})}\}\_{l=1}^{\infty} such that
μ^k:=liml→∞μk(il)∈𝒫2​(ℝd)\widehat{\mu}\_{k}:=\lim\_{l\rightarrow\infty}\mu\_{k}^{(i\_{l})}\in\mathscr{P}\_{2}(\mathbb{R}^{d})333This follows from the result on
Wasserstein distance vs. weak convergence (see, e.g., [[65](https://arxiv.org/html/2510.11829v1#bib.bib65), Theorem 7.12]), which states that Wp​(μk,μ)→0W\_{p}(\mu\_{k},\mu)\to 0 if and only if μk→μ\mu\_{k}\to\mu weakly, and limR→∞lim¯k→∞∫{d​(x,x0)≥R}d​(x,x0)p​μk​(d​x)=0\lim\_{R\to\infty}\mathop{\overline{\rm lim}}\_{k\to\infty}\int\_{\{d(x,x\_{0})\geq R\}}d(x,x\_{0})^{p}\mu\_{k}(dx)=0..
Since the mapping μ↦Dk​(μ)\mu\mapsto D\_{k}(\mu) is continuous, we have

|  |  |  |
| --- | --- | --- |
|  | Dk​(μ^k)=DKL​(μ^k∥ℙXT)+k​G​(μ^k)=infμ∈𝒫2​(ℝd)Dk​(μ),\displaystyle D\_{k}(\widehat{\mu}\_{k})=D\_{\rm KL}(\widehat{\mu}\_{k}\|\mathbb{P}\_{X\_{T}})+kG(\widehat{\mu}\_{k})=\inf\_{\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d})}D\_{k}(\mu), |  |

proving the claim. Furthermore, if we denote the density of ℙXT\mathbb{P}\_{X\_{T}} by fXTf\_{X\_{T}}, and note that DKL​(μ^k;ℙXT)≤Dk​(μ^k)≤m<∞D\_{\rm KL}(\widehat{\mu}\_{k};\mathbb{P}\_{X\_{T}})\leq D\_{k}(\widehat{\mu}\_{k})\leq m<\infty, we know that d​μ^kd​ℙXT\frac{d\widehat{\mu}\_{k}}{d\mathbb{P}\_{X\_{T}}} exists and

|  |  |  |
| --- | --- | --- |
|  | d​μ^kd​x(x)=d​μ^kd​ℙXT⋅fXT(x)=:fk(x).\frac{d\widehat{\mu}\_{k}}{dx}(x)=\frac{d\widehat{\mu}\_{k}}{d\mathbb{P}\_{X\_{T}}}\cdot f\_{X\_{T}}(x)=:f\_{k}(x). |  |

Keeping the above discussion in mind, we are now ready to prove the following theorem.

###### Proposition 3.6.

Assume that Assumption [3.2](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") is in force, and that μini=δx0{\mu\_{\rm ini}}=\delta\_{x\_{0}}, x0∈ℝdx\_{0}\in\mathbb{R}^{d}.
Then, for each k∈ℕk\in\mathbb{N}, the optimal control for Problem [2.4](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem4 "Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), denoted by α^k\widehat{\alpha}^{k}, exists. Furthermore, α^k\widehat{\alpha}^{k} has the following explicit feedback form: α^tk:=∇log⁡hk​(t,Xtα^k)\widehat{\alpha}^{k}\_{t}:=\nabla\log h^{k}(t,X^{\widehat{\alpha}^{k}}\_{t}), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | hk​(t,x)=∫ℝdfk​(z)p​(T,z;0,x0)​p​(T,z;t,x)​𝑑z=𝔼​[fk​(XT)p​(T,XT;0,x0)|Xt=x].\displaystyle h^{k}(t,x)=\int\_{\mathbb{R}^{d}}\frac{f\_{k}(z)}{p(T,z;0,x\_{0})}p(T,z;t,x)dz=\mathbb{E}\Big[\frac{f\_{k}(X\_{T})}{p(T,X\_{T};0,x\_{0})}\Big|X\_{t}=x\Big]. |  | (3.9) |

###### Proof.

Let k∈ℕk\in\mathbb{N} be fixed, and let μ^k\widehat{\mu}\_{k} be the minimizer of Dk​(⋅)D\_{k}(\cdot) defined by ([3.8](https://arxiv.org/html/2510.11829v1#S3.E8 "In 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). Then, by ([3.4](https://arxiv.org/html/2510.11829v1#S3.E4 "In 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), for
any α∈𝕃𝔽02​([0,T])\alpha\in\mathbb{L}^{2}\_{\mathbb{F}^{0}}([0,T]), we have

|  |  |  |
| --- | --- | --- |
|  | Jk​(α)≥Dk​(ℙXTα)≥Dk​(μ^k),\displaystyle J^{k}(\alpha)\geq D\_{k}(\mathbb{P}\_{X^{\alpha}\_{T}})\geq D\_{k}(\widehat{\mu}\_{k}), |  |

Therefore, in order to find the optimal control for Problem [2.4](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem4 "Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") , it suffices to find α^k\widehat{\alpha}^{k} such that (i) XTα^k∼μ^k\ X^{\widehat{\alpha}^{k}}\_{T}\sim\widehat{\mu}\_{k}; and (ii) Jk​(α^k)=Dk​(ℙXTα^k)J^{k}(\widehat{\alpha}^{k})=D\_{k}(\mathbb{P}\_{X^{\widehat{\alpha}^{k}}\_{T}}).

To this end, we first recall that μ^k\widehat{\mu}\_{k} is the minimizer of the function Dk​(⋅)D\_{k}(\cdot) with density fkf\_{k}. Next, we apply Lemma [3.1](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem1 "Lemma 3.1 ( [18, Theorem 3.1]). ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") with μtar{\mu\_{\rm tar}} being replaced by μ^k\widehat{\mu}\_{k} to get the optimal control α^k∈𝒫​(μini,μ^k)\widehat{\alpha}^{k}\in\mathscr{P}({\mu\_{\rm ini}},\widehat{\mu}\_{k}) for the original SBP ([2.5](https://arxiv.org/html/2510.11829v1#S2.E5 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"))-([2.6](https://arxiv.org/html/2510.11829v1#S2.E6 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), which satisfies α^tk=∇log⁡hk​(t,Xtα^k)\widehat{\alpha}^{k}\_{t}=\nabla\log h^{k}(t,X^{\widehat{\alpha}^{k}}\_{t}), where hkh^{k} is defined by ([3.9](https://arxiv.org/html/2510.11829v1#S3.E9 "In Proposition 3.6. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), and XTα^k∼μ^k\ X^{\widehat{\alpha}^{k}}\_{T}\sim\widehat{\mu}\_{k}. Now, note that for this SBP we have

|  |  |  |
| --- | --- | --- |
|  | V​(μini,μ^k)=12​𝔼​[∫0T|α^sk|2​𝑑s]=DKL​(μ^k∥ℙXT),V({\mu\_{\rm ini}},\widehat{\mu}\_{k})=\frac{1}{2}\mathbb{E}\Big[\int\_{0}^{T}|\widehat{\alpha}^{k}\_{s}|^{2}ds\Big]=D\_{\rm KL}(\widehat{\mu}\_{k}\|\mathbb{P}\_{X\_{T}}), |  |

we conclude that

|  |  |  |
| --- | --- | --- |
|  | Jk​(α^k)=DKL​(μ^k∥ℙXT)+k​G​(μ^k)=Dk​(μ^k)=Dk​(ℙXTα^k).J^{k}(\widehat{\alpha}^{k})=D\_{\rm KL}(\widehat{\mu}\_{k}\|\mathbb{P}\_{X\_{T}})+kG(\widehat{\mu}\_{k})=D\_{k}(\widehat{\mu}\_{k})=D\_{k}(\mathbb{P}\_{X^{\widehat{\alpha}^{k}}\_{T}}). |  |

In other words, α^k\widehat{\alpha}^{k} is indeed the optimal control for the Problem [2.4](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem4 "Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), proving the proposition.
∎

## 4 Convergence Results under Delta Initial Distribution

We make the following two observations. First, if we denote g​(x):=ftar​(x)p​(T,x;0,x0)g(x):=\frac{f\_{\rm tar}(x)}{p(T,x;0,x\_{0})}, then by ([3.5](https://arxiv.org/html/2510.11829v1#S3.E5 "In Lemma 3.1 ( [18, Theorem 3.1]). ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) we can write h​(t,x)=𝔼t,x​[g​(XT)]:=𝔼​[g​(XT)|Xt=x]h(t,x)=\mathbb{E}\_{t,x}[g(X\_{T})]:=\mathbb{E}[g(X\_{T})|X\_{t}=x], where XX is the solution to ([3.1](https://arxiv.org/html/2510.11829v1#S3.E1 "In 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) with X0=x0X\_{0}=x\_{0}.
By Feynman-Kac formula, we see that hh satisfy the PDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∂th​(t,x)+ℒt​h​(t,x)=0;h​(T,x)=g​(x)=ftar​(x)p​(T,x;0,x0),\displaystyle\begin{cases}\partial\_{t}h(t,x)+\mathscr{L}\_{t}h(t,x)=0;\\ h(T,x)=g(x)=\frac{f\_{\rm tar}(x)}{p(T,x;0,x\_{0})},\end{cases} |  | (4.1) |

where the infinitesimal generator ℒt\mathscr{L}\_{t} is defined by ℒt:=b​(t,x)⋅∇+12​Δ\mathscr{L}\_{t}:=b(t,x)\cdot\nabla+\frac{1}{2}\Delta. Similarly, we define gk​(x):=fk​(x)p​(T,x;0,x0)g\_{k}(x):=\frac{f\_{k}(x)}{p(T,x;0,x\_{0})}, then the function
hk​(t,x)h^{k}(t,x) can also be represented as the solution of the PDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∂thk​(t,x)+ℒt​hk​(t,x)=0;hk​(T,x)=gk​(x)=fk​(x)p​(T,x;0,x0).\displaystyle\begin{cases}\partial\_{t}h^{k}(t,x)+\mathscr{L}\_{t}h^{k}(t,x)=0;\\ h^{k}(T,x)=g\_{k}(x)=\frac{f\_{k}(x)}{p(T,x;0,x\_{0})}.\end{cases} |  | (4.2) |

Recall that μ^k∈𝒮k\widehat{\mu}\_{k}\in{\cal S}\_{k}, we have k​G​(μ^k)≤Dk​(μ^k)≤mkG(\widehat{\mu}\_{k})\leq D\_{k}(\widehat{\mu}\_{k})\leq m, or

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(μ^k)≤m/k.G(\widehat{\mu}\_{k})\leq m/k. |  | (4.3) |

Then Assumption [3.2](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(ii) amounts to saying that |fk​(x)−ftar​(x)|≤C′k|f\_{k}(x)-f\_{\rm tar}(x)|\leq\frac{C^{\prime}}{k} with constant C′=C​m​MC^{\prime}=CmM.
In other words, for all x∈ℝdx\in\mathbb{R}^{d}, as k→∞k\to\infty we have

|  |  |  |
| --- | --- | --- |
|  | {|g​(x)−gk​(x)|=|h​(T,x)−hk​(T,x)|=1p​(T,x;0,x0)​|ftar​(x)−fk​(x)|→0|h​(t,x)−hk​(t,x)|≤∫ℝdp​(T,z;t,x)p​(T,z;0,x0)​|ftar​(z)−fk​(z)|​𝑑z→0,\displaystyle\left\{\begin{array}[]{lll}\displaystyle|g(x)-g\_{k}(x)|=|h(T,x)-h^{k}(T,x)|=\frac{1}{p(T,x;0,x\_{0})}|f\_{\rm tar}(x)-f\_{k}(x)|\to 0\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \displaystyle|h(t,x)-h^{k}(t,x)|\leq\int\_{\mathbb{R}^{d}}\frac{p(T,z;t,x)}{p(T,z;0,x\_{0})}|f\_{\rm tar}(z)-f\_{k}(z)|dz\to 0,\end{array}\right. |  |

We shall use these facts to study the convergence of the optimal policies in the next subsection.

### 4.1 The Convergence of Optimal Policies

We shall now argue that the optimal controls for Problem [2.4](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem4 "Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), {α^k​(⋅,⋅)}\{\widehat{\alpha}^{k}(\cdot,\cdot)\}, given by Proposition [3.6](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem6 "Proposition 3.6. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), actually converges to the solution of the original SBP α^​(⋅,⋅)\widehat{\alpha}(\cdot,\cdot) given by Lemma [3.1](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem1 "Lemma 3.1 ( [18, Theorem 3.1]). ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), and also establish its rate of convergence. More precisely, we have the following theorem.

###### Theorem 4.1.

Assume that the Assumption [3.2](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") is in force, and that μini=δx0{\mu\_{\rm ini}}=\delta\_{x\_{0}} for some x0∈ℝdx\_{0}\in\mathbb{R}^{d}.
Furthermore, assume that there exists constants C,δ>0C,\delta>0, such that δ≤g​(x),gk​(x)≤C\delta\leq g(x),g\_{k}(x)\leq C, x∈ℝdx\in\mathbb{R}^{d}, k∈ℕk\in\mathbb{N}. Let α^​(t,x)\widehat{\alpha}(t,x) and α^k​(t,x)\widehat{\alpha}^{k}(t,x), (t,x)∈[0,T]×ℝd(t,x)\in[0,T]\times\mathbb{R}^{d} be the optimal controls given in Lemma [3.1](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem1 "Lemma 3.1 ( [18, Theorem 3.1]). ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and Proposition [3.6](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem6 "Proposition 3.6. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), respectively. Then, it holds that

|  |  |  |
| --- | --- | --- |
|  | ∫0T|α^k​(t,x)−α^​(t,x)|​𝑑t≤Ck,x∈ℝd,\int\_{0}^{T}|\widehat{\alpha}^{k}(t,x)-\widehat{\alpha}(t,x)|dt\leq\frac{C}{k},\qquad x\in\mathbb{R}^{d}, |  |

where C>0C>0 is some constant independent of kk.

###### Remark 4.2.

We note that the assumption δ≤g​(x)=ftar​(x)P​(T,x;0,x0)≤C\delta\leq g(x)=\frac{f\_{\rm tar}(x)}{P(T,x;0,x\_{0})}\leq C (resp. δ≤gk​(x)≤C\delta\leq g\_{k}(x)\leq C) amounts to saying that ftar​(x)f\_{\rm tar}(x) (resp. fk​(x)f\_{k}(x)) ∝P​(T,x;0,x0)\propto\,P(T,x;0,x\_{0}) as x→∞x\to\infty, which is not particularly a stringent condition in light of the general estimate ([3.2](https://arxiv.org/html/2510.11829v1#S3.E2 "In 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), and the arbitrariness of the sample data selection for the data generation procedure.
∎

###### Proof.

First, by definition α^​(t,x)=∇log⁡h​(t,x)\widehat{\alpha}(t,x)=\nabla\log h(t,x) and α^k​(t,x)=∇log⁡hk​(t,x)\widehat{\alpha}^{k}(t,x)=\nabla\log h^{k}(t,x), where hkh^{k} and hh are the solution to ([4.1](https://arxiv.org/html/2510.11829v1#S4.E1 "In 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) and ([4.2](https://arxiv.org/html/2510.11829v1#S4.E2 "In 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), respectively, and ∇=∂x\nabla=\partial\_{x}. We can easily deduce that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |α^k​(t,x)−α^​(t,x)|\displaystyle|\widehat{\alpha}^{k}(t,x)-\widehat{\alpha}(t,x)| | =\displaystyle= | |∇log⁡hk​(t,x)−∇log⁡h​(t,x)|=|∇hk​(t,x)hk​(t,x)−∇h​(t,x)h​(t,x)|\displaystyle|\nabla\log h^{k}(t,x)-\nabla\log h(t,x)|=\left|\frac{\nabla h^{k}(t,x)}{h^{k}(t,x)}-\frac{\nabla h(t,x)}{h(t,x)}\right| |  |
|  |  | =\displaystyle= | |∇hk​(t,x)​h​(t,x)−∇h​(t,x)​h​(t,x)+∇h​(t,x)​h​(t,x)−∇h​(t,x)​hk​(t,x)hk​(t,x)​h​(t,x)|\displaystyle\left|\frac{\nabla h^{k}(t,x)h(t,x)-\nabla h(t,x)h(t,x)+\nabla h(t,x)h(t,x)-\nabla h(t,x)h^{k}(t,x)}{h^{k}(t,x)h(t,x)}\right| |  |
|  |  | ≤\displaystyle\leq | |∇hk​(t,x)−∇h​(t,x)hk​(t,x)|+|∇h​(t,x)|​|h​(t,x)−hk​(t,x)hk​(t,x)​h​(t,x)|:=I1+I2.\displaystyle\left|\frac{\nabla h^{k}(t,x)-\nabla h(t,x)}{h^{k}(t,x)}\right|+|\nabla h(t,x)|\left|\frac{h(t,x)-h^{k}(t,x)}{h^{k}(t,x)h(t,x)}\right|:=I\_{1}+I\_{2}. |  |

We now estimate I1I\_{1} and I2I\_{2}, respectively. To this end we first apply the well-known Bismut-Elworthy-Li formula [[8](https://arxiv.org/html/2510.11829v1#bib.bib8), [24](https://arxiv.org/html/2510.11829v1#bib.bib24)] (see also the representation formula in [[27](https://arxiv.org/html/2510.11829v1#bib.bib27), [43](https://arxiv.org/html/2510.11829v1#bib.bib43)]) to get

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∇h​(t,x)=∂x𝔼t,x​[g​(XT)]=𝔼t,x​[g​(XT)​NT],∇hk​(t,x)=∂x𝔼t,x​[gk​(XT)]=𝔼t,x​[gk​(XT)​NT],\displaystyle\left\{\begin{array}[]{lll}\nabla h(t,x)=\partial\_{x}\mathbb{E}\_{t,x}[g(X\_{T})]=\mathbb{E}\_{t,x}\big[g(X\_{T})N\_{T}\big],\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \nabla h^{k}(t,x)=\partial\_{x}\mathbb{E}\_{t,x}[g\_{k}(X\_{T})]=\mathbb{E}\_{t,x}\big[g\_{k}(X\_{T})N\_{T}\big],\end{array}\right. |  | (4.8) |

where,

|  |  |  |
| --- | --- | --- |
|  | Ns=Nst,x:=1s−t​∫ts(∇Xrt,x)⊤​𝑑Wr,s∈[t,T],\displaystyle N\_{s}=N^{t,x}\_{s}:=\frac{1}{s-t}\int\_{t}^{s}(\nabla X^{t,x}\_{r})^{\top}dW\_{r},\qquad s\in[t,T], |  |

and ∇X=∇Xt,x\nabla X=\nabla X^{t,x} is a ℝd×d\mathbb{R}^{d\times d}-valued variational process satisfying the (random) ODE:

|  |  |  |
| --- | --- | --- |
|  | ∂xjXsi=δi​j+∫ts∑ℓ=1d∂xℓbi​(r,Xr)​∂xjXrℓ​d​r,1≤i,j≤d,s∈[t,T].\displaystyle\partial\_{x^{j}}X^{i}\_{s}=\delta\_{ij}+\int\_{t}^{s}\sum\_{\ell=1}^{d}\partial\_{x^{\ell}}b^{i}(r,X\_{r})\partial\_{x^{j}}X^{\ell}\_{r}dr,\qquad 1\leq i,j\leq d,\quad s\in[t,T]. |  |

Furthermore,
one can easily check that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|∇Xst,x|2]≤C​eC​(s−t),𝔼​[|Nst,x|2]≤Cs−t​eC​(s−t),0≤t≤s≤T.\displaystyle\mathbb{E}\big[|\nabla X^{t,x}\_{s}|^{2}\big]\leq Ce^{C(s-t)},\qquad\mathbb{E}\big[|N^{t,x}\_{s}|^{2}\big]\leq{C\over s-t}e^{C(s-t)},\qquad 0\leq t\leq s\leq T. |  |

Therefore, denoting C>0C>0 to be a generic constant that is allowed to vary from line to line, and applying Assumption [3.7](https://arxiv.org/html/2510.11829v1#S3.E7 "In Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and estimate ([3.2](https://arxiv.org/html/2510.11829v1#S3.E2 "In 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |∇hk​(t,x)−∇h​(t,x)|≤𝔼​[|g​(XTt,x)−gk​(XTt,x)|​|NTt,x|]=𝔼​[|fk​(XTt,x)−ftar​(XTt,x)p​(T,XTt,x;0,x0)|​|NTt,x|]≤(𝔼​[|NTt,x|2])12​[𝔼​|fk​(XTt,x)−ftar​(XTt,x)p​(T,XTt,x;0,x0)|2]12≤C​eC​(T−t)T−t​G​(μ^k)​[𝔼​|ϕ​(XTt,x)p​(T,XTt,x;0,x0)|2]12≤Ck​T−t.\displaystyle\begin{split}|\nabla h^{k}(t,x)-\nabla h(t,x)|&\leq\mathbb{E}\big[|g(X^{t,x}\_{T})-g\_{k}(X^{t,x}\_{T})||N^{t,x}\_{T}|\big]=\mathbb{E}\Big[\Big|\frac{f\_{k}(X^{t,x}\_{T})-f\_{\rm tar}(X^{t,x}\_{T})}{p(T,X^{t,x}\_{T};0,x\_{0})}\Big||N^{t,x}\_{T}|\Big]\\ &\leq\Big(\mathbb{E}[|N^{t,x}\_{T}|^{2}]\Big)^{\frac{1}{2}}\Big[\mathbb{E}\Big|\frac{f\_{k}(X^{t,x}\_{T})-f\_{\rm tar}(X^{t,x}\_{T})}{p(T,X^{t,x}\_{T};0,x\_{0})}\Big|^{2}\Big]^{\frac{1}{2}}\\ &\leq\frac{Ce^{C(T-t)}}{\sqrt{T-t}}G(\widehat{\mu}\_{k})\Big[\mathbb{E}\Big|\frac{\phi(X^{t,x}\_{T})}{p(T,X^{t,x}\_{T};0,x\_{0})}\Big|^{2}\Big]^{\frac{1}{2}}\leq\frac{C}{k\sqrt{T-t}}.\end{split} | |  | (4.9) |

Next, we note that by assumption δ≤g​(x),gk​(x)≤C\delta\leq g(x),g\_{k}(x)\leq C for all x∈ℝdx\in\mathbb{R}^{d} and k∈ℕk\in\mathbb{N}, by the weak maximum principle we conclude that as the solutions to the PDEs ([4.1](https://arxiv.org/html/2510.11829v1#S4.E1 "In 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) and ([4.2](https://arxiv.org/html/2510.11829v1#S4.E2 "In 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), respectively, it holds that δ≤h​(t,x),hk​(t,x)≤C\delta\leq h(t,x),h^{k}(t,x)\leq C, for all (t,x)∈ℝd×[0,T)(t,x)\in\mathbb{R}^{d}\times[0,T).
Consequently, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | I1≤Cδ​k​T−t≤Ck​T−t.I\_{1}\leq\frac{C}{\delta k\sqrt{T-t}}\leq\frac{C}{k\sqrt{T-t}}. |  | (4.10) |

Similarly, we can argue that |∇h​(t,x)|≤CT−t|\nabla h(t,x)|\leq\frac{C}{\sqrt{T-t}}, and that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |hk​(t,x)−h​(t,x)|≤𝔼​[|fk​(XTt,x)−ftar​(XTt,x)p​(T,XTt,x;0,x0)|]≤C​G​(μ^k)​𝔼​[|ϕ​(XTt,x)p​(T,XTt,x;0,x0)|]≤Ck,\displaystyle|h^{k}(t,x)-h(t,x)|\leq\mathbb{E}\Big[\Big|\frac{f\_{k}(X^{t,x}\_{T})-f\_{\rm tar}(X^{t,x}\_{T})}{p(T,X^{t,x}\_{T};0,x\_{0})}\Big|\Big]\leq CG(\widehat{\mu}\_{k})\mathbb{E}\Big[\Big|\frac{\phi(X^{t,x}\_{T})}{p(T,X^{t,x}\_{T};0,x\_{0})}\Big|\Big]\leq\frac{C}{k}, |  | (4.11) |

where the last inequality is due to ([4.3](https://arxiv.org/html/2510.11829v1#S4.E3 "In 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) and hence I2≤Ck​T−tI\_{2}\leq\frac{C}{k\sqrt{T-t}}. This, together with ([4.10](https://arxiv.org/html/2510.11829v1#S4.E10 "In 4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) and ([4.1](https://arxiv.org/html/2510.11829v1#S4.Ex5 "4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | |α^k​(t,x)−α^​(t,x)|≤Ck​T−t\displaystyle|\widehat{\alpha}^{k}(t,x)-\widehat{\alpha}(t,x)|\leq\frac{C}{k\sqrt{T-t}} |  | (4.12) |

and hence convergence result :

|  |  |  |
| --- | --- | --- |
|  | ∫0T|α^k​(t,x)−α^​(t,x)|​𝑑t≤∫0TCk​T−t​𝑑t≤C​Tk,\displaystyle\int\_{0}^{T}|\widehat{\alpha}^{k}(t,x)-\widehat{\alpha}(t,x)|dt\leq\int\_{0}^{T}\frac{C}{k\sqrt{T-t}}dt\leq\frac{C\sqrt{T}}{k}, |  |

proving the theorem.
∎

###### Remark 4.3.

A particular example is when we take the penalty function G​(μ)=DKL​(μ∥μtar)G(\mu)=D\_{\rm KL}(\mu\|{\mu\_{\rm tar}}). In this case, it is known
(see, e.g., [[29](https://arxiv.org/html/2510.11829v1#bib.bib29), Theorem 2]) that the optimal control for ([2.9](https://arxiv.org/html/2510.11829v1#S2.E9 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"))-([2.10](https://arxiv.org/html/2510.11829v1#S2.E10 "In Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) is given by
α^tk=∇log⁡hk​(Xtα^k,t)\widehat{\alpha}\_{t}^{k}=\nabla\log h^{k}(X\_{t}^{\widehat{\alpha}^{k}},t), where

|  |  |  |
| --- | --- | --- |
|  | hk(t,x)=dk−1∫p(T,z,;t,x)(ftar​(z)p​(T,z;0,x0))kk+1dz,\displaystyle h^{k}(t,x)=d\_{k}^{-1}\int p(T,z,;t,x)\Big(\frac{f\_{\rm tar}(z)}{p(T,z;0,x\_{0})}\Big)^{\frac{k}{k+1}}dz, |  |

with dk=∫ftar​(x)k1+k​p​(x,T|x0,0)11+k​𝑑xd\_{k}=\int f\_{\rm tar}(x)^{\frac{k}{1+k}}p(x,T\,|\,x\_{0},0)^{\frac{1}{1+k}}dx. In addition, Jk​(α^)=−(1+k)​log⁡(Ck)J^{k}(\widehat{\alpha})=-(1+k)\,\log(C\_{k}).
Consequently, Assumption [3.2](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(ii) can be reduced to that 𝔼​[|ftar​(XT)p​(T,XT;0,x0)|2]\mathbb{E}\Big[\big|\frac{f\_{\rm tar}(X\_{T})}{p(T,X\_{T};0,x\_{0})}\big|^{2}\Big] is bounded (see Assumption [5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") for similar conditions); and the linear rate of convergence can be proved with the same arguments.
∎

### 4.2 The Convergence of the Value Function

Having worked out the convergence analysis for the optimal controls, it is natural to extend the results to the convergence of value functions. However, the singularity at the terminal time TT in ([4.12](https://arxiv.org/html/2510.11829v1#S4.E12 "In 4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) requires some technical care. It turns out that the popular notion of early stopping in diffusion models as well as the flow-based method literature [[4](https://arxiv.org/html/2510.11829v1#bib.bib4), [41](https://arxiv.org/html/2510.11829v1#bib.bib41), [33](https://arxiv.org/html/2510.11829v1#bib.bib33)] is exactly the remedy to this issue.

To be more precise, for any ε>0\varepsilon>0, we introduce the following ε\varepsilon-value function.

|  |  |  |
| --- | --- | --- |
|  | Jε​(α):=𝔼​[∫0T−ε12​|α|2​𝑑t].\displaystyle J\_{\varepsilon}(\alpha):=\mathbb{E}\left[\int\_{0}^{T-\varepsilon}\frac{1}{2}|\alpha|^{2}dt\right]. |  |

There are many practical reasons, mainly for computational purposes, to invoke the notion of early stopping, as elaborated in
[[4](https://arxiv.org/html/2510.11829v1#bib.bib4), [41](https://arxiv.org/html/2510.11829v1#bib.bib41), [33](https://arxiv.org/html/2510.11829v1#bib.bib33)]. But on the other hand, it is clear that the ε\varepsilon-value function effectively excludes the singularity at the terminal time TT. This leads to the following straightforward result.

###### Proposition 4.4.

Assume that all the assumptions of Theorem [4.1](https://arxiv.org/html/2510.11829v1#S4.ThmTheorem1 "Theorem 4.1. ‣ 4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") are in force. Then, for any ε>0\varepsilon>0, there exists a generic constant C:=C​(ε)=𝒪​(1ε)>0C:=C(\varepsilon)=\mathcal{O}(\frac{1}{\sqrt{\varepsilon}})>0, independent of kk, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Jε​(α^k)−Jε​(α^)|≤Ck,k∈ℕ.\displaystyle|J\_{\varepsilon}(\widehat{\alpha}^{k})-J\_{\varepsilon}(\widehat{\alpha})|\leq\frac{C}{k},\qquad k\in\mathbb{N}. |  | (4.13) |

where α^k\widehat{\alpha}^{k} and α^\widehat{\alpha} are the optimal controls in Theorem [4.1](https://arxiv.org/html/2510.11829v1#S4.ThmTheorem1 "Theorem 4.1. ‣ 4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), respectively.

###### Proof.

The proof is straightforward. For any k∈ℕk\in\mathbb{N}, let α^k\widehat{\alpha}^{k} and α^\widehat{\alpha} be the optimal controls in Theorem [4.1](https://arxiv.org/html/2510.11829v1#S4.ThmTheorem1 "Theorem 4.1. ‣ 4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), respectively. Then, for any ε>0\varepsilon>0, applying ([4.12](https://arxiv.org/html/2510.11829v1#S4.E12 "In 4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |Jε​(α^k)−Jε​(α^)|\displaystyle|J\_{\varepsilon}(\widehat{\alpha}^{k})-J\_{\varepsilon}(\widehat{\alpha})|\negthinspace | ≤\displaystyle\negthinspace\leq\negthinspace | 𝔼​[12​∫0T−ε||α^sk|2−|α^s|2|​𝑑s]≤𝔼​[12​∫0T−ε|α^sk−α^s|​(|α^sk|+|α^s|)​𝑑s]\displaystyle\negthinspace\mathbb{E}\Big[\frac{1}{2}\int\_{0}^{T-\varepsilon}\big||\widehat{\alpha}^{k}\_{s}|^{2}-|\widehat{\alpha}\_{s}|^{2}\big|ds\Big]\leq\mathbb{E}\Big[\frac{1}{2}\int\_{0}^{T-\varepsilon}\big|\widehat{\alpha}^{k}\_{s}-\widehat{\alpha}\_{s}\big|\big(|\widehat{\alpha}^{k}\_{s}|+|\widehat{\alpha}\_{s}|\big)ds\Big] |  |
|  |  | ≤\displaystyle\negthinspace\leq\negthinspace | ck​𝔼​[12​∫0T−ε1T−s​(|α^sk|+|α^s|)​𝑑s]≤ck​ε​𝔼​[12​∫0T(|α^sk|+|α^s|)​𝑑s],\displaystyle\negthinspace\frac{c}{k}\mathbb{E}\Big[\frac{1}{2}\int\_{0}^{T-\varepsilon}\frac{1}{\sqrt{T-s}}\big(|\widehat{\alpha}^{k}\_{s}|+|\widehat{\alpha}\_{s}|\big)ds\Big]\leq\frac{c}{k\sqrt{\varepsilon}}\mathbb{E}\Big[\frac{1}{2}\int\_{0}^{T}\big(|\widehat{\alpha}^{k}\_{s}|+|\widehat{\alpha}\_{s}|\big)\,ds\Big], |  |

where
the last inequality is due to the fact that 1T−s≤1ε\frac{1}{\sqrt{T-s}}\leq\frac{1}{\sqrt{\varepsilon}} for s∈[0,T−ε]s\in[0,T-\varepsilon]. To further bound ([4.2](https://arxiv.org/html/2510.11829v1#S4.Ex12 "4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), we recall that the definitions of J​(⋅)J(\cdot) ([2.5](https://arxiv.org/html/2510.11829v1#S2.E5 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) and Jk​(⋅)J^{k}(\cdot) ([2.10](https://arxiv.org/html/2510.11829v1#S2.E10 "In Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), k∈ℕk\in\mathbb{N}, and define

|  |  |  |
| --- | --- | --- |
|  | V∗=J​(α^)=infα∈𝒜J​(α);Vk,∗=Jk​(α^k)=infα∈𝒜Jk​(α).\displaystyle V^{\*}=J(\widehat{\alpha})=\inf\_{\alpha\in\mathcal{A}}J(\alpha);\qquad V^{k,\*}=J^{k}(\widehat{\alpha}^{k})=\inf\_{\alpha\in\mathcal{A}}J^{k}(\alpha). |  |

We should note that Xα^X^{\widehat{\alpha}} follows the constrained dynamics ([2.6](https://arxiv.org/html/2510.11829v1#S2.E6 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), whereas Xα^kX^{\widehat{\alpha}^{k}} follows the soft-constrained dynamics ([2.9](https://arxiv.org/html/2510.11829v1#S2.E9 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). Clearly, by definition ([2.10](https://arxiv.org/html/2510.11829v1#S2.E10 "In Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) we have

|  |  |  |
| --- | --- | --- |
|  | supk≥1Jk​(α)={𝔼​[∫0T12​|αt|2​d⁡t] if ​ℙXTα=μtar∞otherwise.\displaystyle\sup\_{k\geq 1}J^{k}(\alpha)=\begin{cases}\displaystyle\mathbb{E}\Big[\int\_{0}^{T}\frac{1}{2}|\alpha\_{t}|^{2}\operatorname{{\rm d}}t\Big]&\textrm{ if }\,\,\mathbb{P}\_{X\_{T}^{\alpha}}={\mu\_{\rm tar}}\\ \infty&\textrm{otherwise}.\end{cases} |  |

Thus, since α^\widehat{\alpha} satisfies the constraint dynamics ([2.6](https://arxiv.org/html/2510.11829v1#S2.E6 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | V∗=J​(α^)=infα∈𝒜supk≥1Jk​(α)≥infα∈𝒜Jk​(α)=Jk​(α^k)=Vk,∗,k∈ℕ.\displaystyle V^{\*}=J(\widehat{\alpha})=\inf\_{\alpha\in\mathcal{A}}\sup\_{k\geq 1}J^{k}(\alpha)\geq\inf\_{\alpha\in\mathcal{A}}J^{k}(\alpha)=J^{k}(\widehat{\alpha}^{k})=V^{k,\*},\qquad k\in\mathbb{N}. |  | (4.15) |

Consequently, we have, for each k∈ℕk\in\mathbb{N}, a simple application of Cauchy–Schwarz inequality and the fact ([4.15](https://arxiv.org/html/2510.11829v1#S4.E15 "In 4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[12​∫0T(|α^sk|+|α^s|)​𝑑s]≤T2​(𝔼​[∫0T|α^sk|2​𝑑s])1/2+(𝔼​[∫0T|α^s|2​𝑑s])1/2≤T​V∗.\displaystyle\mathbb{E}\Big[\frac{1}{2}\int\_{0}^{T}\big(|\widehat{\alpha}^{k}\_{s}|+|\widehat{\alpha}\_{s}|\big)ds\Big]\leq\frac{{\sqrt{T}}}{2}\Big(\mathbb{E}\Big[\int\_{0}^{T}|\widehat{\alpha}^{k}\_{s}|^{2}ds\Big]\Big)^{1/2}+\Big(\mathbb{E}\Big[\int\_{0}^{T}|\widehat{\alpha}\_{s}|^{2}ds\Big]\Big)^{1/2}\leq\sqrt{T}\sqrt{V^{\*}}. |  | (4.16) |

Combining ([4.2](https://arxiv.org/html/2510.11829v1#S4.Ex12 "4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) and ([4.16](https://arxiv.org/html/2510.11829v1#S4.E16 "In 4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), we obtain ([4.13](https://arxiv.org/html/2510.11829v1#S4.E13 "In Proposition 4.4. ‣ 4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")).
∎

Besides the convergence of the value functions, another important convergence, that relies crucially on the convergence of the optimal controls, is the convergence of the terminal law ℙXTα^k\mathbb{P}\_{X^{\widehat{\alpha}^{k}}\_{T}} (with respect to the target distribution μtar{\mu\_{\rm tar}}), measured, for instance, in the Wasserstein distance. Again, to avoid the technicalities that the singularity at terminal time TT might cause, we shall focus on the early stopped state XT−εα^kX^{\widehat{\alpha}^{k}}\_{T-\varepsilon}, which is a commonly used criterion in statistical estimation results for generative diffusion models (see, e.g., [[28](https://arxiv.org/html/2510.11829v1#bib.bib28), [33](https://arxiv.org/html/2510.11829v1#bib.bib33), [12](https://arxiv.org/html/2510.11829v1#bib.bib12)]). More precisely, we have the following result.

###### Proposition 4.5.

Let all assumptions in Theorem [4.1](https://arxiv.org/html/2510.11829v1#S4.ThmTheorem1 "Theorem 4.1. ‣ 4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") be in force. Assume further that the optimal policy α^\widehat{\alpha} of the original SBP is Lipschitz in xx: there exists κ>0\kappa>0, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |α^​(t,x)−α^​(t,y)|≤κ​|x−y|,t∈[0,T].\displaystyle|\widehat{\alpha}(t,x)-\widehat{\alpha}(t,y)|\leq\kappa|x-y|,\qquad t\in[0,T]. |  | (4.17) |

Then there exists a constant C>0C>0, depending on the Lipschitz constants LL in Assumption [2.2](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem2 "Assumption 2.2. ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and κ\kappa in ([4.17](https://arxiv.org/html/2510.11829v1#S4.E17 "In Proposition 4.5. ‣ 4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), but independent of k∈ℕk\in\mathbb{N}, such that for any ε>0\varepsilon>0, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | W2​(ℙXT−εα^k,μtar)≤C​ln⁡T−ln⁡εk+C​ε.\displaystyle{W}\_{2}(\mathbb{P}\_{X^{\widehat{\alpha}^{k}}\_{T-\varepsilon}},{\mu\_{\rm tar}})\leq\frac{C\sqrt{\ln T-\ln\varepsilon}}{k}+C\varepsilon. |  | (4.18) |

In particular, if we choose ε=1k\varepsilon=\frac{1}{k}, then it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | W2(ℙXT−εα^k,μtar)≤Ck(ln⁡k+ln⁡T)+1)=𝒪(ln⁡kk).\displaystyle{W}\_{2}(\mathbb{P}\_{X^{\widehat{\alpha}^{k}}\_{T-\varepsilon}},{\mu\_{\rm tar}})\leq\frac{C}{k}\big(\sqrt{\ln k}+\sqrt{\ln T})+1\big)=\mathcal{O}\Big(\frac{\sqrt{\ln k}}{k}\Big). |  | (4.19) |

###### Remark 4.6.

(i) The linear (i.e., ∼1k\sim\frac{1}{k}) "closeness" between the law of the optimal state and μtar{\mu\_{\rm tar}} has appeared several times so far. For example, ([4.3](https://arxiv.org/html/2510.11829v1#S4.E3 "In 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) implies that G​(ℙXTα^k)=G​(ℙXTα^k;μtar)≤ckG(\mathbb{P}\_{X^{\widehat{\alpha}^{k}}\_{T}})=G(\mathbb{P}\_{X^{\widehat{\alpha}^{k}}\_{T}};{\mu\_{\rm tar}})\leq\frac{c}{k}, and by
Remark [3.3](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem3 "Remark 3.3. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(ii), this implies that W1​(ℙXTα^k,μtar)∼1kW\_{1}(\mathbb{P}\_{X^{\widehat{\alpha}^{k}}\_{T}},{\mu\_{\rm tar}})\sim\frac{1}{k}. The result in ([4.19](https://arxiv.org/html/2510.11829v1#S4.E19 "In Proposition 4.5. ‣ 4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) is in the same spirit, by under the stronger W2{W}\_{2}-distance, but compensated by an early stopping.

(ii) The Lipschitz condition ([4.17](https://arxiv.org/html/2510.11829v1#S4.E17 "In Proposition 4.5. ‣ 4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) for the optimal control α^\widehat{\alpha} is not unusual in the diffusion model literature (see, e.g., [[60](https://arxiv.org/html/2510.11829v1#bib.bib60), [11](https://arxiv.org/html/2510.11829v1#bib.bib11), [12](https://arxiv.org/html/2510.11829v1#bib.bib12)]). In fact, this can be argued via regularity of the solution to the PDE ([4.1](https://arxiv.org/html/2510.11829v1#S4.E1 "In 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) combined with the speed of decay of the density ftarf\_{\rm tar}, which can be assumed and analyzed rigorously (see Assumption [5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") below). We therefore consider such an assumption non-stringent.
∎

[Proof of Proposition [4.5](https://arxiv.org/html/2510.11829v1#S4.ThmTheorem5 "Proposition 4.5. ‣ 4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday").]
First note that Xα^X^{\widehat{\alpha}} and Xα^kX^{\widehat{\alpha}^{k}} satisfy the following SDEs, respectively:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Xtα^=[b​(t,Xtα^)+α^t​(Xtα^)]​d​t+d​WtX0α^=x0;d​Xtα^k=[b​(t,Xtα^k)+α^tk​(Xtα^k)]​d​t+d​Wt,X0α^=x0.\displaystyle\begin{cases}dX^{\widehat{\alpha}}\_{t}=[b(t,X^{\widehat{\alpha}}\_{t})+\widehat{\alpha}\_{t}(X^{\widehat{\alpha}}\_{t})]dt+dW\_{t}\qquad\quad&X^{\widehat{\alpha}}\_{0}=x\_{0};\\ dX^{\widehat{\alpha}^{k}}\_{t}=[b(t,X^{\widehat{\alpha}^{k}}\_{t})+\widehat{\alpha}\_{t}^{k}(X^{\widehat{\alpha}^{k}}\_{t})]dt+dW\_{t},&X^{\widehat{\alpha}}\_{0}=x\_{0}.\end{cases} |  | (4.20) |

Let us now denote α^t​(x)=α^​(t,x)\widehat{\alpha}\_{t}(x)=\widehat{\alpha}(t,x), α^tk​(x)=α^k​(t,x)\widehat{\alpha}^{k}\_{t}(x)=\widehat{\alpha}^{k}(t,x), and define

|  |  |  |
| --- | --- | --- |
|  | bα^​(t,x)=b​(t,x)+α^t​(x),Δ​α^tk​(x)=α^tk​(x)−α^t​(x),(t,x)∈[0,T]×ℝd.b^{\widehat{\alpha}}(t,x)=b(t,x)+\widehat{\alpha}\_{t}(x),\quad\Delta\widehat{\alpha}^{k}\_{t}(x)=\widehat{\alpha}^{k}\_{t}(x)-\widehat{\alpha}\_{t}(x),\qquad(t,x)\in[0,T]\times\mathbb{R}^{d}. |  |

Then we see that SDE ([4.20](https://arxiv.org/html/2510.11829v1#S4.E20 "In 4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) can be written as

|  |  |  |
| --- | --- | --- |
|  | {d​Xtα^=bα^​(t,Xtα^)​d​t+d​WtX0α^=x0;d​Xtα^k=[bα^​(t,Xtα^k)+Δ​α^tk​(Xtα^k)]​d​t+d​Wt,X0α^=x0.\displaystyle\begin{cases}dX^{\widehat{\alpha}}\_{t}=b^{\widehat{\alpha}}(t,X^{\widehat{\alpha}}\_{t})dt+dW\_{t}\qquad\quad&X^{\widehat{\alpha}}\_{0}=x\_{0};\\ dX^{\widehat{\alpha}^{k}}\_{t}=[b^{\widehat{\alpha}}(t,X^{\widehat{\alpha}^{k}}\_{t})+\Delta\widehat{\alpha}\_{t}^{k}(X^{\widehat{\alpha}^{k}}\_{t})]dt+dW\_{t},&X^{\widehat{\alpha}}\_{0}=x\_{0}.\end{cases} |  |

That is,

|  |  |  |
| --- | --- | --- |
|  | Xtα^−Xtα^k=∫0t[bα^​(s,Xsα^)−bα^​(s,Xsα^k)+Δ​α^sk​(Xsα^k)]​𝑑s,t∈[0,T]\displaystyle X^{\widehat{\alpha}}\_{t}-X^{\widehat{\alpha}^{k}}\_{t}=\int\_{0}^{t}[b^{\widehat{\alpha}}(s,X^{\widehat{\alpha}}\_{s})-b^{\widehat{\alpha}}(s,X^{\widehat{\alpha}^{k}}\_{s})+\Delta\widehat{\alpha}\_{s}^{k}(X^{\widehat{\alpha}^{k}}\_{s})]ds,\qquad t\in[0,T] |  |

Note that by Assumption [2.2](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem2 "Assumption 2.2. ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and ([4.17](https://arxiv.org/html/2510.11829v1#S4.E17 "In Proposition 4.5. ‣ 4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), bα^b^{\widehat{\alpha}} is uniform Lipschitz in xx (with Lipschitz constant L+κL+\kappa),
and applying the estimate ([4.12](https://arxiv.org/html/2510.11829v1#S4.E12 "In 4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), we deduce easily that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[|Xtα^−Xtα^k|2]≤2T∫0t[(L+κ)2𝔼[|Xsα^−Xsα^k|2]ds+2​c2k2ln[TT−t].\displaystyle\mathbb{E}[|X^{\widehat{\alpha}}\_{t}-X^{\widehat{\alpha}^{k}}\_{t}|^{2}]\leq 2T\int\_{0}^{t}\Big[(L+\kappa)^{2}\mathbb{E}[|X^{\widehat{\alpha}}\_{s}-X^{\widehat{\alpha}^{k}}\_{s}|^{2}]ds+\frac{2c^{2}}{k^{2}}\ln\Big[\frac{T}{T-t}\Big]. |  | (4.21) |

In what follows let us denote C>0C>0 to be a generic constant depending only on LL, κ\kappa, cc, but independent of kk, and we allow it to vary from line to line. Then, by a simple calculation using Gronwall’s inequality, we see that ([4.21](https://arxiv.org/html/2510.11829v1#S4.E21 "In 4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) lead to that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|Xtα^−Xtα^k|2]≤Ck2​(ln⁡T−ln⁡(T−t))​eC​t,t∈[0,T).\displaystyle\mathbb{E}[|X^{\widehat{\alpha}}\_{t}-X^{\widehat{\alpha}^{k}}\_{t}|^{2}]\leq\frac{C}{k^{2}}(\ln T-\ln(T-t))e^{Ct},\qquad t\in[0,T). |  | (4.22) |

Furthermore, for any ε>0\varepsilon>0, using the monotonicity of the log function we deduce from ([4.22](https://arxiv.org/html/2510.11829v1#S4.E22 "In 4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|XT−εα^−XT−εα^k|2]≤Ck2​(ln⁡T−ln⁡ε)\displaystyle\mathbb{E}[|X^{\widehat{\alpha}}\_{T-\varepsilon}-X^{\widehat{\alpha}^{k}}\_{T-\varepsilon}|^{2}]\leq\frac{C}{k^{2}}(\ln T-\ln\varepsilon) |  |

It then follows that

|  |  |  |
| --- | --- | --- |
|  | W2​(ℙXT−εα^,ℙXT−εα^k)≤𝔼​[|XT−εα^−XT−εα^k|2]1/2≤Ck​ln⁡T−ln⁡ε.\displaystyle W\_{2}(\mathbb{P}\_{X^{\widehat{\alpha}}\_{T-\varepsilon}},\mathbb{P}\_{X^{\widehat{\alpha}^{k}}\_{T-\varepsilon}})\leq\mathbb{E}[|X^{\widehat{\alpha}}\_{T-\varepsilon}-X^{\widehat{\alpha}^{k}}\_{T-\varepsilon}|^{2}]^{1/2}\leq\frac{\sqrt{C}}{k}\sqrt{\ln T-\ln\varepsilon}. |  |

Finally, since the function bα^=b+α^b^{\widehat{\alpha}}=b+\widehat{\alpha} is Lipschitz, by standard 𝕃2\mathbb{L}^{2}-continuity result of SDE, we have

|  |  |  |
| --- | --- | --- |
|  | W2​(ℙXT−εα^,ℙXTα^)≤C​ε,\displaystyle{W}\_{2}(\mathbb{P}\_{X^{\widehat{\alpha}}\_{T-\varepsilon}},\mathbb{P}\_{X^{\widehat{\alpha}}\_{T}})\leq C\varepsilon, |  |

and consequently, noting that ℙXTα^=μtar\mathbb{P}\_{X^{\widehat{\alpha}}\_{T}}={\mu\_{\rm tar}}, we obtain

|  |  |  |
| --- | --- | --- |
|  | W2​(ℙXT−εα^,μtar)≤W2​(ℙXT−εα^,ℙXT−εα^k)+W2​(ℙXT−εα^,ℙXTα^)≤C​(ln⁡T−ln⁡ε)k+C​ε,\displaystyle{W}\_{2}(\mathbb{P}\_{X^{\widehat{\alpha}}\_{T-\varepsilon}},{\mu\_{\rm tar}})\leq W\_{2}(\mathbb{P}\_{X^{\widehat{\alpha}}\_{T-\varepsilon}},\mathbb{P}\_{X^{\widehat{\alpha}^{k}}\_{T-\varepsilon}})+{W}\_{2}(\mathbb{P}\_{X^{\widehat{\alpha}}\_{T-\varepsilon}},\mathbb{P}\_{X^{\widehat{\alpha}}\_{T}})\leq\frac{\sqrt{C(\ln T-\ln\varepsilon)}}{k}+C\varepsilon, |  |

proving ([4.18](https://arxiv.org/html/2510.11829v1#S4.E18 "In Proposition 4.5. ‣ 4.2 The Convergence of the Value Function ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), whence the proposition.
∎

## 5 Stability of the Solutions to the SBP

We note that all the results in the previous section are based on an important assumption: μini=δx0{\mu\_{\rm ini}}=\delta\_{x\_{0}}, for some x0∈ℝdx\_{0}\in\mathbb{R}^{d}. In this and the next section, we shall extend the results to more general initial condition μini∈𝒫2​(ℝd){\mu\_{\rm ini}}\in\mathscr{P}\_{2}(\mathbb{R}^{d}), and establish a similar rate of convergence.

We shall begin an important aspect in probability theory, which is the basis for the so-called stability issues of the solutions to the classic Schrödinger bridge problem. For notational convenience, we still denote p​(⋅,⋅;⋅,⋅)p(\cdot,\cdot;\cdot,\cdot) to be the transition density of a standard ℝd\mathbb{R}^{d}-valued diffusion ([3.1](https://arxiv.org/html/2510.11829v1#S3.E1 "In 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). We begin with the following well-known result in diffusion theory (cf. e.g., [[7](https://arxiv.org/html/2510.11829v1#bib.bib7)]).

###### Proposition 5.1 ([[7](https://arxiv.org/html/2510.11829v1#bib.bib7)]).

For any μ0,μT∈𝒫​(ℝd)\mu\_{0},\mu\_{T}\in\mathscr{P}(\mathbb{R}^{d}), there exists a unique pair of σ\sigma-finite measures ν0,νT∈ℳ​(ℝd)\nu\_{0},\nu\_{T}\in\mathscr{M}(\mathbb{R}^{d}) such that the measure π∈𝒫​(ℝd×ℝd)\pi\in\mathscr{P}(\mathbb{R}^{d}\times\mathbb{R}^{d}) defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(E)=∫Ep​(T,y;0,x)​ν0​(d​x)​νT​(d​y),E∈ℬ​(ℝd×ℝd)\displaystyle\pi(E)=\int\_{E}p(T,y;0,x)\nu\_{0}(dx)\nu\_{T}(dy),\qquad E\in\mathscr{B}(\mathbb{R}^{d}\times\mathbb{R}^{d}) |  | (5.1) |

has marginals μ0\mu\_{0} and μT\mu\_{T}. Furthermore, νT\nu\_{T} and μT\mu\_{T} (resp. ν0\nu\_{0} and μ0\mu\_{0}) are mutually absolutely continuous,
denoted by νT≃μT\nu\_{T}\simeq\mu\_{T} (resp. ν0≃μ0\nu\_{0}\simeq\mu\_{0}).
∎

Following Proposition [5.1](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem1 "Proposition 5.1 ([7]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), let us denote a (well-defined) mapping
𝒯:𝒫2​(ℝd)×𝒫2​(ℝd)↦ℳ​(ℝd)×ℳ​(ℝd){\cal T}:\mathscr{P}\_{2}(\mathbb{R}^{d})\times\mathscr{P}\_{2}(\mathbb{R}^{d})\mapsto\mathscr{M}(\mathbb{R}^{d})\times\mathscr{M}(\mathbb{R}^{d}) by 𝒯​(μ0,μT)=(ν0,νT){\cal T}(\mu\_{0},\mu\_{T})=(\nu\_{0},\nu\_{T}). In particular, in what follows we shall often fix μ0=μini∈𝒫2​(ℝd)\mu\_{0}={\mu\_{\rm ini}}\in\mathscr{P}\_{2}(\mathbb{R}^{d}), and focus mainly on νT\nu\_{T}.
Note that in Proposition [5.1](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem1 "Proposition 5.1 ([7]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") the measures (ν0,νT)(\nu\_{0},\nu\_{T}) are only σ\sigma-finite in general, to facilitate our discussion, we shall consider, for a given μ0\mu\_{0}, the following set:

|  |  |  |
| --- | --- | --- |
|  | 𝒟μ0:={μ∈𝒫2​(ℝd):𝒯​(μ0,μ)≪L​e​b​(⋅);𝒯​(μ0,μ)​(ℝd×ℝd)<∞}.\displaystyle\mathscr{D}\_{\mu\_{0}}:=\{\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d}):{\cal T}(\mu\_{0},\mu)\ll Leb(\cdot);\,{\cal T}(\mu\_{0},\mu)(\mathbb{R}^{d}\times\mathbb{R}^{d})<\infty\}. |  |

Here L​e​b​(⋅)Leb(\cdot) denotes the Lebesgue measure on ℝd×ℝd\mathbb{R}^{d}\times\mathbb{R}^{d}. In the case when μ0=μini\mu\_{0}={\mu\_{\rm ini}} is fixed in the discussion, we shall simply denote 𝒟=𝒟μini\mathscr{D}=\mathscr{D}\_{{\mu\_{\rm ini}}} when context is clear.

We note that if μ∈𝒟\mu\in\mathscr{D} and (ν0,νT)=𝒯​(μini,μ)(\nu\_{0},\nu\_{T})={\cal T}({\mu\_{\rm ini}},\mu), then
νT\nu\_{T} must have a density function, which we shall denote by ρμ∈𝕃1​(ℝd)\rho^{\mu}\in\mathbb{L}^{1}(\mathbb{R}^{d}).
Moreover, we define an operator S:𝒫2​(ℝd)→𝒫2​(ℝd)S:\mathscr{P}\_{2}(\mathbb{R}^{d})\to\mathscr{P}\_{2}(\mathbb{R}^{d}) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​[μ]​(d​y)=∫ℝdp​(T,y;0,x)​μ​(d​x)​𝑑y,μ∈𝒫2​(ℝd).\displaystyle S[\mu](dy)=\int\_{\mathbb{R}^{d}}p(T,y;0,x)\mu(dx)dy,\qquad\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d}). |  | (5.2) |

Clearly, if μ∈𝒫​(ℝd)\mu\in\mathscr{P}(\mathbb{R}^{d}), then S​[μ]​(d​y)=fXT0,μ​(y)​d​yS[\mu](dy)=f\_{X^{0,\mu}\_{T}}(y)dy, where X0,μ={Xt0,μ}t∈[0,T]X^{0,\mu}=\{X^{0,\mu}\_{t}\}\_{t\in[0,T]} denotes the solution to ([3.1](https://arxiv.org/html/2510.11829v1#S3.E1 "In 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) with X00,μ∼μX^{0,\mu}\_{0}\sim\mu.
But the operator SS can be naturally extended to any μ∈ℳ​(ℝd)\mu\in\mathscr{M}(\mathbb{R}^{d}), provided the right-hand side of ([5.2](https://arxiv.org/html/2510.11829v1#S5.E2 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) is well-defined.

Let us now recall a well-known analogue of Lemma [3.1](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem1 "Lemma 3.1 ( [18, Theorem 3.1]). ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") in the case of general initial condition μini∈𝒫2​(ℝd){\mu\_{\rm ini}}\in\mathscr{P}\_{2}(\mathbb{R}^{d}).

###### Proposition 5.2 ([[18](https://arxiv.org/html/2510.11829v1#bib.bib18), Theorem 3.2]).

Let μini∈𝒫2​(ℝd){\mu\_{\rm ini}}\in\mathscr{P}\_{2}(\mathbb{R}^{d}), and assume that DKL​(μini∥ν0)<∞D\_{\rm KL}({\mu\_{\rm ini}}\|\nu\_{0})<\infty and DKL​(μtar∥S​[ν0])<∞D\_{\rm KL}({\mu\_{\rm tar}}\|S[\nu\_{0}])<\infty. Then, the optimal control for the (original) SBP ([2.5](https://arxiv.org/html/2510.11829v1#S2.E5 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"))-([2.6](https://arxiv.org/html/2510.11829v1#S2.E6 "In Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) is given by α^t=∇log⁡h​(t,Xtα^)\widehat{\alpha}\_{t}=\nabla\log h(t,X^{\widehat{\alpha}}\_{t}) where, denoting ρμtar​(⋅)\rho^{\mu\_{\rm tar}}(\cdot) to be the density function of νT\nu\_{T},

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(t,x):=∫ℝdp​(T,z;t,x)​ρμtar​(z)​𝑑z.\displaystyle h(t,x):=\int\_{\mathbb{R}^{d}}p(T,z;t,x)\rho^{\mu\_{\rm tar}}(z)dz. |  | (5.3) |

Moreover, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(α^)=∫ℝdlog⁡ρμtar​(y)​μtar​(d​y)−DKL​(μini∥ν0).J(\widehat{\alpha})=\int\_{\mathbb{R}^{d}}\log\rho^{\mu\_{\rm tar}}(y){\mu\_{\rm tar}}(dy)-D\_{\rm KL}({\mu\_{\rm ini}}\|\nu\_{0}). |  | (5.4) |

We note that in the above DKL​(μini∥ν0)=∫log⁡μini​(d​x)ν0​(d​x)​μini​(d​x)D\_{\rm KL}({\mu\_{\rm ini}}\|\nu\_{0})=\int\log\frac{{\mu\_{\rm ini}}(dx)}{\nu\_{0}(dx)}{\mu\_{\rm ini}}(dx) (see footnote 1), and ([5.1](https://arxiv.org/html/2510.11829v1#S5.E1 "In Proposition 5.1 ([7]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) implies that μini​(d​x)ν0​(d​x)=∫p​(T,y;0,x)​ρμtar​(y)​𝑑y\frac{{\mu\_{\rm ini}}(dx)}{\nu\_{0}(dx)}=\int p(T,y;0,x)\rho^{\mu\_{\rm tar}}(y)dy. Therefore ([5.4](https://arxiv.org/html/2510.11829v1#S5.E4 "In Proposition 5.2 ([18, Theorem 3.2]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(α^)\displaystyle J(\widehat{\alpha}) | =∫ℝdlog⁡ρμtar​(y)​μtar​(d​y)−∫ℝdlog⁡(∫ℝdp​(T,y;0,x)​ρμtar​(y)​𝑑y)​μini​(d​x)\displaystyle=\int\_{\mathbb{R}^{d}}\log\rho^{\mu\_{\rm tar}}(y){\mu\_{\rm tar}}(dy)-\int\_{\mathbb{R}^{d}}\log\Big(\int\_{\mathbb{R}^{d}}p(T,y;0,x)\rho^{\mu\_{\rm tar}}(y)dy\Big){\mu\_{\rm ini}}(dx) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[log⁡ρμtar​(XTα^)]−∫ℝdlog⁡h​(0,x)​μini​(d​x)=𝔼​[log⁡ρμtar​(XTα^)]−𝔼​[log⁡h​(0,X0α^)].\displaystyle=\mathbb{E}[\log\rho^{\mu\_{\rm tar}}(X^{\widehat{\alpha}}\_{T})]-\int\_{\mathbb{R}^{d}}\log h(0,x){\mu\_{\rm ini}}(dx)=\mathbb{E}\big[\log\rho^{\mu\_{\rm tar}}(X^{\widehat{\alpha}}\_{T})\big]-\mathbb{E}[\log h(0,X^{\widehat{\alpha}}\_{0})]. |  |

Moreover, for fixed μini∈𝒫2​(ℝd){\mu\_{\rm ini}}\in\mathscr{P}\_{2}(\mathbb{R}^{d}) and μ∈𝒟=𝒟μini\mu\in\mathscr{D}=\mathscr{D}\_{{\mu\_{\rm ini}}},
we define hμ​(t,x)=∫ℝdp​(T,z;t,x)​ρμ​(z)​𝑑zh^{\mu}(t,x)=\int\_{\mathbb{R}^{d}}p(T,z;t,x)\rho^{\mu}(z)dz. Then, we have the following result.

###### Lemma 5.3 ([[29](https://arxiv.org/html/2510.11829v1#bib.bib29), Lemma 3.1]).

Let μ∈𝒟=𝒟μini\mu\in\mathscr{D}=\mathscr{D}\_{{\mu\_{\rm ini}}}. Then, for any {αt}∈𝕃𝔽02​([0,T])\{\alpha\_{t}\}\in\mathbb{L}^{2}\_{\mathbb{F}^{0}}([0,T]), it holds that

|  |  |  |
| --- | --- | --- |
|  | J​(α)≥𝔼​[log⁡ρμ​(XTα)]−𝔼​[log⁡hμ​(0,X0α)].\displaystyle J(\alpha)\geq\mathbb{E}[\log\rho^{\mu}(X^{\alpha}\_{T})]-\mathbb{E}[\log h^{\mu}(0,X^{\alpha}\_{0})]. |  |

The equality holds when αt=αtμ=∇log⁡hμ​(t,Xtαμ)\alpha\_{t}=\alpha^{\mu}\_{t}=\nabla\log h^{\mu}(t,X^{\alpha^{\mu}}\_{t}), t∈[0,T]t\in[0,T] and XTαμ∼μX^{\alpha^{\mu}}\_{T}\sim\mu.
∎

From Proposition [5.2](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem2 "Proposition 5.2 ([18, Theorem 3.2]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and Lemma [5.3](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem3 "Lemma 5.3 ([29, Lemma 3.1]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") we see that the density function ρμ\rho^{\mu} plays an important role in the structure of the solution of SBP. We shall be particularly interested in the continuous dependence of ρμ:=Γ1​(μ)\rho^{\mu}:=\Gamma\_{1}(\mu) on μ∈𝒫2​(ℝd)\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d}), which we shall refer to as the Stability of the
SBP, borrowing the well-known concept of the SBP theory (cf. e.g., [[46](https://arxiv.org/html/2510.11829v1#bib.bib46), [22](https://arxiv.org/html/2510.11829v1#bib.bib22), [10](https://arxiv.org/html/2510.11829v1#bib.bib10)]). In light of ([6.4](https://arxiv.org/html/2510.11829v1#S6.E4 "In 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), we see that if both μini{\mu\_{\rm ini}} and μ\mu have densities, then so does 𝒯​(μini,μ){\cal T}({\mu\_{\rm ini}},\mu).
Furthermore, in light of ([5.3](https://arxiv.org/html/2510.11829v1#S5.E3 "In Proposition 5.2 ([18, Theorem 3.2]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), for any ρ∈𝕃1​(ℝd)\rho\in\mathbb{L}^{1}(\mathbb{R}^{d}), we define hρ​(t,x)=∫ℝdp​(T,z;t,x)​ρ​(z)​𝑑zh^{\rho}(t,x)=\int\_{\mathbb{R}^{d}}p(T,z;t,x)\rho(z)dz. Then clearly we have hμ​(t,x)=hρμ​(t,x)h^{\mu}(t,x)=h^{\rho^{\mu}}(t,x).

To continue our discussion, we shall identify a set ℰ⊂𝒫2​(ℝd)\mathscr{E}\subset\mathscr{P}\_{2}(\mathbb{R}^{d})
on which an argument based on Schauder’s fixed-point theorem can be carried out. We begin by denoting

|  |  |  |
| --- | --- | --- |
|  | 𝒦:={μ∈𝒫2​(ℝd):μ has density fμ∈𝕃1​(ℝd)}.\displaystyle{\cal K}:=\Big\{\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d}):\mbox{$\mu$ has density $f\_{\mu}\in\mathbb{L}^{1}(\mathbb{R}^{d})$}\Big\}. |  |

Furthermore, we shall make use of the following assumption.

###### Assumption 5.4.

There exists a function g∈𝕃2​(ℝd;(0,1])g\in\mathbb{L}^{2}(\mathbb{R}^{d};(0,1]), with ∫ℝd|x|2​g​(x)​𝑑s<∞\int\_{\mathbb{R}^{d}}|x|^{2}g(x)ds<\infty, and a constant K>0K>0, such that ‖fμg2‖∞≤K\Big\|\frac{f\_{\mu}}{g^{2}}\Big\|\_{\infty}\leq K, for all μ∈𝒦\mu\in\mathcal{K}.

We shall consider the following two sets that will play a crucial role in our discussion.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ:={μ∈𝒦: Assumption [5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") holds}⊂𝒫2​(ℝd);𝒮ℰ:={fμ:μ∈ℰ}⊂𝕃1​(ℝd).\displaystyle\mathscr{E}:=\left\{\mu\in{\cal K}:\text{ Assumption \ref{assum:g} holds}\right\}\subset\mathscr{P}\_{2}(\mathbb{R}^{d});\quad{\cal S}\_{\mathscr{E}}:=\left\{f\_{\mu}:\mu\in\mathscr{E}\right\}\subset\mathbb{L}^{1}(\mathbb{R}^{d}). |  | (5.5) |

###### Remark 5.5.

A typical example of the function gg in Assumption [5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") is e−c​|x|e^{-c|x|} or e−c​|x|2e^{-c|x|^{2}}, x∈ℝdx\in\mathbb{R}^{d}, c>0c>0. In such a case we see that part (i) holds for all p>0p>0. Assumption [5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") amounts to saying that we focus only on those density functions that have a similar decay rate to function gg at x∼∞x\sim\infty. In fact, in light of the estimate ([3.2](https://arxiv.org/html/2510.11829v1#S3.E2 "In 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), such a property holds essentially for all transition probabilities of diffusion processes.
∎

The following lemma lists some basic properties of the set ℰ\mathscr{E} (or Assumption [5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")).

###### Lemma 5.6.

Assume that Assumption [5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") is in force. Then it holds that

(i) The set {fμ}μ∈ℰ\{f\_{\mu}\}\_{\mu\in\mathscr{E}} is uniformly bounded in 𝕃2​(ℝd)\mathbb{L}^{2}(\mathbb{R}^{d}).

(ii) The set {fμ}μ∈ℰ\{f\_{\mu}\}\_{\mu\in\mathscr{E}} is uniformly integrable in 𝒫2​(ℝd)\mathscr{P}\_{2}(\mathbb{R}^{d}), in the sense that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limR→∞supμ∈ℰ∫{|x|≥R}|x|2​fμ​(x)​𝑑x=0.\displaystyle\lim\_{R\to\infty}\sup\_{\mu\in\mathscr{E}}\int\_{\{|x|\geq R\}}|x|^{2}f\_{\mu}(x)dx=0. |  | (5.6) |

(iii) If {μn}n≥1⊂ℰ\{\mu\_{n}\}\_{{n\geq 1}}\subset\mathscr{E} such that μn⇒μ\mu\_{n}\Rightarrow\mu, as n→∞n\to\infty, then ‖fμn−fμ‖𝕃1→0\|f\_{\mu\_{n}}-f\_{\mu}\|\_{\mathbb{L}^{1}}\to 0.

###### Proof.

For any μ∈ℰ\mu\in\mathscr{E}, we note that 0<g​(x)≤10<g(x)\leq 1, and by assumption,

|  |  |  |
| --- | --- | --- |
|  | ∫ℝd|fμ​(x)|2​𝑑x≤K2​∫ℝd|g​(x)|4​𝑑s≤K2​‖g‖𝕃22,\int\_{\mathbb{R}^{d}}|f\_{\mu}(x)|^{2}dx\leq K^{2}\int\_{\mathbb{R}^{d}}|g(x)|^{4}ds\leq K^{2}\|g\|^{2}\_{\mathbb{L}^{2}}, |  |

That is {fμ}μ∈ℰ\{f\_{\mu}\}\_{\mu\in\mathscr{E}} is uniformly bounded (by K​‖g‖𝕃2K\|g\|\_{\mathbb{L}^{2}}) in 𝕃2​(ℝd)\mathbb{L}^{2}(\mathbb{R}^{d}), proving (i).

Similarly, for any μ∈ℰ\mu\in\mathscr{E}, by the absolute continuity of the integral we have

|  |  |  |
| --- | --- | --- |
|  | supμ∈ℰ∫{|x|≥R}|x|2​fμ​(x)​𝑑x≤K​∫{|x|≥R}|x|2​g​(x)​𝑑x→0,as R→∞,\displaystyle\sup\_{\mu\in\mathscr{E}}\int\_{\{|x|\geq R\}}|x|^{2}f\_{\mu}(x)dx\leq K\int\_{\{|x|\geq R\}}|x|^{2}g(x)dx\to 0,\quad\mbox{\rm as $R\to\infty$,} |  |

This proves ([5.6](https://arxiv.org/html/2510.11829v1#S5.E6 "In Lemma 5.6. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), whence (ii).

The proof of part (iii) is slightly more involved, which is in the spirit of the so-called Scheffé’s theorem (cf. [[59](https://arxiv.org/html/2510.11829v1#bib.bib59)]).
We note that μn⇒μ\mu\_{n}\Rightarrow\mu amounts to saying that fμn​⇀wfμf\_{\mu\_{n}}\mathop{\mathrel{\mathop{\kern 0.0pt\rightharpoonup}\limits^{w}}}f\_{\mu}, as n→∞n\to\infty, in 𝕃2​(ℝd)\mathbb{L}^{2}(\mathbb{R}^{d}). To show fμn→fμf\_{\mu\_{n}}\to f\_{\mu} in 𝕃1​(ℝd)\mathbb{L}^{1}(\mathbb{R}^{d}), we first consider, for each m>0m>0, the smooth mollifiers φm∈ℂ∞​(ℝd;ℝ+)\varphi^{m}\in\mathbb{C}^{\infty}(\mathbb{R}^{d};\mathbb{R}\_{+}) such that ∫ℝdφm​(z)​𝑑z=1\int\_{\mathbb{R}^{d}}\varphi^{m}(z)dz=1, m≥1m\geq 1, and denote

|  |  |  |
| --- | --- | --- |
|  | fμnm​(x)=[φm∗fμn]​(y)=∫ℝdφm​(x−z)​fμn​(z)​𝑑z;fμm​(x)=[φm∗fμ]​(x),x∈ℝd.f^{m}\_{\mu\_{n}}(x)=[\varphi^{m}\*f\_{\mu\_{n}}](y)=\int\_{\mathbb{R}^{d}}\varphi^{m}(x-z)f\_{\mu\_{n}}(z)dz;\quad f^{m}\_{\mu}(x)=[\varphi^{m}\*f\_{\mu}](x),\quad x\in\mathbb{R}^{d}. |  |

Then it is clear that for each n∈ℕn\in\mathbb{N}, limm→∞fμnm​(x)=fμn​(x)\lim\_{m\to\infty}f^{m}\_{\mu\_{n}}(x)=f\_{\mu\_{n}}(x) and limm→∞fμm​(x)=fμ​(x)\lim\_{m\to\infty}f^{m}\_{\mu}(x)=f\_{\mu}(x), for a.e. x∈ℝdx\in\mathbb{R}^{d}. We should remark that the convergence is uniform in nn. Indeed, by Assumption [5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and Dominated Convergence Theorem we have, as m→∞m\to\infty, for all n≥0n\geq 0,
and x∈ℝdx\in\mathbb{R}^{d},

|  |  |  |
| --- | --- | --- |
|  | |fμnm​(x)−fμn​(x)|≤∫ℝd|φm​(x−z)−δx​(z)|​fμn​(z)​𝑑z≤K​∫ℝd|φm​(x−z)−δx​(z)|​g2​(z)​𝑑z→0.|f^{m}\_{\mu\_{n}}(x)-f\_{\mu\_{n}}(x)|\leq\int\_{\mathbb{R}^{d}}|\varphi^{m}(x-z)-\delta\_{x}(z)|f\_{\mu\_{n}}(z)dz\leq K\int\_{\mathbb{R}^{d}}|\varphi^{m}(x-z)-\delta\_{x}(z)|g^{2}(z)dz\to 0. |  |

Furthermore, since supμ∈ℰ|fμ|≤K​g2∈𝕃1​(ℝd)\sup\_{\mu\in\mathscr{E}}|f\_{\mu}|\leq Kg^{2}\in\mathbb{L}^{1}(\mathbb{R}^{d}), by Dominated Convergence Theorem we have limm→∞fμnm=fμn\lim\_{m\to\infty}f^{m}\_{\mu\_{n}}=f\_{\mu\_{n}} in 𝕃1​(ℝd)\mathbb{L}^{1}(\mathbb{R}^{d}), uniformly for n≥0n\geq 0. That is, for any ε>0\varepsilon>0, there exists
M​(ε)>0M(\varepsilon)>0, such that for all n≥1n\geq 1, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖fμnm−fμn‖𝕃1<ε3;‖fμm−fμ‖𝕃1<ε3,whenever m>M.\displaystyle\|f^{m}\_{\mu\_{n}}-f\_{\mu\_{n}}\|\_{\mathbb{L}^{1}}<\frac{\varepsilon}{3};\quad\|f^{m}\_{\mu}-f\_{\mu}\|\_{\mathbb{L}^{1}}<\frac{\varepsilon}{3},\quad\mbox{whenever $m>M$.} |  | (5.7) |

In the sequel we fix m>M​(ε)m>M(\varepsilon), and take a closer look at the sequence {fμnm}n≥1\{f^{m}\_{\mu\_{n}}\}\_{n\geq 1}. Clearly, each fμnmf^{m}\_{\mu\_{n}} is still a density function, and it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supn|fμnm​(y)|≤supn(φm∗|fμn|)​(y)≤K.\displaystyle\sup\_{n}|f^{m}\_{\mu\_{n}}(y)|\leq\sup\_{n}(\varphi^{m}\*|f\_{\mu\_{n}}|)(y)\leq K. |  | (5.8) |

Moreover, since φm\varphi^{m} is continuous, thus for any x,y∈ℝdx,y\in\mathbb{R}^{d},
applying the Dominated Convergence Theorem we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |fμnm​(x+y)−fμnm​(x)|\displaystyle|f^{m}\_{\mu\_{n}}(x+y)-f^{m}\_{\mu\_{n}}(x)| | ≤\displaystyle\leq | ∫ℝd|φm​(x+y−z)−φm​(x−z)|​|fμn​(z)|​𝑑z\displaystyle\int\_{\mathbb{R}^{d}}|\varphi^{m}(x+y-z)-\varphi^{m}(x-z)||f\_{\mu\_{n}}(z)|dz |  |
|  |  | ≤\displaystyle\leq | K​∫ℝd|φm​(z′−y)−φm​(z′)|​𝑑z′→0,as y→0.\displaystyle K\int\_{\mathbb{R}^{d}}|\varphi^{m}(z^{\prime}-y)-\varphi^{m}(z^{\prime})|dz^{\prime}\to 0,\quad\mbox{as $y\to 0$.} |  |

Clearly, the convergence above is uniform in nn. That is, the sequence {fμnm}{n≥1}\{f^{m}\_{\mu\_{n}}\}\_{\{n\geq 1\}} is so-called asymptotically equi-continuous in the sense of Sweeting [[59](https://arxiv.org/html/2510.11829v1#bib.bib59)]. This, together with ([5.8](https://arxiv.org/html/2510.11829v1#S5.E8 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), implies that limn→∞fμnm=fμm\displaystyle\lim\_{n\to\infty}f^{m}\_{\mu\_{n}}=f^{m}\_{\mu}, uniformly on compacts in ℝd\mathbb{R}^{d} (cf. [[59](https://arxiv.org/html/2510.11829v1#bib.bib59), Theorem 1]). Applying the Dominated Convergence Theorem again we have limn→∞‖fμnm−fμm‖𝕃1=0\lim\_{n\to\infty}\|f^{m}\_{\mu\_{n}}-f^{m}\_{\mu}\|\_{\mathbb{L}^{1}}=0. That is, for the given ε>0\varepsilon>0 in ([5.7](https://arxiv.org/html/2510.11829v1#S5.E7 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), there exists N>0N>0 such that
‖fμnm−fμm‖𝕃1<ε3\|f^{m}\_{\mu\_{n}}-f^{m}\_{\mu}\|\_{\mathbb{L}^{1}}<\frac{\varepsilon}{3}, whenever n>Nn>N. This, together with ([5.7](https://arxiv.org/html/2510.11829v1#S5.E7 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), yields

|  |  |  |
| --- | --- | --- |
|  | ‖fμn−fμ‖𝕃1≤‖fμn−fμnm‖𝕃1+‖fμnm−fμm‖𝕃1+‖fμm−fμ‖𝕃1<ε3+ε3+ε3=ε,n>N,\|f\_{\mu\_{n}}-f\_{\mu}\|\_{\mathbb{L}^{1}}\leq\|f\_{\mu\_{n}}-f^{m}\_{\mu\_{n}}\|\_{\mathbb{L}^{1}}+\|f^{m}\_{\mu\_{n}}-f^{m}\_{\mu}\|\_{\mathbb{L}^{1}}+\|f^{m}\_{\mu}-f\_{\mu}\|\_{\mathbb{L}^{1}}<\frac{\varepsilon}{3}+\frac{\varepsilon}{3}+\frac{\varepsilon}{3}=\varepsilon,\quad n>N, |  |

proving (iii), whence the Lemma.
∎

We are now ready to study our main stability result. More precisely, we shall argue that the mapping Γ1:𝒫2​(ℝd)↦𝕃1​(ℝd)\Gamma\_{1}:\mathscr{P}\_{2}(\mathbb{R}^{d})\mapsto\mathbb{L}^{1}(\mathbb{R}^{d}) is continuous. That is, that μn\mu\_{n} weakly converges to μtar{\mu\_{\rm tar}} in Prohorov metric would imply that ρμn\rho^{\mu\_{n}} converges to ρμtar\rho^{{\mu\_{\rm tar}}} in 𝕃1​(ℝd)\mathbb{L}^{1}(\mathbb{R}^{d}). Such a result, to the best of our knowledge, is novel in the literature.

To simplify our discussion, in what follows, we assume T=1T=1, and denote the measure μ\mu in ([5.1](https://arxiv.org/html/2510.11829v1#S5.E1 "In Proposition 5.1 ([7]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) by π\pi for notational clarity. Recall that π\pi has marginals μini{\mu\_{\rm ini}} and μ\mu, and in what follows, we shall assume that μini{\mu\_{\rm ini}} is fixed and μ∈ℰ\mu\in\mathscr{E}. Let us now consider the following entropic optimal transport problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(μ):=infπ∈Π​(μini,μ)∫ℝd×ℝdc​(x,y)​π​(d​x​d​y)+DKL​(π∥μini⊗μ),I(\mu):=\inf\_{\pi\in\Pi({\mu\_{\rm ini}},\mu)}\int\_{\mathbb{R}^{d}\times\mathbb{R}^{d}}{\textbf{c}}(x,y)\pi(dxdy)+D\_{\rm KL}(\pi\|{\mu\_{\rm ini}}\otimes\mu), |  | (5.9) |

where Π​(μini,μ)\Pi({\mu\_{\rm ini}},\mu) is the set of all coupling probability measures π\pi on ℝd×ℝd\mathbb{R}^{d}\times\mathbb{R}^{d} with marginals μini{\mu\_{\rm ini}} and μ\mu; and c​(⋅,⋅){\textbf{c}}(\cdot,\cdot) is a continuous cost function. It is well-known (see, e.g., [[22](https://arxiv.org/html/2510.11829v1#bib.bib22), [16](https://arxiv.org/html/2510.11829v1#bib.bib16), [31](https://arxiv.org/html/2510.11829v1#bib.bib31), [46](https://arxiv.org/html/2510.11829v1#bib.bib46)]) that the minimization ([5.9](https://arxiv.org/html/2510.11829v1#S5.E9 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) admits a unique solution π^\widehat{\pi}, whose density takes the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^​(d​x​d​y)=exp⁡(−c​(x,y)+ϕμ​(x)+ψμ​(y))​μini​(d​x)​μ​(d​y),\widehat{\pi}(dxdy)=\exp\big(-{\textbf{c}}(x,y)+\phi^{\mu}(x)+\psi^{\mu}(y)\big){\mu\_{\rm ini}}(dx)\mu(dy), |  | (5.10) |

where ϕμ,ψμ\phi^{\mu},\psi^{\mu}: ℝd→ℝ\mathbb{R}^{d}\to\mathbb{R} are two measurable functions, often referred to as the Schrödinger potentials. It is clear that the pair (ϕμ,ψμ)(\phi^{\mu},\psi^{\mu}) is unique up to an additive constant. That is, if (ϕμ,ψμ)(\phi^{\mu},\psi^{\mu}) is a pair of Schrödinger potentials, then so is (ϕμ+c,ψμ−c)(\phi^{\mu}+c,\psi^{\mu}-c). Furthermore, since both μini{\mu\_{\rm ini}} and μ\mu are probability measures, we can easily choose a constant cc so that
the following symmetric normalization holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ϕμ​(x)​μini​(d​x)=∫ψμ​(y)​μ​(d​y).\displaystyle\int\phi^{\mu}(x){\mu\_{\rm ini}}(dx)=\int\psi^{\mu}(y)\mu(dy). |  | (5.11) |

(Otherwise we take c=12​[−∫ϕμ​(x)​μini​(d​x)+∫ψμ​(y)​μ​(d​y)]c=\frac{1}{2}\big[-\int\phi^{\mu}(x){\mu\_{\rm ini}}(dx)+\int\psi^{\mu}(y)\mu(dy)\big].) Note that under the symmetric normalization, the Schrödinger potentials is unique. The following stability result for the mappings μ↦(ϕμ,ψμ)\mu\mapsto(\phi^{\mu},\psi^{\mu}) is crucial for our discussion.

###### Lemma 5.7 ([[10](https://arxiv.org/html/2510.11829v1#bib.bib10), Theorem 1.1]).

Assume that the cost function c​(⋅,⋅)∈ℂk+1​(ℝd×ℝd){\textbf{c}}(\cdot,\cdot)\in\mathbb{C}^{k+1}(\mathbb{R}^{d}\times\mathbb{R}^{d}) for some k∈ℕk\in\mathbb{N}. Then there exists C>0C>0 depending only on ‖c‖ℂk+1\|{\textbf{c}}\|\_{\mathbb{C}^{k+1}}, such that for all μ1\mu\_{1}, μ2∈𝒫2​(ℝd)\mu\_{2}\in\mathscr{P}\_{2}(\mathbb{R}^{d}), it holds that

|  |  |  |
| --- | --- | --- |
|  | ‖(ϕμ1−ϕμ2,ψμ1−ψμ2)‖∗≤C​W2​(μ1,μ2),\|(\phi^{\mu\_{1}}-\phi^{\mu\_{2}},\psi^{\mu\_{1}}-\psi^{\mu\_{2}})\|\_{\*}\leq CW\_{2}(\mu\_{1},\ \mu\_{2}), |  |

where ‖(ϕ,ψ)‖∗:=infc∈ℝ{‖ϕ−c‖ℂk​(ℝd)+‖ψ+c‖ℂk​(ℝd)}\|(\phi,\psi)\|\_{\*}:=\inf\_{c\in\mathbb{R}}\left\{\|\phi-c\|\_{\mathbb{C}^{k}(\mathbb{R}^{d})}+\|\psi+c\|\_{\mathbb{C}^{k}(\mathbb{R}^{d})}\right\}.
∎

We now proceed to prove the main result of this section. To begin with, let us consider the entropic optimal transport problem ([5.9](https://arxiv.org/html/2510.11829v1#S5.E9 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) with c​(x,y):=−log⁡p​(1,y;0,x){\textbf{c}}(x,y):=-\log p(1,y;0,x), x,y∈ℝdx,y\in\mathbb{R}^{d}, where p​(s,y;t,x)p(s,y;t,x), 0≤t<s≤10\leq t<s\leq 1 and x,y∈ℝdx,y\in\mathbb{R}^{d}, is the transition density of the diffusion ([3.1](https://arxiv.org/html/2510.11829v1#S3.E1 "In 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). By ([5.10](https://arxiv.org/html/2510.11829v1#S5.E10 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), for fixed μini,μ∈𝒫2​(ℝd){\mu\_{\rm ini}},\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d}), the unique solution for this entropic optimal transport problem is given by (see also [[46](https://arxiv.org/html/2510.11829v1#bib.bib46)])

|  |  |  |
| --- | --- | --- |
|  | π^​(d​x​d​y)=p​(1,y;0,x)​eϕμ​(x)+ψμ​(y)​f0​(x)​fμ​(y)​d​x​d​y,\displaystyle\widehat{\pi}(dxdy)=p(1,y;0,x)e^{\phi^{\mu}(x)+\psi^{\mu}(y)}f\_{0}(x)f\_{\mu}(y)dxdy, |  |

where ϕμ\phi^{\mu} and ψμ\psi^{\mu} are the Schrödinger potentials, and we shall enforce the symmetric normalization so that
they satisfy ([5.11](https://arxiv.org/html/2510.11829v1#S5.E11 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). Since π^\widehat{\pi} has the marginals μini{\mu\_{\rm ini}} and μ\mu, by the uniqueness of (ν0,ν)=𝒯​(μini,μ)(\nu\_{0},\nu)={\cal T}({\mu\_{\rm ini}},\mu), whence (ρ0,ρμ)(\rho\_{0},\rho^{\mu}), in Proposition [5.1](https://arxiv.org/html/2510.11829v1#S5.E1 "In Proposition 5.1 ([7]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), we can conclude that

|  |  |  |
| --- | --- | --- |
|  | p​(1,y;0,x)​ρ0​(x)​ρμ​(y)=p​(1,y;0,x)​eϕμ​(x)+ψμ​(y)​f0​(x)​fμ​(y),x,y∈ℝd.\displaystyle p(1,y;0,x)\rho\_{0}(x)\rho^{\mu}(y)=p(1,y;0,x)e^{\phi^{\mu}(x)+\psi^{\mu}(y)}f\_{0}(x)f\_{\mu}(y),\qquad x,y\in\mathbb{R}^{d}. |  |

An easy argument of separation of variables then yields that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρμ​(y)=eψμ​(y)​fμ​(y);ρ0​(x)=eϕμ​(x)​f0​(x),x,y∈ℝd.\displaystyle\rho^{\mu}(y)=e^{\psi^{\mu}(y)}f\_{\mu}(y);\quad\rho\_{0}(x)=e^{\phi^{\mu}(x)}f\_{0}(x),\qquad x,y\in\mathbb{R}^{d}. |  | (5.12) |

Now note that the transition density p​(⋅,⋅;⋅,⋅)p(\cdot,\cdot\,;\cdot,\cdot) is a classical solution to the Kolmogorov PDE. Thanks to Assumption [2.2](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem2 "Assumption 2.2. ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), we can assume without loss of generality that c​(⋅,⋅)=−log⁡p​(1,⋅;0,⋅)∈ℂ2​(ℝd×ℝd){\textbf{c}}(\cdot,\cdot)=-\log p(1,\cdot\,;0,\cdot)\in\mathbb{C}^{2}(\mathbb{R}^{d}\times\mathbb{R}^{d}). Thus
according to Lemma [5.7](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem7 "Lemma 5.7 ([10, Theorem 1.1]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and noting the definition of ∥⋅∥∗\|\cdot\|\_{\*}, we see that, modulo some constant normalization, we have that the
Schrödinger potential (ϕμn,ψμn)(\phi^{\mu\_{n}},\psi^{\mu\_{n}}) itself satisfies the estimate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ϕμn−ϕμ‖𝕃∞+‖ψμn−ψμ‖𝕃∞≤C​W2​(μn,μ).\|{\phi}^{\mu\_{n}}-\phi^{\mu}\|\_{\mathbb{L}^{\infty}}+\|{\psi}^{\mu\_{n}}-\psi^{\mu}\|\_{\mathbb{L}^{\infty}}\leq CW\_{2}(\mu\_{n},\mu). |  | (5.13) |

Here in the above the constant C>0C>0 depending only on ‖c‖ℂ2\|{\textbf{c}}\|\_{\mathbb{C}^{2}}, but independent of nn.

Furthermore, we note that c∈ℂ2{\textbf{c}}\in\mathbb{C}^{2} also lead to the following a priori estimate of the Schrödinger potential (see, e.g., [[46](https://arxiv.org/html/2510.11829v1#bib.bib46), Lemma 2.1]):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψμ(y)≤∫ℝdc(x,y)μini(dx)=:ξ(y),y∈ℝd.\displaystyle\psi^{\mu}(y)\leq\int\_{\mathbb{R}^{d}}{\textbf{c}}(x,y){\mu\_{\rm ini}}(dx)=:\xi(y),\quad y\in\mathbb{R}^{d}. |  | (5.14) |

Recall the fundamental estimate ([3.2](https://arxiv.org/html/2510.11829v1#S3.E2 "In 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) and the definition of c​(⋅,⋅){\textbf{c}}(\cdot,\cdot), it is readily seen that ξ​(y)∼λ​|y|2\xi(y)\sim\lambda|y|^{2}, as y→∞y\to\infty, for some constant λ>0\lambda>0 depending only on the coefficient b​(⋅,⋅)b(\cdot,\cdot) in SDE([3.1](https://arxiv.org/html/2510.11829v1#S3.E1 "In 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). In light of Remark [5.5](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem5 "Remark 5.5. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), we shall now assume, without loss of generality, that in Assumption [5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") the control function gg satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | η​(⋅):=eξ​(⋅)​g2​(⋅)∈𝕃1​(ℝd).\displaystyle\eta(\cdot):=e^{\xi(\cdot)}g^{2}(\cdot)\in\mathbb{L}^{1}(\mathbb{R}^{d}). |  | (5.15) |

Now for any fμ∈𝒮ℰf\_{\mu}\in{\cal S}\_{\mathscr{E}}, by Assumption [5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and ([5.14](https://arxiv.org/html/2510.11829v1#S5.E14 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) we have

|  |  |  |
| --- | --- | --- |
|  | 0≤ρμ​(y)=eψμ​(y)​fμ​(y)≤eξ​(y)​fμ​(y)≤eξ​(y)​K​g2​(y)≤K​η​(y),y∈ℝd.0\leq\rho^{\mu}(y)=e^{\psi^{\mu}(y)}\ f\_{\mu}(y)\leq e^{\xi(y)}f\_{\mu}(y)\leq e^{\xi(y)}Kg^{2}(y)\leq K\eta(y),\quad y\in\mathbb{R}^{d}. |  |

Consequently, we conclude that ρμ∈𝕃1​(ℝd)\rho^{\mu}\in\mathbb{L}^{1}(\mathbb{R}^{d}) for any μ∈ℰ\mu\in\mathscr{E}, thanks to ([5.15](https://arxiv.org/html/2510.11829v1#S5.E15 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")).

Bearing the above discussion in mind, we are now ready to present the main result of this section.

###### Proposition 5.8.

Assume that Assumptions [2.2](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem2 "Assumption 2.2. ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and [5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") are in force. Assume further that {μn}n≥1⊂ℰ\{\mu\_{n}\}\_{n\geq 1}\subset\mathscr{E} and μn⟹μ\mu\_{n}\Longrightarrow\mu in Prohorov metric. Then ‖ρμn−ρμ‖𝕃1=‖Γ1​(μn)−Γ1​(μ)‖𝕃1→0\|\rho^{\mu\_{n}}-\rho^{\mu}\|\_{\mathbb{L}^{1}}=\|\Gamma\_{1}(\mu\_{n})-\Gamma\_{1}(\mu)\|\_{\mathbb{L}^{1}}\to 0, as n→∞n\to\infty.

###### Proof.

Assume {μn}n≥1⊂ℰ\{\mu\_{n}\}\_{n\geq 1}\subset\mathscr{E}, and μn⟹μ\mu\_{n}\Longrightarrow\mu, in Prohorov metric. By Lemma [5.6](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem6 "Lemma 5.6. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(ii), {μn}\{\mu\_{n}\} is uniformly integrable in 𝕃2\mathbb{L}^{2}, thanks to Assumption [5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), and thus by the relationship between Wasserstein distance and Prohorov metric (see, [[65](https://arxiv.org/html/2510.11829v1#bib.bib65), Theorem 7.12]), we have W2​(μn,μ)→0W\_{2}(\mu\_{n},\mu)\to 0, as n→∞n\to\infty. Thus, if follows from ([5.13](https://arxiv.org/html/2510.11829v1#S5.E13 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) that ‖ψμn−ψμ‖∞→0\|\psi^{\mu\_{n}}-\psi^{\mu}\|\_{\infty}\to 0, as n→∞n\to\infty.

Next, for each μn∈ℰ\mu\_{n}\in\mathscr{E}, n≥1n\geq 1, and μ\mu, we apply ([5.12](https://arxiv.org/html/2510.11829v1#S5.E12 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) and write

|  |  |  |
| --- | --- | --- |
|  | ρμn​(y)=eψμn​(y)​fμn​(y),ρμ​(y)=eψμ​(y)​fμtar​(y),x,y∈ℝd.\displaystyle\rho^{\mu\_{n}}(y)=e^{\psi^{\mu\_{n}}(y)}f\_{\mu\_{n}}(y),\quad\rho^{\mu}(y)=e^{\psi^{\mu}(y)}f\_{{\mu\_{\rm tar}}}(y),\qquad x,y\in\mathbb{R}^{d}. |  |

Therefore, for y∈ℝdy\in\mathbb{R}^{d}, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |ρμ​(y)−ρμn​(y)|\displaystyle|\rho^{\mu}(y)-\rho^{\mu\_{n}}(y)| | =\displaystyle= | |eψμ​(y)​fμ​(y)−eψμn​(y)​fμn​(y)|\displaystyle\big|e^{\psi^{\mu}(y)}f\_{\mu}(y)-e^{\psi^{\mu\_{n}}(y)}f\_{\mu\_{n}}(y)\big| |  |
|  |  | ≤\displaystyle\leq | |eψμ​(y)−eψμn​(y)|fμn(y)+eψμ​(y)|fμn(y)−fμ(y)|=:In1(y)+In2(y),\displaystyle\big|e^{\psi^{\mu}(y)}-e^{\psi^{\mu\_{n}}(y)}\big|f\_{\mu\_{n}}(y)+e^{\psi^{\mu}(y)}\big|f\_{\mu\_{n}}(y)-f\_{\mu}(y)\big|=:I^{1}\_{n}(y)+I\_{n}^{2}(y), |  |

where IniI^{i}\_{n}, i=1,2i=1,2 are defined in an obvious way. It then suffices to show that both In1I^{1}\_{n} and In2→0I^{2}\_{n}\to 0 in 𝕃1\mathbb{L}^{1}, as n→∞n\to\infty.

To this end, we first recall that ‖ψμn−ψμ‖∞→0\|\psi^{\mu\_{n}}-\psi^{\mu}\|\_{\infty}\to 0, as n→∞n\to\infty. Hence there exists N>0N>0, such that ψμn​(y)≤ψμ​(y)+1\psi^{\mu\_{n}}(y)\leq\psi^{\mu}(y)+1, for all y∈ℝdy\in\mathbb{R}^{d}, whenever n≥Nn\geq N.
Thus, for n≥Nn\geq N, we have

|  |  |  |
| --- | --- | --- |
|  | 0≤In1​(y)≤(|eψμ​(y)|+|eψμn​(y)|)​fμn​(y)≤2​eψμ​(y)+1​fμn​(y)≤2​e⋅eξ​(y)​g2​(y)=2​e​η​(y).0\leq I\_{n}^{1}(y)\leq\big(\big|e^{\psi^{\mu}(y)}\big|+\big|e^{\psi^{\mu\_{n}}(y)}\big|\big)f\_{\mu\_{n}}(y)\leq 2e^{\psi^{\mu}(y)+1}f\_{\mu\_{n}}(y)\leq 2e\cdot e^{\xi(y)}g^{2}(y)=2e\eta(y). |  |

Here in the above, the last inequality holds due to Assumption [5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and ([5.15](https://arxiv.org/html/2510.11829v1#S5.E15 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). Since η∈𝕃1\eta\in\mathbb{L}^{1} by ([5.15](https://arxiv.org/html/2510.11829v1#S5.E15 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), the Dominated Convergence Theorem implies that In1​(⋅)I\_{n}^{1}(\cdot) converges to 0 in 𝕃1​(ℝ2)\mathbb{L}^{1}(\mathbb{R}^{2}) as n→∞n\to\infty, because ψμn{\psi^{\mu\_{n}}} converges uniformly to ψμ\psi^{\mu} on ℝd\mathbb{R}^{d}.

Finally, since In2​(y)≤2​η​(y)I\_{n}^{2}(y)\leq 2\eta(y), and fμn→fμf\_{\mu\_{n}}\to f\_{\mu} in 𝕃1​(ℝd)\mathbb{L}^{1}(\mathbb{R}^{d}), thanks to Lemma [5.6](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem6 "Lemma 5.6. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(iii), we can apply Dominated Convergence again to get In2​(⋅)I\_{n}^{2}(\cdot) converges to 0 in 𝕃1​(ℝ2)\mathbb{L}^{1}(\mathbb{R}^{2}), as n→∞n\to\infty, proving the proposition.
∎

## 6 Existence of optimal control and convergence for general μini{\mu\_{\rm ini}}

In this section, we shall extend the results of §3 and show that the Problem [2.4](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem4 "Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") has solution for each k∈ℕk\in\mathbb{N} when μini{\mu\_{\rm ini}} is an arbitrary distribution in 𝒫2​(ℝd)\mathscr{P}\_{2}(\mathbb{R}^{d}). To be more precise, for fixed k∈ℕk\in\mathbb{N},
let Jk​(α)J^{k}(\alpha) be the cost functional in Problem [2.4](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem4 "Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"). Applying Lemma [5.3](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem3 "Lemma 5.3 ([29, Lemma 3.1]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), for any μ∈𝒟\mu\in\mathscr{D}, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Jk​(α)=𝔼​[12​∫0T|αs|2​𝑑s+k​G​(ℙXTα;μtar)]≥k​G​(ℙXTα;μtar)+𝔼​[log⁡ρμ​(XTα)]−𝔼​[log⁡hμ​(0,X0α)]\displaystyle\begin{split}J^{k}(\alpha)&=\mathbb{E}\Big[\frac{1}{2}\int\_{0}^{T}|\alpha\_{s}|^{2}ds+kG(\mathbb{P}\_{X^{\alpha}\_{T}};{\mu\_{\rm tar}})\Big]\\ &\geq kG(\mathbb{P}\_{X^{\alpha}\_{T}};{\mu\_{\rm tar}})+\mathbb{E}[\log\rho^{\mu}(X^{\alpha}\_{T})]-\mathbb{E}[\log h^{\mu}(0,X^{\alpha}\_{0})]\end{split} | |  | (6.1) |

and the equality holds when αt=αtμ=∇log⁡hμ​(t,Xtαμ)\alpha\_{t}=\alpha^{\mu}\_{t}=\nabla\log h^{\mu}(t,X^{\alpha^{\mu}}\_{t}) and XTαμ∼μX^{\alpha^{\mu}}\_{T}\sim\mu. Our main goal of this
section is to determine the density ρ^​(⋅)\widehat{\rho}(\cdot), such that α^t=∇log⁡hα^​(t,Xtα^)\widehat{\alpha}\_{t}=\nabla\log h^{\widehat{\alpha}}(t,X^{\widehat{\alpha}}\_{t}) is the optimal control to Problem [2.4](https://arxiv.org/html/2510.11829v1#S2.ThmTheorem4 "Problem 2.4 (Soft-constrained Schrödinger Bridge Problem (SCSBP)). ‣ Schrödinger Bridge and Related Control Problem. ‣ 2 Preliminary ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), where hα^​(t,x)=𝔼t,x​[ρ^​(XT)]:=𝔼​[ρ^​(XT)|Xt=x]h^{\widehat{\alpha}}(t,x)=\mathbb{E}\_{t,x}[\widehat{\rho}(X\_{T})]:=\mathbb{E}[\widehat{\rho}(X\_{T})|X\_{t}=x].

Before we proceed, let us first introduce some notations. First, for any μ∈𝒫2​(ℝd)\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d}), we denote fμf\_{\mu} to be its density function, whenever exists. In particular, we define f0=fμinif\_{0}=f\_{{\mu\_{\rm ini}}}.
To be consistent with the previous discussions, we recall the mapping (ν0,νT)=𝒯​(μini,μ)(\nu\_{0},\nu\_{T})={\cal T}({\mu\_{\rm ini}},\mu) for μini,μ∈𝒫2​(ℝd){\mu\_{\rm ini}},\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d}), and for fixed μini{\mu\_{\rm ini}}, we denote fν0=ρ0f\_{\nu\_{0}}=\rho\_{0} and fνT=ρμ=Γ1​(μ)f\_{\nu\_{T}}=\rho^{\mu}=\Gamma\_{1}(\mu). Furthermore, from ([5.1](https://arxiv.org/html/2510.11829v1#S5.E1 "In Proposition 5.1 ([7]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) we see that, for any μini,μ∈𝒫2​(ℝd){\mu\_{\rm ini}},\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d})

|  |  |  |
| --- | --- | --- |
|  | μini​(d​x)ν0​(d​x)=f0​(x)ρ0​(x)=∫ℝdP​(T,y;0,x)​ρμ​(y)​𝑑y,μ​(d​y)νT​(d​y)=fμ​(y)ρμ​(y)=∫ℝdp​(T,y;0,x)​ρ0​(x)​𝑑x.\displaystyle\frac{{\mu\_{\rm ini}}(dx)}{\nu\_{0}(dx)}=\frac{f\_{0}(x)}{\rho\_{0}(x)}=\int\_{\mathbb{R}^{d}}P(T,y;0,x)\rho^{\mu}(y)dy,\quad\frac{\mu(dy)}{\nu\_{T}(dy)}=\frac{f\_{\mu}(y)}{\rho^{\mu}(y)}=\int\_{\mathbb{R}^{d}}p(T,y;0,x)\rho\_{0}(x)dx. |  |

In other words, we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | {ρ0​(x)=f0​(x)∫ℝdP​(T,y;0,x)​ρμ​(y)​𝑑y=f0​(x)hμ​(0,x),ρμ​(y)=fμ​(y)∫ℝdp​(T,y;0,x)​ρ0​(x)​𝑑x=fμ​(y)∫ℝdp​(T,y;0,x)​f0​(x)hμ​(0,x)​𝑑x.\displaystyle\left\{\begin{array}[]{lll}\displaystyle\rho\_{0}(x)=\frac{f\_{0}(x)}{\int\_{\mathbb{R}^{d}}P(T,y;0,x)\rho^{\mu}(y)dy}=\frac{f\_{0}(x)}{h^{\mu}(0,x)}\vskip 6.0pt plus 2.0pt minus 2.0pt,\\ \displaystyle\rho^{\mu}(y)=\frac{f\_{\mu}(y)}{\int\_{\mathbb{R}^{d}}p(T,y;0,x)\rho\_{0}(x)dx}=\frac{f\_{\mu}(y)}{\int\_{\mathbb{R}^{d}}p(T,y;0,x)\frac{f\_{0}(x)}{h^{\mu}(0,x)}dx}.\end{array}\right. |  | (6.4) |

We now give the heuristic idea of the construction of "solution mapping" Γ\Gamma. Let μini{\mu\_{\rm ini}} be given. For any μ∈𝒫2​(ℝd)\mu\in\mathscr{P}\_{2}(\mathbb{R}^{d}),
first apply Lemma [5.3](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem3 "Lemma 5.3 ([29, Lemma 3.1]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") to get the feedback control
αtμ=∇log⁡hμ​(t,Xtαμ)\alpha^{\mu}\_{t}=\nabla\log h^{\mu}(t,X^{\alpha^{\mu}}\_{t}) so that ℙXTαμ=μ\mathbb{P}\_{X^{\alpha^{\mu}}\_{T}}=\mu and

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(αμ)=𝔼​[log⁡ρμ​(XTαμ)]−𝔼​[log⁡hμ​(0,X0αμ)].\displaystyle J(\alpha^{\mu})=\mathbb{E}[\log\rho^{\mu}(X^{\alpha^{\mu}}\_{T})]-\mathbb{E}[\log h^{\mu}(0,X^{\alpha^{\mu}}\_{0})]. |  | (6.5) |

In what follows we fix k∈ℕk\in\mathbb{N}. To find the μ^k\widehat{\mu}^{k} such that Jk​(αμ^k)=infJk​(α)J^{k}(\alpha^{\widehat{\mu}^{k}})=\inf J^{k}(\alpha), we consider a mapping:
Γ2:𝕃1​(ℝd)→𝒫2​(ℝd)\Gamma\_{2}:\mathbb{L}^{1}(\mathbb{R}^{d})\to\mathscr{P}\_{2}(\mathbb{R}^{d}) by Γ2​(ρμ)=μ′\Gamma\_{2}(\rho^{\mu})=\mu^{\prime} where

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ′=arg​minμ¯∈𝒫2​(ℝd)⁡{k​G​(μ¯)+∫ℝdlog⁡ρμ​(y)​μ¯​(d​y)}.\mu^{\prime}=\operatorname\*{arg\,min}\_{\bar{\mu}\in\mathscr{P}\_{2}(\mathbb{R}^{d})}\Big\{kG(\bar{\mu})+\int\_{\mathbb{R}^{d}}\log\rho^{\mu}(y)\bar{\mu}(dy)\Big\}. |  | (6.6) |

Finally, we define Γ=Γ2∘Γ1:𝒫2​(ℝd)↦𝒫2​(ℝd)\Gamma=\Gamma\_{2}\circ\Gamma\_{1}:\mathscr{P}\_{2}(\mathbb{R}^{d})\mapsto\mathscr{P}\_{2}(\mathbb{R}^{d}), and we shall argue that the mapping Γ\Gamma has a fixed point μ^∈ℰ\widehat{\mu}\in\mathscr{E}, where ℰ\mathscr{E} is defined by ([5.5](https://arxiv.org/html/2510.11829v1#S5.E5 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). Clearly, if Γ​(μ^)=μ^\Gamma(\widehat{\mu})=\widehat{\mu}, then we can still define α^=αμ^\widehat{\alpha}=\alpha^{\widehat{\mu}}, and by Lemma [5.3](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem3 "Lemma 5.3 ([29, Lemma 3.1]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") we have ℙXαμ^=μ^\mathbb{P}\_{X^{\alpha^{\widehat{\mu}}}}=\widehat{\mu}. Thus by ([6.5](https://arxiv.org/html/2510.11829v1#S6.E5 "In 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), for any α∈𝕃𝔽02​([0,T])\alpha\in\mathbb{L}^{2}\_{\mathbb{F}^{0}}([0,T]) we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Jk​(α^)\displaystyle J^{k}(\widehat{\alpha}) | =\displaystyle= | J​(α^)+k​G​(μ^)=k​G​(μ^)+𝔼​[log⁡ρμ^​(XTα^)]−𝔼​[log⁡hμ^​(0,X0α^)]\displaystyle J(\widehat{\alpha})+kG(\widehat{\mu})=kG(\widehat{\mu})+\mathbb{E}[\log\rho^{\widehat{\mu}}(X^{\widehat{\alpha}}\_{T})]-\mathbb{E}[\log h^{\widehat{\mu}}(0,X^{\widehat{\alpha}}\_{0})] |  |
|  |  | ≤\displaystyle\leq | k​G​(ℙXTα)+𝔼​[log⁡ρμ^​(XTα)]−𝔼​[log⁡hμ^​(0,X0α)]≤Jk​(α).\displaystyle kG(\mathbb{P}\_{X^{\alpha}\_{T}})+\mathbb{E}[\log\rho^{\widehat{\mu}}(X^{\alpha}\_{T})]-\mathbb{E}[\log h^{\widehat{\mu}}(0,X^{\alpha}\_{0})]\leq J^{k}(\alpha). |  |

Here in the above the first inequality is due to ([6.6](https://arxiv.org/html/2510.11829v1#S6.E6 "In 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), and the last inequality is due to ([6.1](https://arxiv.org/html/2510.11829v1#S6.E1 "In 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). This shows that α^\widehat{\alpha} is the minimizer of Jk​(⋅)J^{k}(\cdot).

We now show that the set ℰ⊂𝒟μini\mathscr{E}\subset\mathscr{D}\_{{\mu\_{\rm ini}}} defined by ([5.5](https://arxiv.org/html/2510.11829v1#S5.E5 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) satisfies all the necessary properties, thanks to the Lemma [5.6](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem6 "Lemma 5.6. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and Proposition [5.8](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem8 "Proposition 5.8. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") that we established in the last section, so that the mapping Γ\Gamma possesses a fixed point on ℰ\mathscr{E} by Schauder’s fixed-point theorem.
Our main result is as follows.

###### Theorem 6.1.

Assume that Assumptions
[5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")
is in force. Consider the set ℰ\mathscr{E} defined by ([5.5](https://arxiv.org/html/2510.11829v1#S5.E5 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). Then the following hold:

(i) ℰ\mathscr{E} is convex and closed under Prohorov metric, and 𝒮ℰ{\cal S}\_{\mathscr{E}} is convex and closed in 𝕃1​(ℝd)\mathbb{L}^{1}(\mathbb{R}^{d});

(ii) Γ​(ℰ)⊆ℰ\Gamma(\mathscr{E})\subseteq\mathscr{E}, and is precompact in 𝒫2​(ℝd)\mathscr{P}\_{2}(\mathbb{R}^{d}), under both Prohorov and Wasserstein metric;

(iii) Γ\Gamma is continuous on ℰ\mathscr{E}, under Prohorov metric.

Consequently, the mapping Γ\Gamma has a fixed point in ℰ\mathscr{E}.

###### Proof.

Since the last statement is a direct consequence of Schauder’s fixed point theorem, applying to the space 𝒫​(ℝd)\mathscr{P}(\mathbb{R}^{d}) with Prohorov metric, we need only prove the properties (i)-(iii).

(i) is obvious.

(ii) By definition of 𝒮ℰ{\cal S}\_{\mathscr{E}} we rewrite ([6.6](https://arxiv.org/html/2510.11829v1#S6.E6 "In 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) as

|  |  |  |
| --- | --- | --- |
|  | fμ′=arg​minfμ¯∈𝒮ℰ⁡{k​G​(μ¯)+∫ℝdlog⁡ρμ​(y)​fμ¯​(y)​𝑑y}.f\_{\mu^{\prime}}=\operatorname\*{arg\,min}\_{f\_{\bar{\mu}}\in{\cal S}\_{\mathscr{E}}}\Big\{kG({\bar{\mu}})+\int\_{\mathbb{R}^{d}}\log\rho^{\mu}(y)f\_{\bar{\mu}}(y)dy\Big\}. |  |

Since 𝒮ℰ{\cal S}\_{\mathscr{E}} is convex and closed in 𝕃1​(ℝd)\mathbb{L}^{1}(\mathbb{R}^{d}), it follows that fμ′∈𝒮ℰf\_{\mu^{\prime}}\in{\cal S}\_{\mathscr{E}}, and thus Γ​(ℰ)⊆ℰ\Gamma(\mathscr{E})\subseteq\mathscr{E}.
We are to show that Γ​(ℰ)\Gamma(\mathscr{E}) is precompact in 𝒫2​(ℝd)\mathscr{P}\_{2}(\mathbb{R}^{d}).

To this end, let {μn}⊆Γ​(ℰ)\{\mu\_{n}\}\subseteq\Gamma(\mathscr{E}) be any sequence, we shall find a subsequence {μnk}k≥1\{\mu\_{n\_{k}}\}\_{k\geq 1} such that limk→∞μnk=μ∈𝒫2​(ℝ2)\lim\_{k\to\infty}\mu\_{n\_{k}}=\mu\in\mathscr{P}\_{2}(\mathbb{R}^{2}), under both Prohorov metric and W2W\_{2}-metric. Since Γ​(ℰ)⊆ℰ\Gamma(\mathscr{E})\subseteq\mathscr{E}, by Lemma [5.6](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem6 "Lemma 5.6. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(i), {fμn}\{f\_{\mu\_{n}}\} is bounded in
𝕃2​(ℝd)\mathbb{L}^{2}(\mathbb{R}^{d}). Thus by Banach-Alaoglu Theorem and noting that 𝕃2\mathbb{L}^{2} is reflexive, {fμn}\{f\_{\mu\_{n}}\} is weakly compact, that is, there exists a subsequence {fμnk}\{f\_{\mu\_{n\_{k}}}\} such that fμnk​⇀wfμf\_{\mu\_{n\_{k}}}\mathop{\mathrel{\mathop{\kern 0.0pt\rightharpoonup}\limits^{w}}}f\_{\mu} in 𝕃2​(ℝd)\mathbb{L}^{2}(\mathbb{R}^{d}), as k→∞k\to\infty. But this amounts to
saying the μnk⇒μ\mu\_{n\_{k}}\Rightarrow\mu in Prohorov metric. This, together with Lemma [5.6](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem6 "Lemma 5.6. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(ii) and the relationship between Wasserstein distance and weak convergence (see, e.g., [[65](https://arxiv.org/html/2510.11829v1#bib.bib65), Theorem 7.12]), leads to that limk→∞μnk=μ\lim\_{k\to\infty}\mu\_{n\_{k}}=\mu
in 𝒫2​(ℝd)\mathscr{P}\_{2}(\mathbb{R}^{d}), proving (ii).

(iii) Let us assume that {μn}⊂ℰ\{\mu\_{n}\}\subset\mathscr{E} such that μn⇒μ\mu\_{n}\Rightarrow\mu in Prohorov metric.
The stability result in Proposition [5.8](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem8 "Proposition 5.8. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") shows that ρμn=Γ1​(μn)→Γ1​(μ)=ρμ∈𝒮\rho^{\mu\_{n}}=\Gamma\_{1}(\mu\_{n})\to\Gamma\_{1}(\mu)=\rho^{\mu}\in{\cal S} in 𝕃1​(ℝd)\mathbb{L}^{1}(\mathbb{R}^{d}). Next, we show that Γ2​(ρμn)⇒Γ2​(ρμ)\Gamma\_{2}(\rho^{\mu\_{n}})\Rightarrow\Gamma\_{2}(\rho^{\mu}) in Prohorov metric. Recall the definition of Γ2\Gamma\_{2}, we define a family of
functionals on ℰ\mathscr{E}: for each k,n∈ℕk,n\in\mathbb{N} and μ¯∈ℰ\bar{\mu}\in\mathscr{E},

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Fnk​(μ¯):=k​G​(μ¯)+∫ℝdlog⁡ρμn​(y)​μ¯​(d​y);Fk​(μ¯):=k​G​(μ¯)+∫ℝdlog⁡ρμ​(y)​μ¯​(d​y).\displaystyle\left\{\begin{array}[]{lll}\displaystyle F^{k}\_{n}(\bar{\mu}):=kG(\bar{\mu})+\int\_{\mathbb{R}^{d}}\log\rho^{\mu\_{n}}(y)\bar{\mu}(dy);\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \displaystyle F^{k}(\bar{\mu}):=kG(\bar{\mu})+\int\_{\mathbb{R}^{d}}\log\rho^{\mu}(y)\bar{\mu}(dy).\end{array}\right. |  | (6.9) |

Then μn′=Γ2​(ρμn):=arg​minμ¯∈ℰ⁡Fnk​(μ¯)\mu\_{n}^{\prime}=\Gamma\_{2}(\rho^{\mu\_{n}}):=\operatorname\*{arg\,min}\_{\bar{\mu}\in\mathscr{E}}F^{k}\_{n}(\bar{\mu}) and μ′=Γ2​(ρμ):=arg​minμ¯∈ℰ⁡Fk​(μ¯)\mu^{\prime}=\Gamma\_{2}(\rho^{\mu}):=\operatorname\*{arg\,min}\_{\bar{\mu}\in\mathscr{E}}F^{k}(\bar{\mu}).

To show that the minimizers μn′⇒μ′\mu^{\prime}\_{n}\Rightarrow\mu^{\prime}, we shall invoke
the notion of Γ\Gamma-convergence (cf. [[19](https://arxiv.org/html/2510.11829v1#bib.bib19)]). To be more precise, a sequence {Fn}n≥1\{F\_{n}\}\_{n\geq 1} is said to Γ\Gamma-converge to
FF as n→∞n\to\infty if

|  |  |  |  |
| --- | --- | --- | --- |
|  | {For every sequence μ¯n⇒μ¯, it holds that F​(μ¯)≤lim¯nFnk​(μ¯n);There exists a sequence μ¯n⇒μ¯, such that F​(μ¯)≥lim¯nFn​(μ¯n).\displaystyle\left\{\begin{array}[]{lll}\mbox{For every sequence $\bar{\mu}\_{n}\Rightarrow\bar{\mu}$, it holds that $\displaystyle F(\bar{\mu})\leq\mathop{\underline{\rm lim}}\_{n}F^{k}\_{n}(\bar{\mu}\_{n})$};\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \mbox{There exists a sequence $\bar{\mu}\_{n}\Rightarrow\bar{\mu}$, such that $\displaystyle F(\bar{\mu})\geq\mathop{\overline{\rm lim}}\_{n}F\_{n}(\bar{\mu}\_{n})$.}\end{array}\right. |  | (6.12) |

Now, note that GG is convex and ℰ\mathscr{E} is compact under Prohorov metric, we see that both {Fnk}\{F^{k}\_{n}\} and FkF^{k} are coercive (in the sense that there exists minimizing sequence in ℰ⊂𝒫2​(ℝd)\mathscr{E}\subset\mathscr{P}\_{2}(\mathbb{R}^{d})). Thus, in light of the Γ\Gamma-convergence result (see [[19](https://arxiv.org/html/2510.11829v1#bib.bib19), Theorem 7.1]), in order to show μn′⇒μ′\mu\_{n}^{\prime}\Rightarrow\mu^{\prime}, it suffices to check that {Fnk}\{F^{k}\_{n}\} Γ\Gamma-converges to FkF^{k}, for each kk. To see this, for any {μ¯n}⊂ℰ\{\bar{\mu}\_{n}\}\subset\mathscr{E}, such that μ¯n⇒μ¯\bar{\mu}\_{n}\Rightarrow\bar{\mu}, by Lemma [5.6](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem6 "Lemma 5.6. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(iii), we have fμ¯n→fμ¯f\_{\bar{\mu}\_{n}}\to f\_{\bar{\mu}} in
𝕃1\mathbb{L}^{1}, and therefore by Dominated Convergence,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | |∫ℝd(logρμn(y)μ¯n(dy)−∫ℝdlogρμ(y)μ¯(dy)|\displaystyle\Big|\int\_{\mathbb{R}^{d}}(\log\rho^{\mu\_{n}}(y)\bar{\mu}\_{n}(dy)-\int\_{\mathbb{R}^{d}}\log\rho^{\mu}(y)\bar{\mu}(dy)\Big| |  |
|  |  | ≤\displaystyle\leq | ∫ℝd|log⁡ρμn​(y)|​|fμ¯n​(y)−fμ¯​(y)|​𝑑y+∫ℝd|log⁡ρμn​(y)−log⁡ρμ​(y)|​μ¯​(d​y)\displaystyle\int\_{\mathbb{R}^{d}}|\log\rho^{\mu\_{n}}(y)||f\_{\bar{\mu}\_{n}}(y)-f\_{\bar{\mu}}(y)|dy+\int\_{\mathbb{R}^{d}}|\log\rho^{\mu\_{n}}(y)-\log\rho^{\mu}(y)|\bar{\mu}(dy) |  |
|  |  | ≤\displaystyle\leq | log⁡(Kδ)​‖fμ¯n−fμ¯‖𝕃1+∫ℝd|log⁡ρμn​(y)−log⁡ρμ​(y)|​μ¯​(d​y)→0,as n→∞.\displaystyle\log\big(\frac{K}{\delta}\big)\|f\_{\bar{\mu}\_{n}}-f\_{\bar{\mu}}\|\_{\mathbb{L}^{1}}+\int\_{\mathbb{R}^{d}}|\log\rho^{\mu\_{n}}(y)-\log\rho^{\mu}(y)|\bar{\mu}(dy)\to 0,\quad\mbox{as $n\to\infty$.} |  |

Finally, since G​(⋅)G(\cdot) is continuous on 𝒫2​(ℝd)\mathscr{P}\_{2}(\mathbb{R}^{d}), by definition ([6.9](https://arxiv.org/html/2510.11829v1#S6.E9 "In 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) we see that Fnk​(μ¯n)→Fk​(μ¯)F^{k}\_{n}(\bar{\mu}\_{n})\to F^{k}(\bar{\mu}) whenever μ¯n⇒μ¯\bar{\mu}\_{n}\Rightarrow\bar{\mu}. Thus by ([6.12](https://arxiv.org/html/2510.11829v1#S6.E12 "In 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) we see that {Fnk}\{F^{k}\_{n}\} Γ\Gamma-converges to FkF^{k}, as n→∞n\to\infty. This completes the proof.
∎

Finally, we shall establish an
analogue of Theorem [4.1](https://arxiv.org/html/2510.11829v1#S4.ThmTheorem1 "Theorem 4.1. ‣ 4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") in the case of general μini∈𝒫2​(ℝd){\mu\_{\rm ini}}\in\mathscr{P}\_{2}(\mathbb{R}^{d}). For technical convenience, in what follows we shall make use of the following extra assumptions to facilitate our discussion. Recall the function ξ\xi and η\eta defined by ([5.14](https://arxiv.org/html/2510.11829v1#S5.E14 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) and ([5.15](https://arxiv.org/html/2510.11829v1#S5.E15 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), respectively.

###### Assumption 6.2.

(i) The penalty function GG satisfies G​(μ;μtar)≥W2​(μ,μtar)G(\mu;\mu\_{\rm tar})\geq W\_{2}(\mu,\mu\_{\rm tar});

(ii) In Assumption [3.2](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(ii), the function ϕ\phi satisfies ‖ϕ​(⋅)​eξ​(⋅)‖∞<∞\|\phi(\cdot)e^{\xi(\cdot)}\|\_{\infty}<\infty;

(iii) For any R>0R>0, there exists MR>0M\_{R}>0, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[η2​(XTt,x)]=∫ℝdη2​(y)​p​(T,y;t,x)​𝑑y≤MR,(t,x)∈[0,T]×BR,\displaystyle\mathbb{E}[\eta^{2}(X^{t,x}\_{T})]=\int\_{\mathbb{R}^{d}}\eta^{2}(y)p(T,y;t,x)dy\leq M\_{R},\qquad(t,x)\in[0,T]\times B\_{R}, |  | (6.13) |

where BR:={x∈ℝd:|x|≤R}B\_{R}:=\{x\in\mathbb{R}^{d}:|x|\leq R\}.
∎

###### Remark 6.3.

(1) Assumption [6.2](https://arxiv.org/html/2510.11829v1#S6.ThmTheorem2 "Assumption 6.2. ‣ 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(i) is not overly restrictive, and can be justified by Example [3.5](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem5 "Example 3.5. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday").

(2) Note that the function ϕ\phi in Assumption [3.2](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(ii) satisfies ϕ​(y)​eλ​|y|2≤C\phi(y)e^{\lambda|y|^{2}}\leq C, for some λ>0\lambda>0 and that ξ​(y)∼λ′​|y|2\xi(y)\sim\lambda^{\prime}|y|^{2}, as |y|→∞|y|\to\infty, Assumption [6.2](https://arxiv.org/html/2510.11829v1#S6.ThmTheorem2 "Assumption 6.2. ‣ 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(ii) amounts to saying that ϕ\phi and ξ\xi are compatible.

(3) While Assumption [6.2](https://arxiv.org/html/2510.11829v1#S6.ThmTheorem2 "Assumption 6.2. ‣ 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(iii) is slightly stronger than the requirement ([5.15](https://arxiv.org/html/2510.11829v1#S5.E15 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), it would be trivial if the mapping (t,x)↦𝔼​[η2​(XTt,x)](t,x)\mapsto\mathbb{E}[\eta^{2}(X^{t,x}\_{T})] is continuous, which is by no means stringent.
∎

Our last result of this section is the following.

###### Theorem 6.4.

Assume that the Assumptions [3.2](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), [5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and [6.2](https://arxiv.org/html/2510.11829v1#S6.ThmTheorem2 "Assumption 6.2. ‣ 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") are in force. Let μini∈ℰ{\mu\_{\rm ini}}\in\mathscr{E} be given, and
let α^​(t,x)\widehat{\alpha}(t,x) and α^k​(t,x)\widehat{\alpha}^{k}(t,x), (t,x)∈[0,T]×ℝd(t,x)\in[0,T]\times\mathbb{R}^{d} are optimal controls given in Proposition [3.6](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem6 "Proposition 3.6. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and Lemma [5.3](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem3 "Lemma 5.3 ([29, Lemma 3.1]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"), respectively. Then, for any R>0R>0, there exists CR>0C\_{R}>0, such that for any k∈ℕk\in\mathbb{N}, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0T|α^k​(t,x)−α^​(t,x)|​𝑑t≤CRk,(t,x)∈[0,T]×BR.\displaystyle\int\_{0}^{T}|\widehat{\alpha}^{k}(t,x)-\widehat{\alpha}(t,x)|dt\leq\frac{C\_{R}}{k},\qquad(t,x)\in[0,T]\times B\_{R}. |  | (6.14) |

###### Proof.

We begin by denoting μk:=ℙXTα^k\mu^{k}:=\mathbb{P}\_{X\_{T}^{\widehat{\alpha}^{k}}}, μtar:=ℙXTα^{\mu\_{\rm tar}}:=\mathbb{P}\_{X\_{T}^{\widehat{\alpha}}}, and let ρμk=Γ1​(μk)\rho^{\mu\_{k}}=\Gamma\_{1}(\mu\_{k}), k∈ℕk\in\mathbb{N},
ρμtar=Γ1​(μtar)\rho^{\mu\_{\rm tar}}=\Gamma\_{1}({\mu\_{\rm tar}}), respectively, as we defined before. Next, applying ([5.12](https://arxiv.org/html/2510.11829v1#S5.E12 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |ρμk​(y)−ρμtar​(y)|=|eψμk​(y)​fμk​(y)−eψμtar​(y)​fμtar​(y)|≤eψμtar​(y)​|fμk​(y)−fμtar​(y)|+fμk​(y)​|eψμk​(y)−eψμtar​(y)|.\displaystyle\begin{split}|\rho^{\mu\_{k}}(y)-\rho^{\mu\_{\rm tar}}(y)|&=|e^{\psi^{\mu\_{k}}(y)}f\_{\mu\_{k}}(y)-e^{\psi^{{\mu\_{\rm tar}}}(y)}f\_{\mu\_{\rm tar}}(y)|\\ &\leq e^{\psi^{{\mu\_{\rm tar}}}(y)}|f\_{\mu\_{k}}(y)-f\_{\mu\_{\rm tar}}(y)|+f\_{\mu\_{k}}(y)|e^{\psi^{\mu\_{k}}(y)}-e^{\psi^{{\mu\_{\rm tar}}}(y)}|.\end{split} | |  | (6.15) |

Let us now recall some facts from §4. First, note that the optimality of μk\mu\_{k} implies that G​(μk)≤CkG(\mu\_{k})\leq\frac{C}{k} (cf. ([4.3](https://arxiv.org/html/2510.11829v1#S4.E3 "In 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday"))), for some generic constant C>0C>0 independent of kk, which we shall allow to vary from line to line below. Thus, by virtue of Assumption [3.2](https://arxiv.org/html/2510.11829v1#S3.ThmTheorem2 "Assumption 3.2. ‣ 3 Existence of Optimal Policies for SCSBP’s ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(ii), we can write

|  |  |  |
| --- | --- | --- |
|  | |fμk​(y)−fμtar​(y)|≤Ck​ϕ​(y),y∈ℝd,|f\_{\mu\_{k}}(y)-f\_{\mu\_{\rm tar}}(y)|\leq\frac{C}{k}\phi(y),\qquad y\in\mathbb{R}^{d}, |  |

where ϕ​(y)​eξ​(y)≤C\phi(y)e^{\xi(y)}\leq C, y∈ℝdy\in\mathbb{R}^{d}, thanks to Assumption [6.2](https://arxiv.org/html/2510.11829v1#S6.ThmTheorem2 "Assumption 6.2. ‣ 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(ii). Furthermore, under Assumption [6.2](https://arxiv.org/html/2510.11829v1#S6.ThmTheorem2 "Assumption 6.2. ‣ 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(i), we can assume without loss of generality that the Schrödinger potentials ψμk\psi^{\mu\_{k}} and ψμtar\psi^{{\mu\_{\rm tar}}} all satisfy estimates ([5.13](https://arxiv.org/html/2510.11829v1#S5.E13 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) and ([5.14](https://arxiv.org/html/2510.11829v1#S5.E14 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")). Consequently, by Assumption [6.2](https://arxiv.org/html/2510.11829v1#S6.ThmTheorem2 "Assumption 6.2. ‣ 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(i) and an easy application of Lemma [5.7](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem7 "Lemma 5.7 ([10, Theorem 1.1]). ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and Newton-Leibniz formula we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |eψμtar​(y)−eψμtar​(y)|\displaystyle|e^{\psi^{{\mu\_{\rm tar}}}(y)}-e^{\psi^{{\mu\_{\rm tar}}}(y)}| | =|ψμtar(y)−ψμtar(y)|∫01exp{ψμtar(y)+θ(ψμk(y)−ψμtar(y)}dθ\displaystyle=|{\psi^{{\mu\_{\rm tar}}}(y)}-{\psi^{{\mu\_{\rm tar}}}(y)}|\int\_{0}^{1}\exp\{\psi^{\mu\_{\rm tar}}(y)+\theta(\psi^{\mu\_{k}}(y)-\psi^{\mu\_{\rm tar}}(y)\}d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​eξ​(y)​W2​(μk,μtar)≤C​eξ​(y)​G​(μk)≤Ck​eξ​(y),y∈ℝd.\displaystyle\leq Ce^{\xi(y)}W\_{2}(\mu\_{k},{\mu\_{\rm tar}})\leq Ce^{\xi(y)}G(\mu\_{k})\leq\frac{C}{k}e^{\xi(y)},\quad y\in\mathbb{R}^{d}. |  |

Summarizing above and recalling Assumption [5.4](https://arxiv.org/html/2510.11829v1#S5.ThmTheorem4 "Assumption 5.4. ‣ 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday") and ([5.15](https://arxiv.org/html/2510.11829v1#S5.E15 "In 5 Stability of the Solutions to the SBP ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), we derive from ([6.15](https://arxiv.org/html/2510.11829v1#S6.E15 "In 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) that

|  |  |  |
| --- | --- | --- |
|  | |ρμk​(y)−ρμtar​(y)|≤Ck​(eψμtar​(y)​ϕ​(y)+fμk​(y)​eξ​(y))≤Ck​(eξ​(y)​ϕ​(y)+g2​(y)​eξ​(y))≤Ck​(1+η​(y)),\displaystyle|\rho^{\mu\_{k}}(y)-\rho^{\mu\_{\rm tar}}(y)|\leq\frac{C}{k}\left(e^{\psi^{{\mu\_{\rm tar}}}(y)}\phi(y)+f\_{\mu\_{k}}(y)e^{\xi(y)}\right)\leq\frac{C}{k}\left(e^{\xi(y)}\phi(y)+g^{2}(y)e^{\xi(y)}\right)\leq\frac{C}{k}(1+\eta(y)), |  |

and therefore, given R>0R>0, and (t,x)∈[0,T]×BR(t,x)\in[0,T]\times B\_{R}, we apply Assumption [6.2](https://arxiv.org/html/2510.11829v1#S6.ThmTheorem2 "Assumption 6.2. ‣ 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")-(iii) to get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|ρμk​(XTt,x)−ρμtar​(XTt,x)|]≤𝔼​[|ρμk​(XTt,x)−ρμtar​(XTt,x)|2]12≤CRk,\displaystyle\mathbb{E}[|\rho^{\mu\_{k}}(X^{t,x}\_{T})-\rho^{\mu\_{\rm tar}}(X^{t,x}\_{T})|]\leq\mathbb{E}[|\rho^{\mu\_{k}}(X^{t,x}\_{T})-\rho^{\mu\_{\rm tar}}(X^{t,x}\_{T})|^{2}]^{\frac{1}{2}}\leq\frac{C\_{R}}{k}, |  | (6.16) |

where CR>0C\_{R}>0 is some constant depending on the generic constant CC above and MRM\_{R} in ([6.13](https://arxiv.org/html/2510.11829v1#S6.E13 "In Assumption 6.2. ‣ 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")).

To complete the proof, let us recall that optimal strategies are of the form α^k​(t,x)=∇log⁡hk​(t,x)\widehat{\alpha}^{k}(t,x)=\nabla\log h^{k}(t,x), k∈ℕk\in\mathbb{N}, and α^​(t,x)=∇log⁡h​(t,x)\widehat{\alpha}(t,x)=\nabla\log h(t,x), and hk​(t,x)h^{k}(t,x) and h​(t,x)h(t,x) are the solutions to the respective PDEs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∂thk​(t,x)+ℒt​hk​(t,x)=0;hk​(T,x)=ρμk​(x).{∂th​(t,x)+ℒt​h​(t,x)=0;h​(T,x)=ρμtar​(x),\displaystyle\begin{cases}\partial\_{t}h^{k}(t,x)+\mathscr{L}\_{t}h^{k}(t,x)=0;\\ h^{k}(T,x)=\rho^{\mu\_{k}}(x).\end{cases}\quad\quad\begin{cases}\partial\_{t}h(t,x)+\mathscr{L}\_{t}h(t,x)=0;\\ h(T,x)=\rho^{\mu\_{\rm tar}}(x),\end{cases} |  | (6.17) |

Furthermore, noting that hk​(t,x)=𝔼​[ρμk​(XTt,x)]h^{k}(t,x)=\mathbb{E}[\rho^{\mu\_{k}}(X^{t,x}\_{T})], h​(t,x)=𝔼​[ρμtar​(XTt,x)]h(t,x)=\mathbb{E}[\rho^{{\mu\_{\rm tar}}}(X^{t,x}\_{T})], and by the Bismut-Elworthy-Li formula we have

|  |  |  |
| --- | --- | --- |
|  | ∇hk​(t,x)=𝔼​[ρμk​(XTt,x)​NTt,x];∇h​(t,x)=𝔼​[ρμtar​(XTt,x)​NTt,x].\nabla h^{k}(t,x)=\mathbb{E}[\rho^{\mu\_{k}}(X^{t,x}\_{T})N^{t,x}\_{T}];\quad\nabla h(t,x)=\mathbb{E}[\rho^{{\mu\_{\rm tar}}}(X^{t,x}\_{T})N^{t,x}\_{T}]. |  |

Thus, we have |∇h​(t,x)|≤𝔼​[η2​(XTt,x)]12​𝔼​[|NTt,x|]12≤CRT−t|\nabla h(t,x)|\leq\mathbb{E}[\eta^{2}(X^{t,x}\_{T})]^{\frac{1}{2}}\mathbb{E}[|N^{t,x}\_{T}|]^{\frac{1}{2}}\leq\frac{C\_{R}}{\sqrt{T-t}}, whenever (t,x)∈[0,T]×BR(t,x)\in[0,T]\times B\_{R}, and a similar argument as in ([4.9](https://arxiv.org/html/2510.11829v1#S4.E9 "In 4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) and ([4.11](https://arxiv.org/html/2510.11829v1#S4.E11 "In 4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), together with the estimate ([6.16](https://arxiv.org/html/2510.11829v1#S6.E16 "In 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), leads to that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∇hk​(t,x)−∇h​(t,x)|≤CRk​T−t;|hk​(t,x)−h​(t,x)|≤CRk,(t,x)∈[0,T]×BR.\displaystyle|\nabla h^{k}(t,x)-\nabla h(t,x)|\leq\frac{C\_{R}}{k\sqrt{T-t}};\quad|h^{k}(t,x)-h(t,x)|\leq\frac{C\_{R}}{k},\quad(t,x)\in[0,T]\times B\_{R}. |  | (6.18) |

Finally, we note that by definition the function hh is positive everywhere (unless ρμtar≡0\rho^{\mu\_{\rm tar}}\equiv 0), and being the classical solution to the PDE ([6.17](https://arxiv.org/html/2510.11829v1#S6.E17 "In 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) it is continuous. Thus, given R>0R>0, h​(t,x)≥δR>0h(t,x)\geq\delta\_{R}>0, for all (t,x)∈[0,T]×BR(t,x)\in[0,T]\times B\_{R}. Since ([6.18](https://arxiv.org/html/2510.11829v1#S6.E18 "In 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")) implies that hkh^{k} converges to hh uniformly on compacts, thus it must hold that
hk​(t,x)≥δR/2h^{k}(t,x)\geq\delta\_{R}/2, for (t,x)∈[0,T]×BR(t,x)\in[0,T]\times B\_{R}, and kk large enough. We therefore conclude,
similar to ([4.1](https://arxiv.org/html/2510.11829v1#S4.Ex5 "4.1 The Convergence of Optimal Policies ‣ 4 Convergence Results under Delta Initial Distribution ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")), that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |α^k​(t,x)−α^​(t,x)|\displaystyle|\widehat{\alpha}^{k}(t,x)-\widehat{\alpha}(t,x)| | ≤|∇hk​(t,x)−∇h​(t,x)hk​(t,x)|+|∇h​(t,x)|​|h​(t,x)−hk​(t,x)hk​(t,x)​h​(t,x)|≤CRk​T−t,\displaystyle\leq\left|\frac{\nabla h^{k}(t,x)-\nabla h(t,x)}{h^{k}(t,x)}\right|+|\nabla h(t,x)|\left|\frac{h(t,x)-h^{k}(t,x)}{h^{k}(t,x)h(t,x)}\right|\leq\frac{C\_{R}}{k\sqrt{T-t}}, |  |

as k→∞k\to\infty, for (t,x)∈[0,T]×BR(t,x)\in[0,T]\times B\_{R}, where CRC\_{R} depends on MRM\_{R} and δR\delta\_{R} above, but independent of kk. Integrating in tt we obtain ([6.14](https://arxiv.org/html/2510.11829v1#S6.E14 "In Theorem 6.4. ‣ 6 Existence of optimal control and convergence for general 𝜇ᵢₙᵢ ‣ Schrödinger bridge for generative AI: Soft-constrained formulation and convergence analysis1footnote 11footnote 1We thank helpful comments and discussions from Rama Cont, Huyên Pham, Xin Zhang, and Xun Yu Zhou. In celebration of Prof. Xun Yu Zhou’s 60th birthday")).
∎

## 7 Conclusion

We study the soft-constrained Schrödinger bridge problem (SCSBP) as a flexible alternative to the classical formulation for generative modeling. By replacing hard terminal constraints with a general penalty function, the SCSBP potentially offers greater flexibility and stability for generative AI tasks. Moreover, we establish linear convergence of both the value functions and the optimal controls as the penalty parameter tends to infinity, thereby providing a theoretical guarantee for the framework.

In future work, we will develop efficient algorithms for learning the SCSBP solutions and test the performance on benchmark generative AI tasks. This will allow us to translate the theoretical framework into practical tools, further demonstrating the potential of regularized stochastic control formulations for modern generative modeling.

## References

* [1]

  B. Acciaio, S. Eckstein, and S. Hou.
  Time-causal vae: Robust financial time series generator.
  arXiv preprint arXiv:2411.02947, 2024.
* [2]

  A. Alouadi, B. Barreau, L. Carlier, and H. Pham.
  Robust time series generation via schr\\backslash" odinger bridge: a
  comprehensive evaluation.
  arXiv preprint arXiv:2503.02943, 2025.
* [3]

  D. G. Aronson.
  Bounds for the fundamental solution of a parabolic equation.
  1967.
* [4]

  Y. Bai, E. Yang, B. Han, Y. Yang, J. Li, Y. Mao, G. Niu, and T. Liu.
  Understanding and improving early stopping for learning with noisy
  labels.
  Advances in Neural Information Processing Systems,
  34:24392–24403, 2021.
* [5]

  J.-D. Benamou, G. Chazareix, and G. Loeper.
  From entropic transport to martingale transport, and applications to
  model calibration.
  arXiv preprint arXiv:2406.11537, 2024.
* [6]

  J. Betker, G. Goh, L. Jing, T. Brooks, J. Wang, L. Li, L. Ouyang, J. Zhuang,
  J. Lee, Y. Guo, et al.
  Improving image generation with better captions.
  Computer Science. https://cdn. openai. com/papers/dall-e-3.
  pdf, 2(3):8, 2023.
* [7]

  A. Beurling.
  An automorphism of product measures.
  Annals of Mathematics, 72(1):189–200, 1960.
* [8]

  J.-M. Bismut.
  Large Deviation and Malliavin Calculus, volume 45 of Progress in Mathematics.
  Birkhäser, 1984.
* [9]

  H. Cao, H. Gu, X. Guo, and M. Rosenbaum.
  Risk of transfer learning and its applications in finance.
  arXiv preprint arXiv:2311.03283, 2023.
* [10]

  G. Carlier, L. Chizat, and M. Laborde.
  Displacement smoothness of entropic optimal transport.
  ESAIM: Control, Optimisation and Calculus of Variations, 30:25,
  2024.
* [11]

  M. Chen, K. Huang, T. Zhao, and M. Wang.
  Score approximation, estimation and distribution recovery of
  diffusion models on low-dimensional data.
  In International Conference on Machine Learning, pages
  4672–4712. PMLR, 2023.
* [12]

  M. Chen, R. Xu, Y. Xu, and R. Zhang.
  Diffusion factor models: Generating high-dimensional returns with
  factor structure.
  arXiv preprint arXiv:2504.06566, 2025.
* [13]

  T. Chen, G.-H. Liu, and E. A. Theodorou.
  Likelihood training of schr\\backslash" odinger bridge using
  forward-backward sdes theory.
  arXiv preprint arXiv:2110.11291, 2021.
* [14]

  Y. Chen, T. T. Georgiou, and M. Pavon.
  Stochastic control liaisons: Richard sinkhorn meets gaspard monge on
  a schrodinger bridge.
  Siam Review, 63(2):249–313, 2021.
* [15]

  Z. Chen, A. Mustafi, P. Glaser, A. Korba, A. Gretton, and B. K. Sriperumbudur.
  (de)-regularized maximum mean discrepancy gradient flow.
  arXiv preprint arXiv:2409.14980, 2024.
* [16]

  A. Chiarini, G. Conforti, G. Greco, and L. Tamanini.
  Gradient estimates for the schrödinger potentials: convergence to
  the brenier map and quantitative stability.
  Communications in Partial Differential Equations,
  48(6):895–943, 2023.
* [17]

  S.-N. Chow, W. Li, C. Mou, and H. Zhou.
  Dynamical schrödinger bridge problems on graphs.
  Journal of Dynamics and Differential Equations, pages 1–20,
  2022.
* [18]

  P. Dai Pra.
  A stochastic control approach to reciprocal diffusion processes.
  Applied mathematics and Optimization, 23(1):313–329, 1991.
* [19]

  G. Dal Maso.
  Introduction to Gamma-convergence.
  Springer Science + Business Media, LLC, 1993.
* [20]

  V. De Bortoli, J. Thornton, J. Heng, and A. Doucet.
  Diffusion schrödinger bridge with applications to score-based
  generative modeling.
  Advances in Neural Information Processing Systems,
  34:17695–17709, 2021.
* [21]

  W. E. Deming and F. F. Stephan.
  On a least squares adjustment of a sampled frequency table when the
  expected marginal totals are known.
  The Annals of Mathematical Statistics, 11(4):427–444, 1940.
* [22]

  V. Divol, J. Niles-Weed, and A.-A. Pooladian.
  Tight stability bounds for entropic brenier maps.
  International Mathematics Research Notices, 2025(7):rnaf078,
  2025.
* [23]

  D. A. Edwards.
  On the kantorovish-rubinstein theorem.
  Expositiones Mathematicae, 29:387–398, 2011.
* [24]

  K. D. Elworthy and X. M. Li.
  Formulae for the derivatives of heat semigroups.
  Journal of Functional Analysis, 125:252–286, 1994.
* [25]

  H. Föllmer.
  Random fields and diffusion processes.
  In École d’Été de Probabilités de Saint-Flour
  XV–XVII, 1985–87, pages 101–203. Springer, 2006.
* [26]

  R. Fortet.
  Résolution d’un système d’équations de m.
  schrödinger.
  Journal de mathématiques pures et appliquées,
  19(1-4):83–105, 1940.
* [27]

  E. Fournié, J.-M. Lasry, J. Lebuchoux, P.-L. Lions, and N. Touzi.
  Applications of malliavin calculus to monte carlo methods in finance.
  Finance and Stochastics, 3:391–412, 1999.
* [28]

  H. Fu, Z. Yang, M. Wang, and M. Chen.
  Unveil conditional diffusion models with classifier-free guidance: A
  sharp statistical theory.
  arXiv preprint arXiv:2403.11968, 2024.
* [29]

  J. Garg, X. Zhang, and Q. Zhou.
  Soft-constrained schrödinger bridge: a stochastic control
  approach.
  In International Conference on Artificial Intelligence and
  Statistics, pages 4429–4437. PMLR, 2024.
* [30]

  X. Gu, C. Du, T. Pang, C. Li, M. Lin, and Y. Wang.
  On memorization in diffusion models.
  arXiv preprint arXiv:2310.02664, 2023.
* [31]

  F. F. Gunsilius.
  On the convergence rate of potentials of brenier maps.
  Econometric Theory, 38(2):381–417, 2022.
* [32]

  M. Hamdouche, P. Henry-Labordere, and H. Pham.
  Generative modeling for time series via schr {\{\\backslash" o}\}
  dinger bridge.
  arXiv preprint arXiv:2304.05093, 2023.
* [33]

  Y. Han, M. Razaviyayn, and R. Xu.
  Neural network-based score estimation in diffusion models:
  Optimization and generalization.
  arXiv preprint arXiv:2401.15604, 2024.
* [34]

  Y. Han, M. Razaviyayn, and R. Xu.
  Stochastic control for fine-tuning diffusion models: Optimality,
  regularity, and convergence.
  arXiv preprint arXiv:2412.18164, 2024.
* [35]

  C. Hernández and L. Tangpi.
  Propagation of chaos for mean field schr\\backslash" odinger
  problems.
  arXiv preprint arXiv:2304.09340, 2023.
* [36]

  J. Ho, A. Jain, and P. Abbeel.
  Denoising diffusion probabilistic models.
  In Neurips, volume 33, pages 6840–6851, 2020.
* [37]

  B. Jamison.
  The markov processes of schrödinger.
  Zeitschrift für Wahrscheinlichkeitstheorie und verwandte
  Gebiete, 32(4):323–331, 1975.
* [38]

  L. Kong, H. Wang, T. Wang, G. Xiong, and M. Tambe.
  Composite flow matching for reinforcement learning with
  shifted-dynamics data.
  arXiv preprint arXiv:2505.23062, 2025.
* [39]

  S. Kullback and R. Leibler.
  On information and sufficiency.
  Annals of Mathematical Statistics, 22(1):79–86, 1951.
* [40]

  C. Léonard.
  A survey of the schr\\backslash" odinger problem and some of its
  connections with optimal transport.
  arXiv preprint arXiv:1308.0215, 2013.
* [41]

  P. Li, Z. Li, H. Zhang, and J. Bian.
  On the generalization properties of diffusion models.
  Advances in Neural Information Processing Systems,
  36:2097–2127, 2023.
* [42]

  G. Loeper, J. Obloj, and B. Joseph.
  Calibration of local volatility models with stochastic interest rates
  using optimal transport.
  arXiv preprint arXiv:2305.00200, 2023.
* [43]

  J. Ma and J. Zhang.
  Representation theorems for backward stochastic differential
  equations.
  Annals of Applied Probability, 12(4):1390–1418, 2002.
* [44]

  E. F. Montesuma, F. M. N. Mboula, and A. Souloumiac.
  Recent advances in optimal transport for machine learning.
  IEEE Transactions on Pattern Analysis and Machine Intelligence,
  2024.
* [45]

  T. Moon, M. Choi, G. Lee, J.-W. Ha, and J. Lee.
  Fine-tuning diffusion models with limited data.
  In NeurIPS 2022 Workshop on Score-Based Methods, 2022.
* [46]

  M. Nutz and J. Wiesel.
  Entropic optimal transport: Convergence of potentials.
  Probability Theory and Related Fields, 184(1):401–424, 2022.
* [47]

  OpenAI.
  Sora: Creating video from text.
  <https://openai.com/sora>, 2024.
* [48]

  Y. Ouyang, L. Xie, H. Zha, and G. Cheng.
  Transfer learning for diffusion models.
  Advances in Neural Information Processing Systems,
  37:136962–136989, 2024.
* [49]

  S. Peluchetti.
  Diffusion bridge mixture transports, schrödinger bridge problems
  and generative modeling.
  Journal of Machine Learning Research, 24(374):1–51, 2023.
* [50]

  P. E. Protter.
  Stochastic Integration and Differential Equations.
  Springer-Verlag, Heidelberg, second edition, 2005.
* [51]

  A. Ramesh, P. Dhariwal, A. Nichol, C. Chu, and M. Chen.
  Hierarchical text-conditional image generation with clip latents.
  arXiv preprint arXiv:2204.06125, 1(2):3, 2022.
* [52]

  L. Richter and J. Berner.
  Improved sampling via learned diffusions.
  arXiv preprint arXiv:2307.01198, 2023.
* [53]

  R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer.
  High-resolution image synthesis with latent diffusion models.
  In Proceedings of the IEEE/CVF conference on computer vision and
  pattern recognition, pages 10684–10695, 2022.
* [54]

  Y. Shi, V. De Bortoli, A. Campbell, and A. Doucet.
  Diffusion schrödinger bridge matching.
  Advances in Neural Information Processing Systems, 36, 2024.
* [55]

  J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan, and S. Ganguli.
  Deep unsupervised learning using nonequilibrium thermodynamics.
  In International Conference on Machine Learning, pages
  2256–2265. PMLR, 2015.
* [56]

  K.-U. Song.
  Applying regularized schr\\backslash" odinger-bridge-based
  stochastic process in generative modeling.
  arXiv preprint arXiv:2208.07131, 2022.
* [57]

  Y. Song and S. Ermon.
  Generative modeling by estimating gradients of the data distribution.
  Advances in neural information processing systems, 32, 2019.
* [58]

  Y. Song, J. Sohl-Dickstein, D. P. Kingma, A. Kumar, S. Ermon, and B. Poole.
  Score-based generative modeling through stochastic differential
  equations.
  arXiv preprint arXiv:2011.13456, 2020.
* [59]

  T. Sweeting.
  On a converse to scheffé’s theorem.
  The Annals of Statistics, 14(3):1252–1256, 1986.
* [60]

  W. Tang.
  Fine-tuning of diffusion models via stochastic control: entropy
  regularization and beyond.
  arXiv preprint arXiv:2403.06279, 2024.
* [61]

  L. Torrey and J. Shavlik.
  Transfer learning.
  In Handbook of research on machine learning applications and
  trends: algorithms, methods, and techniques, pages 242–264. IGI Global
  Scientific Publishing, 2010.
* [62]

  M. Uehara, Y. Zhao, K. Black, E. Hajiramezanali, G. Scalia, N. L. Diamant,
  A. M. Tseng, T. Biancalani, and S. Levine.
  Fine-tuning of continuous-time diffusion models as
  entropy-regularized control.
  arXiv preprint arXiv:2402.15194, 2024.
* [63]

  F. Vargas, S. Padhy, D. Blessing, and N. Nüsken.
  Transport meets variational inference: Controlled monte carlo
  diffusions.
  arXiv preprint arXiv:2307.01050, 2023.
* [64]

  F. Vargas, P. Thodoroff, A. Lamacraft, and N. Lawrence.
  Solving schrödinger bridges via maximum likelihood.
  Entropy, 23(9):1134, 2021.
* [65]

  C. Villani.
  Topics in Optimal Transportation.
  Graduate Studies in Mathematics, 58. AMS, Providence, RI, 2003.
* [66]

  G. Wang, Y. Jiao, Q. Xu, Y. Wang, and C. Yang.
  Deep generative learning via schrödinger bridge.
  In International conference on machine learning, pages
  10794–10804. PMLR, 2021.
* [67]

  L. Winkler, C. Ojeda, and M. Opper.
  A score-based approach for training schrödinger bridges for data
  modelling.
  Entropy, 25(2):316, 2023.
* [68]

  T. Xu, L. K. Wenliang, M. Munn, and B. Acciaio.
  Cot-gan: Generating sequential data via causal optimal transport.
  Advances in neural information processing systems,
  33:8798–8809, 2020.
* [69]

  J. Zhang.
  Backward stochastic differential equations.
  Springer, 2017.
* [70]

  H. Zhao, H. Chen, Y. Guo, G. I. Winata, T. Ou, Z. Huang, D. D. Yao, and
  W. Tang.
  Fine-tuning diffusion generative models via rich preference
  optimization.
  arXiv preprint arXiv:2503.11720, 2025.