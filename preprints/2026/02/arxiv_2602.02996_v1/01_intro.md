---
authors:
- Charlie Che
- Tongseok Lim
- Yue Sun
doc_id: arxiv:2602.02996v1
family_id: arxiv:2602.02996
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and
  Its Computation
url_abs: http://arxiv.org/abs/2602.02996v1
url_html: https://arxiv.org/html/2602.02996v1
venue: arXiv q-fin
version: 1
year: 2026
---


Charlie Che
Authors are listed in alphabetical order by last name.charlie.che@jpmchase.com
Quantitative Trading & Research, JPMorganChase, New York, NY 10017, USA

Tongseok Lim∗
lim336@purdue.edu
Mitch Daniels School of Business, Purdue University, West Lafayette, Indiana 47907, USA

Yue Sun∗
yue.sun@jpmorgan.com
Global Technology Applied Research, JPMorganChase, New York, NY 10001, USA

###### Abstract

We establish dual attainment for the multimarginal, multi-asset martingale optimal transport (MOT) problem, a fundamental question in the mathematical theory of model-independent pricing and hedging in quantitative finance. Our main result proves the existence of dual optimizers under mild regularity and irreducibility conditions, extending previous duality and attainment results from the classical and two-marginal settings to arbitrary numbers of assets and time periods. This theoretical advance provides a rigorous foundation for robust pricing and hedging of complex, path-dependent financial derivatives. To support our analysis, we present numerical experiments that demonstrate the practical solvability of large-scale discrete MOT problems using the state-of-the-art primal-dual linear programming (PDLP) algorithm. In particular, we solve multi-dimensional (or vectorial) MOT instances arising from the robust pricing of worst-of autocallable options, confirming the accuracy and feasibility of our theoretical results. Our work advances the mathematical understanding of MOT and highlights its relevance for robust financial engineering in high-dimensional and model-uncertain environments.

## 1 Introduction

