---
authors:
- Johannes Langner
- Gregor Svindland
doc_id: arxiv:2601.19511v1
family_id: arxiv:2601.19511
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: "\U0001D4AB-Sensitive Functions and Localizations1footnote 11footnote 1funded
  by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"
url_abs: http://arxiv.org/abs/2601.19511v1
url_html: https://arxiv.org/html/2601.19511v1
venue: arXiv q-fin
version: 1
year: 2026
---


Johannes Langner222johannes.langner@insurance.uni-hannover.de   & Gregor Svindland333gregor.svindland@insurance.uni-hannover.de

(25.01.2026)

###### Abstract

This paper assumes a robust stochastic model where a set 𝒫\mathcal{P} of probability measures replaces the single probability measure of dominated models. We introduce and study 𝒫\mathcal{P}-sensitive functions defined on robust function spaces of random variables. We show that 𝒫\mathcal{P}-sensitive functions are precisely those that admit a representation via so-called functional localization.
The theory is applied to solving robust optimization problems, to convex risk measures, and to the study of no arbitrage in robust one-period financial models. 
  
Keywords: robustness, non-dominated set of probabilities, 𝒫\mathcal{P}-sensitivity, functional localization, convex risk measures, superhedging functional 
  
MSC2020: 46A20, 46E30, 46N10, 46N30, 60B11, 91G80 
  
JEL: C65, D80

## 1 Introduction

