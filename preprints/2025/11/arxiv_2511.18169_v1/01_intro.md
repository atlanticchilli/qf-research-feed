---
authors:
- Atiqah Almuzaini
- Çağın Ararat
- Jin Ma
doc_id: arxiv:2511.18169v1
family_id: arxiv:2511.18169
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Superhedging under Proportional Transaction Costs in Continuous Time
url_abs: http://arxiv.org/abs/2511.18169v1
url_html: https://arxiv.org/html/2511.18169v1
venue: arXiv q-fin
version: 1
year: 2025
---


Atiqah Almuzaini,  
Çağın Ararat,
  and   Jin Ma
Department of Mathematics and Statistics, University of Jeddah, Jeddah, Saudi Arabia.
Email: ahalmuzaini@uj.edu.saDepartment of Industrial Engineering, Bilkent University, Ankara, 06800, Turkey. Email: cararat@bilkent.edu.tr. This author is supported by TÜBİTAK 2219 Program and by the Fulbright Scholar Program of the U.S. Department of State, sponsored by the Turkish Fulbright Commission. This work was partly completed while the author was visiting University of Southern California, whose hospitality is greatly appreciated. Department of
Mathematics, University of Southern California, Los Angeles, 90089;
email: jinma@usc.edu. This author is supported in part by US NSF grants #2205972 and #2510403.

(November 22, 2025)

###### Abstract

We revisit the well-studied superhedging problem under proportional transaction costs in continuous time using the recently developed tools of set-valued stochastic analysis. By relying on a simple Black-Scholes-type market model for mid-prices and using continuous trading schemes, we define a dynamic family of superhedging sets in continuous time and express them in terms of set-valued integrals. We show that these sets, defined as subsets of Lebesgue spaces at different times, form a dynamic set-valued risk measure with multi-portfolio time-consistency. Finally, we transfer the problem formulation to a path-space setting and introduce approximate versions of superhedging sets that will involve relaxing the superhedging inequality, the superhedging probability, and the solvency requirement for the superhedging strategy with a predetermined error level. In this more technical framework, we are able to relate the approximate superhedging sets at different times by means of a set-valued Bellman’s principle, which we believe will pave the way for a set-valued differential structure that characterizes the superhedging sets.

Keywords: superhedging problem, solvency cone, dynamic set-valued risk measure, set-valued dynamic programming, set-valued integral, path space

AMS subject classifications:
26E25, 28B20, 60H10, 91G70, 93E20

## 1 Introduction

In this paper, we revisit the well-known dynamic superhedging problem in continuous time under proportional transaction costs and offer a new approach for it through the lens of some recently studied tools of set-valued stochastic analysis.

Motivation and Literature Review. In incomplete financial markets, given an uncertain claim, one may look for initial endowments that will yield a better terminal payoff than the given claim under all scenarios. Each such endowment is said to superhedge the claim and the superhedging problem aims to find the “cheapest” such endowment. Our focus in this paper is on markets with transaction costs as a particular case of incompleteness, which has been studied in the literature at least for three decades. Among the earliest works, Jouini and Kallal [jouini] studied the absence of arbitrage (or free lunch) and provided a dual characterization of the superhedging price in discrete-time and continuous-time frameworks with multiple underlying assets. Within the same stream of research, Cvitanić and Karatzas [cvi] studied a more concrete model with a single risky asset and a riskless asset in continuous time; one of their main results is a formula for the superhedging price using dual supermartingale measures.

In 1999, Kabanov [Kcurrency] introduced a new framework for multi-asset markets with proportional transaction costs. By considering currency markets as the canonical example of these markets, contingent claims are modeled in terms of *physical units*, hence as random vectors in this framework. The transaction costs are encoded by a so-called *solvency cone*, which consists of portfolio vectors that can be exchanged into portfolios with long positions in all assets. Accordingly, in the superhedging problem, one now looks for the *superhedging set*, i.e., the set of *all* portfolio vectors as initial endowments that can superhedge the claim. In this framework, dual representation theorems for the superhedging set were proved by Kabanov et al. [KabanovRasonyi], Schachermayer [Sch] in discrete time; by Kabanov and Last [KandG], Kabanov and Stricker [KandS], Campi and Schachermayer [Campi] in continuous time under different levels of generality; see also the book by Kabanov and Safarian [KabanovSafarian] for an extensive treatment of the subject.

The superhedging set considered in the references mentioned above is static, i.e., it consists of deterministic portfolio vectors *at time zero*. Naturally, one can also consider a conditional superhedging set at each point in time and obtain a dynamic family of sets of random vectors. This is indeed one of the prominent examples of dynamic *set-valued risk measures* in discrete time as studied by Feinstein and Rudloff [FR13]. A key feature of these sets is that they satisfy a set-valued backward recursion, also called *multi-portfolio time-consistency*. Thanks to this property, as shown in [lohnerudloff], it is possible calculate these sets by a sequence of vector optimization problems when the underlying probability space is finite. More recently, the dynamic superhedging problem in discrete time is revisited in [araratfeinstein], where dynamic set-valued risk measures with multi-portfolio time-consistency, with superhedging sets being an example, are characterized as both the reachable sets of stochastic difference inclusions and the solutions of set-valued backward stochastic difference equations.

In continuous time, beyond trivial cases, it is an open problem to characterize set-valued dynamic risk measures in terms of backward stochastic differential structures such as inclusions and set-valued equations. One of the major obstacles in having such a characterization is that the literature on set-valued stochastic analysis largely focuses on *forward* differential structures with *bounded* sets (cf. [K, MK]). Forwardness makes the stochastic analysis easier, e.g., it avoids issues related to the stochastic integral representation of set-valued martingales; see [amw] for a recent well-posedness result for backward stochastic differential equations with bounded sets. Boundedness makes the set-valued analysis easier due to the convenient framework provided by the Hausdorff metric; see [AlMa] for a recent well-posedness of forward set-valued stochastic differential equations with unbounded sets having a special structure. More seriously, it is not clear what the limiting nature of the difference inclusions and set-valued difference equations in [araratfeinstein] should be when one passes to continuous time.

In addition to the technical issues discussed above for a general treatment, there are not many examples of dynamic set-valued risk measures in continuous time. To the best of our knowledge, the dynamic set-valued entropic risk measure studied in [FR2015, Section 6.2] is the only set-valued risk measure in continuous time that is multi-portfolio time-consistent beyond the conditional expectation-based risk measure. However, both risk measures are known to reduce down to vector-valued dynamic functionals, hence they do not possess any challenging features of the set-valued case.

Main Contributions. In this paper, we construct a family of superhedging sets as an example of a dynamic set-valued risk measure in continuous time. To keep the technical complications at a minimum, we consider a multi-asset generalized Black-Scholes model under proportional transaction costs. In particular, this model generalizes the one in [cvi] with a single risky asset. In this model, we provide a detailed description of the *solvency cone*. As pointed out in various works on superhedging (cf., e.g., [Campi, KandG, KabanovSafarian]), the definition of an admissible trading strategy is not as straightforward as in discrete time but one can work with processes of bounded variation whose Radon-Nikodym derivative with respect to the total variation takes values in the solvency cone, hence jointly allowing for continuous and impulse trading. By taking advantage of our Black-Scholes-type model, we consider the simpler class of instantaneous trading schemes that are absolutely continuous with respect to the Lebesgue measure with a Radon-Nikodym derivative taking values in the solvency cone. This enables us to make more detailed calculations using Itô formula at the vector-valued level and express the corresponding superhedging sets in terms of set-valued integrals. With these, we are able to prove that the superhedging sets form a dynamic set-valued risk measure that is multi-portfolio time-consistent. Hence, we obtain an example that is truly set-valued and is defined on a concrete market model.

More importantly, we show that the superhedging sets, as subsets of 𝕃2\mathbb{L}^{2} spaces indexed by time, are related by a recursive relation that can be seen as a set-valued Bellman’s principle, which has
been key to analyze some multivariate dynamic problems in the recent literature. We refer the reader to [kovacova] for the mean-risk problem in discrete time, to [karnam2017dynamic] for controlled multi-dimensional backward stochastic differential equations, to [dynamicgames] for dynamic games in discrete and continuous time, and to [meanfield] for mean field games in continuous time.

Finally, by exploiting the decomposability of the superhedging sets in 𝕃2\mathbb{L}^{2}, we associate a set-valued stochastic process to the family of superhedging sets of a fixed multidimensional claim XX. However, as observed in earlier works dealing with multivariate dynamic programming in continuous time (cf. [dynamicgames, meanfield]) in game-theoretic settings, establishing a dynamic programming principle for such set-valued process seems to be a tall task. Instead, we will transfer the problem formulation to a path-space setting and introduce approximate versions of superhedging that will involve relaxing 1) the superhedging inequality, 2) the superhedging probability, and 3) the solvency requirement for the superhedging strategy with a predetermined error level ε>0\varepsilon>0. In this more technical framework, we will be able to relate the approximate superhedging sets at different times by means of a set-valued Bellman’s principle. We conjecture that this principle can be used to obtain a set-valued differential structure that characterizes the superhedging sets. We leave this for future research as it requires a new set of analytical tools, such as set-valued differentiation or a set-valued Itô formula (e.g., as in [hjb]), to be combined with Bellman’s principle.

Our contributions can be summarized as follows:

* •

  We provide a mathematically tractable formulation of the superhedging problem in continuous time using solvency cones and instantaneous trading strategies.
* •

  We define superhedging sets as subsets of 𝕃2\mathbb{L}^{2} at different times using the notion of functional set-valued integral. We show that, modulo a sign change, these sets form a multi-portfolio time-consistent dynamic set-valued coherent risk measure. As a consequence of multi-portfolio time-consistency, we prove that a *functional* set-valued dynamic programming principle holds for the superhedging sets.
* •

  We prove a *pathwise/local* version of the set-valued dynamic programming principle by introducing a formulation of the superhedging problem on the path space. This formulation is the continuous-time analog of the tree-based local formulation in discrete time studied in [araratfeinstein].

The rest of this paper is organized as follows. In Section [2](https://arxiv.org/html/2511.18169v1#S2 "2 Preliminaries ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), we recall some basic definitions of set-valued analysis, set-valued risk measures, and the superhedging problem in discrete time. In Section [3](https://arxiv.org/html/2511.18169v1#S3 "3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), we introduce the multi-asset Black-Scholes-type market model together with its solvency cone, trading strategies, and portfolio processes. For completeness, we also study the dual of the solvency cone and its connection to consistent price processes. This is followed by two main sections on the superhedging problem in continuous time. In Section [4](https://arxiv.org/html/2511.18169v1#S4 "4 Functional Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), we investigate the functional formulation of the superhedging sets as subsets of the 𝕃2\mathbb{L}^{2} space and study their collection as a dynamic set-valued risk measure. In Section [5](https://arxiv.org/html/2511.18169v1#S5 "5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), we formulate superhedging sets as set-valued random variables on the canonical path space and prove a dynamic programming principle for these sets that holds pathwise.

## 2 Preliminaries

In this section, we set up the notation for the rest of the paper and recall some basic concepts about set-valued random variables and set-valued dynamic risk measures, with a final emphasis on the superhedging problem in discrete time.

Let 𝕏\mathbb{X} be a separable real Banach space with norm |⋅||\cdot|. We equip 𝕏\mathbb{X} with its Borel σ\sigma-field. For a set A⊆𝕏A\subseteq\mathbb{X}, we write cl𝕏​(A)\mbox{\rm cl}\_{\mathbb{X}}(A), co​(A)\mbox{\rm co}(A), co¯​(A)\overline{\mbox{\rm co}}(A) for the closure, convex hull, closed convex hull of AA. We denote 𝔹𝕏​(ε)\mathbb{B}\_{\mathbb{X}}(\varepsilon) to be the closed norm ball in 𝕏\mathbb{X} centered at the origin with radius ε≥0\varepsilon\geq 0. When 𝕏=ℝd\mathbb{X}=\mathbb{R}^{d} is the Euclidean space with d∈ℕ:={1,2,…}d\in\mathbb{N}:=\{1,2,\ldots\}, we assume that |⋅||\cdot| is the ℓ2\ell\_{2}-norm and we write cl​(A)=clℝd​(A)\mbox{\rm cl}(A)=\mbox{\rm cl}\_{\mathbb{R}^{d}}(A) for a set A⊆𝕏A\subseteq\mathbb{X}. We denote 𝒞​(𝕏),𝒢​(𝕏)\mathscr{C}(\mathbb{X}),\mathscr{G}(\mathbb{X}) to be the families of all closed, closed convex nonempty subsets of 𝕏\mathbb{X}, respectively. For nonempty sets A,B⊆𝕏A,B\subseteq\mathbb{X} and λ∈ℝ\lambda\in\mathbb{R}, we define the usual Minkowski (elementwise) addition and multiplication by scalars by

|  |  |  |
| --- | --- | --- |
|  | A+B:={x+y:x∈A,y∈B},λ​A:={λ​x:x∈A};A+B:=\{x+y\colon x\in A,\ y\in B\},\quad\lambda A:=\{\lambda x\colon x\in A\}; |  |

we simply write A+y=A+{y}A+y=A+\{y\} for y∈𝕏y\in\mathbb{X}. We endow 𝒞​(𝕏)\mathscr{C}(\mathbb{X}) with the Hausdorff distance hh: for A,B∈𝒞​(𝕏)A,B\in\mathscr{C}(\mathbb{X}), we define

|  |  |  |
| --- | --- | --- |
|  | h​(A,B):=max⁡{h¯​(A,B),h¯​(B,A)}=inf{ε>0:A⊆B+𝔹𝕏​(ε),B⊆A+𝔹𝕏​(ε)},h(A,B):=\max\{\overline{h}(A,B),\overline{h}(B,A)\}=\inf\{\varepsilon>0:A\subseteq B+\mathbb{B}\_{\mathbb{X}}(\varepsilon),~B\subseteq A+\mathbb{B}\_{\mathbb{X}}(\varepsilon)\}, |  |

where h¯​(A,B):=sup{d​(x,B):x∈A}\overline{h}(A,B):=\sup\{d(x,B)\colon x\in A\} and d(x,B):=inf{|x−y|:y∈B}d(x,B):=\inf\{|x-y|\colon y\in B\}. It is well-known that (𝒞​(𝕏),h)(\mathscr{C}(\mathbb{X}),h) is a complete metric space, allowing the value +∞+\infty for the metric hh.

Set-Valued Stochastic Analysis. We recall some concepts in set-valued stochastic analysis, referring the reader to the well-known books [K, MK] and the previous work [AlMa] for more details. To that end, let (Ω,ℰ,μ)(\Omega,\mathscr{E},\mu) be a finite measure space and denote 𝕃ℰ0​(Ω,ℝd)\mathbb{L}^{0}\_{\mathscr{E}}(\Omega,\mathbb{R}^{d}) to be the space of all ℰ\mathscr{E}-measurable functions f:Ω→ℝdf\colon\Omega\to\mathbb{R}^{d} distinguished up to μ\mu-almost everywhere (μ\mu-a.e.) equality. A *set-valued function* F:Ω→𝒞​(ℝd)F\colon\Omega\rightarrow\mathscr{C}(\mathbb{R}^{d}) is said to be *measurable* if, for each A∈𝒞​(ℝd)A\in\mathscr{C}(\mathbb{R}^{d}), it holds that {ω∈Ω:F​(ω)∩A≠∅}∈ℰ\{\omega\in\Omega\colon F(\omega)\cap A\neq\emptyset\}\in\mathscr{E}; we denote ℒℰ0​(Ω,𝒞​(ℝd))\mathscr{L}\_{\mathscr{E}}^{0}(\Omega,\mathscr{C}(\mathbb{R}^{d})) to be the set of all such functions distinguished up to μ\mu-a.e. equality.
A function f∈𝕃ℰ0​(Ω,ℝd)f\in\mathbb{L}^{0}\_{\mathscr{E}}(\Omega,\mathbb{R}^{d}) is called a selector for FF if f​(ω)∈F​(ω)f(\omega)\in F(\omega) for μ\mu-a.e. ω∈Ω\omega\in\Omega. We denote the set of all ℰ\mathscr{E}-measurable selectors of FF by 𝕊ℰ0​(F)\mathbb{S}^{0}\_{\mathscr{E}}(F). Then, it follows from the standard measurable selection theorem that 𝕊ℰ0​(F)≠∅\mathbb{S}^{0}\_{\mathscr{E}}(F)\neq\emptyset whenever FF is measurable. Moreover, the following Castaing Representation is useful (cf. [MK]):
The set-valued function FF is measurable if and only if there exists a sequence (fn)n∈ℕ(f\_{n})\_{n\in\mathbb{N}} in 𝕃ℰ0​(Ω,ℝd)\mathbb{L}^{0}\_{\mathscr{E}}(\Omega,\mathbb{R}^{d}) such that F​(ω)=cl​{fn​(ω):n∈ℕ}F(\omega)=\mbox{\rm cl}\{f\_{n}(\omega)\colon n\in\mathbb{N}\} for μ\mu-a.e. ω∈Ω\omega\in\Omega.

For p∈[1,+∞]p\in[1,+\infty], let 𝕃ℰp​(Ω,ℝd)=𝕃p\mathbb{L}\_{\mathscr{E}}^{p}(\Omega,\mathbb{R}^{d})=\mathbb{L}^{p} denote the space of all f∈𝕃ℰ0​(Ω,ℝd)f\in\mathbb{L}\_{\mathscr{E}}^{0}(\Omega,\mathbb{R}^{d}) such that ‖f‖p:=(∫Ω|f​(ω)|p​μ​(d​ω))1/p<∞\|f\|\_{p}:=(\int\_{\Omega}|f(\omega)|^{p}\mu(d\omega))^{1/p}<\infty when p∈[1,+∞)p\in[1,+\infty) and ‖f‖∞:=inf{λ>0:ℙ​{|f|≤λ}=1}<+∞\|f\|\_{\infty}:=\inf\{\lambda>0\colon\mathbb{P}\{|f|\leq\lambda\}=1\}<+\infty when p=+∞p=+\infty. For a function
F∈ℒℰ0​(Ω,𝒞​(ℝd))F\in\mathscr{L}^{0}\_{\mathscr{E}}(\Omega,\mathscr{C}(\mathbb{R}^{d})), we define 𝕊ℰp​(F):=𝕊ℰ0​(F)∩𝕃ℰp​(Ω,ℝd)\mathbb{S}^{p}\_{\mathscr{E}}(F):=\mathbb{S}^{0}\_{\mathscr{E}}(F)\cap\mathbb{L}^{p}\_{\mathscr{E}}(\Omega,\mathbb{R}^{d}) and say that FF is pp-integrable if 𝕊ℰp​(F)≠∅\mathbb{S}^{p}\_{\mathscr{E}}(F)\neq\emptyset. We denote 𝒜ℰp​(Ω,𝒞​(ℝd))\mathscr{A}^{p}\_{\mathscr{E}}(\Omega,\mathscr{C}(\mathbb{R}^{d})) to be the set of all
pp-integrable 𝒞​(ℝd)\mathscr{C}(\mathbb{R}^{d})-valued functions.

An important concept in set-valued analysis is the so-called decomposibility. To be more precise, given a sub-σ\sigma-field ℋ⊆ℰ\mathscr{H}\subseteq\mathscr{E}, a set M⊆𝕃ℰ0​(Ω,ℝd)M\subseteq\mathbb{L}^{0}\_{\mathscr{E}}(\Omega,\mathbb{R}^{d}) is said to be *ℋ\mathscr{H}-decomposable* if 𝟏A​f+𝟏Ac​g∈M{\bf 1}\_{A}f+{\bf 1}\_{A^{c}}g\in M whenever f,g∈Mf,g\in M and A∈ℋA\in\mathscr{H}; here, 𝟏A​(ω):=1{\bf 1}\_{A}(\omega):=1 if ω∈A\omega\in A and 𝟏A​(ω)=0{\bf 1}\_{A}(\omega)=0 if ω∈Ac\omega\in A^{c}. For a set M⊆𝕃ℰ0​(Ω,ℝd)M\subseteq\mathbb{L}^{0}\_{\mathscr{E}}(\Omega,\mathbb{R}^{d}), we define the ℋ\mathscr{H}-decomposable hull of MM, denoted by decℋ⁡(M)\operatorname{dec}\_{\mathscr{H}}(M), to be the smallest ℋ\mathscr{H}-decomposable superset of MM in 𝕃ℰ0​(Ω,ℝd)\mathbb{L}^{0}\_{\mathscr{E}}(\Omega,\mathbb{R}^{d}). When M⊆𝕃ℰp​(Ω,ℝd)M\subseteq\mathbb{L}^{p}\_{\mathscr{E}}(\Omega,\mathbb{R}^{d}) with p∈[1,+∞)p\in[1,+\infty), we shall often consider the closed ℋ\mathscr{H}-decomposable hull of MM, denoted by dec¯ℋ​(M):=cl𝕃p​(decℋ⁡(M))\overline{\operatorname{dec}}\_{\mathscr{H}}(M):=\mbox{\rm cl}\_{\mathbb{L}^{p}}(\operatorname{dec}\_{\mathscr{H}}(M)), where the closure is with respect to ∥⋅∥p\|\cdot\|\_{p}. The following theorem is crucial in our discussion below (cf. [MK]).

###### Theorem 2.1.

Let M∈𝒞​(𝕃ℰp​(Ω,ℝd))M\in\mathscr{C}(\mathbb{L}^{p}\_{\mathscr{E}}(\Omega,\mathbb{R}^{d})), where p∈[1,+∞)p\in[1,+\infty). Then, MM is ℋ\mathscr{H}-decomposable if and only if there exists a unique F∈𝒜ℋp​(Ω,𝒞​(ℝd))F\in\mathscr{A}^{p}\_{\mathscr{H}}(\Omega,\mathscr{C}(\mathbb{R}^{d})) such that M=𝕊ℋp​(F)M=\mathbb{S}^{p}\_{\mathscr{H}}(F).

Next, let us consider a complete filtered probability space (Ω,ℱ,ℙ,𝔽=(ℱt)t∈[0,T])(\Omega,\mathcal{F},\mathbb{P},\mathbb{F}=(\mathcal{F}\_{t})\_{t\in[0,T]}), where T>0T>0 is a constant. In this setting, a *set-valued random variable* is meant to be a measurable function Ξ:Ω→𝒞​(ℝd)\Xi\colon\Omega\to\mathscr{C}(\mathbb{R}^{d}) and a *(𝔽\mathbb{F}-adapted) set-valued stochastic process* is defined as a collection Φ=(Φt)t∈[0,T]\Phi=(\Phi\_{t})\_{t\in[0,T]}, where Φt\Phi\_{t} is a (ℱt\mathcal{F}\_{t}-measurable) set-valued random variable for each t∈[0,T]t\in[0,T], which can also be treated as a function Φ:[0,T]×Ω→𝒞​(ℝd)\Phi\colon[0,T]\times\Omega\to\mathscr{C}(\mathbb{R}^{d}). By a slight abuse of notation, we denote the 𝔽\mathbb{F}-progressive σ\sigma-field on [0,T]×Ω[0,T]\times\Omega by 𝔽\mathbb{F}. Accordingly, 𝕃𝔽0​([0,T]×Ω,ℝd)\mathbb{L}^{0}\_{\mathbb{F}}([0,T]\times\Omega,\mathbb{R}^{d}) (ℒ𝔽0​([0,T]×Ω,𝒞​(ℝd))\mathscr{L}^{0}\_{\mathbb{F}}([0,T]\times\Omega,\mathscr{C}(\mathbb{R}^{d}))) denotes the set of all 𝔽\mathbb{F}-progressively measurable ℝd\mathbb{R}^{d}-valued (𝒞​(ℝd)\mathscr{C}(\mathbb{R}^{d})-valued) processes. Given Φ∈ℒ𝔽0​([0,T]×Ω,𝒞​(ℝd))\Phi\in\mathscr{L}^{0}\_{\mathbb{F}}([0,T]\times\Omega,\mathscr{C}(\mathbb{R}^{d})), we denote S𝔽0​(Φ)S^{0}\_{\mathbb{F}}(\Phi) to be the set of all 𝔽\mathbb{F}-progressively measurable selectors of Φ\Phi, which is a nonempty set. For p∈[1,+∞)p\in[1,+\infty), we define 𝕊𝔽p​(Φ):=𝕊𝔽0​(Φ)∩𝕃𝔽p​([0,T]×Ω,ℝd)\mathbb{S}^{p}\_{\mathbb{F}}(\Phi):=\mathbb{S}^{0}\_{\mathbb{F}}(\Phi)\cap\mathbb{L}^{p}\_{\mathbb{F}}([0,T]\times\Omega,\mathbb{R}^{d}) and

|  |  |  |
| --- | --- | --- |
|  | 𝒜𝔽p​([0,T]×Ω,𝒞​(ℝd))={Φ∈ℒ𝔽0​([0,T]×Ω,𝒞​(ℝd))∣𝕊𝔽p​(Φ)≠∅}.\mathscr{A}^{p}\_{\mathbb{F}}([0,T]\times\Omega,\mathscr{C}(\mathbb{R}^{d}))=\{\Phi\in\mathscr{L}^{0}\_{\mathbb{F}}([0,T]\times\Omega,\mathscr{C}(\mathbb{R}^{d}))\mid\mathbb{S}^{p}\_{\mathbb{F}}(\Phi)\neq\emptyset\}. |  |

For a vector-valued process ϕ∈𝕃𝔽p​([0,T]×Ω,ℝd)\phi\in\mathbb{L}^{p}\_{\mathbb{F}}([0,T]\times\Omega,\mathbb{R}^{d}) and 0≤t≤u≤T0\leq t\leq u\leq T, let us define Jt,u​(ϕ):=∫tuϕr​𝑑rJ\_{t,u}(\phi):=\int\_{t}^{u}\phi\_{r}dr. Given Φ∈𝒜𝔽p​([0,T]×Ω,𝒞​(ℝd))\Phi\in\mathscr{A}^{p}\_{\mathbb{F}}([0,T]\times\Omega,\mathscr{C}(\mathbb{R}^{d})), the image of 𝕊𝔽p​(Φ)\mathbb{S}^{p}\_{\mathbb{F}}(\Phi) under Jt,uJ\_{t,u}, i.e., the set

|  |  |  |
| --- | --- | --- |
|  | Jt,u​[𝕊𝔽p​(Φ)]:={∫tuϕr​𝑑r:ϕ∈𝕊𝔽p​(Φ)}⊆𝕃ℱup​(Ω,ℝd)J\_{t,u}[\mathbb{S}^{p}\_{\mathbb{F}}(\Phi)]:=\left\{\int\_{t}^{u}\phi\_{r}dr\colon\phi\in\mathbb{S}^{p}\_{\mathbb{F}}(\Phi)\right\}\subseteq\mathbb{L}^{p}\_{{\cal F}\_{u}}(\Omega,\mathbb{R}^{d}) |  |

is called the *functional set-valued integral* of Φ\Phi over [t,u][t,u]. By
Theorem [2.1](https://arxiv.org/html/2511.18169v1#S2.Thmthm1 "Theorem 2.1. ‣ 2 Preliminaries ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), there exists a unique set-valued random variable ∫tuΦr​𝑑r∈𝒜ℱup​(Ω,𝒞​(ℝd))\int\_{t}^{u}\Phi\_{r}dr\in\mathscr{A}^{p}\_{\mathcal{F}\_{u}}(\Omega,\mathscr{C}(\mathbb{R}^{d})) such that

|  |  |  |
| --- | --- | --- |
|  | 𝕊ℱup​(∫tuΦr​𝑑r)=dec¯ℱu​(Jt,u​[𝕊𝔽p​(Φ)]);\mathbb{S}^{p}\_{\mathcal{F}\_{u}}\left(\int\_{t}^{u}\Phi\_{r}dr\right)=\overline{\operatorname{dec}}\_{\mathcal{F}\_{u}}(J\_{t,u}[\mathbb{S}^{p}\_{\mathbb{F}}(\Phi)]); |  |

we call it the *set-valued Lebesgue integral* of Φ\Phi over [t,u][t,u].

Dynamic Set-Valued Risk Measures. We recall some basic definitions related to dynamic set-valued risk measures; we refer the reader to [FR13, FR2015] for a detailed account of the subject. Let us consider a filtered probability space (Ω,ℱ,ℙ,𝔽=(ℱt)t∈𝕋)(\Omega,{\cal F},\mathbb{P},\mathbb{F}=({\cal F}\_{t})\_{t\in\mathbb{T}}), where we either have 𝕋=[0,T]\mathbb{T}=[0,T] (continuous time) for some T>0T>0 or 𝕋\mathbb{T} is a finite subset of [0,T][0,T] (discrete time). Let us fix p∈[1,+∞]p\in[1,+\infty]; we will use p=2p=2 for the superhedging problem later. Let t∈𝕋t\in\mathbb{T}. For ease of notation, we write 𝕃ℱtp​(A)\mathbb{L}^{p}\_{{\cal F}\_{t}}(A) for the set of all ℱt{\cal F}\_{t}-measurable pp-integrable AA-valued random vectors, where A⊆ℝdA\subseteq\mathbb{R}^{d} is nonempty.
For ξ,η∈𝕃ℱtp​(ℝd)\xi,\eta\in\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d}), we write η≥ξ\eta\geq\xi whenever η−ξ∈𝕃ℱtp​(ℝ+d)\eta-\xi\in\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d}\_{+}). We also define the space of all *upper sets* in 𝕃ℱtp​(ℝd)\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d}) by

|  |  |  |
| --- | --- | --- |
|  | 𝒫+​(𝕃ℱtp​(ℝd)):={M⊆𝕃ℱtp​(ℝd):M=M+𝕃ℱtp​(ℝ+d)},\mathscr{P}\_{+}(\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d})):=\{M\subseteq\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon M=M+\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d}\_{+})\}, |  |

where we assume M+∅=∅+M=∅M+\emptyset=\emptyset+M=\emptyset for each M⊆𝕃ℱtp​(ℝd)M\subseteq\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d}).

###### Definition 2.2.

Let t∈𝕋t\in\mathbb{T}. For a set-valued functional Rt:𝕃ℱTp​(ℝd)→𝒫+​(𝕃ℱtp​(ℝd))R\_{t}\colon\mathbb{L}^{p}\_{{\cal F}\_{T}}(\mathbb{R}^{d})\rightarrow\mathscr{P}\_{+}(\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d})), consider the following properties:

(i) Monotone: Y≥XY\geq X implies Rt​(Y)⊇Rt​(X)R\_{t}(Y)\supseteq R\_{t}(X) for every X,Y∈𝕃ℱTp​(ℝd)X,Y\in\mathbb{L}^{p}\_{{\cal F}\_{T}}(\mathbb{R}^{d}).

(ii) Translative: Rt​(X+ξ)=Rt​(X)−ξR\_{t}(X+\xi)=R\_{t}(X)-\xi for every X∈𝕃ℱTp​(ℝd)X\in\mathbb{L}^{p}\_{{\cal F}\_{T}}(\mathbb{R}^{d}) and ξ∈𝕃ℱtp​(ℝd)\xi\in\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d}).

