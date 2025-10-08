---
authors:
- Martin Aichele
- Igor Cialenco
- Damian Jelito
- Marcin Pitera
doc_id: arxiv:2510.05809v1
family_id: arxiv:2510.05809
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Coherent estimation of risk measures
url_abs: http://arxiv.org/abs/2510.05809v1
url_html: https://arxiv.org/html/2510.05809v1
venue: arXiv q-fin
version: 1
year: 2025
---


Martin Aichele

Igor Cialenco

Damian Jelito

Marcin Pitera
European Central Bank, Sonnemannstraße 22, 60314 Frankfurt am Main, Germany
Department of Applied Mathematics, Illinois Institute of Technology, 10 W 32nd Str, Building REC, Room 220, Chicago, IL 60616, USA
Institute of Mathematics, Jagiellonian University, S. Łojasiewicza 6, 30-348 Kraków, Poland

###### Abstract

We develop a statistical framework for risk estimation, inspired by the axiomatic theory of risk measures. Coherent risk estimators—functionals of P&L samples inheriting the economic properties of risk measures—are defined and characterized through robust representations linked to LL-estimators. The framework provides a canonical methodology for constructing estimators with sound financial and statistical properties, unifying risk measure theory, principles for capital adequacy, and practical statistical challenges in market risk. A numerical study illustrates the approach, focusing on expected shortfall estimation under both i.i.d. and overlapping samples relevant for regulatory FRTB model applications.

###### keywords:

risk estimator , coherent risk estimator , estimation of risk measures , risk bias , estimation of risk , expected shortfall , value at risk , coherent risk measure , asymptotic properties of risk estimators , Basel framework , FRTB , IMA , market risk , regulatory capital model

###### MSC:

91G70 , 91B05 , 62G05

††journal: TBD

theorem]Definition
theorem]Proposition
theorem]Theorem
theorem]Corollary

## 1 Introduction

One of the main tasks of any financial institution is managing its risk, which can arise from regulatory requirements or from the need for internal monitoring and control. At the same time, financial regulatory bodies are mandated to establish legislative frameworks and procedures to assess and manage the risks faced by financial institutions, designed to ensure that financial institutions remain solvent under adverse scenarios or market conditions.
In either case, the fundamental problem is to design adequate risk measurement tools that can capture the unobservable, usually highly complex, financial risk profiles based on limited data.

