---
authors:
- Emanuele Borgonovo
- An Chen
- Massimo Marinacci
- Shihao Zhu
doc_id: arxiv:2603.08552v1
family_id: arxiv:2603.08552
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Nonconcave Portfolio Choice under Smooth Ambiguity
url_abs: http://arxiv.org/abs/2603.08552v1
url_html: https://arxiv.org/html/2603.08552v1
venue: arXiv q-fin
version: 1
year: 2026
---


Emanuele Borgonovo
 An Chen
 Massimo Marinacci11footnotemark: 1
 Shihao Zhu22footnotemark: 2
Department of Decision Sciences, Bocconi University, 20136 Milan, Italy, emails: emanuele.borgonovo@unibocconi.it; massimo.marinacci@unibocconi.it.Institute of Insurance Science, Ulm University, Helmholtzstr. 20, 89069 Ulm, Germany, emails: an.chen@uni-ulm.de; shihao.zhu@uni-ulm.de.

###### Abstract

We study continuous-time portfolio choice with nonlinear payoffs under smooth ambiguity and Bayesian learning. We develop a general framework for dynamic, non-concave asset allocation that accommodates nonlinear payoffs, broad utility classes, and flexible ambiguity attitudes. Dynamic consistency is obtained by a robust representation that recasts the ambiguity-averse problem as ambiguity-neutral with distorted priors. This structure delivers explicit trading rules by combining nonlinear filtering with the martingale approach and nests standard concave and linear-payoff benchmarks. As a leading application, delegated management with convex incentives illustrates that ambiguity aversion shifts beliefs toward adverse states, limits the range of states that would otherwise trigger more aggressive risk taking, and reduces volatility through lower risky exposure.

Keywords: Smooth ambiguity, Nonconcave portfolio optimization, Robust representation, Bayesian learning, Option-based payoffs

MSC (2020): 91B06, 91G10, 93E11.

JEL Classification: C61, D81, G11.

## 1 Introduction