(iii) Finite at zero: ∅≠Rt​(0)≠𝕃ℱtp​(ℝd)\emptyset\neq R\_{t}(0)\neq\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d}).

(iv) Normalized: Rt​(X)=Rt​(X)+Rt​(0)R\_{t}(X)=R\_{t}(X)+R\_{t}(0) for every X∈𝕃ℱTp​(ℝd)X\in\mathbb{L}^{p}\_{{\cal F}\_{T}}(\mathbb{R}^{d}).

(v) Conditionally convex: Rt​(λ​X+(1−λ)​Y)⊇λ​Rt​(X)+(1−λ)​Rt​(Y)R\_{t}(\lambda X+(1-\lambda)Y)\supseteq\lambda R\_{t}(X)+(1-\lambda)R\_{t}(Y) for every X,Y∈𝕃ℱTp​(ℝd)X,Y\in\mathbb{L}^{p}\_{{\cal F}\_{T}}(\mathbb{R}^{d}) and λ∈𝕃ℱt∞​([0,1])\lambda\in\mathbb{L}^{\infty}\_{{\cal F}\_{t}}([0,1]).

(vi) Conditionally positively homogeneous: Rt​(λ​X)=λ​Rt​(X)R\_{t}(\lambda X)=\lambda R\_{t}(X) for every X∈𝕃ℱtp​(ℝd)X\in\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d}) and λ∈𝕃ℱt∞​(ℝ++)\lambda\in\mathbb{L}^{\infty}\_{{\cal F}\_{t}}(\mathbb{R}\_{++}).

(vii) Closed: graph⁡Rt:={(X,ξ)∈𝕃ℱTp​(ℝd)×𝕃ℱtp​(ℝd):ξ∈Rt​(X)}\operatorname{graph}R\_{t}:=\{(X,\xi)\in\mathbb{L}^{p}\_{{\cal F}\_{T}}(\mathbb{R}^{d})\times\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon\xi\in R\_{t}(X)\} is a closed set in the product topology.

(viii) Decomposable: Rt​(𝟏A​X+𝟏Ac​Y)=𝟏A​Rt​(X)+𝟏Ac​Rt​(Y)R\_{t}({\bf 1}\_{A}X+{\bf 1}\_{A^{c}}Y)={\bf 1}\_{A}R\_{t}(X)+{\bf 1}\_{A^{c}}R\_{t}(Y) for every X,Y∈𝕃ℱTp​(ℝd)X,Y\in\mathbb{L}^{p}\_{{\cal F}\_{T}}(\mathbb{R}^{d}) and A∈ℱtA\in{\cal F}\_{t}.

The functional RtR\_{t} is called a conditional set-valued risk measure at time tt if it satisfies (i), (ii), (iii). In this case, RtR\_{t} is called conditionally coherent if it also satisfies (v), (vi).

A family (Rt)t∈𝕋(R\_{t})\_{t\in\mathbb{T}} is called a (conditionally coherent) dynamic set-valued risk measure if RtR\_{t} is a (conditionally coherent) conditional set-valued risk measure at time tt for each t∈𝕋t\in\mathbb{T}.

The properties in Definition [2.2](https://arxiv.org/html/2511.18169v1#S2.Thmthm2 "Definition 2.2. ‣ 2 Preliminaries ‣ Superhedging under Proportional Transaction Costs in Continuous Time") are the multi-dimensional and set-valued analogs of the properties of conditional risk measures for univariate positions. A noticeable aspect is that a larger set indicates lower risk as there are more portfolios that can be used for risk compensation. In particular, monotonicity indicates that a financial position with larger gains is less risky and conditional convexity reflects the principle that diversification reduces risk. Translativity and positive homogeneity read the same as their univariate counterparts with obvious interpretations. Finiteness at zero ensures that the zero portfolio has at least one risk compensating portfolio and not every portfolio can be used for this purpose. Finally, closedness is a lower semicontinuity property that is essential in obtaining dual representations for convex and coherent risk measures.

###### Remark 2.3.

Let (Rt)t∈𝕋(R\_{t})\_{t\in\mathbb{T}} be a conditionally convex dynamic set-valued risk measure. Let t∈𝕋t\in\mathbb{T} and X∈𝕃ℱTp​(ℝd)X\in\mathbb{L}^{p}\_{{\cal F}\_{T}}(\mathbb{R}^{d}). It can be checked that Rt​(X)R\_{t}(X) is an ℱt{\cal F}\_{t}-decomposable convex set in 𝕃ℱtp​(ℝd)\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d}). In particular, RtR\_{t} maps into the space of all convex upper sets given by

|  |  |  |
| --- | --- | --- |
|  | ℱ+​(𝕃ℱtp​(ℝd)):={M⊆𝕃ℱtp​(ℝd):M=co​(M+𝕃ℱtp​(ℝ+d))}.\mathscr{F}\_{+}(\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d})):=\{M\subseteq\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon M=\mbox{\rm co}(M+\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d}\_{+}))\}. |  |

Moreover, by Theorem [2.1](https://arxiv.org/html/2511.18169v1#S2.Thmthm1 "Theorem 2.1. ‣ 2 Preliminaries ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), there exists a set-valued random variable R~t​(X)∈𝒜ℱtp​(Ω,𝒢​(ℝd))\tilde{R}\_{t}(X)\in\mathscr{A}^{p}\_{{\cal F}\_{t}}(\Omega,\mathscr{G}(\mathbb{R}^{d})) such that

|  |  |  |
| --- | --- | --- |
|  | cl𝕃p​(Rt​(X))=𝕊ℱtp​(R~t​(X)).\mbox{\rm cl}\_{\mathbb{L}^{p}}(R\_{t}(X))=\mathbb{S}^{p}\_{{\cal F}\_{t}}(\tilde{R}\_{t}(X)). |  |

This way, every X∈𝕃ℱTp​(ℝd)X\in\mathbb{L}^{p}\_{{\cal F}\_{T}}(\mathbb{R}^{d}) gives rise to an 𝔽\mathbb{F}-adapted set-valued stochastic process (R~t​(X))t∈𝕋(\tilde{R}\_{t}(X))\_{t\in\mathbb{T}} that determines (cl𝕃p​(Rt​(X)))t∈𝕋(\mbox{\rm cl}\_{\mathbb{L}^{p}}(R\_{t}(X)))\_{t\in\mathbb{T}}.

Given a conditional risk measure RtR\_{t} at time t∈𝕋t\in\mathbb{T}, we define its *acceptance set* by

|  |  |  |
| --- | --- | --- |
|  | At:={X∈𝕃ℱTp​(ℝd):0∈Rt​(X)},A\_{t}:=\{X\in\mathbb{L}^{p}\_{{\cal F}\_{T}}(\mathbb{R}^{d})\colon 0\in R\_{t}(X)\}, |  |

which gives the set of all dd-dimensional financial positions at time tt that are considered acceptable. Then, RtR\_{t} can be recovered from its acceptance set via

|  |  |  |
| --- | --- | --- |
|  | Rt​(X)={ξ∈𝕃ℱtp​(ℝd):X+ξ∈At}R\_{t}(X)=\{\xi\in\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon X+\xi\in A\_{t}\} |  |

for each X∈𝕃ℱtp​(ℝd)X\in\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d}); hence, each ξ∈Rt​(X)\xi\in R\_{t}(X) can be seen as a portfolio at time tt that can be used to compensate the risk of XX. If u∈𝕋u\in\mathbb{T} is such that t≤ut\leq u, then we denote Rt,uR\_{t,u} to be the restriction of RtR\_{t} on the subspace 𝕃ℱup​(ℝd)\mathbb{L}^{p}\_{{\cal F}\_{u}}(\mathbb{R}^{d}), also called a *stepped risk measure*. In this case, the corresponding *stepped acceptance set* is defined by At,u:={η∈𝕃ℱup​(ℝd):0∈Rt​(η)}A\_{t,u}:=\{\eta\in\mathbb{L}^{p}\_{{\cal F}\_{u}}(\mathbb{R}^{d})\colon 0\in R\_{t}(\eta)\} since Rt,u​(η)=Rt​(η)R\_{t,u}(\eta)=R\_{t}(\eta) for every η∈𝕃ℱup​(ℝd)\eta\in\mathbb{L}^{p}\_{{\cal F}\_{u}}(\mathbb{R}^{d}).

A dynamic risk measure (Rt)t∈𝕋(R\_{t})\_{t\in\mathbb{T}} is called *multi-portfolio time-consistent* if, for every t<ut<u in 𝕋\mathbb{T}, X∈𝕃ℱTp​(ℝd)X\in\mathbb{L}^{p}\_{{\cal F}\_{T}}(\mathbb{R}^{d}), and M⊆𝕃ℱTp​(ℝd)M\subseteq\mathbb{L}^{p}\_{{\cal F}\_{T}}(\mathbb{R}^{d}), the following implication holds:

|  |  |  |
| --- | --- | --- |
|  | Ru(X)⊆⋃Y∈MRu(Y)⟹Rt(X)⊆⋃Y∈MRt(Y)=:Rt[M].R\_{u}(X)\subseteq\bigcup\_{Y\in M}R\_{u}(Y)\implies R\_{t}(X)\subseteq\bigcup\_{Y\in M}R\_{t}(Y)=:R\_{t}[M]. |  |

Multi-portfolio time-consistency is the proper extension of time-consistency for set-valued risk measures and it can be characterized by a recursive property as recalled next.

###### Theorem 2.4.

[FR2015, Theorem 2.8] For a normalized dynamic set-valued risk measure (Rt)t∈𝕋(R\_{t})\_{t\in\mathbb{T}} the following are equivalent:

(i) (Rt)t∈𝕋(R\_{t})\_{t\in\mathbb{T}} is multi-portfolio time consistent.

(ii) Rt​(X)=Rt​[−Ru​(X)]R\_{t}(X)=R\_{t}[-R\_{u}(X)] for every t<ut<u in 𝕋\mathbb{T} and X∈𝕃ℱTp​(ℝd)X\in\mathbb{L}^{p}\_{{\cal F}\_{T}}(\mathbb{R}^{d}).

(iii) At=At,u+AuA\_{t}=A\_{t,u}+A\_{u} for every t<ut<u in 𝕋\mathbb{T}.

The Superhedging Problem in Discrete Time. Before formulating our *superhedging problem* in continuous time, we shall first recall its discrete-time counterpart as discussed in [FR13] and [lohnerudloff]. For simplicity, let us assume that T∈ℕT\in\mathbb{N} and take 𝕋={0,…,T}\mathbb{T}=\{0,\ldots,T\} in the setting of the previous subsection. For each t∈𝕋t\in\mathbb{T}, let K^t∈ℒℱt0​(Ω,𝒢​(ℝd))\hat{K}\_{t}\in\mathscr{L}\_{{\cal F}\_{t}}^{0}(\Omega,\mathscr{G}(\mathbb{R}^{d})) be a random convex cone such that ℝ+d⊆K^t​(ω)\mathbb{R}^{d}\_{+}\subseteq\hat{K}\_{t}(\omega) for ℙ\mathbb{P}-a.e. ω∈Ω\omega\in\Omega. We call K^t\hat{K}\_{t} the *solvency cone* at time t∈𝕋t\in\mathbb{T}; each element of 𝕊ℱtp​(K^t)\mathbb{S}^{p}\_{{\cal F}\_{t}}(\hat{K}\_{t}) is a portfolio vector at time tt that can be exchanged into a portfolio vector with long positions in all assets, where p≥1p\geq 1. An ℝd\mathbb{R}^{d}-valued process (V^t)t∈𝕋(\hat{V}\_{t})\_{t\in\mathbb{T}} is said to be a *self-financing portfolio process* if V^t−V^t−1∈𝕊ℱtp​(−K^t)\hat{V}\_{t}-\hat{V}\_{t-1}\in\mathbb{S}^{p}\_{{\cal F}\_{t}}(-\hat{K}\_{t}) for each t∈𝕋t\in\mathbb{T}, where we set V^−1:=0\hat{V}\_{-1}:=0. Then, the set of all terminal values of self-financing and pp-integrable portfolio processes with zero value at time t∈𝕋t\in\mathbb{T} is given by Ct,T:=∑r=tT𝕊ℱrp​(−K^r)C\_{t,T}:=\sum\_{r=t}^{T}\mathbb{S}^{p}\_{{\cal F}\_{r}}(-\hat{K}\_{r}). For a financial position X∈𝕃ℱTp​(ℝd)X\in\mathbb{L}^{p}\_{{\cal F}\_{T}}(\mathbb{R}^{d}), the set of all *superhedging portfolios* of it at time t∈𝕋t\in\mathbb{T} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​H​Pt​(X):={ξ∈𝕃ℱtp​(ℝd):X∈ξ+Ct,T}.\displaystyle SHP\_{t}(X):=\{\xi\in\mathbb{L}^{p}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon X\in\xi+C\_{t,T}\}. |  | (2.1) |

By [FR13, Corollary 5.2], under the robust no-arbitrage condition (see [FR13, Section 5.1] for the precise formulation), the family (Rt)t∈𝕋(R\_{t})\_{t\in\mathbb{T}} defined by Rt​(X):=S​H​Pt​(−X)R\_{t}(X):=SHP\_{t}(-X), for each X∈𝕃ℱTp​(ℝd)X\in\mathbb{L}^{p}\_{{\cal F}\_{T}}(\mathbb{R}^{d}) and t∈𝕋t\in\mathbb{T}, is a normalized, closed, conditionally coherent dynamic set-valued risk measure that is also multi-portfolio time-consistent.

## 3 Solvency Cone and Consistent Prices

In this section, we introduce the continuous-time market model on which we will study the superhedging problem. Specifically, using the notion of a *solvency cone* (cf. [KandS, Sch]), we will consider a generalized Black-Scholes-type model that is a multi-asset version of the model in [cvi].