The existing risk measurement methodologies, broadly speaking, have evolved along the following pathway. In the first step, we design a risk measure, say ρ\rho, under the assumption that the true law of the future’s profit and loss vector of a financial position (P&L), say XX, is known or can be found. The function ρ\rho maps the random variable XX to a real number ρ​(X)\rho(X), indicating how risky the underlying position is. In the second step, we estimate the risk of a financial position, say ρ^​(X)\hat{\rho}(X), assuming that the true distribution of XX is not known, and only a finite sample of XX is available. Among risk measures that are often used for the first step, one can mention the value at risk (VaR\operatorname{\mathrm{VaR}}) used as the primary metric for capital requirements under the Basel II market risk framework, or the expected shortfall (ES\operatorname{\mathrm{ES}}), adopted by the Basel Committee on Banking Supervision (BCBS) as part of the Basel III reforms, see BCBS [[2006](https://arxiv.org/html/2510.05809v1#bib.bib11), [2013](https://arxiv.org/html/2510.05809v1#bib.bib12), [2019](https://arxiv.org/html/2510.05809v1#bib.bib13)] for details. Unlike VaR\operatorname{\mathrm{VaR}}, which only specifies a quantile loss threshold, ES\operatorname{\mathrm{ES}} captures the average of extreme losses beyond the chosen confidence level, thereby addressing tail risk more effectively. For the second step, there are many well-known risk estimation frameworks linked, e.g., to historical simulation or Monte Carlo methods. We refer to McNeil et al. [[2010](https://arxiv.org/html/2510.05809v1#bib.bib47)] and Alexander [[2009](https://arxiv.org/html/2510.05809v1#bib.bib5)] for other examples of risk measures and an overview of the most popular estimation approaches.

In this work, we focus on the second step and adopt a novel perspective, fundamentally different from the existing literature, focused on the estimation function of ρ\rho, say ρ^\hat{\rho}, which is later used to estimate ρ^​(X)\hat{\rho}(X). We argue that, similar to the risk measures themselves, any estimation must also satisfy a set of desirable financial normative properties, postulated a priori, and in addition be a ”good approximation”111There is a subtle distinction between estimation and approximation. Estimation refers to inferring an unknown true value from limited data, with an emphasis on its statistical properties. Approximation, in contrast, involves simplifying a known value or formula to make it computationally tractable, while analyzing the resulting numerical error. Our approach in this work combines elements of both, but for consistency we refer to them jointly as estimation.. This approach is motivated by the recognition that risk quantification procedures serve primarily to determine capital reserves for mitigating exposures, rather than to provide mere approximations of intrinsic risk values. To this end, we introduce the notion of the coherent risk estimator (CRE) that maps actual P&L samples to real numbers, that is monotone, cash additive, positive homogeneous, and subadditive when applied to a sample X.

The properties imposed on CREs stem from the axiomatic risk measure framework of Artzner et al. [[1997](https://arxiv.org/html/2510.05809v1#bib.bib7), [1999](https://arxiv.org/html/2510.05809v1#bib.bib8)], which laid the foundation for the modern theory of risk measures. Each axiom encodes a financially and economically meaningful requirement–such as monotonicity with respect to losses to allow ordering of positions, cash-additivity to reflect a minimum capital requirement, positive homogeneity to capture the proportional scaling of risk in a rescaled portfolio, or subadditivity to account for diversification benefits; see Section [2](https://arxiv.org/html/2510.05809v1#S2 "2 Preliminaries ‣ Coherent estimation of risk measures") for precise definitions and further discussion.

Our key theoretical contribution is the development of the robust representations of all CREs, see Theorem [4.1](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem1 "Theorem 4.1 (Robust representation of CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"). Similar results are obtained for law-invariant222Similar to risk measures, a law-invariant CRE does not depend on the ordering of the input sample. See Definition [3.2](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem2 "Definition 3.2 (Law-invariant estimator). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures"). CREs, a sublcass of CREs. In fact, we prove that a CRE is law-invariant if and only if it can be represented as a supremum over a set of LL-estimators; see Theorem [4.2](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem2 "Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"). Moreover, assuming additionally that a CRE is also comonotonic, we show that it can be represented as an LL-estimator; see Theorem [4.10](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem10 "Theorem 4.10 (Robust representation of comonotonic and law-invariant CREs). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"). The importance of such results is evident. This approach provides a canonical framework for constructing risk estimators that are designed to possess the desired risk management properties. Furthermore, it enables not only the systematic selection of favorable estimators from the wide variety of existing alternatives, but also ensures that the chosen methods remain practically applicable, are integral, robust and distribution-free, and aligned with supervisory expectations, see e.g. ECB [[2025](https://arxiv.org/html/2510.05809v1#bib.bib31)]. Additionally, the strong connection between CREs and LL-estimators facilitates the leverage of the extensive statistical literature about LL-estimators and their various asymptotic properties, mostly applied to comonotonic and law-invariant CREs. Our approach also provides a fresh look on the robust representation theory for risk measures, in which the duality is build directly into the estimation formula rather than being imposed only on a theoretical risk metric level. Throughout the paper, we present various examples of CREs, with particular emphasis on estimators of ES\operatorname{\mathrm{ES}} and their properties, including a dedicated section comparing different ES\operatorname{\mathrm{ES}} estimators (see Section [6](https://arxiv.org/html/2510.05809v1#S6 "6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures")). We also discuss methods for constructing CREs for a given coherent risk measure using plug-in procedures, which recover estimators of several classical risk measures, including ES\operatorname{\mathrm{ES}}.

For completeness, let us comment how this paper is linked to other results from the risk representation and risk estimation literature, and provide more insight into the underlying regulatory and supervisory background.

First, we note there exists a vast literature on risk measure representation, developed from the ground up using an axiomatic approach, originally introduced in Artzner et al. [[1997](https://arxiv.org/html/2510.05809v1#bib.bib7)] and later extended to various setups; cf. Drapeau and Kupper [[2013](https://arxiv.org/html/2510.05809v1#bib.bib28)] for an overview of one step risk measures, and Bielecki et al. [[2024](https://arxiv.org/html/2510.05809v1#bib.bib19)] for dynamic setup. Within this approach, risk measures can be described in several equivalent ways, allowing both the construction of specific measures and the development of numerical approximation schemes for them. As far as we know, this theory, and consequent robust representations for specific families of risk measures, have not been transferred to risk estimation which is the core topic of this paper.

Second, as far as the estimation of ρ​(X)\rho(X) for a fixed ρ\rho and/or XX is considered, the general goal is to find a formula that is preferably simple and provides a ‘good estimate’ of the true, unknown value of ρ​(X)\rho(X) based on a statistical sample of size nn, say ρ^n​(X)\hat{\rho}\_{n}(X). A traditional method to build ρ^n​(X)\hat{\rho}\_{n}(X), is to approximate the distribution of XX, or the function ρ\rho, or a combination of both. A natural approach is to treat ρ^n​(X)\hat{\rho}\_{n}(X) as a statistical estimate of ρ​(X)\rho(X) and to study its properties as the sample size grows. This corresponds to asymptotic properties induces by the central limit theorem or estimation consistency analysis, i.e. property ρ^n​(X)→ρ​(X)\hat{\rho}\_{n}(X)\to\rho(X), as n→∞n\to\infty.
This approach traces back to Acerbi [[2002](https://arxiv.org/html/2510.05809v1#bib.bib2)], and we refer to the monograph McNeil et al. [[2010](https://arxiv.org/html/2510.05809v1#bib.bib47)] for a comprehensive literature review; see Bartl and Tangpi [[2023](https://arxiv.org/html/2510.05809v1#bib.bib10)] and Bartl and Eckstein [[2024](https://arxiv.org/html/2510.05809v1#bib.bib9)] for a more recent comprehensive discussions on contemporary methodologies. Here, we mention that for some classes of estimators that are also discussed in the present work, such as the empirical distribution plug-in estimators (see Section [3](https://arxiv.org/html/2510.05809v1#S3 "3 Coherent risk estimators ‣ Coherent estimation of risk measures") for precise definition), it was proved that they are consistent and satisfy a central limit theorem type convergence with usual rate n1/2n^{1/2}, cf. Belomestny and Krätschmer [[2012](https://arxiv.org/html/2510.05809v1#bib.bib16)] and some earlier works Weber [[2007](https://arxiv.org/html/2510.05809v1#bib.bib62)], Chen [[2008](https://arxiv.org/html/2510.05809v1#bib.bib23)], Beutner and Zähle [[2010](https://arxiv.org/html/2510.05809v1#bib.bib17)], but for some larger classes of risk measures, the convergence rate is not necessarily n1/2n^{1/2}, see Bartl and Tangpi [[2023](https://arxiv.org/html/2510.05809v1#bib.bib10)]. Within this approach, the authors typically also discuss properties of these estimators that are important from a financial perspective, although such considerations usually arise as a consequence rather than as an initial focus.

Third, in the regulatory Internal Model Approach (IMA) for Pillar I bank models, the 10-day VaR\operatorname{\mathrm{VaR}} and 10-day ES\operatorname{\mathrm{ES}} at the confidence levels α=1%\alpha=1\% and α=2.5%\alpha=2.5\%, respectively, are the key reference market risk capital metrics, see BCBS [[2006](https://arxiv.org/html/2510.05809v1#bib.bib11), [2019](https://arxiv.org/html/2510.05809v1#bib.bib13)] for details.333In most practical applications the confidence level α\alpha is set to 1%1\%, 2.5%2.5\%, or 5%5\%. Two main conventions are used when quoting confidence levels for VaR\operatorname{\mathrm{VaR}} and ES\operatorname{\mathrm{ES}}: the left-tail convention, adopted in this work and common in the risk measurement literature, and the right-tail convention, which reports thresholds of the form 1−α1-\alpha (e.g., 99%99\%, 97.5%97.5\%, 95%95\%) and is more widespread in risk management and regulatory practice, where the right tail represents losses. Although the risk measures themselves are fixed, regulatory and supervisory bodies rarely prescribe explicit estimation formulas. Two notable exceptions are the following locally implemented formulas used for Pillar I capital calculations: the minimal Stressed VaR formula under the Basel II framework [PRA, [2020](https://arxiv.org/html/2510.05809v1#bib.bib53), Article 10.2] and the EU Stress Scenario Risk Measure under the Basel III framework [EU, [2024b](https://arxiv.org/html/2510.05809v1#bib.bib34), Article 11]. More generally, regulatory and supervisory texts specify desired properties of estimators – such as conceptual soundness, proven backtesting track record, or distribution-free character – rather than their explicit form, see e.g. [ECB, [2025](https://arxiv.org/html/2510.05809v1#bib.bib31), Section 5.3], [PRA, [2020](https://arxiv.org/html/2510.05809v1#bib.bib53), Section 10], [CBUAE, [2023](https://arxiv.org/html/2510.05809v1#bib.bib22), Market Risk Standards & Risk Management Standards], or [HKMA, [2024](https://arxiv.org/html/2510.05809v1#bib.bib40), Section 4.5]. In practice, market risk estimators are often non-parametric and based on order statistics from historical simulation P&Ls, i.e., sorted P&L sample values. For VaR\operatorname{\mathrm{VaR}} and ES\operatorname{\mathrm{ES}}, the estimators are typically linear combinations of order statistics, with coefficients independent of the distribution of XX; see EBA [[2025](https://arxiv.org/html/2510.05809v1#bib.bib30)] for typical VaR look-back period and weighting choices. These observations further motivates the relevance of the (comonotonic) CRE representations developed in this paper. We refer to Section [6](https://arxiv.org/html/2510.05809v1#S6 "6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures") for a more detailed discussion of various nonparametric ES\operatorname{\mathrm{ES}} estimations.

The rest of the paper is organized as follows. Section [2](https://arxiv.org/html/2510.05809v1#S2 "2 Preliminaries ‣ Coherent estimation of risk measures") introduces the basic notation and recalls the definition of a coherent risk measure together with its robust representation. In Section [3](https://arxiv.org/html/2510.05809v1#S3 "3 Coherent risk estimators ‣ Coherent estimation of risk measures"), we introduce the central object of this study–the coherent risk estimators, discuss their fundamental properties, and provide illustrative examples. Section [4](https://arxiv.org/html/2510.05809v1#S4 "4 Robust representations of a CRE ‣ Coherent estimation of risk measures") is devoted to the robust representation of coherent risk estimators and presents the main theoretical contributions: Theorem [4.1](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem1 "Theorem 4.1 (Robust representation of CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"), Theorem [4.2](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem2 "Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"), and Theorem [4.10](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem10 "Theorem 4.10 (Robust representation of comonotonic and law-invariant CREs). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"). In Section [5](https://arxiv.org/html/2510.05809v1#S5 "5 Consistency of CREs for i.i.d. samples ‣ Coherent estimation of risk measures") we study the consistency property of CREs, with particular emphasis on the spectral risk measures. Finally, Section [6](https://arxiv.org/html/2510.05809v1#S6 "6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures") compares the performance of several ES estimators based on LL-statistics through a numerical study. The analysis highlights how the weighting scheme in the robust representation of CRE affects estimator performance, underscoring the importance of carefully defining ES estimators–particularly in overlapping scenarios that are typical for regulatory FRTB model risk estimation, cf. [BCBS, [2019](https://arxiv.org/html/2510.05809v1#bib.bib13), MAR 33.4].

## 2 Preliminaries

Let (Ω,𝒢,ℙ)(\Omega,\mathscr{G},\mathbb{P}) be a probability space and denote by L0:=L0​(Ω,𝒢,ℙ)L^{0}:=L^{0}(\Omega,\mathscr{G},\mathbb{P}) the corresponding space of random variables. Throughout, all equalities and inequalities will be understood in ℙ\mathbb{P}-a.s. sense. Assume that 𝒳⊂L0\mathcal{X}\subset L^{0} is a vector subspace that contains all constant random variables. Denote by ℳf:=ℳf​(Ω,𝒢)\mathcal{M}^{f}:=\mathcal{M}^{f}(\Omega,\mathscr{G}) the set of finitely additive set functions Q:𝒢→[0,1]Q\colon\mathscr{G}\to[0,1], which are normalized to 11, i.e. Q​(Ω)=1Q(\Omega)=1. We also use the notation ⌊b⌋:=max⁡{k∈ℤ:k≤b}\lfloor b\rfloor:=\max\{k\in\mathbb{Z}\colon k\leq b\}, for b∈ℝb\in\mathbb{R} and set ℳn:={a∈ℝn:∑i=1nai=1,ai≥0}\mathcal{M}\_{n}:=\left\{a\in\mathbb{R}^{n}:\sum\_{i=1}^{n}a\_{i}=1,a\_{i}\geq 0\right\}, for n∈ℕn\in\mathbb{N}.

For a fixed n∈ℕn\in\mathbb{N}, we use boldface lowercase letters to denote vectors in ℝn\mathbb{R}^{n}, e.g. 𝐱=(x1,…,xn)∈ℝn\mathbf{x}=(x\_{1},\ldots,x\_{n})\in\mathbb{R}^{n}, and ⟨𝐱,𝐲⟩:=∑i=1nxi​yi\langle\mathbf{x},\mathbf{y}\rangle:=\sum\_{i=1}^{n}x\_{i}y\_{i} stands for the usual dot product in ℝn\mathbb{R}^{n}.
Moreover, we denote by s​(𝐱):=(x1:n,…,xn:n)s(\mathbf{x}):=(x\_{1:n},\ldots,x\_{n:n}) the ordered version of 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n}, where xi:nx\_{i:n} is the iith smallest element of (x1,…,xn)(x\_{1},\ldots,x\_{n}), i=1,…,ni=1,\ldots,n.
We denote by SnS\_{n} the set of all permutations of {1,…,n}\{1,\ldots,n\}, and with slight abuse of notation, we set σ​(𝐱):=(xσ​(i),…,xσ​(n))\sigma(\mathbf{x}):=(x\_{\sigma(i)},\ldots,x\_{\sigma(n)}), for 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n} and σ∈Sn\sigma\in S\_{n}.

A risk measuring mapping ρ:𝒳→ℝ∪{+∞}\rho\colon\mathcal{X}\to\mathbb{R}\cup\{+\infty\} is called a coherent risk measure (CRM) if it satisfies the following properties:

1. (R1)

   Monotonicity, for any X,Y∈𝒳X,Y\in\mathcal{X} such that X≥YX\geq Y, we have ρ​(X)≤ρ​(Y)\rho(X)\leq\rho(Y);
2. (R2)

   Cash additivity, for any X∈𝒳X\in\mathcal{X} and m∈ℝm\in\mathbb{R}, we have ρ​(X+m)=ρ​(X)−m\rho(X+m)=\rho(X)-m;
3. (R3)

   Positive homogenity, for any X∈𝒳X\in\mathcal{X} and λ≥0\lambda\geq 0, we have ρ​(λ​X)=λ​ρ​(X)\rho(\lambda X)=\lambda\rho(X);
4. (R4)

   Subadditivity, for any X,Y∈𝒳X,Y\in\mathcal{X}, we have ρ​(X+Y)≤ρ​(X)+ρ​(Y)\rho(X+Y)\leq\rho(X)+\rho(Y).

Many natural risk measures are law-invariant, in the sense that the value of ρ​(X)\rho(X) depends only on the cumulative distribution function (CDF) of XX that we denote by FX​(x):=ℙ​(X≤x),x∈ℝF\_{X}(x):=\mathbb{P}(X\leq x),x\in\mathbb{R}. Formally, ρ:𝒳→ℝ∪{+∞}\rho\colon\mathcal{X}\to\mathbb{R}\cup\{+\infty\} is a law-invariant risk measure if for any X,Y∈𝒳X,Y\in\mathcal{X} with the same distribution under ℙ\mathbb{P}, we have that ρ​(X)=ρ​(Y)\rho(X)=\rho(Y).
For law-invariant risk measures, with a slight abuse of notation, we identify ρ​(X)\rho(X) with ρ​(FX)\rho(F\_{X}).

The class of CRMs has been well studied; cf. Föllmer and Schied [[2016](https://arxiv.org/html/2510.05809v1#bib.bib36)] for a comprehensive review in the bounded case 𝒳=L∞​(Ω,𝒢,ℙ)\mathcal{X}=L^{\infty}(\Omega,\mathscr{G},\mathbb{P}), for both static and dynamic setups, and Drapeau and Kupper [[2013](https://arxiv.org/html/2510.05809v1#bib.bib28)], Bielecki et al. [[2016](https://arxiv.org/html/2510.05809v1#bib.bib18)] for a general space. The postulated properties (R1)–(R4) are both clear and desirable from a risk management perspective. Here, the arguments X∈𝒳X\in\mathcal{X} are interpreted as the profit and loss (P&L) of a financial entity, with X>0X>0 indicating a profit and X≤0X\leq 0 a loss. Accordingly: (R1) implies that a dominating P&L entails lower risk; (R2), equivalently expressed as ρ​(X−ρ​(X))=0\rho(X-\rho(X))=0, indicates that ρ​(X)\rho(X) is the minimal deterministic capital reserve that neutralizes the risk; (R3) states that risk scales proportionally with the size of the position; and (R4) indicates that diversification reduces risk.

Among fundamental results in the theory of risk measures are the robust or numerical representations, which allow to express risk measures as suprema over a set of probability measures, thereby linking risk evaluation to the worst-case outcomes for the so-called generalized scenarios; see [Artzner et al., [1999](https://arxiv.org/html/2510.05809v1#bib.bib8), Section 4] for an economic view. For convenience, we formulate the result for the bounded and coherent case.

###### Theorem 2.1 (Robust representation of CRMs).

Let 𝒳=L∞​(Ω,𝒢,ℙ)\mathcal{X}=L^{\infty}(\Omega,\mathscr{G},\mathbb{P}). A functional ρ:𝒳→ℝ\rho:\mathcal{X}\to\mathbb{R} is a coherent risk measure if and only if there exists Mρ⊂ℳfM\_{\rho}\subset\mathcal{M}^{f} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(X)=supQ∈Mρ𝔼Q​[−X],X∈𝒳.\rho(X)=\sup\_{Q\in M\_{\rho}}\mathbb{E}\_{Q}[-X],\quad X\in\mathcal{X}. |  | (2.1) |

Moreover, MρM\_{\rho} can be chosen as a convex set for which the supremum is attained. That is, for any X∈𝒳X\in\mathcal{X}, there exists QX∗∈MρQ\_{X}^{\*}\in M\_{\rho} such that ρ​(X)=𝔼QX∗​[−X]\rho(X)=\mathbb{E}\_{Q\_{X}^{\*}}[-X].

The proof of Theorem [2.1](https://arxiv.org/html/2510.05809v1#S2.Thmtheorem1 "Theorem 2.1 (Robust representation of CRMs). ‣ 2 Preliminaries ‣ Coherent estimation of risk measures") can be found, for example, in Föllmer and Schied [[2016](https://arxiv.org/html/2510.05809v1#bib.bib36)]; see also Delbaen [[2002](https://arxiv.org/html/2510.05809v1#bib.bib27)] and Kusuoka [[2001](https://arxiv.org/html/2510.05809v1#bib.bib44)], where the law-invariant case was considered. This theorem has been extended to more general spaces, and larger classes of risk measures; we refer to Drapeau and Kupper [[2013](https://arxiv.org/html/2510.05809v1#bib.bib28)] for a comprehensive survey. In particular, one may take 𝒳=L1​(Ω,𝒢,ℙ)\mathcal{X}=L^{1}(\Omega,\mathscr{G},\mathbb{P}), where L1​(Ω,𝒢,ℙ)L^{1}(\Omega,\mathscr{G},\mathbb{P}) is the space of random variables with finite expectation, which encompasses all distributions considered in this paper, including normal or Student’s tt-distributions.

Among the most used and studied risk measures are the value at risk, the expected shortfall, and their weighted generalizations. For completeness, let us now briefly recall selected families of risk measures.

The value at risk (VaR\operatorname{\mathrm{VaR}}) at significance level α∈(0,1)\alpha\in(0,1) is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRα⁡(X):=inf{m∈ℝ|ℙ​(X+m<0)≤α},X∈𝒳.\operatorname{\mathrm{VaR}}\_{\alpha}(X):=\inf\{m\in\mathbb{R}\;|\;\mathbb{P}(X+m<0)\leq\alpha\},\quad X\in\mathcal{X}. |  | (2.2) |

In other words, the VaR\operatorname{\mathrm{VaR}} is the negative of the lower α\alpha-quantile of XX, i.e., the right generalized inverse of the cumulative distribution function at α∈(0,1)\alpha\in(0,1). While widely used, VaR\operatorname{\mathrm{VaR}} is known not to be a CRM due to its lack of subadditivity property (R4). That being said, for linear combinations of risk factors following elliptical distributions, and for confidence levels α<0.5\alpha<0.5, VaR\operatorname{\mathrm{VaR}} is subadditive and thus coherent, see [McNeil, [1999](https://arxiv.org/html/2510.05809v1#bib.bib46), Proposition 8.27].

The expected shortfall (ES) at significance level α∈(0,1)\alpha\in(0,1) is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESα​(X):=1α​∫0αVaRt⁡(X)​d⁡t,X∈𝒳.\textrm{ES}\_{\alpha}(X):=\frac{1}{\alpha}\int\_{0}^{\alpha}\operatorname{\mathrm{VaR}}\_{t}(X)\operatorname{d}\!t,\quad X\in\mathcal{X}. |  | (2.3) |

It is usually interpreted as an average of VaR\operatorname{\mathrm{VaR}}s beyond a specific threshold or negative of expected loss beyond α\alpha-quantile. The second interpretation is motivated by the fact that for continuous random variables ESα\textrm{ES}\_{\alpha} is equal to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESα​(X)=𝔼​[−X|X≤−VaRα⁡(X)],X∈𝒳,\textrm{ES}\_{\alpha}(X)=\mathbb{E}[-X\;|\;X\leq-\operatorname{\mathrm{VaR}}\_{\alpha}(X)],\quad X\in\mathcal{X}, |  | (2.4) |

see Lemma 2.16 in McNeil et al. [[2010](https://arxiv.org/html/2510.05809v1#bib.bib47)].

Note that the definition of ES could differ in literature and some authors use other names such as average value at risk or conditional value at risk to denote the mapping given by either ([2.3](https://arxiv.org/html/2510.05809v1#S2.E3 "In 2 Preliminaries ‣ Coherent estimation of risk measures")) or ([2.4](https://arxiv.org/html/2510.05809v1#S2.E4 "In 2 Preliminaries ‣ Coherent estimation of risk measures")). Notably, ES\operatorname{\mathrm{ES}} could be seen as a main building block of law-invariant and commonotonic CRMs. Namely, for a fixed probability measure μ\mu on [0,1][0,1], one can define the weighted value at risk (WVaR) given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | WVaRμ⁡(X):=∫(0,1]ESα⁡(X)​μ​(d⁡α),X∈𝒳,\operatorname{\mathrm{WVaR}}\_{\mu}(X):=\int\_{(0,1]}\operatorname{\mathrm{ES}}\_{\alpha}(X)\mu(\operatorname{d}\!\alpha),\quad X\in\mathcal{X}, |  | (2.5) |

and, typically, any law-invariant and comonotonic CRM could be represented using ([2.5](https://arxiv.org/html/2510.05809v1#S2.E5 "In 2 Preliminaries ‣ Coherent estimation of risk measures")); we refer to [Cherny, [2006](https://arxiv.org/html/2510.05809v1#bib.bib24), Theorem 2.10] for more details. Similarly, one can show that comonotonic and law-invariant risk measures could be constructed directly from VaR\operatorname{\mathrm{VaR}} using the so-called risk spectrum via the class of spectral risk measures, see Acerbi [[2002](https://arxiv.org/html/2510.05809v1#bib.bib2)] for details.

The closed-form formula for VaR\operatorname{\mathrm{VaR}} and ES\operatorname{\mathrm{ES}} is known for many distribution families used in risk management. In particular, by direct computations, one can show that VaR\operatorname{\mathrm{VaR}} and ES\operatorname{\mathrm{ES}} at level α∈(0,1)\alpha\in(0,1) of a Gaussian random variable XX with mean μ\mu and variance σ2\sigma^{2}, is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRα⁡(X)=−μ−σ​Φ−1​(α)andESα​(X)=−μ+σ​ϕ​(Φ−1​(α))α,\operatorname{\mathrm{VaR}}\_{\alpha}(X)=-\mu-\sigma\Phi^{-1}(\alpha)\quad\textrm{and}\quad\textrm{ES}\_{\alpha}(X)=-\mu+\sigma\frac{\phi(\Phi^{-1}(\alpha))}{\alpha}, |  | (2.6) |

where ϕ​(x):=12​π​exp⁡(−x2/2)\phi(x):=\frac{1}{\sqrt{2\pi}}\exp(-x^{2}/2), x∈ℝx\in\mathbb{R}, is the density of a standard normal, and Φ−1\Phi^{-1} is the standard normal quantile, see McNeil et al. [[2010](https://arxiv.org/html/2510.05809v1#bib.bib47)] for details and more examples.

## 3 Coherent risk estimators

From a practical standpoint, it is of paramount importance to design a reliable approximation of ρ​(X)\rho(X), for a given risk measure ρ\rho, using a random sample 𝐱\mathbf{x} of size nn from XX. Similarly to the notion of estimators from statistical analysis, for some given sample size n≥1n\geq 1, a risk estimator is a measurable map ρ^n:ℝn→ℝ\hat{\rho}\_{n}\colon\mathbb{R}^{n}\to\mathbb{R}. Rather than focusing solely on traditional properties from statistical inference (such as consistency or asymptotic normality), this article argues that a good risk estimator should, above all, satisfy properties grounded in sound financial principles. In this section we present some general properties for a coherent risk estimator ρ^n\hat{\rho}\_{n} and a fixed sample size n∈ℕn\in\mathbb{N}, without any reference to the specific choice of ρ\rho.

Similarly to the properties (R1)-(R4) imposed on coherent risk measures, we argue that an estimator of such measures must satisfy similar financially meaningful properties.

###### Definition 3.1 (Coherent risk estimator).

A function ρ^n:ℝn→ℝ\hat{\rho}\_{n}\colon\mathbb{R}^{n}\to\mathbb{R} is a coherent risk estimator (CRE) if it satisfies

1. (E1)

   Monotonicity, for any 𝐱,𝐱′∈ℝn\mathbf{x},\mathbf{x}^{\prime}\in\mathbb{R}^{n} such that444For vector order 𝐱≤𝐲\mathbf{x}\leq\mathbf{y} we use the component wise comparison xi≤yix\_{i}\leq y\_{i}, for i=1,2,…,ni=1,2,\ldots,n. 𝐱≥𝐱′\mathbf{x}\geq\mathbf{x}^{\prime}, we have ρ^n​(𝐱)≤ρ^n​(𝐱′)\hat{\rho}\_{n}(\mathbf{x})\leq\hat{\rho}\_{n}(\mathbf{x}^{\prime});
2. (E2)

   Cash additivity, for any 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n} and m∈ℝm\in\mathbb{R}, we have ρ^n​(𝐱+m)=ρ^n​(𝐱)−m\hat{\rho}\_{n}(\mathbf{x}+m)=\hat{\rho}\_{n}(\mathbf{x})-m;
3. (E3)

   Positive homogeneity, for any 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n} and λ≥0\lambda\geq 0, we have ρ^n​(λ​𝐱)=λ​ρ^n​(𝐱)\hat{\rho}\_{n}(\lambda\mathbf{x})=\lambda\hat{\rho}\_{n}(\mathbf{x});
4. (E4)

   Subadditivity, for any 𝐱,𝐱′∈ℝn\mathbf{x},\mathbf{x}^{\prime}\in\mathbb{R}^{n}, we have ρ^n​(𝐱+𝐱′)≤ρ^n​(𝐱)+ρ^n​(𝐱′)\hat{\rho}\_{n}(\mathbf{x}+\mathbf{x}^{\prime})\leq\hat{\rho}\_{n}(\mathbf{x})+\hat{\rho}\_{n}(\mathbf{x}^{\prime}).

Coherent risk estimators essentially inherit all axiomatic properties of the coherent risk measures, including their financial meaning. Properties (E1)-(E4) are generic and should hold for any sample points in ℝn\mathbb{R}^{n}. A generic CRE mapping ρ^n\hat{\rho}\_{n} is a priori not linked or generated by a pre-specified CRM ρ\rho, so that one should not expect that ρ^n\hat{\rho}\_{n} will converge to any specfic CRM as sample size increases, n→∞n\to\infty, unless additional conditions are imposed on ρ^n\hat{\rho}\_{n}; see Section [5](https://arxiv.org/html/2510.05809v1#S5 "5 Consistency of CREs for i.i.d. samples ‣ Coherent estimation of risk measures") for details. From a practical and regulatory view point, a risk estimator may be interpreted as a mapping that determines the appropriate capital reserve as a function of available data, in contrast to being solely a function that somehow approximates the unknown theoretical value of risk measure. As we show below, our definition of CRE naturally leads to the important class of non-parametric estimators of baseline risk measures that are based on order statistics as recommended by regulators, see e.g. [ECB, [2025](https://arxiv.org/html/2510.05809v1#bib.bib31), Paragraph 100 in CRR3 market risk chapter].

Next, to capture the law-invariant property, we introduce the notion of a law-invariant estimator. We recall that s​(𝐱),𝐱∈ℝns(\mathbf{x}),\ \mathbf{x}\in\mathbb{R}^{n}, denotes the sorted sample in ascending order.

###### Definition 3.2 (Law-invariant estimator).

A function ρ^n:ℝn→ℝ\hat{\rho}\_{n}\colon\mathbb{R}^{n}\to\mathbb{R} is permutation or law-invariant if, for any 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n}, we have ρ^n​(𝐱)=ρ^n​(s​(𝐱))\hat{\rho}\_{n}(\mathbf{x})=\hat{\rho}\_{n}(s(\mathbf{x})).

Note that in Definition [3.2](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem2 "Definition 3.2 (Law-invariant estimator). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures") we may equivalently require that
ρ^n​(𝐱)=ρ^n​(σ​(𝐱))\hat{\rho}\_{n}(\mathbf{x})=\hat{\rho}\_{n}(\sigma(\mathbf{x})) for any 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n} and permutation σ∈Sn\sigma\in S\_{n}. Indeed, directly from the law-invariance property, we get

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(σ​(𝐱))=ρ^n​(s​(σ​(𝐱)))=ρ^n​(s​(𝐱))=ρ^n​(𝐱).\hat{\rho}\_{n}(\sigma(\mathbf{x}))=\hat{\rho}\_{n}(s(\sigma(\mathbf{x})))=\hat{\rho}\_{n}(s(\mathbf{x}))=\hat{\rho}\_{n}(\mathbf{x}). |  |

It should be emphasized that while properties (E1)–(E4) directly mirror the corresponding CRM properties, the relation between the law-invariance of CRMs and CREs is more intricate. In particular, when we assume that the order of sampling can be altered without affecting the estimator, we implicitly induce sampling independence. This is a substantially stronger condition than merely imposing law-invariance of the underlying risk measure. For example, while an estimator is typically law-invariant within i.i.d. sampling framework, this need not hold when the data is generated by a time-dependent process such as Generalized Auto-Regressive Conditional Heteroskedasticity (GARCH) process, or under an Exponentially Weighted Moving Average (EWMA) framework, even if the underlying CRM is law-invariant, see e.g. Hansen and Lunde [[2005](https://arxiv.org/html/2510.05809v1#bib.bib38)], Alexander [[2009](https://arxiv.org/html/2510.05809v1#bib.bib5)] for details. For clarity, throughout most of this paper, we restrict attention to the i.i.d. sampling, though some results–including the core representation result in Theorem [4.1](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem1 "Theorem 4.1 (Robust representation of CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")–are formulated for the general case.

A natural and simple way to construct a law-invariant CRE based on a given law-invariant CRM is to use a non-parametric plug-in estimator based on the empirical CDF. For 𝐱=(x1,…,xn)∈ℝn\mathbf{x}=(x\_{1},\ldots,x\_{n})\in\mathbb{R}^{n}, the empirical cumulative distribution function is defined as F^𝐱​(t):=1n​∑i=1n𝟙{xi≤t}\hat{F}\_{\mathbf{x}}(t):=\frac{1}{n}\sum\_{i=1}^{n}\mathbbm{1}\_{\{x\_{i}\leq t\}}, t∈ℝt\in\mathbb{R}.

###### Proposition 3.3 (Empirical plug-in risk estimator for CRM is coherent).

Let ρ\rho be a law-invariant CRM. Then, for any n∈ℕn\in\mathbb{N}, the mapping ρ^nemp:𝐱↦ρ^nemp​(𝐱):=ρ​(F^𝐱)\hat{\rho}^{\textnormal{emp}}\_{n}\colon\mathbf{x}\mapsto\hat{\rho}^{\textnormal{emp}}\_{n}(\mathbf{x}):=\rho(\hat{F}\_{\mathbf{x}}), where 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n}, is a law-invariant CRE.

###### Proof.

Let ρ\rho be a law-invariant CRM. The law-invariance of ρ^nemp\hat{\rho}^{\textnormal{emp}}\_{n} follows directly from the fact that F^𝐱=F^s​(𝐱)\hat{F}\_{\mathbf{x}}=\hat{F}\_{s(\mathbf{x})}. Second, we check the cash-additivity (E2), while omitting the remaining properties that follow by similar arguments. Let 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n} and m∈ℝm\in\mathbb{R}. Consider a random variable YY which is uniformly distributed on the set induced by sample 𝐱\mathbf{x}, that is, on {x1,…,xn}\{x\_{1},\ldots,x\_{n}\}. Then, noting that F^𝐱+m\hat{F}\_{\mathbf{x}+m} is the CDF for the random variable Y+mY+m, and using the cash additivity of ρ\rho, we get

|  |  |  |
| --- | --- | --- |
|  | ρ^nemp​(𝐱+m)=ρ​(F^𝐱+m)=ρ​(Y+m)=ρ​(Y)−m=ρ​(F^𝐱)−m=ρ^nemp​(𝐱)−m,\hat{\rho}^{\textnormal{emp}}\_{n}(\mathbf{x}+m)=\rho(\hat{F}\_{\mathbf{x}+m})=\rho(Y+m)=\rho(Y)-m=\rho(\hat{F}\_{\mathbf{x}})-m=\hat{\rho}^{\textnormal{emp}}\_{n}(\mathbf{x})-m, |  |

which completes the argument. ∎

Another popular approach for constructing risk estimators is based on the so-called parametric plug-in procedure. However, as we show in the following example, these risk estimators may not be coherent even though the underlying risk measure is coherent.

###### Example 3.4 (Gaussian parameteric plug-in ES estimator is not coherent).

In view of ([2.6](https://arxiv.org/html/2510.05809v1#S2.E6 "In 2 Preliminaries ‣ Coherent estimation of risk measures")), the Gaussian parametric plug-in estimator of the ES at level α=1%\alpha=1\% could be defined as

|  |  |  |
| --- | --- | --- |
|  | ES^1%norm​(𝐱):=−(μ^​(𝐱)−σ^​(𝐱)​ϕ​(Φ−1​(0.01))0.01),\widehat{\textrm{ES}}^{\textrm{norm}}\_{1\%}(\mathbf{x}):=-\left(\hat{\mu}(\mathbf{x})-\hat{\sigma}(\mathbf{x})\frac{\phi(\Phi^{-1}(0.01))}{0.01}\right), |  |

where μ^​(𝐱)\hat{\mu}(\mathbf{x}) and σ^​(𝐱)\hat{\sigma}(\mathbf{x}) are the sample mean and the sample standard deviation of 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n}. As the name suggests, we replaced the true parametric mean and standard deviation in ([2.6](https://arxiv.org/html/2510.05809v1#S2.E6 "In 2 Preliminaries ‣ Coherent estimation of risk measures")) by their (sample) estimators. Now, consider two data samples 𝐱:=(1,0)\mathbf{x}:=(1,0) and 𝐱′:=(0,0)\mathbf{x}^{\prime}:=(0,0). Clearly, 𝐱≥𝐱′\mathbf{x}\geq\mathbf{x}^{\prime}, but

|  |  |  |
| --- | --- | --- |
|  | ES^1%norm​(𝐱)≈−(12−2.662)≈1.38>0=ES^1%​(𝐱′).\widehat{\textrm{ES}}^{\textrm{norm}}\_{1\%}(\mathbf{x})\approx-\left(\frac{1}{2}-\frac{2.66}{\sqrt{2}}\right)\approx 1.38>0=\widehat{\textrm{ES}}\_{1\%}(\mathbf{x}^{\prime}). |  |

Thus, ES^1%norm\widehat{\textrm{ES}}^{\textrm{norm}}\_{1\%} is not monotone, and hence not coherent. □\square

In fact, as we indirectly show in the next section, parametric risk estimators are structurally not coherent; see Theorem [4.1](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem1 "Theorem 4.1 (Robust representation of CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") for details. Next, let us show that a typical non-parametric ES estimator based on average tail loss is a law-invariant CRE.

###### Example 3.5 (Average tail loss ES estimator is coherent).

Let us consider a commonly used non-parametric estimator of the ES at level α∈(0,1)\alpha\in(0,1) given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ES^α,n1​(𝐱):=−1⌊n​α⌋​∑i=1⌊n​α⌋xi:n,\widehat{\textrm{ES}}^{1}\_{\alpha,n}(\mathbf{x}):=-\frac{1}{\lfloor n\alpha\rfloor}\sum\_{i=1}^{\lfloor n\alpha\rfloor}x\_{i:n}, |  | (3.1) |

where 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n}; see McNeil et al. [[2010](https://arxiv.org/html/2510.05809v1#bib.bib47)]. For simplicity, we assume that nn is large enough to have ⌊n​α⌋≥1\lfloor n\alpha\rfloor\geq 1. This estimator can be obtained using ([2.4](https://arxiv.org/html/2510.05809v1#S2.E4 "In 2 Preliminaries ‣ Coherent estimation of risk measures")) and considering the sample conditional mean.
Moreover, one can show it is a coherent and law-invariant risk estimator; see also [Acerbi and Tasche, [2002](https://arxiv.org/html/2510.05809v1#bib.bib3), Appendix A]. For the sake of completeness, we provide a more direct proof that ES^α,n1\widehat{\textrm{ES}}^{1}\_{\alpha,n} is a CRE, focusing only on the subadditivity (E4) as the remaining properties are trivially satisfied. We start by introducing the modified indicator function

|  |  |  |
| --- | --- | --- |
|  | 𝟙{x≤x⌊n​α⌋:n}∗:=𝟙{x<x⌊n​α⌋:n}+𝟙{x=x⌊n​α⌋:n}​⌊n​α⌋−#​{i∈{1,…,n}:xi<x⌊n​α⌋:n}#​{i∈{1,…,n}:xi=x⌊n​α⌋:n}\mathbbm{1}^{\*}\_{\{x\leq x\_{\lfloor n\alpha\rfloor:n}\}}:=\mathbbm{1}\_{\{x<x\_{\lfloor n\alpha\rfloor:n}\}}+\mathbbm{1}\_{\{x=x\_{\lfloor n\alpha\rfloor:n}\}}\frac{\lfloor n\alpha\rfloor-\#\{i\in\{1,\ldots,n\}\colon x\_{i}<x\_{\lfloor n\alpha\rfloor:n}\}}{\#\{i\in\{1,\ldots,n\}\colon x\_{i}=x\_{\lfloor n\alpha\rfloor:n}\}} |  |

for any x∈ℝx\in\mathbb{R} and 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n}, which accounts for possible ties in the data.
Clearly,

|  |  |  |
| --- | --- | --- |
|  | ES^α,n1​(𝐱)=−1⌊n​α⌋​∑i=1nxi​𝟙{xi≤x⌊n​α⌋:n}∗.\widehat{\textrm{ES}}^{1}\_{\alpha,n}(\mathbf{x})=-\frac{1}{\lfloor n\alpha\rfloor}\sum\_{i=1}^{n}x\_{i}\mathbbm{1}^{\*}\_{\{x\_{i}\leq x\_{\lfloor n\alpha\rfloor:n}\}}. |  |

Then, for any 𝐲∈ℝn\mathbf{y}\in\mathbb{R}^{n} and 𝒛:=𝐱+𝐲\boldsymbol{z}:=\mathbf{x}+\mathbf{y}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⌊n​α⌋​(ES^α,n1​(𝐱)+ES^α,n1​(𝐲)−ES^α,n1​(𝒛))=∑i=1nxi​(𝟙{zi≤z⌊n​α⌋:n}∗−𝟙{xi≤x⌊n​α⌋:n}∗)+∑i=1nyi​(𝟙{zi≤z⌊n​α⌋:n}∗−𝟙{yi≤y⌊n​α⌋:n}∗).\lfloor n\alpha\rfloor\left(\widehat{\textrm{ES}}^{1}\_{\alpha,n}(\mathbf{x})+\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,n}(\mathbf{y})-\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,n}(\boldsymbol{z})\right)=\sum\_{i=1}^{n}x\_{i}\left(\mathbbm{1}^{\*}\_{\{z\_{i}\leq z\_{\lfloor n\alpha\rfloor:n}\}}-\mathbbm{1}^{\*}\_{\{x\_{i}\leq x\_{\lfloor n\alpha\rfloor:n}\}}\right)+\sum\_{i=1}^{n}y\_{i}\left(\mathbbm{1}^{\*}\_{\{z\_{i}\leq z\_{\lfloor n\alpha\rfloor:n}\}}-\mathbbm{1}^{\*}\_{\{y\_{i}\leq y\_{\lfloor n\alpha\rfloor:n}\}}\right). |  | (3.2) |

Note that for i∈{1,…,n}i\in\{1,\ldots,n\} such that xi<x⌊n​α⌋:nx\_{i}<x\_{\lfloor n\alpha\rfloor:n} we have 𝟙{zi≤z⌊n​α⌋:n}∗−𝟙{xi≤x⌊n​α⌋:n}∗≤𝟙{zi≤z⌊n​α⌋:n}∗−1≤0\mathbbm{1}^{\*}\_{\{z\_{i}\leq z\_{\lfloor n\alpha\rfloor:n}\}}-\mathbbm{1}^{\*}\_{\{x\_{i}\leq x\_{\lfloor n\alpha\rfloor:n}\}}\leq\mathbbm{1}^{\*}\_{\{z\_{i}\leq z\_{\lfloor n\alpha\rfloor:n}\}}-1\leq 0. Also, for i∈{1,…,n}i\in\{1,\ldots,n\} such that xi>x⌊n​α⌋:nx\_{i}>x\_{\lfloor n\alpha\rfloor:n} we have 𝟙{zi≤z⌊n​α⌋:n}∗−𝟙{xi≤x⌊n​α⌋:n}∗≥𝟙{zi≤z⌊n​α⌋:n}∗≥0\mathbbm{1}^{\*}\_{\{z\_{i}\leq z\_{\lfloor n\alpha\rfloor:n}\}}-\mathbbm{1}^{\*}\_{\{x\_{i}\leq x\_{\lfloor n\alpha\rfloor:n}\}}\geq\mathbbm{1}^{\*}\_{\{z\_{i}\leq z\_{\lfloor n\alpha\rfloor:n}\}}\geq 0. Consequently, we deduce

|  |  |  |
| --- | --- | --- |
|  | ∑i=1n(xi−x⌊n​α⌋:n)​(𝟙{zi≤z⌊n​α⌋:n}∗−𝟙{xi≤x⌊n​α⌋:n}∗)≥0.\sum\_{i=1}^{n}(x\_{i}-x\_{\lfloor n\alpha\rfloor:n})\left(\mathbbm{1}^{\*}\_{\{z\_{i}\leq z\_{\lfloor n\alpha\rfloor:n}\}}-\mathbbm{1}^{\*}\_{\{x\_{i}\leq x\_{\lfloor n\alpha\rfloor:n}\}}\right)\geq 0. |  |

Using this inequality and repeating the same argument for 𝐲\mathbf{y}, from ([3.2](https://arxiv.org/html/2510.05809v1#S3.E2 "In Example 3.5 (Average tail loss ES estimator is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⌊n​α⌋​(ES^α,n1​(𝐱)+ES^α,n1​(𝐲)−ES^α1​(𝒛))\displaystyle\lfloor n\alpha\rfloor\left(\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,n}(\mathbf{x})+\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,n}(\mathbf{y})-\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha}(\boldsymbol{z})\right) | ≥∑i=1nx⌊n​α⌋:n​(𝟙{zi≤z⌊n​α⌋:n}∗−𝟙{xi≤x⌊n​α⌋:n}∗)+∑i=1ny⌊n​α⌋:n​(𝟙{zi≤z⌊n​α⌋:n}∗−𝟙{yi≤y⌊n​α⌋:n}∗)\displaystyle\geq\sum\_{i=1}^{n}x\_{\lfloor n\alpha\rfloor:n}\left(\mathbbm{1}^{\*}\_{\{z\_{i}\leq z\_{\lfloor n\alpha\rfloor:n}\}}-\mathbbm{1}^{\*}\_{\{x\_{i}\leq x\_{\lfloor n\alpha\rfloor:n}\}}\right)+\sum\_{i=1}^{n}y\_{\lfloor n\alpha\rfloor:n}\left(\mathbbm{1}^{\*}\_{\{z\_{i}\leq z\_{\lfloor n\alpha\rfloor:n}\}}-\mathbbm{1}^{\*}\_{\{y\_{i}\leq y\_{\lfloor n\alpha\rfloor:n}\}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =x⌊n​α⌋:n​(⌊n​α⌋−⌊n​α⌋)+y⌊n​α⌋:n​(⌊n​α⌋−⌊n​α⌋)=0,\displaystyle=x\_{\lfloor n\alpha\rfloor:n}(\lfloor n\alpha\rfloor-\lfloor n\alpha\rfloor)+y\_{\lfloor n\alpha\rfloor:n}(\lfloor n\alpha\rfloor-\lfloor n\alpha\rfloor)=0, |  |

where we used the fact that ∑i=1n𝟙{xi≤x⌊n​α⌋:n}∗=⌊n​α⌋\sum\_{i=1}^{n}\mathbbm{1}^{\*}\_{\{x\_{i}\leq x\_{\lfloor n\alpha\rfloor:n}\}}=\lfloor n\alpha\rfloor. This shows that ES^α,n1​(𝒙+𝒚)≤ES^α,n1​(𝐱)+ES^α,n1​(𝐲)\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,n}(\boldsymbol{x+y})\leq\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,n}(\mathbf{x})+\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,n}(\mathbf{y}). □\square

Next, we recall that VaR\operatorname{\mathrm{VaR}} is not a CRM as it lacks the subadditivity property (R4) and show that the traditionally used non-parametric estimator of VaR\operatorname{\mathrm{VaR}}, the empirical quantile, is also not coherent.

###### Example 3.6 (Empirical quantile VaR\operatorname{\mathrm{VaR}} estimator is not coherent).

Let us consider a non-parametric estimator of VaR\operatorname{\mathrm{VaR}} at level α∈(0,1)\alpha\in(0,1) given by the empirical quantile

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaR^α,n​(𝐱):=−x(⌊α​n⌋+1):n,𝐱∈ℝn.\widehat{\operatorname{\mathrm{VaR}}}\_{\alpha,n}(\mathbf{x}):=-x\_{(\lfloor\alpha n\rfloor+1):n},\quad\mathbf{x}\in\mathbb{R}^{n}. |  | (3.3) |

To illustrate that this estimator is non-coherent we use exemplary parameter values; the example can be easily modified to cover the general case. Namely, let us fix α=1%\alpha=1\%, n=100n=100, and consider 𝐱:=(−100,0,…,0)∈ℝ100\mathbf{x}:=(-100,0,\ldots,0)\in\mathbb{R}^{100} and 𝐱′:=(0,−100,0,…,0)∈ℝ100\mathbf{x}^{\prime}:=(0,-100,0,\ldots,0)\in\mathbb{R}^{100}. Then,

|  |  |  |
| --- | --- | --- |
|  | 100=VaR^1%,100​(𝐱+𝐱′)>VaR^1%,100​(𝐱)+VaR^1%,100​(𝐱′)=0+0=0,100=\widehat{\operatorname{\mathrm{VaR}}}\_{1\%,100}(\mathbf{x}+\mathbf{x}^{\prime})>\widehat{\operatorname{\mathrm{VaR}}}\_{1\%,100}(\mathbf{x})+\widehat{\operatorname{\mathrm{VaR}}}\_{1\%,100}(\mathbf{x}^{\prime})=0+0=0, |  |

and thus the subadditivity property (E4) is violated. Hence, VaR^1%,100\widehat{\operatorname{\mathrm{VaR}}}\_{1\%,100} is not coherent.
□\square

We conclude this section with an example that links risk estimators of VaR\operatorname{\mathrm{VaR}} and ES\operatorname{\mathrm{ES}} via the integration formula in ([2.3](https://arxiv.org/html/2510.05809v1#S2.E3 "In 2 Preliminaries ‣ Coherent estimation of risk measures")).

###### Example 3.7 (Non-parametric plug-in ES estimator is coherent).

In this example, we estimate ES at level α∈(0,1)\alpha\in(0,1) by taking formula ([2.3](https://arxiv.org/html/2510.05809v1#S2.E3 "In 2 Preliminaries ‣ Coherent estimation of risk measures")) and replacing VaRt\operatorname{\mathrm{VaR}}\_{t} by its empirical quantile estimator VaR^t,n\widehat{\operatorname{\mathrm{VaR}}}\_{t,n} given by ([3.3](https://arxiv.org/html/2510.05809v1#S3.E3 "In Example 3.6 (Empirical quantile VaR estimator is not coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures")), for t∈(0,α)t\in(0,\alpha). After direct integration over tt in ([2.3](https://arxiv.org/html/2510.05809v1#S2.E3 "In 2 Preliminaries ‣ Coherent estimation of risk measures")), we obtain the ES estimator given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ES^α,n2​(𝐱):=−1n​α​(∑i=1⌊n​α⌋xi:n+(n​α−⌊n​α⌋)​x(⌊n​α⌋+1):n);\widehat{\textrm{ES}}\_{\alpha,n}^{2}(\mathbf{x}):=-\frac{1}{n\alpha}\left(\sum\_{i=1}^{\lfloor n\alpha\rfloor}x\_{i:n}+(n\alpha-\lfloor n\alpha\rfloor)x\_{(\lfloor n\alpha\rfloor+1):n}\right); |  | (3.4) |

see also Equation 25 in Rockafellar and Uryasev [[2002](https://arxiv.org/html/2510.05809v1#bib.bib55)] with pk=k/np\_{k}=k/n or Article 11 in EU [[2024b](https://arxiv.org/html/2510.05809v1#bib.bib34)]. Note that ([3.4](https://arxiv.org/html/2510.05809v1#S3.E4 "In Example 3.7 (Non-parametric plug-in ES estimator is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures")) is a plug-in estimator for the empirical distribution function; alternative ES estimators based on other types of quantiles could be also obtained, see Hyndman and Fan [[1996](https://arxiv.org/html/2510.05809v1#bib.bib42)] and examples in Section [6](https://arxiv.org/html/2510.05809v1#S6 "6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures"). Finally, we note that while the VaR\operatorname{\mathrm{VaR}} estimator stated in ([3.3](https://arxiv.org/html/2510.05809v1#S3.E3 "In Example 3.6 (Empirical quantile VaR estimator is not coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures")) is not coherent, the corresponding ES\operatorname{\mathrm{ES}} estimator given in ([3.4](https://arxiv.org/html/2510.05809v1#S3.E4 "In Example 3.7 (Non-parametric plug-in ES estimator is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures")) is a CRE. This could be shown using a similar technique as in Example [3.5](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem5 "Example 3.5 (Average tail loss ES estimator is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures") or by applying Theorem [4.1](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem1 "Theorem 4.1 (Robust representation of CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"). ∎

## 4 Robust representations of a CRE

In this section, we derive new representations of the CREs, in the spirit of Delbaen [[2002](https://arxiv.org/html/2510.05809v1#bib.bib27)] and Kusuoka [[2001](https://arxiv.org/html/2510.05809v1#bib.bib44)], cf. Theorem [2.1](https://arxiv.org/html/2510.05809v1#S2.Thmtheorem1 "Theorem 2.1 (Robust representation of CRMs). ‣ 2 Preliminaries ‣ Coherent estimation of risk measures"). As already mentioned in Section [2](https://arxiv.org/html/2510.05809v1#S2 "2 Preliminaries ‣ Coherent estimation of risk measures"), such representations for risk measures are known as robust or numerical representations, are often linked to dual biconjugates, and are obtained, e.g., via the Fenchel-Moreau theorem, see Drapeau and Kupper [[2013](https://arxiv.org/html/2510.05809v1#bib.bib28)].

Let us now comment on the significance of these results. In the statistical setup, they facilitate a full characterization of CREs, and, as we show below, these representations are closely related to the well-studied concept of LL-estimators. Second, with such results at hand, we can establish additional structural properties of CREs. Third, these representations provide a practical tool for constructing new risk estimators or modifying existing ones. In particular, they enable the design of estimators that satisfy additional desired properties. To the best of our knowledge, the results presented in this section are new. In particular, we are not aware of any systematic studies of estimators defined as suprema over a family of LL-estimators, a class that plays a central role in our framework.

We start with the generic representation result in which no additional assumptions are imposed on CRE.

###### Theorem 4.1 (Robust representation of CREs).

A function ρ^n:ℝn→ℝ\hat{\rho}\_{n}\colon\mathbb{R}^{n}\to\mathbb{R} is a CRE if and only if there exists a set Mρ^n∗⊂ℳnM\_{\hat{\rho}\_{n}}^{\*}\subset\mathcal{M}\_{n} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ^n​(𝐱)=supa∈Mρ^n∗⟨a,−𝐱⟩,𝐱∈ℝn.\hat{\rho}\_{n}(\mathbf{x})=\sup\_{a\in M\_{\hat{\rho}\_{n}}^{\*}}\langle a,-\mathbf{x}\rangle,\quad\mathbf{x}\in\mathbb{R}^{n}. |  | (4.1) |

Moreover, Mρ^n∗M\_{\hat{\rho}\_{n}}^{\*} can be chosen to be a convex set, independent of 𝐱\mathbf{x}, such that the supremum is attained, i.e. for any 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n} there exists a∗=a∗​(𝐱)∈Mρ^n∗a^{\*}=a^{\*}(\mathbf{x})\in M\_{\hat{\rho}\_{n}}^{\*} such that ρ^n​(𝐱)=⟨a∗,−𝐱⟩\hat{\rho}\_{n}(\mathbf{x})=\langle a^{\*},-\mathbf{x}\rangle.

###### Proof.

Using properties of the supremum and Definition [3.1](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem1 "Definition 3.1 (Coherent risk estimator). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures"), it is straightforward to check that the map defined in ([4.1](https://arxiv.org/html/2510.05809v1#S4.E1 "In Theorem 4.1 (Robust representation of CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")) is a CRE. Next, we show that any CRE admits the representation ([4.1](https://arxiv.org/html/2510.05809v1#S4.E1 "In Theorem 4.1 (Robust representation of CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")). To illustrate this result from different perspectives, we provide two arguments for this part: (a) based on generic properties of convex functionals; (b) based on a suitable identification of risk measures.

Approach (a).
Combining the positive homogeneity (E3) and the subadditivity (E4) from Definition [3.1](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem1 "Definition 3.1 (Coherent risk estimator). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures"), we deduce that ρ^n\hat{\rho}\_{n} is convex on ℝn\mathbb{R}^{n}, and in view of [Boyd and Vandenberghe, [2004](https://arxiv.org/html/2510.05809v1#bib.bib21), Section 3.2.3], there exist sets Mρ^n∗⊂ℝnM\_{\hat{\rho}\_{n}}^{\*}\subset\mathbb{R}^{n} and Bρ^n∗⊂ℝB\_{\hat{\rho}\_{n}}^{\*}\subset\mathbb{R} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ^n​(𝐱)=supa∈Mρ^n∗b∈Bρ^n∗(⟨a,−𝐱⟩+b),𝐱∈ℝn,\hat{\rho}\_{n}(\mathbf{x})=\sup\_{\begin{subarray}{c}a\in M\_{\hat{\rho}\_{n}}^{\*}\\ b\in B\_{\hat{\rho}\_{n}}^{\*}\end{subarray}}\left(\langle a,-\mathbf{x}\rangle+b\right),\quad\mathbf{x}\in\mathbb{R}^{n}, |  | (4.2) |

and, for any 𝐱\mathbf{x}, the above supremum is attained. By the positive homogeneity (E3) with λ=0\lambda=0, we obtain 0=ρ^n​(0)=supb∈Bρ^n∗b0=\hat{\rho}\_{n}(0)=\sup\_{b\in B\_{\hat{\rho}\_{n}}^{\*}}b. This implies that Bρ^n∗⊂(−∞,0]B\_{\hat{\rho}\_{n}}^{\*}\subset(-\infty,0] and there exists a sequence (bj)j=1∞(b\_{j})\_{j=1}^{\infty}, such that bj∈Bρ^n∗b\_{j}\in B\_{\hat{\rho}\_{n}}^{\*} and limj→∞bj=0\lim\_{j\to\infty}b\_{j}=0. Consequently, since ([4.2](https://arxiv.org/html/2510.05809v1#S4.E2 "In 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")) is given in terms of suprema, we can assume Bρ^n∗={0}B\_{\hat{\rho}\_{n}}^{\*}=\{0\}. Next, for any i=1,…,ni=1,\ldots,n, let eie\_{i} denote the iith canonical unit vector in ℝn\mathbb{R}^{n}. Then, using the monotonicity (E1), we deduce 0≥ρ^n​(ei)=supa∈Mρ^n∗⟨a,−ei⟩0\geq\hat{\rho}\_{n}(e\_{i})=\sup\_{a\in M\_{\hat{\rho}\_{n}}^{\*}}\langle a,-e\_{i}\rangle, for all i=1,…,ni=1,\ldots,n, and hence, for any a∈Mρ^n∗a\in M\_{\hat{\rho}\_{n}}^{\*}, we have a≥0a\geq 0. Let us denote by 𝟏\mathbf{1} the nn-dimensional vector of ones. Then, by the cash additivity (E2), we obtain

|  |  |  |
| --- | --- | --- |
|  | −1=ρ^n​(0)−1=ρ^n​(𝟏)=supa∈Mρ^n∗⟨a,−𝟏⟩,-1=\hat{\rho}\_{n}(0)-1=\hat{\rho}\_{n}(\mathbf{1})=\sup\_{a\in M\_{\hat{\rho}\_{n}}^{\*}}\langle a,-\mathbf{1}\rangle, |  |

and thus, for any a=(a1,…,an)∈Mρ^n∗a=(a\_{1},\ldots,a\_{n})\in M\_{\hat{\rho}\_{n}}^{\*}, we have ∑i=1nai≥1\sum\_{i=1}^{n}a\_{i}\geq 1. On the other hand, we have

|  |  |  |
| --- | --- | --- |
|  | 1=ρ^n​(0)+1=ρ^n​(−𝟏)=supa∈Mρ^n∗⟨a,𝟏⟩,1=\hat{\rho}\_{n}(0)+1=\hat{\rho}\_{n}(-\mathbf{1})=\sup\_{a\in M\_{\hat{\rho}\_{n}}^{\*}}\langle a,\mathbf{1}\rangle, |  |

which implies that ∑i=1nai≤1\sum\_{i=1}^{n}a\_{i}\leq 1. Consequently, we get ∑i=1nai=1\sum\_{i=1}^{n}a\_{i}=1 and conclude the proof.

Approach (b). Let Ω^:={ω1,…,ωn}\hat{\Omega}:=\{\omega\_{1},\ldots,\omega\_{n}\} be a generic nn-tuple, and let 𝒢^\hat{\mathscr{G}} be the family of all subsets of Ω^\hat{\Omega}. For X∈L0​(Ω^,𝒢^)X\in L^{0}(\hat{\Omega},\hat{\mathscr{G}}) we define ρ​(X):=ρ^n​((X​(ω1),…,X​(ωn)))\rho(X):=\hat{\rho}\_{n}((X(\omega\_{1}),\ldots,X(\omega\_{n}))). Clearly, ρ\rho satisfies properties (R1)-(R4), as ρ^\hat{\rho} satisfies properties (E1)-(E4), and thus ρ\rho it is a CRM on (Ω^,𝒢^)(\hat{\Omega},\hat{\mathscr{G}}). In view of Theorem [2.1](https://arxiv.org/html/2510.05809v1#S2.Thmtheorem1 "Theorem 2.1 (Robust representation of CRMs). ‣ 2 Preliminaries ‣ Coherent estimation of risk measures"),
there exists a family Mρ⊂ℳf​(Ω^,𝒢^)M\_{\rho}\subset\mathcal{M}^{f}(\hat{\Omega},\hat{\mathcal{G}}) such that

|  |  |  |
| --- | --- | --- |
|  | ρ^n​((X​(ω1),…,X​(ωn)))=ρ​(X)=supQ∈Mρ𝔼Q​[−X],\hat{\rho}\_{n}((X(\omega\_{1}),\ldots,X(\omega\_{n})))=\rho(X)=\sup\_{Q\in M\_{\rho}}\mathbb{E}\_{Q}[-X], |  |

and, for any XX the supremum is attained. Since Ω^\hat{\Omega} is finite, any Q∈MρQ\in M\_{\rho} is a probability measure which could be identified with a vector a:=(Q​({ω1}),…,Q​({ωn}))a:=(Q(\{\omega\_{1}\}),\ldots,Q(\{\omega\_{n}\})). Noting that 𝔼Q​[−X]=⟨a,−(X​(ω1),…,X​(ωn))⟩\mathbb{E}\_{Q}[-X]=\langle a,-(X(\omega\_{1}),\ldots,X(\omega\_{n}))\rangle, we get ([4.1](https://arxiv.org/html/2510.05809v1#S4.E1 "In Theorem 4.1 (Robust representation of CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")).

Finally, by Theorem [2.1](https://arxiv.org/html/2510.05809v1#S2.Thmtheorem1 "Theorem 2.1 (Robust representation of CRMs). ‣ 2 Preliminaries ‣ Coherent estimation of risk measures"), the convexity Mρ^n∗M^{\*}\_{\hat{\rho}\_{n}} and the existence of the maximizer a∗a^{\*} follow at once. The poof is complete.
∎

In contrast to Theorem [2.1](https://arxiv.org/html/2510.05809v1#S2.Thmtheorem1 "Theorem 2.1 (Robust representation of CRMs). ‣ 2 Preliminaries ‣ Coherent estimation of risk measures"), Theorem [4.1](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem1 "Theorem 4.1 (Robust representation of CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") does not require any additional assumptions on the domain of the underlying mapping. The reason is that for any fixed n∈ℕn\in\mathbb{N}, the realized samples 𝐱\mathbf{x} are elements of the finite-dimensional space ℝn\mathbb{R}^{n}. Consequently, we do not impose any restrictions on the sampling scheme, such as the distribution from which the samples are drawn.
Also, Theorem [4.1](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem1 "Theorem 4.1 (Robust representation of CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") accommodates general non-i.i.d. setups, including sampling from time series models or scenario weighting. Nevertheless, in most practical applications, one is typically interested in estimators whose value does not depend on the order of the sampling.

Let us now derive a version of Theorem [4.1](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem1 "Theorem 4.1 (Robust representation of CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") for law-invariant CREs. This representation is based on the sorted sample s​(𝐱)s(\mathbf{x}), which reflects an important practical aspect: in real-life risk management applications, the first step is usually to sort the observed P&Ls (i.e., construct the empirical distribution) before performing the risk computations. We already mentioned that CRE representations are interlinked with LL-estimators. The next result states that any law-invariant CRE could be represented as a suprema over a family of LL-estimators.

###### Theorem 4.2 (Robust representation of law-invariant CREs).

A function ρ^n:ℝn→ℝ\hat{\rho}\_{n}\colon\mathbb{R}^{n}\to\mathbb{R} is a law-invariant CRE if and only if there exists a set Mρ^ns⊂ℳnM^{s}\_{\hat{\rho}\_{n}}\subset\mathcal{M}\_{n} satisfying a1≥a2≥…≥ana\_{1}\geq a\_{2}\geq\ldots\geq a\_{n} for any a=(a1,…,an)∈Mρ^nsa=(a\_{1},\ldots,a\_{n})\in M\_{\hat{\rho}\_{n}}^{s}, and such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ^n​(𝐱)=supa∈Mρ^ns⟨a,−s​(𝐱)⟩,𝐱∈ℝn.\hat{\rho}\_{n}(\mathbf{x})=\sup\_{a\in M\_{\hat{\rho}\_{n}}^{s}}\langle a,-s(\mathbf{x})\rangle,\quad\mathbf{x}\in\mathbb{R}^{n}. |  | (4.3) |

Moreover, Mρ^nsM\_{\hat{\rho}\_{n}}^{s} can be chosen as a convex set for which the supremum is attained, that is, for any 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n} there exist weights as=as​(𝐱)∈Mρ^nsa^{s}=a^{s}(\mathbf{x})\in M\_{\hat{\rho}\_{n}}^{s}, such that ρ^n​(𝐱)=⟨as,−s​(𝐱)⟩\hat{\rho}\_{n}(\mathbf{x})=\langle a^{s},-s(\mathbf{x})\rangle.

###### Proof.

First, we show that a coherent law-invariant risk estimator ρ^n\hat{\rho}\_{n} admits the representation ([4.3](https://arxiv.org/html/2510.05809v1#S4.E3 "In Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")). By Theorem [4.1](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem1 "Theorem 4.1 (Robust representation of CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"),
there exists a convex set Mρ^ns⊂ℳnM^{s}\_{\hat{\rho}\_{n}}\subset\mathcal{M}\_{n} such that ρ^n​(𝐱)=supa∈Mρ^ns⟨a,−𝐱⟩\hat{\rho}\_{n}(\mathbf{x})=\sup\_{a\in M^{s}\_{\hat{\rho}\_{n}}}\langle a,-\mathbf{x}\rangle, ∀𝐱∈ℝn\forall\mathbf{x}\in\mathbb{R}^{n}, and the supremum is attained. Now, we show that the coordinates of a∈Mρ^nsa\in M^{s}\_{\hat{\rho}\_{n}} must be non-increasing. Indeed, by the law-invariance of ρ^n\hat{\rho}\_{n},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ^n​(𝐱)=ρ^n​(s​(𝐱))=supa∈Mρ^ns⟨a,−s​(𝐱)⟩=ρ^n​(σ​(𝐱))=supa∈Mρ^ns⟨a,−σ​(𝐱)⟩,𝐱∈ℝn,σ∈Sn.\hat{\rho}\_{n}(\mathbf{x})=\hat{\rho}\_{n}(s(\mathbf{x}))=\sup\_{a\in M^{s}\_{\hat{\rho}\_{n}}}\langle a,-s(\mathbf{x})\rangle=\hat{\rho}\_{n}(\sigma(\mathbf{x}))=\sup\_{a\in M^{s}\_{\hat{\rho}\_{n}}}\langle a,-\sigma(\mathbf{x})\rangle,\quad\mathbf{x}\in\mathbb{R}^{n},\ \sigma\in S\_{n}. |  | (4.4) |

Moreover, we can assume that Mρ^nsM^{s}\_{\hat{\rho}\_{n}} consists only of the elements for which the supremum in ([4.1](https://arxiv.org/html/2510.05809v1#S4.E1 "In Theorem 4.1 (Robust representation of CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")) is attained.
Hence, for any as∈Mρ^nsa^{s}\in M^{s}\_{\hat{\rho}\_{n}} we can find 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n} such that supa∈Mρ^ns⟨a,−s​(𝐱)⟩=⟨as,−s​(𝐱)⟩\sup\_{a\in M^{s}\_{\hat{\rho}\_{n}}}\langle a,-s(\mathbf{x})\rangle=\langle a^{s},-s(\mathbf{x})\rangle. Then, by ([4.4](https://arxiv.org/html/2510.05809v1#S4.E4 "In 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")), for any σ∈Sn\sigma\in S\_{n}, we also have

|  |  |  |
| --- | --- | --- |
|  | ⟨−as,σ​(𝐱)⟩=⟨as,−σ​(𝐱)⟩≤supa∈Mρ^ns⟨a,−σ​(𝐱)⟩=⟨as,−s​(𝐱)⟩=⟨−as,s​(𝐱)⟩.\langle-a^{s},\sigma(\mathbf{x})\rangle=\langle a^{s},-\sigma(\mathbf{x})\rangle\leq\sup\_{a\in M^{s}\_{\hat{\rho}\_{n}}}\langle a,-\sigma(\mathbf{x})\rangle=\langle a^{s},-s(\mathbf{x})\rangle=\langle-a^{s},s(\mathbf{x})\rangle. |  |

From here, in view of [Hardy et al., [1988](https://arxiv.org/html/2510.05809v1#bib.bib39), Theorem 369], we deduce that the coordinates of −as-a^{s} and s​(𝐱)s(\mathbf{x}) have
the same monotonicity. Since the coordinates of s​(𝐱)s(\mathbf{x}) are non-decreasing, same are the coordinates of −as-a^{s}. This concludes the proof of this part.

Next, we show that the map defined in ([4.3](https://arxiv.org/html/2510.05809v1#S4.E3 "In Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")) for some fixed set Mρ^ns⊂ℳnM^{s}\_{\hat{\rho}\_{n}}\subset\mathcal{M}\_{n} of vectors with non-increasing coordinates is a law-invariant CRE. The law-invariance property follows at once. As far as coherence, properties (E1)-(E4), we show here only the subadditivity property (E4), since the remaining properties are straightforward to verify. For any a∈Mρ^nsa\in M^{s}\_{\hat{\rho}\_{n}}, using the monotonicity of the coordinates of aa, we claim that there exists b=(b1,…,bn)∈ℳnb=(b\_{1},\ldots,b\_{n})\in\mathcal{M}\_{n} such that, for any 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨a,−s​(𝐱)⟩=−∑i=1nai​xi:n=∑i=1nbi​ES^i/n1​(𝐱),\langle a,-s(\mathbf{x})\rangle=-\sum\_{i=1}^{n}a\_{i}x\_{i:n}=\sum\_{i=1}^{n}b\_{i}\widehat{\operatorname{\mathrm{ES}}}^{1}\_{i/n}(\mathbf{x}), |  | (4.5) |

where, as in ([3.1](https://arxiv.org/html/2510.05809v1#S3.E1 "In Example 3.5 (Average tail loss ES estimator is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures")), we have ES^i/n1​(𝐱)=−1i​∑j=1ixj:n\widehat{\operatorname{\mathrm{ES}}}^{1}\_{i/n}(\mathbf{x})=-\frac{1}{i}\sum\_{j=1}^{i}x\_{j:n}.
Indeed,

|  |  |  |
| --- | --- | --- |
|  | −∑i=1nai​xi:n=−∑i=1n(∑j=in−1(aj−aj+1)+an)​xi:n=−∑i=1n−1(∑j=in−1(aj−aj+1))​xi:n−∑i=1nan​xi:n.\displaystyle-\sum\_{i=1}^{n}a\_{i}x\_{i:n}=-\sum\_{i=1}^{n}\left(\sum\_{j=i}^{n-1}(a\_{j}-a\_{j+1})+a\_{n}\right)x\_{i:n}=-\sum\_{i=1}^{n-1}\left(\sum\_{j=i}^{n-1}(a\_{j}-a\_{j+1})\right)x\_{i:n}-\sum\_{i=1}^{n}a\_{n}x\_{i:n}. |  |

We note that −∑i=1nan​xi:n=an​n​ES^n/n1​(𝐱)-\sum\_{i=1}^{n}a\_{n}x\_{i:n}=a\_{n}n\widehat{\operatorname{\mathrm{ES}}}^{1}\_{n/n}(\mathbf{x}), and by changing the order of summation above, we also get

|  |  |  |
| --- | --- | --- |
|  | −∑i=1n−1(∑j=in−1(aj−aj+1))​xi:n=−∑i=1n−1(ai−ai+1)​∑j=1ixj:n=∑i=1n−1(ai−ai+1)​i​ES^i/n1​(𝐱).\displaystyle-\sum\_{i=1}^{n-1}\left(\sum\_{j=i}^{n-1}(a\_{j}-a\_{j+1})\right)x\_{i:n}=-\sum\_{i=1}^{n-1}(a\_{i}-a\_{i+1})\sum\_{j=1}^{i}x\_{j:n}=\sum\_{i=1}^{n-1}(a\_{i}-a\_{i+1})i\widehat{\operatorname{\mathrm{ES}}}^{1}\_{i/n}(\mathbf{x}). |  |

Thus, setting bi:=(ai−ai+1)​ib\_{i}:=(a\_{i}-a\_{i+1})i, i=1,…,n−1i=1,\ldots,n-1, and bn:=n​anb\_{n}:=na\_{n} we obtain ([4.5](https://arxiv.org/html/2510.05809v1#S4.E5 "In 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")). We remark that bb is independent of 𝐱\mathbf{x}, and by direct calculation we also have ∑i=1nbi=∑i=1nai=1\sum\_{i=1}^{n}b\_{i}=\sum\_{i=1}^{n}a\_{i}=1. Thus, by the monotonicity of (ai)(a\_{i}) we also obtain that bi≥0b\_{i}\geq 0, so b=(b1,…,bn)∈ℳnb=(b\_{1},\ldots,b\_{n})\in\mathcal{M}\_{n}.

By Example [3.5](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem5 "Example 3.5 (Average tail loss ES estimator is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures"), the map 𝐱→ES^i/n1​(𝐱)\mathbf{x}\to\widehat{\operatorname{\mathrm{ES}}}^{1}\_{i/n}(\mathbf{x}) is a CRE, for any ii. Consequentially, for any 𝐱,𝐲∈ℝn\mathbf{x},\mathbf{y}\in\mathbb{R}^{n}, using ([4.5](https://arxiv.org/html/2510.05809v1#S4.E5 "In 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")), we obtain

|  |  |  |
| --- | --- | --- |
|  | ⟨a,−s​(𝐱+𝐲)⟩=∑i=1nbi​ES^i/n1​(𝐱+𝐲)≤∑i=1nbi​ES^i/n1​(𝐱)+∑i=1nbi​ES^i/n1​(𝐲)=⟨a,−s​(𝐱)⟩+⟨a,−s​(𝐲)⟩.\langle a,-s(\mathbf{x}+\mathbf{y})\rangle=\sum\_{i=1}^{n}b\_{i}\widehat{\operatorname{\mathrm{ES}}}^{1}\_{i/n}(\mathbf{x+y})\leq\sum\_{i=1}^{n}b\_{i}\widehat{\operatorname{\mathrm{ES}}}^{1}\_{i/n}(\mathbf{x})+\sum\_{i=1}^{n}b\_{i}\widehat{\operatorname{\mathrm{ES}}}^{1}\_{i/n}(\mathbf{y})=\langle a,-s(\mathbf{x})\rangle+\langle a,-s(\mathbf{y})\rangle. |  |

Finally, taking here the supremum over a∈Mρ^nsa\in M\_{\hat{\rho}\_{n}}^{s}, we deduce that ρ^n​(𝐱+𝐲)≤ρ^n​(𝐱)+ρ^n​(𝐲)\hat{\rho}\_{n}(\mathbf{x}+\mathbf{y})\leq\hat{\rho}\_{n}(\mathbf{x})+\hat{\rho}\_{n}(\mathbf{y}), which concludes the proof.
∎

###### Remark 4.3.

The weights set Mρ^nsM^{s}\_{\hat{\rho}\_{n}} in the representation ([4.3](https://arxiv.org/html/2510.05809v1#S4.E3 "In Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")) is generally not unique. To provide an illustrative example, set ρ^n​(𝐱):=−mini⁡xi\hat{\rho}\_{n}(\mathbf{x}):=-\min\_{i}x\_{i}, for 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n}. This is a law-invariant CRE since mini⁡xi=x1:n\min\_{i}x\_{i}=x\_{1:n}. Now, let M′:={(1,0,…,0)}M^{\prime}:=\{(1,0,\ldots,0)\} and M′′:={(1−1/k,1/k,0,…,0):k∈ℕ,k≥2}M^{\prime\prime}:=\{(1-1/k,1/k,0,\ldots,0)\colon k\in\mathbb{N},k\geq 2\}. Then,
ρ^n​(𝐱)=supa∈M′⟨a,−s​(𝐱)⟩=supa∈M′′⟨a,−s​(𝐱)⟩\hat{\rho}\_{n}(\mathbf{x})=\sup\_{a\in M^{\prime}}\langle a,-s(\mathbf{x})\rangle=\sup\_{a\in M^{\prime\prime}}\langle a,-s(\mathbf{x})\rangle, for any 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n}.

The representation result in Theorem [4.2](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem2 "Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") is consistent with the corresponding result for law-invariant CRMs obtained in Kusuoka [[2001](https://arxiv.org/html/2510.05809v1#bib.bib44)]. However, this does not imply that a supremum over LL-statistics should always be used when estimating a law-invariant CRM, since law-invariance of CREs depends both on the estimation method and on the underlying CRM itself (cf. the comment following Definition [3.2](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem2 "Definition 3.2 (Law-invariant estimator). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures")).

In the next section, we further examine the connection between LL-estimators and CREs. In particular, we show that under comonotonicity, the supremum in Theorem [4.2](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem2 "Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") can be omitted. Before doing so, for completeness, we describe the relationship between the sets Mρ^n∗M\_{\hat{\rho}\_{n}}^{\*} and Mρ^nsM\_{\hat{\rho}\_{n}}^{s} from Theorems [4.1](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem1 "Theorem 4.1 (Robust representation of CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") and [4.2](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem2 "Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"), and present some illustrative examples.

###### Proposition 4.4 (Link between robust representations for general and law-invariant CREs).

Let ρ^n:ℝn→ℝ\hat{\rho}\_{n}\colon\mathbb{R}^{n}\to\mathbb{R} be a law-invariant CRE admitting representation ρ^n​(𝐱)=supa∈Mρ^ns⟨a,−s​(𝐱)⟩\hat{\rho}\_{n}(\mathbf{x})=\sup\_{a\in M^{s}\_{\hat{\rho}\_{n}}}\langle a,-s(\mathbf{x})\rangle, where 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n} and Mρ^ns⊂ℳnM^{s}\_{\hat{\rho}\_{n}}\subset\mathcal{M}\_{n} is such that a1≥a2≥…≥ana\_{1}\geq a\_{2}\geq\ldots\geq a\_{n} for a∈Mρ^nsa\in M^{s}\_{\hat{\rho}\_{n}}. Then, we have

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(𝐱)=supa∈Mρ^nσ⟨a,−𝐱⟩,𝐱∈ℝn,\hat{\rho}\_{n}(\mathbf{x})=\sup\_{a\in M\_{\hat{\rho}\_{n}}^{\sigma}}\langle a,-\mathbf{x}\rangle,\quad\mathbf{x}\in\mathbb{R}^{n}, |  |

where Mρ^nσ:={σ​(a):σ∈Sn,a∈Mρ^ns}M\_{\hat{\rho}\_{n}}^{\sigma}:=\{\sigma(a)\colon\sigma\in S\_{n},a\in M^{s}\_{\hat{\rho}\_{n}}\}.

###### Proof.

Note that, for any σ∈Sn\sigma\in S\_{n}, a∈ℳna\in\mathcal{M}\_{n} and 𝐱∈𝐑n\mathbf{x}\in\mathbf{R}^{n}, we have ⟨σ​(a),𝐱⟩=⟨a,σ−1​(𝐱)⟩\langle\sigma(a),\mathbf{x}\rangle=\langle a,\sigma^{-1}(\mathbf{x})\rangle, where σ−1\sigma^{-1} is the inverse permutation. Then, we obtain

|  |  |  |
| --- | --- | --- |
|  | supa∈Mρ^nσ⟨a,−𝐱⟩=supa∈Mρ^nsσ∈Sn⟨σ​(a),−𝐱⟩=supa∈Mρ^nsσ∈Sn⟨a,−σ−1​(𝐱)⟩≥supa∈Mρ^ns⟨a,−s​(𝐱)⟩=ρ^n​(𝐱),\displaystyle\sup\_{a\in M\_{\hat{\rho}\_{n}}^{\sigma}}\langle a,-\mathbf{x}\rangle=\sup\_{\begin{subarray}{c}a\in M^{s}\_{\hat{\rho}\_{n}}\\ \sigma\in S\_{n}\end{subarray}}\langle\sigma(a),-\mathbf{x}\rangle=\sup\_{\begin{subarray}{c}a\in M^{s}\_{\hat{\rho}\_{n}}\\ \sigma\in S\_{n}\end{subarray}}\langle a,-\sigma^{-1}(\mathbf{x})\rangle\geq\sup\_{\begin{subarray}{c}a\in M^{s}\_{\hat{\rho}\_{n}}\end{subarray}}\langle a,-s(\mathbf{x})\rangle=\hat{\rho}\_{n}(\mathbf{x}), |  |

where the inequality follows from the fact that s​(𝐱)=σ0−1​(𝐱)s(\mathbf{x})=\sigma\_{0}^{-1}(\mathbf{x}) for some permutation σ0∈Sn\sigma\_{0}\in S\_{n}. On the other hand, using the rearrangement inequality [Hardy et al., [1988](https://arxiv.org/html/2510.05809v1#bib.bib39), Theorem 368]), for any a∈Mρ^nsa\in M^{s}\_{\hat{\rho}\_{n}} and σ∈Sn\sigma\in S\_{n}, we obtain

|  |  |  |
| --- | --- | --- |
|  | ⟨a,−σ​(𝐱)⟩≤⟨a,−s​(𝐱)⟩,\langle a,-\sigma(\mathbf{x})\rangle\leq\langle a,-s(\mathbf{x})\rangle, |  |

which concludes the proof.
∎

Now, we show specific formulas for the sets Mρ^M\_{\hat{\rho}} for some specific families of risk measures and show how they are related to estimation formulas.

###### Example 4.5 (Robust representation of average tail loss ES estimator).

Let us fix n∈ℕn\in\mathbb{N}, α∈(0,1)\alpha\in(0,1), and consider a non-parametric estimator ES^α,n1\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,n} defined in Example [3.5](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem5 "Example 3.5 (Average tail loss ES estimator is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures"), see ([3.1](https://arxiv.org/html/2510.05809v1#S3.E1 "In Example 3.5 (Average tail loss ES estimator is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures")). Then, it is easy to show that ES^α,n1\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,n} admits a law-invariant robust representation from Theorem [4.2](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem2 "Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") with the set

|  |  |  |
| --- | --- | --- |
|  | MES^α,n1s:={(a1,…,an):ai:=1⌊n​α⌋​𝟙{i≤⌊n​α⌋},i=1,2​…,n}.M^{s}\_{\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,n}}:=\left\{(a\_{1},\ldots,a\_{n})\colon a\_{i}:=\frac{1}{\lfloor n\alpha\rfloor}\mathbbm{1}\_{\{i\leq\lfloor n\alpha\rfloor\}},\,i=1,2\ldots,n\right\}. |  |

□\square

###### Example 4.6 (Robust representation of CREs based on order statistics).

The weighting scheme introduced in Example [4.5](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem5 "Example 4.5 (Robust representation of average tail loss ES estimator). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") that leads to estimator ES^α,n1\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,n} could be modified. In particular, this could lead to alternative ES estimators such as ES^α,n2\widehat{\operatorname{\mathrm{ES}}}^{2}\_{\alpha,n} defined in ([3.4](https://arxiv.org/html/2510.05809v1#S3.E4 "In Example 3.7 (Non-parametric plug-in ES estimator is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures")). Namely, for a fixed n∈ℕn\in\mathbb{N} and α∈(0,1)\alpha\in(0,1), let us consider the risk estimator

|  |  |  |  |
| --- | --- | --- | --- |
|  | R^α,nq​(𝐱):=−∑i=1⌊n​α⌋+1qi​xi:n,\widehat{R}^{q}\_{\alpha,n}(\mathbf{x}):=-\sum\_{i=1}^{\lfloor n\alpha\rfloor+1}q\_{i}x\_{i:n}, |  | (4.6) |

where a single q:=(q1,…,q⌊n​α⌋+1,0,…,0)∈ℳnq:=(q\_{1},\ldots,q\_{\lfloor n\alpha\rfloor+1},0,\ldots,0)\in\mathcal{M}\_{n} is fixed and such that q1≥q2≥…≥q⌊n​α⌋+1q\_{1}\geq q\_{2}\geq\ldots\geq q\_{\lfloor n\alpha\rfloor+1}. Then, from Theorem [4.2](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem2 "Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") with the supremum being the single element, we get that

|  |  |  |
| --- | --- | --- |
|  | MR^α,nqs:={q}M^{s}\_{\widehat{R}^{q}\_{\alpha,n}}:=\{q\} |  |

is a robust representation set for R^α,nq\widehat{R}^{q}\_{\alpha,n}, and this measure is a law-invariant CRE. ∎

###### Example 4.7 (Robust representation of CREs based on suprema of order statistics).

The class of law-invariant CREs considered in Example [4.6](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem6 "Example 4.6 (Robust representation of CREs based on order statistics). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") could be further generalized by considering the suprema of weighted order statistics. Let us consider the risk estimator

|  |  |  |  |
| --- | --- | --- | --- |
|  | R^α,n​(𝐱):=supq∈QR^α,nq​(𝐱).\widehat{R}\_{\alpha,n}(\mathbf{x}):=\sup\_{q\in Q}\widehat{R}^{q}\_{\alpha,n}(\mathbf{x}). |  | (4.7) |

where Q⊂ℳnQ\subset\mathcal{M}\_{n} is such that any q∈Qq\in Q satisfies the same conditions as in Examples [4.6](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem6 "Example 4.6 (Robust representation of CREs based on order statistics). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"), and R^α,nq\widehat{R}^{q}\_{\alpha,n} is defined in ([4.6](https://arxiv.org/html/2510.05809v1#S4.E6 "In Example 4.6 (Robust representation of CREs based on order statistics). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")). Then, from Theorem [4.2](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem2 "Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"), we get that

|  |  |  |
| --- | --- | --- |
|  | MR^α,ns:=QM^{s}\_{\widehat{R}\_{\alpha,n}}:=Q |  |

is a robust representation set for R^α,n\widehat{R}\_{\alpha,n}, and this risk measure a law-invariant CRE. □\square

In contrast to Example [4.5](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem5 "Example 4.5 (Robust representation of average tail loss ES estimator). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") and Example [4.6](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem6 "Example 4.6 (Robust representation of CREs based on order statistics). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"), the order statistic weighting scheme in Example [4.7](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem7 "Example 4.7 (Robust representation of CREs based on suprema of order statistics). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") could depend on a sample realization, that is, different values of qq could attain a supremum in ([4.7](https://arxiv.org/html/2510.05809v1#S4.E7 "In Example 4.7 (Robust representation of CREs based on suprema of order statistics). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")) for different samples 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n}.

To provide further illustration, let us consider a CRM that has a different structure than ES, and study the dual representation of the corresponding plug-in CRE.

###### Example 4.8 (Robust representation of non-parametric estimator of expectile value at risk).

In this example we consider expectile value at risk (ExpVaR\operatorname{ExpVaR}) family of risk measures indexed by a significance level α∈(0,1/2)\alpha\in(0,1/2). This family identifies an important class of law-invariant risk measures which are both CRM and elicitable, see Bellini and Di Bernardino [[2017](https://arxiv.org/html/2510.05809v1#bib.bib14)], Bellini et al. [[2019](https://arxiv.org/html/2510.05809v1#bib.bib15)], Embrechts et al. [[2022](https://arxiv.org/html/2510.05809v1#bib.bib32)] for more details. The ExpVaR\operatorname{ExpVaR} at significance level α∈(0,1/2)\alpha\in(0,1/2) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ExpVaRα⁡(X):=−arg​minc∈ℝ⁡(α​𝔼​[(X−c)+2]+(1−α)​𝔼​[(X−c)−2]),X∈𝒳,\operatorname{ExpVaR}\_{\alpha}(X):=-\operatorname\*{arg\,min}\_{c\in\mathbb{R}}\left(\alpha\mathbb{E}[(X-c)\_{+}^{2}]+(1-\alpha)\mathbb{E}[(X-c)\_{-}^{2}]\right),\quad X\in\mathcal{X}, |  | (4.8) |

where (b)+:=max⁡(b,0)(b)\_{+}:=\max(b,0) and (b)−:=max⁡(−b,0)(b)\_{-}:=\max(-b,0). For 𝒳=L1\mathcal{X}=L^{1}, we have ExpVaRα⁡(X)=−eα​(X)\operatorname{ExpVaR}\_{\alpha}(X)=-e\_{\alpha}(X), where eα​(X)e\_{\alpha}(X) is the α\alpha-expectile of XX, that is, a unique solution to the equation α​𝔼​[(X−eα​(X))+]−(1−α)​𝔼​[(X−eα​(X))−]=0\alpha\mathbb{E}[(X-e\_{\alpha}(X))\_{+}]-(1-\alpha)\mathbb{E}[(X-e\_{\alpha}(X))\_{-}]=0.
Using this representation and Proposition [3.3](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem3 "Proposition 3.3 (Empirical plug-in risk estimator for CRM is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures"), we can implicitly define a non-parametric plug-in estimator of ExpVaR\operatorname{ExpVaR} by setting

|  |  |  |  |
| --- | --- | --- | --- |
|  | ExpVaR^α,n​(𝐱):=−e^α​(𝐱),\widehat{\operatorname{ExpVaR}}\_{\alpha,n}(\mathbf{x}):=-\hat{e}\_{\alpha}(\mathbf{x}), |  | (4.9) |

where the empirical expectile e^α​(𝐱)\hat{e}\_{\alpha}(\mathbf{x}) is defined as a solution to equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | α​1n​∑i=1n[xi−e^α​(𝐱)]+−(1−α)​1n​∑i=1n[xi−e^α​(𝐱)]−=0.\alpha\frac{1}{n}\sum\_{i=1}^{n}[x\_{i}-\hat{e}\_{\alpha}(\mathbf{x})]\_{+}-(1-\alpha)\frac{1}{n}\sum\_{i=1}^{n}[x\_{i}-\hat{e}\_{\alpha}(\mathbf{x})]\_{-}=0. |  | (4.10) |

Now, let n∗​(𝐱)n^{\*}(\mathbf{x}) be such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | n⋆​(𝐱):=sup{k∈{1,…,n}:xk:n≤e^α​(𝐱)}.n^{\star}(\mathbf{x}):=\sup\{k\in\{1,\ldots,n\}\colon x\_{k:n}\leq\hat{e}\_{\alpha}(\mathbf{x})\}. |  | (4.11) |

Then, we can rewrite ([4.10](https://arxiv.org/html/2510.05809v1#S4.E10 "In Example 4.8 (Robust representation of non-parametric estimator of expectile value at risk). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")) as

|  |  |  |
| --- | --- | --- |
|  | (1−α)​∑i=1n⋆​(𝐱)(xi:n−e^α​(𝐱))+α​∑i=n⋆​(𝐱)+1n(xi:n−e^α​(𝐱))=0.(1-\alpha)\sum\_{i=1}^{n^{\star}(\mathbf{x})}(x\_{i:n}-\hat{e}\_{\alpha}(\mathbf{x}))+\alpha\sum\_{i=n^{\star}(\mathbf{x})+1}^{n}(x\_{i:n}-\hat{e}\_{\alpha}(\mathbf{x}))=0. |  |

Hence, e^α​(𝐱)\hat{e}\_{\alpha}(\mathbf{x}) satisfies

|  |  |  |
| --- | --- | --- |
|  | e^α​(𝐱)=1−α(1−2​α)​n⋆​(𝐱)+n​α​∑i=1n⋆​(𝐱)xi:n+α(1−2​α)​n⋆​(𝐱)+n​α​∑i=n⋆​(𝐱)+1nxi:n.\hat{e}\_{\alpha}(\mathbf{x})=\frac{1-\alpha}{(1-2\alpha)n^{\star}(\mathbf{x})+n\alpha}\sum\_{i=1}^{n^{\star}(\mathbf{x})}x\_{i:n}+\frac{\alpha}{(1-2\alpha)n^{\star}(\mathbf{x})+n\alpha}\sum\_{i=n^{\star}(\mathbf{x})+1}^{n}x\_{i:n}. |  |

Consequently, ExpVaR^\widehat{\operatorname{ExpVaR}} admits the following representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ExpVaR^α,n​(𝐱)=−(∑i=1n⋆​(𝐱)1−α(1−2​α)​n⋆​(𝐱)+n​α​xi:n+∑i=n⋆​(𝐱)+1nα(1−2​α)​n⋆​(𝐱)+n​α​xi:n)=⟨a⋆​(𝐱),−s​(𝐱)⟩,\widehat{\operatorname{ExpVaR}}\_{\alpha,n}(\mathbf{x})=-\left(\sum\_{i=1}^{n^{\star}(\mathbf{x})}\frac{1-\alpha}{(1-2\alpha)n^{\star}(\mathbf{x})+n\alpha}x\_{i:n}+\sum\_{i=n^{\star}(\mathbf{x})+1}^{n}\frac{\alpha}{(1-2\alpha)n^{\star}(\mathbf{x})+n\alpha}x\_{i:n}\right)=\langle a^{\star}(\mathbf{x}),-s(\mathbf{x})\rangle, |  | (4.12) |

where ai⋆​(𝐱):=(1−α)(1−2​α)​n⋆​(𝐱)+n​αa^{\star}\_{i}(\mathbf{x}):=\frac{(1-\alpha)}{(1-2\alpha)n^{\star}(\mathbf{x})+n\alpha} for i=1,…,n⋆​(𝐱)i=1,\ldots,n^{\star}(\mathbf{x}), and ai⋆​(𝐱):=α(1−2​α)​n⋆​(𝐱)+n​αa^{\star}\_{i}(\mathbf{x}):=\frac{\alpha}{(1-2\alpha)n^{\star}(\mathbf{x})+n\alpha} for i=n⋆​(𝐱)+1,…,ni=n^{\star}(\mathbf{x})+1,\ldots,n. As we later illustrate in Example [4.12](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem12 "Example 4.12 (Non-comonotonicity of ExpVaR estimator). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"), a⋆​(𝐱)a^{\star}(\mathbf{x}) is different for different samples 𝐱\mathbf{x}. Using the fact that expectile value at risk is coherent, we can also recover the robust representation of ExpVaR^α,n\widehat{\operatorname{ExpVaR}}\_{\alpha,n} from Theorem [4.2](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem2 "Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"). Indeed, one can show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ExpVaR^α,n​(𝐱)=supa∈MExpVaR^α,ns⟨a,−s​(𝐱)⟩,\widehat{\operatorname{ExpVaR}}\_{\alpha,n}(\mathbf{x})=\sup\_{a\in M^{s}\_{\widehat{\operatorname{ExpVaR}}\_{\alpha,n}}}\langle a,-s(\mathbf{x})\rangle, |  | (4.13) |

where MExpVaR^α,ns:={a⋆​(𝐱):𝐱∈ℝn}M^{s}\_{\widehat{\operatorname{ExpVaR}}\_{\alpha,n}}:=\{a^{\star}(\mathbf{x})\colon\mathbf{x}\in\mathbb{R}^{n}\}. □\square

### 4.1 Comonotonic CREs and their representation as L-estimators

We recall that in statistical analysis an LL-estimator is a linear combination of the order statistics (xi:n)i=1,…,n(x\_{i:n})\_{i=1,\ldots,n}, see [van der Vaart, [1998](https://arxiv.org/html/2510.05809v1#bib.bib61), Section 22] or David and Nagaraja [[2003](https://arxiv.org/html/2510.05809v1#bib.bib26)] for details. Thus, certain risk estimators – such as the ES estimator ES^α,n1​(𝐱)\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,n}(\mathbf{x}) given in Example [3.5](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem5 "Example 3.5 (Average tail loss ES estimator is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures") or the VaR\operatorname{\mathrm{VaR}} estimator VaR^α,n​(𝐱)\widehat{\operatorname{\mathrm{VaR}}}\_{\alpha,n}(\mathbf{x}) given in Example [3.6](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem6 "Example 3.6 (Empirical quantile VaR estimator is not coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures") – are specific instances of LL-statistics. More generally, in view of Theorem [4.2](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem2 "Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") and Proposition [4.4](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem4 "Proposition 4.4 (Link between robust representations for general and law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"), a law-invariant CRE is a supremum over a set of LL-estimators.
For any generic risk measure ρ\rho, from both practical and computational perspectives, it is desirable for the set Mρ^nsM^{s}\_{\hat{\rho}\_{n}} in ([4.3](https://arxiv.org/html/2510.05809v1#S4.E3 "In Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")) to be small – ideally a singleton – as is the case in Example [4.5](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem5 "Example 4.5 (Robust representation of average tail loss ES estimator). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"), where ES^α,n1​(𝐱)\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,n}(\mathbf{x}) is represented via the singleton set MES^α,n1sM^{s}\_{\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,n}}. Indeed, for any a∈ℳna\in\mathcal{M}\_{n} such that a1≥a2≥…≥ana\_{1}\geq a\_{2}\geq\ldots\geq a\_{n}, the value ⟨a,−s​(𝐱)⟩=−∑i=1nai​xi:n\langle a,-s(\mathbf{x})\rangle=-\sum\_{i=1}^{n}a\_{i}x\_{i:n} has a natural interpretation, since it could be seen as an empirical form of an average (or weighted) VaR, in which VaR estimates are represented by order statistics. This shows that such estimators are related to a large and important class of CRMs; cf. [Acerbi, [2002](https://arxiv.org/html/2510.05809v1#bib.bib2), Theorem 2.5], [Föllmer and Schied, [2016](https://arxiv.org/html/2510.05809v1#bib.bib36), Section 4.4], and Remark [4.13](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem13 "Remark 4.13 (Robust representation weights for CRE and risk spectrum). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") for more details. The aim of this section is to provide sufficient conditions for Mρ^nsM^{s}\_{\hat{\rho}\_{n}} to be a singleton, using the comonotonicity property.

We recall that two vectors 𝐱,𝐲∈ℝn\mathbf{x},\mathbf{y}\in\mathbb{R}^{n} are comonotonic if
(xi−xj)​(yi−yj)≥0(x\_{i}-x\_{j})(y\_{i}-y\_{j})\geq 0, for i,j=1,…,ni,j=1,\ldots,n.
In other words, the coordinates of 𝐱\mathbf{x} and 𝐲\mathbf{y} are jointly increasing or decreasing. Comonotonicity has been transferred to the theory of risk measures, where a simplified form of dual representation for law-invariant and comonotonic risk measure has been provided, see Kusuoka [[2001](https://arxiv.org/html/2510.05809v1#bib.bib44)]. Let us formulate and study this property in the context of risk estimators.

###### Definition 4.9 (Comonotonic estimator).

A function ρ^n:ℝn→ℝ\hat{\rho}\_{n}\colon\mathbb{R}^{n}\to\mathbb{R} is comonotonic if ρ^n​(𝐱+𝐲)=ρ^n​(𝐱)+ρ^n​(𝐲)\hat{\rho}\_{n}(\mathbf{x}+\mathbf{y})=\hat{\rho}\_{n}(\mathbf{x})+\hat{\rho}\_{n}(\mathbf{y}) for any comonotonic vectors 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n} and 𝐲∈ℝn\mathbf{y}\in\mathbb{R}^{n}.

As we show next, for any comonotonic law-invariant CRE, the set Mρ^nsM^{s}\_{\hat{\rho}\_{n}} can be chosen as a singleton, a result that may be viewed as a version of [Kusuoka, [2001](https://arxiv.org/html/2510.05809v1#bib.bib44), Theorem 7] adapted to CREs.

###### Theorem 4.10 (Robust representation of comonotonic and law-invariant CREs).

A risk estimator ρ^n:ℝn→ℝ\hat{\rho}\_{n}\colon\mathbb{R}^{n}\to\mathbb{R} is a comonotonic law-invariant CRE if and only if there exists a unique a=(a1,…,an)∈ℳna=(a\_{1},\ldots,a\_{n})\in\mathcal{M}\_{n} satisfying a1≥a2≥…≥ana\_{1}\geq a\_{2}\geq\ldots\geq a\_{n} and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ^n​(𝐱)=⟨a,−s​(𝐱)⟩,𝐱∈ℝn.\hat{\rho}\_{n}(\mathbf{x})=\langle a,-s(\mathbf{x})\rangle,\quad\mathbf{x}\in\mathbb{R}^{n}. |  | (4.14) |

###### Proof.

(⇐)(\Leftarrow) Note that Theorem [4.1](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem1 "Theorem 4.1 (Robust representation of CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") and Theorem [4.2](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem2 "Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") imply that ρ^n\hat{\rho}\_{n} defined in ([4.14](https://arxiv.org/html/2510.05809v1#S4.E14 "In Theorem 4.10 (Robust representation of comonotonic and law-invariant CREs). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")) is a law-invariant CRE. By the definition of comonotonicity, the functions 𝐱↦xi:n\mathbf{x}\mapsto x\_{i:n}, with i=1,…,ni=1,\ldots,n, are comonotonic. Thus, the map ρ^n\hat{\rho}\_{n} is comonotonic as the (negative) convex combination of comonotonic functions.

(⇒)(\Rightarrow) Assume that ρ^n\hat{\rho}\_{n} is a comonotonic law-invariant CRE, and let Mρ^ns{M}^{s}\_{\hat{\rho}\_{n}} be any representing set from Theorem [4.2](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem2 "Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"). We define

|  |  |  |
| --- | --- | --- |
|  | Nρ^n​(𝐱):={a∈Mρ^ns:ρ^n​(𝐱)=⟨a,−s​(𝐱)⟩},𝐱∈ℝn.{N}\_{\hat{\rho}\_{n}}(\mathbf{x}):=\{a\in{M}^{s}\_{\hat{\rho}\_{n}}\colon\hat{\rho}\_{n}(\mathbf{x})=\langle a,-s(\mathbf{x})\rangle\},\quad\mathbf{x}\in\mathbb{R}^{n}. |  |

In view of Theorem [4.2](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem2 "Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") and the continuity of the map a↦⟨a,−s​(𝐱)⟩a\mapsto\langle a,-s(\mathbf{x})\rangle, for any 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n}, the set Nρ^n​(𝐱){N}\_{\hat{\rho}\_{n}}(\mathbf{x}) is non-empty and closed. We show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⋂𝐱∈ℝnNρ^n​(𝐱)≠∅.\bigcap\_{\mathbf{x}\in\mathbb{R}^{n}}{N}\_{\hat{\rho}\_{n}}(\mathbf{x})\neq\emptyset. |  | (4.15) |

Then, any a∈⋂𝐱∈ℝnNρ^n​(𝐱)a\in\bigcap\_{\mathbf{x}\in\mathbb{R}^{n}}{N}\_{\hat{\rho}\_{n}}(\mathbf{x}) satisfies ([4.14](https://arxiv.org/html/2510.05809v1#S4.E14 "In Theorem 4.10 (Robust representation of comonotonic and law-invariant CREs). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")).

To prove ([4.15](https://arxiv.org/html/2510.05809v1#S4.E15 "In 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")), it is enough to show that for any K∈ℕK\in\mathbb{N}, K≥2K\geq 2, and 𝐱1,…,𝐱K∈ℝn\mathbf{x}\_{1},\ldots,\mathbf{x}\_{K}\in\mathbb{R}^{n} we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⋂i=1KNρ^n​(𝐱i)≠∅.\bigcap\_{i=1}^{K}{N}\_{\hat{\rho}\_{n}}(\mathbf{x}\_{i})\neq\emptyset. |  | (4.16) |

Indeed, if ([4.16](https://arxiv.org/html/2510.05809v1#S4.E16 "In 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")) holds and ⋂𝐱∈ℝnNρ^n​(𝐱)=∅\bigcap\_{\mathbf{x}\in\mathbb{R}^{n}}{N}\_{\hat{\rho}\_{n}}(\mathbf{x})=\emptyset, then we have ⋃𝐱∈ℝn(ℳn∖Nρ^n​(𝐱))=ℳn\bigcup\_{\mathbf{x}\in\mathbb{R}^{n}}(\mathcal{M}\_{n}\setminus{N}\_{\hat{\rho}\_{n}}(\mathbf{x}))=\mathcal{M}\_{n}. However, since ℳn\mathcal{M}\_{n} is compact and any ℳn∖Nρ^n​(𝐱)\mathcal{M}\_{n}\setminus{N}\_{\hat{\rho}\_{n}}(\mathbf{x}) is open, we may find 𝐱1,…,𝐱K∈ℝn\mathbf{x}\_{1},\ldots,\mathbf{x}\_{K}\in\mathbb{R}^{n} such that ⋃i=1K(ℳn∖Nρ^n​(𝐱i))=ℳn\bigcup\_{i=1}^{K}(\mathcal{M}\_{n}\setminus{N}\_{\hat{\rho}\_{n}}(\mathbf{x}\_{i}))=\mathcal{M}\_{n}, which contradicts ([4.16](https://arxiv.org/html/2510.05809v1#S4.E16 "In 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")).
Thus, to show ([4.14](https://arxiv.org/html/2510.05809v1#S4.E14 "In Theorem 4.10 (Robust representation of comonotonic and law-invariant CREs). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")), it is enough to show ([4.16](https://arxiv.org/html/2510.05809v1#S4.E16 "In 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")). Hence, let K∈ℕK\in\mathbb{N}, K≥2K\geq 2, 𝐱1,…,𝐱K∈ℝn\mathbf{x}\_{1},\ldots,\mathbf{x}\_{K}\in\mathbb{R}^{n}, and let us define 𝐱:=∑i=1Ks​(𝐱i)\mathbf{x}:=\sum\_{i=1}^{K}s(\mathbf{x}\_{i}). Also, note that for any k=1,…,K−1k=1,\ldots,K-1, the vectors ∑i=1ks​(𝐱i)\sum\_{i=1}^{k}s(\mathbf{x}\_{i}) and s​(𝐱k+1)s(\mathbf{x}\_{k+1}) are comonotonic. By comonotonicity and law-invariance, we inductively get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ^n​(𝐱)=∑i=1Kρ^n​(s​(𝐱i))=∑i=1Kρ^n​(𝐱i).\hat{\rho}\_{n}(\mathbf{x})=\sum\_{i=1}^{K}\hat{\rho}\_{n}(s(\mathbf{x}\_{i}))=\sum\_{i=1}^{K}\hat{\rho}\_{n}(\mathbf{x}\_{i}). |  | (4.17) |

Next, let a∈Nρ^n​(𝐱)a\in{N}\_{\hat{\rho}\_{n}}(\mathbf{x}), and since s​(𝐱)=𝐱s(\mathbf{x})=\mathbf{x}, we deduce

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(𝐱)=⟨a,−s​(𝐱)⟩=⟨a,−𝐱⟩=∑i=1K⟨a,−s​(𝐱i)⟩.\hat{\rho}\_{n}(\mathbf{x})=\langle a,-s(\mathbf{x})\rangle=\langle a,-\mathbf{x}\rangle=\sum\_{i=1}^{K}\langle a,-s(\mathbf{x}\_{i})\rangle. |  |

Next, note that from Nρ^n​(𝐱)⊂Mρ^ns{N}\_{\hat{\rho}\_{n}}(\mathbf{x})\subset{M}^{s}\_{\hat{\rho}\_{n}}, we have ρ^n​(𝐱i)≥⟨a,−s​(𝐱i)⟩\hat{\rho}\_{n}(\mathbf{x}\_{i})\geq\langle a,-s(\mathbf{x}\_{i})\rangle. In fact, recalling ([4.17](https://arxiv.org/html/2510.05809v1#S4.E17 "In 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")), we obtain ρ^n​(𝐱i)=⟨a,−s​(𝐱i)⟩\hat{\rho}\_{n}(\mathbf{x}\_{i})=\langle a,-s(\mathbf{x}\_{i})\rangle for any i=1,…,Ki=1,\ldots,K. Thus, a∈Nρ^n​(𝐱i)a\in{N}\_{\hat{\rho}\_{n}}(\mathbf{x}\_{i}) for any i=1,…,Ki=1,\ldots,K, which concludes the proof of ([4.14](https://arxiv.org/html/2510.05809v1#S4.E14 "In Theorem 4.10 (Robust representation of comonotonic and law-invariant CREs). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")).

Finally, we show that aa from ([4.14](https://arxiv.org/html/2510.05809v1#S4.E14 "In Theorem 4.10 (Robust representation of comonotonic and law-invariant CREs). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")) is unique. Let a1,a2∈ℳna^{1},a^{2}\in\mathcal{M}\_{n} be such that

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(𝐱)=⟨a1,−s​(𝐱)⟩=⟨a2,−s​(𝐱)⟩,𝐱∈ℝn.\hat{\rho}\_{n}(\mathbf{x})=\langle a^{1},-s(\mathbf{x})\rangle=\langle a^{2},-s(\mathbf{x})\rangle,\quad\mathbf{x}\in\mathbb{R}^{n}. |  |

Then, setting 𝐱:=(−1,0,…,0)\mathbf{x}:=(-1,0,\ldots,0) we obtain a11=ρ^n​(x)=a12a\_{1}^{1}=\hat{\rho}\_{n}(x)=a\_{1}^{2}. Next, setting 𝐱:=(−1,−1,…,0)\mathbf{x}:=(-1,-1,\ldots,0), we get
a11+a21=ρ^n​(x)=a12+a22a\_{1}^{1}+a\_{2}^{1}=\hat{\rho}\_{n}(x)=a\_{1}^{2}+a\_{2}^{2}, so a21=a22a\_{2}^{1}=a\_{2}^{2}. Thus, we inductively obtain ai1=ai2a\_{i}^{1}=a\_{i}^{2}, i=1,…,ni=1,\ldots,n, which concludes the proof.
∎

We conclude this section with two examples. In the first example, we recall the usual way of estimating spectral risk measures and show that the corresponding risk estimators are comonotonic and law-invariant CREs, while in the second example we present a numerical illustration that one cannot find unique weights for non-comonotonic risk measure estimators.

###### Example 4.11 (Non-parametric plug-in CRE for spectral risk measures).

As stated in Section [2](https://arxiv.org/html/2510.05809v1#S2 "2 Preliminaries ‣ Coherent estimation of risk measures"), the class of WVaR risk measures could be represented using spectral risk measures, see Acerbi [[2002](https://arxiv.org/html/2510.05809v1#bib.bib2)] for details. A spectral risk measure is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(X)=−∫01VaRα⁡(X)​ϕ​(α)​𝑑α,\rho(X)=-\int\_{0}^{1}\operatorname{\mathrm{VaR}}\_{\alpha}(X)\phi(\alpha)d\alpha, |  | (4.18) |

where the risk spectrum ϕ:[0,1]→ℝ+\phi\colon[0,1]\to\mathbb{R}\_{+} is (weakly) decreasing, bounded, and ∫01ϕ​(t)​𝑑t=1\int\_{0}^{1}\phi(t)dt=1. In order to estimate ([4.18](https://arxiv.org/html/2510.05809v1#S4.E18 "In Example 4.11 (Non-parametric plug-in CRE for spectral risk measures). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")), we can consider the discretised version of risk spectrum. Namely, for any n>1n>1, set ai,n:=∫i−1ninϕ​(s)​𝑑sa\_{i,n}:=\int\_{\frac{i-1}{n}}^{\frac{i}{n}}\phi(s)ds, i=1,…,ni=1,\ldots,n, and consider the risk estimator given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ^na​(𝐱)=−∑i=1nai,n​xi:n.\hat{\rho}^{a}\_{n}(\mathbf{x})=-\sum\_{i=1}^{n}a\_{i,n}x\_{i:n}. |  | (4.19) |

Clearly, due to the properties of the risk spectrum, we have ai,n≥ai+1,na\_{i,n}\geq a\_{i+1,n}, for i=1,…,n−1i=1,\ldots,n-1, and ρ^na\hat{\rho}\_{n}^{a} admits representation ([4.14](https://arxiv.org/html/2510.05809v1#S4.E14 "In Theorem 4.10 (Robust representation of comonotonic and law-invariant CREs). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")), so that it is a law-invariant and comonotonic CRE. This CRE could be seen as a natural non-parametric plug-in estimator of the corresponding spectral risk measure ([4.18](https://arxiv.org/html/2510.05809v1#S4.E18 "In Example 4.11 (Non-parametric plug-in CRE for spectral risk measures). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")), similar to the CRE discussed in Proposition [3.3](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem3 "Proposition 3.3 (Empirical plug-in risk estimator for CRM is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures"). In the next section, we establish further important properties of this estimator. □\square

###### Example 4.12 (Non-comonotonicity of ExpVaR estimator).

Let ExpVaR^\widehat{\operatorname{ExpVaR}} be the law-invariant CRE defined in ([4.9](https://arxiv.org/html/2510.05809v1#S4.E9 "In Example 4.8 (Robust representation of non-parametric estimator of expectile value at risk). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")). Non-comonotonicity of this estimator follows from Theorem [4.10](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem10 "Theorem 4.10 (Robust representation of comonotonic and law-invariant CREs). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") and Example [4.8](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem8 "Example 4.8 (Robust representation of non-parametric estimator of expectile value at risk). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"), where the maximizer has been shown to be dependent on the sample. For completeness, let us now numerically illustrate the non-comonotonicity of ExpVaR^\widehat{\operatorname{ExpVaR}}. Let α=1/4\alpha=1/4, 𝐱:=(1,2,3)\mathbf{x}:=(1,2,3), and 𝐲:=(0,0,1)\mathbf{y}:=(0,0,1). Clearly, 𝐱\mathbf{x} and 𝐲\mathbf{y} are comonotonic. Also, routine calculations show

|  |  |  |
| --- | --- | --- |
|  | ExpVaR^1/4,3​(𝐱):=1.6,ExpVaR^1/4,3​(𝐲)≈0.1429,ExpVaR^1/4,3​(𝐱+𝐲)=1.8,\widehat{\operatorname{ExpVaR}}\_{1/4,3}(\mathbf{x}):=1.6,\quad\widehat{\operatorname{ExpVaR}}\_{1/4,3}(\mathbf{y})\approx 0.1429,\quad\widehat{\operatorname{ExpVaR}}\_{1/4,3}(\mathbf{x}+\mathbf{y})=1.8, |  |

which directly shows non-comonotonicity as ExpVaR^1/4,3​(𝐱+𝐲)≠ExpVaR^1/4,3​(𝐱)+ExpVaR^1/4,3​(𝐲)\widehat{\operatorname{ExpVaR}}\_{1/4,3}(\mathbf{x}+\mathbf{y})\neq\widehat{\operatorname{ExpVaR}}\_{1/4,3}(\mathbf{x})+\widehat{\operatorname{ExpVaR}}\_{1/4,3}(\mathbf{y}). □\square

###### Remark 4.13 (Robust representation weights for CRE and risk spectrum).

In Example [4.11](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem11 "Example 4.11 (Non-parametric plug-in CRE for spectral risk measures). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"), we illustrated the inherent relationship between the risk spectrum in the spectral representation of CRMs and the structure of estimation weights in the robust representation of CREs. Specifically, the vectors a∈ℳna\in\mathcal{M}\_{n} defined in Theorem [4.10](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem10 "Theorem 4.10 (Robust representation of comonotonic and law-invariant CREs). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") and Theorem [4.2](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem2 "Theorem 4.2 (Robust representation of law-invariant CREs). ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") can be interpreted as approximations of risk spectra: they mimic the weakly decreasing, bounded, unit-integral properties and are applied to order statistics, which approximate empirical quantiles, i.e., VaR\operatorname{\mathrm{VaR}} at different significance levels. That said, the link does not amount to a strict equivalence, since plug-in spectral estimators for CRMs rely on empirical quantile representations, whereas risk spectra may also be estimated via alternative approximation schemes; cf. Example [4.11](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem11 "Example 4.11 (Non-parametric plug-in CRE for spectral risk measures). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") and Example [5.5](https://arxiv.org/html/2510.05809v1#S5.Thmtheorem5 "Example 5.5 (Consistency of alternative plug-in CREs for spectral risk measures). ‣ 5 Consistency of CREs for i.i.d. samples ‣ Coherent estimation of risk measures").

## 5 Consistency of CREs for i.i.d. samples

In this section, we focus on the problem how to generate a sequence of CREs ρ^n​(𝐗)\hat{\rho}\_{n}(\mathbf{X}) that approximates a given CRM ρ​(X)\rho(X), where 𝐗\mathbf{X} is an i.i.d. sample from X∈𝒳X\in\mathcal{X}. We start by stating the definition of consistent risk estimators.

###### Definition 5.1 (Consistent estimator).

A sequence of risk estimators (ρ^n)n=1∞(\hat{\rho}\_{n})\_{n=1}^{\infty} is consistent for a risk measure ρ:𝒳→ℝ∪{+∞}\rho\colon\mathcal{X}\to\mathbb{R}\cup\{+\infty\} if, for any X∈𝒳X\in\mathcal{X} such that ρ​(X)<+∞\rho(X)<+\infty, and i.i.d. sample 𝐗n:=(X1,X2,…)\mathbf{X}\_{n}:=(X\_{1},X\_{2},\ldots) from the distribution of XX, we have

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(𝐗n)→a.s.ρ​(X),n→∞,\hat{\rho}\_{n}(\mathbf{X}\_{n})\xrightarrow{a.s.}\rho(X),\quad n\to\infty, |  |

where →a.s.\xrightarrow{a.s.} stands for ℙ\mathbb{P}-almost sure convergence555In this work, for simplicity, we focus on ℙ\mathbb{P}-a.s. convergence of the estimators, which corresponds to strong consistency in classical statistics. Nevertheless, most of the results can be extended to weaker forms of convergence, such as convergence in probability (i.e., weak consistency)..

As the next result shows, consistency of the risk estimators preserves coherence of the limiting risk measure.

###### Proposition 5.2 (CREs consistent limit leads to CRM).

Suppose that there exists a consistent sequence of CREs (ρ^n)n=1∞(\hat{\rho}\_{n})\_{n=1}^{\infty} for ρ:𝒳→ℝ∪{+∞}\rho\colon\mathcal{X}\to\mathbb{R}\cup\{+\infty\}. Then, ρ\rho is a law-invariant CRM.

###### Proof.

To show that ρ\rho is CRM, we only show the subadditivity condition; the remaining properties are proved similarly or are straightforward. Let (Xi,Yi)i=1n(X\_{i},Y\_{i})\_{i=1}^{n} be an i.i.d. bivariate sample from (X,Y)∈𝒳×𝒳(X,Y)\in\mathcal{X}\times\mathcal{X}. Then, (Zi)i=1n(Z\_{i})\_{i=1}^{n} with Zi=Xi+YiZ\_{i}=X\_{i}+Y\_{i} is an i.i.d. sample from X+YX+Y and using the consistency and the coherence of ρ^n\hat{\rho}\_{n}, we have

|  |  |  |
| --- | --- | --- |
|  | ρ(X+Y)=limn→∞ρ^n(𝐙n)≤limn→∞(ρ^n(𝐗n)+ρ^n(𝐘n)))=ρ(X)+ρ(Y),\rho(X+Y)=\lim\_{n\to\infty}\hat{\rho}\_{n}(\mathbf{Z}\_{n})\leq\lim\_{n\to\infty}\left(\hat{\rho}\_{n}(\mathbf{X}\_{n})+\hat{\rho}\_{n}(\mathbf{Y}\_{n}))\right)=\rho(X)+\rho(Y), |  |

where we set 𝐗n:=(X1,…,Xn)\mathbf{X}\_{n}:=(X\_{1},\ldots,X\_{n}), 𝐘n:=(Y1,…,Yn)\mathbf{Y}\_{n}:=(Y\_{1},\ldots,Y\_{n}), 𝐙n:=(Z1,…,Zn)\mathbf{Z}\_{n}:=(Z\_{1},\ldots,Z\_{n}).

To prove law-invariance, let X,Y∈𝒳X,Y\in\mathcal{X} that have the same distribution. Then, an i.i.d. sample 𝐗n=(Xi)i=1n\mathbf{X}\_{n}=(X\_{i})\_{i=1}^{n} from XX is also an i.i.d. sample from YY, and by consistency, we have

|  |  |  |
| --- | --- | --- |
|  | ρ​(X)=limn→∞ρ^n​(𝐗n)=ρ​(Y),\rho(X)=\lim\_{n\to\infty}\hat{\rho}\_{n}(\mathbf{X}\_{n})=\rho(Y), |  |

which concludes the proof.
∎

Note that in Proposition [5.2](https://arxiv.org/html/2510.05809v1#S5.Thmtheorem2 "Proposition 5.2 (CREs consistent limit leads to CRM). ‣ 5 Consistency of CREs for i.i.d. samples ‣ Coherent estimation of risk measures") we do not require ρ^n\hat{\rho}\_{n} to be law-invariant to get the law-invariance of ρ\rho. Also from Proposition [5.2](https://arxiv.org/html/2510.05809v1#S5.Thmtheorem2 "Proposition 5.2 (CREs consistent limit leads to CRM). ‣ 5 Consistency of CREs for i.i.d. samples ‣ Coherent estimation of risk measures"), we observe that if ρ\rho is not coherent, then there is no consistent sequence of CREs for ρ\rho.

Following the discussion in Section [4.1](https://arxiv.org/html/2510.05809v1#S4.SS1 "4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"), our goal is to find CREs represented as an LL-estimator that are consistent. As the next result show, there is a strong connection between consistency of LL-estimators and spectral risk measures discussed in Example [4.11](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem11 "Example 4.11 (Non-parametric plug-in CRE for spectral risk measures). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"). Recall ([4.18](https://arxiv.org/html/2510.05809v1#S4.E18 "In Example 4.11 (Non-parametric plug-in CRE for spectral risk measures). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")) for the definition of a spectral risk measure with the risk spectrum ϕ\phi.

###### Theorem 5.3 (Consistency of spectral risk measure CRE).

Let ρ\rho be a spectral risk measure with the risk spectrum ϕ\phi. Let ρ^n,n>1\hat{\rho}\_{n},\ n>1, be a risk estimator given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ^n​(𝐱)=−∑i=1nai,n​xi:n,\hat{\rho}\_{n}(\mathbf{x})=-\sum\_{i=1}^{n}a\_{i,n}x\_{i:n}, |  | (5.1) |

where an:=(a1,n,…,an,n)∈ℳna^{n}:=(a\_{1,n},\ldots,a\_{n,n})\in\mathcal{M}\_{n} with a1,n≥a2,n≥…≥an,na\_{1,n}\geq a\_{2,n}\geq\ldots\geq a\_{n,n}. Put ϕn​(t):=∑i=1nn​ai,n​𝟙{t∈(i−1n,in]}\phi\_{n}(t):=\sum\_{i=1}^{n}na\_{i,n}\mathbbm{1}\_{\{t\in(\frac{i-1}{n},\frac{i}{n}]\}}, for n>1n>1, t∈[0,1]t\in[0,1], and assume that supnsupt∈[0,1]ϕn​(t)<∞\sup\_{n}\sup\_{t\in[0,1]}\phi\_{n}(t)<\infty. Then, the following conditions are equivalent:

1. 1.

   ρ^n\hat{\rho}\_{n} is a consistent estimator of ρ\rho on 𝒳=L1\mathcal{X}=L^{1}.
2. 2.

   For any t∈(0,1)t\in(0,1), we have ∫0tϕn​(s)​𝑑s→∫0tϕ​(s)​𝑑s\int\_{0}^{t}\phi\_{n}(s)ds\to\int\_{0}^{t}\phi(s)ds, as n→∞n\to\infty.

###### Proof.

The claim follows from van Zwet [[1980](https://arxiv.org/html/2510.05809v1#bib.bib64)], Corollary 2.1 and the subsequent discussion, by setting JN=ϕNJ\_{N}=\phi\_{N}, J=ϕJ=\phi, and g=FX−1g=F\_{X}^{-1}.
∎

Alternative conditions to the uniform boundedness of the sequence (n​an)(na\_{n}) from Theorem [5.3](https://arxiv.org/html/2510.05809v1#S5.Thmtheorem3 "Theorem 5.3 (Consistency of spectral risk measure CRE). ‣ 5 Consistency of CREs for i.i.d. samples ‣ Coherent estimation of risk measures") can be found in the extensive literature on the consistency of LL-estimators; for a comprehensive review, we refer the reader to Aaronson et al. [[1996](https://arxiv.org/html/2510.05809v1#bib.bib1)], Miao and Ma [[2021](https://arxiv.org/html/2510.05809v1#bib.bib48)], [Serfling, [1980](https://arxiv.org/html/2510.05809v1#bib.bib58), Chapter 8], and Mason [[1982](https://arxiv.org/html/2510.05809v1#bib.bib45)].

Next we consider an example of risk estimator that satisfies the assumptions of Theorem [5.3](https://arxiv.org/html/2510.05809v1#S5.Thmtheorem3 "Theorem 5.3 (Consistency of spectral risk measure CRE). ‣ 5 Consistency of CREs for i.i.d. samples ‣ Coherent estimation of risk measures").

###### Example 5.4 (Consistency of plug-in CREs for spectral risk measures).

Let ρ\rho be a spectral risk measure with the risk spectrum ϕ\phi, and let ρ^na\hat{\rho}^{a}\_{n} be its CRE defined in Example [4.11](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem11 "Example 4.11 (Non-parametric plug-in CRE for spectral risk measures). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"). We claim that this estimator is consistent for ρ\rho. Indeed, for any n>1n>1 and i=1,…,ni=1,\ldots,n we have n​ai,n=n​∫i−1ninϕ​(s)​𝑑s≤n​1n​‖ϕ‖1=‖ϕ‖1na\_{i,n}=n\int\_{\frac{i-1}{n}}^{\frac{i}{n}}\phi(s)ds\leq n\frac{1}{n}\|\phi\|\_{1}=\|\phi\|\_{1}.
Thus, setting ϕn​(t):=∑i=1nn​ai,n​𝟙{t∈(i−1n,in]}\phi\_{n}(t):=\sum\_{i=1}^{n}na\_{i,n}\mathbbm{1}\_{\{t\in(\frac{i-1}{n},\frac{i}{n}]\}}, we obtain

|  |  |  |
| --- | --- | --- |
|  | supnsupt∈[0,1]ϕn​(t)=supnsupi=1,…,nn​ai,n≤‖ϕ‖1<∞.\sup\_{n}\sup\_{t\in[0,1]}\phi\_{n}(t)=\sup\_{n}\sup\_{i=1,\ldots,n}na\_{i,n}\leq\|\phi\|\_{1}<\infty. |  |

Also, for any t∈(0,1)t\in(0,1), we deduce

|  |  |  |
| --- | --- | --- |
|  | ∫0tϕn​(s)​𝑑s=n​∑i=1[t​n]ai,n​1n+n​a[t​n],n​(t−[t​n]n)=∫0[t​n]nϕ​(s)​𝑑s+(t​n−[t​n])​∫[t​n]−1n[t​n]nϕ​(s)​𝑑s→∫0tϕ​(s)​𝑑s,n→∞.\int\_{0}^{t}\phi\_{n}(s)ds=n\sum\_{i=1}^{[tn]}a\_{i,n}\frac{1}{n}+na\_{[tn],n}\left(t-\frac{[tn]}{n}\right)=\int\_{0}^{\frac{[tn]}{n}}\phi(s)ds+(tn-[tn])\int\_{\frac{[tn]-1}{n}}^{\frac{[tn]}{n}}\phi(s)ds\to\int\_{0}^{t}\phi(s)ds,\quad n\to\infty. |  |

Then, by Theorem [5.3](https://arxiv.org/html/2510.05809v1#S5.Thmtheorem3 "Theorem 5.3 (Consistency of spectral risk measure CRE). ‣ 5 Consistency of CREs for i.i.d. samples ‣ Coherent estimation of risk measures"), consistency of ρ^na\hat{\rho}\_{n}^{a} follows. □\square

###### Example 5.5 (Consistency of alternative plug-in CREs for spectral risk measures).

The risk spectrum ϕ\phi could be approximated using different weighting schemes.
Let us consider the setup introduced in Example [4.11](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem11 "Example 4.11 (Non-parametric plug-in CRE for spectral risk measures). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures") but with alternative weights defined by as ai,n:=ϕ​(i/n)∑k=1nϕ​(k/n)a\_{i,n}:=\frac{\phi(i/n)}{\sum\_{k=1}^{n}\phi(k/n)}, n>1n>1, i=1,…,ni=1,\ldots,n, we refer to [Acerbi, [2002](https://arxiv.org/html/2510.05809v1#bib.bib2), Section 5] where this approximation scheme is introduced and discussed. Using a similar argument as in Example [5.4](https://arxiv.org/html/2510.05809v1#S5.Thmtheorem4 "Example 5.4 (Consistency of plug-in CREs for spectral risk measures). ‣ 5 Consistency of CREs for i.i.d. samples ‣ Coherent estimation of risk measures") one can show that the corresponding risk estimator is also consistent; see also Theorem 5.4 in Acerbi [[2002](https://arxiv.org/html/2510.05809v1#bib.bib2)]. □\square

The consistency of estimators for general risk measures has been well studied in the literature. Broadly speaking, using the language of this manuscript, these results fall into two (overlapping) categories: non-parametric plug-in estimator (e.g. Example [3.5](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem5 "Example 3.5 (Average tail loss ES estimator is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures")) and empirical distribution plug-in estimators (e.g. Proposition [3.3](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem3 "Proposition 3.3 (Empirical plug-in risk estimator for CRM is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures")). We emphasize that in all these works, the focus has been on statistical asymptotic properties (such as consistency and rates of convergence) and on certain selected economic or financial properties (such as robustness and elicitability). In contrast, the present work concentrates on comprehensive risk management properties of these estimators.

For the sake of completeness, we review some of the existing key results. We recall that a law-invariant CRM ρ\rho, under some mild conditions, e.g. from Kusuoka [[2001](https://arxiv.org/html/2510.05809v1#bib.bib44)], admits the representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(X)=supμ∈ℳWVaRμ⁡(X)=supμ∈ℳ∫(0,1]ESα⁡(X)​μ​(d⁡α),\rho(X)=\sup\_{\mu\in\mathcal{M}}\operatorname{\mathrm{WVaR}}\_{\mu}(X)=\sup\_{\mu\in\mathcal{M}}\int\_{(0,1]}\operatorname{\mathrm{ES}}\_{\alpha}(X)\mu(\operatorname{d}\!\alpha), |  | (5.2) |

for some set ℳ⊂ℳf\mathcal{M}\subset\mathcal{M}^{f}. Similar to Example [4.11](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem11 "Example 4.11 (Non-parametric plug-in CRE for spectral risk measures). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"), using a natural discrete approximation of the integrals as well as replacing ESα,α∈(0,1]\operatorname{\mathrm{ES}}\_{\alpha},\alpha\in(0,1], by a given family of estimators ES^α,α∈(0,1]\widehat{\operatorname{\mathrm{ES}}}\_{\alpha},\alpha\in(0,1], we can consider the estimator

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ^n​(𝐱):=supμ∈ℳ∑i=1nES^αi​(𝐱)​μ​((αi,αi+1]),\hat{\rho}\_{n}(\mathbf{x}):=\sup\_{\mu\in\mathcal{M}}\sum\_{i=1}^{n}\widehat{\operatorname{\mathrm{ES}}}\_{\alpha\_{i}}(\mathbf{x})\mu((\alpha\_{i},\alpha\_{i+1}]), |  | (5.3) |

where (αi)(\alpha\_{i}) forms a uniform partition of [0,1][0,1]. Equivalently, after some direct algebraic transformations, it can be written as

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(𝐱)=supa∈M∗⟨a,−s​(𝐱)⟩,\hat{\rho}\_{n}(\mathbf{x})=\sup\_{a\in M^{\*}}\langle a,-s(\mathbf{x})\rangle, |  |

for some explicitly computed class of weights M∗M^{\*}, i.e. supremum over a class of LL-estimators. We note that while there is a vast literature on asymptotic properties of LL-estimators, those methods rarely can be extended directly to the supremum of a set of LL-estimators. In [Pflug and Wozabal, [2010](https://arxiv.org/html/2510.05809v1#bib.bib51), Theorem 3.15], the authors prove, under some fairly general assumptions, that ρ^n\hat{\rho}\_{n} given by ([5.3](https://arxiv.org/html/2510.05809v1#S5.E3 "In 5 Consistency of CREs for i.i.d. samples ‣ Coherent estimation of risk measures")) is consistent, and asymptotically normal with rate of convergence n1/2n^{1/2}; see also Wozabal [[2009](https://arxiv.org/html/2510.05809v1#bib.bib63)]. In Cont et al. [[2010](https://arxiv.org/html/2510.05809v1#bib.bib25)] the authors study the robustness and sensitivity of similar CREs.

For an arbitrary law-invariant CRM ρ\rho, in view of Proposition [3.3](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem3 "Proposition 3.3 (Empirical plug-in risk estimator for CRM is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures"), one can build a law-invariant CRE, what we call the empirical distribution plug-in estimator. In Belomestny and Krätschmer [[2012](https://arxiv.org/html/2510.05809v1#bib.bib16)] the authors show that these estimators are consistent and satisfy a central limit theorem with usual rate n1/2n^{1/2}; the manuscript also considers the non-i.i.d. data. We refer to Weber [[2007](https://arxiv.org/html/2510.05809v1#bib.bib62)], Chen [[2008](https://arxiv.org/html/2510.05809v1#bib.bib23)], Beutner and Zähle [[2010](https://arxiv.org/html/2510.05809v1#bib.bib17)], for some earlier works on this topic. Finally, we mention Bartl and Tangpi [[2023](https://arxiv.org/html/2510.05809v1#bib.bib10)] that investigates the same class of empirical distribution plug-in estimators but for a larger class of law-invariant risk measures, where the authors show that generally speaking, the rate of convergence is not necessarily classical n1/2n^{1/2}. We also refer to Bartl and Tangpi [[2023](https://arxiv.org/html/2510.05809v1#bib.bib10)] for a comprehensive and relatively up to date literature review on this topic.

## 6 Numerical study: comparison of ES estimators based on L-statistics

The ES is widely recognized as the most prominent coherent risk measure, and its estimation has become an important topic in the risk measurement literature, see McNeil et al. [[2010](https://arxiv.org/html/2510.05809v1#bib.bib47)]. As mentioned in the introduction, the relevance of this subject was reinforced by the FRTB reforms, under which the estimation of ES at the 2.5% level was established as a regulatory standard, see BCBS [[2019](https://arxiv.org/html/2510.05809v1#bib.bib13)]. Consequently, the development of accurate and robust methods for estimating ES has become essential in both academic research and practical risk management.

In this section, we provide a short comparison study of selected ES estimators with focus on their robust representations and provide a short comparative performance analysis for six different non-parametric ES estimators. Throughout this section, we consider confidence level 2.5% and sample size n=250n=250, which is similar to the standard regulatory setup.

### Non-parametric ES estimators

A wide range of ES estimation methodologies have been proposed in the literature, ranging from historical simulation and parametric approaches to more advanced techniques based on extreme value theory and stochastic modeling. We refer to the survey paper Nadarajah et al. [[2014](https://arxiv.org/html/2510.05809v1#bib.bib50)], where more than 45 estimation methods for ES are presented. While most of these approaches are parametric and yield estimators that are not CREs (cf. Example [3.4](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem4 "Example 3.4 (Gaussian parameteric plug-in ES estimator is not coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures")), the authors still identify 11 non-parametric methodologies. Moreover, given any quantile (VaR) estimation method and the reference confidence threshold α∈(0,1)\alpha\in(0,1), one can construct an integral-related pair of (ESα,VaRα)(\textrm{ES}\_{\alpha},\operatorname{\mathrm{VaR}}\_{\alpha}) estimators by plugging the VaR estimators into the formula ([2.3](https://arxiv.org/html/2510.05809v1#S2.E3 "In 2 Preliminaries ‣ Coherent estimation of risk measures")) and integrating. Consequently, any quantile estimation methodology, including those presented in Hyndman and Fan [[1996](https://arxiv.org/html/2510.05809v1#bib.bib42)], may serve as a basis for ES estimation.

For regulatory FRTB model purposes, suitable estimation methodologies should employ distribution-free estimators for which the ES and VaR relationship is straightforward to establish, cf. [ECB, [2025](https://arxiv.org/html/2510.05809v1#bib.bib31), p. 267] or [EU, [2024a](https://arxiv.org/html/2510.05809v1#bib.bib33), Article 42]; this links VaR\operatorname{\mathrm{VaR}} backtesting results to ES estimates for regulatory capital. This naturally motivates the use of estimators based on LL-statistics. Indeed, in the study of ES estimator properties reported in [EBA, [2023](https://arxiv.org/html/2510.05809v1#bib.bib29), Annex I], all VaR and ES estimation methods were based on LL-estimators.

Here we study a representative set of ES estimation methodologies based on LL-estimators, with a particular focus on the choice of CRE robust representation weighting schemes. Namely, for simplicity, we take ES estimators considered in [EBA, [2023](https://arxiv.org/html/2510.05809v1#bib.bib29), Annex I], presented in summary Table [1](https://arxiv.org/html/2510.05809v1#S6.T1 "Table 1 ‣ Non-parametric ES estimators ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures"), and labeled with IDs #1-#6.
Our aim is to investigate how differences in order statistics weights impact estimation accuracy along some other properties.

|  |  |  |  |
| --- | --- | --- | --- |
| Id | Estimator | CRE | Comment |
| #1 | ES^α,n1​(𝐱):=−1⌊α​n⌋​∑i=1⌊α​n⌋xi:n\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,n}(\mathbf{x}):=\frac{-1}{\lfloor\alpha n\rfloor}\sum\_{i=1}^{\lfloor\alpha n\rfloor}x\_{i:n} | Yes | Average tail loss ES estimator based on ([2.4](https://arxiv.org/html/2510.05809v1#S2.E4 "In 2 Preliminaries ‣ Coherent estimation of risk measures")) and sample conditional mean. For details, see Example [3.5](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem5 "Example 3.5 (Average tail loss ES estimator is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures"). |
| #2 | ES^α,n2​(𝐱):=−1α​n​(∑i=1⌊α​n⌋xi:n+(α​n−⌊α​n⌋)​x(⌊α​n⌋+1):n)\widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}^{2}(\mathbf{x}):=\frac{-1}{\alpha n}\left(\sum\_{i=1}^{\lfloor\alpha n\rfloor}x\_{i:n}+(\alpha n-\lfloor\alpha n\rfloor)x\_{(\lfloor\alpha n\rfloor+1):n}\right) | Yes | Non-parametric ES plug-in estimator for the empirical sample quantile. For details, see Example [3.7](https://arxiv.org/html/2510.05809v1#S3.Thmtheorem7 "Example 3.7 (Non-parametric plug-in ES estimator is coherent). ‣ 3 Coherent risk estimators ‣ Coherent estimation of risk measures"). |
| #3 | ES^α,n3​(𝐱):=−1α​(n+1)(32x1:n+∑i=2M6−1xi:n+1+2​R6−R622xM6:n+R622x(M6+1):n)\begin{aligned} \widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}^{3}(\mathbf{x})&\textstyle:=\frac{-1}{\alpha(n+1)}\Big(\frac{3}{2}x\_{1:n}+\sum\_{i=2}^{M\_{6}-1}x\_{i:n}+\frac{1+2R\_{6}-R\_{6}^{2}}{2}x\_{M\_{6}:n}\\ &\textstyle\phantom{:=\,\,}+\frac{R\_{6}^{2}}{2}x\_{(M\_{6}+1):n}\Big)\end{aligned} | Yes | ES plug-in integral estimator for Type 6 sample quantile, based on ([2.3](https://arxiv.org/html/2510.05809v1#S2.E3 "In 2 Preliminaries ‣ Coherent estimation of risk measures")) and flat extrapolation. For details, see [EBA, [2023](https://arxiv.org/html/2510.05809v1#bib.bib29), Annex I] and Hyndman and Fan [[1996](https://arxiv.org/html/2510.05809v1#bib.bib42)]. |
| #4 | ES^α,n4​(𝐱):=−1α​(n+1)((12+11−ξ)x1:n+∑i=2M6−1xi:n+1+2​R6−R622xM6:n+R622x(M6+1):n)\begin{aligned} \widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}^{4}(\mathbf{x})&\textstyle:=\frac{-1}{\alpha(n+1)}\Big(\left(\frac{1}{2}+\frac{1}{1-\xi}\right)x\_{1:n}+\sum\_{i=2}^{M\_{6}-1}x\_{i:n}\\ &\textstyle\phantom{:=\,\,}+\frac{1+2R\_{6}-R\_{6}^{2}}{2}x\_{M\_{6}:n}+\frac{R\_{6}^{2}}{2}x\_{(M\_{6}+1):n}\Big)\end{aligned} | No | ES plug-in integral estimator for Type 6 sample quantile, based on ([2.3](https://arxiv.org/html/2510.05809v1#S2.E3 "In 2 Preliminaries ‣ Coherent estimation of risk measures")) and Pareto-type extrapolation. For details, see [EBA, [2023](https://arxiv.org/html/2510.05809v1#bib.bib29), Annex I] and McNeil [[1999](https://arxiv.org/html/2510.05809v1#bib.bib46)]. |
| #5 | ES^α,n5​(𝐱):=−1M6​(32​x1:n+∑i=2M6xi:n)\widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}^{5}(\mathbf{x}):=\frac{-1}{M\_{6}}\left(\frac{3}{2}x\_{1:n}+\sum\_{i=2}^{M\_{6}}x\_{i:n}\right) | No | Conservative version of ES estimator #3 in which the integral in ([2.3](https://arxiv.org/html/2510.05809v1#S2.E3 "In 2 Preliminaries ‣ Coherent estimation of risk measures")) is restricted to [0,M6][0,M\_{6}]. For details, see [EBA, [2023](https://arxiv.org/html/2510.05809v1#bib.bib29), Annex I]. |
| #6 | ES^α,n6​(𝐱):=−1M6​((12+11−ξ)​x1:n+∑i=2M6xi:n)\widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}^{6}(\mathbf{x}):=\frac{-1}{M\_{6}}\left(\left(\frac{1}{2}+\frac{1}{1-\xi}\right)x\_{1:n}+\sum\_{i=2}^{M\_{6}}x\_{i:n}\right) | No | Conservative version of ES estimator #4 in which the integral in ([2.3](https://arxiv.org/html/2510.05809v1#S2.E3 "In 2 Preliminaries ‣ Coherent estimation of risk measures")) is restricted to [0,M6][0,M\_{6}]. For details, see [EBA, [2023](https://arxiv.org/html/2510.05809v1#bib.bib29), Annex I]. |

Table 1: The table presents six different non-parametric ES estimators that are considered in the comparative analysis; the estimators are taken from [EBA, [2023](https://arxiv.org/html/2510.05809v1#bib.bib29), Annex I]. For brevity, in the table we use notation M6:=⌊α​(n+1)⌋M\_{6}:=\lfloor\alpha(n+1)\rfloor, R6:=α​(n+1)−⌊α​(n+1)⌋R\_{6}:=\alpha(n+1)-\lfloor\alpha(n+1)\rfloor, and consider estimators #3 and #6 with a fixed parameter value ξ:=1/3\xi:=1/3.

First, we note that among the six LL-estimators under consideration, only three satisfy the CRE properties. Those that are not CRE have weights assigned to order statistics that do not sum to one, thereby violating the cash-additivity condition (E2); note that for 𝐱∈ℝn\mathbf{x}\in\mathbb{R}^{n}, m∈ℝm\in\mathbb{R} and k∈{1,…,6}k\in\{1,\ldots,6\} we have ES^α,nk​(𝐱+m)=ES^α,nk​(𝐱)−sk​m\widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}^{k}(\mathbf{x}+m)=\widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}^{k}(\mathbf{x})-s\_{k}m, where sks\_{k} denotes the sum of weights for the kkth ES estimator. For convenience, the exact weighting schemes and the corresponding sum of weights are reported in Table [2](https://arxiv.org/html/2510.05809v1#S6.T2 "Table 2 ‣ Non-parametric ES estimators ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures").

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Estimator (Id) | a1a\_{1} | a2a\_{2} | a3a\_{3} | a4a\_{4} | a5a\_{5} | a6a\_{6} | a7a\_{7} | sum |
| #1 | 0.167 | 0.167 | 0.167 | 0.167 | 0.167 | 0.167 | 0.000 | 1.000 |
| #2 | 0.160 | 0.160 | 0.160 | 0.160 | 0.160 | 0.160 | 0.040 | 1.000 |
| #3 | 0.239 | 0.159 | 0.159 | 0.159 | 0.159 | 0.117 | 0.006 | 1.000 |
| #4 | 0.319 | 0.159 | 0.159 | 0.159 | 0.159 | 0.117 | 0.006 | 1.080 |
| #5 | 0.250 | 0.167 | 0.167 | 0.167 | 0.167 | 0.167 | 0.000 | 1.083 |
| #6 | 0.333 | 0.167 | 0.167 | 0.167 | 0.167 | 0.167 | 0.000 | 1.167 |

Table 2: The table presents weights assigned to the first seven order statistics for estimator #1-#6 from Table [1](https://arxiv.org/html/2510.05809v1#S6.T1 "Table 1 ‣ Non-parametric ES estimators ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures"). The weights are calculated for α=2.5%\alpha=2.5\% and n=250n=250; the remaining weights are equal to 0. The weights for all estimators are decreasing, which is consistent with CRE representation ([4.14](https://arxiv.org/html/2510.05809v1#S4.E14 "In Theorem 4.10 (Robust representation of comonotonic and law-invariant CREs). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures")). The results are rounded to 3 decimal digits.

The violation of the CRE property in estimators #4, #5, and #6 stems from assigning larger weights to the first order statistic (x1:nx\_{1:n}) to account for unobserved tail risks. As discussed in [EBA, [2023](https://arxiv.org/html/2510.05809v1#bib.bib29), Annex I], these weights are motivated by a Pareto tail extrapolation rationale: picking larger values of the Pareto distribution shape parameter ξ\xi imply increasingly heavy tails, see McNeil [[1999](https://arxiv.org/html/2510.05809v1#bib.bib46)]. Still, we remark that the CRE property of such estimators could be preserved by normalizing the weights or transporting mass (encoded in vector aa) toward the first order statistic. In particular, this could be achieved by considering different empirical quantile interpolation and extrapolation schemes that would preserve the link between VaR\operatorname{\mathrm{VaR}} and ES\operatorname{\mathrm{ES}} estimators. On the other hand, we observe that the weights (a1,…,a7)(a\_{1},\ldots,a\_{7}) decrease in all cases, which is consistent with the assumptions of Theorem [4.10](https://arxiv.org/html/2510.05809v1#S4.Thmtheorem10 "Theorem 4.10 (Robust representation of comonotonic and law-invariant CREs). ‣ 4.1 Comonotonic CREs and their representation as L-estimators ‣ 4 Robust representations of a CRE ‣ Coherent estimation of risk measures"). We also note that the weight vectors can be viewed as alternative approximations of risk spectra, cf. Example [5.4](https://arxiv.org/html/2510.05809v1#S5.Thmtheorem4 "Example 5.4 (Consistency of plug-in CREs for spectral risk measures). ‣ 5 Consistency of CREs for i.i.d. samples ‣ Coherent estimation of risk measures").

Second, by examining the weights assigned to specific order statistics, we observe considerable differences in order statistic weight allocation across estimators, particularly for the boundary weights (a1a\_{1} and a6a\_{6} or a7a\_{7}). While these differences may not introduce significant bias for moderately-tailed distributions, they could lead to biased risk estimates in the presence of heavy tails or when an external shock resulting in extreme observations is incorporated into an otherwise i.i.d. sample. To investigate this in greater detail, and to assess the statistical performance of the proposed estimators on both i.i.d. and non-i.i.d. data, we first introduce a set of benchmark statistical metrics and subsequently conduct a numerical study in the spirit of the analysis presented in [EBA, [2023](https://arxiv.org/html/2510.05809v1#bib.bib29), Annex I].

### Evaluation of ES estimators

In order to compare the ES estimators #1-#6, we introduce five benchmark metrics summarized in Table [3](https://arxiv.org/html/2510.05809v1#S6.T3 "Table 3 ‣ Evaluation of ES estimators ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures").

|  |  |  |
| --- | --- | --- |
| Metric | Theoretical formula | Implementation |
| Mean Absolute Error | 𝔼|ES^α,n(𝐗)]−ESα(X)|ESα⁡(X)\frac{\mathbb{E}\left|\widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}(\mathbf{X})]-\operatorname{\mathrm{ES}}\_{\alpha}(X)\right|}{\operatorname{\mathrm{ES}}\_{\alpha}(X)} | A​E:=1K∑k=1K|ES^α,n(𝐱k)]−ESα(X)|ESα⁡(X)AE:=\frac{\tfrac{1}{K}\sum\_{k=1}^{K}\left|\widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}(\mathbf{x}\_{k})]-\operatorname{\mathrm{ES}}\_{\alpha}(X)\right|}{\operatorname{\mathrm{ES}}\_{\alpha}(X)} |
| Root Mean Squared Error | 𝔼[(ES^α,n(𝐗)]−ESα(X))2]ESα⁡(X)\frac{\sqrt{\mathbb{E}[\left(\widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}(\mathbf{X})]-\operatorname{\mathrm{ES}}\_{\alpha}(X)\right)^{2}]}}{\operatorname{\mathrm{ES}}\_{\alpha}(X)} | S​E:=1K∑k=1K[(ES^α,n(𝐱k)]−ESα(X))2]ESα⁡(X)SE:=\frac{\sqrt{\tfrac{1}{K}\sum\_{k=1}^{K}[\left(\widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}(\mathbf{x}\_{k})]-\operatorname{\mathrm{ES}}\_{\alpha}(X)\right)^{2}]}}{\operatorname{\mathrm{ES}}\_{\alpha}(X)} |
| Statistical Bias | 𝔼​[ES^α,n​(𝐗)]−ESα⁡(X)ESα⁡(X)\frac{\mathbb{E}[\widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}(\mathbf{X})]-\operatorname{\mathrm{ES}}\_{\alpha}(X)}{\operatorname{\mathrm{ES}}\_{\alpha}(X)} | S​B:=1K​∑k=1KES^α,n​(𝐱k)ESα⁡(X)−1SB:=\tfrac{1}{K}\sum\_{k=1}^{K}\frac{\widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}(\mathbf{x}\_{k})}{\operatorname{\mathrm{ES}}\_{\alpha}(X)}-1 |
| Risk Bias | −ESα⁡(X+ES^α,n​(𝐗))ESα⁡(X)-\frac{\operatorname{\mathrm{ES}}\_{\alpha}(X+\widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}(\mathbf{X}))}{\operatorname{\mathrm{ES}}\_{\alpha}(X)} | R​B:=−ES^α,K1​((x~k+ES^α,n​(𝐱k))k=1K)ESα⁡(X)RB:=-\frac{\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\alpha,K}\left((\tilde{x}\_{k}+\widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}(\mathbf{x}\_{k}))\_{k=1}^{K}\right)}{\operatorname{\mathrm{ES}}\_{\alpha}(X)} |
| Safe Confidence Threshold | infβ∈(0,1){ESβ⁡(X+ES^α,n​(𝐗))≥0}\inf\_{\beta\in(0,1)}\{\operatorname{\mathrm{ES}}\_{\beta}(X+\widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}(\mathbf{X}))\geq 0\} | C​T:=infβ∈(0,1){ES^β,K1​((x~k+ES^α,n​(𝐱k))k=1K)≥0}CT:=\inf\_{\beta\in(0,1)}\left\{\widehat{\operatorname{\mathrm{ES}}}^{1}\_{\beta,K}\left((\tilde{x}\_{k}+\widehat{\operatorname{\mathrm{ES}}}\_{\alpha,n}(\mathbf{x}\_{k}))\_{k=1}^{K}\right)\geq 0\right\} |

Table 3: The table presents benchmarking metrics that are used in comparative analysis for the estimators presented in Table [1](https://arxiv.org/html/2510.05809v1#S6.T1 "Table 1 ‣ Non-parametric ES estimators ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures"). The first four statistics are expressed in relative terms (in relation to true risk) and are reported in %. For a given test distribution, the metric outputs are calculated using Monte Carlo simulations of size K=107K=10^{7}.

For completeness, we include a brief comment on the chosen benchmarking metrics:

* 1.

  AE and SE: Mean Absolute Error and Root Mean Squared Error are standard distance metrics that are used to measure the dispersion between the true value and its estimate; they are often used in regression and predictive statistics. We categorize them as Fit metrics, as they characterize how close to the true value we are; see e.g. Hyndman and Athanasopoulos [[2018](https://arxiv.org/html/2510.05809v1#bib.bib41)] for more background on these metrics. In both cases, the closer we are to zero, the better.
* 2.

  SB: Statistical Bias is checking if the estimated value is on average equal to the true value and it is the standard estimator property. While it is hard to evaluate in the statistical setup in which a true distribution is unknown, for any predefined distribution the statistical bias for LL-estimators could be directly computed using order statistics expected values since
  𝔼​[⟨a,s​(x)⟩]=∑i=1nai​mi:n\mathbb{E}[\langle a,s(x)\rangle]=\sum\_{i=1}^{n}a\_{i}m\_{i:n}, where mi:n:=𝔼​[Xi:n]m\_{i:n}:=\mathbb{E}[X\_{i:n}]. Thus, for a specific distribution choice, the statistical unbiasedness condition effectively imposes a linear constraint on the choice of the coefficients (ai)(a\_{i}). Also, it is worth mentioning that the expected values of the order statistics for i.i.d. samples can be computed offline using some standard numerical routines, see e.g. [Arnold et al., [2008](https://arxiv.org/html/2510.05809v1#bib.bib6), Section 2.2]. The closer we are to zero, the better.
* 3.

  RB: Risk Bias metric checks if the position secured with a cash amount of estimated risk is safe in terms of the underlying risk. The notion of risk unbiasedness in the risk-management sense was first introduced by Pitera and Schmidt [[2018](https://arxiv.org/html/2510.05809v1#bib.bib52)] and is also called risk fairness in Bielecki et al. [[2020](https://arxiv.org/html/2510.05809v1#bib.bib20)]. In a financial context, the quantity X+ρ^n​(𝐗)X+\hat{\rho}\_{n}(\mathbf{X}) corresponds to the secured position, i.e. a random profit and loss XX is increased by the cash value of the capital reserve ρ^n​(𝐗)\hat{\rho}\_{n}(\mathbf{X}). If the estimated risk is equal to the true risk ρ​(X)\rho(X), then by the cash additivity property (R2), we get ρ​(X+ρ​(X))=ρ​(X)−ρ​(X)=0\rho(X+\rho(X))=\rho(X)-\rho(X)=0, i.e. the core risk management requirement that a secured position should bear no risk is met. However, due to the model and estimation error, we typically have ρ​(X+ρ^n​(𝐗))≥0\rho(X+\hat{\rho}\_{n}(\mathbf{X}))\geq 0. This indicates that some residual risk remains in the supposedly secured position; we refer to Pitera and Schmidt [[2018](https://arxiv.org/html/2510.05809v1#bib.bib52)] for further discussion. We emphasize that if ρ^n\hat{\rho}\_{n} is consistent, then risk unbiasedness is satisfied in the limit, and one can argue that for sufficiently large nn it is close to zero. However, from a practical point of view, the sample size is typically fixed, in many cases dictated by the regulatory frameworks; recall that P&L distributions are unknown and not constant, hence empirical sample limits are hard to reach. The closer to zero we are, the better.
* 4.

  CT: Safe Confidence Threshold identifies the actual (minimal) value of ES confidence threshold for which the secured position is safe. It can be viewed as an acceptability index (or performance measure) dual to the ES family of risk measures, that verifies whether the estimated capital reserve secures the portfolio at a confidence level close to the reference value α∈(0,1)\alpha\in(0,1). We refer to Moldenhauer and Pitera [[2019](https://arxiv.org/html/2510.05809v1#bib.bib49)], where this metric is discussed in details, and used to construct a targeted ES backtest. The closer we are to the reference threshold α\alpha, the better.

Taking into account the nature of the considered metrics, we categorise the first two metrics (AE and SE) as Fit metrics, the next two (SB and RB) as Bias metrics, and the last one (CT) as Confidence metric. It should be noted that while our assessment is focused on estimators’ statistical properties, ES estimators are effectively point-forecast metrics focused on tail risk quantification. Thus, due to the risk-oriented nature of the ES estimators, the output of the AE and SE fit metrics should be handled with care. Those metrics may not be optimal for comparative accuracy assessment (and selection algorithms), since they are not elicitable for ES; see Gneiting [[2011](https://arxiv.org/html/2510.05809v1#bib.bib37)]. In particular, ES itself is not an elicitable risk measure, which makes comparative estimator analysis based on backtesting or scoring challenging. It is known that the joint metric (VaR,ES)(\operatorname{\mathrm{VaR}},\operatorname{\mathrm{ES}}) is elicitable, see Fissler and Ziegel [[2016](https://arxiv.org/html/2510.05809v1#bib.bib35)], but the associated scoring functions are difficult to compute and interpret. Moreover, the resulting comparisons are often statistically insignificant, may depend on the specific choice of scoring function, and require joint consideration of both ES and VaR estimation methodologies.
Due to these challenges, we have decided to present, in addition to AR and SE, another set of metrics related to bias, as well as confidence measurement. We recall that the purpose of this paper is to provide a comparison of ES estimators based on LL-statistics in the context of their CRE representation and the chosen scheme. A comprehensive assessment and comparative performance analysis is beyond the scope of this paper. For in-depth quantitative studies based on both simulated and market data, we refer to Righi and Ceretta [[2015](https://arxiv.org/html/2510.05809v1#bib.bib54)] and Chen [[2008](https://arxiv.org/html/2510.05809v1#bib.bib23)].

In addition, we remark that in practice the ES estimators #1-#6 are often applied to samples based on overlapping observations (e.g. 10-day overlapping P&Ls), for which the i.i.d. property is violated, such as in FRTB models, cf. [BCBS, [2019](https://arxiv.org/html/2510.05809v1#bib.bib13), MAR 33.4] and [ECB, [2025](https://arxiv.org/html/2510.05809v1#bib.bib31), p. 266]. While the inclusion of overlapping scenarios in the estimation increases the sample size, it typically does not substantially reduce the standard errors of the ES estimators when confronted with the ES estimators based on non-overlapping number of observations contained in the considered sample. This creates additional, non-negligible estimation risk. While a full investigation of overlapping data effects is left for future work, we illustrate their potential impact on ES estimation performance with both i.i.d. and non-i.i.d. samples. For further discussion on the implications of overlapping data in risk estimation, see Sun et al. [[2009](https://arxiv.org/html/2510.05809v1#bib.bib59)], Aichele et al. [[2021](https://arxiv.org/html/2510.05809v1#bib.bib4)], Ruiz and Nieto [[2023](https://arxiv.org/html/2510.05809v1#bib.bib56)].

In the next numerical example, we calculate the benchmark metrics for selected families of distributions using Monte Carlo simulations. For comparability, we consider the same family of distributions as in [EBA, [2023](https://arxiv.org/html/2510.05809v1#bib.bib29), Annex I]. This constitutes eight different distributions: standard normal distribution, Student’s tt-distribution with ν=5\nu=5 degrees of freedom, and six different normal inverse gamma (NIG) distributions with parameters (α,β)∈{(0.4,0.14),(0.4,−0.14),(0.55,0.3025),(0.55,−0.3025),(0.4,0.22),(0.4,−0.22)}(\alpha,\beta)\in\{(0.4,0.14),(0.4,-0.14),(0.55,0.3025),(0.55,-0.3025),(0.4,0.22),(0.4,-0.22)\}; the location parameter μ=0\mu=0 and the scale parameter δ=1\delta=1 are standardized. Skewness and kurtosis of the NIG distributions are known analytically and as NIG distributions are closed under convolution also for their rolling sums, [Scott et al., [2011](https://arxiv.org/html/2510.05809v1#bib.bib57), Section 6.1]. For the considered values of (α,β)(\alpha,\beta) parameters, the skewness and excess kurtosis values are (0.9460,3.6282)(0.9460,3.6282), (−0.9460,3.6282)(-0.9460,3.6282), (1.3601,4.5051)(1.3601,4.5051), (−1.3601,4.5051)(-1.3601,4.5051), (1.8702,8.5174)(1.8702,8.5174), and (−1.8702,8.5174)(-1.8702,8.5174). The choice of α\alpha and β\beta aims to consider various signs and magnitudes of the skewness and the kurtosis comparable to trading book P&Ls from 2014 to 2022, see [EBA, [2023](https://arxiv.org/html/2510.05809v1#bib.bib29), Annex I, p. 162] for more details and e.g. Thiele [[2020](https://arxiv.org/html/2510.05809v1#bib.bib60)] for further discussion on the asymmetry in financial data.

### Numerical study

We focus on the ES2.5%\operatorname{\mathrm{ES}}\_{2.5\%} estimation, fix n=250n=250, construct random samples from the pre-defined distributions, and follow the testing framework similar to the one introduced in [EBA, [2023](https://arxiv.org/html/2510.05809v1#bib.bib29), Annex I]. Recall that the weights in the robust representation of the ES estimators #1-#6, for n=250n=250, are provided in Table [2](https://arxiv.org/html/2510.05809v1#S6.T2 "Table 2 ‣ Non-parametric ES estimators ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures"). For every considered distribution, we compute all provided performance metrics; the values of the risk measures for the NIG distribution, as well as the expectations of the risk estimators and the risk biases, are evaluated using Monte Carlo simulations with a sample size K=107K=10^{7}. For completeness, in addition to the results for ES2.5%\operatorname{\mathrm{ES}}\_{2.5\%} estimators #1-#6, we also provide benchmark metrics output for the VaR1%\operatorname{\mathrm{VaR}}\_{1\%} estimator based on the linearly interpolated (Type 6 in the notation of Hyndman and Fan [[1996](https://arxiv.org/html/2510.05809v1#bib.bib42)]) sample quantile given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaR^1%​(𝐱):=0.49​x(2:250)+0.51​x(3:250),\widehat{\operatorname{\mathrm{VaR}}}\_{1\%}(\mathbf{x}):=0.49x\_{(2:250)}+0.51x\_{(3:250)}, |  | (6.1) |

for n=250n=250, cf. [ECB, [2025](https://arxiv.org/html/2510.05809v1#bib.bib31), Page 267]. Note that VaR1%\operatorname{\mathrm{VaR}}\_{1\%} is a reference market risk metric in the Basel II framework and for the normaly distribution random variable XX we get VaR1%⁡(X)=2.326\operatorname{\mathrm{VaR}}\_{1\%}(X)=2.326 and ES2.5%⁡(X)=2.336\operatorname{\mathrm{ES}}\_{2.5\%}(X)=2.336, cf. ([2.6](https://arxiv.org/html/2510.05809v1#S2.E6 "In 2 Preliminaries ‣ Coherent estimation of risk measures")), so that this metric could be used for VaR and ES comparison purposes; see also Kellner and Rösch [[2016](https://arxiv.org/html/2510.05809v1#bib.bib43)].

As already mentioned, we considered two frameworks to generate a sample (Xi)i=1250(X\_{i})\_{i=1}^{250}: (i) standard i.i.d. setup; (ii) overlapping setup, in which initial observations are converted into cumulative overlapping sums of size 10, that is, we consider Xi:=∑j=09Zi−jX\_{i}:=\sum\_{j=0}^{9}Z\_{i-j}, where (Zi)i=−8250(Z\_{i})\_{i=-8}^{250} is the initial i.i.d. sample. This is done to have a theoretical representation of the standard two approaches used for P&L construction in risk management, in which we consider either a series of 1-day non-overlapping P&Ls or a series of 10-day overlapping P&Ls. The results for i.i.d. P&Ls are presented in Table [4](https://arxiv.org/html/2510.05809v1#S6.T4 "Table 4 ‣ Numerical study ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures"), while the results for overlapping P&Ls are presented in Table [5](https://arxiv.org/html/2510.05809v1#S6.T5 "Table 5 ‣ Numerical study ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures").

The numerical study highlights substantial differences between estimator performance across the non-overlapping and overlapping settings. In the non-overlapping framework (Table [4](https://arxiv.org/html/2510.05809v1#S6.T4 "Table 4 ‣ Numerical study ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures")), estimators #–#3 generally provide the most accurate results, while estimators #4–#6 are clearly conservative, which is consistent with their Pareto tail based construction based on conservative simplifications. Among the former group, estimator #2 performs best with respect to fit metrics, whereas estimator #3 often delivers superior bias control and confidence coverage under heavy-tailed distributions. Overall, the ES estimators show a modest advantage over the benchmark VaR\operatorname{\mathrm{VaR}} estimator in terms of fit, but confidence threshold behavior is more sensitive to distributional assumptions; nevertheless, bias levels remain broadly in line with the traffic-light tolerance levels reported in Moldenhauer and Pitera [[2019](https://arxiv.org/html/2510.05809v1#bib.bib49)], where 0–5% CT output corresponds to the green performance zone and 5–10% CT output corresponds to the amber performance zone.

In contrast, the overlapping framework (Table [5](https://arxiv.org/html/2510.05809v1#S6.T5 "Table 5 ‣ Numerical study ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures")) yields markedly different outcomes: estimators #3 and #4 perform best in terms of fit, whereas estimators #5 and #6 are preferable for risk coverage. Here, the ES estimators #1–#4 often exhibit substantial negative bias, particularly for heavy-tailed distributions, reflecting the effective reduction in sample size (comparable to n≈27n\approx 27 by matching standard errors in a normal distribution setup) and the underestimation of tail scenario risk inherent to the overlapping setup in which standard sample estimators are used. As a result, ES estimator choice becomes critical, since naïve ES estimators can underestimate true ES by as much as 5–15%, especially in non-Gaussian settings, with potential material implications for capital adequacy under FRTB, see BCBS [[2019](https://arxiv.org/html/2510.05809v1#bib.bib13)].

Finally, it should be noted that this study is synthetic, and in practice additional features such as heteroskedasticity may further distort ES estimates; moreover, systematic analyses of overlapping constructions remain scarce in the literature, despite their regulatory and supervisory relevance. The results reported here are consistent with findings in [EBA, [2023](https://arxiv.org/html/2510.05809v1#bib.bib29), Annex I] and Aichele et al. [[2021](https://arxiv.org/html/2510.05809v1#bib.bib4)], both of which emphasize the importance of proper risk control and estimator selection, especially in the overlapping case. In this regard, our study also underlines that estimator adequacy and bias can be addressed by directly modifying the weight inputs (see Table [2](https://arxiv.org/html/2510.05809v1#S6.T2 "Table 2 ‣ Non-parametric ES estimators ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures")), which provides a natural motivation for further research on robust representations for CREs.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Distribution | Type | Metric | Estimator | | | | | | |
| VaR^1%\widehat{\operatorname{\mathrm{VaR}}}\_{1\%} | #1 | #2 | #3 | #4 | #5 | #6 |
| Normal | Fit | A​EAE | 8.5% | 7.0% | 6.9% | 7.3% | 12.2% | 10.8% | 19.5% |
| S​ESE | 10.8% | 8.7% | 8.7% | 9.2% | 15.0% | 13.4% | 22.2% |
| Bias | S​BSB | 3.3% | -0.8% | -1.5% | 1.3% | 10.9% | 9.2% | 19.3% |
| R​BRB | 0.6% | -2.8% | -3.3% | -0.8% | 8.3% | 6.8% | 16.2% |
| Conf. | C​TCT | 1.0% | 3.0% | 3.1% | 2.6% | 1.5% | 1.6% | 0.9% |
| Student’s tt (ν=5\nu=5) | Fit | A​EAE | 15.9% | 13.2% | 13.0% | 14.6% | 19.7% | 17.0% | 25.3% |
| S​ESE | 21.6% | 17.1% | 16.7% | 19.9% | 27.8% | 23.6% | 33.9% |
| Bias | S​BSB | 7.9% | -0.8% | -1.8% | 3.6% | 15.1% | 11.3% | 23.3% |
| R​BRB | 1.1% | -5.9% | -6.7% | -2.7% | 6.8% | 4.3% | 14.1% |
| Conf. | C​TCT | 1.0% | 3.1% | 3.2% | 2.8% | 1.9% | 2.1% | 1.5% |
| NIG (α=0.4,β=0.14\alpha=0.4,\beta=0.14) | Fit | A​EAE | 18.2% | 14.4% | 14.3% | 15.8% | 21.2% | 18.3% | 26.6% |
| S​ESE | 24.2% | 18.2% | 17.9% | 20.5% | 28.1% | 24.2% | 34.2% |
| Bias | S​BSB | 8.8% | -0.9% | -2.1% | 3.9% | 15.6% | 11.4% | 23.7% |
| R​BRB | 1.3% | -6.3% | -7.3% | -2.5% | 7.3% | 4.2% | 14.4% |
| Conf. | C​TCT | 1.0% | 3.1% | 3.2% | 2.7% | 2.0% | 2.2% | 1.6% |
| NIG (α=0.4,β=−0.14\alpha=0.4,\beta=-0.14) | Fit | A​EAE | 19.8% | 15.6% | 15.4% | 17.1% | 22.7% | 19.6% | 28.0% |
| S​ESE | 26.5% | 19.7% | 19.3% | 22.3% | 30.3% | 26.1% | 36.4% |
| Bias | S​BSB | 9.7% | -0.8% | -2.1% | 4.4% | 16.4% | 11.8% | 24.5% |
| R​BRB | 1.5% | -6.8% | -7.9% | -2.8% | 7.0% | 3.8% | 14.0% |
| Conf. | C​TCT | 1.0% | 3.1% | 3.2% | 2.7% | 2.0% | 2.2% | 1.6% |
| NIG (α=0.55,β=0.3025\alpha=0.55,\beta=0.3025) | Fit | A​EAE | 17.1% | 13.6% | 13.5% | 14.8% | 20.1% | 17.4% | 25.6% |
| S​ESE | 22.6% | 17.1% | 16.8% | 19.2% | 26.5% | 22.9% | 32.7% |
| Bias | S​BSB | 8.0% | -0.9% | -2.1% | 3.5% | 15.0% | 11.1% | 23.1% |
| R​BRB | 1.2% | -5.8% | -6.8% | -2.3% | 7.5% | 4.6% | 14.8% |
| Conf. | C​TCT | 1.0% | 3.1% | 3.2% | 2.7% | 1.9% | 2.1% | 1.5% |
| NIG (α=0.55,β=−0.3025\alpha=0.55,\beta=-0.3025) | Fit | A​EAE | 19.0% | 15.1% | 14.9% | 16.5% | 22.0% | 19.0% | 27.3% |
| S​ESE | 25.4% | 19.0% | 18.6% | 21.5% | 29.3% | 25.2% | 35.4% |
| Bias | S​BSB | 9.2% | -0.8% | -2.1% | 4.1% | 16.1% | 11.7% | 24.1% |
| R​BRB | 1.5% | -6.5% | -7.5% | -2.7% | 7.2% | 4.0% | 14.2% |
| Conf. | C​TCT | 1.0% | 3.1% | 3.2% | 2.7% | 2.0% | 2.2% | 1.6% |
| NIG (α=0.4,β=0.22\alpha=0.4,\beta=0.22) | Fit | A​EAE | 18.1% | 14.4% | 14.2% | 15.7% | 21.1% | 18.3% | 26.5% |
| S​ESE | 24.1% | 18.2% | 17.8% | 20.4% | 28.0% | 24.2% | 34.2% |
| Bias | S​BSB | 8.7% | -0.9% | -2.1% | 3.9% | 15.6% | 11.4% | 23.7% |
| R​BRB | 1.4% | -6.2% | -7.2% | -2.5% | 7.4% | 4.3% | 14.5% |
| Conf. | C​TCT | 1.0% | 3.1% | 3.2% | 2.7% | 2.0% | 2.2% | 1.6% |
| NIG (α=0.4,β=−0.22\alpha=0.4,\beta=-0.22) | Fit | A​EAE | 21.0% | 16.5% | 16.3% | 18.1% | 23.9% | 20.6% | 29.0% |
| S​ESE | 28.1% | 20.8% | 20.4% | 23.7% | 32.0% | 27.4% | 38.0% |
| Bias | S​BSB | 10.4% | -0.8% | -2.2% | 4.7% | 17.0% | 12.1% | 25.0% |
| R​BRB | 1.7% | -7.2% | -8.3% | -3.0% | 6.9% | 3.5% | 13.8% |
| Conf. | C​TCT | 1.0% | 3.1% | 3.2% | 2.7% | 2.0% | 2.3% | 1.7% |

Table 4: Performance output for non-overlapping data and ES estimators #1-#6. Sample size n=250n=250 and confidence threshold α=2.5%\alpha=2.5\%. See Table [1](https://arxiv.org/html/2510.05809v1#S6.T1 "Table 1 ‣ Non-parametric ES estimators ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures") for the definitions of the ES estimators, and Table [3](https://arxiv.org/html/2510.05809v1#S6.T3 "Table 3 ‣ Evaluation of ES estimators ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures") for the performance metric summary. Estimator VaR^1%\widehat{\operatorname{\mathrm{VaR}}}\_{1\%} is defined in ([6.1](https://arxiv.org/html/2510.05809v1#S6.E1 "In Numerical study ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures")). The best results for the ES estimators are highlighted in bold–one can see that estimators #1–#3 outperform estimators #4–#6.



|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Distribution | Type | Metric | Estimator | | | | | | |
| VaR^1%\widehat{\operatorname{\mathrm{VaR}}}\_{1\%} | #1 | #2 | #3 | #4 | #5 | #6 |
| Normal | Fit | A​EAE | 15.3% | 15.3% | 15.3% | 15.0% | 15.5% | 15.3% | 18.5% |
| S​ESE | 19.2% | 18.9% | 18.9% | 18.7% | 19.9% | 19.6% | 24.0% |
| Bias | S​BSB | -2.6% | -6.4% | -6.9% | -5.0% | 3.6% | 2.6% | 11.5% |
| R​BRB | -10.9% | -13.8% | -14.3% | -12.6% | -5.3% | -6.2% | 1.3% |
| Conf. | C​TCT | 1.8% | 5.3% | 5.5% | 5.0% | 3.4% | 3.5% | 2.3% |
| Student’s tt (ν=5\nu=5) | Fit | A​EAE | 18.5% | 18.7% | 18.8% | 18.4% | 18.2% | 18.1% | 20.2% |
| S​ESE | 24.2% | 23.7% | 23.7% | 23.5% | 24.7% | 24.4% | 28.2% |
| Bias | S​BSB | -3.0% | -7.9% | -8.4% | -6.5% | 1.9% | 0.9% | 9.7% |
| R​BRB | -13.5% | -17.0% | -17.4% | -15.8% | -8.9% | -9.8% | -2.7% |
| Conf. | C​TCT | 2.0% | 5.8% | 5.9% | 5.5% | 3.9% | 4.1% | 2.9% |
| NIG (α=0.4,β=0.14\alpha=0.4,\beta=0.14) | Fit | A​EAE | 24.8% | 24.8% | 24.9% | 24.4% | 24.5% | 24.5% | 26.3% |
| S​ESE | 31.5% | 30.7% | 30.7% | 30.4% | 31.8% | 31.5% | 35.0% |
| Bias | S​BSB | -4.2% | -10.4% | -11.1% | -8.5% | 0.1% | -1.5% | 7.5% |
| R​BRB | -18.0% | -22.5% | -23.0% | -20.8% | -14.3% | -15.6% | -8.8% |
| Conf. | C​TCT | 1.9% | 5.7% | 5.8% | 5.4% | 4.2% | 4.4% | 3.5% |
| NIG (α=0.4,β=−0.14\alpha=0.4,\beta=-0.14) | Fit | A​EAE | 19.0% | 19.4% | 19.5% | 19.1% | 18.5% | 18.5% | 20.0% |
| S​ESE | 24.0% | 23.7% | 23.8% | 23.6% | 24.2% | 24.0% | 27.3% |
| Bias | S​BSB | -4.6% | -8.9% | -9.3% | -7.8% | 0.3% | -0.4% | 8.0% |
| R​BRB | -15.2% | -18.3% | -18.6% | -17.4% | -10.9% | -11.4% | -4.7% |
| Conf. | C​TCT | 2.2% | 6.6% | 6.7% | 6.3% | 4.4% | 4.6% | 3.2% |
| NIG (α=0.55,β=0.3025\alpha=0.55,\beta=0.3025) | Fit | A​EAE | 36.1% | 35.8% | 36.0% | 35.2% | 36.1% | 36.2% | 38.3% |
| S​ESE | 45.7% | 44.3% | 44.4% | 43.9% | 46.1% | 45.9% | 49.7% |
| Bias | S​BSB | -5.7% | -14.8% | -16.0% | -11.7% | -2.5% | -5.2% | 4.4% |
| R​BRB | -25.4% | -32.1% | -33.1% | -29.4% | -23.1% | -25.5% | -19.1% |
| Conf. | C​TCT | 1.8% | 5.4% | 5.5% | 5.0% | 4.3% | 4.6% | 3.9% |
| NIG (α=0.55,β=−0.3025\alpha=0.55,\beta=-0.3025) | Fit | A​EAE | 17.3% | 17.7% | 17.7% | 17.4% | 16.8% | 16.7% | 18.4% |
| S​ESE | 21.8% | 21.6% | 21.6% | 21.5% | 22.0% | 21.8% | 25.2% |
| Bias | S​BSB | -4.3% | -8.2% | -8.5% | -7.2% | 0.8% | 0.2% | 8.6% |
| R​BRB | -13.9% | -16.8% | -17.1% | -16.0% | -9.4% | -9.8% | -2.9% |
| Conf. | C​TCT | 2.3% | 6.7% | 6.8% | 6.4% | 4.4% | 4.5% | 3.0% |
| NIG (α=0.4,β=0.22\alpha=0.4,\beta=0.22) | Fit | A​EAE | 31.2% | 31.0% | 31.1% | 30.5% | 31.0% | 31.0% | 32.9% |
| S​ESE | 39.6% | 38.3% | 38.4% | 38.0% | 39.8% | 39.6% | 43.2% |
| Bias | S​BSB | -4.9% | -12.9% | -13.8% | -10.3% | -1.4% | -3.6% | 5.7% |
| R​BRB | -22.1% | -27.8% | -28.5% | -25.5% | -19.1% | -21.0% | -14.4% |
| Conf. | C​TCT | 1.9% | 5.5% | 5.6% | 5.2% | 4.3% | 4.5% | 3.8% |
| NIG (α=0.4,β=−0.22\alpha=0.4,\beta=-0.22) | Fit | A​EAE | 19.4% | 19.9% | 19.9% | 19.6% | 18.8% | 18.7% | 20.0% |
| S​ESE | 24.4% | 24.2% | 24.2% | 24.1% | 24.5% | 24.4% | 27.3% |
| Bias | S​BSB | -5.3% | -9.4% | -9.8% | -8.4% | -0.5% | -1.1% | 7.2% |
| R​BRB | -15.9% | -19.0% | -19.3% | -18.2% | -11.8% | -12.3% | -5.6% |
| Conf. | C​TCT | 2.3% | 7.0% | 7.1% | 6.7% | 4.7% | 4.9% | 3.4% |

Table 5: 
Performance output for overlapping data and ES estimators #1-#6. Sample size n=250n=250 and confidence threshold α=2.5%\alpha=2.5\%. See Table [1](https://arxiv.org/html/2510.05809v1#S6.T1 "Table 1 ‣ Non-parametric ES estimators ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures") for the definitions of the ES estimators, and Table [3](https://arxiv.org/html/2510.05809v1#S6.T3 "Table 3 ‣ Evaluation of ES estimators ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures") for the performance metric summary. Estimator VaR^1%\widehat{\operatorname{\mathrm{VaR}}}\_{1\%} is defined in ([6.1](https://arxiv.org/html/2510.05809v1#S6.E1 "In Numerical study ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures")). The best results for the ES estimators are highlighted in bold–one can see that the estimators #3-#6 are outperforming the estimators #1-#2, which creates a material difference, when confronted with the non-overlapping data presented in Table [4](https://arxiv.org/html/2510.05809v1#S6.T4 "Table 4 ‣ Numerical study ‣ 6 Numerical study: comparison of ES estimators based on L-statistics ‣ Coherent estimation of risk measures").

## Disclaimer

The views and opinions expressed in this paper are the authors’ own and do not necessarily reflect the views and opinions of their current or past employers. In particular, they cannot be taken to represent those of the European Central Bank (ECB) or to state the ECB’s policy. Neither the ECB nor any person acting on its behalf may be held responsible for the use which may be made of the information contained in this publication, or for any errors which, despite careful preparation and checking, may appear therein.

## Acknowledgements

Igor Cialenco acknowledges support from the US National Science Foundation grant DMS-2407549. Damian Jelito acknowledges support from the National Science Centre, Poland, via project 2024/53/B/ST1/00703. Marcin Pitera acknowledges support from the National Science Centre, Poland, via project 2024/53/B/HS4/00433. Martin Aichele thanks Carlo Acerbi for helpful discussions on preparatory work on ES estimation.

## References

* Aaronson et al. [1996]

  Aaronson, J., Burton, R.,
  Dehling, H., Gilat, D.,
  Hill, T., Weiss, B.,
  1996.
  Strong laws for LL-and UU-statistics.
  Transactions of the American Mathematical Society
  348, 2845–2866.
* Acerbi [2002]

  Acerbi, C., 2002.
  Spectral measures of risk: a coherent representation
  of subjective risk aversion.
  Journal of Banking & Finance
  26, 1505–1518.
* Acerbi and Tasche [2002]

  Acerbi, C., Tasche, D.,
  2002.
  On the coherence of expected shortfall.
  Journal of Banking & Finance
  26, 1487–1503.
* Aichele et al. [2021]

  Aichele, M., Crotti, M.G.,
  Rehle, B., 2021.
  A Universal Stress Scenario Approach for
  Capitalising Non-modellable Risk Factors Under the FRTB.
  European Banking Authority Staff Paper Series .
* Alexander [2009]

  Alexander, C., 2009.
  Market Risk Analysis. volume
  1–4.
  John Wiley & Sons.
* Arnold et al. [2008]

  Arnold, B.C., Balakrishnan, N.,
  Nagaraja, H.N., 2008.
  A first course in order statistics.
  SIAM.
* Artzner et al. [1997]

  Artzner, P., Delbaen, F.,
  Eber, J., Heath, D.,
  1997.
  Thinking coherently.
  Risk 10,
  68–71.
* Artzner et al. [1999]

  Artzner, P., Delbaen, F.,
  Eber, J., Heath, D.,
  1999.
  Coherent measures of risk.
  Math. Finance 9,
  203–228.
* Bartl and Eckstein [2024]

  Bartl, D., Eckstein, S.,
  2024.
  Optimal nonparametric estimation of the expected
  shortfall risk.
  [arXiv:2405.00357](http://arxiv.org/abs/2405.00357).
* Bartl and Tangpi [2023]

  Bartl, D., Tangpi, L.,
  2023.
  Nonasymptotic convergence rates for the plug-in
  estimation of risk measures.
  Mathematics of Operations Research
  48, 2129–2155.
* BCBS [2006]

  BCBS, 2006.
  Basel II: International Convergence of Capital
  Measurement and Capital Standards: A Revised Framework - Comprehensive
  Version.
  Technical Report. Bank for International Settlements,
  Basel Committee on Banking Supervision.
* BCBS [2013]

  BCBS, 2013.
  Fundamental review of the trading book: A revised
  market risk framework - Consultative document.
  Technical Report. Bank for International Settlements,
  Basel Committee on Banking Supervision.
* BCBS [2019]

  BCBS, 2019.
  Minimum capital requirements for market risk.
  Technical Report. Bank for International Settlements,
  Basel Committee on Banking Supervision.
* Bellini and Di Bernardino [2017]

  Bellini, F., Di Bernardino, E.,
  2017.
  Risk management with expectiles.
  The European Journal of Finance
  23, 487–506.
* Bellini et al. [2019]

  Bellini, F., Negri, I.,
  Pyatkova, M., 2019.
  Backtesting VaR and expectiles with realized
  scores.
  Statistical Methods & Applications
  28, 119–142.
* Belomestny and Krätschmer [2012]

  Belomestny, D., Krätschmer, V.,
  2012.
  Central limit theorems for law-invariant coherent
  risk measures.
  Journal of Applied Probability
  49, 1–21.
* Beutner and Zähle [2010]

  Beutner, E., Zähle, H.,
  2010.
  A modified functional delta method and its
  application to the estimation of risk functionals.
  Journal of Multivariate Analysis
  101, 2452–2463.
* Bielecki et al. [2016]

  Bielecki, T.R., Cialenco, I.,
  Drapeau, S., Karliczek, M.,
  2016.
  Dynamic assessment indices.
  Stochastics 88,
  1–44.
* Bielecki et al. [2024]

  Bielecki, T.R., Cialenco, I.,
  Liu, H., 2024.
  Time consistency of dynamic risk measures and dynamic
  performance measures generated by distortion functions.
  Stochastic Models 40,
  2609–2623.
* Bielecki et al. [2020]

  Bielecki, T.R., Cialenco, I.,
  Pitera, M., Schmidt, T.,
  2020.
  Fair estimation of capital risk allocation.
  Statistics & Risk Modeling 37,
  1–24.
* Boyd and Vandenberghe [2004]

  Boyd, S., Vandenberghe, L.,
  2004.
  Convex optimization.
  Cambridge University Press .
* CBUAE [2023]

  CBUAE, 2023.
  CBUAE Rulebook.
  Technical Report. Central Bank of the United Arab
  Emirates.
  URL: <https://rulebook.centralbank.ae/en>.
* Chen [2008]

  Chen, S.X., 2008.
  Nonparametric estimation of expected shortfall.
  Journal of Financial Econometrics
  6, 87–107.
* Cherny [2006]

  Cherny, A.S., 2006.
  Weighted V@R and its properties.
  Finance Stoch. 10,
  367–393.
* Cont et al. [2010]

  Cont, R., Deguest, R.,
  Scandolo, G., 2010.
  Robustness and sensitivity analysis of risk
  measurement procedures.
  Quantitative Finance 10,
  593–606.
* David and Nagaraja [2003]

  David, H.A., Nagaraja, H.N.,
  2003.
  Order Statistics.
  Wiley.
* Delbaen [2002]

  Delbaen, F., 2002.
  Coherent risk measures on general probability
  spaces, in: Advances in finance and stochastics.
  Springer, pp. 1–37.
* Drapeau and Kupper [2013]

  Drapeau, S., Kupper, M.,
  2013.
  Risk preferences and their robust representation.
  Mathematics of Operations Research
  38, 28–62.
* EBA [2023]

  EBA, 2023.
  Final report – Draft RTS on the assessment
  methodology under which competent authorities verify an institution’s
  compliance with the internal model approach as per Article 325az(8) of
  Regulation (EU) No 575/2013 (Capital Requirements Regulation 2 - CRR2).
  Technical Report EBA/RTS/2023/05.
  European Banking Authority.
* EBA [2025]

  EBA, 2025.
  EBA report results from the 2024 Market Risk
  benchmarking exercise – Part 1 - IMA.
  Technical Report EBA/REP/2025/11.
  European Banking Authority.
* ECB [2025]

  ECB, 2025.
  ECB guide to internal models, market risk chapters
  (July 2025).
  Technical Report. European Central Bank.
  URL: <https://www.bankingsupervision.europa.eu/ecb/pub/pdf/ssm.supervisory_guide202507.en.pdf>.
* Embrechts et al. [2022]

  Embrechts, P., Schied, A.,
  Wang, R., 2022.
  Robustness in the optimization of risk measures.
  Operations Research 70,
  95–110.
* EU [2024a]

  EU, 2024a.
  Commission Delegated Regulation (EU) 2024/1085 of 13
  March 2024 supplementing Regulation (EU) No 575/2013 of the European
  Parliament and of the Council with regard to regulatory technical standards
  on the assessment methodology under which competent authorities verify an
  institution’s compliance with the requirements to use internal models for
  market risk.
  OJ L 2024/1085, 17 June 2024.
  Official Journal of the European Union.
* EU [2024b]

  EU, 2024b.
  Commission Delegated Regulation (EU) 2024/397 of 20
  October 2023 supplementing Regulation (EU) No 575/2013 of the European
  Parliament and of the Council with regard to regulatory technical standards
  on the calculation of the stress scenario risk measure.
  OJ L 2024/397, 5 February 2024.
  Official Journal of the European Union.
* Fissler and Ziegel [2016]

  Fissler, T., Ziegel, J.F.,
  2016.
  Higher order elicitability and Osbands’ principle.
  The Annals of Statistics 44,
  1680 – 1707.
* Föllmer and Schied [2016]

  Föllmer, H., Schied, A.,
  2016.
  Stochastic finance. An introduction in discrete
  time.
  fourth ed., Walter de Gruyter
  & Co., Berlin.
* Gneiting [2011]

  Gneiting, T., 2011.
  Making and evaluating point forecasts.
  Journal of the American Statistical Association
  106, 746–762.
* Hansen and Lunde [2005]

  Hansen, P.R., Lunde, A.,
  2005.
  A forecast comparison of volatility models: does
  anything beat a GARCH (1, 1)?
  Journal of Applied Econometrics
  20, 873–889.
* Hardy et al. [1988]

  Hardy, G.H., Littlewood, J.E.,
  Polya, G., 1988.
  Inequalities.
  Cambridge University Press.
* HKMA [2024]

  HKMA, 2024.
  Supervisory Policy Manual, MR-1,V.1 –
  15.03.2024.
  Technical Report. HKMA.
* Hyndman and Athanasopoulos [2018]

  Hyndman, R.J., Athanasopoulos, G.,
  2018.
  Forecasting: principles and practice.
  OTexts.
* Hyndman and Fan [1996]

  Hyndman, R.J., Fan, Y.,
  1996.
  Sample Quantiles in Statistical Packages.
  The American Statistician 50,
  361–365.
* Kellner and Rösch [2016]

  Kellner, R., Rösch, D.,
  2016.
  Quantifying market risk with value-at-risk or
  expected shortfall? – consequences for capital requirements and model risk.
  Journal of Econ. Dyn. and Control
  68, 45 – 63.
* Kusuoka [2001]

  Kusuoka, S., 2001.
  On law invariant coherent risk measures, in:
  Advances in mathematical economics.
  Springer, pp. 83–95.
* Mason [1982]

  Mason, D.M., 1982.
  Some characterizations of strong laws for linear
  functions of order statistics.
  The Annals of Probability 10,
  1051–1057.
* McNeil [1999]

  McNeil, A.J., 1999.
  Extreme value theory for risk managers.
  Internal Modelling and CAD II published by
  RISK Books , 93–113.
* McNeil et al. [2010]

  McNeil, A.J., Frey, R.,
  Embrechts, P., 2010.
  Quantitative Risk Management: Concepts, Techniques,
  and Tools.
  Princeton University Press.
* Miao and Ma [2021]

  Miao, Y., Ma, M., 2021.
  Some limit behavior for linear combinations of order
  statistics.
  Kybernetika 57,
  970–988.
* Moldenhauer and Pitera [2019]

  Moldenhauer, F., Pitera, M.,
  2019.
  Backtesting expected shortfall: a simple recipe?
  Journal of Risk 22.
* Nadarajah et al. [2014]

  Nadarajah, S., Zhang, B.,
  Chan, S., 2014.
  Estimation methods for expected shortfall.
  Quantitative Finance 14,
  271–291.
* Pflug and Wozabal [2010]

  Pflug, G., Wozabal, N.,
  2010.
  Asymptotic distribution of law-invariant risk
  functionals.
  Finance and Stochastics 14,
  397–418.
* Pitera and Schmidt [2018]

  Pitera, M., Schmidt, T.,
  2018.
  Unbiased estimation of risk.
  Journal of Banking & Finance
  91, 133–145.
* PRA [2020]

  PRA, 2020.
  Market risk, Supervisory Statement, SS13/13.
  Technical Report. PRA.
* Righi and Ceretta [2015]

  Righi, M.B., Ceretta, P.S.,
  2015.
  A comparison of expected shortfall estimation
  models.
  Journal of Economics and Business
  78, 14–47.
* Rockafellar and Uryasev [2002]

  Rockafellar, R.T., Uryasev, S.,
  2002.
  Conditional value-at-risk for general loss
  distributions.
  Journal of Banking & Finance
  26, 1443–1471.
* Ruiz and Nieto [2023]

  Ruiz, E., Nieto, M.R.,
  2023.
  Direct versus iterated multiperiod value-at-risk
  forecasts.
  Journal of Economic Surveys 37,
  915–949.
* Scott et al. [2011]

  Scott, D.J., Würtz, D.,
  Dong, C., Tran, T.T.,
  2011.
  Moments of the generalized hyperbolic distribution.
  Comput. Stat. 26,
  459–476.
* Serfling [1980]

  Serfling, R.J., 1980.
  Approximation theorems of mathematical statistics.
  John Wiley & Sons.
* Sun et al. [2009]

  Sun, H., Nelken, I., Han,
  G., Guo, J., 2009.
  Error of VaR by overlapping intervals.
  Risk 22, 86.
* Thiele [2020]

  Thiele, S., 2020.
  Modeling the conditional distribution of financial
  returns with asymmetric tails.
  Journal of Applied Econometrics
  35, 46–60.
* van der Vaart [1998]

  van der Vaart, A.W., 1998.
  Asymptotic Statistics.
  Cambridge Series in Statistical and Probabilistic Mathematics,
  Cambridge University Press.
* Weber [2007]

  Weber, S., 2007.
  Distribution-invariant risk measures, entropy, and
  large deviations.
  J. Appl. Probab. 44,
  16–40.
* Wozabal [2009]

  Wozabal, N., 2009.
  Uniform limit theorems for functions of order
  statistics.
  Statistics & Probability Letters
  79, 1450–1455.
* van Zwet [1980]

  van Zwet, W.R., 1980.
  A strong law for linear functions of order
  statistics.
  The Annals of Probability 8,
  986–990.