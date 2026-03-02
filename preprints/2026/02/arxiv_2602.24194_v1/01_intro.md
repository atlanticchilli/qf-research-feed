---
authors:
- Patrick Beissner
- Tim Boonen
- Mario Ghossoub
doc_id: arxiv:2602.24194v1
family_id: arxiv:2602.24194
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Betting under Common Beliefs: The Effect of Probability Weighting'
url_abs: http://arxiv.org/abs/2602.24194v1
url_html: https://arxiv.org/html/2602.24194v1
venue: arXiv q-fin
version: 1
year: 2026
---


Patrick Beißner
  
Australian National University
  
Tim J. Boonen
  
University of Hong Kong
  
Mario Ghossoub
  
University of Waterloo
  
This draft
Patrick Beißner: Research School of Economics – The Australian National University – Canberra, ACT 2600 – Australia
[[patrick.beissner@anu.edu.au](2602.24194v1/mailto:patrick.beissner@anu.edu.au)](2602.24194v1/mailto:)
Tim J. Boonen:
Department of Statistics and Actuarial Science
– The University of Hong Kong – Pokfulam – Hong Kong
[[tjboonen@hku.hk](2602.24194v1/mailto:tjboonen@hku.hk)](2602.24194v1/mailto:)
Mario Ghossoub: University of Waterloo – Department of Statistics and Actuarial Science – 200 University Ave. W. – Waterloo, ON, N2L 3G1 – Canada
[[mario.ghossoub@uwaterloo.ca](2602.24194v1/mailto:mario.ghossoub@uwaterloo.ca)](2602.24194v1/mailto:)

###### Abstract.

This paper examines the impact of introducing a Rank-Dependent Utility (RDU) agent into a von Neumann-Morgenstern (vNM) pure-exchange economy with no aggregate uncertainty. In the absence of the RDU agent, the classical theory predicts that Pareto-optimal allocations are full-insurance, or no-betting, allocations. We show how the probability weighting function of the RDU agent, seen as a proxy for probabilistic risk aversion that is not captured by marginal utility of wealth, can lead to Pareto optima characterized by endogenous betting, despite common baseline beliefs. Such endogenous betting at an optimum leads to uncertainty-generating trade arising purely from heterogeneity in the perception of risk, rather than in beliefs. Our results formalize the intuitive understanding that probability weighting can act as an endogenous source of belief heterogeneity, and provide a new behavioral foundation for the coexistence of common beliefs and speculative behavior, in an environment with no initial aggregate uncertainty. Interpreting the RDU agent’s nonlinear weighting function as an “internality” prompts the question of whether a social planner should intervene. We show how a benevolent social planner can nudge the RDU agent to behave closer to a vNM agent, through costly statistical or financial education, thereby (partially) restoring the optimality of full-insurance allocations.

Key Words and Phrases: Risk Sharing, Betting, Pareto Optimality, Full-Insurance Allocations, Rank-Dependent Utility, Probability Weighting.

JEL Classification: C02, D86, G22.

2010 Mathematics Subject Classification: 91B30.

Mario Ghossoub acknowledges financial support from the Natural Sciences and Engineering Research Council of Canada (NSERC Grant No. 2018-03961 and 2024-03744).

## 1. Introduction