The Continuous-Time Model.
Let us fix a probability space (Ω,ℱ,ℙ)(\Omega,{\cal F},\mathbb{P}) on which there exists an mm-dimensional standard Brownian motion (Wt)t∈[0,T](W\_{t})\_{t\in[0,T]}, where m∈ℕm\in\mathbb{N} and T>0T>0 is a finite deterministic horizon. Let 𝔽=(ℱt)t∈[0,T]\mathbb{F}=({\cal F}\_{t})\_{t\in[0,T]} be the standard filtration of (Wt)t∈[0,T](W\_{t})\_{t\in[0,T]} augmented by the ℙ\mathbb{P}-null sets of ℱ{\cal F}. In this setting, we consider a financial market that consists of d∈ℕd\in\mathbb{N} assets, where asset 11 is fixed as a *numéraire*. The prices of the assets, quoted in terms of asset 11, are described by a dd-dimensional, strictly positive, 𝔽\mathbb{F}-adapted process (St)t∈[0,T](S\_{t})\_{t\in[0,T]} with St=(St1,…,Std)S\_{t}=(S^{1}\_{t},\ldots,S^{d}\_{t}) for each t∈[0,T]t\in[0,T]. We assume that (St)t∈[0,T](S\_{t})\_{t\in[0,T]} has the following generalized Black-Scholes dynamics with random coefficients:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​St1=rt​St1​d​t,S01=1,d​Sti=bti​Sti​d​t+∑ℓ=1mσti​ℓ​Sti​d​Wtℓ,S0i=s0i>0,i∈[d]∖{1},\displaystyle\left\{\begin{array}[]{lll}\displaystyle dS^{1}\_{t}=r\_{t}S^{1}\_{t}dt,\qquad\qquad S^{1}\_{0}=1,\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \displaystyle dS^{i}\_{t}=b^{i}\_{t}S^{i}\_{t}dt+\sum\_{\ell=1}^{m}\sigma^{i\ell}\_{t}S^{i}\_{t}dW^{\ell}\_{t},~~~S^{i}\_{0}=s\_{0}^{i}>0,\quad i\in[d]\setminus\{1\},\end{array}\right. |  | (3.3) |

where [d]:={1,…,d}[d]:=\{1,\ldots,d\}; (bt)t∈[0,T]=(rt,bt2,…,btd)t∈[0,T](b\_{t})\_{t\in[0,T]}=(r\_{t},b^{2}\_{t},\ldots,b^{d}\_{t})\_{t\in[0,T]} and (σt)t∈[0,T](\sigma\_{t})\_{t\in[0,T]} are
𝔽\mathbb{F}-progressively measurable bounded processes with values in ℝd\mathbb{R}^{d} and ℝd×m\mathbb{R}^{d\times m}, respectively; σ1​ℓ≡0\sigma^{1\ell}\equiv 0 for each ℓ∈[m]\ell\in[m]. In matrix notation, we may rewrite ([3.3](https://arxiv.org/html/2511.18169v1#S3.E3 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=diag⁡(St)​(bt​d​t+σt​d​Wt),S0=s0:=(1,s02,…,s0d),\displaystyle dS\_{t}=\operatorname{diag}(S\_{t})\left(b\_{t}dt+\sigma\_{t}dW\_{t}\right),~~~S\_{0}=s\_{0}:=(1,s\_{0}^{2},\ldots,s\_{0}^{d}), |  | (3.4) |

where, for x∈ℝdx\in\mathbb{R}^{d}, diag⁡(x)\operatorname{diag}(x) denotes the d×dd\times d-matrix whose ithi^{\text{th}} diagonal entry is xix\_{i} for each i∈[d]i\in[d] and all other entries are zero. By the general well-posedness results for stochastic differential equations, the boundedness assumptions on the coefficients guarantee that the above dynamics determine (St)t∈[0,T](S\_{t})\_{t\in[0,T]} uniquely as an 𝔽\mathbb{F}-adapted continuous process with 𝔼​[supt∈[0,T]|St|2]<+∞\mathbb{E}[\sup\_{t\in[0,T]}|S\_{t}|^{2}]<+\infty; see [karatzas, Theorem 5.2.9], for instance. We assume that m=d−1m=d-1 for simplicity.

Transactions Costs and the Solvency Cone. We further assume that asset 11 also plays the role of bank account to be used for the accounting of transaction fees, which we now describe. Let i,j∈[d]i,j\in[d] and suppose that the market allows transferring funds from asset ii to asset jj. In case of such a transfer, a transaction fee has to be deducted from the bank account according to a given *deterministic* proportion μi​j∈[0,1)\mu^{ij}\in[0,1). We assume that μi​i=0\mu^{ii}=0 and, for every k∈[d]k\in[d],

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1+μi​j)≤(1+μi​k)​(1+μk​j),\displaystyle(1+\mu^{ij})\leq(1+\mu^{ik})(1+\mu^{kj}), |  | (3.5) |

i.e., an indirect transfer through a third asset never reduces the incurred transaction cost.

In this market model, we describe trading strategies via cumulative fund transfers between assets. Let i,j∈[d]i,j\in[d]. We denote by Lti​jL^{ij}\_{t} the net cumulative amount of funds, quoted in asset 11, that is transferred from asset ii to asset jj during [0,t][0,t], where t∈[0,T]t\in[0,T].
We assume that Li​j=(Lti​j)t∈[0,T]L^{ij}=(L^{ij}\_{t})\_{t\in[0,T]} is an 𝔽\mathbb{F}-adapted, càdlàg (right-continuous and left-limited), nondecreasing process such that L0i​j=0L^{ij}\_{0}=0. Naturally, we assume that Li​i≡0L^{ii}\equiv 0.
Then, given an initial position V0=v:=(v1,…,vd)∈ℝdV\_{0}=v:=(v^{1},\ldots,v^{d})\in\mathbb{R}^{d}, a dd-dimensional process (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]}, quoted in asset 11, is called a self-financing portfolio process if it has the following dynamics for some trading strategy (Li​j)i,j∈[d](L^{ij})\_{i,j\in[d]}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Vt1=Vt1​rt​d​t−∑j=2d(1+μ1​j)​d​Lt1​j+∑j=2d(1−μj​1)​d​Ltj​1−∑i=2d∑j=2dμi​j​d​Lti​j,d​Vti=Vti​bti​d​t+∑ℓ=1mVti​σti​ℓ​d​Wtℓ+∑j=1d(d​Ltj​i−d​Lti​j),i∈[d]∖{1}.\displaystyle\left\{\begin{array}[]{lll}\displaystyle dV^{1}\_{t}=V^{1}\_{t}r\_{t}dt-\sum\_{j=2}^{d}(1+\mu^{1j})dL^{1j}\_{t}+\sum\_{j=2}^{d}(1-\mu^{j1})dL^{j1}\_{t}-\sum\_{i=2}^{d}\sum\_{j=2}^{d}\mu^{ij}dL^{ij}\_{t},\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \displaystyle dV^{i}\_{t}=V^{i}\_{t}b^{i}\_{t}dt+\sum\_{\ell=1}^{m}V^{i}\_{t}\sigma^{i\ell}\_{t}dW^{\ell}\_{t}+\sum\_{j=1}^{d}(dL^{ji}\_{t}-dL^{ij}\_{t}),\quad i\in[d]\setminus\{1\}.\end{array}\right. |  | (3.8) |

We remark that, in ([3.8](https://arxiv.org/html/2511.18169v1#S3.E8 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), the terms involving the funds Lj​1L^{j1} are transferred from assets jj, therefore they are subject to the transaction fees.

In light of the notion of solvency cone by [Kcurrency, KandS, Sch] and a 2-dimensional special case studied in [AlMa], we now construct a deterministic solvency cone in ℝd\mathbb{R}^{d} based on the portfolio dynamics ([3.8](https://arxiv.org/html/2511.18169v1#S3.E8 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")). To begin with, let us define the following *exchange matrix*
in accordance with ([3.8](https://arxiv.org/html/2511.18169v1#S3.E8 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) (in the spirit of a *bid-ask matrix* as in [Sch] but with some negative entries in our setting), noting that μi​i=0\mu^{ii}=0:

|  |  |  |
| --- | --- | --- |
|  | Π=(πi​j)i,j∈[d]:=(11+μ121+μ13⋯1+μ1​d−(1−μ21)0μ23⋯μ2​d−(1−μ31)μ320⋯μ3​d⋮⋮⋮⋱⋮−(1−μd​1)μd​2μd​3⋯0).\displaystyle\Pi=(\pi^{ij})\_{i,j\in[d]}:=\begin{pmatrix}1&1+\mu^{12}&1+\mu^{13}&\cdots&1+\mu^{1d}\\ -(1-\mu^{21})&0&\mu^{23}&\cdots&\mu^{2d}\\ -(1-\mu^{31})&\mu^{32}&0&\cdots&\mu^{3d}\\ \vdots&\vdots&\vdots&\ddots&\vdots\\ -(1-\mu^{d1})&\mu^{d2}&\mu^{d3}&\cdots&0\end{pmatrix}. |  |

Next, given matrices A=(ai​j)i,j∈[d],B=(bi​j)i,j∈[d]∈ℝd×dA=(a^{ij})\_{i,j\in[d]},B=(b^{ij})\_{i,j\in[d]}\in\mathbb{R}^{d\times d}, we define their Frobenius inner product by

|  |  |  |
| --- | --- | --- |
|  | ⟨A,B⟩:=tr ​(A𝖳​B)=∑i=1d∑j=1dai​j​bi​j.\left\langle A,B\right\rangle:=\hbox{\rm tr$\,$}(A^{\mathsf{T}}B)=\sum\_{i=1}^{d}\sum\_{j=1}^{d}a^{ij}b^{ij}. |  |

For each i∈[d]i\in[d], we denote by eie\_{i} the standard ithi^{\text{th}} unit (column) vector in ℝd\mathbb{R}^{d}, we also define Ei:=[ei,…,ei]E\_{i}:=[e\_{i},\ldots,e\_{i}] to be the d×dd\times d matrix whose entries in the ithi^{\text{th}} row are 11 and all other entries are 0. Let us denote 𝕄+d⊂ℝ+d×d\mathbb{M}^{d}\_{+}\subset\mathbb{R}^{d\times d}\_{+} to be the convex cone of all d×dd\times d matrices A=(ai​j)i,j∈[d]A=(a^{ij})\_{i,j\in[d]} with ai​j≥0a^{ij}\geq 0 and ai​i=0a^{ii}=0 for every i,j∈[d]i,j\in[d]. We define the convex cone

|  |  |  |  |
| --- | --- | --- | --- |
|  | K​(Π):={x∈ℝd:x1=⟨A,Π⟩,xi=⟨A−A𝖳,Ei⟩​∀i∈[d]∖{1},A∈𝕄+d},\displaystyle K(\Pi):=\{x\in\mathbb{R}^{d}\colon x^{1}=\left\langle A,\Pi\right\rangle,~x^{i}=\langle A-A^{\mathsf{T}},E\_{i}\rangle\ \forall i\in[d]\setminus\{1\},~A\in\mathbb{M}^{d}\_{+}\}, |  | (3.9) |

and call it the solvency cone associated to the bid-ask matrix Π\Pi.

The following result regarding the solvency cone will be useful for our discussion.

###### Proposition 3.1.

K​(Π)=K​(Π)+ℝ+dK(\Pi)=K(\Pi)+\mathbb{R}^{d}\_{+}.

Proof. Clearly, K​(Π)⊆K​(Π)+ℝ+dK(\Pi)\subseteq K(\Pi)+\mathbb{R}^{d}\_{+}, since 0∈ℝ+d0\in\mathbb{R}^{d}\_{+}. To show that K​(Π)+ℝ+d⊆K​(Π)K(\Pi)+\mathbb{R}^{d}\_{+}\subseteq K(\Pi), let x:=y+αx:=y+\alpha for some y∈K​(Π)y\in K(\Pi) and α∈ℝ+d\alpha\in\mathbb{R}^{d}\_{+}. By ([3.9](https://arxiv.org/html/2511.18169v1#S3.E9 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), there exists some A=(ai​j)i,j∈[d]∈𝕄+dA=(a^{ij})\_{i,j\in[d]}\in\mathbb{M}^{d}\_{+} such that y1=⟨A,Π⟩y^{1}=\left\langle A,\Pi\right\rangle and yi=⟨A−A𝖳,Ei⟩y^{i}=\langle A-A^{\mathsf{T}},E\_{i}\rangle for each i∈[d]∖{1}i\in[d]\setminus\{1\}. Hence,

|  |  |  |
| --- | --- | --- |
|  | {x1−∑j=2da1​j​(1+μ1​j)+∑j=2daj​1​(1−μj​1)−∑i=2d∑j=2dai​j​μi​j=α1,xi+∑j=1d(aj​i−ai​j)=αi,i∈[d]∖{1}.\displaystyle\left\{\begin{array}[]{lll}\displaystyle x^{1}-\sum\_{j=2}^{d}a^{1j}(1+\mu^{1j})+\sum\_{j=2}^{d}a^{j1}(1-\mu^{j1})-\sum\_{i=2}^{d}\sum\_{j=2}^{d}a^{ij}\mu^{ij}=\alpha^{1},\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \displaystyle x^{i}+\sum\_{j=1}^{d}(a^{ji}-a^{ij})=\alpha^{i},~~~i\in[d]\setminus\{1\}.\end{array}\right. |  |

Note that if we can show that α∈K​(Π)\alpha\in K(\Pi) as well,
then we must have x=y+α∈K​(Π)x=y+\alpha\in K(\Pi), since K​(Π)K(\Pi) is a convex cone, proving the claim. It now suffices to show that the following system of algebraic equations has a solution B∈𝕄+dB\in\mathbb{M}^{d}\_{+}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {⟨B,Π⟩=∑j=2db1​j​(1+μ1​j)−∑j=2dbj​1​(1−μj​1)+∑i=2d∑j=2dbi​j​μi​j=α1,⟨B−B𝖳,Ei⟩=∑j=1d(bi​j−bj​i)=αi,i∈[d]∖{1}.\displaystyle\left\{\begin{array}[]{lll}\displaystyle\left\langle B,\Pi\right\rangle=\sum\_{j=2}^{d}b^{1j}(1+\mu^{1j})-\sum\_{j=2}^{d}b^{j1}(1-\mu^{j1})+\sum\_{i=2}^{d}\sum\_{j=2}^{d}b^{ij}\mu^{ij}=\alpha^{1},\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \displaystyle\langle B-B^{\mathsf{T}},E\_{i}\rangle=\sum\_{j=1}^{d}(b^{ij}-b^{ji})=\alpha^{i},~~~i\in[d]\setminus\{1\}.\end{array}\right. |  | (3.13) |

To this end, since all diagonal entries of a matrix in 𝕄+d\mathbb{M}^{d}\_{+} are zero, we can embed the cone 𝕄+d\mathbb{M}^{d}\_{+} into ℝ+d​(d−1)\mathbb{R}^{d(d-1)}\_{+} by the mapping 𝕄+d∋B↦𝐢B∈ℝ+d​(d−1)\mathbb{M}^{d}\_{+}\ni B\mapsto{\bf i}\_{B}\in\mathbb{R}^{d(d-1)}\_{+} defined by

|  |  |  |
| --- | --- | --- |
|  | 𝐢B:=(b12,…,b1​d;b21,…,bd​1;b23,b24,…,bd​(d−2)​bd​(d−1))𝖳∈ℝ+d​(d−1).{\bf i}\_{B}:=\big(b^{12},\ldots,b^{1d};b^{21},\ldots,b^{d1};b^{23},b^{24},\ldots,b^{d(d-2)}b^{d(d-1)}\big)^{\mathsf{T}}\in\mathbb{R}^{d(d-1)}\_{+}. |  |

We can then rewrite the linear system ([3.13](https://arxiv.org/html/2511.18169v1#S3.E13 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) in the usual form

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(Π)​𝐢B=α,\displaystyle C(\Pi){\bf i}\_{B}=\alpha, |  | (3.14) |

where C​(Π)C(\Pi) is the coefficient matrix of ([3.13](https://arxiv.org/html/2511.18169v1#S3.E13 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), that is,

|  |  |  |
| --- | --- | --- |
|  | C​(Π)=(1+μ12⋯1+μ1​d−(1−μ21)⋯−(1−μd​1)μ23μ24⋯μd​(d−2)μd​(d−1)−1⋯01⋯011⋯00⋮⋱⋮⋮⋱⋮⋮⋮⋮⋮0⋯−10⋯100⋯−1−1).C(\Pi)=\setcounter{MaxMatrixCols}{11}\begin{pmatrix}1+\mu^{12}&\cdots&1+\mu^{1d}&\negthinspace-(1-\mu^{21})&\cdots&\negthinspace-(1-\mu^{d1})&\mu^{23}&\mu^{24}&\cdots&\mu^{d(d-2)}&\mu^{d(d-1)}\\ -1&\cdots&0&1&\cdots&0&1&1&\cdots&0&0\\ \vdots&\ddots&\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&&\vdots&\vdots\\ 0&\cdots&-1&0&\cdots&1&0&0&\cdots&-1&-1\end{pmatrix}. |  |

Now let us look at the following dual algebraic problem: find y∈ℝdy\in\mathbb{R}^{d} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(Π)𝖳​y∈ℝ+d​(d−1),α𝖳​y<0.\displaystyle C(\Pi)^{\mathsf{T}}y\in\mathbb{R}^{d(d-1)}\_{+},\qquad\alpha^{\mathsf{T}}y<0. |  | (3.15) |

Writing y=(y1,…,yd)𝖳y=(y^{1},\ldots,y^{d})^{\mathsf{T}}, we see that
C​(Π)𝖳​y∈ℝ+d​(d−1)C(\Pi)^{\mathsf{T}}y\in\mathbb{R}^{d(d-1)}\_{+} implies that (1+μ12)​y1−y2≥0(1+\mu^{12})y^{1}-y^{2}\geq 0 and −(1−μ21)​y1+y2≥0-(1-\mu^{21})y^{1}+y^{2}\geq 0. Thus, (μ12+μ21)​y1≥0(\mu^{12}+\mu^{21})y^{1}\geq 0 and therefore y1≥0y^{1}\geq 0, as μ12+μ21≥0\mu^{12}+\mu^{21}\geq 0. Furthermore, we also have −(1−μj​1)​y1+yj≥0-(1-\mu^{j1})y^{1}+y^{j}\geq 0, whence yj≥(1−μj​1)​y1≥0y^{j}\geq(1-\mu^{j1})y^{1}\geq 0 for every j∈[d]∖{1}j\in[d]\setminus\{1\}. In other words, y∈ℝ+dy\in\mathbb{R}^{d}\_{+}, and consequently, we have α𝖳​y≥0\alpha^{\mathsf{T}}y\geq 0, since α∈ℝ+d\alpha\in\mathbb{R}^{d}\_{+} as well. Therefore, the problem ([3.15](https://arxiv.org/html/2511.18169v1#S3.E15 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) does not have a solution. Now, by Farkas’ lemma (cf., e.g., [rockafellar, p. 201]), the linear algebraic equation
([3.14](https://arxiv.org/html/2511.18169v1#S3.E14 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) must have a solution 𝐢B∈ℝ+d​(d−1){\bf i}\_{B}\in\mathbb{R}^{d(d-1)}\_{+}, or equivalently, the equation ([3.13](https://arxiv.org/html/2511.18169v1#S3.E13 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) has a solution B∈𝕄+dB\in\mathbb{M}^{d}\_{+}, proving the claim K​(Π)+ℝ+d⊆K​(Π)K(\Pi)+\mathbb{R}^{d}\_{+}\subseteq K(\Pi), whence the proposition.

Instantaneous Trading and Self-Financing Portfolios. In what follows, we will restrict ourselves to trading strategies that occur at an instantaneous rate in continuous time. For this purpose, let 𝕌𝔽\mathbb{U}\_{\mathbb{F}} be the set of all (Li​j)i,j∈[d](L^{ij})\_{i,j\in[d]} such that, for each i,j∈[d]i,j\in[d], L0i​j=0L^{ij}\_{0}=0 and

|  |  |  |
| --- | --- | --- |
|  | d​Lti​j=θti​j​d​tdL^{ij}\_{t}=\theta^{ij}\_{t}dt |  |

for some process θi​j∈𝕃𝔽2​([0,T]×Ω,ℝ+)\theta^{ij}\in\mathbb{L}^{2}\_{\mathbb{F}}([0,T]\times\Omega,\mathbb{R}\_{+}), with θi​i≡0\theta^{ii}\equiv 0. The next theorem characterizes self-financing portfolio processes in this setting. To that end, for a dd-dimensional process (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]}, quoted in asset 11, we denote by (V^t)t∈[0,T](\hat{V}\_{t})\_{t\in[0,T]} the corresponding process quoted in physical units, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^t=(Vt1St1,…,VtdStd)𝖳,t∈[0,T].\displaystyle\hat{V}\_{t}=\left(\frac{V\_{t}^{1}}{S\_{t}^{1}},\ldots,\frac{V\_{t}^{d}}{S\_{t}^{d}}\right)^{\mathsf{T}},\quad t\in[0,T]. |  | (3.16) |

We also define a set-valued process K^=(K^t)t∈[0,T]\hat{K}=(\hat{K}\_{t})\_{t\in[0,T]} via

|  |  |  |  |
| --- | --- | --- | --- |
|  | K^t​(ω):={(x1St1​(ω),…,xdStd​(ω)):x∈K​(Π)},(t,ω)∈[0,T]×Ω,\displaystyle\hat{K}\_{t}(\omega):=\left\{\left(\frac{x^{1}}{S\_{t}^{1}(\omega)},\ldots,\frac{x^{d}}{S\_{t}^{d}(\omega)}\right)\colon x\in K(\Pi)\right\},\quad(t,\omega)\in[0,T]\times\Omega, |  | (3.17) |

and the corresponding 𝕃2\mathbb{L}^{2}-space of vector-valued processes in physical units via

|  |  |  |
| --- | --- | --- |
|  | 𝕊^𝔽2​(K^):={k^∈𝕊𝔽0​(K^):diag⁡(S)​k^∈𝕃𝔽2​([0,T]×Ω,ℝd)}.\displaystyle\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}):=\left\{\hat{k}\in\mathbb{S}^{0}\_{\mathbb{F}}(\hat{K})\colon\operatorname{diag}(S)\hat{k}\in\mathbb{L}^{2}\_{\mathbb{F}}([0,T]\times\Omega,\mathbb{R}^{d})\right\}. |  |

###### Remark 3.2.

As a consequence of Itô’s formula, we have (1S1,…,1Sd)∈𝕃𝔽2​([0,T]×Ω,ℝd)(\frac{1}{S^{1}},\ldots,\frac{1}{S^{d}})\in\mathbb{L}^{2}\_{\mathbb{F}}([0,T]\times\Omega,\mathbb{R}^{d}). In particular, the inclusion 𝕊^𝔽2​(K^)⊆𝕊𝔽1​(K^)\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})\subseteq\mathbb{S}^{1}\_{\mathbb{F}}(\hat{K}) holds.

###### Theorem 3.3.

Let (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]} be a dd-dimensional process with v:=V0v:=V\_{0} and v^:=V^0\hat{v}:=\hat{V}\_{0}. Then, the following are equivalent:
  
(i) (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]} is a self-financing portfolio process, i.e., there exists (Li​j)i,j∈[d]∈𝕌𝔽(L^{ij})\_{i,j\in[d]}\in\mathbb{U}\_{\mathbb{F}} such that ([3.8](https://arxiv.org/html/2511.18169v1#S3.E8 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) holds.
  
(ii) There exists Θ∈𝕊𝔽2​(𝕄+d)\Theta\in\mathbb{S}^{2}\_{\mathbb{F}}(\mathbb{M}^{d}\_{+}) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Vt1=(Vt1​rt−⟨Θt,Π⟩)​d​t,d​Vti=Vti​bti​d​t+∑ℓ=1mVti​σti​ℓ​d​Wtℓ−⟨Θt−Θt𝖳,Ei⟩​d​t,i∈[d]∖{1}.\displaystyle\left\{\begin{array}[]{lll}\displaystyle dV^{1}\_{t}=(V^{1}\_{t}r\_{t}-\left\langle\Theta\_{t},\Pi\right\rangle)dt,\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \displaystyle dV^{i}\_{t}=V^{i}\_{t}b^{i}\_{t}dt+\sum\_{\ell=1}^{m}V\_{t}^{i}\sigma^{i\ell}\_{t}dW^{\ell}\_{t}-\langle\Theta\_{t}-\Theta\_{t}^{\mathsf{T}},E\_{i}\rangle dt,~~~i\in[d]\setminus\{1\}.\end{array}\right. |  | (3.20) |

(iii) There exists k∈𝕊𝔽2​(K​(Π))k\in\mathbb{S}^{2}\_{\mathbb{F}}(K(\Pi)) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Vt1=(Vt1​rt−kt1)​d​t,d​Vti=Vti​bti​d​t+∑ℓ=1mVti​σti​ℓ​d​Wtℓ−kti​d​t,i∈[d]∖{1}.\displaystyle\left\{\begin{array}[]{lll}\displaystyle dV^{1}\_{t}=(V^{1}\_{t}r\_{t}-k\_{t}^{1})dt,\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \displaystyle dV^{i}\_{t}=V^{i}\_{t}b^{i}\_{t}dt+\sum\_{\ell=1}^{m}V\_{t}^{i}\sigma^{i\ell}\_{t}dW^{\ell}\_{t}-k\_{t}^{i}dt,~~~i\in[d]\setminus\{1\}.\end{array}\right. |  | (3.23) |

(iv) (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]} satisfies, for each t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt∈v+∫0tdiag⁡(Vs)​bs​𝑑s−J0,t​[𝕊𝔽2​(K​(Π))]+∫0tdiag⁡(Vs)​σs​𝑑Ws.\displaystyle V\_{t}\in v+\int\_{0}^{t}\operatorname{diag}(V\_{s})b\_{s}ds-J\_{0,t}[\mathbb{S}^{2}\_{\mathbb{F}}(K(\Pi))]+\int\_{0}^{t}\operatorname{diag}(V\_{s})\sigma\_{s}dW\_{s}. |  | (3.24) |

(v) (V^t)t∈[0,T](\hat{V}\_{t})\_{t\in[0,T]} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt^∈v^+J0,t​[𝕊^𝔽2​(−K^)],t∈[0,T].\displaystyle\hat{V\_{t}}\in\hat{v}+J\_{0,t}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(-\hat{K})],~~~~~~t\in[0,T]. |  | (3.25) |

In this case, (V^t)t∈[0,T](\hat{V}\_{t})\_{t\in[0,T]} also satisfies

|  |  |  |
| --- | --- | --- |
|  | V^t∈v^+∫0t(−K^s)dsa.s.t∈[0,T].\hat{V}\_{t}\in\hat{v}+\int\_{0}^{t}(-\hat{K}\_{s})ds\quad a.s.~~~~~~t\in[0,T]. |  |

Proof. (i) ⇔\Leftrightarrow (ii): Suppose that there exists some (Li​j)i,j∈[d]∈𝕌𝔽(L^{ij})\_{i,j\in[d]}\in\mathbb{U}\_{\mathbb{F}} such that ([3.8](https://arxiv.org/html/2511.18169v1#S3.E8 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) holds. Then, for each i,j∈[d]i,j\in[d], we can find θi​j∈𝕃𝔽2​([0,T]×Ω,ℝ+)\theta^{ij}\in\mathbb{L}^{2}\_{\mathbb{F}}([0,T]\times\Omega,\mathbb{R}\_{+}) such that d​Lti​j=θti​j​d​tdL\_{t}^{ij}=\theta\_{t}^{ij}dt, where θi​i≡0\theta^{ii}\equiv 0. Hence, ([3.8](https://arxiv.org/html/2511.18169v1#S3.E8 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Vt1=Vt1​rt​d​t−∑j=2d(1+μ1​j)​θt1​j​d​t+∑j=2d(1−μj​1)​θtj​1​d​t−∑i=2d∑j=2dμi​j​θti​j​d​t,d​Vti=Vti​bti​d​t+∑ℓ=1mVti​σti​ℓ​d​Wtℓ+∑j=1d(θtj​i−θti​j)​d​t,i∈[d]∖{1}.\displaystyle\left\{\begin{array}[]{lll}\displaystyle dV^{1}\_{t}=V^{1}\_{t}r\_{t}dt\negthinspace-\negthinspace\sum\_{j=2}^{d}(1+\mu^{1j})\theta^{1j}\_{t}dt+\sum\_{j=2}^{d}(1-\mu^{j1})\theta^{j1}\_{t}dt\negthinspace-\negthinspace\sum\_{i=2}^{d}\sum\_{j=2}^{d}\mu^{ij}\theta^{ij}\_{t}dt,\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \displaystyle dV^{i}\_{t}=V^{i}\_{t}b^{i}\_{t}dt+\sum\_{\ell=1}^{m}V^{i}\_{t}\sigma^{i\ell}\_{t}dW^{\ell}\_{t}+\sum\_{j=1}^{d}(\theta^{ji}\_{t}-\theta^{ij}\_{t})dt,\quad i\in[d]\setminus\{1\}.\end{array}\right. |  | (3.28) |

Defining Θt=(θti​j)i,j∈[d]\Theta\_{t}=(\theta^{ij}\_{t})\_{i,j\in[d]} for each i,j∈[d]i,j\in[d] and t∈[0,T]t\in[0,T], and recalling ([3.13](https://arxiv.org/html/2511.18169v1#S3.E13 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we observe that Θ∈𝕊𝔽2​(𝕄+d)\Theta\in\mathbb{S}^{2}\_{\mathbb{F}}(\mathbb{M}^{d}\_{+}) and ([3.28](https://arxiv.org/html/2511.18169v1#S3.E28 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) can be reformulated as ([3.20](https://arxiv.org/html/2511.18169v1#S3.E20 "In Theorem 3.3. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")). The reverse implication follows similarly.

(ii) ⇔\Leftrightarrow (iii): Suppose that there exists Θ∈𝕊𝔽2​(𝕄+d)\Theta\in\mathbb{S}^{2}\_{\mathbb{F}}(\mathbb{M}^{d}\_{+}) such that ([3.20](https://arxiv.org/html/2511.18169v1#S3.E20 "In Theorem 3.3. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) (equivalently, ([3.28](https://arxiv.org/html/2511.18169v1#S3.E28 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time"))) holds. For each t∈[0,T]t\in[0,T], let us define kt:=(kt1,…,ktd)𝖳k\_{t}:=(k\_{t}^{1},\ldots,k\_{t}^{d})^{\mathsf{T}} by

|  |  |  |
| --- | --- | --- |
|  | kt1:=⟨Θt,Π⟩,kti:=⟨Θ−Θ𝖳,Ei⟩,i∈[d]∖{1}.k\_{t}^{1}:=\left\langle\Theta\_{t},\Pi\right\rangle,\quad k\_{t}^{i}:=\langle\Theta-\Theta^{\mathsf{T}},E\_{i}\rangle,\ i\in[d]\setminus\{1\}. |  |

By the definition of the solvency cone in ([3.9](https://arxiv.org/html/2511.18169v1#S3.E9 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we have k=(kt)t∈[0,T]∈𝕊𝔽2​(K​(Π))k=(k\_{t})\_{t\in[0,T]}\in\mathbb{S}^{2}\_{\mathbb{F}}(K(\Pi)). Moreover, ([3.23](https://arxiv.org/html/2511.18169v1#S3.E23 "In Theorem 3.3. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) follows directly by ([3.28](https://arxiv.org/html/2511.18169v1#S3.E28 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")). The reverse implication follows similarly.

(iii) ⇔\Leftrightarrow (iv): Suppose that there exists k∈𝕊𝔽2​(K​(Π))k\in\mathbb{S}^{2}\_{\mathbb{F}}(K(\Pi)) such that ([3.23](https://arxiv.org/html/2511.18169v1#S3.E23 "In Theorem 3.3. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) holds. Recalling the notation in ([3.4](https://arxiv.org/html/2511.18169v1#S3.E4 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we may rewrite ([3.23](https://arxiv.org/html/2511.18169v1#S3.E23 "In Theorem 3.3. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) as

|  |  |  |
| --- | --- | --- |
|  | d​Vt=(diag⁡(Vt)​bt−kt)​d​t+diag⁡(Vt)​σt​d​Wt.dV\_{t}=(\operatorname{diag}(V\_{t})b\_{t}-k\_{t})dt+\operatorname{diag}(V\_{t})\sigma\_{t}dW\_{t}. |  |

Hence, for each t∈[0,T]t\in[0,T], we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt\displaystyle V\_{t} | =v+∫0tdiag⁡(Vs)​bs​𝑑s−∫0tks​𝑑s+∫0tdiag⁡(Vt)​σt​𝑑Wt\displaystyle=v+\int\_{0}^{t}\operatorname{diag}(V\_{s})b\_{s}ds-\int\_{0}^{t}k\_{s}ds+\int\_{0}^{t}\operatorname{diag}(V\_{t})\sigma\_{t}dW\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∈v+∫0tdiag⁡(Vs)​bs​𝑑s−J0,t​[S𝔽2​(K​(Π))]+∫0tdiag⁡(Vs)​σs​𝑑Ws\displaystyle\in v+\int\_{0}^{t}\operatorname{diag}(V\_{s})b\_{s}ds-J\_{0,t}[S^{2}\_{\mathbb{F}}(K(\Pi))]+\int\_{0}^{t}\operatorname{diag}(V\_{s})\sigma\_{s}dW\_{s} |  |

so that ([3.24](https://arxiv.org/html/2511.18169v1#S3.E24 "In Theorem 3.3. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) holds. The reverse implication follows similarly.

(iii) ⇒\Rightarrow (v): Suppose that there exists k∈𝕊𝔽2​(K​(Π))k\in\mathbb{S}^{2}\_{\mathbb{F}}(K(\Pi)) such that ([3.23](https://arxiv.org/html/2511.18169v1#S3.E23 "In Theorem 3.3. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) holds. By Itô’s formula and using the price dynamics in ([3.3](https://arxiv.org/html/2511.18169v1#S3.E3 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we obtain that (V^t)t∈[0,T](\hat{V}\_{t})\_{t\in[0,T]} has the dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​V^t1=d​(Vt1St1)=1St1​(rt​Vt1−kt1)​d​t−Vt1​(1St1)​rt​d​t=−kt1St1​d​t,d​V^ti=d​(VtiSti)=1Sti​d​Vti+Vti​d​(1Sti)−∑ℓ=1m(σti​ℓ)2​VtiSti​d​t=−ktiSti​d​t,\displaystyle\left\{\begin{array}[]{lll}\displaystyle d\hat{V}^{1}\_{t}=d\Big(\frac{V^{1}\_{t}}{S^{1}\_{t}}\Big)=\frac{1}{S^{1}\_{t}}(r\_{t}V^{1}\_{t}-k^{1}\_{t})dt-V^{1}\_{t}\Big(\frac{1}{S^{1}\_{t}}\Big)r\_{t}dt=-\frac{k\_{t}^{1}}{S^{1}\_{t}}dt,\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \displaystyle d\hat{V}^{i}\_{t}=d\Big(\frac{V^{i}\_{t}}{S^{i}\_{t}}\Big)=\frac{1}{S^{i}\_{t}}dV^{i}\_{t}+V^{i}\_{t}d\Big(\frac{1}{S^{i}\_{t}}\Big)-\frac{\sum\_{\ell=1}^{m}(\sigma^{i\ell}\_{t})^{2}V^{i}\_{t}}{S^{i}\_{t}}dt=-\frac{k\_{t}^{i}}{S^{i}\_{t}}dt,\end{array}\right. |  | (3.31) |

for every i∈[d]∖{1}i\in[d]\setminus\{1\}.

Using the notation in ([3.16](https://arxiv.org/html/2511.18169v1#S3.E16 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we define the process k^\hat{k} corresponding to kk. Then, we have k^∈𝕊^𝔽2​(K^)\hat{k}\in\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}) and ([3.31](https://arxiv.org/html/2511.18169v1#S3.E31 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​V^t=−k^t​d​t,\displaystyle d\hat{V}\_{t}=-\hat{k}\_{t}dt, |  | (3.32) |

which implies that ([3.25](https://arxiv.org/html/2511.18169v1#S3.E25 "In Theorem 3.3. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) holds.

(v) ⇒\Rightarrow (iii): Suppose that (V^t)t∈[0,T](\hat{V}\_{t})\_{t\in[0,T]} satisfies ([3.25](https://arxiv.org/html/2511.18169v1#S3.E25 "In Theorem 3.3. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")). Hence, there exists k^∈𝕊^𝔽2​(K^)\hat{k}\in\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}) such that ([3.32](https://arxiv.org/html/2511.18169v1#S3.E32 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) holds. Then, by Itô’s formula and ([3.3](https://arxiv.org/html/2511.18169v1#S3.E3 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we obtain

|  |  |  |
| --- | --- | --- |
|  | {d​Vt1=d​(V^t1​St1)=V^t1​d​St1+St1​d​V^t1=Vt1​rt​d​t−kt1​d​t,d​Vti=d​(V^ti​Sti)=V^ti​d​Sti+Sti​d​V^ti+(d​Sti)​(d​V^ti)=Vti​bti​d​t+∑ℓ=1mVti​σti​ℓ​d​Wtℓ−kti​d​t,\left\{\begin{array}[]{lll}\displaystyle dV^{1}\_{t}=d(\hat{V}^{1}\_{t}S^{1}\_{t})=\hat{V}\_{t}^{1}dS\_{t}^{1}+S\_{t}^{1}d\hat{V}\_{t}^{1}=V\_{t}^{1}r\_{t}dt-k\_{t}^{1}dt,\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \displaystyle dV^{i}\_{t}=d(\hat{V}^{i}\_{t}S^{i}\_{t})=\hat{V}\_{t}^{i}dS\_{t}^{i}+S\_{t}^{i}d\hat{V}\_{t}^{i}+(dS\_{t}^{i})(d\hat{V}\_{t}^{i})=V^{i}\_{t}b^{i}\_{t}dt+\sum\_{\ell=1}^{m}V\_{t}^{i}\sigma^{i\ell}\_{t}dW^{\ell}\_{t}-k\_{t}^{i}dt,\end{array}\right. |  |

for every i∈[d]∖{1}i\in[d]\setminus\{1\}. Hence, (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]} satisfies ([3.23](https://arxiv.org/html/2511.18169v1#S3.E23 "In Theorem 3.3. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")).

The Dual of Solvency Cone and Consistent Price Processes. In the rest of the section, we shall study the set-valued process of the dual cones of K^=(K^t)t∈[0,T]\hat{K}=(\hat{K}\_{t})\_{t\in[0,T]}, and define the so-called consistent pricing processes. To begin with, by Proposition [3.1](https://arxiv.org/html/2511.18169v1#S3.Thmthm1 "Proposition 3.1. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time") and ([3.17](https://arxiv.org/html/2511.18169v1#S3.E17 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), for each (t,ω)∈[0,T]×Ω(t,\omega)\in[0,T]\times\Omega, the cone K^t​(ω)\hat{K}\_{t}(\omega) (in physical units) consists of all x∈ℝdx\in\mathbb{R}^{d} for which

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt1=1St1​(ω)​⟨A,Π⟩,xti=1Sti​(ω)​⟨A−A𝖳,Ei⟩,i∈[d]∖{1}.\displaystyle x^{1}\_{t}=\frac{1}{S^{1}\_{t}(\omega)}\left\langle A,\Pi\right\rangle,\quad x^{i}\_{t}=\frac{1}{S^{i}\_{t}(\omega)}\langle A-A^{\mathsf{T}},E\_{i}\rangle,\ i\in[d]\setminus\{1\}. |  | (3.33) |

holds for some A∈𝕄+dA\in\mathbb{M}^{d}\_{+}. We define the (positive) dual cone of K^t​(ω)\hat{K}\_{t}(\omega) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | K^t+​(ω):={z∈ℝd:z𝖳​x≥0​ for every ​x∈K^t​(ω)}.\displaystyle\hat{K}^{+}\_{t}(\omega):=\{z\in\mathbb{R}^{d}\colon z^{\mathsf{T}}x\geq 0\text{ for every }x\in\hat{K}\_{t}(\omega)\}. |  | (3.34) |

The following proposition shows that the dual cones are in line with the auxiliary martingales introduced for the two-dimensional continuous-time case in [cvi].

###### Proposition 3.4.

Let t∈[0,T]t\in[0,T], ω∈Ω\omega\in\Omega, and z∈ℝdz\in\mathbb{R}^{d}. Then z∈K^t+​(ω)z\in\hat{K}^{+}\_{t}(\omega) if and only if

|  |  |  |
| --- | --- | --- |
|  | (1−μi​1)​z1St1​(ω)≤ziSti​(ω)≤(1+μ1​i)​z1St1​(ω),zjStj​(ω)−ziSti​(ω)≤μi​j​z1St1​(ω),i,j∈[d]∖{1}.\displaystyle(1-\mu^{i1})\frac{z^{1}}{S^{1}\_{t}(\omega)}\leq\frac{z^{i}}{S^{i}\_{t}(\omega)}\leq(1+\mu^{1i})\frac{z^{1}}{S^{1}\_{t}(\omega)},\quad\frac{z^{j}}{S^{j}\_{t}(\omega)}-\frac{z^{i}}{S^{i}\_{t}(\omega)}\leq\mu^{ij}\frac{z^{1}}{S^{1}\_{t}(\omega)},\ i,j\in[d]\setminus\{1\}. |  |

Proof. By ([3.33](https://arxiv.org/html/2511.18169v1#S3.E33 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) and ([3.34](https://arxiv.org/html/2511.18169v1#S3.E34 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we have z∈K^t+​(ω)z\in\hat{K}\_{t}^{+}(\omega) if and only if the following inequality holds for every A=(ai​j)i,j∈[d]∈𝕄+dA=(a^{ij})\_{i,j\in[d]}\in\mathbb{M}^{d}\_{+}:

|  |  |  |
| --- | --- | --- |
|  | z1St1​(ω)​⟨A,Π⟩+∑i=1dziSti​(ω)​⟨A−A𝖳,Ei⟩≥0.\frac{z^{1}}{S\_{t}^{1}(\omega)}\left\langle A,\Pi\right\rangle+\sum\_{i=1}^{d}\frac{z^{i}}{S\_{t}^{i}(\omega)}\langle A-A^{\mathsf{T}},E\_{i}\rangle\geq 0. |  |

Recalling ([3.13](https://arxiv.org/html/2511.18169v1#S3.E13 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) and reorganizing the terms, we may rewrite this inequality as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑j=2dc1​j​(z)​a1​j+∑i=2dci​1​(z)​ai​1+∑i=2d∑j=2dci​j​(z)​ai​j≥0,\displaystyle\sum\_{j=2}^{d}c^{1j}(z)a^{1j}+\sum\_{i=2}^{d}c^{i1}(z)a^{i1}+\sum\_{i=2}^{d}\sum\_{j=2}^{d}c^{ij}(z)a^{ij}\geq 0, |  | (3.35) |

where

|  |  |  |
| --- | --- | --- |
|  | {c1​j​(z):=(1+μ1​j)​z1St1​(ω)−zjStj​(ω),ci​1​(z):=−(1−μi​1)​z1St1​(ω)+ziSti​(ω),ci​j​(z):=μi​j​z1St1​(ω)+ziSti​(ω)−zjStj​(ω)≥0,i,j∈[d]∖{1}.\left\{\begin{array}[]{lll}\displaystyle c^{1j}(z):=(1+\mu^{1j})\frac{z^{1}}{S^{1}\_{t}(\omega)}-\frac{z^{j}}{S^{j}\_{t}(\omega)},\quad c^{i1}(z):=-(1-\mu^{i1})\frac{z^{1}}{S^{1}\_{t}(\omega)}+\frac{z^{i}}{S^{i}\_{t}(\omega)},\quad\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \displaystyle c^{ij}(z):=\mu^{ij}\frac{z^{1}}{S^{1}\_{t}(\omega)}+\frac{z^{i}}{S^{i}\_{t}(\omega)}-\frac{z^{j}}{S^{j}\_{t}(\omega)}\geq 0,\quad i,j\in[d]\setminus\{1\}.\end{array}\right. |  |

Hence, z∈K^t+​(ω)z\in\hat{K}\_{t}^{+}(\omega) if and only if ([3.35](https://arxiv.org/html/2511.18169v1#S3.E35 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) holds for every a1​j,ai​1,ai​j≥0a^{1j},a^{i1},a^{ij}\geq 0 and i,j∈[d]∖{0}i,j\in[d]\setminus\{0\}, or equivalently, the corresponding coefficients are nonnegative, i.e., c1​j​(z)≥0c^{1j}(z)\geq 0, ci​1​(z)≥0c^{i1}(z)\geq 0, ci​j​(z)≥0c^{ij}(z)\geq 0 for every i,j∈[d]∖{1}i,j\in[d]\setminus\{1\}. Therefore, the result follows.

The preceding proposition implies that the nonzero elements of the dual of the solvency cone are always strictly positive.

###### Corollary 3.5.

It holds ℙ​{K^t+∖{0}⊆ℝ++d​ for every ​t∈[0,T]}=1\mathbb{P}\{\hat{K}\_{t}^{+}\setminus\{0\}\subseteq\mathbb{R}^{d}\_{++}\text{ for every }t\in[0,T]\}=1.

Proof. The generalized Black-Scholes dynamics of SS in ([3.3](https://arxiv.org/html/2511.18169v1#S3.E3 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) guarantee that, for some Ω0∈ℱ\Omega\_{0}\in{\cal F} with ℙ​(Ω0)=1\mathbb{P}(\Omega\_{0})=1, we have Sti​(ω)>0S^{i}\_{t}(\omega)>0 for every t∈[0,T]t\in[0,T], i∈[d]i\in[d], and ω∈Ω0\omega\in\Omega\_{0}. Let us fix t∈[0,T]t\in[0,T], ω∈Ω0\omega\in\Omega\_{0} and let z∈K^t+​(ω)∖{0}z\in\hat{K}\_{t}^{+}(\omega)\setminus\{0\}. Suppose that z1=0z^{1}=0. Then, the first inequality in Proposition [3.4](https://arxiv.org/html/2511.18169v1#S3.Thmthm4 "Proposition 3.4. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time") yields zi=0z^{i}=0 for every i∈[d]∖{1}i\in[d]\setminus\{1\} so that z=0z=0, a contradiction. Hence, z1>0z^{1}>0. Let i∈[d]∖{1}i\in[d]\setminus\{1\} and suppose that zi=0z^{i}=0. Then, the same inequality enforces (1−μi​1)​z1St1​(ω)=0(1-\mu^{i1})\frac{z^{1}}{S^{1}\_{t}(\omega)}=0, which yields μi​1=1\mu^{i1}=1 as z1>0z^{1}>0. We get a contradiction to our assumption that μi​1∈[0,1)\mu^{i1}\in[0,1), whence zi>0z^{i}>0. Hence, z∈ℝ++dz\in\mathbb{R}^{d}\_{++}.

Next we introduce the notion of consistent price processes  in an analogous way to its discrete-time counterpart given by Schachermayer [Sch].

###### Definition 3.6.

A process (Zt)t∈[0,T]∈𝕃𝔽1​([0,T]×Ω,ℝd)(Z\_{t})\_{t\in[0,T]}\in\mathbb{L}^{1}\_{\mathbb{F}}([0,T]\times\Omega,\mathbb{R}^{d}) is called a consistent price process for the solvency cone process (K^t)t∈[0,T](\hat{K}\_{t})\_{t\in[0,T]} if ZZ is a ℙ\mathbb{P}-martingale under and ℙ​{Zt∈K^t+∖{0}}=1\mathbb{P}\{Z\_{t}\in\hat{K}^{+}\_{t}\setminus\{0\}\}=1 for each t∈[0,T]t\in[0,T].

In what follows, for a consistent price process (Zt)t∈[0,T](Z\_{t})\_{t\in[0,T]}, we define Rtj:=Z^tjZ^t1R^{j}\_{t}:=\frac{\hat{Z}^{j}\_{t}}{\hat{Z}^{1}\_{t}} for each t∈[0,T]t\in[0,T] and i∈[d]i\in[d].

###### Theorem 3.7.

Let (Zt)t∈[0,T]∈𝕃𝔽1​([0,T]×Ω,ℝd)(Z\_{t})\_{t\in[0,T]}\in\mathbb{L}^{1}\_{\mathbb{F}}([0,T]\times\Omega,\mathbb{R}^{d}) be a consistent price process with Z01=1Z^{1}\_{0}=1. Let (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]} be a self-financing portfolio process as in Proposition [3.3](https://arxiv.org/html/2511.18169v1#S3.Thmthm3 "Theorem 3.3. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time"). Then, the process Mt:=1St1​(Vt1+∑j=2dRtj​Vtj)M\_{t}:=\frac{1}{S^{1}\_{t}}(V^{1}\_{t}+\sum\_{j=2}^{d}R^{j}\_{t}V^{j}\_{t}), t∈[0,T]t\in[0,T], is a ℙ1\mathbb{P}^{1}-supermartingale, where d​ℙ1d​ℙ|ℱT:=ZT1\frac{d\mathbb{P}^{1}}{d\mathbb{P}}\big|\_{{\cal F}\_{T}}:=Z^{1}\_{T}.

Proof. Since we assume that 𝔽\mathbb{F} is the standard Brownian filtration corresponding to WW, the process ZZ has a continuous modification, which we also denote by ZZ with slight abuse of notation. Then, by Corollary [3.5](https://arxiv.org/html/2511.18169v1#S3.Thmthm5 "Corollary 3.5. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), we have Zti>0Z\_{t}^{i}>0 for every t∈[0,T]t\in[0,T] and i∈[d]i\in[d], ℙ\mathbb{P}-a.s. Let us fix i∈[d]i\in[d] and consider the local martingale Yti:=∫0t(Zsi)−1​𝑑ZsiY^{i}\_{t}:=\int\_{0}^{t}(Z^{i}\_{s})^{-1}dZ^{i}\_{s},
t∈[0,T]t\in[0,T]. Then, by the local martingale representation theorem (cf., e.g., [karatzas, Theorem 4.2]), there exists ηi∈𝕃𝔽0​([0,T]×Ω,ℝm)\eta^{i}\in\mathbb{L}^{0}\_{\mathbb{F}}([0,T]\times\Omega,\mathbb{R}^{m}) with ℙ​{∫0T|ηti|2​𝑑t<∞}=1\mathbb{P}\{\int\_{0}^{T}|\eta^{i}\_{t}|^{2}dt<\infty\}=1, such that Yti=∫0t(ηsi)𝖳​𝑑WsY^{i}\_{t}=\int\_{0}^{t}(\eta^{i}\_{s})^{\mathsf{T}}dW\_{s}, t∈[0,T]t\in[0,T], ℙ\mathbb{P}-a.s. In other words, ZiZ^{i} satisfies the linear stochastic differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Zti=Zti​(ηti)𝖳​d​Wt,t∈[0,T].\displaystyle dZ^{i}\_{t}=Z^{i}\_{t}(\eta^{i}\_{t})^{\mathsf{T}}dW\_{t},\qquad t\in[0,T]. |  | (3.36) |

Hence, it can be written as the Doléans-Dade stochastic exponential

|  |  |  |
| --- | --- | --- |
|  | Zti=Z0i​exp⁡(∫0t(ηsi)𝖳​𝑑Ws−12​∫0t|ηsi|2​𝑑s),t∈[0,T].Z^{i}\_{t}=Z^{i}\_{0}\exp\left(\int\_{0}^{t}(\eta^{i}\_{s})^{\mathsf{T}}dW\_{s}-\frac{1}{2}\int\_{0}^{t}|\eta^{i}\_{s}|^{2}ds\right),\qquad t\in[0,T]. |  |

Next, note that Z01=1Z^{1}\_{0}=1, d​ℙ1d​ℙ|ℱT=ZT1\frac{d\mathbb{P}^{1}}{d\mathbb{P}}\big|\_{{\cal F}\_{T}}=Z^{1}\_{T} defines a new probability measure ℙ1\mathbb{P}^{1}. Then, by Girsanov Theorem, under ℙ1\mathbb{P}^{1}, Wt1=Wt−∫0tηs1​𝑑sW^{1}\_{t}=W\_{t}-\int\_{0}^{t}\eta^{1}\_{s}ds, t∈[0,T]t\in[0,T], is a Brownian motion. Furthermore, it is easy to check that for any 𝔽\mathbb{F}-adapted process M=(Mt)t∈[0,T]M=(M\_{t})\_{t\in[0,T]}, MM is
a ℙ1\mathbb{P}^{1}-supermartingale if and only if Z1​M=(Zt1​Mt)t∈[0,T]Z^{1}M=(Z^{1}\_{t}M\_{t})\_{t\in[0,T]} is a ℙ\mathbb{P}-supermartingale.

Let (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]} be a self-financing portfolio process as in Theorem [3.3](https://arxiv.org/html/2511.18169v1#S3.Thmthm3 "Theorem 3.3. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time") and consider its physical units form V^\hat{V} defined by ([3.16](https://arxiv.org/html/2511.18169v1#S3.E16 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")). Since, by definition, Rtj=Z^tjZ^t1=ZtjZt1​St1StjR^{j}\_{t}=\frac{\hat{Z}^{j}\_{t}}{\hat{Z}^{1}\_{t}}=\frac{Z^{j}\_{t}}{Z^{1}\_{t}}\frac{S^{1}\_{t}}{S^{j}\_{t}}, we see that

|  |  |  |
| --- | --- | --- |
|  | Mt:=1St1​(Vt1+∑j=2dRtj​Vtj)=V^t1+1St1​∑j=2dZtjZt1​St1Stj​Vtj=1Zt1​Zt𝖳​V^t,t∈[0,T].M\_{t}:=\frac{1}{S^{1}\_{t}}\Big(V^{1}\_{t}+\sum\_{j=2}^{d}R^{j}\_{t}V^{j}\_{t}\Big)=\hat{V}^{1}\_{t}+\frac{1}{S^{1}\_{t}}\sum\_{j=2}^{d}\frac{Z^{j}\_{t}}{Z^{1}\_{t}}\frac{S^{1}\_{t}}{S^{j}\_{t}}V^{j}\_{t}=\frac{1}{Z^{1}\_{t}}Z\_{t}^{\mathsf{T}}\hat{V}\_{t},\quad t\in[0,T]. |  |

Thus, to show that MM is a ℙ1\mathbb{P}^{1}-supermartingale, it suffices to show that Z1​M=Z𝖳​V^Z^{1}M=Z^{\mathsf{T}}\hat{V} is a ℙ\mathbb{P}-supermartingale. To this end, we recall the dynamics of V^\hat{V} in ([3.31](https://arxiv.org/html/2511.18169v1#S3.E31 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) and the SDEs for ZZ in ([3.36](https://arxiv.org/html/2511.18169v1#S3.E36 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")). Applying Itô’s formula, we have

|  |  |  |
| --- | --- | --- |
|  | {d​(Zt1​V^t1)=−Zt1​1St1​⟨Θt,Π⟩​d​t+V^t1​Zt1​(ηt1)𝖳​d​Wt,d​(Ztj​V^tj)=−Ztj​1Stj​⟨Θt−Θt𝖳,Ei⟩​d​t+V^tj​Ztj​(ηtj)𝖳​d​Wt,j∈[d]∖{1},\left\{\begin{array}[]{lll}\displaystyle d(Z^{1}\_{t}\hat{V}^{1}\_{t})=-Z^{1}\_{t}\frac{1}{S^{1}\_{t}}\langle\Theta\_{t},\Pi\rangle dt+\hat{V}^{1}\_{t}Z^{1}\_{t}(\eta^{1}\_{t})^{\mathsf{T}}dW\_{t},\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \displaystyle d(Z^{j}\_{t}\hat{V}^{j}\_{t})=-Z^{j}\_{t}\frac{1}{S^{j}\_{t}}\langle\Theta\_{t}-\Theta\_{t}^{\mathsf{T}},E\_{i}\rangle dt+\hat{V}^{j}\_{t}Z^{j}\_{t}(\eta^{j}\_{t})^{\mathsf{T}}dW\_{t},\quad j\in[d]\setminus\{1\},\end{array}\right. |  |

for some Θ∈𝕊𝔽2​(𝕄+d)\Theta\in\mathbb{S}^{2}\_{\mathbb{F}}(\mathbb{M}^{d}\_{+}). Then, we deduce that

|  |  |  |
| --- | --- | --- |
|  | d​(Zt𝖳​V^t)=∑j=1dd​(Ztj​V^tj)=−Zt𝖳​k^t​d​t+∑j=1dV^tj​Ztj​(ηtj)𝖳​d​Wt,t∈[0,T],\displaystyle d(Z\_{t}^{\mathsf{T}}\hat{V}\_{t})=\sum\_{j=1}^{d}d(Z^{j}\_{t}\hat{V}^{j}\_{t})=-Z\_{t}^{\mathsf{T}}\hat{k}\_{t}dt+\sum\_{j=1}^{d}\hat{V}^{j}\_{t}Z^{j}\_{t}(\eta^{j}\_{t})^{\mathsf{T}}dW\_{t},\qquad t\in[0,T], |  |

where k^t=(kt1St1,…,ktdStd)𝖳\hat{k}\_{t}=(\frac{k^{1}\_{t}}{S^{1}\_{t}},\ldots,\frac{k^{d}\_{t}}{S^{d}\_{t}})^{\mathsf{T}} with kt1=⟨Θt,Π⟩k^{1}\_{t}=\langle\Theta\_{t},\Pi\rangle and kti=⟨Θt−Θt𝖳,Ei⟩k^{i}\_{t}=\langle\Theta\_{t}-\Theta\_{t}^{\mathsf{T}},E\_{i}\rangle, i∈[d]∖{1}i\in[d]\setminus\{1\}. Since kt=(kt1,…,ktd)∈K​(Π)k\_{t}=(k^{1}\_{t},\ldots,k^{d}\_{t})\in K(\Pi) by definition, k^t∈K^t=K^t​(Π)\hat{k}\_{t}\in\hat{K}\_{t}=\hat{K}\_{t}(\Pi). Therefore, by Definition [3.6](https://arxiv.org/html/2511.18169v1#S3.Thmthm6 "Definition 3.6. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time") and ZZ being a consistent process process, we have Zt∈Kt+∖{0}Z\_{t}\in K^{+}\_{t}\setminus\{0\}, that is, Zt𝖳​k^t≥0Z\_{t}^{\mathsf{T}}\hat{k}\_{t}\geq 0, t∈[0,T]t\in[0,T], ℙ\mathbb{P}-a.s. In other words, Z𝖳​V^Z^{\mathsf{T}}\hat{V} is a ℙ\mathbb{P}-supermartingale, proving the theorem.

## 4 Functional Formulation of the Superhedging Problem

In this section, using the set-valued solvency cone process (K^t)t∈[0,T](\hat{K}\_{t})\_{t\in[0,T]} defined in ([3.17](https://arxiv.org/html/2511.18169v1#S3.E17 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we shall describe a basic formulation of the continuous-time superhedging problem for the financial model described in Section [3](https://arxiv.org/html/2511.18169v1#S3 "3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time").

Superhedging Sets and Set-Valued Risk Measures. The formulation is based on the direct meaning of “superhedging” a multi-asset payoff, i.e., finding a self-financing portfolio process whose terminal value exceeds the given payoff in every component. More precisely, in view of Theorem [3.3](https://arxiv.org/html/2511.18169v1#S3.Thmthm3 "Theorem 3.3. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), we say that a portfolio ξ∈𝕃ℱt2​(ℝd)\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}) superhedges a risky position X∈𝕃ℱT2​(ℝd)X\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}) at time t∈[0,T]t\in[0,T] if there exists k^∈𝕊^𝔽2​(K^)\hat{k}\in\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}) such that ξ−∫tTk^r​𝑑r≥X\xi-\int\_{t}^{T}\hat{k}\_{r}dr\geq X ℙ\mathbb{P}-a.s. Hence, the set of all superhedging portfolios at time tt is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​H​Pt​(X):={ξ∈𝕃ℱt2​(ℝd):∃k^∈𝕊^𝔽2​(K^),ξ−∫tTk^r​𝑑r≥X}.\displaystyle SHP\_{t}(X):=\left\{\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon\exists\hat{k}\in\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}),\ \xi-\int\_{t}^{T}\hat{k}\_{r}dr\geq X\right\}. |  | (4.1) |

With the notation of Section [2](https://arxiv.org/html/2511.18169v1#S2 "2 Preliminaries ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), this definition can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | S​H​Pt​(X)={ξ∈𝕃ℱt2​(ℝd):X∈ξ+Jt,T​[𝕊^𝔽2​(−K^)]−𝕃ℱT2​(ℝ+d)},SHP\_{t}(X)=\left\{\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon X\in\xi+J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(-\hat{K})]-\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+})\right\}, |  |

which is the continuous-time analog of the set in ([2.1](https://arxiv.org/html/2511.18169v1#S2.E1 "In 2 Preliminaries ‣ Superhedging under Proportional Transaction Costs in Continuous Time")). Similar to the discrete-time case, we also define the corresponding superhedging risk measure at time tt by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt​(X):=S​H​Pt​(−X)={ξ∈𝕃ℱt2​(ℝd):X+ξ∈Jt,T​[𝕊^𝔽2​(K^)]+𝕃ℱT2​(ℝ+d)},\displaystyle R\_{t}(X):=SHP\_{t}(-X)=\left\{\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon X+\xi\in J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+})\right\}, |  | (4.2) |

and, for 0≤t≤u≤T0\leq t\leq u\leq T, its (stepped) acceptance sets are given by

|  |  |  |
| --- | --- | --- |
|  | At:={X∈𝕃ℱT2​(ℝd):0∈Rt​(X)}=Jt,T​[𝕊^𝔽2​(K^)]+𝕃ℱT2​(ℝ+d),At,u:=At∩𝕃ℱu2​(ℝd).A\_{t}:=\{X\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d})\colon 0\in R\_{t}(X)\}=J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+}),\quad A\_{t,u}:=A\_{t}\cap\mathbb{L}^{2}\_{{\cal F}\_{u}}(\mathbb{R}^{d}). |  |

To avoid some degenerate cases of the superhedging sets, we work under the following assumption throughout this section:

###### Assumption 4.1.

There exists a consistent price process (Zt)t∈[0,T]∈𝕃𝔽1​([0,T]×Ω,ℝd)(Z\_{t})\_{t\in[0,T]}\in\mathbb{L}^{1}\_{\mathbb{F}}([0,T]\times\Omega,\mathbb{R}^{d}) with Z01=1Z\_{0}^{1}=1.

###### Proposition 4.2.

The family (Rt)t∈[0,T](R\_{t})\_{t\in[0,T]} of set-valued functions defined by ([4.2](https://arxiv.org/html/2511.18169v1#S4.E2 "In 4 Functional Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) is a conditionally coherent and normalized dynamic set-valued risk measure.

Proof. Let t∈[0,T]t\in[0,T]. We first show that the function RtR\_{t} takes values in 𝒫+​(𝕃ℱt2​(ℝd))\mathscr{P}\_{+}(\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})). To that end, let us fix X∈𝕃ℱT2​(ℝd)X\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}) and show that Rt​(X)=Rt​(X)+𝕃ℱt2​(ℝ+d)R\_{t}(X)=R\_{t}(X)+\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}\_{+}). The inclusion ⊆\subseteq is trivial since 0∈𝕃ℱt2​(ℝ+d)0\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}\_{+}). Conversely, let ξ∈Rt​(X)\xi\in R\_{t}(X) and η∈𝕃ℱt2​(ℝ+d)\eta\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}\_{+}). Then, X+ξ∈Jt,T​[𝕊^𝔽2​(K^)]+𝕃ℱT2​(ℝ+d)X+\xi\in J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+}), and therefore

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | X+ξ+η\displaystyle X+\xi+\eta | ∈\displaystyle\in | Jt,T​[𝕊^𝔽2​(K^)]+𝕃ℱT2​(ℝ+d)+𝕃ℱt2​(ℝ+d)\displaystyle J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+})+\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}\_{+}) |  |
|  |  | ⊆\displaystyle\subseteq | Jt,T​[𝕊^𝔽2​(K^)]+𝕃ℱT2​(ℝ+d)+𝕃ℱT2​(ℝ+d)\displaystyle J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+})+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+}) |  |
|  |  | =\displaystyle= | Jt,T​[𝕊^𝔽2​(K^)]+𝕃ℱT2​(ℝ+d)\displaystyle J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+}) |  |

since 𝕃ℱT2​(ℝ+d)\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+}) is a convex cone. Hence, ξ+η∈Rt​(X)\xi+\eta\in R\_{t}(X) so that Rt​(X)+𝕃ℱT2​(ℝ+d)⊆Rt​(X)R\_{t}(X)+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+})\subseteq R\_{t}(X).

Next, we check the properties of conditional set-valued risk measures. First, let X,Y∈𝕃ℱT2​(ℝd)X,Y\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}) with Y≥XY\geq X, i.e., Z:=Y−X∈𝕃ℱT2​(ℝ+d)Z:=Y-X\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+}). Let ξ∈Rt​(X)\xi\in R\_{t}(X). Then, ξ∈𝕃ℱt2​(ℝd)\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}) and X+ξ=Y−Z+ξ∈Jt,T​[𝕊^𝔽2​(K^)]+𝕃ℱT2​(ℝ+d)X+\xi=Y-Z+\xi\in J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+}). Then,

|  |  |  |
| --- | --- | --- |
|  | Y+ξ∈Z+Jt,T​[𝕊^𝔽2​(K^)]+𝕃ℱT2​(ℝ+d)⊆Jt,T​[𝕊^𝔽2​(K^)]+𝕃ℱT2​(ℝ+d).Y+\xi\in Z+J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+})\subseteq J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+}). |  |

Hence, ξ∈Rt​(Y)\xi\in R\_{t}(Y) so that Rt​(X)⊆Rt​(Y)R\_{t}(X)\subseteq R\_{t}(Y), i.e., RtR\_{t} is monotone.

Let X∈𝕃ℱT2​(ℝd)X\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}) and η∈𝕃ℱt2​(ℝd)\eta\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}). Then, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Rt​(X+η)\displaystyle R\_{t}(X+\eta) | =\displaystyle= | {ξ∈𝕃ℱt2​(ℝd):X+η+ξ∈Jt,T​[𝕊^𝔽2​(K^)]+𝕃ℱT2​(ℝ+d)}\displaystyle\left\{\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon X+\eta+\xi\in J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+})\right\} |  |
|  |  | =\displaystyle= | {ξ′∈𝕃ℱt2​(ℝd):X+ξ′∈Jt,T​[𝕊^𝔽2​(K^)]+𝕃ℱT2​(ℝ+d)}−η\displaystyle\left\{\xi^{\prime}\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon X+\xi^{\prime}\in J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+})\right\}-\eta |  |
|  |  | =\displaystyle= | Rt​(X)−η.\displaystyle R\_{t}(X)-\eta. |  |

Hence, RtR\_{t} is translative.

Note that Rt​(0)=At∩𝕃ℱt2​(ℝd)R\_{t}(0)=A\_{t}\cap\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}). Since 0∈At0\in A\_{t}, we have Rt​(0)≠∅R\_{t}(0)\neq\emptyset. Next, we show that Rt​(0)≠𝕃ℱt2​(ℝd)R\_{t}(0)\neq\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}). To get a contradiction, suppose that 𝕃ℱt2​(ℝd)⊆At=Jt,T​[𝕊^𝔽2​(K^)]+𝕃ℱT2​(ℝ+d)\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\subseteq A\_{t}=J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+}). Let us fix ξ∈𝕃ℱt2​(ℝd)\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}). Then, there exists k^ξ∈𝕊^𝔽2​(K^)\hat{k}^{\xi}\in\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}) such that ξ≥∫tTk^rξ​𝑑r\xi\geq\int\_{t}^{T}\hat{k}^{\xi}\_{r}dr. For each u∈[t,T]u\in[t,T], let V^uξ:=ξ−∫tuk^rξ​𝑑r\hat{V}^{\xi}\_{u}:=\xi-\int\_{t}^{u}\hat{k}^{\xi}\_{r}dr. Then, (V^u)u∈[t,T](\hat{V}\_{u})\_{u\in[t,T]} is a self-financing portfolio process expressed in physical units over the interval [t,T][t,T]; see Theorem [3.3](https://arxiv.org/html/2511.18169v1#S3.Thmthm3 "Theorem 3.3. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")(v). Let ZZ be a consistent price process wit Z01=1Z^{1}\_{0}=1, whose existence is guaranteed by Assumption [4.1](https://arxiv.org/html/2511.18169v1#S4.Thmthm1 "Assumption 4.1. ‣ 4 Functional Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time"). Then, applying Theorem [3.7](https://arxiv.org/html/2511.18169v1#S3.Thmthm7 "Theorem 3.7. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time") over the interval [t,T][t,T], we obtain that Z𝖳​V^Z^{\mathsf{T}}\hat{V} is a ℙ\mathbb{P}-supermartingale. In particular,

|  |  |  |
| --- | --- | --- |
|  | Zt𝖳​ξ=Zt𝖳​V^t≥𝔼​[ZT𝖳​V^T|ℱt]=𝔼​[ZT𝖳​(ξ−∫tTk^rξ​𝑑r)]≥0,Z^{\mathsf{T}}\_{t}\xi=Z^{\mathsf{T}}\_{t}\hat{V}\_{t}\geq\mathbb{E}[Z^{\mathsf{T}}\_{T}\hat{V}\_{T}|{\cal F}\_{t}]=\mathbb{E}\left[Z\_{T}^{\mathsf{T}}\left(\xi-\int\_{t}^{T}\hat{k}^{\xi}\_{r}dr\right)\right]\geq 0, |  |

where the last inequality follows since ξ≥∫tTk^rξ​𝑑r\xi\geq\int\_{t}^{T}\hat{k}^{\xi}\_{r}dr and ZT≥0Z\_{T}\geq 0 by Corollary [3.5](https://arxiv.org/html/2511.18169v1#S3.Thmthm5 "Corollary 3.5. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time"). The same corollary also yields that Zt∈ℝ++dZ\_{t}\in\mathbb{R}^{d}\_{++} ℙ\mathbb{P}-a.s. Since ξ∈𝕃ℱt2​(ℝd)\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}) is arbitrary, from the above calculations, we get −∞=essinfξ∈𝕃ℱt2​(ℝd)Zt𝖳​ξ≥0-\infty=\mathop{\rm essinf}\_{\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})}Z^{\mathsf{T}}\_{t}\xi\geq 0, which is a contradiction. Hence, Rt​(0)≠𝕃ℱt2​(ℝd)R\_{t}(0)\neq\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}) so that RtR\_{t} is finite at zero.

Let X,Y∈𝕃ℱT2​(ℝd)X,Y\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}) and α,β∈𝕃ℱt∞​(ℝ+)\alpha,\beta\in\mathbb{L}^{\infty}\_{{\cal F}\_{t}}(\mathbb{R}\_{+}). We claim that

|  |  |  |  |
| --- | --- | --- | --- |
|  | α​Rt​(X)+β​Rt​(Y)⊆Rt​(α​X+β​Y).\displaystyle\alpha R\_{t}(X)+\beta R\_{t}(Y)\subseteq R\_{t}(\alpha X+\beta Y). |  | (4.3) |

Let ξ∈Rt​(X)\xi\in R\_{t}(X) and η∈Rt​(Y)\eta\in R\_{t}(Y). Hence, X+ξ,Y+η∈Jt,T​[𝕊^𝔽2​(K^)]+𝕃ℱT2​(ℝ+d)X+\xi,Y+\eta\in J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+}). Since α,β\alpha,\beta are nonnegative ℱt{\cal F}\_{t}-measurable random variables and K^\hat{K} is a convex cone-valued process, we have α​Jt,T​[𝕊^𝔽2​(K^)]+β​Jt,T​[𝕊^𝔽2​(K^)]=Jt,T​[𝕊^𝔽2​(K^)]\alpha J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\beta J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]=J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]. It follows that α​(X+ξ)+β​(Y+η)∈Jt,T​[𝕊^𝔽2​(K^)]+𝕃ℱT2​(ℝ+d)\alpha(X+\xi)+\beta(Y+\eta)\in J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+}). Hence, α​ξ+β​η∈Rt​(α​X+β​Y)\alpha\xi+\beta\eta\in R\_{t}(\alpha X+\beta Y). Taking α=λ\alpha=\lambda and β=1−λ\beta=1-\lambda for each λ∈𝕃ℱt∞​([0,1])\lambda\in\mathbb{L}^{\infty}\_{{\cal F}\_{t}}([0,1]), we see that RtR\_{t} is conditionally convex. Taking β=0\beta=0, we obtain α​Rt​(X)⊆Rt​(α​X)\alpha R\_{t}(X)\subseteq R\_{t}(\alpha X) for every α∈𝕃ℱt∞​(ℝ+)\alpha\in\mathbb{L}^{\infty}\_{{\cal F}\_{t}}(\mathbb{R}\_{+}). Then, assuming that α∈𝕃ℱt∞​(ℝ++)\alpha\in\mathbb{L}^{\infty}\_{{\cal F}\_{t}}(\mathbb{R}\_{++}), we have