Decision-makers face uncertainty not only about outcomes (risk), but also about the probabilities governing those outcomes (ambiguity). Preferences therefore reflect attitudes toward both risk and ambiguity, with substantial evidence supporting ambiguity aversion (Marinacci, [2015](#bib.bib50 "Model uncertainty")). The recent literature on financial decision-making has intensively considered how to model these attitudes in both prescriptive and descriptive modes, as the works of Balter et al. ([2021](#bib.bib69 "Time-consistency of optimal investment under smooth ambiguity")); Guan et al. ([2025a](#bib.bib22 "The continuous-time pre-commitment KMM problem in incomplete markets"), [b](#bib.bib49 "Equilibrium portfolio selection for smooth ambiguity preferences")); Bäuerle and Mahayni ([2024](#bib.bib33 "Optimal investment in ambiguous financial markets with learning")) illustrate. One of the challenges in developing a comprehensive modeling approach is accounting for not only risk and ambiguity preferences but also nonlinear payoffs arising from alternative investment forms and financial compensation mechanisms. A canonical instance is option-like terminal payoffs, as discussed in Carpenter ([2000](#bib.bib61 "Does option compensation increase managerial risk appetite?")) and Dai et al. ([2022](#bib.bib57 "Nonconcave utility maximization with portfolio bounds")). Moreover, the model must reflect the fact that investors revise their beliefs after receiving information, for instance, from market prices, thereby yielding a dynamic class of decision-making problems.

Prior work has typically examined these forces separately. Carpenter ([2000](#bib.bib61 "Does option compensation increase managerial risk appetite?")) studies option-type payoffs, but abstracts from both ambiguity and learning. Bäuerle and Mahayni ([2024](#bib.bib33 "Optimal investment in ambiguous financial markets with learning")), by contrast, incorporates ambiguity aversion and Bayesian learning, yet confines attention to linear payoffs and therefore misses the convex incentives central to option-based compensation. We bring these elements together in a general continuous-time portfolio framework with nonlinear payoffs, ambiguity aversion, and Bayesian learning. This framework yields tractable optimal trading rules and sharp comparative statics, providing a systematic characterization of how incentive convexity, belief updating, and ambiguity interact in dynamic financial decision-making.

We aim to theoretically examine the effects of ambiguity preferences, analyzing the whole spectrum from near-ambiguity neutrality to complete aversion (close to min-max decision-making). The ideal ambiguity representation is then that of the smooth-ambiguity functional of Klibanoff et al. ([2005](#bib.bib75 "A smooth model of decision making under ambiguity")) (KMM, henceforth). The KMM functional separates beliefs from tastes toward ambiguity, uses a concave aggregator to capture dislike for ambiguous bets, and yields a smooth value index that eases calibration, estimation, and comparative statics.

However, when combining smooth ambiguity with non-concavity objectives, two key challenges emerge. First, the concavity of the ambiguity aggregator breaks dynamic consistency (see Hanany and Klibanoff ([2009](#bib.bib3 "Updating ambiguity averse preferences")); Savochkin et al. ([2025](#bib.bib4 "Dynamic consistency and rectangularity for the smooth ambiguity model"))), thus impairing the inclusion of belief updates. Second, nonconcave maximization problems induced by option-style payoffs invalidate off-the-shelf convex optimization tools. We resolve these challenges as follows.
We resort to a representation of quasiconcave functionals that transforms the ambiguity-averse problem into a Bayesian adaptive problem with endogenously distorted priors (Cerreia-Vioglio et al., [2011c](#bib.bib47 "Uncertainty averse preferences"), [a](#bib.bib42 "Complete monotone quasiconcave duality"); Drapeau and Kupper, [2013](#bib.bib65 "Risk preferences and their robust representation"); Mazzon and Tankov, [2024](#bib.bib66 "Optimal stopping and divestment timing under scenario ambiguity and learning")). We use this reformulation because, as shown in Mazzon and Tankov ([2024](#bib.bib66 "Optimal stopping and divestment timing under scenario ambiguity and learning")), it breaks the optimization problem into two parts. We propose a general result for our min-max formulation, where the (external) minimization is taken over the set of all possible priors and the (internal) maximization is equivalent to an ambiguity-neutral problem. The nested structure restores dynamic consistency because the maximization part is now a Bayesian expected utility problem. This makes the approach different from techniques that enforce time consistency by restricting the intertemporal structure of priors (often called “rectangularity”; see Savochkin et al. ([2025](#bib.bib4 "Dynamic consistency and rectangularity for the smooth ambiguity model"))) or from game-theoretic resolutions that accept time inconsistency under concave utility (e.g., Guan et al. ([2025b](#bib.bib49 "Equilibrium portfolio selection for smooth ambiguity preferences"))).

We then apply the resulting two-step approach to solve continuous-time portfolio problems with ambiguity preferences, learning, and non-concave objectives. In particular, we focus on financial decision problems with nonlinear payoffs. By applying nonlinear filtering, we update prior beliefs dynamically as market prices are observed. The internal (ambiguity-neutral) optimization problem is rewritten as an adaptive Bayesian problem with unknown drift (see, e.g., Karatzas and Zhao ([2001](#bib.bib30 "Bayesian adaptive portfolio optimization")); Rieder and Bäuerle ([2005](#bib.bib31 "Portfolio optimization with unobservable markov-modulated drift process"))). Next, we combine the martingale method (e.g., (Karatzas and Shreve, [1998a](#bib.bib72 "Methods of mathematical finance"), Ch. 3)) with concavification, replacing the original non-concave objective by its concave envelope to recover a tractable concave optimization problem. This yields explicit continuous-time trading rules for a broad class of genuinely non-concave problems.

We complete the analysis by incorporating ambiguity preferences and performing an optimization over the set of priors. The approach yields an ambiguity‑neutral portfolio choice evaluated under an endogenously distorted prior that directly determines the optimal trading strategy, while accounting for ambiguity attitudes. We study the impact of ambiguity, deriving closed‑form characterizations for decision-makers whose preferences for risk and ambiguity are modeled, respectively, by power-power and power-exponential specifications.

We then study how ambiguity shapes beliefs and investment policies. We analyze the impact of alternative risk preferences, ambiguity attitudes, and prior beliefs on the distorted prior, the optimal trading strategy, and terminal wealth, respectively.
The analysis shows that ambiguity aversion reallocates probability mass toward adverse states, effectively tightening risk constraints. As a result, optimal exposure to risky assets decreases in regions where the objective is locally convex in wealth or exposure. This pessimistic distortion disciplines incentives that would otherwise promote excessive risk-taking. By contrast, when the objective is locally concave, the impact of ambiguity is attenuated and aligns with standard robust‑investment prescriptions.

We illustrate these mechanisms in a leading application to delegated portfolio management with convex incentive contracts (see Carpenter ([2000](#bib.bib61 "Does option compensation increase managerial risk appetite?"))). In this setting, the endogenous prior distortion and the associated filtering dynamics translate into explicit portfolio rules and sharp quantitative predictions for risk taking.

The remainder of the paper is organized as follows. Section [2](#S2 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") overviews the related literature. Section [3](#S3 "3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") formulates the problem. Section [4](#S4 "4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") sets up the decision functional, introducing the nested objective function. Section [5](#S5 "5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") derives results for the problem of convex incentive contracts under smooth ambiguity preferences.
Section [6](#S6 "6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") presents detailed numerical experiments and comparative statics. Section [7](#S7 "7 Conclusion ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") offers conclusions.

## 2 Related Literature

Our paper intersects previous literature on smooth ambiguity with learning in continuous time, robust representations for ambiguity and quasiconcave functionals, portfolio choice with non-concave objectives, and delegated portfolio management with convex incentives. Each of these research streams is broad in itself, and a comprehensive review is out of reach in the present work. We therefore provide a concise review of the aspects more salient for our work.

Regarding preferences in continuous time with learning, a growing body of work is studying asset allocation under smooth ambiguity. Balter et al. ([2021](#bib.bib69 "Time-consistency of optimal investment under smooth ambiguity")) study portfolio choice under smooth ambiguity, but restrict attention to deterministic strategies and therefore abstract from the subtle issue of time inconsistency. Guan et al. ([2025a](#bib.bib22 "The continuous-time pre-commitment KMM problem in incomplete markets")) examine portfolio choice in incomplete markets from a pre-commitment perspective, in which the decision maker fixes a strategy at the initial date and does not revise it over time. Relative to this literature, we focus on time-consistent portfolio choice with learning. Our goal is to jointly accommodate Bayesian learning, genuinely nonlinear (option-style) payoffs, and broad utility/aggregator classes, while preserving dynamic consistency through a robust representation that delivers explicit trading rules and comparative statics. Closer to our setting, Bäuerle and Mahayni ([2024](#bib.bib33 "Optimal investment in ambiguous financial markets with learning")) and Guan et al. ([2025b](#bib.bib49 "Equilibrium portfolio selection for smooth ambiguity preferences")) allow for Bayesian learning under smooth ambiguity. Guan et al. ([2025b](#bib.bib49 "Equilibrium portfolio selection for smooth ambiguity preferences")) incorporates Bayesian learning but maintains concave utility and derives equilibrium characterizations in a time-inconsistent environment. Bäuerle and Mahayni ([2024](#bib.bib33 "Optimal investment in ambiguous financial markets with learning")), by contrast, considers power utility and linear payoffs, and uses a dual representation based on LpL^{p} norms to obtain time-consistent solutions under smooth ambiguity. Our paper departs from these studies by allowing for general utility and aggregator classes in a dynamically consistent framework that also accommodates learning and genuinely nonlinear, option-like payoffs.

The goal of a general ambiguity representation connects us to the broad literature on dynamic choice under ambiguity. A key conceptual foundation is the robust representation of quasiconcave preference functionals, which provides a rationale for distorted priors; see Cerreia-Vioglio et al. ([2011c](#bib.bib47 "Uncertainty averse preferences"), [a](#bib.bib42 "Complete monotone quasiconcave duality"), [b](#bib.bib40 "Risk measures: Rationality and diversification")); Drapeau and Kupper ([2013](#bib.bib65 "Risk preferences and their robust representation")). In particular, when the smooth ambiguity problem is rewritten in certainty-equivalent form, Theorem 7 of Cerreia-Vioglio et al. ([2011c](#bib.bib47 "Uncertainty averse preferences")) and Proposition 6 of Drapeau and Kupper ([2013](#bib.bib65 "Risk preferences and their robust representation")) deliver a sup–inf representation that is well suited to dynamic updating. Mazzon and Tankov ([2024](#bib.bib66 "Optimal stopping and divestment timing under scenario ambiguity and learning")) exploits this type of reformulation in an optimal stopping problem. Our paper is further related to Hansen and Miao ([2018](#bib.bib64 "Aversion to ambiguity and model misspecification in dynamic stochastic environments"), [2022](#bib.bib5 "Asset pricing under smooth ambiguity in continuous time")), who develop recursive representations of recursive smooth ambiguity preferences (Klibanoff et al. ([2009](#bib.bib2 "Recursive smooth ambiguity preferences"))). They show that ambiguity aversion can be recast as a robust distortion of priors and posteriors over the hidden Markov state, and study its implications for asset allocation and asset pricing.

When coming to financial-decision making, depending on the instrument at hand, problems can give rise to formulations with nonconcave utility maximization and option-style payoffs.
Examples include convex incentive contracts in Carpenter ([2000](#bib.bib61 "Does option compensation increase managerial risk appetite?")), performance-fee schemes in He and Kou ([2018](#bib.bib11 "Profit sharing in hedge funds")), equity-linked insurance with guarantees in Chen et al. ([2019](#bib.bib76 "Constrained non-concave utility maximization: an application to life insurance contracts with guarantees")), and goal-based preferences in Capponi and Zhang ([2024](#bib.bib10 "A continuous time framework for sequential goal-based wealth management")). We refer to Dai et al. ([2022](#bib.bib57 "Nonconcave utility maximization with portfolio bounds")) for a general treatment of non-concave portfolio maximization under portfolio constraints. Departing from this literature, which assumes known return dynamics, we introduce ambiguity in expected returns, incorporate Bayesian updating, and provide explicit decision rules using robust representation, filtering, and concavification.

A vast literature studies how contract convexity shapes risk-taking and induces lock-in effects; see Carpenter ([2000](#bib.bib61 "Does option compensation increase managerial risk appetite?")); Basak et al. ([2007](#bib.bib13 "Optimal asset allocation and risk shifting in money management")). We revisit this setting through the lens of ambiguity and learning.

Taken together, these research strands help us highlight the open issues addressed in this work, namely, to deliver a time-consistent solution method for continuous-time smooth-ambiguity portfolio problems with learning and non-concave payoffs, provide explicit trading policies and comparative statics, and offer portable insights for delegated management and embedded-option applications.

## 3 Problem Formulation

Let (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) be a probability space equipped with a filtration 𝔽=(ℱt)t∈[0,T]\mathbb{F}=(\mathcal{F}\_{t})\_{t\in[0,T]} satisfying the usual conditions of completeness and right-continuity. Here T>0T>0 is the fixed planning horizon, and the filtration 𝔽\mathbb{F} gathers all information available in the financial market.

Before modeling the investor’s decisions under smooth ambiguity preferences, we introduce the source of ambiguity—uncertainty about the expected return—in the financial market setup. Assume that there are two assets that an investor can trade without any transaction costs: a risk-free and a risky asset. The risk-free asset (bond) has price process S0=(St0)t∈[0,T]S^{0}=(S^{0}\_{t})\_{t\in[0,T]} governed by

|  |  |  |
| --- | --- | --- |
|  | d​St0=r​St0​d​t,S00=s0>0,dS^{0}\_{t}=rS^{0}\_{t}dt,\qquad S^{0}\_{0}=s^{0}>0, |  |

where r>0r>0 is the constant interest rate. The risky asset (stock) has the price process S=(St)t∈[0,T]S=(S\_{t})\_{t\in[0,T]} satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=Z​St​d​t+σ​St​d​Bt,S0=s>0,dS\_{t}=ZS\_{t}\,dt+\sigma S\_{t}\,dB\_{t},\qquad S\_{0}=s>0, |  | (3.1) |

where B=(Bt)t∈[0,T]B=(B\_{t})\_{t\in[0,T]} is an 𝔽\mathbb{F}-adapted standard Brownian motion under ℙ\mathbb{P}, σ>0\sigma>0 is the known constant volatility, and Z∈ℝZ\in\mathbb{R} denotes the expected return of the stock. As explained in (Kardaras and Robertson, [2012](#bib.bib21 "ROBUST maximization of asymptotic growth"), footnote 2), high-frequency data readily give good estimators for σ\sigma, while estimating ZZ is much more statistically challenging. Therefore, we assume the investor faces uncertainty about the constant value of Z∈𝒮Z\in\mathcal{S} for a compact metric space 𝒮⊂ℝ\mathcal{S}\subset\mathbb{R}. As time proceeds, the investor learns about the parameter ZZ through observation of the stock prices SS.

Assume that ZZ is, *a priori*, independent of BB and follows a prior 𝒫\mathcal{P} satisfying the condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∃η>0​ such that∫ℝeη​z2​𝒫​(d​z)<∞.\exists\,\eta>0\text{ such that}\quad\int\_{\mathbb{R}}e^{\eta z^{2}}\mathcal{P}(dz)<\infty. |  | (3.2) |

Condition ([3.2](#S3.E2 "In 3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) requires ZZ to be sub-Gaussian, a property that will be useful for the filtering arguments later.

Consider a self-financing portfolio strategy π=(πt)t∈[0,T]\pi=(\pi\_{t})\_{t\in[0,T]} that invests πt∈ℝ\pi\_{t}\in\mathbb{R} dollars in the stock at time tt. Then, the investor’s wealth process Ww,π,Z=(Wtw,π,Z)t∈[0,T]W^{w,\pi,Z}=(W^{w,\pi,Z}\_{t})\_{t\in[0,T]} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Wtw,π,Z=[r​Wtw,π,Z+(Z−r)​πt]​d​t+σ​πt​d​Bt,W0w,π,Z=w>0.dW^{w,\pi,Z}\_{t}=\bigl[rW^{w,\pi,Z}\_{t}+(Z-r)\pi\_{t}\bigr]\,dt+\sigma\pi\_{t}\,dB\_{t},\quad W^{w,\pi,Z}\_{0}=w>0. |  | (3.3) |

The drift term combines the accrual at the risk-free rate rr on the current wealth and the excess return (Z−r)(Z-r) on the risky investment. In the following, we shall simply write WπW^{\pi} to denote Ww,π,ZW^{w,\pi,Z}, where needed.

Because the drift ZZ is unobservable, trading decisions must be based solely on observed stock prices SS. Hence the investor’s available information flow is the natural filtration 𝔽S=(ℱtS)t∈[0,T]\mathbb{F}^{S}=(\mathcal{F}^{S}\_{t})\_{t\in[0,T]} generated by SS. The set of admissible trading strategies is

|  |  |  |
| --- | --- | --- |
|  | 𝒜(w):={πis 𝔽S-adapted,Wtw,π,Z≥0∀t∈[0,T],∫0Tπs2ds<∞}.\displaystyle\mathcal{A}(w):=\Big\{\pi\ \text{is $\mathbb{F}^{S}$-adapted},{W^{w,\pi,Z}\_{t}}\geq 0\ \forall t\in[0,T],\ \int\_{0}^{T}\pi\_{s}^{2}ds<\infty\Big\}. |  |

Non-negativity of the wealth trajectory prevents bankruptcy and ensures that the utility functional U​(WTπ)U(W\_{T}^{\pi}) is evaluated inside the domain ℝ+\mathbb{R}\_{+} whenever the utility function is finite on the non-negative half-line.

We now show that uncertainty about ZZ induces a set of beliefs about the state process WπW^{\pi}, denoted by 𝔓\mathfrak{P}, thereby introducing ambiguity. In the ambiguity jargon 𝔓\mathfrak{P} is the set of models. Throughout, we adopt the common practice of distinguishing terminologically between probability models of beliefs about the state process, which are referred to as models, and probability models that account for uncertainty about ZZ, which are referred to as priors.

For every Z∈𝒮Z\in\mathcal{S} and initial wealth w>0w>0, the stochastic differential equation ([3.3](#S3.E3 "In 3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) admits a unique strong solution Ww,π,ZW^{w,\pi,Z}. By viewing Ww,π,ZW^{w,\pi,Z} as a map from Ω\Omega to itself, we define the probability measure ℙZ\mathbb{P}^{Z} by ℙZ:=ℙ∘(Ww,π,Z)−1\mathbb{P}^{Z}\;:=\;\mathbb{P}\circ\bigl(W^{w,\pi,Z}\bigr)^{-1}. Given Z∈𝒮Z\in\mathcal{S}, we introduce

|  |  |  |
| --- | --- | --- |
|  | 𝔓:={ℙZ:Z∈𝒮}.\mathfrak{P}:=\{\mathbb{P}^{Z}:Z\in\mathcal{S}\}. |  |

Each realization of Z∈𝒮Z\in\mathcal{S} determines a unique probability law of the process WπW^{\pi}, which is seen by the investor as a plausible description of how the process WπW^{\pi} will evolve. If ZZ is certain, then the set 𝔓\mathfrak{P} is a singleton and there is no ambiguity, i.e., no uncertainty about probabilities. In contrast, if ZZ is a non-constant random variable, we have ambiguity.
In the remainder, we state the standard assumption that

###### Assumption 3.1.

All probability measures ℙZ\mathbb{P}^{Z}, Z∈𝒮Z\in\mathcal{S}, are absolutely continuous with respect to a reference measure ℙ0\mathbb{P}\_{0}.

In particular, if 𝒫\mathcal{P} is a two-point prior, then Assumption [3.1](#S3.Thmassumption1 "Assumption 3.1. ‣ 3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") is trivially satisfied by Girsanov’s theorem.

Following Klibanoff et al. ([2005](#bib.bib75 "A smooth model of decision making under ambiguity")), an ambiguity-averse investor chooses π∈𝒜​(w)\pi\in\mathcal{A}(w) so as to maximise the certainty equivalent, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπ∈𝒜​(w)ϕ−1​(∫𝒮ϕ​(𝔼ℙZ​[U​(WTπ)])​𝑑𝒫​(z)),\sup\_{\pi\in\mathcal{A}(w)}\phi^{-1}\Bigl(\int\_{\mathcal{S}}\phi\bigl(\mathbb{E}^{\mathbb{P}^{Z}}[U(W\_{T}^{\pi})]\bigr)d\mathcal{P}(z)\Bigr), |  | (3.4) |

where 𝔼ℙZ\mathbb{E}^{\mathbb{P}^{Z}} is the expectation operator with respect to ℙZ\mathbb{P}^{Z}. Here, ϕ:ℝ→ℝ\phi:\mathbb{R}\to\mathbb{R} is non-decreasing, and either strictly concave (ambiguity-averse) or linear (ambiguity-neutral), and UU is the utility function of terminal wealth.

###### Definition 3.1 (Utility function).

A *utility function* is a mapping U:(0,∞)→ℝU:(0,\infty)\to\mathbb{R} satisfying

1. (i)

   UU is non-constant, increasing, and upper semicontinuous;
2. (ii)

   The growth condition

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | limx→∞U​(x)x=0;\lim\_{x\to\infty}\frac{U(x)}{x}=0; |  | (3.5) |
3. (iii)

   U​(0):=limx↓0U​(x)U(0):=\lim\_{x\downarrow 0}U(x) and the finite limiting utility at infinity U​(∞):=limx↑∞U​(x)>−∞U(\infty):=\lim\_{x\uparrow\infty}U(x)>-\infty.

Here, we do not assume UU to be concave or continuous. If UU is concave, ([3.5](#S3.E5 "In item (ii) ‣ Definition 3.1 (Utility function). ‣ 3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) is equivalent to the Inada condition limx→∞U′​(x)=0\lim\_{x\to\infty}U^{\prime}(x)=0.
Condition ([3.5](#S3.E5 "In item (ii) ‣ Definition 3.1 (Utility function). ‣ 3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) rules out linear utility and ensures that expected utility is finite even under unbounded upside potential of the wealth process. Moreover, condition ([3.5](#S3.E5 "In item (ii) ‣ Definition 3.1 (Utility function). ‣ 3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) and the assumption U​(∞)>−∞U(\infty)>-\infty imply that there is always a concave function Uc:ℝ+→ℝU\_{c}:\mathbb{R}\_{+}\to\mathbb{R} satisfying Uc≥UU\_{c}\geq U (see Reichlin ([2013](#bib.bib58 "Utility maximization with a given pricing measure when the utility is not necessarily concave"))).

Works on continuous-time smooth ambiguity preferences with learning, such as Bäuerle and Mahayni ([2024](#bib.bib33 "Optimal investment in ambiguous financial markets with learning")) and Guan et al. ([2025b](#bib.bib49 "Equilibrium portfolio selection for smooth ambiguity preferences")), typically assume a concave utility function. Our goal is more general: we allow for non-concave preferences, including those induced by payoff structures that are nonlinear in terminal wealth, such as the option-based compensation schemes originally studied by Carpenter ([2000](#bib.bib61 "Does option compensation increase managerial risk appetite?")). These contracts generate effective non-concavities even when the underlying utility function is concave (e.g., power utility). To reach this goal, we shall rely on the concavification principle.

###### Definition 3.2 (Concave envelope).

The *concave envelope* UcU\_{c} of UU is the smallest concave function Uc:ℝ+→ℝU\_{c}:\mathbb{R}\_{+}\to\mathbb{R} such that Uc​(x)≥U​(x)U\_{c}(x)\geq U(x) for all x∈ℝ+x\in\mathbb{R}\_{+}.

In Section [5](#S5 "5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"), we show that the non-concave utility UU can be replaced by its concave envelope UcU\_{c}, thereby transforming the nonconcave utility maximization problem to a concave one. Before such a step, we need to reformulate the ambiguity-averse utility maximization problem so that it becomes time consistent.

## 4 Making Smooth Ambiguity Choices Time Consistent

To obtain time-consistent preferences with ambiguity, we start from the nested functional

|  |  |  |
| --- | --- | --- |
|  | Γ​(U,WTπ,ϕ)=ϕ−1​(∫𝒮ϕ​(𝔼ℙZ​[U​(WTπ)])​𝑑𝒫​(z))\Gamma(U,W\_{T}^{\pi},\phi)=\phi^{-1}\!\Bigl(\int\_{\mathcal{S}}\,\phi\bigl(\mathbb{E}^{\mathbb{P}^{Z}}[\,U(W\_{T}^{\pi})\,]\bigr)d\mathcal{P}(z)\Bigr) |  |

that appears in ([3.4](#S3.E4 "In 3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")). The functional Γ​(U,WTπ,ϕ)\Gamma(U,W\_{T}^{\pi},\phi) is, in fact, a special case of the class of uncertainty averse preferences proposed by Cerreia-Vioglio et al. ([2011c](#bib.bib47 "Uncertainty averse preferences")). A relevant result in that work is that they obtain a preference representation in terms of quasiconcave utility functionals by relaxing the independence axiom, i.e., the coordinate independence axiom within the Savage setting. They also discuss that this is equivalent to assuming independence only at the level of risk. The key technical aspect relevant to our work is that such a preference representation enables one to express the composition “ϕ−1​(∫ϕ​(⋅)​𝑑𝒫)\phi^{-1}(\int\phi(\cdot)d\mathcal{P})” as a minimization problem over a set of alternative equivalent probability measures (priors) on the drift parameter space 𝒮\mathcal{S}. This reformulation then enables the transformation of the ambiguity-averse problem into a max-min formulation, as we show next.

Let ℳ​(𝒮)\mathcal{M}(\mathcal{S}) denote the space of Borel probability measures on the compact metric space 𝒮\mathcal{S}, equipped with the weak topology. Intuitively, an element 𝒬∈ℳ​(𝒮)\mathcal{Q}\in\mathcal{M}(\mathcal{S}) represents a prior, that is, a belief about the parameter ZZ. As in Klibanoff et al. ([2005](#bib.bib75 "A smooth model of decision making under ambiguity")), 𝒬\mathcal{Q} may be viewed as a “second order probability” over the first order probabilities (models) ℙZ\mathbb{P}^{Z}. The prior 𝒫\mathcal{P} belongs to ℳ​(𝒮).\mathcal{M}(\mathcal{S}). For each ZZ, the market (state process WπW^{\pi}) is governed by the model ℙZ\mathbb{P}^{Z} introduced in Section [3](#S3 "3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"). For any 𝒬∈ℳ​(𝒮)\mathcal{Q}\in\mathcal{M}(\mathcal{S}), we denote by ℙ𝒬\mathbb{P}^{\mathcal{Q}} the probability measure on ℬ​(𝒮)×ℱ\mathcal{B}(\mathcal{S})\times\mathcal{F} defined by

|  |  |  |
| --- | --- | --- |
|  | ℙ𝒬​(A):=∫𝒮∫Ω𝟏A​(z,ω)​𝑑ℙZ​(ω)​𝑑𝒬​(z),\mathbb{P}^{\mathcal{Q}}(A)\;:=\;\int\_{\mathcal{S}}\!\int\_{\Omega}\mathbf{1}\_{A}(z,\omega)\,d\mathbb{P}^{Z}(\omega)\,d\mathcal{Q}(z), |  |

for any A∈ℬ​(𝒮)⊗ℱA\in\mathcal{B}(\mathcal{S})\otimes\mathcal{F}, and by 𝔼ℙ𝒬​[⋅]\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[\cdot] the corresponding expectation operator.

Combining Theorem 7 of Cerreia-Vioglio et al. ([2011c](#bib.bib47 "Uncertainty averse preferences")) and Theorem 6 of Drapeau and Kupper ([2013](#bib.bib65 "Risk preferences and their robust representation")), we can state the following proposition.

###### Proposition 4.1 (Robust representation form of smooth ambiguity preferences).

Let ϕ:ℝ→ℝ\phi:\mathbb{R}\to\mathbb{R} be a proper, concave, non-decreasing, and upper semi-continuous function. Then the optimisation problem ([3.4](#S3.E4 "In 3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπ∈𝒜​(w)inf𝒬∈ℳ​(𝒮)R​(𝒬,𝔼ℙ𝒬​[U​(WTπ)]),\sup\_{\pi\in\mathcal{A}(w)}\;\inf\_{\mathcal{Q}\in\mathcal{M}(\mathcal{S})}R\bigl(\mathcal{Q},\,\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[U(W\_{T}^{\pi})]\bigr), |  | (4.1) |

where R:ℳ​(𝒮)×ℝ→ℝR:\mathcal{M}(\mathcal{S})\times\mathbb{R}\to\mathbb{R} is uniquely determined by ϕ\phi and satisfies:

1. (i)

   R​(𝒬,⋅)R(\mathcal{Q},\cdot) is non-decreasing and right-continuous for each fixed 𝒬\mathcal{Q};
2. (ii)

   RR is jointly quasi-convex in (𝒬,s)(\mathcal{Q},s);
3. (iii)

   lims→∞R​(𝒬1,s)=lims→∞R​(𝒬2,s)\displaystyle\lim\_{s\to\infty}R(\mathcal{Q}^{1},s)=\lim\_{s\to\infty}R(\mathcal{Q}^{2},s) for all
   𝒬1,𝒬2∈ℳ​(𝒮)\mathcal{Q}^{1},\mathcal{Q}^{2}\in\mathcal{M}(\mathcal{S});
4. (iv)

   The upper envelope
   R+​(𝒬,s):=sups′<sR​(𝒬,s′)R^{+}(\mathcal{Q},s):=\sup\_{s^{\prime}<s}R(\mathcal{Q},s^{\prime})
   is lower semi-continuous in 𝒬\mathcal{Q}.

The robust representation in ([4.1](#S4.E1 "In Proposition 4.1 (Robust representation form of smooth ambiguity preferences). ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) rewrites the original nested expectation as a max-min optimization problem, where the inner infimum captures the robust adjustment of beliefs over ZZ, and the outer supremum reflects the optimal investment strategy under the resulting worst-case prior. Note that this type of robust representation is also used by Mazzon and Tankov ([2024](#bib.bib66 "Optimal stopping and divestment timing under scenario ambiguity and learning")) in the context of optimal stopping.

We next show that the ambiguity-averse max-min problem in ([4.1](#S4.E1 "In Proposition 4.1 (Robust representation form of smooth ambiguity preferences). ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) can be equivalently represented as a min-max problem. This equivalence follows from the existence of a saddle point and implies that the decision maker behaves as if she were ambiguity-neutral under an endogenously distorted belief. To allow this interchange, we need some further regularity conditions on the penalty function RR.

###### Assumption 4.1.

One of the following conditions holds:

1. (i)

   R​(𝒬,⋅)R(\mathcal{Q},\cdot) is continuous on ℝ\mathbb{R} for every 𝒬∈ℳ​(𝒮)\mathcal{Q}\in\mathcal{M}(\mathcal{S});
2. (ii)

   R​(𝒬,⋅)R(\mathcal{Q},\cdot) is continuous on (0,∞)(0,\infty) for every 𝒬∈ℳ​(𝒮)\mathcal{Q}\in\mathcal{M}(\mathcal{S}), and 𝔼ℙ𝒬​[U​(WTπ)]>0\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[U(W\_{T}^{\pi})]>0 for all Z∈𝒮Z\in\mathcal{S}.

These conditions hold in most practical settings and can be readily verified in specific examples (see below). We then prove that exchanging the supremum and the infimum in ([4.1](#S4.E1 "In Proposition 4.1 (Robust representation form of smooth ambiguity preferences). ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) solves the same decision problem — see Appendix [B.1](#A2.SS1 "B.1 Proof of Theorem 4.1 ‣ Appendix B Technical Proofs ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").—

###### Theorem 4.1.

Let ϕ\phi satisfy the assumptions of Proposition [4.1](#S4.Thmproposition1 "Proposition 4.1 (Robust representation form of smooth ambiguity preferences). ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") and Assumption [4.1](#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") hold. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπ∈𝒜​(w)inf𝒬∈ℳ​(𝒮)R​(𝒬,𝔼ℙ𝒬​[U​(WTπ)])=inf𝒬∈ℳ​(𝒮)supπ∈𝒜​(w)R​(𝒬,𝔼ℙ𝒬​[U​(WTπ)]).\displaystyle\sup\_{\pi\in\mathcal{A}(w)}\inf\_{\mathcal{Q}\in\mathcal{M}(\mathcal{S})}R(\mathcal{Q},\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[U(W\_{T}^{\pi})])=\inf\_{\mathcal{Q}\in\mathcal{M}(\mathcal{S})}\sup\_{\pi\in\mathcal{A}(w)}R(\mathcal{Q},\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[U(W\_{T}^{\pi})]). |  | (4.2) |

This result allows us to solve the Bayesian portfolio problem conditional on a given prior 𝒬\mathcal{Q} first. In a next step, we identify the optimal prior 𝒬∗\mathcal{Q}^{\*} arising from the outer optimization problem. The optimal strategy π∗\pi^{\*} is then characterized as the solution to the Bayesian problem evaluated under 𝒬∗\mathcal{Q}^{\*}.

The functional in ([4.2](#S4.E2 "In Theorem 4.1. ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) accommodates in principle any choice of ambiguity aggregator ϕ\phi and penalty RR, allowing great flexibility in the problem formulation.
To illustrate, we consider the families of aggregators which are the most common in the ambiguity-literature (see, e.g., Taboga ([2005](#bib.bib68 "Portfolio selection with two-stage preferences")); Gollier ([2011](#bib.bib16 "Portfolio choices and asset prices: the comparative statics of ambiguity aversion")); Ju and Miao ([2012](#bib.bib52 "Ambiguity, learning, and asset returns"))) and for each case, we indicate which part of Assumption [4.1](#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") is satisfied, thereby showing that the regularity requirements are, in practice, harmless. It is also worth noting that 𝒫\mathcal{P} and 𝒬\mathcal{Q} in the following example must be equivalent probability measures; otherwise, the Radon-Nikodym derivative is not well defined.

1. 1.

   Power aggregator (λ<1,λ≠0)(\lambda<1,\ \lambda\neq 0): ϕ​(x)=xλ/λ\displaystyle\phi(x)=x^{\lambda}/\lambda for x>0x>0.
   The associated penalty is

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | R​(𝒬,s)=(s)+​(𝔼𝒫​[(d​𝒬d​𝒫)λλ−1])1−λλ,R(\mathcal{Q},s)=(s)^{+}\,\Bigl(\mathbb{E}^{\mathcal{P}}\!\Bigl[\bigl(\tfrac{d\mathcal{Q}}{d\mathcal{P}}\bigr)^{\frac{\lambda}{\lambda-1}}\Bigr]\Bigr)^{\!\frac{1-\lambda}{\lambda}}, |  | (4.3) |

   where 𝔼𝒫\mathbb{E}^{\mathcal{P}} denotes the expectation with respect to 𝒫\mathcal{P} and (⋅)+=max⁡{⋅,0}(\cdot)^{+}=\max\{\cdot,0\}.
   Here, the exponent 1−λ1-\lambda is the relative ambiguity aversion (RAA) parameter, which measures the degree of ambiguity aversion; the limit λ→−∞\lambda\to-\infty yields max-min preferences, while λ→1\lambda\to 1 corresponds to ambiguity neutrality.
   For any fixed 𝒬\mathcal{Q} the map s↦R​(𝒬,s)s\mapsto R(\mathcal{Q},s) is affine on (0,∞)(0,\infty) and thus continuous there.
   Consequently, Assumption [4.1](#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") (ii) is satisfied whenever 𝔼ℙ𝒬​[U​(WTπ)]>0\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[U(W\_{T}^{\pi})]>0. The optimal linear-payoff problem in Bäuerle and Mahayni ([2024](#bib.bib33 "Optimal investment in ambiguous financial markets with learning")) involves a power aggregator. Their expression is derived using the dual representation of the LpL^{p} norm, while our formulation relies on a general robust representation (see ([4.1](#S4.E1 "In Proposition 4.1 (Robust representation form of smooth ambiguity preferences). ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"))).
2. 2.

   Logarithmic aggregator:
   ϕ​(x)=log⁡x\phi(x)=\log x for x>0x>0. The penalty takes the exponential of relative entropy:

   |  |  |  |
   | --- | --- | --- |
   |  | R​(𝒬,s)=(s)+​exp⁡(−𝔼𝒫​[log⁡d​𝒬d​𝒫]).R(\mathcal{Q},s)=(s)^{+}\,\exp\!\left(-\mathbb{E}^{\mathcal{P}}\left[\log\!\frac{d\mathcal{Q}}{d\mathcal{P}}\right]\right). |  |

   This form connects ambiguity aversion to the Kullback-Leibler divergence, penalising beliefs that are far from the prior. Because the logarithm is continuous and the inside expectation is finite for every s∈ℝs\in\mathbb{R}, the map s↦R​(𝒬,s)s\mapsto R(\mathcal{Q},s) is continuous on the entire real line.
   Hence Assumption [4.1](#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") (i) holds automatically.
3. 3.

   Exponential aggregator:
   ϕ​(x)=−e−γ​x\phi(x)=-e^{-\gamma x} with γ>0\gamma>0. Then the penalty function is

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | R​(𝒬,s)=s+1γ​𝔼𝒬​[log⁡d​𝒬d​𝒫],R(\mathcal{Q},s)=s+\frac{1}{\gamma}\,\mathbb{E}^{\mathcal{Q}}\left[\log\!\frac{d\mathcal{Q}}{d\mathcal{P}}\right], |  | (4.4) |

   where 𝔼𝒬\mathbb{E}^{\mathcal{Q}} denotes expectation with respect to 𝒬\mathcal{Q}. The higher the γ\gamma (absolute ambiguity aversion parameter (AAA)), the more ambiguity-averse the agent is. This case yields an entropic penalty, often encountered in robust control and exponential utility frameworks. Because the logarithm is continuous and the inside expectation is finite for every s∈ℝs\in\mathbb{R}, the map s↦R​(𝒬,s)s\mapsto R(\mathcal{Q},s) is continuous on the entire real line. Hence Assumption [4.1](#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") (i) holds automatically. Indeed, this is the standard representation for the entropic risk measure (see, e.g., Föllmer and Knispel ([2011](#bib.bib44 "Entropic risk measures: coherence vs. convexity, model ambiguity and robust large deviations"))). Moreover,

   |  |  |  |
   | --- | --- | --- |
   |  | inf𝒬∈ℳ​(𝒮)(𝔼ℙ𝒬​[U​(WTπ)]+1γ​𝔼𝒬​[log⁡d​𝒬d​𝒫])\inf\_{\mathcal{Q}\in\mathcal{M}(\mathcal{S})}\bigg(\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[U(W\_{T}^{\pi})]+\frac{1}{\gamma}\,\mathbb{E}^{\mathcal{Q}}\left[\log\!\frac{d\mathcal{Q}}{d\mathcal{P}}\right]\bigg) |  |

   is actually of variational form introduced by Maccheroni et al. ([2006](#bib.bib48 "Ambiguity aversion, robustness, and the variational representation of preferences")).

We note that the penalty functions induced by all standard smooth-ambiguity aggregators satisfy the continuity requirements in Assumption [4.1](#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"), and in particular the power, logarithmic, and exponential aggregators illustrated above, satisfy the assumptions of Theorem [4.1](#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"). The minimax interchange is thus justified for the specifications most frequently used in applications. It is worth noting that, under commonly used choices of the aggregator ϕ\phi, the functional RR is linear in 𝔼ℙ𝒬​[⋅]\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[\cdot]. As a result, the problem reduces to a time-consistent Bayesian adaptive control problem, which can be solved using nonlinear filtering and martingale methods.

The results have a notable implication: the inner problem in ([4.2](#S4.E2 "In Theorem 4.1. ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) is of the form

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒜​(w)R​(𝒬,𝔼ℙ𝒬​[U​(WTπ)]).\sup\_{\pi\in\mathcal{A}(w)}R(\mathcal{Q},\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[U(W\_{T}^{\pi})]). |  |

which, under linearity of R​(Q,s)R(Q,s) corresponds to that of an ambiguity-neutral decision-maker. Specifically, it becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπ∈𝒜​(w)𝔼ℙ𝒬​[U​(WTπ)].\sup\_{\pi\in\mathcal{A}(w)}\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[U(W\_{T}^{\pi})]. |  | (4.5) |

This is the case of the three aggregator functions illustrated above. The approach then transforms the problem into two main steps. In the first, we solve a classical Bayesian decision problem in which ambiguity does not play any role and prior 𝒬\mathcal{Q} is updated through observations of market prices. This step has the theoretical implication of making the problem dynamically consistent. It also has the practical advantage that ambiguity-neutral problems are, in general, easier to solve than the corresponding ambiguous counterparts. Ambiguity preferences enter only through the outer minimization over priors. Thus, one is free to select alternative forms of the ambiguity functional and apply them to the solution. Overall, this points to greater tractability and modeling flexibility.

In the next section, we apply the approach to the study of the class of decision delegated portfolio management problems. Our goal is not only to characterize the optimal investment strategies, but also to identify the endogenous prior induced by the investor’s ambiguity preferences.

## 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences

In Section [5.1](#S5.SS1 "5.1 The Theoretical Steps ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"), we present the steps implied by Proposition [4.1](#S4.Thmproposition1 "Proposition 4.1 (Robust representation form of smooth ambiguity preferences). ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") and Theorem [4.1](#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"), which have a general validity beyond delegated portfolio management. In Section [5.2](#S5.SS2 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"), we specify the steps to delegated portfolio management.

### 5.1 The Theoretical Steps

Given Problem ([3.4](#S3.E4 "In 3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")), we outline the analysis procedure in the following steps:

1. Step 1:

   Apply Proposition [4.1](#S4.Thmproposition1 "Proposition 4.1 (Robust representation form of smooth ambiguity preferences). ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"), to obtain a robust representation of the ambiguity-averse problem in the form of a max–min optimization.
2. Step 2:

   Apply Theorem [4.1](#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"), to turn the max–min problem into a min–max problem.
3. Step 3:

   Choose a specification of the aggregator ϕ\phi, such that the functional RR is linear in its second argument, namely in 𝔼ℙ𝒬​[⋅]\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[\cdot].
4. Step 4:

   Conditional on a given prior 𝒬\mathcal{Q} solve the resulting ambiguity-neutral problem ([4.5](#S4.E5 "In 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) using nonlinear filtering and martingale methods, and derive the optimal trading strategy π∗​(𝒬)\pi^{\*}(\mathcal{Q}).
5. Step 5:

   We then solve the outer optimization problem over the set of priors to identify the worst-case prior 𝒬∗\mathcal{Q}^{\*}. The optimal trading strategy is obtained by evaluating π∗​(𝒬)\pi^{\*}(\mathcal{Q}) at 𝒬=𝒬∗\mathcal{Q}=\mathcal{Q}^{\*}.

### 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs

Delegated fund managers are often compensated through convex schemes, most prominently option-like contracts. In such contracts the payment consists of a fixed base fee plus a performance-based component that resembles a call option written on the managed fund and struck at a benchmark value at maturity (see, e.g., Carpenter ([2000](#bib.bib61 "Does option compensation increase managerial risk appetite?"))). We study the optimal investment policy of a manager who faces ambiguity about the return of a risky asset and is compensated through an option-based payoff, within the framework of smooth ambiguity preferences.
This extends Carpenter ([2000](#bib.bib61 "Does option compensation increase managerial risk appetite?")) by allowing for ambiguity and lets us quantify how ambiguity aversion shapes portfolio choices.

Specifically, the manager’s payoff at time TT is δ∈(0,1]\delta\in(0,1] shares of a call option on the fund with strike KK, plus a constant base C≥0C\geq 0. The payoff function gg is

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(WTπ):=δ​(WTπ−K)++C.g(W\_{T}^{\pi}):=\delta(W\_{T}^{\pi}-K)^{+}+C. |  | (5.1) |

The manager is ambiguity-averse with respect to the uncertain return of the risky asset and evaluates terminal wealth utility using a smooth ambiguity functional. Moreover, she updates her prior based on the information of stock prices. Her decision problem is to determine

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπ∈𝒜​(w)ϕ−1​(∫𝒮ϕ​(𝔼ℙZ​[u​(g​(WTπ))])​𝑑𝒫​(z)),\sup\_{\pi\in\mathcal{A}(w)}\phi^{-1}\left(\int\_{\mathcal{S}}\phi\Bigl(\mathbb{E}^{\mathbb{P}^{Z}}\bigl[u\bigl(g(W\_{T}^{\pi})\bigr)\bigr]\Bigr)d\mathcal{P}(z)\right), |  | (5.2) |

which is a special case of ([3.4](#S3.E4 "In 3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) with U​(⋅)=u∘g​(⋅)U(\cdot)=u\!\circ\!g(\cdot).

![Refer to caption](2603.08552v1/x1.png)


Figure 1: Manager’s payoff function with α=0.5,δ=0.2,K=1,C=0.02\alpha=0.5,\delta=0.2,K=1,C=0.02.

![Refer to caption](2603.08552v1/x2.png)


Figure 2: Manager’s original and concavified objective functions with α=0.5,δ=0.2,K=1,C=0.02\alpha=0.5,\delta=0.2,K=1,C=0.02.

###### Example 5.1.

Consider a power utility function of the form

|  |  |  |
| --- | --- | --- |
|  | u​(x)=xα/α,u(x)=x^{\alpha}/\alpha, |  |

where x∈[0,∞)x\in[0,\infty), with α<1\alpha<1, α≠0\alpha\neq 0, so that

|  |  |  |
| --- | --- | --- |
|  | RRA:=1−α,\mathrm{RRA}:=1-\alpha, |  |

is the coefficient of relative risk aversion, together with the payoff function g​(⋅)g(\cdot) given in ([5.2](#S5.E2 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")). Figures [2](#F2 "Figure 2 ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") and [2](#F2 "Figure 2 ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") display the manager’s payoff function g​(⋅)g(\cdot) (right panel, dotted red line), the induced utility u∘g​(⋅)u\circ g(\cdot) (left panel, solid blue line), and its concave envelope (left panel, dashed green line) for selected parameter values. The figures illustrate that the payoff function is nonlinear and that the induced utility U​(⋅)=u∘g​(⋅)U(\cdot)=u\circ g(\cdot) is not globally concave. Hence, the specification satisfies Definition [3.1](#S3.Thmdefinition1 "Definition 3.1 (Utility function). ‣ 3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").

We now adopt the steps highlighted in Section [5.1](#S5.SS1 "5.1 The Theoretical Steps ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") to solve the non-concave portfolio management problem in ([5.2](#S5.E2 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")). In Step 1, we apply Proposition [4.1](#S4.Thmproposition1 "Proposition 4.1 (Robust representation form of smooth ambiguity preferences). ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") to obtain the robust representation:

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒜​(w)inf𝒬∈ℳ​(𝒮)R​(𝒬,𝔼ℙ𝒬​[u​(g​(WTπ))]).\sup\_{\pi\in\mathcal{A}(w)}\;\inf\_{\mathcal{Q}\in\mathcal{M}(\mathcal{S})}R\bigl(\mathcal{Q},\,\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[u(g(W\_{T}^{\pi}))]\bigr). |  |

In Step 2, by Theorem [4.1](#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") we obtain the following equivalent min-max optimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf𝒬∈ℳ​(𝒮)supπ∈𝒜​(w)R​(𝒬,𝔼ℙ𝒬​[u​(g​(WTπ))]).\displaystyle\inf\_{\mathcal{Q}\in\mathcal{M}(\mathcal{S})}\sup\_{\pi\in\mathcal{A}(w)}R(\mathcal{Q},\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[u(g(W\_{T}^{\pi}))]). |  | (5.3) |

In Step 3, regarding the choice of the function ϕ\phi, we focus on two economically relevant cases, the power–power case in which both ϕ\phi and uu are CRRA, and the exponential–power in which ϕ\phi is exponential and uu is CRRA. These two specifications are widely used in the literature, including one-period asset allocation problems (e.g., Taboga ([2005](#bib.bib68 "Portfolio selection with two-stage preferences")); Gollier ([2011](#bib.bib16 "Portfolio choices and asset prices: the comparative statics of ambiguity aversion"))) and consumption-based asset pricing models (e.g., Ju and Miao ([2012](#bib.bib52 "Ambiguity, learning, and asset returns")); Collard et al. ([2018](#bib.bib53 "Ambiguity and the historical equity premium"))).

Formally, in the power-power case, we write ϕ​(x)=xλλ\phi(x)=\frac{x^{\lambda}}{\lambda}, λ<1\lambda<1, λ≠0\lambda\neq 0, and u​(x)=xααu(x)=\frac{x^{\alpha}}{\alpha}, α<1\alpha<1, α≠0\alpha\neq 0. Then, by Equation ([4.3](#S4.E3 "In item 1 ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")), the decision-problem ([5.3](#S5.E3 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf𝒬∈ℳ​(𝒮)supπ∈𝒜​(w)(𝔼ℙ𝒬​[u​(g​(WTπ))])+​(𝔼𝒫​[(d​𝒬d​𝒫)λλ−1])1−λλ.\inf\_{\mathcal{Q}\in\mathcal{M}(\mathcal{S})}\sup\_{\pi\in\mathcal{A}(w)}\;\bigg(\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[u(g(W\_{T}^{\pi}))]\bigg)^{+}\left(\mathbb{E}^{\mathcal{P}}\left[\left(\tfrac{d\mathcal{Q}}{d\mathcal{P}}\right)^{\frac{\lambda}{\lambda-1}}\right]\right)^{\!\frac{1-\lambda}{\lambda}}. |  | (5.4) |

In the exponential-power case, we write ϕ​(x)=−e−γ​x\phi(x)=-e^{-\gamma x}, γ>0\gamma>0, and u​(x)=xααu(x)=\frac{x^{\alpha}}{\alpha}, α<1\alpha<1, α≠0\alpha\neq 0. Then, by Equation ([4.4](#S4.E4 "In item 3 ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")), the decision-problem ([5.3](#S5.E3 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf𝒬∈ℳ​(𝒮)supπ∈𝒜​(w){𝔼ℙ𝒬​[u​(g​(WTπ))]+1γ​𝔼𝒬​[log⁡d​𝒬d​𝒫]}.\inf\_{\mathcal{Q}\in\mathcal{M}(\mathcal{S})}\sup\_{\pi\in\mathcal{A}(w)}\;\bigg\{\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[u(g(W\_{T}^{\pi}))]+\frac{1}{\gamma}\,\mathbb{E}^{\mathcal{Q}}\left[\log\!\frac{d\mathcal{Q}}{d\mathcal{P}}\right]\bigg\}. |  | (5.5) |

Both ([5.4](#S5.E4 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) and ([5.5](#S5.E5 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) are linear in 𝔼ℙ𝒬​[u​(g​(WTπ))]\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[u(g(W\_{T}^{\pi}))]. This allows us to solve the ambiguity neutral problem, which now takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(w;𝒬):=supπ∈𝒜​(w)𝔼ℙ𝒬​[u​(g​(WTπ))].V(w;\mathcal{Q}):=\sup\_{\pi\in\mathcal{A}(w)}\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[u(g(W\_{T}^{\pi}))]. |  | (5.6) |

Technically, this is a Bayesian adaptive problem with a nonlinear payoff gg. In this respect, our approach parallels that of Bäuerle and Mahayni ([2024](#bib.bib33 "Optimal investment in ambiguous financial markets with learning")) for the linear payoff case, extending it to option-type payoffs. We then use stochastic filtering theory (e.g., Karatzas and Zhao ([2001](#bib.bib30 "Bayesian adaptive portfolio optimization")); Rieder and Bäuerle ([2005](#bib.bib31 "Portfolio optimization with unobservable markov-modulated drift process"))) to reduce the partial-information problem with an unknown expected return to one with an adapted (observable) drift. This is achieved by updating priors based on the observed price process (see Appendix [A.1](#A1.SS1 "A.1 Filtering Arguments ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") for details). We subsequently solve the resulting complete-information problem using martingale methods (e.g., (Karatzas and Shreve, [1998a](#bib.bib72 "Methods of mathematical finance"), Ch. 3)) combined with the concavification principle.

Now we come to Step 4, related to the financial modeling part of the problem.
Define the market price of risk by Θ=(Z−r)/σ\Theta=(Z-r)/\sigma, and denote its realization by θ=(z−r)/σ\theta=(z-r)/\sigma.
Let II be the inverse of the marginal utility function u′u^{\prime}, given by I​(x):=x1α−1I(x):=x^{\frac{1}{\alpha-1}}, and

|  |  |  |
| --- | --- | --- |
|  | ξT:=e−r​TF​(T,YT;𝒬)\xi\_{T}:=\frac{e^{-rT}}{F(T,Y\_{T};\mathcal{Q})} |  |

denote the state-price density, where YtY\_{t} is a ℙ\mathbb{P}-Brownian motion with drift Θ\Theta, and F​(t,y;𝒬):=∫𝒮exp⁡{θ​y−12​θ2​t}​𝒬​(d​θ).F(t,y;\mathcal{Q}):=\int\_{\mathcal{S}}\exp\!\left\{\theta y-\tfrac{1}{2}\theta^{2}t\right\}\,\mathcal{Q}(d\theta). The state-price density ξT​(ω)\xi\_{T}(\omega) represents the (discounted) price at t=0t=0 of a unit payoff received in a given state ω\omega at time TT, reflecting both time discounting and the belief-adjusted pricing of risk. Here, a state refers to a realization of the underlying market uncertainty at time TT. A large ξT\xi\_{T} means that a unit payoff delivered in that state is expensive today: investors must pay more now to receive one unit of payoff there, which is why such states are interpreted as unfavorable states (see Carpenter ([2000](#bib.bib61 "Does option compensation increase managerial risk appetite?")) for a detailed discussion).

We then prove the following result regarding the optimal terminal wealth (denoted by WT∗W^{\*}\_{T}) and optimal investment strategy (denoted by πt∗\pi\_{t}^{\ast}) for an ambiguity neutral decision-maker (see Appendix [B.2](#A2.SS2 "B.2 Proof of Theorem 5.1 ‣ Appendix B Technical Proofs ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") for the proof).

###### Theorem 5.1.

With the above definitions, we have the following:

1. (i)

   The optimal terminal wealth for the ambiguity-neutral decision-problem in ([5.6](#S5.E6 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) is

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | WT∗​(κw∗,ξT)=𝒳​(κw∗​ξT)={h​(κw∗​ξT),0<ξT<y^κw∗,0,ξT≥y^κw∗,W^{\*}\_{T}(\kappa^{\*}\_{w},{\xi}\_{T})=\mathcal{X}(\kappa^{\*}\_{w}\xi\_{T})=\begin{cases}h(\kappa^{\*}\_{w}{\xi}\_{T}),\quad 0<{\xi}\_{T}<\frac{\widehat{y}}{\kappa^{\*}\_{w}},\\ 0,\quad\xi\_{T}\geq\frac{\widehat{y}}{\kappa^{\*}\_{w}},\end{cases} |  | (5.7) |

   where the function h​(x):=I​(x/δ)−Cδ+Kh(x):=\dfrac{I(x/\delta)-C}{\delta}+K with x∈[0,∞)x\in[0,\infty), and we recall that KK, δ\delta and CC are defined in ([5.1](#S5.E1 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")), and where the concavification point y^∈(0,δ​Cα−1)\widehat{y}\in(0,\delta C^{\alpha-1}) is the unique root of

   |  |  |  |
   | --- | --- | --- |
   |  | u​(g​(h​(y)))−u​(C)=y​h​(y).u(g(h(y)))-u(C)=yh(y). |  |
2. (ii)

   For any initial wealth w>0w>0, κ∗\kappa^{\*} is the unique root of the budget constraint

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼ℙ​[ξT​WT∗​(κ∗,ξT)]=w,\mathbb{E}^{\mathbb{P}}[\xi\_{T}W^{\*}\_{T}(\kappa^{\*},\xi\_{T})]=w, |  |

   where 𝔼ℙ\mathbb{E}^{\mathbb{P}} is the expectation with respect to ℙ\mathbb{P} and we write κw∗:=κ∗​(w)\kappa\_{w}^{\*}:=\kappa^{\*}(w) to emphasize its dependence on the initial wealth ww.
3. (iii)

   The optimal fraction invested in the stock at time 0<t≤T0<t\leq T for ([5.6](#S5.E6 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) is

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | πt∗Wt∗=−κw∗​e−r​Tσ​∫ℝ(𝒳)′​(κw∗​e−r​TF​(T,Yt+z;𝒬))​∇F​(T,Yt+z;𝒬)F​(T,Yt+z;𝒬)2​φT−t​(z)​𝑑z∫ℝ𝒳​(κw∗​e−r​TF​(T,Yt+z;𝒬))​φT−t​(z)​𝑑z.\frac{\pi\_{t}^{\*}}{W^{\*}\_{t}}=-\frac{\kappa^{\*}\_{w}e^{-rT}}{\sigma}\frac{\displaystyle\int\_{\mathbb{R}}(\mathcal{X})^{\prime}\!\left(\frac{\kappa^{\*}\_{w}e^{-rT}}{F(T,Y\_{t}+z;\mathcal{Q})}\right)\frac{\nabla F(T,Y\_{t}+z;\mathcal{Q})}{F(T,Y\_{t}+z;\mathcal{Q})^{2}}\varphi\_{T-t}(z)dz}{\displaystyle\int\_{\mathbb{R}}\mathcal{X}\!\left(\frac{\kappa^{\*}\_{w}e^{-rT}}{F(T,Y\_{t}+z;\mathcal{Q})}\right)\varphi\_{T-t}(z)\,dz}. |  | (5.8) |
4. (iv)

   The ambiguity-neutral value function at the optimum is

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | V​(w;𝒬)=∫ℝF​(T,z;𝒬)​u​(g​(𝒳​(e−r​T​κw∗F​(T,z;𝒬))))​φT​(z)​𝑑z.V(w;\mathcal{Q})=\int\_{\mathbb{R}}F(T,z;\mathcal{Q})\,u\!\left(g\!\left(\mathcal{X}\!\left(\frac{e^{-rT}\kappa^{\*}\_{w}}{F(T,z;\mathcal{Q})}\right)\right)\right)\varphi\_{T}(z)\,dz. |  | (5.9) |

   where φT\varphi\_{T} is the density of 𝒩​(0,T)\mathcal{N}(0,T).

A key qualitative implication of ([5.7](#S5.E7 "In item (i) ‣ Theorem 5.1. ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) is that the optimal terminal wealth is *discontinuous* in the state-price density ξT\xi\_{T} and exhibits an “all-or-nothing” structure: whenever ξT≥y^/κw∗\xi\_{T}\geq\widehat{y}/\kappa^{\*}\_{w}, the optimal terminal payoff is zero. Here, “zero payoff” means that the investor ends the horizon with zero terminal wealth in those states. In favorable financial scenarios (low ξT\xi\_{T}), the optimal trading policy resembles the classical Merton rule (see Merton ([1971](#bib.bib41 "Optimum consumption and portfolio rules in a continuous-time model"))). In sufficiently unfavorable scenarios (high ξT\xi\_{T}), however, the optimal terminal wealth collapses to zero. Economically, high ξT\xi\_{T} corresponds to states in which delivering one unit of terminal payoff is particularly costly in present-value terms. Under a call-type payoff, compensation is truncated below the performance threshold KK, so additional resources allocated to such states do not increase g​(WTπ)g(W\_{T}^{\pi}) and hence yield no marginal benefit. The optimal policy therefore does not hedge these expensive states and instead reallocates resources toward inexpensive, favorable states, consistent with Chen et al. ([2024](#bib.bib6 "On the equivalence between value-at-risk-and expected shortfall-based risk measures in non-concave optimization")).

Our framework subsumes both the frameworks of Bäuerle and Mahayni ([2024](#bib.bib33 "Optimal investment in ambiguous financial markets with learning")) and Carpenter ([2000](#bib.bib61 "Does option compensation increase managerial risk appetite?")). Setting K=0K=0, C=0C=0, and δ=1\delta=1 in ([5.1](#S5.E1 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) we recover the linear-payoff specification of Bäuerle and Mahayni ([2024](#bib.bib33 "Optimal investment in ambiguous financial markets with learning")). On the other hand, if ZZ is assumed to be a known constant, the optimal terminal wealth simplifies to

|  |  |  |  |
| --- | --- | --- | --- |
|  | WT∗​(κw∗,ξT)=𝒳​(κw∗​ξT)={h​(κw∗​ξT),0<ξT<y^κw∗,0,ξT≥y^κw∗,W^{\*}\_{T}(\kappa^{\*}\_{w},{\xi}\_{T})=\mathcal{X}(\kappa^{\*}\_{w}\xi\_{T})=\begin{cases}h(\kappa^{\*}\_{w}{\xi}\_{T}),\quad 0<{\xi}\_{T}<\frac{\widehat{y}}{\kappa^{\*}\_{w}},\\ 0,\quad\xi\_{T}\geq\frac{\widehat{y}}{\kappa^{\*}\_{w}},\end{cases} |  | (5.10) |

where ξT=exp⁡{−r​T−12​θ2​T−θ​WT}.\xi\_{T}=\exp\{-rT-\tfrac{1}{2}\theta^{2}T-\theta W\_{T}\}. This specification recovers Theorem 1 in Carpenter ([2000](#bib.bib61 "Does option compensation increase managerial risk appetite?")).

Finally (Step 5), we solve the outer optimization problem in ([5.3](#S5.E3 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) over the set of priors to identify the worst-case prior 𝒬∗\mathcal{Q}^{\*} under the two proposed specifications. We start with the power-power case.

###### Proposition 5.1 (Power–power specification).

When

|  |  |  |
| --- | --- | --- |
|  | ϕ​(x)=xλλ,with​λ<1,λ≠0,\phi(x)=\frac{x^{\lambda}}{\lambda},\ \text{with}\ \lambda<1,\lambda\neq 0, |  |

and

|  |  |  |
| --- | --- | --- |
|  | u​(x)=xαα,with​α<1,α≠0,u(x)=\frac{x^{\alpha}}{\alpha},\ \text{with}\ \alpha<1,\alpha\neq 0, |  |

the optimal investment strategy π∗\pi^{\*} satisfies ([5.8](#S5.E8 "In item (iii) ‣ Theorem 5.1. ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) with optimal prior 𝒬∗\mathcal{Q}^{\*} solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf𝒬∈ℳ​(𝒮)(V​(w;𝒬))+​(𝔼𝒫​[(d​𝒬d​𝒫)λλ−1])1−λλ=(V​(w;𝒬∗))+​(𝔼𝒫​[(d​𝒬∗d​𝒫)λλ−1])1−λλ,\displaystyle\inf\_{\mathcal{Q}\in\mathcal{M}(\mathcal{S})}\Big(V(w;\mathcal{Q})\Big)^{+}\left(\mathbb{E}^{\mathcal{P}}\left[\left(\tfrac{d\mathcal{Q}}{d\mathcal{P}}\right)^{\frac{\lambda}{\lambda-1}}\right]\right)^{\!\frac{1-\lambda}{\lambda}}=\Big(V(w;\mathcal{Q}^{\*})\Big)^{+}\left(\mathbb{E}^{\mathcal{P}}\left[\left(\tfrac{d\mathcal{Q^{\*}}}{d\mathcal{P}}\right)^{\frac{\lambda}{\lambda-1}}\right]\right)^{\!\frac{1-\lambda}{\lambda}}, |  | (5.11) |

where V​(w;𝒬)V(w;\mathcal{Q}) is given by ([5.9](#S5.E9 "In item (iv) ‣ Theorem 5.1. ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")).

Even though both our framework and Bäuerle and Mahayni ([2024](#bib.bib33 "Optimal investment in ambiguous financial markets with learning")) employ a power aggregator ϕ\phi to model ambiguity aversion and power utility uu to capture risk aversion, two key differences arise. First, we allow for a nonlinear payoff structure, which generates the endogenous “all-or-nothing” pattern in optimal terminal wealth. Such behavior does not arise in Bäuerle and Mahayni ([2024](#bib.bib33 "Optimal investment in ambiguous financial markets with learning")), where the payoff is linear and the objective remains concave. This nonlinearity yields new economic insights, as illustrated in Section [6](#S6 "6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"), particularly regarding how ambiguity aversion interacts with convex incentive contracts. Second, from a methodological perspective, we rely on a general robust representation rather than the dual representation of the LpL^{p} norm used in Bäuerle and Mahayni ([2024](#bib.bib33 "Optimal investment in ambiguous financial markets with learning")). This approach provides greater flexibility in the specification of ambiguity preferences and extends naturally to non-concave payoff environments.

We now consider the exponential-power specification.

###### Proposition 5.2 (Exponential–power specification).

When

|  |  |  |
| --- | --- | --- |
|  | ϕ​(x)=−e−γ​x,with​γ>0,\phi(x)=-e^{-\gamma x},\ \text{with}\ \gamma>0, |  |

and

|  |  |  |
| --- | --- | --- |
|  | u​(x)=xαα,with​α<1,α≠0,u(x)=\frac{x^{\alpha}}{\alpha},\ \text{with}\ \alpha<1,\alpha\neq 0, |  |

the optimal investment strategy π∗\pi^{\*} satisfies ([5.8](#S5.E8 "In item (iii) ‣ Theorem 5.1. ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) with optimal prior 𝒬∗\mathcal{Q}^{\*} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf𝒬∈ℳ​(𝒮){V​(w;𝒬)+1γ​𝔼𝒬​[log⁡d​𝒬d​𝒫]}={V​(w;𝒬∗)+1γ​𝔼𝒬∗​[log⁡d​𝒬∗d​𝒫]},\displaystyle\inf\_{\mathcal{Q}\in\mathcal{M}(\mathcal{S})}\bigg\{V(w;\mathcal{Q})+\frac{1}{\gamma}\,\mathbb{E}^{\mathcal{Q}}\left[\log\!\frac{d\mathcal{Q}}{d\mathcal{P}}\right]\bigg\}=\bigg\{V(w;\mathcal{Q}^{\*})+\frac{1}{\gamma}\,\mathbb{E}^{\mathcal{Q}^{\*}}\left[\log\!\frac{d\mathcal{Q}^{\*}}{d\mathcal{P}}\right]\bigg\}, |  | (5.12) |

where V​(w;𝒬)V(w;\mathcal{Q}) is given by ([5.9](#S5.E9 "In item (iv) ‣ Theorem 5.1. ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")).

Equations ([5.11](#S5.E11 "In Proposition 5.1 (Power–power specification). ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) and ([5.12](#S5.E12 "In Proposition 5.2 (Exponential–power specification). ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) imply that solving the original smooth ambiguity problem in ([5.2](#S5.E2 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) amounts to characterizing the optimal investment strategy in ([5.8](#S5.E8 "In item (iii) ‣ Theorem 5.1. ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) for a given prior 𝒬\mathcal{Q} and identifying the corresponding optimal prior 𝒬∗\mathcal{Q}^{\*}. Although we focus on two specific ambiguity aggregators, the structure of the formulation makes the framework readily extensible. Once the ambiguity-neutral benchmark in ([5.6](#S5.E6 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) is characterized, alternative ambiguity specifications can be chosen by the analyst and incorporated without difficulty. This modular structure represents a key methodological advantage, enabling different ambiguity attitudes to be imposed in a tractable and systematic manner.

Obtaining a closed-form expression for 𝒬∗\mathcal{Q}^{\*} is generally out of reach due to the difficulty of determining V​(w;𝒬)V(w;\mathcal{Q}) in ([5.9](#S5.E9 "In item (iv) ‣ Theorem 5.1. ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")). However, the solution can be found numerically. In the next section, we use computational experiments to analyze how ambiguity aversion affects the optimal investment strategies.

## 6 Numerical Experiments and Comparative Statics

In this section, we quantify how ambiguity aversion shapes the manager’s priors, terminal wealth, and optimal investment strategies, and we relate the key comparative statics to the theoretical results in Sections [4](#S4 "4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") and [5](#S5 "5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"). Solving the two outer minimization problems over the set of priors also allows us to compare the distorted priors implied by the different ambiguity attitudes, offering a further interpretation perspective for Propositions [5.1](#S5.Thmproposition1 "Proposition 5.1 (Power–power specification). ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") and [5.2](#S5.Thmproposition2 "Proposition 5.2 (Exponential–power specification). ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"). All computations in this section are performed using Mathematica 13.3. The code is available upon request.

#### Ambiguity Absence and the Effects of Nonlinear Payoffs.

We start by considering the problem in the absence of ambiguity, which we will also use as a reference benchmark. Specifically, we assume that the expected return Z is known to the manager and equal to z0z\_{0}.

Table 1: Basic parameter set in the delegated portfolio management.

| Parameter | z0z\_{0} | rr | σ\sigma | δ\delta | KK | CC | TT |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Value | 0.078 | 0.02 | 0.3 | 0.2 | 1 | 0.02 | 10 |

Table [1](#S6.T1 "Table 1 ‣ Ambiguity Absence and the Effects of Nonlinear Payoffs. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") reports the financial model parameters. We set z0=0.078z\_{0}=0.078, the risk-free rate to r=0.02r=0.02, and the volatility to σ=0.3\sigma=0.3, which together imply a reasonable Sharpe ratio of approximately 20%20\%. The compensation scheme is specified as

|  |  |  |
| --- | --- | --- |
|  | g​(WTπ)=0.2​(WTπ−1)++0.02,g(W\_{T}^{\pi})=0.2(W\_{T}^{\pi}-1)^{+}+0.02, |  |

representing an option-based payoff. The slope δ=0.2\delta=0.2 captures a moderate incentive intensity, while the fixed component C=0.02C=0.02 ensures participation and provides downside protection. The contract horizon is set to T=10T=10 years.

We first study the relationship between the optimal terminal wealth WT∗W^{\*}\_{T} and the state-price density ξT\xi\_{T}.
Implementing ([5.10](#S5.E10 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")), we compute the optimal terminal wealth numerically. Figure [4](#F4 "Figure 4 ‣ Ambiguity Absence and the Effects of Nonlinear Payoffs. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") displays the relationship between optimal terminal wealth (vertical axis, WT∗W\_{T}^{\ast}) and the state price density (horizontal axis, ξT\xi\_{T}) for three levels of relative risk aversion (RRA): RRA=0.5\mathrm{RRA}=0.5 (dashed, red), RRA=0.6\mathrm{RRA}=0.6 (dotted, green), and RRA=0.7\mathrm{RRA}=0.7 (solid, blue).

![Refer to caption](2603.08552v1/x3.png)


Figure 3: Optimal terminal wealth WT∗W\_{T}^{\*} as a function of ξT\xi\_{T} for three relative risk aversion (RRA=1−α\mathrm{RRA=1-\alpha}) levels (initial wealth w=10w=10).

![Refer to caption](2603.08552v1/x4.png)


Figure 4: Optimal risky proportion vs. wealth Wt∗W^{\*}\_{t} for three relative risk aversion (RRA=1−α\mathrm{RRA=1-\alpha}) levels (initial wealth w=10w=10, t=T−1t=T-1).

The results in Figure [4](#F4 "Figure 4 ‣ Ambiguity Absence and the Effects of Nonlinear Payoffs. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") show that WT∗W^{\*}\_{T} is discontinuous in ξT\xi\_{T} for all three levels of relative risk aversion: it decreases until ξT\xi\_{T} reaches y^/κw∗\widehat{y}/\kappa^{\*}\_{w}, after which it drops to zero. This kink reflects that, once the option is sufficiently out of the money, additional wealth barely changes the compensation, so it is optimal for the manager to cease allocating resources to these states. Intuitively, in states with high state-price density (“expensive” states), extra wealth hardly increases compensation because the option-style payoff is locally flat. The investor therefore shifts resources away from these expensive states toward low-ξT\xi\_{T} (“inexpensive”) states where each dollar has more impact. This “all-or-nothing” structure in WT∗W^{\*}\_{T} is a direct effect of non-concavity.
Moreover, Figure [4](#F4 "Figure 4 ‣ Ambiguity Absence and the Effects of Nonlinear Payoffs. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") shows that greater risk aversion shifts the kink to the right. Greater risk aversion raises the effective penalty on dispersion across states. As a result, in favorable (low-ξT\xi\_{T}) states, a more risk-averse investor chooses a lower payoff than a less risk-averse one, while in unfavorable states (high-ξT\xi\_{T}) the zero-payoff region shrinks. Thus higher RRA compresses the cross-state wealth distribution, replacing “lottery-like” payoffs by more concave profiles, consistent with the concavification logic in Theorem [5.1](#S5.Thmtheorem1 "Theorem 5.1. ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").

Regarding the trading strategy, Figure [4](#F4 "Figure 4 ‣ Ambiguity Absence and the Effects of Nonlinear Payoffs. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") plots the optimal trading ratio (vertical axis, πt∗/Wt∗\pi\_{t}^{\ast}/W\_{t}^{\ast}) as a function of current wealth (horizontal axis, Wt∗W\_{t}^{\ast}) at time t=T−1=9t=T-1=9 in the absence of ambiguity. As expected, greater risk aversion lowers the fraction of wealth invested in the risky asset. Quantitatively, a 40% increase in RRA reduces the risky share by roughly one third at intermediate wealth levels, illustrating that the non-concave payoff preserves the standard risk-return trade-off but amplifies its impact near the extremes.

#### Ambiguity Aversion Interacts with Nonlinear Payoffs.

To study the impact of ambiguity presence, we consider that the decision-maker is no longer certain about the underlying value of ZZ and models this uncertainty, allowing ZZ to become a random variable over two scenarios, an unfavourable scenario over which Z=z1Z=z\_{1} and a favourable one with Z=z2Z=z\_{2}. The decision-maker assigns a prior 𝒫\mathcal{P} over these realizations, with 𝒫​(Z=z1)=q\mathcal{P}(Z=z\_{1})=q, and 𝒫​(Z=z2)=1−q\mathcal{P}(Z=z\_{2})=1-q. Numerically, we assign z1=0.03z\_{1}=0.03 and z2=0.09z\_{2}=0.09, and 𝒫​(Z=z1)=0.2\mathcal{P}(Z=z\_{1})=0.2 and 𝒫​(Z=z2)=0.8\mathcal{P}(Z=z\_{2})=0.8, so that 𝔼𝒫​[Z]=0.078=z0\mathbb{E}^{\mathcal{P}}[Z]=0.078=z\_{0}, the benchmark return z0z\_{0} in the ambiguity-neutral experiments. Thus, the decision-maker at time t=0t=0 is optimistic about the possibility of the more favourable scenario, assigning it an 80% probability, against a 20% chance of the lower return scenario.

The first effect of ambiguity preferences is a distortion of the decision-maker’s belief about the unknown parameter ZZ. This amounts to understanding how the distorted prior implied by smooth ambiguity preferences (Equation ([5.3](#S5.E3 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"))).

Table 2: Optimal q∗q^{\*} for different RAA levels in the power-power case (initial wealth w=10w=10, RRA=0.5\mathrm{RRA=0.5})

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1−λ1-\lambda (RAA) | 0.01 | 0.02 | 0.04 | 0.1 | 0.3 | 0.7 | 1.2 | 1.7 | 2.0 | 2.2 |
| q∗q^{\*} | 0.733 | 0.573 | 0.413 | 0.238 | 0.168 | 0.127 | 0.102 | 0.091 | 0.087 | 0.086 |

We begin with the power-power specification in Proposition [5.1](#S5.Thmproposition1 "Proposition 5.1 (Power–power specification). ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"). Under ambiguity aversion, the distorted belief 𝒬∗\mathcal{Q}^{\ast} assigns probability q∗:=𝒬∗​(Z=z2)q^{\ast}:=\mathcal{Q}^{\ast}(Z=z\_{2}) and 1−q∗=𝒬∗​(Z=z1)1-q^{\ast}=\mathcal{Q}^{\ast}(Z=z\_{1}), where the distorted belief 𝒬∗\mathcal{Q}^{\ast} arises endogenously from the outer maximization problem in ([5.11](#S5.E11 "In Proposition 5.1 (Power–power specification). ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")).
The resulting numerical value depends on the relative ambiguity aversion 1−λ1-\lambda. Table [2](#S6.T2 "Table 2 ‣ Ambiguity Aversion Interacts with Nonlinear Payoffs. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") reports the values of q∗q^{\ast} after solving Problem ([5.11](#S5.E11 "In Proposition 5.1 (Power–power specification). ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) for increasing values of 1−λ1-\lambda, i.e., for higher ambiguity aversion. To illustrate, at 1−λ=0.011-\lambda=0.01, we have q∗=0.733q^{\ast}=0.733, while at 1−λ=2.21-\lambda=2.2 we find q∗=0.086q^{\ast}=0.086. Because q∗q^{\ast} represents the probability of the favorable state, the values in Table [2](#S6.T2 "Table 2 ‣ Ambiguity Aversion Interacts with Nonlinear Payoffs. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") show that decision-makers shift their belief toward considering the bad state more likely as ambiguity aversion increases. This distortion should imply a cautious approach in the face of uncertainty.

#### Sensitivity Analysis: A 232^{3} Factorial Design.

We quantify the sensitivity of belief distortions using a 232^{3} full-factorial design that varies (A) the baseline prior over the good state (low q=0.5q=0.5 vs. high q=0.8q=0.8), (B) relative risk aversion (RRA =0.3=0.3 vs. 0.50.5), and (C) relative ambiguity aversion (RAA =0.01=0.01 vs. 0.30.3).
For each of the eight configurations, we solve the Problem ([5.11](#S5.E11 "In Proposition 5.1 (Power–power specification). ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) and record the optimal distorted good-state probability q∗q^{\*}. Table [3](#S6.T3 "Table 3 ‣ Sensitivity Analysis: A 2³ Factorial Design. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") reports the implied decomposition and Table [C.2](#A3.T2 "Table C.2 ‣ Appendix C Factorial Design ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") reports the eight values in Appendix [C](#A3 "Appendix C Factorial Design ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").

Table 3: Factorial effects on the distorted good-state probability q∗q^{\*}

|  |  |  |
| --- | --- | --- |
|  | Effect on q∗q^{\*} | Economic interpretation |
| Prior optimism (A) | +0.160+0.160 | Anchors distorted beliefs toward the good state |
| Risk aversion (B) | +0.035+0.035 | Small impact |
| Ambiguity aversion (C) | −0.447-0.447 | Pessimistic tilt: shifts mass to the bad state |
| A ×\times B | +0.001+0.001 | Negligible |
| A ×\times C | −0.113-0.113 | Ambiguity attenuates prior anchoring |
| B ×\times C | +0.021+0.021 | Weak interaction |
| A ×\times B ×\times C | +0.033+0.033 | Small higher-order effect |

Three patterns emerge. First, ambiguity aversion is the dominant force shaping distortions: moving from low to high ambiguity aversion reduces q∗q^{\*} by about 0.450.45 on average, implying a strong pessimistic tilt (probability mass shifts from the good to the bad state). Second, a more optimistic prior increases q∗q^{\*} (about 0.160.16 on average), indicating that distorted beliefs remain anchored to baseline information. Third, ambiguity aversion attenuates the role of the prior: the negative A×CA\times C interaction shows that prior optimism translates into a smaller increase in q∗q^{\*} when ambiguity aversion is high. Risk aversion has only a minor direct or interactive impact. Overall, belief distortions are driven primarily by ambiguity attitudes, while prior information matters mainly when ambiguity concerns are weak.

![Refer to caption](2603.08552v1/x5.png)


Figure 5: Optimal terminal wealth WT∗W\_{T}^{\*} as a function of ξT\xi\_{T} for three ambiguity aversion levels (RAA=1−λ\mathrm{RAA=1-\lambda}) in power-power case (initial wealth w=10w=10, RRA=0.5\mathrm{RRA=0.5}).

![Refer to caption](2603.08552v1/x6.png)


Figure 6: Optimal risky proportion vs. wealth Wt∗W^{\*}\_{t} for three ambiguity aversion levels (RAA=1−λ\mathrm{RAA=1-\lambda}) in the power-power case (initial wealth w=10w=10, RRA=0.5\mathrm{RRA=0.5}, t=T−1t=T-1).

We can now examine the impact of ambiguity preferences on the optimal terminal wealth WT∗W\_{T}^{\ast} and trading strategy πt∗\pi\_{t}^{\ast}. In Figure [6](#F6 "Figure 6 ‣ Sensitivity Analysis: A 2³ Factorial Design. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"), we display the optimal terminal wealth (vertical axis, WT∗W\_{T}^{\ast}) against the state-price density (horizontal axis, ξT\xi\_{T}) for three levels of ambiguity aversion:
RAA=0.01\mathrm{RAA}=0.01 (dashed, red), RAA=0.04\mathrm{RAA}=0.04 (dotted, green) and RAA=2.20\mathrm{RAA}=2.20 (solid, blue). Figure [6](#F6 "Figure 6 ‣ Sensitivity Analysis: A 2³ Factorial Design. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") shows that WT∗W\_{T}^{\*} decreases with ξT\xi\_{T} until it reaches the cutoff y^/κw∗\widehat{y}/\kappa^{\*}\_{w}, after which it drops to zero for all three values of RAA. This behavior is similar to the one in the no-ambiguity case. Ambiguity aversion has two effects. First, stronger ambiguity aversion shifts the cutoff to the left, and, second, it makes the curve WT∗W\_{T}^{\*} systematically lower than the corresponding curve with weaker ambiguity aversion. Overall, the region in which the option is “effectively in the money” shrinks as beliefs become more pessimistic, and the manager accepts zero payoff already at intermediate ξT\xi\_{T}. Intuitively, a more ambiguity-averse manager assigns a higher weight to adverse drifts, which raises the shadow price κw∗\kappa^{\*}\_{w}, so the interior solution WT∗=𝒳​(κw∗​ξT)W\_{T}^{\*}=\mathcal{X}(\kappa^{\*}\_{w}\xi\_{T}) falls and the zero-payoff region expands. This mechanism highlights that ambiguity aversion acts as a disciplining force: it tightens effective risk limits through endogenous belief distortion, even though the underlying contract remains unchanged. This channel differs from the pure effect of risk aversion documented in Figure [4](#F4 "Figure 4 ‣ Ambiguity Absence and the Effects of Nonlinear Payoffs. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"), which operates solely through utility curvature.

Figure [6](#F6 "Figure 6 ‣ Sensitivity Analysis: A 2³ Factorial Design. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") plots the optimal investment ratio (vertical axis, πt∗/Wt∗\pi\_{t}^{\*}/W^{\*}\_{t}) as a function of current wealth (horizontal axis, Wt∗W^{\*}\_{t}) for alternative ambiguity attitudes. The fraction invested in the risky asset declines with wealth regardless of the attitude. This downward slope reflects the concavified objective: as wealth rises, the marginal value of the additional upside diminishes, and the manager behaves more cautiously despite the convex contract. In addition, higher ambiguity aversion leads to a lower allocation to the risky asset. To illustrate, in Figure [6](#F6 "Figure 6 ‣ Sensitivity Analysis: A 2³ Factorial Design. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") the allocation corresponding to RAA=0.01\mathrm{RAA}=0.01 (dashed, red) lies uniformly above that for RAA=0.02\mathrm{RAA}=0.02 (dotted, green), which in turn lies above that for RAA=0.3\mathrm{RAA}=0.3 (solid, blue) and converges rapidly to zero. For even higher values of the relative ambiguity aversion (RAA>0.3\mathrm{RAA}>0.3), the risky share is always substantially lower and converges rapidly toward zero. Quantitatively, moving from low to high ambiguity aversion roughly halves the risky share at intermediate wealth levels. The explanation is that an increase in wealth reduces marginal utility, and ambiguity aversion shifts weight toward adverse scenarios. Both these effects discourage risky exposure. Thus, ambiguity aversion not only distorts beliefs but also induces more conservative dynamic trading, mitigating the risk-shifting incentives generated by the option-based contract.

Table 4: Optimal q∗q^{\*} for different AAA levels in the exponential-power case (initial wealth w=10w=10, RRA=0.5\mathrm{RRA=0.5})

| AAA (γ\gamma) | 0.01 | 0.1 | 0.5 | 1 | 2 | 3 | 4 | 8 | 12 | 15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| q∗q^{\*} | 0.799 | 0.791 | 0.751 | 0.694 | 0.563 | 0.423 | 0.294 | 0.108 | 0.094 | 0.090 |

Now we repeat the analysis for the exponential-power case of Proposition [5.2](#S5.Thmproposition2 "Proposition 5.2 (Exponential–power specification). ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"). We start with the probability distortion. Solving ([5.12](#S5.E12 "In Proposition 5.2 (Exponential–power specification). ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) yields q∗=𝒬∗​(Z=z2)q^{\*}=\mathcal{Q}^{\*}(Z=z\_{2}) and 1−q∗=𝒬∗​(Z=z1)1-q^{\*}=\mathcal{Q}^{\*}(Z=z\_{1}) for different absolute ambiguity aversion (AAA) levels γ\gamma (Table [4](#S6.T4 "Table 4 ‣ Sensitivity Analysis: A 2³ Factorial Design. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")). As γ\gamma increases, q∗q^{\*} decreases, meaning that the manager assigns increasingly higher probability to the worst state. Numerically, q∗q^{\*} declines from 0.7990.799 to 0.0900.090 as γ\gamma rises from 0.010.01 to 1515, more than tripling the probability mass of the bad state.

![Refer to caption](2603.08552v1/x7.png)


Figure 7: Optimal terminal wealth WT∗W\_{T}^{\*} as a function of ξT\xi\_{T} for three ambiguity aversion levels (AAA=γ\mathrm{AAA=\gamma}) in exponential-power case (initial wealth w=10w=10, RRA=0.5\mathrm{RRA=0.5}).

![Refer to caption](2603.08552v1/x8.png)


Figure 8: Optimal risky proportion vs. wealth Wt∗W^{\*}\_{t} for different ambiguity aversion levels (AAA=γ\mathrm{AAA=\gamma}) in the exponential-power case (initial wealth w=10w=10, RRA=0.5\mathrm{RRA=0.5}, t=T−1t=T-1).

Similar to the power–power specification, Figure [8](#F8 "Figure 8 ‣ Sensitivity Analysis: A 2³ Factorial Design. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") plots optimal terminal wealth (vertical axis, WT∗W\_{T}^{\ast}) against the state-price density (horizontal axis, ξT\xi\_{T}) for three levels of ambiguity aversion, AAA=0.01\mathrm{AAA}=0.01 (dashed, red), AAA=3\mathrm{AAA}=3 (dotted, green) and AAA=15\mathrm{AAA}=15 (solid, blue). The qualitative patterns resemble those observed in the power–power case. In addition, Figure [8](#F8 "Figure 8 ‣ Sensitivity Analysis: A 2³ Factorial Design. ‣ 6 Numerical Experiments and Comparative Statics ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") displays the optimal investment ratio (vertical axis, πt∗/Wt∗\pi\_{t}^{\ast}/W\_{t}^{\ast}) as a function of current wealth (horizontal axis, Wt∗W\_{t}^{\ast}) for three levels of ambiguity aversion: AAA=1\mathrm{AAA}=1 (dashed, red), AAA=2\mathrm{AAA}=2 (dotted, green) and AAA=4\mathrm{AAA}=4 (solid, blue). We also find that the fraction invested in the risky asset declines with wealth across all ambiguity attitudes. Moreover, ambiguity aversion shifts probability weight toward adverse scenarios, thereby reducing risk exposure.
These patterns are consistent with those obtained under the power–power specification, underscoring the consistency of the economic implications.

## 7 Conclusion

We have proposed a general framework for non-concave dynamic portfolio optimization under smooth ambiguity with Bayesian learning.
To address the inherent dynamic inconsistency of smooth ambiguity preferences, we have employed the robust representation of quasiconcave functionals. This has allowed us to reformulate the original certainty-equivalent problem into an optimization problem with a penalty on the belief about the uncertain expected return. Under suitable specifications of ϕ\phi, the problem reduces to an ambiguity-neutral optimization with distorted priors, naturally interpreted as a Bayesian adaptive problem. Priors are updated via nonlinear filtering, and in combination with the martingale approach and concavification principle, this structure yields semi-closed-form optimal strategies.

We have then applied this framework to option-based compensation schemes in fund management to study how ambiguity aversion interacts with convex incentive contracts. Our analysis shows that ambiguity aversion endogenously tilts beliefs toward adverse states, shrinks in-the-money regions for convex contract components, and lowers risky exposure, thereby mitigating risk-shifting incentives relative to the ambiguity-neutral benchmark. Thus, effectively, ambiguity aversion functions as an endogenous risk constraint in convex compensation environments.

Because the argument is developed within a general option-style payoff framework, the implications carry over to other payoff-engineering contexts, including guarantees, drawdowns, and insurance products with embedded options such as caps, floors, surrender features, and guaranteed minimum benefits (e.g., Bacinello et al. ([2011](#bib.bib1 "Variable annuities: a unifying valuation approach"))).

This paper opens several avenues for future research. A first technical direction is to explore further and compare the robust representation of quasiconcave functionals with the equilibrium approaches studied in the time-inconsistency literature. For example, it would be interesting to compare our investment strategies with weak/strong/regular equilibria as in Huang and Zhou ([2021](#bib.bib25 "Strong and weak equilibria for time-inconsistent stochastic control in continuous time")) and He and Jiang ([2021](#bib.bib24 "On the equilibrium strategies for time-inconsistent problems in continuous time")). A second extension is to incorporate more realistic market features, such as portfolio constraints ((Dai et al., [2022](#bib.bib57 "Nonconcave utility maximization with portfolio bounds"))) or transaction costs ((Qian and Yang, [2023](#bib.bib8 "Non-concave utility maximization with transaction costs"))). Finally, it would be valuable to investigate other non-concave problems beyond the option-based compensation considered here and to examine how ambiguity aversion shapes outcomes. Examples include goal-reaching problems (Capponi and Zhang, [2024](#bib.bib10 "A continuous time framework for sequential goal-based wealth management")), S-shaped utility from prospect theory (Tse and Zheng, [2023](#bib.bib26 "Portfolio selection, periodic evaluations and risk taking")), and convex performance fee schemes (He and Kou, [2018](#bib.bib11 "Profit sharing in hedge funds")). We leave these questions for future work.

## Acknowledgments

An Chen and Shihao Zhu gratefully acknowledge financial support from the Deutsche Forschungsgemeinschaft (DFG), Project-ID 509303834, FOR 5583 “Asset Allocation and Asset Pricing under Regulatory Uncertainty”.

## References

* A. R. Bacinello, P. Millossovich, A. Olivieri, and E. Pitacco (2011)
  Variable annuities: a unifying valuation approach.
  Insurance: Mathematics and Economics 49 (3),  pp. 285–297.
  Cited by: [§7](#S7.p3.1 "7 Conclusion ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* A. G. Balter, A. Mahayni, and N. Schweizer (2021)
  Time-consistency of optimal investment under smooth ambiguity.
  European Journal of Operational Research 293 (2),  pp. 643–657.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§2](#S2.p2.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* S. Basak, A. Pavlova, and A. Shapiro (2007)
  Optimal asset allocation and risk shifting in money management.
  The Review of Financial Studies 20 (5),  pp. 1583–1621.
  Cited by: [§2](#S2.p5.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* N. Bäuerle and A. Chen (2019)
  Optimal retirement planning under partial information.
  Statistics & Risk Modeling 36 (1-4),  pp. 37–55.
  Cited by: [§A.1](#A1.SS1.1.p1.1 "Proof. ‣ A.1 Filtering Arguments ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* N. Bäuerle and A. Mahayni (2024)
  Optimal investment in ambiguous financial markets with learning.
  European Journal of Operational Research 315 (1),  pp. 393–410.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§1](#S1.p2.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§2](#S2.p2.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§3](#S3.p11.1 "3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [item 1](#S4.I3.i1.p1.14 "In 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§5.2](#S5.SS2.p10.3 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§5.2](#S5.SS2.p4.13 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§5.2](#S5.SS2.p8.4 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* A. Bismuth, O. Guéant, and J. Pu (2019)
  Portfolio choice, portfolio liquidation, and portfolio transition under drift uncertainty.
  Mathematics and Financial Economics 13,  pp. 661–719.
  Cited by: [§A.1](#A1.SS1.p5.4 "A.1 Filtering Arguments ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* A. Capponi and Y. Zhang (2024)
  A continuous time framework for sequential goal-based wealth management.
  Management Science 70 (11),  pp. 7664–7691.
  Cited by: [§2](#S2.p4.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§7](#S7.p4.1 "7 Conclusion ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* J. N. Carpenter (2000)
  Does option compensation increase managerial risk appetite?.
  The Journal of Finance 55 (5),  pp. 2311–2331.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§1](#S1.p2.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§1](#S1.p8.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§2](#S2.p4.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§2](#S2.p5.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§3](#S3.p11.1 "3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§5.2](#S5.SS2.p1.1 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§5.2](#S5.SS2.p5.15 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§5.2](#S5.SS2.p8.4 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§5.2](#S5.SS2.p8.5 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* S. Cerreia-Vioglio, F. Maccheroni, M. Marinacci, and L. Montrucchio (2011a)
  Complete monotone quasiconcave duality.
  Mathematics of Operations Research 36 (2),  pp. 321–339.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§2](#S2.p3.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* S. Cerreia-Vioglio, F. Maccheroni, M. Marinacci, and L. Montrucchio (2011b)
  Risk measures: Rationality and diversification.
  Mathematical Finance 21 (4),  pp. 743–774.
  Cited by: [§2](#S2.p3.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* S. Cerreia-Vioglio, F. Maccheroni, M. Marinacci, and L. Montrucchio (2011c)
  Uncertainty averse preferences.
  Journal of Economic Theory 146 (4),  pp. 1275–1330.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§2](#S2.p3.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§4](#S4.p1.3 "4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§4](#S4.p3.1 "4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* A. Chen, P. Hieber, and T. Nguyen (2019)
  Constrained non-concave utility maximization: an application to life insurance contracts with guarantees.
  European Journal of Operational Research 273 (3),  pp. 1119–1135.
  Cited by: [§2](#S2.p4.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* A. Chen, M. Stadje, and F. Zhang (2024)
  On the equivalence between value-at-risk-and expected shortfall-based risk measures in non-concave optimization.
  Insurance: Mathematics and Economics 117,  pp. 114–129.
  Cited by: [§5.2](#S5.SS2.p7.7 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* F. Collard, S. Mukerji, K. Sheppard, and J. Tallon (2018)
  Ambiguity and the historical equity premium.
  Quantitative Economics 9 (2),  pp. 945–993.
  Cited by: [§5.2](#S5.SS2.p3.5 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* M. Dai, S. Kou, S. Qian, and X. Wan (2022)
  Nonconcave utility maximization with portfolio bounds.
  Management Science 68 (11),  pp. 8368–8385.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§2](#S2.p4.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§7](#S7.p4.1 "7 Conclusion ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* S. Drapeau and M. Kupper (2013)
  Risk preferences and their robust representation.
  Mathematics of Operations Research 38 (1),  pp. 28–62.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§2](#S2.p3.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§4](#S4.p3.1 "4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* H. Föllmer and T. Knispel (2011)
  Entropic risk measures: coherence vs. convexity, model ambiguity and robust large deviations.
  Stochastics and Dynamics 11 (02n03),  pp. 333–351.
  Cited by: [item 3](#S4.I3.i3.p1.7 "In 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* C. Gollier (2011)
  Portfolio choices and asset prices: the comparative statics of ambiguity aversion.
  The Review of Economic Studies 78 (4),  pp. 1329–1344.
  Cited by: [§4](#S4.p8.4 "4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§5.2](#S5.SS2.p3.5 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* G. Guan, Z. Liang, and Y. Song (2025a)
  The continuous-time pre-commitment KMM problem in incomplete markets.
  The Annals of Applied Probability 35 (4),  pp. 2923–2966.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§2](#S2.p2.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* G. Guan, Z. Liang, and J. Xia (2025b)
  Equilibrium portfolio selection for smooth ambiguity preferences.
  Mathematics of Operations Research 50 (2),  pp. 1042–1071.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§1](#S1.p4.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§2](#S2.p2.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§3](#S3.p11.1 "3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* E. Hanany and P. Klibanoff (2009)
  Updating ambiguity averse preferences.
  The BE Journal of Theoretical Economics 9 (1).
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* L. P. Hansen and J. Miao (2018)
  Aversion to ambiguity and model misspecification in dynamic stochastic environments.
  Proceedings of the National Academy of Sciences 115 (37),  pp. 9163–9168.
  Cited by: [§2](#S2.p3.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* L. P. Hansen and J. Miao (2022)
  Asset pricing under smooth ambiguity in continuous time.
  Economic Theory 74 (2),  pp. 335–371.
  Cited by: [§2](#S2.p3.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* X. D. He and Z. L. Jiang (2021)
  On the equilibrium strategies for time-inconsistent problems in continuous time.
  SIAM Journal on Control and Optimization 59 (5),  pp. 3860–3886.
  Cited by: [§7](#S7.p4.1 "7 Conclusion ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* X. D. He and S. Kou (2018)
  Profit sharing in hedge funds.
  Mathematical Finance 28 (1),  pp. 50–81.
  Cited by: [§2](#S2.p4.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§7](#S7.p4.1 "7 Conclusion ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* Y. Huang and Z. Zhou (2021)
  Strong and weak equilibria for time-inconsistent stochastic control in continuous time.
  Mathematics of Operations Research 46 (2),  pp. 428–451.
  Cited by: [§7](#S7.p4.1 "7 Conclusion ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* N. Ju and J. Miao (2012)
  Ambiguity, learning, and asset returns.
  Econometrica 80 (2),  pp. 559–591.
  Cited by: [§4](#S4.p8.4 "4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§5.2](#S5.SS2.p3.5 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* I. Karatzas and S. E. Shreve (1998a)
  Methods of mathematical finance.
  Vol. 39, Springer.
  Cited by: [§1](#S1.p5.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§5.2](#S5.SS2.p4.13 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* I. Karatzas and S. Shreve (1998b)
  Brownian motion and stochastic calculus.
  Vol. 113, Springer Science & Business Media.
  Cited by: [§B.2](#A2.SS2.4.p4.8 "Proof. ‣ B.2 Proof of Theorem 5.1 ‣ Appendix B Technical Proofs ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* I. Karatzas and X. Zhao (2001)
  Bayesian adaptive portfolio optimization.
  Option pricing, interest rates and risk management,  pp. 632–669.
  Cited by: [§A.1](#A1.SS1.p5.4 "A.1 Filtering Arguments ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§1](#S1.p5.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§5.2](#S5.SS2.p4.13 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* C. Kardaras and S. Robertson (2012)
  ROBUST maximization of asymptotic growth.
  The Annals of Applied Probability 22 (4),  pp. 1576–1610.
  Cited by: [§3](#S3.p2.14 "3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* P. Klibanoff, M. Marinacci, and S. Mukerji (2005)
  A smooth model of decision making under ambiguity.
  Econometrica 73 (6),  pp. 1849–1892.
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§3](#S3.p9.1 "3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§4](#S4.p2.14 "4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* P. Klibanoff, M. Marinacci, and S. Mukerji (2009)
  Recursive smooth ambiguity preferences.
  Journal of Economic Theory 144 (3),  pp. 930–976.
  Cited by: [§2](#S2.p3.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* F. Maccheroni, M. Marinacci, and A. Rustichini (2006)
  Ambiguity aversion, robustness, and the variational representation of preferences.
  Econometrica 74 (6),  pp. 1447–1498.
  Cited by: [item 3](#S4.I3.i3.p1.8 "In 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* M. Marinacci (2015)
  Model uncertainty.
  Journal of the European Economic Association 13 (6),  pp. 1022–1100.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* A. Mazzon and P. Tankov (2024)
  Optimal stopping and divestment timing under scenario ambiguity and learning.
  arXiv preprint arXiv:2408.09349.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§2](#S2.p3.1 "2 Related Literature ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§4](#S4.p4.1 "4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* R. Merton (1971)
  Optimum consumption and portfolio rules in a continuous-time model.
  Journal of Economic Theory 3 (4),  pp. 373–413.
  Cited by: [§5.2](#S5.SS2.p7.7 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* S. Qian and C. Yang (2023)
  Non-concave utility maximization with transaction costs.
  arXiv preprint arXiv:2307.02178.
  Cited by: [§7](#S7.p4.1 "7 Conclusion ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* C. Reichlin (2013)
  Utility maximization with a given pricing measure when the utility is not necessarily concave.
  Mathematics and Financial Economics 7 (4),  pp. 531–556.
  Cited by: [§3](#S3.p10.6 "3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* U. Rieder and N. Bäuerle (2005)
  Portfolio optimization with unobservable markov-modulated drift process.
  Journal of Applied Probability 42 (2),  pp. 362–378.
  Cited by: [§A.1](#A1.SS1.p5.4 "A.1 Filtering Arguments ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§1](#S1.p5.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§5.2](#S5.SS2.p4.13 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* A. Savochkin, A. Shklyaev, and A. Galatenko (2025)
  Dynamic consistency and rectangularity for the smooth ambiguity model.
  Journal of Economic Theory 225,  pp. 105991.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* M. Sion (1958)
  On general minimax theorems.
  Pacific Journal of Mathematics 8 (1),  pp. 171–176.
  Cited by: [Appendix A](#A1.1.p1.1 "Proof. ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* M. Taboga (2005)
  Portfolio selection with two-stage preferences.
  Finance Research Letters 2 (3),  pp. 152–164.
  Cited by: [§4](#S4.p8.4 "4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"),
  [§5.2](#S5.SS2.p3.5 "5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").
* A. S. Tse and H. Zheng (2023)
  Portfolio selection, periodic evaluations and risk taking.
  Operations Research 71 (6),  pp. 2078–2091.
  Cited by: [§7](#S7.p4.1 "7 Conclusion ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").

## Appendix A Notation and Auxiliary Lemmata

Table A.1: Notation for probability and expectation

| Symbol | Meaning |
| --- | --- |
| ℙ​(𝔼ℙ)\mathbb{P}\ (\mathbb{E}^{\mathbb{P}}) | Generic probability measure (and expectation) |
| ℙZ​(𝔼ℙZ)\mathbb{P}^{Z}\ (\mathbb{E}^{\mathbb{P}^{Z}}) | Model (and expectation) |
| ℙ0\mathbb{P}\_{0} | Reference probability measure, dominating all ℙZ\mathbb{P}^{Z} |
| 𝔓\mathfrak{P} | Set of models |
| 𝒫​(𝔼𝒫)\mathcal{P}\ (\mathbb{E}^{\mathcal{P}}) | Prior on ZZ (and expectation) |
| 𝒬​(𝔼𝒬)\mathcal{Q}\ (\mathbb{E}^{\mathcal{Q}}) | Distorted Prior on ZZ (and expectation) |
| ℳ​(𝒮)\mathcal{M}(\mathcal{S}) | Set of priors on the parameter space 𝒮\mathcal{S} |
| ℙ𝒬​(𝔼ℙ𝒬)\mathbb{P}^{\mathcal{Q}}\ (\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}) | Product measure of ℙZ\mathbb{P}^{Z} and 𝒬\mathcal{Q} (and expectation) |
| ℙ^​(𝔼ℙ^)\widehat{\mathbb{P}}\ (\mathbb{E}^{\widehat{\mathbb{P}}}) | Equivalent measure of ℙ\mathbb{P} in filtering (and expectation) |

###### Lemma A.1.

Let MM and NN be convex spaces, one of which is compact, and ff a function on M×NM\times N, quasi-concave-convex and upper semi-continuous-lower semi-continuous. Then

|  |  |  |
| --- | --- | --- |
|  | supxinfyf​(x,y)=infysupxf​(x,y).\sup\_{x}\inf\_{y}f(x,y)=\inf\_{y}\sup\_{x}f(x,y). |  |

###### Proof.

Proof
The above lemma can be found in Corollary 3.3 of Sion [[1958](#bib.bib74 "On general minimax theorems")].
∎

###### Lemma A.2 (Convex conjugate for payoff g​(x)g(x)).

Define ℒ​(y,x):=u​(g​(x))−y​x,y>0\mathcal{L}(y,x):=u(g(x))-yx,y>0, I​(x):=x1α−1I(x):=x^{\frac{1}{\alpha-1}} and h​(x):=I​(x/δ)−Cδ+Kh(x):=\frac{I(x/\delta)-C}{\delta}+K. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒳(y):=arg​supx≥0ℒ(y,x)={h​(y),0<y<y^,0,y≥y^,\mathcal{X}(y):=\operatorname\*{arg\,sup}\_{x\geq 0}\mathcal{L}(y,x)\\ =\left\{\begin{aligned} h(y),\quad&0<y<\widehat{y},\\ 0,\quad&y\geq\widehat{y},\end{aligned}\right. |  | (A.1) |

where the concavification point y^\widehat{y} is defined as the unique root y∈(0,δ​Cα−1)y\in(0,\delta C^{\alpha-1}) of

|  |  |  |
| --- | --- | --- |
|  | u​(g​(h​(y)))−u​(C)=y​h​(y).u(g(h(y)))-u(C)=yh(y). |  |

###### Proof.

Proof
Note first that ℒ\mathcal{L} is continuous in xx. Except at KK its derivative with respect to xx exists and is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒx​(y,x)={−y,0≤x<K,δ​u′​(δ​(x−K)+C)−y,x>K.\mathcal{L}\_{x}(y,x)=\begin{cases}-y,&\quad 0\leq x<K,\\ \delta u^{\prime}(\delta(x-K)+C)-y,&\quad x>K.\end{cases} |  | (A.2) |

Solving the first-order condition ℒx​(y,x)​=!​0\mathcal{L}\_{x}(y,x)\overset{!}{=}0 for xx, we obtain a local extrema h​(y)h(y) (if h​(y)h(y) is larger than KK). Further, the edge points 0 and KK are candidates for the maximizer 𝒳​(y)\mathcal{X}(y). At the edge point KK, we obtain

|  |  |  |
| --- | --- | --- |
|  | ℒx​(y,K+)=δ​u′​(C)−y=δ​Cα−1−y.\mathcal{L}\_{x}(y,K+)=\delta u^{\prime}(C)-y=\delta C^{\alpha-1}-y. |  |

This determines two cases that are used to determine 𝒳​(y)\mathcal{X}(y):

Case 1: y≥δ​Cα−1y\geq\delta C^{\alpha-1}. Using ℒx\mathcal{L}\_{x} in ([A.2](#A1.E2 "In Proof. ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")), we obtain the monotonicity pattern in xx: ℒ\mathcal{L} is decreasing on (0,+∞)(0,+\infty). As ℒ\mathcal{L} is continuous in xx, we obtain 𝒳​(y)=0\mathcal{X}(y)=0 when y≥δ​Cα−1y\geq\delta C^{\alpha-1}.

Case 2: 0<y<δ​Cα−10<y<\delta C^{\alpha-1}. We observe that the monotonicity pattern in xx, i.e., ℒ\mathcal{L} is decreasing on (0,K)(0,K), increasing on (K,h​(y))(K,h(y)), decreasing on (h​(y),+∞)(h(y),+\infty). This leaves two candidates for the maximizer 𝒳​(y)\mathcal{X}(y), namely 0 and h​(y)h(y). To compare ℒ​(y,0)\mathcal{L}(y,0) and ℒ​(y,h​(y))\mathcal{L}(y,h(y)), we observe that

|  |  |  |
| --- | --- | --- |
|  | ℒ​(y,h​(y))−ℒ​(y,0)=u​(g​(h​(y)))−u​(C)−y​h​(y)\mathcal{L}(y,h(y))-\mathcal{L}(y,0)=u(g(h(y)))-u(C)-yh(y) |  |

due to h​(y)>Kh(y)>K. Then we define the function

|  |  |  |
| --- | --- | --- |
|  | Δ​ℒ​(y):=u​(g​(h​(y)))−u​(C)−y​h​(y)\Delta\mathcal{L}(y):=u(g(h(y)))-u(C)-yh(y) |  |

and we compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂Δ​ℒ​(y)∂y\displaystyle\frac{\partial\Delta\mathcal{L}(y)}{\partial y} | =δ​[u′​(δ​(h​(y)−K)+C)−y]​h′​(y)−h​(y)\displaystyle=\delta[u^{\prime}(\delta(h(y)-K)+C)-y]h^{\prime}(y)-h(y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−h​(y)<0.\displaystyle=-h(y)<0. |  |

This implies that Δ​ℒ​(y)\Delta\mathcal{L}(y) is strictly decreasing on (0,δ​Cα−1)(0,\delta C^{\alpha-1}). Moreover, we compute

|  |  |  |
| --- | --- | --- |
|  | Δ​ℒ​(0)={u​(∞)−u​(c)=+∞>0,if​ 0<α<1,−Cαα>0,if​α<0,\Delta\mathcal{L}(0)=\begin{cases}u(\infty)-u(c)=+\infty>0,\ &\text{if}\ 0<\alpha<1,\\ -\frac{C^{\alpha}}{\alpha}>0,\ &\text{if}\ \alpha<0,\end{cases} |  |

and Δ​ℒ​(δ​Cα−1)=−δ​Cα<0\Delta\mathcal{L}(\delta C^{\alpha-1})=-\delta C^{\alpha}<0. Therefore, there exists an unique root y^∈(0,δ​Cα−1)\widehat{y}\in(0,\delta C^{\alpha-1}) of u​(g​(h​(y)))−u​(C)=y​h​(y).u(g(h(y)))-u(C)=yh(y). Furthermore, when y∈(0,y^)y\in(0,\widehat{y}), Δ​ℒ>0\Delta\mathcal{L}>0, thus h​(y)h(y) is the maximizer; when y∈(y^,+∞),y\in(\widehat{y},+\infty), 0 is the maximizer, which finishes the proof.

∎

### A.1 Filtering Arguments

In this section, we reformulate the Bayesian adaptive problem by applying filtering theory, thereby modeling the drift as a process adapted to the observation filtration. This transformation lays the foundation for the proof of Theorem [5.1](#S5.Thmtheorem1 "Theorem 5.1. ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity").

Define the market price of risk Θ=(Z−r)/σ\Theta=(Z-r)/\sigma with θ=(z−r)/σ\theta=(z-r)/\sigma.
The setting concerns a financial market in which the stock price process SS is perfectly observable in continuous time, whereas the drift parameter Θ\Theta that drives the expected return of the stock is not directly observable.
Consequently, the investor can only learn about Θ\Theta by observing the evolution of SS and updating her belief on Θ\Theta via Bayesian filtering.

Note further that observing the stock price is equivalent to monitoring the process Y=(Yt)t∈[0,T]Y=(Y\_{t})\_{t\in[0,T]} as Yt:=Wt+Θ​tY\_{t}:=W\_{t}+\Theta t.
The price dynamic of the risky asset SS in ([3.1](#S3.E1 "In 3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) can be written as

|  |  |  |
| --- | --- | --- |
|  | d​St=St​(r​d​t+σ​d​Yt),t≥0,dS\_{t}=S\_{t}\!\left(r\,dt+\sigma\,dY\_{t}\right),\quad t\geq 0, |  |

where YtY\_{t} is a ℙ\mathbb{P}-Brownian motion with drift Θ\Theta.
Let 𝔽Y:=(ℱtY)t∈[0,T]\mathbb{F}^{Y}:=(\mathcal{F}^{Y}\_{t})\_{t\in[0,T]}, where
ℱtY:=σ​(Ys,0≤s≤t)\mathcal{F}^{Y}\_{t}:=\sigma(Y\_{s},0\leq s\leq t) is the filtration generated by YY—equivalent to the filtration generated by SS.

As time progresses, the investor draws her inferences about Θ\Theta and updates
her prior via θ^:=(θ^t)t∈[0,T]\widehat{\theta}:=(\widehat{\theta}\_{t})\_{t\in[0,T]}:

|  |  |  |
| --- | --- | --- |
|  | θ^t:=𝔼𝒬[Θ∣ℱtY].t∈[0,T],\widehat{\theta}\_{t}:=\mathbb{E}^{\mathcal{Q}}[\Theta\mid\mathcal{F}^{Y}\_{t}].\quad t\in[0,T], |  |

Note that condition ([3.2](#S3.E2 "In 3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) ensures that (θ^t)t∈[0,T](\widehat{\theta}\_{t})\_{t\in[0,T]} is well-defined.

Let the process BY=(BtY)t∈[0,T]B^{Y}=(B^{Y}\_{t})\_{t\in[0,T]} be given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​BtY=d​Bt+(Θ−θ^t)​d​t.dB\_{t}^{Y}=dB\_{t}+(\Theta-\widehat{\theta}\_{t})\,dt. |  | (A.3) |

The process (BtY)t∈[0,T](B\_{t}^{Y})\_{t\in[0,T]} is called the innovation process in filtering theory. It is well known that BYB^{Y} is an (𝔽Y,ℙ)(\mathbb{F}^{Y},\mathbb{P}) standard Brownian motion
(see, for example, Proposition 2 in Bismuth et al. [[2019](#bib.bib59 "Portfolio choice, portfolio liquidation, and portfolio transition under drift uncertainty")]).
Moreover, by Theorem 1 in Bismuth et al. [[2019](#bib.bib59 "Portfolio choice, portfolio liquidation, and portfolio transition under drift uncertainty")] (see also Karatzas and Zhao [[2001](#bib.bib30 "Bayesian adaptive portfolio optimization")], Rieder and Bäuerle [[2005](#bib.bib31 "Portfolio optimization with unobservable markov-modulated drift process")]), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ^t=Fy​(t,Yt;𝒬)F​(t,Yt;𝒬),t∈[0,T],\widehat{\theta}\_{t}=\frac{F\_{y}(t,Y\_{t};\mathcal{Q})}{F(t,Y\_{t};\mathcal{Q})},\quad t\in[0,T], |  | (A.4) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(t,y;𝒬):=∫𝒮exp⁡{θ​y−12​θ2​t}​𝒬​(d​θ).F(t,y;\mathcal{Q}):=\int\_{\mathcal{S}}\exp\!\bigl\{\theta y-\tfrac{1}{2}\theta^{2}t\bigr\}\,\mathcal{Q}(d\theta). |  | (A.5) |

With this conditional expectation—i.e. based on the investor’s Bayesian update θ^\widehat{\theta}—the stock-price evolution becomes

|  |  |  |
| --- | --- | --- |
|  | d​St=St​((r+σ​θ^t)​d​t+σ​d​BtY),dS\_{t}=S\_{t}\!\left(\bigl(r+\sigma\widehat{\theta}\_{t}\bigr)\,dt+\sigma\,dB\_{t}^{Y}\right), |  |

where BtYB\_{t}^{Y} is given in ([A.3](#A1.E3 "In A.1 Filtering Arguments ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")).

Note that due to the relation

|  |  |  |
| --- | --- | --- |
|  | Yt=BtY+∫0tθ^s​𝑑s,Y\_{t}={B}^{Y}\_{t}+\int^{t}\_{0}\widehat{\theta}\_{s}ds, |  |

we can define a new probability measure ℙ^\widehat{\mathbb{P}} for each fixed TT, under which YtY\_{t} becomes a standard (𝔽Y,ℙ^)(\mathbb{F}^{Y},\widehat{\mathbb{P}}) Brownian motion for 0≤t≤T0\leq t\leq T:

|  |  |  |
| --- | --- | --- |
|  | ΛT:=d​ℙ^d​ℙ|ℱTY=exp⁡(−∫0Tθ^t​𝑑BtY−12​∫0Tθ^t2​𝑑t).\Lambda\_{T}:=\frac{d\widehat{\mathbb{P}}}{d\mathbb{P}}\bigg|\_{\mathcal{F}^{Y}\_{T}}=\exp\bigg(-\int^{T}\_{0}\widehat{\theta}\_{t}d{B}^{Y}\_{t}-\frac{1}{2}\int^{T}\_{0}\widehat{\theta}\_{t}^{2}dt\bigg). |  |

An application of Itô’s rule to the process Λt\Lambda\_{t} gives

|  |  |  |
| --- | --- | --- |
|  | d​Λt=−Λt​θ^t​d​BtY,Λ0=1.d{\Lambda}\_{t}=-{\Lambda}\_{t}\widehat{\theta}\_{t}dB^{Y}\_{t},\quad{\Lambda}\_{0}=1. |  |

Now we can rewrite ([3.3](#S3.E3 "In 3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Wtπ\displaystyle dW\_{t}^{\pi} | =(r​Wtπ+σ​πt​θ^t)​d​t+πt​σ​d​BtY\displaystyle=(rW^{\pi}\_{t}+\sigma\pi\_{t}\widehat{\theta}\_{t})dt+\pi\_{t}\sigma dB\_{t}^{Y} |  | (A.6) |
|  |  | =r​Wtπ​d​t+πt​σ​d​Yt,\displaystyle=rW^{\pi}\_{t}dt+\pi\_{t}\sigma\;dY\_{t}, |  |

where θ^t\widehat{\theta}\_{t} is given in ([A.4](#A1.E4 "In A.1 Filtering Arguments ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")). Further, we have

|  |  |  |
| --- | --- | --- |
|  | d​(Λt​e−r​t​Wtπ)=e−r​t​Λt​[σ​πt−Wtπ​θ^t]​d​BtY.d({\Lambda}\_{t}e^{-rt}W\_{t}^{\pi})=e^{-rt}{\Lambda}\_{t}[\sigma\pi\_{t}-W\_{t}^{\pi}\widehat{\theta}\_{t}]dB^{Y}\_{t}. |  |

This shows that, on a given finite time horizon [0,T][0,T], the process (e−r​t​Λt​Wtπ)t∈[0,T](e^{-rt}{\Lambda}\_{t}W\_{t}^{\pi})\_{t\in[0,T]} is a nonnegative (𝔽Y,ℙ\mathbb{F}^{Y},\mathbb{P})-local martingale, hence also a supermartingale; in particular, for all π∈𝒜​(w)\pi\in\mathcal{A}(w),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[e−r​T​ΛT​WTπ]=𝔼ℙ^​[e−r​T​WTπ]≤w,\mathbb{E}^{\mathbb{P}}[e^{-rT}{\Lambda}\_{T}W\_{T}^{\pi}]=\mathbb{E}^{\widehat{\mathbb{P}}}[e^{-rT}W\_{T}^{\pi}]\leq w, |  | (A.7) |

where 𝔼ℙ\mathbb{E}^{\mathbb{P}} and 𝔼ℙ^{\mathbb{E}^{\widehat{\mathbb{P}}}} are expectations with respect to ℙ\mathbb{P} and ℙ^\widehat{\mathbb{P}}, respectively.

Moreover, we state the following lemma for later use.

###### Lemma A.3.

We can express Λt\Lambda\_{t} as a function of the observational magnitude YtY\_{t}:

|  |  |  |
| --- | --- | --- |
|  | Λt=1F​(t,Yt;𝒬),t≥0,\Lambda\_{t}=\frac{1}{F(t,Y\_{t};\mathcal{Q})},\quad t\geq 0, |  |

where F​(t,y;𝒬)F(t,y;\mathcal{Q}) is given in ([A.5](#A1.E5 "In A.1 Filtering Arguments ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")).

###### Proof.

Proof
The proof can be found in Lemma 2.1 in Bäuerle and Chen [[2019](#bib.bib43 "Optimal retirement planning under partial information")].
∎

## Appendix B Technical Proofs

### B.1 Proof of Theorem [4.1](#S4.Thmtheorem1 "Theorem 4.1. ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")

###### Proof.

Proof
We apply Lemma [A.1](#A1.Thmlemma1 "Lemma A.1. ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") to the function L:𝒜​(w)×ℳ​(𝒮)→ℝL:\mathcal{A}(w)\times\mathcal{M(}\mathcal{S})\to\mathbb{R} defined by

|  |  |  |
| --- | --- | --- |
|  | L​(π,𝒬):=R​(𝒬,𝔼ℙ𝒬​[U​(WTπ)]).L(\pi,\mathcal{Q}):=R(\mathcal{Q},\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[U(W\_{T}^{\pi})]). |  |

The sets 𝒜​(w)\mathcal{A}(w) and ℳ​(𝒮)\mathcal{M}(\mathcal{S}) are clearly convex and 𝒜\mathcal{A} is a compact set. Point (2) of Proposition [4.1](#S4.Thmproposition1 "Proposition 4.1 (Robust representation form of smooth ambiguity preferences). ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") implies L​(π,⋅)L(\pi,\cdot) is quasi-convex for any π∈𝒜\pi\in\mathcal{A}. Then we notice that π→WTπ\pi\to W^{\pi}\_{T} is linear. Moreover UU is increasing and RR is nondecreasing in the second argument, so that L​(⋅,𝒬)L(\cdot,\mathcal{Q}) is quasi-concave for any 𝒬\mathcal{Q}. Thus, LL is quasi-concave-convex, i.e., LL is quasi-concave in π\pi and quasi-convex in 𝒬\mathcal{Q}.

Moreover, the function L​(𝒬,⋅)L(\mathcal{Q},\cdot) is upper semicontinuous by point (1) of Proposition [4.1](#S4.Thmproposition1 "Proposition 4.1 (Robust representation form of smooth ambiguity preferences). ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") and since

|  |  |  |
| --- | --- | --- |
|  | π↦𝔼ℙ𝒬​[U​(WTπ)]\pi\mapsto\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[U(W\_{T}^{\pi})] |  |

is continuous. It remains to show that L​(π,⋅)L(\pi,\cdot) is lower semi-continuous for all π∈𝒜\pi\in\mathcal{A}. Assume first that we are in the context of Assumption [4.1](#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") (1). Then, for any sequence (𝒬n)(\mathcal{Q}^{n}) converging to a limit 𝒬∈ℳ​(𝒮)\mathcal{Q}\in\mathcal{M}(\mathcal{S}) and for any index k∈ℕk\in\mathbb{N},

|  |  |  |  |
| --- | --- | --- | --- |
|  | limninfL​(π,𝒬n)\displaystyle\lim\_{n}\inf L(\pi,\mathcal{Q}^{n}) | =limninfm≥nR​(𝒬m,𝔼ℙ𝒬m​[U​(WTπ)])\displaystyle=\lim\_{n}\inf\_{m\geq n}R(\mathcal{Q}^{m},\mathbb{E}^{\mathbb{P}^{\mathcal{Q}^{m}}}[U(W\_{T}^{\pi})]) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥limninfm≥nR​(𝒬m,infj≥k𝔼ℙ𝒬j​[U​(WTπ)])\displaystyle\geq\lim\_{n}\inf\_{m\geq n}R(\mathcal{Q}^{m},\inf\_{j\geq k}\mathbb{E}^{\mathbb{P}^{\mathcal{Q}^{j}}}[U(W\_{T}^{\pi})]) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥R​(𝒬,infj≥k𝔼ℙ𝒬j​[U​(WTπ)]),\displaystyle\geq R(\mathcal{Q},\inf\_{j\geq k}\mathbb{E}^{\mathbb{P}^{\mathcal{Q}^{j}}}[U(W\_{T}^{\pi})]), |  |

where the first inequality holds because RR is nondecreasing in ss. Now, making k→+∞k\to+\infty, by continuity we obtain

|  |  |  |
| --- | --- | --- |
|  | limninfL​(π,𝒬n)≥L​(π,𝒬).\lim\_{n}\inf L(\pi,\mathcal{Q}^{n})\geq L(\pi,\mathcal{Q}). |  |

Under Assumption [4.1](#S4.Thmassumption1 "Assumption 4.1. ‣ 4 Making Smooth Ambiguity Choices Time Consistent ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") (2) a similar argument can be used since

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℙ𝒬​[U​(WTπ)]>0.\mathbb{E}^{\mathbb{P}^{\mathcal{Q}}}[U(W\_{T}^{\pi})]>0. |  |

Therefore, the infimum and the supremum in Lemma [A.1](#A1.Thmlemma1 "Lemma A.1. ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") are attained and there exists a saddle point.
∎

### B.2 Proof of Theorem [5.1](#S5.Thmtheorem1 "Theorem 5.1. ‣ 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")

###### Proof.

Proof
Now we use martingale method, to maximize the expected utility

|  |  |  |
| --- | --- | --- |
|  | V​(w;𝒬)=supπ∈𝒜𝔼ℙ​[u​(g​(WTπ))]V(w;\mathcal{Q})=\sup\_{\pi\in\mathcal{A}}\mathbb{E}^{\mathbb{P}}[u(g(W\_{T}^{\pi}))] |  |

subject to the constraint ([A.7](#A1.E7 "In A.1 Filtering Arguments ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) where WTπW\_{T}^{\pi} is given in ([A.6](#A1.E6 "In A.1 Filtering Arguments ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")), that is, we have the following static optimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | WT∗=argmaxWTπ≥0𝔼ℙ​[u​(g​(WTπ))]W\_{T}^{\*}=\operatorname\*{argmax}\_{W^{\pi}\_{T}\geq 0}\mathbb{E}^{\mathbb{P}}[u(g(W\_{T}^{\pi}))] |  | (B.1) |

such that 𝔼ℙ​[ξT​WTπ]≤w\mathbb{E}^{\mathbb{P}}[\xi\_{T}W\_{T}^{\pi}]\leq w with ξT=e−r​T​ΛT\xi\_{T}=e^{-rT}{\Lambda}\_{T}.

To solve ([B.1](#A2.E1 "In Proof. ‣ B.2 Proof of Theorem 5.1 ‣ Appendix B Technical Proofs ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")), consider the Lagrangian problem

|  |  |  |
| --- | --- | --- |
|  | supWTπ≥0𝔼ℙ​[u​(g​(WTπ))+κ​(w−ξT​WTπ)]\sup\_{W\_{T}^{\pi}\geq 0}\mathbb{E}^{\mathbb{P}}[u(g(W\_{T}^{\pi}))+\kappa(w-\xi\_{T}W\_{T}^{\pi})] |  |

for a multiplier κ≥0\kappa\geq 0. Define J​(y):=supx>0{u​(g​(x))−y​x}J(y):=\sup\_{x>0}\{u(g(x))-yx\}. The existence of JJ is ensured by the growth condition in Definition [3.1](#S3.Thmdefinition1 "Definition 3.1 (Utility function). ‣ 3 Problem Formulation ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"). The maximizer in J​(y)J(y) is given by 𝒳\mathcal{X} (cf. ([A.1](#A1.E1 "In Lemma A.2 (Convex conjugate for payoff 𝑔⁢(𝑥)). ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"))), i.e.,

|  |  |  |
| --- | --- | --- |
|  | 𝒳​(y)=h​(y)⋅𝟙{0<y<y^}.\mathcal{X}(y)=h(y)\cdot\mathbbm{1}\_{\{0<y<\widehat{y}\}}. |  |

This leads to WT∗​(κ,ξT)=𝒳​(κ​ξT)W\_{T}^{\*}(\kappa,\xi\_{T})=\mathcal{X}(\kappa\xi\_{T}) as a candidate for optimal terminal wealth. For any admissible terminal wealth WTπW\_{T}^{\pi}, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[u​(g​(WTπ))]\displaystyle\mathbb{E}^{\mathbb{P}}[u(g(W\_{T}^{\pi}))] | ≤𝔼ℙ​[u​(g​(WTπ))+κ​(w−ξT​WTπ)]\displaystyle\leq\mathbb{E}^{\mathbb{P}}[u(g(W\_{T}^{\pi}))+\kappa(w-\xi\_{T}W\_{T}^{\pi})] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼ℙ​[J​(κ​ξT)]+κ​w\displaystyle\leq\mathbb{E}^{\mathbb{P}}[J(\kappa\xi\_{T})]+\kappa w |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙ​[u​(g​(𝒳​(κ​ξT)))],\displaystyle=\mathbb{E}^{\mathbb{P}}[u(g(\mathcal{X}(\kappa\xi\_{T})))], |  |

i.e., optimal terminal wealth is indeed given by WT∗​(κ,ξT)=𝒳​(κ​ξT)W\_{T}^{\*}(\kappa,\xi\_{T})=\mathcal{X}(\kappa\xi\_{T}). In the last equality, we have used that the budget constraint is binding for an optimal solution to ([B.1](#A2.E1 "In Proof. ‣ B.2 Proof of Theorem 5.1 ‣ Appendix B Technical Proofs ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")).

The proof of existence of the Lagrangian multiplier κ∗\kappa^{\*} is as follows. Fix ξT>0\xi\_{T}>0. Define

|  |  |  |
| --- | --- | --- |
|  | χ​(κ):=𝔼ℙ​[ξT​WT∗​(κ,ξT)]=𝔼ℙ​[ξT​𝒳​(κ​ξT)].\chi(\kappa):=\mathbb{E}^{\mathbb{P}}[\xi\_{T}W\_{T}^{\*}(\kappa,\xi\_{T})]=\mathbb{E}^{\mathbb{P}}[\xi\_{T}\mathcal{X}(\kappa\xi\_{T})]. |  |

We first show that χ​(κ)\chi(\kappa) is monotone decreasing in κ\kappa. By Lemma [A.3](#A1.Thmlemma3 "Lemma A.3. ‣ A.1 Filtering Arguments ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity"), we observe that

|  |  |  |
| --- | --- | --- |
|  | χ​(κ)=𝔼ℙ^​[e−r​T​𝒳​(κ​ξT)]=𝔼ℙ^​[e−r​T​𝒳​(κ​e−r​T/F​(T,YT))].\displaystyle\chi(\kappa)={\mathbb{E}^{\widehat{\mathbb{P}}}}[e^{-rT}\mathcal{X}(\kappa\xi\_{T})]={\mathbb{E}^{\widehat{\mathbb{P}}}}[e^{-rT}\mathcal{X}(\kappa e^{-rT}/F(T,Y\_{T}))]. |  |

Clearly, χ​(κ)\chi(\kappa) is continuous and decreasing. Furthermore, limκ→0χ​(κ)=+∞\lim\_{\kappa\to 0}\chi(\kappa)=+\infty, and limκ→∞χ​(κ)=0\lim\_{\kappa\to\infty}\chi(\kappa)=0. Therefore, there exists a unique κw∗>0\kappa^{\*}\_{w}>0 such that χ​(κw∗)=w\chi(\kappa^{\*}\_{w})=w.

Next we show the optimal investment strategy. By martingale representation property of the Brownian filtration (e.g., Theorem 3.4.2 in Karatzas and Shreve [[1998b](#bib.bib73 "Brownian motion and stochastic calculus")]), we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | e−r​t​W^t:\displaystyle e^{-rt}\widehat{W}\_{t}: | =e−r​T​𝔼ℙ^​[𝒳​(κw∗​ξT)|ℱtY]\displaystyle=e^{-rT}{\mathbb{E}^{\widehat{\mathbb{P}}}}[\mathcal{X}(\kappa^{\*}\_{w}\xi\_{T})|\mathcal{F}\_{t}^{Y}] |  | (B.2) |
|  |  | =w+∫0te−r​s​π^s​σ​𝑑Ys,t∈[0,T]\displaystyle=w+\int^{t}\_{0}e^{-rs}\widehat{\pi}\_{s}\sigma dY\_{s},\quad t\in[0,T] |  |

for some 𝔽Y\mathbb{F}^{Y}-progressively measurable process π^:[0,T]×Ω→ℝ\widehat{\pi}:[0,T]\times\Omega\to\mathbb{R} that satisfies ∫0Te−2​r​s​‖π^t‖2​𝑑t<∞\int^{T}\_{0}e^{-2rs}||\widehat{\pi}\_{t}||^{2}dt<\infty a.s. (with respect to both ℙ\mathbb{P} and ℙ^\widehat{\mathbb{P}}). Furthermore, by comparing ([A.6](#A1.E6 "In A.1 Filtering Arguments ‣ Appendix A Notation and Auxiliary Lemmata ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) and ([B.2](#A2.E2 "In Proof. ‣ B.2 Proof of Theorem 5.1 ‣ Appendix B Technical Proofs ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Wtπ^=W^t\displaystyle W^{\widehat{\pi}}\_{t}=\widehat{W}\_{t} | =e−r​(T−t)​𝔼ℙ^​[𝒳​(κw∗​ξT)|ℱtY]\displaystyle=e^{-r(T-t)}\mathbb{E}^{\widehat{\mathbb{P}}}[\mathcal{X}(\kappa^{\*}\_{w}\xi\_{T})|\mathcal{F}\_{t}^{Y}] |  | (B.3) |
|  |  | =𝒴​(T−t,Yt),t∈[0,T],\displaystyle=\mathcal{Y}(T-t,Y\_{t}),\quad t\in[0,T], |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒴(s,y):={e−r​s​∫ℝ𝒳​(κw∗​e−r​TF​(T,y+z))​φs​(z)​𝑑z,0<s≤T,𝒳​(κw∗​e−r​TF​(T,y)),s=0.\mathcal{Y}(s,y):=\begin{cases}\displaystyle e^{-rs}\int\_{\mathbb{R}}\mathcal{X}\!\left(\frac{\kappa^{\*}\_{w}e^{-rT}}{F(T,y+z)}\right)\varphi\_{s}(z)\,dz,&0<s\leq T,\\[5.0pt] \displaystyle\mathcal{X}\!\left(\frac{\kappa^{\*}\_{w}e^{-rT}}{F(T,y)}\right),&s=0.\end{cases} |  | (B.4) |

Here φs​(z):=(2​π​s)−1/2​e−z2/(2​s)\varphi\_{s}(z):=(2\pi s)^{-1/2}e^{-z^{2}/(2s)} is the Gaussian density function.
Together with ([B.2](#A2.E2 "In Proof. ‣ B.2 Proof of Theorem 5.1 ‣ Appendix B Technical Proofs ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")), the equations ([B.3](#A2.E3 "In Proof. ‣ B.2 Proof of Theorem 5.1 ‣ Appendix B Technical Proofs ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) and ([B.4](#A2.E4 "In Proof. ‣ B.2 Proof of Theorem 5.1 ‣ Appendix B Technical Proofs ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) lead to the expression

|  |  |  |
| --- | --- | --- |
|  | πt∗=π^t=1σ​∇𝒴​(T−t,Yt),0≤t<T.\pi^{\*}\_{t}=\widehat{\pi}\_{t}=\frac{1}{\sigma}\nabla\mathcal{Y}(T-t,Y\_{t}),\quad 0\leq t<T. |  |

Finally, in conjunction with ([B.4](#A2.E4 "In Proof. ‣ B.2 Proof of Theorem 5.1 ‣ Appendix B Technical Proofs ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")), we have the gradient

|  |  |  |
| --- | --- | --- |
|  | ∇𝒴​(s,y)=−κw∗​e−r​(T+s)​∫ℝG​(T,y+z)F​(T,y+z)​𝒳′​(κw∗​e−r​TF​(T,y+z))​φs​(z)​𝑑z.\nabla\mathcal{Y}(s,y)=-\kappa^{\*}\_{w}e^{-r(T+s)}\int\_{\mathbb{R}}\frac{G(T,y+z)}{F(T,y+z)}\mathcal{X}^{\prime}\!\left(\frac{\kappa^{\*}\_{w}e^{-rT}}{F(T,y+z)}\right)\varphi\_{s}(z)\,dz. |  |

where G​(t,y):=∇FF​(t,y)G(t,y):=\frac{\nabla F}{F}(t,y).
Then the value function of problem ([5.6](#S5.E6 "In 5.2 Modeling Delegated Portfolio Management with Nonlinear Payoffs ‣ 5 Application: Convex Incentive Contracts with Smooth Ambiguity Preferences ‣ Nonconcave Portfolio Choice under Smooth Ambiguity")) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(w;𝒬)\displaystyle V(w;\mathcal{Q}) | =𝔼ℙ​[u​(g​(WT∗))]\displaystyle=\mathbb{E}^{\mathbb{P}}\bigl[u\bigl(g(W\_{T}^{\*})\bigr)\bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙ​[u​(g​(𝒳​(κw∗​e−r​T/F​(T,YT))))]\displaystyle=\mathbb{E}^{\mathbb{P}}\Bigl[u\bigl(g(\mathcal{X}(\kappa^{\*}\_{w}e^{-rT}/F(T,Y\_{T})))\bigr)\Bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙ^​[F​(T,YT)​u​(g​(𝒳​(e−r​T​κw∗/F​(T,YT))))]\displaystyle=\mathbb{E}^{\widehat{\mathbb{P}}}\Bigl[F(T,Y\_{T})\,u\bigl(g(\mathcal{X}(e^{-rT}\kappa^{\*}\_{w}/F(T,Y\_{T})))\bigr)\Bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫ℝF​(T,z)​u​(g​(𝒳​(e−r​T​κw∗F​(T,z))))​φT​(z)​𝑑z.\displaystyle=\int\_{\mathbb{R}}F(T,z)\,u\!\left(g\!\left(\mathcal{X}\!\left(\frac{e^{-rT}\kappa^{\*}\_{w}}{F(T,z)}\right)\right)\right)\varphi\_{T}(z)\,dz. |  |

∎

## Appendix C Factorial Design

Table C.2: Full 232^{3} factorial design

| Prior (A) | RRA (B) | RAA (C) | q∗q^{\*} |
| --- | --- | --- | --- |
| Low | Low | Low | 0.392 |
| High | Low | Low | 0.663 |
| Low | High | Low | 0.413 |
| High | High | Low | 0.733 |
| Low | Low | High | 0.079 |
| High | Low | High | 0.103 |
| Low | High | High | 0.104 |
| High | High | High | 0.127 |

We implement a 232^{3} design with xA,xB,xC∈{−1,+1}x\_{A},x\_{B},x\_{C}\in\{-1,+1\}
denoting the baseline prior, RRA, and RAA.
Effects are obtained from the saturated linear representation

|  |  |  |
| --- | --- | --- |
|  | q∗=β0+βA​xA+βB​xB+βC​xC+βA​B​xA​xB+βA​C​xA​xC+βB​C​xB​xC+βA​B​C​xA​xB​xC.q^{\*}=\beta\_{0}+\beta\_{A}x\_{A}+\beta\_{B}x\_{B}+\beta\_{C}x\_{C}+\beta\_{AB}x\_{A}x\_{B}+\beta\_{AC}x\_{A}x\_{C}+\beta\_{BC}x\_{B}x\_{C}+\beta\_{ABC}x\_{A}x\_{B}x\_{C}. |  |

Under ±1\pm 1 coding, each effect equals the difference in conditional means. Table [C.2](#A3.T2 "Table C.2 ‣ Appendix C Factorial Design ‣ Nonconcave Portfolio Choice under Smooth Ambiguity") reports the eight solutions.

BETA