---
authors:
- Jinho Cha
- Justin Yu
- Junyeol Ryu
- Eunchan Daniel Cha
- Hyeyoung Hwang
doc_id: arxiv:2510.22518v1
family_id: arxiv:2510.22518
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying
  the System Impact of Adaptive Health Programs'
url_abs: http://arxiv.org/abs/2510.22518v1
url_html: https://arxiv.org/html/2510.22518v1
venue: arXiv q-fin
version: 1
year: 2025
---


[jcha@gwinnetttech.edu](mailto:jcha@gwinnetttech.edu)
  
\fnmJustin \surYu
  
\fnmJunyeol \surRyu
  
\fnmEunchan D. \surCha
  
\fnmHyeyoung \surHwang
[
[
[
[
[

###### Abstract

This study introduces an inverse behavioral optimization framework that integrates QALY-based health outcomes, ROI-driven incentives, and adaptive behavioral learning to quantify how policy design shapes national healthcare performance.
Building on the FOSSIL (Flexible Optimization via Sample-Sensitive Importance Learning) paradigm, the model embeds a regret-minimizing behavioral weighting mechanism that enables dynamic learning from heterogeneous policy environments.
It recovers latent behavioral sensitivities—efficiency (λ)(\lambda), fairness (γ)(\gamma), and temporal responsiveness (T)(T)—from observed QALY–ROI trade-offs, providing an analytical bridge between individual incentive responses and aggregate system productivity.
We formalize this mapping through the proposed System Impact Index (SII), which links behavioral elasticity to measurable macro-level efficiency and equity outcomes.
Using OECD–WHO panel data, the framework empirically demonstrates that modern health systems operate near an efficiency-saturated frontier, where incremental fairness adjustments yield stabilizing but diminishing returns.
Simulation and sensitivity analyses further show how small changes in behavioral parameters propagate into measurable shifts in systemic resilience, equity, and ROI efficiency.
The results establish a quantitative foundation for designing adaptive, data-driven health incentive programs that dynamically balance efficiency, fairness, and long-run sustainability in national healthcare systems.

###### keywords:

QALY–ROI Trade-off, Inverse Behavioral Optimization, FOSSIL Framework, Behavioral Health Economics,
Adaptive Health Incentives, System Impact Index

## 1 Introduction: From Health Outcomes to System Impact

The pursuit of equitable and efficient health systems increasingly depends on quantifying how behavioral incentives shape measurable outcomes such as Quality-Adjusted Life Years (QALY) and Return on Investment (ROI) [[1](https://arxiv.org/html/2510.22518v1#bib.bib1), [2](https://arxiv.org/html/2510.22518v1#bib.bib2)].
Traditionally, these two dimensions—clinical effectiveness and economic efficiency—have been optimized separately, often resulting in policy misalignment between individual care outcomes and systemic financial sustainability [[3](https://arxiv.org/html/2510.22518v1#bib.bib3), [4](https://arxiv.org/html/2510.22518v1#bib.bib4)].
For instance, hospitals and insurers may design incentive programs that improve short-term ROI yet inadvertently reduce long-term population health gains [[5](https://arxiv.org/html/2510.22518v1#bib.bib5)].
Similarly, QALY-based interventions are frequently deployed without evaluating their broader system-level and macroeconomic consequences [[6](https://arxiv.org/html/2510.22518v1#bib.bib6)].
This study contends that such fragmentation arises from the absence of an analytical bridge linking behavioral decision-making at the micro level to system performance at the macro level.
Building on this motivation, we propose that this gap can be addressed through an *inverse behavioral optimization* framework that infers latent decision parameters from observed QALY–ROI trade-offs [[7](https://arxiv.org/html/2510.22518v1#bib.bib7), [8](https://arxiv.org/html/2510.22518v1#bib.bib8)], thereby revealing how learning and adaptation within health programs propagate to system-wide outcomes [[9](https://arxiv.org/html/2510.22518v1#bib.bib9)].

Despite extensive research in health economics and management science [[1](https://arxiv.org/html/2510.22518v1#bib.bib1), [2](https://arxiv.org/html/2510.22518v1#bib.bib2)], existing models typically assume either static optimization (maximizing QALY under budget constraints) or cost-effectiveness evaluation (minimizing cost per QALY gained).
Few studies explicitly model the dynamic behavioral adjustments of healthcare agents—patients, providers, and policymakers—when incentive structures evolve over time [[6](https://arxiv.org/html/2510.22518v1#bib.bib6)].
Moreover, while behavioral economics has illuminated how fairness, effort, and reward sensitivity influence individual decisions [[3](https://arxiv.org/html/2510.22518v1#bib.bib3), [4](https://arxiv.org/html/2510.22518v1#bib.bib4)], its integration into system-level optimization remains limited.
Consequently, the literature lacks a unified methodology for *inferring* the behavioral drivers underlying observed QALY–ROI outcomes and translating them into measurable system-level effects.

To address this gap, we build upon our prior work on the behavioral foundations of QALY–ROI trade-offs in chronic disease management [[9](https://arxiv.org/html/2510.22518v1#bib.bib9)] and introduce the FOSSIL (Flexible Optimization via Sample-Sensitive Importance Learning) framework [[10](https://arxiv.org/html/2510.22518v1#bib.bib10)].
Originally proposed as a learning-based optimization paradigm for robust inference under small and imbalanced data, FOSSIL employs an adaptive weighting mechanism that allows the efficiency frontier itself to evolve with heterogeneous samples.
This regret-minimizing process endogenizes behavioral sensitivity within the optimization, enabling health systems to adapt across diverse policy environments and temporal horizons.
By embedding this mechanism into a structural inverse optimization model, we estimate behavioral parameters (λ,γ,T)(\lambda,\gamma,T)—representing efficiency sensitivity, fairness preference, and temporal adaptation—directly from empirical health performance data.
To our knowledge, this is the first systematic application of a curriculum-based machine learning paradigm to QALY–ROI analysis, extending FOSSIL beyond its original learning context into behavioral inference for health policy design.
This study thus establishes a methodological foundation for dynamic behavioral inference in health-care management.

Health-care policy decisions are increasingly data-driven, yet policymakers continue to face uncertainty about how incentive structures translate into measurable health and financial outcomes.
To ground the proposed approach in a realistic policy setting, we focus on *adaptive chronic disease incentive programs*—for example, diabetes and cardiovascular management initiatives across OECD member countries—where QALY-based performance payments are linked to both patient adherence and long-term cost savings.
These programs provide a natural environment in which fairness (e.g., equitable access to care), efficiency (e.g., cost reduction per QALY gained), and temporal responsiveness (e.g., the rate of behavioral adjustment across policy cycles) interact dynamically.
By calibrating the inverse behavioral model on OECD–WHO panel data, the analysis illustrates how the recovered parameters (λ,γ,T)(\lambda,\gamma,T) can inform policy design—such as subsidy timing, incentive intensity, and fairness adjustments across heterogeneous populations.
The same analytical structure can also be applied to vaccination incentives, preventive screening reimbursements, or chronic care coordination programs, thereby linking the theoretical framework directly to contemporary global health policy challenges.

This study contributes to the literature and practice in three major ways.
First, it introduces the FOSSIL-based Forward–Inverse–Impact (FII) framework, which integrates behavioral decision-making with system-level performance analysis [[5](https://arxiv.org/html/2510.22518v1#bib.bib5), [6](https://arxiv.org/html/2510.22518v1#bib.bib6)].
The forward layer models QALY–ROI optimization under fairness-adjusted utility;
the inverse layer recovers latent behavioral coefficients through adaptive learning;
and the impact layer evaluates how these behavioral dynamics propagate to measurable performance indicators [[11](https://arxiv.org/html/2510.22518v1#bib.bib11)].
Second, we propose the *System Impact Index (SII)*—a composite metric that quantifies improvements in efficiency and fairness arising from adaptive incentive policies [[8](https://arxiv.org/html/2510.22518v1#bib.bib8)].
Third, we empirically demonstrate the managerial relevance of this framework using multi-regional health data, showing that behavioral adaptation—captured through FOSSIL-based learning—can yield substantial improvements in system-level efficiency [[9](https://arxiv.org/html/2510.22518v1#bib.bib9)].
Taken together, these contributions position inverse behavioral optimization, enhanced by FOSSIL, as a unified methodological foundation for designing incentive-aligned, data-driven healthcare systems (see Fig. [2.1](https://arxiv.org/html/2510.22518v1#S2.F1 "Figure 2.1 ‣ 2 Conceptual Architecture: Adaptive Health Systems and System-Level Learning ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")).

## 2 Conceptual Architecture: Adaptive Health Systems and System-Level Learning

Health systems can be viewed as behaviorally responsive ecosystems in which patients, providers, and policymakers continuously learn from feedback and adjust their actions accordingly.
Patients modify adherence as perceived reward sensitivity changes, physicians adapt effort based on fairness and fatigue, and policymakers recalibrate incentives to sustain participation equilibria [[12](https://arxiv.org/html/2510.22518v1#bib.bib12), [13](https://arxiv.org/html/2510.22518v1#bib.bib13), [14](https://arxiv.org/html/2510.22518v1#bib.bib14)].
Such dynamics mirror learning processes observed in manufacturing, logistics, and energy systems, where bounded rationality and delayed feedback shape organizational outcomes [[15](https://arxiv.org/html/2510.22518v1#bib.bib15), [16](https://arxiv.org/html/2510.22518v1#bib.bib16), [17](https://arxiv.org/html/2510.22518v1#bib.bib17)].
The healthcare context, however, introduces an additional layer of ethical and welfare complexity: QALY-based incentives must coexist with moral hazard and equity constraints [[18](https://arxiv.org/html/2510.22518v1#bib.bib18), [19](https://arxiv.org/html/2510.22518v1#bib.bib19), [20](https://arxiv.org/html/2510.22518v1#bib.bib20)].
This behavioral flow thus represents a multi-agent system in which fairness (γ)(\gamma) and efficiency (λ)(\lambda) jointly determine both satisfaction and aggregate system productivity [[21](https://arxiv.org/html/2510.22518v1#bib.bib21), [22](https://arxiv.org/html/2510.22518v1#bib.bib22), [23](https://arxiv.org/html/2510.22518v1#bib.bib23)].
Healthcare delivery should therefore be modeled as an adaptive ecosystem rather than a static service institution.

At the macro level, micro behavioral adjustments converge toward a system equilibrium shaped by heterogeneity and policy responsiveness [[24](https://arxiv.org/html/2510.22518v1#bib.bib24), [25](https://arxiv.org/html/2510.22518v1#bib.bib25), [26](https://arxiv.org/html/2510.22518v1#bib.bib26)].
Each actor’s fairness–efficiency trade-off (γ,λ)(\gamma,\lambda) affects throughput, waiting times, and total welfare [[27](https://arxiv.org/html/2510.22518v1#bib.bib27), [28](https://arxiv.org/html/2510.22518v1#bib.bib28), [29](https://arxiv.org/html/2510.22518v1#bib.bib29)].
When incentives are misaligned—such as excessive pay-for-performance intensity or rigid penalty systems—local optimizations degrade global outcomes, paralleling bullwhip and congestion phenomena in production and service networks [[30](https://arxiv.org/html/2510.22518v1#bib.bib30), [31](https://arxiv.org/html/2510.22518v1#bib.bib31), [32](https://arxiv.org/html/2510.22518v1#bib.bib32)].
Conversely, adaptive coordination mechanisms that integrate fairness awareness and efficiency learning stabilize the entire ecosystem, enabling Pareto-efficient equilibria with simultaneous gains in QALY and ROI [[21](https://arxiv.org/html/2510.22518v1#bib.bib21), [33](https://arxiv.org/html/2510.22518v1#bib.bib33), [34](https://arxiv.org/html/2510.22518v1#bib.bib34)].
This equilibrium framework analytically links behavioral coefficients to system-level performance metrics, bridging behavioral economics and operations management [[35](https://arxiv.org/html/2510.22518v1#bib.bib35), [36](https://arxiv.org/html/2510.22518v1#bib.bib36), [37](https://arxiv.org/html/2510.22518v1#bib.bib37)].
In doing so, it aligns healthcare optimization with system-level analogues and coordination mechanisms widely studied in contemporary health operations research [[38](https://arxiv.org/html/2510.22518v1#bib.bib38), [39](https://arxiv.org/html/2510.22518v1#bib.bib39)].

To formalize these interactions, we propose the FII loop, a recursive learning framework that captures the adaptive behavior of healthcare systems.
In the forward process, agents implement incentive-driven decisions that yield measurable outcomes—QALY gains, cost reductions, adherence improvements, and ROI shifts [[18](https://arxiv.org/html/2510.22518v1#bib.bib18), [33](https://arxiv.org/html/2510.22518v1#bib.bib33), [23](https://arxiv.org/html/2510.22518v1#bib.bib23)].
In the inverse process, the system infers latent behavioral parameters (λ,γ,T)(\lambda,\gamma,T) by applying data-driven inverse optimization and Bayesian updating techniques [[8](https://arxiv.org/html/2510.22518v1#bib.bib8), [6](https://arxiv.org/html/2510.22518v1#bib.bib6), [27](https://arxiv.org/html/2510.22518v1#bib.bib27), [38](https://arxiv.org/html/2510.22518v1#bib.bib38)].
Finally, the impact process aggregates these behavioral updates to evaluate system-level efficiency, fairness, and resilience, forming a closed feedback loop between micro incentives and macro outcomes [[24](https://arxiv.org/html/2510.22518v1#bib.bib24), [37](https://arxiv.org/html/2510.22518v1#bib.bib37), [14](https://arxiv.org/html/2510.22518v1#bib.bib14), [20](https://arxiv.org/html/2510.22518v1#bib.bib20)].
As illustrated in Fig. [2.1](https://arxiv.org/html/2510.22518v1#S2.F1 "Figure 2.1 ‣ 2 Conceptual Architecture: Adaptive Health Systems and System-Level Learning ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs"), this cyclical architecture reflects the properties of complex adaptive systems and dynamic learning frameworks that characterize modern health operations research [[39](https://arxiv.org/html/2510.22518v1#bib.bib39), [29](https://arxiv.org/html/2510.22518v1#bib.bib29), [34](https://arxiv.org/html/2510.22518v1#bib.bib34)].

![Refer to caption](Fig1.png)


Figure 2.1: Fig. 1 System-level impact loop of adaptive health policy learning
illustrating the interaction between forward health decisions, inverse behavioral learning,
and system-level feedback.
The system evolves through iterative adaptation of fairness (γ)(\gamma), efficiency (λ)(\lambda),
and temporal responsiveness (T)(T), producing measurable improvements in overall health
system performance. Solid arrows indicate the primary analytical flow
(Forward →\rightarrow Inverse →\rightarrow Impact), while dashed arrows represent
feedback and adaptation loops capturing macro-level learning across health systems

## 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs

This section formalizes the behavioral foundations of adaptive health incentive systems
within a unified optimization framework.
Building upon the conceptual architecture introduced in Section [2](https://arxiv.org/html/2510.22518v1#S2 "2 Conceptual Architecture: Adaptive Health Systems and System-Level Learning ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs"),
we now derive a mathematical formulation that links behavioral sensitivity, fairness,
and temporal adaptation to observed QALY–ROI trade-offs.
The model operationalizes the behavioral learning dynamics of health systems through
a forward decision process, an inverse parameter estimation stage, and an equilibrium
identification procedure.
Unlike descriptive behavioral models, this structure enables explicit recovery of
latent incentive parameters from data, allowing empirical inference of
systemic efficiency and fairness trade-offs
[[24](https://arxiv.org/html/2510.22518v1#bib.bib24), [33](https://arxiv.org/html/2510.22518v1#bib.bib33), [8](https://arxiv.org/html/2510.22518v1#bib.bib8), [39](https://arxiv.org/html/2510.22518v1#bib.bib39), [20](https://arxiv.org/html/2510.22518v1#bib.bib20), [34](https://arxiv.org/html/2510.22518v1#bib.bib34)].

### 3.1 Forward Optimization Layer

The forward problem describes how agents—patients, providers, or policymakers—choose actions
at∈𝒜a\_{t}\in\mathcal{A} that balance clinical benefit and cost under behavioral fairness adjustment.
This representation reflects the economic foundations of health technology assessment, where
utility is typically expressed in terms of Quality-Adjusted Life Years (QALY) and cost-effectiveness ratios
[[18](https://arxiv.org/html/2510.22518v1#bib.bib18), [40](https://arxiv.org/html/2510.22518v1#bib.bib40), [41](https://arxiv.org/html/2510.22518v1#bib.bib41)].
At each decision epoch tt, the agent maximizes a fairness-adjusted utility function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxat∈𝒜⁡Ut=(1−γt)​QALY​(at)−γt​Cost​(at),\max\_{a\_{t}\in\mathcal{A}}U\_{t}=(1-\gamma\_{t})\,\mathrm{QALY}(a\_{t})-\gamma\_{t}\,\mathrm{Cost}(a\_{t}), |  | (1) |

subject to diminishing marginal returns and bounded effort [[23](https://arxiv.org/html/2510.22518v1#bib.bib23), [37](https://arxiv.org/html/2510.22518v1#bib.bib37)].
Here, γt∈[0,1]\gamma\_{t}\in[0,1] represents the fairness sensitivity parameter that moderates the trade-off
between clinical efficiency and perceived equity, consistent with behavioral fairness models
in health policy design [[6](https://arxiv.org/html/2510.22518v1#bib.bib6), [27](https://arxiv.org/html/2510.22518v1#bib.bib27), [29](https://arxiv.org/html/2510.22518v1#bib.bib29)].

The first-order condition of ([1](https://arxiv.org/html/2510.22518v1#S3.E1 "In 3.1 Forward Optimization Layer ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")) implies the marginal indifference rule:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂QALY​(at)∂at=γt1−γt​∂Cost​(at)∂at,\frac{\partial\mathrm{QALY}(a\_{t})}{\partial a\_{t}}=\frac{\gamma\_{t}}{1-\gamma\_{t}}\frac{\partial\mathrm{Cost}(a\_{t})}{\partial a\_{t}}, |  | (2) |

which expresses the behavioral equilibrium between incremental health gain and cost fairness adjustment.
This relationship parallels marginal cost–benefit conditions in behavioral operations theory
[[24](https://arxiv.org/html/2510.22518v1#bib.bib24)] and in dynamic incentive learning frameworks
recently introduced in health management science [[9](https://arxiv.org/html/2510.22518v1#bib.bib9), [20](https://arxiv.org/html/2510.22518v1#bib.bib20)].
This layer therefore constitutes the forward component of the learning loop in Fig. [2.1](https://arxiv.org/html/2510.22518v1#S2.F1 "Figure 2.1 ‣ 2 Conceptual Architecture: Adaptive Health Systems and System-Level Learning ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs"),
where observed QALY and ROI outcomes are generated through incentive-driven adaptive actions.

### 3.2 Inverse Estimation Layer

Given empirical data {(at,QALYt)}t=1T\{(a\_{t},\mathrm{QALY}\_{t})\}\_{t=1}^{T},
the inverse problem seeks to recover the latent behavioral parameters (λ,γ,T)(\lambda,\gamma,T)
that rationalize observed outcomes generated by the forward system ([1](https://arxiv.org/html/2510.22518v1#S3.E1 "In 3.1 Forward Optimization Layer ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs"))–([2](https://arxiv.org/html/2510.22518v1#S3.E2 "In 3.1 Forward Optimization Layer ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")).
Unlike standard regression or econometric fitting, this procedure infers the underlying *behavioral objective*
that agents implicitly optimize, rather than merely approximating observed outputs.
This perspective follows the recent paradigm of inverse optimization and behavioral inference
used in health policy modeling and operations management
[[8](https://arxiv.org/html/2510.22518v1#bib.bib8), [6](https://arxiv.org/html/2510.22518v1#bib.bib6), [27](https://arxiv.org/html/2510.22518v1#bib.bib27), [38](https://arxiv.org/html/2510.22518v1#bib.bib38), [42](https://arxiv.org/html/2510.22518v1#bib.bib42)].

Formally, the inverse behavioral optimization problem is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | minλ,γ,T​∑t=1T[QALYt−f​(at;λ,γ,T)]2+β1​(λ−λ0)2+β2​(γ−γ0)2,\min\_{\lambda,\gamma,T}\sum\_{t=1}^{T}\big[\mathrm{QALY}\_{t}-f(a\_{t};\lambda,\gamma,T)\big]^{2}+\beta\_{1}(\lambda-\lambda\_{0})^{2}+\beta\_{2}(\gamma-\gamma\_{0})^{2}, |  | (3) |

where f​(at;λ,γ,T)f(a\_{t};\lambda,\gamma,T) denotes the behavioral response function implied by the forward model ([1](https://arxiv.org/html/2510.22518v1#S3.E1 "In 3.1 Forward Optimization Layer ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")),
and (λ0,γ0)(\lambda\_{0},\gamma\_{0}) represent Bayesian priors or reference values learned from prior periods, meta-analyses, or comparable populations
[[7](https://arxiv.org/html/2510.22518v1#bib.bib7), [43](https://arxiv.org/html/2510.22518v1#bib.bib43), [44](https://arxiv.org/html/2510.22518v1#bib.bib44)].
This estimation structure generalizes traditional cost-effectiveness modeling by embedding it within
a behavioral learning context, aligning with the emerging field of data-driven inverse decision modeling
in healthcare [[29](https://arxiv.org/html/2510.22518v1#bib.bib29), [20](https://arxiv.org/html/2510.22518v1#bib.bib20), [33](https://arxiv.org/html/2510.22518v1#bib.bib33)].

Each parameter carries a distinct behavioral and managerial interpretation:

* •

  λ\lambda (efficiency sensitivity) measures how strongly health agents value return-on-investment (ROI) improvements relative to cost,
  consistent with incentive-aligned policy optimization [[24](https://arxiv.org/html/2510.22518v1#bib.bib24)].
* •

  γ\gamma (fairness preference) quantifies aversion to inequality or excessive expenditure, capturing distributive concerns embedded in
  behavioral health economics and equity-adjusted optimization [[14](https://arxiv.org/html/2510.22518v1#bib.bib14), [34](https://arxiv.org/html/2510.22518v1#bib.bib34)].
* •

  TT (temporal responsiveness) captures the rate at which behavioral adjustments occur, linking short-term incentives to
  long-term learning and adaptive policy feedback, as emphasized in dynamic inverse learning studies [[27](https://arxiv.org/html/2510.22518v1#bib.bib27), [9](https://arxiv.org/html/2510.22518v1#bib.bib9)].

Together, (λ,γ,T)(\lambda,\gamma,T) form a latent behavioral state that governs how rapidly the healthcare system rebalances
between efficiency and fairness over time, producing adaptive responses under evolving incentive regimes.

The regularization term

|  |  |  |
| --- | --- | --- |
|  | Ω​(λ,γ)=β1​(λ−λ0)2+β2​(γ−γ0)2\Omega(\lambda,\gamma)=\beta\_{1}(\lambda-\lambda\_{0})^{2}+\beta\_{2}(\gamma-\gamma\_{0})^{2} |  |

acts as a Bayesian prior that enforces identifiability and robustness of the recovered parameters under noise, temporal drift, or heterogeneous response structures.
Regularization introduces a bias–variance trade-off that mitigates overfitting of behavioral shocks
while preserving interpretability through shrinkage toward reference beliefs (λ0,γ0)(\lambda\_{0},\gamma\_{0})
[[7](https://arxiv.org/html/2510.22518v1#bib.bib7), [42](https://arxiv.org/html/2510.22518v1#bib.bib42), [39](https://arxiv.org/html/2510.22518v1#bib.bib39)].
This formulation can be compactly expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | minλ,γ,T⁡ℒinv​(λ,γ,T)=∑tℓt​(λ,γ,T)⏟inverse loss+Ω​(λ,γ)⏟Bayesian regularizer,\min\_{\lambda,\gamma,T}\;\mathcal{L}\_{\text{inv}}(\lambda,\gamma,T)=\underbrace{\sum\_{t}\ell\_{t}(\lambda,\gamma,T)}\_{\text{inverse loss}}+\underbrace{\Omega(\lambda,\gamma)}\_{\text{Bayesian regularizer}}, |  | (4) |

where each ℓt=[QALYt−f​(at;λ,γ,T)]2\ell\_{t}=[\mathrm{QALY}\_{t}-f(a\_{t};\lambda,\gamma,T)]^{2} measures the deviation between observed and theoretically consistent outcomes.

Conceptually, this inverse layer corresponds to the middle block of the FII loop in Fig. [2.1](https://arxiv.org/html/2510.22518v1#S2.F1 "Figure 2.1 ‣ 2 Conceptual Architecture: Adaptive Health Systems and System-Level Learning ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs"),
transforming observed QALY–ROI trajectories into interpretable behavioral parameters that feed into
system-level impact analysis (Section [4](https://arxiv.org/html/2510.22518v1#S4 "4 SII: Measuring Behavioral Efficiency Gains ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")).
By linking individual behavioral learning to collective system performance,
this layer serves as the analytic bridge between micro-level optimization and macro-level health system design.

### 3.3 Identification and Stability

To ensure interpretability and empirical recoverability of the behavioral parameters,
we impose a mild set of regularity and independence conditions that guarantee a unique and stable inverse solution.

#### Assumptions.

1. (A1)

   Convexity. The behavioral mapping
   f​(at;λ,γ,T)f(a\_{t};\lambda,\gamma,T) in ([3](https://arxiv.org/html/2510.22518v1#S3.E3 "In 3.2 Inverse Estimation Layer ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")) is convex in (λ,γ)(\lambda,\gamma)
   and continuously differentiable in TT.
2. (A2)

   Independence. The exogenous factors (α2,c1,Rt′)(\alpha\_{2},c\_{1},R\_{t}^{\prime}) are linearly independent
   and the observed actions satisfy Var​(at)>0\mathrm{Var}(a\_{t})>0.
3. (A3)

   Regularization. The prior penalty
   Ω​(λ,γ)=β1​(λ−λ0)2+β2​(γ−γ0)2\Omega(\lambda,\gamma)=\beta\_{1}(\lambda-\lambda\_{0})^{2}+\beta\_{2}(\gamma-\gamma\_{0})^{2}
   is strictly convex with β1,β2>0\beta\_{1},\beta\_{2}>0.

###### Proposition 3.1 (Identification and Stability).

Under Assumptions (A1)–(A3), the inverse behavioral loss
ℒinv​(λ,γ,T)\mathcal{L}\_{\text{inv}}(\lambda,\gamma,T) defined in ([4](https://arxiv.org/html/2510.22518v1#S3.E4 "In 3.2 Inverse Estimation Layer ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs"))
admits a unique minimizer (λ∗,γ∗,T∗)(\lambda^{\*},\gamma^{\*},T^{\*}).
Moreover, small perturbations in the data {(at,QALYt)}\{(a\_{t},\mathrm{QALY}\_{t})\}
induce continuous (Lipschitz) changes in the optimal parameters,
ensuring local stability of the recovered behavioral sensitivities.

###### Sketch of Proof.

The strict convexity of Ω​(λ,γ)\Omega(\lambda,\gamma) establishes strong convexity in (λ,γ)(\lambda,\gamma),
while the independence and non-degeneracy of (α2,c1,Rt′)(\alpha\_{2},c\_{1},R\_{t}^{\prime}) guarantee that the residual Jacobian matrix
∇f​(at;λ,γ,T)\nabla f(a\_{t};\lambda,\gamma,T) is full rank.
Applying the first-order optimality condition and the Implicit Function Theorem under bounded
∂f/∂T\partial f/\partial T yields the existence and uniqueness of (λ∗,γ∗,T∗)(\lambda^{\*},\gamma^{\*},T^{\*}).
Continuous dependence on the data follows from standard perturbation arguments for convex programs.
Formal statements and detailed proofs—including Lemma [3.2](https://arxiv.org/html/2510.22518v1#S3.Thmtheorem2 "Lemma 3.2 (Strong Convexity of the Inverse Loss). ‣ Assumptions. ‣ 3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs") and
Theorem [3.3](https://arxiv.org/html/2510.22518v1#S3.Thmtheorem3 "Theorem 3.3 (Identification and Local Stability). ‣ Assumptions. ‣ 3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs") establishing strong convexity and local Lipschitz stability—are
provided in Appendix [A](https://arxiv.org/html/2510.22518v1#A1 "Appendix A Proofs of Theoretical Results ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs").
∎

To strengthen the theoretical foundation of the inverse behavioral optimization model,
we formalize the convexity, existence, and stability results that underpin
Proposition [3.1](https://arxiv.org/html/2510.22518v1#S3.Thmtheorem1 "Proposition 3.1 (Identification and Stability). ‣ Assumptions. ‣ 3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs").
The following Lemma and Theorem establish strong convexity and local identifiability
under the regularity conditions (A1)–(A3).

###### Lemma 3.2 (Strong Convexity of the Inverse Loss).

If f​(at;λ,γ,T)f(a\_{t};\lambda,\gamma,T) is convex in (λ,γ)(\lambda,\gamma)
and continuously differentiable in TT, and if the prior penalty
Ω​(λ,γ)\Omega(\lambda,\gamma) is μ\mu-strongly convex with μ>0\mu>0,
then ℒinv​(λ,γ,T)=∑tℓt​(λ,γ,T)+Ω​(λ,γ)\mathcal{L}\_{\mathrm{inv}}(\lambda,\gamma,T)=\sum\_{t}\ell\_{t}(\lambda,\gamma,T)+\Omega(\lambda,\gamma)
is μ\mu-strongly convex in (λ,γ)(\lambda,\gamma) and continuously differentiable in TT.

###### Sketch of Proof.

By Assumption (A1), each period loss ℓt​(λ,γ,T)=[QALYt−f​(at;λ,γ,T)]2\ell\_{t}(\lambda,\gamma,T)=\big[\mathrm{QALY}\_{t}-f(a\_{t};\lambda,\gamma,T)\big]^{2} is convex in (λ,γ)(\lambda,\gamma).
The sum of convex functions remains convex.
Adding the μ\mu-strongly convex regularizer Ω\Omega ensures the entire objective
is μ\mu-strongly convex in (λ,γ)(\lambda,\gamma) (closure of strong convexity under addition; cf. Rockafellar).
Differentiability in TT follows from the smoothness of ff.
A full proof (including the non-affine extension using Gauss–Newton majorization)
is provided in Appendix [A](https://arxiv.org/html/2510.22518v1#A1 "Appendix A Proofs of Theoretical Results ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs").
∎

###### Theorem 3.3 (Identification and Local Stability).

Under Lemma [3.2](https://arxiv.org/html/2510.22518v1#S3.Thmtheorem2 "Lemma 3.2 (Strong Convexity of the Inverse Loss). ‣ Assumptions. ‣ 3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs") and Assumptions (A1)–(A3),
the inverse behavioral loss admits a unique minimizer
(λ∗,γ∗,T∗)(\lambda^{\ast},\gamma^{\ast},T^{\ast}) satisfying the first-order condition

|  |  |  |
| --- | --- | --- |
|  | ∇θℒinv​(θ∗)=0.\nabla\_{\theta}\mathcal{L}\_{\mathrm{inv}}(\theta^{\ast})=0. |  |

Moreover, (λ∗,γ∗,T∗)(\lambda^{\ast},\gamma^{\ast},T^{\ast}) depends Lipschitz-continuously on
data perturbations {(at,QALYt)}\{(a\_{t},\mathrm{QALY}\_{t})\}, ensuring local stability.

###### Sketch of Proof.

*Uniqueness:* For fixed TT, Lemma [3.2](https://arxiv.org/html/2510.22518v1#S3.Thmtheorem2 "Lemma 3.2 (Strong Convexity of the Inverse Loss). ‣ Assumptions. ‣ 3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs") guarantees
μ\mu-strong convexity in (λ,γ)(\lambda,\gamma), hence a unique minimizer.
*Existence and joint identification:*
Define F​(θ;𝒟)=∇θℒinv​(θ;𝒟)F(\theta;\mathcal{D})=\nabla\_{\theta}\mathcal{L}\_{\mathrm{inv}}(\theta;\mathcal{D}),
with data 𝒟={(at,QALYt)}t\mathcal{D}=\{(a\_{t},\mathrm{QALY}\_{t})\}\_{t}.
Assumption (A2) ensures ∇θF​(θ∗;𝒟)\nabla\_{\theta}F(\theta^{\ast};\mathcal{D}) is nonsingular;
the Implicit Function Theorem guarantees the existence, uniqueness, and continuous dependence
of θ∗=(λ∗,γ∗,T∗)\theta^{\ast}=(\lambda^{\ast},\gamma^{\ast},T^{\ast}) on the data.
*Local Lipschitz stability:*
Perturbing 𝒟\mathcal{D} to 𝒟′\mathcal{D}^{\prime} yields

|  |  |  |
| --- | --- | --- |
|  | ‖θ^−θ^′‖≤L𝒟μ​‖𝒟−𝒟′‖,\|\hat{\theta}-\hat{\theta}^{\prime}\|\leq\frac{L\_{\mathcal{D}}}{\mu}\|\mathcal{D}-\mathcal{D}^{\prime}\|, |  |

where L𝒟L\_{\mathcal{D}} bounds the gradient’s sensitivity to data.
Hence the parameter mapping is locally Lipschitz continuous.
A full derivation appears in Appendix [A](https://arxiv.org/html/2510.22518v1#A1 "Appendix A Proofs of Theoretical Results ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs").
∎

###### Corollary 3.4 (Economic Stability of Behavioral Equilibria).

Small policy or data perturbations induce proportionally bounded changes in
the recovered behavioral sensitivities (λ∗,γ∗,T∗)(\lambda^{\ast},\gamma^{\ast},T^{\ast}),
ensuring convergence of adaptive health systems toward a stable fairness–efficiency equilibrium.

###### Sketch of Proof.

From Theorem [3.3](https://arxiv.org/html/2510.22518v1#S3.Thmtheorem3 "Theorem 3.3 (Identification and Local Stability). ‣ Assumptions. ‣ 3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs"), the estimator is locally Lipschitz in the data.
Policy shocks act as bounded perturbations, so parameter shifts are O​(‖Δ​𝒟‖)O(\|\Delta\mathcal{D}\|).
Because the forward mapping ([2](https://arxiv.org/html/2510.22518v1#S3.E2 "In 3.1 Forward Optimization Layer ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")) and the impact layer
are continuously differentiable in (λ,γ,T)(\lambda,\gamma,T),
the resulting equilibrium trajectories remain in a neighborhood of the baseline fixed point,
ensuring economic and behavioral stability.
Full details appear in Appendix [A](https://arxiv.org/html/2510.22518v1#A1 "Appendix A Proofs of Theoretical Results ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs").
∎

Proposition [3.1](https://arxiv.org/html/2510.22518v1#S3.Thmtheorem1 "Proposition 3.1 (Identification and Stability). ‣ Assumptions. ‣ 3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs") implies that
the observed QALY–ROI trade-offs encode a unique behavioral signature (λ∗,γ∗,T∗)(\lambda^{\*},\gamma^{\*},T^{\*})
that characterizes the efficiency–fairness balance of the health system.
Convexity ensures that agents respond predictably to marginal incentive changes,
while stability implies that small policy shocks do not generate chaotic or degenerate equilibria.
Economically, this property guarantees that adaptive incentive systems
converge toward consistent behavioral equilibria rather than oscillating between conflicting fairness–efficiency regimes.

The recovered parameters (λ∗,γ∗,T∗)(\lambda^{\*},\gamma^{\*},T^{\*})
form the structural bridge between individual behavioral learning and system-level outcomes.
They are propagated to the system-level Impact Layer (Section [4](https://arxiv.org/html/2510.22518v1#S4 "4 SII: Measuring Behavioral Efficiency Gains ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")),
where the implications for aggregate productivity, equity, and resilience are quantified.

Table 3.1: Summary of notation used throughout the Inverse Behavioral Optimization and System Impact framework.

|  |  |  |
| --- | --- | --- |
| Symbol | Type | Description |
| Indices and Sets | | |
| t=1,…,Tt=1,\dots,T | Index | Decision epoch or time period. |
| 𝒜\mathcal{A} | Set | Feasible set of health actions or policy levers. |
| Decision and Outcome Variables | | |
| ata\_{t} | Decision | Action or intervention chosen at time tt. |
| QALY​(at)\mathrm{QALY}(a\_{t}) | Function | Health outcome (quality-adjusted life years) from action ata\_{t}. |
| Cost​(at)\mathrm{Cost}(a\_{t}) | Function | Expenditure or resource cost associated with ata\_{t}. |
| ROIt\mathrm{ROI}\_{t} | Scalar | Return-on-investment for period tt. |
| Behavioral Parameters | | |
| λ\lambda | Scalar | Efficiency sensitivity (weight on ROI improvements). |
| γt\gamma\_{t} | Scalar | Fairness preference moderating efficiency–equity trade-off. |
| TT | Scalar | Temporal responsiveness or adaptation rate. |
| (λ∗,γ∗,T∗)(\lambda^{\*},\gamma^{\*},T^{\*}) | Vector | Estimated behavioral equilibrium parameters. |
| Optimization Layers | | |
| UtU\_{t} | Function | Fairness-adjusted utility function (Eq. [1](https://arxiv.org/html/2510.22518v1#S3.E1 "In 3.1 Forward Optimization Layer ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")). |
| f​(at;λ,γ,T)f(a\_{t};\lambda,\gamma,T) | Function | Behavioral response function mapping actions to outcomes. |
| ℒinv​(λ,γ,T)\mathcal{L}\_{\text{inv}}(\lambda,\gamma,T) | Function | Inverse loss function (Eq. [4](https://arxiv.org/html/2510.22518v1#S3.E4 "In 3.2 Inverse Estimation Layer ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")). |
| Ω​(λ,γ)\Omega(\lambda,\gamma) | Function | Bayesian regularizer enforcing prior consistency. |
| Derived Quantities | | |
| S​I​ISII | Scalar | System Impact Index (Eq. [5](https://arxiv.org/html/2510.22518v1#S4.E5 "In 4.1 Definition ‣ 4 SII: Measuring Behavioral Efficiency Gains ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")). |
| S​I​ItSII\_{t} | Scalar | Time-varying dynamic impact index (Eq. [6](https://arxiv.org/html/2510.22518v1#S4.E6 "In 4.2 Analytical Structure ‣ 4 SII: Measuring Behavioral Efficiency Gains ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")). |
| SθS\_{\theta} | Scalar | Sensitivity coefficient for parameter θ∈{λ,γ,T}\theta\in\{\lambda,\gamma,T\}. |
| ρ\rho | Scalar | Behavioral decay rate controlling adaptation penalty. |
| Analytical Constructs | | |
| ℓt​(λ,γ,T)\ell\_{t}(\lambda,\gamma,T) | Function | Period-wise inverse loss component. |
| β1,β2\beta\_{1},\beta\_{2} | Scalars | Regularization hyperparameters. |
| η\eta | Scalar | Learning rate in temporal update rule. |
| 𝒯t\mathcal{T}\_{t} | Operator | Behavioral update operator for time tt. |
| Statistical and Evaluation Metrics | | |
| MSE\mathrm{MSE} | Metric | Mean squared error of predicted QALY outcomes. |
| R2\mathrm{R}^{2} | Metric | Goodness-of-fit for behavioral response regression. |
| SII​-Gain\mathrm{SII\text{-Gain}} | Metric | Percentage increase in system impact after adaptation. |
| Elasticity(λ,γ)\mathrm{Elasticity}\_{(\lambda,\gamma)} | Metric | Impact elasticity with respect to fairness–efficiency trade-off. |

Notation is consistent with the hierarchical structure of Sections [3](https://arxiv.org/html/2510.22518v1#S3 "3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")–[4](https://arxiv.org/html/2510.22518v1#S4 "4 SII: Measuring Behavioral Efficiency Gains ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs").
Behavioral parameters (λ,γ,T)(\lambda,\gamma,T) are estimated through the inverse optimization problem ([3](https://arxiv.org/html/2510.22518v1#S3.E3 "In 3.2 Inverse Estimation Layer ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")),
and propagated to the system-level analysis in Section [5](https://arxiv.org/html/2510.22518v1#S5 "5 System-Level Simulation and Policy Sensitivity Analysis ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs").
system impact measures (SII and its derivatives) serve as quantitative links between behavioral efficiency and macroeconomic performance.

## 4 SII: Measuring Behavioral Efficiency Gains

This section introduces the SII,
a composite metric that quantifies how much behavioral adaptation improves the overall productivity and fairness balance
of an incentive-driven health system.
It translates the micro-level behavioral parameters (λ∗,γ∗,T∗)(\lambda^{\*},\gamma^{\*},T^{\*}) recovered in Section [3.3](https://arxiv.org/html/2510.22518v1#S3.SS3 "3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")
into measurable system-level outcomes, bridging the analytical gap between behavioral learning and system efficiency.

### 4.1 Definition

We define the System Impact Index (SII) as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​I​I=QALY Improvement per PeriodMarginal ROI Cost⋅(1−γ∗),SII=\frac{\text{QALY Improvement per Period}}{\text{Marginal ROI Cost}}\cdot(1-\gamma^{\*}), |  | (5) |

where

* •

  QALY Improvement per Period measures the incremental clinical benefit gained through adaptive learning,
  relative to a static benchmark,
* •

  Marginal ROI Cost denotes the additional cost required to achieve that improvement,
  capturing the system’s cost elasticity, and
* •

  (1−γ∗)(1-\gamma^{\*}) discounts the measured efficiency by the estimated fairness preference recovered from the inverse model

Thus, S​I​ISII reflects the *behaviorally adjusted efficiency-to-cost ratio*—that is, the degree to which learning and fairness jointly enhance
systemic performance.

### 4.2 Analytical Structure

Let Δ​QALYt=QALYt−QALYt−1\Delta\mathrm{QALY}\_{t}=\mathrm{QALY}\_{t}-\mathrm{QALY}\_{t-1}
and Δ​ROIt=ROIt−ROIt−1\Delta\mathrm{ROI}\_{t}=\mathrm{ROI}\_{t}-\mathrm{ROI}\_{t-1} denote marginal changes over consecutive periods.
Then the empirical System Impact Index can be estimated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​I​It=λ∗⋅Δ​QALYtΔ​ROIt⋅(1−γ∗)⋅e−ρ​(1−T∗),SII\_{t}=\lambda^{\*}\cdot\frac{\Delta\mathrm{QALY}\_{t}}{\Delta\mathrm{ROI}\_{t}}\cdot(1-\gamma^{\*})\cdot e^{-\rho(1-T^{\*})}, |  | (6) |

where ρ\rho represents the behavioral decay rate (speed of learning loss).
The exponential adjustment e−ρ​(1−T∗)e^{-\rho(1-T^{\*})} penalizes slow temporal responsiveness (T∗<1T^{\*}<1),
ensuring that systems with faster adaptation achieve higher system impact.

Equation ([6](https://arxiv.org/html/2510.22518v1#S4.E6 "In 4.2 Analytical Structure ‣ 4 SII: Measuring Behavioral Efficiency Gains ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")) implies that
behavioral parameters estimated via inverse optimization directly determine the macro-level efficiency elasticity of the system:

|  |  |  |
| --- | --- | --- |
|  | ∂S​I​It∂λ∗>0,∂S​I​It∂γ∗<0,∂S​I​It∂T∗>0.\frac{\partial SII\_{t}}{\partial\lambda^{\*}}>0,\quad\frac{\partial SII\_{t}}{\partial\gamma^{\*}}<0,\quad\frac{\partial SII\_{t}}{\partial T^{\*}}>0. |  |

Hence, increasing efficiency sensitivity or faster adaptation yields larger system gains,
while excessive fairness weighting may reduce short-term productivity—mirroring trade-offs observed in public health systems
[[33](https://arxiv.org/html/2510.22518v1#bib.bib33), [20](https://arxiv.org/html/2510.22518v1#bib.bib20), [29](https://arxiv.org/html/2510.22518v1#bib.bib29), [34](https://arxiv.org/html/2510.22518v1#bib.bib34)].

### 4.3 Interpretation and Managerial Implications

A higher S​I​ISII indicates that behavioral adaptation produces system-level improvements
that exceed baseline efficiency thresholds and generate positive externalities across the healthcare industry.
From a managerial perspective, S​I​ISII functions as an impact elasticity metric:
it quantifies how one unit of behavioral learning translates into measurable system outcomes such as
cost efficiency, patient equity, and institutional resilience.

Incentive programs with consistently rising S​I​ISII values demonstrate
that behavioral calibration enhances both economic and clinical performance without destabilizing fairness constraints.
Conversely, declining S​I​ISII trajectories may signal policy misalignment or behavioral saturation.
Thus, the S​I​ISII serves as a diagnostic and design tool for adaptive health policy evaluation,
complementing traditional cost-effectiveness metrics such as incremental cost per QALY gained
[[18](https://arxiv.org/html/2510.22518v1#bib.bib18), [40](https://arxiv.org/html/2510.22518v1#bib.bib40), [9](https://arxiv.org/html/2510.22518v1#bib.bib9)].

## 5 System-Level Simulation and Policy Sensitivity Analysis

To bridge the theoretical framework in Section [3](https://arxiv.org/html/2510.22518v1#S3 "3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs") and the empirical validation in Section [6](https://arxiv.org/html/2510.22518v1#S6 "6 Empirical Validation and Policy Implications ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs"),
we conduct a system-level simulation that quantifies how variations in behavioral sensitivities
(λ,γ,T)(\lambda,\gamma,T) influence the SII and aggregate healthcare performance.
This intermediate layer captures how micro-level behavioral adjustments propagate through macro-level system dynamics,
serving as a bridge between analytical propositions and real-world policy implications.

### 5.1 Simulation Design

We simulate a stylized healthcare system consisting of NN interacting regional units,
each characterized by estimated behavioral parameters (λi,γi,Ti)(\lambda\_{i},\gamma\_{i},T\_{i}).
The simulated QALY–ROI dynamics follow the behavioral propagation rule:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​QALYi,t=λi​(1−γi)​Δ​ROIi,t+εi,t,εi,t∼𝒩​(0,σ2),\Delta\mathrm{QALY}\_{i,t}=\lambda\_{i}(1-\gamma\_{i})\,\Delta\mathrm{ROI}\_{i,t}+\varepsilon\_{i,t},\quad\varepsilon\_{i,t}\sim\mathcal{N}(0,\sigma^{2}), |  | (7) |

where λi\lambda\_{i} denotes efficiency responsiveness, γi\gamma\_{i} represents fairness moderation,
and εi,t\varepsilon\_{i,t} captures stochastic behavioral noise.
The temporal evolution of adaptation is governed by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ti,t+1=Ti,t+η​(T∗−Ti,t),T\_{i,t+1}=T\_{i,t}+\eta(T^{\*}-T\_{i,t}), |  | (8) |

where η\eta is the behavioral learning rate and T∗T^{\*} is the steady-state responsiveness estimated in Section [3.3](https://arxiv.org/html/2510.22518v1#S3.SS3 "3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs").
Together, Eqs. ([7](https://arxiv.org/html/2510.22518v1#S5.E7 "In 5.1 Simulation Design ‣ 5 System-Level Simulation and Policy Sensitivity Analysis ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs"))–([8](https://arxiv.org/html/2510.22518v1#S5.E8 "In 5.1 Simulation Design ‣ 5 System-Level Simulation and Policy Sensitivity Analysis ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")) describe a recursive feedback system that
converges toward a stable behavioral equilibrium (λ∗,γ∗,T∗)(\lambda^{\*},\gamma^{\*},T^{\*}) identified in Proposition [3.1](https://arxiv.org/html/2510.22518v1#S3.Thmtheorem1 "Proposition 3.1 (Identification and Stability). ‣ Assumptions. ‣ 3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs").

### 5.2 Sensitivity Analysis of Behavioral Parameters

To assess the macroeconomic implications of behavioral changes,
we perturb each parameter by ±8%\pm 8\% around its equilibrium value and compute the resulting change
in the S​I​ISII:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sθ=∂S​I​I∂θ≈S​I​I​(θ+Δ​θ)−S​I​I​(θ−Δ​θ)2​Δ​θ,θ∈{λ,γ,T}.S\_{\theta}=\frac{\partial SII}{\partial\theta}\approx\frac{SII(\theta+\Delta\theta)-SII(\theta-\Delta\theta)}{2\Delta\theta},\quad\theta\in\{\lambda,\gamma,T\}. |  | (9) |

Intuitively, SλS\_{\lambda} reflects productivity leverage, SγS\_{\gamma} captures distributive damping,
and STS\_{T} measures temporal agility within the system’s adaptive response.
Positive SλS\_{\lambda} and STS\_{T}, coupled with a negative SγS\_{\gamma}, confirm the directional elasticities predicted by
Eq. ([6](https://arxiv.org/html/2510.22518v1#S4.E6 "In 4.2 Analytical Structure ‣ 4 SII: Measuring Behavioral Efficiency Gains ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")), aligning theoretical expectations with simulation outcomes.

### 5.3 Simulation Results and System Interpretation

The simulated trajectories indicate that increasing efficiency sensitivity (λ)(\lambda)
yields rapid improvements in short-term ROI but diminishing QALY gains beyond a threshold.
Conversely, moderate fairness preference (γ≈0.35(\gamma\approx 0.35–0.45)0.45) maximizes the steady-state S​I​ISII,
achieving a balanced trade-off between cost containment and health equity.
Higher temporal responsiveness (T)(T) accelerates convergence toward equilibrium,
enhancing resilience and adaptive recovery under policy shocks.

![Refer to caption](Fig2.png)


Figure 5.1: System-level simulation and behavioral sensitivity analysis.
(a) Elasticity surface of the S​I​I​(λ,γ)SII(\lambda,\gamma) shows concave diminishing returns in efficiency beyond moderate fairness levels.
(b) Policy sensitivity analysis quantifies elasticities (Sλ,Sγ,ST)(S\_{\lambda},S\_{\gamma},S\_{T}) with respect to efficiency, fairness, and adaptation parameters




Table 5.1: Sensitivity coefficients and implied macroeconomic elasticities

| Parameter | Symbol | Elasticity SθS\_{\theta} | System Interpretation |
| --- | --- | --- | --- |
| Efficiency sensitivity | λ\lambda | +0.50+0.50 | 10–12% productivity leverage (ROI gain) |
| Fairness preference | γ\gamma | −0.57-0.57 | 5–7% efficiency moderation (budget damping) |
| Temporal responsiveness | TT | +0.54+0.54 | 20–25% faster post-shock recovery |

Economically, these simulation-based results suggest that a 10% increase in efficiency sensitivity (λ)(\lambda)
translates into an approximate 0.6–0.8 percentage-point improvement in sectoral healthcare productivity,
equivalent to a 0.6–1.0% increase in national healthcare GDP share.
Likewise, enhancing adaptive responsiveness (T)(T) by one standard deviation yields a 20–25% faster post-shock recovery rate,
reducing equilibrium adjustment lag from 5.2 to 3.9 quarters.
Conversely, overemphasis on fairness (γ>0.6)(\gamma>0.6) introduces allocative inertia and a 3–5% contraction in net efficiency.
Taken together, these findings underscore the system significance of behavioral calibration:
small parameter shifts can scale to macroeconomic gains on the order of 0.8–1.0% of sectoral output.

### 5.4 Policy-Level Validation: Adaptive vs. Baseline Design

To verify whether the simulated sensitivities manifest in real-world policy outcomes,
we compare the S​I​ISII under two regimes—Baseline Policy and Adaptive Policy—across
three behavioral dimensions (λ,γ,T)(\lambda,\gamma,T).
Figure [5.2](https://arxiv.org/html/2510.22518v1#S5.F2 "Figure 5.2 ‣ 5.4 Policy-Level Validation: Adaptive vs. Baseline Design ‣ 5 System-Level Simulation and Policy Sensitivity Analysis ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs") presents the comparative results from Monte Carlo experiments
using configuration parameters summarized in Appendix B.
The Adaptive Policy consistently outperforms the Baseline Policy across all dimensions,
with the largest gain observed in temporal adaptation.

![Refer to caption](Fig3.png)


Figure 5.2: Policy effect by behavioral dimension.
Comparison between Baseline and Adaptive policies across efficiency (λ)(\lambda), fairness (γ)(\gamma), and adaptation (T)(T) dimensions.
Error bars denote standard errors (20 simulation replications).
Asterisks indicate significance levels (\* p<0.05p<0.05, \*\* p<0.01p<0.01, \*\*\* p<0.001p<0.001)

### 5.5 Managerial and Policy Implications

The results highlight a behavioral equilibrium region in which system productivity and fairness coexist.
From a managerial and policy standpoint, three actionable insights emerge:

1. (i)

   Efficiency leverage: Incremental reinforcement of efficiency sensitivity (λ)(\lambda)
   improves ROI without destabilizing fairness as long as γ<0.5\gamma<0.5.
   A 1% rise in λ\lambda generates approximately a 0.08% gain in sectoral output.
2. (ii)

   Fairness calibration: Overemphasis on fairness (γ>0.6)(\gamma>0.6) introduces allocative inertia,
   leading to a 3–5% reduction in system-wide efficiency and slower recovery.
3. (iii)

   Adaptive learning: Higher responsiveness (T)(T) supports faster convergence to stable equilibria,
   reducing post-shock recovery time by 25–30%, thereby enhancing system resilience to policy transitions.

Economically, these simulation-based results suggest that a 10% increase in efficiency sensitivity (λ)(\lambda)
translates into an approximate 0.6–0.8 percentage-point improvement in sectoral healthcare productivity,
equivalent to a 0.6–1.0% increase in national healthcare GDP share.
Likewise, enhancing adaptive responsiveness (T)(T) by one standard deviation yields a 20–25% faster post-shock recovery rate,
reducing equilibrium adjustment lag from 5.2 to 3.9 quarters.
Conversely, overemphasis on fairness (γ>0.6)(\gamma>0.6) introduces allocative inertia and a 3–5% contraction in net efficiency.
Taken together, these findings underscore the industrial and macroeconomic significance of behavioral calibration:
small parameter shifts can propagate into system-wide gains on the order of 0.8–1.0% of sectoral output.

## 6 Empirical Validation and Policy Implications

### 6.1 Data and Calibration

We validate the proposed inverse behavioral optimization framework using
the merged OECD–WHO dataset (2007–2021; n=34,023n=34{,}023), which integrates
national health expenditure (PPP-adjusted per capita) and life expectancy
as a QALY proxy.
All monetary variables are normalized by per-patient cost units to ensure
cross-country comparability.
The System Impact Index (SII) is computed as

|  |  |  |
| --- | --- | --- |
|  | SII=LifeExpectancy×ln⁡(1+HealthSpending)100,\mathrm{SII}=\frac{\mathrm{LifeExpectancy}\times\ln(1+\mathrm{HealthSpending})}{100}, |  |

representing a macro-level measure of behavioral efficiency and equity
in national health systems.
Behavioral sensitivities (λ,γ,T)(\lambda,\gamma,T) were estimated through a
reduced-form inverse regression of SII on health spending and life expectancy,
and the dynamic responsiveness parameter TT was calibrated by fitting an
AR(1) process on annual changes in SII for each country.
All estimations and policy simulations were implemented in
Python 3.10 using fully reproducible open-source scripts
provided in the Supplement.

Table 6.1: OECD–WHO merged data and reduced-form estimation summary00footnotetext: Source: Author’s calculation based on merged OECD–WHO data (2007–2021).

|  | Mean | Std. | Min | Max |
| --- | --- | --- | --- | --- |
| Year | 2014.21 | 4.31 | 2007 | 2021 |
| Health Spending (USD PPP) | 144,217 | 929,942 | 0.01 | 29,454,160 |
| Life Expectancy (yrs) | 79.08 | 4.32 | 51.0 | 87.4 |
| SII | 5.00 | 3.41 | 0.01 | 14.32 |
| \botrule |  |  |  |  |

|  |  |  |
| --- | --- | --- |
| Parameter | Estimate | Interpretation |
| OLS slope (∂S​I​I/∂ln⁡(H​S))(\partial SII/\partial\ln(HS)) | 0.794 | Efficiency scaling coefficient |
| Intercept | −0.017-0.017 | Baseline offset |
| λ^\hat{\lambda} | 0.999 | Efficiency sensitivity (saturated) |
| γ^\hat{\gamma} | 0.007 | Fairness preference (neutral) |
| T^\hat{T} | 1.000 | Temporal responsiveness (immediate) |
| \botrule |  |  |

### 6.2 Empirical Results and Discussion

Empirical estimation yields behavioral coefficients
(λ^,γ^,T^)=(0.999, 0.007, 1.000)(\hat{\lambda},\hat{\gamma},\hat{T})=(0.999,\,0.007,\,1.000).
These values indicate that the global health economy operates within an
*efficiency-dominant regime*, where efficiency sensitivity (λ\lambda)
is nearly saturated, fairness preference (γ\gamma) is negligible, and
adaptation is nearly instantaneous (T≈1T\!\approx\!1).
Such a configuration is consistent with ROI-driven system optimization
observed in mature OECD health markets.

![Refer to caption](Fig4.png)


Figure 6.1: 
Empirical behavioral validation and policy sensitivity analysis.
(a) S​I​ISII versus health spending (OECD–WHO data) showing near-linear scaling (∂S​I​I/∂log⁡(H​S)=0.79\partial SII/\partial\log(HS)=0.79).
(b) Counterfactual distributions of SII under fairness-oriented policy (Δ​S​I​I=−19.7%\Delta SII=-19.7\%).
(c) Behavioral elasticities demonstrating efficiency dominance (Sλ≈1.01S\_{\lambda}\approx 1.01) and fairness saturation (Sγ≈0S\_{\gamma}\approx 0).
(d) Policy gain field illustrating the behavioral trade-off between efficiency and fairness.
Together, the panels confirm an efficiency-dominant equilibrium with measurable trade-offs under fairness interventions.

Panel (a) of Figure [6.1](https://arxiv.org/html/2510.22518v1#S6.F1 "Figure 6.1 ‣ 6.2 Empirical Results and Discussion ‣ 6 Empirical Validation and Policy Implications ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs") shows near-linear scaling between health spending and SII
(∂SII/∂ln⁡(H​S)=0.79\partial\mathrm{SII}/\partial\ln(HS)\!=\!0.79), confirming that
marginal productivity of health expenditure remains positive but saturates at higher spending levels.
Panel (b) shows counterfactual shifts:
a fairness-intensive regime (γ′=γ+0.2\gamma^{\prime}\!=\!\gamma\!+\!0.2) reduces SII
by approximately 19.7%, whereas efficiency- or adaptation-oriented regimes
yield negligible change (Δ​SII≤0.1%\Delta\mathrm{SII}\!\leq\!0.1\%).
Panels (c)–(d) visualize the elasticity and policy gain field,
showing that only λ\lambda significantly influences macro performance
(Sλ≈1.01S\_{\lambda}\!\approx\!1.01), while fairness and adaptation remain statistically neutral.

Table 6.2: Behavioral elasticity and robustness summary00footnotetext: Monte Carlo perturbations (±10%\pm 10\%) produced stable elasticities:
(Sλ,Sγ,ST)∈(0.47(S\_{\lambda},S\_{\gamma},S\_{T})\in(0.47–0.53,−0.590.53,\,-0.59–−0.55, 0.50-0.55,\,0.50–0.57)0.57),
confirming numerical robustness of the inferred behavioral parameters.

| Parameter | Elasticity (SθS\_{\theta}) | Interpretation |
| --- | --- | --- |
| λ\lambda | +1.01+1.01 | Dominant efficiency response |
| γ\gamma | −0.007-0.007 | Minimal fairness impact |
| TT | +0.000+0.000 | Instantaneous adaptation |
| \botrule |  |  |

From a policy perspective, these findings imply that OECD health systems
lie on a *behavioral efficiency frontier*.
Further efficiency-oriented reforms generate diminishing returns,
while fairness-based redistributive interventions may reduce
aggregate productivity.
The optimal principle is thus *fairness-corrected efficiency*—
maintaining high ROI while offsetting the 15–20% efficiency erosion
that accompanies equity-driven policies.
At the system level, the dominance of λ\lambda and immediacy of TT
indicate strong absorptive capacity for technological and institutional
innovation (e.g., digital health, AI-assisted care),
reinforcing healthcare’s position as a rapid-adaptation industry.

### 6.3 Behavioral Saturation and Robustness

![Refer to caption](Fig5.png)


Figure 6.2: Robustness of behavioral estimation and sensitivity analysis.
(a) Monte Carlo perturbations (±10%\pm 10\%) confirm stability of inferred
elasticities across behavioral parameters λ\lambda, γ\gamma, and TT.
(b) Parameter trajectories demonstrate convergence consistency over iterations,
indicating a numerically stable equilibrium.
(c) The sensitivity field Δ​S​I​I​(λ,γ)\Delta SII(\lambda,\gamma) visualizes the smooth
trade-off between efficiency and fairness responses

The elasticity landscape reveals a *saturated efficiency frontier*
(Sλ≈1S\_{\lambda}\!\approx\!1), indicating that marginal efficiency incentives
translate nearly one-to-one into system-level gains.
By contrast, fairness (Sγ≈0S\_{\gamma}\!\approx\!0) and temporal adaptivity (ST≈0S\_{T}\!\approx\!0)
exhibit negligible sensitivity, suggesting a behavioral steady state
where additional redistribution or adaptation yields minimal marginal benefit.
This structural rigidity reflects how efficiency-optimized systems
reinforce existing equilibria and resist redistributive or adaptive reforms.

Monte Carlo perturbations and iterative inverse-learning simulations
(Figure [6.2](https://arxiv.org/html/2510.22518v1#S6.F2 "Figure 6.2 ‣ 6.3 Behavioral Saturation and Robustness ‣ 6 Empirical Validation and Policy Implications ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")) confirm this directional stability:
(λt,γt,Tt)(\lambda\_{t},\gamma\_{t},T\_{t}) quickly converge to (1.00,0.00,1.00)(1.00,0.00,1.00) and remain stable across iterations.
The two-dimensional sensitivity field Δ​S​I​I​(λ,γ)\Delta SII(\lambda,\gamma) forms
a smooth, monotonic gradient, indicating continuous rather than abrupt policy trade-offs.
Alternative specifications—including fixed effects, income-tier subsamples,
and log-transformed SII—yield consistent qualitative patterns.
Together, these findings confirm that efficiency saturation and
the fairness–efficiency gradient are intrinsic to the system equilibrium,
not artifacts of model specification.

Efficiency-oriented policies therefore represent an
*evolutionarily stable strategy*: while highly effective in driving productivity,
they may become brittle under exogenous shocks,
underscoring the need for adaptive and redistributive mechanisms
to maintain long-run system resilience.

## 7 Conclusion

This study advances the analytical frontier of health-care management by showing that behavioral optimization, when formulated as a learning-based inverse problem, can quantitatively explain macro-level performance.
By recovering latent behavioral parameters (λ,γ,T)(\lambda,\gamma,T) from observed QALY–ROI trade-offs, we establish a bridge between micro-level incentives and system-level efficiency.
The empirical results suggest that modern health systems operate near an adaptive efficiency frontier—highly responsive to efficiency sensitivity (λ)(\lambda) yet showing diminishing marginal responsiveness in fairness (γ)(\gamma) and temporal adaptation (T)(T).
This structural pattern reveals a form of behavioral rigidity in the global health economy: efficient, but increasingly vulnerable to redistributive and adaptive shocks.

Beyond empirical validation, this research develops a new theoretical foundation for behavioral inference in health systems through the FII framework.
Unlike traditional econometric or DEA models [[45](https://arxiv.org/html/2510.22518v1#bib.bib45), [46](https://arxiv.org/html/2510.22518v1#bib.bib46), [47](https://arxiv.org/html/2510.22518v1#bib.bib47)], which view performance frontiers as fixed and exogenous, the FOSSIL paradigm endogenizes behavioral sensitivity and allows the frontier itself to evolve through data.
This regret-minimizing and sample-sensitive structure [[10](https://arxiv.org/html/2510.22518v1#bib.bib10)] reframes efficiency analysis as a dynamic learning process, connecting operations research, behavioral economics, and health policy in a unified optimization model.
The approach departs from conventional QALY–ROI analyses and provides a generalizable methodological template for learning-driven health-system modeling.

By integrating OECD–WHO macro data with structural inverse estimation, we find that adaptive behavioral trade-offs explain nearly 90% of cross-country variation in health outcomes.
The proposed System Impact Index (SII) captures how incremental behavioral shifts translate into measurable productivity, offering a direct link between learning and policy outcomes.
Elasticity estimates indicate that a 1% rise in efficiency sensitivity can yield 0.2–2.0% gains in sectoral output, while fairness-oriented adjustments—though slower in effect—enhance long-term stability and institutional trust [[48](https://arxiv.org/html/2510.22518v1#bib.bib48), [49](https://arxiv.org/html/2510.22518v1#bib.bib49)].
These findings redefine health systems as adaptive industries whose performance evolves through behavioral learning rather than static optimization.
Unlike traditional DEA or cost-effectiveness models, which assess efficiency retrospectively, the FOSSIL-based framework embeds learning *within* the policy process, enabling real-time calibration of incentive parameters through data-driven feedback.
This provides a foundation for adaptive policy design in which fairness, efficiency, and responsiveness are jointly optimized under uncertainty.
Practically, it offers governments and international organizations a quantitative mechanism to monitor and recalibrate national health investment portfolios in real time.
Beyond healthcare, the empirical framework can extend to other welfare-critical systems—such as education, energy, and climate—where behavioral adaptation and equity–efficiency trade-offs shape long-term resilience.

Conceptually, this study situates health-care management within the emerging paradigm of *learning-based system optimization*.
By bridging inverse optimization, behavioral inference, and data-driven policy design, it advances a unified analytical structure for studying behavioral governance.
The FOSSIL framework, first proposed in Cha et al. [[10](https://arxiv.org/html/2510.22518v1#bib.bib10)] and extended here to the QALY–ROI context, formalizes how adaptive learning and behavioral sensitivity jointly determine macro-level efficiency.
This integration moves beyond disciplinary boundaries, linking health economics and operations research to broader questions of institutional adaptability.
By demonstrating that behavioral learning can be quantified and projected across scales, this study provides a replicable blueprint for analyzing other complex systems—education, energy, or climate—where fairness–efficiency trade-offs define system evolution [[50](https://arxiv.org/html/2510.22518v1#bib.bib50), [51](https://arxiv.org/html/2510.22518v1#bib.bib51), [52](https://arxiv.org/html/2510.22518v1#bib.bib52)].
In both scope and originality, it contributes to the broader movement in operations and management research toward dynamic, learning-centered policy models.

While the behavioral parameters (λ,γ,T)(\lambda,\gamma,T) capture essential aspects of decision sensitivity, they abstract from institutional heterogeneity and cultural variation in fairness perception.
Future work integrating micro-level provider data, hierarchical Bayesian updating, and digital-twin simulation could enhance behavioral granularity and support real-time adaptive policymaking.
Combining the FII framework with reinforcement learning and robust control [[53](https://arxiv.org/html/2510.22518v1#bib.bib53), [54](https://arxiv.org/html/2510.22518v1#bib.bib54)] represents another promising direction for developing a general theory of learning-based system policy design.
Extending multi-sector FOSSIL models to couple healthcare with education, labor, and climate domains could further establish a theory of adaptive efficiency under equity constraints.

Ultimately, this study establishes a theoretically grounded, empirically validated, and policy-relevant foundation for behaviorally adaptive health systems.
It demonstrates that fairness, efficiency, and adaptability are not competing goals but interdependent, learnable dimensions of a sustainable health ecosystem—redefining how performance, equity, and resilience can be optimized together in the 21st-century health economy.

## References

* \bibcommenthead
* Dolan et al. [2010]

  Dolan, P.,
  Peasgood, T.,
  White, M.:
  Measuring Quality of Life: QALYs and the Capabilities Approach.
  Oxford University Press,
  Oxford
  (2010).
  <https://doi.org/10.1093/acprof:oso/9780199560198.001.0001>
* Clemens and Gottlieb [2019]

  Clemens, J.,
  Gottlieb, J.D.:
  Incentives in health care: Reflections and implications.
  Journal of Economic Perspectives
  33(4),
  165–190
  (2019)
  <https://doi.org/10.1257/jep.33.4.165>
* Machina [1987]

  Machina, M.J.:
  Choice under uncertainty: Problems solved and unsolved.
  Journal of Economic Perspectives
  1(1),
  121–154
  (1987)
  <https://doi.org/10.1257/jep.1.1.121>
* Tversky and Kahneman [1992]

  Tversky, A.,
  Kahneman, D.:
  Advances in prospect theory: Cumulative representation of uncertainty.
  Journal of Risk and Uncertainty
  5,
  297–323
  (1992)
  <https://doi.org/10.1007/BF00122574>
* Weiss et al. [2018]

  Weiss, G.,
  Elmachtoub, A.N.,
  Henderson, S.G.:
  Inverse optimization for demand and supply function estimation.
  Operations Research
  66(5),
  1269–1284
  (2018)
  <https://doi.org/10.1287/opre.2018.1731>
* Zhang and Liu [2024]

  Zhang, R.,
  Liu, F.:
  Behavioral economics meets health policy: Modeling adaptive incentive responses.
  Health Economics Review
  14(2),
  45–62
  (2024)
  <https://doi.org/10.1186/s13561-024-00458-2>
* Esfahani and Kuhn [2018]

  Esfahani, P.M.,
  Kuhn, D.:
  Data-driven distributionally robust optimization using the wasserstein metric: Performance guarantees and tractable reformulations.
  Mathematical Programming
  171,
  115–166
  (2018)
  <https://doi.org/10.1007/s10107-017-1172-1>
* Bertsimas and Parys [2022]

  Bertsimas, D.,
  Parys, B.V.:
  Inverse optimization: Theory and applications.
  Operations Research
  70(1),
  311–334
  (2022)
  <https://doi.org/10.1287/opre.2021.2158>
* Cha et al. [2025a]

  Cha, J.,
  Cha, E.D.,
  Yoo, E.,
  Song, H.:
  Modeling roi in chronic disease management: A simulation-based framework integrating patient adherence and policy timing.
  BMC Public Health
  (2025)
  [arXiv:2510.06379](https://arxiv.org/abs/2510.06379)
  [q-fin.GN].
  Accepted for publication. Forthcoming article. Preprint available at <https://arxiv.org/abs/2510.06379>
* Cha et al. [2025b]

  Cha, J.,
  Lee, J.,
  Cho, J.,
  Shin, J.:
  Fossil: Regret-minimizing weighting for robust learning under imbalance and small data.
  arXiv preprint arXiv:2509.13218
  (2025)
  [arXiv:2509.13218](https://arxiv.org/abs/2509.13218)
  [cs.LG].
  Under review at ICLR 2025. Preprint available at <https://arxiv.org/abs/2509.13218>
* Zhang [2024]

  Zhang, H.:
  Behavioral dynamics in industrial economics.
  Journal of Industrial Economics
  72(3),
  1021–1051
  (2024)
  <https://doi.org/10.1111/joie.12345>
* Gino et al. [2016]

  Gino, F.,
  Shu, L.L.,
  Bazerman, M.H.:
  Motivated forgetting by managers: The case of unethical behavior in organizations.
  Organizational Behavior and Human Decision Processes
  137,
  136–150
  (2016)
  <https://doi.org/10.1016/j.obhdp.2016.09.001>
* Bauch and Galvani [2013]

  Bauch, C.T.,
  Galvani, A.P.:
  Social factors in epidemiology.
  Science
  342(6154),
  47–49
  (2013)
  <https://doi.org/10.1126/science.1244492>
* Rahmandad and Repenning [2015]

  Rahmandad, H.,
  Repenning, R.:
  Capability erosion dynamics.
  Strategic Management Journal
  36(11),
  1598–1614
  (2015)
  <https://doi.org/10.1002/smj.2307>
* Bendoly et al. [2014]

  Bendoly, E.,
  Donohue, W.C.,
  Taylor, K.L.:
  Behavioral operations: Past, present, and future.
  Production and Operations Management
  23(6),
  1757–1771
  (2014)
  <https://doi.org/10.1111/poms.12194>
* Gino and Norton [2015]

  Gino, F.,
  Norton, M.E.:
  Why self-reflection matters: How people evaluate their past decisions.
  Organizational Behavior and Human Decision Processes
  136,
  1–14
  (2015)
  <https://doi.org/10.1016/j.obhdp.2016.06.001>
* Fischbacher et al. [2012]

  Fischbacher, U.,
  Gächter, S.,
  Fehr, E.:
  Health economics, experiments, and cooperation.
  Health Economics
  21(9),
  1085–1100
  (2012)
  <https://doi.org/10.1002/hec.2874>
* Devlin and Parkin [2017]

  Devlin, N.,
  Parkin, D.:
  Using the EQ-5D to Measure Health Outcomes: Theoretical and Empirical Aspects.
  Springer, ???
  (2017).
  <https://doi.org/10.1007/978-3-319-56185-5>
* Dehez and Bacache [2020]

  Dehez, P.,
  Bacache, M.:
  Equity, fairness, and efficiency in health care resource allocation.
  Health Economics
  29(S1),
  54–64
  (2020)
  <https://doi.org/10.1002/hec.4040>
* Vissers and Boucherie [2022]

  Vissers, J.M.H.,
  Boucherie, R.J.:
  Value-based health care from an operations management perspective.
  Health Care Management Science
  25,
  96–108
  (2022)
  <https://doi.org/10.1007/s10729-021-09573-2>
* Rothenberg and Vardi [2019]

  Rothenberg, E.,
  Vardi, M.Y.:
  Learning health systems: Aligning incentives for quality and efficiency.
  Health Systems
  8(2),
  93–110
  (2019)
  <https://doi.org/10.1080/20476965.2018.1529694>
* Keller and Karlsson [2021]

  Keller, R.,
  Karlsson, T.:
  Policy incentives and behavioral responses in healthcare delivery.
  Health Policy
  125(7),
  906–915
  (2021)
  <https://doi.org/10.1016/j.healthpol.2021.04.008>
* Ahmadi-Javid and Jalali [2019]

  Ahmadi-Javid, A.,
  Jalali, M.:
  A decision-analytic framework for behavioral healthcare resource allocation.
  Health Care Management Science
  22(3),
  381–398
  (2019)
  <https://doi.org/10.1007/s10729-018-9445-9>
* Benjaafar and Zheng [2019]

  Benjaafar, S.,
  Zheng, Y.:
  Operations management in the age of behavioral economics.
  Production and Operations Management
  28(9),
  2198–2213
  (2019)
  <https://doi.org/10.1111/poms.13098>
* Gallino and Moreno [2018]

  Gallino, S.,
  Moreno, A.:
  Operational implications of behavioral responses to performance incentives.
  Manufacturing & Service Operations Management
  20(1),
  4–22
  (2018)
  <https://doi.org/10.1287/msom.2017.0651>
* Kroes and Lovejoy [2022]

  Kroes, J.R.,
  Lovejoy, W.S.:
  Learning in behavioral operations: Evidence and theory.
  Production and Operations Management
  31(3),
  969–987
  (2022)
  <https://doi.org/10.1111/poms.13671>
* Xu and Shi [2019]

  Xu, H.,
  Shi, C.:
  Dynamic equilibrium in behavioral operations models.
  European Journal of Operational Research
  277(3),
  1041–1053
  (2019)
  <https://doi.org/10.1016/j.ejor.2019.02.057>
* Hong and Jiang [2020]

  Hong, Y.,
  Jiang, Z.-C.:
  Information design in behavioral queueing systems.
  Operations Research
  68(6),
  1829–1848
  (2020)
  <https://doi.org/10.1287/opre.2019.1966>
* Govindan et al. [2021]

  Govindan, K.,
  Fattahi, M.,
  Jafarian, M.:
  A review on multiobjective optimization methods for sustainable supply chains.
  Annals of Operations Research
  300,
  1–60
  (2021)
  <https://doi.org/10.1007/s10479-020-03634-9>
* Li and Dai [2014]

  Li, X.,
  Dai, Y.:
  Behavioral queueing models with bounded rationality.
  European Journal of Operational Research
  239(3),
  882–893
  (2014)
  <https://doi.org/10.1016/j.ejor.2014.06.012>
* Peysakhovich and Lerer [2017]

  Peysakhovich, A.,
  Lerer, A.:
  Principled agents vs. agents of principle in social dilemmas.
  Nature Communications
  8,
  14533
  (2017)
  <https://doi.org/10.1038/ncomms14533>
* Liang and He [2020]

  Liang, C.,
  He, F.:
  Queueing networks with behavioral learning: A system dynamics perspective.
  Systems Research and Behavioral Science
  37(5),
  807–822
  (2020)
  <https://doi.org/10.1002/sres.2671>
* Freeman et al. [2023]

  Freeman, J.,
  Ghosh, S.,
  Collins, L.M.:
  Incentive design for integrated health systems: Behavioral and industrial insights.
  Health Care Management Science
  26(3),
  468–482
  (2023)
  <https://doi.org/10.1007/s10729-022-09601-3>
* Johari et al. [2023]

  Johari, R.,
  Weintraub, G.,
  Bastani, H.:
  Coordination in learning health systems: A game-theoretic framework.
  Operations Research
  (2023)
  <https://doi.org/10.1287/opre.2023.2439>
* Norton and Gino [2021]

  Norton, M.,
  Gino, F.:
  Integrating behavioral science and operations for better policy design.
  Management Science
  67(12),
  7547–7563
  (2021)
  <https://doi.org/10.1287/mnsc.2020.3808>
* Saadatmand et al. [2019]

  Saadatmand, A.,
  Safaei, H.R.,
  Niaki, S.T.A.:
  Multiobjective optimization in healthcare facility networks: A behavioral approach.
  Annals of Operations Research
  283,
  897–918
  (2019)
  <https://doi.org/10.1007/s10479-017-2779-6>
* Gans et al. [2019]

  Gans, N.,
  Katok, E.,
  Netessine, S.:
  Behavioral operations: Past, present, and future directions.
  Manufacturing & Service Operations Management
  21(1),
  1–23
  (2019)
  <https://doi.org/10.1287/msom.2018.0730>
* Khajeh and Ahmadi-Javid [2020]

  Khajeh, M.,
  Ahmadi-Javid, A.:
  Optimization and policy design in behavioral healthcare systems.
  Health Care Management Science
  23(2),
  278–291
  (2020)
  <https://doi.org/10.1007/s10729-018-9464-6>
* Xie and Han [2022]

  Xie, W.,
  Han, Z.:
  Integrated industrial and health system modeling under adaptive incentives.
  Annals of Operations Research
  319(2),
  803–825
  (2022)
  <https://doi.org/10.1007/s10479-021-04009-7>
* Brazier et al. [2017]

  Brazier, J.,
  Ratcliffe, J.,
  Saloman, J.,
  Tsuchiya, A.:
  Measuring and Valuing Health Benefits for Economic Evaluation.
  Oxford University Press, ???
  (2017).
  <https://doi.org/10.1093/med/9780198725925.001.0001>
* Murray et al. [2020]

  Murray, C.J.L., et al.:
  A deep learning technique for imputing missing healthcare data.
  Journal of Biomedical Informatics
  112,
  103586
  (2020)
  <https://doi.org/10.1016/j.jbi.2020.103586>
* Scroccaro and et al. [2025]

  Scroccaro, S.,
  al.:
  Learning systems in health informatics: A comprehensive survey.
  Health Informatics Journal
  (2025)
  <https://doi.org/10.1177/14604582231123456>
* Bertsimas and Dunn [2017]

  Bertsimas, D.,
  Dunn, J.:
  Optimal classification trees.
  Machine Learning
  106,
  1039–1082
  (2017)
  <https://doi.org/10.1007/s10994-017-5643-8>
* Keshavarz and et al. [2011]

  Keshavarz, A.,
  al.:
  Imputing missing data in healthcare.
  IEEE Access
  (2011)
  <https://doi.org/10.1109/EMBC.2019.8856760>
* Arrow [1963]

  Arrow, K.J.:
  Uncertainty and the welfare economics of medical care.
  American Economic Review
  53(5),
  941–973
  (1963)
  <https://doi.org/10.2307/1809778>
* Weinstein et al. [2017]

  Weinstein, M.C., et al.:
  Statistical issues in health economic efficiency models.
  Health Economics
  26,
  1238–1243
  (2017)
  <https://doi.org/10.1002/hec.3476>
* Atkinson [2019]

  Atkinson, A.:
  Measuring inequality in healthcare systems.
  Journal of Health Economics
  67,
  102216
  (2019)
  <https://doi.org/10.1016/j.jhealeco.2019.102216>
* Cutler [2020]

  Cutler, D.:
  Efficiency and equity in u.s. health care.
  JAMA
  324(7),
  613–614
  (2020)
  <https://doi.org/10.1001/jama.2020.12638>
* Hall [2023]

  Hall, M.:
  Trust and health policy: Measuring the long-run effects of fairness.
  Health Policy
  127(4),
  456–462
  (2023)
  [https://doi.org/%\*\*\*\*␣HCMS\_Cha.bbl␣Line␣725␣\*\*\*\*10.1016/j.healthpol.2023.01.012](https://doi.org/%****%20HCMS_Cha.bbl%20Line%20725%20****10.1016/j.healthpol.2023.01.012)
* Raman and Grover [2024]

  Raman, S.,
  Grover, P.:
  Behavioral tradeoffs in energy and education policy.
  Nature Energy
  9,
  320–329
  (2024)
  <https://doi.org/10.1038/s41560-024-01147-7>
* Sun et al. [2023]

  Sun, H., et al.:
  Cross-sectoral fairness–efficiency analysis: Methods and applications.
  Annals of Operations Research
  326,
  713–741
  (2023)
  <https://doi.org/10.1007/s10479-022-04896-x>
* McWilliams et al. [2022]

  McWilliams, J.M., et al.:
  Measuring adaptive capacity in health care systems.
  Health Services Research
  57,
  1105–1114
  (2022)
  <https://doi.org/10.1111/1475-6773.14067>
* Zhang and Zhao [2023]

  Zhang, L.,
  Zhao, T.:
  Reinforcement learning and robust control in health policy optimization.
  IEEE Transactions on Systems, Man, and Cybernetics
  53(7),
  7312–7325
  (2023)
  <https://doi.org/10.1109/TSMC.2023.3235103>
* Fernandez et al. [2022]

  Fernandez, D., et al.:
  Continuous policy optimization in healthcare systems under uncertainty.
  Journal of Health Informatics
  14(2),
  92–105
  (2022)
  <https://doi.org/10.1093/jhi/ocac024>

## Appendix A Proofs of Theoretical Results

This appendix provides the complete proofs of the analytical results stated in
Section [3.3](https://arxiv.org/html/2510.22518v1#S3.SS3 "3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs"), including the
Proposition on identification and stability,
and the supporting Lemma, Theorem, and Corollary.
All results are derived under Assumptions (A1)–(A3),
which guarantee convexity, independence, and strict regularization.

### A.1 Proof of Proposition [3.1](https://arxiv.org/html/2510.22518v1#S3.Thmtheorem1 "Proposition 3.1 (Identification and Stability). ‣ Assumptions. ‣ 3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")

We restate the inverse behavioral optimization problem as

|  |  |  |
| --- | --- | --- |
|  | minλ,γ,T∈[0,1]⁡ℒinv​(λ,γ,T)=∑t=1Tℓt​(λ,γ,T)+Ω​(λ,γ),\min\_{\lambda,\gamma,T\in[0,1]}\mathcal{L}\_{\text{inv}}(\lambda,\gamma,T)=\sum\_{t=1}^{T}\ell\_{t}(\lambda,\gamma,T)+\Omega(\lambda,\gamma), |  |

where ℓt​(λ,γ,T)=[QALYt−f​(at;λ,γ,T)]2\ell\_{t}(\lambda,\gamma,T)=[\mathrm{QALY}\_{t}-f(a\_{t};\lambda,\gamma,T)]^{2}
and Ω​(λ,γ)=β1​(λ−λ0)2+β2​(γ−γ0)2\Omega(\lambda,\gamma)=\beta\_{1}(\lambda-\lambda\_{0})^{2}+\beta\_{2}(\gamma-\gamma\_{0})^{2}.
Convexity in (λ,γ)(\lambda,\gamma) and differentiability in TT imply that
ℒinv\mathcal{L}\_{\text{inv}} is continuously differentiable on a compact domain.

#### Step 1: Existence.

Since ℒinv\mathcal{L}\_{\text{inv}} is continuous and coercive (due to the quadratic regularizer),
and the domain [0,1]3[0,1]^{3} is compact, a minimizer (λ∗,γ∗,T∗)(\lambda^{\*},\gamma^{\*},T^{\*}) exists.

#### Step 2: Uniqueness.

The prior penalty Ω​(λ,γ)\Omega(\lambda,\gamma) is strictly convex in (λ,γ)(\lambda,\gamma),
and ℓt​(λ,γ,T)\ell\_{t}(\lambda,\gamma,T) is convex by Assumption (A1).
Hence, for any TT, the combined loss
∑tℓt​(λ,γ,T)+Ω​(λ,γ)\sum\_{t}\ell\_{t}(\lambda,\gamma,T)+\Omega(\lambda,\gamma)
is strictly convex in (λ,γ)(\lambda,\gamma) and admits a unique minimizer.
Differentiability of ff in TT ensures that the joint minimizer over (λ,γ,T)(\lambda,\gamma,T)
is unique up to a constant transformation in ηt\eta\_{t}.

#### Step 3: Stability.

Let 𝒟={(at,QALYt)}\mathcal{D}=\{(a\_{t},\mathrm{QALY}\_{t})\} and
𝒟′={(at′,QALYt′)}\mathcal{D}^{\prime}=\{(a\_{t}^{\prime},\mathrm{QALY}\_{t}^{\prime})\} denote two datasets differing by small perturbations.
By standard sensitivity analysis for convex programs (Rockafellar and Wets, 1998),
the difference between the corresponding minimizers satisfies

|  |  |  |
| --- | --- | --- |
|  | ‖θ∗​(𝒟)−θ∗​(𝒟′)‖≤L𝒟μ​‖𝒟−𝒟′‖,\|\theta^{\*}(\mathcal{D})-\theta^{\*}(\mathcal{D}^{\prime})\|\leq\frac{L\_{\mathcal{D}}}{\mu}\,\|\mathcal{D}-\mathcal{D}^{\prime}\|, |  |

where μ\mu is the strong convexity modulus of ℒinv\mathcal{L}\_{\text{inv}} in (λ,γ)(\lambda,\gamma),
and L𝒟L\_{\mathcal{D}} bounds the Lipschitz constant of the gradient
∇θℓt​(θ)\nabla\_{\theta}\ell\_{t}(\theta) with respect to the data.
Hence, the mapping 𝒟↦θ∗​(𝒟)\mathcal{D}\mapsto\theta^{\*}(\mathcal{D}) is Lipschitz continuous.
This establishes the existence, uniqueness, and local stability of
(λ∗,γ∗,T∗)(\lambda^{\*},\gamma^{\*},T^{\*}).

□\square

### A.2 Proof of Lemma [3.2](https://arxiv.org/html/2510.22518v1#S3.Thmtheorem2 "Lemma 3.2 (Strong Convexity of the Inverse Loss). ‣ Assumptions. ‣ 3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")

#### Restatement.

If f​(at;λ,γ,T)f(a\_{t};\lambda,\gamma,T) is convex in (λ,γ)(\lambda,\gamma) and continuously differentiable in TT,
and if Ω​(λ,γ)\Omega(\lambda,\gamma) is μ\mu-strongly convex,
then ℒinv​(λ,γ,T)=∑tℓt​(λ,γ,T)+Ω​(λ,γ)\mathcal{L}\_{\mathrm{inv}}(\lambda,\gamma,T)=\sum\_{t}\ell\_{t}(\lambda,\gamma,T)+\Omega(\lambda,\gamma)
is μ\mu-strongly convex in (λ,γ)(\lambda,\gamma) and continuously differentiable in TT.

#### Proof.

Each ℓt​(λ,γ,T)=[QALYt−f​(at;λ,γ,T)]2\ell\_{t}(\lambda,\gamma,T)=[\mathrm{QALY}\_{t}-f(a\_{t};\lambda,\gamma,T)]^{2}
is convex in (λ,γ)(\lambda,\gamma) by composition of convex and affine-smooth mappings,
since (x↦(y−x)2)(x\mapsto(y-x)^{2}) is convex and non-decreasing for x≤yx\leq y.
Let g​(λ,γ,T)=∑tℓt​(λ,γ,T)g(\lambda,\gamma,T)=\sum\_{t}\ell\_{t}(\lambda,\gamma,T).
Then ∇(λ,γ)2g​(λ,γ,T)⪰0\nabla^{2}\_{(\lambda,\gamma)}g(\lambda,\gamma,T)\succeq 0 and
∇(λ,γ)2Ω​(λ,γ)⪰μ​I2\nabla^{2}\_{(\lambda,\gamma)}\Omega(\lambda,\gamma)\succeq\mu I\_{2}.
Hence

|  |  |  |
| --- | --- | --- |
|  | ∇(λ,γ)2ℒinv=∇(λ,γ)2g+∇(λ,γ)2Ω⪰μ​I2.\nabla^{2}\_{(\lambda,\gamma)}\mathcal{L}\_{\text{inv}}=\nabla^{2}\_{(\lambda,\gamma)}g+\nabla^{2}\_{(\lambda,\gamma)}\Omega\succeq\mu I\_{2}. |  |

Therefore, ℒinv\mathcal{L}\_{\text{inv}} is μ\mu-strongly convex in (λ,γ)(\lambda,\gamma).
Because ff is continuously differentiable in TT,
ℒinv\mathcal{L}\_{\text{inv}} inherits the same differentiability.
□\square

### A.3 Proof of Theorem [3.3](https://arxiv.org/html/2510.22518v1#S3.Thmtheorem3 "Theorem 3.3 (Identification and Local Stability). ‣ Assumptions. ‣ 3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")

Let θ=(λ,γ,T)\theta=(\lambda,\gamma,T) and define the stationarity operator
F​(θ;𝒟)=∇θℒinv​(θ;𝒟)F(\theta;\mathcal{D})=\nabla\_{\theta}\mathcal{L}\_{\text{inv}}(\theta;\mathcal{D}).
At the optimum θ∗\theta^{\*}, we have F​(θ∗;𝒟)=0F(\theta^{\*};\mathcal{D})=0.

#### Step 1: Local existence and uniqueness.

By Lemma [3.2](https://arxiv.org/html/2510.22518v1#S3.Thmtheorem2 "Lemma 3.2 (Strong Convexity of the Inverse Loss). ‣ Assumptions. ‣ 3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs"), ℒinv\mathcal{L}\_{\text{inv}} is μ\mu-strongly convex in (λ,γ)(\lambda,\gamma),
implying ∇θF​(θ∗;𝒟)\nabla\_{\theta}F(\theta^{\*};\mathcal{D}) is nonsingular.
By the Implicit Function Theorem,
there exists a continuously differentiable mapping θ∗​(𝒟)\theta^{\*}(\mathcal{D}) in a neighborhood of 𝒟\mathcal{D}
such that F​(θ∗​(𝒟);𝒟)=0F(\theta^{\*}(\mathcal{D});\mathcal{D})=0.
Hence, (λ∗,γ∗,T∗)(\lambda^{\*},\gamma^{\*},T^{\*}) is uniquely defined and locally smooth in 𝒟\mathcal{D}.

#### Step 2: Lipschitz continuity.

For any two datasets 𝒟\mathcal{D} and 𝒟′\mathcal{D}^{\prime},
consider Δ​θ∗=θ∗​(𝒟)−θ∗​(𝒟′)\Delta\theta^{\*}=\theta^{\*}(\mathcal{D})-\theta^{\*}(\mathcal{D}^{\prime}).
By mean value expansion of FF, we obtain

|  |  |  |
| --- | --- | --- |
|  | ∇θF​(θ¯;𝒟)​Δ​θ∗=F​(θ∗​(𝒟);𝒟)−F​(θ∗​(𝒟′);𝒟′)=Δ𝒟​F,\nabla\_{\theta}F(\bar{\theta};\mathcal{D})\,\Delta\theta^{\*}=F(\theta^{\*}(\mathcal{D});\mathcal{D})-F(\theta^{\*}(\mathcal{D}^{\prime});\mathcal{D}^{\prime})=\Delta\_{\mathcal{D}}F, |  |

where θ¯\bar{\theta} lies between θ∗​(𝒟)\theta^{\*}(\mathcal{D}) and θ∗​(𝒟′)\theta^{\*}(\mathcal{D}^{\prime}).
Using the nonsingularity of ∇θF\nabla\_{\theta}F and its bounded inverse,

|  |  |  |
| --- | --- | --- |
|  | ‖Δ​θ∗‖≤‖∇θF​(θ¯;𝒟)−1‖⋅‖Δ𝒟​F‖≤L𝒟μ​‖𝒟−𝒟′‖.\|\Delta\theta^{\*}\|\leq\|\nabla\_{\theta}F(\bar{\theta};\mathcal{D})^{-1}\|\cdot\|\Delta\_{\mathcal{D}}F\|\leq\frac{L\_{\mathcal{D}}}{\mu}\|\mathcal{D}-\mathcal{D}^{\prime}\|. |  |

Therefore, the mapping 𝒟↦θ∗​(𝒟)\mathcal{D}\mapsto\theta^{\*}(\mathcal{D}) is Lipschitz continuous,
which proves local stability of the inverse estimator.

□\square

### A.4 Proof of Corollary (Economic Stability of Behavioral Equilibria)

By Theorem [3.3](https://arxiv.org/html/2510.22518v1#S3.Thmtheorem3 "Theorem 3.3 (Identification and Local Stability). ‣ Assumptions. ‣ 3.3 Identification and Stability ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs"), the estimated parameters
θ∗=(λ∗,γ∗,T∗)\theta^{\*}=(\lambda^{\*},\gamma^{\*},T^{\*}) vary Lipschitz-continuously with the data 𝒟\mathcal{D}.
Since the forward equilibrium condition ([2](https://arxiv.org/html/2510.22518v1#S3.E2 "In 3.1 Forward Optimization Layer ‣ 3 Model Formulation: Inverse Behavioral Optimization under QALY–ROI Trade-offs ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs"))
and the system impact function ([5](https://arxiv.org/html/2510.22518v1#S4.E5 "In 4.1 Definition ‣ 4 SII: Measuring Behavioral Efficiency Gains ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs"))
are continuously differentiable in θ\theta,
the corresponding equilibrium outcomes
(at∗,Ut∗,S​I​It)(a\_{t}^{\*},U\_{t}^{\*},SII\_{t}) respond smoothly to small data or policy perturbations.
Therefore, small bounded shocks Δ​𝒟\Delta\mathcal{D} yield
bounded deviations in both micro-level decisions and macro-level industrial indices,
ensuring convergence toward a stable fairness–efficiency equilibrium.

□\square

### A.5 Technical Remarks and Extensions

#### 1. Gauss–Newton majorization.

If f​(at;λ,γ,T)f(a\_{t};\lambda,\gamma,T) is nonlinear but twice differentiable,
then the Hessian ∇(λ,γ)2ℓt\nabla^{2}\_{(\lambda,\gamma)}\ell\_{t}
can be upper-bounded by the Gauss–Newton approximation
Jt⊤​JtJ\_{t}^{\top}J\_{t}, where Jt=∇(λ,γ)f​(at;λ,γ,T)J\_{t}=\nabla\_{(\lambda,\gamma)}f(a\_{t};\lambda,\gamma,T).
This ensures positive semidefiniteness and preserves convexity in the local neighborhood.

#### 2. Stochastic extension.

Under stochastic perturbations of QALYt\mathrm{QALY}\_{t} with sub-Gaussian noise εt\varepsilon\_{t},
the expected loss 𝔼​[ℒinv]\mathbb{E}[\mathcal{L}\_{\text{inv}}]
retains the same convexity and stability properties in expectation,
yielding 𝔼​‖θ^T−θ∗‖2=𝒪​(1/T)\mathbb{E}\|\hat{\theta}\_{T}-\theta^{\*}\|\_{2}=\mathcal{O}(1/\sqrt{T})
by standard stochastic approximation arguments.

#### 3. Generalization to dynamic inverse learning.

If behavioral parameters evolve via θt+1=θt+ηt​∇θft​(θt)\theta\_{t+1}=\theta\_{t}+\eta\_{t}\nabla\_{\theta}f\_{t}(\theta\_{t}),
the regret bounds derived in Appendix [B](https://arxiv.org/html/2510.22518v1#A2 "Appendix B Supplementary Analysis and Reproducibility ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs") apply directly,
establishing dynamic stability under bounded drift VTV\_{T}.

## Appendix B Supplementary Analysis and Reproducibility

This appendix provides extended validation, robustness diagnostics,
and reproducibility information for the empirical and simulation experiments
presented in Section [5](https://arxiv.org/html/2510.22518v1#S5 "5 System-Level Simulation and Policy Sensitivity Analysis ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs").
It documents the OECD–WHO data characteristics,
the behavioral simulation setup, and the macroeconomic mapping procedure
underlying the Industrial Impact Index (SII).

### B.1 Empirical Data and Simulation Overview

![Refer to caption](FigS1.png)


Figure B.1: Empirical and simulated data characteristics.
(a) Log-scale scatter of per-capita health spending (USD PPP) versus life expectancy
from the merged OECD–WHO dataset (2007–2021).
(b) Baseline simulation trajectory of the S​I​ISII showing
steady convergence toward equilibrium (t=50t\!=\!50).

The merged OECD–WHO dataset integrates national-level health expenditure
(per capita, PPP-adjusted) with life expectancy data for 2007–2021.
A total of 34,023 observations were retained after cleaning
(HealthSpending >0>0 and non-missing LifeExpectancy).
The S​I​ISII was computed as

|  |  |  |
| --- | --- | --- |
|  | SII=LifeExpectancy×ln⁡(1+HealthSpending)100.\mathrm{SII}=\frac{\mathrm{LifeExpectancy}\times\ln(1+\mathrm{HealthSpending})}{100}. |  |

Panel (a) of Figure [B.1](https://arxiv.org/html/2510.22518v1#A2.F1 "Figure B.1 ‣ B.1 Empirical Data and Simulation Overview ‣ Appendix B Supplementary Analysis and Reproducibility ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs") reveals a strong positive association
between health expenditure and longevity, confirming that higher per-capita spending
correlates with system-level efficiency gains.
Panel (b) shows that simulated dynamics converge smoothly to an equilibrium level
near SII≈7.5\mathrm{SII}\!\approx\!7.5, consistent with the empirical range observed across OECD economies.

### B.2 Simulation Configuration and Policy Scenarios

Table [B.1](https://arxiv.org/html/2510.22518v1#A2.T1 "Table B.1 ‣ B.2 Simulation Configuration and Policy Scenarios ‣ Appendix B Supplementary Analysis and Reproducibility ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs") summarizes the behavioral and policy configurations
used to generate Figures [5.1](https://arxiv.org/html/2510.22518v1#S5.F1 "Figure 5.1 ‣ 5.3 Simulation Results and System Interpretation ‣ 5 System-Level Simulation and Policy Sensitivity Analysis ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs")–[6.2](https://arxiv.org/html/2510.22518v1#S6.F2 "Figure 6.2 ‣ 6.3 Behavioral Saturation and Robustness ‣ 6 Empirical Validation and Policy Implications ‣ Inverse Behavioral Optimization of QALY-Based Incentive Systems: Quantifying the System Impact of Adaptive Health Programs").
Each scenario isolates the effect of efficiency sensitivity (λ)(\lambda),
fairness preference (γ)(\gamma), and adaptive responsiveness (T)(T).

Table B.1: Simulation configuration for behavioral and policy experiments00footnotetext: All simulations are Monte Carlo–averaged over 20 replications with Gaussian noise
𝒩​(0,0.022)\mathcal{N}(0,0.02^{2}).
Parameters: λ\lambda = efficiency sensitivity,
γ\gamma = fairness preference,
TT = temporal responsiveness,
η\eta = learning rate, and T∗T^{\*} = steady-state responsiveness.

| Experiment ID | λ\lambda | γ\gamma | TT | kk | T0T\_{0} | σnoise\sigma\_{\text{noise}} | nrepn\_{\text{rep}} | η\eta | T∗T^{\*} | Scenario Label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| base | 0.6 | 0.4 | 0.6 | 5.0 | 0.5 | 0.02 | 20 | 0.1 | 0.7 | Baseline equilibrium |
| fairness\_high | 0.6 | 0.6 | 0.6 | 5.0 | 0.5 | 0.02 | 20 | 0.1 | 0.7 | Fairness-intensive policy |
| adaptive\_fast | 0.6 | 0.4 | 0.6 | 5.0 | 0.5 | 0.02 | 20 | 0.3 | 0.7 | High adaptation speed |
| efficiency\_boost | 0.8 | 0.3 | 0.6 | 5.0 | 0.5 | 0.02 | 20 | 0.1 | 0.7 | Efficiency-oriented system |

### B.3 Policy Sensitivity and Macroeconomic Conversion

![Refer to caption](FigS2.png)


Figure B.2: Policy sensitivity and macroeconomic conversion.
(a) Policy scenarios’ effect on the Δ​S​I​I\Delta SII,
showing that fairness-intensive policies substantially reduce system-level efficiency
while efficiency-oriented configurations yield small but positive gains.
(b) Macroeconomic conversion field (λ,γ→Δ​Y\lambda,\gamma\!\rightarrow\!\Delta Y)
expressed as percent of GDP, with contour lines denoting equal economic impact
and markers locating the corresponding policy regimes.

Panel (a) demonstrates that fairness-oriented policies (fairness\_high)
reduce the S​I​ISII by nearly one unit relative to baseline,
whereas efficiency-boosting policies increase it marginally.
Panel (b) converts the same behavioral sensitivity field
into GDP-equivalent terms using Δ​Y=αhealth​Δ​S​I​I\Delta Y=\alpha\_{\text{health}}\Delta SII,
with αhealth=0.11\alpha\_{\text{health}}=0.11 representing the healthcare sector’s GDP share.
Contour gradients illustrate that greater efficiency sensitivity (λ\lambda)
corresponds to positive GDP contributions, while higher fairness preference (γ\gamma)
reduces economic output, reflecting a quantifiable equity–efficiency trade-off.

### B.4 Robustness and Local Stability

Robustness was further examined by perturbing each behavioral parameter
by ±10%\pm 10\% around its estimated equilibrium value.
The resulting sensitivity estimates confirmed numerical stability and
local convergence across all behavioral dimensions.
Efficiency sensitivity (λ\lambda) remained tightly centered near 1.00,
while fairness preference (γ\gamma) fluctuated around zero,
and temporal responsiveness (TT) converged near 1.00 with minimal variation.
These results collectively indicate that the behavioral equilibrium is
robust and structurally well-conditioned, with no evidence of numerical drift
or local instability under Monte Carlo perturbations.

Table B.2: Summary statistics of behavioral parameters under robustness test

|  | Mean | Std. | Min | Max |
| --- | --- | --- | --- | --- |
| λ\lambda | 1.0003 | 0.0477 | 0.8888 | 1.1192 |
| γ\gamma | −0.0006-0.0006 | 0.0047 | −0.0139-0.0139 | 0.0115 |
| TT | 0.9975 | 0.0195 | 0.9468 | 1.0451 |
| \botrule |  |  |  |  |

Monte Carlo standard deviations remained below 0.05 for all par ameters,
and none exhibited divergence across iterations, confirming that
the estimated equilibrium (λ,γ,T)(\lambda,\gamma,T) is numerically
robust and locally stable.

### B.5 Reproducibility and Code Availability

All simulations were implemented in Python 3.10
using NumPy, Pandas, and Matplotlib.
All random seeds and hyperparameter schedules were fixed
to ensure full reproducibility and comparability.
Upon publication, the complete repository, including all configuration files,
simulation codes, and figure-generation scripts,
will be made publicly available to ensure transparency and replicability.

## Declarations

Funding:
No funds, grants, or other support was received for this study.

Competing Interests:
The authors have no relevant financial or non-financial interests to disclose.

Ethics Approval:
This study analyzed secondary, de-identified data and therefore did not require ethics approval according to institutional policies.

Data Availability:
The datasets and simulation codes used in this study are fully available in a public Zenodo repository. The repository contains all preprocessed data, configuration scripts, and robustness simulation files described in the manuscript. The complete package is accessible at <https://zenodo.org/records/17439497>,
entitled “Behavioral Industrial Health Simulation Data and Code (HCMS Study)”.
All data are synthetic or aggregated, and do not contain any sensitive or personally identifiable information.

Author Contributions:
Conceptualization and methodology: Jinho Cha, Junyeol Ryu;
Formal analysis and simulation: Junyeol Ryu, Justin Yu;
Data curation and visualization: Junyeol Ryu, Justin Yu, Eunchan Daniel Cha, Hyeyoung Hwang;
Writing – original draft: Jinho Cha;
Writing – review and editing: Eunchan Daniel Cha, Hyeyoung Hwang;
Supervision and project administration: Jinho Cha.
All authors read and approved the final version of the manuscript.