|  |  |  |
| --- | --- | --- |
|  | Rt​(α​X)=α​1α​Rt​(α​X)⊆α​Rt​(X)R\_{t}(\alpha X)=\alpha\frac{1}{\alpha}R\_{t}(\alpha X)\subseteq\alpha R\_{t}(X) |  |

as well. Hence, Rt​(α​X)=α​Rt​(X)R\_{t}(\alpha X)=\alpha R\_{t}(X) so that RtR\_{t} is conditionally positively homogeneous.

Let X∈LℱT2​(ℝd)X\in L^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}). Since 0∈Rt​(0)0\in R\_{t}(0), we have Rt​(X)⊆Rt​(X)+Rt​(0)R\_{t}(X)\subseteq R\_{t}(X)+R\_{t}(0). By ([4.3](https://arxiv.org/html/2511.18169v1#S4.E3 "In 4 Functional Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we also have Rt​(X)+Rt​(0)⊆Rt​(X)R\_{t}(X)+R\_{t}(0)\subseteq R\_{t}(X). Hence, RtR\_{t} is normalized.

Thus, (Rt)t∈[0,T](R\_{t})\_{t\in[0,T]} is a conditionally coherent and normalized dynamic set-valued risk measure.

The Functional Dynamic Programming Principle. The next proposition states the time-consistency of the family (Rt)t∈[0,T](R\_{t})\_{t\in[0,T]} in the set-valued setting.

###### Proposition 4.3.

The set-valued dynamic risk measure (Rt)t∈[0,T](R\_{t})\_{t\in[0,T]} is multi-portfolio time-consistent.

Proof. Since (Rt)t∈[0,T](R\_{t})\_{t\in[0,T]} is normalized, by Theorem [2.4](https://arxiv.org/html/2511.18169v1#S2.Thmthm4 "Theorem 2.4. ‣ 2 Preliminaries ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), multi-portfolio time-consistency is equivalent to At=At,u+AuA\_{t}=A\_{t,u}+A\_{u} for every 0≤t<u≤T0\leq t<u\leq T, which we check next. Note that

|  |  |  |
| --- | --- | --- |
|  | At=Jt,T​[𝕊^𝔽2​(K^)]+𝕃ℱT2​(ℝ+d),At,u=At∩𝕃ℱu2​(ℝd).A\_{t}=J\_{t,T}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]+\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}\_{+}),\quad A\_{t,u}=A\_{t}\cap\mathbb{L}^{2}\_{{\cal F}\_{u}}(\mathbb{R}^{d}). |  |

Let ξ∈At,u\xi\in A\_{t,u} and X∈AuX\in A\_{u}. Then ξ∈𝕃ℱu2​(ℝd)\xi\in\mathbb{L}^{2}\_{{\cal F}\_{u}}(\mathbb{R}^{d}) and ξ≥∫tTk^rξ​𝑑r\xi\geq\int\_{t}^{T}\hat{k}^{\xi}\_{r}dr for some k^ξ∈𝕊^𝔽2​(K^)\hat{k}^{\xi}\in\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}), and similarly, X∈𝕃ℱT2​(ℝd)X\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}) and η≥∫uTk^rX​𝑑r\eta\geq\int\_{u}^{T}\hat{k}^{X}\_{r}dr for some k^X∈𝕊^𝔽2​(K^)\hat{k}^{X}\in\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}). Thus, Y:=ξ+X∈𝕃ℱT2​(ℝd)Y:=\xi+X\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}) and Y≥∫tTk^rξ​𝑑r+∫uTk^rX​𝑑r=∫tT(k^rξ+𝟏[u,T]​(r)​k^rX)​𝑑rY\geq\int\_{t}^{T}\hat{k}^{\xi}\_{r}dr+\int\_{u}^{T}\hat{k}^{X}\_{r}dr=\int\_{t}^{T}(\hat{k}^{\xi}\_{r}+{\bf 1}\_{[u,T]}(r)\hat{k}^{X}\_{r})dr, and therefore Y∈AtY\in A\_{t}.

Conversely, let X∈AtX\in A\_{t}. Then X∈𝕃ℱT2​(ℝd)X\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}) and X≥∫tTk^r​𝑑rX\geq\int\_{t}^{T}\hat{k}\_{r}dr for some k^∈𝕊^𝔽2​(K^)\hat{k}\in\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}). Let us take ξ:=∫tuk^r​𝑑r\xi:=\int\_{t}^{u}\hat{k}\_{r}dr and Y:=X−ξY:=X-\xi. Then, clearly ξ∈At,u\xi\in A\_{t,u}. On the other hand, Y≥∫uTk^r​𝑑rY\geq\int\_{u}^{T}\hat{k}\_{r}dr, and hence Y∈AuY\in A\_{u}. Since X=ξ+YX=\xi+Y, the result follows.

###### Remark 4.4.

As an immediate consequence of Proposition [4.3](https://arxiv.org/html/2511.18169v1#S4.Thmthm3 "Proposition 4.3. ‣ 4 Functional Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), the family (S​H​Pt)t∈[0,T](SHP\_{t})\_{t\in[0,T]} satisfies the following recursive property:

|  |  |  |
| --- | --- | --- |
|  | S​H​Pt​(X)=Rt​(−X)=⋃η∈Ru​(−X)Rt​(−η)=⋃η∈S​H​Pu​(X)S​H​Pt​(η),\displaystyle SHP\_{t}(X)=R\_{t}(-X)=\bigcup\_{\eta\in R\_{u}(-X)}R\_{t}(-\eta)=\bigcup\_{\eta\in SHP\_{u}(X)}SHP\_{t}(\eta), |  |

for every 0≤t≤u≤T0\leq t\leq u\leq T and X∈𝕃ℱT2​(ℝd)X\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}).

We now sharpen the observation in Remark [4.4](https://arxiv.org/html/2511.18169v1#S4.Thmthm4 "Remark 4.4. ‣ 4 Functional Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time") and obtain a more useful recursive relation for the family (S​H​Pt)t∈[0,T](SHP\_{t})\_{t\in[0,T]}, which can be seen as a set-valued dynamic programming principle.

###### Theorem 4.5.

Let 0≤t≤u≤T0\leq t\leq u\leq T and X∈𝕃ℱT2​(ℝd)X\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}). Then, it holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​H​Pt​(X)=(S​H​Pu​(X)+Jt,u​[𝕊^𝔽2​(K^)])∩𝕃ℱt2​(ℝd).\displaystyle SHP\_{t}(X)=\big(SHP\_{u}(X)+J\_{t,u}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]\big)\cap\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}). |  | (4.4) |

