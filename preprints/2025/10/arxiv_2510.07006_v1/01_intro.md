---
authors:
- Jinho Cha
- Long Pham
- Thi Le Hoa Vo
- Jaeyoung Cho
- Jaejin Lee
doc_id: arxiv:2510.07006v1
family_id: arxiv:2510.07006
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization
  Approach'
url_abs: http://arxiv.org/abs/2510.07006v1
url_html: https://arxiv.org/html/2510.07006v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jinho Cha
Department of Computer Science, Gwinnett Technical College, Lawrenceville, GA, USA

Long Pham
Department of Decision Sciences and Economics, Texas A&M University–Corpus Christi, TX, USA

Thi Le Hoa Vo
Corresponding author: thi-le-hoa.vo@univ-rennes.fr
IGR-IAE Rennes, Université de Rennes, CREM UMR CNRS 6211, Rennes, France

Jaeyoung Cho
Department of Computer Science, Prairie View A&M University, Prairie View, TX, USA

Jaejin Lee
Intel Corporation, Chandler, AZ, USA

###### Abstract

This study develops and analyzes an optimization model of smart contract adoption under bounded risk,
linking structural theory with simulation and real-world validation.
We examine how adoption intensity and profitability respond to threshold costs, variance shocks, and
distributional changes. Comparative statics and Monte Carlo experiments show that adoption intensity
α⋆\alpha^{\star} is structurally pinned at a boundary solution, invariant to variance and heterogeneity,
while profitability and service outcomes are variance-fragile, eroding under volatility and heavy-tailed demand.
A sharp threshold in the fixed-cost parameter A3A\_{3} triggers discontinuous adoption collapse (H1),
variance shocks reduce profits monotonically but not adoption (H2), and additional results on readiness
heterogeneity (H3), profit–service co-benefits (H4), and distributional robustness (H5) confirm the duality
between stable adoption and fragile payoffs. External validity checks further establish convergence of
sample-average approximation at the canonical 𝒪​(1/N)\mathcal{O}(1/\sqrt{N}) rate (H6). Empirical validation using
S&P500 returns and the MovieLens-100K dataset corroborates the theoretical structure: bounded and heavy-tailed
distributions fit better than Gaussian models, and profits diverge across volatility regimes even as adoption
remains stable. Taken together, the results demonstrate that adoption choices are robust to uncertainty,
but their financial consequences are highly fragile. For operations and finance, this duality underscores the
need for risk-adjusted performance evaluation, option-theoretic modeling, and distributional stress testing in
strategic investment and supply chain design.

Keywords: Smart Contracts; Bounded Risk; Derivative Markets; Optimization; Threshold Effects; Variance Fragility; Robustness

## 1 Introduction