We consider a robust probabilistic model given by a measure space (Ω,ℱ)(\Omega,\mathcal{F}) and a non-empty set of probability measures 𝒫\mathcal{P} on (Ω,ℱ)(\Omega,\mathcal{F}). The set 𝒫\mathcal{P} describes the degree of ambiguity, or Knightian uncertainty, inherent in the model. This includes the case where 𝒫={P}\mathcal{P}=\{P\}, where there is no ambiguity, as well as the case in which there exists a probability measure PP dominating each element in 𝒫\mathcal{P} and ambiguity may be present. In both cases, the mathematical machinery used to handle such models typically relies on the dominating probability measure PP, which, among other things, determines relevant model spaces of random variables and provides exhaustion and approximation methods. If 𝒫\mathcal{P} is not dominated by a probability measure, then the aforementioned approaches and techniques fail, and we are in a truly robust setting. It is this latter situation that we have in mind throughout this study, even though we do not exclude the other cases. Some prominent examples of robust stochastic models and robust model spaces considered in financial mathematics are the volatility uncertainty models studied in, e.g., [[3](https://arxiv.org/html/2601.19511v1#bib.bib8 "Duality theory for robust utility maximisation")], [[13](https://arxiv.org/html/2601.19511v1#bib.bib21 "Quasi-sure analysis, aggregation and dual representations of sublinear expectations in general spaces")], [[26](https://arxiv.org/html/2601.19511v1#bib.bib129 "Second order reflected backward stochastic differential equations")], [[27](https://arxiv.org/html/2601.19511v1#bib.bib130 "Superhedging and dynamic risk measures under volatility uncertainty")], [[29](https://arxiv.org/html/2601.19511v1#bib.bib44 "Quasi-sure stochastic analysis through aggregation")], [[28](https://arxiv.org/html/2601.19511v1#bib.bib131 "Wellposedness of second order backward SDEs")], and [[30](https://arxiv.org/html/2601.19511v1#bib.bib132 "Dual formulation of second order target problems")], as well as the models applied to study the Fundamental Theorem of Asset Pricing and the superhedging problem in [[2](https://arxiv.org/html/2601.19511v1#bib.bib7 "Pathwise superhedging on prediction sets")], [[8](https://arxiv.org/html/2601.19511v1#bib.bib12 "No-arbitrage with multiple-priors in discrete time")], [[9](https://arxiv.org/html/2601.19511v1#bib.bib13 "Arbitrage and duality in nondominated discrete-time models")], [[10](https://arxiv.org/html/2601.19511v1#bib.bib15 "Pointwise arbitrage pricing theory in discrete time")], [[11](https://arxiv.org/html/2601.19511v1#bib.bib17 "Arbitrage-free modeling under knightian uncertainty")], [[12](https://arxiv.org/html/2601.19511v1#bib.bib20 "Super‐replication with transaction costs under model uncertainty for continuous processes")], and [[20](https://arxiv.org/html/2601.19511v1#bib.bib29 "Robust pricing–hedging dualities in continuous time")]. For further references, we refer to the references in those articles.

Let (Ω,ℱ,𝒫)(\Omega,\mathcal{F},\mathcal{P}) be a robust probabilistic model and define the upper probability given by 𝒫\mathcal{P} as

|  |  |  |
| --- | --- | --- |
|  | c​(A):=supP∈𝒫P​(A),A∈ℱ.c(A):=\sup\_{P\in\mathcal{P}}P(A),\qquad A\in\mathcal{F}. |  |

The robust function space Lc0L^{0}\_{c} consists of equivalence classes of random variables, which are identified up to PP-almost sure equality under each P∈𝒫P\in\mathcal{P} (see Section [2](https://arxiv.org/html/2601.19511v1#S2 "2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")). If 𝒫={P}\mathcal{P}=\{P\}, then, of course, Lc0=LP0:=L0​(Ω,ℱ,P)L^{0}\_{c}=L^{0}\_{P}:=L^{0}(\Omega,\mathcal{F},P).

In this paper, we consider functions ff mapping subsets 𝒳\mathcal{X} of Lc0L^{0}\_{c} to the extended real numbers. Examples of such functions in financial mathematics include robust risk measures, the superhedging functional in robust financial market models, and robust utilities. The primary question we address is under which conditions such a function f:𝒳→[−∞,∞]f\colon\mathcal{X}\to[-\infty,\infty] can be represented as

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(X)=supQ∈𝒬fQ​(X),X∈𝒳.f(X)=\sup\_{Q\in\mathcal{Q}}f^{Q}(X),\qquad X\in\mathcal{X}. |  | (1) |

Here 𝒬\mathcal{Q} is a set of probability measures on (Ω,ℱ)(\Omega,\mathcal{F}), and fQ:𝒳→[−∞,∞]f^{Q}\colon\mathcal{X}\to[-\infty,\infty], Q∈𝒬Q\in\mathcal{Q}, are functions that are consistent with the respective QQ in the sense that, whenever X,Y∈𝒳X,Y\in\mathcal{X} look identical under QQ, that is, Q​(x=y)=1Q(x=y)=1 for all representatives x∈Xx\in X and y∈Yy\in Y, we have fQ​(X)=fQ​(Y)f^{Q}(X)=f^{Q}(Y). Due to this consistency, each fQf^{Q} may also be identified with a function on a subset of the reduced model space LQ0L^{0}\_{Q}.

The existence of a robust representation ([1](https://arxiv.org/html/2601.19511v1#S1.E1 "In 1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) is very useful when handling robust models, since it allows to break down the mathematical reasoning for ff to the classical dominated level, that is, to argue for fQf^{Q} under each Q∈𝒬Q\in\mathcal{Q}, and then to aggregate over the probability measures Q∈𝒬Q\in\mathcal{Q}. We show that the existence of a representation ([1](https://arxiv.org/html/2601.19511v1#S1.E1 "In 1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) is equivalent to a property called 𝒫\mathcal{P}-sensitivity of ff. For sets of (equivalence classes of) random variables, this property has already been studied, for instance, in [[11](https://arxiv.org/html/2601.19511v1#bib.bib17 "Arbitrage-free modeling under knightian uncertainty")], [[22](https://arxiv.org/html/2601.19511v1#bib.bib34 "Bipolar theorems for sets of nonnegative random variables")], and [[25](https://arxiv.org/html/2601.19511v1#bib.bib38 "Fatou closedness under model uncertainty")]. We extend the definition of 𝒫\mathcal{P}-sensitivity from sets to functions and illustrate its usefulness.

A family of functions (fQ)Q∈𝒬(f^{Q})\_{Q\in\mathcal{Q}} such that ([1](https://arxiv.org/html/2601.19511v1#S1.E1 "In 1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) holds, is called a functional localization of ff. This localization of ff is not unique, and there are several ways to construct a localizing family depending on the properties of the given function ff. In particular, we study two canonical types of localizations. One is based on a primal reduction of the function ff given a probability measure QQ via its level sets, while the other takes a dual approach in the sense of the Fenchel-Moreau theorem. We derive conditions under which both localizations coincide.

For illustration, the theory is applied to optimization problems, convex risk measures, and the superhedging functional in a robust one-period financial market model. For 𝒫\mathcal{P}-sensitive functions ff with localization (fQ)Q∈𝒬(f^{Q})\_{Q\in\mathcal{Q}}, we show how solving optimization problems for ff may be reduced to solving corresponding optimization problems for each fQf^{Q} in a dominated framework and then aggregating the optimizers. As regards convex risk measures, we are interested in the interplay of a given risk measure defined on the robust model space under 𝒫\mathcal{P}—which is understood as an aggregate of risk opinions—with the elements of its two canonical localizations, which may be interpreted as individual risk opinions under some probability measure QQ. We show that there may be inconsistencies, which we call localization bubbles, when breaking down the risk measure to the local dominated level, and we provide conditions under which such localization bubbles do not appear. In our study of robust one-period financial market models, suitable localizations of the superhedging functional provide different robust versions of the Fundamental Theorem of Asset Pricing.

#### Further Related Literature

[[14](https://arxiv.org/html/2601.19511v1#bib.bib23 "Function spaces and capacity related to a sublinear expectation: Application to G-Brownian motion paths")] investigate capacities and robust function spaces based on sublinear expectations, in particular, GG-expectation.
[[23](https://arxiv.org/html/2601.19511v1#bib.bib35 "Model uncertainty: a reverse approach")] approach model uncertainty from a reverse perspective, aiming to understand the conditions that a probabilistic model must satisfy to obtain robust analogs of useful properties known in dominated frameworks.
In [[7](https://arxiv.org/html/2601.19511v1#bib.bib11 "Risk measuring under model uncertainty")], risk measures under model uncertainty are studied with a focus on dual representations. Robust duality has further been explored by [[5](https://arxiv.org/html/2601.19511v1#bib.bib10 "Duality and general equilibrium theory under knightian uncertainty")], who examine general equilibrium theory under Knightian uncertainty.

#### Outline

The paper is organized as follows. In Section [2](https://arxiv.org/html/2601.19511v1#S2 "2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), we introduce some notation and present a first discussion of 𝒫\mathcal{P}-sensitivity for both sets and functions. Section [3](https://arxiv.org/html/2601.19511v1#S3 "3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") studies the relation between 𝒫\mathcal{P}-sensitivity and functional localization. Moreover, we define and analyze the different canonical localizations mentioned above. Lastly, in Section [4](https://arxiv.org/html/2601.19511v1#S4 "4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), we consider applications to optimization problems (see Section [4.1](https://arxiv.org/html/2601.19511v1#S4.SS1 "4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")), convex risk measures (see Section [4.2](https://arxiv.org/html/2601.19511v1#S4.SS2 "4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")), and the superhedging functional (see Section [4.3](https://arxiv.org/html/2601.19511v1#S4.SS3 "4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")).

## 2 Preliminaries and Notation

### 2.1 Basics

Throughout this paper, (Ω,ℱ)(\Omega,\mathcal{F}) is an arbitrary measurable space. We denote by c​aca the real vector space of all countably additive finite variation set functions μ:ℱ→ℝ\mu\colon\mathcal{F}\rightarrow\mathbb{R}, and by c​a+ca\_{+} its positive elements (μ∈c​a+⇔∀A∈ℱ​μ​(A)≥0\mu\in ca\_{+}\Leftrightarrow\forall A\in\mathcal{F}\ \mu(A)\geq 0), that is, all finite measures on (Ω,ℱ)(\Omega,\mathcal{F}).

|  |  |  |  |
| --- | --- | --- | --- |
|  | |μ|​(A):=sup{μ​(B)−μ​(A∖B)∣B∈ℱ,B⊆A},A∈ℱ,\lvert\mu\rvert(A):=\sup\{\mu(B)-\mu(A\setminus B)\mid B\in\mathcal{F},B\subseteq A\},\qquad A\in\mathcal{F}, |  | (2) |

denotes the total variation of μ∈c​a\mu\in ca, which is a measure |μ|∈c​a+|\mu|\in ca\_{+}. Given non-empty subsets 𝔊\mathfrak{G} and ℑ\mathfrak{I} of c​a+ca\_{+}, we say that ℑ\mathfrak{I} dominates 𝔊\mathfrak{G} (𝔊≪ℑ\mathfrak{G}\ll\mathfrak{I}) if for all N∈ℱN\in\mathcal{F} satisfying supν∈ℑν​(N)=0\sup\_{\nu\in\mathfrak{I}}\nu(N)=0, we have supμ∈𝔊μ​(N)=0\sup\_{\mu\in\mathfrak{G}}\mu(N)=0. 𝔊\mathfrak{G} and ℑ\mathfrak{I} are equivalent (𝔊≈ℑ\mathfrak{G}\approx\mathfrak{I}) if 𝔊≪ℑ\mathfrak{G}\ll\mathfrak{I} and ℑ≪𝔊\mathfrak{I}\ll\mathfrak{G}. For the sake of brevity, for μ∈c​a+\mu\in ca\_{+} we shall write 𝔊≪μ\mathfrak{G}\ll\mu, μ≪ℑ\mu\ll\mathfrak{I}, and μ≈𝔊\mu\approx\mathfrak{G} instead of 𝔊≪{μ}\mathfrak{G}\ll\{\mu\}, {μ}≪ℑ\{\mu\}\ll\mathfrak{I}, and {μ}≈𝔊\{\mu\}\approx\mathfrak{G}, respectively.

𝔓​(Ω)⊆c​a+\mathfrak{P}(\Omega)\subseteq ca\_{+} denotes the set of probability measures on (Ω,ℱ)(\Omega,\mathcal{F}) and the letters 𝒫\mathcal{P} and 𝒬\mathcal{Q} are used to denote non-empty subsets of 𝔓​(Ω)\mathfrak{P}(\Omega).
Fix such a set 𝒫\mathcal{P}. We then write cc for the induced upper probability c:ℱ→[0,1]c\colon\mathcal{F}\rightarrow[0,1] defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(A):=supP∈𝒫P​(A),A∈ℱ.c(A):=\sup\_{P\in\mathcal{P}}P(A),\qquad A\in\mathcal{F}. |  | (3) |

An event A∈ℱA\in\mathcal{F} is called 𝒫\mathcal{P}-polar if c​(A)=0c(A)=0. A property holds 𝒫\mathcal{P}-quasi surely (q.s.) if it holds outside a 𝒫\mathcal{P}-polar event. We set c​ac:={μ∈c​a∣|μ|≪𝒫}ca\_{c}:=\{\mu\in ca\mid|\mu|\ll\mathcal{P}\}, c​ac+:=c​a+∩c​acca\_{c+}:=ca\_{+}\cap ca\_{c}, and 𝔓c​(Ω):=𝔓​(Ω)∩c​ac\mathfrak{P}\_{c}(\Omega):=\mathfrak{P}(\Omega)\cap ca\_{c}.

Consider the ℝ\mathbb{R}-vector space ℒ0:=ℒ0​(Ω,ℱ)\mathcal{L}^{0}:=\mathcal{L}^{0}(\Omega,\mathcal{F}) of all real-valued random variables x:Ω→ℝx\colon\Omega\rightarrow\mathbb{R} as well as its subspace 𝒩:={x∈ℒ0∣c​(|x|>0)=0}\mathcal{N}:=\{x\in\mathcal{L}^{0}\mid c(\lvert x\rvert>0)=0\}. The quotient space Lc0:=ℒ0/𝒩L^{0}\_{c}:=\mathcal{L}^{0}/\mathcal{N} consists of equivalence classes XX of random variables up to 𝒫\mathcal{P}-q.s. equality comprising representatives x∈Xx\in X. The equivalence class induced by x∈ℒ0x\in\mathcal{L}^{0} in Lc0L^{0}\_{c} is denoted by [x]c[x]\_{c}. The space Lc0L^{0}\_{c} carries the so-called 𝒫\mathcal{P}-quasi-sure order ≼𝒫\preccurlyeq\_{\mathcal{P}} as a natural vector space order: X,Y∈Lc0X,Y\in L^{0}\_{c} satisfy X≼𝒫YX\preccurlyeq\_{\mathcal{P}}Y if for x∈Xx\in X and y∈Yy\in Y, x≤yx\leq y 𝒫\mathcal{P}-q.s., that is, {x>y}\{x>y\} is 𝒫\mathcal{P}-polar. In order to facilitate the notation, we suppress the dependence of ≼𝒫\preccurlyeq\_{\mathcal{P}} on 𝒫\mathcal{P} and simply write ≼\preccurlyeq if there is no risk of confusion.

For an event A∈ℱA\in\mathcal{F}, χA\chi\_{A} denotes the indicator of the event (i.e., χA​(ω)=1\chi\_{A}(\omega)=1 if and only if ω∈A\omega\in A, and χA​(ω)=0\chi\_{A}(\omega)=0 otherwise), while 𝟏A:=[χA]c\mathbf{1}\_{A}:=[\chi\_{A}]\_{c} denotes the generated equivalence class in Lc0L^{0}\_{c}. Throughout the paper, for convenience, we identify the constants m∈ℝm\in\mathbb{R} with the (equivalence classes of) constant random variables they induce. In particular, m=[m]c=m⋅𝟏Ωm=[m]\_{c}=m\cdot\mathbf{1}\_{\Omega}.

A subspace of Lc0L^{0}\_{c} which will turn out to be important for our studies is the space Lc∞L^{\infty}\_{c} of equivalence classes of 𝒫\mathcal{P}-q.s. bounded random variables, i.e.,

|  |  |  |
| --- | --- | --- |
|  | Lc∞:={X∈Lc0∣∃m>0:|X|≼m}.L^{\infty}\_{c}:=\{X\in L^{0}\_{c}\mid\exists m>0\colon\lvert X\rvert\preccurlyeq m\}. |  |

Lc∞L^{\infty}\_{c} is a Banach lattice when endowed with the norm

|  |  |  |
| --- | --- | --- |
|  | ∥X∥c,∞:=inf{m>0∣|X|≼m},X∈Lc0.\lVert X\rVert\_{c,\infty}:=\inf\{m>0\mid\lvert X\rvert\preccurlyeq m\},\qquad X\in L^{0}\_{c}. |  |

Lc+0L^{0}\_{c+} and Lc+∞L^{\infty}\_{c+} denote the positive cones of Lc0L^{0}\_{c} and Lc∞L^{\infty}\_{c}, respectively. If 𝒫={P}\mathcal{P}=\{P\} is given by a singleton and thus c=Pc=P, we write LP0L^{0}\_{P}, LP∞L^{\infty}\_{P}, and [x]P[x]\_{P} instead of Lc0L^{0}\_{c}, Lc∞L^{\infty}\_{c}, and [x]c[x]\_{c}, and similarly for other expressions in which cc appears. Also, the 𝒫\mathcal{P}-q.s. order in this case coincides with the PP-almost-sure (a.s.) order, which we will denote by ≤P\leq\_{P} when working with both the 𝒫\mathcal{P}-q.s. order ≼\preccurlyeq for some set 𝒫⊆𝔓​(Ω)\mathcal{P}\subseteq\mathfrak{P}(\Omega) and the PP-a.s. order for some P∈𝔓c​(Ω)P\in\mathfrak{P}\_{c}(\Omega). In that respect, note that ≤P\leq\_{P} is well defined on Lc0L^{0}\_{c} for any P∈𝔓c​(Ω)P\in\mathfrak{P}\_{c}(\Omega).

Often we will, as is common practice, identify equivalence classes of random variables with their representatives. However, sometimes it will be helpful to distinguish between them to avoid confusion. Let us clarify this further: For any X∈Lc0X\in L^{0}\_{c}, we have X={x∈ℒ0∣x∼y}X=\{x\in\mathcal{L}^{0}\mid x\sim y\} for some y∈ℒ0y\in\mathcal{L}^{0} where we write x∼yx\sim y to indicate that {x≠y}\{x\neq y\} is 𝒫\mathcal{P}-polar. Any measure P∈𝔓c​(Ω)P\in\mathfrak{P}\_{c}(\Omega) is consistent with the equivalence relation ∼\sim in the sense that

|  |  |  |
| --- | --- | --- |
|  | ∀x,y∈ℒ0:x∼y⟹P​(x=y)=1.\forall x,y\in\mathcal{L}^{0}\colon\qquad x\sim y\Longrightarrow P(x=y)=1. |  |

In that case we write, for instance, EP​[X]E\_{P}[X] for the expectation of XX under PP, which actually means EP​[x]E\_{P}[x] for any x∈Xx\in X provided the latter integral is well-defined. Also, we write expressions like P​(X=Y)P(X=Y), where Y∈Lc0Y\in L^{0}\_{c}, actually meaning P​(x=y)P(x=y) for arbitrary x∈Xx\in X and y∈Yy\in Y.

### 2.2 𝓟\boldsymbol{\mathcal{P}}-sensitive Sets and Functions

Let 𝒫⊆𝔓​(Ω)\mathcal{P}\subseteq\mathfrak{P}(\Omega) and denote by cc the corresponding upper probability ([3](https://arxiv.org/html/2601.19511v1#S2.E3 "In 2.1 Basics ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")). For any given Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega), the following map identifies any X,Y∈Lc0X,Y\in L^{0}\_{c} which appear to coincide under QQ, that is, Q​(x=y)=1Q(x=y)=1 for all x∈Xx\in X and y∈Yy\in Y:

|  |  |  |
| --- | --- | --- |
|  | jQ:Lc0→LQ0,[x]c↦[x]Q.j\_{Q}\colon L^{0}\_{c}\rightarrow L^{0}\_{Q},\qquad[x]\_{c}\mapsto[x]\_{Q}. |  |

Note that jQj\_{Q} is linear and monotone, in the sense that X≼YX\preccurlyeq Y implies jQ​(X)≤QjQ​(Y)j\_{Q}(X)\leq\_{Q}j\_{Q}(Y), and that jQ​(m)=mj\_{Q}(m)=m for all m∈ℝm\in\mathbb{R}.

In the sequel, let 𝒳⊆Lc0\mathcal{X}\subseteq L^{0}\_{c} be non-empty.

###### Definition 2.1.

A set 𝒞⊆𝒳\mathcal{C}\subseteq\mathcal{X} is called 𝒫\mathcal{P}-sensitive (in 𝒳\mathcal{X}) if either 𝒞=∅\mathcal{C}=\emptyset or if for all X∈𝒳X\in\mathcal{X}

|  |  |  |
| --- | --- | --- |
|  | X∈𝒞⇔∀Q∈𝔓c​(Ω):jQ​(X)∈jQ​(𝒞).X\in\mathcal{C}\qquad\Leftrightarrow\qquad\forall Q\in\mathfrak{P}\_{c}(\Omega)\colon\,j\_{Q}(X)\in j\_{Q}(\mathcal{C}). |  |

Clearly, the non-trivial implication in Definition [2.1](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem1 "Definition 2.1. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") is that ∀Q∈𝔓c​(Ω):jQ​(X)∈jQ​(𝒞)\forall Q\in\mathfrak{P}\_{c}(\Omega)\colon\,j\_{Q}(X)\in j\_{Q}(\mathcal{C}) implies X∈𝒞X\in\mathcal{C}. Indeed, a set 𝒞\mathcal{C} is 𝒫\mathcal{P}-sensitive if it is completely determined by its image under each model Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega). Thus, if X∈𝒳X\in\mathcal{X} looks like a member of 𝒞\mathcal{C} under each Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega), i.e., jQ​(X)∈jQ​(𝒞)j\_{Q}(X)\in j\_{Q}(\mathcal{C}) for all Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega), then in fact X∈𝒞X\in\mathcal{C}. Trivially, if 𝒫={P}\mathcal{P}=\{P\}, then every set 𝒞⊆LP0\mathcal{C}\subseteq L^{0}\_{P} is PP-sensitive. It has been noticed earlier in, e.g., [[22](https://arxiv.org/html/2601.19511v1#bib.bib34 "Bipolar theorems for sets of nonnegative random variables")] and [[25](https://arxiv.org/html/2601.19511v1#bib.bib38 "Fatou closedness under model uncertainty")] that 𝒫\mathcal{P}-sensitivity of a set 𝒞\mathcal{C} is an essential property to handle sets in non-dominated robust models.

Before we extend the definition of 𝒫\mathcal{P}-sensitivity from sets to functions, let us collect some notions and useful results for 𝒫\mathcal{P}-sensitive sets. Firstly, sometimes it is useful to work with a stronger representation of 𝒞\mathcal{C}.

###### Definition 2.2.

Let 𝒞⊆𝒳\mathcal{C}\subseteq\mathcal{X}. 𝒬⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathfrak{P}\_{c}(\Omega) is called a reduction set for 𝒞\mathcal{C} if 𝒬≠∅\mathcal{Q}\neq\emptyset and for all X∈𝒳X\in\mathcal{X}

|  |  |  |  |
| --- | --- | --- | --- |
|  | X∈𝒞⇔∀Q∈𝒬:jQ​(X)∈jQ​(𝒞).X\in\mathcal{C}\qquad\Leftrightarrow\qquad\forall Q\in\mathcal{Q}\colon\,j\_{Q}(X)\in j\_{Q}(\mathcal{C}). |  | (4) |

Clearly, any 𝒫\mathcal{P}-sensitive set admits the reduction set 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega). The following lemma relates reduction sets to each other and, in particular, shows that any set satisfying ([4](https://arxiv.org/html/2601.19511v1#S2.E4 "In Definition 2.2. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) is indeed 𝒫\mathcal{P}-sensitive. Its straightforward proof is provided in [[22](https://arxiv.org/html/2601.19511v1#bib.bib34 "Bipolar theorems for sets of nonnegative random variables")].

###### Lemma 2.3 ([[22](https://arxiv.org/html/2601.19511v1#bib.bib34 "Bipolar theorems for sets of nonnegative random variables"), Lemma 2.10]).

Let 𝒞⊆𝒳\mathcal{C}\subseteq\mathcal{X}.

1. (i)

   Consider a reduction set 𝒬1\mathcal{Q}\_{1} for 𝒞\mathcal{C} and any other set of probability measures 𝒬2⊆𝔓c​(Ω)\mathcal{Q}\_{2}\subseteq\mathfrak{P}\_{c}(\Omega) such that 𝒬1⊆𝒬2\mathcal{Q}\_{1}\subseteq\mathcal{Q}\_{2}. Then 𝒬2\mathcal{Q}\_{2} is also a reduction set for 𝒞\mathcal{C}.
2. (ii)

   𝒞\mathcal{C} is 𝒫\mathcal{P}-sensitive if and only if there exists a reduction set for 𝒞\mathcal{C}.

The reason for considering other reduction sets than simply 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega) will become evident throughout the paper.

###### Lemma 2.4 ([[22](https://arxiv.org/html/2601.19511v1#bib.bib34 "Bipolar theorems for sets of nonnegative random variables"), Lemma 2.11]).

Let II be a non-empty index set and let 𝒞α⊆𝒳\mathcal{C}\_{\alpha}\subseteq\mathcal{X}, α∈I\alpha\in I, be 𝒫\mathcal{P}-sensitive. Then

|  |  |  |
| --- | --- | --- |
|  | 𝒞:=⋂α∈I𝒞α\mathcal{C}:=\bigcap\_{\alpha\in I}\mathcal{C}\_{\alpha} |  |

is also 𝒫\mathcal{P}-sensitive. If for each α∈I\alpha\in I, 𝒬α⊆𝔓c​(Ω)\mathcal{Q}\_{\alpha}\subseteq\mathfrak{P}\_{c}(\Omega) is a reduction set for 𝒞α\mathcal{C}\_{\alpha}, then 𝒬:=⋃α∈I𝒬α\mathcal{Q}:=\bigcup\_{\alpha\in I}\mathcal{Q}\_{\alpha} is a reduction set for 𝒞\mathcal{C}.

###### Lemma 2.5.

Let 𝒬⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathfrak{P}\_{c}(\Omega) be non-empty and consider subsets EQ⊆LQ0E\_{Q}\subseteq L^{0}\_{Q}, Q∈𝒬Q\in\mathcal{Q}. Define

|  |  |  |
| --- | --- | --- |
|  | E:={X∈𝒳∣∀Q∈𝒬:jQ​(X)∈EQ}.E:=\{X\in\mathcal{X}\mid\forall Q\in\mathcal{Q}\colon j\_{Q}(X)\in E\_{Q}\}. |  |

Then EE is 𝒫\mathcal{P}-sensitive with reduction set 𝒬\mathcal{Q}.

###### Proof.

Suppose that X∈𝒳X\in\mathcal{X} is such that jQ​(X)∈jQ​(E)j\_{Q}(X)\in j\_{Q}(E) for all Q∈𝒬Q\in\mathcal{Q}. As jQ​(E)⊆EQj\_{Q}(E)\subseteq E\_{Q} for all Q∈𝒬Q\in\mathcal{Q}, we conclude that X∈EX\in E.
∎

Note that in the following we write [−∞,∞][-\infty,\infty] for the set ℝ∪{−∞,∞}\mathbb{R}\cup\{-\infty,\infty\} and (−∞,∞](-\infty,\infty] for ℝ∪{∞}\mathbb{R}\cup\{\infty\}.

###### Definition 2.6.

A function f:𝒳→[−∞,∞]f\colon\mathcal{X}\to[-\infty,\infty] is called (lower) 𝒫\mathcal{P}-sensitive if each (lower) level set Er:={X∈𝒳∣f​(X)≤r}E\_{r}:=\{X\in\mathcal{X}\mid f(X)\leq r\}, r∈ℝr\in\mathbb{R}, is 𝒫\mathcal{P}-sensitive.

Similarly, ff is upper 𝒫\mathcal{P}-sensitive if each upper level set {X∈𝒳∣f​(X)≥r}\{X\in\mathcal{X}\mid f(X)\geq r\}, r∈ℝr\in\mathbb{R}, is 𝒫\mathcal{P}-sensitive.

Note that ff is upper 𝒫\mathcal{P}-sensitive if and only if −f-f is lower 𝒫\mathcal{P}-sensitive. For that reason, we will mainly focus on lower 𝒫\mathcal{P}-sensitive functions in the following and simply refer to them as 𝒫\mathcal{P}-sensitive if there is no risk of confusion.

###### Definition 2.7.

Let f:𝒳→[−∞,∞]f\colon\mathcal{X}\to[-\infty,\infty]. 𝒬⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathfrak{P}\_{c}(\Omega) is called a reduction set for ff if 𝒬≠∅\mathcal{Q}\neq\emptyset and 𝒬\mathcal{Q} is a joint reduction set for all lower level sets ErE\_{r}, r∈ℝr\in\mathbb{R}, of ff.

Clearly, 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega) is a reduction set for every 𝒫\mathcal{P}-sensitive function ff. In analogy to Lemmas [2.3](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem3 "Lemma 2.3 ([22, Lemma 2.10]). ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") and [2.4](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem4 "Lemma 2.4 ([22, Lemma 2.11]). ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), we obtain the corresponding results for functions:

###### Lemma 2.8.

Let f:𝒳→[−∞,∞]f\colon\mathcal{X}\to[-\infty,\infty].

1. (i)

   Consider a reduction set 𝒬1\mathcal{Q}\_{1} for ff and any other set 𝒬2⊆𝔓c​(Ω)\mathcal{Q}\_{2}\subseteq\mathfrak{P}\_{c}(\Omega) such that 𝒬1⊆𝒬2\mathcal{Q}\_{1}\subseteq\mathcal{Q}\_{2}. Then 𝒬2\mathcal{Q}\_{2} is a reduction set for ff too.
2. (ii)

   ff is 𝒫\mathcal{P}-sensitive if and only if there exists a reduction set for ff.

###### Proof.

Recall Lemma [2.3](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem3 "Lemma 2.3 ([22, Lemma 2.10]). ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
∎

###### Lemma 2.9.

Suppose that the members of the family of functions fα:𝒳→[−∞,∞]f\_{\alpha}:\mathcal{X}\to[-\infty,\infty] , α∈I\alpha\in I, for some non-empty index set II are all 𝒫\mathcal{P}-sensitive. Then f:𝒳→[−∞,∞],X↦supα∈Ifα​(X)f:\mathcal{X}\to[-\infty,\infty],\,X\mapsto\sup\_{\alpha\in I}f\_{\alpha}(X), is also 𝒫\mathcal{P}-sensitive.

###### Proof.

Recall Lemma [2.4](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem4 "Lemma 2.4 ([22, Lemma 2.11]). ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
∎

###### Definition 2.10.

Let 𝒬⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathfrak{P}\_{c}(\Omega) be non-empty and Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega). A function f:𝒳→[−∞,∞]f\colon\mathcal{X}\to[-\infty,\infty] is called QQ-consistent (on 𝒳\mathcal{X}) if for any X,Y∈𝒳X,Y\in\mathcal{X} with jQ​(X)=jQ​(Y)j\_{Q}(X)=j\_{Q}(Y), it holds that f​(X)=f​(Y)f(X)=f(Y).

A family of functions fQ:𝒳→[−∞,∞]f^{Q}\colon\mathcal{X}\to[-\infty,\infty], Q∈𝒬Q\in\mathcal{Q}, is called 𝒬\mathcal{Q}-consistent (on 𝒳\mathcal{X}) if fQf^{Q} is QQ-consistent for all Q∈𝒬Q\in\mathcal{Q}.

###### Remark 2.11.

Let Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega).
Any function g:jQ​(𝒳)→[−∞,∞]g\colon j\_{Q}(\mathcal{X})\to[-\infty,\infty] defines a canonical QQ-consistent function f:𝒳→[−∞,∞]f\colon\mathcal{X}\to[-\infty,\infty] by f​(X):=g​(jQ​(X))f(X):=g(j\_{Q}(X)), X∈𝒳X\in\mathcal{X}. Conversely, any QQ-consistent function f:𝒳→[−∞,∞]f\colon\mathcal{X}\to[-\infty,\infty] defines a function g:jQ​(𝒳)→[−∞,∞]g\colon j\_{Q}(\mathcal{X})\to[-\infty,\infty] by g​(X)=f​(Y)g(X)=f(Y) for arbitrary Y∈jQ−1​(X)∩𝒳Y\in j\_{Q}^{-1}(X)\cap\mathcal{X}. We will, with some abuse of notation, denote this function gg by f∘jQ−1f\circ j\_{Q}^{-1}. ⋄\diamond

Again, analogously to Lemma [2.5](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem5 "Lemma 2.5. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), we obtain the following results for functions:

###### Lemma 2.12.

Let 𝒬⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathfrak{P}\_{c}(\Omega) be non-empty and let (fQ)Q∈𝒬(f^{Q})\_{Q\in\mathcal{Q}} be a 𝒬\mathcal{Q}-consistent family of functions on 𝒳\mathcal{X}. Then the function

|  |  |  |
| --- | --- | --- |
|  | f​(X):=supQ∈𝒬fQ​(X),X∈𝒳,f(X):=\sup\_{Q\in\mathcal{Q}}f^{Q}(X),\qquad X\in\mathcal{X}, |  |

is 𝒫\mathcal{P}-sensitive with reduction set 𝒬\mathcal{Q}.

###### Proof.

Fix r∈ℝr\in\mathbb{R} and let Er:={Y∈𝒳∣f​(Y)≤r}E\_{r}:=\{Y\in\mathcal{X}\mid f(Y)\leq r\}. Consider X∈𝒳X\in\mathcal{X} such that jQ​(X)∈jQ​(Er)j\_{Q}(X)\in j\_{Q}(E\_{r}) for all Q∈𝒬Q\in\mathcal{Q}. Then, for any Q∈𝒬Q\in\mathcal{Q}, there exists XQ∈ErX^{Q}\in E\_{r} such that jQ​(X)=jQ​(XQ)j\_{Q}(X)=j\_{Q}(X^{Q}). As (fQ)Q∈𝒬(f^{Q})\_{Q\in\mathcal{Q}} is 𝒬\mathcal{Q}-consistent, it follows that for any Q∈𝒬Q\in\mathcal{Q}

|  |  |  |
| --- | --- | --- |
|  | fQ​(X)=fQ​(XQ)≤f​(XQ)≤r.f^{Q}(X)=f^{Q}(X^{Q})\leq f(X^{Q})\leq r. |  |

Consequently,

|  |  |  |
| --- | --- | --- |
|  | f​(X)=supQ∈𝒬fQ​(X)≤r,f(X)=\sup\_{Q\in\mathcal{Q}}f^{Q}(X)\leq r, |  |

that is, X∈ErX\in E\_{r}. Hence, ErE\_{r} is 𝒫\mathcal{P}-sensitive with reduction set 𝒬\mathcal{Q}.
∎

Of course, a set is 𝒫\mathcal{P}-sensitive if and only if its indictor is 𝒫\mathcal{P}-sensitive as a function:

###### Lemma 2.13.

A set 𝒞⊆𝒳\mathcal{C}\subseteq\mathcal{X} is 𝒫\mathcal{P}-sensitive if and only if its convex analytic indicator function

|  |  |  |
| --- | --- | --- |
|  | δ​(X∣𝒞):={0,if ​X∈𝒞,∞,if ​X∉𝒞,​X∈𝒳,\delta(X\mid\mathcal{C}):=\begin{cases}0,&\text{if }X\in\mathcal{C},\\ \infty,&\text{if }X\not\in\mathcal{C},\end{cases}\qquad X\in\mathcal{X}, |  |

is 𝒫\mathcal{P}-sensitive.

The following proposition shows that 𝒫\mathcal{P}-sensitivity is automatically satisfied for a large class of lower semicontinuous quasi-convex functions under mild assumptions on the dual space.

###### Proposition 2.14.

Let 𝒳⊆Lc0\mathcal{X}\subseteq L^{0}\_{c} and 𝒴⊆cac\mathcal{Y}\subseteq\mathrm{ca}\_{c} be subspaces such that ⟨𝒳,𝒴⟩\langle\mathcal{X},\mathcal{Y}\rangle is a dual pair, and 𝒴\mathcal{Y} satisfies μ∈𝒴⇒|μ|∈𝒴\mu\in\mathcal{Y}\,\Rightarrow|\mu|\in\mathcal{Y}. Then each σ​(𝒳,𝒴)\sigma(\mathcal{X},\mathcal{Y})-lower semicontinuous quasi-convex function f:𝒳→[−∞,∞]f\colon\mathcal{X}\to[-\infty,\infty] is 𝒫\mathcal{P}-sensitive.

###### Proof.

If ff is quasi-convex and lower semicontinuous, then each level set ErE\_{r} is convex and σ​(𝒳,𝒴)\sigma(\mathcal{X},\mathcal{Y})-closed. According to [[22](https://arxiv.org/html/2601.19511v1#bib.bib34 "Bipolar theorems for sets of nonnegative random variables"), Theorem 5.13], ErE\_{r} is 𝒫\mathcal{P}-sensitive.
∎

Regarding sufficient properties to ensure that a set is 𝒫\mathcal{P}-sensitive, we refer to [[22](https://arxiv.org/html/2601.19511v1#bib.bib34 "Bipolar theorems for sets of nonnegative random variables")]. In the case of 𝒫\mathcal{P}-sensitive functions, sufficient conditions will be provided throughout the remainder of this paper. The question we address next is whether there are robust models (Ω,ℱ,𝒫)(\Omega,\mathcal{F},\mathcal{P}) such that all sets 𝒞⊆𝒳\mathcal{C}\subseteq\mathcal{X}, and thus all functions f:𝒳→[−∞,∞]f:\mathcal{X}\to[-\infty,\infty], are 𝒫\mathcal{P}-sensitive:

###### Theorem 2.15.

Suppose that {𝟏A∣A∈ℱ}⊆𝒳\{\mathbf{1}\_{A}\mid A\in\mathcal{F}\}\subseteq\mathcal{X}. All subsets of 𝒳\mathcal{X} are 𝒫\mathcal{P}-sensitive if and only if 𝒫\mathcal{P} is dominated, that is, there is Q∈𝔓​(Ω)Q\in\mathfrak{P}(\Omega) such that 𝒫≪Q\mathcal{P}\ll Q.

The condition {𝟏A∣A∈ℱ}⊆𝒳\{\mathbf{1}\_{A}\mid A\in\mathcal{F}\}\subseteq\mathcal{X} is in particular satisfied if Lc∞⊆𝒳L^{\infty}\_{c}\subseteq\mathcal{X}.
The proof of Theorem [2.15](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem15 "Theorem 2.15. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") needs some preparation. As already observed in [[22](https://arxiv.org/html/2601.19511v1#bib.bib34 "Bipolar theorems for sets of nonnegative random variables")], 𝒫\mathcal{P}-sensitivity is closely related to the problem of aggregation of families of (equivalence classes of) random variables as introduced in the following.

###### Definition 2.16.

Let 𝒬⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathfrak{P}\_{c}(\Omega) be non-empty.

1. 1.

   A family (XQ)Q∈𝒬⊆𝒳(X^{Q})\_{Q\in\mathcal{Q}}\subseteq\mathcal{X} is called 𝒬\mathcal{Q}-coherent (in 𝒳\mathcal{X}) if there exists X∈𝒳X\in\mathcal{X} such that jQ​(XQ)=jQ​(X)j\_{Q}(X^{Q})=j\_{Q}(X) for all Q∈𝒬Q\in\mathcal{Q}. In that case, XX is called a 𝒬\mathcal{Q}-aggregator (in 𝒳\mathcal{X}) of the family (XQ)Q∈𝒬(X^{Q})\_{Q\in\mathcal{Q}}.
2. 2.

   A set 𝒞⊆𝒳\mathcal{C}\subseteq\mathcal{X} is 𝒬\mathcal{Q}-stable (in 𝒳\mathcal{X}) if 𝒞\mathcal{C} contains all 𝒬\mathcal{Q}-aggregators (in 𝒳\mathcal{X}) of all 𝒬\mathcal{Q}-coherent families (XQ)Q∈𝒬⊆𝒞(X^{Q})\_{Q\in\mathcal{Q}}\subseteq\mathcal{C}.
3. 3.

   Let (XQ)Q∈𝒬(X^{Q})\_{Q\in\mathcal{Q}} be 𝒬\mathcal{Q}-coherent in 𝒳\mathcal{X}. A 𝒬\mathcal{Q}-aggregator XX of (XQ)Q∈𝒬(X^{Q})\_{Q\in\mathcal{Q}} in 𝒳\mathcal{X} is called trivial if there exists Q∈𝒬Q\in\mathcal{Q} such that X=XQX=X^{Q}. XX is called non-trivial if X≠XQX\neq X^{Q} for all Q∈𝒬Q\in\mathcal{Q} (i.e., for all Q∈𝒬Q\in\mathcal{Q} there exists P∈𝒫P\in\mathcal{P} such that P​(X≠XQ)>0P(X\neq X^{Q})>0).

The following is easily verified, see [[22](https://arxiv.org/html/2601.19511v1#bib.bib34 "Bipolar theorems for sets of nonnegative random variables"), Proposition 5.8] for a proof in case 𝒳=Lc0\mathcal{X}=L^{0}\_{c}.

###### Lemma 2.17.

A set 𝒞⊆𝒳\mathcal{C}\subseteq\mathcal{X} is 𝒫\mathcal{P}-sensitive with reduction set 𝒬\mathcal{Q} if any only if 𝒞\mathcal{C} is 𝒬\mathcal{Q}-stable.

In particular, 𝒞\mathcal{C} is 𝒫\mathcal{P}-sensitive if and only if 𝒞\mathcal{C} is 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-stable.

###### Lemma 2.18.

Every set 𝒞⊆𝒳\mathcal{C}\subseteq\mathcal{X} is 𝒫\mathcal{P}-sensitive if and only if every 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-aggregator (of any 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-coherent family) is trivial.

###### Proof.

Suppose that every set 𝒞⊆𝒳\mathcal{C}\subseteq\mathcal{X} is 𝒫\mathcal{P}-sensitive, and let (XQ)Q∈𝒬⊆Lc0(X^{Q})\_{Q\in\mathcal{Q}}\subseteq L^{0}\_{c} be 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-coherent. By assumption, 𝒞:={XQ∣Q∈𝔓c​(Ω)}\mathcal{C}:=\{X^{Q}\mid Q\in\mathfrak{P}\_{c}(\Omega)\} is 𝒫\mathcal{P}-sensitive and thus 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-stable. Hence, any 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-aggregator X∈𝒳X\in\mathcal{X} of (XQ)Q∈𝒬(X^{Q})\_{Q\in\mathcal{Q}} must satisfy X∈𝒞X\in\mathcal{C}.

Conversely, suppose that every 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-aggregator is trivial. Consider an arbitrary non-empty set 𝒞⊆𝒳\mathcal{C}\subseteq\mathcal{X} and any 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-coherent family (XQ)Q∈𝒬⊆𝒞(X^{Q})\_{Q\in\mathcal{Q}}\subseteq\mathcal{C} with 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-aggregator X∈𝒳X\in\mathcal{X}. Then X∈𝒞X\in\mathcal{C}, because X=XQ∈𝒞X=X^{Q}\in\mathcal{C} for some Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega). Hence, 𝒞\mathcal{C} is 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-stable and thus 𝒫\mathcal{P}-sensitive.
∎

Lemma [2.18](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem18 "Lemma 2.18. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") can be further refined:

###### Lemma 2.19.

Suppose that {𝟏A∣A∈ℱ}⊆𝒳\{\mathbf{1}\_{A}\mid A\in\mathcal{F}\}\subseteq\mathcal{X}. All sets 𝒞⊆𝒳\mathcal{C}\subseteq\mathcal{X} are 𝒫\mathcal{P}-sensitive if and only if 11 is a trivial 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-aggregator of every family of indicators (𝟏AQ)Q∈𝔓c​(Ω)(\mathbf{1}\_{A^{Q}})\_{Q\in\mathfrak{P}\_{c}(\Omega)} such that Q​(AQ)=1Q(A^{Q})=1 for all Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega).

###### Proof.

First note that any family of indicators (𝟏AQ)Q∈𝔓c​(Ω)(\mathbf{1}\_{A^{Q}})\_{Q\in\mathfrak{P}\_{c}(\Omega)} such that Q​(AQ)=1Q(A^{Q})=1 for all Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega) is 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-coherent with 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-aggregator 11. Hence, if every set 𝒞⊆Lc0\mathcal{C}\subseteq L^{0}\_{c} is 𝒫\mathcal{P}-sensitive, then this aggregator must be trivial by Lemma [2.18](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem18 "Lemma 2.18. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").

Conversely, consider a non-empty set 𝒞⊆𝒳\mathcal{C}\subseteq\mathcal{X} and any 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-coherent family (XQ)Q∈𝔓c​(Ω)⊆𝒞(X^{Q})\_{Q\in\mathfrak{P}\_{c}(\Omega)}\subseteq\mathcal{C} with 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-aggregator X∈𝒳X\in\mathcal{X}. Let x∈Xx\in X and xQ∈XQx^{Q}\in X^{Q}, and set AQ:={xQ=x}A^{Q}:=\{x^{Q}=x\}, Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega). Then Q​(AQ)=1Q(A^{Q})=1 for all Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega). As 11 is a trivial 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-aggregator of (𝟏AQ)Q∈𝔓c​(Ω)(\mathbf{1}\_{A^{Q}})\_{Q\in\mathfrak{P}\_{c}(\Omega)}, there is Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega) such that 1=𝟏AQ1=\mathbf{1}\_{A^{Q}}. This implies that for all P∈𝒫P\in\mathcal{P} we have 1=P​(1=𝟏AQ)=P​(XQ=X)1=P(1=\mathbf{1}\_{A^{Q}})=P(X^{Q}=X). Hence, XQ=XX^{Q}=X, and thus X∈𝒞X\in\mathcal{C}. Therefore, 𝒞\mathcal{C} is 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-stable.
∎

###### Proof of Theorem [2.15](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem15 "Theorem 2.15. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").

Suppose that 𝒫≪Q\mathcal{P}\ll Q. For all P∈𝒫P\in\mathcal{P}, denote by d​P/d​Q∈ℒ1​(Ω,ℱ,Q)dP/dQ\in\mathcal{L}^{1}(\Omega,\mathcal{F},Q) a version of the Radon-Nikodym density of PP with respect to QQ. Let zz be a version of

|  |  |  |
| --- | --- | --- |
|  | esssup⁡{χ{d​Pd​Q>0}|P∈𝒫}∈L0​(Ω,ℱ,Q).\operatorname{esssup}\bigg\{\chi\_{\{\frac{dP}{dQ}>0\}}\biggm|P\in\mathcal{P}\bigg\}\in L^{0}(\Omega,\mathcal{F},Q). |  |

Then A:={z>0}∈ℱA:=\{z>0\}\in\mathcal{F}, and one verifies that the conditional probability measure Q~:=Q(⋅∣A)\widetilde{Q}:=Q(\,\cdot\mid A) satisfies Q~≈𝒫\widetilde{Q}\approx\mathcal{P}. In particular, Q~∈𝔓c​(Ω)\widetilde{Q}\in\mathfrak{P}\_{c}(\Omega) and indeed Lc0=L0​(Ω,ℱ,Q~)L^{0}\_{c}=L^{0}(\Omega,\mathcal{F},\widetilde{Q}). Any set 𝒞⊆𝒳⊆Lc0\mathcal{C}\subseteq\mathcal{X}\subseteq L^{0}\_{c} is thus 𝒫\mathcal{P}-sensitive with reduction set {Q~}\{\widetilde{Q}\}.

Conversely, assume that all sets 𝒞⊆𝒳\mathcal{C}\subseteq\mathcal{X} are 𝒫\mathcal{P}-sensitive. Then, by Lemma [2.19](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem19 "Lemma 2.19. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), there exists R∈𝔓c​(Ω)R\in\mathfrak{P}\_{c}(\Omega) such that 𝟏A=1\mathbf{1}\_{A}=1 for all A∈ℱA\in\mathcal{F} with R​(A)=1R(A)=1. Indeed, otherwise for all R~∈𝔓c​(Ω)\widetilde{R}\in\mathfrak{P}\_{c}(\Omega) there would exist A∈ℱA\in\mathcal{F} with R~​(A)=1\widetilde{R}(A)=1 such that 𝟏A≠1\mathbf{1}\_{A}\neq 1. Then 11 is a non-trivial 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-aggregator, contradicting Lemma [2.19](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem19 "Lemma 2.19. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"). We claim that 𝒫≪R\mathcal{P}\ll R. To this end, suppose that N∈ℱN\in\mathcal{F} satisfies R​(N)=0R(N)=0. Then R​(Ω∖N)=1R(\Omega\setminus N)=1 and therefore 𝟏Ω∖N=1\mathbf{1}\_{\Omega\setminus N}=1, that is, 1=P​(𝟏Ω∖N=1)=P​(Ω∖N)1=P(\mathbf{1}\_{\Omega\setminus N}=1)=P(\Omega\setminus N) for all P∈𝒫P\in\mathcal{P}. Consequently, P​(N)=0P(N)=0 for all P∈𝒫P\in\mathcal{P}.
∎

###### Example 2.20.

Let (Ω,ℱ)=([0,1],ℬ​([0,1]))(\Omega,\mathcal{F})=([0,1],\mathcal{B}([0,1])), where ℬ​([0,1])\mathcal{B}([0,1]) denotes the Borel-σ\sigma-algebra over [0,1][0,1]. Further, let 𝒫:={δω∣ω∈[0,1]}\mathcal{P}:=\{\delta\_{\omega}\mid\omega\in[0,1]\} be the set of all Dirac measures. Note that in this case ≼\preccurlyeq coincides with the pointwise order and that Lc0=ℒ0​(Ω,ℱ)L^{0}\_{c}=\mathcal{L}^{0}(\Omega,\mathcal{F}) is simply the space of all random variables. Moreover, c​ac=c​aca\_{c}=ca and, in particular, 𝔓c​(Ω)=𝔓​(Ω)\mathfrak{P}\_{c}(\Omega)=\mathfrak{P}(\Omega). For any Q∈𝔓​(Ω)Q\in\mathfrak{P}(\Omega) denote by A​(Q):={ω∈Ω∣Q​({ω})>0}A(Q):=\{\omega\in\Omega\mid Q(\{\omega\})>0\} the set of QQ-atoms, and recall that the set A​(Q)A(Q) is at most countable. Therefore, Ω∖A​(Q)≠∅\Omega\setminus A(Q)\neq\emptyset. Since any probability measure QQ dominating 𝒫\mathcal{P} would have to satisfy Q​({ω})>0Q(\{\omega\})>0 for all ω∈Ω\omega\in\Omega, that is, A​(Q)=ΩA(Q)=\Omega, which is not possible, 𝒫\mathcal{P} is not dominated.

Moreover, for instance, by removing an arbitrary ω∈Ω∖A​(Q)\omega\in\Omega\setminus A(Q) from Ω\Omega, it follows that, for any Q∈𝔓​(Ω)Q\in\mathfrak{P}(\Omega), we may choose BQ∈ℱB^{Q}\in\mathcal{F} such that Q​(BQ)=1Q(B^{Q})=1 but BQ≠ΩB^{Q}\neq\Omega, and thus 1≠𝟏BQ1\neq\mathbf{1}\_{B^{Q}}. The family (𝟏BQ)Q∈𝔓​(Ω)(\mathbf{1}\_{B^{Q}})\_{Q\in\mathfrak{P}(\Omega)} is 𝔓​(Ω)\mathfrak{P}(\Omega)-coherent with non-trivial 𝔓​(Ω)\mathfrak{P}(\Omega)-aggregator 11 in any 𝒳⊆Lc0\mathcal{X}\subseteq L^{0}\_{c} such that {𝟏A∣A∈ℱ}⊆𝒳\{\mathbf{1}\_{A}\mid A\in\mathcal{F}\}\subseteq\mathcal{X}. The set

|  |  |  |
| --- | --- | --- |
|  | 𝒞:={𝟏BQ∣Q∈𝔓​(Ω)}\mathcal{C}:=\{\mathbf{1}\_{B^{Q}}\mid Q\in\mathfrak{P}(\Omega)\} |  |

is not 𝒫\mathcal{P}-sensitive in any 𝒳⊆Lc0\mathcal{X}\subseteq L^{0}\_{c} such that {𝟏A∣A∈ℱ}⊆𝒳\{\mathbf{1}\_{A}\mid A\in\mathcal{F}\}\subseteq\mathcal{X}, because it is not 𝔓​(Ω)\mathfrak{P}(\Omega)-stable. This can also be directly verified without invoking aggregation and stability, since for all Q∈𝔓​(Ω)Q\in\mathfrak{P}(\Omega), we have jQ​(1)=jQ​(𝟏BQ)∈jQ​(𝒞)j\_{Q}(1)=j\_{Q}(\mathbf{1}\_{B^{Q}})\in j\_{Q}(\mathcal{C}). However, 1∉𝒞1\notin\mathcal{C}, since 1≠𝟏BQ1\neq\mathbf{1}\_{B^{Q}} for all Q∈𝔓​(Ω)Q\in\mathfrak{P}(\Omega). ⋄\diamond

###### Remark 2.21.

Whether a set is 𝒫\mathcal{P}-sensitive not only depends on (Ω,ℱ,𝒫)(\Omega,\mathcal{F},\mathcal{P}) but also on the domain 𝒳\mathcal{X}. Clearly, if 𝒞⊆𝒳⊆𝒳~\mathcal{C}\subseteq\mathcal{X}\subseteq\widetilde{\mathcal{X}} is 𝒫\mathcal{P}-sensitive in 𝒳~\widetilde{\mathcal{X}}, then 𝒞\mathcal{C} is 𝒫\mathcal{P}-sensitive in 𝒳\mathcal{X}. Indeed, in 𝒳\mathcal{X} there are less 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-coherent families or 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-aggregators. ⋄\diamond

## 3 𝓟\boldsymbol{\mathcal{P}}-Sensitivity and Functional Localization

As before, let 𝒳⊆Lc0\mathcal{X}\subseteq L^{0}\_{c} be non-empty and let f:𝒳→[−∞,∞]f\colon\mathcal{X}\to[-\infty,\infty].

###### Definition 3.1.

Let fQ:𝒳→[−∞,∞]f^{Q}:\mathcal{X}\to[-\infty,\infty], Q∈𝒬Q\in\mathcal{Q}, be a 𝒬\mathcal{Q}-consistent family of functions, where 𝒬⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathfrak{P}\_{c}(\Omega) is non-empty. If

|  |  |  |
| --- | --- | --- |
|  | f​(X)=supQ∈𝒬fQ​(X),X∈𝒳,f(X)=\sup\_{Q\in\mathcal{Q}}f^{Q}(X),\qquad X\in\mathcal{X}, |  |

then (fQ)Q∈𝒬(f^{Q})\_{Q\in\mathcal{Q}} is called a (functional) 𝒬\mathcal{Q}-localization of ff.

Note that the aggregator of the functions fQf^{Q} in the definition of a 𝒬\mathcal{Q}-localization is the supremum, which may be seen as a worst-case approach when the fQf^{Q} represent some type of local risk assessment under the model Q∈𝒬Q\in\mathcal{Q}.

By Lemma [2.12](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem12 "Lemma 2.12. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), if ff admits a 𝒬\mathcal{Q}-localization, then ff is necessarily 𝒫\mathcal{P}-sensitive. We will show that the converse is also true. To this end, we consider a particular family of local functions which will turn out to be a localization of ff whenever ff is 𝒫\mathcal{P}-sensitive. For Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega), let fEQ:𝒳→ℝf^{Q}\_{E}\colon\mathcal{X}\to\mathbb{R} be given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | fEQ​(X):=inf{r∈ℝ∣jQ​(X)∈jQ​(Er)}​(inf∅:=∞),\displaystyle\begin{split}f^{Q}\_{E}(X)&:=\inf\{r\in\mathbb{R}\mid j\_{Q}(X)\in j\_{Q}(E\_{r})\}\qquad(\inf\emptyset:=\infty),\end{split} | |  |

where, as before, Er:={X∈𝒳∣f​(X)≤r}E\_{r}:=\{X\in\mathcal{X}\mid f(X)\leq r\}, r∈ℝr\in\mathbb{R}, denote the level sets of ff. Moreover, for non-empty 𝒬⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathfrak{P}\_{c}(\Omega), we define

|  |  |  |
| --- | --- | --- |
|  | fE𝒬​(X):=supQ∈𝒬fEQ​(X),X∈𝒳,f^{\mathcal{Q}}\_{E}(X):=\sup\_{Q\in\mathcal{Q}}f^{Q}\_{E}(X),\qquad X\in\mathcal{X}, |  |

and fE:=fE𝔓c​(Ω)f\_{E}:=f^{\mathfrak{P}\_{c}(\Omega)}\_{E}.

###### Theorem 3.2.

There exists a 𝒬\mathcal{Q}-localization of ff if and only if ff is 𝒫\mathcal{P}-sensitive with reduction set 𝒬\mathcal{Q}. In that case f=fE𝒬=fE𝒬′f=f^{\mathcal{Q}}\_{E}=f^{\mathcal{Q}^{\prime}}\_{E} for every 𝒬′\mathcal{Q}^{\prime} satisfying 𝒬⊆𝒬′⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathcal{Q}^{\prime}\subseteq\mathfrak{P}\_{c}(\Omega), i.e., (fEQ)Q∈𝒬′(f^{Q}\_{E})\_{Q\in\mathcal{Q}^{\prime}} is a 𝒬′\mathcal{Q}^{\prime}-localization of ff.

In particular, f=fEf=f\_{E} if and only if ff is 𝒫\mathcal{P}-sensitive, because 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega) is a reduction set for every 𝒫\mathcal{P}-sensitive function.
The proof of Theorem [3.2](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") is postponed to after the following lemma, the proof of which is straightforward and left to the reader.

###### Lemma 3.3.

Let f:𝒳→[−∞,∞]f:\mathcal{X}\to[-\infty,\infty] and denote by ErE\_{r}, r∈ℝr\in\mathbb{R}, the level sets of ff. Moreover, let Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega).

1. (i)

   fEQf^{Q}\_{E} is QQ-consistent.
2. (ii)

   fEQ≤ff^{Q}\_{E}\leq f.
3. (iii)

   fEQ​(X)=inf{f​(Y)∣Y∈𝒳:jQ​(X)=jQ​(Y)}f^{Q}\_{E}(X)=\inf\{f(Y)\mid Y\in\mathcal{X}\colon j\_{Q}(X)=j\_{Q}(Y)\}, X∈𝒳X\in\mathcal{X}.
4. (iv)

   If fQ:𝒳→[−∞,∞]f^{Q}:\mathcal{X}\to[-\infty,\infty] is QQ-consistent such that fQ≤ff^{Q}\leq f, then fQ≤fEQf^{Q}\leq f^{Q}\_{E}.
5. (v)

   Let 𝒬⊆𝒬′⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathcal{Q}^{\prime}\subseteq\mathfrak{P}\_{c}(\Omega), then fE𝒬≤fE𝒬′f^{\mathcal{Q}}\_{E}\leq f^{\mathcal{Q}^{\prime}}\_{E}. In particular, fE𝒬≤fE≤ff^{\mathcal{Q}}\_{E}\leq f\_{E}\leq f.

###### Proof of Theorem [3.2](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").

If ff admits a 𝒬\mathcal{Q}-localization, then ff is 𝒫\mathcal{P}-sensitive with reduction set 𝒬\mathcal{Q} by Lemma [2.12](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem12 "Lemma 2.12. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").

Conversely, let ff be 𝒫\mathcal{P}-sensitive with reduction set 𝒬\mathcal{Q}. We show that f=fE𝒬f=f^{\mathcal{Q}}\_{E}. In view of Lemma [3.3](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), this is equivalent to f≤fE𝒬f\leq f^{\mathcal{Q}}\_{E} since always f≥fE𝒬f\geq f^{\mathcal{Q}}\_{E}. Consider X∈𝒳X\in\mathcal{X} such that fE𝒬​(X)<∞f^{\mathcal{Q}}\_{E}(X)<\infty and let r∈ℝr\in\mathbb{R} such that fE𝒬​(X)<rf^{\mathcal{Q}}\_{E}(X)<r. Then, for all Q∈𝒬Q\in\mathcal{Q}, fEQ​(X)≤fE𝒬​(X)<rf^{Q}\_{E}(X)\leq f^{\mathcal{Q}}\_{E}(X)<r and thus jQ​(X)∈jQ​(Er)j\_{Q}(X)\in j\_{Q}(E\_{r}). As 𝒬\mathcal{Q} is a reduction set for ErE\_{r}, we obtain that X∈ErX\in E\_{r} and thus, f​(X)≤rf(X)\leq r. It follows that

|  |  |  |
| --- | --- | --- |
|  | fE𝒬​(X)=inf{r∈ℝ∣fE𝒬​(X)<r}≥inf{r∈ℝ∣f​(X)≤r}=f​(X).f^{\mathcal{Q}}\_{E}(X)=\inf\{r\in\mathbb{R}\mid f^{\mathcal{Q}}\_{E}(X)<r\}\geq\inf\{r\in\mathbb{R}\mid f(X)\leq r\}=f(X). |  |

Finally, recall that if 𝒬\mathcal{Q} is a reduction set for ff, then so is any 𝒬′\mathcal{Q}^{\prime} with 𝒬⊆𝒬′⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathcal{Q}^{\prime}\subseteq\mathfrak{P}\_{c}(\Omega) (see Lemma [2.8](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem8 "Lemma 2.8. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")).
∎

###### Remark 3.4.

Let 𝒬⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathfrak{P}\_{c}(\Omega) be non-empty. Theorem [3.2](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") implies that a function f:𝒳→[−∞,∞]f\colon\mathcal{X}\to[-\infty,\infty] admits a representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(X)=infQ∈𝒬fQ​(X),X∈𝒳,f(X)=\inf\_{Q\in\mathcal{Q}}f^{Q}(X),\qquad X\in\mathcal{X}, |  | (5) |

where (fQ)Q∈𝒬(f^{Q})\_{Q\in\mathcal{Q}} is a 𝒬\mathcal{Q}-consistent family of functions, if and only if ff is upper 𝒫\mathcal{P}-sensitive and 𝒬\mathcal{Q} is a joint reduction set for every upper level set of ff. Moreover, ([5](https://arxiv.org/html/2601.19511v1#S3.E5 "In Remark 3.4. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) corresponds to a worst-case approach when the fQf^{Q} represent a local utility assessment under the model Q∈𝒬Q\in\mathcal{Q}. ⋄\diamond

### 3.1 Properties of 𝓟\boldsymbol{\mathcal{P}}-Sensitive Functions

In this section, we analyze the relationship between properties of ff and its localizations. We now assume that 𝒳\mathcal{X} is a linear space containing the constants. We will consider the following properties known, e.g., from the study of risk measures:

1. (i)

   Monotonicity: For all X1,X2∈𝒳X\_{1},X\_{2}\in\mathcal{X} such that X1≼X2X\_{1}\preccurlyeq X\_{2}, we have f​(X1)≤f​(X2)f(X\_{1})\leq f(X\_{2}).
2. (ii)

   Cash-additivity: For all X∈𝒳X\in\mathcal{X} and m∈ℝm\in\mathbb{R}, we have f​(X+m)=f​(X)+mf(X+m)=f(X)+m.
3. (iii)

   Quasi-convexity: For all X1,X2∈𝒳X\_{1},X\_{2}\in\mathcal{X} and λ∈[0,1]\lambda\in[0,1], we have f​(λ​X1+(1−λ)​X2)≤max⁡{f​(X1),f​(X2)}f(\lambda X\_{1}+(1-\lambda)X\_{2})\leq\max\{f(X\_{1}),f(X\_{2})\}.
4. (iv)

   Convexity: For all X1,X2∈𝒳X\_{1},X\_{2}\in\mathcal{X} and λ∈[0,1]\lambda\in[0,1], we have f​(λ​X1+(1−λ)​X2)≤λ​f​(X1)+(1−λ)​f​(X2)f(\lambda X\_{1}+(1-\lambda)X\_{2})\leq\lambda f(X\_{1})+(1~-~\lambda)f(X\_{2}).
5. (v)

   Positive homogeneity: For all X∈𝒳X\in\mathcal{X} and λ≥0\lambda\geq 0, we have f​(λ​X)=λ​f​(X)f(\lambda X)=\lambda f(X).
6. (vi)

   Subadditivity: For all X1,X2∈𝒳X\_{1},X\_{2}\in\mathcal{X}, we have f​(X1+X2)≤f​(X1)+f​(X2)f(X\_{1}+X\_{2})\leq f(X\_{1})+f(X\_{2}).

###### Lemma 3.5.

Consider a 𝒬\mathcal{Q}-localization (fQ)Q∈𝒬(f^{Q})\_{Q\in\mathcal{Q}} of ff.

1. (i)

   ff is monotone whenever each fQf^{Q}, Q∈𝒬Q\in\mathcal{Q}, is monotone.
2. (ii)

   ff is cash-additive whenever each fQf^{Q}, Q∈𝒬Q\in\mathcal{Q}, is cash-additive.
3. (iii)

   ff is (quasi-)convex whenever each fQf^{Q}, Q∈𝒬Q\in\mathcal{Q}, is (quasi-)convex.
4. (iv)

   ff is positively homogeneous whenever each fQf^{Q}, Q∈𝒬Q\in\mathcal{Q}, is positively homogeneous.
5. (v)

   ff is subadditive whenever each fQf^{Q}, Q∈𝒬Q\in\mathcal{Q}, is subadditive.

###### Proof.

Recall that f​(X)=supQ∈𝒬fQ​(X)f(X)=\sup\_{Q\in\mathcal{Q}}f^{Q}(X). Then the assertions follow.
∎

###### Lemma 3.6.

Let Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega).

1. (i)

   If ff is monotone, then fEQf^{Q}\_{E} is monotone. Moreover, jQ​(X1)≤QjQ​(X2)j\_{Q}(X\_{1})\leq\_{Q}j\_{Q}(X\_{2}) implies fEQ​(X1)≤fEQ​(X2)f^{Q}\_{E}(X\_{1})\leq f^{Q}\_{E}(X\_{2}).
2. (ii)

   If ff is cash-additive, then fEQf^{Q}\_{E} is cash-additive.
3. (iii)

   If ff is (quasi-)convex, then fEQf^{Q}\_{E} is (quasi-)convex.
4. (iv)

   If ff is positively homogeneous, then fEQf^{Q}\_{E} satisfies fEQ​(λ​X)=λ​fEQ​(X)f^{Q}\_{E}(\lambda X)=\lambda f^{Q}\_{E}(X) for all X∈𝒳X\in\mathcal{X} and λ>0\lambda>0. Moreover, either fEQ​(0)=−∞f^{Q}\_{E}(0)=-\infty or fEQf^{Q}\_{E} is positively homogeneous.
5. (v)

   If ff is subadditive, then fEQf^{Q}\_{E} is subadditive.

###### Proof.

(i) Let X1,X2∈𝒳X\_{1},X\_{2}\in\mathcal{X} such that X1≼X2X\_{1}\preccurlyeq X\_{2}. Then jQ​(X1)≤QjQ​(X2)j\_{Q}(X\_{1})\leq\_{Q}j\_{Q}(X\_{2}). Hence, it suffices to show the second assertion. To this end, suppose that jQ​(X1)≤QjQ​(X2)j\_{Q}(X\_{1})\leq\_{Q}j\_{Q}(X\_{2}). If fEQ​(X2)=∞f^{Q}\_{E}(X\_{2})=\infty, there is nothing to show. Let r∈ℝr\in\mathbb{R} such that fEQ​(X2)<rf^{Q}\_{E}(X\_{2})<r. There is X~2∈𝒳\widetilde{X}\_{2}\in\mathcal{X} such that f​(X~2)≤rf(\widetilde{X}\_{2})\leq r and jQ​(X~2)=jQ​(X2)j\_{Q}(\widetilde{X}\_{2})=j\_{Q}(X\_{2}). Set A:={ω∈Ω∣g1​(ω)≤g2​(ω)}A:=\{\omega\in\Omega\mid g\_{1}(\omega)\leq g\_{2}(\omega)\} where g1∈X1g\_{1}\in X\_{1} and g2∈X~2g\_{2}\in\widetilde{X}\_{2}. Then Q​(A)=1Q(A)=1 and

|  |  |  |
| --- | --- | --- |
|  | 𝟏A​X1+𝟏Ac​X~2≼X~2.\mathbf{1}\_{A}X\_{1}+\mathbf{1}\_{A^{c}}\widetilde{X}\_{2}\preccurlyeq\widetilde{X}\_{2}. |  |

Since ff is monotone, f​(𝟏A​X1+𝟏Ac​X~2)≤f​(X~2)≤rf(\mathbf{1}\_{A}X\_{1}+\mathbf{1}\_{A^{c}}\widetilde{X}\_{2})\leq f(\widetilde{X}\_{2})\leq r. As jQ​(X1)=jQ​(𝟏A​X1+𝟏Ac​X~2)j\_{Q}(X\_{1})=j\_{Q}(\mathbf{1}\_{A}X\_{1}+\mathbf{1}\_{A^{c}}\widetilde{X}\_{2}), we conclude by Lemma [3.3](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") that fEQ​(X1)≤f​(𝟏A​X1+𝟏Ac​X~2)≤rf\_{E}^{Q}(X\_{1})\leq f(\mathbf{1}\_{A}X\_{1}+\mathbf{1}\_{A^{c}}\widetilde{X}\_{2})\leq r. Since r>fEQ​(X2)r>f^{Q}\_{E}(X\_{2}) was arbitrary, it follows that fEQ​(X1)≤fEQ​(X2)f^{Q}\_{E}(X\_{1})\leq f^{Q}\_{E}(X\_{2}).

(ii), (iii), and (v) follow from Lemma [3.3](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") (iii) and linearity of jQj\_{Q}.

(iv) In case λ>0\lambda>0 and X∈𝒳X\in\mathcal{X}, Lemma [3.3](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") (iii) yields the assertion. Since f​(0)=0f(0)=0, we have that fEQ​(0)≤0f^{Q}\_{E}(0)\leq 0. Suppose that fEQ​(0)<0f^{Q}\_{E}(0)<0. Then there must be X≠0X\neq 0 and r<0r<0 such that f​(X)≤rf(X)\leq r and jQ​(X)=0j\_{Q}(X)=0. But then also jQ​(λ​X)=0j\_{Q}(\lambda X)=0 for all λ>0\lambda>0. Thus, fEQ​(0)≤f​(λ​X)=λ​f​(X)=−∞f^{Q}\_{E}(0)\leq f(\lambda X)=\lambda f(X)=-\infty.
∎

### 3.2 Robust Dual Representation and 𝓟\boldsymbol{\mathcal{P}}-Sensitivity

In this section, we will show that a function f:𝒳→[−∞,∞]f:\mathcal{X}\to[-\infty,\infty] admits a dual representation over c​acca\_{c} only if it is 𝒫\mathcal{P}-sensitive. Moreover, in that case we obtain another functional localization of ff via a dual approach. In contrast, the localization defined by the functions fEQf^{Q}\_{E}, which are based on the level sets, can be viewed as a primal approach to represent ff.

Throughout this section, we assume that 𝒳⊆Lc0\mathcal{X}\subseteq L^{0}\_{c} is a linear space containing the constants. Let

|  |  |  |
| --- | --- | --- |
|  | c​ac​(𝒳):={μ∈c​ac|∫X​𝑑μ​ is well-defined and finite for all ​X∈𝒳}.ca\_{c}(\mathcal{X}):=\bigg\{\mu\in ca\_{c}\biggm|\int Xd\mu\text{ is well-defined and finite for all }X\in\mathcal{X}\bigg\}. |  |

Note that always 0∈c​ac​(𝒳)0\in ca\_{c}(\mathcal{X}). A function f:𝒳→[−∞,∞]f\colon\mathcal{X}\to[-\infty,\infty] is said to admit a dual representation over c​ac​(𝒳)ca\_{c}(\mathcal{X}) if

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(X)=supμ∈c​ac​(𝒳)∫X​𝑑μ−f∗​(μ),X∈𝒳,f(X)=\sup\_{\mu\in ca\_{c}(\mathcal{X})}\int Xd\mu-f^{\*}(\mu),\qquad X\in\mathcal{X}, |  | (6) |

where f∗:c​ac​(𝒳)→[−∞,∞]f^{\*}\colon ca\_{c}(\mathcal{X})\to[-\infty,\infty]. Note that f∗​(μ)=∞f^{\ast}(\mu)=\infty, means that μ\mu is effectively not considered in ([6](https://arxiv.org/html/2601.19511v1#S3.E6 "In 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")). Also, f∗f^{\ast} in ([6](https://arxiv.org/html/2601.19511v1#S3.E6 "In 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) is not necessarily unique, meaning that ff may admit a representation of the form ([6](https://arxiv.org/html/2601.19511v1#S3.E6 "In 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) for different f∗f^{\ast}. In order to deal with the latter issue, we consider, as usual, the minimal f∗f^{\ast} for which ff admits a representation ([6](https://arxiv.org/html/2601.19511v1#S3.E6 "In 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")). This so-called dual function f¯:c​ac​(𝒳)→[−∞,∞]\overline{f}:ca\_{c}(\mathcal{X})\to[-\infty,\infty] is given by

|  |  |  |
| --- | --- | --- |
|  | f¯​(μ):=supX∈𝒳∫X​𝑑μ−f​(X),μ∈c​ac​(𝒳).\overline{f}(\mu):=\sup\_{X\in\mathcal{X}}\int Xd\mu-f(X),\qquad\mu\in ca\_{c}(\mathcal{X}). |  |

Note that f¯\overline{f} is indeed defined for every function f:𝒳→[−∞,∞]f:\mathcal{X}\to[-\infty,\infty], including those that do not admit a dual representation. If ff takes the value −∞-\infty, then f¯≡∞\overline{f}\equiv\infty. The dual regularization fDf\_{D} of ff is given by

|  |  |  |
| --- | --- | --- |
|  | fD​(X):=supμ∈c​ac​(𝒳)∫X​𝑑μ−f¯​(μ),X∈𝒳.f\_{D}(X):=\sup\_{\mu\in ca\_{c}(\mathcal{X})}\int Xd\mu-\overline{f}(\mu),\qquad X\in\mathcal{X}. |  |

Clearly, fDf\_{D} is convex and fD≤ff\_{D}\leq f. It is well-known that a function ff admits a dual representation of the form ([6](https://arxiv.org/html/2601.19511v1#S3.E6 "In 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) if and only if f=fDf=f\_{D}. Indeed, suppose that ff admits a dual representation ([6](https://arxiv.org/html/2601.19511v1#S3.E6 "In 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")), then by definition of f¯\overline{f}, we have f∗≥f¯f^{\ast}\geq\overline{f}. Thus,

|  |  |  |
| --- | --- | --- |
|  | f​(X)=supμ∈c​ac​(𝒳)∫X​𝑑μ−f∗​(μ)≤supμ∈c​ac​(𝒳)∫X​𝑑μ−f¯​(μ)=fD​(X)≤f​(X).f(X)=\sup\_{\mu\in ca\_{c}(\mathcal{X})}\int Xd\mu-f^{\*}(\mu)\leq\sup\_{\mu\in ca\_{c}(\mathcal{X})}\int Xd\mu-\overline{f}(\mu)=f\_{D}(X)\leq f(X). |  |

###### Remark 3.7.

Recall that the Fenchel-Moreau Theorem (see, e.g., [[15](https://arxiv.org/html/2601.19511v1#bib.bib25 "Convex analysis and variational problems"), Part One, Proposition 3.1]) provides necessary and sufficient conditions on ff guaranteeing that ff admits a dual representation. Indeed, suppose 𝒳\mathcal{X} carries a locally convex topology τ\tau such that the dual space (𝒳,τ)∗(\mathcal{X},\tau)^{\ast} may be identified with a subset of c​ac​(𝒳)ca\_{c}(\mathcal{X}) via the usual representation of continuous linear functionals as integrals over elements of c​ac​(𝒳)ca\_{c}(\mathcal{X}). Then, according to the Fenchel-Moreau Theorem, f=fDf=f\_{D} is equivalent to ff being convex, lower semicontinuous with respect to τ\tau, and satisfying that ff takes the value −∞-\infty if and only if f≡−∞f\equiv-\infty. ⋄\diamond

For Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega), the QQ-dual regularization of ff is given by

|  |  |  |
| --- | --- | --- |
|  | fDQ​(X):=supμ∈c​aQ​(𝒳)∫X​𝑑μ−f¯Q​(μ),X∈𝒳,f^{Q}\_{D}(X):=\sup\_{\mu\in ca\_{Q}(\mathcal{X})}\int Xd\mu-\overline{f}^{Q}(\mu),\qquad X\in\mathcal{X}, |  |

where c​aQ​(𝒳):=c​aQ∩c​ac​(𝒳)ca\_{Q}(\mathcal{X}):=ca\_{Q}\cap ca\_{c}(\mathcal{X}) and

|  |  |  |
| --- | --- | --- |
|  | f¯Q​(μ):=supX∈𝒳∫X​𝑑μ−fEQ​(X),μ∈c​aQ​(𝒳).\overline{f}^{Q}(\mu):=\sup\_{X\in\mathcal{X}}\int Xd\mu-f^{Q}\_{E}(X),\qquad\mu\in ca\_{Q}(\mathcal{X}). |  |

fDQf^{Q}\_{D} corresponds to a QQ-local dual view on ff. For non-empty 𝒬⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathfrak{P}\_{c}(\Omega), we set fD𝒬:=supQ∈𝒬fDQf^{\mathcal{Q}}\_{D}:=\sup\_{Q\in\mathcal{Q}}f^{Q}\_{D}. Clearly, fD=fD𝔓c​(Ω)f\_{D}=f^{\mathfrak{P}\_{c}(\Omega)}\_{D}.

###### Lemma 3.8.

Let Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega).

1. (i)

   fDQf^{Q}\_{D} is QQ-consistent.
2. (ii)

   fDQ≤fEQf^{Q}\_{D}\leq f^{Q}\_{E}.
3. (iii)

   Consider any QQ-consistent function fQ:𝒳→[−∞,∞]f^{Q}\colon\mathcal{X}\to[-\infty,\infty] which satisfies fQ≤ff^{Q}\leq f and admits a dual representation over c​aQ​(𝒳)ca\_{Q}(\mathcal{X}), that is,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | fQ​(X)=supμ∈c​aQ​(𝒳)∫X​𝑑μ−(fQ)∗​(μ),X∈𝒳,f^{Q}(X)=\sup\_{\mu\in ca\_{Q}(\mathcal{X})}\int Xd\mu-(f^{Q})^{\*}(\mu),\qquad X\in\mathcal{X}, |  | (7) |

   where (fQ)∗:c​aQ​(𝒳)→[−∞,∞](f^{Q})^{\*}\colon ca\_{Q}(\mathcal{X})\to[-\infty,\infty]. Then f¯Q≤(fQ)∗\overline{f}^{Q}\leq(f^{Q})^{\*} and fQ≤fDQf^{Q}\leq f^{Q}\_{D}.
4. (iv)

   f¯Q​(μ)=f¯​(μ)\overline{f}^{Q}(\mu)=\overline{f}(\mu) for all μ∈c​aQ​(𝒳)\mu\in ca\_{Q}(\mathcal{X}) and hence,

   |  |  |  |
   | --- | --- | --- |
   |  | fDQ​(X)=supμ∈c​aQ​(𝒳)∫X​𝑑μ−f¯​(μ),X∈𝒳.f^{Q}\_{D}(X)=\sup\_{\mu\in ca\_{Q}(\mathcal{X})}\int Xd\mu-\overline{f}(\mu),\qquad X\in\mathcal{X}. |  |
5. (v)

   fDQ≤fD≤ff^{Q}\_{D}\leq f\_{D}\leq f.
6. (vi)

   fDQ=fEQf^{Q}\_{D}=f^{Q}\_{E} if and only if fEQf^{Q}\_{E} admits a dual representation over c​aQ​(𝒳)ca\_{Q}(\mathcal{X}).

###### Proof.

(i) and (ii) are obvious.

(iii) By Lemma [3.3](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), fQ≤fEQf^{Q}\leq f^{Q}\_{E}. Hence, for each μ∈c​aQ​(𝒳)\mu\in ca\_{Q}(\mathcal{X}), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | f¯Q​(μ)\displaystyle\overline{f}^{Q}(\mu) | =supX∈𝒳∫X​𝑑μ−fEQ​(X)≤supX∈𝒳∫X​𝑑μ−fQ​(X)\displaystyle=\sup\_{X\in\mathcal{X}}\int Xd\mu-f^{Q}\_{E}(X)\qquad\leq\qquad\sup\_{X\in\mathcal{X}}\int Xd\mu-f^{Q}(X) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =supX∈𝒳∫X​𝑑μ−supν∈c​aQ​(𝒳)(∫X​𝑑ν−(fQ)∗​(ν))≤(fQ)∗​(μ).\displaystyle=\sup\_{X\in\mathcal{X}}\int Xd\mu-\sup\_{\nu\in ca\_{Q}(\mathcal{X})}\bigg(\int Xd\nu-(f^{Q})^{\*}(\nu)\bigg)\qquad\leq\qquad(f^{Q})^{\*}(\mu). |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | ∫X​𝑑μ−(fQ)∗​(μ)≤∫X​𝑑μ−f¯Q​(μ)≤fDQ​(X).\int Xd\mu-(f^{Q})^{\ast}(\mu)\leq\int Xd\mu-\overline{f}^{Q}(\mu)\leq f\_{D}^{Q}(X). |  |

Taking the supremum over all μ∈c​aQ​(𝒳)\mu\in ca\_{Q}(\mathcal{X}) on the left side proves the assertion.

(iv) Let g​(Y):=supμ∈c​aQ​(𝒳)∫Y​𝑑μ−f¯​(μ)g(Y):=\sup\_{\mu\in ca\_{Q}(\mathcal{X})}\int Yd\mu-\overline{f}(\mu), Y∈𝒳Y\in\mathcal{X}. By definition, g≤fD≤fg\leq f\_{D}\leq f. Therefore, f¯Q​(μ)≤f¯​(μ)\overline{f}^{Q}(\mu)\leq\overline{f}(\mu) for all μ∈c​aQ​(𝒳)\mu\in ca\_{Q}(\mathcal{X}) by (iii). Moreover, for μ∈c​aQ​(𝒳)\mu\in ca\_{Q}(\mathcal{X}), we have

|  |  |  |
| --- | --- | --- |
|  | f¯Q​(μ)=supX∈𝒳∫X​𝑑μ−fEQ​(X)≥supX∈𝒳∫X​𝑑μ−f​(X)=f¯​(μ)\overline{f}^{Q}(\mu)=\sup\_{X\in\mathcal{X}}\int Xd\mu-f^{Q}\_{E}(X)\geq\sup\_{X\in\mathcal{X}}\int Xd\mu-f(X)=\overline{f}(\mu) |  |

since fEQ≤ff\_{E}^{Q}\leq f by Lemma [3.3](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").

(v) follows from (iv).

(vi) follows from (ii) and (iii).
∎

Provided that 𝒳\mathcal{X} admits a locally convex topology and the corresponding dual space is consistent with c​acca\_{c}, Lemma [3.6](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem6 "Lemma 3.6. ‣ 3.1 Properties of 𝓟-Sensitive Functions ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") (iv) implies that fDQf^{Q}\_{D} is the convex, lower semicontinuous regularization of ff (or fEQf\_{E}^{Q}) under QQ (see [[15](https://arxiv.org/html/2601.19511v1#bib.bib25 "Convex analysis and variational problems"), Part One, Definition 3.2]).

###### Proposition 3.9.

Suppose that f:𝒳→[−∞,∞]f\colon\mathcal{X}\to[-\infty,\infty] admits a dual representation over c​ac​(𝒳)ca\_{c}(\mathcal{X}). Let 𝒬⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathfrak{P}\_{c}(\Omega) be non-empty with

|  |  |  |
| --- | --- | --- |
|  | {μ∈c​ac​(𝒳)∣f¯​(μ)∈ℝ}⊆⋃Q∈𝒬c​aQ​(𝒳).\{\mu\in ca\_{c}(\mathcal{X})\mid\overline{f}(\mu)\in\mathbb{R}\}\subseteq\bigcup\_{Q\in\mathcal{Q}}ca\_{Q}(\mathcal{X}). |  |

Then 𝒬\mathcal{Q} is a reduction set for ff and f=fE𝒬=fD𝒬f=f^{\mathcal{Q}}\_{E}=f^{\mathcal{Q}}\_{D}.

###### Proof.

By assumption, f=fDf=f\_{D}. Let ℳ:={μ∈c​ac​(𝒳)∣f¯​(μ)<∞}\mathcal{M}:=\{\mu\in ca\_{c}(\mathcal{X})\mid\overline{f}(\mu)<\infty\}. Suppose that ℳ=∅\mathcal{M}=\emptyset. Then f≡−∞f\equiv-\infty, and thus fDQ≡−∞f^{Q}\_{D}\equiv-\infty for all Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega). From now on assume that ℳ≠∅\mathcal{M}\neq\emptyset. If there exists μ∈c​ac​(𝒳)\mu\in ca\_{c}(\mathcal{X}) such that f¯​(μ)=−∞\overline{f}(\mu)=-\infty, then f≡∞f\equiv\infty. In that case f¯≡−∞\overline{f}\equiv-\infty, and thus fDQ≡∞f^{Q}\_{D}\equiv\infty for all Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega) by Lemma [3.8](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem8 "Lemma 3.8. ‣ 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"). Hence, assume that f¯​(μ)>−∞\overline{f}(\mu)>-\infty for all μ∈c​ac​(𝒳)\mu\in ca\_{c}(\mathcal{X}).
Recalling that fDQ≤ff^{Q}\_{D}\leq f and Lemma [3.8](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem8 "Lemma 3.8. ‣ 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") (iv), for all X∈𝒳X\in\mathcal{X},

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(X)\displaystyle f(X) | =supμ∈ℳ∫X​𝑑μ−f¯​(μ)=supμ∈ℳ∩⋃Q∈𝒬c​aQ∫X​𝑑μ−f¯​(μ)\displaystyle=\sup\_{\mu\in\mathcal{M}}\int Xd\mu-\overline{f}(\mu)\qquad=\qquad\sup\_{\mu\in\mathcal{M}\cap\bigcup\_{Q\in\mathcal{Q}}ca\_{Q}}\int Xd\mu-\overline{f}(\mu) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =supQ∈𝒬supμ∈ℳ∩c​aQ∫X​𝑑μ−f¯​(μ)≤supQ∈𝒬supμ∈c​aQ​(𝒳)∫X​𝑑μ−f¯​(μ)\displaystyle=\sup\_{Q\in\mathcal{Q}}\sup\_{\mu\in\mathcal{M}\cap ca\_{Q}}\int Xd\mu-\overline{f}(\mu)\qquad\leq\qquad\sup\_{Q\in\mathcal{Q}}\sup\_{\mu\in ca\_{Q}(\mathcal{X})}\int Xd\mu-\overline{f}(\mu) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =supQ∈𝒬fDQ​(X)≤f​(X).\displaystyle=\sup\_{Q\in\mathcal{Q}}f^{Q}\_{D}(X)\qquad\leq\qquad f(X). |  |

Thus, f=fD𝒬f=f^{\mathcal{Q}}\_{D} and 𝒬\mathcal{Q} is a reduction set for ff according to Lemma [2.12](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem12 "Lemma 2.12. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"). Finally, recall that always f≥fE𝒬≥fD𝒬f\geq f^{\mathcal{Q}}\_{E}\geq f^{\mathcal{Q}}\_{D}.
∎

###### Theorem 3.10.

Let f:𝒳→[−∞,∞]f\colon\mathcal{X}\to[-\infty,\infty]. The following are equivalent:

* (i)

  ff admits a dual representation over c​ac​(𝒳)ca\_{c}(\mathcal{X}).
* (ii)

  f=fDf=f\_{D}.
* (iii)

  There is a non-empty set 𝒬⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathfrak{P}\_{c}(\Omega) such that f=fD𝒬f=f^{\mathcal{Q}}\_{D}.
* (iv)

  ff is 𝒫\mathcal{P}-sensitive and, for a reduction set 𝒬⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathfrak{P}\_{c}(\Omega) of ff, there exists a 𝒬\mathcal{Q}-localization (fQ)Q∈𝒬(f^{Q})\_{Q\in\mathcal{Q}} of ff such that each fQf^{Q} admits a representation ([7](https://arxiv.org/html/2601.19511v1#S3.E7 "In item (iii) ‣ Lemma 3.8. ‣ 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")).

In particular, let 𝒬⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathfrak{P}\_{c}(\Omega) be non-empty and suppose that, for all Q∈𝒬Q\in\mathcal{Q}, jQ​(𝒳)j\_{Q}(\mathcal{X}) admits a topology τQ\tau^{Q} such that (jQ​(𝒳),τQ)(j\_{Q}(\mathcal{X}),\tau^{Q}) is a locally convex space with dual space 𝒴Q⊆c​aQ\mathcal{Y}^{Q}\subseteq ca\_{Q}. If there is a 𝒬\mathcal{Q}-localization (fQ)Q∈𝒬(f^{Q})\_{Q\in\mathcal{Q}} of ff such that each fQ∘jQ−1f^{Q}\circ j\_{Q}^{-1} (recall Remark [2.11](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem11 "Remark 2.11. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) is convex, lower semicontinuous (with respect to τQ\tau^{Q}), and takes the value −∞-\infty only if fQ≡−∞f^{Q}\equiv-\infty, then ff admits a dual representation over c​ac​(𝒳)ca\_{c}(\mathcal{X}).

###### Proof.

(i) ⇔\Leftrightarrow (ii): Shown above.

(i) ⇒\Rightarrow (iii): Suppose that the dual representation of ff is given as in ([6](https://arxiv.org/html/2601.19511v1#S3.E6 "In 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")). Consider the set

|  |  |  |
| --- | --- | --- |
|  | 𝒬:={|μ||μ​(Ω)||μ∈c​ac​(𝒳)∖{0}}∪{P}⊆𝔓c​(Ω),\mathcal{Q}:=\bigg\{\frac{|\mu|}{|\mu(\Omega)|}\biggm|\mu\in ca\_{c}(\mathcal{X})\setminus\{0\}\bigg\}\cup\{P\}\subseteq\mathfrak{P}\_{c}(\Omega), |  |

where P∈𝔓c​(Ω)P\in\mathfrak{P}\_{c}(\Omega) is arbitrary. For each μ∈c​ac​(𝒳)\mu\in ca\_{c}(\mathcal{X}) there is Q∈𝒬Q\in\mathcal{Q} such that μ≪Q\mu\ll Q. Now apply Proposition [3.9](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem9 "Proposition 3.9. ‣ 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").

(iii) ⇒\Rightarrow (iv): This follows from Theorem [3.2](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").

(iv) ⇒\Rightarrow (ii): By Lemma [3.8](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem8 "Lemma 3.8. ‣ 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), we have fQ≤fDQf^{Q}\leq f\_{D}^{Q} for all Q∈𝒬Q\in\mathcal{Q} and therefore,

|  |  |  |
| --- | --- | --- |
|  | f=supQ∈𝒬fQ≤supQ∈𝒬fDQ≤fD≤f.f=\sup\_{Q\in\mathcal{Q}}f^{Q}\leq\sup\_{Q\in\mathcal{Q}}f^{Q}\_{D}\leq f\_{D}\leq f. |  |

Finally, if (jQ​(𝒳),τQ)(j\_{Q}(\mathcal{X}),\tau^{Q}) is a locally convex space with dual space 𝒴Q⊆c​aQ\mathcal{Y}^{Q}\subseteq ca\_{Q}, then 𝒴Q⊆c​aQ​(𝒳)\mathcal{Y}^{Q}\subseteq ca\_{Q}(\mathcal{X}), and the Fenchel-Moreau theorem (see, e.g., [[15](https://arxiv.org/html/2601.19511v1#bib.bib25 "Convex analysis and variational problems"), Part One, Proposition 3.1]) implies that, under the stated conditions, fQ∘jQ−1f^{Q}\circ j\_{Q}^{-1} admits a dual representation (on (jQ​(𝒳),τQ)(j\_{Q}(\mathcal{X}),\tau^{Q})), which implies that fQf^{Q} admits a dual representation ([7](https://arxiv.org/html/2601.19511v1#S3.E7 "In item (iii) ‣ Lemma 3.8. ‣ 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")). Hence, we have (iv), and therefore (i).
∎

If one of the conditions of Theorem [3.10](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem10 "Theorem 3.10. ‣ 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") is satisfied, then f=fD=fEf=f\_{D}=f\_{E} (see Theorem [3.2](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")).
In Section [4.2](https://arxiv.org/html/2601.19511v1#S4.SS2 "4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), we show that fDQ<fEQf\_{D}^{Q}<f^{Q}\_{E} is possible even if f=fDf=f\_{D}, and we discuss sufficient conditions for fEQ=fDQf\_{E}^{Q}=f^{Q}\_{D} tailored to robust monetary risk measures.

## 4 Applications

### 4.1 Robust Optimization

Let 𝒳⊆Lc0\mathcal{X}\subseteq L^{0}\_{c} be non-empty. Further, let f:𝒳→[−∞,∞]f:\mathcal{X}\to[-\infty,\infty], and consider the minimization (maximization) problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(X)→min⁡(max)​subject to ​X∈𝒞,f(X)\to\min\,(\max)\qquad\text{subject to }X\in\mathcal{C}, |  | (8) |

where 𝒞⊆𝒳\mathcal{C}\subseteq\mathcal{X} is a non-empty set.

###### Proposition 4.1.

Suppose that ff and 𝒞\mathcal{C} are 𝒫\mathcal{P}-sensitive, and that there exists a joint reduction set 𝒬\mathcal{Q} for ff and 𝒞\mathcal{C}. Let (fQ)Q∈𝒬(f^{Q})\_{Q\in\mathcal{Q}} be a 𝒬\mathcal{Q}-localization of ff (see Theorem [3.2](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")). Moreover, suppose that, for each Q∈𝒬Q\in\mathcal{Q}, XQ∗∈𝒳X^{\ast}\_{Q}\in\mathcal{X} is a solution to the optimization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | fQ​(X)→min⁡(max)​subject to​X∈𝒞.f^{Q}(X)\to\min\,(\max)\qquad\mbox{subject to}\;X\in\mathcal{C}. |  | (9) |

Then any 𝒬\mathcal{Q}-aggregator X∗X^{\ast} of the family (XQ∗)Q∈𝒬(X^{\ast}\_{Q})\_{Q\in\mathcal{Q}} (if it exists) is a solution to ([8](https://arxiv.org/html/2601.19511v1#S4.E8 "In 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")).

Recalling Remark [2.11](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem11 "Remark 2.11. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), note that solving ([9](https://arxiv.org/html/2601.19511v1#S4.E9 "In Proposition 4.1. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) is indeed equivalent to solving

|  |  |  |  |
| --- | --- | --- | --- |
|  | fQ∘jQ−1​(Y)→min⁡(max)​subject to​Y∈jQ​(𝒞)f^{Q}\circ j\_{Q}^{-1}(Y)\to\min\,(\max)\qquad\mbox{subject to}\;Y\in j\_{Q}(\mathcal{C}) |  | (10) |

in the sense that if XQ∗X^{\ast}\_{Q} solves ([9](https://arxiv.org/html/2601.19511v1#S4.E9 "In Proposition 4.1. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")), then jQ​(XQ∗)j\_{Q}(X^{\ast}\_{Q}) solves ([10](https://arxiv.org/html/2601.19511v1#S4.E10 "In 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")), and for any solution Y∗Y^{\ast} of ([10](https://arxiv.org/html/2601.19511v1#S4.E10 "In 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")), any element in jQ−1​(Y)∩𝒞j\_{Q}^{-1}(Y)\cap\mathcal{C} is a solution to ([9](https://arxiv.org/html/2601.19511v1#S4.E9 "In Proposition 4.1. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")). ([10](https://arxiv.org/html/2601.19511v1#S4.E10 "In 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) is an optimization problem on a subset of LQ0L^{0}\_{Q} under the dominating probability measure QQ. Here, a classical machinery for solving such problems is available, in particular if each fQf^{Q} is convex and admits a dual representation ([7](https://arxiv.org/html/2601.19511v1#S3.E7 "In item (iii) ‣ Lemma 3.8. ‣ 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")).

###### Proof of Proposition [4.1](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").

Since 𝒞\mathcal{C} is 𝒬\mathcal{Q}-stable by Lemma [2.17](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem17 "Lemma 2.17. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), we conclude that X∗∈𝒞X^{\ast}\in\mathcal{C}. Suppose that Y∈𝒞Y\in\mathcal{C} satisfies f​(Y)<f​(X∗)f(Y)<f(X^{\ast}) (f​(Y)>f​(X∗)f(Y)>f(X^{\ast})). Then, as f=supQ∈𝒬fQf=\sup\_{Q\in\mathcal{Q}}f^{Q}, there is Q∈𝒬Q\in\mathcal{Q} such that

|  |  |  |
| --- | --- | --- |
|  | fQ​(Y)<fQ​(X∗)=fQ​(XQ∗)​(fQ​(Y)>fQ​(X∗)=fQ​(XQ∗))f^{Q}(Y)<f^{Q}(X^{\ast})=f^{Q}(X^{\ast}\_{Q})\qquad\big(f^{Q}(Y)>f^{Q}(X^{\ast})=f^{Q}(X^{\ast}\_{Q})\big) |  |

where the last equality holds due to the QQ-consistency of fQf^{Q}. This contradicts the assumed optimality of XQ∗X^{\ast}\_{Q}.
∎

###### Corollary 4.2.

Suppose that ff is upper 𝒫\mathcal{P}-sensitive and 𝒞\mathcal{C} is 𝒫\mathcal{P}-sensitive, and that there exists a joint reduction set 𝒬\mathcal{Q} for 𝒞\mathcal{C} and all upper level sets of ff. Let (fQ)Q∈𝒬(f^{Q})\_{Q\in\mathcal{Q}} be a 𝒬\mathcal{Q}-consistent family of functions such that ([5](https://arxiv.org/html/2601.19511v1#S3.E5 "In Remark 3.4. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) holds. Moreover, suppose that for each Q∈𝒬Q\in\mathcal{Q}, XQ∗∈𝒳X^{\ast}\_{Q}\in\mathcal{X} is a solution to ([9](https://arxiv.org/html/2601.19511v1#S4.E9 "In Proposition 4.1. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")).
Then any 𝒬\mathcal{Q}-aggregator X∗X^{\ast} of the family (XQ∗)Q∈𝒬(X^{\ast}\_{Q})\_{Q\in\mathcal{Q}} (if it exists) is a solution to ([8](https://arxiv.org/html/2601.19511v1#S4.E8 "In 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")).

###### Proof.

Apply Proposition [4.1](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") to −f-f.
∎

In view of Proposition [4.1](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), in Lemma [4.4](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") we give a condition which guarantees that there always exists a 𝒬\mathcal{Q}-aggregator X∗X^{\ast} of the family (XQ∗)Q∈𝒬(X^{\ast}\_{Q})\_{Q\in\mathcal{Q}} if (XQ∗)Q∈𝒬(X^{\ast}\_{Q})\_{Q\in\mathcal{Q}} is sufficiently bounded. To this end, we will need to distinguish between so-called supported and unsupported probability measures:

###### Definition 4.3.

A probability measure Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega) is called supported if there is an event S​(Q)∈ℱS(Q)\in\mathcal{F} such that

1. (i)

   Q​(S​(Q)c)=0Q(S(Q)^{c})=0,
2. (ii)

   whenever N∈ℱN\in\mathcal{F} satisfies Q​(N)=0Q(N)=0, then N∩S​(Q)N\cap S(Q) is 𝒫\mathcal{P}-polar.

The set S​(Q)S(Q) is called the (order) support of QQ.

Supported measures play a key role in handling robustness. Standard robust models, such as volatility uncertainty models, are based on supported probability measures, see [[23](https://arxiv.org/html/2601.19511v1#bib.bib35 "Model uncertainty: a reverse approach")] for a detailed review. Note that if two sets S,S′∈ℱS,S^{\prime}\in\mathcal{F} satisfy conditions (i) and (ii) in Definition [4.3](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem3 "Definition 4.3. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), then χS=χS′\chi\_{S}=\chi\_{S^{\prime}} 𝒫\mathcal{P}-q.s. (𝟏S=𝟏S′{\bf 1}\_{S}={\bf 1}\_{S^{\prime}}), i.e., the symmetric difference S△S′S\bigtriangleup S^{\prime} is 𝒫\mathcal{P}-polar. The order support S​(Q)S(Q) is thus usually not unique as an event, but only unique up to 𝒫\mathcal{P}-polar events. In the following, S​(Q)S(Q) therefore denotes an arbitrary version of the order support.

We recall that 𝒳\mathcal{X} is said to be Dedekind complete if every bounded set 𝒟⊂𝒳\mathcal{D}\subset\mathcal{X} admits a least upper bound in 𝒳\mathcal{X}. For a detailed discussion of Dedekind completeness of robust model spaces, we again refer to [[23](https://arxiv.org/html/2601.19511v1#bib.bib35 "Model uncertainty: a reverse approach")]. Versions of Lemma [4.4](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") and Corollary [4.6](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem6 "Corollary 4.6. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") are found in the literature (see, e.g., [[24](https://arxiv.org/html/2601.19511v1#bib.bib128 "Sur l’existence d’une plus petite sous-tribu exhaustive par paire")]). We state their short proofs for the sake of completeness.

###### Lemma 4.4.

Suppose that 𝒳\mathcal{X} is Dedekind complete and let 𝒬⊂𝔓c​(Ω)\mathcal{Q}\subset\mathfrak{P}\_{c}(\Omega) be non-empty. Moreover, suppose that each Q∈𝒬Q\in\mathcal{Q} is supported. Consider any family (XQ)Q∈𝒬⊆𝒳(X^{Q})\_{Q\in\mathcal{Q}}\subseteq\mathcal{X} which is pairwise 𝒬\mathcal{Q}-coherent, that is, for all Q,Q′∈𝒬Q,Q^{\prime}\in\mathcal{Q}, we have

|  |  |  |
| --- | --- | --- |
|  | XQ​𝟏S​(Q)∩S​(Q′)=XQ′​𝟏S​(Q)∩S​(Q′),X^{Q}\mathbf{1}\_{S(Q)\cap S(Q^{\prime})}=X^{Q^{\prime}}\mathbf{1}\_{S(Q)\cap S(Q^{\prime})}, |  |

and bounded in the sense that there exists some Y∈𝒳Y\in\mathcal{X} such that |XQ|​𝟏S​(Q)≼Y|X^{Q}|\mathbf{1}\_{S(Q)}\preccurlyeq Y. Then (XQ)Q∈𝒬(X^{Q})\_{Q\in\mathcal{Q}} is 𝒬\mathcal{Q}-coherent (and thus admits a 𝒬\mathcal{Q}-aggregator).

###### Proof.

As the family YQ:=XQ​𝟏S​(Q)−Y​𝟏S​(Q)cY^{Q}:=X^{Q}\mathbf{1}\_{S(Q)}-Y\mathbf{1}\_{S(Q)^{c}}, Q∈𝒬Q\in\mathcal{Q}, is bounded by YY, there exists a least upper bound XX of (YQ)Q∈𝒬(Y^{Q})\_{Q\in\mathcal{Q}}. We will show that jQ​(X)=jQ​(XQ)j\_{Q}(X)=j\_{Q}(X^{Q}) for all Q∈𝒬Q\in\mathcal{Q}. To this end, let Q′∈𝒬Q^{\prime}\in\mathcal{Q}. By XX being an upper bound, we know that jQ′​(XQ′)=jQ′​(YQ′)≤Q′jQ′​(X)j\_{Q^{\prime}}(X^{Q^{\prime}})=j\_{Q^{\prime}}(Y^{Q^{\prime}})\leq\_{Q^{\prime}}j\_{Q^{\prime}}(X). Suppose that Q′​(XQ′<X)>0Q^{\prime}(X^{Q^{\prime}}<X)>0. Let Z:=XQ′​𝟏S​(Q′)+X​𝟏S​(Q′)cZ:=X^{Q^{\prime}}\mathbf{1}\_{S(Q^{\prime})}+X\mathbf{1}\_{S(Q^{\prime})^{c}}. Then Z≼XZ\preccurlyeq X and Z≠XZ\neq X. Clearly, by definition of XX, we have that

|  |  |  |
| --- | --- | --- |
|  | 𝟏S​(Q′)c​YQ≼𝟏S​(Q′)c​X=𝟏S​(Q′)c​Z\mathbf{1}\_{S(Q^{\prime})^{c}}Y^{Q}\preccurlyeq\mathbf{1}\_{S(Q^{\prime})^{c}}X=\mathbf{1}\_{S(Q^{\prime})^{c}}Z |  |

for all Q∈𝒬Q\in\mathcal{Q}. To see that YQ​𝟏S​(Q′)≼Z​𝟏S​(Q′)Y^{Q}\mathbf{1}\_{S(Q^{\prime})}\preccurlyeq Z\mathbf{1}\_{S(Q^{\prime})} holds for all Q∈𝒬Q\in\mathcal{Q}, we first note that −Y≼Z-Y\preccurlyeq Z and thus

|  |  |  |
| --- | --- | --- |
|  | YQ​𝟏S​(Q′)∩S​(Q)c=−Y​𝟏S​(Q′)∩S​(Q)c≼Z​𝟏S​(Q′)∩S​(Q)c.Y^{Q}\mathbf{1}\_{S(Q^{\prime})\cap S(Q)^{c}}=-Y\mathbf{1}\_{S(Q^{\prime})\cap S(Q)^{c}}\preccurlyeq Z\mathbf{1}\_{S(Q^{\prime})\cap S(Q)^{c}}. |  |

On S​(Q′)∩S​(Q)S(Q^{\prime})\cap S(Q), by pairwise 𝒬\mathcal{Q}-coherence of (XQ)Q∈𝒬(X^{Q})\_{Q\in\mathcal{Q}}, we have

|  |  |  |
| --- | --- | --- |
|  | YQ​𝟏S​(Q′)∩S​(Q)=XQ​𝟏S​(Q′)∩S​(Q)=XQ′​𝟏S​(Q′)∩S​(Q)=Z​𝟏S​(Q′)∩S​(Q).Y^{Q}\mathbf{1}\_{S(Q^{\prime})\cap S(Q)}=X^{Q}\mathbf{1}\_{S(Q^{\prime})\cap S(Q)}=X^{Q^{\prime}}\mathbf{1}\_{S(Q^{\prime})\cap S(Q)}=Z\mathbf{1}\_{S(Q^{\prime})\cap S(Q)}. |  |

Overall, it then follows that for all Q∈𝒬Q\in\mathcal{Q},

|  |  |  |  |
| --- | --- | --- | --- |
|  | YQ\displaystyle Y^{Q} | =𝟏S​(Q′)∩S​(Q)​YQ+𝟏S​(Q′)∩S​(Q)c​YQ+𝟏S​(Q′)c​YQ\displaystyle=\mathbf{1}\_{S(Q^{\prime})\cap S(Q)}Y^{Q}+\mathbf{1}\_{S(Q^{\prime})\cap S(Q)^{c}}Y^{Q}+\mathbf{1}\_{S(Q^{\prime})^{c}}Y^{Q} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≼𝟏S​(Q′)∩S​(Q)​Z+𝟏S​(Q′)∩S​(Q)c​Z+𝟏S​(Q′)c​Z=Z\displaystyle\preccurlyeq\mathbf{1}\_{S(Q^{\prime})\cap S(Q)}Z+\mathbf{1}\_{S(Q^{\prime})\cap S(Q)^{c}}Z+\mathbf{1}\_{S(Q^{\prime})^{c}}Z=Z |  |

Hence, ZZ is an upper bound of (YQ)Q∈𝒬(Y^{Q})\_{Q\in\mathcal{Q}} with Z≼XZ\preccurlyeq X and Z≠XZ\neq X, contradicting the fact that XX is the least upper bound. Therefore, we must have Q′​(XQ′<X)=0Q^{\prime}(X^{Q^{\prime}}<X)=0 which shows that indeed jQ′​(X)=jQ′​(XQ′)j\_{Q^{\prime}}(X)=j\_{Q^{\prime}}(X^{Q^{\prime}}).
∎

Note that, when 𝒬\mathcal{Q} is uncountable (which is the interesting case), the assertion of Lemma [4.4](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), that pairwise 𝒬\mathcal{Q}-coherence implies 𝒬\mathcal{Q}-coherence, is not as obvious as it may seem on a first glance.

###### Definition 4.5.

Supported probability measures Q,Q′∈𝔓c​(Ω)Q,Q^{\prime}\in\mathfrak{P}\_{c}(\Omega) are called disjoint if S​(Q)∩S​(Q′)S(Q)\cap S(Q^{\prime}) is a 𝒫\mathcal{P}-polar set (for any choice of S​(Q)S(Q) and S​(Q′)S(Q^{\prime})) or, equivalently, 𝟏S​(Q)∧𝟏S​(Q′)=0\mathbf{1}\_{S(Q)}\wedge\mathbf{1}\_{S(Q^{\prime})}=0.

In fact, many robust models assume disjoint supported reference measures, see [[23](https://arxiv.org/html/2601.19511v1#bib.bib35 "Model uncertainty: a reverse approach")].

###### Corollary 4.6.

Suppose that 𝒳\mathcal{X} is Dedekind complete and let 𝒬⊂𝔓c​(Ω)\mathcal{Q}\subset\mathfrak{P}\_{c}(\Omega) be non-empty. Moreover, suppose that each Q∈𝒬Q\in\mathcal{Q} is supported and the elements of 𝒬\mathcal{Q} are mutually disjoint. Consider any family (XQ)Q∈𝒬⊆𝒳(X^{Q})\_{Q\in\mathcal{Q}}\subseteq\mathcal{X} which is bounded in the sense that there is Y∈𝒳Y\in\mathcal{X} with |XQ|​𝟏S​(Q)≼Y|X^{Q}|\mathbf{1}\_{S(Q)}\preccurlyeq Y. Then (XQ)Q∈𝒬(X^{Q})\_{Q\in\mathcal{Q}} is 𝒬\mathcal{Q}-coherent (and thus admits a 𝒬\mathcal{Q}-aggregator).

###### Proof.

Since 𝟏S​(Q)∩S​(Q′)=0\mathbf{1}\_{S(Q)\cap S(Q^{\prime})}=0 for all Q,Q′∈𝒬Q,Q^{\prime}\in\mathcal{Q}, every family (XQ)Q∈𝒬⊆𝒳(X^{Q})\_{Q\in\mathcal{Q}}\subseteq\mathcal{X} is pairwise 𝒬\mathcal{Q}-coherent. By Lemma [4.4](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), the result follows.
∎

###### Example 4.7 (Bliss point consumption).

Suppose that 𝒳\mathcal{X} is Dedekind complete and each P∈𝒫P\in\mathcal{P} is supported. Let A,B∈𝒳A,B\in\mathcal{X} such that A≼BA\preccurlyeq B and set 𝒞:={X∈𝒳∣A≼X≼B}\mathcal{C}:=\{X\in\mathcal{X}\mid A\preccurlyeq X\preccurlyeq B\}. We interpret each X∈𝒞X\in\mathcal{C} as an admissible consumption plan and A,B∈𝒳A,B\in\mathcal{X} as global lower and upper constraints. Note that 𝒞\mathcal{C} is 𝒫\mathcal{P}-sensitive with reduction set 𝒫\mathcal{P}. Indeed, let X∈𝒳X\in\mathcal{X} satisfy jP​(X)∈jP​(𝒞)j\_{P}(X)\in j\_{P}(\mathcal{C}), that is A≤PX≤PBA\leq\_{P}X\leq\_{P}B, for all P∈𝒫P\in\mathcal{P}, then, by definition of the 𝒫\mathcal{P}-q.s. order, A≼X≼BA\preccurlyeq X\preccurlyeq B, so X∈𝒞X\in\mathcal{C}.

Locally, that is, under each reference measure P∈𝒫P\in\mathcal{P}, YP∈𝒳Y^{P}\in\mathcal{X} denotes a target consumption level. We suppose that the family (YP)P∈𝒫(Y^{P})\_{P\in\mathcal{P}} is pairwise 𝒫\mathcal{P}-coherent. The task is to find a consumption plan X∗∈𝒞X^{\ast}\in\mathcal{C} that minimizes

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(X):=supP∈𝒫EP​[(YP−X)2]​subject to ​X∈𝒞.f(X):=\sup\_{P\in\mathcal{P}}E\_{P}\big[(Y^{P}-X)^{2}\big]\qquad\mbox{subject to }\;X\in\mathcal{C}. |  | (11) |

For each P∈𝒫P\in\mathcal{P}, define fP:𝒳→[−∞,∞]f^{P}\colon\mathcal{X}\to[-\infty,\infty] by

|  |  |  |
| --- | --- | --- |
|  | fP​(X):=EP​[(YP−X)2].f^{P}(X):=E\_{P}\big[(Y^{P}-X)^{2}\big]. |  |

Clearly, ff is 𝒫\mathcal{P}-sensitive with reduction set 𝒫\mathcal{P} (see Lemma [2.12](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem12 "Lemma 2.12. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) and (fP)P∈𝒫(f^{P})\_{P\in\mathcal{P}} is a 𝒫\mathcal{P}-localization of ff. Further, we obtain the local optimizers

|  |  |  |
| --- | --- | --- |
|  | XP∗:=A​𝟏{YP≼A}+YP​𝟏{A≼YP≼B,A≠YP}+B​𝟏{B≼YP,YP≠B}∈𝒞.X\_{P}^{\*}:=A\mathbf{1}\_{\{Y^{P}\preccurlyeq A\}}+Y^{P}\mathbf{1}\_{\{A\preccurlyeq Y^{P}\preccurlyeq B,A\neq Y^{P}\}}+B\mathbf{1}\_{\{B\preccurlyeq Y^{P},Y^{P}\neq B\}}\in\mathcal{C}. |  |

Fix P,P′∈𝒫P,P^{\prime}\in\mathcal{P}. Then, since (YP)P∈𝒫(Y^{P})\_{P\in\mathcal{P}} is pairwise 𝒫\mathcal{P}-coherent, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | XP∗​𝟏S​(P)∩S​(P′)\displaystyle X\_{P}^{\*}\mathbf{1}\_{S(P)\cap S(P^{\prime})} | =(A​𝟏{YP≼A}+YP​𝟏{A≼YP≼B,A≠YP}+B​𝟏{B≼YP,YP≠B})​𝟏S​(P)∩S​(P′)\displaystyle=\big(A\mathbf{1}\_{\{Y^{P}\preccurlyeq A\}}+Y^{P}\mathbf{1}\_{\{A\preccurlyeq Y^{P}\preccurlyeq B,A\neq Y^{P}\}}+B\mathbf{1}\_{\{B\preccurlyeq Y^{P},Y^{P}\neq B\}}\big)\mathbf{1}\_{S(P)\cap S(P^{\prime})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(A​𝟏{YP′≼A}+YP′​𝟏{A≼YP′≼B,A≠YP′}+B​𝟏{B≼YP′,YP′≠B})​𝟏S​(P)∩S​(P′)\displaystyle=\big(A\mathbf{1}\_{\{Y^{P^{\prime}}\preccurlyeq A\}}+Y^{P^{\prime}}\mathbf{1}\_{\{A\preccurlyeq Y^{P^{\prime}}\preccurlyeq B,A\neq Y^{P^{\prime}}\}}+B\mathbf{1}\_{\{B\preccurlyeq Y^{P^{\prime}},Y^{P^{\prime}}\neq B\}}\big)\mathbf{1}\_{S(P)\cap S(P^{\prime})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =XP′∗​𝟏S​(P)∩S​(P′).\displaystyle=X\_{P^{\prime}}^{\*}\mathbf{1}\_{S(P)\cap S(P^{\prime})}. |  |

Hence, (XP∗)P∈𝒫(X\_{P}^{\*})\_{P\in\mathcal{P}} is pairwise 𝒫\mathcal{P}-coherent and |XP∗|​𝟏S​(P)≼|XP∗|≼|A|∨|B|\lvert X\_{P}^{\*}\rvert\mathbf{1}\_{S(P)}\preccurlyeq\lvert X\_{P}^{\*}\rvert\preccurlyeq\lvert A\rvert\vee\lvert B\rvert for all P∈𝒫P\in\mathcal{P}. By Lemma [4.4](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), there exists a 𝒫\mathcal{P}-aggregator X∗X^{\*} of the family (XP∗)P∈𝒫(X\_{P}^{\*})\_{P\in\mathcal{P}}.
Consequently, X∗X^{\*} solves ([11](https://arxiv.org/html/2601.19511v1#S4.E11 "In Example 4.7 (Bliss point consumption). ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) according to Proposition [4.1](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"). ⋄\diamond

### 4.2 Monetary Risk Measures and Localization Bubbles

In this section, 𝒳=Lc∞\mathcal{X}=L^{\infty}\_{c} and thus c​ac​(𝒳)=c​acca\_{c}(\mathcal{X})=ca\_{c}.

###### Definition 4.8.

A mapping ρ:Lc∞→ℝ\rho\colon L^{\infty}\_{c}\to\mathbb{R} is called a monetary risk measure if it is monotone and cash-additive (see Section [3.1](https://arxiv.org/html/2601.19511v1#S3.SS1 "3.1 Properties of 𝓟-Sensitive Functions ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")). 𝒜ρ:={X∈Lc∞∣ρ​(X)≤0}\mathcal{A}\_{\rho}:=\{X\in L^{\infty}\_{c}\mid\rho(X)\leq 0\} denotes the acceptance set of ρ\rho. If ρ\rho is, in addition, convex, ρ\rho is called a convex risk measure. A convex risk measure which is also positively homogeneous is called a coherent risk measure.

ρ​(X)\rho(X) is a capital requirement which may also be seen as the indifference price of the loss XX. In fact, charging ρ​(X)\rho(X) reduces the loss to X−ρ​(X)X-\rho(X), which is acceptable since ρ​(X−ρ​(X))=0\rho(X-\rho(X))=0 by cash-additivity. Let Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega). We may interpret ρEQ\rho^{Q}\_{E} as the minimal price from a QQ-perspective charged by the market with aggregate risk measure ρ\rho for taking a loss XX. Indeed, from a QQ-perspective, all losses YY such that jQ​(Y)=jQ​(X)j\_{Q}(Y)=j\_{Q}(X) are the same. Thus, when we hand the loss XX to the market, we buy a contract YY such that jQ​(Y)=jQ​(X)j\_{Q}(Y)=j\_{Q}(X)—which therefore secures XX from the QQ perspective—at minimal price. In other words, the price is inf{ρ​(Y)∣jQ​(Y)=jQ​(X)}\inf\{\rho(Y)\mid j\_{Q}(Y)=j\_{Q}(X)\} (or arbitrarily close when this infimum is not attained), which is exactly ρEQ​(X)\rho^{Q}\_{E}(X) according to Lemma [3.3](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"). By Lemma [3.6](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem6 "Lemma 3.6. ‣ 3.1 Properties of 𝓟-Sensitive Functions ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") and Lemma [4.10](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem10 "Lemma 4.10. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") below, ρEQ\rho^{Q}\_{E} is a monetary risk measure provided that ρEQ​(0)∈ℝ\rho^{Q}\_{E}(0)\in\mathbb{R}. Otherwise, we are in a degenerate situation.

###### Definition 4.9.

Let ρ:Lc∞→ℝ\rho\colon L^{\infty}\_{c}\to\mathbb{R} be a monetary risk measure and Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega). We call ρEQ\rho^{Q}\_{E} relevant if ρEQ​(0)∈ℝ\rho^{Q}\_{E}(0)\in\mathbb{R}.

###### Lemma 4.10.

Let ρ:Lc∞→ℝ\rho\colon L^{\infty}\_{c}\to\mathbb{R} be a monetary risk measure and Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega). Then the following are equivalent:

1. (i)

   ρEQ\rho^{Q}\_{E} is a monetary risk measure.
2. (ii)

   ρEQ\rho^{Q}\_{E} is relevant.
3. (iii)

   sup{m∈ℝ∣m∈jQ​(𝒜ρ)}<∞\sup\{m\in\mathbb{R}\mid m\in j\_{Q}(\mathcal{A}\_{\rho})\}<\infty.

###### Proof.

(i) obviously implies (ii). In order to prove that (ii) implies (i), recall that according to Lemma [3.6](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem6 "Lemma 3.6. ‣ 3.1 Properties of 𝓟-Sensitive Functions ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), ρEQ\rho^{Q}\_{E} is monotone and cash-additive, and thus a monetary risk measure on Lc∞L^{\infty}\_{c}, provided that ρEQ\rho\_{E}^{Q} is real-valued. If ρEQ\rho^{Q}\_{E} is relevant, then by cash-additivity, ρEQ​(m)=ρEQ​(0)+m∈ℝ\rho\_{E}^{Q}(m)=\rho^{Q}\_{E}(0)+m\in\mathbb{R} for all m∈ℝm\in\mathbb{R}. Moreover, since

|  |  |  |
| --- | --- | --- |
|  | ρEQ​(−‖X‖c,∞)≤ρEQ​(X)≤ρEQ​(‖X‖c,∞)\rho\_{E}^{Q}(-\|X\|\_{c,\infty})\leq\rho\_{E}^{Q}(X)\leq\rho\_{E}^{Q}(\|X\|\_{c,\infty}) |  |

for all X∈Lc∞X\in L^{\infty}\_{c} by monotonicity, it follows that ρEQ\rho\_{E}^{Q} is indeed real-valued.

(ii) ⇔\Leftrightarrow (iii) follows from Er={X∈Lc∞∣ρ​(X)≤r}=𝒜ρ+rE\_{r}=\{X\in L^{\infty}\_{c}\mid\rho(X)\leq r\}=\mathcal{A}\_{\rho}+r and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρEQ​(0)\displaystyle\rho^{Q}\_{E}(0) | =inf{m∈ℝ∣0∈jQ​(𝒜ρ+m)}\displaystyle=\inf\{m\in\mathbb{R}\mid 0\in j\_{Q}(\mathcal{A}\_{\rho}+m)\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =inf{m∈ℝ∣−m∈jQ​(𝒜ρ)}\displaystyle=\inf\{m\in\mathbb{R}\mid-m\in j\_{Q}(\mathcal{A}\_{\rho})\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−sup{m∈ℝ∣m∈jQ​(𝒜ρ)},\displaystyle=-\sup\{m\in\mathbb{R}\mid m\in j\_{Q}(\mathcal{A}\_{\rho})\}, |  |

and ρEQ​(0)≤ρ​(0)\rho\_{E}^{Q}(0)\leq\rho(0) (see Lemma [3.3](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")).
∎

Note that if sup{m∈ℝ∣m∈jQ​(𝒜ρ)}=∞\sup\{m\in\mathbb{R}\mid m\in j\_{Q}(\mathcal{A}\_{\rho})\}=\infty, that is, ρEQ​(0)=−∞\rho^{Q}\_{E}(0)=-\infty, then, by cash-additivity and monotonicity, it follows that jQ​(𝒜ρ)=LQ∞j\_{Q}(\mathcal{A}\_{\rho})=L^{\infty}\_{Q} and ρEQ≡−∞\rho^{Q}\_{E}\equiv-\infty.

###### Remark 4.11.

Lemma [3.6](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem6 "Lemma 3.6. ‣ 3.1 Properties of 𝓟-Sensitive Functions ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") not only shows that ρEQ\rho^{Q}\_{E} is a monetary risk measure on Lc∞L^{\infty}\_{c} provided it is relevant, but also, thanks to the monotonicity established in Lemma [3.6](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem6 "Lemma 3.6. ‣ 3.1 Properties of 𝓟-Sensitive Functions ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") (i), that ρEQ∘jQ−1\rho^{Q}\_{E}\circ j\_{Q}^{-1} (recall Remark [2.11](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem11 "Remark 2.11. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) is indeed a monetary risk measure on LQ∞L^{\infty}\_{Q} which is convex or even coherent whenever ρ\rho is. ⋄\diamond

###### Lemma 4.12.

Let ρ:Lc∞→ℝ\rho\colon L^{\infty}\_{c}\to\mathbb{R} be a monetary risk measure. Then {μ∈c​ac∣ρ¯​(μ)<∞}⊆𝔓c​(Ω)\{\mu\in ca\_{c}\mid\overline{\rho}(\mu)<\infty\}\subseteq\mathfrak{P}\_{c}(\Omega) and therefore,

|  |  |  |
| --- | --- | --- |
|  | ρD​(X)=supQ∈𝔓c​(Ω)EQ​[X]−ρ¯​(Q),X∈Lc∞,\rho\_{D}(X)=\sup\_{Q\in\mathfrak{P}\_{c}(\Omega)}E\_{Q}[X]-\overline{\rho}(Q),\qquad X\in L^{\infty}\_{c}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | ρ¯​(Q)=supX∈𝒜ρEQ​[X],Q∈𝔓c​(Ω).\overline{\rho}(Q)=\sup\_{X\in\mathcal{A}\_{\rho}}E\_{Q}[X],\qquad Q\in\mathfrak{P}\_{c}(\Omega). |  |

Consequently,

|  |  |  |
| --- | --- | --- |
|  | ρDQ​(Y)=supR≪QER​[Y]−ρ¯​(R),Y∈LQ∞.\rho^{Q}\_{D}(Y)=\sup\_{R\ll Q}E\_{R}[Y]-\overline{\rho}(R),\qquad Y\in L^{\infty}\_{Q}. |  |

###### Proof.

{μ∈c​ac∣ρ¯​(μ)<∞}⊆𝔓c​(Ω)\{\mu\in ca\_{c}\mid\overline{\rho}(\mu)<\infty\}\subseteq\mathfrak{P}\_{c}(\Omega) follows from a straightforward adaptation of (parts of) the proof of [[16](https://arxiv.org/html/2601.19511v1#bib.bib26 "Stochastic finance"), Theorem 4.16].
∎

###### Lemma 4.13.

Let ρ:Lc∞→ℝ\rho\colon L^{\infty}\_{c}\to\mathbb{R} be a monetary risk measure and let Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega) be supported (recall Definition [4.3](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem3 "Definition 4.3. ‣ 4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")). Then for any X∈Lc∞X\in L^{\infty}\_{c},

|  |  |  |
| --- | --- | --- |
|  | ρEQ​(X)=limm→∞ρ​(X​𝟏S​(Q)−m​𝟏S​(Q)c).\rho^{Q}\_{E}(X)=\lim\_{m\to\infty}\rho\big(X\mathbf{1}\_{S(Q)}-m\mathbf{1}\_{S(Q)^{c}}\big). |  |

If ρ=ρD\rho=\rho\_{D}, then ρEQ\rho^{Q}\_{E} is relevant only if infρ¯​(R)<∞R​(S​(Q)c)=0\inf\_{\overline{\rho}(R)<\infty}R(S(Q)^{c})=0. Moreover, if ρ\rho is coherent and ρ=ρD\rho=\rho\_{D}, then ρEQ\rho\_{E}^{Q} is relevant if and only if infρ¯​(R)<∞R​(S​(Q)c)=0\inf\_{\overline{\rho}(R)<\infty}R(S(Q)^{c})=0.

###### Proof.

Let Xm:=X​𝟏S​(Q)−m​𝟏S​(Q)cX\_{m}:=X\mathbf{1}\_{S(Q)}-m\mathbf{1}\_{S(Q)^{c}}, m∈ℕm\in\mathbb{N}. Then jQ​(X)=jQ​(Xm)j\_{Q}(X)=j\_{Q}(X\_{m}). For any Y∈Lc∞Y\in L^{\infty}\_{c} such that jQ​(Y)=jQ​(X)j\_{Q}(Y)=j\_{Q}(X), choosing m≥∥Y∥c,∞m\geq\lVert Y\rVert\_{c,\infty}, we obtain Xm≼YX\_{m}\preccurlyeq Y. Therefore, by monotonicity, it follows that

|  |  |  |
| --- | --- | --- |
|  | ρEQ​(X)=inf{ρ​(Y)∣jQ​(Y)=jQ​(X)}=infm≥0ρ​(Xm)=limm→∞ρ​(Xm).\rho\_{E}^{Q}(X)=\inf\{\rho(Y)\mid j\_{Q}(Y)=j\_{Q}(X)\}=\inf\_{m\geq 0}\rho(X\_{m})=\lim\_{m\to\infty}\rho(X\_{m}). |  |

In particular, assuming that ρ=ρD\rho=\rho\_{D} and recalling Lemma [4.12](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem12 "Lemma 4.12. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρEQ​(0)\displaystyle\rho^{Q}\_{E}(0) | =limm→∞ρ​(−m​𝟏S​(Q)c)\displaystyle=\lim\_{m\to\infty}\rho\big(-m\mathbf{1}\_{S(Q)^{c}}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =limm→∞supρ¯​(R)<∞−m​R​(S​(Q)c)−ρ¯​(R)\displaystyle=\lim\_{m\to\infty}\sup\_{\overline{\rho}(R)<\infty}-mR\big(S(Q)^{c}\big)-\overline{\rho}(R) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ρ​(0)+limm→∞supρ¯​(R)<∞−m​R​(S​(Q)c)\displaystyle\leq\rho(0)+\lim\_{m\to\infty}\sup\_{\overline{\rho}(R)<\infty}-mR\big(S(Q)^{c}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ρ​(0)+limm→∞−(m​infρ¯​(R)<∞R​(S​(Q)c)),\displaystyle=\rho(0)+\lim\_{m\to\infty}-\Big(m\inf\_{\overline{\rho}(R)<\infty}R\big(S(Q)^{c}\big)\Big), |  |

where we used the estimate ρ¯​(R)≥ER​[0]−ρ​(0)=−ρ​(0)\overline{\rho}(R)\geq E\_{R}[0]-\rho(0)=-\rho(0). Therefore, ρEQ\rho^{Q}\_{E} is relevant only if infρ¯​(R)<∞R​(S​(Q)c)=0\inf\_{\overline{\rho}(R)<\infty}R(S(Q)^{c})=0. In case ρ\rho is coherent, the inequality above is an equality which yields the claimed sufficiency.
∎

###### Lemma 4.14.

Let ρ:Lc∞→ℝ\rho\colon L^{\infty}\_{c}\to\mathbb{R} be a monetary risk measure, and let

|  |  |  |
| --- | --- | --- |
|  | 𝒬r​e​lρ:={Q∈𝔓c​(Ω)∣ρEQ​is relevant}.\mathcal{Q}\_{rel}^{\rho}:=\{Q\in\mathfrak{P}\_{c}(\Omega)\mid\rho^{Q}\_{E}\,\mbox{is relevant}\}. |  |

If 𝒜ρ\mathcal{A}\_{\rho} is 𝒫\mathcal{P}-sensitive, then 𝒬r​e​lρ\mathcal{Q}\_{rel}^{\rho} is a reduction set for 𝒜ρ\mathcal{A}\_{\rho}, and ρ=ρE𝒬r​e​lρ\rho=\rho^{\mathcal{Q}\_{rel}^{\rho}}\_{E}. If, in addition, ρ=ρD\rho=\rho\_{D}, then ρ=ρE𝒬r​e​lρ=ρD𝒬r​e​lρ\rho=\rho^{\mathcal{Q}\_{rel}^{\rho}}\_{E}=\rho^{\mathcal{Q}\_{rel}^{\rho}}\_{D}.

###### Proof.

Let 𝒜ρ\mathcal{A}\_{\rho} be 𝒫\mathcal{P}-sensitive. Suppose that for all Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega), the risk measures ρEQ\rho^{Q}\_{E} are not relevant, and thus jQ​(𝒜ρ)=LQ∞j\_{Q}(\mathcal{A}\_{\rho})=L^{\infty}\_{Q} for all Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega). Let m∈ℝm\in\mathbb{R}. Then, trivially, m∈jQ​(𝒜ρ)m\in j\_{Q}(\mathcal{A}\_{\rho}) for all Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega). Consequently, 𝒫\mathcal{P}-sensitivity implies that m∈𝒜ρm\in\mathcal{A}\_{\rho}. Thus, −ρ​(0)=sup{m∈ℝ∣m∈𝒜ρ}=∞-\rho(0)=\sup\{m\in\mathbb{R}\mid m\in\mathcal{A}\_{\rho}\}=\infty, which is a contradiction since ρ​(0)∈ℝ\rho(0)\in\mathbb{R}. Hence, we must have that 𝒬r​e​lρ≠∅\mathcal{Q}\_{rel}^{\rho}\neq\emptyset. Moreover, by definition of 𝒫\mathcal{P}-sensitivity, we have

|  |  |  |
| --- | --- | --- |
|  | X∈𝒜ρ⇔∀Q∈𝔓c​(Ω):jQ​(X)∈jQ​(𝒜ρ).X\in\mathcal{A}\_{\rho}\qquad\Leftrightarrow\qquad\forall Q\in\mathfrak{P}\_{c}(\Omega)\colon\,j\_{Q}(X)\in j\_{Q}(\mathcal{A}\_{\rho}). |  |

Those QQ such that jQ​(𝒜ρ)=LQ∞j\_{Q}(\mathcal{A}\_{\rho})=L^{\infty}\_{Q} do not pose any constraint on the right-hand side. Therefore, if jQ​(X)∈jQ​(𝒜ρ)j\_{Q}(X)\in j\_{Q}(\mathcal{A}\_{\rho}) for all Q∈𝒬r​e​lρQ\in\mathcal{Q}\_{rel}^{\rho}, then indeed jQ​(X)∈jQ​(𝒜ρ)j\_{Q}(X)\in j\_{Q}(\mathcal{A}\_{\rho}) for all Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega), and thus X∈𝒜ρX\in\mathcal{A}\_{\rho}. Hence, 𝒬r​e​lρ\mathcal{Q}\_{rel}^{\rho} is a reduction set for 𝒜ρ\mathcal{A}\_{\rho}. Theorem [3.2](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") and Remark [4.15](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem15 "Remark 4.15. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") below imply that ρ=ρE𝒬r​e​lρ\rho=\rho^{\mathcal{Q}\_{rel}^{\rho}}\_{E}.

Suppose that ρ=ρD\rho=\rho\_{D}. Let Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega) such that ρ¯​(Q)∈ℝ\overline{\rho}(Q)\in\mathbb{R}. Then ρEQ​(0)≥ρDQ​(0)≥−ρ¯​(Q)\rho^{Q}\_{E}(0)\geq\rho^{Q}\_{D}(0)\geq-\overline{\rho}(Q) (see Lemma [4.12](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem12 "Lemma 4.12. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")). Since also ρEQ​(0)≤ρ​(0)\rho^{Q}\_{E}(0)\leq\rho(0), we obtain ρEQ​(0)∈ℝ\rho^{Q}\_{E}(0)\in\mathbb{R}, and therefore Q∈𝒬r​e​lρQ\in\mathcal{Q}\_{rel}^{\rho}. Thus, ρ=ρE𝒬r​e​lρ=ρD𝒬r​e​lρ\rho=\rho^{\mathcal{Q}\_{rel}^{\rho}}\_{E}=\rho^{\mathcal{Q}\_{rel}^{\rho}}\_{D} follows from Proposition [3.9](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem9 "Proposition 3.9. ‣ 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
∎

###### Remark 4.15.

The level sets ErE\_{r}, r∈ℝr\in\mathbb{R}, of any monetary risk measure ρ\rho satisfy Er=𝒜ρ+rE\_{r}=\mathcal{A}\_{\rho}+r. Therefore, ρ\rho is 𝒫\mathcal{P}-sensitive if and only if 𝒜ρ\mathcal{A}\_{\rho} is 𝒫\mathcal{P}-sensitive, and any reduction set for 𝒜ρ\mathcal{A}\_{\rho} is a reduction set for ρ\rho, and vice versa. ⋄\diamond

Regarding an interpretation of ρDQ\rho\_{D}^{Q}, note that measures R∈𝔓c​(Ω)R\in\mathfrak{P}\_{c}(\Omega) such that ρ¯​(R)<∞\overline{\rho}(R)<\infty correspond to acceptability constraints, since X∈𝒜ρX\in\mathcal{A}\_{\rho} if and only if ER​[X]≤ρ¯​(R)E\_{R}[X]\leq\overline{\rho}(R) for all such RR. They may also be interpreted as penalized pricing functionals. Measures RR such that also R≪QR\ll Q correspond to constraints which are understood from the QQ-perspective. Hence, the convex risk measure ρDQ​(X)\rho\_{D}^{Q}(X) is the capital requirement or indifference price of the loss XX based on acceptability constraints from the QQ-perspective.

Assume that the monetary risk measure ρ\rho satisfies ρ=ρD\rho=\rho\_{D}, i.e., it displays a reasonable degree of regularity from a dual perspective, a property that is commonly assumed. Models Q∉𝒬r​e​lρQ\not\in\mathcal{Q}\_{rel}^{\rho} are irrelevant, whereas Q∈𝒬r​e​lρQ\in\mathcal{Q}\_{rel}^{\rho} are the models that in aggregate yield ρ\rho both from a primal and a dual perspective, since ρ=ρE𝒬r​e​lρ=ρD𝒬r​e​lρ\rho=\rho^{\mathcal{Q}\_{rel}^{\rho}}\_{E}=\rho^{\mathcal{Q}\_{rel}^{\rho}}\_{D} according to Lemma [4.14](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem14 "Lemma 4.14. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"). In our discussion we will focus on Q∈𝒬r​e​lρQ\in\mathcal{Q}\_{rel}^{\rho}, even if the results derived below do not require this condition. Recall that always ρDQ≤ρEQ\rho\_{D}^{Q}\leq\rho\_{E}^{Q}. Examples [4.21](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem21 "Example 4.21. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") and [4.22](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem22 "Example 4.22. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") show that ρDQ​(X)<ρEQ​(X)\rho\_{D}^{Q}(X)<\rho\_{E}^{Q}(X) is possible. In that case, ρEQ​(X)−ρDQ​(X)\rho\_{E}^{Q}(X)-\rho\_{D}^{Q}(X) may be seen as a market inconsistency which we call a localization bubble, where the actual price under QQ exceeds what the risk assessment based on acceptability constraints under QQ would imply. In Example [4.21](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem21 "Example 4.21. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), the size of this bubble is infinite, whereas in Example [4.22](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem22 "Example 4.22. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), it is finite. In the following, we will show how such a bubble is related to purely finitely additive set functions, so-called charges, appearing in the dual representation of ρEQ\rho^{Q}\_{E}. Note that there is a line of literature that identifies bubbles as a consequence of pricing under charges (see, e.g., [[6](https://arxiv.org/html/2601.19511v1#bib.bib133 "Existence of equilibria in economies with infinitely many commodities")], [[19](https://arxiv.org/html/2601.19511v1#bib.bib134 "Charges as equilibrium prices and asset bubbles")], [[18](https://arxiv.org/html/2601.19511v1#bib.bib137 "Bubbles and charges")], [[21](https://arxiv.org/html/2601.19511v1#bib.bib136 "Asset price bubbles in incomplete markets")], and references therein).

If ρ\rho is convex and Q∈𝒬r​e​lρQ\in\mathcal{Q}\_{rel}^{\rho}, so that ρEQ\rho^{Q}\_{E} is relevant, then ρEQ∘jQ−1\rho^{Q}\_{E}\circ j\_{Q}^{-1} is a convex risk measure on LQ∞L^{\infty}\_{Q} (recall Remark [4.11](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem11 "Remark 4.11. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")). Hence, it is well-known that we obtain a dual representation of ρEQ\rho\_{E}^{Q} over the finitely additive measures

|  |  |  |
| --- | --- | --- |
|  | b​aQ1:={μ∈b​aQ∣μ​(Ω)=1​ and ​μ​(A)≥0​ for all ​A∈ℱ},ba\_{Q}^{1}:=\{\mu\in ba\_{Q}\mid\mu(\Omega)=1\text{ and }\mu(A)\geq 0\text{ for all }A\in\mathcal{F}\}, |  |

where b​aba is the real vector space of all finitely additive finite variation set functions μ:ℱ→ℝ\mu\colon\mathcal{F}\rightarrow\mathbb{R}, and

|  |  |  |
| --- | --- | --- |
|  | b​aQ:={μ∈b​a∣|μ|≪Q}.ba\_{Q}:=\{\mu\in ba\mid|\mu|\ll Q\}. |  |

The total variation of finitely additive measures is defined in the same way as for measures in ([2](https://arxiv.org/html/2601.19511v1#S2.E2 "In 2.1 Basics ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")).
In fact (see, e.g., [[16](https://arxiv.org/html/2601.19511v1#bib.bib26 "Stochastic finance"), Theorem 4.16]),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρEQ​(X)=maxμ∈b​aQ1​∫X​𝑑μ−ρQ∗​(μ),X∈Lc∞,\rho^{Q}\_{E}(X)=\max\_{\mu\in ba\_{Q}^{1}}\int Xd\mu-\rho^{\ast}\_{Q}(\mu),\ \ X\in L^{\infty}\_{c}, |  | (12) |

where the dual function ρQ∗\rho^{\ast}\_{Q} is given by

|  |  |  |
| --- | --- | --- |
|  | ρQ∗​(μ):=sup{∫Y​𝑑μ|Y∈Lc∞:ρEQ​(Y)≤0},μ∈b​aQ1.\rho^{\ast}\_{Q}(\mu):=\sup\bigg\{\int Yd\mu\biggm|Y\in L^{\infty}\_{c}\colon\rho\_{E}^{Q}(Y)\leq 0\bigg\},\qquad\mu\in ba\_{Q}^{1}. |  |

Note that in ([12](https://arxiv.org/html/2601.19511v1#S4.E12 "In 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) we used the QQ-consistency of ρEQ\rho^{Q}\_{E} to rewrite the dual representation of ρEQ∘jQ−1\rho^{Q}\_{E}\circ j\_{Q}^{-1} on LQ∞L^{\infty}\_{Q} as a representation of ρEQ\rho^{Q}\_{E} on Lc∞L^{\infty}\_{c}. Consider any R∈𝔓Q​(Ω)R\in\mathfrak{P}\_{Q}(\Omega). Then,

|  |  |  |
| --- | --- | --- |
|  | ρ¯​(R)=supY∈𝒜ρER​[Y]=supY∈Lc∞:ρEQ​(Y)≤0ER​[Y]=ρQ∗​(R),\overline{\rho}(R)=\sup\_{Y\in\mathcal{A}\_{\rho}}E\_{R}[Y]=\sup\_{Y\in L^{\infty}\_{c}\colon\rho^{Q}\_{E}(Y)\leq 0}E\_{R}[Y]=\rho^{\ast}\_{Q}(R), |  |

where for the second equality, we used that Y∈𝒜ρY\in\mathcal{A}\_{\rho} implies ρEQ​(Y)≤0\rho^{Q}\_{E}(Y)\leq 0, and, conversely,

|  |  |  |
| --- | --- | --- |
|  | ρEQ​(Y)=inf{ρ​(Z)∣jQ​(Z)=jQ​(Y)}≤0\rho^{Q}\_{E}(Y)=\inf\{\rho(Z)\mid j\_{Q}(Z)=j\_{Q}(Y)\}\leq 0 |  |

implies that there is a non-increasing sequence (mn)n∈ℕ⊆ℝ+(m\_{n})\_{n\in\mathbb{N}}\subseteq\mathbb{R}\_{+} such that limn→∞mn≤0\lim\_{n\to\infty}m\_{n}\leq 0, and a sequence (Yn)n∈ℕ⊆Lc∞(Y\_{n})\_{n\in\mathbb{N}}\subseteq L^{\infty}\_{c} with jQ​(Yn)=jQ​(Y)j\_{Q}(Y\_{n})=j\_{Q}(Y) and Yn−mn∈𝒜ρY\_{n}-m\_{n}\in\mathcal{A}\_{\rho} for all n∈ℕn\in\mathbb{N}. Note that, as R≪QR\ll Q, ER​[Yn]=ER​[Y]E\_{R}[Y\_{n}]=E\_{R}[Y].
Hence, if ρEQ​(Y)>ρDQ​(Y)\rho^{Q}\_{E}(Y)>\rho^{Q}\_{D}(Y), then there must exist ν∈b​aQ1∖𝔓Q​(Ω)\nu\in ba\_{Q}^{1}\setminus\mathfrak{P}\_{Q}(\Omega) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρEQ​(Y)=∫Y​𝑑ν−ρQ∗​(ν)>ρDQ​(Y).\rho^{Q}\_{E}(Y)=\int Yd\nu-\rho^{\*}\_{Q}(\nu)>\rho^{Q}\_{D}(Y). |  | (13) |

This establishes the aforementioned relation of localization bubbles to charges.

Before stating Examples [4.21](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem21 "Example 4.21. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") and [4.22](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem22 "Example 4.22. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), we give a number of sufficient conditions ensuring that localization bubbles do not appear. An obvious sufficient condition is that QQ be finitely atomic, that is, there are pairwise disjoint events A1,…,An∈ℱA\_{1},\ldots,A\_{n}\in\mathcal{F} such that Q​(Ai)>0Q(A\_{i})>0 for all i=1,…,ni=1,\ldots,n, ⋃i=1nAi=Ω\bigcup\_{i=1}^{n}A\_{i}=\Omega, and, for any B∈ℱB\in\mathcal{F} and any i∈{1,…,n}i\in\{1,\ldots,n\}, B⊆AiB\subseteq A\_{i} implies Q​(B)=0Q(B)=0 or Q​(B)=Q​(Ai)Q(B)=Q(A\_{i}). In that case b​aQ1=𝔓Q​(Ω)ba^{1}\_{Q}=\mathfrak{P}\_{Q}(\Omega). Hence, ([13](https://arxiv.org/html/2601.19511v1#S4.E13 "In 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) cannot hold.

###### Lemma 4.16.

Let ρ:Lc∞→ℝ\rho:L^{\infty}\_{c}\to\mathbb{R} be a convex risk measure and suppose that Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega) is finitely atomic. Then ρEQ=ρDQ\rho^{Q}\_{E}=\rho^{Q}\_{D}.

The next sufficient condition for ρEQ=ρDQ\rho^{Q}\_{E}=\rho^{Q}\_{D} is a version of the Lebesgue property discussed, e.g., in [[16](https://arxiv.org/html/2601.19511v1#bib.bib26 "Stochastic finance"), Corollary 4.35].

###### Proposition 4.17.

Let ρ:Lc∞→ℝ\rho\colon L^{\infty}\_{c}\to\mathbb{R} be a coherent risk measure. Suppose that ρ​(𝟏An)↓0\rho(\mathbf{1}\_{A\_{n}})\downarrow 0 whenever the sequence of events (An)n∈ℕ⊆ℱ(A\_{n})\_{n\in\mathbb{N}}\subseteq\mathcal{F} satisfies An↓∅A\_{n}\downarrow\emptyset. Then ρEQ=ρDQ\rho^{Q}\_{E}=\rho^{Q}\_{D} for all Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega).

###### Proof.

If Q∉𝒬r​e​lρQ\not\in\mathcal{Q}\_{rel}^{\rho}, then ρEQ≡−∞\rho^{Q}\_{E}\equiv-\infty and thus also ρDQ≡−∞\rho^{Q}\_{D}\equiv-\infty (recall ρDQ≤ρEQ\rho^{Q}\_{D}\leq\rho^{Q}\_{E}). Let Q∈𝒬r​e​lρQ\in\mathcal{Q}\_{rel}^{\rho}. Let ν∈b​aQ1∖𝔓c​(Ω)\nu\in ba^{1}\_{Q}\setminus\mathfrak{P}\_{c}(\Omega). Then there exists (An)n∈ℕ⊆ℱ(A\_{n})\_{n\in\mathbb{N}}\subseteq\mathcal{F} such that An↓∅A\_{n}\downarrow\emptyset and ε>0\varepsilon>0 such that ν​(An)>ε\nu(A\_{n})>\varepsilon for all n∈ℕn\in\mathbb{N} (see [[1](https://arxiv.org/html/2601.19511v1#bib.bib2 "Infinite dimensional analysis: a hitchhiker’s guide"), Lemma 10.9]). Note that by positive homogeneity, ρQ∗​(ν)∈{0,∞}\rho^{\ast}\_{Q}(\nu)\in\{0,\infty\} (see [[16](https://arxiv.org/html/2601.19511v1#bib.bib26 "Stochastic finance"), Corollary 4.19]).
If ρQ∗​(ν)=0\rho^{\ast}\_{Q}(\nu)=0, then

|  |  |  |
| --- | --- | --- |
|  | ρ​(𝟏An)≥ρEQ​(𝟏An)≥ν​(An)−ρQ∗​(ν)≥ε,n∈ℕ,\rho(\mathbf{1}\_{A\_{n}})\geq\rho^{Q}\_{E}(\mathbf{1}\_{A\_{n}})\geq\nu(A\_{n})-\rho^{\ast}\_{Q}(\nu)\geq\varepsilon,\qquad n\in\mathbb{N}, |  |

while ρ​(𝟏An)↓0\rho(\mathbf{1}\_{A\_{n}})\downarrow 0, which is absurd. Hence, ρQ∗​(ν)=∞\rho^{\ast}\_{Q}(\nu)=\infty for all ν∈b​aQ1∖𝔓c​(Ω)\nu\in ba^{1}\_{Q}\setminus\mathfrak{P}\_{c}(\Omega). Consequently, ([13](https://arxiv.org/html/2601.19511v1#S4.E13 "In 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) is not possible, and therefore ρEQ=ρDQ\rho^{Q}\_{E}=\rho^{Q}\_{D}.
∎

###### Proposition 4.18.

Let ρ:Lc∞→ℝ\rho:L^{\infty}\_{c}\to\mathbb{R} be a convex risk measure and let Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega). Then ρDQ=ρEQ\rho\_{D}^{Q}=\rho\_{E}^{Q} whenever jQ​(𝒜ρ)j\_{Q}(\mathcal{A}\_{\rho}) is σ​(LQ∞,c​aQ)\sigma(L^{\infty}\_{Q},ca\_{Q})-closed. In particular, if ρ=ρD\rho=\rho\_{D}, Q∈𝒬r​e​lρQ\in\mathcal{Q}\_{rel}^{\rho} is supported, and X∈𝒜ρX\in\mathcal{A}\_{\rho} implies X​𝟏S​(Q)∈𝒜ρX\mathbf{1}\_{S(Q)}\in\mathcal{A}\_{\rho}, then jQ​(𝒜ρ)j\_{Q}(\mathcal{A}\_{\rho}) is σ​(LQ∞,c​aQ)\sigma(L^{\infty}\_{Q},ca\_{Q})-closed.

###### Proof.

We may assume that Q∈𝒬r​e​lρQ\in\mathcal{Q}\_{rel}^{\rho} since otherwise ρEQ=ρDQ≡−∞\rho\_{E}^{Q}=\rho\_{D}^{Q}\equiv-\infty.
If jQ​(𝒜ρ)j\_{Q}(\mathcal{A}\_{\rho}) is σ​(LQ∞,c​aQ)\sigma(L^{\infty}\_{Q},ca\_{Q})-closed, one verifies that ρEQ∘jQ−1\rho^{Q}\_{E}\circ j^{-1}\_{Q} is σ​(LQ∞,c​aQ)\sigma(L^{\infty}\_{Q},ca\_{Q})-lower semicontinuous. Therefore, according to [[16](https://arxiv.org/html/2601.19511v1#bib.bib26 "Stochastic finance"), Theorem 4.33], ρEQ\rho\_{E}^{Q} admits a dual representation over c​aQca\_{Q} and ρDQ=ρEQ\rho\_{D}^{Q}=\rho\_{E}^{Q} by Lemma [3.8](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem8 "Lemma 3.8. ‣ 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").

Now suppose that ρ=ρD\rho=\rho\_{D}, Q∈𝒬r​e​lρQ\in\mathcal{Q}\_{rel}^{\rho} is supported, and for all X∈𝒜ρX\in\mathcal{A}\_{\rho} we have X​𝟏S​(Q)∈𝒜ρX\mathbf{1}\_{S(Q)}\in\mathcal{A}\_{\rho}. Since ρ\rho admits a dual representation over c​acca\_{c}, 𝒜ρ\mathcal{A}\_{\rho} is σ​(Lc∞,c​ac)\sigma(L^{\infty}\_{c},ca\_{c})-closed. We show that jQ​(𝒜ρ)j\_{Q}(\mathcal{A}\_{\rho}) is σ​(LQ∞,c​aQ)\sigma(L^{\infty}\_{Q},ca\_{Q})-closed. To this end, let (XαQ)α∈I⊆jQ​(𝒜ρ)(X^{Q}\_{\alpha})\_{\alpha\in I}\subseteq j\_{Q}(\mathcal{A\_{\rho}}) converge to XQ∈LQ∞X^{Q}\in L^{\infty}\_{Q} with respect to σ​(LQ∞,c​aQ)\sigma(L^{\infty}\_{Q},ca\_{Q}). Take Xα∈𝒜ρX\_{\alpha}\in\mathcal{A}\_{\rho} and X∈Lc∞X\in L^{\infty}\_{c} such that jQ​(Xα)=XαQj\_{Q}(X\_{\alpha})=X^{Q}\_{\alpha}, α∈I\alpha\in I, and jQ​(X)=XQj\_{Q}(X)=X^{Q}. Then Xα​𝟏S​(Q)∈𝒜ρX\_{\alpha}\mathbf{1}\_{S(Q)}\in\mathcal{A}\_{\rho}, jQ​(Xα​𝟏S​(Q))=XαQj\_{Q}(X\_{\alpha}\mathbf{1}\_{S(Q)})=X^{Q}\_{\alpha}, and jQ​(X​𝟏S​(Q))=XQj\_{Q}(X\mathbf{1}\_{S(Q)})=X^{Q}. For any μ∈c​ac\mu\in ca\_{c}, let μQ∈c​aQ\mu\_{Q}\in ca\_{Q} be given by μ​(A)=μ​(S​(Q)∩A)\mu(A)=\mu(S(Q)\cap A), A∈ℱA\in\mathcal{F}. Then, as XαQX^{Q}\_{\alpha} converges to XQX^{Q} in σ​(LQ∞,c​aQ)\sigma(L^{\infty}\_{Q},ca\_{Q}),

|  |  |  |
| --- | --- | --- |
|  | ∫Xα​𝟏S​(Q)​𝑑μ=∫XαQ​𝑑μQ⟶∫XQ​𝑑μQ=∫X​𝟏S​(Q)​𝑑μ.\int X\_{\alpha}\mathbf{1}\_{S(Q)}d\mu=\int X^{Q}\_{\alpha}d\mu\_{Q}\longrightarrow\int X^{Q}d\mu\_{Q}=\int X\mathbf{1}\_{S(Q)}d\mu. |  |

Since μ∈c​ac\mu\in ca\_{c} was arbitrary, we find that Xα​𝟏S​(Q)X\_{\alpha}\mathbf{1}\_{S(Q)}, α∈I\alpha\in I, converges to X​𝟏S​(Q)X\mathbf{1}\_{S(Q)} with respect to σ​(Lc∞,c​ac)\sigma(L^{\infty}\_{c},ca\_{c}). Hence, as 𝒜ρ\mathcal{A}\_{\rho} is σ​(Lc∞,c​ac)\sigma(L^{\infty}\_{c},ca\_{c})-closed, we have X​𝟏S​(Q)∈𝒜ρX\mathbf{1}\_{S(Q)}\in\mathcal{A}\_{\rho} and thus XQ∈jQ​(𝒜)X^{Q}\in j\_{Q}(\mathcal{A}). Consequently, jQ​(Aρ)j\_{Q}(A\_{\rho}) is σ​(LQ∞,c​aQ)\sigma(L^{\infty}\_{Q},ca\_{Q})-closed.
∎

###### Corollary 4.19.

Let ρ:Lc∞→ℝ\rho\colon L^{\infty}\_{c}\to\mathbb{R} be a surplus-invariant convex risk measure, that is, ρ​(X)=ρ​(X+)\rho(X)=\rho(X^{+}), and suppose that ρ=ρD\rho=\rho\_{D}. If Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega) is supported, then ρEQ=ρDQ\rho^{Q}\_{E}=\rho^{Q}\_{D}.

We refer to [[17](https://arxiv.org/html/2601.19511v1#bib.bib27 "Surplus-invariant risk measures")] for a comprehensive discussion of surplus invariant risk measures.

###### Proof.

As before we may assume that Q∈𝒬r​e​lρQ\in\mathcal{Q}^{\rho}\_{rel}, because otherwise ρEQ=ρDQ≡−∞\rho^{Q}\_{E}=\rho^{Q}\_{D}\equiv-\infty. Note that X∈𝒜ρX\in\mathcal{A}\_{\rho} if and only if X+∈𝒜ρX^{+}\in\mathcal{A}\_{\rho}. As X+​𝟏S​(Q)≼X+X^{+}\mathbf{1}\_{S(Q)}\preccurlyeq X^{+}, it follows that

|  |  |  |
| --- | --- | --- |
|  | ρ​(X​𝟏S​(Q))=ρ​(X+​𝟏S​(Q))≤ρ​(X+)=ρ​(X),\rho(X\mathbf{1}\_{S(Q)})=\rho(X^{+}\mathbf{1}\_{S(Q)})\leq\rho(X^{+})=\rho(X), |  |

and therefore X​𝟏S​(Q)∈𝒜ρX\mathbf{1}\_{S(Q)}\in\mathcal{A}\_{\rho} whenever X∈𝒜ρX\in\mathcal{A}\_{\rho}. Now apply Proposition [4.18](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem18 "Proposition 4.18. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
∎

###### Lemma 4.20.

Let ρ:Lc∞→ℝ\rho\colon L^{\infty}\_{c}\to\mathbb{R} be a coherent risk measure which admits a representation over finitely many 𝔓c​(Ω)\mathfrak{P}\_{c}(\Omega)-constraints, that is,

|  |  |  |
| --- | --- | --- |
|  | ρ​(X)=maxR∈𝒬⁡ER​[X],X∈Lc∞,\rho(X)=\max\_{R\in\mathcal{Q}}E\_{R}[X],\qquad X\in L^{\infty}\_{c}, |  |

where 𝒬⊆𝔓c​(Ω)\mathcal{Q}\subseteq\mathfrak{P}\_{c}(\Omega) is finite. Then ρEQ=ρDQ\rho^{Q}\_{E}=\rho^{Q}\_{D} for all supported Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega).

###### Proof.

Let Q∈𝒬r​e​lρQ\in\mathcal{Q}\_{rel}^{\rho} be supported. One verifies that ρ¯​(R)<∞\overline{\rho}(R)<\infty if and only if RR lies in the convex hull of 𝒬\mathcal{Q}. According to Lemma [4.13](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem13 "Lemma 4.13. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),

|  |  |  |
| --- | --- | --- |
|  | infR∈co⁡𝒬R​(S​(Q)c)=minR∈𝒬⁡R​(S​(Q)c)=0.\inf\_{R\in\operatorname{co}\mathcal{Q}}R(S(Q)^{c})=\min\_{R\in\mathcal{Q}}R(S(Q)^{c})=0. |  |

Hence, there is R′∈𝒬R^{\prime}\in\mathcal{Q} such that R′≪QR^{\prime}\ll Q. Suppose there is R∈𝒬R\in\mathcal{Q} such that R​(S​(Q)c)>0R(S(Q)^{c})>0. For any X∈Lc∞X\in L^{\infty}\_{c} and Xm:=X​𝟏S​(Q)−m​𝟏S​(Q)cX\_{m}:=X\mathbf{1}\_{S(Q)}-m\mathbf{1}\_{S(Q)^{c}}, m∈ℕm\in\mathbb{N}, we have

|  |  |  |
| --- | --- | --- |
|  | ER​[Xm]=ER​[X​𝟏S​(Q)]−m​R​(S​(Q)c)≤ER′​[X]E\_{R}[X\_{m}]=E\_{R}[X\mathbf{1}\_{S(Q)}]-mR(S(Q)^{c})\leq E\_{R^{\prime}}[X] |  |

whenever

|  |  |  |
| --- | --- | --- |
|  | m≥ER​[X​𝟏S​(Q)]−ER′​[X]R​(S​(Q)c).m\geq\frac{E\_{R}[X\mathbf{1}\_{S(Q)}]-E\_{R^{\prime}}[X]}{R(S(Q)^{c})}. |  |

Consequently, as 𝒬\mathcal{Q} is finite and as ER​[Xm]=ER​[X]E\_{R}[X\_{m}]=E\_{R}[X] for all R≪QR\ll Q, for mm large enough we obtain

|  |  |  |
| --- | --- | --- |
|  | ρ​(Xm)=maxR∈𝒬⁡ER​[Xm]=maxR∈𝒬,R≪Q⁡ER​[X],\rho(X\_{m})=\max\_{R\in\mathcal{Q}}E\_{R}[X\_{m}]=\max\_{R\in\mathcal{Q},R\ll Q}E\_{R}[X], |  |

and thus, by another application of Lemma [4.13](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem13 "Lemma 4.13. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),

|  |  |  |
| --- | --- | --- |
|  | ρEQ​(X)=limm→∞ρ​(Xm)=maxR∈𝒬,R≪Q⁡ER​[X]=ρDQ​(X).\rho^{Q}\_{E}(X)=\lim\_{m\to\infty}\rho(X\_{m})=\max\_{R\in\mathcal{Q},R\ll Q}E\_{R}[X]=\rho^{Q}\_{D}(X). |  |

∎

Examples [4.21](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem21 "Example 4.21. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") and [4.22](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem22 "Example 4.22. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") show that ρEQ​(Y)−ρDQ​(Y)>0\rho\_{E}^{Q}(Y)-\rho\_{D}^{Q}(Y)>0 may happen even in a dominated framework.

###### Example 4.21.

Let (Ω,ℱ)=((0,1),ℬ​(0,1))(\Omega,\mathcal{F})=((0,1),\mathcal{B}(0,1)) and 𝒫={λ}\mathcal{P}=\{\lambda\}, where λ\lambda denotes the Lebesgue measure on (Ω,ℱ)(\Omega,\mathcal{F}). Set An:=(0,1n+1)A\_{n}:=(0,\frac{1}{n+1}) and B:=[12,1)B:=[\frac{1}{2},1), and define probability measures PnP\_{n} on (Ω,ℱ)(\Omega,\mathcal{F}) by

|  |  |  |
| --- | --- | --- |
|  | Pn(⋅):=n−1nλ(⋅∣An)+1nλ(⋅∣B),n∈ℕ.P\_{n}(\,\cdot\,):=\frac{n-1}{n}\lambda(\,\cdot\mid A\_{n})+\frac{1}{n}\lambda(\,\cdot\mid B),\qquad n\in\mathbb{N}. |  |

Consider the coherent risk measure

|  |  |  |
| --- | --- | --- |
|  | ρ​(X):=supn∈ℕEPn​[X],X∈Lλ∞.\rho(X):=\sup\_{n\in\mathbb{N}}E\_{P\_{n}}[X],\qquad X\in L^{\infty}\_{\lambda}. |  |

Note that Lemma [4.20](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem20 "Lemma 4.20. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") does not apply, since ρ\rho is given by infinitely many constraints. As ρ\rho admits a dual representation over c​aλca\_{\lambda} by definition, it follows from Theorem [3.10](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem10 "Theorem 3.10. ‣ 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") that

|  |  |  |
| --- | --- | --- |
|  | ρ=ρD=ρE.\rho=\rho\_{D}=\rho\_{E}. |  |

However, as we will see in the following, there exists Q∈𝔓λ​(Ω)Q\in\mathfrak{P}\_{\lambda}(\Omega) such that ρDQ≠ρEQ\rho^{Q}\_{D}\neq\rho^{Q}\_{E}.

Set Y:=[y]λY:=[y]\_{\lambda}, where

|  |  |  |
| --- | --- | --- |
|  | y​(ω):={−1,if ​ω∈B,2​ω,otherwise.y(\omega):=\begin{cases}-1,&\text{if }\omega\in B,\\ 2\omega,&\text{otherwise.}\end{cases} |  |

Then Y∈Lλ∞Y\in L^{\infty}\_{\lambda} and

|  |  |  |
| --- | --- | --- |
|  | EPn​[Y]=((n−1)​(n+1)n​∫01n+12​ω​𝑑ω−1n)=−2(n+1)​n≤0.E\_{P\_{n}}[Y]=\bigg(\frac{(n-1)(n+1)}{n}\int\_{0}^{\frac{1}{n+1}}2\omega\,d\omega-\frac{1}{n}\bigg)=-\frac{2}{(n+1)n}\leq 0. |  |

Hence, ρ​(Y)=0\rho(Y)=0 and Y∈𝒜ρY\in\mathcal{A}\_{\rho}. Consider any probability measure R∈𝔓λ​(Ω)R\in\mathfrak{P}\_{\lambda}(\Omega) such that R​(B)=0R(B)=0. As R​(Y>0)=1R(Y>0)=1, it follows that ER​[Y]>0E\_{R}[Y]>0. Consequently, recalling that t​Y∈𝒜ρtY\in\mathcal{A}\_{\rho} for all t>0t>0 by positive homogeneity, we have

|  |  |  |
| --- | --- | --- |
|  | ρ¯​(R)=supX∈𝒜ρER​[X]≥supt>0ER​[t​Y]=∞.\overline{\rho}(R)=\sup\_{X\in\mathcal{A}\_{\rho}}E\_{R}[X]\geq\sup\_{t>0}E\_{R}[tY]=\infty. |  |

Consider the supported probability measure Q=λ(⋅∣(0,12))Q=\lambda(\,\cdot\mid(0,\frac{1}{2})). Indeed S​(Q)=(0,12)=BcS(Q)=(0,\frac{1}{2})=B^{c}. Any R≪QR\ll Q has to satisfy R​(B)=R​(S​(Q)c)=0R(B)=R(S(Q)^{c})=0 and therefore ρ¯​(R)=∞\overline{\rho}(R)=\infty. It follows that ρDQ≡−∞\rho^{Q}\_{D}\equiv-\infty.

As regards ρEQ\rho^{Q}\_{E}, we have

|  |  |  |
| --- | --- | --- |
|  | infρ¯​(R)<∞R​(S​(Q)c)=infρ¯​(R)<∞R​(B)≤infn∈ℕPn​(B)=infn∈ℕ1n=0.\inf\_{\overline{\rho}(R)<\infty}R\big(S(Q)^{c}\big)=\inf\_{\overline{\rho}(R)<\infty}R(B)\leq\inf\_{n\in\mathbb{N}}P\_{n}(B)=\inf\_{n\in\mathbb{N}}\frac{1}{n}=0. |  |

Hence, by Lemma [4.13](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem13 "Lemma 4.13. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") ρEQ\rho^{Q}\_{E} is a coherent risk measure. Consequently, ρEQ​(X)>ρDQ​(X)\rho^{Q}\_{E}(X)>\rho^{Q}\_{D}(X) for all X∈Lc∞X\in L^{\infty}\_{c} and the size of the localization bubble is infinite. ⋄\diamond

###### Example 4.22.

Recall Example [4.21](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem21 "Example 4.21. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"). This time define

|  |  |  |
| --- | --- | --- |
|  | κ​(X):=ρ​(X)∨EQ​[X],X∈Lλ∞,\kappa(X):=\rho(X)\vee E\_{Q}[X],\qquad X\in L^{\infty}\_{\lambda}, |  |

which is another coherent risk measure. Suppose that R≪QR\ll Q but R≠QR\neq Q. Pick a version φ\varphi of the density d​Rd​Q\frac{dR}{dQ} such that φ​χ[12,1)=0\varphi\chi\_{[\frac{1}{2},1)}=0. As R≠QR\neq Q, we must have Q​(φ>1)>0Q(\varphi>1)>0 and Q​(φ<1)>0Q(\varphi<1)>0. Moreover, An↓∅A\_{n}\downarrow\emptyset and thus

|  |  |  |
| --- | --- | --- |
|  | limn→∞Q​({φ>1}∩An)=0​and​limn→∞Q​({φ<1}∩An)=0.\lim\_{n\to\infty}Q(\{\varphi>1\}\cap A\_{n})=0\qquad\text{and}\qquad\lim\_{n\to\infty}Q(\{\varphi<1\}\cap A\_{n})=0. |  |

Choose mm large enough such that

|  |  |  |
| --- | --- | --- |
|  | Q​({φ>1}∩Am)<Q​({φ>1})​and​Q​({φ<1}∩Am)<Q​({φ<1}).Q(\{\varphi>1\}\cap A\_{m})<Q(\{\varphi>1\})\qquad\text{and}\qquad Q(\{\varphi<1\}\cap A\_{m})<Q(\{\varphi<1\}). |  |

Then there is

|  |  |  |
| --- | --- | --- |
|  | D⊆{φ>1}∖Am​and​D′⊆({φ<1}∖Am)∩(0,12)D\subseteq\{\varphi>1\}\setminus A\_{m}\qquad\text{and}\qquad D^{\prime}\subseteq(\{\varphi<1\}\setminus A\_{m})\cap(0,\tfrac{1}{2}) |  |

such that Q​(D)=Q​(D′)>0Q(D)=Q(D^{\prime})>0. Note that λ​(D∣An)=λ​(D′∣An)=0\lambda(D\mid A\_{n})=\lambda(D^{\prime}\mid A\_{n})=0 for all n≥mn\geq m. Consider Z:=[z]λZ:=[z]\_{\lambda}, where

|  |  |  |
| --- | --- | --- |
|  | z:=χD−χD′−m​χB.z:=\chi\_{D}-\chi\_{D^{\prime}}-m\chi\_{B}. |  |

Then, EQ​[Z]=0E\_{Q}[Z]=0 and EPn​[Z]=−mn≤0E\_{P\_{n}}[Z]=-\frac{m}{n}\leq 0 for n≥mn\geq m. For n<mn<m, we have

|  |  |  |
| --- | --- | --- |
|  | EPn​[Z]≤(n−1)​(n+1)n​∫01n+11​𝑑ω−mn=n−1−mn≤0.E\_{P\_{n}}[Z]\leq\frac{(n-1)(n+1)}{n}\int\_{0}^{\frac{1}{n+1}}1\,d\omega-\frac{m}{n}=\frac{n-1-m}{n}\leq 0. |  |

Therefore, Z∈𝒜κZ\in\mathcal{A}\_{\kappa}. However,

|  |  |  |
| --- | --- | --- |
|  | ER​[Z]=EQ​[φ​Z]>Q​(D)−Q​(D′)=0E\_{R}[Z]=E\_{Q}[\varphi Z]>Q(D)-Q(D^{\prime})=0 |  |

which implies that κ¯​(R)≥supt>0ER​[t​Z]=∞\overline{\kappa}(R)\geq\sup\_{t>0}E\_{R}[tZ]=\infty. Clearly, κ¯​(Q)=0\overline{\kappa}(Q)=0, and therefore κDQ​(⋅)=EQ​[⋅]\kappa^{Q}\_{D}(\,\cdot\,)=E\_{Q}[\,\cdot\,].

Regarding κEQ\kappa^{Q}\_{E}, as in Example [4.21](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem21 "Example 4.21. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), we conclude that infκ¯​(R)<∞R​(S​(Q)c)=0\inf\_{\overline{\kappa}(R)<\infty}R\big(S(Q)^{c}\big)=0, which implies that κEQ\kappa^{Q}\_{E} is a coherent risk measure (see Lemma [4.13](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem13 "Lemma 4.13. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")). Hence, both κDQ\kappa^{Q}\_{D} and κEQ\kappa^{Q}\_{E} are coherent risk measures. Consider W:=[−y]λW:=[-y]\_{\lambda}, where yy was given in Example [4.21](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem21 "Example 4.21. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"). Then κDQ​(W)=EQ​[W]<0\kappa^{Q}\_{D}(W)=E\_{Q}[W]<0. For any m∈ℕm\in\mathbb{N},

|  |  |  |
| --- | --- | --- |
|  | EPn​[W​𝟏(0,12)−m​𝟏B]=−(n−1)n​(n+1)−mn≤0,E\_{P\_{n}}[W\mathbf{1}\_{(0,\frac{1}{2})}-m\mathbf{1}\_{B}]=-\frac{(n-1)}{n(n+1)}-\frac{m}{n}\leq 0, |  |

and thus, as EQ​[W​𝟏(0,12)−m​𝟏B]=EQ​[W]<0E\_{Q}[W\mathbf{1}\_{(0,\frac{1}{2})}-m\mathbf{1}\_{B}]=E\_{Q}[W]<0,

|  |  |  |
| --- | --- | --- |
|  | κ​(W​𝟏(0,12)−m​𝟏B)=supn∈ℕ(−(n−1)n​(n+1)−mn)=0.\kappa(W\mathbf{1}\_{(0,\frac{1}{2})}-m\mathbf{1}\_{B})=\sup\_{n\in\mathbb{N}}\bigg(-\frac{(n-1)}{n(n+1)}-\frac{m}{n}\bigg)=0. |  |

By applying Lemma [4.13](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem13 "Lemma 4.13. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), we therefore have that

|  |  |  |
| --- | --- | --- |
|  | κEQ​(W)=limm→∞κ​(W​𝟏(0,12)−m​𝟏B)=0.\kappa^{Q}\_{E}(W)=\lim\_{m\to\infty}\kappa(W\mathbf{1}\_{(0,\frac{1}{2})}-m\mathbf{1}\_{B})=0. |  |

Hence, there is a finite localization bubble κEQ​(W)−κDQ​(W)>0\kappa^{Q}\_{E}(W)-\kappa^{Q}\_{D}(W)>0. ⋄\diamond

### 4.3 Arbitrage and Superhedging in One Period

Again, we let 𝒳=Lc∞\mathcal{X}=L^{\infty}\_{c} with c​ac​(𝒳)=c​acca\_{c}(\mathcal{X})=ca\_{c}. A one-period market model of dimension d∈ℕd\in\mathbb{N} is given by a (discounted) stock price process S=(S0,S1)∈𝒮S=(S\_{0},S\_{1})\in\mathcal{S}, where S0∈ℝdS\_{0}\in\mathbb{R}^{d} and S1S\_{1} is a bounded dd-dimensional random vector. All coordinates StiS^{i}\_{t}, i=1,…,di=1,\ldots,d, of StS\_{t}, t=0,1t=0,1, are assumed to be non-negative and (S0i,S1i)(S^{i}\_{0},S^{i}\_{1}) will be called the ii-th asset of SS, i=1,…,di=1,\ldots,d. The space of all such market models is denoted by

|  |  |  |
| --- | --- | --- |
|  | 𝒮:={S=(S0,S1)∣S​ is a one-period market model of dimension ​d,d∈ℕ}.\mathcal{S}:=\{S=(S\_{0},S\_{1})\mid S\text{ is a one-period market model of dimension }d,\ d\in\mathbb{N}\}. |  |

Let d​(S)d(S) denote the dimension of S∈𝒮S\in\mathcal{S}, and we write S⊲S′S\lhd S^{\prime} to indicate that S∈𝒮S\in\mathcal{S} is a submarket of S′∈𝒮S^{\prime}\in\mathcal{S}, that is, for all i∈{1,…,d​(S)}i\in\{1,\ldots,d(S)\} there is j∈{1,…,d​(S′)}j\in\{1,\ldots,d(S^{\prime})\} such that (S0i,S1i)=(S0j,S1j)(S\_{0}^{i},S\_{1}^{i})=(S\_{0}^{j},S\_{1}^{j}). Moreover, for S=(S0,S1)∈𝒮S=(S\_{0},S\_{1})\in\mathcal{S}, let

|  |  |  |
| --- | --- | --- |
|  | Δ​S:=(Δ​S1,…​Δ​Sd​(S)):=S1−S0=(S11−S01,…,S1d​(S)−S0d​(S))\Delta S:=(\Delta S^{1},\ldots\Delta S^{d(S)}):=S\_{1}-S\_{0}=(S^{1}\_{1}-S^{1}\_{0},\ldots,S^{d(S)}\_{1}-S^{d(S)}\_{0}) |  |

and recall that a probability measure Q∈𝔓​(Ω)Q\in\mathfrak{P}(\Omega) is called a martingale measure for the market model SS if, for each i=1,…,d​(S)i=1,\ldots,d(S), S1iS^{i}\_{1} is QQ-integrable and

|  |  |  |
| --- | --- | --- |
|  | EQ​[Δ​S]:=(EQ​[Δ​S1],…,EQ​[Δ​Sd​(S)])=0.E\_{Q}[\Delta S]:=(E\_{Q}[\Delta S^{1}],\ldots,E\_{Q}[\Delta S^{d(S)}])=0. |  |

The space of (investment) strategies for a given dd-dimensional market S∈𝒮S\in\mathcal{S} is given by ℋ​(S):=ℝd\mathcal{H}(S):=\mathbb{R}^{d}.

In the following, for Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega), we write Q⋘𝒫Q\lll\mathcal{P} if there exists P∈𝒫P\in\mathcal{P} such that Q≪PQ\ll P. We will consider the following set-valued maps:

* •

  𝔐:𝒮↠𝒫c​(Ω)\mathfrak{M}\colon\mathcal{S}\twoheadrightarrow\mathcal{P}\_{c}(\Omega) defined by

  |  |  |  |
  | --- | --- | --- |
  |  | 𝔐​(S):={Q∈𝔓c​(Ω)∣Q​is a martingale measure for​S},\mathfrak{M}(S):=\{Q\in\mathfrak{P}\_{c}(\Omega)\mid Q\,\mbox{is a martingale measure for}\,S\}, |  |
* •

  𝔑​𝔄:𝒮↠𝔓c​(Ω)\mathfrak{NA}\colon\mathcal{S}\twoheadrightarrow\mathfrak{P}\_{c}(\Omega) defined by

  |  |  |  |
  | --- | --- | --- |
  |  | 𝔑​𝔄​(S):={R∈𝔓c​(Ω)∣∃Q∈𝔐​(S):R≈Q},\mathfrak{NA}(S):=\{R\in\mathfrak{P}\_{c}(\Omega)\mid\exists Q\in\mathfrak{M}(S)\colon R\approx Q\}, |  |
* •

  𝔐≪:𝒮↠𝔓c​(Ω)\mathfrak{M}\_{\ll}\colon\mathcal{S}\twoheadrightarrow\mathfrak{P}\_{c}(\Omega) defined by

  |  |  |  |
  | --- | --- | --- |
  |  | 𝔐≪​(S):={Q∈𝔓c​(Ω)∣Q∈𝔐​(S)​ and ​Q⋘𝒫},\mathfrak{M}\_{\ll}(S):=\{Q\in\mathfrak{P}\_{c}(\Omega)\mid Q\in\mathfrak{M}(S)\text{ and }Q\lll\mathcal{P}\}, |  |
* •

  𝔐≈:𝒮↠𝔓c​(Ω)\mathfrak{M}\_{\approx}\colon\mathcal{S}\twoheadrightarrow\mathfrak{P}\_{c}(\Omega) defined by

  |  |  |  |
  | --- | --- | --- |
  |  | 𝔐≈​(S):={Q∈𝔓c​(Ω)∣Q∈𝔐​(S)​ and ​∃P∈𝒫:Q≈P},\mathfrak{M}\_{\approx}(S):=\{Q\in\mathfrak{P}\_{c}(\Omega)\mid Q\in\mathfrak{M}(S)\text{ and }\exists P\in\mathcal{P}\colon Q\approx P\}, |  |
* •

  𝔐≈Q:𝒮↠𝔓c​(Ω)\mathfrak{M}^{Q}\_{\approx}\colon\mathcal{S}\twoheadrightarrow\mathfrak{P}\_{c}(\Omega), where Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega), defined by

  |  |  |  |
  | --- | --- | --- |
  |  | 𝔐≈Q​(S):={R∈𝔓c​(Ω)∣R∈𝔐​(S)​ and ​R≈Q}.\mathfrak{M}^{Q}\_{\approx}(S):=\{R\in\mathfrak{P}\_{c}(\Omega)\mid R\in\mathfrak{M}(S)\text{ and }R\approx Q\}. |  |

Clearly, 𝔐≈​(S)⊆𝔐≪​(S)⊆𝔐​(S)⊆𝔑​𝔄​(S)\mathfrak{M}\_{\approx}(S)\subseteq\mathfrak{M}\_{\ll}(S)\subseteq\mathfrak{M}(S)\subseteq\mathfrak{NA}(S) for any S∈𝒮S\in\mathcal{S}. Following the standard approach to no-arbitrage in robust models (see, e.g., [[9](https://arxiv.org/html/2601.19511v1#bib.bib13 "Arbitrage and duality in nondominated discrete-time models"), Definition 1.1]), we say that the no-arbitrage condition NA(𝒫,S\mathcal{P},S) holds for the market S∈𝒮S\in\mathcal{S} if, for all H∈ℋ​(S)H\in\mathcal{H}(S),

|  |  |  |
| --- | --- | --- |
|  | H​Δ​S≥0​𝒫​-q.s.​implies​H​Δ​S=0​𝒫​-q.s.H\Delta S\geq 0\ \mathcal{P}\text{-q.s.}\qquad\text{implies}\qquad H\Delta S=0\ \mathcal{P}\text{-q.s.} |  |

Note that H​Δ​SH\Delta S is the usual (ω\omega-wise) Eulidean scalar product of the vectors HH and Δ​S\Delta S.
Similarly, for any Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega), S∈𝒮S\in\mathcal{S} satisfies NA(Q,SQ,S) if, for all H∈ℋ​(S)H\in\mathcal{H}(S),

|  |  |  |
| --- | --- | --- |
|  | H​Δ​S≥0​Q​-a.s.​implies​H​Δ​S=0​Q​-a.s.H\Delta S\geq 0\ Q\text{-a.s.}\qquad\text{implies}\qquad H\Delta S=0\ Q\text{-a.s.} |  |

For any given S∈𝒮S\in\mathcal{S}, we define the 𝒫\mathcal{P}-superhedging functional π(⋅∣S):Lc∞→ℝ∪{−∞}\pi(\,\cdot\mid S)\colon L^{\infty}\_{c}\to\mathbb{R}\cup\{-\infty\} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(X∣S):=inf{r∈ℝ∣∃H∈ℋ​(S):X≼r+[H​Δ​S]c}.\pi(X\mid S):=\inf\{r\in\mathbb{R}\mid\exists H\in\mathcal{H}(S)\colon X\preccurlyeq r+[H\Delta S]\_{c}\}. |  | (14) |

Considering the strategy H=0H=0, we see that π(⋅∣S)\pi(\,\cdot\mid S) indeed takes values in ℝ∪{−∞}\mathbb{R}\cup\{-\infty\} since π​(X∣S)≤‖X‖c,∞\pi(X\mid S)\leq\|X\|\_{c,\infty} for all X∈Lc∞X\in L^{\infty}\_{c}. Finally, for Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega),

|  |  |  |
| --- | --- | --- |
|  | πQ​(X∣S):=inf{r∈ℝ∣∃H∈ℋ​(S):X≤Qr+[H​Δ​S]c},X∈Lc∞,\pi^{Q}(X\mid S):=\inf\{r\in\mathbb{R}\mid\exists H\in\mathcal{H}(S)\colon X\leq\_{Q}r+[H\Delta S]\_{c}\},\qquad X\in L^{\infty}\_{c}, |  |

is the QQ-superhedging functional for a given S∈𝒮S\in\mathcal{S}. Note that both π(⋅∣S)\pi(\,\cdot\mid S) and πQ(⋅∣S)\pi^{Q}(\,\cdot\mid S) are coherent risk measures on Lc∞L^{\infty}\_{c}, provided they are ℝ\mathbb{R}-valued, which is equivalent to π​(0∣S)=0\pi(0\mid S)=0 and πQ​(0∣S)=0\pi^{Q}(0\mid S)=0, respectively (by the same reasoning as in the proof of Lemma [4.10](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem10 "Lemma 4.10. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")).

###### Lemma 4.23.

Let S∈𝒮S\in\mathcal{S}. Then

|  |  |  |
| --- | --- | --- |
|  | {R∈𝔓c​(Ω)∣π¯​(R∣S)<∞}={R∈𝔓c​(Ω)∣π¯​(R∣S)=0}=𝔐​(S).\{R\in\mathfrak{P}\_{c}(\Omega)\mid\overline{\pi}(R\mid S)<\infty\}=\{R\in\mathfrak{P}\_{c}(\Omega)\mid\overline{\pi}(R\mid S)=0\}=\mathfrak{M}(S). |  |

###### Proof.

We may assume that π​(0∣S)=0\pi(0\mid S)=0, so that π(⋅∣S)\pi(\,\cdot\mid S) is a coherent risk measure on Lc∞L^{\infty}\_{c}, because otherwise, π(⋅∣S)≡−∞\pi(\,\cdot\mid S)\equiv-\infty and thus π¯(⋅∣S)≡∞\overline{\pi}(\,\cdot\mid S)\equiv\infty. The first equality is a well-known consequence of coherence of π(⋅∣S)\pi(\,\cdot\mid S) (see [[16](https://arxiv.org/html/2601.19511v1#bib.bib26 "Stochastic finance"), Corollary 4.19]). Let R∈𝔐​(S)R\in\mathfrak{M}(S). Then, by ([14](https://arxiv.org/html/2601.19511v1#S4.E14 "In 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")), ER​[X]≤π​(X∣S)E\_{R}[X]\leq\pi(X\mid S) for all X∈Lc∞X\in L^{\infty}\_{c}. Lemma [4.12](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem12 "Lemma 4.12. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") implies 𝔐​(S)⊆{R∈𝔓c​(Ω)∣π¯​(R∣S)=0}\mathfrak{M}(S)\subseteq\{R\in\mathfrak{P}\_{c}(\Omega)\mid\overline{\pi}(R\mid S)=0\}.

Conversely, let R∈𝔓c​(Ω)R\in\mathfrak{P}\_{c}(\Omega) satisfy π¯​(R∣S)=0\overline{\pi}(R\mid S)=0, that is, ER​[X]≤0E\_{R}[X]\leq 0 for all X∈Lc∞X\in L^{\infty}\_{c} such that π​(X∣S)≤0\pi(X\mid S)\leq 0 (see Lemma [4.12](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem12 "Lemma 4.12. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")). Since both π​([Δ​Si]c∣S)≤0\pi([\Delta S^{i}]\_{c}\mid S)\leq 0 and π​(−[Δ​Si]c∣S)≤0\pi(-[\Delta S^{i}]\_{c}\mid S)\leq 0 for all i=1,…,d​(S)i=1,\ldots,d(S), we conclude that R∈𝔐​(S)R\in\mathfrak{M}(S).
∎

###### Proposition 4.24.

Let S∈𝒮S\in\mathcal{S} and Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega). Then

|  |  |  |
| --- | --- | --- |
|  | πDQ(⋅∣S)≤πQ(⋅∣S)≤πEQ(⋅∣S)≤π(⋅∣S).\pi^{Q}\_{D}(\,\cdot\mid S)\leq\pi^{Q}(\,\cdot\mid S)\leq\pi^{Q}\_{E}(\,\cdot\mid S)\leq\pi(\,\cdot\mid S). |  |

If NA⁡(Q,S)\operatorname{NA}(Q,S) holds, then πDQ(⋅∣S)=πQ(⋅∣S)\pi^{Q}\_{D}(\,\cdot\mid S)=\pi^{Q}(\,\cdot\mid S). If QQ is supported, we have πQ(⋅∣S)=πEQ(⋅∣S)\pi^{Q}(\,\cdot\mid S)=\pi^{Q}\_{E}(\,\cdot\mid S).

###### Proof.

If X≼r+[H​Δ​S]cX\preccurlyeq r+[H\Delta S]\_{c}, then X≤Qr+[H​Δ​S]cX\leq\_{Q}r+[H\Delta S]\_{c}. Therefore, πQ​(X∣S)≤π​(X∣S)\pi^{Q}(X\mid S)\leq\pi(X\mid S). Thus, as πQ(⋅∣S)\pi^{Q}(\,\cdot\mid S) is QQ-consistent, πQ(⋅∣S)≤πEQ(⋅∣S)≤π(⋅∣S)\pi^{Q}(\,\cdot\mid S)\leq\pi^{Q}\_{E}(\,\cdot\mid S)\leq\pi(\,\cdot\mid S) follows from Lemma [3.3](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"). Recall Lemma [4.23](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem23 "Lemma 4.23. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"). Let R≪QR\ll Q such that π¯​(R∣S)=0\overline{\pi}(R\mid S)=0. Then, for each X∈Lc∞X\in L^{\infty}\_{c}, H∈ℋ​(S)H\in\mathcal{H}(S), and r∈ℝr\in\mathbb{R} such that X≤Qr+[H​Δ​S]cX\leq\_{Q}r+[H\Delta S]\_{c}, we have ER​[X]≤rE\_{R}[X]\leq r, because R∈𝔐​(S)R\in\mathfrak{M}(S). Therefore, πQ(⋅∣S)≥πDQ(⋅∣S)\pi^{Q}(\,\cdot\mid S)\geq\pi^{Q}\_{D}(\,\cdot\mid S).

For any Q∈𝔓c​(Ω)Q\in\mathfrak{P}\_{c}(\Omega) such that NA⁡(Q,S)\operatorname{NA}(Q,S) holds, the superhedging duality for dominated models (see [[16](https://arxiv.org/html/2601.19511v1#bib.bib26 "Stochastic finance"), Theorem 1.32]) and Lemma [3.8](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem8 "Lemma 3.8. ‣ 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") imply that πQ(⋅∣S)≤πDQ(⋅∣S)\pi^{Q}(\,\cdot\mid S)\leq\pi^{Q}\_{D}(\,\cdot\mid S), because πQ(⋅∣S)\pi^{Q}(\,\cdot\mid S) admits a dual representation over c​aQca\_{Q}.

Suppose that QQ is supported and let X≤Qr+[H​Δ​S]cX\leq\_{Q}r+[H\Delta S]\_{c}. Define

|  |  |  |
| --- | --- | --- |
|  | Y:=X​𝟏S​(Q)+(r+[H​Δ​S]c)​𝟏S​(Q)c.Y:=X\mathbf{1}\_{S(Q)}+(r+[H\Delta S]\_{c})\mathbf{1}\_{S(Q)^{c}}. |  |

Then jQ​(Y)=jQ​(X)j\_{Q}(Y)=j\_{Q}(X) and Y≼r+[H​Δ​S]cY\preccurlyeq r+[H\Delta S]\_{c}. Therefore, πEQ​(X∣S)≤π​(Y∣S)≤r\pi\_{E}^{Q}(X\mid S)\leq\pi(Y\mid S)\leq r, and hence πEQ​(X∣S)≤πQ​(X∣S)\pi\_{E}^{Q}(X\mid S)\leq\pi^{Q}(X\mid S).
∎

In view of the discussion in Section [4.2](https://arxiv.org/html/2601.19511v1#S4.SS2 "4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), a natural question is whether the superhedging functionals admit localization bubbles. The answer is no, at least if QQ is supported and NA⁡(Q,S)\operatorname{NA}(Q,S) is satisfied, because then Proposition [4.24](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem24 "Proposition 4.24. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") shows that πDQ(⋅∣S)=πQ(⋅∣S)=πEQ(⋅∣S)\pi^{Q}\_{D}(\,\cdot\mid S)=\pi^{Q}(\,\cdot\mid S)=\pi^{Q}\_{E}(\,\cdot\mid S).

The following lemma is a key observation for the results that follow.

###### Lemma 4.25.

For any market model S∈𝒮S\in\mathcal{S} such that NA⁡(𝒫,S)\operatorname{NA}(\mathcal{P},S) is satisfied, there exists P∈co⁡(𝒫)P\in\operatorname{co}(\mathcal{P}), where co⁡(𝒫)\operatorname{co}(\mathcal{P}) is the convex hull of 𝒫\mathcal{P}, such that NA⁡(P,S)\operatorname{NA}(P,S) holds.

For the sake of completeness, we provide the proof below, even though the result follows from, e.g., [[4](https://arxiv.org/html/2601.19511v1#bib.bib9 "On arbitrage and duality under model uncertainty and portfolio constraints"), Lemma 2.7]:

###### Proof.

Fix S∈𝒮S\in\mathcal{S} with dimension d:=d​(S)d:=d(S) such that NA(𝒫\mathcal{P}) holds. Let

|  |  |  |
| --- | --- | --- |
|  | N​(𝒫):={H∈ℝd∣[H​Δ​S]c=0}​and​N​(𝒫)⟂={H∈ℝd∣∀H~∈N​(𝒫):H~⋅H=0},N(\mathcal{P}):=\{H\in\mathbb{R}^{d}\mid[H\Delta S]\_{c}=0\}\qquad\mbox{and}\qquad N(\mathcal{P})^{\perp}=\{H\in\mathbb{R}^{d}\mid\forall\widetilde{H}\in N(\mathcal{P})\colon\widetilde{H}\cdot H=0\}, |  |

where, for the sake of better readability, the Euclidean scalar product between the vectors H~\widetilde{H} and HH is denoted by H~⋅H\widetilde{H}\cdot H.

First suppose that N​(𝒫)⟂={0}N(\mathcal{P})^{\perp}=\{0\}. Then, for all H∈ℝdH\in\mathbb{R}^{d}, H​Δ​S=0H\Delta S=0 𝒫\mathcal{P}-q.s. and thus H​Δ​S=0H\Delta S=0 PP-a.s. for any P∈𝔓c​(Ω)P\in\mathfrak{P}\_{c}(\Omega). In particular, NA(P,SP,S) holds for any P∈𝒫P\in\mathcal{P}. From now on assume that N​(𝒫)⟂≠{0}N(\mathcal{P})^{\perp}\neq\{0\}. Then

|  |  |  |
| --- | --- | --- |
|  | ℍ:={H∈N​(𝒫)⟂∣∥H∥=1}≠∅,\mathbb{H}:=\{H\in N(\mathcal{P})^{\perp}\mid\lVert H\rVert=1\}\neq\emptyset, |  |

where ∥⋅∥\lVert\,\cdot\,\rVert denotes the Euclidean norm. For any H∈ℍH\in\mathbb{H}, by NA(𝒫,S\mathcal{P},S), there exists PH∈𝒫P\_{H}\in\mathcal{P} such that PH​(H​Δ​S<0)>0P\_{H}(H\Delta S<0)>0. Moreover, there exists εH>0\varepsilon\_{H}>0 such that for each H′∈B​(H,εH):={H~∣‖H~−H‖<εH}H^{\prime}\in B(H,\varepsilon\_{H}):=\{\widetilde{H}\mid\|\widetilde{H}-H\|<\varepsilon\_{H}\}, we have

|  |  |  |
| --- | --- | --- |
|  | PH​(H′​Δ​S<0)>0.P\_{H}(H^{\prime}\Delta S<0)>0. |  |

Indeed, there exists δ>0\delta>0 such that PH​(H​Δ​S<−δ)>0P\_{H}(H\Delta S<-\delta)>0, and, by boundedness of S1S\_{1}, there is M>0M>0 such that ∥Δ​S∥<M\lVert\Delta S\rVert<M. Let εH:=δ/M\varepsilon\_{H}:=\delta/M. For any H′∈B​(H,εH)H^{\prime}\in B(H,\varepsilon\_{H}),

|  |  |  |
| --- | --- | --- |
|  | H′​Δ​S−H​Δ​S≤|H′​Δ​S−H​Δ​S|≤∥H′−H∥⋅∥Δ​S∥≤εH⋅M=δ.H^{\prime}\Delta S-H\Delta S\leq\lvert H^{\prime}\Delta S-H\Delta S\rvert\leq\lVert H^{\prime}-H\rVert\cdot\lVert\Delta S\rVert\leq\varepsilon\_{H}\cdot M=\delta. |  |

Thus, PH​(H′​Δ​S<0)≥PH​(H​Δ​S<−δ)P\_{H}(H^{\prime}\Delta S<0)\geq P\_{H}(H\Delta S<-\delta). Note that ℍ⊆⋃H∈ℍB​(H,εH)\mathbb{H}\subseteq\bigcup\_{H\in\mathbb{H}}B(H,\varepsilon\_{H}). As ℍ\mathbb{H} is compact, there exists a finite subcover of ℍ\mathbb{H} given by H1,…,Hn∈ℍH\_{1},\ldots,H\_{n}\in\mathbb{H}, i.e., ℍ⊆⋃i=1nB​(Hi,εHi)\mathbb{H}\subseteq\bigcup\_{i=1}^{n}B(H\_{i},\varepsilon\_{H\_{i}}). Let P:=1n​∑i=1nPHiP:=\frac{1}{n}\sum\_{i=1}^{n}P\_{H\_{i}}. Then P∈co⁡(𝒫)P\in\operatorname{co}(\mathcal{P}) and P​(H​Δ​S<0)>0P(H\Delta S<0)>0 for all H∈ℍH\in\mathbb{H}. We now verify that NA(P,SP,S) holds. To this end, let H∈ℝdH\in\mathbb{R}^{d} and decompose H=H0+H⟂H=H^{0}+H^{\perp}, where H0∈N​(𝒫)H^{0}\in N(\mathcal{P}) and H⟂∈N​(𝒫)⟂H^{\perp}\in N(\mathcal{P})^{\perp}. Since H0​Δ​S=0H^{0}\Delta S=0 𝒫\mathcal{P}-q.s., it follows that H0​Δ​S=0H^{0}\Delta S=0 PP-a.s. If H⟂=0H^{\perp}=0, then H​Δ​S=H0​Δ​S=0H\Delta S=H^{0}\Delta S=0 PP-a.s. Otherwise, if H⟂≠0H^{\perp}\neq 0, then H⟂/‖H⟂‖∈ℍH^{\perp}/\|H^{\perp}\|\in\mathbb{H}, and therefore

|  |  |  |
| --- | --- | --- |
|  | P​(H​Δ​S<0)=P​(H⟂​Δ​S<0)=P​(H⟂‖H⟂‖​Δ​S<0)>0.P(H\Delta S<0)=P(H^{\perp}\Delta S<0)=P\bigg(\frac{H^{\perp}}{\|H^{\perp}\|}\Delta S<0\bigg)>0. |  |

Thus, NA(P,SP,S) is satisfied.
∎

As we will see below, the following class of set-valued maps 𝔔:𝒮↠𝔓c​(Ω)\mathfrak{Q}\colon\mathcal{S}\twoheadrightarrow\mathfrak{P}\_{c}(\Omega) is closely related to the 𝒫\mathcal{P}-sensitivity of the superhedging functional.

###### Definition 4.26.

A set-valued map 𝔔:𝒮↠𝔓c​(Ω)\mathfrak{Q}\colon\mathcal{S}\twoheadrightarrow\mathfrak{P}\_{c}(\Omega) is called

1. (i)

   ⊲\lhd-monotone if 𝔔​(S′)⊆𝔔​(S)\mathfrak{Q}(S^{\prime})\subseteq\mathfrak{Q}(S) for any S,S′∈𝒮S,S^{\prime}\in\mathcal{S} such that S⊲S′S\lhd S^{\prime},
2. (ii)

   weakly NA\operatorname{NA}-preserving if for any S∈𝒮S\in\mathcal{S} that satisfies NA⁡(𝒫,S)\operatorname{NA}(\mathcal{P},S), there exists Q∈𝔔​(S)Q\in\mathfrak{Q}(S) such that NA⁡(Q,S)\operatorname{NA}(Q,S) holds,
3. (iii)

   strongly NA\operatorname{NA}-preserving if for any S∈𝒮S\in\mathcal{S} that satisfies NA⁡(𝒫,S)\operatorname{NA}(\mathcal{P},S), 𝔔​(S)≠∅\mathfrak{Q}(S)\neq\emptyset and NA⁡(Q,S)\operatorname{NA}(Q,S) holds for all Q∈𝔔​(S)Q\in\mathfrak{Q}(S).

###### Lemma 4.27.

The maps 𝔔​(S)≡𝒫\mathfrak{Q}(S)\equiv\mathcal{P} for S∈𝒮S\in\mathcal{S}, 𝔐\mathfrak{M}, 𝔑​𝔄\mathfrak{NA}, 𝔐≪\mathfrak{M}\_{\ll}, and 𝔐≈\mathfrak{M}\_{\approx} are all ⊲\lhd-monotone. Moreover, 𝔐\mathfrak{M} and 𝔑​𝔄\mathfrak{NA} are strongly NA\operatorname{NA}-preserving. If 𝒫\mathcal{P} is convex, then 𝔔​(S)≡𝒫\mathfrak{Q}(S)\equiv\mathcal{P}, S∈𝒮S\in\mathcal{S}, is weakly NA\operatorname{NA}-preserving, while 𝔐≪\mathfrak{M}\_{\ll} and 𝔐≈\mathfrak{M}\_{\approx} are strongly NA\operatorname{NA}-preserving.

###### Proof.

⊲\lhd-monotonicity follows directly from the respective definitions of the maps.
Let S∈𝒮S\in\mathcal{S} satisfy NA⁡(𝒫,S)\operatorname{NA}(\mathcal{P},S). Then, by Lemma [4.25](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem25 "Lemma 4.25. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), there exists P∈co⁡(𝒫)P\in\operatorname{co}(\mathcal{P}) such that NA(P,SP,S). Thus, by the Fundamental Theorem of Asset Pricing (see, e.g., [[16](https://arxiv.org/html/2601.19511v1#bib.bib26 "Stochastic finance"), Theorem 1.7]), there is a martingale measure Q≈PQ\approx P. In particular, 𝔐​(S)≠∅\mathfrak{M}(S)\neq\emptyset and NA(R,SR,S) is satisfied for any R∈𝔑​𝔄​(S)R\in\mathfrak{NA}(S). Recalling that 𝔐​(S)⊆𝔑​𝔄​(S)\mathfrak{M}(S)\subseteq\mathfrak{NA}(S), we conclude that 𝔐\mathfrak{M} and 𝔑​𝔄\mathfrak{NA} are strongly NA\operatorname{NA}-preserving. If 𝒫=co⁡(𝒫)\mathcal{P}=\operatorname{co}(\mathcal{P}), then the previous arguments also prove the remaining assertions.
∎

###### Theorem 4.28.

Let 𝔔:𝒮↠𝔓c​(Ω)\mathfrak{Q}\colon\mathcal{S}\twoheadrightarrow\mathfrak{P}\_{c}(\Omega) be ⊲\lhd-monotone and weakly NA\operatorname{NA}-preserving. Suppose that S∈𝒮S\in\mathcal{S} satisfies NA⁡(𝒫,S)\operatorname{NA}(\mathcal{P},S). Then π(⋅∣S)\pi(\,\cdot\mid S) is 𝒫\mathcal{P}-sensitive with reduction set 𝔔​(S)\mathfrak{Q}(S) and (πQ(⋅∣S))Q∈𝔔​(S)(\pi^{Q}(\,\cdot\mid S))\_{Q\in\mathfrak{Q}(S)} is a 𝔔​(S)\mathfrak{Q}(S)-localization of π(⋅∣S)\pi(\,\cdot\mid S). In particular,

|  |  |  |  |
| --- | --- | --- | --- |
|  | π(X∣S)=supQ∈𝔔​(S)πEQ(X∣S)=supQ∈𝔔​(S)πQ(X∣S)=:π𝔔​(S)(X∣S).\pi(X\mid S)=\sup\_{Q\in\mathfrak{Q}(S)}\pi^{Q}\_{E}(X\mid S)=\sup\_{Q\in\mathfrak{Q}(S)}\pi^{Q}(X\mid S)=:\pi^{\mathfrak{Q}(S)}(X\mid S). |  | (15) |

###### Proof.

Suppose that S∈𝒮S\in\mathcal{S} satisfies NA(𝒫,S\mathcal{P},S). By Proposition [4.24](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem24 "Proposition 4.24. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | π(⋅∣S)≥πEQ(⋅∣S)≥πQ(⋅∣S)\pi(\,\cdot\mid S)\geq\pi^{Q}\_{E}(\,\cdot\mid S)\geq\pi^{Q}(\,\cdot\mid S) |  | (16) |

for all Q∈𝔔​(S)Q\in\mathfrak{Q}(S). Let X∈Lc∞X\in L^{\infty}\_{c}. If π​(X∣S)=−∞\pi(X\mid S)=-\infty, then ([15](https://arxiv.org/html/2601.19511v1#S4.E15 "In Theorem 4.28. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) follows. Assume that π​(X)>−∞\pi(X)>-\infty and let

|  |  |  |
| --- | --- | --- |
|  | π~​(Y∣S):=sup{x∈ℝ∣∃H∈ℋ​(S):Y≽x+[H​Δ​S]c},Y∈Lc∞,\widetilde{\pi}(Y\mid S):=\sup\{x\in\mathbb{R}\mid\exists H\in\mathcal{H}(S)\colon Y\succcurlyeq x+[H\Delta S]\_{c}\},\qquad Y\in L^{\infty}\_{c}, |  |

be the subhedging price for the market model SS. One verifies that NA(𝒫,S\mathcal{P},S) implies π~(⋅∣S)≤π(⋅∣S)\widetilde{\pi}(\,\cdot\mid S)\leq\pi(\,\cdot\mid S). If π~​(X∣S)<π​(X∣S)\widetilde{\pi}(X\mid S)<\pi(X\mid S), let x∈(π~​(X∣S),π​(X∣S))x\in(\widetilde{\pi}(X\mid S),\pi(X\mid S)) and consider the extended market SX=((S0,x),(S1,X))S\_{X}=((S\_{0},x),(S\_{1},X)). Let H∈ℝdH\in\mathbb{R}^{d}, h∈ℝh\in\mathbb{R} satisfy

|  |  |  |
| --- | --- | --- |
|  | [H​Δ​S]c+h​(X−x)≽0.[H\Delta S]\_{c}+h(X-x)\succcurlyeq 0. |  |

If h=0h=0, NA(𝒫,S\mathcal{P},S) implies that [H​Δ​S]c=0[H\Delta S]\_{c}=0. If h≠0h\neq 0 then either

|  |  |  |
| --- | --- | --- |
|  | −[Hh​Δ​S]c+x≽X​or−[Hh​Δ​S]c+x≼X.-\bigg[\frac{H}{h}\Delta S\bigg]\_{c}+x\succcurlyeq X\qquad\mbox{or}\qquad-\bigg[\frac{H}{h}\Delta S\bigg]\_{c}+x\preccurlyeq X. |  |

Hence, either x≥π​(X∣S)x\geq\pi(X\mid S) or x≤π~​(X∣S)x\leq\widetilde{\pi}(X\mid S), which is absurd. Thus, NA(𝒫,SX\mathcal{P},S\_{X}) is satisfied. As 𝔔\mathfrak{Q} is weakly NA\operatorname{NA}-preserving, there exists Q∈𝔔​(SX)Q\in\mathfrak{Q}(S\_{X}) such that NA(Q,SXQ,S\_{X}) holds. Hence, by the Fundamental Theorem of Asset Pricing for dominated models (see [[16](https://arxiv.org/html/2601.19511v1#bib.bib26 "Stochastic finance"), Theorem 1.7]), there is a martingale measure R∈𝔓c​(Ω)R\in\mathfrak{P}\_{c}(\Omega) for SS which is equivalent to QQ and satisfies ER​[X]=xE\_{R}[X]=x. The superhedging duality for dominated models (see [[16](https://arxiv.org/html/2601.19511v1#bib.bib26 "Stochastic finance"), Theorem 1.32]) implies πQ​(X∣S)≥ER​[X]=x\pi^{Q}(X\mid S)\geq E\_{R}[X]=x. By ⊲\lhd-monotonicity, we have Q∈𝔔​(S)Q\in\mathfrak{Q}(S). Therefore, as x∈(π~​(X∣S),π​(X∣S))x\in(\widetilde{\pi}(X\mid S),\pi(X\mid S)) was arbitrary, it follows that

|  |  |  |
| --- | --- | --- |
|  | π𝔔​(S)​(X∣S)=supQ∈𝔔​(S)πQ​(X∣S)≥π​(X∣S),\pi^{\mathfrak{Q}(S)}(X\mid S)=\sup\_{Q\in\mathfrak{Q}(S)}\pi^{Q}(X\mid S)\geq\pi(X\mid S), |  |

which, in conjunction with ([16](https://arxiv.org/html/2601.19511v1#S4.E16 "In Proof. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")), implies ([15](https://arxiv.org/html/2601.19511v1#S4.E15 "In Theorem 4.28. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")).

Finally, suppose that π~​(X∣S)=π​(X∣S)\widetilde{\pi}(X\mid S)=\pi(X\mid S). For every ε>0\varepsilon>0 there are H,H~∈ℝdH,\widetilde{H}\in\mathbb{R}^{d} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(X∣S)+ε+[H​Δ​S]c≽X≽π~​(X∣S)−ε+[H~​Δ​S]c=π​(X∣S)−ε+[H~​Δ​S]c.\pi(X\mid S)+\varepsilon+[H\Delta S]\_{c}\succcurlyeq X\succcurlyeq\widetilde{\pi}(X\mid S)-\varepsilon+[\widetilde{H}\Delta S]\_{c}=\pi(X\mid S)-\varepsilon+[\widetilde{H}\Delta S]\_{c}. |  | (17) |

As 𝔔\mathfrak{Q} is weakly NA\operatorname{NA}-preserving, there exists Q∈𝔔​(S)Q\in\mathfrak{Q}(S) such that NA(Q,SQ,S) holds. Consider any martingale measure R∈𝔓c​(Ω)R\in\mathfrak{P}\_{c}(\Omega) which is equivalent to QQ. Taking expectations under RR in ([17](https://arxiv.org/html/2601.19511v1#S4.E17 "In Proof. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) yields

|  |  |  |
| --- | --- | --- |
|  | π​(X∣S)+ε≥ER​[X]≥π​(X∣S)−ε.\pi(X\mid S)+\varepsilon\geq E\_{R}[X]\geq\pi(X\mid S)-\varepsilon. |  |

Since the latter is true for any ε>0\varepsilon>0, we conclude that ER​[X]=π​(X∣S)E\_{R}[X]=\pi(X\mid S). Again, the superhedging duality in dominated models implies πQ​(X∣S)≥ER​[X]=π​(X∣S)\pi^{Q}(X\mid S)\geq E\_{R}[X]=\pi(X\mid S), and thus

|  |  |  |
| --- | --- | --- |
|  | π𝔔​(S)​(X∣S)=supQ∈𝔔​(S)πQ​(X∣S)≥π​(X∣S),\pi^{\mathfrak{Q}(S)}(X\mid S)=\sup\_{Q\in\mathfrak{Q}(S)}\pi^{Q}(X\mid S)\geq\pi(X\mid S), |  |

which, in conjunction with ([16](https://arxiv.org/html/2601.19511v1#S4.E16 "In Proof. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")), implies ([15](https://arxiv.org/html/2601.19511v1#S4.E15 "In Theorem 4.28. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")).
∎

###### Corollary 4.29.

Suppose that S∈𝒮S\in\mathcal{S} satisfies NA⁡(𝒫,S)\operatorname{NA}(\mathcal{P},S). Then π(⋅∣S)=πE(⋅∣S)=πD(⋅∣S)\pi(\,\cdot\mid S)=\pi\_{E}(\,\cdot\mid S)=\pi\_{D}(\,\cdot\mid S).

###### Proof.

Letting 𝔔=𝔑​𝔄\mathfrak{Q}=\mathfrak{NA} and recalling Lemma [4.27](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem27 "Lemma 4.27. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), we have π(⋅∣S)=π𝔑​𝔄​(S)(⋅∣S)\pi(\,\cdot\mid S)=\pi^{\mathfrak{NA}(S)}(\,\cdot\mid S) by Theorem [4.28](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem28 "Theorem 4.28. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"). The superhedging duality for dominated models (see [[16](https://arxiv.org/html/2601.19511v1#bib.bib26 "Stochastic finance"), Theorem 1.32]) implies that π(⋅∣S)\pi(\,\cdot\mid S) admits a dual representation over c​acca\_{c}, since each πQ(⋅∣S)\pi^{Q}(\,\cdot\mid S) does so for every Q∈𝔑​𝔄​(S)Q\in\mathfrak{NA}(S). Hence, π(⋅∣S)=πE(⋅∣S)=πD(⋅∣S)\pi(\,\cdot\mid S)=\pi\_{E}(\,\cdot\mid S)=\pi\_{D}(\,\cdot\mid S) according to Theorem [3.10](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem10 "Theorem 3.10. ‣ 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
∎

###### Corollary 4.30.

Let 𝔔:𝒮↠𝔓c​(Ω)\mathfrak{Q}\colon\mathcal{S}\twoheadrightarrow\mathfrak{P}\_{c}(\Omega) be ⊲\lhd-monotone and strongly NA\operatorname{NA}-preserving. Then, for every S∈𝒮S\in\mathcal{S} such that NA⁡(𝒫,S)\operatorname{NA}(\mathcal{P},S) is satisfied, we have

|  |  |  |
| --- | --- | --- |
|  | π​(X∣S)=supQ∈𝔔​(S)supR∈𝔐≈Q​(S)ER​[X].\pi(X\mid S)=\sup\_{Q\in\mathfrak{Q}(S)}\sup\_{R\in\mathfrak{M}^{Q}\_{\approx}(S)}E\_{R}[X]. |  |

###### Proof.

Theorem [4.28](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem28 "Theorem 4.28. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") and the superhedging duality for dominated models.
∎

Lemma [4.31](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem31 "Lemma 4.31. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") and Corollary [4.32](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem32 "Corollary 4.32. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") below can also be found in [[9](https://arxiv.org/html/2601.19511v1#bib.bib13 "Arbitrage and duality in nondominated discrete-time models"), Theorems 2.2 and 2.3]. For the sake of completeness, we provide the proofs for the one-period case with deterministic trading strategies based on the proof of [[16](https://arxiv.org/html/2601.19511v1#bib.bib26 "Stochastic finance"), Theorem 1.32].

###### Lemma 4.31.

Suppose that S∈𝒮S\in\mathcal{S} satisfies NA⁡(𝒫,S)\operatorname{NA}(\mathcal{P},S). Then

|  |  |  |
| --- | --- | --- |
|  | 𝒞​(S):={X∈Lc∞∣∃H∈ℝd:X≼[H​Δ​S]c}.\mathcal{C}(S):=\{X\in L^{\infty}\_{c}\mid\exists H\in\mathbb{R}^{d}\colon X\preccurlyeq[H\Delta S]\_{c}\}. |  |

is closed under 𝒫\mathcal{P}-q.s. convergence.

###### Proof.

X∈𝒞​(S)X\in\mathcal{C}(S) if and only if X=[H​Δ​S]c−YX=[H\Delta S]\_{c}-Y for some H∈ℝdH\in\mathbb{R}^{d} and Y∈Lc+0Y\in L^{0}\_{c+}. Let (Xn)n∈ℕ⊆𝒞​(S)(X\_{n})\_{n\in\mathbb{N}}\subseteq\mathcal{C}(S) be a sequence which converges 𝒫\mathcal{P}-q.s. to a random variable X∈Lc∞X\in L^{\infty}\_{c}. Then, for any n∈ℕn\in\mathbb{N}, Xn=[Hn​Δ​S]c−YnX\_{n}=[H\_{n}\Delta S]\_{c}-Y\_{n}, where Hn∈ℝdH\_{n}\in\mathbb{R}^{d} and Yn∈Lc+0Y\_{n}\in L^{0}\_{c+}, and we will show that there exists H∈ℝdH\in\mathbb{R}^{d} and Y∈Lc+0Y\in L^{0}\_{c+} such that X=[H​Δ​S]c−YX=[H\Delta S]\_{c}-Y. To this end, we may assume that the market SS is non-redundant in the sense that [H​Δ​S]c=0[H\Delta S]\_{c}=0 implies H=0H=0. Otherwise, there is a component i∈{1,…,d}i\in\{1,\ldots,d\} and constants aj∈ℝa^{j}\in\mathbb{R}, j∈{1,…,d}∖{i}j\in\{1,\ldots,d\}\setminus\{i\}, such that S1i−S0i=∑j≠iaj​(S1j−S0j)S^{i}\_{1}-S\_{0}^{i}=\sum\_{j\neq i}a^{j}(S^{j}\_{1}-S\_{0}^{j}). Thus, letting S~\widetilde{S} be the market model obtained by removing the ii-th asset from SS, it follows that NA⁡(𝒫,S~)\operatorname{NA}(\mathcal{P},\widetilde{S}) is satisfied and

|  |  |  |
| --- | --- | --- |
|  | ∃H∈ℝd:X≼[H​Δ​S]c⇔∃H∈ℝd−1:X≼[H​Δ​S~]c,\exists H\in\mathbb{R}^{d}\colon X\preccurlyeq[H\Delta S]\_{c}\qquad\Leftrightarrow\qquad\exists H\in\mathbb{R}^{d-1}\colon X\preccurlyeq[H\Delta\widetilde{S}]\_{c}, |  |

so that 𝒞​(S)=𝒞​(S~)\mathcal{C}(S)=\mathcal{C}(\widetilde{S}).
Hence, from now on, consider a non-redundant market SS. Suppose that lim infn→∞∥Hn∥<∞\liminf\_{n\to\infty}\lVert H\_{n}\rVert<\infty.
Then there is a subsequence (Hnk)k∈ℕ(H\_{n\_{k}})\_{k\in\mathbb{N}} of (Hn)n∈ℕ(H\_{n})\_{n\in\mathbb{N}} which converges to a vector H∈ℝdH\in\mathbb{R}^{d}. In that case,

|  |  |  |
| --- | --- | --- |
|  | Ynk=Ynk+[Hnk​Δ​S]c−[Hnk​Δ​S]c=[Hnk​Δ​S]c−Xnk∈Lc+0Y\_{n\_{k}}=Y\_{n\_{k}}+[H\_{n\_{k}}\Delta S]\_{c}-[H\_{n\_{k}}\Delta S]\_{c}=[H\_{n\_{k}}\Delta S]\_{c}-X\_{n\_{k}}\in L^{0}\_{c+} |  |

converges 𝒫\mathcal{P}-q.s. to Y:=[H​Δ​S]c−X∈Lc+0Y:=[H\Delta S]\_{c}-X\in L^{0}\_{c+} and X=[H​Δ​S]c−YX=[H\Delta S]\_{c}-Y,
so X∈𝒞​(S)X\in\mathcal{C}(S).
Now suppose that lim infn→∞∥Hn∥=∞\liminf\_{n\to\infty}\lVert H\_{n}\rVert=\infty. Let

|  |  |  |
| --- | --- | --- |
|  | Gn:=Hn1+∥Hn∥,n∈ℕ.G\_{n}:=\frac{H\_{n}}{1+\lVert H\_{n}\rVert},\qquad n\in\mathbb{N}. |  |

As ∥Gn∥≤1\lVert G\_{n}\rVert\leq 1, n∈ℕn\in\mathbb{N}, there is a subsequence (Gnk)k∈ℕ(G\_{n\_{k}})\_{k\in\mathbb{N}} which converges to a vector G∈ℝdG\in\mathbb{R}^{d}, and ∥G∥=1\lVert G\rVert=1. Moreover, we have Xnk/(1+∥Hnk∥)→0X\_{n\_{k}}/(1+\lVert H\_{n\_{k}}\rVert)\to 0 and hence 𝒫\mathcal{P}-q.s.

|  |  |  |
| --- | --- | --- |
|  | limk→∞Ynk1+∥Hnk∥=limk→∞[Hnk​Δ​S]c1+∥Hnk∥−limk→∞Xnk1+∥Hnk∥=[G​Δ​S]c+0=[G​Δ​S]c.\lim\_{k\to\infty}\frac{Y\_{n\_{k}}}{1+\lVert H\_{n\_{k}}\rVert}=\lim\_{k\to\infty}\frac{[H\_{n\_{k}}\Delta S]\_{c}}{1+\lVert H\_{n\_{k}}\rVert}-\lim\_{k\to\infty}\frac{X\_{n\_{k}}}{1+\lVert H\_{n\_{k}}\rVert}=[G\Delta S]\_{c}+0=[G\Delta S]\_{c}. |  |

As Ynk/(1+∥Hnk∥)∈Lc+0Y\_{n\_{k}}/(1+\lVert H\_{n\_{k}}\rVert)\in L^{0}\_{c+} for all k∈ℕk\in\mathbb{N}, it follows that [G​Δ​S]c∈Lc+0[G\Delta S]\_{c}\in L^{0}\_{c+}. However, by NA(𝒫\mathcal{P}) we must have [G​Δ​S]c=0[G\Delta S]\_{c}=0 and thus G=0G=0, which contradicts ∥G∥=1\lVert G\rVert=1. Therefore, lim infn→∞∥Hn∥=∞\liminf\_{n\to\infty}\lVert H\_{n}\rVert=\infty is not possible.
∎

Lemma [4.31](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem31 "Lemma 4.31. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") implies the existence of optimal superhedging strategies.

###### Corollary 4.32.

Suppose that S∈𝒮S\in\mathcal{S} satisfies NA⁡(𝒫,S)\operatorname{NA}(\mathcal{P},S), and let X∈Lc∞X\in L^{\infty}\_{c}. Then, π​(X∣S)>−∞\pi(X\mid S)>-\infty and there exists H∈ℝdH\in\mathbb{R}^{d} such that X≼π​(X∣S)+[H​Δ​S]cX\preccurlyeq\pi(X\mid S)+[H\Delta S]\_{c}.

###### Proof.

Suppose that π​(X∣S)=−∞\pi(X\mid S)=-\infty. Then, for all n∈ℕn\in\mathbb{N}, there exists Hn∈ℝdH\_{n}\in\mathbb{R}^{d} such that X≼−n+[Hn​Δ​S]cX\preccurlyeq-n+[H\_{n}\Delta S]\_{c} and thus,

|  |  |  |
| --- | --- | --- |
|  | (X+n)∧1≼X+n≼[Hn​Δ​S]c.(X+n)\wedge 1\preccurlyeq X+n\preccurlyeq[H\_{n}\Delta S]\_{c}. |  |

That is, Xn:=(X+n)∧1∈𝒞​(S)X\_{n}:=(X+n)\wedge 1\in\mathcal{C}(S) for all n∈ℕn\in\mathbb{N}. Letting n→∞n\to\infty, Proposition [4.31](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem31 "Lemma 4.31. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") implies that 1∈𝒞​(S)1\in\mathcal{C}(S), which clearly contradicts NA(𝒫,S\mathcal{P},S).
If π​(X∣S)\pi(X\mid S) is finite, then Xn:=X−π​(X∣S)−1/n∈𝒞​(S)X\_{n}:=X-\pi(X\mid S)-1/n\in\mathcal{C}(S) for all n∈ℕn\in\mathbb{N}, and thus X−π​(X∣S)∈𝒞​(S)X-\pi(X\mid S)\in\mathcal{C}(S) by Proposition [4.31](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem31 "Lemma 4.31. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), which implies the existence of H∈ℝdH\in\mathbb{R}^{d} such that X≼π​(X∣S)+[H​Δ​S]cX\preccurlyeq\pi(X\mid S)+[H\Delta S]\_{c}.
∎

###### Corollary 4.33.

Let 𝔔:𝒮↠𝔓c​(Ω)\mathfrak{Q}\colon\mathcal{S}\twoheadrightarrow\mathfrak{P}\_{c}(\Omega) be ⊲\lhd-monotone and strongly NA\operatorname{NA}-preserving. Moreover, assume that ⋃Q∈𝔔​(S)𝔐≈Q​(S)⊆𝔔​(S)\bigcup\_{Q\in\mathfrak{Q}(S)}\mathfrak{M}^{Q}\_{\approx}(S)\subseteq\mathfrak{Q}(S), i.e., Q∈𝔔​(S)Q\in\mathfrak{Q}(S), R∈𝔐​(S)R\in\mathfrak{M}(S), and R≈QR\approx Q imply that R∈𝔔​(S)R\in\mathfrak{Q}(S).
Then, for every SS such that NA⁡(𝒫,S)\operatorname{NA}(\mathcal{P},S) is satisfied, 𝒫≈𝔔​(S)\mathcal{P}\approx\mathfrak{Q}(S) and

|  |  |  |
| --- | --- | --- |
|  | π​(X∣S)=supQ∈𝔔​(S)EQ​[X].\pi(X\mid S)=\sup\_{Q\in\mathfrak{Q}(S)}E\_{Q}[X]. |  |

###### Proof.

Corollary [4.30](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem30 "Corollary 4.30. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") and the additional requirement imply

|  |  |  |
| --- | --- | --- |
|  | π​(X∣S)=supQ∈𝔔​(S)supR∈𝔐≈Q​(S)ER​[X]=supR∈𝔔​(S)ER​[X].\pi(X\mid S)=\sup\_{Q\in\mathfrak{Q}(S)}\sup\_{R\in\mathfrak{M}^{Q}\_{\approx}(S)}E\_{R}[X]=\sup\_{R\in\mathfrak{Q}(S)}E\_{R}[X]. |  |

Let A∈ℱA\in\mathcal{F}. If c​(A)>0c(A)>0, then Corollary [4.32](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem32 "Corollary 4.32. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") and NA(𝒫,S\mathcal{P},S) imply π​(𝟏A∣S)>0\pi(\mathbf{1}\_{A}\mid S)>0, so there must be Q∈𝔔​(S)Q\in\mathfrak{Q}(S) such that Q​(A)=EQ​[𝟏A]>0Q(A)=E\_{Q}[\mathbf{1}\_{A}]>0. Conversely, if Q​(A)>0Q(A)>0, then π​(𝟏A∣S)>0\pi(\mathbf{1}\_{A}\mid S)>0. Therefore, 𝟏A≠0\mathbf{1}\_{A}\neq 0, that is c​(A)>0c(A)>0, because otherwise 𝟏A≼0+[0​Δ​S]c\mathbf{1}\_{A}\preccurlyeq 0+[0\Delta S]\_{c} implies that π​(𝟏A∣S)≤0\pi(\mathbf{1}\_{A}\mid S)\leq 0.
∎

According to Lemma [4.27](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem27 "Lemma 4.27. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), 𝔐\mathfrak{M}, 𝔑​𝔄\mathfrak{NA}, and, if 𝒫\mathcal{P} is convex, also 𝔐≪\mathfrak{M}\_{\ll} and 𝔐≈\mathfrak{M}\_{\approx} satisfy the requirements of Corollary [4.33](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem33 "Corollary 4.33. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"). We thus obtain the following version of the robust Superhedging Theorem.

###### Corollary 4.34.

Consider a market model S∈𝒮S\in\mathcal{S} for which NA⁡(𝒫,S)\operatorname{NA}(\mathcal{P},S) holds. Then

|  |  |  |
| --- | --- | --- |
|  | π​(X∣S)=supQ∈𝔑​𝔄​(S)EQ​[X]=supQ∈𝔐​(S)EQ​[X].\pi(X\mid S)=\sup\_{Q\in\mathfrak{NA}(S)}E\_{Q}[X]=\sup\_{Q\in\mathfrak{M}(S)}E\_{Q}[X]. |  |

If 𝒫\mathcal{P} is convex, then also

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(X∣S)=supQ∈𝔐≪​(S)EQ​[X]=supQ∈𝔐≈​(S)EQ​[X].\pi(X\mid S)=\sup\_{Q\in\mathfrak{M}\_{\ll}(S)}E\_{Q}[X]=\sup\_{Q\in\mathfrak{M}\_{\approx}(S)}E\_{Q}[X]. |  | (18) |

Note that the first equality in ([18](https://arxiv.org/html/2601.19511v1#S4.E18 "In Corollary 4.34. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162")) corresponds to the robust Superhedging Theorem given in [[9](https://arxiv.org/html/2601.19511v1#bib.bib13 "Arbitrage and duality in nondominated discrete-time models"), Theorem 3.4].

###### Theorem 4.35.

Suppose that each P∈𝒫P\in\mathcal{P} is supported. Moreover, suppose that 𝔔:𝒮↠𝔓c​(Ω)\mathfrak{Q}\colon\mathcal{S}\twoheadrightarrow\mathfrak{P}\_{c}(\Omega) is ⊲\lhd-monotone, strongly NA\operatorname{NA}-preserving, and satisfies the following conditions:

* •

  𝔔​(S)\mathfrak{Q}(S) is countably convex for all S∈𝒮S\in\mathcal{S}, in the sense that if (αn)n∈ℕ(\alpha\_{n})\_{n\in\mathbb{N}} is a sequence of non-negative real numbers summing up to 11 and Qn∈𝔔​(S)Q\_{n}\in\mathfrak{Q}(S) for all n∈ℕn\in\mathbb{N}, then ∑n∈ℕαn​Qn∈𝔔​(S)\sum\_{n\in\mathbb{N}}\alpha\_{n}Q\_{n}\in\mathfrak{Q}(S).
* •

  ⋃Q∈𝔔​(S)𝔐≈Q​(S)⊆𝔔​(S)⊆𝔐​(S)\bigcup\_{Q\in\mathfrak{Q}(S)}\mathfrak{M}^{Q}\_{\approx}(S)\subseteq\mathfrak{Q}(S)\subseteq\mathfrak{M}(S).

Then, for any S∈𝒮S\in\mathcal{S}, the following are equivalent:

1. (i)

   NA⁡(𝒫,S)\operatorname{NA}(\mathcal{P},S) holds.
2. (ii)

   For all P∈𝒫P\in\mathcal{P} there exists Q∈𝔔​(S)Q\in\mathfrak{Q}(S) such that P≪QP\ll Q.

###### Proof.

(i) ⇒\Rightarrow (ii): Suppose that NA(𝒫,S\mathcal{P},S) holds for SS and let P∈𝒫P\in\mathcal{P}.
For all Q∈𝔔​(S)Q\in\mathfrak{Q}(S), consider the Lebesgue decomposition Q=QP+Q⟂Q=Q\_{P}+Q\_{\perp} such that QP≪PQ\_{P}\ll P. Let

|  |  |  |
| --- | --- | --- |
|  | u:=supQ∈𝔔​(S)P​(d​QPd​P>0).u:=\sup\_{Q\in\mathfrak{Q}(S)}P\bigg(\frac{dQ\_{P}}{dP}>0\bigg). |  |

Choose Q1,Q2,⋯∈𝔔​(S)Q^{1},Q^{2},\dots\in\mathfrak{Q}(S) such that P​(d​QPnd​P>0)→uP(\frac{dQ^{n}\_{P}}{dP}>0)\to u as n→∞n\to\infty and set

|  |  |  |
| --- | --- | --- |
|  | Q~:=∑i∈ℕαi​Qi\widetilde{Q}:=\sum\_{i\in\mathbb{N}}\alpha\_{i}Q^{i} |  |

where αi>0\alpha\_{i}>0 for all i∈ℕi\in\mathbb{N}, and ∑i∈ℕαi=1\sum\_{i\in\mathbb{N}}\alpha\_{i}=1. Then, Q~∈𝔔​(S)\widetilde{Q}\in\mathfrak{Q}(S) by countable convexity, and Q~P=∑i∈ℕαi​QPi\widetilde{Q}\_{P}=\sum\_{i\in\mathbb{N}}\alpha\_{i}Q^{i}\_{P} and Q~⟂=∑i∈ℕαi​Q⟂i\widetilde{Q}\_{\perp}=\sum\_{i\in\mathbb{N}}\alpha\_{i}Q^{i}\_{\perp}. In particular, d​Q~Pd​P=∑i∈ℕαi​d​QPid​P\frac{d\widetilde{Q}\_{P}}{dP}=\sum\_{i\in\mathbb{N}}\alpha\_{i}\frac{dQ^{i}\_{P}}{dP} and thus

|  |  |  |
| --- | --- | --- |
|  | P​(d​Q~Pd​P>0)=P​(⋃n∈ℕ{d​QPnd​P>0})≥limn→∞P​(d​QPnd​P>0)=u.P\bigg(\frac{d\widetilde{Q}\_{P}}{dP}>0\bigg)=P\bigg(\bigcup\_{n\in\mathbb{N}}\bigg\{\frac{dQ^{n}\_{P}}{dP}>0\bigg\}\bigg)\geq\lim\_{n\to\infty}P\bigg(\frac{dQ^{n}\_{P}}{dP}>0\bigg)=u. |  |

Hence, P​(d​Q~Pd​P>0)=uP(\frac{d\widetilde{Q}\_{P}}{dP}>0)=u. Suppose that u<1u<1. Then A:={d​Q~Pd​P=0}∩S​(P)A:=\{\frac{d\widetilde{Q}\_{P}}{dP}=0\}\cap S(P) satisfies P​(A)>0P(A)>0. According to Corollary [4.33](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem33 "Corollary 4.33. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), there exists Q^∈𝔔​(S)\widehat{Q}\in\mathfrak{Q}(S) such that Q^​(A)>0\widehat{Q}(A)>0. Note that Q^P​(A)>0\widehat{Q}\_{P}(A)>0, because one verifies that Q^⟂​(S​(P))=0\widehat{Q}\_{\perp}(S(P))=0. Therefore,

|  |  |  |
| --- | --- | --- |
|  | P​({d​Q^Pd​P>0}∩A)>0.P\bigg(\bigg\{\frac{d\widehat{Q}\_{P}}{dP}>0\bigg\}\cap A\bigg)>0. |  |

Let R:=12​(Q~+Q^)∈𝔔​(S)R:=\frac{1}{2}(\widetilde{Q}+\widehat{Q})\in\mathfrak{Q}(S). Then

|  |  |  |
| --- | --- | --- |
|  | P​(d​RPd​P>0)=P​(12​(d​Q^Pd​P+d​Q~Pd​P)>0)≥P​({d​Q^Pd​P>0}∩A)+P​(d​Q~Pd​P>0)>u,P\bigg(\frac{dR\_{P}}{dP}>0\bigg)=P\bigg(\frac{1}{2}\bigg(\frac{d\widehat{Q}\_{P}}{dP}+\frac{d\widetilde{Q}\_{P}}{dP}\bigg)>0\bigg)\geq P\bigg(\bigg\{\frac{d\widehat{Q}\_{P}}{dP}>0\bigg\}\cap A\bigg)+P\bigg(\frac{d\widetilde{Q}\_{P}}{dP}>0\bigg)>u, |  |

which is a contradiction. Hence, P​(d​Q~Pd​P>0)=1P(\frac{d\widetilde{Q}\_{P}}{dP}>0)=1 and P≪Q~P\ll\widetilde{Q}.

(ii) ⇒\Rightarrow (i): Let H∈ℝdH\in\mathbb{R}^{d} such that H​Δ​S≥0H\Delta S\geq 0 𝒫\mathcal{P}-q.s. Suppose there exists P∈𝒫P\in\mathcal{P} such that P​(H​Δ​S>0)>0P(H\Delta S>0)>0. By assumption, there exists Q∈𝔔​(S)Q\in\mathfrak{Q}(S) such that P≪QP\ll Q. Consequently, Q​(H​Δ​S>0)>0Q(H\Delta S>0)>0, while H​Δ​S≥0H\Delta S\geq 0 𝒫\mathcal{P}-q.s. implies H​Δ​S≥0H\Delta S\geq 0 QQ-a.s. But Q∈𝔐​(S)Q\in\mathfrak{M}(S) and thus EQ​[H​Δ​S]=0E\_{Q}[H\Delta S]=0, which is absurd. Therefore, P​(H​Δ​S>0)=0P(H\Delta S>0)=0 for all P∈𝒫P\in\mathcal{P}, which implies [H​Δ​S]c=0[H\Delta S]\_{c}=0.
∎

Note that 𝔐\mathfrak{M} satisfies the requirements of Theorem [4.35](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem35 "Theorem 4.35. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), and, if 𝒫\mathcal{P} is itself countably convex, so do 𝔐≪\mathfrak{M}\_{\ll} and 𝔐≈\mathfrak{M}\_{\approx}. Consequently, we obtain Corollaries [4.36](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem36 "Corollary 4.36. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), [4.37](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem37 "Corollary 4.37. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), and [4.38](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem38 "Corollary 4.38. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").

###### Corollary 4.36.

Suppose that each P∈𝒫P\in\mathcal{P} is supported. For any S∈𝒮S\in\mathcal{S}, the following are equivalent:

1. (i)

   NA⁡(𝒫,S)\operatorname{NA}(\mathcal{P},S) holds.
2. (ii)

   For all P∈𝒫P\in\mathcal{P} there exists Q∈𝔐​(S)Q\in\mathfrak{M}(S) such that P≪QP\ll Q.

The following corollary is a version of [[9](https://arxiv.org/html/2601.19511v1#bib.bib13 "Arbitrage and duality in nondominated discrete-time models"), Theorem 3.1].

###### Corollary 4.37.

Suppose that each P∈𝒫P\in\mathcal{P} is supported and that 𝒫\mathcal{P} is countably convex. For any S∈𝒮S\in\mathcal{S}, the following are equivalent:

1. (i)

   NA⁡(𝒫,S)\operatorname{NA}(\mathcal{P},S) holds.
2. (ii)

   For all P∈𝒫P\in\mathcal{P} there exists Q∈𝔐≪​(S)Q\in\mathfrak{M}\_{\ll}(S) such that P≪QP\ll Q.

We further obtain the following stronger version of the Fundamental Theorem of Asset Pricing, where we only consider equivalent martingale measures. A result in that vain can also be found in [[8](https://arxiv.org/html/2601.19511v1#bib.bib12 "No-arbitrage with multiple-priors in discrete time"), Corollary 3.10].

###### Corollary 4.38.

Suppose that each P∈𝒫P\in\mathcal{P} is supported and that 𝒫\mathcal{P} is countably convex. For any S∈𝒮S\in\mathcal{S}, the following are equivalent:

1. (i)

   NA⁡(𝒫,S)\operatorname{NA}(\mathcal{P},S) holds.
2. (ii)

   For all P∈𝒫P\in\mathcal{P} there exists Q∈𝔐≈​(S)Q\in\mathfrak{M}\_{\approx}(S) such that P≪QP\ll Q.

Example [4.39](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem39 "Example 4.39. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") shows that the assumption that each P∈𝒫P\in\mathcal{P} is supported in Theorem [4.35](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem35 "Theorem 4.35. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") cannot be dropped.

###### Example 4.39.

Consider the unit interval Ω=[0,1]\Omega=[0,1] equipped with the Borel-σ\sigma-algebra ℱ=ℬ​(Ω)\mathcal{F}=\mathcal{B}(\Omega). Let 𝒫={δω∣ω∈Ω}∪{λ}\mathcal{P}=\{\delta\_{\omega}\mid\omega\in\Omega\}\cup\{\lambda\}, where λ\lambda is the Lebesgue measure on (Ω,ℱ)(\Omega,\mathcal{F}). One verifies that λ\lambda is not supported. Define 𝔔:𝒮↠𝔓c​(Ω)\mathfrak{Q}\colon\mathcal{S}\twoheadrightarrow\mathfrak{P}\_{c}(\Omega) by

|  |  |  |
| --- | --- | --- |
|  | 𝔔​(S):={∑i∈ℕαi​δωi|∀i∈ℕ:ωi∈Ω,αi≥0∧∑i∈ℕαi=1​and​∑i∈ℕαi​Δ​S​(ωi)=0}.\mathfrak{Q}(S):=\bigg\{\sum\_{i\in\mathbb{N}}\alpha\_{i}\delta\_{\omega\_{i}}\biggm|\forall i\in\mathbb{N}\colon\omega\_{i}\in\Omega,\ \alpha\_{i}\geq 0\ \wedge\ \sum\_{i\in\mathbb{N}}\alpha\_{i}=1\qquad\text{and}\qquad\sum\_{i\in\mathbb{N}}\alpha\_{i}\Delta S(\omega\_{i})=0\bigg\}. |  |

Note that 𝔔​(S)⊆𝔐​(S)\mathfrak{Q}(S)\subseteq\mathfrak{M}(S). Clearly, 𝔔\mathfrak{Q} is ⊲\lhd-monotone. Next, we check that 𝔔\mathfrak{Q} is also strongly NA\operatorname{NA}-preserving. Let S∈𝒮S\in\mathcal{S} such that NA(𝒫,S\mathcal{P},S) holds. In this case also NA(𝒫′,S\mathcal{P}^{\prime},S) is satisfied, where 𝒫′={δω∣ω∈Ω}\mathcal{P}^{\prime}=\{\delta\_{\omega}\mid\omega\in\Omega\}. By Lemma [4.25](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem25 "Lemma 4.25. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"), there exists P∈co⁡(𝒫′)P\in\operatorname{co}(\mathcal{P}^{\prime}) such that NA(P,SP,S) is satisfied. Since P∈co⁡(𝒫′)P\in\operatorname{co}(\mathcal{P}^{\prime}), there are n∈ℕn\in\mathbb{N}, ωi∈Ω\omega\_{i}\in\Omega, αi>0\alpha\_{i}>0, i=1,…,ni=1,\ldots,n, such that ∑i=1nαi=1\sum\_{i=1}^{n}\alpha\_{i}=1 and P=∑i=1nαi​δωiP=\sum\_{i=1}^{n}\alpha\_{i}\delta\_{\omega\_{i}}. NA(P,SP,S) implies that there exists Q∈𝔐≈P​(S)Q\in\mathfrak{M}^{P}\_{\approx}(S). In particular, Q=∑i=1nβi​δωiQ=\sum\_{i=1}^{n}\beta\_{i}\delta\_{\omega\_{i}} for some βi>0\beta\_{i}>0, i=1,…,ni=1,\ldots,n, with ∑i=1nβi=1\sum\_{i=1}^{n}\beta\_{i}=1.
Clearly, NA(Q,SQ,S) holds and Q∈𝔔​(S)Q\in\mathfrak{Q}(S). Moreover, as 𝔔​(S)⊆𝔐​(S)\mathfrak{Q}(S)\subseteq\mathfrak{M}(S), 𝔔​(S)\mathfrak{Q}(S) is strongly NA\operatorname{NA}-preserving.
Furthermore, 𝔔​(S)\mathfrak{Q}(S) is countably convex and ⋃Q∈𝔔​(S)𝔐≈Q​(S)⊆𝔔​(S)⊆𝔐​(S)\bigcup\_{Q\in\mathfrak{Q}(S)}\mathfrak{M}^{Q}\_{\approx}(S)\subseteq\mathfrak{Q}(S)\subseteq\mathfrak{M}(S). However, there is clearly no Q∈𝔔​(S)Q\in\mathfrak{Q}(S) such that λ≪Q\lambda\ll Q, and Theorem [4.35](https://arxiv.org/html/2601.19511v1#S4.Thmtheorem35 "Theorem 4.35. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162") does not hold. ⋄\diamond

## References

* [1]
  C. D. Aliprantis and K. C. Border (2006)
  Infinite dimensional analysis: a hitchhiker’s guide.
  3 edition, Springer.
  External Links: [Document](https://dx.doi.org/10.1007/3-540-29587-9)
  Cited by: [§4.2](https://arxiv.org/html/2601.19511v1#S4.SS2.7.p1.13 "Proof. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [2]
  D. Bartl, M. Kupper, and A. Neufeld (2020)
  Pathwise superhedging on prediction sets.
  Finance and Stochastics 24 (1),  pp. 215–248.
  External Links: [Document](https://dx.doi.org/10.1007/s00780-019-00412-4)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p1.9 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [3]
  D. Bartl, M. Kupper, and A. Neufeld (2021-06-14)
  Duality theory for robust utility maximisation.
  Finance and Stochastics 25 (3),  pp. 469–503.
  External Links: [Document](https://dx.doi.org/10.1007/s00780-021-00455-6)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p1.9 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [4]
  E. Bayraktar and Z. Zhou (2015-09-29)
  On arbitrage and duality under model uncertainty and portfolio constraints.
  Mathematical Finance 27 (4),  pp. 988–1012.
  External Links: [Document](https://dx.doi.org/10.1111/mafi.12104)
  Cited by: [§4.3](https://arxiv.org/html/2601.19511v1#S4.SS3.p5.1 "4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [5]
  P. Beissner and L. Denis (2018-01)
  Duality and general equilibrium theory under knightian uncertainty.
  SIAM Journal on Financial Mathematics 9 (1),  pp. 381–400.
  External Links: [Document](https://dx.doi.org/10.1137/17m1120877)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.SS0.SSS0.Px1.p1.1 "Further Related Literature ‣ 1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [6]
  T. F. Bewley (1972)
  Existence of equilibria in economies with infinitely many commodities.
  Journal of Economic Theory 4 (3),  pp. 514–540.
  External Links: ISSN 0022-0531,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/0022-0531%2872%2990136-6),
  [Link](https://www.sciencedirect.com/science/article/pii/0022053172901366)
  Cited by: [§4.2](https://arxiv.org/html/2601.19511v1#S4.SS2.p5.13 "4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [7]
  J. Bion-Nadal and M. Kervarec (2012-02-01)
  Risk measuring under model uncertainty.
  The Annals of Applied Probability 22 (1),  pp. 213–238.
  External Links: [Document](https://dx.doi.org/10.1214/11-aap766)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.SS0.SSS0.Px1.p1.1 "Further Related Literature ‣ 1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [8]
  R. Blanchard and L. Carassus (2020-11)
  No-arbitrage with multiple-priors in discrete time.
  Stochastic Processes and their Applications 130 (11),  pp. 6657–6688.
  External Links: [Document](https://dx.doi.org/10.1016/j.spa.2020.06.006)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p1.9 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.3](https://arxiv.org/html/2601.19511v1#S4.SS3.p13.1 "4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [9]
  B. Bouchard and M. Nutz (2015-04-01)
  Arbitrage and duality in nondominated discrete-time models.
  The Annals of Applied Probability 25 (2).
  External Links: [Document](https://dx.doi.org/10.1214/14-aap1011)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p1.9 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.3](https://arxiv.org/html/2601.19511v1#S4.SS3.p10.1 "4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.3](https://arxiv.org/html/2601.19511v1#S4.SS3.p12.1 "4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.3](https://arxiv.org/html/2601.19511v1#S4.SS3.p2.9 "4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.3](https://arxiv.org/html/2601.19511v1#S4.SS3.p7.1 "4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [10]
  M. Burzoni, M. Frittelli, Z. Hou, M. Maggis, and J. Obłój (2019-08)
  Pointwise arbitrage pricing theory in discrete time.
  Mathematics of Operations Research 44 (3),  pp. 1034–1057.
  External Links: [Document](https://dx.doi.org/10.1287/moor.2018.0956)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p1.9 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [11]
  M. Burzoni and M. Maggis (2020-06-09)
  Arbitrage-free modeling under knightian uncertainty.
  Mathematics and Financial Economics 14 (4),  pp. 635–659.
  External Links: [Document](https://dx.doi.org/10.1007/s11579-020-00267-w)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p1.9 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§1](https://arxiv.org/html/2601.19511v1#S1.p4.7 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [12]
  H. Chau, M. Fukasawa, and M. Rásonyi (2022-06-23)
  Super‐replication with transaction costs under model uncertainty for continuous processes.
  Mathematical Finance 32 (4),  pp. 1066–1085.
  External Links: [Document](https://dx.doi.org/10.1111/mafi.12355)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p1.9 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [13]
  S. Cohen (2012-01-01)
  Quasi-sure analysis, aggregation and dual representations of sublinear expectations in general spaces.
  Electronic Journal of Probability 17,  pp. 1–15.
  External Links: [Document](https://dx.doi.org/10.1214/ejp.v17-2224)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p1.9 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [14]
  L. Denis, M. Hu, and S. Peng (2011)
  Function spaces and capacity related to a sublinear expectation: Application to G-Brownian motion paths.
  Potential Analysis 34 (2),  pp. 139–161.
  External Links: [Document](https://dx.doi.org/10.1007/s11118-010-9185-x)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.SS0.SSS0.Px1.p1.1 "Further Related Literature ‣ 1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [15]
  I. Ekeland and R. Témam (1999-01)
  Convex analysis and variational problems.
   Society for Industrial and Applied Mathematics.
  External Links: [Document](https://dx.doi.org/10.1137/1.9781611971088)
  Cited by: [§3.2](https://arxiv.org/html/2601.19511v1#S3.SS2.12.p5.6 "Proof. ‣ 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§3.2](https://arxiv.org/html/2601.19511v1#S3.SS2.p4.6 "3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [Remark 3.7](https://arxiv.org/html/2601.19511v1#S3.Thmtheorem7.p1.14 "Remark 3.7. ‣ 3.2 Robust Dual Representation and 𝓟-Sensitivity ‣ 3 𝓟-Sensitivity and Functional Localization ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [16]
  H. Föllmer and A. Schied (2016-07-25)
  Stochastic finance.
  4 edition, De Gruyter.
  External Links: [Document](https://dx.doi.org/10.1515/9783110463453)
  Cited by: [§4.2](https://arxiv.org/html/2601.19511v1#S4.SS2.3.p1.1 "Proof. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.2](https://arxiv.org/html/2601.19511v1#S4.SS2.7.p1.13 "Proof. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.2](https://arxiv.org/html/2601.19511v1#S4.SS2.8.p1.9 "Proof. ‣ 4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.2](https://arxiv.org/html/2601.19511v1#S4.SS2.p6.29 "4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.2](https://arxiv.org/html/2601.19511v1#S4.SS2.p8.1 "4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.3](https://arxiv.org/html/2601.19511v1#S4.SS3.1.p1.10 "Proof. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.3](https://arxiv.org/html/2601.19511v1#S4.SS3.11.p1.7 "Proof. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.3](https://arxiv.org/html/2601.19511v1#S4.SS3.4.p2.5 "Proof. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.3](https://arxiv.org/html/2601.19511v1#S4.SS3.8.p1.14 "Proof. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.3](https://arxiv.org/html/2601.19511v1#S4.SS3.9.p1.33 "Proof. ‣ 4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.3](https://arxiv.org/html/2601.19511v1#S4.SS3.p7.1 "4.3 Arbitrage and Superhedging in One Period ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [17]
  N. Gao and C. Munari (2020-11)
  Surplus-invariant risk measures.
  Mathematics of Operations Research 45 (4),  pp. 1342–1370.
  External Links: [Document](https://dx.doi.org/10.1287/moor.2019.1035)
  Cited by: [§4.2](https://arxiv.org/html/2601.19511v1#S4.SS2.p9.1 "4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [18]
  C. Gilles and S. F. LeRoy (1992)
  Bubbles and charges.
  International Economic Review 33 (2),  pp. 323–339.
  External Links: ISSN 00206598, 14682354,
  [Link](http://www.jstor.org/stable/2526897)
  Cited by: [§4.2](https://arxiv.org/html/2601.19511v1#S4.SS2.p5.13 "4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [19]
  C. Gilles (1989)
  Charges as equilibrium prices and asset bubbles.
  Journal of Mathematical Economics 18 (2),  pp. 155–167.
  External Links: ISSN 0304-4068,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/0304-4068%2889%2990019-0),
  [Link](https://www.sciencedirect.com/science/article/pii/0304406889900190)
  Cited by: [§4.2](https://arxiv.org/html/2601.19511v1#S4.SS2.p5.13 "4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [20]
  Z. Hou and J. Obłój (2018-05-30)
  Robust pricing–hedging dualities in continuous time.
  Finance and Stochastics 22 (3),  pp. 511–567.
  External Links: [Document](https://dx.doi.org/10.1007/s00780-018-0363-9)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p1.9 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [21]
  R. A. Jarrow, P. Protter, and K. Shimbo (2010)
  Asset price bubbles in incomplete markets.
  Mathematical Finance 20 (2),  pp. 145–185.
  External Links: [Document](https://dx.doi.org/https%3A//doi.org/10.1111/j.1467-9965.2010.00394.x),
  https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1467-9965.2010.00394.x,
  [Link](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9965.2010.00394.x)
  Cited by: [§4.2](https://arxiv.org/html/2601.19511v1#S4.SS2.p5.13 "4.2 Monetary Risk Measures and Localization Bubbles ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [22]
  J. Langner and G. Svindland (2025-10-14)
  Bipolar theorems for sets of nonnegative random variables.
  Finance and Stochastics.
  External Links: [Document](https://dx.doi.org/10.1007/s00780-025-00579-z)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p4.7 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§2.2](https://arxiv.org/html/2601.19511v1#S2.SS2.6.p1.5 "Proof. ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§2.2](https://arxiv.org/html/2601.19511v1#S2.SS2.p13.6 "2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§2.2](https://arxiv.org/html/2601.19511v1#S2.SS2.p14.3 "2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§2.2](https://arxiv.org/html/2601.19511v1#S2.SS2.p15.1 "2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§2.2](https://arxiv.org/html/2601.19511v1#S2.SS2.p3.16 "2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§2.2](https://arxiv.org/html/2601.19511v1#S2.SS2.p5.3 "2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [Lemma 2.3](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem3 "Lemma 2.3 ([22, Lemma 2.10]). ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [Lemma 2.4](https://arxiv.org/html/2601.19511v1#S2.Thmtheorem4 "Lemma 2.4 ([22, Lemma 2.11]). ‣ 2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [23]
  F. Liebrich, M. Maggis, and G. Svindland (2022-09)
  Model uncertainty: a reverse approach.
  SIAM Journal on Financial Mathematics 13 (3),  pp. 1230–1269.
  External Links: [Document](https://dx.doi.org/10.1137/21m1425463)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.SS0.SSS0.Px1.p1.1 "Further Related Literature ‣ 1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.1](https://arxiv.org/html/2601.19511v1#S4.SS1.p4.9 "4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.1](https://arxiv.org/html/2601.19511v1#S4.SS1.p5.3 "4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§4.1](https://arxiv.org/html/2601.19511v1#S4.SS1.p7.1 "4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [24]
  H. Luschgy (1978)
  Sur l’existence d’une plus petite sous-tribu exhaustive par paire.
  Annales de l’institut Henri Poincaré. Section B. Calcul des probabilités et statistiques 14 (4),  pp. 391–398 (fr).
  External Links: [Link](https://www.numdam.org/item/AIHPB_1978__14_4_391_0/),
  [MathReview Entry](https://www.ams.org/mathscinet-getitem?mr=523218)
  Cited by: [§4.1](https://arxiv.org/html/2601.19511v1#S4.SS1.p5.3 "4.1 Robust Optimization ‣ 4 Applications ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [25]
  M. Maggis, T. Meyer-Brandis, and G. Svindland (2018-03-24)
  Fatou closedness under model uncertainty.
  Positivity 22 (5),  pp. 1325–1343.
  External Links: [Document](https://dx.doi.org/10.1007/s11117-018-0578-1)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p4.7 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162"),
  [§2.2](https://arxiv.org/html/2601.19511v1#S2.SS2.p3.16 "2.2 𝓟-sensitive Sets and Functions ‣ 2 Preliminaries and Notation ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [26]
  A. Matoussi, D. Possamai, and C. Zhou (2013)
  Second order reflected backward stochastic differential equations.
  The Annals of Applied Probability 23 (6),  pp. 2420 – 2457.
  External Links: [Document](https://dx.doi.org/10.1214/12-AAP906),
  [Link](https://doi.org/10.1214/12-AAP906)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p1.9 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [27]
  M. Nutz and H. M. Soner (2012)
  Superhedging and dynamic risk measures under volatility uncertainty.
  SIAM Journal on Control and Optimization 50 (4),  pp. 2065–2089.
  External Links: [Document](https://dx.doi.org/10.1137/100814925),
  [Link](https://doi.org/10.1137/100814925)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p1.9 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [28]
  H. M. Soner, N. Touzi, and J. Zhang (2012)
  Wellposedness of second order backward SDEs.
  Probability Theory and Related Fields 153,  pp. 149–190.
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p1.9 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [29]
  H. M. Soner, N. Touzi, and J. Zhang (2011-01-01)
  Quasi-sure stochastic analysis through aggregation.
  Electronic Journal of Probability 16,  pp. 1844–1879.
  External Links: [Document](https://dx.doi.org/10.1214/ejp.v16-950)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p1.9 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").
* [30]
  H. M. Soner, N. Touzi, and J. Zhang (2013)
  Dual formulation of second order target problems.
  The Annals of Applied Probability 23 (1),  pp. 308 – 347.
  External Links: [Document](https://dx.doi.org/10.1214/12-AAP844),
  [Link](https://doi.org/10.1214/12-AAP844)
  Cited by: [§1](https://arxiv.org/html/2601.19511v1#S1.p1.9 "1 Introduction ‣ 𝒫-Sensitive Functions and Localizations1footnote 11footnote 1funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – 471178162").