Proof. For a random vector η∈𝕃ℱu2​(ℝd)\eta\in\mathbb{L}^{2}\_{{\cal F}\_{u}}(\mathbb{R}^{d}), first note that η∈S​H​Pu​(X)\eta\in SHP\_{u}(X) if and only if there exists k~∈𝕊^𝔽2​(K^)\tilde{k}\in\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}) such that η≥X+Ju,T​(k~)\eta\geq X+J\_{u,T}(\tilde{k}). Thus, by Remark [4.4](https://arxiv.org/html/2511.18169v1#S4.Thmthm4 "Remark 4.4. ‣ 4 Functional Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | S​H​Pt​(X)\displaystyle SHP\_{t}(X) | ={ξ∈𝕃ℱt2​(ℝd):∃η∈S​H​Pu​(X),ξ∈S​H​Pt​(η)}\displaystyle=\big\{\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon\exists\eta\in SHP\_{u}(X),\xi\in SHP\_{t}(\eta)\big\} |  | (4.5) |
|  |  | ={ξ∈𝕃ℱt2​(ℝd):∃k^∈𝕊^𝔽2​(K^),∃η∈S​H​Pu​(X),ξ≥η+Jt,T​(k^)}\displaystyle=\big\{\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon\exists\hat{k}\in\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}),\exists\eta\in SHP\_{u}(X),\xi\geq\eta+J\_{t,T}(\hat{k})\big\} |  |
|  |  | ⊆{ξ∈𝕃ℱt2​(ℝd):∃k^,k~∈𝕊^𝔽2​(K^),ξ≥X+Ju,T​(k~)+Jt,T​(k^)}\displaystyle\subseteq\big\{\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon\exists\hat{k},\tilde{k}\in\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}),\xi\geq X+J\_{u,T}(\tilde{k})+J\_{t,T}(\hat{k})\big\} |  |
|  |  | ={ξ∈𝕃ℱt2​(ℝd):∃k^,k~∈𝕊^𝔽2​(K^),ξ−Jt,u​(k^)≥X+Ju,T​(k~+k^)}.\displaystyle=\big\{\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon\exists\hat{k},\tilde{k}\in\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}),\xi-J\_{t,u}(\hat{k})\geq X+J\_{u,T}(\tilde{k}+\hat{k})\big\}. |  |

Since 𝕃ℱt2​(ℝd)⊆𝕃ℱu2​(ℝd)\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\subseteq\mathbb{L}^{2}\_{{\cal F}\_{u}}(\mathbb{R}^{d}), having ξ−Jt,u​(k^)≥X+Ju,T​(k~+k^)\xi-J\_{t,u}(\hat{k})\geq X+J\_{u,T}(\tilde{k}+\hat{k}) for some ξ∈𝕃ℱt2​(ℝd)\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}) implies that ξ−Jt,u​(k^)∈S​H​Pu​(X)\xi-J\_{t,u}(\hat{k})\in SHP\_{u}(X). Hence, from ([4.5](https://arxiv.org/html/2511.18169v1#S4.E5 "In 4 Functional Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​H​Pt​(X)\displaystyle SHP\_{t}(X) | ⊆{ξ∈𝕃ℱt2​(ℝd):∃k^∈𝕊^𝔽2​(K^),ξ−Jt,u​(k^)∈S​H​Pu​(X)}\displaystyle\subseteq\big\{\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon\exists\hat{k}\in\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}),\ \xi-J\_{t,u}(\hat{k})\in SHP\_{u}(X)\big\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(S​H​Pu​(X)+Jt,u​[𝕊^𝔽2​(K^)])∩𝕃ℱt2​(ℝd).\displaystyle=\big(SHP\_{u}(X)+J\_{t,u}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]\big)\cap\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}). |  |

Conversely, let ξ∈(S​H​Pu​(X)+Jt,u​[𝕊^𝔽2​(K^)])∩𝕃ℱt2​(ℝd)\xi\in(SHP\_{u}(X)+J\_{t,u}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})])\cap\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}). Then, there exist η∈S​H​Pu​(X)\eta\in SHP\_{u}(X) and k^∈𝕊^𝔽2​(K^)\hat{k}\in\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}) such that ξ=η+Jt,u​(k^)\xi=\eta+J\_{t,u}(\hat{k}). Since η∈S​H​Pu​(X)\eta\in SHP\_{u}(X), there exists k~∈𝕊^𝔽2​(K^)\tilde{k}\in\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K}) such that η≥X+Ju,T​(k~)\eta\geq X+J\_{u,T}(\tilde{k}). Hence, ξ≥X+Ju,T​(k~)+Jt,u​(k^)=X+Jt,T​(𝟏[t,u)​k^+𝟏[u,T]​k~)\xi\geq X+J\_{u,T}(\tilde{k})+J\_{t,u}(\hat{k})=X+J\_{t,T}({\bf 1}\_{[t,u)}\hat{k}+{\bf 1}\_{[u,T]}\tilde{k}) so that ξ∈S​H​Pt​(X)\xi\in SHP\_{t}(X).

###### Remark 4.6.

We note that the recursive relation in Theorem [4.5](https://arxiv.org/html/2511.18169v1#S4.Thmthm5 "Theorem 4.5. ‣ 4 Functional Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time") is closely related to the notion of *conditional core* introduced in [LepMol]. While their definition applies for random closed sets, we now give a slightly modified version of the concept that fits our case.
Let M⊆𝕃ℱ2​(ℝd)M\subseteq\mathbb{L}^{2}\_{{\cal F}}(\mathbb{R}^{d}) be a nonempty set
and 𝒢⊆ℱ{\cal G}\subseteq{\cal F} be a sub-σ\sigma-field of ℱ{\cal F}. We define the 𝒢{\cal G}-conditional core 𝐦​[M|𝒢]{\bf m}[M|{\cal G}] of MM to be the largest 𝒢{\cal G}-decomposable closed set M′⊆𝕃𝒢2​(ℝd)M^{\prime}\subseteq\mathbb{L}^{2}\_{{\cal G}}(\mathbb{R}^{d}) such that M′⊆dec¯𝒢​(M)M^{\prime}\subseteq\overline{\operatorname{dec}}\_{\cal G}(M). It can be argued that (cf. [LepMol]) if MM is convex, or a cone, then so is 𝐦​[M|𝒢]{\bf m}[M|{\cal G}], whenever it exists. Now for any closed subset M⊆𝕃ℱu2​(ℝd)M\subseteq\mathbb{L}^{2}\_{{\cal F}\_{u}}(\mathbb{R}^{d}),
we consider Mt:=𝕃ℱt2​(ℝd)∩MM\_{t}:=\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\cap M, t≤ut\leq u. Then, clearly Mt=𝐦​[M|ℱt]M\_{t}={\bf m}[M|{\cal F}\_{t}] provided that MtM\_{t} is ℱt{\cal F}\_{t}-decomposable. Since S​H​Pt​(X)SHP\_{t}(X) is ℱt{\cal F}\_{t}-decomposable, t∈[0,T]t\in[0,T], we may write ([4.4](https://arxiv.org/html/2511.18169v1#S4.E4 "In Theorem 4.5. ‣ 4 Functional Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) in Theorem [4.5](https://arxiv.org/html/2511.18169v1#S4.Thmthm5 "Theorem 4.5. ‣ 4 Functional Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time") as the following dynamic programming principle in terms of the conditional core:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​H​Pt​(X)=𝐦​[S​H​Pu​(X)+Jt,u​[𝕊^𝔽2​(K^)]|ℱt],\displaystyle SHP\_{t}(X)={\bf m}\big[SHP\_{u}(X)+J\_{t,u}[\hat{\mathbb{S}}^{2}\_{\mathbb{F}}(\hat{K})]\big|{\cal F}\_{t}\big], |  | (4.6) |

where 0≤t≤u0\leq t\leq u and X∈𝕃ℱT2​(ℝd)X\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}).

###### Remark 4.7.

As an alternative to the formulation in this section, we may consider the following relaxed formulation of the superhedging problem based on the set-valued Lebesgue integral reviewed in Section [2](https://arxiv.org/html/2511.18169v1#S2 "2 Preliminaries ‣ Superhedging under Proportional Transaction Costs in Continuous Time"). Given a financial position X∈𝕃ℱT2​(ℝd)X\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}), we may say that a portfolio ξ∈𝕃ℱt2​(ℝd)\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}) superhedges XX at time t∈[0,T]t\in[0,T] if ξ∈X+𝕊ℱT2​(∫tTK^r​𝑑r)\xi\in X+\mathbb{S}^{2}\_{{\cal F}\_{T}}(\int\_{t}^{T}\hat{K}\_{r}dr), yielding the superhedging risk measure

|  |  |  |
| --- | --- | --- |
|  | Rt′​(X):={ξ∈𝕃ℱt2:ξ+X∈𝕊ℱT2​(∫tTK^r​𝑑r)}.R^{\prime}\_{t}(X):=\left\{\xi\in\mathbb{L}^{2}\_{{\cal F}\_{t}}\colon\xi+X\in\mathbb{S}^{2}\_{{\cal F}\_{T}}\left(\int\_{t}^{T}\hat{K}\_{r}dr\right)\right\}. |  |

Notably, Rt′R\_{t}^{\prime} possesses some of the nice features of RtR\_{t} such as translativity and convexity, and the corresponding acceptance set

|  |  |  |
| --- | --- | --- |
|  | At′:={X∈𝕃ℱT2​(ℝd):0∈Rt′​(X)}=𝕊ℱT2​(∫tTK^r​𝑑r)=dec¯ℱT​(Jt,T​[𝕊𝔽2​(K^)])A\_{t}^{\prime}:=\{X\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d})\colon 0\in R^{\prime}\_{t}(X)\}=\mathbb{S}^{2}\_{{\cal F}\_{T}}\left(\int\_{t}^{T}\hat{K}\_{r}dr\right)=\overline{\operatorname{dec}}\_{{\cal F}\_{T}}(J\_{t,T}[\mathbb{S}^{2}\_{\mathbb{F}}(\hat{K})]) |  |

is closed in 𝕃ℱt2​(ℝd)\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}). However, this definition lacks a clear financial interpretation. In fact, an acceptable position X∈At′X\in A^{\prime}\_{t} can only be written as the limit of a sequence of positions of the form ∑i=1m𝟏Bi​∫tTk^ri​𝑑r\sum\_{i=1}^{m}{\bf 1}\_{B\_{i}}\int\_{t}^{T}\hat{k}^{i}\_{r}dr, where (Bi)i∈[m](B\_{i})\_{i\in[m]} is an ℱT{\cal F}\_{T}-partition of Ω\Omega and k^1,…,k^m∈𝕊𝔽2​(K^)\hat{k}^{1},\ldots,\hat{k}^{m}\in\mathbb{S}^{2}\_{\mathbb{F}}(\hat{K}). Such an approximation of XX does not correspond to a clear superhedging strategy since ∑i=1m𝟏Bi​k^i\sum\_{i=1}^{m}{\bf 1}\_{B\_{i}}\hat{k}^{i} is not adapted in general. Hence, among the two notions of set-valued integration with respect to the time variable, we conclude that the functional set-valued integral is a more suitable alternative for the superhedging problem.

## 5 Pathwise Formulation of the Superhedging Problem

In this section, we will provide a pathwise formulation of the superhedging problem based on the canonical space of continuous functions.

Motivation. Let us briefly explain the motivation to pass to the path-space setting. According to the functional formulation of the superhedging problem in Section [4](https://arxiv.org/html/2511.18169v1#S4 "4 Functional Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), the set of superhedging strategies of a risky position X∈𝕃ℱT2​(ℝd)X\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}) at time t∈[0,T]t\in[0,T] is defined as a convex cone Rt​(X)⊆𝕃ℱt2​(ℝd)R\_{t}(X)\subseteq\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}). In view of Remark [2.3](https://arxiv.org/html/2511.18169v1#S2.Thmthm3 "Remark 2.3. ‣ 2 Preliminaries ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), the set Rt​(X)R\_{t}(X) is also ℱt{\cal F}\_{t}-decomposable and

|  |  |  |
| --- | --- | --- |
|  | cl𝕃2​(Rt​(X))=𝕊ℱt2​(R~t​(X))\mbox{\rm cl}\_{\mathbb{L}^{2}}(R\_{t}(X))=\mathbb{S}^{2}\_{{\cal F}\_{t}}(\tilde{R}\_{t}(X)) |  |

for some set-valued random variable R~t​(X)∈𝒜ℱtp​(Ω,𝒢​(ℝd))\tilde{R}\_{t}(X)\in\mathscr{A}^{p}\_{{\cal F}\_{t}}(\Omega,\mathscr{G}(\mathbb{R}^{d})). Intuitively, one would like to treat the set-valued process (t,ω)↦R~t​(X)​(ω)(t,\omega)\mapsto\tilde{R}\_{t}(X)(\omega) as a pathwise version of the collection (Rt​(X))t∈[0,T](R\_{t}(X))\_{t\in[0,T]} and expect that this set-valued process satisfies a local form of the multi-portfolio time-consistency in Proposition [4.3](https://arxiv.org/html/2511.18169v1#S4.Thmthm3 "Proposition 4.3. ‣ 4 Functional Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time") and a local form of the dynamic programming principle in Theorem [4.5](https://arxiv.org/html/2511.18169v1#S4.Thmthm5 "Theorem 4.5. ‣ 4 Functional Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time"). However, an attempt to prove a dynamic programming principle directly for the set-valued process (t,ω)↦R~t​(X)​(ω)(t,\omega)\mapsto\tilde{R}\_{t}(X)(\omega) involves numerous technical challenges such as joint measurability and the lack of decomposability for the functional set-valued integral. By formulating superhedging sets as set-valued random variables on the path space, we will prove a pathwise version of the dynamic programming principle for a slightly relaxed version of (t,ω)↦R~t​(X)​(ω)(t,\omega)\mapsto\tilde{R}\_{t}(X)(\omega).

Shifted and Concatenated Paths. Throughout this section, we will work under the following filtered probability space. Let us take Ω=ℂ0​([0,T],ℝm)\Omega=\mathbb{C}\_{0}([0,T],\mathbb{R}^{m}) be the collection of all continuous functions ω=(ωt)t∈[0,T]:[0,T]→ℝm\omega=(\omega\_{t})\_{t\in[0,T]}\colon[0,T]\to\mathbb{R}^{m} with ω0=0\omega\_{0}=0, equipped with the norm ω↦‖ω‖∞:=supt∈[0,T]|ωt|\omega\mapsto\|\omega\|\_{\infty}:=\sup\_{t\in[0,T]}|\omega\_{t}| for uniform convergence. We take ℱ{\cal F} to be the Borel σ\sigma-algebra on Ω\Omega and ℙ\mathbb{P} to be the Wiener measure on (Ω,ℱ)(\Omega,{\cal F}). Let W=(Wt)t∈[0,T]W=(W\_{t})\_{t\in[0,T]} denote the canonical process, i.e., Wt​(ω):=ωtW\_{t}(\omega):=\omega\_{t} for every t∈[0,T]t\in[0,T] and ω∈Ω\omega\in\Omega. We take 𝔽\mathbb{F} to be the standard filtration of WW that satisfies the usual conditions.

Following [dynamicgames, meanfield], we will work with concatenations of paths in Ω\Omega. Let t∈[0,T]t\in[0,T]. For each ω,ω~∈Ω\omega,\tilde{\omega}\in\Omega, we define their concatenation ω⊕tω~∈Ω\omega\oplus\_{t}\tilde{\omega}\in\Omega at tt by

|  |  |  |
| --- | --- | --- |
|  | (ω⊕tω~)r:=ωr​𝟏[0,t)​(r)+(ωt+ω~r−t)​𝟏[t,T]​(r),r∈[0,T].(\omega\oplus\_{t}\tilde{\omega})\_{r}:=\omega\_{r}{\bf{1}}\_{[0,t)}(r)+(\omega\_{t}+\tilde{\omega}\_{r-t}){\bf{1}}\_{[t,T]}(r),\quad r\in[0,T]. |  |

Since (Ω,ℱ)(\Omega,{\cal F}) is a standard measurable space, there exists a regular conditional probability (ℙtω)ω∈Ω(\mathbb{P}^{\omega}\_{t})\_{\omega\in\Omega} given ℱt{\cal F}\_{t}. Without loss of generality, we assume that ℙtω​({ω~∈Ω:ωs=ω~s​ for every ​s∈[0,t]})=1\mathbb{P}^{\omega}\_{t}(\{\tilde{\omega}\in\Omega\colon\omega\_{s}=\tilde{\omega}\_{s}\text{ for every }s\in[0,t]\})=1 for every ω∈Ω\omega\in\Omega. For each ω∈Ω\omega\in\Omega, ξ∈𝕃ℱ0​(ℝd)\xi\in\mathbb{L}^{0}\_{{\cal F}}(\mathbb{R}^{d}), we define

|  |  |  |
| --- | --- | --- |
|  | ξt,ω​(ω~):=ξ​(ω⊕tω~),ω~∈Ω;ℙt,ω​(A):=ℙtω​(ω⊕tA),A∈ℱ,\xi^{t,\omega}(\tilde{\omega}):=\xi(\omega\oplus\_{t}\tilde{\omega}),\quad\tilde{\omega}\in\Omega;\quad\quad\mathbb{P}^{t,\omega}(A):=\mathbb{P}^{\omega}\_{t}(\omega\oplus\_{t}A),\quad A\in{\cal F}, |  |

where ω⊕tA:={ω⊕tω~:ω~∈A}\omega\oplus\_{t}A:=\{\omega\oplus\_{t}\tilde{\omega}\colon\tilde{\omega}\in A\}. Note that ℙt,ω\mathbb{P}^{t,\omega} is a probability measure on (Ω,ℱ)(\Omega,{\cal F}) for each ω∈Ω\omega\in\Omega. Indeed, by the Markov property of Wiener process, we have ℙt,ω=ℙ\mathbb{P}^{t,\omega}=\mathbb{P} for ℙ\mathbb{P}-a.e. ω∈Ω\omega\in\Omega. Moreover, whenever ξ∈𝕃ℱ1​(ℝd)\xi\in\mathbb{L}^{1}\_{{\cal F}}(\mathbb{R}^{d}), it is easy to verify that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ξ|ℱt]​(ω)=𝔼tω​[ξ]=𝔼t,ω​[ξt,ω]=𝔼​[ξt,ω]\displaystyle\mathbb{E}[\xi|{\cal F}\_{t}](\omega)=\mathbb{E}^{\omega}\_{t}[\xi]=\mathbb{E}^{t,\omega}[\xi^{t,\omega}]=\mathbb{E}[\xi^{t,\omega}] |  | (5.1) |

for ℙ\mathbb{P}-a.e. ω∈Ω\omega\in\Omega. We also define the time-shifted Wiener process Wt=(Wut)u∈[t,T]W^{t}=(W^{t}\_{u})\_{u\in[t,T]} by Wut:=Wu−tW^{t}\_{u}:=W\_{u-t} for each u∈[t,T]u\in[t,T], and denote by 𝔽t=(ℱut)u∈[t,T]\mathbb{F}^{t}=({\cal F}^{t}\_{u})\_{u\in[t,T]} its natural filtration, i.e., ℱut=σ​({Wrt:r∈[t,u]}){\cal F}^{t}\_{u}=\sigma(\{W^{t}\_{r}\colon\ r\in[t,u]\}) for each u∈[t,T]u\in[t,T]. Note that, for each ω,ω~∈Ω\omega,\tilde{\omega}\in\Omega and u∈[t,T]u\in[t,T],

|  |  |  |
| --- | --- | --- |
|  | Wut,ω​(ω~):=(Wu)t,ω​(ω~)=Wu​(ω⊕tω~)=ωt+ω~u−t=Wtt,ω​(ω~)+Wut​(ω~),W^{t,\omega}\_{u}(\tilde{\omega}):=(W\_{u})^{t,\omega}(\tilde{\omega})=W\_{u}(\omega\oplus\_{t}\tilde{\omega})=\omega\_{t}+\tilde{\omega}\_{u-t}=W\_{t}^{t,\omega}(\tilde{\omega})+W^{t}\_{u}(\tilde{\omega}), |  |

i.e., Wut=Wut,ω−Wtt,ωW^{t}\_{u}=W^{t,\omega}\_{u}-W^{t,\omega}\_{t}. Since the increments of (Wut,ω)u∈[t,T](W^{t,\omega}\_{u})\_{u\in[t,T]} do not depend on ω\omega, we simply use WtW^{t} in the sequel.

Shifted Dynamics. In this setting, we will consider the stock price process (St)t∈[0,T](S\_{t})\_{t\in[0,T]} that is uniquely defined by the dynamics in ([3.3](https://arxiv.org/html/2511.18169v1#S3.E3 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) with the additional assumption that b:[0,T]→ℝdb\colon[0,T]\to\mathbb{R}^{d} and σ:[0,T]→ℝd×m\sigma\colon[0,T]\to\mathbb{R}^{d\times m} are deterministic functions of time. Given η∈𝕃ℱt2​(ℝ++d)\eta\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}\_{++}), we denote by Sη;t=(Suη;t)u∈[t,T]S^{\eta;t}=(S^{\eta;t}\_{u})\_{u\in[t,T]} the unique solution of the same SDE starting at tt with initial value η\eta, i.e.,

|  |  |  |
| --- | --- | --- |
|  | d​Suη;t=diag⁡(Suη;t)​(bu​d​u+σu​d​Wu),u∈[t,T];Stη;t=η.dS^{\eta;t}\_{u}=\operatorname{diag}(S^{\eta;t}\_{u})(b\_{u}du+\sigma\_{u}dW\_{u}),\ u\in[t,T];\quad S^{\eta;t}\_{t}=\eta. |  |

In particular, by the flow property of the SDE, we have SuSt;t=SuS^{S\_{t};t}\_{u}=S\_{u} for every u∈[t,T]u\in[t,T] ℙ\mathbb{P}-a.s.

Let ω∈Ω\omega\in\Omega. Then, for ℙ\mathbb{P}-a.e. ω~∈Ω\tilde{\omega}\in\Omega, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sut,ω​(ω~)\displaystyle S^{t,\omega}\_{u}(\tilde{\omega}) | =Su​(ω⊕tω~)\displaystyle=S\_{u}(\omega\oplus\_{t}\tilde{\omega}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =St​(ω⊕tω~)+(∫tudiag⁡(Sr)​br​𝑑r)​(ω⊕tω~)+(∫tudiag⁡(Sr)​σr​𝑑Wr)​(ω⊕tω~)\displaystyle=S\_{t}(\omega\oplus\_{t}\tilde{\omega})+\left(\int\_{t}^{u}\operatorname{diag}(S\_{r})b\_{r}dr\right)(\omega\oplus\_{t}\tilde{\omega})+\left(\int\_{t}^{u}\operatorname{diag}(S\_{r})\sigma\_{r}dW\_{r}\right)(\omega\oplus\_{t}\tilde{\omega}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =St​(ω)+(∫tudiag⁡(Srt,ω)​br​𝑑r)​(ω~)+(∫tudiag⁡(Srt,ω)​σr​𝑑Wrt)​(ω~)\displaystyle=S\_{t}(\omega)+\left(\int\_{t}^{u}\operatorname{diag}(S^{t,\omega}\_{r})b\_{r}dr\right)(\tilde{\omega})+\left(\int\_{t}^{u}\operatorname{diag}(S^{t,\omega}\_{r})\sigma\_{r}dW^{t}\_{r}\right)(\tilde{\omega}) |  |

for every u∈[t,T]u\in[t,T]. Hence, the shifted stock price dynamics can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sut,ω=diag⁡(Sut,ω)​(bu​d​u+σu​d​Wut),u∈[t,T],Stt,ω=St​(ω).\displaystyle dS\_{u}^{t,\omega}=\operatorname{diag}(S\_{u}^{t,\omega})(b\_{u}du+\sigma\_{u}dW^{t}\_{u}),\ u\in[t,T],\quad S^{t,\omega}\_{t}=S\_{t}(\omega). |  | (5.2) |

Approximate Solvency Cones. Recall the deterministic solvency cone K​(Π)K(\Pi) defined in ([3.9](https://arxiv.org/html/2511.18169v1#S3.E9 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")). For some formulations in this section, we will rely on the following *halfspace representation* of K​(Π)K(\Pi). Since K​(Π)K(\Pi) is a polyhedral closed convex cone satisfying K​(Π)=K​(Π)+ℝ+dK(\Pi)=K(\Pi)+\mathbb{R}^{d}\_{+} (see Proposition [3.1](https://arxiv.org/html/2511.18169v1#S3.Thmthm1 "Proposition 3.1. ‣ 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we may find direction vectors w1,…,wN∈ℝ+d∖{0}w^{1},\ldots,w^{N}\in\mathbb{R}^{d}\_{+}\setminus\{0\} for some N∈ℕN\in\mathbb{N} such that

|  |  |  |
| --- | --- | --- |
|  | K​(Π)=⋂n=1N{x∈ℝd:(wn)𝖳​x≥0}.K(\Pi)=\bigcap\_{n=1}^{N}\{x\in\mathbb{R}^{d}\colon(w^{n})^{\mathsf{T}}x\geq 0\}. |  |

Without loss of generality, we assume that |wn|=1|w^{n}|=1 for each n∈[N]n\in[N]. Given ε≥0\varepsilon\geq 0, we introduce the ε\varepsilon-solvency cone in physical units at y∈ℝ++dy\in\mathbb{R}^{d}\_{++} by

|  |  |  |
| --- | --- | --- |
|  | 𝒦^ε​(y):=⋂n=1N{x∈ℝd:(diag⁡(y)​wn)𝖳​x≥−ε​|x|∞},\hat{\mathscr{K}}^{\varepsilon}(y):=\bigcap\_{n=1}^{N}\{x\in\mathbb{R}^{d}\colon(\operatorname{diag}(y)w^{n})^{\mathsf{T}}x\geq-\varepsilon|x|\_{\infty}\}, |  |

which is a polyhedral closed convex cone; here, |x|∞:=maxi∈[d]⁡|xi||x|\_{\infty}:=\max\_{i\in[d]}|x\_{i}| for x∈ℝdx\in\mathbb{R}^{d}. Note that

|  |  |  |
| --- | --- | --- |
|  | 𝒦^(y):=𝒦^0(y)=⋂n=1N{x∈ℝd:(diag(y)wn)𝖳x≥0}=diag(y)−1K(Π).\hat{\mathscr{K}}(y):=\hat{\mathscr{K}}^{0}(y)=\bigcap\_{n=1}^{N}\{x\in\mathbb{R}^{d}\colon(\operatorname{diag}(y)w^{n})^{\mathsf{T}}x\geq 0\}=\operatorname{diag}(y)^{-1}K(\Pi). |  |

Given (t,ω)∈[0,T]×Ω(t,\omega)\in[0,T]\times\Omega, we also define K^tε​(ω):=𝒦^ε​(St​(ω))\hat{K}^{\varepsilon}\_{t}(\omega):=\hat{\mathscr{K}}^{\varepsilon}(S\_{t}(\omega)) and its shifted version

|  |  |  |
| --- | --- | --- |
|  | K^uε;t,ω​(ω~):=K^uε​(ω⊕tω~)=𝒦^ε​(Sut,ω​(ω~))\hat{K}\_{u}^{\varepsilon;t,\omega}(\tilde{\omega}):=\hat{K}^{\varepsilon}\_{u}(\omega\oplus\_{t}\tilde{\omega})=\hat{\mathscr{K}}^{\varepsilon}(S^{t,\omega}\_{u}(\tilde{\omega})) |  |

for every (u,ω~)∈[t,T]×Ω(u,\tilde{\omega})\in[t,T]\times\Omega. With this notation, the cone-valued process in ([3.17](https://arxiv.org/html/2511.18169v1#S3.E17 "In 3 Solvency Cone and Consistent Prices ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) can be expressed by K^t​(ω)=K^t0​(ω)\hat{K}\_{t}(\omega)=\hat{K}^{0}\_{t}(\omega) and we write K^ut,ω​(ω~):=K^u0;t,ω​(ω~)\hat{K}^{t,\omega}\_{u}(\tilde{\omega}):=\hat{K}^{0;t,\omega}\_{u}(\tilde{\omega}).

As the process SS has ℙ\mathbb{P}-a.s. continuous paths, the cone-valued process K^ε\hat{K}^{\varepsilon} is uniquely defined up to indistinguishability and we can introduce process selectors of it with additional path regularity properties. To that end, let 𝔻𝔽0​(ℝd)⊂𝕃𝔽0​(ℝd)\mathbb{D}^{0}\_{\mathbb{F}}(\mathbb{R}^{d})\subset\mathbb{L}^{0}\_{\mathbb{F}}(\mathbb{R}^{d}) denote the space of all 𝔽\mathbb{F}-progressively measurable ℝd\mathbb{R}^{d}-valued càdlàg processes and define the subspace

|  |  |  |
| --- | --- | --- |
|  | 𝔻^𝔽2​(ℝd):={k^∈𝔻𝔽0​(ℝd):diag⁡(S)​k^∈𝕃𝔽2​([0,T]×Ω,ℝd)}.\hat{\mathbb{D}}^{2}\_{\mathbb{F}}(\mathbb{R}^{d}):=\left\{\hat{k}\in\mathbb{D}^{0}\_{\mathbb{F}}(\mathbb{R}^{d})\colon\operatorname{diag}(S)\hat{k}\in\mathbb{L}^{2}\_{\mathbb{F}}([0,T]\times\Omega,\mathbb{R}^{d})\right\}. |  |

Then, the corresponding space of square-integrable portfolio processes in physical units is given by

|  |  |  |
| --- | --- | --- |
|  | 𝔻^𝔽2​(K^ε):=𝔻^𝔽2​(ℝd)∩𝕊𝔽0​(K^ε).\hat{\mathbb{D}}\_{\mathbb{F}}^{2}(\hat{K}^{\varepsilon}):=\hat{\mathbb{D}}^{2}\_{\mathbb{F}}(\mathbb{R}^{d})\cap\mathbb{S}^{0}\_{\mathbb{F}}(\hat{K}^{\varepsilon}). |  |

Note that each k^∈𝔻^𝔽2​(K^ε)\hat{k}\in\hat{\mathbb{D}}^{2}\_{\mathbb{F}}(\hat{K}^{\varepsilon}) satisfies ℙ​{k^r∈K^rε​∀r∈[0,T]}=1\mathbb{P}\{\hat{k}\_{r}\in\hat{K}\_{r}^{\varepsilon}\ \forall r\in[0,T]\}=1. The shifted space 𝔻^𝔽t2​(K^ε;t,ω)\hat{\mathbb{D}}^{2}\_{\mathbb{F}^{t}}(\hat{K}^{\varepsilon;t,\omega}) is defined similarly for each (t,ω)∈[0,T]×Ω(t,\omega)\in[0,T]\times\Omega.

The next lemma is a useful observation about the set-valued functions (𝒦^ε)ε≥0(\hat{\mathscr{K}}^{\varepsilon})\_{\varepsilon\geq 0}.

###### Lemma 5.1.

Let ε1,ε2≥0\varepsilon\_{1},\varepsilon\_{2}\geq 0 and y,y′∈ℝ++dy,y^{\prime}\in\mathbb{R}^{d}\_{++}. If |y−y′|≤ε1|y-y^{\prime}|\leq\varepsilon\_{1}, then 𝒦^ε2​(y)⊆𝒦^ε1+ε2​(y′)\hat{\mathscr{K}}^{\varepsilon\_{2}}(y)\subseteq\hat{\mathscr{K}}^{\varepsilon\_{1}+\varepsilon\_{2}}(y^{\prime}).

Proof. Suppose that |y−y′|≤ε1|y-y^{\prime}|\leq\varepsilon\_{1}. Let x∈𝒦^ε2​(y)x\in\hat{\mathscr{K}}^{\varepsilon\_{2}}(y) and fix some n∈{1,…,N}n\in\{1,\ldots,N\}. Note that (diag⁡(y)​wn)𝖳​x≥−ε2​|x|∞(\operatorname{diag}(y)w^{n})^{\mathsf{T}}x\geq-\varepsilon\_{2}|x|\_{\infty}. Then,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (diag⁡(y′)​wn)𝖳​x\displaystyle(\operatorname{diag}(y^{\prime})w^{n})^{\mathsf{T}}x | =\displaystyle= | (diag⁡(y′−y)​wn)𝖳​x+(diag⁡(y)​wn)𝖳​x\displaystyle(\operatorname{diag}(y^{\prime}-y)w^{n})^{\mathsf{T}}x+(\operatorname{diag}(y)w^{n})^{\mathsf{T}}x |  |
|  |  | ≥\displaystyle\geq | infz∈𝔹ℝd​(ε1)(diag⁡(z)​wn)𝖳​x−ε2​|x|∞\displaystyle\inf\_{z\in\mathbb{B}\_{\mathbb{R}^{d}}(\varepsilon\_{1})}(\operatorname{diag}(z)w^{n})^{\mathsf{T}}x-\varepsilon\_{2}|x|\_{\infty} |  |
|  |  | =\displaystyle= | infz∈𝔹ℝd​(ε1)(diag⁡(x)​wn)𝖳​z−ε2​|x|∞\displaystyle\inf\_{z\in\mathbb{B}\_{\mathbb{R}^{d}}(\varepsilon\_{1})}(\operatorname{diag}(x)w^{n})^{\mathsf{T}}z-\varepsilon\_{2}|x|\_{\infty} |  |
|  |  | =\displaystyle= | −ε1​|diag⁡(x)​wn|−ε2​|x|∞\displaystyle-\varepsilon\_{1}|\operatorname{diag}(x)w^{n}|-\varepsilon\_{2}|x|\_{\infty} |  |
|  |  | ≥\displaystyle\geq | −ε1​|x|∞​|wn|−ε2​|x|∞=−(ε1+ε2)​|x|∞,\displaystyle-\varepsilon\_{1}|x|\_{\infty}|w^{n}|-\varepsilon\_{2}|x|\_{\infty}=-(\varepsilon\_{1}+\varepsilon\_{2})|x|\_{\infty}, |  |

where the evaluation of the infimum follows by a simple geometric observation (or by the definition of dual norm). Hence, x∈𝒦^ε1+ε2​(y′)x\in\hat{\mathscr{K}}^{\varepsilon\_{1}+\varepsilon\_{2}}(y^{\prime}).

Approximate Superhedging Sets. As a financial position to superhedge, we consider a random vector XX that is a deterministic function of the stock price history, i.e., we take X:=g∘SX:=g\circ S for some contract function g:ℂs0​([0,T],ℝd)→ℝdg\colon\mathbb{C}\_{s\_{0}}([0,T],\mathbb{R}^{d})\to\mathbb{R}^{d}, where ℂs0​([0,T],ℝd)\mathbb{C}\_{s\_{0}}([0,T],\mathbb{R}^{d}) is the space of continuous functions f=(ft)t∈[0,T]:[0,T]→ℝdf=(f\_{t})\_{t\in[0,T]}\colon[0,T]\to\mathbb{R}^{d} with f0=s0∈ℝ++df\_{0}=s\_{0}\in\mathbb{R}^{d}\_{++}, equipped with the supremum norm ∥⋅∥∞\|\cdot\|\_{\infty}. We assume that gg satisfies the following two conditions:

1. 1.

   𝔼​[|g∘S|2]<+∞\mathbb{E}[|g\circ S|^{2}]<+\infty, i.e., X∈𝕃ℱT2​(ℝd)X\in\mathbb{L}^{2}\_{{\cal F}\_{T}}(\mathbb{R}^{d}).
2. 2.

   gg is Lipschitz continuous, i.e., there exists L≥1L\geq 1 such that |g​(f)−g​(f′)|≤L​‖f−f′‖∞|g(f)-g(f^{\prime})|\leq L\|f-f^{\prime}\|\_{\infty} for every f,f′∈ℂs0​([0,T],ℝd)f,f^{\prime}\in\mathbb{C}\_{s\_{0}}([0,T],\mathbb{R}^{d}).

Such XX covers most of the frequently used payoff structures of vanilla and exotic options.

Let ε∈[0,1]\varepsilon\in[0,1]. We define the (functional) ε\varepsilon-superhedging set at time t∈[0,T]t\in[0,T] as

|  |  |  |
| --- | --- | --- |
|  | SHPtε(X):={η∈𝕃ℱt2(ℝd):∃k^∈𝔻^𝔽2(ℝd),ℙ{k^r∈K^rε​∀r∈[t,T],η−∫tTk^r​𝑑r+L​ε​𝟏≥X|ℱt}≥1−ε}.SHP\_{t}^{\varepsilon}(X):=\left\{\eta\in\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d})\colon\exists\hat{k}\in\hat{\mathbb{D}}^{2}\_{\mathbb{F}}(\mathbb{R}^{d}),\ \mathbb{P}\left\{\begin{array}[]{@{}c@{}}\hat{k}\_{r}\in\hat{K}\_{r}^{\varepsilon}\ \forall r\in[t,T],\\ \eta-\int\_{t}^{T}\hat{k}\_{r}dr+L\varepsilon{\bf 1}\geq X\end{array}\;\Big|\;{\cal F}\_{t}\right\}\negthinspace\geq\negthinspace 1-\varepsilon\right\}. |  |

Clearly, S​H​Pt0​(X)=S​H​Pt​(X)SHP\_{t}^{0}(X)=SHP\_{t}(X) recovers the superhedging set given in ([4.1](https://arxiv.org/html/2511.18169v1#S4.E1 "In 4 Functional Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")).

Finally, we define the value of the local superhedging problem as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕍t​(ω):=⋂ε∈(0,1]𝕍tε​(ω),(t,ω)∈[0,T]×Ω,\displaystyle\mathbb{V}\_{t}(\omega):=\bigcap\_{\varepsilon\in(0,1]}\mathbb{V}^{\varepsilon}\_{t}(\omega),\quad(t,\omega)\in[0,T]\times\Omega, |  | (5.3) |

where 𝕍tε​(ω):=𝕍~tε​(ω)+𝔹ℝd​(ε)\mathbb{V}^{\varepsilon}\_{t}(\omega):=\tilde{\mathbb{V}}^{\varepsilon}\_{t}(\omega)+\mathbb{B}\_{\mathbb{R}^{d}}(\varepsilon) and

|  |  |  |
| --- | --- | --- |
|  | 𝕍~tε​(ω):={y∈ℝd:∃k^ω∈𝔻^𝔽t2​(ℝd),ℙ​{k^rω∈K^rε;t,ω​∀r∈[t,T],y−∫tTk^rω​𝑑r+L​ε​𝟏≥Xt,ω}≥1−ε}.\displaystyle\tilde{\mathbb{V}}^{\varepsilon}\_{t}(\omega):=\left\{y\in\mathbb{R}^{d}\colon\exists\hat{k}^{\omega}\in\hat{\mathbb{D}}\_{\mathbb{F}^{t}}^{2}(\mathbb{R}^{d}),\ \mathbb{P}\left\{\begin{array}[]{@{}c@{}}\hat{k}\_{r}^{\omega}\in\hat{K}\_{r}^{\varepsilon;t,\omega}\ \forall r\in[t,T],\\ y-\int\_{t}^{T}\hat{k}^{\omega}\_{r}dr+L\varepsilon{\bf 1}\geq X^{t,\omega}\end{array}\right\}\geq 1-\varepsilon\right\}. |  |

Note that 𝕍t0​(ω)⊆𝕍t​(ω)\mathbb{V}\_{t}^{0}(\omega)\subseteq\mathbb{V}\_{t}(\omega) since 𝕍t0​(ω)=𝕍~t0​(ω)⊆𝕍~tε​(ω)⊆𝕍tε​(ω)\mathbb{V}\_{t}^{0}(\omega)=\tilde{\mathbb{V}}^{0}\_{t}(\omega)\subseteq\tilde{\mathbb{V}}^{\varepsilon}\_{t}(\omega)\subseteq\mathbb{V}^{\varepsilon}\_{t}(\omega) for every ε∈(0,1]\varepsilon\in(0,1]. The next lemma makes this observation slightly sharper.

###### Lemma 5.2.

Let 0≤ε′<ε≤10\leq\varepsilon^{\prime}<\varepsilon\leq 1 and (t,ω)∈[0,T]×Ω(t,\omega)\in[0,T]\times\Omega. Then, cl​(𝕍tε′​(ω))⊆𝕍tε​(ω)\mbox{\rm cl}(\mathbb{V}\_{t}^{\varepsilon^{\prime}}(\omega))\subseteq\mathbb{V}\_{t}^{\varepsilon}(\omega).

Proof. Let y∈cl​(𝕍tε′​(ω))y\in\mbox{\rm cl}(\mathbb{V}^{\varepsilon^{\prime}}\_{t}(\omega)). Then, there exists y^∈𝕍tε′​(ω)\hat{y}\in\mathbb{V}\_{t}^{\varepsilon^{\prime}}(\omega) such that |y−y^|≤ε−ε′2|y-\hat{y}|\leq\frac{\varepsilon-\varepsilon^{\prime}}{2}. Since y^∈𝕍tε′​(ω)\hat{y}\in\mathbb{V}^{\varepsilon^{\prime}}\_{t}(\omega), there exists y~∈𝕍~tε′​(ω)\tilde{y}\in\tilde{\mathbb{V}}^{\varepsilon^{\prime}}\_{t}(\omega) such that |y^−y~|≤ε′|\hat{y}-\tilde{y}|\leq\varepsilon^{\prime}. Hence,

|  |  |  |
| --- | --- | --- |
|  | |y−y~|≤|y−y^|+|y^−y~|≤ε−ε′2+ε′≤ε+ε′2≤ε.|y-\tilde{y}|\leq|y-\hat{y}|+|\hat{y}-\tilde{y}|\leq\frac{\varepsilon-\varepsilon^{\prime}}{2}+\varepsilon^{\prime}\leq\frac{\varepsilon+\varepsilon^{\prime}}{2}\leq\varepsilon. |  |

We also have y∈𝕍~tε′​(ω)⊆𝕍~tε​(ω)y\in\tilde{\mathbb{V}}\_{t}^{\varepsilon^{\prime}}(\omega)\subseteq\tilde{\mathbb{V}}\_{t}^{\varepsilon}(\omega). Thus, y~∈𝕍tε​(ω)\tilde{y}\in\mathbb{V}\_{t}^{\varepsilon}(\omega).

As an immediate consequence of Lemma [5.2](https://arxiv.org/html/2511.18169v1#S5.Thmthm2 "Lemma 5.2. ‣ 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time") and the definition in ([5.3](https://arxiv.org/html/2511.18169v1#S5.E3 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕍t​(ω)=⋂ε∈(0,1]cl​(𝕍tε​(ω)).\displaystyle\mathbb{V}\_{t}(\omega)=\bigcap\_{\varepsilon\in(0,1]}\mbox{\rm cl}(\mathbb{V}\_{t}^{\varepsilon}(\omega)). |  | (5.5) |

In particular, 𝕍t​(ω)\mathbb{V}\_{t}(\omega) is a closed set.

Next, we formulate a simple inclusion that connects the functional ε\varepsilon-superhedging set S​H​Ptε​(X)SHP^{\varepsilon}\_{t}(X) and its random set analog cl​(𝕍tε)\mbox{\rm cl}(\mathbb{V}\_{t}^{\varepsilon}).

###### Proposition 5.3.

For every ε∈[0,1]\varepsilon\in[0,1], t∈[0,T]t\in[0,T], it holds cl𝕃2​(S​H​Ptε​(X))⊆𝕊ℱt2​(cl​(𝕍tε))\mbox{\rm cl}\_{\mathbb{L}^{2}}(SHP^{\varepsilon}\_{t}(X))\subseteq\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}^{\varepsilon}\_{t})).

Proof. Since 𝕊ℱt2​(cl​(𝕍tε))\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}^{\varepsilon}\_{t})) is a closed subset of 𝕃ℱt2​(ℝd)\mathbb{L}^{2}\_{{\cal F}\_{t}}(\mathbb{R}^{d}), it is enough to show that S​H​Ptε​(X)⊆𝕊ℱt2​(cl​(𝕍tε))SHP^{\varepsilon}\_{t}(X)\subseteq\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}^{\varepsilon}\_{t})). Let η∈S​H​Ptε​(X)\eta\in SHP^{\varepsilon}\_{t}(X). Hence, there exists k^∈𝔻^𝔽2​(ℝd)\hat{k}\in\hat{\mathbb{D}}^{2}\_{\mathbb{F}}(\mathbb{R}^{d}) such that ℙ​(A|ℱt)≥1−ε\mathbb{P}(A|{\cal F}\_{t})\geq 1-\varepsilon, where

|  |  |  |
| --- | --- | --- |
|  | A:={k^r∈K^rε∀r∈[t,T],η−∫tTk^rdr+Lε𝟏≥X}.A:=\left\{\hat{k}\_{r}\in\hat{K}\_{r}^{\varepsilon}\ \forall r\in[t,T],\ \eta-\int\_{t}^{T}\hat{k}\_{r}dr+L\varepsilon{\bf 1}\geq X\right\}. |  |

Note that for ℙ\mathbb{P}-a.e. ω∈Ω\omega\in\Omega,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(A|ℱt)​(ω)=ℙt,ω​(At,ω)=ℙ​(At,ω).\displaystyle\mathbb{P}(A|{\cal F}\_{t})(\omega)=\mathbb{P}^{t,\omega}(A^{t,\omega})=\mathbb{P}(A^{t,\omega}). |  | (5.6) |

In particular, there exists Ω0∈ℱ\Omega\_{0}\in{\cal F} with ℙ​(Ω0)=1\mathbb{P}(\Omega\_{0})=1 such that ℙ​(At,ω)≥1−ε\mathbb{P}(A^{t,\omega})\geq 1-\varepsilon for every ω∈Ω0\omega\in\Omega\_{0}.

Let us fix ω∈Ω0\omega\in\Omega\_{0}. Note that

|  |  |  |
| --- | --- | --- |
|  | At,ω={k^rt,ω∈K^rε;t,ω∀r∈[t,T],ηt,ω−∫tTk^rt,ωdr+Lε𝟏≥Xt,ω}.A^{t,\omega}=\left\{\hat{k}^{t,\omega}\_{r}\in\hat{K}\_{r}^{\varepsilon;t,\omega}\ \forall r\in[t,T],\ \eta^{t,\omega}-\int\_{t}^{T}\hat{k}^{t,\omega}\_{r}dr+L\varepsilon{\bf 1}\geq X^{t,\omega}\right\}. |  |

Since η\eta is ℱt{\cal F}\_{t}-measurable, its shifted version ηt,ω\eta^{t,\omega} is deterministic, say, ηt,ω=y\eta^{t,\omega}=y ℙ\mathbb{P}-a.s. for some y∈ℝdy\in\mathbb{R}^{d}. Then, we have

|  |  |  |
| --- | --- | --- |
|  | ℙ(At,ω)=ℙ{k^rt,ω∈K^rε;t,ω∀r∈[t,T],y−∫tTk^rt,ωdr+Lε𝟏≥Xt,ω}≥1−ε.\mathbb{P}(A^{t,\omega})=\mathbb{P}\left\{\hat{k}^{t,\omega}\_{r}\in\hat{K}\_{r}^{\varepsilon;t,\omega}\ \forall r\in[t,T],\ y-\int\_{t}^{T}\hat{k}^{t,\omega}\_{r}dr+L\varepsilon{\bf 1}\geq X^{t,\omega}\right\}\geq 1-\varepsilon. |  |

Note that k^t,ω∈𝔻^𝔽t2​(ℝd)\hat{k}^{t,\omega}\in\hat{\mathbb{D}}^{2}\_{\mathbb{F}^{t}}(\mathbb{R}^{d}).
Therefore, y∈𝕍~tε​(ω)⊆cl​(𝕍tε​(ω))y\in\tilde{\mathbb{V}}^{\varepsilon}\_{t}(\omega)\subseteq\mbox{\rm cl}(\mathbb{V}^{\varepsilon}\_{t}(\omega)) so that ηt,ω​(ω~)∈cl​(𝕍tε​(ω))\eta^{t,\omega}(\tilde{\omega})\in\mbox{\rm cl}(\mathbb{V}^{\varepsilon}\_{t}(\omega)) for ℙ\mathbb{P}-a.e. ω~∈Ω\tilde{\omega}\in\Omega. Then, similar to ([5.6](https://arxiv.org/html/2511.18169v1#S5.E6 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) above, we have

|  |  |  |
| --- | --- | --- |
|  | ℙ​{η∈cl​(𝕍tε)}=∫Ω0ℙ​{ηt,ω∈cl​(𝕍tε;t,ω)}​ℙ​(d​ω)=∫Ω0ℙ​{ηt,ω∈cl​(𝕍tε​(ω))}​ℙ​(d​ω)=1,\mathbb{P}\{\eta\in\mbox{\rm cl}(\mathbb{V}^{\varepsilon}\_{t})\}=\int\_{\Omega\_{0}}\mathbb{P}\{\eta^{t,\omega}\in\mbox{\rm cl}(\mathbb{V}\_{t}^{\varepsilon;t,\omega})\}\mathbb{P}(d\omega)=\int\_{\Omega\_{0}}\mathbb{P}\{\eta^{t,\omega}\in\mbox{\rm cl}(\mathbb{V}^{\varepsilon}\_{t}(\omega))\}\mathbb{P}(d\omega)=1, |  |

where the second equality follows since cl​(𝕍tε)\mbox{\rm cl}(\mathbb{V}^{\varepsilon}\_{t}) is ℱt{\cal F}\_{t}-measurable, hence cl​(𝕍tε;t,ω)\mbox{\rm cl}(\mathbb{V}\_{t}^{\varepsilon;t,\omega}) is deterministic for each ω∈Ω0\omega\in\Omega\_{0}. Hence, η∈𝕊ℱt2​(cl​(𝕍tε))\eta\in\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}^{\varepsilon}\_{t})).