Martingale optimal transport (MOT) has emerged as a central topic in mathematical finance and probability, providing a rigorous framework for model-independent pricing and hedging of financial derivatives under marginal and martingale constraints. The MOT problem generalizes classical optimal transport (OT) by requiring the transport plan to respect the martingale property, which is fundamental for risk-neutral valuation in quantitative finance. While the classical OT problem, introduced by Monge and Kantorovich [[27](https://arxiv.org/html/2602.02996v1#bib.bib27), [20](https://arxiv.org/html/2602.02996v1#bib.bib20)], has a rich mathematical theory and wide-ranging applications [[34](https://arxiv.org/html/2602.02996v1#bib.bib34), [31](https://arxiv.org/html/2602.02996v1#bib.bib31)], the martingale extension introduces significant new challenges, both theoretically and computationally.

A key question in MOT is the existence of dual optimizers, the so-called *dual attainment* property. Dual attainment is not only of intrinsic mathematical interest, but also has direct implications for robust hedging: dual optimizers correspond to explicit sub- and super-hedging strategies using tradable instruments [[2](https://arxiv.org/html/2602.02996v1#bib.bib2), [3](https://arxiv.org/html/2602.02996v1#bib.bib3), [5](https://arxiv.org/html/2602.02996v1#bib.bib5), [4](https://arxiv.org/html/2602.02996v1#bib.bib4)]. While duality and dual attainment have been extensively studied in the classical OT and single-asset, two-period MOT settings [[3](https://arxiv.org/html/2602.02996v1#bib.bib3), [5](https://arxiv.org/html/2602.02996v1#bib.bib5), [4](https://arxiv.org/html/2602.02996v1#bib.bib4), [13](https://arxiv.org/html/2602.02996v1#bib.bib13)], the general case of multi-marginal, multi-asset MOT remains much less understood. Theoretical advances in this direction are crucial for the robust pricing and hedging of complex, path-dependent financial products, which often depend on the joint evolution of multiple assets over several time periods.

This paper is devoted to the theoretical development of dual attainment for the multimarginal, multi-asset MOT problem. We establish the existence of dual optimizers under mild regularity and irreducibility conditions, extending previous results to arbitrary numbers of assets and time periods. Our approach builds on and generalizes the techniques developed for the single-asset, two-period case, and provides a rigorous foundation for robust pricing and hedging in high-dimensional, path-dependent settings. The main results contribute to the mathematical understanding of MOT and open the door to further applications in quantitative finance.

While the primary focus of this work is theoretical, we complement our analysis with a numerical demonstration. Specifically, we apply a state-of-the-art large-scale linear programming solver, PDLP [[1](https://arxiv.org/html/2602.02996v1#bib.bib1), [18](https://arxiv.org/html/2602.02996v1#bib.bib18)], to solve discrete instances of the multimarginal MOT problem. To our knowledge, this is the first demonstration of PDLP applied to large-scale multimarginal MOT, and the results provide supporting evidence for the practical relevance and accuracy of our theoretical findings. The numerical experiments, including a case study on a worst-of autocallable option, are intended to illustrate the feasibility of solving high-dimensional MOT problems and to validate the dual attainment results in realistic financial scenarios.

##### Contributions.

The primary contribution of this paper is a rigorous proof of dual attainment for the multimarginal, multi-asset martingale optimal transport (MOT) problem under general conditions. We also present numerical illustrations based on PDLP as supporting evidence; however, the development of computational methodologies is not a focus of this work and serves only to corroborate the theoretical results. Overall, our findings advance the mathematical theory of MOT and provide a foundation for robust pricing and hedging in complex financial markets.

##### Organization.

The remainder of the paper is organized as follows.
Section [1.1](https://arxiv.org/html/2602.02996v1#S1.SS1 "1.1 Related Literature ‣ 1 Introduction ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") provides a review of the related literature on optimal transport, martingale optimal transport, and their connections to mathematical finance.
Section [1.2](https://arxiv.org/html/2602.02996v1#S1.SS2 "1.2 Applications in Quantitative Finance ‣ 1 Introduction ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") discusses key applications of MOT in quantitative finance, motivating the theoretical developments of this work.
Section [2](https://arxiv.org/html/2602.02996v1#S2 "2 Problem Formulation ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") introduces the mathematical formulation of the multimarginal martingale optimal transport problem, including the market setting, the VMOT problem, and its dual.
Section [3](https://arxiv.org/html/2602.02996v1#S3 "3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") develops our main theoretical results, establishing duality and dual attainment in the multi-marginal, multi-asset setting, and highlights the key ideas underlying the proofs.
Section [4](https://arxiv.org/html/2602.02996v1#S4 "4 Numerical Methods and Implementation ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") describes the numerical methodology, including the PDLP algorithm and the discrete MOT formulation, and Section [5](https://arxiv.org/html/2602.02996v1#S5 "5 Numerical Experiments and Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") reports numerical experiments that support the theoretical findings, with a focus on a worst-of autocallable option case study.
Section [6](https://arxiv.org/html/2602.02996v1#S6 "6 Conclusion and Future Work ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") concludes the paper and outlines directions for future research.
Finally, Section [7](https://arxiv.org/html/2602.02996v1#S7 "7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") contains detailed proofs of the main theoretical results.

### 1.1 Related Literature

The classical OT problem has been extensively studied, with foundational contributions by Monge, Kantorovich, and later Villani [[34](https://arxiv.org/html/2602.02996v1#bib.bib34)] and Santambrogio [[31](https://arxiv.org/html/2602.02996v1#bib.bib31)]. The extension to martingale constraints was pioneered in [[2](https://arxiv.org/html/2602.02996v1#bib.bib2), [3](https://arxiv.org/html/2602.02996v1#bib.bib3)], with further developments on duality and dual attainment in [[5](https://arxiv.org/html/2602.02996v1#bib.bib5), [4](https://arxiv.org/html/2602.02996v1#bib.bib4), [13](https://arxiv.org/html/2602.02996v1#bib.bib13)]. Multi-marginal and multi-asset MOT has been investigated in [[10](https://arxiv.org/html/2602.02996v1#bib.bib10), [28](https://arxiv.org/html/2602.02996v1#bib.bib28), [15](https://arxiv.org/html/2602.02996v1#bib.bib15), [21](https://arxiv.org/html/2602.02996v1#bib.bib21)], but dual attainment in the general setting remains an open and challenging problem. Applications in quantitative finance include model calibration [[25](https://arxiv.org/html/2602.02996v1#bib.bib25), [17](https://arxiv.org/html/2602.02996v1#bib.bib17), [16](https://arxiv.org/html/2602.02996v1#bib.bib16)], robust pricing and hedging [[19](https://arxiv.org/html/2602.02996v1#bib.bib19), [13](https://arxiv.org/html/2602.02996v1#bib.bib13)], and the extraction of risk-neutral marginals from market data using the Breeden–Litzenberger formula [[6](https://arxiv.org/html/2602.02996v1#bib.bib6)]. Moreover, recent advances in large-scale linear programming, such as PDLP [[1](https://arxiv.org/html/2602.02996v1#bib.bib1), [18](https://arxiv.org/html/2602.02996v1#bib.bib18)], have enabled practical solution of high-dimensional MOT problems, which we adopt as our computational approach in this paper.

### 1.2 Applications in Quantitative Finance

The martingale optimal transport (MOT) framework has found increasing relevance in quantitative finance, both as a tool for model calibration and for robust pricing and hedging of complex derivatives. In this section, we review key application domains, highlight recent advances, and illustrate how the multi-marginal, multi-asset MOT approach enables new capabilities for practitioners.

#### 1.2.1 Model Calibration via Martingale Optimal Transport

A major application of MOT in finance is the calibration of market models to observed data, particularly volatility surfaces and marginal distributions inferred from vanilla option prices. Traditional calibration methods often rely on parametric models, which may fail to capture the full range of market-implied dynamics. MOT provides a non-parametric alternative, allowing practitioners to fit models that are consistent with observed marginals while imposing the martingale property required by risk-neutral pricing.

Recent works have leveraged MOT for volatility surface fitting and stochastic volatility model calibration [[25](https://arxiv.org/html/2602.02996v1#bib.bib25), [17](https://arxiv.org/html/2602.02996v1#bib.bib17), [16](https://arxiv.org/html/2602.02996v1#bib.bib16)]. For example, Demarch and Labordere formulated volatility surface fitting as a MOT problem using entropic regularization, while Guyon addressed the joint calibration of SPX and VIX smiles. Guo, Loeper, and Wang extended these ideas to a general setting, enabling calibration with arbitrary cost functionals and constraints. The flexibility of the MOT framework allows for the incorporation of additional market observable information, such as intermediate marginals or observable non vanilla instruments, to further tighten calibration and pricing bounds [[22](https://arxiv.org/html/2602.02996v1#bib.bib22), [32](https://arxiv.org/html/2602.02996v1#bib.bib32)].

#### 1.2.2 Robust Pricing and Hedging

Beyond calibration, MOT has emerged as a powerful tool for robust pricing and hedging of exotic derivatives. The pioneering work of Hobson [[19](https://arxiv.org/html/2602.02996v1#bib.bib19)] used the Skorokhod embedding problem to derive tight, model-independent price bounds for complex derivatives. In practice, however, price bounds generated by classical optimal transport are often too wide to be useful, motivating the imposition of additional constraints such as martingality and observable market data.

The dual formulation of the MOT problem is particularly significant for hedging, as dual attainment corresponds to the existence of optimal sub- or super-hedging strategies using tradable instruments. Establishing dual attainment thus provides theoretical justification for robust hedging approaches and informs the construction of practical hedging portfolios.

Most research to date has focused on single-asset, two-period payoffs due to their theoretical tractability. However, many popular structured products in the market are multi-asset and path-dependent. Extending dual attainment results to the vectorial, multi-marginal setting, as in this work, provides a foundation for robust pricing and hedging of such exotics.

#### 1.2.3 Multi-Asset Path-Dependent Products

The MOT framework is especially well-suited for pricing and hedging multi-asset, path-dependent derivatives, such as autocallables, worst-of options, and basket products. These instruments often depend on the joint evolution of several underlyings over multiple time periods, and their payoffs are sensitive to both marginal distributions and the dependence structure among assets.

A key advantage of the MOT approach is its minimal reliance on assumptions about asset correlations or joint dynamics. By only requiring consistency with observed marginals and the martingale property, MOT produces price bounds that reflect genuine model uncertainty. These bounds can be further tightened by incorporating additional market information, such as prices of liquid correlation-sensitive products or intermediate marginals. For example, the pricing bounds generated from the vectorial multi-marginal MOT framework can be interpreted as the range of model uncertainty due to unknown correlations. By introducing constraints based on market prices of pairwise correlation products (e.g., call vs. call or put vs. put), practitioners can further refine these bounds. This flexibility opens the door to robust pricing and risk management for a wide variety of exotic products.

In summary, the martingale optimal transport framework offers a robust foundation for a wide range of financial applications, from model calibration to pricing and hedging of complex derivatives. In the following section, we turn to the numerical implementation and results that demonstrate the practical effectiveness of these methods.

## 2 Problem Formulation

This section introduces the mathematical framework for martingale optimal transport in multi-asset, multi-period markets. We first describe the market setting and the available marginal information, then formulate the vectorial martingale optimal transport (VMOT) problem, and finally present its dual formulation together with its financial interpretation.

### 2.1 Market Setting and Marginal Information

Consider a financial market with dd underlying assets, whose price processes are denoted by (Xt,i)t≥0(X\_{t,i})\_{t\geq 0} for each asset i∈[d]:={1,2,…,d}i\in[d]:=\{1,2,\dots,d\}. We do not assume that the joint law of all asset prices—often referred to as the *market model*—is known, since such information cannot be fully inferred from observable market data.

Instead, following the classical argument of Breeden and Litzenberger [[6](https://arxiv.org/html/2602.02996v1#bib.bib6)], we assume that the market reveals the marginal distribution of each asset price at any fixed maturity t>0t>0. That is, for each tt and ii, the distribution Law​(Xt,i)=μt,i∈𝒫​(ℝ){\rm Law}(X\_{t,i})=\mu\_{t,i}\in{\cal P}({\mathbb{R}}) is observed, where 𝒫​(𝒳){\cal P}({\cal X}) denotes the set of probability measures on a space 𝒳{\cal X}. We consider a finite collection of maturities 0<T1<T2<⋯<TN0<T\_{1}<T\_{2}<\dots<T\_{N}, and for notational convenience write Xt,i:=XTt,iX\_{t,i}:=X\_{T\_{t},i} and Xt:=(Xt,1,…,Xt,d)X\_{t}:=(X\_{t,1},\dots,X\_{t,d}). Throughout the paper, we assume (Xt)t∈[N](X\_{t})\_{t\in[N]} is an ℝd{\mathbb{R}}^{d}-valued martingale, consistent with the standard risk-neutral framework in mathematical finance. While the full joint distribution Law​(X1,…,XN){\rm Law}(X\_{1},\dots,X\_{N}) remains unspecified, we assume that the collection of N​dNd marginal distributions μt,i:=Law​(Xt,i)\mu\_{t,i}:={\rm Law}(X\_{t,i}) is fixed and known. This motivates the following admissible class.

###### Definition 2.1 (Vectorial Martingale Transports).

Assume the marginal measures (μt,i)t,i(\mu\_{t,i})\_{t,i} have finite first moments. Let μt:=(μt,1,…,μt,d)\mu\_{t}:=(\mu\_{t,1},\dots,\mu\_{t,d}) and μ:=(μ1,…,μN)\mu:=(\mu\_{1},\dots,\mu\_{N}). The set of *vectorial martingale transports* is defined by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | VMT(μ):={π∈𝒫(ℝN​d)|\displaystyle{\rm VMT}(\mu):=\Big\{\pi\in{\cal P}({\mathbb{R}}^{Nd})\ \Big|\ | π=Law​(X),𝔼π​[Xt+1∣Xt]=Xt,\displaystyle\pi={\rm Law}(X),\quad\mathbb{E}\_{\pi}[X\_{t+1}\mid X\_{t}]=X\_{t}, |  | (2.1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Law(Xt,i)=μt,ifor all t∈[N],i∈[d]}.\displaystyle{\rm Law}(X\_{t,i})=\mu\_{t,i}\ \text{for all }t\in[N],\ i\in[d]\Big\}. |  |

### 2.2 Vectorial Martingale Optimal Transport (VMOT)

Given a measurable cost (or payoff) function c:ℝN​d→ℝc:{\mathbb{R}}^{Nd}\to{\mathbb{R}}, the vectorial martingale optimal transport (VMOT) problem is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | minπ∈VMT​(μ)⁡𝔼π​[c​(X)]ormaxπ∈VMT​(μ)⁡𝔼π​[c​(X)].\displaystyle\min\_{\pi\in{\rm VMT}(\mu)}\ \mathbb{E}\_{\pi}[c(X)]\qquad\text{or}\qquad\max\_{\pi\in{\rm VMT}(\mu)}\ \mathbb{E}\_{\pi}[c(X)]. |  | (2.2) |

In a financial interpretation, c​(X)c(X) represents the payoff of a path-dependent derivative determined by the entire price trajectory X=(Xt)t=1NX=(X\_{t})\_{t=1}^{N}. Since the true market model π\pi is unknown, all martingale measures consistent with the observed marginal information must be considered. The minimum and maximum values in ([2.2](https://arxiv.org/html/2602.02996v1#S2.E2 "Equation 2.2 ‣ 2.2 Vectorial Martingale Optimal Transport (VMOT) ‣ 2 Problem Formulation ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) therefore correspond to the lower and upper arbitrage-free bounds for the derivative price.

A key distinction between VMOT and classical optimal transport lies in the martingale constraint 𝔼π​[Xt+1∣Xt]=Xt\mathbb{E}\_{\pi}[X\_{t+1}\mid X\_{t}]=X\_{t}. This constraint imposes that, for each asset ii and time tt, the marginal distributions satisfy the *convex order* condition

|  |  |  |
| --- | --- | --- |
|  | μt,i⪯cμt+1,i,\mu\_{t,i}\preceq\_{c}\mu\_{t+1,i}, |  |

meaning that μt,i​(f)≤μt+1,i​(f)\mu\_{t,i}(f)\leq\mu\_{t+1,i}(f) for all convex functions ff on ℝ{\mathbb{R}}, where μ​(f):=∫f​(x)​𝑑μ​(x)\mu(f):=\int f(x)d\mu(x). Strassen’s theorem [[33](https://arxiv.org/html/2602.02996v1#bib.bib33)] guarantees that this condition is both necessary and sufficient for VMT​(μ){\rm VMT}(\mu) to be nonempty. Accordingly, we assume μt,i⪯cμt+1,i\mu\_{t,i}\preceq\_{c}\mu\_{t+1,i} for all t<Nt<N and i∈[d]i\in[d] throughout the paper.

### 2.3 Dual Problem and Financial Interpretation

The VMOT problem is an infinite-dimensional linear program and therefore admits a natural dual formulation. When ([2.2](https://arxiv.org/html/2602.02996v1#S2.E2 "Equation 2.2 ‣ 2.2 Vectorial Martingale Optimal Transport (VMOT) ‣ 2 Problem Formulation ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) is a minimization problem, the dual problem takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(ϕ,h)∈Ψμ​(ϕ),\sup\_{(\phi,h)\in\Psi}\ \mu(\phi), |  | (2.3) |

where ϕ=(ϕ1,…,ϕN)\phi=(\phi\_{1},\dots,\phi\_{N}) with ϕt=(ϕt,1,…,ϕt,d)\phi\_{t}=(\phi\_{t,1},\dots,\phi\_{t,d}), each ϕt,i:ℝ→ℝ∪{−∞}\phi\_{t,i}:{\mathbb{R}}\to{\mathbb{R}}\cup\{-\infty\}, and

|  |  |  |
| --- | --- | --- |
|  | μ​(ϕ):=∑t=1N∑i=1d∫ϕt,i​𝑑μt,i.\mu(\phi):=\sum\_{t=1}^{N}\sum\_{i=1}^{d}\int\phi\_{t,i}\,d\mu\_{t,i}. |  |

The process h=(h1,…,hN)h=(h\_{1},\dots,h\_{N}), with hN≡0h\_{N}\equiv 0, consists of functions ht,i:ℝt​d→ℝh\_{t,i}:{\mathbb{R}}^{td}\to{\mathbb{R}} representing dynamic trading strategies. The admissible class Ψ\Psi consists of all (ϕ,h)(\phi,h) such that ϕt,i∈L1​(μt,i)\phi\_{t,i}\in L^{1}(\mu\_{t,i}), ht,ih\_{t,i} is bounded, and the following pathwise inequality holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑t=1N∑i=1dϕt,i​(xt,i)+ht,i​(x1,…,xt)​(xt+1,i−xt,i)≤c​(x),\displaystyle\sum\_{t=1}^{N}\sum\_{i=1}^{d}\phi\_{t,i}(x\_{t,i})+h\_{t,i}(x\_{1},\dots,x\_{t})\,(x\_{t+1,i}-x\_{t,i})\leq c(x), |  | (2.4) |

for all x=(x1,…,xN)∈ℝN​dx=(x\_{1},\dots,x\_{N})\in{\mathbb{R}}^{Nd}.

For any π∈VMT​(μ)\pi\in{\rm VMT}(\mu) and (ϕ,h)∈Ψ(\phi,h)\in\Psi, the martingale property implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ​(ϕ)=𝔼π​[∑t=1N∑i=1dϕt,i​(Xt,i)+ht,i​(X1,…,Xt)​(Xt+1,i−Xt,i)].\mu(\phi)=\mathbb{E}\_{\pi}\!\left[\sum\_{t=1}^{N}\sum\_{i=1}^{d}\phi\_{t,i}(X\_{t,i})+h\_{t,i}(X\_{1},\dots,X\_{t})\,(X\_{t+1,i}-X\_{t,i})\right]. |  | (2.5) |

Thus the dual value represents the cost of a semi-static hedging strategy composed of European options ϕ\phi and dynamic trading strategies hh. The inequality ([2.4](https://arxiv.org/html/2602.02996v1#S2.E4 "Equation 2.4 ‣ 2.3 Dual Problem and Financial Interpretation ‣ 2 Problem Formulation ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) enforces that the portfolio subhedges the payoff cc pathwise. When ([2.2](https://arxiv.org/html/2602.02996v1#S2.E2 "Equation 2.2 ‣ 2.2 Vectorial Martingale Optimal Transport (VMOT) ‣ 2 Problem Formulation ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) is a maximization problem, the dual problem becomes inf(ϕ,h)∈Ψμ​(ϕ)\inf\_{(\phi,h)\in\Psi}\mu(\phi), with the inequality reversed (and ϕt,i\phi\_{t,i} taking on their values in ℝ∪{+∞}{\mathbb{R}}\cup\{+\infty\}).

Having established the market framework, the VMOT formulation, and its dual interpretation, we now turn to our main theoretical results concerning duality and dual attainment, which form the foundation for robust pricing and hedging in multi-asset, multi-period markets.

## 3 Main Theoretical Results

In this section, we present the central theoretical contributions of the paper. We first recall the duality result for the vectorial martingale optimal transport (VMOT) problem, then discuss the challenges surrounding dual attainment and state our main theorem, and finally give an intuitive explanation of the proof strategy, emphasizing the role of irreducibility and local L1L^{1} bounds.

### 3.1 Duality in Martingale Optimal Transport

Under mild assumptions on the cost function cc and the marginal distributions, the primal and dual optimal values coincide (see, e.g., [[13](https://arxiv.org/html/2602.02996v1#bib.bib13), [35](https://arxiv.org/html/2602.02996v1#bib.bib35)]):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P​(c)\displaystyle P(c) | :=infπ∈VMT​(μ)𝔼π​[c​(X)]\displaystyle:=\inf\_{\pi\in\mathrm{VMT}(\mu)}\mathbb{E}\_{\pi}[c(X)] |  | (3.1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =sup(ϕ,h)∈Ψμ(ϕ)=:D(c).\displaystyle=\sup\_{(\phi,h)\in\Psi}\mu(\phi)=:D(c). |  |

Furthermore, the primal problem is known to admit a minimizer; that is, there exists a martingale transport plan π∈VMT​(μ)\pi\in\mathrm{VMT}(\mu) such that 𝔼π​[c​(X)]=P​(c)\mathbb{E}\_{\pi}[c(X)]=P(c). Such martingale transports represent extremal market models for asset price evolution, optimizing the expected payoff of the derivative cc.

### 3.2 Dual Attainment: Existence and Challenges

In contrast to the primal problem, whose solvability follows from standard compactness arguments under mild regularity conditions on cc, proving *dual attainment*—existence of an optimal dual pair (ϕ,h)(\phi,h)—is considerably more delicate. This difficulty already appears in classical optimal transport, as exemplified by Brenier’s work [[7](https://arxiv.org/html/2602.02996v1#bib.bib7)]. In the martingale setting, the additional martingale constraint significantly complicates matters. As shown in [[3](https://arxiv.org/html/2602.02996v1#bib.bib3), [4](https://arxiv.org/html/2602.02996v1#bib.bib4), [5](https://arxiv.org/html/2602.02996v1#bib.bib5)], even in the single-asset, two-period case (d,N)=(1,2)(d,N)=(1,2), dual attainment may fail within the natural class Ψ\Psi, and positive results typically rely on careful analysis of limiting convex potentials.

This issue is not merely technical. In financial terms, dual optimizers correspond to optimal sub-/super-hedging strategies and encode important structural information about primal solutions, i.e., extremal market models. For this reason, the dual attainment problem has attracted substantial attention, though most of the literature focuses on the single-asset, two-period framework. Notable exceptions include [[10](https://arxiv.org/html/2602.02996v1#bib.bib10), [28](https://arxiv.org/html/2602.02996v1#bib.bib28), [30](https://arxiv.org/html/2602.02996v1#bib.bib30)], which treat multi-period single-asset settings, and [[23](https://arxiv.org/html/2602.02996v1#bib.bib23), [24](https://arxiv.org/html/2602.02996v1#bib.bib24), [26](https://arxiv.org/html/2602.02996v1#bib.bib26), [15](https://arxiv.org/html/2602.02996v1#bib.bib15), [21](https://arxiv.org/html/2602.02996v1#bib.bib21), [29](https://arxiv.org/html/2602.02996v1#bib.bib29)], which study vector-valued martingale transports mostly in two-period models.

### 3.3 Main Result: Dual Attainment for Multi-Asset, Multi-Period MOT

Our main theoretical result establishes dual attainment for the martingale optimal transport problem with an arbitrary number of time steps NN and assets dd. This extension is particularly relevant for financial applications in which derivative payoffs depend on the full price path of multiple underlyings.

###### Theorem 3.1.

Let (μt,i)t∈[N](\mu\_{t,i})\_{t\in[N]} be an irreducible sequence of marginal distributions on ℝ\mathbb{R} for each i∈[d]i\in[d]. Suppose c:ℝN​d→ℝc:{\mathbb{R}}^{Nd}\to{\mathbb{R}} is a lower semicontinuous cost function such that

|  |  |  |
| --- | --- | --- |
|  | |c​(x)|≤∑t=1N∑i=1dvt,i​(xt,i)|c(x)|\;\leq\;\sum\_{t=1}^{N}\sum\_{i=1}^{d}v\_{t,i}(x\_{t,i}) |  |

for some continuous functions vt,i∈L1​(μt,i)v\_{t,i}\in L^{1}(\mu\_{t,i}). Then there exists a dual optimizer, that is, a family of functions

|  |  |  |
| --- | --- | --- |
|  | (ϕ,h)=(ϕt,i,ht,i)t∈[N],i∈[d](\phi,h)=(\phi\_{t,i},h\_{t,i})\_{t\in[N],\,i\in[d]} |  |

satisfying the pathwise inequality ([2.4](https://arxiv.org/html/2602.02996v1#S2.E4 "Equation 2.4 ‣ 2.3 Dual Problem and Financial Interpretation ‣ 2 Problem Formulation ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), and such that, for every primal optimizer π∈VMT​(μ)\pi\in\mathrm{VMT}(\mu) solving ([2.2](https://arxiv.org/html/2602.02996v1#S2.E2 "Equation 2.2 ‣ 2.2 Vectorial Martingale Optimal Transport (VMOT) ‣ 2 Problem Formulation ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), we have the pathwise equality

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑t=1N∑i=1dϕt,i​(xt,i)+ht,i​(x1,…,xt)​(xt+1,i−xt,i)=c​(x)π-a.s.\displaystyle\sum\_{t=1}^{N}\sum\_{i=1}^{d}\phi\_{t,i}(x\_{t,i})+h\_{t,i}(x\_{1},\dots,x\_{t})\,(x\_{t+1,i}-x\_{t,i})=c(x)\quad\text{$\pi$-a.s.} |  | (3.2) |

The dual optimizer need not belong to the class Ψ\Psi.

The pair (ϕ,h)(\phi,h) in Theorem [3.1](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Main Result: Dual Attainment for Multi-Asset, Multi-Period MOT ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") is often called a *dual maximizer*, as it solves the dual problem ([2.3](https://arxiv.org/html/2602.02996v1#S2.E3 "Equation 2.3 ‣ 2.3 Dual Problem and Financial Interpretation ‣ 2 Problem Formulation ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) associated with the primal minimization problem ([2.2](https://arxiv.org/html/2602.02996v1#S2.E2 "Equation 2.2 ‣ 2.2 Vectorial Martingale Optimal Transport (VMOT) ‣ 2 Problem Formulation ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")). The identity ([3.2](https://arxiv.org/html/2602.02996v1#S3.E2 "Equation 3.2 ‣ Theorem 3.1. ‣ 3.3 Main Result: Dual Attainment for Multi-Asset, Multi-Period MOT ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) shows that the semi-static portfolio built from (ϕ,h)(\phi,h) *replicates* the derivative cc: for any primal minimizer π\pi, the portfolio payoff agrees with c​(X)c(X) for π\pi-almost every price path. The inequality ([2.4](https://arxiv.org/html/2602.02996v1#S2.E4 "Equation 2.4 ‣ 2.3 Dual Problem and Financial Interpretation ‣ 2 Problem Formulation ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) ensures that, away from primal minimizers, the same portfolio provides a pathwise subhedge of cc. By symmetry, Theorem [3.1](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Main Result: Dual Attainment for Multi-Asset, Multi-Period MOT ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") also yields the existence of a dual *minimizer* for the maximization problem in ([2.2](https://arxiv.org/html/2602.02996v1#S2.E2 "Equation 2.2 ‣ 2.2 Vectorial Martingale Optimal Transport (VMOT) ‣ 2 Problem Formulation ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) when cc is upper semicontinuous; in that case, the resulting portfolio superhedges the payoff and replicates cc along primal maximizers.

It is crucial to note that a dual optimizer is not guaranteed to lie in Ψ\Psi. Previous work has shown that the dual problem ([2.3](https://arxiv.org/html/2602.02996v1#S2.E3 "Equation 2.3 ‣ 2.3 Dual Problem and Financial Interpretation ‣ 2 Problem Formulation ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) is in general not attained within Ψ\Psi, even for (d,N)=(1,2)(d,N)=(1,2) (see [[3](https://arxiv.org/html/2602.02996v1#bib.bib3), [5](https://arxiv.org/html/2602.02996v1#bib.bib5)]), unless cc satisfies additional regularity assumptions [[4](https://arxiv.org/html/2602.02996v1#bib.bib4)]. While Ψ\Psi is a natural domain for formulating the dual problem, it is relatively “narrow” due to the lack of compactness in infinite dimensions. Proving dual attainment is therefore substantially harder than proving duality ([3.1](https://arxiv.org/html/2602.02996v1#S3.E1 "Equation 3.1 ‣ 3.1 Duality in Martingale Optimal Transport ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), which often follows from standard tools in functional analysis and convex duality. In particular, although the dual optimizer (ϕ,h)(\phi,h) in Theorem [3.1](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Main Result: Dual Attainment for Multi-Asset, Multi-Period MOT ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") may lie outside Ψ\Psi, each component ϕt,i\phi\_{t,i} is real-valued μt,i\mu\_{t,i}-a.s., and each ht,ih\_{t,i} is real-valued as well. Since the marginals (μt,i)t,i(\mu\_{t,i})\_{t,i} are fixed in the VMOT problem, all functions appearing in the theorem can be regarded as essentially real-valued measurable functions, with no further regularity imposed.

### 3.4 Intuitive Explanation and Approximating Dual Maximizers

Upgrading the duality relation ([3.1](https://arxiv.org/html/2602.02996v1#S3.E1 "Equation 3.1 ‣ 3.1 Duality in Martingale Optimal Transport ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) to full dual attainment requires a refined approximation argument. The key idea, originating in [[3](https://arxiv.org/html/2602.02996v1#bib.bib3), [5](https://arxiv.org/html/2602.02996v1#bib.bib5)] for the single-asset, two-period case, is to construct a sequence of “nice” dual candidates and then extract a pointwise limit using local compactness and irreducibility.

We call a sequence (ϕn,hn)n∈ℕ(\phi\_{n},h\_{n})\_{n\in\mathbb{N}} an *approximating dual maximizer* if, for each nn:

* •

  ϕt,i,n\phi\_{t,i,n} is real-valued, continuous, and integrable with respect to μt,i\mu\_{t,i}, i.e., ϕt,i,n∈L1​(μt,i)\phi\_{t,i,n}\in L^{1}(\mu\_{t,i});
* •

  ht,i,nh\_{t,i,n} is bounded and continuous (with the convention hN,i,n≡0h\_{N,i,n}\equiv 0);
* •

  the following pathwise inequality holds:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∑t=1N∑i=1dϕt,i,n​(xt,i)+ht,i,n​(x¯t)​Δ​xt,i≤c​(x)for all ​x∈ℝN​d,\displaystyle\sum\_{t=1}^{N}\sum\_{i=1}^{d}\phi\_{t,i,n}(x\_{t,i})+h\_{t,i,n}(\bar{x}\_{t})\,\Delta x\_{t,i}\;\leq\;c(x)\quad\text{for all }x\in{\mathbb{R}}^{Nd}, |  | (3.3) |

  where x¯t:=(x1,…,xt)∈ℝd​t\bar{x}\_{t}:=(x\_{1},\dots,x\_{t})\in{\mathbb{R}}^{dt} and Δ​xt,i:=xt+1,i−xt,i\Delta x\_{t,i}:=x\_{t+1,i}-x\_{t,i};
* •

  and the dual values converge increasingly to D​(c)D(c):

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | μ​(ϕn):=∑t=1N∑i=1d∫ϕt,i,n​(xt,i)​𝑑μt,i​(xt,i)↗D​(c)as ​n→∞.\displaystyle\mu(\phi\_{n}):=\sum\_{t=1}^{N}\sum\_{i=1}^{d}\int\phi\_{t,i,n}(x\_{t,i})\,d\mu\_{t,i}(x\_{t,i})\nearrow D(c)\quad\text{as }n\to\infty. |  | (3.4) |

Adapting the strategy of [[3](https://arxiv.org/html/2602.02996v1#bib.bib3), [5](https://arxiv.org/html/2602.02996v1#bib.bib5)] to the multi-asset, multi-period setting, the next proposition provides pointwise convergence of a subsequence of (ϕn,hn)(\phi\_{n},h\_{n}), which is a crucial step toward Theorem [3.1](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Main Result: Dual Attainment for Multi-Asset, Multi-Period MOT ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation").

###### Proposition 3.2.

Under the assumptions of Theorem [3.1](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Main Result: Dual Attainment for Multi-Asset, Multi-Period MOT ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation"), there exists an approximating dual maximizer (ϕn,hn)n∈ℕ(\phi\_{n},h\_{n})\_{n\in\mathbb{N}} such that, for each t∈[N]t\in[N] and i∈[d]i\in[d], the sequence ϕt,i,n\phi\_{t,i,n} converges μt,i\mu\_{t,i}-a.s. to a real-valued function ϕt,i\phi\_{t,i} as n→∞n\to\infty.

The proof of Proposition [3.2](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") relies on a structural property of the marginals, namely irreducibility in convex order, together with a local L1L^{1} bound. We briefly recall the relevant notion (see [[5](https://arxiv.org/html/2602.02996v1#bib.bib5)] for details). A pair of probability measures μ⪯cν\mu\preceq\_{c}\nu (with finite first moments) on ℝ{\mathbb{R}} is called *irreducible* if the open set

|  |  |  |
| --- | --- | --- |
|  | I:={x∈ℝ:uμ​(x)<uν​(x)}I:=\{x\in{\mathbb{R}}:u\_{\mu}(x)<u\_{\nu}(x)\} |  |

is a connected interval and μ​(I)=μ​(ℝ)\mu(I)=\mu({\mathbb{R}}), where

|  |  |  |
| --- | --- | --- |
|  | uμ​(x):=∫ℝ|x−y|​𝑑μ​(y)u\_{\mu}(x):=\int\_{\mathbb{R}}|x-y|\,d\mu(y) |  |

is the potential function of μ\mu. In this case, we define the *domain* (I,J)(I,J) of (μ,ν)(\mu,\nu) by letting JJ be the smallest interval with ν​(J)=ν​(ℝ)\nu(J)=\nu({\mathbb{R}}). Then JJ is the union of II and any endpoints of II that are atoms of ν\nu, and one has I=int​(J)I=\mathrm{int}(J). The interval JJ may be bounded or unbounded, and may take the form (a,b](a,b], [a,b)[a,b), (a,b)(a,b), or [a,b][a,b], with I=(a,b)I=(a,b) in all cases. Intuitively, irreducibility expresses that ν\nu is “spread out” from μ\mu in a regular way. It is a natural and generic property: most pairs of distributions in convex order satisfy irreducibility, and pairs that do not can typically be perturbed slightly to obtain it.

Let (It,i,Jt,i)(I\_{t,i},J\_{t,i}) denote the domain of the irreducible pair μt,i⪯cμt+1,i\mu\_{t,i}\preceq\_{c}\mu\_{t+1,i} for t∈[N−1]t\in[N-1], with the conventions J0,i:=J1,iJ\_{0,i}:=J\_{1,i} and IN,i:=JN−1,iI\_{N,i}:=J\_{N-1,i}. We have Jt,i⊂It+1,iJ\_{t,i}\subset I\_{t+1,i} for all t∈[N−1]t\in[N-1] and i∈[d]i\in[d]. The next lemma provides a local L1L^{1} bound on the approximating potentials.

###### Lemma 3.3.

Under the assumptions of Theorem [3.1](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Main Result: Dual Attainment for Multi-Asset, Multi-Period MOT ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation"), there exists an approximating dual maximizer (ϕn,hn)n∈ℕ(\phi\_{n},h\_{n})\_{n\in\mathbb{N}}. Moreover, for each t∈[N−1]t\in[N-1] and i∈[d]i\in[d], there exists an increasing sequence of compact intervals (Jt,i,k)k∈ℕ(J\_{t,i,k})\_{k\in\mathbb{N}} such that ⋃k∈ℕJt,i,k=Jt,i\bigcup\_{k\in\mathbb{N}}J\_{t,i,k}=J\_{t,i} and

|  |  |  |  |
| --- | --- | --- | --- |
|  | supn‖ϕt,i,n−∫ϕt,i,n​𝑑μt,i,k‖L1​(μt,i,k)≤Ck,\displaystyle\sup\_{n}\left\|\phi\_{t,i,n}-\int\phi\_{t,i,n}\,d\mu\_{t,i,k}\right\|\_{L^{1}(\mu\_{t,i,k})}\;\leq\;C\_{k}, |  | (3.5) |

where μt,i,k:=1μt,i​(Jt−1,i,k)​μt,i|Jt−1,i,k\mu\_{t,i,k}:=\frac{1}{\mu\_{t,i}(J\_{t-1,i,k})}\,\mu\_{t,i}\big|\_{J\_{t-1,i,k}} is the normalized restriction of μt,i\mu\_{t,i} to Jt−1,i,kJ\_{t-1,i,k}, and CkC\_{k} depends only on kk (not on nn).

The local L1L^{1} bound in Lemma [3.3](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") is a key ingredient for extracting pointwise convergent subsequences and thus for proving Proposition [3.2](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") and Theorem [3.1](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Main Result: Dual Attainment for Multi-Asset, Multi-Period MOT ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation"). Beyond its technical role, it is also of independent interest in the analysis of martingale optimal transport with general cost functions. Detailed proofs of Proposition [3.2](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") and Lemma [3.3](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") are given in Section [7](https://arxiv.org/html/2602.02996v1#S7 "7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation").

These duality and dual attainment results establish a rigorous foundation for robust pricing and hedging in multi-asset, multi-period markets. In the following sections, we show how they translate into practical tools for model calibration, risk management, and the pricing of complex path-dependent derivatives.

## 4 Numerical Methods and Implementation

As discussed in [Section 1.2](https://arxiv.org/html/2602.02996v1#S1.SS2 "1.2 Applications in Quantitative Finance ‣ 1 Introduction ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation"), the martingale optimal transport (MOT) framework has emerged as a powerful tool in quantitative finance, enabling both model calibration to observed market marginals and robust pricing and hedging of complex, multi-asset derivatives.
In particular, MOT offers a non-parametric, model-independent methodology that naturally accommodates path-dependence and requires only minimal assumptions on asset dynamics. Moreover, it allows practitioners to incorporate additional market information—such as intermediate marginals or correlation-sensitive products—to further tighten price bounds.
These theoretical advances, particularly in the multi-marginal and multi-asset setting, underscore the importance of scalable and accurate numerical methods. Motivated by these applications, we now turn to the numerical implementation that make the solution of high-dimensional MOT problems feasible in practice.

In this section, we detail the computational strategies employed to solve the multi-marginal MOT problem, emphasizing the challenges posed by high-dimensionality and path-dependent constraints. We introduce the primal-dual linear programming (PDLP) approach, describe its algorithmic enhancements, and present the discrete formulation of the MOT problem suitable for large-scale numerical resolution.

### 4.1 Computational Challenges

The numerical resolution of the martingale optimal transport (MOT) problem has garnered considerable attention in recent literature.
In the multi-marginal case, the direct solution of the underlying linear programming (LP) formulation of MOT suffers from the curse of dimensionality, as the computational complexity grows exponentially with the number of time periods and the number of dimensions of the process.

Conventional methods for solving MOT include entropy-regularized approaches, most notably the Sinkhorn algorithm, and neural network (NN) based methods. The Sinkhorn algorithm has been successfully applied to the primal formulation of optimal transport problems by exploiting Bregman projections to solve the regularized linear program [[11](https://arxiv.org/html/2602.02996v1#bib.bib11)].
De March [[12](https://arxiv.org/html/2602.02996v1#bib.bib12)] proposes a modified Sinkhorn algorithm for bimarginal MOT, which replaces the standard Bregman projections with an approximate projection procedure that iteratively enforces the martingale constraints through a fixed-point update mechanism, thereby achieving adequate accuracy while mitigating the numerical instabilities inherent in the exact projection computations.
However, significant challenges arise when extending this approach to the multi-marginal MOT framework.
Moreover, the Bregman projections essential to the Sinkhorn algorithm are problematic to compute under the martingale constraints; indeed, even in the bimarginal case, these projections are solved only approximately, which compromises accuracy. Additionally, the iterative nature of Sinkhorn renders it susceptible to significant numerical instability when handling the intricate constraints imposed by the martingale requirement.

Neural network methods, which have been developed to tackle the dual formulation of the MOT problem [[14](https://arxiv.org/html/2602.02996v1#bib.bib14)], offer a flexible approach to handle high-dimensional data. However, these methods currently do not offer theoretical guarantees regarding convergence or precision, which limits their reliability in scenarios where rigorous accuracy is paramount.

Given these challenges, there is a need for scalable, robust algorithms that can efficiently handle the high-dimensional, sparse and path-dependent structure of multi-marginal MOT problems.

### 4.2 PDLP Algorithm and Enhancements

To address these computational challenges, we employ the primal-dual linear programming (PDLP) framework [[1](https://arxiv.org/html/2602.02996v1#bib.bib1), [18](https://arxiv.org/html/2602.02996v1#bib.bib18)], which is well-suited for large-scale linear programs.
PDLP is a first-order method that combines a saddle-point reformulation of the LP with adaptive algorithmic enhancements.
It reformulates the standard LP as a saddle-point problem and iteratively updates primal and dual variables using matrix-vector products, avoiding explicit matrix storage and factorization.
Its inherent matrix-free nature and reliance solely on matrix-vector products make PDLP particularly well-suited to the high-dimensional and sparse settings often encountered in MOT problems.

In brief, PDLP begins by rewriting the standard LP formulation

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | minx∈ℝn\displaystyle\min\_{x\in\mathbb{R}^{n}} | c⊤​x,\displaystyle c^{\top}x, |  | (4.1) |
|  | s.t. | A​x=b,x≥0,\displaystyle Ax=b,\quad x\geq 0, |  |

into an equivalent saddle-point (or primal-dual) problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minx∈X⁡maxy∈Y⁡L​(x,y)withL​(x,y)=c⊤​x−y⊤​A​x+b⊤​y,\min\_{x\in X}\max\_{y\in Y}\;L(x,y)\quad\text{with}\quad L(x,y)=c^{\top}x-y^{\top}Ax+b^{\top}y, |  | (4.2) |

where X=ℝ≥0nX=\mathbb{R}\_{\geq 0}^{n} and Y=ℝmY=\mathbb{R}^{m}.
The *primal-dual hybrid gradient* (PDHG) scheme [[8](https://arxiv.org/html/2602.02996v1#bib.bib8)] is then applied by iteratively performing the updates

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | xk+1\displaystyle x\_{k+1} | =projX⁡(xk−τ​(c−A⊤​yk)),\displaystyle=\operatorname{proj}\_{X}\left(x\_{k}-\tau\left(c-A^{\top}y\_{k}\right)\right), |  | (4.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | yk+1\displaystyle y\_{k+1} | =yk+σ​(b−A​(2​xk+1−xk)),\displaystyle=y\_{k}+\sigma\left(b-A\left(2x\_{k+1}-x\_{k}\right)\right), |  | (4.4) |

where τ\tau and σ\sigma denote the primal and dual step sizes, respectively.

PDLP enhances the baseline PDHG method by incorporating several key features:

* •

  Adaptive Step Size. An adaptive heuristic adjusts the step size dynamically to guarantee that the step condition

  |  |  |  |
  | --- | --- | --- |
  |  | τ,σ≤‖zk+1−zk‖ω22​(yk+1−yk)⊤​A​(xk+1−xk)\tau,\sigma\leq\frac{\|z\_{k+1}-z\_{k}\|\_{\omega}^{2}}{2\,(y\_{k+1}-y\_{k})^{\top}A(x\_{k+1}-x\_{k})} |  |

  is satisfied. This avoids overly conservative fixed-step estimates (e.g., τ=σ=1/‖A‖2\tau=\sigma=1/\|A\|^{2}) and accelerates convergence.
* •

  Adaptive Restarts. Periodic restarts based on the normalized duality gap (which remains finite even when the standard duality gap is unbounded) ensure that progress is regularly “reset” to counteract self-inhibiting tailing-off, thereby leading to empirical linear convergence.
* •

  Primal Weight Updates. During restarts, a weight parameter is updated to balance the progress in the primal and dual variables. In effect, the update aims to equalize the weighted distances to optimality in both spaces.
* •

  Presolving and Diagonal Preconditioning. Prior to the main iterations, problem data are simplified using presolve routines and then rescaled via a diagonal preconditioner. Such scaling helps to alleviate numerical imbalances, thereby reducing the effective condition number of the data matrix.

From a computational complexity perspective, recent analyses have established rigorous bounds for the PDLP algorithm in both special and general cases. While PDLP achieves particularly strong complexity guarantees for totally unimodular constraint matrices [[18](https://arxiv.org/html/2602.02996v1#bib.bib18)], it is important to note that total unimodularity of the constraint matrix AA is a property specific to the classical bimarginal optimal transport (OT) problem. In contrast, the constraint matrices encountered in multimarginal OT and in bi- and multi-marginal martingale optimal transport (MOT) problems generally lack total unimodularity due to the more complex structure of the marginal and martingale constraints.

For general linear programs, PDLP requires at most
O​(L2​R2ϵ2)O\left(\frac{L^{2}R^{2}}{\epsilon^{2}}\right)
matrix-vector multiplications to reach an ϵ\epsilon-optimal solution [[1](https://arxiv.org/html/2602.02996v1#bib.bib1)], where LL is a Lipschitz constant related to the problem data, RR is a bound on the feasible region, and ϵ\epsilon is the desired accuracy. Although this worst-case bound is less favorable than in the unimodular case, PDLP remains highly effective in practice for large, sparse, and structured problems such as those encountered in multi-marginal MOT. Its matrix-free implementation and scalability make it a robust choice for high-dimensional optimal transport computations.

This general complexity result underscores the practical viability of PDLP for MOT applications, even when the underlying linear program does not possess special structure. The algorithm’s ability to exploit sparsity and avoid explicit matrix factorizations is particularly advantageous in the high-dimensional, path-dependent setting of multi-marginal MOT.

### 4.3 Discrete Multimarginal MOT Formulation

For numerical implementation, we discretize the multi-marginal MOT problem over a finite grid of asset prices and time steps.
Specifically, we consider a MOT problem that spans multiple assets and time steps, defined over a discrete support.
The discrete formulation is given by the following linear program:

###### Problem 4.1 (discrete multimarginal MOT).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | minπ≥0\displaystyle\min\_{\pi\geq 0} | ⟨C,π⟩\displaystyle\langle C,\pi\rangle |  | (multiMOT) |
|  | subject to | proj(t,k)⁡(π)=μt,k,∀t∈[T],k∈[d],\displaystyle\operatorname{proj}\_{(t,k)}\left(\pi\right)=\mu\_{t,k},\quad\forall t\in[T],\ k\in[d], |  |
|  |  | 𝔼π​[st+1,k−st,k∣ℱt]=0,∀t∈[T−1],k∈[d],\displaystyle\mathbb{E}\_{\pi}\left[s\_{t+1,k}-s\_{t,k}\mid\mathcal{F}\_{t}\right]=0,\quad\forall t\in[T-1],\ k\in[d], |  |

where C=[Ci1,1,…​iT,d]i1,1∈[n1,1],…,iT,d∈[nT,d]C=[C\_{i\_{1,1},\dots i\_{T,d}}]\_{i\_{1,1}\in[n\_{1,1}],\dots,i\_{T,d}\in[n\_{T,d}]} denotes the non-negative cost tensor with rank m=T​dm=Td, μt,k=[μt,k,i]i∈[nt,k]\mu\_{t,k}=[\mu\_{t,k,i}]\_{i\in[n\_{t,k}]} is the probability vector representing the marginal of the kk-th process at the tt-th time step.

To account for discretization error, we relax the martingale constraints by introducing a tolerance parameter corresponding to the grid size:

###### Problem 4.2 (discrete multimarginal MOT with relaxed martingale constraints).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | minπ≥0\displaystyle\min\_{\pi\geq 0} | ⟨C,π⟩\displaystyle\langle C,\pi\rangle |  | (multiMOTrelaxed) |
|  | subject to | proj(t,k)⁡(π)=μt,k,∀t∈[T],k∈[d],\displaystyle\operatorname{proj}\_{(t,k)}\left(\pi\right)=\mu\_{t,k},\quad\forall t\in[T],\ k\in[d], |  |
|  |  | 𝔼π​[st+1,k−st,k∣ℱt]≤Δt,k2,∀t∈[T−1],k∈[d],\displaystyle\mathbb{E}\_{\pi}\left[s\_{t+1,k}-s\_{t,k}\mid\mathcal{F}\_{t}\right]\leq\frac{\Delta\_{t,k}}{2},\quad\forall t\in[T-1],\ k\in[d], |  |
|  |  | 𝔼π​[st+1,k−st,k∣ℱt]≥−Δt,k2,∀t∈[T−1],k∈[d],\displaystyle\mathbb{E}\_{\pi}\left[s\_{t+1,k}-s\_{t,k}\mid\mathcal{F}\_{t}\right]\geq-\frac{\Delta\_{t,k}}{2},\quad\forall t\in[T-1],\ k\in[d], |  |

where C=[Ci1,1,…​iT,d]i1,1∈[n1,1],…,iT,d∈[nT,d]C=[C\_{i\_{1,1},\dots i\_{T,d}}]\_{i\_{1,1}\in[n\_{1,1}],\dots,i\_{T,d}\in[n\_{T,d}]} denotes the non-negative cost tensor with rank m=T​dm=Td, μt,k=[μt,k,i]i∈[nt,k]\mu\_{t,k}=[\mu\_{t,k,i}]\_{i\in[n\_{t,k}]} is the probability vector representing the marginal of the kk-th process at the tt-th time step.

This discrete formulation enables the use of efficient large-scale linear programming solvers, such as the PDLP implementation in NVIDIA cuOpt, to compute optimal transport plans and corresponding dual certificates under realistic market constraints. Leveraging this computational framework, we now present the results of our numerical experiments, including solution quality metrics, illustrative case studies, and an analysis of both primal and dual solutions.

## 5 Numerical Experiments and Results

In this section, we present the results of our numerical experiments for the MOT problem. We begin by describing the metrics used to evaluate solution quality, detail the construction of marginal data from market information, analyze the computed primal and dual solutions, and provide a case study on a worst-of autocallable option. We conclude with a discussion of the implications and limitations of our findings.

### 5.1 Metrics for solution quality

To rigorously assess the quality and reliability of the computed solutions to the MOT problem, we employ a suite of quantitative metrics that capture both optimality and feasibility aspects. These metrics are designed to provide a comprehensive evaluation of the numerical performance of the PDLP approach under the high-dimensional and path-dependent constraints characteristic of the MOT framework.

The primary metric is the *primal objective value*, which represents the expected cost (or payoff) under the optimal transport plan for the given cost tensor. Complementing this, the *dual objective value* aggregates the contributions from the dual variables associated with the marginal constraints, weighted by the prescribed marginals. The difference between these two values, known as the *duality gap*, serves as a certificate of optimality: a small gap indicates that the computed solution is close to optimal, while a larger gap may signal numerical issues or suboptimal convergence.

Feasibility with respect to the problem constraints is evaluated through measures of *primal infeasibility* and *dual infeasibility*. Primal infeasibility quantifies the deviation of the computed transport plan from the prescribed marginal distributions, while dual infeasibility measures the extent to which the dual variables fail to satisfy the dual constraints imposed by the cost structure and the martingale conditions.

To summarize these deviations, we report the ℓp\ell\_{p}-norms of the infeasibility vectors, including ℓ1\ell\_{1}, ℓ2\ell\_{2}, and ℓ∞\ell\_{\infty} norms. These norms provide insight into the aggregate, average, and worst-case violations, respectively, and are useful for benchmarking solver performance across different problem instances and parameter regimes.

For clarity, the key metrics are:

* •

  Primal objective value (VpV\_{p}): Expected cost or payoff under the optimal transport plan.
* •

  Dual objective value (VdV\_{d}): Aggregate value from dual variables, weighted by the prescribed marginals.
* •

  Duality gap (GG): Difference between primal and dual objective values, indicating solution optimality.
* •

  Primal infeasibility (δp\delta^{p}): Deviation of the computed transport plan from the prescribed marginal distributions.
* •

  Dual infeasibility (δd\delta^{d}): Extent to which dual variables fail to satisfy dual constraints.
* •

  ℓp\ell\_{p}-norms of infeasibility: Aggregate (ℓ1\ell\_{1}), average (ℓ2\ell\_{2}), and worst-case (ℓ∞\ell\_{\infty}) violations of constraints.

Together, these metrics enable a transparent and robust evaluation of both the accuracy and feasibility of the computed solutions, facilitating meaningful comparisons with alternative methods and guiding further algorithmic improvements.

### 5.2 Case study: worst-of autocallable option

To showcase the practical relevance of our approach, we consider a worst-of autocallable option referencing the S&P 500 and NASDAQ 100 indices. Autocallable options are a prominent class of structured products in finance, widely traded in equity-linked markets due to their attractive risk-return profiles and embedded path-dependent features. These instruments offer periodic opportunities for early redemption (autocall), contingent on the performance of one or more underlying assets relative to specified barriers. Their popularity stems from the ability to generate enhanced yields in low-volatility environments, provide partial downside protection, and facilitate tailored risk exposures for both retail and institutional investors. The liquidity and market depth of autocallable products, especially those linked to major equity indices, make them a natural choice for robust pricing and risk management studies. Moreover, the worst-of variant, where the payoff depends on the least-performing asset in a basket, is particularly relevant for risk transfer and capital protection strategies.

###### Definition 5.1 (Multi-Asset Autocall Payoff).

Let 𝐒​(t):=(S1​(t),S2​(t),…,Sd​(t))\bm{S}(t):=(S\_{1}(t),S\_{2}(t),\ldots,S\_{d}(t)) for t∈[0,T]t\in[0,T] denote the vector of stochastic processes representing the prices of dd underlying assets.
Consider a sequence of observation dates 0<t1<t2<⋯<tm=T0<t\_{1}<t\_{2}<\cdots<t\_{m}=T, where barrier and knock-out conditions are evaluated and coupons are accrued.
Let KK be the strike price, BKIB\_{\mathrm{KI}} the knock-in barrier, BKOB\_{\mathrm{KO}} the knock-out barrier, and CjC\_{j} the coupon accrued over [tj−1,tj][t\_{j-1},t\_{j}] for j∈[m]j\in[m] (with t0:=0t\_{0}:=0).

Define the worst-performing asset at time tt as

|  |  |  |
| --- | --- | --- |
|  | X​(t):=mini∈[d]⁡Si​(t).\displaystyle X(t):=\min\_{i\in[d]}S\_{i}(t). |  |

Define the knock-out stopping time as

|  |  |  |
| --- | --- | --- |
|  | τ:=inf{j∈[m]:X​(tj)≥BKO},\displaystyle\tau:=\inf\left\{j\in[m]:X(t\_{j})\geq B\_{\mathrm{KO}}\right\}, |  |

with the convention that inf∅=+∞\inf\varnothing=+\infty.

The payoff at time tkt\_{k} for k∈[m]k\in[m] of a worst-of multi-asset autocall is given by

|  |  |  |
| --- | --- | --- |
|  | fk​(𝑺​(t1),…,𝑺​(tk))={∑j=1τCj,if ​k=τ<m,min⁡{X​(T)−K,0},if ​k=m≤τ​ and ​X​(T)≤BKI,∑j=1mCj,if ​k=m≤τ​ and ​X​(T)>BKI,0,otherwise, i.e., ​k<min⁡{m,τ}.\displaystyle f\_{k}\left(\bm{S}(t\_{1}),\ldots,\bm{S}(t\_{k})\right)=\begin{cases}\sum\_{j=1}^{\tau}C\_{j},&\text{if }k=\tau<m,\\[6.45831pt] \min\{X(T)-K,0\},&\text{if }k=m\leq\tau\text{ and }X(T)\leq B\_{\mathrm{KI}},\\[6.45831pt] \sum\_{j=1}^{m}C\_{j},&\text{if }k=m\leq\tau\text{ and }X(T)>B\_{\mathrm{KI}},\\[6.45831pt] 0,&\text{otherwise, i.e., }k<\min\{m,\tau\}.\end{cases} |  |

In our specific application, we consider a worst-of autocallable structure linked to two major equity indices: the S&P 500 (SPX) and the NASDAQ 100 (NDX), corresponding to d=2d=2 underlying assets. The product features a three-year maturity, with an inception date tinc=−524t\_{\mathrm{inc}}=-\frac{5}{24} years and three annual monitoring dates: t1=tinc+1t\_{1}=t\_{\mathrm{inc}}+1, t2=tinc+2t\_{2}=t\_{\mathrm{inc}}+2, and t3=tinc+3t\_{3}=t\_{\mathrm{inc}}+3 years. The knock-out barrier is set at BKO=120%B\_{\mathrm{KO}}=120\% of the initial level, and the knock-in barrier at BKI=60%B\_{\mathrm{KI}}=60\%. The strike price is K=100%K=100\%. The coupon is a fixed rate, with an annualized rate of 8%8\%, accrued at each period, i.e., Cj=8%×(tj−tj−1)C\_{j}=8\%\times(t\_{j}-t\_{j-1}) for j∈{1,2,3}j\in\{1,2,3\}. We perform present value calculations as of t0=0t\_{0}=0, assuming a constant discount rate of 1%1\%.111In practice, the *inception date* refers to the date when the product is issued and the initial asset levels are fixed, while the *evaluation date* is the date at which the product is being valued or analyzed, typically for risk management or pricing purposes. The separation allows for the modeling of products that have already been running for some time, and for the use of current market data in valuation.

It is important to note that the payoff function described above is defined *per unit notional*. In practical applications, the final payout to the investor is obtained by multiplying the computed payoff by the notional amount of the contract.

At each monitoring date, the reference level is determined by the worst-performing underlying between SPX and NDX. For example, suppose at t1=tinc+1t\_{1}=t\_{\mathrm{inc}}+1 years, SPX is at 125%125\% and NDX is at 130%130\% of their respective initial levels. The worst-performing asset is SPX, which exceeds the 120%120\% knock-out barrier, triggering the autocall feature. The product is then redeemed early, and the holder receives the notional plus the accrued coupon up to that date.

If neither asset breaches the knock-out barrier at any monitoring date, the product continues to maturity. At t3=t1+3t\_{3}=t\_{1}+3 years, if the worst-performing asset is below the knock-in barrier (60%60\%), the holder receives a down-and-in put payoff, min⁡{X​(T)−K,0}\min\{X(T)-K,0\}, reflecting the loss relative to the strike. If the worst-performing asset remains above the knock-in barrier, the holder receives the full coupon accrued over the three years.

This structure provides a realistic and challenging test case for the martingale optimal transport framework, as the payoff is highly path-dependent and sensitive to joint asset dynamics. The dimensionality of the problem is d​m=2×3=6dm=2\times 3=6 for the two assets and three monitoring dates, making it tractable for numerical solution via large-scale linear programming. In the following sections, we present numerical results illustrating dual attainment and optimal transport plans for this worst-of autocallable payoff, computed using PDLP solvers under the prescribed marginal and martingale constraints.

### 5.3 Marginal data construction

To construct the marginal distributions required for the multi-period, multi-asset martingale optimal transport (MOT) problem, we utilize market data in the form of vanilla option prices for the S&P 500 (SPX) and NASDAQ 100 (NDX) indices, evaluated as of December 5, 2025 (t0t\_{0}). These option prices are used to infer the risk-neutral marginal distributions of the underlying asset prices at the three monitoring dates specified in the autocallable payoff definition (see [Definition 5.1](https://arxiv.org/html/2602.02996v1#S5.Thmtheorem1 "Definition 5.1 (Multi-Asset Autocall Payoff). ‣ 5.2 Case study: worst-of autocallable option ‣ 5 Numerical Experiments and Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")).

For each asset and each monitoring date, the marginal distribution is discretized over a support of n=10n=10 points, chosen to adequately capture the range of plausible price scenarios implied by the market. The support points are scaled by the respective spot prices at the evaluation date (t0t\_{0}), ensuring comparability and normalization across assets and time steps.

The construction of these marginals from market data follows a standard procedure in quantitative finance. First, a smooth implied volatility surface is calibrated to the observed vanilla option prices for each asset and maturity. Then, using the Breeden–Litzenberger formula [[6](https://arxiv.org/html/2602.02996v1#bib.bib6)], the risk-neutral probability density function is extracted by taking the second derivative of the call price with respect to strike. The resulting densities are discretized to form the input marginals for the MOT problem.

The resulting discrete marginal distributions for SPX and NDX at all three monitoring dates are visualized in [Figure 1](https://arxiv.org/html/2602.02996v1#S5.F1 "In 5.3 Marginal data construction ‣ 5 Numerical Experiments and Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation"). These marginals serve as input constraints for the MOT problem, enabling robust pricing and hedging of the worst-of autocallable payoff under the prescribed market information.

![Refer to caption](x1.png)


Figure 1: Discrete marginal distributions used as input to the 22-dimensional, 33-time-step MOT problem. Asset prices are scaled by their respective spot prices at t0t\_{0}.

### 5.4 Discussion of results

In our numerical experiments, we employ the PDLP solver implemented within NVIDIA cuOpt [[9](https://arxiv.org/html/2602.02996v1#bib.bib9)], running on GPU hardware, to solve the discrete multi-marginal MOT problems. Leveraging GPU acceleration enables efficient large-scale computation and significantly reduces solution times for high-dimensional instances. The solver is configured with an optimality tolerance of 10−1210^{-12}, ensuring that the primal and dual infeasibilities, as well as the optimality gap, are all maintained below this threshold in both absolute and relative terms. This stringent tolerance guarantees that the computed solutions are not only highly accurate but also robust with respect to the complex constraints inherent in the MOT framework.

![Refer to caption](x2.png)


(a) primal maximization

![Refer to caption](x3.png)


(b) primal minimization

Figure 2: Absolute infeasibility with respect to the marginal constraints in the primal solution of the 22-dimensional, 33-time-step MOT problem. Results are shown for both maximization and minimization directions, computed using the PDLP solver in NVIDIA cuOpt with an optimality tolerance of 10−1210^{-12}. The low levels of infeasibility confirm the solver’s ability to enforce marginal constraints with high precision.



![Refer to caption](x4.png)


(a) primal maximization

![Refer to caption](x5.png)


(b) primal minimization

Figure 3: Absolute infeasibility with respect to the martingale constraints in the primal solution of the 22-dimensional, 33-time-step MOT problem. The PDLP solver in cuOpt maintains infeasibility below the grid discretization error for both optimization directions, demonstrating robust enforcement of path-dependent martingale constraints.

The primal solution, represented by the optimal transport plan π\pi, encodes the joint probability distribution over asset prices and time steps that minimizes (or maximizes) the expected payoff under the specified cost function, subject to the marginal and martingale constraints. [Figures 2](https://arxiv.org/html/2602.02996v1#S5.F2 "In 5.4 Discussion of results ‣ 5 Numerical Experiments and Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") and [3](https://arxiv.org/html/2602.02996v1#S5.F3 "Figure 3 ‣ 5.4 Discussion of results ‣ 5 Numerical Experiments and Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") illustrate the infeasibility of the primal solution with respect to the marginal and martingale constraints, respectively, for both the maximization and minimization problems. The results demonstrate that the PDLP solver achieves high accuracy, with infeasibility levels well within the prescribed tolerances. In particular, the relaxed martingale constraints are satisfied within the grid discretization error, confirming the effectiveness of the presolve and preconditioning steps in the numerical pipeline.

![Refer to caption](x6.png)


(a) primal maximization

![Refer to caption](x7.png)


(b) primal minimization

Figure 4: Absolute infeasibility with respect to the dual constraints in the primal solution of the 22-dimensional, 33-time-step MOT problem. The results highlight the tightness of the dual bounds achieved by the PDLP solver in cuOpt, with infeasibility consistently below the prescribed tolerance.



|  |  |  |  |
| --- | --- | --- | --- |
| Optimization Direction | | Maximization | Minimization |
| Optimal Primal Objective Value | | 0.1878800.187880 | 0.0622080.062208 |
| Optimal Dual Objective Value | | 0.1878800.187880 | 0.0622080.062208 |
| Duality Gap | | −7.7577×10−14-7.7577\times 10^{-14} | −1.1971×10−13-1.1971\times 10^{-13} |
| Primal Infeasibility | ℓ1\ell\_{1} | 4.1653×10−124.1653\times 10^{-12} | 1.3085×10−141.3085\times 10^{-14} |
| ℓ2\ell\_{2} | 1.6503×10−121.6503\times 10^{-12} | 7.0355×10−157.0355\times 10^{-15} |
| ℓ∞\ell\_{\infty} | 1.4217×10−121.4217\times 10^{-12} | 6.8279×10−156.8279\times 10^{-15} |
| Dual Infeasibility | ℓ1\ell\_{1} | 7.0409×10−117.0409\times 10^{-11} | 3.7987×10−83.7987\times 10^{-8} |
| ℓ2\ell\_{2} | 7.7958×10−137.7958\times 10^{-13} | 2.8302×10−102.8302\times 10^{-10} |
| ℓ∞\ell\_{\infty} | 2.0761×10−142.0761\times 10^{-14} | 3.0800×10−123.0800\times 10^{-12} |

Table 1: Summary of numerical results for the 22-dimensional, 33-time-step MOT problem solved using the PDLP solver in NVIDIA cuOpt. The table reports optimal primal and dual objective values, duality gaps, and infeasibility norms for both maximization and minimization. All metrics are on the order of or below 10−810^{-8}, with the majority well below 10−1010^{-10}, confirming the accuracy and robustness of the computed solutions.

The dual solution, comprising the variables ϕ\phi and hh, provides valuable insight into the shadow prices associated with the marginal and martingale constraints. These dual variables can be interpreted as sensitivities of the optimal value to perturbations in the input marginals and the martingale conditions, respectively. [Figure 4](https://arxiv.org/html/2602.02996v1#S5.F4 "In 5.4 Discussion of results ‣ 5 Numerical Experiments and Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") presents the infeasibility of the dual solution, further corroborating the tightness of the computed bounds and the robustness of the solver.

[Table 1](https://arxiv.org/html/2602.02996v1#S5.T1 "In 5.4 Discussion of results ‣ 5 Numerical Experiments and Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") summarizes the key numerical results, including the optimal primal and dual objective values, duality gaps, and infeasibility norms for both maximization and minimization directions. The duality gaps are on the order of 10−1310^{-13} or smaller, demonstrating that the solutions achieve optimality to within nearly machine precision. Primal and dual infeasibility norms are similarly small, reflecting the solver’s ability to enforce the complex constraints of the MOT problem in a high-dimensional, path-dependent setting.

Overall, the computed primal and dual solutions validate the theoretical guarantees of the PDLP approach and demonstrate its practical effectiveness for large-scale, multi-asset, multi-period MOT problems. The use of GPU-accelerated computation via NVIDIA cuOpt was essential for handling the high-dimensional, path-dependent structure of these problems, enabling robust and scalable solution of MOT instances that would be infeasible on standard CPU-based solvers. These results provide a foundation for further applications in robust pricing, risk management, and model calibration in financial engineering and related fields.

## 6 Conclusion and Future Work

In this work, we have developed a comprehensive framework for dual attainment in the multi-marginal, multi-asset martingale optimal transport (MOT) problem. By extending duality and existence results to arbitrary numbers of assets and time periods, we have provided both theoretical and practical foundations for robust pricing and hedging of complex financial derivatives. Our analysis demonstrates that, under mild regularity and irreducibility conditions, dual optimizers exist and can be constructed, enabling the replication and sub-/super-hedging of path-dependent payoffs in multi-dimensional settings.

On the computational side, we have shown that the primal-dual linear programming (PDLP) approach, implemented within NVIDIA cuOpt and executed on GPU hardware, is highly effective for solving large-scale discrete MOT problems. Leveraging GPU acceleration was essential for handling the high-dimensional, path-dependent structure of these problems, enabling solution times and scalability that would be infeasible on standard CPU-based solvers. Our numerical experiments confirm that the PDLP solver achieves near-optimality and enforces intricate marginal and martingale constraints with high precision, even for challenging products such as worst-of autocallable options.

The martingale optimal transport framework thus offers a powerful and flexible tool for quantitative finance, supporting model calibration, robust pricing, and risk management in environments with limited model assumptions and rich market data. The demonstrated effectiveness of GPU-accelerated computation further expands the practical applicability of MOT to real-world, large-scale financial problems.

##### Future work

There remain several promising directions for further research in the study of multi-marginal, multi-asset martingale optimal transport. One avenue is to investigate how additional structural properties of the payoff function may be leveraged to refine theoretical bounds and enhance the robustness of pricing results.
Another important direction is the development of more efficient computational techniques, particularly those that exploit problem-specific features to improve scalability and reduce dimensionality in large-scale numerical implementations. Advancing these aspects could lead to significant improvements in both the theoretical understanding and practical applicability of the MOT framework in high-dimensional financial settings. We leave these and related questions for future work.

## 7 Proofs of Main Results

The assumption |c​(x)|≤∑t,ivt,i​(xt,i)|c(x)|\leq\sum\_{t,i}v\_{t,i}(x\_{t,i}) for some continuous vt,i∈L1​(μt,i)v\_{t,i}\in L^{1}(\mu\_{t,i}) ensures P​(c)=D​(c)P(c)=D(c) in ([3.1](https://arxiv.org/html/2602.02996v1#S3.E1 "Equation 3.1 ‣ 3.1 Duality in Martingale Optimal Transport ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) (see e.g. [[35](https://arxiv.org/html/2602.02996v1#bib.bib35)]). Clearly, a dual optimizer exists for c​(x)c(x) if and only if so does for c~​(x):=c​(x)−∑t,ivt,i\tilde{c}(x):=c(x)-\sum\_{t,i}v\_{t,i}. Thus by replacing cc with c~\tilde{c}, from now on we can (and will) assume that c≤0c\leq 0 throughout the proofs.

###### Proof of Lemma [3.3](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation").

Let (ϕn,hn)n∈ℕ(\phi\_{n},h\_{n})\_{n\in{\mathbb{N}}} be an approximating dual maximizer satisfying ([3.3](https://arxiv.org/html/2602.02996v1#S3.E3 "Equation 3.3 ‣ 3rd item ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), ([3.4](https://arxiv.org/html/2602.02996v1#S3.E4 "Equation 3.4 ‣ 4th item ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), where D​(c)=P​(c)∈ℝD(c)=P(c)\in{\mathbb{R}} and c≤0c\leq 0 without loss of generality. Denote ϕt,n⊕​(xt)=∑i=1dϕt,i,n​(xt,i)\phi\_{t,n}^{\oplus}(x\_{t})=\sum\_{i=1}^{d}\phi\_{t,i,n}(x\_{t,i}), ht,n​(x¯t)=(ht,1,n​(x¯t),…,ht,d,n​(x¯t))h\_{t,n}(\bar{x}\_{t})=\big(h\_{t,1,n}(\bar{x}\_{t}),...,h\_{t,d,n}(\bar{x}\_{t})\big). Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | χt,n​(xt):=supx1,…,xt−1∑s=1t−1(ϕs,n⊕​(xs)+hs,n​(x¯s)⋅Δ​xs)\displaystyle\chi\_{t,n}(x\_{t}):=\sup\_{x\_{1},...,x\_{t-1}}\sum\_{s=1}^{t-1}\big(\phi\_{s,n}^{\oplus}(x\_{s})+h\_{s,n}(\bar{x}\_{s})\cdot\Delta x\_{s}\big) |  | (7.1) |

with the convention χ1,n=χN+1,n≡0\chi\_{1,n}=\chi\_{N+1,n}\equiv 0. Notice χt,n\chi\_{t,n} is a convex function on ℝd{\mathbb{R}}^{d}, since it is a supremum of affine functions of xtx\_{t}. We claim

|  |  |  |  |
| --- | --- | --- | --- |
|  | χt,n≤χt+1,n−ϕt,n⊕​ for all ​t∈[N]​ and ​n∈ℕ.\displaystyle\chi\_{t,n}\leq\chi\_{t+1,n}-\phi\_{t,n}^{\oplus}\ \text{ for all }t\in[N]\text{ and }n\in{\mathbb{N}}. |  | (7.2) |

This inequality can be shown as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | χt+1,n​(xt+1)\displaystyle\chi\_{t+1,n}(x\_{t+1}) | =supx1,…,xt∑s=1t(ϕs,n⊕​(xs)+hs,n​(x¯s)⋅Δ​xs)\displaystyle=\sup\_{x\_{1},...,x\_{t}}\sum\_{s=1}^{t}\big(\phi\_{s,n}^{\oplus}(x\_{s})+h\_{s,n}(\bar{x}\_{s})\cdot\Delta x\_{s}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥supx1,…,xt−1xt=xt+1∑s=1t−1(ϕs,n⊕​(xs)+hs,n​(x¯s)⋅Δ​xs)+ϕt,n⊕​(xt+1)\displaystyle\geq\sup\_{\begin{subarray}{c}x\_{1},...,x\_{t-1}\\ x\_{t}=x\_{t+1}\end{subarray}}\sum\_{s=1}^{t-1}\big(\phi\_{s,n}^{\oplus}(x\_{s})+h\_{s,n}(\bar{x}\_{s})\cdot\Delta x\_{s}\big)+\phi\_{t,n}^{\oplus}(x\_{t+1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =χt,n​(xt+1)+ϕt,n⊕​(xt+1),\displaystyle=\chi\_{t,n}(x\_{t+1})+\phi\_{t,n}^{\oplus}(x\_{t+1}), |  |

while the inequality χN,n≤−ϕN,n⊕\chi\_{N,n}\leq-\phi^{\oplus}\_{N,n} directly follows from c≤0c\leq 0. Let μt⊗=μt,1⊗⋯⊗μt,d\mu^{\otimes}\_{t}=\mu\_{t,1}\otimes\dots\otimes\mu\_{t,d} denote the product measure. We claim the following bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫χt,n​d​(μt⊗−μt−1⊗)≤C​ for all ​t=2,…,N​ and ​n∈ℕ,\displaystyle\int\chi\_{t,n}\,d(\mu\_{t}^{\otimes}-\mu\_{t-1}^{\otimes})\leq C\ \text{ for all }t=2,...,N\text{ and }n\in{\mathbb{N}}, |  | (7.3) |

where CC is independent of nn throughout the proof.

To show ([7.3](https://arxiv.org/html/2602.02996v1#S7.E3 "Equation 7.3 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), observe that repeated application of ([7.2](https://arxiv.org/html/2602.02996v1#S7.E2 "Equation 7.2 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | μt⊗​(χt,n)\displaystyle\mu\_{t}^{\otimes}(\chi\_{t,n}) | ≤μt⊗​(χt+1,n)−μt⊗​(ϕt,n⊕)\displaystyle\leq\mu\_{t}^{\otimes}(\chi\_{t+1,n})-\mu\_{t}^{\otimes}(\phi\_{t,n}^{\oplus}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤μt+1⊗​(χt+1,n)−μt⊗​(ϕt,n⊕)\displaystyle\leq\mu\_{t+1}^{\otimes}(\chi\_{t+1,n})-\mu\_{t}^{\otimes}(\phi\_{t,n}^{\oplus}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤μt+1⊗​(χt+2,n)−μt+1⊗​(ϕt+1,n⊕)−μt⊗​(ϕt,n⊕)\displaystyle\leq\mu\_{t+1}^{\otimes}(\chi\_{t+2,n})-\mu\_{t+1}^{\otimes}(\phi\_{t+1,n}^{\oplus})-\mu\_{t}^{\otimes}(\phi\_{t,n}^{\oplus}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤⋯≤−∑s=tNμs⊗​(ϕs,n⊕),\displaystyle\leq\dots\leq-\sum\_{s=t}^{N}\mu\_{s}^{\otimes}(\phi\_{s,n}^{\oplus}), |  |

where the second inequality is due to μt⊗⪯cμt+1⊗\mu\_{t}^{\otimes}\preceq\_{c}\mu\_{t+1}^{\otimes} and convexity of χ\chi. Similarly,

|  |  |  |  |
| --- | --- | --- | --- |
|  | μt−1⊗​(χt,n)\displaystyle\mu\_{t-1}^{\otimes}(\chi\_{t,n}) | ≥μt−1⊗​(χt−1,n)+μt−1⊗​(ϕt−1,n⊕)\displaystyle\geq\mu\_{t-1}^{\otimes}(\chi\_{t-1,n})+\mu\_{t-1}^{\otimes}(\phi\_{t-1,n}^{\oplus}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥μt−2⊗​(χt−1,n)+μt−1⊗​(ϕt−1,n⊕)\displaystyle\geq\mu\_{t-2}^{\otimes}(\chi\_{t-1,n})+\mu\_{t-1}^{\otimes}(\phi\_{t-1,n}^{\oplus}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥μt−2⊗​(χt−2,n)+μt−2⊗​(ϕt−2,n⊕)+μt−1⊗​(ϕt−1,n⊕)\displaystyle\geq\mu\_{t-2}^{\otimes}(\chi\_{t-2,n})+\mu\_{t-2}^{\otimes}(\phi\_{t-2,n}^{\oplus})+\mu\_{t-1}^{\otimes}(\phi\_{t-1,n}^{\oplus}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥⋯≥∑s=1t−1μs⊗​(ϕs,n⊕).\displaystyle\geq\dots\geq\sum\_{s=1}^{t-1}\mu\_{s}^{\otimes}(\phi\_{s,n}^{\oplus}). |  |

The two inequalities, along with μt−1⊗​(χt,n)≤μt⊗​(χt,n)\mu\_{t-1}^{\otimes}(\chi\_{t,n})\leq\mu\_{t}^{\otimes}(\chi\_{t,n}) due to μt−1⊗⪯cμt⊗\mu\_{t-1}^{\otimes}\preceq\_{c}\mu\_{t}^{\otimes}, imply

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫χt,n​d​(μt⊗−μt−1⊗)≤−∑s=1Nμs⊗​(ϕs,n⊕)=−μ​(ϕn)\displaystyle\int\chi\_{t,n}\,d(\mu\_{t}^{\otimes}-\mu\_{t-1}^{\otimes})\leq-\sum\_{s=1}^{N}\mu\_{s}^{\otimes}(\phi\_{s,n}^{\oplus})=-\mu(\phi\_{n}) |  | (7.4) |

which, in conjunction with ([3.4](https://arxiv.org/html/2602.02996v1#S3.E4 "Equation 3.4 ‣ 4th item ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), yields ([7.3](https://arxiv.org/html/2602.02996v1#S7.E3 "Equation 7.3 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) as claimed.

We can now obtain local uniform boundedness of {χt,n}n\{\chi\_{t,n}\}\_{n} using ([7.3](https://arxiv.org/html/2602.02996v1#S7.E3 "Equation 7.3 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) and [[21](https://arxiv.org/html/2602.02996v1#bib.bib21), Proposition A.1]. We need to meet the proposition’s second condition. For this, fix any a∈I1:=I1,1×⋯×I1,da\in I\_{1}:=I\_{1,1}\times\dots\times I\_{1,d}, and let L2,n:ℝd→ℝL\_{2,n}:{\mathbb{R}}^{d}\to{\mathbb{R}} be an affine function satisfying L2,n≤χ2,nL\_{2,n}\leq\chi\_{2,n} and L2,n​(a)=χ2,n​(a)L\_{2,n}(a)=\chi\_{2,n}(a). By linearity, we have L2,n​(x2)=∇L2,n​(x1)⋅(x2−x1)+L2,n​(x1)L\_{2,n}(x\_{2})=\nabla L\_{2,n}(x\_{1})\cdot(x\_{2}-x\_{1})+L\_{2,n}(x\_{1}). This allows us to modify the given approximating dual maximizer (ϕn,hn)n∈ℕ(\phi\_{n},h\_{n})\_{n\in{\mathbb{N}}} by replacing ϕ1,n⊕​(x1)\phi\_{1,n}^{\oplus}(x\_{1}) with ϕ1,n⊕​(x1)−L2,n​(x1)\phi\_{1,n}^{\oplus}(x\_{1})-L\_{2,n}(x\_{1}), ϕ2,n⊕​(x2)\phi\_{2,n}^{\oplus}(x\_{2}) with ϕ2,n⊕​(x2)+L2,n​(x2)\phi\_{2,n}^{\oplus}(x\_{2})+L\_{2,n}(x\_{2}), and h1,n​(x1)h\_{1,n}(x\_{1}) with h1,n​(x1)−∇L2,n​(x1)h\_{1,n}(x\_{1})-\nabla L\_{2,n}(x\_{1}) (∇L2,n\nabla L\_{2,n} is constant and does not depend on x1x\_{1}). Notice this yields χ2,n≥0\chi\_{2,n}\geq 0 and χ2,n​(a)=0\chi\_{2,n}(a)=0. We can continue subtracting appropriate linear functions Lt,nL\_{t,n}, t=2,…,Nt=2,...,N, and achieve

|  |  |  |  |
| --- | --- | --- | --- |
|  | χt,n≥0​ and ​χt,n​(a)=0for all ​n∈ℕ​ and ​t∈[N].\displaystyle\chi\_{t,n}\geq 0\ \text{ and }\ \chi\_{t,n}(a)=0\quad\text{for all }n\in{\mathbb{N}}\text{ and }t\in[N]. |  | (7.5) |

Note that the modifications have no effect on the value μ​(ϕn)\mu(\phi\_{n}).

Next, let {ϵk}k\{\epsilon\_{k}\}\_{k} be a positive decreasing sequence tending to zero as k→∞k\to\infty, and write It,i=]at,i,bt,i[I\_{t,i}=]a\_{t,i},b\_{t,i}[ where −∞≤at,i<bt,i≤+∞-\infty\leq a\_{t,i}<b\_{t,i}\leq+\infty. Then we define the compact interval Jt,i,k:=[ct,i,k,dt,i,k]J\_{t,i,k}:=[c\_{t,i,k},d\_{t,i,k}] for t∈[N−1]t\in[N-1], i∈[d]i\in[d] and k∈ℕk\in{\mathbb{N}} as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | If ​at,i>−∞, then define ct,i,k by the following rule:\displaystyle\text{If }a\_{t,i}>-\infty,\text{ then define $c\_{t,i,k}$ by the following rule:} |  | (7.6) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | μt+1,i​(at,i)=0⇒ct,i,k:=at,i+ϵk;μt+1,i​(at,i)>0⇒ct,i,k:=at,i;\displaystyle\ \mu\_{t+1,i}(a\_{t,i})=0\Rightarrow c\_{t,i,k}:=a\_{t,i}+\epsilon\_{k};\ \ \mu\_{t+1,i}(a\_{t,i})>0\Rightarrow c\_{t,i,k}:=a\_{t,i}; |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | If ​bt,i<+∞, then define dt,i,k by the following rule:\displaystyle\text{If }b\_{t,i}<+\infty,\text{ then define $d\_{t,i,k}$ by the following rule:} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | μt+1,i​(bt,i)=0⇒dt,i,k:=bt,i−ϵk;μt+1,i​(bt,i)>0⇒dt,i,k:=bt,i;\displaystyle\ \mu\_{t+1,i}(b\_{t,i})=0\Rightarrow d\_{t,i,k}:=b\_{t,i}-\epsilon\_{k};\ \ \mu\_{t+1,i}(b\_{t,i})>0\Rightarrow d\_{t,i,k}:=b\_{t,i}; |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | If ​at,i=−∞, then ​ct,i,k:=−1/ϵk;\displaystyle\text{If }a\_{t,i}=-\infty,\text{ then }c\_{t,i,k}:=-1/\epsilon\_{k}; |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | If ​bt,i=+∞, then ​dt,i,k:=+1/ϵk.\displaystyle\text{If }b\_{t,i}=+\infty,\text{ then }d\_{t,i,k}:=+1/\epsilon\_{k}. |  |

Set J0,i,k:=J1,i,kJ\_{0,i,k}:=J\_{1,i,k}. For example, if μt+1,i​(at,i)=0\mu\_{t+1,i}(a\_{t,i})=0 and μt+1,i​(bt,i)>0\mu\_{t+1,i}(b\_{t,i})>0, then Jt,i,k=[at,i+ϵk,bt,i]J\_{t,i,k}=[a\_{t,i}+\epsilon\_{k},b\_{t,i}]. Let ϵ1\epsilon\_{1} be so small so that μt,i​(Jt,i,1)>0\mu\_{t,i}(J\_{t,i,1})>0, μt+1,i​(Jt,i,1)>0\mu\_{t+1,i}(J\_{t,i,1})>0 for every t,it,i. Observe that Jt,i,k↗Jt,iJ\_{t,i,k}\nearrow J\_{t,i} as k→∞k\to\infty. Let Jt,k:=Jt,1,k×Jt,2,k×…×Jt,d,kJ\_{t,k}:=J\_{t,1,k}\times J\_{t,2,k}\times...\times J\_{t,d,k}. Then [[21](https://arxiv.org/html/2602.02996v1#bib.bib21), Proposition A.1] with ([7.3](https://arxiv.org/html/2602.02996v1#S7.E3 "Equation 7.3 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) and ([7.5](https://arxiv.org/html/2602.02996v1#S7.E5 "Equation 7.5 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) yields that there exists Mk≥0M\_{k}\geq 0 for each k∈ℕk\in{\mathbb{N}} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤supn∈ℕsupxt∈Jt−1,kχt,n​(xt)≤Mk.\displaystyle 0\leq\sup\_{n\in{\mathbb{N}}}\sup\_{x\_{t}\in J\_{t-1,k}}\chi\_{t,n}(x\_{t})\leq M\_{k}. |  | (7.7) |

Next, another repeated application of ([7.2](https://arxiv.org/html/2602.02996v1#S7.E2 "Equation 7.2 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | C\displaystyle C | ≥−∑s=1Nμs⊗​(ϕs,n⊕)\displaystyle\geq-\sum\_{s=1}^{N}\mu\_{s}^{\otimes}(\phi\_{s,n}^{\oplus}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥μN⊗​(χN,n)−∑s=1N−1μs⊗​(ϕs,n⊕)\displaystyle\geq\mu\_{N}^{\otimes}(\chi\_{N,n})-\sum\_{s=1}^{N-1}\mu\_{s}^{\otimes}(\phi\_{s,n}^{\oplus}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥μN−1⊗​(χN,n)−∑s=1N−1μs⊗​(ϕs,n⊕)\displaystyle\geq\mu\_{N-1}^{\otimes}(\chi\_{N,n})-\sum\_{s=1}^{N-1}\mu\_{s}^{\otimes}(\phi\_{s,n}^{\oplus}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =μN−1⊗​(χN,n)−μN−1⊗​(χN−1,n)+μN−1⊗​(χN−1,n)−∑s=1N−1μs⊗​(ϕs,n⊕)\displaystyle=\,\mu\_{N-1}^{\otimes}(\chi\_{N,n})-\mu\_{N-1}^{\otimes}(\chi\_{N-1,n})+\mu\_{N-1}^{\otimes}(\chi\_{N-1,n})-\sum\_{s=1}^{N-1}\mu\_{s}^{\otimes}(\phi\_{s,n}^{\oplus}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =‖χN,n−χN−1,n−ϕN−1,n⊕‖L1​(μN−1⊗)+μN−1⊗​(χN−1,n)−∑s=1N−2μs⊗​(ϕs,n⊕)\displaystyle=\,\parallel\chi\_{N,n}-\chi\_{N-1,n}-\phi\_{N-1,n}^{\oplus}\parallel\_{L^{1}(\mu\_{N-1}^{\otimes})}+\mu\_{N-1}^{\otimes}(\chi\_{N-1,n})-\sum\_{s=1}^{N-2}\mu\_{s}^{\otimes}(\phi\_{s,n}^{\oplus}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥‖χN,n−χN−1,n−ϕN−1,n⊕‖L1​(μN−1⊗)+μN−2⊗​(χN−1,n)−∑s=1N−2μs⊗​(ϕs,n⊕)\displaystyle\geq\,\parallel\chi\_{N,n}-\chi\_{N-1,n}-\phi\_{N-1,n}^{\oplus}\parallel\_{L^{1}(\mu\_{N-1}^{\otimes})}+\mu\_{N-2}^{\otimes}(\chi\_{N-1,n})-\sum\_{s=1}^{N-2}\mu\_{s}^{\otimes}(\phi\_{s,n}^{\oplus}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥⋯≥∑s=2N‖χs,n−χs−1,n−ϕs−1,n⊕‖L1​(μs−1⊗)\displaystyle\geq\dots\geq\sum\_{s=2}^{N}\parallel\chi\_{s,n}-\chi\_{s-1,n}-\phi\_{s-1,n}^{\oplus}\parallel\_{L^{1}(\mu\_{s-1}^{\otimes})} |  |

where the third and sixth inequality is due to the convexity of χ\chi with μt⊗⪯cμt+1⊗\mu\_{t}^{\otimes}\preceq\_{c}\mu\_{t+1}^{\otimes}, and the fifth equality is by the nonnegativity χt,n−χt−1,n−ϕt−1,n⊕≥0\chi\_{t,n}-\chi\_{t-1,n}-\phi\_{t-1,n}^{\oplus}\geq 0 from ([7.2](https://arxiv.org/html/2602.02996v1#S7.E2 "Equation 7.2 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")).

On the other hand, the nonpositivity c≤0c\leq 0 in ([3.3](https://arxiv.org/html/2602.02996v1#S3.E3 "Equation 3.3 ‣ 3rd item ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) yields

|  |  |  |
| --- | --- | --- |
|  | ∑s=1N(ϕs,n⊕​(xs)+hs,n​(x¯s)⋅Δ​xs)≤χN,n​(xN)+ϕN,n⊕​(xN)≤0\displaystyle\sum\_{s=1}^{N}\big(\phi\_{s,n}^{\oplus}(x\_{s})+h\_{s,n}(\bar{x}\_{s})\cdot\Delta x\_{s}\big)\leq\chi\_{N,n}(x\_{N})+\phi^{\oplus}\_{N,n}(x\_{N})\leq 0 |  |

where the first inequality follows by taking supremum over x1,…,xN−1x\_{1},...,x\_{N-1} (recall ([7.1](https://arxiv.org/html/2602.02996v1#S7.E1 "Equation 7.1 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) and the convention hN,n≡0h\_{N,n}\equiv 0). Integrating with any π∈VMT​(μ)\pi\in{\rm VMT}(\mu) yields ‖χN,n​(xN)+ϕN,n⊕‖L1​(μN⊗)≤−∑s=1Nμs⊗​(ϕs,n⊕)≤C\parallel\chi\_{N,n}(x\_{N})+\phi^{\oplus}\_{N,n}\parallel\_{L^{1}(\mu\_{N}^{\otimes})}\leq-\sum\_{s=1}^{N}\mu\_{s}^{\otimes}(\phi\_{s,n}^{\oplus})\leq C. We therefore deduce

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖χt+1,n−χt,n−ϕt,n⊕‖L1​(μt⊗)≤C​ for all ​n∈ℕ,t∈[N].\parallel\chi\_{t+1,n}-\chi\_{t,n}-\phi\_{t,n}^{\oplus}\parallel\_{L^{1}(\mu\_{t}^{\otimes})}\,\leq C\ \text{ for all }n\in{\mathbb{N}},t\in[N]. |  | (7.8) |

Now for each k∈ℕk\in{\mathbb{N}}, let μt,i,k\mu\_{t,i,k} be the restriction of μt,i\mu\_{t,i} on Jt−1,i,kJ\_{t-1,i,k} (where J0,i,k:=J1,i,kJ\_{0,i,k}:=J\_{1,i,k}) then normalized to be a probability distribution, as defined in Lemma [3.3](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation"). Let μt,k⊗=⊗iμt,i,k\mu^{\otimes}\_{t,k}=\otimes\_{i}\mu\_{t,i,k}, so that μt,k⊗​(Jt−1,k)=1\mu^{\otimes}\_{t,k}(J\_{t-1,k})=1 where Jt−1,k:=⊗iJt−1,i,kJ\_{t-1,k}:=\otimes\_{i}J\_{t-1,i,k}. Define

|  |  |  |
| --- | --- | --- |
|  | vt,i,k,n:=∫ϕt,i,n​𝑑μt,i,k,t∈[N],i∈[d],k∈ℕ,n∈ℕ.\displaystyle v\_{t,i,k,n}:=\int\phi\_{t,i,n}\,d\mu\_{t,i,k},\quad t\in[N],i\in[d],k\in{\mathbb{N}},n\in{\mathbb{N}}. |  |

To complete the proof of Lemma [3.3](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation"), that is to show for each k∈ℕk\in{\mathbb{N}}

|  |  |  |  |
| --- | --- | --- | --- |
|  | supn‖ϕt,i,n−vt,i,k,n‖L1​(μt,i,k)≤C,\displaystyle\sup\_{n}\parallel\phi\_{t,i,n}-v\_{t,i,k,n}\parallel\_{L^{1}(\mu\_{t,i,k})}\,\leq C, |  | (7.9) |

observe that ([7.7](https://arxiv.org/html/2602.02996v1#S7.E7 "Equation 7.7 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), ([7.8](https://arxiv.org/html/2602.02996v1#S7.E8 "Equation 7.8 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) and the fact Jt−1,k⊂Jt,kJ\_{t-1,k}\subset J\_{t,k} together imply

|  |  |  |
| --- | --- | --- |
|  | ‖ϕt,n⊕‖L1​(μt,k⊗)\displaystyle\parallel\phi\_{t,n}^{\oplus}\parallel\_{L^{1}(\mu^{\otimes}\_{t,k})} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤‖χt+1,n−χt,n−ϕt,n⊕‖L1​(μt,k⊗)+‖χt,n−χt+1,n‖L1​(μt,k⊗)\displaystyle\leq\,\parallel\chi\_{t+1,n}-\chi\_{t,n}-\phi\_{t,n}^{\oplus}\parallel\_{L^{1}(\mu^{\otimes}\_{t,k})}+\parallel\chi\_{t,n}-\chi\_{t+1,n}\parallel\_{L^{1}(\mu^{\otimes}\_{t,k})} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤C+Mk=:C\displaystyle\leq C+M\_{k}=:C |  |

where we used χt+1,n−χt,n−ϕt,n⊕≥0\chi\_{t+1,n}-\chi\_{t,n}-\phi\_{t,n}^{\oplus}\geq 0 to get the bound ‖χt+1,n−χt,n−ϕt,n⊕‖L1​(μt,k⊗)≤C\parallel\chi\_{t+1,n}-\chi\_{t,n}-\phi\_{t,n}^{\oplus}\parallel\_{L^{1}(\mu^{\otimes}\_{t,k})}\,\leq C from ([7.8](https://arxiv.org/html/2602.02996v1#S7.E8 "Equation 7.8 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")). From this, we obtain the bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∑i=1dvt,i,k,n|≤‖ϕt,n⊕‖L1​(μt,k⊗)≤C​ for all ​n,\displaystyle\bigg|\sum\_{i=1}^{d}v\_{t,i,k,n}\bigg|\leq\,\parallel\phi\_{t,n}^{\oplus}\parallel\_{L^{1}(\mu^{\otimes}\_{t,k})}\,\leq C\,\text{ for all }n, |  | (7.10) |

where the first inequality is by Jensen’s inequality.
Next, because ϕt,n⊕≤Mk\phi\_{t,n}^{\oplus}\leq M\_{k} on Jt,kJ\_{t,k} by ([7.2](https://arxiv.org/html/2602.02996v1#S7.E2 "Equation 7.2 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), ([7.5](https://arxiv.org/html/2602.02996v1#S7.E5 "Equation 7.5 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) and ([7.7](https://arxiv.org/html/2602.02996v1#S7.E7 "Equation 7.7 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), by taking supremum over Jt,kJ\_{t,k}, we have

|  |  |  |
| --- | --- | --- |
|  | ∑i=1dsupxt,i∈Jt,i,kϕt,i,n​(xt,i)≤Mk​ for all ​n.\displaystyle\sum\_{i=1}^{d}\sup\_{x\_{t,i}\in J\_{t,i,k}}\phi\_{t,i,n}(x\_{t,i})\leq M\_{k}\,\text{ for all }n. |  |

In particular, since vt,i,k,n≤supxt,i∈Jt,i,kϕt,i,n​(xt,i)v\_{t,i,k,n}\leq\sup\_{x\_{t,i}\in J\_{t,i,k}}\phi\_{t,i,n}(x\_{t,i}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | supxt,1∈Jt,1,kϕt,1,n​(xt,1)+∑i=2dvt,i,k,n≤Mk.\displaystyle\sup\_{x\_{t,1}\in J\_{t,1,k}}\phi\_{t,1,n}(x\_{t,1})+\sum\_{i=2}^{d}v\_{t,i,k,n}\leq M\_{k}. |  | (7.11) |

Define v^t,1,k,n:=−∑i=2dvt,i,k,n\hat{v}\_{t,1,k,n}:=-\sum\_{i=2}^{d}v\_{t,i,k,n}. Since ϕt,n⊕≤Mk\phi\_{t,n}^{\oplus}\leq M\_{k} on Jt,kJ\_{t,k}, we have

|  |  |  |
| --- | --- | --- |
|  | C≥‖Mk−ϕt,n⊕‖L1​(μt,k⊗)=Mk−∫(ϕt,1,n+∑i=2dvt,i,k,n)​𝑑μt,1,k.\displaystyle C\geq\,\,\parallel M\_{k}-\phi\_{t,n}^{\oplus}\parallel\_{L^{1}(\mu^{\otimes}\_{t,k})}\,=M\_{k}-\int(\phi\_{t,1,n}+\sum\_{i=2}^{d}v\_{t,i,k,n})d\mu\_{t,1,k}. |  |

With ([7.11](https://arxiv.org/html/2602.02996v1#S7.E11 "Equation 7.11 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), this implies that supn‖ϕt,1,n−v^t,1,k,n‖L1​(μt,1,k)\sup\_{n}\parallel\phi\_{t,1,n}-\hat{v}\_{t,1,k,n}\parallel\_{L^{1}(\mu\_{t,1,k})} is bounded, and then by ([7.10](https://arxiv.org/html/2602.02996v1#S7.E10 "Equation 7.10 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), supn‖ϕt,1,n−vt,1,k,n‖L1​(μt,1,k)\sup\_{n}\parallel\phi\_{t,1,n}-v\_{t,1,k,n}\parallel\_{L^{1}(\mu\_{t,1,k})} is bounded. This proves ([7.9](https://arxiv.org/html/2602.02996v1#S7.E9 "Equation 7.9 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")).
∎

We turn to the proof of Proposition [3.2](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation").

###### Proof of Proposition [3.2](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") .

Lemma [3.3](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation") and Komlós lemma (which states that every L1L^{1}-bounded sequence of real functions contains a subsequence such that the arithmetic means of all its subsequences converge almost everywhere) implies that for each k∈ℕk\in{\mathbb{N}}, there exists a subsequence {ϕt,i,k,n}n\{\phi\_{t,i,k,n}\}\_{n} of {ϕt,i,n}n\{\phi\_{t,i,n}\}\_{n} such that

(i) {ϕt,i,k+1,n}n\{\phi\_{t,i,k+1,n}\}\_{n} is a further subsequence of {ϕt,i,k,n}n\{\phi\_{t,i,k,n}\}\_{n}, and

(ii) ϕ~t,i,k,n​(xt,i)−v~t,i,k,n\tilde{\phi}\_{t,i,k,n}(x\_{t,i})-\tilde{v}\_{t,i,k,n} converges μt,i,k\mu\_{t,i,k} - a.s.   as   n→∞n\to\infty,
  
where vt,i,k,n=∫ϕt,i,k,n​𝑑μt,i,kv\_{t,i,k,n}=\int\phi\_{t,i,k,n}\,d\mu\_{t,i,k}, v^t,1,k,n=−∑i=2dvt,i,k,n\hat{v}\_{t,1,k,n}=-\sum\_{i=2}^{d}v\_{t,i,k,n}, v~t,1,k,n=1n​∑m=1nv^t,1,k,m\tilde{v}\_{t,1,k,n}=\frac{1}{n}\sum\_{m=1}^{n}\hat{v}\_{t,1,k,m}, v~t,i,k,n=1n​∑m=1nvt,i,k,m\tilde{v}\_{t,i,k,n}=\frac{1}{n}\sum\_{m=1}^{n}v\_{t,i,k,m} for i≥2i\geq 2, and ϕ~t,i,k,n=1n​∑m=1nϕt,i,k,m\tilde{\phi}\_{t,i,k,n}=\frac{1}{n}\sum\_{m=1}^{n}\phi\_{t,i,k,m}. Note that for each kk, our choice of a subsequence index can be made identical for every t,it,i, since there are finitely many indices of t,it,i. Then we select the diagonal sequence

|  |  |  |
| --- | --- | --- |
|  | Φt,i,n:=ϕt,i,n,n\Phi\_{t,i,n}:=\phi\_{t,i,n,n} |  |

and again define

|  |  |  |  |
| --- | --- | --- | --- |
|  | wt,i,k,n\displaystyle w\_{t,i,k,n} | =∫Φt,i,n​𝑑μt,i,k,w~t,i,k,n=1n​∑m=1nwt,i,k,m,2≤i≤d,\displaystyle=\int\Phi\_{t,i,n}d\mu\_{t,i,k},\ \ \tilde{w}\_{t,i,k,n}=\frac{1}{n}\sum\_{m=1}^{n}w\_{t,i,k,m},\quad 2\leq i\leq d, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | w^t,1,k,n\displaystyle\hat{w}\_{t,1,k,n} | =−∑i=2dwt,i,k,n,w~t,1,k,n=1n​∑m=1nw^t,1,k,m,Φ~t,i,n​(xt,i)=1n​∑m=1nΦt,i,m​(xt,i).\displaystyle=-\sum\_{i=2}^{d}w\_{t,i,k,n},\ \ \tilde{w}\_{t,1,k,n}=\frac{1}{n}\sum\_{m=1}^{n}\hat{w}\_{t,1,k,m},\ \ \tilde{\Phi}\_{t,i,n}(x\_{t,i})=\frac{1}{n}\sum\_{m=1}^{n}\Phi\_{t,i,m}(x\_{t,i}). |  |

We then claim:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ~t,i,n​(xt,i)−w~t,i,1,n​converges ​μt,i−a.s. for all ​t∈[N],i∈[d].\displaystyle\tilde{\Phi}\_{t,i,n}(x\_{t,i})-\tilde{w}\_{t,i,1,n}\,\text{converges }\,\mu\_{t,i}-a.s.\,\text{ for all }t\in[N],i\in[d]. |  | (7.12) |

Note that the dependence on kk has now been removed. To prove the claim, since {Φt,i,n}n\{\Phi\_{t,i,n}\}\_{n} is a subsequence of {ϕt,i,k,n}n\{\phi\_{t,i,k,n}\}\_{n} for every k∈ℕk\in{\mathbb{N}}, Komlós lemma implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φ~t,i,n​(xt,i)−w~t,i,k,n​converges ​μt,i,k−a.s. for all ​t​ and ​i.\displaystyle\tilde{\Phi}\_{t,i,n}(x\_{t,i})-\tilde{w}\_{t,i,k,n}\ \text{converges }\,\mu\_{t,i,k}-a.s.\,\text{ for all }t\text{ and }i. |  | (7.13) |

In particular, both {Φ~t,i,n​(xt,i)−w~t,i,1,n}n\{\tilde{\Phi}\_{t,i,n}(x\_{t,i})-\tilde{w}\_{t,i,1,n}\}\_{n} and {Φ~t,i,n​(xt,i)−w~t,i,k,n}n\{\tilde{\Phi}\_{t,i,n}(x\_{t,i})-\tilde{w}\_{t,i,k,n}\}\_{n} converge μt,i,1\mu\_{t,i,1}-a.s. as n→∞n\to\infty, so does the difference {w~t,i,1,n−w~t,i,k,n}n\{\tilde{w}\_{t,i,1,n}-\tilde{w}\_{t,i,k,n}\}\_{n} for each kk. Hence ([7.12](https://arxiv.org/html/2602.02996v1#S7.E12 "Equation 7.12 ‣ Proof of Proposition 3.2 . ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) follows from ([7.13](https://arxiv.org/html/2602.02996v1#S7.E13 "Equation 7.13 ‣ Proof of Proposition 3.2 . ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")). The identity ∑i=1dw~t,i,1,n=0\sum\_{i=1}^{d}\tilde{w}\_{t,i,1,n}=0 then allows to replace the approximating dual maximizer (ϕn,hn)n(\phi\_{n},h\_{n})\_{n} by (ψn,h~n)n(\psi\_{n},\tilde{h}\_{n})\_{n}, where ψt,i,n:=Φ~t,i,n​(xt,i)−w~t,i,1,n\psi\_{t,i,n}:=\tilde{\Phi}\_{t,i,n}(x\_{t,i})-\tilde{w}\_{t,i,1,n} and h~t,i,n\tilde{h}\_{t,i,n} is the corresponding Cesàro mean of the subsequence of (ht,i,n)n(h\_{t,i,n})\_{n} chosen consistently with the selection of {Φt,i,n}n\{\Phi\_{t,i,n}\}\_{n} out of {ϕt,i,n}n\{\phi\_{t,i,n}\}\_{n}.
∎

Finally, we turn to the proof of Theorem [3.1](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Main Result: Dual Attainment for Multi-Asset, Multi-Period MOT ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation").

###### Proof of Theorem [3.1](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Main Result: Dual Attainment for Multi-Asset, Multi-Period MOT ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation").

By Proposition [3.2](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation"), we have an approximating dual maximizer (ϕn,hn)n(\phi\_{n},h\_{n})\_{n} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | {ϕt,i,n}n​ converges to a function ​ϕt,i​μt,i−a.s. as ​n→∞​ for each t∈[N] and i∈[d].\{\phi\_{t,i,n}\}\_{n}\text{ converges to a function }\phi\_{t,i}\ \mu\_{t,i}-a.s.\text{ as }n\to\infty\ \text{ for each $t\in[N]$ and $i\in[d]$}. |  | (7.14) |

We shall prove the convergence of the convex functions {χt,n}n\{\chi\_{t,n}\}\_{n} defined in ([7.1](https://arxiv.org/html/2602.02996v1#S7.E1 "Equation 7.1 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")).

In the proof of Lemma [3.3](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation"), we obtained an approximating dual maximizer (say (ϕn0,hn0)n(\phi^{0}\_{n},h^{0}\_{n})\_{n}) such that the associated {χt,n0}n\{\chi^{0}\_{t,n}\}\_{n} satisfied the local bound ([7.7](https://arxiv.org/html/2602.02996v1#S7.E7 "Equation 7.7 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")). As observed in the proof of Proposition [3.2](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation"), the approximating dual maximizer (ϕn,hn)n(\phi\_{n},h\_{n})\_{n} satisfying ([7.14](https://arxiv.org/html/2602.02996v1#S7.E14 "Equation 7.14 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) can be taken as a Cesàro mean of a suitable subsequence of (ϕn0,hn0)n(\phi^{0}\_{n},h^{0}\_{n})\_{n}. This implies the upper bound in ([7.7](https://arxiv.org/html/2602.02996v1#S7.E7 "Equation 7.7 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) continues to hold

|  |  |  |  |
| --- | --- | --- | --- |
|  | supnχt,n≤MkonJt−1,k.\displaystyle\sup\_{n}\chi\_{t,n}\leq M\_{k}\ \ \text{on}\ \ J\_{t-1,k}. |  | (7.15) |

We shall modify (ϕn,hn)n(\phi\_{n},h\_{n})\_{n} so that ([7.5](https://arxiv.org/html/2602.02996v1#S7.E5 "Equation 7.5 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) holds while ([7.15](https://arxiv.org/html/2602.02996v1#S7.E15 "Equation 7.15 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) is retained. Let It:=It,1×⋯×It,dI\_{t}:=I\_{t,1}\times\dots\times I\_{t,d}. Fix any a∈I1a\in I\_{1} and define ϕt⊕:=∑iϕt,i\phi^{\oplus}\_{t}:=\sum\_{i}\phi\_{t,i}. First, ([7.14](https://arxiv.org/html/2602.02996v1#S7.E14 "Equation 7.14 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) implies that there exists at∈Ita\_{t}\in I\_{t} for every t∈[N]t\in[N] such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞ϕt,n⊕​(at)=ϕt⊕​(at)∈ℝ.\lim\_{n\to\infty}\phi\_{t,n}^{\oplus}(a\_{t})=\phi\_{t}^{\oplus}(a\_{t})\in{\mathbb{R}}. |  | (7.16) |

In view of ([7.2](https://arxiv.org/html/2602.02996v1#S7.E2 "Equation 7.2 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) which gives ϕ1,n⊕≤χ2,n\phi^{\oplus}\_{1,n}\leq\chi\_{2,n}, this implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | infnχ2,n​(a1)>−∞.\inf\_{n}\chi\_{2,n}(a\_{1})>-\infty. |  | (7.17) |

On the other hand, since I1=int​(J1)I\_{1}={\rm int}(J\_{1}) and J1,k↗J1J\_{1,k}\nearrow J\_{1} (see ([7.6](https://arxiv.org/html/2602.02996v1#S7.E6 "Equation 7.6 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) for the definition of compact intervals Jt,i,kJ\_{t,i,k}), for large enough kk we have {a,a1}⊂int​(J1,k)\{a,a\_{1}\}\subset{\rm int}(J\_{1,k}). Now ([7.15](https://arxiv.org/html/2602.02996v1#S7.E15 "Equation 7.15 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), ([7.17](https://arxiv.org/html/2602.02996v1#S7.E17 "Equation 7.17 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) imply that both χ2,n​(a)\chi\_{2,n}(a) and ∇χ2,n​(a)\nabla\chi\_{2,n}(a) are uniformly bounded in nn, where ∇χ2,n​(a)∈∂χ2,n​(a)\nabla\chi\_{2,n}(a)\in\partial\chi\_{2,n}(a) is a subgradient of the convex function χ2,n\chi\_{2,n} at aa. Hence by taking a subsequence, we can assume that {χ2,n​(a)}n\{\chi\_{2,n}(a)\}\_{n} and {∇χ2,n​(a)}n\{\nabla\chi\_{2,n}(a)\}\_{n} both converge. As in the proof of Lemma [3.3](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation"), define an affine function L2,n​(y)=χ2,n​(a)+∇χ2,n​(a)⋅(y−a)L\_{2,n}(y)=\chi\_{2,n}(a)+\nabla\chi\_{2,n}(a)\cdot(y-a), and replace ϕ1,n⊕​(x1)\phi\_{1,n}^{\oplus}(x\_{1}) with ϕ1,n⊕​(x1)−L2,n​(x1)\phi\_{1,n}^{\oplus}(x\_{1})-L\_{2,n}(x\_{1}), ϕ2,n⊕​(x2)\phi\_{2,n}^{\oplus}(x\_{2}) with ϕ2,n⊕​(x2)+L2,n​(x2)\phi\_{2,n}^{\oplus}(x\_{2})+L\_{2,n}(x\_{2}), and finally h1,n​(x1)h\_{1,n}(x\_{1}) with h1,n​(x1)−∇χ2,n​(a)h\_{1,n}(x\_{1})-\nabla\chi\_{2,n}(a). This yields χ2,n​(a)=∇χ2,n​(a)=0\chi\_{2,n}(a)=\nabla\chi\_{2,n}(a)=0 for all nn, while the a.s. convergence of ϕt,i,n\phi\_{t,i,n} and the bound ([7.15](https://arxiv.org/html/2602.02996v1#S7.E15 "Equation 7.15 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) are retained. Next, the inequality χ3,n≥χ2,n+ϕ2,n⊕\chi\_{3,n}\geq\chi\_{2,n}+\phi^{\oplus}\_{2,n} with χ2,n≥0\chi\_{2,n}\geq 0 yields infnχ3,n​(a2)>−∞\inf\_{n}\chi\_{3,n}(a\_{2})>-\infty. Thus we can repeat the argument and achieve the normalization ([7.5](https://arxiv.org/html/2602.02996v1#S7.E5 "Equation 7.5 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), while the a.s. convergence of ϕt,i,n\phi\_{t,i,n} and the bound ([7.15](https://arxiv.org/html/2602.02996v1#S7.E15 "Equation 7.15 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) are retained. Thanks to the local bound ([7.7](https://arxiv.org/html/2602.02996v1#S7.E7 "Equation 7.7 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) and ([7.3](https://arxiv.org/html/2602.02996v1#S7.E3 "Equation 7.3 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), we can now apply [[21](https://arxiv.org/html/2602.02996v1#bib.bib21), Proposition A.1] to deduce the pointwise convergence χt,n→χt\chi\_{t,n}\to\chi\_{t} on Jt−1J\_{t-1}.

As the limit function (ϕt,i)t,i(\phi\_{t,i})\_{t,i} is only well defined μt,i\mu\_{t,i}-a.s., define ϕt,i:=−∞\phi\_{t,i}:=-\infty on a μt,i\mu\_{t,i}-null set (which includes ℝ∖It,i{\mathbb{R}}\setminus I\_{t,i}), so that they are defined everywhere on ℝ{\mathbb{R}}. We now show that there exist functions ht=(ht,i)i:ℝt​d→ℝdh\_{t}=(h\_{t,i})\_{i}:{\mathbb{R}}^{td}\to{\mathbb{R}}^{d} for all t∈[N]t\in[N] with hN≡0h\_{N}\equiv 0, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑t=1N(ϕt⊕​(xt)+ht​(x¯t)⋅Δ​xt)≤c​(x)for all ​x∈ℝN​d.\displaystyle\sum\_{t=1}^{N}\big(\phi\_{t}^{\oplus}(x\_{t})+h\_{t}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)\leq c(x)\ \ \text{for all }x\in{\mathbb{R}}^{Nd}. |  | (7.18) |

For any function f:ℝd→ℝ∪{+∞}f:{\mathbb{R}}^{d}\to{\mathbb{R}}\cup\{+\infty\} which is bounded below by an affine function, let conv​[f]:ℝd→ℝ∪{+∞}{\rm conv}[f]:{\mathbb{R}}^{d}\to{\mathbb{R}}\cup\{+\infty\} denote the lower semi-continuous convex envelope of ff, that is the supremum of all affine functions ll satisfying l≤fl\leq f (If there is no such ll, let conv​[f]≡−∞{\rm conv}[f]\equiv-\infty.) We will inductively obtain hN−1,hN−2,…,h1h\_{N-1},h\_{N-2},...,h\_{1}. Let us rewrite ([3.3](https://arxiv.org/html/2602.02996v1#S3.E3 "Equation 3.3 ‣ 3rd item ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑t=1N−1(ϕt,n⊕​(xt)+ht,n​(x¯t)⋅Δ​xt)≤c​(x)−ϕN,n⊕​(xN).\displaystyle\sum\_{t=1}^{N-1}\big(\phi\_{t,n}^{\oplus}(x\_{t})+h\_{t,n}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)\leq c(x)-\phi\_{N,n}^{\oplus}(x\_{N}). |  | (7.19) |

Define HN−1,n​(x¯N−1,xN)=conv​[c​(x¯N−1,⋅)−ϕN,n⊕​(⋅)]​(xN)H\_{N-1,n}(\bar{x}\_{N-1},x\_{N})={\rm conv}[c(\bar{x}\_{N-1},\,\cdot\,)-\phi\_{N,n}^{\oplus}(\,\cdot\,)](x\_{N}). We then have

|  |  |  |
| --- | --- | --- |
|  | ∑t=1N−1(ϕt,n⊕​(xt)+ht,n​(x¯t)⋅Δ​xt)≤HN−1,n​(x¯N−1,xN)≤c​(x)−ϕN,n⊕​(xN)\displaystyle\sum\_{t=1}^{N-1}\big(\phi\_{t,n}^{\oplus}(x\_{t})+h\_{t,n}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)\leq H\_{N-1,n}(\bar{x}\_{N-1},x\_{N})\leq c(x)-\phi\_{N,n}^{\oplus}(x\_{N}) |  |

because the left hand side is affine in xNx\_{N}. If we let xN=xN−1x\_{N}=x\_{N-1}, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑t=1N−2(ϕt,n⊕​(xt)+ht,n​(x¯t)⋅Δ​xt)≤HN−1,n​(x¯N−1,xN−1)−ϕN−1,n⊕​(xN−1).\displaystyle\sum\_{t=1}^{N-2}\big(\phi\_{t,n}^{\oplus}(x\_{t})+h\_{t,n}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)\leq H\_{N-1,n}(\bar{x}\_{N-1},x\_{N-1})-\phi\_{N-1,n}^{\oplus}(x\_{N-1}). |  | (7.20) |

We see that ([7.19](https://arxiv.org/html/2602.02996v1#S7.E19 "Equation 7.19 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) and ([7.20](https://arxiv.org/html/2602.02996v1#S7.E20 "Equation 7.20 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) exhibit a similar structure. With the convention HN,n​(x):=c​(x)H\_{N,n}(x):=c(x),
this allows us to inductively deduce, backward in tt,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑s=1t(ϕs,n⊕​(xs)+hs,n​(x¯s)⋅Δ​xs)≤Ht+1,n​(x¯t+1,xt+1)−ϕt+1,n⊕​(xt+1)\displaystyle\sum\_{s=1}^{t}\big(\phi\_{s,n}^{\oplus}(x\_{s})+h\_{s,n}(\bar{x}\_{s})\cdot\Delta x\_{s}\big)\leq H\_{t+1,n}(\bar{x}\_{t+1},x\_{t+1})-\phi\_{t+1,n}^{\oplus}(x\_{t+1}) |  | (7.21) |

for t=1,…,N−1t=1,...,N-1, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ht,n​(x¯t,xt+1):=conv​[Ht+1,n​(x¯t,⋅)−ϕt+1,n⊕​(⋅)]​(xt+1)\displaystyle H\_{t,n}(\bar{x}\_{t},x\_{t+1}):={\rm conv}[H\_{t+1,n}(\bar{x}\_{t},\,\cdot\,)-\phi\_{t+1,n}^{\oplus}(\,\cdot\,)](x\_{t+1}) |  | (7.22) |

with an abuse of notation Ht+1,n​(x¯t,xt+1):=Ht+1,n​(x¯t+1,xt+1)H\_{t+1,n}(\bar{x}\_{t},x\_{t+1}):=H\_{t+1,n}(\bar{x}\_{t+1},x\_{t+1}).

Now by dropping the index nn, we analogously define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ht​(x¯t,xt+1):=conv​[Ht+1​(x¯t,⋅)−ϕt+1⊕​(⋅)]​(xt+1)\displaystyle H\_{t}(\bar{x}\_{t},x\_{t+1}):={\rm conv}[H\_{t+1}(\bar{x}\_{t},\,\cdot\,)-\phi\_{t+1}^{\oplus}(\,\cdot\,)](x\_{t+1}) |  | (7.23) |

with HN​(x):=c​(x)H\_{N}(x):=c(x). Next, since the lim sup\limsup of convex functions is convex, in conjunction with the almost sure convergence ([7.14](https://arxiv.org/html/2602.02996v1#S7.E14 "Equation 7.14 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supn→∞HN−1,n​(x¯N−1,xN)\displaystyle\limsup\_{n\to\infty}H\_{N-1,n}(\bar{x}\_{N-1},x\_{N}) | =lim supn→∞conv​[c​(x¯N−1,⋅)−ϕN,n⊕​(⋅)]​(xN)\displaystyle=\limsup\_{n\to\infty}{\rm conv}[c(\bar{x}\_{N-1},\,\cdot\,)-\phi\_{N,n}^{\oplus}(\,\cdot\,)](x\_{N}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤conv​[lim supn→∞(c​(x¯N−1,⋅)−ϕN,n⊕​(⋅))]​(xN)\displaystyle\leq{\rm conv}[\limsup\_{n\to\infty}\big(c(\bar{x}\_{N-1},\,\cdot\,)-\phi\_{N,n}^{\oplus}(\,\cdot\,)\big)](x\_{N}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤conv​[c​(x¯N−1,⋅)−ϕN⊕​(⋅)]​(xN)\displaystyle\leq{\rm conv}[c(\bar{x}\_{N-1},\,\cdot\,)-\phi\_{N}^{\oplus}(\,\cdot\,)](x\_{N}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =HN−1​(x¯N−1,xN).\displaystyle=H\_{N-1}(\bar{x}\_{N-1},x\_{N}). |  |

This allows us to inductively deduce, for t=1,…,N−1t=1,...,N-1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supn→∞Ht,n​(x¯t,xt+1)\displaystyle\limsup\_{n\to\infty}H\_{t,n}(\bar{x}\_{t},x\_{t+1}) | =lim supn→∞conv​[Ht+1,n​(x¯t,⋅)−ϕt+1,n⊕​(⋅)]​(xt+1)\displaystyle=\limsup\_{n\to\infty}{\rm conv}[H\_{t+1,n}(\bar{x}\_{t},\,\cdot\,)-\phi\_{t+1,n}^{\oplus}(\,\cdot\,)](x\_{t+1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤conv​[lim supn→∞(Ht+1,n​(x¯t,⋅)−ϕt+1,n⊕​(⋅))]​(xt+1)\displaystyle\leq{\rm conv}[\limsup\_{n\to\infty}\big(H\_{t+1,n}(\bar{x}\_{t},\,\cdot\,)-\phi\_{t+1,n}^{\oplus}(\,\cdot\,)\big)](x\_{t+1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤conv​[Ht+1​(x¯t,⋅)−ϕt+1⊕​(⋅)]​(xt+1)\displaystyle\leq{\rm conv}[H\_{t+1}(\bar{x}\_{t},\,\cdot\,)-\phi\_{t+1}^{\oplus}(\,\cdot\,)](x\_{t+1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Ht​(x¯t,xt+1).\displaystyle=H\_{t}(\bar{x}\_{t},x\_{t+1}). |  |

Let us discuss continuity of the convex function xt+1↦Ht​(x¯t,xt+1)x\_{t+1}\mapsto H\_{t}(\bar{x}\_{t},x\_{t+1}). The following inequality from ([7.23](https://arxiv.org/html/2602.02996v1#S7.E23 "Equation 7.23 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation"))

|  |  |  |
| --- | --- | --- |
|  | Ht​(x¯t,xt+1)≤Ht+1​(x¯t+1,xt+1)−ϕt+1⊕​(xt+1)H\_{t}(\bar{x}\_{t},x\_{t+1})\leq H\_{t+1}(\bar{x}\_{t+1},x\_{t+1})-\phi\_{t+1}^{\oplus}(x\_{t+1}) |  |

becomes HN−1​(x¯N−1,xN)≤c​(x)−ϕN⊕​(xN)H\_{N-1}(\bar{x}\_{N-1},x\_{N})\leq c(x)-\phi\_{N}^{\oplus}(x\_{N}) when t=N−1t=N-1. Then the μN⊗\mu\_{N}^{\otimes}-a.s. finiteness of ϕN⊕\phi\_{N}^{\oplus} implies, by convexity, HN−1​(x¯N−1,xN)<∞H\_{N-1}(\bar{x}\_{N-1},x\_{N})<\infty if xN∈JN−1x\_{N}\in J\_{N-1}. Backward induction in tt then gives Ht​(x¯t,xt+1)<∞H\_{t}(\bar{x}\_{t},x\_{t+1})<\infty if xt+1∈Jtx\_{t+1}\in J\_{t}. This implies that if there exists y0∈ℝdy\_{0}\in{\mathbb{R}}^{d} such that Ht​(x¯t,y0)>−∞H\_{t}(\bar{x}\_{t},y\_{0})>-\infty, then y↦Ht​(x¯t,y)y\mapsto H\_{t}(\bar{x}\_{t},y) is real-valued and continuous in JtJ\_{t}. This being observed, now ([7.21](https://arxiv.org/html/2602.02996v1#S7.E21 "Equation 7.21 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), ([7.22](https://arxiv.org/html/2602.02996v1#S7.E22 "Equation 7.22 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) gives

|  |  |  |
| --- | --- | --- |
|  | ϕ1,n⊕​(x1)+h1,n​(x1)⋅Δ​x1≤H1,n​(x1,x2)≤H2,n​(x1,x2,x2)−ϕ2,n⊕​(x2).\displaystyle\phi\_{1,n}^{\oplus}(x\_{1})+h\_{1,n}(x\_{1})\cdot\Delta x\_{1}\leq H\_{1,n}(x\_{1},x\_{2})\leq H\_{2,n}(x\_{1},x\_{2},x\_{2})-\phi\_{2,n}^{\oplus}(x\_{2}). |  |

Letting x2=x1x\_{2}=x\_{1} gives ϕ1,n⊕​(x1)≤H1,n​(x1,x1)\phi\_{1,n}^{\oplus}(x\_{1})\leq H\_{1,n}(x\_{1},x\_{1}). Taking lim sup\limsup yields

|  |  |  |
| --- | --- | --- |
|  | ϕ1⊕​(x1)≤H1​(x1,x1)​ and ​H1​(x1,x2)≤H2​(x1,x2,x2)−ϕ2⊕​(x2).\displaystyle\phi\_{1}^{\oplus}(x\_{1})\leq H\_{1}(x\_{1},x\_{1})\ \text{ and }\ H\_{1}(x\_{1},x\_{2})\leq H\_{2}(x\_{1},x\_{2},x\_{2})-\phi\_{2}^{\oplus}(x\_{2}). |  |

Define At:={xt∈ℝd|ϕt⊕​(xt)∈ℝ}A\_{t}:=\{x\_{t}\in{\mathbb{R}}^{d}\,|\,\phi\_{t}^{\oplus}(x\_{t})\in{\mathbb{R}}\} for each t∈[N]t\in[N], and note that At⊂ItA\_{t}\subset I\_{t}. Since x2↦H1​(x1,x2)x\_{2}\mapsto H\_{1}(x\_{1},x\_{2}) is continuous in J1J\_{1} for every x1∈A1x\_{1}\in A\_{1}, the subdifferential ∂H1​(x1,⋅)​(x2)\partial H\_{1}(x\_{1},\,\cdot\,)(x\_{2}) is nonempty, convex and compact for every x2∈I1=int​(J1)x\_{2}\in I\_{1}={\rm int}(J\_{1}). This allows us to choose a measurable function h1:A1→ℝdh\_{1}:A\_{1}\to{\mathbb{R}}^{d} satisfying h1​(x1)∈∂H1​(x1,⋅)​(x1)h\_{1}(x\_{1})\in\partial H\_{1}(x\_{1},\,\cdot\,)(x\_{1}). Then for x1∈A1x\_{1}\in A\_{1}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ1⊕​(x1)+h1​(x1)⋅(x2−x1)\displaystyle\phi\_{1}^{\oplus}(x\_{1})+h\_{1}(x\_{1})\cdot(x\_{2}-x\_{1}) | ≤H1​(x1,x1)+h1​(x1)⋅(x2−x1)\displaystyle\leq H\_{1}(x\_{1},x\_{1})+h\_{1}(x\_{1})\cdot(x\_{2}-x\_{1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤H1​(x1,x2)\displaystyle\leq H\_{1}(x\_{1},x\_{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤H2​(x1,x2,x2)−ϕ2⊕​(x2).\displaystyle\leq H\_{2}(x\_{1},x\_{2},x\_{2})-\phi\_{2}^{\oplus}(x\_{2}). |  |

In particular, for x1∈A1x\_{1}\in A\_{1} and x2∈A2x\_{2}\in A\_{2}, it holds H2​(x1,x2,x2)>−∞H\_{2}(x\_{1},x\_{2},x\_{2})>-\infty. Hence again we can choose h2:A1×A2→ℝdh\_{2}:A\_{1}\times A\_{2}\to{\mathbb{R}}^{d} that satisfies h2​(x1,x2)∈∂H2​(x1,x2,⋅)​(x2)h\_{2}(x\_{1},x\_{2})\in\partial H\_{2}(x\_{1},x\_{2},\,\cdot\,)(x\_{2}). Then for every x1∈A1x\_{1}\in A\_{1} and x2∈A2x\_{2}\in A\_{2}, we have

|  |  |  |
| --- | --- | --- |
|  | ϕ1⊕​(x1)+ϕ2⊕​(x2)+h1​(x1)⋅(x2−x1)+h2​(x1,x2)⋅(x3−x2)\displaystyle\phi\_{1}^{\oplus}(x\_{1})+\phi\_{2}^{\oplus}(x\_{2})+h\_{1}(x\_{1})\cdot(x\_{2}-x\_{1})+h\_{2}(x\_{1},x\_{2})\cdot(x\_{3}-x\_{2}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤H2​(x1,x2,x2)+h2​(x1,x2)⋅(x3−x2)\displaystyle\leq H\_{2}(x\_{1},x\_{2},x\_{2})+h\_{2}(x\_{1},x\_{2})\cdot(x\_{3}-x\_{2}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤H2​(x1,x2,x3)\displaystyle\leq H\_{2}(x\_{1},x\_{2},x\_{3}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤H3​(x1,x2,x3,x3)−ϕ3⊕​(x3).\displaystyle\leq H\_{3}(x\_{1},x\_{2},x\_{3},x\_{3})-\phi\_{3}^{\oplus}(x\_{3}). |  |

By induction in tt, we obtain ht:A1×⋯×At→ℝdh\_{t}:A\_{1}\times\dots\times A\_{t}\to{\mathbb{R}}^{d} (with hN≡0h\_{N}\equiv 0), satisfying ([7.18](https://arxiv.org/html/2602.02996v1#S7.E18 "Equation 7.18 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) as desired. We may define ht=0h\_{t}=0 in ℝt​d∖A1×⋯×At{\mathbb{R}}^{td}\setminus A\_{1}\times\dots\times A\_{t}, noting that the left hand side of ([7.18](https://arxiv.org/html/2602.02996v1#S7.E18 "Equation 7.18 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) is −∞-\infty if xt∉Atx\_{t}\notin A\_{t} for some tt.

The last step is to show the following claim: for any functions ht:ℝt​d→ℝdh\_{t}:{\mathbb{R}}^{td}\to{\mathbb{R}}^{d}, t=1,…,Nt=1,...,N with hN≡0h\_{N}\equiv 0 satisfying ([7.18](https://arxiv.org/html/2602.02996v1#S7.E18 "Equation 7.18 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) (whose existence was just shown), and for any minimizer π∗\pi^{\*} for the VMOT problem ([2.2](https://arxiv.org/html/2602.02996v1#S2.E2 "Equation 2.2 ‣ 2.2 Vectorial Martingale Optimal Transport (VMOT) ‣ 2 Problem Formulation ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), it holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑t=1N(ϕt⊕​(xt)+ht​(x¯t)⋅Δ​xt)=c​(x),π∗−a.s..\displaystyle\sum\_{t=1}^{N}\big(\phi\_{t}^{\oplus}(x\_{t})+h\_{t}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)=c(x),\quad\pi^{\*}-a.s.. |  | (7.24) |

In other words, every minimizer π∗\pi^{\*} is concentrated on the contact set

|  |  |  |
| --- | --- | --- |
|  | Γ:={x∈ℝN​d|∑t=1N(ϕt⊕​(xt)+ht​(x¯t)⋅Δ​xt)=c​(x)}\Gamma:=\bigg\{x\in{\mathbb{R}}^{Nd}\,\bigg|\,\sum\_{t=1}^{N}\big(\phi\_{t}^{\oplus}(x\_{t})+h\_{t}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)=c(x)\bigg\} |  |

whenever {ht}t\{h\_{t}\}\_{t} satisfies ([7.18](https://arxiv.org/html/2602.02996v1#S7.E18 "Equation 7.18 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")). This will complete the proof of the theorem.

The proof of this claim was provided in [[5](https://arxiv.org/html/2602.02996v1#bib.bib5)] for the single-asset, two-period case (d,N)=(1,2)(d,N)=(1,2), and we build upon that approach to extend to the general case. To begin, recall ϕt,i,n→ϕt,i\phi\_{t,i,n}\to\phi\_{t,i} μt,i\mu\_{t,i}-a.s. and χt,n→χt\chi\_{t,n}\to\chi\_{t} in Jt−1J\_{t-1} where χt,n\chi\_{t,n} is defined in ([7.1](https://arxiv.org/html/2602.02996v1#S7.E1 "Equation 7.1 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) with χt\chi\_{t} being its limit. For any π∈VMT​(μ)\pi\in{\rm VMT}(\mu) (not necessarily an optimizer), we have c∈L1​(π)c\in L^{1}(\pi) by the assumption of Theorem [3.1](https://arxiv.org/html/2602.02996v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.3 Main Result: Dual Attainment for Multi-Asset, Multi-Period MOT ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation"). We claim:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | lim supn→∞\displaystyle\limsup\_{n\to\infty} | ∫∑t=1N(ϕt,n⊕​(xt)+ht,n​(x¯t)⋅Δ​xt)​d​π\displaystyle\int\sum\_{t=1}^{N}\big(\phi\_{t,n}^{\oplus}(x\_{t})+h\_{t,n}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)d\pi |  | (7.25) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫∑t=1N(ϕt⊕​(xt)+ht​(x¯t)⋅Δ​xt)​d​π.\displaystyle\leq\int\sum\_{t=1}^{N}\big(\phi\_{t}^{\oplus}(x\_{t})+h\_{t}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)d\pi. |  |

To see how the claim implies ([7.24](https://arxiv.org/html/2602.02996v1#S7.E24 "Equation 7.24 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), let π∗\pi^{\*} be any minimizer for ([2.2](https://arxiv.org/html/2602.02996v1#S2.E2 "Equation 2.2 ‣ 2.2 Vectorial Martingale Optimal Transport (VMOT) ‣ 2 Problem Formulation ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) (which exists by the assumption on cc). Then D​(c)=P​(c)=∫c​𝑑π∗D(c)=P(c)=\int c\,d\pi^{\*}, hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(c)\displaystyle P(c) | =limn→∞∫∑t=1N(ϕt,n⊕​(xt)+ht,n​(x¯t)⋅Δ​xt)​d​π∗\displaystyle=\lim\_{n\to\infty}\int\sum\_{t=1}^{N}\big(\phi\_{t,n}^{\oplus}(x\_{t})+h\_{t,n}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)d\pi^{\*} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫∑t=1N(ϕt⊕​(xt)+ht​(x¯t)⋅Δ​xt)​d​π∗\displaystyle\leq\int\sum\_{t=1}^{N}\big(\phi\_{t}^{\oplus}(x\_{t})+h\_{t}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)d\pi^{\*} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫c​(x)​𝑑π∗=P​(c)\displaystyle\leq\int c(x)\,d\pi^{\*}=P(c) |  |

by Fatou’s lemma, yielding equality throughout. Notice that this implies ([7.24](https://arxiv.org/html/2602.02996v1#S7.E24 "Equation 7.24 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")).

To prove ([7.25](https://arxiv.org/html/2602.02996v1#S7.E25 "Equation 7.25 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), fix any π∈VMT​(μ)\pi\in{\rm VMT}(\mu). Denoting π=Law​(X)\pi={\rm Law}(X) where X=(X1,…,XN)X=(X\_{1},...,X\_{N}) is an ℝd{\mathbb{R}}^{d}-valued martingale under π\pi, let πt:=Law​(Xt)\pi\_{t}:={\rm Law}(X\_{t}). By following the argument which establishes ([7.8](https://arxiv.org/html/2602.02996v1#S7.E8 "Equation 7.8 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), but this time utilizing the convex order πt⪯cπt+1\pi\_{t}\preceq\_{c}\pi\_{t+1} instead of μt⊗⪯cμt+1⊗\mu^{\otimes}\_{t}\preceq\_{c}\mu^{\otimes}\_{t+1}, by ([3.4](https://arxiv.org/html/2602.02996v1#S3.E4 "Equation 3.4 ‣ 4th item ‣ 3.4 Intuitive Explanation and Approximating Dual Maximizers ‣ 3 Main Theoretical Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) and ([7.2](https://arxiv.org/html/2602.02996v1#S7.E2 "Equation 7.2 ‣ Proof of Lemma 3.3. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), we can deduce

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖χt+1,n−χt,n−ϕt,n⊕‖L1​(πt)≤C​ for all ​n∈ℕ,t∈[N].\parallel\chi\_{t+1,n}-\chi\_{t,n}-\phi\_{t,n}^{\oplus}\parallel\_{L^{1}(\pi\_{t})}\,\leq C\ \text{ for all }n\in{\mathbb{N}},t\in[N]. |  | (7.26) |

Using ϕt,n⊕→ϕt⊕\phi^{\oplus}\_{t,n}\to\phi^{\oplus}\_{t}, χt,n→χt\chi\_{t,n}\to\chi\_{t} and Fatou’s lemma, from ([7.26](https://arxiv.org/html/2602.02996v1#S7.E26 "Equation 7.26 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) we deduce

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | χt+1−χt−ϕt⊕∈L1​(πt), and\displaystyle\chi\_{t+1}-\chi\_{t}-\phi\_{t}^{\oplus}\in L^{1}(\pi\_{t}),\ \text{ and} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supn→∞∫(\displaystyle\limsup\_{n\to\infty}\int( | ϕt,n⊕+χt,n−χt+1,n)dπt≤∫(ϕt⊕+χt−χt+1)dπt,\displaystyle\phi\_{t,n}^{\oplus}+\chi\_{t,n}-\chi\_{t+1,n})\,d\pi\_{t}\leq\int(\phi\_{t}^{\oplus}+\chi\_{t}-\chi\_{t+1})\,d\pi\_{t}, |  |

recalling χ1,n=χN+1,n≡0\chi\_{1,n}=\chi\_{N+1,n}\equiv 0 and πt​(Jt−1)=1\pi\_{t}(J\_{t-1})=1. This allows us to deduce

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supn→∞\displaystyle\limsup\_{n\to\infty} | ∫∑t=1N(ϕt,n⊕​(xt)+ht,n​(x¯t)⋅Δ​xt)​d​π\displaystyle\int\sum\_{t=1}^{N}\big(\phi\_{t,n}^{\oplus}(x\_{t})+h\_{t,n}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)d\pi |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =lim supn→∞\displaystyle=\limsup\_{n\to\infty} | ∫∑t=1N(ϕt,n⊕(xt)+χt,n(xt)−χt+1,n(xt)\displaystyle\int\sum\_{t=1}^{N}\big(\phi\_{t,n}^{\oplus}(x\_{t})+\chi\_{t,n}(x\_{t})-\chi\_{t+1,n}(x\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −χt,n(xt)+χt+1,n(xt)+ht,n(x¯t)⋅Δxt)dπ\displaystyle\ \ \quad\quad\quad-\chi\_{t,n}(x\_{t})+\chi\_{t+1,n}(x\_{t})+h\_{t,n}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)d\pi |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤∑t=1N∫\displaystyle\leq\sum\_{t=1}^{N}\int | (ϕt⊕+χt−χt+1)​d​πt\displaystyle\big(\phi\_{t}^{\oplus}+\chi\_{t}-\chi\_{t+1}\big)d\pi\_{t} |  | (7.27) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +lim supn→∞\displaystyle+\limsup\_{n\to\infty} | ∫∑t=1N−1(χt+1,n​(xt)−χt+1,n​(xt+1)+ht,n​(x¯t)⋅Δ​xt)​d​π,\displaystyle\int\sum\_{t=1}^{N-1}\big(\chi\_{t+1,n}(x\_{t})-\chi\_{t+1,n}(x\_{t+1})+h\_{t,n}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)\,d\pi, |  |

since ∑t=1Nχt,n​(xt)=∑t=1Nχt+1,n​(xt+1)\sum\_{t=1}^{N}\chi\_{t,n}(x\_{t})=\sum\_{t=1}^{N}\chi\_{t+1,n}(x\_{t+1}). Now denote X¯t=(X1,…,Xt)\bar{X}\_{t}=(X\_{1},...,X\_{t}), πt:=Law​(X¯t)∈𝒫​(ℝt​d)\pi^{t}:={\rm Law}(\bar{X}\_{t})\in{\cal P}({\mathbb{R}}^{td}). Then we can write πt+1=πx¯t⊗πt\pi^{t+1}=\pi\_{\bar{x}\_{t}}\otimes\pi^{t}, where πx¯t∈𝒫​(ℝd)\pi\_{\bar{x}\_{t}}\in{\cal P}({\mathbb{R}}^{d}) is the conditional distribution of Xt+1X\_{t+1} given X¯t=x¯t\bar{X}\_{t}=\bar{x}\_{t} under the martingale law π\pi. Martingale property means that ∫y​𝑑πx¯t​(y)=xt\int y\,d\pi\_{\bar{x}\_{t}}(y)=x\_{t}. For each tt, choose a sequence of functions ξt,n:It→ℝd\xi\_{t,n}:I\_{t}\to{\mathbb{R}}^{d} satisfying ξt,n​(xt)∈∂χt+1,n​(xt)\xi\_{t,n}(x\_{t})\in\partial\chi\_{t+1,n}(x\_{t}). Then we compute

|  |  |  |
| --- | --- | --- |
|  | ∫∑t=1N−1(χt+1,n​(xt)−χt+1,n​(xt+1)+ht,n​(x¯t)⋅Δ​xt)​d​π\displaystyle\int\sum\_{t=1}^{N-1}\big(\chi\_{t+1,n}(x\_{t})-\chi\_{t+1,n}(x\_{t+1})+h\_{t,n}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)\,d\pi |  |
|  |  |  |
| --- | --- | --- |
|  | =∫(∫(χN,n(xN−1)−χN,n(xN)+ξN−1,n(xN−1)⋅ΔxN−1)dπx¯N−1(xN)\displaystyle=\int\bigg(\int\big(\chi\_{N,n}(x\_{N-1})-\chi\_{N,n}(x\_{N})+\xi\_{N-1,n}(x\_{N-1})\cdot\Delta x\_{N-1}\big)d\pi\_{\bar{x}\_{N-1}}(x\_{N}) |  |
|  |  |  |
| --- | --- | --- |
|  | +∑t=1N−2(χt+1,n(xt)−χt+1,n(xt+1)+ht,n(x¯t)⋅Δxt))dπN−1(x¯N−1),\displaystyle\quad\quad\quad+\sum\_{t=1}^{N-2}\big(\chi\_{t+1,n}(x\_{t})-\chi\_{t+1,n}(x\_{t+1})+h\_{t,n}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)\bigg)d\pi^{N-1}(\bar{x}\_{N-1}), |  |

where we replaced hN−1,n​(x¯N−1)h\_{N-1,n}(\bar{x}\_{N-1}) by ξN−1,n​(x¯N−1)\xi\_{N-1,n}(\bar{x}\_{N-1}) due to the martingale property

|  |  |  |
| --- | --- | --- |
|  | ∫hN−1,n​(x¯N−1)⋅Δ​xN−1​𝑑πx¯N−1​(xN)=∫ξN−1,n​(xN−1)⋅Δ​xN−1​𝑑πx¯N−1​(xN)=0.\displaystyle\int h\_{N-1,n}(\bar{x}\_{N-1})\cdot\Delta x\_{N-1}\,d\pi\_{\bar{x}\_{N-1}}(x\_{N})=\int\xi\_{N-1,n}(x\_{N-1})\cdot\Delta x\_{N-1}\,d\pi\_{\bar{x}\_{N-1}}(x\_{N})=0. |  |

By definition of ξ\xi, we have χN,n​(xN−1)−χN,n​(xN)+ξN−1,n​(xN−1)⋅Δ​xN−1≤0\chi\_{N,n}(x\_{N-1})-\chi\_{N,n}(x\_{N})+\xi\_{N-1,n}(x\_{N-1})\cdot\Delta x\_{N-1}\leq 0.
This allows us to disintegrate πN−1=πx¯N−2⊗πN−2\pi^{N-1}=\pi\_{\bar{x}\_{N-2}}\otimes\pi^{N-2} and repeat the same argument

|  |  |  |
| --- | --- | --- |
|  | ∫∑t=1N−1(χt+1,n​(xt)−χt+1,n​(xt+1)+ht,n​(x¯t)⋅Δ​xt)​d​π\displaystyle\int\sum\_{t=1}^{N-1}\big(\chi\_{t+1,n}(x\_{t})-\chi\_{t+1,n}(x\_{t+1})+h\_{t,n}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)\,d\pi |  |
|  |  |  |
| --- | --- | --- |
|  | =∫…​∫(χN,n​(xN−1)−χN,n​(xN)+ξN−1,n​(xN−1)⋅Δ​xN−1)​𝑑πx¯N−1​(xN)\displaystyle=\int\dots\int\big(\chi\_{N,n}(x\_{N-1})-\chi\_{N,n}(x\_{N})+\xi\_{N-1,n}(x\_{N-1})\cdot\Delta x\_{N-1}\big)d\pi\_{\bar{x}\_{N-1}}(x\_{N}) |  |
|  |  |  |
| --- | --- | --- |
|  | +(χN−1,n​(xN−2)−χN−1,n​(xN−1)+ξN−2,n​(xN−2)⋅Δ​xN−2)​d​πx¯N−2​(xN−1)\displaystyle\ +\big(\chi\_{N-1,n}(x\_{N-2})-\chi\_{N-1,n}(x\_{N-1})+\xi\_{N-2,n}(x\_{N-2})\cdot\Delta x\_{N-2}\big)d\pi\_{\bar{x}\_{N-2}}(x\_{N-1}) |  |
|  |  |  |
| --- | --- | --- |
|  | +⋯+(χ2,n​(x1)−χ2,n​(x2)+ξ1,n​(x1)⋅Δ​x1)​d​πx¯1​(x2)​d​π1​(x1).\displaystyle\ +\dots+\big(\chi\_{2,n}(x\_{1})-\chi\_{2,n}(x\_{2})+\xi\_{1,n}(x\_{1})\cdot\Delta x\_{1}\big)d\pi\_{\bar{x}\_{1}}(x\_{2})d\pi^{1}(x\_{1}). |  |

Since χt+1,n​(xt)−χt+1,n​(xt+1)+ξt,n​(xt)⋅Δ​xt≤0\chi\_{t+1,n}(x\_{t})-\chi\_{t+1,n}(x\_{t+1})+\xi\_{t,n}(x\_{t})\cdot\Delta x\_{t}\leq 0 for all tt, repeated application of Fatou’s lemma allows lim sup\limsup to continue to penetrate into the innermost integral. Using lim sup(an+bn)≤lim supan+lim supbn\limsup(a\_{n}+b\_{n})\leq\limsup a\_{n}+\limsup b\_{n}, this eventually yield

|  |  |  |
| --- | --- | --- |
|  | lim supn→∞∫∑t=1N−1(χt+1,n​(xt)−χt+1,n​(xt+1)+ht,n​(x¯t)⋅Δ​xt)​d​π\displaystyle\limsup\_{n\to\infty}\int\sum\_{t=1}^{N-1}\big(\chi\_{t+1,n}(x\_{t})-\chi\_{t+1,n}(x\_{t+1})+h\_{t,n}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)\,d\pi |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫…​∫(χN​(xN−1)−χN​(xN)+ξN−1​(xN−1)⋅Δ​xN−1)​𝑑πx¯N−1​(xN)\displaystyle\leq\int\dots\int\big(\chi\_{N}(x\_{N-1})-\chi\_{N}(x\_{N})+\xi\_{N-1}(x\_{N-1})\cdot\Delta x\_{N-1}\big)d\pi\_{\bar{x}\_{N-1}}(x\_{N}) |  |
|  |  |  |
| --- | --- | --- |
|  | +(χN−1​(xN−2)−χN−1​(xN−1)+ξN−2​(xN−2)⋅Δ​xN−2)​d​πx¯N−2​(xN−1)\displaystyle\ +\big(\chi\_{N-1}(x\_{N-2})-\chi\_{N-1}(x\_{N-1})+\xi\_{N-2}(x\_{N-2})\cdot\Delta x\_{N-2}\big)d\pi\_{\bar{x}\_{N-2}}(x\_{N-1}) |  |
|  |  |  |
| --- | --- | --- |
|  | +⋯+(χ2​(x1)−χ2​(x2)+ξ1​(x1)⋅Δ​x1)​d​πx¯1​(x2)​d​π1​(x1)\displaystyle\ +\dots+\big(\chi\_{2}(x\_{1})-\chi\_{2}(x\_{2})+\xi\_{1}(x\_{1})\cdot\Delta x\_{1}\big)d\pi\_{\bar{x}\_{1}}(x\_{2})d\pi^{1}(x\_{1}) |  |

for some ξt​(xt)∈∂χt+1​(xt)\xi\_{t}(x\_{t})\in\partial\chi\_{t+1}(x\_{t}) which is a limit point of the bounded sequence {ξt,n​(xt)}n\{\xi\_{t,n}(x\_{t})\}\_{n}. Substituting ξt​(xt)\xi\_{t}(x\_{t}) back to ht​(x¯t)h\_{t}(\bar{x}\_{t}) in the above inequality yields

|  |  |  |
| --- | --- | --- |
|  | lim supn→∞∫∑t=1N−1(χt+1,n​(xt)−χt+1,n​(xt+1)+ht,n​(x¯t)⋅Δ​xt)​d​π\displaystyle\limsup\_{n\to\infty}\int\sum\_{t=1}^{N-1}\big(\chi\_{t+1,n}(x\_{t})-\chi\_{t+1,n}(x\_{t+1})+h\_{t,n}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)\,d\pi |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫∑t=1N−1(χt+1​(xt)−χt+1​(xt+1)+ht​(x¯t)⋅Δ​xt)​d​π.\displaystyle\leq\int\sum\_{t=1}^{N-1}\big(\chi\_{t+1}(x\_{t})-\chi\_{t+1}(x\_{t+1})+h\_{t}(\bar{x}\_{t})\cdot\Delta x\_{t}\big)\,d\pi. |  |

Combining the integrals in ([7.27](https://arxiv.org/html/2602.02996v1#S7.E27 "Equation 7.27 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")) then yields the claim ([7.25](https://arxiv.org/html/2602.02996v1#S7.E25 "Equation 7.25 ‣ Proof of Theorem 3.1. ‣ 7 Proofs of Main Results ‣ Dual Attainment in Multi-Period Multi-Asset Martingale Optimal Transport and Its Computation")), hence the theorem.
∎

## References

* [1]

  David Applegate, Mateo Díaz, Oliver Hinder, Haihao Lu, Miles Lubin, Brendan O’Donoghue, and Warren Schudy.
  Practical large-scale linear programming using primal-dual hybrid gradient.
  Advances in Neural Information Processing Systems, 34:20243–20257, 2021.
* [2]

  M. Beiglböck, P. Henry-Labordère, and F. Penkner.
  Model-independent bounds for option prices: a mass transport approach.
  Finance and Stochastics, 17:477–501, 2013.
* [3]

  M. Beiglböck and N. Juillet.
  On a problem of optimal transport under marginal martingale constraints.
  Ann. Probab., 44(1):42–106, 2016.
* [4]

  M. Beiglböck, T. Lim, and J. Obłój.
  Dual attainment for the martingale transport problem.
  Bernoulli, 25(3):1640–1658, 2019.
* [5]

  M. Beiglböck, M. Nutz, and N. Touzi.
  Complete duality for martingale optimal transport on the line.
  Ann. Probab., 45(5):3038–3074, 2017.
* [6]

  D. T. Breeden and R. H. Litzenberger.
  Prices of state-contingent claims implicit in option prices.
  J. Business, 51(4):621–651, 1978.
* [7]

  Y. Brenier.
  Polar factorization and monotone rearrangement of vector-valued functions.
  Comm. Pure Appl. Math., 44(4):375–417, 1991.
* [8]

  Antonin Chambolle and Thomas Pock.
  A first-order primal-dual algorithm for convex problems with applications to imaging.
  Journal of Mathematical Imaging and Vision, 40:120–145, 2011.
* [9]

  NVIDIA Corporation.
  cuOpt: GPU-accelerated optimization engine.
  <https://nvidia.com/cuopt>, 2025.
  Version 25.08.00.
* [10]

  A. M. G. Cox, J. Obłój, and N. Touzi.
  The root solution to the multi-marginal embedding problem: an optimal stopping and time-reversal approach.
  Probab. Theory Related Fields., 173(1-2):211–259, 2019.
* [11]

  Marco Cuturi.
  Sinkhorn distances: Lightspeed computation of optimal transport.
  In C.J. Burges, L. Bottou, M. Welling, Z. Ghahramani, and K.Q. Weinberger, editors, Advances in Neural Information Processing Systems, volume 26. Curran Associates, Inc., 2013.
* [12]

  Hadrien De March.
  Entropic approximation for multi-dimensional martingale optimal transport.
  arXiv preprint arXiv:1812.11104, 2018.
* [13]

  S. Eckstein, G. Guo, T. Lim, and J. Obłój.
  Robust pricing and hedging of options on multiple assets and its numerics.
  SIAM J. Financial Math., 12(1):158–188, 2021.
* [14]

  Stephan Eckstein, Gaoyue Guo, Tongseok Lim, and Jan Obłój.
  Robust pricing and hedging of options on multiple assets and its numerics.
  SIAM Journal on Financial Mathematics, 12(1):158–188, 2021.
* [15]

  N. Ghoussoub, Y-H Kim, and T. Lim.
  Structure of optimal martingale transport plans in general dimensions.
  Ann. Probab., 47(1):109–164, 2019.
* [16]

  I. Guo, G. Loeper, and S. Wang.
  Calibration of local-stochastic volatility models by optimal transport.
  arXiv preprint, 2019.
* [17]

  J. Guyon.
  The joint S&P 500/VIX smile calibration puzzle solved.
  2020.
* [18]

  Oliver Hinder.
  Worst-case analysis of restarted primal-dual hybrid gradient on totally unimodular linear programs.
  arXiv preprint arXiv:2309.03988, 2023.
* [19]

  D. Hobson.
  The skorokhod embedding problem and model-independent bounds for option prices.
  In Paris-Princeton Lectures on Mathematical Finance 2010, volume 2003 of Lecture Notes in Math., pages 267–318. Springer, Berlin, 2011.
* [20]

  L. V. Kantorovich.
  On the translocation of masses.
  Dokl. Akad. Nauk. USSR, 37:199–201, 1942.
* [21]

  T. Lim.
  Geometry of vectorial martingale optimal transportations and duality.
  Mathematical Programming, 2023.
  <https://doi.org/10.1007/s10107-023-01954-4>.
* [22]

  E. Lütkebohmert and J. Sester.
  Tightening robust price bounds for exotic derivatives.
  Quantitative Finance, 19:1797–1815, 2019.
* [23]

  H. De March.
  Local structure of multi-dimensional martingale optimal transport.
  arXiv preprint, 2018.
* [24]

  H. De March.
  Quasi-sure duality for multi-dimensional martingale optimal transport.
  arXiv preprint, 2018.
  <https://arxiv.org/abs/1805.01757>.
* [25]

  H. De March and P. Henry-Labordere.
  Building arbitrage-free implied volatility: Sinkhorn’s algorithm and variants.
  arXiv preprint, 2019.
  <https://arxiv.org/abs/1902.04456>.
* [26]

  H. De March and N. Touzi.
  Irreducible convex paving for decomposition of multidimensional martingale transport plans.
  Ann. Probab., 47(3):1726–1774, 2019.
* [27]

  Gaspard Monge.
  Mémoire sur la théorie des déblais et des remblais.
  Histoire de l’Académie Royale des Sciences de Paris, pages 666–704, 1781.
* [28]

  M. Nutz, F. Stebegg, and X. Tan.
  Multiperiod martingale transport.
  Stochastic Process. Appl., 130(3):1568–1615, 2020.
* [29]

  J. Obłój and P. Siorpaes.
  Structure of martingale transports in finite dimensions.
  arXiv preprint, 2017.
  <https://arxiv.org/abs/1702.08433>.
* [30]

  J. Obłój and P. Spoida.
  An iterated azéma-yor type embedding for finitely many marginals.
  Ann. Probab., 45(4):2210–2247, 2017.
* [31]

  F. Santambrogio.
  Optimal transport for applied mathematicians. Calculus of variations, PDEs, and modeling, volume 87 of Progress in Nonlinear Differential Equations and their Applications.
  Birkhäuser/Springer, Cham, 2015.
* [32]

  J. Sester.
  On intermediate marginals in martingale optimal transportation.
  Mathematics and financial economics, 17:615–654, 2023.
* [33]

  V. Strassen.
  The existence of probability measures with given marginals.
  Ann. Math. Statist., 36:423–439, 1965.
* [34]

  C. Villani.
  Optimal Transport. Old and New, volume 338 of Grundlehren der mathematischen Wissenschaften.
  Springer, 2009.
* [35]

  D. Zaev.
  On the monge-kantorovich problem with additional linear constraints.
  Mathematical Notes, 98(5-6):725–741, 2015.

## Acknowledgments

YS thanks colleagues at the Global Technology Applied Research center of JPMorganChase for their support and helpful discussions.
  
CC thanks colleagues at Quantitative Trading & Research of JPMorganChase for many fruitful discussions.

## Disclaimer

This paper was prepared for informational purposes with contributions from the Global Technology Applied Research center of JPMorgan Chase & Co. This paper is not a product of the Research Department of JPMorgan Chase & Co. or its affiliates. Neither JPMorgan Chase & Co. nor any of its affiliates makes any explicit or implied representation or warranty and none of them accept any liability in connection with this paper, including, without limitation, with respect to the completeness, accuracy, or reliability of the information contained herein and the potential legal, compliance, tax, or accounting effects thereof. This document is not intended as investment research or investment advice, or as a recommendation, offer, or solicitation for the purchase or sale of any security, financial instrument, financial product or service, or to be used in any way for evaluating the merits of participating in any transaction.