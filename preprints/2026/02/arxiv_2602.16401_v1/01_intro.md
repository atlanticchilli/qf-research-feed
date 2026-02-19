---
authors:
- Maria Andraos
- Mario Ghossoub
- Bin Li
- Benxuan Shi
doc_id: arxiv:2602.16401v1
family_id: arxiv:2602.16401
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting
url_abs: http://arxiv.org/abs/2602.16401v1
url_html: https://arxiv.org/html/2602.16401v1
venue: arXiv q-fin
version: 1
year: 2026
---


Maria Andraos
  
University of Waterloo
  
Mario Ghossoub
  
University of Waterloo
  
Bin Li
  
University of Waterloo
  
Benxuan Shi
  
University of Waterloo
  
Maria Andraos: University of Waterloo – Department of Statistics and Actuarial Science – 200 University Ave. W. – Waterloo, ON, N2L 3G1 – Canada
[[mandraos@uwaterloo.ca](mailto:mandraos@uwaterloo.ca)](mailto:)
Mario Ghossoub: University of Waterloo – Department of Statistics and Actuarial Science – 200 University Ave. W. – Waterloo, ON, N2L 3G1 – Canada
[[mario.ghossoub@uwaterloo.ca](mailto:mario.ghossoub@uwaterloo.ca)](mailto:)
Bin Li: University of Waterloo – Department of Statistics and Actuarial Science – 200 University Ave. W. – Waterloo, ON, N2L 3G1 – Canada
[[bin.li@uwaterloo.ca](mailto:bin.li@uwaterloo.ca)](mailto:)
Benxuan Shi: University of Waterloo – Department of Statistics and Actuarial Science – 200 University Ave. W. – Waterloo, ON, N2L 3G1 – Canada
[[benxuan.shi1@uwaterloo.ca](mailto:benxuan.shi1@uwaterloo.ca)](mailto:)

###### Abstract.

We study Stackelberg Equilibria (Bowley optima) in a monopolistic centralized sequential-move insurance market, with a profit-maximizing insurer who sets premia using a distortion premium principle, and a single policyholder who seeks to minimize a distortion risk measure. We show that equilibria are characterized as follows: In equilibrium, the optimal indemnity function exhibits a layer-type structure, providing full insurance over any loss layer on which the policyholder is more pessimistic than the insurer’s pricing functional about tail losses; and no insurance coverage over loss layers on which the policyholder is less pessimistic than the insurer’s pricing functional about tail losses. In equilibrium, the optimal pricing distortion function is determined by the policyholder’s degree of risk aversion, whereby prices never exceed the policyholder’s marginal willingness to insure tail losses. Moreover, we show that both the insurance coverage and the insurer’s expected profit increase with the policyholder’s degree of risk aversion. Additionally, and echoing recent work in the literature, we show that equilibrium contracts are Pareto efficient, but they do not induce a welfare gain to the policyholder. Conversely, any Pareto-optimal contract that leaves no welfare gain to the policyholder can be obtained as an equilibrium contract. Finally, we consider a few examples of interest that recover some existing results in the literature as special cases of our analysis.

JEL Classification: C61; C62; C72; C79; D86; G22.

Key Words and Phrases: Distortion risk measure; Distortion premium principle; Probability weighting; Stackelberg equilibria; Bowley optima; Pareto optima.

Mario Ghossoub acknowledges financial support from the Natural Sciences and Engineering Research Council of Canada (NSERC Grant No. 2024-03744). Bin Li acknowledges financial support from (NSERC Grant No. 2020-04338). Benxuan Shi acknowledges financial support from the Society of Actuaries through the Hickman Scholars Program.

## 1. Introduction

In monopoly insurance markets under perfect information, the classical literature has been mostly interested in characterizing the insurer’s profit-maximizing (or welfare-maximizing) insurance contracts, without any consideration for strategic interaction between the insurer and insured. Whenever such strategic considerations are introduced into the market model, the natural framework is a sequential-move game with the insurer as the leader and the insured as the follower, borrowing from the literature on bilateral monopoly. This is a two-stage game, whereby in the first stage, the insured selects their optimal indemnification given a certain pricing mechanism selected by the insurer; and in the second stage, the insurer observes the insured’s demand function and sets prices so as to maximize profit or welfare. The associated strategic equilibrium concept has been termed the Stackelberg equilibrium, or Bowley optimum.