In the next proposition, we show that the 𝕃2\mathbb{L}^{2}-selectors of the local superhedging set 𝕍t\mathbb{V}\_{t} can be calculated in terms of the 𝕃2\mathbb{L}^{2}-selectors of its approximate versions.

###### Proposition 5.4.

For every t∈[0,T]t\in[0,T], it holds

|  |  |  |
| --- | --- | --- |
|  | 𝕊ℱt2​(𝕍t)=⋂ε∈(0,1]𝕊ℱt2​(cl​(𝕍tε))=⋂ε∈(0,1](𝕊ℱt2​(cl​(𝕍tε))+𝔹𝕃2​(ε)).\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mathbb{V}\_{t})=\bigcap\_{\varepsilon\in(0,1]}\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}\_{t}^{\varepsilon}))=\bigcap\_{\varepsilon\in(0,1]}\left(\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}\_{t}^{\varepsilon}))+\mathbb{B}\_{\mathbb{L}^{2}}(\varepsilon)\right). |  |

Proof. The ⊆\subseteq parts of both equalities are obvious. We first show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⋂ε∈(0,1]𝕊ℱt2​(cl​(𝕍tε))⊆𝕊ℱt2​(𝕍t).\displaystyle\bigcap\_{\varepsilon\in(0,1]}\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}\_{t}^{\varepsilon}))\subseteq\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mathbb{V}\_{t}). |  | (5.7) |

Let η∈⋂ε∈(0,1]𝕊ℱt2​(cl​(𝕍tε))\eta\in\bigcap\_{\varepsilon\in(0,1]}\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}\_{t}^{\varepsilon})). In particular, η∈𝕊ℱt2​(cl​(𝕍t1n))\eta\in\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}\_{t}^{\frac{1}{n}})) for every n∈ℕn\in\mathbb{N}. By throwing away a ℙ\mathbb{P}-null set for each n∈ℕn\in\mathbb{N}, we see that η∈⋂n∈ℕ(cl​(𝕍t1n))\eta\in\bigcap\_{n\in\mathbb{N}}(\mbox{\rm cl}(\mathbb{V}\_{t}^{\frac{1}{n}})) ℙ\mathbb{P}-a.s. By Lemma [5.2](https://arxiv.org/html/2511.18169v1#S5.Thmthm2 "Lemma 5.2. ‣ 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time") and ([5.5](https://arxiv.org/html/2511.18169v1#S5.E5 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), it is clear that this intersection equals 𝕍t\mathbb{V}\_{t}. Hence, η∈𝕊ℱt2​(𝕍t)\eta\in\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mathbb{V}\_{t}) and ([5.7](https://arxiv.org/html/2511.18169v1#S5.E7 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) follows.

Next, we show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⋂ε∈(0,1](𝕊ℱt2​(cl​(𝕍tε))+𝔹𝕃2​(ε))⊆⋂ε∈(0,1]𝕊ℱt2​(cl​(𝕍tε)).\displaystyle\bigcap\_{\varepsilon\in(0,1]}\left(\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}\_{t}^{\varepsilon}))+\mathbb{B}\_{\mathbb{L}^{2}}(\varepsilon)\right)\subseteq\bigcap\_{\varepsilon\in(0,1]}\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}\_{t}^{\varepsilon})). |  | (5.8) |

Let η\eta belong to the set on the left of ([5.8](https://arxiv.org/html/2511.18169v1#S5.E8 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")). Let us fix ε∈(0,1]\varepsilon\in(0,1]. To show that η∈𝕊ℱt2​(cl​(𝕍tε))\eta\in\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}\_{t}^{\varepsilon})), let us fix an arbitrary δ∈(0,2​ε]\delta\in(0,2\varepsilon]. Then, there exists η~∈𝕊ℱt2​(cl​(𝕍tδ2))\tilde{\eta}\in\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}\_{t}^{\frac{\delta}{2}})) such that

|  |  |  |
| --- | --- | --- |
|  | ‖η−η~‖2≤δ2.\|\eta-\tilde{\eta}\|\_{2}\leq\frac{\delta}{2}. |  |

Since η~∈𝕊ℱt2​(cl​(𝕍tδ2))\tilde{\eta}\in\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}\_{t}^{\frac{\delta}{2}})), by [Molchanov, Theorem 1.3.31, Lemma 2.1.5], there exist η1,…,ηn∈𝕊ℱt2​(𝕍tδ2)\eta^{1},\ldots,\eta^{n}\in\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mathbb{V}\_{t}^{\frac{\delta}{2}}); A1,…,An∈ℱtA\_{1},\ldots,A\_{n}\in{\cal F}\_{t} partitioning Ω\Omega; n∈ℕn\in\mathbb{N} such that

|  |  |  |
| --- | --- | --- |
|  | ‖η~−∑i=1nηi​𝟏Ai‖2≤δ2.\Big\|\tilde{\eta}-\sum\_{i=1}^{n}\eta^{i}{\bf 1}\_{A\_{i}}\Big\|\_{2}\leq\frac{\delta}{2}. |  |

Then,

|  |  |  |
| --- | --- | --- |
|  | ‖η−∑i=1nηi​𝟏Ai‖2≤‖η−η~‖2+‖η~−∑i=1nηi​𝟏Ai‖2≤δ2+δ2=δ.\Big\|\eta-\sum\_{i=1}^{n}\eta^{i}{\bf 1}\_{A\_{i}}\Big\|\_{2}\leq\|\eta-\tilde{\eta}\|\_{2}+\Big\|\tilde{\eta}-\sum\_{i=1}^{n}\eta^{i}{\bf 1}\_{A\_{i}}\Big\|\_{2}\leq\frac{\delta}{2}+\frac{\delta}{2}=\delta. |  |

Moreover, since δ≤2​ε\delta\leq 2\varepsilon, we have ηi∈𝕊ℱt2​(𝕍tδ2)⊆𝕊ℱt2​(𝕍tε)\eta^{i}\in\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mathbb{V}\_{t}^{\frac{\delta}{2}})\subseteq\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mathbb{V}\_{t}^{\varepsilon}) for each i∈{1,…,n}i\in\{1,\ldots,n\}. As δ∈(0,2​ε]\delta\in(0,2\varepsilon] is arbitrary, by [Molchanov, Theorem 1.3.31, Lemma 2.1.5] again, we conclude that η∈𝕊ℱt2​(cl​(𝕍tε))\eta\in\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}\_{t}^{\varepsilon})), proving ([5.8](https://arxiv.org/html/2511.18169v1#S5.E8 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")).

Functional vs. Pathwise Superhedging Sets. The pathwise superhedging set 𝕍t\mathbb{V}\_{t} can naively be considered as a local formulation of the functional superhedging set S​H​Pt​(X)SHP\_{t}(X). The next theorem shows that this is not exactly correct; instead, the set of 𝕃2\mathbb{L}^{2}-selectors of 𝕍t\mathbb{V}\_{t} coincides with the “approximation-closure” of S​H​Pt​(X)SHP\_{t}(X), allowing an infinitesimal approximation error for the superhedging portfolios.

###### Theorem 5.5.

For every t∈[0,T]t\in[0,T], it holds

|  |  |  |
| --- | --- | --- |
|  | 𝕊ℱt2​(𝕍t)=⋂ε∈(0,1](S​H​Ptε​(X)+𝔹𝕃2​(ε)).\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mathbb{V}\_{t})=\bigcap\_{\varepsilon\in(0,1]}\left(SHP\_{t}^{\varepsilon}(X)+\mathbb{B}\_{\mathbb{L}^{2}}(\varepsilon)\right). |  |

Proof. From Propositions [5.3](https://arxiv.org/html/2511.18169v1#S5.Thmthm3 "Proposition 5.3. ‣ 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time") and [5.4](https://arxiv.org/html/2511.18169v1#S5.Thmthm4 "Proposition 5.4. ‣ 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), we have

|  |  |  |
| --- | --- | --- |
|  | ⋂ε∈(0,1](S​H​Ptε​(X)+𝔹𝕃2​(ε))⊆⋂ε∈(0,1](𝕊ℱt2​(cl​(𝕍tε))+𝔹𝕃2​(ε))=𝕊ℱt2​(𝕍t).\bigcap\_{\varepsilon\in(0,1]}\left(SHP\_{t}^{\varepsilon}(X)+\mathbb{B}\_{\mathbb{L}^{2}}(\varepsilon)\right)\subseteq\bigcap\_{\varepsilon\in(0,1]}\left(\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}\_{t}^{\varepsilon}))+\mathbb{B}\_{\mathbb{L}^{2}}(\varepsilon)\right)=\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mathbb{V}\_{t}). |  |

To show the inclusion ⊆\subseteq in the theorem, let η∈𝕊ℱt2​(𝕍t)\eta\in\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mathbb{V}\_{t}) and ε∈(0,1]\varepsilon\in(0,1]. It is enough to find ηε∈S​H​Ptε​(X)\eta\_{\varepsilon}\in SHP\_{t}^{\varepsilon}(X) such that ‖η−ηε‖2≤ε\|\eta-\eta\_{\varepsilon}\|\_{2}\leq\varepsilon.

