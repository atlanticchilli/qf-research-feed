---
authors:
- Chiheb Ben Hammouda
- Truong Ngoc Nguyen
doc_id: arxiv:2602.06424v1
family_id: arxiv:2602.06424
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk
url_abs: http://arxiv.org/abs/2602.06424v1
url_html: https://arxiv.org/html/2602.06424v1
venue: arXiv q-fin
version: 1
year: 2026
---


Chiheb Ben Hammouda
Mathematical Institute, Utrecht University, 3584 CD Utrecht, the Netherlands

Truong Ngoc Nguyen
Corresponding Author: Email: n.t.nguyen@uu.nl
Mathematical Institute, Utrecht University, 3584 CD Utrecht, the Netherlands

###### Abstract

Multivariate shortfall risk measures provide a principled framework for quantifying systemic risk and determining capital allocations prior to aggregation in interconnected financial systems. Despite their well-established theoretical properties, the numerical estimation of multivariate shortfall risk and the corresponding optimal allocations remains computationally challenging, as existing Monte Carlo–based approaches can be numerically expensive due to slow convergence.

In this work, we develop a new class of single- and multilevel numerical algorithms for estimating multivariate shortfall risk and the associated optimal allocations, based on a combination of Fourier inversion techniques and randomized quasi–Monte Carlo (RQMC) sampling. Rather than operating in physical space, our approach evaluates the relevant expectations appearing in the risk constraint and its optimization in the frequency domain, where the integrands exhibit enhanced smoothness properties that are well suited for RQMC integration. We establish a rigorous mathematical framework for the resulting Fourier-RQMC estimators, including convergence analysis and computational complexity bounds. Beyond the single-level method, we introduce a multilevel RQMC scheme that exploits the geometric convergence of the underlying deterministic optimization algorithm to reduce computational cost while preserving accuracy.

Numerical experiments demonstrate that the proposed Fourier–RQMC methods outperform sample average approximation and stochastic optimization benchmarks in terms of accuracy and computational cost across a range of models for the risk factors and loss structures. Consistent with the theoretical analysis, these results demonstrate improved asymptotic convergence and complexity rates relative to the benchmark methods, with additional savings achieved through the proposed multilevel RQMC construction.

Keywords: Multivariate risk measures, systemic risk, risk allocations, randomized quasi-Monte Carlo, Fourier inversion, multilevel algorithms, asymptotic convergence, complexity rates.
MSC2020 classifications: 65C05, 65D30, 42A38, 65Y20, 91G45, 91G60.

## 1 Introduction

Systemic risk is the risk that the entire financial system could fail due to the inherent characteristics of the system itself. Such a risk can trigger severe economic losses, requiring effective tools for its assessment and control. To this end, risk assessment methods must be accurate, coherent, and capable of assessing risks and informing capital allocation across interconnected financial components, such as portfolios, financial institutions, and clearinghouse members.

Two modelling approaches have been proposed in the literature. In the *post-aggregation* view (i.e., *aggregate first, then allocate*)[[13](https://arxiv.org/html/2602.06424v1#bib.bib197 "An Axiomatic Approach to Systemic Risk"), [12](https://arxiv.org/html/2602.06424v1#bib.bib37 "Measuring and Allocating Systemic Risk")], systemic risk measures are interpreted as the minimal amount of capital required to secure the financial system after aggregating losses across individual institutions, i.e., we first compress the multivariate loss vector 𝐗=(X1,…,Xd)\mathbf{X}=(X\_{1},\ldots,X\_{d}) through an aggregator Λ\Lambda and then apply a univariate risk functional η\eta,

|  |  |  |
| --- | --- | --- |
|  | R​(𝐗)=η​(Λ​(𝐗)).R(\mathbf{X})=\eta\!\big(\Lambda(\mathbf{X})\big). |  |

While conceptually appealing, this aggregation step collapses the multivariate loss profile into a single scalar quantity, potentially obscuring information about interdependencies and interactions among system components not encoded by Λ\Lambda. In contrast, the *pre-aggregation* view (i.e., *allocate first, then aggregate*) [[20](https://arxiv.org/html/2602.06424v1#bib.bib196 "Measures of Systemic Risk"), [9](https://arxiv.org/html/2602.06424v1#bib.bib28 "A unified approach to systemic risk measures via acceptance sets"), [36](https://arxiv.org/html/2602.06424v1#bib.bib198 "Systemic risk measures on general measurable spaces")] allocates capital componentwise before aggregation, leading to risk measures of the form

|  |  |  |
| --- | --- | --- |
|  | R​(𝐗)=inf{∑i=1dmi:Λ​(𝐗+𝐦)∈𝒜},R(\mathbf{X})=\inf\Bigl\{\sum\_{i=1}^{d}m\_{i}:\Lambda(\mathbf{X}+\mathbf{m})\in\mathcal{A}\Bigr\}, |  |

where 𝐦=(m1,…,md)\mathbf{m}=(m\_{1},\dots,m\_{d}) denotes the capital allocation vector and 𝒜\mathcal{A} is an acceptance set. This formulation preserves the multivariate dependence structure among the components of the system and yields both a total risk measure and consistent component-wise capital allocations.

Beyond their theoretical formulation, systemic risk measures must be monitored on a regular basis—monthly or even weekly—making computational efficiency and numerical scalability essential. In this work, we adopt the pre-aggregation perspective and focus on the efficient computation of the Multivariate Shortfall Risk Measure (MSRM) introduced by [[1](https://arxiv.org/html/2602.06424v1#bib.bib204 "Multivariate Shortfall Risk Allocation and Systemic Risk")].

Computing the MSRM requires repeatedly evaluating expectations involving the loss function and its gradient, which enter the first-order optimality conditions of the associated allocation problem along an optimization trajectory. This repeated evaluation of expectation-based quantities constitutes the main computational bottleneck. Two main numerical approaches were introduced in the literature. The first is *Sample-Average Approximation* (SAA) [[1](https://arxiv.org/html/2602.06424v1#bib.bib204 "Multivariate Shortfall Risk Allocation and Systemic Risk")], where NN i.i.d. samples of 𝐗\mathbf{X} are drawn *once* at the beginning, required expectations are approximated by their Monte Carlo (MC) estimators, and subsequently solved using standard deterministic optimization methods. In unconstrained stochastic optimization, SAA attains the canonical,
dimension-independent convergence rate 𝒪​(N−1/2)\mathcal{O}\left(N^{-1/2}\right) for optimal solutions under suitable
regularity conditions [[28](https://arxiv.org/html/2602.06424v1#bib.bib35 "Monte Carlo Sampling-Based Methods for Stochastic Optimization"), [34](https://arxiv.org/html/2602.06424v1#bib.bib34 "A Guide to Sample Average Approximation")], a rate that is often regarded as slow in practice [[24](https://arxiv.org/html/2602.06424v1#bib.bib26 "Monte Carlo Methods in Financial Engineering")]. In the MSRM setting, however, the literature typically does not provide a convergence analysis for the corresponding SAA estimators. In contrast, [[33](https://arxiv.org/html/2602.06424v1#bib.bib203 "Estimation of Systemic Shortfall Risk Measure Using Stochastic Algorithms")] proposes a second approach based on stochastic approximation (SA), in which the optimizer is updated iteratively using noisy gradient information obtained from samples of the loss vector 𝐗\mathbf{X}, following a Robbins–Monro–type scheme [[2](https://arxiv.org/html/2602.06424v1#bib.bib40 "Computing VaR and CVaR using Stochastic Approximation and Adaptive Unconstrained Importance Sampling"), [19](https://arxiv.org/html/2602.06424v1#bib.bib39 "Stochastic Root Finding and Efficient Estimation of Convex Risk Measures")].
While these SA algorithms are carefully adapted to the MSRM framework and are shown to converge theoretically, the numerical experiments in [[33](https://arxiv.org/html/2602.06424v1#bib.bib203 "Estimation of Systemic Shortfall Risk Measure Using Stochastic Algorithms")] suggest that their numerical performance can be inferior to that of SAA-based methods.

In this work, we address this computational challenge by developing efficient numerical methods for MSRM that operate in the frequency domain and are tailored to the optimization-driven structure of the problem. Our approach combines Fourier-based representations of the MSRM optimality conditions with randomized quasi–Monte Carlo (RQMC) sampling to efficiently evaluate the expectation-based quantities required along the allocation optimization trajectory. Compared to previously proposed Monte Carlo–based approaches [[1](https://arxiv.org/html/2602.06424v1#bib.bib204 "Multivariate Shortfall Risk Allocation and Systemic Risk"), [33](https://arxiv.org/html/2602.06424v1#bib.bib203 "Estimation of Systemic Shortfall Risk Measure Using Stochastic Algorithms")], our method exploits the smoothness of frequency-domain integrands and the improved error convergence properties of RQMC. Building on this single-level framework, we further introduce a multilevel strategy that leverages the fast local (geometric) convergence of the underlying numerical optimization scheme to reduce overall computational cost while preserving accuracy.

In risk measurement, QMC methods have been used primarily within the post-aggregation paradigm, where computations are performed in physical space on the aggregated portfolio loss, most notably for quantile-based risk measures such as VaR and CVaR [[35](https://arxiv.org/html/2602.06424v1#bib.bib32 "Measuring Portfolio Risk Using Quasi Monte Carlo Methods"), [3](https://arxiv.org/html/2602.06424v1#bib.bib27 "Recursive Computation of Value-at-Risk and Conditional Value-at-Risk using MC and QMC"), [26](https://arxiv.org/html/2602.06424v1#bib.bib7 "Convergence analysis of quasi-Monte Carlo sampling for quantile and expected shortfall")]. Under suitable smoothness assumptions, QMC estimators in this setting can achieve convergence rates of order 𝒪​(N−1)\mathcal{O}(N^{-1}) [[26](https://arxiv.org/html/2602.06424v1#bib.bib7 "Convergence analysis of quasi-Monte Carlo sampling for quantile and expected shortfall")]. A key limitation of these approaches is their strong sensitivity to both the effective dimension and the regularity of the integrand. In risk measurement, loss functions and their gradients often involve kinks or discontinuities, which can severely degrade QMC efficiency when treated directly in physical space. These issues are further exacerbated in pre-aggregation frameworks such as MSRM, where expectations depend on an evolving allocation vector along a high-dimensional optimization trajectory. As a result, regularity must be preserved uniformly over the allocation iterates generated by the optimization algorithm, rather than only at a single scalar value. Consequently, despite their success in post-aggregation settings, applications of QMC and RQMC methods to pre-aggregation risk measures remain scarce.

One possible route to improving the regularity structure111Besides alternative approaches based on analytical or numerical smoothing, as explored for example in the context of option pricing in [[5](https://arxiv.org/html/2602.06424v1#bib.bib2 "Hierarchical adaptive sparse grids and quasi-Monte Carlo for option pricing under the rough Bergomi model"), [6](https://arxiv.org/html/2602.06424v1#bib.bib3 "Numerical smoothing with hierarchical adaptive sparse grids and quasi-Monte Carlo methods for efficient option pricing")]. is to work in the frequency domain, leveraging Fourier representations when characteristic functions of the loss vector are available. In the MSRM setting, Fourier-based techniques have been explored primarily in [[1](https://arxiv.org/html/2602.06424v1#bib.bib204 "Multivariate Shortfall Risk Allocation and Systemic Risk")], where they are used mainly as numerical benchmarks against SAA-type methods and are reported to exhibit limited practical efficiency relative to SAA. However, this approach remains largely heuristic and does not systematically exploit the potential advantages of QMC integration. In particular, the proposed implementation in [[1](https://arxiv.org/html/2602.06424v1#bib.bib204 "Multivariate Shortfall Risk Allocation and Systemic Risk")] relies on generic Gaussian quadrature rules that scale poorly with dimension, offers limited guidance on the choice of contour-shift (damping) parameters, which are selected ad hoc despite their critical role in controlling the smoothness of the resulting Fourier integrands [[7](https://arxiv.org/html/2602.06424v1#bib.bib71 "Optimal Damping with Hierarchical Adaptive Quadrature for Efficient Fourier Pricing of Multi-Asset Options in Lévy Models")], and does not provide a unified analytical framework ensuring stability and accuracy along the optimization trajectory. Moreover, neither a rigorous error analysis nor a computational complexity analysis is provided.

These limitations highlight the need for a systematic formulation that tightly couples Fourier representations, regularity control, and optimization-aware numerical integration, while remaining robust along the optimization trajectory. We address this need by developing an optimization-aware Fourier–RQMC framework for MSRM, together with a rigorous error and complexity analysis that demonstrates its convergence properties and computational advantages over SA and SAA-based approaches. Although developed in the context of MSRM, the proposed theoretical and numerical framework naturally extends to other classes of multivariate risk measures for which suitable Fourier representations and optimization regularity conditions are available.

##### Our contributions.

The main contributions of this work are summarized as follows:

* •

  We develop a new class of single-level and multilevel numerical algorithms for estimating multivariate shortfall risk measures and the associated optimal capital allocations, based on a combination of Fourier inversion techniques and RQMC sampling. The proposed design incorporates carefully constructed damping rules and domain transformations to preserve the regularity structure of the Fourier integrands associated with the loss functions and their gradients, uniformly along the allocation iterates (see Sections [3](https://arxiv.org/html/2602.06424v1#S3 "3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") and [4](https://arxiv.org/html/2602.06424v1#S4 "4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).
* •

  We introduce a multilevel RQMC construction whose sample allocation explicitly exploits the local geometric convergence of the underlying deterministic optimization algorithm, leading to work-optimal sampling strategies and further reductions in computational complexity.
* •

  We provide a rigorous error and complexity analysis of the proposed single-level and multilevel Fourier–RQMC schemes for the MSRM problem, establishing improved asymptotic convergence and complexity rates relative to the benchmark methods (see Section [5](https://arxiv.org/html/2602.06424v1#S5 "5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"); Appendix [A](https://arxiv.org/html/2602.06424v1#A1 "Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).
* •

  Building on ideas introduced in [[7](https://arxiv.org/html/2602.06424v1#bib.bib71 "Optimal Damping with Hierarchical Adaptive Quadrature for Efficient Fourier Pricing of Multi-Asset Options in Lévy Models")] in the context of option pricing, we design an adaptive damping strategy across optimization iterations, complemented by a regularized update rule that ensures robustness under repeated evaluation of evolving integrands along the optimization trajectory. In addition, we provide theoretical guarantees for the convexity of the resulting damping-selection problem (se Section [3.1](https://arxiv.org/html/2602.06424v1#S3.SS1 "3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") and Appendix [B](https://arxiv.org/html/2602.06424v1#A2 "Appendix B Supplementary results for Section 3.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).
* •

  We adapt the domain transformation for RQMC integration proposed in [[4](https://arxiv.org/html/2602.06424v1#bib.bib72 "Quasi-Monte Carlo with Domain Transformation for Efficient Fourier Pricing of Multi-Asset Options")] to the repeated integration problems arising along an optimization trajectory. Moreover, we provide an alternative derivation of the transformation rule based on a detailed analysis and control of boundary oscillations tailored to our setting (see Section [4.1.1](https://arxiv.org/html/2602.06424v1#S4.SS1.SSS1 "4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"); Appendix [C](https://arxiv.org/html/2602.06424v1#A3 "Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).
* •

  We demonstrate the computational advantages of the proposed Fourier–RQMC methods through different numerical experiments, using SAA and SA as benchmarks across different loss functions, risk-factor distributions, and dimensional settings. The experiments further illustrate the additional savings achieved through the proposed multilevel RQMC construction (see Section [6](https://arxiv.org/html/2602.06424v1#S6 "6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

##### Organization of the paper.

The outline of this paper is as follows. Section [2](https://arxiv.org/html/2602.06424v1#S2 "2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") introduces the problem setting and the associated optimization framework. Section [3](https://arxiv.org/html/2602.06424v1#S3 "3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") presents the Fourier representations of the risk-measure problems together with the proposed optimal damping strategy. Section [4](https://arxiv.org/html/2602.06424v1#S4 "4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") develops the optimization-aware Fourier–RQMC framework and its multilevel extension. Section [5](https://arxiv.org/html/2602.06424v1#S5 "5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") provides a rigorous error and work–accuracy complexity analysis of the proposed methods. Finally, Section [6](https://arxiv.org/html/2602.06424v1#S6 "6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") reports the numerical experiments and results.

## 2 Optimization Framework for Multivariate Shortfall Risk

This section introduces the analytical setting and optimization framework for MSRM, together with the constrained optimization formulation used throughout the paper. We establish notation, define admissible multivariate loss functions and dependence structures, and recall key existence, uniqueness, and first-order optimality results for risk allocations. These results underpin the Sequential Quadratic Programming (SQP)-based numerical framework used to solve the MSRM problem.

###### Notation 2.1.

* •

  ∥.∥\left\lVert.\right\rVert denotes the Euclidean norm for vectors and the associated Frobenius norm for matrices, unless stated otherwise.
* •

  Let (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) be a probability space and let d∈ℕd\in\mathbb{N}. We denote by L0​(Ω;ℝd)L^{0}\left(\Omega;\mathbb{R}^{d}\right) the space of
  ℝd\mathbb{R}^{d}-valued ℱ\mathcal{F}-measurable random variables on
  (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}).
  For p∈[1,∞)p\in[1,\infty) we define Lp​(Ω;ℝd):={𝐗∈L0​(Ω;ℝd):𝔼​[‖𝐗‖p]<∞}L^{p}\left(\Omega;\mathbb{R}^{d}\right):=\bigl\{\mathbf{X}\in L^{0}\left(\Omega;\mathbb{R}^{d}\right):\mathbb{E}[\|\mathbf{X}\|^{p}]<\infty\bigr\}.
* •

  For p∈[1,∞)p\in[1,\infty), we denote the space of pp-integrable functions on ℝd\mathbb{R}^{d} as

  Lp(ℝd):={f:ℝd→ℝ|∫ℝd|f(x)|pdx<∞}.L^{p}(\mathbb{R}^{d}):=\Bigl\{f:\mathbb{R}^{d}\to\mathbb{R}\ \big|\ \int\_{\mathbb{R}^{d}}|f(x)|^{p}\,dx<\infty\Bigr\}.
* •

  For 𝐱,𝐲∈ℝd\mathbf{x},\mathbf{y}\in\mathbb{R}^{d} we define
  𝐱≥𝐲⟺xk≥yk\mathbf{x}\geq\mathbf{y}\;\Longleftrightarrow\;x\_{k}\geq y\_{k} for all k∈{1,…,d}k\in\{1,\dots,d\},
  and 𝐱>𝐲\mathbf{x}>\mathbf{y} if xk>ykx\_{k}>y\_{k} for all kk.
  Here xkx\_{k} and yky\_{k} denote the kk-th components of 𝐱\mathbf{x} and
  𝐲\mathbf{y}, respectively.
* •

  A generic element 𝐗=(X1,…,Xd)∈L0​(Ω;ℝd)\mathbf{X}=(X\_{1},\ldots,X\_{d})\in L^{0}(\Omega;\mathbb{R}^{d}) denotes an ℝd\mathbb{R}^{d}-valued random vector of (monetary) financial losses (i.e., for each k=1,…,dk=1,\ldots,d, the component XkX\_{k} represents the loss of institution kk. We assume that 𝐗\mathbf{X} admits a joint density f𝐗f\_{\mathbf{X}} on ℝd\mathbb{R}^{d} with the parameters denoted by 𝚯𝐗\boldsymbol{\Theta}\_{\mathbf{X}}.

We begin by defining a multivariate loss function ℓ:ℝd→(−∞,∞]\ell:\mathbb{R}^{d}\to(-\infty,\infty], which serves as the basic building block of the multivariate shortfall risk framework.

###### Definition 2.2 (Multivariate Loss Function).

A function ℓ:ℝd→(−∞,∞]\ell:\mathbb{R}^{d}\to(-\infty,\infty] is called a *loss function* if:

1. (A1)

   ℓ\ell is increasing: ℓ​(𝐱)≥ℓ​(𝐲)\ell(\mathbf{x})\geq\ell(\mathbf{y}) whenever 𝐱≥𝐲\mathbf{x}\geq\mathbf{y},with 𝐱,𝐲∈ℝd\mathbf{x},\mathbf{y}\in\mathbb{R}^{d};
2. (A2)

   ℓ\ell is convex and lower semicontinuous, with infℓ<0\inf\ell<0;
3. (A3)

   For 𝐱∈ℝd\mathbf{x}\in\mathbb{R}^{d}, ℓ​(𝐱)≥∑k=1dxk−c\ell(\mathbf{x})\geq\sum\_{k=1}^{d}x\_{k}-c for some constant c∈ℝc\in\mathbb{R}.

Throughout this work, we shall refer to ℓ\ell as a (multivariate) loss function if it satisfies Assumptions ([A1](https://arxiv.org/html/2602.06424v1#S2.I2.i1 "item A1 ‣ Definition 2.2 (Multivariate Loss Function). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"))–([A3](https://arxiv.org/html/2602.06424v1#S2.I2.i3 "item A3 ‣ Definition 2.2 (Multivariate Loss Function). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). We will additionally impose permutation invariance ([A4](https://arxiv.org/html/2602.06424v1#S2.I3.i4 "item A4 ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) when needed.

1. (A4)

   ℓ\ell is *permutation invariant*, which means ℓ​(𝐱)=ℓ​(π​(𝐱))\ell(\mathbf{x})=\ell(\pi(\mathbf{x})) for every permutation π\pi of the components.

Property ([A1](https://arxiv.org/html/2602.06424v1#S2.I2.i1 "item A1 ‣ Definition 2.2 (Multivariate Loss Function). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) states that the risk measure increases with losses. Property ([A2](https://arxiv.org/html/2602.06424v1#S2.I2.i2 "item A2 ‣ Definition 2.2 (Multivariate Loss Function). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) reflects that the diversification should not increase risk; the lower semi-continuity ensures that losses may exhibit one-sided jumps while still guaranteeing that the infimum of the risk measure is attained on the domain. Property ([A3](https://arxiv.org/html/2602.06424v1#S2.I2.i3 "item A3 ‣ Definition 2.2 (Multivariate Loss Function). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) ensures that the risk measure penalizes large losses more heavily than a risk-neutral evaluation. Assumption ([A4](https://arxiv.org/html/2602.06424v1#S2.I3.i4 "item A4 ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) implies that when the considered risk components are of the same nature, such as banks, clearinghouse members, or trading desks within the same trading floor, the loss function ℓ\ell encodes fairness, meaning that it should not discriminate against any particular component.

We now illustrate how to build a multivariate loss function from a one-dimensional loss function together with a coupling term that encodes dependence and interaction across components of the loss vector 𝐗\mathbf{X}.

###### Example 2.3.

Let h:ℝ→ℝh:\mathbb{R}\to\mathbb{R} be a one-dimensional loss function satisfying ([A1](https://arxiv.org/html/2602.06424v1#S2.I2.i1 "item A1 ‣ Definition 2.2 (Multivariate Loss Function). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"))–([A3](https://arxiv.org/html/2602.06424v1#S2.I2.i3 "item A3 ‣ Definition 2.2 (Multivariate Loss Function). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), and let Ξ:ℝd→ℝ\Xi:\mathbb{R}^{d}\to\mathbb{R} be a coupling functional modelling the dependence structure among the components of the loss vector, also satisfying ([A1](https://arxiv.org/html/2602.06424v1#S2.I2.i1 "item A1 ‣ Definition 2.2 (Multivariate Loss Function). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"))–([A3](https://arxiv.org/html/2602.06424v1#S2.I2.i3 "item A3 ‣ Definition 2.2 (Multivariate Loss Function). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). We construct a multivariate loss function ℓ\ell by222This generalizes class (C3) in [[1](https://arxiv.org/html/2602.06424v1#bib.bib204 "Multivariate Shortfall Risk Allocation and Systemic Risk"), Example 2.3]. As discussed in [[1](https://arxiv.org/html/2602.06424v1#bib.bib204 "Multivariate Shortfall Risk Allocation and Systemic Risk"), Section 4], the parameter α\alpha influences risk allocation through the dependence structure of the components of the loss vector 𝐗\mathbf{X}.

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | ℓ​(𝐱):=∑h​(xk)+α​Ξ​(𝐱),0≤α≤1.\ell\left(\mathbf{x}\right):=\sum h(x\_{k})+\alpha\Xi(\mathbf{x}),\quad 0\leq\alpha\leq 1. |  |

In this work, we consider two examples of multivariate loss functions constructed from ([2.1](https://arxiv.org/html/2602.06424v1#S2.E1 "In Example 2.3. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"))

1. (i)

   Exponential (entropic-type) loss function

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (2.2) |  | ℓexp​(𝐱):=11+α​[∑k=1deβ​xk+α​eβ​∑k=1dxk]−α+dα+1,α≥0,β≥0.\ell\_{\mathrm{exp}}(\mathbf{x}):=\frac{1}{1+\alpha}\left[\sum\_{k=1}^{d}e^{\beta x\_{k}}+\alpha\,e^{\beta\sum\_{k=1}^{d}x\_{k}}\right]-\frac{\alpha+d}{\alpha+1},\qquad\alpha\geq 0,\;\beta\geq 0. |  |
2. (ii)

   Quadratic pairwise coupling loss function (QPC)

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (2.3) |  | ℓqpc​(𝐱):=∑k=1dxk+12​∑k=1d(xk+)2+α​∑1≤j<k≤dxj+​xk+−1,α≥0.\ell\_{\mathrm{qpc}}(\mathbf{x}):=\sum\_{k=1}^{d}x\_{k}+\frac{1}{2}\sum\_{k=1}^{d}(x\_{k}^{+})^{2}+\alpha\sum\_{1\leq j<k\leq d}x\_{j}^{+}x\_{k}^{+}-1,\qquad\alpha\geq 0. |  |

where α\alpha and β\beta denote the systemic weight and the risk-aversion coefficient, respectively.

###### Assumption 2.4 (Integrability of the loss vector).

To ensure integrability, we assume that the loss vector 𝐗\mathbf{X} belongs to the following multivariate Orcliz heart:333Orlicz spaces have been widely used in the study of risk measures [[14](https://arxiv.org/html/2602.06424v1#bib.bib87 "Risk Measures on Orlicz Hearts")]. A detailed discussion of their properties in the multivariate sense can be found in Appendix B of [[1](https://arxiv.org/html/2602.06424v1#bib.bib204 "Multivariate Shortfall Risk Allocation and Systemic Risk")].

|  |  |  |  |
| --- | --- | --- | --- |
| (2.4) |  | Mγ={𝐗∈L0​(Ω;ℝd):𝔼​[γ​(λ​𝐗)]​<∞​ for all ​λ>​0},where ​γ​(𝐱):=ℓ​(|𝐱|),𝐱∈ℝd.M^{\gamma}=\left\{\mathbf{X}\in L^{0}\left(\Omega;\mathbb{R}^{d}\right):\mathbb{E}[\gamma(\lambda\mathbf{X})]<\infty\text{ for all }\lambda>0\right\},\quad\text{where }\gamma(\mathbf{x}):=\ell(|\mathbf{x}|),\ \mathbf{x}\in\mathbb{R}^{d}. |  |

Next, we recall the definition of the MSRM as introduced in [[1](https://arxiv.org/html/2602.06424v1#bib.bib204 "Multivariate Shortfall Risk Allocation and Systemic Risk"), Definition 2.7].

###### Definition 2.5 (Multivariate shortfall risk).

Let ℓ\ell be a multivariate loss function and that 𝐗∈Mγ\mathbf{X}\in M^{\gamma} be defined on (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}). The multivariate shortfall risk R​(𝐗)R(\mathbf{X}) is defined as

|  |  |  |  |
| --- | --- | --- | --- |
| (2.5) |  | R​(𝐗):=inf{∑k=1dmk:𝐦∈𝒜​(𝐗)}=inf{∑k=1dmk:𝔼​[ℓ​(𝐗−𝐦)]≤0},R(\mathbf{X}):=\inf\left\{\sum\_{k=1}^{d}m\_{k}:\mathbf{m}\in\mathcal{A}(\mathbf{X})\right\}=\inf\left\{\sum\_{k=1}^{d}m\_{k}:\mathbb{E}[\ell(\mathbf{X-m})]\leq 0\right\}, |  |

where 𝐦=(m1,…,md)\mathbf{m}=(m\_{1},\dots,m\_{d}) denotes the risk (capital) allocation vector, and the acceptance set is characterised as

|  |  |  |  |
| --- | --- | --- | --- |
| (2.6) |  | 𝒜​(𝐗):={𝐦∈ℝd:𝔼​[ℓ​(𝐗−𝐦)]≤0}.\mathcal{A}(\mathbf{X}):=\left\{\mathbf{m}\in\mathbb{R}^{d}:\mathbb{E}[\ell(\mathbf{X-m})]\leq 0\right\}. |  |

We now address the question of existence and uniqueness of risk allocations. To this end, we introduce the following definition and impose additional assumptions on the loss function ℓ\ell and the loss vector 𝐗\mathbf{X}.

###### Definition 2.6.

A vector 𝐦∈ℝd\mathbf{m}\in\mathbb{R}^{d} is called an *acceptable monetary risk allocation* if 𝐦∈𝒜​(𝐗)\mathbf{m}\in\mathcal{A}(\mathbf{X}) such that R​(𝐗)=∑k=1dmkR(\mathbf{X})=\sum\_{k=1}^{d}m\_{k}.

###### Assumption 2.7.

1. (A5)

   For every 𝐦𝟎∈ℝd\mathbf{m\_{0}}\in\mathbb{R}^{d}, the mapping 𝐦↦ℓ​(𝐗−𝐦)\mathbf{m}\mapsto\ell(\mathbf{X-m}) is differentiable at 𝐦0\mathbf{m}\_{0} almost surely (a.s).
2. (A6)

   Let 𝒰:={𝐮∈ℝd:∑ui=0}\mathcal{U}:=\left\{\mathbf{u}\in\mathbb{R}^{d}:\sum u\_{i}=0\right\}
   be the zero-sum allocations set. We assume that, for every 𝐱∈ℝd\mathbf{x}\in\mathbb{R}^{d},
   the function 𝐦↦ℓ​(𝐱+𝐦)\mathbf{m}\mapsto\ell(\mathbf{x}+\mathbf{m}) is strictly convex on 𝒰\mathcal{U}, and that ℓ​(𝐱)≥0\ell(\mathbf{x})\geq 0.

###### Theorem 2.8 (Theorem 3.4 in [[1](https://arxiv.org/html/2602.06424v1#bib.bib204 "Multivariate Shortfall Risk Allocation and Systemic Risk")]).

Let ℓ\ell be a loss function that satisfies Assumptions ([A4](https://arxiv.org/html/2602.06424v1#S2.I3.i4 "item A4 ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"))–([A5](https://arxiv.org/html/2602.06424v1#S2.I5.i5 "item A5 ‣ Assumption 2.7. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) and 𝐗∈Mγ\mathbf{X}\in M^{\gamma}. Then a risk allocation 𝐦∗∈ℝd\mathbf{m}^{\*}\in\mathbb{R}^{d} exists and is characterized by the first-order conditions (F.O.C.):

|  |  |  |  |
| --- | --- | --- | --- |
| (2.7) |  | (λ∗​𝔼​[∇ℓ​(𝐗−𝐦∗)]−𝟏𝔼​[ℓ​(𝐗−𝐦∗)])=𝟎,\begin{pmatrix}\lambda^{\*}\,\mathbb{E}\left[\nabla\ell(\mathbf{X}-\mathbf{m^{\*}})\right]-\mathbf{1}\\[3.0pt] \mathbb{E}[\ell(\mathbf{X}-\mathbf{m^{\*}})]\end{pmatrix}=\mathbf{0}, |  |

where λ∗>0\lambda^{\*}>0 is the Lagrange multiplier, and 𝟏:=(1,…,1)T∈ℝd\mathbf{1}:=(1,\dots,1)^{T}\in\mathbb{R}^{d}.
  
Moreover, if Assumption ([A6](https://arxiv.org/html/2602.06424v1#S2.I5.i6 "item A6 ‣ Assumption 2.7. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) holds, then the risk allocation 𝐦∗\mathbf{m}^{\*} is unique.

###### Remark 2.9.

Throughout the paper, the gradient ∇\nabla and the Hessian ∇2\nabla^{2} are taken with respect to (w.r.t.) the allocation vector 𝐦\mathbf{m}, unless the differentiation variable is explicitly indicated.

###### Remark 2.10.

Theorem 3.4 in [[1](https://arxiv.org/html/2602.06424v1#bib.bib204 "Multivariate Shortfall Risk Allocation and Systemic Risk")] is formulated in terms of subdifferentials and holds under the weaker standing Assumption ([A4](https://arxiv.org/html/2602.06424v1#S2.I3.i4 "item A4 ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), without requiring ([A5](https://arxiv.org/html/2602.06424v1#S2.I5.i5 "item A5 ‣ Assumption 2.7. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). Under Assumption ([A5](https://arxiv.org/html/2602.06424v1#S2.I5.i5 "item A5 ‣ Assumption 2.7. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), the subdifferential inclusion reduces to the F.O.C. in Theorem [2.8](https://arxiv.org/html/2602.06424v1#S2.Thmtheorem8 "Theorem 2.8 (Theorem 3.4 in [1]). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

###### Remark 2.11 (Interchanging Differentiation and Expectation).

Based on property ([A2](https://arxiv.org/html/2602.06424v1#S2.I2.i2 "item A2 ‣ Definition 2.2 (Multivariate Loss Function). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), the loss function ℓ\ell is locally Lipschitz on the interior of its effective domain; see [[48](https://arxiv.org/html/2602.06424v1#bib.bib192 "Another Proof that Convex Functions are Locally Lipschitz"), Theorem B]. Together with Assumption ([A5](https://arxiv.org/html/2602.06424v1#S2.I5.i5 "item A5 ‣ Assumption 2.7. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), this allows interchanging differentiation and expectation, yielding ∇𝔼​[ℓ​(𝐗−𝐦)]=𝔼​[∇ℓ​(𝐗−𝐦)]\nabla\mathbb{E}\left[\ell\left(\mathbf{X}-\mathbf{m}\right)\right]=\mathbb{E}[\nabla\ell(\mathbf{X}-\mathbf{m})].

When extending to the multivariate setting, the uniqueness of risk allocations becomes crucial. Without uniqueness, the total capital requirement may be distributed arbitrarily across components, potentially leading to outcomes that are not acceptable from a regulatory standpoint. For loss functions of the form ([2.1](https://arxiv.org/html/2602.06424v1#S2.E1 "In Example 2.3. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), we have the following corollary.

###### Corollary 2.12 (Uniqueness of the optimal allocation).

Let ℓ\ell be defined as in ([2.1](https://arxiv.org/html/2602.06424v1#S2.E1 "In Example 2.3. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) with a strictly convex univariate loss function hh.
Assume that the coupling term Ξ\Xi satisfies ([A4](https://arxiv.org/html/2602.06424v1#S2.I3.i4 "item A4 ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) and that Assumption ([A5](https://arxiv.org/html/2602.06424v1#S2.I5.i5 "item A5 ‣ Assumption 2.7. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) holds. Then, for every 𝐗∈Mγ\mathbf{X}\in M^{\gamma}, the associated multivariate shortfall risk admits a unique optimal allocation 𝐦∗\mathbf{m}^{\*}.

###### Proof.

The argument follows [[1](https://arxiv.org/html/2602.06424v1#bib.bib204 "Multivariate Shortfall Risk Allocation and Systemic Risk"), Proposition 3.8]. The term ∑k=1dh​(xk)\sum\_{k=1}^{d}h(x\_{k}) is permutation-invariant and thus ℓ\ell satisfies ([A4](https://arxiv.org/html/2602.06424v1#S2.I3.i4 "item A4 ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) whenever Ξ\Xi does. Moreover, strict convexity of hh yields the strict convexity property required for uniqueness (Assumption ([A6](https://arxiv.org/html/2602.06424v1#S2.I5.i6 "item A6 ‣ Assumption 2.7. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"))). Hence, the uniqueness conclusion follows from Theorem [2.8](https://arxiv.org/html/2602.06424v1#S2.Thmtheorem8 "Theorem 2.8 (Theorem 3.4 in [1]). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
∎

For convenience, we define g​(𝐦):=𝔼​[ℓ​(𝐗−𝐦)]g\left(\mathbf{m}\right):=\mathbb{E}\left[\ell\left(\mathbf{X}-\mathbf{m}\right)\right] and collect the primal–dual variables in 𝐳:=(𝐦,λ)\mathbf{z}:=(\mathbf{m},\lambda); this notation will be used throughout the following Sections when constructing Fourier–RQMC surrogate estimators for the gradient and Hessian of the Lagrangian.

The F.O.C. in ([2.7](https://arxiv.org/html/2602.06424v1#S2.E7 "In Theorem 2.8 (Theorem 3.4 in [1]). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) can be rewritten as:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.8) |  | ∇𝐳ℒ​(𝐳∗):=(λ∗​∇g​(𝐦∗)−1g​(𝐦∗))=0\nabla\_{\mathbf{z}}\mathcal{L}(\mathbf{z^{\*}}):=\begin{pmatrix}\lambda^{\*}\,\nabla g\left(\mathbf{m^{\*}}\right)-1\\[3.0pt] g\left(\mathbf{m^{\*}}\right)\end{pmatrix}=0 |  |

For the numerical analysis in Section [5](https://arxiv.org/html/2602.06424v1#S5 "5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), we also make use of the Hessian of the Lagrangian. Under Assumption ([C1](https://arxiv.org/html/2602.06424v1#A1.I1.i1 "item C1 ‣ Assumption A.1 (Regularity conditions for the exact problem). ‣ A.1 Additional Assumptions for the Error Analysis ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), it is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.9) |  | ∇𝐳2ℒ​(𝐳):=[−λ​∇2g​(𝐦)∇g​(𝐦)∇g​(𝐦)⊤0].\nabla^{2}\_{\mathbf{z}}\mathcal{L}(\mathbf{z}):=\begin{bmatrix}-\lambda\nabla^{2}g(\mathbf{m})&\nabla g(\mathbf{m})\\[3.0pt] \nabla g(\mathbf{m})^{\!\top}&0\end{bmatrix}. |  |

When solving ([2.7](https://arxiv.org/html/2602.06424v1#S2.E7 "In Theorem 2.8 (Theorem 3.4 in [1]). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) numerically, the expectation-based terms
g​(𝐦)g(\mathbf{m}), ∇g​(𝐦)\nabla g(\mathbf{m}), and ∇2g​(𝐦)\nabla^{2}g(\mathbf{m}) in ([2.8](https://arxiv.org/html/2602.06424v1#S2.E8 "In 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"))–([2.9](https://arxiv.org/html/2602.06424v1#S2.E9 "In 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"))
need to be estimated. Two common approaches are: (i) constructing *deterministic surrogates*
and applying deterministic optimizers [[1](https://arxiv.org/html/2602.06424v1#bib.bib204 "Multivariate Shortfall Risk Allocation and Systemic Risk")] or (ii) using *stochastic approximation* (SA) methods [[33](https://arxiv.org/html/2602.06424v1#bib.bib203 "Estimation of Systemic Shortfall Risk Measure Using Stochastic Algorithms")]. In this work, we
construct our methodology based on the former one. In particular, g​(𝐦)g(\mathbf{m}), ∇g​(𝐦)\nabla g(\mathbf{m}), and ∇2g​(𝐦)\nabla^{2}g(\mathbf{m}) are approximated by
g^Fou​(𝐦)\widehat{g}^{\mathrm{Fou}}(\mathbf{m}), g^∇Fou​(𝐦)\widehat{g}^{\mathrm{Fou}}\_{\nabla}(\mathbf{m}), and g^∇2Fou​(𝐦)\widehat{g}^{\mathrm{Fou}}\_{\nabla^{2}}(\mathbf{m}), respectively, using Fourier transform representations combined with single-level and multilevel RQMC methods. This will be explained in Sections [3](https://arxiv.org/html/2602.06424v1#S3 "3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") and [4](https://arxiv.org/html/2602.06424v1#S4 "4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). Once these surrogates are in place, the MSRM problem in ([2.5](https://arxiv.org/html/2602.06424v1#S2.E5 "In Definition 2.5 (Multivariate shortfall risk). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) becomes a deterministic nonlinear constrained optimization problem in 𝐦\mathbf{m}. We then compute 𝐳∗=(𝐦∗,λ∗)\mathbf{z}^{\*}=\left(\mathbf{m}^{\*},\lambda^{\*}\right) by solving ([2.8](https://arxiv.org/html/2602.06424v1#S2.E8 "In 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) numerically, for which a natural choice numerical optimizer is SQP [[40](https://arxiv.org/html/2602.06424v1#bib.bib75 "Numerical optimization"), Chapter 18].

Algorithm [1](https://arxiv.org/html/2602.06424v1#alg1 "Algorithm 1 ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") summarizes the generic SQP framework used throughout this work to solve the MSRM problem. The framework is built around surrogate-based Fourier–RQMC estimators and incorporates explicit control of statistical and optimization errors. In our numerical implementation, we adopt a practical variant of this framework, described in Remark [2.13](https://arxiv.org/html/2602.06424v1#S2.Ex4 "Remark 2.13 (SLSQP). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). Concrete constructions of the estimators and their associated error bounds are provided in the following sections.

Algorithm 1  SQP for MSRM Problem

1:Initial point 𝐳1=(𝐦1,λ1)\mathbf{z}\_{1}=(\mathbf{m}\_{1},\lambda\_{1}), surrogates g^Fou,g^∇Fou,g^∇2Fou\widehat{g}^{\mathrm{Fou}},\widehat{g}^{\mathrm{Fou}}\_{\nabla},\widehat{g}^{\mathrm{Fou}}\_{\nabla^{2}}, the prescribed convergence tolerance ε\varepsilon.
Note: The surrogates are estimated via Single-level Fourier-RQMC (see Section [4.1](https://arxiv.org/html/2602.06424v1#S4.SS1 "4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), Algorithm [3](https://arxiv.org/html/2602.06424v1#alg3 "Algorithm 3 ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) or Multilevel Fourier-RQMC (see Section [4.2](https://arxiv.org/html/2602.06424v1#S4.SS2 "4.2 Iteration-Indexed Multilevel Fourier–RQMC Approximation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), Algorithm [4](https://arxiv.org/html/2602.06424v1#alg4 "Algorithm 4 ‣ 4.2 Iteration-Indexed Multilevel Fourier–RQMC Approximation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

2:for each iteration j=1,2,…​Jj=1,2,\ldots J do

3:  Step 1: Linearization of the active constraint

4:Around 𝐦(j)\mathbf{m}^{(j)}, we approximate

|  |  |  |
| --- | --- | --- |
|  | g^Fou​(𝐦(j)+𝐝(j))≈g^Fou​(𝐦(j))+g^∇Fou​(𝐦(j))⊤​𝐝(j)≤0.\widehat{g}^{\mathrm{Fou}}(\mathbf{m}^{(j)}+\mathbf{d}^{(j)})\approx\widehat{g}^{\mathrm{Fou}}\left(\mathbf{m}^{(j)}\right)+\widehat{g}^{\mathrm{Fou}}\_{\nabla}\left(\mathbf{m}^{(j)}\right)^{\!\top}\mathbf{d}^{(j)}\leq 0. |  |

5:  Step 2: Formulation of the Quadratic subproblem (QP)

6:Solve the quadratic program

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝐝(j)∈ℝd\displaystyle\min\_{\mathbf{d}^{(j)}\in\mathbb{R}^{d}} | 𝟏⊤​𝐝(j),⊤+12​𝐝(j),⊤​λ(j)​g^∇2Fou​(𝐦(j))​𝐝(j)\displaystyle\mathbf{1}^{\!\top}\mathbf{d}^{(j),\top}+\tfrac{1}{2}\mathbf{d}^{(j),\top}\lambda^{(j)}\widehat{g}^{\mathrm{Fou}}\_{\nabla^{2}}\left(\mathbf{m}^{(j)}\right)\,\mathbf{d}^{(j)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. | g^Fou​(𝐦(j))+g^∇Fou​(𝐦(j))⊤​𝐝(j)=0.\displaystyle\widehat{g}^{\mathrm{Fou}}\left(\mathbf{m}^{(j)}\right)+\widehat{g}^{\mathrm{Fou}}\_{\nabla}\left(\mathbf{m}^{(j)}\right)^{\!\top}\mathbf{d}^{(j)}=0. |  |

7:  Step 3: Solve the QP problem

8:The pair Δ​𝐳(j):=(𝐝(j),p(j))\Delta\mathbf{z}^{(j)}:=(\mathbf{d}^{(j)},p^{(j)}) satisfies the KKT system:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.10) |  | [−λ(j)​g^∇2Fou​(𝐦(j))g^∇Fou​(𝐦(j))⊤g^∇Fou​(𝐦(j))0]⏟:=ℒ^∇𝐳2Fou​(𝐳(j))​[𝐝(j)p(j)]=[𝟏−λ(j)​g^∇Fou​(𝐦(j))−g^Fou​(𝐦(j))]⏟:=ℒ^∇𝐳Fou​(𝐳(j)).\underbrace{\begin{bmatrix}-\lambda^{(j)}\widehat{g}^{\mathrm{Fou}}\_{\nabla^{2}}\left(\mathbf{m}^{(j)}\right)&\widehat{g}^{\mathrm{Fou}}\_{\nabla}\left(\mathbf{m}^{(j)}\right)^{\!\top}\\[3.0pt] \widehat{g}^{\mathrm{Fou}}\_{\nabla}\left(\mathbf{m}^{(j)}\right)&0\end{bmatrix}}\_{:=\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}^{2}}^{\mathrm{Fou}}\left(\mathbf{z}^{(j)}\right)}\begin{bmatrix}\mathbf{d}^{(j)}\\[3.0pt] p^{(j)}\end{bmatrix}=\underbrace{\begin{bmatrix}\mathbf{1}-\lambda^{(j)}\widehat{g}^{\mathrm{Fou}}\_{\nabla}\left(\mathbf{m}^{(j)}\right)\\[3.0pt] -\widehat{g}^{\mathrm{Fou}}\left(\mathbf{m}^{(j)}\right)\end{bmatrix}}\_{:=\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}}\left(\mathbf{z}^{(j)}\right)}. |  |

9:  Step 4: Line search and update

10:Determine a step size αj∈(0,1]\alpha\_{j}\in(0,1] via a backtracking line search
using an appropriate merit function
(see [[40](https://arxiv.org/html/2602.06424v1#bib.bib75 "Numerical optimization"), Section 18.3]),
and update:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.11) |  | 𝐳(j+1)=𝐳(j)+α(j)​Δ​𝐳(j)\mathbf{z}^{(j+1)}=\mathbf{z}^{(j)}+\alpha^{(j)}\Delta\mathbf{z}^{(j)} |  |

11:  Step 5: Convergence check

12:  if |Δ​𝐳(j)|≤εopt\left\lvert\Delta\mathbf{z}^{(j)}\right\rvert\leq\varepsilon\_{\mathrm{opt}}, with εopt≤ε2\varepsilon\_{\mathrm{opt}}\leq\frac{\varepsilon}{2} then

13:    stop.

###### Remark 2.13 (SLSQP).

In the numerical experiments, Algorithm [1](https://arxiv.org/html/2602.06424v1#alg1 "Algorithm 1 ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") is realized using Sequential Least Squares Programming (SLSQP), a standard quasi-Newton variant of the SQP methodology. A key advantage of SLSQP is that it does not require explicit evaluation of exact second-order derivative information at every iteration. Instead, it relies on a quasi-Newton approximation (e.g., BFGS; see [[40](https://arxiv.org/html/2602.06424v1#bib.bib75 "Numerical optimization"), Chapters 6 and 18]) to capture the second-order information associated with the SQP subproblem. More precisely, SLSQP maintains a symmetric matrix
𝐁^Fou​(𝐦(j))∈ℝd×d\widehat{\mathbf{B}}^{\mathrm{Fou}}\left(\mathbf{m}^{(j)}\right)\in\mathbb{R}^{d\times d} which serves as an approximation of the Hessian of the Lagrangian. The initialization is typically chosen as 𝐁^Fou​(𝐦(1))=𝑰d\widehat{\mathbf{B}}^{\mathrm{Fou}}\left(\mathbf{m}^{(1)}\right)=\boldsymbol{I}\_{d} (or a diagonal approximation).
At iteration jj, the update takes the form

|  |  |  |
| --- | --- | --- |
|  | 𝐁^Fou​(𝐦(j+1))=𝐁^Fou​(𝐦(j))+𝐲(j)​𝐲(j),⊤𝐲(j),⊤​𝐬(j)−𝐁^Fou​(𝐦(j))​𝐬(j)​𝐬(j),⊤​𝐁^Fou​(𝐦(j))𝐬(j),⊤​𝐁^Fou​(𝐦(j))​𝐬(j),\widehat{\mathbf{B}}^{\mathrm{Fou}}\left(\mathbf{m}^{(j+1)}\right)=\widehat{\mathbf{B}}^{\mathrm{Fou}}\left(\mathbf{m}^{(j)}\right)+\frac{\mathbf{y}^{(j)}\mathbf{y}^{(j),\top}}{\mathbf{y}^{(j),\top}\mathbf{s}^{(j)}}-\frac{\widehat{\mathbf{B}}^{\mathrm{Fou}}\left(\mathbf{m}^{(j)}\right)\,\mathbf{s}^{(j)}\mathbf{s}^{(j),\top}\,\widehat{\mathbf{B}}^{\mathrm{Fou}}\left(\mathbf{m}^{(j)}\right)}{\mathbf{s}^{(j),\top}\widehat{\mathbf{B}}^{\mathrm{Fou}}\left(\mathbf{m}^{(j)}\right)\,\mathbf{s}^{(j)}}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | 𝐬(j):=𝐦(j+1)−𝐦(j),𝐲(j):=λ(j+1)​g^∇Fou​(𝐦(j+1))−λ(j)​g^∇Fou​(𝐦(j)).\mathbf{s}^{(j)}:=\mathbf{m}^{(j+1)}-\mathbf{m}^{(j)},\qquad\mathbf{y}^{(j)}:=\lambda^{(j+1)}\widehat{g}^{\mathrm{Fou}}\_{\nabla}\!\left(\mathbf{m}^{(j+1)}\right)-\lambda^{(j)}\widehat{g}^{\mathrm{Fou}}\_{\nabla}\!\left(\mathbf{m}^{(j)}\right). |  |

## 3 Fourier Representations of the MSRM Problem

In this section we derive Fourier-domain representations of the MSRM objective, its gradient, and its Hessian along the allocation trajectory. Our approach extends the framework of [[18](https://arxiv.org/html/2602.06424v1#bib.bib85 "A Fourier Approach to the Computation of CV@R and Optimized Certainty Equivalents")] to the multivariate setting. Although the Fourier methodology in [[7](https://arxiv.org/html/2602.06424v1#bib.bib71 "Optimal Damping with Hierarchical Adaptive Quadrature for Efficient Fourier Pricing of Multi-Asset Options in Lévy Models"), [4](https://arxiv.org/html/2602.06424v1#bib.bib72 "Quasi-Monte Carlo with Domain Transformation for Efficient Fourier Pricing of Multi-Asset Options")] was developed in option pricing, we adapt it here to risk measurement. We first introduce the required notation and integrability assumptions, and then obtain a unified Fourier representation in Corollary [3.4](https://arxiv.org/html/2602.06424v1#S3.Thmtheorem4 "Corollary 3.4 (Fourier representations for MSRM problem). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

###### Notation 3.1.

* •

  For 𝐲∈ℂd\mathbf{y}\in\mathbb{C}^{d}, Φ𝐗​(𝐲):=𝔼​[ei​⟨𝐲,𝐗⟩],\Phi\_{\mathbf{X}}(\mathbf{y}):=\mathbb{E}\left[e^{\mathrm{i}\langle\mathbf{y},\mathbf{X}\rangle}\right], denotes the joint extended characteristic function (CF) of 𝐗\mathbf{X}. Here ⟨.,.⟩\langle.,.\rangle denotes the inner product on ℝd\mathbb{R}^{d} extended bi-linearly to ℂd\mathbb{C}^{d}, i.e., for 𝐰,𝐭∈ℂd,⟨𝐰,𝐭⟩=∑k=1dwk​tk\mathbf{w,t}\in\mathbb{C}^{d},\langle\mathbf{w},\mathbf{t}\rangle=\sum\_{k=1}^{d}w\_{k}t\_{k}
* •

  For 𝐲∈ℂd\mathbf{y}\in\mathbb{C}^{d}, the function f^​(𝐲):=∫ℝde−i​⟨𝐲,𝐱⟩​f​(𝐱)​d𝐱\widehat{f}(\mathbf{y}):=\int\_{\mathbb{R}^{d}}e^{-\mathrm{i}\,\langle\mathbf{y},\mathbf{x}\rangle}\,f(\mathbf{x})\,\mathrm{d}\mathbf{x} represents the (extended) Fourier transforms of the function ff.
* •

  The Fourier transform of ∇𝐱f\nabla\_{\mathbf{x}}f is taken componentwise, i.e.,
  f^∇𝐱​(𝐲)=(ℓ^∂x1​(𝐲),…,ℓ^∂xd​(𝐲))\widehat{f}\_{\nabla\_{\mathbf{x}}}(\mathbf{y})=\big(\widehat{\ell}\_{\partial\_{x\_{1}}}(\mathbf{y}),\dots,\widehat{\ell}\_{\partial\_{x\_{d}}}(\mathbf{y})\big).
  Similarly, the Fourier transform of ∇𝐱2f\nabla\_{\mathbf{x}}^{2}f is taken entrywise:
  f^∇𝐱2​(𝐲)=(f^∂xi​xj2​(𝐲))i,j=1d\widehat{f}\_{\nabla\_{\mathbf{x}}^{2}}(\mathbf{y})=\left(\widehat{f}\_{\partial^{2}\_{x\_{i}x\_{j}}}(\mathbf{y})\right)\_{i,j=1}^{d}.
* •

  i\mathrm{i} denotes the imaginary unit number, ℜ⁡[⋅]\Re[\cdot] and ℑ⁡[⋅]\Im[\cdot] are the real and imaginary parts of a complex number, respectively.
* •

  𝚯ℓ\boldsymbol{\Theta}\_{\ell} denotes the parameters of the loss function
  ℓ\ell.
* •

  For ν=0,1,2\nu=0,1,2, define ℓ(ν):=ℓ,∇ℓ,∇2ℓ\ell^{(\nu)}:=\ell,\,\nabla\ell,\,\nabla^{2}\ell, respectively, and let ℓ^(ν):=ℓ^,ℓ^∇,ℓ^∇2\widehat{\ell}^{(\nu)}:=\widehat{\ell},\,\widehat{\ell}\_{\nabla},\,\widehat{\ell}\_{\nabla^{2}} denote their corresponding Fourier transforms.
  Let δℓ(ν)\delta\_{\ell}^{(\nu)} denote the strip of analyticity of ℓ^(ν)\widehat{\ell}^{(\nu)}, i.e.,

  |  |  |  |
  | --- | --- | --- |
  |  | δℓ(ν):={𝐊(ν)∈ℝd∣𝐱↦e⟨𝐊(ν),𝐱⟩​ℓ(ν)​(𝐱)∈L1​(ℝd)}.\delta\_{\ell}^{(\nu)}:=\{\mathbf{K}^{(\nu)}\in\mathbb{R}^{d}\mid\mathbf{x}\mapsto e^{\langle\mathbf{K}^{(\nu)},\mathbf{x}\rangle}\ell^{(\nu)}(\mathbf{x})\in L^{1}(\mathbb{R}^{d})\}. |  |
* •

  δX:={𝐊∈ℝd:𝔼​[e⟨𝐊,𝐗⟩]<∞}\delta\_{X}:=\{\mathbf{K}\in\mathbb{R}^{d}:\mathbb{E}[e^{\langle\mathbf{K},\mathbf{X}\rangle}]<\infty\}.

###### Assumption 3.2 (Admissible contour shifts).

For each ν∈{0,1,2}\nu\in\{0,1,2\}, there exists 𝐊(ν)∈δX\mathbf{K}^{(\nu)}\in\delta\_{X} such that w⟼ΦX​(𝐰+i​𝐊(ν))​ℓ^(ν)​(𝐰+i​𝐊(ν))∈L1​(ℝd)w\longmapsto\Phi\_{X}(\mathbf{w}+\mathrm{i}\mathbf{K}^{(\nu)})\,\widehat{\ell}^{(\nu)}(\mathbf{w}+\mathrm{i}\mathbf{K}^{(\nu)})\in L^{1}(\mathbb{R}^{d}). We denote the corresponding admissible set by

|  |  |  |
| --- | --- | --- |
|  | δK(ν):={𝐊∈δX:ΦX(⋅+i𝐊)ℓ^(ν)(⋅+i𝐊)∈L1(ℝd)},\delta\_{K}^{(\nu)}:=\left\{\mathbf{K}\in\delta\_{X}:\ \Phi\_{X}(\cdot+\mathrm{i}\mathbf{K})\,\widehat{\ell}^{(\nu)}(\cdot+\mathrm{i}\mathbf{K})\in L^{1}(\mathbb{R}^{d})\right\}, |  |

and assume δK(ν)≠∅\delta\_{K}^{(\nu)}\neq\varnothing.

###### Remark 3.3.

By construction, δK(ν)⊆δX∩δℓ(ν)\delta\_{K}^{(\nu)}\subseteq\delta\_{X}\cap\delta\_{\ell}^{(\nu)}.

The corollary and its proof below are adapted for the MSRM problem, which is based on [[7](https://arxiv.org/html/2602.06424v1#bib.bib71 "Optimal Damping with Hierarchical Adaptive Quadrature for Efficient Fourier Pricing of Multi-Asset Options in Lévy Models"), Proposition 2.4].

###### Corollary 3.4 (Fourier representations for MSRM problem).

Suppose Assumption [3.2](https://arxiv.org/html/2602.06424v1#S3.Ex2 "Assumption 3.2 (Admissible contour shifts). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") holds. Then, for any choice of
𝐊(ν)∈δK(ν)\mathbf{K}^{(\nu)}\in\delta\_{K}^{(\nu)}, the Fourier-based representation for g​(𝐦)g(\mathbf{m}),
∇g​(𝐦)\nabla g(\mathbf{m}) and ∇2g​(𝐦)\nabla^{2}g(\mathbf{m}) in ([2.8](https://arxiv.org/html/2602.06424v1#S2.E8 "In 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"))-([2.9](https://arxiv.org/html/2602.06424v1#S2.E9 "In 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) are given in unified form by:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.1) |  | g^(ν),Fou​(𝐦)\displaystyle\widehat{g}^{(\nu),\mathrm{Fou}}(\mathbf{m}) | :=(2​π)−d​ℜ⁡[∫ℝde⟨𝐊(ν)−i​𝐰,𝐦⟩​Φ𝐗​(𝐰+i​𝐊(ν))​ℓ^(ν)​(𝐰+i​𝐊(ν))​d𝐰],ν=0,1,2.\displaystyle:=(2\pi)^{-d}\,\Re\!\left[\int\_{\mathbb{R}^{d}}e^{\langle\mathbf{K}^{(\nu)}-\mathrm{i}\mathbf{w},\,\mathbf{m}\rangle}\,\Phi\_{\mathbf{X}}\left(\mathbf{w}+\mathrm{i}\mathbf{K}^{(\nu)}\right)\,\widehat{\ell}^{(\nu)}\left(\mathbf{w}+\mathrm{i}\mathbf{K}^{(\nu)}\right)\,\mathrm{d}\mathbf{w}\right],\quad\nu=0,1,2. |  |

###### Proof.

The proof for Corollary [3.4](https://arxiv.org/html/2602.06424v1#S3.Thmtheorem4 "Corollary 3.4 (Fourier representations for MSRM problem). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") is presented in Appendix [E.1](https://arxiv.org/html/2602.06424v1#A5.SS1 "E.1 Proof for Corollary 3.4 ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
∎

In view of the Fourier representations ([3.1](https://arxiv.org/html/2602.06424v1#S3.E1 "In Corollary 3.4 (Fourier representations for MSRM problem). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), we introduce the aggregate integrands

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | h(ν)​(𝐰;𝐦,𝐊(ν),𝚯):=(2​π)−d​e⟨𝐊(ν)−i​𝐰,𝐦⟩​Φ𝐗​(𝐰+i​𝐊(ν))​ℓ^(ν)​(𝐰+i​𝐊(ν)),ν=0,1,2.\displaystyle h^{(\nu)}\left(\mathbf{w};\mathbf{m},\mathbf{K}^{(\nu)},\boldsymbol{\Theta}\right)=(2\pi)^{-d}e^{\langle\mathbf{K}^{(\nu)}-\mathrm{i}\mathbf{w},\,\mathbf{m}\rangle}\,\Phi\_{\mathbf{X}}\left(\mathbf{w}+\mathrm{i}\mathbf{K}^{(\nu)}\right)\,\widehat{\ell}^{(\nu)}\left(\mathbf{w}+\mathrm{i}\mathbf{K}^{(\nu)}\right),\quad\nu=0,1,2. |  |

for 𝐰∈ℝd\mathbf{w}\in\mathbb{R}^{d}, where 𝐊(ν)∈δK(ν)\mathbf{K}^{(\nu)}\in\delta\_{K}^{(\nu)}, and
𝚯:=(𝚯𝐗,𝚯ℓ)\boldsymbol{\Theta}:=(\boldsymbol{\Theta}\_{\mathbf{X}},\boldsymbol{\Theta}\_{\ell}).

Motivated by the structure of the multivariate loss functions in Example [2.1](https://arxiv.org/html/2602.06424v1#S2.E1 "In Example 2.3. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), which combine marginal terms with dependence components of finite interaction order qℓq\_{\ell}, we exploit this structure to decompose the aggregate Fourier integrands into componentwise contributions indexed by interaction order and coordinate subsets. This decomposition is not introduced for dimension adaptivity but rather as a fundamental tool for the construction of our numerical methods and their subsequent analysis, allowing expectations, gradients, and Hessians to be expressed as finite sums of lower-dimensional Fourier integrals. The decomposition is formalized in the following notation.

###### Notation 3.5 (Component selection and componentwise integrands).

Let qℓ∈ℕ,qℓ≤dq\_{\ell}\in\mathbb{N},q\_{\ell}\leq d denote the maximal interaction order appearing in the dependence structure of the loss function, ℓ\ell; for instance, qℓ=2q\_{\ell}=2 corresponds to pairwise interactions, qℓ=3q\_{\ell}=3 to triplet interactions, and so on. Let ℐqℓ⊂{1,…,qℓ}\mathcal{I}\_{q\_{\ell}}\subset\{1,\dots,q\_{\ell}\}. For each k∈ℐqℓk\in\mathcal{I}\_{q\_{\ell}}, let ℐk:={𝐩=(p1,…,pk):1≤p1<⋯<pk≤d}\mathcal{I}\_{k}:=\{\mathbf{p}=(p\_{1},\dots,p\_{k}):1\leq p\_{1}<\cdots<p\_{k}\leq d\} denote the collection of all kk-dimensional coordinate subsets. For each 𝐩∈ℐk\mathbf{p}\in\mathcal{I}\_{k}, let Pk,p∈ℝk×dP\_{k,p}\in\mathbb{R}^{k\times d} denote the corresponding coordinate selection matrix, whose rr-th row equals the canonical basis vector epr⊤e\_{p\_{r}}^{\top}, 444In particular, its entries are given by
(Pk,p)r​j={1,if ​j=pr,0,otherwise,r=1,…,k,j=1,…,d.(P\_{k,p})\_{rj}=\begin{cases}1,&\text{if }j=p\_{r},\\
0,&\text{otherwise},\end{cases}\quad r=1,\dots,k,\;j=1,\dots,d. and define the projected vectors

|  |  |  |
| --- | --- | --- |
|  | 𝐦k,p:=Pk,p​𝐦∈ℝk,𝐗k,p:=Pk,p​𝐗∈ℝk.\mathbf{m}\_{k,p}:=P\_{k,p}\;\mathbf{m}\in\mathbb{R}^{k},\qquad\mathbf{X}\_{k,p}:=P\_{k,p}\;\mathbf{X}\in\mathbb{R}^{k}. |  |

Then, for ν=0,1,2\nu=0,1,2, the Fourier-based componentwise integrands are defined by

|  |  |  |  |
| --- | --- | --- | --- |
| (3.3) |  | hk,p(ν)(𝐮;𝐦k,p,𝐊k,p(ν),,𝚯k,p):=(2π)−kexp(⟨𝐊k,p(ν)−i𝐮,𝐦k,p⟩)Φ𝐗k,p(𝐮+i𝐊k,p(ν))ℓ^k,p(ν)(𝐮+i𝐊k,p(ν)),𝐮∈ℝkh\_{k,p}^{(\nu)}\left(\mathbf{u};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},,\boldsymbol{\Theta}\_{k,p}\right):=(2\pi)^{-k}\exp\!\bigl(\langle\mathbf{K}\_{k,p}^{(\nu)}-\mathrm{i}\mathbf{u},\,\mathbf{m}\_{k,p}\rangle\bigr)\,\Phi\_{\mathbf{X}\_{k,p}}\left(\mathbf{u}+\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right)\,\widehat{\ell}^{(\nu)}\_{k,p}\left(\mathbf{u}+\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right),\quad\mathbf{u}\in\mathbb{R}^{k} |  |

where 𝚯k,p:=(𝚯𝐗k,p,𝚯ℓk,p)\boldsymbol{\Theta}\_{k,p}:=(\boldsymbol{\Theta}\_{\mathbf{X}\_{k,p}},\boldsymbol{\Theta}\_{\ell\_{k,p}}) collects the corresponding parameters for component (k,p)(k,p), and 𝐊k,p∈δKk,p(ν):=δXk,p(ν)∩δlk,p(ν)\mathbf{K}\_{k,p}\in\delta\_{K\_{k,p}}^{(\nu)}:=\delta\_{X\_{k,p}}^{(\nu)}\cap\delta\_{l\_{k,p}}^{(\nu)}.

The aggregated loss function, integrands in ([3.2](https://arxiv.org/html/2602.06424v1#S3.E2 "In 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) and integrals in ([3.1](https://arxiv.org/html/2602.06424v1#S3.E1 "In Corollary 3.4 (Fourier representations for MSRM problem). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) admit the following finite decomposition:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (3.4) |  | ℓ(0)\displaystyle\ell^{(0)} | =∑k∈ℐqℓ∑𝐩∈ℐkℓk,p(0),\displaystyle=\sum\_{k\in\mathcal{I}\_{q\_{\ell}}}\sum\_{\mathbf{p}\in\mathcal{I}\_{k}}\ell^{(0)}\_{k,p}, | h(0)\displaystyle h^{(0)} | =∑k∈ℐqℓ∑𝐩∈ℐkhk,p(0),\displaystyle=\sum\_{k\in\mathcal{I}\_{q\_{\ell}}}\sum\_{\mathbf{p}\in\mathcal{I}\_{k}}h^{(0)}\_{k,p}, | g(0),Fou\displaystyle g^{(0),\mathrm{Fou}} | =∑k∈ℐqℓ∑𝐩∈ℐkgk,p(0),Fou,\displaystyle=\sum\_{k\in\mathcal{I}\_{q\_{\ell}}}\sum\_{\mathbf{p}\in\mathcal{I}\_{k}}g^{(0),\mathrm{Fou}}\_{k,p}, |  |
|  | ℓ(1)\displaystyle\ell^{(1)} | =∑k∈ℐqℓ∑𝐩∈ℐkPk,p⊤​ℓk,p(1),\displaystyle=\sum\_{k\in\mathcal{I}\_{q\_{\ell}}}\sum\_{\mathbf{p}\in\mathcal{I}\_{k}}P\_{k,p}^{\top}\,\ell^{(1)}\_{k,p}, | h(1)\displaystyle h^{(1)} | =∑k∈ℐqℓ∑𝐩∈ℐkPk,p⊤​hk,p(1),\displaystyle=\sum\_{k\in\mathcal{I}\_{q\_{\ell}}}\sum\_{\mathbf{p}\in\mathcal{I}\_{k}}P\_{k,p}^{\top}\,h^{(1)}\_{k,p}, | g(1),Fou\displaystyle g^{(1),\mathrm{Fou}} | =∑k∈ℐqℓ∑𝐩∈ℐkPk,p⊤​gk,p(1),Fou,\displaystyle=\sum\_{k\in\mathcal{I}\_{q\_{\ell}}}\sum\_{\mathbf{p}\in\mathcal{I}\_{k}}P\_{k,p}^{\top}\,g^{(1),\mathrm{Fou}}\_{k,p}, |  |
|  | ℓ(2)\displaystyle\ell^{(2)} | =∑k∈ℐqℓ∑𝐩∈ℐkPk,p⊤​ℓk,p(2)​Pk,p,\displaystyle=\sum\_{k\in\mathcal{I}\_{q\_{\ell}}}\sum\_{\mathbf{p}\in\mathcal{I}\_{k}}P\_{k,p}^{\top}\,\ell^{(2)}\_{k,p}\,P\_{k,p}, | h(2)\displaystyle h^{(2)} | =∑k∈ℐqℓ∑𝐩∈ℐkPk,p⊤​hk,p(2)​Pk,p,\displaystyle=\sum\_{k\in\mathcal{I}\_{q\_{\ell}}}\sum\_{\mathbf{p}\in\mathcal{I}\_{k}}P\_{k,p}^{\top}\,h^{(2)}\_{k,p}\,P\_{k,p}, | g(2),Fou\displaystyle g^{(2),\mathrm{Fou}} | =∑k∈ℐqℓ∑𝐩∈ℐkPk,p⊤​gk,p(2),Fou​Pk,p.\displaystyle=\sum\_{k\in\mathcal{I}\_{q\_{\ell}}}\sum\_{\mathbf{p}\in\mathcal{I}\_{k}}P\_{k,p}^{\top}\,g^{(2),\mathrm{Fou}}\_{k,p}\,P\_{k,p}. |  |

The decomposition in Notation [3.5](https://arxiv.org/html/2602.06424v1#S3.Thmtheorem5 "Notation 3.5 (Component selection and componentwise integrands). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") makes explicit that, under finite interaction order qℓq\_{\ell}, the Fourier representations of the MSRM objective, its gradient, and its Hessian can be written as finite sums of lower-dimensional Fourier integrals, each involving at most k≤qℓk\leq q\_{\ell} coordinates. This representation will be exploited in the subsequent sections to construct numerical schemes whose complexity is governed by the interaction order rather than the full dimension dd of the loss vector.

###### Remark 3.6.

For the choice of loss functions in Example [2.1](https://arxiv.org/html/2602.06424v1#S2.E1 "In Example 2.3. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), we restrict attention to the admissible dimension set ℐqℓ={1,qℓ}\mathcal{I}\_{q\_{\ell}}=\{1,q\_{\ell}\}, where qℓ=2q\_{\ell}=2 for ([2.2](https://arxiv.org/html/2602.06424v1#S2.E2 "In item (i) ‣ Example 2.3. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) and qℓ=dq\_{\ell}=d for ([2.3](https://arxiv.org/html/2602.06424v1#S2.E3 "In item (ii) ‣ Example 2.3. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

For the loss functions in Example [2.1](https://arxiv.org/html/2602.06424v1#S2.E1 "In Example 2.3. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), the componentwise Fourier transforms (see Appendix [E.2](https://arxiv.org/html/2602.06424v1#A5.SS2 "E.2 Fourier transform of the given loss functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) and their strips of analyticity, δℓk,p(ν)\delta\_{\ell\_{k,p}}^{(\nu)}, can be characterized explicitly (see Table [3.1](https://arxiv.org/html/2602.06424v1#S3.T1 "Table 3.1 ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). Moreover, for the loss families in Example [2.1](https://arxiv.org/html/2602.06424v1#S2.E1 "In Example 2.3. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") the admissible damping domains for ℓ,∇ℓ\ell,\nabla\ell, and ∇2ℓ\nabla^{2}\ell coincide; hence we use a single domain for all ν∈{0,1,2}\nu\in\{0,1,2\}. For loss components whose Fourier representations rely on a domain decomposition, admissible damping parameters are characterized componentwise on the corresponding one-sided domains. In particular, for the exponential loss this leads naturally to admissible pairs (Kk,p−,Kk,p+)(K^{-}\_{k,p},K^{+}\_{k,p}), as summarized in Table [3.1](https://arxiv.org/html/2602.06424v1#S3.T1 "Table 3.1 ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

|  |  |
| --- | --- |
| Loss function | δℓk,p(ν),ν=0,1,2\delta\_{\ell\_{k,p}}^{(\nu)},{\nu={0,1,2}} |
| Exponential | {(Kk,p−,Kk,p+)∈ℝk×ℝk|Kk,p−<β<Kk,p+,𝐩∈ℐk,k∈ℐqℓ}\left\{\left(K^{-}\_{k,p},\,K^{+}\_{k,p}\right)\in\mathbb{R}^{k}\times\mathbb{R}^{k}\;\middle|\;K^{-}\_{k,p}<\beta<K^{+}\_{k,p},\quad\mathbf{p}\in\mathcal{I}\_{k},\;k\in\mathcal{I}\_{q\_{\ell}}\right\} |
| QPC | {𝐊k,p∈ℝk:𝐊k,p<0,𝐩∈ℐk,k∈ℐqℓ}\left\{\mathbf{K}\_{k,p}\in\mathbb{R}^{k}:\mathbf{K}\_{k,p}<0,\;\mathbf{p}\in\mathcal{I}\_{k},\;k\in\mathcal{I}\_{q\_{\ell}}\right\} |

Table 3.1: Strips of analyticity for ℓ^k,p(ν)\widehat{\ell}\_{k,p}^{(\nu)}.

For the loss vector 𝐗\mathbf{X}, we focus on continuous distributional families admitting closed-form extended characteristic functions, namely Gaussian and Normal Inverse Gaussian (NIG). Appendix [E.3](https://arxiv.org/html/2602.06424v1#A5.SS3 "E.3 Loss vector distributions and extended characteristic functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") provides the corresponding parameterizations and extended characteristic functions of the marginals 𝐗k,p\mathbf{X}\_{k,p}, while Table [3.2](https://arxiv.org/html/2602.06424v1#S3.T2 "Table 3.2 ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") summarizes the associated analyticity domains δXk,p{\delta\_{X\_{k,p}}}.

|  |  |
| --- | --- |
| Distribution | δXk,p{\delta\_{X\_{k,p}}} |
| Gaussian | {𝐊k,p∈ℝk,𝐩∈ℐk,k∈ℐqℓ}\{\,{\mathbf{K}\_{k,p}}\in\mathbb{R}^{k},\ \mathbf{p}\in\mathcal{I}\_{k},\ k\in\mathcal{I}\_{q\_{\ell}}\,\} |
| NIG | {𝐊k,p∈ℝk,(αk,p2−⟨(𝜷k,p−𝐊k,p),𝚪k,p​(𝜷k,p−𝐊k,p)⟩)>0,𝐩∈ℐk,k∈ℐqℓ}\left\{{\mathbf{K}\_{k,p}}\in\mathbb{R}^{k},\ \left(\alpha\_{k,p}^{2}-\langle(\boldsymbol{\beta}\_{k,p}-\mathbf{K}\_{k,p}),\ \boldsymbol{\Gamma}\_{k,p}(\boldsymbol{\beta}\_{k,p}-\mathbf{K}\_{k,p})\rangle\right)>0,\ \mathbf{p}\in\mathcal{I}\_{k},\ k\in\mathcal{I}\_{q\_{\ell}}\,\right\} |

Table 3.2: Strip of analyticity for the extended CF 𝚽𝐗k,p\boldsymbol{\Phi}\_{\mathbf{X}\_{k,p}}.

The choice of damping parameters 𝐊k,p(ν)\mathbf{K}\_{k,p}^{(\nu)} is crucial to control the integrability and smoothness of component integrands. As shown in Figure [3.1](https://arxiv.org/html/2602.06424v1#S3.F1 "Figure 3.1 ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), an inappropriate choice of 𝐊k,p(ν)\mathbf{K}\_{k,p}^{(\nu)} can produce ill-behaved integrands and might destabilize the numerical optimization procedure in Algorithm [1](https://arxiv.org/html/2602.06424v1#alg1 "Algorithm 1 ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). We therefore select 𝐊k,p(ν)\mathbf{K}\_{k,p}^{(\nu)} using the optimal damping rule developed in Section [3.1](https://arxiv.org/html/2602.06424v1#S3.SS1 "3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

![Refer to caption](x1.png)


(a) 𝐊1,1(0)=0.5{\mathbf{K}\_{1,1}^{(0)}}=0.5

![Refer to caption](x2.png)


(b) 𝐊1,1(0)=2.5{\mathbf{K}\_{1,1}^{(0)}}=2.5

Figure 3.1: Effect of the damping parameter 𝐊1,1(0){\mathbf{K}\_{1,1}^{(0)}} on the QPC loss integrand component h1,1(0)h^{(0)}\_{1,1} for a 1010-dimensional Gaussian loss vector (Example in Section [6.2](https://arxiv.org/html/2602.06424v1#S6.SS2 "6.2 QPC Loss with Ten-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

### 3.1 Optimal Damping Rule

We adopt the optimal damping rule from [[7](https://arxiv.org/html/2602.06424v1#bib.bib71 "Optimal Damping with Hierarchical Adaptive Quadrature for Efficient Fourier Pricing of Multi-Asset Options in Lévy Models")], which is originally developed in an option-pricing context, and extend it to the MSRM setting. Specifically, we select damping vectors 𝐊k,p(ν)\mathbf{K}\_{k,p}^{(\nu)} and update them along the optimization trajectory. From this section onward, the index (ν)(\nu) is understood to take values ν=0,1\nu=0,1, unless stated otherwise.

Corollary [3.7](https://arxiv.org/html/2602.06424v1#S3.Thmtheorem7 "Corollary 3.7 (Damping Rule). ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") provides the derivation of the optimal damping rule for the component (k,p)(k,p).

###### Corollary 3.7 (Damping Rule).

For component integrands hk,p(ν)h\_{k,p}^{(\nu)} defined in ([3.3](https://arxiv.org/html/2602.06424v1#S3.E3 "In Notation 3.5 (Component selection and componentwise integrands). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) with 𝐊k,p(ν)∈δKk,p(ν)\mathbf{K}\_{k,p}^{(\nu)}\in\delta\_{K\_{k,p}}^{(\nu)}, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.5) |  | 𝐊k,p(ν),∗​(𝐦k,p,𝚯k,p)\displaystyle\mathbf{K}^{(\nu),\*}\_{k,p}\left(\mathbf{m}\_{k,p},\boldsymbol{\Theta}\_{k,p}\right) | :=arg​min𝐊k,p(ν)∈δKk,p(ν)​sup𝐮∈ℝk|hk,p(ν)​(𝐮;𝐦k,p,𝐊k,p(ν),𝚯k,p)|\displaystyle=\operatorname\*{arg\,min}\_{\mathbf{K}\_{k,p}^{(\nu)}\in\delta\_{K\_{k,p}}^{(\nu)}}\sup\_{\mathbf{u}\in\mathbb{R}^{k}}\,\Big|h\_{k,p}^{(\nu)}\big(\mathbf{u};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}\big)\Big| |  |
|  |  | =arg​min𝐊k,p(ν)∈δKk,p(ν)⁡|hk,p(ν)​(𝟎ℝk;𝐦k,p,𝐊k,p(ν),𝚯k,p)|\displaystyle=\operatorname\*{arg\,min}\_{\mathbf{K}\_{k,p}^{(\nu)}\in\delta\_{K\_{k,p}}^{(\nu)}}\Big|h\_{k,p}^{(\nu)}\big(\mathbf{0}\_{\mathbb{R}^{k}};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}\big)\Big| |  |
|  |  | =arg​min𝐊k,p(ν)∈δKk,p(ν)⁡υk,p(ν)​(𝐦k,p,𝐊k,p(ν),𝚯k,p),\displaystyle=\operatorname\*{arg\,min}\_{\mathbf{K}\_{k,p}^{(\nu)}\in\delta\_{K\_{k,p}}^{(\nu)}}\upsilon\_{k,p}^{(\nu)}\!\left(\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}\right), |  |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.6) |  | υk,p(ν)​(𝐦k,p,𝐊k,p(ν),𝚯k,p)\displaystyle\upsilon\_{k,p}^{(\nu)}\!\left(\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}\right) | :=ln⁡|hk,p(ν)​(𝟎ℝk;𝐦k,p,𝐊k,p(ν),𝚯k,p)|\displaystyle=\ln\Big|h\_{k,p}^{(\nu)}\big(\mathbf{0}\_{\mathbb{R}^{k}};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}\big)\Big| |  |
|  |  | =−k​ln⁡(2​π)+⟨𝐊k,p(ν),𝐦k,p⟩+ln⁡|𝚽𝐗k,p​(i​𝐊k,p(ν))|+ln⁡|ℓ^k,p(ν)​(i​𝐊k,p(ν))|.\displaystyle=-k\ln(2\pi)+\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{m}\_{k,p}\rangle+\ln\Big|\mathbf{\Phi}\_{\mathbf{X}\_{k,p}}\!\big(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\big)\Big|+\ln\Big|\widehat{\ell}\_{k,p}^{(\nu)}\!\big(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\big)\Big|. |  |

###### Proof.

Appendix [B.1.1](https://arxiv.org/html/2602.06424v1#A2.SS1.SSS1 "B.1.1 Proof for Corollary 3.7 ‣ B.1 Damping rule and convexity properties ‣ Appendix B Supplementary results for Section 3.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") presents the proof.
∎

We need to solve ([3.5](https://arxiv.org/html/2602.06424v1#S3.E5 "In Corollary 3.7 (Damping Rule). ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) numerically, since it is generally not available in closed form. For numerical convenience, we apply a logarithmic transformation to the minimization problem in ([3.5](https://arxiv.org/html/2602.06424v1#S3.E5 "In Corollary 3.7 (Damping Rule). ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). Moreover, by Proposition [B.1](https://arxiv.org/html/2602.06424v1#A2.Thmtheorem1 "Proposition B.1. ‣ B.1.2 On the Convexity of 𝜐_{𝑘,𝑝}^(𝜈) in in (3.6) ‣ B.1 Damping rule and convexity properties ‣ Appendix B Supplementary results for Section 3.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") and Remark [B.2](https://arxiv.org/html/2602.06424v1#A2.Thmtheorem2 "Remark B.2. ‣ B.1.2 On the Convexity of 𝜐_{𝑘,𝑝}^(𝜈) in in (3.6) ‣ B.1 Damping rule and convexity properties ‣ Appendix B Supplementary results for Section 3.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), this log-transformed objective is strictly convex or even strongly convex in 𝐊k,p(ν)\mathbf{K}\_{k,p}^{(\nu)}, so standard numerical optimization routines typically converge quickly to the minimizer.

In most cases, ([3.5](https://arxiv.org/html/2602.06424v1#S3.E5 "In Corollary 3.7 (Damping Rule). ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) can be solved efficiently along the optimization trajectory to obtain 𝐊k,p(ν),∗\mathbf{K}\_{k,p}^{(\nu),\*} with given 𝐦k,p\mathbf{m}\_{k,p}. A potential issue arises, because 𝐦k,p\mathbf{m}\_{k,p} enters νk,p(ν)\nu\_{k,p}^{(\nu)} linearly (through the term ⟨𝐊k,p(ν),𝐦k,p⟩\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{m}\_{k,p}\rangle); as a result, the minimizer 𝐊k,p(ν),∗​(𝐦k,p){\mathbf{K}\_{k,p}^{(\nu),\*}}\left(\mathbf{m}\_{k,p}\right) might approach the boundary of the analyticity strip δKk,p(ν)\delta\_{K\_{k,p}}^{(\nu)} for certain iterates 𝐦k,p\mathbf{m}\_{k,p}. In this case, minimizing υk,p(ν)\upsilon\_{k,p}^{(\nu)} can drive 𝐊k,p(ν)\mathbf{K}\_{k,p}^{(\nu)} toward the boundary of δKk,p(ν)\delta\_{K\_{k,p}}^{(\nu)}, potentially yielding component integrands that are numerically unstable.

![Refer to caption](x3.png)


(a) v1,2(0)v\_{1,2}^{(0)} with 𝐦1,2=−0.8\mathbf{m}\_{1,2}=-0.8, varying damping 𝐊1,2(0)\mathbf{K}\_{1,2}^{(0)}.

![Refer to caption](x4.png)


(b) Integrand h1,2(0)h\_{1,2}^{(0)} at 𝐦1,2=−0.8\mathbf{m}\_{1,2}=-0.8, 𝐊1,2(0)≈200\mathbf{K}\_{1,2}^{(0)}\approx 200, varying 𝐮\mathbf{u}.

Figure 3.2: Unregularized optimal damping selection for the QPC loss with a 33-dimensional NIG loss vector (Example in Section [6.3](https://arxiv.org/html/2602.06424v1#S6.SS3 "6.3 QPC Loss with Three-Dimensional NIG Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

For illustration, as shown in Figure [2(a)](https://arxiv.org/html/2602.06424v1#S3.F2.sf1 "In Figure 3.2 ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), the minimizer of υ1,2(0)\upsilon\_{1,2}^{(0)} is attained close to the boundary of the analyticity strip, at approximately 𝐊1,2(0)≈200\mathbf{K}\_{1,2}^{(0)}\approx 200. Using this value in h1,2(0)h\_{1,2}^{(0)}, Figure [2(b)](https://arxiv.org/html/2602.06424v1#S3.F2.sf2 "In Figure 3.2 ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") shows that the resulting function becomes highly oscillatory in 𝐮\mathbf{u} and attains very large magnitudes. One way to alleviate this problem is to establish the anisotropic Tikhonov-regularization for ([3.5](https://arxiv.org/html/2602.06424v1#S3.E5 "In Corollary 3.7 (Damping Rule). ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) (see Appendix [B.2](https://arxiv.org/html/2602.06424v1#A2.SS2 "B.2 Regularized damping ‣ Appendix B Supplementary results for Section 3.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") for more details), which yields to solving the following problem for the optimal damping parameters

|  |  |  |  |
| --- | --- | --- | --- |
| (3.7) |  | min𝐊k,p(ν)⁡υ​(𝐦k,p,𝐊k,p(ν),𝚯k,p)+λk,p2​‖𝐊k,p(ν)‖𝑾k,p2s.t.𝐊k,p(ν)∈δKk,p(ν).\min\_{\mathbf{K}\_{k,p}^{(\nu)}}\;\upsilon\left(\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}\right)+\tfrac{\lambda\_{k,p}}{2}\|\mathbf{K}\_{k,p}^{(\nu)}\|\_{\boldsymbol{W}\_{k,p}}^{2}\quad\text{s.t.}\quad\mathbf{K}\_{k,p}^{(\nu)}\in\delta\_{K\_{k,p}}^{(\nu)}. |  |

where 𝑾k,p≻0\boldsymbol{W}\_{k,p}\succ 0 is a weighting matrix, and λk,p>0\lambda\_{k,p}>0 is a regularization parameter controlling the strength of the penalty.

![Refer to caption](x5.png)


(a) v1,2(0)v\_{1,2}^{(0)} with 𝐦1,2=−0.8\mathbf{m}\_{1,2}=-0.8, varying damping 𝐊1,2(0)\mathbf{K}\_{1,2}^{(0)}.

![Refer to caption](x6.png)


(b) Integrand h1,2(0)h\_{1,2}^{(0)} at 𝐦1,2=−0.8\mathbf{m}\_{1,2}=-0.8, 𝐊1,2(0)≈5\mathbf{K}\_{1,2}^{(0)}\approx 5, varying 𝐮\mathbf{u}.

Figure 3.3: Regularized damping selection for the QPC loss with a 33-dimensional NIG loss vector (parameter setting in Section [6.3](https://arxiv.org/html/2602.06424v1#S6.SS3 "6.3 QPC Loss with Three-Dimensional NIG Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), using the anisotropic weighting matrix 𝑾1,2\boldsymbol{W}\_{1,2}.
Compared to Figure [3.2](https://arxiv.org/html/2602.06424v1#S3.F2 "Figure 3.2 ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), regularization shifts the optimal damping away from the boundary of the analyticity strip, yielding a smoother and better-conditioned integrand h1,2(0)h^{(0)}\_{1,2}.

With the inclusion of the anisotropic term 𝑾1,2\boldsymbol{W}\_{1,2}, the minimizer of υ1,2(0)\upsilon\_{1,2}^{(0)} is attained at
𝐊1,2(0)≈5\mathbf{K}\_{1,2}^{(0)}\approx 5. In this case, the resulting integrand exhibits a much more favorable shape compared to the scenario where only the peak 𝐮=0\mathbf{u}=0 is minimized.

Having determined the optimal choice of 𝐊k,p(ν)\mathbf{K}\_{k,p}^{(\nu)}, we can next set up the suitable numerical scheme to compute hk,p(ν){h}\_{k,p}^{(\nu)} in Section [4](https://arxiv.org/html/2602.06424v1#S4 "4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). We summarize the main idea in Algorithm [2](https://arxiv.org/html/2602.06424v1#alg2 "Algorithm 2 ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") for computing the optimal damping vector 𝐊k,p(ν),\mathbf{K}\_{k,p}^{(\nu)}, for the component integrands along the optimization trajectory.

###### Remark 3.8 (Choosing λk,p\lambda\_{k,p}).

In our numerical experiments, we observe boundary-hugging behavior (Figure [2(a)](https://arxiv.org/html/2602.06424v1#S3.F2.sf1 "In Figure 3.2 ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) for the NIG loss vector 𝐗\mathbf{X}.
Accordingly, in the Gaussian case we set λk,p=0\lambda\_{k,p}=0.
In contrast, for the NIG case, we set a positive penalty and choose λk,p∈[0.1,0.5]\lambda\_{k,p}\in[0.1,0.5] to ensure that the optimizer 𝐊k,p(ν)\mathbf{K}\_{k,p}^{(\nu)} remains in a reasonable interior region.

Algorithm 2  Selecting optimal damping vectors at each optimization step jj

1:components hk,p(ν)h\_{k,p}^{(\nu)} in ([3.3](https://arxiv.org/html/2602.06424v1#S3.E3 "In Notation 3.5 (Component selection and componentwise integrands). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), allocation 𝐦k,p(j)\mathbf{m}\_{k,p}^{(j)}, marginal distribution 𝐗k,p\mathbf{X}\_{k,p} of 𝐗\mathbf{X} .

2:Find 𝐊k,p(ν,j)\mathbf{K}\_{k,p}^{(\nu,j)} by solving the optimization problem ([3.7](https://arxiv.org/html/2602.06424v1#S3.E7 "In 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"))
for hk,p(ν)h\_{k,p}^{(\nu)}. The choice of the regularization parameter λk,p\lambda\_{k,p} follows Remark [3.8](https://arxiv.org/html/2602.06424v1#S3.Thmtheorem8 "Remark 3.8 (Choosing 𝜆_{𝑘,𝑝}). ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). The resulting problem can be efficiently solved using a numerical optimizer (e.g., SLSQP or trust-constr).

## 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals

Building on the Fourier representations derived in Section [3](https://arxiv.org/html/2602.06424v1#S3 "3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), we now approximate the resulting Fourier integrals numerically. These integrals can be moderately high-dimensional and must be evaluated repeatedly along the iterates of the constrained optimization algorithm. We therefore use (R)QMC methods, which are computationally efficient, provide practical error quantification, and perform well in moderate dimensions. Section [4.1](https://arxiv.org/html/2602.06424v1#S4.SS1 "4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") introduces a single-level Fourier–RQMC estimator with a suitable domain transformation, and Section [4.2](https://arxiv.org/html/2602.06424v1#S4.SS2 "4.2 Iteration-Indexed Multilevel Fourier–RQMC Approximation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") develops a multilevel extension that exploits the geometric convergence of the deterministic optimizer. The resulting estimators are subsequently employed as deterministic surrogate models for objective and gradient evaluations within the constrained optimization algorithm [1](https://arxiv.org/html/2602.06424v1#alg1 "Algorithm 1 ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

### 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation

We begin by constructing a single-level RQMC estimator for the Fourier-based integrals derived in Section [3](https://arxiv.org/html/2602.06424v1#S3 "3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). This requires mapping the Fourier integration domain ℝk\mathbb{R}^{k} to the unit cube [0,1]k[0,1]^{k} and applying an RQMC rule with tractable error estimation.

The component integrands hk,p(ν)h\_{k,p}^{(\nu)} in ([3.3](https://arxiv.org/html/2602.06424v1#S3.E3 "In Notation 3.5 (Component selection and componentwise integrands). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) are defined on ℝk\mathbb{R}^{k}, 1≤k≤q≤d1\leq k\leq q\leq d. To apply (R)QMC methods, we perform a change of variables 𝐯=G​(𝐮)\mathbf{v}=G(\mathbf{u}) mapping ℝk\mathbb{R}^{k} to the unit cube [0,1]k[0,1]^{k}. The transformation GG is drawn from a fixed, distribution-driven family whose functional form is independent of (k,p)(k,p), while its dimension is determined by kk and its parameters may depend on (k,p)(k,p) (see Section [4.1.1](https://arxiv.org/html/2602.06424v1#S4.SS1.SSS1 "4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") for details). The resulting transformed integrands are given by

|  |  |  |  |
| --- | --- | --- | --- |
| (4.1) |  | h~k,p(ν)​(𝐯;⋅):=hk,p(ν)​(𝐮;⋅)​|detJG−1​(𝐯;⋅)|\widetilde{h}\_{k,p}^{(\nu)}\left(\mathbf{v};\cdot\right):=h\_{k,p}^{(\nu)}\left(\mathbf{u};\cdot\right)\,\bigl|\det J\_{G^{-1}}(\mathbf{v};\cdot)\bigr| |  |

Here JG−1​(𝐯;⋅)J\_{G^{-1}}(\mathbf{v};\cdot) denotes the Jacobian matrix of the inverse transformation G−1G^{-1} w.r.t. 𝐯\mathbf{v}. We assume that GG is invertible almost everywhere with an almost-everywhere differentiable inverse.

The QMC estimator for the integral of transform component integrands h~k,p(ν):[0,1]k→ℝ\widetilde{h}\_{k,p}^{(\nu)}:[0,1]^{k}\to\mathbb{R} is an NN-point equal-weight quadrature rule, denoted by
INQMCI\_{N}^{\mathrm{QMC}}, defined as

|  |  |  |  |
| --- | --- | --- | --- |
| (4.2) |  | g^k,p(ν),Fou​(𝐦k,p)=∫[0,1]kh~k,p(ν)​(𝐯;𝐦k,p)​d𝐯≈INQMC​[h~k,p(ν)​(⋅;𝐦k,p)]:=1N​∑n=1Nh~k,p(ν)​(𝐯n;𝐦k,p),\widehat{g}^{(\nu),\mathrm{Fou}}\_{k,p}\left(\mathbf{m}\_{k,p}\right)\;=\;\int\_{[0,1]^{k}}\widetilde{h}\_{k,p}^{(\nu)}\left(\mathbf{v};\mathbf{m}\_{k,p}\right)\,\mathrm{d}\mathbf{v}\;\approx\;I\_{N}^{\mathrm{QMC}}\left[\widetilde{h}\_{k,p}^{(\nu)}\left(\cdot;\mathbf{m}\_{k,p}\right)\right]:=\frac{1}{N}\sum\_{n=1}^{N}\widetilde{h}\_{k,p}^{(\nu)}\left(\mathbf{v}\_{n};\mathbf{m}\_{k,p}\right), |  |

where {𝐯n}n=1N⊂[0,1]k\{\mathbf{v}\_{n}\}\_{n=1}^{N}\subset[0,1]^{k} is a deterministic low-discrepancy
sequence (e.g., Halton, Faure, Sobol; see [[16](https://arxiv.org/html/2602.06424v1#bib.bib33 "High-dimensional integration: The quasi-Monte Carlo way")] for details). The advantage of the QMC estimator in ([4.2](https://arxiv.org/html/2602.06424v1#S4.E2 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) over standard MC lies in the more uniform coverage of the unit cube [0,1]k[0,1]^{k} provided by low-discrepancy sequences, which often leads to improved convergence in practice. However, since the quadrature points are deterministic and exhibit strong dependence, the classical i.i.d. central limit theorem (CLT) does not apply directly, and probabilistic error bounds are not immediately available. Instead, convergence of deterministic QMC estimators is typically analyzed via discrepancy-based bounds, most notably the Koksma–Hlawka inequality [[27](https://arxiv.org/html/2602.06424v1#bib.bib92 "Funktionen von beschränkter Variatiou in der Theorie der Gleichverteilung")]. To evaluate this error bound, we need to compute the integral involving the first mixed partial derivatives of h~k,p(ν)\widetilde{h}\_{k,p}^{(\nu)}, which is often more difficult than evaluating the original integrand h~k,p(ν)\widetilde{h}\_{k,p}^{(\nu)} itself. To recover probabilistic error quantification while retaining the favorable space-filling properties of QMC, we employ a randomized version of the estimator in ([4.2](https://arxiv.org/html/2602.06424v1#S4.E2 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), referred to as the RQMC estimator [[46](https://arxiv.org/html/2602.06424v1#bib.bib65 "Practical Quasi-Monte Carlo Integration"), Chapter 17], which is expressed as

|  |  |  |  |
| --- | --- | --- | --- |
| (4.3) |  | IN,SshiftRQMC​[h~k,p(ν)​(⋅;𝐦k,p)]:=1Sshift​∑s=1Sshift1N​∑n=1Nh~k,p(ν)​(𝐯n(s);𝐦k,p),I^{\text{RQMC}}\_{N,S\_{\mathrm{shift}}}\left[\widetilde{h}\_{k,p}^{(\nu)}\left(\cdot;\mathbf{m}\_{k,p}\right)\right]:=\frac{1}{S\_{\text{shift}}}\sum\_{s=1}^{S\_{\text{shift}}}\frac{1}{N}\sum\_{n=1}^{N}\widetilde{h}\_{k,p}^{(\nu)}\left(\mathbf{v}\_{n}^{(s)};\mathbf{m}\_{k,p}\right), |  |

where {𝐯n(s)}s=1Sshift\left\{\mathbf{v}\_{n}^{(s)}\right\}\_{s=1}^{S\_{\mathrm{shift}}} is obtained by applying independent digital shifts to the underlying deterministic digital net {vn}n=1N⊂[0,1]k\{v\_{n}\}\_{n=1}^{N}\subset[0,1]^{k}, while preserving the low-discrepancy structure. Various randomization schemes exist, each with different theoretical guarantees (see, e.g., [[46](https://arxiv.org/html/2602.06424v1#bib.bib65 "Practical Quasi-Monte Carlo Integration"), Chapter 17]). In this work, we employ Sobol sequences [[52](https://arxiv.org/html/2602.06424v1#bib.bib67 "Construction and Comparison of High-Dimensional Sobol’ Generators")] with *digital shifting* [[15](https://arxiv.org/html/2602.06424v1#bib.bib66 "Randomization of Number Theoretic Methods for Multiple Integration")] as our randomization method. In order for this randomization to yield a valid RQMC estimator, we need the following assumption

###### Assumption 4.1 (Square-integrability of transformed integrands).

For each (k,p)(k,p) and for the selected damping vectors 𝐊k,p(ν)\mathbf{K}\_{k,p}^{(\nu)} along the optimization iterates, the transformed integrands
h~k,p(ν)\widetilde{h}\_{k,p}^{(\nu)}
belong to L2​([0,1]k)L^{2}\!\left([0,1]^{k}\right), with ν=0,1,2\nu=0,1,2.

Under Assumption [4.1](https://arxiv.org/html/2602.06424v1#S4.Thmtheorem1 "Assumption 4.1 (Square-integrability of transformed integrands). ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") and using independent digital shifts, the RQMC estimator ([4.3](https://arxiv.org/html/2602.06424v1#S4.E3 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) is unbiased, i.e.,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[IN,SshiftRQMC​[h~k,p(ν)​(⋅;𝐦k,p)]]=g^k,p(ν),Fou​(𝐦k,p),\mathbb{E}\!\left[I^{\mathrm{RQMC}}\_{N,S\_{\mathrm{shift}}}\left[\widetilde{h}\_{k,p}^{(\nu)}\left(\cdot;\mathbf{m}\_{k,p}\right)\right]\right]=\widehat{g}^{(\nu),\mathrm{Fou}}\_{k,p}\left(\mathbf{m}\_{k,p}\right), |  |

and enables us to derive the root mean squared error (RMSE) of the estimator:

|  |  |  |  |
| --- | --- | --- | --- |
| (4.4) |  | εN,SshiftRQMC​[h~k,p(ν)​(⋅;𝐦k,p)]=Cα​1Sshift​(Sshift−1)​∑s=1Sshift(1N​∑n=1Nh~k,p(ν)​(𝐯n(s);𝐦k,p)−IN,SshiftRQMC​[h~k,p(ν)​(⋅;𝐦k,p)])2\varepsilon\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\widetilde{h}\_{k,p}^{(\nu)}\left(\cdot;\mathbf{m}\_{k,p}\right)\right]=C\_{\alpha}\sqrt{\frac{1}{S\_{\mathrm{shift}}(S\_{\mathrm{shift}}-1)}\sum\_{s=1}^{S\_{\text{shift}}}\left(\frac{1}{N}\sum\_{n=1}^{N}\widetilde{h}\_{k,p}^{(\nu)}\left(\mathbf{v}\_{n}^{(s)};\mathbf{m}\_{k,p}\right)-I^{\text{RQMC}}\_{N,S\_{\mathrm{shift}}}\left[\widetilde{h}\_{k,p}^{(\nu)}\left(\cdot;\mathbf{m}\_{k,p}\right)\right]\right)^{2}} |  |

where CαC\_{\alpha} denotes the (1−α2)(1-\frac{\alpha}{2})-quantile of the standard normal distribution for a confidence level 0<α≪10<\alpha\ll 1.

Since the smoothness of the transformed integrands h~k,p(v)\widetilde{h}^{(v)}\_{k,p} near the boundary of [0,1]k[0,1]^{k} depends critically on the choice of the domain transformation GG, we adopt the boundary-singularity framework of [[45](https://arxiv.org/html/2602.06424v1#bib.bib121 "Halton Sequences Avoid the Origin")] to characterize the resulting convergence rate of the RQMC estimator in ([4.3](https://arxiv.org/html/2602.06424v1#S4.E3 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). Specifically, there exists C<∞C<\infty such that

|  |  |  |  |
| --- | --- | --- | --- |
| (4.5) |  | |∂𝜿h~k,p(ν)(𝐯)|≤C∏j=1kmin(vj,1−vj)−Aj,p(ν)−𝟏j∈𝜿,∀𝜿⊆{1,…,k},\bigl|\partial^{\boldsymbol{\kappa}}\widetilde{h}^{(\nu)}\_{k,p}(\mathbf{v})\bigr|\;\leq\;C\prod\_{j=1}^{k}\min(v\_{j},1-v\_{j})^{-A^{(\nu)}\_{j,p}-\mathbf{1}\_{j\in\boldsymbol{\kappa}}},\qquad\forall\,\boldsymbol{\kappa}\subseteq\{1,\dots,k\}, |  |

where ∂𝜿h~k,p(ν)​(𝐯):=∏j∈𝜿∂∂vj​h~k,p(ν)​(𝐯)\partial^{\boldsymbol{\kappa}}\widetilde{h}^{(\nu)}\_{k,p}(\mathbf{v})\;:=\;\prod\_{j\in\boldsymbol{\kappa}}\frac{\partial}{\partial v\_{j}}\,\widetilde{h}^{(\nu)}\_{k,p}(\mathbf{v}), and the exponents
Aj,p(ν)>0A^{(\nu)}\_{j,p}>0 quantify the boundary growth of the transformed integrands and its derivatives as
vj→0v\_{j}\to 0 or vj→1v\_{j}\to 1.
To obtain a single convergence exponent that is valid uniformly across all transformed integrands and will be used later in the statistical error analysis of Section [5.2](https://arxiv.org/html/2602.06424v1#S5.SS2 "5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), we define the worst-case boundary singularity exponent

|  |  |  |  |
| --- | --- | --- | --- |
| (4.6) |  | Asing∗:=maxν∈{0,1}⁡maxk∈ℐqℓ⁡max𝐩∈ℐk⁡max1≤j≤k⁡Aj,p(ν).A\_{\mathrm{sing}}^{\*}:=\max\_{\nu\in\{0,1\}}\max\_{k\in\mathcal{I}\_{q\_{\ell}}}\max\_{\mathbf{p}\in\mathcal{I}\_{k}}\max\_{1\leq j\leq k}A\_{j,p}^{(\nu)}. |  |

Then, for any ς>0\varsigma>0, [[45](https://arxiv.org/html/2602.06424v1#bib.bib121 "Halton Sequences Avoid the Origin"), Theorem 5.7] implies that the RQMC estimator

|  |  |  |  |
| --- | --- | --- | --- |
| (4.7) |  | εN,SshiftRQMC​[h~k,p(ν)​(⋅;𝐦k,p)]=𝒪​(N−r),\varepsilon\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\widetilde{h}\_{k,p}^{(\nu)}\left(\cdot;\mathbf{m}\_{k,p}\right)\right]=\mathcal{O}\!\left(N^{-r}\right), |  |

with r:=1−Asing∗−ςr:=1-A\_{\mathrm{sing}}^{\*}-\varsigma. Equation ([4.7](https://arxiv.org/html/2602.06424v1#S4.E7 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) shows that RQMC can outperform MC when Aj,p(ν)<12A\_{j,p}^{(\nu)}<\tfrac{1}{2}, although the convergence rate deteriorates as the boundary singularities become more severe. Moreover, [[38](https://arxiv.org/html/2602.06424v1#bib.bib64 "Randomized quasi-Monte Carlo and Owen’s boundary growth condition: a spectral analysis")] provides
a complementary spectral interpretation by linking the boundary-growth condition ([4.5](https://arxiv.org/html/2602.06424v1#S4.E5 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) to the decay of Fourier/Walsh coefficients. In particular,
larger exponents Aj,p(v)A^{(v)}\_{j,p} (and hence a larger Asing∗A^{\*}\_{\mathrm{sing}})
correspond to slower spectral decay and increased oscillatory behavior near
the boundary. This observation motivates designing a domain transformation GG so that the transformed integrands h~k,p(ν)\widetilde{h}\_{k,p}^{(\nu)} exhibit sufficiently mild boundary growth, as discussed in detail in Section [4.1.1](https://arxiv.org/html/2602.06424v1#S4.SS1.SSS1 "4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). We summarize the resulting single-level Fourier–RQMC procedure in Algorithm [3](https://arxiv.org/html/2602.06424v1#alg3 "Algorithm 3 ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

###### Remark 4.2.

In ([4.7](https://arxiv.org/html/2602.06424v1#S4.E7 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), the exponent rr satisfies r≤1r\leq 1 under the general boundary-growth assumptions adopted here. In more specific settings, higher (R)QMC rates may be attainable. For instance, when RQMC is combined with importance sampling, asymptotic rates of order 𝒪​(N−32+ς)\mathcal{O}\!\left(N^{-\frac{3}{2}+\varsigma}\right) have been reported [[41](https://arxiv.org/html/2602.06424v1#bib.bib6 "Achieving High Convergence Rates by Quasi-Monte Carlo and Importance Sampling for Unbounded Integrands")]. Moreover, suitably chosen domain transformations can substantially improve integrand regularity, which may translate into markedly better non-asymptotic error decay in practice [[4](https://arxiv.org/html/2602.06424v1#bib.bib72 "Quasi-Monte Carlo with Domain Transformation for Efficient Fourier Pricing of Multi-Asset Options"), [37](https://arxiv.org/html/2602.06424v1#bib.bib1 "Nonasymptotic Convergence Rate of Quasi-Monte Carlo: Applications to Linear Elliptic PDEs with Lognormal Coefficients and Importance Samplings")].
.

###### Remark 4.3.

The exponent Asing∗A^{\*}\_{\mathrm{sing}} yields a uniform (worst-case) convergence rate for the RQMC estimator across all components (k,p,ν)(k,p,\nu) and along the optimization trajectory. Such a worst-case bound is essential for the subsequent error propagation analysis in Section [5](https://arxiv.org/html/2602.06424v1#S5 "5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). In practice, however, the observed RQMC convergence can be substantially faster than the rate predicted by Asing∗A^{\*}\_{\mathrm{sing}}, owing to effective low dimensionality, the smoothing effect of the domain transformation GG, and boundary growth that is milder than the worst-case behavior permitted by the theoretical bounds. Less conservative bounds can be obtained by retaining the coordinate- and component-wise boundary exponents and anisotropic constructions (e.g., transform employing tuning or weighted QMC rules). We do not pursue such refinements here and instead leverage variance reduction through iteration-indexed multilevel differences.

Algorithm 3  Single-level Fourier-RQMC at optimization step jj

1:Allocation 𝐦(j)\mathbf{m}^{(j)}, Sobol size N∈ℕN\in\mathbb{N}, shifts SshiftS\_{\mathrm{shift}}. For k∈ℐqℓk\in\mathcal{I}\_{q\_{\ell}}: index set ℐk\mathcal{I}\_{k}; for 𝐩∈ℐk\mathbf{p}\in\mathcal{I}\_{k}: integrands hk,p(ν)​(𝐯;𝐦k,p(j))h\_{k,p}^{(\nu)}\left(\mathbf{v};\mathbf{m}\_{k,p}^{(j)}\right), marginal 𝐗k,p\mathbf{X}\_{k,p}, damping vectors 𝐊k,p(ν,j)\mathbf{K}\_{k,p}^{(\nu,j)} (Algorithm [2](https://arxiv.org/html/2602.06424v1#alg2 "Algorithm 2 ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

2:Based on the distribution of 𝐗k,p\mathbf{X}\_{k,p}, apply the appropriate
transformation from ([4.9](https://arxiv.org/html/2602.06424v1#S4.E9 "In 4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) or
([4.10](https://arxiv.org/html/2602.06424v1#S4.E10 "In 4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) to obtain the transformed integrands
h~k,p(ν)​(𝐯;𝐦k,p(j))\widetilde{h}\_{k,p}^{(\nu)}\left(\mathbf{v};\mathbf{m}\_{k,p}^{(j)}\right).

3:for k∈ℐqℓk\in\mathcal{I}\_{q\_{\ell}} do

4:  (Digital net generation)

5:  Generate once per kk an unshifted base-2 digital net {𝐮n(s)}n=1N⊂[0,1]k\{\mathbf{u}^{(s)}\_{n}\}\_{n=1}^{N}\subset[0,1]^{k} and reuse it for all 𝐩∈ℐk\mathbf{p}\in\mathcal{I}\_{k} 555For the NIG transform in ([4.10](https://arxiv.org/html/2602.06424v1#S4.E10 "In 4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), an additional mixing variable introduces one extra integration dimension. Hence, we generate {𝐮n(s)}n=1N⊂[0,1]k+1\{\mathbf{u}^{(s)}\_{n}\}\_{n=1}^{N}\subset[0,1]^{k+1} instead of [0,1]k[0,1]^{k}..

6:  Draw a digital shift 𝚫(s)∈[0,1]k\boldsymbol{\Delta}^{(s)}\in[0,1]^{k} (seed 1:Sshift1:S\_{\mathrm{shift}}) and set

|  |  |  |
| --- | --- | --- |
|  | 𝐯n(s)=𝐮n(s)⊕𝚫(s),n=1,…,N,\mathbf{v}^{(s)}\_{n}\;=\;\mathbf{u}^{(s)}\_{n}\,\oplus\,\boldsymbol{\Delta}^{(s)},\qquad n=1,\dots,N, |  |

where ⊕\oplus denotes the base-2 digital (bitwise XOR) shift.

7:Set IN,SshiftRQMC​[h~(ν)​(⋅;𝐦(j))]←0{I}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\widetilde{h}^{(\nu)}\left(\cdot;\mathbf{m}^{(j)}\right)\right]\leftarrow 0.

8:for k∈ℐqℓk\in\mathcal{I}\_{q\_{\ell}} do

9:  for 𝐩∈ℐk\mathbf{p}\in\mathcal{I}\_{k} do

10:    Compute the RQMC estimate IN,SshiftRQMC​[h~k,p(ν)​(⋅;𝐦k,p(j))]{I}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\widetilde{h}\_{k,p}^{(\nu)}\left(\cdot;\mathbf{m}\_{k,p}^{(j)}\right)\right] using {𝐯n(s)}n=1N\{\mathbf{v}^{(s)}\_{n}\}\_{n=1}^{N}.

11:    IN,SshiftRQMC[h~(ν)(⋅;𝐦(j))]+=IN,SshiftRQMC[h~k,p(ν)(⋅;𝐦k,p(j))]{I}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\widetilde{h}^{(\nu)}\left(\cdot;\mathbf{m}^{(j)}\right)\right]\mathrel{+}={I}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\widetilde{h}\_{k,p}^{(\nu)}\left(\cdot;\mathbf{m}\_{k,p}^{(j)}\right)\right]

12:return IN,SshiftRQMC​[h~(ν)​(⋅;𝐦(j))]{I}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\widetilde{h}^{(\nu)}\left(\cdot;\mathbf{m}^{(j)}\right)\right].

#### 4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation

To control oscillatory behavior and boundary growth in the Fourier-based integrands, we introduce a distribution-dependent, oscillation-aware change of variables GG, mapping ℝk\mathbb{R}^{k} to [0,1]k[0,1]^{k}, for k∈ℐqℓk\in\mathcal{I}\_{q\_{\ell}}. Our construction builds on ideas from Fourier-based option pricing [[4](https://arxiv.org/html/2602.06424v1#bib.bib72 "Quasi-Monte Carlo with Domain Transformation for Efficient Fourier Pricing of Multi-Asset Options")], but is adapted to the multivariate risk setting and complemented by a dedicated analysis of the induced oscillatory behavior.

We rewrite hk,p(ν)h\_{k,p}^{(\nu)} in ([3.3](https://arxiv.org/html/2602.06424v1#S3.E3 "In Notation 3.5 (Component selection and componentwise integrands). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) as a standard oscillatory (Fourier-type) integrand, with a (complex) amplitude ak,p(ν)​(𝐮;𝐦k,p,𝐊k,p(ν),𝚯k,p)a\_{k,p}^{(\nu)}\left(\mathbf{u};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}\right) and oscillatory phase wk,p​(𝐮;𝐦k,p)w\_{k,p}\left(\mathbf{u};\mathbf{m}\_{k,p}\right) as follows:

|  |  |  |
| --- | --- | --- |
|  | hk,p(ν)​(𝐮;𝐦k,p,𝐊k,p(ν),𝚯k,p)=ak,p(ν)​(𝐮;𝐦k,p,𝐊k,p(ν),𝚯k,p)​exp⁡(−i​wk,p​(𝐮;𝐦k,p)),h\_{k,p}^{(\nu)}(\mathbf{u};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p})\;=\;a\_{k,p}^{(\nu)}\left(\mathbf{u};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}\right)\,\exp\!\bigl(-\mathrm{i}\,w\_{k,p}(\mathbf{u};\mathbf{m}\_{k,p})\bigr), |  |

where:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ak,p(ν)​(𝐮;𝐦k,p,𝐊k,p(ν),𝚯k,p)\displaystyle a\_{k,p}^{(\nu)}\left(\mathbf{u};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}\right) | :=(2​π)−k​exp⁡(⟨𝐊k,p(ν),𝐦k,p⟩)​Φ𝐗k,p​(𝐮+i​𝐊k,p(ν))​ℓ^k,p(ν)​(𝐮+i​𝐊k,p(ν)),\displaystyle=(2\pi)^{-k}\exp\!\bigl(\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{m}\_{k,p}\rangle\bigr)\,\Phi\_{\mathbf{X}\_{k,p}}\left(\mathbf{u}+\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right)\,\widehat{\ell}\_{k,p}^{(\nu)}\left(\mathbf{u}+\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | wk,p​(𝐮;𝐦k,p)\displaystyle w\_{k,p}(\mathbf{u};\mathbf{m}\_{k,p}) | :=𝐦k,p⊤​𝐮,\displaystyle=\mathbf{m}\_{k,p}^{\top}\mathbf{u}, |  |

with 𝐮∈ℝk,𝐊k,p(ν)∈δKk,p(ν)\mathbf{u}\in\mathbb{R}^{k},\mathbf{K}\_{k,p}^{(\nu)}\in\delta\_{K\_{k,p}}^{(\nu)}. The transformed integrand is then expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
| (4.8) |  | h~k,p(ν)​(𝐯;𝐦k,p)=ak,p(ν)​(𝐮;𝐦k,p,𝐊k,p(ν),𝚯k,p)​exp⁡(−i​ϖ​(𝐯;𝚯k,p))​|detJG−1​(𝐯;𝚯k,p)|\widetilde{h}\_{k,p}^{(\nu)}(\mathbf{v};\mathbf{m}\_{k,p})=\;a\_{k,p}^{(\nu)}\left(\mathbf{u};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}\right)\,\exp{\left(-\mathrm{i}\,\varpi(\mathbf{v};\boldsymbol{\Theta}\_{k,p})\right)}\,\big|\det J\_{G^{-1}}(\mathbf{v};\boldsymbol{\Theta}\_{k,p})\big| |  |

with ϖ(𝐯;𝚯k,p):=𝐦k,p⊤G−1(𝐯;𝚯k,p)).\varpi\left(\mathbf{v};\boldsymbol{\Theta}\_{k,p}\right):=\mathbf{m}\_{k,p}^{\top}G^{-1}\left(\mathbf{v};\boldsymbol{\Theta}\_{k,p})\right).

If the domain transformation GG is not chosen appropriately, it can amplify oscillations of the transformed integrand near the boundary of [0,1]k[0,1]^{k} and thereby deteriorate the convergence of RQMC methods. To guide the choice of GG, we analyze in Appendix [C.1](https://arxiv.org/html/2602.06424v1#A3.SS1 "C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") the boundary oscillatory behavior of h~k,p(ν)\widetilde{h}\_{k,p}^{(\nu)} and derive distribution-dependent oscillation counts. These results motivate adopting the density-driven change of variables as proposed in [[4](https://arxiv.org/html/2602.06424v1#bib.bib72 "Quasi-Monte Carlo with Domain Transformation for Efficient Fourier Pricing of Multi-Asset Options")].

The effectiveness of the domain transformation is governed by the choice of a reference density
ψ​(⋅;𝚯𝐗k,p)\psi(\,\cdot\,;\boldsymbol{\Theta}\_{\mathbf{X}\_{k,p}}), with associated shape matrix 𝚺~k,p\widetilde{\boldsymbol{\Sigma}}\_{k,p}.
This reference density is chosen to control the boundary growth of the transformed integrand
h~k,p(ν)​(𝐯,𝐦k,p)\widetilde{h}\_{k,p}^{(\nu)}\left(\mathbf{v},\mathbf{m}\_{k,p}\right) defined in ([4.8](https://arxiv.org/html/2602.06424v1#S4.E8 "In 4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). For Gaussian marginals, the reference density is Gaussian, whereas for NIG marginals
we employ an auxiliary exponential (Laplace-type) reference density arising from the
mixture representation.

Given 𝚺~k,p\widetilde{\boldsymbol{\Sigma}}\_{k,p}, let L~k,p\widetilde{L}\_{k,p} denote a Cholesky factor such that
𝚺~k,p=𝑳~k,p​𝑳~k,p⊤\widetilde{\boldsymbol{\Sigma}}\_{k,p}=\widetilde{\boldsymbol{L}}\_{k,p}\widetilde{\boldsymbol{L}}\_{k,p}^{\top}.
For the loss vector models considered in Section [3](https://arxiv.org/html/2602.06424v1#S3 "3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), we employ the following distribution-dependent inverse transformations G−1G^{-1}.

* •

  Gaussian.
  Let G−1=TGauss:[0,1]k→ℝkG^{-1}=T\_{\mathrm{Gauss}}:[0,1]^{k}\to\mathbb{R}^{k} be defined by

  |  |  |  |
  | --- | --- | --- |
  |  | 𝐯1:k↦𝐮:=𝑳~k,p​Ψ−1​(𝐯1:k;𝐈k),\mathbf{v}\_{1:k}\;\mapsto\;\mathbf{u}:=\widetilde{\boldsymbol{L}}\_{k,p}\,\Psi^{-1}(\mathbf{v}\_{1:k};\mathbf{I}\_{k}), |  |

  where Ψ\Psi denotes the standard Gaussian CDF applied componentwise.
* •

  NIG.
  Let W∼Exp​(1)W\sim\mathrm{Exp}(1) be an auxiliary mixing variable with CDF ΨW​(w)=1−e−w\Psi\_{W}(w)=1-e^{-w}.
  Define G−1=TNIG:[0,1]k+1→ℝk×(0,∞)G^{-1}=T\_{\mathrm{NIG}}:[0,1]^{k+1}\to\mathbb{R}^{k}\times(0,\infty) by

  |  |  |  |
  | --- | --- | --- |
  |  | (𝐯1:k,vk+1)↦(𝐮,w):=(ΨW−1​(vk+1)​𝑳~k,p​Ψ−1​(𝐯1:k;𝐈k),ΨW−1​(vk+1)).(\mathbf{v}\_{1:k},v\_{k+1})\;\mapsto\;(\mathbf{u},w):=\Big(\sqrt{\Psi\_{W}^{-1}(v\_{k+1})}\,\widetilde{\boldsymbol{L}}\_{k,p}\Psi^{-1}(\mathbf{v}\_{1:k};\mathbf{I}\_{k}),\;\Psi\_{W}^{-1}(v\_{k+1})\Big). |  |

where 𝐯1:k:=(v1,…,vk)\mathbf{v}\_{1:k}:=(v\_{1},\ldots,v\_{k}), and 𝑰k\boldsymbol{I}\_{k} denotes the k×kk\times k identity matrix.

The resulting choice for 𝚺~k,p\widetilde{\boldsymbol{\Sigma}}\_{k,p} in this work is presented in Table [4.1](https://arxiv.org/html/2602.06424v1#S4.T1 "Table 4.1 ‣ 4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). We derive this choice in detail in Appendix [C.1.2](https://arxiv.org/html/2602.06424v1#A3.SS1.SSS2 "C.1.2 Choice of matrix 𝚺̃_{𝑘,𝑝} ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), where we quantify the boundary oscillations induced by the transformation and show how the choice of 𝚺~k,p\boldsymbol{\widetilde{\Sigma}}\_{k,p} and the scaling parameter cc controls the resulting oscillatory behavior. The scalar parameter c>1c>1 acts as a regularity control, trading off boundary oscillations
against concentration of the transformed integrand.

|  |  |
| --- | --- |
| Distribution | 𝚺~k,p\widetilde{\boldsymbol{\Sigma}}\_{k,p} |
| Gaussian | c​𝚺k,p−1\displaystyle c\,{\boldsymbol{\Sigma}}\_{k,p}^{-1} |
| NIG | 2​cδk,p2​𝚪k,p−1\displaystyle\frac{2c}{\delta\_{k,p}^{2}}\,\boldsymbol{\Gamma}\_{k,p}^{-1} |

Table 4.1: Choice of 𝚺~k,p\widetilde{\boldsymbol{\Sigma}}\_{k,p}. In the Gaussian case, 𝚺k,p\boldsymbol{\Sigma}\_{k,p} is defined in Example [E.1](https://arxiv.org/html/2602.06424v1#A5.Thmtheorem1 "Example E.1 (Gaussian). ‣ E.3 Loss vector distributions and extended characteristic functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). In the NIG case, 𝚪k,p\boldsymbol{\Gamma}\_{k,p} and δk,p\delta\_{k,p} are defined in Example [E.2](https://arxiv.org/html/2602.06424v1#A5.Thmtheorem2 "Example E.2 (Normal Inverse Gaussian (NIG)). ‣ E.3 Loss vector distributions and extended characteristic functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). The scaling parameter c>1c>1.

With this choice of reference density and associated scaling, the domain transformation for the Gaussian case takes the form

|  |  |  |  |
| --- | --- | --- | --- |
| (4.9) |  | ∫ℝkhk,p(ν)​(𝐮;𝐦k,p)​d𝐮=∫[0,1]khk,p(ν)​(𝑳~k,p​Ψ−1​(𝐯;𝑰k);𝐦k,p)ψk,p​(𝑳~k,p​Ψ−1​(𝐯;𝑰k))⏟:=h~k,p(ν)​(𝐯;𝐦k,p)​d𝐯,\int\_{\mathbb{R}^{k}}h\_{k,p}^{(\nu)}(\mathbf{u};\mathbf{m}\_{k,p})\,\mathrm{d}\mathbf{u}=\int\_{[0,1]^{k}}\underbrace{\frac{h\_{k,p}^{(\nu)}\!\left(\widetilde{\boldsymbol{L}}\_{k,p}\,\Psi^{-1}(\mathbf{v};\boldsymbol{I}\_{k});\mathbf{m}\_{k,p}\right)}{\psi\_{k,p}\!\left(\widetilde{\boldsymbol{L}}\_{k,p}\,\Psi^{-1}(\mathbf{v};\boldsymbol{I}\_{k})\right)}}\_{:=\widetilde{h}\_{k,p}^{(\nu)}(\mathbf{v};\mathbf{m}\_{k,p})}\,\mathrm{d}\mathbf{v}, |  |

For the NIG case, this yields the transform

|  |  |  |  |
| --- | --- | --- | --- |
| (4.10) |  | ∫ℝkhk,p(ν)​(𝐮;𝐦k,p)​d𝐮=∫[0,1]k+1hk,p(ν)​(ΨW−1​(vk+1)​𝑳~k,p​Ψ−1​(𝐯1:k;𝑰k);𝐦k,p)ψk,plap​(ΨW−1​(vk+1)​𝑳~k,p​Ψ−1​(𝐯1:k;𝑰k))⏟:=h~k,p(ν)​(𝐯;𝐦k,p)​d𝐯,\int\_{\mathbb{R}^{k}}h\_{k,p}^{(\nu)}(\mathbf{u};\mathbf{m}\_{k,p})\,\mathrm{d}\mathbf{u}=\int\_{[0,1]^{k+1}}\underbrace{\frac{h\_{k,p}^{(\nu)}\!\left(\sqrt{\Psi\_{W}^{-1}(v\_{k+1})}\,\widetilde{\boldsymbol{L}}\_{k,p}\,\Psi^{-1}(\mathbf{v}\_{1:k};\boldsymbol{I}\_{k});\mathbf{m}\_{k,p}\right)}{\psi\_{k,p}^{\mathrm{lap}}\!\left(\sqrt{\Psi\_{W}^{-1}(v\_{k+1})}\,\widetilde{\boldsymbol{L}}\_{k,p}\,\Psi^{-1}(\mathbf{v}\_{1:k};\boldsymbol{I}\_{k})\right)}}\_{:=\widetilde{h}\_{k,p}^{(\nu)}(\mathbf{v};\mathbf{m}\_{k,p})}\,\mathrm{d}\mathbf{v}, |  |

where ψlap\psi^{\mathrm{lap}} denotes the reference mixing density induced by the exponential variable WW and the associated change of variables, including the Jacobian factors arising from the scaling u↦W​uu\mapsto\sqrt{W}\,u and from the inverse CDF ΨW−1\Psi\_{W}^{-1}.

The resulting transformed integrands can be shown (Appendix [C.1](https://arxiv.org/html/2602.06424v1#A3.SS1 "C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")–[C.1.2](https://arxiv.org/html/2602.06424v1#A3.SS1.SSS2 "C.1.2 Choice of matrix 𝚺̃_{𝑘,𝑝} ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) to satisfy the polynomial-type boundary growth condition ([4.5](https://arxiv.org/html/2602.06424v1#S4.E5 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), with exponents Aj,p(ν)A^{(\nu)}\_{j,p} depending on the reference parameters and the scaling cc.

Figures [4.1](https://arxiv.org/html/2602.06424v1#S4.F1 "Figure 4.1 ‣ 4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") and [4.2](https://arxiv.org/html/2602.06424v1#S4.F2 "Figure 4.2 ‣ 4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") illustrate the distribution-dependent boundary oscillation behavior analyzed in Appendix [C.1](https://arxiv.org/html/2602.06424v1#A3.SS1 "C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). In the Gaussian case, the proposed transformation suppresses boundary oscillations more effectively than in the NIG case, even though the Gaussian example is higher-dimensional (10D) than the NIG example (3D). When c=1c=1, the transformed component integrands exhibit kink-like oscillations near the boundary in both settings, with the effect being more pronounced under the NIG transformation. Increasing the scale parameter to c>1c>1 improves the regularity of the transformed integrands, leading to smoother behavior and reduced boundary oscillations.

![Refer to caption](x7.png)


(a) c=1c=1

![Refer to caption](x8.png)


(b) c=8c=8

Figure 4.1: Transformed integrand component h~1,1(0)\widetilde{h}^{(0)}\_{1,1} for the QPC loss and a 33-dimensional NIG loss vector, with 𝐊1,1(0)=4.5\mathbf{K}^{(0)}\_{1,1}=4.5 and 𝐦1,1=−0.8\mathbf{m}\_{1,1}=-0.8 (parameter setting in Section [6.3](https://arxiv.org/html/2602.06424v1#S6.SS3 "6.3 QPC Loss with Three-Dimensional NIG Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).



![Refer to caption](x9.png)


(a) c=1c=1

![Refer to caption](x10.png)


(b) c=2.5c=2.5

Figure 4.2: 1D slice of the transformed integrand component h~2,(3,4)(0){\widetilde{h}\_{2,(3,4)}^{(0)}} with 𝐊2,(3,4)(0)=[2.763,0.523],𝐦2,(3,4)=[0.255,0.105]\mathbf{K}\_{2,(3,4)}^{(0)}=\left[2.763,0.523\right],\mathbf{m}\_{2,(3,4)}=\left[0.255,0.105\right] for the QPC loss and a 1010-dimensional Gaussian loss vector (parameter setting in Section [6.2](https://arxiv.org/html/2602.06424v1#S6.SS2 "6.2 QPC Loss with Ten-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

###### Remark 4.4.

We choose the domain transformation to mitigate boundary-induced oscillations by taking a scaling parameter c>1c>1, while avoiding excessive concentration of the reference density that would lead to poor numerical conditioning of the transformed integrands. In practice, the parameter cc trades off two competing effects: values close to 11 may leave residual oscillations near the boundary, whereas excessively large values of cc lead to overly concentrated (peaked) integrands due to strong decay. In our numerical experiments, we select cc from a moderate range, specifically c∈[4,10]c\in[4,10], which yields stable and robust performance. A principled, theoretically optimal choice of cc is left for future work.

With this choice of transformation for the component integrands, we next develop the multilevel extension of the Fourier-RQMC framework.

### 4.2 Iteration-Indexed Multilevel Fourier–RQMC Approximation

Recall from Section [2](https://arxiv.org/html/2602.06424v1#S2 "2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") that the primal–dual variable of the MSRM optimization problem is 𝐳:=(𝐦,λ)\mathbf{z}:=(\mathbf{m},\lambda). At the optimization step jj, we denote the iterate by 𝐳(j):=(𝐦(j),λ(j))\mathbf{z}^{(j)}:=(\mathbf{m}^{(j)},\lambda^{(j)}). In Algorithm [1](https://arxiv.org/html/2602.06424v1#alg1 "Algorithm 1 ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), the constrained optimizer requires repeated evaluations of the Fourier-based objective, gradient, and Hessian at successive iterates 𝐳(j)\mathbf{z}^{(j)}. Directly recomputing these quantities via RQMC at every iteration can be computationally expensive. This section introduces an iteration-indexed multilevel Fourier–RQMC construction that exploits the strong correlation between consecutive iterates 𝐳(j−1)\mathbf{z}^{(j-1)} and 𝐳(j)\mathbf{z}^{(j)}. By expressing gradient and Hessian evaluations in a block form and estimating differences across iterations, we obtain a multilevel estimator with reduced variance and improved efficiency. For notational convenience in this section and in Section [5](https://arxiv.org/html/2602.06424v1#S5 "5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), we introduce the following block-valued mappings.

###### Notation 4.5.

For ν=0,1,2\nu=0,1,2, define the block-valued mappings ℋ(ν)​(⋅;𝐳)\mathcal{H}^{(\nu)}(\cdot;\mathbf{z}) by

|  |  |  |
| --- | --- | --- |
|  | ℋ(0)​(⋅;𝐳):=∑k=1dmk+λ​h~(0)​(⋅;𝐦),ℋ(1)​(⋅;𝐳):=[𝟏−λ​h~(1)​(⋅;𝐦)−h~(0)​(⋅;𝐦)],\mathcal{H}^{(0)}(\cdot;\mathbf{z}):=\sum\_{k=1}^{d}m\_{k}+\lambda\,\widetilde{h}^{(0)}(\cdot;\mathbf{m}),\qquad\mathcal{H}^{(1)}(\cdot;\mathbf{z}):=\begin{bmatrix}\mathbf{1}-\lambda\,\widetilde{h}^{(1)}(\cdot;\mathbf{m})\\[3.0pt] -\,\widetilde{h}^{(0)}(\cdot;\mathbf{m})\end{bmatrix}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ℋ(2)​(⋅;𝐳):=[−λ​h~(2)​(⋅;𝐦)(h~(1)​(⋅;𝐦))⊤h~(1)​(⋅;𝐦)0].\mathcal{H}^{(2)}(\cdot;\mathbf{z}):=\begin{bmatrix}-\lambda\,\widetilde{h}^{(2)}(\cdot;\mathbf{m})&\big(\widetilde{h}^{(1)}(\cdot;\mathbf{m})\big)^{\!\top}\\[3.0pt] \widetilde{h}^{(1)}(\cdot;\mathbf{m})&0\end{bmatrix}. |  |

Then the Fourier-RQMC approximations of
ℒ^Fou​(𝐳)\widehat{\mathcal{L}}^{\mathrm{Fou}}(\mathbf{z}),
ℒ^∇𝐳Fou​(𝐳)\widehat{\mathcal{L}}^{\mathrm{Fou}}\_{\nabla\_{\mathbf{z}}}(\mathbf{z}), and
ℒ^∇𝐳2Fou​(𝐳)\widehat{\mathcal{L}}^{\mathrm{Fou}}\_{\nabla\_{\mathbf{z}}^{2}}(\mathbf{z})
are denoted by
IN,SshiftRQMC​[ℋ(0)​(⋅;𝐳)]I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\!\big[\mathcal{H}^{(0)}(\cdot;\mathbf{z})\big],
IN,SshiftRQMC​[ℋ(1)​(⋅;𝐳)]I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\!\big[\mathcal{H}^{(1)}(\cdot;\mathbf{z})\big], and
IN,SshiftRQMC​[ℋ(2)​(⋅;𝐳)]I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\!\big[\mathcal{H}^{(2)}(\cdot;\mathbf{z})\big], respectively.
Here IN,SshiftRQMC​[⋅]I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}[\cdot] is applied componentwise to vector-valued
h~(1)​(⋅;𝐦)\widetilde{h}^{(1)}(\cdot;\mathbf{m}) and entrywise to matrix-valued h~(2)​(⋅;𝐦)\widetilde{h}^{(2)}(\cdot;\mathbf{m}).

The mappings ℋ(0)\mathcal{H}^{(0)}, ℋ(1)\mathcal{H}^{(1)}, and ℋ(2)\mathcal{H}^{(2)} in Notation [4.5](https://arxiv.org/html/2602.06424v1#S4.Thmtheorem5 "Notation 4.5. ‣ 4.2 Iteration-Indexed Multilevel Fourier–RQMC Approximation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") correspond to the Fourier-based representations of the objective, first-order optimality conditions, and second-order conditions w.r.t. the primal–dual variable 𝐳\mathbf{z}.

Within the single-level Fourier–RQMC framework, Algorithm [3](https://arxiv.org/html/2602.06424v1#alg3 "Algorithm 3 ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") evaluates at each optimization iteration j∈{1,…,J}j\in\{1,\ldots,J\} the Fourier-based gradient ℒ^∇zFou​(𝐳(j))\widehat{\mathcal{L}}^{\mathrm{Fou}}\_{\nabla z}\left(\mathbf{z}^{(j)}\right). This quantity is approximated using a RQMC estimator IN,SshiftRQMCI^{\mathrm{RQMC}}\_{N,S\_{\mathrm{shift}}}, constructed from a fixed set of NN Sobol points and SshiftS\_{\mathrm{shift}} digital shifts. In particular, the component g^(v),Fou​(𝐦(j))\widehat{g}^{(v),\mathrm{Fou}}(\mathbf{m}^{(j)}) is approximated by

|  |  |  |  |
| --- | --- | --- | --- |
| (4.11) |  | IN,SshiftRQMC​[h~(ν)​(⋅;𝐦(j))]=∑k∈ℐqℓ∑𝐩∈ℐkIN,SshiftRQMC​[h~k,p(ν)​(⋅;𝐦k,p(j))].\displaystyle I^{\mathrm{RQMC}}\_{N,S\_{\mathrm{shift}}}\!\left[\widetilde{h}^{(\nu)}\left(\,\cdot\,;\mathbf{m}^{(j)}\right)\right]=\sum\_{k\in\mathcal{I}\_{q\_{\ell}}}\sum\_{\mathbf{p}\in\mathcal{I}\_{k}}I^{\mathrm{RQMC}}\_{N,S\_{\mathrm{shift}}}\!\left[\widetilde{h}^{(\nu)}\_{k,p}\left(\,\cdot\,;\mathbf{m}^{(j)}\_{k,p}\right)\right]. |  |

Evaluating ([4.11](https://arxiv.org/html/2602.06424v1#S4.E11 "In 4.2 Iteration-Indexed Multilevel Fourier–RQMC Approximation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) at every optimization iteration can be computationally demanding, particularly when the integrand dimension kk is large, when many component integrands h~k,p(v)\widetilde{h}^{(v)}\_{k,p} must be evaluated, or when the number of optimization iterations is itself substantial. From a numerical optimization perspective, however, the successive iterates 𝐳(j−1)\mathbf{z}^{(j-1)} and 𝐳(j)\mathbf{z}^{(j)} are typically strongly correlated, since the optimization algorithm evolves gradually toward a solution. This observation motivates the use of a control-variate strategy, whereby the estimator at iteration 𝐳(j−1)\mathbf{z}^{(j-1)} is exploited to reduce the variance of the estimator at the current iteration 𝐳(j)\mathbf{z}^{(j)}.

To formalize this idea, we express the Fourier-based gradient at iteration j as the telescoping sum

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ^∇𝐳Fou​(𝐳(j))\displaystyle\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}}\left(\mathbf{z}^{(j)}\right) | =ℒ^∇𝐳Fou​(𝐳(1))+∑j=2J[ℒ^∇𝐳Fou​(𝐳(j))−ℒ^∇𝐳Fou​(𝐳(j−1))]\displaystyle=\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}}\left(\mathbf{z}^{(1)}\right)+\sum\_{j=2}^{J}\left[\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}}\left(\mathbf{z}^{(j)}\right)-\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}}\left(\mathbf{z}^{(j-1)}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℒ^∇𝐳Fou​(𝐳(1))+∑j=2JΔ​ℒ^∇𝐳Fou​(𝐳(j),𝐳(j−1))\displaystyle=\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}}\left(\mathbf{z}^{(1)}\right)+\sum\_{j=2}^{J}\Delta\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}}\left(\mathbf{z}^{(j)},\mathbf{z}^{(j-1)}\right) |  |

where Δ​ℒ^∇𝐳Fou​(𝐳(j),𝐳(j−1)):=ℒ^∇𝐳Fou​(𝐳(j))−ℒ^∇𝐳Fou​(𝐳(j−1))\Delta\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}}\left(\mathbf{z}^{(j)},\mathbf{z}^{(j-1)}\right):=\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}}\left(\mathbf{z}^{(j)}\right)-\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}}\left(\mathbf{z}^{(j-1)}\right). The increments in this decomposition capture differences between consecutive optimization iterates and typically exhibit smaller variance and improved regularity compared to the original estimator. This structure enables an iteration-indexed multilevel RQMC construction, conceptually related to Multilevel Monte Carlo (MLMC) methods [[23](https://arxiv.org/html/2602.06424v1#bib.bib59 "Multilevel Monte Carlo methods"), [8](https://arxiv.org/html/2602.06424v1#bib.bib8 "Multilevel Monte Carlo with Numerical Smoothing for Robust and Efficient Computation of Probabilities and Densities")], with the crucial distinction that here the “levels” correspond to optimization iterations rather than to discretization levels of a stochastic differential equation.

We first estimate ℒ^∇𝐳Fou​(𝐳(1))\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}}\left(\mathbf{z}^{(1)}\right) by its RQMC approximation
IN,SshiftRQMC​[ℋ(1)​(⋅;𝐳1)]{I}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}\left(\cdot;\mathbf{z}\_{1}\right)\right] using ([4.11](https://arxiv.org/html/2602.06424v1#S4.E11 "In 4.2 Iteration-Indexed Multilevel Fourier–RQMC Approximation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"))
with NN Sobol points and SshiftS\_{\mathrm{shift}} digital shifts.
At each subsequent iteration j∈{2,…,J}j\in\{2,\dots,J\}, we evaluate the incremental difference Δ​ℒ^∇𝐳Fou​(𝐳(j),𝐳(j−1))\Delta\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}}\left(\mathbf{z}^{(j)},\mathbf{z}^{(j-1)}\right) by INj,SshiftRQMC​[Δ​ℋ(1)​(⋅;𝐳(j),𝐳(j−1))]{I}\_{N\_{j},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\mathcal{H}^{(1)}\left(\cdot;\mathbf{z}^{(j)},\mathbf{z}^{(j-1)}\right)\right] using NjN\_{j} Sobol points and the same number SshiftS\_{\mathrm{shift}} of randomizations, but with *independent* digital shifts (i.e., a fresh set of RQMC randomizations for each iteration),
whose components are given by
INj,SshiftRQMC​[Δ​h~(ν)]{I}\_{N\_{j},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\widetilde{h}^{(\nu)}\right]

|  |  |  |  |
| --- | --- | --- | --- |
|  | INj,SshiftRQMC​[Δ​h~(ν)​(⋅;𝐦(j),𝐦(j−1))]\displaystyle{I}\_{N\_{j},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\widetilde{h}^{(\nu)}\left(\cdot;\mathbf{m}^{(j)},\mathbf{m}^{(j-1)}\right)\right] | :=∑k∈ℐqℓ∑𝐩∈ℐkINj,SshiftRQMC​[Δ​h~k,p(ν)​(⋅;𝐦k,p(j),𝐦k,p(j−1))],\displaystyle=\sum\_{k\in\mathcal{I}\_{q\_{\ell}}}\sum\_{\mathbf{p}\in\mathcal{I}\_{k}}I\_{N\_{j},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\!\left[\Delta\widetilde{h}\_{k,p}^{(\nu)}\!\left(\cdot;\mathbf{m}^{(j)}\_{k,p},\mathbf{m}^{(j-1)}\_{k,p}\right)\right], |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | INj,SshiftRQMC​[Δ​h~k,p(ν),Fou​(⋅;𝐦(j),𝐦(j−1))]\displaystyle{I}\_{N\_{j},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\widetilde{h}\_{k,p}^{(\nu),{\mathrm{Fou}}}\left(\cdot;\mathbf{m}^{(j)},\mathbf{m}^{(j-1)}\right)\right] | :=1Sshift​∑s=1Sshift1Nj​∑n=1NjΔ​h~k,p(ν)​(𝐯n(s,j);𝐦k,p(j),𝐦k,p(j−1)),\displaystyle=\frac{1}{S\_{\text{shift}}}\sum\_{s=1}^{S\_{\text{shift}}}\frac{1}{N\_{j}}\sum\_{n=1}^{N\_{j}}\Delta\widetilde{h}\_{k,p}^{(\nu)}\!\left(\mathbf{v}\_{n}^{(s,j)};\mathbf{m}^{(j)}\_{k,p},\mathbf{m}^{(j-1)}\_{k,p}\right), |  |

and the differences of the transformed integrands are defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​h~k,p(ν)​(𝐯;𝐦k,p(j),𝐦k,p(j−1))\displaystyle\Delta\widetilde{h}\_{k,p}^{(\nu)}\!\left(\mathbf{v};\mathbf{m}\_{k,p}^{(j)},\mathbf{m}\_{k,p}^{(j-1)}\right) | :=h~k,p(ν)​(𝐯;𝐦k,p(j))−h~k,p(ν)​(𝐯;𝐦k,p(j−1)).\displaystyle=\widetilde{h}\_{k,p}^{(\nu)}\!\left(\mathbf{v};\mathbf{m}\_{k,p}^{(j)}\right)-\widetilde{h}\_{k,p}^{(\nu)}\!\left(\mathbf{v};\mathbf{m}\_{k,p}^{(j-1)}\right). |  |

The advantage of the multilevel method is that the difference terms Δ​h~k,p(ν)​(𝐯;𝐦k,p(j),𝐦k,p(j−1))\Delta\widetilde{h}\_{k,p}^{(\nu)}\!\left(\mathbf{v};\mathbf{m}^{(j)}\_{k,p},\mathbf{m}^{(j-1)}\_{k,p}\right)
often have better regularity and smaller variability than the original integrands,
h~k,p(ν)​(𝐯;𝐦k,p(j))\widetilde{h}\_{k,p}^{(\nu)}\!\left(\mathbf{v};\mathbf{m}^{(j)}\_{k,p}\right)(see Figure [4.3](https://arxiv.org/html/2602.06424v1#S4.F3 "Figure 4.3 ‣ 4.2 Iteration-Indexed Multilevel Fourier–RQMC Approximation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") for illustration), and then we can choose the number of Sobol points NjN\_{j} in a level-dependent manner through the optimization process, which can reduce our computational time. This will be discussed in more detail in Section [5.3.2](https://arxiv.org/html/2602.06424v1#S5.SS3.SSS2 "5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

![Refer to caption](x11.png)


Figure 4.3: Transformed integrand component h~1,1(0)\widetilde{h}\_{1,1}^{(0)} (solid) and the corresponding difference integrand arising in the multilevel construction (dashed) across successive optimization iterations, for the QPC loss and 10D Gaussian loss vector (parameter setting in Section [6.2](https://arxiv.org/html/2602.06424v1#S6.SS2 "6.2 QPC Loss with Ten-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

###### Remark 4.6 (Damping for difference integrands).

Instead of determining two separate damping vectors
𝐊k,p(ν,j−1)\mathbf{K}^{(\nu,j-1)}\_{k,p} and 𝐊k,p(ν,j)\mathbf{K}^{(\nu,j)}\_{k,p} for the integrands
h~k,p(ν)​(𝐯;𝐦k,p(j−1))\widetilde{h}^{(\nu)}\_{k,p}\left(\mathbf{v};\mathbf{m}^{(j-1)}\_{k,p}\right) and
h~k,p(ν)​(𝐯;𝐦k,p(j))\widetilde{h}^{(\nu)}\_{k,p}\left(\mathbf{v};\mathbf{m}^{(j)}\_{k,p}\right),
we apply Algorithm [2](https://arxiv.org/html/2602.06424v1#alg2 "Algorithm 2 ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") directly to the difference integrand

|  |  |  |
| --- | --- | --- |
|  | Δ​h~k,p(ν)​(𝐯;𝐦k,p(j),𝐦k,p(j−1))=h~k,p(ν)​(𝐯;𝐦k,p(j))−h~k,p(ν)​(𝐯;𝐦k,p(j−1)),\Delta\widetilde{h}^{(\nu)}\_{k,p}\left(\mathbf{v};\mathbf{m}^{(j)}\_{k,p},\mathbf{m}^{(j-1)}\_{k,p}\right)=\widetilde{h}^{(\nu)}\_{k,p}\left(\mathbf{v};\mathbf{m}^{(j)}\_{k,p}\right)-\widetilde{h}^{(\nu)}\_{k,p}\left(\mathbf{v};\mathbf{m}^{(j-1)}\_{k,p}\right), |  |

and compute a single damping vector 𝐊k,p(ν,j)\mathbf{K}^{(\nu,j)}\_{k,p} for this term.

This choice is justified because the difference integrand typically inherits an admissible analyticity strip given by the intersection of the strips of the two terms and, in practice, often exhibits milder oscillations and boundary growth due to cancellation. In particular, cancellations between consecutive optimization iterates reduce oscillatory behavior and boundary growth. As a result, the difference integrands exhibit improved regularity and smaller variability, which is advantageous both for contour selection and for variance reduction in the multilevel estimator.

A concise overview of the multilevel Fourier–RQMC algorithm is provided in Algorithm [4](https://arxiv.org/html/2602.06424v1#alg4 "Algorithm 4 ‣ 4.2 Iteration-Indexed Multilevel Fourier–RQMC Approximation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

Algorithm 4  Multilevel Fourier-RQMC at optimization step jj

1:Allocation 𝐦(j)\mathbf{m}^{(j)}; baseline Sobol size N1=N∈ℕN\_{1}=N\in\mathbb{N}; level sizes {Nl}l=2j\{N\_{l}\}\_{l=2}^{j};
number of shifts SshiftS\_{\mathrm{shift}}; for k∈ℐqℓk\in\mathcal{I}\_{q\_{\ell}}; index set ℐk\mathcal{I}\_{k}, for 𝐩∈ℐk\mathbf{p}\in\mathcal{I}\_{k}: component *difference* integrands
Δ​hk,p(ν,l)​(𝐯;𝐦k,p(l),𝐦k,p(l−1))\Delta h\_{k,p}^{(\nu,l)}\left(\mathbf{v};\mathbf{m}\_{k,p}^{(l)},\mathbf{m}\_{k,p}^{(l-1)}\right) for levels l=2,…,jl=2,\dots,j with corresponding optimal damping vectors 𝐊k,p(ν,l)\mathbf{K}\_{k,p}^{(\nu,l)}; RQMC estimates at *level-1*
IN1,SshiftRQMC​[h~(ν)​(⋅;𝐦(1))]{I}\_{N\_{1},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\widetilde{h}^{(\nu)}\left(\cdot;\mathbf{m}^{(1)}\right)\right] from Algorithm [3](https://arxiv.org/html/2602.06424v1#alg3 "Algorithm 3 ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

2:For each (k,p)(k,p), apply the same transform ([4.9](https://arxiv.org/html/2602.06424v1#S4.E9 "In 4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) or ([4.10](https://arxiv.org/html/2602.06424v1#S4.E10 "In 4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) used at the level 11 to obtain Δ​h~k,p(ν,l)​(𝐯;𝐦k,p(l),𝐦k,p(l−1))\Delta\widetilde{h}\_{k,p}^{(\nu,l)}\left(\mathbf{v};\mathbf{m}\_{k,p}^{(l)},\mathbf{m}\_{k,p}^{(l-1)}\right).

3:(Coupled base nets across levels) For k∈ℐqℓk\in\mathcal{I}\_{q\_{\ell}}:

* •

  Generate a single *unshifted* base-2 digital net
  {𝐮n(s)}n=1N1⊂[0,1]k\{\mathbf{u}^{(s)}\_{n}\}\_{n=1}^{N\_{1}}\subset[0,1]^{k}. Reuse this same *unshifted* net for *all* levels l=1,…,jl=1,\dots,j and all 𝐩∈ℐk\mathbf{p}\in\mathcal{I}\_{k}.

4:Initialize the multi-level estimators from level 22 to jj, IN2:l,SshiftRQMC​[Δ​h~(ν)]←0{I}\_{N\_{2:l},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\widetilde{h}^{(\nu)}\right]\leftarrow 0

5:for l=2,…,jl=2,\dots,j do

6:  Draw an *independent* digital shift 𝚫(s,l)∈[0,1]k\boldsymbol{\Delta}^{(s,l)}\in[0,1]^{k} (with a new seed, independent across kk and ll).

7:  Form the shifted points 𝐯n(s,l)=𝐮n(s)⊕𝚫(s,l)\mathbf{v}^{(s,l)}\_{n}=\mathbf{u}^{(s)}\_{n}\oplus\boldsymbol{\Delta}^{(s,l)}, n=1,…,Nln=1,\dots,N\_{l}.

8:  Initialize the level-ll increments:
INl,SshiftRQMC​[Δ​h~(ν)​(⋅;𝐦(l),𝐦(l−1))]←0.{I}\_{N\_{l},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\widetilde{h}^{(\nu)}\left(\cdot;\mathbf{m}^{(l)},\mathbf{m}^{(l-1)}\right)\right]\leftarrow 0.

9:  for k∈ℐqℓk\in\mathcal{I}\_{q\_{\ell}} do

10:    for 𝐩∈ℐk\mathbf{p}\in\mathcal{I}\_{k} do

11:     Compute
INl,SshiftRQMC​[Δ​h~k,p(ν)​(⋅;𝐦k,p(l),𝐦k,p(l−1))]I^{\mathrm{RQMC}}\_{N\_{l},S\_{\mathrm{shift}}}\!\left[\Delta\widetilde{h}\_{k,p}^{(\nu)}\left(\cdot;\mathbf{m}\_{k,p}^{(l)},\mathbf{m}\_{k,p}^{(l-1)}\right)\right]
using {𝐯n(s,l)}n=1Nl\{\mathbf{v}^{(s,l)}\_{n}\}\_{n=1}^{N\_{l}}.

12:     Accumulate
INl,SshiftRQMC[Δh~(ν)(⋅;𝐦(l),𝐦(l−1))]+=INl,SshiftRQMC[Δh~k,p(ν)(⋅;𝐦k,p(l),𝐦k,p(l−1))].{I}\_{N\_{l},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\widetilde{h}^{(\nu)}\left(\cdot;\mathbf{m}^{(l)},\mathbf{m}^{(l-1)}\right)\right]\mathrel{+}=I^{\mathrm{RQMC}}\_{N\_{l},S\_{\mathrm{shift}}}\!\left[\Delta\widetilde{h}\_{k,p}^{(\nu)}\left(\cdot;\mathbf{m}\_{k,p}^{(l)},\mathbf{m}\_{k,p}^{(l-1)}\right)\right].

13:  Update the multi-level estimators:
IN2:l,SshiftRQMC[Δh~(ν)]+=INj,SshiftRQMC[Δh~(ν)(⋅;𝐦(l),𝐦(l−1))].{I}\_{N\_{2:l},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\widetilde{h}^{(\nu)}\right]\mathrel{+}={I}\_{N\_{j},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\widetilde{h}^{(\nu)}\left(\cdot;\mathbf{m}^{(l)},\mathbf{m}^{(l-1)}\right)\right].

14:Output at step jj:
INj,SshiftRQMC​[h~(ν)​(⋅;𝐦(j))]=IN1,SshiftRQMC​[h~(ν)​(⋅;𝐦(1))]+IN2:l,SshiftRQMC​[Δ​h~(ν)].{I}\_{N\_{j},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\widetilde{h}^{(\nu)}\left(\cdot;\mathbf{m}^{(j)}\right)\right]={I}\_{N\_{1},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\widetilde{h}^{(\nu)}\left(\cdot;\mathbf{m}^{(1)}\right)\right]+{I}\_{N\_{2:l},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\widetilde{h}^{(\nu)}\right].

## 5 Error and Complexity Analysis for Fourier–RQMC Methods

This section analyzes the error and computational complexity of the proposed single-level and multilevel Fourier–RQMC schemes. We decompose the total numerical error into (i) an optimization error due to the SQP solver (Section [5.1](https://arxiv.org/html/2602.06424v1#S5.SS1 "5.1 Optimization error ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) and (ii) a quadrature-induced surrogate error due to Fourier–RQMC approximation of the expectation terms (Section [5.2](https://arxiv.org/html/2602.06424v1#S5.SS2 "5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). Throughout, we assume the KKT system ([2.7](https://arxiv.org/html/2602.06424v1#S2.E7 "In Theorem 2.8 (Theorem 3.4 in [1]). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) admits a unique solution 𝐳∗=(𝐦∗,λ∗)\mathbf{z}^{\ast}=(\mathbf{m}^{\ast},\lambda^{\ast}), ensuring the target allocation is well defined. A convergence analysis of the SAA method for the MSRM problem is presented in Appendix [D](https://arxiv.org/html/2602.06424v1#A4 "Appendix D Convergence analysis for the SAA method ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), providing a benchmark for comparison with our Fourier–RQMC surrogates. We now introduce additional notation that will be used in Sections [5.1](https://arxiv.org/html/2602.06424v1#S5.SS1 "5.1 Optimization error ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")–[5.3](https://arxiv.org/html/2602.06424v1#S5.SS3 "5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

###### Notation 5.1.

* •

  Let M⊂ℝdM\subset\mathbb{R}^{d} be a nonempty compact set. For each component (k,p)(k,p), define
  Mk,p:=Pk,p​M⊂ℝkM\_{k,p}:=P\_{k,p}M\subset\mathbb{R}^{k}, with Pk,pP\_{k,p} is defined in Notation [3.5](https://arxiv.org/html/2602.06424v1#S3.Thmtheorem5 "Notation 3.5 (Component selection and componentwise integrands). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
  Moreover, for a given λ¯>0\overline{\lambda}>0, set
  𝒵:=M×(0,λ¯]⊂ℝd+1\mathcal{Z}:=M\times(0,\overline{\lambda}]\subset\mathbb{R}^{d+1}.
* •

  𝐳∗=(𝐦∗,λ∗)\mathbf{z}^{\*}=\left(\mathbf{m^{\*}},\lambda^{\*}\right) denotes the exact unique solution obtained using the
  true Lagrangian
  ℒ​(𝐳)​(ℒ^Fou​(𝐳))\mathcal{L}(\mathbf{z})\left(\widehat{\mathcal{L}}^{\mathrm{Fou}}(\mathbf{z})\right).
* •

  𝐳N,SshiftRQMC,∗:=(𝐦N,SshiftRQMC,∗,λN,SshiftRQMC,∗){\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}:=\left({\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*},{\lambda}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}\right) denotes the solution obtained by
  replacing the true Lagrangian
  with its Fourier-RQMC approximation IN,SshiftRQMC​(ℋ(0)​(⋅;𝐳)).I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\!\left(\mathcal{H}^{(0)}(\cdot;\mathbf{z})\right).
* •

  𝐳N,Sshift(RQMC,j):=(𝐦N,Sshift(RQMC,j),λN,Sshift(RQMC,j)){\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}:=\left({\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)},{\lambda}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\right) be the jj-th iterate solution, which is returned by the numerical optimization solver (SLSQP) applied to the Fourier-RQMC problem IN,SshiftRQMC​(ℋ(0)​(⋅;𝐳)).I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\!\left(\mathcal{H}^{(0)}(\cdot;\mathbf{z})\right).

By the triangle inequality, we obtain the following decomposition of the total error

|  |  |  |  |
| --- | --- | --- | --- |
| (5.1) |  | ‖𝐳N,Sshift(RQMC,j)−𝐳∗‖≤‖𝐳N,Sshift(RQMC,j)−𝐳N,SshiftRQMC,∗‖⏟εopt​(j)+‖𝐳N,SshiftRQMC,∗−𝐳∗‖⏟εstatRQMC​(N).\bigl\|{\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}-\mathbf{z}^{\*}\bigr\|\;\leq\;\underbrace{\bigl\|{\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}-{\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}\bigr\|}\_{\varepsilon\_{\mathrm{opt}}(j)}\;+\;\underbrace{\bigl\|{\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}-\mathbf{z}^{\*}\bigr\|}\_{\varepsilon\_{\mathrm{stat}}^{\mathrm{RQMC}}(N)}. |  |

where

* •

  εopt​(j){\varepsilon\_{\mathrm{opt}}(j)} is optimization error, set by the deterministic solver (SLSQP) on the Fourier-RQMC surrogate.
* •

  εstatRQMC​(N){\varepsilon\_{\mathrm{stat}}^{\mathrm{RQMC}}(N)} is a statistical error when approximating the exact system with the Fourier-RQMC surrogate.

###### Remark 5.2.

We emphasize that the optimization error εopt​(j)\varepsilon\_{\mathrm{opt}}(j) is governed solely by the convergence properties of the SQP algorithm applied to the Fourier–RQMC surrogate problem and is therefore insensitive to whether a single-level or multilevel Fourier–RQMC estimator is employed. In contrast, the statistical error εstatRQMC​(N)\varepsilon^{\mathrm{RQMC}}\_{\mathrm{stat}}(N) depends explicitly on the structure of the underlying Fourier–RQMC estimator, and it is at this level that the distinction between single-level and multilevel constructions becomes essential for variance reduction and complexity improvements.

We now analyze these two error contributions separately, starting with the optimization error εopt​(j)\varepsilon\_{\mathrm{opt}}(j).

### 5.1 Optimization error

We perform numerical optimization based on the Fourier–RQMC surrogates. To derive convergence rates for the associated numerical optimization scheme implemented via SQP, we introduce in Appendix [A.1](https://arxiv.org/html/2602.06424v1#A1.SS1 "A.1 Additional Assumptions for the Error Analysis ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") a set of regularity assumptions, adapted from [[10](https://arxiv.org/html/2602.06424v1#bib.bib46 "Sequential Quadratic Programming")] and tailored to the Fourier–RQMC surrogate optimization problem, and obtain the following result from [[10](https://arxiv.org/html/2602.06424v1#bib.bib46 "Sequential Quadratic Programming"), Theorem 3.4].

###### Theorem 5.3.

Suppose that Assumption [A.2](https://arxiv.org/html/2602.06424v1#A1.Thmtheorem2 "Assumption A.2 (Regularity conditions for the Fourier–RQMC problem). ‣ A.1 Additional Assumptions for the Error Analysis ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") holds, and let the sequence
{𝐳N,Sshift(RQMC,j)}j≥0\{{\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\}\_{j\geq 0} be generated by the SQP algorithm.
Assume further that, for almost every realization of the RQMC shifts, the SQP iterates satisfy 𝐳N,Sshift(RQMC,j)→𝐳N,SshiftRQMC,∗{\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\to{\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*} as j→∞j\to\infty. Then the convergence is superlinear: there exists a sequence of constants
{ηj}j≥0\{\eta\_{j}\}\_{j\geq 0} with ηj>0\eta\_{j}>0 and ηj→0\eta\_{j}\to 0 such that

|  |  |  |  |
| --- | --- | --- | --- |
| (5.2) |  | ‖𝐳N,Sshift(RQMC,j+1)−𝐳N,SshiftRQMC,∗‖≤ηj​‖𝐳N,Sshift(RQMC,j)−𝐳N,SshiftRQMC,∗‖.\left\lVert\mathbf{z}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j+1)}-{\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}\right\rVert\leq\eta\_{j}\,\left\lVert{\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}-{\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}\right\rVert. |  |

###### Proof.

The detailed proof of Theorem [5.2](https://arxiv.org/html/2602.06424v1#S5.E2 "In Theorem 5.3. ‣ 5.1 Optimization error ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") is in [[10](https://arxiv.org/html/2602.06424v1#bib.bib46 "Sequential Quadratic Programming")].
∎

###### Remark 5.4.

Under the conditions of Theorem [5.2](https://arxiv.org/html/2602.06424v1#S5.E2 "In Theorem 5.3. ‣ 5.1 Optimization error ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), there exists an iteration index
JlocJ\_{\mathrm{loc}} such that, for all j≥Jlocj\geq J\_{\mathrm{loc}}, 𝐳N,Sshift(RQMC,j){\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)} exhibit the corresponding superlinear contraction. We refer to this regime as the *local convergence stage*.

Using Theorem [5.2](https://arxiv.org/html/2602.06424v1#S5.E2 "In Theorem 5.3. ‣ 5.1 Optimization error ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") together with
Remark [5.4](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem4 "Remark 5.4. ‣ 5.1 Optimization error ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), the optimization error, measured w.r.t. the Fourier-RQMC surrogate solution, 𝐳N,SshiftRQMC,∗\mathbf{z}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*},
εopt​(j)\varepsilon\_{\mathrm{opt}}(j) admits the superlinear bound

|  |  |  |  |
| --- | --- | --- | --- |
| (5.3) |  | εopt​(j)=𝒪​(‖eJloc‖pj−Jloc),1<p<2,j≥Jloc,\varepsilon\_{\mathrm{opt}}(j)=\mathcal{O}\left(\|e\_{J\_{\mathrm{loc}}}\|^{\,p^{\,j-J\_{\mathrm{loc}}}}\right),\quad 1<p<2,\qquad j\geq J\_{\mathrm{loc}}, |  |

where
‖eJloc‖:=‖𝐳N,Sshift(RQMC,Jloc)−𝐳N,SshiftRQMC,∗‖.\|e\_{J\_{\mathrm{loc}}}\|:=\left\lVert{\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},J\_{\mathrm{loc}})}-{\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}\right\rVert.

We next analyze the statistical error εstatRQMC​(N)\varepsilon\_{\mathrm{stat}}^{\mathrm{RQMC}}(N) induced by the Fourier-RQMC approximation of the expectation terms.

### 5.2 Statistical Error and Asymptotic Analysis

In order to bound the statistical error of the Fourier-RQMC solution, we first establish a uniform strong law of large numbers (USLLN) for the estimators IN,S¯RQMC​[h~k,p(ν)​(⋅;𝐦k,p)]I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}(\cdot;\mathbf{m}\_{k,p})\right], ν∈{0,1,2}\nu\in\{0,1,2\}, k∈ℐqℓk\in\mathcal{I}\_{q\_{\ell}}, and 𝐩∈ℐk\mathbf{p}\in\mathcal{I}\_{k}, in the regime N→∞N\to\infty for fixed Sshift=S¯S\_{\mathrm{shift}}=\overline{S}.

As noted in [[42](https://arxiv.org/html/2602.06424v1#bib.bib53 "A Strong Law of Large Numbers for Scrambled Net Integration")], almost sure convergence in NN need not hold for arbitrary randomizations of low-discrepancy nets. Therefore, throughout the remainder of this section, we work with Sobol point sets randomized via *nested uniform scrambling* [[43](https://arxiv.org/html/2602.06424v1#bib.bib19 "Randomly Permuted (t,m,s)-Nets and (t, s)-Sequences")]. For numerical experiments (Section  [4.1](https://arxiv.org/html/2602.06424v1#S4.SS1 "4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), we instead employ digitally shifted Sobol sequences.
Moreover, in what follows, we work under Assumptions [3.2](https://arxiv.org/html/2602.06424v1#S3.Ex2 "Assumption 3.2 (Admissible contour shifts). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") for g^k,p(ν),Fou\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}} and [4.1](https://arxiv.org/html/2602.06424v1#S4.Thmtheorem1 "Assumption 4.1 (Square-integrability of transformed integrands). ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") for h~k,p(ν)\widetilde{h}\_{k,p}^{(\nu)}, with ν∈{0,1,2}\nu\in\{0,1,2\}.

The following lemma provides uniform convergence of the Fourier–RQMC estimators over the decision set; this is the key input for consistency of the surrogate solution.

###### Lemma 5.5 (Uniform convergence of Fourier-RQMC estimators).

Let {𝐯n}n=1N\{\mathbf{v}\_{n}\}\_{n=1}^{N} be a Sobol sequence in [0,1]k[0,1]^{k} with a uniformly bounded gain coefficient.666See [[44](https://arxiv.org/html/2602.06424v1#bib.bib91 "Scrambling Sobol’ and Niederreiter–Xing Points"), Theorem 1].
Fix Sshift=S¯S\_{\mathrm{shift}}=\overline{S}, and for each s=1,…,Sshifts=1,\dots,S\_{\mathrm{shift}} let
{𝐯n(s)}n=1N\{\mathbf{v}\_{n}^{(s)}\}\_{n=1}^{N} be obtained by applying nested uniform scrambling to {𝐯n}n=1N\{\mathbf{v}\_{n}\}\_{n=1}^{N} as in [[43](https://arxiv.org/html/2602.06424v1#bib.bib19 "Randomly Permuted (t,m,s)-Nets and (t, s)-Sequences")].
Then, for each ν∈{0,1,2}\nu\in\{0,1,2\},
the RQMC estimator IN,S¯RQMC​[h~k,p(ν)​(⋅;𝐦k,p)]I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}(\cdot;\mathbf{m}\_{k,p})\right]
satisfies a USLLN on Mk,pM\_{k,p},

|  |  |  |  |
| --- | --- | --- | --- |
| (5.4) |  | sup𝐦k,p∈Mk,p‖IN,S¯RQMC​[h~k,p(ν)​(⋅;𝐦k,p)]−g^k,p(ν),Fou​(𝐦k,p)‖→N→∞a.s.0.\sup\_{\mathbf{m}\_{k,p}\in M\_{k,p}}\left\|I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}(\cdot;\mathbf{m}\_{k,p})\right]-\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}}(\mathbf{m}\_{k,p})\right\|\xrightarrow[\;N\to\infty\;]{\mathrm{a.s.}}0. |  |

###### Proof.

The detailed proof is presented in Appendix [A.2](https://arxiv.org/html/2602.06424v1#A1.SS2 "A.2 Proof for Lemma 5.5 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")
∎

To pass from uniform convergence of the estimators to convergence of the corresponding solution, a stability condition on the underlying F.O.C. system ([2.7](https://arxiv.org/html/2602.06424v1#S2.E7 "In Theorem 2.8 (Theorem 3.4 in [1]). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) is required, which we formalize via the notion of *strong regularity* [[49](https://arxiv.org/html/2602.06424v1#bib.bib50 "Strongly Regular Generalized Equations")] in Definition [5.5](https://arxiv.org/html/2602.06424v1#S5.E5 "In Definition 5.6 (Strong regularity of optimal solution). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

###### Definition 5.6 (Strong regularity of optimal solution).

Suppose that our Fourier-based representation for the true Lagrangian gradient ℒ^∇𝐳Fou​(𝐳)\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}}(\mathbf{z}) is continuously differentiable. We say that a solution 𝐳∗\mathbf{z}^{\*} is strongly regular if there exist neighborhoods U1U\_{1} and U2U\_{2} of 𝟎𝒵\mathbf{0}\_{\mathcal{Z}} and 𝐳∗\mathbf{z^{\*}}, such that for every δ𝐳∈U1\delta\_{\mathbf{z}}\in U\_{1} the linearized equation

|  |  |  |  |
| --- | --- | --- | --- |
| (5.5) |  | δ𝐳+ℒ^∇𝐳Fou​(𝐳∗)+ℒ^∇𝐳2Fou​(𝐳∗)​(𝐳−𝐳∗)=0\delta\_{\mathbf{z}}+\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}}(\mathbf{z^{\*}})+\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}^{2}}^{\mathrm{Fou}}(\mathbf{z^{\*}})\left(\mathbf{z}-\mathbf{z^{\*}}\right)=0 |  |

has a unique solution
in U2U\_{2}, denoted 𝐳~=𝐳~​(δ𝐳)\widetilde{\mathbf{z}}=\widetilde{\mathbf{z}}(\delta\_{\mathbf{z}}), and 𝐳~(.)\widetilde{\mathbf{z}}(.) is Lipschitz continuous on U1U\_{1}.

Next, we state Theorem [5.7](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem7 "Theorem 5.7 (Consistency of solution from Fourier-RQMC problem). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), which establishes the consistency of the Fourier–RQMC solution w.r.t.NN.

###### Theorem 5.7 (Consistency of solution from Fourier-RQMC problem).

Fix Sshift=S¯S\_{\mathrm{shift}}=\overline{S}, and let {𝐯n(s)}n=1N\left\{\mathbf{v}\_{n}^{(s)}\right\}\_{n=1}^{N} be constructed as in Lemma [5.5](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem5 "Lemma 5.5 (Uniform convergence of Fourier-RQMC estimators). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). Suppose that Assumption [A.1](https://arxiv.org/html/2602.06424v1#A1.Thmtheorem1 "Assumption A.1 (Regularity conditions for the exact problem). ‣ A.1 Additional Assumptions for the Error Analysis ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") holds and that the exact solution 𝐳∗\mathbf{z}^{\ast} is strongly regular in the sense of Definition [5.5](https://arxiv.org/html/2602.06424v1#S5.E5 "In Definition 5.6 (Strong regularity of optimal solution). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). 777Under Assumption [A.1](https://arxiv.org/html/2602.06424v1#A1.Thmtheorem1 "Assumption A.1 (Regularity conditions for the exact problem). ‣ A.1 Additional Assumptions for the Error Analysis ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), strong regularity of 𝐳∗\mathbf{z}^{\ast} follows from [[53](https://arxiv.org/html/2602.06424v1#bib.bib49 "The Strong Second-Order Sufficient Condition and Constraint Nondegeneracy in Nonlinear Semidefinite Programming and Their Implications"), Proposition 16]. Then, as N→∞N\to\infty, the Fourier-RQMC problem admits a (locally) unique solution
𝐳N,S¯RQMC,∗∈𝒵{\mathbf{z}}\_{N,\overline{S}}^{\mathrm{RQMC},\*}\in\mathcal{Z} , and
𝐳N,S¯RQMC,∗∈𝒵{\mathbf{z}}\_{N,\overline{S}}^{\mathrm{RQMC},\*}\in\mathcal{Z} , and

|  |  |  |
| --- | --- | --- |
|  | 𝐳N,S¯RQMC,∗→a.s.𝐳∗.{\mathbf{z}}\_{N,\overline{S}}^{\mathrm{RQMC},\*}\xrightarrow[]{\mathrm{a.s.}}\mathbf{z}^{\*}. |  |

###### Proof.

The detailed proof is presented in Appendix [A.3](https://arxiv.org/html/2602.06424v1#A1.SS3 "A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
∎

In RQMC, the CLT for the estimators is obtained by letting the number of i.i.d shifts Sshift→∞S\_{\mathrm{shift}}\to\infty. In the Fourier-RQMC setting for the MSRM problem, the CLT over shifts will describe the fluctuations of 𝐳N,SshiftRQMC,∗\mathbf{z}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*} around 𝐳N,∞RQMC,∗\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*} not the exact solution 𝐳∗\mathbf{z}^{\*}. To express a limiting distribution centered at 𝐳∗\mathbf{z}^{\ast}, we therefore consider the joint regime in which Sshift→∞,N→∞S\_{\mathrm{shift}}\to\infty,N\to\infty, and impose the following assumptions.

###### Assumption 5.8.

1. (i)

   Sshift​Nr​‖𝐳N,∞RQMC,∗−𝐳∗‖→ℙ0\sqrt{S\_{\mathrm{shift}}}N^{r}\,\left\lVert\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}-\mathbf{z}^{\*}\right\rVert\xrightarrow[]{\mathbb{P}}0, as Sshift→∞,N→∞S\_{\mathrm{shift}}\to\infty,N\to\infty .
2. (ii)

   There exists a positive semidefinite matrix 𝑯​(𝐳∗)\boldsymbol{H}(\mathbf{z^{\*}}) such that:

   |  |  |  |
   | --- | --- | --- |
   |  | limN→∞N2​r​VarS​(INRQMC​[ℋ(1)​(𝐯n(s),𝐳∗)])=𝑯​(𝐳∗).\lim\_{N\to\infty}N^{2r}\mathrm{Var}\_{S}\!\left(I\_{N}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}\left(\mathbf{v}\_{n}^{(s)},\mathbf{z}^{\*}\right)\right]\right)=\boldsymbol{H}\!\left(\mathbf{z}^{\*}\right). |  |

with rr is defined in ([4.7](https://arxiv.org/html/2602.06424v1#S4.E7 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

Assumption ([i](https://arxiv.org/html/2602.06424v1#S5.I3.i1 "item i ‣ Assumption 5.8. ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) requires NN to grow sufficiently fast relative to SshiftS\_{\mathrm{shift}}, so the term 𝐳N,∞RQMC,∗−𝐳∗\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}-\mathbf{z}^{\*} is negligible at Sshift​Nr\sqrt{S\_{\mathrm{shift}}}N^{r} scale. Joint growth conditions of this type for many randomization schemes are discussed in detail in [[39](https://arxiv.org/html/2602.06424v1#bib.bib52 "Sufficient Conditions for Central Limit Theorems and Confidence Intervals for Randomized Quasi-Monte Carlo Methods")]. Assumption ([ii](https://arxiv.org/html/2602.06424v1#S5.I3.i2 "item ii ‣ Assumption 5.8. ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) allows us to identify the asymptotic covariance and recenter the CLT at 𝐳∗\mathbf{z}^{\*}.

We now state Theorem [5.9](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem9 "Theorem 5.9 (CLT for the Fourier-RQMC solution). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), which describes the asymptotic behavior of 𝐳N,SshiftRQMC,∗\mathbf{z}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}.

###### Theorem 5.9 (CLT for the Fourier-RQMC solution).

Let {𝐯n(s)}n=1N\left\{\mathbf{v}\_{n}^{(s)}\right\}\_{n=1}^{N} be constructed as in Lemma [5.5](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem5 "Lemma 5.5 (Uniform convergence of Fourier-RQMC estimators). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). Suppose that Assumption [5.8](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem8 "Assumption 5.8. ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") holds. Then, as Sshift→∞,N→∞S\_{\mathrm{shift}}\to\infty,N\to\infty,

|  |  |  |  |
| --- | --- | --- | --- |
| (5.6) |  | Sshift​Nr​(𝐳N,SshiftRQMC,∗−𝐳∗)→law𝒩​(𝟎,𝑽​(𝐳∗)).\sqrt{S\_{\mathrm{shift}}}N^{r}\,\left({\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}-\mathbf{z}^{\*}\right)\xrightarrow{\mathrm{law}}\mathcal{N}\!\left(\mathbf{0},\boldsymbol{V}\left(\mathbf{z}^{\*}\right)\right). |  |

, and the sandwich covariance matrix 𝐕​(𝐳∗)\boldsymbol{V}\left(\mathbf{z}^{\*}\right) is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.7) |  | 𝑽​(𝐳∗):=(ℒ^∇𝐳2Fou​(𝐳∗))−1​𝑯​(𝐳∗)​(ℒ^∇𝐳2Fou​(𝐳∗))−1.\boldsymbol{V}\left(\mathbf{z}^{\*}\right):=\left(\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}^{2}}^{\mathrm{Fou}}\big(\mathbf{z}^{\*}\big)\right)^{-1}\,\boldsymbol{H}\!\left(\mathbf{z}^{\*}\right)\,\left(\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}^{2}}^{\mathrm{Fou}}\big(\mathbf{z}^{\*}\big)\right)^{-1}. |  |

###### Proof.

To prove this theorem, we also need to establish the consistency for the solution w.r.t. SshiftS\_{\mathrm{shift}}, which is mentioned in Proposition [A.4](https://arxiv.org/html/2602.06424v1#A1.Thmtheorem4 "Proposition A.4 (Consistency of solution from Fourier-RQMC problem with 𝑆_shift). ‣ A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). The detailed proof is provided in Appendix [A.4](https://arxiv.org/html/2602.06424v1#A1.SS4 "A.4 Proof for Theorem 5.9 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
∎

Using Theorem [5.9](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem9 "Theorem 5.9 (CLT for the Fourier-RQMC solution). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") together with ([4.7](https://arxiv.org/html/2602.06424v1#S4.E7 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), the statistical error satisfies

|  |  |  |  |
| --- | --- | --- | --- |
| (5.8) |  | εstatRQMC​(N)=𝒪​(N−r).\varepsilon\_{\mathrm{stat}}^{\mathrm{RQMC}}(N)=\mathcal{O}\left(N^{-r}\right). |  |

###### Remark 5.10 (Estimating 𝑽\boldsymbol{V} under digital shift randomization).

In the numerical experiments of Section [4.1](https://arxiv.org/html/2602.06424v1#S4.SS1 "4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), we employ digital shift randomization to compute RQMC estimators. For this randomization, a USLLN w.r.t. NN does not generally hold for Fourier–RQMC estimators; see [[42](https://arxiv.org/html/2602.06424v1#bib.bib53 "A Strong Law of Large Numbers for Scrambled Net Integration")]. Nevertheless, the statistical error and asymptotic variance can still be characterized via a CLT by letting Sshift→∞S\_{\mathrm{shift}}\to\infty. In this setting, the covariance matrix 𝑽\boldsymbol{V} in ([5.7](https://arxiv.org/html/2602.06424v1#S5.E7 "In Theorem 5.9 (CLT for the Fourier-RQMC solution). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) is obtained by replacing 𝐳∗\mathbf{z}^{\*} with 𝐳N,∞RQMC,∗\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*},
ℒ^∇𝐳2Fou​(𝐳∗)\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}^{2}}^{\mathrm{Fou}}\big(\mathbf{z}^{\*}\big)
with
IN,SshiftRQMC​[ℋ(2)​(⋅;𝐳N,∞RQMC,∗)]I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(2)}\big(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)\right], and 𝑯​(𝐳∗)\boldsymbol{H}(\mathbf{z^{\*}}) with 𝑯N,∞RQMC​(⋅;𝐳N,∞RQMC,∗)\boldsymbol{H}\_{N,\infty}^{\mathrm{RQMC}}\left(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\right).
This substitution is justified because a USLLN does hold for Fourier-RQMC estimators w.r.t. SshiftS\_{\mathrm{shift}}; see Lemma [A.3](https://arxiv.org/html/2602.06424v1#A1.Thmtheorem3 "Lemma A.3 (Uniform convergence of Fourier-RQMC estimators with 𝑆_shift). ‣ A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") and Proposition [A.4](https://arxiv.org/html/2602.06424v1#A1.Thmtheorem4 "Proposition A.4 (Consistency of solution from Fourier-RQMC problem with 𝑆_shift). ‣ A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

We conclude with remarks on how to compute the statistical error for single-level RQMC in practice.

###### Remark 5.11 (Estimation of 𝑯​(𝐳∗)\boldsymbol{H}(\mathbf{z}^{\*})).

The true variance w.r.t. the random-shift measure is generally unknown and must be estimated numerically.
A natural estimator is the sample variance of the RQMC estimator,
Var​(IN,SshiftRQMC​[ℋ(1)​(⋅;𝐳∗)]).\mathrm{Var}\!\left(I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\!\left[\mathcal{H}^{(1)}(\cdot;\mathbf{z}^{\*})\right]\right).
This estimator is well defined since, under Assumption [4.1](https://arxiv.org/html/2602.06424v1#S4.Thmtheorem1 "Assumption 4.1 (Square-integrability of transformed integrands). ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), the transformed integrands admit finite second moments. Then, by the LLN applied to the i.i.d shifts ss, we have

|  |  |  |
| --- | --- | --- |
|  | Var​(IN,SshiftRQMC​[ℋ(1)​(⋅;𝐳∗)])→VarS​(INRQMC​[ℋ(1)​(𝐯n(s),𝐳∗)]),\mathrm{Var}\!\left(I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\!\left[\mathcal{H}^{(1)}(\cdot;\mathbf{z}^{\*})\right]\right)\;\xrightarrow[]{}\;\mathrm{Var}\_{S}\!\left(I\_{N}^{\mathrm{RQMC}}\!\left[\mathcal{H}^{(1)}\bigl(\mathbf{v}\_{n}^{(s)},\mathbf{z}^{\*}\bigr)\right]\right), |  |

, as Sshift→∞S\_{\mathrm{shift}}\to\infty.

###### Remark 5.12 (Statistical error of the single-level Fourier–RQMC solution).

We construct a practical plug-in estimator of the asymptotic covariance matrix 𝑽​(𝐳∗)\boldsymbol{V}(\mathbf{z}^{\*}) from two components:888If 𝐳∗\mathbf{z}^{\*} is unavailable, we replace it by the solution returned at the last step of the optimization process 𝐳J,N,SshiftRQMC\mathbf{z}\_{J,N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}.

1. 1.

   *Gradient variance.*
   The variance of the RQMC estimator of the gradient block, Var​(IN,SshiftRQMC​[ℋ(1)​(⋅;𝐳∗)])\mathrm{Var}\!\left(I^{\mathrm{RQMC}}\_{N,S\_{\mathrm{shift}}}\big[\mathcal{H}^{(1)}(\cdot;\mathbf{z}^{\ast})\big]\right) which is estimated using the sample variance over the random digital shifts as described in Remark [5.11](https://arxiv.org/html/2602.06424v1#S5.Ex3 "Remark 5.11 (Estimation of 𝑯⁢(𝐳^∗)). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), with componentwise contributions Var​(IN,SshiftRQMC​[h~(ν)​(⋅;m∗)])\mathrm{Var}\!\big(I^{\mathrm{RQMC}}\_{N,S\_{\mathrm{shift}}}[\widetilde{h}^{(\nu)}(\cdot;m^{\ast})]\big).
2. 2.

   *Hessian approximation.*
   A Fourier–RQMC approximation of the Hessian term
   ℒ^∇z2Fou​(𝐳∗)\widehat{\mathcal{L}}^{\mathrm{Fou}}\_{\nabla\_{z}^{2}}(\mathbf{z}^{\ast}), computed via
   IN,SshiftRQMC​[ℋ(2)​(⋅;𝐳∗)].I^{\mathrm{RQMC}}\_{N,S\_{\mathrm{shift}}}[\mathcal{H}^{(2)}(\cdot;\mathbf{z}^{\ast})].

For the first component, independence of the randomized digital nets across interaction orders
k∈ℐqℓk\in\mathcal{I}\_{q\_{\ell}} implies that variances add across kk, yielding

|  |  |  |
| --- | --- | --- |
|  | Var​(IN,SshiftRQMC​[h~(ν)​(⋅;𝐦∗)])=∑k∈ℐqℓVar​(∑𝐩∈ℐkIN,SshiftRQMC​[h~k,p(ν)​(⋅;𝐦k,p∗)]).\mathrm{Var}\!\left(I^{\mathrm{RQMC}}\_{N,S\_{\mathrm{shift}}}[\widetilde{h}^{(\nu)}(\cdot;\mathbf{m}^{\ast})]\right)=\sum\_{k\in\mathcal{I}\_{q\_{\ell}}}\mathrm{Var}\!\left(\sum\_{\mathbf{p}\in\mathcal{I}\_{k}}I^{\mathrm{RQMC}}\_{N,S\_{\mathrm{shift}}}[\widetilde{h}^{(\nu)}\_{k,p}(\cdot;\mathbf{m}^{\ast}\_{k,p})]\right). |  |

For a fixed interaction order kk, all components 𝐩∈ℐk\mathbf{p}\in\mathcal{I}\_{k} share the same digital net and the same random shifts, and are therefore correlated. Consequently, the variance within each kk expands as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​(∑𝐩∈ℐkIN,SshiftRQMC​[h~k,p(ν)​(⋅;𝐦k,p∗)])\displaystyle\mathrm{Var}\!\left(\sum\_{\mathbf{p}\in\mathcal{I}\_{k}}I^{\mathrm{RQMC}}\_{N,S\_{\mathrm{shift}}}[\widetilde{h}^{(\nu)}\_{k,p}(\cdot;\mathbf{m}^{\ast}\_{k,p})]\right) | =∑p∈ℐkVar​(IN,SshiftRQMC​[h~k,p(ν)​(⋅;𝐦k,p∗)])\displaystyle=\sum\_{p\in\mathcal{I}\_{k}}\mathrm{Var}\!\left(I^{\mathrm{RQMC}}\_{N,S\_{\mathrm{shift}}}[\widetilde{h}^{(\nu)}\_{k,p}(\cdot;\mathbf{m}^{\ast}\_{k,p})]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​∑𝐩,𝐭∈ℐk𝐩<𝐭Cov​(IN,SshiftRQMC​[h~k,p(ν)],IN,SshiftRQMC​[h~k,t(ν)]).\displaystyle\quad+2\!\!\!\sum\_{\begin{subarray}{c}\mathbf{p},\mathbf{t}\in\mathcal{I}\_{k}\\ \mathbf{p}<\mathbf{t}\end{subarray}}\mathrm{Cov}\!\left(I^{\mathrm{RQMC}}\_{N,S\_{\mathrm{shift}}}[\widetilde{h}^{(\nu)}\_{k,p}],\,I^{\mathrm{RQMC}}\_{N,S\_{\mathrm{shift}}}[\widetilde{h}^{(\nu)}\_{k,t}]\right). |  |

Combining the gradient variance estimator in (i) with the Hessian approximation in (ii) yields the plug-in covariance estimator
VN,SshiftRQMC,sing​(⋅;𝐳∗)V^{\mathrm{RQMC,sing}}\_{N,S\_{\mathrm{shift}}}(\cdot;\mathbf{z}^{\ast}).
The resulting statistical error of the single-level Fourier–RQMC solution is then estimated by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.9) |  | εN,SshiftRQMC,sing​(𝐳∗)=CαSshift​‖VN,SshiftRQMC,sing​(⋅;𝐳∗)‖,\varepsilon^{\mathrm{RQMC,sing}}\_{N,S\_{\mathrm{shift}}}(\mathbf{z}^{\ast})=\frac{C\_{\alpha}}{\sqrt{S\_{\mathrm{shift}}}}\sqrt{\left\|V^{\mathrm{RQMC,sing}}\_{N,S\_{\mathrm{shift}}}(\cdot;\mathbf{z}^{\ast})\right\|}, |  |

where CαC\_{\alpha} is defined in ([4.4](https://arxiv.org/html/2602.06424v1#S4.E4 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).
All variances and covariances above are taken with respect to the random digital shifts, conditional on the underlying Sobol base nets.

### 5.3 Computational Complexity

Combining the optimization error bound ([5.3](https://arxiv.org/html/2602.06424v1#S5.E3 "In 5.1 Optimization error ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) with the statistical error rate ([5.8](https://arxiv.org/html/2602.06424v1#S5.E8 "In 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), we now derive the computational complexity of the Fourier–RQMC methods for both single-level and multilevel constructions.

#### 5.3.1 Single-level Fourier-RQMC

We first analyze the computational complexity of the single-level Fourier–RQMC scheme, summarized in Corollary [5.13](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem13 "Corollary 5.13 (Single-level Fourier-RQMC work complexity). ‣ 5.3.1 Single-level Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") below.

###### Corollary 5.13 (Single-level Fourier-RQMC work complexity).

Consider the single-level Fourier-RQMC estimator defined in ([4.3](https://arxiv.org/html/2602.06424v1#S4.E3 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) with NN points and SshiftS\_{\mathrm{shift}} shifts. Let ε\varepsilon denote the target total error and allocate the error budget by enforcing
εstatRQMC​(N)≤ε/2\varepsilon\_{\mathrm{stat}}^{\mathrm{RQMC}}(N)\leq\varepsilon/2 and εopt​(J)≤ε/2\varepsilon\_{\mathrm{opt}}(J)\leq\varepsilon/2.
Choose N=N​(ε)N=N(\varepsilon) accordingly, and J=J​(ε)J=J(\varepsilon) denote the number of optimization iterations. Then the total work satisfies

|  |  |  |  |
| --- | --- | --- | --- |
| (5.10) |  | WsingRQMC​(ε)=𝒪​(ε−1r​log⁡log⁡(1/ε)),W\_{\mathrm{sing}}^{\mathrm{RQMC}}(\varepsilon)=\mathcal{O}\!\left(\varepsilon^{-\tfrac{1}{r}}\,\log\!\log(1/\varepsilon)\right), |  |

where rr is defined in ([4.7](https://arxiv.org/html/2602.06424v1#S4.E7 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

###### Proof.

Appendix [A.5](https://arxiv.org/html/2602.06424v1#A1.SS5 "A.5 Proof for Corrolary 5.13 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") presents the proof.
∎

###### Remark 5.14 (On constants in the single-level work complexity).

The hidden constant in WsingRQMC​(ε)W\_{\mathrm{sing}}^{\mathrm{RQMC}}(\varepsilon) may depend on the decision dimension dd and on the number of component integration problems NcompN\_{\mathrm{comp}}; see Appendix [A.5](https://arxiv.org/html/2602.06424v1#A1.SS5 "A.5 Proof for Corrolary 5.13 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") for the explicit cost decomposition.

We next derive the total work complexity of the multilevel Fourier–RQMC estimator, highlighting its complexity improvements relative to the single-level scheme.

#### 5.3.2 Multilevel Fourier-RQMC

When moving to the multilevel setting (Section [4.2](https://arxiv.org/html/2602.06424v1#S4.SS2 "4.2 Iteration-Indexed Multilevel Fourier–RQMC Approximation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), we allow the sample size to vary across levels, i.e., we use {Nj}j=1J\{N\_{j}\}\_{j=1}^{J} together with SshiftS\_{\mathrm{shift}} shifts at each level jj. As described in Section  [4.2](https://arxiv.org/html/2602.06424v1#S4.SS2 "4.2 Iteration-Indexed Multilevel Fourier–RQMC Approximation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), the multilevel construction couples levels through a shared Sobol base net, while independent shifts are applied across levels. Following Remark [5.2](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem2 "Remark 5.2. ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), to determine {Nj}j=1J\{N\_{j}\}\_{j=1}^{J}, we can solve a preliminary constrained optimization problem in which we minimize the total work complexity subject to achieving the prescribed statistical error at εstatRQMC≤ε/2\varepsilon\_{\mathrm{stat}}^{\mathrm{RQMC}}\leq\varepsilon/2 at final iteration JJ. The resulting work-optimal allocation is stated in Corollary [5.15](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem15 "Corollary 5.15 (Work-optimal multilevel allocation). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

###### Corollary 5.15 (Work-optimal multilevel allocation).

For each level jj, let the smoothness parameter
Amult,j∗A\_{\mathrm{mult},j}^{\*}
correspond to the most singular component among the level-jj difference
integrands Δ​h~k,p(ν,j)\Delta\widetilde{h}\_{k,p}^{(\nu,j)}.
Assume that Amult,j∗=Asing∗A\_{\mathrm{mult},j}^{\*}=A\_{\mathrm{sing}}^{\*} for all j=1,…,Jj=1,\dots,J. Then the work-optimal sample across levels is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.11) |  | Nj∝𝑫j12​r+1​cj−12​r+1,N\_{j}\;\propto\;\boldsymbol{D}\_{j}^{\tfrac{1}{2r+1}}\,c\_{j}^{-\tfrac{1}{2r+1}}, |  |

and the corresponding multilevel computational work scales as

|  |  |  |  |
| --- | --- | --- | --- |
| (5.12) |  | WmultRQMC​(ε)∝S12​r+12​r​ε−1r.W\_{\mathrm{mult}}^{\mathrm{RQMC}}(\varepsilon)\;\propto\;S\_{1}^{\tfrac{2r+1}{2r}}\,\varepsilon^{-\tfrac{1}{r}}. |  |

where rr is defined in ([4.7](https://arxiv.org/html/2602.06424v1#S4.E7 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")),
𝐃j:=‖Var​[INj,SshiftRQMC​[Δ​ℋ(1)​(⋅;𝐳(j),𝐳(j−1))]]‖\boldsymbol{D}\_{j}:=\left\lVert\mathrm{Var}\!\left[I\_{N\_{j},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\mathcal{H}^{(1)}\left(\cdot;\mathbf{z}^{(j)},\mathbf{z}^{(j-1)}\right)\right]\right]\right\rVert999To simplify notation, throughout this section we denote the solution
returned by the Fourier-RQMC problem at iteration jj by
𝐳Nj,Sshift(RQMC,j)≡𝐳(j)\mathbf{z}\_{N\_{j},S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\equiv\mathbf{z}^{(j)}
and 𝐦Nj,Sshift(RQMC,j)≡𝐦(j)\mathbf{m}\_{N\_{j},S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\equiv\mathbf{m}^{(j)}.,
S1:=∑j=1J𝐃j11+2​r​cj2​r1+2​r,S\_{1}:=\sum\_{j=1}^{J}\boldsymbol{D}\_{j}^{\frac{1}{1+2r}}c\_{j}^{\frac{2r}{1+2r}}, and cjc\_{j} is the total cost at level jj.

###### Proof.

Appendix [A.6](https://arxiv.org/html/2602.06424v1#A1.SS6 "A.6 Proof for Corollary 5.15 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") presents the proof.
∎

###### Remark 5.16 (Improved regularity at higher levels).

In practice, the difference integrands often exhibit improved smoothness as jj increases, which corresponds to larger effective rates rjr\_{j} at finer levels. Allowing level-dependent rates in the allocation problem can further improve the constants (and potentially the work) compared to the worst-case bound in Corollary [5.15](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem15 "Corollary 5.15 (Work-optimal multilevel allocation). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"); we keep the uniform-rate assumption here to obtain a closed-form allocation and complexity estimate.

In order to derive a closed-form expression for {Nj}j=1J\{N\_{j}\}\_{j=1}^{J} in Proposition [5.14](https://arxiv.org/html/2602.06424v1#S5.E14 "In Proposition 5.18 (Adaptive choice of the sample size 𝑁_𝑗). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), we impose an additional regularity assumption on the Fourier-RQMC difference surrogates.

###### Assumption 5.17.

For all j≥Jlocj\geq J\_{\mathrm{loc}},
INj,SshiftRQMC​[Δ​ℋ(1)​(⋅;𝐳(j),𝐳(j−1))]I\_{N\_{j},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\!\big[\Delta\mathcal{H}^{(1)}(\cdot;\mathbf{z}^{(j)},\mathbf{z}^{(j-1)})\big]
satisfy a mean-square Lipschitz property w.r.t. the iterates; that is, there exist a constant LH≥0L\_{H}\geq 0 such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖INj,SshiftRQMC​[Δ​ℋ(1)​(⋅;𝐳(j),𝐳(j−1))]‖2]≤LH​𝔼​[‖𝐳(j)−𝐳(j−1)‖2]\mathbb{E}\left[\left\lVert{I}\_{N\_{j},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\mathcal{H}^{(1)}\left(\cdot;\mathbf{z}^{(j)},\mathbf{z}^{(j-1)}\right)\right]\right\rVert^{2}\right]\leq L\_{H}\,\mathbb{E}\left[\left\lVert\mathbf{z}^{(j)}-\mathbf{z}^{(j-1)}\right\rVert^{2}\right] |  |

###### Proposition 5.18 (Adaptive choice of the sample size NjN\_{j}).

Let JlocJ\_{\mathrm{loc}} denote the iteration index at which the SQP iterates enter
their *local convergence region*. Suppose that Assumption [5.17](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem17 "Assumption 5.17. ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") holds; then the sample size at iteration jj can be chosen as

|  |  |  |  |
| --- | --- | --- | --- |
| (5.13) |  | Nj=max⁡{N1​ 1{j<Jloc}+Cloc,j−1​N1​η~j−122​r+1​ 1{j≥Jloc},Nmin},N\_{j}=\max\!\left\{N\_{1}\,\mathbf{1}\_{\{j<J\_{\mathrm{loc}}\}}+C\_{\mathrm{loc},j-1}\,N\_{1}\,\widetilde{\eta}\_{j-1}^{\frac{2}{2r+1}}\,\mathbf{1}\_{\{j\geq J\_{\mathrm{loc}}\}},\;N\_{\min}\right\}, |  |

where N1N\_{1} denotes the initial number of QMC points,
NminN\_{\min} is a prescribed minimal sample size,
Cloc,j−1>0C\_{\mathrm{loc},j-1}>0 is a level-dependent constant, and
η~j−1→0\widetilde{\eta}\_{j-1}\to 0 as j→∞j\to\infty.

If we make the local convergence rate constant
η~j−1=η∈(0,1)\widetilde{\eta}\_{j-1}=\eta\in(0,1) for all j≥Jlocj\geq J\_{\mathrm{loc}},
the allocation ([5.13](https://arxiv.org/html/2602.06424v1#S5.E13 "In Proposition 5.18 (Adaptive choice of the sample size 𝑁_𝑗). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) reduces to

|  |  |  |  |
| --- | --- | --- | --- |
| (5.14) |  | Nj=max⁡{N1​ 1{j<Jloc}+Cloc​N1​η2​(j−1−Jloc)2​r+1​ 1{j≥Jloc},Nmin}.N\_{j}=\max\!\left\{N\_{1}\,\mathbf{1}\_{\{j<J\_{\mathrm{loc}}\}}+C\_{\mathrm{loc}}\,N\_{1}\,\eta^{\frac{2(j-1-J\_{\mathrm{loc}})}{2r+1}}\,\mathbf{1}\_{\{j\geq J\_{\mathrm{loc}}\}},\;N\_{\min}\right\}. |  |

###### Proof.

Proof for Proposition [5.14](https://arxiv.org/html/2602.06424v1#S5.E14 "In Proposition 5.18 (Adaptive choice of the sample size 𝑁_𝑗). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") is presented in Appendix [A.7](https://arxiv.org/html/2602.06424v1#A1.SS7 "A.7 Proof for Proposition 5.14 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
∎

###### Remark 5.19 (Choice of Sobol points).

Since Sobol sequences exhibit their best performance when the number of points is a power of two [[52](https://arxiv.org/html/2602.06424v1#bib.bib67 "Construction and Comparison of High-Dimensional Sobol’ Generators")], in our numerical experiments we select,

|  |  |  |
| --- | --- | --- |
|  | Nj≈ 2⌊log2⁡(Cloc​N1​η2​(j−1−Jloc)2​r+1)⌋,N\_{j}\;\approx\;2^{\left\lfloor\log\_{2}\!\left(C\_{\mathrm{loc}}\,N\_{1}\,\eta^{\frac{2(j-1-J\_{\mathrm{loc}})}{2r+1}}\right)\right\rfloor}, |  |

i.e., the nearest power of two to Cloc​N1​η2​(j−1)r+1C\_{\mathrm{loc}}N\_{1}\eta^{\frac{2(j-1)}{r+1}}, and
likewise choose NminN\_{\min} as a power of two.

Under the multilevel sampling design described above, we now derive the asymptotic computational complexity.

###### Proposition 5.20 (Computational Complexity for multilevel Fourier-RQMC).

Assume that the per-iteration cost of multilevel Fourier-RQMC is level-independent, i.e.,
cj≈cc\_{j}\approx c for all jj where cc denotes the per-iteration cost of the single-level RQMC.
Assume further ηj≈η\eta\_{j}\approx\eta within the local convergence region j≥Jlocj\geq J\_{\mathrm{loc}},
then

|  |  |  |  |
| --- | --- | --- | --- |
| (5.15) |  | WsingRQMC​(ε)WmultRQMC​(ε)=𝒪​(J).\frac{W^{\mathrm{RQMC}}\_{\mathrm{sing}}(\varepsilon)}{W^{\mathrm{RQMC}}\_{\mathrm{mult}}(\varepsilon)}=\mathcal{O}(J). |  |

Moreover, the total computational cost of the multilevel Fourier-RQMC method satisfies

|  |  |  |  |
| --- | --- | --- | --- |
| (5.16) |  | Wmult​(ε)=𝒪​(ε−1r),W\_{\mathrm{mult}}(\varepsilon)=\mathcal{O}\!\left(\varepsilon^{-\tfrac{1}{r}}\right), |  |

where r=1−Asing∗−ςr=1-A\_{\mathrm{sing}}^{\*}-\varsigma.

###### Proof.

Proof for Proposition [5.20](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem20 "Proposition 5.20 (Computational Complexity for multilevel Fourier-RQMC). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") is presented in Appendix [A.8](https://arxiv.org/html/2602.06424v1#A1.SS8 "A.8 Proof for Proposition 5.20 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
∎

###### Remark 5.21 (On constants in the multilevel work complexity).

From Proposition [5.20](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem20 "Proposition 5.20 (Computational Complexity for multilevel Fourier-RQMC). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), the total multilevel computational work is, asymptotically, reduced by a factor proportional to the number of optimization iterations JJ when compared with the total single-level work. Beyond this asymptotic gain, the leading constant in the multilevel work complexity can be further improved in practice because the difference integrands typically exhibit substantially smaller variance than the original integrands, which reduces the variance prefactors DjD\_{j} entering the multilevel allocation and hence lowers the overall computational cost. These constant-level improvements are not captured by the worst-case bounds in Proposition [5.20](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem20 "Proposition 5.20 (Computational Complexity for multilevel Fourier-RQMC). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") but are consistently observed in numerical experiments in Section [6](https://arxiv.org/html/2602.06424v1#S6 "6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

###### Remark 5.22 (Statistical error of multilevel Fourier-RQMC solution).

In the multilevel setting, the variance Var​(IN,SshiftRQMC​[h~(ν)​(⋅;𝐦∗)])\mathrm{Var}\left(I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\widetilde{h}^{(\nu)}\left(\cdot;\mathbf{m}^{\*}\right)\right]\right) is decomposed as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (5.17) |  | Var(IN,SshiftRQMC[h~(ν)(;𝐦∗)])\displaystyle\mathrm{Var}\!\left(I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\Big[\widetilde{h}^{(\nu)}(;\mathbf{m}^{\*})\Big]\right) | =Var​(IN1,SshiftRQMC​[h~(ν)​(⋅;𝐦(RQMC,1))])\displaystyle=\mathrm{Var}\!\left(I\_{N\_{1},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\Big[\widetilde{h}^{(\nu)}\big(\cdot;\mathbf{m}^{(\mathrm{RQMC},1)}\big)\Big]\right) |  |
|  |  | +∑j=2JVar​(INj,SshiftRQMC​[Δ​h~(ν)​(⋅;𝐦(RQMC,j),𝐦(RQMC,j−1))]).\displaystyle\quad+\sum\_{j=2}^{J}\mathrm{Var}\!\left(I\_{N\_{j},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\Big[\Delta\widetilde{h}^{(\nu)}\big(\cdot;\mathbf{m}^{(\mathrm{RQMC},j)},\mathbf{m}^{(\mathrm{RQMC},j-1)}\big)\Big]\right). |  |

Since independent shifts are generated at each level jj, the level-wise variances are estimated separately, using the same *Gradient variance* estimator as in Remark [5.12](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem12 "Remark 5.12 (Statistical error of the single-level Fourier–RQMC solution). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). For levels j≥2j\geq 2, the estimator is applied to the difference integrands Δ​h~(ν)\Delta\widetilde{h}^{(\nu)} (componentwise, Δ​h~k,p(ν)\Delta\widetilde{h}\_{k,p}^{(\nu)}). Combining ([5.17](https://arxiv.org/html/2602.06424v1#S5.E17 "In Remark 5.22 (Statistical error of multilevel Fourier-RQMC solution). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) with Remark [5.12](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem12 "Remark 5.12 (Statistical error of the single-level Fourier–RQMC solution). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") yields an estimator 𝑽N,SshiftRQMC,mult​(⋅;𝐳∗)\boldsymbol{V}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC,mult}}(\cdot;\mathbf{z}^{\*}) of 𝑽​(𝐳∗)\boldsymbol{V}(\mathbf{z}^{\*}), and the corresponding statistical error of the solution is

|  |  |  |  |
| --- | --- | --- | --- |
| (5.18) |  | εN,SshiftRQMC,mult​(𝐳∗)=CαSshift​‖𝑽N,SshiftRQMC,mult​(⋅;𝐳∗)‖.\varepsilon\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC,mult}}(\mathbf{z}^{\*})=\frac{C\_{\alpha}}{\sqrt{S\_{\mathrm{shift}}}}\,\sqrt{\left\lVert\boldsymbol{V}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC,mult}}(\cdot;\mathbf{z}^{\*})\right\rVert}. |  |

with CαC\_{\alpha} is defined in ([4.4](https://arxiv.org/html/2602.06424v1#S4.E4 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

## 6 Numerical Experiments and Results

In this section, we evaluate the performance of the proposed Fourier–RQMC methods for the MSRM problem on three representative test cases: an exponential loss under a bivariate Gaussian model (see Section [6.1](https://arxiv.org/html/2602.06424v1#S6.SS1 "6.1 Exponential Loss with Two-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) and a QPC loss under both a 10D Gaussian model (see Section [6.2](https://arxiv.org/html/2602.06424v1#S6.SS2 "6.2 QPC Loss with Ten-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) and a 3D NIG model (see Section [6.3](https://arxiv.org/html/2602.06424v1#S6.SS3 "6.3 QPC Loss with Three-Dimensional NIG Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). The component-wise Fourier transforms for given loss functions are derived in Appendix [E.2](https://arxiv.org/html/2602.06424v1#A5.SS2 "E.2 Fourier transform of the given loss functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). For the loss vector 𝐗\mathbf{X}, Gaussian parameter sets are taken from [[1](https://arxiv.org/html/2602.06424v1#bib.bib204 "Multivariate Shortfall Risk Allocation and Systemic Risk")] and NIG parameter sets from [[32](https://arxiv.org/html/2602.06424v1#bib.bib201 "Multivariate Optimized Certainty Equivalent Risk Measures and their Numerical Computation")], and the corresponding component CFs are computed using the formulas in Appendix [E.3](https://arxiv.org/html/2602.06424v1#A5.SS3 "E.3 Loss vector distributions and extended characteristic functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

For the numerical implementation, the optimization error is determined by the numerical optimization solver (SLSQP).101010In all experiments, we control the deterministic optimization error through the SLSQP stopping tolerance ftol, denoted ftolf\_{\mathrm{tol}}. Since ftol bounds several stopping criteria, we heuristically model the resulting optimization error as εopt≈ftol 2\varepsilon\_{\mathrm{opt}}\approx f\_{\mathrm{tol}}^{\,2}, consistent with the local superlinear regime in Theorem [5.2](https://arxiv.org/html/2602.06424v1#S5.E2 "In Theorem 5.3. ‣ 5.1 Optimization error ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
The statistical error of the solution is quantified as follows:
(i) for single-level Fourier-RQMC, we use ([5.9](https://arxiv.org/html/2602.06424v1#S5.E9 "In Remark 5.12 (Statistical error of the single-level Fourier–RQMC solution). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"));
(ii) for multilevel Fourier-RQMC, we use ([5.18](https://arxiv.org/html/2602.06424v1#S5.E18 "In Remark 5.22 (Statistical error of multilevel Fourier-RQMC solution). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"));
(iii) for SAA, we use ([D.4](https://arxiv.org/html/2602.06424v1#A4.E4 "In Appendix D Convergence analysis for the SAA method ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).
In all cases, we report the statistical error using the maximum diagonal norm ∥⋅∥diag,∞\|\cdot\|\_{\mathrm{diag},\infty} 111111For a matrix 𝑨∈ℝd×d\boldsymbol{A}\in\mathbb{R}^{d\times d}, the maximum diagonal norm is defined as
‖𝑨‖diag,∞:=max1≤i≤d⁡|Ai​i|.\|\boldsymbol{A}\|\_{\mathrm{diag},\infty}:=\max\_{1\leq i\leq d}|A\_{ii}|.
, and choose Cα=1.96C\_{\alpha}=1.96 for 95% confidence level. For method comparison, we also report the relative statistical error

|  |  |  |  |
| --- | --- | --- | --- |
| (6.1) |  | εstat,rel:=εstat‖𝐳ref‖∞,\varepsilon\_{\mathrm{stat,rel}}:=\frac{\varepsilon\_{\mathrm{stat}}}{\|\mathbf{z}^{\mathrm{ref}}\|\_{\infty}}, |  |

where 𝐳ref:=(𝐦ref,λref)\mathbf{z}^{\mathrm{ref}}:=\left(\mathbf{m}^{\mathrm{ref}},\lambda^{\mathrm{ref}}\right) denotes a reference solution (available in closed form when possible, or otherwise approximated by SAA with N=108N=10^{8} samples, where the reference is taken as the final solution returned by the solver using an optimization tolerance εopt=10−6\varepsilon\_{\mathrm{opt}}=10^{-6}).

Reported computational times exclude the cost of estimating statistical errors and account solely for the runtime of the optimization procedures. All experiments were conducted using Python 3.13.2 on a MacBook Pro with an Apple M4 Pro.

### 6.1 Exponential Loss with Two-Dimensional Gaussian Loss Vector

In this section, we test the Fourier-RQMC method using the exponential loss function from [[33](https://arxiv.org/html/2602.06424v1#bib.bib203 "Estimation of Systemic Shortfall Risk Measure Using Stochastic Algorithms")], defined in ([2.2](https://arxiv.org/html/2602.06424v1#S2.E2 "In item (i) ‣ Example 2.3. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), with α=1\alpha=1 and β=1\beta=1. We consider a bivariate Gaussian loss vector with mean 𝝁=(0,0)⊤\boldsymbol{\mu}=(0,0)^{\top} and 𝚺=(1ρρ1)\boldsymbol{\Sigma}=\begin{pmatrix}1&\rho\\
\rho&1\end{pmatrix}, where ρ∈{−0.5, 0.5}\rho\in\{-0.5,\,0.5\}. In this setting, the optimal allocation 𝐦∗\mathbf{m}^{\*} admits a closed-form expression and is symmetric, i.e., m1∗=m2∗m\_{1}^{\*}=m\_{2}^{\*} (see [[33](https://arxiv.org/html/2602.06424v1#bib.bib203 "Estimation of Systemic Shortfall Risk Measure Using Stochastic Algorithms"), Lemma 3.1]). Table [6.1](https://arxiv.org/html/2602.06424v1#S6.T1 "Table 6.1 ‣ 6.1 Exponential Loss with Two-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") reports this closed-form solution together with the single-level Fourier-RQMC estimate and its 95%95\% confidence interval (CI).

|  |  |  |
| --- | --- | --- |
| ρ\rho | m1∗=m2∗m\_{1}^{\*}=m\_{2}^{\*} | CI for m1(=m2)m\_{1}(=m\_{2}) |
| −0.5-0.5 | 0.38680.3868 | [0.38688, 0.38690][0.38688,\,0.38690] |
| 0.50.5 | 0.63640.6364 | [0.63645, 0.63647][0.63645,\,0.63647] |

Table 6.1: Exact optimal allocations and 95% CI from single-level Fourier–RQMC (N=2048N=2048, Sshift=32S\_{\mathrm{shift}}=32).

We see the convergence of the Fourier-RQMC solution at order 10−410^{-4} to the exact solution from Table [6.1](https://arxiv.org/html/2602.06424v1#S6.T1 "Table 6.1 ‣ 6.1 Exponential Loss with Two-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), and this is further supported by the convergence plot shown in Figure [6.1](https://arxiv.org/html/2602.06424v1#S6.F1 "Figure 6.1 ‣ 6.1 Exponential Loss with Two-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), where the local superlinear convergence of the optimization solver is observed.

![Refer to caption](x12.png)

![Refer to caption](x13.png)

Figure 6.1: Exponential loss with a two-dimensional Gaussian loss vector: convergence of the single-level Fourier–RQMC iterate m(j)m^{(j)} to the exact solution m∗m^{\*} for ρ=−0.5\rho=-0.5 (left) and ρ=0.5\rho=0.5 (right).

Next, we choose the optimization tolerance εopt\varepsilon\_{\mathrm{opt}} sufficiently small relative to εstat\varepsilon\_{\mathrm{stat}}, so that the observed error is dominated by the statistical component. This allows us to directly assess the rate of convergence of the statistical error as a function of the total sampling budget B for single-level Fourier–RQMC and SAA. Figure [6.2](https://arxiv.org/html/2602.06424v1#S6.F2 "Figure 6.2 ‣ 6.1 Exponential Loss with Two-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") shows that, for any prescribed relative statistical tolerance εstat,rel\varepsilon\_{\mathrm{stat,rel}}, single-level Fourier–RQMC achieves the target accuracy with a substantially smaller budget than SAA, with the performance gap widening as εstat,rel\varepsilon\_{\mathrm{stat,rel}} decreases. The empirical convergence rates for Fourier–RQMC, estimated as r=1.49r=1.49 for ρ=−0.5\rho=-0.5 and r=1.29r=1.29 for ρ=0.5\rho=0.5, are significantly higher than the
rate r=1/2r=1/2 observed for SAA. While these empirical rates are faster than the asymptotic rate in ([4.7](https://arxiv.org/html/2602.06424v1#S4.E7 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), they are consistent with Remark [4.2](https://arxiv.org/html/2602.06424v1#S4.Thmtheorem2 "Remark 4.2. ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") and can be attributed to the domain transformation introduced in Section [4.1.1](https://arxiv.org/html/2602.06424v1#S4.SS1.SSS1 "4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), which mitigates boundary-induced oscillations and enhances the effective smoothness of the integrand.

![Refer to caption](x14.png)

![Refer to caption](x15.png)

Figure 6.2: Exponential loss with a two-dimensional Gaussian loss vector: relative statistical error εstat,rel\varepsilon\_{\mathrm{stat,rel}} versus total sampling budget BB for SAA and single-level Fourier–RQMC, with ρ=−0.5\rho=-0.5 (left) and ρ=0.5\rho=0.5 (right). Here BSAA=NB\_{\mathrm{SAA}}=N and BRQMC=N​SshiftB\_{\mathrm{RQMC}}=NS\_{\mathrm{shift}}.

To further assess the computational performance of the Fourier–RQMC methods, we compare the average computational time required to reach a prescribed relative total error εrel\varepsilon\_{\mathrm{rel}} against SAA and stochastic approximation (SA). For SA, we follow [[33](https://arxiv.org/html/2602.06424v1#bib.bib203 "Estimation of Systemic Shortfall Risk Measure Using Stochastic Algorithms")] and employ the constrained Robbins–Monro scheme with parameters (c,t,γ)=(2,10,0.7)(c,t,\gamma)=(2,10,0.7), combined with Polyak–Ruppert averaging to estimate the statistical error εstat\varepsilon\_{\mathrm{stat}}. The corresponding relative error εstat,rel\varepsilon\_{\mathrm{stat,rel}} is computed via ([6.1](https://arxiv.org/html/2602.06424v1#S6.E1 "In 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). Figure [6.3](https://arxiv.org/html/2602.06424v1#S6.F3 "Figure 6.3 ‣ 6.1 Exponential Loss with Two-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") reports the average runtime required to achieve a given εrel\varepsilon\_{\mathrm{rel}}, using the splitting strategy εopt=εstat=ε/2\varepsilon\_{\mathrm{opt}}=\varepsilon\_{\mathrm{stat}}=\varepsilon/2. 121212εstat\varepsilon\_{\mathrm{stat}} is not enforced *a priori*. We first run the optimizer with a coarse surrogate, targeting εopt≤ε/2\varepsilon\_{\mathrm{opt}}\leq\varepsilon/2, to obtain a rough solution estimate. We then refine the sample sizes so that εstat≤ε/2\varepsilon\_{\mathrm{stat}}\leq\varepsilon/2. For SA, since no explicit optimization error is available, we directly report the runtime to reach εrel\varepsilon\_{\mathrm{rel}}.

Across both correlation settings, single-level Fourier–RQMC consistently outperforms both SAA and SA in terms of numerical complexity, exhibiting improved complexity rates that closely match the theoretical analysis of Section [5](https://arxiv.org/html/2602.06424v1#S5 "5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). In particular, for relative tolerances of order 10−410^{-4}, Fourier–RQMC attains the target accuracy with approximately 10410^{4} times fewer samples than SAA and up to 10610^{6} times fewer samples than SA. Finally, the multilevel variant provides only a limited additional improvement in this setting, which is consistent with the fact that only a small number of iterations (approximately 2​–​32\text{--}3) are spent in the local convergence regime.

![Refer to caption](x16.png)

![Refer to caption](x17.png)

Figure 6.3: Exponential loss with a two-dimensional Gaussian loss vector: average runtime (seconds) versus prescribed relative total tolerance εrel\varepsilon\_{\mathrm{rel}} for ρ=−0.5\rho=-0.5 (left) and ρ=0.5\rho=0.5 (right).

As shown in Figure [6.3](https://arxiv.org/html/2602.06424v1#S6.F3 "Figure 6.3 ‣ 6.1 Exponential Loss with Two-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), the SA method is consistently less efficient than the other approaches, in line with the findings of [[33](https://arxiv.org/html/2602.06424v1#bib.bib203 "Estimation of Systemic Shortfall Risk Measure Using Stochastic Algorithms")]. We therefore omit SA as a baseline in the subsequent numerical experiments.

### 6.2 QPC Loss with Ten-Dimensional Gaussian Loss Vector

We now consider the QPC loss defined in ([2.3](https://arxiv.org/html/2602.06424v1#S2.E3 "In item (ii) ‣ Example 2.3. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) with α=1\alpha=1, applied to a 10-dimensional Gaussian loss vector as in [[1](https://arxiv.org/html/2602.06424v1#bib.bib204 "Multivariate Shortfall Risk Allocation and Systemic Risk")], with mean 𝝁=(0,…,0)⊤\boldsymbol{\mu}=(0,\dots,0)^{\top} and covariance matrix

|  |  |  |
| --- | --- | --- |
|  | 𝚺=(2.110.37−0.42⋯−0.940.371.78−0.45⋯−0.48⋮⋮⋱⋮⋮−0.94−0.480.45⋯0.88).\boldsymbol{\Sigma}=\begin{pmatrix}2.11&0.37&-0.42&\cdots&-0.94\\ 0.37&1.78&-0.45&\cdots&-0.48\\ \vdots&\vdots&\ddots&\vdots&\vdots\\ -0.94&-0.48&0.45&\cdots&0.88\end{pmatrix}. |  |

Since no closed-form solution is available for this loss setting, we compute a reference solution using SAA, as described at the beginning of Section [6](https://arxiv.org/html/2602.06424v1#S6 "6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

The right panel of Figure [6.4](https://arxiv.org/html/2602.06424v1#S6.F4 "Figure 6.4 ‣ 6.2 QPC Loss with Ten-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") shows that single-level Fourier–RQMC remains up to two orders of magnitude more efficient than SAA for achieving a relative error of order 10−310^{-3}. Moreover, the computational advantage of the multilevel estimator over the single-level Fourier–RQMC becomes more pronounced in this regime. For the prescribed tolerance εrel\varepsilon\_{\mathrm{rel}}, the optimizer typically requires approximately 8​–​128\text{--}12 iterations and enters the local convergence regime after roughly 4​–​64\text{--}6 iterations. Within this regime, the multilevel estimator achieves substantial variance reduction for the component integrands, leading to a lower per-iteration computational cost (see the left panel of Figure [6.4](https://arxiv.org/html/2602.06424v1#S6.F4 "Figure 6.4 ‣ 6.2 QPC Loss with Ten-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) and an improved asymptotic complexity compared with the single-level method, in agreement with the analysis in Section [5.3](https://arxiv.org/html/2602.06424v1#S5.SS3 "5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). Nevertheless, the overall computational gain of the multilevel approach remains limited, since independent random shifts must be generated at each level, whereas the single-level method draws random shifts only once at initialization (see Algorithms [3](https://arxiv.org/html/2602.06424v1#alg3 "Algorithm 3 ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") and [4](https://arxiv.org/html/2602.06424v1#alg4 "Algorithm 4 ‣ 4.2 Iteration-Indexed Multilevel Fourier–RQMC Approximation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

![Refer to caption](x18.png)

![Refer to caption](x19.png)

Figure 6.4: QPC loss with a ten-dimensional Gaussian loss vector:
(Left): Estimated variance across shifts of the estimator of m5m\_{5} over optimization iterations.
(Right): Average runtime in seconds w.r.t. prescribed relative total tolerance εrel\varepsilon\_{\mathrm{rel}} .

### 6.3 QPC Loss with Three-Dimensional NIG Loss Vector

We next assess the performance of the Fourier–RQMC methods for the same QPC loss under a heavier-tailed distribution for the loss vector 𝐗\mathbf{X}, namely a three-dimensional NIG distribution. Specifically, we consider 𝐗∼𝒩​ℐ​𝒢​(α,𝜷,δ,𝝁,𝚪)\mathbf{X}\sim\mathcal{NIG}(\alpha,\boldsymbol{\beta},\delta,\boldsymbol{\mu},\boldsymbol{\Gamma}), with parameters from [[32](https://arxiv.org/html/2602.06424v1#bib.bib201 "Multivariate Optimized Certainty Equivalent Risk Measures and their Numerical Computation")]

|  |  |  |
| --- | --- | --- |
|  | α=365.78,δ=0.373,𝜽=(2,2,2)⊤,𝝁=(0.00084,0.00024,0.00055)⊤,𝜷=(−64.27,41.45,7.35)⊤\alpha=365.78,\;\delta=0.373,\;\boldsymbol{\theta}=(2,2,2)^{\top},\;\boldsymbol{\mu}=(0.00084,0.00024,0.00055)^{\top},\;\boldsymbol{\beta}=(-64.27,41.45,7.35)^{\top} |  |

and covariance matrix

|  |  |  |
| --- | --- | --- |
|  | 𝚪=(2.3381.7962.0801.7962.3272.0882.0802.0882.555).\boldsymbol{\Gamma}=\begin{pmatrix}2.338&1.796&2.080\\ 1.796&2.327&2.088\\ 2.080&2.088&2.555\end{pmatrix}. |  |

In this NIG setting, boundary-induced oscillations in the transformed integrands become more pronounced, as discussed in Section [4.1.1](https://arxiv.org/html/2602.06424v1#S4.SS1.SSS1 "4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). As a consequence, the choice of the scaling parameter cc for single-level Fourier–RQMC becomes critical: inappropriate values can significantly degrade both numerical stability and optimization performance. In contrast, the multilevel Fourier–RQMC estimator partially mitigates these oscillatory effects by operating on the difference integrands, which tend to cancel boundary oscillations across successive optimization iterates. This behavior is illustrated in Figure [6.5](https://arxiv.org/html/2602.06424v1#S6.F5 "Figure 6.5 ‣ 6.3 QPC Loss with Three-Dimensional NIG Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), where the difference integrands exhibit markedly reduced oscillations compared with the corresponding single-level integrands, leading to a more favorable variance structure and improved numerical robustness, implying more significant computation gain of the multilevel method over the single-level one compared to the previous examples.

Compared with the Gaussian examples in Sections [6.1](https://arxiv.org/html/2602.06424v1#S6.SS1 "6.1 Exponential Loss with Two-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")-[6.2](https://arxiv.org/html/2602.06424v1#S6.SS2 "6.2 QPC Loss with Ten-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), the component integrands under the NIG model are less smooth. Accordingly, the numerical complexity rate deteriorates relative to the Gaussian case but remain close to the asymptotic rate predicted in ([4.7](https://arxiv.org/html/2602.06424v1#S4.E7 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), namely r≈1r\approx 1. Despite this reduced smoothness, the right panel of Figure [6.6](https://arxiv.org/html/2602.06424v1#S6.F6 "Figure 6.6 ‣ 6.3 QPC Loss with Three-Dimensional NIG Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") shows that Fourier–RQMC methods continue to substantially outperform SAA in terms of computational complexity. For instance, at a relative tolerance of order 10−110^{-1}, Fourier–RQMC methods achieves the prescribed accuracy with a computational cost approximately 10510^{5} times smaller than that of SAA.

This significant gain can be attributed to two complementary effects. First, the variance of the estimators is evaluated in Fourier space using RQMC, which appears to be significantly less sensitive to rare-event contributions of the gradient terms than MC estimators in physical space when using SAA, leading to smaller constants. Second, the method requires the numerical inversion of the Hessian matrix ∇𝐳2ℒ​(ℒ^∇𝐳2Fou)\nabla\_{\mathbf{z}}^{2}\mathcal{L}\left(\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}^{2}}^{\mathrm{Fou}}\right) at the final iteration JJ. When this Hessian is estimated in physical space using MC, it may become poorly conditioned, causing the associated error constants to grow excessively. In contrast, within the Fourier–RQMC framework, the Hessian is evaluated in Fourier space, where the transformed integrands exhibit increased smoothness. This additional regularity results in improved numerical conditioning of the Hessian matrix and, consequently, more stable error constants, as clearly observed in the left panel of Figure [6.6](https://arxiv.org/html/2602.06424v1#S6.F6 "Figure 6.6 ‣ 6.3 QPC Loss with Three-Dimensional NIG Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

![Refer to caption](x20.png)


(a) c=44.

![Refer to caption](x21.png)


(b) c=10c=10.

Figure 6.5: QPC loss with a three-dimensional NIG loss vector: Transformed integrand component h~1,2(1)\widetilde{h}\_{1,2}^{(1)} (solid) and the corresponding difference integrand arising in the multilevel construction (dashed) across successive optimization iterations with different scaling cc.



![Refer to caption](x22.png)

![Refer to caption](x23.png)

Figure 6.6: QPC loss with a three-dimensional NIG loss vector: (left) spectral condition number κ​(∇z2ℒ^​(z(J)))\kappa(\nabla\_{z}^{2}\widehat{\mathcal{L}}(z^{(J)})) at the final iterate JJ; (right) average runtime (seconds) versus prescribed relative total tolerance εrel\varepsilon\_{\mathrm{rel}}.

## References Cited

* [1]
  Y. Armenti, S. Crépey, S. Drapeau, and A. Papapantoleon (2018-01)
  Multivariate Shortfall Risk Allocation and Systemic Risk.
  SIAM Journal on Financial Mathematics 9 (1),  pp. 90–126 (en).
  External Links: ISSN 1945-497X,
  [Link](https://epubs.siam.org/doi/10.1137/16M1087357),
  [Document](https://dx.doi.org/10.1137/16M1087357)
  Cited by: [§1](https://arxiv.org/html/2602.06424v1#S1.p3.1 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§1](https://arxiv.org/html/2602.06424v1#S1.p4.4 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§1](https://arxiv.org/html/2602.06424v1#S1.p5.1 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§1](https://arxiv.org/html/2602.06424v1#S1.p7.1 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§2](https://arxiv.org/html/2602.06424v1#S2.1.p1.4 "Proof. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [Remark 2.10](https://arxiv.org/html/2602.06424v1#S2.Thmtheorem10.p1.1 "Remark 2.10. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [Theorem 2.8](https://arxiv.org/html/2602.06424v1#S2.Thmtheorem8 "Theorem 2.8 (Theorem 3.4 in [1]). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§2](https://arxiv.org/html/2602.06424v1#S2.p5.1 "2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§2](https://arxiv.org/html/2602.06424v1#S2.p9.11 "2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§6.2](https://arxiv.org/html/2602.06424v1#S6.SS2.p1.2 "6.2 QPC Loss with Ten-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§6](https://arxiv.org/html/2602.06424v1#S6.p1.1 "6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [footnote 2](https://arxiv.org/html/2602.06424v1#footnote2 "In Example 2.3. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [footnote 3](https://arxiv.org/html/2602.06424v1#footnote3 "In Assumption 2.4 (Integrability of the loss vector). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [2]
  O. A. Bardou, N. N. Frikha, and G. Pagès (2009)
  Computing VaR and CVaR using Stochastic Approximation and Adaptive Unconstrained Importance Sampling.
  Monte Carlo Methods and Applications 15 (3),  pp. 173–210.
  Cited by: [§1](https://arxiv.org/html/2602.06424v1#S1.p4.4 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [3]
  O. Bardou, N. Frikha, and G. Pagès (2009)
  Recursive Computation of Value-at-Risk and Conditional Value-at-Risk using MC and QMC.
  In Monte Carlo and Quasi-Monte Carlo Methods 2008,
   pp. 193–208 (en).
  External Links: ISBN 978-3-642-04106-8 978-3-642-04107-5,
  [Link](https://link.springer.com/10.1007/978-3-642-04107-5_11)
  Cited by: [§1](https://arxiv.org/html/2602.06424v1#S1.p6.1 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [4]
  C. Bayer, C. Ben Hammouda, A. Papapantoleon, M. Samet, and R. Tempone (2025-04)
  Quasi-Monte Carlo with Domain Transformation for Efficient Fourier Pricing of Multi-Asset Options.
   arXiv.
  Note: arXiv:2403.02832 [q-fin]
  External Links: [Link](http://arxiv.org/abs/2403.02832),
  [Document](https://dx.doi.org/10.48550/arXiv.2403.02832)
  Cited by: [§C.1.2](https://arxiv.org/html/2602.06424v1#A3.SS1.SSS2.Px1.p2.2 "The Gaussian case. ‣ C.1.2 Choice of matrix 𝚺̃_{𝑘,𝑝} ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§C.1.2](https://arxiv.org/html/2602.06424v1#A3.SS1.SSS2.Px2.p1.6 "The NIG case. ‣ C.1.2 Choice of matrix 𝚺̃_{𝑘,𝑝} ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [5th item](https://arxiv.org/html/2602.06424v1#S1.I1.i5.p1.1 "In Our contributions. ‣ 1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§3](https://arxiv.org/html/2602.06424v1#S3.p1.1 "3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§4.1.1](https://arxiv.org/html/2602.06424v1#S4.SS1.SSS1.p1.4 "4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§4.1.1](https://arxiv.org/html/2602.06424v1#S4.SS1.SSS1.p3.4 "4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [Remark 4.2](https://arxiv.org/html/2602.06424v1#S4.Thmtheorem2.p1.3 "Remark 4.2. ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [5]
  C. Bayer, C. Ben Hammouda, and R. Tempone (2020-09)
  Hierarchical adaptive sparse grids and quasi-Monte Carlo for option pricing under the rough Bergomi model.
  Quantitative Finance 20 (9),  pp. 1457–1473.
  External Links: ISSN 1469-7688
  Cited by: [footnote 1](https://arxiv.org/html/2602.06424v1#footnote1 "In 1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [6]
  C. Bayer, C. Ben Hammouda, and R. Tempone (2023-02)
  Numerical smoothing with hierarchical adaptive sparse grids and quasi-Monte Carlo methods for efficient option pricing.
  Quantitative Finance 23 (2),  pp. 209–227.
  External Links: ISSN 1469-7688,
  [Document](https://dx.doi.org/10.1080/14697688.2022.2135455)
  Cited by: [footnote 1](https://arxiv.org/html/2602.06424v1#footnote1 "In 1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [7]
  C. Bayer, C. B. Hammouda, A. Papapantoleon, M. Samet, and R. Tempone (2023)
  Optimal Damping with Hierarchical Adaptive Quadrature for Efficient Fourier Pricing of Multi-Asset Options in Lévy Models.
  Journal of Computational Finance 27 (3),  pp. 43–86.
  Cited by: [§B.1.1](https://arxiv.org/html/2602.06424v1#A2.SS1.SSS1.p1.3 "B.1.1 Proof for Corollary 3.7 ‣ B.1 Damping rule and convexity properties ‣ Appendix B Supplementary results for Section 3.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [4th item](https://arxiv.org/html/2602.06424v1#S1.I1.i4.p1.1 "In Our contributions. ‣ 1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§1](https://arxiv.org/html/2602.06424v1#S1.p7.1 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§3.1](https://arxiv.org/html/2602.06424v1#S3.SS1.p1.3 "3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§3](https://arxiv.org/html/2602.06424v1#S3.p1.1 "3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§3](https://arxiv.org/html/2602.06424v1#S3.p2.1 "3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [8]
  C. Bayer, C. B. Hammouda, and R. Tempone (2024-05)
  Multilevel Monte Carlo with Numerical Smoothing for Robust and Efficient Computation of Probabilities and Densities.
  SIAM Journal on Scientific Computing (en).
  External Links: [Link](https://epubs.siam.org/doi/10.1137/22M1495718),
  [Document](https://dx.doi.org/10.1137/22M1495718)
  Cited by: [§4.2](https://arxiv.org/html/2602.06424v1#S4.SS2.p4.1 "4.2 Iteration-Indexed Multilevel Fourier–RQMC Approximation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [9]
  F. Biagini, J. Fouque, M. Frittelli, and T. Meyer-Brandis (2019)
  A unified approach to systemic risk measures via acceptance sets.
  Mathematical Finance 29 (1),  pp. 329–367 (en).
  External Links: ISSN 1467-9965,
  [Link](https://onlinelibrary.wiley.com/doi/abs/10.1111/mafi.12170),
  [Document](https://dx.doi.org/10.1111/mafi.12170)
  Cited by: [§1](https://arxiv.org/html/2602.06424v1#S1.p2.4 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [10]
  P. T. Boggs and J. W. Tolle (1995-01)
  Sequential Quadratic Programming.
  Acta Numerica 4,  pp. 1–51 (en).
  External Links: ISSN 1474-0508, 0962-4929,
  [Document](https://dx.doi.org/10.1017/S0962492900002518)
  Cited by: [§5.1](https://arxiv.org/html/2602.06424v1#S5.SS1.1.p1.1 "Proof. ‣ 5.1 Optimization error ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§5.1](https://arxiv.org/html/2602.06424v1#S5.SS1.p1.1 "5.1 Optimization error ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [footnote 13](https://arxiv.org/html/2602.06424v1#footnote13 "In item C2 ‣ Assumption A.1 (Regularity conditions for the exact problem). ‣ A.1 Additional Assumptions for the Error Analysis ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [11]
  N. G. d. Bruijn (2014-03)
  Asymptotic Methods in Analysis.
   Courier Corporation (en).
  External Links: ISBN 978-0-486-15079-6
  Cited by: [§B.2](https://arxiv.org/html/2602.06424v1#A2.SS2.p1.4 "B.2 Regularized damping ‣ Appendix B Supplementary results for Section 3.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [12]
  M. K. Brunnermeier and P. Cheridito (2019-04)
  Measuring and Allocating Systemic Risk.
  Risks 7 (2),  pp. 46 (en).
  External Links: ISSN 2227-9091,
  [Link](https://www.mdpi.com/2227-9091/7/2/46)
  Cited by: [§1](https://arxiv.org/html/2602.06424v1#S1.p2.3 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [13]
  C. Chen, G. Iyengar, and C. C. Moallemi (2013-06)
  An Axiomatic Approach to Systemic Risk.
  Management Science 59 (6),  pp. 1373–1388 (en).
  External Links: ISSN 0025-1909, 1526-5501,
  [Link](https://pubsonline.informs.org/doi/10.1287/mnsc.1120.1631),
  [Document](https://dx.doi.org/10.1287/mnsc.1120.1631)
  Cited by: [§1](https://arxiv.org/html/2602.06424v1#S1.p2.3 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [14]
  P. Cheridito and T. Li (2009-04)
  Risk Measures on Orlicz Hearts.
  Mathematical Finance 19 (2),  pp. 189–214 (en).
  External Links: ISSN 0960-1627, 1467-9965,
  [Link](https://onlinelibrary.wiley.com/doi/10.1111/j.1467-9965.2009.00364.x),
  [Document](https://dx.doi.org/10.1111/j.1467-9965.2009.00364.x)
  Cited by: [footnote 3](https://arxiv.org/html/2602.06424v1#footnote3 "In Assumption 2.4 (Integrability of the loss vector). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [15]
  R. Cranley and T. N. L. Patterson (1976-12)
  Randomization of Number Theoretic Methods for Multiple Integration.
  SIAM Journal on Numerical Analysis 13 (6),  pp. 904–914.
  External Links: ISSN 0036-1429,
  [Link](https://epubs.siam.org/doi/abs/10.1137/0713071),
  [Document](https://dx.doi.org/10.1137/0713071)
  Cited by: [§4.1](https://arxiv.org/html/2602.06424v1#S4.SS1.p3.9 "4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [16]
  J. Dick, F. Y. Kuo, and I. H. Sloan (2013-05)
  High-dimensional integration: The quasi-Monte Carlo way.
  Acta Numerica 22,  pp. 133–288 (en).
  External Links: ISSN 0962-4929, 1474-0508,
  [Link](https://www.cambridge.org/core/product/identifier/S0962492913000044/type/journal_article)
  Cited by: [§4.1](https://arxiv.org/html/2602.06424v1#S4.SS1.p3.7 "4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [17]
  A. L. Dontchev and R. T. Rockafellar (2009)
  Implicit Functions and Solution Mappings.
  Vol. 543, Springer.
  Cited by: [§A.3](https://arxiv.org/html/2602.06424v1#A1.SS3.p1.2 "A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [18]
  S. Drapeau, M. Kupper, and A. Papapantoleon (2014)
  A Fourier Approach to the Computation of CV@R and Optimized Certainty Equivalents.
  Journal of Risk 16 (6),  pp. 3–29.
  Cited by: [§3](https://arxiv.org/html/2602.06424v1#S3.p1.1 "3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [19]
  J. Dunkel and S. Weber (2010-10)
  Stochastic Root Finding and Efficient Estimation of Convex Risk Measures.
  Operations Research 58 (5),  pp. 1505–1521.
  External Links: ISSN 0030-364X,
  [Link](https://pubsonline.informs.org/doi/abs/10.1287/opre.1090.0784)
  Cited by: [§1](https://arxiv.org/html/2602.06424v1#S1.p4.4 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [20]
  Z. Feinstein, B. Rudloff, and S. Weber (2017-01)
  Measures of Systemic Risk.
  SIAM Journal on Financial Mathematics 8 (1),  pp. 672–708.
  External Links: [Link](https://epubs.siam.org/doi/abs/10.1137/16M1066087),
  [Document](https://dx.doi.org/10.1137/16M1066087)
  Cited by: [§1](https://arxiv.org/html/2602.06424v1#S1.p2.4 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [21]
  H. U. Gerber and E. S. W. Shiu (1994)
  Option Pricing by Esscher Transforms.
  Transactions of the Society of Actuaries 46,  pp. 99–191.
  External Links: [Link](https://pages.stern.nyu.edu/~dbackus/Disasters/Gerber_Shiu_94.pdf)
  Cited by: [Remark B.2](https://arxiv.org/html/2602.06424v1#A2.Thmtheorem2.p1.6 "Remark B.2. ‣ B.1.2 On the Convexity of 𝜐_{𝑘,𝑝}^(𝜈) in in (3.6) ‣ B.1 Damping rule and convexity properties ‣ Appendix B Supplementary results for Section 3.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [22]
  A. Gibbs, D. P. Hewett, and D. Huybrechs (2024-03)
  Numerical evaluation of oscillatory integrals via automated steepest descent contour deformation.
  Journal of Computational Physics 501,  pp. 112787.
  External Links: ISSN 0021-9991,
  [Link](https://www.sciencedirect.com/science/article/pii/S0021999124000366),
  [Document](https://dx.doi.org/10.1016/j.jcp.2024.112787)
  Cited by: [§C.1](https://arxiv.org/html/2602.06424v1#A3.SS1.p3.5 "C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [23]
  M. B. Giles (2015-05)
  Multilevel Monte Carlo methods.
  Acta Numerica 24,  pp. 259–328 (en).
  External Links: ISSN 0962-4929, 1474-0508,
  [Link](https://www.cambridge.org/core/journals/acta-numerica/article/abs/multilevel-monte-carlo-methods/C5AF9A57ED8FF8FDF08074C1071C5511),
  [Document](https://dx.doi.org/10.1017/S096249291500001X)
  Cited by: [§4.2](https://arxiv.org/html/2602.06424v1#S4.SS2.p4.1 "4.2 Iteration-Indexed Multilevel Fourier–RQMC Approximation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [24]
  P. Glasserman (2003)
  Monte Carlo Methods in Financial Engineering.
  Stochastic Modelling and Applied Probability, Vol. 53, Springer, New York, NY.
  External Links: ISBN 978-1-4419-1822-2 978-0-387-21617-1,
  [Link](http://link.springer.com/10.1007/978-0-387-21617-1)
  Cited by: [§1](https://arxiv.org/html/2602.06424v1#S1.p4.4 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [25]
  E. A. v. Hammerstein (2016)
  Tail Behaviour and Tail Dependence of Generalized Hyperbolic Distributions.
  In Advanced Modelling in Mathematical Finance, J. Kallsen and A. Papapantoleon (Eds.),
  Cham,  pp. 3–40 (en).
  External Links: ISBN 978-3-319-45875-5
  Cited by: [Example E.2](https://arxiv.org/html/2602.06424v1#A5.Thmtheorem2.p1.13 "Example E.2 (Normal Inverse Gaussian (NIG)). ‣ E.3 Loss vector distributions and extended characteristic functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [Example E.2](https://arxiv.org/html/2602.06424v1#A5.Thmtheorem2.p1.15 "Example E.2 (Normal Inverse Gaussian (NIG)). ‣ E.3 Loss vector distributions and extended characteristic functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [26]
  Z. He and X. Wang (2021-01)
  Convergence analysis of quasi-Monte Carlo sampling for quantile and expected shortfall.
  Mathematics of Computation 90 (327),  pp. 303–319 (English).
  External Links: ISSN 0025-5718, 1088-6842,
  [Link](https://www.ams.org/mcom/2021-90-327/S0025-5718-2020-03555-8/),
  [Document](https://dx.doi.org/10.1090/mcom/3555)
  Cited by: [§1](https://arxiv.org/html/2602.06424v1#S1.p6.1 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [27]
  E. Hlawka (1961-12)
  Funktionen von beschränkter Variatiou in der Theorie der Gleichverteilung.
  Annali di Matematica Pura ed Applicata 54 (1),  pp. 325–333 (de).
  External Links: ISSN 1618-1891,
  [Link](https://doi.org/10.1007/BF02415361),
  [Document](https://dx.doi.org/10.1007/BF02415361)
  Cited by: [§4.1](https://arxiv.org/html/2602.06424v1#S4.SS1.p3.7 "4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [28]
  T. Homem-de-Mello and G. Bayraksan (2014-01)
  Monte Carlo Sampling-Based Methods for Stochastic Optimization.
  Surveys in Operations Research and Management Science 19 (1),  pp. 56–85 (en).
  External Links: ISSN 18767354,
  [Link](https://linkinghub.elsevier.com/retrieve/pii/S1876735414000038)
  Cited by: [§1](https://arxiv.org/html/2602.06424v1#S1.p4.4 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [29]
  L. Hörmander (2009)
  The Analysis of Linear Partial Differential Operators IV.
  Classics in Mathematics, Springer Berlin Heidelberg, Berlin, Heidelberg (en).
  External Links: ISBN 978-3-642-00117-8 978-3-642-00136-9,
  [Link](http://link.springer.com/10.1007/978-3-642-00136-9),
  [Document](https://dx.doi.org/10.1007/978-3-642-00136-9)
  Cited by: [§E.1](https://arxiv.org/html/2602.06424v1#A5.SS1.p1.3 "E.1 Proof for Corollary 3.4 ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [30]
  D. Huybrechs and S. Vandewalle (2007-10)
  The Construction of cubature rules for multivariate highly oscillatory integrals.
  Mathematics of Computation 76 (260),  pp. 1955–1981 (en).
  External Links: ISSN 00255718,
  [Link](http://www.ams.org/journal-getitem?pii=S0025-5718-07-01937-0),
  [Document](https://dx.doi.org/10.1090/S0025-5718-07-01937-0)
  Cited by: [§C.1](https://arxiv.org/html/2602.06424v1#A3.SS1.p3.5 "C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [31]
  A. Iserles and S. P. Nørsett (2006-09)
  On the computation of highly oscillatory multivariate integrals with stationary points.
  BIT Numerical Mathematics 46 (3),  pp. 549–566 (en).
  External Links: ISSN 1572-9125,
  [Link](https://doi.org/10.1007/s10543-006-0071-2),
  [Document](https://dx.doi.org/10.1007/s10543-006-0071-2)
  Cited by: [§C.1](https://arxiv.org/html/2602.06424v1#A3.SS1.p3.5 "C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [32]
  S. Kaakai, A. Matoussi, and A. Tamtalini (2022-12)
  Multivariate Optimized Certainty Equivalent Risk Measures and their Numerical Computation.
   arXiv.
  Note: arXiv:2210.13825 [math]
  External Links: [Link](http://arxiv.org/abs/2210.13825),
  [Document](https://dx.doi.org/10.48550/arXiv.2210.13825)
  Cited by: [§6.3](https://arxiv.org/html/2602.06424v1#S6.SS3.p1.2 "6.3 QPC Loss with Three-Dimensional NIG Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§6](https://arxiv.org/html/2602.06424v1#S6.p1.1 "6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [33]
  S. Kaakaï, A. Matoussi, and A. Tamtalini (2024-09)
  Estimation of Systemic Shortfall Risk Measure Using Stochastic Algorithms.
  SIAM Journal on Financial Mathematics 15 (3),  pp. 700–733 (en).
  External Links: ISSN 1945-497X,
  [Link](https://epubs.siam.org/doi/10.1137/22M1539344),
  [Document](https://dx.doi.org/10.1137/22M1539344)
  Cited by: [§1](https://arxiv.org/html/2602.06424v1#S1.p4.4 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§1](https://arxiv.org/html/2602.06424v1#S1.p5.1 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§2](https://arxiv.org/html/2602.06424v1#S2.p9.11 "2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§6.1](https://arxiv.org/html/2602.06424v1#S6.SS1.p1.8 "6.1 Exponential Loss with Two-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§6.1](https://arxiv.org/html/2602.06424v1#S6.SS1.p4.7 "6.1 Exponential Loss with Two-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§6.1](https://arxiv.org/html/2602.06424v1#S6.SS1.p6.1 "6.1 Exponential Loss with Two-Dimensional Gaussian Loss Vector ‣ 6 Numerical Experiments and Results ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [34]
  S. Kim, R. Pasupathy, and S. G. Henderson (2015)
  A Guide to Sample Average Approximation.
  In Handbook of Simulation Optimization, M. C. Fu (Ed.),
  Vol. 216,  pp. 207–243 (en).
  Note: Series Title: International Series in Operations Research & Management Science
  External Links: ISBN 978-1-4939-1383-1 978-1-4939-1384-8,
  [Link](https://link.springer.com/10.1007/978-1-4939-1384-8_8)
  Cited by: [§1](https://arxiv.org/html/2602.06424v1#S1.p4.4 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [35]
  A. Kreinin, L. Merkoulovitch, D. Rosen, and M. Zerbs (1998)
  Measuring Portfolio Risk Using Quasi Monte Carlo Methods.
  Algo Research Quarterly 1 (1),  pp. 17–26.
  Cited by: [§1](https://arxiv.org/html/2602.06424v1#S1.p6.1 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [36]
  E. Kromer, L. Overbeck, and K. Zilch (2016-10)
  Systemic risk measures on general measurable spaces.
  Mathematical Methods of Operations Research 84 (2),  pp. 323–357 (en).
  External Links: ISSN 1432-5217,
  [Link](https://doi.org/10.1007/s00186-016-0545-1),
  [Document](https://dx.doi.org/10.1007/s00186-016-0545-1)
  Cited by: [§1](https://arxiv.org/html/2602.06424v1#S1.p2.4 "1 Introduction ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [37]
  Y. Liu and R. Tempone (2026-08)
  Nonasymptotic Convergence Rate of Quasi-Monte Carlo: Applications to Linear Elliptic PDEs with Lognormal Coefficients and Importance Samplings.
  Journal of Computational and Applied Mathematics 482,  pp. 117310.
  External Links: ISSN 03770427
  Cited by: [Remark 4.2](https://arxiv.org/html/2602.06424v1#S4.Thmtheorem2.p1.3 "Remark 4.2. ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [38]
  Y. Liu (2025-05)
  Randomized quasi-Monte Carlo and Owen’s boundary growth condition: a spectral analysis.
  IMA Journal of Numerical Analysis,  pp. draf020.
  External Links: ISSN 0272-4979,
  [Link](https://doi.org/10.1093/imanum/draf020),
  [Document](https://dx.doi.org/10.1093/imanum/draf020)
  Cited by: [§4.1](https://arxiv.org/html/2602.06424v1#S4.SS1.p5.15 "4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [39]
  M. K. Nakayama and B. Tuffin (2024-07)
  Sufficient Conditions for Central Limit Theorems and Confidence Intervals for Randomized Quasi-Monte Carlo Methods.
  ACM Transactions on Modeling and Computer Simulation 34 (3),  pp. 1–38 (en).
  External Links: ISSN 1049-3301, 1558-1195,
  [Link](https://dl.acm.org/doi/10.1145/3643847),
  [Document](https://dx.doi.org/10.1145/3643847)
  Cited by: [§5.2](https://arxiv.org/html/2602.06424v1#S5.SS2.p7.5 "5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [40]
  J. Nocedal and S. J. Wright (2006)
  Numerical optimization.
  Springer series in operations research and financial engineering, Springer, New York, NY (en).
  External Links: ISBN 978-0-387-30303-1 978-0-387-40065-5
  Cited by: [Remark 2.13](https://arxiv.org/html/2602.06424v1#S2.Thmtheorem13.p1.3 "Remark 2.13 (SLSQP). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§2](https://arxiv.org/html/2602.06424v1#S2.p9.11 "2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [10](https://arxiv.org/html/2602.06424v1#alg1.l10 "In Algorithm 1 ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [41]
  D. Ouyang, X. Wang, and Z. He (2024-10)
  Achieving High Convergence Rates by Quasi-Monte Carlo and Importance Sampling for Unbounded Integrands.
  SIAM Journal on Numerical Analysis 62 (5),  pp. 2393–2414.
  External Links: ISSN 0036-1429,
  [Link](https://epubs.siam.org/doi/abs/10.1137/23M1622489),
  [Document](https://dx.doi.org/10.1137/23M1622489)
  Cited by: [Remark 4.2](https://arxiv.org/html/2602.06424v1#S4.Thmtheorem2.p1.3 "Remark 4.2. ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [42]
  A. B. Owen and D. Rudolf (2021-01)
  A Strong Law of Large Numbers for Scrambled Net Integration.
  SIAM Review 63 (2),  pp. 360–372.
  External Links: ISSN 0036-1445,
  [Link](https://epubs.siam.org/doi/abs/10.1137/20M1320535),
  [Document](https://dx.doi.org/10.1137/20M1320535)
  Cited by: [3rd item](https://arxiv.org/html/2602.06424v1#A1.I3.i3.p1.3 "In A.2 Proof for Lemma 5.5 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§A.2](https://arxiv.org/html/2602.06424v1#A1.SS2.p2.18 "A.2 Proof for Lemma 5.5 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§A.3](https://arxiv.org/html/2602.06424v1#A1.SS3.1.p1.4 "Proof. ‣ A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§5.2](https://arxiv.org/html/2602.06424v1#S5.SS2.p2.4 "5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [Remark 5.10](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem10.p1.10 "Remark 5.10 (Estimating 𝑽 under digital shift randomization). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [43]
  A. B. Owen (1995)
  Randomly Permuted (t,m,s)-Nets and (t, s)-Sequences.
  In Monte Carlo and Quasi-Monte Carlo Methods in Scientific Computing, H. Niederreiter and P. J. Shiue (Eds.),
  New York, NY,  pp. 299–317 (en).
  External Links: ISBN 978-1-4612-2552-2
  Cited by: [§5.2](https://arxiv.org/html/2602.06424v1#S5.SS2.p2.4 "5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [Lemma 5.5](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem5.p1.9.9 "Lemma 5.5 (Uniform convergence of Fourier-RQMC estimators). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [44]
  A. B. Owen (1998-12)
  Scrambling Sobol’ and Niederreiter–Xing Points.
  Journal of Complexity 14 (4),  pp. 466–489.
  External Links: ISSN 0885-064X,
  [Link](https://www.sciencedirect.com/science/article/pii/S0885064X98904873),
  [Document](https://dx.doi.org/10.1006/jcom.1998.0487)
  Cited by: [footnote 6](https://arxiv.org/html/2602.06424v1#footnote6 "In Lemma 5.5 (Uniform convergence of Fourier-RQMC estimators). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [45]
  A. B. Owen (2006-01)
  Halton Sequences Avoid the Origin.
  SIAM Review 48 (3),  pp. 487–503.
  External Links: ISSN 0036-1445,
  [Link](https://epubs.siam.org/doi/abs/10.1137/S0036144504441573),
  [Document](https://dx.doi.org/10.1137/S0036144504441573)
  Cited by: [§4.1](https://arxiv.org/html/2602.06424v1#S4.SS1.p5.4 "4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§4.1](https://arxiv.org/html/2602.06424v1#S4.SS1.p5.9 "4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [46]
  A. B. Owen (2023)
  Practical Quasi-Monte Carlo Integration.
  Cited by: [§4.1](https://arxiv.org/html/2602.06424v1#S4.SS1.p3.7 "4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [§4.1](https://arxiv.org/html/2602.06424v1#S4.SS1.p3.9 "4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [47]
  K. Prause (1999-10)
  The Generalized Hyperbolic Model: Estimation, Financial Derivatives, and Risk Measures.
  PhD thesis, University of Freiburg.
  External Links: [Link](https://webdoc.sub.gwdg.de/ebook/e/2001/freidok/15.pdf)
  Cited by: [Remark B.2](https://arxiv.org/html/2602.06424v1#A2.Thmtheorem2.p1.6 "Remark B.2. ‣ B.1.2 On the Convexity of 𝜐_{𝑘,𝑝}^(𝜈) in in (3.6) ‣ B.1 Damping rule and convexity properties ‣ Appendix B Supplementary results for Section 3.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [48]
  A. W. Roberts and D. E. Varberg (1974-11)
  Another Proof that Convex Functions are Locally Lipschitz.
  The American Mathematical Monthly (EN).
  External Links: ISSN 0002-9890,
  [Link](https://www.tandfonline.com/doi/abs/10.1080/00029890.1974.11993721),
  [Document](https://dx.doi.org/10.2307/2319313)
  Cited by: [Remark 2.11](https://arxiv.org/html/2602.06424v1#S2.Thmtheorem11.p1.2 "Remark 2.11 (Interchanging Differentiation and Expectation). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [49]
  S. M. Robinson (1980-02)
  Strongly Regular Generalized Equations.
  Mathematics of Operations Research 5 (1),  pp. 43–62.
  External Links: ISSN 0364-765X,
  [Link](https://pubsonline.informs.org/doi/abs/10.1287/moor.5.1.43),
  [Document](https://dx.doi.org/10.1287/moor.5.1.43)
  Cited by: [§5.2](https://arxiv.org/html/2602.06424v1#S5.SS2.p4.1 "5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [50]
  A. Shapiro, D. Dentcheva, and A. P. Ruszczyński (2014-07)
  Lectures on Stochastic Programming: Modeling and Theory, Second Edition.
   SIAM (en).
  External Links: ISBN 978-1-61197-342-6
  Cited by: [Appendix D](https://arxiv.org/html/2602.06424v1#A4.2.p1.2 "Proof. ‣ Appendix D Convergence analysis for the SAA method ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [Appendix D](https://arxiv.org/html/2602.06424v1#A4.p2.1 "Appendix D Convergence analysis for the SAA method ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [51]
  A. Shapiro (2003)
  Monte Carlo Sampling Methods.
  In Handbooks in Operations Research and Management Science,
  Vol. 10,  pp. 353–425 (en).
  External Links: ISBN 978-0-444-50854-6,
  [Link](https://linkinghub.elsevier.com/retrieve/pii/S0927050703100060),
  [Document](https://dx.doi.org/10.1016/S0927-0507%2803%2910006-0)
  Cited by: [§A.2](https://arxiv.org/html/2602.06424v1#A1.SS2.p1.1 "A.2 Proof for Lemma 5.5 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [Appendix D](https://arxiv.org/html/2602.06424v1#A4.1.p1.4 "Proof. ‣ Appendix D Convergence analysis for the SAA method ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [52]
  I. M. Sobol’, D. Asotsky, A. Kreinin, and S. Kucherenko (2011)
  Construction and Comparison of High-Dimensional Sobol’ Generators.
  Wilmott 2011 (56),  pp. 64–79 (en).
  External Links: ISSN 1541-8286,
  [Link](https://onlinelibrary.wiley.com/doi/abs/10.1002/wilm.10056),
  [Document](https://dx.doi.org/10.1002/wilm.10056)
  Cited by: [§4.1](https://arxiv.org/html/2602.06424v1#S4.SS1.p3.9 "4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),
  [Remark 5.19](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem19.p1.3 "Remark 5.19 (Choice of Sobol points). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
* [53]
  D. Sun (2006-11)
  The Strong Second-Order Sufficient Condition and Constraint Nondegeneracy in Nonlinear Semidefinite Programming and Their Implications.
  Mathematics of Operations Research 31 (4),  pp. 761–776 (en).
  External Links: ISSN 0364-765X, 1526-5471,
  [Document](https://dx.doi.org/10.1287/moor.1060.0195)
  Cited by: [footnote 7](https://arxiv.org/html/2602.06424v1#footnote7 "In Theorem 5.7 (Consistency of solution from Fourier-RQMC problem). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

## Appendix A Supplementary results for Sections [5](https://arxiv.org/html/2602.06424v1#S5 "5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")

### A.1 Additional Assumptions for the Error Analysis

###### Assumption A.1 (Regularity conditions for the exact problem).

The point 𝐦∗\mathbf{m^{\*}} is a (local) solution of equation ([2.5](https://arxiv.org/html/2602.06424v1#S2.E5 "In Definition 2.5 (Multivariate shortfall risk). ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) at which the following conditions hold:

1. (C1)

   For every 𝐦𝟎∈ℝd\mathbf{m\_{0}}\in\mathbb{R}^{d}, the mapping 𝐦↦∇ℓ​(𝐗−𝐦)\mathbf{m}\mapsto\nabla\ell(\mathbf{X-m}) is differentiable at 𝐦0\mathbf{m}\_{0} a.s.
2. (C2)

   The strong second-order sufficient conditions (SSOSC) hold at the point 𝐦∗\mathbf{m}^{\*}. Let the tangent space at 𝐦∗\mathbf{m}^{\*}

   |  |  |  |
   | --- | --- | --- |
   |  | 𝒦​(𝐦∗):={𝐚∈ℝd:∇g​(𝐦∗)⊤​𝐚=0}.\mathcal{K}(\mathbf{m}^{\*}):=\left\{\mathbf{a}\in\mathbb{R}^{d}\ :\ \nabla g(\mathbf{m}^{\*})^{\!\top}\mathbf{a}=0\right\}. |  |

   Then 𝐚⊤​∇2g​(𝐦∗)​𝐚<0,∀𝐚∈𝒦​(𝐦∗)∖{0}.\mathbf{a}^{\top}\nabla^{2}g(\mathbf{m}^{\*})\mathbf{a}<0,\quad\forall\mathbf{a}\in\mathcal{K}(\mathbf{m}^{\*})\setminus\left\{0\right\}. 131313∇2ℒ​(𝐳∗)=−λ∗​∇2g​(𝐦∗)\nabla^{2}\mathcal{L}(\mathbf{z}^{\*})=-\lambda^{\*}\nabla^{2}g(\mathbf{m}^{\*}) as in ([2.9](https://arxiv.org/html/2602.06424v1#S2.E9 "In 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) with λ∗>0\lambda^{\*}>0, so the normal SSOSC in [[10](https://arxiv.org/html/2602.06424v1#bib.bib46 "Sequential Quadratic Programming")] become 𝐚⊤​∇2g​(𝐦∗)​𝐚<0\mathbf{a}^{\top}\nabla^{2}g(\mathbf{m}^{\*})\mathbf{a}<0

###### Assumption A.2 (Regularity conditions for the Fourier–RQMC problem).

1. (C3)

   The SSOSC holds at the point 𝐦N,SshiftRQMC,∗{\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*} a.s. 141414a.s. in Assumption [A.2](https://arxiv.org/html/2602.06424v1#A1.Thmtheorem2 "Assumption A.2 (Regularity conditions for the Fourier–RQMC problem). ‣ A.1 Additional Assumptions for the Error Analysis ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") will be understood as for almost every realization of the RQMC shifts SS.Define the tangent space at 𝐦N,SshiftRQMC,∗{\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}

   |  |  |  |
   | --- | --- | --- |
   |  | 𝒦N,Sshift​(𝐦N,SshiftRQMC,∗):={𝐚∈ℝd:IN,SshiftRQMC​[h~(1)​(⋅;𝐦N,SshiftRQMC,∗)]⊤​𝐚=0}.\mathcal{K}\_{N,S\_{\mathrm{shift}}}\left({\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}\right):=\left\{\mathbf{a}\in\mathbb{R}^{d}\ :\ I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\widetilde{h}^{(1)}\left({\cdot;\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}\right)\right]^{\top}\mathbf{a}=0\right\}. |  |

   Then 𝐚⊤​IN,SshiftRQMC​[h~(2)​(⋅;𝐦N,SshiftRQMC,∗)]​𝐚<0,∀𝐚∈𝒦N,Sshift​(𝐦N,SshiftRQMC,∗)∖{0}.\mathbf{a}^{\top}I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\widetilde{h}^{(2)}\left({\cdot;\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}\right)\right]\mathbf{a}<0,\quad\forall\mathbf{a}\in\mathcal{K}\_{N,S\_{\mathrm{shift}}}\left({\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}\right)\setminus\left\{0\right\}.
2. (C4)

   The Hessian matrix IN,SshiftRQMC​[h~(2)​(⋅;𝐦N,SshiftRQMC,∗)]I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\widetilde{h}^{(2)}\left({\cdot;\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}\right)\right],
   is invertible a.s.
3. (C5)

   For each iteration jj, the BFGS approximation matrix 𝐁N,Sshift(RQMC,j)​(⋅;𝐦N,Sshift(RQMC,j))\mathbf{B}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\left({\cdot;\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\right)
   is μ1\mu\_{1}-strongly convex a.s. on the tangent space 𝒦N,Sshift​(𝐦N,Sshift(RQMC,j))\mathcal{K}\_{N,S\_{\mathrm{shift}}}\left({\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\right), i.e.,

   |  |  |  |
   | --- | --- | --- |
   |  | μ1​𝑰⪯𝐁N,Sshift(RQMC,j)​(⋅;𝐦N,Sshift(RQMC,j)),0<μ1<∞,\mu\_{1}\,\boldsymbol{I}\;\preceq\;\mathbf{B}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\left({\cdot;\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\right),\qquad 0<\mu\_{1}<\infty, |  |
4. (C6)

   For each iteration jj, the approximation matrix
   𝐁N,Sshift(RQMC,j)​(⋅;𝐦N,Sshift(RQMC,j))\mathbf{B}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\left({\cdot;\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\right)
   is invertible a.s., and both it and its inverse are uniformly bounded a.s., i.e.,

   |  |  |  |
   | --- | --- | --- |
   |  | ‖𝐁N,Sshift(RQMC,j)​(⋅;𝐦N,Sshift(RQMC,j))‖≤B1,‖(𝐁N,Sshift(RQMC,j)​(⋅;𝐦N,Sshift(RQMC,j)))−1‖≤B2,\Bigl\|\mathbf{B}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\left({\cdot;\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\right)\Bigr\|\leq B\_{1},\qquad\Bigl\|\Bigl(\mathbf{B}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\left({\cdot;\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\right)\Bigr)^{-1}\Bigr\|\leq B\_{2}, |  |

   for some constants B1>0B\_{1}>0 and B2>0B\_{2}>0.
5. (C7)

   Let PjP\_{j} denote the projection matrix onto the tangent space 𝒦N,Sshift​(𝐦N,Sshift(RQMC,j))\mathcal{K}\_{N,S\_{\mathrm{shift}}}\left({\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\right).
   The approximation matrix 𝐁N,Sshift(RQMC,j)​(⋅;𝐦N,Sshift(RQMC,j))\mathbf{B}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\left({\cdot;\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\right) satisfies, a.s.,

   |  |  |  |
   | --- | --- | --- |
   |  | limj→∞‖Pj​(𝐁N,Sshift(RQMC,j)​(⋅;𝐦N,Sshift(RQMC,j))−IN,SshiftRQMC​[h~(2)​(⋅;𝐦N,SshiftRQMC,∗)]​(𝐦j+1,N,SshiftRQMC−𝐦N,Sshift(RQMC,j)))‖‖𝐦j+1,N,SshiftRQMC−𝐦N,Sshift(RQMC,j)‖=0.\lim\_{j\to\infty}\frac{\left\lVert P\_{j}\left(\mathbf{B}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\left({\cdot;\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\right)-I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\widetilde{h}^{(2)}\left({\cdot;\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}\right)\right]\left({\mathbf{m}}\_{j+1,N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}-{\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\right)\right)\right\rVert}{\left\lVert{\mathbf{m}}\_{j+1,N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}-{\mathbf{m}}\_{N,S\_{\mathrm{shift}}}^{(\mathrm{RQMC},j)}\right\rVert}=0. |  |

### A.2 Proof for Lemma [5.5](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem5 "Lemma 5.5 (Uniform convergence of Fourier-RQMC estimators). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")

The argument is based on the uniform convergence proof for unconstrained SAA problems in
[[51](https://arxiv.org/html/2602.06424v1#bib.bib183 "Monte Carlo Sampling Methods"), Proposition 7]. We adapt that reasoning by replacing the SAA estimators with our Fourier-RQMC
estimators and present the full proof for completeness. Recall that our Fourier-RQMC estimator with S¯\overline{S} independent shifts can be written as

|  |  |  |  |
| --- | --- | --- | --- |
| (A.1) |  | IN,S¯RQMC​[h~k,p(ν)​(⋅;𝐦k,p)]=1S¯​∑s=1S¯1N​∑n=1Nh~k,p(ν)​(𝐯n(s),𝐦k,p),I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}(\cdot;\mathbf{m}\_{k,p})\right]=\frac{1}{\overline{S}}\sum\_{s=1}^{\overline{S}}\frac{1}{N}\sum\_{n=1}^{N}\widetilde{h}\_{k,p}^{(\nu)}\!\left(\mathbf{v}\_{n}^{(s)},\mathbf{m}\_{k,p}\right), |  |

and the corresponding target quantity g^k,p(ν),Fou​(𝐦k,p)\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}}(\mathbf{m}\_{k,p}) satisfies Assumption [3.2](https://arxiv.org/html/2602.06424v1#S3.Ex2 "Assumption 3.2 (Admissible contour shifts). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") is

|  |  |  |  |
| --- | --- | --- | --- |
| (A.2) |  | g^k,p(ν),Fou​(𝐦k,p)=𝔼𝐕​[h~k,p(ν)​(𝐕,𝐦k,p)],\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}}(\mathbf{m}\_{k,p})=\mathbb{E}\_{\mathbf{V}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}(\mathbf{V},\mathbf{m}\_{k,p})\right], |  |

where 𝐕\mathbf{V} denotes a generic random vector distributed on [0,1]k[0,1]^{k}.

Fix 𝐦¯k,p∈Mk,p\overline{\mathbf{m}}\_{k,p}\in M\_{k,p}. For η>0\eta>0,

|  |  |  |
| --- | --- | --- |
|  | U​(𝐦¯k,p,η):={𝐦k,p∈Mk,p:‖𝐦k,p−𝐦¯k,p‖≤η}.U(\overline{\mathbf{m}}\_{k,p},\eta):=\bigl\{\mathbf{m}\_{k,p}\in M\_{k,p}:\ \|\mathbf{m}\_{k,p}-\overline{\mathbf{m}}\_{k,p}\|\leq\eta\bigr\}. |  |

Define
δ𝐦¯k,p,η(ν)​(𝐯):=sup𝐦k,p∈U​(𝐦¯k,p,η)‖h~k,p(ν)​(𝐯,𝐦k,p)−h~k,p(ν)​(𝐯,𝐦¯k,p)‖.\delta\_{\overline{\mathbf{m}}\_{k,p},\eta}^{(\nu)}(\mathbf{v}):=\sup\_{\mathbf{m}\_{k,p}\in U(\overline{\mathbf{m}}\_{k,p},\eta)}\left\lVert\widetilde{h}\_{k,p}^{(\nu)}(\mathbf{v},\mathbf{m}\_{k,p})-\widetilde{h}\_{k,p}^{(\nu)}(\mathbf{v},\overline{\mathbf{m}}\_{k,p})\right\rVert.
From ([4.8](https://arxiv.org/html/2602.06424v1#S4.E8 "In 4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), we have that h~k,p(ν)​(𝐯,⋅)\widetilde{h}\_{k,p}^{(\nu)}(\mathbf{v},\cdot) is continuous with 𝐦k,p\mathbf{m}\_{k,p} (they only depend on 𝐦k,p\mathbf{m}\_{k,p} through exp(.)\exp(.) part) for each fixed 𝐯\mathbf{v}, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (A.3) |  | δ𝐦¯k,p,η(ν)​(𝐯)→ 0,as ​η↓0,∀𝐯∈[0,1]k.\delta\_{\overline{\mathbf{m}}\_{k,p},\eta}^{(\nu)}\left(\mathbf{v}\right)\ \xrightarrow[]{}\ 0,\qquad\text{as }\eta\downarrow 0,\ \ \forall\mathbf{v}\in[0,1]^{k}. |  |

Moreover, from the representation of h~k,p(ν)\widetilde{h}\_{k,p}^{(\nu)} in ([4.8](https://arxiv.org/html/2602.06424v1#S4.E8 "In 4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), for 𝐦k,p∈Mk,p\mathbf{m}\_{k,p}\in M\_{k,p} along with the admissible damping vector 𝐊k,p(ν)\mathbf{K}\_{k,p}^{(\nu)} from Assumption [3.2](https://arxiv.org/html/2602.06424v1#S3.Ex2 "Assumption 3.2 (Admissible contour shifts). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), we also have

|  |  |  |
| --- | --- | --- |
|  | sup𝐦k,p∈Mk,pexp⁡⟨𝐊k,p(ν),𝐦k,p⟩≤CM\sup\_{\mathbf{m}\_{k,p}\in M\_{k,p}}\exp\!\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{m}\_{k,p}\rangle\leq C\_{M} |  |

for some finite constant CMC\_{M}. Consequently, there exists an integrable envelope HH such that ‖h~k,p(ν)​(𝐯;𝐦k,p)‖≤H​(𝐯)\left\lVert\widetilde{h}\_{k,p}^{(\nu)}(\mathbf{v};\mathbf{m}\_{k,p})\right\rVert\leq H(\mathbf{v}) for all 𝐦k,p\mathbf{m}\_{k,p} in a neighborhood of 𝐦¯k,p\overline{\mathbf{m}}\_{k,p}. Hence,

|  |  |  |
| --- | --- | --- |
|  | 0≤δ𝐦¯k,p,η(ν)​(𝐯)≤2​H​(𝐯),∀𝐯∈[0,1]k.0\leq\delta\_{\overline{\mathbf{m}}\_{k,p},\eta}^{(\nu)}(\mathbf{v})\leq 2H(\mathbf{v}),\qquad\forall\mathbf{v}\in[0,1]^{k}. |  |

Therefore, by the Dominated Convergence Theorem,

|  |  |  |  |
| --- | --- | --- | --- |
| (A.4) |  | limη→0𝔼𝐕​[δ𝐦¯k,p,η(ν)​(𝐕)]=𝔼𝐕​[limη→0δ𝐦¯k,p,η(ν)​(𝐕)]\lim\_{\eta\to 0}\mathbb{E}\_{\mathbf{V}}\!\left[\delta\_{\overline{\mathbf{m}}\_{k,p},\eta}^{(\nu)}\left(\mathbf{V}\right)\right]=\mathbb{E}\_{\mathbf{V}}\left[\lim\_{\eta\to 0}\delta\_{\overline{\mathbf{m}}\_{k,p},\eta}^{(\nu)}\left(\mathbf{V}\right)\right] |  |

For any 𝐦k,p∈U​(𝐦¯k,p,η)\mathbf{m}\_{k,p}\in U(\overline{\mathbf{m}}\_{k,p},\eta), by ([A.1](https://arxiv.org/html/2602.06424v1#A1.E1 "In A.2 Proof for Lemma 5.5 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")),

|  |  |  |  |
| --- | --- | --- | --- |
| (A.5) |  | ‖IN,S¯RQMC​[h~k,p(ν)​(⋅;𝐦k,p)]−IN,S¯RQMC​[h~k,p(ν)​(⋅;𝐦¯k,p)]‖≤IN,S¯RQMC​[δ𝐦¯k,p,η(ν)].\left\lVert I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}(\cdot;\mathbf{m}\_{k,p})\right]-I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}(\cdot;\overline{\mathbf{m}}\_{k,p})\right]\right\rVert\leq I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\delta\_{\overline{\mathbf{m}}\_{k,p},\eta}^{(\nu)}\right]. |  |

By Assumption [4.1](https://arxiv.org/html/2602.06424v1#S4.Thmtheorem1 "Assumption 4.1 (Square-integrability of transformed integrands). ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), from [[42](https://arxiv.org/html/2602.06424v1#bib.bib53 "A Strong Law of Large Numbers for Scrambled Net Integration"), Theorem 4.2], we have the SLLN for the nested uniform scrambling Sobol sequence (applied to the integrable function
δ𝐦¯k,p,η(ν)\delta\_{\overline{\mathbf{m}}\_{k,p},\eta}^{(\nu)}), we have

|  |  |  |  |
| --- | --- | --- | --- |
| (A.6) |  | IN,S¯RQMC​[δ𝐦¯k,p,η(ν)]→a.s.𝔼𝐕​[δ𝐦¯k,p,η(ν)​(𝐕)],N→∞.I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\delta\_{\overline{\mathbf{m}}\_{k,p},\eta}^{(\nu)}\right]\xrightarrow[]{\mathrm{a.s.}}\mathbb{E}\_{\mathbf{V}}\!\left[\delta\_{\overline{\mathbf{m}}\_{k,p},\eta}^{(\nu)}\left(\mathbf{V}\right)\right],\qquad N\to\infty. |  |

Combining ([A.3](https://arxiv.org/html/2602.06424v1#A1.E3 "In A.2 Proof for Lemma 5.5 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"))–([A.6](https://arxiv.org/html/2602.06424v1#A1.E6 "In A.2 Proof for Lemma 5.5 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), for any ϵ>0\epsilon>0, there exists small enough
η>0\eta>0 and sufficient large N0N\_{0} such that for all N≥N0N\geq N\_{0},

|  |  |  |  |
| --- | --- | --- | --- |
| (A.7) |  | sup𝐦k,p∈U​(𝐦¯k,p,η)‖IN,S¯RQMC​[h~k,p(ν)​(⋅;𝐦k,p)]−IN,S¯RQMC​[h~k,p(ν)​(⋅;𝐦¯k,p)]‖≤ϵa.s.\sup\_{\mathbf{m}\_{k,p}\in U(\overline{\mathbf{m}}\_{k,p},\eta)}\left\lVert I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}(\cdot;\mathbf{m}\_{k,p})\right]-I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}(\cdot;\overline{\mathbf{m}}\_{k,p})\right]\right\rVert\leq\epsilon\quad\text{a.s.} |  |

Since Mk,pM\_{k,p} is compact, for the above η>0\eta>0 there exist points
𝐦k,p(1),…,𝐦k,p(E)∈Mk,p\mathbf{m}\_{k,p}^{(1)},\dots,\mathbf{m}\_{k,p}^{(E)}\in M\_{k,p} such that
Mk,p⊂⋃i=1EU​(𝐦k,p(i),η).M\_{k,p}\subset\bigcup\_{i=1}^{E}U\left(\mathbf{m}\_{k,p}^{(i)},\eta\right).
Fix such a finite cover; for any 𝐦k,p∈Mk,p\mathbf{m}\_{k,p}\in M\_{k,p}, choose an index ii such that
𝐦k,p∈U​(𝐦k,p(i),η)\mathbf{m}\_{k,p}\in U\left(\mathbf{m}\_{k,p}^{(i)},\eta\right). Then, by the triangle inequality,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.8) |  | ‖IN,S¯RQMC​[h~k,p(ν)​(⋅;𝐦k,p)]−g^k,p(ν),Fou​(𝐦k,p)‖\displaystyle\left\lVert I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}(\cdot;\mathbf{m}\_{k,p})\right]-\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}}(\mathbf{m}\_{k,p})\right\rVert | ≤‖IN,S¯RQMC​[h~k,p(ν)​(⋅;𝐦k,p)]−IN,S¯RQMC​[h~k,p(ν)​(⋅;𝐦k,p(i))]‖⏟(I)\displaystyle\leq\underbrace{\left\lVert I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}(\cdot;\mathbf{m}\_{k,p})\right]-I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}\!\left(\cdot;\mathbf{m}\_{k,p}^{(i)}\right)\right]\right\rVert}\_{(\mathrm{I})} |  |
|  |  | +‖IN,S¯RQMC​[h~k,p(ν)​(⋅;𝐦k,p(i))]−g^k,p(ν),Fou​(𝐦k,p(i))‖⏟(II)\displaystyle+\underbrace{\left\lVert I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}\!\left(\cdot;\mathbf{m}\_{k,p}^{(i)}\right)\right]-\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}}\!\left(\mathbf{m}\_{k,p}^{(i)}\right)\right\rVert}\_{(\mathrm{II})} |  |
|  |  | +‖g^k,p(ν),Fou​(𝐦k,p(i))−g^k,p(ν),Fou​(𝐦k,p)‖⏟(III).\displaystyle+\underbrace{\left\lVert\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}}\!\left(\mathbf{m}\_{k,p}^{(i)}\right)-\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}}(\mathbf{m}\_{k,p})\right\rVert}\_{(\mathrm{III})}. |  |

* •

  Term (I)(\mathrm{I}) is controlled uniformly by ([A.7](https://arxiv.org/html/2602.06424v1#A1.E7 "In A.2 Proof for Lemma 5.5 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")):

  |  |  |  |
  | --- | --- | --- |
  |  | sup𝐦k,p∈Mk,p(I)≤ϵa.s. for N sufficient large.\sup\_{\mathbf{m}\_{k,p}\in M\_{k,p}}(\mathrm{I})\leq\epsilon\quad\text{a.s. for $N$ sufficient large.} |  |
* •

  Under Assumption [3.2](https://arxiv.org/html/2602.06424v1#S3.Ex2 "Assumption 3.2 (Admissible contour shifts). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), g^k,p(ν),Fou\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}} is continuous on Mk,pM\_{k,p}. Since Mk,pM\_{k,p} is compact, g^k,p(ν),Fou\widehat{g}^{(\nu),\mathrm{Fou}}\_{k,p} is uniformly continuous on Mk,pM\_{k,p}. Consequently, term (III)(\mathrm{III}) can be controlled deterministically. In particular, for any 𝐦k,p∈U​(𝐦k,p(i),η)\mathbf{m}\_{k,p}\in U\left(\mathbf{m}\_{k,p}^{(i)},\eta\right),

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (A.9) |  | sup𝐦k,p∈Mk,p‖g^k,p(ν),Fou​(𝐦k,p)−g^k,p(ν),Fou​(𝐦k,p(i))‖≤ϵ\sup\_{\mathbf{m}\_{k,p}\in M\_{k,p}}\left\lVert\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}}\left(\mathbf{m}\_{k,p}\right)-\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}}\left(\mathbf{m}\_{k,p}^{(i)}\right)\right\rVert\leq\epsilon |  |
* •

  For Term (II)(\mathrm{II}), note that it involves only finitely many points 𝐦k,p(i)\mathbf{m}\_{k,p}^{(i)}. Again by the SLLN for the nested uniform scrambling Sobol sequence (Assumption [4.1](https://arxiv.org/html/2602.06424v1#S4.Thmtheorem1 "Assumption 4.1 (Square-integrability of transformed integrands). ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") and [[42](https://arxiv.org/html/2602.06424v1#bib.bib53 "A Strong Law of Large Numbers for Scrambled Net Integration"), Theorem 4.2]) for h~k,p(ν)\widetilde{h}\_{k,p}^{(\nu)},

  |  |  |  |
  | --- | --- | --- |
  |  | IN,S¯RQMC​[h~k,p(ν)​(⋅;𝐦k,p(i))]→a.s.g^k,p(ν),Fou​(𝐦k,p(i)),N→∞,I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}\left(\cdot;\mathbf{m}\_{k,p}^{(i)}\right)\right]\xrightarrow[]{\mathrm{a.s.}}\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}}\left(\mathbf{m}\_{k,p}^{(i)}\right),\qquad N\to\infty, |  |

  with g^k,p(ν),Fou​(𝐦k,p(i))=𝔼𝐕​[h~k,p(ν)​(𝐕,𝐦k,p(i))]\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}}\left(\mathbf{m}\_{k,p}^{(i)}\right)=\mathbb{E}\_{\mathbf{V}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}\left(\mathbf{V},\mathbf{m}\_{k,p}^{(i)}\right)\right] for each i=1,…,Ei=1,\dots,E. Taking the maximum over finitely many ii preserves almost sure convergence, hence
  max1≤i≤E⁡(II)→a.s.0\max\_{1\leq i\leq E}(\mathrm{II})\xrightarrow[]{\mathrm{a.s.}}0. In particular, for NN sufficient large, sup𝐦k,p∈Mk,p(II)≤ϵ\sup\_{\mathbf{m}\_{k,p}\in M\_{k,p}}(\mathrm{II})\leq\epsilon almost surely.

Putting the three bounds into ([A.8](https://arxiv.org/html/2602.06424v1#A1.E8 "In A.2 Proof for Lemma 5.5 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), we obtain that for NN sufficient large,

|  |  |  |
| --- | --- | --- |
|  | sup𝐦k,p∈Mk,p‖IN,S¯RQMC​[h~k,p(ν)​(⋅;𝐦k,p)]−g^k,p(ν),Fou​(𝐦k,p)‖≤3​ϵa.s.\sup\_{\mathbf{m}\_{k,p}\in M\_{k,p}}\left\lVert I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}(\cdot;\mathbf{m}\_{k,p})\right]-\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}}(\mathbf{m}\_{k,p})\right\rVert\leq 3\epsilon\qquad\text{a.s.} |  |

Since ϵ>0\epsilon>0 is arbitrary, the first convergence in ([5.4](https://arxiv.org/html/2602.06424v1#S5.E4 "In Lemma 5.5 (Uniform convergence of Fourier-RQMC estimators). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) follows.

### A.3 Proof for Theorem [5.7](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem7 "Theorem 5.7 (Consistency of solution from Fourier-RQMC problem). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")

The proof follows standard local stability and implicit-function arguments for stochastic generalized equations (see [[17](https://arxiv.org/html/2602.06424v1#bib.bib48 "Implicit Functions and Solution Mappings")]).
For η>0\eta>0, define the neighborhood of the optimal solution 𝐳∗\mathbf{z}^{\*} by

|  |  |  |  |
| --- | --- | --- | --- |
| (A.10) |  | U​(𝐳∗,η):={𝐳∈𝒵:‖𝐳−𝐳∗‖≤η}.U\left(\mathbf{z}^{\*},\eta\right):=\bigl\{\mathbf{z}\in\mathcal{Z}:\ \left\lVert\mathbf{z}-\mathbf{z^{\*}}\right\rVert\leq\eta\bigr\}. |  |

Recall that the aggregate Fourier-based integrands admit the finite decompositions. By Lemma [5.5](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem5 "Lemma 5.5 (Uniform convergence of Fourier-RQMC estimators). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), the USLLN holds on each Mk,p⊂ℝkM\_{k,p}\subset\mathbb{R}^{k} for
IN,S¯RQMC​[h~k,p(ν)​(⋅;𝐦k,p)]I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}^{(\nu)}\_{k,p}(\cdot;\mathbf{m}\_{k,p})\right].
Applying the triangle inequality yields, for NN sufficiently large, the corresponding USLLN for the aggregate integrands:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.11) |  | sup𝐦∈M‖IN,S¯RQMC​[h~(ν)​(⋅;𝐦)]−g^(ν),Fou​(𝐦)‖\displaystyle\sup\_{\mathbf{m}\in M}\left\lVert I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\widetilde{h}^{(\nu)}(\cdot;\mathbf{m})\right]-\widehat{g}^{(\nu),\mathrm{Fou}}(\mathbf{m})\right\rVert | →a.s.0.\displaystyle\xrightarrow[]{\mathrm{a.s.}}0. |  |

Next, by the strong regularity of solution 𝐳∗\mathbf{z}^{\*}, from Definition [5.5](https://arxiv.org/html/2602.06424v1#S5.E5 "In Definition 5.6 (Strong regularity of optimal solution). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), the Fourier representation of the true Hessian
ℒ^∇𝐳2Fou​(𝐳∗)\widehat{\mathcal{L}}\_{\nabla^{2}\_{\mathbf{z}}}^{\mathrm{Fou}}(\mathbf{z}^{\*}) is invertible. Moreover, by continuity of ℒ^∇𝐳2Fou​(⋅)\widehat{\mathcal{L}}\_{\nabla^{2}\_{\mathbf{z}}}^{\mathrm{Fou}}(\cdot), there exists η>0\eta>0 and a constant CL>0C\_{L}>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
| (A.12) |  | ‖ℒ^∇𝐳2Fou​(𝐳)−1‖≤CL,∀𝐳∈U​(𝐳∗,η).\left\lVert\widehat{\mathcal{L}}\_{\nabla^{2}\_{\mathbf{z}}}^{\mathrm{Fou}}(\mathbf{z})^{-1}\right\rVert\leq C\_{L},\qquad\forall\,\mathbf{z}\in U\left(\mathbf{z}^{\*},\eta\right). |  |

Define the map TNT\_{N} associated with the Fourier-RQMC problem by

|  |  |  |  |
| --- | --- | --- | --- |
| (A.13) |  | TN​(𝐳):=𝐳−[ℒ^∇𝐳2Fou​(𝐳)−1]​IN,S¯RQMC​[ℋ(1)​(⋅;𝐳)],T\_{N}(\mathbf{z}):=\mathbf{z}-\left[\widehat{\mathcal{L}}\_{\nabla^{2}\_{\mathbf{z}}}^{\mathrm{Fou}}(\mathbf{z})^{-1}\right]I\_{N,\overline{S}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}(\cdot;\mathbf{z})\right], |  |

By construction,
IN,S¯RQMC​[ℋ(1)​(⋅;𝐳)]=0⟺TN​(𝐳)=𝐳.I\_{N,\overline{S}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}(\cdot;\mathbf{z})\right]=0\quad\Longleftrightarrow\quad T\_{N}(\mathbf{z})=\mathbf{z}.

Step 1: TNT\_{N} is a contraction on U​(𝐳∗,η)U\left(\mathbf{z}^{\*},\eta\right).

Let 𝐳1,𝐳2∈U​(𝐳∗,η)\mathbf{z}\_{1},\mathbf{z}\_{2}\in U\left(\mathbf{z}^{\*},\eta\right).
Since ℒ^∇𝐳Fou\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}} is continuously differentiable on U​(𝐳∗,η)U\left(\mathbf{z}^{\*},\eta\right), the mean value theorem yields

|  |  |  |
| --- | --- | --- |
|  | IN,S¯RQMC​[ℋ(1)​(⋅;𝐳1)]−IN,S¯RQMC​[ℋ(1)​(⋅;𝐳2)]=IN,S¯RQMC​[ℋ(2)​(⋅;𝐳¯)]​(𝐳1−𝐳2),I\_{N,\overline{S}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}(\cdot;\mathbf{z}\_{1})\right]-I\_{N,\overline{S}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}(\cdot;\mathbf{z}\_{2})\right]=I\_{N,\overline{S}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(2)}(\cdot;\overline{\mathbf{z}})\right]\,(\mathbf{z}\_{1}-\mathbf{z}\_{2}), |  |

for some 𝐳¯\overline{\mathbf{z}} on the line segment between 𝐳1\mathbf{z}\_{1} and 𝐳2\mathbf{z}\_{2}.
Substituting into ([A.13](https://arxiv.org/html/2602.06424v1#A1.E13 "In A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.14) |  | TN​(𝐳1)−TN​(𝐳2)\displaystyle T\_{N}\left(\mathbf{z}\_{1}\right)-T\_{N}\left(\mathbf{z}\_{2}\right) | =(𝑰−ℒ^∇𝐳2Fou​(𝐳¯)−1​IN,S¯RQMC​[ℋ(2)​(⋅;𝐳¯)])​(𝐳1−𝐳2).\displaystyle=\left(\boldsymbol{I}-\,\widehat{\mathcal{L}}\_{\nabla^{2}\_{\mathbf{z}}}^{\mathrm{Fou}}(\overline{\mathbf{z}})^{-1}\,I\_{N,\overline{S}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(2)}(\cdot;\overline{\mathbf{z}})\right]\right)(\mathbf{z}\_{1}-\mathbf{z}\_{2}). |  |

From ([A.11](https://arxiv.org/html/2602.06424v1#A1.E11 "In A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) (restricted to UU) we obtain the uniform convergence,

|  |  |  |  |
| --- | --- | --- | --- |
| (A.15) |  | sup𝐳¯∈U‖IN,S¯RQMC​[ℋ(2)​(⋅;𝐳¯)]−ℒ^∇𝐳2Fou​(𝐳¯)‖→a.s.0,\sup\_{\overline{\mathbf{z}}\in U}\Bigl\|I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\mathcal{H}^{(2)}(\cdot;\overline{\mathbf{z}})\right]-\widehat{\mathcal{L}}\_{\nabla^{2}\_{\mathbf{z}}}^{\mathrm{Fou}}(\overline{\mathbf{z}})\Bigr\|\xrightarrow[]{\mathrm{a.s.}}0, |  |

and combining ([A.12](https://arxiv.org/html/2602.06424v1#A1.E12 "In A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) with ([A.15](https://arxiv.org/html/2602.06424v1#A1.E15 "In A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) yields: for NN sufficient large, there exists q∈(0,1)q\in(0,1) such that

|  |  |  |
| --- | --- | --- |
|  | sup𝐳¯∈U‖𝑰−ℒ^∇𝐳2Fou​(𝐳¯)−1​IN,S¯RQMC​[ℋ(2)​(⋅;𝐳¯)]‖≤q.\sup\_{\overline{\mathbf{z}}\in U}\Bigl\|\boldsymbol{I}-\,\widehat{\mathcal{L}}\_{\nabla^{2}\_{\mathbf{z}}}^{\mathrm{Fou}}(\overline{\mathbf{z}})^{-1}\,I\_{N,\overline{S}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(2)}(\cdot;\overline{\mathbf{z}})\right]\Bigr\|\leq q. |  |

Hence, ‖TN​(𝐳1)−TN​(𝐳2)‖≤q​‖𝐳1−𝐳2‖\left\lVert T\_{N}(\mathbf{z}\_{1})-T\_{N}(\mathbf{z}\_{2})\right\rVert\leq q\,\left\lVert\mathbf{z}\_{1}-\mathbf{z}\_{2}\right\rVert for all 𝐳1,𝐳2∈U\mathbf{z}\_{1},\mathbf{z}\_{2}\in U, i.e., TNT\_{N} is a contraction on UU.

Step 2: TNT\_{N} maps U​(𝐳∗,η)U\left(\mathbf{z}^{\*},\eta\right) into itself.

By ([A.11](https://arxiv.org/html/2602.06424v1#A1.E11 "In A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) (restricted to UU) we also have

|  |  |  |  |
| --- | --- | --- | --- |
| (A.16) |  | sup𝐳∈U‖IN,S¯RQMC​[ℋ(1)​(⋅;𝐳)]−ℒ^∇𝐳Fou​(𝐳)‖→a.s.0.\sup\_{\mathbf{z}\in U}\Bigl\|I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\mathcal{H}^{(1)}(\cdot;\mathbf{z})\right]-\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}}^{\mathrm{Fou}}(\mathbf{z})\Bigr\|\xrightarrow[]{\mathrm{a.s.}}0. |  |

Since ℒ^∇Fou​(𝐳∗)=0\widehat{\mathcal{L}}\_{\nabla}^{\mathrm{Fou}}(\mathbf{z}^{\*})=0, it follows from
([A.13](https://arxiv.org/html/2602.06424v1#A1.E13 "In A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) and ([A.16](https://arxiv.org/html/2602.06424v1#A1.E16 "In A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) that
‖TN​(𝐳∗)−𝐳∗‖→a.s.0\left\lVert T\_{N}(\mathbf{z}^{\*})-\mathbf{z}^{\*}\right\rVert\xrightarrow[]{\mathrm{a.s.}}0.
Therefore, for all sufficiently large NN , we can enforce
‖TN​(𝐳∗)−𝐳∗‖≤(1−q)​η\left\lVert T\_{N}(\mathbf{z}^{\*})-\mathbf{z}^{\*}\right\rVert\leq(1-q)\eta, which implies that for any 𝐳∈U\mathbf{z}\in U,

|  |  |  |
| --- | --- | --- |
|  | ‖TN​(𝐳)−𝐳∗‖≤‖TN​(𝐳)−TN​(𝐳∗)‖+‖TN​(𝐳∗)−𝐳∗‖≤q​‖𝐳−𝐳∗‖+(1−q)​η≤η,\left\lVert T\_{N}(\mathbf{z})-\mathbf{z}^{\*}\right\rVert\leq\left\lVert T\_{N}(\mathbf{z})-T\_{N}(\mathbf{z}^{\*})\right\rVert+\left\lVert T\_{N}(\mathbf{z}^{\*})-\mathbf{z}^{\*}\right\rVert\leq q\,\left\lVert\mathbf{z}-\mathbf{z}^{\*}\right\rVert+(1-q)\eta\leq\eta, |  |

i.e. TN​(U)⊂UT\_{N}(U)\subset U.

By Steps 1–2, for all sufficiently large NN , TNT\_{N} is a Banach contraction on UU and maps UU into itself. Hence, by the Banach fixed point theorem, there exists a unique fixed point
𝐳N,S¯RQMC,∗∈U{\mathbf{z}}\_{N,\overline{S}}^{\mathrm{RQMC},\*}\in U such that
TN​(𝐳N,S¯RQMC,∗)=𝐳N,S¯RQMC,∗T\_{N}\!\left({\mathbf{z}}\_{N,\overline{S}}^{\mathrm{RQMC},\*}\right)={\mathbf{z}}\_{N,\overline{S}}^{\mathrm{RQMC},\*}, equivalently
IN,S¯RQMC​[ℋ(1)​(⋅;𝐳N,S¯RQMC,∗)]=0I\_{N,\overline{S}}^{\mathrm{RQMC}}\!\left[\mathcal{H}^{(1)}\left(\cdot;{\mathbf{z}}\_{N,\overline{S}}^{\mathrm{RQMC},\*}\right)\right]=0, Finally

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝐳N,S¯RQMC,∗−𝐳∗‖\displaystyle\left\lVert{\mathbf{z}}\_{N,\overline{S}}^{\mathrm{RQMC},\*}-\mathbf{z}^{\*}\right\rVert | =‖TN​(𝐳N,S¯RQMC,∗)−TN​(𝐳∗)+TN​(𝐳∗)−𝐳∗‖\displaystyle=\left\lVert T\_{N}\left({\mathbf{z}}\_{N,\overline{S}}^{\mathrm{RQMC},\*}\right)-T\_{N}\left(\mathbf{z}^{\*}\right)+T\_{N}\left(\mathbf{z}^{\*}\right)-\mathbf{z^{\*}}\right\rVert |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤q​‖𝐳N,S¯RQMC,∗−𝐳∗‖+‖TN​(𝐳∗)−𝐳∗‖\displaystyle\leq q\,\left\lVert{\mathbf{z}}\_{N,\overline{S}}^{\mathrm{RQMC},\*}-\mathbf{z}^{\*}\right\rVert+\left\lVert T\_{N}(\mathbf{z}^{\*})-\mathbf{z}^{\*}\right\rVert |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =q​‖𝐳N,S¯RQMC,∗−𝐳∗‖+‖ℒ^∇𝐳2Fou​(𝐳∗)−1​IN,S¯RQMC​[ℋ(1)​(⋅;𝐳∗)]‖\displaystyle=q\,\left\lVert{\mathbf{z}}\_{N,\overline{S}}^{\mathrm{RQMC},\*}-\mathbf{z}^{\*}\right\rVert+\left\lVert\,\widehat{\mathcal{L}}\_{\nabla^{2}\_{\mathbf{z}}}^{\mathrm{Fou}}({\mathbf{z^{\*}}})^{-1}\,I\_{N,\overline{S}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}(\cdot;{\mathbf{z^{\*}}})\right]\right\rVert |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤q​‖𝐳N,S¯RQMC,∗−𝐳∗‖+‖ℒ^∇𝐳2Fou​(𝐳∗)−1‖​‖IN,S¯RQMC​[ℋ(1)​(⋅;𝐳∗)]‖.\displaystyle\leq q\,\left\lVert{\mathbf{z}}\_{N,\overline{S}}^{\mathrm{RQMC},\*}-\mathbf{z}^{\*}\right\rVert+\left\lVert\widehat{\mathcal{L}}\_{\nabla^{2}\_{\mathbf{z}}}^{\mathrm{Fou}}({\mathbf{z^{\*}}})^{-1}\right\rVert\left\lVert I\_{N,\overline{S}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}(\cdot;{\mathbf{z^{\*}}})\right]\right\rVert. |  |

Rearranging yields

|  |  |  |
| --- | --- | --- |
|  | (1−q)​‖𝐳N,S¯RQMC,∗−𝐳∗‖≤‖ℒ^∇𝐳2Fou​(𝐳∗)−1‖​‖IN,S¯RQMC​[ℋ(1)​(⋅;𝐳∗)]‖,(1-q)\,\left\lVert{\mathbf{z}}\_{N,\overline{S}}^{\mathrm{RQMC},\*}-\mathbf{z}^{\*}\right\rVert\leq\left\lVert\widehat{\mathcal{L}}\_{\nabla^{2}\_{\mathbf{z}}}^{\mathrm{Fou}}({\mathbf{z^{\*}}})^{-1}\right\rVert\left\lVert I\_{N,\overline{S}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}(\cdot;{\mathbf{z^{\*}}})\right]\right\rVert, |  |

and ‖ℒ^∇𝐳2Fou​(𝐳∗)−1‖​‖IN,S¯RQMC​[ℋ(1)​(⋅;𝐳∗)]‖→a.s.0,\left\lVert\widehat{\mathcal{L}}\_{\nabla^{2}\_{\mathbf{z}}}^{\mathrm{Fou}}({\mathbf{z^{\*}}})^{-1}\right\rVert\left\lVert I\_{N,\overline{S}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}(\cdot;{\mathbf{z^{\*}}})\right]\right\rVert\xrightarrow[]{\mathrm{a.s.}}0,
we conclude that 𝐳N,S¯RQMC,∗→a.s.𝐳∗{\mathbf{z}}\_{N,\overline{S}}^{\mathrm{RQMC},\*}\xrightarrow[]{\mathrm{a.s.}}\mathbf{z}^{\*} as N→∞N\to\infty.

For the CLT in Theorem [5.9](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem9 "Theorem 5.9 (CLT for the Fourier-RQMC solution). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), we work under the joint regime Sshift→∞S\_{\mathrm{shift}}\to\infty. We therefore provide uniform convergence of the Fourier-RQMC estimators in Lemma [A.3](https://arxiv.org/html/2602.06424v1#A1.Thmtheorem3 "Lemma A.3 (Uniform convergence of Fourier-RQMC estimators with 𝑆_shift). ‣ A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), and then deduce consistency of the optimizer in Proposition [A.4](https://arxiv.org/html/2602.06424v1#A1.Thmtheorem4 "Proposition A.4 (Consistency of solution from Fourier-RQMC problem with 𝑆_shift). ‣ A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") with SshiftS\_{\mathrm{shift}}.

###### Lemma A.3 (Uniform convergence of Fourier-RQMC estimators with SshiftS\_{\mathrm{shift}}).

Fix N=N¯N=\overline{N}, let {𝐯n}n=1N¯\{\mathbf{v}\_{n}\}\_{n=1}^{\overline{N}} be the Sobol sequence, and {𝐯n(s)}s=1Sshift\left\{\mathbf{v}\_{n}^{(s)}\right\}\_{s=1}^{S\_{\mathrm{shift}}} be the sequence obtained by applying suitable randomization (i.e., nested uniform scrambling, digital shifting) to
{𝐯n}n=1N¯\{\mathbf{v}\_{n}\}\_{n=1}^{\overline{N}}.
Then the Fourier-RQMC estimators
IN¯,SshiftRQMC​[h~k,p(ν)​(⋅;𝐦k,p)]I\_{\overline{N},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}(\cdot;\mathbf{m}\_{k,p})\right]
satisfy a USLLN on Mk,pM\_{k,p}, that is,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.17) |  | sup𝐦k,p∈Mk,p‖IN¯,SshiftRQMC​[h~k,p(ν)​(⋅;𝐦k,p)]−g^k,p(ν),Fou​(𝐦k,p)‖\displaystyle\sup\_{\mathbf{m}\_{k,p}\in M\_{k,p}}\left\lVert I\_{\overline{N},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\!\left[\widetilde{h}\_{k,p}^{(\nu)}(\cdot;\mathbf{m}\_{k,p})\right]-\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}}(\mathbf{m}\_{k,p})\right\rVert | →a.s.0,\displaystyle\xrightarrow[]{\mathrm{a.s.}}0, |  |

as Sshift→∞S\_{\mathrm{shift}}\to\infty.

###### Proof.

The argument follows the same lines as the proof of
Lemma [5.5](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem5 "Lemma 5.5 (Uniform convergence of Fourier-RQMC estimators). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
The only difference is that, instead of taking expectations w.r.t. a generic random vector 𝐕∈[0,1]k\mathbf{V}\in[0,1]^{k}, we take expectations w.r.t. the random shift index SS. Since N¯\overline{N} and {𝐯n(s)}s=1Sshift\{\mathbf{v}\_{n}^{(s)}\}\_{s=1}^{S\_{\mathrm{shift}}} are i.i.d.  the standard SLLN applies without using [[42](https://arxiv.org/html/2602.06424v1#bib.bib53 "A Strong Law of Large Numbers for Scrambled Net Integration"), Theorem 4.2].
Consequently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | IN¯,SshiftRQMC​[δ𝐦¯k,p,η(ν)]\displaystyle I\_{\overline{N},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\!\left[\delta\_{\overline{\mathbf{m}}\_{k,p},\eta}^{(\nu)}\right] | →a.s.𝔼S​[IN¯RQMC​[δ𝐦¯k,p,η(ν)​(𝐯n(s))]],\displaystyle\xrightarrow[]{\mathrm{a.s.}}\mathbb{E}\_{S}\!\left[I\_{\overline{N}}^{\mathrm{RQMC}}\!\left[\delta\_{\overline{\mathbf{m}}\_{k,p},\eta}^{(\nu)}\left(\mathbf{v}\_{n}^{(s)}\right)\right]\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | IN¯,SshiftRQMC​[h~(ν)​(⋅;𝐦k,p)]\displaystyle I\_{\overline{N},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\!\left[\widetilde{h}^{(\nu)}\!\left(\cdot;\mathbf{m}\_{k,p}\right)\right] | →a.s.𝔼S​[IN¯RQMC​[h~(ν)​(𝐯n(s),𝐦k,p)]].\displaystyle\xrightarrow[]{\mathrm{a.s.}}\mathbb{E}\_{S}\!\left[I\_{\overline{N}}^{\mathrm{RQMC}}\!\left[\widetilde{h}^{(\nu)}\!\left(\mathbf{v}\_{n}^{(s)},\mathbf{m}\_{k,p}\right)\right]\right]. |  |

as Sshift→∞S\_{\mathrm{shift}}\to\infty, and

|  |  |  |
| --- | --- | --- |
|  | 𝔼S​[IN¯RQMC​[h~(ν)​(𝐯n(s),𝐦k,p)]]=g^k,p(ν),Fou​(𝐦k,p)\mathbb{E}\_{S}\!\left[I\_{\overline{N}}^{\mathrm{RQMC}}\!\left[\widetilde{h}^{(\nu)}\!\left(\mathbf{v}\_{n}^{(s)},\mathbf{m}\_{k,p}\right)\right]\right]=\widehat{g}\_{k,p}^{(\nu),\mathrm{Fou}}(\mathbf{m}\_{k,p}) |  |

.
∎

###### Proposition A.4 (Consistency of solution from Fourier-RQMC problem with SshiftS\_{\mathrm{shift}}).

Fix N=N¯N=\overline{N}, let {𝐯n}n=1N\{\mathbf{v}\_{n}\}\_{n=1}^{N} be the Sobol sequence, and {𝐯n(s)}s=1Sshift\left\{\mathbf{v}\_{n}^{(s)}\right\}\_{s=1}^{S\_{\mathrm{shift}}} be the sequence obtained by applying suitable randomization (i.e., nested uniform scrambling, digital shifting) to
{𝐯n}n=1N\{\mathbf{v}\_{n}\}\_{n=1}^{N}. Suppose that Assumption
([C3](https://arxiv.org/html/2602.06424v1#A1.I2.i3 "item C3 ‣ Assumption A.2 (Regularity conditions for the Fourier–RQMC problem). ‣ A.1 Additional Assumptions for the Error Analysis ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) holds.
Then, as Sshift→∞S\_{\mathrm{shift}}\to\infty, the Fourier-RQMC problem admits a unique solution
𝐳N¯,SshiftRQMC,∗∈𝒵{\mathbf{z}}\_{\overline{N},S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}\in\mathcal{Z}, and

|  |  |  |
| --- | --- | --- |
|  | 𝐳N¯,SshiftRQMC,∗→a.s.𝐳N¯,∞RQMC,∗.{\mathbf{z}}\_{\overline{N},S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}\xrightarrow[]{\mathrm{a.s.}}\mathbf{z}\_{\overline{N},\infty}^{\mathrm{RQMC},\*}. |  |

###### Proof.

The proof follows the same arguments as that of
Theorem [5.7](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem7 "Theorem 5.7 (Consistency of solution from Fourier-RQMC problem). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").
The only modification is that we invoke
Lemma [A.3](https://arxiv.org/html/2602.06424v1#A1.Thmtheorem3 "Lemma A.3 (Uniform convergence of Fourier-RQMC estimators with 𝑆_shift). ‣ A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") to obtain uniform convergence of the component integrands under random shifting. Moreover, by Assumption ([C3](https://arxiv.org/html/2602.06424v1#A1.I2.i3 "item C3 ‣ Assumption A.2 (Regularity conditions for the Fourier–RQMC problem). ‣ A.1 Additional Assumptions for the Error Analysis ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), the limiting solution
𝐳N¯,∞RQMC,∗\mathbf{z}\_{\overline{N},\infty}^{\mathrm{RQMC},\*} is strongly regular.
As a result, the same Banach fixed-point argument applies to
IN¯,∞RQMC​[ℋ(0)],I\_{\overline{N},\infty}^{\mathrm{RQMC}}\!\left[\mathcal{H}^{(0)}\right],
which yields the desired consistency result.
∎

### A.4 Proof for Theorem [5.9](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem9 "Theorem 5.9 (CLT for the Fourier-RQMC solution). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")

We decompose

|  |  |  |
| --- | --- | --- |
|  | 𝐳N,SshiftRQMC,∗−𝐳∗=𝐳N,SshiftRQMC,∗−𝐳N,∞RQMC,∗⏟(A)+𝐳N,∞RQMC,∗−𝐳∗⏟(B).{\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}-\mathbf{z}^{\*}=\underbrace{{\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}-{\mathbf{z}}\_{N,\infty}^{\mathrm{RQMC},\*}}\_{(\mathrm{A})}+\underbrace{{\mathbf{z}}\_{N,\infty}^{\mathrm{RQMC},\*}-\mathbf{z}^{\*}}\_{(\mathrm{B})}. |  |

##### Term (A)

For each fixed NN,
Proposition [A.4](https://arxiv.org/html/2602.06424v1#A1.Thmtheorem4 "Proposition A.4 (Consistency of solution from Fourier-RQMC problem with 𝑆_shift). ‣ A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") yields

|  |  |  |
| --- | --- | --- |
|  | 𝐳N,SshiftRQMC,∗→a.s𝐳N,∞RQMC,∗,Sshift→∞.{\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}\xrightarrow[]{a.s}\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*},\qquad S\_{\mathrm{shift}}\to\infty. |  |

Moreover, by strong regularity at 𝐳N,∞RQMC,∗\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*} and the corresponding linearized equation (Definition [5.5](https://arxiv.org/html/2602.06424v1#S5.E5 "In Definition 5.6 (Strong regularity of optimal solution). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), we have the expansion

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐳N,SshiftRQMC,∗−𝐳N,∞RQMC,∗\displaystyle\mathbf{z}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}-\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*} | =−(IN,∞RQMC​[ℋ(2)​(⋅;𝐳N,∞RQMC,∗)])−1\displaystyle=-\Big(I\_{N,\infty}^{\mathrm{RQMC}}\!\big[\mathcal{H}^{(2)}(\,\cdot\,;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*})\big]\Big)^{-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(IN,∞RQMC​[ℋ(1)​(⋅;𝐳N,∞RQMC,∗)]−IN,SshiftRQMC​[ℋ(1)​(⋅;𝐳N,∞RQMC,∗)])+aN.\displaystyle\quad\times\Big(I\_{N,\infty}^{\mathrm{RQMC}}\!\big[\mathcal{H}^{(1)}(\,\cdot\,;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*})\big]-I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\!\big[\mathcal{H}^{(1)}(\,\cdot\,;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*})\big]\Big)+a\_{N}. |  |

where aN:=oℙ​(‖IN,∞RQMC​[ℋ(1)​(⋅;𝐳N,∞RQMC,∗)]−IN,SshiftRQMC​[ℋ(1)​(⋅;𝐳N,∞RQMC,∗)]‖)=oℙ​(Sshift−12),a\_{N}:=o\_{\mathbb{P}}\!\left(\left\lVert I\_{N,\infty}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}\big(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)\right]-I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}\big(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)\right]\right\rVert\right)=o\_{\mathbb{P}}\!\left(S\_{\mathrm{shift}}^{-\tfrac{1}{2}}\right),
the latter equality following from ([4.4](https://arxiv.org/html/2602.06424v1#S4.E4 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). Multiplying by Sshift\sqrt{S\_{\mathrm{shift}}} gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.18) |  | Sshift​(𝐳N,SshiftRQMC,∗−𝐳N,∞RQMC,∗)\displaystyle\sqrt{S\_{\mathrm{shift}}}\bigl(\mathbf{z}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}-\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\bigr) | =−[IN,∞RQMC​[ℋ(2)​(⋅;𝐳N,∞RQMC,∗)]]−1\displaystyle=-\left[I\_{N,\infty}^{\mathrm{RQMC}}\left[\mathcal{H}^{(2)}\big(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)\right]\right]^{-1} |  |
|  |  | ×Sshift​(IN,∞RQMC​[ℋ(1)​(⋅;𝐳N,∞RQMC,∗)]−IN,SshiftRQMC​[ℋ(1)​(⋅;𝐳N,∞RQMC,∗)])\displaystyle\quad\times\sqrt{S\_{\mathrm{shift}}}\left(I\_{N,\infty}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}\left(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\right)\right]-I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}\left(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\right)\right]\right) |  |
|  |  | +oℙ​(1).\displaystyle\quad+o\_{\mathbb{P}}(1). |  |

Since we use SshiftS\_{\mathrm{shift}} independent shifts, we can apply the multivariate CLT as Sshift→∞S\_{\mathrm{shift}}\to\infty,

|  |  |  |
| --- | --- | --- |
|  | Sshift​(IN,SshiftRQMC​[ℋ(1)​(⋅;𝐳N,∞RQMC,∗)]−IN,∞RQMC​[ℋ(1)​(⋅;𝐳N,∞RQMC,∗)])→law𝒩​(𝟎,𝑯N,∞RQMC​(𝐳N,∞RQMC,∗)),\sqrt{S\_{\mathrm{shift}}}\!\left(I\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}\big(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)\right]-I\_{N,\infty}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}\big(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)\right]\right)\ \xrightarrow[]{\mathrm{law}}\ \mathcal{N}\!\left(\mathbf{0},\,\boldsymbol{H}\_{N,\infty}^{\mathrm{RQMC}}\big(\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)\right), |  |

where
𝑯N,∞RQMC​(𝐳N,∞RQMC,∗)=Vars​(INRQMC​[ℋ(1)​(𝐯n(s),𝐳N,∞RQMC,∗)]).\boldsymbol{H}\_{N,\infty}^{\mathrm{RQMC}}\big(\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)=\mathrm{Var}\_{s}\!\Big(I\_{N}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}\big(\mathbf{v}\_{n}^{(s)},\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)\right]\Big).
Combining this with ([A.18](https://arxiv.org/html/2602.06424v1#A1.E18 "In Term (A) ‣ A.4 Proof for Theorem 5.9 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) and the invertibility of
IN,∞RQMC​[ℋ(2)​(⋅;𝐳N,∞RQMC,∗)]I\_{N,\infty}^{\mathrm{RQMC}}\left[\mathcal{H}^{(2)}\big(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)\right],
it yields

|  |  |  |
| --- | --- | --- |
|  | Sshift​(𝐳N,SshiftRQMC,∗−𝐳N,∞RQMC,∗)→law𝒩​(𝟎,𝑽N,∞RQMC​(⋅;𝐳N,∞RQMC,∗)),\sqrt{S\_{\mathrm{shift}}}\!\left({\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}-\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\right)\ \xrightarrow[]{\mathrm{law}}\ \mathcal{N}\!\left(\mathbf{0},\,\boldsymbol{V}\_{N,\infty}^{\mathrm{RQMC}}\big(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)\right), |  |

with the sandwich covariance

|  |  |  |
| --- | --- | --- |
|  | 𝑽N,∞RQMC​(⋅;𝐳N,∞RQMC,∗):=(IN,∞RQMC​[ℋ(2)​(⋅;𝐳N,∞RQMC,∗)])−1​𝑯N,∞RQMC​(𝐳N,∞RQMC,∗)​(IN,∞RQMC​[ℋ(2)​(⋅;𝐳N,∞RQMC,∗)])−1.\boldsymbol{V}\_{N,\infty}^{\mathrm{RQMC}}\big(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big):=\left(I\_{N,\infty}^{\mathrm{RQMC}}\left[\mathcal{H}^{(2)}\big(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)\right]\right)^{-1}\boldsymbol{H}\_{N,\infty}^{\mathrm{RQMC}}\big(\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)\left(I\_{N,\infty}^{\mathrm{RQMC}}\left[\mathcal{H}^{(2)}\big(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)\right]\right)^{-1}. |  |

##### Term (B)

By Theorem [5.7](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem7 "Theorem 5.7 (Consistency of solution from Fourier-RQMC problem). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"),

|  |  |  |
| --- | --- | --- |
|  | 𝐳N,∞RQMC,∗→a.s𝐳∗,N→∞.{\mathbf{z}}\_{N,\infty}^{\mathrm{RQMC},\*}\xrightarrow[]{a.s}\mathbf{z}^{\*},\qquad N\to\infty. |  |

for the joint regime, by Assumption [5.8](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem8 "Assumption 5.8. ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") ([i](https://arxiv.org/html/2602.06424v1#S5.I3.i1 "item i ‣ Assumption 5.8. ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")),
we have that term (B) is negligible at the Sshift​Nr\sqrt{S\_{\mathrm{shift}}}N^{r}scale. Hence,

|  |  |  |
| --- | --- | --- |
|  | Sshift​Nr​(𝐳N,SshiftRQMC,∗−𝐳∗)=Sshift​Nr​(𝐳N,SshiftRQMC,∗−𝐳N,∞RQMC,∗)+oℙ​(1),\sqrt{S\_{\mathrm{shift}}}N^{r}\!\left({\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}-\mathbf{z}^{\*}\right)=\sqrt{S\_{\mathrm{shift}}}N^{r}\!\left({\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}-\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\right)+o\_{\mathbb{P}}(1), |  |

and the limiting distribution is governed by term (A).

Finally, to identify the limiting covariance at 𝐳∗\mathbf{z}^{\*}, we use

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝑵2​r​𝑽N,∞RQMC​(⋅;𝐳N,∞RQMC,∗)−𝑽​(𝐳∗)‖≤\displaystyle\left\lVert\boldsymbol{N}^{2r}\boldsymbol{V}\_{N,\infty}^{\mathrm{RQMC}}\big(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)-\boldsymbol{V}\left(\mathbf{z}^{\*}\right)\right\rVert\;\leq | N2​r​‖𝑽N,∞RQMC​(⋅;𝐳N,∞RQMC,∗)−𝑽N,∞RQMC​(⋅;𝐳∗)‖\displaystyle\;N^{2r}\left\lVert\boldsymbol{V}\_{N,\infty}^{\mathrm{RQMC}}\big(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)-\boldsymbol{V}\_{N,\infty}^{\mathrm{RQMC}}\big(\cdot;\mathbf{z}^{\*}\big)\right\rVert |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +‖N2​r​𝑽N,∞RQMC​(⋅;𝐳∗)−𝑽​(𝐳∗)‖.\displaystyle\;+\;\left\lVert N^{2r}\boldsymbol{V}\_{N,\infty}^{\mathrm{RQMC}}\big(\cdot;\mathbf{z}^{\*}\big)-\boldsymbol{V}\left(\mathbf{z}^{\*}\right)\right\rVert. |  |

As N→∞N\to\infty, the first term converges to 0 by continuity of 𝑽N,∞RQMC​(⋅)\boldsymbol{V}\_{N,\infty}^{\mathrm{RQMC}}(\cdot) on a neighborhood of 𝐳∗\mathbf{z}^{\*}
together with 𝐳N,∞RQMC,∗→𝐳∗{\mathbf{z}}\_{N,\infty}^{\mathrm{RQMC},\*}\to\mathbf{z}^{\*}. The second term converges to 0 by the
USLLN with NN of
IN,∞RQMC​[ℋ(2)]→ℒ^∇𝐳2FouI\_{N,\infty}^{\mathrm{RQMC}}\left[\mathcal{H}^{(2)}\right]\to\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}^{2}}^{\mathrm{Fou}} from ([A.11](https://arxiv.org/html/2602.06424v1#A1.E11 "In A.3 Proof for Theorem 5.7 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), the uniform
invertibility of ℒ^∇𝐳2Fou\widehat{\mathcal{L}}\_{\nabla\_{\mathbf{z}}^{2}}^{\mathrm{Fou}} on that neighborhood due to the strong regularity of 𝐳∗\mathbf{z}^{\*} and N2​r​HN,∞​(𝐳∗)→𝑯​(𝐳∗)N^{2r}H\_{N,\infty}\big(\mathbf{z}^{\*}\big)\xrightarrow{}\boldsymbol{H}(\mathbf{z}^{\*}), from Assumption [5.8](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem8 "Assumption 5.8. ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") ([ii](https://arxiv.org/html/2602.06424v1#S5.I3.i2 "item ii ‣ Assumption 5.8. ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).
Therefore,
𝑽N,∞RQMC​(⋅;𝐳N,∞RQMC,∗)→𝑽​(𝐳∗).\boldsymbol{V}\_{N,\infty}^{\mathrm{RQMC}}\big(\cdot;\mathbf{z}\_{N,\infty}^{\mathrm{RQMC},\*}\big)\to\boldsymbol{V}(\mathbf{z}^{\*}).
By Slutsky’s theorem, as Sshift→∞S\_{\mathrm{shift}}\to\infty and N→∞N\to\infty, we have

|  |  |  |
| --- | --- | --- |
|  | Sshift​Nr​(𝐳N,SshiftRQMC,∗−𝐳∗)→law𝒩​(𝟎,𝑽​(𝐳∗)).\sqrt{S\_{\mathrm{shift}}}N^{r}\!\left({\mathbf{z}}\_{N,S\_{\mathrm{shift}}}^{\mathrm{RQMC},\*}-\mathbf{z}^{\*}\right)\ \xrightarrow[]{\mathrm{law}}\ \mathcal{N}\!\left(\mathbf{0},\ \boldsymbol{V}\left(\mathbf{z}^{\*}\right)\right). |  |

### A.5 Proof for Corrolary [5.13](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem13 "Corollary 5.13 (Single-level Fourier-RQMC work complexity). ‣ 5.3.1 Single-level Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")

For a fixed NN and SshiftS\_{\mathrm{shift}} digital shifts, the total work decomposes into a one-off sampling cost and the cumulative cost of JJ SQP iterations:

|  |  |  |  |
| --- | --- | --- | --- |
| (A.19) |  | WsingRQMC​(N,J)=Cdraw​(N)+J​Citer​(N,d).W\_{\mathrm{sing}}^{\mathrm{RQMC}}(N,J)=C\_{\mathrm{draw}}(N)+J\,C\_{\mathrm{iter}}(N,d). |  |

* •

  *Sampling cost.* For each k∈ℐqℓk\in\mathcal{I}\_{q\_{\ell}} we generate a single fixed RQMC design. The associated cost is

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (A.20) |  | Cdraw​(N):=𝒪​(N​Sshift​cdraw),cdraw:=maxk∈ℐqℓ⁡cdraw,k,C\_{\mathrm{draw}}(N):=\mathcal{O}\left(NS\_{\mathrm{shift}}\,c\_{\mathrm{draw}}\right),\qquad c\_{\mathrm{draw}}:=\max\_{k\in\mathcal{I}\_{q\_{\ell}}}c\_{\mathrm{draw},k}, |  |

  where cdraw,kc\_{\mathrm{draw},k} denotes the cost of drawing one sample at the dependence level kk.
* •

  *Per-iteration cost.*
  Each SQP iteration incurs the following costs:

  + –

    *Function and gradient evaluation.*
    Evaluating the aggregate integrands h~(ν)\widetilde{h}^{(\nu)} involves summing over all components, hence

    |  |  |  |  |
    | --- | --- | --- | --- |
    | (A.21) |  | Ceval​(N):=𝒪​(N​Sshift​ceval),ceval≈cmax​Ncomp,C\_{\mathrm{eval}}(N):=\mathcal{O}\left(NS\_{\mathrm{shift}}\,c\_{\mathrm{eval}}\right),\qquad c\_{\mathrm{eval}}\approx c\_{\max}\,N\_{\mathrm{comp}}, |  |

    where cmaxc\_{\max} denotes the maximum cost ck,pc\_{k,p} incurred in evaluating the component integrands h~k,p(ν)\widetilde{h}\_{k,p}^{(\nu)}.

    |  |  |  |  |
    | --- | --- | --- | --- |
    | (A.22) |  | cmax:=maxν∈{0,1}⁡maxk∈ℐqℓ⁡max𝐩∈ℐk⁡ck,p,Ncomp:=∑k∈ℐqℓ∑𝐩∈ℐk1.c\_{\max}:=\max\_{\nu\in\{0,1\}}\max\_{k\in\mathcal{I}\_{q\_{\ell}}}\ \max\_{\mathbf{p}\in\mathcal{I}\_{k}}c\_{k,p},\qquad N\_{\mathrm{comp}}:=\sum\_{k\in\mathcal{I}\_{q\_{\ell}}}\ \sum\_{\mathbf{p}\in\mathcal{I}\_{k}}1. |  |
  + –

    *BFGS update.*
    Forming the BFGS update costs 𝒪​(d2)\mathcal{O}(d^{2}) (outer products and matrix-vector products).
    In addition, we still incur the evaluation cost Ceval​(N)C\_{\mathrm{eval}}(N) to compute the required gradient differences.
  + –

    *QP solve.*
    With one active inequality constraint, solving the resulting dense QP costs 𝒪​((d+1)3)\mathcal{O}((d+1)^{3}).

  Collecting the dominant terms
  , the per-iteration cost can be summarized as

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (A.23) |  | Citer​(N,d)=𝒪​(N​Sshift​ceval+(d+1)3)C\_{\mathrm{iter}}(N,d)=\mathcal{O}\left(NS\_{\mathrm{shift}}\,c\_{\mathrm{eval}}+(d+1)^{3}\right) |  |

By ([5.8](https://arxiv.org/html/2602.06424v1#S5.E8 "In 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), choosing
N=N​(ε)N=N(\varepsilon) such that εstatRQMC​(N)≤ε/2\varepsilon\_{\mathrm{stat}}^{\mathrm{RQMC}}(N)\leq\varepsilon/2 yields

|  |  |  |
| --- | --- | --- |
|  | N​(ε)=𝒪​(ε−1r).N(\varepsilon)=\mathcal{O}\!\left(\varepsilon^{-\tfrac{1}{r}}\right). |  |

Moreover, by ([A.30](https://arxiv.org/html/2602.06424v1#A1.E30 "In A.7 Proof for Proposition 5.14 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), achieving εopt​(j)≤ε/2\varepsilon\_{\mathrm{opt}}(j)\leq\varepsilon/2 requires

|  |  |  |
| --- | --- | --- |
|  | J​(ε)=𝒪​(log⁡log⁡(1/ε)).J(\varepsilon)=\mathcal{O}\!\big(\log\log(1/\varepsilon)\big). |  |

Substituting the choices N​(ε)N(\varepsilon) and J​(ε)J(\varepsilon) into ([A.19](https://arxiv.org/html/2602.06424v1#A1.E19 "In A.5 Proof for Corrolary 5.13 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) yields

|  |  |  |
| --- | --- | --- |
|  | WsingRQMC​(ε)=𝒪​(ε−1r​log⁡log⁡(1/ε)),W\_{\mathrm{sing}}^{\mathrm{RQMC}}(\varepsilon)=\mathcal{O}\!\Big(\varepsilon^{-\tfrac{1}{r}}\log\log(1/\varepsilon)\Big), |  |

This concludes the proof.

### A.6 Proof for Corollary [5.15](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem15 "Corollary 5.15 (Work-optimal multilevel allocation). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")

Following Algorithm [4](https://arxiv.org/html/2602.06424v1#alg4 "Algorithm 4 ‣ 4.2 Iteration-Indexed Multilevel Fourier–RQMC Approximation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), at each level jj we generate a fresh set of
SshiftS\_{\mathrm{shift}} independent digital shifts
{𝐯n(s,j)}s=1Sshift\left\{\mathbf{v}\_{n}^{(s,j)}\right\}\_{s=1}^{S\_{\mathrm{shift}}}.
The resulting per-iteration cost follows the same structure as the single-level case ([A.23](https://arxiv.org/html/2602.06424v1#A1.E23 "In 2nd item ‣ A.5 Proof for Corrolary 5.13 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"))
where the per-sample cost at level jj is

|  |  |  |  |
| --- | --- | --- | --- |
| (A.24) |  | cj:=ceval(j)+cdraw(j).c\_{j}:=c\_{\mathrm{eval}}^{(j)}+c\_{\mathrm{draw}}^{(j)}. |  |

The per-drawing cost at level jj is defined as
cdraw(j):=maxk∈ℐqℓ⁡cdraw,k(j)c\_{\mathrm{draw}}^{(j)}:=\max\_{k\in\mathcal{I}\_{q\_{\ell}}}c\_{\mathrm{draw},k}^{(j)},
while the per-evaluation cost at level jj satisfies
ceval(j)≈cmax(j)​Ncompc\_{\mathrm{eval}}^{(j)}\approx c\_{\max}^{(j)}\,N\_{\mathrm{comp}},
where
cmax(j):=maxν∈{0,1}⁡maxk∈ℐqℓ⁡max𝐩∈ℐk⁡ck,p(j)c\_{\max}^{(j)}:=\max\_{\nu\in\{0,1\}}\max\_{k\in\mathcal{I}\_{q\_{\ell}}}\max\_{\mathbf{p}\in\mathcal{I}\_{k}}c\_{k,p}^{(j)}
denotes the maximum cost incurred in evaluating the level-jj component difference integrands
Δ​h~k,p(ν,j)\Delta\widetilde{h}\_{k,p}^{(\nu,j)}. The MSE at level JJ is computed as

|  |  |  |  |
| --- | --- | --- | --- |
| (A.25) |  | MSEstatRQMC=∑j=1J𝑫jSshift​Nj2​r.\mathrm{MSE}\_{\mathrm{stat}}^{\mathrm{RQMC}}=\sum\_{j=1}^{J}\frac{\boldsymbol{D}\_{j}}{S\_{\mathrm{shift}}N\_{j}^{2r}}. |  |

From ([A.24](https://arxiv.org/html/2602.06424v1#A1.E24 "In A.6 Proof for Corollary 5.15 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) and ([A.25](https://arxiv.org/html/2602.06424v1#A1.E25 "In A.6 Proof for Corollary 5.15 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), our constrained optimization problem is

|  |  |  |  |
| --- | --- | --- | --- |
| (A.26) |  | minNj≥1​∑j=1JSshift​cj​Nj s.t ∑j=1J𝑫jSshift​Nj2​r≤ε24.\min\_{N\_{j}\geq 1}\sum\_{j=1}^{J}S\_{\mathrm{shift}}c\_{j}N\_{j}\qquad\text{ s.t }\quad\sum\_{j=1}^{J}\frac{\boldsymbol{D}\_{j}}{S\_{\mathrm{shift}}N\_{j}^{2r}}\leq\frac{\varepsilon^{2}}{4}. |  |

The Lagrangian associated with ([A.26](https://arxiv.org/html/2602.06424v1#A1.E26 "In A.6 Proof for Corollary 5.15 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). with μ>0\mu>0 is:

|  |  |  |
| --- | --- | --- |
|  | ℒ​(Nj,μ)=∑j=1JSshift​cj​Nj+μ​(∑j=1J4​𝑫jSshift​Nj2​r−ε2).\mathcal{L}(N\_{j},\mu)=\sum\_{j=1}^{J}S\_{\mathrm{shift}}c\_{j}N\_{j}+\mu\left(\sum\_{j=1}^{J}\frac{4\boldsymbol{D}\_{j}}{S\_{\mathrm{shift}}N\_{j}^{2r}}-\varepsilon^{2}\right). |  |

The F.O.C. gives:

|  |  |  |  |
| --- | --- | --- | --- |
| (A.27) |  | {∂ℒ∂Nj=Sshift​cj−8​μ​r​𝑫jSshift​Nj2​r+1=0,∂ℒ∂μ=∑j=1J4​𝑫jSshift​Nj2​r−ε2=0.\left\{\begin{aligned} \frac{\partial\mathcal{L}}{\partial N\_{j}}&=S\_{\mathrm{shift}}c\_{j}-\frac{8\mu r\boldsymbol{D}\_{j}}{S\_{\mathrm{shift}}N\_{j}^{2r+1}}=0,\\[4.0pt] \frac{\partial\mathcal{L}}{\partial\mu}&=\sum\_{j=1}^{J}\frac{4\boldsymbol{D}\_{j}}{S\_{\mathrm{shift}}N\_{j}^{2r}}-\varepsilon^{2}=0.\end{aligned}\right. |  |

From the first equation in ([A.27](https://arxiv.org/html/2602.06424v1#A1.E27 "In A.6 Proof for Corollary 5.15 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
| (A.28) |  | Nj=(8​μ​r​𝑫jSshift2​cj)12​r+1,N\_{j}=\left(\frac{8\mu r\boldsymbol{D}\_{j}}{S^{2}\_{\mathrm{shift}}c\_{j}}\right)^{\frac{1}{2r+1}}, |  |

which yields ([5.11](https://arxiv.org/html/2602.06424v1#S5.E11 "In Corollary 5.15 (Work-optimal multilevel allocation). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). Replacing ([A.28](https://arxiv.org/html/2602.06424v1#A1.E28 "In A.6 Proof for Corollary 5.15 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) into the second
equation in ([A.27](https://arxiv.org/html/2602.06424v1#A1.E27 "In A.6 Proof for Corollary 5.15 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), we find

|  |  |  |  |
| --- | --- | --- | --- |
| (A.29) |  | 4​(8​r​μ)−2​r2​r+1​Sshift2​r−12​r+1​S1=ε2,4\left(8r\mu\right)^{-\tfrac{2r}{2r+1}}S\_{\mathrm{shift}}^{\tfrac{2r-1}{2r+1}}S\_{1}=\varepsilon^{2}, |  |

Combining ([A.28](https://arxiv.org/html/2602.06424v1#A1.E28 "In A.6 Proof for Corollary 5.15 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) with ([A.29](https://arxiv.org/html/2602.06424v1#A1.E29 "In A.6 Proof for Corollary 5.15 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")),
we have ([5.12](https://arxiv.org/html/2602.06424v1#S5.E12 "In Corollary 5.15 (Work-optimal multilevel allocation). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

### A.7 Proof for Proposition [5.14](https://arxiv.org/html/2602.06424v1#S5.E14 "In Proposition 5.18 (Adaptive choice of the sample size 𝑁_𝑗). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")

From Theorem [5.2](https://arxiv.org/html/2602.06424v1#S5.E2 "In Theorem 5.3. ‣ 5.1 Optimization error ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), there exists an index
JlocJ\_{\mathrm{loc}} such that for all j≥Jlocj\geq J\_{\mathrm{loc}},

|  |  |  |  |
| --- | --- | --- | --- |
| (A.30) |  | ‖𝐳(j)−𝐳∗‖≤ηj−1​‖𝐳(j−1)−𝐳∗‖,with ​ηj−1→0.\left\lVert\mathbf{z}^{(j)}-{\mathbf{z}}^{\*}\right\rVert\leq\eta\_{j-1}\,\left\lVert{\mathbf{z}}^{(j-1)}-{\mathbf{z}}^{\*}\right\rVert,\qquad\text{with }\ \eta\_{j-1}\to 0. |  |

Applying the reverse triangle inequality and the triangle inequality yields, for all j≥Jlocj\geq J\_{\mathrm{loc}},

|  |  |  |  |
| --- | --- | --- | --- |
| (A.31) |  | (1−ηj−1)​‖𝐳(j−1)−𝐳∗‖≤‖𝐳(j)−𝐳(j−1)‖≤(1+ηj−1)​‖𝐳(j−1)−𝐳∗‖.\left(1-\eta\_{j-1}\right)\left\lVert{\mathbf{z}}^{(j-1)}-{\mathbf{z}}^{\*}\right\rVert\leq\left\lVert\mathbf{z}^{(j)}-\mathbf{z}^{(j-1)}\right\rVert\leq\left(1+\eta\_{j-1}\right)\left\lVert{\mathbf{z}}^{(j-1)}-{\mathbf{z}}^{\*}\right\rVert. |  |

Consequently, combining ([A.31](https://arxiv.org/html/2602.06424v1#A1.E31 "In A.7 Proof for Proposition 5.14 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) at indices jj and j+1j+1 with ([A.30](https://arxiv.org/html/2602.06424v1#A1.E30 "In A.7 Proof for Proposition 5.14 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.32) |  | ‖𝐳(j+1)−𝐳(j)‖‖𝐳(j)−𝐳(j−1)‖\displaystyle\frac{\left\lVert\mathbf{z}^{(j+1)}-\mathbf{z}^{(j)}\right\rVert}{\left\lVert\mathbf{z}^{(j)}-\mathbf{z}^{(j-1)}\right\rVert} | ≤(1+ηj)​‖𝐳(j)−𝐳∗‖(1−ηj−1)​‖𝐳(j−1)−𝐳∗‖\displaystyle\leq\frac{\left(1+\eta\_{j}\right)\left\lVert{\mathbf{z}}^{(j)}-{\mathbf{z}}^{\*}\right\rVert}{\left(1-\eta\_{j-1}\right)\left\lVert{\mathbf{z}}^{(j-1)}-{\mathbf{z}}^{\*}\right\rVert} |  |
|  |  | ≤1+ηj1−ηj−1​ηj−1⏟:=η~j−1.\displaystyle\leq\underbrace{\frac{1+\eta\_{j}}{1-\eta\_{j-1}}\eta\_{j-1}}\_{:=\widetilde{\eta}\_{j-1}}. |  |

Since ηj−1→0\eta\_{j-1}\to 0 as J→∞J\to\infty, we also have η~j−1→0\widetilde{\eta}\_{j-1}\to 0. For each j≥Jlocj\geq J\_{\mathrm{loc}} there exists a finite constant
Cj−1C\_{j-1} such that

|  |  |  |  |
| --- | --- | --- | --- |
| (A.33) |  | ‖𝐳(j)−𝐳(j−1)‖≤Cj−1​η~j−1.\left\lVert\mathbf{z}^{(j)}-\mathbf{z}^{(j-1)}\right\rVert\leq C\_{j-1}\widetilde{\eta}\_{j-1}. |  |

Combine ([A.33](https://arxiv.org/html/2602.06424v1#A1.E33 "In A.7 Proof for Proposition 5.14 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) with Assumption [5.17](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem17 "Assumption 5.17. ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), for all j≥Jlocj\geq J\_{\mathrm{loc}}, we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.34) |  | 𝔼​[‖INj,SshiftRQMC​[Δ​ℋ(1)​(⋅;𝐳(j),𝐳(j−1))]‖2]\displaystyle\mathbb{E}\left[\left\lVert{I}\_{N\_{j},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\mathcal{H}^{(1)}\left(\cdot;\mathbf{z}^{(j)},\mathbf{z}^{(j-1)}\right)\right]\right\rVert^{2}\right] | ≤CH,j−1​ηj−12.\displaystyle\leq C\_{H,j-1}\eta\_{j-1}^{2}. |  |

where CH,j−1:=LH​Cj−12C\_{H,j-1}:=L\_{H}C\_{j-1}^{2}. Moreover, for a random vector 𝐗∈ℝd\mathbf{X}\in\mathbb{R}^{d},

|  |  |  |
| --- | --- | --- |
|  | Var​[𝐗]=𝔼​[𝐗𝐗⊤]−𝔼​[𝐗]​𝔼​[𝐗⊤]⪯𝔼​[𝐗𝐗⊤].\text{Var}\left[\mathbf{X}\right]=\mathbb{E}\left[\mathbf{X}\mathbf{X}^{\top}\right]-\mathbb{E}\left[\mathbf{X}\right]\mathbb{E}\left[\mathbf{X}^{\top}\right]\preceq\mathbb{E}\left[\mathbf{X}\mathbf{X}^{\top}\right]. |  |

Using Jensen’s inequality for the matrix norm, we have

|  |  |  |
| --- | --- | --- |
|  | ‖Var​[𝐗]‖≤‖𝔼​[𝐗𝐗⊤]‖≤𝔼​[‖𝐗𝐗⊤‖]=𝔼​[‖𝐗‖2].\left\lVert\text{Var}\left[\mathbf{X}\right]\right\rVert\leq\left\lVert\mathbb{E}\left[\mathbf{X}\mathbf{X}^{\top}\right]\right\rVert\leq\mathbb{E}\left[\left\lVert\mathbf{X}\mathbf{X}^{\top}\right\rVert\right]=\mathbb{E}\left[\left\lVert\mathbf{X}\right\rVert^{2}\right]. |  |

Applying this to
𝐗=INj,SshiftRQMC​[Δ​ℋ(1)​(⋅;𝐳(j),𝐳(j−1))]\mathbf{X}={I}\_{N\_{j},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\mathcal{H}^{(1)}\left(\cdot;\mathbf{z}^{(j)},\mathbf{z}^{(j-1)}\right)\right]
and using ([A.34](https://arxiv.org/html/2602.06424v1#A1.E34 "In A.7 Proof for Proposition 5.14 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) gives

|  |  |  |  |
| --- | --- | --- | --- |
| (A.35) |  | 𝑫j=‖Var​[INj,SshiftRQMC​[Δ​ℋ(1)​(⋅;𝐳(j),𝐳(j−1))]]‖≤𝔼​[‖INj,SshiftRQMC​[Δ​ℋ(1)​(⋅;𝐳(j),𝐳(j−1))]‖2]≤CH,j−1​ηj−12.\boldsymbol{D}\_{j}=\left\lVert\text{Var}\left[{I}\_{N\_{j},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\mathcal{H}^{(1)}\left(\cdot;\mathbf{z}^{(j)},\mathbf{z}^{(j-1)}\right)\right]\right]\right\rVert\leq\mathbb{E}\left[\left\lVert{I}\_{N\_{j},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\Delta\mathcal{H}^{(1)}\left(\cdot;\mathbf{z}^{(j)},\mathbf{z}^{(j-1)}\right)\right]\right\rVert^{2}\right]\leq C\_{H,j-1}\eta\_{j-1}^{2}. |  |

Using this variance contraction property of 𝑫j\boldsymbol{D}\_{j}, we substitute it into ([5.11](https://arxiv.org/html/2602.06424v1#S5.E11 "In Corollary 5.15 (Work-optimal multilevel allocation). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) to obtain the expression in
([A.28](https://arxiv.org/html/2602.06424v1#A1.E28 "In A.6 Proof for Corollary 5.15 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), with constant Cloc,j−1C\_{\mathrm{loc},j-1}. Moreover, by fixing
ηj−1=η\eta\_{j-1}=\eta, we recover the formula in ([5.14](https://arxiv.org/html/2602.06424v1#S5.E14 "In Proposition 5.18 (Adaptive choice of the sample size 𝑁_𝑗). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) with constant ClocC\_{\mathrm{loc}}. This
completes the proof.

### A.8 Proof for Proposition [5.20](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem20 "Proposition 5.20 (Computational Complexity for multilevel Fourier-RQMC). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")

In the single-level RQMC setting, the uniform number of points
NsingN\_{\mathrm{sing}} is used for all iterations jj, and is derived from
([5.8](https://arxiv.org/html/2602.06424v1#S5.E8 "In 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) as

|  |  |  |  |
| --- | --- | --- | --- |
| (A.36) |  | Nsing=(𝑽maxSshift​ε2)12​r,N\_{\mathrm{sing}}=\left(\frac{\boldsymbol{V}\_{\max}}{S\_{\mathrm{shift}}\,\varepsilon^{2}}\right)^{\tfrac{1}{2r}}, |  |

where 𝑽max:=max1≤j≤J⁡𝑽j\boldsymbol{V}\_{\max}:=\max\_{1\leq j\leq J}\boldsymbol{V}\_{j},
𝑽j:=‖Var​(IN1,SshiftRQMC​[ℋ(1)​(⋅;𝐳(j))])‖\boldsymbol{V}\_{j}:=\left\lVert\mathrm{Var}\!\left({I}\_{N\_{1},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}\left(\cdot;\mathbf{z}^{(j)}\right)\right]\right)\right\rVert,
and

|  |  |  |
| --- | --- | --- |
|  | 𝑽1=𝑫1=‖Var​(IN1,SshiftRQMC​[ℋ(1)​(⋅;𝐳(1))])‖.\boldsymbol{V}\_{1}=\boldsymbol{D}\_{1}=\left\lVert\mathrm{Var}\!\left(I\_{N\_{1},S\_{\mathrm{shift}}}^{\mathrm{RQMC}}\left[\mathcal{H}^{(1)}\left(\cdot;\mathbf{z}^{(1)}\right)\right]\right)\right\rVert. |  |

The total work across all JJ iterations is

|  |  |  |  |
| --- | --- | --- | --- |
| (A.37) |  | WsingRQMC​(ε)=∑j=1JSshift​c​Nsing≈J​Sshift​𝑽max12​r​ε−1r.W^{\text{RQMC}}\_{\mathrm{sing}}(\varepsilon)=\sum\_{j=1}^{J}S\_{\mathrm{shift}}\,c\,N\_{\mathrm{sing}}\approx J\,S\_{\mathrm{shift}}\,\boldsymbol{V}\_{\max}^{\tfrac{1}{2r}}\,\varepsilon^{-\tfrac{1}{r}}. |  |

From ([5.12](https://arxiv.org/html/2602.06424v1#S5.E12 "In Corollary 5.15 (Work-optimal multilevel allocation). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
| (A.38) |  | WsingRQMC​(ε)WmultRQMC​(ε)≈J​𝑽max12​r(V112​r+1+∑j=2Jloc−1𝑫j12​r+1+∑j=JlocJ𝑫j12​r+1)2​r+12​r.\frac{W^{\text{RQMC}}\_{\mathrm{sing}}(\varepsilon)}{W^{\text{RQMC}}\_{\mathrm{mult}}(\varepsilon)}\approx\frac{J\,\boldsymbol{V}\_{\max}^{\tfrac{1}{2r}}}{\left(V\_{1}^{\tfrac{1}{2r+1}}+\sum\_{j=2}^{J\_{\mathrm{loc}}-1}\boldsymbol{D}\_{j}^{\tfrac{1}{2r+1}}+\sum\_{j=J\_{\mathrm{loc}}}^{J}\boldsymbol{D}\_{j}^{\tfrac{1}{2r+1}}\right)^{\tfrac{2r+1}{2r}}}. |  |

Using the contraction property for 𝑫j\boldsymbol{D}\_{j} from Proposition [5.14](https://arxiv.org/html/2602.06424v1#S5.E14 "In Proposition 5.18 (Adaptive choice of the sample size 𝑁_𝑗). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
| (A.39) |  | ∑j=JlocJ𝑫j12​r+1=Cloc12​r+1​∑j=JlocJ(η12​r+1)2​j−2=Cloc12​r+1​η2​Jloc−22​r+1−η2​J2​r+11−η22​r+1.\sum\_{j=J\_{\mathrm{loc}}}^{J}\boldsymbol{D}\_{j}^{\tfrac{1}{2r+1}}=C\_{\mathrm{loc}}^{\tfrac{1}{2r+1}}\sum\_{j=J\_{\mathrm{loc}}}^{J}\!\left(\eta^{\tfrac{1}{2r+1}}\right)^{\!2j-2}=C\_{\mathrm{loc}}^{\tfrac{1}{2r+1}}\frac{\eta^{\tfrac{2J\_{\mathrm{loc}}-2}{2r+1}}-\eta^{\tfrac{2J}{2r+1}}}{1-\eta^{\tfrac{2}{2r+1}}}. |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | ∑j=JlocJ𝑫j12​r+1→J→∞Cloc12​r+1​η2​Jloc−22​r+11−η22​r+1=𝒪​(1),\sum\_{j=J\_{\mathrm{loc}}}^{J}\boldsymbol{D}\_{j}^{\tfrac{1}{2r+1}}\xrightarrow[J\to\infty]{}C\_{\mathrm{loc}}^{\tfrac{1}{2r+1}}\frac{\eta^{\tfrac{2J\_{\mathrm{loc}}-2}{2r+1}}}{1-\eta^{\tfrac{2}{2r+1}}}=\mathcal{O}(1), |  |

which implies ([5.15](https://arxiv.org/html/2602.06424v1#S5.E15 "In Proposition 5.20 (Computational Complexity for multilevel Fourier-RQMC). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). Finally, the multilevel work complexity ([5.16](https://arxiv.org/html/2602.06424v1#S5.E16 "In Proposition 5.20 (Computational Complexity for multilevel Fourier-RQMC). ‣ 5.3.2 Multilevel Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) follows from Corollary [5.10](https://arxiv.org/html/2602.06424v1#S5.E10 "In Corollary 5.13 (Single-level Fourier-RQMC work complexity). ‣ 5.3.1 Single-level Fourier-RQMC ‣ 5.3 Computational Complexity ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

## Appendix B Supplementary results for Section [3.1](https://arxiv.org/html/2602.06424v1#S3.SS1 "3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")

### B.1 Damping rule and convexity properties

#### B.1.1 Proof for Corollary [3.7](https://arxiv.org/html/2602.06424v1#S3.Thmtheorem7 "Corollary 3.7 (Damping Rule). ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")

Following the construction in Appendix [E.2](https://arxiv.org/html/2602.06424v1#A5.SS2 "E.2 Fourier transform of the given loss functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), the loss components
ℓk,p(ν)\ell^{(\nu)}\_{k,p} (for the exponential loss and QPC loss, excluding the linear term ℓ​(x)=x\ell(x)=x) are nonnegative,
and the marginal densities f𝐗k,pf\_{\mathbf{X}\_{k,p}} are also nonnegative.
Therefore, by [[7](https://arxiv.org/html/2602.06424v1#bib.bib71 "Optimal Damping with Hierarchical Adaptive Quadrature for Efficient Fourier Pricing of Multi-Asset Options in Lévy Models"), Proposition 3.2], the associated Fourier factors satisfy the ridge property, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℓ^k,p(ν)​(𝐮+i​𝐊k,p(ν))|\displaystyle\left\lvert\widehat{\ell}^{(\nu)}\_{k,p}\left(\mathbf{u}+\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right)\right\rvert | ≤|ℓ^k,p(ν)​(i​𝐊k,p(ν))|,∀𝐮∈ℝk,𝐊k,p(ν)∈δℓk,p(ν),\displaystyle\leq\left\lvert\widehat{\ell}^{(\nu)}\_{k,p}\left(\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right)\right\rvert,\quad\forall\mathbf{u}\in\mathbb{R}^{k},\,\mathbf{K}\_{k,p}^{(\nu)}\in\delta\_{\ell\_{k,p}}^{(\nu)}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |Φ𝐗k,p​(𝐮+i​𝐊k,p(ν))|\displaystyle\left\lvert\Phi\_{\mathbf{X}\_{k,p}}\left(\mathbf{u}+\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right)\right\rvert | ≤|Φ𝐗k,p​(i​𝐊k,p(ν))|,∀𝐮∈ℝk,𝐊k,p(ν)∈δXk,p.\displaystyle\leq\left\lvert\Phi\_{\mathbf{X}\_{k,p}}\left(\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right)\right\rvert,\qquad\forall\,\mathbf{u}\in\mathbb{R}^{k},\ \mathbf{K}\_{k,p}^{(\nu)}\in\delta\_{X\_{k,p}}. |  |

Combining these bounds with the definition of hk,p(ν)h^{(\nu)}\_{k,p} in ([3.3](https://arxiv.org/html/2602.06424v1#S3.E3 "In Notation 3.5 (Component selection and componentwise integrands). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) yields (B.1) and shows that the supremum over 𝐮\mathbf{u} is attained at 𝐮=0\mathbf{u}=0.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (B.1) |  | |hk,p(ν)​(𝐮,𝐦k,p,𝐊k,p(ν),𝚯k,p)|\displaystyle\left\lvert h\_{k,p}^{(\nu)}\left(\mathbf{u},\mathbf{m}\_{k,p},{\mathbf{K}\_{k,p}^{(\nu)}},\boldsymbol{\Theta}\_{k,p}\right)\right\rvert | ≤(2​π)−k​e⟨𝐊k,p(ν),𝐦k,p⟩​|e−i​⟨𝐮,𝐦k,p⟩|​|𝚽𝐗k,p​(i​𝐊k,p(ν))|​|ℓ^k,p(ν)​(i​𝐊k,p(ν))|\displaystyle\leq(2\pi)^{-k}e^{\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{m}\_{k,p}\rangle}\left|e^{-\mathrm{i}\langle\mathbf{u},\mathbf{m}\_{k,p}\rangle}\right|\left|\mathbf{\Phi}\_{\mathbf{X}\_{k,p}}\left(\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right)\right|\left|\widehat{\ell}^{(\nu)}\_{k,p}\left(\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right)\right| |  |
|  |  | =|hk,p(ν)​(𝟎ℝk;𝐦k,p,𝐊k,p(ν),𝚯k,p)|,∀𝐮∈ℝk,𝐊k,p(ν)∈δKk,p(ν).\displaystyle=\left|h\_{k,p}^{(\nu)}\left(\mathbf{0}\_{\mathbb{R}^{k}};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}\right)\right|,\quad\forall\mathbf{u}\in\mathbb{R}^{k},\,\mathbf{K}\_{k,p}^{(\nu)}\in\delta\_{K\_{k,p}}^{(\nu)}. |  |

Also, the quantity |hk,p(ν)​(𝟎ℝk;𝐦k,p,𝐊k,p(ν),𝚯k,p)|\left\lvert h\_{k,p}^{(\nu)}\left(\mathbf{0}\_{\mathbb{R}^{k}};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}\right)\right\rvert is strictly positive, so taking logarithms is valid and directly yields ([3.6](https://arxiv.org/html/2602.06424v1#S3.E6 "In Corollary 3.7 (Damping Rule). ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). Since log⁡(⋅)\log(\cdot) is strictly increasing on (0,∞)(0,\infty), the logarithmic transformation preserves the minimizer. This completes the proof.

#### B.1.2 On the Convexity of υk,p(ν)\upsilon\_{k,p}^{(\nu)} in in ([3.6](https://arxiv.org/html/2602.06424v1#S3.E6 "In Corollary 3.7 (Damping Rule). ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"))

We need an additional assumption below to prove Proposition [B.1](https://arxiv.org/html/2602.06424v1#A2.Thmtheorem1 "Proposition B.1. ‣ B.1.2 On the Convexity of 𝜐_{𝑘,𝑝}^(𝜈) in in (3.6) ‣ B.1 Damping rule and convexity properties ‣ Appendix B Supplementary results for Section 3.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")

1. (A7)

   For all 𝐊k,p(ν)∈δKk,p(ν)\mathbf{K}\_{k,p}^{(\nu)}\in\delta^{(\nu)}\_{K\_{k,p}}, we assume

   |  |  |  |
   | --- | --- | --- |
   |  | ∫ℝk‖𝐱‖2​e−⟨𝐊k,p(ν),𝐱⟩​f𝐗k,p​(𝐱)​𝑑𝐱<∞,∫ℝk‖𝐱‖2​e⟨𝐊k,p(ν),𝐱⟩​ℓk,p(ν)​(𝐱)​𝑑𝐱<∞.\int\_{\mathbb{R}^{k}}\|\mathbf{x}\|^{2}e^{-\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{x}\rangle}f\_{\mathbf{X}\_{k,p}}(\mathbf{x})\,d\mathbf{x}<\infty,\quad\int\_{\mathbb{R}^{k}}\|\mathbf{x}\|^{2}e^{\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{x}\rangle}\ell\_{k,p}^{(\nu)}(\mathbf{x})\,d\mathbf{x}<\infty. |  |

   Moreover, for every compact set C⊂δKk,p(ν)C\subset\delta\_{K\_{k,p}}^{(\nu)} there exist
   integrable functions φk,p𝐗,φk,pℓ:ℝk→(0,∞)\varphi^{\mathbf{X}}\_{k,p},\varphi^{\ell}\_{k,p}:\mathbb{R}^{k}\to(0,\infty) such that,
   for all 𝐊k,p(ν)∈C\mathbf{K}\_{k,p}^{(\nu)}\in C and all 𝐱∈ℝk\mathbf{x}\in\mathbb{R}^{k},

   |  |  |  |
   | --- | --- | --- |
   |  | ‖𝐱‖2​e−⟨𝐊k,p(ν),𝐱⟩​f𝐗k,p​(𝐱)≤φk,p𝐗​(𝐱),‖𝐱‖2​e⟨𝐊k,p(ν),𝐱⟩​ℓk,p(ν)​(𝐱)≤φk,pℓ​(𝐱).\|\mathbf{x}\|^{2}e^{-\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{x}\rangle}\,f\_{\mathbf{X}\_{k,p}}(\mathbf{x})\leq\varphi^{\mathbf{X}}\_{k,p}(\mathbf{x}),\qquad\|\mathbf{x}\|^{2}e^{\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{x}\rangle}\,\ell\_{k,p}^{(\nu)}(\mathbf{x})\leq\varphi^{\ell}\_{k,p}(\mathbf{x}). |  |

###### Proposition B.1.

Suppose Assumptions [3.2](https://arxiv.org/html/2602.06424v1#S3.Ex2 "Assumption 3.2 (Admissible contour shifts). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") and ([A7](https://arxiv.org/html/2602.06424v1#A2.I1.i7 "item A7 ‣ B.1.2 On the Convexity of 𝜐_{𝑘,𝑝}^(𝜈) in in (3.6) ‣ B.1 Damping rule and convexity properties ‣ Appendix B Supplementary results for Section 3.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) hold. Define the normalized weights (Esscher transforms) as:

|  |  |  |
| --- | --- | --- |
|  | w𝚽k,p​(𝐱;𝐊k,p(ν)):=e−⟨𝐊k,p(ν),𝐱⟩​f𝐗k,p​(𝐱)∫ℝke−⟨𝐊k,p(ν),𝐱⟩​f𝐗k,p​(𝐱)​d𝐱,wℓk,p(ν)​(𝐱;𝐊k,p(ν)):=e⟨𝐊k,p(ν),𝐱⟩​ℓk,p(ν)​(𝐱)∫ℝke⟨𝐊k,p(ν),𝐱⟩​ℓk,p(ν)​(𝐱)​d𝐱.w\_{\boldsymbol{\Phi}\_{k,p}}\left(\mathbf{x};\mathbf{K}\_{k,p}^{(\nu)}\right)\;:=\;\frac{e^{-\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{x}\rangle}f\_{\mathbf{X}\_{k,p}}(\mathbf{x})}{\int\_{\mathbb{R}^{k}}e^{-\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{x}\rangle}f\_{\mathbf{X}\_{k,p}}(\mathbf{x})\mathrm{d}\mathbf{x}},\qquad w\_{\ell\_{k,p}^{(\nu)}}\left(\mathbf{x};\mathbf{K}\_{k,p}^{(\nu)}\right)\;:=\;\frac{e^{\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{x}\rangle}\ell\_{k,p}^{(\nu)}(\mathbf{x})}{\int\_{\mathbb{R}^{k}}e^{\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{x}\rangle}\ell\_{k,p}^{(\nu)}(\mathbf{x})\mathrm{d}\mathbf{x}}. |  |

Then the Hessian of υk,p(ν)​(𝐦k,p,𝐊k,p(ν),𝚯k,p)\upsilon\_{k,p}^{(\nu)}\!\left(\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}\right) (defined in ([3.6](https://arxiv.org/html/2602.06424v1#S3.E6 "In Corollary 3.7 (Damping Rule). ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"))) is expressed as: 151515𝔼w​[𝐗],Covw⁡[𝐗]\mathbb{E}\_{w}\left[\mathbf{X}\right],\operatorname{Cov}\_{w}\left[\mathbf{X}\right] denotes the expectation and covariance matrix of 𝐗\mathbf{X}, respectively, under the given probability density ww.

|  |  |  |  |
| --- | --- | --- | --- |
| (B.2) |  | ∇𝐊k,p(ν)2υk,p(ν)​(𝐦k,p,𝐊k,p(ν),𝚯k,p)=Covw𝚽k,p⁡[𝐗k,p]+Covwℓk,p(ν)⁡[𝐗k,p]⪰ 0.\nabla^{2}\_{\mathbf{K}\_{k,p}^{(\nu)}}\upsilon\_{k,p}^{(\nu)}\!\left(\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}\right)\;=\;\operatorname{Cov}\_{w\_{\boldsymbol{\Phi}\_{k,p}}}\left[\mathbf{X}\_{k,p}\right]\;+\;\operatorname{Cov}\_{w\_{\ell\_{k,p}^{(\nu)}}}\left[\mathbf{X}\_{k,p}\right]\;\succeq\;0. |  |

Moreover, υk,p(ν)​(𝐦k,p,𝐊k,p(ν),𝚯k,p)\upsilon\_{k,p}^{(\nu)}(\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}) is strictly convex on δKk,p(ν)\delta\_{K\_{k,p}}^{(\nu)} if, for every
𝐊k,p(ν)∈δKk,p(ν)\mathbf{K}\_{k,p}^{(\nu)}\in\delta\_{K\_{k,p}}^{(\nu)}, at least one of the two covariance matrices
Covw𝚽k,p⁡[𝐗k,p]\operatorname{Cov}\_{w\_{\boldsymbol{\Phi}\_{k,p}}}[\mathbf{X}\_{k,p}] or
Covwℓk,p(ν)⁡[𝐗k,p]\operatorname{Cov}\_{w\_{\ell\_{k,p}^{(\nu)}}}[\mathbf{X}\_{k,p}]
≻0{\succ 0}. If, in addition, there exists a compact set
C⊂δKk,p(ν)C\subset\delta\_{K\_{k,p}}^{(\nu)} and a constant μk,p>0\mu\_{k,p}>0 such that 161616λmin​(𝐀)\lambda\_{\min}(\boldsymbol{A}) denotes the smallest eigenvalue of a square matrix 𝐀\boldsymbol{A}.

|  |  |  |
| --- | --- | --- |
|  | λmin​(∇𝐊k,p(ν)2υk,p(ν)​(𝐦k,p,𝐊k,p(ν),𝚯k,p))≥μk,p,∀𝐊k,p(ν)∈C,\lambda\_{\min}\!\Big(\nabla^{2}\_{\mathbf{K}\_{k,p}^{(\nu)}}\,\upsilon\_{k,p}^{(\nu)}(\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p})\Big)\;\geq\;\mu\_{k,p},\qquad\forall\,\mathbf{K}\_{k,p}^{(\nu)}\in C, |  |

then υk,p(ν)​(𝐦k,p,𝐊k,p(ν),𝚯k,p)\upsilon\_{k,p}^{(\nu)}(\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p})
is μk,p\mu\_{k,p}-strongly convex on CC

###### Proof.

From Assumption
[3.2](https://arxiv.org/html/2602.06424v1#S3.Ex2 "Assumption 3.2 (Admissible contour shifts). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), the integrals

|  |  |  |
| --- | --- | --- |
|  | ∫ℝke−⟨𝐊k,p,𝐱⟩​f𝐗k,p​(𝐱)​𝑑𝐱,∫ℝke⟨𝐊k,p,𝐱⟩​ℓk,p(ν)​(𝐱)​𝑑𝐱\int\_{\mathbb{R}^{k}}e^{-\langle\mathbf{K}\_{k,p},\mathbf{x}\rangle}f\_{\mathbf{X}\_{k,p}}(\mathbf{x})\,d\mathbf{x},\qquad\int\_{\mathbb{R}^{k}}e^{\langle\mathbf{K}\_{k,p},\mathbf{x}\rangle}\ell\_{k,p}^{(\nu)}(\mathbf{x})\,d\mathbf{x} |  |

are finite for all 𝐊k,p(ν)∈δKk,p(ν)\mathbf{K}\_{k,p}^{(\nu)}\in\delta\_{K\_{k,p}}^{(\nu)}, combining with Assumption ([A7](https://arxiv.org/html/2602.06424v1#A2.I1.i7 "item A7 ‣ B.1.2 On the Convexity of 𝜐_{𝑘,𝑝}^(𝜈) in in (3.6) ‣ B.1 Damping rule and convexity properties ‣ Appendix B Supplementary results for Section 3.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), the normalized Esscher weights w𝚽k,p​(𝐱;𝐊k,p(ν))w\_{\boldsymbol{\Phi}\_{k,p}}\left(\mathbf{x};\mathbf{K}\_{k,p}^{(\nu)}\right) and
wℓk,p(ν)​(𝐱;𝐊k,p(ν))w\_{\ell\_{k,p}^{(\nu)}}\left(\mathbf{x};\mathbf{K}\_{k,p}^{(\nu)}\right) are well-defined probability densities on ℝk\mathbb{R}^{k}. Also, Assumption ([A7](https://arxiv.org/html/2602.06424v1#A2.I1.i7 "item A7 ‣ B.1.2 On the Convexity of 𝜐_{𝑘,𝑝}^(𝜈) in in (3.6) ‣ B.1 Damping rule and convexity properties ‣ Appendix B Supplementary results for Section 3.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) provides the uniform integrability needed to apply the dominated convergence theorem. Hence, the differentiation w.r.t. 𝐊k,p(ν)\mathbf{K}\_{k,p}^{(\nu)} can be passed through the integrals, and the first- and second-order derivatives are given by

|  |  |  |
| --- | --- | --- |
|  | ∇𝐊k,p(ν)𝚽𝐗k,p​(i​𝐊k,p(ν)):=−∫ℝk𝐱​e−⟨𝐊k,p(ν),𝐱⟩​f𝐗k,p​(𝐱)​d𝐱,∇𝐊k,p(ν)ℓ^k,p(ν)​(i​𝐊k,p(ν)):=∫ℝk𝐱​e⟨𝐊k,p(ν),𝐱⟩​ℓk,p(ν)​(𝐱)​d𝐱\nabla\_{\mathbf{K}\_{k,p}^{(\nu)}}\mathbf{\Phi}\_{\mathbf{X}\_{k,p}}\left(\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right):=-\int\_{\mathbb{R}^{k}}\mathbf{x}e^{-\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{x}\rangle}f\_{\mathbf{X}\_{k,p}}(\mathbf{x})\mathrm{d}\mathbf{x},\quad\nabla\_{\mathbf{K}\_{k,p}^{(\nu)}}\widehat{\ell}^{(\nu)}\_{k,p}\left(\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right):=\int\_{\mathbb{R}^{k}}\mathbf{x}e^{\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{x}\rangle}\ell\_{k,p}^{(\nu)}(\mathbf{x})\mathrm{d}\mathbf{x} |  |

|  |  |  |
| --- | --- | --- |
|  | ∇𝐊k,p(ν)2𝚽𝐗k,p​(i​𝐊k,p(ν)):=∫ℝk𝐱𝐱T​e−⟨𝐊k,p(ν),𝐱⟩​f𝐗k,p​(𝐱)​d𝐱,∇𝐊k,p(ν)2ℓ^k,p(ν)​(i​𝐊k,p(ν)):=∫ℝk𝐱𝐱T​e⟨𝐊k,p(ν),𝐱⟩​ℓk,p(ν)​(𝐱)​d𝐱\nabla^{2}\_{\mathbf{K}\_{k,p}^{(\nu)}}\mathbf{\Phi}\_{\mathbf{X}\_{k,p}}\left(\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right):=\int\_{\mathbb{R}^{k}}\mathbf{x}\mathbf{x}^{T}e^{-\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{x}\rangle}f\_{\mathbf{X}\_{k,p}}(\mathbf{x})\mathrm{d}\mathbf{x},\quad\nabla^{2}\_{\mathbf{K}\_{k,p}^{(\nu)}}\widehat{\ell}^{(\nu)}\_{k,p}\left(\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right):=\int\_{\mathbb{R}^{k}}\mathbf{x}\mathbf{x}^{T}e^{\langle\mathbf{K}\_{k,p}^{(\nu)},\mathbf{x}\rangle}\ell\_{k,p}^{(\nu)}(\mathbf{x})\mathrm{d}\mathbf{x} |  |

By the nonnegativity of the loss components ℓk,p(ν)\ell\_{k,p}^{(\nu)} established in Appendix [E.2](https://arxiv.org/html/2602.06424v1#A5.SS2 "E.2 Fourier transform of the given loss functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), together with the nonnegativity of the marginal densities f𝐗k,pf\_{\mathbf{X}\_{k,p}}, we obtain

|  |  |  |
| --- | --- | --- |
|  | ln⁡|Φ𝐗k,p​(i​𝐊k,p(ν))|=ln⁡Φ𝐗k,p​(i​𝐊k,p(ν)),ln⁡|ln⁡ℓ^k,p(ν)​(i​𝐊k,p(ν))|=ln⁡ℓ^k,p(ν)​(i​𝐊k,p(ν))\ln\left\lvert\Phi\_{\mathbf{X}\_{k,p}}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right)\right\rvert=\ln\Phi\_{\mathbf{X}\_{k,p}}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right),\quad\ln\left\lvert\ln\widehat{\ell}^{(\nu)}\_{k,p}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right)\right\rvert=\ln\widehat{\ell}^{(\nu)}\_{k,p}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right) |  |

Now using the chain rule, we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (B.3) |  | ∇𝐊k,p(ν)2ln⁡Φ𝐗k,p​(i​𝐊k,p(ν))\displaystyle\nabla^{2}\_{\mathbf{K}\_{k,p}^{(\nu)}}\ln\Phi\_{\mathbf{X}\_{k,p}}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right) | =∇𝐊k,p(ν)2Φ𝐗k,p​(i​𝐊k,p(ν))Φ𝐗k,p​(i​𝐊k,p(ν))−∇𝐊k,p(ν)Φ𝐗k,p​(i​𝐊k,p(ν))​∇𝐊k,p(ν)Φ𝐗k,p​(i​𝐊k,p(ν))⊤Φ𝐗k,p2​(i​𝐊k,p(ν)),\displaystyle=\frac{\nabla^{2}\_{\mathbf{K}\_{k,p}^{(\nu)}}\Phi\_{\mathbf{X}\_{k,p}}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right)}{\Phi\_{\mathbf{X}\_{k,p}}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right)}-\frac{\nabla\_{\mathbf{K}\_{k,p}^{(\nu)}}\Phi\_{\mathbf{X}\_{k,p}}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right)\,\nabla\_{\mathbf{K}\_{k,p}^{(\nu)}}\Phi\_{\mathbf{X}\_{k,p}}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right)^{\top}}{\Phi\_{\mathbf{X}\_{k,p}}^{2}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right)}, |  |
|  | ∇𝐊k,p(ν)2ln⁡ℓ^k,p(ν)​(i​𝐊k,p(ν))\displaystyle\nabla^{2}\_{\mathbf{K}\_{k,p}^{(\nu)}}\ln\widehat{\ell}^{(\nu)}\_{k,p}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right) | =∇𝐊k,p(ν)2ℓ^k,p(ν)​(i​𝐊k,p(ν))ℓ^k,p(ν)​(i​𝐊k,p(ν))−∇𝐊k,p(ν)ℓ^k,p(ν)​(i​𝐊k,p(ν))​∇𝐊k,p(ν)ℓ^k,p(ν)​(i​𝐊k,p(ν))⊤(ℓ^k,p(ν))2​(i​𝐊k,p(ν)).\displaystyle=\frac{\nabla^{2}\_{\mathbf{K}\_{k,p}^{(\nu)}}\widehat{\ell}^{(\nu)}\_{k,p}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right)}{\widehat{\ell}^{(\nu)}\_{k,p}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right)}-\frac{\nabla\_{\mathbf{K}\_{k,p}^{(\nu)}}\widehat{\ell}^{(\nu)}\_{k,p}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right)\,\nabla\_{\mathbf{K}\_{k,p}^{(\nu)}}\widehat{\ell}^{(\nu)}\_{k,p}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right)^{\top}}{\left(\widehat{\ell}^{(\nu)}\_{k,p}\right)^{2}\left(\mathrm{i}\,\mathbf{K}\_{k,p}^{(\nu)}\right)}. |  |

We can rewrite ([B.3](https://arxiv.org/html/2602.06424v1#A2.E3 "In Proof. ‣ B.1.2 On the Convexity of 𝜐_{𝑘,𝑝}^(𝜈) in in (3.6) ‣ B.1 Damping rule and convexity properties ‣ Appendix B Supplementary results for Section 3.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) in terms of the Esscher transform as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (B.4) |  | ∇𝐊k,p(ν)2ln⁡Φ𝐗k,p​(i​𝐊k,p(ν))\displaystyle\nabla^{2}\_{\mathbf{K}\_{k,p}^{(\nu)}}\ln\Phi\_{\mathbf{X}\_{k,p}}\left(\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right) | =𝔼w𝚽k,p​[𝐗k,p​𝐗k,p⊤]−𝔼w𝚽k,p​[𝐗k,p]​𝔼w𝚽k,p​[𝐗k,p]⊤=Covw𝚽k,p⁡[𝐗k,p]\displaystyle=\mathbb{E}\_{w\_{\boldsymbol{\Phi}\_{k,p}}}\left[\mathbf{X}\_{k,p}\mathbf{X}\_{k,p}^{\top}\right]-\mathbb{E}\_{w\_{\boldsymbol{\Phi}\_{k,p}}}\left[\mathbf{X}\_{k,p}\right]\mathbb{E}\_{w\_{\boldsymbol{\Phi}\_{k,p}}}\left[\mathbf{X}\_{k,p}\right]^{\top}=\operatorname{Cov}\_{w\_{\boldsymbol{\Phi}\_{k,p}}}\left[\mathbf{X}\_{k,p}\right] |  |
|  | ∇𝐊k,p(ν)2ln⁡ℓ^k,p(ν)​(i​𝐊k,p(ν))\displaystyle\nabla^{2}\_{\mathbf{K}\_{k,p}^{(\nu)}}\ln\widehat{\ell}^{(\nu)}\_{k,p}\left(\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right) | =𝔼w𝚽k,p​[𝐗k,p​𝐗k,p⊤]−𝔼wℓk,p(ν)​[𝐗k,p]​𝔼wℓk,p(ν)​[𝐗k,p]⊤=Covwℓk,p(ν)⁡[𝐗k,p]\displaystyle=\mathbb{E}\_{w\_{\boldsymbol{\Phi}\_{k,p}}}\left[\mathbf{X}\_{k,p}\mathbf{X}\_{k,p}^{\top}\right]-\mathbb{E}\_{w\_{\ell\_{k,p}^{(\nu)}}}\left[\mathbf{X}\_{k,p}\right]\mathbb{E}\_{w\_{\ell\_{k,p}^{(\nu)}}}\left[\mathbf{X}\_{k,p}\right]^{\top}=\operatorname{Cov}\_{w\_{\ell\_{k,p}^{(\nu)}}}\left[\mathbf{X}\_{k,p}\right] |  |

Since Covw⁡[𝐗]⪰0\operatorname{Cov}\_{w}[\mathbf{X}]\succeq 0 for any probability density ww, ([B.2](https://arxiv.org/html/2602.06424v1#A2.E2 "In Proposition B.1. ‣ B.1.2 On the Convexity of 𝜐_{𝑘,𝑝}^(𝜈) in in (3.6) ‣ B.1 Damping rule and convexity properties ‣ Appendix B Supplementary results for Section 3.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) follows immediately. Strict convexity holds whenever, for every 𝐊k,p(ν)\mathbf{K}\_{k,p}^{(\nu)}, at least one of the two covariance terms is ≻0\succ 0. The strong convexity statement is exactly the uniform curvature bound for ∇𝐊k,p(ν)2υk,p(ν)​(𝐦k,p,𝐊k,p(ν),𝚯k,p)\nabla^{2}\_{\mathbf{K}\_{k,p}^{(\nu)}}\,\upsilon\_{k,p}^{(\nu)}(\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}) on CC.
∎

###### Remark B.2.

In our numerical setting, 𝐗k,p\mathbf{X}\_{k,p} is either a non-degenerate Gaussian (Σk,p≻0)(\Sigma\_{k,p}\succ 0) or a non-degenerate NIG with full-dimensional dispersion/shape (Γk,p≻0)(\Gamma\_{k,p}\succ 0). Under such non-degeneracy, the corresponding Esscher-tilted measures remain non-degenerate, hence CovwΦ​[Xk,p]≻0\mathrm{Cov}\_{w\_{\Phi}}[X\_{k,p}]\succ 0; see also [[47](https://arxiv.org/html/2602.06424v1#bib.bib15 "The Generalized Hyperbolic Model: Estimation, Financial Derivatives, and Risk Measures"), [21](https://arxiv.org/html/2602.06424v1#bib.bib14 "Option Pricing by Esscher Transforms")]. Hence vk,p(ν)v^{(\nu)}\_{k,p} is strictly convex on δKk,p(ν)\delta^{(\nu)}\_{K\_{k,p}}.

### B.2 Regularized damping

This appendix complements the discussion in Section [3.1](https://arxiv.org/html/2602.06424v1#S3.SS1 "3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") by providing a principled regularization of the peak-minimizing damping rule. In order to handle the closed-to-boundary behavior of the minimizer, we need to account also for the width of the integrand around its peak 𝐮=𝟎ℝk\mathbf{u}=\mathbf{0}\_{\mathbb{R}^{k}}, which controls for how fast the integrand decays away from 𝟎ℝk\mathbf{0}\_{\mathbb{R}^{k}}. Based on analysis about the asymptotic behavior of the integral around its peak from [[11](https://arxiv.org/html/2602.06424v1#bib.bib103 "Asymptotic Methods in Analysis"), Chapter 4], a Taylor expansion of υk,p(ν)​(𝐮;𝐦k,p,𝐊k,p(ν),𝚯k,p)\upsilon\_{k,p}^{(\nu)}\left(\mathbf{u};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\boldsymbol{\Theta}\_{k,p}}\right) around 𝐮=𝟎ℝk\mathbf{u}=\mathbf{0}\_{\mathbb{R}^{k}} gives 171717From ([3.6](https://arxiv.org/html/2602.06424v1#S3.E6 "In Corollary 3.7 (Damping Rule). ‣ 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), we recall υk,p(ν)​(𝟎ℝk;𝐦k,p,𝐊k,p(ν),𝚯k,p)≡υk,p(ν)​(𝐦k,p,𝐊k,p(ν),𝚯k,p)\upsilon\_{k,p}^{(\nu)}\left(\mathbf{0}\_{\mathbb{R}^{k}};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\boldsymbol{\Theta}\_{k,p}}\right)\equiv\upsilon\_{k,p}^{(\nu)}\left(\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\boldsymbol{\Theta}\_{k,p}}\right)

|  |  |  |  |
| --- | --- | --- | --- |
| (B.5) |  | υk,p(ν)​(𝐮;𝐦k,p,𝐊k,p(ν),𝚯k,p)=υk,p(ν)​(𝐦k,p,𝐊k,p(ν),𝚯k,p)−12​𝐮⊤​κ​(𝐊k,p(ν))​𝐮+𝒪​(‖𝐮‖3)\upsilon\_{k,p}^{(\nu)}\left(\mathbf{u};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\boldsymbol{\Theta}\_{k,p}}\right)=\upsilon\_{k,p}^{(\nu)}\left(\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\boldsymbol{\Theta}\_{k,p}}\right)-\frac{1}{2}\mathbf{u}^{\top}\kappa\left(\mathbf{K}\_{k,p}^{(\nu)}\right)\mathbf{u}+\mathcal{O}\left(\|\mathbf{u}\|^{3}\right) |  |

with κ​(𝐊k,p(ν))=∇𝐮2υk,p(ν)​(𝐮;𝐦k,p,𝐊k,p(ν),𝚯k,p)|𝐮=𝟎ℝk⪰0\kappa\left(\mathbf{K}\_{k,p}^{(\nu)}\right)=\nabla\_{\mathbf{u}}^{2}\upsilon\_{k,p}^{(\nu)}\left(\mathbf{u};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\boldsymbol{\Theta}\_{k,p}}\right)|\_{\mathbf{u}=\mathbf{0}\_{\mathbb{R}^{k}}}\succeq 0.

Near 𝐮=𝟎ℝk\mathbf{u}=\mathbf{0}\_{\mathbb{R}^{k}}, the component integrand of interest along any direction 𝐮\mathbf{u} can be approximated as

|  |  |  |
| --- | --- | --- |
|  | |hk,p(ν)​(𝐮;𝐦k,p,𝐊k,p(ν),𝚯k,p)|≈exp⁡{υk,p(ν)​(𝐦k,p,𝐊k,p(ν),𝚯k,p)}​exp⁡(12​𝐮⊤​κ​(𝐊k,p(ν))​𝐮)\bigl|h\_{k,p}^{(\nu)}\left(\mathbf{u};\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\boldsymbol{\Theta}\_{k,p}}\right)\bigr|\;\approx\;\exp\!\left\{\upsilon\_{k,p}^{(\nu)}\left(\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},{\color[rgb]{0,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@gray@stroke{0}\pgfsys@color@gray@fill{0}\boldsymbol{\Theta}\_{k,p}}\right)\right\}\exp\!\left(\frac{1}{2}\mathbf{u}^{\top}\kappa\left(\mathbf{K}\_{k,p}^{(\nu)}\right)\mathbf{u}\right) |  |

where κ​(𝐊k,p(ν))\kappa\left(\mathbf{K}\_{k,p}^{(\nu)}\right) denotes the local curvature (Hessian-type) matrix.

Controlling the peak width required bounding the curvature relative to a
reference geometry 𝑾k,p≻0\boldsymbol{W}\_{k,p}\succ 0. A minimum admissible width is enforced by the upper bound,

|  |  |  |
| --- | --- | --- |
|  | κ​(𝐊k,p(ν))⪯rmax​𝑾k,p⟺𝐮⊤​κ​(𝐊k,p(ν))​𝐮≤rmax​𝐮⊤​𝑾k,p​𝐮,\kappa\left(\mathbf{K}\_{k,p}^{(\nu)}\right)\preceq r\_{\max}\boldsymbol{W}\_{k,p}\quad\Longleftrightarrow\quad\mathbf{u}^{\top}\kappa\left(\mathbf{K}\_{k,p}^{(\nu)}\right)\mathbf{u}\leq r\_{\max}\,\mathbf{u}^{\top}\boldsymbol{W}\_{k,p}\mathbf{u}, |  |

while a maximum admissible width follows from the lower bound

|  |  |  |
| --- | --- | --- |
|  | κ​(𝐊k,p(ν))⪰rmin​𝑾k,p⟺𝐮⊤​κ​(𝐊k,p(ν))​𝐮≥rmin​𝐮⊤​𝑾k,p​𝐮.\kappa\left(\mathbf{K}\_{k,p}^{(\nu)}\right)\succeq r\_{\min}\boldsymbol{W}\_{k,p}\quad\Longleftrightarrow\quad\mathbf{u}^{\top}\kappa\left(\mathbf{K}\_{k,p}^{(\nu)}\right)\mathbf{u}\geq r\_{\min}\,\mathbf{u}^{\top}\boldsymbol{W}\_{k,p}\mathbf{u}. |  |

These curvature bounds can lead to a trust-region formulation for the damping selection:

|  |  |  |
| --- | --- | --- |
|  | min𝐊k,p(ν)⁡υ​(𝐦k,p,𝐊k,p(ν))s.t.‖𝐊k,p(ν)‖𝑾k,p≤R,𝐊k,p(ν)∈δKk,p(ν),\min\_{\mathbf{K}\_{k,p}^{(\nu)}}\;\upsilon\left(\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)}\right)\quad\text{s.t.}\quad\|\mathbf{K}\_{k,p}^{(\nu)}\|\_{\boldsymbol{W}\_{k,p}}\leq R,\;\;\mathbf{K}\_{k,p}^{(\nu)}\in\delta\_{K\_{k,p}}^{(\nu)}, |  |

where
R:=|rmax−rmin|,‖𝐊k,p(ν)‖𝑾k,p2:=(𝐊k,p(ν))⊤​𝑾k,p​𝐊k,p(ν),𝑾k,p≻0R:=\lvert r\_{\max}-r\_{\min}\rvert,\qquad\|\mathbf{K}\_{k,p}^{(\nu)}\|\_{\boldsymbol{W}\_{k,p}}^{2}:=\left(\mathbf{K}\_{k,p}^{(\nu)}\right)^{\top}\boldsymbol{W}\_{k,p}\mathbf{K}\_{k,p}^{(\nu)},\qquad\boldsymbol{W}\_{k,p}\succ 0.

The above derivation leads to the Tikhonov-regularized problem ([3.7](https://arxiv.org/html/2602.06424v1#S3.E7 "In 3.1 Optimal Damping Rule ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

###### Remark B.3.

The natural choice for the weighting matrix 𝑾k,p\boldsymbol{W}\_{k,p} is given by the
dispersion (or shape) matrix associated with the distribution of the
marginal loss vector 𝐗k,p\mathbf{X}\_{k,p}. Concretely, for the models considered,
𝑾k,p\boldsymbol{W}\_{k,p} is chosen as follows:

|  |  |
| --- | --- |
| Model | Choice of Wk,p\boldsymbol{W}\_{k,p} |
| Gaussian | 𝚺k,p\boldsymbol{\Sigma}\_{k,p} |
| NIG | 𝚪k,p\boldsymbol{\Gamma}\_{k,p} |

Table B.1: Choice of the weighting matrix 𝑾k,p\boldsymbol{W}\_{k,p}.

## Appendix C Supplementary results for Section [4.1.1](https://arxiv.org/html/2602.06424v1#S4.SS1.SSS1 "4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")

### C.1 Boundary Oscillation Analysis

This appendix analyzes boundary-induced oscillations of the transformed integrands in Section [4.1.1](https://arxiv.org/html/2602.06424v1#S4.SS1.SSS1 "4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). For notational convenience, we write ak,p(ν)​(G−1​(𝐯;𝚯k,p);𝐦k,p,𝐊k,p(ν),𝚯k,p)≡ak,p(ν)​(G−1​(𝐯;𝚯k,p))\;a\_{k,p}^{(\nu)}\left(G^{-1}\left(\mathbf{v};\boldsymbol{\Theta}\_{k,p}\right);\mathbf{m}\_{k,p},\mathbf{K}\_{k,p}^{(\nu)},\boldsymbol{\Theta}\_{k,p}\right)\equiv a\_{k,p}^{(\nu)}\left(G^{-1}\left(\mathbf{v};\boldsymbol{\Theta}\_{k,p}\right)\right). Fix a boundary face 𝐁⊂∂[0,1]k\mathbf{B}\subset\partial[0,1]^{k}, and consider a Lipschitz path Υ:[t0,t1]→[0,1]k\Upsilon:[t\_{0},t\_{1}]\to[0,1]^{k}, 𝐯:=Υ​(t)\mathbf{v}:=\Upsilon(t)
approaching 𝐁\mathbf{B} (e.g., by fixing all but one coordinate and letting
vj→0v\_{j}\to 0). Throughout this appendix, we assume that the inverse transformation G−1​(⋅;𝚯k,p)G^{-1}(\cdot;\boldsymbol{\Theta}\_{k,p}) is almost everywhere differentiable on (0,1)k(0,1)^{k} and locally absolutely continuous along Lipschitz paths Υ\Upsilon. The Jacobian JG−1​(𝐯;𝚯k,p)J\_{G^{-1}}(\mathbf{v};\boldsymbol{\Theta}\_{k,p}) denotes the derivative of G−1G^{-1} w.r.t. 𝐯\mathbf{v}.

The phase advance, or equivalently the total variation of
ϖ\varpi, along the path Υ\Upsilon is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | TV[t0,t1]​(ϖ∘Υ)\displaystyle\mathrm{TV}\_{[t\_{0},t\_{1}]}(\varpi\circ\Upsilon) | :=∫t0t1|∂tϖ​(Υ​(t),𝚯k,p)⋅Υ′​(t)|​𝑑t\displaystyle=\int\_{t\_{0}}^{t\_{1}}\left|\partial\_{t}\;\varpi\left(\Upsilon(t),\boldsymbol{\Theta}\_{k,p}\right)\cdot\Upsilon^{\prime}(t)\right|\,dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫t0t1|(JG−1​(Υ​(t),𝚯k,p)⊤​𝐦k,p)⋅Υ′​(t)|​𝑑t.\displaystyle=\int\_{t\_{0}}^{t\_{1}}\left|\big(J\_{G^{-1}}\left(\Upsilon(t),\boldsymbol{\Theta}\_{k,p}\right)^{\top}\mathbf{m}\_{k,p}\big)\cdot\Upsilon^{\prime}(t)\right|\,dt. |  |

The *number of oscillations accumulated along Υ\Upsilon* is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Nosc​(Υ;[t0,t1])\displaystyle N\_{\text{osc}}(\Upsilon;[t\_{0},t\_{1}]) | :=12​π​TV[t0,t1]​(ϖ∘Υ).\displaystyle=\frac{1}{2\pi}\,\mathrm{TV}\_{[t\_{0},t\_{1}]}(\varpi\circ\Upsilon). |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫t0t1|(JG−1(Υ(t),𝚯k,p)⊤𝐦k,p)⋅Υ′(t)|dt.2​π\displaystyle=\frac{\int\_{t\_{0}}^{t\_{1}}\left|\big(J\_{G^{-1}}\left(\Upsilon(t),\boldsymbol{\Theta}\_{k,p}\right)^{\top}\mathbf{m}\_{k,p}\big)\cdot\Upsilon^{\prime}(t)\right|\,dt.}{2\pi} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥|𝐦k,p⊤[G−1(Υ(t1),𝚯k,p)−G−1(Υ(t0,𝚯k,p)]|2​π\displaystyle\geq\frac{\left|\mathbf{m}\_{k,p}^{\top}\left[G^{-1}\left(\Upsilon(t\_{1}),\boldsymbol{\Theta}\_{k,p}\right)-G^{-1}\left(\Upsilon(t\_{0},\boldsymbol{\Theta}\_{k,p}\right)\right]\right|}{2\pi} |  |

Suppose that the amplitude of the integrand falls below the prescribed tolerance ξ\xi for t≥t∗t\geq t^{\*}, where

|  |  |  |  |
| --- | --- | --- | --- |
| (C.1) |  | t∗:=inf{t∈[t0,t1]:|a​(G−1​(Υ​(t),𝚯k,p))|​|detJG−1​(Υ​(t),𝚯k,p)|≤ξ}.t^{\*}:=\inf\left\{t\in[t\_{0},t\_{1}]:\left\lvert a\left(G^{-1}\left(\Upsilon({t}),\boldsymbol{\Theta}\_{k,p}\right)\right)\right\rvert\,\left\lvert\det J\_{G^{-1}}\left(\Upsilon(t),\boldsymbol{\Theta}\_{k,p}\right)\right\rvert\leq\xi\right\}. |  |

Let 𝐯∗:=Υ​(t∗)\mathbf{v}^{\*}:=\Upsilon(t^{\*}) and define

|  |  |  |  |
| --- | --- | --- | --- |
|  | r𝐁\displaystyle r\_{\mathbf{B}} | :=limt→t𝐁G−1​(Υ​(t),𝚯k,p)‖G−1​(Υ​(t),𝚯k,p)‖=lim𝐯→𝐁G−1​(𝐯,𝚯k,p)‖G−1​(𝐯,𝚯k,p)‖,\displaystyle:=\lim\_{t\to t\_{\mathbf{B}}}\frac{G^{-1}\left(\Upsilon(t),\boldsymbol{\Theta}\_{k,p}\right)}{\left\lVert G^{-1}\left(\Upsilon(t),\boldsymbol{\Theta}\_{k,p}\right)\right\rVert}\;=\;\lim\_{\mathbf{v}\to\mathbf{B}}\frac{G^{-1}\left(\mathbf{v},\boldsymbol{\Theta}\_{k,p}\right)}{\left\lVert G^{-1}\left(\mathbf{v},\boldsymbol{\Theta}\_{k,p}\right)\right\rVert}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | U∗\displaystyle U\_{\*} | :=‖G−1​(Υ​(t∗),𝚯k,p)‖=‖G−1​(𝐯∗,𝚯k,p)‖.\displaystyle:=\left\lVert G^{-1}\left(\Upsilon(t^{\*}),\boldsymbol{\Theta}\_{k,p}\right)\right\rVert\;=\;\left\lVert G^{-1}\left(\mathbf{v}^{\*},\boldsymbol{\Theta}\_{k,p}\right)\right\rVert. |  |

Here, r𝐁r\_{\mathbf{B}} is the *normalized direction* of G−1​(𝐯,𝚯k,p)G^{-1}(\mathbf{v},\boldsymbol{\Theta}\_{k,p}) as 𝐯\mathbf{v} approaches the boundary face 𝐁\mathbf{B}, and U∗U\_{\*} is the *truncation radius* at the threshold point 𝐯∗=Υ​(t∗)\mathbf{v}^{\*}=\Upsilon(t^{\*}).

Moreover, if the phase ϖ\varpi is monotone in a neighborhood of 𝐁\mathbf{B} along the path Υ​(t)\Upsilon(t) and G−1​(Υ​(t))G^{-1}(\Upsilon(t)) is asymptotically radial, then the number of oscillations near the boundary can be approximated by: 181818By
symmetry, the same argument applies when 𝐯→𝟏ℝk\mathbf{v}\to\mathbf{1}\_{\mathbb{R}^{k}}; for definiteness, we
consider here the limiting behavior as 𝐯→𝟎ℝk\mathbf{v}\to\mathbf{0}\_{\mathbb{R}^{k}}.

|  |  |  |  |
| --- | --- | --- | --- |
| (C.2) |  | Nosc​(𝐁)≈12​π​|𝐦k,p⊤​G−1​(𝐯∗,𝚯)|=12​π​|𝐦k,p⊤​r𝐁|​U∗,N\_{\text{osc}}(\mathbf{B})\;\approx\;\frac{1}{2\pi}\,\bigl|\mathbf{m}\_{k,p}^{\top}G^{-1}(\mathbf{v}^{\*},\boldsymbol{\Theta})\bigr|\;=\;\frac{1}{2\pi}\,\bigl|\mathbf{m}\_{k,p}^{\top}r\_{\mathbf{B}}\bigr|\,U\_{\*}, |  |

For related analysis of multivariate oscillatory integrals, emphasizing the role of stationary points (∂tϖ​(Υ​(t),𝚯k,p)⋅Υ′​(t)=0)\left(\partial\_{t}\;\varpi(\Upsilon(t),\boldsymbol{\Theta}\_{k,p})\cdot\Upsilon^{\prime}(t)=0\right), we refer to [[30](https://arxiv.org/html/2602.06424v1#bib.bib96 "The Construction of cubature rules for multivariate highly oscillatory integrals"), [31](https://arxiv.org/html/2602.06424v1#bib.bib60 "On the computation of highly oscillatory multivariate integrals with stationary points")]. Our notion of quantifying the number of oscillations via phase advance along a given path follows the same spirit as steepest descent based algorithms; see, for example, [[22](https://arxiv.org/html/2602.06424v1#bib.bib61 "Numerical evaluation of oscillatory integrals via automated steepest descent contour deformation")].

###### Remark C.1 (Boundary–Admissibility Condition (BAC)).

In order to analyze the oscillatory behavior near the boundaries, we must ensure that the mapped amplitude ak,p(ν)a\_{k,p}^{(\nu)} decays appropriately as we approach the hypercube boundary 𝐁\mathbf{B}. Otherwise, by ([C.1](https://arxiv.org/html/2602.06424v1#A3.E1 "In C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), the threshold point 𝐯∗\mathbf{v}^{\*} may not exist. Thus, for every 𝐯→𝐁\mathbf{v}\to\mathbf{B}, we require

|  |  |  |  |
| --- | --- | --- | --- |
| (C.3) |  | lim sup𝐯→𝐁|ak,p(ν)​(G−1​(𝐯,𝚯k,p))|​|detJG−1​(𝐯,𝚯k,p)|<∞.\limsup\_{\mathbf{v}\to\mathbf{B}}\;\left\lvert a\_{k,p}^{(\nu)}\!\left(G^{-1}\left(\mathbf{v},\boldsymbol{\Theta}\_{k,p}\right)\right)\,\right\rvert\left\lvert\det J\_{G^{-1}}\left(\mathbf{v},\boldsymbol{\Theta}\_{k,p}\right)\right\rvert\;<\;\infty. |  |

The BAC condition ensures that the envelope does not counteract the decay induced by the extended characteristic function, thereby guaranteeing the existence of a truncation radius and a finite oscillation count.

In Appendix [E.2](https://arxiv.org/html/2602.06424v1#A5.SS2 "E.2 Fourier transform of the given loss functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), we show that ℓ^k,p(ν)​(𝐮+i​𝐊)\widehat{\ell}^{(\nu)}\_{k,p}(\mathbf{u}+i\mathbf{K}) decays at most polynomially in ‖u‖\|u\| for fixed admissible 𝐊\mathbf{K}. By contrast, for the Gaussian and NIG models considered in Section [3](https://arxiv.org/html/2602.06424v1#S3 "3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), the extended CF Φ𝐗k,p​(𝐮+i​𝐊)\Phi\_{\mathbf{X}\_{k,p}}(\mathbf{u}+i\mathbf{K}) admits exponential-type decay in ‖u‖\|u\|. Consequently, as 𝐯→𝐁\mathbf{v}\to\mathbf{B} and ‖G−1​(𝐯)‖→∞\|G^{-1}(\mathbf{v})\|\to\infty, the boundary behavior of the product ΦXk,p​(G−1​(𝐯)+i​𝐊)​ℓ^k,p(ν)​(G−1​(𝐯)+i​𝐊)\Phi\_{X\_{k,p}}(G^{-1}(\mathbf{v})+i\mathbf{K})\,\widehat{\ell}^{(\nu)}\_{k,p}(G^{-1}(\mathbf{v})+i\mathbf{K}) is governed by Φ𝐗k,p\Phi\_{\mathbf{X}\_{k,p}}, up to polynomial factors.

So, in order to characterize the oscillatory behavior for our component integrands, we examine the behavior of its corresponding extended CF. The expression for NoscN\_{\text{osc}} near the boundaries, for a given loss distribution, 𝐗\mathbf{X} is provided in Table [C.1](https://arxiv.org/html/2602.06424v1#A3.T1 "Table C.1 ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). A detailed derivation is provided in Appendix [C.1.1](https://arxiv.org/html/2602.06424v1#A3.SS1.SSS1 "C.1.1 Approximating the number of oscillation for specific loss distributions ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

|  |  |
| --- | --- |
| Distribution | Nosc​(𝐯)N\_{\mathrm{osc}}(\mathbf{v}) |
| Gaussian | C​(𝐯∗)​|𝐦k,p⊤​r𝐁|2​π​1λmin​(𝚺k,p)\displaystyle C(\mathbf{v}^{\*})\frac{|\mathbf{m}\_{k,p}^{\top}r\_{\mathbf{B}}|}{\sqrt{2}\pi}\sqrt{\frac{1}{\lambda\_{\min}(\boldsymbol{\Sigma}\_{k,p})}} |
| NIG | C​(𝐯∗)​|𝐦k,p⊤​r𝐁|2​π​1δk,p​λmin​(𝚪k,p)\displaystyle C(\mathbf{v}^{\*})\frac{|\mathbf{m}\_{k,p}^{\top}r\_{\mathbf{B}}|}{2\pi}\frac{1}{\delta\_{k,p}\sqrt{\lambda\_{\min}(\boldsymbol{\Gamma}\_{k,p})}} |

Table C.1: Asymptotic scaling of the oscillation count NoscN\_{\mathrm{osc}} near a boundary face 𝐁\mathbf{B} for the Gaussian and NIG reference models (see Appendix [C.1.1](https://arxiv.org/html/2602.06424v1#A3.SS1.SSS1 "C.1.1 Approximating the number of oscillation for specific loss distributions ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")). In the Gaussian case, 𝚺k,p\boldsymbol{\Sigma}\_{k,p} is defined in Example [E.1](https://arxiv.org/html/2602.06424v1#A5.Thmtheorem1 "Example E.1 (Gaussian). ‣ E.3 Loss vector distributions and extended characteristic functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). In the NIG case, 𝚪k,p\boldsymbol{\Gamma}\_{k,p} and δk,p\delta\_{k,p} are defined in Example [E.2](https://arxiv.org/html/2602.06424v1#A5.Thmtheorem2 "Example E.2 (Normal Inverse Gaussian (NIG)). ‣ E.3 Loss vector distributions and extended characteristic functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

|  |  |  |
| --- | --- | --- |
|  | C​(𝐯∗)={log⁡(C​|detJG−1​(𝐯∗,𝚯k,p)|ξ),if ​𝐗∼𝒩,log⁡(C​|detJG−1​(𝐯∗,𝚯k,p)|ξ),if ​𝐗∼𝒩​ℐ​𝒢.C(\mathbf{v}^{\*})=\begin{cases}\displaystyle\sqrt{\log\!\left(\dfrac{C\,\bigl|\det J\_{G^{-1}}(\mathbf{v}^{\*},\boldsymbol{\Theta}\_{k,p})\bigr|}{\xi}\right)},&\text{if }\mathbf{X}\sim\mathcal{N},\\[8.0pt] \displaystyle\log\!\left(\dfrac{C\,\bigl|\det J\_{G^{-1}}(\mathbf{v}^{\*},\boldsymbol{\Theta}\_{k,p})\bigr|}{\xi}\right),&\text{if }\mathbf{X}\sim\mathcal{NIG}.\end{cases} |  |

###### Remark C.2.

The estimates in Table [C.1](https://arxiv.org/html/2602.06424v1#A3.T1 "Table C.1 ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") distinguish two cases:
for the Gaussian case, the decay of the CF damps oscillations much more rapidly, while in the NIG setting, the slower exponential decay allows oscillatory behavior to persist over a wider region near the boundary.

###### Remark C.3.

The factor
1λmin​(⋅)\frac{1}{\sqrt{\lambda\_{\min}(\,\cdot\,)}}
originates from the truncation radius U∗U\_{\*}. As λmin​(⋅)→0\lambda\_{\min}(\,\cdot\,)\to 0, the envelope decays increasingly slowly, which causes both U∗U\_{\*} and, consequently, NoscN\_{\text{osc}} to diverge. In the degenerate case λmin​(⋅)=0\lambda\_{\min}(\,\cdot\,)=0, there is no decay along at least one direction. Hence U∗U\_{\*} is not finite and NoscN\_{\text{osc}} cannot be estimated using formulas in Table [C.1](https://arxiv.org/html/2602.06424v1#A3.T1 "Table C.1 ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). In this situation, the integrand exhibits non-decaying tails and might have piecewise “kinked” behavior near the boundary.

From Remarks [C.3](https://arxiv.org/html/2602.06424v1#A3.E3 "In Remark C.1 (Boundary–Admissibility Condition (BAC)). ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), [C.3](https://arxiv.org/html/2602.06424v1#A3.Thmtheorem3 "Remark C.3. ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") together with
Table [C.1](https://arxiv.org/html/2602.06424v1#A3.T1 "Table C.1 ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), it follows that
the oscillatory behavior of the integrand can be improved by:

* •

  reducing the projection of |𝐦k,p⊤​r𝐁|\left\lvert\mathbf{m}\_{k,p}^{\top}r\_{\mathbf{B}}\right\rvert onto the
  preimage direction r𝐁r\_{\mathbf{B}};
* •

  matching the decay of the determinant at 𝐯∗\mathbf{v}^{\*},
  |detJG−1​(𝐯∗,𝚯k,p)|\left\lvert\det J\_{G^{-1}}(\mathbf{v}^{\*},\boldsymbol{\Theta}\_{k,p})\right\rvert with the decay of the extended CF Φ𝐗k,p\Phi\_{\mathbf{X}\_{k,p}}, while ensuring that the BAC condition holds
  and that the smallest eigenvalue λmin\lambda\_{\min} of the dispersion matrices
  (𝚺k,p,𝚪k,p)(\boldsymbol{\Sigma}\_{k,p},\boldsymbol{\Gamma}\_{k,p}) does not deteriorate (i.e. λmin↛0\lambda\_{\min}\not\to 0).

Regarding the former point, we always have |𝐦k,p⊤​r𝐁|≤‖𝐦k,p‖​‖r𝐁‖=‖𝐦k,p‖\left\lvert\mathbf{m}\_{k,p}^{\top}r\_{\mathbf{B}}\right\rvert\leq\left\lVert\mathbf{m}\_{k,p}\right\rVert\left\lVert r\_{\mathbf{B}}\right\rVert=\left\lVert\mathbf{m}\_{k,p}\right\rVert, and 𝐦k,p\mathbf{m}\_{k,p} is determined through the optimization procedure, so what matters more for our transformation is the latter point, which provides the rationale for the density-driven transformation mentioned in Section [4.1.1](https://arxiv.org/html/2602.06424v1#S4.SS1.SSS1 "4.1.1 Oscillation-Aware, Distribution-Dependent Domain Transformation ‣ 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

#### C.1.1 Approximating the number of oscillation for specific loss distributions

##### The Gaussian case.

Using the formula from Example [E.1](https://arxiv.org/html/2602.06424v1#A5.Thmtheorem1 "Example E.1 (Gaussian). ‣ E.3 Loss vector distributions and extended characteristic functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") in Appendix [E.3](https://arxiv.org/html/2602.06424v1#A5.SS3 "E.3 Loss vector distributions and extended characteristic functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") for the extended CF of the component, when 𝐯→𝐁\mathbf{v}\to\mathbf{B} we have

|  |  |  |
| --- | --- | --- |
|  | |ak,p(ν)​(G−1​(𝐯,𝚯k,p))|​|detJG−1​(𝐯,𝚯k,p)|≤C​|detJG−1​(𝐯,𝚯k,p)|​exp⁡(−12​λmin​(𝚺k,p)​|G−1​(𝐯,𝚯k,p)|2),\left\lvert a\_{k,p}^{(\nu)}\left(G^{-1}(\mathbf{v},\boldsymbol{\Theta}\_{k,p})\right)\right\rvert\,\left\lvert\det J\_{G^{-1}}(\mathbf{v},\boldsymbol{\Theta}\_{k,p})\right\rvert\;\leq\;C\big|\det J\_{G^{-1}}(\mathbf{v},\boldsymbol{\Theta}\_{k,p})\big|\exp\!\left(-\frac{1}{2}\lambda\_{\min}(\boldsymbol{\Sigma}\_{k,p})\left\lvert G^{-1}(\mathbf{v},\boldsymbol{\Theta}\_{k,p})\right\rvert^{2}\right), |  |

where C>0C>0. Hence, the truncation radius U∗U\_{\*} in
([C.1](https://arxiv.org/html/2602.06424v1#A3.E1 "In C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) satisfies

|  |  |  |
| --- | --- | --- |
|  | U∗=2λmin​(𝚺k,p)​log⁡C​|detJG−1​(𝐯∗,𝚯k,p)|ξ.U\_{\*}=\sqrt{\frac{2}{\lambda\_{\min}(\boldsymbol{\Sigma}\_{k,p})}\log\!\frac{C\big|\det J\_{G^{-1}}(\mathbf{v}^{\*},\boldsymbol{\Theta}\_{k,p})\big|}{\xi}}. |  |

Therefore, the number of oscillations near the boundary

|  |  |  |  |
| --- | --- | --- | --- |
| (C.4) |  | Nosc​(𝐯∗)≈|𝐦k,p⊤​r𝐁|2​π​2λmin​(𝚺k,p)​log⁡C​|detJG−1​(𝐯∗,𝚯k,p)|ξ.N\_{\text{osc}}(\mathbf{v}^{\*})\;\approx\;\frac{\left\lvert\mathbf{m}\_{k,p}^{\top}r\_{\mathbf{B}}\right\rvert}{2\pi}\sqrt{\frac{2}{\lambda\_{\min}(\boldsymbol{\Sigma}\_{k,p})}\log\!\frac{C\big|\det J\_{G^{-1}}(\mathbf{v}^{\*},\boldsymbol{\Theta}\_{k,p})\big|}{\xi}}. |  |

##### The NIG case.

Using the formula from Example [E.2](https://arxiv.org/html/2602.06424v1#A5.Thmtheorem2 "Example E.2 (Normal Inverse Gaussian (NIG)). ‣ E.3 Loss vector distributions and extended characteristic functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") in Appendix [E.3](https://arxiv.org/html/2602.06424v1#A5.SS3 "E.3 Loss vector distributions and extended characteristic functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), when
𝐯→𝐁\mathbf{v}\to\mathbf{B} we have that the extended CF of the component satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ𝐗k,p​(G−1​(𝐯,𝚯k,p)+i​𝐊k,p)\displaystyle\Phi\_{\mathbf{X}\_{k,p}}\left(G^{-1}(\mathbf{v},\boldsymbol{\Theta}\_{k,p})+\mathrm{i}\,\mathbf{K}\_{k,p}\right) | ≤C​exp⁡(−δk,p​|𝚪k,p1/2​(G−1​(𝐯,𝚯k,p))|)\displaystyle\leq C\exp\!\left(-\,\delta\_{k,p}\,\left\lvert\boldsymbol{\Gamma}\_{k,p}^{1/2}\left(G^{-1}(\mathbf{v},\boldsymbol{\Theta}\_{k,p})\right)\right\rvert\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​exp⁡(−δk,p​λmin​(𝚪k,p)​|G−1​(𝐯,𝚯k,p)|).\displaystyle\leq C\exp\!\left(-\,\delta\_{k,p}\,\sqrt{\lambda\_{\min}(\boldsymbol{\Gamma}\_{k,p})}\,\left\lvert G^{-1}(\mathbf{v},\boldsymbol{\Theta}\_{k,p})\right\rvert\right). |  |

|  |  |  |
| --- | --- | --- |
|  | ⇒|ak,p(ν)​(G−1​(𝐯,𝚯k,p))|​|detJG−1​(𝐯,𝚯k,p)|≤C​|detJG−1​(𝐯,𝚯k,p)|​exp⁡(−δk,p​λmin​(𝚪k,p)​|G−1​(𝐯,𝚯k,p)|).\Rightarrow\quad\begin{aligned} &\left\lvert a\_{k,p}^{(\nu)}\left(G^{-1}(\mathbf{v},\boldsymbol{\Theta}\_{k,p})\right)\right\rvert\,\left\lvert\det J\_{G^{-1}}(\mathbf{v},\boldsymbol{\Theta}\_{k,p})\right\rvert\\ &\qquad\leq\;C\,\big|\det J\_{G^{-1}}(\mathbf{v},\boldsymbol{\Theta}\_{k,p})\big|\,\exp\!\left(-\,\delta\_{k,p}\,\sqrt{\lambda\_{\min}(\boldsymbol{\Gamma}\_{k,p})}\,\left\lvert G^{-1}(\mathbf{v},\boldsymbol{\Theta}\_{k,p})\right\rvert\right).\end{aligned} |  |

Hence the truncation radius U∗U\_{\*} in ([C.1](https://arxiv.org/html/2602.06424v1#A3.E1 "In C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) satisfies

|  |  |  |
| --- | --- | --- |
|  | U∗=1δk,p​λmin​(𝚪k,p)​log⁡C​|detJG−1​(𝐯∗,𝚯k,p)|ξ.U\_{\*}\;=\;\frac{1}{\delta\_{k,p}\,\sqrt{\lambda\_{\min}(\boldsymbol{\Gamma}\_{k,p})}}\,\log\!\frac{C\big|\det J\_{G^{-1}}(\mathbf{v}^{\*},\boldsymbol{\Theta}\_{k,p})\big|}{\xi}. |  |

Consequently,

|  |  |  |  |
| --- | --- | --- | --- |
| (C.5) |  | Nosc​(𝐯∗)≈|𝐦k,p⊤​r𝐁|2​π​1δk,p​λmin​(𝚪k,p)​log⁡C​|detJG−1​(𝐯∗,𝚯k,p)|ξ.N\_{\text{osc}}(\mathbf{v}^{\*})\;\approx\;\frac{|\mathbf{m}\_{k,p}^{\top}r\_{\mathbf{B}}|}{2\pi}\,\frac{1}{\delta\_{k,p}\sqrt{\lambda\_{\min}(\boldsymbol{\Gamma}\_{k,p})}}\,\log\!\frac{C\big|\det J\_{G^{-1}}(\mathbf{v}^{\*},\boldsymbol{\Theta}\_{k,p})\big|}{\xi}. |  |

#### C.1.2 Choice of matrix 𝚺~k,p\widetilde{\boldsymbol{\Sigma}}\_{k,p}

Let
𝐲:=Ψ−1​(𝐯1:k,𝐈k).\mathbf{y}:=\Psi^{-1}(\mathbf{v}\_{1:k},\mathbf{I}\_{k}).

##### The Gaussian case.

A change of variables yields

|  |  |  |  |
| --- | --- | --- | --- |
| (C.6) |  | |detJ𝒯Gauss​(𝐯)|=|det𝑳~k,p|⏟∂𝐮/∂𝐲⋅∏i=1k1φ​(yi)⏟𝐲=ΨGauss−1​(𝐯1:k)∝|det𝑳~k,p|​exp⁡(12​‖𝐲‖2).\Bigl|\det J\_{\mathcal{T}\_{\text{Gauss}}(\mathbf{v})}\Bigr|\;=\;\underbrace{\,|\det\widetilde{\boldsymbol{L}}\_{k,p}|}\_{\partial\mathbf{u}/\partial\mathbf{y}}\cdot\underbrace{\prod\_{i=1}^{k}\frac{1}{\varphi(y\_{i})}}\_{\mathbf{y}=\Psi^{-1}\_{\text{Gauss}}(\mathbf{v}\_{1:k})}\;\propto\;\left|\det\widetilde{\boldsymbol{L}}\_{k,p}\right|\exp\!\left(\tfrac{1}{2}\|\mathbf{y}\|^{2}\right). |  |

Accordingly, the truncation radius U∗U\_{\*} becomes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (C.7) |  | |ak,p(ν)​(𝒯Gauss​(𝐯∗))|​|detJ𝒯Gauss​(𝐯∗)|\displaystyle\left\lvert a\_{k,p}^{(\nu)}\!\left(\mathcal{T}\_{\text{Gauss}}(\mathbf{v}^{\*})\right)\right\rvert\left\lvert\det J\_{\mathcal{T}\_{\text{Gauss}}}(\mathbf{v}^{\*})\right\rvert | ∝|det𝑳~k,p|​exp⁡(12​‖𝐲∗‖2)​Φ𝐗k,pGauss​(𝑳~k,p​𝐲∗+i​𝐊k,p(ν))\displaystyle\;\propto\;\left|\det\widetilde{\boldsymbol{L}}\_{k,p}\right|\exp\!\left(\tfrac{1}{2}\|\mathbf{y^{\*}}\|^{2}\right)\Phi\_{\mathbf{X}\_{k,p}}^{\mathrm{Gauss}}\left(\widetilde{\boldsymbol{L}}\_{k,p}\mathbf{y^{\*}}+\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right) |  |
|  |  | ∝|det𝑳~k,p|​exp⁡[−12​𝐲∗⊤​(𝑳~k,p⊤​𝚺k,p​𝑳~k,p−𝑰k)​𝐲∗]\displaystyle\;\propto\;\left|\det\widetilde{\boldsymbol{L}}\_{k,p}\right|\exp\!\left[-\tfrac{1}{2}\,\mathbf{y^{\*}}^{\top}\left(\widetilde{\boldsymbol{L}}\_{k,p}^{\top}\boldsymbol{\Sigma}\_{k,p}\widetilde{\boldsymbol{L}}\_{k,p}-\boldsymbol{I}\_{k}\right)\,\mathbf{y^{\*}}\right] |  |
|  |  | =|det𝑳~k,p|​exp⁡[−12​𝐮∗⊤​(𝚺k,p−𝚺~k,p−1)​𝐮∗],\displaystyle\;=\;\left|\det\widetilde{\boldsymbol{L}}\_{k,p}\right|\exp\!\left[-\tfrac{1}{2}\,\mathbf{u^{\*}}^{\top}\left(\boldsymbol{\Sigma}\_{k,p}-\widetilde{\boldsymbol{\Sigma}}\_{k,p}^{-1}\right)\,\mathbf{u^{\*}}\right], |  |

To satisfy the BAC condition (Remark [C.3](https://arxiv.org/html/2602.06424v1#A3.E3 "In Remark C.1 (Boundary–Admissibility Condition (BAC)). ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), it is necessary that

|  |  |  |  |
| --- | --- | --- | --- |
| (C.8) |  | 𝚺k,p−𝚺~k,p−1⪰0\boldsymbol{\Sigma}\_{k,p}-\widetilde{\boldsymbol{\Sigma}}\_{k,p}^{-1}\succeq 0 |  |

, which coincides with the condition derived in [[4](https://arxiv.org/html/2602.06424v1#bib.bib72 "Quasi-Monte Carlo with Domain Transformation for Efficient Fourier Pricing of Multi-Asset Options"), Section 3.2.1] for the GBM model with T=1T=1.

The number of oscillations near the boundary is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (C.9) |  | NoscGauss∝‖𝐦k,p‖λmin​(𝚺k,p−𝚺~k,p−1)​C.N\_{\text{osc}}^{\text{Gauss}}\;\propto\;\frac{\|\mathbf{m}\_{k,p}\|}{\sqrt{\lambda\_{\min}\!\bigl(\boldsymbol{\Sigma}\_{k,p}-\widetilde{\boldsymbol{\Sigma}}\_{k,p}^{-1}\bigr)}}\;\sqrt{{C}}. |  |

To avoid the degeneracy for λmin\lambda\_{\min} (Remark [C.3](https://arxiv.org/html/2602.06424v1#A3.Thmtheorem3 "Remark C.3. ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), we require

|  |  |  |
| --- | --- | --- |
|  | 𝚺k,p≻𝚺~k,p−1.\boldsymbol{\Sigma}\_{k,p}\succ\widetilde{\boldsymbol{\Sigma}}\_{k,p}^{-1}. |  |

A convenient parametrization is

|  |  |  |  |
| --- | --- | --- | --- |
| (C.10) |  | 𝚺~k,p−1=1c​𝚺k,p,c>1.\widetilde{\boldsymbol{\Sigma}}\_{k,p}^{-1}=\frac{1}{c}\,\boldsymbol{\Sigma}\_{k,p},\qquad c>1. |  |

##### The NIG case.

We have:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (C.11) |  | |detJ𝒯NIG​(𝐯)|\displaystyle\left\lvert\det J\_{\mathcal{T}\_{\mathrm{NIG}}}(\mathbf{v})\right\rvert | =wk/2​|det𝑳~k,p|⏟∂𝐮/∂𝐲⋅∏i=1k1φ​(yi)⏟𝐲=ΦGauss−1​(𝐯1:k)⋅1ψW​(w)⏟w=ΨW−1​(vk+1)\displaystyle=\;\underbrace{w^{k/2}\,\left\lvert\det\widetilde{\boldsymbol{L}}\_{k,p}\right\rvert}\_{\partial\mathbf{u}/\partial\mathbf{y}}\cdot\underbrace{\prod\_{i=1}^{k}\frac{1}{\varphi(y\_{i})}}\_{\mathbf{y}=\Phi\_{\mathrm{Gauss}}^{-1}(\mathbf{v}\_{1:k})}\cdot\underbrace{\frac{1}{\psi\_{W}(w)}}\_{w=\Psi\_{W}^{-1}(v\_{k+1})} |  |
|  |  | ∝wk/2​|det𝑳~k,p|​exp⁡(12​‖𝐲‖2)ψW​(w)\displaystyle\propto w^{k/2}\,\left\lvert\det\widetilde{\boldsymbol{L}}\_{k,p}\right\rvert\,\frac{\exp\!\left(\tfrac{1}{2}\|\mathbf{y}\|^{2}\right)}{\psi\_{W}(w)} |  |
|  |  | ∝wk/2​|det𝑳~k,p|​exp⁡(12​w​𝐮⊤​𝚺~k,p−1​𝐮)ψW​(w).\displaystyle\propto w^{k/2}\,\left\lvert\det\widetilde{\boldsymbol{L}}\_{k,p}\right\rvert\,\frac{\exp\!\left(\tfrac{1}{2w}\,\mathbf{u}^{\top}\widetilde{\boldsymbol{\Sigma}}\_{k,p}^{-1}\,\mathbf{u}\right)}{\psi\_{W}(w)}. |  |

Define the *effective determinant* 𝒟U​(𝐮)\mathcal{D}\_{U}(\mathbf{u}) for the transform of 𝐮\mathbf{u} as

|  |  |  |  |
| --- | --- | --- | --- |
| (C.12) |  | 𝒟U​(𝐮):=[∫ℝ+d​w|detJ𝒯NIG​(𝐯)|]−1.\mathcal{D}\_{U}(\mathbf{u}):=\left[\int\_{\mathbb{R}^{+}}\frac{dw}{\big|\det J\_{\mathcal{T}\_{\mathrm{NIG}}}(\mathbf{v})\big|}\right]^{-1}. |  |

This quantity represents the inverse of the multivariate Laplace density ψlap\psi^{\mathrm{lap}}. In fact,

|  |  |  |  |
| --- | --- | --- | --- |
| (C.13) |  | 𝒟U​(𝐮)=1ψlap​(𝐮)∝|det𝑳~k,p|Kλ​(2​𝐮⊤​𝚺~k,p−1​𝐮),\mathcal{D}\_{U}(\mathbf{u})=\frac{1}{\psi^{\mathrm{lap}}(\mathbf{u)}}\;\propto\;\frac{|\det\widetilde{\boldsymbol{L}}\_{k,p}|}{K\_{\lambda}\!\left(\sqrt{2\,\mathbf{u}^{\top}\widetilde{\boldsymbol{\Sigma}}\_{k,p}^{-1}\,\mathbf{u}}\right)}, |  |

where Kλ​(⋅)K\_{\lambda}(\cdot) denotes the modified Bessel function of the third kind. The truncation radius at U∗U\_{\*} then becomes

|  |  |  |  |
| --- | --- | --- | --- |
| (C.14) |  | |ak,p(ν)​(𝐮∗)|​|𝒟U​(𝐮∗)|∝|det𝚺~k,p|12Kλ​(2​𝐮∗⊤​𝚺~k,p−1​𝐮∗)×Φ𝐗k,pNIG​(𝐮∗+i​𝐊k,p(ν)).\left\lvert a\_{k,p}^{(\nu)}\!\left(\mathbf{u}^{\*}\right)\right\rvert\left\lvert\mathcal{D}\_{U}(\mathbf{u}^{\*})\right\rvert\;\propto\;\frac{\left\lvert\det\widetilde{\boldsymbol{\Sigma}}\_{k,p}\right\rvert^{\tfrac{1}{2}}}{K\_{\lambda}\!\left(\sqrt{2\,\mathbf{u^{\*}}^{\top}\widetilde{\boldsymbol{\Sigma}}\_{k,p}^{-1}\,\mathbf{u^{\*}}}\right)}\,\times\,\Phi\_{\mathbf{X}\_{k,p}}^{\mathrm{NIG}}\left(\mathbf{u^{\*}}+\mathrm{i}\mathbf{K}\_{k,p}^{(\nu)}\right). |  |

Following the same arguments as in [[4](https://arxiv.org/html/2602.06424v1#bib.bib72 "Quasi-Monte Carlo with Domain Transformation for Efficient Fourier Pricing of Multi-Asset Options"), Section 3.2.2] with T=1T=1, we can have:

|  |  |  |  |
| --- | --- | --- | --- |
| (C.15) |  | |ak,p(ν)​(𝐮∗)|​|𝒟U​(𝐮∗)|∝|det𝚺~k,p|12​exp⁡[−(δk,p​𝐮∗⊤​𝚪k,p​𝐮∗−2​𝐮∗⊤​𝚺~k,p−1​𝐮∗)]\left\lvert a\_{k,p}^{(\nu)}\!\left(\mathbf{u}^{\*}\right)\right\rvert\left\lvert\mathcal{D}\_{U}(\mathbf{u}^{\*})\right\rvert\;\propto\;\left\lvert\det\widetilde{\boldsymbol{\Sigma}}\_{k,p}\right\rvert^{\tfrac{1}{2}}\exp\left[-\left(\delta\_{k,p}\sqrt{\mathbf{u^{\*}}^{\top}\boldsymbol{\Gamma}\_{k,p}\mathbf{u^{\*}}}-\sqrt{2\mathbf{u^{\*}}^{\top}\widetilde{\boldsymbol{\Sigma}}^{-1}\_{k,p}\mathbf{u^{\*}}}\right)\right] |  |

To satisfy the BAC condition (Remark [C.3](https://arxiv.org/html/2602.06424v1#A3.E3 "In Remark C.1 (Boundary–Admissibility Condition (BAC)). ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")), it is required that

|  |  |  |  |
| --- | --- | --- | --- |
| (C.16) |  | δk,p2​𝚪k,p−2​𝚺~k,p−1⪰0.\delta\_{k,p}^{2}\boldsymbol{\Gamma}\_{k,p}-2\widetilde{\boldsymbol{\Sigma}}\_{k,p}^{-1}\succeq 0. |  |

Analogous to the Gaussian case in ([C.9](https://arxiv.org/html/2602.06424v1#A3.E9 "In The Gaussian case. ‣ C.1.2 Choice of matrix 𝚺̃_{𝑘,𝑝} ‣ C.1 Boundary Oscillation Analysis ‣ Appendix C Supplementary results for Section 4.1.1 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")),
we impose the strict inequality

|  |  |  |
| --- | --- | --- |
|  | δk,p2​𝚪k,p≻2​𝚺~k,p−1,\delta\_{k,p}^{2}\boldsymbol{\Gamma}\_{k,p}\succ 2\widetilde{\boldsymbol{\Sigma}}\_{k,p}^{-1}, |  |

and choose the parametrization

|  |  |  |  |
| --- | --- | --- | --- |
| (C.17) |  | 𝚺~k,p−1=δk,p2​𝚪k,p2​c,c>1.\widetilde{\boldsymbol{\Sigma}}\_{k,p}^{-1}=\frac{\delta\_{k,p}^{2}\boldsymbol{\Gamma}\_{k,p}}{2c},\qquad c>1. |  |

## Appendix D Convergence analysis for the SAA method

Before presenting the convergence analysis of the SAA method, we introduce the notation and estimators used throughout this appendix. Let {𝐗(i)}i=1N\{\mathbf{X}^{(i)}\}\_{i=1}^{N} be i.i.d. copies of 𝐗\mathbf{X}, drawn once and kept fixed throughout the optimization. The MC estimators of g,∇gg,\nabla g and ∇2g\nabla^{2}g are defined by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (D.1) |  | g^N(0),SAA​(𝐦)\displaystyle\widehat{g}^{(0),\mathrm{SAA}}\_{N}(\mathbf{m}) | :=1N​∑i=1Nℓ​(𝐗(i)−𝐦),\displaystyle=\frac{1}{N}\sum\_{i=1}^{N}\ell\!\big(\mathbf{X}^{(i)}-\mathbf{m}\big), |  |
|  | g^N(1),SAA​(𝐦)\displaystyle\widehat{g}^{(1),\mathrm{SAA}}\_{N}(\mathbf{m}) | :=1N​∑i=1N∇ℓ​(𝐗(i)−𝐦),\displaystyle=\frac{1}{N}\sum\_{i=1}^{N}\nabla\ell\!\big(\mathbf{X}^{(i)}-\mathbf{m}\big), |  |
|  | g^N(2),SAA​(𝐦)\displaystyle\widehat{g}^{(2),\mathrm{SAA}}\_{N}(\mathbf{m}) | :=1N​∑i=1N∇2ℓ​(𝐗(i)−𝐦).\displaystyle=\frac{1}{N}\sum\_{i=1}^{N}\nabla^{2}\ell\!\big(\mathbf{X}^{(i)}-\mathbf{m}\big). |  |

and the corresponding MC estimators for the Lagrangian as:

|  |  |  |
| --- | --- | --- |
|  | ℒN(0),SAA​(𝐳):=∑k=1dmk+λ​g^N(0),SAA​(𝐦),ℒN(1),SAA​(𝐳):=[𝟏−λ​g^N(1),SAA​(𝐦)−g^N(0),SAA​(𝐦)],\mathcal{L}\_{N}^{(0),\mathrm{SAA}}(\mathbf{z}):=\sum\_{k=1}^{d}m\_{k}+\lambda\,\widehat{g}^{(0),\mathrm{SAA}}\_{N}(\mathbf{m}),\qquad\mathcal{L}\_{N}^{(1),\mathrm{SAA}}(\mathbf{z}):=\begin{bmatrix}\mathbf{1}-\lambda\,\widehat{g}^{(1),\mathrm{SAA}}\_{N}(\mathbf{m})\\[3.0pt] -\,\widehat{g}^{(0),\mathrm{SAA}}\_{N}(\mathbf{m})\end{bmatrix}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ℒN(2),SAA​(𝐳):=[−λ​g^N(2),SAA​(𝐦)(g^N(1),SAA​(𝐦))⊤g^N(1),SAA(𝐦))0].\mathcal{L}\_{N}^{(2),\mathrm{SAA}}(\mathbf{z}):=\begin{bmatrix}-\lambda\,\widehat{g}^{(2),\mathrm{SAA}}\_{N}(\mathbf{m})&\big(\widehat{g}^{(1),\mathrm{SAA}}\_{N}(\mathbf{m})\big)^{\!\top}\\[3.0pt] \widehat{g}^{(1),\mathrm{SAA}}\_{N}(\mathbf{m}))&0\end{bmatrix}. |  |

To establish consistency and asymptotic efficiency of the SAA solution in
Propositions [D.2](https://arxiv.org/html/2602.06424v1#A4.Thmtheorem2 "Proposition D.2 (Consistency of the SAA solution). ‣ Appendix D Convergence analysis for the SAA method ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") and [D.3](https://arxiv.org/html/2602.06424v1#A4.Thmtheorem3 "Proposition D.3 (Asymptotic behavior of the SAA solution). ‣ Appendix D Convergence analysis for the SAA method ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), we adopt the framework in [[50](https://arxiv.org/html/2602.06424v1#bib.bib55 "Lectures on Stochastic Programming: Modeling and Theory, Second Edition"), Section 5.2] and impose the following condition.

###### Assumption D.1.

1. 1.

   For every 𝐦𝟎∈ℝd\mathbf{m\_{0}}\in\mathbb{R}^{d}, the mapping 𝐦↦∇2ℓ​(𝐗−𝐦)\mathbf{m}\mapsto\nabla^{2}\ell(\mathbf{X-m}) is continuous at 𝐦0\mathbf{m}\_{0} a.s.
2. 2.

   There exist integrable random variables D0,D1,D2D\_{0},D\_{1},D\_{2} such that, for all 𝐦∈M\mathbf{m}\in M a.s.,

   |  |  |  |
   | --- | --- | --- |
   |  | |ℓ​(𝐗−𝐦)|≤D0,‖∇ℓ​(𝐗−𝐦)‖≤D1,‖∇2ℓ​(𝐗−𝐦)‖≤D2.|\ell(\mathbf{X}-\mathbf{m})|\leq D\_{0},\qquad\|\nabla\ell(\mathbf{X}-\mathbf{m})\|\leq D\_{1},\qquad\|\nabla^{2}\ell(\mathbf{X}-\mathbf{m})\|\leq D\_{2}. |  |

###### Proposition D.2 (Consistency of the SAA solution).

Suppose Assumptions [A.1](https://arxiv.org/html/2602.06424v1#A1.Thmtheorem1 "Assumption A.1 (Regularity conditions for the exact problem). ‣ A.1 Additional Assumptions for the Error Analysis ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") and [D.1](https://arxiv.org/html/2602.06424v1#A4.Thmtheorem1 "Assumption D.1. ‣ Appendix D Convergence analysis for the SAA method ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") hold. Then, as N→∞N\to\infty, the SAA problem admits a unique optimal solution
𝐳NSAA,∗∈𝒵\mathbf{z}\_{N}^{\mathrm{SAA},\*}\in\mathcal{Z}, and

|  |  |  |
| --- | --- | --- |
|  | 𝐳NSAA,∗→a.s.𝐳∗.\mathbf{z}\_{N}^{\mathrm{SAA},\*}\xrightarrow[]{\mathrm{a.s.}}\mathbf{z}^{\*}. |  |

###### Proof.

The proof follows the same line of arguments as that of Theorem [5.7](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem7 "Theorem 5.7 (Consistency of solution from Fourier-RQMC problem). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). Uniform convergence of the SAA estimators is established in [[51](https://arxiv.org/html/2602.06424v1#bib.bib183 "Monte Carlo Sampling Methods"), Proposition 7] ; here, we adapt this result to the functions ℓ\ell, ∇ℓ\nabla\ell, and ∇2ℓ\nabla^{2}\ell under the given norm ∥.∥\left\lVert.\right\rVert. With these uniform convergence properties in place, the Banach fixed-point argument applies in the same manner as in the Fourier-RQMC case.
∎

###### Proposition D.3 (Asymptotic behavior of the SAA solution).

Suppose Assumptions [A.1](https://arxiv.org/html/2602.06424v1#A1.Thmtheorem1 "Assumption A.1 (Regularity conditions for the exact problem). ‣ A.1 Additional Assumptions for the Error Analysis ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") and [D.1](https://arxiv.org/html/2602.06424v1#A4.Thmtheorem1 "Assumption D.1. ‣ Appendix D Convergence analysis for the SAA method ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") hold.
Then, as N→∞N\to\infty, the SAA solution satisfies

|  |  |  |  |
| --- | --- | --- | --- |
| (D.2) |  | N​(𝐳NSAA,∗−𝐳∗)→law𝒩​(𝟎,𝑽​(𝐳∗)),\sqrt{N}\bigl(\mathbf{z}\_{N}^{\mathrm{SAA},\*}-\mathbf{z}^{\*}\bigr)\xrightarrow{\mathrm{law}}\mathcal{N}\!\left(\mathbf{0},\boldsymbol{V}(\mathbf{z}^{\*})\right), |  |

where the asymptotic covariance matrix is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (D.3) |  | 𝑽​(𝐳∗)=(∇𝐳2ℒ​(𝐳∗))−1​𝑯​(𝐳∗)​(∇𝐳2ℒ​(𝐳∗))−1,\boldsymbol{V}(\mathbf{z}^{\*})=\Bigl({{\nabla\_{\mathbf{z}}^{2}}\mathcal{L}}\bigl(\mathbf{z}^{\*}\bigr)\Bigr)^{-1}\boldsymbol{H}(\mathbf{z}^{\*})\Bigl({{\nabla\_{\mathbf{z}}^{2}}\mathcal{L}}\bigl(\mathbf{z}^{\*}\bigr)\Bigr)^{-1}, |  |

with

|  |  |  |
| --- | --- | --- |
|  | 𝑯​(𝐳∗)=Var𝐗​(∇𝐳ℒ​(𝐗,𝐳∗)).\boldsymbol{H}(\mathbf{z}^{\*})=\mathrm{Var}\_{\mathbf{X}}\!\left({{\nabla\_{\mathbf{z}}}\mathcal{L}}\bigl(\mathbf{X},\mathbf{z}^{\*}\bigr)\right). |  |

###### Proof.

The result follows by the same argument as in the proof Theorem [5.9](https://arxiv.org/html/2602.06424v1#S5.Thmtheorem9 "Theorem 5.9 (CLT for the Fourier-RQMC solution). ‣ 5.2 Statistical Error and Asymptotic Analysis ‣ 5 Error and Complexity Analysis for Fourier–RQMC Methods ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk") in Appendix [A.4](https://arxiv.org/html/2602.06424v1#A1.SS4 "A.4 Proof for Theorem 5.9 ‣ Appendix A Supplementary results for Sections 5 ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), term (A), with SshiftS\_{\mathrm{shift}} replaced by NN; see [[50](https://arxiv.org/html/2602.06424v1#bib.bib55 "Lectures on Stochastic Programming: Modeling and Theory, Second Edition"), Section 5.2.2].
∎

In the numerical experiments, we estimate the statistical error at the solution for SAA by replacing 𝑯\boldsymbol{H} with the SAA estimator 𝑯^NSAA\widehat{\boldsymbol{H}}^{\mathrm{SAA}}\_{N}, computed from Var​[ℒN(1),SAA​(𝐳∗)]\mathrm{Var}\left[\mathcal{L}\_{N}^{(1),\mathrm{SAA}}(\mathbf{z}^{\*})\right], and by approximating ∇𝐳2ℒ{\nabla\_{\mathbf{z}}^{2}}\mathcal{L} with ℒN(2),SAA\mathcal{L}\_{N}^{(2),\mathrm{SAA}}. These two quantities define 𝑽NSAA​(𝐳∗)\boldsymbol{V}\_{N}^{\mathrm{SAA}}(\mathbf{z}^{\*}), yielding

|  |  |  |  |
| --- | --- | --- | --- |
| (D.4) |  | εNSAA​(𝐳∗)=CαN​‖𝑽NSAA​(⋅;𝐳∗)‖.\varepsilon\_{N}^{\mathrm{SAA}}(\mathbf{z}^{\*})=\frac{C\_{\alpha}}{\sqrt{N}}\,\sqrt{\left\lVert\boldsymbol{V}\_{N}^{\mathrm{SAA}}(\cdot;\mathbf{z}^{\*})\right\rVert}. |  |

where CαC\_{\alpha} is defined in ([4.4](https://arxiv.org/html/2602.06424v1#S4.E4 "In 4.1 Single-Level Fourier–RQMC Approximation with Domain Transformation ‣ 4 Single- and Multilevel RQMC Approximation of Fourier-Based MSRM Integrals ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

## Appendix E Fourier Representation of the MSRM problem

### E.1 Proof for Corollary [3.4](https://arxiv.org/html/2602.06424v1#S3.Thmtheorem4 "Corollary 3.4 (Fourier representations for MSRM problem). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")

Let
ℓ𝐊(ν)(ν)​(𝐱):=e⟨𝐊(ν),𝐱⟩​ℓ(ν)​(𝐱)\ell^{(\nu)}\_{\mathbf{K}^{(\nu)}}(\mathbf{x}):=e^{\langle\mathbf{K}^{(\nu)},\mathbf{x}\rangle}\ell^{(\nu)}(\mathbf{x}) and ℓ^𝐊(ν)(ν)​(𝐱):=e⟨𝐊(ν),𝐱⟩​ℓ^(ν)​(𝐱)\widehat{\ell}^{(\nu)}\_{\mathbf{K}^{(\nu)}}(\mathbf{x}):=e^{\langle\mathbf{K}^{(\nu)},\mathbf{x}\rangle}\widehat{\ell}^{(\nu)}(\mathbf{x}). Now, using the inverse generalized Fourier transform theorem
[[29](https://arxiv.org/html/2602.06424v1#bib.bib187 "The Analysis of Linear Partial Differential Operators IV")], we express ℓ(ν)\ell^{(\nu)} as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (E.1) |  | ℓ(ν)​(𝐱−𝐦)\displaystyle\ell^{(\nu)}(\mathbf{x}-\mathbf{m}) | =ℜ⁡[(2​π)−d​e⟨−𝐊(ν),𝐱−𝐦⟩​∫ℝdei​⟨𝐰,𝐱−𝐦⟩​ℓ^(ν)𝐊(ν)​(𝐰)​d𝐰],\displaystyle=\Re\left[(2\pi)^{-d}e^{\langle\mathbf{-K}^{(\nu)},\mathbf{x-\mathbf{m}}\rangle}\int\_{\mathbb{R}^{d}}e^{\mathrm{i}\langle\mathbf{w},\mathbf{x-\mathbf{m}}\rangle}{\widehat{\ell}^{(\nu)}}\_{\mathbf{K}^{(\nu)}}(\mathbf{w})\mathrm{d}\mathbf{w}\right],\> |  |
|  |  | =ℜ⁡[(2​π)−d​e⟨−𝐊(ν),𝐱−𝐦⟩​∫ℝdei​⟨𝐰,𝐱−𝐦⟩​ℓ^(ν)​(𝐰+i​𝐊(ν))​d𝐰],𝐊(ν)∈δℓ(ν),𝐱∈ℝd\displaystyle=\Re\left[(2\pi)^{-d}e^{\langle\mathbf{-K}^{(\nu)},\mathbf{x-\mathbf{m}}\rangle}\int\_{\mathbb{R}^{d}}e^{\mathrm{i}\langle\mathbf{w},\mathbf{x-\mathbf{m}}\rangle}{\widehat{\ell}^{(\nu)}}\left(\mathbf{w}+\mathrm{i}\mathbf{K}^{(\nu)}\right)\mathrm{d}\mathbf{w}\right],\>\mathbf{K}^{(\nu)}\in{\delta}\_{\ell}^{(\nu)},\>\mathbf{x}\in\mathbb{R}^{d} |  |

Here we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ^(ν)𝐊(ν)​(𝐰)\displaystyle{\widehat{\ell}^{(\nu)}}\_{\mathbf{K}^{(\nu)}}(\mathbf{w}) | =∫ℝde−i​⟨𝐰,𝐱−𝐦∗⟩​e⟨𝐊(ν),𝐱−𝐦∗⟩​ℓ(ν)​(𝐱−𝐦∗)​d𝐱\displaystyle=\int\_{\mathbb{R}^{d}}e^{-\mathrm{i}\langle\mathbf{w},\mathbf{x-\mathbf{m^{\*}}}\rangle}e^{\langle\mathbf{K}^{(\nu)},\mathbf{x-\mathbf{m^{\*}}}\rangle}\ell^{(\nu)}(\mathbf{x}-\mathbf{m^{\*}})\mathrm{d}\mathbf{x} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫ℝde−i​⟨𝐰+i​𝐊(ν),𝐱−𝐦∗⟩​ℓ(ν)​(𝐱−𝐦∗)​d𝐱=ℓ^(ν)​(𝐰+i​𝐊(ν))\displaystyle=\int\_{\mathbb{R}^{d}}e^{-\mathrm{i}\langle\mathbf{w}+\mathrm{i}\mathbf{K}^{(\nu)},\mathbf{x-\mathbf{m^{\*}}}\rangle}\ell^{(\nu)}(\mathbf{x}-\mathbf{m^{\*}})\mathrm{d}\mathbf{x}={\widehat{\ell}^{(\nu)}}(\mathbf{w}+\mathrm{i}\mathbf{K}^{(\nu)}) |  |

Let 𝔼​[ℓ(ν)​(𝐗−𝐦)]:=∫ℝdℓ(ν)​(𝐱−𝐦)​f𝐗​(𝐱)​d𝐱\mathbb{E}[\ell^{(\nu)}(\mathbf{X}-\mathbf{m})]:=\int\_{\mathbb{R}^{d}}\ell^{(\nu)}(\mathbf{x-\mathbf{m}})f\_{\mathbf{X}}(\mathbf{x})\mathrm{d}\mathbf{x}, then using ([E.1](https://arxiv.org/html/2602.06424v1#A5.E1 "In E.1 Proof for Corollary 3.4 ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")) and Fubini’s theorem, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | g^(ν),Fou​(𝐦)\displaystyle\widehat{g}^{(\nu),\mathrm{Fou}}(\mathbf{m}) | =𝔼​[ℓ(ν)​(𝐗−𝐦)]=∫ℝdℓ(ν)​(𝐱−𝐦)​f𝐗​(𝐱)​d𝐱,\displaystyle=\mathbb{E}[\ell^{(\nu)}(\mathbf{X}-\mathbf{m})]=\int\_{\mathbb{R}^{d}}\ell^{(\nu)}(\mathbf{x-\mathbf{m}})f\_{\mathbf{X}}(\mathbf{x})\mathrm{d}\mathbf{x}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(2​π)−d​𝔼f𝐗​ℜ⁡[(2​π)−d​e⟨−𝐊(ν),𝐱−𝐦⟩​∫ℝdei​⟨𝐰,𝐱−𝐦⟩​ℓ^(ν)​(𝐰+i​𝐊(ν))​𝑑𝐰],𝐊(ν)∈δℓ(ν)\displaystyle=(2\pi)^{-d}\mathbb{E}\_{f\_{\mathbf{X}}}\Re\left[(2\pi)^{-d}e^{\langle\mathbf{-K}^{(\nu)},\mathbf{x-\mathbf{m}}\rangle}\int\_{\mathbb{R}^{d}}e^{\mathrm{i}\langle\mathbf{w},\mathbf{x-\mathbf{m}}\rangle}{\widehat{\ell}^{(\nu)}}\left(\mathbf{w}+\mathrm{i}\mathbf{K}^{(\nu)}\right)d\mathbf{w}\right],\quad\mathbf{K}^{(\nu)}\in{\delta}\_{\ell}^{(\nu)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(2​π)−d​ℜ⁡(∫ℝde⟨𝐊(ν)−i​𝐰,𝐦⟩​𝔼f𝐗​[ei​⟨𝐰+i​𝐊(ν),𝐗⟩]​ℓ^(ν)​(𝐰+i​𝐊(ν))​d𝐰),𝐊(ν)∈δK(ν)=δℓ(ν)∩δX\displaystyle=(2\pi)^{-d}\Re\left(\int\_{\mathbb{R}^{d}}e^{\langle\mathbf{K}^{(\nu)}-\mathrm{i}\mathbf{w},\mathbf{m}\rangle}\mathbb{E}\_{f\_{\mathbf{X}}}\left[e^{\mathrm{i}\left\langle\mathbf{w}+\mathrm{i}\mathbf{K}^{(\nu)},\mathbf{X}\right\rangle}\right]{\widehat{\ell}^{(\nu)}}(\mathbf{w}+\mathrm{i}\mathbf{K}^{(\nu)})\mathrm{d}\mathbf{w}\right),\quad\mathbf{K}^{(\nu)}\in\delta\_{K}^{(\nu)}={\delta}\_{\ell}^{(\nu)}\cap\delta\_{X} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(2​π)−d​ℜ⁡(∫ℝde⟨𝐊(ν)−i​𝐰,𝐦⟩​Φ𝐗​(𝐰+i​𝐊(ν))​ℓ^(ν)​(𝐰+i​𝐊(ν))​d𝐰).\displaystyle=(2\pi)^{-d}\Re\left(\int\_{\mathbb{R}^{d}}e^{\langle\mathbf{K}^{(\nu)}-\mathrm{i}\mathbf{w},\mathbf{m}\rangle}\Phi\_{\mathbf{X}}(\mathbf{w+\mathrm{i}\mathbf{K}^{(\nu)}}){\widehat{\ell}^{(\nu)}}(\mathbf{w+\mathrm{i}\mathbf{K}^{(\nu)}})\mathrm{d}\mathbf{w}\right). |  |

The application of Fubini’s theorem is justified by Assumption [3.2](https://arxiv.org/html/2602.06424v1#S3.Ex2 "Assumption 3.2 (Admissible contour shifts). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

### E.2 Fourier transform of the given loss functions

This section presents the Fourier transforms of the component integrands, ℓk,p(ν)\ell^{(\nu)}\_{k,p} for the loss functions in Example [2.1](https://arxiv.org/html/2602.06424v1#S2.E1 "In Example 2.3. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), arising in the decomposition in Notation [3.5](https://arxiv.org/html/2602.06424v1#S3.Thmtheorem5 "Notation 3.5 (Component selection and componentwise integrands). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk").

##### Exponential loss function in ([2.2](https://arxiv.org/html/2602.06424v1#S2.E2 "In item (i) ‣ Example 2.3. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

For k∈{1,d}k\in\{1,d\} and 𝐩=(p1,…,pk)∈ℐk\mathbf{p}=(p\_{1},\dots,p\_{k})\in\mathcal{I}\_{k}, the loss component can be represented as
ℓk,p​(𝐱)=ck,p​exp⁡(β​ 1⊤​𝐱)\ell\_{k,p}(\mathbf{x})=c\_{k,p}\exp\!\big(\beta\,\mathbf{1}^{\top}\mathbf{x}\big)
with 𝐱∈ℝk\mathbf{x}\in\mathbb{R}^{k}, where the constants ck,pc\_{k,p} depend on the selected component.

Following the domain decomposition induced by the transformation in
Notation [3.5](https://arxiv.org/html/2602.06424v1#S3.Thmtheorem5 "Notation 3.5 (Component selection and componentwise integrands). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), we split the integral into
one-sided contributions and introduce componentwise damping parameters
Kk,p−,Kk,p+∈ℝkK^{-}\_{k,p},K^{+}\_{k,p}\in\mathbb{R}^{k} such that

|  |  |  |
| --- | --- | --- |
|  | Kk,p−<β<Kk,p+.K^{-}\_{k,p}<\beta<K^{+}\_{k,p}. |  |

Under this choice, the damped Fourier transform of ℓk,p\ell\_{k,p} is well defined
and given by

|  |  |  |
| --- | --- | --- |
|  | ℓ^k,p(0)​(u+i​Kk,p)=ck,p​∏j=1k(1Kk,p+−β−i​uj+1β−Kk,p−+i​uj),\widehat{\ell}^{(0)}\_{k,p}(u+iK\_{k,p})=c\_{k,p}\prod\_{j=1}^{k}\left(\frac{1}{K^{+}\_{k,p}-\beta-iu\_{j}}+\frac{1}{\beta-K^{-}\_{k,p}+iu\_{j}}\right), |  |

where Kk,pK\_{k,p} denotes the combined contour shift arising from the
positive and negative half-line contributions.
For its gradient and Hessian, letting 𝟏k:=(1,…,1)⊤∈ℝk\mathbf{1}\_{k}:=(1,\dots,1)^{\top}\in\mathbb{R}^{k},
we obtain

|  |  |  |
| --- | --- | --- |
|  | ℓ^k,p(1)​(𝐮+i​𝐊k,p)=β​ℓ^k,p(0)​(𝐮+i​𝐊k,p)​ 1k,ℓ^k,p(2)​(𝐮+i​𝐊k,p)=β2​ℓ^k,p(0)​(𝐮+i​𝐊k,p)​ 1k​𝟏k⊤.\widehat{\ell}^{(1)}\_{k,p}\left(\mathbf{u}+\mathrm{i}\mathbf{K}\_{k,p}\right)=\beta\,\widehat{\ell}^{(0)}\_{k,p}\left(\mathbf{u}+\mathrm{i}\mathbf{K}\_{k,p}\right)\,\mathbf{1}\_{k},\qquad\widehat{\ell}^{(2)}\_{k,p}\left(\mathbf{u}+\mathrm{i}\mathbf{K}\_{k,p}\right)=\beta^{2}\,\widehat{\ell}^{(0)}\_{k,p}\left(\mathbf{u}+\mathrm{i}\mathbf{K}\_{k,p}\right)\,\mathbf{1}\_{k}\mathbf{1}\_{k}^{\top}. |  |

##### QPC loss function in ([2.3](https://arxiv.org/html/2602.06424v1#S2.E3 "In item (ii) ‣ Example 2.3. ‣ 2 Optimization Framework for Multivariate Shortfall Risk ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

The linear component ℓ​(x)=x\ell(x)=x does not require a Fourier transform,
since its expectation and its derivatives can be computed directly under the law of the loss vector 𝐗\mathbf{X}.

Let θ∈{0,1,2}\theta\in\{0,1,2\} and define ϕθ​(x):=(xθ)+\phi\_{\theta}(x):=(x^{\theta})^{+}.
Fix a damping parameter K<0K<0 and set, for y∈ℝy\in\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | ϕ^θ​(y+i​K):=∫ℝe−i​y​x​eK​x​ϕθ​(x)​𝑑x=∫0∞e(K−i​y)​x​xθ​𝑑x=θ!(−K+i​y)θ+1.\widehat{\phi}\_{\theta}(y+iK):=\int\_{\mathbb{R}}e^{-iyx}e^{Kx}\phi\_{\theta}(x)\,dx=\int\_{0}^{\infty}e^{(K-iy)x}x^{\theta}\,dx=\frac{\theta!}{(-K+iy)^{\theta+1}}. |  |

Moreover, for ν∈{0,1,2}\nu\in\{0,1,2\} with ν≤θ\nu\leq\theta,

|  |  |  |  |
| --- | --- | --- | --- |
| (E.2) |  | ϕ^θ(ν)(y+iK):=∫ℝe−i​y​xeK​xϕθ(ν)(x)dx=θ!(−K+i​y)θ−ν+1.\widehat{\phi}^{(\nu)}\_{\theta}(y+iK):=\int\_{\mathbb{R}}e^{-iyx}e^{Kx}\phi^{(\nu)}\_{\theta}(x)\,dx=\frac{\theta!}{(-K+iy)^{\theta-\nu+1}}. |  |

For k∈{1,2}k\in\{1,2\} and 𝐩=(p1,…,pk)∈ℐk\mathbf{p}=(p\_{1},\dots,p\_{k})\in\mathcal{I}\_{k},
the loss components can be written as

|  |  |  |
| --- | --- | --- |
|  | ℓk,p​(𝐱k,p)=ck,p​∏j=1kϕa​(k)​(xpj),a​(1)=2,a​(2)=1,\ell\_{k,p}(\mathbf{x}\_{k,p})=c\_{k,p}\prod\_{j=1}^{k}\phi\_{a(k)}(x\_{p\_{j}}),\qquad a(1)=2,\quad a(2)=1, |  |

with

|  |  |  |
| --- | --- | --- |
|  | ck,p={12,k=1,α,k=2.c\_{k,p}=\begin{cases}\frac{1}{2},&k=1,\\[3.00003pt] \alpha,&k=2.\end{cases} |  |

Then, for ν∈{0,1,2}\nu\in\{0,1,2\} and damping vectors 𝐊k,p<0\mathbf{K}\_{k,p}<0,
the Fourier transform of ℓk,p(ν)\ell^{(\nu)}\_{k,p} is given by

|  |  |  |
| --- | --- | --- |
|  | ℓ^k,p(ν)​(𝐮+i​𝐊k,p)=ck,p​∏j=1kϕ^a​(k)(ν)​(uj+i​(𝐊k,p)j),\widehat{\ell}^{(\nu)}\_{k,p}(\mathbf{u}+i\mathbf{K}\_{k,p})=c\_{k,p}\prod\_{j=1}^{k}\widehat{\phi}^{(\nu)}\_{a(k)}\!\left(u\_{j}+i(\mathbf{K}\_{k,p})\_{j}\right), |  |

with ϕ^θ(ν)\widehat{\phi}^{(\nu)}\_{\theta} defined in ([E.2](https://arxiv.org/html/2602.06424v1#A5.E2 "In QPC loss function in (2.3). ‣ E.2 Fourier transform of the given loss functions ‣ Appendix E Fourier Representation of the MSRM problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk")).

### E.3 Loss vector distributions and extended characteristic functions

###### Example E.1 (Gaussian).

Let 𝐗∼𝒩d​(𝝁,𝚺)\mathbf{X}\sim\mathcal{N}\_{d}(\boldsymbol{\mu},\boldsymbol{\Sigma}) with
𝝁∈ℝd\boldsymbol{\mu}\in\mathbb{R}^{d} and symmetric positive definite
𝚺∈ℝd×d\boldsymbol{\Sigma}\in\mathbb{R}^{d\times d}. Then the marginal distribution of 𝐗k,p\mathbf{X}\_{k,p} is

|  |  |  |
| --- | --- | --- |
|  | 𝐗k,p∼𝒩k​(𝝁k,p,𝚺k,p),𝝁k,p=Pk,p​𝝁,𝚺k,p=Pk,p​𝚺​Pk,p⊤.\mathbf{X}\_{k,p}\sim\mathcal{N}\_{k}(\boldsymbol{\mu}\_{k,p},\boldsymbol{\Sigma}\_{k,p}),\qquad\boldsymbol{\mu}\_{k,p}=P\_{k,p}\boldsymbol{\mu},\quad\boldsymbol{\Sigma}\_{k,p}=P\_{k,p}\boldsymbol{\Sigma}P\_{k,p}^{\top}. |  |

where Pk,pP\_{k,p} is the coordinate selection matrix introduced in Notation [3.5](https://arxiv.org/html/2602.06424v1#S3.Thmtheorem5 "Notation 3.5 (Component selection and componentwise integrands). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"). The extended CF of 𝐗k,p\mathbf{X}\_{k,p} is, for any 𝐲∈ℂk\mathbf{y}\in\mathbb{C}^{k},

|  |  |  |
| --- | --- | --- |
|  | Φ𝐗k,p​(𝐲):=𝔼​[ei​⟨𝐲,𝐗k,p⟩]=exp⁡(i​𝐲⊤​𝝁k,p−12​𝐲⊤​𝚺k,p​𝐲),\Phi\_{\mathbf{X}\_{k,p}}({\mathbf{y}}):=\mathbb{E}\!\left[e^{\mathrm{i}\langle\mathbf{y},\mathbf{X}\_{k,p}\rangle}\right]=\exp\!\left(\mathrm{i}\,\mathbf{y}^{\top}\boldsymbol{\mu}\_{k,p}-\tfrac{1}{2}\,\mathbf{y}^{\top}\boldsymbol{\Sigma}\_{k,p}\mathbf{y}\right), |  |

in particular for 𝐲=𝐮+i​𝐊k,p\mathbf{y}=\mathbf{u}+\mathrm{i}\,\mathbf{K}\_{k,p} with 𝐮,𝐊k,p∈ℝk\mathbf{u},\mathbf{K}\_{k,p}\in\mathbb{R}^{k}.

###### Example E.2 (Normal Inverse Gaussian (NIG)).

Let 𝐗∼NIGd​(α,𝜷,δ,𝝁,𝚪)\mathbf{X}\sim\mathrm{NIG}\_{d}(\alpha,\boldsymbol{\beta},\delta,\boldsymbol{\mu},\boldsymbol{\Gamma}), i.e. 𝐗\mathbf{X} is the Generalized Hyperbolic distribution with
λ=−12\lambda=-\tfrac{1}{2}, α>0\alpha>0, δ>0\delta>0, 𝝁,𝜷∈ℝd\boldsymbol{\mu},\boldsymbol{\beta}\in\mathbb{R}^{d}, and 𝚪∈ℝd×d\boldsymbol{\Gamma}\in\mathbb{R}^{d\times d} symmetric positive definite [[25](https://arxiv.org/html/2602.06424v1#bib.bib17 "Tail Behaviour and Tail Dependence of Generalized Hyperbolic Distributions")], satisfying α2>𝜷⊤​𝚪​𝜷\alpha^{2}>\boldsymbol{\beta}^{\top}\boldsymbol{\Gamma}\boldsymbol{\beta}. From Notation [3.5](https://arxiv.org/html/2602.06424v1#S3.Thmtheorem5 "Notation 3.5 (Component selection and componentwise integrands). ‣ 3 Fourier Representations of the MSRM Problem ‣ Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk"), let 𝐩c:={1,…,d}∖𝐩\mathbf{p}^{c}:=\{1,\dots,d\}\setminus\mathbf{p} be the complement index list of 𝐩\mathbf{p}, ordered increasingly. Define the selection matrix for the complement Pd−k,pc∈ℝd−k×dP\_{d-k,p^{c}}\in\mathbb{R}^{{d-k}\times d}
. Let Πk,p∈ℝd×d\Pi\_{k,p}\in\mathbb{R}^{d\times d} be any permutation matrix that reorders coordinates so that
Πk,p:=[Pk,pPd−k,pc]\Pi\_{k,p}:=\begin{bmatrix}P\_{k,p}\\
P\_{d-k,p^{c}}\end{bmatrix}, and write the permuted parameters as,

|  |  |  |
| --- | --- | --- |
|  | Πk,p​𝝁=(𝝁1𝝁2),Πk,p​𝜷=(𝜷1𝜷2),Πk,p​𝚪​Πk,p⊤=(𝚪11𝚪12𝚪21𝚪22),𝚪11∈ℝk×k.\Pi\_{k,p}\boldsymbol{\mu}=\binom{\boldsymbol{\mu}\_{1}}{\boldsymbol{\mu}\_{2}},\qquad\Pi\_{k,p}\boldsymbol{\beta}=\binom{\boldsymbol{\beta}\_{1}}{\boldsymbol{\beta}\_{2}},\qquad\Pi\_{k,p}\boldsymbol{\Gamma}\Pi\_{k,p}^{\top}=\begin{pmatrix}\boldsymbol{\Gamma}\_{11}&\boldsymbol{\Gamma}\_{12}\\ \boldsymbol{\Gamma}\_{21}&\boldsymbol{\Gamma}\_{22}\end{pmatrix},\quad\boldsymbol{\Gamma}\_{11}\in\mathbb{R}^{k\times k}. |  |

Then, by [[25](https://arxiv.org/html/2602.06424v1#bib.bib17 "Tail Behaviour and Tail Dependence of Generalized Hyperbolic Distributions"), Theorem 1(a)] (applied with λ=−12\lambda=-\tfrac{1}{2}), the selected marginal 𝐗k,p\mathbf{X}\_{k,p} satisfies:

|  |  |  |
| --- | --- | --- |
|  | 𝐗k,p∼NIGk​(αk,p,𝜷k,p,δk,p,𝝁k,p,𝚪k,p),\mathbf{X}\_{k,p}\sim\mathrm{NIG}\_{k}\!\big(\alpha\_{k,p},\boldsymbol{\beta}\_{k,p},\delta\_{k,p},\boldsymbol{\mu}\_{k,p},\boldsymbol{\Gamma}\_{k,p}\big), |  |

with

|  |  |  |
| --- | --- | --- |
|  | 𝝁k,p=𝝁1,𝜷k,p=𝜷1+𝚪11−1​𝚪12​𝜷2,δk,p=det(𝚪11)1/2​δ,𝚪k,p=det(𝚪11)−1/k​𝚪11,\boldsymbol{\mu}\_{k,p}=\boldsymbol{\mu}\_{1},\qquad\boldsymbol{\beta}\_{k,p}=\boldsymbol{\beta}\_{1}+\boldsymbol{\Gamma}\_{11}^{-1}\boldsymbol{\Gamma}\_{12}\boldsymbol{\beta}\_{2},\qquad\delta\_{k,p}=\det(\boldsymbol{\Gamma}\_{11})^{1/2}\,\delta,\qquad\boldsymbol{\Gamma}\_{k,p}=\det(\boldsymbol{\Gamma}\_{11})^{-1/k}\,\boldsymbol{\Gamma}\_{11}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | αk,p=det(𝚪11)−1/(2​k)​α2−⟨𝜷2,(𝚪22−𝚪21​𝚪11−1​𝚪12)​𝜷2⟩.\alpha\_{k,p}=\det(\boldsymbol{\Gamma}\_{11})^{-1/(2k)}\sqrt{\alpha^{2}-\big\langle\boldsymbol{\beta}\_{2},\,(\boldsymbol{\Gamma}\_{22}-\boldsymbol{\Gamma}\_{21}\boldsymbol{\Gamma}\_{11}^{-1}\boldsymbol{\Gamma}\_{12})\,\boldsymbol{\beta}\_{2}\big\rangle}. |  |

The extended CF is, for any 𝐲∈ℂk\mathbf{y}\in\mathbb{C}^{k},

|  |  |  |
| --- | --- | --- |
|  | ϕ𝐗k,pNIG​(𝐲)=exp⁡(i​𝐲⊤​𝝁k,p+δk,p​(γk,p−αk,p2−(𝜷k,p+i​𝐲)⊤​𝚪k,p​(𝜷k,p+i​𝐲))),\phi^{\mathrm{NIG}}\_{\mathbf{X}\_{k,p}}(\mathbf{y})=\exp\!\left(\mathrm{i}\,\mathbf{y}^{\top}\boldsymbol{\mu}\_{k,p}+\delta\_{k,p}\Big(\gamma\_{k,p}-\sqrt{\alpha\_{k,p}^{2}-(\boldsymbol{\beta}\_{k,p}+\mathrm{i}\,\mathbf{y})^{\top}\boldsymbol{\Gamma}\_{k,p}(\boldsymbol{\beta}\_{k,p}+\mathrm{i}\,\mathbf{y})}\Big)\right), |  |

where γk,p=αk,p2−𝜷k,p⊤​𝚪k,p​𝜷k,p>0\gamma\_{k,p}=\sqrt{\alpha\_{k,p}^{2}-\boldsymbol{\beta}\_{k,p}^{\top}\boldsymbol{\Gamma}\_{k,p}\,\boldsymbol{\beta}\_{k,p}}>0. In particular, this applies to 𝐲=𝐮+i​𝐊k,p\mathbf{y}=\mathbf{u}+\mathrm{i}\,\mathbf{K}\_{k,p} with 𝐮,𝐊k,p∈ℝk\mathbf{u},\mathbf{K}\_{k,p}\in\mathbb{R}^{k}.