Derivative markets have expanded substantially in recent years, with structured products and risk-transfer instruments becoming increasingly common. These instruments allow market participants to hedge exposures and share risks more effectively, yet they also raise persistent concerns about transparency and counterparty exposure. Several financial episodes have illustrated how limited contract enforcement or monitoring can amplify systemic stress, underscoring the need for more reliable settlement mechanisms (Bolton and Dewatripont, [2005](https://arxiv.org/html/2510.07006v1#bib.bib8); Cachon, [2003](https://arxiv.org/html/2510.07006v1#bib.bib11)). In this context, digital technologies such as blockchain and smart contracts have been proposed as potential tools to enhance contract reliability and reduce frictions in clearing and settlement (Catalini and Gans, [2016](https://arxiv.org/html/2510.07006v1#bib.bib13); Cong and He, [2019](https://arxiv.org/html/2510.07006v1#bib.bib15); Schär, [2021](https://arxiv.org/html/2510.07006v1#bib.bib38)).

The idea of embedding smart contracts into derivative transactions is appealing, but adoption remains relatively limited. Market participants face a fundamental trade-off: efficiency and transparency gains must be weighed against the costs of technological implementation, integration with legacy systems, and coordination across counterparties (Tapscott and Tapscott, [2017](https://arxiv.org/html/2510.07006v1#bib.bib42)). Moreover, most existing modeling approaches assume heavy-tailed or unbounded risk distributions, which emphasize extreme events but may overstate volatility in settings where exposures are naturally capped. In practice, mechanisms such as margin rules, collateral requirements, and regulatory limits frequently impose bounds on both losses and gains (Embrechts et al., [1997](https://arxiv.org/html/2510.07006v1#bib.bib19); Johnson et al., [1995](https://arxiv.org/html/2510.07006v1#bib.bib28)).

To capture such bounded exposures in a more realistic manner, we adopt the lognormal distribution. Lognormal distributions are strictly non-negative and positively skewed, making them particularly suitable for modeling derivative exposures where downside losses are limited but upside shocks can be extreme. This property provides a natural representation of demand and settlement risk in financial markets, where asymmetry and fat tails are empirically observed (Embrechts et al., [1997](https://arxiv.org/html/2510.07006v1#bib.bib19)). Recent studies also emphasize the importance of distributional choice in variance and tail risk modeling across asset classes, reinforcing the need for flexible yet tractable specifications (Fathi, [2025](https://arxiv.org/html/2510.07006v1#bib.bib21)). Alongside robustness checks using beta distributions, this choice allows us to examine adoption incentives under realistic bounded risk environments.

The purpose of this paper is to develop a tractable optimization framework for smart contract adoption under bounded risk. We introduce an adoption intensity decision variable and formulate the associated profit maximization problem under lognormal demand. The model remains convex and analytically interpretable, which allows us to characterize optimality conditions and highlight threshold effects in adoption. In particular, we show how adoption collapses or accelerates depending on the interplay between adoption costs and supplier digital readiness.

Our analysis proceeds in two steps. First, we establish the baseline convex optimization model and derive conditions for positive adoption intensity. Second, we conduct numerical experiments using synthetic data, including sensitivity analysis with lognormal and beta demand distributions (Shapiro et al., [2014](https://arxiv.org/html/2510.07006v1#bib.bib40); Rockafellar and Uryasev, [2000](https://arxiv.org/html/2510.07006v1#bib.bib37)). This design allows us to provide comparative statics and counterfactual scenarios, including cost shocks and risk shocks, that speak directly to managerial and policy questions.

Overall, our contribution is incremental but useful. We extend the contract theory and digital adoption literature by embedding lognormal risk explicitly into the adoption decision, and by showing how threshold effects and supplier heterogeneity shape equilibrium outcomes. While our framework is stylized and based on synthetic data, it offers a transparent and interpretable foundation that can inform both future empirical validation and regulatory discussions of digital adoption in derivative markets.

Finally, based on this motivation, we formulate a set of testable hypotheses (Section [3](https://arxiv.org/html/2510.07006v1#S3 "3 Research Hypotheses ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")) that directly link adoption cost, risk variance, supplier readiness, and distributional assumptions to observable adoption outcomes. These hypotheses guide our experimental design and provide a rigorous structure for interpreting numerical results.

## 2 Literature Review

### 2.1 Financial Contract Design

The study of financial contract design has long emphasized mechanisms to align incentives and distribute risk among contracting parties. Classical models consider arrangements such as buyback contracts, revenue-sharing agreements, and quantity-flexibility provisions (Cachon, [2003](https://arxiv.org/html/2510.07006v1#bib.bib11); Lariviere and Porteus, [2001](https://arxiv.org/html/2510.07006v1#bib.bib30)). These frameworks typically assume enforcement is guaranteed through legal systems, reputation, or repeated interaction (Bolton and Dewatripont, [2005](https://arxiv.org/html/2510.07006v1#bib.bib8); Tirole, [1999](https://arxiv.org/html/2510.07006v1#bib.bib43)). More recent work has extended contract theory into supply chains and financial markets, exploring issues of renegotiation, moral hazard, and dynamic incentives (Narayanan and Raman, [2004](https://arxiv.org/html/2510.07006v1#bib.bib35); Bernheim and Whinston, [1987](https://arxiv.org/html/2510.07006v1#bib.bib7); Maskin and Tirole, [2001](https://arxiv.org/html/2510.07006v1#bib.bib33)).

A parallel stream of literature has examined incomplete contracts and relational enforcement, emphasizing the role of trust and long-term cooperation (Grossman and Hart, [1986](https://arxiv.org/html/2510.07006v1#bib.bib25); Hart and Moore, [1990](https://arxiv.org/html/2510.07006v1#bib.bib26); Baker et al., [2002](https://arxiv.org/html/2510.07006v1#bib.bib4)). These insights are particularly relevant for modern markets where counterparties are diverse, information asymmetry is prevalent, and enforcement may be imperfect.

Building on these foundations, recent studies have started to integrate digital execution and smart contracting into the analysis of contract design. For instance, Atalay et al. ([2019](https://arxiv.org/html/2510.07006v1#bib.bib3)) examine how blockchain-enabled settlement alters counterparty incentives, while Harvey et al. ([2021](https://arxiv.org/html/2510.07006v1#bib.bib27)) and Broby ([2022](https://arxiv.org/html/2510.07006v1#bib.bib9)) highlight how decentralized finance (DeFi) changes the enforcement environment by embedding rules directly into code. Very recent work such as Fanti and Kogan ([2022](https://arxiv.org/html/2510.07006v1#bib.bib20)), Chen et al. ([2023](https://arxiv.org/html/2510.07006v1#bib.bib14)), and Wang ([2025](https://arxiv.org/html/2510.07006v1#bib.bib45)) stresses the importance of bounded enforcement costs and digital readiness when contracts are executed on distributed ledgers. These contributions suggest that the adoption of smart contracts requires rethinking classical enforcement assumptions, especially in settings where risk exposures are capped by regulation or collateral.

Our work connects to this evolving stream by extending the classical contract design perspective into a digital execution setting with explicit bounded risk. In particular, we study how the introduction of smart contracts reshapes enforcement and monitoring, while also interacting with supplier heterogeneity and adoption thresholds.

### 2.2 Blockchain and Smart Contracts

The emergence of blockchain technologies introduces the possibility of programmable enforcement. Smart contracts can automate settlement, reduce transaction costs, and improve transparency (Catalini and Gans, [2016](https://arxiv.org/html/2510.07006v1#bib.bib13); Cong and He, [2019](https://arxiv.org/html/2510.07006v1#bib.bib15)). Early theoretical work emphasizes their ability to mitigate information asymmetry and reduce reliance on centralized intermediaries (Tapscott and Tapscott, [2017](https://arxiv.org/html/2510.07006v1#bib.bib42)).

Yet, adoption outcomes remain mixed. Case studies and sectoral analyses indicate substantial heterogeneity: while some industries have realized efficiency gains, others report limited improvements once integration and compliance costs are considered (Schär, [2021](https://arxiv.org/html/2510.07006v1#bib.bib38); Arora et al., [2021](https://arxiv.org/html/2510.07006v1#bib.bib2)). Empirical work in financial markets highlights that integrating blockchain into trading and derivatives settlement is non-trivial, as high implementation costs and strategic concerns frequently limit adoption (Arora et al., [2021](https://arxiv.org/html/2510.07006v1#bib.bib2)).

Recent surveys and comparative studies reinforce this point, noting that coordination costs, digital readiness, and regulatory uncertainty are persistent barriers to scaling smart contract use in finance (Shaiku et al., [2025](https://arxiv.org/html/2510.07006v1#bib.bib39); Fanti and Kogan, [2022](https://arxiv.org/html/2510.07006v1#bib.bib20)). This evidence suggests that adoption decisions are highly context-dependent and cannot be explained by efficiency gains alone. Instead, digital adoption must be analyzed jointly with risk exposure, supplier heterogeneity, and bounded enforcement environments—precisely the dimensions addressed in our optimization framework.

### 2.3 Risk Modeling in Financial Markets

A second relevant stream concerns risk modeling. Classical portfolio and contract studies often rely on normal or heavy-tailed distributions such as Pareto or lognormal to capture extreme outcomes (Embrechts et al., [1997](https://arxiv.org/html/2510.07006v1#bib.bib19); Mandelbrot, [1963](https://arxiv.org/html/2510.07006v1#bib.bib32)). While useful for systemic risk analyses, these unbounded models may overstate volatility where contractual or regulatory features cap exposures (Johnson et al., [1995](https://arxiv.org/html/2510.07006v1#bib.bib28); Glasserman, [2005](https://arxiv.org/html/2510.07006v1#bib.bib23)). In practice, mechanisms such as margin rules, collateral requirements, and regulatory limits impose upper and lower bounds on realized payoffs (Duffie et al., [2005](https://arxiv.org/html/2510.07006v1#bib.bib18); Brunnermeier and Sannikov, [2014](https://arxiv.org/html/2510.07006v1#bib.bib10)).

More recent work examines variance risk and tail properties across multiple asset classes, emphasizing how distributional choice affects inference about shocks and systemic fragility (Andersen et al., [2015](https://arxiv.org/html/2510.07006v1#bib.bib1); Barndorff-Nielsen et al., [2011](https://arxiv.org/html/2510.07006v1#bib.bib6); Fathi, [2025](https://arxiv.org/html/2510.07006v1#bib.bib21)). This literature highlights that modeling assumptions about boundedness and skewness can meaningfully change conclusions about optimal hedging and adoption incentives.

Among alternative specifications, lognormal distributions are particularly relevant because they are strictly non-negative and positively skewed, matching empirical features of derivative exposures where downside is limited but upside shocks can be large (Embrechts et al., [1997](https://arxiv.org/html/2510.07006v1#bib.bib19); Cont, [2001](https://arxiv.org/html/2510.07006v1#bib.bib16)). Beta distributions also offer flexibility in representing bounded outcomes and have been applied in option pricing and risk-limiting contracts (Carmona, [2014](https://arxiv.org/html/2510.07006v1#bib.bib12); Stoyanov et al., [2011](https://arxiv.org/html/2510.07006v1#bib.bib41)).

Yet these bounded models have been rarely integrated into the study of digital contract adoption, leaving a gap that our work addresses by embedding lognormal and beta risk explicitly into the optimization of smart contract adoption.

### 2.4 Positioning of This Study

Our work builds on these literatures in three complementary ways.

First, relative to the financial contract design literature, we extend the analysis of adoption incentives into a digital execution environment, where enforcement is programmed rather than legally adjudicated. This shift allows us to study how classical incentive alignment results change when contracts are executed by smart contracts under bounded risk.

Second, relative to blockchain adoption studies, we move beyond descriptive or case-based accounts by providing an analytical optimization framework that explicitly incorporates adoption costs, supplier readiness, and threshold effects. This enables a sharper characterization of when adoption collapses or accelerates.

Third, relative to risk modeling studies, we embed bounded lognormal risk directly into the adoption decision. Unlike prior work that focused either on incentive alignment or on digital trust, our framework highlights how convex optimization under bounded risk produces threshold adoption behavior, with clear implications for managerial decision-making and regulatory design.

## 3 Research Hypotheses

Drawing on the theoretical formulation and literature synthesis, we propose six testable hypotheses that guide our numerical experiments and empirical validation:

H1 (Threshold).
:   As adoption cost decreases, adoption intensity α\alpha exhibits a sharp jump at a critical threshold, rather than a smooth increase.
    *(Tested by varying A3A\_{3} and identifying discontinuities in α⋆\alpha^{\star}.)*

H2 (Risk–Adoption).
:   As demand variance σ\sigma increases, the optimal adoption level α⋆\alpha^{\star} increases monotonically.
    *(Tested by simulating lognormal demand with alternative variance parameters.)*

H3 (Readiness).
:   Higher average or variance in supplier readiness βi\beta\_{i} significantly increases α⋆\alpha^{\star} and expected profit.
    *(Tested by varying the support of βi\beta\_{i} across replications.)*

H4 (Service co-benefit).
:   Moderate adoption levels simultaneously improve profit and service performance (Fill Rate).
    *(Tested by computing profit–Fill Rate trade-off curves.)*

H5 (Distribution).
:   Even with the same mean and variance, heavy- vs. light-tailed distributions significantly shift the threshold location of α⋆\alpha^{\star}.
    *(Tested by comparing lognormal and beta demand distributions.)*

H6 (External validity).
:   SAA/Monte Carlo approximations converge at rate O​(1/N)O(1/\sqrt{N}) and preserve adoption thresholds as NN grows.
    *(Tested by varying sample size NN and tracking the stability of α⋆\alpha^{\star} and profit rankings.)*

Table 1: Dependency of assumptions across hypotheses (H1–H6), grouped by section

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Assumption | H1 Threshold | H2 Variance | H3 Readiness | H4 Service Co-benefit | H5 Distribution | H6 External Validity | Notes |
| Model Assumptions (Section [4](https://arxiv.org/html/2510.07006v1#S4 "4 Model Formulation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")) | | | | | | | |
| Assump. 1 (Demand regularity) | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | Continuous, finite mean demand (lognormal/beta) |
| Assump. 2 (Concavity and boundedness) | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | ✓\checkmark | Convexity, bounded optimization |
| Assump. 3 (Strict monotonicity) | ✓\checkmark |  |  |  | ✓\checkmark | ✓\checkmark | Ensures unique Q⋆Q^{\star}, threshold stability |
| Synthetic Data and Simulation (Section [5](https://arxiv.org/html/2510.07006v1#S5 "5 Synthetic Data Generation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")) | | | | | | | |
| Lognormal demand (baseline) | ✓\checkmark | ✓\checkmark |  | ✓\checkmark |  |  | Captures bounded skewed exposures |
| Beta demand (robustness) |  |  |  |  | ✓\checkmark |  | Distributional robustness check |
| Monte Carlo approximation (SAA) |  |  |  |  |  | ✓\checkmark | Convergence of simulation estimates |

## 4 Model Formulation

### 4.1 Decision Variables

#### 4.1.1 Adoption Intensity

Let α∈[0,1]\alpha\in[0,1] denote the proportion of smart-contract adoption.
Here, α=0\alpha=0 corresponds to no adoption, while α=1\alpha=1 indicates full adoption.

#### 4.1.2 Order Quantity

Let qi≥0q\_{i}\geq 0 be the order from supplier ii, and let the aggregate order be
Q=∑iqiQ=\sum\_{i}q\_{i}. The firm chooses both (qi)(q\_{i}) and α\alpha simultaneously.

### 4.2 Objective Function

We adopt a newsvendor-style expected profit formulation with salvage value s≥0s\geq 0 for overage and shortage penalty r≥0r\geq 0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxα∈[0,1],q≥0⁡Π​(α,q)\displaystyle\max\_{\alpha\in[0,1],\,q\geq 0}\ \Pi(\alpha,q) | =𝔼​[p​min⁡(Q,D)+s​(Q−D)+−r​(D−Q)+]\displaystyle=\mathbb{E}\!\Big[\,p\,\min(Q,D)\;+\;s\,(Q-D)^{+}\;-\;r\,(D-Q)^{+}\,\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −∑ic​(α,βi)​qi−ψ​(α).\displaystyle\quad-\sum\_{i}c(\alpha,\beta\_{i})\,q\_{i}\;-\;\psi(\alpha). |  | (1) |

##### Standing assumptions.

We impose three assumptions to ensure the problem is well-posed.

###### Assumption 1 (Demand regularity).

The demand DD is continuous with cumulative distribution function FF and density ff, and satisfies 𝔼​[D]<∞\mathbb{E}[D]<\infty.
This condition holds for standard families such as lognormal or truncated lognormal, which we adopt in simulations.

###### Assumption 2 (Concavity and boundedness).

Assume s≤p+rs\leq p+r and

|  |  |  |  |
| --- | --- | --- | --- |
|  | s≤c¯:=infα∈[0,1]mini⁡c​(α,βi)=mini⁡(c0​i−A1−A2​βi).s\ \leq\ \underline{c}\ :=\ \inf\_{\alpha\in[0,1]}\min\_{i}c(\alpha,\beta\_{i})\ =\ \min\_{i}\big(c\_{0i}-A\_{1}-A\_{2}\,\beta\_{i}\big). |  | (2) |

The first inequality ensures that revenue is concave in QQ, while the second prevents “salvage arbitrage”
(i.e., infinite ordering). Together, these guarantee the optimization problem is bounded and well-posed.

###### Assumption 3 (Strict monotonicity for uniqueness).

FF is strictly increasing, which is satisfied for lognormal and other continuous demand distributions.
If demand is truncated at an upper bound bb, then subgradient conditions apply at Q=bQ=b;
all subsequent results remain valid using the natural subdifferential.

##### Concavity in (Q,α)(Q,\alpha).

Define the marginal expected revenue

|  |  |  |
| --- | --- | --- |
|  | M​(Q)=∂∂Q​𝔼​[p​min⁡(Q,D)+s​(Q−D)+−r​(D−Q)+].M(Q)\;=\;\frac{\partial}{\partial Q}\,\mathbb{E}\!\Big[\,p\min(Q,D)+s(Q-D)^{+}-r(D-Q)^{+}\,\Big]. |  |

A standard calculation yields

|  |  |  |
| --- | --- | --- |
|  | M​(Q)=(p+s)​(1−F​(Q))−(r−s)​F​(Q).M(Q)=(p+s)\,(1-F(Q))-(r-s)\,F(Q). |  |

Since M​(Q)M(Q) is nonincreasing when s≤p+rs\leq p+r, the revenue function is concave in QQ.
The procurement cost term −∑ic​(α,βi)​qi-\sum\_{i}c(\alpha,\beta\_{i})q\_{i} is affine in (α,q)(\alpha,q), and the adoption cost
−ψ​(α)-\psi(\alpha) is concave since ψ​(α)\psi(\alpha) is convex.
Thus, the objective Π​(α,q)\Pi(\alpha,q) in ([1](https://arxiv.org/html/2510.07006v1#S4.E1 "In 4.2 Objective Function ‣ 4 Model Formulation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")) is concave in (Q,α)(Q,\alpha) over the convex feasible region.
The problem therefore reduces to a convex optimization, ensuring existence of a global maximizer.

##### First-order conditions.

The optimal order Q⋆Q^{\star} satisfies the critical fractile condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(Q⋆)=p−sp+r−s,F(Q^{\star})\;=\;\frac{p-s}{p+r-s}, |  | (3) |

which is the standard newsvendor solution, independent of α\alpha.
Thus, adoption does not affect Q⋆Q^{\star} directly, but only indirectly through the effective cost structure.
Given Q⋆Q^{\star}, the optimal adoption α⋆\alpha^{\star} solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxα∈[0,1]−(c0−A1​α−A2​β¯)​Q⋆−A3​αν,\max\_{\alpha\in[0,1]}\;-\Big(c\_{0}-A\_{1}\alpha-A\_{2}\bar{\beta}\Big)Q^{\star}\;-\;A\_{3}\alpha^{\nu}, |  | (4) |

where β¯\bar{\beta} is the mean readiness across suppliers.
The first-order condition for interior α\alpha is

|  |  |  |
| --- | --- | --- |
|  | A1​Q⋆=ν​A3​αν−1.A\_{1}Q^{\star}=\nu A\_{3}\alpha^{\nu-1}. |  |

If this equality cannot be satisfied within α∈[0,1]\alpha\in[0,1], the solution collapses to the boundary α⋆=0\alpha^{\star}=0 or α⋆=1\alpha^{\star}=1.
In our calibration, the inequality holds only at the lower boundary, producing the corner solution α⋆=0.05\alpha^{\star}=0.05 observed in simulation.

### 4.3 Cost Functions

#### 4.3.1 Procurement Cost

We assume the effective unit cost from supplier ii decreases both with adoption intensity α\alpha
and supplier readiness βi\beta\_{i}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(α,βi)=c0​i−A1​α−A2​βi,c(\alpha,\beta\_{i})\;=\;c\_{0i}-A\_{1}\,\alpha-A\_{2}\,\beta\_{i}, |  | (5) |

where c0​ic\_{0i} is the baseline procurement cost, A1>0A\_{1}>0 measures marginal cost reduction from adoption,
and A2>0A\_{2}>0 captures the effect of supplier readiness.
Hence, higher adoption and greater readiness jointly lower effective procurement costs.

#### 4.3.2 Adoption Cost

Adoption incurs a convex integration cost:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(α)=A3​αν,A3>0,ν>1,\psi(\alpha)\;=\;A\_{3}\,\alpha^{\nu},\qquad A\_{3}>0,\;\;\nu>1, |  | (6) |

so that ψ\psi is increasing and strictly convex in α\alpha.
This form captures the empirically observed fact that marginal integration costs rise
with adoption intensity due to compatibility and coordination frictions.

### 4.4 Risk Distribution

#### 4.4.1 Lognormal Demand (with optional cap)

Market demand DD is assumed to follow a positively skewed, nonnegative distribution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D∼Lognormal​(m,v),with cumulative distribution function ​F​(⋅).D\;\sim\;\mathrm{Lognormal}(m,v),\qquad\text{with cumulative distribution function }F(\cdot). |  | (7) |

The lognormal captures both nonnegativity and heavy right tails,
consistent with empirical evidence on derivative exposures.

If institutional or contractual caps apply, we instead consider the truncated form

|  |  |  |  |
| --- | --- | --- | --- |
|  | D~=min⁡{D,b},\tilde{D}\;=\;\min\{D,b\}, |  | (8) |

where b>0b>0 is the upper bound. At Q=bQ=b, first-order conditions are interpreted in terms of the natural
subdifferential of FF (see Assumption (A3)).

### 4.5 Analytic Derivatives and KKT System

#### 4.5.1 Marginal Expected Revenue in QQ

###### Lemma 1 (Marginal revenue in aggregate order).

Suppose Assumptions (A1)–(A2) hold and DD is continuous with CDF FF and PDF ff.
Then the derivative of the expected stage revenue with respect to QQ is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂∂Q​𝔼​[p​min⁡(Q,D)+s​(Q−D)+−r​(D−Q)+]\displaystyle\frac{\partial}{\partial Q}\,\mathbb{E}\!\left[p\min(Q,D)+s(Q-D)^{+}-r(D-Q)^{+}\right] | =(p+r)​(1−F​(Q))\displaystyle=(p+r)\big(1-F(Q)\big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +sF(Q)=:M(Q).\displaystyle\quad+\;s\,F(Q)\;=:\;M(Q). |  | (9) |

Moreover, M′​(Q)=(s−(p+r))​f​(Q)≤0M^{\prime}(Q)=(s-(p+r))f(Q)\leq 0 when s≤p+rs\leq p+r.
Hence the expected revenue is concave in QQ, strictly concave when s<p+rs<p+r and f​(Q)>0f(Q)>0 on a set of positive measure.

###### Proof.

By dominated convergence, differentiation under the expectation is valid.
For any QQ at continuity points of FF:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dd​Q​min⁡(Q,D)\displaystyle\frac{d}{dQ}\min(Q,D) | =𝟙​{D≥Q},\displaystyle=\mathbbm{1}\{D\geq Q\}, |  | (10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dd​Q​(Q−D)+\displaystyle\frac{d}{dQ}(Q-D)^{+} | =𝟙​{Q>D},\displaystyle=\mathbbm{1}\{Q>D\}, |  | (11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dd​Q​(D−Q)+\displaystyle\frac{d}{dQ}(D-Q)^{+} | =− 1​{D>Q}.\displaystyle=-\,\mathbbm{1}\{D>Q\}. |  | (12) |

Taking expectations yields

|  |  |  |
| --- | --- | --- |
|  | p​ℙ​(D≥Q)+s​ℙ​(D<Q)+r​ℙ​(D>Q).p\,\mathbb{P}(D\geq Q)+s\,\mathbb{P}(D<Q)+r\,\mathbb{P}(D>Q). |  |

Since DD is continuous, ℙ​(D≥Q)=ℙ​(D>Q)=1−F​(Q)\mathbb{P}(D\geq Q)=\mathbb{P}(D>Q)=1-F(Q) and ℙ​(D<Q)=F​(Q)\mathbb{P}(D<Q)=F(Q).
Therefore

|  |  |  |
| --- | --- | --- |
|  | M​(Q)=(p+r)​(1−F​(Q))+s​F​(Q).M(Q)=(p+r)(1-F(Q))+sF(Q). |  |

Differentiating gives M′​(Q)=(s−(p+r))​f​(Q)M^{\prime}(Q)=(s-(p+r))f(Q), which is weakly negative whenever s≤p+rs\leq p+r.
Thus expected revenue is concave in QQ and strictly concave when s<p+rs<p+r with f​(Q)>0f(Q)>0 on a set of positive measure.
∎

##### Interpretation.

The marginal revenue M​(Q)M(Q) declines monotonically in QQ, exactly as in the newsvendor model.
Hence the optimal order size equates this decreasing curve with supplier costs.
This provides the basis for the KKT characterization below.

Using M​(Q)M(Q), the stationarity condition for each supplier order qiq\_{i} (multiplier λi≥0\lambda\_{i}\geq 0 for qi≥0q\_{i}\geq 0) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂Π∂qi=M​(Q)⋅∂Q∂qi−c​(α,βi)+λi=M​(Q)−c​(α,βi)+λi=0,\frac{\partial\Pi}{\partial q\_{i}}=M(Q)\cdot\frac{\partial Q}{\partial q\_{i}}-c(\alpha,\beta\_{i})+\lambda\_{i}=M(Q)-c(\alpha,\beta\_{i})+\lambda\_{i}=0, |  | (13) |

with complementary slackness λi​qi=0\lambda\_{i}q\_{i}=0 and feasibility qi≥0q\_{i}\geq 0.

##### Active-set characterization.

At the optimum, any supplier ii with qi>0q\_{i}>0 must satisfy

|  |  |  |
| --- | --- | --- |
|  | c​(α,βi)=M​(Q⋆),c(\alpha,\beta\_{i})=M(Q^{\star}), |  |

while suppliers with qi=0q\_{i}=0 satisfy c​(α,βi)≥M​(Q⋆)c(\alpha,\beta\_{i})\geq M(Q^{\star}).
*In the absence of capacity constraints*, this implies that orders concentrate on the cheapest suppliers mini⁡c​(α,βi)\min\_{i}c(\alpha,\beta\_{i}), with proportional allocation in case of ties.111If diversification is required, one can impose supplier capacities 0≤qi≤q¯i0\leq q\_{i}\leq\bar{q}\_{i} or introduce convex supplier-specific cost functions. The KKT characterization extends directly.

### 4.6 Optimal adoption intensity α⋆\alpha^{\star}

###### Proposition 1 (Closed-form solution for α⋆\alpha^{\star}).

Let Assumptions (A1)–(A3) hold. Then the KKT condition for adoption intensity is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂Π∂α=A1​∑iqi−ψ′​(α)+γ+−γ−=0,\frac{\partial\Pi}{\partial\alpha}=A\_{1}\sum\_{i}q\_{i}-\psi^{\prime}(\alpha)+\gamma^{+}-\gamma^{-}=0, |  | (14) |

with multipliers γ+≥0\gamma^{+}\geq 0 (for α≤1\alpha\leq 1) and γ−≥0\gamma^{-}\geq 0 (for α≥0\alpha\geq 0).

The optimal adoption intensity is

|  |  |  |  |
| --- | --- | --- | --- |
|  | α⋆={0,if ​ψ′​(0+)≥A1​∑iqi,1,if ​ψ′​(1−)≤A1​∑iqi,(A1​∑iqiA3​ν)1ν−1,otherwise.\alpha^{\star}=\begin{cases}0,&\text{if }\ \psi^{\prime}(0^{+})\ \geq A\_{1}\sum\_{i}q\_{i},\\[5.69054pt] 1,&\text{if }\ \psi^{\prime}(1^{-})\ \leq A\_{1}\sum\_{i}q\_{i},\\[5.69054pt] \left(\dfrac{A\_{1}\sum\_{i}q\_{i}}{A\_{3}\,\nu}\right)^{\!\frac{1}{\nu-1}},&\text{otherwise}.\end{cases} |  | (15) |

In particular, when ψ​(α)=A3​αν\psi(\alpha)=A\_{3}\alpha^{\nu} with ν>1\nu>1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | αint⋆=(A1​∑iqiA3​ν)1ν−1,α⋆=min⁡{1,max⁡{0,αint⋆}}.\alpha^{\star}\_{\mathrm{int}}=\left(\frac{A\_{1}\sum\_{i}q\_{i}}{A\_{3}\,\nu}\right)^{\!\frac{1}{\nu-1}},\qquad\alpha^{\star}=\min\{1,\max\{0,\alpha^{\star}\_{\mathrm{int}}\}\}. |  | (16) |

###### Proof.

If α∈(0,1)\alpha\in(0,1), both multipliers vanish (γ+=γ−=0\gamma^{+}=\gamma^{-}=0), and the stationarity condition reduces to ψ′​(α)=A1​∑iqi\psi^{\prime}(\alpha)=A\_{1}\sum\_{i}q\_{i}.
For ψ​(α)=A3​αν\psi(\alpha)=A\_{3}\alpha^{\nu}, we have ψ′​(α)=A3​ν​αν−1\psi^{\prime}(\alpha)=A\_{3}\nu\alpha^{\nu-1}.
Thus the interior solution is

|  |  |  |
| --- | --- | --- |
|  | αint⋆=(A1​∑iqiA3​ν)1/(ν−1).\alpha^{\star}\_{\mathrm{int}}=\left(\frac{A\_{1}\sum\_{i}q\_{i}}{A\_{3}\nu}\right)^{1/(\nu-1)}. |  |

Feasibility requires α∈[0,1]\alpha\in[0,1], so the admissible solution is

|  |  |  |
| --- | --- | --- |
|  | α⋆=min⁡{1,max⁡{0,αint⋆}}.\alpha^{\star}=\min\{1,\max\{0,\alpha^{\star}\_{\mathrm{int}}\}\}. |  |

If A1​∑iqi≤ψ′​(0+)A\_{1}\sum\_{i}q\_{i}\leq\psi^{\prime}(0^{+}), the marginal benefit is too small, and α⋆=0\alpha^{\star}=0.
If A1​∑iqi≥ψ′​(1−)A\_{1}\sum\_{i}q\_{i}\geq\psi^{\prime}(1^{-}), the marginal benefit dominates cost even at α=1\alpha=1, so α⋆=1\alpha^{\star}=1.
Otherwise the interior value applies.
∎

##### Interpretation.

Proposition [1](https://arxiv.org/html/2510.07006v1#Thmproposition1 "Proposition 1 (Closed-form solution for 𝛼^⋆). ‣ 4.6 Optimal adoption intensity 𝛼^⋆ ‣ 4 Model Formulation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") highlights the threshold nature of adoption.
If procurement efficiency is weak, adoption collapses to zero.
If efficiency is very strong, adoption jumps to full intensity.
In between, adoption scales smoothly with order volume.
In baseline calibration, however, the inequality usually binds at the lower bound, so α⋆\alpha^{\star} remains at the corner solution—explaining the empirical robustness observed in H1–H5.

#### 4.6.1 Threshold (Corner) Rules

###### Proposition 2 (Threshold adoption behavior).

From the KKT condition ([14](https://arxiv.org/html/2510.07006v1#S4.E14 "In Proposition 1 (Closed-form solution for 𝛼^⋆). ‣ 4.6 Optimal adoption intensity 𝛼^⋆ ‣ 4 Model Formulation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")), the optimal adoption intensity satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | α⋆={0,if ​ψ′​(0+)≥A1​∑iqi,1,if ​ψ′​(1−)≤A1​∑iqi,(A1​∑iqiA3​ν)1ν−1,otherwise.\alpha^{\star}=\begin{cases}0,&\text{if }\ \psi^{\prime}(0^{+})\ \geq\ A\_{1}\sum\_{i}q\_{i},\\[5.69054pt] 1,&\text{if }\ \psi^{\prime}(1^{-})\ \leq\ A\_{1}\sum\_{i}q\_{i},\\[5.69054pt] \left(\dfrac{A\_{1}\sum\_{i}q\_{i}}{A\_{3}\,\nu}\right)^{\!\frac{1}{\nu-1}},&\text{otherwise.}\end{cases} |  | (17) |

In particular, for power costs ψ​(α)=A3​αν\psi(\alpha)=A\_{3}\alpha^{\nu} with ν>1\nu>1, we have ψ′​(0+)=0\psi^{\prime}(0^{+})=0, so α⋆=0\alpha^{\star}=0 only if ∑iqi=0\sum\_{i}q\_{i}=0.
Conversely, a “full-adoption collapse” α⋆=1\alpha^{\star}=1 occurs whenever A1​∑iqi≥A3​νA\_{1}\sum\_{i}q\_{i}\geq A\_{3}\nu.

##### Interpretation.

Proposition [2](https://arxiv.org/html/2510.07006v1#Thmproposition2 "Proposition 2 (Threshold adoption behavior). ‣ 4.6.1 Threshold (Corner) Rules ‣ 4.6 Optimal adoption intensity 𝛼^⋆ ‣ 4 Model Formulation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") formalizes the corner-solution dynamics observed in our simulations.
If order volumes are too low, the marginal cost of adoption dominates, forcing α⋆=0\alpha^{\star}=0.
If order volumes are sufficiently high, the adoption cost becomes negligible relative to procurement gains, producing α⋆=1\alpha^{\star}=1.
Between these two extremes lies an interior regime in which adoption scales continuously with ∑iqi\sum\_{i}q\_{i}.
This threshold logic explains why adoption responses can appear robust over wide parameter regions but collapse discontinuously when certain boundaries are crossed.

### 4.7 Equivalent Convex SAA Formulation (Implementation Ready)

To accommodate general demand distributions DD, we employ a Sample Average Approximation (SAA) with i.i.d. draws D(n)D^{(n)}, n=1,…,Nn=1,\dots,N.
For each sample, we introduce auxiliary variables (yn,zn,un)(y\_{n},z\_{n},u\_{n}) that encode realized sales, overage, and shortage through the linear constraints:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | yn\displaystyle y\_{n} | ≤Q,\displaystyle\leq Q, | yn\displaystyle y\_{n} | ≤D(n),\displaystyle\leq D^{(n)}, | yn\displaystyle y\_{n} | ≥0,\displaystyle\geq 0, |  | (18) |
|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | zn\displaystyle z\_{n} | ≥Q−D(n),\displaystyle\geq Q-D^{(n)}, | zn\displaystyle z\_{n} | ≥0,\displaystyle\geq 0, |  | | | (19) |
|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | un\displaystyle u\_{n} | ≥D(n)−Q,\displaystyle\geq D^{(n)}-Q, | un\displaystyle u\_{n} | ≥0.\displaystyle\geq 0. |  | | | (20) |

These variables ensure that the nonlinear expressions in the expected revenue are replaced by linear inequalities that hold scenario by scenario.

The resulting finite-dimensional SAA problem takes the form:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | maxα∈[0,1],q≥0,Q=∑iqi,y,z,u\displaystyle\max\_{\alpha\in[0,1],\,q\geq 0,\,Q=\sum\_{i}q\_{i},\,y,z,u} | 1N​∑n=1N(p​yn+s​zn−r​un)−∑ic​(α,βi)​qi−ψ​(α)\displaystyle\frac{1}{N}\sum\_{n=1}^{N}\big(p\,y\_{n}+s\,z\_{n}-r\,u\_{n}\big)-\sum\_{i}c(\alpha,\beta\_{i})\,q\_{i}-\psi(\alpha) |  | (21) |
|  | subject to | constraints ([18](https://arxiv.org/html/2510.07006v1#S4.E18 "In 4.7 Equivalent Convex SAA Formulation (Implementation Ready) ‣ 4 Model Formulation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach"))−−([20](https://arxiv.org/html/2510.07006v1#S4.E20 "In 4.7 Equivalent Convex SAA Formulation (Implementation Ready) ‣ 4 Model Formulation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach"))∀n=1,…,N.\displaystyle\text{constraints }\eqref{eq:yn}--\eqref{eq:un}\quad\forall n=1,\ldots,N. |  |

##### Convexity.

The feasible region defined by ([18](https://arxiv.org/html/2510.07006v1#S4.E18 "In 4.7 Equivalent Convex SAA Formulation (Implementation Ready) ‣ 4 Model Formulation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach"))–([20](https://arxiv.org/html/2510.07006v1#S4.E20 "In 4.7 Equivalent Convex SAA Formulation (Implementation Ready) ‣ 4 Model Formulation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")) is polyhedral and therefore convex.
The objective consists of the sample average of linear functions of (yn,zn,un,Q)(y\_{n},z\_{n},u\_{n},Q) combined with the concave term −ψ​(α)-\psi(\alpha).
Consequently, problem ([21](https://arxiv.org/html/2510.07006v1#S4.E21 "In 4.7 Equivalent Convex SAA Formulation (Implementation Ready) ‣ 4 Model Formulation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")) is a concave maximization over a convex set, i.e., a convex optimization problem in the standard sense.
This guarantees both tractability and the existence of globally optimal solutions.

##### Asymptotic equivalence.

As the sample size NN grows, the law of large numbers ensures that the SAA objective converges almost surely to the expected profit in ([1](https://arxiv.org/html/2510.07006v1#S4.E1 "In 4.2 Objective Function ‣ 4 Model Formulation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")).
In addition, by classical results on epi-convergence in stochastic programming, the optimal value and the Karush–Kuhn–Tucker conditions of the SAA problem converge to those of the population problem ([13](https://arxiv.org/html/2510.07006v1#S4.E13 "In Interpretation. ‣ 4.5.1 Marginal Expected Revenue in 𝑄 ‣ 4.5 Analytic Derivatives and KKT System ‣ 4 Model Formulation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach"))–([14](https://arxiv.org/html/2510.07006v1#S4.E14 "In Proposition 1 (Closed-form solution for 𝛼^⋆). ‣ 4.6 Optimal adoption intensity 𝛼^⋆ ‣ 4 Model Formulation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")).
Thus, the SAA provides both a statistically consistent and computationally implementable formulation.

##### Comparative statics.

The SAA framework also makes the comparative statics of the model transparent.
An increase in adoption intensity α\alpha lowers procurement costs c​(α,βi)c(\alpha,\beta\_{i}) and expands the set of active suppliers, raising the equilibrium order quantity Q⋆Q^{\star} until the marginal revenue condition M​(Q⋆)=c​(α,βi)M(Q^{\star})=c(\alpha,\beta\_{i}) is restored.
Higher supplier readiness βi\beta\_{i} further decreases effective costs, making more suppliers competitive and shaping the extensive margin of participation.
Shifts in the demand distribution also matter: a higher log-mean mm raises marginal revenue and expands Q⋆Q^{\star}, whereas higher log-variance vv thickens the right tail of demand, amplifying exposure to upside shocks.
Finally, the closed-form solution for α⋆\alpha^{\star} highlights corner thresholds: when order volumes are negligible, adoption collapses to zero, whereas when procurement benefits are sufficiently large (A1​∑iqi≥A3​νA\_{1}\sum\_{i}q\_{i}\geq A\_{3}\nu), full adoption emerges.
These thresholds generate discontinuities in adoption dynamics and explain the robustness-versus-fragility patterns documented in the empirical results.

## 5 Synthetic Data Generation

To evaluate the proposed model under controlled yet realistic conditions,
we construct a synthetic dataset that mirrors key features of derivative
transactions under bounded risk. The design introduces heterogeneity in
both market demand and supplier readiness, while enabling systematic
exploration of contract-parameter sensitivity. This facilitates
reproducibility and supports counterfactual experiments that would be
infeasible with proprietary data.

### 5.1 Demand Simulation

#### 5.1.1 Distributional Assumptions

Market demand DD is modeled as lognormal to capture non-negativity,
right skewness, and heavy tails:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D∼Lognormal​(μ,σ2),D∈[a,b].D\sim\mathrm{Lognormal}(\mu,\sigma^{2}),\qquad D\in[a,b]. |  | (22) |

Baseline calibration uses μ=50\mu=50, σ=8\sigma=8, truncated to [30,70][30,70]
to reflect regulatory/contractual limits. For distributional robustness
(H5), we additionally compare against a Beta family calibrated on the
same support.

#### 5.1.2 Monte Carlo Approximation

Expected values in the objective are approximated by Monte Carlo:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[g​(D)]≈1N​∑n=1Ng​(D(n)),D(n)​∼i.i.d.​Lognormal​(μ,σ2).\mathbb{E}[g(D)]\approx\frac{1}{N}\sum\_{n=1}^{N}g(D^{(n)}),\qquad D^{(n)}\overset{\mathrm{i.i.d.}}{\sim}\mathrm{Lognormal}(\mu,\sigma^{2}). |  | (23) |

Unless otherwise noted, we use N=10,000N=10{,}000 draws per experiment. In H6
we explicitly vary N∈{1,000,5,000,20,000}N\in\{1{,}000,5{,}000,20{,}000\} and document
convergence.

### 5.2 Supplier Readiness

#### 5.2.1 Heterogeneity in Digital Capabilities

Each supplier ii is assigned a readiness index βi\beta\_{i}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | βi∼U​(0.3,0.7).\beta\_{i}\sim U(0.3,0.7). |  | (24) |

For H3, we vary the support to U​(0.1,0.9)U(0.1,0.9) and U​(0.4,0.6)U(0.4,0.6) to probe
how broader/narrower heterogeneity shifts outcomes.

### 5.3 Contract Parameters

#### 5.3.1 Baseline Calibration

Baseline contract terms are

|  |  |  |  |
| --- | --- | --- | --- |
|  | c0​i=100,A1=5,A2=8,A3=2000,ν>1,c\_{0i}=100,\quad A\_{1}=5,\quad A\_{2}=8,\quad A\_{3}=2000,\quad\nu>1, |  | (25) |

with adoption cost ψ​(α)=A3​αν\psi(\alpha)=A\_{3}\alpha^{\nu}. Under this baseline,
the optimal adoption settles at the corner α⋆=0.05\alpha^{\star}=0.05; interior
solutions emerge only after targeted parameter shifts (e.g., lowering
A3A\_{3} or ν\nu, or increasing A1A\_{1}).

Table 2: Summary of simulation parameters actually used: baseline values, variation ranges, and associated hypotheses (H1–H6).

|  |  |  |  |
| --- | --- | --- | --- |
| Parameter | Baseline | Variation Range | Purpose / Hypothesis |
| Demand mean μ\mu | 50 | Fixed | Scale normalization |
| Demand std. σ\sigma | 8 | {5,10,15}\{5,10,15\} | Variance effects (H2) |
| Demand cap [a,b][a,b] | [30,70][30,70] | ±10\pm 10 | Robustness to bounds |
| Supplier readiness βi\beta\_{i} | U​(0.3,0.7)U(0.3,0.7) | U​(0.1,0.9)U(0.1,0.9), U​(0.4,0.6)U(0.4,0.6) | Heterogeneity (H3) |
| Procurement cost c0​ic\_{0i} | 100 | Fixed | Normalization |
| Adoption cost A3A\_{3} | 2000 | {500,2000,4000}\{500,2000,4000\} | Threshold effects (H1) |
| Adoption scale A1A\_{1} | 5 | ±25%\pm 25\% | Service co-benefit / sensitivity (H4) |
| Readiness weight A2A\_{2} | 8 | ±25%\pm 25\% | Service co-benefit / sensitivity (H4) |
| Convexity ν\nu | >1>1 | {1.5,2,3}\{1.5,2,3\} | Convexity check (H1 robustness) |
| Demand distribution | Lognormal | Beta (same support) | Distributional robustness (H5) |
| Monte Carlo size NN | 10,000 | {1,000,5,000,20,000}\{1{,}000,5{,}000,20{,}000\} | Convergence of SAA estimates (H6) |

#### 5.3.2 Sensitivity and Robustness

We vary (A1,A2)(A\_{1},A\_{2}) by ±25%\pm 25\% and A3∈{500,2000,4000}A\_{3}\in\{500,2000,4000\} to map
threshold behavior (H1) and service co-benefits (H4). Distributional
robustness (H5) is assessed by comparing lognormal versus Beta demand on
[a,b][a,b].

### 5.4 Replication Protocol

Replication counts follow the actual experiments:
H1/H4 use bootstrap B=200B=200;
H2 uses B=100B=100 over σ∈{5,10,15}\sigma\in\{5,10,15\};
H3 runs 5050 replicates per (mean,var)(\mathrm{mean},\mathrm{var}) setting;
H5 uses R=200R=200 repetitions per distribution family;
H6 evaluates 3030 repetitions per N∈{1,000,5,000,20,000}N\in\{1{,}000,5{,}000,20{,}000\}.
Distinct seeds are used across runs; all intermediate CSVs and figures
reported in the paper are generated from these runs.

Algorithm 1  Convex SAA Solver via Mirror Descent

1:

* •

  Convex feasible parameter set Θ⊆ℝd\Theta\subseteq\mathbb{R}^{d}
* •

  Step size schedule {ηt}t=1T\{\eta\_{t}\}\_{t=1}^{T}
* •

  Strongly convex regularizer ψ:Θ→ℝ\psi:\Theta\to\mathbb{R} inducing Bregman divergence

  |  |  |  |
  | --- | --- | --- |
  |  | Dψ​(u∥v)=ψ​(u)−ψ​(v)−⟨∇ψ​(v),u−v⟩D\_{\psi}(u\|\;v)=\psi(u)-\psi(v)-\langle\nabla\psi(v),u-v\rangle |  |
* •

  i.i.d. sampled scenarios {(Bt,qt,x~t)}t=1T\{(B\_{t},q\_{t},\tilde{x}\_{t})\}\_{t=1}^{T}

2:

* •

  Parameter trajectory {θ^t}t=1T\{\hat{\theta}\_{t}\}\_{t=1}^{T} approximating the SAA solution

  |  |  |  |
  | --- | --- | --- |
  |  | minθ∈Θ⁡1T​∑t=1Tℓt​(θ),ℓt​(θ)=‖xt⋆​(θ)−x~t‖2.\min\_{\theta\in\Theta}\;\tfrac{1}{T}\sum\_{t=1}^{T}\ell\_{t}(\theta),\quad\ell\_{t}(\theta)=\|x\_{t}^{\star}(\theta)-\tilde{x}\_{t}\|^{2}. |  |

3:Initialize θ^1∈Θ\hat{\theta}\_{1}\in\Theta

4:for t=1t=1 to TT do

5:  Solve forward allocation xt⋆​(θ^t)x\_{t}^{\star}(\hat{\theta}\_{t})

6:  Compute instantaneous loss ℓt​(θ)\ell\_{t}(\theta) and subgradient gt∈∂θℓt​(θ^t)g\_{t}\in\partial\_{\theta}\ell\_{t}(\hat{\theta}\_{t})

7:Update by mirror descent:

|  |  |  |
| --- | --- | --- |
|  | θ^t+1←arg⁡minθ∈Θ⁡{⟨gt,θ⟩+1ηt​Dψ​(θ∥θ^t)}\hat{\theta}\_{t+1}\leftarrow\arg\min\_{\theta\in\Theta}\{\langle g\_{t},\theta\rangle+\tfrac{1}{\eta\_{t}}D\_{\psi}(\theta\|\hat{\theta}\_{t})\} |  |

8:  if ψ​(θ)=12​‖θ‖2\psi(\theta)=\tfrac{1}{2}\|\theta\|^{2} then

9:   Projected OGD: θ^t+1=ΠΘ​(θ^t−ηt​gt)\hat{\theta}\_{t+1}=\Pi\_{\Theta}(\hat{\theta}\_{t}-\eta\_{t}g\_{t})

10:  else

11:   General mirror descent step

12:  end if

13:end for

14:Return: trajectory {θ^t}t=1T\{\hat{\theta}\_{t}\}\_{t=1}^{T}

Theoretical Guarantees.
Suppose Assumptions (convexity, PL-inequality, KKT regularity, bounded subgradients, sub-Gaussian noise) hold and ηt=η/t\eta\_{t}=\eta/\sqrt{t}. Then with high probability:

|  |  |  |
| --- | --- | --- |
|  | Static Regret=𝒪​(T),Dynamic Regret=𝒪​(T+VT),‖θ^−θ⋆‖=𝒪​(1T),\text{Static Regret}=\mathcal{O}(\sqrt{T}),\quad\text{Dynamic Regret}=\mathcal{O}(\sqrt{T}+V\_{T}),\quad\|\hat{\theta}-\theta^{\star}\|=\mathcal{O}\!\big(\tfrac{1}{\sqrt{T}}\big), |  |

where VT=∑t=2T‖θt−θt−1‖V\_{T}=\sum\_{t=2}^{T}\|\theta\_{t}-\theta\_{t-1}\| is the variation budget. Thus the estimator is consistent, drift-robust, and statistically stable for the convex SAA problem.

As shown in Algorithm [1](https://arxiv.org/html/2510.07006v1#alg1 "Algorithm 1 ‣ 5.4 Replication Protocol ‣ 5 Synthetic Data Generation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach"), the solver updates parameters
iteratively using stochastic subgradients and Bregman projections.
This routine guarantees sublinear regret bounds and stability under
drift and noise, and thus serves as the computational backbone for
the experiments reported in Section [6](https://arxiv.org/html/2510.07006v1#S6 "6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach").

## 6 Numerical Experiments

We conduct numerical experiments to test hypotheses H1–H6.
Unless stated otherwise, all experiments use baseline calibration
(μ=50\mu=50, σ=8\sigma=8, c0​i=100c\_{0i}=100, A1=5A\_{1}=5, A2=8A\_{2}=8, A3=2000A\_{3}=2000, ν=2\nu=2, p=120p=120, s=10s=10, r=20r=20),
with R=100R=100 replications and N=10,000N=10{,}000 Monte Carlo draws.

Independent random seeds are used for each replication, ensuring reproducibility.
We primarily adopt a one-at-a-time (OAT) design for interpretability, but selected two-way interactions
(e.g., σ×A3\sigma\times A\_{3}) were also tested and found not to alter qualitative results.
All reported pp-values are adjusted using a false discovery rate (FDR) correction to mitigate
multiple-comparison bias.222Results with Bonferroni correction are reported in the Supplement, Table S1.

### 6.1 H1 and H4: Threshold and Service Co-Benefit

#### 6.1.1 Profit and Service Surfaces

![Refer to caption](Fig1.png)


Figure 1: Baseline results (H1, H4).
(a) Profit surface (Q,α)(Q,\alpha).
(b) Fill Rate surface (Q,α)(Q,\alpha).
(c) Profit–Fill Rate frontier (bootstrap).
(d) Adoption threshold jump as a function of A3A\_{3}.

As shown in Figure [1](https://arxiv.org/html/2510.07006v1#S6.F1 "Figure 1 ‣ 6.1.1 Profit and Service Surfaces ‣ 6.1 H1 and H4: Threshold and Service Co-Benefit ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach"), the baseline landscape illustrates both
the concavity of the profit surface in (Q,α)(Q,\alpha) and the monotone improvement in
service performance (Fill Rate) as order quantities increase. The profit–fill rate
frontier further highlights a narrow “co-benefit zone” where both profit and service
outcomes improve simultaneously, consistent with hypothesis H4. Panel (d) confirms
a discontinuous jump in adoption intensity as adoption cost A3A\_{3} crosses the threshold,
providing direct evidence for H1.

#### 6.1.2 Comparative Statics of Adoption

To complement the baseline results,
Figure [2](https://arxiv.org/html/2510.07006v1#S6.F2 "Figure 2 ‣ 6.1.2 Comparative Statics of Adoption ‣ 6.1 H1 and H4: Threshold and Service Co-Benefit ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") illustrates how the optimal adoption intensity
α⋆\alpha^{\star} changes as the key structural parameters vary.
Specifically, panel (a) shows that α⋆\alpha^{\star} collapses as adoption cost A3A\_{3}
increases beyond a critical threshold, panel (b) demonstrates the positive effect
of procurement efficiency A1A\_{1}, and panel (c) shows how greater convexity ν\nu
dampens adoption.
These comparative statics confirm that the discontinuous adoption behavior observed
in Figure [1](https://arxiv.org/html/2510.07006v1#S6.F1 "Figure 1 ‣ 6.1.1 Profit and Service Surfaces ‣ 6.1 H1 and H4: Threshold and Service Co-Benefit ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") is not a numerical artifact, but rather a
structural feature of the model.

![Refer to caption](Fig2.png)


Figure 2: Comparative statics of optimal adoption intensity
α⋆\alpha^{\star} (Figure 1.2).
Panel (a) shows collapse as adoption cost A3A\_{3} rises,
(b) illustrates the increase with procurement efficiency A1A\_{1},
and (c) demonstrates the dampening effect of convexity ν\nu.
Red dashed lines indicate baseline calibration values.

#### 6.1.3 Bootstrap Summary Statistics

Table [3](https://arxiv.org/html/2510.07006v1#S6.T3 "Table 3 ‣ 6.1.3 Bootstrap Summary Statistics ‣ 6.1 H1 and H4: Threshold and Service Co-Benefit ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") summarizes baseline calibration statistics.
Expected profit is highly stable across bootstrap replications (mean = 904.7,
95% CI [899.2, 910.8]), while adoption intensity α⋆\alpha^{\star} converges to
a unique corner solution at 0.050.05 in all runs. The optimal order quantity
Q⋆≈45.7Q^{\star}\approx 45.7 and fill rate ≈0.88\approx 0.88 remain tightly concentrated,
demonstrating that both economic and service outcomes are robust to sampling variation.
Taken together, these results establish the empirical basis for hypotheses H1 and H4.

Table 3: Baseline calibration (H1, H4).
Reported values are bootstrap means over R=100R=100 replications with N=10,000N=10{,}000 samples each.
Standard deviations (Std) reflect sampling variability, and confidence intervals (CI) are bias-corrected percentiles
from 200 bootstrap resamples.
Adoption intensity α⋆\alpha^{\star} converges to a unique corner solution across all replications,
indicating robustness of the threshold effect.
All pp-values are adjusted using false discovery rate (FDR) correction.

|  | Mean | Std | 2.5% | 97.5% |
| --- | --- | --- | --- | --- |
| Profit (expected units) | 904.706 | 2.807 | 899.245 | 910.833 |
| Adoption α⋆\alpha^{\star} | 0.050 | 0.000 | 0.050 | 0.050 |
| Order Q⋆Q^{\star} | 45.685 | 0.466 | 45.000 | 46.000 |
| Fill Rate | 0.879 | 0.006 | 0.869 | 0.885 |

### 6.2 H2: Variance Effects

#### 6.2.1 Adoption and Profit vs. Variance

![Refer to caption](Fig3.png)


Figure 3: Variance effects (H2).
(a) Optimal adoption α⋆\alpha^{\star} vs. demand variance σ\sigma (bootstrap scatter cloud).
All bootstrap draws collapse to α⋆=0.05\alpha^{\star}=0.05, indicating a degenerate *corner solution*.
(b) Profit vs. σ\sigma (bootstrap scatter with mean ±\pm95% CI and linear trend).
Profit declines monotonically as variance increases.

##### Narrative Summary.

Figure [3](https://arxiv.org/html/2510.07006v1#S6.F3 "Figure 3 ‣ 6.2.1 Adoption and Profit vs. Variance ‣ 6.2 H2: Variance Effects ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")(a) shows that the optimal adoption intensity α⋆\alpha^{\star} remains fixed at 0.050.05 across all variance levels σ∈{5,8,10,15}\sigma\in\{5,8,10,15\}.
The bootstrap distribution collapses into a single point, with confidence intervals of essentially zero width, reflecting that convex adoption costs ψ​(α)=A3​αν\psi(\alpha)=A\_{3}\alpha^{\nu} in combination with the KKT conditions (Eq. ([14](https://arxiv.org/html/2510.07006v1#S4.E14 "In Proposition 1 (Closed-form solution for 𝛼^⋆). ‣ 4.6 Optimal adoption intensity 𝛼^⋆ ‣ 4 Model Formulation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach"))) yield a *corner solution* rather than an interior solution (Proposition [2](https://arxiv.org/html/2510.07006v1#Thmproposition2 "Proposition 2 (Threshold adoption behavior). ‣ 4.6.1 Threshold (Corner) Rules ‣ 4.6 Optimal adoption intensity 𝛼^⋆ ‣ 4 Model Formulation ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")).
Thus, in the present calibration, variance shocks do not alter the marginal benefit of adoption, leaving adoption *variance-insensitive* and locked at the corner.

In contrast, Figure [3](https://arxiv.org/html/2510.07006v1#S6.F3 "Figure 3 ‣ 6.2.1 Adoption and Profit vs. Variance ‣ 6.2 H2: Variance Effects ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")(b) demonstrates that profit declines sharply and monotonically as σ\sigma increases.
Mean bootstrap profits decrease from {1010.0, 900.6, 839.3, 705.4}\{1010.0,\\
\,900.6,\,839.3,\,705.4\} across the four variance levels, with 95% confidence intervals
[1007.2,1013.2][1007.2,1013.2], [896.3,904.96][896.3,904.96], [834.06,845.39][834.06,845.39], and [697.35,711.13][697.35,711.13].
The intervals are narrow and non-overlapping, and Spearman rank correlation equals −1-1, indicating a perfectly monotonic decline.
Taken together, adoption remains robustly fixed, while profits are clearly vulnerable to variance shocks.

##### Interpretation and Implications.

The corner solution indicates that adoption is effectively determined by scale (total order quantity) and cost parameters, while variance affects outcomes primarily through the overage/shortage channel in the profit function.
From a managerial perspective, (i) reducing variance via hedging, pooling, or improved forecasting directly enhances profitability, and (ii) shifting adoption away from the corner requires adjustments to A3A\_{3}, ν\nu, or A1​∑iqiA\_{1}\sum\_{i}q\_{i}, which can alter the cost–benefit balance and induce an interior solution.
This contrast yields a clear message of *adoption robustness versus profit fragility*: adoption is locked, but profitability erodes under uncertainty.

#### 6.2.2 Regression Analysis

Table 4: Regression results for variance effects (H2).
Panel A: regression of α⋆\alpha^{\star} on σ\sigma (corner solution, slope insignificant).
Panel B: regression of profit on σ\sigma (significant negative slope).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Estimate | Std. Error | tt-value | pp-value |
| Panel A: Adoption α⋆\alpha^{\star} on Variance | | | | |
| Intercept (β0\beta\_{0}) | 0.0500 | 1.53×10−171.53\times 10^{-17} | 3.26×10153.26\times 10^{15} | 0.000 |
| Slope (β1\beta\_{1}) | 1.74×10−181.74\times 10^{-18} | 1.51×10−181.51\times 10^{-18} | 1.151 | 0.369 |
| R2R^{2} | – (flat corner solution) | | | |
| Panel B: Profit on Variance | | | | |
| Intercept (β0\beta\_{0}) | 1149.98 | 17.83 | 64.48 | 0.000 |
| Slope (β1\beta\_{1}) | −30.12-30.12 | 1.75 | −17.18-17.18 | 0.003 |
| R2R^{2} | 0.993 | | | |
| F-statistic | 295.2 (p=0.003) | | | |

##### Notes on Statistical Rigor.

Because only four variance levels were simulated, normality tests produce warnings and regression inferences should be interpreted with caution.
Nevertheless, significance is strongly supported by (i) the bootstrap confidence intervals and (ii) perfect monotonicity (Spearman ρ=−1\rho=-1).
The estimated slope β^1≈−30.12\hat{\beta}\_{1}\approx-30.12 (95% CI [−37.66,−22.58][-37.66,-22.58]) provides robust evidence that higher demand variance significantly reduces expected profit.

### 6.3 H2: Variance Effects (Extended Evidence)

Figure [4](https://arxiv.org/html/2510.07006v1#S6.F4 "Figure 4 ‣ 6.3 H2: Variance Effects (Extended Evidence) ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") provides extended evidence on the role of
demand variance in shaping adoption behavior by directly comparing the
baseline and interior regimes within a single visualization. In the baseline
calibration (blue line), the optimal adoption intensity remains locked at a
corner solution of α⋆=0.05\alpha^{\star}=0.05 across all variance levels. This flat
profile indicates that the baseline specification effectively masks the true
sensitivity of adoption to variance shocks, creating the illusion of
robustness that is in fact an artifact of boundary constraints.

![Refer to caption](Fig4.png)


Figure 4: Extended variance effects on adoption (H2).
The baseline calibration (blue line) shows adoption locked at
α⋆=0.05\alpha^{\star}=0.05 across all variance levels, while the interior regime
(red line and scatter cloud, A3=500,ν=1.5,A1=10A\_{3}=500,\nu=1.5,A\_{1}=10) reveals the
predicted monotone decline of α⋆\alpha^{\star} as demand variance σ\sigma
increases. Bootstrap scatter points with a 95% confidence band highlight
that adoption becomes an active decision margin once corner-locking is
relaxed.

By contrast, the interior parameter regime (red line in
Figure [4](https://arxiv.org/html/2510.07006v1#S6.F4 "Figure 4 ‣ 6.3 H2: Variance Effects (Extended Evidence) ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")) relaxes the corner-locking mechanism by
lowering adoption costs and increasing complementarity. Once these constraints
are removed, the theoretically predicted negative relationship clearly emerges:
as demand variance σ\sigma increases, the optimal adoption level
α⋆\alpha^{\star} decreases monotonically. The scatter–cloud visualization with
bootstrap replicates and a 95% confidence band further illustrates that
adoption becomes an *active margin*, responding smoothly to uncertainty
rather than being passively trapped at the boundary.

Viewed jointly, these results yield two key insights. First, variance effects
may be obscured in baseline environments due to corner solutions, underscoring
the importance of examining interior regimes for robust inference. Second,
the interior regime demonstrates close alignment between simulation outcomes
and theoretical predictions, thereby reinforcing the robustness of H2: higher
variance systematically lowers equilibrium adoption, consistent with the
precautionary effect of risk on strategic investment decisions.

Table 5: Baseline vs. interior regimes (H2 summary of equilibrium outcomes).
Metrics: optimal adoption α⋆\alpha^{\star}, profit, and fill rate.
The baseline calibration yields a corner solution with fixed adoption,
whereas interior regimes reveal responsiveness of α⋆\alpha^{\star} and
performance outcomes.

| Regime | A3A\_{3} | ν\nu | A1A\_{1} | α⋆\alpha^{\star} | Profit | Fill Rate |
| --- | --- | --- | --- | --- | --- | --- |
| Baseline (corner) | 2000 | 2.0 | 5 | 0.050 | 905.9 | 0.871 |
| Interior (example 1) | 500 | 1.2 | 10 | 0.275 | 920.4 | 0.882 |
| Interior (example 2) | 500 | 1.5 | 15 | 0.875 | 1089.2 | 0.896 |
| Interior (example 3) | 1000 | 1.5 | 15 | 0.200 | 944.5 | 0.869 |

##### Table [5](https://arxiv.org/html/2510.07006v1#S6.T5 "Table 5 ‣ 6.3 H2: Variance Effects (Extended Evidence) ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") Summary.

The numerical outcomes in Table [5](https://arxiv.org/html/2510.07006v1#S6.T5 "Table 5 ‣ 6.3 H2: Variance Effects (Extended Evidence) ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") complement the
graphical evidence by quantifying adoption, profit, and fill rate under both
baseline and interior regimes. In the baseline calibration, adoption is locked
at α⋆=0.05\alpha^{\star}=0.05, producing modest profit and service outcomes. By
contrast, the interior regimes display substantial variation: lower adoption
costs (A3A\_{3}) and stronger complementarity (A1A\_{1}) induce higher equilibrium
adoption, which in turn raises both profit and service performance. These
results confirm that the apparent robustness of adoption in baseline settings
is an artifact of corner locking; once structural constraints are relaxed,
adoption and performance outcomes become sensitive to cost and heterogeneity
parameters in theoretically consistent ways.

### 6.4 H3: Readiness Heterogeneity

#### 6.4.1 Simulation Outcomes

![Refer to caption](Fig5.png)


Figure 5: Readiness heterogeneity (H3, baseline calibration).
(a) Distribution of readiness β\beta (histogram + KDE).
(b) Optimal adoption α⋆\alpha^{\star} vs. Mean​(β)\mathrm{Mean}(\beta).
(c) Optimal α⋆\alpha^{\star} vs. Var​(β)\mathrm{Var}(\beta).
(d) Profit vs. Var​(β)\mathrm{Var}(\beta) with OLS trend and 95% CI.
All experiments reuse the demand generator and profit function from Figures [1](https://arxiv.org/html/2510.07006v1#S6.F1 "Figure 1 ‣ 6.1.1 Profit and Service Surfaces ‣ 6.1 H1 and H4: Threshold and Service Co-Benefit ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")–[3](https://arxiv.org/html/2510.07006v1#S6.F3 "Figure 3 ‣ 6.2.1 Adoption and Profit vs. Variance ‣ 6.2 H2: Variance Effects ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach"), ensuring comparability across H1–H3.

##### What Figure [5](https://arxiv.org/html/2510.07006v1#S6.F5 "Figure 5 ‣ 6.4.1 Simulation Outcomes ‣ 6.4 H3: Readiness Heterogeneity ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") shows.

Panels (b)–(c) reveal that the optimal adoption remains at a *corner solution* α⋆=0.05\alpha^{\star}=0.05 across the full range of readiness means and variances. This is the same corner trap documented in H1 and H2: with convex integration costs, the marginal benefit of adoption is dominated by procurement economics, so heterogeneity in β\beta does not move the optimal α⋆\alpha^{\star}.
Panel (d) overlays an OLS line (with 95% CI) on the scatter of profits against Var​(β)\mathrm{Var}(\beta). The slope is near zero and visually flat; combined with the statistical tests below, we find no economically meaningful sensitivity of profit to readiness variance under the current baseline calibration. The three horizontal profit bands (high ≈1000\approx 1000, mid ≈900\approx 900, low ≈830\approx 830) correspond to distinct inventory balance regimes induced by the optimal Q⋆Q^{\star} interacting with realized demand (good match, average match, mismatch).

![Refer to caption](Fig6.png)


Figure 6: Extended readiness effects (H3, baseline vs. interior).
Left: baseline calibration (adoption corner α⋆=0.05\alpha^{\star}=0.05 across readiness distributions).
Right: interior regime (A3=500,ν=1.5,A1=10A\_{3}=500,\nu=1.5,A\_{1}=10), where adoption α⋆\alpha^{\star} responds positively to mean readiness β¯\bar{\beta} and negatively to readiness variance Var​(β)\mathrm{Var}(\beta).
The 3D surface plots highlight that once the corner-locking mechanism is relaxed, readiness heterogeneity becomes an *active margin* shaping equilibrium adoption intensity.

##### Discussion (H3).

Taken together, Figures [5](https://arxiv.org/html/2510.07006v1#S6.F5 "Figure 5 ‣ 6.4.1 Simulation Outcomes ‣ 6.4 H3: Readiness Heterogeneity ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")–[6](https://arxiv.org/html/2510.07006v1#S6.F6 "Figure 6 ‣ What Figure 5 shows. ‣ 6.4.1 Simulation Outcomes ‣ 6.4 H3: Readiness Heterogeneity ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") show that readiness heterogeneity is inconsequential under the baseline corner solution, but becomes a key driver of adoption once interior regimes are considered. Higher mean readiness boosts adoption and profit, while greater variance depresses them. This contrast underscores that *heterogeneity effects are latent under corner locking, but emerge sharply once the adoption cost structure is relaxed*.

#### 6.4.2 Statistical Tests

Table 6: Readiness heterogeneity (H3).
Panel A (rows 1–2): α⋆\alpha^{\star} by β\beta-mean quartiles.  Panel B (rows 3–4): profit vs. Var​(β)\mathrm{Var}(\beta), with a wide–narrow comparison (two-sample tt) and Cohen’s dd.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Mean α⋆\alpha^{\star} | Profit | F/t-stat | pp-value | Cohen’s dd |
| Low mean(β\beta) quartile | 0.050 | 826.806 | n/a | n/a | n/a |
| High mean(β\beta) quartile | 0.050 | 980.122 | n/a | n/a | n/a |
| Wide variance | 0.050 | 903.603 | −0.073-0.073 | 0.9420.942 | −0.007-0.007 |
| Narrow variance | 0.050 | 904.022 | Ref. | Ref. | Ref. |

Notes. (i) In Panel A, α⋆\alpha^{\star} is identical across quartiles (all =0.05=0.05). Because there is *no between-group variance*, the ANOVA FF-statistic is not defined; we therefore report *n/a*.
(ii) In Panel B, “Wide” and “Narrow” are split at the median of Var​(β)\mathrm{Var}(\beta); we report the two-sample tt-test and Cohen’s dd for the wide group *relative to* the narrow group (the latter is the reference row, “Ref.”).
(iii) Numbers are rounded from the underlying simulation output.

##### Discussion (H3).

Under the baseline calibration used throughout H1–H2, readiness heterogeneity does not dislodge the adoption corner: α⋆\alpha^{\star} stays fixed at 0.050.05 regardless of Mean​(β)\mathrm{Mean}(\beta) or Var​(β)\mathrm{Var}(\beta). Consistent with the visual trend in Panel (d), the wide–narrow variance comparison yields a statistically non-significant difference in profit (t≈−0.073t\!\approx\!-0.073, p≈0.942p\!\approx\!0.942) and a negligible effect size (d≈−0.007d\!\approx\!-0.007). Taken together, the H3 evidence indicates that—in this cost regime—*readiness dispersion is not a first-order driver of either adoption or profitability*. Combined with H2 (where rising *demand* variance unambiguously reduces profit), these results suggest that managers will make more progress by (i) reducing demand-side risk (pooling, better forecasting) and/or (ii) changing the adoption cost structure (e.g., lowering A3A\_{3} or ν\nu) to move the firm off the adoption corner, rather than trying to reshape readiness heterogeneity alone.

### 6.5 H5: Distributional Robustness

#### 6.5.1 Broader Distributional Comparisons

We extend the lognormal–beta comparison by incorporating Pareto and Gamma distributions,
which capture heavy-tailed and skewed environments.
This provides a stress-test of whether the corner solution for adoption α⋆\alpha^{\star}
remains invariant.

#### 6.5.2 Simulation Outcomes

![Refer to caption](Fig7.png)


Figure 7: Distributional robustness (H5).
(a) Profit distributions across demand families, visualized with raincloud plots.
(b) Fill rate distributions using ridge density plots.
Adoption α⋆\alpha^{\star} is omitted from the figure since it remains structurally fixed
at the corner solution (0.050.05) across all cases.
All experiments reuse the same demand generator and profit function as in
Figures [1](https://arxiv.org/html/2510.07006v1#S6.F1 "Figure 1 ‣ 6.1.1 Profit and Service Surfaces ‣ 6.1 H1 and H4: Threshold and Service Co-Benefit ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach")–[5](https://arxiv.org/html/2510.07006v1#S6.F5 "Figure 5 ‣ 6.4.1 Simulation Outcomes ‣ 6.4 H3: Readiness Heterogeneity ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach"), ensuring comparability across H1–H5.

##### What Figure [7](https://arxiv.org/html/2510.07006v1#S6.F7 "Figure 7 ‣ 6.5.2 Simulation Outcomes ‣ 6.5 H5: Distributional Robustness ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") shows.

Adoption α⋆\alpha^{\star} is invariant under all distributional assumptions, reinforcing the robustness
patterns documented in H1–H3. In sharp contrast, both profit and fill rate vary considerably.
Lognormal demand generates consistently higher profits relative to beta, while gamma and pareto introduce
heavier tails, leading to lower mean profits and more dispersed fill rates.
Thus, adoption decisions are robust, but profitability and service quality are fragile to the assumed
distributional form.

#### 6.5.3 Distributional Tests

Table 7: Distributional robustness (H5).
Comparisons of lognormal vs. beta demand distributions.
Reported are two-sample KS test pp-values, Welch unequal-variance tt-tests, and effect sizes (Cohen’s dd).
Adoption α⋆\alpha^{\star} remains pinned to the corner solution, so differences are not statistically meaningful.

| Metric | KS-test pp | Welch tt-test pp | Cohen’s dd |
| --- | --- | --- | --- |
| Adoption α⋆\alpha^{\star} | 1.000 | n/a | n/a |
| Profit | 1.9×10−1191.9\times 10^{-119} | <0.001<0.001 | 71.6 |
| Fill rate | 2.2×10−752.2\times 10^{-75} | <0.001<0.001 | −1.05-1.05 |

##### Interpretation and Implications.

Table [7](https://arxiv.org/html/2510.07006v1#S6.T7 "Table 7 ‣ 6.5.3 Distributional Tests ‣ 6.5 H5: Distributional Robustness ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") highlights a fundamental asymmetry: adoption is structurally locked, while
profits and fill rates are highly sensitive to distributional assumptions. Profits under lognormal demand
are not only statistically higher but also economically significant, with effect sizes exceeding d=70d=70.
Fill rates likewise show systematic shifts (d≈−1.0d\approx-1.0), indicating that service reliability degrades
under beta-type demand. Taken together, these findings suggest a managerial paradox: *firms’ adoption
decisions are robust to uncertainty, but their realized performance is fragile to model misspecification*.
This distinction underscores the value of distributional calibration and motivates extensions to
distributionally robust optimization in future work.

### 6.6 H6: External Validity

To assess whether the results of our simulation-based approach are robust
to sampling noise and scale consistently with theoretical predictions,
we examine the external validity of the sample-average approximation (SAA).
Specifically, we study how the quality of SAA estimates improves as the
Monte Carlo sample size NN increases, testing whether convergence follows
the canonical 𝒪​(1/N)\mathcal{O}(1/\sqrt{N}) rate.

#### 6.6.1 Convergence Patterns

A central requirement for external validity is that simulation-based
estimates converge reliably as the number of Monte Carlo samples grows.
If the SAA is well behaved, increasing NN should reduce sampling noise
at the canonical 𝒪​(1/N)\mathcal{O}(1/\sqrt{N}) rate and drive the estimator
toward the true benchmark profit. To evaluate this property, we vary NN
systematically and track both the stability of the adoption decision and
the accuracy of profit estimation.

![Refer to caption](Fig8.png)


Figure 8: External validity (H6).
Profit convergence as the number of Monte Carlo samples NN increases.
Blue dots show sample-average estimates with 95% confidence intervals,
while the red dashed line denotes the true profit benchmark.
Estimates converge quickly and intervals shrink at the canonical
𝒪​(1/N)\mathcal{O}(1/\sqrt{N}) rate.

#### 6.6.2 Approximation Quality

Table [8](https://arxiv.org/html/2510.07006v1#S6.T8 "Table 8 ‣ 6.6.2 Approximation Quality ‣ 6.6 H6: External Validity ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") quantifies the convergence patterns observed in
Figure [8](https://arxiv.org/html/2510.07006v1#S6.F8 "Figure 8 ‣ 6.6.1 Convergence Patterns ‣ 6.6 H6: External Validity ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach"). As NN grows, the estimated profit converges
tightly to the true benchmark, with confidence intervals shrinking as
predicted. Adoption α⋆\alpha^{\star} remains stable at the corner solution
across all replications, while approximation error in profit falls rapidly.
The RMSE values decrease proportionally with 1/N1/\sqrt{N}, and empirical
coverage of the 95% confidence interval remains at 100%, demonstrating
correct uncertainty quantification.

Table 8: Approximation quality of SAA/Monte Carlo under increasing sample sizes NN (H6).
Reported are the root mean squared error (RMSE), empirical coverage of the 95% CI,
and relative improvement compared to the baseline case N=1,000N=1{,}000.

| NN | RMSE | Coverage (%) | Convergence rate | Gain vs. N=1,000N=1{,}000 |
| --- | --- | --- | --- | --- |
| 1,0001{,}000 | 1.430 | 100.0 | ≈1/N\approx 1/\sqrt{N} | – |
| 5,0005{,}000 | 0.653 | 100.0 | ≈1/N\approx 1/\sqrt{N} | 54% reduction |
| 20,00020{,}000 | 0.345 | 100.0 | ≈1/N\approx 1/\sqrt{N} | 76% reduction |

##### Interpretation and Implications.

These results provide strong evidence that the SAA/Monte Carlo procedure is
both statistically reliable and computationally efficient. In particular,
the approach delivers consistent estimates even under relatively small sample
sizes (N=1,000N=1{,}000), and rapidly attains near-exact convergence by N=20,000N=20{,}000.
Thus, the external validity check establishes that our simulation-based
framework is robust, asymptotically consistent, and suitable for empirical
applications where data availability or computational budgets may vary.

### 6.7 Real-World Data: MovieLens-100K

To complement our simulation-based validation, we test the empirical plausibility of our
mechanism using the MovieLens-100K dataset, a canonical benchmark in recommender
systems. We map user–item interactions into adoption decisions and infer implied demand
variability from rating dispersion. This provides a stylized, yet realistic, environment
to assess whether our theoretical hypotheses (H1–H5) retain qualitative validity under
real-world data conditions.

##### Distributional Evidence.

Panel (a) of Figure [9](https://arxiv.org/html/2510.07006v1#S6.F9 "Figure 9 ‣ Managerial Implication. ‣ 6.7 Real-World Data: MovieLens-100K ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") shows the empirical distribution of daily adoption
returns, benchmarked against lognormal, normal, tt-distribution, and bounded-beta fits.
The bounded-beta and tt-distribution provide visibly superior tail behavior, as confirmed
by goodness-of-fit metrics in panel (b). This evidence empirically justifies our modeling
choice of bounded and heavy-tailed demand shocks over Gaussian approximations.

##### Variance Regimes.

Panels (c)–(d) of Figure [9](https://arxiv.org/html/2510.07006v1#S6.F9 "Figure 9 ‣ Managerial Implication. ‣ 6.7 Real-World Data: MovieLens-100K ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") split the sample into “bull” and “bear”
regimes, capturing low- vs. high-volatility periods. Consistent with H2, adoption intensity
α⋆\alpha^{\star} remains robustly cornered, while realized profit degrades significantly under
high-variance regimes. This pattern directly mirrors our simulation-based variance fragility
results.

##### Hypothesis Matrix.

Figure [10](https://arxiv.org/html/2510.07006v1#S6.F10 "Figure 10 ‣ Managerial Implication. ‣ 6.7 Real-World Data: MovieLens-100K ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") summarizes all hypotheses (H1–H5) in a 2×32\times 3 matrix of
empirical mini-results. We find:
(i) the adoption–cost tradeoff (H1) follows the predicted convex decay;
(ii) variance undermines profitability (H2), while leaving adoption cornered;
(iii) readiness heterogeneity (H3) is reflected in cross-user variance of adoption probabilities;
(iv) profit–service co-benefits (H4) remain present, though attenuated; and
(v) distributional robustness (H5) favors bounded and heavy-tailed fits.
Together, these results demonstrate that our theoretical structure extends to real-world
data without loss of qualitative validity.

##### Managerial Implication.

The empirical MovieLens evidence strengthens our central claim:
*adoption outcomes are structurally robust to variance shocks,
while profitability is variance-fragile.*
This duality suggests that managers cannot rely on stable adoption alone,
but must actively hedge or diversify against volatility to preserve economic value.

![Refer to caption](Fig9.png)


Figure 9: Real-world validation (R1).
(a) Empirical distribution vs. fits;
(b) Goodness-of-fit comparison (AIC/BIC/KS);
(c) Bull vs. Bear regimes;
(d) Adoption α⋆\alpha^{\star} vs. Profit by regime.

![Refer to caption](Fig10.png)


Figure 10: Real-world hypothesis matrix (R2).
Empirical mini-results for H1–H5, plus extended variance–profit evidence.
Even with noisy real data, the structure of our theoretical predictions
remains qualitatively intact.

##### Quantitative Evidence.

Table [9](https://arxiv.org/html/2510.07006v1#S6.T9 "Table 9 ‣ Quantitative Evidence. ‣ 6.7 Real-World Data: MovieLens-100K ‣ 6 Numerical Experiments ‣ Smart Contract Adoption in Derivative Markets under Bounded Risk: An Optimization Approach") reports the log-likelihood, information criteria,
and KS statistics for competing distributional fits.
The tt-distribution achieves the best overall fit
(AIC=−9384.5\mathrm{AIC}=-9384.5, BIC=−9368.5\mathrm{BIC}=-9368.5, KS ≈0.017\approx 0.017),
while both Normal and Beta significantly outperform the Lognormal benchmark
(AIC improvement of ≈1100\approx 1100–1500 points).
This provides rigorous confirmation that bounded or heavy-tailed distributions
capture empirical adoption variability more accurately than lognormal models.

Turning to regime outcomes, the estimated volatility differs moderately across periods
(Bull σ=0.0141\sigma=0.0141 vs. Bear σ=0.0123\sigma=0.0123), yet profits exhibit a clear divergence:
mean profit is ≈680.2\approx 680.2 in Bull periods and ≈742.4\approx 742.4 in Bear periods.
In contrast, adoption intensity remains cornered at α⋆≈0.05\alpha^{\star}\approx 0.05 in both regimes.
Thus, the empirical results reinforce our central message:
*adoption intensity is structurally robust, whereas profitability remains variance-fragile*.
The narrow but consistent gap across volatility regimes illustrates how even moderate shifts
in variance propagate into sizable profit differences, without affecting adoption.

Table 9: Goodness-of-fit (GOF) results for real-world data (S&P500, 2019–2024).
The tt-distribution dominates under all metrics, while Lognormal provides the weakest fit.

| Distribution | LogLik | AIC | BIC | KS |
| --- | --- | --- | --- | --- |
| Lognormal | 3905.16 | −7804.3-7804.3 | −7788.4-7788.4 | 0.228 |
| Normal | 4460.65 | −8917.3-8917.3 | −8906.7-8906.7 | 0.094 |
| tt-dist | 4695.23 | −9384.5-9384.5 | −9368.5-9368.5 | 0.017 |
| Beta | 4462.14 | −8916.3-8916.3 | −8895.0-8895.0 | 0.091 |

## 7 Results and Discussion

### 7.1 Structural Drivers of Adoption

The comparative statics reveal how adoption intensity responds to core cost parameters.
Consistent with model predictions, the optimal adoption intensity α⋆\alpha^{\star} decreases
monotonically with the convexity parameter A3A\_{3}, reflecting the rising marginal burden of
integration costs. Conversely, α⋆\alpha^{\star} increases with the procurement complementarity
parameter A1A\_{1}, indicating that stronger alignment between procurement efficiency and
adoption incentives induces greater adoption. These results underscore the central role of
cost convexities in shaping adoption thresholds: A3A\_{3} functions as a brake, while A1A\_{1}
acts as a catalyst for digital integration.

Threshold dynamics further confirm that adoption intensity is governed by a discontinuous,
nonlinear regime. When the fixed-cost parameter A3A\_{3} crosses a critical value
A3threshA\_{3}^{\text{thresh}}, adoption collapses abruptly from an interior solution to the boundary
value 0.050.05. This bifurcation-like behavior mirrors real options in finance, where exercise
occurs only once a barrier is breached (Dixit and Pindyck, [1994](https://arxiv.org/html/2510.07006v1#bib.bib17); Trigeorgis, [1996](https://arxiv.org/html/2510.07006v1#bib.bib44)).
Thus, adoption is not smoothly sensitive to marginal shocks, but instead exhibits threshold-driven
jumps that are structurally robust to other perturbations.

*Takeaway: Adoption responds discontinuously to cost thresholds, with A3A\_{3} acting as
a brake and A1A\_{1} as a catalyst, confirming that adoption is best understood as a
threshold-driven option-like decision.*

### 7.2 Practical and Financial Implications

From a managerial perspective, these findings highlight the need to align supplier readiness
with adoption incentives. Since adoption remains robust to variance shocks (H2) and supplier
heterogeneity (H3), firms cannot rely on uncertainty to discipline technology choices.
Instead, the binding constraint lies in the threshold effect: once A3A\_{3} exceeds
A3threshA\_{3}^{\text{thresh}}, adoption collapses irrespective of readiness. Managers should therefore
(i) closely monitor and control adoption-related fixed costs, and (ii) coordinate procurement
efficiency (via A1A\_{1}) with readiness-enhancing policies to sustain adoption in the interior
region. These strategies link theoretical robustness (H1–H5) to practical approaches for
maintaining profitability under uncertainty (H6).

From a financial perspective, the invariance of α⋆\alpha^{\star} demonstrates that adoption
behaves as a barrier option: insensitive to volatility and distributional shocks until a
critical cost boundary is crossed. This parallels real options and credit risk models, where
exercise or default occurs discontinuously at a threshold
(Merton, [1974](https://arxiv.org/html/2510.07006v1#bib.bib34); Leland, [1994](https://arxiv.org/html/2510.07006v1#bib.bib31)). By contrast, profits and service outcomes remain
fragile to variance and tail behavior, mirroring cash-flow exposure to volatility and
heavy-tailed shocks in financial markets (Mandelbrot, [1963](https://arxiv.org/html/2510.07006v1#bib.bib32); Cont, [2001](https://arxiv.org/html/2510.07006v1#bib.bib16)).

This duality carries three implications. First, managers may underestimate risk if they equate
stable adoption with stable outcomes; payoff distributions remain highly sensitive to volatility
and distributional tails. Second, the results resonate with broader themes in capital markets,
where ESG or digital adoption commitments appear stable at the margin but yield fragile economic
payoffs once tail risks materialize (Pástor et al., [2022](https://arxiv.org/html/2510.07006v1#bib.bib36); Krueger et al., [2020](https://arxiv.org/html/2510.07006v1#bib.bib29); Greenwood et al., [2023](https://arxiv.org/html/2510.07006v1#bib.bib24)).
Third, the convergence analysis in H6 highlights the value of simulation-based stress testing:
adoption equilibria converge quickly, but profit distributions require larger samples for reliable
inference, echoing best practices in financial risk management (Glasserman, [2003](https://arxiv.org/html/2510.07006v1#bib.bib22); Ban et al., [2023](https://arxiv.org/html/2510.07006v1#bib.bib5)).

*Takeaway: Adoption stability should not be conflated with financial stability; robust-looking
adoption masks fragile payoffs, reinforcing the need for risk-adjusted evaluation and
stress testing.*

### 7.3 Variance Effects and Cross-Hypothesis Synthesis

The variance experiments (H2) show a sharp divergence between economic and adoption outcomes.
Profitability declines monotonically as demand variance σ\sigma increases, with bootstrap
confidence intervals confirming robustness, while adoption intensity remains pinned at 0.050.05.
This insensitivity of α⋆\alpha^{\star} to σ\sigma is a structural feature of convex integration
costs: variance shocks are absorbed through profits rather than through adoption. Taken together
with H1, the narrative is clear: thresholds drive adoption, while variance erodes profitability.

Synthesizing across H1–H6, a consistent pattern emerges:

* •

  H1 (Threshold): Adoption responds sharply and nonlinearly to cost thresholds.
* •

  H2 (Variance): Variance shocks degrade profitability but leave adoption locked.
* •

  H3 (Readiness): Supplier heterogeneity shifts profits, yet adoption remains invariant.
* •

  H4 (Service Co-benefit): Profit and fill rate align in a narrow “co-benefit zone.”
* •

  H5 (Distribution): Adoption is robust across distributions, but profits and service
  outcomes are fragile to tail behavior.
* •

  H6 (External Validity): Monte Carlo approximations converge at the canonical
  𝒪​(1/N)\mathcal{O}(1/\sqrt{N}) rate, with stable adoption but variance-fragile profits.

*Takeaway: Across all hypotheses, adoption is structurally robust to shocks, while profitability
and service outcomes are variance- and distribution-sensitive, highlighting the need to jointly
recognize adoption thresholds and actively manage payoff fragility.*

### 7.4 Bridge to Conclusion

Viewed collectively, the results validate our six hypotheses and reveal a deeper structural insight:
adoption is governed by discrete thresholds, while profitability is continuously eroded by
uncertainty. This duality forms the central contribution of the paper and directly motivates the
concluding discussion on theory, practice, and avenues for future research.

## 8 Conclusion

This paper develops and analyzes an optimization model of smart contract adoption under bounded risk.
Across a sequence of experiments, the results reveal a structural duality: adoption intensity
α⋆\alpha^{\star} is robust—pinned at boundary solutions and invariant to variance shocks, readiness
heterogeneity, and distributional changes—whereas profitability and service outcomes are fragile,
eroding under volatility, heterogeneity, and tail risk. Adoption thus appears stable at the decision
margin, but the financial consequences of those decisions remain acutely vulnerable to uncertainty.
This duality parallels real options and credit risk models in finance, where exercise occurs only once
thresholds are breached, but cash flows remain exposed to volatility and tail shocks
(Dixit and Pindyck, [1994](https://arxiv.org/html/2510.07006v1#bib.bib17); Trigeorgis, [1996](https://arxiv.org/html/2510.07006v1#bib.bib44); Merton, [1974](https://arxiv.org/html/2510.07006v1#bib.bib34); Leland, [1994](https://arxiv.org/html/2510.07006v1#bib.bib31)).

At the same time, the robustness documented in H1–H5 partly reflects the baseline calibration.
Under the convex cost structure ψ​(α)=A3​αν\psi(\alpha)=A\_{3}\alpha^{\nu} combined with the procurement penalty
term A1​αA\_{1}\alpha, the marginal benefit of adoption never outweighs marginal cost, forcing a boundary
solution of α⋆=0.05\alpha^{\star}=0.05. This provides theoretical insight into structural robustness,
but also reveals a limitation: adoption is effectively inert under the assumed parameters. Moreover,
the reliance on synthetic demand distributions and stylized calibration constrains external
generalizability. The findings should therefore be interpreted as a theory-building step rather than
as direct policy prescriptions.

Future research should relax these assumptions to identify conditions under which interior solutions
emerge and adoption becomes an active decision margin. Promising avenues include modifying the cost
structure (e.g., reducing A3A\_{3}, altering the curvature ν\nu, or increasing complementarity A1A\_{1}),
endogenizing readiness by linking β\beta to past adoption decisions, and extending the static model
to dynamic environments with learning-by-doing. A systematic mapping of the parameter space
(A3,ν,A1)(A\_{3},\nu,A\_{1}) could clarify the boundaries between corner- and interior-solution regimes. Beyond
structural analysis, empirical validation using derivatives, insurance, or technology adoption data
would allow calibration against observed distributions, while extensions to distributionally robust
optimization and machine learning–based stress testing (e.g., Ban et al., [2023](https://arxiv.org/html/2510.07006v1#bib.bib5); Greenwood et al., [2023](https://arxiv.org/html/2510.07006v1#bib.bib24))
could further strengthen applicability in practice.

In summary, future work can build a richer theory of adoption sensitivity—one that not only identifies
when adoption is structurally robust but also clarifies when it becomes economically responsive.
For both operations and finance, the broader implication is clear: decisions that appear stable at the
adoption margin may conceal fragile financial outcomes. *Recognizing and managing this duality is
essential for designing digital adoption strategies that are both operationally viable and financially
resilient in uncertain markets.*

## References

* Andersen et al. (2015)

  Torben G Andersen, Tim Bollerslev, Francis X Diebold, and Jin Wu.
  Risk premia in option-implied and realized variance.
  *Quarterly Journal of Economics*, 130(2):1029–1086, 2015.
  doi: 10.1093/qje/qjv008.
* Arora et al. (2021)

  Siddharth Arora, Rohan Gupta, and Neha Sharma.
  Blockchain adoption in financial trading and derivatives settlement: Challenges and opportunities.
  *Journal of Financial Innovation*, 7(3):45–62, 2021.
  doi: 10.1016/j.fininn.2021.100123.
* Atalay et al. (2019)

  Enghin Atalay, Ali Hortacsu, and Chad Syverson.
  Blockchain and contract enforcement in supply chains.
  *NBER Working Paper No. 25763*, 2019.
  doi: 10.3386/w25763.
* Baker et al. (2002)

  George Baker, Robert Gibbons, and Kevin J Murphy.
  Relational contracts and the theory of the firm.
  *Quarterly Journal of Economics*, 117(1):39–84, 2002.
  doi: 10.1162/003355302753399445.
* Ban et al. (2023)

  Gah-Yi Ban, Noureddine El Karoui, and Andrew E.B. Lim.
  Robustness and uncertainty in stochastic programming.
  *Management Science*, 69(1):107–128, 2023.
  doi: 10.1287/mnsc.2022.4460.
* Barndorff-Nielsen et al. (2011)

  Ole E Barndorff-Nielsen, Peter R Hansen, Asger Lunde, and Neil Shephard.
  Multivariate realized kernels: Consistent positive semi-definite estimators of the covariation of equity prices with noise and non-synchronous trading.
  *Journal of Econometrics*, 162(2):149–169, 2011.
  doi: 10.1016/j.jeconom.2010.07.009.
* Bernheim and Whinston (1987)

  B. Douglas Bernheim and Michael D Whinston.
  Coalition-proof nash equilibria i. concepts.
  *Journal of Economic Theory*, 42(1):1–12, 1987.
  doi: 10.1016/0022-0531(87)90099-8.
* Bolton and Dewatripont (2005)

  Patrick Bolton and Mathias Dewatripont.
  *Contract Theory*.
  MIT Press, 2005.
  ISBN 9780262025768.
* Broby (2022)

  Daniel Broby.
  Financial technology and the future of banking.
  *Journal of Risk and Financial Management*, 15(5):233, 2022.
  doi: 10.3390/jrfm15050233.
* Brunnermeier and Sannikov (2014)

  Markus K Brunnermeier and Yuliy Sannikov.
  A macroeconomic model with a financial sector.
  *American Economic Review*, 104(2):379–421, 2014.
  doi: 10.1257/aer.104.2.379.
* Cachon (2003)

  Gerard P. Cachon.
  Supply chain coordination with contracts.
  In *Handbooks in Operations Research and Management Science*, volume 11, pages 229–339. Elsevier, 2003.
  doi: 10.1016/S0927-0507(03)11006-7.
* Carmona (2014)

  René Carmona.
  *Financial mathematics of derivatives: A short introduction*.
  SIAM, 2014.
  doi: 10.1137/1.9781611973541.
* Catalini and Gans (2016)

  Christian Catalini and Joshua S. Gans.
  Some simple economics of the blockchain.
  Technical Report 22952, National Bureau of Economic Research, 2016.
* Chen et al. (2023)

  Yifan Chen, Xiaoyang Li, and Yan Zhou.
  Smart contract adoption in financial derivatives: Risk, enforcement, and efficiency.
  *Finance Research Letters*, 52:103656, 2023.
  doi: 10.1016/j.frl.2022.103656.
* Cong and He (2019)

  Lin William Cong and Zhiguo He.
  Blockchain disruption and smart contracts.
  *The Review of Financial Studies*, 32(5):1754–1797, 2019.
  doi: 10.1093/rfs/hhz007.
* Cont (2001)

  Rama Cont.
  Empirical properties of asset returns: Stylized facts and statistical issues.
  *Quantitative Finance*, 1(2):223–236, 2001.
  doi: 10.1080/713665670.
* Dixit and Pindyck (1994)

  Avinash K. Dixit and Robert S. Pindyck.
  *Investment under Uncertainty*.
  Princeton University Press, 1994.
  doi: 10.2307/j.ctvcm4gqx.
* Duffie et al. (2005)

  Darrell Duffie, Nicolae Garleanu, and Lasse Heje Pedersen.
  Dark markets: Asset pricing and information transmission in over-the-counter markets.
  *Econometrica*, 73(1):181–196, 2005.
  doi: 10.1111/j.1468-0262.2004.00503.x.
* Embrechts et al. (1997)

  Paul Embrechts, Claudia Klüppelberg, and Thomas Mikosch.
  *Modelling Extremal Events for Insurance and Finance*.
  Springer, 1997.
  doi: 10.1007/978-3-642-33483-2.
* Fanti and Kogan (2022)

  Giulia C Fanti and Leonid Kogan.
  Blockchain contracts with bounded enforcement costs.
  *Management Science*, 68(9):6543–6562, 2022.
  doi: 10.1287/mnsc.2021.4221.
* Fathi (2025)

  Mehdi Fathi.
  Modeling variance risk in financial markets using power-laws: Evidence from s&p 500, gold, crude oil, fx and bitcoin.
  *Journal of International Financial Markets, Institutions & Money*, 2025.
  doi: 10.1080/10424431.2025.2529485.
* Glasserman (2003)

  Paul Glasserman.
  *Monte Carlo Methods in Financial Engineering*, volume 53 of *Applications of Mathematics*.
  Springer, 2003.
  doi: 10.1007/978-0-387-21617-1.
* Glasserman (2005)

  Paul Glasserman.
  *Monte Carlo methods in financial engineering*, volume 53 of *Applications of Mathematics*.
  Springer, 2005.
  doi: 10.1007/b97213.
* Greenwood et al. (2023)

  Robin Greenwood, Samuel G. Hanson, and Gordon Y. Liao.
  Fragility in financial markets.
  *Journal of Finance*, 78(5):2423–2471, 2023.
  doi: 10.1111/jofi.13278.
* Grossman and Hart (1986)

  Sanford J Grossman and Oliver D Hart.
  The costs and benefits of ownership: A theory of vertical and lateral integration.
  *Journal of Political Economy*, 94(4):691–719, 1986.
  doi: 10.1086/261404.
* Hart and Moore (1990)

  Oliver Hart and John Moore.
  Property rights and the nature of the firm.
  *Journal of Political Economy*, 98(6):1119–1158, 1990.
  doi: 10.1086/261729.
* Harvey et al. (2021)

  Campbell R Harvey, Ashwin Ramachandran, and Joey Santoro.
  *DeFi and the future of finance*.
  Wiley, 2021.
  doi: 10.1002/9781119836015.
* Johnson et al. (1995)

  Norman L. Johnson, Samuel Kotz, and N. Balakrishnan.
  *Continuous Univariate Distributions, Volume 2*.
  Wiley, 1995.
  ISBN 9780471584952.
* Krueger et al. (2020)

  Philipp Krueger, Zacharias Sautner, and Laura T. Starks.
  Climate change and firm valuation: A review of the literature.
  *Review of Finance*, 24(6):1449–1493, 2020.
  doi: 10.1093/rof/rfaa013.
* Lariviere and Porteus (2001)

  Martin A Lariviere and Evan L Porteus.
  Selling to the newsvendor: An analysis of price-only contracts.
  *Manufacturing & Service Operations Management*, 3(4):293–305, 2001.
  doi: 10.1287/msom.3.4.293.9972.
* Leland (1994)

  Hayne E. Leland.
  Corporate debt value, bond covenants, and optimal capital structure.
  *Journal of Finance*, 49(4):1213–1252, 1994.
  doi: 10.1111/j.1540-6261.1994.tb02452.x.
* Mandelbrot (1963)

  Benoit Mandelbrot.
  The variation of certain speculative prices.
  *Journal of Business*, 36(4):394–419, 1963.
  doi: 10.1086/294632.
* Maskin and Tirole (2001)

  Eric Maskin and Jean Tirole.
  Implementation theory.
  *Handbook of Game Theory with Economic Applications*, 3:2371–2420, 2001.
  doi: 10.1016/S1574-0005(02)03018-4.
* Merton (1974)

  Robert C. Merton.
  On the pricing of corporate debt: The risk structure of interest rates.
  *Journal of Finance*, 29(2):449–470, 1974.
  doi: 10.1111/j.1540-6261.1974.tb03058.x.
* Narayanan and Raman (2004)

  V. G. Narayanan and Ananth Raman.
  Aligning incentives in supply chains.
  *Harvard Business Review*, 82(11):94–102, 2004.
* Pástor et al. (2022)

  Ľuboš Pástor, Robert F. Stambaugh, and Lucian A. Taylor.
  Sustainable investing in equilibrium.
  *Journal of Financial Economics*, 145(2):348–371, 2022.
  doi: 10.1016/j.jfineco.2021.08.013.
* Rockafellar and Uryasev (2000)

  R. Tyrrell Rockafellar and Stanislav Uryasev.
  Optimization of conditional value-at-risk.
  *Journal of Risk*, 2(3):21–42, 2000.
  doi: 10.21314/JOR.2000.038.
* Schär (2021)

  Fabian Schär.
  Decentralized finance: On blockchain- and smart contract-based financial markets.
  *Federal Reserve Bank of St. Louis Review*, 103(2):153–174, 2021.
  doi: 10.20955/r.103.153-174.
* Shaiku et al. (2025)

  S. S. Shaiku et al.
  Factors leading to the adoption of blockchain technology in financial reporting and audit practices.
  *Frontiers in Blockchain*, 8:1491609, 2025.
  doi: 10.3389/fbloc.2025.1491609.
* Shapiro et al. (2014)

  Alexander Shapiro, Darinka Dentcheva, and Andrzej Ruszczyński.
  *Lectures on Stochastic Programming: Modeling and Theory*.
  SIAM, 2nd edition, 2014.
  doi: 10.1137/1.9781611973433.
* Stoyanov et al. (2011)

  Stoyan V Stoyanov, Svetlozar T Rachev, and Frank J Fabozzi.
  Fat-tailed models for risk management.
  *Journal of Portfolio Management*, 37(2):107–117, 2011.
  doi: 10.3905/jpm.2011.37.2.107.
* Tapscott and Tapscott (2017)

  Don Tapscott and Alex Tapscott.
  *Blockchain Revolution: How the Technology Behind Bitcoin and Other Cryptocurrencies is Changing the World*.
  Penguin, 2017.
  ISBN 9781101980149.
* Tirole (1999)

  Jean Tirole.
  Incomplete contracts: Where do we stand?
  *Econometrica*, 67(4):741–781, 1999.
  doi: 10.1111/1468-0262.00047.
* Trigeorgis (1996)

  Lenos Trigeorgis.
  *Real Options: Managerial Flexibility and Strategy in Resource Allocation*.
  MIT Press, 1996.
  doi: 10.7551/mitpress/9780262201025.001.0001.
* Wang (2025)

  Jun Wang.
  Contract theory in digital markets: Enforcement, risk, and smart adoption.
  *Journal of Financial Economics*, 2025.
  doi: 10.2139/ssrn.4958123.
  Forthcoming.