A fundamental question in economic theory is when and why economic agents engage in speculative trade (or betting). Starting from an economic environment with no aggregate uncertainty, the classical prediction under Expected-Utility (EU) theory is that risk-averse agents will refrain from any uncertainty-generating trade unless they hold heterogeneous probabilistic beliefs. Indeed, as shown by Billot et al. ([2000](#bib.bib31 "Sharing Beliefs: Between Agreeing and Disagreeing"), [2002](#bib.bib32 "Sharing Beliefs and the Absence of Betting in the Choquet Expected Utility Model")) and Rigotti et al. ([2008](#bib.bib35 "Subjective Beliefs and ex ante Trade")), when all agents are EU maximizers sharing the same belief, every Pareto-efficient allocation must be a *no-betting allocation* (sometimes called a *full-insurance allocation*), that is, an allocation where each individual’s consumption is deterministic and equal across states. Conversely, any form of betting can be Pareto improving only if agents disagree about probability assessments. In the EU framework, therefore, heterogeneity in beliefs is both a necessary and sufficient condition for betting to be Pareto improving when starting from a full-insurance allocation.

The prediction of the classical literature is, however, empirically unconvincing. As emphasized by Billot et al. ([2000](#bib.bib31 "Sharing Beliefs: Between Agreeing and Disagreeing"), [2002](#bib.bib32 "Sharing Beliefs and the Absence of Betting in the Choquet Expected Utility Model")), real-world economies exhibit far less betting than the classical theory predicts. If agents’ beliefs differ because their subjective probabilities arise from differences in preferences, as in the subjective expected utility (SEU) model of De Finetti ([1937](#bib.bib3 "La Prévision: Ses Lois Logiques, Ses Sources Subjectives")) and Savage ([1972](#bib.bib5 "The Foundations of Statistics (2nd revised edition) – 1⁢st ed. 1954")), then divergent preferences would generically induce heterogeneous beliefs, thereby implying speculative trade. The observed paucity of betting in the real world would therefore suggest an implausibly high degree of homogeneity in preferences. Following Billot et al. ([2000](#bib.bib31 "Sharing Beliefs: Between Agreeing and Disagreeing"), [2002](#bib.bib32 "Sharing Beliefs and the Absence of Betting in the Choquet Expected Utility Model")), we interpret this discrepancy as evidence that the classical SEU model may be too restrictive a description of actual behavior.

Billot et al. ([2000](#bib.bib31 "Sharing Beliefs: Between Agreeing and Disagreeing"), [2002](#bib.bib32 "Sharing Beliefs and the Absence of Betting in the Choquet Expected Utility Model")) argue that the failure of the SEU model is due to Ellsberg-type behavior, and they re-examine the validity of the classical model’s predictions under either a multiple-priors maxmin model of decision making à la Gilboa and Schmeidler ([1989](#bib.bib6 "Maxmin Expected Utility with a Non-Unique Prior")) (as in Billot et al. ([2000](#bib.bib31 "Sharing Beliefs: Between Agreeing and Disagreeing"))) or a Choquet-type model of decision making à la Schmeidler ([1989](#bib.bib7 "Subjective Probability and Expected Utility without Additivity")) (as in Billot et al. ([2002](#bib.bib32 "Sharing Beliefs and the Absence of Betting in the Choquet Expected Utility Model"))). Beißner et al. ([2024](#bib.bib10 "(No-)Betting Pareto-Optima under Rank-Dependent Utility")), on the other hand, argue that this might be due to Allais-type behavior, as encapsulated in the Rank-Dependent Utility (RDU) model of Quiggin ([1982](#bib.bib11 "A Theory of Anticipated Utility"), [1991](#bib.bib12 "Comparative Statics for Rank-Dependent Expected Utility Theory")), which is based on distorting objectively given probabilities through a probability weighting function. Beißner et al. ([2024](#bib.bib10 "(No-)Betting Pareto-Optima under Rank-Dependent Utility")) demonstrate how betting can arise in a market with two RDU agents having different distortions of a common baseline objective probability measure on the space: sufficiently risk-seeking probability weighting may induce betting at Pareto-efficient allocations, even without differences in baseline beliefs.

In this paper, we take a similar stance to that of Beißner et al. ([2024](#bib.bib10 "(No-)Betting Pareto-Optima under Rank-Dependent Utility")), by starting from the initial position that the empirical failure of the classical model in predicting betting behavior in real-world markets could very well stem from Allais-type behavior, rather than Ellsberg-type behavior. We aim to show how the introduction of a single RDU agent, into an otherwise classical setting with EU agents that have common beliefs, can lead to drastically different predictions; namely, that betting might be Pareto improving, despite the presence of a common baseline probability measure on the state space.

Specifically, we study an economy with n>1n>1 agents and a deterministic aggregate endowment, in which n−1n-1 agents are EU maximizers and the nt​hn^{th} agent is an RDU maximizer. All agents share the same underlying probability measure on the state space, but the RDU agent distorts this measure through a nonlinear probability weighting function seen as a proxy for probabilistic risk aversion, that is, an element of risk aversion that is not captured by the marginal utility of wealth. We provide a general characterization of Pareto-efficient allocations in this mixed EU-RDU economy. We then identify conditions under which no-betting allocations remain Pareto efficient, and we show how deviations from linear probability weighting translate into well-defined regions of Pareto-efficient betting. Thereby, we demonstrate how the RDU agent’s probabilistic risk aversion fundamentally alters the structure of Pareto optima. When the RDU agent’s weighting function is linear, we recover the classical no-betting result of Billot et al. ([2000](#bib.bib31 "Sharing Beliefs: Between Agreeing and Disagreeing"), [2002](#bib.bib32 "Sharing Beliefs and the Absence of Betting in the Choquet Expected Utility Model")). When the weighting function departs from linearity, however, Pareto-efficient allocations can exhibit endogenous betting, that is, uncertainty-generating trade arising purely from heterogeneity in the perception of risk, rather than in beliefs. In essence, our results formalize the intuitive understanding that probability weighting can act as an endogenous source of belief heterogeneity. Even when all agents agree on the underlying probabilities, distortions generate effective disagreements that restore the possibility of beneficial speculative trade. Our framework therefore provides a new behavioral foundation for the coexistence of common beliefs and speculative behavior in an environment with no initial aggregate uncertainty.

We develop comparative statics for endogenous uncertainty when the RDU agent is endowed with inverse S-shaped or S-shaped probability weighting functions. Inverse S-shaped (S-shaped) weighting functions arise when agents overweight (underweight) extreme gains and losses, and are studied in Tversky and Kahneman ([1992](#bib.bib28 "Advances in prospect theory: cumulative representation of uncertainty")), Prelec ([1998](#bib.bib29 "The Probability Weighting Function")), and, more recently, Bleichrodt et al. ([2023](#bib.bib15 "Testing hurwicz expected utility")). We show that a shift from linear to inverse S-shaped or S-shaped probability weighting functions systematically splits efficient allocations into a risk-free component and a risky component. The analysis provides a simple principle for identifying when full insurance prevails and when betting emerges, and it links the extent of probability distortions to the shape of the distribution functions of optimal payoffs. To make these mechanisms transparent, we offer a tractable characterization under exponential utility and Prelec ([1998](#bib.bib29 "The Probability Weighting Function")) type weighting specifications. Moreover, we evaluate welfare via certainty equivalents and discuss how compensating transfers based on the Kaldor-Hicks criterion (e.g., Kaldor ([1939](#bib.bib17 "Welfare propositions of economics and interpersonal comparisons of utility"))) can convert a specific efficient allocation into the set of all Pareto-optimal allocations.

When agents use Prelec weighting functions, we characterize the optimal risk allocations in closed form. Interestingly, the more inverse S-shaped the weighting function becomes, the larger the probability of the full-insurance event, hence implying that the risk allocation yields a deterministic payoff with a larger probability. However, if the Prelec weighting function is S-shaped, then making it more S-shaped renders the probability of the full-insurance event smaller. For the Hurwitz weighting function used in Bleichrodt et al. ([2023](#bib.bib15 "Testing hurwicz expected utility")), we find that the probability of the atom increases with the ambiguity index, but the slope is less steep when the perceived ambiguity is larger.

The aforementioned emergence of endogenous betting despite common beliefs, as a result of probability distortions, prompts the question of whether a social planner should intervene. Guided by libertarian paternalism, in the sense of Thaler and Sunstein ([2009](#bib.bib18 "Nudge: improving decisions about health, wealth, and happiness")) and Bernheim and Taubinsky ([2018](#bib.bib19 "Behavioral public economics")), we consider a benevolent social planner who “nudges” the RDU agent through statistical or financial education. Education directly impacts the probability weighting function, pushing it toward linearity, so that the distorted beliefs move back toward the baseline belief. Education is costly, resulting in a reduction of the aggregate endowment in the economy. The outcome is to nudge the RDU agent to behave closer to an EU agent, thereby (partially) restoring the risk-free full-insurance (no-betting) allocation of the reduced constant aggregate endowment.

Our conceptual framework for nudging the RDU agent builds upon the distinction between experienced utility and decision utility, which has received renewed attention since Kahneman et al. ([1997](#bib.bib21 "Back to bentham? explorations of experienced utility")). In the same vein, Chetty ([2015](#bib.bib20 "Behavioral economics and public policy: a pragmatic perspective")) highlights how behavioral economics generates new welfare implications. Indeed, behavioral biases often lead to differences between a policymaker’s perspective, typically rooted in an agent’s experienced utility, and the agent’s decision utility. Therefore, an expansion of the set of policy tools that accounts for such differences is needed.
Our view is that the RDU agent’s nonlinear weighting function is an “internality” (e.g., Herrnstein et al. ([1993](#bib.bib22 "Utility Maximization and Melioration: Internalities in Individual Choice"))), that is, a within-person externality stemming from the individual’s failure to successfully pursue their own interests.111This interpretation relates our work to a broader class of behavioral biases that address welfare consequences, such as low saving rates (Thaler and Benartzi ([2004](#bib.bib42 "Save for tomorrow: using behavioral economics to increase employee saving"))), changes in reference points (Reck and Seibold ([2023](#bib.bib43 "The welfare economics of reference dependence"))), and deficits in financial literacy (Hastings et al. ([2013](#bib.bib45 "Financial literacy, financial education, and economic outcomes")); Bernheim and Taubinsky ([2018](#bib.bib19 "Behavioral public economics"))). The probability weighting function becomes a measurable proxy for the degree of misalignment between experienced and decision utility, offering both diagnostic insight and a lever for policy intervention.

The remainder of this paper is organized as follows. Section  [2](#S2 "2. The Economy ‣ Betting under Common Beliefs: The Effect of Probability Weighting") and Section  [3](#S3 "3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting") develop the model and characterize Pareto optima. Section  [4](#S4 "4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting") examines the endogenous uncertainty in detail, providing comparative-static results linking distortions in probability weighting to the variance and skewness of efficient allocations. Section  [5](#S5 "5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting") introduces the planner’s intervention and evaluates its effectiveness in restoring full insurance. Section  [6](#S6 "6. Conclusion ‣ Betting under Common Beliefs: The Effect of Probability Weighting") concludes. All proofs appear in the [Appendix](#LinkToAppendix "6. Conclusion ‣ Betting under Common Beliefs: The Effect of Probability Weighting").

## 2. The Economy

### 2.1. Preferences

Let (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) be a nonatomic probability space and let 𝒳⊂L∞​(Ω,ℱ,ℙ)\mathcal{X}\subset L^{\infty}(\Omega,\mathcal{F},\mathbb{P}) be a given collection of random variables containing all payoffs available to the economic agents. Consider a pure-exchange economy under uncertainty, with nn economic agents and no aggregate uncertainty. The first agent is a Rank-Dependent Utility (RDU) maximizer (as in Quiggin ([1982](#bib.bib11 "A Theory of Anticipated Utility"), [1991](#bib.bib12 "Comparative Statics for Rank-Dependent Expected Utility Theory"))), with a preference representation given by the functional U1:𝒳→ℝU\_{1}:\mathcal{X}\to\mathbb{R} defined by

|  |  |  |
| --- | --- | --- |
|  | U1​(X)=∫u1​(X)​d​T∘ℙ,∀X∈𝒳,U\_{1}(X)=\int u\_{1}(X)\,\textnormal{d}\,T\circ\mathbb{P},\ \ \forall\,X\in\mathcal{X}, |  |

for some utility function u1u\_{1} and a probability weighting function T:[0,1]→[0,1]T:[0,1]\to[0,1], where integration is in the sense of Choquet.

The agents i=2,…,ni=2,\ldots,n are Expected-Utility (EU) maximizers, each with a utility function uiu\_{i} and preferences represented by the functional Ui:𝒳→ℝU\_{i}:\mathcal{X}\to\mathbb{R}, with

|  |  |  |
| --- | --- | --- |
|  | Ui​(X)=∫ui​(X)​d​ℙ.U\_{i}(X)=\int u\_{i}(X)\,\textnormal{d}\mathbb{P}. |  |

Hence, all agents have the same underlying beliefs ℙ\mathbb{P} on (Ω,ℱ)(\Omega,\mathcal{F}). We make the following standard assumption.

###### Assumption 2.1.

The function TT is twice differentiable, strictly increasing, and such that T​(0)=0T(0)=0 and T​(1)=1T(1)=1. Moreover, each utility function uiu\_{i} is twice differentiable, strictly concave, and increasing.

Note that U1U\_{1} fails to be concave in general, unless TT is convex. Additionally, concavity of u1u\_{1} and convexity of TT are tantamount to strong risk aversion of the RDU agent (e.g., Chew et al. ([1987](#bib.bib30 "Risk Aversion in the Theory of Expected Utility with Rank Dependent Probabilities"))).

### 2.2. Allocations

The initial endowments of the agents are denoted by ζ1,…,ζn∈𝒳\zeta\_{1},\ldots,\zeta\_{n}\in\mathcal{X}, assumed nonzero. Additionally, we assume that there is no aggregate uncertainty in the economy, that is, the aggregate endowment is constant:

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nζi=𝚠∈ℝ.\sum\_{i=1}^{n}\zeta\_{i}=\mathtt{w}\in\mathbb{R}. |  |

The set of feasible allocations is given by

|  |  |  |
| --- | --- | --- |
|  | 𝒜​(𝚠):={𝐗:=(X1,…,Xn)∈𝒳n:∑i=1nXi=𝚠},\mathcal{A}(\mathtt{w}):=\Big\{\mathbf{X}:=\left(X\_{1},\ldots,X\_{n}\right)\in\mathcal{X}^{n}:\sum\_{i=1}^{n}X\_{i}=\mathtt{w}\Big\}, |  |

that is, the set of all vectors in 𝒳n\mathcal{X}^{n} that add up to the constant aggregate endowment 𝚠\mathtt{w}.

###### Definition 2.2.

An allocation 𝐗∈𝒜​(𝚠)\mathbf{X}\in\mathcal{A}(\mathtt{w}) is said to be Pareto Optimal (in short, PO) if there is no allocation 𝐗′∈𝒜​(𝚠)\mathbf{X}^{\prime}\in\mathcal{A}(\mathtt{w}) such that Ui​(Xi′)≥Ui​(Xi),U\_{i}(X^{\prime}\_{i})\geq U\_{i}(X\_{i}), for all i∈{1,…,n},i\in\{1,\ldots,n\}, with at least one strict inequality.

Similarly, for each Y∈𝒳Y\in\mathcal{X}, an allocation

|  |  |  |
| --- | --- | --- |
|  | 𝐗−1∈𝒜−1​(Y):={𝐗−1:=(X2,…,Xn)∈𝒳n−1:∑i=2nXi=Y}\mathbf{X}\_{-1}\in{\mathcal{A}}\_{-1}(Y):=\Big\{\mathbf{X}\_{-1}:=\left(X\_{2},\ldots,X\_{n}\right)\in\mathcal{X}^{n-1}:\sum\_{i=2}^{n}X\_{i}=Y\Big\} |  |

is said to be YY-Pareto Optimal (in short, YY-PO) if there is no allocation 𝐗′∈𝒜−1​(Y)\mathbf{X}^{\prime}\in{\mathcal{A}}\_{-1}(Y) such that
Ui​(Xi′)≥Ui​(Xi)U\_{i}(X^{\prime}\_{i})\geq U\_{i}(X\_{i}), for all i∈{2,…,n},i\in\{2,\ldots,n\}, with at least one strict inequality.

## 3. Betting and Efficiency

### 3.1. The Utilitarian Welfare Function

Our focus is on the following social welfare maximization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup𝐗∈𝒜​(𝚠)[U1​(X1)+∑i=2nλi​Ui​(Xi)],\sup\_{\mathbf{X}\in\mathcal{A}(\mathtt{w})}\left[U\_{1}(X\_{1})+\sum\_{i=2}^{n}\lambda\_{i}\,U\_{i}(X\_{i})\right], |  | (3.1) |

for a given vector of weights λ∈ℝ++n−1\lambda\in\mathbb{R}^{n-1}\_{++}. We now make the following observation (see Dana ([1993](#bib.bib23 "Existence and Uniqueness of Equilibria When Preferences are Additively Separable"), [2011](#bib.bib24 "Comonotonicity, Efficient Risk-Sharing and Equilibria in Markets with Short-Selling for Concave Law-Invariant Utilities"))), in light of Assumption [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1. Preferences ‣ 2. The Economy ‣ Betting under Common Beliefs: The Effect of Probability Weighting").

###### Proposition 3.1.

Solutions to ([3.1](#S3.E1 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) are PO. Moreover, if TT is convex, then any PO is a solution to ([3.1](#S3.E1 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")), for some vector of weights λ∈ℝ++n−1\lambda\in\mathbb{R}\_{++}^{n-1}.

Set X=X1X={X}\_{1} and define, for a given λ∈ℝ++n−1\lambda\in\mathbb{R}\_{++}^{n-1}, the “inner problem”:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uλ​(𝚠−X):=sup𝐗−1∈𝒜−1​(𝚠−X)Uλ​(𝐗−1),whereUλ​(𝐗−1):=∑i=2nλi​Ui​(Xi).\displaystyle U\_{\lambda}(\mathtt{w}-X):=\sup\_{\mathbf{X}\_{-1}\in{\mathcal{A}}\_{-1}(\mathtt{w}-X)}\ U^{\lambda}(\mathbf{X}\_{-1}),\ \ \text{where}\ \ U^{\lambda}(\mathbf{X}\_{-1}):=\sum\_{i=2}^{n}\lambda\_{i}\,U\_{i}(X\_{i}). |  | (3.2) |

Then problem ([3.1](#S3.E1 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) can be reformulated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | supX∈𝒳[U1​(X)+Uλ​(𝚠−X)].\displaystyle\sup\_{X\in\mathcal{X}}\,\left[U\_{1}(X)+U\_{\lambda}(\mathtt{w}-X)\right]. |  | (3.3) |

By standard results on PO allocations for risk-averse EU maximizers, solutions to ([3.3](#S3.E3 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) are characterized by the Borch rule (see Borch ([1962](#bib.bib26 "Equilibrium in a Reinsurance Market")) and Wilson ([1968](#bib.bib27 "The Theory of Syndicates"))). Specifically:

###### Proposition 3.2.

The following holds, for any 𝐗−1∈𝒜−1​(Y)\mathbf{X}\_{-1}\in{\mathcal{A}}\_{-1}(Y):

1. (1)

   𝐗−1\mathbf{X}\_{-1} is (𝚠−X)(\mathtt{w}-X)-PO if and only if there exists some λ∈ℝ++n−1\lambda\in\mathbb{R}\_{++}^{n-1} such that 𝐗−1\mathbf{X}\_{-1} is optimal for ([3.2](#S3.E2 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")).
2. (2)

   𝐗−1\mathbf{X}\_{-1} is optimal for ([3.2](#S3.E2 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) if and only if
   λi​ui′​(Xi)=λj​uj′​(Xj),\lambda\_{i}\,u\_{i}^{\prime}(X\_{i})=\lambda\_{j}\,u\_{j}^{\prime}(X\_{j}), for all i,j∈{2,…,n}i,j\in\{2,\ldots,n\}.

In particular, if 𝐗−1∈𝒜−1​(𝚠−X)\mathbf{X}\_{-1}\in{\mathcal{A}}\_{-1}(\mathtt{w}-X) is (𝚠−X)(\mathtt{w}-X)-PO then it must be comonotonic222Y,Z∈𝒳Y,Z\in\mathcal{X} are said to be comonotonic if [Y​(ω)−Y​(ω′)]​[Z​(ω)−Z​(ω′)]≥0\left[Y(\omega)-Y(\omega^{\prime})\right]\left[Z(\omega)-Z(\omega^{\prime})\right]\geq 0, for all ω,ω′∈Ω\omega,\omega^{\prime}\in\Omega. Moreover, a vector is comonotonic if it is pairwise comonotonic., by monotonicity of marginal utilities (Assumption [2.1](#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1. Preferences ‣ 2. The Economy ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). Therefore, Pareto-optimal allocations are comonotonic vectors, and hence it suffices to look for solutions to ([3.2](#S3.E2 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) that are comonotonic. For a given Y∈𝒳Y\in\mathcal{X}, let 𝒜−1C​(Y){\mathcal{A}}\_{-1}^{C}(Y) denote the collection of comonotonic allocations in 𝒜−1​(Y){\mathcal{A}}\_{-1}(Y):

|  |  |  |
| --- | --- | --- |
|  | 𝒜−1C​(Y):={𝐗−1∈𝒜−1​(Y):𝐗−1​ is comonotonic}.\mathcal{A}\_{-1}^{C}(Y):=\left\{\mathbf{X}\_{-1}\in\mathcal{A}\_{-1}(Y):\,\mathbf{X}\_{-1}\hbox{ is comonotonic}\right\}. |  |

Then in light of the above,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uλ​(𝚠−X)=sup𝐗−1∈𝒜−1C​(𝚠−X)Uλ​(𝐗−1).\displaystyle U\_{\lambda}(\mathtt{w}-X)=\sup\_{\mathbf{X}\_{-1}\in{\mathcal{A}}^{C}\_{-1}(\mathtt{w}-X)}\ U^{\lambda}(\mathbf{X}\_{-1}). |  | (3.4) |

### 3.2. Quantile Formulation of Welfare Functions

By nonatomicity, the probability space supports a random variable 𝚄\mathtt{U} that is uniformly distributed over (0,1)(0,1) (Föllmer and Schied, [2025](#bib.bib1 "Stochastic Finance: An Introduction in Discrete Time – 5⁢th ed."), Proposition D.16 & Lemma D.17). The following result allows us to exploit an important property of comonotonic allocations that leads to a recasting of problem ([3.4](#S3.E4 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) in terms of an optimization of social welfare functions over quantiles, rather than over random variable. This gives an analytically tractable formulation that will yield a closed-form characterization of Pareto optima.

For any X∈𝒳X\in\mathcal{X}, let FXF\_{X} and FX−1F\_{X}^{-1} denote the cumulative distribution function and (left-continuous) quantile function of XX, respectively, defined by:

|  |  |  |
| --- | --- | --- |
|  | FX(x):=ℙ(s∈S:X(s)≤x) and FX−1(t):=inf{x∈ℝ|FX(x)≥t}.F\_{X}(x):=\mathbb{P}\left(s\in S:X(s)\leq x\right)\ \ \hbox{ and }\ \ F^{-1}\_{X}\left(t\right):=\inf\Big\{x\in\mathbb{R}\ \Big|\ F\_{X}\left(x\right)\geq t\Big\}. |  |

###### Proposition 3.3.

For a given X∈𝒳X\in\mathcal{X}, the following are equivalent:

1. (1)

   𝐗−1∈𝒜−1C​(𝚠−X)\mathbf{X}\_{-1}\in{\mathcal{A}}\_{-1}^{C}(\mathtt{w}-X).
2. (2)

   There exists some 𝚄∼U​n​i​(0,1)\mathtt{U}\sim Uni(0,1) that is comonotonic with 𝚠−X\mathtt{w}-X, such that Xi=FXi−1​(𝚄)X\_{i}=F\_{X\_{i}}^{-1}(\mathtt{U}), a.s., for each i∈{2,…,n}i\in\{2,\ldots,n\}.

Therefore, for a given 𝐗−1∈𝒜−1C​(𝚠−X)\mathbf{X}\_{-1}\in{\mathcal{A}}\_{-1}^{C}(\mathtt{w}-X), and for each i∈{2,…,n}i\in\{2,\ldots,n\},

|  |  |  |
| --- | --- | --- |
|  | Ui​(Xi)=∫01ui​(FXi−1​(t))​d​t.\displaystyle U\_{i}(X\_{i})=\int\_{0}^{1}u\_{i}\left(F\_{X\_{i}}^{-1}(t)\right)\,\textnormal{d}t. |  |

Consequently,

|  |  |  |
| --- | --- | --- |
|  | Uλ​(𝐗−1)=∫01∑i=2nλi​ui​(FXi−1​(t))​d​t,\displaystyle U^{\lambda}(\mathbf{X}\_{-1})=\int\_{0}^{1}\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}(F\_{X\_{i}}^{-1}(t))\,\textnormal{d}t, |  |

and for each t∈(0,1)t\in(0,1), since quantiles are additive over comonotonic random variables (Föllmer and Schied, [2025](#bib.bib1 "Stochastic Finance: An Introduction in Discrete Time – 5⁢th ed."), Lemma 4.96), we obtain

|  |  |  |
| --- | --- | --- |
|  | ∑i=2nFXi−1​(t)=F𝚠−X−1​(t).\sum\_{i=2}^{n}F\_{X\_{i}}^{-1}(t)=F\_{\mathtt{w}-{X}}^{-1}(t). |  |

The quantile reformulation motivates the following problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | supf2,…,fn∈𝒬∫01∑i=2nλi​ui​(fi​(t))​d​t, such that ​∑i=2nfi=F𝚠−X−1,\displaystyle\sup\_{f\_{2},\ldots,f\_{n}\in\mathcal{Q}}\,\int\_{0}^{1}\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(f\_{i}(t)\right)\,\textnormal{d}t,\quad\text{ such that }\ \sum\_{i=2}^{n}f\_{i}=F\_{\mathtt{w}-{X}}^{-1}, |  | (3.5) |

where 𝒬\mathcal{Q} is the collection of all quantile functions, i.e.,

|  |  |  |
| --- | --- | --- |
|  | 𝒬:={f:(0,1)→ℝ|f​ is nondecreasing and left-continuous}.\mathcal{Q}:=\Big\{f:(0,1)\rightarrow\mathbb{R}\ \Big|f\hbox{ is nondecreasing and left-continuous}\Big\}. |  |

###### Proposition 3.4.

Fix X∈𝒳X\in\mathcal{X} and let 𝚄∼U​n​i​(0,1)\mathtt{U}\sim Uni(0,1) be such that 𝚠−X=F𝚠−X−1​(𝚄)\mathtt{w}-{X}=F\_{\mathtt{w}-{X}}^{-1}(\mathtt{U}), a.s. Then {fi∗}i=2n\{f\_{i}^{\*}\}\_{i=2}^{n} is optimal for ([3.5](#S3.E5 "In 3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) if and only if {fi∗​(𝚄)}i=2n\{f\_{i}^{\*}(\mathtt{U})\}\_{i=2}^{n} is optimal for ([3.4](#S3.E4 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")).

Proposition [3.4](#S3.Thmtheorem4 "Proposition 3.4. ‣ 3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting") implies that solutions to ([3.5](#S3.E5 "In 3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) also yield solutions of the “inner problem” ([3.2](#S3.E2 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")).

### 3.3. Characterization of Efficient Allocations

We can now provide a closed-form characterization of efficient allocations, when one agent is an RDU-maximizer. For each i∈{2,…,n}i\in\{2,\ldots,n\}, let Ii:=(ui′)−1I\_{i}:=\left(u\_{i}^{\prime}\right)^{-1}. For a given vector of welfare weights λ∈ℝ++n−1\lambda\in\mathbb{R}\_{++}^{n-1}, let Jλ:=Iλ−1J\_{\lambda}:=I\_{\lambda}^{-1}, where Iλ​(x):=∑i=2nIi​(xλi)I\_{\lambda}(x):=\sum\_{i=2}^{n}I\_{i}\left(\frac{x}{\lambda\_{i}}\right), for all x≥0x\geq 0.

###### Lemma 3.5.

The (n−1)(n-1)-tuple {fi⋄}i=2n\{f^{\diamond}\_{i}\}\_{i=2}^{n} of the quantile functions below is optimal for Problem ([3.5](#S3.E5 "In 3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | fi⋄:=Ii​(λi−1​Jλ​(F𝚠−X−1)),for all ​i∈{2,…,n}.f^{\diamond}\_{i}:=I\_{i}\Big(\lambda\_{i}^{-1}J\_{\lambda}\big(F^{-1}\_{\mathtt{w}-{X}}\big)\Big),\ \ \text{for all }i\in\{2,\ldots,n\}. |  | (3.6) |

Moreover, if 𝚄∼U​n​i​(0,1)\mathtt{U}\sim Uni(0,1) is such that 𝚠−X=F𝚠−X−1​(𝚄)\mathtt{w}-{X}=F\_{\mathtt{w}-{X}}^{-1}(\mathtt{U}), a.s., then the following holds.

1. (1)

   λi​ui′​(fi⋄​(𝚄))=λj​uj′​(fj⋄​(𝚄))=uλ′​(𝚠−X)\lambda\_{i}\,u\_{i}^{\prime}(f^{\diamond}\_{i}(\mathtt{U}))=\lambda\_{j}\,u\_{j}^{\prime}(f^{\diamond}\_{j}(\mathtt{U}))=u\_{\lambda}^{\prime}(\mathtt{w}-{X}), a.s., all i,j∈{2,…,n}i,j\in\{2,\ldots,n\}.
2. (2)

   {fi⋄​(𝚄)}i=2n\left\{f^{\diamond}\_{i}(\mathtt{U})\right\}\_{i=2}^{n} is optimal for ([3.2](#S3.E2 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) and hence (𝚠−X)(\mathtt{w}-{X})–PO, and fi⋄​(𝚄)=Ii​(Jλ​(𝚠−X)λi)f^{\diamond}\_{i}(\mathtt{U})=I\_{i}\left(\frac{J\_{\lambda}\left(\mathtt{w}-{X}\right)}{\lambda\_{i}}\right), a.s., for each i∈{2,…,n}i\in\{2,\ldots,n\}.
3. (3)

   Additionally,

   |  |  |  |
   | --- | --- | --- |
   |  | Uλ​(𝚠−X)=sup𝐗−1∈𝒜−1​(𝚠−X)∑i=2nλi​Ui​(Xi)=∑i=2nλi​Ui​(fi⋄​(𝚄))=Eℙ​[uλ​(𝚠−X)].\displaystyle U\_{\lambda}(\mathtt{w}-X)=\sup\_{\mathbf{X}\_{-1}\in{\mathcal{A}}\_{-1}(\mathtt{w}-X)}\ \sum\_{i=2}^{n}\lambda\_{i}\,U\_{i}(X\_{i})=\sum\_{i=2}^{n}\lambda\_{i}\,U\_{i}\left(f^{\diamond}\_{i}(\mathtt{U})\right)=E^{\mathbb{P}}[u\_{\lambda}\left(\mathtt{w}-{X}\right)]. |  |

Here, uλu\_{\lambda} is the pointwise aggregate utility given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | uλ​(x):=∑i=2nλi​ui​(Ii​(Jλ​(x)λi)).u\_{\lambda}(x):=\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(I\_{i}\left(\tfrac{J\_{\lambda}(x)}{\lambda\_{i}}\right)\right). |  | (3.7) |

This representative agent formulation helps us now to solve Problem ([3.3](#S3.E3 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). The proof of the following result is similar to Beißner et al. ([2024](#bib.bib10 "(No-)Betting Pareto-Optima under Rank-Dependent Utility")), who examine the two-person case. For completeness, we provide a proof in the Appendix. Recall first that the convex envelope of a function f:[0,1]→ℝf:[0,1]\to\mathbb{R} is the greatest convex function δ:[0,1]→ℝ\delta:[0,1]\to\mathbb{R} that satisfies δ​(x)≤f​(x)\delta\left(x\right)\leq f\left(x\right), for each x∈[0,1]x\in[0,1]. The function δ\delta is affine on the set {x∈[0,1]:δ​(x)<f​(x)}\left\{x\in\left[0,1\right]:\delta(x)<f(x)\right\} (e.g., He et al. ([2017](#bib.bib2 "Rank-Dependent Utility and Risk Taking in Complete Markets"))).

###### Lemma 3.6.

A random variable X1∈𝒳{X}\_{1}\in\mathcal{X} is optimal for Problem ([3.3](#S3.E3 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | X1=mλ−1​(δ′​(𝚄)),a.s.,{X}\_{1}=m^{-1}\_{\lambda}\left(\delta^{\prime}(\mathtt{U})\right),\ \text{a.s.}, |  | (3.8) |

where mλ​(x):=uλ′​(𝚠−x)u1′​(x),∀x∈ℝm\_{\lambda}\left(x\right):=\frac{u\_{\lambda}^{\prime}\left(\mathtt{w}-x\right)}{u\_{1}^{\prime}\left(x\right)},\ \forall x\in\mathbb{R}, and δ\delta is the convex envelope of T~​(t):=1−T​(1−t)\widetilde{T}(t):=1-T(1-t).

Combining lemmata [3.5](#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting") and [3.6](#S3.Thmtheorem6 "Lemma 3.6. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting") leads to the following result.

###### Theorem 3.7.

An allocation 𝐗∈𝒜​(𝚠)\mathbf{X}\in\mathcal{A}(\mathtt{w}) is optimal for Problem ([3.1](#S3.E1 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) if and only if

|  |  |  |
| --- | --- | --- |
|  | X1=mλ−1​(δ′​(𝚄)) and Xi=Ii​(λi−1​Jλ​(𝚠−X1)),for all ​i∈{2,…,n}.\displaystyle{X}\_{1}=m^{-1}\_{\lambda}(\delta^{\prime}(\mathtt{U}))\ \ \hbox{ and }\ \ X\_{i}=I\_{i}\left(\lambda\_{i}^{-1}J\_{\lambda}\left(\mathtt{w}-{X}\_{1}\right)\right),\ \ \text{for all }\,i\in\{2,\ldots,n\}. |  |

If TT is convex, then δ​(t)=t\delta(t)=t, for t∈[0,1]t\in[0,1]. We then immediately recover the special case of full insurance (no-betting).

###### Corollary 3.8.

If TT is convex, then 𝐗\mathbf{X} is PO if and only if it is a full-insurance allocation.

When TT is convex, all agents in the market are risk averse, with common baseline beliefs. In this case, PO allocations are full-insurance allocations, as one would expect. If TT is not concave, then T~\widetilde{T} is not convex, and hence δ\delta will not coincide with T~\widetilde{T}. Moreover δ\delta will be affine on the set

|  |  |  |
| --- | --- | --- |
|  | {p∈[0,1]:δ​(p)<T~​(p)}.\left\{p\in\left[0,1\right]:\delta(p)<\widetilde{T}(p)\right\}. |  |

The probability mass of this event is a gauge of the degree of full insurance within a PO allocation. The probability mass of the complement of this event quantifies the degree of endogenous uncertainty, the principal source of betting in a Pareto-optimal outcome. The following section explores in more detail the impact of introducing an RDU agent, in an otherwise classical EU-economy, on the emergence of betting and the generation of endogenous uncertainty.

## 4. Comparative Statics of Endogenous Uncertainty

We wish to understand how the RDU agent disrupts the full-insurance property of efficient allocations in an EU economy with common beliefs. Theorem [3.7](#S3.Thmtheorem7 "Theorem 3.7. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting") suggests that the derivative of the function δ\delta describes and quantifies how endogenous uncertainty is introduced into the economy by the RDU agent in a Pareto-efficient allocation.

### 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions

For illustration, we consider the broad class of inverse S-shaped and S-shaped distortion functions, with a unique inflection point 1−p¯∈(0,1)1-\bar{p}\in(0,1). A distortion function T:[0,1]→[0,1]T:[0,1]\to[0,1] is inverse S-shaped if it is concave on [0,1−p¯][0,1-\bar{p}] and convex on [1−p¯,1][1-\bar{p},1]. It is S-shaped if it is convex on [0,1−p¯][0,1-\bar{p}] and concave on [1−p¯,1][1-\bar{p},1]. Note that if T~\widetilde{T} denotes the conjugate distortion function given by T~​(t):=1−T​(1−t)\widetilde{T}(t):=1-T(1-t), then T~\widetilde{T} is inverse S-shaped (resp. S-shaped) with inflection point p¯\bar{p} if and only if TT is inverse S-shaped (resp. S-shaped) with inflection point 1−p¯1-\bar{p}.

For this class of distortion functions, the following result gives an explicit characterization of the convex envelope δ\delta of the conjugate distortion function T~\widetilde{T}. This is illustrated in Figure [1](#S4.F1 "Figure 1 ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting").

###### Proposition 4.1.

1. (1)

   Suppose that TT is S-shaped, with an inflection point of 1−p¯∈(0,1)1-\bar{p}\in(0,1), and let

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | p∗:=inf{p∈[0,1):T~′​(p)≥1−T~​(p)1−p}.p^{\*}:=\inf\left\{p\in\left[0,1\right):\widetilde{T}^{\prime}\left(p\right)\geq\frac{1-\widetilde{T}\left(p\right)}{1-p}\right\}. |  | (4.1) |

   Then p∗∈[0,p¯]p^{\*}\in[0,\bar{p}], and the convex envelope δ\delta of T~\widetilde{T} is given by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | δ​(p)={T~​(p)if ​p≤p∗,T~​(p∗)+1−T~​(p∗)1−p∗⋅(p−p∗)otherwise.\qquad\quad\delta(p)\>=\>\begin{cases}\widetilde{T}(p)&\quad\text{if }p\leq p^{\*},\\[4.0pt] \widetilde{T}(p^{\*})+\frac{1-\widetilde{T}(p^{\*})}{1-p^{\*}}\cdot(p-p^{\*})&\quad\text{otherwise.}\end{cases} |  | (4.2) |
2. (2)

   Suppose that TT is inverse S-shaped, with an inflection point of 1−p¯∈(0,1)1-\bar{p}\in(0,1), and let

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | p∗:=sup{p∈[0,1):T~′​(p)≤T~​(p)p}.p^{\*}:=\sup\left\{p\in\left[0,1\right):\widetilde{T}^{\prime}\left(p\right)\leq\frac{\widetilde{T}\left(p\right)}{p}\right\}. |  | (4.3) |

   Then p∗∈[p¯,1]p^{\*}\in[\bar{p},1], and the convex envelope δ\delta of T~\widetilde{T} is given by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | δ​(p)={T~​(p∗)p∗⋅pif ​p≤p∗,T~​(p)otherwise.\delta(p)\>=\>\begin{cases}\frac{\widetilde{T}(p^{\*})}{p^{\*}}\cdot p&\quad\text{if }p\leq p^{\*},\\[6.0pt] \widetilde{T}(p)&\quad\text{otherwise.}\end{cases}\qquad\qquad\>\> |  | (4.4) |

We can now identify the type of betting and the event on which full insurance is prevalent. When TT is inverse S-shaped, δ′\delta^{\prime} is constant on [0,p∗][0,p^{\*}], and hence full insurance occurs on the event {𝚄∈[0,p∗]}\{\mathtt{U}\in[0,p^{\*}]\}; see the right part of Figure [1](#S4.F1 "Figure 1 ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"). On the other hand, for an S-shaped distortion function TT, δ′\delta^{\prime} is constant on [p∗,1][p^{\*},1]. This yields a full-insurance event {𝚄∈[p∗,1]}\{\mathtt{U}\in[p^{\*},1]\}; see the left part of Figure [1](#S4.F1 "Figure 1 ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting").

![Refer to caption](2602.24194v1/x1.jpg)


Figure 1.  Plot of an S-shaped (left) function T~\widetilde{T} and an inverse S-shaped (right) function T~\widetilde{T}, based on Prelec with α=12,2\alpha=\frac{1}{2},2. In both cases the convex envelope (dashed graph) δ\delta with tangent point p∗p^{\*} and inflection point p¯\bar{p} are highlighted.

Additionally, by Corollary [3.8](#S3.Thmtheorem8 "Corollary 3.8. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), if TT is linear (or convex), then efficient allocations are full-insurance allocations. In sum, the probability mass of the full-insurance event, denoted by 𝔽​𝕀\mathbb{FI}, is

|  |  |  |
| --- | --- | --- |
|  | 𝔽​𝕀={p∗if T is inverse S-shaped;1if T is linear (or convex);1−p∗if T is S-shaped.\displaystyle\mathbb{FI}=\left\{\begin{array}[]{l l}p^{\*}&\quad\mbox{if $T$ is inverse S-shaped;}\\[4.0pt] 1&\quad\mbox{if $T$ is linear (or convex);}\\[4.0pt] 1-p^{\*}&\quad\mbox{if $T$ is S-shaped.}\end{array}\right. |  |

In other words, 1−𝔽​𝕀1-\mathbb{FI} captures the degree of endogenous uncertainty.

By Theorem [3.7](#S3.Thmtheorem7 "Theorem 3.7. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), an efficient allocation 𝐗\mathbf{X} consists of random variables that have a mixed distribution, combining a continuous density and a discrete point mass 𝔽​𝕀\mathbb{FI}, corresponding to the full-insurance part of the allocation. The following result provides a characterization of the (defective) probability density function of the endogenous uncertainty in closed form, for the case of inverse S-shaped distortion functions.

###### Proposition 4.2 (Inverse S-Shaped Distortion).

Suppose that the RDU agent’s distortion function TT is inverse S-shaped, and let p∗p^{\*} be as in ([4.3](#S4.E3 "In item 2 ‣ Proposition 4.1. ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). Let I​(x):=mλ−1​(T′​(1−x))I(x):=m\_{\lambda}^{-1}(T^{\prime}(1-x)), where mλ​(x)=uλ′​(𝚠−x)u1′​(x)m\_{\lambda}(x)=\frac{u\_{\lambda}^{\prime}(\mathtt{w}-x)}{u\_{1}^{\prime}(x)}. Let 𝚄∼U​n​i​(0,1)\mathtt{U}\sim Uni(0,1), and let

|  |  |  |
| --- | --- | --- |
|  | X1=mλ−1​(δ′​(𝚄))X\_{1}=m^{-1}\_{\lambda}(\delta^{\prime}(\mathtt{U})) |  |

be the optimal payoff of the RDU agent, where δ\delta is the convex envelope of T~\widetilde{T}. Then X1X\_{1} has a mixed distribution consisting of:

1. (1)

   An atom of mass p∗p^{\*} at the point

   |  |  |  |
   | --- | --- | --- |
   |  | x0:=mλ−1​(T~​(p∗)p∗).x\_{0}:=m\_{\lambda}^{-1}\left(\frac{\widetilde{T}(p^{\*})}{p^{\*}}\right). |  |
2. (2)

   An absolutely continuous component supported on I​([p∗,1])I([p^{\*},1]), with probability density given by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | f1​(x):=−mλ′​(x)T′′​((T′)−1​(mλ​(x))),∀x∈I​([p∗,1]).f\_{1}(x):=\frac{-m\_{\lambda}^{\prime}(x)}{T^{\prime\prime}\left((T^{\prime})^{-1}(m\_{\lambda}(x))\right)},\ \ \forall\,x\in I([p^{\*},1]). |  | (4.6) |

Clearly, since TT is inverse S-shaped, 1−𝔽​𝕀=1−p∗=∫𝐟1​(x)​𝑑x.1-\mathbb{FI}=1-p^{\*}=\int\mathbf{f}\_{1}(x)\,dx. By Theorem [3.7](#S3.Thmtheorem7 "Theorem 3.7. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), we obtain the densities 𝐟j\mathbf{f}\_{j} also for XjX\_{j}, j≥2j\geq 2. Figure [3](#S4.F3 "Figure 3 ‣ 4.3. Closed-Form Solutions for a Prelec RDU Agent ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting") below provides an illustration of the risky part and the full-insurance part.

### 4.2. The Case of a Prelec Probability Weighting Function

Consider the case of Prelec probability weighting functions with parameter α>0\alpha>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | T​(p)=exp⁡(−(−ln⁡(p))α),∀p∈[0,1],T\left(p\right)=\exp(-(-\ln(p))^{\alpha}),\ \ \forall p\,\in[0,1], |  | (4.7) |

introduced and characterized axiomatically by Prelec ([1998](#bib.bib29 "The Probability Weighting Function")).
This function is inverse S-shaped when α∈(0,1)\alpha\in(0,1), linear when α=1\alpha=1, and S-shaped when α>1\alpha>1. It then follows that T~\widetilde{T} from Lemma [3.6](#S3.Thmtheorem6 "Lemma 3.6. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting") is given by
T~​(p)=1−exp⁡(−(−ln⁡(1−p))α).\widetilde{T}(p)=1-\exp(-(-\ln(1-p))^{\alpha}). Moreover, if TT is (inverse-) S-shaped, then so is T~\widetilde{T}. Hence, if α∈(0,1)\alpha\in(0,1), i.e., inverse S-shaped, then δ\delta has the form in ([4.4](#S4.E4 "In item 2 ‣ Proposition 4.1. ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting")); and if α>1\alpha>1 then δ\delta has the form in ([4.2](#S4.E2 "In item 1 ‣ Proposition 4.1. ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting")); see again Figure [1](#S4.F1 "Figure 1 ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting").

Based on the unique tangent point p∗=p∗​(α)p^{\*}=p^{\*}(\alpha) where the convex envelope binds, we can now identify the magnitude of the 𝔽​𝕀\mathbb{FI} event depending on the parameter α\alpha. We have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔽​𝕀​(α)\displaystyle\mathbb{FI}(\alpha) | =\displaystyle= | {p∗​(α),if ​α<1,1,if ​α=1,1−p∗​(α),if ​α>1,\displaystyle\begin{cases}p^{\*}(\alpha),&\quad\text{if }\alpha<1,\\[2.0pt] 1,&\quad\text{if }\alpha=1,\\[2.0pt] 1-p^{\*}(\alpha),&\quad\text{if }\alpha>1,\end{cases}\qquad\qquad\qquad\qquad\qquad\qquad |  |

where p∗​(α)p^{\*}(\alpha) can be derived from the following result.

###### Corollary 4.3.

Let the RDU agent have a Prelec weighting function TT.

1. (1)

   If TT is SS-shaped, i.e., α>1\alpha>1, then
   p∗​(α)=1−exp⁡(−α−1α−1).p^{\*}(\alpha)=1-\exp(-{\alpha}^{-\frac{1}{\alpha-1}}).
2. (2)

   If TT is inverse SS-shaped, i.e., α<1\alpha<1, then
   p∗​(α)=1−exp⁡(−x),p^{\*}(\alpha)=1-\exp(-x), where xx is the unique solution of the equation
   x=ln(αxα−1ex(1−e−x)+1)1αx=\ln\left(\alpha x^{\alpha-1}e^{x}(1-e^{-x})+1\right)^{\frac{1}{\alpha}}.

This result is illustrated in Figure [2](#S4.F2 "Figure 2 ‣ 4.2. The Case of a Prelec Probability Weighting Function ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"). We observe a counter-intuitive implication of the Prelec weighting functions. Apart from the two jumps around α=1\alpha=1, we observe, for the inverse S-shaped region, that an increase in the nonlinearity leads to an increase in the probability mass of the full-insurance event.
This pattern also holds true for the inverse S-shaped function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | T​(p)=pγ(pγ+(1−p)γ)1/γ,∀p∈[0,1],T\left(p\right)=\frac{p^{\gamma}}{(p^{\gamma}+(1-p)^{\gamma})^{1/\gamma}},\ \forall p\in[0,1], |  | (4.8) |

which is introduced by Tversky and Kahneman ([1992](#bib.bib28 "Advances in prospect theory: cumulative representation of uncertainty")), and is inverse S shaped for γ∈(0.279,1)\gamma\in(0.279,1), as per Rieger and Wang ([2006](#bib.bib13 "Cumulative Prospect Theory and the St. Petersburg Paradox")).
In Section 4.4, we consider another class of weighting functions, introduced in Bleichrodt et al. ([2023](#bib.bib15 "Testing hurwicz expected utility")) with different comparative statics of 𝔽​𝕀\mathbb{FI}.

![Refer to caption](2602.24194v1/x2.png)

![Refer to caption](2602.24194v1/x3.png)

Figure 2.  Figure (a) shows the probability of the full-insurance event 𝔽​𝕀​(α)\mathbb{FI(\alpha)} as a function of α∈[0,10]\alpha\in[0,10], for the Prelec weighting function. Figure (b) shows the probability of the full-insurance event 𝔽​𝕀=p∗\mathbb{FI}=p^{\*} as a function of g​a​m​m​a∈[0,10]gamma\in[0,10], for the Tversky-Kahneman weighting function, defined in ([4.8](#S4.E8 "In 4.2. The Case of a Prelec Probability Weighting Function ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting")).

### 4.3. Closed-Form Solutions for a Prelec RDU Agent

In the following, we present closed-form solutions for Pareto efficiency. Consider therefore a more specific setup with aggregate wealth 𝚠=0\mathtt{w}=0 and CARA utility for each agent i∈{1,2,…,n}i\in\{1,2,\ldots,n\} given by

|  |  |  |
| --- | --- | --- |
|  | ui​(x)=−1βi​exp⁡(−βi​x), with ​βi>0.u\_{i}(x)=-\frac{1}{\beta\_{i}}\exp({-\beta\_{i}x}),\text{ with }\beta\_{i}>0. |  |

###### Corollary 4.4.

Let β¯:=(β2−1+⋯+βn−1)−1\overline{\beta}:=(\beta\_{2}^{-1}+\cdots+\beta\_{n}^{-1})^{-1}, and define the rescaled risk preference parameters β¯j:=βjβ¯>0\overline{\beta}\_{j}:=\frac{\beta\_{j}}{\overline{\beta}}>0 , for each jj. Let I​(x):=ln⁡(δ′​(x))I(x):=\ln(\delta^{\prime}(x)) and let ln⁡(∑i=2nλi)\ln(\sum\_{i=2}^{n}\lambda\_{i}) be a deterministic side payment. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | X1=1β1+β¯​(I​(𝚄)−ln⁡(∑i=2nλi)),X\_{1}=\frac{1}{\beta\_{1}+\overline{\beta}}\Big(I\left(\mathtt{U}\right)-\ln(\sum\_{i=2}^{n}\lambda\_{i})\Big),\qquad\qquad\qquad\qquad\qquad\qquad\quad\qquad |  | (4.9) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | andXj=−1β¯j⋅1β1+β¯​I​(𝚄)⏟Xj∼​ random +1βj​(ln⁡(λj)−∑k=2n1β¯k​ln⁡(λk))⏟Xj∙​ side payment ,j=2,3,…,n.\text{and}\quad\qquad X\_{j}=\underbrace{-\frac{1}{\overline{\beta}\_{j}}\cdot\frac{1}{\beta\_{1}+\overline{\beta}}\ I\left(\mathtt{U}\right)}\_{X^{\sim}\_{j}\>\text{ random }}\>+\>\underbrace{\frac{1}{\beta\_{j}}\Big(\ln(\lambda\_{j})-\sum\_{k=2}^{n}\frac{1}{\overline{\beta}\_{k}}\ln(\lambda\_{k})\Big)}\_{X\_{j}^{\bullet}\>\text{ side payment }},\quad j=2,3,\ldots,n. |  | (4.10) |

This result delivers an explicit decomposition of optimal consumption into an atomless random variable Xj∼X^{\sim}\_{j} and an atom Xj∙X^{\bullet}\_{j}. Moreover, the role of the vector λ\lambda is to determine the zero-sum deterministic side payments to the agents. An increase in the aggregate risk aversion β1+β¯\beta\_{1}+\overline{\beta} moves mλ−1m\_{\lambda}^{-1} from Lemma [3.6](#S3.Thmtheorem6 "Lemma 3.6. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting") closer to the xx-axis, and thus PO allocations are in turn closer to zero.

![Refer to caption](2602.24194v1/x4.png)


Figure 3.  Baseline case density function, with α=0.8\alpha=0.8, β1=0.5=β2\beta\_{1}=0.5=\beta\_{2}, and β3=2\beta\_{3}=2.

Figure [3](#S4.F3 "Figure 3 ‣ 4.3. Closed-Form Solutions for a Prelec RDU Agent ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting") illustrates the density parts

|  |  |  |
| --- | --- | --- |
|  | (𝚏1α,𝚏2α,𝚏3α)(\mathtt{f}^{\alpha}\_{1},\mathtt{f}^{\alpha}\_{2},\mathtt{f}^{\alpha}\_{3}) |  |

of the optimal allocations, when the RDU agent has an inverse S-shaped distortion function with α=0.8\alpha=0.8. λ2\lambda\_{2} and λ3\lambda\_{3} are chosen to guarantee no side payments, i.e.,

|  |  |  |
| --- | --- | --- |
|  | X1=1β1+β¯​I​(𝚄), and Xj=−β¯βj⋅X1,j=2,3.X\_{1}=\frac{1}{\beta\_{1}+\overline{\beta}}\ I(\mathtt{U}),\quad\textnormal{ and }\quad X\_{j}=-\frac{\overline{\beta}}{\beta\_{j}}\cdot X\_{1},\quad j=2,3. |  |

This implies that λ2+λ3=1\lambda\_{2}+\lambda\_{3}=1, and β2−β¯β2​ln⁡(λ2)=β¯β3​ln⁡(λ3)\frac{\beta\_{2}-\overline{\beta}}{\beta\_{2}}\ \ln(\lambda\_{2})=\frac{\overline{\beta}}{\beta\_{3}}\ \ln(\lambda\_{3}).
This is without loss, as any zero-sum side payments can be obtained by specific choices of λ\lambda. For the exponential utilities, we assume that β1=12=β2\beta\_{1}=\frac{1}{2}=\beta\_{2} and β3=2\beta\_{3}=2. For λ2+λ3=1\lambda\_{2}+\lambda\_{3}=1, ln⁡(λ2+λ3)=0\ln(\lambda\_{2}+\lambda\_{3})=0 and thus the side payment to Agent 1 is equal to zero, implying that X1=1β1+β¯​I​(𝚄)X\_{1}=\frac{1}{\beta\_{1}+\overline{\beta}}\ I(\mathtt{U}). Specifically, on the interval [0,p∗]≈[0,910][0,p^{\*}]\approx[0,\frac{9}{10}], PO allocations are full-insurance allocations, which holds true because δ\delta is linear on the domain [0,p∗][0,p^{\*}], as in the left part of Figure [1](#S4.F1 "Figure 1 ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"). This finding holds true for any inverse S-shaped distortion function T~\widetilde{T} (see equation ([4.4](#S4.E4 "In item 2 ‣ Proposition 4.1. ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"))). Moreover, βi\beta\_{i} is a factor that is multiplied with the risk exposure: smaller values of βi\beta\_{i} lead to larger absolute values of the risk exposure. Moreover, for this RDU agent, the distribution of X1X\_{1} is positively (right-)skewed, due to the over-weighting of small probabilities (and absence of loss aversion). The other two EU agents show a negative skewness in their optimal payoffs X2X\_{2} and X3X\_{3}, due to risk aversion and no over-weighting of small probabilities.

### 4.4. Examples

The following four subsections present some more perspective on the role of the RDU agent in the structure of sharing rules: apart from the risk preference parameters (β1,β2,β3)(\beta\_{1},\beta\_{2},\beta\_{3}), we modify the parameter of the Prelec weighting function α\alpha. Each example captures a three-agent economy.
We can identify optimal consumption in closed form for the RDU agent, as in ([4.9](#S4.E9 "In Corollary 4.4. ‣ 4.3. Closed-Form Solutions for a Prelec RDU Agent ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting")), and also capture the underlying probability density function.

#### 4.4.1. Robustness Check

We begin with some sensitivity analysis of the main parameter choices. Figure [4](#S4.F4 "Figure 4 ‣ 4.4.1. Robustness Check ‣ 4.4. Examples ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting")(a) shows the case where β3\beta\_{3} is lowered to 0.7. Due to a lower risk aversion of Agent 3, we find that Agent 3 obtains a larger risk exposure in the tail (in absolute value), and that Agent 1 is the main counterparty of this larger risk exposure.
Figure [4](#S4.F4 "Figure 4 ‣ 4.4.1. Robustness Check ‣ 4.4. Examples ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting")(b) shows that if β1\beta\_{1} is increased to 2, the risk exposures for all agents, captured by the variance, become closer to 0 due to the larger risk aversion of the RDU agent.

![Refer to caption](2602.24194v1/x5.png)

![Refer to caption](2602.24194v1/x6.png)

Figure 4. Robustness: (a) Case with β1=0.5,β2=0.5\beta\_{1}=0.5,\beta\_{2}=0.5, β3=0.7\beta\_{3}=0.7, and α=0.8\alpha=0.8.
(b) Case with β1=2=β3\beta\_{1}=2=\beta\_{3}, β2=0.5\beta\_{2}=0.5 and α=0.8\alpha=0.8.

#### 4.4.2. Concave and Convex Case

Next, we illustrate the risk allocations when we have a concave or convex probability weighting function. We fix α=0.5\alpha=0.5, and re-adjust the distortion function to make it concave/convex. That is, we use the convex T~1​(p)=T~​(p/4)T~​(1/4)\widetilde{T}\_{1}(p)=\frac{\widetilde{T}(p/4)}{\widetilde{T}(1/4)} and the concave T2​(p)=T​(p/4)T​(1/4)T\_{2}(p)=\frac{T(p/4)}{T(1/4)}. The corresponding risk allocations are shown in Figure [5](#S4.F5 "Figure 5 ‣ 4.4.2. Concave and Convex Case ‣ 4.4. Examples ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"). Convex distortion functions lead to full-insurance allocations, as per Corollary [3.8](#S3.Thmtheorem8 "Corollary 3.8. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"). Moreover, concave distortion functions lead to δ=T~2\delta=\widetilde{T}\_{2}, and thus to strictly monotonic functions of UU. This implies that the risk allocation does not contain an atom and there is no full-insurance event, i.e., 𝔽​𝕀=0\mathbb{FI}=0.

![Refer to caption](2602.24194v1/x7.png)

![Refer to caption](2602.24194v1/x8.png)

Figure 5. (a) Heavy betting with concave T2T\_{2}. (b) Full insurance with convex T1T\_{1}.

#### 4.4.3. From S-Shaped to Inverse S-Shaped

Figure [6](#S4.F6 "Figure 6 ‣ 4.4.3. From S-Shaped to Inverse S-Shaped ‣ 4.4. Examples ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting") shows the optimal risk allocations when α=1.2\alpha=1.2. Since α>1\alpha>1, the corresponding probability weighting function is S-shaped. We see that there is a switch in the risk allocations: in the atomless component, the density of Agents 2 and 3, which was concentrated in the left tail when α<1\alpha<1 (Figure [3](#S4.F3 "Figure 3 ‣ 4.3. Closed-Form Solutions for a Prelec RDU Agent ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting")), is now concentrated in the right tail when α>1\alpha>1 (Figure [6](#S4.F6 "Figure 6 ‣ 4.4.3. From S-Shaped to Inverse S-Shaped ‣ 4.4. Examples ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). The risk allocation can be viewed as a swap of densities 𝚏1α\mathtt{f}^{\alpha}\_{1} and (𝚏2α,𝚏3α)(\mathtt{f}^{\alpha}\_{2},\mathtt{f}^{\alpha}\_{3}) in the atomless component, and this swap changes the role of Agent 1 from the “buyer” of a bet (a small chance of large gains) to a “seller” of a bet (a small chance of large losses). In fact, this phenomenon occurs if we change from α<1\alpha<1 (inverse S-shaped) to α>1\alpha>1 (S-shaped).

![Refer to caption](2602.24194v1/x9.png)


Figure 6. S-shaped weighting function with β1=β2=0.5\beta\_{1}=\beta\_{2}=0.5, β3=2\beta\_{3}=2, α=1.2\alpha=1.2.

This also clarifies that an S-shaped probability weighting function creates more “unpleasant” left-tail uncertainty for the RDU agent, whereas she receives a positive payoff in the full-insurance event. As for the EU agents, the right-tail uncertainty is associated with a negative payoff in the full-insurance event, as shown in Figure [6](#S4.F6 "Figure 6 ‣ 4.4.3. From S-Shaped to Inverse S-Shaped ‣ 4.4. Examples ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"). In view of Figure [3](#S4.F3 "Figure 3 ‣ 4.3. Closed-Form Solutions for a Prelec RDU Agent ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting") with an inverse S-shaped RDU agent, the sign of the skewness flips for each agent.

### 4.5. Alternative Weighting Function

Thus far, we have discussed the emergence of endogenous uncertainty under the assumption of a Prelec-type weighting function. In this subsection, we discuss the class of weighting functions

|  |  |  |  |
| --- | --- | --- | --- |
|  | T​(p)=γ​(1−κ)​p(1+κ)​(1−p)+(1−κ)​p+(1−γ)​(1+κ)​p(1−κ)​(1−p)+(1+κ)​p,T(p)=\gamma\ \frac{(1-\kappa)p}{(1+\kappa)(1-p)+(1-\kappa)p}\,+\,(1-\gamma)\ \frac{(1+\kappa)p}{(1-\kappa)(1-p)+(1+\kappa)p}, |  | (4.11) |

induced in the context of Hurwicz Expected Utility (HEU) by Bleichrodt et al. ([2023](#bib.bib15 "Testing hurwicz expected utility")). The parameter γ∈[0,1]\gamma\in[0,1] is an ambiguity index, with γ=1\gamma=1 corresponding to ambiguity aversion and γ=0\gamma=0 to ambiguity-seeking behavior. The parameter κ∈[0,1]\kappa\in[0,1] captures ambiguity perception, with larger values of κ\kappa indicating greater perceived ambiguity. The probability weighting function TT in ([4.11](#S4.E11 "In 4.5. Alternative Weighting Function ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) is a weighted average of a convex and a concave function, and it can therefore exhibit an inverse S shape.

![Refer to caption](2602.24194v1/x10.png)


Figure 7.  The case of Hurwicz expected utility; the probability of the discrete full-insurance event 𝔽​𝕀\mathbb{FI} as a function of γ∈[0,1]\gamma\in[0,1], for various values of κ\kappa.

Figure [7](#S4.F7 "Figure 7 ‣ 4.5. Alternative Weighting Function ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), as a counterpart of Figure [2](#S4.F2 "Figure 2 ‣ 4.2. The Case of a Prelec Probability Weighting Function ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting") for the Prelec case, displays the probability of the discrete full-insurance event as a function
of γ\gamma, for various values of κ\kappa. We find that as γ\gamma increases, implying more ambiguity aversion, the probability of the discrete full-insurance event increases, except when κ\kappa is small (low perceived ambiguity). Moreover, for larger perceived ambiguity, this effect is stronger for small γ\gamma, but increases more slowly for larger γ\gamma.

![Refer to caption](2602.24194v1/x11.png)


Figure 8.  Risk allocations with HEU; we set γ=κ=0.5\gamma=\kappa=0.5, β1=β2=0.5\beta\_{1}=\beta\_{2}=0.5 and β3=2\beta\_{3}=2.

For the risk allocation, we provide an example in Figure [8](#S4.F8 "Figure 8 ‣ 4.5. Alternative Weighting Function ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"). In particular, with γ=κ=0.5\gamma=\kappa=0.5, we observe that the probability weighting function is inverse S-shaped, and p∗≈0.768p^{\*}\approx 0.768. That is, the probability of the full-insurance event is approximately 76.8%76.8\%. Moreover, because T~′​(1−)=1.75\widetilde{T}^{\prime}(1-)=1.75 is finite, we find an abrupt jump in the density function to/from zero in the tail. This is in contrast to Prelec probability weighting functions. Since T~′​(p∗)≈0.95\widetilde{T}^{\prime}(p^{\*})\approx 0.95 and T~=δ\widetilde{T}=\delta on [p∗,1][p^{\*},1], it follows that the distribution of ln⁡(δ′​(U))\ln(\delta^{\prime}(U)) is supported on [−0.05,0.56][-0.05,0.56]. By Corollary [4.4](#S4.Thmtheorem4 "Corollary 4.4. ‣ 4.3. Closed-Form Solutions for a Prelec RDU Agent ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting") and as displayed in Figure [8](#S4.F8 "Figure 8 ‣ 4.5. Alternative Weighting Function ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), the continuous density component of X1X\_{1} has a range of width (0.56+0.05)/(β1+β¯)≈0.68(0.56+0.05)/(\beta\_{1}+\bar{\beta})\approx 0.68. The continuous density component of X2X\_{2} has a range of width β¯β2​0.68=0.54\frac{\bar{\beta}}{\beta\_{2}}0.68=0.54, and the continuous density component of X3X\_{3} has the smallest range of width β¯β3​0.68=0.135\frac{\bar{\beta}}{\beta\_{3}}0.68=0.135, due to larger risk aversion.

### 4.6. Side Payments

In the context of side payments, the Kaldor-Hicks criterion (e.g., Kaldor ([1939](#bib.bib17 "Welfare propositions of economics and interpersonal comparisons of utility"))) offers a useful efficiency benchmark. An alternative allocation is a potential Pareto improvement if there exists a feasible transfer scheme that compensates all agents who lose from the change. In our framework, the surplus gained by agents advantaged through RDU-induced probability distortions could hypothetically finance such compensation, implying that the resulting allocation satisfies the Kaldor-Hicks criterion even without the transfers being implemented.

We next display the certainty equivalents for the three agents as a function of α\alpha from ([4.7](#S4.E7 "In 4.2. The Case of a Prelec Probability Weighting Function ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). We start with the setting of Figure [3](#S4.F3 "Figure 3 ‣ 4.3. Closed-Form Solutions for a Prelec RDU Agent ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"). For Agent 1, the certainty equivalent of any payoff XX with cumulative distribution function FXF\_{X} is given by:

|  |  |  |
| --- | --- | --- |
|  | C​E1​(X):=u1−1​(∫01u1​(FX−1​(p))​T~′​(p)​d​p),CE\_{1}(X):=u\_{1}^{-1}\left(\displaystyle\int\_{0}^{1}u\_{1}\left(F\_{X}^{-1}(p)\right)\widetilde{T}^{\prime}(p)\,\textnormal{d}p\right),\qquad\quad |  |

and for the other agents it is given by:

|  |  |  |
| --- | --- | --- |
|  | C​Ei​(X):=ui−1​(∫01ui​(FX−1​(p))​d​p),i=2,…,n.CE\_{i}(X):=u\_{i}^{-1}\left(\displaystyle\int\_{0}^{1}u\_{i}\left(F\_{X}^{-1}(p)\right)\,\textnormal{d}p\right),\quad i=2,\ldots,n. |  |

By construction, certainty equivalents satisfy C​Ej​(c)=cCE\_{j}(c)=c, for c∈ℝc\in\mathbb{R}. Moreover, for exponential utilities, C​EjCE\_{j} is cash additive: C​Ej​(X+c)=C​Ej​(X)+cCE\_{j}(X+c)=CE\_{j}(X)+c, and it is also called an entropic risk measure if T=i​dT=id. Here, we assume that all initial endowments are 0. By Corollary [3.8](#S3.Thmtheorem8 "Corollary 3.8. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), if T=i​dT=id, then (X1,X2,X3)(X\_{1},X\_{2},X\_{3}) is a full-insurance allocation, and we have ∑i=1nC​Ei​(Xi)=𝚠=0\sum\_{i=1}^{n}CE\_{i}(X\_{i})=\mathtt{w}=0, so that a positive certainty equivalent corresponds to a strict improvement over no trading. That is, if T≠i​dT\neq id, then C​E=∑iC​Ei​(Xi)>0CE=\sum\_{i}CE\_{i}(X\_{i})>0.

![Refer to caption](2602.24194v1/x12.png)


(a) The individual certainty equivalents
  
C​Ei​(Xi)CE\_{i}(X\_{i}) of the three agents, for varying α\alpha.

![Refer to caption](2602.24194v1/x13.png)


(b) The aggregate certainty equivalents
  
   C​ECE, for varying α\alpha.

Figure 9. Here, we use β1=12=β2\beta\_{1}=\frac{1}{2}=\beta\_{2}, and β3=2\beta\_{3}=2.

We show the certainty equivalents for our baseline example with various choices of α\alpha in Figure [9(a)](#S4.F9.sf1 "In Figure 9 ‣ 4.6. Side Payments ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"). Notice that the certainty equivalents are equal to 0 when α=1\alpha=1. In this case, there are no risk exposures, corresponding to no betting. Just like in Beißner et al. ([2024](#bib.bib10 "(No-)Betting Pareto-Optima under Rank-Dependent Utility")), we can argue that zero-sum deterministic cash transfers (side payments) can be arbitrarily selected, and thus a negative value of C​E1​(X1)CE\_{1}(X\_{1}) for the RDU agent 1 when α>1.5\alpha>1.5 can be increased to a positive value via side payments from the other agents. Thus, only the sum of certainty equivalents is relevant, and a positive sum of certainty equivalents means that all agents may be better off from betting in combination with some appropriately selected side payments. We display the sum of certainty equivalents in Figure [9(b)](#S4.F9.sf2 "In Figure 9 ‣ 4.6. Side Payments ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
We see that for α\alpha further away from 1, the sum of certainty equivalents becomes larger, which indicates that betting is attractive due to the probability distortion of the RDU agent.

## 5. Nudging the RDU agent

Consider an economy populated by one RDU agent and one EU agent with a given distortion function TT.333By Lemma [3.5](#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), this single EU agent can be interpreted as the representative agent for the n−1n-1 EU agents in the market, endowed with the aggregate utility function uλu\_{\lambda}. As shown in Section [3](#S3 "3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting") and Section [4](#S4 "4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), the degree of nonlinearity of the RDU agent’s distortion function directly impacts the degree of non-idiosyncratic risk within any efficient allocation.

We assume that a sophisticated social planner is aware of the deterministic aggregate endowment 𝚠\mathtt{w}, and wishes to control the level of non-idiosyncratic risk within efficient allocations resulting from the RDU agent’s probability weighting. The social planner can exert a costly effort to nudge the RDU agent, and this nudging brings the RDU agent’s probability weighting function closer to linearity. The effort MM is exerted by the social planner, at a monetary cost M>0M>0, which reduces the aggregate endowment to 𝚠−M\mathtt{w}-M. This impacts the curvature of the “nudged” weighting function TMT\_{M}.444One illustrative real-world example is to *educate* an RDU agent in probability theory and statistics. In this perspective, TT models a *lack of information*, rather than a probabilistic form of “risk aversion.” Meanwhile, EU agents behave much like econometricians, and the social planner aspires to elevate the RDU agent to the same level of expertise. However, this “education” or “nudging” comes at a cost, which explains why it does not occur automatically.

The welfare maximization problem with nudging then reads as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxM∈[0,𝚠]​supX1+X2=𝚠−MU1​(X1,TM)+U2​(X2)⏟=⁣:W​(X1,M),\displaystyle\max\_{M\in[0,\mathtt{w}]}\ \sup\_{X\_{1}+X\_{2}=\mathtt{w}-M}\ \underbrace{U\_{1}(X\_{1},T\_{M})+U\_{2}(X\_{2})}\_{=:W(X\_{1},M)}, |  | (5.1) |

with a “nudged” weighting function TM:[0,1]→[0,1]T\_{M}:[0,1]\to[0,1] that depends on the effort level MM and is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | TM​(p):=(1−f​(M))​T​(p)+f​(M)​p.\displaystyle T\_{M}(p):=(1-f(M))\,T(p)+f(M)\,p. |  | (5.2) |

We assume that the function ff is a strictly increasing and concave function f:[0,𝚠]→[0,1]f:[0,\mathtt{w}]\to[0,1] that satisfies the following:

1. (1)

   The outer problem is well-defined.
2. (2)

   If M>M′M>M^{\prime} then TMT\_{M} is more linear than TM′T\_{M^{\prime}}.
3. (3)

   f​(0)=0f(0)=0, so that T0=TT\_{0}=T.

In the numerical illustration of Example [5.6](#S5.Thmtheorem6 "Example 5.6. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), we adopt the specific functional form
f​(M)=1−(1−M)kf(M)=1-(1-M)^{k}, for k>1k>1, so that higher values of kk correspond to stronger curvature, i.e., a faster convergence of TMT\_{M} toward linearity as MM increases.

###### Example 5.1.

We continue studying the case with a Prelec weighting function, n=3n=3, and exponential utilities. Thus, we now use two EU agents, which can be summarized as a representative EU agent via Lemma [3.5](#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
Consider the case in which α=0.4\alpha=0.4, β1=12=β2\beta\_{1}=\frac{1}{2}=\beta\_{2}, β3=2\beta\_{3}=2.
In Figure [10](#S5.F10 "Figure 10 ‣ Example 5.1. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), we illustrate how the optimal allocation changes with MM. Specifically, we plot the atom and the atomless density 𝚏1M\mathtt{f}^{M}\_{1} of X1MX^{M}\_{1}. By Corollary [4.4](#S4.Thmtheorem4 "Corollary 4.4. ‣ 4.3. Closed-Form Solutions for a Prelec RDU Agent ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), this distribution of X1MX^{M}\_{1} coincides with the one obtained in the three-agent economy when the two EU agents are aggregated into a single representative EU agent with risk-aversion parameter β¯=0.4\bar{\beta}=0.4.

![Refer to caption](2602.24194v1/x14.png)


Figure 10. Examples of the density 𝚏1M\mathtt{f}^{M}\_{1} for various choices of f​(M)f(M) under the base case. We set f​(M)=0,0.25,0.5,0.75,1f(M)=0,0.25,0.5,0.75,1.

We find that the atom becomes more likely when f​(M)f(M) increases, and moreover, the densities become lower as f​(M)f(M) takes lower values. This means that increases in f​(M)f(M) make the optimal risk allocation “closer” to the full insurance allocation.

The following result gives a handy representation of the RDU functional after nudging at level MM.

###### Lemma 5.2.

The RDU functional with distortion function TMT\_{M} from ([5.2](#S5.E2 "In 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | U1​(X,TM)=[1−f​(M)]​U1​(X,T)+f​(M)​∫u1​(X)​d​ℙ.\displaystyle U\_{1}(X,T\_{M})=\left[1-f(M)\right]\,U\_{1}(X,T)+f(M)\,\int u\_{1}(X)\,\textnormal{d}\mathbb{P}. |  | (5.3) |

These results highlight the functional dependency of the planer’s effort level MM in Problem ([5.1](#S5.E1 "In 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) with value function M↦V​(M)M\mapsto V(M). We can apply all insights from Sections 2-4.
In particular V​(M)V(M) can be analyzed in a pointwise manner. In view of Lemma [5.2](#S5.Thmtheorem2 "Lemma 5.2. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), the social planner is assigning a total welfare to the RDU agent that consists of two parts: (i) a fraction 1−f​(M)1-f(M) coming from the prior preferences of the RDU agent; and (ii) a fraction f​(M)f(M) coming from discarding the probability weighting of the RDU agent and treating this agent as an EU-maximizer.

In this case, the characterization in the economy with an RDU having distortion TMT\_{M} follows again by Theorem [3.7](#S3.Thmtheorem7 "Theorem 3.7. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"). However, we need to replace δ\delta by δM\delta\_{M}, the convex envelope of T~M\widetilde{T}\_{M}.
The following result shows that the modified convexification depends in an affine linear way on ff.

###### Lemma 5.3.

For TMT\_{M} as in ([5.2](#S5.E2 "In 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting")), we have δM​(p)=δ​(p)−f​(M)​(δ​(p)−p)\delta\_{M}\left(p\right)=\delta(p)-f(M)(\delta\left(p\right)-p).

It directly follows that δM′​(p)=δ′​(p)−f​(M)​(δ′​(p)−1)\delta^{\prime}\_{M}\left(p\right)=\delta^{\prime}(p)-f(M)(\delta^{\prime}(p)-1).
Lemma [5.3](#S5.Thmtheorem3 "Lemma 5.3. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting") gives a useful decomposition of δM\delta\_{M}. In view of the optimal sharing rule under TMT\_{M}, the resulting properties of M↦δM′M\mapsto\delta\_{M}^{\prime} clarify the relationship between δ′\delta^{\prime} and δM′\delta^{\prime}\_{M}.
For instance, if TT is inverse S-shaped, then by Proposition [4.1](#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting")(1) there exists a unique tangent point pM∗∈(0,p¯)p\_{M}^{\*}\in\left(0,\bar{p}\right) such that δM\delta\_{M} is given by

|  |  |  |
| --- | --- | --- |
|  | δM​(p)={T~M​(pM∗)pM∗⋅pif p<pM∗;T~M​(p)otherwise. \delta\_{M}\left(p\right)=\left\{\begin{array}[]{l l}\frac{\widetilde{T}\_{M}\left(p^{\*}\_{M}\right)}{p^{\*}\_{M}}\cdot p&\quad\mbox{if $p<p^{\*}\_{M}$;}\\ \widetilde{T}\_{M}\left(p\right)&\quad\mbox{otherwise. }\\ \end{array}\right. |  |

If TT is S-shaped, the argument is similar (see Proposition [4.1](#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting")(2)).

We now formulate for every MM the optimal allocation in closed form.
We focus first on the inner part of Problem ([5.1](#S5.E1 "In 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting")), the weighted-sum risk-allocation problem under given MM:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(M)=supX1+X2=𝚠−M{U1​(X1,TM)+λ2​U2​(X2)},λ2>0.V(M)=\sup\_{X\_{1}+X\_{2}=\mathtt{w}-M}\,\Big\{U\_{1}(X\_{1},T\_{M})+\lambda\_{2}\,U\_{2}(X\_{2})\Big\},\ \quad\lambda\_{2}>0. |  | (5.4) |

Moreover, we show the (smooth) sensitivity of the optimal solution with respect to the effort level MM in closed form.

###### Proposition 5.4.

1. (1)

   For a given effort level MM, 𝐗M=(xM​(𝚄),𝚠−M−xM​(𝚄))\mathbf{X}^{M}=(x\_{M}(\mathtt{U}),\mathtt{w}-M-x\_{M}(\mathtt{U})) solves Problem ([5.4](#S5.E4 "In 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) if and only if

   |  |  |  |
   | --- | --- | --- |
   |  | xM​(𝚄)=mλ2−1​(δ′​(𝚄)−f​(M)​(δ′​(𝚄)−1)),\displaystyle x\_{M}(\mathtt{U})=m^{-1}\_{\lambda\_{2}}\Big(\delta^{\prime}(\mathtt{U})-f(M)(\delta^{\prime}(\mathtt{U})-1)\Big), |  |

   where mλ2​(x):=λ2​u2′​(𝚠−M−x)u1′​(x)m\_{\lambda\_{2}}(x):=\lambda\_{2}\,\frac{u\_{2}^{\prime}\left(\mathtt{w}-M-x\right)}{u\_{1}^{\prime}\left(x\right)}.
2. (2)

   Moreover, the optimal allocation depends smoothly on the effort level MM:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | xp′​(M):=∂∂M​XM​(p)=−f′​(M)​(δ′​(p)−1)+λ2​u2′′​(𝚠−M−mλ2−1​(δ′​(p)−f​(M)​(δ′​(p)−1)))u1′​(mλ2−1​(δ′​(p)−f​(M)​(δ′​(p)−1)))Λ​(δ′​(p)−f​(M)​(δ′​(p)−1)),\begin{split}x^{\prime}\_{p}(M)&:=\frac{\partial}{\partial M}X\_{M}(p)\\ &=\frac{-f^{\prime}(M)\left(\delta^{\prime}(p)-1\right)+\lambda\_{2}\,\dfrac{u\_{2}^{\prime\prime}\left(\mathtt{w}-M-m\_{\lambda\_{2}}^{-1}\left(\delta^{\prime}(p)-f(M)\left(\delta^{\prime}(p)-1\right)\right)\right)}{u\_{1}^{\prime}\left(m\_{\lambda\_{2}}^{-1}\left(\delta^{\prime}(p)-f(M)\left(\delta^{\prime}(p)-1\right)\right)\right)}}{\Lambda\left(\delta^{\prime}(p)-f(M)\left(\delta^{\prime}(p)-1\right)\right)},\end{split} |  | (5.5) |

   where

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Λ​(x)\displaystyle\Lambda(x) | :=dd​x​mλ2​(mλ2−1​(x))\displaystyle:=\frac{d}{dx}m\_{\lambda\_{2}}\,\big(m\_{\lambda\_{2}}^{-1}(x)\big) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =−λ2u1′​(mλ2−1​(x))​[u2′′​(𝚠−M−mλ2−1​(x))+u2′​(𝚠−M−mλ2−1​(x))​u1′′​(mλ2−1​(x))u1′​(mλ2−1​(x))].\displaystyle=\frac{-\lambda\_{2}}{u\_{1}^{\prime}\left(m\_{\lambda\_{2}}^{-1}(x)\right)}\left[u\_{2}^{\prime\prime}\left(\mathtt{w}-M-m\_{\lambda\_{2}}^{-1}(x)\right)+u\_{2}^{\prime}\left(\mathtt{w}-M-m\_{\lambda\_{2}}^{-1}(x)\right)\frac{u\_{1}^{\prime\prime}\left(m\_{\lambda\_{2}}^{-1}(x)\right)}{u\_{1}^{\prime}\left(m\_{\lambda\_{2}}^{-1}(x)\right)}\right]. |  |

Since Λ​(x)≥0\Lambda(x)\geq 0 and the second summand in the numerator of ([5.5](#S5.E5 "In item 2 ‣ Proposition 5.4. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) is negative, Proposition [5.4](#S5.Thmtheorem4 "Proposition 5.4. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting")(2) implies that the mapping M↦xM​(p)M\mapsto x\_{M}(p) is increasing only for those values of pp for which the term f′​(M)​(δ′​(p)−1)f^{\prime}(M)\left(\delta^{\prime}(p)-1\right) is sufficiently negative, i.e., when δ′​(p)<1\delta^{\prime}(p)<1, and f′​(M)>0f^{\prime}(M)>0 is large. By concavity of the function ff, this happens for small values of MM. This is consistent with Figure [10](#S5.F10 "Figure 10 ‣ Example 5.1. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
which shows that the density components of X1M=xM​(𝚄)X\_{1}^{M}=x\_{M}(\mathtt{U}) (for varying MM) are predominantly decreasing in MM in the right tails, and they increase only in a small region around the corresponding atoms.

Proposition [5.4](#S5.Thmtheorem4 "Proposition 5.4. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting")(2) quantifies the sensitivity of XMX\_{M} to changes in MM and will also help in determining the optimal level of effort. This is the content of the following result.
Without loss of generality, we set λ2=1\lambda\_{2}=1.

###### Theorem 5.5.

The optimal level of effort M∗=M∗​(T,f)M^{\*}=M^{\*}(T,f) can be characterized through FOC of ([5.1](#S5.E1 "In 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). That is,

|  |  |  |
| --- | --- | --- |
|  | W​(XM∗,M∗)=maxM⁡W​(XM,M)=maxM⁡maxX⁡W​(X,M),\displaystyle W(X\_{M^{\*}},M^{\*})=\max\_{M}\,W(X\_{M},M)=\max\_{M}\,\max\_{X}\,W(X,M), |  |

where M∗M^{\*} solves the equation

|  |  |  |
| --- | --- | --- |
|  | ∫01∂∂M​[u1​(xM​(t))​T~M′​(t)]​𝑑t=−∫01∂∂M​u2​(𝚠−M−xM​(1−t))​𝑑t.\int\_{0}^{1}\frac{\partial}{\partial M}\,\left[u\_{1}(x\_{M}(t))\,\widetilde{T}^{\prime}\_{M}(t)\right]\,dt=-\int\_{0}^{1}\frac{\partial}{\partial M}\,u\_{2}(\mathtt{w}-M-x\_{M}(1-t))\,dt. |  |

In the following example, we illustrate this result by returning to the setup of Section [4.2](#S4.SS2 "4.2. The Case of a Prelec Probability Weighting Function ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), with two CARA agents.

###### Example 5.6.

Let 𝚠=1\mathtt{w}=1 and λ2=1\lambda\_{2}=1. The RDU agent has a distortion function T​(p)=exp⁡(−(−ln⁡(p))α)T(p)=\exp(-(-\ln(p))^{\alpha}), with conjugate distortion function T~​(p)=1−exp⁡(−(−ln⁡(1−p))α)\widetilde{T}(p)=1-\exp(-(-\ln(1-p))^{\alpha}).
The two agents have CARA utility functions ui​(x)=−1βi​e−βi​xu\_{i}(x)=-\frac{1}{\beta\_{i}}e^{-\beta\_{i}x}, with first derivatives ui′​(x)=e−βi​xu\_{i}^{\prime}(x)=e^{-\beta\_{i}x}, for i=1,2i=1,2. In the numerical illustration we set β1=12\beta\_{1}=\tfrac{1}{2} and β2=β¯=0.4\beta\_{2}=\bar{\beta}=0.4, so that the EU agent coincides with the representative agent from Corollary [4.4](#S4.Thmtheorem4 "Corollary 4.4. ‣ 4.3. Closed-Form Solutions for a Prelec RDU Agent ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"). Using T~M′​(t)=f​(M)+(1−f​(M))​T~′​(t)\widetilde{T}^{\prime}\_{M}(t)=f(M)+(1-f(M))\,\widetilde{T}^{\prime}(t) and ∂∂M​T~M′​(t)=f′​(M)​(1−T~′​(t))\frac{\partial}{\partial M}\,\widetilde{T}^{\prime}\_{M}(t)=f^{\prime}(M)\,(1-\widetilde{T}^{\prime}(t)), it follows that the FOC from Theorem [5.5](#S5.Thmtheorem5 "Theorem 5.5. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting") is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01e−β1​xM​(t)​[xM′​(t)​(f​(M)+(1−f​(M))​T~′​(t))−1β1​f′​(M)​(T~′​(t)−1)]​𝑑t=∫01e−β2​(1−M−xM​(1−t))​[1+xM′​(1−t)]​𝑑t.\begin{split}&\displaystyle\int\_{0}^{1}e^{-\beta\_{1}{x\_{M}(t)}}\left[x\_{M}^{\prime}(t)\,\Big(f(M)+(1-f(M))\,\widetilde{T}^{\prime}(t)\Big)-\frac{1}{\beta\_{1}}f^{\prime}(M)(\widetilde{T}^{\prime}(t)-1)\right]dt\\ &\qquad=\displaystyle\int\_{0}^{1}e^{-\beta\_{2}(1-M-x\_{M}(1-t))}\left[1+x\_{M}^{\prime}(1-t)\right]dt.\end{split} |  | (5.6) |

In the following, we aim to derive the function M↦XMM\mapsto X\_{M} in closed form, by applying Proposition [5.4](#S5.Thmtheorem4 "Proposition 5.4. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting")(1). With β1+β2=1\beta\_{1}+\beta\_{2}=1, we obtain first

|  |  |  |
| --- | --- | --- |
|  | m​(x)=u2′​(𝚠−M−x)u1′​(x)=e−β2​(𝚠−M−x)+β1​x=e−β2​(𝚠−M)+(β1+β2)​x,m(x)=\frac{u\_{2}^{\prime}(\mathtt{w}-M-x)}{u\_{1}^{\prime}(x)}=e^{-\beta\_{2}(\mathtt{w}-M-x)+\beta\_{1}x}=e^{-\beta\_{2}(\mathtt{w}-M)+(\beta\_{1}+\beta\_{2})x}, |  |

with inverse function m−1​(x)=ln⁡(x)+β2​(𝚠−M)β1+β2=ln⁡(x)+β2​(1−M)m^{-1}(x)=\frac{\ln(x)+\beta\_{2}(\mathtt{w}-M)}{\beta\_{1}+\beta\_{2}}=\ln(x)+\beta\_{2}(1-M). Substituting m−1​(x)m^{-1}(x) into XMX\_{M} from Proposition [5.4](#S5.Thmtheorem4 "Proposition 5.4. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting")(1) yields

|  |  |  |
| --- | --- | --- |
|  | xM​(t)=ln⁡(δ′​(t)−f​(M)​(δ′​(t)−1))+β2​(1−M).x\_{M}(t)=\ln\left(\delta^{\prime}(t)-f(M)\left(\delta^{\prime}(t)-1\right)\right)+\beta\_{2}(1-M). |  |

We now compute XM′X\_{M}^{\prime}. Based on Proposition [5.4](#S5.Thmtheorem4 "Proposition 5.4. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting")(2), we aim to find Λ​(x)=dd​x​m​(m−1​(x))\Lambda(x)=\frac{d}{dx}m\,\big(m^{-1}(x)\big) in closed form. Now, letting y:=m−1​(x)y:=m^{-1}(x), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ​(x)\displaystyle\Lambda(x) | =−λ2u1′​(m−1​(x))​[u2′′​(𝚠−M−m−1​(x))+u2′​(𝚠−M−m−1​(x))​u1′′​(mλ2−1​(x))u1′​(mλ2−1​(x))]\displaystyle=\frac{-\lambda\_{2}}{u\_{1}^{\prime}\left(m^{-1}(x)\right)}\left[u\_{2}^{\prime\prime}\left(\mathtt{w}-M-m^{-1}(x)\right)+u\_{2}^{\prime}\left(\mathtt{w}-M-m^{-1}(x)\right)\frac{u\_{1}^{\prime\prime}\left(m\_{\lambda\_{2}}^{-1}(x)\right)}{u\_{1}^{\prime}\left(m\_{\lambda\_{2}}^{-1}(x)\right)}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−λ2e−β1​y​[−β2​e−β2​(𝚠−M−y)+e−β2​(𝚠−M−y)​−β1​e−β1​ye−β1​y]=−λ2e−β1​y​[−(β1+β2)​e−β2​(𝚠−M−y)]\displaystyle=\frac{-\lambda\_{2}}{e^{-\beta\_{1}y}}\left[-\beta\_{2}e^{-\beta\_{2}(\mathtt{w}-M-y)}+e^{-\beta\_{2}(\mathtt{w}-M-y)}\,\frac{-\beta\_{1}e^{-\beta\_{1}y}}{e^{-\beta\_{1}y}}\right]=\frac{-\lambda\_{2}}{e^{-\beta\_{1}y}}\left[-(\beta\_{1}+\beta\_{2})\,e^{-\beta\_{2}(\mathtt{w}-M-y)}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =λ2​(β1+β2)​e−β2​(𝚠−M)+(β1+β2)​y=e−β2​(1−M)+y=e−β2​(1−M)+ln⁡(x)+β2​(1−M)=x.\displaystyle=\lambda\_{2}(\beta\_{1}+\beta\_{2})\,e^{-\beta\_{2}(\mathtt{w}-M)+(\beta\_{1}+\beta\_{2})\,y}=e^{-\beta\_{2}(1-M)+y}=e^{-\beta\_{2}(1-M)+\ln(x)+\beta\_{2}(1-M)}=x. |  |

Consequently, for each tt,

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt′​(M)\displaystyle x^{\prime}\_{t}(M) | :=∂∂M​XM​(t)=−f′​(M)​(δ′​(t)−1)+λ2​u2′′​(𝚠−M−m−1​(δ′​(t)−f​(M)​(δ′​(t)−1)))u1′​(m−1​(δ′​(t)−f​(M)​(δ′​(t)−1)))Λ​(δ′​(t)−f​(M)​(δ′​(t)−1))\displaystyle:=\frac{\partial}{\partial M}X\_{M}(t)=\frac{-f^{\prime}(M)\left(\delta^{\prime}(t)-1\right)+\lambda\_{2}\,\dfrac{u\_{2}^{\prime\prime}\left(\mathtt{w}-M-m^{-1}\left(\delta^{\prime}(t)-f(M)\left(\delta^{\prime}(t)-1\right)\right)\right)}{u\_{1}^{\prime}\left(m^{-1}\left(\delta^{\prime}(t)-f(M)\left(\delta^{\prime}(t)-1\right)\right)\right)}}{\Lambda\left(\delta^{\prime}(t)-f(M)\left(\delta^{\prime}(t)-1\right)\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−f′​(M)​(δ′​(t)−1)+u2′′​(𝚠−M−m−1​(δ′​(t)−f​(M)​(δ′​(t)−1)))u1′​(m−1​(δ′​(t)−f​(M)​(δ′​(t)−1)))δ′​(t)−f​(M)​(δ′​(t)−1)\displaystyle=\frac{-f^{\prime}(M)\left(\delta^{\prime}(t)-1\right)+\dfrac{u\_{2}^{\prime\prime}\left(\mathtt{w}-M-m^{-1}\left(\delta^{\prime}(t)-f(M)\left(\delta^{\prime}(t)-1\right)\right)\right)}{u\_{1}^{\prime}\left(m^{-1}\left(\delta^{\prime}(t)-f(M)\left(\delta^{\prime}(t)-1\right)\right)\right)}}{\delta^{\prime}(t)-f(M)\left(\delta^{\prime}(t)-1\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−f′​(M)​(δ′​(t)−1)−[δ′​(t)−f​(M)​(δ′​(t)−1)]​β2δ′​(t)−f​(M)​(1−δ′​(t))=f′​(M)​(1−δ′​(t))(1−f​(M))​δ′​(t)+f​(M)−β2.\displaystyle=\frac{-f^{\prime}(M)\left(\delta^{\prime}(t)-1\right)-\left[\delta^{\prime}(t)-f(M)(\delta^{\prime}(t)-1)\right]\beta\_{2}}{\delta^{\prime}(t)-f(M)(1-\delta^{\prime}(t))}=\frac{f^{\prime}(M)\left(1-\delta^{\prime}(t)\right)}{{(1-f(M))\delta^{\prime}(t)+f(M)}}-\beta\_{2}. |  |

Substituting xMx\_{M} and xM′x\_{M}^{\prime} into (LABEL:inteq) gives an integral equation to identify the optimal effort level M∗​(k,α)∈(0,1)M^{\*}(k,\alpha)\in(0,1) that maximizes the social welfare of the nudging planner. If we now take the specific form f​(M):=1−(1−M)kf(M):=1-(1-M)^{k}, with k>1k>1, then in view of Section [4](#S4 "4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), we see that M∗M^{\*} reduces the riskiness of the allocation, since the full-insurance term 𝔽​𝕀\mathbb{FI} increases with M∗M^{\*}, at the cost of decreasing aggregate wealth 1−M∗1-M^{\*}.

With sufficient curvature in ff, say k=20k=20 and α=0.4\alpha=0.4, the integral equation in (LABEL:inteq) can be solved numerically. This gives M∗≈6.57%M^{\*}\approx 6.57\% of the aggregate wealth 𝚠=1\mathtt{w}=1 as the optimal fraction of the (constant) aggregate endowment that is invested in nudging. However, a distortion with less linearity, say α=0.2\alpha=0.2, results in a significant increase in the optimal fraction to M∗≈9.25%M^{\*}\approx 9.25\%. See Figure [11](#S5.F11 "Figure 11 ‣ Example 5.6. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting") for an overview.

![Refer to caption](2602.24194v1/x15.png)


Figure 11. Optimal investment in nudging as a function of the Prelec parameter α\alpha. For α>0.76\alpha>0.76, we have M∗=0M^{\*}=0.

Figure [11](#S5.F11 "Figure 11 ‣ Example 5.6. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting") shows that the optimal effort M∗M^{\*} is zero whenever the Prelec parameter α\alpha is sufficiently close to its EU benchmark value α=1\alpha=1. In this region, the probability weighting function is almost linear, so the welfare gains from correcting the internality are too small to justify the reduction in aggregate wealth, and the planner will not intervene. Only once probability distortions become sufficiently pronounced (that is, when α\alpha is much smaller than 11) is M∗M^{\*} strictly positive. This illustrates that the social planner is willing to tolerate a nontrivial amount of endogenous uncertainty in equilibrium, before spending resources on nudging the RDU agent toward more linear probability weighting.

## 6. Conclusion

In pure-exchange economies with no aggregate uncertainty populated by Subjective-Expected Utility (SEU) maximizers, Pareto-efficient allocations are no-betting (full-insurance) allocations if and only if the agents have common beliefs. In this paper, we show how the introduction of a single Rank-Dependent Utility (RDU) agent, into an otherwise classical setting with EU agents that have common beliefs, can lead to drastically different predictions. We demonstrate how betting, that is, uncertainty-generating trade, can be Pareto improving despite the presence of a common baseline probability measure on the state space. That is, probability weighting endogenously generates betting at an optimum, even under common baseline beliefs, thereby showing that uncertainty-generating trade can arise purely from heterogeneity in the perception of risk, rather than in beliefs.

Our analysis provides a micro-founded explanation for the coexistence of common beliefs and speculative behavior in an environment with no initial aggregate uncertainty. We quantify this behavior by providing a crisp closed-form characterization of Pareto optima that shows precisely how betting behavior emerges at optima. Additionally, we provide comparative statics for some popular classes of probability weighting functions. Finally, we examine how an appropriately designed intervention, such as statistical or financial education of the RDU agent, can attenuate undesirable speculative trade and partially re-establish the optimality of full-insurance allocations.

## Appendix A Proofs for Section [3](#S3 "3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")

By a slight abuse of notation, set ∫⋅d​t=∫01⋅d​t\displaystyle\int\cdot\,\textnormal{d}t=\int\_{0}^{1}\cdot\,\textnormal{d}t and ∫⋅d​ℙ=∫Ω⋅d​ℙ\displaystyle\int\cdot\,\textnormal{d}\mathbb{P}=\int\_{\Omega}\cdot\,\textnormal{d}\mathbb{P}.

Proof of Proposition [3.1](#S3.Thmtheorem1 "Proposition 3.1. ‣ 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"): (1) Immediate. (2) When TT is convex, it follows from Chew et al. ([1987](#bib.bib30 "Risk Aversion in the Theory of Expected Utility with Rank Dependent Probabilities")) that U1U\_{1} is concave. Moreover, by assumption, the functionals UiU\_{i} are concave, for each i∈{2,…,n}i\in\{2,\ldots,n\}. The rest follows from a classical separation argument (Carlier and Dana, [2006](#bib.bib39 "Law Invariant Concave Utility Functions and Optimization Problems with Monotonicity and Comonotonicity Constraints"), Proposition 3.4).∎

Proof of Proposition [3.3](#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"):

(1)⟹(2)(1)\implies(2):
Fix 𝐗−1∈𝒜−1C​(𝚠−X)\mathbf{X}\_{-1}\in{\mathcal{A}}\_{-1}^{C}(\mathtt{w}-X). Then by a classical result (Föllmer and Schied, [2025](#bib.bib1 "Stochastic Finance: An Introduction in Discrete Time – 5⁢th ed."), Lemma 4.95),
there are nondecreasing and 11-Lipschitz functions gig\_{i} that sum to the identity function, such that for each i∈{2,…,n}i\in\{2,\ldots,n\}, Xi=gi​(𝚠−X)X\_{i}=g\_{i}(\mathtt{w}-X). Since the probability space is nonatomic, it follows from (Föllmer and Schied, [2025](#bib.bib1 "Stochastic Finance: An Introduction in Discrete Time – 5⁢th ed."), Lemma D.17) that there exists a random variable 𝚄∼U​n​i​(0,1)\mathtt{U}\sim Uni(0,1) such that 𝚠−X=F𝚠−X−1​(𝚄)\mathtt{w}-{X}=F\_{\mathtt{w}-{X}}^{-1}(\mathtt{U}), a.s. In particular, 𝚠−X\mathtt{w}-{X} is comonotonic with 𝚄\mathtt{U}. Moreover, for each i∈{2,…,n}i\in\{2,\ldots,n\},

|  |  |  |
| --- | --- | --- |
|  | Xi=gi​(𝚠−X)=gi​(F𝚠−X−1​(𝚄))=Fgi​(𝚠−X)−1​(𝚄)=FXi−1​(𝚄),a.s.,X\_{i}=g\_{i}(\mathtt{w}-X)=g\_{i}\left(F\_{\mathtt{w}-{X}}^{-1}(\mathtt{U})\right)=F\_{g\_{i}(\mathtt{w}-{X})}^{-1}(\mathtt{U})=F\_{X\_{i}}^{-1}(\mathtt{U}),\ \hbox{a.s.,} |  |

by monotonicity of each function gig\_{i} (Föllmer and Schied, [2025](#bib.bib1 "Stochastic Finance: An Introduction in Discrete Time – 5⁢th ed."), Lemma D.12).

(2)⟹(1)(2)\implies(1):
Suppose that there exists some 𝚄∼U​n​i​(0,1)\mathtt{U}\sim Uni(0,1) comonotonic with 𝚠−X\mathtt{w}-X, such that Xi=FXi−1​(𝚄)X\_{i}=F\_{X\_{i}}^{-1}(\mathtt{U}), a.s., for each i∈{2,…,n}i\in\{2,\ldots,n\}. Then clearly the vector (X2,…,Xn)\left(X\_{2},\ldots,X\_{n}\right) is comonotonic.∎

Proof of Proposition [3.4](#S3.Thmtheorem4 "Proposition 3.4. ‣ 3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"):
By nonatomicity of the space, let 𝚄∼U​n​i​(0,1)\mathtt{U}\sim Uni(0,1) be such that 𝚠−X=F𝚠−X−1​(𝚄)\mathtt{w}-{X}=F\_{\mathtt{w}-{X}}^{-1}(\mathtt{U}), a.s. Let {fi∗}i=2n\{f\_{i}^{\*}\}\_{i=2}^{n} be optimal for ([3.5](#S3.E5 "In 3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). For each i∈{2,…,n}i\in\{2,\ldots,n\}, let Xi∗:=fi∗​(𝚄)X\_{i}^{\*}:=f\_{i}^{\*}(\mathtt{U}). Then {Xi∗}i=2n\{X\_{i}^{\*}\}\_{i=2}^{n} is comonotonic since fi∗f\_{i}^{\*} is nondecreasing for all i∈{2,…,n}i\in\{2,\ldots,n\}. Moreover, by feasibility of {fi∗}i=2n\{f\_{i}^{\*}\}\_{i=2}^{n} for ([3.5](#S3.E5 "In 3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")),

|  |  |  |
| --- | --- | --- |
|  | ∑i=2nXi∗:=∑i=2nfi∗​(𝚄)=F𝚠−X−1​(𝚄)=𝚠−X,a.s.\sum\_{i=2}^{n}X\_{i}^{\*}:=\sum\_{i=2}^{n}f\_{i}^{\*}(\mathtt{U})=F\_{\mathtt{w}-{X}}^{-1}(\mathtt{U})=\mathtt{w}-{X},\ a.s. |  |

Thus, (Xi∗)i=2n∈𝒜−1C​(𝚠−X)(X\_{i}^{\*})\_{i=2}^{n}\in{\mathcal{A}}^{C}\_{-1}(\mathtt{w}-{X}), and hence it is feasible for ([3.2](#S3.E2 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). Suppose that {Xi∗}i=2n\{X\_{i}^{\*}\}\_{i=2}^{n} is not optimal for ([3.2](#S3.E2 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). Then there exists some (Zi)i=2n∈𝒜−1C​(𝚠−X)(Z\_{i})\_{i=2}^{n}\in{\mathcal{A}}^{C}\_{-1}(\mathtt{w}-{X}) such that

|  |  |  |
| --- | --- | --- |
|  | ∑i=2nλi​Ui​(Zi)>∑i=2nλi​Ui​(Xi∗).\sum\_{i=2}^{n}\lambda\_{i}\,U\_{i}(Z\_{i})>\sum\_{i=2}^{n}\lambda\_{i}\,U\_{i}(X\_{i}^{\*}). |  |

For each i∈{2,…,n}i\in\{2,\ldots,n\}, let gi:=FZi−1g\_{i}:=F\_{Z\_{i}}^{-1}. Then since (Zi)i=2n∈𝒜−1C​(𝚠−X)(Z\_{i})\_{i=2}^{n}\in{\mathcal{A}}^{C}\_{-1}(\mathtt{w}-{X}),

|  |  |  |
| --- | --- | --- |
|  | ∑i=2ngi=F∑i=2nZi−1=F𝚠−X−1.\sum\_{i=2}^{n}g\_{i}=F\_{\sum\_{i=2}^{n}Z\_{i}}^{-1}=F\_{\mathtt{w}-{X}}^{-1}. |  |

Thus {gi}i=2n\{g\_{i}\}\_{i=2}^{n} is feasible for ([3.5](#S3.E5 "In 3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")), and so

|  |  |  |
| --- | --- | --- |
|  | ∑i=2nλi​Ui​(Zi)=∫∑i=2nλi​ui​(gi​(t))​d​t≤∫∑i=2nλi​ui​(fi∗​(t))​d​t=∑i=2nλi​Ui​(Xi∗),\sum\_{i=2}^{n}\lambda\_{i}\,U\_{i}(Z\_{i})=\int\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(g\_{i}(t)\right)\,\textnormal{d}t\leq\int\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(f\_{i}^{\*}(t)\right)\,\textnormal{d}t=\sum\_{i=2}^{n}\lambda\_{i}\,U\_{i}(X\_{i}^{\*}), |  |

a contradiction. Therefore, {Xi∗}i=2n\{X\_{i}^{\*}\}\_{i=2}^{n} is optimal for ([3.2](#S3.E2 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")).

Conversely, let {Xi∗:=fi∗​(𝚄)}i=2n\{X\_{i}^{\*}:=f\_{i}^{\*}(\mathtt{U})\}\_{i=2}^{n} be optimal for ([3.2](#S3.E2 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). Since (Xi∗)i=2n∈𝒜−1C​(𝚠−X)(X\_{i}^{\*})\_{i=2}^{n}\in{\mathcal{A}}^{C}\_{-1}(\mathtt{w}-{X}), it follows that

|  |  |  |
| --- | --- | --- |
|  | ∑i=2nfi∗=∑i=2nFXi∗−1=F∑i=2nXi∗−1=F𝚠−X−1,\sum\_{i=2}^{n}f\_{i}^{\*}=\sum\_{i=2}^{n}F\_{X\_{i}^{\*}}^{-1}=F\_{\sum\_{i=2}^{n}X\_{i}^{\*}}^{-1}=F\_{\mathtt{w}-{X}}^{-1}, |  |

and hence {fi∗}i=2n\{f\_{i}^{\*}\}\_{i=2}^{n} is feasible for ([3.5](#S3.E5 "In 3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). Suppose that {fi∗}i=2n\{f\_{i}^{\*}\}\_{i=2}^{n} is not optimal for ([3.5](#S3.E5 "In 3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). Then there exists some (gi)i=2n∈𝒬(g\_{i})\_{i=2}^{n}\in\mathcal{Q} such that ∑i=2ngi=F𝚠−X−1\sum\_{i=2}^{n}g\_{i}=F\_{\mathtt{w}-{X}}^{-1} and

|  |  |  |
| --- | --- | --- |
|  | ∫∑i=2nλi​ui​(gi​(t))​d​t>∫∑i=2nλi​ui​(fi∗​(t))​d​t=∫∑i=2nλi​ui​(FXi∗−1​(𝚄))​d​ℙ=∑i=2nλi​Ui​(Xi∗).\int\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(g\_{i}(t)\right)\,\textnormal{d}t>\int\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(f^{\*}\_{i}(t)\right)\,\textnormal{d}t=\int\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(F^{-1}\_{X^{\*}\_{i}}(\mathtt{U})\right)\,\textnormal{d}\mathbb{P}=\sum\_{i=2}^{n}\lambda\_{i}\,U\_{i}(X\_{i}^{\*}). |  |

Letting Zi:=gi​(𝚄)Z\_{i}:=g\_{i}(\mathtt{U}) for each i∈{2,…,n}i\in\{2,\ldots,n\}, it follows that

|  |  |  |
| --- | --- | --- |
|  | ∑i=2nλi​Ui​(Zi)=∫∑i=2nλi​ui​(FZi−1​(𝚄))​d​ℙ=∫∑i=2nλi​ui​(gi​(𝚄))​d​ℙ=∫∑i=2nλi​ui​(gi​(t))​d​t>∑i=2nλi​Ui​(Xi∗),\sum\_{i=2}^{n}\lambda\_{i}\,U\_{i}(Z\_{i})=\int\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(F^{-1}\_{Z\_{i}}(\mathtt{U})\right)\,\textnormal{d}\mathbb{P}=\int\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(g\_{i}(\mathtt{U})\right)\,\textnormal{d}\mathbb{P}=\int\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(g\_{i}(t)\right)\,\textnormal{d}t>\sum\_{i=2}^{n}\lambda\_{i}\,U\_{i}(X\_{i}^{\*}), |  |

a contradiction. Hence, {fi∗}i=2n\{f\_{i}^{\*}\}\_{i=2}^{n} is optimal for ([3.5](#S3.E5 "In 3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")).∎

Proof of Lemma [3.5](#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"): Note that for all xx,

|  |  |  |
| --- | --- | --- |
|  | x=Iλ​(Jλ​(x))=∑i=2nIi​(Jλ​(x)λi)anduλ′​(x)=Jλ​(x).x=I\_{\lambda}(J\_{\lambda}(x))=\sum\_{i=2}^{n}I\_{i}\left(\frac{J\_{\lambda}(x)}{\lambda\_{i}}\right)\ \ \hbox{and}\ \ u^{\prime}\_{\lambda}(x)=J\_{\lambda}(x). |  |

Hence, it follows that f2⋄,…,fn⋄∈𝒬f^{\diamond}\_{2},\ldots,f^{\diamond}\_{n}\in\mathcal{Q} and
∑i=2nfi⋄=∑i=2nIi​(λi−1​Jλ​(F𝚠−X−1))=F𝚠−X−1.\sum\_{i=2}^{n}f^{\diamond}\_{i}=\sum\_{i=2}^{n}I\_{i}\left(\lambda\_{i}^{-1}J\_{\lambda}\left(F^{-1}\_{\mathtt{w}-{X}}\right)\right)=F^{-1}\_{\mathtt{w}-{X}}.
That is, {fi⋄}i=2n\{f^{\diamond}\_{i}\}\_{i=2}^{n} is feasible for ([3.5](#S3.E5 "In 3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). In addition, if {fi∗}i=2n\{f^{\*}\_{i}\}\_{i=2}^{n} is optimal for ([3.5](#S3.E5 "In 3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")), then

|  |  |  |
| --- | --- | --- |
|  | ∑i=2n(fi∗​(t)−fi⋄​(t))=0,a.s.,\sum\_{i=2}^{n}\left(f^{\*}\_{i}(t)-f^{\diamond}\_{i}(t)\right)=0,\,a.s., |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | and ​∫uλ​(F𝚠−X−1​(t))​d​t=∫∑i=2nλi​ui​(fi⋄​(t))​d​t≤∫∑i=2nλi​ui​(fi∗​(t))​d​t.\textnormal{ and }\int u\_{\lambda}\left(F^{-1}\_{\mathtt{w}-{X}}(t)\right)\,\textnormal{d}t=\int\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(f^{\diamond}\_{i}(t)\right)\,\textnormal{d}t\leq\int\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(f^{\*}\_{i}(t)\right)\,\textnormal{d}t. |  | (A.1) |

Moreover, for a fixed t∈[0,1]t\in[0,1], the concavity of uiu\_{i} for i∈{2,…,n}i\in\{2,\ldots,n\} yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=2nλi​ui​(fi∗​(t))\displaystyle\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(f^{\*}\_{i}(t)\right) | ≤∑i=2nλi​ui​(fi⋄​(t))+∑i=2nλi​(fi∗​(t)−fi⋄​(t))​ui′​(fi⋄​(t))\displaystyle\leq\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(f^{\diamond}\_{i}(t)\right)+\sum\_{i=2}^{n}\lambda\_{i}\,\left(f^{\*}\_{i}(t)-f^{\diamond}\_{i}(t)\right)\,u\_{i}^{\prime}\left(f^{\diamond}\_{i}(t)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =uλ​(F𝚠−X−1​(t))+∑i=2nλi​(fi∗​(t)−fi⋄​(t))​ui′​(Ii​(Jλ​(F𝚠−X−1​(t))λi))⏟=λi−1​Jλ​(F𝚠−X−1​(t)).\displaystyle=u\_{\lambda}\left(F^{-1}\_{\mathtt{w}-{X}}(t)\right)+\sum\_{i=2}^{n}\lambda\_{i}\,\left(f^{\*}\_{i}(t)-f^{\diamond}\_{i}(t)\right)\,\underbrace{u\_{i}^{\prime}\Big(I\_{i}\Big(\frac{J\_{\lambda}(F^{-1}\_{\mathtt{w}-{X}}(t))}{\lambda\_{i}}\Big)\Big)}\_{=\lambda\_{i}^{-1}J\_{\lambda}\left(F^{-1}\_{\mathtt{w}-{X}}(t)\right)}. |  |

Hence, for a.e. t∈[0,1]t\in[0,1], the derivation yields ∑i=2nλi​ui​(fi∗​(t))≤uλ​(F𝚠−X−1​(t)).\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(f^{\*}\_{i}(t)\right)\leq u\_{\lambda}\left(F^{-1}\_{\mathtt{w}-{X}}(t)\right). Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫∑i=2nλi​ui​(fi∗​(t))​d​t≤∫uλ​(F𝚠−X−1​(t))​d​t.\int\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(f^{\*}\_{i}(t)\right)\,\textnormal{d}t\leq\int u\_{\lambda}\left(F^{-1}\_{\mathtt{w}-{X}}(t)\right)\textnormal{d}t. |  | (A.2) |

Consequently, by ([A.1](#A1.E1 "In Appendix A Proofs for Section 3 ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) and ([A.2](#A1.E2 "In Appendix A Proofs for Section 3 ‣ Betting under Common Beliefs: The Effect of Probability Weighting")),

|  |  |  |
| --- | --- | --- |
|  | ∫∑i=2nλi​ui​(fi∗​(t))​d​t=∫uλ​(F𝚠−X−1​(t))​d​t=∫∑i=2nλi​ui​(fi⋄​(t))​d​t,\int\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(f^{\*}\_{i}(t)\right)\,\textnormal{d}t=\int u\_{\lambda}\left(F^{-1}\_{\mathtt{w}-{X}}(t)\right)\,\textnormal{d}t=\int\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(f^{\diamond}\_{i}(t)\right)\,\textnormal{d}t, |  |

implying that {fi⋄}i=2n\{f^{\diamond}\_{i}\}\_{i=2}^{n} is optimal for ([3.5](#S3.E5 "In 3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). Additionally, note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup𝐗−1∈𝒜−1​(𝚠−X)∑i=2nλi​Ui​(Xi)\displaystyle\sup\_{\mathbf{X}\_{-1}\in{\mathcal{A}}\_{-1}(\mathtt{w}-{X})}\ \sum\_{i=2}^{n}\lambda\_{i}\,U\_{i}(X\_{i}) | =∑i=2nλi​Ui​(fi⋄​(𝚄))=∑i=2nλi​∫ui​(fi⋄​(𝚄))​d​ℙ\displaystyle=\sum\_{i=2}^{n}\lambda\_{i}\,U\_{i}\left(f^{\diamond}\_{i}(\mathtt{U})\right)=\sum\_{i=2}^{n}\lambda\_{i}\,\int u\_{i}\left(f^{\diamond}\_{i}(\mathtt{U})\right)\textnormal{d}\mathbb{P} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫∑i=2nλi​ui​(fi⋄​(t))​d​t=∫uλ​(F𝚠−X−1​(t))​d​t\displaystyle=\int\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(f^{\diamond}\_{i}(t)\right)\,\textnormal{d}t=\int u\_{\lambda}\left(F^{-1}\_{\mathtt{w}-{X}}(t)\right)\,\textnormal{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫uλ​(F𝚠−X−1​(𝚄))​d​ℙ=∫uλ​(𝚠−X)​d​ℙ.\displaystyle=\int u\_{\lambda}\left(F^{-1}\_{\mathtt{w}-{X}}(\mathtt{U})\right)\,\textnormal{d}\mathbb{P}=\int u\_{\lambda}\left(\mathtt{w}-{X}\right)\,\textnormal{d}\mathbb{P}. |  |

∎

As a preparation of the proof of Lemma [3.6](#S3.Thmtheorem6 "Lemma 3.6. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), define the pointwise aggregate utility of the EU agents by

|  |  |  |  |
| --- | --- | --- | --- |
|  | uλ​(x):=∑i=2nλi​ui​(Ii​(Jλ​(x)λi)).u\_{\lambda}(x):=\sum\_{i=2}^{n}\lambda\_{i}\,u\_{i}\left(I\_{i}\left(\tfrac{J\_{\lambda}(x)}{\lambda\_{i}}\right)\right). |  | (A.3) |

It also follows from Lemma [3.5](#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting") that if 𝚄∼U​n​i​(0,1)\mathtt{U}\sim Uni(0,1) is such that 𝚠−X=F𝚠−X−1​(𝚄)\mathtt{w}-{X}=F\_{\mathtt{w}-{X}}^{-1}(\mathtt{U}), a.s., then

1. (1)

   For all i∈{2,…,n}i\in\{2,\ldots,n\}, we have ui′​(fi⋄​(𝚄))=λi−1​uλ′​(𝚠−X),a.s.u\_{i}^{\prime}(f^{\diamond}\_{i}(\mathtt{U}))=\lambda\_{i}^{-1}\,u\_{\lambda}^{\prime}(\mathtt{w}-{X}),\,a.s.
2. (2)

   {fi⋄​(𝚄)}i=2n\{f^{\diamond}\_{i}(\mathtt{U})\}\_{i=2}^{n} is optimal for ([3.2](#S3.E2 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) and hence (𝚠−X)(\mathtt{w}-{X})-PO, and fi⋄​(𝚄)=Ii​(Jλ​(𝚠−X)λi)f^{\diamond}\_{i}(\mathtt{U})=I\_{i}\left(\frac{J\_{\lambda}\left(\mathtt{w}-{X}\right)}{\lambda\_{i}}\right), a.s., for each i∈{2,…,n}i\in\{2,\ldots,n\}. Moreover, with Uλ​(𝚠−X)U\_{\lambda}(\mathtt{w}-{X}) as in ([3.2](#S3.E2 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")), we have

   |  |  |  |
   | --- | --- | --- |
   |  | Uλ​(𝚠−X)=∑i=2nλi​Ui​(fi⋄​(𝚄))=∫uλ​(𝚠−X)​d​ℙ.\displaystyle U\_{\lambda}(\mathtt{w}-{X})=\sum\_{i=2}^{n}\lambda\_{i}\,U\_{i}\left(f^{\diamond}\_{i}(\mathtt{U})\right)=\int u\_{\lambda}(\mathtt{w}-{X})\,\textnormal{d}\mathbb{P}. |  |

Proof of Lemma [3.6](#S3.Thmtheorem6 "Lemma 3.6. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"):
Recall that Problem ([3.3](#S3.E3 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) is given by supX∈𝒳[U1​(X)+Uλ​(𝚠−X)]\sup\_{X\in\mathcal{X}}\left[U\_{1}(X)+U\_{\lambda}(\mathtt{w}-X)\right], where by Lemma [3.5](#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),

|  |  |  |
| --- | --- | --- |
|  | Uλ​(𝚠−X)=∫uλ​(𝚠−X)​d​ℙ,U\_{\lambda}(\mathtt{w}-X)=\int u\_{\lambda}(\mathtt{w}-{X})\,\textnormal{d}\mathbb{P}, |  |

and uλu\_{\lambda} is defined in ([A.3](#A1.E3 "In Appendix A Proofs for Section 3 ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). Hence, X∗X^{\*} is optimal for Problem ([3.3](#S3.E3 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) if and only if it is optimal for

|  |  |  |
| --- | --- | --- |
|  | supX∈𝒳[∫u1​(X)​d​T∘ℙ+∫uλ​(𝚠−X)​d​ℙ].\sup\_{X\in\mathcal{X}}\,\left[\int u\_{1}(X)\,\textnormal{d}T\circ\mathbb{P}\ +\int u\_{\lambda}(\mathtt{w}-{X})\,\textnormal{d}\mathbb{P}\right]. |  |

Moreover, as in (Beißner et al., [2024](#bib.bib10 "(No-)Betting Pareto-Optima under Rank-Dependent Utility"), Lemma A.1),

|  |  |  |
| --- | --- | --- |
|  | ∫u1​(X)​d​T∘ℙ=∫u1​(ft)​T~t′​d​tand∫uλ​(𝚠−X)​d​ℙ=∫uλ​(𝚠−ft)​d​t,\int u\_{1}(X)\,\textnormal{d}T\circ\mathbb{P}=\int u\_{1}(f\_{t})\,\widetilde{T}^{\prime}\_{t}\,\textnormal{d}t\ \ \hbox{and}\ \ \int u\_{\lambda}(\mathtt{w}-{X})\,\textnormal{d}\mathbb{P}=\int u\_{\lambda}\left(\mathtt{w}-f\_{t}\right)\,\textnormal{d}t, |  |

where ft:=FX−1​(t)f\_{t}:=F\_{X}^{-1}(t) and T~t′:=T~′​(t)\widetilde{T}^{\prime}\_{t}:=\widetilde{T}^{\prime}(t), for all t∈[0,1]t\in[0,1]. Hence, using a quantile reformulation approach as in Beißner et al. ([2024](#bib.bib10 "(No-)Betting Pareto-Optima under Rank-Dependent Utility")), X∗X^{\*} is optimal for Problem ([3.3](#S3.E3 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) if and only if it is optimal for

|  |  |  |  |
| --- | --- | --- | --- |
|  | supf∈𝒬∫[u1​(ft)​T~t′+uλ​(𝚠−ft)]​d​t.\displaystyle\sup\_{f\in\mathcal{Q}}\,\int\left[u\_{1}(f\_{t})\,\widetilde{T}^{\prime}\_{t}+u\_{\lambda}(\mathtt{w}-f\_{t})\right]\,\textnormal{d}t. |  | (A.4) |

We solve Problem ([A.4](#A1.E4 "In Appendix A Proofs for Section 3 ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) using a pointwise optimization approach. First, it is easy to verify that, for each t∈[0,1]t\in[0,1],

|  |  |  |
| --- | --- | --- |
|  | f¯t:=mλ−1​(T~t′)=arg⁡maxy⁡{u1​(y)​T~t′+uλ​(𝚠−y)},\bar{f}\_{t}:=m^{-1}\_{\lambda}\left(\widetilde{T}^{\prime}\_{t}\right)=\operatorname\*{\arg\max}\_{y}\big\{u\_{1}(y)\,\widetilde{T}^{\prime}\_{t}+u\_{\lambda}(\mathtt{w}-y)\big\}, |  |

where mλ​(x):=uλ′​(𝚠−x)u1′​(x)m\_{\lambda}(x):=\frac{u\_{\lambda}^{\prime}(\mathtt{w}-x)}{u\_{1}^{\prime}(x)}, for all x∈ℝx\in\mathbb{R}. Since T~′\widetilde{T}^{\prime} might fail to be monotone, f¯\bar{f} might fail to be monotone and hence might not be an element of 𝒬\mathcal{Q}. To overcome this difficulty (arising from the nonconvexity of TT), we consider the following relaxation of Problem ([3.3](#S3.E3 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | supf∈𝒬∫[u1​(ft)​δt′+uλ​(𝚠−ft)]​d​t,\displaystyle\sup\_{f\in\mathcal{Q}}\ \int\left[u\_{1}(f\_{t})\delta^{\prime}\_{t}+u\_{\lambda}(\mathtt{w}-f\_{t})\right]\,\textnormal{d}t, |  | (A.5) |

where the function δ\delta is the (smooth) convex envelope of T~\widetilde{T}. The convexity of δ\delta yields monotonicity of δ′\delta^{\prime}, which guarantees that the pointwise optimizer f∗f^{\*} of Problem ([A.5](#A1.E5 "In Appendix A Proofs for Section 3 ‣ Betting under Common Beliefs: The Effect of Probability Weighting")), given by

|  |  |  |
| --- | --- | --- |
|  | ft∗:=mλ−1​(δt′)=arg⁡maxy⁡{u1​(y)​δt′+uλ​(𝚠−y)},f^{\*}\_{t}:=m^{-1}\_{\lambda}\left(\delta^{\prime}\_{t}\right)=\operatorname\*{\arg\max}\_{y}\big\{u\_{1}(y)\delta^{\prime}\_{t}+u\_{\lambda}(\mathtt{w}-y)\big\}, |  |

is indeed a quantile function.

Now, for any f∈𝒬f\in\mathcal{Q}, it follows from Lemma [A.1](#A1.Thmtheorem1 "Lemma A.1 (Lemma A.5 in Beißner et al. (2024)). ‣ Appendix A Proofs for Section 3 ‣ Betting under Common Beliefs: The Effect of Probability Weighting") that

|  |  |  |
| --- | --- | --- |
|  | ∫[u1​(ft)​T~t′+uλ​(𝚠−ft)]​d​t≤∫u1​(ft)​[δt′+uλ​(𝚠−ft)]​d​t≤∫[u1​(ft∗)​δt′+uλ​(𝚠−ft∗)]​d​t.\displaystyle\int\left[u\_{1}(f\_{t})\widetilde{T}^{\prime}\_{t}+u\_{\lambda}(\mathtt{w}-f\_{t})\right]\textnormal{d}t\leq\int u\_{1}(f\_{t})\left[\delta^{\prime}\_{t}+u\_{\lambda}(\mathtt{w}-f\_{t})\right]\textnormal{d}t\leq\int\left[u\_{1}(f^{\*}\_{t})\delta^{\prime}\_{t}+u\_{\lambda}(\mathtt{w}-f^{\*}\_{t})\right]\textnormal{d}t. |  |

Letting 𝒟:={t∈[0,1]:δt≠T~t}={t∈[0,1]:δt<T~t}\mathcal{D}:=\Big\{t\in\left[0,1\right]:\delta\_{t}\neq\widetilde{T}\_{t}\Big\}=\Big\{t\in\left[0,1\right]:\delta\_{t}<\widetilde{T}\_{t}\Big\}, it follows that

|  |  |  |
| --- | --- | --- |
|  | ∫[T~t−δt]​d​u1​(ft∗)=∫𝒟[T~t−δt]​d​u1​(ft∗).\begin{split}\int\left[\widetilde{T}\_{t}-\delta\_{t}\right]\textnormal{d}u\_{1}(f^{\*}\_{t})=\int\_{\mathcal{D}}\left[\widetilde{T}\_{t}-\delta\_{t}\right]\textnormal{d}u\_{1}(f^{\*}\_{t}).\end{split} |  |

But, since δ\delta is affine on 𝒟\mathcal{D}, d​δ′=0\textnormal{d}\delta^{\prime}=0 on 𝒟\mathcal{D}, and it follows from d​ft∗=(mλ−1)′​(δt′)​d​δt′\textnormal{d}f^{\*}\_{t}=\left(m^{-1}\_{\lambda}\right)^{\prime}\left(\delta^{\prime}\_{t}\right)\textnormal{d}\delta^{\prime}\_{t} that d​ft∗=0\textnormal{d}f^{\*}\_{t}=0 on 𝒟\mathcal{D}. Consequently, ∫[T~t−δt]​d​u1​(ft∗)=0\displaystyle\int\left[\widetilde{T}\_{t}-\delta\_{t}\right]\textnormal{d}u\_{1}(f^{\*}\_{t})=0. Therefore, applying Fubini’s Theorem yields

|  |  |  |
| --- | --- | --- |
|  | 0=∫(T~t−δt)​d​u1​(ft∗)=∫u1​(ft∗)​(T~t′−δt′)​d​t.0=\int(\widetilde{T}\_{t}-\delta\_{t})\,\textnormal{d}u\_{1}(f^{\*}\_{t})=\int u\_{1}(f^{\*}\_{t})(\widetilde{T}^{\prime}\_{t}-\delta^{\prime}\_{t})\,\textnormal{d}t. |  |

Hence, ∫u1​(ft∗)​T~t′​d​t=∫u1​(ft∗)​δt′​d​t\displaystyle\int u\_{1}(f^{\*}\_{t})\,\widetilde{T}^{\prime}\_{t}\,\textnormal{d}t=\int u\_{1}(f^{\*}\_{t})\,\delta^{\prime}\_{t}\,\textnormal{d}t. Therefore, for all f∈𝒬f\in\mathcal{Q},

|  |  |  |
| --- | --- | --- |
|  | ∫[u1​(ft)​T~t′+uλ​(𝚠−ft)]​d​t≤∫[u1​(ft∗)​δt′+uλ​(𝚠−ft∗)]​d​t=∫[u1​(ft∗)​T~t′+uλ​(𝚠−ft∗)]​d​t.\begin{split}\int\left[u\_{1}(f\_{t})\widetilde{T}^{\prime}\_{t}+u\_{\lambda}\left(\mathtt{w}-f\_{t}\right)\right]\textnormal{d}t\leq\int\left[u\_{1}(f^{\*}\_{t})\delta^{\prime}\_{t}+u\_{\lambda}\left(\mathtt{w}-f^{\*}\_{t}\right)\right]\textnormal{d}t=\int\left[u\_{1}(f^{\*}\_{t})\widetilde{T}^{\prime}\_{t}+u\_{\lambda}(\mathtt{w}-f^{\*}\_{t})\right]\textnormal{d}t.\end{split} |  |

Thus, f∗f^{\*} solves Problem ([A.4](#A1.E4 "In Appendix A Proofs for Section 3 ‣ Betting under Common Beliefs: The Effect of Probability Weighting")), and so
X∗=f∗​(𝚄)=mλ−1​(δ′​(𝚄)){X}^{\*}=f^{\*}(\mathtt{U})=m^{-1}\_{\lambda}(\delta^{\prime}(\mathtt{U})) solves Problem ([3.3](#S3.E3 "In 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting")). The uniqueness in distribution of X∗{X}^{\*} follows from (Beißner et al., [2024](#bib.bib10 "(No-)Betting Pareto-Optima under Rank-Dependent Utility"), Lemma A.8).∎

The following lemma was employed for the proof of Lemma [3.6](#S3.Thmtheorem6 "Lemma 3.6. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting").

###### Lemma A.1 (Lemma A.5 in Beißner et al. ([2024](#bib.bib10 "(No-)Betting Pareto-Optima under Rank-Dependent Utility"))).

Let δ\delta be the convex envelope of T~\widetilde{T} on [0,1]\left[0,1\right]. Then for any f∈𝒬f\in\mathcal{Q}, we have
∫u1​(ft)​T~t′​d​t≤∫u1​(ft)​δt′​d​t.\displaystyle\int u\_{1}\left(f\_{t}\right)\,\widetilde{T}^{\prime}\_{t}\,\textnormal{d}t\leq\int u\_{1}\left(f\_{t}\right)\,\delta^{\prime}\_{t}\,\textnormal{d}t.

Proof of Corollary [3.8](#S3.Thmtheorem8 "Corollary 3.8. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"): This is a direct consequence of Proposition [3.1](#S3.Thmtheorem1 "Proposition 3.1. ‣ 3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), Lemma [3.5](#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), Lemma [3.6](#S3.Thmtheorem6 "Lemma 3.6. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), and the observation that if TT is convex, then T~\widetilde{T} is concave and hence δ​(t)=t\delta(t)=t, for all t∈[0,1]t\in[0,1].∎

## Appendix B Proofs for Section [4](#S4 "4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting")

Proof of Proposition [4.1](#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"):
The proof of the first part of this proposition is similar to that of (Ghossoub, [2019](#bib.bib41 "Optimal Insurance under Rank-Dependent Expected Utility"), Lemma A.8). We provide it below for the sake of completeness.

Suppose that T~\widetilde{T} is S-shaped with inflection point t0∈[0,1]t\_{0}\in[0,1]. First, note that T~​(0)=δT~​(0)=0\widetilde{T}\left(0\right)=\delta\_{\widetilde{T}}\left(0\right)=0 and T~​(1)=δT~​(1)=1\widetilde{T}\left(1\right)=\delta\_{\widetilde{T}}\left(1\right)=1. Moreover, T~\widetilde{T} is convex on [0,t0)\left[0,t\_{0}\right), concave on [t0,1]\left[t\_{0},1\right], and increasing on [0,1]\left[0,1\right]. Hence, T~′​(t)≥0\widetilde{T}^{\prime}\left(t\right)\geq 0 for all t∈[0,1]t\in\left[0,1\right], T~′\widetilde{T}^{\prime} is nondecreasing on [0,t0)\left[0,t\_{0}\right), T~′\widetilde{T}^{\prime} attains its maximum T~′​(t0)\widetilde{T}^{\prime}\left(t\_{0}\right) at t0t\_{0}, and T~′\widetilde{T}^{\prime} is nonincreasing on [t0,1]\left[t\_{0},1\right].

Moreover, since T~\widetilde{T} is convex on [0,t0]\left[0,t\_{0}\right] and concave on [t0,1]\left[t\_{0},1\right], there exists some z∗∈[0,1]z^{\*}\in\left[0,1\right], which is unique by strict monotonicity of T~\widetilde{T}, such that δT~​(t)=T~​(t)\delta\_{\widetilde{T}}\left(t\right)=\widetilde{T}\left(t\right) for all t∈[0,z∗]t\in\left[0,z^{\*}\right] and δT~​(t)≠T~​(t)\delta\_{\widetilde{T}}\left(t\right)\neq\widetilde{T}\left(t\right) (i.e., δT~​(t)<T~​(t)\delta\_{\widetilde{T}}\left(t\right)<\widetilde{T}\left(t\right)) for all t∈(z∗,1)t\in\left(z^{\*},1\right). Consequently, z∗<t0z^{\*}<t\_{0}, since otherwise δT~\delta\_{\widetilde{T}} will not be convex on all of the interval [0,1]\left[0,1\right]. Also, δT~\delta\_{\widetilde{T}} is affine on [z∗,1]\left[z^{\*},1\right], of the form a​t+bat+b. Since δT~​(1)=1\delta\_{\widetilde{T}}\left(1\right)=1 and δT~​(z∗)=T~​(z∗)\delta\_{\widetilde{T}}\left(z\_{\*}\right)=\widetilde{T}\left(z\_{\*}\right), it follows that a=1−T~​(z∗)1−z∗a=\frac{1-\widetilde{T}\left(z^{\*}\right)}{1-z^{\*}} and b=1−a=T~​(z∗)−z∗1−z∗b=1-a=\frac{\widetilde{T}\left(z^{\*}\right)-z^{\*}}{1-z^{\*}}. Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | δT~​(t)={T~​(t)if t∈[0,z∗];(1−T~​(z∗)1−z∗)​t+(T~​(z∗)−z∗1−z∗)=T~​(z∗)+(T~​(z∗)−1z∗−1)​(t−z∗)if t∈[z∗,1].\delta\_{\widetilde{T}}\left(t\right)=\left\{\begin{array}[]{l l}\widetilde{T}\left(t\right)&\quad\mbox{if $t\in\left[0,z^{\*}\right]$;}\\ \left(\frac{1-\widetilde{T}\left(z^{\*}\right)}{1-z^{\*}}\right)t+\left(\frac{\widetilde{T}\left(z^{\*}\right)-z^{\*}}{1-z^{\*}}\right)=\widetilde{T}\left(z^{\*}\right)+\left(\frac{\widetilde{T}\left(z^{\*}\right)-1}{z^{\*}-1}\right)\left(t-z^{\*}\right)&\quad\mbox{if $t\in\left[z^{\*},1\right]$.}\\ \end{array}\right. |  | (B.1) |

Let z0∈[0,1)z\_{0}\in\left[0,1\right) be defined by

|  |  |  |
| --- | --- | --- |
|  | z0:=inf{z∈[0,1):T~​(t)>T~​(z)+(1−T~​(z)1−z)​(t−z), for all ​t∈(z,1)}.z\_{0}:=\inf\left\{z\in\left[0,1\right):\widetilde{T}\left(t\right)>\widetilde{T}\left(z\right)+\left(\frac{1-\widetilde{T}\left(z\right)}{1-z}\right)\left(t-z\right),\hbox{ for all }t\in(z,1)\right\}. |  |

Since T~\widetilde{T} is strictly concave on (t0,1)\left(t\_{0},1\right), the line segment connecting any two points (t1,T~​(t1))(t\_{1},\widetilde{T}\left(t\_{1}\right)) and (t2,T~​(t2))(t\_{2},\widetilde{T}\left(t\_{2}\right)), for t1,t2∈[t0,1]t\_{1},t\_{2}\in\left[t\_{0},1\right] with t1<t2t\_{1}<t\_{2}, lies below the graph of T~\widetilde{T} (the epigraph of −T~-\widetilde{T} on the interval [t0,1]\left[t\_{0},1\right] is a convex set). In particular, for t1=t0t\_{1}=t\_{0} and t2=1t\_{2}=1, we have that for all t∈(t0,1)t\in(t\_{0},1),

|  |  |  |
| --- | --- | --- |
|  | T~​(t)>T~​(t0)+(T~​(1)−T~​(t0)1−t0)​(t−t0)=T~​(t0)+(1−T~​(t0)1−t0)​(t−t0).\widetilde{T}\left(t\right)>\widetilde{T}\left(t\_{0}\right)+\left(\frac{\widetilde{T}\left(1\right)-\widetilde{T}\left(t\_{0}\right)}{1-t\_{0}}\right)\left(t-t\_{0}\right)=\widetilde{T}\left(t\_{0}\right)+\left(\frac{1-\widetilde{T}\left(t\_{0}\right)}{1-t\_{0}}\right)\left(t-t\_{0}\right). |  |

Therefore, t0≥z0t\_{0}\geq z\_{0}, by definition of z0z\_{0}.

Now, let z1:=inf{z∈[0,1):T~′​(z)≥1−T~​(z)1−z}.z\_{1}:=\inf\left\{z\in[0,1):\widetilde{T}^{\prime}(z)\geq\frac{1-\widetilde{T}\left(z\right)}{1-z}\right\}. Define the subsets 𝒜,ℬ⊂[0,1]\mathcal{A},\mathcal{B}\subset\left[0,1\right] by

|  |  |  |
| --- | --- | --- |
|  | 𝒜:={z:T~​(t)>T~​(z)+1−T~​(z)1−z​(t−z),∀t∈(z,1)}, and ℬ:={z:T~′​(z)≥1−T~​(z)1−z}.\displaystyle\mathcal{A}:=\left\{z:\widetilde{T}\left(t\right)>\widetilde{T}\left(z\right)+\frac{1-\widetilde{T}\left(z\right)}{1-z}\left(t-z\right),\forall t\in(z,1)\right\},\quad\textnormal{ and }\quad\mathcal{B}:=\left\{z:\widetilde{T}^{\prime}\left(z\right)\geq\frac{1-\widetilde{T}\left(z\right)}{1-z}\right\}. |  |

Since TT is continuously differentiable on [0,1], so is T~\widetilde{T}, and so for every z∈𝒜z\in\mathcal{A},

|  |  |  |
| --- | --- | --- |
|  | T~′​(z)=limt→z​T~​(t)−T~​(z~)t−z=limt↓z​T~​(t)−T~​(z~)t−z≥1−T~​(z)1−z,\widetilde{T}^{\prime}\left(z\right)=\underset{t\to z}{\lim}\,\frac{\widetilde{T}\left(t\right)-\widetilde{T}\left(\widetilde{z}\right)}{t-z}=\underset{t\downarrow z}{\lim}\,\frac{\widetilde{T}\left(t\right)-\widetilde{T}\left(\widetilde{z}\right)}{t-z}\geq\frac{1-\widetilde{T}\left(z\right)}{1-z}, |  |

implying that 𝒜⊆ℬ\mathcal{A}\subseteq\mathcal{B}. If 𝒜⊊ℬ\mathcal{A}\subsetneq\mathcal{B}, there exists z~\widetilde{z} such that T~​(t)>T~​(z~)+(1−T~​(z~)1−z~)​(t−z~)\widetilde{T}\left(t\right)>\widetilde{T}(\widetilde{z})+(\frac{1-\widetilde{T}\left(\widetilde{z}\right)}{1-\widetilde{z}})\left(t-\widetilde{z}\right), for all t∈(z~,1)t\in(\widetilde{z},1), and T~′​(z~)<1−T~​(z~)1−z~\widetilde{T}^{\prime}\left(\widetilde{z}\right)<\frac{1-\widetilde{T}\left(\widetilde{z}\right)}{1-\widetilde{z}}, implying that T~′​(z~)≥1−T~​(z~)1−z~\widetilde{T}^{\prime}\left(\widetilde{z}\right)\geq\frac{1-\widetilde{T}\left(\widetilde{z}\right)}{1-\widetilde{z}} and T~′​(z~)<1−T~​(z~)1−z~\widetilde{T}^{\prime}\left(\widetilde{z}\right)<\frac{1-\widetilde{T}\left(\widetilde{z}\right)}{1-\widetilde{z}}, a contradiction. Therefore, 𝒜=ℬ\mathcal{A}=\mathcal{B}, and so z0=z1z\_{0}=z\_{1}.

We next show that z∗=z0=z1z^{\*}=z\_{0}=z\_{1}. Suppose, by way of contradiction, that z∗≠z0z^{\*}\neq z\_{0}. If z∗<z0z^{\*}<z\_{0}, then there exists some m∈(z∗,1)m\in(z^{\*},1) such that T~​(m)≤T~​(z∗)+(1−T~​(z∗)1−z∗)​(m−z∗)=δT~∗​(m)\widetilde{T}\left(m\right)\leq\widetilde{T}\left(z^{\*}\right)+(\frac{1-\widetilde{T}(z^{\*})}{1-z^{\*}})\left(m-z^{\*}\right)=\delta\_{\widetilde{T}}^{\*}(m), contradicting the fact that δT~​(t)<T~​(t)\delta\_{\widetilde{T}}\left(t\right)<\widetilde{T}\left(t\right), for all t∈(z∗,1)t\in\left(z^{\*},1\right). Now, suppose that z∗>z0=z1z^{\*}>z\_{0}=z\_{1}, and fix some z¯∈(z0,z∗)\bar{z}\in(z\_{0},z^{\*}). Then T~​(z¯)=δT~​(z¯)\widetilde{T}(\bar{z})=\delta\_{\widetilde{T}}(\bar{z}), T~′​(z¯)≥1−T~​(z¯)1−z¯\widetilde{T}^{\prime}\left(\bar{z}\right)\geq\frac{1-\widetilde{T}\left(\bar{z}\right)}{1-\bar{z}}, and T~​(t)>T~​(z¯)+(1−T~​(z¯)1−z¯)​(t−z¯)\widetilde{T}\left(t\right)>\widetilde{T}\left(\bar{z}\right)+(\frac{1-\widetilde{T}\left(\bar{z}\right)}{1-\bar{z}})(t-\bar{z}), for all t∈(z¯,1)t\in(\bar{z},1). In particular,

|  |  |  |
| --- | --- | --- |
|  | δT~​(z∗)=T~​(z∗)>T~​(z¯)+(1−T~​(z¯)1−z¯)​(z∗−z¯)=δT~​(z¯)+(1−δT~​(z¯)1−z¯)​(z∗−z¯).\delta\_{\widetilde{T}}(z^{\*})=\widetilde{T}\left(z^{\*}\right)>\widetilde{T}\left(\bar{z}\right)+\left(\frac{1-\widetilde{T}\left(\bar{z}\right)}{1-\bar{z}}\right)\left(z^{\*}-\bar{z}\right)=\delta\_{\widetilde{T}}(\bar{z})+\left(\frac{1-\delta\_{\widetilde{T}}(\bar{z})}{1-\bar{z}}\right)\left(z^{\*}-\bar{z}\right). |  |

However, since δT~\delta\_{\widetilde{T}} is convex on [0,1][0,1], it lies below the line segment connecting the points (z¯,δT~​(z¯))\left(\bar{z},\delta\_{\widetilde{T}}(\bar{z})\right) and (1,δT~​(1))=(1,1)\left(1,\delta\_{\widetilde{T}}(1)\right)=\left(1,1\right). Therefore,

|  |  |  |
| --- | --- | --- |
|  | δT~​(z∗)≤δT~​(z¯)+(1−δT~​(z¯)1−z¯)​(z∗−z¯),\delta\_{\widetilde{T}}(z^{\*})\leq\delta\_{\widetilde{T}}(\bar{z})+\left(\frac{1-\delta\_{\widetilde{T}}(\bar{z})}{1-\bar{z}}\right)\left(z^{\*}-\bar{z}\right), |  |

a contradiction. Hence, z∗=z0=z1z^{\*}=z\_{0}=z\_{1}, and so δT~\delta\_{\widetilde{T}} is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δT~​(t)={T~​(t)if t∈[0,z0];T~​(z0)+(1−T~​(z0)1−z0)​(t−z0)if t∈[z0,1].\delta\_{\widetilde{T}}\left(t\right)=\left\{\begin{array}[]{l l}\widetilde{T}\left(t\right)&\quad\mbox{if $t\in\left[0,z\_{0}\right]$;}\\ \widetilde{T}\left(z\_{0}\right)+\left(\frac{1-\widetilde{T}\left(z\_{0}\right)}{1-z\_{0}}\right)\left(t-z\_{0}\right)&\quad\mbox{if $t\in\left[z\_{0},1\right]$.}\\ \end{array}\right. |  | (B.2) |

Finally, since δT~\delta\_{\widetilde{T}} is convex on the interval [0,1]\left[0,1\right], the line segment connecting the two points (0,δT~​(0))=(0,0)\left(0,\delta\_{\widetilde{T}}\left(0\right)\right)=\left(0,0\right) and (0,δT~​(1))=(1,1)\left(0,\delta\_{\widetilde{T}}\left(1\right)\right)=\left(1,1\right) lies above the graph of δT~\delta\_{\widetilde{T}}. However, this line segment is the graph of the identity function on [0,1]\left[0,1\right]. Consequently, δT~​(t)≤t\delta\_{\widetilde{T}}\left(t\right)\leq t, for all t∈[0,1]t\in\left[0,1\right]. In particular, since T~​(z0)=δT~​(z0)\widetilde{T}\left(z\_{0}\right)=\delta\_{\widetilde{T}}\left(z\_{0}\right) by eq. ([B.2](#A2.E2 "In Appendix B Proofs for Section 4 ‣ Betting under Common Beliefs: The Effect of Probability Weighting")), we have T~​(z0)≤z0\widetilde{T}\left(z\_{0}\right)\leq z\_{0}.

The proof of the second part of Proposition [4.1](#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting") follows by a symmetric argument.∎

Proof of Proposition [4.2](#S4.Thmtheorem2 "Proposition 4.2 (Inverse S-Shaped Distortion). ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"):
Let 𝚄∼U​n​i​(0,1)\mathtt{U}\sim Uni(0,1). By Theorem [3.7](#S3.Thmtheorem7 "Theorem 3.7. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), we have X1=mλ−1​(δ′​(𝚄)){X}\_{1}=m\_{\lambda}^{-1}(\delta^{\prime}(\mathtt{U})), and by Proposition [4.1](#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), since TT is inverse S-shaped, the convex envelope δ\delta of T~\widetilde{T} satisfies

|  |  |  |
| --- | --- | --- |
|  | δ′​(U)=T~​(p∗)p∗​ 1{U<p∗}+T~′​(p)​ 1{U≥p∗}.\delta^{\prime}(U)=\frac{\widetilde{T}(p^{\*})}{p^{\*}}\,\mathbf{1}\_{\{U<p^{\*}\}}+\widetilde{T}^{\prime}(p)\,\mathbf{1}\_{\{U\geq p^{\*}\}}. |  |

Consequently,

|  |  |  |
| --- | --- | --- |
|  | X1=x0​ 1{U<p∗}+mλ−1​(T~′​(U))​ 1{U≥p∗},X\_{1}=x\_{0}\,\mathbf{1}\_{\{U<p^{\*}\}}+m\_{\lambda}^{-1}\left(\widetilde{T}^{\prime}(U)\right)\,\mathbf{1}\_{\{U\geq p^{\*}\}}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | x0:=mλ−1​(T~​(p∗)p∗).x\_{0}:=m\_{\lambda}^{-1}\,\left(\frac{\widetilde{T}(p^{\*})}{p^{\*}}\right). |  |

Hence, X1X\_{1} has an atom of mass p∗=ℙ​[U<p∗]p^{\*}=\mathbb{P}[U<p^{\*}] at x0x\_{0}. On the event {U≥p∗}\{U\geq p^{\*}\}, define the transformation

|  |  |  |
| --- | --- | --- |
|  | I​(p):=mλ−1​(T~′​(p)),I(p):=m\_{\lambda}^{-1}\left(\widetilde{T}^{\prime}(p)\right), |  |

for p∈[p∗,1]p\in[p^{\*},1], so that

|  |  |  |
| --- | --- | --- |
|  | X1=x0​ 1{U<p∗}+I​(U)​ 1{U≥p∗}.X\_{1}=x\_{0}\,\mathbf{1}\_{\{U<p^{\*}\}}+I\left(U\right)\,\mathbf{1}\_{\{U\geq p^{\*}\}}. |  |

Since T~′\widetilde{T}^{\prime} and mλm\_{\lambda} are strictly increasing, II is strictly increasing and continuously differentiable on [p∗,1][p^{\*},1]. Moreover, for x∈I​([p∗,1])x\in I([p^{\*},1]),

|  |  |  |
| --- | --- | --- |
|  | f1​(x):=fX1​(x)=fI​(U)​(x)=dd​x​ℙ​[I​(U)≤x]=|(I−1)′​(x)|.f\_{1}(x):=f\_{X\_{1}}(x)=f\_{I(U)}(x)=\frac{d}{dx}\mathbb{P}[I(U)\leq x]=\left|(I^{-1})^{\prime}(x)\right|. |  |

Since I−1​(x)=(T~′)−1​(mλ​(x))I^{-1}(x)=(\widetilde{T}^{\prime})^{-1}\left(m\_{\lambda}(x)\right), we have

|  |  |  |
| --- | --- | --- |
|  | (I−1)′​(x)=dd​x​(T~′)−1​(mλ​(x)).(I^{-1})^{\prime}(x)=\frac{d}{dx}(\widetilde{T}^{\prime})^{-1}\left(m\_{\lambda}(x)\right). |  |

Now, strict convexity of T~\widetilde{T} on [p∗,1][p^{\*},1] implies T~′′>0\widetilde{T}^{\prime\prime}>0 on [p∗,1][p^{\*},1]. Monotonicity of mλm\_{\lambda} gives mλ′>0m\_{\lambda}^{\prime}>0. Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | f1​(x)\displaystyle f\_{1}(x) | =|dd​x​(T~′)−1​(mλ​(x))|=|mλ′​(x)T~′′​((T~′)−1​(mλ​(x)))|=mλ′​(x)T~′′​((T~′)−1​(mλ​(x))).\displaystyle=\left|\frac{d}{dx}(\widetilde{T}^{\prime})^{-1}\left(m\_{\lambda}(x)\right)\right|=\left|\frac{m\_{\lambda}^{\prime}(x)}{\widetilde{T}^{\prime\prime}\left((\widetilde{T}^{\prime})^{-1}(m\_{\lambda}(x))\right)}\right|=\frac{m\_{\lambda}^{\prime}(x)}{\widetilde{T}^{\prime\prime}\left((\widetilde{T}^{\prime})^{-1}(m\_{\lambda}(x))\right)}. |  |

Since T~′​(t)=T′​(1−t)\widetilde{T}^{\prime}(t)=T^{\prime}(1-t), we have (T~′)−1​(y)=1−(T′)−1​(y)(\widetilde{T}^{\prime})^{-1}(y)=1-(T^{\prime})^{-1}(y). Therefore,

|  |  |  |
| --- | --- | --- |
|  | T~′′​((T~′)−1​(mλ​(x)))=−T′′​(1−(T~′)−1​(mλ​(x)))=−T′′​((T′)−1​(mλ​(x))),\widetilde{T}^{\prime\prime}\left((\widetilde{T}^{\prime})^{-1}(m\_{\lambda}(x))\right)=-T^{\prime\prime}\left(1-(\widetilde{T}^{\prime})^{-1}(m\_{\lambda}(x))\right)=-T^{\prime\prime}\left((T^{\prime})^{-1}(m\_{\lambda}(x))\right), |  |

and hence

|  |  |  |
| --- | --- | --- |
|  | f1​(x)=−mλ′​(x)T′′​((T′)−1​(mλ​(x))),f\_{1}(x)=\frac{-m\_{\lambda}^{\prime}(x)}{T^{\prime\prime}\left((T^{\prime})^{-1}(m\_{\lambda}(x))\right)}, |  |

for x∈I​([p∗,1])x\in I([p^{\*},1]). ∎

Proof of Corollary [4.3](#S4.Thmtheorem3 "Corollary 4.3. ‣ 4.2. The Case of a Prelec Probability Weighting Function ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"):

(1) By Proposition [4.1](#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting").1, for SS-shaped Prelec distortion functions (α>1\alpha>1), we have
for the first deviation point, p∗​(α)p^{\*}(\alpha), of the convex envelope with respect to T~\widetilde{T} is given by

|  |  |  |
| --- | --- | --- |
|  | p∗​(α)=inf{p∈[0,1):T~′​(p)≥T~​(p)−1p−1},p^{\*}(\alpha)=\inf\left\{p\in[0,1):\widetilde{T}^{\prime}(p)\geq\frac{\widetilde{T}(p)-1}{p-1}\right\}, |  |

where T​(p)=exp⁡(−(−ln⁡(p))α),∀p∈[0,1],T\left(p\right)=\exp\left(-\left(-\ln\left(p\right)\right)^{\alpha}\right),\ \forall p\in[0,1],
with α>1\alpha>1. Then

|  |  |  |
| --- | --- | --- |
|  | T′​(p)=−αp​ln⁡(p)​exp⁡(−(−ln⁡(p))α)​(−ln⁡(p))α≥0,\displaystyle T^{\prime}(p)=\frac{-\alpha}{p\,\ln(p)}\,\exp\left(-\left(-\ln\left(p\right)\right)^{\alpha}\right)\,\left(-\ln(p)\right)^{\alpha}\geq 0, |  |
|  |  |  |
| --- | --- | --- |
|  | T~​(p)=1−exp⁡(−(−ln⁡(1−p))α),\displaystyle\widetilde{T}(p)=1-\exp\left(-\left(-\ln\left(1-p\right)\right)^{\alpha}\right), |  |
|  |  |  |
| --- | --- | --- |
|  | T~′​(p)=−α(1−p)​ln⁡(1−p)​exp⁡(−(−ln⁡(1−p))α)​(−ln⁡(1−p))α\displaystyle\widetilde{T}^{\prime}(p)=\frac{-\alpha}{(1-p)\,\ln(1-p)}\,\exp\left(-\left(-\ln\left(1-p\right)\right)^{\alpha}\right)\,\left(-\ln(1-p)\right)^{\alpha} |  |
|  |  |  |
| --- | --- | --- |
|  | =α1−p​exp⁡(−(−ln⁡(1−p))α)​(−ln⁡(1−p))α−1≥0.\displaystyle\quad\quad=\frac{\alpha}{1-p}\,\exp\left(-\left(-\ln\left(1-p\right)\right)^{\alpha}\right)\,\left(-\ln(1-p)\right)^{\alpha-1}\geq 0. |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | p∗​(α)\displaystyle p^{\*}(\alpha) | =inf{p∈[0,1):α1−p​exp⁡(−(−ln⁡(1−p))α)​(−ln⁡(1−p))α−1≥exp⁡(−(−ln⁡(1−p))α)1−p}.\displaystyle=\inf\left\{p\in[0,1):\frac{\alpha}{1-p}\,\exp\left(-\left(-\ln\left(1-p\right)\right)^{\alpha}\right)\,\left(-\ln(1-p)\right)^{\alpha-1}\geq\frac{\exp\left(-\left(-\ln\left(1-p\right)\right)^{\alpha}\right)}{1-p}\right\}. |  |

For the S-shaped Prelec function that we consider here, the functions T~′​(p)\widetilde{T}^{\prime}(p) and 1−T~​(p)1−p\frac{1-\widetilde{T}(p)}{1-p} cross once, and the point at which they cross is precisely p∗​(α)p^{\*}(\alpha), so that

|  |  |  |
| --- | --- | --- |
|  | T~′​(p∗​(α))=1−T~​(p∗​(α))1−p∗​(α),\widetilde{T}^{\prime}\left(p^{\*}(\alpha)\right)=\frac{1-\widetilde{T}\left(p^{\*}(\alpha)\right)}{1-p^{\*}(\alpha)}, |  |

that is

|  |  |  |
| --- | --- | --- |
|  | α1−p∗​(α)​exp⁡(−(−ln⁡(1−p∗​(α)))α)​(−ln⁡(1−p∗​(α)))α−1=exp⁡(−(−ln⁡(1−p∗​(α)))α)1−p∗​(α),\frac{\alpha}{1-p^{\*}(\alpha)}\,\exp\left(-\left(-\ln\left(1-p^{\*}(\alpha)\right)\right)^{\alpha}\right)\,\left(-\ln(1-p^{\*}(\alpha))\right)^{\alpha-1}=\frac{\exp\left(-\left(-\ln\left(1-p^{\*}(\alpha)\right)\right)^{\alpha}\right)}{1-p^{\*}(\alpha)}, |  |

which yields the desired closed form
p∗​(α)=1−exp⁡(−(1α)1α−1).p^{\*}(\alpha)=1-\exp(-\left(\frac{1}{\alpha}\right)^{\frac{1}{\alpha-1}}).

(2)
By Proposition [4.1](#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1. S-Shaped and Inverse S-Shaped Probability Weighting Functions ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting")(2) for an inverse S-shaped Prelec distortion function, with α<1\alpha<1, we have

|  |  |  |
| --- | --- | --- |
|  | p∗​(α)=sup{p∈[0,1):T~′​(p)≤T~​(p)p}=sup{p∈[0,1):α1−p​exp⁡(−(−ln⁡(1−p))α)​(−ln⁡(1−p))α−1≤1−exp⁡(−(−ln⁡(1−p))α)p}.\begin{split}p^{\*}(\alpha)&=\sup\left\{p\in\left[0,1\right):\widetilde{T}^{\prime}\left(p\right)\leq\frac{\widetilde{T}\left(p\right)}{p}\right\}\\ &=\sup\left\{p\in\left[0,1\right):\frac{\alpha}{1-p}\,\exp\left(-\left(-\ln\left(1-p\right)\right)^{\alpha}\right)\,\left(-\ln(1-p)\right)^{\alpha-1}\leq\frac{1-\exp\left(-\left(-\ln\left(1-p\right)\right)^{\alpha}\right)}{p}\right\}.\\ \end{split} |  |

The functions T~′​(p)\widetilde{T}^{\prime}(p) and T~​(p)p\frac{\widetilde{T}(p)}{p} cross once, and the point at which they cross is precisely p∗​(α)p^{\*}(\alpha), so that
T~′​(p∗​(α))=T~​(p∗​(α))p∗​(α),\widetilde{T}^{\prime}\left(p^{\*}(\alpha)\right)=\frac{\widetilde{T}\left(p^{\*}(\alpha)\right)}{p^{\*}(\alpha)},
that is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | α1−p∗​(α)​exp⁡(−(−ln⁡(1−p∗​(α)))α)​(−ln⁡(1−p∗​(α)))α−1\displaystyle\frac{\alpha}{1-p^{\*}(\alpha)}\,\exp\left(-\left(-\ln\left(1-p^{\*}(\alpha)\right)\right)^{\alpha}\right)\,\left(-\ln(1-p^{\*}(\alpha))\right)^{\alpha-1} |  |
|  |  | =\displaystyle= | 1−exp⁡(−(−ln⁡(1−p∗​(α)))α)p∗​(α).\displaystyle\frac{1-\exp\left(-\left(-\ln\left(1-p^{\*}(\alpha)\right)\right)^{\alpha}\right)}{p^{\*}(\alpha)}. |  |

Now define x=−ln⁡(1−p∗​(α))x=-\ln(1-p^{\*}(\alpha)).
Then we can rewrite 1−p∗​(α)1-p^{\*}(\alpha) as
1−p∗​(α)=e−x1-p^{\*}(\alpha)=e^{-x}.
Rewriting ([B](#A2.Ex26 "Appendix B Proofs for Section 4 ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) in terms of xx yields

|  |  |  |
| --- | --- | --- |
|  | αe−x​e−xα​xα−1=1−e−xα1−e−x⟺α​e−xα​xα−1=1−e−xαex​(1−e−x).\frac{\alpha}{e^{-x}}e^{-x^{\alpha}}x^{\alpha-1}=\frac{1-e^{-x^{\alpha}}}{1-e^{-x}}\Longleftrightarrow\alpha e^{-x^{\alpha}}x^{\alpha-1}=\frac{1-e^{-x^{\alpha}}}{e^{x}(1-e^{-x})}. |  |

Multiplying both sides by ex​(1−e−x)e^{x}(1-e^{-x}) yields α​xα−1​e−xα​ex​(1−e−x)=1−e−xα\alpha x^{\alpha-1}e^{-x^{\alpha}}e^{x}(1-e^{-x})=1-e^{-x^{\alpha}}.
Rearrange to make e−xαe^{-x^{\alpha}} dividing both sides by α​xα−1​ex​(1−e−x)+1\alpha x^{\alpha-1}e^{x}(1-e^{-x})+1 gives

|  |  |  |
| --- | --- | --- |
|  | e−xα=1α​xα−1​ex​(1−e−x)+1,e^{-x^{\alpha}}=\frac{1}{\alpha x^{\alpha-1}e^{x}(1-e^{-x})+1}, |  |

and so:

|  |  |  |
| --- | --- | --- |
|  | xα=−ln⁡(1α​xα−1​ex​(1−e−x)+1)=ln⁡(α​xα−1​ex​(1−e−x)+1).x^{\alpha}=-\ln\left(\frac{1}{\alpha x^{\alpha-1}e^{x}(1-e^{-x})+1}\right)=\ln\left(\alpha x^{\alpha-1}e^{x}(1-e^{-x})+1\right). |  |

This gives an implicit definition for p∗​(α)p^{\*}(\alpha), via x=−ln⁡(1−p∗​(α))x=-\ln(1-p^{\*}(\alpha)), for p∗​(α)=1−e−xp^{\*}(\alpha)=1-e^{-x}. ∎

Proof of Corollary [4.4](#S4.Thmtheorem4 "Corollary 4.4. ‣ 4.3. Closed-Form Solutions for a Prelec RDU Agent ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"):
Note that X1=mλ−1​(δ′​(𝚄))X\_{1}=m^{-1}\_{\lambda}\left(\delta^{\prime}(\mathtt{U})\right), by Theorem [3.7](#S3.Thmtheorem7 "Theorem 3.7. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"). In that case, it holds that uλ​(x)=−1β¯​e−β¯​x​∑i=2nλiu\_{\lambda}(x)=-\frac{1}{\overline{\beta}}e^{-\overline{\beta}x}\sum\_{i=2}^{n}\lambda\_{i}.
We then have mλ​(x)=e(β1+β¯)​x​∑i=2nλim\_{\lambda}(x)=e^{\left(\beta\_{1}+\overline{\beta}\right)x}\sum\_{i=2}^{n}\lambda\_{i} for x∈ℝx\in\mathbb{R}, and so

|  |  |  |
| --- | --- | --- |
|  | mλ−1​(y)=1β1+β¯​(ln⁡(y)−ln⁡(∑i=2nλi)),m^{-1}\_{\lambda}(y)=\frac{1}{\beta\_{1}+\overline{\beta}}\,\left(\ln(y)-\ln(\sum\_{i=2}^{n}\lambda\_{i})\right), |  |

for y>0y>0. In general, mλ−1m\_{\lambda}^{-1} is increasing with limy→0mλ−1​(y)=−∞\lim\_{y\rightarrow 0}m\_{\lambda}^{-1}(y)=-\infty and limy→∞mλ−1​(y)=∞\lim\_{y\rightarrow\infty}m\_{\lambda}^{-1}(y)=\infty.∎

## Appendix C Proofs for Section [5](#S5 "5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting")

Proof of Lemma [5.2](#S5.Thmtheorem2 "Lemma 5.2. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting"):
By the definition of TMT\_{M}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | T~M​(p)=1−TM​(1−p)\displaystyle\widetilde{T}\_{M}\left(p\right)=1-T\_{M}\left(1-p\right) | =1−((1−f​(M))​T​(1−p)+f​(M)​(1−p))\displaystyle=1-\left((1-f(M))T(1-p)+f(M)(1-p)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1−T​(1−p)+f​(M)​T​(1−p)−f​(M)​(1−p)\displaystyle=1-T(1-p)+f(M)T(1-p)-f(M)(1-p) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =T~​(p)−f​(M)​[T~​(p)−p],\displaystyle=\widetilde{T}(p)-f(M)\left[\widetilde{T}(p)-p\right], |  |

and thus T~M′​(p)=T~′​(p)−f​(M)​[T~′​(p)−1]=T~′​(p)​[1−f​(M)]+f​(M)\widetilde{T}\_{M}^{\prime}\left(p\right)=\widetilde{T}^{\prime}(p)-f(M)\left[\widetilde{T}^{\prime}(p)-1\right]=\widetilde{T}^{\prime}(p)\left[1-f(M)\right]+f(M). Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | U1​(X,TM)\displaystyle U\_{1}(X,T\_{M}) | =∫01u1​(FX−1​(p))​T~M′​(p)​d​p\displaystyle=\displaystyle\int\_{0}^{1}u\_{1}\left(F\_{X}^{-1}\left(p\right)\right)\widetilde{T}\_{M}^{\prime}\left(p\right)\,\textnormal{d}p |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01u1​(FX−1​(p))​{T~′​(p)​[1−f​(M)]+f​(M)}​d​p\displaystyle=\displaystyle\int\_{0}^{1}u\_{1}\left(F\_{X}^{-1}\left(p\right)\right)\left\{\widetilde{T}^{\prime}(p)\left[1-f(M)\right]+f(M)\right\}\,\textnormal{d}p |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =[1−f​(M)]​∫01u1​(FX−1​(p))​T~′​(p)​d​p+f​(M)​∫01u1​(FX−1​(p))​d​p\displaystyle=\left[1-f(M)\right]\displaystyle\int\_{0}^{1}u\_{1}\left(F\_{X}^{-1}\left(p\right)\right)\widetilde{T}^{\prime}(p)\,\textnormal{d}p+f(M)\,\displaystyle\int\_{0}^{1}u\_{1}\left(F\_{X}^{-1}\left(p\right)\right)\,\textnormal{d}p |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =[1−f​(M)]​U1​(X,T)+f​(M)​∫u1​(X)​d​ℙ.\displaystyle=\left[1-f(M)\right]\,U\_{1}(X,T)+f(M)\,\int u\_{1}(X)\,\textnormal{d}\mathbb{P}. |  |

∎

Proof of Lemma [5.3](#S5.Thmtheorem3 "Lemma 5.3. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting"):
Note that T:[0,1]→[0,1]T:[0,1]\to[0,1] is increasing, with T​(0)=0T(0)=0 and T​(1)=1T(1)=1. Define T~:[0,1]→[0,1]\widetilde{T}:[0,1]\to[0,1] by T~​(t):=1−T​(1−t)\widetilde{T}(t):=1-T(1-t). For f​(M)∈[0,1]f(M)\in[0,1], recall that TM:[0,1]→[0,1]T\_{M}:[0,1]\to[0,1] is defined by TM​(t):=(1−f​(M))​T​(t)+f​(M)​tT\_{M}(t):=\left(1-f(M)\right)\,T(t)+f(M)\,t, and T~M:[0,1]→[0,1]\widetilde{T}\_{M}:[0,1]\to[0,1] is given by

|  |  |  |
| --- | --- | --- |
|  | T~M​(t):=1−TM​(1−t)=(1−f​(M))​T~​(t)+f​(M)​t.\widetilde{T}\_{M}(t):=1-T\_{M}(1-t)=\left(1-f(M)\right)\,\widetilde{T}(t)+f(M)\,t. |  |

Recall that the convex envelope δ\delta of T~\widetilde{T} on [0,1][0,1] is defined as the largest convex function that satisfies δ​(t)≤T~​(t)\delta(t)\leq\widetilde{T}(t), for all t∈[0,1]t\in[0,1]:

|  |  |  |
| --- | --- | --- |
|  | δ​(t)=sup{h​(t):h​ is convex on ​[0,1],h​(t)≤T~​(t),∀t∈[0,1]}.\delta(t)=\sup\,\left\{h(t):h\hbox{ is convex on }[0,1],\ h(t)\leq\widetilde{T}(t),\ \forall\,t\in[0,1]\right\}. |  |

Similarly, δM\delta\_{M} is the convex envelope of T~M\widetilde{T}\_{M}. Define the function gg on [0,1][0,1] by

|  |  |  |
| --- | --- | --- |
|  | g​(t):=(1−f​(M))​δ​(t)+f​(M)​t.g(t):=\left(1-f(M)\right)\,\delta(t)+f(M)\,t. |  |

We show that g=δMg=\delta\_{M} by showing that gg satisfies the definition of the convex envelope of T~M\widetilde{T}\_{M}.

gg is convex: Since f​(M)∈[0,1]f(M)\in[0,1], gg is a convex combination of the convex function δ\delta, and the affine (hence convex) function t↦tt\mapsto t. A convex combination of convex functions is convex, and therefore gg is convex on [0,1][0,1].

g≤T~Mg\leq\widetilde{T}\_{M} on [0,1][0,1]: For any t∈[0,1]t\in[0,1], we have δ​(t)≤T~​(t)\delta(t)\leq\widetilde{T}(t), by the definition of the convex envelope. Since f​(M)∈[0,1]f(M)\in[0,1], it follows that

|  |  |  |
| --- | --- | --- |
|  | g​(t)=(1−f​(M))​δ​(t)+f​(M)​t≤(1−f​(M))​T~​(t)+f​(M)​t=T~M​(t).g(t)=\left(1-f(M)\right)\,\delta(t)+f(M)\,t\leq\left(1-f(M)\right)\,\widetilde{T}(t)+f(M)\,t=\widetilde{T}\_{M}(t). |  |

gg is maximal: For any convex function h:[0,1]→ℝh:[0,1]\to\mathbb{R} with h≤T~Mh\leq\widetilde{T}\_{M} on [0,1][0,1], we have h≤gh\leq g.

(1) If f​(M)<1f(M)<1: Define the function h0h\_{0} by

|  |  |  |
| --- | --- | --- |
|  | h0​(t):=h​(t)−f​(M)​t1−f​(M).h\_{0}(t):=\frac{h(t)-f(M)\,t}{1-f(M)}. |  |

We claim that h0h\_{0} is convex and h0≤T~h\_{0}\leq\widetilde{T} on [0,1][0,1].

1. (a)

   h0h\_{0} is convex:
   For any t1,t2∈[0,1]t\_{1},t\_{2}\in[0,1] and λ∈[0,1]\lambda\in[0,1], the convexity of hh gives

   |  |  |  |
   | --- | --- | --- |
   |  | h​(λ​t1+(1−λ)​t2)≤λ​h​(t1)+(1−λ)​h​(t2).h(\lambda t\_{1}+(1-\lambda)t\_{2})\leq\lambda\,h(t\_{1})+(1-\lambda)\,h(t\_{2}). |  |

   Let tλ:=λ​t1+(1−λ)​t2t\_{\lambda}:=\lambda t\_{1}+(1-\lambda)t\_{2}. Then

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | h0​(tλ)=h​(tλ)−f​(M)​tλ1−f​(M)\displaystyle h\_{0}(t\_{\lambda})=\frac{h(t\_{\lambda})-f(M)\,t\_{\lambda}}{1-f(M)} | ≤λ​h​(t1)+(1−λ)​h​(t2)−f​(M)​(λ​t1+(1−λ)​t2)1−f​(M)\displaystyle\leq\frac{\lambda\,h(t\_{1})+(1-\lambda)\,h(t\_{2})-f(M)(\lambda t\_{1}+(1-\lambda)\,t\_{2})}{1-f(M)} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =λ​[h​(t1)−f​(M)​t1]+(1−λ)​[h​(t2)−f​(M)​t2]1−f​(M)\displaystyle=\frac{\lambda\,[h(t\_{1})-f(M)\,t\_{1}]+(1-\lambda)\,[h(t\_{2})-f(M)\,t\_{2}]}{1-f(M)} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =λ​h0​(t1)+(1−λ)​h0​(t2),\displaystyle=\lambda\,h\_{0}(t\_{1})+(1-\lambda)\,h\_{0}(t\_{2}), |  |

   and hence h0h\_{0} is convex.
2. (b)

   h0≤T~h\_{0}\leq\widetilde{T} on [0,1][0,1]:
   Since h≤T~Mh\leq\widetilde{T}\_{M} by hypothesis, we have for all t∈[0,1]t\in[0,1],

   |  |  |  |
   | --- | --- | --- |
   |  | h​(t)≤T~M​(t)=(1−f​(M))​T~​(t)+f​(M)​t,h(t)\leq\widetilde{T}\_{M}(t)=\left(1-f(M)\right)\,\widetilde{T}(t)+f(M)\,t, |  |

   and hence
   h​(t)−f​(M)​t≤(1−f​(M))​T~​(t).h(t)-f(M)\,t\leq\left(1-f(M)\right)\,\widetilde{T}(t). Since 1−f​(M)>01-f(M)>0, it follows that

   |  |  |  |
   | --- | --- | --- |
   |  | h0​(t)=h​(t)−f​(M)​t1−f​(M)≤T~​(t).h\_{0}(t)=\frac{h(t)-f(M)t}{1-f(M)}\leq\widetilde{T}(t). |  |

By (a) and (b), the maximality of the convex envelope δ\delta implies that h0≤δh\_{0}\leq\delta on [0,1][0,1]. Therefore,

|  |  |  |
| --- | --- | --- |
|  | h​(t)=(1−f​(M))​h0​(t)+f​(M)​t≤(1−f​(M))​δ​(t)+f​(M)​t=g​(t).h(t)=\left(1-f(M)\right)\,h\_{0}(t)+f(M)\,t\leq\left(1-f(M)\right)\,\delta(t)+f(M)\,t=g(t). |  |

(2) If f​(M)=1f(M)=1:
In this case, T~M​(t)=t\widetilde{T}\_{M}(t)=t and g​(t)=tg(t)=t. Since t↦tt\mapsto t is convex and equals T~M\widetilde{T}\_{M}, we have δM​(t)=t=g​(t)\delta\_{M}(t)=t=g(t).

Consequently, gg is the largest convex function bounded above by T~M\widetilde{T}\_{M}, which means that g=δMg=\delta\_{M}.

Finally, since T~\widetilde{T} is bounded on [0,1][0,1] and δ\delta is its convex envelope,
δ\delta is finite and convex on [0,1][0,1], with δ​(0)=T~​(0)=0\delta(0)=\widetilde{T}(0)=0 and δ​(1)=T~​(1)=1\delta(1)=\widetilde{T}(1)=1. Any finite convex function on a compact interval is locally Lipschitz continuous on the interior of its domain, and hence absolutely continuous on every compact subinterval of (0,1)(0,1). In particular, δ\delta is absolutely continuous on (0,1)(0,1) and therefore differentiable a.e. on (0,1)(0,1). Now, since δM​(t)=(1−f​(M))​δ​(t)+f​(M)​t\delta\_{M}(t)=(1-f(M))\,\delta(t)+f(M)\,t, δM\delta\_{M} is also finite and convex on [0,1][0,1], and it is absolutely continuous on (0,1)(0,1). Linearity of differentiation under scaling and addition then yields δM′​(t)=(1−f​(M))​δ′​(t)+f​(M)\delta\_{M}^{\prime}(t)=(1-f(M))\,\delta^{\prime}(t)+f(M), for a.e. t∈(0,1)t\in(0,1). □\square

Proof of Proposition [5.4](#S5.Thmtheorem4 "Proposition 5.4. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting"):

(1) For a given effort level MM, applying Theorem [3.7](#S3.Thmtheorem7 "Theorem 3.7. ‣ 3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting") to the two-agent economy with aggregate endowment 𝚠−M\mathtt{w}-M, the allocation 𝐗M\mathbf{X}^{M} solves Problem ([5.4](#S5.E4 "In 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) if and only if

|  |  |  |
| --- | --- | --- |
|  | X1M=mλ2−1​(δM′​(𝚄))andX2M=𝚠−M−X1M,\displaystyle X\_{1}^{M}=m^{-1}\_{\lambda\_{2}}\left(\delta\_{M}^{\prime}(\mathtt{U})\right)\ \ \hbox{and}\ \ X\_{2}^{M}=\mathtt{w}-M-{X}\_{1}^{M}, |  |

where mλ2​(x):=λ2​u2′​(𝚠−M−x)u1′​(x)m\_{\lambda\_{2}}(x):=\lambda\_{2}\,\frac{u\_{2}^{\prime}\left(\mathtt{w}-M-x\right)}{u\_{1}^{\prime}\left(x\right)}. By Lemma [5.3](#S5.Thmtheorem3 "Lemma 5.3. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting"), we have

|  |  |  |
| --- | --- | --- |
|  | δM′​(t)=(1−f​(M))​δ′​(t)+f​(M)=δ′​(t)−f​(M)​[δ′​(t)−1],\delta\_{M}^{\prime}(t)=(1-f(M))\,\delta^{\prime}(t)+f(M)=\delta^{\prime}(t)-f(M)\left[\delta^{\prime}(t)-1\right], |  |

for a.e. t∈(0,1)t\in(0,1). Consequently,

|  |  |  |
| --- | --- | --- |
|  | X1M=mλ2−1​(δ′​(U)−f​(M)​[δ′​(U)−1]).X\_{1}^{M}=m\_{\lambda\_{2}}^{-1}\left(\delta^{\prime}(U)-f(M)\left[\delta^{\prime}(U)-1\right]\right). |  |

(2) Note that the function mλ2​(x)=λ2​u2′​(𝚠−M−x)u1′​(x)m\_{\lambda\_{2}}(x)=\lambda\_{2}\,\frac{u\_{2}^{\prime}(\mathtt{w}-M-x)}{u\_{1}^{\prime}(x)} depends explicitly on MM. Consequently, its inverse mλ2−1m\_{\lambda\_{2}}^{-1} also depends on MM. To emphasize this dependence, we write mλ2​(X1M;M)=ϕ​(M)m\_{\lambda\_{2}}\left(X\_{1}^{M};M\right)=\phi(M), where ϕ​(M):=δ′​(U)−f​(M)​(δ′​(U)−1)\phi(M):=\delta^{\prime}(U)-f(M)\left(\delta^{\prime}(U)-1\right). The chain rule gives

|  |  |  |
| --- | --- | --- |
|  | ϕ′​(M)=∂∂X1M​mλ2​(X1M;M)​∂X1M∂M+∂∂M​mλ2​(X1M;M).\phi^{\prime}(M)=\frac{\partial}{\partial X\_{1}^{M}}\,m\_{\lambda\_{2}}\left(X\_{1}^{M};M\right)\,\frac{\partial X\_{1}^{M}}{\partial M}+\frac{\partial}{\partial M}\,m\_{\lambda\_{2}}\left(X\_{1}^{M};M\right). |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | ∂X1M∂M=ϕ′​(M)−∂∂M​mλ2​(X1M;M)∂∂X1M​mλ2​(X1M;M).\frac{\partial X\_{1}^{M}}{\partial M}=\frac{\phi^{\prime}(M)-\frac{\partial}{\partial M}\,m\_{\lambda\_{2}}\left(X\_{1}^{M};M\right)}{\frac{\partial}{\partial X\_{1}^{M}}\,m\_{\lambda\_{2}}\left(X\_{1}^{M};M\right)}. |  |

Since

|  |  |  |
| --- | --- | --- |
|  | ϕ′​(M)=−f′​(M)​(δ′​(U)−1)and∂∂M​mλ2​(X1M;M)=λ2​−u2′′​(𝚠−M−x)u1′​(x),\phi^{\prime}(M)=-f^{\prime}(M)\left(\delta^{\prime}(U)-1\right)\ \ \hbox{and}\ \ \frac{\partial}{\partial M}\,m\_{\lambda\_{2}}\left(X\_{1}^{M};M\right)=\lambda\_{2}\,\frac{-u\_{2}^{\prime\prime}(\mathtt{w}-M-x)}{u\_{1}^{\prime}(x)}, |  |

we obtain

|  |  |  |
| --- | --- | --- |
|  | ∂X1M∂M=−f′​(M)​(δ′​(U)−1)+λ2​u2′′​(𝚠−M−X1M)u1′​(X1M)∂∂X1M​mλ2​(X1M;M).\frac{\partial X\_{1}^{M}}{\partial M}=\frac{-f^{\prime}(M)\left(\delta^{\prime}(U)-1\right)+\lambda\_{2}\,\dfrac{u\_{2}^{\prime\prime}(\mathtt{w}-M-X\_{1}^{M})}{u\_{1}^{\prime}(X\_{1}^{M})}}{\frac{\partial}{\partial X\_{1}^{M}}\,m\_{\lambda\_{2}}\left(X\_{1}^{M};M\right)}. |  |

Writing X1M=mλ2−1​(ϕ​(M))X\_{1}^{M}=m\_{\lambda\_{2}}^{-1}(\phi(M)) and Λ​(x):=dd​x​mλ2​(mλ2−1​(x))\Lambda(x):=\frac{d}{dx}m\_{\lambda\_{2}}\big(m\_{\lambda\_{2}}^{-1}(x)\big), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂X1M∂M\displaystyle\frac{\partial X\_{1}^{M}}{\partial M} | =−f′​(M)​(δ′​(U)−1)+λ2​u2′′​(𝚠−M−mλ2−1​(ϕ​(M)))u1′​(mλ2−1​(ϕ​(M)))Λ​(ϕ​(M))\displaystyle=\frac{-f^{\prime}(M)\left(\delta^{\prime}(U)-1\right)+\lambda\_{2}\,\dfrac{u\_{2}^{\prime\prime}\left(\mathtt{w}-M-m\_{\lambda\_{2}}^{-1}(\phi(M))\right)}{u\_{1}^{\prime}\left(m\_{\lambda\_{2}}^{-1}(\phi(M))\right)}}{\Lambda(\phi(M))} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−f′​(M)​(δ′​(U)−1)+λ2​u2′′​(𝚠−M−mλ2−1​(δ′​(U)−f​(M)​(δ′​(U)−1)))u1′​(mλ2−1​(δ′​(U)−f​(M)​(δ′​(U)−1)))Λ​(δ′​(U)−f​(M)​(δ′​(U)−1)).\displaystyle=\frac{-f^{\prime}(M)\left(\delta^{\prime}(U)-1\right)+\lambda\_{2}\,\dfrac{u\_{2}^{\prime\prime}\left(\mathtt{w}-M-m\_{\lambda\_{2}}^{-1}\left(\delta^{\prime}(U)-f(M)\left(\delta^{\prime}(U)-1\right)\right)\right)}{u\_{1}^{\prime}\left(m\_{\lambda\_{2}}^{-1}\left(\delta^{\prime}(U)-f(M)\left(\delta^{\prime}(U)-1\right)\right)\right)}}{\Lambda\left(\delta^{\prime}(U)-f(M)\left(\delta^{\prime}(U)-1\right)\right)}. |  |

Finally, since

|  |  |  |
| --- | --- | --- |
|  | dd​x​mλ2​(x)=λ2​[−u2′′​(𝚠−M−x)u1′​(x)−u2′​(𝚠−M−x)​u1′′​(x)(u1′​(x))2],\frac{d}{dx}m\_{\lambda\_{2}}(x)=\lambda\_{2}\left[\frac{-u\_{2}^{\prime\prime}(\mathtt{w}-M-x)}{u\_{1}^{\prime}(x)}-\frac{u\_{2}^{\prime}(\mathtt{w}-M-x)\,u\_{1}^{\prime\prime}(x)}{(u\_{1}^{\prime}(x))^{2}}\right], |  |

it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ​(x)\displaystyle\Lambda(x) | =λ2​[−u2′′​(𝚠−M−mλ2−1​(x))u1′​(mλ2−1​(x))−u2′​(𝚠−M−mλ2−1​(x))​u1′′​(mλ2−1​(x))(u1′​(mλ2−1​(x)))2]\displaystyle=\lambda\_{2}\left[\frac{-u\_{2}^{\prime\prime}\,\big(\mathtt{w}-M-m\_{\lambda\_{2}}^{-1}(x)\big)}{u\_{1}^{\prime}\,\big(m\_{\lambda\_{2}}^{-1}(x)\big)}-\frac{u\_{2}^{\prime}\,\big(\mathtt{w}-M-m\_{\lambda\_{2}}^{-1}(x)\big)\,u\_{1}^{\prime\prime}\,\big(m\_{\lambda\_{2}}^{-1}(x)\big)}{\Big(u\_{1}^{\prime}\,\big(m\_{\lambda\_{2}}^{-1}(x)\big)\Big)^{2}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−λ2u1′​(mλ2−1​(x))​[u2′′​(𝚠−M−mλ2−1​(x))+u2′​(𝚠−M−mλ2−1​(x))​u1′′​(mλ2−1​(x))u1′​(mλ2−1​(x))].\displaystyle=\frac{-\lambda\_{2}}{u\_{1}^{\prime}\left(m\_{\lambda\_{2}}^{-1}(x)\right)}\left[u\_{2}^{\prime\prime}\left(\mathtt{w}-M-m\_{\lambda\_{2}}^{-1}(x)\right)+u\_{2}^{\prime}\left(\mathtt{w}-M-m\_{\lambda\_{2}}^{-1}(x)\right)\frac{u\_{1}^{\prime\prime}\left(m\_{\lambda\_{2}}^{-1}(x)\right)}{u\_{1}^{\prime}\left(m\_{\lambda\_{2}}^{-1}(x)\right)}\right]. |  |

∎

Proof of Theorem [5.5](#S5.Thmtheorem5 "Theorem 5.5. ‣ 5. Nudging the RDU agent ‣ Betting under Common Beliefs: The Effect of Probability Weighting"):
The welfare maximization with a control on MM is formally given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxM∈[0,𝚠]​supX1+X2=𝚠−M[U1​(X1,TM)+U2​(X2)]=maxM∈[0,𝚠]​supX∈𝒳[U1​(X,TM)+U2​(𝚠−M−X)].\displaystyle\max\_{M\in[0,\mathtt{w}]}\,\sup\_{X\_{1}+X\_{2}=\mathtt{w}-M}\left[U\_{1}(X\_{1},T\_{M})+U\_{2}(X\_{2})\right]=\max\_{M\in[0,\mathtt{w}]}\,\sup\_{X\in\mathcal{X}}\,\left[U\_{1}(X,T\_{M})+U\_{2}(\mathtt{w}-M-X)\right]. |  | (C.1) |

For a given effort level MM, the optimal risk sharing rule (XM,𝚠−M−XM)(X\_{M},\mathtt{w}-M-X\_{M}) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​(XM,M)\displaystyle W(X\_{M},M) | =maxX⁡{U1​(X,TM)+U2​(𝚠−M−X)}\displaystyle=\max\_{X}\left\{U\_{1}(X,T\_{M})+U\_{2}(\mathtt{w}-M-X)\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =U1​(XM,TM)+U2​(𝚠−M−XM)\displaystyle=U\_{1}(X\_{M},T\_{M})+U\_{2}(\mathtt{w}-M-X\_{M}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1−f​(M))​U1​(XM,T)+Eℙ​[f​(M)​u1​(XM)+u2​(𝚠−M−XM)].\displaystyle=\left(1-f(M)\right)\,U\_{1}(X\_{M},T)+\,E^{\mathbb{P}}\left[f(M)u\_{1}(X\_{M})+u\_{2}(\mathtt{w}-M-X\_{M})\right]. |  |

To find the optimal monetary value M∗M^{\*}, we need to find the maximum of M↦W​(XM,M)M\mapsto W(X\_{M},M), by taking first order conditions ∂∂M​W​(XM,M)=0\frac{\partial}{\partial M}\,W(X^{M},M)=0. To do so, we first rewrite W​(XM,M)W(X^{M},M) and then compute ∂∂M​W​(XM,M)\frac{\partial}{\partial M}\,W(X^{M},M). Recall that TM​(t)=(1−f​(M))​T​(t)+f​(M)​t,T\_{M}(t)=(1-f(M))\,T(t)+f(M)\,t,
so that

|  |  |  |
| --- | --- | --- |
|  | T~M​(t)=1−(1−f​(M))​T​(1−t)−f​(M)​(1−t)andT~M′​(t)=f​(M)+(1−f​(M))​T~′​(t).\displaystyle\widetilde{T}\_{M}(t)=1-(1-f(M))\,T(1-t)-f(M)\,(1-t)\quad\textnormal{and}\quad\widetilde{T}\_{M}^{\prime}(t)=f(M)+(1-f(M))\,\widetilde{T}^{\prime}(t). |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | W​(XM,M)\displaystyle W(X^{M},M) | =(1−f​(M))​U1​(XM,T)+Eℙ​[f​(M)​u1​(XM)+u2​(𝚠−M−XM)]\displaystyle=\left(1-f(M)\right)\,U\_{1}(X\_{M},T)+\,E^{\mathbb{P}}[f(M)u\_{1}(X\_{M})+u\_{2}(\mathtt{w}-M-X\_{M})] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1−f​(M))​∫u1​(XM)​𝑑T∘ℙ+∫[f​(M)​u1​(XM)+u2​(𝚠−M−XM)]​𝑑ℙ\displaystyle=\left(1-f(M)\right)\,\int u\_{1}(X\_{M})\,dT\circ\mathbb{P}\,+\,\int[f(M)\,u\_{1}(X\_{M})+u\_{2}(\mathtt{w}-M-X\_{M})]\,d\mathbb{P} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1−f​(M))​∫01u1​(FXM−1​(t))​T′​(1−t)​𝑑t+f​(M)​∫01u1​(FXM−1​(t))​𝑑t+∫01u2​(F𝚠−M−XM−1​(t))​𝑑t\displaystyle=\left(1-f(M)\right)\,\int\_{0}^{1}u\_{1}(F\_{X\_{M}}^{-1}(t))\,T^{\prime}(1-t)\,dt\,+\,f(M)\,\int\_{0}^{1}u\_{1}(F\_{X\_{M}}^{-1}(t))\,dt+\int\_{0}^{1}u\_{2}(F^{-1}\_{\mathtt{w}-M-X\_{M}}(t))\,dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01[(1−f​(M))​u1​(xM​(t))​T~′​(t)+f​(M)​u1​(xM​(t))+u2​(𝚠−M−xM​(1−t))]​𝑑t.\displaystyle=\int\_{0}^{1}\left[(1-f(M))\,u\_{1}(x\_{M}(t))\,\widetilde{T}^{\prime}(t)+f(M)\,u\_{1}(x\_{M}(t))+\ u\_{2}(\mathtt{w}-M-x\_{M}(1-t))\right]\,dt. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01u1​(xM​(t))​[(1−f​(M))​T~′​(t)+f​(M)]​𝑑t+∫01u2​(𝚠−M−xM​(1−t))​𝑑t\displaystyle=\int\_{0}^{1}u\_{1}(x\_{M}(t))\,\left[(1-f(M))\,\widetilde{T}^{\prime}(t)+f(M)\right]\,dt+\int\_{0}^{1}u\_{2}(\mathtt{w}-M-x\_{M}(1-t))\,dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01u1​(xM​(t))​T~M′​(t)​𝑑t+∫01u2​(𝚠−M−xM​(1−t))​𝑑t,\displaystyle=\int\_{0}^{1}u\_{1}\left(x\_{M}(t)\right)\,\widetilde{T}^{\prime}\_{M}(t)\,dt+\int\_{0}^{1}u\_{2}(\mathtt{w}-M-x\_{M}(1-t))\,dt, |  |

where we used
FXM−1​(t)=xM​(t)F^{-1}\_{X\_{M}}(t)=x\_{M}(t), F𝚠−M−XM−1​(t)=𝚠−M−FXM−1​(1−t)F^{-1}\_{\mathtt{w}-M-X\_{M}}(t)=\mathtt{w}-M-F^{-1}\_{X\_{M}}(1-t),
and T′​(1−t)=T~′​(t)T^{\prime}(1-t)=\widetilde{T}^{\prime}(t). Hence, letting xM′​(t):=∂∂M​xM​(t)x^{\prime}\_{M}(t):=\frac{\partial}{\partial M}\,x\_{M}(t), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂∂M​W​(XM,M)\displaystyle\frac{\partial}{\partial M}\,W(X^{M},M) | =∫01∂∂M​[u1​(xM​(t))​T~M′​(t)]​𝑑t+∫01∂∂M​u2​(𝚠−M−xM​(1−t))​𝑑t\displaystyle=\int\_{0}^{1}{\frac{\partial}{\partial M}\,\left[u\_{1}(x\_{M}(t))\,\widetilde{T}^{\prime}\_{M}(t)\right]}\,dt+\int\_{0}^{1}\frac{\partial}{\partial M}u\_{2}(\mathtt{w}-M-x\_{M}(1-t))dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01{u1′​(xM​(t))​xM′​(t)​T~M′​(t)+u1​(xM​(t))​f′​(M)​[1−T~′​(t)]}​𝑑t\displaystyle=\int\_{0}^{1}\left\{u\_{1}^{\prime}(x\_{M}(t))x\_{M}^{\prime}(t)\widetilde{T}\_{M}^{\prime}(t)+u\_{1}(x\_{M}(t))f^{\prime}(M)\left[1-\widetilde{T}^{\prime}(t)\right]\right\}dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫01u2′​(𝚠−M−xM​(1−t))​[1+xM′​(1−t)]​𝑑t.\displaystyle\qquad\qquad\qquad-\int\_{0}^{1}u\_{2}^{\prime}(\mathtt{w}-M-x\_{M}(1-t))\,\left[1+x^{\prime}\_{M}(1-t)\right]\,dt. |  |

Thus, the FOC is given by:

|  |  |  |
| --- | --- | --- |
|  | ∫01∂∂M​[u1​(xM​(t))​T~M′​(t)]​𝑑t=−∫01∂∂M​u2​(𝚠−M−xM​(1−t))​𝑑t.\int\_{0}^{1}\frac{\partial}{\partial M}\,\left[u\_{1}(x\_{M}(t))\,\widetilde{T}^{\prime}\_{M}(t)\right]\,dt=-\int\_{0}^{1}\frac{\partial}{\partial M}\,u\_{2}(\mathtt{w}-M-x\_{M}(1-t))\,dt. |  |

Of course, a sufficient condition for the FOC to hold is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂∂M​[u1​(xM​(t))​T~M′​(t)]=−∂∂M​u2​(𝚠−M−xM​(1−t)),∀t∈(0,1).\displaystyle\frac{\partial}{\partial M}\,\left[u\_{1}(x\_{M}(t))\,\widetilde{T}^{\prime}\_{M}(t)\right]=-\frac{\partial}{\partial M}\,u\_{2}(\mathtt{w}-M-x\_{M}(1-t)),\ \ \,\forall\,t\in(0,1). |  | (C.2) |

Note that ([C.2](#A3.E2 "In Appendix C Proofs for Section 5 ‣ Betting under Common Beliefs: The Effect of Probability Weighting")) can be written as

|  |  |  |
| --- | --- | --- |
|  | u1′​(xM​(t))​xM′​(t)​T~M′​(t)+u1​(xM​(t))​f′​(M)​[1−T~′​(t)]=u2′​(𝚠−M−xM​(1−t))​[1+xM′​(1−t)].∎u\_{1}^{\prime}(x\_{M}(t))x\_{M}^{\prime}(t)\widetilde{T}\_{M}^{\prime}(t)+u\_{1}(x\_{M}(t))f^{\prime}(M)\left[1-\widetilde{T}^{\prime}(t)\right]=u\_{2}^{\prime}(\mathtt{w}-M-x\_{M}(1-t))\left[1+x\_{M}^{\prime}(1-t)\right].\qed |  |

## References

* P. Beißner, T.J. Boonen, and M. Ghossoub (2024)
  (No-)Betting Pareto-Optima under Rank-Dependent Utility.
  Mathematics of Operations Research 49 (3),  pp. 1452–1471.
  Cited by: [Lemma A.1](#A1.Thmtheorem1 "Lemma A.1 (Lemma A.5 in Beißner et al. (2024)). ‣ Appendix A Proofs for Section 3 ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [Appendix A](#A1.p18.4 "Appendix A Proofs for Section 3 ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [Appendix A](#A1.p18.5 "Appendix A Proofs for Section 3 ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [Appendix A](#A1.p24.3 "Appendix A Proofs for Section 3 ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§1](#S1.p3.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§1](#S1.p4.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§3.3](#S3.SS3.p2.6 "3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§4.6](#S4.SS6.p4.5 "4.6. Side Payments ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* B. D. Bernheim and D. Taubinsky (2018)
  Behavioral public economics.
  Handbook of behavioral economics: Applications and Foundations 1 1,  pp. 381–516.
  Cited by: [§1](#S1.p8.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [footnote 1](#footnote1 "In 1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* A. Billot, A. Chateauneuf, I. Gilboa, and J.M. Tallon (2000)
  Sharing Beliefs: Between Agreeing and Disagreeing.
  Econometrica 68 (3),  pp. 685–694.
  Cited by: [§1](#S1.p1.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§1](#S1.p2.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§1](#S1.p3.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§1](#S1.p5.3 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* A. Billot, A. Chateauneuf, I. Gilboa, and J.M. Tallon (2002)
  Sharing Beliefs and the Absence of Betting in the Choquet Expected Utility Model.
  Statistical Papers 43 (1),  pp. 127–136.
  Cited by: [§1](#S1.p1.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§1](#S1.p2.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§1](#S1.p3.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§1](#S1.p5.3 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* H. Bleichrodt, S. Grant, and J. Yang (2023)
  Testing hurwicz expected utility.
  Econometrica 91 (4),  pp. 1393–1416.
  Cited by: [§1](#S1.p6.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§1](#S1.p7.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§4.2](#S4.SS2.p4.2 "4.2. The Case of a Prelec Probability Weighting Function ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§4.5](#S4.SS5.p2.6 "4.5. Alternative Weighting Function ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* K. Borch (1962)
  Equilibrium in a Reinsurance Market.
  Econometrica 30 (3),  pp. 424–44.
  Cited by: [§3.1](#S3.SS1.p5.1 "3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* G. Carlier and R.A. Dana (2006)
  Law Invariant Concave Utility Functions and Optimization Problems with Monotonicity and Comonotonicity Constraints.
  Statistics & Decisions 24 (1),  pp. 127–152.
  Cited by: [Appendix A](#A1.p2.4 "Appendix A Proofs for Section 3 ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* R. Chetty (2015)
  Behavioral economics and public policy: a pragmatic perspective.
  American Economic Review 105 (5),  pp. 1–33.
  Cited by: [§1](#S1.p9.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* S.H. Chew, E. Karni, and Z. Safra (1987)
  Risk Aversion in the Theory of Expected Utility with Rank Dependent Probabilities.
  Journal of Economic Theory 42 (2),  pp. 370–381.
  Cited by: [Appendix A](#A1.p2.4 "Appendix A Proofs for Section 3 ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§2.1](#S2.SS1.p5.4 "2.1. Preferences ‣ 2. The Economy ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* R.A. Dana (1993)
  Existence and Uniqueness of Equilibria When Preferences are Additively Separable.
  Econometrica 61 (4),  pp. 953–957.
  Cited by: [§3.1](#S3.SS1.p2.1 "3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* R.A. Dana (2011)
  Comonotonicity, Efficient Risk-Sharing and Equilibria in Markets with Short-Selling for Concave Law-Invariant Utilities.
  Journal of Mathematical Economics 47 (3),  pp. 328–335.
  Cited by: [§3.1](#S3.SS1.p2.1 "3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* B. De Finetti (1937)
  La Prévision: Ses Lois Logiques, Ses Sources Subjectives.
  Annales de l’Institut Henri Poincaré 7 (1),  pp. 1–68.
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* H. Föllmer and A. Schied (2025)
  Stochastic Finance: An Introduction in Discrete Time – 5t​h5^{th} ed..
   Walter de Gruyter.
  Cited by: [Appendix A](#A1.p4.11 "Appendix A Proofs for Section 3 ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [Appendix A](#A1.p4.12 "Appendix A Proofs for Section 3 ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§3.2](#S3.SS2.p1.2 "3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§3.2](#S3.SS2.p5.1 "3.2. Quantile Formulation of Welfare Functions ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* M. Ghossoub (2019)
  Optimal Insurance under Rank-Dependent Expected Utility.
  Insurance Mathematics and Economics 87,  pp. 51–66.
  Cited by: [Appendix B](#A2.p1.1 "Appendix B Proofs for Section 4 ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* I. Gilboa and D. Schmeidler (1989)
  Maxmin Expected Utility with a Non-Unique Prior.
  Journal of Mathematical Economics 18 (2),  pp. 141–153.
  Cited by: [§1](#S1.p3.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* J. S. Hastings, B. C. Madrian, and W. L. Skimmyhorn (2013)
  Financial literacy, financial education, and economic outcomes.
  Annual Review of Economics 5 (1),  pp. 347–373.
  Cited by: [footnote 1](#footnote1 "In 1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* X. He, R. Kouwenberg, and X.Y. Zhou (2017)
  Rank-Dependent Utility and Risk Taking in Complete Markets.
  SIAM Journal on Financial Mathematics 8 (1),  pp. 214–239.
  Cited by: [§3.3](#S3.SS3.p2.6 "3.3. Characterization of Efficient Allocations ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* R.J. Herrnstein, G.F. Loewenstein, D. Prelec, and Jr. Vaughan (1993)
  Utility Maximization and Melioration: Internalities in Individual Choice.
  Journal of Behavioral Decision Making 6,  pp. 149–185.
  Cited by: [§1](#S1.p9.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* D. Kahneman, P. P. Wakker, and R. Sarin (1997)
  Back to bentham? explorations of experienced utility.
  The Quarterly Journal of Economics 112 (2),  pp. 375–406.
  Cited by: [§1](#S1.p9.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* N. Kaldor (1939)
  Welfare propositions of economics and interpersonal comparisons of utility.
  The Economic Journal 49 (195),  pp. 549–552.
  Cited by: [§1](#S1.p6.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§4.6](#S4.SS6.p1.1 "4.6. Side Payments ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* D. Prelec (1998)
  The Probability Weighting Function.
  Econometrica 66 (3),  pp. 497–527.
  Cited by: [§1](#S1.p6.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§4.2](#S4.SS2.p1.12 "4.2. The Case of a Prelec Probability Weighting Function ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* J. Quiggin (1982)
  A Theory of Anticipated Utility.
  Journal of Economic Behavior & Organization 3 (4),  pp. 323–343.
  Cited by: [§1](#S1.p3.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§2.1](#S2.SS1.p1.4 "2.1. Preferences ‣ 2. The Economy ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* J. Quiggin (1991)
  Comparative Statics for Rank-Dependent Expected Utility Theory.
  Journal of Risk and Uncertainty 4 (4),  pp. 339–350.
  Cited by: [§1](#S1.p3.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§2.1](#S2.SS1.p1.4 "2.1. Preferences ‣ 2. The Economy ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* D. Reck and A. Seibold (2023)
  The welfare economics of reference dependence.
  Technical report
   National Bureau of Economic Research.
  Cited by: [footnote 1](#footnote1 "In 1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* M.O. Rieger and M. Wang (2006)
  Cumulative Prospect Theory and the St. Petersburg Paradox.
  Economic Theory 28 (3),  pp. 665–679.
  Cited by: [§4.2](#S4.SS2.p4.2 "4.2. The Case of a Prelec Probability Weighting Function ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* L. Rigotti, C. Shannon, and T. Strzalecki (2008)
  Subjective Beliefs and ex ante Trade.
  Econometrica 76 (5),  pp. 1167–1190.
  Cited by: [§1](#S1.p1.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* L.J. Savage (1972)
  The Foundations of Statistics (2nd revised edition) – 1s​t1^{st} ed. 1954.
   New York: Dover Publications.
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* D. Schmeidler (1989)
  Subjective Probability and Expected Utility without Additivity.
  Econometrica 57 (3),  pp. 571–587.
  Cited by: [§1](#S1.p3.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* R. H. Thaler and S. Benartzi (2004)
  Save for tomorrow: using behavioral economics to increase employee saving.
  Journal of Political Economy 112 (S1),  pp. S164–S187.
  Cited by: [footnote 1](#footnote1 "In 1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* R. H. Thaler and C. R. Sunstein (2009)
  Nudge: improving decisions about health, wealth, and happiness.
   Penguin.
  Cited by: [§1](#S1.p8.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* A. Tversky and D. Kahneman (1992)
  Advances in prospect theory: cumulative representation of uncertainty.
  Journal of Risk and Uncertainty 5,  pp. 297–323.
  Cited by: [§1](#S1.p6.1 "1. Introduction ‣ Betting under Common Beliefs: The Effect of Probability Weighting"),
  [§4.2](#S4.SS2.p4.2 "4.2. The Case of a Prelec Probability Weighting Function ‣ 4. Comparative Statics of Endogenous Uncertainty ‣ Betting under Common Beliefs: The Effect of Probability Weighting").
* R. Wilson (1968)
  The Theory of Syndicates.
  Econometrica 36 (1),  pp. 119–132.
  Cited by: [§3.1](#S3.SS1.p5.1 "3.1. The Utilitarian Welfare Function ‣ 3. Betting and Efficiency ‣ Betting under Common Beliefs: The Effect of Probability Weighting").

BETA