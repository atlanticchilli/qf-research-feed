---
authors:
- Dmitry Arkhangelsky
- Wisse Rutgers
doc_id: arxiv:2510.20032v1
family_id: arxiv:2510.20032
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh
  Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback,
  which has greatly improved the paper. We also thank seminar participants at Harvard
  and Stanford, as well as conference participants at the 2024 Winter Meetings of
  the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support
  from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M,
  funded by MCIN/AEI/10.13039/501100011033, and CEMFI.
url_abs: http://arxiv.org/abs/2510.20032v1
url_html: https://arxiv.org/html/2510.20032v1
venue: arXiv q-fin
version: 1
year: 2025
---


Dmitry Arkhangelsky
Associate Professor, CEMFI, darkhangel@cemfi.es. 
  
Wisse Rutgers
PhD student, CEMFI, wisse.rutgers@cemfi.edu.es.

(October 22, 2025)

We study a policy evaluation problem in centralized markets. We show that the aggregate impact of any marginal reform, the Marginal Policy Effect (MPE), is nonparametrically identified using data from a baseline equilibrium, without additional variation in the policy rule. We achieve this by constructing the equilibrium-adjusted outcome: a policy-invariant structural object that augments an agent’s outcome with the full equilibrium externality their participation imposes on others. We show that these externalities can be constructed using estimands that are already common in empirical work. The MPE is identified as the covariance between our structural outcome and the reform’s direction, providing a flexible tool for optimal policy targeting and a novel bridge to the Marginal Treatment Effects literature.

Keywords: Causal Inference, Market Equilibrium, Policy Evaluation, Spillovers

## 1 Introduction

Centralized marketplaces are a cornerstone of the modern economy, organizing a vast and growing share of economic activity. In the digital world, they match riders with drivers, allocate advertising slots in real-time auctions, and connect millions of sellers to buyers. In the public and non-profit sectors, they assign students to schools, allocate housing vouchers, and match organ donors to recipients. The defining feature of these markets is a well-defined algorithm or set of rules that processes inputs from participants, e.g., bids, preferences, scores, and produces an allocation of scarce resources.

A fundamental question for both the designers and regulators of these marketplaces is how to improve the outcomes they generate. This paper focuses on a particularly common class of interventions: those that influence participants’ behavior within a fixed set of market rules. This includes policies like providing subsidies to certain users, offering informational nudges, or creating incentives to alter how they participate in the market. Given an existing policy instrument, the central challenge for a platform or regulator is how to optimize it. This optimization is often an iterative process, focused on the aggregate welfare consequences of a marginal adjustment, for example, slightly expanding eligibility for a fee waiver or tweaking the size of a subsidy.

The natural approach to evaluate such a change is to run an experiment. However, standard experimentation in these environments faces a well-known challenge: equilibrium spillovers. Any intervention that meaningfully changes the behavior of one group of participants induces an endogenous response from the market-clearing mechanism that affects all other participants. For example, a subsidy that encourages more applications to a university with fixed capacity will raise the admission cutoff, creating a negative spillover for all other applicants. Because this spillover affects both treated and control groups alike, a simple comparison between them would difference away this common, system-wide component.