By Proposition [5.4](https://arxiv.org/html/2511.18169v1#S5.Thmthm4 "Proposition 5.4. ‣ 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), we have η∈𝕊ℱt2​(cl​(𝕍tε2))\eta\in\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mbox{\rm cl}(\mathbb{V}\_{t}^{\frac{\varepsilon}{2}})). Hence, by [Molchanov, Theorem 1.3.31, Lemma 2.1.5], there exist η1,…,ηn∈𝕊ℱt2​(𝕍tε2)\eta^{1},\ldots,\eta^{n}\in\mathbb{S}^{2}\_{{\cal F}\_{t}}(\mathbb{V}\_{t}^{\frac{\varepsilon}{2}}); A1,…,An∈ℱtA\_{1},\ldots,A\_{n}\in{\cal F}\_{t} partitioning Ω\Omega; n∈ℕn\in\mathbb{N} such that

|  |  |  |
| --- | --- | --- |
|  | ‖η−∑i=1nηi​𝟏Ai‖2≤ε2.\Big\|\eta-\sum\_{i=1}^{n}\eta^{i}{\bf 1}\_{A\_{i}}\Big\|\_{2}\leq\frac{\varepsilon}{2}. |  |

By throwing away finitely many null sets from Ω\Omega, without loss of generality, we assume that η​(ω)∈𝕍t​(ω)\eta(\omega)\in\mathbb{V}\_{t}(\omega) and η1​(ω),…,ηn​(ω)∈𝕍tε2​(ω)\eta^{1}(\omega),\ldots,\eta^{n}(\omega)\in\mathbb{V}\_{t}^{\frac{\varepsilon}{2}}(\omega) for every ω∈Ω\omega\in\Omega.

We fix a Borel-measurable partition (Oj)j∈ℕ(O\_{j})\_{j\in\mathbb{N}} of ℝd\mathbb{R}^{d} and a Borel-measurable partition (Cℓ)ℓ∈ℕ(C\_{\ell})\_{\ell\in\mathbb{N}} of ℂs0​([0,T],ℝd)\mathbb{C}\_{s\_{0}}([0,T],\mathbb{R}^{d}) such that, for every j,ℓ∈ℕj,\ell\in\mathbb{N},

|  |  |  |
| --- | --- | --- |
|  | supy,y′∈Oj|y−y′|≤ε2,supf1,f2∈Cℓ‖f1−f2‖∞≤ε​ε2​2​c,\sup\_{y,y^{\prime}\in O\_{j}}|y-y^{\prime}|\leq\frac{\varepsilon}{2},\quad\sup\_{f^{1},f^{2}\in C\_{\ell}}\|f^{1}-f^{2}\|\_{\infty}\leq\frac{\varepsilon\sqrt{\varepsilon}}{2\sqrt{2c}}, |  |

where c≥1c\geq 1 is a constant to be defined later.

For θ:=(i,j,ℓ)∈Θ:={1,…,n}×ℕ×ℕ\theta:=(i,j,\ell)\in\Theta:=\{1,\ldots,n\}\times\mathbb{N}\times\mathbb{N}, let us define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bθ:=Ai∩{ηi∈Oj}∩{St∧⁣⋅∈Cℓ}.\displaystyle B\_{\theta}:=A\_{i}\cap\{\eta^{i}\in O\_{j}\}\cap\{S\_{t\wedge\cdot}\in C\_{\ell}\}. |  | (5.9) |

Then, (Bθ)θ∈Θ(B\_{\theta})\_{\theta\in\Theta} is an ℱt{\cal F}\_{t}-measurable partition of Ω\Omega.

Let us fix θ=(i,j,ℓ)∈Θ\theta=(i,j,\ell)\in\Theta and a representative outcome ωθ∈Bθ\omega^{\theta}\in B\_{\theta}. Since ηi​(ωθ)∈𝕍tε2​(ωθ)\eta^{i}(\omega^{\theta})\in\mathbb{V}\_{t}^{\frac{\varepsilon}{2}}(\omega^{\theta}), there exists yθ∈𝕍~tε2​(ωθ)y^{\theta}\in\tilde{\mathbb{V}}^{\frac{\varepsilon}{2}}\_{t}(\omega^{\theta}) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |yθ−ηi​(ωθ)|≤ε2.\displaystyle|y^{\theta}-\eta^{i}(\omega^{\theta})|\leq\frac{\varepsilon}{2}. |  | (5.10) |

Moreover, since yθ∈𝕍~tε2​(ωθ)y^{\theta}\in\tilde{\mathbb{V}}^{\frac{\varepsilon}{2}}\_{t}(\omega^{\theta}), there exists k^θ∈𝔻^𝔽t2​(ℝd)\hat{k}^{\theta}\in\hat{\mathbb{D}}^{2}\_{\mathbb{F}^{t}}(\mathbb{R}^{d}) such that ℙ​(Fθ)≥1−ε2\mathbb{P}(F\_{\theta})\geq 1-\frac{\varepsilon}{2}, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fθ:={k^rθ∈K^rε2;t,ωθ∀r∈[t,T],yθ−∫tTk^rθdr+Lε2𝟏≥Xt,ωθ}.\displaystyle F\_{\theta}:=\left\{\hat{k}^{\theta}\_{r}\in\hat{K}\_{r}^{\frac{\varepsilon}{2};t,\omega^{\theta}}\ \forall r\in[t,T],\ y^{\theta}-\int\_{t}^{T}\hat{k}^{\theta}\_{r}dr+L\frac{\varepsilon}{2}{\bf 1}\geq X^{t,\omega^{\theta}}\right\}. |  | (5.11) |

Let

|  |  |  |
| --- | --- | --- |
|  | StΘ:=∑θ∈ΘSt​(ωθ)​𝟏Bθ.S^{\Theta}\_{t}:=\sum\_{\theta\in\Theta}S\_{t}(\omega^{\theta}){\bf 1}\_{B\_{\theta}}. |  |

Then, by standard SDE estimates, there exists a constant c≥1c\geq 1 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[supr∈[t,T]|Sr−SrStΘ;t|2∣ℱt]=𝔼​[supr∈[t,T]|SrSt;t−SrStΘ;t|2∣ℱt]≤c​|St−StΘ|2​ℙ​-a.s.\displaystyle\mathbb{E}\left[\sup\_{r\in[t,T]}|S\_{r}-S\_{r}^{S\_{t}^{\Theta};t}|^{2}\mid{\cal F}\_{t}\right]=\mathbb{E}\left[\sup\_{r\in[t,T]}|S\_{r}^{S\_{t};t}-S\_{r}^{S\_{t}^{\Theta};t}|^{2}\mid{\cal F}\_{t}\right]\leq c|S\_{t}-S\_{t}^{\Theta}|^{2}\;\mathbb{P}\text{-a.s.}\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace |  | (5.12) |

Let ω∈Bθ\omega\in B\_{\theta}. Similar to the derivation of ([5.2](https://arxiv.org/html/2511.18169v1#S5.E2 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), it is easy to observe that (SStΘ;t)t,ω(S^{S^{\Theta}\_{t};t})^{t,\omega} has the same dynamics as in ([5.2](https://arxiv.org/html/2511.18169v1#S5.E2 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) but with initial condition (StStΘ;t)t,ω=St​(ωθ)(S\_{t}^{S^{\Theta}\_{t};t})^{t,\omega}=S\_{t}(\omega^{\theta}). Hence, by the uniqueness of the solution of the SDE, we have (SStΘ;t)t,ω=St,ωθ(S^{S^{\Theta}\_{t};t})^{t,\omega}=S^{t,\omega^{\theta}} ℙ\mathbb{P}-a.s. After using this with ([5.1](https://arxiv.org/html/2511.18169v1#S5.E1 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) and ([5.9](https://arxiv.org/html/2511.18169v1#S5.E9 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), ([5.12](https://arxiv.org/html/2511.18169v1#S5.E12 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) implies that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supr∈[t,T]|Srt,ω−Srt,ωθ|2]≤c​|St​(ω)−St​(ωθ)|2≤c​ε38​c=ε38\mathbb{E}\left[\sup\_{r\in[t,T]}|S\_{r}^{t,\omega}-S\_{r}^{t,\omega^{\theta}}|^{2}\right]\leq c|S\_{t}(\omega)-S\_{t}(\omega^{\theta})|^{2}\leq c\frac{\varepsilon^{3}}{8c}=\frac{\varepsilon^{3}}{8} |  |

for ℙ\mathbb{P}-a.e. ω∈Bθ\omega\in B\_{\theta}. Let us define

|  |  |  |
| --- | --- | --- |
|  | E:={supr∈[t,T]|Sr−SrStΘ;t|≤ε2}E:=\left\{\sup\_{r\in[t,T]}|S\_{r}-S\_{r}^{S\_{t}^{\Theta};t}|\leq\frac{\varepsilon}{2}\right\} |  |

so that, whenever ω∈Bθ\omega\in B\_{\theta}, we have

|  |  |  |
| --- | --- | --- |
|  | Et,ω={supr∈[t,T]|Srt,ω−Srt,ωθ|≤ε2}.E^{t,\omega}=\left\{\sup\_{r\in[t,T]}|S\_{r}^{t,\omega}-S\_{r}^{t,\omega^{\theta}}|\leq\frac{\varepsilon}{2}\right\}. |  |

Then, by Markov inequality, we have

|  |  |  |
| --- | --- | --- |
|  | 1−ℙ​(Et,ω)=ℙ​{supr∈[t,T]|Srt,ω−Srt,ωθ|2>ε24}≤ε38ε24=ε2,1-\mathbb{P}(E^{t,\omega})=\mathbb{P}\left\{\sup\_{r\in[t,T]}|S\_{r}^{t,\omega}-S\_{r}^{t,\omega^{\theta}}|^{2}>\frac{\varepsilon^{2}}{4}\right\}\leq\frac{\frac{\varepsilon^{3}}{8}}{\frac{\varepsilon^{2}}{4}}=\frac{\varepsilon}{2}, |  |

and hence ℙ​(Et,ω)≥1−ε2\mathbb{P}(E^{t,\omega})\geq 1-\frac{\varepsilon}{2} for ℙ\mathbb{P}-a.e. ω∈Bθ\omega\in B\_{\theta}.

Let ω∈Bθ\omega\in B\_{\theta} be such that ℙ​(Et,ω)≥1−ε2\mathbb{P}(E^{t,\omega})\geq 1-\frac{\varepsilon}{2}. Then, for every ω~∈Ω\tilde{\omega}\in\Omega, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |Xt,ω​(ω~)−Xt,ωθ​(ω~)|\displaystyle|X^{t,\omega}(\tilde{\omega})-X^{t,\omega^{\theta}}(\tilde{\omega})| | =\displaystyle= | |g​(St,ω​(ω~))−g​(St,ωθ​(ω~))|\displaystyle|g(S^{t,\omega}(\tilde{\omega}))-g(S^{t,\omega^{\theta}}(\tilde{\omega}))| |  |
|  |  | ≤\displaystyle\leq | L​‖St,ω​(ω~)−St,ωθ​(ω~)‖∞\displaystyle L\|S^{t,\omega}(\tilde{\omega})-S^{t,\omega^{\theta}}(\tilde{\omega})\|\_{\infty} |  |
|  |  | =\displaystyle= | L​max⁡{‖St∧⁣⋅​(ω)−St∧⁣⋅​(ωθ)‖∞,supr∈[t,T]|Srt,ω​(ω~)−Srt,ωθ​(ω~)|}\displaystyle L\max\left\{\|S\_{t\wedge\cdot}(\omega)-S\_{t\wedge\cdot}(\omega^{\theta})\|\_{\infty},\sup\_{r\in[t,T]}|S^{t,\omega}\_{r}(\tilde{\omega})-S^{t,\omega^{\theta}}\_{r}(\tilde{\omega})|\right\} |  |
|  |  | ≤\displaystyle\leq | L​max⁡{ε​ε2​2​c,supr∈[t,T]|Srt,ω​(ω~)−Srt,ωθ​(ω~)|}.\displaystyle L\max\left\{\frac{\varepsilon\sqrt{\varepsilon}}{2\sqrt{2c}},\sup\_{r\in[t,T]}|S^{t,\omega}\_{r}(\tilde{\omega})-S^{t,\omega^{\theta}}\_{r}(\tilde{\omega})|\right\}. |  |

Let us fix ω~∈Et,ω\tilde{\omega}\in E^{t,\omega}. Then, we also have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Xt,ω​(ω~)−Xt,ωθ​(ω~)|≤L​max⁡{ε​ε2​2​c,ε2}=L​ε2​max⁡{ε2​c,1}=L​ε2\displaystyle|X^{t,\omega}(\tilde{\omega})-X^{t,\omega^{\theta}}(\tilde{\omega})|\leq L\max\left\{\frac{\varepsilon\sqrt{\varepsilon}}{2\sqrt{2c}},\frac{\varepsilon}{2}\right\}=L\frac{\varepsilon}{2}\max\left\{\sqrt{\frac{\varepsilon}{2c}},1\right\}=L\frac{\varepsilon}{2} |  | (5.13) |

since we have ε≤1≤c≤2​c\varepsilon\leq 1\leq c\leq 2c.

Now, let us suppose further that ω~∈Et,ω∩Fθ\tilde{\omega}\in E^{t,\omega}\cap F\_{\theta}. Then, using ([5.13](https://arxiv.org/html/2511.18169v1#S5.E13 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) in ([5.11](https://arxiv.org/html/2511.18169v1#S5.E11 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we obtain

|  |  |  |
| --- | --- | --- |
|  | yθ−∫tTk^rθ​(ω~)​𝑑r+L​ε2​𝟏≥Xt,ωθ​(ω~)≥Xt,ω​(ω~)−L​ε2​𝟏,y^{\theta}-\int\_{t}^{T}\hat{k}\_{r}^{\theta}(\tilde{\omega})dr+L\frac{\varepsilon}{2}{\bf 1}\geq X^{t,\omega^{\theta}}(\tilde{\omega})\geq X^{t,\omega}(\tilde{\omega})-L\frac{\varepsilon}{2}{\bf 1}, |  |

which implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | yθ−∫tTk^rθ​(ω~)​𝑑r+L​ε​𝟏≥Xt,ω​(ω~).\displaystyle y^{\theta}-\int\_{t}^{T}\hat{k}\_{r}^{\theta}(\tilde{\omega})dr+L\varepsilon{\bf 1}\geq X^{t,\omega}(\tilde{\omega}). |  | (5.14) |

Moreover, by Lemma [5.1](https://arxiv.org/html/2511.18169v1#S5.Thmthm1 "Lemma 5.1. ‣ 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), having k^rθ​(ω~)∈𝒦^ε2​(Srt,ωθ​(ω~))\hat{k}^{\theta}\_{r}(\tilde{\omega})\in\hat{\mathscr{K}}^{\frac{\varepsilon}{2}}(S\_{r}^{t,\omega^{\theta}}(\tilde{\omega})) and |Srt,ω​(ω~)−Srt,ωθ​(ω~)|≤ε2|S\_{r}^{t,\omega}(\tilde{\omega})-S\_{r}^{t,\omega^{\theta}}(\tilde{\omega})|\leq\frac{\varepsilon}{2}, we conclude for each r∈[t,T]r\in[t,T] that

|  |  |  |  |
| --- | --- | --- | --- |
|  | k^rθ​(ω~)∈𝒦^ε​(Srt,ω​(ω~))=K^rε;t,ω​(ω~).\displaystyle\hat{k}^{\theta}\_{r}(\tilde{\omega})\in\hat{\mathscr{K}}^{\varepsilon}(S^{t,\omega}\_{r}(\tilde{\omega}))=\hat{K}\_{r}^{\varepsilon;t,\omega}(\tilde{\omega}). |  | (5.15) |

Let us define

|  |  |  |
| --- | --- | --- |
|  | ηε​(ω):=∑θ∈Θyθ​𝟏Bθ​(ω)\eta\_{\varepsilon}(\omega):=\sum\_{\theta\in\Theta}y^{\theta}{\bf 1}\_{B\_{\theta}}(\omega) |  |

and

|  |  |  |
| --- | --- | --- |
|  | k^r​(ω):=k^r0​(ω)​𝟏[0,t)​(r)+𝟏[t,T]​(r)​∑θ∈Θk^rθ​(W~​(ω))​𝟏Bθ​(ω),\hat{k}\_{r}(\omega):=\hat{k}^{0}\_{r}(\omega){\bf 1}\_{[0,t)}(r)+{\bf 1}\_{[t,T]}(r)\sum\_{\theta\in\Theta}\hat{k}^{\theta}\_{r}(\tilde{W}(\omega)){\bf 1}\_{B\_{\theta}}(\omega), |  |

where k^0∈𝔻^𝔽2​(ℝd)\hat{k}^{0}\in\hat{\mathbb{D}}\_{\mathbb{F}}^{2}(\mathbb{R}^{d}) is arbitrarily fixed and W~:Ω→Ω\tilde{W}\colon\Omega\to\Omega is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | W~u​(ω):=(ωu+t−ωt)​𝟏[0,T−t)​(u)+(ωT−ωt)​𝟏[T−t,T]​(u),u∈[0,T],\displaystyle\tilde{W}\_{u}(\omega):=(\omega\_{u+t}-\omega\_{t}){\bf 1}\_{[0,T-t)}(u)+(\omega\_{T}-\omega\_{t}){\bf 1}\_{[T-t,T]}(u),\quad u\in[0,T], |  | (5.16) |

for each ω∈Ω\omega\in\Omega. Then, these definitions guarantee that k^∈𝔻^𝔽2​(ℝd)\hat{k}\in\hat{\mathbb{D}}^{2}\_{\mathbb{F}}(\mathbb{R}^{d}) and, for every ω~∈Et,ω\tilde{\omega}\in E^{t,\omega} and r∈[t,T]r\in[t,T], we have k^rt,ω​(ω~)=k^rθ​(ω~)∈K^rε;t,ω​(ω~)\hat{k}^{t,\omega}\_{r}(\tilde{\omega})=\hat{k}\_{r}^{\theta}(\tilde{\omega})\in\hat{K}\_{r}^{\varepsilon;t,\omega}(\tilde{\omega}) and (ηε)t,ω​(ω~)=yθ(\eta\_{\varepsilon})^{t,\omega}(\tilde{\omega})=y^{\theta}. In particular, by ([5.14](https://arxiv.org/html/2511.18169v1#S5.E14 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) and ([5.15](https://arxiv.org/html/2511.18169v1#S5.E15 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we get

|  |  |  |
| --- | --- | --- |
|  | ℙ{k^rt,ω∈K^rε;t,ω∀r∈[t,T],(ηε)t,ω−∫tTk^rt,ωdr+Lε𝟏≥Xt,ω}\displaystyle\mathbb{P}\left\{\hat{k}^{t,\omega}\_{r}\in\hat{K}^{\varepsilon;t,\omega}\_{r}\ \forall r\in[t,T],\ (\eta\_{\varepsilon})^{t,\omega}-\int\_{t}^{T}\hat{k}^{t,\omega}\_{r}dr+L\varepsilon{\bf 1}\geq X^{t,\omega}\right\} |  |
|  |  |  |
| --- | --- | --- |
|  | ≥ℙ​(Et,ω∩Fθ)≥ℙ​(Et,ω)+ℙ​(Fθ)−1≥(1−ε2)+(1−ε2)−1=1−ε.\displaystyle\geq\mathbb{P}(E^{t,\omega}\cap F\_{\theta})\geq\mathbb{P}(E^{t,\omega})+\mathbb{P}(F\_{\theta})-1\geq\left(1-\frac{\varepsilon}{2}\right)+\left(1-\frac{\varepsilon}{2}\right)-1=1-\varepsilon. |  |

Equivalently, we have

|  |  |  |
| --- | --- | --- |
|  | ℙ{k^r∈K^rε∀r∈[t,T],ηε−∫tTk^rdr+Lε𝟏≥X∣ℱt}≥1−εℙ-a.s.\mathbb{P}\left\{\hat{k}\_{r}\in\hat{K}^{\varepsilon}\_{r}\ \forall r\in[t,T],\ \eta\_{\varepsilon}-\int\_{t}^{T}\hat{k}\_{r}dr+L\varepsilon{\bf 1}\geq X\mid{\cal F}\_{t}\right\}\geq 1-\varepsilon\quad\mathbb{P}\text{-a.s.} |  |

Hence, ηε∈S​H​Ptε​(X)\eta\_{\varepsilon}\in SHP^{\varepsilon}\_{t}(X).

Finally, note that

|  |  |  |
| --- | --- | --- |
|  | ‖η−ηε‖2≤‖η−∑i=1nηi​𝟏Ai‖2+‖∑i=1nηi​𝟏Ai−ηε‖2≤ε2+‖∑θ=(i,j,ℓ)∈Θ(ηi−yθ)​𝟏Bθ‖2≤ε\left\|\eta-\eta\_{\varepsilon}\right\|\_{2}\leq\Big\|\eta-\sum\_{i=1}^{n}\eta^{i}{\bf 1}\_{A\_{i}}\Big\|\_{2}+\Big\|\sum\_{i=1}^{n}\eta^{i}{\bf 1}\_{A\_{i}}-\eta\_{\varepsilon}\Big\|\_{2}\leq\frac{\varepsilon}{2}+\Big\|\sum\_{\theta=(i,j,\ell)\in\Theta}(\eta^{i}-y^{\theta}){\bf 1}\_{B\_{\theta}}\Big\|\_{2}\leq\varepsilon |  |

since, for ω∈Bθ\omega\in B\_{\theta} with θ=(i,j,ℓ)\theta=(i,j,\ell), we have |ηi​(ω)−yθ|≤|ηi​(ω)−ηi​(ωθ)|+|ηi​(ωθ)−yθ|≤ε2|\eta^{i}(\omega)-y^{\theta}|\leq|\eta^{i}(\omega)-\eta^{i}(\omega^{\theta})|+|\eta^{i}(\omega^{\theta})-y^{\theta}|\leq\frac{\varepsilon}{2} by ([5.9](https://arxiv.org/html/2511.18169v1#S5.E9 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) and ([5.10](https://arxiv.org/html/2511.18169v1#S5.E10 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")). Therefore, η∈S​H​Ptε​(X)+𝔹𝕃2​(ε)\eta\in SHP^{\varepsilon}\_{t}(X)+\mathbb{B}\_{\mathbb{L}^{2}}(\varepsilon).

The Pathwise Dynamic Programming Principle. We begin with a lemma that will be used in the proof of the main result. It provides a simple one-sided concentration inequality for conditional expectations; we include its short proof for completeness.

###### Lemma 5.6.

Let 𝒢{\cal G} be a sub-σ\sigma-algebra of ℱ{\cal F}. Let A∈ℱA\in{\cal F} and ε∈(0,1]\varepsilon\in(0,1]. Then, the following implication holds:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(A)≤ε⇒ℙ​{ℙ​(A|𝒢)≥ε}≤ε.\mathbb{P}(A)\leq\varepsilon\quad\Rightarrow\quad\mathbb{P}\{\mathbb{P}(A|{\cal G})\geq\sqrt{\varepsilon}\}\leq\sqrt{\varepsilon}. |  |

Proof. Let Y:Ω→ℝ+Y\colon\Omega\to\mathbb{R}\_{+} be an ℱ{\cal F}-measurable random variable such that 𝔼​[Y]≤ε\mathbb{E}[Y]\leq\varepsilon. Let δ>0\delta>0. Then, we have ε≥𝔼​[Y]=𝔼​[Y​𝟏{Y≥δ}]+𝔼​[Y​𝟏{Y<δ}]≥δ​ℙ​{Y≥δ}\varepsilon\geq\mathbb{E}[Y]=\mathbb{E}[Y{\bf 1}\_{\{Y\geq\delta\}}]+\mathbb{E}[Y{\bf 1}\_{\{Y<\delta\}}]\geq\delta\mathbb{P}\{Y\geq\delta\}, which implies that ℙ​{Y≥δ}≤εδ\mathbb{P}\{Y\geq\delta\}\leq\frac{\varepsilon}{\delta}. In particular, taking δ=ε\delta=\sqrt{\varepsilon} gives ℙ​{Y≥ε}≤ε\mathbb{P}\{Y\geq\sqrt{\varepsilon}\}\leq\sqrt{\varepsilon}. Finally, by taking Y=ℙ​(A|𝒢)Y=\mathbb{P}(A|{\cal G}), the lemma follows since 𝔼​[Y]=ℙ​(A)\mathbb{E}[Y]=\mathbb{P}(A) by tower property.

To formulate the pathwise dynamic programming principle, we generalize the concept of a superhedging portfolio for a subinterval of [0,T][0,T] next.

###### Definition 5.7.

Let ω∈Ω\omega\in\Omega, 0≤t≤u≤T0\leq t\leq u\leq T, and ε∈[0,1]\varepsilon\in[0,1]. We say that a vector y∈ℝdy\in\mathbb{R}^{d} is an ε\varepsilon-superhedging portfolio at ω\omega over [t,u][t,u] if there exist a strategy k^ω∈𝔻^𝔽t2​(ℝd)\hat{k}^{\omega}\in\hat{\mathbb{D}}^{2}\_{\mathbb{F}^{t}}(\mathbb{R}^{d}) and a target claim ξ∈𝕃ℱu2​(ℝd)\xi\in\mathbb{L}^{2}\_{{\cal F}\_{u}}(\mathbb{R}^{d}) at time uu such that the following conditions are satisfied:

1. Approximate feasibility of the target: It holds ℙ​{ξ∈𝕍uε;t,ω}≥1−ε\mathbb{P}\{\xi\in\mathbb{V}\_{u}^{\varepsilon;t,\omega}\}\geq 1-\varepsilon.

2. Approximate superhedging over [t,u][t,u]: It holds

|  |  |  |
| --- | --- | --- |
|  | ℙ{k^rω∈K^rε;t,ω∀r∈[t,u],y−∫tuk^rωdr+Lε𝟏≥ξt,ω}≥1−ε.\mathbb{P}\left\{\hat{k}^{\omega}\_{r}\in\hat{K}\_{r}^{\varepsilon;t,\omega}\ \forall r\in[t,u],\ y-\int\_{t}^{u}\hat{k}^{\omega}\_{r}dr+L\varepsilon{\bf 1}\geq\xi^{t,\omega}\right\}\geq 1-\varepsilon. |  |

We denote 𝕍~t,uε​(ω)\tilde{\mathbb{V}}\_{t,u}^{\varepsilon}(\omega) to be the set of all ε\varepsilon-superhedging portfolios at ω\omega over [t,u][t,u].

The next theorem is the main result of this section. It relates the pathwise superhedging sets at different times through a *set-valued dynamic programming principle*.

###### Theorem 5.8.

Let ω∈Ω\omega\in\Omega and 0≤t≤u≤T0\leq t\leq u\leq T. Then, it holds

|  |  |  |
| --- | --- | --- |
|  | 𝕍t​(ω)=⋂ε∈(0,1](𝕍~t,uε​(ω)+𝔹ℝd​(ε)).\mathbb{V}\_{t}(\omega)=\bigcap\_{\varepsilon\in(0,1]}\left(\tilde{\mathbb{V}}\_{t,u}^{\varepsilon}(\omega)+\mathbb{B}\_{\mathbb{R}^{d}}(\varepsilon)\right). |  |

Proof: To avoid dealing with complicated notation, we will prove the theorem for the case t=0t=0 and ω≡0\omega\equiv 0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕍0​(0)=⋂ε∈(0,1](𝕍~0,uε​(0)+𝔹ℝd​(ε)),\displaystyle\mathbb{V}\_{0}(0)=\bigcap\_{\varepsilon\in(0,1]}\left(\tilde{\mathbb{V}}\_{0,u}^{\varepsilon}(0)+\mathbb{B}\_{\mathbb{R}^{d}}(\varepsilon)\right), |  | (5.17) |

where 𝕍~0,uε​(0)\tilde{\mathbb{V}}^{\varepsilon}\_{0,u}(0) simplifies as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝕍~0,uε​(0)=\displaystyle\tilde{\mathbb{V}}^{\varepsilon}\_{0,u}(0)= | {y∈ℝd:∃k^∈𝔻^𝔽2​(ℝd),∃ξ∈𝕃ℱu2​(ℝd),ℙ​{ξ∈𝕍uε}≥1−ε,ℙ{k^r∈K^rε∀r∈[0,u],y−∫0uk^rdr+Lε𝟏≥ξ}≥1−ε}.\displaystyle\left\{y\in\mathbb{R}^{d}\colon\begin{array}[]{l}\exists\hat{k}\in\hat{\mathbb{D}}^{2}\_{\mathbb{F}}(\mathbb{R}^{d}),\ \exists\xi\in\mathbb{L}^{2}\_{{\cal F}\_{u}}(\mathbb{R}^{d}),\quad\mathbb{P}\{\xi\in\mathbb{V}^{\varepsilon}\_{u}\}\geq 1-\varepsilon,\\ \mathbb{P}\left\{\hat{k}\_{r}\in\hat{K}\_{r}^{\varepsilon}\ \forall r\in[0,u],\ y-\int\_{0}^{u}\hat{k}\_{r}dr+L\varepsilon{\bf 1}\geq\xi\right\}\geq 1-\varepsilon\end{array}\right\}. |  |  |

The proof of the general case works similarly.

To prove the inclusion ⊆\subseteq in ([5.17](https://arxiv.org/html/2511.18169v1#S5.E17 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), let y∈𝕍0​(0)y\in\mathbb{V}\_{0}(0) and fix ε∈(0,1]\varepsilon\in(0,1]. We aim to find y¯∈𝕍~0,uε​(0)\bar{y}\in\tilde{\mathbb{V}}\_{0,u}^{\varepsilon}(0) such that |y−y¯|≤ε|y-\bar{y}|\leq\varepsilon.

Let δ∈(0,ε]\delta\in(0,\varepsilon] to be chosen later depending on ε\varepsilon. By ([5.3](https://arxiv.org/html/2511.18169v1#S5.E3 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), there exists yδ∈𝕍~0δ​(0)y^{\delta}\in\tilde{\mathbb{V}}\_{0}^{\delta}(0) such that |y−yδ|≤δ|y-y^{\delta}|\leq\delta. Since yδ∈𝕍~0δ​(0)y^{\delta}\in\tilde{\mathbb{V}}\_{0}^{\delta}(0), there exists k^δ∈𝔻^𝔽2​(ℝd)\hat{k}^{\delta}\in\hat{\mathbb{D}}^{2}\_{\mathbb{F}}(\mathbb{R}^{d}) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ{k^rδ∈K^rδ∀r∈[0,T],yδ−∫0Tk^rδdr+Lδ𝟏≥X}≥1−δ.\displaystyle\mathbb{P}\left\{\hat{k}^{\delta}\_{r}\in\hat{K}\_{r}^{\delta}\ \forall r\in[0,T],\ y^{\delta}-\int\_{0}^{T}\hat{k}\_{r}^{\delta}dr+L\delta{\bf 1}\geq X\right\}\geq 1-\delta. |  | (5.19) |

Let ξδ:=yδ−∫0uk^rδ​𝑑r∈𝕃ℱu2​(ℝd)\xi^{\delta}:=y^{\delta}-\int\_{0}^{u}\hat{k}^{\delta}\_{r}dr\in\mathbb{L}^{2}\_{{\cal F}\_{u}}(\mathbb{R}^{d}). Obviously, we have

|  |  |  |
| --- | --- | --- |
|  | yδ−∫0uk^rδ​𝑑r+L​δ​𝟏≥ξδℙ​-a.s.y^{\delta}-\int\_{0}^{u}\hat{k}\_{r}^{\delta}dr+L\delta{\bf 1}\geq\xi^{\delta}\quad\mathbb{P}\text{-a.s.} |  |

This, together with ([5.19](https://arxiv.org/html/2511.18169v1#S5.E19 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), implies that

|  |  |  |
| --- | --- | --- |
|  | ℙ{k^rδ∈K^rδ∀r∈[0,u],yδ−∫0uk^rδdr+Lδ𝟏≥ξδ}≥1−δ.\mathbb{P}\left\{\hat{k}^{\delta}\_{r}\in\hat{K}^{\delta}\_{r}\ \forall r\in[0,u],\ y^{\delta}-\int\_{0}^{u}\hat{k}\_{r}^{\delta}dr+L\delta{\bf 1}\geq\xi^{\delta}\right\}\geq 1-\delta. |  |

Since we assume that δ≤ε\delta\leq\varepsilon, we also have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ{k^rδ∈K^rε∀r∈[0,u],yδ−∫0uk^rδdr+Lε𝟏≥ξδ}≥1−ε.\displaystyle\mathbb{P}\left\{\hat{k}^{\delta}\_{r}\in\hat{K}^{\varepsilon}\_{r}\ \forall r\in[0,u],\ y^{\delta}-\int\_{0}^{u}\hat{k}\_{r}^{\delta}dr+L\varepsilon{\bf 1}\geq\xi^{\delta}\right\}\geq 1-\varepsilon. |  | (5.20) |

Moreover, by ([5.19](https://arxiv.org/html/2511.18169v1#S5.E19 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we have ℙ​(B)≥1−δ\mathbb{P}(B)\geq 1-\delta, where

|  |  |  |
| --- | --- | --- |
|  | B:={k^rδ∈K^rδ∀r∈[u,T],ξδ−∫uTk^rδdr+Lδ𝟏≥X}.B:=\left\{\hat{k}^{\delta}\_{r}\in\hat{K}^{\delta}\_{r}\ \forall r\in[u,T],\ \xi^{\delta}-\int\_{u}^{T}\hat{k}\_{r}^{\delta}dr+L\delta{\bf 1}\geq X\right\}. |  |

Then, by applying Lemma [5.6](https://arxiv.org/html/2511.18169v1#S5.Thmthm6 "Lemma 5.6. ‣ 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time") to the event BcB^{c}, we get ℙ​{ℙ​(Bc|ℱu)≥δ}≤δ\mathbb{P}\{\mathbb{P}(B^{c}|{\cal F}\_{u})\geq\sqrt{\delta}\}\leq\sqrt{\delta}, or equivalently, ℙ​{ℙ​(B|ℱu)>1−δ}≥1−δ\mathbb{P}\{\mathbb{P}(B|{\cal F}\_{u})>1-\sqrt{\delta}\}\geq 1-\sqrt{\delta}. Hence, we choose δ=ε2∈(0,ε]\delta=\varepsilon^{2}\in(0,\varepsilon] and obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​{ℙ​(B|ℱu)>1−ε}≥1−ε.\displaystyle\mathbb{P}\{\mathbb{P}(B|{\cal F}\_{u})>1-\varepsilon\}\geq 1-\varepsilon. |  | (5.21) |

Note that ℙ​(B|ℱu)​(ω)=ℙ​(Bu,ω)\mathbb{P}(B|{\cal F}\_{u})(\omega)=\mathbb{P}(B^{u,\omega}) for ℙ\mathbb{P}-a.e. ω∈Ω\omega\in\Omega, where

|  |  |  |
| --- | --- | --- |
|  | Bu,ω={(k^rε2)u,ω∈K^rε2;u,ω∀r∈[u,T],(ξε2)u,ω−∫uT(k^rε2)u,ωdr+Lε2𝟏≥Xu,ω}.B^{u,\omega}=\left\{(\hat{k}\_{r}^{\varepsilon^{2}})^{u,\omega}\in\hat{K}\_{r}^{\varepsilon^{2};u,\omega}\ \forall r\in[u,T],\ (\xi^{\varepsilon^{2}})^{u,\omega}-\int\_{u}^{T}(\hat{k}^{\varepsilon^{2}}\_{r})^{u,\omega}dr+L\varepsilon^{2}{\bf 1}\geq X^{u,\omega}\right\}. |  |

Let Ω¯:={ω∈Ω:ξε2​(ω)=𝔼​[(ξε2)u,ω]}\bar{\Omega}:=\{\omega\in\Omega\colon\xi^{\varepsilon^{2}}(\omega)=\mathbb{E}[(\xi^{\varepsilon^{2}})^{u,\omega}]\}. Since ξε2\xi^{\varepsilon^{2}} is ℱu{\cal F}\_{u}-measurable, we have ℙ​(Ω¯)=1\mathbb{P}(\bar{\Omega})=1. We claim that

|  |  |  |  |
| --- | --- | --- | --- |
|  | {ω∈Ω¯:ℙ​(Bu,ω)≥1−ε}⊆{ω∈Ω¯:ξε2​(ω)∈𝕍uε​(ω)}.\displaystyle\{\omega\in\bar{\Omega}\colon\mathbb{P}(B^{u,\omega})\geq 1-\varepsilon\}\subseteq\{\omega\in\bar{\Omega}\colon\xi^{\varepsilon^{2}}(\omega)\in\mathbb{V}\_{u}^{\varepsilon}(\omega)\}. |  | (5.22) |

To see this, let ω∈Ω¯\omega\in\bar{\Omega} be such that ℙ​(Bu,ω)≥1−ε\mathbb{P}(B^{u,\omega})\geq 1-\varepsilon. Let us take k^ω:=(k^ε2)u,ω∈𝔻^𝔽u2​(ℝd)\hat{k}^{\omega}:=(\hat{k}^{\varepsilon^{2}})^{u,\omega}\in\hat{\mathbb{D}}^{2}\_{\mathbb{F}^{u}}(\mathbb{R}^{d}). Since ξε2\xi^{\varepsilon^{2}} is ℱu{\cal F}\_{u}-measurable, (ξε2)u,ω(\xi^{\varepsilon^{2}})^{u,\omega} is deterministic ℙ\mathbb{P}-a.s.; hence, (ξε2)u,ω=𝔼​[(ξε2)u,ω]=ξε2​(ω)(\xi^{\varepsilon^{2}})^{u,\omega}=\mathbb{E}[(\xi^{\varepsilon^{2}})^{u,\omega}]=\xi^{\varepsilon^{2}}(\omega) ℙ\mathbb{P}-a.s. because ω∈Ω¯\omega\in\bar{\Omega}. Let yω:=ξε2​(ω)y^{\omega}:=\xi^{\varepsilon^{2}}(\omega). Then, since ℙ​(Bu,ω)≥1−ε\mathbb{P}(B^{u,\omega})\geq 1-\varepsilon, we have

|  |  |  |
| --- | --- | --- |
|  | ℙ{k^rω∈K^rε;u,ω∀r∈[u,T],yω−∫uTk^rωdr+Lε𝟏≥Xu,ω}\displaystyle\mathbb{P}\left\{\hat{k}^{\omega}\_{r}\in\hat{K}\_{r}^{\varepsilon;u,\omega}\ \forall r\in[u,T],\ y^{\omega}-\int\_{u}^{T}\hat{k}^{\omega}\_{r}dr+L\varepsilon{\bf 1}\geq X^{u,\omega}\right\} |  |
|  |  |  |
| --- | --- | --- |
|  | ≥ℙ{k^rω∈K^rε2;u,ω∀r∈[u,T],yω−∫uTk^rωdr+Lε2𝟏≥Xu,ω}≥1−ε.\displaystyle\geq\mathbb{P}\left\{\hat{k}^{\omega}\_{r}\in\hat{K}\_{r}^{\varepsilon^{2};u,\omega}\ \forall r\in[u,T],\ y^{\omega}-\int\_{u}^{T}\hat{k}^{\omega}\_{r}dr+L\varepsilon^{2}{\bf 1}\geq X^{u,\omega}\right\}\geq 1-\varepsilon. |  |

Hence, ξε2​(ω)=yω∈𝕍~uε​(ω)⊆𝕍uε​(ω)\xi^{\varepsilon^{2}}(\omega)=y^{\omega}\in\tilde{\mathbb{V}}\_{u}^{\varepsilon}(\omega)\subseteq\mathbb{V}\_{u}^{\varepsilon}(\omega), which finishes the proof of ([5.22](https://arxiv.org/html/2511.18169v1#S5.E22 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")).

From ([5.22](https://arxiv.org/html/2511.18169v1#S5.E22 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) and ([5.21](https://arxiv.org/html/2511.18169v1#S5.E21 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we get ℙ​{ξε2∈𝕍uε}≥1−ε\mathbb{P}\{\xi^{\varepsilon^{2}}\in\mathbb{V}\_{u}^{\varepsilon}\}\geq 1-\varepsilon. By combining this with ([5.20](https://arxiv.org/html/2511.18169v1#S5.E20 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) and taking y¯=yε2\bar{y}=y^{\varepsilon^{2}}, we see that y¯∈𝕍~0,uε​(0)\bar{y}\in\tilde{\mathbb{V}}\_{0,u}^{\varepsilon}(0) and |y−y¯|≤ε|y-\bar{y}|\leq\varepsilon; hence, y∈𝕍~0,uε​(0)+𝔹ℝd​(ε)y\in\tilde{\mathbb{V}}^{\varepsilon}\_{0,u}(0)+\mathbb{B}\_{\mathbb{R}^{d}}(\varepsilon), completing the proof of the inclusion ⊆\subseteq in ([5.17](https://arxiv.org/html/2511.18169v1#S5.E17 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")).

To prove the inclusion ⊇\supseteq in ([5.17](https://arxiv.org/html/2511.18169v1#S5.E17 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we follow a similar line of thought as in the proof of Theorem [5.5](https://arxiv.org/html/2511.18169v1#S5.Thmthm5 "Theorem 5.5. ‣ 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time") using partitioning ideas and SDE estimates. To that end, let y∈ℝdy\in\mathbb{R}^{d} be such that y∈𝕍~0,uδ​(0)+𝔹ℝd​(δ)y\in\tilde{\mathbb{V}}^{\delta}\_{0,u}(0)+\mathbb{B}\_{\mathbb{R}^{d}}(\delta) for every δ∈(0,1]\delta\in(0,1]. Let us fix ε∈(0,1]\varepsilon\in(0,1]. Thanks to ([5.3](https://arxiv.org/html/2511.18169v1#S5.E3 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we aim to show that y∈𝕍~0ε​(0)+𝔹ℝd​(ε)y\in\tilde{\mathbb{V}}^{\varepsilon}\_{0}(0)+\mathbb{B}\_{\mathbb{R}^{d}}(\varepsilon).

By the choice of yy, taking δ=ε4\delta=\frac{\varepsilon}{4} yields the existence of y~∈𝕍~0,uε4​(0)\tilde{y}\in\tilde{\mathbb{V}}\_{0,u}^{\frac{\varepsilon}{4}}(0) such that |y−y~|≤ε4|y-\tilde{y}|\leq\frac{\varepsilon}{4}. Since y~∈𝕍~0,uε4​(0)\tilde{y}\in\tilde{\mathbb{V}}^{\frac{\varepsilon}{4}}\_{0,u}(0), there exist k^∈𝔻^𝔽2​(ℝd)\hat{k}\in\hat{\mathbb{D}}^{2}\_{\mathbb{F}}(\mathbb{R}^{d}), ξ∈𝕃ℱu2​(ℝd)\xi\in\mathbb{L}^{2}\_{{\cal F}\_{u}}(\mathbb{R}^{d}) such that ℙ​{ξ∈𝕍uε4}≥1−ε4\mathbb{P}\{\xi\in\mathbb{V}\_{u}^{\frac{\varepsilon}{4}}\}\geq 1-\frac{\varepsilon}{4} and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ{k^r∈K^rε4∀r∈[0,u],y~−∫0uk^rdr+Lε4𝟏≥ξ}≥1−ε4.\displaystyle\mathbb{P}\left\{\hat{k}\_{r}\in\hat{K}\_{r}^{\frac{\varepsilon}{4}}\ \forall r\in[0,u],\ \tilde{y}-\int\_{0}^{u}\hat{k}\_{r}dr+L\frac{\varepsilon}{4}{\bf 1}\geq\xi\right\}\geq 1-\frac{\varepsilon}{4}. |  | (5.23) |

As justified above, without loss of generality, we assume that ξu,ω=ξ​(ω)\xi^{u,\omega}=\xi(\omega) a.s. for every ω∈Ω\omega\in\Omega.

Let us fix a Borel-measurable partition (Oj)j∈ℕ(O\_{j})\_{j\in\mathbb{N}} of ℝd\mathbb{R}^{d} and a Borel-measurable partition (Cℓ)ℓ∈ℕ(C\_{\ell})\_{\ell\in\mathbb{N}} of ℂs0​([0,T],ℝd)\mathbb{C}\_{s\_{0}}([0,T],\mathbb{R}^{d}) such that, for every j,ℓ∈ℕj,\ell\in\mathbb{N},

|  |  |  |
| --- | --- | --- |
|  | supy′,y′′∈Oj|y′−y′′|≤ε8,supf1,f2∈Cℓ‖f1−f2‖∞≤ε​ε16​c,\sup\_{y^{\prime},y^{\prime\prime}\in O\_{j}}|y^{\prime}-y^{\prime\prime}|\leq\frac{\varepsilon}{8},\quad\sup\_{f^{1},f^{2}\in C\_{\ell}}\|f^{1}-f^{2}\|\_{\infty}\leq\frac{\varepsilon\sqrt{\varepsilon}}{16\sqrt{c}}, |  |

where c≥1c\geq 1 is a constant to be defined later.

Let B:={ξ∈𝕍uε4}∈ℱuB:=\{\xi\in\mathbb{V}\_{u}^{\frac{\varepsilon}{4}}\}\in{\cal F}\_{u}. For each (j,ℓ)∈ℕ2(j,\ell)\in\mathbb{N}^{2}, let us define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bj,ℓ:=B∩{ξ∈Oj}∩{Su∧⁣⋅∈Cℓ}.\displaystyle B\_{j,\ell}:=B\cap\{\xi\in O\_{j}\}\cap\{S\_{u\wedge\cdot}\in C\_{\ell}\}. |  | (5.24) |

Then, (Bj,ℓ)(j,ℓ)∈ℕ2(B\_{j,\ell})\_{(j,\ell)\in\mathbb{N}^{2}} is an ℱu{\cal F}\_{u}-measurable partition of BB.

Let us fix (j,ℓ)∈ℕ2(j,\ell)\in\mathbb{N}^{2} and a representative outcome ωj,ℓ∈Bj,ℓ\omega^{j,\ell}\in B\_{j,\ell}. Since ξ​(ωj,ℓ)∈𝕍uε4​(ωj,ℓ)\xi(\omega^{j,\ell})\in\mathbb{V}\_{u}^{\frac{\varepsilon}{4}}(\omega^{j,\ell}), there exists yj,ℓ∈𝕍~uε4​(ωj,ℓ)y^{j,\ell}\in\tilde{\mathbb{V}}\_{u}^{\frac{\varepsilon}{4}}(\omega^{j,\ell}) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |yj,ℓ−ξ​(ωj,ℓ)|≤ε4.\displaystyle|y^{j,\ell}-\xi(\omega^{j,\ell})|\leq\frac{\varepsilon}{4}. |  | (5.25) |

Moreover, since yj,ℓ∈𝕍~uε4​(ωj,ℓ)y^{j,\ell}\in\tilde{\mathbb{V}}\_{u}^{\frac{\varepsilon}{4}}(\omega^{j,\ell}), there exists k^j,ℓ∈𝔻^𝔽u2​(ℝd)\hat{k}^{j,\ell}\in\hat{\mathbb{D}}^{2}\_{\mathbb{F}^{u}}(\mathbb{R}^{d}) such that ℙ​(Fj,ℓ)≥1−ε4\mathbb{P}(F\_{j,\ell})\geq 1-\frac{\varepsilon}{4}, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fj,ℓ:={k^rj,ℓ∈K^rε4;u,ωj,ℓ∀r∈[u,T],yj,ℓ−∫uTk^rj,ℓdr+Lε4𝟏≥Xu,ωj,ℓ}.\displaystyle F\_{j,\ell}:=\left\{\hat{k}^{j,\ell}\_{r}\in\hat{K}^{\frac{\varepsilon}{4};u,\omega^{j,\ell}}\_{r}\ \forall r\in[u,T],\ y^{j,\ell}-\int\_{u}^{T}\hat{k}^{j,\ell}\_{r}dr+L\frac{\varepsilon}{4}{\bf 1}\geq X^{u,\omega^{j,\ell}}\right\}. |  | (5.26) |

Let us also fix a representative outcome ω0∈Bc\omega^{0}\in B^{c}. Let

|  |  |  |
| --- | --- | --- |
|  | S¯u:=∑(j,ℓ)∈ℕ2Su​(ωj,ℓ)​𝟏Bj,ℓ+Su​(ω0)​𝟏Bc.\bar{S}\_{u}:=\sum\_{(j,\ell)\in\mathbb{N}^{2}}S\_{u}(\omega^{j,\ell}){\bf 1}\_{B\_{j,\ell}}+S\_{u}(\omega^{0}){\bf 1}\_{B^{c}}. |  |

Then, by standard SDE estimates, there exists a constant c≥1c\geq 1 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[supr∈[u,T]|Sr−SrS¯u;u|2∣ℱu]=𝔼​[supr∈[u,T]|SrSu;u−SrS¯u;u|2∣ℱu]≤c​|Su−S¯u|2​ℙ​-a.s.\displaystyle\mathbb{E}\left[\sup\_{r\in[u,T]}\negthinspace|S\_{r}-S\_{r}^{\bar{S}\_{u};u}|^{2}\negthinspace\mid\negthinspace{\cal F}\_{u}\negthinspace\right]\negthinspace=\negthinspace\mathbb{E}\left[\sup\_{r\in[u,T]}\negthinspace|S\_{r}^{S\_{u};u}-S\_{r}^{\bar{S}\_{u};u}|^{2}\negthinspace\mid\negthinspace{\cal F}\_{u}\negthinspace\right]\negthinspace\leq\negthinspace c|S\_{u}-\bar{S}\_{u}|^{2}\;\mathbb{P}\text{-a.s.}\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace\negthinspace |  | (5.27) |

Let ω∈Bj,ℓ\omega\in B\_{j,\ell}. Repeating the arguments in the proof of Theorem [5.5](https://arxiv.org/html/2511.18169v1#S5.Thmthm5 "Theorem 5.5. ‣ 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time") together with ([5.24](https://arxiv.org/html/2511.18169v1#S5.E24 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), ([5.27](https://arxiv.org/html/2511.18169v1#S5.E27 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), and Markov inequality, we obtain ℙ​(Eu,ω)≥1−ε4\mathbb{P}(E^{u,\omega})\geq 1-\frac{\varepsilon}{4} for ℙ\mathbb{P}-a.e. ω∈Bj,ℓ\omega\in B\_{j,\ell}, where

|  |  |  |
| --- | --- | --- |
|  | Eu,ω:={supr∈[u,T]|Sru,ω−Sru,ωj,ℓ|≤ε8}.E^{u,\omega}:=\left\{\sup\_{r\in[u,T]}|S\_{r}^{u,\omega}-S\_{r}^{u,\omega^{j,\ell}}|\leq\frac{\varepsilon}{8}\right\}. |  |

Let ω∈Bj,ℓ\omega\in B\_{j,\ell} be such that ℙ​(Eu,ω)≥1−ε4\mathbb{P}(E^{u,\omega})\geq 1-\frac{\varepsilon}{4}. Similar to ([5.13](https://arxiv.org/html/2511.18169v1#S5.E13 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) in the proof of Theorem [5.5](https://arxiv.org/html/2511.18169v1#S5.Thmthm5 "Theorem 5.5. ‣ 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), for every ω~∈Eu,ω\tilde{\omega}\in E^{u,\omega}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Xt,ω​(ω~)−Xt,ωj,ℓ​(ω~)|≤L​ε8.\displaystyle|X^{t,\omega}(\tilde{\omega})-X^{t,\omega^{j,\ell}}(\tilde{\omega})|\leq L\frac{\varepsilon}{8}. |  | (5.28) |

Now, let us suppose further that ω~∈Eu,ω∩Fj,ℓ\tilde{\omega}\in E^{u,\omega}\cap F\_{j,\ell} and ξu,ω​(ω~)=ξ​(ω)\xi^{u,\omega}(\tilde{\omega})=\xi(\omega). Then, using ([5.28](https://arxiv.org/html/2511.18169v1#S5.E28 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) in ([5.26](https://arxiv.org/html/2511.18169v1#S5.E26 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we obtain

|  |  |  |
| --- | --- | --- |
|  | yj,ℓ−∫uTk^rj,ℓ​(ω~)​𝑑r+L​ε4​𝟏≥Xu,ωj,ℓ​(ω~)≥Xu,ω​(ω~)−L​ε8​𝟏,y^{j,\ell}-\int\_{u}^{T}\hat{k}\_{r}^{j,\ell}(\tilde{\omega})dr+L\frac{\varepsilon}{4}{\bf 1}\geq X^{u,\omega^{j,\ell}}(\tilde{\omega})\geq X^{u,\omega}(\tilde{\omega})-L\frac{\varepsilon}{8}{\bf 1}, |  |

which implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | yj,ℓ−∫uTk^rj,ℓ​(ω~)​𝑑r+L​3​ε8​𝟏≥Xu,ω​(ω~).\displaystyle y^{j,\ell}-\int\_{u}^{T}\hat{k}\_{r}^{j,\ell}(\tilde{\omega})dr+L\frac{3\varepsilon}{8}{\bf 1}\geq X^{u,\omega}(\tilde{\omega}). |  | (5.29) |

By ([5.24](https://arxiv.org/html/2511.18169v1#S5.E24 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) and ([5.25](https://arxiv.org/html/2511.18169v1#S5.E25 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we also have

|  |  |  |
| --- | --- | --- |
|  | |ξu,ω​(ω~)−yj,ℓ|=|ξ​(ω)−yj,ℓ|≤|ξ​(ω)−ξ​(ωj,ℓ)|+|ξ​(ωj,ℓ)−yj,ℓ|≤ε8+ε4=3​ε8.|\xi^{u,\omega}(\tilde{\omega})-y^{j,\ell}|=|\xi(\omega)-y^{j,\ell}|\leq|\xi(\omega)-\xi(\omega^{j,\ell})|+|\xi(\omega^{j,\ell})-y^{j,\ell}|\leq\frac{\varepsilon}{8}+\frac{\varepsilon}{4}=\frac{3\varepsilon}{8}. |  |

Combining this with ([5.29](https://arxiv.org/html/2511.18169v1#S5.E29 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) and recalling that L≥1L\geq 1 yield

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξu,ω​(ω~)−∫uTk^rj,ℓ​(ω~)​𝑑r+L​3​ε4​𝟏≥yj,ℓ−∫uTk^rj,ℓ​(ω~)​𝑑r+L​3​ε8​𝟏≥Xu,ω​(ω~).\displaystyle\xi^{u,\omega}(\tilde{\omega})-\int\_{u}^{T}\hat{k}\_{r}^{j,\ell}(\tilde{\omega})dr+L\frac{3\varepsilon}{4}{\bf 1}\geq y^{j,\ell}-\int\_{u}^{T}\hat{k}\_{r}^{j,\ell}(\tilde{\omega})dr+L\frac{3\varepsilon}{8}{\bf 1}\geq X^{u,\omega}(\tilde{\omega}).\negthinspace\negthinspace\negthinspace |  | (5.30) |

Moreover, for each r∈[u,T]r\in[u,T], by Lemma [5.1](https://arxiv.org/html/2511.18169v1#S5.Thmthm1 "Lemma 5.1. ‣ 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time"), having k^rj,ℓ​(ω~)∈𝒦^ε4​(Sru,ωj,ℓ​(ω~))\hat{k}\_{r}^{j,\ell}(\tilde{\omega})\in\hat{\mathscr{K}}^{\frac{\varepsilon}{4}}(S\_{r}^{u,\omega^{j,\ell}}(\tilde{\omega})) and |Sru,ω​(ω~)−Sru,ωj,ℓ​(ω~)|≤ε8|S\_{r}^{u,\omega}(\tilde{\omega})-S\_{r}^{u,\omega^{j,\ell}}(\tilde{\omega})|\leq\frac{\varepsilon}{8} implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | k^rj,ℓ​(ω~)∈𝒦^3​ε8​(Sru,ω​(ω~))=K^r3​ε8;u,ω​(ω~)⊆K^rε;u,ω​(ω~).\displaystyle\hat{k}\_{r}^{j,\ell}(\tilde{\omega})\in\hat{\mathscr{K}}^{\frac{3\varepsilon}{8}}(S^{u,\omega}\_{r}(\tilde{\omega}))=\hat{K}\_{r}^{\frac{3\varepsilon}{8};u,\omega}(\tilde{\omega})\subseteq\hat{K}\_{r}^{\varepsilon;u,\omega}(\tilde{\omega}). |  | (5.31) |

For each (r,ω)∈[0,T]×Ω(r,\omega)\in[0,T]\times\Omega, let us define

|  |  |  |
| --- | --- | --- |
|  | k^rε​(ω):=k^r​(ω)​𝟏B​(ω)​𝟏[0,u)​(r)+∑(j,ℓ)∈ℕ2k^rj,ℓ​(W~​(ω))​𝟏Bj,ℓ​(ω)​𝟏[u,T]​(r)+k^r0​(ω)​𝟏Bc​(ω)​𝟏[0,T]​(r),\hat{k}^{\varepsilon}\_{r}(\omega)\negthinspace:=\negthinspace\hat{k}\_{r}(\omega){\bf 1}\_{B}(\omega){\bf 1}\_{[0,u)}(r)\negthinspace+\negthinspace\sum\_{(j,\ell)\in\mathbb{N}^{2}}\hat{k}^{j,\ell}\_{r}(\tilde{W}(\omega)){\bf 1}\_{B\_{j,\ell}}(\omega){\bf 1}\_{[u,T]}(r)\negthinspace+\negthinspace\hat{k}^{0}\_{r}(\omega){\bf 1}\_{B^{c}}(\omega){\bf 1}\_{[0,T]}(r), |  |

where k^0∈𝔻^𝔽2​(ℝd)\hat{k}^{0}\in\hat{\mathbb{D}}\_{\mathbb{F}}^{2}(\mathbb{R}^{d}) is arbitrarily fixed and W~:Ω→Ω\tilde{W}\colon\Omega\to\Omega is defined by ([5.16](https://arxiv.org/html/2511.18169v1#S5.E16 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")). This definition guarantees that k^ε∈𝔻^𝔽2​(ℝd)\hat{k}^{\varepsilon}\in\hat{\mathbb{D}}^{2}\_{\mathbb{F}}(\mathbb{R}^{d}).

To check that y~∈𝕍~0ε​(0)\tilde{y}\in\tilde{\mathbb{V}}^{\varepsilon}\_{0}(0), it is enough to show that ℙ​(C)≥1−ε\mathbb{P}(C)\geq 1-\varepsilon, where

|  |  |  |
| --- | --- | --- |
|  | C:={k^rε∈K^rε∀r∈[0,T],y~−∫0Tk^rεdr+Lε𝟏≥X}.C:=\left\{\hat{k}\_{r}^{\varepsilon}\in\hat{K}^{\varepsilon}\_{r}\ \forall r\in[0,T],\ \tilde{y}-\int\_{0}^{T}\hat{k}^{\varepsilon}\_{r}dr+L\varepsilon{\bf 1}\geq X\right\}. |  |

Clearly, we have C⊇B∩C1∩C2C\supseteq B\cap C\_{1}\cap C\_{2}, where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | C1\displaystyle C\_{1} | :=\displaystyle:= | {k^rε∈K^rε​∀r∈[0,u],y~−∫0uk^rε​𝑑r+L​ε4​𝟏≥ξ},\displaystyle\left\{\hat{k}\_{r}^{\varepsilon}\in\hat{K}^{\varepsilon}\_{r}\ \forall r\in[0,u],\ \tilde{y}-\int\_{0}^{u}\hat{k}^{\varepsilon}\_{r}dr+L\frac{\varepsilon}{4}{\bf 1}\geq\xi\right\}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | C2\displaystyle C\_{2} | :=\displaystyle:= | {k^rε∈K^rε​∀r∈[u,T],ξ−∫uTk^rε​𝑑r+L​3​ε4​𝟏≥X}.\displaystyle\left\{\hat{k}\_{r}^{\varepsilon}\in\hat{K}^{\varepsilon}\_{r}\ \forall r\in[u,T],\ \xi-\int\_{u}^{T}\hat{k}^{\varepsilon}\_{r}dr+L\frac{3\varepsilon}{4}{\bf 1}\geq X\right\}. |  |

Recall that B={ξ∈𝕍uε4}B=\{\xi\in\mathbb{V}\_{u}^{\frac{\varepsilon}{4}}\}. By the definition of k^ε\hat{k}^{\varepsilon} and ([5.23](https://arxiv.org/html/2511.18169v1#S5.E23 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℙ​(B∩C1)\displaystyle\mathbb{P}(B\cap C\_{1}) | ≥\displaystyle\geq | ℙ(B∩{k^r∈K^rε4∀r∈[0,u],y~−∫0uk^rdr+Lε4𝟏≥ξ})\displaystyle\mathbb{P}\left(B\cap\left\{\hat{k}\_{r}\in\hat{K}^{\frac{\varepsilon}{4}}\_{r}\ \forall r\in[0,u],\ \tilde{y}-\int\_{0}^{u}\hat{k}\_{r}dr+L\frac{\varepsilon}{4}{\bf 1}\geq\xi\right\}\right) |  |
|  |  | ≥\displaystyle\geq | ℙ(B)+ℙ{k^r∈K^rε4∀r∈[0,u],y~−∫0uk^rdr+Lε4𝟏≥ξ}−1≥1−ε2.\displaystyle\mathbb{P}(B)+\mathbb{P}\left\{\hat{k}\_{r}\in\hat{K}^{\frac{\varepsilon}{4}}\_{r}\ \forall r\in[0,u],\ \tilde{y}-\int\_{0}^{u}\hat{k}\_{r}dr+L\frac{\varepsilon}{4}{\bf 1}\geq\xi\right\}-1\geq 1-\frac{\varepsilon}{2}. |  |

Let us fix (j,ℓ)∈ℕ2(j,\ell)\in\mathbb{N}^{2} and ω∈Bj,ℓ\omega\in B\_{j,\ell} such that ℙ​(Eu,ω)≥1−ε4\mathbb{P}(E^{u,\omega})\geq 1-\frac{\varepsilon}{4}. The definition of k^ε\hat{k}^{\varepsilon} yields that (k^ε)u,ω=k^j,ℓ(\hat{k}^{\varepsilon})^{u,\omega}=\hat{k}^{j,\ell}. Hence, by ([5.30](https://arxiv.org/html/2511.18169v1#S5.E30 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")) and ([5.31](https://arxiv.org/html/2511.18169v1#S5.E31 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℙ​(C2u,ω)\displaystyle\mathbb{P}(C\_{2}^{u,\omega}) | =\displaystyle= | ℙ{k^rj,ℓ∈K^rε;u,ω∀r∈[u,T],ξu,ω−∫uTk^rj,ℓdr+L3​ε4𝟏≥Xu,ω}\displaystyle\mathbb{P}\left\{\hat{k}\_{r}^{j,\ell}\in\hat{K}^{\varepsilon;u,\omega}\_{r}\ \forall r\in[u,T],\ \xi^{u,\omega}-\int\_{u}^{T}\hat{k}^{j,\ell}\_{r}dr+L\frac{3\varepsilon}{4}{\bf 1}\geq X^{u,\omega}\right\} |  |
|  |  | ≥\displaystyle\geq | ℙ​(Eu,ω∩Fj,ℓ)≥ℙ​(Eu,ω)+ℙ​(Fj,ℓ)−1≥1−ε2.\displaystyle\mathbb{P}(E^{u,\omega}\cap F\_{j,\ell})\geq\mathbb{P}(E^{u,\omega})+\mathbb{P}(F\_{j,\ell})-1\geq 1-\frac{\varepsilon}{2}. |  |

Since B∩C1∈ℱuB\cap C\_{1}\in{\cal F}\_{u}, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℙ​(C)\displaystyle\mathbb{P}(C) | ≥\displaystyle\geq | ℙ​(B∩C1∩C2)=𝔼​[𝟏B∩C1​ℙ​(C2|ℱu)]=∫B∩C1ℙ​(C2u,ω)​ℙ​(d​ω)\displaystyle\mathbb{P}(B\cap C\_{1}\cap C\_{2})=\mathbb{E}[{\bf 1}\_{B\cap C\_{1}}\mathbb{P}(C\_{2}|{\cal F}\_{u})]=\int\_{B\cap C\_{1}}\mathbb{P}(C\_{2}^{u,\omega})\mathbb{P}(d\omega) |  |
|  |  | ≥\displaystyle\geq | (1−ε2)​ℙ​(B∩C1)≥(1−ε2)2=1−ε+ε24≥1−ε.\displaystyle\left(1-\frac{\varepsilon}{2}\right)\mathbb{P}(B\cap C\_{1})\geq\left(1-\frac{\varepsilon}{2}\right)^{2}=1-\varepsilon+\frac{\varepsilon^{2}}{4}\geq 1-\varepsilon. |  |

Therefore, y~∈𝕍~0ε​(0)\tilde{y}\in\tilde{\mathbb{V}}^{\varepsilon}\_{0}(0). Since we also have |y−y~|≤ε4≤ε|y-\tilde{y}|\leq\frac{\varepsilon}{4}\leq\varepsilon, this finishes the proof of the inclusion ⊇\supseteq in ([5.17](https://arxiv.org/html/2511.18169v1#S5.E17 "In 5 Pathwise Formulation of the Superhedging Problem ‣ Superhedging under Proportional Transaction Costs in Continuous Time")).