Bowley optima were first introduced by Bowley ([1928](https://arxiv.org/html/2602.16401v1#bib.bib8 "Bilateral Monopoly")) in the context of a bilateral monopoly, and then first applied to insurance markets by Chan and Gerber ([1985](https://arxiv.org/html/2602.16401v1#bib.bib32 "The Reinsurer’s Monopoly and the Bowley Solution")), in the context of Expected-Utility (EU) preferences with exponential utility functions. Several extensions and/or modifications to this model have subsequently been proposed. For instance, G.Taylor ([1992](https://arxiv.org/html/2602.16401v1#bib.bib44 "Risk Exchange I: a Unification of Some Existing Results")) extends these findings to more general risk exchanges with EU preferences. Cheung et al. ([2019](https://arxiv.org/html/2602.16401v1#bib.bib33 "Risk-Adjusted Bowley Reinsurance under Distorted Probabilities")) consider the case of markets in which the insurer is a risk-neutral Expected utility maximizer, who sets premia using a distortion premium principle, and a insured who seeks to minimize a distortion risk measure (DRM). They assume that the insured’s distortion function is either a concave function (indicating risk aversion), or a distortion function corresponding to the Value-at-Risk (VaR) risk measure. Li and Young ([2021](https://arxiv.org/html/2602.16401v1#bib.bib45 "Bowley Solution of a Mean–Mariance Game in Insurance")) characterize Stackelberg equilibria when agents use a mean-variance functional. Boonen et al. ([2021](https://arxiv.org/html/2602.16401v1#bib.bib39 "Bowley Reinsurance with Asymmetric Information on the Insurer’s Risk Preferences")) and Boonen and Zhang ([2022](https://arxiv.org/html/2602.16401v1#bib.bib40 "Bowley Reinsurance with Asymmetric Information: A First-Best Solution")) examine the effect of information asymmetry in the context of DRMs. Ghossoub et al. ([2025](https://arxiv.org/html/2602.16401v1#bib.bib12 "Bowley-Optimal Convex-Loaded Premium Principles")) propose an extension in a different direction, by examining the optimal (nonlinear) pricing mechanisms in the market for the class of deductible and coinsurance indemnity functions. Boonen and Ghossoub ([2023](https://arxiv.org/html/2602.16401v1#bib.bib48 "Bowley vs. Pareto Optima in Reinsurance Contracting")) examine the relationship between Bowley optimality and Pareto optimality, under fairly general preferences. Zhu et al. ([2023](https://arxiv.org/html/2602.16401v1#bib.bib43 "Equilibria and Efficiency in a Reinsurance Market")) and Ghossoub and Zhu ([2024](https://arxiv.org/html/2602.16401v1#bib.bib42 "Stackelberg Equilibria with Multiple Policyholders")) provide the first extensions beyond the case of a two-agent insurance market. The former consider a market with multiple insurer having the first move advantage, and one insured; whereas the latter consider the case of one monopoly insurance facing demand from several policyholders. Andraos et al. ([2026](https://arxiv.org/html/2602.16401v1#bib.bib10 "Subgame perfect nash equilibria in large reinsurance markets")) recently provided a unification and an extension thereof to more general preferences.

In this paper, we consider a monopoly insurance market with a single policyholder. We assume that the policyholder evaluates insurance contracts using a distortion risk measure, following the approach of Assa ([2015](https://arxiv.org/html/2602.16401v1#bib.bib17 "On Optimal Reinsurance Policy with Distortion Risk Measures and Premiums")), Cheung et al. ([2019](https://arxiv.org/html/2602.16401v1#bib.bib33 "Risk-Adjusted Bowley Reinsurance under Distorted Probabilities")), or Zhu et al. ([2023](https://arxiv.org/html/2602.16401v1#bib.bib43 "Equilibria and Efficiency in a Reinsurance Market")), for instance. The insurer is a risk-neutral profit maximizer, who sets premia using a distortion premium principle. To avoid ex post moral hazard that might arise from the policyholder’s misreporting of the true value of the loss, we impose the customary no sabotage condition of Carlier and Dana ([2003](https://arxiv.org/html/2602.16401v1#bib.bib4 "Pareto Efficient Insurance Contracts when the Insurer’s Cost Function is Discontinuous"), [2005](https://arxiv.org/html/2602.16401v1#bib.bib5 "Rearrangement Inequalities in Non-convex Insurance Models")) on the set of acceptable indemnity functions. Our framework is most closely related to that of Cheung et al. ([2019](https://arxiv.org/html/2602.16401v1#bib.bib33 "Risk-Adjusted Bowley Reinsurance under Distorted Probabilities")). However, in contrast to their study, which assumes that the policyholder is either strictly risk averse (strictly concave distortion function) or a VaR minimizer, we impose no specific restriction on the curvature of the policyholder’s distortion function. This is a significant extension, as it accommodates for several forms of distortion functions that are empirically more relevant than the concave distortion functions, such as the inverse-S-shaped distortion functions of Tversky and Kahneman ([1992](https://arxiv.org/html/2602.16401v1#bib.bib50 "Advances in Prospect Theory: Cumulative Representation of Uncertainty")), the S-shaped distortion functions of Prelec ([1998](https://arxiv.org/html/2602.16401v1#bib.bib7 "The Probability Weighting Function")), or the very flexible class of distortion functions recently introduced by Bleichrodt et al. ([2023](https://arxiv.org/html/2602.16401v1#bib.bib6 "Testing hurwicz expected utility")).

To characterize Stackelberg equilibria in our model, we proceed in two steps. First for a fixed distortion function used to determine the distortion premium principle, we determine the optimal indemnity function that minimizes the policyholder’s risk measure of their end-of-period risk exposure (Theorem [3.6](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem6 "Theorem 3.6. ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). Second, using the resulting optimal indemnity, we find the pricing distortion function that maximizes the insurer’s expected profit (Corollary [3.10](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem10 "Corollary 3.10. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). We show that, in the first step, the optimal indemnity function exhibits a layer-type structure, determined by the interplay between the policyholder’s distortion function and the insurer’s pricing distortion function. Specifically, the optimal indemnity provides full indemnification over any loss layer on which the policyholder is more pessimistic than the insurer’s pricing functional about tail losses. When the policyholder is less pessimistic than the insurer’s pricing functional about tail losses, no indemnification is offered. Finally, when the policyholder and the insurer’s pricing functional are equally pessimistic about tail losses, the marginal indemnity may take an arbitrary shape, within the global 11-Lispchitz (i.e., comonotonicity) constraints. In the second step, the optimal pricing distortion is determined by the policyholder’s degree of (weak) risk aversion, that is, whether the policyholder’s distortion function is above or below the identity function. In equilibrium, the insurer selects a pricing distortion that is aligned with the policyholder’s risk perception, as encoded by their distortion function, in the sense that prices never exceed the policyholder’s marginal willingness to insure tail losses. Moreover, we show that both the insurance coverage and the insurer’s expected profit increase with the policyholder’s degree of strong or weak risk aversion.

We also analyze the Pareto efficiency of the Stackelberg equilibrium contracts. Our results show that any Stackelberg equilibrium contract is Pareto optimal and makes the policyholder indifferent between participating and not participating in the insurance market. Moreover, any Pareto-optimal contract in which the policyholder is indifferent between participation and non-participation can be obtained at a Stackelberg equilibrium. These findings echo similar results obtained by Boonen and Ghossoub ([2023](https://arxiv.org/html/2602.16401v1#bib.bib48 "Bowley vs. Pareto Optima in Reinsurance Contracting")) and Ghossoub and Zhu ([2024](https://arxiv.org/html/2602.16401v1#bib.bib42 "Stackelberg Equilibria with Multiple Policyholders")), and they highlight a well-known fundamental phenomenon that occurs in monopoly markets, whereby all consumer surplus is extracted by the monopoly.

When the policyholder is either weakly risk averse (with a distortion function that lies above the identity function) or strongly risk averse (with a concave distortion function), we show that the optimal contract provides full insurance, and the optimal pricing distortion function coincides with that of the policyholder. This recovers the result of Cheung et al. ([2019](https://arxiv.org/html/2602.16401v1#bib.bib33 "Risk-Adjusted Bowley Reinsurance under Distorted Probabilities")) in the case of concave distortion function. For policyholders who minimize VaR at a confidence level α∈(0,1)\alpha\in(0,1), the optimal coverage includes an upper limit. Specifically, the contract provides full insurance for losses below the α\alpha-quantile while leaving the upper tail uninsured. This recovers another result of Cheung et al. ([2019](https://arxiv.org/html/2602.16401v1#bib.bib33 "Risk-Adjusted Bowley Reinsurance under Distorted Probabilities")). However, in contrast, we show that for individuals with inverse-S shaped distortion functions, reflecting strong sensitivity to extreme losses, the optimal indemnity function takes the form of a deductible contract, whereby extreme losses are fully transferred to the insurer.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2602.16401v1#S2 "2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") introduces the insurance market setting, including the risk preferences of the agents, the market mechanisms and resulting insurance contracts, and the (Stackelberg, or Bowley) equilibrium concept. Section [3](https://arxiv.org/html/2602.16401v1#S3 "3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") provides a characterization of Stackelberg equilibria in our setting. Section [4](https://arxiv.org/html/2602.16401v1#S4 "4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") examines the Pareto efficiency of the equilibrium contracts, and provides a version of the two welfare theorems. Section [5](https://arxiv.org/html/2602.16401v1#S5 "5. Examples ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") presents several examples of interest, for specific types of policyholders. Finally, Section [6](https://arxiv.org/html/2602.16401v1#S6 "6. Conclusion ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") concludes. Proofs and related analysis are given in the [Appendices](https://arxiv.org/html/2602.16401v1#LinkToAppendix "6. Conclusion ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").

## 2. Problem Formulation

Let B​(ℱ)B(\mathcal{F}) denote the set of all bounded random variables on a given non-atomic probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}). An individual, or potential policyholder, is subject to an insurable loss, which we model as a random variable X∈B+​(ℱ)X\in B^{+}(\mathcal{F}), the positive cone of B​(ℱ)B(\mathcal{F}), with range [0,M][0,M]. A positive realization of XX is seen as a loss. We denote by FXF\_{X} the cumulative distribution function of XX, and by FX−1F\_{X}^{-1} the left-continuous inverse of FXF\_{X}, i.e., the quantile of XX, defined as:

|  |  |  |
| --- | --- | --- |
|  | FX−1​(t)=inf{z∈ℝ+|FX​(z)≥t},∀t∈[0,1].F\_{X}^{-1}(t)=\inf\left\{z\in\mathbb{R}^{+}\,\middle|\,F\_{X}(z)\geq t\right\},\ \forall t\in[0,1]. |  |

Let 𝒬\mathcal{Q} denote the set of quantile functions of random variables in B​(ℱ)B(\mathcal{F}). That is,

|  |  |  |
| --- | --- | --- |
|  | 𝒬={q:(0,1)→ℝ+|q is non-decreasing and left-continuous}.\mathcal{Q}=\left\{q:(0,1)\to\mathbb{R}^{+}\,\middle|\,q\mbox{ is non-decreasing and left-continuous}\right\}. |  |

### 2.1. Preferences

###### Definition 2.1.

A distortion risk measure ρ\rho on (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}), is defined as the Choquet integral with respect to the distorted probability measure T∘ℙT\circ\mathbb{P}. Namely, for any Y∈B​(ℱ)Y\in B(\mathcal{F}),

|  |  |  |
| --- | --- | --- |
|  | ρ​(Y)=∫Y​dT∘ℙ=∫0+∞T​(ℙ​(Y≥y))​dy+∫−∞0[T​(ℙ​(Y≥y))−1]​dy,\displaystyle\rho(Y)=\int\,Y\,\mathrm{d}T\circ\mathbb{P}=\int\_{0}^{+\infty}T(\mathbb{P}(Y\geq y))\,\mathrm{d}y+\int\_{-\infty}^{0}\left[T(\mathbb{P}(Y\geq y))-1\right]\mathrm{d}y, |  |

where T:[0,1]→[0,1]T:[0,1]\rightarrow[0,1] is a distortion function, that is, a non-decreasing differentiable mapping, satisfying T​(0)=0T(0)=0 and T​(1)=1T(1)=1.

The conjugate of the distortion function TT, is given by: T~​(t)=1−T​(1−t)\widetilde{T}(t)=1-T(1-t), for all t∈[0,1]t\in[0,1]. It is easy to verify that T~\widetilde{T} is a distortion function.

The policyholder’s preference over B​(ℱ)B(\mathcal{F}) is assumed to admit a distortion
risk measure representation, associated with a distortion function TT. Specifically, for any
Z∈B​(ℱ)Z\in B(\mathcal{F}), the policyholder evaluates risk according to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρP​o​l​(Z):=∫Z​𝑑T∘ℙ.\rho^{Pol}(Z):=\int Z\,d\,T\circ\mathbb{P}. |  | (1) |

The induced preference relation ≽\succcurlyeq on B​(ℱ)B(\mathcal{F}) is defined by
Z1≽Z2Z\_{1}\succcurlyeq Z\_{2}, if and only if, ρPol​(Z1)≤ρPol​(Z2)\rho^{\mathrm{Pol}}(Z\_{1})\leq\rho^{\mathrm{Pol}}(Z\_{2}).
Indifference is defined by Z1∼Z2Z\_{1}\sim Z\_{2}, whenever
Z1≽Z2Z\_{1}\succcurlyeq Z\_{2}, and Z2≽Z1Z\_{2}\succcurlyeq Z\_{1}.

### 2.2. Risk Aversion

Given two random variables Z1,Z2∈B​(ℱ)Z\_{1},Z\_{2}\in B(\mathcal{F}), we say that Z1Z\_{1} dominates Z2Z\_{2} in Second-Order Stochastic Dominance (SSD), written Z1≽S​S​DZ2Z\_{1}\succcurlyeq\_{\hskip-1.13809pt{}\_{SSD}}Z\_{2}, if

|  |  |  |
| --- | --- | --- |
|  | ∫−∞xFZ1​(t)​𝑑t≤∫−∞xFZ2​(t)​𝑑t,for all x∈ℝ.\displaystyle\int\_{-\infty}^{x}F\_{Z\_{1}}(t)\ dt\leq\int\_{-\infty}^{x}F\_{Z\_{2}}(t)\ dt,\ \text{for all $x\in\mathbb{R}$}. |  |

Moreover, Z2Z\_{2} is said to be a Mean-Preserving Increase in Risk (MPIR) of Z1Z\_{1} if 𝔼​[Z1]=𝔼​[Z2]\mathbb{E}[Z\_{1}]=\mathbb{E}[Z\_{2}] and Z1≽S​S​DZ2Z\_{1}\succcurlyeq\_{\hskip-1.13809pt{}\_{SSD}}Z\_{2}. We next discuss weak and strong risk aversion of a preference ≽\succcurlyeq over B​(ℱ)B(\mathcal{F}).

###### Definition 2.2.

A preference ≽\succcurlyeq over B​(ℱ)B(\mathcal{F}) is said to be weakly risk averse, if 𝔼​[Z]≽Z\mathbb{E}[Z]\succcurlyeq Z for all Z∈B​(ℱ)Z\in B(\mathcal{F}).

###### Definition 2.3.

A preference ≽\succcurlyeq over B​(ℱ)B(\mathcal{F}) is said to be strongly risk averse if it ranks any random variable above all of its mean-preserving increases in risk. That is, ≽\succcurlyeq is strongly risk averse if Z1≽Z2Z\_{1}\succcurlyeq Z\_{2}, for all Z1,Z2∈B​(ℱ)Z\_{1},Z\_{2}\in B(\mathcal{F}), such that Z2Z\_{2} is a MPIR of Z1Z\_{1}.

Strong risk aversion implies weak risk aversion, since any Z∈B​(ℱ)Z\in B(\mathcal{F})
is a mean-preserving increase in risk of 𝔼​[Z]\mathbb{E}[Z].
Moreover, by the positive homogeneity of the Choquet integral, it follows that,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Z]≽Z⟺𝔼​[Z]≤ρP​o​l​(Z),∀Z∈B​(ℱ).\mathbb{E}[Z]\succcurlyeq Z\Longleftrightarrow\mathbb{E}[Z]\leq\rho^{Pol}(Z),\ \forall Z\in B(\mathcal{F}). |  |

By a classical result (see, e.g., Yaari ([1987](https://arxiv.org/html/2602.16401v1#bib.bib1 "The Dual Theory of Choice under Risk"))), risk aversion under distortion risk measures is characterized by properties of the distortion function T. In particular, the policyholder is weakly risk averse if and only if T​(t)≥tT(t)\geq t for all t∈[0,1]t\in[0,1]. Moreover, the policyholder is strongly risk averse if and only if the distortion function TT is concave.

Recall that for a given preference relation ≽\succcurlyeq, the certainty equivalent of Z∈B​(ℱ)Z\in B(\mathcal{F}) is the constant CE≽​(Z)∈ℝ\text{CE}^{\succcurlyeq}(Z)\in\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | Z∼CE≽​(Z),Z\sim\text{CE}^{\succcurlyeq}(Z), |  |

and the risk premium associated with Z∈B​(ℱ)Z\in B(\mathcal{F}) is defined as

|  |  |  |
| --- | --- | --- |
|  | Δ≽​(Z):=𝔼​[Z]−CE≽​(Z).\Delta^{\succcurlyeq}(Z):=\mathbb{E}[Z]-\text{CE}^{\succcurlyeq}(Z). |  |

Following Chew et al. ([1987](https://arxiv.org/html/2602.16401v1#bib.bib3 "Risk Aversion in the Theory of Expected Utility with Rank Dependent Pobabilities")), Quiggin ([1993](https://arxiv.org/html/2602.16401v1#bib.bib2 "Generalized Expected Utility Theory - The Rank-Dependent Model")), and Ghossoub and He ([2021](https://arxiv.org/html/2602.16401v1#bib.bib11 "Comparative Risk Aversion in RDEU with Applications to Optimal Underwriting of Securities Issuance")), we define comparative notions of risk aversion below.

###### Definition 2.4 (Comparative risk aversion).

Consider two preference relations ≽\succcurlyeq and ≽∗\succcurlyeq^{\*} over B​(ℱ)B(\mathcal{F}):

1. (1)

   ≽∗\succcurlyeq^{\*} is said to be more weakly risk averse than ≽\succcurlyeq if, for any Z∈B​(ℱ)Z\in B(\mathcal{F}), Δ≽∗​(Z)≥Δ≽​(Z)\Delta^{\succcurlyeq^{\*}}(Z)\geq\Delta^{\succcurlyeq}(Z).
2. (2)

   ≽∗\succcurlyeq^{\*} is said to be more strongly risk averse than ≽\succcurlyeq if Z1≽∗Z2Z\_{1}\succcurlyeq^{\*}Z\_{2} for any Z1,Z2∈B​(ℱ)Z\_{1},Z\_{2}\in B(\mathcal{F}) such that:

   1. (a)

      Z1∼Z2Z\_{1}\sim Z\_{2}.
   2. (b)

      There exists z0∈ℝz\_{0}\in\mathbb{R} with FZ2​(z)≥FZ1​(z)F\_{Z\_{2}}(z)\geq F\_{Z\_{1}}(z) for all z<z0z<z\_{0}, and FZ2​(z)≤FZ1​(z)F\_{Z\_{2}}(z)\leq F\_{Z\_{1}}(z) for all z≥z0z\geq z\_{0}.

By a classical result (e.g., Chew et al. ([1987](https://arxiv.org/html/2602.16401v1#bib.bib3 "Risk Aversion in the Theory of Expected Utility with Rank Dependent Pobabilities"))), we obtain the following characterization of comparative weak and strong risk aversion for distortion risk measures.

###### Proposition 2.5.

Consider two policyholders whose preferences ≽\succcurlyeq and ≽∗\succcurlyeq^{\*} over B​(ℱ)B(\mathcal{F}) admit representations by distortion risk measures ρP​o​l\rho^{Pol} and ρ∗P​o​l{\rho^{\*}}^{Pol} respectively. Let TT and T∗T^{\*} denote the respective distortion functions of each policyholder. Then the following holds:

1. (1)

   The second policyholder is more weakly risk averse than the first policyholder if and only if T∗​(t)≥T​(t)T^{\*}(t)\geq T(t), for all t∈[0,1]t\in[0,1].
2. (2)

   The second policyholder is more strongly risk averse than the first policyholder if and only if T∗T^{\*} is a concave transformation of TT. That is, there exists an increasing and concave function g:[0,1]→[0,1]g:[0,1]\to[0,1], satisfying g​(0)=0g(0)=0, g​(1)=1g(1)=1, and T∗​(t)=g​(T​(t))T^{\*}(t)=g\left(T(t)\right) for all t∈[0,1]t\in[0,1].

###### Remark 2.6.

If gg is an increasing and concave function on [0,1][0,1] such that g​(0)=0g(0)=0 and g​(1)=1g(1)=1, then g​(t)≥tg(t)\geq t, for all t∈[0,1]t\in[0,1]. Consequently, if T∗≡g∘TT^{\*}\equiv g\circ T, we obtain that T∗​(t)≥T​(t)T^{\*}(t)\geq T(t) for all t∈[0,1]t\in[0,1]. That is, if T∗T^{\*} is more strongly risk averse than TT, then T∗T^{\*} is also more weakly risk averse than TT.

### 2.3. Market Mechanisms and Contracts

The market allows the policyholder to cede part of the loss XX to an insurer, in exchange for a premium payment. We assume that the market only offers indemnities in the set of ex ante admissible indemnity schedules ℐL\mathcal{I}\_{L} defined below.

|  |  |  |
| --- | --- | --- |
|  | ℐL={I:[0,M]→[0,M]|I​(0)=0, 0≤I​(x1)−I​(x2)≤x1−x2,∀x2≤x1∈[0,M]}.\mathcal{I}\_{L}=\Big\{I:[0,M]\rightarrow[0,M]\ \Big|\ I(0)=0,\ 0\leq I(x\_{1})-I(x\_{2})\leq x\_{1}-x\_{2},\forall\,x\_{2}\leq x\_{1}\in[0,M]\Big\}. |  |

That is, ℐL\mathcal{I}\_{L} is the set of 11-Lipschitz functions satisfying the so-called no-sabotage condition of Carlier and Dana ([2003](https://arxiv.org/html/2602.16401v1#bib.bib4 "Pareto Efficient Insurance Contracts when the Insurer’s Cost Function is Discontinuous")), so as to rule ex post moral hazard that could arise from misreporting of the actual realized loss.

###### Definition 2.7.

An insurance contract is a pair (I,π)(I,\pi), where I∈ℐLI\in\mathcal{I}\_{L} is an indemnity function and π∈ℝ\pi\in\mathbb{R} is the premium paid by the policyholder for coverage II.

###### Assumption 2.8.

The insurer is assumed to price insurance using a distortion premium principle of the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πg​(I​(X)):=∫I​(X)​𝑑g∘ℙ,∀I∈ℐL,\displaystyle\Pi\_{g}\left(I(X)\right):=\int I(X)\,dg\circ\mathbb{P},\ \forall\,I\in\mathcal{I}\_{L}, |  | (2) |

for some distortion function gg, which we hereafter refer to as the pricing distortion used by the insurer.

###### Definition 2.9.

A market mechanism is a pair (I,g)(I,g), where I∈ℐLI\in\mathcal{I}\_{L} is an indemnity function and gg is a pricing distortion function.

A market mechanism (I,g)(I,g) induces an insurance contract of the form (I,Πg​(I​(X)))\left(I,\Pi\_{g}\big(I(X)\big)\right), where the premium is computed using the pricing distortion gg. The insurer’s end-of-period profit is therefore given by Πg​(I​(X))−I​(X)\Pi\_{g}\big(I(X)\big)-I(X), while the policyholder’s end-of-period risk exposure is given by X−I​(X)+Πg​(I​(X))X-I(X)+\Pi\_{g}\big(I(X)\big). Accordingly, the insurer’s resulting expected profit is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VI​n​(I,g)=Πg​(I​(X))−𝔼​[I​(X)],\displaystyle V^{In}(I,g)=\Pi\_{g}\big(I(X)\big)-\mathbb{E}\left[I(X)\right], |  | (3) |

and the policyholder evaluates this risk exposure using:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρP​o​l​(I,g)=ρP​o​l​(X−I​(X)+Πg​(I​(X))).\displaystyle\rho^{Pol}(I,g)=\rho^{Pol}\Big(X-I(X)+\Pi\_{g}\big(I(X)\big)\Big). |  | (4) |

Letting R​(X):=X−I​(X)R(X):=X-I(X) denote the retention function, i.e., the part of the loss XX that is retained by the policyholder, and by translation invariance of ρP​o​l\rho^{Pol}, ([4](https://arxiv.org/html/2602.16401v1#S2.E4 "Equation 4 ‣ 2.3. Market Mechanisms and Contracts ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) reduces to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρP​o​l​(I,g)=ρP​o​l​(R​(X))+Πg​(I​(X)).\rho^{Pol}(I,g)=\rho^{Pol}\big(R(X)\big)+\Pi\_{g}\big(I(X)\big). |  | (5) |

###### Remark 2.10.

An indemnity function II belongs to ℐL\mathcal{I}\_{L} if and only if the corresponding retention function R​(X)=X−I​(X)R(X)=X-I(X) belongs to ℐL\mathcal{I}\_{L}. Moreover, since II is non-decreasing, the random variables I​(X)I(X) and R​(X)R(X) are comonotonic 111Two random variables X,Y∈B​(ℱ)X,Y\in B(\mathcal{F}) are said to be comonotone if (X​(ω1)−X​(ω2))​(Y​(ω1)−Y​(ω2))≥0(X(\omega\_{1})-X(\omega\_{2}))(Y(\omega\_{1})-Y(\omega\_{2}))\geq 0, for all ω1,ω2∈Ω\omega\_{1},\omega\_{2}\in\Omega..

### 2.4. A Sequential-Move Game

The insurance market is modeled as a sequential move game, in which the insurer, having the first-mover advantage, starts by selecting a pricing distortion function gg. Given that choice, the policyholder then selects an indemnity function that minimizes their risk exposure ρP​o​l​(I,g)\rho^{Pol}(I,g). Anticipating the policyholder’s optimal indemnity choice as a function of the selected pricing distortion function gg, the insurer selects the optimal distortion function g∗g^{\*} that maximizes their expected profit VI​n​(I,g)V^{In}(I,g). The equilibrium concept that is best suited for this sequential game is the Stackelberg equilibrium.

###### Definition 2.11.

A given market mechanism (I∗,g∗)(I^{\*},g^{\*}) is said to be a Stackelberg Equilibrium (SE), if

1. (1)

   I∗∈arg⁡minI∈ℐL​ρP​o​l​(I,g∗)I^{\*}\in\underset{I\in\mathcal{I}\_{L}}{\arg\min}\ \rho^{Pol}(I,{g^{\*}}), and
2. (2)

   VI​n​(I∗,g∗)≥VI​n​(I,g)V^{In}(I^{\*},{g^{\*}})\geq V^{In}(I,g), for all (I,g)(I,g) such that I∈arg⁡minI¯∈ℐL​ρP​o​l​(I¯,g)I\in\underset{\bar{I}\in\mathcal{I}\_{L}}{\arg\min}\ \rho^{Pol}(\bar{I},g).

Definition [2.11](https://arxiv.org/html/2602.16401v1#S2.Thmtheorem11 "Definition 2.11. ‣ 2.4. A Sequential-Move Game ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") suggests that Stackelberg equilibria can be characterized through a two-step procedure. In the first step, for a fixed pricing distortion function gg, the policyholder chooses an indemnity function that minimizes their risk exposure. This problem will be referred to as the *policyholder’s problem*. In the second step, anticipating the policyholder’s optimal response as a function of gg, the insurer selects a pricing distortion function g∗g^{\*} that maximizes expected profit. This problem will be referred to as the *insurer’s problem*.

For a given insurance contract (I,π)∈ℐL×ℝ(I,\pi)\in\mathcal{I}\_{L}\times\mathbb{R}, the policyholder’s risk exposure and the insurer’s expected profit can be written as

|  |  |  |
| --- | --- | --- |
|  | ρP​o​l​(I,π)=ρP​o​l​(X−I​(X)+π)​ and ​VI​n​(I,π)=π−𝔼​[I​(X)].\rho^{Pol}(I,\pi)=\rho^{Pol}\left(X-I(X)+\pi\right)\ \hbox{ and }\ V^{In}(I,\pi)=\pi-\mathbb{E}\left[I(X)\right]. |  |

###### Definition 2.12.

An insurance contract (I∗,π∗)∈ℐL×ℝ(I^{\*},\pi^{\*})\in\mathcal{I}\_{L}\times\mathbb{R} is said to be individually rational, IR, if

|  |  |  |
| --- | --- | --- |
|  | ρP​o​l​(I∗,π∗)≤ρP​o​l​(0,0)​ and ​VI​n​(I∗,π∗)≥VI​n​(0,0).\rho^{Pol}(I^{\*},\pi^{\*})\leq\rho^{Pol}(0,0)\ \hbox{ and }\ V^{In}(I^{\*},\pi^{\*})\geq V^{In}(0,0). |  |

Definition [2.12](https://arxiv.org/html/2602.16401v1#S2.Thmtheorem12 "Definition 2.12. ‣ 2.4. A Sequential-Move Game ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") states that an insurance contract (I∗,π∗)∈ℐL×ℝ(I^{\*},\pi^{\*})\in\mathcal{I}\_{L}\times\mathbb{R} is individually rational, if it incentivizes the policyholder and the monopolist insurer to participate in the market.

###### Definition 2.13.

An insurance contract (I∗,π∗)∈ℐL×ℝ(I^{\*},\pi^{\*})\in\mathcal{I}\_{L}\times\mathbb{R} is said to be Pareto optimal, PO, if there does not exist another contract (I,π)∈ℐL×ℝ(I,\pi)\in\mathcal{I}\_{L}\times\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | ρP​o​l​(I,π)≤ρP​o​l​(I∗,π∗)​ and ​VI​n​(I,π)≥VI​n​(I∗,π∗),\rho^{Pol}(I,\pi)\leq\rho^{Pol}(I^{\*},\pi^{\*})\ \hbox{ and }\ V^{In}(I,\pi)\geq V^{In}(I^{\*},\pi^{\*}), |  |

with at least one strict inequality.

Definition [2.13](https://arxiv.org/html/2602.16401v1#S2.Thmtheorem13 "Definition 2.13. ‣ 2.4. A Sequential-Move Game ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") states that an insurance contract (I∗,π∗)∈ℐL×ℝ(I^{\*},\pi^{\*})\in\mathcal{I}\_{L}\times\mathbb{R} is Pareto optimal if there is no alternative contract that weakly reduces the policyholder’s risk exposure and weakly increases the insurer’s profit, with at least one of these improvements being strict.

## 3. Characterization of Stackelberg Equilibria

In this Section, we aim to characterize Stackelberg equilibria through a two-step procedure as suggested in Definition [2.11](https://arxiv.org/html/2602.16401v1#S2.Thmtheorem11 "Definition 2.11. ‣ 2.4. A Sequential-Move Game ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"). Specifically, in Subsection [3.1](https://arxiv.org/html/2602.16401v1#S3.SS1 "3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"), we study the policyholder’s problem, which constitutes the first step in determining Stackelberg equilibria. Then, in Subsection [3.2](https://arxiv.org/html/2602.16401v1#S3.SS2 "3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"), we consider the second step by addressing the insurer’s problem.

### 3.1. The Policyholder’s Problem

For a given choice of pricing distortion function gg, the policyholder chooses an indemnity I∈ℐLI\in\mathcal{I}\_{L} to minimize risk exposure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minI∈ℐL⁡ρP​o​l​(I,g).\displaystyle\min\limits\_{I\in\mathcal{I}\_{L}}\,\rho^{Pol}(I,g). |  | (6) |

To analyze the policyholder’s problem given in ([6](https://arxiv.org/html/2602.16401v1#S3.E6 "Equation 6 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")), we impose the following assumption on the loss distribution that will allow us to reformulate the problem in terms of quantile functions.

###### Assumption 3.1.

The cumulative distribution function FXF\_{X} is strictly increasing.

It follows from Assumption [3.1](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") that FXF\_{X} is differentiable almost everywhere. Moreover, by Föllmer and Schied ([2016](https://arxiv.org/html/2602.16401v1#bib.bib9 "Stochastic Finance: An Introduction in Discrete Time – 4⁢th ed."), Lemma A.25), Assumption [3.1](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") also guarantees that U:=FX​(X)U:=F\_{X}(X) is uniformly distributed on (0,1)(0,1), and that X=FX−1​(U),ℙX=F\_{X}^{-1}(U),\ \mathbb{P}-a.s.

###### Remark 3.2.

For each I∈ℐLI\in\mathcal{I}\_{L}, I​(X)I(X) and X−I​(X)X-I(X) have strictly increasing cumulative distribution functions by Assumption [3.1](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem1 "Assumption 3.1. ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"). Consequently, their quantile functions are strictly increasing, left-continuous, and differentiable a.e. on [0,1][0,1].

For any Z∈B+​(ℱ)Z\in B^{+}(\mathcal{F}) whose quantile function FZ−1F\_{Z}^{-1} is differentiable almost everywhere, the policyholder’s risk measure admits the following representation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρP​o​l​(Z)\displaystyle\rho^{Pol}(Z) | =∫Z​dT∘ℙ=∫(FZ−1)′​(U)​T​(1−U)​dℙ.\displaystyle=\int\,Z\,\mathrm{d}T\circ\mathbb{P}=\int\left(F\_{Z}^{-1}\right)^{\prime}(U)\,T(1-U)\,\mathrm{d}\mathbb{P}. |  |

Similarly, the premium evaluated under the given pricing distortion gg can be written as

|  |  |  |
| --- | --- | --- |
|  | Πg​(Z)=∫Z​𝑑g∘ℙ=∫(FZ−1)′​(U)​g​(1−U)​dℙ.\displaystyle\Pi\_{g}\left(Z\right)=\int Z\,dg\circ\mathbb{P}=\int\left(F\_{Z}^{-1}\right)^{\prime}(U)\,g(1-U)\,\mathrm{d}\mathbb{P}. |  |

Applying these formulas to the retention R​(X)R(X) and the indemnity I​(X)I(X) respectively, and using expression ([5](https://arxiv.org/html/2602.16401v1#S2.E5 "Equation 5 ‣ 2.3. Market Mechanisms and Contracts ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) of ρPol​(I,g)\rho^{\mathrm{Pol}}(I,g), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρP​o​l​(I,g)=∫(FR​(X)−1)′​(U)​T​(1−U)​dℙ+∫(FI​(X)−1)′​(U)​g​(1−U)​dℙ.\rho^{Pol}(I,g)=\int\left(F\_{R(X)}^{-1}\right)^{\prime}(U)\ T(1-U)\,\mathrm{d}\mathbb{P}+\int\left(F\_{I(X)}^{-1}\right)^{\prime}(U)\ g(1-U)\,\mathrm{d}\mathbb{P}. |  | (7) |

###### Remark 3.3.

Since X=I​(X)+R​(X)X=I(X)+R(X), we can write FX−1=FI​(X)−1+FR​(X)−1F\_{X}^{-1}=F\_{I(X)}^{-1}+F\_{R(X)}^{-1}, by comonotonic additivity of the quantile function.

As a result of the above remark, ([7](https://arxiv.org/html/2602.16401v1#S3.E7 "Equation 7 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) can be rewritten as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρP​o​l​(I,g)\displaystyle\rho^{Pol}(I,g) | =∫01(FR​(X)−1)′​(t)​[T​(1−t)−g​(1−t)]​dt+∫01(FX−1)′​(t)​g​(1−t)​dt.\displaystyle=\int\_{0}^{1}\left(F\_{R(X)}^{-1}\right)^{\prime}(t)\ \left[T(1-t)-g(1-t)\right]\mathrm{d}t+\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\ g(1-t)\mathrm{d}t. |  |

Let 𝒬L\mathcal{Q}\_{L} be the set of admissible quantile functions, defined as

|  |  |  |
| --- | --- | --- |
|  | 𝒬L={q∈𝒬|q​(0)=0, 0≤q′​(t)≤(FX−1)′​(t)}.\mathcal{Q}\_{L}=\left\{q\in\mathcal{Q}\,\Big|\,q(0)=0,\ 0\leq q^{\prime}(t)\leq\left(F\_{X}^{-1}\right)^{\prime}(t)\right\}. |  |

Each q∈𝒬Lq\in\mathcal{Q}\_{L} corresponds to the quantile of the retention random variable R​(X)=X−I​(X)R(X)=X-I(X) for some admissible I∈ℐLI\in\mathcal{I}\_{L}. Hence, for a given q∈𝒬Lq\in\mathcal{Q}\_{L}, we have:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ρP​o​l​(q,g)\displaystyle\rho^{Pol}(q,g) | =∫01q′​(t)​[T​(1−t)−g​(1−t)]​dt+∫01(FX−1)′​(t)​g​(1−t)​dt.\displaystyle=\int\_{0}^{1}q^{\prime}(t)\,\left[T(1-t)-g(1-t)\right]\,\mathrm{d}t+\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,g(1-t)\,\mathrm{d}t. |  | (8) |

Reformulating the policyholder’s problem ([6](https://arxiv.org/html/2602.16401v1#S3.E6 "Equation 6 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) in quantile form, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minq∈𝒬L⁡ρP​o​l​(q,g).\displaystyle\min\limits\_{q\in\mathcal{Q}\_{L}}\rho^{Pol}(q,g). |  | (9) |

###### Lemma 3.4.

For a given pricing distortion function gg, the feasible quantile qg​(t)∈𝒬Lq\_{g}(t)\in\mathcal{Q}\_{L} is optimal for ([9](https://arxiv.org/html/2602.16401v1#S3.E9 "Equation 9 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) if and only if the indemnity Ig​(x)=x−qg​(FX​(x))I\_{g}(x)=x-q\_{g}\left(F\_{X}(x)\right) is optimal for ([6](https://arxiv.org/html/2602.16401v1#S3.E6 "Equation 6 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")).

###### Proof.

The proof can be found in Appendix [A.1](https://arxiv.org/html/2602.16401v1#A1.SS1 "A.1. Proof of Lemma 3.4 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
∎

###### Lemma 3.5.

For a given pricing distortion function gg, a quantile function qgq\_{g} is optimal for ([9](https://arxiv.org/html/2602.16401v1#S3.E9 "Equation 9 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | (qg)′​(t)={0,g​(1−t)<T​(1−t),ϕg​(t),g​(1−t)=T​(1−t),(FX−1)′​(t),g​(1−t)>T​(1−t),\left(q\_{{g}}\right)^{\prime}(t)=\left\{\begin{array}[c]{ll}0,&g(1-t)<T(1-t),\vskip 5.69046pt\\ \phi\_{g}(t),&g(1-t)=T(1-t),\vskip 5.69046pt\\ \left(F\_{X}^{-1}\right)^{\prime}(t),&g(1-t)>T(1-t),\end{array}\right. |  | (10) |

where ϕg​(t)∈[0,(FX−1)′​(t)]\phi\_{g}(t)\in\left[0,\left(F\_{X}^{-1}\right)^{\prime}(t)\right], for almost every t∈[0,1]t\in[0,1] such that g​(1−t)=T​(1−t)g(1-t)=T(1-t).

###### Proof.

The proof can be found in Appendix [A.2](https://arxiv.org/html/2602.16401v1#A1.SS2 "A.2. Proof of Lemma 3.5 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
∎

###### Theorem 3.6.

For a given pricing distortion function gg, an indemnity function IgI\_{g} is optimal for the policyholder’s problem given in ([6](https://arxiv.org/html/2602.16401v1#S3.E6 "Equation 6 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) if and only if it is of the form Ig​(x)=∫0xκ​(y)​𝑑yI\_{g}(x)=\int\_{0}^{x}\kappa(y)\,dy, for all x∈[0,M]x\in[0,M], with κ:[0,M]→[0,1]\kappa:[0,M]\to[0,1] satisfying the following:

|  |  |  |
| --- | --- | --- |
|  | κ​(y)={1,g​(ℙ​[X>y])<T​(ℙ​[X>y]),1−ϕg​(FX​(y))​fX​(y),g​(ℙ​[X>y])=T​(ℙ​[X>y]),0,g​(ℙ​[X>y])>T​(ℙ​[X>y]),\kappa(y)=\left\{\begin{array}[c]{ll}1,&g\left(\mathbb{P}[X>y]\right)<T\left(\mathbb{P}[X>y]\right),\vskip 5.69046pt\\ 1-\phi\_{g}(F\_{X}(y))\,f\_{X}(y),&g\left(\mathbb{P}[X>y]\right)=T\left(\mathbb{P}[X>y]\right),\vskip 5.69046pt\\ 0,&g\left(\mathbb{P}[X>y]\right)>T\left(\mathbb{P}[X>y]\right),\end{array}\right. |  |

where ϕg​(t)∈[0,(FX−1)′​(t)]\phi\_{g}(t)\in\left[0,\left(F\_{X}^{-1}\right)^{\prime}(t)\right], for almost every t∈[0,1]t\in[0,1] such that g​(1−t)=T​(1−t)g(1-t)=T(1-t), and fXf\_{X} denotes the probability density function of the loss XX.

###### Proof.

The proof follows immediately from Lemmata [3.4](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") and [3.5](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
∎

Theorem [3.6](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem6 "Theorem 3.6. ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") characterizes the set of optimal indemnity functions for a given pricing distortion function gg, in terms of the policyholder’s marginal indemnification. Specifically, full indemnification is optimal when the insurer’s pricing distortion assigns less weight to tail probabilities than the policyholder’s distortion function TT. The policyholder retains the entire loss if the insurer’s pricing distortion overweights the tail probability compared to the policyholder’s distortion. Finally, when the policyholder’s distortion is equal to the insurer’s pricing distortion at a given tail probability, the policyholder may receive partial coverage, as long as feasibility is maintained.

This structural characterization is consistent with Assa ([2015](https://arxiv.org/html/2602.16401v1#bib.bib17 "On Optimal Reinsurance Policy with Distortion Risk Measures and Premiums")), who considers a reinsurance problem in which the premium principle is fixed and distortion based, and characterizes the optimal contract of the policyholder. In contrast, our result arises as the policyholder’s best response within a Stackelberg framework, where the pricing distortion is a strategic choice of the insurer. Moreover, in the absence of strategic interaction and when the policyholder’s problem only is considered, our model reduces to the setting analyzed in Assa ([2015](https://arxiv.org/html/2602.16401v1#bib.bib17 "On Optimal Reinsurance Policy with Distortion Risk Measures and Premiums")).

### 3.2. The Insurer’s Problem

The optimal indemnity characterized in Theorem [3.6](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem6 "Theorem 3.6. ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") is not unique. The insurer’s objective is to identify a market mechanism (Ig∗∗,g∗)(I^{\*}\_{g^{\*}},g^{\*}) that solves the following problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxg⁡VI​n​(Ig,g),such that​Ig∈arg⁡minI∈ℐL⁡ρP​o​l​(I,g).\displaystyle\max\_{g}\,V^{In}(I\_{g},g),\ \text{such that}\ I\_{g}\in\arg\min\_{I\in\mathcal{I}\_{L}}\,\rho^{Pol}(I,g). |  | (11) |

###### Lemma 3.7.

The market mechanism (Ig∗∗,g∗)(I^{\*}\_{g^{\*}},g^{\*}) is a Stackelberg equilibrium if and only if it is optimal for the insurer’s problem in ([11](https://arxiv.org/html/2602.16401v1#S3.E11 "Equation 11 ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")).

###### Proof.

The proof follows immediately from Definition [2.11](https://arxiv.org/html/2602.16401v1#S2.Thmtheorem11 "Definition 2.11. ‣ 2.4. A Sequential-Move Game ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
∎

The insurer’s problem ([11](https://arxiv.org/html/2602.16401v1#S3.E11 "Equation 11 ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) can be reformulated using quantile functions, similarly to the policyholder’s problem analyzed in Subsection [3.1](https://arxiv.org/html/2602.16401v1#S3.SS1 "3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"). Consider a market mechanism (I,g)(I,g), using Remark [3.3](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem3 "Remark 3.3. ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"), the premium can be written as

|  |  |  |
| --- | --- | --- |
|  | Πg​(I​(X))=∫01[(FX−1)′​(t)−(FR​(X)−1)′​(t)]​g​(1−t)​dt.\Pi\_{g}\big(I(X)\big)=\int\_{0}^{1}\left[\left(F\_{X}^{-1}\right)^{\prime}(t)-\left(F\_{R(X)}^{-1}\right)^{\prime}(t)\right]\,g(1-t)\,\mathrm{d}t. |  |

Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[I​(X)]\displaystyle\mathbb{E}\left[I(X)\right] | =∫01[FX−1​(t)−FR​(X)−1​(t)]​dt.\displaystyle=\int\_{0}^{1}\left[F\_{X}^{-1}(t)-F\_{R(X)}^{-1}(t)\right]\,\mathrm{d}t. |  |

Substituting the quantile representations of the premium and the expected indemnity into VI​n​(Ig,g)V^{In}(I\_{g},g) in ([3](https://arxiv.org/html/2602.16401v1#S2.E3 "Equation 3 ‣ 2.3. Market Mechanisms and Contracts ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")), where RgR\_{g} denotes the retention function associated with IgI\_{g}, yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VI​n​(Ig,g)\displaystyle V^{In}(I\_{g},g) | =∫01[(FX−1)′​(t)−(FRg​(X)−1)′​(t)]​g​(1−t)​dt−∫01[FX−1​(t)−FRg​(X)−1​(t)]​dt.\displaystyle=\int\_{0}^{1}\left[\left(F\_{X}^{-1}\right)^{\prime}(t)-\left(F\_{R\_{g}(X)}^{-1}\right)^{\prime}(t)\right]\,g(1-t)\,\mathrm{d}t-\int\_{0}^{1}\left[F\_{X}^{-1}(t)-F\_{R\_{g}(X)}^{-1}(t)\right]\,\mathrm{d}t. |  |

For a given quantile q∈𝒬Lq\in\mathcal{Q}\_{L}, this expression reduces to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VI​n​(q,g)\displaystyle V^{In}(q,g) | =∫01[(FX−1)′​(t)−q′​(t)]​g​(1−t)​dt−∫01[FX−1​(t)−q​(t)]​dt.\displaystyle=\int\_{0}^{1}\left[\left(F\_{X}^{-1}\right)^{\prime}(t)-q^{\prime}(t)\right]\,g(1-t)\,\mathrm{d}t-\int\_{0}^{1}\left[F\_{X}^{-1}(t)-q(t)\right]\,\mathrm{d}t. |  |

Hence, the insurer’s problem can be equivalently written in quantile form as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxg⁡VI​n​(qg,g),such that qg∈arg⁡minq∈𝒬L⁡ρP​o​l​(q,g).\displaystyle\max\limits\_{g}\,V^{In}(q\_{g},g),\ \text{such that $q\_{g}\in\arg\min\_{q\in\mathcal{Q}\_{L}}\rho^{Pol}(q,g)$}. |  | (12) |

The following result suggests that solving the insurer’s problem ([11](https://arxiv.org/html/2602.16401v1#S3.E11 "Equation 11 ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) is equivalent to solving ([12](https://arxiv.org/html/2602.16401v1#S3.E12 "Equation 12 ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")), providing a one-to-one correspondence between optimal solutions in the quantile space and optimal mechanisms.

###### Lemma 3.8.

(qg,g)(q\_{g},g) is optimal for ([12](https://arxiv.org/html/2602.16401v1#S3.E12 "Equation 12 ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) if and only if (Ig,g)(I\_{g},g) is optimal for ([11](https://arxiv.org/html/2602.16401v1#S3.E11 "Equation 11 ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")), where Ig​(x)=x−qg​(FX​(x))I\_{g}(x)=x-q\_{g}\left(F\_{X}(x)\right), for all x∈[0,M]x\in[0,M].

###### Proof.

The proof is similar to that of Lemma [3.4](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
∎

###### Theorem 3.9.

(qg∗∗,g∗)(q^{\*}\_{g^{\*}},{g}^{\*}) is optimal for ([12](https://arxiv.org/html/2602.16401v1#S3.E12 "Equation 12 ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) if and only if the following two conditions hold:

1. (1)

   The optimal pricing distortion g∗g^{\*} satisfies g∗​(t)=1−g~∗​(1−t)g^{\*}(t)=1-\widetilde{g}^{\*}(1-t) for all t∈[0,1]t\in[0,1], where the optimal pricing conjugate g~∗\widetilde{g}^{\*} is given by:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | g~∗​(t)={T~​(t),T~​(t)<t,∈[sup{z<t;g~∗​(z)},T~​(t)],T~​(t)≥t,\widetilde{g}^{\*}(t)=\left\{\begin{array}[c]{ll}\widetilde{T}(t),&\widetilde{T}(t)<t,\vskip 8.5359pt\\ \in\left[\,\sup\left\{z<t;\ \widetilde{g}^{\*}(z)\right\},\widetilde{T}(t)\right],&\widetilde{T}(t)\geq t,\end{array}\right. |  | (13) |

   and T~\widetilde{T} is the conjugate distortion function of TT.
2. (2)

   The optimal quantile qg∗∗q^{\*}\_{g^{\*}} satisfies:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | (qg∗∗)′​(t)={0,T~​(t)<t,ϕg∗​(t)t∈{z;g~∗​(z)=T~​(z)=z},(FX−1)′​(t),t∈{z;g~∗​(z)<T~​(z)=z}∪{z;T~​(z)>z},\left(q^{\*}\_{{g}^{\*}}\right)^{\prime}(t)=\left\{\begin{array}[c]{ll}0,&\widetilde{T}(t)<t,\vskip 5.69046pt\\ \phi\_{g^{\*}}(t)&t\in\{z;\ \widetilde{g}^{\*}(z)=\widetilde{T}(z)=z\},\vskip 5.69046pt\\ \left(F\_{X}^{-1}\right)^{\prime}(t),&t\in\{z;\ \widetilde{g}^{\*}(z)<\widetilde{T}(z)=z\}\cup\{z;\ \widetilde{T}(z)>z\},\end{array}\right. |  | (14) |

   where ϕg∗​(t)∈[0,(FX−1)′​(t)]\phi\_{g^{\*}}(t)\in\left[0,\left(F\_{X}^{-1}\right)^{\prime}(t)\right] for a.e. t∈[0,1]t\in[0,1] such that g~∗​(t)=T~​(t)=t.\widetilde{g}^{\*}(t)=\widetilde{T}(t)=t.

Moreover, the insurer’s expected profit under (qg∗∗,g∗)(q^{\*}\_{g^{\*}},g^{\*}) is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VI​n​(qg∗∗,g∗)=∫01(FX−1)′​(t)​(t−T~​(t))​𝟙{T~​(t)<t}​dt.V^{In}\left(q^{\*}\_{g^{\*}},g^{\*}\right)=\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,(t-\widetilde{T}(t))\mathbbm{1}\_{\{\widetilde{T}(t)<t\}}\,\mathrm{d}t. |  | (15) |

###### Proof.

The proof can be found in Appendix [A.3](https://arxiv.org/html/2602.16401v1#A1.SS3 "A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
∎

Theorem [3.9](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem9 "Theorem 3.9. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") provides a complete characterization of the Stackelberg equilibrium by identifying the optimal pricing distortion g∗g^{\*} and the induced optimal quantile qg∗∗q^{\*}\_{g^{\*}}. The following corollary explicitly provides the characterization of Stackelberg equilibria in terms of market mechanisms of the form (Ig,g)(I\_{g},g).

###### Corollary 3.10.

The market mechanism (Ig∗∗,g∗)(I^{\*}\_{g^{\*}},g^{\*}) is optimal for ([11](https://arxiv.org/html/2602.16401v1#S3.E11 "Equation 11 ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) if and only if the following two conditions hold:

1. (1)

   The optimal pricing distortion g∗g^{\*} is given by:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | g∗​(t)={T​(t),T​(t)>t,∈[T​(t),inf{z>t:g∗​(z)}],T​(t)≤t,g^{\*}(t)=\left\{\begin{array}[c]{ll}T(t),&T(t)>t,\vskip 8.5359pt\\ \in\left[\,T(t),\,\inf\left\{z>t:g^{\*}(z)\right\}\right],&T(t)\leq t,\end{array}\right. |  | (16) |
2. (2)

   The optimal indemnity satisfies Ig∗∗​(x)=∫0xκ∗​(y)​dyI^{\*}\_{g^{\*}}(x)=\int\_{0}^{x}\kappa^{\*}(y)\,\mathrm{d}y for all x∈[0,M]x\in[0,M], where κ∗:[0,M]→[0,1]\kappa^{\*}:[0,M]\to[0,1] is defined as follows:

   |  |  |  |
   | --- | --- | --- |
   |  | κ∗​(y):={1,ℙ​[X>y]<T​(ℙ​[X>y]),1−ϕg∗​(FX​(y))​fX​(y),g∗​(ℙ​[X>y])=T​(ℙ​[X>y])=ℙ​[X>y],0,g∗​(ℙ​[X>y])>T​(ℙ​[X>y])=ℙ​[X>y],or ​ℙ​[X>y]>T​(ℙ​[X>y]),\kappa^{\*}(y):=\begin{cases}1,&\mathbb{P}[X>y]<T(\mathbb{P}[X>y]),\\[3.00003pt] 1-\phi\_{g^{\*}}(F\_{X}(y))\,f\_{X}(y),&g^{\*}(\mathbb{P}[X>y])=T(\mathbb{P}[X>y])=\mathbb{P}[X>y],\\[3.00003pt] 0,&g^{\*}(\mathbb{P}[X>y])>T(\mathbb{P}[X>y])=\mathbb{P}[X>y],\text{or }\mathbb{P}[X>y]>T(\mathbb{P}[X>y]),\end{cases} |  |

   where ϕg∗​(t)∈[0,(FX−1)′​(t)]\phi\_{g^{\*}}(t)\in\left[0,\left(F\_{X}^{-1}\right)^{\prime}(t)\right], for a.e. t∈[0,1]t\in[0,1] such that g∗​(1−t)=T​(1−t)=1−tg^{\*}(1-t)=T(1-t)=1-t.

###### Proof.

The proof follows immediately from Lemma [3.8](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem8 "Lemma 3.8. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") and Theorem [3.9](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem9 "Theorem 3.9. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
∎

###### Theorem 3.11.

Consider two policyholders whose respective distortion functions T1T\_{1} and T2T\_{2} satisfy T1​(t)≤T2​(t)T\_{1}(t)\leq T\_{2}(t) for all t∈[0,1]t\in[0,1]. Let (Ig1∗∗,g1∗)(I\_{g^{\*}\_{1}}^{\*},g\_{1}^{\*}) and (Ig2∗∗,g2∗)(I\_{g^{\*}\_{2}}^{\*},g\_{2}^{\*}) denote the corresponding Stackelberg equilibria. Then, the following holds.

1. (1)

   Ig1∗∗​(x)≤Ig2∗∗​(x)I\_{g^{\*}\_{1}}^{\*}(x)\leq I\_{g^{\*}\_{2}}^{\*}(x), for all x∈[0,M]x\in[0,M].
2. (2)

   VI​n​(Ig1∗∗,g1∗)≤VI​n​(Ig2∗∗,g2∗)V^{In}(I\_{g^{\*}\_{1}}^{\*},g\_{1}^{\*})\leq V^{In}(I\_{g^{\*}\_{2}}^{\*},g\_{2}^{\*})

Theorem [3.11](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem11 "Theorem 3.11. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") states that under Stackelberg equilibria, the optimal insurance coverage and the insurer’s expected profit both increase as the policyholder becomes weakly more risk averse in the sense of Proposition [2.5](https://arxiv.org/html/2602.16401v1#S2.Thmtheorem5 "Proposition 2.5. ‣ 2.2. Risk Aversion ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"). That is, the more weakly risk averse the policyholder is, the more coverage they receive, and the more profitable the insurer becomes. The following corollary shows that this result also holds under strong risk aversion.

###### Corollary 3.12.

Under Stackelberg equilibria, if the policyholder becomes more strongly risk averse, then both the optimal insurance coverage and the insurer’s expected profit increase.

###### Proof.

The proof of this result follows immediately from Remark [2.6](https://arxiv.org/html/2602.16401v1#S2.Thmtheorem6 "Remark 2.6. ‣ 2.2. Risk Aversion ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") and Theorem [3.11](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem11 "Theorem 3.11. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
∎

In contrast to this clear monotonic relationship with respect to risk aversion obtained in Theorem [3.11](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem11 "Theorem 3.11. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") and Corollary [3.12](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem12 "Corollary 3.12. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"), no such monotonicity can generally be established for the insurance coverage or the insurer’s expected profit when the policyholder’s risk distribution itself changes.

## 4. Pareto Efficiency of Stackelberg Equilibria

In this section, we examine whether the Stackelberg equilibria characterized in Section [3](https://arxiv.org/html/2602.16401v1#S3 "3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") lead to Pareto efficient contracts. We first characterize Pareto optimal insurance contracts and then establish their relationship with Stackelberg equilibria. The proofs of these results can be found in Appendix [A.5](https://arxiv.org/html/2602.16401v1#A1.SS5 "A.5. Proof of Proposition 4.1 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"), Appendix [A.6](https://arxiv.org/html/2602.16401v1#A1.SS6 "A.6. Proof of Proposition 4.2 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"), and Appendix [A.7](https://arxiv.org/html/2602.16401v1#A1.SS7 "A.7. Proof of Proposition 4.3 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").

###### Proposition 4.1.

An insurance contract (I∗,π∗)(I^{\*},\pi^{\*}) is Pareto optimal if and only if it solves the following problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min(I,π)∈ℐL×ℝ⁡{ρP​o​l​(I,π)−VI​n​(I,π)}.\min\limits\_{(I,\pi)\in\mathcal{I}\_{L}\times\mathbb{R}}\,\left\{\rho^{Pol}(I,\pi)-V^{In}(I,\pi)\right\}. |  | (17) |

###### Proposition 4.2.

Let (Ig∗∗,g∗)(I^{\*}\_{g^{\*}},g^{\*}) be a Stackelberg equilibrium characterized in Corollary [3.10](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem10 "Corollary 3.10. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"). The induced insurance contract (Ig∗∗,πg∗∗)(I^{\*}\_{g^{\*}},\pi^{\*}\_{g^{\*}}) is individually rational and Pareto optimal. Moreover, ρP​o​l​(Ig∗∗,πg∗∗)=ρP​o​l​(0,0)\rho^{Pol}(I^{\*}\_{g^{\*}},\pi^{\*}\_{g^{\*}})=\rho^{Pol}(0,0).

Proposition [4.2](https://arxiv.org/html/2602.16401v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") establishes a first welfare theorem for the sequential-move monopolistic market considered in this paper. Specifically, Stackelberg equilibria lead to Pareto optimal insurance contracts. Moreover, in equilibrium, the policyholder is indifferent between participating in the market and not participating, and the monopolist insurer extracts all surplus. In contrast, not every Pareto optimal contract arises from a Stackelberg equilibrium mechanism. The following result discusses the conditions under which Pareto optimal contracts are induced by Stackelberg equilibria.

###### Proposition 4.3.

Consider a Pareto optimal contract (I∗,π∗)(I^{\*},\pi^{\*}) satisfying ρPol​(I∗,π∗)=ρPol​(0,0)\rho^{\text{Pol}}(I^{\*},\pi^{\*})=\rho^{\text{Pol}}(0,0). Then there exists a Stackelberg equilibrium (I∗,gI∗∗)(I^{\*},g^{\*}\_{I^{\*}}) that induces the Pareto optimal contract (I∗,π∗)(I^{\*},\pi^{\*}), that is,

|  |  |  |
| --- | --- | --- |
|  | ΠgI∗∗​(I∗​(X))=π∗.\Pi\_{g^{\*}\_{I^{\*}}}\left(I^{\*}(X)\right)=\pi^{\*}. |  |

Proposition [4.3](https://arxiv.org/html/2602.16401v1#S4.Thmtheorem3 "Proposition 4.3. ‣ 4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") states that the Pareto optimal contracts that leave the policyholder indifferent between participating and not participating in the market are induced by Stackelberg equilibrium mechanisms.

The results of this section are consistent with findings of the existing literature, e.g., Boonen and Ghossoub ([2023](https://arxiv.org/html/2602.16401v1#bib.bib48 "Bowley vs. Pareto Optima in Reinsurance Contracting")), Ghossoub and Zhu ([2024](https://arxiv.org/html/2602.16401v1#bib.bib42 "Stackelberg Equilibria with Multiple Policyholders")), in which the monopolistic market is modeled as a sequential-move game. Additionally, Andraos et al. ([2026](https://arxiv.org/html/2602.16401v1#bib.bib10 "Subgame perfect nash equilibria in large reinsurance markets")) consider a generalized framework and obtain similar results for the special case of monopoly. Specifically, Stackelberg equilibria yield Pareto optimality without inducing any welfare gain to the policyholder. Conversely, only the Pareto optimal contracts that leave the policyholder indifferent between suffering loss and entering the market are induced from Stackelberg equilibrium mechanisms.

## 5. Examples

In this section, we assume that the policyholder evaluates risk using a specific class of risk measures, and we examine the resulting Stackelberg equilibria. As established in Lemma [3.5](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") and Theorem [3.9](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem9 "Theorem 3.9. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"), the solutions to both stages of the Stackelberg game are generally not unique. Nevertheless, we show that under certain assumptions, Stackelberg equilibria may take one of several familiar forms such as full insurance, a coverage limit insurance contract, or a deductible insurance contract.

### 5.1. Optimality of Full Insurance

Suppose that the policyholder is weakly risk averse, that is, the distortion function satisfies

|  |  |  |
| --- | --- | --- |
|  | T​(t)≥t,∀t∈[0,1].T(t)\geq t,\ \forall t\in[0,1]. |  |

It follows from Corollary [3.10](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem10 "Corollary 3.10. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"), that the market mechanism (Ig∗∗,g∗)(I^{\*}\_{g^{\*}},g^{\*}) described below is a Stackelberg equilibrium:

|  |  |  |
| --- | --- | --- |
|  | g∗​(t)=T​(t),∀t∈[0,1],andIg∗∗​(x)=x,∀x∈[0,M].g^{\*}(t)=T(t),\ \forall\,t\in[0,1],\ \ \hbox{and}\ \ I^{\*}\_{g^{\*}}(x)=x,\ \forall\,x\in[0,M]. |  |

That is, the insurer offers full coverage, and the pricing distortion function coincides with the distortion function that reflects the policyholder’s risk aversion. This result also holds for a strongly risk averse policyholder, by Remark [2.6](https://arxiv.org/html/2602.16401v1#S2.Thmtheorem6 "Remark 2.6. ‣ 2.2. Risk Aversion ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").

This example covers many important risk preference models commonly used in practice, such as Tail Value-at-Risk (TVaR), which corresponds to a concave distortion function of the form

|  |  |  |
| --- | --- | --- |
|  | T​(t):=min⁡(1,t1−α),for a given α∈(0,1).T(t):=\min\left(1,\frac{t}{1-\alpha}\right),\ \text{for a given $\alpha\in(0,1)$}. |  |

Moreover, under TVaR, the insurer’s expected profit satisfies:

|  |  |  |
| --- | --- | --- |
|  | VI​n​(Ig∗∗,g∗)=∫01(FX−1)′​(t)​[t−T~​(t)]​ 1{T~​(t)<t}​dt≥0,V^{{In}}(I^{\*}\_{g^{\*}},\,g^{\*})=\int\_{0}^{1}\big(F\_{X}^{-1}\big)^{\prime}(t)\,\big[t-\widetilde{T}(t)\big]\,\mathbbm{1}\_{\{\widetilde{T}(t)<t\}}\,\mathrm{d}t\geq 0, |  |

since the set {t∈[0,1]:T~​(t)<t}\{t\in[0,1]:\widetilde{T}(t)<t\} has positive measure.

### 5.2. Optimality of Coverage Limit Contracts

In this example, we assume that the policyholder evaluates risk using Value-at-Risk (VaR) at confidence level α∈(0,1)\alpha\in(0,1). This corresponds to a distortion risk measure with distortion function

|  |  |  |
| --- | --- | --- |
|  | T​(t):=𝟙(1−α, 1]​(t),∀t∈[0,1].T(t):=\mathbbm{1}\_{(1-\alpha,\,1]}(t),\ \forall t\in[0,1]. |  |

It follows from Corollary [3.10](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem10 "Corollary 3.10. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") that a Stackelberg equilibrium (Ig∗∗,g∗)(I^{\*}\_{g^{\*}},g^{\*}) is characterized as follows. The optimal pricing distortions g∗g^{\*} satisfies

|  |  |  |
| --- | --- | --- |
|  | g∗​(t)={1,t>1−α,∈[ 0,inf{z>t:g∗​(z)}],t≤1−α,for a.e t∈[0,1], g^{\*}(t)=\begin{cases}1,&t>1-\alpha,\quad\\[6.0pt] \in\Big[\,0,\,\inf\big\{z>t:g^{\*}(z)\big\}\Big],&t\leq 1-\alpha,\quad\end{cases}\quad\text{for a.e $t\in[0,1]$, } |  |

and the optimal indemnity function Ig∗∗I^{\*}\_{g^{\*}} is given by

|  |  |  |
| --- | --- | --- |
|  | Ig∗∗​(x)={x,x<FX−1​(α),FX−1​(α),x≥FX−1​(α),∀x∈[0,M].I^{\*}\_{g^{\*}}(x)=\begin{cases}x,&x<F\_{X}^{-1}(\alpha),\quad\\[6.0pt] F\_{X}^{-1}(\alpha),&x\geq F\_{X}^{-1}(\alpha),\quad\end{cases}\quad\forall x\in[0,M]. |  |

In this case, the policyholder receives full coverage for losses below the VaR threshold FX−1​(α)F\_{X}^{-1}(\alpha). Moreover, coverage is capped at this threshold level, so that for losses exceeding FX−1​(α)F\_{X}^{-1}(\alpha), the policyholder retains the excess loss. The insurer’s expected profit satisfies:

|  |  |  |
| --- | --- | --- |
|  | VI​n​(Ig∗∗,g∗)=∫01(FX−1)′​(t)​[t−T~​(t)]​ 1{T~​(t)<t}​dt=∫0αt⋅(FX−1)′​(t)​dt,V^{{In}}(I^{\*}\_{g^{\*}},\,g^{\*})=\int\_{0}^{1}\big(F\_{X}^{-1}\big)^{\prime}(t)\,\big[t-\widetilde{T}(t)\big]\,\mathbbm{1}\_{\{\widetilde{T}(t)<t\}}\,\mathrm{d}t=\int\_{0}^{\alpha}t\,\cdot\big(F\_{X}^{-1}\big)^{\prime}(t)\,\mathrm{d}t, |  |

since T~​(t)=𝟙[α,1]​(t)\widetilde{T}(t)=\mathbbm{1}\_{[\alpha,1]}(t), for all t∈[0,1]t\in[0,1]. Additionally, note that since FX−1F\_{X}^{-1} is strictly increasing, it follows that for a fixed x∈[0,M]x\in[0,M], the optimal indemnity function Ig∗∗I^{\*}\_{g^{\*}} weakly increases with the VaR confidence level α\alpha. Moreover, the insurer’s expected profit increases with α\alpha.

Hence, if the policyholder is a VaR minimizer, then the coverage limit contract is a Stackelberg equilibrium and depends on the chosen VaR confidence level α\alpha. In addition, a more risk-averse policyholder (with a higher value for α\alpha) receives greater coverage and generates higher expected profit for the insurer, consistently with Theorem [3.11](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem11 "Theorem 3.11. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") and Corollary [3.12](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem12 "Corollary 3.12. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").

The results of our examples so far, align with the findings of Cheung et al. ([2019](https://arxiv.org/html/2602.16401v1#bib.bib33 "Risk-Adjusted Bowley Reinsurance under Distorted Probabilities")), where the policyholder is assumed to be either strongly risk averse or a VaR minimizer. Specifically, if the policyholder’s preferences are represented by a DRM with a concave distortion function, the results of Example [5.1](https://arxiv.org/html/2602.16401v1#S5.SS1 "5.1. Optimality of Full Insurance ‣ 5. Examples ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") align with Cheung et al. ([2019](https://arxiv.org/html/2602.16401v1#bib.bib33 "Risk-Adjusted Bowley Reinsurance under Distorted Probabilities"), Theorem 3.1, case γ=0\gamma=0). On the other hand, if the distortion function corresponds to a VaR risk measure, then the results of Example [5.2](https://arxiv.org/html/2602.16401v1#S5.SS2 "5.2. Optimality of Coverage Limit Contracts ‣ 5. Examples ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") are consistent with Cheung et al. ([2019](https://arxiv.org/html/2602.16401v1#bib.bib33 "Risk-Adjusted Bowley Reinsurance under Distorted Probabilities"), Theorem 3.5, case γ=0\gamma=0).

### 5.3. Optimality of Deductible Contracts

We now assume that the policyholder uses an inverse-S-shaped distortion function (ISSD), which is commonly used to study decision making under uncertainty (e.g., Tversky and Kahneman ([1992](https://arxiv.org/html/2602.16401v1#bib.bib50 "Advances in Prospect Theory: Cumulative Representation of Uncertainty"))).

###### Definition 5.1.

A distortion function TT is said to be an inverse-S-shaped distortion function (ISSD) if it is twice-differentiable on (0,1)(0,1), and there exists t0∈(0,1)t\_{0}\in(0,1) such that:

1. (1)

   T′​(t)T^{\prime}(t) is strictly deceasing on (0,t0)(0,t\_{0}), and
2. (2)

   T′​(t)T^{\prime}(t) strictly increasing on (t0,1).(t\_{0},1).

Moreover, limt↓0T′​(t)>1,\lim\_{t\downarrow 0}T^{\prime}(t)>1, and limt↑1T′​(t)>1.\lim\_{t\uparrow 1}T^{\prime}(t)>1.

In this case, for Y∈B+​(ℱ)Y\in B^{+}(\mathcal{F}), the expression of the distortion risk measure is given by

|  |  |  |
| --- | --- | --- |
|  | ρ​(Y)=∫0+∞T​(ℙ​(Y≥y))​dy=∫0+∞y​T′​(1−FY​(y))​dFY​(y).\displaystyle\rho(Y)=\int\_{0}^{+\infty}T(\mathbb{P}(Y\geq y))\,\mathrm{d}y=\int\_{0}^{+\infty}\,y\,T^{\prime}(1-F\_{Y}(y))\,\mathrm{d}F\_{Y}(y). |  |

Assume that there exists t1∈(0,1)t\_{1}\in(0,1) such that T​(t1)=t1T(t\_{1})=t\_{1}. That is, t1t\_{1} is the intersection point between the identity function and the policyholder’s distortion function. We know from Corollary [3.10](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem10 "Corollary 3.10. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"), that the Stackelberg equilibrium (Ig∗∗,g∗)(I^{\*}\_{g^{\*}},g^{\*}) is characterized as follows. The optimal pricing distortion g∗g^{\*} satisfies:

|  |  |  |
| --- | --- | --- |
|  | g∗​(t)={T​(t),t<t1,∈[T​(t),inf{z>t:g∗​(z)}],t≥t1,for a.e. t∈[0,1],g^{\*}(t)=\begin{cases}T(t),&t<t\_{1},\quad\\[6.0pt] \in\big[\,T(t),\,\inf\{z>t:g^{\*}(z)\}\big],&t\geq t\_{1},\quad\end{cases}\quad\text{for a.e. $t\in[0,1]$,} |  |

and the optimal indemnity function Ig∗∗I^{\*}\_{g^{\*}} satisfies:

|  |  |  |
| --- | --- | --- |
|  | Ig∗∗​(x)={0,x≤FX−1​(1−t1),x−FX−1​(1−t1),x>FX−1​(1−t1),∀x∈[0,M].I^{\*}\_{g^{\*}}(x)=\begin{cases}0,&x\leq F\_{X}^{-1}(1-t\_{1}),\quad\\[6.0pt] x-F\_{X}^{-1}(1-t\_{1}),&x>F\_{X}^{-1}(1-t\_{1}),\quad\end{cases}\quad\forall x\in[0,M]. |  |

In this case, the optimal indemnity fully covers losses above a fixed deductible FX−1​(1−t1)F\_{X}^{-1}(1-t\_{1}), which is fully determined by t1t\_{1}. Hence, if the policyholder is more concerned about extreme losses, then the deductible contract is a Stackelberg equilibrium. Moreover, the insurer’s expected profit is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VI​n​(Ig∗∗,g∗)\displaystyle V^{In}\left(I^{\*}\_{{g}^{\*}},{g}^{\*}\right) | =∫0t1(FX−1)′​(1−t)​(T​(t)−t)​dt.\displaystyle=\int\_{0}^{t\_{1}}\left(F\_{X}^{-1}\right)^{\prime}(1-t)\left(T(t)-t\right)\,\mathrm{d}t. |  |

We note that for a fixed x∈[0,M]x\in[0,M], as t1t\_{1} increases, FX−1​(1−t1)F\_{X}^{-1}(1-t\_{1}) decreases, implying a greater insurance coverage. That is, the optimal indemnity Ig∗∗I^{\*}\_{g^{\*}} increases with t1t\_{1}. However, from the expression of the expected profit at equilibrium, we cannot conclude whether VI​n​(Ig∗∗,g∗)V^{In}\left(I^{\*}\_{{g}^{\*}},{g}^{\*}\right) increases with t1t\_{1}. This is because a higher value of t1t\_{1} implies a change in the distortion function TT on the interval [0,t1)[0,t\_{1}). Hence, to evaluate the impact of t1t\_{1} on the insurer’s expected profit, we consider the following concrete numerical example, in which the distortion function takes the form given in Tversky and Kahneman ([1992](https://arxiv.org/html/2602.16401v1#bib.bib50 "Advances in Prospect Theory: Cumulative Representation of Uncertainty")):

|  |  |  |
| --- | --- | --- |
|  | Tθ​(t):=tθ(tθ+(1−t)θ)1θ,T\_{\theta}(t):=\frac{t^{\theta}}{\left(t^{\theta}+(1-t)^{\theta}\right)^{\frac{1}{\theta}}}, |  |

where θ∈[0.3,0.8]\theta\in[0.3,0.8]. Additionally, we consider three cases for the distribution of the random loss XX.

We first assume that the random loss XX follows a uniform distribution with cumulative distribution function (CDF) given by

|  |  |  |
| --- | --- | --- |
|  | FX​(x)=xM,∀x∈[0,M]​and M=10.F\_{X}(x)=\frac{x}{M},\ \forall x\in[0,M]\ \text{and $M=10$}. |  |

Figure [1(a)](https://arxiv.org/html/2602.16401v1#S5.F1.sf1 "Figure 1(a) ‣ Figure 1 ‣ 5.3. Optimality of Deductible Contracts ‣ 5. Examples ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") plots the distortion functions TθT\_{\theta} for different values of θ\theta. The figure shows that as θ\theta increases, TθT\_{\theta} approaches the identity function, and the intersection point t1t\_{1} shifts to larger values. Moreover, functions with smaller values of θ\theta are more concave near 0 and more convex near 11, implying that the policyholder places greater emphasis on extreme losses.

Figure [1(b)](https://arxiv.org/html/2602.16401v1#S5.F1.sf2 "Figure 1(b) ‣ Figure 1 ‣ 5.3. Optimality of Deductible Contracts ‣ 5. Examples ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") depicts the insurer’s expected profit under the Stackelberg optimal contract as a function of t1t\_{1}. The result shows that the insurer’s expected profit does not vary monotonically with θ\theta or the intersection point t1t\_{1}. Notably, it reaches a maximum around t1≈0.32t\_{1}\approx 0.32.

![Refer to caption](x1.png)


(a) Policyholder’s Distortion Function.

![Refer to caption](x2.png)


(b) Insurer’s Expected Profit Under SE.

Figure 1. The case where XX follows a uniform distribution.

Alternatively, assume now that the loss random variable XX follows a truncated exponential distribution, with CDF given by

|  |  |  |
| --- | --- | --- |
|  | FX​(x)=1−exp⁡(−λ​x)1−exp⁡(−λ​M),∀x∈[0,M],M=10,and λ>0.F\_{X}(x)=\frac{1-\exp(-\lambda x)}{1-\exp(-\lambda M)},\ \forall x\in[0,M],\ M=10,\ \text{and $\lambda>0$}. |  |

Figure [2(a)](https://arxiv.org/html/2602.16401v1#S5.F2.sf1 "Figure 2(a) ‣ Figure 2 ‣ 5.3. Optimality of Deductible Contracts ‣ 5. Examples ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") plots the CDF for different values of λ\lambda. It shows that as λ\lambda increases, the CDF becomes steeper for small losses, implying that losses are more likely to take smaller values. Figure [2(b)](https://arxiv.org/html/2602.16401v1#S5.F2.sf2 "Figure 2(b) ‣ Figure 2 ‣ 5.3. Optimality of Deductible Contracts ‣ 5. Examples ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") plots the insurer’s profit as a function of t1t\_{1} for different values of λ\lambda. The insurer’s profit does not vary monotonically with the parameter θ\theta or the intersection point t1t\_{1}.

The result also depends on the loss distribution parameter λ\lambda. In particular, the insurer’s profit reaches its maximum around t1≈0.3t\_{1}\approx 0.3 when λ=0.1\lambda=0.1. When λ\lambda increases to 0.50.5, meaning that the distribution becomes more concentrated on the left, the maximum shifts to about t1≈0.22t\_{1}\approx 0.22, indicating that if the policyholder faces a lower probability of large losses, greater concern for extreme losses becomes more valuable to the insurer. When λ\lambda increases further to 11, implying that losses are even more likely to be small, the maximum shifts slightly further left, and the insurer’s profit then decreases monotonically with t1t\_{1}. This suggests that the insurer achieves the highest profit when the policyholder places more weight on extreme loss events.

![Refer to caption](x3.png)


(a) Cumulative Distribution Function.

![Refer to caption](x4.png)


(b) Insurer’s Expected Profit Under SE.

Figure 2. The case where XX follows a truncated exponential distribution.

Finally, assume that the random loss XX follows a Kumaraswamy distribution with CDF given by

|  |  |  |
| --- | --- | --- |
|  | FX​(x)=1−(1−(xM)a)b,∀x∈[0,M],M=10,and a,b>0.F\_{X}(x)=1-\big(1-(\tfrac{x}{M})^{a}\big)^{b},\ \forall x\in[0,M],\ M=10,\ \text{and $a,b>0$}. |  |

Figure [3(a)](https://arxiv.org/html/2602.16401v1#S5.F3.sf1 "Figure 3(a) ‣ Figure 3 ‣ 5.3. Optimality of Deductible Contracts ‣ 5. Examples ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") plots the CDFs for different combinations of aa and bb. The blue curve lies close to, but slightly below, the identity function, indicating that more losses are concentrated on the right compared to the uniform distribution. The red curve is more concave than the blue one, implying that larger losses are more likely. The green curve represents the most extreme right-skewed case among the three.

Figure [3(b)](https://arxiv.org/html/2602.16401v1#S5.F3.sf2 "Figure 3(b) ‣ Figure 3 ‣ 5.3. Optimality of Deductible Contracts ‣ 5. Examples ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") shows the corresponding insurer’s profit under these three scenarios. When a=1.5a=1.5 and b=1b=1, the insurer’s profit does not vary monotonically with t1t\_{1}, and it reaches its maximum around t1≈0.32t\_{1}\approx 0.32. When a=1.5a=1.5 and b=0.5b=0.5, meaning the loss distribution becomes riskier in the sense of first-order stochastic dominance, the insurer’s profit decreases for all t1t\_{1}. This suggests that when the underlying risk increases, the insurer’s profit declines regardless of the policyholder’s risk attitude. Moreover, the maximum shifts to the right, reaching about t1≈0.37t\_{1}\approx 0.37. When the loss becomes even riskier with a=2a=2 and b=0.3b=0.3, a similar decreasing pattern is observed, with the maximum shifting further to the right to approximately t1≈0.4t\_{1}\approx 0.4.

![Refer to caption](x5.png)


(a) Cumulative Distribution Function.

![Refer to caption](x6.png)


(b) Insurer’s Expected Profit Under SE.

Figure 3. The case where XX follows a Kumaraswamy distribution.

## 6. Conclusion

In this paper, we study Stackelberg Equilibria (Bowley optima) in a monopolistic centralized sequential-move insurance market. We consider a risk-neutral, profit-maximizing insurer who sets premia using a distortion premium principle, and a single policyholder who seeks to minimize a distortion risk measure.

We characterize Stackelberg equilibria explicitly, and we show that, in equilibrium, the optimal indemnity function exhibits a layer-type structure, providing full insurance over any loss layer on which the policyholder is more pessimistic than the insurer’s pricing functional about tail losses. Equilibrium contracts provide no coverage over loss layers on which the policyholder is less pessimistic than the insurer’s pricing functional about tail losses. When the policyholder and the insurer’s pricing functional are equally pessimistic about tail losses, the marginal indemnity may take an arbitrary shape, within the global feasibility constraints.
Additionally, in equilibrium, the optimal pricing distortion function is determined by the policyholder’s degree of (weak) risk aversion, that is, whether the policyholder’s distortion function is above or below the identity function, such that prices never exceed the policyholder’s marginal willingness to insure tail losses.

When the policyholder is either weakly risk averse (with a distortion function that lies above the identity function) or strongly risk averse (with a concave distortion function), we show that the optimal contract provides full insurance, and the optimal pricing distortion function coincides with that of the policyholder. For policyholders who evaluate risk using a VaR risk measure at a confidence level α∈(0,1)\alpha\in(0,1), the optimal coverage includes an upper limit, by providing full insurance for losses below the α\alpha-quantile while leaving the upper tail uninsured. For a policyholder who displays strong sensitivity to extreme losses, captured by an inverse-S-shaped distortion function, the optimal indemnity function takes the form of a deductible contract, whereby extreme losses are fully transferred to the insurer. Furthermore, we show that in a Stackelberg equilibrium, both the insurance coverage and the insurer’s expected profit increase with the policyholder’s degree of strong or weak risk aversion. A more risk-averse policyholder will receive greater insurance coverage under an equilibrium optimal contract, and is more valuable to the insurer.

Moreover, we examine the Pareto efficiency of equilibrium contracts. Echoing recent work in the literature, we show that equilibrium contracts are Pareto optimal, but they do not induce a welfare gain to the policyholder, which is unsurprising in a monopoly. Conversely, any Pareto-optimal contract that leaves no welfare gain to the policyholder can be obtained as a Stackelberg equilibrium contract.

## Appendix A Proofs of Main Results

### A.1. Proof of Lemma [3.4](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")

For a given pricing distortion function gg, assume that qgq\_{g} is optimal for ([9](https://arxiv.org/html/2602.16401v1#S3.E9 "Equation 9 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")), and we aim to show that Ig​(x)=x−qg​(FX​(x))I\_{g}(x)=x-q\_{g}\left(F\_{X}(x)\right) is optimal for ([6](https://arxiv.org/html/2602.16401v1#S3.E6 "Equation 6 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). Consider any feasible solution II to ([6](https://arxiv.org/html/2602.16401v1#S3.E6 "Equation 6 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")), and let q​(t)q(t) be the quantile function of the associated retention R​(X)R(X), for all t∈[0,1]t\in[0,1]. We saw in ([8](https://arxiv.org/html/2602.16401v1#S3.E8 "Equation 8 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρP​o​l​(I,g)\displaystyle\rho^{Pol}(I,g) | =ρP​o​l​(R​(X))+Πg​(I​(X))\displaystyle=\rho^{Pol}(R(X))+\Pi\_{g}(I(X)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01q′​(t)​[T​(1−t)−g​(1−t)]​dt+∫01(FX−1)′​(t)​g​(1−t)​dt.\displaystyle=\int\_{0}^{1}q^{\prime}(t)\,\left[T(1-t)-g(1-t)\right]\,\mathrm{d}t+\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,g(1-t)\,\mathrm{d}t. |  |

Since qgq\_{g} is optimal for the problem given in ([9](https://arxiv.org/html/2602.16401v1#S3.E9 "Equation 9 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")), then the following inequality holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρP​o​l​(I,g)\displaystyle\rho^{Pol}(I,g) | ≥∫01qg′​(t)​[T​(1−t)−g​(1−t)]​dt+∫01(FX−1)′​(t)​g​(1−t)​dt,\displaystyle\geq\int\_{0}^{1}q\_{g}^{\prime}(t)\,\left[T(1-t)-g(1-t)\right]\,\mathrm{d}t+\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,g(1-t)\,\mathrm{d}t, |  |

where, by Remark [3.3](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem3 "Remark 3.3. ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),

|  |  |  |
| --- | --- | --- |
|  | qg​(t)=FX−1​(t)−FIg​(X)−1​(t),∀t∈[0,1].q\_{g}(t)=F\_{X}^{-1}(t)-F^{-1}\_{I\_{g}(X)}(t),\ \forall t\in[0,1]. |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρP​o​l​(I,g)\displaystyle\rho^{Pol}(I,g) | ≥∫01[FX−1​(t)−FIg​(X)−1​(t)]′​[T​(1−t)−g​(1−t)]​dt+∫01(FX−1)′​(t)​g​(1−t)​dt\displaystyle\geq\int\_{0}^{1}\big[F\_{X}^{-1}(t)-F^{-1}\_{I\_{g}(X)}(t)\big]^{\prime}\left[T(1-t)-g(1-t)\right]\,\mathrm{d}t+\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,g(1-t)\,\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01(FX−1)′​(t)​T​(1−t)​dt−∫01(FIg​(X)−1)′​(t)​T​(1−t)​dt+πg​(Ig​(X))\displaystyle=\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,T(1-t)\,\mathrm{d}t-\int\_{0}^{1}\left(F^{-1}\_{I\_{g}(X)}\right)^{\prime}(t)\,T(1-t)\,\mathrm{d}t+\pi\_{g}\left(I\_{g}(X)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫(X−Ig​(X)+Πg​(Ig​(X)))​dT∘ℙ=ρP​o​l​(Ig,g),\displaystyle=\int\left(X-I\_{g}(X)+\Pi\_{g}\left(I\_{g}(X)\right)\right)\mathrm{d}T\circ\mathbb{P}=\rho^{Pol}\left(I\_{g},g\right), |  |

which implies that the indemnity function Ig​(x)=x−qg​(FX​(x))I\_{g}(x)=x-q\_{g}\big(F\_{X}(x)\big) is optimal for the policyholder’s problem ([6](https://arxiv.org/html/2602.16401v1#S3.E6 "Equation 6 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")).

Conversely, we assume that the indemnity function IgI\_{g}, given by Ig​(x)=x−qg​(FX​(x))I\_{g}(x)=x-q\_{g}\big(F\_{X}(x)\big) is optimal for the policyholder’s problem ([6](https://arxiv.org/html/2602.16401v1#S3.E6 "Equation 6 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")), and we aim to show that the quantile qgq\_{g} is optimal for ([9](https://arxiv.org/html/2602.16401v1#S3.E9 "Equation 9 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). Consider any feasible solution qq to ([9](https://arxiv.org/html/2602.16401v1#S3.E9 "Equation 9 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) and let I​(x)=x−q​(FX​(x))I(x)=x-q(F\_{X}(x)). We have that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρP​o​l​(q,g)\displaystyle\rho^{Pol}\left(q,g\right) | =∫01q′​(t)​[T​(1−t)−g​(1−t)]​dt+∫01(FX−1)′​(t)​g​(1−t)​dt\displaystyle=\int\_{0}^{1}q^{\prime}(t)\,\left[T(1-t)-g(1-t)\right]\,\mathrm{d}t+\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,g(1-t)\,\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫(X−I​(X)+Πg​(I​(X)))​dT∘ℙ.\displaystyle=\int\left(X-I(X)+\Pi\_{g}\left(I(X)\right)\right)\,\mathrm{d}T\circ\mathbb{P}. |  |

Since IgI\_{g} is optimal for ([6](https://arxiv.org/html/2602.16401v1#S3.E6 "Equation 6 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")), then the following inequality holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρP​o​l​(q,g)\displaystyle\rho^{Pol}\left(q,g\right) | ≥∫(X−Ig​(X)+Πg​(Ig​(X)))​dT∘ℙ\displaystyle\geq\int\left(X-I\_{g}(X)+\Pi\_{g}\left(I\_{g}(X)\right)\right)\,\mathrm{d}T\circ\mathbb{P} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01qg′​(t)​[T​(1−t)−g​(1−t)]​dt+∫01(FX−1)′​(t)​g​(1−t)​dt=ρP​o​l​(qg,g),\displaystyle=\int\_{0}^{1}q\_{g}^{\prime}(t)\,\left[T(1-t)-g(1-t)\right]\,\mathrm{d}t+\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,g(1-t)\,\mathrm{d}t=\rho^{Pol}\left(q\_{g},g\right), |  |

which implies the optimality of qgq\_{g} for ([9](https://arxiv.org/html/2602.16401v1#S3.E9 "Equation 9 ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). ∎

### A.2. Proof of Lemma [3.5](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")

First, note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρP​o​l​(q,g)\displaystyle\rho^{Pol}(q,g) | =Πg​(q)+∫01q′​(t)​T​(1−t)​dt\displaystyle=\Pi\_{g}(q)+\int\_{0}^{1}q^{\prime}(t)\,T(1-t)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01((FX−1)′​(t)−q′​(t))​g​(1−t)​dt+∫01q′​(t)​T​(1−t)​dt\displaystyle=\int\_{0}^{1}\left(\left(F\_{X}^{-1}\right)^{\prime}(t)-q^{\prime}(t)\right)\,g(1-t)\,\mathrm{d}t+\int\_{0}^{1}q^{\prime}(t)\,T(1-t)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01(FX−1)′​(t)​g​(1−t)​dt+∫01q′​(t)​(T​(1−t)−g​(1−t))​dt.\displaystyle=\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,g(1-t)\,\mathrm{d}t+\int\_{0}^{1}q^{\prime}(t)\,\left(T(1-t)-g(1-t)\right)\mathrm{d}t. |  |

The first term in the final line is independent of qq, so minimizing the risk measure ρP​o​l​(q,g)\rho^{Pol}(q,g) over q∈𝒬Lq\in\mathcal{Q}\_{L} is equivalent to solving:

|  |  |  |
| --- | --- | --- |
|  | minq∈𝒬L​∫01q′​(t)​(T​(1−t)−g​(1−t))​dt.\min\limits\_{q\in\mathcal{Q}\_{L}}\int\_{0}^{1}q^{\prime}(t)\left(T(1-t)-g(1-t)\right)\,\mathrm{d}t. |  |

By the Marginal Indemnity Function Approach given in Assa ([2015](https://arxiv.org/html/2602.16401v1#bib.bib17 "On Optimal Reinsurance Policy with Distortion Risk Measures and Premiums")), the optimal quantile function qgq\_{g} must satisfy:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (qg)′​(t)={0,g​(1−t)<T​(1−t),∈[0,(FX−1)′​(t)],g​(1−t)=T​(1−t),(FX−1)′​(t),g​(1−t)>T​(1−t).\left(q\_{g}\right)^{\prime}(t)=\left\{\begin{array}[c]{ll}0,&g(1-t)<T(1-t),\vskip 5.69046pt\\ \in\left[0,\left(F\_{X}^{-1}\right)^{\prime}(t)\right],&g(1-t)=T(1-t),\vskip 5.69046pt\\ \left(F\_{X}^{-1}\right)^{\prime}(t),&g(1-t)>T(1-t).\end{array}\right. |  | (18) |

∎

### A.3. Proof of Theorem [3.9](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem9 "Theorem 3.9. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")

First, note that the insurer’s profit can be expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VI​n​(qg,g)=∫01[(FX−1)′​(t)−qg′​(t)]​g​(1−t)​dt−∫01[FX−1​(t)−qg​(t)]​dt=∫01[(FX−1)′​(t)−qg′​(t)]​g​(1−t)​dt−∫01[(FX−1)′​(t)−qg′​(t)]​(1−t)​dt=∫01[(FX−1)′​(t)−qg′​(t)]​h​(t)​𝑑t,\begin{split}V^{In}\left(q\_{{g}},g\right)&=\int\_{0}^{1}\left[\left(F\_{X}^{-1}\right)^{\prime}(t)-q\_{{g}}^{\prime}(t)\right]\,g(1-t)\,\mathrm{d}t-\int\_{0}^{1}\left[F\_{X}^{-1}(t)-q\_{{g}}(t)\right]\,\mathrm{d}t\\ &=\int\_{0}^{1}\left[\left(F\_{X}^{-1}\right)^{\prime}(t)-q\_{{g}}^{\prime}(t)\right]\,g(1-t)\,\mathrm{d}t-\int\_{0}^{1}\left[\left(F\_{X}^{-1}\right)^{\prime}(t)-q\_{{g}}^{\prime}(t)\right](1-t)\,\mathrm{d}t\\ &=\int\_{0}^{1}\left[\left(F\_{X}^{-1}\right)^{\prime}(t)-q\_{{g}}^{\prime}(t)\right]h(t)\ dt,\end{split} |  | (19) |

where h​(t):=t−1+g​(1−t)h(t):=t-1+g(1-t), for all t∈[0,1]t\in[0,1]. Consider now the following three sets:

|  |  |  |
| --- | --- | --- |
|  | 𝒜1={t∈[0,1]:h​(t)<t−T~​(t)},𝒜2={t∈[0,1]:h​(t)=t−T~​(t)},and​𝒜3={t∈[0,1]:h​(t)>t−T~​(t)}.\mathcal{A}\_{1}=\left\{t\in[0,1]:h(t)<t-\widetilde{T}(t)\right\},\ \mathcal{A}\_{2}=\left\{t\in[0,1]:h(t)=t-\widetilde{T}(t)\right\},\ \hbox{and}\ \mathcal{A}\_{3}=\left\{t\in[0,1]:h(t)>t-\widetilde{T}(t)\right\}. |  |

where T~\widetilde{T} is the conjugate of the distortion function TT. Then it follows from Lemma [3.5](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (qh)′​(t)={0,t∈𝒜1,ϕh​(t)∈[0,(FX−1)′​(t)],t∈𝒜2,(FX−1)′​(t),t∈𝒜3.\big(q\_{h}\big)^{\prime}(t)=\left\{\begin{array}[c]{ll}0,&t\in\mathcal{A}\_{1},\\ \phi\_{h}(t)\in\left[0,\left(F\_{X}^{-1}\right)^{\prime}(t)\right],&t\in\mathcal{A}\_{2},\\ \left(F\_{X}^{-1}\right)^{\prime}(t),&t\in\mathcal{A}\_{3}.\end{array}\right. |  | (20) |

The insurer’s profit in ([19](https://arxiv.org/html/2602.16401v1#A1.E19 "Equation 19 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) can then be rewritten as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | VI​n​(qh,h)\displaystyle V^{In}\left(q\_{{h}},h\right) | =∫01(FX−1)′​(t)​h​(t)​ 1𝒜1​(t)​dt+∫01[(FX−1)′​(t)−ϕh​(t)]​h​(t)​ 1𝒜2​(t)​dt.\displaystyle=\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,h(t)\,\mathbbm{1}\_{\mathcal{A}\_{1}}(t)\,\mathrm{d}t+\int\_{0}^{1}\left[\left(F\_{X}^{-1}\right)^{\prime}(t)-\phi\_{h}(t)\right]\,h(t)\,\mathbbm{1}\_{\mathcal{A}\_{2}}(t)\,\mathrm{d}t. |  | (21) |

Note that on 𝒜2\mathcal{A}\_{2}, the optimal retention function allows for some flexibility as long as qh∈𝒬Lq\_{h}\in\mathcal{Q}\_{L}. The arbitrary choice of ϕh​(t)\phi\_{h}(t) does not affect the policyholder’s risk exposure level, but it does impact the insurer’s profit. To maximize the insurer’s profit, we must take a further step to determine the value of ϕh\phi\_{h} when t∈𝒜2t\in\mathcal{A}\_{2}. This is achieved by analyzing the profit over a finer partition {ℬi}i=13\left\{\mathcal{B}\_{i}\right\}\_{i=1}^{3} such that:

|  |  |  |
| --- | --- | --- |
|  | ℬ1={t∈[0,1]:T~​(t)<t},ℬ2={t∈[0,1]:T~​(t)=t},andℬ3={t∈[0,1]:T~​(t)>t}.\mathcal{B}\_{1}=\{t\in[0,1]:\ \widetilde{T}(t)<t\},\ \ \mathcal{B}\_{2}=\{t\in[0,1]:\ \widetilde{T}(t)=t\},\ \ \hbox{and}\ \ \mathcal{B}\_{3}=\{t\in[0,1]:\ \widetilde{T}(t)>t\}. |  |

The insurer’s profit in ([21](https://arxiv.org/html/2602.16401v1#A1.E21 "Equation 21 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VI​n​(qh,h)\displaystyle V^{In}\left(q\_{{h}},h\right) | =∫01(FX−1)′​(t)​h​(t)​ 1𝒜1​(t)​dt+∑i=13∫01[(FX−1)′​(t)−ϕh​(t)]​h​(t)​ 1𝒜2​(t)⋅𝟙ℬi​(t)​dt\displaystyle=\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,h(t)\,\mathbbm{1}\_{\mathcal{A}\_{1}}(t)\,\mathrm{d}t+\sum\_{i=1}^{3}\int\_{0}^{1}\left[\left(F\_{X}^{-1}\right)^{\prime}(t)-\phi\_{h}(t)\right]h(t)\,\mathbbm{1}\_{\mathcal{A}\_{2}}(t)\cdot\mathbbm{1}\_{\mathcal{B}\_{i}}(t)\ \mathrm{d}t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫01(FX−1)′​(t)​h​(t)​ 1𝒜1​(t)​dt+∑i=13∫01[(FX−1)′​(t)−ϕh​(t)]​h​(t)​ 1𝒜2∩ℬi​(t)​dt.\displaystyle=\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,h(t)\,\mathbbm{1}\_{\mathcal{A}\_{1}}(t)\,\mathrm{d}t+\sum\_{i=1}^{3}\int\_{0}^{1}\left[\left(F\_{X}^{-1}\right)^{\prime}(t)-\phi\_{h}(t)\right]h(t)\,\mathbbm{1}\_{\mathcal{A}\_{2}\cap\mathcal{B}\_{i}}(t)\ \mathrm{d}t. |  | (22) |

We consider the following three cases:

1. (1)

   On 𝒜2∩ℬ1\mathcal{A}\_{2}\cap\mathcal{B}\_{1}, h​(t)=t−T~​(t)>0h(t)=t-\widetilde{T}(t)>0. Thus, the insurer’s profit in ([A.3](https://arxiv.org/html/2602.16401v1#A1.Ex56 "A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) is decreasing in ϕh​(t)\phi\_{h}(t), and it is optimal to set ϕh​(t)=0\phi\_{h}(t)=0.
2. (2)

   On 𝒜2∩ℬ2\mathcal{A}\_{2}\cap\mathcal{B}\_{2}, h​(t)=t−T~​(t)=0h(t)=t-\widetilde{T}(t)=0. The profit contribution is always zero regardless of the value of ϕh​(t)\phi\_{h}(t). Thus, ϕh​(t)\phi\_{h}(t) can take any value in [0,(FX−1)′​(t)]\left[0,\left(F\_{X}^{-1}\right)^{\prime}(t)\right] without affecting the insurer’s profit.
3. (3)

   On 𝒜2∩ℬ3\mathcal{A}\_{2}\cap\mathcal{B}\_{3}, h​(t)=t−T~​(t)<0h(t)=t-\widetilde{T}(t)<0. The insurer’s profit is increasing in ϕh​(t)\phi\_{h}(t). Thus, it is optimal to set ϕh​(t)=(FX−1)′​(t)\phi\_{h}(t)=\left(F\_{X}^{-1}\right)^{\prime}(t).

Hence, for a given hh, the marginal quantile of the optimal retention can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (qh∗)′​(t)={0,t∈𝒜2∩ℬ1,ϕh​(t)∈[0,(FX−1)′​(t)],t∈𝒜2∩ℬ2,(FX−1)′​(t),t∈𝒜2∩ℬ3.\left(q^{\*}\_{h}\right)^{\prime}(t)=\left\{\begin{array}[c]{ll}0,&t\in\mathcal{A}\_{2}\cap\mathcal{B}\_{1},\vskip 5.69046pt\\ \phi\_{h}(t)\in\left[0,\left(F\_{X}^{-1}\right)^{\prime}(t)\right],&t\in\mathcal{A}\_{2}\cap\mathcal{B}\_{2},\vskip 5.69046pt\\ \left(F\_{X}^{-1}\right)^{\prime}(t),&t\in\mathcal{A}\_{2}\cap\mathcal{B}\_{3}.\vskip 5.69046pt\end{array}\right. |  | (23) |

It then follows from ([20](https://arxiv.org/html/2602.16401v1#A1.E20 "Equation 20 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) and ([23](https://arxiv.org/html/2602.16401v1#A1.E23 "Equation 23 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (qh∗)′​(t)={0,t∈𝒜1∪(𝒜2∩ℬ1),ϕh​(t)∈[0,(FX−1)′​(t)],t∈𝒜2∩ℬ2,(FX−1)′​(t),t∈𝒜3∪(𝒜2∩ℬ3).\left(q^{\*}\_{h}\right)^{\prime}(t)=\left\{\begin{array}[c]{ll}0,&t\in\mathcal{A}\_{1}\cup\left(\mathcal{A}\_{2}\cap\mathcal{B}\_{1}\right),\vskip 5.69046pt\\ \phi\_{h}(t)\in\left[0,\left(F\_{X}^{-1}\right)^{\prime}(t)\right],&t\in\mathcal{A}\_{2}\cap\mathcal{B}\_{2},\vskip 5.69046pt\\ \left(F\_{X}^{-1}\right)^{\prime}(t),&t\in\mathcal{A}\_{3}\cup\left(\mathcal{A}\_{2}\cap\mathcal{B}\_{3}\right).\vskip 5.69046pt\end{array}\right. |  | (24) |

Using ([24](https://arxiv.org/html/2602.16401v1#A1.E24 "Equation 24 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) and the fact that h​(t)=0h(t)=0 on 𝒜2∩ℬ2\mathcal{A}\_{2}\cap\mathcal{B}\_{2}, the insurer’s profit in ([A.3](https://arxiv.org/html/2602.16401v1#A1.Ex56 "A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) reduces to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VI​n​(qh∗,h)\displaystyle V^{In}\left(q^{\*}\_{h},h\right) | =∫01(FX−1)′​(t)​h​(t)​[𝟙𝒜1​(t)+𝟙𝒜2∩ℬ1​(t)]​dt\displaystyle=\int\_{0}^{1}(F\_{X}^{-1})^{\prime}(t)\,h(t)\bigl[\mathbbm{1}\_{\mathcal{A}\_{1}}(t)+\mathbbm{1}\_{\mathcal{A}\_{2}\cap\mathcal{B}\_{1}}(t)\bigr]\ \mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01(FX−1)′​(t)​h​(t)​ 1𝒜1∪(𝒜2∩ℬ1)​(t)​dt,since 𝒜1 and 𝒜2 are disjoint.\displaystyle=\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,h(t)\ \mathbbm{1}\_{\mathcal{A}\_{1}\cup\big(\mathcal{A}\_{2}\cap\mathcal{B}\_{1}\big)}(t)\ \mathrm{d}t,\ \text{since $\mathcal{A}\_{1}$ and $\mathcal{A}\_{2}$ are disjoint.} |  |

Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜1∪(𝒜2∩ℬ1)\displaystyle\mathcal{A}\_{1}\cup\big(\mathcal{A}\_{2}\cap\mathcal{B}\_{1}\big) | =(𝒜1∪𝒜2)∩(𝒜1∪ℬ1).\displaystyle=\big(\mathcal{A}\_{1}\cup\mathcal{A}\_{2}\big)\ \cap\ \big(\mathcal{A}\_{1}\cup\mathcal{B}\_{1}\big). |  |

Since {ℬi}i=13\{\mathcal{B}\_{i}\}\_{i=1}^{3} forms a partition of [0,1][0,1], we have:

|  |  |  |
| --- | --- | --- |
|  | 𝒜1∪ℬ1=ℬ1∪(𝒜1∩(ℬ2∪ℬ3)).\mathcal{A}\_{1}\cup\mathcal{B}\_{1}=\mathcal{B}\_{1}\cup\left(\mathcal{A}\_{1}\cap(\mathcal{B}\_{2}\cup\mathcal{B}\_{3})\right). |  |

Combining the above identities yields:

|  |  |  |
| --- | --- | --- |
|  | 𝒜1∪(𝒜2∩ℬ1)=[(𝒜1∪𝒜2)∩ℬ1]∪[𝒜1∩(ℬ2∪ℬ3)],\mathcal{A}\_{1}\cup(\mathcal{A}\_{2}\cap\mathcal{B}\_{1})=\left[(\mathcal{A}\_{1}\cup\mathcal{A}\_{2})\cap\mathcal{B}\_{1}\right]\cup\left[\mathcal{A}\_{1}\cap(\mathcal{B}\_{2}\cup\mathcal{B}\_{3})\right], |  |

which is a union of disjoint sets. Therefore,

|  |  |  |
| --- | --- | --- |
|  | VI​n​(qh∗,h)=∫01(FX−1)′​(t)​h​(t)​[𝟏(𝒜1∪𝒜2)∩ℬ1​(t)+𝟏𝒜1∩(ℬ2∪ℬ3)​(t)]​dt.V^{In}(q\_{h}^{\*},h)=\int\_{0}^{1}(F\_{X}^{-1})^{\prime}(t)\,h(t)\left[\mathbf{1}\_{(\mathcal{A}\_{1}\cup\mathcal{A}\_{2})\cap\mathcal{B}\_{1}}(t)+\mathbf{1}\_{\mathcal{A}\_{1}\cap(\mathcal{B}\_{2}\cup\mathcal{B}\_{3})}(t)\right]\ \mathrm{d}t. |  |

The insurer’s optimization problem given in ([12](https://arxiv.org/html/2602.16401v1#S3.E12 "Equation 12 ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) thus reduces to the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxh⁡{∫01(FX−1)′​(t)​h​(t)​[𝟙{h​(t)≤t−T~​(t)}​𝟙{T~​(t)<t}+𝟙{h​(t)<t−T~​(t)}​𝟙{T~​(t)≥t}]​dt}.\displaystyle\max\limits\_{h}\ \left\{\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,h(t)\left[\mathbbm{1}\_{\{h(t)\leq t-\widetilde{T}(t)\}}\mathbbm{1}\_{\{\widetilde{T}(t)<t\}}+\mathbbm{1}\_{\{h(t)<t-\widetilde{T}(t)\}}\mathbbm{1}\_{\{\widetilde{T}(t)\geq t\}}\right]\mathrm{d}t\right\}. |  | (25) |

Since the integrand depends on hh only through the pointwise value h​(t)h(t), the above problem ([25](https://arxiv.org/html/2602.16401v1#A1.E25 "Equation 25 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) can be solved by maximizing the integrand pointwise. Fix t0∈(0,1)t\_{0}\in(0,1) and consider the auxiliary maximization problem:

|  |  |  |
| --- | --- | --- |
|  | maxy≥0⁡m​(y;t0),\max\_{y\geq 0}\ m(y;t\_{0}), |  |

where the auxiliary function m​(y;t0)m(y;t\_{0}) is given by

|  |  |  |
| --- | --- | --- |
|  | m​(y;t0):=y​[𝟙{y≤t0−T~​(t0)}​𝟙{T~​(t0)<t0}+𝟙{y<t0−T~​(t0)}​𝟙{T~​(t0)≥t0}].m(y;t\_{0}):=y\left[\mathbbm{1}\_{\{y\leq t\_{0}-\widetilde{T}(t\_{0})\}}\mathbbm{1}\_{\{\widetilde{T}(t\_{0})<t\_{0}\}}+\mathbbm{1}\_{\{y<t\_{0}-\widetilde{T}(t\_{0})\}}\mathbbm{1}\_{\{\widetilde{T}(t\_{0})\geq t\_{0}\}}\right]. |  |

For a fixed t0t\_{0}, the function m​(y;t0)m(y;t\_{0}) is piecewise linear in yy. Let yt0∈arg⁡max𝑦​m​(y;t0)y\_{t\_{0}}\in\underset{y}{\operatorname\*{\arg\max}}\,m(y;t\_{0}). The maximum value of m​(y;t0)m(y;t\_{0}) is given by

|  |  |  |
| --- | --- | --- |
|  | m​(yt0;t0)={t0−T~​(t0),T~​(t0)<t0,0,T~​(t0)≥t0,m(y\_{t\_{0}};t\_{0})=\left\{\begin{array}[c]{ll}t\_{0}-\widetilde{T}(t\_{0}),&\widetilde{T}(t\_{0})<t\_{0},\vskip 5.69046pt\\ 0,&\widetilde{T}(t\_{0})\geq t\_{0},\end{array}\right. |  |

and any maximizer yt0y\_{t\_{0}} satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {yt0=t0−T~​(t0), if T~​(t0)<t0,yt0≥t0−T~​(t0), if T~​(t0)≥t0.\begin{cases}y\_{t\_{0}}=t\_{0}-\widetilde{T}(t\_{0}),\ &\text{ if $\widetilde{T}(t\_{0})<t\_{0}$},\\ y\_{t\_{0}}\geq t\_{0}-\widetilde{T}(t\_{0}),\ &\text{ if $\widetilde{T}(t\_{0})\geq t\_{0}$}.\end{cases} |  | (26) |

for any t0∈(0,1)t\_{0}\in(0,1). We now proceed to the characterization of optimal solutions to ([25](https://arxiv.org/html/2602.16401v1#A1.E25 "Equation 25 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) through the following Lemma.

###### Lemma A.1.

A function h∗h^{\*} is optimal to ([25](https://arxiv.org/html/2602.16401v1#A1.E25 "Equation 25 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) if and only if for every t0∈(0,1)t\_{0}\in(0,1), h∗​(t0)=yt0h^{\*}(t\_{0})=y\_{t\_{0}}, where yt0y\_{t\_{0}} satisfies ([26](https://arxiv.org/html/2602.16401v1#A1.E26 "Equation 26 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")).

###### Proof.

Assume that h∗h^{\*} is a solution to ([25](https://arxiv.org/html/2602.16401v1#A1.E25 "Equation 25 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). We show that h∗​(t0)=yt0h^{\*}(t\_{0})=y\_{t\_{0}}, where yt0y\_{t\_{0}} satisfies ([26](https://arxiv.org/html/2602.16401v1#A1.E26 "Equation 26 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). We consider the following two cases.

1. (1)

   If T~​(t0)<t0,\widetilde{T}(t\_{0})<t\_{0}, we aim to show that h∗​(t0)=t0−T~​(t0)h^{\*}(t\_{0})=t\_{0}-\widetilde{T}(t\_{0}) for any t0∈(0,1)t\_{0}\in(0,1). Suppose for the sake of contradiction that

   |  |  |  |
   | --- | --- | --- |
   |  | h∗​(t0)≠t0−T~​(t0).h^{\*}(t\_{0})\neq t\_{0}-\widetilde{T}(t\_{0}). |  |

   Since T~​(t0)<t0\widetilde{T}(t\_{0})<t\_{0} and T~\widetilde{T} is continuous (being differentiable), we can find an arbitrary small ϵ>0\epsilon>0 such that

   |  |  |  |
   | --- | --- | --- |
   |  | T~​(t)<t,when t∈(t0−ϵ,t0+ϵ).\widetilde{T}(t)<t,\ \ \text{when $t\in(t\_{0}-\epsilon,t\_{0}+\epsilon)$}. |  |

   If h∗​(t0)<t0−T~​(t0)h^{\*}(t\_{0})<t\_{0}-\widetilde{T}(t\_{0}), we have m​(h∗​(t0);t0)=h∗​(t0)m(h^{\*}(t\_{0});t\_{0})=h^{\*}(t\_{0}). Then there exists a function h~\widetilde{h} such that:

   |  |  |  |
   | --- | --- | --- |
   |  | h~​(t)={yt>h∗​(t),t∈(t0−ϵ,t0+ϵ),h∗​(t),t∉(t0−ϵ,t0+ϵ),\widetilde{h}(t)=\begin{cases}y\_{t}>h^{\*}(t),&t\in(t\_{0}-\epsilon,t\_{0}+\epsilon),\\ h^{\*}(t),&t\notin(t\_{0}-\epsilon,t\_{0}+\epsilon),\end{cases} |  |

   where yty\_{t} satisfies ([26](https://arxiv.org/html/2602.16401v1#A1.E26 "Equation 26 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")), which implies the following:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | VI​n​(qh~∗,h~)−VI​n​(qh∗∗,h∗)\displaystyle V^{In}\left(q^{\*}\_{\widetilde{h}},\widetilde{h}\right)-V^{In}\left(q^{\*}\_{h^{\*}},h^{\*}\right) | =∫t0−ϵt0+ϵ(FX−1)′​(t)​[m​(yt;t)−m​(h∗​(t);t)]​dt\displaystyle=\int\_{t\_{0}-\epsilon}^{t\_{0}+\epsilon}\left(F\_{X}^{-1}\right)^{\prime}(t)\,\left[m(y\_{t};t)-m\left(h^{\*}(t);t\right)\right]\mathrm{d}t |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =∫t0−ϵt0+ϵ(FX−1)′​(t)​[yt−h∗​(t)]​dt>0,\displaystyle=\int\_{t\_{0}-\epsilon}^{t\_{0}+\epsilon}\left(F\_{X}^{-1}\right)^{\prime}(t)\,\left[y\_{t}-h^{\*}(t)\right]\mathrm{d}t>0, |  |

   since yt>h∗​(t)y\_{t}>h^{\*}(t) when t∈(t0−ϵ,t0+ϵ)t\in(t\_{0}-\epsilon,t\_{0}+\epsilon). Hence, this contradicts the fact that h∗h^{\*} is optimal for problem ([25](https://arxiv.org/html/2602.16401v1#A1.E25 "Equation 25 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")).

   If, in contrast, h∗​(t0)>t0−T~​(t0)h^{\*}(t\_{0})>{t\_{0}}-\widetilde{T}(t\_{0}), then m​(h∗​(t0);t0)=0m\left(h^{\*}(t\_{0});t\_{0}\right)=0. With the same ϵ\epsilon, there exists a function h~\widetilde{h} such that:

   |  |  |  |
   | --- | --- | --- |
   |  | h~​(t)={yt<h∗​(t),t∈(t0−ϵ,t0+ϵ),h∗​(t),t∉(t0−ϵ,t0+ϵ).\widetilde{h}(t)=\begin{cases}y\_{t}<h^{\*}(t),&t\in(t\_{0}-\epsilon,t\_{0}+\epsilon),\\ h^{\*}(t),&t\notin(t\_{0}-\epsilon,t\_{0}+\epsilon).\end{cases} |  |

   Hence,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | VI​n​(qh~∗,h~)−VI​n​(qh∗∗,h∗)\displaystyle V^{In}\left(q^{\*}\_{\widetilde{h}},\widetilde{h}\right)-V^{In}\left(q^{\*}\_{h^{\*}},h^{\*}\right) | =∫t0−ϵt0+ϵ(FX−1)′​(t)​[m​(yt;t)−m​(h∗​(t);t)]​dt\displaystyle=\int\_{t\_{0}-\epsilon}^{t\_{0}+\epsilon}\left(F\_{X}^{-1}\right)^{\prime}(t)\,\left[m(y\_{t};t)-m\left(h^{\*}(t);t\right)\right]\mathrm{d}t |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =∫t0−ϵt0+ϵ(FX−1)′​(t)​(yt−0)​dt>0,\displaystyle=\int\_{t\_{0}-\epsilon}^{t\_{0}+\epsilon}\left(F\_{X}^{-1}\right)^{\prime}(t)\,\left(y\_{t}-0\right)\mathrm{d}t>0, |  |

   which also contradicts the optimality of h∗h^{\*} for ([25](https://arxiv.org/html/2602.16401v1#A1.E25 "Equation 25 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). Therefore, h∗​(t0)=t0−T~​(t0)h^{\*}(t\_{0})=t\_{0}-\widetilde{T}(t\_{0}), for any t0∈(0,1)t\_{0}\in(0,1), when T~​(t0)<t0\widetilde{T}(t\_{0})<t\_{0}.
2. (2)

   If T~​(t0)≥t0,\widetilde{T}(t\_{0})\geq t\_{0}, we aim to show that h∗​(t0)≥t0−T~​(t0)h^{\*}(t\_{0})\geq t\_{0}-\widetilde{T}(t\_{0}), for any t0∈(0,1)t\_{0}\in(0,1). Suppose for the sake of contradiction that

   |  |  |  |
   | --- | --- | --- |
   |  | h∗​(t0)<t0−T~​(t0).h^{\*}(t\_{0})<t\_{0}-\widetilde{T}(t\_{0}). |  |

   Then

   |  |  |  |
   | --- | --- | --- |
   |  | m​(h∗​(t0);t0)=h∗​(t0)<t0−T~​(t0)≤0.m\left(h^{\*}(t\_{0});t\_{0}\right)=h^{\*}(t\_{0})<t\_{0}-\widetilde{T}(t\_{0})\leq 0. |  |

   There exists an arbitrary small ϵ>0\epsilon>0 such that T~​(t)≥t\widetilde{T}(t)\geq t on (t0−ϵ,t0](t\_{0}-\epsilon,t\_{0}] or on [t0,t0+ϵ)[t\_{0},t\_{0}+\epsilon). First, assume that T~​(t)≥t\widetilde{T}(t)\geq t on (t0−ϵ,t0](t\_{0}-\epsilon,t\_{0}]. Then there exists a function h~\widetilde{h} such that:

   |  |  |  |
   | --- | --- | --- |
   |  | h~​(t)={yt>h∗​(t),t∈(t0−ϵ,t0],h∗​(t),t∉(t0−ϵ,t0].\widetilde{h}(t)=\begin{cases}y\_{t}>h^{\*}(t),&t\in(t\_{0}-\epsilon,t\_{0}],\\ h^{\*}(t),&t\notin(t\_{0}-\epsilon,t\_{0}].\end{cases} |  |

   Therefore,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | VI​n​(qh~∗,h~)−VI​n​(qh∗∗,h∗)\displaystyle V^{In}\left(q^{\*}\_{\widetilde{h}},\widetilde{h}\right)-V^{In}\left(q^{\*}\_{h^{\*}},h^{\*}\right) | =∫t0−ϵt0(FX−1)′​(t)​[m​(yt;t)−m​(h∗​(t);t)]​dt\displaystyle=\int\_{t\_{0}-\epsilon}^{t\_{0}}\left(F\_{X}^{-1}\right)^{\prime}(t)\,\left[m(y\_{t};t)-m\left(h^{\*}(t);t\right)\right]\mathrm{d}t |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =∫t0−ϵt0(FX−1)′​(t)​[0−m​(h∗​(t);t)]​dt>0,\displaystyle=\int\_{t\_{0}-\epsilon}^{t\_{0}}\left(F\_{X}^{-1}\right)^{\prime}(t)\,\left[0-m\left(h^{\*}(t);t\right)\right]\mathrm{d}t>0, |  |

   since m​(h∗​(t);t)<0m\left(h^{\*}(t);t\right)<0 when t∈(t0−ϵ,t0]t\in(t\_{0}-\epsilon,t\_{0}], which leads to a contradiction. Hence,

   |  |  |  |
   | --- | --- | --- |
   |  | h∗​(t0)≥t0−T~​(t0).h^{\*}(t\_{0})\geq t\_{0}-\widetilde{T}(t\_{0}). |  |

   Moreover, we can derive a similar result if T~​(t)≥t\widetilde{T}(t)\geq t on [t0,t0+ϵ)[t\_{0},t\_{0}+\epsilon). In sum, for any t0∈[0,1]t\_{0}\in[0,1], we obtain:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | {h∗​(t0)=t0−T~​(t0), if​T~​(t0)<t0,h∗​(t0)≥t0−T~​(t0), if​T~​(t0)≥t0.\begin{cases}h^{\*}(t\_{0})=t\_{0}-\widetilde{T}(t\_{0}),&\text{ if}\ \widetilde{T}(t\_{0})<t\_{0},\vskip 5.69046pt\\ h^{\*}(t\_{0})\geq t\_{0}-\widetilde{T}(t\_{0}),&\text{ if}\ \widetilde{T}(t\_{0})\geq t\_{0}.\vskip 5.69046pt\end{cases} |  | (27) |

Conversely, assume that h∗h^{\*} satisfies ([27](https://arxiv.org/html/2602.16401v1#A1.E27 "Equation 27 ‣ Item 2 ‣ Proof. ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). We show that h∗h^{\*} is optimal for ([25](https://arxiv.org/html/2602.16401v1#A1.E25 "Equation 25 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). We first note that the insurer’s expected profit under (qh∗∗,h∗)(q^{\*}\_{h^{\*}},h^{\*}) is given by

|  |  |  |
| --- | --- | --- |
|  | VI​n​(qh∗∗,h∗)=∫01(FX−1)′​(t)​(t−T~​(t))​𝟙{T~​(t)<t}​dt.V^{In}\left(q^{\*}\_{h^{\*}},h^{\*}\right)=\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,(t-\widetilde{T}(t))\mathbbm{1}\_{\{\widetilde{T}(t)<t\}}\,\mathrm{d}t. |  |

For any other feasible solution hh, we compare the insurer’s expected profit under h∗h^{\*} and hh. Specifically, from the structure of ([25](https://arxiv.org/html/2602.16401v1#A1.E25 "Equation 25 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")), we have:

|  |  |  |
| --- | --- | --- |
|  | VI​n​(qh∗∗,h∗)−VI​n​(qh∗,h)\displaystyle V^{In}\left(q^{\*}\_{h^{\*}},h^{\*}\right)-V^{In}\left(q^{\*}\_{h},h\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫01(FX−1)′​(t)​(t−T~​(t))​𝟙{T~​(t)<t}​dt\displaystyle\quad=\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,(t-\widetilde{T}(t))\mathbbm{1}\_{\{\widetilde{T}(t)<t\}}\mathrm{d}t |  |
|  |  |  |
| --- | --- | --- |
|  | −∫01(FX−1)′​(t)​h​(t)​[𝟙{h​(t)≤t−T~​(t)}​𝟙{T~​(t)<t}​(t)+𝟙{h​(t)<t−T~​(t)}​𝟙{T~​(t)=t}​(t)+𝟙{h​(t)<t−T~​(t)}​𝟙{T~​(t)>t}​(t)]​dt.\displaystyle\qquad-\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,h(t)\bigg[\mathbbm{1}\_{\{h(t)\leq t-\widetilde{T}(t)\}}\mathbbm{1}\_{\{\widetilde{T}(t)<t\}}(t)+\mathbbm{1}\_{\{h(t)<t-\widetilde{T}(t)\}}\mathbbm{1}\_{\{\widetilde{T}(t)=t\}}(t)+\mathbbm{1}\_{\{h(t)<t-\widetilde{T}(t)\}}\mathbbm{1}\_{\{\widetilde{T}(t)>t\}}(t)\bigg]\mathrm{d}t. |  |

That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | VI​n​(qh∗∗,h∗)−VI​n​(qh∗,h)\displaystyle V^{In}\left(q^{\*}\_{h^{\*}},h^{\*}\right)-V^{In}\left(q^{\*}\_{h},h\right) | =∫01(FX−1)′​(t)​[t−T~​(t)−h​(t)​𝟙{h(t)≤t−T~(t))}]​𝟙{T~​(t)<t}​dt\displaystyle=\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,\left[t-\widetilde{T}(t)-h(t)\mathbbm{1}\_{\{h(t)\leq t-\widetilde{T}(t))\}}\right]\mathbbm{1}\_{\{\widetilde{T}(t)<t\}}\mathrm{d}t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −∫01(FX−1)′​(t)​h​(t)​[𝟙{h​(t)<t−T~​(t)}​𝟙{T~​(t)=t}+𝟙{h​(t)<t−T~​(t)}​𝟙{T~​(t)>t}]​dt.\displaystyle\qquad-\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,h(t)\left[\mathbbm{1}\_{\{h(t)<t-\widetilde{T}(t)\}}\mathbbm{1}\_{\{\widetilde{T}(t)=t\}}+\mathbbm{1}\_{\{h(t)<t-\widetilde{T}(t)\}}\mathbbm{1}\_{\{\widetilde{T}(t)>t\}}\right]\mathrm{d}t. |  | (28) |

Looking at the first term of ([A.3](https://arxiv.org/html/2602.16401v1#A1.Ex84 "Proof. ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")), we know that

|  |  |  |  |
| --- | --- | --- | --- |
|  | t−T~​(t)−h​(t)​𝟙{h​(t)≤t−T~​(t)}\displaystyle t-\widetilde{T}(t)-h(t)\mathbbm{1}\_{\{h(t)\leq t-\widetilde{T}(t)\}} | ={t−T~​(t),h​(t)>t−T~​(t)t−T~​(t)−h​(t),h​(t)≤t−T~​(t),\displaystyle=\left\{\begin{array}[c]{ll}t-\widetilde{T}(t),&h(t)>t-\widetilde{T}(t)\vskip 5.69046pt\\ t-\widetilde{T}(t)-h(t),&h(t)\leq t-\widetilde{T}(t),\end{array}\right. |  |

which is always nonnegative. For the second term,

|  |  |  |
| --- | --- | --- |
|  | −h​(t)​𝟙{h​(t)<t−T~​(t)}​{=h​(t)​𝟙{h​(t)<0}≥0,if ​T~​(t)=t,≥0,if ​T~​(t)>t.-h(t)\mathbbm{1}\_{\{h(t)<t-\widetilde{T}(t)\}}\ \begin{cases}=h(t)\mathbbm{1}\_{\{h(t)<0\}}\geq 0,&\text{if }\widetilde{T}(t)=t,\\ \geq 0,&\text{if }\widetilde{T}(t)>t.\end{cases} |  |

Thus, both terms of ([A.3](https://arxiv.org/html/2602.16401v1#A1.Ex84 "Proof. ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) are nonnegative, for all t∈[0,1]t\in[0,1], implying that the integrand is pointwise nonnegative. Therefore, the difference in profit is nonnegative, i.e.

|  |  |  |
| --- | --- | --- |
|  | VI​n​(qh∗∗,h∗)≥VI​n​(qh∗,h).V^{In}\left(q^{\*}\_{h^{\*}},h^{\*}\right)\geq V^{In}\left(q^{\*}\_{h},h\right). |  |

Hence, h∗h^{\*} maximizes the insurer’s profit functional, thereby establishing sufficiency.
∎

Moreover, when h∗h^{\*} satisfies ([27](https://arxiv.org/html/2602.16401v1#A1.E27 "Equation 27 ‣ Item 2 ‣ Proof. ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")), we can characterize the structure of the critical sets 𝒜1∪(𝒜2∩ℬ1)\mathcal{A}\_{1}\cup(\mathcal{A}\_{2}\cap\mathcal{B}\_{1}), 𝒜2∩ℬ2\mathcal{A}\_{2}\cap\mathcal{B}\_{2}, and 𝒜3∪(𝒜2∩ℬ3)\mathcal{A}\_{3}\cup(\mathcal{A}\_{2}\cap\mathcal{B}\_{3}) that define qh∗∗q^{\*}\_{h^{\*}} in ([24](https://arxiv.org/html/2602.16401v1#A1.E24 "Equation 24 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). First, if h∗h^{\*} satisfies ([27](https://arxiv.org/html/2602.16401v1#A1.E27 "Equation 27 ‣ Item 2 ‣ Proof. ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")), we can clearly see that 𝒜1=∅\mathcal{A}\_{1}=\varnothing. Hence,

|  |  |  |
| --- | --- | --- |
|  | 𝒜1∪(𝒜2∩ℬ1)={t∈[0,1]:t−T~​(t)>0}.\mathcal{A}\_{1}\cup\left(\mathcal{A}\_{2}\cap\mathcal{B}\_{1}\right)=\{t\in[0,1]:t-\widetilde{T}(t)>0\}. |  |

Moreover,

|  |  |  |
| --- | --- | --- |
|  | 𝒜2∩ℬ2={t∈[0,1]:h∗​(t)=t−T~​(t)=0},\mathcal{A}\_{2}\cap\mathcal{B}\_{2}=\{t\in[0,1]:h^{\*}(t)=t-\widetilde{T}(t)=0\}, |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜3∪(𝒜2∩ℬ3)\displaystyle\mathcal{A}\_{3}\cup\left(\mathcal{A}\_{2}\cap\mathcal{B}\_{3}\right) | ={t∈[0,1]:h∗​(t)>t−T~​(t)}∪{t∈[0,1]:h∗​(t)=t−T~​(t)<0}.\displaystyle=\{t\in[0,1]:h^{\*}(t)>t-\widetilde{T}(t)\}\ \cup\ \{t\in[0,1]:h^{\*}(t)=t-\widetilde{T}(t)<0\}. |  |

Additionally, since {ℬi}i=13\{\mathcal{B}\_{i}\}\_{i=1}^{3} forms a partition over (0,1)(0,1), it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜3\displaystyle\mathcal{A}\_{3} | =(𝒜3∩ℬ1)∪(𝒜3∩ℬ2)∪(𝒜3∩ℬ3)\displaystyle=(\mathcal{A}\_{3}\cap\mathcal{B}\_{1})\ \cup\ (\mathcal{A}\_{3}\cap\mathcal{B}\_{2})\ \cup\ (\mathcal{A}\_{3}\cap\mathcal{B}\_{3}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ={t∈[0,1]:h∗​(t)>t−T~​(t),t>T~​(t)}\displaystyle=\{t\in[0,1]:h^{\*}(t)>t-\widetilde{T}(t),t>\widetilde{T}(t)\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∪{t∈[0,1]:h∗​(t)>t−T~​(t)=0}\displaystyle\qquad\qquad\cup\ \{t\in[0,1]:h^{\*}(t)>t-\widetilde{T}(t)=0\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∪{t∈[0,1]:h​(t)∗>t−T~​(t),T~​(t)>t}.\displaystyle\qquad\qquad\qquad\cup\{t\in[0,1]:h(t)^{\*}>t-\widetilde{T}(t),\widetilde{T}(t)>t\}. |  |

The first intersection must be empty since h∗h^{\*} satisfies ([27](https://arxiv.org/html/2602.16401v1#A1.E27 "Equation 27 ‣ Item 2 ‣ Proof. ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")):

|  |  |  |
| --- | --- | --- |
|  | 𝒜3∩ℬ1=∅.\mathcal{A}\_{3}\cap\mathcal{B}\_{1}=\varnothing. |  |

Hence, the union of 𝒜3\mathcal{A}\_{3} with 𝒜2∩ℬ3\mathcal{A}\_{2}\cap\mathcal{B}\_{3} reduces to the following:

|  |  |  |
| --- | --- | --- |
|  | 𝒜3∪(𝒜2∩ℬ3)={t∈[0,1]:h∗​(t)>t−T~​(t)=0}∪{t∈[0,1]:T~​(t)>t}.\mathcal{A}\_{3}\cup\left(\mathcal{A}\_{2}\cap\mathcal{B}\_{3}\right)=\{t\in[0,1]:h^{\*}(t)>t-\widetilde{T}(t)=0\}\ \cup\ \{t\in[0,1]:\widetilde{T}(t)>t\}. |  |

Thus, the function qh∗∗q^{\*}\_{h^{\*}} given in ([24](https://arxiv.org/html/2602.16401v1#A1.E24 "Equation 24 ‣ A.3. Proof of Theorem 3.9 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")) can be written as follows:

|  |  |  |
| --- | --- | --- |
|  | (qh∗∗)′​(t)={0,T~​(t)<t,ϕh​(t)∈[0,(FX−1)′​(t)],t∈{z;h∗​(z)=z−T~​(z)=0}(FX−1)′​(t),t∈{z;h∗​(z)>z−T~​(z)=0}∪{z;T~​(z)>z}.\left(q^{\*}\_{h^{\*}}\right)^{\prime}(t)=\left\{\begin{array}[c]{ll}0,&\widetilde{T}(t)<t,\vskip 5.69046pt\\ \phi\_{h}(t)\in\left[0,\left(F\_{X}^{-1}\right)^{\prime}(t)\right],&t\in\{z;\ h^{\*}(z)=z-\widetilde{T}(z)=0\}\\ \left(F\_{X}^{-1}\right)^{\prime}(t),&t\in\{z;\ h^{\*}(z)>z-\widetilde{T}(z)=0\}\cup\{z;\ \widetilde{T}(z)>z\}.\end{array}\right. |  |

Since g~∗​(t)=t−h∗​(t)\widetilde{g}^{\*}(t)=t-h^{\*}(t), the optimal h∗h^{\*} leads to the following optimal pricing distortion function g~∗\widetilde{g}^{\*}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | g~∗​(t)={T~​(t),T~​(t)<t,∈[0,T~​(t)],T~​(t)≥t.\widetilde{g}^{\*}(t)=\left\{\begin{array}[c]{ll}\widetilde{T}(t),&\widetilde{T}(t)<t,\vskip 5.69046pt\\ \in\left[0,\widetilde{T}(t)\right],&\widetilde{T}(t)\geq t.\end{array}\right. |  | (29) |

Consequently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | g~∗​(t)={T~​(t),T~​(t)<t,∈[sup{z<t;g~∗​(z)},T~​(t)],T~​(t)≥t.\widetilde{g}^{\*}(t)=\left\{\begin{array}[c]{ll}\widetilde{T}(t),&\widetilde{T}(t)<t,\vskip 8.5359pt\\ \in\left[\,\sup\left\{z<t;\ \widetilde{g}^{\*}(z)\right\},\widetilde{T}(t)\right],&\widetilde{T}(t)\geq t.\end{array}\right. |  | (30) |

We then obtain the optimal retention quantile q∗q^{\*} as a function of the distortion premium function g∗g^{\*}, as follows:

|  |  |  |
| --- | --- | --- |
|  | (qg∗∗)′​(t)={0,T~​(t)<t,ϕg∗​(t)∈[0,(FX−1)′​(t)],t∈{z;g~∗​(z)=T~​(z)=z},(FX−1)′​(t),t∈{z;g~∗​(z)<T~​(z)=z}∪{z;T~​(z)>z}.\left(q^{\*}\_{{g}^{\*}}\right)^{\prime}(t)=\left\{\begin{array}[c]{ll}0,&\widetilde{T}(t)<t,\vskip 5.69046pt\\ \phi\_{g^{\*}}(t)\in\left[0,\left(F\_{X}^{-1}\right)^{\prime}(t)\right],&t\in\{z;\ \widetilde{g}^{\*}(z)=\widetilde{T}(z)=z\},\vskip 5.69046pt\\ \left(F\_{X}^{-1}\right)^{\prime}(t),&t\in\{z;\ \widetilde{g}^{\*}(z)<\widetilde{T}(z)=z\}\cup\{z;\ \widetilde{T}(z)>z\}.\vskip 5.69046pt\end{array}\right. |  |

∎

### A.4. Proof of Theorem [3.11](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem11 "Theorem 3.11. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")

Consider two policyholders whose respective distortion functions T1T\_{1} and T2T\_{2} satisfy T1​(t)≤T2​(t)T\_{1}(t)\leq T\_{2}(t) for all t∈[0,1]t\in[0,1]. Then

|  |  |  |
| --- | --- | --- |
|  | T1​(ℙ​[X>y])≤T2​(ℙ​[X>y]),∀y∈[0,M].T\_{1}(\mathbb{P}[X>y])\leq T\_{2}(\mathbb{P}[X>y]),\quad\forall\,y\in[0,M]. |  |

Let (Ig1∗∗,g1∗)(I\_{g^{\*}\_{1}}^{\*},g\_{1}^{\*}) and (Ig2∗∗,g2∗)(I\_{g^{\*}\_{2}}^{\*},g\_{2}^{\*}) denote the corresponding Stackelberg equilibria, where κ1∗\kappa\_{1}^{\*} and κ2∗\kappa\_{2}^{\*} denote the marginal indemnity functions of the two policyholders, respectively, and satisfy Corollary [3.10](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem10 "Corollary 3.10. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"). Hence, we obtain

|  |  |  |
| --- | --- | --- |
|  | κ1∗​(y)≤κ2∗​(y),for almost every y∈[0,M].\kappa^{\*}\_{1}(y)\leq\kappa^{\*}\_{2}(y),\ \text{for almost every $y\in[0,M]$}. |  |

The above inequality gives

|  |  |  |
| --- | --- | --- |
|  | Ig1∗∗​(x)≤Ig2∗∗​(x),∀x∈[0,M].I\_{g^{\*}\_{1}}^{\*}(x)\leq I\_{g^{\*}\_{2}}^{\*}(x),\ \forall x\in[0,M]. |  |

The insurer’s expected profits for the two policyholders are given by:

|  |  |  |
| --- | --- | --- |
|  | VI​n​(Ig1∗∗,g1∗)=∫01(FX−1)′​(t)​[t−T~1​(t)]​ 1{T~1​(t)<t}​dt and VI​n​(Ig2∗∗,g2∗)=∫01(FX−1)′​(t)​[t−T~2​(t)]​ 1{T~2​(t)<t}​dt,V^{In}(I\_{g^{\*}\_{1}}^{\*},g\_{1}^{\*})=\int\_{0}^{1}\big(F\_{X}^{-1}\big)^{\prime}(t)\,[t-\widetilde{T}\_{1}(t)]\,\mathbbm{1}\_{\{\widetilde{T}\_{1}(t)<t\}}\,\mathrm{d}t\ \ \hbox{ and }\ \ V^{In}(I\_{g^{\*}\_{2}}^{\*},g\_{2}^{\*})=\int\_{0}^{1}\big(F\_{X}^{-1}\big)^{\prime}(t)\,[t-\widetilde{T}\_{2}(t)]\,\mathbbm{1}\_{\{\widetilde{T}\_{2}(t)<t\}}\,\mathrm{d}t, |  |

where T~1\widetilde{T}\_{1} and T~2\widetilde{T}\_{2} denote the conjugates of T1T\_{1} and T2T\_{2}, respectively. Since T1​(t)≤T2​(t)T\_{1}(t)\leq T\_{2}(t) for all t∈[0,1]t\in[0,1], it follows that T~1​(t)≥T~2​(t)\widetilde{T}\_{1}(t)\geq\widetilde{T}\_{2}(t), for all t∈[0,1]t\in[0,1]. Hence,

|  |  |  |
| --- | --- | --- |
|  | t−T~1​(t)≤t−T~2​(t),∀t∈[0,1],t-\widetilde{T}\_{1}(t)\leq t-\widetilde{T}\_{2}(t),\ \forall t\in[0,1], |  |

and,

|  |  |  |
| --- | --- | --- |
|  | {T~1​(t)<t}⊆{T~2​(t)<t}.\{\widetilde{T}\_{1}(t)<t\}\subseteq\{\widetilde{T}\_{2}(t)<t\}. |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | VI​n​(Ig1∗∗,g1∗)\displaystyle V^{In}(I\_{g^{\*}\_{1}}^{\*},g\_{1}^{\*}) | =∫01(FX−1)′​(t)​[t−T~1​(t)]​ 1{T~1​(t)<t}​dt\displaystyle=\int\_{0}^{1}\big(F\_{X}^{-1}\big)^{\prime}(t)\,[t-\widetilde{T}\_{1}(t)]\,\mathbbm{1}\_{\{\widetilde{T}\_{1}(t)<t\}}\,\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫01(FX−1)′​(t)​[t−T~2​(t)]​ 1{T~2​(t)<t}​dt=VI​n​(Ig2∗∗,g2∗).\displaystyle\leq\int\_{0}^{1}\big(F\_{X}^{-1}\big)^{\prime}(t)\,[t-\widetilde{T}\_{2}(t)]\,\mathbbm{1}\_{\{\widetilde{T}\_{2}(t)<t\}}\,\mathrm{d}t=V^{In}(I\_{g^{\*}\_{2}}^{\*},g\_{2}^{\*}). |  |

Hence, the second policyholder is more profitable for the insurer than the first. ∎

### A.5. Proof of Proposition [4.1](https://arxiv.org/html/2602.16401v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")

Let (I∗,π∗)∈ℐL×ℝ(I^{\*},\pi^{\*})\in\mathcal{I}\_{L}\times\mathbb{R} be optimal for the problem given in ([17](https://arxiv.org/html/2602.16401v1#S4.E17 "Equation 17 ‣ Proposition 4.1. ‣ 4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")), and assume for the sake of contradiction that (I∗,π∗)(I^{\*},\pi^{\*}) is not Pareto optimal. Then there exists a contract (I,π)∈ℐL×ℝ(I,\pi)\in\mathcal{I}\_{L}\times\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | ρP​o​l​(I,π)≤ρP​o​l​(I∗,π∗)andVI​n​(I,π)≥VI​n​(I∗,π∗),\rho^{{Pol}}(I,\pi)\leq\rho^{{Pol}}(I^{\*},\pi^{\*})\quad\text{and}\quad V^{{In}}(I,\pi)\geq V^{{In}}(I^{\*},\pi^{\*}), |  |

with at least one strict inequality. Consequently,

|  |  |  |
| --- | --- | --- |
|  | ρP​o​l​(I,π)−VI​n​(I,π)<ρP​o​l​(I∗,π∗)−VI​n​(I∗,π∗),\rho^{{Pol}}(I,\pi)-V^{{In}}(I,\pi)<\rho^{{Pol}}(I^{\*},\pi^{\*})-V^{{In}}(I^{\*},\pi^{\*}), |  |

which contradicts the optimality of (I∗,π∗)(I^{\*},\pi^{\*}) for the problem given in ([17](https://arxiv.org/html/2602.16401v1#S4.E17 "Equation 17 ‣ Proposition 4.1. ‣ 4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). Hence, the contract (I∗,π∗)(I^{\*},\pi^{\*}) is Pareto optimal.

Conversely, suppose that the contract (I∗,π∗)(I^{\*},\pi^{\*}) is Pareto optimal, and assume for the sake of contradiction that (I∗,π∗)(I^{\*},\pi^{\*}) is not optimal for ([17](https://arxiv.org/html/2602.16401v1#S4.E17 "Equation 17 ‣ Proposition 4.1. ‣ 4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). Then there exists a contract (I~,π~)∈ℐL×ℝ(\widetilde{I},\widetilde{\pi})\in\mathcal{I}\_{L}\times\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | ρP​o​l​(I~,π~)−VI​n​(I~,π~)<ρP​o​l​(I∗,π∗)−VI​n​(I∗,π∗).\rho^{{Pol}}(\widetilde{I},\widetilde{\pi})-V^{{In}}(\widetilde{I},\widetilde{\pi})<\rho^{{Pol}}(I^{\*},\pi^{\*})-V^{{In}}(I^{\*},\pi^{\*}). |  |

Let π^:=π~+ρP​o​l​(I∗,π∗)−ρP​o​l​(I~,π~)\hat{\pi}:=\widetilde{\pi}+\rho^{{Pol}}(I^{\*},\pi^{\*})-\rho^{{Pol}}(\widetilde{I},\widetilde{\pi}). Then by translation invariance of ρP​o​l\rho^{Pol}, we have:

|  |  |  |
| --- | --- | --- |
|  | ρP​o​l​(I~,π^)=ρP​o​l​(X−I~​(X))+π^=ρP​o​l​(I∗,π∗).\rho^{{Pol}}(\widetilde{I},\hat{\pi})=\rho^{{Pol}}(X-\widetilde{I}(X))+\hat{\pi}=\rho^{{Pol}}(I^{\*},\pi^{\*}). |  |

Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | VI​n​(I~,π^)−VI​n​(I∗,π∗)\displaystyle V^{{In}}(\widetilde{I},\hat{\pi})-V^{{In}}(I^{\*},\pi^{\*}) | =π^−𝔼​[I~​(X)]−VI​n​(I∗,π∗)\displaystyle=\hat{\pi}-\mathbb{E}[\widetilde{I}(X)]-V^{{In}}(I^{\*},\pi^{\*}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(π~+ρP​o​l​(I∗,π∗)−ρP​o​l​(I~,π~))−𝔼​[I~​(X)]−VI​n​(I∗,π∗)\displaystyle=\left(\widetilde{\pi}+\rho^{{Pol}}(I^{\*},\pi^{\*})-\rho^{{Pol}}(\widetilde{I},\widetilde{\pi})\right)-\mathbb{E}[\widetilde{I}(X)]-V^{{In}}(I^{\*},\pi^{\*}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ρP​o​l​(I∗,π∗)−ρP​o​l​(I~,π~)+VI​n​(I~,π~)−VI​n​(I∗,π∗)>0.\displaystyle=\rho^{{Pol}}(I^{\*},\pi^{\*})-\rho^{{Pol}}(\widetilde{I},\widetilde{\pi})+V^{{In}}(\widetilde{I},\widetilde{\pi})-V^{{In}}(I^{\*},\pi^{\*})>0. |  |

Thus, the contract (I~,π^)(\widetilde{I},\hat{\pi}) satisfies

|  |  |  |
| --- | --- | --- |
|  | ρP​o​l​(I~,π^)=ρP​o​l​(I∗,π∗)andVI​n​(I~,π^)>VI​n​(I∗,π∗),\rho^{{Pol}}(\widetilde{I},\hat{\pi})=\rho^{{Pol}}(I^{\*},\pi^{\*})\quad\text{and}\quad V^{{In}}(\widetilde{I},\hat{\pi})>V^{{In}}(I^{\*},\pi^{\*}), |  |

which contradicts the Pareto optimality of (I∗,π∗)(I^{\*},\pi^{\*}). Hence, (I∗,π∗)(I^{\*},\pi^{\*}) is optimal for ([17](https://arxiv.org/html/2602.16401v1#S4.E17 "Equation 17 ‣ Proposition 4.1. ‣ 4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). ∎

### A.6. Proof of Proposition [4.2](https://arxiv.org/html/2602.16401v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")

Consider a Stackelberg equilibrium (Ig∗∗,g∗)(I^{\*}\_{g^{\*}},g^{\*}) inducing a contract (Ig∗∗,πg∗∗)(I^{\*}\_{g^{\*}},\pi^{\*}\_{g^{\*}}), where πg∗∗:=Πg∗​(Ig∗∗​(X))=∫Ig∗∗​𝑑g∗∘ℙ\pi^{\*}\_{g^{\*}}:=\Pi\_{g^{\*}}(I^{\*}\_{g^{\*}}(X))=\int I^{\*}\_{g^{\*}}\,dg^{\*}\circ\mathbb{P}. By Proposition [4.1](https://arxiv.org/html/2602.16401v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"), to show that (Ig∗∗,πg∗∗)(I^{\*}\_{g^{\*}},\pi^{\*}\_{g^{\*}}) is Pareto optimal, it suffices to show that it is optimal for Problem ([17](https://arxiv.org/html/2602.16401v1#S4.E17 "Equation 17 ‣ Proposition 4.1. ‣ 4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). By translation invariance of the distortion risk measure, a contract (I∗,π∗)(I^{\*},\pi^{\*}) is Pareto optimal if and only if the indemnity function I∗I^{\*} solves

|  |  |  |
| --- | --- | --- |
|  | minI∈ℐL⁡{ρP​o​l​(X−I​(X))+𝔼​[I​(X)]}.\min\_{I\in\mathcal{I}\_{L}}\left\{\rho^{{Pol}}(X-I(X))+\mathbb{E}[I(X)]\right\}. |  |

Equivalently, using retention functions, the above problem becomes:

|  |  |  |
| --- | --- | --- |
|  | minR∈ℐL⁡{ρP​o​l​(R​(X))+𝔼​[X−R​(X)]}.\min\_{R\in\mathcal{I}\_{L}}\left\{\rho^{{Pol}}(R(X))+\mathbb{E}[X-R(X)]\right\}. |  |

Using q​(t):=FR​(X)−1​(t)q(t):=F\_{R(X)}^{-1}(t) for a.e. t∈[0,1]t\in[0,1], the above problem is equivalent to the following:

|  |  |  |
| --- | --- | --- |
|  | minq∈𝒬L⁡{∫01q′​(t)​[T​(1−t)−(1−t)]​dt+𝔼​[X]}.\displaystyle\min\_{q\in\mathcal{Q}\_{L}}\left\{\int\_{0}^{1}q^{\prime}(t)\left[T(1-t)-(1-t)\right]\,\mathrm{d}t+\mathbb{E}[X]\right\}. |  |

Since (Ig∗∗,g∗)(I^{\*}\_{g^{\*}},g^{\*}) is a Stackelberg equilibrium, the optimal quantile qg∗∗q^{\*}\_{g^{\*}} characterized in Theorem [3.9](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem9 "Theorem 3.9. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") solves the above minimization problem. Hence, the induced contract (Ig∗∗,πg∗∗)(I^{\*}\_{g^{\*}},\pi^{\*}\_{g^{\*}}) is Pareto optimal. We now show that (Ig∗∗,πg∗∗)(I^{\*}\_{g^{\*}},\pi^{\*}\_{g^{\*}}) is individually rational but leaves the policyholder indifferent. First, note that the insurer’s expected profit under (Ig∗∗,πg∗∗)(I^{\*}\_{g^{\*}},\pi^{\*}\_{g^{\*}}) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | VI​n​(Ig∗∗,πg∗∗)\displaystyle V^{In}(I^{\*}\_{g^{\*}},\pi^{\*}\_{g^{\*}}) | =∫01(FX−1)′​(t)​[t−T~​(t)]​ 1{T~​(t)<t}​dt≥0=VI​n​(0,0).\displaystyle=\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\left[t-\widetilde{T}(t)\right]\,\mathbbm{1}\_{\{\widetilde{T}(t)<t\}}\,\mathrm{d}t\geq 0=V^{In}(0,0). |  |

Moreover, for the policyholder, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρP​o​l​(Ig∗∗,πg∗∗)−ρP​o​l​(0,0)\displaystyle\rho^{Pol}(I^{\*}\_{g^{\*}},\pi^{\*}\_{g^{\*}})-\rho^{Pol}(0,0) | =∫01(FX−1)′​(t)​g∗​(1−t)​dt+∫01(qg∗∗)′​(t)​[T​(1−t)−g∗​(1−t)]​dt\displaystyle=\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,g^{\*}(1-t)\,\mathrm{d}t+\int\_{0}^{1}\left(q^{\*}\_{g^{\*}}\right)^{\prime}(t)\,\left[T(1-t)-g^{\*}(1-t)\right]\,\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫01(FX−1)′​(t)​T​(1−t)​dt\displaystyle\qquad\qquad-\int\_{0}^{1}\left(F\_{X}^{-1}\right)^{\prime}(t)\,T(1-t)\,\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01[(qg∗∗)′​(t)−(FX−1)′​(t)]​[T​(1−t)−g∗​(1−t)]​dt.\displaystyle=\int\_{0}^{1}\left[\left(q^{\*}\_{g^{\*}}\right)^{\prime}(t)-\left(F\_{X}^{-1}\right)^{\prime}(t)\right]\,\left[T(1-t)-g^{\*}(1-t)\right]\,\mathrm{d}t. |  |

Consider the following three cases:

1. (1)

   If T~​(t)<t\widetilde{T}(t)<t, then by optimality, g~∗​(t)=T~​(t)\widetilde{g}^{\*}(t)=\widetilde{T}(t), or equivalently g∗​(1−t)=T​(1−t)g^{\*}(1-t)=T(1-t). Hence,
   [(qg∗∗)′​(t)−(FX−1)′​(t)]​[T​(1−t)−g∗​(1−t)]=0\left[\left(q^{\*}\_{g^{\*}}\right)^{\prime}(t)-\left(F\_{X}^{-1}\right)^{\prime}(t)\right]\,\left[T(1-t)-g^{\*}(1-t)\right]=0.
2. (2)

   If T~​(t)=t\widetilde{T}(t)=t and g~∗​(t)<T~​(t)\widetilde{g}^{\*}(t)<\widetilde{T}(t), then (qg∗∗)′​(t)=(FX−1)′​(t)\left(q^{\*}\_{g^{\*}}\right)^{\prime}(t)=\left(F\_{X}^{-1}\right)^{\prime}(t).
   If T~​(t)=t\widetilde{T}(t)=t and g~∗​(t)=T~​(t)\widetilde{g}^{\*}(t)=\widetilde{T}(t), then g∗​(1−t)=T​(1−t)g^{\*}(1-t)=T(1-t).
   In both cases,
   [(qg∗∗)′​(t)−(FX−1)′​(t)]​[T​(1−t)−g∗​(1−t)]=0\left[\left(q^{\*}\_{g^{\*}}\right)^{\prime}(t)-\left(F\_{X}^{-1}\right)^{\prime}(t)\right]\,\left[T(1-t)-g^{\*}(1-t)\right]=0.
3. (3)

   If T~​(t)>t\widetilde{T}(t)>t, then (qg∗∗)′​(t)=(FX−1)′​(t)\left(q^{\*}\_{g^{\*}}\right)^{\prime}(t)=\left(F\_{X}^{-1}\right)^{\prime}(t), and [(qg∗∗)′​(t)−(FX−1)′​(t)]​[T​(1−t)−g∗​(1−t)]=0\left[\left(q^{\*}\_{g^{\*}}\right)^{\prime}(t)-\left(F\_{X}^{-1}\right)^{\prime}(t)\right]\,\left[T(1-t)-g^{\*}(1-t)\right]=0.

Consequently, we finally obtain ρP​o​l​(Ig∗∗,πg∗∗)=ρP​o​l​(0,0)\rho^{Pol}(I^{\*}\_{g^{\*}},\pi^{\*}\_{g^{\*}})=\rho^{Pol}(0,0).∎

### A.7. Proof of Proposition [4.3](https://arxiv.org/html/2602.16401v1#S4.Thmtheorem3 "Proposition 4.3. ‣ 4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")

Consider a Pareto optimal contract (I∗,π∗)(I^{\*},\pi^{\*}), such that ρP​o​l​(I∗,π∗)=ρP​o​l​(0,0)\rho^{Pol}(I^{\*},\pi^{\*})=\rho^{{Pol}}(0,0). We show that this contract is induced by a Stackelberg equilibrium. First, note that under (I∗,π∗)(I^{\*},\pi^{\*}), the following holds by translation invariance and comonotonic additivity of ρP​o​l\rho^{Pol}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρP​o​l​(I∗,π∗)\displaystyle\rho^{Pol}(I^{\*},\pi^{\*}) | =ρP​o​l​(X−I∗​(X))+π∗=ρP​o​l​(X)−ρP​o​l​(I∗​(X))+π∗.\displaystyle=\rho^{Pol}\left(X-I^{\*}(X)\right)+\pi^{\*}=\rho^{Pol}\left(X\right)-\rho^{Pol}\left(I^{\*}(X)\right)+\pi^{\*}. |  |

Since, ρP​o​l​(I∗,π∗)=ρP​o​l​(0,0)=ρP​o​l​(X)\rho^{Pol}(I^{\*},\pi^{\*})=\rho^{{Pol}}(0,0)=\rho^{{Pol}}(X), we have that π∗=ρP​o​l​(I∗​(X))\pi^{\*}=\rho^{{Pol}}(I^{\*}(X)). Moreover, since (I∗,π∗)(I^{\*},\pi^{\*}) is Pareto optimal, Proposition [4.1](https://arxiv.org/html/2602.16401v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") implies that the quantile function q∗​(t):=FX−1​(t)−FI∗​(X)−1​(t)q^{\*}(t):=F\_{X}^{-1}(t)-F\_{I^{\*}(X)}^{-1}(t) satisfies

|  |  |  |
| --- | --- | --- |
|  | (q∗)′​(t)={0,T​(1−t)>1−t,ϕ​(t),T​(1−t)=1−t,(FX−1)′​(t),T​(1−t)<1−t,(q^{\*})^{\prime}(t)=\begin{cases}0,&T(1-t)>1-t,\\ \phi(t),&T(1-t)=1-t,\\ \left(F\_{X}^{-1}\right)^{\prime}(t),&T(1-t)<1-t,\end{cases} |  |

for some measurable function ϕ\phi satisfying ϕ​(t)∈[0,(FX−1)′​(t)].\phi(t)\in[0,\left(F\_{X}^{-1}\right)^{\prime}(t)].

Consider now the pair (q∗,gI∗∗)(q^{\*},g^{\*}\_{I^{\*}}), where the pricing distortion function gI∗∗g^{\*}\_{I^{\*}} coincides with the policyholder’s distortion function TT. That is,

|  |  |  |
| --- | --- | --- |
|  | gI∗∗​(t):=T​(t),∀t∈[0,1].g^{\*}\_{I^{\*}}(t):=T(t),\ \forall\,t\in[0,1]. |  |

Thus,

|  |  |  |
| --- | --- | --- |
|  | ΠgI∗∗​(I∗​(X))=∫I∗​(X)​dgI∗∗∘ℙ=∫I∗​(X)​dT∘ℙ=ρP​o​l​(I∗​(X))=π∗.\Pi\_{g^{\*}\_{I^{\*}}}\left(I^{\*}(X)\right)=\int I^{\*}(X)\,\mathrm{d}g^{\*}\_{I^{\*}}\circ\mathbb{P}=\int I^{\*}(X)\,\mathrm{d}T\circ\mathbb{P}=\rho^{{Pol}}(I^{\*}(X))=\pi^{\*}. |  |

Since (q∗,gI∗∗)(q^{\*},g^{\*}\_{I^{\*}}) satisfies the optimality conditions of Theorem [3.9](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem9 "Theorem 3.9. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"), it follows that (q∗,gI∗∗)(q^{\*},g^{\*}\_{I^{\*}}) solves the problem given in ([12](https://arxiv.org/html/2602.16401v1#S3.E12 "Equation 12 ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting")). Lemma [3.8](https://arxiv.org/html/2602.16401v1#S3.Thmtheorem8 "Lemma 3.8. ‣ 3.2. The Insurer’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting") then implies that the market mechanism (I∗,gI∗∗)(I^{\*},g^{\*}\_{I^{\*}}) is a Stackelberg equilibrium. Hence, the Pareto optimal insurance contract (I∗,π∗)(I^{\*},\pi^{\*}) can be obtained from the Stackelberg equilibrium (I∗,gI∗∗)(I^{\*},g^{\*}\_{I^{\*}}), where π∗:=ΠgI∗∗​(I∗​(X))\pi^{\*}:=\Pi\_{g^{\*}\_{I^{\*}}}\left(I^{\*}(X)\right) . ∎

## References

* M. Andraos, M. Ghossoub, and M. B. Zhu (2026)
  Subgame perfect nash equilibria in large reinsurance markets.
  Insurance: Mathematics and Economics 127,  pp. 103210.
  External Links: [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.insmatheco.2025.103210),
  ISSN 0167-6687,
  [Link](https://www.sciencedirect.com/science/article/pii/S0167668725001568)
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p2.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),
  [§4](https://arxiv.org/html/2602.16401v1#S4.p4.1 "4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* H. Assa (2015)
  On Optimal Reinsurance Policy with Distortion Risk Measures and Premiums.
  Insurance: Mathematics and Economics 61,  pp. 70–75.
  External Links: ISSN 0167-6687
  Cited by: [§A.2](https://arxiv.org/html/2602.16401v1#A1.SS2.p3.1 "A.2. Proof of Lemma 3.5 ‣ Appendix A Proofs of Main Results ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),
  [§1](https://arxiv.org/html/2602.16401v1#S1.p3.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),
  [§3.1](https://arxiv.org/html/2602.16401v1#S3.SS1.p12.1 "3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* H. Bleichrodt, S. Grant, and J. Yang (2023)
  Testing hurwicz expected utility.
  Econometrica 91 (4),  pp. 1393–1416.
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p3.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* T.J. Boonen, K.C. Cheung, and Y. Zhang (2021)
  Bowley Reinsurance with Asymmetric Information on the Insurer’s Risk Preferences.
  Scandinavian Actuarial Journal 2021 (7),  pp. 623–644.
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p2.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* T.J. Boonen and Y. Zhang (2022)
  Bowley Reinsurance with Asymmetric Information: A First-Best Solution.
  Scandinavian Actuarial Journal 2022,  pp. 532–551.
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p2.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* T. J. Boonen and M. Ghossoub (2023)
  Bowley vs. Pareto Optima in Reinsurance Contracting.
  European Journal of Operational Research 307 (1),  pp. 382–391.
  External Links: ISSN 0377-2217
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p2.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),
  [§1](https://arxiv.org/html/2602.16401v1#S1.p5.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),
  [§4](https://arxiv.org/html/2602.16401v1#S4.p4.1 "4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* A. L. Bowley (1928)
  Bilateral Monopoly.
  Economic Journal 38 (152),  pp. 651–659.
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p2.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* G. Carlier and R. Dana (2003)
  Pareto Efficient Insurance Contracts when the Insurer’s Cost Function is Discontinuous.
  Economic Theory 21 (4),  pp. 871–893.
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p3.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),
  [§2.3](https://arxiv.org/html/2602.16401v1#S2.SS3.p2.2 "2.3. Market Mechanisms and Contracts ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* G. Carlier and R. Dana (2005)
  Rearrangement Inequalities in Non-convex Insurance Models.
  Journal of Mathematical Economics 41 (4-5),  pp. 483–503.
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p3.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* F-Y. Chan and H.U. Gerber (1985)
  The Reinsurer’s Monopoly and the Bowley Solution.
  ASTIN Bulletin: The Journal of the IAA 15 (2),  pp. 141–148.
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p2.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* K. C. Cheung, S. C. P. Yam, and Y. Zhang (2019)
  Risk-Adjusted Bowley Reinsurance under Distorted Probabilities.
  Insurance: Mathematics and Economics 86,  pp. 64–72.
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p2.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),
  [§1](https://arxiv.org/html/2602.16401v1#S1.p3.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),
  [§1](https://arxiv.org/html/2602.16401v1#S1.p6.2 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),
  [§5.2](https://arxiv.org/html/2602.16401v1#S5.SS2.p7.2 "5.2. Optimality of Coverage Limit Contracts ‣ 5. Examples ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* S.H. Chew, E. Karni, and Z. Safra (1987)
  Risk Aversion in the Theory of Expected Utility with Rank Dependent Pobabilities.
  Journal of Economic Theory 42 (2),  pp. 370–381.
  Cited by: [§2.2](https://arxiv.org/html/2602.16401v1#S2.SS2.p7.1 "2.2. Risk Aversion ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),
  [§2.2](https://arxiv.org/html/2602.16401v1#S2.SS2.p8.1 "2.2. Risk Aversion ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* H. Föllmer and A. Schied (2016)
  Stochastic Finance: An Introduction in Discrete Time – 4t​h4^{th} ed..
   Walter de Gruyter.
  Cited by: [§3.1](https://arxiv.org/html/2602.16401v1#S3.SS1.p3.4 "3.1. The Policyholder’s Problem ‣ 3. Characterization of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* G.Taylor (1992)
  Risk Exchange I: a Unification of Some Existing Results.
  Scandinavian Actuarial Journal 1992 (1),  pp. 15–39.
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p2.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* M. Ghossoub and X. He (2021)
  Comparative Risk Aversion in RDEU with Applications to Optimal Underwriting of Securities Issuance.
  Insurance Mathematics and Economics 101 (1),  pp. 6–22.
  Cited by: [§2.2](https://arxiv.org/html/2602.16401v1#S2.SS2.p7.1 "2.2. Risk Aversion ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* M. Ghossoub, B. Li, and B. Shi (2025)
  Bowley-Optimal Convex-Loaded Premium Principles.
  Insurance: Mathematics and Economics 121 (1),  pp. 157–180.
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p2.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* M. Ghossoub and M. B. Zhu (2024)
  Stackelberg Equilibria with Multiple Policyholders.
  Insurance: Mathematics and Economics 116 (1),  pp. 189–201.
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p2.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),
  [§1](https://arxiv.org/html/2602.16401v1#S1.p5.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),
  [§4](https://arxiv.org/html/2602.16401v1#S4.p4.1 "4. Pareto Efficiency of Stackelberg Equilibria ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* D. Li and V. R. Young (2021)
  Bowley Solution of a Mean–Mariance Game in Insurance.
  Insurance: Mathematics and Economics 98,  pp. 35–43.
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p2.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* D. Prelec (1998)
  The Probability Weighting Function.
  Econometrica 66 (3),  pp. 497–527.
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p3.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* J. Quiggin (1993)
  Generalized Expected Utility Theory - The Rank-Dependent Model.
   Kluwer Academic Publishers.
  Cited by: [§2.2](https://arxiv.org/html/2602.16401v1#S2.SS2.p7.1 "2.2. Risk Aversion ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* A. Tversky and D. Kahneman (1992)
  Advances in Prospect Theory: Cumulative Representation of Uncertainty.
  Journal of Risk and Uncertainty 5 (4),  pp. 297–323.
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p3.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),
  [§5.3](https://arxiv.org/html/2602.16401v1#S5.SS3.p1.1 "5.3. Optimality of Deductible Contracts ‣ 5. Examples ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),
  [§5.3](https://arxiv.org/html/2602.16401v1#S5.SS3.p6.11 "5.3. Optimality of Deductible Contracts ‣ 5. Examples ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* M.E. Yaari (1987)
  The Dual Theory of Choice under Risk.
  Econometrica 55 (1),  pp. 95–115.
  Cited by: [§2.2](https://arxiv.org/html/2602.16401v1#S2.SS2.p4.3 "2.2. Risk Aversion ‣ 2. Problem Formulation ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").
* M. B. Zhu, M. Ghossoub, and T. J. Boonen (2023)
  Equilibria and Efficiency in a Reinsurance Market.
  Insurance: Mathematics and Economics 113,  pp. 24–49.
  External Links: ISSN 0167-6687
  Cited by: [§1](https://arxiv.org/html/2602.16401v1#S1.p2.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting"),
  [§1](https://arxiv.org/html/2602.16401v1#S1.p3.1 "1. Introduction ‣ Stackelberg Equilibria in Monopoly Insurance Markets with Probability Weighting").