This issue, sometimes called the "missing intercept problem" in macroeconomics (Wolf, [2023](https://arxiv.org/html/2510.20032v1#bib.bib48)), has led to a conventional wisdom that nonparametric identification of aggregate effects requires observing the system’s response to explicit variation in the policy environment itself. Researchers typically seek this variation either over time, as is common in industry with switchback experiments (Bojinov et al., [2023](https://arxiv.org/html/2510.20032v1#bib.bib13)), or across distinct economic contexts where the policy rule or its intensity differs. For instance, a common design in development economics involves a two-stage randomization where the share of participants receiving a benefit is experimentally varied across different local labor markets (e.g., Crépon et al., [2013](https://arxiv.org/html/2510.20032v1#bib.bib16)). However, such designs can be costly to implement, their findings may be difficult to interpret due to substantial heterogeneity across environments, and finally, the statistical results might lack power due to a small number of experimental units.

Our central contribution is to show that aggregate effects of policy changes are, in fact, nonparametrically identified from data within a single policy environment. We achieve this without requiring cross-market variation or imposing strong extrapolating assumptions. The key to our approach is the construction of a single, policy-invariant structural object for each agent: the equilibrium-adjusted outcome (Ψitotal\Psi\_{i}^{\text{total}}). This object augments an agent’s observed outcome with a correction term that captures the full equilibrium externality their participation imposes on all others. The result is a single measure of an agent’s total contribution to welfare, accounting for both their private outcomes and the full cost of the competitive pressure they exert on the system. We show that this key theoretical object is identified from the data under natural assumptions about the market structure.

Our framework uses this structural object to evaluate the effects of local reforms—that is, marginal adjustments to an existing policy, such as slightly increasing the share of participants who receive a subsidy. Any such reform is characterized by a "score" function, sWs\_{W}, which describes the precise direction of the change. For instance, a reform that marginally increases the share of treated individuals would be represented by a score that is positive for the treated group and negative for the untreated group, capturing the small shift of participants between them. This construction leads to a powerful "separation principle" that is the main practical result of our paper. We show that the Marginal Policy Effect (MPE)—the first-order welfare impact of the reform—can be expressed as a simple covariance between this score and our structural outcome:

|  |  |  |
| --- | --- | --- |
|  | MPE=𝔼​[Ψitotal⋅sW​(Wi)].\text{MPE}=\mathbb{E}[\Psi\_{i}^{\text{total}}\cdot s\_{W}(W\_{i})]. |  |

This result provides a practical tool for policy evaluation. It separates the complex, fixed market structure, which is entirely encapsulated in Ψitotal\Psi\_{i}^{\text{total}}, from the specific policy change under consideration, which is represented by the score sWs\_{W}. A researcher or platform can invest in estimating the structural object Ψitotal\Psi\_{i}^{\text{total}} once and then use it to evaluate any local reform.

While we frame our discussion in terms of average outcomes for clarity, the framework is substantially more general. It applies to any welfare criterion that is a smooth functional of the outcome distribution, allowing policymakers to evaluate a reform’s impact on quantiles, measures of inequality like the Gini coefficient, or other distributional objectives. This generality is a direct consequence of our focus on local reforms. For a marginal policy change, the first-order impact on any smooth distributional functional can be represented as an expectation of a specific, policy-invariant transformation of the outcome, known as its influence function. Our analysis, therefore, proceeds by first developing the results for the simple case where welfare is the average outcome, and we later demonstrate that our framework accommodates these more general criteria by simply substituting the outcome variable with its relevant influence function.

The identification of different components of Ψitotal\Psi\_{i}^{\text{total}} is not straightforward. The key technical hurdle is that centralized allocation mechanisms are often discontinuous. A school admission rule, for example, is a step function of a student’s test score. A marginal policy reform that infinitesimally raises an admission cutoff has no effect on most students, but it causes a discrete jump in the allocation of students right at the margin, who now lose their seats. This creates a fundamental identification challenge, as the observed data contains no direct information about the outcomes of these marginal students under their new, counterfactual allocation.

Our framework resolves this by formally characterizing the indirect, equilibrium component of a policy’s effect and showing that it can be identified by focusing on the "marginal agents" at the allocation boundary. This approach builds a direct bridge between the theory of market design and a large body of empirical work. We show that the crucial inputs required to compute the market externalities are often the same local average treatment effects (LATEs) identified in regression discontinuity (RDD) studies of admission cutoffs or randomized lotteries (e.g., Abdulkadiroğlu et al., [2017](https://arxiv.org/html/2510.20032v1#bib.bib2); abdulkadi̇rouglu2022breaking; Kirkeboen et al., [2016](https://arxiv.org/html/2510.20032v1#bib.bib26); Walters, [2018](https://arxiv.org/html/2510.20032v1#bib.bib47)). Our framework clarifies that these well-studied parameters are not merely reduced-form objects but essential structural inputs required to conduct a full equilibrium evaluation of any marginal policy change (see Kline and Walters ([2016](https://arxiv.org/html/2510.20032v1#bib.bib29)) for a related discussion).

The flexibility of our framework allows us to extend the analysis beyond idealized experiments to more common observational settings. We first consider the case of selection on observables, where a policy is assigned randomly conditional on a set of covariates. The primary application of this extension is to provide a rigorous foundation for optimal policy targeting, connecting our results to the literature on empirical welfare maximization (EWM) (Manski, [2004](https://arxiv.org/html/2510.20032v1#bib.bib32); Kitagawa and Tetenov, [2018](https://arxiv.org/html/2510.20032v1#bib.bib27); Athey and Wager, [2021](https://arxiv.org/html/2510.20032v1#bib.bib8); Viviano and Rudder, [2024](https://arxiv.org/html/2510.20032v1#bib.bib44)). A practical implication of our framework is that it can avoid a common curse of dimensionality. As long as the market mechanism is anonymous with respect to the covariates—reacting only to agents’ reports, not their background characteristics—the structural components of Ψitotal\Psi\_{i}^{\text{total}} do not need to be re-estimated conditionally. A researcher can proceed directly with an aggregate analysis, using unconditionally estimated parameters like the RDD effects.

Finally, the framework can be adapted to answer a different and more structural class of questions central to economic analysis. In many contexts, a policymaker cannot directly mandate an action because it is an agent’s endogenous choice, such as the decision to apply for a voucher or take up a program. We show that our framework can still be used to evaluate the welfare consequences of a marginal shift in the distribution of these choices. This is achieved by introducing an instrumental variable that provides exogenous variation in agents’ decisions, building a novel bridge to the literature on Marginal Treatment Effects (MTE) (Björklund and Moffitt, [1987](https://arxiv.org/html/2510.20032v1#bib.bib12); Heckman and Vytlacil, [2001](https://arxiv.org/html/2510.20032v1#bib.bib22), [2005](https://arxiv.org/html/2510.20032v1#bib.bib23)). We show that the MTE of the equilibrium-adjusted outcome is precisely the correct structural object for evaluating policies that operate by influencing agents’ choices. This connects the estimands from an IV analysis to the MPE for specific, economically meaningful reforms, providing a powerful tool for structural evaluation in the presence of endogenous selection.

Our analysis is local, providing the welfare gradient for marginal policy reforms rather than evaluating large-scale, global changes. This focus is necessitated by a fundamental identification challenge: a marginal change to a market-clearing cutoff can assign agents to allocations they never would have received in the baseline equilibrium, meaning their counterfactual outcomes are unobserved. While methods for identifying global effects exist (Munro, [2025](https://arxiv.org/html/2510.20032v1#bib.bib37)), they often rely on strong assumptions to bridge this identification gap. We show that even identifying the local welfare effect in the presence of these discontinuities is a non-trivial problem that requires a dedicated framework.

To isolate this core challenge, our framework makes several simplifying assumptions. First, we focus exclusively on spillovers transmitted through the market-clearing mechanism itself. We abstract from other empirically important channels of interference, such as peer effects where agents’ preferences respond to the allocation of others (Allende, [2019](https://arxiv.org/html/2510.20032v1#bib.bib6); Leshno, [2022](https://arxiv.org/html/2510.20032v1#bib.bib30)), strategic reporting in non-strategy-proof environments (Agarwal and Somaini, [2018](https://arxiv.org/html/2510.20032v1#bib.bib5); Bertanha et al., [2024](https://arxiv.org/html/2510.20032v1#bib.bib11)), and exogenous policy spillovers like information diffusion.
Second, we focus on identification rather than estimation or inference. This involves assuming that the researcher observes all relevant data, including agents’ full reports, thereby abstracting from important practical challenges such as mistakes or incomplete preference rankings that are the subject of a separate literature (Artemov et al., [2023](https://arxiv.org/html/2510.20032v1#bib.bib7); Fack et al., [2019](https://arxiv.org/html/2510.20032v1#bib.bib18)).

We adopt these limitations not because these other channels are unimportant, but to establish what is possible in an ideal setting. Our finding that identification is limited to local effects even under these demanding assumptions suggests that incorporating additional complexities would require further, potentially less credible, restrictions. In particular, after establishing our key results, we discuss the issue of strategic reporting, arguing that existing solutions (Agarwal and Somaini, [2018](https://arxiv.org/html/2510.20032v1#bib.bib5); Bertanha et al., [2023](https://arxiv.org/html/2510.20032v1#bib.bib10)) can only partially address the challenges that arise in our context.

In summary, our framework provides a bridge between reduced-form data and the equilibrium structure of the market, yielding a tool with several distinct applications. First, our results can be applied directly to policy optimization. While our analysis is local, many practical policy decisions are iterative and marginal in nature, such as tweaking the size of a subsidy or adjusting eligibility criteria. Our framework provides the precise tool needed to guide these decisions by evaluating the "bang-for-the-buck" of a wide range of potential local reforms. Second, our work serves as a disciplined first step toward evaluating global policy changes. By sharply delineating what is identified from the data, it provides a transparent foundation upon which any analysis of large-scale reforms must be built; any claim about global effects must necessarily rely on extrapolating from the local effects that we identify. Finally, and relatedly, our results can be used to assess and discipline more ambitious structural models. A global model, likely estimated under more restrictive conditions, should be able to reproduce the local equilibrium effects that our framework identifies from the data, providing a powerful, data-driven specification test for more complex models of market behavior.

Our work is situated at the intersection of several active research areas: causal inference in markets, sufficient statistics approach in public economics, the empirical analysis of market design, the literature on optimal policy targeting, and the analysis of treatment effects with endogenous selection.

Our paper contributes to the recent literature on causal inference in the presence of interference and market equilibrium effects. The challenge that equilibrium adjustments can invalidate standard treatment effect comparisons has long been recognized (Heckman et al., [1998](https://arxiv.org/html/2510.20032v1#bib.bib21)). One prominent branch of the recent literature leverages auxiliary experimental variation—for instance, randomized prices—to identify spillovers (Wager and Xu, [2021](https://arxiv.org/html/2510.20032v1#bib.bib46); Munro et al., [2025](https://arxiv.org/html/2510.20032v1#bib.bib38)). Another branch, closer to our own, relies on institutional knowledge of the market-clearing rule (Munro, [2025](https://arxiv.org/html/2510.20032v1#bib.bib37)). Our framework follows this latter approach but makes a distinct contribution by focusing on general, stochastic downstream outcomes (e.g., future earnings) rather than on the allocation itself or its deterministic functions. This broader scope for the outcome variable is what necessitates our focus on local, rather than global, policy effects. Our work also provides a clear economic structure for the statistical decompositions of interference proposed in the causal inference literature (Hu et al., [2022](https://arxiv.org/html/2510.20032v1#bib.bib24)), showing precisely how the indirect effects arise from the market mechanism. Finally, it is related to the recent design-based causal analysis of equilibrium systems by Menzel ([2025](https://arxiv.org/html/2510.20032v1#bib.bib34)).

Our work is related to the influential sufficient statistics literature in public economics, which connects credibly identified, reduced-form parameters to welfare theory without requiring the estimation of a full structural model (e.g., Chetty, [2009](https://arxiv.org/html/2510.20032v1#bib.bib15); Kleven, [2021](https://arxiv.org/html/2510.20032v1#bib.bib28)). In particular, in constructing the equilibrium-adjusted outcome, we explicitly rely on quasi-experimental estimands (such as LATEs from RDDs), combining them with institutional knowledge of the market mechanism. Our approach is more structural in nature, relying on details of the allocation mechanism.

Our analysis is directly related to applied market design. A prominent empirical literature uses randomized lotteries or regression discontinuity designs to estimate the causal effect of attending a particular school (Abdulkadiroğlu et al., [2017](https://arxiv.org/html/2510.20032v1#bib.bib2); abdulkadi̇rouglu2022breaking; Walters, [2018](https://arxiv.org/html/2510.20032v1#bib.bib47)). We show that the LATEs identified in these studies are not merely reduced-form parameters. Instead, they are the essential structural inputs required to evaluate the equilibrium consequences of any marginal policy change. Our analysis builds on theoretical work that characterizes large matching markets with cutoffs (Azevedo and Leshno, [2016](https://arxiv.org/html/2510.20032v1#bib.bib9); Leshno and Lo, [2021](https://arxiv.org/html/2510.20032v1#bib.bib31)) and also speaks to the econometric challenges that arise in non-strategy-proof mechanisms, as studied in a growing literature on preference recovery and strategic reporting (Agarwal and Somaini, [2018](https://arxiv.org/html/2510.20032v1#bib.bib5); Bertanha et al., [2023](https://arxiv.org/html/2510.20032v1#bib.bib10)). Finally, our analysis is related to recent empirical work on outcomes and choices in empirical market design by (Agarwal et al., [2025](https://arxiv.org/html/2510.20032v1#bib.bib4))

By focusing on policy optimization, our work connects to the literature on optimal policy targeting (Manski, [2004](https://arxiv.org/html/2510.20032v1#bib.bib32); Kitagawa and Tetenov, [2018](https://arxiv.org/html/2510.20032v1#bib.bib27); Athey and Wager, [2021](https://arxiv.org/html/2510.20032v1#bib.bib8); Viviano and Rudder, [2024](https://arxiv.org/html/2510.20032v1#bib.bib44)). This literature typically seeks to find a globally optimal policy rule, which often depends only on the sign of a conditional average treatment effect (CATE). Our approach is local, focusing on the welfare gradient to guide iterative policy improvement. Our central contribution to this literature is to identify the correct welfare-relevant object for policy targeting in an equilibrium setting. We show that the policymaker’s objective should be to maximize the CATE of the equilibrium-adjusted outcome, Ψitotal\Psi\_{i}^{\text{total}}, not the observed outcome. This objective function correctly accounts for equilibrium spillovers and leverages the magnitude of the causal effect, not just its sign.

Finally, to address settings with endogenous policy take-up, we connect to the literature on MTE (Björklund and Moffitt, [1987](https://arxiv.org/html/2510.20032v1#bib.bib12); Heckman and Vytlacil, [2001](https://arxiv.org/html/2510.20032v1#bib.bib22), [2005](https://arxiv.org/html/2510.20032v1#bib.bib23)). In contexts where a policy instrument influences, but does not mandate, an agent’s choice, we show how to use instrumental variables to conduct a full welfare analysis. Our key contribution is to demonstrate that the proper object of study is the MTE of the equilibrium-adjusted outcome. This synthesizes the MTE framework, which accounts for selection on unobservables, with our framework, which accounts for equilibrium spillovers. By connecting our equilibrium analysis to recent advances in the MTE literature (Brinch et al., [2017](https://arxiv.org/html/2510.20032v1#bib.bib14); Mogstad et al., [2018](https://arxiv.org/html/2510.20032v1#bib.bib35); Mogstad and Torgovitsky, [2024](https://arxiv.org/html/2510.20032v1#bib.bib36)), this result provides a clear path from reduced-form IV estimates to a rich set of structural statements about the welfare impact of policies that target endogenous choices.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2510.20032v1#S2 "2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") lays out the theoretical framework, defining the economic environment and the propagation of a policy reform. Section [3](https://arxiv.org/html/2510.20032v1#S3 "3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") presents our main identification result, detailing the construction of the equilibrium-adjusted outcome and the derivation of the Marginal Policy Effect. Section [4](https://arxiv.org/html/2510.20032v1#S4 "4 Examples ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") illustrates the framework with several canonical examples, including auctions and school choice. Section [5](https://arxiv.org/html/2510.20032v1#S5 "5 Applications and Extensions ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") develops the extensions to general welfare functionals, optimal policy targeting, and endogenous selection. Section [6](https://arxiv.org/html/2510.20032v1#S6 "6 Conclusion ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") concludes.

## 2 Framework

This section develops the formal framework to address the challenge of equilibrium spillovers outlined in the introduction. Standard causal inference methods are ill-suited for this environment, as a policy change for one agent directly alters the competitive landscape for all others. Our analysis overcomes this "missing intercept problem" by leveraging institutional knowledge of the market. To do so, we first specify the economic environment, defining the two components of institutional context on which our analysis rests: the allocation mechanism and the market conduct rule. We then trace how these components allow a local policy reform to propagate through the system.

### 2.1 Environment

Our analysis begins with a population of agents, indexed by ii. Each agent has a potential outcome, Yi​(w,a)Y\_{i}(w,a), which is a function of two variables: the allocation they ultimately receive, aa, and their exposure to a policy instrument, ww. The allocation aa belongs to a discrete set 𝒜={0,1,…,K}\mathcal{A}=\{0,1,\dots,K\}, representing one of KK scarce goods—such as a seat at a charter school, a housing voucher, or a specific advertising slot—or an outside option (a=0a=0). The policy instrument (or "treatment") w∈𝒲w\in\mathcal{W} represents an existing intervention that a platform or regulator is considering adjusting. Examples include the size of a tuition subsidy, an informational treatment about market options, or a targeted incentive. We denote the realized policy for agent ii by the random variable WiW\_{i}.

In addition to the outcome, the policy WiW\_{i} influences agent ii’s report to the allocation mechanism, Ri=Ri​(Wi)∈ℛR\_{i}=R\_{i}(W\_{i})\in\mathcal{R}. This report can correspond to a vector of preferences, a bid, or school priorities. An agent’s final allocation, AiA\_{i}, is determined by their own report RiR\_{i} and the aggregate competitive environment. We summarize this environment with a vector of market-clearing parameters, 𝐜\mathbf{c} (e.g., equilibrium prices, rationing probabilities, or admission cutoffs), and the population-wide distribution of reports, PRP\_{R}.

###### Assumption 2.1 (Anonymous Allocation Mechanism).

The counterfactual allocation Ai​(r,𝐜,PR)A\_{i}(r,\mathbf{c},P\_{R}) is determined by an anonymous mechanism that depends on an agent’s report rr, the common parameter 𝐜\mathbf{c}, and the counterfactual marginal distribution of reports in the population PRP\_{R}. The probability of receiving allocation aa is given by a known function μa​(r,𝐜,PR)\mu\_{a}(r,\mathbf{c},P\_{R}).

This framework is designed to capture two distinct but related economic settings. The first is a large market where an agent’s allocation depends on their report relative to aggregate competitive conditions. In many such markets, these conditions are fully summarized by the equilibrium parameter 𝐜\mathbf{c}, rendering the direct dependence of μa\mu\_{a} on PRP\_{R} redundant once 𝐜\mathbf{c} is known. The second setting is a market with a finite number of symmetric participants, such as a symmetric auction. Here, μa​(r,𝐜,PR)\mu\_{a}(r,\mathbf{c},P\_{R}) represents an agent’s interim probability of receiving allocation aa, which naturally depends on both the common parameter (e.g., a reserve price) and the distribution of their opponents’ reports, PRP\_{R}. Our general formulation, μa​(r,𝐜,PR)\mu\_{a}(r,\mathbf{c},P\_{R}), is deliberately chosen to encompass both of these cases.

Crucially, we assume the functional form of this allocation rule is known to the researcher. This institutional knowledge is essential for analyzing counterfactual allocations under different market conditions. Together, these two assumptions formalize the institutional knowledge of the market’s structure. This knowledge is an essential component of our identification strategy, allowing us to proceed without requiring the cross-policy variation used in conventional approaches. Our next assumption extends this requirement from the mechanism’s rules to the market’s conduct.

###### Assumption 2.2 (Market Conduct Rule).

The counterfactual parameter vector 𝐜\mathbf{c} is determined by the counterfactual competitive environment PRP\_{R},

|  |  |  |
| --- | --- | --- |
|  | 𝐜=𝐜​(PR),\mathbf{c}=\mathbf{c}(P\_{R}), |  |

for some known function 𝐜​(⋅)\mathbf{c}(\cdot).

We deliberately separate the market-clearing parameter 𝐜\mathbf{c} from the full report distribution PRP\_{R} as arguments in the allocation function, μa​(r,𝐜,PR)\mu\_{a}(r,\mathbf{c},P\_{R}). This distinction is not merely notational but economically and mathematically meaningful. Economically, it reflects a natural hierarchy: PRP\_{R} represents the primitive competitive environment, while 𝐜\mathbf{c} is the endogenous summary statistic of that environment (e.g., a vector of prices or admission cutoffs) to which agents directly react. Mathematically, this separation allows us to impose different regularity conditions on each component. For instance, an agent’s allocation is often a discontinuous function of the clearing parameter 𝐜\mathbf{c}. In contrast, the market conduct rule 𝐜​(PR)\mathbf{c}(P\_{R}) can be a smooth functional of the underlying distribution PRP\_{R}. This structure is critical for analyzing the propagation of marginal policy reforms, as the examples below will illustrate.

##### Example 1: Competitive Equilibrium.

Consider a market where for each product k∈{1,…,K}k\in\{1,\dots,K\}, there is a fixed supply qkq\_{k}. The market-clearing parameter 𝐜∈ℝK\mathbf{c}\in\mathbb{R}^{K} can be interpreted as a vector of prices, admission standards, or rationing probabilities that adjust to equilibrate demand with supply. An equilibrium in a typical allocation mechanism, e.g., the Deferred Acceptance Algorithm, will depend only on 𝐜\mathbf{c}, not the whole distribution of reports PRP\_{R} (Azevedo and Leshno, [2016](https://arxiv.org/html/2510.20032v1#bib.bib9)). The equilibrium constraint requires that these parameters satisfy market-clearing:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝟏​{Ai=k}]=∫μk​(r,𝐜)​𝑑PR​(r)=qk,∀k∈{1,…,K}.\mathbb{E}[\mathbf{1}\{A\_{i}=k\}]=\int\mu\_{k}(r,\mathbf{c})dP\_{R}(r)=q\_{k},\quad\forall k\in\{1,\dots,K\}. |  |

This system of equations implicitly defines the parameter 𝐜\mathbf{c} as a functional of the entire distribution of reports, 𝐜​(PR)\mathbf{c}(P\_{R}).

##### Example 2: Optimal Reserve Price in an Auction.

Suppose a seller is auctioning a single item (𝒜={0,1}\mathcal{A}=\{0,1\}) and agents’ reports RiR\_{i} are their valuations. Parameter cc corresponds to a reserve price. In this situation, the allocation probability for an agent with valuation rr will depend discontinuously on the reserve price and smoothly on the distribution of the competitors’ valuations. Suppose the seller sets a reserve price cc to maximize expected revenue. Following Myerson ([1981](https://arxiv.org/html/2510.20032v1#bib.bib39)), the optimal reserve price solves the first-order condition of the seller’s problem, which balances the revenue gain from a higher price against the risk of the item going unsold. This trade-off is captured by the equation:

|  |  |  |
| --- | --- | --- |
|  | fR​(c)​c−(1−FR​(c))=0,f\_{R}(c)c-(1-F\_{R}(c))=0, |  |

where FRF\_{R} and fRf\_{R} are the distribution and density functions of valuations, respectively. The solution, cc, is the price where the marginal revenue of raising the price equals zero. Because this condition directly involves the distribution of valuations, the optimal reserve price is a function of the report distribution, c​(PR)c(P\_{R}). This example highlights the value of our two-part structure: Assumption [2.1](https://arxiv.org/html/2510.20032v1#S2.Thmassumption1 "Assumption 2.1 (Anonymous Allocation Mechanism). ‣ 2.1 Environment ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") defines the allocation rule for any given reserve price, while the market conduct rule in Assumption [2.2](https://arxiv.org/html/2510.20032v1#S2.Thmassumption2 "Assumption 2.2 (Market Conduct Rule). ‣ 2.1 Environment ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") models the seller’s optimizing behavior.

##### Example 3: School Choice with Trading Cycles.

Suppose KK products correspond to spots in public schools. An agent’s report consists of a vector of priorities, (Vi,1,…,Vi,K)(V\_{i,1},\dots,V\_{i,K}), and a strict preference relation, ≻i\succ\_{i}. The slots are allocated using Gale’s Top Trading Cycles algorithm (Shapley and Scarf, [1974](https://arxiv.org/html/2510.20032v1#bib.bib41); Abdulkadiroğlu and Sönmez, [2003](https://arxiv.org/html/2510.20032v1#bib.bib3)). As shown by Leshno and Lo ([2021](https://arxiv.org/html/2510.20032v1#bib.bib31)), the final allocation from this process can be characterized by a matrix of admission cutoffs 𝐜∈ℝK×K\mathbf{c}\in\mathbb{R}^{K\times K}. Here, ca,bc\_{a,b} represents the minimum priority score required at an endowment school bb to successfully obtain a seat at a destination school aa. A student is assigned their most-preferred school from the set of schools for which they are admissible:

|  |  |  |
| --- | --- | --- |
|  | Ai=max≻i⁡{{a|Vi,b≥ca,b​ for some b}∪{0}}.A\_{i}=\max\_{\succ\_{i}}\left\{\{a|V\_{i,b}\geq c\_{a,b}\text{ for some $b$}\}\cup\{0\}\right\}. |  |

These cutoffs are the endogenous outcome of the matching process, which can be described as a solution to a dynamic system that depends on the joint distribution of priorities and preferences, allowing us to write 𝐜=𝐜​(PR)\mathbf{c}=\mathbf{c}(P\_{R}).111We discuss application of our results to TTC in more detail in Appendix [C](https://arxiv.org/html/2510.20032v1#A3 "Appendix C Examples ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.").

The previous assumptions describe the counterfactual world. The observed data are generated from a baseline equilibrium that unfolds in a sequence of steps. First, the baseline policy distribution, PW|0P\_{W|0}, induces a distribution of agent reports, PR|0P\_{R|0}. This report distribution, via the market conduct rule in Assumption [2.2](https://arxiv.org/html/2510.20032v1#S2.Thmassumption2 "Assumption 2.2 (Market Conduct Rule). ‣ 2.1 Environment ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), determines the parameter 𝐜0:=𝐜​(PR|0)\mathbf{c}\_{0}:=\mathbf{c}(P\_{R|0}). Finally, the allocation mechanism from Assumption [2.1](https://arxiv.org/html/2510.20032v1#S2.Thmassumption1 "Assumption 2.1 (Anonymous Allocation Mechanism). ‣ 2.1 Environment ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") assigns an allocation Ai=Ai​(Ri,𝐜0,PR|0)A\_{i}=A\_{i}(R\_{i},\mathbf{c}\_{0},P\_{R|0}), which determines the realized outcome Yi:=Yi​(Wi,Ai)Y\_{i}:=Y\_{i}(W\_{i},A\_{i}). We define the benchmark aggregate welfare, 𝒰0\mathcal{U}\_{0}, as the expected value of this realized outcome:

|  |  |  |
| --- | --- | --- |
|  | 𝒰0:=𝔼0​[Yi],\displaystyle\mathcal{U}\_{0}:=\mathbb{E}\_{0}[Y\_{i}], |  |

where the expectation 𝔼0\mathbb{E}\_{0} is taken over the distribution of the observed data described above.

We will think of a marginal policy reform as a specific "direction" of change to the baseline policy distribution. Any such change can be characterized by a score function, sW​(w)s\_{W}(w), which tells us how the reform re-weights the baseline distribution of WiW\_{i}. Intuitively, if sW​(w)s\_{W}(w) is positive, the reform slightly increases the proportion of individuals receiving policy ww; if it is negative, it slightly decreases that proportion. A convenient way to generate a local reform is to embed the baseline policy distribution in a parametric family, PW|θ,sWP\_{W|\theta,s\_{W}}, indexed by a real-valued parameter θ\theta and score sWs\_{W}, so that PW|0,sW=PW|0P\_{W|0,s\_{W}}=P\_{W|0}. A marginal reform is then represented by an infinitesimal change in θ\theta away from its baseline value of zero.

To make this more concrete, consider two examples. First, suppose the policy is a binary treatment (Wi∈{0,1}W\_{i}\in\{0,1\}) and the reform’s goal is to marginally increase the share of treated agents. This corresponds to a score function that is proportional to Wi𝔼0​[Wi]−1−Wi1−𝔼0​[Wi]\frac{W\_{i}}{\mathbb{E}\_{0}[W\_{i}]}-\frac{1-W\_{i}}{1-\mathbb{E}\_{0}[W\_{i}]} and thus is positive for the treated (s​(1)>0s(1)>0) and negative for the untreated (s​(0)<0s(0)<0), effectively shifting a small amount of probability mass between the two groups. Alternatively, suppose the policy is a subsidy (in logs) distributed as Wi∼𝒩​(a0,σ02)W\_{i}\sim\mathcal{N}(a\_{0},\sigma^{2}\_{0}), and the reform aims to reduce the subsidy’s variance. This corresponds to a score function sW​(w)s\_{W}(w) that is high for subsidies near the mean and negative for subsidies in the tails, effectively pulling the distribution in towards its center.

Given (θ,sW)(\theta,s\_{W}) we can define the welfare as the average outcome,

|  |  |  |
| --- | --- | --- |
|  | 𝒰​(θ,sw):=𝔼(θ,sW)​[Yi],\displaystyle\mathcal{U}(\theta,s\_{w}):=\mathbb{E}\_{(\theta,s\_{W})}[Y\_{i}], |  |

where the expectation is over the distribution of the outcomes induced by (θ,sW)(\theta,s\_{W}), which we will describe in detail in the next section. By definition 𝒰​(0,sW)=𝒰0\mathcal{U}(0,s\_{W})=\mathcal{U}\_{0}. Following Hu et al. ([2022](https://arxiv.org/html/2510.20032v1#bib.bib24)), our primary objective is to characterize the marginal policy effect (MPE), which measures the first-order impact of the reform on the aggregate outcome:

|  |  |  |
| --- | --- | --- |
|  | Marginal Policy Effect:=∂𝒰​(θ,sW)∂θ|θ=0.\displaystyle\text{Marginal Policy Effect}:=\frac{\partial\mathcal{U}(\theta,s\_{W})}{\partial\theta}\bigg|\_{\theta=0}. |  |

The next several sections of the paper will focus on the identification of the MPE for a fixed local reform (score sWs\_{W}). We will discuss the question of optimal local reform in detail in Section [5](https://arxiv.org/html/2510.20032v1#S5 "5 Applications and Extensions ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.").

Our analysis focuses on identification of the MPE, not estimation or inference. We therefore proceed as if the joint distribution of the data vector Di=(Yi,Ai,Wi,Ri)D\_{i}=(Y\_{i},A\_{i},W\_{i},R\_{i}) under the baseline policy regime is known to the researcher. Note that it implies that the full report RiR\_{i} is observed. Part of this data is often missing in some empirical market design applications, such as auctions (e.g., observing the bids only for winners). The reports can contain mistakes or incomplete rankings in other applications, such as school choice (Artemov et al., [2023](https://arxiv.org/html/2510.20032v1#bib.bib7); Fack et al., [2019](https://arxiv.org/html/2510.20032v1#bib.bib18)). Our analysis abstracts from these data limitations.

###### Remark 2.1 (Beyond average outcomes).

Our discussion focuses on welfare, which is defined as an average outcome, but given that the reforms we analyze are local, our results apply almost immediately to any other smooth functionals of the outcome distribution. For instance, they can be extended to cover quantiles or aggregate measures of inequality, such as the Gini coefficient. We discuss this extension in Section [5](https://arxiv.org/html/2510.20032v1#S5 "5 Applications and Extensions ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.").

### 2.2 From Policy to Likelihood: Tracing the Perturbation

To trace how a local policy reform propagates through the market, we must connect the observed data to the counterfactual world. Our first step is to decompose the joint distribution of the observed data for agent ii, Di=(Yi,Ai,Ri,Wi)D\_{i}=(Y\_{i},A\_{i},R\_{i},W\_{i}), which we denote PDo​b​sP\_{D}^{obs}. We assume this distribution has a density, fDo​b​s​(y,a,r,w)f\_{D}^{obs}(y,a,r,w), with respect to an underlying well-behaved measure, which we factor as:

|  |  |  |
| --- | --- | --- |
|  | fDo​b​s​(y,a,r,w)=fY|A,R,Wo​b​s​(y|a,r,w)​fA|R,Wo​b​s​(a|r,w)​fR|Wo​b​s​(r|w)​fWo​b​s​(w).\displaystyle f\_{D}^{obs}(y,a,r,w)=f^{obs}\_{Y|A,R,W}(y|a,r,w)f^{obs}\_{A|R,W}(a|r,w)f^{obs}\_{R|W}(r|w)f^{obs}\_{W}(w). |  |

This factorization is purely statistical and holds by construction. Our goal in this section is to use this distribution to inform us about the counterfactual distribution of the data PDc​o​u​n​t​(θ,sW)P\_{D}^{count}(\theta,s\_{W}) induced by a particular local reform.

Our model already imposes structure on this decomposition. Specifically, Assumptions [2.1](https://arxiv.org/html/2510.20032v1#S2.Thmassumption1 "Assumption 2.1 (Anonymous Allocation Mechanism). ‣ 2.1 Environment ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")-[2.2](https://arxiv.org/html/2510.20032v1#S2.Thmassumption2 "Assumption 2.2 (Market Conduct Rule). ‣ 2.1 Environment ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") imply that the observed conditional allocation probability, fA|R,Wo​b​s​(a|r,w)f^{obs}\_{A|R,W}(a|r,w) is given by the known allocation rule μa​(⋅)\mu\_{a}(\cdot) evaluated at the baseline equilibrium:

|  |  |  |
| --- | --- | --- |
|  | fA|R,Wo​b​s​(a|r,w)=μa​(r,𝐜0,PR|0).\displaystyle f^{obs}\_{A|R,W}(a|r,w)=\mu\_{a}(r,\mathbf{c}\_{0},P\_{R|0}). |  |

The counterfactual distribution of WiW\_{i} is controlled by the policy maker, and for a given (θ,sW)(\theta,s\_{W}), we denote its density by fW​(w|θ,sW)f\_{W}(w|\theta,s\_{W}). This leaves two components that we must understand: fY|A,R,Wo​b​s​(y|a,r,w)f^{obs}\_{Y|A,R,W}(y|a,r,w) and fR|Wo​b​s​(r|w)f^{obs}\_{R|W}(r|w). To do so, we start with an assumption about the assignment of the baseline policy.

###### Assumption 2.3 (Random Assignment).

The policy WiW\_{i} is randomly assigned to agents in the baseline environment.

This assumption isolates the mechanism’s spillover effects from confounding selection effects, simplifying our initial analysis. We relax this restriction in Section [5](https://arxiv.org/html/2510.20032v1#S5 "5 Applications and Extensions ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") to allow for selection on both observed and unobserved characteristics. Our next assumption isolates the spillovers created by the allocation mechanism from other potential interference channels.

###### Assumption 2.4 (Policy Invariance).

The potential outcomes Yi​(w,a)Y\_{i}(w,a) and potential reports Ri​(w)R\_{i}(w) are structural primitives that are invariant to (θ,sW)(\theta,s\_{W}).

Assumption [2.4](https://arxiv.org/html/2510.20032v1#S2.Thmassumption4 "Assumption 2.4 (Policy Invariance). ‣ 2.2 From Policy to Likelihood: Tracing the Perturbation ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") requires that an agent’s underlying potential outcomes and potential reports, Yi​(w,a)Y\_{i}(w,a) and Ri​(w)R\_{i}(w), do not respond to changes in the aggregate policy environment (θ,sW)(\theta,s\_{W}). This allows us to focus squarely on externalities transmitted through the allocation mechanism. The assumption would be violated in two main scenarios. First, if the mechanism were not strategy-proof, an agent’s optimal report RiR\_{i} would depend on the distribution of competitors’ reports, which is a function of (θ,sW)(\theta,s\_{W}). Second, if direct peer effects were present (e.g., an agent’s utility is affected by the allocation of its competitors), both potential outcomes and potential reports would depend on the policy distribution (e.g., Allende, [2019](https://arxiv.org/html/2510.20032v1#bib.bib6); Leshno, [2022](https://arxiv.org/html/2510.20032v1#bib.bib30)). By ruling these out at the outset, our framework provides a clean benchmark for understanding spillovers induced by the mechanism only. We discuss the strategic reporting channel in Section [5](https://arxiv.org/html/2510.20032v1#S5 "5 Applications and Extensions ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.").

With these assumptions in place, we can now trace how the policy perturbation reshapes the joint distribution of the data.

###### Proposition 2.1 (Propagation of a Policy Perturbation).

Suppose Assumptions [2.1](https://arxiv.org/html/2510.20032v1#S2.Thmassumption1 "Assumption 2.1 (Anonymous Allocation Mechanism). ‣ 2.1 Environment ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")-[2.4](https://arxiv.org/html/2510.20032v1#S2.Thmassumption4 "Assumption 2.4 (Policy Invariance). ‣ 2.2 From Policy to Likelihood: Tracing the Perturbation ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") hold. Then PDo​b​sP\_{D}^{obs}-almost surely we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | fDcount​(Yi,Ai,Ri,Wi|θ,sW)=\displaystyle f\_{D}^{\text{count}}(Y\_{i},A\_{i},R\_{i},W\_{i}|\theta,s\_{W})=\; | fY|A,R,Wobs​(Yi|Ai,Ri,Wi)​μa​(Ri,𝐜​(PR|θ,sW),PR|θ,sW)\displaystyle f^{\text{obs}}\_{Y|A,R,W}(Y\_{i}|A\_{i},R\_{i},W\_{i})\mu\_{a}(R\_{i},\mathbf{c}(P\_{R|\theta,s\_{W}}),P\_{R|\theta,s\_{W}}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×fR|Wobs​(Ri|Wi)​fW​(Wi|θ,sW)\displaystyle\times f^{\text{obs}}\_{R|W}(R\_{i}|W\_{i})f\_{W}(W\_{i}|\theta,s\_{W}) |  |

where fDc​o​u​n​t​(y,a,r,w|θ,sW)f\_{D}^{count}(y,a,r,w|\theta,s\_{W}) is the density of PDc​o​u​n​t​(θ,sW)P\_{D}^{count}(\theta,s\_{W}), and PR|θ,sWP\_{R|\theta,s\_{W}} is the counterfactual distribution of reports induced by the new policy. Its density is formed by integrating the observed reporting rule, fR|Wo​b​s​(r|w)f^{obs}\_{R|W}(r|w), against the new policy distribution, f​(w|θ,sW)f(w|\theta,s\_{W}).

Proposition [2.1](https://arxiv.org/html/2510.20032v1#S2.Thmprop1 "Proposition 2.1 (Propagation of a Policy Perturbation). ‣ 2.2 From Policy to Likelihood: Tracing the Perturbation ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") provides a crucial link between the observed data and the counterfactual world. The expression reveals that a policy reform propagates through two distinct channels: (1) a direct effect on agents from the change in the policy distribution itself, from fWo​b​s​(w)f\_{W}^{obs}(w) to fW​(w|θ,sW)f\_{W}(w|\theta,s\_{W}); and (2) an indirect equilibrium effect that operates through the allocation rule μa​(⋅)\mu\_{a}(\cdot), which is shifted by changes in both the market-clearing parameters, 𝐜​(PR|θ,sW)\mathbf{c}(P\_{R|\theta,s\_{W}}), and the aggregate report distribution, PR|θ,sWP\_{R|\theta,s\_{W}}.

The key challenge is that Proposition [2.1](https://arxiv.org/html/2510.20032v1#S2.Thmprop1 "Proposition 2.1 (Propagation of a Policy Perturbation). ‣ 2.2 From Policy to Likelihood: Tracing the Perturbation ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") only restricts the distribution of PDc​o​u​n​t​(θ,sW)P^{count}\_{D}(\theta,s\_{W}) on the support of the distribution of the observed data, PDo​b​sP\_{D}^{obs}. To see why this creates a problem, note that in most economically relevant examples, a small change in 𝐜\mathbf{c} induces a discontinuous change in allocation for some agents. This implies that the observed data contains no direct information about the outcomes of these agents under their newly assigned allocations. The analysis in the next section introduces the key assumptions that allow us to bridge this identification gap.

## 3 The Marginal Policy Effect

This section derives our main identification result for the Marginal Policy Effect (MPE). The derivation must confront the central technical challenge of this environment: the inherent discontinuities in centralized allocation mechanisms. We begin by showing why these discontinuities violate the core smoothness assumptions of standard statistical methods, such as a score-based decomposition, rendering them insufficient for identifying the total MPE. To overcome this, our analysis proceeds in two steps. First, we dissect the indirect equilibrium effect into two identified economic forces: a competition effect, from shifting reports, and a market conduct effect, from the response of the clearing parameters. Second, we show how these components can be combined to construct our central result: a single, policy-invariant structural object for each agent—the equilibrium-adjusted outcome, Ψitotal\Psi\_{i}^{\text{total}}. This variable captures an agent’s full contribution to welfare, including the market externalities they generate, and ultimately reduces the MPE of any policy to a simple covariance with the policy’s score. Our discussion proceeds informally to build intuition; Appendix [B](https://arxiv.org/html/2510.20032v1#A2 "Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") collects the regularity conditions and formal proofs.

### 3.1 A Score-Based Decomposition

To analyze the MPE, we begin with a standard method for evaluating the impact of a marginal perturbation of a distribution: a score-based decomposition. If the joint density of the data, fDc​o​u​n​t​(y,a,r,w|θ,sW)f\_{D}^{count}(y,a,r,w|\theta,s\_{W}), varies smoothly, the effect on welfare can be expressed as the covariance between the outcome and the model’s score.222Formally, this requires the family of densities to be Differentiable in Quadratic Mean (DQM), a central concept in asymptotic statistics; see Van der Vaart ([2000](https://arxiv.org/html/2510.20032v1#bib.bib42)). The interchange of differentiation and integration is permissible because the mean is a differentiable functional, subject to mild moment conditions (Van Der Vaart, [1991](https://arxiv.org/html/2510.20032v1#bib.bib43)). The derivative of the aggregate welfare function is then given by:

|  |  |  |
| --- | --- | --- |
|  | 𝒰′​(sW)=∂∂θ​𝔼(θ,sW)​[Yi]|θ=0=𝔼0​[Yi​sD​(Yi,Ai,Ri,Wi|sW)],\displaystyle\mathcal{U}^{\prime}(s\_{W})=\frac{\partial}{\partial\theta}\mathbb{E}\_{(\theta,s\_{W})}[Y\_{i}]\bigg|\_{\theta=0}=\mathbb{E}\_{0}[Y\_{i}s\_{D}(Y\_{i},A\_{i},R\_{i},W\_{i}|s\_{W})], |  |

where the score, sD​(Yi,Ai,Ri,Wi|sW)=∂∂θ​log⁡fDc​o​u​n​t​(Yi,Ai,Ri,Wi|θ,sW)|θ=0s\_{D}(Y\_{i},A\_{i},R\_{i},W\_{i}|s\_{W})=\frac{\partial}{\partial\theta}\log f\_{D}^{count}(Y\_{i},A\_{i},R\_{i},W\_{i}|\theta,s\_{W})\big|\_{\theta=0}, measures the sensitivity of an observation’s log-likelihood to the policy change.

This approach is powerful because it yields a highly intuitive decomposition of the total welfare effect. Based on our factorization of the data-generating process from Proposition [2.1](https://arxiv.org/html/2510.20032v1#S2.Thmprop1 "Proposition 2.1 (Propagation of a Policy Perturbation). ‣ 2.2 From Policy to Likelihood: Tracing the Perturbation ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), the score is additive in its components, allowing us to write:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒰′​(sW)=𝔼0​[Yi​sW​(Wi)]⏟Direct Effect+𝔼0​[Yi​sA|R​(Ai|Ri,sW)]⏟Indirect Effect.\mathcal{U}^{\prime}(s\_{W})=\underbrace{\mathbb{E}\_{0}[Y\_{i}s\_{W}(W\_{i})]}\_{\text{Direct Effect}}+\underbrace{\mathbb{E}\_{0}[Y\_{i}s\_{A|R}(A\_{i}|R\_{i},s\_{W})]}\_{\text{Indirect Effect}}. |  | (1) |

This decomposition, a specific application of the concepts introduced by Hu et al. ([2022](https://arxiv.org/html/2510.20032v1#bib.bib24)), separates the MPE into two channels. The first term is a direct effect: the impact of perturbing the policy instrument WiW\_{i}, holding the market’s allocation rule fixed. The second is an indirect effect, which captures the equilibrium consequences of the policy as the allocation mechanism adjusts to the change.

The decomposition ([1](https://arxiv.org/html/2510.20032v1#S3.E1 "In 3.1 A Score-Based Decomposition ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")), however, rests on the critical assumption of smoothness, which, as already foreshadowed by the discussion following Proposition [2.1](https://arxiv.org/html/2510.20032v1#S2.Thmprop1 "Proposition 2.1 (Propagation of a Policy Perturbation). ‣ 2.2 From Policy to Likelihood: Tracing the Perturbation ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), fails in the settings we study. The reason is fundamental to the nature of centralized markets: their allocation rules are often discontinuous. For instance, a school admission rule is a step function of a student’s test score. A marginal policy reform that tightens admission standards by infinitesimally raising the cutoff score has no effect on most students, but it has a discrete and dramatic effect on students right at the original cutoff, who now lose their seats. This economic discontinuity breaks the mathematics behind the standard score-based machinery. Because the allocation probability, μa​(r,𝐜​(θ),PR|θ)\mu\_{a}(r,\mathbf{c}(\theta),P\_{R|\theta}), does not change smoothly with a reform that moves a hard threshold, the allocation score, sA|R​(Ai|Ri,sW)s\_{A|R}(A\_{i}|R\_{i},s\_{W}), is not a well-defined random variable that we can evaluate for each agent. The standard approach, which relies on this score, cannot be directly applied.333Formally, the family is not DQM because a first-order change in the cutoff induces a first-order change in the support of the distribution of the data.

Despite this challenge, the decomposition in ([1](https://arxiv.org/html/2510.20032v1#S3.E1 "In 3.1 A Score-Based Decomposition ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")) remains a valuable conceptual tool. In particular, the first term—the direct effect—is well-defined and identifiable. This is because the policymaker controls the perturbation to the policy distribution, f​(w|θ,sW)f(w|\theta,s\_{W}), and can ensure that the policy score sW​(Wi)s\_{W}(W\_{i}) is well-behaved. For example, if Wi∈{0,1}W\_{i}\in\{0,1\} is a binary treatment with baseline probability π0=𝔼0​[Wi]\pi\_{0}=\mathbb{E}\_{0}[W\_{i}], the score is proportional to Wiπ0−1−Wi1−π0\frac{W\_{i}}{\pi\_{0}}-\frac{1-W\_{i}}{1-\pi\_{0}}, and the direct effect becomes:

|  |  |  |
| --- | --- | --- |
|  | 𝔼0​[Yi​sW​(Wi)]∝𝔼0​[Yi|Wi=1]−𝔼0​[Yi|Wi=0].\displaystyle\mathbb{E}\_{0}[Y\_{i}s\_{W}(W\_{i})]\propto\mathbb{E}\_{0}[Y\_{i}|W\_{i}=1]-\mathbb{E}\_{0}[Y\_{i}|W\_{i}=0]. |  |

Under random assignment (Assumption [2.3](https://arxiv.org/html/2510.20032v1#S2.Thmassumption3 "Assumption 2.3 (Random Assignment). ‣ 2.2 From Policy to Likelihood: Tracing the Perturbation ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")), this corresponds to the average treatment effect for the potential outcome Yi​(w,Ai​(w))Y\_{i}(w,A\_{i}(w)). Here Ai​(w)A\_{i}(w) is a random variable with the distribution μa​(Ri​(w),𝐜0,PR|0)\mu\_{a}(R\_{i}(w),\mathbf{c}\_{0},P\_{R|0}).
This direct effect is therefore the average causal effect of the policy on the final outcome YiY\_{i} in the baseline market equilibrium.

The central technical challenge of our analysis, therefore, is to characterize and identify the indirect effect when the allocation score is ill-defined. The intuition for our approach, which we discuss in detail in the next section, is that while we cannot measure the effect of the market response on all agents, we can identify it by focusing precisely on those at the margin of their allocation—the very agents for whom an infinitesimal change in market conditions alters their allocation.

### 3.2 The Indirect Effect: Competition and Market Conduct

The indirect effect operates through the two distinct economic channels foreshadowed in the introduction. A policy reform alters the distribution of reports, changing the competitive environment. This leads to a competition effect. In response, the market’s conduct adjusts the clearing parameters 𝐜\mathbf{c}, leading to a market conduct effect. To formalize these, we define a counterfactual welfare function that depends on arbitrary clearing parameters (𝐜,P)(\mathbf{c},P):

|  |  |  |
| --- | --- | --- |
|  | 𝒰​(𝐜,P):=𝔼0​[∑a=0Kma​(Ri)​μa​(Ri,𝐜,P)],\displaystyle\mathcal{U}(\mathbf{c},P):=\mathbb{E}\_{0}\left[\sum\_{a=0}^{K}m\_{a}(R\_{i})\mu\_{a}(R\_{i},\mathbf{c},P)\right], |  |

where ma​(r):=𝔼0​[Yi​(Wi,a)|Ri=r]m\_{a}(r):=\mathbb{E}\_{0}[Y\_{i}(W\_{i},a)|R\_{i}=r]. Applying the chain rule to the aggregate welfare function 𝒰​(𝐜0,PR|0)\mathcal{U}(\mathbf{c}\_{0},P\_{R|0}) decomposes the indirect effect:

|  |  |  |
| --- | --- | --- |
|  | Indirect Effect=∇𝐜𝒰​(𝐜0,PR|0)⋅𝐜′​[sR]⏟Market Conduct Effect+DP​𝒰​(𝐜0,PR|0)​[sR]⏟Competition Effect.\displaystyle\text{Indirect Effect}=\underbrace{\nabla\_{\mathbf{c}}\mathcal{U}(\mathbf{c}\_{0},P\_{R|0})\cdot\mathbf{c}^{\prime}[s\_{R}]}\_{\text{Market Conduct Effect}}+\underbrace{D\_{P}\mathcal{U}(\mathbf{c}\_{0},P\_{R|0})[s\_{R}]}\_{\text{Competition Effect}}. |  |

This decomposition is driven by the report score sR​(Ri):=𝔼0​[sW​(Wi)|Ri]s\_{R}(R\_{i}):=\mathbb{E}\_{0}[s\_{W}(W\_{i})|R\_{i}]. The remainder of this section is dedicated to characterizing these two effects. To do so, our strategy is to first impose a structure on the allocation rule that isolates the source of the discontinuity.

###### Assumption 3.1 (Well-Behaved Mechanism).

The allocation probability, μa\mu\_{a}, can be decomposed into a smooth component, hah\_{a}, and a sharp eligibility boundary, ϕa\phi\_{a}, with the following properties:

1. (a)

   The allocation rule takes the form:

   |  |  |  |
   | --- | --- | --- |
   |  | μa​(Ri,𝐜,P)=ha​(Ri,𝐜,P)​𝟏​{ϕa​(Ri,𝐜)≥0}.\mu\_{a}(R\_{i},\mathbf{c},P)=h\_{a}(R\_{i},\mathbf{c},P)\mathbf{1}\{\phi\_{a}(R\_{i},\mathbf{c})\geq 0\}. |  |
2. (b)

   The conditional allocation probability, ha​(Ri,𝐜,P)h\_{a}(R\_{i},\mathbf{c},P), is a smooth function of the market-clearing parameters, 𝐜\mathbf{c}, and the aggregate report distribution, PP.
3. (c)

   The eligibility index, ϕa​(Ri,𝐜)\phi\_{a}(R\_{i},\mathbf{c}), is a smooth function of the clearing parameters, 𝐜\mathbf{c}. Crucially, it does not depend on the aggregate report distribution PP.

This structure is general enough to capture a wide range of common market designs, including all examples discussed in this paper. Intuitively, it represents the allocation as a combination of a lottery and a cutoff rule. An agent must first pass a hard eligibility threshold determined by the cutoff rule (ϕa≥0\phi\_{a}\geq 0). Conditional on being eligible, they are then assigned the good with some probability determined by the lottery (ha>0h\_{a}>0). This structure ensures that while the overall competitive environment (PP) affects allocation probabilities smoothly through the hah\_{a} term, sharp discontinuities are driven solely by the interaction of the clearing parameter 𝐜\mathbf{c} with agent reports at the eligibility boundary.

#### 3.2.1 The Competition Effect

The competition effect captures the welfare impact of the shift in the distribution of reports, holding the clearing parameters fixed. To quantify this, we consider how perturbing the density of one agent’s report, r′r^{\prime}, affects the allocation probability of another agent with report rr. This peer externality is captured by a functional derivative of hah\_{a} with respect to PP, which we denote La​(r,r′)L\_{a}(r,r^{\prime}). The total competition effect is the expected impact of this change on welfare:

|  |  |  |
| --- | --- | --- |
|  | DP​𝒰​(𝐜0,PR|0)​[sR]=𝔼0​[∑a=0Kma​(Ri)​𝔼0​[La​(Ri,Rj)​sR​(Rj)|Ri]],\displaystyle D\_{P}\mathcal{U}(\mathbf{c}\_{0},P\_{R|0})[s\_{R}]=\mathbb{E}\_{0}\left[\sum\_{a=0}^{K}m\_{a}(R\_{i})\mathbb{E}\_{0}[L\_{a}(R\_{i},R\_{j})s\_{R}(R\_{j})|R\_{i}]\right], |  |

where RjR\_{j} is an independent copy of RiR\_{i}. This expression presents a potential identification challenge, as it depends on the unobserved conditional mean of the potential outcome, ma​(Ri)m\_{a}(R\_{i}). However, our mechanism structure resolves this: if an agent is ineligible for good aa, a marginal change in others’ reports cannot make them eligible, meaning the spillover effect must also be zero (La=0L\_{a}=0). This feature allows us to use an inverse probability weighting approach to identify the competition effect. Since the terms in the sum are non-zero only when μa​(Ri)>0\mu\_{a}(R\_{i})>0, we can substitute the observed outcome YiY\_{i} for the unobserved mean, which yields an identified expression:

|  |  |  |
| --- | --- | --- |
|  | DP​𝒰​(𝐜0,PR|0)​[sR]=𝔼0​[γ​(Rj)​sW​(Wj)],\displaystyle D\_{P}\mathcal{U}(\mathbf{c}\_{0},P\_{R|0})[s\_{R}]=\mathbb{E}\_{0}[\gamma(R\_{j})s\_{W}(W\_{j})], |  |

where γ​(Rj):=𝔼0​[Yi​LAi​(Ri,Rj)μAi​(Ri,𝐜0,PR|0)|Rj]\gamma(R\_{j}):=\mathbb{E}\_{0}\left[Y\_{i}\frac{L\_{A\_{i}}(R\_{i},R\_{j})}{\mu\_{A\_{i}}(R\_{i},\mathbf{c}\_{0},P\_{R|0})}|R\_{j}\right]. This term, γ​(Rj)\gamma(R\_{j}), is the average welfare spillover that an agent with report RjR\_{j} imposes on others through pure competition, holding the market’s conduct fixed. Since the functional derivative LAiL\_{A\_{i}} is known from the mechanism rule (Assumption [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmassumption1 "Assumption 3.1 (Well-Behaved Mechanism). ‣ 3.2 The Indirect Effect: Competition and Market Conduct ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")), this entire expression is identified from the data.

#### 3.2.2 The Market Conduct Effect

The market conduct effect, ∇𝐜𝒰​(𝐜0,PR|0)⋅𝐜′​[sR]\nabla\_{\mathbf{c}}\mathcal{U}(\mathbf{c}\_{0},P\_{R|0})\cdot\mathbf{c}^{\prime}[s\_{R}], captures the total welfare impact from the endogenous response of the market-clearing parameters. Characterizing it requires understanding two building blocks: first, how aggregate welfare responds to an infinitesimal change in the clearing parameters (∇𝐜𝒰\nabla\_{\mathbf{c}}\mathcal{U}), and second, how the clearing parameters themselves respond to the policy reform (𝐜′​[sR]\mathbf{c}^{\prime}[s\_{R}]).

##### The Welfare Response to Clearing Parameters (∇𝐜𝒰\nabla\_{\mathbf{c}}\mathcal{U}).

The gradient ∇𝐜𝒰\nabla\_{\mathbf{c}}\mathcal{U} captures the effect of tightening or loosening the market’s eligibility constraints. An infinitesimal change in 𝐜\mathbf{c} affects welfare through two channels: a smooth change for inframarginal agents (via hah\_{a}) and a discontinuous change for marginal agents at the eligibility boundary (via ϕa\phi\_{a}). To formally analyze these marginal agents, we require the following regularity condition.

###### Assumption 3.2 (Marginal Agents).

For each a∈𝒜a\in\mathcal{A}:

1. (a)

   The report RiR\_{i} consists of two components, (Ri,u​n,Ri,c​o​n​t)(R\_{i,un},R\_{i,cont}), such that conditional on Ri,u​nR\_{i,un} the distribution of Ri,c​o​n​tR\_{i,cont} is absolutely continuous with respect to the Lebesgue measure.
2. (b)

   The functions hah\_{a} and ϕa\phi\_{a} are smooth in rc​o​n​tr\_{cont}.
3. (c)

   The continuous report component has a non-degenerate effect on eligibility,

   |  |  |  |
   | --- | --- | --- |
   |  | ‖∇rc​o​n​tϕa​(ru​n,rc​o​n​t,𝐜)‖2>0.\displaystyle\|\nabla\_{r\_{cont}}\phi\_{a}(r\_{un},r\_{cont},\mathbf{c})\|\_{2}>0. |  |
4. (d)

   The conditional mean potential outcome, ma​(r):=𝔼0​[Yi​(Wi,a)|Ri=r]m\_{a}(r):=\mathbb{E}\_{0}[Y\_{i}(W\_{i},a)|R\_{i}=r], is continuous in rc​o​n​tr\_{cont}.

This assumption ensures that the concept of "marginal agents" is well-defined and provides the necessary regularity to identify the welfare impact at the boundary. The gradient ∇𝐜𝒰\nabla\_{\mathbf{c}}\mathcal{U} is the sum of the effects on these two groups. Let Ξa​(Ri)\Xi\_{a}(R\_{i}) be the welfare impact for agents at the margin of allocation aa:

|  |  |  |
| --- | --- | --- |
|  | Ξa​(Ri):=ma​(Ri)​ha​(Ri,𝐜0,PR|0)​∇𝐜ϕa​(Ri,𝐜0).\Xi\_{a}(R\_{i}):=m\_{a}(R\_{i})h\_{a}(R\_{i},\mathbf{c}\_{0},P\_{R|0})\nabla\_{\mathbf{c}}\phi\_{a}(R\_{i},\mathbf{c}\_{0}). |  |

The total gradient is then given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇𝐜𝒰​(𝐜0,PR|0)=\displaystyle\nabla\_{\mathbf{c}}\mathcal{U}(\mathbf{c}\_{0},P\_{R|0})= | ∑a=0K𝔼0​[𝔼0​[Ξa​(Ri)|ϕa​(Ri,𝐜0)=0,Ri,u​n]​fϕa|Ru​n​(0|Ri,u​n)]⏟Marginal (RDD) Effect\displaystyle\underbrace{\sum\_{a=0}^{K}\mathbb{E}\_{0}\left[\mathbb{E}\_{0}\left[\Xi\_{a}(R\_{i})\bigg|\phi\_{a}(R\_{i},\mathbf{c}\_{0})=0,R\_{i,un}\right]f\_{\phi\_{a}|R\_{un}}(0|R\_{i,un})\right]}\_{\text{Marginal (RDD) Effect}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼0​[Yi​∇𝐜hAi​(Ri,𝐜0,PR|0)hAi​(Ri,𝐜0,PR|0)]⏟Inframarginal Effect\displaystyle+\underbrace{\mathbb{E}\_{0}\left[Y\_{i}\frac{\nabla\_{\mathbf{c}}h\_{A\_{i}}(R\_{i},\mathbf{c}\_{0},P\_{R|0})}{h\_{A\_{i}}(R\_{i},\mathbf{c}\_{0},P\_{R|0})}\right]}\_{\text{Inframarginal Effect}} |  |

Each component of this gradient is identified from the data. The inframarginal effect is a standard expectation over observed quantities, using the known functional form of hah\_{a}. The marginal effect is a sum of RDD effects, which are identified under Assumption [3.2](https://arxiv.org/html/2510.20032v1#S3.Thmassumption2 "Assumption 3.2 (Marginal Agents). ‣ The Welfare Response to Clearing Parameters (∇_𝐜𝒰). ‣ 3.2.2 The Market Conduct Effect ‣ 3.2 The Indirect Effect: Competition and Market Conduct ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") from local comparisons of agents at the eligibility boundary. As we will demonstrate concretely in our examples in Section [4](https://arxiv.org/html/2510.20032v1#S4 "4 Examples ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), these boundary terms often correspond directly to the LATEs that are the focus of the empirical market design literature. Our framework thus clarifies that these well-studied parameters are not merely reduced-form objects but are, in fact, essential structural inputs for any equilibrium analysis.

##### The Response of Clearing Parameters (𝐜′​[sR]\mathbf{c}^{\prime}[s\_{R}]).

The second building block, the derivative of the market conduct rule 𝐜′​(⋅)\mathbf{c}^{\prime}(\cdot), describes how the clearing parameters themselves respond to a policy reform. This response depends critically on the nature of the rule, and we highlight two canonical cases that correspond to distinct economic environments.

Case 1: Competitive Equilibrium. In many markets, the clearing parameters passively adjust to satisfy exogenous constraints, such as fixed supply. This is analogous to a competitive equilibrium where prices clear the market. As shown in our fixed-supply example from Section [2](https://arxiv.org/html/2510.20032v1#S2 "2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), the conduct rule 𝔼PR​[μa​(𝐜,Ri)]=qa\mathbb{E}\_{P\_{R}}[\mu\_{a}(\mathbf{c},R\_{i})]=q\_{a} depends on integrals over the entire report distribution. This property ensures the derivative 𝐜′​[sR]\mathbf{c}^{\prime}[s\_{R}] is a continuous linear functional in the standard space of square-integrable functions, L2L\_{2}. This means the derivative can be represented by a familiar influence function through a standard expectation:

|  |  |  |
| --- | --- | --- |
|  | 𝐜′​[sR]=𝔼0​[𝝍𝐜0​(Ri)​sR​(Ri)].\mathbf{c}^{\prime}[s\_{R}]=\mathbb{E}\_{0}[\bm{\psi}\_{\mathbf{c}\_{0}}(R\_{i})s\_{R}(R\_{i})]. |  |

The influence function 𝝍𝐜0​(Ri)\bm{\psi}\_{\mathbf{c}\_{0}}(R\_{i}) is derived from the implicit function theorem and its form is determined by the local structure of the market at the baseline equilibrium:

|  |  |  |
| --- | --- | --- |
|  | 𝝍𝐜0​(Ri)=−𝐉0−1​(μ1​(𝐜0,Ri)⋮μK​(𝐜0,Ri)).\bm{\psi}\_{\mathbf{c}\_{0}}(R\_{i})=-\mathbf{J}\_{0}^{-1}\begin{pmatrix}\mu\_{1}(\mathbf{c}\_{0},R\_{i})\\ \vdots\\ \mu\_{K}(\mathbf{c}\_{0},R\_{i})\end{pmatrix}. |  |

Here, the matrix 𝐉0\mathbf{J}\_{0} is the Jacobian of the vector of aggregate market shares with respect to 𝐜\mathbf{c}. This object, which is identified from the data given Assumption [2.1](https://arxiv.org/html/2510.20032v1#S2.Thmassumption1 "Assumption 2.1 (Anonymous Allocation Mechanism). ‣ 2.1 Environment ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), captures how a small change in the clearing parameters affects aggregate demand.

Case 2: Monopoly. In other settings, the market maker is an active agent who sets parameters to optimize an objective, such as maximizing revenue. This is analogous to a monopolist’s problem. Our optimal reserve price example, where the rule (1−FR​(c))−c​fR​(c)=0(1-F\_{R}(c))-cf\_{R}(c)=0 is the seller’s first-order condition, illustrates this case. Here, the rule’s dependence on the probability density function, fR​(c)f\_{R}(c), at the specific point cc makes the operator mathematically ill-behaved in the standard L2L\_{2} space. Handling such cases requires restricting the analysis to smoother policy reforms, which is achieved by working in a different function space (a Sobolev space).

The contrast between these two economically distinct cases—passive market clearing versus active optimization—motivates our general approach, which we formalize next.

###### Assumption 3.3 (Differentiability of the Market Conduct Rule).

The market conduct rule 𝐜​(⋅)\mathbf{c}(\cdot) is differentiable at PR|0P\_{R|0} with respect to a tangent set of scores in a Hilbert space ℋR\mathcal{H}\_{R}. Its derivative has the representation:

|  |  |  |
| --- | --- | --- |
|  | 𝐜′​[sR]=⟨𝝍𝐜0,sR⟩ℋR,\mathbf{c}^{\prime}[s\_{R}]=\langle\bm{\psi}\_{\mathbf{c}\_{0}},s\_{R}\rangle\_{\mathcal{H}\_{R}}, |  |

where ⟨⋅,⋅⟩ℋR\langle\cdot,\cdot\rangle\_{\mathcal{H}\_{R}} is the inner product on ℋR\mathcal{H}\_{R} and 𝛙𝐜0\bm{\psi}\_{\mathbf{c}\_{0}} is the representer of the derivative.

The function 𝝍𝐜0​(Ri)\bm{\psi}\_{\mathbf{c}\_{0}}(R\_{i}) is the influence function of the market conduct rule, generalized to the appropriate space ℋR\mathcal{H}\_{R}.

### 3.3 The Equilibrium-Adjusted Outcome

Having established that each building block of the indirect effect—the competition externality γ​(Ri)\gamma(R\_{i}), the welfare gradient ∇𝐜𝒰\nabla\_{\mathbf{c}}\mathcal{U}, and the influence function of the market conduct rule 𝝍𝐜0\bm{\psi}\_{\mathbf{c}\_{0}}—is identified from the data under our assumptions, we can now combine them to state our main result. The total MPE is the sum of the direct effect and the two components of the indirect effect. The technical subtleties of the market conduct rule prevent the entire MPE from always being expressed as a single covariance. Our main theorem, therefore, presents the MPE in a more general form that respects this distinction.

###### Theorem 3.1 (The Marginal Policy Effect).

Suppose Assumptions [2.1](https://arxiv.org/html/2510.20032v1#S2.Thmassumption1 "Assumption 2.1 (Anonymous Allocation Mechanism). ‣ 2.1 Environment ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")-[2.4](https://arxiv.org/html/2510.20032v1#S2.Thmassumption4 "Assumption 2.4 (Policy Invariance). ‣ 2.2 From Policy to Likelihood: Tracing the Perturbation ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") and [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmassumption1 "Assumption 3.1 (Well-Behaved Mechanism). ‣ 3.2 The Indirect Effect: Competition and Market Conduct ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")-[3.3](https://arxiv.org/html/2510.20032v1#S3.Thmassumption3 "Assumption 3.3 (Differentiability of the Market Conduct Rule). ‣ The Response of Clearing Parameters (𝐜'⁢[𝑠_𝑅]). ‣ 3.2.2 The Market Conduct Effect ‣ 3.2 The Indirect Effect: Competition and Market Conduct ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") hold and for each a∈𝒜a\in\mathcal{A} the conditional expectation function, ma​(ru​n,rc​o​n​t)m\_{a}(r\_{un},r\_{cont}), is bounded and continuous in rc​o​n​tr\_{cont}. Then, the MPE is identified and can be expressed as:

|  |  |  |
| --- | --- | --- |
|  | 𝒰′​(sW)=𝔼0​[Ψifixed​sW​(Wi)]+⟨Ψconduct,sR⟩ℋR\displaystyle\mathcal{U}^{\prime}(s\_{W})=\mathbb{E}\_{0}[\Psi\_{i}^{\text{fixed}}s\_{W}(W\_{i})]+\langle\Psi^{\text{conduct}},s\_{R}\rangle\_{\mathcal{H}\_{R}} |  |

where Ψifixed\Psi\_{i}^{\text{fixed}} represents the portion of an agent’s welfare contribution independent of the market’s conduct:

|  |  |  |
| --- | --- | --- |
|  | Ψifixed=Yi⏟Private Outcome+γ​(Ri)⏟Competition Externality,\Psi\_{i}^{\text{fixed}}=\underbrace{Y\_{i}}\_{\text{Private Outcome}}+\underbrace{\gamma(R\_{i})}\_{\text{Competition Externality}}, |  |

and Ψconduct\Psi^{\text{conduct}} captures the market conduct externality:

|  |  |  |
| --- | --- | --- |
|  | Ψconduct​(Ri):=∇𝐜𝒰​(𝐜0,PR|0)⋅𝝍𝐜0​(Ri).\Psi^{\text{conduct}}(R\_{i}):=\nabla\_{\mathbf{c}}\mathcal{U}(\mathbf{c}\_{0},P\_{R|0})\cdot\bm{\psi}\_{\mathbf{c}\_{0}}(R\_{i}). |  |

Theorem [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmtheorem1 "Theorem 3.1 (The Marginal Policy Effect). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") provides a universally applicable formula for the MPE. Its two-part structure cleanly separates the welfare change into components that can be analyzed using standard covariance-based methods and a component that depends on the specific geometry of the policy space, ℋR\mathcal{H}\_{R}. This general form simplifies if the market conduct rule is differentiable in the standard L2L\_{2} space.

###### Corollary 3.1 (The Equilibrium-Adjusted Outcome).

If the market conduct rule 𝐜​(P)\mathbf{c}(P) is differentiable in ℋR=L2​(Ri)\mathcal{H}\_{R}=L\_{2}(R\_{i}), then the MPE from Theorem [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmtheorem1 "Theorem 3.1 (The Marginal Policy Effect). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") can be written as:

|  |  |  |
| --- | --- | --- |
|  | 𝒰′​(sW)=𝔼0​[Ψitotal​sW​(Wi)],\displaystyle\mathcal{U}^{\prime}(s\_{W})=\mathbb{E}\_{0}[\Psi\_{i}^{\text{total}}s\_{W}(W\_{i})], |  |

where Ψitotal\Psi\_{i}^{\text{total}} is the score-independent equilibrium-adjusted outcome. It represents an agent’s total contribution to welfare:

|  |  |  |
| --- | --- | --- |
|  | Ψitotal=Ψifixed+Ψconduct​(Ri).\Psi\_{i}^{\text{total}}=\Psi\_{i}^{\text{fixed}}+\Psi^{\text{conduct}}(R\_{i}). |  |

This corollary recovers the powerful intuition from our motivating discussion. In many common environments, all complex market interactions can be summarized by a single, policy-invariant structural object, Ψitotal\Psi\_{i}^{\text{total}}. This object represents the correct welfare-relevant outcome for a policymaker. To find the welfare-maximizing local reform, one must simply find the policy score that has the highest covariance with this fixed, structural outcome.

The power of this "separation principle" is that it provides a unified foundation for addressing a range of practical policy questions. By isolating the full market structure in the single object Ψitotal\Psi\_{i}^{\text{total}}, our framework provides a flexible tool for applied work. As we demonstrate in Section [5](https://arxiv.org/html/2510.20032v1#S5 "5 Applications and Extensions ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), this allows our framework to address complex empirical challenges, including optimal policy targeting and endogenous selection.

## 4 Examples

In this section, we illustrate how our general framework applies to several canonical economic environments. These examples serve to build intuition by showing how the abstract components of the marginal policy effect map onto concrete, estimable quantities in specific models. The examples also clarify the conditions under which a researcher can identify the full welfare function versus only its local gradient. We begin with simple single-product markets and proceed to more complex, multi-product settings.

### 4.1 Single Product with Random Rationing

Consider a market for a single product (𝒜={0,1}\mathcal{A}=\{0,1\}) with fixed supply qq. The policy is a binary treatment, Wi∈{0,1}W\_{i}\in\{0,1\}, and agents submit a preference report Ri∈{0,1}R\_{i}\in\{0,1\}, where Ri=1R\_{i}=1 indicates a desire for the product. The product is allocated via random rationing, so the allocation probability is

|  |  |  |
| --- | --- | --- |
|  | μ1​(Ri,c)=Ri⋅c,\displaystyle\mu\_{1}(R\_{i},c)=R\_{i}\cdot c, |  |

where the rationing probability cc is the market-clearing parameter that adjusts to satisfy the fixed supply constraint

|  |  |  |
| --- | --- | --- |
|  | 𝔼(θ,sW)​[μ1​(Ri,c)]=q1.\displaystyle\mathbb{E}\_{(\theta,s\_{W})}[\mu\_{1}(R\_{i},c)]=q\_{1}. |  |

The mechanism is strategy-proof, so this report reflects agents’ true preferences. We assume excess demand at baseline, 𝔼0​[Ri]>q1\mathbb{E}\_{0}[R\_{i}]>q\_{1}. The equilibrium constraint 𝔼(θ,sW)[Ri⋅c]=q1\mathbb{E}\_{(\theta,s\_{W}})[R\_{i}\cdot c]=q\_{1} implies that c​(PR|θ,sW)=q1/𝔼(θ,sW)​[Ri]c(P\_{R|\theta,s\_{W}})=q\_{1}/\mathbb{E}\_{(\theta,s\_{W})}[R\_{i}]. A policy reform alters the share of agents demanding the product, which creates an equilibrium effect through the adjustment of c​(θ)c(\theta).

We derive the equilibrium-adjusted outcome Ψitotal\Psi\_{i}^{\text{total}} by applying Corollary [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmcorollary1 "Corollary 3.1 (The Equilibrium-Adjusted Outcome). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."). Since the allocation rule μ1​(Ri,c)\mu\_{1}(R\_{i},c) depends only on an agent’s own report and the clearing parameter cc, and not on the aggregate report distribution PRP\_{R}, the competition term, γ​(Ri)\gamma(R\_{i}), is zero. The indirect effect therefore operates entirely through the market conduct externality. Let τ​(r):=𝔼θ0​[Yi​(Wi,1)−Yi​(Wi,0)|Ri=r]\tau(r):=\mathbb{E}\_{\theta\_{0}}[Y\_{i}(W\_{i},1)-Y\_{i}(W\_{i},0)|R\_{i}=r] denote the average treatment effect of the allocation for agents with report rr. The market conduct externality an agent imposes by demanding the good (Ri=1R\_{i}=1) simplifies to τ​(1)\tau(1).

The resulting equilibrium-adjusted outcome is:

|  |  |  |
| --- | --- | --- |
|  | Ψitotal=Yi−τ​(1)⋅Ai.\Psi\_{i}^{\text{total}}=Y\_{i}-\tau(1)\cdot A\_{i}. |  |

The interpretation is direct: an agent’s total contribution to welfare is their private outcome, YiY\_{i}, net of the externality they impose by receiving a unit of the scarce good (Ai=1A\_{i}=1). This externality is valued at τ​(1)\tau(1), which represents the average welfare gain the good provides to the other potential recipients displaced at the margin.

This stylized example connects directly to empirical work. The term τ​(1)\tau(1) is a policy-specific local average treatment effect. If the policy WiW\_{i} has no direct effect on outcomes (Yi​(w,a)=Yi​(a)Y\_{i}(w,a)=Y\_{i}(a)), this term simplifies to the standard LATE identified in school choice lotteries (e.g., Abdulkadiroğlu et al., [2017](https://arxiv.org/html/2510.20032v1#bib.bib2); Walters, [2018](https://arxiv.org/html/2510.20032v1#bib.bib47)). Our framework shows that this familiar estimand is not just a reduced form quantity; it is a structural object needed to conduct counterfactual policy analysis, echoing the approach in Kline and Walters ([2016](https://arxiv.org/html/2510.20032v1#bib.bib29)).

### 4.2 Price-Based Allocation

We now consider a market where the report Ri∈ℝ+R\_{i}\in\mathbb{R}\_{+} is a continuous valuation for a single product, and allocation is determined by a market-clearing price or cutoff, cc. An agent receives the product if their valuation exceeds the price, so the allocation rule is the discontinuous function μ1​(Ri,c)=𝟏​{Ri>c}\mu\_{1}(R\_{i},c)=\mathbf{1}\{R\_{i}>c\}. We assume the distribution of reports RiR\_{i} admits a continuous, positive density, f​(r)f(r). We also assume that the conditional mean functions {m0​(r),m1​(r)}\{m\_{0}(r),m\_{1}(r)\} are continuous functions of reports. The market-clearing price c​(PR|θ,sW)c(P\_{R|\theta,s\_{W}}) is set to satisfy the supply constraint,

|  |  |  |
| --- | --- | --- |
|  | 𝔼(θ,sW)​[𝟏​{Ri>c}]=q,\displaystyle\mathbb{E}\_{(\theta,s\_{W})}[\mathbf{1}\{R\_{i}>c\}]=q, |  |

which implies that c​(PR|θ,sW)c(P\_{R|\theta,s\_{W}}) is the (1−q)(1-q)-quantile of the report distribution under policy regime θ\theta.

As in the random rationing case, the allocation rule does not depend on the aggregate report distribution PRP\_{R}, so the competition externality term, γ​(Ri)\gamma(R\_{i}), is zero. The indirect effect operates entirely through the market conduct externality. The welfare gradient with respect to the cutoff is the effect on aggregate welfare of marginally raising the price, which under stated conditions is

|  |  |  |
| --- | --- | --- |
|  | ∇c𝒰​(θ0)=−[m1​(c0)−m0​(c0)]​f​(c0).\displaystyle\nabla\_{c}\mathcal{U}(\theta\_{0})=-[m\_{1}(c\_{0})-m\_{0}(c\_{0})]f(c\_{0}). |  |

The market’s response, c′​(⋅)c^{\prime}(\cdot) is given by the following influence function

|  |  |  |
| --- | --- | --- |
|  | ψc0​(Ri)=−𝟏​{Ri>c}f​(c0)=−Aif​(c0)\psi\_{c\_{0}}(R\_{i})=-\frac{\mathbf{1}\{R\_{i}>c\}}{f(c\_{0})}=-\frac{A\_{i}}{f(c\_{0})} |  |

The density terms cancel, leaving a simple expression for the market conduct term:

|  |  |  |
| --- | --- | --- |
|  | Ψitotal=Yi−τ​(c0)⋅Ai.\displaystyle\Psi\_{i}^{\text{total}}=Y\_{i}-\tau(c\_{0})\cdot A\_{i}. |  |

The simplicity of this final expression, where the density terms cancel, reveals a powerful economic intuition. The market conduct externality is the product of two opposing forces. The first is the aggregate welfare impact of a marginal increase in the cutoff, which is large when the density at the cutoff, f​(c0)f(c\_{0}), is high, as many agents are affected. The second is the influence of a single inframarginal agent on the equilibrium cutoff, which is small when the density f​(c0)f(c\_{0}) is high, as only a small price change is needed to displace one marginal agent to make room for them. These two effects, one proportional to the density and the other inversely proportional to it, exactly offset each other. The result is that the externality any inframarginal agent imposes is simply the welfare loss of the single agent at the margin that they displace, −τ​(c0)-\tau(c\_{0}). This last term, τ​(c0)\tau(c\_{0}), is precisely the RDD estimand used to quantify the effects of charter schools (e.g., abdulkadi̇rouglu2022breaking). Our framework demonstrates that this RDD parameter can be directly used to compute the welfare consequences of any local policy.

### 4.3 Second-Price Auction

We now illustrate the full decomposition of the MPE in a second-price auction for a single good with nn i.i.d. participants. The second-price auction is strategy proof, which implies that bidding one’s private valuation, Ri∈ℝ+R\_{i}\in\mathbb{R}\_{+}, is a dominant strategy. The platform sets a reserve price, cc, to ensure the ex-ante probability of winning is a fixed quantity, qq.444This is relevant in applications like sponsored search, where a platform may wish to display advertisements with a certain frequency. An agent with valuation RiR\_{i} wins if they bid above the reserve price and have the highest bid among all participants, so their win probability is

|  |  |  |
| --- | --- | --- |
|  | μ1​(Ri,c,PR)=𝟏​{Ri>c}⋅[FR​(Ri)]n−1.\displaystyle\mu\_{1}(R\_{i},c,P\_{R})=\mathbf{1}\{R\_{i}>c\}\cdot[F\_{R}(R\_{i})]^{n-1}. |  |

A policy that perturbs the distribution of valuations creates spillovers through two distinct channels. First, it affects the reserve price c​(PR|θ,sW)c(P\_{R|\theta,s\_{W}}) needed to meet the win-rate target—a market conduct effect. Second, it changes the distribution of competing bids, PR|θ,sWP\_{R|\theta,s\_{W}}, altering the win probability for all bidders above the reserve price. As a result, this example features a non-zero competition effect, γ​(Ri)≠0\gamma(R\_{i})\neq 0.

To see how this competition effect is constructed, we first compute the functional derivative of the win probability, L1​(r,r′)L\_{1}(r,r^{\prime}). A change in the density of bidders at value r′r^{\prime} only affects bidders with valuations r>r′r>r^{\prime}, as it changes the value of the CDF FR​(r)F\_{R}(r). Applying the definition of the functional derivative yields:

|  |  |  |
| --- | --- | --- |
|  | L1​(r,r′)=∂μ1​(r,c,PR)∂PR​(r′)=𝟏​{r>c}⋅(n−1)​[FR​(r)]n−2⋅𝟏​{r′≤r}.L\_{1}(r,r^{\prime})=\frac{\partial\mu\_{1}(r,c,P\_{R})}{\partial P\_{R}(r^{\prime})}=\mathbf{1}\{r>c\}\cdot(n-1)[F\_{R}(r)]^{n-2}\cdot\mathbf{1}\{r^{\prime}\leq r\}. |  |

Substituting this into the general formula for the competition externality from Section [3](https://arxiv.org/html/2510.20032v1#S3 "3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), 𝔼0​[Yi​LAi​(Ri,Rj)μAi​(Ri,𝐜0,PR|0)|Rj]\mathbb{E}\_{0}\left[Y\_{i}\frac{L\_{A\_{i}}(R\_{i},R\_{j})}{\mu\_{A\_{i}}(R\_{i},\mathbf{c}\_{0},P\_{R|0})}|R\_{j}\right] gives the expression for γ​(Ri)\gamma(R\_{i}).

Combining these components yields the equilibrium-adjusted outcome, which is the sum of the private outcome and two distinct externality terms:

|  |  |  |
| --- | --- | --- |
|  | Ψitotal=Yi⏟Private Outcome+γ​(Ri)⏟Competition Externality+Ψconduct​(Ri)⏟Market Conduct Externality.\displaystyle\Psi\_{i}^{\text{total}}=\underbrace{Y\_{i}}\_{\text{Private Outcome}}+\underbrace{\gamma(R\_{i})}\_{\text{Competition Externality}}+\underbrace{\Psi^{\text{conduct}}(R\_{i})}\_{\text{Market Conduct Externality}}. |  |

Here, the competition externality, γ​(Ri)\gamma(R\_{i}), is the welfare impact an agent’s bid imposes on inframarginal competitors. It can be expressed intuitively using the maximum order statistic of the competing bids, R(n−1)R\_{(n-1)}:

|  |  |  |
| --- | --- | --- |
|  | γ​(Ri)=𝔼0​[τ​(R(n−1))|R(n−1)≥r~]×(1−FR|0​(R~i)n−1),where ​R~i=max⁡(c0,Ri).\displaystyle\gamma(R\_{i})=\mathbb{E}\_{0}\left[\tau(R\_{(n-1)})|R\_{(n-1)}\geq\tilde{r}\right]\times\left(1-F\_{R|0}(\tilde{R}\_{i})^{n-1}\right),\quad\text{where }\tilde{R}\_{i}=\max(c\_{0},R\_{i}). |  |

This is the expected treatment effect for the winning competitor, conditional on them being a relevant threat (bidding above r~\tilde{r}), multiplied by the probability that such a threat exists. The market conduct externality, Ψconduct​(Ri)\Psi^{\text{conduct}}(R\_{i}), is the welfare impact from agent ii’s influence on the equilibrium reserve price:

|  |  |  |
| --- | --- | --- |
|  | Ψconduct​(Ri)=−τ​(c0)​FR|0​(c0)n−1​𝟏​{Ri>c0}.\displaystyle\Psi^{\text{conduct}}(R\_{i})=-\tau(c\_{0})F\_{R|0}(c\_{0})^{n-1}\mathbf{1}\{R\_{i}>c\_{0}\}. |  |

#### 4.3.1 Optimal reserve price

Our analysis above focused on a c​(⋅)c(\cdot) that forces a fixed allocation probability. We now discuss a more complex objective for the platform: setting the reserve price cc to maximize the expected revenue, following the principles of optimal auction design (Myerson, [1981](https://arxiv.org/html/2510.20032v1#bib.bib39)). The optimal reserve price c​(PR)c(P\_{R}) is the solution to the first-order condition:

|  |  |  |
| --- | --- | --- |
|  | 1−FR​(c​(PR))−c​(PR)​fR​(c​(PR))=0.1-F\_{R}(c(P\_{R}))-c(P\_{R})f\_{R}(c(P\_{R}))=0. |  |

As discussed in our theoretical section, the dependency on the density fRf\_{R} means the derivative c′​(PR)c^{\prime}(P\_{R}) is not a continuous operator in L2L\_{2}. Correctly characterizing the market conduct effect requires our general framework based on a Sobolev space, ℋR\mathcal{H}\_{R}, with the inner product:

|  |  |  |
| --- | --- | --- |
|  | ⟨ψc0,sR⟩ℋR:=𝔼0​[ψc0​(Ri)​sR​(Ri)]+𝔼0​[ψc0′​(Ri)​sR′​(Ri)].\langle\psi\_{c\_{0}},s\_{R}\rangle\_{\mathcal{H}\_{R}}:=\mathbb{E}\_{0}[\psi\_{c\_{0}}(R\_{i})s\_{R}(R\_{i})]+\mathbb{E}\_{0}[\psi\_{c\_{0}}^{\prime}(R\_{i})s\_{R}^{\prime}(R\_{i})]. |  |

As shown in Appendix [C](https://arxiv.org/html/2510.20032v1#A3 "Appendix C Examples ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), the representer for the derivative of the optimal reserve price, ψc0\psi\_{c\_{0}}, is the solution to the following Sturm-Liouville differential equation:

|  |  |  |
| --- | --- | --- |
|  | ψc0​(r)​fR|0​(r)−(ψc0′​(r)​fR|0​(r))′=K⋅(𝟏​{r≤c0}​fR|0​(r)+α​δ​(r−c0)).\psi\_{c\_{0}}(r)f\_{R|0}(r)-(\psi\_{c\_{0}}^{\prime}(r)f\_{R|0}(r))^{\prime}=K\cdot\left(\mathbf{1}\{r\leq c\_{0}\}f\_{R|0}(r)+\alpha\delta(r-c\_{0})\right). |  |

While complex, this equation can be solved for a given baseline density fR|0f\_{R|0}, yielding the influence function ψc0​(⋅)\psi\_{c\_{0}}(\cdot). The MPE is then fully identified by applying our general formula from Theorem [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmtheorem1 "Theorem 3.1 (The Marginal Policy Effect). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), demonstrating the framework’s capacity to handle a wide class of economically relevant mechanisms.

### 4.4 School Choice with Multiple Schools

Our final example is a multi-product extension of the price-based model: a centralized school choice mechanism. As shown by Azevedo and Leshno ([2016](https://arxiv.org/html/2510.20032v1#bib.bib9)), allocations in large matching markets can often be characterized by a vector of market-clearing score cutoffs, which makes this an empirically relevant setting.

Consider a market with two schools (k=1,2k=1,2) and an outside option (k=0k=0), each with capacity qkq\_{k}. A student’s type RiR\_{i} consists of a preference ranking, ≻i\succ\_{i}, and a vector of school-specific scores, (Vi,1,Vi,2)(V\_{i,1},V\_{i,2}). A student is assigned to their most-preferred school kk for which they are eligible, which requires their score to exceed the school’s cutoff, Vi,k>ckV\_{i,k}>c\_{k}. The vector of cutoffs 𝐜=(c1,c2)\mathbf{c}=(c\_{1},c\_{2}) is set endogenously to ensure that the number of assigned students exactly meets the capacity constraints for each school.

A policy reform perturbs the joint distribution of preferences and scores. To maintain equilibrium, the market responds by adjusting the cutoff vector by a marginal amount, 𝐜′=(c1′,c2′)\mathbf{c}^{\prime}=(c\_{1}^{\prime},c\_{2}^{\prime}). This change in cutoffs reallocates students who are precisely on the margin of admission. The score space, shown in Figure [I](https://arxiv.org/html/2510.20032v1#S4.F1 "Figure I ‣ 4.4 School Choice with Multiple Schools ‣ 4 Examples ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), helps build intuition. The initial cutoffs (c1,c2)(c\_{1},c\_{2}) define eligibility regions. When the policy changes, the cutoffs shift, creating thin “bands” of students whose eligibility status changes. The welfare impact of the reform depends entirely on who these marginal students are and how they are reallocated based on their preferences.

V1V\_{1}V2V\_{2}c1c\_{1}c2c\_{2}c1+c1′c\_{1}+c^{\prime}\_{1}c2+c2′c\_{2}+c^{\prime}\_{2}



Figure I: A policy reform shifts cutoffs from the dashed to the red lines. Students in the shaded red bands are “marginal”—their eligibility changes.

We can define the key building blocks for this effect: let ρj→k\rho\_{j\to k} be the density of students at the cutoff for school jj (i.e., with score Vi,j=cjV\_{i,j}=c\_{j}) who, upon losing eligibility for jj, are reallocated to school kk. Let τj→k​(cj)\tau\_{j\to k}(c\_{j}) be the average causal effect of this switch for this specific group:

|  |  |  |
| --- | --- | --- |
|  | τj→k​(cj)=𝔼​[Yi​(Wi,k)−Yi​(Wi,j)|Vi,j=cj,reallocated from ​j​ to ​k].\displaystyle\tau\_{j\to k}(c\_{j})=\mathbb{E}[Y\_{i}(W\_{i},k)-Y\_{i}(W\_{i},j)|V\_{i,j}=c\_{j},\text{reallocated from }j\text{ to }k]. |  |

These are precisely the types of parameters estimated in RDD-based studies of school choice. Table [1](https://arxiv.org/html/2510.20032v1#S4.T1 "Table 1 ‣ 4.4 School Choice with Multiple Schools ‣ 4 Examples ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") illustrates the primary reallocations (assuming cutoffs rise).

These densities of marginal students are the building blocks of the Jacobian matrix, 𝐉\mathbf{J}, which describes the derivative of the market conduct rule, 𝐜′​(PR|0)\mathbf{c}^{\prime}(P\_{R|0}). An element Jk​jJ\_{kj} of this matrix represents the change in enrollment at school kk from a marginal increase in the cutoff for school jj. The diagonal elements are negative (raising a school’s cutoff lowers its own enrollment), while the off-diagonal elements are positive (raising one school’s cutoff pushes some students to the other school). The Jacobian for this market is:

|  |  |  |
| --- | --- | --- |
|  | 𝐉=(−(ρ1→0+ρ1→2)ρ2→1ρ1→2−(ρ2→0+ρ2→1))\mathbf{J}=\begin{pmatrix}-(\rho\_{1\to 0}+\rho\_{1\to 2})&\rho\_{2\to 1}\\ \rho\_{1\to 2}&-(\rho\_{2\to 0}+\rho\_{2\to 1})\end{pmatrix} |  |

The non-zero off-diagonal terms, ρ1→2\rho\_{1\to 2} and ρ2→1\rho\_{2\to 1}, explicitly measure the cross-school substitution effects.

The market conduct externality for a seat at each school, which we denote by the vector 𝐯=(v1,v2)\mathbf{v}=(v\_{1},v\_{2}), is a combination of the marginal effects at both cutoffs, adjusted for the full matrix of equilibrium interactions. Define G1:=−[∇𝐜𝒰​(c0)]1=−(ρ1→0​τ1→0+ρ1→2​τ1→2)G\_{1}:=-[\nabla\_{\mathbf{c}}\mathcal{U}(c\_{0})]\_{1}=-(\rho\_{1\to 0}\tau\_{1\to 0}+\rho\_{1\to 2}\tau\_{1\to 2}) and G2:=−[∇𝐜𝒰​(c0)]2=(ρ2→1​τ2→1+ρ2→0​τ2→0)G\_{2}:=-[\nabla\_{\mathbf{c}}\mathcal{U}(c\_{0})]\_{2}=(\rho\_{2\to 1}\tau\_{2\to 1}+\rho\_{2\to 0}\tau\_{2\to 0}) be the total welfare effect at each margin. Solving the system of equilibrium interactions yields the following expressions for the social externality values:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v1\displaystyle v\_{1} | =1det(𝐉)​[(ρ2→0+ρ2→1)​G1+ρ1→2​G2]\displaystyle=\frac{1}{\det(\mathbf{J})}\left[(\rho\_{2\to 0}+\rho\_{2\to 1})G\_{1}+\rho\_{1\to 2}G\_{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | v2\displaystyle v\_{2} | =1det(𝐉)​[(ρ1→0+ρ1→2)​G2+ρ2→1​G1]\displaystyle=\frac{1}{\det(\mathbf{J})}\left[(\rho\_{1\to 0}+\rho\_{1\to 2})G\_{2}+\rho\_{2\to 1}G\_{1}\right] |  |

The crucial feature of these expressions is that the social value of a seat at School 1 (v1v\_{1}) explicitly depends on the treatment effects at the margin for School 2 (embedded in G2G\_{2}), weighted by the substitution patterns.

The final equilibrium-adjusted outcome for a student is:

|  |  |  |
| --- | --- | --- |
|  | Ψitotal=Yi−v1⋅𝟏​{Ai=1}−v2⋅𝟏​{Ai=2}\Psi\_{i}^{\text{total}}=Y\_{i}-v\_{1}\cdot\mathbf{1}\{A\_{i}=1\}-v\_{2}\cdot\mathbf{1}\{A\_{i}=2\} |  |

This example shows precisely how the framework synthesizes readily interpretable RDD treatment effects (τj→k\tau\_{j\to k}) with the market’s underlying substitution patterns (𝐉\mathbf{J}) to construct the policy-invariant parameters (vkv\_{k}) required for any counterfactual policy evaluation.

Table 1: Classification of Marginal Reallocations

|  |  |  |
| --- | --- | --- |
| Marginal Group | Reallocation Path | Welfare Effect Component |
| Vi,1≈c1V\_{i,1}\approx c\_{1}, Pref: 1≻01\succ 0 | School 1 →\to Outside Option | ρ1→0⋅τ1→0​(c1)\rho\_{1\to 0}\cdot\tau\_{1\to 0}(c\_{1}) |
| Vi,2≈c2V\_{i,2}\approx c\_{2}, Pref: 2≻02\succ 0 | School 2 →\to Outside Option | ρ2→0⋅τ2→0​(c2)\rho\_{2\to 0}\cdot\tau\_{2\to 0}(c\_{2}) |
| Vi,1≈c1V\_{i,1}\approx c\_{1}, Pref: 1≻2≻01\succ 2\succ 0 | School 1 →\to School 2 | ρ1→2⋅τ1→2​(c1)\rho\_{1\to 2}\cdot\tau\_{1\to 2}(c\_{1}) |
| Vi,2≈c2V\_{i,2}\approx c\_{2}, Pref: 2≻1≻02\succ 1\succ 0 | School 2 →\to School 1 | ρ2→1⋅τ2→1​(c2)\rho\_{2\to 1}\cdot\tau\_{2\to 1}(c\_{2}) |

### 4.5 Discussion

Our main result identifies the Marginal Policy Effect—the local gradient of the welfare function at the observed equilibrium. A natural question is under what conditions a researcher can go beyond this local result to evaluate large-scale, or "global," policy changes. Proposition [2.1](https://arxiv.org/html/2510.20032v1#S2.Thmprop1 "Proposition 2.1 (Propagation of a Policy Perturbation). ‣ 2.2 From Policy to Likelihood: Tracing the Perturbation ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") shows that global identification hinges on a stringent support condition, which requires that a policy reform does not assign agents to allocations they could never have received in the baseline equilibrium.

As our examples illustrate, however, this condition is the exception rather than the rule. It holds in markets with pervasive randomness, like the random rationing mechanism, where the allocation process itself acts as an experiment that reveals the distribution of potential outcomes (Narita and Yata, [2023](https://arxiv.org/html/2510.20032v1#bib.bib40)). In contrast, markets with deterministic cutoffs—such as price-based allocation, auctions, and school choice systems—violate this condition. A marginal change in a cutoff pushes agents across a sharp boundary, meaning the causal effect of the allocation is only ever revealed for agents at that specific, observed margin.

The local nature of our identification result has an immediate implication for any analysis aiming to evaluate global reforms: such an analysis must rely on extrapolation. Our framework contributes to this goal by providing a sharp delineation between what is identified from the data and what must be assumed. By first constructing the equilibrium-adjusted outcome, Ψitotal\Psi\_{i}^{\text{total}}, applied researchers can isolate the identified foundation upon which transparent extrapolation assumptions—about functional forms or the outcomes of inframarginal agents—can be built.

## 5 Applications and Extensions

Section [3](https://arxiv.org/html/2510.20032v1#S3 "3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") developed our main theoretical result, the "separation principle," which hinges on the construction of the equilibrium-adjusted outcome, Ψitotal\Psi\_{i}^{\text{total}}. We now demonstrate the framework’s flexibility and breadth by extending it in four directions. First, we generalize the welfare criterion beyond simple averages to a broad class of distributional objectives, such as quantiles and inequality measures. Second, we incorporate observable covariates to handle selection on observables and lay the groundwork for optimal policy targeting. Third, we address endogenous selection by connecting our framework to the MTE literature. Finally, we discuss the significant identification challenges that arise in non-strategy-proof mechanisms where agent reports are themselves endogenous.

### 5.1 Beyond Average Outcomes: General Welfare Functionals

Our analysis has thus far defined aggregate welfare as the average outcome, 𝒰0=𝔼0​[Yi]\mathcal{U}\_{0}=\mathbb{E}\_{0}[Y\_{i}]. However, as foreshadowed by Remark [2.1](https://arxiv.org/html/2510.20032v1#S2.Thmremark1 "Remark 2.1 (Beyond average outcomes). ‣ Example 3: School Choice with Trading Cycles. ‣ 2.1 Environment ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), because our approach is local—focused on identifying the marginal effect of a reform—it can be extended to any welfare criterion that is sufficiently smooth with respect to the distribution of outcomes. This allows policymakers to evaluate reforms based not only on their average effects but also on their impact on other distributional objectives.

Let the welfare criterion be a functional 𝒰​(FY)\mathcal{U}(F\_{Y}) that maps the CDF of the outcome, FYF\_{Y}, to a real number. The key condition for our analysis to apply is that this functional must be Hadamard differentiable at the baseline outcome distribution, FY|0F\_{Y|0}. This is a standard smoothness condition in statistics that guarantees the existence of a well-behaved and identifiable influence function, IF​(y;FY|0)\text{IF}(y;F\_{Y|0}), which characterizes the marginal contribution of an observation yy to the overall functional. The entire analysis from our main theorems holds, with one simple substitution: the individual outcome YiY\_{i} is replaced by its marginal contribution to the welfare functional, IF​(Yi;FY|0)\text{IF}(Y\_{i};F\_{Y|0}).

The new equilibrium-adjusted outcome, which we denote Ψi𝒰\Psi\_{i}^{\mathcal{U}}, is therefore:

|  |  |  |
| --- | --- | --- |
|  | Ψi𝒰=IF​(Yi;FY|0)+γ𝒰​(Ri)+Ψconduct,𝒰​(Ri),\Psi\_{i}^{\mathcal{U}}=\text{IF}(Y\_{i};F\_{Y|0})+\gamma^{\mathcal{U}}(R\_{i})+\Psi^{\text{conduct},\mathcal{U}}(R\_{i}), |  |

where the competition externality (γ𝒰\gamma^{\mathcal{U}}) and the market conduct externality (Ψconduct,𝒰\Psi^{\text{conduct},\mathcal{U}}) are constructed exactly as before, but using the conditional expectation of the influence function, 𝔼​[IF​(Yi;FY|0)|Ai=a,Ri=r]\mathbb{E}[\text{IF}(Y\_{i};F\_{Y|0})|A\_{i}=a,R\_{i}=r], in place of the conditional mean of the outcome.

This generalization covers a wide range of common welfare criteria.

* •

  Quantiles. If the policymaker is interested in the effect on the τ\tau-th quantile of the outcome distribution, qτq\_{\tau}, the relevant influence function is IF​(y;FY|0)=τ−𝟏​{y≤qτ}fY|0​(qτ)\text{IF}(y;F\_{Y|0})=\frac{\tau-\mathbf{1}\{y\leq q\_{\tau}\}}{f\_{Y|0}(q\_{\tau})}, where fY|0f\_{Y|0} is the baseline density of the outcome. Our framework can thus be used to find the MPE of any local policy on, for example, the median outcome.
* •

  Inequality Measures. As another distributional measure, one could use the Gini coefficient. This functional is also Hadamard differentiable, and its well-known influence function can be substituted into our formulas to find the MPE of a policy on inequality.

This extension demonstrates that our framework provides a general toolkit for evaluating the local effects of policies on any social objective that can be expressed as a smooth functional of the outcome distribution.

### 5.2 Covariates, Identification, and Optimal Targeting

In many empirical settings, the assumption of unconditional random assignment is unrealistic. It is often more plausible to assume selection on observables, where a policy is randomly assigned only after conditioning on a rich set of pre-determined covariates. This section extends our baseline analysis to incorporate such covariates, serving three critical purposes. First, doing so strengthens the credibility of the underlying identification assumptions. Second, it provides the necessary foundation for designing and evaluating targeted policies. Third, this extension lays the groundwork for our analysis of selection on unobservables in the subsequent section.

We generalize our baseline framework by replacing Assumption [2.3](https://arxiv.org/html/2510.20032v1#S2.Thmassumption3 "Assumption 2.3 (Random Assignment). ‣ 2.2 From Policy to Likelihood: Tracing the Perturbation ‣ 2 Framework ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") with the following standard condition:

###### Assumption 5.1 (Unconfoundedness).

The policy instrument WiW\_{i} is randomly assigned conditional on a vector of observed, pre-determined covariates XiX\_{i}.

Under Assumption [5.1](https://arxiv.org/html/2510.20032v1#S5.Thmassumption1 "Assumption 5.1 (Unconfoundedness). ‣ 5.2 Covariates, Identification, and Optimal Targeting ‣ 5 Applications and Extensions ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), a policy reform is a change to the conditional distribution of the policy instrument, characterized by a conditional score sW|X​(w|x)s\_{W|X}(w|x). This in turn induces a marginal score on the distribution of reports, sR​(Ri):=𝔼0​[sW|X​(Wi|Xi)|Ri]s\_{R}(R\_{i}):=\mathbb{E}\_{0}[s\_{W|X}(W\_{i}|X\_{i})|R\_{i}]. The key insight of this section is that the fundamental structure of our main result remains intact. The MPE is still given by the expression from Theorem [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmtheorem1 "Theorem 3.1 (The Marginal Policy Effect). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."):

|  |  |  |
| --- | --- | --- |
|  | 𝒰′​(sW|X)=𝔼0​[Ψifixed​sW|X​(Wi|Xi)]+⟨Ψconduct,sR⟩ℋR,\mathcal{U}^{\prime}(s\_{W|X})=\mathbb{E}\_{0}[\Psi\_{i}^{\text{fixed}}s\_{W|X}(W\_{i}|X\_{i})]+\langle\Psi^{\text{conduct}},s\_{R}\rangle\_{\mathcal{H}\_{R}}, |  |

where the structural components, Ψifixed\Psi\_{i}^{\text{fixed}} and Ψconduct\Psi^{\text{conduct}}, are the same as those defined previously.

The invariance of these structural components might seem surprising, but it is a direct consequence of the mechanism’s design. Because the allocation rule responds only to an agent’s report RiR\_{i}, and not directly to the covariates XiX\_{i}, the equilibrium adjustment functions are anonymous with respect to this observed heterogeneity.555This does not preclude covariates from being part of the report, i.e., Xi⊂RiX\_{i}\subset R\_{i}, provided they are components that are unaffected by the policy instrument WiW\_{i}. This anonymity has powerful simplifying implications for empirical analysis. For instance, the local RDD estimands discussed in Section [4](https://arxiv.org/html/2510.20032v1#S4 "4 Examples ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")
only need to be identified unconditionally, rather than conditional on the full vector XiX\_{i}, thereby avoiding a curse of dimensionality.

Conceptually, this implies a departure from the standard “condition-then-aggregate” approach often used in settings with selection on observables. Our framework instead justifies a direct aggregate analysis. This insight will be crucial in the next section, where we extend this logic to handle selection on unobservables.

This structure allows us to turn to the problem of optimal policy design. Focusing on the important class of environments from Corollary [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmcorollary1 "Corollary 3.1 (The Equilibrium-Adjusted Outcome). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), where the MPE simplifies to a single covariance, we have:

|  |  |  |
| --- | --- | --- |
|  | 𝒰′​(sW|X)=𝔼0​[Ψitotal​sW|X​(Wi|Xi)].\mathcal{U}^{\prime}(s\_{W|X})=\mathbb{E}\_{0}[\Psi\_{i}^{\text{total}}s\_{W|X}(W\_{i}|X\_{i})]. |  |

This representation of the MPE as a linear functional connects our framework directly to the literature on optimal policy targeting and empirical welfare maximization (EWM) (e.g., Manski ([2004](https://arxiv.org/html/2510.20032v1#bib.bib32)); Kitagawa and Tetenov ([2018](https://arxiv.org/html/2510.20032v1#bib.bib27)); Athey and Wager ([2021](https://arxiv.org/html/2510.20032v1#bib.bib8))).
In those frameworks, the objective is to choose a policy that maximizes the expectation of a welfare-relevant outcome. Our central result shows that in an equilibrium environment, the correct welfare-relevant object is not the observed outcome YiY\_{i}, but the equilibrium-adjusted outcome, Ψitotal\Psi\_{i}^{\text{total}}. The policymaker’s problem is thus to choose a targeting rule—represented by the conditional score sW|X​(Wi|Xi)s\_{W|X}(W\_{i}|X\_{i})—that maximizes the covariance with this fixed, structural outcome.

Our focus on the MPE as the key object for policy improvement also connects our work to a design-based literature on EWM. For instance, Viviano and Rudder ([2024](https://arxiv.org/html/2510.20032v1#bib.bib44)) propose an experimental design that uses “local perturbations” to treatment probabilities across large, independent clusters to directly estimate the MPE in settings with unknown, decentralized spillovers. Whereas their approach provides an experimental method for estimating the total welfare gradient, our complementary framework provides its structural decomposition in centralized markets.

To make this connection explicit, we analyze the canonical case of a binary policy, Wi∈{0,1}W\_{i}\in\{0,1\}. A targeted local reform is a marginal perturbation to the baseline propensity score, p​(Xi)=ℙ​(Wi=1|Xi)p(X\_{i})=\mathbb{P}(W\_{i}=1|X\_{i}), in a direction defined by a square-integrable function h​(Xi)h(X\_{i}). The score for such a reform is given by:666This score arises from a perturbation of the log-odds ratio, a standard way to ensure perturbed probabilities remain in (0,1)(0,1). Specifically, if the new log-odds is log⁡p​(Xi)1−p​(Xi)+θ​h​(Xi)\log\frac{p(X\_{i})}{1-p(X\_{i})}+\theta h(X\_{i}), the derivative of the log-likelihood with respect to θ\theta at θ=0\theta=0 yields this score.

|  |  |  |
| --- | --- | --- |
|  | sW|X​(Wi|Xi)=(Wip​(Xi)−1−Wi1−p​(Xi))​h​(Xi).s\_{W|X}(W\_{i}|X\_{i})=\left(\frac{W\_{i}}{p(X\_{i})}-\frac{1-W\_{i}}{1-p(X\_{i})}\right)h(X\_{i}). |  |

Substituting this score into the MPE formula and applying the law of iterated expectations yields:

|  |  |  |
| --- | --- | --- |
|  | 𝒰′​(sW|X)=𝔼0​[(𝔼0​[Ψitotal|Wi=1,Xi]−𝔼0​[Ψitotal|Wi=0,Xi])⋅h​(Xi)].\displaystyle\mathcal{U}^{\prime}(s\_{W|X})=\mathbb{E}\_{0}\left[\left(\mathbb{E}\_{0}[\Psi^{\text{total}}\_{i}|W\_{i}=1,X\_{i}]-\mathbb{E}\_{0}[\Psi^{\text{total}}\_{i}|W\_{i}=0,X\_{i}]\right)\cdot h(X\_{i})\right]. |  |

This result provides a clear recipe for policy design. The welfare gain from a local reform is the inner product of the Conditional Average Treatment Effect on the equilibrium-adjusted outcome (CATE-Ψ\Psi), defined as the term in parentheses, and the function h​(Xi)h(X\_{i}) that defines the reform’s direction. Unlike in the global EWM literature, where a policy rule maps covariates to probabilities, the function h​(Xi)h(X\_{i}) is unconstrained in sign. It represents the gradient of the reform; a negative value for a subpopulation simply implies that the welfare-improving direction is to locally reduce their probability of treatment.

The optimal local reform is the one that maximizes this welfare gain for a given budget or “size.” A natural choice is to constrain the variance of the perturbation, 𝔼​[h2​(Xi)]≤C\mathbb{E}[h^{2}(X\_{i})]\leq C. The problem of maximizing the MPE subject to this constraint is a standard Hilbert space projection problem, whose solution, by the Cauchy-Schwarz inequality, is to set h​(Xi)h(X\_{i}) proportional to the CATE-Ψ\Psi. This yields the optimal score:

|  |  |  |
| --- | --- | --- |
|  | sW|X⋆​(Wi|Xi)∝(Wip​(Xi)−1−Wi1−p​(Xi))​(𝔼0​[Ψitotal|Wi=1,Xi]−𝔼0​[Ψitotal|Wi=0,Xi]).s^{\star}\_{W|X}(W\_{i}|X\_{i})\propto\left(\frac{W\_{i}}{p(X\_{i})}-\frac{1-W\_{i}}{1-p(X\_{i})}\right)\left(\mathbb{E}\_{0}[\Psi^{\text{total}}\_{i}|W\_{i}=1,X\_{i}]-\mathbb{E}\_{0}[\Psi^{\text{total}}\_{i}|W\_{i}=0,X\_{i}]\right). |  |

This policy for local improvement differs fundamentally from the globally optimal rule derived in the EWM literature, which typically takes the form (Manski, [2004](https://arxiv.org/html/2510.20032v1#bib.bib32)):

|  |  |  |
| --- | --- | --- |
|  | sW|XEWM​(Wi|Xi)∝(Wip​(Xi)−1−Wi1−p​(Xi))​𝟏​{𝔼0​[Ψitotal|Wi=1,Xi]−𝔼0​[Ψitotal|Wi=0,Xi]≥0}.s^{\text{EWM}}\_{W|X}(W\_{i}|X\_{i})\propto\left(\frac{W\_{i}}{p(X\_{i})}-\frac{1-W\_{i}}{1-p(X\_{i})}\right)\mathbf{1}\left\{\mathbb{E}\_{0}[\Psi^{\text{total}}\_{i}|W\_{i}=1,X\_{i}]-\mathbb{E}\_{0}[\Psi^{\text{total}}\_{i}|W\_{i}=0,X\_{i}]\geq 0\right\}. |  |

Our approach identifies the most welfare-improving direction for a marginal reform from the current baseline, which leverages the magnitude of the CATE-Ψ\Psi. The EWM approach, in contrast, identifies the optimal policy level within a particular class of rules, which depends only on the sign of the CATE-Ψ\Psi.

###### Remark 5.1 (The Role of Covariates in Defining Reforms).

Our analysis of targeting has focused on using covariates XiX\_{i} to generate a rich space of policy reforms. This is particularly crucial for binary policies. When the policy instrument is binary (Wi∈{0,1}W\_{i}\in\{0,1\}), the space of valid scores is one-dimensional; any score must be proportional to Wi−𝔼0​[Wi]𝕍​[Wi]\frac{W\_{i}-\mathbb{E}\_{0}[W\_{i}]}{\mathbb{V}[W\_{i}]}. Without covariates, there is therefore only a single direction for local policy improvement. In contrast, a non-binary policy instrument, such as a continuous subsidy, naturally admits a high-dimensional space of reforms even without covariates. In that case, the score can be any function of the instrument, s​(Wi)s(W\_{i}), that is orthogonal to a constant (i.e., satisfies 𝔼​[s​(Wi)]=0\mathbb{E}[s(W\_{i})]=0). This allows for a wide variety of budgetary reallocations, such as increasing small subsidies while decreasing large ones.

### 5.3 Unobserved Heterogeneity and Endogenous Selection

We now consider a setting where the baseline choice WiW\_{i} is not assigned by a policymaker but is instead an endogenous decision made by each agent. In this context, it is less natural to think of a change in the distribution of WiW\_{i} as a directly implementable reform. Nevertheless, it remains economically valuable to quantify how aggregate welfare responds to shifts in the distribution of these choices. To conduct this analysis, we assume the presence of exogenous variation in the form of an instrumental variable (IV), denoted by ZiZ\_{i}. We focus on a binary choice, Wi∈{0,1}W\_{i}\in\{0,1\}, to simplify the exposition.

###### Assumption 5.2 (Instrumental Variable).

There exists an instrument ZiZ\_{i} for the binary choice WiW\_{i} that satisfies:

1. 1.

   Random Assignment: ZiZ\_{i} is independent of all potential outcomes and reports.
2. 2.

   Selection Model: Selection is governed by the latent variable model Wi=𝟏​{p​(Zi)>ξi}W\_{i}=\mathbf{1}\{p(Z\_{i})>\xi\_{i}\}, where ξi\xi\_{i} is uniform on [0,1][0,1] and independent of ZiZ\_{i}.
3. 3.

   Exclusion Restriction: The instrument ZiZ\_{i} does not directly enter the allocation mechanism, potential outcomes Yi​(w,a)Y\_{i}(w,a), or potential reports Ri​(w)R\_{i}(w).

This setup describes a conventional selection model in the spirit of Heckman ([1979](https://arxiv.org/html/2510.20032v1#bib.bib20)).777As shown by Vytlacil ([2002](https://arxiv.org/html/2510.20032v1#bib.bib45)), this latent variable formulation is equivalent to the monotonicity assumption in the LATE framework of Imbens and Angrist ([1994](https://arxiv.org/html/2510.20032v1#bib.bib25)). It opens two distinct avenues for policy analysis. The first is to treat the instrument ZiZ\_{i} itself as the policy lever. Since ZiZ\_{i} is randomly assigned, this case reduces to a direct application of our main result. In the context of Corollary [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmcorollary1 "Corollary 3.1 (The Equilibrium-Adjusted Outcome). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), the MPE with respect to a reform of the instrument’s distribution, characterized by a score sZs\_{Z}, is given by:

|  |  |  |
| --- | --- | --- |
|  | 𝒰′​(sZ)=𝔼0​[Ψitotal​sZ​(Zi)].\mathcal{U}^{\prime}(s\_{Z})=\mathbb{E}\_{0}[\Psi\_{i}^{\text{total}}s\_{Z}(Z\_{i})]. |  |

This is effectively an intention-to-treat (ITT) analysis using our equilibrium-adjusted outcome Ψitotal\Psi\_{i}^{\text{total}}. Critically, because the market mechanism does not respond directly to ZiZ\_{i}, this ITT-type result does not require the exclusion restriction (part 3 of Assumption [5.2](https://arxiv.org/html/2510.20032v1#S5.Thmassumption2 "Assumption 5.2 (Instrumental Variable). ‣ 5.3 Unobserved Heterogeneity and Endogenous Selection ‣ 5 Applications and Extensions ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")).

The second, more structural avenue uses the MTE framework to analyze policies that target the endogenous choice WiW\_{i} (Björklund and Moffitt, [1987](https://arxiv.org/html/2510.20032v1#bib.bib12); Heckman and Vytlacil, [2001](https://arxiv.org/html/2510.20032v1#bib.bib22), [2005](https://arxiv.org/html/2510.20032v1#bib.bib23)). For a binary instrument Zi∈{0,1}Z\_{i}\in\{0,1\}, it is natural to consider the Wald-type estimand for our welfare-relevant outcome:

|  |  |  |
| --- | --- | --- |
|  | 𝔼0​[Ψitotal|Zi=1]−𝔼0​[Ψitotal|Zi=0]𝔼0​[Wi|Zi=1]−𝔼0​[Wi|Zi=0]=Cov​(Ψitotal,Zi)Cov​(Wi,Zi).\frac{\mathbb{E}\_{0}[\Psi\_{i}^{\text{total}}|Z\_{i}=1]-\mathbb{E}\_{0}[\Psi\_{i}^{\text{total}}|Z\_{i}=0]}{\mathbb{E}\_{0}[W\_{i}|Z\_{i}=1]-\mathbb{E}\_{0}[W\_{i}|Z\_{i}=0]}=\frac{\text{Cov}(\Psi\_{i}^{\text{total}},Z\_{i})}{\text{Cov}(W\_{i},Z\_{i})}. |  |

A key result from the MTE literature is that this ratio identifies the average treatment effect for the subpopulation of “compliers”—those induced to change their choice by the instrument (Imbens and Angrist, [1994](https://arxiv.org/html/2510.20032v1#bib.bib25)). By applying this logic to our structural outcome Ψitotal\Psi\_{i}^{\text{total}}, we can show that this estimand is equal to the average MTE for the complier population:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[M​T​EΨtotal​(ξi)|p​(0)≤ξi≤p​(1)],whereM​T​EΨtotal​(ξ):=𝔼​[Ψitotal​(1)−Ψitotal​(0)|ξi=ξ].\mathbb{E}[MTE\_{\Psi^{\text{total}}}(\xi\_{i})|p(0)\leq\xi\_{i}\leq p(1)],\quad\text{where}\quad MTE\_{\Psi^{\text{total}}}(\xi):=\mathbb{E}[\Psi\_{i}^{\text{total}}(1)-\Psi\_{i}^{\text{total}}(0)|\xi\_{i}=\xi]. |  |

This representation is powerful because it establishes a direct link between an estimable quantity (the Wald ratio for Ψitotal\Psi\_{i}^{\text{total}}) and the MPE for a specific, economically meaningful policy. The policy is one that induces a uniform shift in the choice probability for the complier group, characterized by the score:

|  |  |  |
| --- | --- | --- |
|  | sW|ξ​(Wi|ξi)∝(Wiℙ​(Wi=1|ξi)−1−Wiℙ​(Wi=0|ξi))⋅𝟏​{p​(0)≤ξi≤p​(1)}.s\_{W|\xi}(W\_{i}|\xi\_{i})\propto\left(\frac{W\_{i}}{\mathbb{P}(W\_{i}=1|\xi\_{i})}-\frac{1-W\_{i}}{\mathbb{P}(W\_{i}=0|\xi\_{i})}\right)\cdot\mathbf{1}\{p(0)\leq\xi\_{i}\leq p(1)\}. |  |

This particular policy can be implemented by manipulating the distribution of the instrument ZiZ\_{i}. Whether such a manipulation is a practical policy or a purely theoretical benchmark depends on the nature of ZiZ\_{i} itself.

This logic extends directly to a discrete instrument with L+1L+1 support points, Zi∈{0,…,L}Z\_{i}\in\{0,\dots,L\}. In this case, we can identify the MPE for any policy that targets a linear combination of the LL complier groups (those with ξi∈[p​(l),p​(l+1)]\xi\_{i}\in[p(l),p(l+1)]). A policymaker can then choose the weights on these groups to find the optimal implementable local reform. To evaluate a broader class of policies—those that cannot be implemented by simply re-weighting the instrument—one must rely on additional assumptions to extrapolate the MTE curve beyond the identified regions. The literature provides extensive tools for such exercises, from parametric assumptions (Brinch et al., [2017](https://arxiv.org/html/2510.20032v1#bib.bib14)) to partial identification approaches (Mogstad et al., [2018](https://arxiv.org/html/2510.20032v1#bib.bib35)). In the latter case, the question of the optimal local reform is directly connected to a robust policy design under ambiguity (Manski, [2011](https://arxiv.org/html/2510.20032v1#bib.bib33)).

###### Remark 5.2 (Non-Binary Choices).

Our focus on a binary choice WiW\_{i} is for expositional simplicity. The core logic developed here extends to settings with non-binary choices, such as discrete or ordered choice models and non-ordered instruments. Although the MTE framework is most developed for the binary case, a growing literature provides the necessary tools for these richer settings. For a recent and comprehensive overview, see the Handbook chapter by Mogstad and Torgovitsky ([2024](https://arxiv.org/html/2510.20032v1#bib.bib36)).

### 5.4 Discussion: Strategic Reporting in Non-Strategy-Proof Mechanisms

Our analysis has so far assumed that an individual’s report to the mechanism is a stable function of the policy instrument. This is reasonable in strategy-proof environments, but many real-world markets are not. In such settings, rational individuals adapt their reports to the market environment. A policy that alters this environment will therefore induce a strategic response, adding a new channel through which welfare is affected.

##### A Framework for Strategic Reporting.

To analyze these settings, we distinguish between an agent’s latent “true” type, Ri⋆=Ri⋆​(Wi)R\_{i}^{\star}=R\_{i}^{\star}(W\_{i}), and their strategically chosen report, RiR\_{i}. The path to identification depends critically on the informational content of the observed reports. In some environments, such as a first-price auction, economic theory provides an invertible mapping from reports to types, allowing Ri⋆R\_{i}^{\star} to be point-identified for each agent (Guerre et al., [2000](https://arxiv.org/html/2510.20032v1#bib.bib19)). In such cases, our previous analysis applies directly to the recovered true types.

In more complex settings like matching markets, however, point-identification often fails. A potential way forward is to first recover the distribution of latent types in the baseline equilibrium, following methods like those in Agarwal and Somaini ([2018](https://arxiv.org/html/2510.20032v1#bib.bib5)). One can then model the strategic reporting strategy as a conditional distribution, fR|R⋆​(Ri|Ri⋆,PR⋆)f\_{R|R^{\star}}(R\_{i}|R\_{i}^{\star},P\_{R^{\star}}), which captures how submitted reports respond to the competitive environment (summarized by the distribution of true types, PR⋆P\_{R^{\star}}). A marginal policy reform now propagates through two channels: its direct effect on the distribution of true types, PR⋆P\_{R^{\star}}, and its indirect effect on reporting strategies. If the strategic response is smooth, we can linearize it, leading to a total score that is the sum of the baseline policy score and a new strategic-response score. The MPE from Corollary [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmcorollary1 "Corollary 3.1 (The Equilibrium-Adjusted Outcome). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") would then be:

|  |  |  |
| --- | --- | --- |
|  | 𝒰′​(sW)=𝔼0​[Ψitotal​(sW​(Wi)+sR|R⋆​(Ri|Ri⋆,sW))],\mathcal{U}^{\prime}(s\_{W})=\mathbb{E}\_{0}[\Psi\_{i}^{\text{total}}(s\_{W}(W\_{i})+s\_{R|R^{\star}}(R\_{i}|R\_{i}^{\star},s\_{W}))], |  |

where sR|R⋆s\_{R|R^{\star}} captures the strategic adjustment. Importantly, the structural object Ψitotal\Psi\_{i}^{\text{total}} remains invariant, as the market mechanism observes and responds only to the submitted reports RiR\_{i}, not the latent types.

##### Identification Challenges.

While this representation provides a theoretical path forward, identifying the MPE in practice faces at least two significant challenges. The first challenge concerns the market conduct externality, Ψconduct\Psi^{\text{conduct}}. Its identification relies on the continuity of conditional mean outcomes at the allocation margin. As Bertanha et al. ([2023](https://arxiv.org/html/2510.20032v1#bib.bib10)) show, this continuity can be violated in markets with strategic reporting. The intuition is that agents with knowledge of market cutoffs can strategically sort around them, invalidating the local comparisons underlying RDD-type estimands. Bertanha et al. ([2023](https://arxiv.org/html/2510.20032v1#bib.bib10)) propose a solution using partial identification, deriving bounds on the marginal causal effects. These could, in principle, be used to derive bounds for the MPE.

The second, more fundamental challenge involves the correlation between an agent’s outcome, YiY\_{i}, and their unobserved true type, Ri⋆R\_{i}^{\star}. Even if the joint distribution of (Ri,Ri⋆)(R\_{i},R\_{i}^{\star}) is identified, as in Agarwal and Somaini ([2018](https://arxiv.org/html/2510.20032v1#bib.bib5)), this is not sufficient to compute the expectation in the MPE formula. Doing so requires the joint distribution of (Yi,Ri,Ri⋆)(Y\_{i},R\_{i},R\_{i}^{\star}). The situation is analogous to a standard selection model, where RiR\_{i} is an observed choice and the latent type Ri⋆R\_{i}^{\star} is an unobserved state that may be correlated with the outcome YiY\_{i}, conditional on the choice. Extending methods from related problems, such as in Kline and Walters ([2016](https://arxiv.org/html/2510.20032v1#bib.bib29)), could offer a path forward, but would likely require non-trivial extrapolation and further assumptions. Thus, applying our framework in non-strategy-proof settings requires confronting deep identification problems, likely leading to partial identification of the MPE.

## 6 Conclusion

Evaluating policies in centralized markets is complicated by equilibrium spillovers, which standard methods often fail to capture. The conventional wisdom is that identifying these effects requires observing the system’s response to variation across different policy environments. This paper challenges that view by developing a framework to identify the total welfare effect of any marginal policy reform using data from within a single market. Our solution is the construction of the equilibrium-adjusted outcome (Ψitotal\Psi\_{i}^{\text{total}}), a policy-invariant structural object that augments an agent’s private outcome with the full equilibrium externalities they impose on others. A key insight of our approach is that the building blocks for this object’s externality terms are often precisely the Local Average Treatment Effects (LATEs) identified in the empirical Regression Discontinuity Design (RDD) literature. This construction yields a practical "separation principle," where the marginal policy effect is a simple covariance between the policy score and Ψitotal\Psi\_{i}^{\text{total}}.

This framework provides a toolkit with several applications. For policymakers, it offers a direct way to evaluate the "bang-for-the-buck" of the iterative, marginal policy changes that are common in practice. For researchers, it serves as a disciplined first step for analyzing global reforms. By sharply delineating what is identified non-parametrically from the data, our results provide a transparent foundation upon which any extrapolation required for global analysis must be built. More ambitious structural models can also be disciplined by requiring them to reproduce the identified local effects our framework provides. The framework’s flexibility is further demonstrated by its extensions to optimal policy targeting and its novel connection to the Marginal Treatment Effects (MTE) literature for analyzing endogenous choice. By bridging reduced-form empirical work with the equilibrium structure of the market, our results offer a path toward more robust, data-driven policy design in a wide array of important economic settings.

## References

* (1)
* Abdulkadiroğlu et al. (2017)

  Abdulkadiroğlu, Atila, Joshua D Angrist, Yusuke Narita, and
  Parag A Pathak. 2017. “Research design meets market design: Using
  centralized assignment for impact evaluation.” Econometrica 85 (5):
  1373–1432.
* Abdulkadiroğlu and Sönmez (2003)

  Abdulkadiroğlu, Atila, and Tayfun Sönmez. 2003. “School
  choice: A mechanism design approach.” American Economic Review 93
  (3): 729–747.
* Agarwal et al. (2025)

  Agarwal, Nikhil, Charles Hodgson, and Paulo Somaini. 2025. “Choices
  and outcomes in assignment mechanisms: The allocation of deceased donor
  kidneys.” Econometrica 93 (2): 395–438.
* Agarwal and Somaini (2018)

  Agarwal, Nikhil, and Paulo Somaini. 2018. “Demand analysis using
  strategic reports: An application to a school choice mechanism.”
  Econometrica 86 (2): 391–444.
* Allende (2019)

  Allende, Claudia. 2019. “Competition under social interactions and
  the design of education policies.” Job Market Paper.
* Artemov et al. (2023)

  Artemov, Georgy, Yeon-Koo Che, and YingHua He. 2023. “Stable matching
  with mistaken agents.” Journal of Political Economy Microeconomics
  1 (2): 270–320.
* Athey and Wager (2021)

  Athey, Susan, and Stefan Wager. 2021. “Policy learning with
  observational data.” Econometrica 89 (1): 133–161.
* Azevedo and Leshno (2016)

  Azevedo, Eduardo M, and Jacob D Leshno. 2016. “A supply and demand
  framework for two-sided matching markets.” Journal of Political
  Economy 124 (5): 1235–1268.
* Bertanha et al. (2023)

  Bertanha, Marinho, Margaux Luflade, and Ismael Mourifié. 2023.
  “Causal Effects in Matching Mechanisms with Strategically Reported
  Preferences.” arXiv preprint arXiv:2307.14282.
* Bertanha et al. (2024)

  Bertanha, Marinho, Margaux Luflade, and Ismael Mourifié. 2024.
  “Causal Effects in Matching Mechanisms with Strategically Reported
  Preferences.”Technical report, National Bureau of Economic Research.
* Björklund and Moffitt (1987)

  Björklund, Anders, and Robert Moffitt. 1987. “The estimation of
  wage gains and welfare gains in self-selection models.” The Review
  of Economics and Statistics 42–49.
* Bojinov et al. (2023)

  Bojinov, Iavor, David Simchi-Levi, and Jinglong Zhao. 2023. “Design
  and analysis of switchback experiments.” Management Science 69 (7):
  3759–3777.
* Brinch et al. (2017)

  Brinch, Christian N, Magne Mogstad, and Matthew Wiswall. 2017.
  “Beyond LATE with a discrete instrument.” Journal of Political
  Economy 125 (4): 985–1039.
* Chetty (2009)

  Chetty, Raj. 2009. “Sufficient statistics for welfare analysis: A
  bridge between structural and reduced-form methods.” Annu. Rev.
  Econ. 1 (1): 451–488.
* Crépon et al. (2013)

  Crépon, Bruno, Esther Duflo, Marc Gurgand, Roland Rathelot, and
  Philippe Zamora. 2013. “Do labor market policies have displacement effects?
  Evidence from a clustered randomized experiment.” The Quarterly
  Journal of Economics 128 (2): 531–580.
* Delfour and Zolésio (2011)

  Delfour, Michel C, and J-P Zolésio. 2011. Shapes and
  geometries: metrics, analysis, differential calculus, and optimization.
  SIAM.
* Fack et al. (2019)

  Fack, Gabrielle, Julien Grenet, and Yinghua He. 2019. “Beyond
  truth-telling: Preference estimation with centralized school choice and
  college admissions.” American Economic Review 109 (4):
  1486–1529.
* Guerre et al. (2000)

  Guerre, Emmanuel, Isabelle Perrigne, and Quang Vuong. 2000. “Optimal
  nonparametric estimation of first-price auctions.” Econometrica 68
  (3): 525–574.
* Heckman (1979)

  Heckman, James J. 1979. “Sample selection bias as a specification
  error.” Econometrica: Journal of the Econometric Society 153–161.
* Heckman et al. (1998)

  Heckman, James J, Lance Lochner, and Christopher R Taber. 1998.
  “General equilibrium treatment effects: A study of tuition policy.”
  American Economic Review 88 (2): 381–386.
* Heckman and Vytlacil (2001)

  Heckman, James J, and Edward Vytlacil. 2001. “Policy-relevant
  treatment effects.” American Economic Review 91 (2): 107–111.
* Heckman and Vytlacil (2005)

  Heckman, James J, and Edward Vytlacil. 2005. “Structural equations,
  treatment effects, and econometric policy evaluation 1.”
  Econometrica 73 (3): 669–738.
* Hu et al. (2022)

  Hu, Yuchen, Shuangning Li, and Stefan Wager. 2022. “Average direct
  and indirect causal effects under interference.” Biometrika 109
  (4): 1165–1172.
* Imbens and Angrist (1994)

  Imbens, Guido W, and Joshua D Angrist. 1994. “Identification and
  Estimation of Local Average Treatment Effects.” Econometrica 62
  (2): 467–475.
* Kirkeboen et al. (2016)

  Kirkeboen, Lars J, Edwin Leuven, and Magne Mogstad. 2016. “Field of
  study, earnings, and self-selection.” The Quarterly Journal of
  Economics 131 (3): 1057–1111.
* Kitagawa and Tetenov (2018)

  Kitagawa, Toru, and Aleksey Tetenov. 2018. “Who should be treated?
  empirical welfare maximization methods for treatment choice.”
  Econometrica 86 (2): 591–616.
* Kleven (2021)

  Kleven, Henrik J. 2021. “Sufficient statistics revisited.”
  Annual Review of Economics 13 (1): 515–538.
* Kline and Walters (2016)

  Kline, Patrick, and Christopher R Walters. 2016. “Evaluating public
  programs with close substitutes: The case of Head Start.” The
  Quarterly Journal of Economics 131 (4): 1795–1848.
* Leshno (2022)

  Leshno, Jacob. 2022. “Stable matching with peer-dependent preferences
  in large markets: Existence and cutoff characterization.” Available
  at SSRN 3822060.
* Leshno and Lo (2021)

  Leshno, Jacob D, and Irene Lo. 2021. “The cutoff structure of top
  trading cycles in school choice.” The Review of Economic Studies 88
  (4): 1582–1623.
* Manski (2004)

  Manski, Charles F. 2004. “Statistical treatment rules for
  heterogeneous populations.” Econometrica 72 (4): 1221–1246.
* Manski (2011)

  Manski, Charles F. 2011. “Choosing treatment policies under
  ambiguity.” Annual Review of Economics 3 (1): 25–49.
* Menzel (2025)

  Menzel, Konrad. 2025. “Fixed-Population Causal Inference for Models
  of Equilibrium.” arXiv preprint arXiv:2501.19394.
* Mogstad et al. (2018)

  Mogstad, Magne, Andres Santos, and Alexander Torgovitsky. 2018.
  “Using instrumental variables for inference about policy relevant treatment
  parameters.” Econometrica 86 (5): 1589–1619.
* Mogstad and Torgovitsky (2024)

  Mogstad, Magne, and Alexander Torgovitsky. 2024. “Instrumental
  variables with unobserved heterogeneity in treatment effects.” In
  Handbook of Labor Economics, Volume 5. 1–114, Elsevier.
* Munro (2025)

  Munro, Evan. 2025. “Causal Inference under Interference through
  Designed Markets.” arXiv preprint arXiv:2011.08174.
* Munro et al. (2025)

  Munro, Evan, Xu Kuang, and Stefan Wager. 2025. “Treatment effects in
  market equilibrium.” American Economic Review 115 (10):
  3273–3321.
* Myerson (1981)

  Myerson, Roger B. 1981. “Optimal auction design.”
  Mathematics of operations research 6 (1): 58–73.
* Narita and Yata (2023)

  Narita, Yusuke, and Kohei Yata. 2023. “Algorithm as experiment:
  machine learning, market design, and policy eligibility rules.”
  arXiv preprint arXiv:2104.12909.
* Shapley and Scarf (1974)

  Shapley, Lloyd, and Herbert Scarf. 1974. “On cores and
  indivisibility.” Journal of Mathematical Economics 1 (1): 23–37.
* Van der Vaart (2000)

  Van der Vaart, Aad W. 2000. Asymptotic statistics. Volume 3.
  Cambridge university press.
* Van Der Vaart (1991)

  Van Der Vaart, Aad. 1991. “On differentiable functionals.”
  The Annals of Statistics 178–204.
* Viviano and Rudder (2024)

  Viviano, Davide, and Jess Rudder. 2024. “Policy design in experiments
  with unknown interference.” arXiv preprint arXiv:2011.08174 4.
* Vytlacil (2002)

  Vytlacil, Edward. 2002. “Independence, monotonicity, and latent index
  models: An equivalence result.” Econometrica 70 (1): 331–341.
* Wager and Xu (2021)

  Wager, Stefan, and Kuang Xu. 2021. “Experimenting in equilibrium.”
  Management Science 67 (11): 6694–6715.
* Walters (2018)

  Walters, Christopher R. 2018. “The demand for effective charter
  schools.” Journal of Political Economy 126 (6): 2179–2223.
* Wolf (2023)

  Wolf, Christian K. 2023. “The missing intercept: A demand equivalence
  approach.” American Economic Review 113 (8): 2232–2269.

Online Appendix

## Appendix A Differentiating integrals

Let XX be a random variable on ℝk\mathbb{R}^{k} with a probability density function p​(x)p(x). Let I⊂ℝpI\subset\mathbb{R}^{p} be an open set of parameters. We are interested in the differentiability of the functional 𝒰:I→ℝ\mathcal{U}:I\to\mathbb{R} defined as:

|  |  |  |
| --- | --- | --- |
|  | 𝒰​(𝐜)=𝔼​[h​(X,𝐜)​𝟏​{ϕ​(X,𝐜)≥0}]=∫ℝkh​(x,𝐜)​p​(x)​𝟏​{ϕ​(x,𝐜)≥0}​𝑑x\displaystyle\mathcal{U}(\mathbf{c})=\mathbb{E}[h(X,\mathbf{c})\mathbf{1}\{\phi(X,\mathbf{c})\geq 0\}]=\int\_{\mathbb{R}^{k}}h(x,\mathbf{c})p(x)\mathbf{1}\{\phi(x,\mathbf{c})\geq 0\}\,dx |  |

This functional is central to our analysis, representing the aggregate welfare where h​(x,𝐜)h(x,\mathbf{c}) is an agent’s outcome and the indicator function reflects an eligibility rule determined by market-clearing parameters 𝐜\mathbf{c}.

###### Assumption A.1.

The functions h​(x,𝐜)h(x,\mathbf{c}), p​(x)p(x), and ϕ​(x,𝐜)\phi(x,\mathbf{c}) satisfy the following conditions:

1. 1.

   Integrability: The density p​(x)p(x) is bounded and continuous; the function x↦h​(x,𝐜0)x\mapsto h(x,\mathbf{c}\_{0}) is integrable.
2. 2.

   Differentiability: For almost every x∈ℝkx\in\mathbb{R}^{k} function 𝐜↦h​(x,𝐜)\mathbf{c}\mapsto h(x,\mathbf{c}) is differentiable in the neighbourhood of 𝐜0\mathbf{c}\_{0} and its derivative is uniformly bounded by some integrable function Kh​(x)K\_{h}(x).
3. 3.

   Continuity: Function h​(x,𝐜0)​p​(x)h(x,\mathbf{c}\_{0})p(x) is continuous in the open neighbourhood of {x|ϕ​(x,𝐜0)=0}\{x|\phi(x,\mathbf{c}\_{0})=0\}.
4. 4.

   Boundary Non-degeneracy: Function (x,𝐜)↦ϕ​(x,𝐜)(x,\mathbf{c})\mapsto\phi(x,\mathbf{c}) is Lipschitz continuous and ‖∇xϕ​(x,𝐜0)‖2>ϵ>0\|\nabla\_{x}\phi(x,\mathbf{c}\_{0})\|\_{2}>\epsilon>0 ℋk−1\mathcal{H}^{k-1}-a.s. on the boundary surface {ϕ​(x,𝐜0)=0}\{\phi(x,\mathbf{c}\_{0})=0\}.

###### Theorem A.1.

Under Assumption [A.1](https://arxiv.org/html/2510.20032v1#A1.Thmassumption1 "Assumption A.1. ‣ Appendix A Differentiating integrals ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), the functional 𝒰​(𝐜)\mathcal{U}(\mathbf{c}) is differentiable at 𝐜0∈I\mathbf{c}\_{0}\in I. Its partial derivative with respect to cjc\_{j} is given by:

|  |  |  |
| --- | --- | --- |
|  | ∂𝒰∂cj​(𝐜0)=∫ℝk∂h​(x,𝐜0)∂cj​p​(x)​𝟏​{ϕ​(x,𝐜0)≥0}​𝑑x+∫{x|ϕ​(x,𝐜0)=0}h​(x,𝐜0)​p​(x)​∂ϕ​(x,𝐜0)/∂cj‖∇xϕ​(x,𝐜0)‖2​𝑑ℋk−1​(x)\displaystyle\frac{\partial\mathcal{U}}{\partial c\_{j}}(\mathbf{c}\_{0})=\int\_{\mathbb{R}^{k}}\frac{\partial h(x,\mathbf{c}\_{0})}{\partial c\_{j}}p(x)\mathbf{1}\{\phi(x,\mathbf{c}\_{0})\geq 0\}\,dx+\int\_{\{x\,|\,\phi(x,\mathbf{c}\_{0})=0\}}h(x,\mathbf{c}\_{0})p(x)\frac{\partial\phi(x,\mathbf{c}\_{0})/\partial c\_{j}}{\|\nabla\_{x}\phi(x,\mathbf{c}\_{0})\|\_{2}}d\mathcal{H}^{k-1}(x) |  |

where ℋk−1\mathcal{H}^{k-1} is the (k−1)(k-1)-dimensional Hausdorff measure.

###### Proof.

The proof proceeds by analyzing the limit of the difference quotient for 𝒰​(𝐜)\mathcal{U}(\mathbf{c}) at 𝐜0\mathbf{c}\_{0}. Let 𝐞j\mathbf{e}\_{j} be the jj-th standard basis vector in ℝp\mathbb{R}^{p}. The partial derivative is the limit:

|  |  |  |
| --- | --- | --- |
|  | ∂𝒰∂cj​(𝐜0)=limt→0𝒰​(𝐜0+t​𝐞j)−𝒰​(𝐜0)t\displaystyle\frac{\partial\mathcal{U}}{\partial c\_{j}}(\mathbf{c}\_{0})=\lim\_{t\to 0}\frac{\mathcal{U}(\mathbf{c}\_{0}+t\mathbf{e}\_{j})-\mathcal{U}(\mathbf{c}\_{0})}{t} |  |

Let g​(x,𝐜)=h​(x,𝐜)​p​(x)g(x,\mathbf{c})=h(x,\mathbf{c})p(x) and let H​(z)=𝟏​{z≥0}H(z)=\mathbf{1}\{z\geq 0\} be the Heaviside step function. The difference quotient can be written as:

|  |  |  |
| --- | --- | --- |
|  | 1t​∫ℝk[g​(x,𝐜0+t​𝐞j)​H​(ϕ​(x,𝐜0+t​𝐞j))−g​(x,𝐜0)​H​(ϕ​(x,𝐜0))]​𝑑x\displaystyle\frac{1}{t}\int\_{\mathbb{R}^{k}}\left[g(x,\mathbf{c}\_{0}+t\mathbf{e}\_{j})H(\phi(x,\mathbf{c}\_{0}+t\mathbf{e}\_{j}))-g(x,\mathbf{c}\_{0})H(\phi(x,\mathbf{c}\_{0}))\right]\,dx |  |

We add and subtract g​(x,𝐜0)​H​(ϕ​(x,𝐜0+t​𝐞j))g(x,\mathbf{c}\_{0})H(\phi(x,\mathbf{c}\_{0}+t\mathbf{e}\_{j})) inside the brackets to separate the expression into two parts:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Term 1: | ∫ℝkg​(x,𝐜0+t​𝐞j)−g​(x,𝐜0)t​H​(ϕ​(x,𝐜0+t​𝐞j))​𝑑x\displaystyle\int\_{\mathbb{R}^{k}}\frac{g(x,\mathbf{c}\_{0}+t\mathbf{e}\_{j})-g(x,\mathbf{c}\_{0})}{t}H(\phi(x,\mathbf{c}\_{0}+t\mathbf{e}\_{j}))\,dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Term 2: | ∫ℝkg​(x,𝐜0)​H​(ϕ​(x,𝐜0+t​𝐞j))−H​(ϕ​(x,𝐜0))t​𝑑x\displaystyle\int\_{\mathbb{R}^{k}}g(x,\mathbf{c}\_{0})\frac{H(\phi(x,\mathbf{c}\_{0}+t\mathbf{e}\_{j}))-H(\phi(x,\mathbf{c}\_{0}))}{t}\,dx |  |

For the first term, by the Mean Value Theorem, the integrand is equal to ∂g​(x,𝐜~)∂cj\frac{\partial g(x,\tilde{\mathbf{c}})}{\partial c\_{j}} for some 𝐜~\tilde{\mathbf{c}} on the line segment between 𝐜0\mathbf{c}\_{0} and 𝐜0+t​𝐞j\mathbf{c}\_{0}+t\mathbf{e}\_{j}. By Assumption [A.1](https://arxiv.org/html/2510.20032v1#A1.Thmassumption1 "Assumption A.1. ‣ Appendix A Differentiating integrals ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")(2), this is bounded in absolute value by the integrable function Kh​(x)​p​(x)K\_{h}(x)p(x). Therefore, the Dominated Convergence Theorem applies, and Term 1 converges to:

|  |  |  |
| --- | --- | --- |
|  | ∫ℝk∂h​(x,𝐜0)∂cj​p​(x)​𝟏​{ϕ​(x,𝐜0)≥0}​𝑑x\displaystyle\int\_{\mathbb{R}^{k}}\frac{\partial h(x,\mathbf{c}\_{0})}{\partial c\_{j}}p(x)\mathbf{1}\{\phi(x,\mathbf{c}\_{0})\geq 0\}\,dx |  |

The second term is the derivative of a function 𝐜↦∫{x|ϕ​(x,𝐜)≥0}h​(x,𝐜0)​p​(x)​𝑑x\mathbf{c}\mapsto\int\_{\{x|\phi(x,\mathbf{c})\geq 0\}}h(x,\mathbf{c}\_{0})p(x)dx. We appeal to the theory of shape derivatives to evaluate this. The conditions in Assumption [A.1](https://arxiv.org/html/2510.20032v1#A1.Thmassumption1 "Assumption A.1. ‣ Appendix A Differentiating integrals ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") are sufficient to apply Theorem 4.2 in Delfour and Zolésio ([2011](https://arxiv.org/html/2510.20032v1#bib.bib17)), which guarantees that the derivative exists and is equal to:

|  |  |  |
| --- | --- | --- |
|  | ∫{x|ϕ​(x,𝐜0)=0}h​(x,𝐜0)​p​(x)​∂ϕ​(x,𝐜0)/∂cj‖∇xϕ​(x,𝐜0)‖2​𝑑ℋk−1​(x),\displaystyle\int\_{\{x\,|\,\phi(x,\mathbf{c}\_{0})=0\}}h(x,\mathbf{c}\_{0})p(x)\frac{\partial\phi(x,\mathbf{c}\_{0})/\partial c\_{j}}{\|\nabla\_{x}\phi(x,\mathbf{c}\_{0})\|\_{2}}d\mathcal{H}^{k-1}(x), |  |

thus proving the result.
∎

###### Corollary A.1.

Let X=(Y,Z)X=(Y,Z), where Y∈ℝk1,Z∈ℝk2Y\in\mathbb{R}^{k\_{1}},Z\in\mathbb{R}^{k\_{2}}. Consider 𝒰​(𝐜)=𝔼​[h​(Y,Z,𝐜)​𝟏​{ϕ​(Y,Z,𝐜)≥0}]\mathcal{U}(\mathbf{c})=\mathbb{E}[h(Y,Z,\mathbf{c})\mathbf{1}\{\phi(Y,Z,\mathbf{c})\geq 0\}]. Suppose for PZP\_{Z}-almost every zz, the assumptions of Theorem [A.1](https://arxiv.org/html/2510.20032v1#A1.Thmtheorem1 "Theorem A.1. ‣ Appendix A Differentiating integrals ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") hold for the conditional expectation over YY. Let gj​(𝐜|z)g\_{j}(\mathbf{c}|z) be the resulting conditional derivative. If |gj(𝐜|z)||g\_{j}(\mathbf{c}|z)| is dominated by an integrable function K​(z)K(z), then 𝒰​(𝐜)\mathcal{U}(\mathbf{c}) is differentiable and

|  |  |  |
| --- | --- | --- |
|  | ∂𝒰​(𝐜)∂𝐜j=𝔼Z​[gj​(𝐜|Z)].\displaystyle\frac{\partial\mathcal{U}(\mathbf{c})}{\partial\mathbf{c}\_{j}}=\mathbb{E}\_{Z}[g\_{j}(\mathbf{c}|Z)]. |  |

###### Proof.

By the law of total expectation, 𝒰​(𝐜)=𝔼Z​[𝒰​(𝐜|Z)]\mathcal{U}(\mathbf{c})=\mathbb{E}\_{Z}[\mathcal{U}(\mathbf{c}|Z)]. For a.e. zz, 𝒰​(𝐜|z)\mathcal{U}(\mathbf{c}|z) is differentiable with derivative gj​(𝐜|z)g\_{j}(\mathbf{c}|z) by Theorem [A.1](https://arxiv.org/html/2510.20032v1#A1.Thmtheorem1 "Theorem A.1. ‣ Appendix A Differentiating integrals ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."). The domination condition allows us to apply the Differentiated DCT to interchange the derivative and the outer expectation 𝔼Z​[⋅]\mathbb{E}\_{Z}[\cdot].
∎

## Appendix B Derivation of the Marginal Policy Effect

This appendix provides a formal derivation of the Marginal Policy Effect (MPE) discussed in Section [3](https://arxiv.org/html/2510.20032v1#S3 "3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") of the main text. We first state the rigorous versions of the assumptions used in the derivation. We then prove a sequence of lemmas and propositions that decompose the MPE into its constituent parts: a direct effect, a competition effect, and a market conduct effect. The proof relies on the result for differentiating integrals over moving domains from Appendix [A](https://arxiv.org/html/2510.20032v1#A1 "Appendix A Differentiating integrals ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.").

Let the space of observable data for an agent be 𝒟:=𝒴×𝒜×ℛ×𝒲\mathcal{D}:=\mathcal{Y}\times\mathcal{A}\times\mathcal{R}\times\mathcal{W}. We assume the baseline policy regime is characterized by a probability measure on 𝒟\mathcal{D} that has a density with respect to a product measure λ\lambda. This density can be factorized as:

|  |  |  |
| --- | --- | --- |
|  | fY|A,W,R​(y|a,w,r)​μa​(r,𝐜0,PR|0)​fR|W​(r|w)​fW|0​(w),\displaystyle f\_{Y|A,W,R}(y|a,w,r)\mu\_{a}(r,\mathbf{c}\_{0},P\_{R|0})f\_{R|W}(r|w)f\_{W|0}(w), |  |

where 𝐜0\mathbf{c}\_{0} is the equilibrium parameter vector and PR|0P\_{R|0} is the marginal measure on the report space ℛ\mathcal{R}, induced by the baseline policy fW|0f\_{W|0}. Its density is fR|0​(r)=∫fR|W​(r|w)​fW|0​(w)​𝑑wf\_{R|0}(r)=\int f\_{R|W}(r|w)f\_{W|0}(w)dw. We use 𝔼0\mathbb{E}\_{0} to denote the expectation with respect to this baseline measure.

A marginal policy reform is a perturbation of the baseline policy distribution fW|0f\_{W|0} in a specific direction. We characterize these directions by a set of score functions.

###### Definition 1 (Policy Score Space).

The space of admissible policy scores, 𝒮W\mathcal{S}\_{W}, is the set of functions sW:𝒲→ℝs\_{W}:\mathcal{W}\to\mathbb{R} such that 𝔼0​[sW​(Wi)]=0\mathbb{E}\_{0}[s\_{W}(W\_{i})]=0 and 𝔼0​[sW2​(Wi)]<∞\mathbb{E}\_{0}[s^{2}\_{W}(W\_{i})]<\infty.

For any given score sW∈𝒮Ws\_{W}\in\mathcal{S}\_{W}, we can construct a local path of policy distributions indexed by a parameter θ∈ℝ\theta\in\mathbb{R}. A standard construction that accommodates all scores in 𝒮W\mathcal{S}\_{W} is the linear path:

|  |  |  |
| --- | --- | --- |
|  | fW​(w|θ,sW)=fW|0​(w)​(1+θ​sW​(w))\displaystyle f\_{W}(w|\theta,s\_{W})=f\_{W|0}(w)(1+\theta s\_{W}(w)) |  |

This path is well-defined for θ\theta in a neighborhood of 0. It satisfies fW​(w|0,sW)=fW|0​(w)f\_{W}(w|0,s\_{W})=f\_{W|0}(w) and guarantees that the score of the log-likelihood with respect to θ\theta at θ=0\theta=0 is precisely sW​(w)s\_{W}(w):

|  |  |  |
| --- | --- | --- |
|  | ∂∂θ​log⁡fW​(w|θ,sW)|θ=0=fW|0​(w)​sW​(w)fW|0​(w)=sW​(w).\displaystyle\frac{\partial}{\partial\theta}\log f\_{W}(w|\theta,s\_{W})\bigg|\_{\theta=0}=\frac{f\_{W|0}(w)s\_{W}(w)}{f\_{W|0}(w)}=s\_{W}(w). |  |

A reform to the policy distribution fWf\_{W} induces a change in the marginal distribution of reports fRf\_{R}. The perturbed report density is given by:

|  |  |  |
| --- | --- | --- |
|  | fR​(r|θ,sW)=∫fR|W​(r|w)​fW​(w|θ,sW)​𝑑w.\displaystyle f\_{R}(r|\theta,s\_{W})=\int f\_{R|W}(r|w)f\_{W}(w|\theta,s\_{W})dw. |  |

This perturbation of the report distribution also has a well-defined score, sR​(r)s\_{R}(r), which is characterized by the following result.

###### Lemma B.1 (Induced Score).

The score of the induced report distribution, sR​(r)=∂∂θ​log⁡fR​(r|θ,sW)|θ=0s\_{R}(r)=\frac{\partial}{\partial\theta}\log f\_{R}(r|\theta,s\_{W})|\_{\theta=0}, is the conditional expectation of the policy score:

|  |  |  |
| --- | --- | --- |
|  | sR​(r)=𝔼0​[sW​(Wi)|Ri=r].\displaystyle s\_{R}(r)=\mathbb{E}\_{0}[s\_{W}(W\_{i})|R\_{i}=r]. |  |

We use 𝒮R\mathcal{S}\_{R} to denote the set of scores sR​(Ri)s\_{R}(R\_{i}) induced by 𝒮W\mathcal{S}\_{W}.

###### Proof.

By definition, sR​(r)=fR′​(r|0)/fR|0​(r)s\_{R}(r)=f\_{R}^{\prime}(r|0)/f\_{R|0}(r), where the prime denotes the partial derivative with respect to θ\theta at θ=0\theta=0. We have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fR′​(r|0)\displaystyle f\_{R}^{\prime}(r|0) | =∫fR|W​(r|w)​fW′​(w|0)​𝑑w\displaystyle=\int f\_{R|W}(r|w)f\_{W}^{\prime}(w|0)dw |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫fR|W​(r|w)​[sW​(w)​fW|0​(w)]​𝑑w\displaystyle=\int f\_{R|W}(r|w)[s\_{W}(w)f\_{W|0}(w)]dw |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫fR|W​(r|w)​fW|0​(w)fR|0​(r)​sW​(w)​fR|0​(r)​𝑑w\displaystyle=\int\frac{f\_{R|W}(r|w)f\_{W|0}(w)}{f\_{R|0}(r)}s\_{W}(w)f\_{R|0}(r)dw |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =fR|0​(r)​∫fW|R​(w|r)​sW​(w)​𝑑w=fR|0​(r)​𝔼0​[sW​(Wi)|Ri=r].\displaystyle=f\_{R|0}(r)\int f\_{W|R}(w|r)s\_{W}(w)dw=f\_{R|0}(r)\mathbb{E}\_{0}[s\_{W}(W\_{i})|R\_{i}=r]. |  |

Here the differentiation under the integral is justified because fW​(w|θ,sW)f\_{W}(w|\theta,s\_{W}) is linear in θ\theta and the DCT can be applied because 𝔼0​[sW2​(Wi)]<∞\mathbb{E}\_{0}[s^{2}\_{W}(W\_{i})]<\infty. Dividing by fR|0​(r)f\_{R|0}(r) yields the result.
∎

###### Assumption B.1 (Marginal Agent Regularity).

For each a∈𝒜a\in\mathcal{A} define ma​(r):=𝔼0​[Yi​(Wi,a)|Ri=r]m\_{a}(r):=\mathbb{E}\_{0}[Y\_{i}(W\_{i},a)|R\_{i}=r]; we assume

1. 1.

   Report Structure: The report vector can be decomposed as Ri=(Ri,u​n,Ri,c​o​n​t)R\_{i}=(R\_{i,un},R\_{i,cont}), where, conditional on Ri,u​nR\_{i,un}, the distribution of Ri,c​o​n​tR\_{i,cont} is absolutely continuous with respect to the Lebesgue measure on ℝk\mathbb{R}^{k} with a bounded and continuous density function.
2. 2.

   Continuity of Conditional Outcomes: For each allocation a∈𝒜a\in\mathcal{A} and fixed ru​nr\_{un}, the conditional mean function rc​o​n​t↦ma​(ru​n,rc​o​n​t)r\_{cont}\mapsto m\_{a}(r\_{un},r\_{cont}) is continuous and bounded.

###### Assumption B.2 (Well-Behaved Mechanism).

For any a∈𝒜a\in\mathcal{A} the allocation probability, μa​(r,𝐜,PR)\mu\_{a}(r,\mathbf{c},P\_{R}), can be decomposed as:

|  |  |  |
| --- | --- | --- |
|  | μa​(r,𝐜,PR)=ha​(r,𝐜,PR)⋅𝟏​{ϕa​(r,𝐜)≥0}\displaystyle\mu\_{a}(r,\mathbf{c},P\_{R})=h\_{a}(r,\mathbf{c},P\_{R})\cdot\mathbf{1}\{\phi\_{a}(r,\mathbf{c})\geq 0\} |  |

where the components satisfy the following conditions at the baseline equilibrium (𝐜0,PR|0)(\mathbf{c}\_{0},P\_{R|0}):

1. 1.

   PRu​n|0P\_{R\_{u}n|0}-a.s. the functions (rc​o​n​t,𝐜)↦ϕa​(ru​n,rc​o​n​t,𝐜)(r\_{cont},\mathbf{c})\mapsto\phi\_{a}(r\_{un},r\_{cont},\mathbf{c}), (rc​o​n​t,𝐜)↦ha​(ru​n,rc​o​n​t,𝐜,PR|0)(r\_{cont},\mathbf{c})\mapsto h\_{a}(r\_{un},r\_{cont},\mathbf{c},P\_{R|0}) satisfy the conditions laid out in Assumption [A.1](https://arxiv.org/html/2510.20032v1#A1.Thmassumption1 "Assumption A.1. ‣ Appendix A Differentiating integrals ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") of Appendix [A](https://arxiv.org/html/2510.20032v1#A1 "Appendix A Differentiating integrals ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.").
2. 2.

   PR|0P\_{R|0}-a.s. the function (𝐜,PR)↦ha​(r,𝐜,PR)(\mathbf{c},P\_{R})\mapsto h\_{a}(r,\mathbf{c},P\_{R}) is Hadamard differentiable with respect to PRP\_{R} at PR|0P\_{R|0} for paths induced by scores sR∈𝒮Rs\_{R}\in\mathcal{S}\_{R}. Its derivative in the direction sRs\_{R} is a continuous linear functional given by:

   |  |  |  |
   | --- | --- | --- |
   |  | DP​ha​(r,𝐜,PR|0)​[sR]=∫La,𝐜​(r,r′)​sR​(r′)​𝑑r′\displaystyle D\_{P}h\_{a}(r,\mathbf{c},P\_{R|0})[s\_{R}]=\int L\_{a,\mathbf{c}}(r,r^{\prime})s\_{R}(r^{\prime})dr^{\prime} |  |

   where La,𝐜​(r,r′)L\_{a,\mathbf{c}}(r,r^{\prime}) is the square-integrable kernel and the mapping 𝐜↦La,𝐜​(r,r′)\mathbf{c}\mapsto L\_{a,\mathbf{c}}(r,r^{\prime}) is continuous at 𝐜0\mathbf{c}\_{0}.

###### Assumption B.3 (Differentiability of the Market Conduct Rule).

The market conduct rule 𝐜​(PR)\mathbf{c}(P\_{R}) is Hadamard differentiable at the baseline report distribution PR|0P\_{R|0} along the paths induced by scores sRs\_{R}. Its derivative, a continuous linear operator from the space of scores to ℝp\mathbb{R}^{p}, has the representation:

|  |  |  |
| --- | --- | --- |
|  | 𝐜′​[sR]=⟨𝝍c0,sR⟩ℋR\displaystyle\mathbf{c}^{\prime}[s\_{R}]=\langle\bm{\psi}\_{c\_{0}},s\_{R}\rangle\_{\mathcal{H}\_{R}} |  |

where ⟨⋅,⋅⟩ℋR\langle\cdot,\cdot\rangle\_{\mathcal{H}\_{R}} is the inner product on a Hilbert space ℋR\mathcal{H}\_{R} containing the scores, and 𝛙c0\bm{\psi}\_{c\_{0}} is the representer of the derivative.

We will split the proof of Theorem [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmtheorem1 "Theorem 3.1 (The Marginal Policy Effect). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") and Corollary [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmcorollary1 "Corollary 3.1 (The Equilibrium-Adjusted Outcome). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") into Lemmas [B.2](https://arxiv.org/html/2510.20032v1#A2.Thmlemma2 "Lemma B.2 (The Direct Effect). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")-[B.5](https://arxiv.org/html/2510.20032v1#A2.Thmlemma5 "Lemma B.5 (Identification). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."). The final result follows from the direct combination of the intermediate results.

###### Lemma B.2 (The Direct Effect).

Suppose Assumption [B.1](https://arxiv.org/html/2510.20032v1#A2.Thmassumption1 "Assumption B.1 (Marginal Agent Regularity). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") holds.
The direct effect of a policy reform, defined as the welfare impact of perturbing the policy distribution while holding the allocation rule fixed at the baseline (𝐜0,PR|0)(\mathbf{c}\_{0},P\_{R|0}), is given by 𝔼0​[Yi​sW​(Wi)]\mathbb{E}\_{0}[Y\_{i}s\_{W}(W\_{i})].

###### Proof.

The welfare functional for the direct effect is

|  |  |  |
| --- | --- | --- |
|  | 𝒰direct​(θ):=∫y​fY|A,W,R​μa​(r,𝐜0,PR|0)​fR|W​fW​(w|θ,sW)​𝑑λ.\displaystyle\mathcal{U}\_{\text{direct}}(\theta):=\int yf\_{Y|A,W,R}\mu\_{a}(r,\mathbf{c}\_{0},P\_{R|0})f\_{R|W}f\_{W}(w|\theta,s\_{W})d\lambda. |  |

Since μa\mu\_{a} is held fixed, this is a standard expectation. The score of the density of the data with respect to θ\theta is simply sW​(w)s\_{W}(w). The derivative of the expectation is the expectation of the outcome multiplied by the score, which gives 𝔼0​[Yi​sW​(Wi)]\mathbb{E}\_{0}[Y\_{i}s\_{W}(W\_{i})]. The differentiation under the integral is permitted by Assumption [B.1](https://arxiv.org/html/2510.20032v1#A2.Thmassumption1 "Assumption B.1 (Marginal Agent Regularity). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") which guarantees that the conditional expectation of YiY\_{i} is bounded.
∎

Next, we consider the indirect effect. To this end, we define

|  |  |  |
| --- | --- | --- |
|  | 𝒰part​(θ):=∑a=0K∫ma​(r)​μa​(r,𝐜​(θ,sW),PR|θ,sW)​fR|0​(r)​𝑑r\displaystyle\mathcal{U}\_{\text{part}}(\theta):=\sum\_{a=0}^{K}\int m\_{a}(r)\mu\_{a}(r,\mathbf{c}(\theta,s\_{W}),P\_{R|\theta,s\_{W}})f\_{R|0}(r)dr |  |

We define this auxiliary functional, which evolves the market mechanism but holds the population of agents fixed to the baseline distribution, as a tool to isolate the indirect effects via the chain rule.

###### Lemma B.3 (Decomposition of the Indirect Effect).

Suppose Assumptions [B.1](https://arxiv.org/html/2510.20032v1#A2.Thmassumption1 "Assumption B.1 (Marginal Agent Regularity). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")-[B.3](https://arxiv.org/html/2510.20032v1#A2.Thmassumption3 "Assumption B.3 (Differentiability of the Market Conduct Rule). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") hold. Then 𝒰part′​(0)\mathcal{U}^{\prime}\_{\text{part}}(0) exists and is equal to:

|  |  |  |
| --- | --- | --- |
|  | 𝒰part′​(0)=∑a=0K𝔼0​[ma​(Ri)​La,𝐜0​(Ri,Rj)​sR​(Rj)]+⟨∇c𝒰​(c0,PR|0)⋅𝝍c0,sR⟩ℋR,\displaystyle\mathcal{U}^{\prime}\_{\text{part}}(0)=\sum\_{a=0}^{K}\mathbb{E}\_{0}[m\_{a}(R\_{i})L\_{a,\mathbf{c}\_{0}}(R\_{i},R\_{j})s\_{R}(R\_{j})]+\langle\nabla\_{c}\mathcal{U}(c\_{0},P\_{R|0})\cdot\bm{\psi}\_{c\_{0}},s\_{R}\rangle\_{\mathcal{H}\_{R}}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇c𝒰​(c0,PR|0)=\displaystyle\nabla\_{c}\mathcal{U}(c\_{0},P\_{R|0})= | ∑a=0K𝔼0​[ma​(Ri)​∇𝐜ha​(Ri,𝐜0,PR|0)​𝟏​{ϕa​(Ri,𝐜0)≥0}]+\displaystyle\sum\_{a=0}^{K}\mathbb{E}\_{0}\left[m\_{a}(R\_{i})\nabla\_{\mathbf{c}}h\_{a}(R\_{i},\mathbf{c}\_{0},P\_{R|0})\mathbf{1}\{\phi\_{a}(R\_{i},\mathbf{c}\_{0})\geq 0\}\right]+ |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑a=0K𝔼0​[𝔼0​[ma​(Ri)​ha​(Ri,𝐜0,PR|0)​∇𝐜ϕa​(Ri,𝐜0)∣Ri,u​n,ϕa​(Ri,𝐜0)=0]​fϕa​(0∣Ri,u​n)],\displaystyle\sum\_{a=0}^{K}\mathbb{E}\_{0}\left[\mathbb{E}\_{0}\left[m\_{a}(R\_{i})h\_{a}(R\_{i},\mathbf{c}\_{0},P\_{R|0})\nabla\_{\mathbf{c}}\phi\_{a}(R\_{i},\mathbf{c}\_{0})\mid R\_{i,un},\phi\_{a}(R\_{i},\mathbf{c}\_{0})=0\right]f\_{\phi\_{a}}(0\mid R\_{i,un})\right], |  |

and fϕa​(0∣ru​n)f\_{\phi\_{a}}(0\mid r\_{un}) is the conditional density of ϕa​(Ri,𝐜0)\phi\_{a}(R\_{i},\mathbf{c}\_{0}) given Ri,u​n=ru​nR\_{i,un}=r\_{un}.

###### Proof.

The derivative of 𝒰part​(θ)\mathcal{U}\_{\text{part}}(\theta) at θ=0\theta=0 can be found by applying the chain rule to the underlying functional 𝒰​(𝐜,PR)=∑a∫ma​(r)​μa​(r,𝐜,PR)​fR|0​(r)​𝑑r\mathcal{U}(\mathbf{c},P\_{R})=\sum\_{a}\int m\_{a}(r)\mu\_{a}(r,\mathbf{c},P\_{R})f\_{R|0}(r)dr. The derivative is the sum of the partial derivatives with respect to each argument, evaluated along the path of the reform:

|  |  |  |
| --- | --- | --- |
|  | 𝒰part′​(0)=DP​𝒰​(𝐜0,PR|0)​[sR]⏟Competition Effect+∇c𝒰​(𝐜0,PR|0)⋅𝐜′​[sR]⏟Market Conduct Effect.\displaystyle\mathcal{U}^{\prime}\_{\text{part}}(0)=\underbrace{D\_{P}\mathcal{U}(\mathbf{c}\_{0},P\_{R|0})[s\_{R}]}\_{\text{Competition Effect}}+\underbrace{\nabla\_{c}\mathcal{U}(\mathbf{c}\_{0},P\_{R|0})\cdot\mathbf{c}^{\prime}[s\_{R}]}\_{\text{Market Conduct Effect}}. |  |

The first term, the Competition Effect, is the functional derivative with respect to PRP\_{R} in the direction of the induced score sRs\_{R}. Using Assumption [B.2](https://arxiv.org/html/2510.20032v1#A2.Thmassumption2 "Assumption B.2 (Well-Behaved Mechanism). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), it is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | DP​𝒰​(𝐜0,PR|0)​[sR]\displaystyle D\_{P}\mathcal{U}(\mathbf{c}\_{0},P\_{R|0})[s\_{R}] | =∑a𝔼0​[ma​(Ri)​DP​μa​(Ri,𝐜0,PR|0)​[sR]]\displaystyle=\sum\_{a}\mathbb{E}\_{0}[m\_{a}(R\_{i})D\_{P}\mu\_{a}(R\_{i},\mathbf{c}\_{0},P\_{R|0})[s\_{R}]] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑a𝔼0​[ma​(Ri)​𝟏​{ϕa​(Ri,𝐜0)≥0}​DP​ha​(Ri,𝐜0,PR|0)​[sR]]\displaystyle=\sum\_{a}\mathbb{E}\_{0}[m\_{a}(R\_{i})\mathbf{1}\{\phi\_{a}(R\_{i},\mathbf{c}\_{0})\geq 0\}D\_{P}h\_{a}(R\_{i},\mathbf{c}\_{0},P\_{R|0})[s\_{R}]] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑a𝔼0​[ma​(Ri)​∫La,𝐜0​(Ri,r′)​sR​(r′)​𝑑r′]\displaystyle=\sum\_{a}\mathbb{E}\_{0}\left[m\_{a}(R\_{i})\int L\_{a,\mathbf{c}\_{0}}(R\_{i},r^{\prime})s\_{R}(r^{\prime})dr^{\prime}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑a𝔼0​[ma​(Ri)​La,𝐜0​(Ri,Rj)​sR​(Rj)].\displaystyle=\sum\_{a}\mathbb{E}\_{0}[m\_{a}(R\_{i})L\_{a,\mathbf{c}\_{0}}(R\_{i},R\_{j})s\_{R}(R\_{j})]. |  |

The second term is the Market Conduct Effect. The gradient ∇c𝒰​(𝐜0,PR|0)\nabla\_{c}\mathcal{U}(\mathbf{c}\_{0},P\_{R|0}) is derived by applying Corollary [A.1](https://arxiv.org/html/2510.20032v1#A1.Thmcorollary1 "Corollary A.1. ‣ Appendix A Differentiating integrals ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") from Appendix [A](https://arxiv.org/html/2510.20032v1#A1 "Appendix A Differentiating integrals ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), yielding the expression in the lemma statement. Combining this with the derivative of the market conduct rule from Assumption [B.3](https://arxiv.org/html/2510.20032v1#A2.Thmassumption3 "Assumption B.3 (Differentiability of the Market Conduct Rule). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), 𝐜′​[sR]=⟨𝝍c0,sR⟩ℋR\mathbf{c}^{\prime}[s\_{R}]=\langle\bm{\psi}\_{c\_{0}},s\_{R}\rangle\_{\mathcal{H}\_{R}}, gives the second part of the result. Summing the two effects proves the lemma.
∎

###### Lemma B.4 (Decomposition of the MPE).

Suppose Assumptions [B.1](https://arxiv.org/html/2510.20032v1#A2.Thmassumption1 "Assumption B.1 (Marginal Agent Regularity). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")-[B.3](https://arxiv.org/html/2510.20032v1#A2.Thmassumption3 "Assumption B.3 (Differentiability of the Market Conduct Rule). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") hold; then the total MPE can be decomposed into a direct effect and an indirect equilibrium effect:

|  |  |  |
| --- | --- | --- |
|  | 𝒰′​(0)=𝔼0​[Yi​sW​(Wi)]+𝒰part′​(0).\displaystyle\mathcal{U}^{\prime}(0)=\mathbb{E}\_{0}[Y\_{i}s\_{W}(W\_{i})]+\mathcal{U}^{\prime}\_{\text{part}}(0). |  |

###### Proof.

We analyze the difference quotient for 𝒰​(θ)\mathcal{U}(\theta). Let μa​(θ)=μa​(r,𝐜​(θ),PR|θ)\mu\_{a}(\theta)=\mu\_{a}(r,\mathbf{c}(\theta),P\_{R|\theta}) and μa​(0)=μa​(r,𝐜0,PR|0)\mu\_{a}(0)=\mu\_{a}(r,\mathbf{c}\_{0},P\_{R|0}). The difference quotient is:

|  |  |  |
| --- | --- | --- |
|  | 𝒰​(θ)−𝒰​(0)θ=1θ​∫y​fY|A,W,R​[μa​(θ)​fR|W​fW​(θ)−μa​(0)​fR|W​fW​(0)]​𝑑λ\displaystyle\frac{\mathcal{U}(\theta)-\mathcal{U}(0)}{\theta}=\frac{1}{\theta}\int yf\_{Y|A,W,R}\left[\mu\_{a}(\theta)f\_{R|W}f\_{W}(\theta)-\mu\_{a}(0)f\_{R|W}f\_{W}(0)\right]d\lambda |  |

We decompose the term in the brackets by adding and subtracting μa​(0)​fR|W​fW​(θ)\mu\_{a}(0)f\_{R|W}f\_{W}(\theta):

|  |  |  |
| --- | --- | --- |
|  | 1θ​∫y​fY|A,W,R​[(μa​(θ)−μa​(0))​fR|W​fW​(θ)+μa​(0)​fR|W​(fW​(θ)−fW​(0))]​𝑑λ\displaystyle\frac{1}{\theta}\int yf\_{Y|A,W,R}\left[(\mu\_{a}(\theta)-\mu\_{a}(0))f\_{R|W}f\_{W}(\theta)+\mu\_{a}(0)f\_{R|W}(f\_{W}(\theta)-f\_{W}(0))\right]d\lambda |  |

The second term in this sum corresponds to the direct effect. As θ→0\theta\to 0, its limit is 𝔼0​[Yi​sW​(Wi)]\mathbb{E}\_{0}[Y\_{i}s\_{W}(W\_{i})] by Lemma [B.2](https://arxiv.org/html/2510.20032v1#A2.Thmlemma2 "Lemma B.2 (The Direct Effect). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."). We now focus on the first term, which captures the indirect effect:

|  |  |  |
| --- | --- | --- |
|  | Indirect Term=1θ​∫y​fY|A,W,R​(μa​(θ)−μa​(0))​fR|W​fW​(θ)​𝑑λ\displaystyle\text{Indirect Term}=\frac{1}{\theta}\int yf\_{Y|A,W,R}(\mu\_{a}(\theta)-\mu\_{a}(0))f\_{R|W}f\_{W}(\theta)d\lambda |  |

We further decompose this by writing fW​(θ)=fW​(0)+(fW​(θ)−fW​(0))f\_{W}(\theta)=f\_{W}(0)+(f\_{W}(\theta)-f\_{W}(0)):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Indirect Term | =1θ​∫y​fY|A,W,R​(μa​(θ)−μa​(0))​fR|W​fW​(0)​𝑑λ\displaystyle=\frac{1}{\theta}\int yf\_{Y|A,W,R}(\mu\_{a}(\theta)-\mu\_{a}(0))f\_{R|W}f\_{W}(0)d\lambda\qquad | (A)\displaystyle(A) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫y​fY|A,W,R​(μa​(θ)−μa​(0))​fR|W​fW​(θ)−fW​(0)θ​𝑑λ\displaystyle+\int yf\_{Y|A,W,R}(\mu\_{a}(\theta)-\mu\_{a}(0))f\_{R|W}\frac{f\_{W}(\theta)-f\_{W}(0)}{\theta}d\lambda\qquad | (B)\displaystyle(B) |  |

The second part, Term (B), is negligible. As θ→0\theta\to 0, the factor (μa​(θ)−μa​(0))(\mu\_{a}(\theta)-\mu\_{a}(0)) converges to 0 due to the continuity of the mechanism and market conduct rule. The other factor, fW​(θ)−fW​(0)θ\frac{f\_{W}(\theta)-f\_{W}(0)}{\theta}, converges to sW​(w)​fW|0​(w)s\_{W}(w)f\_{W|0}(w). Thus, the entire integrand converges pointwise to 0. The Dominated Convergence Theorem (justified by our assumptions) implies the integral of this term converges to 0.

The first part, Term (A), is the difference quotient for 𝒰part​(θ)\mathcal{U}\_{\text{part}}(\theta). By integrating over yy and ww with the baseline policy fW​(0)f\_{W}(0), the expression becomes:

|  |  |  |
| --- | --- | --- |
|  | Term (A)=1θ​(∫ma​(r)​μa​(θ)​fR|0​(r)​𝑑r−∫ma​(r)​μa​(0)​fR|0​(r)​𝑑r)=𝒰part​(θ)−𝒰part​(0)θ\displaystyle\text{Term (A)}=\frac{1}{\theta}\left(\int m\_{a}(r)\mu\_{a}(\theta)f\_{R|0}(r)dr-\int m\_{a}(r)\mu\_{a}(0)f\_{R|0}(r)dr\right)=\frac{\mathcal{U}\_{\text{part}}(\theta)-\mathcal{U}\_{\text{part}}(0)}{\theta} |  |

Taking the limit as θ→0\theta\to 0 for all terms, we find that 𝒰′​(0)\mathcal{U}^{\prime}(0) is the sum of the direct effect and 𝒰part′​(0)\mathcal{U}^{\prime}\_{\text{part}}(0), which proves the result.
∎

###### Lemma B.5 (Identification).

Suppose Assumptions [B.1](https://arxiv.org/html/2510.20032v1#A2.Thmassumption1 "Assumption B.1 (Marginal Agent Regularity). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")-[B.3](https://arxiv.org/html/2510.20032v1#A2.Thmassumption3 "Assumption B.3 (Differentiability of the Market Conduct Rule). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") hold. Also, suppose 𝔼0​[1ha​(Ri,𝐜0,PR|0)]<∞\mathbb{E}\_{0}\left[\frac{1}{h\_{a}(R\_{i},\mathbf{c}\_{0},P\_{R|0})}\right]<\infty and 𝔼0​[(‖∇𝐜h​(Ri,𝐜0,PR|0)‖2ha​(Ri,𝐜0,PR|0))2]<∞\mathbb{E}\_{0}\left[\left(\frac{\|\nabla\_{\mathbf{c}}h(R\_{i},\mathbf{c}\_{0},P\_{R|0})\|\_{2}}{h\_{a}(R\_{i},\mathbf{c}\_{0},P\_{R|0})}\right)^{2}\right]<\infty Then the MPE is identified

###### Proof.

To show identification, we must express the components of the MPE as expectations over the observed data distribution. The core of the argument is an inverse weighting identity that allows us to replace the unobserved ma​(Ri)m\_{a}(R\_{i}) with the observed outcome YiY\_{i}. For any sufficiently regular function g​(a,r,r′)g(a,r,r^{\prime}), the following identity holds:

|  |  |  |
| --- | --- | --- |
|  | ∑a=0K𝔼0​[ma​(Ri)​g​(a,Ri,Rj)​μa​(Ri,𝐜0,PR|0)]=𝔼0​[Yi​g​(Ai,Ri,Rj)].\displaystyle\sum\_{a=0}^{K}\mathbb{E}\_{0}[m\_{a}(R\_{i})g(a,R\_{i},R\_{j})\mu\_{a}(R\_{i},\mathbf{c}\_{0},P\_{R|0})]=\mathbb{E}\_{0}[Y\_{i}g(A\_{i},R\_{i},R\_{j})]. |  |

To see this, we apply the law of iterated expectations to the right-hand side, conditioning first on (Ai,Ri,Rj)(A\_{i},R\_{i},R\_{j}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼0​[Yi​g​(Ai,Ri,Rj)]\displaystyle\mathbb{E}\_{0}[Y\_{i}g(A\_{i},R\_{i},R\_{j})] | =𝔼0​[𝔼0​[Yi|Ai,Ri,Rj]​g​(Ai,Ri,Rj)]\displaystyle=\mathbb{E}\_{0}[\mathbb{E}\_{0}[Y\_{i}|A\_{i},R\_{i},R\_{j}]g(A\_{i},R\_{i},R\_{j})] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼0​[mAi​(Ri)​g​(Ai,Ri,Rj)]\displaystyle=\mathbb{E}\_{0}[m\_{A\_{i}}(R\_{i})g(A\_{i},R\_{i},R\_{j})] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑a=0K𝔼0​[ma​(Ri)​g​(a,Ri,Rj)​𝟏​{Ai=a}]\displaystyle=\sum\_{a=0}^{K}\mathbb{E}\_{0}[m\_{a}(R\_{i})g(a,R\_{i},R\_{j})\mathbf{1}\{A\_{i}=a\}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑a=0K𝔼0​[ma​(Ri)​g​(a,Ri,Rj)​ℙ​(Ai=a|Ri,Rj)],\displaystyle=\sum\_{a=0}^{K}\mathbb{E}\_{0}[m\_{a}(R\_{i})g(a,R\_{i},R\_{j})\mathbb{P}(A\_{i}=a|R\_{i},R\_{j})], |  |

where the second line follows from the definition of mam\_{a} and the fact that YiY\_{i} is independent of RjR\_{j} conditional on (Ai,Ri)(A\_{i},R\_{i}). Since ℙ​(Ai=a|Ri,Rj)=μa​(Ri,𝐜0,PR|0)\mathbb{P}(A\_{i}=a|R\_{i},R\_{j})=\mu\_{a}(R\_{i},\mathbf{c}\_{0},P\_{R|0}), the identity is established. The moment conditions in the Lemma statement ensure these expectations are well-defined.

We now apply this identity to the two terms.

1. Competition Effect Term:
Let g​(a,Ri,Rj)=La,𝐜0​(Ri,Rj)ha​(Ri,𝐜0,PR|0)​sR​(Rj)g(a,R\_{i},R\_{j})=\frac{L\_{a,\mathbf{c}\_{0}}(R\_{i},R\_{j})}{h\_{a}(R\_{i},\mathbf{c}\_{0},P\_{R|0})}s\_{R}(R\_{j}). The term is:

|  |  |  |
| --- | --- | --- |
|  | ∑a=0K𝔼0​[ma​(Ri)​La,𝐜0​(Ri,Rj)​sR​(Rj)].\displaystyle\sum\_{a=0}^{K}\mathbb{E}\_{0}[m\_{a}(R\_{i})L\_{a,\mathbf{c}\_{0}}(R\_{i},R\_{j})s\_{R}(R\_{j})]. |  |

Note that La,𝐜0​(Ri,Rj)L\_{a,\mathbf{c}\_{0}}(R\_{i},R\_{j}) must be zero if agent ii is ineligible (ϕa​(Ri,𝐜0)<0\phi\_{a}(R\_{i},\mathbf{c}\_{0})<0), as their allocation cannot be affected by others. Thus, we can write the term as:

|  |  |  |
| --- | --- | --- |
|  | ∑a=0K𝔼0​[ma​(Ri)​La,𝐜0​(Ri,Rj)ha​(Ri,𝐜0,PR|0)​μa​(Ri,𝐜0,PR|0)​sR​(Rj)].\displaystyle\sum\_{a=0}^{K}\mathbb{E}\_{0}\left[m\_{a}(R\_{i})\frac{L\_{a,\mathbf{c}\_{0}}(R\_{i},R\_{j})}{h\_{a}(R\_{i},\mathbf{c}\_{0},P\_{R|0})}\mu\_{a}(R\_{i},\mathbf{c}\_{0},P\_{R|0})s\_{R}(R\_{j})\right]. |  |

Using our identity, this is equal to 𝔼0​[Yi​LAi,𝐜0​(Ri,Rj)hAi​(Ri,𝐜0,PR|0)​sR​(Rj)]\mathbb{E}\_{0}\left[Y\_{i}\frac{L\_{A\_{i},\mathbf{c}\_{0}}(R\_{i},R\_{j})}{h\_{A\_{i}}(R\_{i},\mathbf{c}\_{0},P\_{R|0})}s\_{R}(R\_{j})\right], which simplifies to 𝔼0​[γ​(Rj)​sW​(Wj)]\mathbb{E}\_{0}[\gamma(R\_{j})s\_{W}(W\_{j})]. The assumption 𝔼0​[1/ha]<∞\mathbb{E}\_{0}[1/h\_{a}]<\infty ensures this expression is well-defined.

2. Inframarginal Market Conduct Term:
Let g​(a,Ri,Rj)=∇𝐜ha​(Ri,𝐜0,PR|0)ha​(Ri,𝐜0,PR|0)g(a,R\_{i},R\_{j})=\frac{\nabla\_{\mathbf{c}}h\_{a}(R\_{i},\mathbf{c}\_{0},P\_{R|0})}{h\_{a}(R\_{i},\mathbf{c}\_{0},P\_{R|0})}. The term is:

|  |  |  |
| --- | --- | --- |
|  | ∑a=0K𝔼0​[ma​(Ri)​∇𝐜ha​(Ri,𝐜0,PR|0)​𝟏​{ϕa​(Ri,𝐜0)≥0}].\displaystyle\sum\_{a=0}^{K}\mathbb{E}\_{0}[m\_{a}(R\_{i})\nabla\_{\mathbf{c}}h\_{a}(R\_{i},\mathbf{c}\_{0},P\_{R|0})\mathbf{1}\{\phi\_{a}(R\_{i},\mathbf{c}\_{0})\geq 0\}]. |  |

Replacing the indicator with μa/ha\mu\_{a}/h\_{a} and applying the identity yields the identified expression:

|  |  |  |
| --- | --- | --- |
|  | 𝔼0​[Yi​∇𝐜hAi​(Ri,𝐜0,PR|0)hAi​(Ri,𝐜0,PR|0)].\displaystyle\mathbb{E}\_{0}\left[Y\_{i}\frac{\nabla\_{\mathbf{c}}h\_{A\_{i}}(R\_{i},\mathbf{c}\_{0},P\_{R|0})}{h\_{A\_{i}}(R\_{i},\mathbf{c}\_{0},P\_{R|0})}\right]. |  |

The assumption 𝔼0​[(‖∇𝐜ha‖/ha)2]<∞\mathbb{E}\_{0}[(\|\nabla\_{\mathbf{c}}h\_{a}\|/h\_{a})^{2}]<\infty ensures this is well-defined.

Finally, the boundary term in ∇c𝒰\nabla\_{c}\mathcal{U} involves the conditional mean ma​(r)m\_{a}(r) evaluated at the boundary surface. Since ma​(r)m\_{a}(r) is assumed to be continuous in rc​o​n​tr\_{cont}, its value at the boundary is the limit of its values on the interior, which are identified from the observed data. This standard RDD-style argument ensures that ma​(r)m\_{a}(r) is identified for any rr at the boundary. This, together with the fact that hah\_{a} and ϕa\phi\_{a} are known functions, guarantees that the entire boundary term is identified.
∎

## Appendix C Examples

This appendix applies the general framework developed in Appendix [B](https://arxiv.org/html/2510.20032v1#A2 "Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") to the canonical examples presented in Section [4](https://arxiv.org/html/2510.20032v1#S4 "4 Examples ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") of the main text. For each example, we follow a three-step process: (1) we formally specify the model’s components, (2) we verify that the model satisfies the key assumptions required for our main theorem, and (3) we derive the specific form of the equilibrium-adjusted outcome, Ψitotal\Psi\_{i}^{\text{total}}, by simplifying the general formula.

### C.1 Price-Based Allocation

#### C.1.1 Model Specification

The market allocates a single product (a∈{0,1}a\in\{0,1\}) with fixed supply q∈(0,1)q\in(0,1).

* •

  Reports: Agents submit a continuous valuation Ri∈ℝ+R\_{i}\in\mathbb{R}\_{+}. We assume the baseline distribution of reports PR|0P\_{R|0} admits a continuous and positive density, fR​(r)f\_{R}(r).
* •

  Allocation Rule: An agent receives the good if their report exceeds a market-clearing price or cutoff, c∈ℝ+c\in\mathbb{R}\_{+}. The allocation probability is thus:

  |  |  |  |
  | --- | --- | --- |
  |  | μ1​(Ri,c)=𝟏​{Ri>c},μ0​(Ri,c)=𝟏​{Ri≤c}.\mu\_{1}(R\_{i},c)=\mathbf{1}\{R\_{i}>c\},\quad\mu\_{0}(R\_{i},c)=\mathbf{1}\{R\_{i}\leq c\}. |  |
* •

  Market Conduct Rule: The cutoff c0c\_{0} is set to satisfy the supply constraint, i.e., it is the (1−q)(1-q)-quantile of the report distribution:

  |  |  |  |
  | --- | --- | --- |
  |  | 𝔼0​[μ1​(Ri,c0)]=∫c0∞fR​(r)​𝑑r=q.\mathbb{E}\_{0}[\mu\_{1}(R\_{i},c\_{0})]=\int\_{c\_{0}}^{\infty}f\_{R}(r)dr=q. |  |

#### C.1.2 Verification of Assumptions

We verify the key assumptions from Appendix [B](https://arxiv.org/html/2510.20032v1#A2 "Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.").

* •

  Assumption [B.2](https://arxiv.org/html/2510.20032v1#A2.Thmassumption2 "Assumption B.2 (Well-Behaved Mechanism). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") (Well-Behaved Mechanism): The allocation rule fits the required decomposition. For a=1a=1, we have ϕ1​(Ri,c)=Ri−c\phi\_{1}(R\_{i},c)=R\_{i}-c and h1​(Ri,c,PR)=1h\_{1}(R\_{i},c,P\_{R})=1. For a=0a=0, we have ϕ0​(Ri,c)=c−Ri\phi\_{0}(R\_{i},c)=c-R\_{i} and h0​(Ri,c,PR)=1h\_{0}(R\_{i},c,P\_{R})=1.

  1. 1.

     The functions ha=1h\_{a}=1 and ϕa\phi\_{a} are continuously differentiable in cc.
  2. 2.

     The eligibility function ϕa\phi\_{a} does not depend on PRP\_{R}.
  3. 3.

     The smooth component ha=1h\_{a}=1 is constant and thus trivially Hadamard differentiable in PRP\_{R}, with a derivative kernel La​(r,r′)=0L\_{a}(r,r^{\prime})=0.
  4. 4.

     All components are continuous.
* •

  Assumption [B.1](https://arxiv.org/html/2510.20032v1#A2.Thmassumption1 "Assumption B.1 (Marginal Agent Regularity). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") (Marginal Agents): The report RiR\_{i} is fully continuous. We assume the conditional mean outcomes ma​(r)m\_{a}(r) are continuous in rr, as stated in the main text. The non-degeneracy condition ‖∇rϕa‖2=|1|=1>0\|\nabla\_{r}\phi\_{a}\|\_{2}=|1|=1>0 holds.
* •

  Assumption [B.3](https://arxiv.org/html/2510.20032v1#A2.Thmassumption3 "Assumption B.3 (Differentiability of the Market Conduct Rule). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") (Differentiability of Market Conduct): The market conduct rule is defined implicitly by G​(c,PR):=∫c∞𝑑PR​(r)−q=0G(c,P\_{R}):=\int\_{c}^{\infty}dP\_{R}(r)-q=0. This is differentiable in L2L\_{2}. By the Implicit Function Theorem, its derivative is c′​[sR]=−(∂G/∂c)−1​(∂G/∂PR)​[sR]c^{\prime}[s\_{R}]=-(\partial G/\partial c)^{-1}(\partial G/\partial P\_{R})[s\_{R}]. We have ∂G/∂c=−fR​(c)\partial G/\partial c=-f\_{R}(c) and (∂G/∂PR)​[sR]=𝔼0​[sR​(Ri)​𝟏​{Ri>c}](\partial G/\partial P\_{R})[s\_{R}]=\mathbb{E}\_{0}[s\_{R}(R\_{i})\mathbf{1}\{R\_{i}>c\}]. Thus, c′​[sR]c^{\prime}[s\_{R}] is a continuous linear functional in L2L\_{2}, and the assumption holds.

Since the market conduct rule is differentiable in L2L\_{2}, Corollary [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmcorollary1 "Corollary 3.1 (The Equilibrium-Adjusted Outcome). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") applies.

#### C.1.3 Derivation of Ψitotal\Psi\_{i}^{\text{total}}

We start with the general formula from Corollary [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmcorollary1 "Corollary 3.1 (The Equilibrium-Adjusted Outcome). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."): Ψitotal=Ψifixed+Ψconduct​(Ri)\Psi\_{i}^{\text{total}}=\Psi\_{i}^{\text{fixed}}+\Psi^{\text{conduct}}(R\_{i}).

1. 1.

   Fixed Component Ψifixed=Yi+γ​(Ri)\Psi\_{i}^{\text{fixed}}=Y\_{i}+\gamma(R\_{i}):
   The competition externality, γ​(Ri)\gamma(R\_{i}), depends on the kernel LaL\_{a}. Since hah\_{a} is constant with respect to PRP\_{R}, its derivative kernel La​(r,r′)L\_{a}(r,r^{\prime}) is identically zero. Therefore, γ​(Ri)=0\gamma(R\_{i})=0, and Ψifixed=Yi\Psi\_{i}^{\text{fixed}}=Y\_{i}.
2. 2.

   Market Conduct Component Ψconduct​(Ri)=∇c𝒰​(c0)⋅ψc0​(Ri)\Psi^{\text{conduct}}(R\_{i})=\nabla\_{c}\mathcal{U}(c\_{0})\cdot\psi\_{c\_{0}}(R\_{i}):
   We need to derive the welfare gradient ∇c𝒰​(c0)\nabla\_{c}\mathcal{U}(c\_{0}) and the influence function of the cutoff, ψc0​(Ri)\psi\_{c\_{0}}(R\_{i}).

   * •

     Welfare Gradient ∇c𝒰​(c0)\nabla\_{c}\mathcal{U}(c\_{0}): We apply Theorem [A.1](https://arxiv.org/html/2510.20032v1#A1.Thmtheorem1 "Theorem A.1. ‣ Appendix A Differentiating integrals ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."). Since ha=1h\_{a}=1 does not depend on cc, the volume term is zero. The derivative comes entirely from the boundary term. For a=1a=1, the boundary is at Ri=cR\_{i}=c, and for a=0a=0, it is also at Ri=cR\_{i}=c. A marginal increase in cc moves agents from allocation 1 to 0. The total effect is the mass of agents at the boundary, fR​(c0)f\_{R}(c\_{0}), times their change in average outcome, m0​(c0)−m1​(c0)m\_{0}(c\_{0})-m\_{1}(c\_{0}).

     |  |  |  |
     | --- | --- | --- |
     |  | ∇c𝒰​(c0)=−[m1​(c0)−m0​(c0)]​fR​(c0)=−τ​(c0)​fR​(c0).\nabla\_{c}\mathcal{U}(c\_{0})=-[m\_{1}(c\_{0})-m\_{0}(c\_{0})]f\_{R}(c\_{0})=-\tau(c\_{0})f\_{R}(c\_{0}). |  |
   * •

     Influence Function ψc0​(Ri)\psi\_{c\_{0}}(R\_{i}): From the verification of Assumption [B.3](https://arxiv.org/html/2510.20032v1#A2.Thmassumption3 "Assumption B.3 (Differentiability of the Market Conduct Rule). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), we have c′​[sR]=𝔼0​[sR​(Ri)​𝟏​{Ri>c0}fR​(c0)]c^{\prime}[s\_{R}]=\mathbb{E}\_{0}[s\_{R}(R\_{i})\frac{\mathbf{1}\{R\_{i}>c\_{0}\}}{f\_{R}(c\_{0})}]. By definition, the influence function is the term inside the expectation multiplying the score:

     |  |  |  |
     | --- | --- | --- |
     |  | ψc0​(Ri)=𝟏​{Ri>c0}fR​(c0)=AifR​(c0).\psi\_{c\_{0}}(R\_{i})=\frac{\mathbf{1}\{R\_{i}>c\_{0}\}}{f\_{R}(c\_{0})}=\frac{A\_{i}}{f\_{R}(c\_{0})}. |  |

   Combining these pieces, the market conduct externality is:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Ψconduct​(Ri)\displaystyle\Psi^{\text{conduct}}(R\_{i}) | =∇c𝒰​(c0)⋅ψc0​(Ri)\displaystyle=\nabla\_{c}\mathcal{U}(c\_{0})\cdot\psi\_{c\_{0}}(R\_{i}) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =(−τ​(c0)​fR​(c0))⋅(AifR​(c0))=−τ​(c0)​Ai.\displaystyle=\left(-\tau(c\_{0})f\_{R}(c\_{0})\right)\cdot\left(\frac{A\_{i}}{f\_{R}(c\_{0})}\right)=-\tau(c\_{0})A\_{i}. |  |
3. 3.

   Total Equilibrium-Adjusted Outcome:
   Summing the components gives the final result:

   |  |  |  |
   | --- | --- | --- |
   |  | Ψitotal=Yi−τ​(c0)​Ai.\Psi\_{i}^{\text{total}}=Y\_{i}-\tau(c\_{0})A\_{i}. |  |

   This matches the expression in the main text. The density terms fR​(c0)f\_{R}(c\_{0}) cancel out, revealing that the externality an inframarginal agent imposes by taking a slot is exactly the welfare loss of the single marginal agent they displace.

### C.2 School Choice with Multiple Schools

#### C.2.1 Model Specification

We consider a market with two schools (k∈{1,2}k\in\{1,2\}) and an outside option (a=0a=0). Each school has a fixed capacity qkq\_{k}.

* •

  Reports: An agent’s report is a vector Ri=(≻i,Vi,1,Vi,2)R\_{i}=(\succ\_{i},V\_{i,1},V\_{i,2}), consisting of a strict preference ranking ≻i\succ\_{i} over {0,1,2}\{0,1,2\} and a vector of school-specific continuous scores (e.g., grades or test scores).
* •

  Allocation Rule: The market is cleared by a vector of score cutoffs 𝐜=(c1,c2)\mathbf{c}=(c\_{1},c\_{2}). An agent is eligible for school kk if their score exceeds the cutoff, Vi,k>ckV\_{i,k}>c\_{k}. Each agent is assigned to their most-preferred school for which they are eligible. If they are not eligible for any school they prefer to the outside option, they receive a=0a=0.
* •

  Market Conduct Rule: The cutoff vector 𝐜0\mathbf{c}\_{0} is determined by the system of capacity constraints:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝔼0​[μ1​(Ri,𝐜0)]\displaystyle\mathbb{E}\_{0}[\mu\_{1}(R\_{i},\mathbf{c}\_{0})] | =q1\displaystyle=q\_{1} |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝔼0​[μ2​(Ri,𝐜0)]\displaystyle\mathbb{E}\_{0}[\mu\_{2}(R\_{i},\mathbf{c}\_{0})] | =q2\displaystyle=q\_{2} |  |

#### C.2.2 Verification of Assumptions

* •

  Assumption [B.2](https://arxiv.org/html/2510.20032v1#A2.Thmassumption2 "Assumption B.2 (Well-Behaved Mechanism). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") (Well-Behaved Mechanism): For any given preference ranking ≻i\succ\_{i}, the allocation rule is a series of indicator functions based on the scores. For example, for an agent with preferences 1≻2≻01\succ\_{2}\succ 0, the allocation rule is μ1​(Ri,𝐜)=𝟏​{Vi,1>c1}\mu\_{1}(R\_{i},\mathbf{c})=\mathbf{1}\{V\_{i,1}>c\_{1}\} and μ2​(Ri,𝐜)=𝟏​{Vi,1≤c1,Vi,2>c2}\mu\_{2}(R\_{i},\mathbf{c})=\mathbf{1}\{V\_{i,1}\leq c\_{1},V\_{i,2}>c\_{2}\}. Each of these can be written in the required form with ha=1h\_{a}=1 and ϕa\phi\_{a} being a function of the score margins (e.g., ϕ1=Vi,1−c1\phi\_{1}=V\_{i,1}-c\_{1}). The conditions on smoothness, anonymity, and Hadamard differentiability (with La=0L\_{a}=0) hold trivially.
* •

  Assumption [B.1](https://arxiv.org/html/2510.20032v1#A2.Thmassumption1 "Assumption B.1 (Marginal Agent Regularity). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") (Marginal Agents): The scores (Vi,1,Vi,2)(V\_{i,1},V\_{i,2}) are the continuous components of the report, while the preference ranking ≻i\succ\_{i} is the discrete component. We assume ma​(Ri)m\_{a}(R\_{i}) is continuous in the scores. The non-degeneracy condition on the gradients of ϕa\phi\_{a} holds.
* •

  Assumption [B.3](https://arxiv.org/html/2510.20032v1#A2.Thmassumption3 "Assumption B.3 (Differentiability of the Market Conduct Rule). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") (Differentiability of Market Conduct): The market conduct rule is defined by the system of equations 𝐆​(𝐜,PR):=𝔼PR​[𝝁​(Ri,𝐜)]−𝐪=𝟎\mathbf{G}(\mathbf{c},P\_{R}):=\mathbb{E}\_{P\_{R}}[\bm{\mu}(R\_{i},\mathbf{c})]-\mathbf{q}=\mathbf{0}. The Jacobian of this system is Jk​j=∂Gk/∂cjJ\_{kj}=\partial G\_{k}/\partial c\_{j}. We assume this matrix is invertible at 𝐜0\mathbf{c}\_{0}, which requires that the cross-school substitution effects are not perfectly collinear. The rule is differentiable in L2L\_{2}.

As in the previous example, Corollary [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmcorollary1 "Corollary 3.1 (The Equilibrium-Adjusted Outcome). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") applies.

#### C.2.3 Derivation of Ψitotal\Psi\_{i}^{\text{total}}

We again use the formula Ψitotal=Yi+γ​(Ri)+Ψconduct​(Ri)\Psi\_{i}^{\text{total}}=Y\_{i}+\gamma(R\_{i})+\Psi^{\text{conduct}}(R\_{i}).

1. 1.

   Fixed Component Ψifixed\Psi\_{i}^{\text{fixed}}: Since the allocation rule (conditional on preferences) does not depend on PRP\_{R}, the derivative kernel LaL\_{a} is zero. This implies the competition externality is γ​(Ri)=0\gamma(R\_{i})=0, and thus Ψifixed=Yi\Psi\_{i}^{\text{fixed}}=Y\_{i}.
2. 2.

   Market Conduct Component Ψconduct​(Ri)\Psi^{\text{conduct}}(R\_{i}): This component is given by ⟨∇𝐜𝒰​(𝐜0),𝝍𝐜0​(Ri)⟩\langle\nabla\_{\mathbf{c}}\mathcal{U}(\mathbf{c}\_{0}),\bm{\psi}\_{\mathbf{c}\_{0}}(R\_{i})\rangle, where the gradient and influence function are now vectors.

   * •

     Influence Function ψ𝐜0​(Ri)\bm{\psi}\_{\mathbf{c}\_{0}}(R\_{i}): Applying the Implicit Function Theorem to the vector market conduct rule gives 𝐜′​[sR]=−J0−1​(∂𝐆/∂PR)​[sR]\mathbf{c}^{\prime}[s\_{R}]=-J\_{0}^{-1}(\partial\mathbf{G}/\partial P\_{R})[s\_{R}]. The second term is 𝔼0​[sR​(Ri)​𝝁​(Ri,𝐜0)]=𝔼0​[sR​(Ri)​𝐀i]\mathbb{E}\_{0}[s\_{R}(R\_{i})\bm{\mu}(R\_{i},\mathbf{c}\_{0})]=\mathbb{E}\_{0}[s\_{R}(R\_{i})\mathbf{A}\_{i}], where 𝐀i\mathbf{A}\_{i} is the vector of allocation indicators. The vector-valued influence function is therefore:

     |  |  |  |
     | --- | --- | --- |
     |  | 𝝍𝐜0​(Ri)=−J0−1​𝐀i.\bm{\psi}\_{\mathbf{c}\_{0}}(R\_{i})=-J\_{0}^{-1}\mathbf{A}\_{i}. |  |
   * •

     Welfare Gradient ∇𝐜𝒰​(𝐜0)\nabla\_{\mathbf{c}}\mathcal{U}(\mathbf{c}\_{0}): We apply Theorem [A.1](https://arxiv.org/html/2510.20032v1#A1.Thmtheorem1 "Theorem A.1. ‣ Appendix A Differentiating integrals ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."). The derivative with respect to a single cutoff, cjc\_{j}, is determined by the welfare change of agents at that margin (Vi,j=cjV\_{i,j}=c\_{j}). Let ρj→k\rho\_{j\to k} be the density of agents with score Vi,j=cjV\_{i,j}=c\_{j} who, upon losing eligibility for school jj, are reallocated to their next-best option, kk. Let τj→k​(cj)\tau\_{j\to k}(c\_{j}) be their average change in outcome. The jj-th component of the gradient is the sum over all possible reallocations from margin jj:

     |  |  |  |
     | --- | --- | --- |
     |  | ∂𝒰∂cj​(𝐜0)=−∑k∈𝒜ρj→k​τj→k​(cj).\frac{\partial\mathcal{U}}{\partial c\_{j}}(\mathbf{c}\_{0})=-\sum\_{k\in\mathcal{A}}\rho\_{j\to k}\tau\_{j\to k}(c\_{j}). |  |

     This corresponds to the vector 𝝈~\tilde{\bm{\sigma}} defined in the main text.
   * •

     The Jacobian Matrix J0J\_{0}: The entry Jk​j=∂𝔼0​[μk]/∂cjJ\_{kj}=\partial\mathbb{E}\_{0}[\mu\_{k}]/\partial c\_{j} measures how enrollment at school kk changes when the cutoff for school jj increases. The diagonal elements Jj​jJ\_{jj} are negative (enrollment at jj falls). The off-diagonal elements Jk​jJ\_{kj} (k≠jk\neq j) are positive and represent the substitution effects: the density of agents who are pushed out of school jj and into school kk, i.e., Jk​j=ρj→kJ\_{kj}=\rho\_{j\to k}.

   Combining these, the market conduct externality is:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Ψconduct​(Ri)\displaystyle\Psi^{\text{conduct}}(R\_{i}) | =⟨∇𝐜𝒰​(𝐜0),𝝍𝐜0​(Ri)⟩=(∇𝐜𝒰​(𝐜0))⊤​(−J0−1​𝐀i)\displaystyle=\langle\nabla\_{\mathbf{c}}\mathcal{U}(\mathbf{c}\_{0}),\bm{\psi}\_{\mathbf{c}\_{0}}(R\_{i})\rangle=(\nabla\_{\mathbf{c}}\mathcal{U}(\mathbf{c}\_{0}))^{\top}(-J\_{0}^{-1}\mathbf{A}\_{i}) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =−((J0−1)⊤​∇𝐜𝒰​(𝐜0))⊤​𝐀i.\displaystyle=-\left((J\_{0}^{-1})^{\top}\nabla\_{\mathbf{c}}\mathcal{U}(\mathbf{c}\_{0})\right)^{\top}\mathbf{A}\_{i}. |  |

   Let us define the vector of social externality values 𝐯:=(J0−1)⊤​∇𝐜𝒰​(𝐜0)\mathbf{v}:=(J\_{0}^{-1})^{\top}\nabla\_{\mathbf{c}}\mathcal{U}(\mathbf{c}\_{0}). Then the expression simplifies to Ψconduct​(Ri)=−𝐯⊤​𝐀i\Psi^{\text{conduct}}(R\_{i})=-\mathbf{v}^{\top}\mathbf{A}\_{i}.
3. 3.

   Total Equilibrium-Adjusted Outcome:
   Summing the components gives the final vector form:

   |  |  |  |
   | --- | --- | --- |
   |  | Ψitotal=Yi−𝐯⊤​𝐀i=Yi−v1⋅𝟏​{Ai=1}−v2⋅𝟏​{Ai=2}.\Psi\_{i}^{\text{total}}=Y\_{i}-\mathbf{v}^{\top}\mathbf{A}\_{i}=Y\_{i}-v\_{1}\cdot\mathbf{1}\{A\_{i}=1\}-v\_{2}\cdot\mathbf{1}\{A\_{i}=2\}. |  |

   This result shows that the social value of a seat at a given school, vkv\_{k}, is a complex combination of the marginal treatment effects at \*all\* cutoffs, weighted by the full matrix of equilibrium substitution patterns captured by (J0−1)⊤(J\_{0}^{-1})^{\top}.

### C.3 Second-Price Auction with a Reserve Price

#### C.3.1 Model Specification

We consider a sealed-bid, second-price auction for a single good (a∈{0,1}a\in\{0,1\}) among nn i.i.d. participants.

* •

  Reports: Each agent ii submits a bid Ri∈ℝ+R\_{i}\in\mathbb{R}\_{+}, which we take to be their private valuation.
* •

  Allocation Rule: An agent wins if their bid is above the reserve price, cc, and is the highest of all nn bids. The probability of winning is μ1​(r,c,PR)=𝟏​{r>c}⋅FR​(r)n−1\mu\_{1}(r,c,P\_{R})=\mathbf{1}\{r>c\}\cdot F\_{R}(r)^{n-1}.
* •

  Market Conduct Rule: The reserve price c0c\_{0} is set to ensure the ex-ante probability of an agent winning is a fixed quantity qq. This rule simplifies to an algebraic equation:

  |  |  |  |
  | --- | --- | --- |
  |  | 1n​(1−FR|0​(c0)n)=q.\displaystyle\frac{1}{n}\left(1-F\_{R|0}(c\_{0})^{n}\right)=q. |  |

#### C.3.2 Derivation of Ψitotal\Psi\_{i}^{\text{total}}

The total equilibrium-adjusted outcome is the sum of the private outcome and two distinct externality terms: Ψitotal=Yi+γ​(Ri)+Ψconduct​(Ri)\Psi\_{i}^{\text{total}}=Y\_{i}+\gamma(R\_{i})+\Psi^{\text{conduct}}(R\_{i}).

##### 1. Competition Externality γ​(Ri)\gamma(R\_{i}):

This term captures the welfare impact from a change in the bid distribution on other bidders, holding the reserve price fixed. It simplifies to an intuitive expression involving the maximum order statistic of the n−1n-1 competing bids, which we denote R(n−1)R\_{(n-1)}:

|  |  |  |
| --- | --- | --- |
|  | γ​(Ri)=𝔼0​[τ​(R(n−1))|R(n−1)≥r~]×(1−FR|0​(r~)n−1),where ​r~=max⁡(c0,Ri).\displaystyle\gamma(R\_{i})=\mathbb{E}\_{0}\left[\tau(R\_{(n-1)})|R\_{(n-1)}\geq\tilde{r}\right]\times\left(1-F\_{R|0}(\tilde{r})^{n-1}\right),\qquad\text{where }\tilde{r}=\max(c\_{0},R\_{i}). |  |

This is the expected treatment effect for the winning competitor, conditional on them being a relevant threat (bidding above r~\tilde{r}), multiplied by the probability that such a threat exists.

##### 2. Market Conduct Externality Ψconduct​(Ri)\Psi^{\text{conduct}}(R\_{i}):

This term captures the welfare impact from agent ii’s influence on the equilibrium reserve price. We derive its influence function, ψc0​(Ri)\psi\_{c\_{0}}(R\_{i}), from the simplified market conduct rule using the Implicit Function Theorem. This yields:

|  |  |  |
| --- | --- | --- |
|  | ψc0​(Ri)=𝟏​{Ri>c0}fR|0​(c0).\displaystyle\psi\_{c\_{0}}(R\_{i})=\frac{\mathbf{1}\{R\_{i}>c\_{0}\}}{f\_{R|0}(c\_{0})}. |  |

Multiplying this by the welfare gradient, ∇c𝒰​(c0)=−τ​(c0)​FR|0​(c0)n−1​fR|0​(c0)\nabla\_{c}\mathcal{U}(c\_{0})=-\tau(c\_{0})F\_{R|0}(c\_{0})^{n-1}f\_{R|0}(c\_{0}), gives the externality:

|  |  |  |
| --- | --- | --- |
|  | Ψconduct​(Ri)=−τ​(c0)​FR|0​(c0)n−1⋅𝟏​{Ri>c0}.\displaystyle\Psi^{\text{conduct}}(R\_{i})=-\tau(c\_{0})F\_{R|0}(c\_{0})^{n-1}\cdot\mathbf{1}\{R\_{i}>c\_{0}\}. |  |

This shows the externality is non-zero only for losing bidders.

### C.4 Auction with an Optimal Reserve Price

We now modify the previous auction example by changing the platform’s objective. Instead of setting a reserve price to meet a quantity target, the platform sets it to maximize expected revenue, following Myerson (1981).

#### C.4.1 Model Specification

The setup for agents, reports, and the allocation rule is identical to the second-price auction in the previous section. The only change is the market conduct rule.

* •

  Market Conduct Rule: The reserve price cc is set to solve the platform’s first-order condition for revenue maximization:

  |  |  |  |
  | --- | --- | --- |
  |  | G​(c,PR):=(1−FR​(c))−c​fR​(c)=0,G(c,P\_{R}):=(1-F\_{R}(c))-cf\_{R}(c)=0, |  |

  where fR​(c)f\_{R}(c) is the probability density function of reports evaluated at the reserve price cc.

#### C.4.2 Verification of Assumptions

The presence of the density term fR​(c)f\_{R}(c) in the market conduct rule makes its differentiability properties more subtle.

* •

  Failure in L2L\_{2}: The derivative of the functional c​(PR)c(P\_{R}) with respect to a perturbation with score sRs\_{R} can be found via the Implicit Function Theorem. This derivative involves a term proportional to fR​(c0)​sR​(c0)f\_{R}(c\_{0})s\_{R}(c\_{0}), which is a point evaluation of the score function. The point-evaluation operator is not a continuous linear functional on the space L2​(Ri)L\_{2}(R\_{i}). A sequence of scores can converge to zero in the L2L\_{2} norm while diverging at the specific point c0c\_{0}. Consequently, Assumption [B.3](https://arxiv.org/html/2510.20032v1#A2.Thmassumption3 "Assumption B.3 (Differentiability of the Market Conduct Rule). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") is violated for the standard L2L\_{2} space, and Corollary [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmcorollary1 "Corollary 3.1 (The Equilibrium-Adjusted Outcome). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") does not apply.
* •

  Resolution in Sobolev Space: To proceed, we must restrict the class of admissible policy reforms to those that induce sufficiently smooth scores. We assume the space of report scores ℋR\mathcal{H}\_{R} is a weighted Sobolev space H1H^{1}, with the inner product:

  |  |  |  |
  | --- | --- | --- |
  |  | ⟨ψ,s⟩H1:=𝔼0​[ψ​(Ri)​s​(Ri)]+𝔼0​[ψ′​(Ri)​s′​(Ri)].\langle\psi,s\rangle\_{H^{1}}:=\mathbb{E}\_{0}[\psi(R\_{i})s(R\_{i})]+\mathbb{E}\_{0}[\psi^{\prime}(R\_{i})s^{\prime}(R\_{i})]. |  |

  In this space, the Sobolev embedding theorem ensures that point evaluation is a continuous operator. Therefore, the functional c​(PR)c(P\_{R}) is continuously differentiable. Assumption [B.3](https://arxiv.org/html/2510.20032v1#A2.Thmassumption3 "Assumption B.3 (Differentiability of the Market Conduct Rule). ‣ Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") now holds, but for this stronger Hilbert space. All other assumptions are maintained as before.

#### C.4.3 Derivation of the MPE

Since Corollary [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmcorollary1 "Corollary 3.1 (The Equilibrium-Adjusted Outcome). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") does not apply, we must use the general form of the MPE from Theorem [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmtheorem1 "Theorem 3.1 (The Marginal Policy Effect). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."):

|  |  |  |
| --- | --- | --- |
|  | MPE=𝔼0​[Ψifixed​sW​(Wi)]+⟨Ψconduct,sR⟩ℋR.\text{MPE}=\mathbb{E}\_{0}[\Psi\_{i}^{\text{fixed}}s\_{W}(W\_{i})]+\langle\Psi^{\text{conduct}},s\_{R}\rangle\_{\mathcal{H}\_{R}}. |  |

1. 1.

   Fixed Component Ψifixed\Psi\_{i}^{\text{fixed}}: This component is identical to the previous auction example: Ψifixed=Yi+γ​(Ri)\Psi\_{i}^{\text{fixed}}=Y\_{i}+\gamma(R\_{i}).
2. 2.

   Market Conduct Component ⟨Ψconduct,sR⟩ℋR\langle\Psi^{\text{conduct}},s\_{R}\rangle\_{\mathcal{H}\_{R}}: This term is ⟨∇c𝒰​(c0)⋅ψc0​(Ri),sR​(Ri)⟩H1\langle\nabla\_{c}\mathcal{U}(c\_{0})\cdot\psi\_{c\_{0}}(R\_{i}),s\_{R}(R\_{i})\rangle\_{H^{1}}. We derive the representer ψc0\psi\_{c\_{0}} below.

   * •

     Welfare Gradient ∇c𝒰​(c0)\nabla\_{c}\mathcal{U}(c\_{0}): This is identical to the previous auction example:

     |  |  |  |
     | --- | --- | --- |
     |  | ∇c𝒰​(c0)=−τ​(c0)​fR|0​(c0)​FR|0​(c0)n−1.\nabla\_{c}\mathcal{U}(c\_{0})=-\tau(c\_{0})f\_{R|0}(c\_{0})F\_{R|0}(c\_{0})^{n-1}. |  |
   * •

     Characterization of the Representer ψc0\psi\_{c\_{0}}: The representer is defined by the relation c′​[sR]=⟨ψc0,sR⟩H1c^{\prime}[s\_{R}]=\langle\psi\_{c\_{0}},s\_{R}\rangle\_{H^{1}}. We first find an expression for the functional c′​[sR]c^{\prime}[s\_{R}] using the Implicit Function Theorem on G​(c,PR)=0G(c,P\_{R})=0. Differentiating w.r.t. the policy perturbation at baseline gives:

     |  |  |  |
     | --- | --- | --- |
     |  | ∂G∂c|c0,PR|0⋅c′​[sR]+∂G∂PR​[sR]|c0,PR|0=0.\frac{\partial G}{\partial c}\bigg|\_{c\_{0},P\_{R|0}}\cdot c^{\prime}[s\_{R}]+\frac{\partial G}{\partial P\_{R}}[s\_{R}]\bigg|\_{c\_{0},P\_{R|0}}=0. |  |

     The partial derivatives are ∂G∂c=−2​fR​(c)−c​fR′​(c)\frac{\partial G}{\partial c}=-2f\_{R}(c)-cf^{\prime}\_{R}(c) and
     ∂G∂PR​[sR]=−𝔼0​[sR​(Ri)​𝟏​{Ri≤c0}]−c0​fR|0​(c0)​sR​(c0)\frac{\partial G}{\partial P\_{R}}[s\_{R}]=-\mathbb{E}\_{0}[s\_{R}(R\_{i})\mathbf{1}\{R\_{i}\leq c\_{0}\}]-c\_{0}f\_{R|0}(c\_{0})s\_{R}(c\_{0}).
     Solving for c′​[sR]c^{\prime}[s\_{R}] gives the functional:

     |  |  |  |
     | --- | --- | --- |
     |  | c′​[sR]=K⋅(𝔼0​[sR​(Ri)​𝟏​{Ri≤c0}]+c0​fR|0​(c0)​sR​(c0)),c^{\prime}[s\_{R}]=K\cdot\left(\mathbb{E}\_{0}[s\_{R}(R\_{i})\mathbf{1}\{R\_{i}\leq c\_{0}\}]+c\_{0}f\_{R|0}(c\_{0})s\_{R}(c\_{0})\right), |  |

     where K=(2​fR|0​(c0)+c0​fR|0′​(c0))−1K=(2f\_{R|0}(c\_{0})+c\_{0}f^{\prime}\_{R|0}(c\_{0}))^{-1}. We now equate this with the inner product form:

     |  |  |  |
     | --- | --- | --- |
     |  | 𝔼0​[ψc0​sR]+𝔼0​[ψc0′​sR′]=K⋅(𝔼0​[sR⋅𝟏≤c0]+c0​fR|0​(c0)​sR​(c0)).\mathbb{E}\_{0}[\psi\_{c\_{0}}s\_{R}]+\mathbb{E}\_{0}[\psi^{\prime}\_{c\_{0}}s^{\prime}\_{R}]=K\cdot\left(\mathbb{E}\_{0}[s\_{R}\cdot\mathbf{1}\_{\leq c\_{0}}]+c\_{0}f\_{R|0}(c\_{0})s\_{R}(c\_{0})\right). |  |

     Using integration by parts on the second term on the left, 𝔼0​[ψc0′​sR′]=−𝔼0​[sR​(ψc0′​fR|0)′/fR|0]\mathbb{E}\_{0}[\psi^{\prime}\_{c\_{0}}s^{\prime}\_{R}]=-\mathbb{E}\_{0}[s\_{R}(\psi^{\prime}\_{c\_{0}}f\_{R|0})^{\prime}/f\_{R|0}], and representing the point evaluation using the Dirac delta function, sR​(c0)=𝔼0​[sR​(Ri)​δ​(Ri−c0)/fR|0​(c0)]s\_{R}(c\_{0})=\mathbb{E}\_{0}[s\_{R}(R\_{i})\delta(R\_{i}-c\_{0})/f\_{R|0}(c\_{0})], we can group all terms under a single expectation over sR​(Ri)s\_{R}(R\_{i}):

     |  |  |  |
     | --- | --- | --- |
     |  | 𝔼0​[sR​(Ri)​(ψc0​(Ri)−(ψc0′​(Ri)​fR|0​(Ri))′fR|0​(Ri)−K⋅(𝟏​{Ri≤c0}+c0​δ​(Ri−c0)))]=0.\mathbb{E}\_{0}\left[s\_{R}(R\_{i})\left(\psi\_{c\_{0}}(R\_{i})-\frac{(\psi^{\prime}\_{c\_{0}}(R\_{i})f\_{R|0}(R\_{i}))^{\prime}}{f\_{R|0}(R\_{i})}-K\cdot(\mathbf{1}\{R\_{i}\leq c\_{0}\}+c\_{0}\delta(R\_{i}-c\_{0}))\right)\right]=0. |  |

     Since this must hold for all sR∈H1s\_{R}\in H^{1}, the term in the parentheses must be zero. This yields the Sturm-Liouville differential equation that uniquely defines the representer ψc0​(r)\psi\_{c\_{0}}(r):

     |  |  |  |
     | --- | --- | --- |
     |  | ψc0​(r)​fR|0​(r)−(ψc0′​(r)​fR|0​(r))′=K⋅(𝟏​{r≤c0}​fR|0​(r)+c0​fR|0​(c0)​δ​(r−c0)).\psi\_{c\_{0}}(r)f\_{R|0}(r)-(\psi^{\prime}\_{c\_{0}}(r)f\_{R|0}(r))^{\prime}=K\cdot\left(\mathbf{1}\{r\leq c\_{0}\}f\_{R|0}(r)+c\_{0}f\_{R|0}(c\_{0})\delta(r-c\_{0})\right). |  |
3. 3.

   Total Marginal Policy Effect:
   The MPE is therefore:

   |  |  |  |
   | --- | --- | --- |
   |  | MPE=𝔼0​[(Yi+γ​(Ri))​sW​(Wi)]+∇c𝒰​(c0)⋅⟨ψc0,sR⟩H1.\displaystyle\text{MPE}=\mathbb{E}\_{0}[(Y\_{i}+\gamma(R\_{i}))s\_{W}(W\_{i})]+\nabla\_{c}\mathcal{U}(c\_{0})\cdot\langle\psi\_{c\_{0}},s\_{R}\rangle\_{H^{1}}. |  |

   This expression cannot be simplified into a single covariance. It demonstrates that when the market-clearing rule is itself the solution to an optimization problem that depends on local features of the report distribution, the welfare impact of a policy reform depends not just on its direction (sRs\_{R}), but also on its smoothness (via the derivative term sR′s^{\prime}\_{R} implicit in the H1H^{1} inner product).

### C.5 Top Trading Cycles

This section discusses the Top Trading Cycles (TTC) mechanism. Unlike the previous examples, the market-clearing parameters (the cutoffs) are defined as the solution to a dynamic system. We first describe this characterization and then provide a high-level sketch of our analysis.

#### C.5.1 Model Specification and Cutoff Characterization

We follow the continuum model of Leshno and Lo ([2021](https://arxiv.org/html/2510.20032v1#bib.bib31)). The market consists of a continuum of students and a finite set of schools 𝒞={1,…,n}\mathcal{C}=\{1,...,n\} with capacities qcq\_{c}. A student’s type RiR\_{i} includes their strict preference ordering ≻i\succ\_{i} and a vector of priority scores Vi=(Vi,1,…,Vi,n)∈[0,1]nV\_{i}=(V\_{i,1},...,V\_{i,n})\in[0,1]^{n}.

* •

  Allocation Rule and Cutoffs: The TTC algorithm assigns students by clearing trading cycles. Leshno and Lo ([2021](https://arxiv.org/html/2510.20032v1#bib.bib31)) show that the final assignment can be described by a matrix of cutoffs 𝐜={ca,b}a,b∈𝒞\mathbf{c}=\{c\_{a,b}\}\_{a,b\in\mathcal{C}}. A student ii is admitted to their most-preferred school aa within their "budget set," which is the set of schools B​(Ri,𝐜)={k∈𝒞∣∃b∈𝒞​ s.t. ​Vi,b≥ck,b}B(R\_{i},\mathbf{c})=\{k\in\mathcal{C}\mid\exists b\in\mathcal{C}\text{ s.t. }V\_{i,b}\geq c\_{k,b}\}
* •

  Market Conduct Rule (Dynamic System): The cutoff matrix 𝐜\mathbf{c} is not determined by a simple set of algebraic equations but as the solution to a dynamic process. The key objects are:

  1. 1.

     The TTC Path γ​(t)\bm{\gamma}(t): A vector-valued function 𝜸​(t)∈[0,1]n\bm{\gamma}(t)\in[0,1]^{n} that tracks the priority frontiers of the schools over time, starting from 𝜸​(0)=𝟏\bm{\gamma}(0)=\mathbf{1}.
  2. 2.

     Marginal Trade Balance Equations: The path evolves according to a system of ordinary differential equations that ensure the "flow" of students trading into a school equals the "flow" of students trading out of it at every moment. For each school kk, this is:

     |  |  |  |
     | --- | --- | --- |
     |  | ∑b∈𝒞γb′​(t)​Hbk​(𝜸​(t))=∑a∈𝒞γk′​(t)​Hka​(𝜸​(t)).\sum\_{b\in\mathcal{C}}\gamma^{\prime}\_{b}(t)H\_{b}^{k}(\bm{\gamma}(t))=\sum\_{a\in\mathcal{C}}\gamma^{\prime}\_{k}(t)H\_{k}^{a}(\bm{\gamma}(t)). |  |

     Here, Hbk​(𝐱)H\_{b}^{k}(\mathbf{x}) is the marginal density of students at the priority frontier 𝐱\mathbf{x} whose top choice is school kk and who have the highest priority at school bb.
  3. 3.

     Capacity Equations (Stopping Conditions): The process for a school kk stops at time t(k)t^{(k)} when its capacity is filled. The final cutoffs are determined by the path evaluated at these stopping times: ck,b=γb​(t(k))c\_{k,b}=\gamma\_{b}(t^{(k)}).

The market conduct rule 𝐜​(PR)\mathbf{c}(P\_{R}) is therefore the function that maps a distribution of reports PRP\_{R} (which determines the marginal densities HbkH\_{b}^{k}) to the matrix of cutoffs that solves this dynamic system.

#### C.5.2 TTC in the MPE Framework

For a given cutoff matrix 𝐜\mathbf{c}, the allocation rule μa​(Ri,𝐜)\mu\_{a}(R\_{i},\mathbf{c}) is a complex but deterministic indicator function. It can be written in our decomposition form with ha=1h\_{a}=1 and ϕa​(Ri,𝐜)\phi\_{a}(R\_{i},\mathbf{c}) representing the condition that aa is the most-preferred school in the budget set B​(Ri,𝐜)B(R\_{i},\mathbf{c}).
Since ha=1h\_{a}=1, the allocation rule does not depend on PRP\_{R} once 𝐜\mathbf{c} is known. Therefore, the Hadamard derivative kernel LaL\_{a} is zero, and the competition externality γ​(Ri)\gamma(R\_{i}) is zero. The entire equilibrium spillover is captured by the market conduct effect. We assume the primitives are regular enough for the assumptions of Corollary [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmcorollary1 "Corollary 3.1 (The Equilibrium-Adjusted Outcome). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") to hold.

#### C.5.3 Derivation for a Parametric Case

Let’s analyze an economy with two schools (n=2n=2), capacities q1,q2q\_{1},q\_{2}, and a unit mass of students. A fraction π1\pi\_{1} of students prefer school 1, and the remaining π2=1−π1\pi\_{2}=1-\pi\_{1} prefer school 2. Priorities Vi=(Vi,1,Vi,2)V\_{i}=(V\_{i,1},V\_{i,2}) are independently and uniformly distributed on [0,1]2[0,1]^{2} and are independent of preferences.

1. 1.

   Solving the Dynamic System:
   In this setting, the marginal densities are constant: Hbk​(𝐱)=πkH\_{b}^{k}(\mathbf{x})=\pi\_{k} for any b,k∈{1,2}b,k\in\{1,2\}. The trade balance equation for school 1 becomes:

   |  |  |  |
   | --- | --- | --- |
   |  | γ1′​(t)​H11+γ2′​(t)​H21=γ1′​(t)​H11+γ1′​(t)​H12⟹γ2′​(t)​π1=γ1′​(t)​π2.\gamma^{\prime}\_{1}(t)H\_{1}^{1}+\gamma^{\prime}\_{2}(t)H\_{2}^{1}=\gamma^{\prime}\_{1}(t)H\_{1}^{1}+\gamma^{\prime}\_{1}(t)H\_{1}^{2}\implies\gamma^{\prime}\_{2}(t)\pi\_{1}=\gamma^{\prime}\_{1}(t)\pi\_{2}. |  |

   This gives the simple linear ODE γ2′​(t)/γ1′​(t)=π2/π1\gamma^{\prime}\_{2}(t)/\gamma^{\prime}\_{1}(t)=\pi\_{2}/\pi\_{1}. Parameterizing the path by tt such that γ1​(t)=1−t\gamma\_{1}(t)=1-t, the solution with initial condition 𝜸​(0)=(1,1)\bm{\gamma}(0)=(1,1) is the line:

   |  |  |  |
   | --- | --- | --- |
   |  | γ2​(t)=1−(π2/π1)​t.\gamma\_{2}(t)=1-(\pi\_{2}/\pi\_{1})t. |  |
2. 2.

   Characterizing the Welfare Gradient ∇𝐜𝒰\nabla\_{\mathbf{c}}\mathcal{U}:
   The parameter vector 𝐜\mathbf{c} is the matrix of four cutoffs {c1,1,c1,2,c2,1,c2,2}\{c\_{1,1},c\_{1,2},c\_{2,1},c\_{2,2}\}. Applying Theorem [A.1](https://arxiv.org/html/2510.20032v1#A1.Thmtheorem1 "Theorem A.1. ‣ Appendix A Differentiating integrals ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), the gradient ∂𝒰/∂ck,b\partial\mathcal{U}/\partial c\_{k,b} is identified by the welfare change of agents on the boundary Vi,b=ck,bV\_{i,b}=c\_{k,b} who are reallocated. We denote this gradient abstractly by ∇𝐜𝒰\nabla\_{\mathbf{c}}\mathcal{U}.
3. 3.

   Characterizing the Influence Function ψ𝐜0​(Ri)\bm{\psi}\_{\mathbf{c}\_{0}}(R\_{i}):
   The influence function is the vector of derivatives of the cutoffs with respect to a perturbation in the distribution. A general policy perturbation with score sRs\_{R} on the report distribution PRP\_{R} induces a pathwise derivative on any functional of that distribution. We find the influence function by differentiating the entire dynamic system that determines the cutoffs.

   * •

     Perturbation of Primitives: The perturbation directly affects the marginal densities Hbk​(𝜸)H\_{b}^{k}(\bm{\gamma}) that govern the path’s evolution, and the demand functions Dk​(𝜸)D^{k}(\bm{\gamma}) that determine the stopping times. We denote their pathwise derivatives as Hbk⁣′​[sR]H\_{b}^{k\prime}[s\_{R}] and Dk⁣′​[sR]D^{k\prime}[s\_{R}]. For example, in our parametric case, the perturbation affects both the shares πk\pi\_{k} and the uniformity of the priority distribution.
   * •

     Path Influence Function: The TTC path is defined by the ODE γ2′​(t)​H21​(𝜸​(t))=γ1′​(t)​H12​(𝜸​(t))\gamma^{\prime}\_{2}(t)H\_{2}^{1}(\bm{\gamma}(t))=\gamma^{\prime}\_{1}(t)H\_{1}^{2}(\bm{\gamma}(t)). We differentiate this entire equation with respect to the policy perturbation. This yields a variational equation for the influence on the path, 𝝍γ​(t;Ri)\bm{\psi}\_{\gamma}(t;R\_{i}), which now includes a forcing term due to the direct perturbation of the HH functions:

     |  |  |  |
     | --- | --- | --- |
     |  | dd​t​ψγ,2​(t)=J​(𝜸​(t))⋅ψγ,2​(t)+F​(𝜸​(t),sR).\frac{d}{dt}\psi\_{\gamma,2}(t)=J(\bm{\gamma}(t))\cdot\psi\_{\gamma,2}(t)+F(\bm{\gamma}(t),s\_{R}). |  |

     Here, JJ is a Jacobian term from differentiating the ODE’s coefficients with respect to 𝜸\bm{\gamma}, and the forcing term FF is a linear functional of the score sRs\_{R} that depends on the derivatives Hbk⁣′​[sR]H\_{b}^{k\prime}[s\_{R}]. The solution to this ODE gives the influence function for the path shape.
   * •

     Stopping Time Influence Function: Assume school 1 fills first. The stopping time t(1)t^{(1)} is implicitly defined by the capacity constraint D1​(𝜸​(t(1)),PR)=q1D^{1}(\bm{\gamma}(t^{(1)}),P\_{R})=q\_{1}. Differentiating this constraint with respect to the perturbation at baseline gives:

     |  |  |  |
     | --- | --- | --- |
     |  | ∂D1∂PR​[sR]+∇𝜸D1⋅(𝜸′​(t0(1))​d​t(1)d​θ​[sR]+d​𝜸​(t0(1))d​θ​[sR])=0.\frac{\partial D^{1}}{\partial P\_{R}}[s\_{R}]+\nabla\_{\bm{\gamma}}D^{1}\cdot\left(\bm{\gamma}^{\prime}(t^{(1)}\_{0})\frac{dt^{(1)}}{d\theta}[s\_{R}]+\frac{d\bm{\gamma}(t^{(1)}\_{0})}{d\theta}[s\_{R}]\right)=0. |  |

     The term ∂D1∂PR​[sR]\frac{\partial D^{1}}{\partial P\_{R}}[s\_{R}] captures the direct effect of the perturbation on the demand functional. Solving for the derivative of the stopping time, d​t(1)d​θ​[sR]\frac{dt^{(1)}}{d\theta}[s\_{R}], yields its influence function ψt(1)​(Ri)\psi\_{t^{(1)}}(R\_{i}):

     |  |  |  |
     | --- | --- | --- |
     |  | ψt(1)​(Ri)=−(d​D1d​t|t0(1))−1​(D1⁣′​[Ri]+∇𝜸D1⋅𝝍γ​(t0(1);Ri)),\psi\_{t^{(1)}}(R\_{i})=-\left(\frac{dD^{1}}{dt}\bigg|\_{t^{(1)}\_{0}}\right)^{-1}\left(D^{1\prime}[R\_{i}]+\nabla\_{\bm{\gamma}}D^{1}\cdot\bm{\psi}\_{\gamma}(t^{(1)}\_{0};R\_{i})\right), |  |

     where D1⁣′​[Ri]D^{1\prime}[R\_{i}] is the representer for the pathwise derivative of the demand functional.
   * •

     Cutoff Influence Functions: The influence functions for the cutoffs are found by applying the chain rule. The derivation for the second-round cutoffs simplifies considerably. As established by Leshno and Lo ([2021](https://arxiv.org/html/2510.20032v1#bib.bib31)), once school 1 fills at time t(1)t^{(1)}, its priority frontier stops advancing, i.e., γ1​(t)=γ1​(t(1))\gamma\_{1}(t)=\gamma\_{1}(t^{(1)}) for all t≥t(1)t\geq t^{(1)}.

     + –

       The cutoff c1,2c\_{1,2}: This cutoff is defined as γ1​(t(2))\gamma\_{1}(t^{(2)}). Since t(2)≥t(1)t^{(2)}\geq t^{(1)}, it follows that γ1​(t(2))=γ1​(t(1))=c1,1\gamma\_{1}(t^{(2)})=\gamma\_{1}(t^{(1)})=c\_{1,1}. Thus, we have the identity c1,2=c1,1c\_{1,2}=c\_{1,1}, which implies their influence functions must also be equal: ψc1,2​(Ri)=ψc1,1​(Ri)\psi\_{c\_{1,2}}(R\_{i})=\psi\_{c\_{1,1}}(R\_{i}).
     + –

       The cutoff c2,2c\_{2,2}: The final cutoff, c2,2=γ2​(t(2))c\_{2,2}=\gamma\_{2}(t^{(2)}), is found by solving the capacity constraint for school 2 in the residual economy. Its influence function is found by differentiating this expression: ψc2,2​(Ri)=γ2′​(t0(2))​ψt(2)​(Ri)+ψγ,2​(t0(2);Ri)\psi\_{c\_{2,2}}(R\_{i})=\gamma^{\prime}\_{2}(t^{(2)}\_{0})\psi\_{t^{(2)}}(R\_{i})+\psi\_{\gamma,2}(t^{(2)}\_{0};R\_{i}). The term ψt(2)​(Ri)\psi\_{t^{(2)}}(R\_{i}) is the influence function for the second stopping time, which is found by differentiating the capacity constraint for the residual economy. This constraint depends on the outcomes of the first round, making ψt(2)​(Ri)\psi\_{t^{(2)}}(R\_{i}) a function of the previously derived first-round influence functions.

   This more general procedure fully identifies the vector of influence functions, 𝝍𝐜0​(Ri)\bm{\psi}\_{\mathbf{c}\_{0}}(R\_{i}), for any perturbation to the report distribution that satisfies our regularity conditions.
4. 4.

   Total Equilibrium-Adjusted Outcome:
   The final expression is:

   |  |  |  |
   | --- | --- | --- |
   |  | Ψitotal=Yi−⟨∇𝐜𝒰​(𝐜0),𝝍𝐜0​(Ri)⟩.\Psi\_{i}^{\text{total}}=Y\_{i}-\langle\nabla\_{\mathbf{c}}\mathcal{U}(\mathbf{c}\_{0}),\bm{\psi}\_{\mathbf{c}\_{0}}(R\_{i})\rangle. |  |

   This derivation confirms that even for a complex procedural mechanism like TTC, the MPE can be constructed within our framework. The market conduct externality is fully characterized by the welfare gradient at the cutoff boundaries and the influence function of the cutoffs, which is itself found by analyzing the sensitivity of the underlying dynamic system to policy perturbations.

## Appendix D Extensions

This appendix provides formal derivations for the extensions discussed in Section [5](https://arxiv.org/html/2510.20032v1#S5 "5 Applications and Extensions ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") of the main text.

### D.1 General Welfare Functionals

This section demonstrates that our framework extends from the mean to a general class of welfare criteria. We first provide a simple proof for functionals defined by moment conditions using the Implicit Function Theorem. We then provide a more abstract, general proof that covers any Hadamard differentiable functional.

#### D.1.1 A Direct Proof for Functionals Defined by Moment Conditions

Many common statistics, like quantiles, are defined implicitly as the solution to a moment equation. For this large class of functionals, we can prove the main result directly using the Implicit Function Theorem.

###### Proposition D.1.

Let the welfare functional 𝒰\mathcal{U} be defined implicitly as the unique solution to a moment equation 𝔼​[g​(Yi,𝒰)]=0\mathbb{E}[g(Y\_{i},\mathcal{U})]=0. Assume the function g​(y,u)g(y,u) is continuously differentiable in uu and that 𝔼0​[∂g​(Yi,𝒰0)/∂𝒰]≠0\mathbb{E}\_{0}[\partial g(Y\_{i},\mathcal{U}\_{0})/\partial\mathcal{U}]\neq 0. The Marginal Policy Effect on 𝒰\mathcal{U} is given by applying Theorem [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmtheorem1 "Theorem 3.1 (The Marginal Policy Effect). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") (or Corollary [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmcorollary1 "Corollary 3.1 (The Equilibrium-Adjusted Outcome). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")) to the transformed outcome Zi=I​F​(Yi;𝒰0)Z\_{i}=IF(Y\_{i};\mathcal{U}\_{0}), where I​F​(y;u)=−(𝔼​[∂g∂u])−1​g​(y,u)IF(y;u)=-\left(\mathbb{E}[\frac{\partial g}{\partial u}]\right)^{-1}g(y,u) is the influence function of the functional 𝒰\mathcal{U}.

###### Proof.

Under a policy perturbation θ\theta, the moment condition must hold for the perturbed value of the functional, 𝒰​(θ)\mathcal{U}(\theta):

|  |  |  |
| --- | --- | --- |
|  | G​(θ,𝒰​(θ)):=𝔼θ​[g​(Yi,𝒰​(θ))]=0.G(\theta,\mathcal{U}(\theta)):=\mathbb{E}\_{\theta}[g(Y\_{i},\mathcal{U}(\theta))]=0. |  |

Our goal is to find the MPE, d​𝒰d​θ|θ=0\frac{d\mathcal{U}}{d\theta}|\_{\theta=0}. By the Implicit Function Theorem:

|  |  |  |
| --- | --- | --- |
|  | d​𝒰d​θ|θ=0=−(∂G∂𝒰|0,𝒰0)−1​(∂G∂θ|0,𝒰0).\frac{d\mathcal{U}}{d\theta}\bigg|\_{\theta=0}=-\left(\frac{\partial G}{\partial\mathcal{U}}\bigg|\_{0,\mathcal{U}\_{0}}\right)^{-1}\left(\frac{\partial G}{\partial\theta}\bigg|\_{0,\mathcal{U}\_{0}}\right). |  |

The first component is ∂G∂𝒰=𝔼0​[∂g​(Yi,𝒰0)∂𝒰]\frac{\partial G}{\partial\mathcal{U}}=\mathbb{E}\_{0}[\frac{\partial g(Y\_{i},\mathcal{U}\_{0})}{\partial\mathcal{U}}]. The second component is the MPE for the outcome variable Zig:=g​(Yi,𝒰0)Z\_{i}^{g}:=g(Y\_{i},\mathcal{U}\_{0}):

|  |  |  |
| --- | --- | --- |
|  | ∂G∂θ=dd​θ​𝔼θ​[g​(Yi,𝒰0)]|θ=0=ℒ​(g),\frac{\partial G}{\partial\theta}=\frac{d}{d\theta}\mathbb{E}\_{\theta}[g(Y\_{i},\mathcal{U}\_{0})]\bigg|\_{\theta=0}=\mathcal{L}(g), |  |

where ℒ​(g)\mathcal{L}(g) is the MPE operator. From Appendix [B](https://arxiv.org/html/2510.20032v1#A2 "Appendix B Derivation of the Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), we know ℒ​(g)=𝔼0​[Ψig​sW​(Wi)]\mathcal{L}(g)=\mathbb{E}\_{0}[\Psi\_{i}^{g}s\_{W}(W\_{i})] (in the L2L\_{2} case).
Substituting these into the IFT formula gives:

|  |  |  |
| --- | --- | --- |
|  | d​𝒰d​θ=−(𝔼0​[∂g∂𝒰])−1​𝔼0​[Ψig​sW​(Wi)]=𝔼0​[−(𝔼0​[∂g∂𝒰])−1​Ψig⋅sW​(Wi)].\frac{d\mathcal{U}}{d\theta}=-\left(\mathbb{E}\_{0}\left[\frac{\partial g}{\partial\mathcal{U}}\right]\right)^{-1}\mathbb{E}\_{0}[\Psi\_{i}^{g}s\_{W}(W\_{i})]=\mathbb{E}\_{0}\left[-\left(\mathbb{E}\_{0}\left[\frac{\partial g}{\partial\mathcal{U}}\right]\right)^{-1}\Psi\_{i}^{g}\cdot s\_{W}(W\_{i})\right]. |  |

The term inside the expectation is the equilibrium-adjusted outcome for 𝒰\mathcal{U}. The influence function for 𝒰\mathcal{U} is I​F​(Y;𝒰0)=−(𝔼0​[∂g∂𝒰])−1​g​(Y,𝒰0)IF(Y;\mathcal{U}\_{0})=-(\mathbb{E}\_{0}[\frac{\partial g}{\partial\mathcal{U}}])^{-1}g(Y,\mathcal{U}\_{0}). Since the construction of the externality terms in Ψ\Psi is linear, it follows that −(𝔼0​[∂g∂𝒰])−1​Ψig=ΨiI​F-(\mathbb{E}\_{0}[\frac{\partial g}{\partial\mathcal{U}}])^{-1}\Psi\_{i}^{g}=\Psi\_{i}^{IF}. This shows that the MPE for 𝒰\mathcal{U} is 𝔼0​[ΨiI​F​sW​(Wi)]\mathbb{E}\_{0}[\Psi\_{i}^{IF}s\_{W}(W\_{i})], which completes the proof.
∎

#### D.1.2 The General Case for Hadamard Differentiable Functionals

The result holds more generally for any Hadamard differentiable functional. The proof below uses an integration-by-parts argument that relies on the linearity of the MPE operator and an assumption of bounded support for the outcome variable.

###### Lemma D.1 (Continuity of the MPE Operator).

The MPE operator ℒ​(g):=dd​θ​𝔼θ​[g​(Yi)]|θ=0\mathcal{L}(g):=\frac{d}{d\theta}\mathbb{E}\_{\theta}[g(Y\_{i})]|\_{\theta=0} is a continuous (bounded) linear operator on the space of bounded, measurable functions gg, equipped with the sup norm ‖g‖∞=supy|g​(y)|||g||\_{\infty}=\sup\_{y}|g(y)|.

###### Proof.

Linearity follows from the linearity of expectations and the construction of Ψg\Psi^{g}. For continuity, we show the operator is bounded. From Corollary [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmcorollary1 "Corollary 3.1 (The Equilibrium-Adjusted Outcome). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI."), ℒ​(g)=𝔼0​[Ψg​sW]\mathcal{L}(g)=\mathbb{E}\_{0}[\Psi^{g}s\_{W}]. By Cauchy-Schwarz, |ℒ​(g)|≤𝔼0​[(Ψg)2]⋅𝔼0​[sW2]|\mathcal{L}(g)|\leq\sqrt{\mathbb{E}\_{0}[(\Psi^{g})^{2}]}\cdot\sqrt{\mathbb{E}\_{0}[s\_{W}^{2}]}. The externality terms in Ψg\Psi^{g} are constructed via bounded linear operations on the conditional mean of gg, which is itself bounded by ‖g‖∞||g||\_{\infty}. It follows that 𝔼0​[(Ψg)2]\sqrt{\mathbb{E}\_{0}[(\Psi^{g})^{2}]} is bounded by a constant times ‖g‖∞||g||\_{\infty}. Thus, |ℒ​(g)|≤C⋅‖g‖∞|\mathcal{L}(g)|\leq C\cdot||g||\_{\infty} for some constant CC.
∎

###### Proposition D.2.

Let 𝒰​(FY)\mathcal{U}(F\_{Y}) be a Hadamard differentiable functional with a continuously differentiable influence function I​F​(y;FY|0)IF(y;F\_{Y|0}). Assume the outcome variable YY has bounded support. The Marginal Policy Effect on 𝒰\mathcal{U} is given by applying Theorem [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmtheorem1 "Theorem 3.1 (The Marginal Policy Effect). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.") (or Corollary [3.1](https://arxiv.org/html/2510.20032v1#S3.Thmcorollary1 "Corollary 3.1 (The Equilibrium-Adjusted Outcome). ‣ 3.3 The Equilibrium-Adjusted Outcome ‣ 3 The Marginal Policy Effect ‣ Evaluating Local Policies in Centralized MarketsWe thank Kevin Chen, Ramesh Johari, Lihua Lei, Evan Munro, Davide Viviano, and Stefan Wager for their feedback, which has greatly improved the paper. We also thank seminar participants at Harvard and Stanford, as well as conference participants at the 2024 Winter Meetings of the Econometric Society, and ACIC 2025. Wisse Rutgers acknowledges financial support from the Fundación Ramón Areces, the Maria de Maeztu Unit of Excellence CEX2020-001104-M, funded by MCIN/AEI/10.13039/501100011033, and CEMFI.")) to the transformed outcome I​F​(Yi;FY|0)IF(Y\_{i};F\_{Y|0}).

###### Proof.

The proof establishes the identity MPE​(𝒰)=MPE​(𝔼​[I​F​(Y)])\text{MPE}(\mathcal{U})=\text{MPE}(\mathbb{E}[IF(Y)]).

Step 1: MPE(𝒰\mathcal{U}) as a Stieltjes Integral.
By definition of the Hadamard derivative, the MPE of 𝒰\mathcal{U} is the integral of its influence function against the derivative of the path of outcome measures, ν′\nu^{\prime}. Let the bounded support of YY be [a,b][a,b].

|  |  |  |
| --- | --- | --- |
|  | MPE​(𝒰)=∫abI​F​(y;FY|0)​𝑑ν′​(y),where​ν′​([a,y])=ℒ​(𝟏​{Y≤y}).\text{MPE}(\mathcal{U})=\int\_{a}^{b}IF(y;F\_{Y|0})\,d\nu^{\prime}(y),\quad\text{where}\quad\nu^{\prime}([a,y])=\mathcal{L}(\mathbf{1}\{Y\leq y\}). |  |

Step 2: Integration by Parts.
We apply the integration by parts formula for Stieltjes integrals. Let u​(y)=I​F​(y)u(y)=IF(y) and d​v=d​ν′​(y)dv=d\nu^{\prime}(y), which implies v​(y)=ℒ​(𝟏​{Y≤y})v(y)=\mathcal{L}(\mathbf{1}\{Y\leq y\}).

|  |  |  |
| --- | --- | --- |
|  | MPE​(𝒰)=[I​F​(y)⋅ℒ​(𝟏​{Y≤y})]y=ab−∫abℒ​(𝟏​{Y≤y})⋅I​F′​(y)​𝑑y.\text{MPE}(\mathcal{U})=\left[IF(y)\cdot\mathcal{L}(\mathbf{1}\{Y\leq y\})\right]\_{y=a}^{b}-\int\_{a}^{b}\mathcal{L}(\mathbf{1}\{Y\leq y\})\cdot IF^{\prime}(y)dy. |  |

The boundary terms are zero. At y=by=b, ℒ​(𝟏​{Y≤b})=ℒ​(1)=0\mathcal{L}(\mathbf{1}\{Y\leq b\})=\mathcal{L}(1)=0. At y=ay=a, ℒ​(𝟏​{Y≤a})=ℒ​(0)=0\mathcal{L}(\mathbf{1}\{Y\leq a\})=\mathcal{L}(0)=0.

Step 3: Swapping Linear Operators.
We are left with the integral term. By the preceding lemma, ℒ\mathcal{L} is a continuous linear operator and thus commutes with the integral:

|  |  |  |
| --- | --- | --- |
|  | MPE​(𝒰)=−∫abℒ​(𝟏​{Y≤y})⋅I​F′​(y)​𝑑y=−ℒ​(∫abI​F′​(y)⋅𝟏​{Y≤y}​𝑑y).\text{MPE}(\mathcal{U})=-\int\_{a}^{b}\mathcal{L}(\mathbf{1}\{Y\leq y\})\cdot IF^{\prime}(y)dy=-\mathcal{L}\left(\int\_{a}^{b}IF^{\prime}(y)\cdot\mathbf{1}\{Y\leq y\}dy\right). |  |

Step 4: Conclusion.
The inner integral, for a fixed realization of YY, is ∫YbI​F′​(y)​𝑑y=[I​F​(y)]Yb=I​F​(b)−I​F​(Y)\int\_{Y}^{b}IF^{\prime}(y)dy=[IF(y)]\_{Y}^{b}=IF(b)-IF(Y).
Substituting this back, the MPE is:

|  |  |  |
| --- | --- | --- |
|  | MPE​(𝒰)=−ℒ​(I​F​(b)−I​F​(Y))=−ℒ​(I​F​(b))+ℒ​(I​F​(Y)).\text{MPE}(\mathcal{U})=-\mathcal{L}\left(IF(b)-IF(Y)\right)=-\mathcal{L}(IF(b))+\mathcal{L}(IF(Y)). |  |

Since I​F​(b)IF(b) is a constant, its MPE is zero, so ℒ​(I​F​(b))=0\mathcal{L}(IF(b))=0. This leaves the final identity:

|  |  |  |
| --- | --- | --- |
|  | MPE​(𝒰)=ℒ​(I​F​(Y))=MPE​(𝔼0​[I​F​(Y)]).\text{MPE}(\mathcal{U})=\mathcal{L}(IF(Y))=\text{MPE}(\mathbb{E}\_{0}[IF(Y)]). |  |

This shows that computing the MPE for a general functional is equivalent to computing the MPE for the mean of its influence function, which our main framework is designed to do.
∎