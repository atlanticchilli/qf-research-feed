---
authors:
- Yang Liu
- Yunran Wei
- Xintao Ye
doc_id: arxiv:2603.10327v2
family_id: arxiv:2603.10327
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization
  and Application'
url_abs: http://arxiv.org/abs/2603.10327v2
url_html: https://arxiv.org/html/2603.10327v2
venue: arXiv q-fin
version: 2
year: 2026
---


Yang Liu
School of Science and Engineering, The Chinese University of Hong Kong (Shenzhen), China. Email: yangliu16@cuhk.edu.cn
  
Yunran Wei
School of Mathematics and Statistics, Carleton University, Canada. Email: yunran.wei@carleton.ca
  
Xintao Ye
Corresponding Author. School of Mathematics, Shandong University, China. Email: xintaoye2@gmail.com

###### Abstract

Various financial market scenarios may cause heterogeneous risk assessments among analysts, which motivates the usage of the Generalized Risk Measure in Fadina et al. ([2024](#bib.bib15 "A framework for measures of risk under uncertainty")). Effectively synthesizing these diverse assessments avoids over-relying on a single, potentially flawed or conservative forecast and promotes more robust decision-making. Motivated by this, we establish analytical characterizations of the Weighted Generalized Risk Measure (WGRM) under both discrete and continuous settings. Building upon the WGRM, we incorporate the Fundamental Risk Quadrangle (FRQ) in Rockafellar and Uryasev ([2013](#bib.bib34 "The fundamental risk quadrangle in risk management, optimization and statistical estimation")) into the Weighted Risk Quadrangle (WRQ) and show that the intrinsic relationships among risk, deviation, regret, error, and statistics in FRQ are preserved under weighted aggregation across scenarios. Moreover, we demonstrate that certain complex risk optimization problems under the WGRM can be reformulated as tractable linear programs through the WRQ structure, thus ensuring computational feasibility. Finally, the WGRM and WRQ framework is applied to empirical analyses using constituents of the NASDAQ 100 and S&P 500 indices across recession and expansion regimes, which validates that WGRM-based portfolios exhibit superior risk-adjusted performance and enhanced downside resilience and effectively mitigate losses arising from erroneous single-scenario judgments.

Keywords: Financial Risk Management, Weighted Generalized Risk Measure, Weighted Risk Quadrangle, Portfolio Optimization, Empirical Validation.

Mathematics Subject Classification (2020): 91G70, 91G10

JEL Classification: D81, G32, G11

## 1 Introduction

### 1.1 Background and Motivation

The global financial crisis of 2008 revealed a fundamental weakness in modern risk management: risk assessments that appeared conservative in normal times proved fragile when market regimes shifted. Many highly rated financial institutions collapsed not solely due to excessive risk-taking, but because of an over-reliance on a single or a narrow set of scenarios and the unchecked confidence in singular probabilistic models. A key lesson from this episode is that financial risk is inherently scenario-dependent. In adverse markets, different analysts often arrive at different risk assessments—even when applying the same formal risk measure—since they rely on distinct data sources, data process techniques and stress scenarios. In such settings, the central question for a department manager is no longer whether a risk measure is conservative enough, but how to avoid the catastrophic losses that can result from trusting any single, potentially flawed analyst’s forecast in isolation (Cont et al., [2010](#bib.bib13 "Robustness and sensitivity analysis of risk measurement procedures"); Embrechts et al., [2015](#bib.bib14 "Aggregation-robustness and model uncertainty of regulatory risk measures")).

As a response, practitioners increasingly rely on consulting and combining heterogeneous scenario analyses. Consequently, the traditional risk measures—which are typically characterized as functionals operating either on random variable spaces or, given law-invariance, on the spaces comprising their distribution functions (see Artzner et al. [1999](#bib.bib3 "Coherent measures of risk"))—are no longer adequate. It is of significance and interest to switch from single-scenario traditional risk measures to multi-scenario settings; see Kou and Peng ([2016](#bib.bib26 "On the measurement of economic tail risk")); Wang and Ziegel ([2021](#bib.bib37 "Scenario-based risk evaluation")). A recent framework in Fadina et al. ([2024](#bib.bib15 "A framework for measures of risk under uncertainty")), the generalized risk measure (GRM), accepts two inputs: the loss variable XX along with a collection 𝒬\mathcal{Q} of admissible probability measures, which together provide a richer characterization of the underlying stochastic environment.

Under that framework, for an arbitrary measurable space (Ω,ℱ)(\Omega,\mathcal{F}), we denote by 𝒫\mathcal{P} the collection of all atomless probability measures on ℱ\mathcal{F} and, for simplicity, we assume it is a compact Polish space. Correspondingly, let 𝒳\mathcal{X} denote the set of all random variables defined on this space. The power set of 𝒫\mathcal{P} is denoted 2𝒫2^{\mathcal{P}}. The formal definition of GRM in Fadina et al. ([2024](#bib.bib15 "A framework for measures of risk under uncertainty")) is as follows.

###### Definition 1.

A generalized risk measure is a mapping Ψ\Psi: 𝒳×2𝒫→(−∞,∞)\mathcal{X}\times 2^{\mathcal{P}}\to(-\infty,\infty).

The worst-case, coherent, and robust GRMs are characterized via different sets of axioms in Fadina et al. ([2024](#bib.bib15 "A framework for measures of risk under uncertainty")), where the worst-case one might be too conservative. Actually, the weighted aggregation form is worthy of exploration as it fully incorporates different analysts’ expertise.
Motivated by this, we introduce the Weighted Generalized Risk Measure (WGRM), a principled framework designed to aggregate heterogeneous risk perspectives into a single, analytically tractable functional under both discrete and continuous settings to align with real-world risk management needs. Specifically, For any 𝒬⊆𝒫\mathcal{Q}\subseteq\mathcal{P}, we aim to find a probability measure μ𝒬\mu\_{\mathcal{Q}} that assigns weights to the elements of 𝒬\mathcal{Q}, satisfying μ𝒬​(∅)=0\mu\_{\mathcal{Q}}(\emptyset)=0 and μ𝒬​(𝒬)=1\mu\_{\mathcal{Q}}(\mathcal{Q})=1, along with 0⩽μ𝒬​(P)⩽10\leqslant\mu\_{\mathcal{Q}}(P)\leqslant 1 for all P∈𝒬P\in\mathcal{Q}. We formally define WGRM as follows.

###### Definition 2.

The mapping Ψ\Psi admits a weighted generalized risk measure (WGRM) representation if for every 𝒬⊆𝒫\mathcal{Q}\subseteq\mathcal{P},∃μ𝒬\,\exists\,\,\mu\_{\mathcal{Q}} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (continuous)Ψ​(X|𝒬)=∫𝒬Ψ​(X|P)​dμ𝒬​(P),X∈𝒳,𝒬∈2𝒫.\text{(continuous)}\quad\quad\Psi(X|\mathcal{Q})=\int\_{\mathcal{Q}}\Psi(X|P)\,\mathrm{d}\mu\_{\mathcal{Q}}(P),\quad X\in\mathcal{X},\ \mathcal{Q}\in 2^{\mathcal{P}}. |  | (1) |

If 𝒬\mathcal{Q} is a discrete set, then μ𝒬\mu\_{\mathcal{Q}} reduces to discrete measure and Ψ\Psi is equivalent as

|  |  |  |  |
| --- | --- | --- | --- |
|  | (discrete)Ψ​(X|𝒬)=∑P∈𝒬Ψ​(X|P)⋅μ𝒬​(P),X∈𝒳,𝒬∈2𝒫.\text{(discrete)}\quad\quad\Psi(X|\mathcal{Q})=\sum\_{P\in\mathcal{Q}}\Psi(X|P)\cdot\mu\_{\mathcal{Q}}(P),\quad X\in\mathcal{X},\ \mathcal{Q}\in 2^{\mathcal{P}}. |  | (2) |

Subsequently, building on the WGRM model, we further extend the Fundamental Risk Quadrangle (FRQ), which is a framework combining optimization and estimation in risk management proposed by Rockafellar and Uryasev ([2013](#bib.bib34 "The fundamental risk quadrangle in risk management, optimization and statistical estimation")). We use Figure [1](#S1.F1 "Figure 1 ‣ 1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") to briefly illustrate the FRQ with details postponed to Section [3](#S3 "3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"). By leveraging the weight structure derived from WGRM, we perform a weighted aggregation of the single-probability-measure risk quadrangle to develop the Weighted Risk Quadrangle (WRQ).

Risk ℛ\mathcal{R}Deviation 𝒟\mathcal{D}Regret 𝒱\mathcal{V}Error ℰ\mathcal{E}Statistic 𝒮\mathcal{S}OptimizationEstimation


Figure 1: Fundamental Risk Quadrangle in Rockafellar and Uryasev ([2013](#bib.bib34 "The fundamental risk quadrangle in risk management, optimization and statistical estimation")).

![Refer to caption](2603.10327v2/Flowchart.png)


Figure 2: A Schematic Procedure for Department Managers to Aggregate Heterogeneous Risk Assessments.

Before elaborating on the theoretical framework, Figure [2](#S1.F2 "Figure 2 ‣ 1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") presents a specific application. Consider a department manager allocating capital across assets based on the assessments from multiple risk analysts. Even when applying a common metric like ES0.95\text{ES}\_{0.95}, analysts typically report divergent estimates due to distinct modeling choices and stress scenarios. These differences reflect distinct subjective probability measures PP each analyst adopts, collectively forming a family of probability measures 𝒬\mathcal{Q}. Crucially, relying on a single analyst’s estimate may expose the portfolio to idiosyncratic model bias, but also not fully make use of others’ effort and expertise.
Thus, the WGRM framework serves as a structural defense to perform a weighted aggregation of the analysts’ heterogeneous assessments. The weights assigned to each analyst can be based on their historical prediction accuracy, professional competence, or other relevant criteria. Such process corresponds to assigning a weight μ𝒬​(P)\mu\_{\mathcal{Q}}(P) to each probability measure P∈𝒬P\in\mathcal{Q}.
The manager then aims to minimize the aggregated risk while ensuring a predefined level of expected return. Thus, the obtained risk measure by the WGRM can be used as the objective function, which is then integrated into the WRQ. By defining relevant constraints (e.g., expected return targets, position limits) and solving the optimization problem, the manager ultimately obtains a robust asset allocation strategy. By design, this WRQ-based portfolio is inherently resilient, dampening the adverse financial consequences that would arise from relying on an isolated, incorrect market outlook.

### 1.2 Connection to Other Frameworks and Contribution

Our study is directly inspired by and develops the GRM proposed in Fadina et al. ([2024](#bib.bib15 "A framework for measures of risk under uncertainty")), thus exhibiting substantial differences in both mathematical structure and methodology from traditional risk measures (e.g., Frittelli and Rosazza Gianin [2002](#bib.bib19 "Putting order in risk measures"); Föllmer and Schied [2002](#bib.bib17 "Convex measures of risk and trading constraints"); Föllmer2004; Wakker [2010](#bib.bib36 "Prospect theory: for risk and ambiguity"); Castagnoli et al. [2022](#bib.bib11 "Star-shaped risk measures")).
Nevertheless, Fadina et al. ([2024](#bib.bib15 "A framework for measures of risk under uncertainty")) primarily discuss the worst-case GRM, which can be regarded as a special case of the WGRM in this paper under certain regularity conditions. This generality gives rise to disparities in mathematical treatments. Conceptually, our framework requires to accommodate information within each probability measure, whereas the worst-case one relies more on extreme scenarios; see also Gilboa and Schmeidler ([1989](#bib.bib20 "Maxmin expected utility with a non-unique prior")); Zhu and Fukushima ([2009](#bib.bib39 "Worst-case conditional value-at-risk with application to robust portfolio management")); Zymler et al. ([2013](#bib.bib40 "Worst-case value at risk of nonlinear portfolios")); Adrian and Brunnermeier ([2016](#bib.bib1 "CoVaR")); Liu and Wang ([2021](#bib.bib29 "A theory for measures of tail risk")); Chen et al. ([2022](#bib.bib12 "Ordering and inequalities of mixtures on risk aggregation")); Blanchet et al. ([2025](#bib.bib9 "Convolution bounds on quantile aggregation")).

While another analogous framework also accounting for multiple scenarios is the scenario-based risk measure in Wang and Ziegel ([2021](#bib.bib37 "Scenario-based risk evaluation")), they are fundamentally distinct in nature. Specifically, their framework, under the assumption of mutually singular probability measures, emphasizes model uncertainty other than heterogeneous assessments, whereas our framework focuses on the weight structure, particularly on how convex weights are derived. This critical difference leads to distinct methodological treatments, resulting in no overlap in research scopes or analytical approaches.
Other similar weighted aggregation frameworks appear in Klibanoff et al. ([2005](#bib.bib24 "A smooth model of decision making under uncertainty")); Brutti Righi ([2018](#bib.bib32 "A theory for combinations of risk measures")); Jokhadze and Schmidt ([2020](#bib.bib22 "Measuring model risk in financial risk management and pricing")); however, these works lack a systematic theoretical characterization of the weight structure itself.

For recent advances in risk measure theory, we refer to Bellini and Bernardino ([2017](#bib.bib7 "Risk management with expectiles")); Wang and Zitikis ([2021](#bib.bib38 "An axiomatic foundation for the expected shortfall")); Fissler and Pesenti ([2023](#bib.bib16 "Sensitivity measures based on scoring functions")); Bernard et al. ([2024](#bib.bib8 "Robust distortion risk measures")); La Torre and Rocca ([2024](#bib.bib28 "Distributionally robust multiobjective optimization with application to risk measure theory")); Gomez et al. ([2024](#bib.bib21 "Multi-period portfolio selection with interval-based conditional Value-at-Risk")); Battiston and Rimella ([2025](#bib.bib4 "Disclosure risk assessment with bayesian non-parametric hierarchical modelling")); Cai et al. ([2025](#bib.bib10 "Distributionally robust optimization under distorted expectations")). Our goal is to provide a comprehensive discussion of the weight structure inherent to the GRM framework; as such, this work may enable further synergistic integration with the aforementioned strands of research, laying groundwork for more comprehensive and context-aware risk management paradigms.

The contributions of this paper include the following aspects. Our primary contribution is that, building upon the foundational work of Kou et al. ([2013](#bib.bib25 "External risk measures and basel accords")); Kou and Peng ([2016](#bib.bib26 "On the measurement of economic tail risk")), Section [2](#S2 "2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") establishes analytical characterization of the WGRM framework under both discrete and continuous scenario settings. This dual formulation accommodates the diverse analytical demands of real-world risk management applications. This work represents a crucial deepening of the GRM theory, complementing the worst-case structure that the GRM initially focuses on. Furthermore, we analyze the specific conditions under which the aggregation weights can be uniquely determined. By focusing on the weighting structure itself, the WGRM achieves broad generality, seamlessly adapting to the heterogeneous individual risk measures utilized in the aggregation process.

It must be emphasized that the weighted aggregation of separate risk assessments is distinct from evaluating a single risk measure under a pre-aggregated probability distribution. The latter excessively smooths inherent risk volatility, an information loss that adjusting quantile parameters or other ad hoc modifications cannot adequately offset.

Our second key contribution, detailed in Section [3](#S3 "3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"), is to introduce the WRQ by extending the FRQ via the proposed WGRM weighting structure. This extension provides an integrated framework that theoretically unifies risk management, optimization, and statistical estimation in multi-scenario settings. While existing literature typically enhances FRQ by aggregating single-measure components with varying parameters, as noted earlier, heterogeneity across distinct scenarios and probability measures remains a more critical dimension to address for practical risk management.
WRQ inherently integrates risk management and portfolio optimization in a cohesive, theoretically consistent manner. Accordingly, in Section [4](#S4 "4 Optimization under WGRM and WRQ ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"), we elaborate on the embedded optimization problems within WRQ, as well as how to transform complex risk-minimization problems using WRQ’s components.

Finally, an empirical validation is provided in Section [5](#S5 "5 Empirical Study ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"), where we use NASDAQ 100 and S&P 500 data to compare portfolio performance with and without WGRM (and WRQ) across expansion and recession regimes, and conduct sensitivity analyses. Our results validate that WGRM-based portfolios exhibit superior risk-adjusted performance and pronounced downside resilience, effectively mitigating adverse consequences caused by isolated, erroneous market judgments.

## 2 Weighted Generalized Risk Measures

### 2.1 Properties and Technical Discussions

In this section, we examine the conditions under which the WGRM representation exists. To begin with, we recall several properties of a GRM Ψ\Psi: 𝒳×2𝒫→(−∞,∞)\mathcal{X}\times 2^{\mathcal{P}}\to(-\infty,\infty) from Fadina et al. ([2024](#bib.bib15 "A framework for measures of risk under uncertainty")) to facilitate a preliminary comparison between the worst-case GRM and WGRM.

The measure is called standard if Ψ​(s|𝒬)=s,∀s∈ℝ​and​𝒬⊆𝒫\Psi(s|\mathcal{Q})=s,\,\forall s\in\mathbb{R}\,\text{and}\,\mathcal{Q}\subseteq\mathcal{P}. When it is a single scenario case, the measure takes the form of Ψ\Psi: 𝒳×𝒫→(−∞,∞)\mathcal{X}\times\mathcal{P}\to(-\infty,\infty). Clearly, the explicit inclusion of 𝒬\mathcal{Q} as an input generalizes traditional risk measures. When 𝒬\mathcal{Q} is restricted to a singleton set (i.e., 𝒬={P}\mathcal{Q}=\{P\} for some P∈𝒫P\in\mathcal{P}), this generalized risk measure reduces to its traditional counterpart. The worst-case GRM satisfies the following properties.

(A1) Scenario monotonicity: if Ψ​(X|P)⩽Ψ​(Y|P)\Psi(X|P)\leqslant\Psi(Y|P) holds for every P∈𝒬P\in\mathcal{Q}, then Ψ​(X|𝒬)⩽Ψ​(Y|𝒬)\Psi(X|\mathcal{Q})\leqslant\Psi(Y|\mathcal{Q}).

(A2) Scenario upper bound: Ψ​(X|𝒬)⩽supP∈𝒬Ψ​(X|P)\Psi(X|\mathcal{Q})\leqslant\sup\_{P\in\mathcal{Q}}\Psi(X|P) holds for every X∈𝒳X\in\mathcal{X} and 𝒬⊆𝒫\mathcal{Q}\subseteq\mathcal{P}.

(A3) Uncertainty aversion: Ψ​(X|𝒬)⩽Ψ​(X|ℛ)\Psi(X|\mathcal{Q})\leqslant\Psi(X|\mathcal{R}) for every X∈𝒳X\in\mathcal{X} and 𝒬⊆ℛ⊆𝒫\mathcal{Q}\subseteq\mathcal{R}\subseteq\mathcal{P}.

For a WGRM Ψ\Psi, properties (A1) and (A2) are intuitively justified. Property (A1) holds due to the monotonicity of the integral: Ψ​(X|𝒬)=∫𝒬Ψ​(X|P)​dμ𝒬​(P)⩽∫𝒬Ψ​(Y|P)​dμ𝒬​(P)=Ψ​(Y|𝒬)\Psi(X|\mathcal{Q})=\int\_{\mathcal{Q}}\Psi(X|P)\,\mathrm{d}\mu\_{\mathcal{Q}}(P)\leqslant\int\_{\mathcal{Q}}\Psi(Y|P)\,\mathrm{d}\mu\_{\mathcal{Q}}(P)=\Psi(Y|\mathcal{Q}).
And property (A2) is derived from Ψ​(X|𝒬)⩽supP∗∈𝒬Ψ​(X|P∗)​∫𝒬dμ𝒬​(P)=supP∗∈𝒬Ψ​(X|P∗)⋅μ𝒬​(𝒬)=supP∗∈𝒬Ψ​(X|P∗)\Psi(X|\mathcal{Q})\leqslant\displaystyle\sup\_{P^{\*}\in\mathcal{Q}}\Psi(X|P^{\*})\int\_{\mathcal{Q}}\,\mathrm{d}\mu\_{\mathcal{Q}}(P)=\sup\_{P^{\*}\in\mathcal{Q}}\Psi(X|P^{\*})\cdot\mu\_{\mathcal{Q}}(\mathcal{Q})=\sup\_{P^{\*}\in\mathcal{Q}}\Psi(X|P^{\*}).

However, property (A3) is rarely satisfied by most of WGRMs but aligns more closely with the worst-case one. The defining characteristic of (A3) is that risk evaluation is monotonically non-decreasing with respect to expanding the scenario set. This monotonicity may induce excessive conservatism in risk assessment. Intuitively, if posterior scenarios incorporate more favorable states, the aggregate risk measure should exhibit a non-increasing trend rather than a non-decreasing one. This is why the characterization of the WGRM is worth being investigated.

###### Remark 1.

While the codomain of Ψ\Psi is formally defined as (−∞,∞)(-\infty,\infty), alternative specifications such as [−∞,∞][-\infty,\infty] or (−∞,∞](-\infty,\infty] are both theoretically admissible. However, from a practical standpoint, risk measures with finite values are generally more interpretable and operationally meaningful in financial applications.

###### Remark 2.

We require that 𝒫\mathcal{P} is a compact Polish space, which is a simplified technical assumption made for clarity of exposition. The collection 𝒫\mathcal{P} of all atomless probability measures on (Ω,ℱ)(\Omega,\mathcal{F}) can be endowed with topologies (e.g., the topology of weak convergence, provided that (Ω,ℱ)(\Omega,\mathcal{F}) supports a metric making it a Polish space) under which it forms a Polish space. However, 𝒫\mathcal{P} itself is generally not compact in these natural topologies. For instance, consider Ω=ℝ\Omega=\mathbb{R} with the Borel σ\sigma-algebra. The sequence of atomless measures {Pn}\{P\_{n}\}, where PnP\_{n} is the uniform distribution on the interval [n,n+1][n,n+1], typically lacks a convergent subsequence within 𝒫\mathcal{P} under weak convergence; the probability mass escapes to infinity. Nevertheless, we can always restrict attention to a suitable compact subset 𝒫~⊆𝒫\widetilde{\mathcal{P}}\subseteq\mathcal{P} containing the relevant scenario sets 𝒬\mathcal{Q} under consideration. Examples include families of atomless measures defined by bounded likelihood ratios with respect to a reference atomless measure (e.g., {P∈𝒫:|d​P/d​P0|⩽M}\{P\in\mathcal{P}:|\mathrm{d}P/\mathrm{d}P\_{0}|\leqslant M\} for some M<∞M<\infty and P0∈𝒫P\_{0}\in\mathcal{P}) or parametric families of atomless measures (e.g., {Pθ∈Θ}\{P\_{\theta}\in\Theta\} with compact parameter spaces Θ\Theta).

Critically, since 𝒬\mathcal{Q} is an arbitrary subset of 𝒫\mathcal{P} which may be either discrete or continuous, these two cases exhibit different mathematical structures and must be discussed separately. We first examine the case where 𝒬\mathcal{Q} is discrete.

### 2.2 WGRM under a Discrete Setting

In the discrete case where 𝒬\mathcal{Q} is finite, e.g., of size nn, our focus is on the Euclidean space ℝn\mathbb{R}^{n}. For notational simplicity, we present μ𝒬\mu\_{\mathcal{Q}} as a vector, i.e., μ𝒬=(μ1,…,μn)T∈ℝn\mu\_{\mathcal{Q}}=(\mu\_{1},\dots,\mu\_{n})^{T}\in\mathbb{R}^{n}.
Let 𝒞:={𝐱=(x1,x2,…,xn)∈ℝn∣x1⩽x2⩽⋯⩽xn}\mathcal{C}:=\{\mathbf{x}=(x\_{1},x\_{2},\dots,x\_{n})\in\mathbb{R}^{n}\mid x\_{1}\leqslant x\_{2}\leqslant\dots\leqslant x\_{n}\}, which is a translation-invariant and closed convex cone. And denote by int​𝒞:={𝐱∈ℝn∣x1<x2<⋯<xn}\text{int}\mathcal{C}:=\{\mathbf{x}\in\mathbb{R}^{n}\mid x\_{1}<x\_{2}<\dots<x\_{n}\} the interior of 𝒞\mathcal{C}.
Let 𝒟:={𝐱∈ℝn∣∑i=1nxi=1,xi⩾0,i=1,2,…,n}\mathcal{D}:=\{\mathbf{x}\in\mathbb{R}^{n}\mid\sum\_{i=1}^{n}x\_{i}=1,x\_{i}\geqslant 0,i=1,2,\dots,n\} be the whole weight set in ℝn\mathbb{R}^{n}. Let ⟨⋅,⋅⟩\left\langle\cdot,\cdot\right\rangle denote the inner product on ℝn\mathbb{R}^{n}. For a function f:ℝn→ℝf:\mathbb{R}^{n}\to\mathbb{R}, we define its domain as dom​f:={𝐱∈ℝn∣f​(𝐱)<∞}\text{dom}\,f:=\{\mathbf{x}\in\mathbb{R}^{n}\mid f(\mathbf{x})<\infty\} and ff is said to be proper if dom​f≠∅\text{dom}f\neq\emptyset.

When 𝒬\mathcal{Q} is finite, we can index its elements as 𝒬={Pi}i=1n\mathcal{Q}=\{P\_{i}\}\_{i=1}^{n}.
Generally, the GRM Ψ​(X|𝒬)\Psi(X|\mathcal{Q}) can be constructed through an aggregation function f:ℝn→ℝf:\mathbb{R}^{n}\to\mathbb{R} that combines all individual risk measures under each Pi∈𝒬P\_{i}\in\mathcal{Q}, i.e.,

|  |  |  |
| --- | --- | --- |
|  | Ψ​(X|𝒬)=f​(Ψ​(X|P1),Ψ​(X|P2),…,Ψ​(X|Pn)).\displaystyle\Psi(X|\mathcal{Q})=f(\Psi(X|P\_{1}),\Psi(X|P\_{2}),\dots,\Psi(X|P\_{n})). |  |

For simplicity, we define Φ𝒬,X=(Ψ​(X|P1),Ψ​(X|P2),…,Ψ​(X|Pn))T∈ℝn\Phi\_{\mathcal{Q},X}=(\Psi(X|P\_{1}),\Psi(X|P\_{2}),\dots,\Psi(X|P\_{n}))^{T}\in\mathbb{R}^{n}. Thus, the above can be expressed as Ψ​(X|𝒬)=f​(Φ𝒬,X)\Psi(X|\mathcal{Q})=f(\Phi\_{\mathcal{Q},X}).
To be a satisfactory aggregation function, ff is expected to satisfy several properties (Kou et al., [2013](#bib.bib25 "External risk measures and basel accords"); Kou and Peng, [2016](#bib.bib26 "On the measurement of economic tail risk")):

(B1) Positive homogeneity and translation invariance:
f​(a​Φ𝒬,X+b​𝟏)=a​f​(Φ𝒬,X)+b,∀Φ𝒬,X∈ℝn,a⩾0,b∈ℝf(a\Phi\_{\mathcal{Q},X}+b\mathbf{1})=af(\Phi\_{\mathcal{Q},X})+b,\forall\,\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n},a\geqslant 0,b\in\mathbb{R}. Here, 𝟏=(1,1,…,1)T∈ℝn\mathbf{1}=(1,1,\dots,1)^{T}\in\mathbb{R}^{n}.

(B2) Monotonicity:
f​(Φ𝒬,X)⩽f​(Φ𝒬,Y)f(\Phi\_{\mathcal{Q},X})\leqslant f(\Phi\_{\mathcal{Q},Y}), if Φ𝒬,X⩽Φ𝒬,Y\Phi\_{\mathcal{Q},X}\leqslant\Phi\_{\mathcal{Q},Y}, where Φ𝒬,X⩽Φ𝒬,Y\Phi\_{\mathcal{Q},X}\leqslant\Phi\_{\mathcal{Q},Y} is understood component-wise, i.e., Ψ​(X|Pi)⩽Ψ​(Y|Pi)\Psi(X|P\_{i})\leqslant\Psi(Y|P\_{i}), for all i=1,2,…,ni=1,2,\dots,n.

(B3) Comonotonic sub-additivity:
f​(Φ𝒬,X+Φ𝒬,Y)⩽f​(Φ𝒬,X)+f​(Φ𝒬,Y)f(\Phi\_{\mathcal{Q},X}+\Phi\_{\mathcal{Q},Y})\leqslant f(\Phi\_{\mathcal{Q},X})+f(\Phi\_{\mathcal{Q},Y}) whenever Φ𝒬,X\Phi\_{\mathcal{Q},X} and Φ𝒬,Y\Phi\_{\mathcal{Q},Y} are comonotonic, i.e., (Ψ​(X|Pi)−Ψ​(X|Pj))​(Ψ​(Y|Pi)−Ψ​(Y|Pj))⩾0(\Psi(X|P\_{i})-\Psi(X|P\_{j}))(\Psi(Y|P\_{i})-\Psi(Y|P\_{j}))\geqslant 0 for any i,j∈{1,2,…,n}i,j\in\{1,2,\dots,n\}.

(B4) Permutation invariance: f​(Φ𝒬,X)=f​(Φ𝒬,Xπ)f(\Phi\_{\mathcal{Q},X})=f(\Phi\_{\mathcal{Q},X}^{\pi}) for every π∈Sn\pi\in S\_{n}, where SnS\_{n} is the set of all permutations of {1,2,…,n}\{1,2,\dots,n\} and Φ𝒬,Xπ=(Ψ​(X|Pπ​(1)),Ψ​(X|Pπ​(2)),…,Ψ​(X|Pπ​(n)))T\Phi\_{\mathcal{Q},X}^{\pi}=(\Psi(X|P\_{\pi(1)}),\Psi(X|P\_{\pi(2)}),\dots,\Psi(X|P\_{\pi(n)}))^{T} is therefore the corresponding permuted vector.

(B1) indicates that ff is robust to affine transformation.
(B2) is equivalent to (A1) scenario monotonicity. A direct observation is that, under (B1) and (B2), ff is Lipschitz continuous with respect to the maximum-norm ∥⋅∥∞\|\cdot\|\_{\infty}, ensuring stability under small perturbations of risk inputs.
(B3) is also a common assumption which focuses on the co-movement consistency across two risk inputs.
(B4), though less frequently stated in literature, is intuitive for risk aggregation, as the overall risk measure should be invariant to the ordering of individual evaluations.

###### Remark 3.

One might argue that (B1) should be f​(a​Φ𝒬,X+b​𝟏)=a​f​(Φ𝒬,X)+s⋅bf(a\Phi\_{\mathcal{Q},X}+b\mathbf{1})=af(\Phi\_{\mathcal{Q},X})+s\cdot b, where ss is a fixed constant related to each aggregation function ff. However, since here ff is designed for weighted-averaging individual risk measures, it is reasonable to impose the invariance of aggregating constant values, i.e., s=1s=1.

The assumption of (B3) comonotonic sub-additivity holds practical relevance in real-world data contexts. For instance, if each component Ψ​(X|Pi)\Psi(X|P\_{i}) of Φ𝒬,X\Phi\_{\mathcal{Q},X} represents an individual risk measure under a specific market scenario, the risk measures of correlated assets across a family of coherent scenarios often exhibit comonotonicity. Nevertheless, the comonotonicity constraint is not sufficiently elegant for a general risk structure. If we instead require the aggregation function ff to satisfy full sub-additivity (unrestricted to comonotonic vectors), it will impose more stringent conditions on the resulting weights. Formally, we write

(B3’) Full sub-additivity:
f​(Φ𝒬,X+Φ𝒬,Y)⩽f​(Φ𝒬,X)+f​(Φ𝒬,Y)f(\Phi\_{\mathcal{Q},X}+\Phi\_{\mathcal{Q},Y})\leqslant f(\Phi\_{\mathcal{Q},X})+f(\Phi\_{\mathcal{Q},Y}) for any Φ𝒬,X,Φ𝒬,Y∈ℝn\Phi\_{\mathcal{Q},X},\Phi\_{\mathcal{Q},Y}\in\mathbb{R}^{n}.

We first propose the following characterization result on worst-case WGRM, where we technically get inspired from Ahmed et al. ([2008](#bib.bib2 "A note on natural risk statistics")).

###### Theorem 1.

(1) The aggregation function f:ℝn→ℝf:\mathbb{R}^{n}\to\mathbb{R} satisfies (B1)-(B4) if and only if there exists a closed convex set of weights 𝒲1⊆𝒟⊆ℝn\mathcal{W}\_{1}\subseteq\mathcal{D}\subseteq\mathbb{R}^{n}, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(Φ𝒬,X)=supμ𝒬∈𝒲1⟨μ𝒬,Φ𝒬,Xq⟩,∀Φ𝒬,X∈ℝn,\displaystyle f(\Phi\_{\mathcal{Q},X})=\sup\limits\_{\mu\_{\mathcal{Q}}\in\mathcal{W}\_{1}}\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}^{q}\right\rangle,\quad\forall\,\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}, |  | (3) |

where Φ𝒬,Xq:=(Ψ​(X|P(1)),Ψ​(X|P(2)),…,Ψ​(X|P(n)))T\Phi\_{\mathcal{Q},X}^{q}:=\big(\Psi(X|P\_{(1)}),\Psi(X|P\_{(2)}),\dots,\Psi(X|P\_{(n)})\big)^{T} is the vector of order statistics obtained by sorting the individual risk assessments {Ψ​(X|Pi)}i=1n\{\Psi(X|P\_{i})\}\_{i=1}^{n} into non-decreasing order.

(2) The aggregation function f:ℝn→ℝf:\mathbb{R}^{n}\to\mathbb{R} satisfies (B1), (B2), (B3’) and (B4) if and only if there exists a closed convex set of weights 𝒲2⊆𝒟∩𝒞⊆ℝn\mathcal{W}\_{2}\subseteq\mathcal{D}\cap\mathcal{C}\subseteq\mathbb{R}^{n}, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(Φ𝒬,X)=supμ𝒬∈𝒲2⟨μ𝒬,Φ𝒬,Xq⟩,∀Φ𝒬,X∈ℝn.\displaystyle f(\Phi\_{\mathcal{Q},X})=\sup\limits\_{\mu\_{\mathcal{Q}}\in\mathcal{W}\_{2}}\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}^{q}\right\rangle,\quad\forall\,\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}. |  | (4) |

###### Remark 4.

The key distinction between Parts (1) and (2) in Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 2.2 WGRM under a Discrete Setting ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") lies in the origin of convexity. Under full sub-additivity, the aggregation function ff inherently possesses convexity, whereas under comonotonic sub-additivity, convexity is induced by restricting the domain to 𝒞\mathcal{C} due to δ(⋅|𝒞)\delta(\cdot|\mathcal{C}). Specifically, considering the setting in Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 2.2 WGRM under a Discrete Setting ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"), for any Φ𝒬,Xq∈int​𝒞\Phi\_{\mathcal{Q},X}^{q}\in\text{int}\mathcal{C} with components Ψ​(X|P1)<Ψ​(X|P2)<⋯<Ψ​(X|Pn)\Psi(X|P\_{1})<\Psi(X|P\_{2})<\dots<\Psi(X|P\_{n}), the closed and convex nature of 𝒲1\mathcal{W}\_{1} guarantees the existence of a weight vector μ1∈𝒲1\mu\_{1}\in\mathcal{W}\_{1} that achieves the supremum of f​(Φ𝒬,Xq)f(\Phi\_{\mathcal{Q},X}^{q}). If we suppose μ1\mu\_{1} is not non-decreasing, then there exist indices 1⩽j<k⩽n1\leqslant j<k\leqslant n such that μ1​j>μ1​k\mu\_{1j}>\mu\_{1k}. Define μ2\mu\_{2} as the weight vector obtained by swapping the jj-th and kk-th components of μ1\mu\_{1}. Clearly, μ2\mu\_{2} still belongs to 𝒟\mathcal{D}. However, direct calculation yields

|  |  |  |
| --- | --- | --- |
|  | ⟨μ2,Φ𝒬,Xq⟩−⟨μ1,Φ𝒬,Xq⟩=(μ1​k−μ1​j)​Ψ​(X|Pj)+(μ1​j−μ1​k)​Ψ​(X|Pk)=(μ1​k−μ1​j)​(Ψ​(X|Pj)−Ψ​(X|Pk))>0.\left\langle\mu\_{2},\Phi\_{\mathcal{Q},X}^{q}\right\rangle-\left\langle\mu\_{1},\Phi\_{\mathcal{Q},X}^{q}\right\rangle=(\mu\_{1k}-\mu\_{1j})\Psi(X|P\_{j})+(\mu\_{1j}-\mu\_{1k})\Psi(X|P\_{k})=(\mu\_{1k}-\mu\_{1j})(\Psi(X|P\_{j})-\Psi(X|P\_{k}))>0. |  |

This implies ⟨μ2,Φ𝒬,Xq⟩>⟨μ1,Φ𝒬,Xq⟩=f​(Φ𝒬,Xq)\left\langle\mu\_{2},\Phi\_{\mathcal{Q},X}^{q}\right\rangle>\left\langle\mu\_{1},\Phi\_{\mathcal{Q},X}^{q}\right\rangle=f(\Phi\_{\mathcal{Q},X}^{q}), which contradicts the definition of μ1\mu\_{1} as the supremum-achieving weight. Nevertheless, this contradiction does not directly indicate that μ1∈𝒞\mu\_{1}\in\mathcal{C}, since the swapped vector μ2\mu\_{2} may not belong to 𝒲1\mathcal{W}\_{1} in the first place.

The above theorem provides a formal representation of Ψ​(X|𝒬)\Psi(X|\mathcal{Q}) via a linear weighting of individual risk assessments Ψ​(X|Pi)\Psi(X|P\_{i}). However, it should be noted that the weighting vectors μ𝒬\mu\_{\mathcal{Q}} in this representation are not uniquely determined. More precisely, the weights depend functionally on the input risk vector Φ𝒬,X\Phi\_{\mathcal{Q},X}, exhibiting variability as Φ𝒬,X\Phi\_{\mathcal{Q},X} changes. While this theoretical formulation possesses mathematical elegance, the state-dependent nature of the weights may present practical implementation challenges. Consequently, we shall introduce additional structural constraints to enhance the stability and applicability of the weighting scheme.

(B6) Comonotonic additivity:
f​(Φ𝒬,X+Φ𝒬,Y)=f​(Φ𝒬,X)+f​(Φ𝒬,Y)f(\Phi\_{\mathcal{Q},X}+\Phi\_{\mathcal{Q},Y})=f(\Phi\_{\mathcal{Q},X})+f(\Phi\_{\mathcal{Q},Y}) whenever Φ𝒬,X\Phi\_{\mathcal{Q},X} and Φ𝒬,Y\Phi\_{\mathcal{Q},Y} are comonotonic, i.e., (Ψ​(X|Pi)−Ψ​(X|Pj))​(Ψ​(Y|Pi)−Ψ​(Y|Pj))⩾0(\Psi(X|P\_{i})-\Psi(X|P\_{j}))(\Psi(Y|P\_{i})-\Psi(Y|P\_{j}))\geqslant 0 for any i,j∈{1,2,…,n}i,j\in\{1,2,\dots,n\}.

(B6’) Full additivity:
f​(Φ𝒬,X+Φ𝒬,Y)=f​(Φ𝒬,X)+f​(Φ𝒬,Y)f(\Phi\_{\mathcal{Q},X}+\Phi\_{\mathcal{Q},Y})=f(\Phi\_{\mathcal{Q},X})+f(\Phi\_{\mathcal{Q},Y}) for any Φ𝒬,X,Φ𝒬,Y∈ℝn\Phi\_{\mathcal{Q},X},\Phi\_{\mathcal{Q},Y}\in\mathbb{R}^{n}.

(B6) transforms the (B3) comonotonic sub-additivity into comonotonic additivity and (B6’) transforms the (B3’) full sub-additivity into full additivity at the expense of weakening the convexity of the function. The rationality behind this transformation is that the sub-additivity should be represented in Ψ​(X|⋅)\Psi(X|\cdot) rather than in f​(⋅)f(\cdot) to avoid overemphasizing the diversification effects. In other words, this aligns with scenarios where hedging effects are primarily captured within the individual risk measures Ψ​(X|⋅)\Psi(X|\cdot) rather than the aggregation process. (B6) and (B6’) necessitate the linearity of f​(Φ𝒬,X)f(\Phi\_{\mathcal{Q},X}), which enables us to apply the Riesz Representation Theorem to attain unique weighting vectors μ𝒬∗\mu\_{\mathcal{Q}}^{\*}.

###### Proposition 1.

(1) The aggregation function f:𝒞→ℝf:\mathcal{C}\to\mathbb{R} satisfies (B1), (B2) and (B6) if and only if there exists a unique weighting vector μ𝒬∗∈𝒟\mu\_{\mathcal{Q}}^{\*}\in\mathcal{D}, such that

|  |  |  |
| --- | --- | --- |
|  | f​(Φ𝒬,X)=⟨μ𝒬∗,Φ𝒬,X⟩,∀Φ𝒬,X∈𝒞.\displaystyle f(\Phi\_{\mathcal{Q},X})=\left\langle\mu\_{\mathcal{Q}}^{\*},\Phi\_{\mathcal{Q},X}\right\rangle,\quad\forall\,\Phi\_{\mathcal{Q},X}\in\mathcal{C}. |  |

(2) The aggregation function f:ℝn→ℝf:\mathbb{R}^{n}\to\mathbb{R} satisfies (B1), (B2), (B4) and (B6) if and only if there exists a unique weighting vector μ𝒬∗∈𝒟\mu\_{\mathcal{Q}}^{\*}\in\mathcal{D}, such that

|  |  |  |
| --- | --- | --- |
|  | f​(Φ𝒬,X)=⟨μ𝒬∗,Φ𝒬,Xq⟩,∀Φ𝒬,X∈ℝn.\displaystyle f(\Phi\_{\mathcal{Q},X})=\left\langle\mu\_{\mathcal{Q}}^{\*},\Phi\_{\mathcal{Q},X}^{q}\right\rangle,\quad\forall\,\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}. |  |

(3) The aggregation function f:ℝn→ℝf:\mathbb{R}^{n}\to\mathbb{R} satisfies (B1), (B2) and (B6’) if and only if there exists a unique weighting vector μ𝒬∗∈𝒟\mu\_{\mathcal{Q}}^{\*}\in\mathcal{D}, such that

|  |  |  |
| --- | --- | --- |
|  | f​(Φ𝒬,X)=⟨μ𝒬∗,Φ𝒬,X⟩,∀Φ𝒬,X∈ℝn.\displaystyle f(\Phi\_{\mathcal{Q},X})=\left\langle\mu\_{\mathcal{Q}}^{\*},\Phi\_{\mathcal{Q},X}\right\rangle,\quad\forall\,\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}. |  |

(4) The aggregation function f:ℝn→ℝf:\mathbb{R}^{n}\to\mathbb{R} satisfies (B1), (B2), (B4) and (B6’) if and only if

|  |  |  |
| --- | --- | --- |
|  | f​(Φ𝒬,X)=⟨μ𝒬∗,Φ𝒬,X⟩,∀Φ𝒬,X∈ℝn,\displaystyle f(\Phi\_{\mathcal{Q},X})=\left\langle\mu\_{\mathcal{Q}}^{\*},\Phi\_{\mathcal{Q},X}\right\rangle,\quad\forall\,\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}, |  |

where μ𝒬∗=(1n,1n,…,1n)T∈ℝn\mu\_{\mathcal{Q}}^{\*}=(\frac{1}{n},\frac{1}{n},\dots,\frac{1}{n})^{T}\in\mathbb{R}^{n}.

### 2.3 WGRM under a Continuous Setting

The results for the discrete case cover a vast majority of practical applications. However, in situations where the number of distinct individual risk measures requiring aggregation is substantial, or the scenarios under consideration become exceedingly numerous, the elements in 𝒬\mathcal{Q} may proliferate toward infinity. In such asymptotic regimes, the existing framework is no longer adequate. Therefore, we are motivated to discuss the WGRM structure in the continuous case. Nevertheless, due to the significant differences between two settings, we begin by establishing the basic framework for the continuous version of WGRM.

In such setting, we assume 𝒬\mathcal{Q} to be a closed subset of 𝒫\mathcal{P}. Let μ0\mu\_{0} be a fixed atomless Borel probability reference measure on 𝒬\mathcal{Q}. By the isomorphism theorem for standard probability spaces, there exists a measure-preserving bijection τ:(𝒬,μ0)→([0,1],λ)\tau:(\mathcal{Q},\mu\_{0})\to([0,1],\lambda), where λ\lambda denotes the Lebesgue measure on [0,1][0,1]. This isomorphism allows us to transfer the analysis from the abstract space 𝒬\mathcal{Q} to a concrete interval [0,1][0,1]. Define the scenario risk functional φX:[0,1]→ℝ\varphi\_{X}:[0,1]\to\mathbb{R} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | φX​(t)=Ψ​(X∣τ−1​(t)),t∈[0,1],\displaystyle\varphi\_{X}(t)=\Psi(X\mid\tau^{-1}(t)),\quad t\in[0,1], |  | (5) |

which directly maps points in [0,1][0,1] to the corresponding single-scenario risk evaluations. The quantile function (or non-decreasing rearrangement) of φX\varphi\_{X} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | φXq(t)=inf{s∈ℝ∣λ(u∈[0,1]:φX(u)⩽s)⩾t},t∈[0,1].\displaystyle\varphi\_{X}^{q}(t)=\inf\{s\in\mathbb{R}\mid\lambda({u\in[0,1]:\varphi\_{X}(u)\leqslant s})\geqslant t\},\quad t\in[0,1]. |  | (6) |

Previously, in the discrete case, the finite number of scenarios ensures bounded risk vectors. However, in the continuous setting, to ensure the mathematical robustness of the aggregation function, we assume that the scenario risk functional remains bounded.
As a common practice, we consider the space L∞​([0,1])L^{\infty}([0,1]).
Consequently, the aggregation function ff is defined as a mapping f:L∞​([0,1])→ℝf:L^{\infty}([0,1])\to\mathbb{R}, satisfying Ψ​(X|𝒬)=f​(φX)\Psi(X|\mathcal{Q})=f(\varphi\_{X}). By restricting the domain to L∞​([0,1])L^{\infty}([0,1]), we avoid a pathological behavior such as non-integrability of the scenario risk functional φX\varphi\_{X}, thereby guaranteeing the existence and integrability of the quantile function. Note that if φX∈L∞​([0,1])\varphi\_{X}\in L^{\infty}([0,1]), then φXq∈L∞​([0,1])\varphi\_{X}^{q}\in L^{\infty}([0,1]) as well, with ‖φXq‖∞=‖φX‖∞\|\varphi\_{X}^{q}\|\_{\infty}=\|\varphi\_{X}\|\_{\infty}.

Also, the aggregation function ff is expected to satisfy the following properties under the continuous case. These properties are not totally different, but are the counterparts in a continuous context of (B1) to (B4).

(C1) Affine invariance: f​(a​φX+b​𝟏[0,1])=a​f​(φX)+bf(a\varphi\_{X}+b\mathbf{1}\_{[0,1]})=af(\varphi\_{X})+b, ∀φX∈L∞​([0,1])\forall\,\varphi\_{X}\in L^{\infty}([0,1]), a⩾0a\geqslant 0, b∈ℝb\in\mathbb{R}, where 𝟏[0,1]\mathbf{1}\_{[0,1]} is an indicator function over interval [0,1][0,1].

(C2) Pointwise monotonicity: f​(φX)⩽f​(φY)f(\varphi\_{X})\leqslant f(\varphi\_{Y}) if φX⩽φY\varphi\_{X}\leqslant\varphi\_{Y}. Here, φX⩽φY\varphi\_{X}\leqslant\varphi\_{Y} means φX​(t)⩽φY​(t)\varphi\_{X}(t)\leqslant\varphi\_{Y}(t) for almost every t∈[0,1]t\in[0,1].

(C3) Comonotonic sub-additivity: f​(φX+φY)⩽f​(φX)+f​(φY)f(\varphi\_{X}+\varphi\_{Y})\leqslant f(\varphi\_{X})+f(\varphi\_{Y}) whenever φX,φY\varphi\_{X},\varphi\_{Y} are comonotonic, i.e., (φX​(s)−φX​(t))​(φY​(s)−φY​(t))⩾0(\varphi\_{X}(s)-\varphi\_{X}(t))(\varphi\_{Y}(s)-\varphi\_{Y}(t))\geqslant 0 for almost every s,t∈[0,1]s,t\in[0,1].

(C4) Strong permutation invariance:
f​(φX)=f​(φX∘T)f(\varphi\_{X})=f(\varphi\_{X}\circ T) holds for any measure-preserving transformation T:[0,1]→[0,1]T:[0,1]\to[0,1] with respect to the Lebesgue measure λ\lambda, i.e., λ​(T−1​(A))=λ​(A)\lambda(T^{-1}(A))=\lambda(A) for any Lebesgue measurable set A⊆[0,1]A\subseteq[0,1].

Similar to the discrete case, we can also transform (C3) comonotonic sub-additivity into (C3’) full sub-additivity, which yields non-decreasing weighting measures as shown in the following result.

(C3’) Full sub-additivity: f​(φX+φY)⩽f​(φX)+f​(φY)f(\varphi\_{X}+\varphi\_{Y})\leqslant f(\varphi\_{X})+f(\varphi\_{Y}), for any φX,φY∈L∞​([0,1])\varphi\_{X},\varphi\_{Y}\in L^{\infty}([0,1]).

But unfortunately, relying solely on conditions (C1)-(C4) does not directly yield the infinite-dimensional extension of Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 2.2 WGRM under a Discrete Setting ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"). While these parallel properties ensure a reasonable behavior for standard risks, they fail to exclude pathological functionals known as Banach limits (purely finitely additive measures). Consequently, we propose introducing a non-trivial condition to filter out these pathological instances.

(C5) Fatou property: For any sequence {φXn}⊂L∞​([0,1])\{\varphi\_{X\_{n}}\}\subset L^{\infty}([0,1]) such that φXn→a.e.φX∈L∞​([0,1])\varphi\_{X\_{n}}\xrightarrow{a.e.}\varphi\_{X}\in L^{\infty}([0,1]), we have f​(φX)⩽lim infn→∞f​(φXn)f(\varphi\_{X})\leqslant\liminf\_{n\to\infty}f(\varphi\_{X\_{n}}).

In Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 2.3 WGRM under a Continuous Setting ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") below, condition (C5) is explicitly invoked in Part (1) but omitted in Part (2), since the Fatou property is automatically satisfied under the assumptions of Part (2) (see Theorem 2.2, Jouini et al. ([2006](#bib.bib23 "Law invariant risk measures have the fatou property"))). Based on these considerations, we formally state the following theorem.

###### Theorem 2.

(1) The aggregation function ff on L∞​([0,1])L^{\infty}([0,1]) satisfies (C1)-(C5) if and only if there exists a closed convex set of density 𝒲3⊆{ν∈L1​([0,1])∣∫01ν​(t)​dt=1,ν​(t)⩾0​a.e.}\mathcal{W}\_{3}\subseteq\{\nu\in L^{1}([0,1])\mid\int^{1}\_{0}\nu(t)\mathrm{d}t=1,\nu(t)\geqslant 0\ \text{a.e.}\} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψ​(X|𝒬)=f​(φX)=supν∈𝒲3∫01φXq​(t)​ν​(t)​dt,∀φX∈L∞​([0,1]).\displaystyle\Psi(X|\mathcal{Q})=f(\varphi\_{X})=\sup\limits\_{\nu\in\mathcal{W}\_{3}}\int\_{0}^{1}\varphi\_{X}^{q}(t)\nu(t)\mathrm{d}t,\quad\forall\,\varphi\_{X}\in L^{\infty}([0,1]). |  | (7) |

(2) The aggregation function ff on L∞​([0,1])L^{\infty}([0,1]) satisfies (C1), (C2), (C3’) and (C4) if and only if there exists a closed convex set of density 𝒲4⊆{ν∈L∞​([0,1])∣∫01ν​(t)​dt=1,ν​(t)⩾0​a.e.,ν​ is non-decreasing}\mathcal{W}\_{4}\subseteq\{\nu\in L^{\infty}([0,1])\mid\int^{1}\_{0}\nu(t)\mathrm{d}t=1,\nu(t)\geqslant 0\ \text{a.e.},\nu\text{ is non-decreasing}\} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψ​(X|𝒬)=f​(φX)=supν∈𝒲4∫01φXq​(t)​ν​(t)​dt,∀φX∈L∞​([0,1]).\displaystyle\Psi(X|\mathcal{Q})=f(\varphi\_{X})=\sup\limits\_{\nu\in\mathcal{W}\_{4}}\int\_{0}^{1}\varphi\_{X}^{q}(t)\nu(t)\mathrm{d}t,\quad\forall\,\varphi\_{X}\in L^{\infty}([0,1]). |  | (8) |

One may question the expressions in Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 2.3 WGRM under a Continuous Setting ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") differ from our original definition in Eq.([1](#S1.E1 "In Definition 2. ‣ 1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")). Despite formal differences, they are essentially equivalent. For any density function ν∈L1​([0,1])\nu\in L^{1}([0,1]) with ν⩾0\nu\geqslant 0 a.e. and ∫01ν​(t)​dt=1\int\_{0}^{1}\nu(t)\,\mathrm{d}t=1, we can define an absolutely continuous probability measure μν\mu\_{\nu} on [0,1][0,1] by

|  |  |  |
| --- | --- | --- |
|  | μν​(A)=∫Aν​(t)​dt,\displaystyle\mu\_{\nu}(A)=\int\_{A}\nu(t)\,\mathrm{d}t, |  |

for any Lebesgue measurable set A⊆[0,1].A\subseteq[0,1].
Conversely, by the Radon-Nikodym Theorem, for any probability measure μ𝒬\mu\_{\mathcal{Q}} on [0,1][0,1] satisfying μ𝒬≪λ\mu\_{\mathcal{Q}}\ll\lambda, where λ\lambda denotes the Lebesgue measure, there exists a unique (up to a.e. equivalence) density function νμ=d​μ𝒬d​λ∈L1​([0,1])\nu\_{\mu}=\frac{\mathrm{d}\mu\_{\mathcal{Q}}}{\mathrm{d}\lambda}\in L^{1}([0,1]) with νμ⩾0\nu\_{\mu}\geqslant 0 a.e. such that

|  |  |  |
| --- | --- | --- |
|  | μ𝒬​(A)=∫Aνμ​(t)​dt,\displaystyle\mu\_{\mathcal{Q}}(A)=\int\_{A}\nu\_{\mu}(t)\,\mathrm{d}t, |  |

for any Lebesgue measurable set A⊆[0,1].A\subseteq[0,1].
This establishes a bijective correspondence (up to a.e. equivalence) between non-negative density functions integrating to 11 and absolutely continuous probability measures on [0,1][0,1].
Now we define two sets of absolutely continuous probability measures:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒲~3\displaystyle\widetilde{\mathcal{W}}\_{3} | ={μ𝒬∈ℳ+​([0,1])∣μ𝒬≪λ,μ𝒬​([0,1])=1},\displaystyle=\left\{\mu\_{\mathcal{Q}}\in\mathcal{M}\_{+}([0,1])\,\mid\,\mu\_{\mathcal{Q}}\ll\lambda,\;\mu\_{\mathcal{Q}}([0,1])=1\right\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒲~4\displaystyle\widetilde{\mathcal{W}}\_{4} | ={μ𝒬∈ℳ+​([0,1])|μ𝒬≪λ,μ𝒬​([0,1])=1,d​μ𝒬d​λ​ is non-decreasing},\displaystyle=\left\{\mu\_{\mathcal{Q}}\in\mathcal{M}\_{+}([0,1])\,\middle|\,\mu\_{\mathcal{Q}}\ll\lambda,\;\mu\_{\mathcal{Q}}([0,1])=1,\;\frac{\mathrm{d}\mu\_{\mathcal{Q}}}{\mathrm{d}\lambda}\text{ is non-decreasing}\right\}, |  |

where ℳ+​([0,1])\mathcal{M}\_{+}([0,1]) denotes the space of non-negative finite measures on [0,1][0,1]. By the bijective correspondence established above, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | {ν∈L1​([0,1])|∫01ν​(t)​dt=1,ν​(t)⩾0​ a.e.}\displaystyle\left\{\nu\in L^{1}([0,1])\,\middle|\,\int\_{0}^{1}\nu(t)\,\mathrm{d}t=1,\;\nu(t)\geqslant 0\text{ a.e.}\right\} | ={d​μ𝒬d​λ|μ𝒬∈𝒲~3},\displaystyle=\left\{\frac{\mathrm{d}\mu\_{\mathcal{Q}}}{\mathrm{d}\lambda}\,\middle|\,\mu\_{\mathcal{Q}}\in\widetilde{\mathcal{W}}\_{3}\right\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | {ν∈L1​([0,1])|∫01ν​(t)​dt=1,ν​(t)⩾0​ a.e.,ν​ is non-decreasing}\displaystyle\left\{\nu\in L^{1}([0,1])\,\middle|\,\int\_{0}^{1}\nu(t)\,\mathrm{d}t=1,\;\nu(t)\geqslant 0\text{ a.e.},\;\nu\text{ is non-decreasing}\right\} | ={d​μ𝒬d​λ|μ𝒬∈𝒲~4}.\displaystyle=\left\{\frac{\mathrm{d}\mu\_{\mathcal{Q}}}{\mathrm{d}\lambda}\,\middle|\,\mu\_{\mathcal{Q}}\in\widetilde{\mathcal{W}}\_{4}\right\}. |  |

Then for any ν∈𝒲3\nu\in\mathcal{W}\_{3} or 𝒲4\mathcal{W}\_{4}, and for any g∈L∞​([0,1])g\in L^{\infty}([0,1]), we have

|  |  |  |
| --- | --- | --- |
|  | ∫01g​(t)​ν​(t)​dt=∫01g​(t)​dμν​(t).\displaystyle\int\_{0}^{1}g(t)\,\nu(t)\,\mathrm{d}t=\int\_{0}^{1}g(t)\,\mathrm{d}\mu\_{\nu}(t). |  |

This allows us to reformulate Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 2.3 WGRM under a Continuous Setting ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") within the framework of measure-theoretic integration.

###### Proposition 2.

(1) The aggregation function ff on L∞​([0,1])L^{\infty}([0,1]) satisfies (C1)-(C5) if and only if there exists a closed convex set of measures 𝒲~3∗:={μν∣ν∈𝒲3}⊂𝒲~3\widetilde{\mathcal{W}}\_{3}^{\*}:=\{\mu\_{\nu}\mid\nu\in\mathcal{W}\_{3}\}\subset\widetilde{\mathcal{W}}\_{3} such that

|  |  |  |
| --- | --- | --- |
|  | Ψ​(X|𝒬)=f​(φX)=supμ𝒬∈𝒲~3∗∫01φXq​(t)​dμ𝒬​(t),∀φX∈L∞​([0,1]).\displaystyle\Psi(X|\mathcal{Q})=f(\varphi\_{X})=\sup\_{\mu\_{\mathcal{Q}}\in\widetilde{\mathcal{W}}\_{3}^{\*}}\int\_{0}^{1}\varphi\_{X}^{q}(t)\,\mathrm{d}\mu\_{\mathcal{Q}}(t),\quad\forall\,\varphi\_{X}\in L^{\infty}([0,1]). |  |

(2) The aggregation function ff on L∞​([0,1])L^{\infty}([0,1]) satisfies (C1), (C2), (C3’) and (C4) if and only if there exists a closed convex set of measures 𝒲~4∗:={μν∣ν∈𝒲4}⊂𝒲~4\widetilde{\mathcal{W}}\_{4}^{\*}:=\{\mu\_{\nu}\mid\nu\in\mathcal{W}\_{4}\}\subset\widetilde{\mathcal{W}}\_{4} such that

|  |  |  |
| --- | --- | --- |
|  | Ψ​(X|𝒬)=f​(φX)=supμ𝒬∈𝒲~4∗∫01φXq​(t)​dμ𝒬​(t),∀φX∈L∞​([0,1]).\displaystyle\Psi(X|\mathcal{Q})=f(\varphi\_{X})=\sup\_{\mu\_{\mathcal{Q}}\in\widetilde{\mathcal{W}}\_{4}^{\*}}\int\_{0}^{1}\varphi\_{X}^{q}(t)\,\mathrm{d}\mu\_{\mathcal{Q}}(t),\quad\forall\,\varphi\_{X}\in L^{\infty}([0,1]). |  |

Recall that in the discrete setting, replacing (comonotonic) sub-additivity with (comonotonic) additivity guarantees the uniqueness of the weights via the Riesz Representation Theorem. A natural question arises: Can the weighting density ν​(t)\nu(t) in the continuous setting also be unique in this way? Unfortunately, the answer is not straightforward. Unlike the discrete case, working within L∞​([0,1])L^{\infty}([0,1]) presents a topological hurdle. Its dual space is not L1​([0,1])L^{1}([0,1]), but rather (L∞)∗(L^{\infty})^{\*}, which includes pathological purely finitely additive measures. Consequently, a standard application of the Riesz Representation Theorem on L∞L^{\infty} does not yield a unique weighting density function.

To secure uniqueness within the L∞L^{\infty} framework, one would typically need to impose additional constraints—such as L1L^{1}-continuity (see property (D5) below)—to force the functional to behave like an L1L^{1} functional, thereby allowing it to be extended to the L1L^{1} space. However, rather than navigating this circuitous route of constraining an L∞L^{\infty} functional to mimic the L1L^{1} behavior, we find it more mathematically natural to directly shift the underlying domain to L1​([0,1])L^{1}([0,1]). This approach may be of greater interest as L1​([0,1])L^{1}([0,1]) accommodates a broader class of risk profiles.

Define the set 𝒞^={g:[0,1]→ℝ∣g​is non-decreasing and left-continuous}⊆L1​([0,1])\hat{\mathcal{C}}=\{g:[0,1]\to\mathbb{R}\mid g\ \text{is non-decreasing and left-continuous}\}\subseteq L^{1}([0,1]). For any φX∈L1​([0,1])\varphi\_{X}\in L^{1}([0,1]), its quantile function is defined as in Eq.([6](#S2.E6 "In 2.3 WGRM under a Continuous Setting ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")). We examine the following properties under this new setup.

(D1) Affine invariance: f​(a​φX+b​𝟏[0,1])=a​f​(φX)+bf(a\varphi\_{X}+b\mathbf{1}\_{[0,1]})=af(\varphi\_{X})+b for all φX∈L1​([0,1])\varphi\_{X}\in L^{1}([0,1]), a⩾0a\geqslant 0, b∈ℝb\in\mathbb{R}, where 𝟏[0,1]\mathbf{1}\_{[0,1]} is an indicator function over interval [0,1][0,1].

(D2) Pointwise monotonicity: f​(φX)⩽f​(φY)f(\varphi\_{X})\leqslant f(\varphi\_{Y}) if φX⩽φY\varphi\_{X}\leqslant\varphi\_{Y} almost everywhere on [0,1][0,1], i.e., φX​(t)⩽φY​(t)\varphi\_{X}(t)\leqslant\varphi\_{Y}(t) for almost every t∈[0,1]t\in[0,1].

(D3) Comonotonic additivity: f​(φX+φY)=f​(φX)+f​(φY)f(\varphi\_{X}+\varphi\_{Y})=f(\varphi\_{X})+f(\varphi\_{Y}) whenever φX\varphi\_{X} and φY\varphi\_{Y} are comonotonic, i.e., (φX​(s)−φX​(t))​(φY​(s)−φY​(t))⩾0(\varphi\_{X}(s)-\varphi\_{X}(t))(\varphi\_{Y}(s)-\varphi\_{Y}(t))\geqslant 0 for almost every s,t∈[0,1]s,t\in[0,1].

(D3’) Full additivity: f​(φX+φY)=f​(φX)+f​(φY)f(\varphi\_{X}+\varphi\_{Y})=f(\varphi\_{X})+f(\varphi\_{Y}) for all φX,φY∈L1​([0,1])\varphi\_{X},\varphi\_{Y}\in L^{1}([0,1]).

(D4) Strong permutation invariance: f​(φX)=f​(φX∘T)f(\varphi\_{X})=f(\varphi\_{X}\circ T) for any Lebesgue measure-preserving transformations T:[0,1]→[0,1]T:[0,1]\to[0,1], i.e., λ​(T−1​(A))=λ​(A)\lambda(T^{-1}(A))=\lambda(A) for any Lebesgue measurable set A⊆[0,1]A\subseteq[0,1], where λ\lambda denotes the Lebesgue measure.

(D5) L1−L^{1}-continuity: There exists a constant M>0M>0 such that |f​(φX)−f​(φY)|⩽M​‖φX−φY‖L1|f(\varphi\_{X})-f(\varphi\_{Y})|\leqslant M\|\varphi\_{X}-\varphi\_{Y}\|\_{L^{1}} for all φX,φY∈L1​([0,1])\varphi\_{X},\varphi\_{Y}\in L^{1}([0,1]).

Based on these properties, we present the following results.

###### Proposition 3.

(1) The aggregation function ff satisfies (D1), (D2), (D3), and (D5) if and only if there exists a unique density function ν∗∈𝒲5⊆{ν∈L∞​([0,1])∣∫01ν​(t)​dt=1,ν​(t)⩾0​a.e.}\nu^{\*}\in\mathcal{W}\_{5}\subseteq\{\nu\in L^{\infty}([0,1])\mid\int\_{0}^{1}\nu(t)\mathrm{d}t=1,\nu(t)\geqslant 0\ \text{a.e.}\} such that

|  |  |  |
| --- | --- | --- |
|  | Ψ​(X|𝒬)=f​(φX)=∫01φX​(t)​ν∗​(t)​dt,∀φX∈𝒞^.\displaystyle\Psi(X|\mathcal{Q})=f(\varphi\_{X})=\int\_{0}^{1}\varphi\_{X}(t)\nu^{\*}(t)\mathrm{d}t,\quad\forall\,\varphi\_{X}\in\hat{\mathcal{C}}. |  |

(2) The aggregation function ff satisfies (D1), (D2), (D3), (D4), and (D5) if and only if there exists a unique density function ν∗∈𝒲5⊆{ν∈L∞​([0,1])∣∫01ν​(t)​dt=1,ν​(t)⩾0​a.e.}\nu^{\*}\in\mathcal{W}\_{5}\subseteq\{\nu\in L^{\infty}([0,1])\mid\int\_{0}^{1}\nu(t)\mathrm{d}t=1,\nu(t)\geqslant 0\ \text{a.e.}\} such that

|  |  |  |
| --- | --- | --- |
|  | Ψ​(X|𝒬)=f​(φX)=∫01φXq​(t)​ν∗​(t)​dt,∀φX∈L1​([0,1]).\displaystyle\Psi(X|\mathcal{Q})=f(\varphi\_{X})=\int\_{0}^{1}\varphi\_{X}^{q}(t)\nu^{\*}(t)\mathrm{d}t,\quad\forall\,\varphi\_{X}\in L^{1}([0,1]). |  |

(3) The aggregation function ff satisfies (D1), (D2), (D3’), and (D5) if and only if there exists a unique density function ν∗∈𝒲5⊆{ν∈L∞​([0,1])∣∫01ν​(t)​dt=1,ν​(t)⩾0​a.e.}\nu^{\*}\in\mathcal{W}\_{5}\subseteq\{\nu\in L^{\infty}([0,1])\mid\int\_{0}^{1}\nu(t)\mathrm{d}t=1,\nu(t)\geqslant 0\ \text{a.e.}\} such that

|  |  |  |
| --- | --- | --- |
|  | Ψ​(X|𝒬)=f​(φX)=∫01φX​(t)​ν∗​(t)​dt,∀φX∈L1​([0,1]).\displaystyle\Psi(X|\mathcal{Q})=f(\varphi\_{X})=\int\_{0}^{1}\varphi\_{X}(t)\nu^{\*}(t)\mathrm{d}t,\quad\forall\,\varphi\_{X}\in L^{1}([0,1]). |  |

(4) The aggregation function ff satisfies (D1), (D2), (D3’), (D4), and (D5) if and only if

|  |  |  |
| --- | --- | --- |
|  | Ψ​(X|𝒬)=f​(φX)=∫01φX​(t)​dt,∀φX∈L1​([0,1]),\displaystyle\Psi(X|\mathcal{Q})=f(\varphi\_{X})=\int\_{0}^{1}\varphi\_{X}(t)\mathrm{d}t,\quad\forall\,\varphi\_{X}\in L^{1}([0,1]), |  |

which implies ν∗​(t)≡1\nu^{\*}(t)\equiv 1 almost everywhere on [0,1][0,1].

## 3 Weighted Risk Quadrangle

WGRM offers a wide range of potential applications. In this section, however, we concentrate specifically on how it extends the Fundamental Risk Quadrangle framework introduced in Rockafellar and Uryasev ([2013](#bib.bib34 "The fundamental risk quadrangle in risk management, optimization and statistical estimation")). We begin with a detailed explanation of this foundational quadrangle. Several examples are then provided to illustrate the form and implications of WGRM within the expanded quadrangle framework. Although slight notational or presentational variations may occur across different settings, for consistency we adopt the expression given in Eq.([1](#S1.E1 "In Definition 2. ‣ 1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) throughout this section, regardless of the discreteness or continuity of the scenario or the uniqueness of the weighting measure μ𝒬\mu\_{\mathcal{Q}}.

### 3.1 Fundamental Risk Quadrangle Overview

Recall that an overview of the FRQ is illustrated in Figure [1](#S1.F1 "Figure 1 ‣ 1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"). Starting from the upper-left corner of the quadrangle, ℛ\mathcal{R} denotes a measure of risk, which quantifies the overall risk inherent in a random variable XX (representing loss or cost) by assigning it a numerical value. Such measures are frequently employed in the constraints of optimization problems or used as the objective function. For a constant c∈ℝc\in\mathbb{R}, the implicit constraint implied by the uncertain condition X⩽cX\leqslant c can be replaced by the explicit inequality ℛ​(X)⩽c\mathcal{R}(X)\leqslant c. This substitution leverages a concrete numerical metric ℛ​(X)\mathcal{R}(X) to offset the uncertain outcomes, thereby eliminating the uncertainty associated with XX and yielding a well-defined constraint.

Formally, we define ℛ\mathcal{R} as a regular measure of risk if ℛ\mathcal{R} is a closed convex functional with values in (−∞,∞](-\infty,\infty]; for any constant c∈ℝc\in\mathbb{R}, we have ℛ​(c)=c\mathcal{R}(c)=c, i.e., the risk of a deterministic cost cc equals cc itself; for any non-constant random variable XX, we have ℛ​(X)>𝔼​[X]\mathcal{R}(X)>\mathbb{E}[X], i.e., the risk measure exhibits risk aversion by assigning a value greater than the expected loss of a non-deterministic XX.

In the upper-right corner of the quadrangle, 𝒟\mathcal{D} denotes a measure of deviation, which quantifies the nonconstancy, i.e., uncertainty inherent in the random variable XX. Classic examples include the variance and standard deviation. Formally, a regular measure of deviation is defined as a closed convex functional taking values in [0,∞][0,\infty] such that for any constant c∈ℝc\in\mathbb{R}, we have 𝒟​(c)=0\mathcal{D}(c)=0, while for any non-constant random variable XX, it holds that 𝒟​(X)>0\mathcal{D}(X)>0. Notably, symmetry is not imposed as a general requirement. In other words, deviation measures where 𝒟​(X)≠𝒟​(−X)\mathcal{D}(X)\neq\mathcal{D}(-X) may be of greater interest in practical applications, since downside risk is somewhat always more annoying than upside risk.

In the lower-left corner of the quadrangle, 𝒱\mathcal{V} denotes a measure of regret, which quantifies the dissatisfaction associated with the potential outcomes—positive, zero, or negative.
Formally, a regular measure of regret is defined as a closed convex functional with values in (−∞,∞](-\infty,\infty] that satisfies 𝒱​(0)=0\mathcal{V}(0)=0; and for any non-zero random variable XX, it holds that 𝒱​(X)>𝔼​[X]\mathcal{V}(X)>\mathbb{E}[X].

Regret measures are naturally connected to utility measures 𝒰\mathcal{U}, another central concept in decision-making under uncertainty. Specifically, if XX is viewed as a loss, then −X-X corresponds to a gain, and the two concepts are interconvertible through the relation 𝒱​(X)=−𝒰​(−X)\mathcal{V}(X)=-\mathcal{U}(-X). Equivalently, if YY denotes a gain, the inverse conversion holds: 𝒰​(Y)=−𝒱​(−Y)\mathcal{U}(Y)=-\mathcal{V}(-Y).

In the lower-right corner of the quadrangle, ℰ\mathcal{E} denotes a measure of error, which quantifies the nonzeroness of a random variable. Formally, a regular measure of error is defined as a closed convex functional with values in [0,∞][0,\infty] that satisfies ℰ​(0)=0\mathcal{E}(0)=0, and ℰ​(X)>0\mathcal{E}(X)>0 for any non-zero random variable XX; moreover, for any sequence of random variables {Xk}k=1∞\{X\_{k}\}\_{k=1}^{\infty}, if limk→∞ℰ​(Xk)=0\lim\limits\_{k\to\infty}\mathcal{E}(X\_{k})=0, then we have limk→∞𝔼​[Xk]=0\lim\limits\_{k\to\infty}\mathbb{E}[X\_{k}]=0.

In estimation problems, particularly in regression where a loss random variable YY is approximated by a function f​(X1,…,XN)f(X\_{1},\dots,X\_{N}) of other random variables, ℰ\mathcal{E} serves as a metric to evaluate the magnitude of the prediction error Zf=Y−f​(X1,…,XN)Z\_{f}=Y-f(X\_{1},\dots,X\_{N}), thereby assessing the quality of the estimation. As with 𝒟\mathcal{D}, asymmetric measures of error, where ℰ​(X)≠ℰ​(−X)\mathcal{E}(X)\neq\mathcal{E}(-X), often warrant greater attention.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℛ​(X)\displaystyle\mathcal{R}(X) | =𝔼​[X]+𝒟​(X),𝒟​(X)=ℛ​(X)−𝔼​[X];\displaystyle=\mathbb{E}[X]+\mathcal{D}(X),\quad\mathcal{D}(X)=\mathcal{R}(X)-\mathbb{E}[X]; |  | (9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒱​(X)\displaystyle\mathcal{V}(X) | =𝔼​[X]+ℰ​(X),ℰ​(X)=𝒱​(X)−𝔼​[X];\displaystyle=\mathbb{E}[X]+\mathcal{E}(X),\quad\mathcal{E}(X)=\mathcal{V}(X)-\mathbb{E}[X]; |  | (10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℛ​(X)\displaystyle\mathcal{R}(X) | =minc⁡{c+𝒱​(X−c)},𝒟​(X)=minc⁡{ℰ​(X−c)};\displaystyle=\min\_{c}\{c+\mathcal{V}(X-c)\},\quad\mathcal{D}(X)=\min\_{c}\{\mathcal{E}(X-c)\}; |  | (11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | arg⁡minc\displaystyle\arg\min\_{c} | {c+𝒱​(X−c)}=𝒮​(X)=arg⁡minc⁡{ℰ​(X−c)}.\displaystyle\{c+\mathcal{V}(X-c)\}=\mathcal{S}(X)=\arg\min\_{c}\{\mathcal{E}(X-c)\}. |  | (12) |

The four corner elements of the quadrangle are not independent; rather, they interact and are interconnected through Eqs.([9](#S3.E9 "In 3.1 Fundamental Risk Quadrangle Overview ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"))–([12](#S3.E12 "In 3.1 Fundamental Risk Quadrangle Overview ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")). Specifically, it is noted in Figure [1](#S1.F1 "Figure 1 ‣ 1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") that bidirectional arrows connect the risk measure ℛ\mathcal{R} to the deviation measure 𝒟\mathcal{D}, and the regret measure 𝒱\mathcal{V} to the error measure ℰ\mathcal{E}—their conversion relations are given by Eqs.([9](#S3.E9 "In 3.1 Fundamental Risk Quadrangle Overview ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) and ([10](#S3.E10 "In 3.1 Fundamental Risk Quadrangle Overview ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")), respectively. In contrast, there is no direct equivalent conversion relation between ℛ\mathcal{R} and 𝒱\mathcal{V}, nor between 𝒟\mathcal{D} and ℰ\mathcal{E}; instead, these pairs are linked through 𝒮\mathcal{S}, the statistic located at the center of the quadrangle.

Concretely, for a given error measure ℰ\mathcal{E} and random variable XX, we seek a constant c∈ℝc\in\mathbb{R} that minimizes ℰ​(X−c)\mathcal{E}(X-c). The minimum value attained by this error measure is exactly the deviation measure 𝒟​(X)\mathcal{D}(X) of XX, and the constant cc that achieves this minimum is precisely the statistic 𝒮​(X)\mathcal{S}(X) of XX, with 𝒮​(X+d)=𝒮​(X)+d\mathcal{S}(X+d)=\mathcal{S}(X)+d for any d∈ℝd\in\mathbb{R}. This relationship is reflected in the right-hand segments of Eqs.([11](#S3.E11 "In 3.1 Fundamental Risk Quadrangle Overview ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) and ([12](#S3.E12 "In 3.1 Fundamental Risk Quadrangle Overview ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")). The relationship between ℛ\mathcal{R} and 𝒱\mathcal{V} follows the same logic, as illustrated in the left-hand segments of Eqs.([11](#S3.E11 "In 3.1 Fundamental Risk Quadrangle Overview ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) and ([12](#S3.E12 "In 3.1 Fundamental Risk Quadrangle Overview ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")).

For expositional brevity, we refer to the five quantities (i.e., ℛ\mathcal{R}, 𝒟\mathcal{D}, 𝒱\mathcal{V}, ℰ\mathcal{E}, and 𝒮\mathcal{S}) in Figure [1](#S1.F1 "Figure 1 ‣ 1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") that satisfy Eqs.([9](#S3.E9 "In 3.1 Fundamental Risk Quadrangle Overview ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"))–([12](#S3.E12 "In 3.1 Fundamental Risk Quadrangle Overview ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) a quadrangle quartet (ℛ,𝒟,𝒱,ℰ)(\mathcal{R},\mathcal{D},\mathcal{V},\mathcal{E}) associated with the statistic 𝒮\mathcal{S}. If the four measures (i.e., ℛ\mathcal{R}, 𝒟\mathcal{D}, 𝒱\mathcal{V}, and ℰ\mathcal{E}) within this quartet are all regular, we term this structure a regular quadrangle quartet. In what follows, our primary focus will be on regular quadrangle quartets.

### 3.2 Weighted Risk Quadrangle

While the quadrangle framework ingeniously integrates the five quantities into a unified structure, it suffers from a notable limitation that it is confined to various measures defined under a single probability measure. With the advancement of risk management technologies and the growing complexity of real-world stochastic environments, this single-measure setting has become restrictive. Thus, in this subsection, we build on the WGRM proposed earlier to further expand this quadrangle framework, which is denoted as Weighted Risk Quadrangle (WRQ), enabling it to accommodate multi-measure and multi-scenario risk modeling.

To avoid notational confusion, we denote the measures of the original FRQ under a single probability measure as ℛP,𝒟P,𝒱P,ℰP,𝒮P\mathcal{R}\_{P},\mathcal{D}\_{P},\mathcal{V}\_{P},\mathcal{E}\_{P},\mathcal{S}\_{P}, while using ℛ𝒬,𝒟𝒬,𝒱𝒬,ℰ𝒬,𝒮𝒬\mathcal{R}\_{\mathcal{Q}},\mathcal{D}\_{\mathcal{Q}},\mathcal{V}\_{\mathcal{Q}},\mathcal{E}\_{\mathcal{Q}},\mathcal{S}\_{\mathcal{Q}} to represent the corresponding measures within WRQ under a family of probability measures. Leveraging the results from Section [2](#S2 "2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"), we naturally adopt the proposed WGRM as the risk measure in the WRQ. Specifically, ℛ𝒬​(X)=Ψ​(X|𝒬)=∫𝒬Ψ​(X|P)​dμ𝒬​(P)\mathcal{R}\_{\mathcal{Q}}(X)=\Psi(X|\mathcal{Q})=\int\_{\mathcal{Q}}\Psi(X|P)\,\mathrm{d}\mu\_{\mathcal{Q}}(P). Under the weight μ𝒬\mu\_{\mathcal{Q}} defined, the risk quadrangle can be extended to a multi-scenario setting.

Prior to this extension, we first observe that the relationships in Eqs.([9](#S3.E9 "In 3.1 Fundamental Risk Quadrangle Overview ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"))–([12](#S3.E12 "In 3.1 Fundamental Risk Quadrangle Overview ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) also need to be extended to a multi-scenario context. In the original framework, the expectation operator 𝔼​[X]\mathbb{E}[X] plays a crucial bridging role. However, in the multi-scenario setting, this operator should also be extended to a multi-scenario expectation, defined as 𝔼𝒬​[X]=∫𝒬𝔼P​[X]​dμ𝒬​(P)\mathbb{E}\_{\mathcal{Q}}[X]=\int\_{\mathcal{Q}}\mathbb{E}\_{P}[X]\mathrm{d}\mu\_{\mathcal{Q}}(P). Then we can carry out a parallel generalization of Eqs.([9](#S3.E9 "In 3.1 Fundamental Risk Quadrangle Overview ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"))–([12](#S3.E12 "In 3.1 Fundamental Risk Quadrangle Overview ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) in the multi-scenario context as follows.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℛ𝒬​(X)\displaystyle\mathcal{R}\_{\mathcal{Q}}(X) | =𝔼𝒬​[X]+𝒟𝒬​(X),𝒟𝒬​(X)=ℛ𝒬​(X)−𝔼𝒬​[X];\displaystyle=\mathbb{E}\_{\mathcal{Q}}[X]+\mathcal{D}\_{\mathcal{Q}}(X),\quad\mathcal{D}\_{\mathcal{Q}}(X)=\mathcal{R}\_{\mathcal{Q}}(X)-\mathbb{E}\_{\mathcal{Q}}[X]; |  | (13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒱𝒬​(X)\displaystyle\mathcal{V}\_{\mathcal{Q}}(X) | =𝔼𝒬​[X]+ℰ𝒬​(X),ℰ𝒬​(X)=𝒱𝒬​(X)−𝔼𝒬​[X];\displaystyle=\mathbb{E}\_{\mathcal{Q}}[X]+\mathcal{E}\_{\mathcal{Q}}(X),\quad\mathcal{E}\_{\mathcal{Q}}(X)=\mathcal{V}\_{\mathcal{Q}}(X)-\mathbb{E}\_{\mathcal{Q}}[X]; |  | (14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℛ𝒬​(X)\displaystyle\mathcal{R}\_{\mathcal{Q}}(X) | =minc⁡{c+𝒱𝒬​(X−c)},𝒟𝒬​(X)=minc⁡{ℰ𝒬​(X−c)};\displaystyle=\min\_{c}\{c+\mathcal{V}\_{\mathcal{Q}}(X-c)\},\quad\mathcal{D}\_{\mathcal{Q}}(X)=\min\_{c}\{\mathcal{E}\_{\mathcal{Q}}(X-c)\}; |  | (15) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | arg⁡minc\displaystyle\arg\min\_{c} | {c+𝒱𝒬​(X−c)}=𝒮𝒬​(X)=arg⁡minc⁡{ℰ𝒬​(X−c)}.\displaystyle\{c+\mathcal{V}\_{\mathcal{Q}}(X-c)\}=\mathcal{S}\_{\mathcal{Q}}(X)=\arg\min\_{c}\{\mathcal{E}\_{\mathcal{Q}}(X-c)\}. |  | (16) |

The expansion implied by Eqs.([13](#S3.E13 "In 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"))–([16](#S3.E16 "In 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) requires theoretical justifications. Inspired by the Mixing Theorem by Rockafellar and Uryasev ([2013](#bib.bib34 "The fundamental risk quadrangle in risk management, optimization and statistical estimation")), we further propose the following theorem.

###### Theorem 3.

Under the weighting measure μ𝒬\mu\_{\mathcal{Q}} defined within ℛ𝒬​(X)=Ψ​(X|𝒬)=∫𝒬Ψ​(X|P)​dμ𝒬​(P)\mathcal{R}\_{\mathcal{Q}}(X)=\Psi(X|\mathcal{Q})=\int\_{\mathcal{Q}}\Psi(X|P)\,\mathrm{d}\mu\_{\mathcal{Q}}(P), let (ℛP=Ψ(⋅|P),𝒟P,𝒱P,ℰP)(\mathcal{R}\_{P}=\Psi(\cdot|P),\mathcal{D}\_{P},\mathcal{V}\_{P},\mathcal{E}\_{P}) denote a regular quadrangle quartet with statistic 𝒮P\mathcal{S}\_{P} for each P∈𝒬P\in\mathcal{Q}. A muti-scenario quadrangle quartet (ℛ𝒬,𝒟𝒬,𝒱𝒬,ℰ𝒬)(\mathcal{R}\_{\mathcal{Q}},\mathcal{D}\_{\mathcal{Q}},\mathcal{V}\_{\mathcal{Q}},\mathcal{E}\_{\mathcal{Q}}) with statistic S𝒬S\_{\mathcal{Q}} is generated by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒮𝒬​(X)\displaystyle\mathcal{S}\_{\mathcal{Q}}(X) | =∫𝒬𝒮P​(X)​dμ𝒬​(P),\displaystyle=\int\_{\mathcal{Q}}\mathcal{S}\_{P}(X)\mathrm{d}\mu\_{\mathcal{Q}}(P), |  | (17) |
|  | ℛ𝒬​(X)\displaystyle\mathcal{R}\_{\mathcal{Q}}(X) | =∫𝒬ℛP​(X)​dμ𝒬​(P),\displaystyle=\int\_{\mathcal{Q}}\mathcal{R}\_{P}(X)\mathrm{d}\mu\_{\mathcal{Q}}(P), |  |
|  | 𝒟𝒬​(X)\displaystyle\mathcal{D}\_{\mathcal{Q}}(X) | =∫𝒬𝒟P​(X)​dμ𝒬​(P),\displaystyle=\int\_{\mathcal{Q}}\mathcal{D}\_{P}(X)\mathrm{d}\mu\_{\mathcal{Q}}(P), |  |
|  | 𝒱𝒬​(X)\displaystyle\mathcal{V}\_{\mathcal{Q}}(X) | =minb​(P),P∈𝒬⁡{∫𝒬𝒱P​(X−b​(P))​dμ𝒬​(P)|∫𝒬b​(P)​dμ𝒬​(P)=0},\displaystyle=\min\_{b(P),P\in\mathcal{Q}}\left\{\int\_{\mathcal{Q}}\mathcal{V}\_{P}(X-b(P))\mathrm{d}\mu\_{\mathcal{Q}}(P)\ \middle|\ \int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0\right\}, |  |
|  | ℰ𝒬​(X)\displaystyle\mathcal{E}\_{\mathcal{Q}}(X) | =minb​(P),P∈𝒬⁡{∫𝒬ℰP​(X−b​(P))​dμ𝒬​(P)|∫𝒬b​(P)​dμ𝒬​(P)=0},\displaystyle=\min\_{b(P),P\in\mathcal{Q}}\left\{\int\_{\mathcal{Q}}\mathcal{E}\_{P}(X-b(P))\mathrm{d}\mu\_{\mathcal{Q}}(P)\ \middle|\ \int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0\right\}, |  |

where b​(⋅)b(\cdot) is a functional on 𝒬\mathcal{Q}.

So far, we have presented the theorem formulation of the WRQ. Next, we provide several relevant examples. Notably, due to the equivalent conversion relationships in Eqs.([13](#S3.E13 "In 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) and ([14](#S3.E14 "In 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")), as long as we know one of ℛ𝒬\mathcal{R}\_{\mathcal{Q}} and 𝒟𝒬\mathcal{D}\_{\mathcal{Q}}, and one of 𝒱𝒬\mathcal{V}\_{\mathcal{Q}} and ℰ𝒬\mathcal{E}\_{\mathcal{Q}}, we can derive the entire quartet (ℛ𝒬,𝒟𝒬,𝒱𝒬,ℰ𝒬)(\mathcal{R}\_{\mathcal{Q}},\mathcal{D}\_{\mathcal{Q}},\mathcal{V}\_{\mathcal{Q}},\mathcal{E}\_{\mathcal{Q}}). We can then further obtain 𝒮\mathcal{S} via Eq.([15](#S3.E15 "In 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")), thereby constructing the complete quadrangle.

###### Example 1.

Value-at-Risk (VaR, or quantile) and Expected Shortfall (ES, or Conditional VaR/CVaR) are both common tail-based risk metrics that have gained substantial significance in modern risk management frameworks (Basel Committee on Banking Supervision, [2019](#bib.bib5 "Minimum capital requirements for market risk"); McNeil et al., [2015](#bib.bib30 "Quantitative risk management: concepts, techniques and tools")). However, the latter is often preferred over the former because it accounts for tail risk and satisfies coherency. Thus, in this example, for each P∈𝒬P\in\mathcal{Q}, we set ℛP​(X)=ESαP​(X)\mathcal{R}\_{P}(X)=\text{ES}\_{\alpha}^{P}(X), where ESαP​(X)\text{ES}\_{\alpha}^{P}(X) denotes the α\alpha-level Expected Shortfall of XX under probability measure PP. For the error measure, we adopt the Koenker-Bassett error with appropriate adjustments to ensure that it projects to the desired 𝒟P​(X)\mathcal{D}\_{P}(X). Specifically, we define ℰP​(X)=𝔼P​[α1−α​X++X−]\mathcal{E}\_{P}(X)=\mathbb{E}\_{P}\left[\frac{\alpha}{1-\alpha}X\_{+}+X\_{-}\right], where X+=max⁡{0,X}X\_{+}=\max\{0,X\} and X−=max⁡{0,−X}X\_{-}=\max\{0,-X\}. Using the conversion relations in Eqs.([13](#S3.E13 "In 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"))–([16](#S3.E16 "In 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")), we can derive the remaining quantities of the single-measure quadrangle: 𝒟P​(X)=ESαP​(X−𝔼P​[X])\mathcal{D}\_{P}(X)=\text{ES}\_{\alpha}^{P}(X-\mathbb{E}\_{P}[X]), 𝒱P​(X)=11−α​𝔼P​[X+]\mathcal{V}\_{P}(X)=\frac{1}{1-\alpha}\mathbb{E}\_{P}[X\_{+}], and 𝒮P​(X)=VaRαP​(X)\mathcal{S}\_{P}(X)=\text{VaR}\_{\alpha}^{P}(X). Leveraging Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"), we immediately obtain the corresponding WRQ:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮𝒬​(X)\displaystyle\mathcal{S}\_{\mathcal{Q}}(X) | =∫𝒬VaRαP​(X)​dμ𝒬​(P),\displaystyle=\int\_{\mathcal{Q}}\text{VaR}\_{\alpha}^{P}(X)\mathrm{d}\mu\_{\mathcal{Q}}(P), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ𝒬​(X)\displaystyle\mathcal{R}\_{\mathcal{Q}}(X) | =∫𝒬ESαP​(X)​dμ𝒬​(P),\displaystyle=\int\_{\mathcal{Q}}\text{ES}\_{\alpha}^{P}(X)\mathrm{d}\mu\_{\mathcal{Q}}(P), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟𝒬​(X)\displaystyle\mathcal{D}\_{\mathcal{Q}}(X) | =∫𝒬ESαP​(X−𝔼𝒬​[X])​dμ𝒬​(P),\displaystyle=\int\_{\mathcal{Q}}\text{ES}\_{\alpha}^{P}(X-\mathbb{E}\_{\mathcal{Q}}[X])\mathrm{d}\mu\_{\mathcal{Q}}(P), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱𝒬​(X)\displaystyle\mathcal{V}\_{\mathcal{Q}}(X) | =minb​(P),P∈𝒬⁡{∫𝒬11−α​𝔼P​[(X−b​(P))+]​dμ𝒬​(P)|∫𝒬b​(P)​dμ𝒬​(P)=0},\displaystyle=\min\_{b(P),P\in\mathcal{Q}}\left\{\int\_{\mathcal{Q}}\frac{1}{1-\alpha}\mathbb{E}\_{P}[(X-b(P))\_{+}]\mathrm{d}\mu\_{\mathcal{Q}}(P)\ \middle|\ \int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0\right\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ𝒬​(X)\displaystyle\mathcal{E}\_{\mathcal{Q}}(X) | =minb​(P),P∈𝒬⁡{∫𝒬𝔼P​[α1−α​(X−b​(P))++(X−b​(P))−]​dμ𝒬​(P)|∫𝒬b​(P)​dμ𝒬​(P)=0}.\displaystyle=\min\_{b(P),P\in\mathcal{Q}}\left\{\int\_{\mathcal{Q}}\mathbb{E}\_{P}\left[\frac{\alpha}{1-\alpha}(X-b(P))\_{+}+(X-b(P))\_{-}\right]\mathrm{d}\mu\_{\mathcal{Q}}(P)\ \middle|\ \int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0\right\}. |  |

For appropriately chosen values of the α\alpha-level, each individual quadrangle quartet (ℛP,𝒟P,𝒱P,ℰP)(\mathcal{R}\_{P},\mathcal{D}\_{P},\mathcal{V}\_{P},\mathcal{E}\_{P}) corresponding to a single probability measure P∈𝒬P\in\mathcal{Q} is regular. Thus, the resulting multi-scenario quadrangle quartet (ℛ𝒬,𝒟𝒬,𝒱𝒬,ℰ𝒬)(\mathcal{R}\_{\mathcal{Q}},\mathcal{D}\_{\mathcal{Q}},\mathcal{V}\_{\mathcal{Q}},\mathcal{E}\_{\mathcal{Q}}) is also regular.

###### Remark 5.

Notably, in Example [1](#Thmexample1 "Example 1. ‣ 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"), neither 𝒟𝒬​(X)\mathcal{D}\_{\mathcal{Q}}(X) nor ℰ𝒬​(X)\mathcal{E}\_{\mathcal{Q}}(X) is necessarily symmetric. This asymmetry inherits from the single-measure components. The ESαP\text{ES}\_{\alpha}^{P} operator in 𝒟P\mathcal{D}\_{P} preserves the asymmetry of asymmetric distributions. For any random variable XX , it holds that ESαP​(−X)=𝔼P​[−X∣−X⩾VaRαP​(−X)]=−𝔼P​[X∣X⩽VaR1−αP​(X)]\text{ES}\_{\alpha}^{P}(-X)=\mathbb{E}\_{P}\left[-X\mid-X\geqslant\text{VaR}\_{\alpha}^{P}(-X)\right]=-\mathbb{E}\_{P}\left[X\mid X\leqslant\text{VaR}\_{1-\alpha}^{P}(X)\right], which shows that ESαP​(−X)≠−ESαP​(X)\text{ES}\_{\alpha}^{P}(-X)\neq-\text{ES}\_{\alpha}^{P}(X) in general, thus directly introducing asymmetry into 𝒟P\mathcal{D}\_{P}. Additionally, the single-measure error measure ℰP​(X)\mathcal{E}\_{P}(X) assigns distinct weights to the positive and negative parts of XX; specifically, a weight of α1−α\frac{\alpha}{1-\alpha} to X+X\_{+} and a weight of 11 to X−X\_{-}. This weighted distinction between X+X\_{+} and X−X\_{-} inherently makes ℰP​(X)\mathcal{E}\_{P}(X) asymmetric. Crucially, this asymmetry carries over to the weighted aggregation.

## 4 Optimization under WGRM and WRQ

This section presents a discussion on the connection between the WGRM, the WRQ, and optimization problems. In a typical optimization setting, the random variable XX, representing loss, generally depends on a decision vector 𝐱∈𝒢⊆ℝm\mathbf{x}\in\mathcal{G}\subseteq\mathbb{R}^{m}, where 𝒢\mathcal{G} denotes the feasible region. The objective is to determine an optimal decision vector 𝐱=(x1,…,xm)T\mathbf{x}=(x\_{1},\dots,x\_{m})^{T} within 𝒢\mathcal{G} that optimizes an objective function involving X​(𝐱)X(\mathbf{x}).
While the above theoretical framework accommodates both discrete and continuous scenarios, discrete scenarios are predominant in most practical optimization applications. Consequently, Eq.([17](#S3.E17 "In Theorem 3. ‣ 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) can be reformulated for a discrete set 𝒬={Pi∈𝒫∣i=1,…,n}\mathcal{Q}=\{P\_{i}\in\mathcal{P}\mid i=1,\dots,n\} as follows.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮𝒬​(X​(𝐱))\displaystyle\mathcal{S}\_{\mathcal{Q}}(X(\mathbf{x})) | =∑i=1n𝒮Pi​(X​(𝐱))⋅μ𝒬​(Pi),\displaystyle=\sum\_{i=1}^{n}\mathcal{S}\_{P\_{i}}(X(\mathbf{x}))\cdot\mu\_{\mathcal{Q}}(P\_{i}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ𝒬​(X​(𝐱))\displaystyle\mathcal{R}\_{\mathcal{Q}}(X(\mathbf{x})) | =∑i=1nℛPi​(X​(𝐱))⋅μ𝒬​(Pi),\displaystyle=\sum\_{i=1}^{n}\mathcal{R}\_{P\_{i}}(X(\mathbf{x}))\cdot\mu\_{\mathcal{Q}}(P\_{i}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟𝒬​(X​(𝐱))\displaystyle\mathcal{D}\_{\mathcal{Q}}(X(\mathbf{x})) | =∑i=1n𝒟Pi​(X​(𝐱))⋅μ𝒬​(Pi),\displaystyle=\sum\_{i=1}^{n}\mathcal{D}\_{P\_{i}}(X(\mathbf{x}))\cdot\mu\_{\mathcal{Q}}(P\_{i}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱𝒬​(X​(𝐱))\displaystyle\mathcal{V}\_{\mathcal{Q}}(X(\mathbf{x})) | =min{b​(Pi)}i=1n⁡{∑i=1n𝒱Pi​(X​(𝐱)−b​(Pi))⋅μ𝒬​(Pi)|∑i=1nb​(Pi)⋅μ𝒬​(Pi)=0},\displaystyle=\min\_{\{b(P\_{i})\}\_{i=1}^{n}}\left\{\sum\_{i=1}^{n}\mathcal{V}\_{P\_{i}}(X(\mathbf{x})-b(P\_{i}))\cdot\mu\_{\mathcal{Q}}(P\_{i})\ \middle|\ \sum\_{i=1}^{n}b(P\_{i})\cdot\mu\_{\mathcal{Q}}(P\_{i})=0\right\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ𝒬​(X​(𝐱))\displaystyle\mathcal{E}\_{\mathcal{Q}}(X(\mathbf{x})) | =min{b​(Pi)}i=1n⁡{∑i=1nℰPi​(X​(𝐱)−b​(Pi))⋅μ𝒬​(Pi)|∑i=1nb​(Pi)⋅μ𝒬​(Pi)=0}.\displaystyle=\min\_{\{b(P\_{i})\}\_{i=1}^{n}}\left\{\sum\_{i=1}^{n}\mathcal{E}\_{P\_{i}}(X(\mathbf{x})-b(P\_{i}))\cdot\mu\_{\mathcal{Q}}(P\_{i})\ \middle|\ \sum\_{i=1}^{n}b(P\_{i})\cdot\mu\_{\mathcal{Q}}(P\_{i})=0\right\}. |  |

A straightforward observation is that the expressions for 𝒱𝒬\mathcal{V}\_{\mathcal{Q}} and ℰ𝒬\mathcal{E}\_{\mathcal{Q}} are inherently minimization problems.
While the proof of Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") directly indicates that b​(Pi)=𝒮Pi​(X​(𝐱))−∑j=1n𝒮Pj​(X​(𝐱))⋅μ𝒬​(Pj)b(P\_{i})=\mathcal{S}\_{P\_{i}}(X(\mathbf{x}))-\sum\_{j=1}^{n}\mathcal{S}\_{P\_{j}}(X(\mathbf{x}))\cdot\mu\_{\mathcal{Q}}(P\_{j}), which in turn allows us to derive an explicit expression for 𝒱𝒬​(X​(𝐱))\mathcal{V}\_{\mathcal{Q}}(X(\mathbf{x})), practical implementation may favor numerical solutions via linear programming. This is particularly advantageous when confronting issues such as the complexity and nonlinearity of the individual functional 𝒱Pi\mathcal{V}\_{P\_{i}}, which makes linear programming more computationally tractable. Specifically, under a regular WRQ, each 𝒱Pi\mathcal{V}\_{P\_{i}} is a closed convex functional. Then there exists a family of linear functions ϕi​k\phi\_{ik}, where k∈Kik\in K\_{i} and KiK\_{i} denotes an index set, such that 𝒱Pi​(X​(𝐱))=supk∈Kiϕi​k​(X​(𝐱))\mathcal{V}\_{P\_{i}}(X(\mathbf{x}))=\sup\limits\_{k\in K\_{i}}\phi\_{ik}(X(\mathbf{x})). Thus, when X​(𝐱)X(\mathbf{x}) is linear in 𝐱\mathbf{x}, by introducing auxiliary variables tit\_{i}, the optimization problem in 𝒱𝒬​(X​(𝐱))\mathcal{V}\_{\mathcal{Q}}(X(\mathbf{x})) can be transformed into the following linear program:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min{b​(Pi)}i=1n\displaystyle\min\_{\{b(P\_{i})\}\_{i=1}^{n}} | ∑i=1nμ𝒬​(Pi)⋅ti\displaystyle\sum\_{i=1}^{n}\mu\_{\mathcal{Q}}(P\_{i})\cdot t\_{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. | ti⩾ϕi​k​(X​(𝐱)−b​(Pi)),∀i=1,…,n,k∈Ki,\displaystyle t\_{i}\geqslant\phi\_{ik}(X(\mathbf{x})-b(P\_{i})),\quad\forall\,i=1,\dots,n,\,k\in K\_{i}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑i=1nb​(Pi)⋅μ𝒬​(Pi)=0,\displaystyle\sum\_{i=1}^{n}b(P\_{i})\cdot\mu\_{\mathcal{Q}}(P\_{i})=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | b​(Pi)∈ℝ,∀i=1,…,n.\displaystyle b(P\_{i})\in\mathbb{R},\quad\forall\,i=1,\dots,n. |  |

Another set of optimization problems inherent to the WRQ is encapsulated in Eq.([15](#S3.E15 "In 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")). Taking the relationship between ℛ𝒬\mathcal{R}\_{\mathcal{Q}} and 𝒱𝒬\mathcal{V}\_{\mathcal{Q}} as an example, a typical risk management optimization problem might aim to minimize ℛ𝒬​(X​(𝐱))\mathcal{R}\_{\mathcal{Q}}(X(\mathbf{x})) with respect to the decision vector 𝐱\mathbf{x}. Notably, leveraging the key relation ℛ𝒬​(X​(𝐱))=minc∈ℝ⁡{c+𝒱𝒬​(X​(𝐱)−c)}\mathcal{R}\_{\mathcal{Q}}(X(\mathbf{x}))=\min\limits\_{c\in\mathbb{R}}\left\{c+\mathcal{V}\_{\mathcal{Q}}(X(\mathbf{x})-c)\right\}, the constraint ℛ𝒬​(X​(𝐱))⩽d\mathcal{R}\_{\mathcal{Q}}(X(\mathbf{x}))\leqslant d for any d∈ℝd\in\mathbb{R} is equivalent to the existence of some c0∈ℝc\_{0}\in\mathbb{R} such that c0+𝒱𝒬​(X​(𝐱)−c0)⩽dc\_{0}+\mathcal{V}\_{\mathcal{Q}}(X(\mathbf{x})-c\_{0})\leqslant d.
Consequently, the original objective function min𝐱⁡ℛ𝒬​(X​(𝐱))\min\limits\_{\mathbf{x}}\mathcal{R}\_{\mathcal{Q}}(X(\mathbf{x})) is equivalent to min𝐱,c⁡{c+𝒱𝒬​(X​(𝐱)−c)}\min\limits\_{\mathbf{x},c}\left\{c+\mathcal{V}\_{\mathcal{Q}}(X(\mathbf{x})-c)\right\}, which can be further transformed using the linear programming result above. Namely:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝐱ℛ𝒬​(X​(𝐱))s.t.𝐱∈𝒢,other constraints.⟷  min{⁢b(Pi)}=i1n,x,c+c∑=i1n⋅⁢μQ(Pi)tis.t.⩾ti⁢ϕ⁢ik(-⁢X(x)c⁢b(Pi)),=∀i1,…,n,∈kKi,=∑=i1n⁢⋅⁢b(Pi)μQ(Pi)0,∈⁢b(Pi)R,=∀i1,…,n,∈xG,other constraints. \begin{minipage}{86.72267pt}$\begin{aligned} \min\_{\mathbf{x}}\ &\mathcal{R}\_{\mathcal{Q}}(X(\mathbf{x}))\\ \text{s.t.}\,\ &\mathbf{x}\in\mathcal{G},\\ &\text{other constraints}.\end{aligned}$ \end{minipage}\longleftrightarrow\begin{minipage}{216.81pt}$\begin{aligned} \min\_{\{b(P\_{i})\}\_{i=1}^{n},\mathbf{x},c}&c+\sum\_{i=1}^{n}\mu\_{\mathcal{Q}}(P\_{i})\cdot t\_{i}\\ \text{s.t.}\quad&t\_{i}\geqslant\phi\_{ik}(X(\mathbf{x})-c-b(P\_{i})),\quad\forall\,i=1,\dots,n,\,k\in K\_{i},\\ &\sum\_{i=1}^{n}b(P\_{i})\cdot\mu\_{\mathcal{Q}}(P\_{i})=0,\\ &b(P\_{i})\in\mathbb{R},\quad\forall\,i=1,\dots,n,\\ &\mathbf{x}\in\mathcal{G},\\ &\text{other constraints}.\end{aligned}$ \end{minipage} |  | (18) |

###### Example 2.

We present here an application of Eq.([18](#S4.E18 "In 4 Optimization under WGRM and WRQ ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) in portfolio management (Zhu and Fukushima, [2009](#bib.bib39 "Worst-case conditional value-at-risk with application to robust portfolio management"); Behera and Kumar, [2025](#bib.bib6 "Optimizing mean conditional value-at-risk portfolios through deep neural network stock prediction")). It is assumed that there are mm financial assets in the market, with their returns denoted by random variables RjR\_{j} (j=1,…,mj=1,\dots,m) and corresponding expected values θj\theta\_{j}. We can thus use −Rj-R\_{j} to represent their potential losses. Our goal is to determine the optimal investment weights 𝐱=(x1,…,xm)T\mathbf{x}=(x\_{1},\dots,x\_{m})^{T} for each assest by incorporating the heterogeneous assessments of nn analysts on mm financial assets. The total loss of the portfolio can be expressed as X​(𝐱)=∑j=1m−xj​RjX(\mathbf{x})=\sum\limits\_{j=1}^{m}-x\_{j}R\_{j}.

Following the approach in Example [1](#Thmexample1 "Example 1. ‣ 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"), we adopt ESα\text{ES}\_{\alpha} as the portfolio risk metric (see Basel Committee on Banking Supervision ([2019](#bib.bib5 "Minimum capital requirements for market risk"))). Each analyst forms a view on the probability distribution of X​(𝐱)X(\mathbf{x}) based on their own insight, leading to the individual risk measure ℛPi​(X​(𝐱))=ESαPi​(X​(𝐱))=ESαPi​(∑j=1m−xj​Rj)\mathcal{R}\_{P\_{i}}(X(\mathbf{x}))=\text{ES}\_{\alpha}^{P\_{i}}(X(\mathbf{x}))=\text{ES}\_{\alpha}^{P\_{i}}\left(\sum\limits\_{j=1}^{m}-x\_{j}R\_{j}\right). Due to differences in analysts’ experience, professional competence, historical performance, and other factors, their perspectives are assigned different weights μ𝒬​(Pi)\mu\_{\mathcal{Q}}(P\_{i}) by the department manager. The corresponding optimization problem is therefore to select the optimal asset allocation weights that minimize the portfolio’s ES, given a target expected portfolio return (denoted by θ0\theta\_{0}). The objective function of this problem can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝐱⁡ℛ𝒬​(X​(𝐱))=min{xj}j=1m​∑i=1nESαPi​(∑j=1m−xj​Rj)⋅μ𝒬​(Pi).\displaystyle\min\limits\_{\mathbf{x}}\mathcal{R}\_{\mathcal{Q}}(X(\mathbf{x}))=\min\limits\_{\{x\_{j}\}\_{j=1}^{m}}\sum\limits\_{i=1}^{n}\text{ES}\_{\alpha}^{P\_{i}}\left(\sum\limits\_{j=1}^{m}-x\_{j}R\_{j}\right)\cdot\mu\_{\mathcal{Q}}(P\_{i}). |  | (19) |

However, directly solving ([19](#S4.E19 "In Example 2. ‣ 4 Optimization under WGRM and WRQ ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) using the relation ESαPi​(X)=11−α​∫α1VaRβPi​(X)​dβ\text{ES}\_{\alpha}^{P\_{i}}(X)=\frac{1}{1-\alpha}\int\_{\alpha}^{1}\text{VaR}\_{\beta}^{P\_{i}}(X)\mathrm{d}\beta requires a complete estimation of the cumulative distribution function, which is generally unavailable. Notably, within the risk quadrangle, the regret measure corresponding to the risk measure ℛPi​(X)=ESαPi​(X)\mathcal{R}\_{P\_{i}}(X)=\text{ES}\_{\alpha}^{P\_{i}}(X) is 𝒱Pi​(X)=11−α​𝔼Pi​[X+]\mathcal{V}\_{P\_{i}}(X)=\frac{1}{1-\alpha}\mathbb{E}^{P\_{i}}[X\_{+}]. This regret measure, for each Analyst ii, can be estimated using a series of historical data Xi​kX\_{ik} (k=1,…,Tik=1,\dots,T\_{i}), specifically as 11−α⋅1Ti​∑k=1Ti(Xi​k)+\frac{1}{1-\alpha}\cdot\frac{1}{T\_{i}}\sum\limits\_{k=1}^{T\_{i}}(X\_{ik})\_{+}. Thus, by introducing auxiliary variables ti​kt\_{ik}, this optimization problem can be transformed into the following linear program:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | min{xj},c,{b​(Pi)},{ti​k}\displaystyle\min\_{\{x\_{j}\},c,\{b(P\_{i})\},\{t\_{ik}\}} | c+11−α​∑i=1nμ𝒬​(Pi)​(1Ti​∑k=1Titi​k)\displaystyle c+\frac{1}{1-\alpha}\sum\_{i=1}^{n}\mu\_{\mathcal{Q}}(P\_{i})\left(\frac{1}{T\_{i}}\sum\limits\_{k=1}^{T\_{i}}t\_{ik}\right) |  | (20) |
|  | s.t. | ti​k⩾∑j=1m−xj​rj​k−c−b​(Pi),∀k=1,…,Ti,∀i=1,…,n,\displaystyle t\_{ik}\geqslant\sum\_{j=1}^{m}-x\_{j}r\_{jk}-c-b(P\_{i}),\quad\forall\,k=1,\dots,T\_{i},\ \forall\,i=1,\dots,n, |  |
|  |  | ti​k⩾0,∀k=1,…,Ti,∀i=1,…,n,\displaystyle t\_{ik}\geqslant 0,\quad\forall\,k=1,\dots,T\_{i},\quad\forall\,i=1,\dots,n, |  |
|  |  | ∑i=1nb​(Pi)⋅μ𝒬​(Pi)=0,\displaystyle\sum\_{i=1}^{n}b(P\_{i})\cdot\mu\_{\mathcal{Q}}(P\_{i})=0, |  |
|  |  | ∑j=1mxj​θj=θ0,\displaystyle\sum\_{j=1}^{m}x\_{j}\theta\_{j}=\theta\_{0}, |  |
|  |  | ∑j=1mxj=1, 0⩽xj<1,∀j=1,…,m.\displaystyle\sum\_{j=1}^{m}x\_{j}=1,0\leqslant x\_{j}<1,\quad\forall\,j=1,\dots,m. |  |

###### Remark 6.

It is worth noting that in Example [2](#Thmexample2 "Example 2. ‣ 4 Optimization under WGRM and WRQ ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"), the specific reflection of each analyst’s subjective probability measure PiP\_{i} lies in the selection of historical data when estimating 𝔼Pi​[(−∑j=1mrj​xj−c−b​(Pi))+]\mathbb{E}\_{P\_{i}}\left[\left(-\sum\_{j=1}^{m}r\_{j}x\_{j}-c-b(P\_{i})\right)\_{+}\right]. This estimation 1Ti​∑k=1Ti(∑j=1m−xj​rj​k−c−b​(Pi))+\frac{1}{T\_{i}}\sum\_{k=1}^{T\_{i}}\left(\sum\_{j=1}^{m}-x\_{j}r\_{jk}-c-b(P\_{i})\right)\_{+} relies on empirical average, where the choice of historical data encodes the analysts’ perspectives on future market dynamics.
Particularly, the length of the time horizon TiT\_{i} reflects Analyst ii’s view on the differences between historical and future market conditions. A longer TiT\_{i} indicates a belief that historical patterns are more representative of future trends without much structural change, while a shorter TiT\_{i} signals a perception of greater market divergence from the past. Meanwhile, the selection of specific historical return data rj​kr\_{jk} embodies an analyst’s judgment on potential future market cycles (e.g., expansion, recession, or stability). For instance, if an analyst believes the future will be characterized by high growth and low inflation without huge structural changes to fundamental market conditions, they will select return data from historical periods with similar macroeconomic contexts and adopt a longer time horizon.

## 5 Empirical Study

In this section, we illustrate the methodology introduced in Example [2](#Thmexample2 "Example 2. ‣ 4 Optimization under WGRM and WRQ ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") and apply it to the stock market. Using real-world examples, we conduct a discussion on the advantages and limitations of portfolio optimization leveraging the WGRM and WRQ. Specifically, we select constituent stocks of the NASDAQ 100 Index as the underlying assets, compare portfolio returns under different optimization methods with the index return across both expansion and recession market conditions, and subsequently perform sensitivity analysis by varying model parameters. The data used in this study are publicly available and were retrieved from <https://finance.yahoo.com>.

### 5.1 Empirical Setup

We assume there are 4 analysts (n=4n=4) with heterogeneous assessments in future macroeconomic trends. Based on their outlooks, each analyst estimates stock returns and informs stock selection in the portfolio, resulting in four distinct scenarios (Scenarios 1–4). The department manager integrates these four analysts’ assessments to make the optimal investment decision.
Analyst 1 expects future interest rates to rise. Thus, when using historical data to estimate expected stock returns, they select periods where interest rates exceeded the median within the observation window, yielding estimated expected returns {θj1}j=1m\{\theta^{1}\_{j}\}\_{j=1}^{m}. Analyst 2 anticipates future interest rates to fall, so they use data from periods where interest rates were below the median to estimate expected returns, denoted by {θj2}j=1m\{\theta^{2}\_{j}\}\_{j=1}^{m}.
Analyst 3 and Analyst 4 focus primarily on inflation, emphasizing the impact of real economic fluctuations on stock prices. Thus, Analyst 3 predicts rising inflation, with corresponding expected returns denoted by {θj3}j=1m\{\theta^{3}\_{j}\}\_{j=1}^{m}, while Analyst 4 predicts falling inflation, with expected returns {θj4}j=1m\{\theta^{4}\_{j}\}\_{j=1}^{m}. For this study, we use the U.S. 10-year Treasury bond yield as the interest rate proxy since its maturity is more aligned with that of stocks, and use the CPI for inflation measurements. For each analyst ii, the corresponding portfolio optimization problem is formulated as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | min{xj},c,{ti​k}\displaystyle\min\_{\{x\_{j}\},c,\{t\_{ik}\}} | c+1(1−α)​Ti​∑k=1Titi​k\displaystyle c+\frac{1}{(1-\alpha)T\_{i}}\sum\_{k=1}^{T\_{i}}t\_{ik} |  | (21) |
|  | s.t. | ti​k⩾∑j=1m−xj​rj​k−c,∀k=1,…,Ti,\displaystyle t\_{ik}\geqslant\sum\_{j=1}^{m}-x\_{j}r\_{jk}-c,\quad\forall\,k=1,\dots,T\_{i}, |  |
|  |  | ti​k⩾0,∀k=1,…,Ti,\displaystyle t\_{ik}\geqslant 0,\quad\forall\,k=1,\dots,T\_{i}, |  |
|  |  | ∑j=1mxj​θji⩾θ0,\displaystyle\sum\_{j=1}^{m}x\_{j}\theta^{i}\_{j}\geqslant\theta\_{0}, |  |
|  |  | ∑j=1mxj=1, 0⩽xj<1,∀j=1,…,m.\displaystyle\sum\_{j=1}^{m}x\_{j}=1,0\leqslant x\_{j}<1,\forall\,\ j=1,\dots,m. |  |

The manager integrates the four analysts’ assessments, so their expected stock returns are a weighted aggregation of the analysts’ estimates, i.e., θj=∑i=14μ𝒬​(Pi)​θji\theta\_{j}=\sum\limits\_{i=1}^{4}\mu\_{\mathcal{Q}}(P\_{i})\theta^{i}\_{j}. For simplicity, we assign equal weights to each analyst’s perspective, i.e., μ𝒬​(Pi)=14\mu\_{\mathcal{Q}}(P\_{i})=\frac{1}{4}, adopting a purely synthetic lens to evaluate the framework. Thus, the manager’s optimization problem is exactly the one formulated in Eq.([20](#S4.E20 "In Example 2. ‣ 4 Optimization under WGRM and WRQ ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")).

To conduct a comprehensive assessment, we examine two distinct market regimes, recession and expansion respectively, to evaluate how the manager using the integrated multi-scenario approach performs compared to individual analysts relying on single-scenario frameworks. For the ES metric, we adopt the commonly used level α=0.95\alpha=0.95. During February and March 2025, the NASDAQ 100 Index experienced a sharp decline, with a cumulative two-month return of −11.86%-11.86\%. Although this episode reflects market turbulence rather than a macroeconomic recession, we refer to it as a recession regime for terminological convenience. For this scenario, we use a total time window of T=150T=150 trading days, spanning from August 23, 2024, to March 31, 2025, and split the data into a training set and a backtesting set using February 1, 2025, as the cutoff date. The target return θ0\theta\_{0} is set to the average daily return of January 2025, calculated as θ0=1.64%/20\theta\_{0}=1.64\%/20. We construct portfolios using weights estimated from the training set, evaluate their performance using backtesting set data, and compare the results to the actual NASDAQ 100 Index return.

In contrast, September and October 2025 saw robust growth in the index, with a cumulative two-month return of 10.58%10.58\%, designated as the expansion regime. Following a consistent methodology, we again use a 150-trading-day time window (May 12, 2025, to October 30, 2025), splitting the data at September 1, 2025, into two sets. The target return θ0\theta\_{0} is the average daily return of August 2025, computed as θ0=3.90%/21\theta\_{0}=3.90\%/21, while all other parameters remain identical to the recession regime.

We use these two regimes as benchmark cases, and then conduct sensitivity analysis by adjusting key model parameters to test the framework’s robustness. Specifically, within each regime, we modify the time window to T=120T=120 and T=180T=180 trading days, adjust the ES level to α=0.90\alpha=0.90 and α=0.99\alpha=0.99, scale the target return θ0\theta\_{0} by a factor of 2 and 0.5, and finally replace the underlying assets from NASDAQ 100 constituents with S&P 500 constituents.

Intuitively, since ES explicitly accounts for tail risks, ES-based portfolios exhibit inherent robustness. While this conservative focus on downside protection may moderate returns during market expansions, it should deliver superior resilience during recessions to the broader index. Furthermore, the manager’s equal-weighted aggregation of conflicting scenarios (i.e., opposing views on interest rates and inflation) achieves a form of view diversification. This prevents overexposure to any single bullish forecast, effectively mitigating the idiosyncratic risk of an isolated misjudgment and lowering overall portfolio volatility. Therefore, to comprehensively evaluate the portfolios beyond raw two-month returns, we incorporate annualized Sharpe and Sortino ratios. By explicitly penalizing total and downside volatility, these metrics properly align with our focus on tail-risk mitigation. The one-year U.S. Treasury yield (3.65%) serves as the risk-free rate.

### 5.2 Baseline Results

Table [1](#S5.T1 "Table 1 ‣ 5.2 Baseline Results ‣ 5 Empirical Study ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") presents the baseline results. During the recession regime, all ES-based portfolios demonstrate excellent downside resilience by delivering positive returns despite a substantial index decline. Although Analyst 1 achieves the highest raw return, the manager’s portfolio yields the highest annualized Sharpe and Sortino ratios, generating the highest risk-adjusted return per unit of risk. This indicates the robustness of the WGRM-based portfolios during market distress.
In the expansion regime, the inherent conservatism of ES optimization causes all portfolios to underperform the strongly rallying index. Crucially, however, while Analyst 1’s isolated forecast results in a negative return, the manager’s portfolio maintains moderate profitability and mid-tier risk-adjusted performance.
This outcome directly underscores the method’s inherent trade-off: while the WGRM-based approach may lag during aggressive market expansions, it excels in distressed markets by providing robust downside protection and structurally buffering against the idiosyncratic risk of a single erroneous forecast.

Table 1: Baseline Results.

Recession regime
Expansion regime

Portfolio



Two-month

return



Sharpe

ratio



Sortino

ratio



Two-month

return



Sharpe

ratio



Sortino

ratio


Analyst 1
5.98%
2.574
4.387
-2.81%
-1.893
-2.610

Analyst 2
1.85%
0.713
1.355
3.93%
1.533
3.514

Analyst 3
4.27%
1.895
3.890
6.93%
3.307
5.224

Analyst 4
4.56%
1.723
2.584
1.67%
0.432
0.671

Manager
5.71%
2.809
5.336
3.28%
1.665
2.857

Index two-month return
-11.86%


10.58%

Figure [3](#S5.F3 "Figure 3 ‣ 5.2 Baseline Results ‣ 5 Empirical Study ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") visualizes the daily portfolio returns across both market regimes. The manager’s portfolio exhibits lower volatility than any single analyst’s strategy. By avoiding extreme return fluctuations and structurally reducing both the frequency and magnitude of deep drawdowns, the WGRM-based method confirms its distinctly conservative and downside-protective risk profile.

![Refer to caption](2603.10327v2/NASDAQ_Bad_150.png)


(a) Recession regime

![Refer to caption](2603.10327v2/NASDAQ_Good_150.png)


(b) Expansion regime

Figure 3: Baseline Portfolio Daily Return.

### 5.3 Sensitivity Analysis

In this subsection, we conduct a sensitivity analysis to ensure our baseline findings are not artifacts of specific parameter choices. Table [2](#S5.T2 "Table 2 ‣ 5.3 Sensitivity Analysis ‣ 5 Empirical Study ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") reports portfolio performance under alternative time windows (T=120T=120 and T=180T=180). During the recession regime, the manager’s portfolio is more noticeably dragged down by Analyst 2’s misjudgment than in the baseline; crucially, however, it still significantly outperforms Analyst 2’s isolated strategy. In the expansion regime, the integrated portfolio maintains mid-tier performance similar to the baseline case at T=120T=120 but underperforms at T=180T=180.

###### Remark 7.

Varying time windows induces performance fluctuations due to the bias-variance tradeoff inherent in historical data estimation: shorter windows increase estimation variance, whereas longer windows may incorporate outdated market fundamentals.
However, our primary goal here is not to evaluate the absolute robustness of ES itself, but rather to verify whether the manager’s WGRM-based approach consistently maintains its structural advantage across diverse parameter specifications.

Table 2: Change Time Window.

Recession regime
Expansion regime

Portfolio



Two-month

return



Sharpe

ratio



Sortino

ratio



Two-month

return



Sharpe

ratio



Sortino

ratio

Panel A: Change time window to T=120T=120


Analyst 1
8.38%
2.910
5.480
9.85%
3.396
5.061

Analyst 2
0.71%
0.059
0.094
10.08%
4.321
9.064

Analyst 3
3.91%
1.675
3.529
6.93%
3.307
5.224

Analyst 4
5.64%
1.515
2.680
19.26%
5.974
16.135

Manager
3.00%
1.266
2.695
7.42%
3.960
7.586

Panel B: Change time window to T=180T=180


Analyst 1
5.20%
2.388
4.290
-2.02%
-1.518
-2.208

Analyst 2
-1.29%
-0.748
-1.079
2.27%
0.841
1.420

Analyst 3
4.68%
2.154
3.653
3.92%
2.067
3.239

Analyst 4
3.56%
1.172
1.937
1.24%
0.288
0.503

Manager
0.26%
-0.161
-0.285
-1.16%
-0.913
-1.292

Table [3](#S5.T3 "Table 3 ‣ 5.3 Sensitivity Analysis ‣ 5 Empirical Study ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") reports the results when the ES level is adjusted to α=0.90\alpha=0.90 and α=0.99\alpha=0.99. The manager’s portfolio performs consistently with the baseline, except for notable underperformance during the expansion regime at α=0.99\alpha=0.99. The observed underperformance might be attributed to excessive conservatism. This heightened risk aversion likely leads the optimization process to over-allocate to low-volatility, defensive assets. Such assets tend to underperform in bull markets, as they fail to capture the strong upward momentum typically associated with growth-oriented stocks during economic expansions.

Table 3: Change Level.

Recession regime
Expansion regime

Portfolio



Two-month

return



Sharpe

ratio



Sortino

ratio



Two-month

return



Sharpe

ratio



Sortino

ratio

Panel A: Change level to α=0.90\alpha=0.90


Analyst 1
1.30%
0.363
0.686
1.01%
0.223
0.324

Analyst 2
1.42%
0.435
0.884
11.43%
5.960
12.281

Analyst 3
0.04%
-0.270
-0.534
9.70%
5.252
10.859

Analyst 4
4.63%
1.757
2.523
2.43%
0.853
1.515

Manager
2.63%
1.078
2.153
8.01%
4.579
9.388

Panel B: Change level to α=0.99\alpha=0.99


Analyst 1
6.70%
2.715
5.529
-2.78%
-1.866
-2.565

Analyst 2
-0.19%
-0.382
-0.869
3.70%
1.256
2.546

Analyst 3
6.96%
2.977
6.180
9.91%
5.073
11.733

Analyst 4
4.56%
1.723
2.584
0.27%
-0.138
-0.216

Manager
7.88%
3.927
7.604
-2.62%
-1.471
-2.618

Table [4](#S5.T4 "Table 4 ‣ 5.3 Sensitivity Analysis ‣ 5 Empirical Study ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") displays the results with target returns scaled by 0.5 and 2. The manager’s portfolio aligns with the baseline except during the expansion regime with a doubled target, unexpectedly posting a negative return while all individual analysts remain profitable. This counterintuitive result highlights the tension between aggressive return targets and the WGRM framework’s mandate for risk mitigation. Pressured to pursue outsized gains in a market already exceeding historical averages, the integrated method’s requirement to balance heterogeneous assessments structurally prevents over concentration in high-momentum assets. Consequently, the optimizer defaults to less volatile, value-oriented stocks, which inherently lag in a momentum-driven bull market.

Table 4: Change Target Return.

Recession regime
Expansion regime

Portfolio



Two-month

return



Sharpe

ratio



Sortino

ratio



Two-month

return



Sharpe

ratio



Sortino

ratio

Panel A: Change target return to θ×2\theta\times 2


Analyst 1
7.68%
3.156
5.752
3.83%
1.370
2.160

Analyst 2
1.18%
0.285
0.497
7.89%
2.326
5.134

Analyst 3
7.11%
2.501
5.829
18.24%
5.470
8.988

Analyst 4
4.52%
1.876
3.623
2.92%
0.914
1.495

Manager
7.98%
3.568
7.228
-1.70%
-0.937
-1.367

Panel B: Change target return to θ/2\theta/2


Analyst 1
6.70%
2.715
5.529
-1.49%
-1.114
-1.407

Analyst 2
-0.16%
-0.369
-0.837
1.80%
0.507
0.840

Analyst 3
8.74%
3.811
7.434
8.23%
4.998
9.160

Analyst 4
4.56%
1.723
2.584
0.71%
0.037
0.052

Manager
7.47%
3.762
7.699
7.24%
3.814
6.165

Table [5](#S5.T5 "Table 5 ‣ 5.3 Sensitivity Analysis ‣ 5 Empirical Study ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application") replicates the baseline and sensitivity analyses using S&P 500 constituents. Outcomes consistently match, and occasionally surpass, the initial findings. In several cases (e.g., Panels A, D, E, and G), during the recession regime, the manager’s portfolio maintains a positive return even in instances where every individual analyst’s strategy incurs losses. This demonstrates the resilience of the WGRM framework across different asset universes. Furthermore, compared to the tech-heavy NASDAQ 100, the broader sectoral coverage of the S&P 500 inherently introduces more defensive and value-oriented stocks. This expanded asset base provides more options for diversification, and also confirms that the WGRM method’s structural robustness is not asset-specific, highlighting its superior adaptability to diverse market segments.

Table 5: Change Underlying Assets.

Recession regime
Expansion regime

Portfolio



Two-month

return



Sharpe

ratio



Sortino

ratio



Two-month

return



Sharpe

ratio



Sortino

ratio

Panel A: Benchmark case


Analyst 1
-1.84%
-0.839
-1.089
4.28%
2.409
4.745

Analyst 2
-0.06%
-0.430
-0.704
3.20%
1.212
2.196

Analyst 3
-2.11%
-1.461
-2.023
7.86%
4.332
5.640

Analyst 4
-4.20%
-1.893
-3.147
4.39%
1.876
3.361

Manager
0.44%
-0.144
-0.186
3.44%
1.427
3.011

Panel B: Change time window to T=120T=120


Analyst 1
1.03%
0.163
0.237
7.55%
2.923
4.936

Analyst 2
-1.04%
-3.781
-6.903
10.76%
4.608
7.351

Analyst 3
-0.90%
-0.571
-0.905
7.86%
4.332
5.640

Analyst 4
-10.43%
-2.578
-4.340
8.28%
2.750
4.637

Manager
0.09%
-0.429
-0.529
8.73%
4.934
7.010

Panel C: Change time window to T=180T=180


Analyst 1
0.67%
0.038
0.055
3.14%
1.278
1.881

Analyst 2
-1.99%
-1.556
-2.499
1.39%
0.378
0.769

Analyst 3
-0.14%
-0.336
-0.497
5.55%
3.139
4.103

Analyst 4
-2.03%
-1.407
-2.443
4.37%
2.037
4.150

Manager
-0.19%
-0.401
-0.662
3.65%
1.724
4.287

Panel D: Change level to α=0.90\alpha=0.90


Analyst 1
-1.84%
-0.839
-1.089
4.28%
2.409
4.745

Analyst 2
-0.06%
-0.430
-0.704
4.71%
1.856
3.117

Analyst 3
-2.11%
-1.461
-2.023
7.86%
4.332
5.640

Analyst 4
-4.20%
-1.893
-3.147
3.98%
2.009
4.771

Manager
0.64%
0.069
0.088
3.88%
1.919
4.769

Panel E: Change level to α=0.99\alpha=0.99


Analyst 1
-1.84%
-0.839
-1.089
4.28%
2.409
4.745

Analyst 2
-0.06%
-0.430
-0.704
3.20%
1.212
2.196

Analyst 3
-2.11%
-1.461
-2.023
7.86%
4.332
5.640

Analyst 4
-4.20%
-1.893
-3.147
4.39%
1.876
3.361

Manager
0.44%
-0.144
-0.186
2.48%
0.893
1.566

Panel F: Change target return to θ×2\theta\times 2


Analyst 1
-1.84%
-0.839
-1.089
7.38%
2.843
5.052

Analyst 2
-0.06%
-0.430
-0.704
2.19%
0.504
0.722

Analyst 3
-2.03%
-1.367
-1.903
4.85%
2.335
3.202

Analyst 4
-4.20%
-1.893
-3.147
3.04%
0.837
1.174

Manager
-2.20%
-1.548
-2.140
6.27%
1.664
3.766

Panel G: Change target return to θ/2\theta/2


Analyst 1
-1.84%
-0.839
-1.089
2.35%
1.238
2.270

Analyst 2
-0.06%
-0.430
-0.704
6.17%
2.744
6.208

Analyst 3
-2.11%
-1.461
-2.023
7.86%
4.332
5.640

Analyst 4
-4.20%
-1.893
-3.147
3.70%
1.556
3.736

Manager
1.58%
0.739
0.947
3.30%
1.417
3.635

In summary, our empirical findings confirm that WGRM-based portfolios exhibit greater conservatism and robustness. While this framework may not generate outstanding raw returns in expansion regimes due to its inherent focus on downside protection, it consistently delivers superior resilience during recessions. Most crucially, it acts as a structural buffer, neutralizing the idiosyncratic risk of isolated misjudgments and preventing the severe consequences of over-relying on a single, flawed market outlook.

## Acknowledgements

YL acknowledges financial support from the National Natural Science Foundation of China (Grant No. 12401624), The Chinese University of Hong Kong (Shenzhen) University Development Fund (Grant No. UDF01003336) and Shenzhen Science and Technology Program (Grant No. RCBS20231211090814028, JCYJ20250604141203005, 2025TC0010) and is partly supported by the Guangdong Provincial Key Laboratory of Mathematical Foundations for Artificial Intelligence (Grant No. 2023B1212010001).
YW acknowledges financial support from the Natural Sciences and Engineering Research Council of Canada (RGPIN-2023-04674, DGECR-2023-00454), and the start-up fund at Carleton University.
YW thanks The Chinese University of Hong Kong (Shenzhen) for the kind hospitality during her visit in 2025.

## References

* T. Adrian and M. K. Brunnermeier (2016)
  CoVaR.
  American Economic Review 106 (7),  pp. 1705–41.
  External Links: [Document](https://dx.doi.org/10.1257/aer.20120555),
  [Link](https://www.aeaweb.org/articles?id=10.1257/aer.20120555)
  Cited by: [§1.2](#S1.SS2.p1.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* S. Ahmed, D. Filipović, and G. Svindland (2008)
  A note on natural risk statistics.
  Operations Research Letters 36 (6),  pp. 662–664.
  External Links: ISSN 0167-6377,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.orl.2008.06.009),
  [Link](https://www.sciencedirect.com/science/article/pii/S0167637708000874)
  Cited by: [§2.2](#S2.SS2.p11.1 "2.2 WGRM under a Discrete Setting ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* P. Artzner, F. Delbaen, J. Eber, and D. Heath (1999)
  Coherent measures of risk.
  Mathematical Finance 9 (3),  pp. 203–228.
  External Links: [Document](https://dx.doi.org/https%3A//doi.org/10.1111/1467-9965.00068),
  [Link](https://onlinelibrary.wiley.com/doi/abs/10.1111/1467-9965.00068),
  https://onlinelibrary.wiley.com/doi/pdf/10.1111/1467-9965.00068
  Cited by: [§1.1](#S1.SS1.p2.2 "1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* Basel Committee on Banking Supervision (2019)
  Minimum capital requirements for market risk.
  Standard
   Bank for International Settlements, Basel, Switzerland (en).
  External Links: [Link](https://www.bis.org/bcbs/publ/d457.htm)
  Cited by: [Example 1](#Thmexample1.p1.13 "Example 1. ‣ 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [Example 2](#Thmexample2.p2.5 "Example 2. ‣ 4 Optimization under WGRM and WRQ ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* M. Battiston and L. Rimella (2025)
  Disclosure risk assessment with bayesian non-parametric hierarchical modelling.
  Statistics and Computing 35 (5),  pp. 158.
  External Links: ISSN 1573-1375,
  [Document](https://dx.doi.org/10.1007/s11222-025-10693-9),
  [Link](https://doi.org/10.1007/s11222-025-10693-9)
  Cited by: [§1.2](#S1.SS2.p3.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* J. Behera and P. Kumar (2025)
  Optimizing mean conditional value-at-risk portfolios through deep neural network stock prediction.
  Engineering Applications of Artificial Intelligence 161,  pp. 112198.
  External Links: ISSN 0952-1976,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.engappai.2025.112198),
  [Link](https://www.sciencedirect.com/science/article/pii/S0952197625022067)
  Cited by: [Example 2](#Thmexample2.p1.9 "Example 2. ‣ 4 Optimization under WGRM and WRQ ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* F. Bellini and E. D. Bernardino (2017)
  Risk management with expectiles.
  European Journal of Finance 23 (6),  pp. 487–506.
  External Links: [Document](https://dx.doi.org/10.1080/1351847X.2015.1052150),
  [Link](https://doi.org/10.1080/1351847X.2015.1052150),
  https://doi.org/10.1080/1351847X.2015.1052150
  Cited by: [§1.2](#S1.SS2.p3.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* C. Bernard, S. M. Pesenti, and S. Vanduffel (2024)
  Robust distortion risk measures.
  Mathematical Finance 34 (3),  pp. 774–818.
  External Links: [Document](https://dx.doi.org/https%3A//doi.org/10.1111/mafi.12414),
  [Link](https://onlinelibrary.wiley.com/doi/abs/10.1111/mafi.12414),
  https://onlinelibrary.wiley.com/doi/pdf/10.1111/mafi.12414
  Cited by: [§1.2](#S1.SS2.p3.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* J. Blanchet, H. Lam, Y. Liu, and R. Wang (2025)
  Convolution bounds on quantile aggregation.
  Operations Research 73 (5),  pp. 2761–2781.
  Cited by: [§1.2](#S1.SS2.p1.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* M. Brutti Righi (2018)
  A theory for combinations of risk measures.
  arXiv e-prints,  pp. arXiv:1807.01977.
  External Links: [Document](https://dx.doi.org/10.48550/arXiv.1807.01977),
  1807.01977
  Cited by: [§1.2](#S1.SS2.p2.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* J. Cai, J. Y. Li, and T. Mao (2025)
  Distributionally robust optimization under distorted expectations.
  Operations Research 73 (2),  pp. 969–985.
  External Links: [Document](https://dx.doi.org/10.1287/opre.2020.0685),
  [Link](https://doi.org/10.1287/opre.2020.0685),
  https://doi.org/10.1287/opre.2020.0685
  Cited by: [§1.2](#S1.SS2.p3.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* E. Castagnoli, G. Cattelan, F. Maccheroni, C. Tebaldi, and R. Wang (2022)
  Star-shaped risk measures.
  Operations Research 70 (5),  pp. 2637–2654.
  External Links: [Document](https://dx.doi.org/10.1287/opre.2022.2303),
  [Link](https://doi.org/10.1287/opre.2022.2303),
  https://doi.org/10.1287/opre.2022.2303
  Cited by: [§1.2](#S1.SS2.p1.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* Y. Chen, P. Liu, Y. Liu, and R. Wang (2022)
  Ordering and inequalities of mixtures on risk aggregation.
  Mathematical Finance 32 (1),  pp. 421–451.
  Cited by: [§1.2](#S1.SS2.p1.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* R. Cont, R. Deguest, and G. Scandolo (2010)
  Robustness and sensitivity analysis of risk measurement procedures.
  Quantitative Finance 10 (6),  pp. 593–606.
  External Links: [Document](https://dx.doi.org/10.1080/14697681003685597),
  [Link](https://doi.org/10.1080/14697681003685597),
  https://doi.org/10.1080/14697681003685597
  Cited by: [§1.1](#S1.SS1.p1.1 "1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* P. Embrechts, B. Wang, and R. Wang (2015)
  Aggregation-robustness and model uncertainty of regulatory risk measures.
  Finance and Stochastics 19 (4),  pp. 763–790.
  External Links: [Document](https://dx.doi.org/10.1007/s00780-015-0273-z),
  [Link](https://link.springer.com/article/10.1007/s00780-015-0273-z)
  Cited by: [§1.1](#S1.SS1.p1.1 "1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* T. Fadina, Y. Liu, and R. Wang (2024)
  A framework for measures of risk under uncertainty.
  Finance and Stochastics 28 (2),  pp. 363–390.
  External Links: ISSN 1432-1122,
  [Document](https://dx.doi.org/10.1007/s00780-024-00528-2),
  [Link](https://doi.org/10.1007/s00780-024-00528-2)
  Cited by: [§1.1](#S1.SS1.p2.2 "1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [§1.1](#S1.SS1.p3.6 "1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [§1.1](#S1.SS1.p4.7 "1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [§1.2](#S1.SS2.p1.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [§2.1](#S2.SS1.p1.2 "2.1 Properties and Technical Discussions ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* T. Fissler and S. M. Pesenti (2023)
  Sensitivity measures based on scoring functions.
  European Journal of Operational Research 307 (3),  pp. 1408–1423.
  External Links: ISSN 0377-2217,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.ejor.2022.10.002),
  [Link](https://www.sciencedirect.com/science/article/pii/S0377221722007718)
  Cited by: [§1.2](#S1.SS2.p3.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* H. Föllmer and A. Schied (2002)
  Convex measures of risk and trading constraints.
  Finance and Stochastics 6 (4),  pp. 429–447.
  External Links: ISSN 0949-2984,
  [Document](https://dx.doi.org/10.1007/s007800200072),
  [Link](https://doi.org/10.1007/s007800200072)
  Cited by: [§1.2](#S1.SS2.p1.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* M. Frittelli and E. Rosazza Gianin (2002)
  Putting order in risk measures.
  Journal of Banking & Finance 26 (7),  pp. 1473–1486.
  External Links: ISSN 0378-4266,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/S0378-4266%2802%2900270-4),
  [Link](https://www.sciencedirect.com/science/article/pii/S0378426602002704)
  Cited by: [§1.2](#S1.SS2.p1.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* I. Gilboa and D. Schmeidler (1989)
  Maxmin expected utility with a non-unique prior.
  Journal of Mathematical Economics 18,  pp. 141–153.
  Cited by: [§1.2](#S1.SS2.p1.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* A. A. Gomez, G. Consigli, and J. Liu (2024)
  Multi-period portfolio selection with interval-based conditional Value-at-Risk.
  Annals of Operations Research.
  External Links: ISSN 1572-9338,
  [Document](https://dx.doi.org/10.1007/s10479-024-05913-w),
  [Link](https://doi.org/10.1007/s10479-024-05913-w)
  Cited by: [§1.2](#S1.SS2.p3.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* V. Jokhadze and W. M. Schmidt (2020)
  Measuring model risk in financial risk management and pricing.
  International Journal of Theoretical and Applied Finance 23 (02),  pp. 2050012.
  External Links: [Document](https://dx.doi.org/10.1142/S0219024920500120),
  [Link](https://doi.org/10.1142/S0219024920500120),
  https://doi.org/10.1142/S0219024920500120
  Cited by: [§1.2](#S1.SS2.p2.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* E. Jouini, W. Schachermayer, and N. Touzi (2006)
  Law invariant risk measures have the fatou property.
  In Advances in Mathematical Economics,
   pp. 49–71.
  External Links: ISBN 978-4-431-34342-4,
  [Document](https://dx.doi.org/10.1007/4-431-34342-3%5F4),
  [Link](https://doi.org/10.1007/4-431-34342-3_4)
  Cited by: [Proof of Theorem 2.](#Ax1.24.p10.2 "Proof of Theorem 2. ‣ Appendix: Proofs ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [§2.3](#S2.SS3.p13.1 "2.3 WGRM under a Continuous Setting ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* P. Klibanoff, M. Marinacci, and S. Mukerji (2005)
  A smooth model of decision making under uncertainty.
  Econometrica 73 (3),  pp. 1849–1892.
  Cited by: [§1.2](#S1.SS2.p2.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* S. Kou, X. Peng, and C. C. Heyde (2013)
  External risk measures and basel accords.
  Mathematics of Operations Research 38 (3),  pp. 393–417.
  External Links: [Document](https://dx.doi.org/10.1287/moor.1120.0577),
  [Link](https://doi.org/10.1287/moor.1120.0577),
  https://doi.org/10.1287/moor.1120.0577
  Cited by: [§1.2](#S1.SS2.p4.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [§2.2](#S2.SS2.p3.3 "2.2 WGRM under a Discrete Setting ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* S. Kou and X. Peng (2016)
  On the measurement of economic tail risk.
  Operations Research 64 (5),  pp. 1056–1072.
  External Links: [Document](https://dx.doi.org/10.1287/opre.2016.1539),
  [Link](https://doi.org/10.1287/opre.2016.1539),
  https://doi.org/10.1287/opre.2016.1539
  Cited by: [§1.1](#S1.SS1.p2.2 "1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [§1.2](#S1.SS2.p4.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [§2.2](#S2.SS2.p3.3 "2.2 WGRM under a Discrete Setting ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* D. La Torre and M. Rocca (2024)
  Distributionally robust multiobjective optimization with application to risk measure theory.
  Annals of Operations Research.
  External Links: ISSN 1572-9338,
  [Document](https://dx.doi.org/10.1007/s10479-024-06401-x),
  [Link](https://doi.org/10.1007/s10479-024-06401-x)
  Cited by: [§1.2](#S1.SS2.p3.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* F. Liu and R. Wang (2021)
  A theory for measures of tail risk.
  Mathematics of Operations Research 46 (3),  pp. 1109–1128.
  External Links: [Document](https://dx.doi.org/10.1287/moor.2020.1072),
  [Link](https://doi.org/10.1287/moor.2020.1072),
  https://doi.org/10.1287/moor.2020.1072
  Cited by: [§1.2](#S1.SS2.p1.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* A. J. McNeil, R. Frey, and P. Embrechts (2015)
  Quantitative risk management: concepts, techniques and tools.
  Revised edition edition, Princeton series in finance, Princeton University Press, Princeton Oxford (eng).
  External Links: ISBN 9780691166278
  Cited by: [Example 1](#Thmexample1.p1.13 "Example 1. ‣ 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* R. T. Rockafellar and S. Uryasev (2013)
  The fundamental risk quadrangle in risk management, optimization and statistical estimation.
  Surveys in Operations Research and Management Science 18 (1),  pp. 33–53.
  External Links: ISSN 1876-7354,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.sorms.2013.03.001)
  Cited by: [Figure 1](#S1.F1 "In 1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [Figure 1](#S1.F1.3.2 "In 1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [§1.1](#S1.SS1.p5.1 "1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [§3.2](#S3.SS2.p4.1 "3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [§3](#S3.p1.1 "3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* R. T. Rockafellar (1970)
  Convex analysis.
   Princeton University Press, Princeton.
  External Links: [Link](https://doi.org/10.1515/9781400873173),
  [Document](https://dx.doi.org/doi%3A10.1515/9781400873173),
  ISBN 9781400873173
  Cited by: [Proof of Theorem 2.](#Ax1.16.p4.1 "Proof of Theorem 2. ‣ Appendix: Proofs ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [Proof of Theorem 1.](#Ax1.2.p2.20 "Proof of Theorem 1. ‣ Appendix: Proofs ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* P. P. Wakker (2010)
  Prospect theory: for risk and ambiguity.
   Cambridge University Press.
  Cited by: [§1.2](#S1.SS2.p1.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* R. Wang and J. F. Ziegel (2021)
  Scenario-based risk evaluation.
  Finance and Stochastics 25 (4),  pp. 725–756.
  External Links: ISSN 1432-1122,
  [Document](https://dx.doi.org/10.1007/s00780-021-00460-9),
  [Link](https://doi.org/10.1007/s00780-021-00460-9)
  Cited by: [§1.1](#S1.SS1.p2.2 "1.1 Background and Motivation ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [§1.2](#S1.SS2.p2.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* R. Wang and R. Zitikis (2021)
  An axiomatic foundation for the expected shortfall.
  Management Science 67 (3),  pp. 1413–1429.
  External Links: [Document](https://dx.doi.org/10.1287/mnsc.2020.3617),
  [Link](https://doi.org/10.1287/mnsc.2020.3617),
  https://doi.org/10.1287/mnsc.2020.3617
  Cited by: [§1.2](#S1.SS2.p3.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* S. Zhu and M. Fukushima (2009)
  Worst-case conditional value-at-risk with application to robust portfolio management.
  Operations Research 57 (5),  pp. 1155–1168.
  External Links: [Document](https://dx.doi.org/10.1287/opre.1080.0684),
  [Link](https://doi.org/10.1287/opre.1080.0684),
  https://doi.org/10.1287/opre.1080.0684
  Cited by: [§1.2](#S1.SS2.p1.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"),
  [Example 2](#Thmexample2.p1.9 "Example 2. ‣ 4 Optimization under WGRM and WRQ ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").
* S. Zymler, D. Kuhn, and B. Rustem (2013)
  Worst-case value at risk of nonlinear portfolios.
  Management Science 59 (1),  pp. 172–188.
  External Links: ISSN 00251909, 15265501,
  [Link](http://www.jstor.org/stable/23359612)
  Cited by: [§1.2](#S1.SS2.p1.1 "1.2 Connection to Other Frameworks and Contribution ‣ 1 Introduction ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").

## Appendix: Proofs

###### Proof of Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 2.2 WGRM under a Discrete Setting ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").

The “if” statement can be checked directly. We only focus on the “only if” statement.

(1) Step 1: Dual representation via an auxiliary convex function. We first define an auxiliary function:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g​(Φ𝒬,X):\displaystyle g(\Phi\_{\mathcal{Q},X}): | =f​(Φ𝒬,X)+δ​(Φ𝒬,X|𝒞)∈(−∞,∞],Φ𝒬,X∈ℝn,\displaystyle=f(\Phi\_{\mathcal{Q},X})+\delta(\Phi\_{\mathcal{Q},X}|\mathcal{C})\in(-\infty,\infty],\quad\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}, |  | (22) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | δ​(Φ𝒬,X|𝒞)\displaystyle\delta(\Phi\_{\mathcal{Q},X}|\mathcal{C}) | ={0,if​Φ𝒬,X∈𝒞,∞,if​Φ𝒬,X∉𝒞.\displaystyle=\begin{cases}0,&\text{if}\,\,\Phi\_{\mathcal{Q},X}\in\mathcal{C},\\ \infty,&\text{if}\,\,\Phi\_{\mathcal{Q},X}\notin\mathcal{C}.\end{cases} |  | (23) |

Obviously, g​(Φ𝒬,X)=f​(Φ𝒬,X)g(\Phi\_{\mathcal{Q},X})=f(\Phi\_{\mathcal{Q},X}) on 𝒞\mathcal{C}. Since f​(Φ𝒬,X)f(\Phi\_{\mathcal{Q},X}) satisfies (B1)-(B2), it is easy to verify that g​(Φ𝒬,X)g(\Phi\_{\mathcal{Q},X}) also satisfies positive homogeneity, translation invariance, and monotonicity.
Moreover, we can further verify that g​(Φ𝒬,X)g(\Phi\_{\mathcal{Q},X}) is also sub-additive, i.e., g​(Φ𝒬,X+Φ𝒬,Y)⩽g​(Φ𝒬,X)+g​(Φ𝒬,Y)g(\Phi\_{\mathcal{Q},X}+\Phi\_{\mathcal{Q},Y})\leqslant g(\Phi\_{\mathcal{Q},X})+g(\Phi\_{\mathcal{Q},Y}), for any Φ𝒬,X,Φ𝒬,Y∈ℝn\Phi\_{\mathcal{Q},X},\Phi\_{\mathcal{Q},Y}\in\mathbb{R}^{n}. Note that if Φ𝒬,X,Φ𝒬,Y∈𝒞\Phi\_{\mathcal{Q},X},\Phi\_{\mathcal{Q},Y}\in\mathcal{C}, then the inequality is valid by the comonotonic sub-additivity of ff. If Φ𝒬,X\Phi\_{\mathcal{Q},X} or Φ𝒬,Y∉𝒞\Phi\_{\mathcal{Q},Y}\notin\mathcal{C}, then the right-hand side of Eq.([22](#Ax1.E22 "In Proof of Theorem 1. ‣ Appendix: Proofs ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) goes to infinity due to δ​(Φ𝒬,X|𝒞)\delta(\Phi\_{\mathcal{Q},X}|\mathcal{C}). The positive homogeneity and sub-additivity indicate convexity of gg.
Furthermore, since f​(⋅)<∞f(\cdot)<\infty, we have dom​g:={Φ𝒬,X∈ℝn∣g​(Φ𝒬,X)<∞}≠∅\text{dom}\,g:=\{\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}\mid g(\Phi\_{\mathcal{Q},X})<\infty\}\neq\emptyset, i.e., g​(⋅)g(\cdot) is proper. From the fact that f​(⋅)f(\cdot) is Lipschitz continuous with respect to the maximum-norm ∥⋅∥∞\|\cdot\|\_{\infty} and 𝒞\mathcal{C} is a closed convex set, g​(⋅)g(\cdot) is lower semi-continuous (l.s.c.). By Fenchel-Moreau Biconjugation Theorem (Chapter 12, Rockafellar ([1970](#bib.bib33 "Convex analysis"))), it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(Φ𝒬,X)=supμ𝒬∈ℝn{⟨μ𝒬,Φ𝒬,X⟩−g∗​(μ𝒬)},Φ𝒬,X∈ℝn,\displaystyle g(\Phi\_{\mathcal{Q},X})=\sup\limits\_{\mu\_{\mathcal{Q}}\in\mathbb{R}^{n}}\{\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}\right\rangle-g^{\*}(\mu\_{\mathcal{Q}})\},\quad\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}, |  | (24) |

where g∗:ℝn→(−∞,∞]g^{\*}:\mathbb{R}^{n}\to(-\infty,\infty], g∗​(μ𝒬)=supΦ𝒬,X∈ℝn{⟨μ𝒬,Φ𝒬,X⟩−g​(Φ𝒬,X)}g^{\*}(\mu\_{\mathcal{Q}})=\sup\limits\_{\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}}\{\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}\right\rangle-g(\Phi\_{\mathcal{Q},X})\}, for μ𝒬=(μ1,μ2,…,μn)T∈ℝn\mu\_{\mathcal{Q}}=(\mu\_{1},\mu\_{2},\dots,\mu\_{n})^{T}\in\mathbb{R}^{n}, is the dual function of g​(⋅)g(\cdot).

Step 2: Structure of the conjugate and characterization of the weight set.
Next we investigate the characteristic of dom​g∗\text{dom}\,g^{\*}. First, since ∀k∈ℝ\forall\,k\in\mathbb{R}, k​𝟏∈𝒞k\mathbf{1}\in\mathcal{C}, by translation invariance, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | g∗​(μ𝒬)\displaystyle g^{\*}(\mu\_{\mathcal{Q}}) | =supΦ𝒬,X∈ℝn{⟨μ𝒬,Φ𝒬,X⟩−g​(Φ𝒬,X)}⩾supk∈ℝ{⟨μ𝒬,k​𝟏⟩−g​(k​𝟏)}={⟨μ𝒬,𝟏⟩−g​(𝟏)}⋅supk∈ℝk.\displaystyle=\sup\limits\_{\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}}\{\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}\right\rangle-g(\Phi\_{\mathcal{Q},X})\}\geqslant\sup\limits\_{k\in\mathbb{R}}\{\left\langle\mu\_{\mathcal{Q}},k\mathbf{1}\right\rangle-g(k\mathbf{1})\}=\{\left\langle\mu\_{\mathcal{Q}},\mathbf{1}\right\rangle-g(\mathbf{1})\}\cdot\sup\limits\_{k\in\mathbb{R}}k. |  |

If ⟨μ𝒬,𝟏⟩−g​(𝟏)=⟨μ𝒬,𝟏⟩−f​(𝟏)=0\left\langle\mu\_{\mathcal{Q}},\mathbf{1}\right\rangle-g(\mathbf{1})=\left\langle\mu\_{\mathcal{Q}},\mathbf{1}\right\rangle-f(\mathbf{1})=0, i.e., ∑i=1nμi=1\sum\_{i=1}^{n}\mu\_{i}=1, we have g∗​(μ𝒬)⩾0g^{\*}(\mu\_{\mathcal{Q}})\geqslant 0. Alternatively, if ⟨μ𝒬,𝟏⟩−g​(𝟏)≠0\left\langle\mu\_{\mathcal{Q}},\mathbf{1}\right\rangle-g(\mathbf{1})\neq 0, i.e., ∑i=1nμi≠1\sum\_{i=1}^{n}\mu\_{i}\neq 1, we have g∗​(μ𝒬)=∞g^{\*}(\mu\_{\mathcal{Q}})=\infty, since kk is arbitrary. This indicates that g​(μ𝒬)g(\mu\_{\mathcal{Q}}) is non-negative and that dom​g∗⊆{μ𝒬∈ℝn|∑i=1nμi=1}\text{dom}\,g^{\*}\subseteq\{\mu\_{\mathcal{Q}}\in\mathbb{R}^{n}\,|\,\sum^{n}\_{i=1}\mu\_{i}=1\}. Second, by positive homogeneity,

|  |  |  |  |
| --- | --- | --- | --- |
|  | g∗​(μ𝒬)\displaystyle g^{\*}(\mu\_{\mathcal{Q}}) | =supΦ𝒬,X∈ℝn{⟨μ𝒬,Φ𝒬,X⟩−g​(Φ𝒬,X)}=supΦ𝒬,X∈ℝna​{1a​⟨μ𝒬,Φ𝒬,X⟩−1a​g​(Φ𝒬,X)}\displaystyle=\sup\limits\_{\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}}\{\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}\right\rangle-g(\Phi\_{\mathcal{Q},X})\}=\sup\limits\_{\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}}a\ \{\frac{1}{a}\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}\right\rangle-\frac{1}{a}g(\Phi\_{\mathcal{Q},X})\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =a​supΦ𝒬,X/a∈ℝn{⟨μ𝒬,1a​Φ𝒬,X⟩−g​(1a​Φ𝒬,X)}=a​g∗​(μ𝒬),\displaystyle=a\sup\limits\_{\Phi\_{\mathcal{Q},X}/a\,\in\mathbb{R}^{n}}\{\langle\mu\_{\mathcal{Q}},\frac{1}{a}\Phi\_{\mathcal{Q},X}\rangle-g(\frac{1}{a}\Phi\_{\mathcal{Q},X})\}=ag^{\*}(\mu\_{\mathcal{Q}}), |  |

for arbitrary a⩾0a\geqslant 0. This indicates that if g∗​(μ𝒬)<∞g^{\*}(\mu\_{\mathcal{Q}})<\infty, it must hold that g∗​(μ𝒬)=0g^{\*}(\mu\_{\mathcal{Q}})=0. Combining the above two claims, we can conclude that

|  |  |  |  |
| --- | --- | --- | --- |
|  | g∗(μ𝒬)=δ(⋅|domg∗)andg(Φ𝒬,X)=supμ𝒬∈dom​g∗⟨μ𝒬,Φ𝒬,X⟩,\displaystyle g^{\*}(\mu\_{\mathcal{Q}})=\delta(\cdot|\text{dom}\,g^{\*})\quad\text{and}\quad g(\Phi\_{\mathcal{Q},X})=\sup\limits\_{\mu\_{\mathcal{Q}}\in\text{dom}\,g^{\*}}\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}\right\rangle, |  | (25) |

where the second equation of ([25](#Ax1.E25 "In Proof of Theorem 1. ‣ Appendix: Proofs ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) yields from the fact that, when μ𝒬∉dom​g∗\mu\_{\mathcal{Q}}\notin\text{dom}\,g^{\*}, we have g∗​(μ𝒬)=∞g^{\*}(\mu\_{\mathcal{Q}})=\infty, implying that g​(Φ𝒬,X)=−∞g(\Phi\_{\mathcal{Q},X})=-\infty.

Define the set of maximizers at Φ𝒬,X\Phi\_{\mathcal{Q},X} of Eq.([24](#Ax1.E24 "In Proof of Theorem 1. ‣ Appendix: Proofs ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) as ∂g​(Φ𝒬,X)\partial g(\Phi\_{\mathcal{Q},X}), i.e., ∂g​(Φ𝒬,X):={μ𝒬∈dom​g∗∣g​(Φ𝒬,X)+g∗​(μ𝒬)=⟨μ𝒬,Φ𝒬,X⟩}\partial g(\Phi\_{\mathcal{Q},X}):=\{\mu\_{\mathcal{Q}}\in\text{dom}\,g^{\*}\mid g(\Phi\_{\mathcal{Q},X})+g^{\*}(\mu\_{\mathcal{Q}})=\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}\right\rangle\}.
It can be shown that ∀Φ𝒬,X∈int​𝒞\forall\,\Phi\_{\mathcal{Q},X}\in\text{int}\mathcal{C}, ∂g​(Φ𝒬,X)≠∅\partial g(\Phi\_{\mathcal{Q},X})\neq\emptyset.
Now, fix any Φ𝒬,X∈int​𝒞\Phi\_{\mathcal{Q},X}\in\text{int}\mathcal{C} and let μ𝒬∈∂g​(Φ𝒬,X)\mu\_{\mathcal{Q}}\in\partial g(\Phi\_{\mathcal{Q},X}).
From Eq.([25](#Ax1.E25 "In Proof of Theorem 1. ‣ Appendix: Proofs ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")), we know that g​(Φ𝒬,X)=⟨μ𝒬,Φ𝒬,X⟩g(\Phi\_{\mathcal{Q},X})=\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}\right\rangle holds. Let 𝐞1,𝐞2,…,𝐞n\mathbf{e}\_{1},\mathbf{e}\_{2},\dots,\mathbf{e}\_{n} be the canonical basis of ℝn\mathbb{R}^{n}.
Since Φ𝒬,X∈int​𝒞\Phi\_{\mathcal{Q},X}\in\text{int}\mathcal{C}, for each ii, there exists an ε>0\varepsilon>0 small enough such that Φ𝒬,X−ε​𝐞i∈𝒞\Phi\_{\mathcal{Q},X}-\varepsilon\mathbf{e}\_{i}\in\mathcal{C}. Note that μ𝒬\mu\_{\mathcal{Q}} is an element of ∂g​(Φ𝒬,X)\partial g(\Phi\_{\mathcal{Q},X}), but it does not necessarily indicate μ𝒬∈∂g​(Φ𝒬,X−ε​𝐞i)\mu\_{\mathcal{Q}}\in\partial g(\Phi\_{\mathcal{Q},X}-\varepsilon\mathbf{e}\_{i}) as well. Therefore, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨μ𝒬,Φ𝒬,X−ε​𝐞i⟩⩽g​(Φ𝒬,X−ε​𝐞i)⩽g​(Φ𝒬,X)=⟨μ𝒬,Φ𝒬,X⟩,\displaystyle\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}-\varepsilon\mathbf{e}\_{i}\right\rangle\leqslant g(\Phi\_{\mathcal{Q},X}-\varepsilon\mathbf{e}\_{i})\leqslant g(\Phi\_{\mathcal{Q},X})=\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}\right\rangle, |  | (26) |

where the second inequality of ([26](#Ax1.E26 "In Proof of Theorem 1. ‣ Appendix: Proofs ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) results from monotonicity of gg. Equivalently, ⟨μ𝒬,−ε​𝐞i⟩⩽0\left\langle\mu\_{\mathcal{Q}},-\varepsilon\mathbf{e}\_{i}\right\rangle\leqslant 0, i.e., −𝐞i​μi⩽0-\mathbf{e}\_{i}\mu\_{i}\leqslant 0, μi⩾0\mu\_{i}\geqslant 0, which indicates that all coordinates of μ𝒬\mu\_{\mathcal{Q}} are non-negative. Since g∗g^{\*} is l.s.c. (as gg is l.s.c.), the set 𝒲1:=dom ​g∗⊆𝒟\mathcal{W}\_{1}:=\text{dom\,}g^{\*}\subseteq\mathcal{D} is closed and convex. To sum up, so far we have obtained that

|  |  |  |
| --- | --- | --- |
|  | g​(Φ𝒬,X)=supμ𝒬∈𝒲1⟨μ𝒬,Φ𝒬,X⟩,∀Φ𝒬,X∈int​𝒞.\displaystyle g(\Phi\_{\mathcal{Q},X})=\sup\limits\_{\mu\_{\mathcal{Q}}\in\mathcal{W}\_{1}}\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}\right\rangle,\quad\forall\,\Phi\_{\mathcal{Q},X}\in\text{int}\mathcal{C}. |  |

Step 3: Extension to the boundary and final representation.
For any boundary point Φ𝒬,X\Phi\_{\mathcal{Q},X} of 𝒞\mathcal{C}, we could choose a sequence {Φ𝒬,Xk}⊂int​𝒞\{\Phi\_{\mathcal{Q},X}^{k}\}\subset\text{int}\mathcal{C} converging to Φ𝒬,X\Phi\_{\mathcal{Q},X}. Then by the Lipschitz continuity of ff and the fact that g​(Φ𝒬,X)=f​(Φ𝒬,X)g(\Phi\_{\mathcal{Q},X})=f(\Phi\_{\mathcal{Q},X}) on 𝒞\mathcal{C}, we have f​(Φ𝒬,X)=supμ𝒬∈𝒲1⟨μ𝒬,Φ𝒬,X⟩f(\Phi\_{\mathcal{Q},X})=\sup\limits\_{\mu\_{\mathcal{Q}}\in\mathcal{W}\_{1}}\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}\right\rangle.
Finally, since f​(Φ𝒬,X)f(\Phi\_{\mathcal{Q},X}) is permutation invariant and Φ𝒬,Xq∈𝒞\Phi\_{\mathcal{Q},X}^{q}\in\mathcal{C} for every Φ𝒬,X∈ℝn\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}, we have

|  |  |  |
| --- | --- | --- |
|  | f​(Φ𝒬,X)=f​(Φ𝒬,Xq)=g​(Φ𝒬,Xq)=supμ𝒬∈𝒲1⟨μ𝒬,Φ𝒬,Xq⟩,∀Φ𝒬,X∈ℝn.\displaystyle f(\Phi\_{\mathcal{Q},X})=f(\Phi\_{\mathcal{Q},X}^{q})=g(\Phi\_{\mathcal{Q},X}^{q})=\sup\limits\_{\mu\_{\mathcal{Q}}\in\mathcal{W}\_{1}}\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}^{q}\right\rangle,\quad\forall\,\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}. |  |

(2) Since now f​(Φ𝒬,X)f(\Phi\_{\mathcal{Q},X}) is assumed to be sub-additive, it is directly convex along with properties of positive homogeneity, translation invariance, and monotonicity. From Part (1), we immediately have

|  |  |  |
| --- | --- | --- |
|  | f​(Φ𝒬,X)=supμ𝒬∈dom ​f∗{⟨μ𝒬,Φ𝒬,X⟩−f∗​(μ𝒬)},Φ𝒬,X∈ℝn,\displaystyle f(\Phi\_{\mathcal{Q},X})=\sup\limits\_{\mu\_{\mathcal{Q}}\in\text{dom\,}f^{\*}}\left\{\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}\right\rangle-f^{\*}(\mu\_{\mathcal{Q}})\right\},\quad\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | f∗​(μ𝒬)=supΦ𝒬,X∈ℝn{⟨μ𝒬,Φ𝒬,X⟩−f​(Φ𝒬,X)},\displaystyle f^{\*}(\mu\_{\mathcal{Q}})=\sup\limits\_{\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}}\left\{\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}\right\rangle-f(\Phi\_{\mathcal{Q},X})\right\}, |  |

and dom ​f∗⊆𝒟\text{dom\,}f^{\*}\subseteq\mathcal{D}. We first note that for any π∈Sn\pi\in S\_{n}, μ𝒬π∈dom​g∗\mu\_{\mathcal{Q}}^{\pi}\in\text{dom}\,g^{\*} and Φ𝒬,X∈ℝn\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}, there exists a unique inverse permutation π−1\pi^{-1} (since permutations are bijections) for permuted μ𝒬π\mu\_{\mathcal{Q}}^{\pi} such that ⟨μ𝒬π,Φ𝒬,X⟩=⟨μ𝒬,Φ𝒬,Xπ−1⟩\left\langle\mu\_{\mathcal{Q}}^{\pi},\Phi\_{\mathcal{Q},X}\right\rangle=\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}^{\pi^{-1}}\right\rangle. Therefore, it is evident that

|  |  |  |  |
| --- | --- | --- | --- |
|  | f∗​(μ𝒬π)=supΦ𝒬,X∈ℝn{⟨μ𝒬π,Φ𝒬,X⟩−f​(Φ𝒬,X)}=supΦ𝒬,Xπ−1∈ℝn{⟨μ𝒬,Φ𝒬,Xπ−1⟩−f​(Φ𝒬,Xπ−1)}=f∗​(μ𝒬).\displaystyle f^{\*}(\mu\_{\mathcal{Q}}^{\pi})=\sup\limits\_{\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}}\left\{\left\langle\mu\_{\mathcal{Q}}^{\pi},\Phi\_{\mathcal{Q},X}\right\rangle-f(\Phi\_{\mathcal{Q},X})\right\}=\sup\limits\_{\Phi\_{\mathcal{Q},X}^{\pi^{-1}}\in\mathbb{R}^{n}}\left\{\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}^{\pi^{-1}}\right\rangle-f(\Phi\_{\mathcal{Q},X}^{\pi^{-1}})\right\}=f^{\*}(\mu\_{\mathcal{Q}}). |  | (27) |

The second equality of ([27](#Ax1.E27 "In Proof of Theorem 1. ‣ Appendix: Proofs ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) is valid due to the permutation invariance of f​(Φ𝒬,X)f(\Phi\_{\mathcal{Q},X}), i.e., f​(Φ𝒬,X)=f​(Φ𝒬,Xπ−1)f(\Phi\_{\mathcal{Q},X})=f(\Phi\_{\mathcal{Q},X}^{\pi^{-1}}). The above relationship implies that dom​g∗\text{dom}\,g^{\*} is also permutation invariant. Moreover, since f​(Φ𝒬,X)=supμ𝒬∈𝒲1⟨μ𝒬,Φ𝒬,Xq⟩f(\Phi\_{\mathcal{Q},X})=\sup\limits\_{\mu\_{\mathcal{Q}}\in\mathcal{W}\_{1}}\left\langle\mu\_{\mathcal{Q}},\Phi\_{\mathcal{Q},X}^{q}\right\rangle, where Φ𝒬,Xq\Phi\_{\mathcal{Q},X}^{q} is non-decreasingly ordered, the Rearrangement Inequality implies that the supremum would be attained when μ𝒬\mu\_{\mathcal{Q}} is also non-decreasingly ordered. Therefore, 𝒲2⊆𝒟∩𝒞\mathcal{W}\_{2}\subseteq\mathcal{D}\,\cap\,\mathcal{C}.
∎

###### Proof of Proposition [1](#Thmproposition1 "Proposition 1. ‣ 2.2 WGRM under a Discrete Setting ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").

The “if” statement is direct. We only focus on the “only if” statement.

(1) Proof for f:𝒞→ℝf:\mathcal{C}\to\mathbb{R} satisfying (B1), (B2), (B6).
Since ff satisfies (B1) positive homogeneity and translation invariance, setting a=0a=0 and b=0b=0 yields f​(𝟎)=0f(\mathbf{0})=0. Note that the intersection of 𝒞\mathcal{C} and its negative cone satisfies 𝒞∩−𝒞={c𝟏∣c∈ℝ,𝟏=(1,1,…,1)T∈ℝn}\mathcal{C}\cap-\mathcal{C}=\{c\mathbf{1}\mid c\in\mathbb{R},\mathbf{1}=(1,1,\dots,1)^{T}\in\mathbb{R}^{n}\}. For any c∈ℝc\in\mathbb{R}, the constant vectors c​𝟏c\mathbf{1} and −c​𝟏-c\mathbf{1} are comonotonic. Then by (B6) comonotonic additivity, it holds that 0=f​(𝟎)=f​(c​𝟏−c​𝟏)=f​(c​𝟏)+f​(−c​𝟏)0=f(\mathbf{0})=f(c\mathbf{1}-c\mathbf{1})=f(c\mathbf{1})+f(-c\mathbf{1}). Combined with (B1) positive homogeneity, ff is fully homogeneous over ℝ\mathbb{R} on 𝒞\mathcal{C}.
Since 𝒞\mathcal{C} is a convex cone and ff satisfies comonotonic additivity and full homogeneity, ff is linear on 𝒞\mathcal{C}. By the Hahn-Banach Extension Theorem, there exists a unique linear extension f^:ℝn→ℝ\hat{f}:\mathbb{R}^{n}\to\mathbb{R} such that f^​(Φ𝒬,X)=f​(Φ𝒬,X)\hat{f}(\Phi\_{\mathcal{Q},X})=f(\Phi\_{\mathcal{Q},X}) for all Φ𝒬,X∈𝒞\Phi\_{\mathcal{Q},X}\in\mathcal{C}.
By the Riesz Representation Theorem, there exists a unique vector μ𝒬∗∈ℝn\mu\_{\mathcal{Q}}^{\*}\in\mathbb{R}^{n} such that f^​(Φ𝒬,X)=⟨μ𝒬∗,Φ𝒬,X⟩\hat{f}(\Phi\_{\mathcal{Q},X})=\left\langle\mu\_{\mathcal{Q}}^{\*},\Phi\_{\mathcal{Q},X}\right\rangle for all Φ𝒬,X∈ℝn\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}; hence f​(Φ𝒬,X)=⟨μ𝒬∗,Φ𝒬,X⟩f(\Phi\_{\mathcal{Q},X})=\left\langle\mu\_{\mathcal{Q}}^{\*},\Phi\_{\mathcal{Q},X}\right\rangle for all Φ𝒬,X∈𝒞\Phi\_{\mathcal{Q},X}\in\mathcal{C}.
Finally, (B1) translation invariance enforces ⟨μ𝒬∗,𝟏⟩=1\left\langle\mu\_{\mathcal{Q}}^{\*},\mathbf{1}\right\rangle=1, and (B2) monotonicity requires μi∗⩾0\mu\_{i}^{\*}\geqslant 0 for all ii. Thus, we have μ𝒬∗∈𝒟\mu\_{\mathcal{Q}}^{\*}\in\mathcal{D}.

(2) Proof for f:ℝn→ℝf:\mathbb{R}^{n}\to\mathbb{R} satisfying (B1), (B2), (B4), (B6).
From Part (1), for any ordered risk vector Φ𝒬,Xq∈𝒞\Phi\_{\mathcal{Q},X}^{q}\in\mathcal{C}, there exists a unique μ𝒬∗∈𝒟\mu\_{\mathcal{Q}}^{\*}\in\mathcal{D} such that f​(Φ𝒬,Xq)=⟨μ𝒬∗,Φ𝒬,Xq⟩f(\Phi\_{\mathcal{Q},X}^{q})=\left\langle\mu\_{\mathcal{Q}}^{\*},\Phi\_{\mathcal{Q},X}^{q}\right\rangle.
For any unordered risk vector Φ𝒬,X∉𝒞\Phi\_{\mathcal{Q},X}\notin\mathcal{C}, (B4) permutation invariance guarantees that f​(Φ𝒬,X)=f​(Φ𝒬,Xπ)f(\Phi\_{\mathcal{Q},X})=f(\Phi\_{\mathcal{Q},X}^{\pi}) for any permutation π∈Sn\pi\in S\_{n}. By definition, there exists a permutation π∗\pi^{\*} such that Φ𝒬,Xπ∗=Φ𝒬,Xq∈𝒞\Phi\_{\mathcal{Q},X}^{\pi^{\*}}=\Phi\_{\mathcal{Q},X}^{q}\in\mathcal{C}, where Φ𝒬,Xq\Phi\_{\mathcal{Q},X}^{q} is the non-decreasingly sorted version of Φ𝒬,X\Phi\_{\mathcal{Q},X}. Thus, it holds that f​(Φ𝒬,X)=f​(Φ𝒬,Xq)=⟨μ𝒬∗,Φ𝒬,Xq⟩.f(\Phi\_{\mathcal{Q},X})=f(\Phi\_{\mathcal{Q},X}^{q})=\left\langle\mu\_{\mathcal{Q}}^{\*},\Phi\_{\mathcal{Q},X}^{q}\right\rangle. The uniqueness of μ𝒬∗\mu\_{\mathcal{Q}}^{\*} follows directly from Part (1).

(3) Proof for f:ℝn→ℝf:\mathbb{R}^{n}\to\mathbb{R} satisfying (B1), (B2), (B6’).
(B6’) additivity and (B1) positive homogeneity imply that ff is a linear functional on ℝn\mathbb{R}^{n}. By the Riesz Representation Theorem, there exists a unique μ𝒬∗∈ℝn\mu\_{\mathcal{Q}}^{\*}\in\mathbb{R}^{n} such that f​(Φ𝒬,X)=⟨μ𝒬∗,Φ𝒬,X⟩f(\Phi\_{\mathcal{Q},X})=\left\langle\mu\_{\mathcal{Q}}^{\*},\Phi\_{\mathcal{Q},X}\right\rangle for all Φ𝒬,X∈ℝn\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}.
As in Part (1), translation invariance and monotonicity enforce μ𝒬∗∈𝒟\mu\_{\mathcal{Q}}^{\*}\in\mathcal{D}.

(4) Proof for f:ℝn→ℝf:\mathbb{R}^{n}\to\mathbb{R} satisfying (B1), (B2), (B4), (B6’).
From Part (3), we have f​(Φ𝒬,X)=⟨μ𝒬∗,Φ𝒬,X⟩f(\Phi\_{\mathcal{Q},X})=\left\langle\mu\_{\mathcal{Q}}^{\*},\Phi\_{\mathcal{Q},X}\right\rangle for all Φ𝒬,X∈ℝn\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}, with μ𝒬∗∈𝒟\mu\_{\mathcal{Q}}^{\*}\in\mathcal{D}.
(B4) permutation invariance requires that for any permutation π∈Sn\pi\in S\_{n} and any Φ𝒬,X∈ℝn\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}, it holds that ⟨μ𝒬∗,Φ𝒬,X⟩=⟨μ𝒬∗,Φ𝒬,Xπ⟩.\left\langle\mu\_{\mathcal{Q}}^{\*},\Phi\_{\mathcal{Q},X}\right\rangle=\left\langle\mu\_{\mathcal{Q}}^{\*},\Phi\_{\mathcal{Q},X}^{\pi}\right\rangle. Rewriting the right-hand side using permutation properties yields ⟨μ𝒬∗,Φ𝒬,Xπ⟩=⟨μ𝒬∗π−1,Φ𝒬,X⟩\left\langle\mu\_{\mathcal{Q}}^{\*},\Phi\_{\mathcal{Q},X}^{\pi}\right\rangle=\left\langle\mu\_{\mathcal{Q}}^{\*\pi^{-1}},\Phi\_{\mathcal{Q},X}\right\rangle, where μ𝒬∗π−1\mu\_{\mathcal{Q}}^{\*\pi^{-1}} denotes the weight vector obtained by permuting μ𝒬∗\mu\_{\mathcal{Q}}^{\*} with the inverse permutation π−1\pi^{-1}.
For this equality to hold for all Φ𝒬,X∈ℝn\Phi\_{\mathcal{Q},X}\in\mathbb{R}^{n}, it is necessary that μ𝒬∗=μ𝒬∗π−1\mu\_{\mathcal{Q}}^{\*}=\mu\_{\mathcal{Q}}^{\*\pi^{-1}} for all π∈Sn\pi\in S\_{n}. The only permutation-invariant vector in 𝒟\mathcal{D} is the uniform weight vector, i.e., μ𝒬∗=(1n,1n,…,1n)T.\mu\_{\mathcal{Q}}^{\*}=\left(\frac{1}{n},\frac{1}{n},\dots,\frac{1}{n}\right)^{T}.

∎

###### Proof of Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 2.3 WGRM under a Continuous Setting ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").

The “if” statement can be checked directly. We only focus on the “only if” statement.

(1) Step 1: Dual representation via an auxiliary convex function. Let 𝒞~={φX∈L∞​([0,1])∣φX​ is non-decreasing and left-continuous}\tilde{\mathcal{C}}=\{\varphi\_{X}\in L^{\infty}([0,1])\mid\varphi\_{X}\text{ is non-decreasing and left-continuous}\} be a cone of monotone functions. For any φX∈L∞​([0,1])\varphi\_{X}\in L^{\infty}([0,1]), its quantile function φXq\varphi\_{X}^{q} clearly belongs to 𝒞~\tilde{\mathcal{C}}. We first define an auxiliary function g:L∞​([0,1])→(−∞,∞]g:L^{\infty}([0,1])\to(-\infty,\infty] via:

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(φX):\displaystyle g(\varphi\_{X}): | =f​(φX)+δ​(φX|𝒞~),\displaystyle=f(\varphi\_{X})+\delta(\varphi\_{X}|\tilde{\mathcal{C}}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​(φX|𝒞~)\displaystyle\delta(\varphi\_{X}|\tilde{\mathcal{C}}) | ={0,if​φX∈𝒞~,∞,if​φX∉𝒞~.\displaystyle=\begin{cases}0,&\text{if}\,\,\varphi\_{X}\in\tilde{\mathcal{C}},\\ \infty,&\text{if}\,\,\varphi\_{X}\notin\tilde{\mathcal{C}}.\end{cases} |  |

The properness and convexity of g​(φX)g(\varphi\_{X}) can be established similarly to the discrete case. To establish the σ​(L∞,L1)\sigma(L^{\infty},L^{1})-lower semi-continuity of gg, which is equivalent to the Fatou property, we consider a uniformly bounded sequence {φXn}⊆L∞​([0,1])\{\varphi\_{X\_{n}}\}\subseteq L^{\infty}([0,1]) such that φXn→a.e.φX\varphi\_{X\_{n}}\xrightarrow{a.e.}\varphi\_{X}. We aim to show g​(φX)⩽lim infn→∞g​(φXn)g(\varphi\_{X})\leqslant\liminf\limits\_{n\to\infty}g(\varphi\_{X\_{n}}). If lim infn→∞g​(φXn)=∞\liminf\limits\_{n\to\infty}g(\varphi\_{X\_{n}})=\infty, the inequality holds trivially. Otherwise, if lim infn→∞g​(φXn)<∞\liminf\limits\_{n\to\infty}g(\varphi\_{X\_{n}})<\infty, then there exists a subsequence {φXnk}⊆𝒞~\{\varphi\_{X\_{n\_{k}}}\}\subseteq\tilde{\mathcal{C}} such that limk→∞g​(φXnk)=lim infn→∞g​(φXn)\lim\limits\_{k\to\infty}g(\varphi\_{X\_{n\_{k}}})=\liminf\limits\_{n\to\infty}g(\varphi\_{X\_{n}}). Since 𝒞~\tilde{\mathcal{C}} is closed under almost everywhere convergence (taking the left-continuous modification), the limit φX\varphi\_{X} also belongs to 𝒞~\tilde{\mathcal{C}}.
Thus, it suffices to show that f​(φX)⩽lim infk→∞f​(φXnk)f(\varphi\_{X})\leqslant\liminf\limits\_{k\to\infty}f(\varphi\_{X\_{n\_{k}}}), which is ensured by (C5).

###### Remark 8.

We emphasize the condition φXn→a.e.φX\varphi\_{X\_{n}}\xrightarrow{a.e.}\varphi\_{X} rather than convergence in the L∞L^{\infty}-norm to ensure the functional is compatible with the σ​(L∞,L1)\sigma(L^{\infty},L^{1}) topology. This continuity requirement forces the dual representation to lie strictly within L1​([0,1])L^{1}([0,1]), thereby eliminating the singular components (purely finitely additive measures) that are otherwise inherent in the general dual space (L∞)∗(L^{\infty})^{\*}.

Since gg is proper, convex and l.s.c., by the Fenchel-Moreau Biconjugation Theorem (Chapter 12, Rockafellar ([1970](#bib.bib33 "Convex analysis"))), it holds that

|  |  |  |
| --- | --- | --- |
|  | g​(φX)=supν∈L1​([0,1]){∫01φX​(t)​ν​(t)​dt−g∗​(ν)},\displaystyle g(\varphi\_{X})=\sup\limits\_{\nu\in L^{1}([0,1])}\left\{\int^{1}\_{0}\varphi\_{X}(t)\nu(t)\mathrm{d}t-g^{\*}(\nu)\right\}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | g∗​(ν)=supφX∈L∞​([0,1]){∫01φX​(t)​ν​(t)​dt−g​(φX)}.\displaystyle g^{\*}(\nu)=\sup\limits\_{\varphi\_{X}\in L^{\infty}([0,1])}\left\{\int^{1}\_{0}\varphi\_{X}(t)\nu(t)\mathrm{d}t-g(\varphi\_{X})\right\}. |  |

Step 2: Structure of the conjugate and characterization of the weight set.
Similar to the discrete case, we investigate the characteristic of dom ​g∗\text{dom }g^{\*}. First, for any k∈ℝk\in\mathbb{R}, the constant function φX​(t)≡k∈L∞​([0,1])\varphi\_{X}(t)\equiv k\in L^{\infty}([0,1]). By (C1) affine invariance, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | g∗​(ν)\displaystyle g^{\*}(\nu) | =supφX∈L∞​([0,1]){∫01φX​(t)​ν​(t)​dt−g​(φX)}\displaystyle=\sup\limits\_{\varphi\_{X}\in L^{\infty}([0,1])}\left\{\int^{1}\_{0}\varphi\_{X}(t)\nu(t)\mathrm{d}t-g(\varphi\_{X})\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩾supk∈ℝ{∫01k​𝟏[0,1]​ν​(t)​dt−g​(k​𝟏[0,1])}={∫01ν​(t)​dt−1}⋅supk∈ℝk.\displaystyle\geqslant\sup\limits\_{k\in\mathbb{R}}\left\{\int^{1}\_{0}k\mathbf{1}\_{[0,1]}\,\nu(t)\mathrm{d}t-g(k\mathbf{1}\_{[0,1]})\right\}=\left\{\int^{1}\_{0}\nu(t)\mathrm{d}t-1\right\}\cdot\sup\limits\_{k\in\mathbb{R}}k. |  |

If ∫01ν​(t)​dt=1\int^{1}\_{0}\nu(t)\mathrm{d}t=1, then we have g∗​(ν)⩾0g^{\*}(\nu)\geqslant 0. Otherwise, if ∫01ν​(t)​dt≠1\int^{1}\_{0}\nu(t)\mathrm{d}t\neq 1, then g∗​(ν)=∞g^{\*}(\nu)=\infty. This indicates dom​g∗⊆{ν∈L1​([0,1])|∫01ν​(t)​dt=1}\text{dom}\,g^{\*}\subseteq\{\nu\in L^{1}([0,1])|\int^{1}\_{0}\nu(t)\mathrm{d}t=1\}. Moreover, (C1) affine invariance also indicates

|  |  |  |  |
| --- | --- | --- | --- |
|  | g∗​(ν)\displaystyle g^{\*}(\nu) | =supφX∈L∞​([0,1]){∫01φX​(t)​ν​(t)​dt−g​(φX)}\displaystyle=\sup\limits\_{\varphi\_{X}\in L^{\infty}([0,1])}\left\{\int^{1}\_{0}\varphi\_{X}(t)\nu(t)\mathrm{d}t-g(\varphi\_{X})\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =k​supφX/k∈L∞​([0,1]){∫01φX​(t)k​ν​(t)​dt−g​(φXk)}=k​g∗​(ν),∀k∈ℝ+,\displaystyle=k\sup\limits\_{\varphi\_{X}/k\in L^{\infty}([0,1])}\left\{\int^{1}\_{0}\frac{\varphi\_{X}(t)}{k}\nu(t)\mathrm{d}t-g\left(\frac{\varphi\_{X}}{k}\right)\right\}=kg^{\*}(\nu),\quad\forall\,k\in\mathbb{R\_{+}}, |  |

which indicates that if g∗​(ν)<∞g^{\*}(\nu)<\infty, it must hold that g∗​(ν)=0g^{\*}(\nu)=0. That is, if ∫01ν​(t)​dt=1\int^{1}\_{0}\nu(t)\mathrm{d}t=1, we have g∗​(ν)=0g^{\*}(\nu)=0. By the above claims, it is evident that

|  |  |  |
| --- | --- | --- |
|  | g∗(ν)=δ(⋅|domg∗),g(φX)=supν∈dom​g∗∫01φX(t)ν(t)dt.\displaystyle g^{\*}(\nu)=\delta(\cdot|\text{dom}\,g^{\*}),\quad g(\varphi\_{X})=\sup\limits\_{\nu\in\text{dom}\,g^{\*}}\int^{1}\_{0}\varphi\_{X}(t)\nu(t)\mathrm{d}t. |  |

We next go on to prove that for each valid ν​(t)\nu(t), it holds that ν​(t)⩾0\nu(t)\geqslant 0 almost everywhere. Since g​(φX)g(\varphi\_{X}) is proper, convex and l.s.c., for any φX\varphi\_{X}, it is easy to verify the non-emptiness of its subdifferential, i.e., ∂g​(φX)≠∅\partial g(\varphi\_{X})\neq\emptyset. This indicates that for any φX∈𝒞~\varphi\_{X}\in\tilde{\mathcal{C}}, there exists ν∈dom​g∗\nu\in\text{dom}\,g^{\*} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀φ∈L∞​([0,1]),g​(φ)⩾g​(φX)+∫01(φ​(t)−φX​(t))​ν​(t)​dt.\displaystyle\forall\,\varphi\in L^{\infty}([0,1]),\quad g(\varphi)\geqslant g(\varphi\_{X})+\int^{1}\_{0}(\varphi(t)-\varphi\_{X}(t))\nu(t)\mathrm{d}t. |  | (28) |

We first define another auxiliary set

|  |  |  |
| --- | --- | --- |
|  | 𝒞~0={φX∈𝒞~∣∃δ>0​ such that ​φX​(t)−φX​(s)⩾δ​(t−s),∀ 0⩽s<t⩽1},\displaystyle\tilde{\mathcal{C}}\_{0}=\left\{\varphi\_{X}\in\tilde{\mathcal{C}}\mid\exists\,\delta>0\text{\,such that\,}\varphi\_{X}(t)-\varphi\_{X}(s)\geqslant\delta(t-s),\forall\,0\leqslant s<t\leqslant 1\right\}, |  |

which consists of strictly increasing functions with a uniform positive lower bound on the slope. We proceed by arising two lemmas.

###### Lemma 1.

Let φX∈𝒞~0\varphi\_{X}\in\tilde{\mathcal{C}}\_{0} with φX​(t)−φX​(s)⩾δ​(t−s),∀ 0⩽s<t⩽1\varphi\_{X}(t)-\varphi\_{X}(s)\geqslant\delta(t-s),\forall\,0\leqslant s<t\leqslant 1. Let ϕ:[0,1]→ℝ\phi:[0,1]\to\mathbb{R} be a smooth function satisfying

(1) ϕ⩾0\phi\geqslant 0 on [0,1][0,1],

(2) ϕ\phi is supported on the interval [c,d]⊆(0,1)[c,d]\subseteq(0,1),

(3) ∥ϕ′∥∞⩽Kϕ\|\phi\prime\|\_{\infty}\leqslant K\_{\phi} for some constant Kϕ>0K\_{\phi}>0.

Then for all 0<ε<δ/Kϕ0<\varepsilon<\delta/K\_{\phi}, the function φε​(t)=φX​(t)−ε​ϕ​(t)\varphi^{\varepsilon}(t)=\varphi\_{X}(t)-\varepsilon\phi(t) belongs to 𝒞~\tilde{\mathcal{C}}.

###### Proof.

For any s<ts<t, φε​(t)−φε​(s)=[φX​(t)−φX​(s)]−ε​[ϕ​(t)−ϕ​(s)]\varphi^{\varepsilon}(t)-\varphi^{\varepsilon}(s)=[\varphi\_{X}(t)-\varphi\_{X}(s)]-\varepsilon[\phi(t)-\phi(s)]. Since |ϕ​(t)−ϕ​(s)|⩽Kϕ​(t−s)|\phi(t)-\phi(s)|\leqslant K\_{\phi}(t-s) by property (3) and φX​(t)−φX​(s)⩾δ​(t−s)\varphi\_{X}(t)-\varphi\_{X}(s)\geqslant\delta(t-s) by definition, it holds that

|  |  |  |
| --- | --- | --- |
|  | φε​(t)−φε​(s)⩾δ​(t−s)−ε​Kϕ​(t−s)=(δ−ε​Kϕ)​(t−s)>0\displaystyle\varphi^{\varepsilon}(t)-\varphi^{\varepsilon}(s)\geqslant\delta(t-s)-\varepsilon K\_{\phi}(t-s)=(\delta-\varepsilon K\_{\phi})(t-s)>0 |  |

when ε<δ/Kϕ\varepsilon<\delta/K\_{\phi}. Hence φε\varphi^{\varepsilon} is strictly increasing, and therefore φε∈𝒞~\varphi^{\varepsilon}\in\tilde{\mathcal{C}}.
∎

###### Lemma 2.

For any φX∈𝒞~0\varphi\_{X}\in\tilde{\mathcal{C}}\_{0} and any ν∈∂g​(φX)∩dom ​g∗\nu\in\partial g(\varphi\_{X})\cap\text{dom\,}g^{\*}, we have ν​(t)⩾0\nu(t)\geqslant 0 a.e.

###### Proof.

Let φX∈𝒞~0\varphi\_{X}\in\tilde{\mathcal{C}}\_{0} with minimum slope δ>0\delta>0. Fix any interval [c,d]⊆(0,1)[c,d]\subseteq(0,1), and let ϕ⩾0\phi\geqslant 0 be a smooth function supported on [c,d][c,d] with ∥ϕ′∥∞⩽Kϕ\|\phi\prime\|\_{\infty}\leqslant K\_{\phi}. For ε<δ/Kϕ\varepsilon<\delta/K\_{\phi}, we define φε=φX−ε​ϕ\varphi^{\varepsilon}=\varphi\_{X}-\varepsilon\phi. By Lemma [1](#Thmlemma1 "Lemma 1. ‣ Proof of Theorem 2. ‣ Appendix: Proofs ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"), we have φε∈𝒞~\varphi^{\varepsilon}\in\tilde{\mathcal{C}}. Since ν∈∂g​(φX)\nu\in\partial g(\varphi\_{X}), the subdifferential inequality in ([28](#Ax1.E28 "In Proof of Theorem 2. ‣ Appendix: Proofs ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) gives

|  |  |  |
| --- | --- | --- |
|  | g​(φε)⩾g​(φX)+∫01(φε​(t)−φX​(t))​ν​(t)​dt=g​(φX)−ε​∫01ϕ​(t)​ν​(t)​dt.\displaystyle g(\varphi^{\varepsilon})\geqslant g(\varphi\_{X})+\int^{1}\_{0}(\varphi^{\varepsilon}(t)-\varphi\_{X}(t))\nu(t)\mathrm{d}t=g(\varphi\_{X})-\varepsilon\int^{1}\_{0}\phi(t)\nu(t)\mathrm{d}t. |  |

Since φε​(t)=φX​(t)−ε​ϕ​(t)⩽φX​(t)\varphi^{\varepsilon}(t)=\varphi\_{X}(t)-\varepsilon\phi(t)\leqslant\varphi\_{X}(t) and φε,φX∈𝒞~\varphi^{\varepsilon},\varphi\_{X}\in\tilde{\mathcal{C}}, by (C2) pointwise monotonicity, we have g​(φε)⩽g​(φX)g(\varphi^{\varepsilon})\leqslant g(\varphi\_{X}). Combining the above claims yields

|  |  |  |
| --- | --- | --- |
|  | ∞>g​(φX)⩾g​(φε)⩾g​(φX)−ε​∫01ϕ​(t)​ν​(t)​dt,\displaystyle\infty>g(\varphi\_{X})\geqslant g(\varphi^{\varepsilon})\geqslant g(\varphi\_{X})-\varepsilon\int^{1}\_{0}\phi(t)\nu(t)\mathrm{d}t, |  |

which implies ε​∫01ϕ​(t)​ν​(t)​dt⩾0\varepsilon\int^{1}\_{0}\phi(t)\nu(t)\mathrm{d}t\geqslant 0, i.e., ∫01ϕ​(t)​ν​(t)​dt⩾0\int^{1}\_{0}\phi(t)\nu(t)\mathrm{d}t\geqslant 0. Since this relationship holds true for any smooth function ϕ\phi supported on any interval [c,d]⊆(0,1)[c,d]\subseteq(0,1), we conclude that ν​(t)⩾0\nu(t)\geqslant 0 holds almost everywhere on (0,1)(0,1), and hence almost everywhere on [0,1][0,1].
∎

Step 3: Extension to the boundary and final representation.
Since g∗g^{\*} is l.s.c. (as gg is σ​(L∞,L1)\sigma(L^{\infty},L^{1})-lower semi-continuous), the set 𝒲3:=dom ​g∗⊆{ν∈L1​([0,1])|∫01ν​(t)​dt=1,ν​(t)⩾0​a.e.}\mathcal{W}\_{3}:=\text{dom\,}g^{\*}\subseteq\{\nu\in L^{1}([0,1])|\int^{1}\_{0}\nu(t)\mathrm{d}t=1,\nu(t)\geqslant 0\ \text{a.e.}\} is closed and convex. By Lemma [2](#Thmlemma2 "Lemma 2. ‣ Proof of Theorem 2. ‣ Appendix: Proofs ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"), we immediately have

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(φX)=f​(φX)=supν∈𝒲3∫01φX​(t)​ν​(t)​dt,∀φX∈𝒞~0.\displaystyle g(\varphi\_{X})=f(\varphi\_{X})=\sup\limits\_{\nu\in\mathcal{W}\_{3}}\int\_{0}^{1}\varphi\_{X}(t)\nu(t)\mathrm{d}t,\quad\forall\,\varphi\_{X}\in\tilde{\mathcal{C}}\_{0}. |  | (29) |

For any function outside 𝒞~0\tilde{\mathcal{C}}\_{0}, i.e., φX∈𝒞~∖𝒞~0\varphi\_{X}\in\tilde{\mathcal{C}}\setminus\tilde{\mathcal{C}}\_{0}, we can always choose a sequence {φXk}∈𝒞~0\{\varphi\_{X\_{k}}\}\in\tilde{\mathcal{C}}\_{0} converging to φX\varphi\_{X}. For example, choosing φXk​(t)=φX​(t)+t/k\varphi\_{X\_{k}}(t)=\varphi\_{X}(t)+t/k for t∈[0,1]t\in[0,1], where k∈ℕk\in\mathbb{N} is always valid. Note that for identity map id​(t)=t\text{id}(t)=t, t∈[0,1]t\in[0,1], it holds that f​(id)⩽f​(𝟏[0,1])<∞f(\text{id})\leqslant f(\mathbf{1}\_{[0,1]})<\infty. Then by the fact that

|  |  |  |
| --- | --- | --- |
|  | f​(φX)⩽f​(φXk)⩽f​(φX)+f​(id)k,\displaystyle f(\varphi\_{X})\leqslant f(\varphi\_{X\_{k}})\leqslant f(\varphi\_{X})+\frac{f(\text{id})}{k}, |  |

we have f​(φXk)→f​(φX)f(\varphi\_{X\_{k}})\to f(\varphi\_{X}) when k→∞k\to\infty.
Then the relationship Eq.([29](#Ax1.E29 "In Proof of Theorem 2. ‣ Appendix: Proofs ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) is valid in the entire C~\tilde{C}.

Finally, by the (C4) strong permutation invariance, we can extend the result outside 𝒞~\tilde{\mathcal{C}}:

|  |  |  |
| --- | --- | --- |
|  | f​(φX)=f​(φXq)=g​(φXq)=supν∈𝒲3∫01φXq​(t)​ν​(t)​dt,∀φX∈L∞​([0,1]).\displaystyle f(\varphi\_{X})=f(\varphi^{q}\_{X})=g(\varphi^{q}\_{X})=\sup\limits\_{\nu\in\mathcal{W}\_{3}}\int^{1}\_{0}\varphi^{q}\_{X}(t)\nu(t)\mathrm{d}t,\quad\forall\,\varphi\_{X}\in L^{\infty}([0,1]). |  |

(2) The idea is very similar as in the discrete case. By assumptions, it is straightforward to check that ff is proper and convex. The lower semi-continuity of ff is a corollary of Theorem 2.2 in Jouini et al. ([2006](#bib.bib23 "Law invariant risk measures have the fatou property")). Then from the above proof, we have

|  |  |  |
| --- | --- | --- |
|  | f​(φX)=supν∈dom ​f∗{∫01ν​(t)​φX​(t)​dt−f∗​(ν)},\displaystyle f(\varphi\_{X})=\sup\_{\nu\in\text{dom }f^{\*}}\left\{\int\_{0}^{1}\nu(t)\varphi\_{X}(t)\mathrm{d}t-f^{\*}(\nu)\right\}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | f∗​(ν)=supφX∈L∞​([0,1]){∫01ν​(t)​φX​(t)​dt−f​(φX)},\displaystyle f^{\*}(\nu)=\sup\_{\varphi\_{X}\in L^{\infty}([0,1])}\left\{\int\_{0}^{1}\nu(t)\varphi\_{X}(t)\mathrm{d}t-f(\varphi\_{X})\right\}, |  |

and dom​f∗⊆{ν∈L1​([0,1])∣∫01ν​(t)​dt=1,ν​(t)⩾0​a.e.}\text{dom}\,f^{\*}\subseteq\{\nu\in L^{1}([0,1])\mid\int^{1}\_{0}\nu(t)\mathrm{d}t=1,\nu(t)\geqslant 0\ \text{a.e.}\}.
Note that for any measure-preserving transformations TT, ν∈dom​f∗\nu\in\text{dom}\,f^{\*} and φX∈L∞​([0,1])\varphi\_{X}\in L^{\infty}([0,1]), there must exist an inverse measure-preserving transformations T−1T^{-1} such that ∫01(ν∘T​(t))​φX​(t)​dt=∫01ν​(t)​(φX∘T−1​(t))​dt\int\_{0}^{1}(\nu\circ T(t))\varphi\_{X}(t)\mathrm{d}t=\int\_{0}^{1}\nu(t)(\varphi\_{X}\circ T^{-1}(t))\mathrm{d}t, which directly implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | f∗​(ν∘T)\displaystyle f^{\*}(\nu\circ T) | =supφX∈L∞​([0,1]){∫01(ν∘T​(t))​φX​(t)​dt−f​(φX)}\displaystyle=\sup\_{\varphi\_{X}\in L^{\infty}([0,1])}\left\{\int\_{0}^{1}(\nu\circ T(t))\varphi\_{X}(t)\mathrm{d}t-f(\varphi\_{X})\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =supφX∘T−1∈L∞​([0,1]){∫01ν​(t)​(φX∘T−1​(t))​dt−f​(φ∘T−1)}=f∗​(ν).\displaystyle=\sup\_{\varphi\_{X}\circ T^{-1}\in L^{\infty}([0,1])}\left\{\int\_{0}^{1}\nu(t)(\varphi\_{X}\circ T^{-1}(t))\mathrm{d}t-f(\varphi\circ T^{-1})\right\}=f^{\*}(\nu). |  |

The second equality is valid due to the strong permutation invariance of ff. The above relationship implies that dom ​f∗\text{dom }f^{\*} also satisfies strong permutation invariance. Thus it is reasonable to restrict 𝒲4:=dom ​f∗⊆{ν∈L∞​([0,1])∣∫01ν​(t)​dt=1,ν​(t)⩾0​a.e.,ν​ is non-decreasing}\mathcal{W}\_{4}:=\text{dom }f^{\*}\subseteq\{\nu\in L^{\infty}([0,1])\mid\int^{1}\_{0}\nu(t)\mathrm{d}t=1,\nu(t)\geqslant 0\ \text{a.e.},\ \nu\text{ is non-decreasing}\}.

∎

###### Proof of Proposition [3](#Thmproposition3 "Proposition 3. ‣ 2.3 WGRM under a Continuous Setting ‣ 2 Weighted Generalized Risk Measures ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").

The “if” statement is direct. We only focus on the “only if” statement.

(1) Proof for f:𝒞^→ℝf:\hat{\mathcal{C}}\to\mathbb{R} satisfying (D1), (D2), (D3), and (D5).
By (D3) comonotonic additivity, we have f​(φX1+φX2)=f​(φX1)+f​(φX2)f(\varphi\_{X\_{1}}+\varphi\_{X\_{2}})=f(\varphi\_{X\_{1}})+f(\varphi\_{X\_{2}}) for any φX1,φX2∈𝒞^\varphi\_{X\_{1}},\varphi\_{X\_{2}}\in\hat{\mathcal{C}}.

Define V=span​(𝒞^)⊆L1​([0,1])V=\text{span}(\hat{\mathcal{C}})\subseteq L^{1}([0,1]), the linear span of 𝒞^\hat{\mathcal{C}}. For any φ=φX1−φX2\varphi=\varphi\_{X\_{1}}-\varphi\_{X\_{2}} with φX1,φX2∈𝒞^\varphi\_{X\_{1}},\varphi\_{X\_{2}}\in\hat{\mathcal{C}}, we define f^​(φ)=f​(φX1)−f​(φX2)\hat{f}(\varphi)=f(\varphi\_{X\_{1}})-f(\varphi\_{X\_{2}}). To verify that f^\hat{f} is well-defined, suppose φX1−φX2=φX3−φX4\varphi\_{X\_{1}}-\varphi\_{X\_{2}}=\varphi\_{X\_{3}}-\varphi\_{X\_{4}}, i.e., φX1+φX4=φX2+φX3\varphi\_{X\_{1}}+\varphi\_{X\_{4}}=\varphi\_{X\_{2}}+\varphi\_{X\_{3}}. By (D3) comonotonic additivity, we have

|  |  |  |
| --- | --- | --- |
|  | f​(φX1)+f​(φX4)=f​(φX1+φX4)=f​(φX2+φX3)=f​(φX2)+f​(φX3),\displaystyle f(\varphi\_{X\_{1}})+f(\varphi\_{X\_{4}})=f(\varphi\_{X\_{1}}+\varphi\_{X\_{4}})=f(\varphi\_{X\_{2}}+\varphi\_{X\_{3}})=f(\varphi\_{X\_{2}})+f(\varphi\_{X\_{3}}), |  |

which implies f​(φX1)−f​(φX2)=f​(φX3)−f​(φX4)f(\varphi\_{X\_{1}})-f(\varphi\_{X\_{2}})=f(\varphi\_{X\_{3}})-f(\varphi\_{X\_{4}}). Thus, f^\hat{f} is uniquely defined on VV.
By definition, f^\hat{f} is linear on VV. With (D5) L1L^{1}-continuity, we have

|  |  |  |
| --- | --- | --- |
|  | |f^​(φ)|=|f​(φX1)−f​(φX2)|⩽M​‖φX1−φX2‖L1=M​‖φ‖L1,\displaystyle|\hat{f}(\varphi)|=|f(\varphi\_{X\_{1}})-f(\varphi\_{X\_{2}})|\leqslant M\|\varphi\_{X\_{1}}-\varphi\_{X\_{2}}\|\_{L^{1}}=M\|\varphi\|\_{L^{1}}, |  |

confirming that f^\hat{f} is bounded (hence continuous) on VV.

A critical observation is that by the Jordan Decomposition Theorem, any function of bounded variation can be expressed as the difference of two non-decreasing functions. Thus, the set of bounded variation functions is a subset of VV. Since step functions (dense in L1​([0,1])L^{1}([0,1])) are of bounded variation, we know VV is dense in L1​([0,1])L^{1}([0,1]), i.e., V¯=L1​([0,1])\bar{V}=L^{1}([0,1]).

As a continuous linear functional on a dense subspace, f^\hat{f} admits a unique continuous linear extension f~:L1​([0,1])→ℝ\tilde{f}:L^{1}([0,1])\to\mathbb{R}. By the Riesz Representation Theorem for L1L^{1} Spaces, there exists a unique ν∗∈L∞​([0,1])\nu^{\*}\in L^{\infty}([0,1]) such that f~​(φX)=∫01φX​(t)​ν∗​(t)​dt,∀φX∈L1​([0,1])\tilde{f}(\varphi\_{X})=\int\_{0}^{1}\varphi\_{X}(t)\nu^{\*}(t)\mathrm{d}t,\forall\,\varphi\_{X}\in L^{1}([0,1]).
Restricting to 𝒞^\hat{\mathcal{C}}, we have f​(φX)=f~​(φX)=∫01g​(t)​ν∗​(t)​dtf(\varphi\_{X})=\tilde{f}(\varphi\_{X})=\int\_{0}^{1}g(t)\nu^{\*}(t)\mathrm{d}t.

Finally, (D1) affine invariance implies f​(𝟏[0,1])=1f(\mathbf{1}\_{[0,1]})=1, so ∫01ν∗​(t)​dt=1\int\_{0}^{1}\nu^{\*}(t)\mathrm{d}t=1. For any 0⩽c<d⩽10\leqslant c<d\leqslant 1, 𝟏(c,1]⩾𝟏(d,1]\mathbf{1}\_{(c,1]}\geqslant\mathbf{1}\_{(d,1]} implies f​(𝟏(c,1])⩾f​(𝟏(d,1])f(\mathbf{1}\_{(c,1]})\geqslant f(\mathbf{1}\_{(d,1]}) by (D2) Pointwise monotonicity, and hence ∫cdν∗​(t)​dt⩾0\int\_{c}^{d}\nu^{\*}(t)\mathrm{d}t\geqslant 0. The arbitrariness of cc and dd ensures ν∗​(t)⩾0\nu^{\*}(t)\geqslant 0 a.e. on [0,1][0,1].

(2) Proof for f:L1​([0,1])→ℝf:L^{1}([0,1])\to\mathbb{R} satisfying (D1), (D2), (D3), (D4), and (D5).
For any φX∈L1​([0,1])\varphi\_{X}\in L^{1}([0,1]), there exists a Lebesgue measure-preserving transformation TT such that φX=φXq∘T\varphi\_{X}=\varphi\_{X}^{q}\circ T. By (D4) strong permutation invariance, we have f​(φX)=f​(φXq∘T)=f​(φXq).f(\varphi\_{X})=f(\varphi\_{X}^{q}\circ T)=f(\varphi\_{X}^{q}).
Combining with the result from (1), we obtain f​(φX)=∫01φXq​(t)​ν∗​(t)​dt,∀φX∈L1​([0,1]).f(\varphi\_{X})=\int\_{0}^{1}\varphi\_{X}^{q}(t)\nu^{\*}(t)\mathrm{d}t,\forall\,\varphi\_{X}\in L^{1}([0,1]). Uniqueness of ν∗\nu^{\*} follows from (1).

(3) Proof for f:L1​([0,1])→ℝf:L^{1}([0,1])\to\mathbb{R} satisfying (D1), (D2), (D3’), and (D5).
(D1) affine invariance and (D3’) additivity directly imply ff is a linear functional on L1​([0,1])L^{1}([0,1]). By (D5) L1L^{1}-continuity, ff is bounded (i.e., ‖f‖(L1)∗⩽M\|f\|\_{(L^{1})^{\*}}\leqslant M). The Riesz Representation Theorem guarantees a unique ν∗∈L∞​([0,1])\nu^{\*}\in L^{\infty}([0,1]) such that f​(φX)=∫01φX​(t)​ν∗​(t)​dtf(\varphi\_{X})=\int\_{0}^{1}\varphi\_{X}(t)\nu^{\*}(t)\mathrm{d}t, ∀φX∈L1​([0,1]).\forall\,\varphi\_{X}\in L^{1}([0,1]). Normalization (∫01ν∗​(t)​dt=1\int\_{0}^{1}\nu^{\*}(t)\mathrm{d}t=1) and non-negativeness (ν∗​(t)⩾0\nu^{\*}(t)\geqslant 0 a.e.) follow from (D1) and (D2), respectively, as shown in (1).

(4) Proof for f:L1​([0,1])→ℝf:L^{1}([0,1])\to\mathbb{R} satisfying (D1), (D2), (D3’), (D4), and (D5). By Part (3) we know f​(φX)=∫01φX​(t)​ν∗​(t)​dtf(\varphi\_{X})=\int\_{0}^{1}\varphi\_{X}(t)\nu^{\*}(t)\mathrm{d}t holds for any φX∈L1​([0,1])\varphi\_{X}\in L^{1}([0,1]). For any φX∈L1​([0,1])\varphi\_{X}\in L^{1}([0,1]) and any measure-preserving transformation TT, by (D4) strong permutation invariance, we have ∫01φX​(t)​ν∗​(t)​dt=∫01(φX∘T​(t))​ν∗​(t)​dt\int\_{0}^{1}\varphi\_{X}(t)\nu^{\*}(t)\mathrm{d}t=\int\_{0}^{1}(\varphi\_{X}\circ T(t))\nu^{\*}(t)\mathrm{d}t. Note that for the measure-preserving transformation TT, there must exist an inverse transformation T−1T^{-1} such that ∫01(φX∘T​(t))​ν∗​(t)​dt=∫01φX​(t)​(ν∗∘T−1​(t))​dt\int\_{0}^{1}(\varphi\_{X}\circ T(t))\nu^{\*}(t)\mathrm{d}t=\int\_{0}^{1}\varphi\_{X}(t)(\nu^{\*}\circ T^{-1}(t))\mathrm{d}t, whcih further implies that ∫01φX​(t)​ν∗​(t)​dt=∫01φX​(t)​(ν∗∘T−1​(t))​dt\int\_{0}^{1}\varphi\_{X}(t)\nu^{\*}(t)\mathrm{d}t=\int\_{0}^{1}\varphi\_{X}(t)(\nu^{\*}\circ T^{-1}(t))\mathrm{d}t. Hence, we conclude that ν∗​(t)=ν∗​(T−1​(t))\nu^{\*}(t)=\nu^{\*}(T^{-1}(t)) for a.e. tt and any measure-preserving TT, which implies that ν∗​(t)\nu^{\*}(t) is constant almost everywhere. The normalization of ν∗\nu^{\*} forces the constant to be 11, i.e., ν∗​(t)≡1\nu^{\*}(t)\equiv 1 a.e.

∎

###### Proof of Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application").

We first prove that the measures in Eq.([17](#S3.E17 "In Theorem 3. ‣ 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) satisfy Eqs.([13](#S3.E13 "In 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application"))–([16](#S3.E16 "In 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")).
For Eq.([13](#S3.E13 "In 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼𝒬​[X]+𝒟𝒬​(X)\displaystyle\mathbb{E}\_{\mathcal{Q}}[X]+\mathcal{D}\_{\mathcal{Q}}(X) | =∫𝒬𝔼P​[X]​dμ𝒬​(P)+∫𝒬𝒟P​(X)​dμ𝒬​(P)=∫𝒬(𝔼P​[X]+𝒟P​(X))​dμ𝒬​(P)\displaystyle=\int\_{\mathcal{Q}}\mathbb{E}\_{P}[X]\mathrm{d}\mu\_{\mathcal{Q}}(P)+\int\_{\mathcal{Q}}\mathcal{D}\_{P}(X)\mathrm{d}\mu\_{\mathcal{Q}}(P)=\int\_{\mathcal{Q}}(\mathbb{E}\_{P}[X]+\mathcal{D}\_{P}(X))\mathrm{d}\mu\_{\mathcal{Q}}(P) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫𝒬ℛP​(X)​dμ𝒬​(P)=ℛ𝒬​(X),\displaystyle=\int\_{\mathcal{Q}}\mathcal{R}\_{P}(X)\mathrm{d}\mu\_{\mathcal{Q}}(P)=\mathcal{R}\_{\mathcal{Q}}(X), |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ𝒬​(X)−𝔼𝒬​[X]\displaystyle\mathcal{R}\_{\mathcal{Q}}(X)-\mathbb{E}\_{\mathcal{Q}}[X] | =∫𝒬ℛP​(X)​dμ𝒬​(P)−∫𝒬𝔼P​[X]​dμ𝒬​(P)=∫𝒬(ℛP​(X)−𝔼P​[X])​dμ𝒬​(P)\displaystyle=\int\_{\mathcal{Q}}\mathcal{R}\_{P}(X)\mathrm{d}\mu\_{\mathcal{Q}}(P)-\int\_{\mathcal{Q}}\mathbb{E}\_{P}[X]\mathrm{d}\mu\_{\mathcal{Q}}(P)=\int\_{\mathcal{Q}}(\mathcal{R}\_{P}(X)-\mathbb{E}\_{P}[X])\mathrm{d}\mu\_{\mathcal{Q}}(P) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫𝒬𝒟P​(X)​dμ𝒬​(P)=𝒟𝒬​(X).\displaystyle=\int\_{\mathcal{Q}}\mathcal{D}\_{P}(X)\mathrm{d}\mu\_{\mathcal{Q}}(P)=\mathcal{D}\_{\mathcal{Q}}(X). |  |

For Eq.([14](#S3.E14 "In 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼𝒬​[X]+ℰ𝒬​(X)\displaystyle\mathbb{E}\_{\mathcal{Q}}[X]+\mathcal{E}\_{\mathcal{Q}}(X) | =∫𝒬𝔼P​[X]​dμ𝒬​(P)+minb​(𝒬)⁡{∫𝒬ℰP​(X−b​(P))​dμ𝒬​(P)∣∫𝒬b​(P)​dμ𝒬​(P)=0}\displaystyle=\int\_{\mathcal{Q}}\mathbb{E}\_{P}[X]\mathrm{d}\mu\_{\mathcal{Q}}(P)+\min\_{b(\mathcal{Q})}\left\{\int\_{\mathcal{Q}}\mathcal{E}\_{P}(X-b(P))\mathrm{d}\mu\_{\mathcal{Q}}(P)\mid\int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =minb​(𝒬)⁡{∫𝒬(ℰP​(X−b​(P))+𝔼P​[X])​dμ𝒬​(P)∣∫𝒬b​(P)​dμ𝒬​(P)=0}\displaystyle=\min\_{b(\mathcal{Q})}\left\{\int\_{\mathcal{Q}}(\mathcal{E}\_{P}(X-b(P))+\mathbb{E}\_{P}[X])\mathrm{d}\mu\_{\mathcal{Q}}(P)\mid\int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =minb​(𝒬)⁡{∫𝒬(ℰP​(X−b​(P))+𝔼P​[X−b​(P)]+b​(P))​dμ𝒬​(P)∣∫𝒬b​(P)​dμ𝒬​(P)=0}\displaystyle=\min\_{b(\mathcal{Q})}\left\{\int\_{\mathcal{Q}}(\mathcal{E}\_{P}(X-b(P))+\mathbb{E}\_{P}[X-b(P)]+b(P))\mathrm{d}\mu\_{\mathcal{Q}}(P)\mid\int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =minb​(𝒬)⁡{∫𝒬(ℰP​(X−b​(P))+𝔼P​[X−b​(P)])​dμ𝒬​(P)+∫𝒬b​(P)​dμ𝒬​(P)∣∫𝒬b​(P)​dμ𝒬​(P)=0}\displaystyle=\min\_{b(\mathcal{Q})}\left\{\int\_{\mathcal{Q}}(\mathcal{E}\_{P}(X-b(P))+\mathbb{E}\_{P}[X-b(P)])\mathrm{d}\mu\_{\mathcal{Q}}(P)+\int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)\mid\int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =minb​(𝒬)⁡{∫𝒬𝒱P​(X−b​(P))​dμ𝒬​(P)∣∫𝒬b​(P)​dμ𝒬​(P)=0}\displaystyle=\min\_{b(\mathcal{Q})}\left\{\int\_{\mathcal{Q}}\mathcal{V}\_{P}(X-b(P))\mathrm{d}\mu\_{\mathcal{Q}}(P)\mid\int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝒱𝒬​(X),\displaystyle=\mathcal{V}\_{\mathcal{Q}}(X), |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱𝒬​(X)−𝔼𝒬​[X]\displaystyle\mathcal{V}\_{\mathcal{Q}}(X)-\mathbb{E}\_{\mathcal{Q}}[X] | =minb​(𝒬)⁡{∫𝒬(𝒱P​(X−b​(P))−𝔼P​[X−b​(P)+b​(P)])​dμ𝒬​(P)∣∫𝒬b​(P)​dμ𝒬​(P)=0}\displaystyle=\min\_{b(\mathcal{Q})}\left\{\int\_{\mathcal{Q}}(\mathcal{V}\_{P}(X-b(P))-\mathbb{E}\_{P}[X-b(P)+b(P)])\mathrm{d}\mu\_{\mathcal{Q}}(P)\mid\int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =minb​(𝒬)⁡{∫𝒬(𝒱P​(X−b​(P))−𝔼P​[X−b​(P)])​dμ𝒬​(P)−∫𝒬b​(P)​dμ𝒬​(P)∣∫𝒬b​(P)​dμ𝒬​(P)=0}\displaystyle=\min\_{b(\mathcal{Q})}\left\{\int\_{\mathcal{Q}}(\mathcal{V}\_{P}(X-b(P))-\mathbb{E}\_{P}[X-b(P)])\mathrm{d}\mu\_{\mathcal{Q}}(P)-\int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)\mid\int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =minb​(𝒬)⁡{∫𝒬ℰP​(X−b​(P))​dμ𝒬​(P)∣∫𝒬b​(P)​dμ𝒬​(P)=0}\displaystyle=\min\_{b(\mathcal{Q})}\left\{\int\_{\mathcal{Q}}\mathcal{E}\_{P}(X-b(P))\mathrm{d}\mu\_{\mathcal{Q}}(P)\mid\int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℰ𝒬​(X).\displaystyle=\mathcal{E}\_{\mathcal{Q}}(X). |  |

Then we move on Eqs.([15](#S3.E15 "In 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")) and ([16](#S3.E16 "In 3.2 Weighted Risk Quadrangle ‣ 3 Weighted Risk Quadrangle ‣ Weighted Generalized Risk Measure and Risk Quadrangle: Characterization, Optimization and Application")). We observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | c+𝒱𝒬​(X−c)\displaystyle c+\mathcal{V}\_{\mathcal{Q}}(X-c) | =c+minb​(𝒬)⁡{∫𝒬𝒱P​(X−c−b​(P))​dμ𝒬​(P)∣∫𝒬b​(P)​dμ𝒬​(P)=0}\displaystyle=c+\min\_{b(\mathcal{Q})}\left\{\int\_{\mathcal{Q}}\mathcal{V}\_{P}(X-c-b(P))\mathrm{d}\mu\_{\mathcal{Q}}(P)\mid\int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =minb​(𝒬)⁡{∫𝒬(𝒱P​(X−c−b​(P))+c+b​(P))​dμ𝒬​(P)∣∫𝒬b​(P)​dμ𝒬​(P)=0}.\displaystyle=\min\_{b(\mathcal{Q})}\left\{\int\_{\mathcal{Q}}\left(\mathcal{V}\_{P}(X-c-b(P))+c+b(P)\right)\mathrm{d}\mu\_{\mathcal{Q}}(P)\mid\int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0\right\}. |  |

For each P∈𝒬P\in\mathcal{Q}, the term 𝒱P​(X−c−b​(P))+c+b​(P)\mathcal{V}\_{P}(X-c-b(P))+c+b(P) attains its minimum if and only if c+b​(P)=𝒮P​(X)c+b(P)=\mathcal{S}\_{P}(X), where 𝒮P​(X)\mathcal{S}\_{P}(X) denotes the statistic of XX under probability measure PP. By the monotonicity of the integral operation under a fixed μ𝒬\mu\_{\mathcal{Q}}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | c+𝒱𝒬​(X−c)\displaystyle c+\mathcal{V}\_{\mathcal{Q}}(X-c) | ⩾∫𝒬(𝒱P​(X−𝒮P​(X))+𝒮P​(X))​dμ𝒬​(P)\displaystyle\geqslant\int\_{\mathcal{Q}}\left(\mathcal{V}\_{P}(X-\mathcal{S}\_{P}(X))+\mathcal{S}\_{P}(X)\right)\mathrm{d}\mu\_{\mathcal{Q}}(P) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫𝒬ℛP​(X)​dμ𝒬​(P)=ℛ𝒬​(X),\displaystyle=\int\_{\mathcal{Q}}\mathcal{R}\_{P}(X)\mathrm{d}\mu\_{\mathcal{Q}}(P)=\mathcal{R}\_{\mathcal{Q}}(X), |  |

with equality if and only if c+b​(P)=𝒮P​(X)c+b(P)=\mathcal{S}\_{P}(X) for all P∈𝒬P\in\mathcal{Q}. Combining this with the constraint ∫𝒬b​(P)​dμ𝒬​(P)=0\int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0, we immediately obtain:

|  |  |  |
| --- | --- | --- |
|  | c=∫𝒬(c+b​(P))​dμ𝒬​(P)=∫𝒬𝒮P​(X)​dμ𝒬​(P),c=\int\_{\mathcal{Q}}(c+b(P))\mathrm{d}\mu\_{\mathcal{Q}}(P)=\int\_{\mathcal{Q}}\mathcal{S}\_{P}(X)\mathrm{d}\mu\_{\mathcal{Q}}(P), |  |

which further implies that arg⁡minc⁡{c+𝒱𝒬​(X−c)}=𝒮𝒬​(X)\arg\min\_{c}\left\{c+\mathcal{V}\_{\mathcal{Q}}(X-c)\right\}=\mathcal{S}\_{\mathcal{Q}}(X).

Similarly, for the ℰ𝒬​(X−c)\mathcal{E}\_{\mathcal{Q}}(X-c) term, we have

|  |  |  |
| --- | --- | --- |
|  | ℰ𝒬​(X−c)=minb​(𝒬)⁡{∫𝒬ℰP​(X−c−b​(P))​dμ𝒬​(P)∣∫𝒬b​(P)​dμ𝒬​(P)=0}.\displaystyle\mathcal{E}\_{\mathcal{Q}}(X-c)=\min\_{b(\mathcal{Q})}\left\{\int\_{\mathcal{Q}}\mathcal{E}\_{P}(X-c-b(P))\mathrm{d}\mu\_{\mathcal{Q}}(P)\mid\int\_{\mathcal{Q}}b(P)\mathrm{d}\mu\_{\mathcal{Q}}(P)=0\right\}. |  |

By the same logic, for each P∈𝒬P\in\mathcal{Q}, ℰP​(X−c−b​(P))\mathcal{E}\_{P}(X-c-b(P)) attains its minimum if and only if c+b​(P)=𝒮P​(X)c+b(P)=\mathcal{S}\_{P}(X). From this, we can immediately derive that ℰ𝒬​(X−c)⩾𝒟𝒬​(X)\mathcal{E}\_{\mathcal{Q}}(X-c)\geqslant\mathcal{D}\_{\mathcal{Q}}(X), where equality holds if and only if c+B​(P)=𝒮P​(X)c+B(P)=\mathcal{S}\_{P}(X) for all P∈𝒬P\in\mathcal{Q}; this also implies arg⁡minc⁡{ℰ𝒬​(X−c)}=𝒮𝒬​(X)\arg\min\_{c}\left\{\mathcal{E}\_{\mathcal{Q}}(X-c)\right\}=\mathcal{S}\_{\mathcal{Q}}(X).

Next, if each paired (ℛP,𝒟P,𝒱P,ℰP)(\mathcal{R}\_{P},\mathcal{D}\_{P},\mathcal{V}\_{P},\mathcal{E}\_{P}) is regular, then it is straightforward to check that the corresponding (ℛ𝒬,𝒟𝒬,𝒱𝒬,ℰ𝒬)(\mathcal{R}\_{\mathcal{Q}},\mathcal{D}\_{\mathcal{Q}},\mathcal{V}\_{\mathcal{Q}},\mathcal{E}\_{\mathcal{Q}}) is also regular.

∎

BETA