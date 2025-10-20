---
authors:
- Tiziano De Angelis
- Jan Palczewski
- Jacob Smith
doc_id: arxiv:2510.15616v1
family_id: arxiv:2510.15616
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Martingale theory for Dynkin games with asymmetric information
url_abs: http://arxiv.org/abs/2510.15616v1
url_html: https://arxiv.org/html/2510.15616v1
venue: arXiv q-fin
version: 1
year: 2025
---


Tiziano De Angelis
, 
Jan Palczewski
 and 
Jacob Smith
T. De Angelis: School of Management and Economics, Dept. ESOMAS, University of Torino, Corso Unione Sovietica, 218 Bis, 10134, Torino, Italy; Collegio Carlo Alberto, Piazza Arbarello 8, 10122, Torino, Italy.
[[tiziano.deangelis@unito.it](mailto:tiziano.deangelis@unito.it)](mailto:)
J. Palczewski: Faculty of Mathematics, Wrocław University of Science and Technology, Wybrzeże Wyspiańskiego 27,
50-370, Wrocław, Poland.
[[jan.palczewski@pwr.edu.pl](mailto:jan.palczewski@pwr.edu.pl)](mailto:)
J. Smith: School of Mathematics, University of Leeds, Woodhouse Lane, LS2 9JT Leeds, UK.
[[mm15js@leeds.ac.uk](mailto:mm15js@leeds.ac.uk)](mailto:)

(Date: October 17, 2025)

###### Abstract.

This paper provides necessary and sufficient conditions for a pair of randomised stopping times to form a saddle point of a zero-sum Dynkin game with partial and/or asymmetric information across players. The framework is non-Markovian and covers essentially any information structure. Our methodology relies on the identification of suitable super and submartingales involving players’ equilibrium payoffs. Saddle point strategies are characterised in terms of the dynamics of those equilibrium payoffs and are related to their Doob-Meyer decompositions.

###### Key words and phrases:

Dynkin games; zero-sum games; partial information; asymmetric information; Nash equilibrium; martingale theory

###### 2020 Mathematics Subject Classification:

91A27, 91A55, 91A15, 60G07, 60G40

Acknowledgements: T. De Angelis was partially supported by EU – Next Generation EU – PRIN2022 (2022BEMMLZ) CUP: D53D23005780006 and PRIN-PNRR2022 (P20224TM7Z) CUP: D53D23018780001.

## 1. Introduction

Zero-sum optimal stopping games (Dynkin games) in which players have access to different filtrations are an emerging field of continuous-time stochastic game theory. Recent results by [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12)] have shown that such games admit a saddle point in randomised stopping times in a general non-Markovian setting. Players’ filtrations are arbitrary and only need to satisfy the usual conditions. The underlying payoff processes are bounded in expectation, càdlàg, measurable but not necessarily adapted to either of the players’ filtrations.

The results in [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12)] concern the existence of saddle points but do not offer a dynamic picture which is necessary for characterisation and construction of players’ optimal strategies. The present paper addresses this shortcoming by offering three main contributions: (i) *necessary* and *sufficient* conditions for a pair of randomised stopping times to form a saddle point (equilibrium) of the game, (ii) a dynamic characterisation of the game, including super/submartingale conditions for players’ equilibrium value processes111In line with game-theoretic terminology for repeated games, these are also referred to as continuation value processes, because they represent the optimal value that a player can obtain by continuing to play the game from a given instant of time. and a representation of optimal strategies, (iii) an application of the abstract theory to two classes of games with asymmetric information. From the methodological perspective we break with the classical approach to zero-sum games which is based on the study of the game’s value. The generality of the information structure leads us naturally to consider zero-sum games through the lens of nonzero-sum games in which each player’s equilibrium value process has dynamics adapted to the player’s own filtration. The zero-sum feature of the game is recovered thanks to an equivalence in expectation between the two players’ payoffs, which yields a quantity that can be thought of as the ex-ante value of the game (i.e., the game’s value before players have access to the pieces of information that create asymmetry in the game).

To obtain necessary and sufficient conditions for a saddle point, we build on the general theory of stochastic processes in the spirit of El Karoui’s seminal work [[EK81](https://arxiv.org/html/2510.15616v1#bib.bibx20)] which was brought in touch with Dynkin games by Lepeltier and Maingueneau [[LM84](https://arxiv.org/html/2510.15616v1#bib.bibx34)] in a full information setup. Unlike those contributions, games with asymmetric information cannot be characterised by a value process common to both players. Consequenty, their stopping strategies cannot be written purely in terms of the coincidence of the value process with the respective payoff process. Instead, starting from general families of random variables and proceeding with aggregation results, we develop a martingale theory for the players’ equilibrium value processes and optimal randomised strategies.

We show that equilibrium value processes can be described by optional semi-martingales (with respect to each player’s own filtration) which evolve above/below suitable optional projections of players’ stopping payoffs (depending on whether a player is a maximiser or a minimiser). Differently from the full information game, the aggregation step and the super/submartingale properties require a dynamic representation of the game involving non-decreasing processes that “generate” the players’ optimal randomised stopping times; these generating processes are conditional cumulative distribution functions of the players’
randomised stopping times; due to the asymmetry of information, each player must project their opponent’s stopping rule (e.g., optimal generating process) onto the observed filtration. We also obtain exact formulae for jumps in the dynamics of the equilibrium value processes and determine the support of the generating processes for the equilibrium pair of randomised stopping times. Finally, we deduce a relationship between the Doob-Meyer decompositions of the equilibrium value processes and the generating processes of the corresponding equilibrium stopping times. That relationship can be used to construct optimal randomised stopping times in concrete applications of the theory.

Our paper provides theoretical foundations for the study of stopping games with asymmetric information in general non-Markovian setups, where the information structure is essentially arbitrary. We believe this to be the first comprehensive treatment of such games in their generality. The literature on Dynkin games with asymmetric information is patchy and problems have been solved on a case-by-case basis with ad-hoc methods (cf. next section for details). In this work we focus on the dynamic aspects of the game and devise a methodology that allows a more systematic approach to the construction of saddle points in randomised strategies. We remark that randomised strategies are indeed necessary for the construction of saddle points, because simple counterexamples with no saddle point in pure strategies are provided in, e.g., [[Grü13](https://arxiv.org/html/2510.15616v1#bib.bibx24)] and [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12), Sec. 6].

Beyond the abstract theory, we demonstrate the scope of our study by specialising to two natural classes of games with asymmetric information and showing that our methods lead to computable expressions. In the first class of games, motivated by the seminal paper [[Grü13](https://arxiv.org/html/2510.15616v1#bib.bibx24)], there are finitely many payoff regimes. One player is fully informed and learns the realisation of the regime at the beginning of the game. The other player is only aware of its probability distribution. A fully worked out example of a game from this class is available in [[Smi24](https://arxiv.org/html/2510.15616v1#bib.bibx41), Ch. 6]. In the second class of games, the asymmetry of information is analogous albeit the regime affects only the drift of the underlying observable diffusion which determines the payoff; this generalises a specific problem solved in [[DAEG22](https://arxiv.org/html/2510.15616v1#bib.bibx9)]. The difference between the first and the second class of games lies in the available learning opportunities for the less-informed player. In the first class, this player can only infer information about the regime from the lack of actions of the other player. In the second class, an additional source of information comes in the form of the observations of the underlying diffusion, which can be utilised through the application of the stochastic filtering theory.

### 1.1. Related literature

The study of zero-sum Dynkin games, formulated by Dynkin [[Dyn69](https://arxiv.org/html/2510.15616v1#bib.bibx18)], dates back to the 1970s in the classical set-up where players have full and symmetric information. Although in this introduction we focus on the continuous-time version of the problem, we acknowledge the existence of a vast body of work in the discrete-time setting, see, e.g., [[Dom02](https://arxiv.org/html/2510.15616v1#bib.bibx17)], [[Kif71](https://arxiv.org/html/2510.15616v1#bib.bibx29)], [[Nev75](https://arxiv.org/html/2510.15616v1#bib.bibx36), Ch. VI], [[RSV01](https://arxiv.org/html/2510.15616v1#bib.bibx38)], [[Yas85](https://arxiv.org/html/2510.15616v1#bib.bibx45)].

The theory of zero-sum Dynkin games has been developed over the past five decades with methods ranging from PDEs to BSDEs and the theory of Markov processes. Early contributions were due to Bensoussan and Friedman [[BF74](https://arxiv.org/html/2510.15616v1#bib.bibx2)], Bismut [[Bis77](https://arxiv.org/html/2510.15616v1#bib.bibx5)] and Stettner [[Ste82](https://arxiv.org/html/2510.15616v1#bib.bibx42)], among others. A milestone in the general (non-Markovian) theory was the work of Lepeltier and Maingueneau [[LM84](https://arxiv.org/html/2510.15616v1#bib.bibx34)], who used tools from the theory of stochastic processes to prove the existence and obtain a characterisation of the game’s value and of the equilibrium stopping times.

Following this, the research on Dynkin games slowed for nearly two decades before being revived in the early 2000s. Hamadène and Lepeltier [[HL00](https://arxiv.org/html/2510.15616v1#bib.bibx26)] applied BSDE methods to solve mixed control-stopping games, while Kifer [[Kif00](https://arxiv.org/html/2510.15616v1#bib.bibx30)] introduced an application of Dynkin games in mathematical finance. Relaxation of classical conditions on the payoffs sparked a new wave of general results on the existence of a value in randomised stopping times in a non-Markovian setting, see, e.g., Touzi and Vieille [[TV02](https://arxiv.org/html/2510.15616v1#bib.bibx43)] and Laraki and Solan [[LS05](https://arxiv.org/html/2510.15616v1#bib.bibx35)]. In parallel, Ekström and Peskir developed the theory for general Markovian games in [[EP08](https://arxiv.org/html/2510.15616v1#bib.bibx21)], while Ekström and Villeneuve [[EV06](https://arxiv.org/html/2510.15616v1#bib.bibx22)] solved the problem for one-dimensional diffusions under relaxed integrability conditions. More recently, there has been a new drive towards the development of a general theory for Markovian equilibria in randomised stopping times for Dynkin games with full information. The field is growing rapidly with the most recent contributions by Décamps, Gensbittel and Mariotti [[DGM24](https://arxiv.org/html/2510.15616v1#bib.bibx14)], [[DGM22](https://arxiv.org/html/2510.15616v1#bib.bibx13)], Christensen and Lindensj̈o [[CL24](https://arxiv.org/html/2510.15616v1#bib.bibx6)], and Christensen and Schultz [[CS24](https://arxiv.org/html/2510.15616v1#bib.bibx8)].

While the full-information case has been extensively studied,
the literature on partial and asymmetric information games is more recent and less developed. We now review the main contributions in this direction. The first work was due to Grün [[Grü13](https://arxiv.org/html/2510.15616v1#bib.bibx24)] who formulated a class of Markovian zero-sum Dynkin games with asymmetric information and diffusive underlying dynamics. The asymmetry arises from a discrete, finite-valued random variable that enters into the payoff functions along with the underlying diffusion. The player who observes this variable at the outset of the game is strictly more informed about the payoff processes than the opponent who only learns it when the game ends. Grün studied the game with methods based on viscosity solutions of variational inequalities, inspired by the work of Cardaliaguet and Rainer [[CR09](https://arxiv.org/html/2510.15616v1#bib.bibx7)] on stochastic differential games with asymmetric information. In [[Grü13](https://arxiv.org/html/2510.15616v1#bib.bibx24)], the author showed the existence of the game’s value and of an optimal strategy for the more informed player. Numerical methods for the solution of the associated variational problem were studied many years later by Baňas et al. [[BFR25](https://arxiv.org/html/2510.15616v1#bib.bibx3)]. Using similar methods as [[Grü13](https://arxiv.org/html/2510.15616v1#bib.bibx24)], Gensbittel and Grün [[GG19](https://arxiv.org/html/2510.15616v1#bib.bibx23)] proved the existence of a saddle point in a game where each player observes only their private finite-state continuous-time Markov chain, while the payoff is a function of both Markov chains.

In both [[Grü13](https://arxiv.org/html/2510.15616v1#bib.bibx24)] and [[GG19](https://arxiv.org/html/2510.15616v1#bib.bibx23)], a player’s learning is restricted to inference from the opponent’s actions (or inaction). A different model is considered by De Angelis, Ekström, and Glover [[DAEG22](https://arxiv.org/html/2510.15616v1#bib.bibx9)], who analysed a bi-valued regime influencing the drift of the diffusion observed by both players. The realisation of the regime is revealed to the informed player at the outset. The uninformed player must infer it from the diffusion path and, as in previously discussed papers, from the opponent’s behaviour. The authors constructed a saddle point based on an educated guess followed by a verification theorem. Their approach is difficult to generalise. The variational problem obtained in [[DAEG22](https://arxiv.org/html/2510.15616v1#bib.bibx9)] is conceptually distinct from those in [[Grü13](https://arxiv.org/html/2510.15616v1#bib.bibx24), [GG19](https://arxiv.org/html/2510.15616v1#bib.bibx23)] and closer in spirit to the theory that we develop here.

As we already mentioned in the previous section, the recent paper [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12)] provided minimal sufficient conditions for the existence of a value and a saddle point in non-Markovian Dynkin games with partial and asymmetric information. The present paper continues that line of research by characterising the dynamics of equilibrium value processes and optimal strategies through necessary and sufficient conditions.

Our focus here is exclusively on asymmetric-information games. We therefore do not review the literature on games with partial but *symmetric* information (see, e.g., [[DAGV21](https://arxiv.org/html/2510.15616v1#bib.bibx10)]), where players are equally uninformed. Such models can typically be reformulated within the frameworks of [[LM84](https://arxiv.org/html/2510.15616v1#bib.bibx34)] or [[EP08](https://arxiv.org/html/2510.15616v1#bib.bibx21)] by means of Bayesian filtering.

Finally, we mention related but distinct works on nonzero-sum partial-information games. For instance, a recent work by Kwon and Palczewski [[KP24](https://arxiv.org/html/2510.15616v1#bib.bibx31)] considered a nonzero-sum stopping game modelling the exit problem from a duopoly, where both players’ random exit values are private and unobservable by the opponent. The problem falls outside our zero-sum framework, but its structure shares similarities with the games that we analyse here. Although a Nash equilibrium is found in pure stopping times, mathematical tools used to represent the opponent’s behaviour (due to the private information) are akin to randomised strategies. In this context, both players are equally uninformed and they learn solely from the actions of their opponents.

### 1.2. Structure of the paper

The problem is formulated in Section [2](https://arxiv.org/html/2510.15616v1#S2 "2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information"). Sections [3](https://arxiv.org/html/2510.15616v1#S3 "3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and [4](https://arxiv.org/html/2510.15616v1#S4 "4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") contain necessary and sufficient conditions for a saddle point, respectively. In particular, Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") aggregates the players’ equilibrium value processes into optional semi-martingales and it quantifies the size of their jumps. Proposition [3.10](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem10 "Proposition 3.10. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") establishes the connection between the two players’ equilibrium value processes via an averaging procedure that can be interpreted as evaluating the game’s ex-ante value (cf. also Corollary [3.13](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem13 "Corollary 3.13. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")). Proposition [3.17](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem17 "Proposition 3.17. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and Corollary [3.19](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem19 "Corollary 3.19. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") establish further properties that characterise the equilibrium strategies and equilibrium value processes. Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") is the main result of Section [4](https://arxiv.org/html/2510.15616v1#S4 "4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). It provides sufficient conditions for a saddle point in terms of a suitable quadruple of stochastic processes. That result is refined and reinterpreted in various ways in the subsequent statements of the section in order to provide a transparent formulation of all the key ingredients. In Section [5](https://arxiv.org/html/2510.15616v1#S5 "5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") we apply our results to two particularly representative classes of problems. In Section [5.1](https://arxiv.org/html/2510.15616v1#S5.SS1 "5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") we generalise Grün’s original problem from [[Grü13](https://arxiv.org/html/2510.15616v1#bib.bibx24)] to a non-Markovian setting. In Section [5.2](https://arxiv.org/html/2510.15616v1#S5.SS2 "5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") we apply our methods to the class of games with partially observed dynamics motivated by [[DAEG22](https://arxiv.org/html/2510.15616v1#bib.bibx9)]. Finally, Section [5.3](https://arxiv.org/html/2510.15616v1#S5.SS3 "5.3. A heuristic derivation of PDE systems ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") provides an informal, yet detailed connection between our martingale methods and PDE characterisation of equilibrium value functions. This provides a theoretical justification for the variational problem used by [[DAEG22](https://arxiv.org/html/2510.15616v1#bib.bibx9)] in their guess-and-verify approach and a comparison with Grün’s variational approach in [[Grü13](https://arxiv.org/html/2510.15616v1#bib.bibx24)]. The paper concludes with several technical results collected in Appendices.

## 2. Setting and preliminaries

In this section we formally introduce the problem in a framework very similar to the one in [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12)].
Let T∈(0,∞)T\in(0,\infty). All definitions that follow remain valid in the case T=∞T=\infty with a one-point compactification of [0,∞)[0,\infty); then [0,∞][0,\infty] is mapped homeomorfically into [0,1][0,1] and the game is considered on the latter, see also [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12)].222When T=∞T=\infty, the space 𝒮\mathcal{S} in [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12), Section 5] should have been defined with a weighted Lebesgue measure such that the measure of [0,∞][0,\infty] is finite; all remaining arguments in the paper remain valid. Alternatively, one can map homemorfically [0,∞][0,\infty] into [0,1][0,1] and note that all assumptions remain valid. It is the latter approach that we follow in this paper. Let (Ω,ℱ,𝖯)(\Omega,\mathcal{F},\mathsf{P}) be a complete probability space, equipped with a right-continuous filtration 𝔽:=(ℱt)t∈[0,T]\mathbb{F}:=(\mathcal{F}\_{t})\_{t\in[0,T]} completed with all 𝖯\mathsf{P}-null sets. We emphasise that ℱT⊊ℱ\mathcal{F}\_{T}\subsetneq\mathcal{F} because we need ℱ\mathcal{F} to be sufficiently rich to accommodate so-called randomisation devices, according to Definition [2.2](https://arxiv.org/html/2510.15616v1#S2.Thmtheorem2 "Definition 2.2. ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information"). In the paper, all equations and inequalities between random variables are meant 𝖯\mathsf{P}-a.s. unless stated otherwise. Let ℒb​(𝖯)\mathcal{L}\_{b}(\mathsf{P}) be the Banach space of càdlàg ℬ​([0,T])×ℱ\mathcal{B}([0,T])\times\mathcal{F}-measurable processes X=(Xt)t∈[0,T]X=(X\_{t})\_{t\in[0,T]} with finite norm

|  |  |  |
| --- | --- | --- |
|  | ‖X‖ℒb​(𝖯):=𝖤​[sup0≤t≤T|Xt|]<∞.\|X\|\_{\mathcal{L}\_{b}(\mathsf{P})}:=\mathsf{E}\Big[\sup\_{0\leq t\leq T}|X\_{t}|\Big]<\infty. |  |

There are two players in the game and they have access to the information contained in two different filtrations. In particular, we consider right-continuous filtrations 𝔽1:=(ℱt1)t∈[0,T]\mathbb{F}^{1}:=(\mathcal{F}^{1}\_{t})\_{t\in[0,T]} and 𝔽2:=(ℱt2)t∈[0,T]\mathbb{F}^{2}:=(\mathcal{F}^{2}\_{t})\_{t\in[0,T]}, which are both contained in 𝔽\mathbb{F} (i.e., ℱt1∨ℱt2⊆ℱt\mathcal{F}^{1}\_{t}\vee\mathcal{F}^{2}\_{t}\subseteq\mathcal{F}\_{t} for all t∈[0,T]t\in[0,T]) and completed with 𝖯\mathsf{P}-null sets. We assume that the first player (Player 1) has access to 𝔽1\mathbb{F}^{1} and the second player (Player 2) has access to 𝔽2\mathbb{F}^{2}. Player 1 chooses a random time τ\tau and Player 2 chooses a random time σ\sigma. At time τ∧σ\tau\wedge\sigma Player 1 delivers a payoff 𝒫​(τ,σ)\mathcal{P}(\tau,\sigma) to Player 2. Therefore, Player 1 (the τ\tau-player) is a minimiser while Player 2 (the σ\sigma-player) is a maximiser.
The payoff exchanged between players is of the following form

|  |  |  |
| --- | --- | --- |
|  | 𝒫​(τ,σ)≔fτ​𝟏{τ<σ}+hτ​𝟏{τ=σ}+gσ​𝟏{σ<τ},\mathcal{P}(\tau,\sigma)\coloneqq f\_{\tau}\mathbf{1}\_{\{\tau<\sigma\}}+h\_{\tau}\mathbf{1}\_{\{\tau=\sigma\}}+g\_{\sigma}\mathbf{1}\_{\{\sigma<\tau\}}, |  |

where ff, gg, hh are stochastic processes satisfying assumptions specified below.

###### Assumption 2.1.

The payoff processes in the game are f,g,h∈ℒb​(𝖯)f,g,h\in\mathcal{L}\_{b}(\mathsf{P}) adapted to the filtration 𝔽\mathbb{F} and such that ft≥ht≥gtf\_{t}\geq h\_{t}\geq g\_{t} for all t∈[0,T]t\in[0,T], 𝖯\mathsf{P}-a.s.

We notice that, in general, the payoff processes are not adapted to the players’ filtrations and therefore they are not fully observable by either player. Players choose random times σ\sigma and τ\tau from the class of randomised stopping times with respect to their observed filtrations. In particular, we will say that Player 1 chooses τ\tau as an 𝔽1\mathbb{F}^{1}-randomised stopping time and Player 2 chooses σ\sigma as an 𝔽2\mathbb{F}^{2}-randomised stopping time, according to the next definition (that generalises slightly the one used in [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12)]). From now on, and unless otherwise specified, we denote 𝔾:=(𝒢t)t∈[0,T]⊆𝔽\mathbb{G}:=(\mathcal{G}\_{t})\_{t\in[0,T]}\subseteq\mathbb{F} a generic right-continuous filtration, completed with 𝖯\mathsf{P}-null sets, which we use for the statement of some general definitions and results.

###### Definition 2.2.

Given a 𝔾\mathbb{G}-stopping time θ\theta, we introduce a class of processes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜θ∘(𝔾):={ρ:\displaystyle\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{G}):=\{\rho: | ρ\rho is 𝔾\mathbb{G}-adapted with t↦ρt​(ω)t\mapsto\rho\_{t}(\omega) càdlàg and non-decreasing, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ρθ−​(ω)=0 and ρT​(ω)=1 for all ω∈Ω}.\displaystyle\text{$\rho\_{\theta-}(\omega)=0$ and $\rho\_{T}(\omega)=1$ for all $\omega\in\Omega$}\}. |  |

We say that η\eta is a 𝔾\mathbb{G}-randomised stopping time after time θ\theta, with generating process ρ\rho and randomisation device ZZ, if

|  |  |  |
| --- | --- | --- |
|  | η=inf{t∈[0,T]:ρt>Z},\eta=\inf\{t\in[0,T]:\rho\_{t}>Z\}, |  |

where ρ∈𝒜θ∘​(𝔾)\rho\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{G}) and Z∼U​([0,1])Z\sim U([0,1]) is a random variable independent of ℱT\mathcal{F}\_{T}.

Clearly 𝖯​(θ≤η≤T)=1\mathsf{P}(\theta\leq\eta\leq T)=1 and the class of such randomised stopping times is denoted by 𝒯θR​(𝔾)\mathcal{T}^{R}\_{\theta}(\mathbb{G}).
In the context of the game, the randomisation device for Player 1 is independent from the randomisation device for Player 2.

For η∈𝒯θR​(𝔾)\eta\in\mathcal{T}^{R}\_{\theta}(\mathbb{G}), we will often use the notation

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | η​(ρ,z)=inf{t∈[0,T]:ρt>z},for z∈[0,1],\displaystyle\eta(\rho,z)=\inf\{t\in[0,T]:\rho\_{t}>z\},\quad\text{for $z\in[0,1]$}, |  |

and even write η​(z)\eta(z), when the underlying generating process is clear from the context.
Given a 𝔾\mathbb{G}-stopping time θ∈[0,T]\theta\in[0,T] we also use the notation

|  |  |  |
| --- | --- | --- |
|  | 𝒯θ​(𝔾):={η:η is 𝔾-stopping time with η∈[θ,T], 𝖯-a.s.},\mathcal{T}\_{\theta}(\mathbb{G}):=\big\{\eta:\text{$\eta$ is $\mathbb{G}$-stopping time with $\eta\in[\theta,T]$, $\mathsf{P}$-a.s.}\big\}, |  |

for the class of 𝔾\mathbb{G}-stopping times after time θ\theta.
It is clear that 𝒯θ​(𝔾)⊂𝒯θR​(𝔾)\mathcal{T}\_{\theta}(\mathbb{G})\subset\mathcal{T}^{R}\_{\theta}(\mathbb{G}).

Given a pair (τ,σ)∈𝒯0R​(𝔽1)×𝒯0R​(𝔽2)(\tau,\sigma)\in\mathcal{T}^{R}\_{0}(\mathbb{F}^{1})\times\mathcal{T}^{R}\_{0}(\mathbb{F}^{2}) and a σ\sigma-algebra ℋ0⊂ℱ01∩ℱ02\mathcal{H}\_{0}\subset\mathcal{F}^{1}\_{0}\cap\mathcal{F}^{2}\_{0}, representing shared information at time zero333Since ℱ0i\mathcal{F}^{i}\_{0} is not necessarily trivial, we can cover examples like ℋ0=ℱλX\mathcal{H}\_{0}=\mathcal{F}^{X}\_{\lambda}, where 𝔽X=(ℱtX)t∈[0,T]\mathbb{F}^{X}=(\mathcal{F}^{X}\_{t})\_{t\in[0,T]} is the filtration generated by a stochastic process (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} and λ\lambda is an 𝔽X\mathbb{F}^{X}-stopping time., the players evaluate the associated expected payoff of the game by

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[𝒫​(τ,σ)|ℋ0].\mathsf{E}[\mathcal{P}(\tau,\sigma)|\mathcal{H}\_{0}]. |  |

The upper and lower value of the game at time zero read

|  |  |  |  |
| --- | --- | --- | --- |
| (2.2) |  | V¯≔ess​infτ∈𝒯0R​(𝔽1)⁡ess​supσ∈𝒯0R​(𝔽2)⁡𝖤​[𝒫​(τ,σ)|ℋ0]andV¯≔ess​supσ∈𝒯0R​(𝔽2)⁡ess​infτ∈𝒯0R​(𝔽1)⁡𝖤​[𝒫​(τ,σ)|ℋ0].\displaystyle\overline{V}\coloneqq\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}^{R}\_{0}(\mathbb{F}^{1})}\operatorname\*{ess\,sup}\_{\sigma\in\mathcal{T}^{R}\_{0}(\mathbb{F}^{2})}\mathsf{E}[\mathcal{P}(\tau,\sigma)|\mathcal{H}\_{0}]\quad\text{and}\quad\underline{V}\coloneqq\operatorname\*{ess\,sup}\_{\sigma\in\mathcal{T}^{R}\_{0}(\mathbb{F}^{2})}\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}^{R}\_{0}(\mathbb{F}^{1})}\mathsf{E}[\mathcal{P}(\tau,\sigma)|\mathcal{H}\_{0}]. |  |

In [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12)] it is shown that under Assumption [2.1](https://arxiv.org/html/2510.15616v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information") and mild technical assumptions444Here we do not impose these assumptions because we are interested in a characterisation of optimal strategies rather than in their existence. However, for the reader’s convenience we recall them: ftp≤ft−{}^{p}f\_{t}\leq f\_{t-} and gtp≥gt−{}^{p}g\_{t}\geq g\_{t-} for t∈(0,T)t\in(0,T), and fTp=fT−{}^{p}f\_{T}=f\_{T-} and gTp=gT−{}^{p}g\_{T}=g\_{T-}, where (⋅)p{}^{p}(\cdot) denotes the 𝔽\mathbb{F}-previsible projection. they indeed coincide, i.e., V¯=V¯≕V\underline{V}=\overline{V}\eqqcolon V, and VV is called the value of the game at time zero. It is also shown that both players have an optimal strategy, that is, the game admits a saddle point (τ∗,σ∗)∈𝒯0R​(𝔽1)×𝒯0R​(𝔽2)(\tau\_{\*},\sigma\_{\*})\in\mathcal{T}^{R}\_{0}(\mathbb{F}^{1})\times\mathcal{T}^{R}\_{0}(\mathbb{F}^{2}) such that

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[𝒫​(τ∗,σ)|ℋ0]≤𝖤​[𝒫​(τ∗,σ∗)|ℋ0]≤𝖤​[𝒫​(τ,σ∗)|ℋ0]\mathsf{E}[\mathcal{P}(\tau\_{\*},\sigma)|\mathcal{H}\_{0}]\leq\mathsf{E}[\mathcal{P}(\tau\_{\*},\sigma\_{\*})|\mathcal{H}\_{0}]\leq\mathsf{E}[\mathcal{P}(\tau,\sigma\_{\*})|\mathcal{H}\_{0}] |  |

for all other pairs (τ,σ)∈𝒯0R​(𝔽1)×𝒯0R​(𝔽2)(\tau,\sigma)\in\mathcal{T}^{R}\_{0}(\mathbb{F}^{1})\times\mathcal{T}^{R}\_{0}(\mathbb{F}^{2}). An important first step in the derivation of those results is the following observation (cf. [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12), Prop. 4.4]): for a given pair (τ,σ)∈𝒯0R​(𝔽1)×𝒯0R​(𝔽2)(\tau,\sigma)\in\mathcal{T}^{R}\_{0}(\mathbb{F}^{1})\times\mathcal{T}^{R}\_{0}(\mathbb{F}^{2}) with generating processes (ξ,ζ)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\xi,\zeta)\in\mathcal{A}^{\circ}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\circ}\_{0}(\mathbb{F}^{2}), it holds

|  |  |  |  |
| --- | --- | --- | --- |
| (2.3) |  | 𝖤​[𝒫​(τ,σ)|ℋ0]=𝖤​[∫[0,T)ft​(1−ζt)​dξt+∫[0,T)gt​(1−ξt)​dζt+∑t∈[0,T]ht​Δ​ζt​Δ​ξt|ℋ0].\displaystyle\mathsf{E}\big[\mathcal{P}(\tau,\sigma)\big|\mathcal{H}\_{0}\big]=\mathsf{E}\Big[\int\_{[0,T)}f\_{t}(1-\zeta\_{t})\mathrm{d}\xi\_{t}+\int\_{[0,T)}g\_{t}(1-\xi\_{t})\mathrm{d}\zeta\_{t}+\sum\_{t\in[0,T]}h\_{t}\Delta\zeta\_{t}\Delta\xi\_{t}\Big|\mathcal{H}\_{0}\Big]. |  |

The argument is performed pathwise and it uses the well-known change of variable of integration from [[RY99](https://arxiv.org/html/2510.15616v1#bib.bibx40), Prop. 0.4.9].
We will use this formula and suitable variants thereof several times throughout the paper.

###### Notation 2.3.

From now on we denote (ξ∗,ζ∗)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\xi^{\*},\zeta^{\*})\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}) the pair of generating processes of a saddle point (τ∗,σ∗)∈𝒯0R​(𝔽1)×𝒯0R​(𝔽2)(\tau\_{\*},\sigma\_{\*})\in\mathcal{T}^{R}\_{0}(\mathbb{F}^{1})\times\mathcal{T}^{R}\_{0}(\mathbb{F}^{2}) for the game starting at time zero as in ([2.3](https://arxiv.org/html/2510.15616v1#S2.E3 "In 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")).

A dynamic formulation of the game requires a definition of upper and lower value at any random time θ\theta, much in the spirit of the formulation provided by [[LM84](https://arxiv.org/html/2510.15616v1#bib.bibx34)] for stopping games with full information. However, such approach also requires a definition of conditional expected payoff at time θ\theta and, due to the different filtrations available to the two players, there is no unique way to choose the conditioning σ\sigma-algebra. Likewise, it is not clear what random times θ\theta are to be considered. One possible approach would be to work with the common filtration shared by both players,
𝔽1,2=(ℱt1,2)t∈[0,T]\mathbb{F}^{1,2}=(\mathcal{F}^{1,2}\_{t})\_{t\in[0,T]} with ℱt1,2≔ℱt1∩ℱt2\mathcal{F}^{1,2}\_{t}\coloneqq\mathcal{F}^{1}\_{t}\cap\mathcal{F}^{2}\_{t}. Then, for θ∈𝒯0R​(𝔽1,2)\theta\in\mathcal{T}^{R}\_{0}(\mathbb{F}^{1,2}) we could consider the conditional upper and lower values

|  |  |  |  |
| --- | --- | --- | --- |
| (2.4) |  | V¯​(θ)≔ess​infτ∈𝒯θR​(𝔽1)⁡ess​supσ∈𝒯θR​(𝔽2)⁡𝖤​[𝒫​(τ,σ)|ℱθ1,2]andV¯​(θ)≔ess​supσ∈𝒯θR​(𝔽2)⁡ess​infτ∈𝒯θR​(𝔽1)⁡𝖤​[𝒫​(τ,σ)|ℱθ1,2].\displaystyle\overline{V}(\theta)\coloneqq\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1})}\operatorname\*{ess\,sup}\_{\sigma\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{2})}\mathsf{E}\big[\mathcal{P}(\tau,\sigma)\big|\mathcal{F}^{1,2}\_{\theta}\big]\quad\text{and}\quad\underline{V}(\theta)\coloneqq\operatorname\*{ess\,sup}\_{\sigma\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{2})}\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\big[\mathcal{P}(\tau,\sigma)|\mathcal{F}^{1,2}\_{\theta}\big]. |  |

Existence of a value V​(θ)=V¯​(θ)=V¯​(θ)V(\theta)=\overline{V}(\theta)=\underline{V}(\theta) and of a saddle point can be deduced by the argument of proof of [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12), Thm. 2.6]. Methods as those that we will illustrate in detail in later sections (cf. Corollary [3.13](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem13 "Corollary 3.13. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) allow us to aggregate the family {V​(θ),θ∈𝒯0R​(𝔽1,2)}\{V(\theta),\,\theta\in\mathcal{T}^{R}\_{0}(\mathbb{F}^{1,2})\} into a 𝔽1,2\mathbb{F}^{1,2}-adapted stochastic value process (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]}. However, this formulation is subject to a number of drawbacks. We mention two important ones: (i) since 𝔽1,2⊂𝔽i\mathbb{F}^{1,2}\subset\mathbb{F}^{i}, i=1,2i=1,2, the conditioning is not properly keeping track of players’ updates of their information over time (this becomes particularly apparent when ℱt1∩ℱt2={∅,Ω}\mathcal{F}^{1}\_{t}\cap\mathcal{F}^{2}\_{t}=\{\varnothing,\Omega\} for all t∈[0,T]t\in[0,T]); (ii) the dynamics of the value process (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]} does not, in general, reveal optimality conditions for the saddle point exactly because of the insufficient information content of the filtration 𝔽1,2\mathbb{F}^{1,2}. For these reasons we take a different approach, considering each player’s expected payoff, for a fixed strategy of their opponent. By doing that, we formally recast our zero-sum game as a nonzero-sum one. We proceed to illustrate the details in the next section.

### 2.1. Players’ subjective views and equilibrium values as families of random variables

As the game proceeds, players acquire more information via their filtration and, crucially, via actions of their opponent (or rather the lack of action, in the sense that they learn for as long as their opponent has not stopped). This naturally leads to a notion of players’ dynamic subjective view of the game. In order to capture that idea we need to work under dynamically changing probability measures, which motivates the next definition.

###### Definition 2.4.

Given a σ\sigma-algebra 𝒢⊆ℱ\mathcal{G}\subseteq\mathcal{F}, let

|  |  |  |
| --- | --- | --- |
|  | ℛ(𝒢)≔{Π:Π is ℱ-measurable with Π≥0 and 𝖤​[Π|𝒢]=1}.\mathcal{R}(\mathcal{G})\coloneqq\{\Pi:\text{$\Pi$ is $\mathcal{F}$-measurable with $\Pi\geq 0$ and $\mathsf{E}[\Pi|\mathcal{G}]=1$\}.} |  |

For Π∈ℛ​(𝒢)\Pi\in\mathcal{R}(\mathcal{G}) we denote by 𝖯Π\mathsf{P}^{\Pi} the probability measure defined by

|  |  |  |
| --- | --- | --- |
|  | 𝖯Π​(A)=𝖤​[1A​Π],for A∈ℱ.\mathsf{P}^{\Pi}(A)=\mathsf{E}[1\_{A}\Pi],\quad\text{for $A\in\mathcal{F}$}. |  |

The condition 𝖤​[Π|𝒢]=1\mathsf{E}[\Pi|\mathcal{G}]=1 satisfied by Π∈ℛ​(𝒢)\Pi\in\mathcal{R}(\mathcal{G}) is stronger than the usual condition 𝖤​[Π]=1\mathsf{E}[\Pi]=1, needed for the change of measure.
Indeed we observe that for Π∈ℛ​(𝒢)\Pi\in\mathcal{R}(\mathcal{G})

|  |  |  |
| --- | --- | --- |
|  | 𝖯Π​(A|𝒢)=𝖤Π​[1A|𝒢]=𝖤​[Π​1A|𝒢]𝖤​[Π|𝒢]=𝖤​[Π​1A|𝒢],\mathsf{P}^{\Pi}(A|\mathcal{G})=\mathsf{E}^{\Pi}[1\_{A}|\mathcal{G}]=\frac{\mathsf{E}[\Pi 1\_{A}|\mathcal{G}]}{\mathsf{E}[\Pi|\mathcal{G}]}=\mathsf{E}[\Pi 1\_{A}|\mathcal{G}], |  |

and therefore we have the interpretation

|  |  |  |  |
| --- | --- | --- | --- |
| (2.5) |  | Π=d𝖯Π(⋅|𝒢)d𝖯(⋅|𝒢).\displaystyle\Pi=\frac{\mathrm{d}\mathsf{P}^{\Pi}(\,\cdot\,|\mathcal{G})}{\mathrm{d}\mathsf{P}(\,\cdot\,|\mathcal{G})}. |  |

Recall the notation for an equilibrium pair (ξ∗,ζ∗)(\xi^{\*},\zeta^{\*}) from Notation [2.3](https://arxiv.org/html/2510.15616v1#S2.Thmtheorem3 "Notation 2.3. ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information"). For our purposes, we are particularly interested in the dynamic changes of measure induced by the families of random variables

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.6) |  | Πθ∗,1≔1−ζθ−∗𝖤​[1−ζθ−∗|ℱθ1],Π^θ∗,1≔1−ζθ−∗𝖤​[1−ζθ−∗|ℱθ−1],θ∈𝒯0​(𝔽1),Πγ∗,2≔1−ξγ−∗𝖤​[1−ξγ−∗|ℱγ2],Π^γ∗,2≔1−ξγ−∗𝖤​[1−ξγ−∗|ℱγ−2],γ∈𝒯0​(𝔽2),\displaystyle\begin{split}&\Pi^{\*,1}\_{\theta}\coloneqq\frac{1-\zeta^{\*}\_{\theta-}}{\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]},\quad\widehat{\Pi}^{\*,1}\_{\theta}\coloneqq\frac{1-\zeta^{\*}\_{\theta-}}{\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta-}]},\quad\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}),\\ &\Pi^{\*,2}\_{\gamma}\coloneqq\frac{1-\xi^{\*}\_{\gamma-}}{\mathsf{E}[1-\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}]},\quad\widehat{\Pi}^{\*,2}\_{\gamma}\coloneqq\frac{1-\xi^{\*}\_{\gamma-}}{\mathsf{E}[1-\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma-}]},\quad\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}),\end{split} | |  |

where the ratio is defined to be 11 whenever the denominator is 0. We emphasise that the random variables in ([2.6](https://arxiv.org/html/2510.15616v1#S2.E6 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) are defined 𝖯\mathsf{P}-a.s. as the conditional expectations are defined 𝖯\mathsf{P}-a.s. and the set of zero probability depends on θ\theta and γ\gamma, respectively. We notice that Πθ∗,1∈ℛ​(ℱθ1)\Pi^{\*,1}\_{\theta}\in\mathcal{R}(\mathcal{F}^{1}\_{\theta}) and Πγ∗,2∈ℛ​(ℱγ2)\Pi^{\*,2}\_{\gamma}\in\mathcal{R}(\mathcal{F}^{2}\_{\gamma}) whereas Π^θ∗,1∈ℛ​(ℱθ−1)\widehat{\Pi}^{\*,1}\_{\theta}\in\mathcal{R}(\mathcal{F}^{1}\_{\theta-}) and Π^γ∗,2∈ℛ​(ℱγ−2)\widehat{\Pi}^{\*,2}\_{\gamma}\in\mathcal{R}(\mathcal{F}^{2}\_{\gamma-}), by construction. Moreover, when the filtrations 𝔽1\mathbb{F}^{1} and 𝔽2\mathbb{F}^{2} are continuous we have (Π^θ∗,1,Π^γ∗,2)=(Πθ∗,1,Πγ∗,2)(\widehat{\Pi}^{\*,1}\_{\theta},\widehat{\Pi}^{\*,2}\_{\gamma})=(\Pi^{\*,1}\_{\theta},\Pi^{\*,2}\_{\gamma}).

To link random variables Πθ∗,1\Pi^{\*,1}\_{\theta} and Πγ∗,2\Pi^{\*,2}\_{\gamma} to players’ views on the remainder of the game, we notice that, for θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}),

|  |  |  |
| --- | --- | --- |
|  | 𝖯​(σ∗≥θ|ℱT)=𝖯​(ζθ−∗≤Zζ|ℱT)=1−ζθ−∗,\mathsf{P}(\sigma\_{\*}\geq\theta|\mathcal{F}\_{T})=\mathsf{P}(\zeta^{\*}\_{\theta-}\leq Z\_{\zeta}|\mathcal{F}\_{T})=1-\zeta^{\*}\_{\theta-}, |  |

where ZζZ\_{\zeta} is the randomisation device of Player 2. Upon conditioning on ℱθ1\mathcal{F}^{1}\_{\theta}, we further have 𝖯​(σ∗≥θ|ℱθ1)=𝖤​[1−ζθ−∗|ℱθ1]\mathsf{P}(\sigma\_{\*}\geq\theta|\mathcal{F}^{1}\_{\theta})=\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]. This offers a new perspective on Πθ∗,1\Pi^{\*,1}\_{\theta}:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.7) |  | Πθ∗,1=𝖯​(σ∗≥θ|ℱT)𝖯​(σ∗≥θ|ℱθ1)=𝖤​[𝟏{σ∗≥θ}|ℱT]𝖤​[𝟏{σ∗≥θ}|ℱθ1].\Pi^{\*,1}\_{\theta}=\frac{\mathsf{P}(\sigma\_{\*}\geq\theta|\mathcal{F}\_{T})}{\mathsf{P}(\sigma\_{\*}\geq\theta|\mathcal{F}^{1}\_{\theta})}=\frac{\mathsf{E}[\mathbf{1}\_{\{\sigma\_{\*}\geq\theta\}}|\mathcal{F}\_{T}]}{\mathsf{E}[\mathbf{1}\_{\{\sigma\_{\*}\geq\theta\}}|\mathcal{F}^{1}\_{\theta}]}. |  |

The expectation of an integrable ℱT\mathcal{F}\_{T}-measurable random variable XX given the information at time θ\theta and conditional on Player 2 not having terminated the game prior to θ\theta is given by (see [[Kal02](https://arxiv.org/html/2510.15616v1#bib.bibx28), Exercise 10, p. 94])

|  |  |  |  |
| --- | --- | --- | --- |
| (2.8) |  | 𝖤​[X|ℱθ1,σ∗≥θ]=𝖤​[X​𝟏{σ∗≥θ}|ℱθ1]𝖯​(σ∗≥θ|ℱθ1),on the event {𝖯​(σ∗≥θ|ℱθ1)>0}.\mathsf{E}[X|\mathcal{F}^{1}\_{\theta},\sigma\_{\*}\geq\theta]=\frac{\mathsf{E}[X\mathbf{1}\_{\{\sigma\_{\*}\geq\theta\}}|\mathcal{F}^{1}\_{\theta}]}{\mathsf{P}(\sigma\_{\*}\geq\theta|\mathcal{F}^{1}\_{\theta})},\qquad\text{on the event $\{\mathsf{P}(\sigma\_{\*}\geq\theta|\mathcal{F}^{1}\_{\theta})>0\}$.} |  |

Here, by the conditional expectation 𝖤​[X|ℱθ1,σ∗≥θ]\mathsf{E}[X|\mathcal{F}^{1}\_{\theta},\sigma\_{\*}\geq\theta] we mean the conditional expectation given ℱθ1∨σ​({σ∗≥θ})\mathcal{F}^{1}\_{\theta}\vee\sigma(\{\sigma\_{\*}\geq\theta\}). Definition ([2.7](https://arxiv.org/html/2510.15616v1#S2.E7 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) and the tower property of conditional expectation yield

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[X|ℱθ1,σ∗≥θ]=𝖤​[𝖤​[𝟏{σ∗≥θ}|ℱT]𝖯​(σ∗≥θ|ℱθ1)​X|ℱθ1]=𝖤​[Πθ∗,1​X|ℱθ1]=𝖤Πθ∗,1​[X|ℱθ1].\mathsf{E}[X|\mathcal{F}^{1}\_{\theta},\sigma\_{\*}\geq\theta]=\mathsf{E}\Big[\frac{\mathsf{E}[\mathbf{1}\_{\{\sigma\_{\*}\geq\theta\}}|\mathcal{F}\_{T}]}{\mathsf{P}(\sigma\_{\*}\geq\theta|\mathcal{F}^{1}\_{\theta})}X\Big|\mathcal{F}^{1}\_{\theta}\Big]=\mathsf{E}[\Pi^{\*,1}\_{\theta}X|\mathcal{F}^{1}\_{\theta}]=\mathsf{E}^{\Pi^{\*,1}\_{\theta}}[X|\mathcal{F}^{1}\_{\theta}]. |  |

Hence, the measure Πθ∗,1\Pi^{\*,1}\_{\theta} encapsulates conditioning on the event {σ∗≥θ}\{\sigma\_{\*}\geq\theta\}. The fact that a change of measure describes the conditioning is natural as Player 1 reassesses her perception of the world given that the opponent has not acted yet. This motivates the following terminology.

###### Definition 2.5.

The family of random variables {Πθ∗,1:θ∈𝒯0​(𝔽1)}\{\Pi^{\*,1}\_{\theta}:\ \theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})\} is called *Player 1’s subjective view*, while the family {Πγ∗,2:γ∈𝒯0​(𝔽2)}\{\Pi^{\*,2}\_{\gamma}:\ \gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2})\} is called *Player 2’s subjective view*.

It is worth noting that processes (Πt∗,i)t∈[0,T](\Pi^{\*,i}\_{t})\_{t\in[0,T]}, i=1,2i=1,2, are not adapted to players’ filtrations 𝔽i\mathbb{F}^{i}, i=1,2i=1,2. However, in the concrete examples of Section [5](https://arxiv.org/html/2510.15616v1#S5 "5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") we show how the players’ subjective views can be linked to belief processes which are adapted to the players’ filtrations.

It will emerge that assigning one to the ratios in ([2.6](https://arxiv.org/html/2510.15616v1#S2.E6 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) when the denominators are zero is convenient for the interpretation of Πθ∗,1\Pi^{\*,1}\_{\theta} and Πγ∗,2\Pi^{\*,2}\_{\gamma} as changes of probability measure. The freedom to choose this convention follows from the implication: for 𝖯\mathsf{P}-a.e. ω∈Ω\omega\in\Omega,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.9) |  | 𝖤​[1−ζθ−∗|ℱθ1]​(ω)=0⟹(1−ζθ−∗)​(ω)=0,\displaystyle\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}](\omega)=0\implies(1-\zeta^{\*}\_{\theta-})(\omega)=0, |  |

and analogously for ξ∗\xi^{\*}. For the proof, denote A={ω∈Ω:𝖤​[1−ζθ−∗|ℱθ1]​(ω)=0}A=\{\omega\in\Omega:\,\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}](\omega)=0\}. We have A∈ℱθ1A\in\mathcal{F}^{1}\_{\theta} and

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[1A​(1−ζθ−∗)]=𝖤​[1A​𝖤​[1−ζθ−∗|ℱθ1]]=0,\mathsf{E}\big[1\_{A}(1-\zeta^{\*}\_{\theta-})\big]=\mathsf{E}\big[1\_{A}\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]\big]=0, |  |

which, by the non-negativity of 1−ζθ−∗1-\zeta^{\*}\_{\theta-} implies that 1−ζθ−∗​(ω)=01-\zeta^{\*}\_{\theta-}(\omega)=0 for 𝖯\mathsf{P}-a.e. ω∈A\omega\in A.

###### Remark 2.6.

If regular conditional probabilities 𝖯(⋅|ℱθ1)\mathsf{P}(\,\cdot\,|\mathcal{F}^{1}\_{\theta}) and 𝖯(⋅|ℱθ−1)\mathsf{P}(\,\cdot\,|\mathcal{F}^{1}\_{\theta-}) exist, then the ratios in the first line of ([2.6](https://arxiv.org/html/2510.15616v1#S2.E6 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) can be defined ω\omega by ω\omega with the convention that 0/0=10/0=1. An analogous statement can be made for the second line of ([2.6](https://arxiv.org/html/2510.15616v1#S2.E6 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")). However, we want to avoid using regular conditional probabilities as their existence requires additional assumptions on the probability space and filtrations.

We now focus on the concept of the player’s equilibrium value, representing the player’s perception of the future play in the game,
based on the information gathered until a stopping time. For this, we need notions of *dynamic payoff* associated to a filtration 𝔾\mathbb{G} and *truncated controls*.

###### Definition 2.7.

Given θ∈𝒯0​(𝔾)\theta\in\mathcal{T}\_{0}(\mathbb{G}), Π∈ℛ​(𝒢θ)\Pi\in\mathcal{R}(\mathcal{G}\_{\theta}) and a pair (τ,σ)∈𝒯θR​(𝔽)×𝒯θR​(𝔽)(\tau,\sigma)\in\mathcal{T}^{R}\_{\theta}(\mathbb{F})\times\mathcal{T}^{R}\_{\theta}(\mathbb{F}), the *dynamic payoff* is defined as

|  |  |  |
| --- | --- | --- |
|  | JΠ​(τ,σ|𝒢θ)≔𝖤Π​[𝒫​(τ,σ)|𝒢θ]=𝖤​[Π​𝒫​(τ,σ)|𝒢θ],J^{\Pi}(\tau,\sigma|\mathcal{G}\_{\theta})\coloneqq\mathsf{E}^{\Pi}[\mathcal{P}(\tau,\sigma)|\mathcal{G}\_{\theta}]=\mathsf{E}[\Pi\mathcal{P}(\tau,\sigma)|\mathcal{G}\_{\theta}], |  |

where the final equality holds because Π∈ℛ​(𝒢θ)\Pi\in\mathcal{R}(\mathcal{G}\_{\theta}).

As in [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12), Sec. 4], using the definition of 𝒯θR​(𝔽)\mathcal{T}^{R}\_{\theta}(\mathbb{F}) we can derive the 𝒢θ\mathcal{G}\_{\theta}-conditional analogue of ([2.3](https://arxiv.org/html/2510.15616v1#S2.E3 "In 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")). That is, it is not hard to verify that

|  |  |  |  |
| --- | --- | --- | --- |
| (2.10) |  | JΠ​(τ,σ|𝒢θ)=JΠ​(ξ,ζ|𝒢θ)=𝖤Π​[∫[θ,T)ft​(1−ζt)​dξt+∫[θ,T)gt​(1−ξt)​dζt+∑t∈[θ,T]ht​Δ​ζt​Δ​ξt|𝒢θ]=𝖤​[Π​(∫[θ,T)ft​(1−ζt)​dξt+∫[θ,T)gt​(1−ξt)​dζt+∑t∈[θ,T]ht​Δ​ζt​Δ​ξt)|𝒢θ],\displaystyle\begin{aligned} &J^{\Pi}(\tau,\sigma|\mathcal{G}\_{\theta})=J^{\Pi}(\xi,\zeta|\mathcal{G}\_{\theta})\\ &=\mathsf{E}^{\Pi}\Big[\int\_{[\theta,T)}f\_{t}(1-\zeta\_{t})\mathrm{d}\xi\_{t}+\int\_{[\theta,T)}g\_{t}(1-\xi\_{t})\mathrm{d}\zeta\_{t}+\sum\_{t\in[\theta,T]}h\_{t}\Delta\zeta\_{t}\Delta\xi\_{t}\Big|\mathcal{G}\_{\theta}\Big]\\ &=\mathsf{E}\Big[\Pi\Big(\int\_{[\theta,T)}f\_{t}(1-\zeta\_{t})\mathrm{d}\xi\_{t}+\int\_{[\theta,T)}g\_{t}(1-\xi\_{t})\mathrm{d}\zeta\_{t}+\sum\_{t\in[\theta,T]}h\_{t}\Delta\zeta\_{t}\Delta\xi\_{t}\Big)\Big|\mathcal{G}\_{\theta}\Big],\end{aligned} |  |

where (ξ,ζ)∈𝒜θ∘​(𝔽)×𝒜θ∘​(𝔽)(\xi,\zeta)\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}) are the generating processes of the pair (τ,σ)(\tau,\sigma). This notation of generating processes will be upheld throughout the paper. With a slight abuse of notation, we will also write

|  |  |  |
| --- | --- | --- |
|  | 𝒫​(ξ,ζ)≔∫[0,T)ft​(1−ζt)​dξt+∫[0,T)gt​(1−ξt)​dζt+∑t∈[0,T]ht​Δ​ζt​Δ​ξt.\mathcal{P}(\xi,\zeta)\coloneqq\int\_{[0,T)}f\_{t}(1-\zeta\_{t})\mathrm{d}\xi\_{t}+\int\_{[0,T)}g\_{t}(1-\xi\_{t})\mathrm{d}\zeta\_{t}+\sum\_{t\in[0,T]}h\_{t}\Delta\zeta\_{t}\Delta\xi\_{t}. |  |

Using this notation, ([2.10](https://arxiv.org/html/2510.15616v1#S2.E10 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) reads JΠ​(ξ,ζ|𝒢θ)=𝖤​[Π​𝒫​(ξ,ζ)|𝒢θ]J^{\Pi}(\xi,\zeta|\mathcal{G}\_{\theta})=\mathsf{E}[\Pi\,\mathcal{P}(\xi,\zeta)|\mathcal{G}\_{\theta}] as the integrals and the sum over [0,θ)[0,\theta) are zero because (ξ,ζ)∈𝒜θ∘​(𝔽1)×𝒜θ∘​(𝔽2)(\xi,\zeta)\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{2}). When θ=0\theta=0 and Π=1\Pi=1, with 𝒢0⊇ℋ0\mathcal{G}\_{0}\supseteq\mathcal{H}\_{0}, we recover the expected payoff of the game 𝖤​[JΠ​(ξ,ζ|𝒢0)|ℋ0]=𝖤​[𝒫​(ξ,ζ)|ℋ0]\mathsf{E}[J^{\Pi}(\xi,\zeta|\mathcal{G}\_{0})|\mathcal{H}\_{0}]=\mathsf{E}[\mathcal{P}(\xi,\zeta)|\mathcal{H}\_{0}].

###### Definition 2.8.

Given a filtration 𝔾⊂𝔽\mathbb{G}\subset\mathbb{F}, a stopping time η∈𝒯0​(𝔾)\eta\in\mathcal{T}\_{0}(\mathbb{G}) and a generating pair (ξ,ζ)∈𝒜0∘​(𝔽)×𝒜0∘​(𝔽)(\xi,\zeta)\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}) of randomised stopping times, we call truncated controls the following processes:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.11) |  | ξtη≔ξt−ξη−1−ξη−​𝟏{t≥η}andζtη≔ζt−ζη−1−ζη−​𝟏{t≥η},for t∈[0,T],\displaystyle\xi^{\eta}\_{t}\coloneqq\frac{\xi\_{t}-\xi\_{\eta-}}{1-\xi\_{\eta-}}\mathbf{1}\_{\{t\geq\eta\}}\quad\text{and}\quad\zeta^{\eta}\_{t}\coloneqq\frac{\zeta\_{t}-\zeta\_{\eta-}}{1-\zeta\_{\eta-}}\mathbf{1}\_{\{t\geq\eta\}},\quad\text{for $t\in[0,T]$}, |  |

with the convention 0/0=10/0=1. By construction ξη−η=ζη−η=0\xi^{\eta}\_{\eta-}=\zeta^{\eta}\_{\eta-}=0 and ξTη=ζTη=1\xi^{\eta}\_{T}=\zeta^{\eta}\_{T}=1.

The dynamics of *equilibrium values*555In the theory of non-zero sum games, players’ equilibrium values are often called *equilibrium payoffs*, *expected payoffs* or *continuation values*. However, we decided to use the terms ‘equilibrium value’ or ‘player’s value’ to emphasise parallels with the full information theory of Dynkin games and to minimise confusion with payoff processes f,g,hf,g,h defining the game. (often referred to, in short, as *players’ values*) for the two players are modelled via two families of random variables

|  |  |  |  |
| --- | --- | --- | --- |
| (2.12) |  | {V∗,1​(θ),θ∈𝒯0​(𝔽1)}and{V∗,2​(γ),γ∈𝒯0​(𝔽2)},\displaystyle\big\{V^{\*,1}(\theta),\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})\big\}\quad\text{and}\quad\big\{V^{\*,2}(\gamma),\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2})\big\}, |  |

defined by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.13) |  | V∗,1​(θ)≔ess​infξ∈𝒜θ∘​(𝔽1)⁡JΠθ∗,1​(ξ,ζ∗;θ|ℱθ1) and V∗,2​(γ)≔ess​supζ∈𝒜γ∘​(𝔽2)⁡JΠγ∗,2​(ξ∗;γ,ζ|ℱγ2).\displaystyle V^{\*,1}(\theta)\coloneqq\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\circ}\_{\theta}(\mathbb{F}^{1})}J^{\Pi^{\*,1}\_{\theta}}\big(\xi,\zeta^{\*;\theta}\big|\mathcal{F}^{1}\_{\theta}\big)\quad\text{ and }\quad V^{\*,2}(\gamma)\coloneqq\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\circ}\_{\gamma}(\mathbb{F}^{2})}J^{\Pi^{\*,2}\_{\gamma}}\big(\xi^{\*;\gamma},\zeta\big|\mathcal{F}^{2}\_{\gamma}\big). |  |

We remark that the value of V∗,1​(θ)V^{\*,1}(\theta) on the event {𝖤​[ζθ−∗|ℱθ1]=1}⊆{ζθ−∗=1}\{\mathsf{E}[\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]=1\}\subseteq\{\zeta^{\*}\_{\theta-}=1\} (cf. ([2.9](https://arxiv.org/html/2510.15616v1#S2.E9 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information"))) is trivially equal to 𝖤​[gθ|ℱθ1]\mathsf{E}[g\_{\theta}|\mathcal{F}^{1}\_{\theta}]. Indeed, on this event, Πθ∗,1=1\Pi^{\*,1}\_{\theta}=1, ζθ−∗;θ=0\zeta^{\*;\theta}\_{\theta-}=0 and ζt∗;θ=1\zeta^{\*;\theta}\_{t}=1 for t∈[θ,T]t\in[\theta,T]; thus, JθΠ∗,1​(ξ,ζ∗;θ|ℱθ1)=𝖤​[gθ​(1−ξθ)+hθ​Δ​ξθ|ℱθ1]J^{\Pi^{\*,1}}\_{\theta}(\xi,\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})=\mathsf{E}[g\_{\theta}(1-\xi\_{\theta})+h\_{\theta}\Delta\xi\_{\theta}|\mathcal{F}^{1}\_{\theta}] for any ξ∈𝒜θ∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1}) and, since gθ≤hθg\_{\theta}\leq h\_{\theta}, it is optimal to choose ξθ=0\xi\_{\theta}=0.
Same comments apply to V∗,2​(γ)=𝖤​[fγ|ℱγ2]V^{\*,2}(\gamma)=\mathsf{E}[f\_{\gamma}|\mathcal{F}^{2}\_{\gamma}] on the event {𝖤​[ξγ−∗|ℱγ2]=1}\{\mathsf{E}[\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}]=1\}.
We note that the equilibrium values V∗,1​(θ)V^{\*,1}(\theta) and V∗,2​(γ)V^{\*,2}(\gamma) on the events {𝖤​[ζθ−∗|ℱθ1]=1}\{\mathsf{E}[\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]=1\} and {𝖤​[ξγ−∗|ℱγ2]=1}\{\mathsf{E}[\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}]=1\}, respectively, do not play any significant role in the context of the game:
in most expressions V∗,1​(θ)V^{\*,1}(\theta) and V∗,2​(γ)V^{\*,2}(\gamma) are preceded by 𝖤​[1−ζθ−∗|ℱθ1]\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}] and 𝖤​[1−ξγ−∗|ℱγ2]\mathsf{E}[1-\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}], respectively (see, e.g., Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")).

The interpretation of V∗,1​(θ)V^{\*,1}(\theta) (and analogously for V∗,2​(γ)V^{\*,2}(\gamma)) is as follows: at time zero the game starts and the players pick an optimal pair (ξ∗,ζ∗)(\xi^{\*},\zeta^{\*}); at time θ\theta, if the game has not ended, Player 1 calculates V∗,1​(θ)V^{\*,1}(\theta) as the smallest payoff they can attain with a best response to the remainder of strategy ζ∗\zeta^{\*} on the interval [θ,T][\theta,T]. We are going to show in Proposition [3.8](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") that the truncated control ξ∗;θ\xi^{\*;\theta} attains the infimum in V∗,1​(θ)V^{\*,1}(\theta) and, analogously, ζ∗;γ\zeta^{\*;\gamma} attains the infimum in V∗,2​(γ)V^{\*,2}(\gamma). Thus, for any β∈𝒯R​(𝔽1,2)\beta\in\mathcal{T}^{R}(\mathbb{F}^{1,2}) the pair of truncated controls (ξ∗;β,ζ∗;β)(\xi^{\*;\beta},\zeta^{\*;\beta}) is a saddle point for the game started at β\beta with payoff 𝖤​[𝒫​(ξ,ζ)|ℱβ1,2]\mathsf{E}[\mathcal{P}(\xi,\zeta)|\mathcal{F}^{1,2}\_{\beta}] for (ξ,ζ)∈𝒜β∘​(𝔽1)×𝒜β∘​(𝔽2)(\xi,\zeta)\in\mathcal{A}^{\circ}\_{\beta}(\mathbb{F}^{1})\times\mathcal{A}^{\circ}\_{\beta}(\mathbb{F}^{2}) (cf. Proposition [3.10](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem10 "Proposition 3.10. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and Corollary [3.13](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem13 "Corollary 3.13. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") for further details).

###### Remark 2.9.

In the theory of zero-sum games with full information, values V∗,1​(β)V^{\*,1}(\beta) and V∗,2​(β)V^{\*,2}(\beta) coincide for any stopping time β\beta with respect to the common filtration. They are then termed the value of the game and play a pivotal role in determining players’ optimal strategies. Here, the values of players are distinct for multiple reasons: (i) they are defined for different familites of random times, (ii) they condition on the information available to the player at that time, and (iii) they include the updated perception of the future probabilities via Π∗,j\Pi^{\*,j} arising from learning from the opponent’s inaction.

In view of the above remark, it should come as no surprise that the families of random variables ([2.12](https://arxiv.org/html/2510.15616v1#S2.E12 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) are the main object of interest throughout the paper. We will establish a link between the two via the so-called ex-ante value of the game in Corollary [3.13](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem13 "Corollary 3.13. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

###### Convention 2.10.

For the ease of exposition, in the next sections we assume ℋ0={Ω,∅}\mathcal{H}\_{0}=\{\Omega,\varnothing\}. This comes with no loss of generality because all results continue to hold with generic ℋ0⊆ℱ01∩ℱ02\mathcal{H}\_{0}\subseteq\mathcal{F}^{1}\_{0}\cap\mathcal{F}^{2}\_{0} upon replacing everywhere the unconditional expectation 𝖤​[⋅]\mathsf{E}[\cdot] with conditional one 𝖤[⋅|ℋ0]\mathsf{E}[\cdot|\mathcal{H}\_{0}].

### 2.2. Roadmap

To facilitate reading of the upcoming technical content, we provide intuitions and a quick sketch of results to come. Section [3](https://arxiv.org/html/2510.15616v1#S3 "3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") is devoted to the derivation of necessary conditions, i.e., of conditions that must be satisfied by players’ equilibrium values and their optimal strategies. Unlike the classical theory of Dynkin games, where the equilibrium value can be defined without knowing players’ optimal strategies, here those strategies play a pivotal role: they reveal additional information that shapes players’ subjective views about the remainder of the game and the probability measures (𝖯Πθ∗,1\mathsf{P}^{\Pi^{\*,1}\_{\theta}} and 𝖯Πγ∗,2\mathsf{P}^{\Pi^{\*,2}\_{\gamma}}) under which they assess future payoffs. A subset of those necessary conditions is shown in Section [4](https://arxiv.org/html/2510.15616v1#S4 "4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") to be sufficient for a saddle point. Hence, we will concentrate on explaining our ideas guiding developments in Section [3](https://arxiv.org/html/2510.15616v1#S3 "3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

We start by recalling the classical theory of Dynkin games with full information. Denoting by VtV\_{t} the value process and by (τ^,σ^)(\hat{\tau},\hat{\sigma}) a saddle point, they satisfy the super- and sub-martingale conditions:

|  |  |  |
| --- | --- | --- |
|  | t↦Vt∧τ^​ is a supermartingale and​t↦Vt∧σ^​ is a submartingale.\displaystyle t\mapsto V\_{t\wedge\hat{\tau}}\text{ is a supermartingale and}\ t\mapsto V\_{t\wedge\hat{\sigma}}\text{ is a submartingale.} |  |

In our framework, due to involvement of randomised strategies and learning, these martingale conditions take a much more complicated form. For θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}) and γ∈𝒯0​(𝔽2)\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}), let

|  |  |  |  |
| --- | --- | --- | --- |
|  | M0​(θ)\displaystyle M^{0}(\theta) | =𝖤​[∫[0,θ)gt​dζt∗|ℱθ1]+𝖤​[1−ζθ−∗|ℱθ1]​V∗,1​(θ),\displaystyle=\mathsf{E}\Big[\int\_{[0,\theta)}\!\!g\_{t}\mathrm{d}\zeta^{\*}\_{t}\!\Big|\mathcal{F}^{1}\_{\theta}\Big]+\mathsf{E}[1\!-\!\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]V^{\*,1}(\theta), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | N0​(γ)\displaystyle N^{0}(\gamma) | =𝖤​[∫[0,γ)ft​dξt∗|ℱγ2]+𝖤​[1−ξγ−∗|ℱγ2]​V∗,2​(γ);\displaystyle=\mathsf{E}\Big[\!\int\_{[0,\gamma)}\!\!f\_{t}\mathrm{d}\xi^{\*}\_{t}\Big|\mathcal{F}^{2}\_{\gamma}\Big]+\mathsf{E}[1\!-\!\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}]V^{\*,2}(\gamma); |  |

such familities of random variables will be defined in greater generality in Section [3.2](https://arxiv.org/html/2510.15616v1#S3.SS2 "3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). We then show that the family {M0​(θ):θ∈𝒯0​(𝔽1)}\{M^{0}(\theta):\ \theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})\} can be aggregared into a càdlàg 𝔽1\mathbb{F}^{1}-submartingale (Mt0)t∈[0,T](M^{0}\_{t})\_{t\in[0,T]} and the family {N0​(γ):γ∈𝒯0​(𝔽2)}\{N^{0}(\gamma):\ \gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2})\} can be aggregared into a càdlàg 𝔽2\mathbb{F}^{2}-supermartingale (Nt0)t∈[0,T](N^{0}\_{t})\_{t\in[0,T]}. An analogue of the martingale condition for t↦Vt∧τ^∧σ^t\mapsto V\_{t\wedge\hat{\tau}\wedge\hat{\sigma}} requires new families of random variables {M∗​(θ):θ∈𝒯0​(𝔽1)}\{M^{\*}(\theta):\ \theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})\} and {N∗​(γ):γ∈𝒯0​(𝔽2)}\{N^{\*}(\gamma):\ \gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2})\} involving both ξ∗\xi^{\*} and ζ∗\zeta^{\*}, which can be aggregated into 𝔽1\mathbb{F}^{1} and 𝔽2\mathbb{F}^{2}-martingales, respectively.

Differently from the full information setting, where the aggregation of the value process is done directly, in our setting players’ equilibrium values are aggregated indirectly through the families {M0​(θ):θ∈𝒯0​(𝔽1)}\{M^{0}(\theta):\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})\} and {N0​(γ):γ∈𝒯0​(𝔽2)}\{N^{0}(\gamma):\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2})\}. To be more precise, the families

|  |  |  |
| --- | --- | --- |
|  | {𝖤[1−ζθ−∗|ℱθ1]V∗,1(θ):θ∈𝒯0(𝔽1)}and{𝖤[1−ξγ−∗|ℱγ2]V∗,2(γ):γ∈𝒯0(𝔽2)}\{\mathsf{E}[1\!-\!\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]V^{\*,1}(\theta):\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})\}\quad\text{and}\quad\{\mathsf{E}[1\!-\!\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}]V^{\*,2}(\gamma):\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2})\} |  |

are aggregated into optional semi-martingales. The prefactor in front of the equilibrium value is needed because a player’s value is only defined as long as the game has not been terminated by the opponent; it should be stressed that its role is purely technical: it is non-zero if and only if there is a possibility of the opponent to be still in the game given the information available to the player; however, players observe when the game finishes so the game will never be active when the prefactor is 0, see also ([2.9](https://arxiv.org/html/2510.15616v1#S2.E9 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")).

Our final major aim is to identify the support of optimal strategies of players, understood as the set of times when players may stop optimally. In the classical theory, that is the coincidence set of the value process with respective payoffs. We show in Subsection [3.4](https://arxiv.org/html/2510.15616v1#S3.SS4 "3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") that a close analogue of this behaviour holds in the present much more complex setting. To simplify this informal presentation, assume that players do not act simultaneously, i.e., Δ​ξt∗​Δ​ζt∗=0\Delta\xi^{\*}\_{t}\Delta\zeta^{\*}\_{t}=0 for all t∈[0,T]t\in[0,T]. Define

|  |  |  |
| --- | --- | --- |
|  | Yt1≔V^t∗,1−(of⋅(1−ζ⋅∗))t𝔽1andYt2≔V^t∗,2−(og⋅(1−ξ⋅∗))t𝔽2,Y^{1}\_{t}\coloneqq\hat{V}^{\*,1}\_{t}-\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}f\_{\cdot}(1-\zeta^{\*}\_{\cdot})\big)\_{t}^{\mathbb{F}^{1}}\quad\text{and}\quad Y^{2}\_{t}\coloneqq\hat{V}^{\*,2}\_{t}-\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}g\_{\cdot}(1-\xi^{\*}\_{\cdot})\big)^{\mathbb{F}^{2}}\_{t}, |  |

where (o⋅)t𝔾\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-4.5449pt{o}\kern 2.12502pt}}\_{{\kern-1.66977pt\kern 2.12502pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-4.5449pt{o}\kern 2.12502pt}}\_{{\kern-1.66977pt\kern 2.12502pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-2.64682pt{o}\kern 0.90555pt}}\_{{\kern-0.4503pt\kern 0.90555pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-2.10239pt{o}\kern 0.36111pt}}\_{{\kern 0.09413pt\kern 0.36111pt}}}\cdot)^{\mathbb{G}}\_{t} denotes the optional projection with respect to the filtration 𝔾\mathbb{G}. We take the perspective of Player 1. The quantity (of⋅(1−ζ⋅∗))t𝔽1\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}f\_{\cdot}(1-\zeta^{\*}\_{\cdot})\big)\_{t}^{\mathbb{F}^{1}} is the perception of the payoff if Player 1 stops the game at time tt – the optional projection is needed as neither the process ff nor the opponent’s strategy ζ∗\zeta^{\*} have to be 𝔽1\mathbb{F}^{1}-adapted. In analogy to the full information game, we will show that Yt1≤0Y^{1}\_{t}\leq 0 for any t∈[0,T]t\in[0,T], i.e., the equilibrium value of Player 1 is dominated by the optional projection of the payoff – a natural requirement for a minimiser. Furthermore, we will show that Player 1 acts only when Yt1=0Y^{1}\_{t}=0, which is formally written as ∫[0,T]Yt1​dξt∗=0\int\_{[0,T]}Y^{1}\_{t}\mathrm{d}\xi^{\*}\_{t}=0. Analogous conditions for Player 2 are Yt2≥0Y^{2}\_{t}\geq 0 and ∫[0,T]Yt2​dζt∗=0\int\_{[0,T]}Y^{2}\_{t}\mathrm{d}\zeta^{\*}\_{t}=0.

The above conditions allow, in specific settings, to formulate variational inequalities for equilibrium value functions and to postulate players’ action sets – the sets on which players are allowed to increase their generating processes. Such examples are discussed in Section [5](https://arxiv.org/html/2510.15616v1#S5 "5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information").

## 3. Necessary conditions for a saddle point

In this section we obtain properties of the equilibrium values of the two players and of their optimal strategies. The analysis is performed in a dynamic setting.
We will later show in Section [4](https://arxiv.org/html/2510.15616v1#S4 "4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") that such properties are indeed sufficient to characterise any equilibrium in the game.
Since the section is quite rich of technical materials it is worth summarising here the results that, taken together, provide the desired necessary conditions. In particular, we are going to prove:

* •

  Aggregation into optional semi-martingales of players’ equilibrium values (Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")),
* •

  Martingale characterisation of players’ equilibrium values (Propositions [3.7](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem7 "Proposition 3.7. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and [3.8](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), and Corollary [3.16](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem16 "Corollary 3.16. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")),
* •

  Link between players’ equilibrium values and ex-ante value of the game (Proposition [3.10](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem10 "Proposition 3.10. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and Corollary [3.13](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem13 "Corollary 3.13. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")),
* •

  Properties of equilibrium strategies and their link to the dynamics of equilibrium values (Proposition [3.17](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem17 "Proposition 3.17. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and Corollary [3.19](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem19 "Corollary 3.19. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")).

### 3.1. Aggregation of the equilibrium dynamics

The first step in our analysis is to aggregate the families ([2.12](https://arxiv.org/html/2510.15616v1#S2.E12 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) into stochastic processes. For the convenience of the reader, we collect aggregation results from the general theory of stochastic processes in Appendix [A](https://arxiv.org/html/2510.15616v1#A1 "Appendix A Review of aggregation results ‣ Martingale theory for Dynkin games with asymmetric information").
We start by showing upward/downward-directed properties (cf. Appendix [B](https://arxiv.org/html/2510.15616v1#A2 "Appendix B Upward and downward directed families ‣ Martingale theory for Dynkin games with asymmetric information")) of the payoffs in ([2.13](https://arxiv.org/html/2510.15616v1#S2.E13 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) which allow replacing essential suprema/infima with monotone limits.

###### Lemma 3.1.

Given θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}),
the family {JΠθ∗,1​(ξ,ζ∗;θ|ℱθ1),ξ∈𝒜θ∘​(𝔽1)}\{J^{\Pi^{\*,1}\_{\theta}}(\xi,\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta}),\ \xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1})\} is downward-directed. Therefore, there is a sequence (ξn)n∈ℕ⊂𝒜θ∘​(𝔽1)(\xi^{n})\_{n\in\mathbb{N}}\subset\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1}) such that

|  |  |  |
| --- | --- | --- |
|  | V∗,1​(θ)=limn→∞JΠθ∗,1​(ξn,ζ∗;θ|ℱθ1),V^{\*,1}(\theta)=\lim\_{n\to\infty}J^{\Pi^{\*,1}\_{\theta}}(\xi^{n},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta}), |  |

where the limit is monotone from above.

Analogously, given γ∈𝒯0​(𝔽2)\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}),
the family {JΠγ∗,2​(ξ∗;γ,ζ|ℱγ2),ζ∈𝒜γ∘​(𝔽2)}\{J^{\Pi^{\*,2}\_{\gamma}}(\xi^{\*;\gamma},\zeta|\mathcal{F}^{2}\_{\gamma}),\ \zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\gamma}(\mathbb{F}^{2})\} is upward-directed. Therefore, there is a sequence (ζn)n∈ℕ⊂𝒜γ∘​(𝔽2)(\zeta^{n})\_{n\in\mathbb{N}}\subset\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\gamma}(\mathbb{F}^{2}) such that

|  |  |  |
| --- | --- | --- |
|  | V∗,2​(γ)=limn→∞JΠγ∗,2​(ξ∗;γ,ζn|ℱγ2),V^{\*,2}(\gamma)=\lim\_{n\to\infty}J^{\Pi^{\*,2}\_{\gamma}}(\xi^{\*;\gamma},\zeta^{n}|\mathcal{F}^{2}\_{\gamma}), |  |

where the limit is monotone from below.

The proof is completely standard and it is provided in Appendix [C.1](https://arxiv.org/html/2510.15616v1#A3.SS1 "C.1. Proof of Lemma 3.1 ‣ Appendix C Remaining proofs ‣ Martingale theory for Dynkin games with asymmetric information"). The next lemma states that each player’s equilibrium value is attained in pure strategies once the other player’s strategy is fixed. Notice, however, that equilibria in pure strategies do not exist in the generality of our setting (see various counterexamples in, e.g., [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12), Sec. 6]).

###### Lemma 3.2.

For (θ,γ)∈𝒯0​(𝔽1)×𝒯0​(𝔽2)(\theta,\gamma)\in\mathcal{T}\_{0}(\mathbb{F}^{1})\times\mathcal{T}\_{0}(\mathbb{F}^{2}), let τ∗γ\tau\_{\*}^{\gamma} and σ∗θ\sigma\_{\*}^{\theta} be the randomised stopping times generated by the truncated controls ξ∗;γ\xi^{\*;\gamma} and ζ∗;θ\zeta^{\*;\theta}, respectively. Then

|  |  |  |  |
| --- | --- | --- | --- |
| (3.1) |  | V∗,1​(θ)=ess​infτ∈𝒯θ​(𝔽1)⁡JΠθ∗,1​(τ,σ∗θ|ℱθ1)andV∗,2​(γ)=ess​supσ∈𝒯γ​(𝔽2)⁡JΠγ∗,2​(τγ∗,σ|ℱγ2).\displaystyle V^{\*,1}(\theta)=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}J^{\Pi^{\*,1}\_{\theta}}(\tau,\sigma\_{\*}^{\theta}|\mathcal{F}^{1}\_{\theta})\quad\text{and}\quad V^{\*,2}(\gamma)=\operatorname\*{ess\,sup}\_{\sigma\in\mathcal{T}\_{\gamma}(\mathbb{F}^{2})}J^{\Pi^{\*,2}\_{\gamma}}(\tau\_{\gamma}^{\*},\sigma|\mathcal{F}^{2}\_{\gamma}). |  |

###### Proof.

We only prove the claim for V∗,1​(θ)V^{\*,1}(\theta) as the one for V∗,2​(γ)V^{\*,2}(\gamma) can be proven analogously.

By Lemma [3.1](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem1 "Lemma 3.1. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), there is a sequence (ξn)⊂𝒜θ∘​(𝔽1)(\xi\_{n})\subset\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}\_{1}) such that

|  |  |  |
| --- | --- | --- |
|  | V∗,1​(θ)=limn→∞JΠθ∗,1​(ξn,ζ∗;θ|ℱθ1),𝖯−a.s.V^{\*,1}(\theta)=\lim\_{n\to\infty}J^{\Pi^{\*,1}\_{\theta}}(\xi^{n},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta}),\quad\mathsf{P}-a.s. |  |

We take expectation on both sides and apply the monotone convergence theorem to obtain

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[V∗,1​(θ)]=limn→∞𝖤​[Πθ∗,1​𝒫​(ξn,ζ∗;θ)].\mathsf{E}\big[V^{\*,1}(\theta)\big]=\lim\_{n\to\infty}\mathsf{E}\big[\Pi^{\*,1}\_{\theta}\mathcal{P}(\xi^{n},\zeta^{\*;\theta})\big]. |  |

Combining the above equality with the following upper bound

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[V∗,1​(θ)]=𝖤​[ess​infξ∈𝒜θ∘​(𝔽1)⁡JΠθ∗,1​(ξ,ζ∗;θ|ℱθ1)]≤infξ∈𝒜θ∘​(𝔽1)𝖤​[JΠθ∗,1​(ξ,ζ∗;θ|ℱθ1)]=infξ∈𝒜θ∘​(𝔽1)𝖤​[Πθ∗,1​𝒫​(ξ,ζ∗;θ)]\mathsf{E}\big[V^{\*,1}(\theta)\big]=\mathsf{E}\big[\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1})}J^{\Pi^{\*,1}\_{\theta}}(\xi,\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})\big]\leq\inf\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\big[J^{\Pi^{\*,1}\_{\theta}}(\xi,\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})\big]=\inf\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\big[\Pi^{\*,1}\_{\theta}\mathcal{P}(\xi,\zeta^{\*;\theta})\big] |  |

we obtain

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | 𝖤​[V∗,1​(θ)]=𝖤​[ess​infξ∈𝒜θ∘​(𝔽1)⁡JΠθ∗,1​(ξ,ζ∗;θ|ℱθ1)]=infξ∈𝒜θ∘​(𝔽1)𝖤​[Πθ∗,1​𝒫​(ξ,ζ∗;θ)]=infτ∈𝒯θR​(𝔽1)𝖤​[Πθ∗,1​𝒫​(τ,σ∗θ)],\displaystyle\begin{aligned} \mathsf{E}\big[V^{\*,1}(\theta)\big]&=\mathsf{E}\big[\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1})}J^{\Pi^{\*,1}\_{\theta}}(\xi,\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})\big]\\ &=\inf\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\big[\Pi^{\*,1}\_{\theta}\mathcal{P}(\xi,\zeta^{\*;\theta})\big]=\inf\_{\tau\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\big[\Pi^{\*,1}\_{\theta}\mathcal{P}(\tau,\sigma\_{\*}^{\theta})\big],\end{aligned} |  |

where the last equality is due to the relationship between randomised stopping times and their generating processes. For τ∈𝒯θR​(ℱθ1)\tau\in\mathcal{T}^{R}\_{\theta}(\mathcal{F}^{1}\_{\theta}), recalling the notation τ​(z)=τ​(ξ,z)\tau(z)=\tau(\xi,z), z∈[0,1]z\in[0,1], from ([2.1](https://arxiv.org/html/2510.15616v1#S2.E1 "In 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | infτ∈𝒯θR​(𝔽1)𝖤​[Πθ∗,1​𝒫​(τ,σ∗θ)]\displaystyle\inf\_{\tau\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\big[\Pi^{\*,1}\_{\theta}\mathcal{P}(\tau,\sigma\_{\*}^{\theta})\big] | =infτ∈𝒯θR​(𝔽1)∫01𝖤​[Πθ∗,1​𝒫​(τ​(z),σ∗θ)]​𝑑z\displaystyle=\inf\_{\tau\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1})}\int\_{0}^{1}\mathsf{E}\big[\Pi^{\*,1}\_{\theta}\mathcal{P}(\tau(z),\sigma\_{\*}^{\theta})\big]dz |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥infτ∈𝒯θR​(𝔽1)∫01infτ¯∈𝒯θ​(𝔽1)𝖤​[Πθ∗,1​𝒫​(τ¯,σ∗θ)]​d​z\displaystyle\geq\inf\_{\tau\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1})}\int\_{0}^{1}\inf\_{\bar{\tau}\in\mathcal{T}\_{\theta}(\mathbb{F}\_{1})}\mathsf{E}\big[\Pi^{\*,1}\_{\theta}\mathcal{P}(\bar{\tau},\sigma\_{\*}^{\theta})\big]dz |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =infτ∈𝒯θ​(𝔽1)𝖤​[Πθ∗,1​𝒫​(τ,σ∗θ)]=infτ∈𝒯θ​(𝔽1)𝖤​[JΠθ∗,1​(τ,σ∗θ|ℱθ1)],\displaystyle=\inf\_{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\big[\Pi^{\*,1}\_{\theta}\mathcal{P}(\tau,\sigma\_{\*}^{\theta})\big]=\inf\_{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\big[J^{\Pi^{\*,1}\_{\theta}}(\tau,\sigma\_{\*}^{\theta}|\mathcal{F}^{1}\_{\theta})\big], |  |

where in the first inequality we integrate with respect to the distribution of Player 1’s randomisation device and the inequality holds because τ​(z)∈𝒯θ​(𝔽1)\tau(z)\in\mathcal{T}\_{\theta}(\mathbb{F}^{1}) for each z∈[0,1]z\in[0,1]. We insert this estimate into the equality ([3.2](https://arxiv.org/html/2510.15616v1#S3.E2 "In 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) to notice

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[ess​infτ∈𝒯θR​(𝔽1)⁡JΠθ∗,1​(τ,σ∗θ|ℱθ1)]≥infτ∈𝒯θ​(𝔽1)𝖤​[JΠθ∗,1​(τ,σ∗θ|ℱθ1)]≥𝖤​[ess​infτ∈𝒯θ​(𝔽1)⁡JΠθ∗,1​(τ,σ∗θ|ℱθ1)].\mathsf{E}\big[\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1})}J^{\Pi^{\*,1}\_{\theta}}(\tau,\sigma\_{\*}^{\theta}|\mathcal{F}^{1}\_{\theta})\big]\geq\inf\_{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\big[J^{\Pi^{\*,1}\_{\theta}}(\tau,\sigma\_{\*}^{\theta}|\mathcal{F}^{1}\_{\theta})\big]\geq\mathsf{E}\big[\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}J^{\Pi^{\*,1}\_{\theta}}(\tau,\sigma\_{\*}^{\theta}|\mathcal{F}^{1}\_{\theta})\big]. |  |

Since trivially ess​infτ∈𝒯θR​(𝔽1)⁡JΠθ∗,1​(τ,σ∗θ|ℱθ1)≤ess​infτ∈𝒯θ​(𝔽1)⁡JΠθ∗,1​(τ,σ∗θ|ℱθ1)\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1})}J^{\Pi^{\*,1}\_{\theta}}(\tau,\sigma\_{\*}^{\theta}|\mathcal{F}^{1}\_{\theta})\leq\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}J^{\Pi^{\*,1}\_{\theta}}(\tau,\sigma\_{\*}^{\theta}|\mathcal{F}^{1}\_{\theta}), we have

|  |  |  |
| --- | --- | --- |
|  | ess​infτ∈𝒯θR​(𝔽1)⁡JΠθ∗,1​(τ,σ∗θ|ℱθ1)=ess​infτ∈𝒯θ​(𝔽1)⁡JΠθ∗,1​(τ,σ∗θ|ℱθ1),\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1})}J^{\Pi^{\*,1}\_{\theta}}(\tau,\sigma\_{\*}^{\theta}|\mathcal{F}^{1}\_{\theta})=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}J^{\Pi^{\*,1}\_{\theta}}(\tau,\sigma\_{\*}^{\theta}|\mathcal{F}^{1}\_{\theta}), |  |

which concludes the proof.
∎

It should be noted that the randomised stopping times τ∗γ\tau\_{\*}^{\gamma} and σ∗θ\sigma\_{\*}^{\theta} appearing in the above lemma may not belong to 𝒯γR​(𝔽1)\mathcal{T}\_{\gamma}^{R}(\mathbb{F}^{1}) and 𝒯θR​(𝔽2)\mathcal{T}\_{\theta}^{R}(\mathbb{F}^{2}), respectively, because γ\gamma and θ\theta are stopping times with respect to the opponent’s filtration. This fact causes no difficulty in the statements and proofs above and we recall that τ∗γ\tau\_{\*}^{\gamma} can be expressed in terms of the truncated control ξ∗;γ\xi^{\*;\gamma}, representing the remainder of Player 1’s stopping after time γ\gamma (we can argue analogously for σ∗θ\sigma^{\theta}\_{\*} and ζ∗;θ\zeta^{\*;\theta}). Finally, we recall that the smallest filtration under which τ∗γ\tau\_{\*}^{\gamma} is a randomised stopping time is ℱt1∨σ​(γ∧t)\mathcal{F}^{1}\_{t}\vee\sigma(\gamma\wedge t), t∈[0,T]t\in[0,T] (or equivalently ℱt1∨σ​(γ∧s,s≤t)\mathcal{F}^{1}\_{t}\vee\sigma(\gamma\wedge s,\ s\leq t), t∈[0,T]t\in[0,T]). Analogous considerations hold for σ∗θ\sigma\_{\*}^{\theta}.

An analogue of Lemma [3.1](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem1 "Lemma 3.1. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") holds for pure stopping times. The proof of Lemma [3.1](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem1 "Lemma 3.1. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") can be repeated nearly verbatim or one can use the classical optimal stopping theory recalled in Appendix [B](https://arxiv.org/html/2510.15616v1#A2 "Appendix B Upward and downward directed families ‣ Martingale theory for Dynkin games with asymmetric information"). The result is formulated rigorously in the corollary below.

###### Corollary 3.3.

Given θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}),
the family {JΠθ∗,1​(τ,σ∗θ|ℱθ1),τ∈𝒯θ​(𝔽1)}\{J^{\Pi^{\*,1}\_{\theta}}(\tau,\sigma\_{\*}^{\theta}|\mathcal{F}^{1}\_{\theta}),\ \tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})\} is downward-directed. Therefore, there is a sequence (τn)n∈ℕ⊂𝒯θ​(𝔽1)(\tau^{n})\_{n\in\mathbb{N}}\subset\mathcal{T}\_{\theta}(\mathbb{F}^{1}) such that

|  |  |  |
| --- | --- | --- |
|  | V∗,1​(θ)=limn→∞JΠθ∗,1​(τn,σ∗θ|ℱθ1),V^{\*,1}(\theta)=\lim\_{n\to\infty}J^{\Pi^{\*,1}\_{\theta}}(\tau^{n},\sigma\_{\*}^{\theta}|\mathcal{F}^{1}\_{\theta}), |  |

where the limit is monotone from above.

Analogously, given γ∈𝒯0​(𝔽2)\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}),
the family {JΠγ∗,2​(τγ∗,σ|ℱγ2),σ∈𝒯γ​(𝔽2)}\{J^{\Pi^{\*,2}\_{\gamma}}(\tau\_{\gamma}^{\*},\sigma|\mathcal{F}^{2}\_{\gamma}),\ \sigma\in\mathcal{T}\_{\gamma}(\mathbb{F}^{2})\} is upward-directed. Therefore, there is a sequence (σn)n∈ℕ⊂𝒯γ​(𝔽2)(\sigma^{n})\_{n\in\mathbb{N}}\subset\mathcal{T}\_{\gamma}(\mathbb{F}^{2}) such that

|  |  |  |
| --- | --- | --- |
|  | V∗,2​(γ)=limn→∞JΠγ∗,2​(τγ∗,σn|ℱγ2),V^{\*,2}(\gamma)=\lim\_{n\to\infty}J^{\Pi^{\*,2}\_{\gamma}}(\tau\_{\gamma}^{\*},\sigma^{n}|\mathcal{F}^{2}\_{\gamma}), |  |

where the limit is monotone from below.

We state here the main aggregation result concerning players’ values V∗,iV^{\*,i}, i=1,2i=1,2.
Its proof
is formally presented in Section [3.3](https://arxiv.org/html/2510.15616v1#S3.SS3 "3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").
Before stating the theorem, we introduce some notation. Given a process (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} we define its left and right limit as

|  |  |  |
| --- | --- | --- |
|  | Xt0+≔lims>t0s→t0Xs=lims↓t0Xs and Xt0−≔lims<t0s→t0Xs=lims↑t0Xs,X\_{t\_{0}+}\coloneqq\lim\_{\stackrel{{\scriptstyle s\to t\_{0}}}{{s>t\_{0}}}}X\_{s}=\lim\_{s\downarrow t\_{0}}X\_{s}\quad\text{ and }\quad X\_{t\_{0}-}\coloneqq\lim\_{\stackrel{{\scriptstyle s\to t\_{0}}}{{s<t\_{0}}}}X\_{s}=\lim\_{s\uparrow t\_{0}}X\_{s}, |  |

whenever they exist. In order to emphasise that a process (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} is adapted/optional/previsible with respect to a filtration 𝔾\mathbb{G}, we use (Xt,𝔾)t∈[0,T](X\_{t},\mathbb{G})\_{t\in[0,T]} or, occasionally, (Xt,𝔾,𝖯)t∈[0,T](X\_{t},\mathbb{G},\mathsf{P})\_{t\in[0,T]}.

###### Theorem 3.4.

Given an optimal pair (ξ∗,ζ∗)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\xi^{\*},\zeta^{\*})\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}), the families

|  |  |  |  |
| --- | --- | --- | --- |
| (3.3) |  | 𝐕∗,1≔{𝖤​[1−ζθ−∗|ℱθ1]​V∗,1​(θ),θ∈𝒯0​(𝔽1)},𝐕∗,2≔{𝖤​[1−ξγ−∗|ℱγ2]​V∗,2​(γ),γ∈𝒯0​(𝔽2)},\displaystyle\begin{aligned} &{\bf V}^{\*,1}\coloneqq\big\{\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]\,V^{\*,1}(\theta),\,\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})\big\},\\ &{\bf V}^{\*,2}\coloneqq\big\{\mathsf{E}[1-\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}]\,V^{\*,2}(\gamma),\,\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2})\big\},\end{aligned} |  |

can be aggregated into optional semi-martingale processes of class (D)(D)

|  |  |  |
| --- | --- | --- |
|  | (V^t∗,1,𝔽1)t∈[0,T]and(V^t∗,2,𝔽2)t∈[0,T],\displaystyle\big(\hat{V}^{\*,1}\_{t},\,\mathbb{F}^{1}\big)\_{t\in[0,T]}\quad\text{and}\quad\big(\hat{V}^{\*,2}\_{t},\,\mathbb{F}^{2}\big)\_{t\in[0,T]}, |  |

where, for θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}) and γ∈𝒯0​(𝔽2)\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}),

|  |  |  |  |
| --- | --- | --- | --- |
| (3.4) |  | V^θ∗,1=ess​infτ∈𝒯θ​(𝔽1)⁡𝖤​[fτ​(1−ζτ∗)+∫[θ,τ)gu​dζu∗+hτ​Δ​ζτ∗|ℱθ1],V^γ∗,2=ess​supσ∈𝒯γ​(𝔽2)⁡𝖤​[gσ​(1−ξσ∗)+∫[γ,σ)fu​dξu∗+hσ​Δ​ξσ∗|ℱγ2].\displaystyle\begin{aligned} \hat{V}^{\*,1}\_{\theta}&=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\tau}(1-\zeta^{\*}\_{\tau})+\int\_{[\theta,\tau)}g\_{u}\mathrm{d}\zeta^{\*}\_{u}+h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta}\Big],\\ \hat{V}^{\*,2}\_{\gamma}&=\operatorname\*{ess\,sup}\_{\sigma\in\mathcal{T}\_{\gamma}(\mathbb{F}^{2})}\mathsf{E}\Big[g\_{\sigma}(1-\xi^{\*}\_{\sigma})+\int\_{[\gamma,\sigma)}f\_{u}\mathrm{d}\xi^{\*}\_{u}+h\_{\sigma}\Delta\xi^{\*}\_{\sigma}\Big|\mathcal{F}^{2}\_{\gamma}\Big].\end{aligned} |  |

Moreover, for θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}) and γ∈𝒯0​(𝔽2)\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}) the limits below hold 𝖯\mathsf{P}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
| (3.5) |  | V^θ+∗,1=V^θ∗,1−𝖤​[1−ζθ−∗|ℱθ1]​𝖤Πθ∗,1​[gθ​Δ​ζθ∗;θ|ℱθ1]=V^θ∗,1−𝖤​[gθ​Δ​ζθ∗|ℱθ1],V^γ+∗,2=V^γ∗,2−𝖤​[1−ξγ−∗|ℱγ2]​𝖤Πγ∗,2​[fγ​Δ​ξγ∗;γ|ℱγ2]=V^γ∗,2−𝖤​[fγ​Δ​ξγ∗|ℱγ2].\displaystyle\begin{aligned} &\hat{V}^{\*,1}\_{\theta+}=\hat{V}^{\*,1}\_{\theta}-\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]\,\mathsf{E}^{\Pi^{\*,1}\_{\theta}}[g\_{\theta}\Delta\zeta^{\*;\theta}\_{\theta}|\mathcal{F}^{1}\_{\theta}]=\hat{V}^{\*,1}\_{\theta}-\mathsf{E}[g\_{\theta}\Delta\zeta^{\*}\_{\theta}|\mathcal{F}^{1}\_{\theta}],\\ &\hat{V}^{\*,2}\_{\gamma+}=\hat{V}^{\*,2}\_{\gamma}-\mathsf{E}[1-\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}]\,\mathsf{E}^{\Pi^{\*,2}\_{\gamma}}[f\_{\gamma}\Delta\xi^{\*;\gamma}\_{\gamma}|\mathcal{F}^{2}\_{\gamma}]=\hat{V}^{\*,2}\_{\gamma}-\mathsf{E}[f\_{\gamma}\Delta\xi^{\*}\_{\gamma}|\mathcal{F}^{2}\_{\gamma}].\end{aligned} |  |

Finally, for any previsible θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}) and γ∈𝒯0​(𝔽2)\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}),

|  |  |  |  |
| --- | --- | --- | --- |
| (3.6) |  | V^θ−∗,1≤𝖤​[1−ζθ−∗|ℱθ−1]​ess​infξ∈𝒜θ∘​(𝔽1)⁡JΠ^θ∗,1​(ξ,ζ∗;θ|ℱθ−1),V^γ−∗,2≥𝖤​[1−ξγ−∗|ℱγ−2]​ess​supζ∈𝒜γ∘​(𝔽2)⁡JΠ^γ∗,2​(ξ∗;γ,ζ|ℱγ−2),\displaystyle\begin{aligned} \hat{V}^{\*,1}\_{\theta-}&\leq\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta-}]\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1})}J^{\widehat{\Pi}^{\*,1}\_{\theta}}\big(\xi,\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta-}),\\ \hat{V}^{\*,2}\_{\gamma-}&\geq\mathsf{E}[1-\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma-}]\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\gamma}(\mathbb{F}^{2})}J^{\widehat{\Pi}^{\*,2}\_{\gamma}}\big(\xi^{\*;\gamma},\zeta|\mathcal{F}^{2}\_{\gamma-}),\end{aligned} |  |

with equality on the events {ξθ−∗<1}\{\xi^{\*}\_{\theta-}<1\} and {ζγ−∗<1}\{\zeta^{\*}\_{\gamma-}<1\}, respectively, and Π^θ∗,1\widehat{\Pi}^{\*,1}\_{\theta} and Π^γ∗,2\widehat{\Pi}^{\*,2}\_{\gamma} defined in ([2.6](https://arxiv.org/html/2510.15616v1#S2.E6 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")).
Thus, if the filtrations 𝔽1\mathbb{F}^{1} and 𝔽2\mathbb{F}^{2} are continuous, the processes (V^t∗,1)t∈[0,T](\hat{V}^{\*,1}\_{t})\_{t\in[0,T]}, (V^t∗,2)t∈[0,T](\hat{V}^{\*,2}\_{t})\_{t\in[0,T]} are càglàd as long as ξt−∗<1\xi^{\*}\_{t-}<1 and ζt−∗<1\zeta^{\*}\_{t-}<1, respectively.

It is important to notice that in the formulae ([3.4](https://arxiv.org/html/2510.15616v1#S3.E4 "In Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) for the processes (V^t∗,i)t∈[0,T](\hat{V}^{\*,i}\_{t})\_{t\in[0,T]}, i=1,2i=1,2, the optimisation runs over stopping times for the players’ respective filtrations. This is a result that we will essentially derive from the Lemma [3.2](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

From the definition of Π^θ∗,1\widehat{\Pi}^{\*,1}\_{\theta} in ([2.6](https://arxiv.org/html/2510.15616v1#S2.E6 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) it is easy to verify that, for any previsible θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}) and γ∈𝒯0​(𝔽2)\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}), the right-hand sides of inequalities in ([3.6](https://arxiv.org/html/2510.15616v1#S3.E6 "In Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) can be equivalently written as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.7) |  |  | 𝖤​[1−ζθ−∗|ℱθ−1]​ess​infξ∈𝒜θ∘​(𝔽1)⁡JΠ^θ∗,1​(ξ,ζ∗;θ|ℱθ−1)=ess​infτ∈𝒯θ​(𝔽1)⁡𝖤​[fτ​(1−ζτ∗)+∫[θ,τ)gu​dζu∗+hτ​Δ​ζτ∗|ℱθ−1],\displaystyle\mathsf{E}[1\!-\!\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta-}]\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1})}J^{\widehat{\Pi}^{\*,1}\_{\theta}}\big(\xi,\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta-})=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\tau}(1\!-\!\zeta^{\*}\_{\tau})\!+\!\int\_{[\theta,\tau)}\!\!g\_{u}\mathrm{d}\zeta^{\*}\_{u}\!+\!h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta-}\Big], |  |
|  |  | 𝖤​[1−ξγ−∗|ℱγ−2]​ess​supζ∈𝒜γ∘​(𝔽2)⁡JΠ^γ∗,2​(ξ∗;γ,ζ|ℱγ−2)=ess​supσ∈𝒯γ​(𝔽2)⁡𝖤​[gσ​(1−ξσ∗)+∫[γ,σ)fu​dξu∗+hσ​Δ​ξσ∗|ℱγ−2].\displaystyle\mathsf{E}[1\!-\!\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma-}]\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\gamma}(\mathbb{F}^{2})}J^{\widehat{\Pi}^{\*,2}\_{\gamma}}\big(\xi^{\*;\gamma},\zeta|\mathcal{F}^{2}\_{\gamma-})=\operatorname\*{ess\,sup}\_{\sigma\in\mathcal{T}\_{\gamma}(\mathbb{F}^{2})}\mathsf{E}\Big[g\_{\sigma}(1\!-\!\xi^{\*}\_{\sigma})\!+\!\int\_{[\gamma,\sigma)}\!\!f\_{u}\mathrm{d}\xi^{\*}\_{u}\!+\!h\_{\sigma}\Delta\xi^{\*}\_{\sigma}\Big|\mathcal{F}^{2}\_{\gamma-}\Big]. |  |

This observation allows us to derive a corollary that refines Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

###### Corollary 3.5.

When the first inequality in ([3.6](https://arxiv.org/html/2510.15616v1#S3.E6 "In Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) is strict, we have V^θ−∗,1=𝖤​[fθ−​(1−ζθ−∗)|ℱθ−1]\hat{V}^{\*,1}\_{\theta-}=\mathsf{E}\big[f\_{\theta-}(1-\zeta^{\*}\_{\theta-})\big|\mathcal{F}^{1}\_{\theta-}\big]. When the second inequality in ([3.6](https://arxiv.org/html/2510.15616v1#S3.E6 "In Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) is strict, we have V^γ−∗,2=𝖤​[gγ−​(1−ξγ−∗)|ℱγ−2]\hat{V}^{\*,2}\_{\gamma-}=\mathsf{E}[g\_{\gamma-}(1-\xi^{\*}\_{\gamma-})|\mathcal{F}^{2}\_{\gamma-}].
Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^θ−∗,1\displaystyle\hat{V}^{\*,1}\_{\theta-} | =min⁡(𝖤​[fθ−​(1−ζθ−∗)|ℱθ−1],ess​infτ∈𝒯θ​(𝔽1)⁡𝖤​[fτ​(1−ζτ∗)+∫[θ,τ)gu​dζu∗+hτ​Δ​ζτ∗|ℱθ−1]),\displaystyle=\min\Big(\mathsf{E}\big[f\_{\theta-}(1-\zeta^{\*}\_{\theta-})\big|\mathcal{F}^{1}\_{\theta-}\big],\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\tau}(1\!-\!\zeta^{\*}\_{\tau})\!+\!\int\_{[\theta,\tau)}\!\!g\_{u}\mathrm{d}\zeta^{\*}\_{u}\!+\!h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta-}\Big]\Big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | V^γ−∗,2\displaystyle\hat{V}^{\*,2}\_{\gamma-} | =max⁡(𝖤​[gγ−​(1−ξγ−∗)|ℱγ−2],ess​supσ∈𝒯γ​(𝔽2)⁡𝖤​[gσ​(1−ξσ∗)+∫[γ,σ)fu​dξu∗+hσ​Δ​ξσ∗|ℱγ−2]).\displaystyle=\max\Big(\mathsf{E}[g\_{\gamma-}(1-\xi^{\*}\_{\gamma-})|\mathcal{F}^{2}\_{\gamma-}],\operatorname\*{ess\,sup}\_{\sigma\in\mathcal{T}\_{\gamma}(\mathbb{F}^{2})}\mathsf{E}\Big[g\_{\sigma}(1\!-\!\xi^{\*}\_{\sigma})\!+\!\int\_{[\gamma,\sigma)}\!\!f\_{u}\mathrm{d}\xi^{\*}\_{u}\!+\!h\_{\sigma}\Delta\xi^{\*}\_{\sigma}\Big|\mathcal{F}^{2}\_{\gamma-}\Big]\Big). |  |

This corollary is justified after the proof of Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") in Section [3.3](https://arxiv.org/html/2510.15616v1#S3.SS3 "3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

### 3.2. Auxiliary super/sub-martingale systems

Let us now prepare the ground for the proof of Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and for the martingale characterisation of players’ values by first introducing two auxiliary families of random variables.
Let (ξ,ζ)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\xi,\zeta)\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}) be an arbitrary pair and recall that (ξ∗,ζ∗)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\xi^{\*},\zeta^{\*})\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}) is an optimal pair for the game started at zero in ([2.2](https://arxiv.org/html/2510.15616v1#S2.E2 "In 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) (cf. Notation [2.3](https://arxiv.org/html/2510.15616v1#S2.Thmtheorem3 "Notation 2.3. ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")). Let 𝐌ξ≔{Mξ​(θ),θ∈𝒯0​(𝔽1)}{\bf M}^{\xi}\coloneqq\{M^{\xi}(\theta),\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})\} and 𝐍ζ≔{Nζ​(γ),γ∈𝒯0​(𝔽2)}{\bf N}^{\zeta}\coloneqq\{N^{\zeta}(\gamma),\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2})\} be defined as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.8) |  | Mξ​(θ)\displaystyle M^{\xi}(\theta) | =𝖤​[∫[0,θ)ft​(1−ζt∗)​dξt+∫[0,θ)gt​(1−ξt)​dζt∗+∑t∈[0,θ)ht​Δ​ξt​Δ​ζt∗|ℱθ1]\displaystyle=\mathsf{E}\Big[\!\int\_{[0,\theta)}\!\!f\_{t}(1\!-\!\zeta^{\*}\_{t})\mathrm{d}\xi\_{t}\!+\!\int\_{[0,\theta)}\!\!g\_{t}(1\!-\!\xi\_{t})\mathrm{d}\zeta^{\*}\_{t}\!+\!\!\sum\_{t\in[0,\theta)}\!\!h\_{t}\Delta\xi\_{t}\Delta\zeta^{\*}\_{t}\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−ξθ−)​𝖤​[1−ζθ−∗|ℱθ1]​V∗,1​(θ),\displaystyle\quad+\!(1\!-\!\xi\_{\theta-})\mathsf{E}[1\!-\!\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]V^{\*,1}(\theta), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.9) |  | Nζ​(γ)\displaystyle N^{\zeta}(\gamma) | =𝖤​[∫[0,γ)ft​(1−ζt)​dξt∗+∫[0,γ)gt​(1−ξt∗)​dζt+∑t∈[0,γ)ht​Δ​ξt∗​Δ​ζt|ℱγ2]\displaystyle=\mathsf{E}\Big[\!\int\_{[0,\gamma)}\!\!f\_{t}(1\!-\!\zeta\_{t})\mathrm{d}\xi^{\*}\_{t}\!+\!\int\_{[0,\gamma)}\!\!g\_{t}(1\!-\!\xi^{\*}\_{t})\mathrm{d}\zeta\_{t}\!+\!\!\sum\_{t\in[0,\gamma)}\!\!h\_{t}\Delta\xi^{\*}\_{t}\Delta\zeta\_{t}\Big|\mathcal{F}^{2}\_{\gamma}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−ζγ−)​𝖤​[1−ξγ−∗|ℱγ2]​V∗,2​(γ).\displaystyle\quad+\!(1\!-\!\zeta\_{\gamma-})\mathsf{E}[1\!-\!\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}]V^{\*,2}(\gamma). |  |

Two choices of ξ\xi and ζ\zeta will be of particular interest in the paper: (i) ξ≡ξ∗\xi\equiv\xi^{\*} and ζ≡ζ∗\zeta\equiv\zeta^{\*}, yielding 𝐌∗=𝐌ξ∗{\bf M}^{\*}={\bf M}^{\xi^{\*}} and 𝐍∗=𝐍ζ∗{\bf N}^{\*}={\bf N}^{\zeta^{\*}}, respectively, and (ii) ξ≡0\xi\equiv 0 and ζ≡0\zeta\equiv 0, yielding 𝐌0{\bf M}^{0} and 𝐍0{\bf N}^{0}, respectively. The families 𝐌∗{\bf M}^{\*} and 𝐍∗{\bf N}^{\*}, where both players are acting optimally, will be shown to form martingale systems – an analogue of the martingale condition for the value process Vt∧τ^∧σ^V\_{t\wedge\hat{\tau}\wedge\hat{\sigma}} in the full-information game (cf. Subsection [2.2](https://arxiv.org/html/2510.15616v1#S2.SS2 "2.2. Roadmap ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")).
Related super- and submartingale conditions will be formulated for the families 𝐌0{\bf M}^{0} and 𝐍0{\bf N}^{0} as mentioned in Subsection [2.2](https://arxiv.org/html/2510.15616v1#S2.SS2 "2.2. Roadmap ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information").

The pair (ξ∗,ζ∗)(\xi^{\*},\zeta^{\*}) generates the randomised stopping times (τ∗,σ∗)=(τ∗​(ξ∗,Z1),σ∗​(ζ∗,Z2))(\tau\_{\*},\sigma\_{\*})=(\tau\_{\*}(\xi^{\*},Z\_{1}),\sigma\_{\*}(\zeta^{\*},Z\_{2})) (Definition [2.2](https://arxiv.org/html/2510.15616v1#S2.Thmtheorem2 "Definition 2.2. ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")), where Z1Z\_{1} and Z2Z\_{2} are uniformly distributed on [0,1][0,1], independent of ℱT\mathcal{F}\_{T} and also mutually independent. For z∈[0,1)z\in[0,1) we denote,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.10) |  | τ¯∗​(z)=inf{t∈[0,T]:ξt∗>z}andσ¯∗​(z)=inf{t∈[0,T]:ζt∗>z},\displaystyle\bar{\tau}\_{\*}(z)=\inf\{t\in[0,T]:\xi^{\*}\_{t}>z\}\quad\text{and}\quad\bar{\sigma}\_{\*}(z)=\inf\{t\in[0,T]:\zeta^{\*}\_{t}>z\}, |  |

so that τ∗=τ¯∗​(Z1)\tau\_{\*}=\bar{\tau}\_{\*}(Z\_{1}) and σ∗=σ¯∗​(Z2)\sigma\_{\*}=\bar{\sigma}\_{\*}(Z\_{2}). Since z↦τ¯∗​(z)z\mapsto\bar{\tau}\_{\*}(z) and z↦σ¯∗​(z)z\mapsto\bar{\sigma}\_{\*}(z) are increasing, we can define the pair of largest optimal stopping times

|  |  |  |  |
| --- | --- | --- | --- |
| (3.11) |  | τ¯∗​(1)=inf{t∈[0,T]:ξt∗=1}andσ¯∗​(1)=inf{t∈[0,T]:ζt∗=1}.\displaystyle\bar{\tau}\_{\*}(1)=\inf\{t\in[0,T]:\xi^{\*}\_{t}=1\}\quad\text{and}\quad\bar{\sigma}\_{\*}(1)=\inf\{t\in[0,T]:\zeta^{\*}\_{t}=1\}. |  |

The stopping time τ¯∗​(1)∧σ¯∗​(1)\bar{\tau}\_{\*}(1)\wedge\bar{\sigma}\_{\*}(1) is the latest time at which the game – started at time zero – ends, in equilibrium.

###### Remark 3.6.

Observe that τ¯∗​(z)∈𝒯​(𝔽1)\bar{\tau}\_{\*}(z)\in\mathcal{T}(\mathbb{F}^{1}) for each z∈(0,1)z\in(0,1). Moreover, it follows from the proof of Lemma [3.2](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") that V∗,1​(0)=J​(τ¯∗​(z),σ∗|ℱ01)V^{\*,1}(0)=J(\bar{\tau}\_{\*}(z),\sigma\_{\*}|\mathcal{F}^{1}\_{0}) for a.e. z∈(0,1)z\in(0,1). Hence, the optimal strategy τ∗\tau\_{\*} can be interpreted as a randomisation over *optimal pure* stopping times τ¯∗​(z)\bar{\tau}\_{\*}(z) for Player 1. An analogous conclusion holds for the pair σ¯∗​(z)\bar{\sigma}\_{\*}(z) and σ∗\sigma\_{\*}, concerning Player 2. Further properties of the optimal strategies are presented in Subsection [3.4](https://arxiv.org/html/2510.15616v1#S3.SS4 "3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

In the next proposition we show (super/sub)martingale properties of the families 𝐌0{\bf M}^{0}, 𝐌∗{\bf M}^{\*}, 𝐍0{\bf N}^{0} and 𝐍∗{\bf N}^{\*} that lead to aggregation results. A reader unfamiliar with notions of super/sub-martingale systems may refer to Definition [A.1](https://arxiv.org/html/2510.15616v1#A1.Thmtheorem1 "Definition A.1. ‣ Appendix A Review of aggregation results ‣ Martingale theory for Dynkin games with asymmetric information") in Appendix [A](https://arxiv.org/html/2510.15616v1#A1 "Appendix A Review of aggregation results ‣ Martingale theory for Dynkin games with asymmetric information").

###### Proposition 3.7.

The family 𝐌0{\bf M}^{0} is a 𝒯0​(𝔽1)\mathcal{T}\_{0}(\mathbb{F}^{1})-submartingale system and the family 𝐍0{\bf N}^{0} is a 𝒯0​(𝔽2)\mathcal{T}\_{0}(\mathbb{F}^{2})-supermartingale system. Both families are right-continuous in expectation and of class (D)(D). Thus, they can be aggregated (uniquely up to indistinguishability) into a càdlàg submartingale (Mt0,𝔽1,𝖯)t∈[0,T](M^{0}\_{t},\mathbb{F}^{1},\mathsf{P})\_{t\in[0,T]} and a càdlàg supermartingale (Nt0,𝔽2,𝖯)t∈[0,T](N^{0}\_{t},\mathbb{F}^{2},\mathsf{P})\_{t\in[0,T]}, respectively.

###### Proof.

From the definition of V∗,1​(θ)V^{\*,1}(\theta) and V∗,2​(γ)V^{\*,2}(\gamma) (cf. Eq. ([2.12](https://arxiv.org/html/2510.15616v1#S2.E12 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information"))) it is not difficult to verify that the families 𝐌ξ{\bf M}^{\xi} and 𝐍ζ{\bf N}^{\zeta} are a 𝒯0​(𝔽1)\mathcal{T}\_{0}(\mathbb{F}^{1})-system and a 𝒯0​(𝔽2)\mathcal{T}\_{0}(\mathbb{F}^{2})-system, respectively, for any choice of ξ∈𝒜0∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1}) and ζ∈𝒜0∘​(𝔽2)\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}). It remains to verify the claimed (super/sub)martingale properties. We only present a proof for 𝐌0{\bf M}^{0} as analogous arguments apply to 𝐍0{\bf N}^{0}.

Since f,g∈ℒb​(𝖯)f,g\in\mathcal{L}\_{b}(\mathsf{P}), it is easy to verify that 𝐌0{\bf M}^{0} satisfies 𝖤​[ess​supθ∈𝒯0​(𝔽1)⁡|M0​(θ)|]<∞\mathsf{E}[\operatorname\*{ess\,sup}\_{\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})}|M^{0}(\theta)|]<\infty. Hence the family is of class (D)(D).
The submartingale property of 𝐌0{\bf M}^{0} is equivalent to 𝖤​[M0​(τ)]≥𝖤​[M0​(σ)]\mathsf{E}[M^{0}(\tau)]\geq\mathsf{E}[M^{0}(\sigma)] for every τ,σ∈𝒯0​(𝔽1)\tau,\sigma\in\mathcal{T}\_{0}(\mathbb{F}^{1}), σ≤τ\sigma\leq\tau (cf. Lemma [A.4](https://arxiv.org/html/2510.15616v1#A1.Thmtheorem4 "Lemma A.4. ‣ Appendix A Review of aggregation results ‣ Martingale theory for Dynkin games with asymmetric information")), which we are about to prove.

Take τ,σ∈𝒯0​(𝔽1)\tau,\sigma\in\mathcal{T}\_{0}(\mathbb{F}^{1}), σ≤τ\sigma\leq\tau. We will argue first on the event {σ<T}\{\sigma<T\} as on the event {σ=T}\{\sigma=T\} we trivially have M0​(σ)=M0​(τ)=M0​(T)M^{0}(\sigma)=M^{0}(\tau)=M^{0}(T).
By the definition of M0M^{0} we have

|  |  |  |  |
| --- | --- | --- | --- |
| (3.12) |  | M0​(σ)=𝖤​[∫[0,σ)gt​dζt∗|ℱσ1]+𝖤​[1−ζσ−∗|ℱσ1]​V∗,1​(σ).M^{0}(\sigma)=\mathsf{E}\Big[\int\_{[0,\sigma)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}\Big|\mathcal{F}^{1}\_{\sigma}\Big]+\mathsf{E}[1-\zeta^{\*}\_{\sigma-}|\mathcal{F}^{1}\_{\sigma}]\,V^{\*,1}(\sigma). |  |

We recall from ([2.13](https://arxiv.org/html/2510.15616v1#S2.E13 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) the definition of V∗,1​(σ)V^{\*,1}(\sigma) and use Lemma [3.2](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") to obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.13) |  |  | 𝖤​[1−ζσ−∗|ℱσ1]​V∗,1​(σ)\displaystyle\mathsf{E}[1-\zeta^{\*}\_{\sigma-}|\mathcal{F}^{1}\_{\sigma}]V^{\*,1}(\sigma) |  |
|  |  | =𝖤​[1−ζσ−∗|ℱσ1]​ess​infθ∈𝒯σ​(𝔽1)⁡𝖤​[Πσ∗,1​(fθ​(1−ζθ∗;σ)+∫[σ,θ)gt​dζt∗;σ+hθ​Δ​ζθ∗;σ)|ℱσ1]\displaystyle=\mathsf{E}[1-\zeta^{\*}\_{\sigma-}|\mathcal{F}^{1}\_{\sigma}]\operatorname\*{ess\,inf}\_{\theta\in\mathcal{T}\_{\sigma}(\mathbb{F}^{1})}\mathsf{E}\Big[\Pi^{\*,1}\_{\sigma}\Big(f\_{\theta}(1-\zeta^{\*;\sigma}\_{\theta})+\int\_{[\sigma,\theta)}g\_{t}\mathrm{d}\zeta^{\*;\sigma}\_{t}+h\_{\theta}\Delta\zeta^{\*;\sigma}\_{\theta}\Big)\Big|\mathcal{F}^{1}\_{\sigma}\Big] |  |
|  |  | =ess​infθ∈𝒯σ​(𝔽1)⁡𝖤​[fθ​(1−ζθ∗)+∫[σ,θ)gt​dζt∗+hθ​Δ​ζθ∗|ℱσ1],\displaystyle=\operatorname\*{ess\,inf}\_{\theta\in\mathcal{T}\_{\sigma}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\theta}(1-\zeta^{\*}\_{\theta})+\int\_{[\sigma,\theta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\theta}\Delta\zeta^{\*}\_{\theta}\Big|\mathcal{F}^{1}\_{\sigma}\Big], |  |

where for the second equality we used 𝖤​[1−ζσ−∗|ℱσ1]​Πθ∗,1=1−ζσ−∗\mathsf{E}[1-\zeta^{\*}\_{\sigma-}|\mathcal{F}^{1}\_{\sigma}]\Pi^{\*,1}\_{\theta}=1-\zeta^{\*}\_{\sigma-} by the definition of Πθ∗,1\Pi^{\*,1}\_{\theta} in ([2.6](https://arxiv.org/html/2510.15616v1#S2.E6 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) and the definition of truncated controls (cf. ([2.11](https://arxiv.org/html/2510.15616v1#S2.E11 "In Definition 2.8. ‣ 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information"))). Hence, taking η∈𝒯τ​(𝔽1)⊂𝒯σ​(𝔽1)\eta\in\mathcal{T}\_{\tau}(\mathbb{F}^{1})\subset\mathcal{T}\_{\sigma}(\mathbb{F}^{1}) we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.14) |  |  | 𝖤​[1−ζσ−∗|ℱσ1]​V∗,1​(σ)≤𝖤​[fη​(1−ζη∗)+∫[σ,η)gt​dζt∗+hη​Δ​ζη∗|ℱσ1]\displaystyle\mathsf{E}[1-\zeta^{\*}\_{\sigma-}|\mathcal{F}^{1}\_{\sigma}]V^{\*,1}(\sigma)\leq\mathsf{E}\Big[f\_{\eta}(1-\zeta^{\*}\_{\eta})+\int\_{[\sigma,\eta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\eta}\Delta\zeta^{\*}\_{\eta}\Big|\mathcal{F}^{1}\_{\sigma}\Big] |  |
|  |  | =𝖤​[fη​(1−ζη∗)+∫[σ,τ)gt​dζt∗+∫[τ,η)gt​dζt∗+hη​Δ​ζη∗|ℱσ1]\displaystyle=\mathsf{E}\Big[f\_{\eta}(1-\zeta^{\*}\_{\eta})+\int\_{[\sigma,\tau)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\int\_{[\tau,\eta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\eta}\Delta\zeta^{\*}\_{\eta}\Big|\mathcal{F}^{1}\_{\sigma}\Big] |  |
|  |  | =𝖤​[∫[σ,τ)gt​dζt∗+𝖤​[fη​(1−ζη∗)+∫[τ,η)gt​dζt∗+hη​Δ​ζη∗|ℱτ1]|ℱσ1]\displaystyle=\mathsf{E}\bigg[\int\_{[\sigma,\tau)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\mathsf{E}\Big[f\_{\eta}(1-\zeta^{\*}\_{\eta})+\int\_{[\tau,\eta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\eta}\Delta\zeta^{\*}\_{\eta}\Big|\mathcal{F}^{1}\_{\tau}\Big]\bigg|\mathcal{F}^{1}\_{\sigma}\bigg] |  |
|  |  | =𝖤​[∫[σ,τ)gt​dζt∗+𝖤​[1−ζτ−∗|ℱτ1]​𝖤​[Πτ∗,1​(fη​(1−ζη∗;τ)+∫[τ,η)gt​dζt∗;τ+hη​Δ​ζη∗;τ)|ℱτ1]|ℱσ1]\displaystyle=\mathsf{E}\bigg[\int\_{[\sigma,\tau)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\mathsf{E}[1-\zeta^{\*}\_{\tau-}|\mathcal{F}^{1}\_{\tau}]\mathsf{E}\Big[\Pi^{\*,1}\_{\tau}\Big(f\_{\eta}(1-\zeta^{\*;\tau}\_{\eta})+\int\_{[\tau,\eta)}g\_{t}\mathrm{d}\zeta^{\*;\tau}\_{t}+h\_{\eta}\Delta\zeta^{\*;\tau}\_{\eta}\Big)\Big|\mathcal{F}^{1}\_{\tau}\Big]\bigg|\mathcal{F}^{1}\_{\sigma}\bigg] |  |
|  |  | =𝖤​[∫[σ,τ)gt​dζt∗+𝖤​[1−ζτ−∗|ℱτ1]​JΠτ∗,1​(η,σ∗τ|ℱτ1)|ℱσ1],\displaystyle=\mathsf{E}\Big[\int\_{[\sigma,\tau)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\mathsf{E}[1-\zeta^{\*}\_{\tau-}|\mathcal{F}^{1}\_{\tau}]J^{\Pi^{\*,1}\_{\tau}}(\eta,\sigma\_{\*}^{\tau}|\mathcal{F}^{1}\_{\tau})\Big|\mathcal{F}^{1}\_{\sigma}\Big], |  |

where in the final expression σ∗τ\sigma\_{\*}^{\tau} is generated by the truncated control ζ∗;τ\zeta^{\*;\tau} (cf. notation in Lemma [3.2](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")). Thanks to Lemma [3.2](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and since the family
{JΠτ∗,1​(η,σ∗τ|ℱτ1),η∈𝒯τ​(𝔽1)}\big\{J^{\Pi^{\*,1}\_{\tau}}(\eta,\sigma\_{\*}^{\tau}|\mathcal{F}^{1}\_{\tau}),\,\eta\in\mathcal{T}\_{\tau}(\mathbb{F}^{1})\big\}
is downward-directed (Corollary [3.3](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem3 "Corollary 3.3. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), we can take a sequence (ηn)⊂𝒯τ​(𝔽1)(\eta\_{n})\subset\mathcal{T}\_{\tau}(\mathbb{F}^{1})
such that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.15) |  | limn→∞JΠτ∗,1​(ηn,σ∗τ|ℱτ1)=V∗,1​(τ)\lim\_{n\to\infty}J^{\Pi^{\*,1}\_{\tau}}(\eta\_{n},\sigma\_{\*}^{\tau}|\mathcal{F}^{1}\_{\tau})=V^{\*,1}(\tau) |  |

and the limit is monotone from above. Equations (LABEL:eq:subm0) and ([3.14](https://arxiv.org/html/2510.15616v1#S3.E14 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) yield

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[1−ζσ−∗|ℱσ1]​V∗,1​(σ)\displaystyle\mathsf{E}[1-\zeta^{\*}\_{\sigma-}|\mathcal{F}^{1}\_{\sigma}]V^{\*,1}(\sigma) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝖤​[∫[σ,τ)gt​dζt∗+𝖤​[1−ζτ−∗|ℱτ1]​JΠτ∗,1​(ηn,σ∗τ|ℱτ1)|ℱσ1]\displaystyle\leq\mathsf{E}\Big[\int\_{[\sigma,\tau)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\mathsf{E}[1-\zeta^{\*}\_{\tau-}|\mathcal{F}^{1}\_{\tau}]\,J^{\Pi^{\*,1}\_{\tau}}(\eta\_{n},\sigma\_{\*}^{\tau}|\mathcal{F}^{1}\_{\tau})\Big|\mathcal{F}^{1}\_{\sigma}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | →n→∞𝖤​[∫[σ,τ)gt​dζt∗+𝖤​[1−ζτ−∗|ℱτ1]​V∗,1​(τ)|ℱσ1],\displaystyle\xrightarrow{n\to\infty}\mathsf{E}\Big[\int\_{[\sigma,\tau)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\mathsf{E}[1-\zeta^{\*}\_{\tau-}|\mathcal{F}^{1}\_{\tau}]\,V^{\*,1}(\tau)\Big|\mathcal{F}^{1}\_{\sigma}\Big], |  |

where the limit is by the monotone convergence theorem and ([3.15](https://arxiv.org/html/2510.15616v1#S3.E15 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")). Substituting into ([3.12](https://arxiv.org/html/2510.15616v1#S3.E12 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and adding M0​(σ)M^{0}(\sigma) on the event {σ=T}\{\sigma=T\} yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤​[M0​(σ)]\displaystyle\mathsf{E}[M^{0}(\sigma)] | =𝖤​[𝟏{σ<T}​M0​(σ)+𝟏{σ=T}​M0​(σ)]\displaystyle=\mathsf{E}[\mathbf{1}\_{\{\sigma<T\}}M^{0}(\sigma)+\mathbf{1}\_{\{\sigma=T\}}M^{0}(\sigma)] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝖤​[𝟏{σ<T}​(∫[0,τ)gt​dζt∗+𝖤​[1−ζτ−∗|ℱτ1]​V∗,1​(τ))+𝟏{σ=T}​M0​(σ)]\displaystyle\leq\mathsf{E}\Big[\mathbf{1}\_{\{\sigma<T\}}\Big(\int\_{[0,\tau)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\mathsf{E}[1-\zeta^{\*}\_{\tau-}|\mathcal{F}^{1}\_{\tau}]\,V^{\*,1}(\tau)\Big)+\mathbf{1}\_{\{\sigma=T\}}M^{0}(\sigma)\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖤​[𝟏{σ<T}​M0​(τ)+𝟏{σ=T}​M0​(τ)]=𝖤​[M0​(τ)],\displaystyle=\mathsf{E}\big[\mathbf{1}\_{\{\sigma<T\}}M^{0}(\tau)+\mathbf{1}\_{\{\sigma=T\}}M^{0}(\tau)\big]=\mathsf{E}[M^{0}(\tau)], |  |

where we used that {σ<T}∈ℱσ1\{\sigma<T\}\in\mathcal{F}^{1}\_{\sigma} combined with the tower property, and M0​(σ)=M0​(T)=M0​(τ)M^{0}(\sigma)=M^{0}(T)=M^{0}(\tau) on {σ=T}\{\sigma=T\}. This is the required inequality for the submartingale property of the family.

In order to show the right-continuity in expectation let us consider a sequence (τn)n∈ℕ⊂𝒯0​(𝔽1)(\tau\_{n})\_{n\in\mathbb{N}}\subset\mathcal{T}\_{0}(\mathbb{F}^{1}) such that τn↓τ∈𝒯0​(𝔽1)\tau\_{n}\downarrow\tau\in\mathcal{T}\_{0}(\mathbb{F}^{1}). Arguing as in (LABEL:eq:subm0) with τn\tau\_{n} in place of σ\sigma we have the first equality below. The second one follows by the monotone convergence theorem and Corollary [3.3](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem3 "Corollary 3.3. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") (cf. ([B.2](https://arxiv.org/html/2510.15616v1#A2.E2 "In Appendix B Upward and downward directed families ‣ Martingale theory for Dynkin games with asymmetric information"))):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.16) |  | 𝖤​[M0​(τn)]\displaystyle\mathsf{E}[M^{0}(\tau\_{n})] | =𝖤​[∫[0,τn)gt​dζt∗+ess​infη∈𝒯τn​(𝔽1)⁡𝖤​[fη​(1−ζη∗)+∫[τn,η)gt​dζt∗+hη​Δ​ζη∗|ℱτn1]]\displaystyle=\mathsf{E}\Big[\int\_{[0,\tau\_{n})}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\operatorname\*{ess\,inf}\_{\eta\in\mathcal{T}\_{\tau\_{n}}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\eta}(1-\zeta^{\*}\_{\eta})+\int\_{[\tau\_{n},\eta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\eta}\Delta\zeta^{\*}\_{\eta}\Big|\mathcal{F}^{1}\_{\tau\_{n}}\Big]\Big] |  |
|  |  | =infη∈𝒯τn​(𝔽1)𝖤​[fη​(1−ζη∗)+∫[0,η)gt​dζt∗+hη​Δ​ζη∗].\displaystyle=\inf\_{\eta\in\mathcal{T}\_{\tau\_{n}}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\eta}(1-\zeta^{\*}\_{\eta})+\int\_{[0,\eta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\eta}\Delta\zeta^{\*}\_{\eta}\Big]. |  |

We claim that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.17) |  | limn→∞infη∈𝒯τn​(𝔽1)𝖤​[fη​(1−ζη∗)+∫[0,η)gt​dζt∗+hη​Δ​ζη∗]=infη∈𝒯τ​(𝔽1)𝖤​[fη​(1−ζη∗)+∫[0,η)gt​dζt∗+hη​Δ​ζη∗].\displaystyle\begin{aligned} &\lim\_{n\to\infty}\inf\_{\eta\in\mathcal{T}\_{\tau\_{n}}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\eta}(1-\zeta^{\*}\_{\eta})+\int\_{[0,\eta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\eta}\Delta\zeta^{\*}\_{\eta}\Big]\\ &=\inf\_{\eta\in\mathcal{T}\_{\tau}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\eta}(1-\zeta^{\*}\_{\eta})+\int\_{[0,\eta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\eta}\Delta\zeta^{\*}\_{\eta}\Big].\end{aligned} |  |

Deferring for a moment the proof of ([3.17](https://arxiv.org/html/2510.15616v1#S3.E17 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), we observe that the latter and ([3.16](https://arxiv.org/html/2510.15616v1#S3.E16 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) yield

|  |  |  |
| --- | --- | --- |
|  | limn→∞𝖤​[M0​(τn)]=infη∈𝒯τ​(𝔽1)𝖤​[fη​(1−ζη∗)+∫[0,η)gt​dζt∗+hη​Δ​ζη∗]=𝖤​[M0​(τ)],\displaystyle\begin{aligned} \lim\_{n\to\infty}\mathsf{E}[M^{0}(\tau\_{n})]&=\inf\_{\eta\in\mathcal{T}\_{\tau}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\eta}(1-\zeta^{\*}\_{\eta})+\int\_{[0,\eta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\eta}\Delta\zeta^{\*}\_{\eta}\Big]=\mathsf{E}[M^{0}(\tau)],\end{aligned} |  |

where for the final equality we applied an analogue of ([3.16](https://arxiv.org/html/2510.15616v1#S3.E16 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) with τ\tau instead of τn\tau\_{n}. This
completes the proof of the right-continuity of M0M^{0} in expectation.

In order to prove ([3.17](https://arxiv.org/html/2510.15616v1#S3.E17 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) we first observe that the limit exists because 𝒯τn​(𝔽1)⊂𝒯τn+1​(𝔽1)\mathcal{T}\_{\tau\_{n}}(\mathbb{F}^{1})\subset\mathcal{T}\_{\tau\_{n+1}}(\mathbb{F}^{1}) and so the associated infima form a decreasing sequence. Moreover, 𝒯τn​(𝔽1)⊂𝒯τ​(𝔽1)\mathcal{T}\_{\tau\_{n}}(\mathbb{F}^{1})\subset\mathcal{T}\_{\tau}(\mathbb{F}^{1}) trivially implies that ([3.17](https://arxiv.org/html/2510.15616v1#S3.E17 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) holds with “≥\geq” instead of equality. It remains to show the opposite inequality. Let us fix θ∈𝒯τ​(𝔽1)\theta\in\mathcal{T}\_{\tau}(\mathbb{F}^{1}). Let θn=θ∨τn\theta\_{n}=\theta\vee\tau\_{n} for n∈ℕn\in\mathbb{N} and notice that

|  |  |  |
| --- | --- | --- |
|  | A={θn>θ,∀n∈ℕ}=⋂n≥1{θn>θ}=⋂n≥1{τn>θ}⊂{θ=τ},A=\{\theta\_{n}>\theta,\ \forall n\in\mathbb{N}\}=\bigcap\_{n\geq 1}\{\theta\_{n}>\theta\}=\bigcap\_{n\geq 1}\{\tau\_{n}>\theta\}\subset\{\theta=\tau\}, |  |

where the last inclusion is deduced from τn↓τ\tau\_{n}\downarrow\tau. On the set AcA^{c}, the sequence θn\theta\_{n} stabilises, i.e., θn=θ\theta\_{n}=\theta for all n>N​(ω)n>N(\omega) and some N​(ω)∈ℕN(\omega)\in\mathbb{N}. We will therefore argue differently on the set AA and on its complement AcA^{c}.

Since f≥hf\geq h (cf. Assumption [2.1](https://arxiv.org/html/2510.15616v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")),

|  |  |  |
| --- | --- | --- |
|  | fθn​(1−ζθn∗)+hθn​Δ​ζθn∗=fθn​(1−ζθn−∗)+(hθn−fθn)​Δ​ζθn∗≤fθn​(1−ζθn−∗).f\_{\theta\_{n}}(1-\zeta^{\*}\_{\theta\_{n}})+h\_{\theta\_{n}}\Delta\zeta^{\*}\_{\theta\_{n}}=f\_{\theta\_{n}}(1-\zeta^{\*}\_{\theta\_{n}-})+(h\_{\theta\_{n}}-f\_{\theta\_{n}})\Delta\zeta^{\*}\_{\theta\_{n}}\leq f\_{\theta\_{n}}(1-\zeta^{\*}\_{\theta\_{n}-}). |  |

Using this inequality we first write

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[fθn​(1−ζθn∗)+∫[τ,θn)gt​dζt∗+hθn​Δ​ζθn∗]\displaystyle\mathsf{E}\Big[f\_{\theta\_{n}}(1-\zeta^{\*}\_{\theta\_{n}})+\int\_{[\tau,\theta\_{n})}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\theta\_{n}}\Delta\zeta^{\*}\_{\theta\_{n}}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝖤​[1A​(fθn​(1−ζθn∗)+∫[τ,θn)gt​dζt∗+hθn​Δ​ζθn∗)+𝟏Ac​(fθn​(1−ζθn∗)+∫[τ,θn)gt​dζt∗+hθn​Δ​ζθn∗)]\displaystyle=\mathsf{E}\Big[1\_{A}\Big(f\_{\theta\_{n}}(1-\zeta^{\*}\_{\theta\_{n}})+\int\_{[\tau,\theta\_{n})}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\theta\_{n}}\Delta\zeta^{\*}\_{\theta\_{n}}\Big)+\mathbf{1}\_{A^{c}}\Big(f\_{\theta\_{n}}(1-\zeta^{\*}\_{\theta\_{n}})+\int\_{[\tau,\theta\_{n})}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\theta\_{n}}\Delta\zeta^{\*}\_{\theta\_{n}}\Big)\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝖤​[1A​(fθn​(1−ζθn−∗)+∫[τ,θn)gt​dζt∗)+𝟏Ac​(fθn​(1−ζθn∗)+∫[τ,θn)gt​dζt∗+hθn​Δ​ζθn∗)].\displaystyle\leq\mathsf{E}\Big[1\_{A}\Big(f\_{\theta\_{n}}(1-\zeta^{\*}\_{\theta\_{n}-})+\int\_{[\tau,\theta\_{n})}g\_{t}\mathrm{d}\zeta^{\*}\_{t}\Big)+\mathbf{1}\_{A^{c}}\Big(f\_{\theta\_{n}}(1-\zeta^{\*}\_{\theta\_{n}})+\int\_{[\tau,\theta\_{n})}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\theta\_{n}}\Delta\zeta^{\*}\_{\theta\_{n}}\Big)\Big]. |  |

Now, given that θn∈𝒯τn​(𝔽1)\theta\_{n}\in\mathcal{T}\_{\tau\_{n}}(\mathbb{F}^{1}) for all n∈ℕn\in\mathbb{N}, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (3.18) |  | limn→∞infη∈𝒯τn​(𝔽1)𝖤​[fη​(1−ζη∗)+∫[0,η)gt​dζt∗+hη​Δ​ζη∗]≤limn→∞𝖤​[𝟏A​(fθn​(1−ζθn−∗)+∫[σ,θn)gt​dζt∗)+𝟏Ac​(fθn​(1−ζθn∗)+∫[σ,θn)gt​dζt∗+hθn​Δ​ζθn∗)]=𝖤​[𝟏A​(fθ​(1−ζθ∗)+∫[σ,θ]gt​dζt∗)+𝟏Ac​(fθ​(1−ζθ∗)+∫[σ,θ)gt​dζt∗+hθ​Δ​ζθ∗)],\displaystyle\begin{aligned} &\lim\_{n\to\infty}\inf\_{\eta\in\mathcal{T}\_{\tau\_{n}}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\eta}(1-\zeta^{\*}\_{\eta})+\int\_{[0,\eta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\eta}\Delta\zeta^{\*}\_{\eta}\Big]\\ &\leq\lim\_{n\to\infty}\mathsf{E}\Big[\mathbf{1}\_{A}\Big(f\_{\theta\_{n}}(1\!-\!\zeta^{\*}\_{\theta\_{n}-})\!+\!\int\_{[\sigma,\theta\_{n})}\!g\_{t}\mathrm{d}\zeta^{\*}\_{t}\Big)\!+\!\mathbf{1}\_{A^{c}}\Big(f\_{\theta\_{n}}(1\!-\!\zeta^{\*}\_{\theta\_{n}})\!+\!\int\_{[\sigma,\theta\_{n})}\!g\_{t}\mathrm{d}\zeta^{\*}\_{t}\!+\!h\_{\theta\_{n}}\Delta\zeta^{\*}\_{\theta\_{n}}\Big)\Big]\\ &=\mathsf{E}\Big[\mathbf{1}\_{A}\Big(f\_{\theta}(1-\zeta^{\*}\_{\theta})+\int\_{[\sigma,\theta]}g\_{t}\mathrm{d}\zeta^{\*}\_{t}\Big)+\mathbf{1}\_{A^{c}}\Big(f\_{\theta}(1-\zeta^{\*}\_{\theta})+\int\_{[\sigma,\theta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\theta}\Delta\zeta^{\*}\_{\theta}\Big)\Big],\end{aligned} |  |

by the dominated convergence theorem and the fact that on AcA^{c} we have θn=θ\theta\_{n}=\theta for all sufficiently large n≥N​(ω)n\geq N(\omega). Next we use gθ≤hθg\_{\theta}\leq h\_{\theta} to write

|  |  |  |
| --- | --- | --- |
|  | 1A​∫[σ,θ]gt​dζt∗=1A​(∫[σ,θ)gt​dζt∗+gθ​Δ​ζθ∗)≤1A​(∫[σ,θ)gt​dζt∗+hθ​Δ​ζθ∗).1\_{A}\int\_{[\sigma,\theta]}g\_{t}\mathrm{d}\zeta^{\*}\_{t}=1\_{A}\Big(\int\_{[\sigma,\theta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+g\_{\theta}\Delta\zeta^{\*}\_{\theta}\Big)\leq 1\_{A}\Big(\int\_{[\sigma,\theta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\theta}\Delta\zeta^{\*}\_{\theta}\Big). |  |

Inserting this inequality into ([3.18](https://arxiv.org/html/2510.15616v1#S3.E18 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and recombining the indicator functions yield

|  |  |  |
| --- | --- | --- |
|  | limn→∞infη∈𝒯τn​(𝔽1)𝖤​[fη​(1−ζη∗)+∫[0,η)gt​dζt∗+hη​Δ​ζη∗]≤𝖤​[fθ​(1−ζθ∗)+∫[σ,θ)gt​dζt∗+hθ​Δ​ζθ∗].\displaystyle\lim\_{n\to\infty}\inf\_{\eta\in\mathcal{T}\_{\tau\_{n}}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\eta}(1-\zeta^{\*}\_{\eta})+\int\_{[0,\eta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\eta}\Delta\zeta^{\*}\_{\eta}\Big]\leq\mathsf{E}\Big[f\_{\theta}(1-\zeta^{\*}\_{\theta})+\int\_{[\sigma,\theta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\theta}\Delta\zeta^{\*}\_{\theta}\Big]. |  |

From the arbitrariness of θ∈𝒯τ​(𝔽1)\theta\in\mathcal{T}\_{\tau}(\mathbb{F}^{1}), we conclude that ([3.17](https://arxiv.org/html/2510.15616v1#S3.E17 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) holds.

Properties of 𝐍0{\bf N}^{0} are shown in an analogous way so we omit their proof.
It remains to invoke Proposition [A.2](https://arxiv.org/html/2510.15616v1#A1.Thmtheorem2 "Proposition A.2. ‣ Appendix A Review of aggregation results ‣ Martingale theory for Dynkin games with asymmetric information") to conclude that the families 𝐌0{\bf M}^{0} and 𝐍0{\bf N}^{0} can be aggregated into a càdlàg submartingale (Mt0,𝔽1,𝖯)t∈[0,T](M^{0}\_{t},\mathbb{F}^{1},\mathsf{P})\_{t\in[0,T]} and a càdlàg supermartingale (Nt0,𝔽2,𝖯)t∈[0,T](N^{0}\_{t},\mathbb{F}^{2},\mathsf{P})\_{t\in[0,T]}, respectively.
∎

We will later refine the above result by showing in Corollary [3.16](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem16 "Corollary 3.16. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") that the processes (Mt0)t∈[0,T](M^{0}\_{t})\_{t\in[0,T]} and (Nt0)t∈[0,T](N^{0}\_{t})\_{t\in[0,T]} are martingales up to the ‘last optimal stopping time’ for Player 1 and Player 2, respectively. Next, we aggregate the families 𝐌∗=𝐌ξ∗{\bf M}^{\*}={\bf M}^{\xi^{\*}} and 𝐍∗=𝐍ζ∗{\bf N}^{\*}={\bf N}^{\zeta^{\*}}.

###### Proposition 3.8.

The family 𝐌∗{\bf M}^{\*} is a 𝒯0​(𝔽1)\mathcal{T}\_{0}(\mathbb{F}^{1})-martingale system and the family 𝐍∗{\bf N}^{\*} is a 𝒯0​(𝔽2)\mathcal{T}\_{0}(\mathbb{F}^{2})-martingale system. Both are of class (D)(D). Hence, they can be uniquely aggregated into càdlàg martingales (Mt∗,𝔽1,𝖯)t∈[0,T](M^{\*}\_{t},\mathbb{F}^{1},\mathsf{P})\_{t\in[0,T]} and (Nt∗,𝔽2,𝖯)t∈[0,T](N^{\*}\_{t},\mathbb{F}^{2},\mathsf{P})\_{t\in[0,T]} (up to indistinguishability).

Moreover,
the *truncated controls* remain optimal at every time (prior to the end of the game) in the sense that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.19) |  |  | 𝟏Γθ1​V∗,1​(θ)=𝟏Γθ1​JΠθ∗,1​(ξ∗;θ,ζ∗;θ|ℱθ1),θ∈𝒯0​(𝔽1),\displaystyle\mathbf{1}\_{\Gamma^{1}\_{\theta}}V^{\*,1}(\theta)=\mathbf{1}\_{\Gamma^{1}\_{\theta}}J^{\Pi^{\*,1}\_{\theta}}(\xi^{\*;\theta},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta}),\quad\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}), |  |
|  |  | 𝟏Γγ2​V∗,2​(γ)=𝟏Γγ2​JΠγ∗,2​(ξ∗;γ,ζ∗;γ|ℱγ2),γ∈𝒯0​(𝔽2),\displaystyle\mathbf{1}\_{\Gamma^{2}\_{\gamma}}V^{\*,2}(\gamma)=\mathbf{1}\_{\Gamma^{2}\_{\gamma}}J^{\Pi^{\*,2}\_{\gamma}}(\xi^{\*;\gamma},\zeta^{\*;\gamma}|\mathcal{F}^{2}\_{\gamma}),\quad\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}), |  |

where

|  |  |  |
| --- | --- | --- |
|  | Γθ1={ω∈Ω:(1−ξθ−∗​(ω))​𝖤​[1−ζθ−∗|ℱθ1]​(ω)>0}∈ℱθ1,\displaystyle\Gamma^{1}\_{\theta}=\big\{\omega\in\Omega:(1-\xi^{\*}\_{\theta-}(\omega))\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}](\omega)>0\big\}\in\mathcal{F}^{1}\_{\theta}, |  |
|  |  |  |
| --- | --- | --- |
|  | Γγ2={ω∈Ω:(1−ζγ−∗​(ω))​𝖤​[1−ξγ−∗|ℱγ2]​(ω)>0}∈ℱγ2.\displaystyle\Gamma^{2}\_{\gamma}=\big\{\omega\in\Omega:(1-\zeta^{\*}\_{\gamma-}(\omega))\mathsf{E}[1-\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}](\omega)>0\big\}\in\mathcal{F}^{2}\_{\gamma}. |  |

###### Proof.

The fact that 𝐌∗{\bf M}^{\*} and 𝐍∗{\bf N}^{\*} are 𝒯0​(𝔽1)\mathcal{T}\_{0}(\mathbb{F}^{1})- and 𝒯0​(𝔽2)\mathcal{T}\_{0}(\mathbb{F}^{2})-systems and their integrability is argued as in the proof of Proposition [3.7](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem7 "Proposition 3.7. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). Next we show the martingale property. We only consider the question for 𝐌∗{\bf M}^{\*} as analogous arguments apply to 𝐍∗{\bf N}^{\*}.

In suffices to show that 𝖤​[M∗​(θ)]=𝖤​[M∗​(0)]\mathsf{E}[M^{\*}(\theta)]=\mathsf{E}[M^{\*}(0)] for any θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}) in order to establish the martingale property of 𝐌∗{\bf M}^{\*} (cf. Lemma [A.4](https://arxiv.org/html/2510.15616v1#A1.Thmtheorem4 "Lemma A.4. ‣ Appendix A Review of aggregation results ‣ Martingale theory for Dynkin games with asymmetric information")). Fix θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}) and define

|  |  |  |  |
| --- | --- | --- | --- |
| (3.20) |  | ξ~t≔ξt∗​𝟏[0,θ)​(t)+[ξθ−∗+(1−ξθ−∗)​ξt]​𝟏[θ,T]​(t)\displaystyle\tilde{\xi}\_{t}\coloneqq\xi^{\*}\_{t}\mathbf{1}\_{[0,\theta)}(t)+\big[\xi^{\*}\_{\theta-}+(1-\xi^{\*}\_{\theta-})\xi\_{t}\big]\mathbf{1}\_{[\theta,T]}(t) |  |

for some arbitrary ξ∈𝒜θ∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1}). Then it is easy to check that ξ~∈𝒜0∘​(𝔽1)\tilde{\xi}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1}).
From the definition of M∗M^{\*}, noticing that Π0∗,1=1\Pi^{\*,1}\_{0}=1, using tower property and sub-optimality of ξ~\tilde{\xi} we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.21) |  | 𝖤​[M∗​(0)]=𝖤​[V∗,1​(0)]≤𝖤​[∫[0,T)ft​(1−ζt∗)​dξ~t+∫[0,T)gt​(1−ξ~t)​dζt∗+∑t∈[0,T]ht​Δ​ζt∗​Δ​ξ~t]=𝖤​[∫[0,θ)ft​(1−ζt∗)​dξt∗+∫[0,θ)gt​(1−ξt∗)​dζt∗+∑t∈[0,θ)ht​Δ​ζt∗​Δ​ξt∗]+𝖤​[(1−ξθ−∗)​(∫[θ,T)ft​(1−ζt∗)​dξt+∫[θ,T)gt​(1−ξt)​dζt∗+∑t∈[θ,T]ht​Δ​ζt∗​Δ​ξt)].\displaystyle\begin{split}\mathsf{E}[M^{\*}(0)]&=\mathsf{E}[V^{\*,1}(0)]\\ &\leq\mathsf{E}\Big[\int\_{[0,T)}f\_{t}(1-\zeta^{\*}\_{t})\mathrm{d}\tilde{\xi}\_{t}+\int\_{[0,T)}g\_{t}(1-\tilde{\xi}\_{t})\mathrm{d}\zeta^{\*}\_{t}+\sum\_{t\in[0,T]}h\_{t}\Delta\zeta^{\*}\_{t}\Delta\tilde{\xi}\_{t}\Big]\\ &=\mathsf{E}\Big[\int\_{[0,\theta)}f\_{t}(1-\zeta^{\*}\_{t})\mathrm{d}\xi^{\*}\_{t}+\int\_{[0,\theta)}g\_{t}(1-\xi^{\*}\_{t})\mathrm{d}\zeta^{\*}\_{t}+\sum\_{t\in[0,\theta)}h\_{t}\Delta\zeta^{\*}\_{t}\Delta\xi^{\*}\_{t}\Big]\\ &\quad+\mathsf{E}\Big[(1-\xi^{\*}\_{\theta-})\Big(\int\_{[\theta,T)}f\_{t}(1-\zeta^{\*}\_{t})\mathrm{d}\xi\_{t}+\int\_{[\theta,T)}g\_{t}(1-\xi\_{t})\mathrm{d}\zeta^{\*}\_{t}+\sum\_{t\in[\theta,T]}h\_{t}\Delta\zeta^{\*}\_{t}\Delta\xi\_{t}\Big)\Big].\end{split} | |  |

Notice that the random variable inside the final expectation is different from zero only on the event {ξθ−∗∨ζθ−∗<1}\{\xi^{\*}\_{\theta-}\vee\zeta^{\*}\_{\theta-}<1\}.
Setting ζt∗;θ\zeta^{\*;\theta}\_{t} as in ([2.11](https://arxiv.org/html/2510.15616v1#S2.E11 "In Definition 2.8. ‣ 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) and recalling the convention 00=1\frac{0}{0}=1, we can write

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[(1−ξθ−∗)​(∫[θ,T)ft​(1−ζt∗)​dξt+∫[θ,T)gt​(1−ξt)​dζt∗+∑t∈[θ,T]ht​Δ​ζt∗​Δ​ξt)|ℱθ1]\displaystyle\mathsf{E}\Big[(1-\xi^{\*}\_{\theta-})\Big(\int\_{[\theta,T)}f\_{t}(1-\zeta^{\*}\_{t})\mathrm{d}\xi\_{t}+\int\_{[\theta,T)}g\_{t}(1-\xi\_{t})\mathrm{d}\zeta^{\*}\_{t}+\sum\_{t\in[\theta,T]}h\_{t}\Delta\zeta^{\*}\_{t}\Delta\xi\_{t}\Big)\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =(1−ξθ−∗)​𝖤​[(1−ζθ−∗)​(∫[θ,T)ft​(1−ζt∗;θ)​dξt+∫[θ,T)gt​(1−ξt)​dζt∗;θ+∑t∈[θ,T]ht​Δ​ζt∗;θ​Δ​ξt)|ℱθ1]\displaystyle=(1-\xi^{\*}\_{\theta-})\mathsf{E}\Big[(1-\zeta^{\*}\_{\theta-})\Big(\int\_{[\theta,T)}f\_{t}(1-\zeta^{\*;\theta}\_{t})\mathrm{d}\xi\_{t}+\int\_{[\theta,T)}g\_{t}(1-\xi\_{t})\mathrm{d}\zeta^{\*;\theta}\_{t}+\sum\_{t\in[\theta,T]}h\_{t}\Delta\zeta^{\*;\theta}\_{t}\Delta\xi\_{t}\Big)\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =(1−ξθ−∗)​𝖤​[1−ζθ−∗|ℱθ1]​JΠθ∗,1​(ξ,ζ∗;θ|ℱθ1).\displaystyle=(1-\xi^{\*}\_{\theta-})\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]J^{\Pi^{\*,1}\_{\theta}}(\xi,\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta}). |  |

Combining this with ([3.21](https://arxiv.org/html/2510.15616v1#S3.E21 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) yields for any ξ∈𝒜θ∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1})

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.22) |  | 𝖤​[M∗​(0)]\displaystyle\mathsf{E}[M^{\*}(0)] | ≤𝖤[∫[0,θ)ft(1−ζt∗)dξt∗+∫[0,θ)gt(1−ξt∗)dζt∗+∑t∈[0,θ)htΔζt∗Δξt∗\displaystyle\leq\mathsf{E}\Big[\int\_{[0,\theta)}f\_{t}(1-\zeta^{\*}\_{t})\mathrm{d}\xi^{\*}\_{t}+\int\_{[0,\theta)}g\_{t}(1-\xi^{\*}\_{t})\mathrm{d}\zeta^{\*}\_{t}+\sum\_{t\in[0,\theta)}h\_{t}\Delta\zeta^{\*}\_{t}\Delta\xi^{\*}\_{t} |  |
|  |  | +(1−ξθ−∗)𝖤[1−ζθ−∗|ℱθ1]JΠθ∗,1(ξ,ζ∗;θ|ℱθ1)].\displaystyle\qquad+(1-\xi^{\*}\_{\theta-})\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]\,J^{\Pi^{\*,1}\_{\theta}}(\xi,\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})\Big]. |  |

Thanks to Lemma [3.1](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem1 "Lemma 3.1. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") we can select a sequence (ξn)⊂𝒜θ∘​(𝔽1)(\xi^{n})\subset\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1}) such that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.23) |  | V∗,1​(θ)=limn→∞JΠθ∗,1​(ξn,ζ∗;θ|ℱθ1),\displaystyle V^{\*,1}(\theta)=\lim\_{n\to\infty}J^{\Pi^{\*,1}\_{\theta}}(\xi^{n},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta}), |  |

where the limit is monotone from above. We write the inequality ([3.22](https://arxiv.org/html/2510.15616v1#S3.E22 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) with ξ=ξn\xi=\xi^{n} and let n→∞n\to\infty. Invoking the monotone convergence theorem, we arrive at

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.24) |  | 𝖤​[M∗​(0)]\displaystyle\mathsf{E}[M^{\*}(0)] | ≤𝖤​[∫[0,θ)ft​(1−ζt∗)​dξt∗+∫[0,θ)gt​(1−ξt∗)​dζt∗+∑t∈[0,θ)ht​Δ​ζt∗​Δ​ξt∗]\displaystyle\leq\mathsf{E}\Big[\int\_{[0,\theta)}f\_{t}(1-\zeta^{\*}\_{t})\mathrm{d}\xi^{\*}\_{t}+\int\_{[0,\theta)}g\_{t}(1-\xi^{\*}\_{t})\mathrm{d}\zeta^{\*}\_{t}+\sum\_{t\in[0,\theta)}h\_{t}\Delta\zeta^{\*}\_{t}\Delta\xi^{\*}\_{t}\Big] |  |
|  |  | +limn→∞𝖤​[(1−ξθ−∗)​𝖤​[1−ζθ−∗|ℱθ1]​JΠθ∗,1​(ξn,ζ∗;θ|ℱθ1)]\displaystyle\quad+\lim\_{n\to\infty}\mathsf{E}\Big[(1-\xi^{\*}\_{\theta-})\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]J^{\Pi^{\*,1}\_{\theta}}(\xi^{n},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})\Big] |  |
|  |  | =𝖤​[∫[0,θ)ft​(1−ζt∗)​dξt∗+∫[0,θ)gt​(1−ξt∗)​dζt∗+∑t∈[0,θ)ht​Δ​ζt∗​Δ​ξt∗]\displaystyle=\mathsf{E}\Big[\int\_{[0,\theta)}f\_{t}(1-\zeta^{\*}\_{t})\mathrm{d}\xi^{\*}\_{t}+\int\_{[0,\theta)}g\_{t}(1-\xi^{\*}\_{t})\mathrm{d}\zeta^{\*}\_{t}+\sum\_{t\in[0,\theta)}h\_{t}\Delta\zeta^{\*}\_{t}\Delta\xi^{\*}\_{t}\Big] |  |
|  |  | +𝖤​[(1−ξθ−∗)​𝖤​[1−ζθ−∗|ℱθ1]​V∗,1​(θ)]=𝖤​[M∗​(θ)].\displaystyle\quad+\mathsf{E}\Big[(1-\xi^{\*}\_{\theta-})\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]V^{\*,1}(\theta)\Big]=\mathsf{E}[M^{\*}(\theta)]. |  |

The inequality in ([3.21](https://arxiv.org/html/2510.15616v1#S3.E21 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) becomes an equality if we replace ξ~\tilde{\xi} with ξ∗\xi^{\*}. So ([3.22](https://arxiv.org/html/2510.15616v1#S3.E22 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) becomes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.25) |  | 𝖤​[M∗​(0)]=𝖤[∫[0,θ)ft(1−ζt∗)dξt∗+∫[0,θ)gt(1−ξt∗)dζt∗+∑t∈[0,θ)htΔζt∗Δξt∗+(1−ξθ−∗)𝖤[1−ζθ−∗|ℱθ1]JΠθ∗,1(ξ∗;θ,ζ∗;θ|ℱθ1)]≥𝖤[M∗(θ)],\displaystyle\begin{split}\mathsf{E}[M^{\*}(0)]&=\mathsf{E}\Big[\int\_{[0,\theta)}f\_{t}(1-\zeta^{\*}\_{t})\mathrm{d}\xi^{\*}\_{t}+\int\_{[0,\theta)}g\_{t}(1-\xi^{\*}\_{t})\mathrm{d}\zeta^{\*}\_{t}+\sum\_{t\in[0,\theta)}h\_{t}\Delta\zeta^{\*}\_{t}\Delta\xi^{\*}\_{t}\\ &\qquad+(1-\xi^{\*}\_{\theta-})\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]J^{\Pi^{\*,1}\_{\theta}}(\xi^{\*;\theta},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})\Big]\geq\mathsf{E}[M^{\*}(\theta)],\end{split} | |  |

where the inequality is due to the fact that a priori the truncated control ξ∗;θ∈𝒜θ∘​(𝔽1)\xi^{\*;\theta}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1}) may not be optimal for JΠθ∗,1​(⋅,ζ∗;θ|ℱθ1)J^{\Pi^{\*,1}\_{\theta}}(\cdot,\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta}).

Combining ([3.24](https://arxiv.org/html/2510.15616v1#S3.E24 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and ([3.25](https://arxiv.org/html/2510.15616v1#S3.E25 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) yields the desired result, i.e., 𝐌∗{\bf M}^{\*} is a martingale system. By Corollary [A.3](https://arxiv.org/html/2510.15616v1#A1.Thmtheorem3 "Corollary A.3. ‣ Appendix A Review of aggregation results ‣ Martingale theory for Dynkin games with asymmetric information"), it can be uniquely aggregated into a càdlàg martingale (Mt∗,𝔽1,𝖯)t∈[0,T](M^{\*}\_{t},\mathbb{F}^{1},\mathsf{P})\_{t\in[0,T]} (up to indistinguishability).
The inequalities ([3.24](https://arxiv.org/html/2510.15616v1#S3.E24 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and ([3.25](https://arxiv.org/html/2510.15616v1#S3.E25 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) also show that

|  |  |  |
| --- | --- | --- |
|  | (1−ξθ−∗)​𝖤​[1−ζθ−∗|ℱθ1]​V∗,1​(θ)=(1−ξθ−∗)​𝖤​[1−ζθ−∗|ℱθ1]​JΠθ∗,1​(ξ∗;θ,ζ∗;θ|ℱθ1),(1-\xi^{\*}\_{\theta-})\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]V^{\*,1}(\theta)=(1-\xi^{\*}\_{\theta-})\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]J^{\Pi^{\*,1}\_{\theta}}\big(\xi^{\*;\theta},\zeta^{\*;\theta}\big|\mathcal{F}^{1}\_{\theta}\big), |  |

from which we deduce ([3.19](https://arxiv.org/html/2510.15616v1#S3.E19 "In Proposition 3.8. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and the optimality of the truncated strategy ξ∗;θ\xi^{\*;\theta}.
∎

### 3.3. Proof of Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and some further results

Thanks to Proposition [3.7](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem7 "Proposition 3.7. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") we are able to obtain an aggregation of the systems of equilibrium values into optional processes. Moreover, we compute the right and left limits of such optional processes, thus providing also a formula for their jumps.

###### Proof of Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

We prove all the claims for V^t∗,1\hat{V}^{\*,1}\_{t} as the ones for V^t∗,2\hat{V}^{\*,2}\_{t} follow by analogous arguments.
By the definition of the submartingale (Mt0)t∈[0,T](M^{0}\_{t})\_{t\in[0,T]} obtained in Proposition [3.7](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem7 "Proposition 3.7. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") we have, for any τ∈𝒯0​(𝔽1)\tau\in\mathcal{T}\_{0}(\mathbb{F}^{1}),

|  |  |  |  |
| --- | --- | --- | --- |
| (3.26) |  | 𝖤​[1−ζτ−∗|ℱτ1]​V∗,1​(τ)=Mτ0−𝖤​[∫[0,τ)gs​dζs∗|ℱτ1]=Mτ0−Sτ1,\displaystyle\mathsf{E}[1-\zeta^{\*}\_{\tau-}|\mathcal{F}^{1}\_{\tau}]V^{\*,1}(\tau)=M^{0}\_{\tau}-\mathsf{E}\Big[\int\_{[0,\tau)}g\_{s}\mathrm{d}\zeta^{\*}\_{s}\Big|\mathcal{F}^{1}\_{\tau}\Big]=M^{0}\_{\tau}-S^{1}\_{\tau}, |  |

where
(St1)t∈[0,T](S^{1}\_{t})\_{t\in[0,T]} is the 𝔽1\mathbb{F}^{1}-optional projection of (∫[0,t)gs​dζs∗)t∈[0,T]\big(\int\_{[0,t)}g\_{s}\mathrm{d}\zeta^{\*}\_{s}\big)\_{t\in[0,T]}. This shows that 𝐕∗,1{\bf V}^{\*,1} is aggregated into an optional process V^∗,1≔M0−S1\hat{V}^{\*,1}\coloneqq M^{0}-S^{1}. The process S1S^{1} is the 𝔽1\mathbb{F}^{1}-optional projection of a bounded variation process, hence a difference of two submartingales and, in particular, a semi-martingale. Therefore, V^∗,1\hat{V}^{\*,1} is also a semi-martingale, as claimed. The explicit expression ([3.4](https://arxiv.org/html/2510.15616v1#S3.E4 "In Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) for V^∗,1\hat{V}^{\*,1} is easily deduced from the one for V∗,1​(θ)V^{\*,1}(\theta) in ([2.13](https://arxiv.org/html/2510.15616v1#S2.E13 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")), upon noticing that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.27) |  | 𝖤​[1−ζθ−∗|ℱθ1]​JΠθ∗,1​(ξ,ζ∗;θ|ℱθ1)=𝖤​[fτ​(1−ζτ∗)+∫[θ,τ)gu​dζu∗+hτ​Δ​ζτ∗|ℱθ1],\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]J^{\Pi^{\*,1}\_{\theta}}(\xi,\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})=\mathsf{E}\Big[f\_{\tau}(1-\zeta^{\*}\_{\tau})+\int\_{[\theta,\tau)}g\_{u}\mathrm{d}\zeta^{\*}\_{u}+h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta}\Big], |  |

for τ∈𝒯θR​(𝔽1)\tau\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1}) generated by ξ∈𝒜θ∘​(𝔽1)\xi\in\mathcal{A}^{\circ}\_{\theta}(\mathbb{F}^{1}), and then applying Lemma [3.2](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") to restrict the optimisation to stopping times τ∈𝒯θ​(𝔽1)\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1}) (cf. (LABEL:eq:subm0) for the same argument). The class (D)(D) property easily follows because f,g,h∈ℒb​(𝖯)f,g,h\in\mathcal{L}\_{b}(\mathsf{P}).

The process M0M^{0} has càdlàg paths. Moreover, there is a set Ω∗∈ℱ\Omega\_{\*}\in\mathcal{F} of probability one such that for all ω∈Ω∗\omega\in\Omega\_{\*} the process t↦St1​(ω)t\mapsto S^{1}\_{t}(\omega) has right and left limits at all t∈(0,T)t\in(0,T), thanks to [[KS98a](https://arxiv.org/html/2510.15616v1#bib.bibx32), Prop. I.3.14], because S1S^{1} is a difference of two submartingales. Then, outside of a universal null set, all paths of the process V^∗,1\hat{V}^{\*,1} have right and left limits V^t+∗,1\hat{V}^{\*,1}\_{t+} and V^t−∗,1\hat{V}^{\*,1}\_{t-} at all points t∈(0,T)t\in(0,T).
Moreover, we notice that by the right continuity of the filtration, the process (V^t+∗,1)t∈[0,T)(\hat{V}^{\*,1}\_{t+})\_{t\in[0,T)} is 𝔽1\mathbb{F}^{1}-adapted.

Fix θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}), θ<T\theta<T. From ([3.4](https://arxiv.org/html/2510.15616v1#S3.E4 "In Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) with θ\theta therein replaced by θn∈𝒯0​(𝔽1)\theta\_{n}\in\mathcal{T}\_{0}(\mathbb{F}^{1}), θn>θ\theta\_{n}>\theta, we get

|  |  |  |  |
| --- | --- | --- | --- |
| (3.28) |  | V^θn∗,1=ess​infτ∈𝒯θn​(𝔽1)⁡𝖤​[fτ​(1−ζτ∗)+∫[θn,τ)gu​dζu∗+hτ​Δ​ζτ∗|ℱθn1].\hat{V}^{\*,1}\_{\theta\_{n}}=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta\_{n}}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\tau}(1-\zeta^{\*}\_{\tau})+\int\_{[\theta\_{n},\tau)}g\_{u}\mathrm{d}\zeta^{\*}\_{u}+h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big]. |  |

We apply monotone convergence and Corollary [3.3](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem3 "Corollary 3.3. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") to the above equality to obtain (cf. ([B.2](https://arxiv.org/html/2510.15616v1#A2.E2 "In Appendix B Upward and downward directed families ‣ Martingale theory for Dynkin games with asymmetric information")))

|  |  |  |  |
| --- | --- | --- | --- |
| (3.29) |  | 𝖤​[V^θn∗,1|ℱθ1]=ess​infτ∈𝒯θn​(𝔽1)⁡𝖤​[fτ​(1−ζτ∗)+∫[θn,τ)gu​dζu∗+hτ​Δ​ζτ∗|ℱθ1].\mathsf{E}[\hat{V}^{\*,1}\_{\theta\_{n}}|\mathcal{F}^{1}\_{\theta}]=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta\_{n}}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\tau}(1-\zeta^{\*}\_{\tau})+\int\_{[\theta\_{n},\tau)}g\_{u}\mathrm{d}\zeta^{\*}\_{u}+h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta}\Big]. |  |

Then,

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[V^θn∗,1|ℱθ1]≥ess​infτ∈𝒯>θ​(𝔽1)⁡𝖤​[fτ​(1−ζτ∗)+∫[θn,τ)gu​dζu∗+hτ​Δ​ζτ∗|ℱθ1],\mathsf{E}[\hat{V}^{\*,1}\_{\theta\_{n}}|\mathcal{F}^{1}\_{\theta}]\geq\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{>\theta}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\tau}(1-\zeta^{\*}\_{\tau})+\int\_{[\theta\_{n},\tau)}g\_{u}\mathrm{d}\zeta^{\*}\_{u}+h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta}\Big], |  |

where 𝒯>θ​(𝔽1)≔{τ∈𝒯θ​(𝔽1):𝖯​(τ>θ)=1}\mathcal{T}\_{>\theta}(\mathbb{F}^{1})\coloneqq\{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1}):\mathsf{P}(\tau>\theta)=1\}. We let θn↓θ\theta\_{n}\downarrow\theta as n→∞n\to\infty (i.e., θn→θ\theta\_{n}\to\theta, θn>θ\theta\_{n}>\theta). Taking limits in the expression above yields

|  |  |  |  |
| --- | --- | --- | --- |
| (3.30) |  | V^θ+∗,1=𝖤​[V^θ+∗,1|ℱθ1]=limn→∞𝖤​[V^θn∗,1|ℱθ1]≥ess​infτ∈𝒯>θ​(𝔽1)⁡𝖤​[fτ​(1−ζτ∗)+∫(θ,τ)gu​dζu∗+hτ​Δ​ζτ∗|ℱθ1],\displaystyle\begin{aligned} &\hat{V}^{\*,1}\_{\theta+}=\mathsf{E}[\hat{V}^{\*,1}\_{\theta+}|\mathcal{F}^{1}\_{\theta}]=\lim\_{n\to\infty}\mathsf{E}[\hat{V}^{\*,1}\_{\theta\_{n}}|\mathcal{F}^{1}\_{\theta}]\\ &\geq\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{>\theta}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\tau}(1-\zeta^{\*}\_{\tau})+\int\_{(\theta,\tau)}g\_{u}\mathrm{d}\zeta^{\*}\_{u}+h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta}\Big],\end{aligned} |  |

where we refer to the right continuity of the filtration 𝔽1\mathbb{F}^{1} to justify the first equality, to the dominated convergence theorem for the second equality and, for the convergence of the right-hand side, to

|  |  |  |  |
| --- | --- | --- | --- |
| (3.31) |  | 0≤𝖤​[∫(θ,θn)|gu|​dζu∗]≤𝖤​[(ζθn−∗−ζθ∗)​supu∈[0,T]|gu|]→0,0\leq\mathsf{E}\Big[\int\_{(\theta,\theta\_{n})}|g\_{u}|\mathrm{d}\zeta^{\*}\_{u}\Big]\leq\mathsf{E}\big[(\zeta^{\*}\_{\theta\_{n}-}-\zeta^{\*}\_{\theta})\sup\_{u\in[0,T]}|g\_{u}|\big]\to 0, |  |

which holds by the dominated convergence as θn↓θ\theta\_{n}\downarrow\theta.

For the opposite inequality, we fix τ∈𝒯>θ​(𝔽1)\tau\in\mathcal{T}\_{>\theta}(\mathbb{F}^{1}), θn∈(θ,T)\theta\_{n}\in(\theta,T) and notice that τ∨θn∈𝒯θn​(𝔽1)\tau\vee\theta\_{n}\in\mathcal{T}\_{\theta\_{n}}(\mathbb{F}^{1}). It then follows from ([3.29](https://arxiv.org/html/2510.15616v1#S3.E29 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) that

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[V^θn∗,1|ℱθ1]≤𝖤​[fτ∨θn​(1−ζτ∨θn∗)+∫[θn,τ∨θn)gu​dζu∗+hτ∨θn​Δ​ζτ∨θn∗|ℱθ1].\mathsf{E}[\hat{V}^{\*,1}\_{\theta\_{n}}|\mathcal{F}^{1}\_{\theta}]\leq\mathsf{E}\Big[f\_{\tau\vee\theta\_{n}}(1-\zeta^{\*}\_{\tau\vee\theta\_{n}})+\int\_{[\theta\_{n},\tau\vee\theta\_{n})}g\_{u}\mathrm{d}\zeta^{\*}\_{u}+h\_{\tau\vee\theta\_{n}}\Delta\zeta^{\*}\_{\tau\vee\theta\_{n}}\Big|\mathcal{F}^{1}\_{\theta}\Big]. |  |

Letting θn↓θ\theta\_{n}\downarrow\theta as n→∞n\to\infty, we observe that [θn,τ∨θn)→(θ,τ)[\theta\_{n},\tau\vee\theta\_{n})\to(\theta,\tau), because τ>θ\tau>\theta, and likewise

|  |  |  |
| --- | --- | --- |
|  | limn→∞(fτ∨θn​(1−ζτ∨θn∗)+∫[θn,τ∨θn)gu​dζu∗+hτ∨θn​Δ​ζτ∨θn∗)=fτ​(1−ζτ∗)+∫(θ,τ)gu​dζu∗+hτ​Δ​ζτ∗.\displaystyle\lim\_{n\to\infty}\Big(f\_{\tau\vee\theta\_{n}}(1\!-\!\zeta^{\*}\_{\tau\vee\theta\_{n}})\!+\!\int\_{[\theta\_{n},\tau\vee\theta\_{n})}\!\!g\_{u}\mathrm{d}\zeta^{\*}\_{u}\!+\!h\_{\tau\vee\theta\_{n}}\Delta\zeta^{\*}\_{\tau\vee\theta\_{n}}\Big)\!=\!f\_{\tau}(1\!-\!\zeta^{\*}\_{\tau})\!+\!\int\_{(\theta,\tau)}\!\!g\_{u}\mathrm{d}\zeta^{\*}\_{u}\!+\!h\_{\tau}\Delta\zeta^{\*}\_{\tau}. |  |

Therefore, the dominated convergence theorem yields (cf. ([3.31](https://arxiv.org/html/2510.15616v1#S3.E31 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) for a similar argument)

|  |  |  |
| --- | --- | --- |
|  | V^θ+∗,1≤𝖤​[fτ​(1−ζτ∗)+∫(θ,τ)gu​dζu∗+hτ​Δ​ζτ∗|ℱθ1].\hat{V}^{\*,1}\_{\theta+}\leq\mathsf{E}\Big[f\_{\tau}(1-\zeta^{\*}\_{\tau})+\int\_{(\theta,\tau)}g\_{u}\mathrm{d}\zeta^{\*}\_{u}+h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta}\Big]. |  |

Thus, combining this with ([3.30](https://arxiv.org/html/2510.15616v1#S3.E30 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"))
we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^θ+∗,1\displaystyle\hat{V}^{\*,1}\_{\theta+} | =ess​infτ∈𝒯>θ​(𝔽1)⁡𝖤​[fτ​(1−ζτ∗)+∫(θ,τ)gu​dζu∗+hτ​Δ​ζτ∗|ℱθ1]\displaystyle=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{>\theta}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\tau}(1-\zeta^{\*}\_{\tau})+\int\_{(\theta,\tau)}g\_{u}\mathrm{d}\zeta^{\*}\_{u}+h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ess​infτ∈𝒯>θ​(𝔽1)⁡𝖤​[fτ​(1−ζτ∗)+∫[θ,τ)gu​dζu∗+hτ​Δ​ζτ∗|ℱθ1]−𝖤​[gθ​Δ​ζθ∗|ℱθ1].\displaystyle=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{>\theta}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\tau}(1-\zeta^{\*}\_{\tau})+\int\_{[\theta,\tau)}g\_{u}\mathrm{d}\zeta^{\*}\_{u}+h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta}\Big]-\mathsf{E}\big[g\_{\theta}\Delta\zeta^{\*}\_{\theta}\big|\mathcal{F}^{1}\_{\theta}\big]. |  |

To prove ([3.5](https://arxiv.org/html/2510.15616v1#S3.E5 "In Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) it remains to show that, although 𝒯>θ​(𝔽1)⊊𝒯θ​(𝔽1)\mathcal{T}\_{>\theta}(\mathbb{F}^{1})\subsetneq\mathcal{T}\_{\theta}(\mathbb{F}^{1}), it still holds

|  |  |  |  |
| --- | --- | --- | --- |
| (3.32) |  | V^θ∗,1=ess​infτ∈𝒯>θ​(𝔽1)⁡𝖤​[fτ​(1−ζτ∗)+∫[θ,τ)gu​dζu∗+hτ​Δ​ζτ∗|ℱθ1].\displaystyle\hat{V}^{\*,1}\_{\theta}=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{>\theta}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\tau}(1-\zeta^{\*}\_{\tau})+\int\_{[\theta,\tau)}g\_{u}\mathrm{d}\zeta^{\*}\_{u}+h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta}\Big]. |  |

First, we notice that for any η∈𝒯θ​(𝔽1)\eta\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[fη​(1−ζη∗)+∫[θ,η)gt​dζt∗+hη​Δ​ζη∗|ℱθ1]\displaystyle\mathsf{E}\Big[f\_{\eta}(1-\zeta^{\*}\_{\eta})+\int\_{[\theta,\eta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\eta}\Delta\zeta^{\*}\_{\eta}\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝟏{η=θ}​𝖤​[fθ​(1−ζθ∗)+hθ​Δ​ζθ∗|ℱθ1]+𝟏{η>θ}​𝖤​[fη​(1−ζη∗)+∫[θ,η)gt​dζt∗+hη​Δ​ζη∗|ℱθ1]\displaystyle=\mathbf{1}\_{\{\eta=\theta\}}\mathsf{E}\Big[f\_{\theta}(1-\zeta^{\*}\_{\theta})+h\_{\theta}\Delta\zeta^{\*}\_{\theta}\Big|\mathcal{F}^{1}\_{\theta}\Big]+\mathbf{1}\_{\{\eta>\theta\}}\mathsf{E}\Big[f\_{\eta}(1-\zeta^{\*}\_{\eta})+\int\_{[\theta,\eta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\eta}\Delta\zeta^{\*}\_{\eta}\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≥𝟏{η=θ}​𝖤​[fθ​(1−ζθ∗)+hθ​Δ​ζθ∗|ℱθ1]\displaystyle\geq\mathbf{1}\_{\{\eta=\theta\}}\mathsf{E}\Big[f\_{\theta}(1-\zeta^{\*}\_{\theta})+h\_{\theta}\Delta\zeta^{\*}\_{\theta}\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | +𝟏{η>θ}​ess​infτ∈𝒯>θ​(ℱt1)⁡𝖤​[fτ​(1−ζτ∗)+∫[θ,τ)gt​dζt∗+hτ​Δ​ζτ∗|ℱθ1].\displaystyle\quad+\mathbf{1}\_{\{\eta>\theta\}}\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{>\theta}(\mathcal{F}^{1}\_{t})}\mathsf{E}\Big[f\_{\tau}(1-\zeta^{\*}\_{\tau})+\int\_{[\theta,\tau)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta}\Big]. |  |

It then follows that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.33) |  | ess​infη∈𝒯θ​(𝔽1)⁡𝖤​[fη​(1−ζη∗)+∫[θ,η)gt​dζt∗+hη​Δ​ζη∗|ℱθ1]=𝖤​[fθ​(1−ζθ∗)+hθ​Δ​ζθ∗|ℱθ1]∧ess​infτ∈𝒯>θ​(𝔽1)⁡𝖤​[fτ​(1−ζτ∗)+∫[θ,τ)gt​dζt∗+hτ​Δ​ζτ∗|ℱθ1].\displaystyle\begin{aligned} &\operatorname\*{ess\,inf}\_{\eta\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\eta}(1-\zeta^{\*}\_{\eta})+\int\_{[\theta,\eta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\eta}\Delta\zeta^{\*}\_{\eta}\Big|\mathcal{F}^{1}\_{\theta}\Big]\\ &=\mathsf{E}[f\_{\theta}(1-\zeta^{\*}\_{\theta})+h\_{\theta}\Delta\zeta^{\*}\_{\theta}|\mathcal{F}^{1}\_{\theta}]\wedge\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{>{\theta}}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\tau}(1-\zeta^{\*}\_{\tau})+\int\_{[\theta,\tau)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta}\Big].\end{aligned} |  |

Take a sequence (τn)n∈ℕ⊂𝒯>θ​(𝔽1)(\tau\_{n})\_{n\in\mathbb{N}}\subset\mathcal{T}\_{>\theta}(\mathbb{F}^{1}) such that τn↓θ\tau\_{n}\downarrow\theta (i.e., τn>θ\tau\_{n}>\theta for all n∈ℕn\in\mathbb{N}). We have

|  |  |  |
| --- | --- | --- |
|  | ess​infτ∈𝒯>θ​(𝔽1)⁡𝖤​[fτ​(1−ζτ∗)+∫[θ,τ)gt​dζt∗+hτ​Δ​ζτ∗|ℱθ1]\displaystyle\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{>\theta}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\tau}(1-\zeta^{\*}\_{\tau})+\int\_{[\theta,\tau)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =ess​infτ∈𝒯>θ​(𝔽1)⁡𝖤​[fτ​(1−ζτ−∗)+∫[θ,τ)gt​dζt∗+(hτ−fτ)​Δ​ζτ∗|ℱθ1]\displaystyle=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{>\theta}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\tau}(1-\zeta^{\*}\_{\tau-})+\int\_{[\theta,\tau)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+(h\_{\tau}-f\_{\tau})\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤limn→∞𝖤​[fτn​(1−ζτn−∗)+∫[θ,τn)gt​dζt∗|ℱθ1]=𝖤​[fθ​(1−ζθ∗)+gθ​Δ​ζθ∗|ℱθ1]\displaystyle\leq\lim\_{n\to\infty}\mathsf{E}\Big[f\_{\tau\_{n}}(1-\zeta^{\*}\_{\tau\_{n}-})+\int\_{[\theta,\tau\_{n})}g\_{t}\mathrm{d}\zeta^{\*}\_{t}\Big|\mathcal{F}^{1}\_{\theta}\Big]=\mathsf{E}\Big[f\_{\theta}(1-\zeta^{\*}\_{\theta})+g\_{\theta}\Delta\zeta^{\*}\_{\theta}\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝖤​[fθ​(1−ζθ∗)+hθ​Δ​ζθ∗|ℱθ1],\displaystyle\leq\mathsf{E}[f\_{\theta}(1-\zeta^{\*}\_{\theta})+h\_{\theta}\Delta\zeta^{\*}\_{\theta}|\mathcal{F}^{1}\_{\theta}], |  |

where we used
f≥h≥gf\geq h\geq g in both inequalities, and we passed the limit inside the expectation by the dominated convergence theorem. Combining the above inequality and ([3.33](https://arxiv.org/html/2510.15616v1#S3.E33 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) yields ([3.32](https://arxiv.org/html/2510.15616v1#S3.E32 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) as needed.
Then, the first equation in ([3.5](https://arxiv.org/html/2510.15616v1#S3.E5 "In Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) holds. Analogous arguments prove the aggregation for the family 𝐕∗,2{\bf V}^{\*,2} and the second equation in ([3.5](https://arxiv.org/html/2510.15616v1#S3.E5 "In Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")).

We proceed now with the left-limit. For τ∈𝒯θR​(𝔽1)\tau\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1}) and any υ∈𝒯0R​(𝔽1)\upsilon\in\mathcal{T}^{R}\_{0}(\mathbb{F}^{1}) with υ≤τ\upsilon\leq\tau, denote

|  |  |  |
| --- | --- | --- |
|  | 𝒫υ​(τ,ζ∗)≔fτ​(1−ζτ∗)+∫[υ,τ)gt​dζt∗+hτ​Δ​ζτ∗\mathcal{P}\_{\upsilon}(\tau,\zeta^{\*})\coloneqq f\_{\tau}(1-\zeta^{\*}\_{\tau})+\int\_{[\upsilon,\tau)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\tau}\Delta\zeta^{\*}\_{\tau} |  |

and notice that, by the definition of Π^θ∗,1\widehat{\Pi}^{\*,1}\_{\theta} in ([2.6](https://arxiv.org/html/2510.15616v1#S2.E6 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.34) |  |  | 𝖤​[1−ζθ−∗|ℱθ−1]​JΠ^θ∗,1​(ξ,ζ∗;θ|ℱθ−1)=𝖤​[𝒫θ​(τ,ζ∗)|ℱθ−1],\displaystyle\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta-}]J^{\widehat{\Pi}^{\*,1}\_{\theta}}\big(\xi,\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta-})=\mathsf{E}[\mathcal{P}\_{\theta}(\tau,\zeta^{\*})|\mathcal{F}^{1}\_{\theta-}], |  |
|  |  | 𝖤​[1−ζθ−∗|ℱθ−1]​JΠ^θ∗,1​(ξ,ζ∗;θ|ℱθ1)=𝖤​[𝒫θ​(τ,ζ∗)|ℱθ1],\displaystyle\mathsf{E}[1-\zeta^{\*}\_{\theta-}|\mathcal{F}^{1}\_{\theta-}]J^{\widehat{\Pi}^{\*,1}\_{\theta}}\big(\xi,\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})=\mathsf{E}[\mathcal{P}\_{\theta}(\tau,\zeta^{\*})|\mathcal{F}^{1}\_{\theta}], |  |

where τ\tau is the randomised stopping time generated by ξ∈𝒜θ∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1}). Let (τk)k∈ℕ⊂𝒯θ​(𝔽1)(\tau\_{k})\_{k\in\mathbb{N}}\subset\mathcal{T}\_{\theta}(\mathbb{F}^{1}) be a minimising sequence limk→∞𝖤​[𝒫θ​(τk,ζ∗)|ℱθ1]=ess​infτ∈𝒯θ​(𝔽1)⁡𝖤​[𝒫θ​(τ,ζ∗)|ℱθ1]\lim\_{k\to\infty}\mathsf{E}[\mathcal{P}\_{\theta}(\tau\_{k},\zeta^{\*})|\mathcal{F}^{1}\_{\theta}]=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}[\mathcal{P}\_{\theta}(\tau,\zeta^{\*})|\mathcal{F}^{1}\_{\theta}], which exists thanks to Corollary [3.3](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem3 "Corollary 3.3. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and ([3.34](https://arxiv.org/html/2510.15616v1#S3.E34 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")). Then,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ess​infτ∈𝒯θ​(𝔽1)⁡𝖤​[𝒫θ​(τ,ζ∗)|ℱθ−1]≥ess​infτ∈𝒯θR​(𝔽1)⁡𝖤​[𝒫θ​(τ,ζ∗)|ℱθ−1]\displaystyle\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}[\mathcal{P}\_{\theta}(\tau,\zeta^{\*})|\mathcal{F}^{1}\_{\theta-}]\geq\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}[\mathcal{P}\_{\theta}(\tau,\zeta^{\*})|\mathcal{F}^{1}\_{\theta-}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥𝖤​[ess​infτ∈𝒯θR​(𝔽1)⁡𝖤​[𝒫θ​(τ,ζ∗)|ℱθ1]|ℱθ−1]=𝖤​[limk→∞𝖤​[𝒫θ​(τk,ζ∗)|ℱθ1]|ℱθ−1]\displaystyle\geq\mathsf{E}\Big[\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}[\mathcal{P}\_{\theta}(\tau,\zeta^{\*})|\mathcal{F}^{1}\_{\theta}]\Big|\mathcal{F}^{1}\_{\theta-}\Big]=\mathsf{E}\Big[\lim\_{k\to\infty}\mathsf{E}[\mathcal{P}\_{\theta}(\tau\_{k},\zeta^{\*})|\mathcal{F}^{1}\_{\theta}]\Big|\mathcal{F}^{1}\_{\theta-}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =limk→∞𝖤​[𝒫θ​(τk,ζ∗)|ℱθ−1]≥ess​infτ∈𝒯θ​(𝔽1)⁡𝖤​[𝒫θ​(τ,ζ∗)|ℱθ−1],\displaystyle=\lim\_{k\to\infty}\mathsf{E}[\mathcal{P}\_{\theta}(\tau\_{k},\zeta^{\*})|\mathcal{F}^{1}\_{\theta-}]\geq\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}[\mathcal{P}\_{\theta}(\tau,\zeta^{\*})|\mathcal{F}^{1}\_{\theta-}], |  |

where we used the dominated convergence theorem in the second equality. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.35) |  | Σθ−≔ess​infτ∈𝒯θ​(𝔽1)⁡𝖤​[𝒫θ​(τ,ζ∗)|ℱθ−1]=ess​infτ∈𝒯θR​(𝔽1)⁡𝖤​[𝒫θ​(τ,ζ∗)|ℱθ−1],\Sigma\_{\theta-}\coloneqq\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}[\mathcal{P}\_{\theta}(\tau,\zeta^{\*})|\mathcal{F}^{1}\_{\theta-}]=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}[\mathcal{P}\_{\theta}(\tau,\zeta^{\*})|\mathcal{F}^{1}\_{\theta-}], |  |

and (τk)k∈ℕ(\tau\_{k})\_{k\in\mathbb{N}} is also a minimising sequence for Σθ−\Sigma\_{\theta-}. The first inequality in ([3.6](https://arxiv.org/html/2510.15616v1#S3.E6 "In Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) is equivalent to showing that Δ≔V^θ−∗,1−Σθ−≤0\Delta\coloneqq\hat{V}^{\*,1}\_{\theta-}-\Sigma\_{\theta-}\leq 0, which we set out to do next.

Letting (θn)n∈ℕ⊂𝒯0​(𝔽1)(\theta\_{n})\_{n\in\mathbb{N}}\subset\mathcal{T}\_{0}(\mathbb{F}^{1}) be an announcing sequence for θ\theta (i.e., θn<θn+1<θ\theta\_{n}<\theta\_{n+1}<\theta and θn↑θ\theta\_{n}\uparrow\theta), we define Δn≔V^θn∗,1−Σθ−\Delta\_{n}\coloneqq\hat{V}^{\*,1}\_{\theta\_{n}}-\Sigma\_{\theta-} and note that Δ=limn→∞Δn\Delta=\lim\_{n\to\infty}\Delta\_{n}, recalling the existence of the left limit of V^∗,1\hat{V}^{\*,1} at all times. We proceed to derive an upper bound on Δn\Delta\_{n}. Let (τk)k∈ℕ(\tau\_{k})\_{k\in\mathbb{N}} be the minimising sequence for Σθ−\Sigma\_{\theta-} and set Uk≔𝖤​[𝒫θ​(τk,ζ∗)|ℱθ−1]−Σθ−U\_{k}\coloneqq\mathsf{E}\big[\mathcal{P}\_{\theta}(\tau\_{k},\zeta^{\*})\big|\mathcal{F}^{1}\_{\theta-}\big]-\Sigma\_{\theta-}, so that (Uk)k∈ℕ(U\_{k})\_{k\in\mathbb{N}} is a non-negative sequence and it converges to zero 𝖯\mathsf{P}-a.s. as k→∞k\to\infty. Using that 𝒯θn​(𝔽1)⊃𝒯θ​(𝔽1)\mathcal{T}\_{\theta\_{n}}(\mathbb{F}^{1})\supset\mathcal{T}\_{\theta}(\mathbb{F}^{1}) and ([3.28](https://arxiv.org/html/2510.15616v1#S3.E28 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) we have

|  |  |  |
| --- | --- | --- |
|  | Δn≤𝖤​[𝒫θn​(τk,ζ∗)|ℱθn1]−𝖤​[𝒫θ​(τk,ζ∗)|ℱθ−1]+Uk=𝖤​[𝒫θ​(τk,ζ∗)|ℱθn1]−𝖤​[𝒫θ​(τk,ζ∗)|ℱθ−1]+Uk+𝖤​[∫(θn,θ)gt​dζt∗|ℱθn1]≤|𝖤[𝒫θ(τk,ζ∗)|ℱθn1]−𝖤[𝒫θ(τk,ζ∗)|ℱθ−1]|+Uk+𝖤[sup0≤t≤T|gt|(ζθ−∗−ζθn∗)|ℱθn1].\displaystyle\begin{aligned} \Delta\_{n}&\leq\mathsf{E}\big[\mathcal{P}\_{\theta\_{n}}(\tau\_{k},\zeta^{\*})\big|\mathcal{F}^{1}\_{\theta\_{n}}\big]-\mathsf{E}\big[\mathcal{P}\_{\theta}(\tau\_{k},\zeta^{\*})\big|\mathcal{F}^{1}\_{\theta-}\big]+U\_{k}\\ &=\mathsf{E}\big[\mathcal{P}\_{\theta}(\tau\_{k},\zeta^{\*})\big|\mathcal{F}^{1}\_{\theta\_{n}}\big]-\mathsf{E}\big[\mathcal{P}\_{\theta}(\tau\_{k},\zeta^{\*})\big|\mathcal{F}^{1}\_{\theta-}\big]+U\_{k}+\mathsf{E}\Big[\int\_{(\theta\_{n},\theta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big]\\ &\leq\big|\mathsf{E}\big[\mathcal{P}\_{\theta}(\tau\_{k},\zeta^{\*})\big|\mathcal{F}^{1}\_{\theta\_{n}}\big]-\mathsf{E}\big[\mathcal{P}\_{\theta}(\tau\_{k},\zeta^{\*})\big|\mathcal{F}^{1}\_{\theta-}\big]\big|+U\_{k}+\mathsf{E}\Big[\sup\_{0\leq t\leq T}|g\_{t}|\big(\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}}\big)\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big].\end{aligned} |  |

For fixed k∈ℕk\in\mathbb{N} we let n→∞n\to\infty. For the first term in the last line, we define a martingale Λtk≔𝖤​[𝒫θ​(τk,ζ∗)|ℱt1]\Lambda^{k}\_{t}\coloneqq\mathsf{E}\big[\mathcal{P}\_{\theta}(\tau\_{k},\zeta^{\*})\big|\mathcal{F}^{1}\_{t}\big], t≥0t\geq 0, which is càdlàg thanks to Proposition [A.2](https://arxiv.org/html/2510.15616v1#A1.Thmtheorem2 "Proposition A.2. ‣ Appendix A Review of aggregation results ‣ Martingale theory for Dynkin games with asymmetric information"). We have

|  |  |  |
| --- | --- | --- |
|  | limn→∞𝖤​[𝒫θ​(τk,ζ∗)|ℱθn1]=limn→∞Λθnk=Λθ−k=𝖤​[𝒫θ​(τk,ζ∗)|ℱθ−1],\lim\_{n\to\infty}\mathsf{E}\big[\mathcal{P}\_{\theta}(\tau\_{k},\zeta^{\*})\big|\mathcal{F}^{1}\_{\theta\_{n}}\big]=\lim\_{n\to\infty}\Lambda^{k}\_{\theta\_{n}}=\Lambda^{k}\_{\theta-}=\mathsf{E}\big[\mathcal{P}\_{\theta}(\tau\_{k},\zeta^{\*})\big|\mathcal{F}^{1}\_{\theta-}\big], |  |

where the third equality holds thanks to [[DM83](https://arxiv.org/html/2510.15616v1#bib.bibx16), Thm. VI.14] (recall that θ\theta is previsible). The last term in the upper bound for Δn\Delta\_{n} is positive and, by the Markov inequality, for any ε>0\varepsilon>0,

|  |  |  |
| --- | --- | --- |
|  | 𝖯​(𝖤​[sup0≤t≤T|gt|​(ζθ−∗−ζθn∗)|ℱθn1]>ε)≤ε−1​𝖤​[sup0≤t≤T|gt|​(ζθ−∗−ζθn∗)].\mathsf{P}\Big(\mathsf{E}\Big[\sup\_{0\leq t\leq T}|g\_{t}|\big(\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}}\big)\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big]>\varepsilon\Big)\leq\varepsilon^{-1}\mathsf{E}\Big[\sup\_{0\leq t\leq T}|g\_{t}|\big(\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}}\big)\Big]. |  |

Since limn→∞ζθn∗=ζθ−∗\lim\_{n\to\infty}\zeta^{\*}\_{\theta\_{n}}=\zeta^{\*}\_{\theta-}, the right-hand side converges to 0 by the dominated convergence theorem. Hence, 𝖤​[sup0≤t≤T|gt|​(ζθ−∗−ζθn∗)|ℱθn1]→0\mathsf{E}[\sup\_{0\leq t\leq T}|g\_{t}|(\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}})|\mathcal{F}^{1}\_{\theta\_{n}}]\to 0 in probability as n→∞n\to\infty, and it converges a.s. along a subsequence. In conclusion, for each kk, we have Δ≤Uk\Delta\leq U\_{k}. Letting k→∞k\to\infty yields Δ≤0\Delta\leq 0, as needed.

In order to conclude the proof of the theorem it remains to show 𝟏{ξθ−∗<1}​Δ=0\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Delta=0. We proceed with the lower bound on Δn\Delta\_{n} on the set {ξθ−∗<1}\{\xi^{\*}\_{\theta-}<1\}. We start from the observation that

|  |  |  |
| --- | --- | --- |
|  | 𝟏{ξθ−∗<1}​V^θn∗,1=𝟏{ξθ−∗<1}​𝖤​[∫[θn,T)ft​(1−ζt∗)​dξt∗;θn+∫[θn,T)gt​(1−ξt∗;θn)​dζt∗+∑t∈[θn,T]ht​Δ​ξt∗;θn​Δ​ζt∗|ℱθn1],\displaystyle\begin{aligned} &\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\hat{V}^{\*,1}\_{\theta\_{n}}\\ &=\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\mathsf{E}\Big[\int\_{[\theta\_{n},T)}f\_{t}\big(1\!-\!\zeta^{\*}\_{t}\big)\mathrm{d}\xi^{\*;\theta\_{n}}\_{t}\!+\!\int\_{[\theta\_{n},T)}g\_{t}\big(1\!-\!\xi^{\*;\theta\_{n}}\_{t}\big)\mathrm{d}\zeta^{\*}\_{t}\!+\!\sum\_{t\in[\theta\_{n},T]}h\_{t}\Delta\xi^{\*;\theta\_{n}}\_{t}\Delta\zeta^{\*}\_{t}\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big],\end{aligned} |  |

where we invoked the optimality of the truncated controls shown in Proposition [3.8](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), which holds only on the set {ξθn−∗<1}⊃{ξθ−∗<1}\{\xi^{\*}\_{\theta\_{n}-}<1\}\supset\{\xi^{\*}\_{\theta\_{-}}<1\}. Splitting the integration at θ\theta yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.36) |  |  | 𝟏{ξθ−∗<1}​V^θn∗,1\displaystyle\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\hat{V}^{\*,1}\_{\theta\_{n}} |  |
|  |  | =𝟏{ξθ−∗<1}​𝖤​[∫[θn,θ)ft​(1−ζt∗)​dξt∗;θn+∫[θn,θ)gt​(1−ξt∗;θn)​dζt∗+∑t∈[θn,θ)ht​Δ​ξt∗;θn​Δ​ζt∗|ℱθn1]\displaystyle=\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\mathsf{E}\Big[\int\_{[\theta\_{n},\theta)}f\_{t}\big(1-\zeta^{\*}\_{t}\big)\mathrm{d}\xi^{\*;\theta\_{n}}\_{t}+\int\_{[\theta\_{n},\theta)}g\_{t}\big(1-\xi^{\*;\theta\_{n}}\_{t}\big)\mathrm{d}\zeta^{\*}\_{t}+\sum\_{t\in[\theta\_{n},\theta)}h\_{t}\Delta\xi^{\*;\theta\_{n}}\_{t}\Delta\zeta^{\*}\_{t}\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big] |  |
|  |  | +𝟏{ξθ−∗<1}​𝖤​[∫[θ,T)ft​(1−ζt∗)​dξt∗;θn+∫[θ,T)gt​(1−ξt∗;θn)​dζt∗+∑t∈[θ,T]ht​Δ​ξt∗;θn​Δ​ζt∗|ℱθn1].\displaystyle\quad+\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\mathsf{E}\Big[\int\_{[\theta,T)}f\_{t}\big(1-\zeta^{\*}\_{t}\big)\mathrm{d}\xi^{\*;\theta\_{n}}\_{t}+\int\_{[\theta,T)}g\_{t}\big(1-\xi^{\*;\theta\_{n}}\_{t}\big)\mathrm{d}\zeta^{\*}\_{t}+\sum\_{t\in[\theta,T]}h\_{t}\Delta\xi^{\*;\theta\_{n}}\_{t}\Delta\zeta^{\*}\_{t}\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big]. |  |

For the first term on the right-hand side, denoting for simplicity Z≔sup0≤t≤T(|ft|+|gt|+|ht|)Z\coloneqq\sup\_{0\leq t\leq T}\big(|f\_{t}|+|g\_{t}|+|h\_{t}|\big), we have

|  |  |  |
| --- | --- | --- |
|  | 𝟏{ξθ−∗<1}​𝖤​[∫[θn,θ)ft​(1−ζt∗)​dξt∗;θn+∫[θn,θ)gt​(1−ξt∗;θn)​dζt∗+∑t∈[θn,θ)ht​Δ​ξt∗;θn​Δ​ζt∗|ℱθn1]\displaystyle\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\mathsf{E}\Big[\int\_{[\theta\_{n},\theta)}f\_{t}\big(1-\zeta^{\*}\_{t}\big)\mathrm{d}\xi^{\*;\theta\_{n}}\_{t}+\int\_{[\theta\_{n},\theta)}g\_{t}\big(1-\xi^{\*;\theta\_{n}}\_{t}\big)\mathrm{d}\zeta^{\*}\_{t}+\sum\_{t\in[\theta\_{n},\theta)}h\_{t}\Delta\xi^{\*;\theta\_{n}}\_{t}\Delta\zeta^{\*}\_{t}\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≥−𝟏{ξθ−∗<1}​𝖤​[Z​(ξθ−∗−ξθn−∗1−ξθn−∗+ζθ−∗−ζθn−∗)|ℱθn1]\displaystyle\geq-\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\mathsf{E}\Big[Z\Big(\frac{\xi^{\*}\_{\theta-}-\xi^{\*}\_{\theta\_{n}-}}{1-\xi^{\*}\_{\theta\_{n}-}}+\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}-}\Big)\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≥−𝟏{ξθ−∗<1}​𝖤​[Z​(𝟏{ξθ−∗<1}+𝟏{ξθ−∗=1})​(ξθ−∗−ξθn−∗1−ξθn−∗+ζθ−∗−ζθn−∗)|ℱθn1]\displaystyle\geq-\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\mathsf{E}\Big[Z\big(\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}+\mathbf{1}\_{\{\xi^{\*}\_{\theta-}=1\}}\big)\Big(\frac{\xi^{\*}\_{\theta-}-\xi^{\*}\_{\theta\_{n}-}}{1-\xi^{\*}\_{\theta\_{n}-}}+\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}-}\Big)\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≥−𝟏{ξθ−∗<1}​(𝖤​[Z​𝟏{ξθ−∗<1}​(ξθ−∗−ξθn−∗1−ξθn−∗+ζθ−∗−ζθn−∗)|ℱθn1]+𝖤​[2​Z​𝟏{ξθ−∗=1}|ℱθn1]).\displaystyle\geq-\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Big(\mathsf{E}\Big[Z\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Big(\frac{\xi^{\*}\_{\theta-}-\xi^{\*}\_{\theta\_{n}-}}{1-\xi^{\*}\_{\theta\_{n}-}}+\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}-}\Big)\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big]+\mathsf{E}\big[2Z\mathbf{1}\_{\{\xi^{\*}\_{\theta-}=1\}}\big|\mathcal{F}^{1}\_{\theta\_{n}}\big]\Big). |  |

For the second term of ([3.36](https://arxiv.org/html/2510.15616v1#S3.E36 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) we have,

|  |  |  |
| --- | --- | --- |
|  | 𝟏{ξθ−∗<1}​𝖤​[∫[θ,T)ft​(1−ζt∗)​dξt∗;θn+∫[θ,T)gt​(1−ξt∗;θn)​dζt∗+∑t∈[θ,T]ht​Δ​ξt∗;θn​Δ​ζt∗|ℱθn1]\displaystyle\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\mathsf{E}\Big[\int\_{[\theta,T)}f\_{t}\big(1-\zeta^{\*}\_{t}\big)\mathrm{d}\xi^{\*;\theta\_{n}}\_{t}+\int\_{[\theta,T)}g\_{t}\big(1-\xi^{\*;\theta\_{n}}\_{t}\big)\mathrm{d}\zeta^{\*}\_{t}+\ \sum\_{t\in[\theta,T]}h\_{t}\Delta\xi^{\*;\theta\_{n}}\_{t}\Delta\zeta^{\*}\_{t}\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝟏{ξθ−∗<1}​𝖤​[𝟏{ξθ−∗<1}​(∫[θ,T)ft​(1−ζt∗)​dξt∗;θn+∫[θ,T)gt​(1−ξt∗;θn)​dζt∗+∑t∈[θ,T]ht​Δ​ξt∗;θn​Δ​ζt∗)|ℱθn1],\displaystyle=\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\mathsf{E}\Big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Big(\int\_{[\theta,T)}\!\!f\_{t}\big(1\!-\!\zeta^{\*}\_{t}\big)\mathrm{d}\xi^{\*;\theta\_{n}}\_{t}\!+\!\int\_{[\theta,T)}\!\!g\_{t}\big(1\!-\!\xi^{\*;\theta\_{n}}\_{t}\big)\mathrm{d}\zeta^{\*}\_{t}\!+\!\sum\_{t\in[\theta,T]}\!h\_{t}\Delta\xi^{\*;\theta\_{n}}\_{t}\Delta\zeta^{\*}\_{t}\Big)\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big], |  |

because the expression under the expectation equals 0 on {ξθ−∗=1}\{\xi^{\*}\_{\theta-}=1\} as ξt∗;θn=1\xi^{\*;\theta\_{n}}\_{t}=1 for t∈[θ,T]t\in[\theta,T] (recall ([2.11](https://arxiv.org/html/2510.15616v1#S2.E11 "In Definition 2.8. ‣ 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information"))).
By the tower property and skipping the indicator 𝟏{ξθ−∗<1}\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}} outside the expectation for brevity,

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[𝟏{ξθ−∗<1}​(∫[θ,T)ft​(1−ζt∗)​dξt∗;θn+∫[θ,T)gt​(1−ξt∗;θn)​dζt∗+∑t∈[θ,T]ht​Δ​ξt∗;θn​Δ​ζt∗)|ℱθn1]\displaystyle\mathsf{E}\Big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Big(\int\_{[\theta,T)}f\_{t}\big(1-\zeta^{\*}\_{t}\big)\mathrm{d}\xi^{\*;\theta\_{n}}\_{t}+\int\_{[\theta,T)}g\_{t}\big(1-\xi^{\*;\theta\_{n}}\_{t}\big)\mathrm{d}\zeta^{\*}\_{t}+\ \sum\_{t\in[\theta,T]}h\_{t}\Delta\xi^{\*;\theta\_{n}}\_{t}\Delta\zeta^{\*}\_{t}\Big)\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝖤​[𝟏{ξθ−∗<1}​1−ξθ−∗1−ξθn−∗​𝖤​[∫[θ,T)ft​(1−ζt∗)​dξt∗;θ+∫[θ,T)gt​(1−ξt∗;θ)​dζt∗+∑t∈[θ,T]ht​Δ​ξt∗;θ​Δ​ζt∗|ℱθ−1]|ℱθn1]\displaystyle=\mathsf{E}\Big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\frac{1\!-\!\xi^{\*}\_{\theta-}}{1\!-\!\xi^{\*}\_{\theta\_{n}-}}\mathsf{E}\Big[\int\_{[\theta,T)}\!\!f\_{t}\big(1\!-\!\zeta^{\*}\_{t}\big)\mathrm{d}\xi^{\*;\theta}\_{t}\!+\!\int\_{[\theta,T)}\!\!g\_{t}\big(1\!-\!\xi^{\*;\theta}\_{t}\big)\mathrm{d}\zeta^{\*}\_{t}\!+\!\sum\_{t\in[\theta,T]}\!h\_{t}\Delta\xi^{\*;\theta}\_{t}\Delta\zeta^{\*}\_{t}\Big|\mathcal{F}^{1}\_{\theta-}\Big]\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≥𝖤​[𝟏{ξθ−∗<1}​1−ξθ−∗1−ξθn−∗​ess​infτ∈𝒯θR​(𝔽1)⁡𝖤​[fτ​(1−ζτ∗)+∫[θ,τ)gt​dζt∗+hτ​Δ​ζτ∗|ℱθ−1]|ℱθn1]\displaystyle\geq\mathsf{E}\Big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\frac{1-\xi^{\*}\_{\theta-}}{1-\xi^{\*}\_{\theta\_{n}-}}\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\tau}\big(1-\zeta^{\*}\_{\tau}\big)+\int\_{[\theta,\tau)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta-}\Big]\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝖤​[𝟏{ξθ−∗<1}​1−ξθ−∗1−ξθn−∗​ess​infτ∈𝒯θ​(𝔽1)⁡𝖤​[fτ​(1−ζτ∗)+∫[θ,τ)gt​dζt∗+hτ​Δ​ζτ∗|ℱθ−1]|ℱθn1]\displaystyle=\mathsf{E}\Big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\frac{1-\xi^{\*}\_{\theta-}}{1-\xi^{\*}\_{\theta\_{n}-}}\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\tau}\big(1-\zeta^{\*}\_{\tau}\big)+\int\_{[\theta,\tau)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\tau}\Delta\zeta^{\*}\_{\tau}\Big|\mathcal{F}^{1}\_{\theta-}\Big]\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝖤​[𝟏{ξθ−∗<1}​1−ξθ−∗1−ξθn−∗​Σθ−|ℱθn1],\displaystyle=\mathsf{E}\big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\frac{1-\xi^{\*}\_{\theta-}}{1-\xi^{\*}\_{\theta\_{n}-}}\Sigma\_{\theta-}\big|\mathcal{F}^{1}\_{\theta\_{n}}\big], |  |

where in the penultimate equality we substitute 𝒯θR​(𝔽1)\mathcal{T}^{R}\_{\theta}(\mathbb{F}^{1}) with 𝒯θ​(𝔽1)\mathcal{T}\_{\theta}(\mathbb{F}^{1}) by an analogous argument as in the proof of Lemma [3.2](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). Notice that |Σθ−|≤𝖤​[Z|ℱθ−1]|\Sigma\_{\theta-}|\leq\mathsf{E}[Z|\mathcal{F}^{1}\_{\theta-}] and therefore we can further continue the lower bound as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤​[𝟏{ξθ−∗<1}​1−ξθ−∗1−ξθn−∗​Σθ−|ℱθn1]\displaystyle\mathsf{E}\big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\frac{1-\xi^{\*}\_{\theta-}}{1-\xi^{\*}\_{\theta\_{n}-}}\Sigma\_{\theta-}\big|\mathcal{F}^{1}\_{\theta\_{n}}\big] | =𝖤​[𝟏{ξθ−∗<1}​Σθ−|ℱθn1]−𝖤​[𝟏{ξθ−∗<1}​ξθ−∗−ξθn−∗1−ξθn−∗​Σθ−|ℱθn1]\displaystyle=\mathsf{E}\big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Sigma\_{\theta-}\big|\mathcal{F}^{1}\_{\theta\_{n}}\big]-\mathsf{E}\big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\frac{\xi^{\*}\_{\theta-}-\xi^{\*}\_{\theta\_{n}-}}{1-\xi^{\*}\_{\theta\_{n}-}}\Sigma\_{\theta-}\big|\mathcal{F}^{1}\_{\theta\_{n}}\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥𝖤​[𝟏{ξθ−∗<1}​Σθ−|ℱθn1]−𝖤​[𝟏{ξθ−∗<1}​ξθ−∗−ξθn−∗1−ξθn−∗​𝖤​[Z|ℱθ−1]|ℱθn1]\displaystyle\geq\mathsf{E}\big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Sigma\_{\theta-}\big|\mathcal{F}^{1}\_{\theta\_{n}}\big]-\mathsf{E}\big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\frac{\xi^{\*}\_{\theta-}-\xi^{\*}\_{\theta\_{n}-}}{1-\xi^{\*}\_{\theta\_{n}-}}\mathsf{E}[Z|\mathcal{F}^{1}\_{\theta-}]\big|\mathcal{F}^{1}\_{\theta\_{n}}\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖤​[𝟏{ξθ−∗<1}​Σθ−|ℱθn1]−𝖤​[𝟏{ξθ−∗<1}​Z​ξθ−∗−ξθn−∗1−ξθn−∗|ℱθn1],\displaystyle=\mathsf{E}\big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Sigma\_{\theta-}\big|\mathcal{F}^{1}\_{\theta\_{n}}\big]-\mathsf{E}\big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}Z\frac{\xi^{\*}\_{\theta-}-\xi^{\*}\_{\theta\_{n}-}}{1-\xi^{\*}\_{\theta\_{n}-}}\big|\mathcal{F}^{1}\_{\theta\_{n}}\big], |  |

where the final equality is by the tower property.

Combining the estimates above, the lower bound on Δn\Delta\_{n} takes the form

|  |  |  |  |
| --- | --- | --- | --- |
| (3.37) |  | 𝟏{ξθ−∗<1}​Δn≥−𝟏{ξθ−∗<1}​(𝖤​[Z​𝟏{ξθ−∗<1}​(2​ξθ−∗−ξθn−∗1−ξθn−∗+ζθ−∗−ζθn−∗)|ℱθn1]−2​𝖤​[Z​𝟏{ξθ−∗=1}|ℱθn1])+𝟏{ξθ−∗<1}​(𝖤​[𝟏{ξθ−∗<1}​Σθ−|ℱθn1]−Σθ−).\displaystyle\begin{aligned} \mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Delta\_{n}&\geq-\!\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Big(\mathsf{E}\Big[Z\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Big(2\frac{\xi^{\*}\_{\theta-}\!-\!\xi^{\*}\_{\theta\_{n}-}}{1-\xi^{\*}\_{\theta\_{n}-}}\!+\!\zeta^{\*}\_{\theta-}\!-\!\zeta^{\*}\_{\theta\_{n}-}\Big)\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big]-2\mathsf{E}\big[Z\mathbf{1}\_{\{\xi^{\*}\_{\theta-}=1\}}\big|\mathcal{F}^{1}\_{\theta\_{n}}\big]\Big)\\ &\quad+\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Big(\mathsf{E}\big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Sigma\_{\theta-}\big|\mathcal{F}^{1}\_{\theta\_{n}}\big]-\Sigma\_{\theta-}\Big).\end{aligned} |  |

Using again [[DM83](https://arxiv.org/html/2510.15616v1#bib.bibx16), Thm. VI.14] we have 𝖯\mathsf{P}-a.s.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.38) |  | limn→∞𝟏{ξθ−∗<1}​𝖤​[Z​𝟏{ξθ−∗=1}|ℱθn1]\displaystyle\lim\_{n\to\infty}\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\mathsf{E}\big[Z\mathbf{1}\_{\{\xi^{\*}\_{\theta-}=1\}}\big|\mathcal{F}^{1}\_{\theta\_{n}}\big] | =𝟏{ξθ−∗<1}​𝖤​[Z​𝟏{ξθ−∗=1}|ℱθ−1]\displaystyle=\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\mathsf{E}\big[Z\mathbf{1}\_{\{\xi^{\*}\_{\theta-}=1\}}\big|\mathcal{F}^{1}\_{\theta-}\big] |  |
|  |  | =𝟏{ξθ−∗<1}​𝟏{ξθ−∗=1}​𝖤​[Z|ℱθ−1]=0,\displaystyle=\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\mathbf{1}\_{\{\xi^{\*}\_{\theta-}=1\}}\mathsf{E}[Z|\mathcal{F}^{1}\_{\theta-}]=0, |  |

and

|  |  |  |
| --- | --- | --- |
|  | limn→∞𝟏{ξθ−∗<1}​(𝖤​[𝟏{ξθ−∗<1}​Σθ−|ℱθn1]−Σθ−)=𝟏{ξθ−∗<1}​(𝖤​[𝟏{ξθ−∗<1}​Σθ−|ℱθ−1]−Σθ−)=0.\displaystyle\lim\_{n\to\infty}\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Big(\mathsf{E}\big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Sigma\_{\theta-}\big|\mathcal{F}^{1}\_{\theta\_{n}}\big]-\Sigma\_{\theta-}\Big)=\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Big(\mathsf{E}\big[\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Sigma\_{\theta-}\big|\mathcal{F}^{1}\_{\theta-}\big]-\Sigma\_{\theta-}\Big)=0. |  |

By the Markov inequality, for any ε>0\varepsilon>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | limn→∞𝖯​(𝖤​[Z​𝟏{ξθ−∗<1}​(2​ξθ−∗−ξθn−∗1−ξθn−∗+ζθ−∗−ζθn−∗)|ℱθn1]>ε)\displaystyle\lim\_{n\to\infty}\mathsf{P}\Big(\mathsf{E}\Big[Z\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Big(2\frac{\xi^{\*}\_{\theta-}-\xi^{\*}\_{\theta\_{n}-}}{1-\xi^{\*}\_{\theta\_{n}-}}+\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}-}\Big)\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big]>\varepsilon\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ε−1​limn→∞𝖤​[Z​𝟏{ξθ−∗<1}​(2​ξθ−∗−ξθn−∗1−ξθn−∗+ζθ−∗−ζθn−∗)]=0,\displaystyle\leq\varepsilon^{-1}\lim\_{n\to\infty}\mathsf{E}\Big[Z\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Big(2\frac{\xi^{\*}\_{\theta-}-\xi^{\*}\_{\theta\_{n}-}}{1-\xi^{\*}\_{\theta\_{n}-}}+\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}-}\Big)\Big]=0, |  |

where the equality holds by the monotone convergence, because ξθn−∗↑ξθ−∗\xi^{\*}\_{\theta\_{n}-}\uparrow\xi^{\*}\_{\theta-}, ζθn−∗↑ζθ−∗\zeta^{\*}\_{\theta\_{n}-}\uparrow\zeta^{\*}\_{\theta-},
and the mapping x↦(ξθ−∗−x)/(1−x)x\mapsto(\xi^{\*}\_{\theta-}-x)/(1-x) is decreasing for x∈[0,ξθ−∗]x\in[0,\xi^{\*}\_{\theta-}].

Thus, up to selecting a subsequence, all terms on the right-hand side of ([3.37](https://arxiv.org/html/2510.15616v1#S3.E37 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) vanish 𝖯\mathsf{P}-a.s. when n→∞n\to\infty.
This concludes the proof of 𝟏{ξθ−∗<1}​Δ=limn→∞𝟏{ξθ−∗<1}​Δn≥0\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Delta=\lim\_{n\to\infty}\mathbf{1}\_{\{\xi^{\*}\_{\theta-}<1\}}\Delta\_{n}\geq 0. Combining with the upper bound Δ≤0\Delta\leq 0 demonstrates that the inequality in ([3.6](https://arxiv.org/html/2510.15616v1#S3.E6 "In Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) becomes an equality on the set {ξθ−∗<1}\{\xi^{\*}\_{\theta-}<1\}.
∎

###### Proof of Corollary [3.5](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem5 "Corollary 3.5. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

We recall ([3.28](https://arxiv.org/html/2510.15616v1#S3.E28 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), which implies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.39) |  | V^θn∗,1\displaystyle\hat{V}^{\*,1}\_{\theta\_{n}} | ≤𝖤​[fθn​(1−ζθn∗)+hθn​Δ​ζθn∗|ℱθn1]≤𝖤​[fθn​(1−ζθn−∗)|ℱθn1]\displaystyle\leq\mathsf{E}[f\_{\theta\_{n}}(1-\zeta^{\*}\_{\theta\_{n}})+h\_{\theta\_{n}}\Delta\zeta^{\*}\_{\theta\_{n}}|\mathcal{F}^{1}\_{\theta\_{n}}]\leq\mathsf{E}[f\_{\theta\_{n}}(1-\zeta^{\*}\_{\theta\_{n}-})|\mathcal{F}^{1}\_{\theta\_{n}}] |  |
|  |  | =𝖤​[fθn​(ζθ−∗−ζθn−∗)|ℱθn1]+𝖤​[(fθn−fθ−)​(1−ζθ−∗)|ℱθn1]+𝖤​[fθ−​(1−ζθ−∗)|ℱθn1]\displaystyle=\mathsf{E}[f\_{\theta\_{n}}(\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}-})|\mathcal{F}^{1}\_{\theta\_{n}}]+\mathsf{E}[(f\_{\theta\_{n}}-f\_{\theta-})(1-\zeta^{\*}\_{\theta-})|\mathcal{F}^{1}\_{\theta\_{n}}]+\mathsf{E}[f\_{\theta-}(1-\zeta^{\*}\_{\theta-})|\mathcal{F}^{1}\_{\theta\_{n}}] |  |
|  |  | ≤𝖤​[|fθn|​(ζθ−∗−ζθn−∗)|ℱθn1]+𝖤​[|fθn−fθ−|​(1−ζθ−∗)|ℱθn1]+𝖤​[fθ−​(1−ζθ−∗)|ℱθn1].\displaystyle\leq\mathsf{E}[|f\_{\theta\_{n}}|(\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}-})|\mathcal{F}^{1}\_{\theta\_{n}}]+\mathsf{E}[|f\_{\theta\_{n}}-f\_{\theta-}|(1-\zeta^{\*}\_{\theta-})|\mathcal{F}^{1}\_{\theta\_{n}}]+\mathsf{E}[f\_{\theta-}(1-\zeta^{\*}\_{\theta-})|\mathcal{F}^{1}\_{\theta\_{n}}]. |  |

By the Markov inequality, for any ε>0\varepsilon>0 we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝖯​(𝖤​[|fθn|​(ζθ−∗−ζθn−∗)|ℱθn1]>ε)≤1ε​𝖤​[sup0≤t≤T|ft|​(ζθ−∗−ζθn−∗)],\displaystyle\mathsf{P}\big(\mathsf{E}[|f\_{\theta\_{n}}|(\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}-})|\mathcal{F}^{1}\_{\theta\_{n}}]>\varepsilon\big)\leq\tfrac{1}{\varepsilon}\mathsf{E}\big[\sup\_{0\leq t\leq T}|f\_{t}|(\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}-})\big], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝖯​(𝖤​[|fθn−fθ−|​(1−ζθ−∗)|ℱθn1]>ε)≤1ε​𝖤​[|fθn−fθ−|​(1−ζθ−∗)].\displaystyle\mathsf{P}\big(\mathsf{E}[|f\_{\theta\_{n}}-f\_{\theta-}|(1-\zeta^{\*}\_{\theta-})|\mathcal{F}^{1}\_{\theta\_{n}}]>\varepsilon\big)\leq\tfrac{1}{\varepsilon}\mathsf{E}\big[|f\_{\theta\_{n}}-f\_{\theta-}|(1-\zeta^{\*}\_{\theta-})\big]. |  |

Letting n→∞n\to\infty, and applying the dominated convergence on the right-hand side of the above inequalities we obtain convergence in probability

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[|fθn|​(ζθ−∗−ζθn−∗)|ℱθn]→0and𝖤​[|fθn−fθ−|​(1−ζθ−∗)|ℱθn1]→0.\mathsf{E}[|f\_{\theta\_{n}}|(\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}-})|\mathcal{F}\_{\theta\_{n}}]\to 0\quad\text{and}\quad\mathsf{E}[|f\_{\theta\_{n}}-f\_{\theta-}|(1-\zeta^{\*}\_{\theta-})|\mathcal{F}^{1}\_{\theta\_{n}}]\to 0. |  |

Moreover, 𝖤​[fθ−​(1−ζθ−∗)|ℱθn1]→𝖤​[fθ−​(1−ζθ−∗)|ℱθ−1]\mathsf{E}[f\_{\theta-}(1-\zeta^{\*}\_{\theta-})|\mathcal{F}^{1}\_{\theta\_{n}}]\to\mathsf{E}[f\_{\theta-}(1-\zeta^{\*}\_{\theta-})|\mathcal{F}^{1}\_{\theta-}], 𝖯\mathsf{P}-a.s., by [[DM83](https://arxiv.org/html/2510.15616v1#bib.bibx16), Thm. VI.14]. In conclusion, passing to the limit along a subsequence in ([3.39](https://arxiv.org/html/2510.15616v1#S3.E39 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) we obtain

|  |  |  |
| --- | --- | --- |
|  | V^θ−∗,1≤𝖤​[fθ−​(1−ζθ−∗)|ℱθ−1].\hat{V}^{\*,1}\_{\theta-}\leq\mathsf{E}\big[f\_{\theta-}(1-\zeta^{\*}\_{\theta-})\big|\mathcal{F}^{1}\_{\theta-}\big]. |  |

Recalling ([3.28](https://arxiv.org/html/2510.15616v1#S3.E28 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and the notation Σθ−\Sigma\_{\theta-} from ([3.35](https://arxiv.org/html/2510.15616v1#S3.E35 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), the tower property yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^θn∗,1\displaystyle\hat{V}^{\*,1}\_{\theta\_{n}} | ≥ess​infτ∈𝒯θn​(𝔽1)𝖤[𝟏{τ<θ}infs∈[θn,θ)(fs(1−ζs∗)+∫[θn,s)gudζu∗+hsΔζs∗)\displaystyle\geq\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta\_{n}}(\mathbb{F}^{1})}\mathsf{E}\Big[\mathbf{1}\_{\{\tau<\theta\}}\inf\_{s\in[\theta\_{n},\theta)}\Big(f\_{s}(1-\zeta^{\*}\_{s})+\int\_{[\theta\_{n},s)}g\_{u}\mathrm{d}\zeta^{\*}\_{u}+h\_{s}\Delta\zeta^{\*}\_{s}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟏{τ≥θ}(∫[θn,θ)gudζu∗+Σθ−)|ℱθn1].\displaystyle\hskip 65.0pt+\mathbf{1}\_{\{\tau\geq\theta\}}\Big(\int\_{[\theta\_{n},\theta)}g\_{u}\mathrm{d}\zeta^{\*}\_{u}+\Sigma\_{\theta-}\Big)\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big]. |  |

Denoting Zn≔𝖤​[supu∈[0,T]|gu|​(ζθ−∗−ζθn−∗)|ℱθn1]Z\_{n}\coloneqq\mathsf{E}\big[\sup\_{u\in[0,T]}|g\_{u}|(\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}-})\big|\mathcal{F}^{1}\_{\theta\_{n}}\big],
we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | V^θn∗,1\displaystyle\hat{V}^{\*,1}\_{\theta\_{n}} | ≥ess​infτ∈𝒯θn​(𝔽1)⁡𝖤​[𝟏{τ<θ}​𝖤​[infs∈[θn,θ)(fs​(1−ζs∗)+hs​Δ​ζs∗)|ℱθ−1]+𝟏{τ≥θ}​Σθ−|ℱθn1]−Zn\displaystyle\geq\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta\_{n}}(\mathbb{F}^{1})}\mathsf{E}\Big[\mathbf{1}\_{\{\tau<\theta\}}\mathsf{E}\Big[\inf\_{s\in[\theta\_{n},\theta)}\Big(f\_{s}(1-\zeta^{\*}\_{s})+h\_{s}\Delta\zeta^{\*}\_{s}\Big)\Big|\mathcal{F}^{1}\_{\theta-}\Big]+\mathbf{1}\_{\{\tau\geq\theta\}}\Sigma\_{\theta-}\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big]-Z\_{n} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥𝖤​[min⁡(𝖤​[infs∈[θn,θ)(fs​(1−ζs∗)+hs​Δ​ζs∗)|ℱθ−1],Σθ−)|ℱθn1]−Zn,\displaystyle\geq\mathsf{E}\Big[\min\Big(\mathsf{E}\big[\inf\_{s\in[\theta\_{n},\theta)}\big(f\_{s}(1-\zeta^{\*}\_{s})+h\_{s}\Delta\zeta^{\*}\_{s}\big)\big|\mathcal{F}^{1}\_{\theta-}\big],\Sigma\_{\theta-}\Big)\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big]-Z\_{n}, |  |

where in the first line we also used the tower property, the fact that Σθ−\Sigma\_{\theta-} is ℱθ−1\mathcal{F}^{1}\_{\theta-}-measurable and {τ<θ}∈ℱθ−1\{\tau<\theta\}\in\mathcal{F}^{1}\_{\theta-} because θ\theta is previsible.
Setting Yn=𝖤​[supu∈[0,T]|hu|​(ζθ−∗−ζθn−∗)|ℱθn]Y\_{n}=\mathsf{E}[\sup\_{u\in[0,T]}|h\_{u}|(\zeta^{\*}\_{\theta-}-\zeta^{\*}\_{\theta\_{n}-})|\mathcal{F}\_{\theta\_{n}}] and continuing from the above inequalities we get

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.40) |  | V^θn∗,1\displaystyle\hat{V}^{\*,1}\_{\theta\_{n}} | ≥𝖤​[min⁡(𝖤​[infs∈[θn,θ)fs​(1−ζs∗)|ℱθ−1],Σθ−)|ℱθn1]−Yn−Zn.\displaystyle\geq\mathsf{E}\Big[\min\Big(\mathsf{E}\big[\inf\_{s\in[\theta\_{n},\theta)}f\_{s}(1-\zeta^{\*}\_{s})\big|\mathcal{F}^{1}\_{\theta-}\big],\Sigma\_{\theta-}\Big)\Big|\mathcal{F}^{1}\_{\theta\_{n}}\Big]-Y\_{n}-Z\_{n}. |  |

By analogous arguments to those employed above, using the Markov inequality, we can show that Yn→0Y\_{n}\to 0 and Zn→0Z\_{n}\to 0 in probability as n→∞n\to\infty. Moreover, letting n→∞n\to\infty

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[infs∈[θn,θ)fs​(1−ζs∗)|ℱθ−1]→𝖤​[fθ−​(1−ζθ−∗)|ℱθ−1],\mathsf{E}\big[\inf\_{s\in[\theta\_{n},\theta)}f\_{s}(1-\zeta^{\*}\_{s})\big|\mathcal{F}^{1}\_{\theta-}\big]\to\mathsf{E}\big[f\_{\theta-}(1-\zeta^{\*}\_{\theta-})\big|\mathcal{F}^{1}\_{\theta-}\big], |  |

𝖯\mathsf{P}-a.s. by the dominated convergence theorem for conditional expectation [[Bil95](https://arxiv.org/html/2510.15616v1#bib.bibx4), Thm. 34.2].

To simplify presentation, let

|  |  |  |
| --- | --- | --- |
|  | Wn≔min⁡(𝖤​[infs∈[θn,θ)fs​(1−ζs∗)|ℱθ−1],Σθ−)​and​W≔min⁡(𝖤​[fθ−​(1−ζθ−∗)|ℱθ−1],Σθ−).W\_{n}\coloneqq\min\Big(\mathsf{E}\big[\inf\_{s\in[\theta\_{n},\theta)}f\_{s}(1-\zeta^{\*}\_{s})\big|\mathcal{F}^{1}\_{\theta-}\big],\Sigma\_{\theta-}\Big)\ \text{and}\ W\coloneqq\min\Big(\mathsf{E}\big[f\_{\theta-}(1-\zeta^{\*}\_{\theta-})\big|\mathcal{F}^{1}\_{\theta-}\big],\Sigma\_{\theta-}\Big). |  |

Since we have shown that Wn→WW\_{n}\to W, 𝖯\mathsf{P}-a.s., it is not difficult to show

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[Wn|ℱθn]−𝖤​[W|ℱθ−]=𝖤​[Wn−W|ℱθn]+𝖤​[W|ℱθn]−𝖤​[W|ℱθ−]→0,\mathsf{E}[W\_{n}|\mathcal{F}\_{\theta\_{n}}]-\mathsf{E}[W|\mathcal{F}\_{\theta-}]=\mathsf{E}[W\_{n}-W|\mathcal{F}\_{\theta\_{n}}]+\mathsf{E}[W|\mathcal{F}\_{\theta\_{n}}]-\mathsf{E}[W|\mathcal{F}\_{\theta-}]\to 0, |  |

in probability as n→∞n\to\infty, using the Markov inequality and [[DM83](https://arxiv.org/html/2510.15616v1#bib.bibx16), Thm. VI.14] as before.

Finally, we can select a subsequence (nk)n∈ℕ(n\_{k})\_{n\in\mathbb{N}} along which all limits above hold 𝖯\mathsf{P}-a.s., and passing to the limit along such subsequence in ([3.40](https://arxiv.org/html/2510.15616v1#S3.E40 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) we get

|  |  |  |
| --- | --- | --- |
|  | V^θ−∗,1≥min⁡(𝖤​[fθ−​(1−ζθ−∗)|ℱθ−1],Σθ−).\hat{V}^{\*,1}\_{\theta-}\geq\min\big(\mathsf{E}\big[f\_{\theta-}(1-\zeta^{\*}\_{\theta-})\big|\mathcal{F}^{1}\_{\theta-}\big],\Sigma\_{\theta-}\big). |  |

Since we have also shown that V^θ−∗,1≤𝖤​[fθ−​(1−ζθ−∗)|ℱθ−1]\hat{V}^{\*,1}\_{\theta-}\leq\mathsf{E}\big[f\_{\theta-}(1-\zeta^{\*}\_{\theta-})\big|\mathcal{F}^{1}\_{\theta-}\big], we must have V^θ−∗,1=𝖤​[fθ−​(1−ζθ−∗)|ℱθ−1]\hat{V}^{\*,1}\_{\theta-}=\mathsf{E}\big[f\_{\theta-}(1-\zeta^{\*}\_{\theta-})\big|\mathcal{F}^{1}\_{\theta-}\big] on the set {V^θ−∗,1<Σθ−}\{\hat{V}^{\*,1}\_{\theta-}<\Sigma\_{\theta-}\}.
∎

The next result is a refinement of Propositions [3.7](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem7 "Proposition 3.7. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and [3.8](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). In the definition of the families 𝐌ξ{\bf M}^{\xi} and 𝐍ζ{\bf N}^{\zeta}, for arbitrary (ξ,ζ)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\xi,\zeta)\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}), the only terms that require an aggregation step are the families 𝐕∗,𝟏\bf V^{\*,1} and 𝐕∗,𝟐\bf V^{\*,2} appearing therein (the rest is an optional projection of an 𝔽\mathbb{F}-adapted process). The latter have been aggregated into optional processes in Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). Then, the families 𝐌ξ{\bf M}^{\xi} and 𝐍ζ{\bf N}^{\zeta} can also be aggregated into optional processes. The next proposition shows that the resulting processes are respectively super- and sub-martingales as well.

###### Proposition 3.9.

For any (ξ,ζ)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\xi,\zeta)\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}) the families 𝐌ξ{\bf M}^{\xi} and 𝐍ζ{\bf N}^{\zeta} are of class (D)(D) and can be aggregated into an optional submartingale process (Mtξ,𝔽1,𝖯)t∈[0,T](M^{\xi}\_{t},\mathbb{F}^{1},\mathsf{P})\_{t\in[0,T]} and an optional supermartingale process (Ntζ,𝔽2,𝖯)t∈[0,T](N^{\zeta}\_{t},\mathbb{F}^{2},\mathsf{P})\_{t\in[0,T]}, respectively.

###### Proof.

We only need to prove the sub/super-martingale property of the families. As usual, we provide a proof only for MξM^{\xi} because the arguments for NζN^{\zeta} are analogous. We argue in a similar way as in the proof of Proposition [3.7](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem7 "Proposition 3.7. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

Since f,g∈ℒb​(𝖯)f,g\in\mathcal{L}\_{b}(\mathsf{P}), it is easy to verify that 𝐌ξ{\bf M}^{\xi} satisfies 𝖤​[ess​supθ∈𝒯0​(𝔽1)⁡|Mξ​(θ)|]<∞\mathsf{E}[\operatorname\*{ess\,sup}\_{\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})}|M^{\xi}(\theta)|]<\infty. We now want to verify that 𝖤​[Mξ​(τ)]≥𝖤​[Mξ​(σ)]\mathsf{E}[M^{\xi}(\tau)]\geq\mathsf{E}[M^{\xi}(\sigma)] for every τ,σ∈𝒯0​(𝔽1)\tau,\sigma\in\mathcal{T}\_{0}(\mathbb{F}^{1}), σ≤τ\sigma\leq\tau so that the submartingale property can be deduced by Lemma [A.4](https://arxiv.org/html/2510.15616v1#A1.Thmtheorem4 "Lemma A.4. ‣ Appendix A Review of aggregation results ‣ Martingale theory for Dynkin games with asymmetric information").

First we argue on the set {σ<T}\{\sigma<T\}. By the definition of MξM^{\xi} and noticing that

|  |  |  |
| --- | --- | --- |
|  | ∫[0,σ)(1−ζt∗)​ft​dξt+∑t∈[0,σ)ht​Δ​ζt∗​Δ​ξt=∫[0,σ)[(1−ζt∗)​ft+ht​Δ​ζt∗]​dξt,\int\_{[0,\sigma)}(1-\zeta^{\*}\_{t})f\_{t}\mathrm{d}\xi\_{t}+\sum\_{t\in[0,\sigma)}h\_{t}\Delta\zeta^{\*}\_{t}\Delta\xi\_{t}=\int\_{[0,\sigma)}\big[(1-\zeta^{\*}\_{t})f\_{t}+h\_{t}\Delta\zeta^{\*}\_{t}\big]\mathrm{d}\xi\_{t}, |  |

we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.41) |  | Mξ​(σ)\displaystyle M^{\xi}(\sigma) | =𝖤​[∫[0,σ)[(1−ζt∗)​ft+ht​Δ​ζt∗]​dξt+∫[0,σ)(1−ξt)​gt​dζt∗|ℱσ1]\displaystyle=\mathsf{E}\Big[\int\_{[0,\sigma)}\big[(1\!-\!\zeta^{\*}\_{t})f\_{t}\!+\!h\_{t}\Delta\zeta^{\*}\_{t}\big]\mathrm{d}\xi\_{t}+\!\int\_{[0,\sigma)}\!(1\!-\!\xi\_{t})g\_{t}\mathrm{d}\zeta^{\*}\_{t}\Big|\mathcal{F}^{1}\_{\sigma}\Big] |  |
|  |  | +(1−ξσ−)​𝖤​[1−ζσ−∗|ℱσ1]​V∗,1​(σ).\displaystyle\quad+\!(1\!-\!\xi\_{\sigma-})\mathsf{E}[1\!-\!\zeta^{\*}\_{\sigma-}|\mathcal{F}^{1}\_{\sigma}]V^{\*,1}(\sigma). |  |

We recall from ([2.13](https://arxiv.org/html/2510.15616v1#S2.E13 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) the definition of V∗,1​(σ)V^{\*,1}(\sigma) and obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.42) |  |  | 𝖤​[1−ζσ−∗|ℱσ1]​V∗,1​(σ)\displaystyle\mathsf{E}[1-\zeta^{\*}\_{\sigma-}|\mathcal{F}^{1}\_{\sigma}]V^{\*,1}(\sigma) |  |
|  |  | =𝖤​[1−ζσ−∗|ℱσ1]​ess​infθ∈𝒯σR​(𝔽1)⁡𝖤​[Πσ∗,1​(fθ​(1−ζθ∗;σ)+∫[σ,θ)gt​dζt∗;σ+hθ​Δ​ζθ∗;σ)|ℱσ1]\displaystyle=\mathsf{E}[1-\zeta^{\*}\_{\sigma-}|\mathcal{F}^{1}\_{\sigma}]\operatorname\*{ess\,inf}\_{\theta\in\mathcal{T}^{R}\_{\sigma}(\mathbb{F}^{1})}\mathsf{E}\Big[\Pi^{\*,1}\_{\sigma}\Big(f\_{\theta}(1-\zeta^{\*;\sigma}\_{\theta})+\int\_{[\sigma,\theta)}g\_{t}\mathrm{d}\zeta^{\*;\sigma}\_{t}+h\_{\theta}\Delta\zeta^{\*;\sigma}\_{\theta}\Big)\Big|\mathcal{F}^{1}\_{\sigma}\Big] |  |
|  |  | =ess​infθ∈𝒯σR​(𝔽1)⁡𝖤​[fθ​(1−ζθ∗)+∫[σ,θ)gt​dζt∗+hθ​Δ​ζθ∗|ℱσ1]\displaystyle=\operatorname\*{ess\,inf}\_{\theta\in\mathcal{T}^{R}\_{\sigma}(\mathbb{F}^{1})}\mathsf{E}\Big[f\_{\theta}(1-\zeta^{\*}\_{\theta})+\int\_{[\sigma,\theta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\theta}\Delta\zeta^{\*}\_{\theta}\Big|\mathcal{F}^{1}\_{\sigma}\Big] |  |
|  |  | ≤𝖤​[fθ¯​(1−ζθ¯∗)+∫[σ,θ¯)gt​dζt∗+hθ¯​Δ​ζθ¯∗|ℱσ1]for any θ¯∈𝒯σR​(𝔽1),\displaystyle\leq\mathsf{E}\Big[f\_{\bar{\theta}}(1-\zeta^{\*}\_{\bar{\theta}})+\int\_{[\sigma,{\bar{\theta}})}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\bar{\theta}}\Delta\zeta^{\*}\_{\bar{\theta}}\Big|\mathcal{F}^{1}\_{\sigma}\Big]\quad\text{for any $\bar{\theta}\in\mathcal{T}^{R}\_{\sigma}(\mathbb{F}^{1})$,} |  |

where for the second equality we use that 𝖤​[1−ζσ−∗|ℱσ1]​Πθ∗,1=1−ζσ−∗\mathsf{E}[1-\zeta^{\*}\_{\sigma-}|\mathcal{F}^{1}\_{\sigma}]\Pi^{\*,1}\_{\theta}=1-\zeta^{\*}\_{\sigma-} by the definition of Πθ∗,1\Pi^{\*,1}\_{\theta} in ([2.6](https://arxiv.org/html/2510.15616v1#S2.E6 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")). In particular, we choose θ¯∈𝒯σR​(𝔽1)\bar{\theta}\in\mathcal{T}^{R}\_{\sigma}(\mathbb{F}^{1}) generated by a process ξ¯∈𝒜σ∘​(𝔽1)\bar{\xi}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\sigma}(\mathbb{F}^{1}) of the form

|  |  |  |
| --- | --- | --- |
|  | ξ¯t=ξtσ​𝟏{t∈[σ,τ)}+[ξτ−σ+(1−ξτ−σ)​𝟏{t≥η}]​𝟏{t≥τ},\bar{\xi}\_{t}=\xi^{\sigma}\_{t}\mathbf{1}\_{\{t\in[\sigma,\tau)\}}+[\xi^{\sigma}\_{\tau-}+(1-\xi^{\sigma}\_{\tau-})\mathbf{1}\_{\{t\geq\eta\}}]\mathbf{1}\_{\{t\geq\tau\}}, |  |

for an arbitrary η∈𝒯τ​(𝔽1)\eta\in\mathcal{T}\_{\tau}(\mathbb{F}^{1}) and where ξσ\xi^{\sigma} is the truncated control ξ\xi at time σ\sigma. The increasing process ξ¯\bar{\xi} follows the truncated control ξσ\xi^{\sigma} between time σ\sigma and time τ\tau and then it has a single jump to 11 at time η\eta.
Such choice of θ¯∈𝒯σR​(𝔽1)\bar{\theta}\in\mathcal{T}^{R}\_{\sigma}(\mathbb{F}^{1}) in (LABEL:eq:subm0a) yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.43) |  |  | 𝖤​[1−ζσ−∗|ℱσ1]​V∗,1​(σ)\displaystyle\mathsf{E}[1-\zeta^{\*}\_{\sigma-}|\mathcal{F}^{1}\_{\sigma}]V^{\*,1}(\sigma) |  |
|  |  | ≤𝖤[∫[σ,τ)(1−ζt∗)ftdξtσ+∫[σ,τ)(1−ξtσ)gtdζt∗+∑s∈[σ,τ)hsΔζs∗Δξsσ\displaystyle\leq\mathsf{E}\Big[\int\_{[\sigma,\tau)}(1-\zeta^{\*}\_{t})f\_{t}\mathrm{d}\xi^{\sigma}\_{t}+\int\_{[\sigma,\tau)}(1-\xi^{\sigma}\_{t})g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\sum\_{s\in[\sigma,\tau)}h\_{s}\Delta\zeta^{\*}\_{s}\Delta\xi^{\sigma}\_{s} |  |
|  |  | +(1−ξτ−σ)𝖤[fη(1−ζη∗)+∫[τ,η)gtdζt∗+hηΔζη∗|ℱτ1]|ℱσ1]\displaystyle\qquad+(1-\xi^{\sigma}\_{\tau-})\mathsf{E}\Big[f\_{\eta}(1-\zeta^{\*}\_{\eta})+\int\_{[\tau,\eta)}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{\eta}\Delta\zeta^{\*}\_{\eta}\Big|\mathcal{F}^{1}\_{\tau}\Big]\Big|\mathcal{F}^{1}\_{\sigma}\Big] |  |
|  |  | =𝖤[∫[σ,τ)(1−ζt∗)ftdξtσ+∫[σ,τ)(1−ξtσ)gtdζt∗+∑s∈[σ,τ)hsΔζs∗Δξsσ\displaystyle=\mathsf{E}\Big[\int\_{[\sigma,\tau)}(1-\zeta^{\*}\_{t})f\_{t}\mathrm{d}\xi^{\sigma}\_{t}+\int\_{[\sigma,\tau)}(1-\xi^{\sigma}\_{t})g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\sum\_{s\in[\sigma,\tau)}h\_{s}\Delta\zeta^{\*}\_{s}\Delta\xi^{\sigma}\_{s} |  |
|  |  | +(1−ξτ−σ)𝖤[1−ζτ−∗|ℱτ1]𝖤[Πτ∗,1(fη(1−ζη∗;τ)+∫[τ,η)gtdζt∗;τ+hηΔζη∗;τ)|ℱτ1]|ℱσ1]\displaystyle\qquad+(1-\xi^{\sigma}\_{\tau-})\mathsf{E}[1-\zeta^{\*}\_{\tau-}|\mathcal{F}^{1}\_{\tau}]\mathsf{E}\Big[\Pi^{\*,1}\_{\tau}\Big(f\_{\eta}(1-\zeta^{\*;\tau}\_{\eta})+\int\_{[\tau,\eta)}g\_{t}\mathrm{d}\zeta^{\*;\tau}\_{t}+h\_{\eta}\Delta\zeta^{\*;\tau}\_{\eta}\Big)\Big|\mathcal{F}^{1}\_{\tau}\Big]\Big|\mathcal{F}^{1}\_{\sigma}\Big] |  |
|  |  | =𝖤[∫[σ,τ)(1−ζt∗)ftdξtσ+∫[σ,τ)(1−ξtσ)gtdζt∗+∑s∈[σ,τ)hsΔζs∗Δξsσ\displaystyle=\mathsf{E}\Big[\int\_{[\sigma,\tau)}(1-\zeta^{\*}\_{t})f\_{t}\mathrm{d}\xi^{\sigma}\_{t}+\int\_{[\sigma,\tau)}(1-\xi^{\sigma}\_{t})g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\sum\_{s\in[\sigma,\tau)}h\_{s}\Delta\zeta^{\*}\_{s}\Delta\xi^{\sigma}\_{s} |  |
|  |  | +(1−ξτ−σ)𝖤[1−ζτ−∗|ℱτ1]JΠτ∗,1(η,σ∗τ)|ℱτ1)|ℱσ1],\displaystyle\qquad+(1-\xi^{\sigma}\_{\tau-})\mathsf{E}[1-\zeta^{\*}\_{\tau-}|\mathcal{F}^{1}\_{\tau}]J^{\Pi^{\*,1}\_{\tau}}(\eta,\sigma\_{\*}^{\tau})|\mathcal{F}^{1}\_{\tau})\Big|\mathcal{F}^{1}\_{\sigma}\Big], |  |

where in the final expression we use the notation σ∗τ\sigma\_{\*}^{\tau} for the randomised stopping time generated by ζ∗;τ\zeta^{\*;\tau} (cf. Lemma [3.2](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")). By Corollary [3.3](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem3 "Corollary 3.3. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") we can take a sequence (ηn)n∈ℕ⊂𝒯τ​(𝔽1)(\eta\_{n})\_{n\in\mathbb{N}}\subset\mathcal{T}\_{\tau}(\mathbb{F}^{1}) such that 𝖯\mathsf{P}-a.s.

|  |  |  |  |
| --- | --- | --- | --- |
| (3.44) |  | limn→∞JΠτ∗,1(ηn,σ(ζ∗;τ)|ℱτ1),=V∗,1(τ)\lim\_{n\to\infty}J^{\Pi^{\*,1}\_{\tau}}(\eta\_{n},\sigma(\zeta^{\*;\tau})|\mathcal{F}^{1}\_{\tau}),=V^{\*,1}(\tau) |  |

and the limit is monotone from above (although this is a feature which does not play a role in the arguments below). Equation (LABEL:eq:subm01a) with ηn\eta\_{n} instead of η\eta yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤​[1−ζσ−∗|ℱσ1]​V∗,1​(σ)\displaystyle\mathsf{E}[1-\zeta^{\*}\_{\sigma-}|\mathcal{F}^{1}\_{\sigma}]V^{\*,1}(\sigma) | ≤𝖤[∫[σ,τ)(1−ζt∗)ftdξtσ+∫[σ,τ)(1−ξtσ)gtdζt∗+∑s∈[σ,τ)hsΔζs∗Δξsσ\displaystyle\leq\mathsf{E}\Big[\int\_{[\sigma,\tau)}(1-\zeta^{\*}\_{t})f\_{t}\mathrm{d}\xi^{\sigma}\_{t}+\int\_{[\sigma,\tau)}(1-\xi^{\sigma}\_{t})g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\sum\_{s\in[\sigma,\tau)}h\_{s}\Delta\zeta^{\*}\_{s}\Delta\xi^{\sigma}\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−ξτ−σ)𝖤[1−ζτ−∗|ℱτ1]JΠτ∗,1(ηn,σ∗τ)|ℱτ1)|ℱσ1]\displaystyle\qquad+(1-\xi^{\sigma}\_{\tau-})\mathsf{E}[1-\zeta^{\*}\_{\tau-}|\mathcal{F}^{1}\_{\tau}]J^{\Pi^{\*,1}\_{\tau}}(\eta\_{n},\sigma\_{\*}^{\tau})|\mathcal{F}^{1}\_{\tau})\Big|\mathcal{F}^{1}\_{\sigma}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | →n→∞𝖤[∫[σ,τ)(1−ζt∗)ftdξtσ+∫[σ,τ)(1−ξtσ)gtdζt∗+∑s∈[σ,τ)hsΔζs∗Δξsσ\displaystyle\hskip-21.0pt\xrightarrow{n\to\infty}\mathsf{E}\Big[\int\_{[\sigma,\tau)}(1-\zeta^{\*}\_{t})f\_{t}\mathrm{d}\xi^{\sigma}\_{t}+\int\_{[\sigma,\tau)}(1-\xi^{\sigma}\_{t})g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\sum\_{s\in[\sigma,\tau)}h\_{s}\Delta\zeta^{\*}\_{s}\Delta\xi^{\sigma}\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−ξτ−σ)𝖤[1−ζτ−∗|ℱτ1]V∗,1(τ)|ℱσ1],\displaystyle\qquad+(1-\xi^{\sigma}\_{\tau-})\mathsf{E}[1-\zeta^{\*}\_{\tau-}|\mathcal{F}^{1}\_{\tau}]V^{\*,1}(\tau)\Big|\mathcal{F}^{1}\_{\sigma}\Big], |  |

where the limit holds by the dominated convergence theorem and ([3.44](https://arxiv.org/html/2510.15616v1#S3.E44 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")). Substituting into ([3.41](https://arxiv.org/html/2510.15616v1#S3.E41 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), adding the trivial equality Mξ​(σ)=Mξ​(τ)=Mξ​(T)M^{\xi}(\sigma)=M^{\xi}(\tau)=M^{\xi}(T) on {σ=T}\{\sigma=T\} and taking expectation we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤​[Mξ​(σ)]\displaystyle\mathsf{E}[M^{\xi}(\sigma)] | =𝖤​[𝟏{σ<T}​Mξ​(σ)+𝟏{σ=T}​Mξ​(σ)]\displaystyle=\mathsf{E}[\mathbf{1}\_{\{\sigma<T\}}M^{\xi}(\sigma)+\mathbf{1}\_{\{\sigma=T\}}M^{\xi}(\sigma)] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝖤[𝟏{σ<T}(∫[0,τ)[(1−ζt∗)ft+htΔζt∗]dξt+∫[0,τ)(1−ξt)gtdζt∗+(1−ξτ−)𝖤[1−ζτ−∗|ℱτ1]V∗,1(τ))\displaystyle\leq\mathsf{E}\Big[\mathbf{1}\_{\{\sigma<T\}}\Big(\int\_{[0,\tau)}\![(1\!-\!\zeta^{\*}\_{t})f\_{t}\!+\!h\_{t}\Delta\zeta^{\*}\_{t}]\mathrm{d}\xi\_{t}\!+\!\int\_{[0,\tau)}(1\!-\!\xi\_{t})g\_{t}\mathrm{d}\zeta^{\*}\_{t}\!+\!(1\!-\!\xi\_{\tau-})\mathsf{E}[1\!-\!\zeta^{\*}\_{\tau-}|\mathcal{F}^{1}\_{\tau}]V^{\*,1}(\tau)\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟏{σ=T}Mξ(T)]\displaystyle\qquad+\mathbf{1}\_{\{\sigma=T\}}M^{\xi}(T)\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖤​[Mξ​(τ)],\displaystyle=\mathsf{E}[M^{\xi}(\tau)], |  |

where we used that for t∈[σ,τ]t\in[\sigma,\tau] the identities hold
(1−ξσ−)​(1−ξtσ)=(1−ξt)(1-\xi\_{\sigma-})(1-\xi^{\sigma}\_{t})=(1-\xi\_{t}) and (1−ξσ−)​d​ξtσ=d​ξt(1-\xi\_{\sigma-})\mathrm{d}\xi^{\sigma}\_{t}=\mathrm{d}\xi\_{t}.
The above is the required inequality for the submartingale property of the family.
∎

Finally, we obtain a link between the equilibrium values of the two players. Informally, we say that such link is obtained using the information available to both players, in the sense that we consider conditional expectations with respect to the common filtration. Recall the notation ℱt1,2=ℱt1∩ℱt2\mathcal{F}^{1,2}\_{t}=\mathcal{F}^{1}\_{t}\cap\mathcal{F}^{2}\_{t}, t∈[0,T]t\in[0,T], and 𝔽1,2=(ℱt1,2)t∈[0,T]\mathbb{F}^{1,2}=(\mathcal{F}^{1,2}\_{t})\_{t\in[0,T]}.

###### Proposition 3.10.

Let (ξ∗,ζ∗)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\xi^{\*},\zeta^{\*})\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}) be an optimal pair and recall the families 𝐕∗,1{\bf V}^{\*,1} and 𝐕∗,2{\bf V}^{\*,2} from ([3.3](https://arxiv.org/html/2510.15616v1#S3.E3 "In Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")). Then, for any λ∈𝒯0​(𝔽1,2)\lambda\in\mathcal{T}\_{0}(\mathbb{F}^{1,2}) it holds

|  |  |  |  |
| --- | --- | --- | --- |
| (3.45) |  | 𝖤​[(1−ξλ−∗)​𝖤​[1−ζλ−∗|ℱλ1]​V∗,1​(λ)|ℱλ1,2]=𝖤​[(1−ζλ−∗)​𝖤​[1−ξλ−∗|ℱλ2]​V∗,2​(λ)|ℱλ1,2]=𝖤​[∫[λ,T)(1−ζt∗)​ft​dξt∗+∫[λ,T)[(1−ξt∗)​gt+ht​Δ​ξt∗]​dζt∗+hT​Δ​ζT∗​Δ​ξT∗|ℱλ1,2].\displaystyle\begin{aligned} &\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})\mathsf{E}[1-\zeta^{\*}\_{\lambda-}|\mathcal{F}^{1}\_{\lambda}]V^{\*,1}(\lambda)|\mathcal{F}^{1,2}\_{\lambda}\big]\\ &=\mathsf{E}\big[(1-\zeta^{\*}\_{\lambda-})\mathsf{E}[1-\xi^{\*}\_{\lambda-}|\mathcal{F}^{2}\_{\lambda}]V^{\*,2}(\lambda)|\mathcal{F}^{1,2}\_{\lambda}\big]\\ &=\mathsf{E}\Big[\int\_{[\lambda,T)}(1-\zeta^{\*}\_{t})f\_{t}\mathrm{d}\xi^{\*}\_{t}+\int\_{[\lambda,T)}\big[(1-\xi^{\*}\_{t})g\_{t}+h\_{t}\Delta\xi^{\*}\_{t}\big]\mathrm{d}\zeta^{\*}\_{t}+h\_{T}\Delta\zeta^{\*}\_{T}\Delta\xi^{\*}\_{T}\Big|\mathcal{F}^{1,2}\_{\lambda}\Big].\end{aligned} |  |

###### Proof.

From the definition of V∗,1V^{\*,1} and the assumed optimality of the pair (ξ∗,ζ∗)(\xi^{\*},\zeta^{\*}) we have

|  |  |  |  |
| --- | --- | --- | --- |
| (3.46) |  | 𝖤​[(1−ξλ−∗)​𝖤​[1−ζλ−∗|ℱλ1]​V∗,1​(λ)|ℱλ1,2]=𝖤​[(1−ξλ−∗)​𝖤​[1−ζλ−∗|ℱλ1]​ess​infξ∈𝒜λ∘​(𝔽1)⁡JΠλ∗,1​(ξ,ζ∗;λ|ℱλ1)|ℱλ1,2]=𝖤​[(1−ξλ−∗)​𝖤​[1−ζλ−∗|ℱλ1]​JΠλ∗,1​(ξ∗;λ,ζ∗;λ|ℱλ1)|ℱλ1,2],\displaystyle\begin{aligned} &\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})\mathsf{E}[1-\zeta^{\*}\_{\lambda-}|\mathcal{F}^{1}\_{\lambda}]V^{\*,1}(\lambda)|\mathcal{F}^{1,2}\_{\lambda}\big]\\ &=\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})\mathsf{E}[1-\zeta^{\*}\_{\lambda-}|\mathcal{F}^{1}\_{\lambda}]\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1})}J^{\Pi^{\*,1}\_{\lambda}}\big(\xi,\zeta^{\*;\lambda}\big|\mathcal{F}^{1}\_{\lambda}\big)|\mathcal{F}^{1,2}\_{\lambda}\big]\\ &=\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})\mathsf{E}[1-\zeta^{\*}\_{\lambda-}|\mathcal{F}^{1}\_{\lambda}]J^{\Pi^{\*,1}\_{\lambda}}\big(\xi^{\*;\lambda},\zeta^{\*;\lambda}\big|\mathcal{F}^{1}\_{\lambda}\big)|\mathcal{F}^{1,2}\_{\lambda}\big],\end{aligned} |  |

where the final equality uses the optimality of ξ∗;λ\xi^{\*;\lambda} (cf. Proposition [3.8](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")). Then, the tower property and the definition of Πλ∗,1\Pi^{\*,1}\_{\lambda} yield

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[(1−ξλ−∗)​𝖤​[1−ζλ−∗|ℱλ1]​V∗,1​(λ)|ℱλ1,2]=𝖤​[∫[λ,T)[(1−ζt∗)​ft+ht​Δ​ζt∗]​dξt∗+∫[λ,T)(1−ξt∗)​gt​dζt∗+hT​Δ​ζT∗​Δ​ξT∗|ℱλ1,2].\displaystyle\begin{aligned} &\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})\mathsf{E}[1-\zeta^{\*}\_{\lambda-}|\mathcal{F}^{1}\_{\lambda}]V^{\*,1}(\lambda)|\mathcal{F}^{1,2}\_{\lambda}\big]\\ &=\mathsf{E}\Big[\int\_{[\lambda,T)}\big[(1-\zeta^{\*}\_{t})f\_{t}+h\_{t}\Delta\zeta^{\*}\_{t}\big]\mathrm{d}\xi^{\*}\_{t}+\int\_{[\lambda,T)}(1-\xi^{\*}\_{t})g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{T}\Delta\zeta^{\*}\_{T}\Delta\xi^{\*}\_{T}\Big|\mathcal{F}^{1,2}\_{\lambda}\Big].\end{aligned} |  |

By analogous arguments, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
| (3.47) |  | 𝖤​[(1−ζλ−∗)​𝖤​[1−ξλ−∗|ℱλ2]​V∗,2​(λ)|ℱλ1,2]=𝖤​[(1−ζλ−∗)​𝖤​[1−ξλ−∗|ℱλ2]​ess​supζ∈𝒜λ∘⁡JΠλ∗,2​(ξ∗;λ,ζ|ℱλ2)|ℱλ1,2]=𝖤​[∫[λ,T)(1−ζt∗)​ft​dξt∗+∫[λ,T)[(1−ξt∗)​gt+ht​Δ​ξt∗]​dζt∗+hT​Δ​ζT∗​Δ​ξT∗|ℱλ1,2].\displaystyle\begin{aligned} &\mathsf{E}\big[(1-\zeta^{\*}\_{\lambda-})\mathsf{E}[1-\xi^{\*}\_{\lambda-}|\mathcal{F}^{2}\_{\lambda}]V^{\*,2}(\lambda)|\mathcal{F}^{1,2}\_{\lambda}\big]\\ &=\mathsf{E}\big[(1-\zeta^{\*}\_{\lambda-})\mathsf{E}[1-\xi^{\*}\_{\lambda-}|\mathcal{F}^{2}\_{\lambda}]\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}}J^{\Pi^{\*,2}\_{\lambda}}\big(\xi^{\*;\lambda},\zeta\big|\mathcal{F}^{2}\_{\lambda}\big)|\mathcal{F}^{1,2}\_{\lambda}\big]\\ &=\mathsf{E}\Big[\int\_{[\lambda,T)}(1-\zeta^{\*}\_{t})f\_{t}\mathrm{d}\xi^{\*}\_{t}+\int\_{[\lambda,T)}\big[(1-\xi^{\*}\_{t})g\_{t}+h\_{t}\Delta\xi^{\*}\_{t}\big]\mathrm{d}\zeta^{\*}\_{t}+h\_{T}\Delta\zeta^{\*}\_{T}\Delta\xi^{\*}\_{T}\Big|\mathcal{F}^{1,2}\_{\lambda}\Big].\end{aligned} |  |

This concludes the proof upon noticing ∫[λ,T)ht​Δ​ζt∗​dξt∗=∫[λ,T)ht​Δ​ξt∗​dζt∗=∑t∈[λ,T)ht​Δ​ξt∗​Δ​ζt∗\int\_{[\lambda,T)}h\_{t}\Delta\zeta^{\*}\_{t}\mathrm{d}\xi^{\*}\_{t}=\int\_{[\lambda,T)}h\_{t}\Delta\xi^{\*}\_{t}\mathrm{d}\zeta^{\*}\_{t}=\sum\_{t\in[\lambda,T)}h\_{t}\Delta\xi^{\*}\_{t}\Delta\zeta^{\*}\_{t}.
∎

###### Remark 3.11.

Notice that the first two lines of ([3.45](https://arxiv.org/html/2510.15616v1#S3.E45 "In Proposition 3.10. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) equivalently read

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝖤​[(1−ξλ−∗)​(1−ζλ−∗)​V∗,1​(λ)|ℱλ1,2]=𝖤​[(1−ζλ−∗)​(1−ξλ−∗)​V∗,2​(λ)|ℱλ1,2],\displaystyle\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})(1-\zeta^{\*}\_{\lambda-})V^{\*,1}(\lambda)|\mathcal{F}^{1,2}\_{\lambda}\big]=\mathsf{E}\big[(1-\zeta^{\*}\_{\lambda-})(1-\xi^{\*}\_{\lambda-})V^{\*,2}(\lambda)|\mathcal{F}^{1,2}\_{\lambda}\big], |  |

because (1−ξλ−∗)​V∗,1​(λ)(1-\xi^{\*}\_{\lambda-})V^{\*,1}(\lambda) is ℱλ1\mathcal{F}^{1}\_{\lambda}-measurable and (1−ζλ−∗)​V∗,2​(λ)(1-\zeta^{\*}\_{\lambda-})V^{\*,2}(\lambda) is ℱλ2\mathcal{F}^{2}\_{\lambda}-measurable, so that the tower property yields the required transformation of the first two expressions in ([3.45](https://arxiv.org/html/2510.15616v1#S3.E45 "In Proposition 3.10. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")). We formulated ([3.45](https://arxiv.org/html/2510.15616v1#S3.E45 "In Proposition 3.10. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) with the additional conditional expectation due to the special role played by the quantities 𝖤​[1−ζλ−∗|ℱλ1]​V∗,1​(λ)\mathsf{E}[1-\zeta^{\*}\_{\lambda-}|\mathcal{F}^{1}\_{\lambda}]V^{\*,1}(\lambda) and 𝖤​[1−ξλ−∗|ℱλ2]​V∗,2​(λ)\mathsf{E}[1-\xi^{\*}\_{\lambda-}|\mathcal{F}^{2}\_{\lambda}]V^{\*,2}(\lambda) in Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

###### Remark 3.12.

When 𝔽1,2={Ω,∅}\mathbb{F}^{1,2}=\{\Omega,\varnothing\}, ([3.45](https://arxiv.org/html/2510.15616v1#S3.E45 "In Proposition 3.10. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) reduces to

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[(1−ξλ−∗)​𝖤​[1−ζλ−∗|ℱλ1]​V∗,1​(λ)]=𝖤​[(1−ζλ−∗)​𝖤​[1−ξλ−∗|ℱλ2]​V∗,2​(λ)],\displaystyle\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})\mathsf{E}[1-\zeta^{\*}\_{\lambda-}|\mathcal{F}^{1}\_{\lambda}]V^{\*,1}(\lambda)\big]=\mathsf{E}\big[(1-\zeta^{\*}\_{\lambda-})\mathsf{E}[1-\xi^{\*}\_{\lambda-}|\mathcal{F}^{2}\_{\lambda}]V^{\*,2}(\lambda)\big], |  |

for deterministic times λ∈[0,T]\lambda\in[0,T].

When 𝔽1⊃𝔽2\mathbb{F}^{1}\supset\mathbb{F}^{2}, then ([3.45](https://arxiv.org/html/2510.15616v1#S3.E45 "In Proposition 3.10. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) holds for any λ∈𝒯0​(𝔽2)\lambda\in\mathcal{T}\_{0}(\mathbb{F}^{2}) in a more explicit form:

|  |  |  |
| --- | --- | --- |
|  | (1−ζλ−∗)​𝖤​[(1−ξλ−∗)​V∗,1​(λ)|ℱλ2]=𝖤​[1−ξλ−∗|ℱλ2]​(1−ζλ−∗)​V∗,2​(λ).\displaystyle(1-\zeta^{\*}\_{\lambda-})\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})V^{\*,1}(\lambda)|\mathcal{F}^{2}\_{\lambda}\big]=\mathsf{E}\big[1-\xi^{\*}\_{\lambda-}|\mathcal{F}^{2}\_{\lambda}\big](1-\zeta^{\*}\_{\lambda-})V^{\*,2}(\lambda). |  |

The final expression in ([3.45](https://arxiv.org/html/2510.15616v1#S3.E45 "In Proposition 3.10. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) can be related to the ex-ante value of the game. To make the statement rigorous, we introduce the family 𝐕¯≔{V¯​(λ),λ∈𝒯0​(𝔽1,2)}{\bf\bar{V}}\coloneqq\{\bar{V}(\lambda),\,\lambda\in\mathcal{T}\_{0}(\mathbb{F}^{1,2})\}, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯​(λ)\displaystyle\bar{V}(\lambda) | ≔𝖤​[∫[λ,T)(1−ζt∗)​ft​dξt∗+∫[λ,T)[(1−ξt∗)​gt+ht​Δ​ξt∗]​dζt∗+hT​Δ​ζT∗​Δ​ξT∗|ℱλ1,2]\displaystyle\coloneqq\mathsf{E}\Big[\int\_{[\lambda,T)}(1-\zeta^{\*}\_{t})f\_{t}\mathrm{d}\xi^{\*}\_{t}+\int\_{[\lambda,T)}\big[(1-\xi^{\*}\_{t})g\_{t}+h\_{t}\Delta\xi^{\*}\_{t}\big]\mathrm{d}\zeta^{\*}\_{t}+h\_{T}\Delta\zeta^{\*}\_{T}\Delta\xi^{\*}\_{T}\Big|\mathcal{F}^{1,2}\_{\lambda}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖤​[∫[λ,T)(1−ζt∗)​[ft+ht​Δ​ζt∗]​dξt∗+∫[λ,T)(1−ξt∗)​gt​dζt∗+hT​Δ​ζT∗​Δ​ξT∗|ℱλ1,2],\displaystyle=\mathsf{E}\Big[\int\_{[\lambda,T)}(1-\zeta^{\*}\_{t})\big[f\_{t}+h\_{t}\Delta\zeta^{\*}\_{t}\big]\mathrm{d}\xi^{\*}\_{t}+\int\_{[\lambda,T)}(1-\xi^{\*}\_{t})g\_{t}\mathrm{d}\zeta^{\*}\_{t}+h\_{T}\Delta\zeta^{\*}\_{T}\Delta\xi^{\*}\_{T}\Big|\mathcal{F}^{1,2}\_{\lambda}\Big], |  |

where the second equality is simply eliciting the symmetry of the expected payoffs.
The family 𝐕¯{\bf\bar{V}} can be aggregated into an 𝔽1,2\mathbb{F}^{1,2}-optional process (V¯t)t∈[0,T](\bar{V}\_{t})\_{t\in[0,T]}, thanks to the following observation:

|  |  |  |
| --- | --- | --- |
|  | V¯​(λ)=𝖤​[(1−ξλ−∗)​(1−ζλ−∗)​V∗,1​(λ)|ℱλ1,2]=𝖤​[(1−ξλ−∗)​V^λ∗,1|ℱλ1,2],\bar{V}(\lambda)=\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})(1-\zeta^{\*}\_{\lambda-})V^{\*,1}(\lambda)\big|\mathcal{F}^{1,2}\_{\lambda}\big]=\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})\hat{V}^{\*,1}\_{\lambda}\big|\mathcal{F}^{1,2}\_{\lambda}\big], |  |

where the first equality is by ([3.45](https://arxiv.org/html/2510.15616v1#S3.E45 "In Proposition 3.10. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and the second stems from the fact that (V^t)t∈[0,T](\hat{V}\_{t})\_{t\in[0,T]} aggregates the family {𝖤​[1−ζλ−∗|ℱθ1]​V∗,1​(θ):θ∈𝒯0​(𝔽1)}\{\mathsf{E}[1-\zeta^{\*}\_{\lambda-}|\mathcal{F}^{1}\_{\theta}]V^{\*,1}(\theta):\ \theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})\} and 𝒯0​(𝔽1,2)⊂𝒯0​(𝔽1)\mathcal{T}\_{0}(\mathbb{F}^{1,2})\subset\mathcal{T}\_{0}(\mathbb{F}^{1}). Hence, the process (V¯t)t∈[0,T](\bar{V}\_{t})\_{t\in[0,T]} that aggregates the family 𝐕¯{\bf\bar{V}} is the 𝔽1,2\mathbb{F}^{1,2}-optional projection of the process ((1−ξt−∗)​V^t∗,1)t∈[0,T]((1-\xi^{\*}\_{t-})\hat{V}^{\*,1}\_{t})\_{t\in[0,T]} or equivalently of the process ((1−ζt−∗)​V^t∗,2)t∈[0,T]((1-\zeta^{\*}\_{t-})\hat{V}^{\*,2}\_{t})\_{t\in[0,T]}.

###### Corollary 3.13.

Let (ξ∗,ζ∗)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\xi^{\*},\zeta^{\*})\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}) be an optimal pair. For any λ∈𝒯0​(𝔽1,2)\lambda\in\mathcal{T}\_{0}(\mathbb{F}^{1,2}), set

|  |  |  |
| --- | --- | --- |
|  | Πλ∗≔(1−ξλ−∗)​(1−ζλ−∗)𝖤​[(1−ξλ−∗)​(1−ζλ−∗)|ℱλ1,2]∈ℛ​(ℱλ1,2),\Pi^{\*}\_{\lambda}\coloneqq\frac{(1-\xi^{\*}\_{\lambda-})(1-\zeta^{\*}\_{\lambda-})}{\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})(1-\zeta^{\*}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]}\in\mathcal{R}(\mathcal{F}^{1,2}\_{\lambda}), |  |

with the convention adopted in ([2.6](https://arxiv.org/html/2510.15616v1#S2.E6 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) that 0/0=10/0=1 (cf. ([2.9](https://arxiv.org/html/2510.15616v1#S2.E9 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) for a justification of this choice).

Define V​(λ)≔JΠλ∗​(ξ∗;λ,ζ∗;λ|ℱλ1,2)V(\lambda)\coloneqq J^{\Pi^{\*}\_{\lambda}}(\xi^{\*;\lambda},\zeta^{\*;\lambda}|\mathcal{F}^{1,2}\_{\lambda}). Then,
we have

|  |  |  |  |
| --- | --- | --- | --- |
| (3.48) |  | V​(λ)=ess​infξ∈𝒜λ∘​(𝔽1)⁡ess​supζ∈𝒜λ∘​(𝔽2)⁡JΠλ∗​(ξ,ζ|ℱλ1,2)=ess​supζ∈𝒜λ∘​(𝔽2)⁡ess​infξ∈𝒜λ∘​(𝔽1)⁡JΠλ∗​(ξ,ζ|ℱλ1,2),\displaystyle\begin{aligned} V(\lambda)=\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1})}\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{2})}J^{\Pi^{\*}\_{\lambda}}(\xi,\zeta|\mathcal{F}^{1,2}\_{\lambda})=\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{2})}\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1})}J^{\Pi^{\*}\_{\lambda}}(\xi,\zeta|\mathcal{F}^{1,2}\_{\lambda}),\end{aligned} |  |

on the event {𝖤​[(1−ξλ−∗)​(1−ζλ−∗)|ℱλ1,2]>0}\{\mathsf{E}[(1-\xi^{\*}\_{\lambda-})(1-\zeta^{\*}\_{\lambda-})|\mathcal{F}^{1,2}\_{\lambda}]>0\}.
Moreover, it holds

|  |  |  |  |
| --- | --- | --- | --- |
| (3.49) |  | V¯​(λ)=𝖤​[(1−ξλ−∗)​(1−ζλ−∗)|ℱλ1,2]​V​(λ).\displaystyle\bar{V}(\lambda)=\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})(1-\zeta^{\*}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]V(\lambda). |  |

###### Proof.

From the second line of ([3.46](https://arxiv.org/html/2510.15616v1#S3.E46 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), using the minimising sequence from Lemma [3.1](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem1 "Lemma 3.1. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and the monotone convergence we get the second equality below (cf. ([B.2](https://arxiv.org/html/2510.15616v1#A2.E2 "In Appendix B Upward and downward directed families ‣ Martingale theory for Dynkin games with asymmetric information")))

|  |  |  |  |
| --- | --- | --- | --- |
| (3.50) |  | V¯​(λ)=𝖤​[(1−ξλ−∗)​𝖤​[1−ζλ−∗|ℱλ1]​V∗,1​(λ)|ℱλ1,2]=𝖤​[(1−ξλ−∗)​𝖤​[1−ζλ−∗|ℱλ1]​ess​infξ∈𝒜λ∘​(𝔽1)⁡JΠλ∗,1​(ξ,ζ∗;λ|ℱλ1)|ℱλ1,2]=ess​infξ∈𝒜λ∘​(𝔽1)⁡𝖤​[(1−ξλ−∗)​𝖤​[1−ζλ−∗|ℱλ1]​JΠλ∗,1​(ξ,ζ∗;λ|ℱλ1)|ℱλ1,2].\displaystyle\begin{aligned} \bar{V}(\lambda)&=\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})\mathsf{E}[1-\zeta^{\*}\_{\lambda-}|\mathcal{F}^{1}\_{\lambda}]V^{\*,1}(\lambda)\,\big|\mathcal{F}^{1,2}\_{\lambda}\big]\\ &=\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})\mathsf{E}[1-\zeta^{\*}\_{\lambda-}|\mathcal{F}^{1}\_{\lambda}]\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1})}J^{\Pi^{\*,1}\_{\lambda}}(\xi,\zeta^{\*;\lambda}|\mathcal{F}^{1}\_{\lambda})\,\big|\mathcal{F}^{1,2}\_{\lambda}\big]\\ &=\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1})}\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})\mathsf{E}[1-\zeta^{\*}\_{\lambda-}|\mathcal{F}^{1}\_{\lambda}]J^{\Pi^{\*,1}\_{\lambda}}(\xi,\zeta^{\*;\lambda}|\mathcal{F}^{1}\_{\lambda})\,\big|\mathcal{F}^{1,2}\_{\lambda}\big].\end{aligned} |  |

Using the expression for JΠλ∗,1​(ξ,ζ∗;λ|ℱλ1)J^{\Pi^{\*,1}\_{\lambda}}\big(\xi,\zeta^{\*;\lambda}\big|\mathcal{F}^{1}\_{\lambda}\big) and the tower property

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[(1−ξλ−∗)​𝖤​[1−ζλ−∗|ℱλ1]​JΠλ∗,1​(ξ,ζ∗;λ|ℱλ1)|ℱλ1,2]=𝖤[(1−ξλ−∗)(1−ζλ−∗)(∫[λ,T)[(1−ζT∗;λ)ft+htΔζt∗;λ]dξt+∫[λ,T)(1−ξt)gtdζt∗;λ+hTΔξTΔζT∗;λ)|ℱλ1,2]=𝖤​[(1−ξλ−∗)​(1−ζλ−∗)|ℱλ1,2]​JΠλ∗​(ξ,ζ∗;λ|ℱλ1,2).\displaystyle\begin{aligned} &\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})\mathsf{E}[1-\zeta^{\*}\_{\lambda-}|\mathcal{F}^{1}\_{\lambda}]J^{\Pi^{\*,1}\_{\lambda}}\big(\xi,\zeta^{\*;\lambda}\big|\mathcal{F}^{1}\_{\lambda}\big)|\mathcal{F}^{1,2}\_{\lambda}\big]\\ &=\mathsf{E}\Big[(1-\xi^{\*}\_{\lambda-})(1-\zeta^{\*}\_{\lambda-})\Big(\int\_{[\lambda,T)}\!\!\big[(1\!-\!\zeta^{\*;\lambda}\_{T})f\_{t}\!+\!h\_{t}\Delta\zeta^{\*;\lambda}\_{t}\big]\mathrm{d}\xi\_{t}\\ &\hskip 120.0pt+\!\int\_{[\lambda,T)}\!\!(1\!-\!\xi\_{t})g\_{t}\mathrm{d}\zeta^{\*;\lambda}\_{t}\!+\!h\_{T}\Delta\xi\_{T}\Delta\zeta^{\*;\lambda}\_{T}\Big)\Big|\mathcal{F}^{1,2}\_{\lambda}\Big]\\ &=\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})(1-\zeta^{\*}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]J^{\Pi^{\*}\_{\lambda}}\big(\xi,\zeta^{\*;\lambda}\big|\mathcal{F}^{1,2}\_{\lambda}\big).\end{aligned} |  |

Combining the two expressions above we deduce

|  |  |  |  |
| --- | --- | --- | --- |
| (3.51) |  | V¯​(λ)=𝖤​[(1−ξλ−∗)​(1−ζλ−∗)|ℱλ1,2]​ess​infξ∈𝒜λ∘​(𝔽1)⁡JΠλ∗​(ξ,ζ∗;λ|ℱλ1,2)≤𝖤​[(1−ξλ−∗)​(1−ζλ−∗)|ℱλ1,2]​ess​supζ∈𝒜λ∘​(𝔽2)⁡ess​infξ∈𝒜λ∘​(𝔽1)⁡JΠλ∗​(ξ,ζ|ℱλ1,2).\displaystyle\begin{aligned} \bar{V}(\lambda)&=\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})(1-\zeta^{\*}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1})}J^{\Pi^{\*}\_{\lambda}}\big(\xi,\zeta^{\*;\lambda}\big|\mathcal{F}^{1,2}\_{\lambda}\big)\\ &\leq\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})(1-\zeta^{\*}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{2})}\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1})}J^{\Pi^{\*}\_{\lambda}}\big(\xi,\zeta\big|\mathcal{F}^{1,2}\_{\lambda}\big).\end{aligned} |  |

For the reverse inequality, we start from the second line in ([3.47](https://arxiv.org/html/2510.15616v1#S3.E47 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and follow the same steps as above. That yields

|  |  |  |  |
| --- | --- | --- | --- |
| (3.52) |  | V¯​(λ)=𝖤​[(1−ζλ−∗)​𝖤​[1−ξλ−∗|ℱλ2]​V∗,2​(λ)|ℱλ1,2]=ess​supζ∈𝒜λ∘​(𝔽2)⁡𝖤​[(1−ζλ−∗)​𝖤​[1−ξλ−∗|ℱλ2]​JΠλ∗,2​(ξ∗;λ,ζ|ℱλ2)|ℱλ1,2]=𝖤​[(1−ξλ−∗)​(1−ζλ−∗)|ℱλ1,2]​ess​supζ∈𝒜λ∘​(𝔽2)⁡JΠλ∗​(ξ∗;λ,ζ|ℱλ1,2)≥𝖤​[(1−ξλ−∗)​(1−ζλ−∗)|ℱλ1,2]​ess​infξ∈𝒜λ∘​(𝔽1)⁡ess​supζ∈𝒜λ∘​(𝔽2)⁡JΠλ∗​(ξ,ζ|ℱλ1,2),\displaystyle\begin{aligned} \bar{V}(\lambda)&=\mathsf{E}\big[(1-\zeta^{\*}\_{\lambda-})\mathsf{E}[1-\xi^{\*}\_{\lambda-}|\mathcal{F}^{2}\_{\lambda}]V^{\*,2}(\lambda)\,\big|\mathcal{F}^{1,2}\_{\lambda}\big]\\ &=\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{2})}\mathsf{E}\big[(1-\zeta^{\*}\_{\lambda-})\mathsf{E}[1-\xi^{\*}\_{\lambda-}|\mathcal{F}^{2}\_{\lambda}]J^{\Pi^{\*,2}\_{\lambda}}(\xi^{\*;\lambda},\zeta|\mathcal{F}^{2}\_{\lambda})\,\big|\mathcal{F}^{1,2}\_{\lambda}\big]\\ &=\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})(1-\zeta^{\*}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{2})}J^{\Pi^{\*}\_{\lambda}}(\xi^{\*;\lambda},\zeta|\mathcal{F}^{1,2}\_{\lambda})\\ &\geq\mathsf{E}\big[(1-\xi^{\*}\_{\lambda-})(1-\zeta^{\*}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1})}\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{2})}J^{\Pi^{\*}\_{\lambda}}(\xi,\zeta|\mathcal{F}^{1,2}\_{\lambda}),\end{aligned} |  |

where the third equality is by the use of the tower property and the definition of JΠλ∗,2​(ξ∗;λ,ζ|ℱλ2)J^{\Pi^{\*,2}\_{\lambda}}\big(\xi^{\*;\lambda},\zeta\big|\mathcal{F}^{2}\_{\lambda}\big).

Since

|  |  |  |
| --- | --- | --- |
|  | ess​infξ∈𝒜λ∘​(𝔽1)⁡ess​supζ∈𝒜λ∘​(𝔽2)⁡JΠλ∗​(ξ∗;λ,ζ|ℱλ1,2)≥ess​supζ∈𝒜λ∘​(𝔽2)⁡ess​infξ∈𝒜λ∘​(𝔽1)⁡JΠλ∗​(ξ∗;λ,ζ|ℱλ1,2),\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1})}\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{2})}J^{\Pi^{\*}\_{\lambda}}\big(\xi^{\*;\lambda},\zeta\big|\mathcal{F}^{1,2}\_{\lambda}\big)\geq\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{2})}\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1})}J^{\Pi^{\*}\_{\lambda}}\big(\xi^{\*;\lambda},\zeta\big|\mathcal{F}^{1,2}\_{\lambda}\big), |  |

the inequalities ([3.51](https://arxiv.org/html/2510.15616v1#S3.E51 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and ([3.52](https://arxiv.org/html/2510.15616v1#S3.E52 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) yield ([3.49](https://arxiv.org/html/2510.15616v1#S3.E49 "In Corollary 3.13. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and the second equality in ([3.48](https://arxiv.org/html/2510.15616v1#S3.E48 "In Corollary 3.13. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")). The first equality in ([3.48](https://arxiv.org/html/2510.15616v1#S3.E48 "In Corollary 3.13. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) is easily deduced from the first line of ([3.50](https://arxiv.org/html/2510.15616v1#S3.E50 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and ([3.52](https://arxiv.org/html/2510.15616v1#S3.E52 "In 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), using the optimality of truncated controls (cf. Proposition [3.8](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")).
∎

The random variable V​(λ)V(\lambda) is a dynamic analogue of the ex-ante value of the game starting at time λ\lambda. In the expression for V​(λ)V(\lambda), players optimise the expected payoff conditional on the jointly available information at time λ\lambda (i.e., conditioning on ℱλ1,2\mathcal{F}^{1,2}\_{\lambda}). However, they still pick their randomised stopping times making use of their individual filtrations 𝔽1\mathbb{F}^{1} and 𝔽2\mathbb{F}^{2}. That is to say, players know that they will have access to the full content of their individual filtrations after time λ\lambda.

### 3.4. Structure of optimal strategies

In this section we look into some structural properties of optimal strategies.
The main results in this section are Proposition [3.17](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem17 "Proposition 3.17. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and Corollary [3.19](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem19 "Corollary 3.19. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") but they require some preparation which we do in Propositions [3.14](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem14 "Proposition 3.14. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), [3.15](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem15 "Proposition 3.15. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and Corollary [3.16](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem16 "Corollary 3.16. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). Throughout the section we maintain Notation [2.3](https://arxiv.org/html/2510.15616v1#S2.Thmtheorem3 "Notation 2.3. ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information") for the optimal pairs (ξ∗,ζ∗)(\xi^{\*},\zeta^{\*}) and (τ∗,σ∗)(\tau\_{\*},\sigma\_{\*}).

Combining the expressions of the aggregated càdlàg processes M∗M^{\*} and N∗N^{\*} from Proposition [3.8](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and of the optional processes V^∗,1\hat{V}^{\*,1} and V^∗,2\hat{V}^{\*,2} from Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") we have, for any (θ,γ)∈𝒯0​(𝔽1)×𝒯0​(𝔽2)(\theta,\gamma)\in\mathcal{T}\_{0}(\mathbb{F}^{1})\times\mathcal{T}\_{0}(\mathbb{F}^{2}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mθ∗\displaystyle M^{\*}\_{\theta} | =𝖤​[∫[0,θ)(fs​(1−ζs∗)+hs​Δ​ζs∗)​dξs∗+∫[0,θ)(1−ξs∗)​gs​dζs∗|ℱθ1]+(1−ξθ−∗)​V^θ∗,1\displaystyle=\mathsf{E}\Big[\int\_{[0,\theta)}\Big(f\_{s}(1-\zeta^{\*}\_{s})+h\_{s}\Delta\zeta^{\*}\_{s}\Big)\mathrm{d}\xi^{\*}\_{s}+\int\_{[0,\theta)}(1-\xi^{\*}\_{s})g\_{s}\mathrm{d}\zeta^{\*}\_{s}\Big|\mathcal{F}^{1}\_{\theta}\Big]+(1-\xi^{\*}\_{\theta-})\hat{V}^{\*,1}\_{\theta} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖤​[𝟏{τ∗<θ}​(fτ∗​𝟏{τ∗<σ∗}+hτ∗​𝟏{τ∗=σ∗})+𝟏{σ∗<θ}​𝟏{σ∗<τ∗}​gσ∗|ℱθ1]+𝖤​[𝟏{θ≤τ∗}|ℱθ1]​V^θ∗,1,\displaystyle=\mathsf{E}\Big[\mathbf{1}\_{\{\tau\_{\*}<\theta\}}\Big(f\_{\tau\_{\*}}\mathbf{1}\_{\{\tau\_{\*}<\sigma\_{\*}\}}+h\_{\tau\_{\*}}\mathbf{1}\_{\{\tau\_{\*}=\sigma\_{\*}\}}\Big)+\mathbf{1}\_{\{\sigma\_{\*}<\theta\}}\mathbf{1}\_{\{\sigma\_{\*}<\tau\_{\*}\}}g\_{\sigma\_{\*}}\Big|\mathcal{F}^{1}\_{\theta}\Big]+\mathsf{E}[\mathbf{1}\_{\{\theta\leq\tau\_{\*}\}}|\mathcal{F}^{1}\_{\theta}]\hat{V}^{\*,1}\_{\theta}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Nγ∗\displaystyle N^{\*}\_{\gamma} | =𝖤​[∫[0,γ)fs​(1−ζs∗)​dξs∗+∫[0,γ)((1−ξs∗)​gs+hs​Δ​ξs∗)​dζs∗|ℱγ2]+(1−ζγ−∗)​V^γ∗,2\displaystyle=\mathsf{E}\Big[\int\_{[0,\gamma)}f\_{s}(1-\zeta^{\*}\_{s})\mathrm{d}\xi^{\*}\_{s}+\int\_{[0,\gamma)}\Big((1-\xi^{\*}\_{s})g\_{s}+h\_{s}\Delta\xi^{\*}\_{s}\Big)\mathrm{d}\zeta^{\*}\_{s}\Big|\mathcal{F}^{2}\_{\gamma}\Big]+(1-\zeta^{\*}\_{\gamma-})\hat{V}^{\*,2}\_{\gamma} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖤​[𝟏{τ∗<γ}​𝟏{τ∗<σ∗}​fτ∗+𝟏{σ∗<γ}​(𝟏{σ∗<τ∗}​gσ∗+hσ∗​𝟏{τ∗=σ∗})|ℱγ2]+𝖤​[𝟏{γ≤σ∗}|ℱγ2]​V^γ∗,2.\displaystyle=\mathsf{E}\Big[\mathbf{1}\_{\{\tau\_{\*}<\gamma\}}\mathbf{1}\_{\{\tau\_{\*}<\sigma\_{\*}\}}f\_{\tau\_{\*}}+\mathbf{1}\_{\{\sigma\_{\*}<\gamma\}}\Big(\mathbf{1}\_{\{\sigma\_{\*}<\tau\_{\*}\}}g\_{\sigma\_{\*}}+h\_{\sigma\_{\*}}\mathbf{1}\_{\{\tau\_{\*}=\sigma\_{\*}\}}\Big)\Big|\mathcal{F}^{2}\_{\gamma}\Big]+\mathsf{E}[\mathbf{1}\_{\{\gamma\leq\sigma\_{\*}\}}|\mathcal{F}^{2}\_{\gamma}]\hat{V}^{\*,2}\_{\gamma}. |  |

We will explicitly write the integration of players’ randomisation devices and in doing so identify stopping times over which the players randomise.
Recall (τ¯∗​(z),σ¯∗​(z))∈𝒯0​(𝔽1)×𝒯0​(𝔽2)(\bar{\tau}\_{\*}(z),\bar{\sigma}\_{\*}(z))\in\mathcal{T}\_{0}(\mathbb{F}^{1})\times\mathcal{T}\_{0}(\mathbb{F}^{2}) from ([3.10](https://arxiv.org/html/2510.15616v1#S3.E10 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), which we denote here (τ∗​(z),σ∗​(z))(\tau\_{\*}(z),\sigma\_{\*}(z)) for the simplicity of notation.

The next characterisation of Mθ∗M^{\*}\_{\theta} and Nγ∗N^{\*}\_{\gamma} proves useful.

###### Proposition 3.14.

There are mappings (z,ω)↦m∗​(θ;z)​(ω)(z,\omega)\mapsto m^{\*}(\theta;z)(\omega) and (z,ω)↦n∗​(γ;z)​(ω)(z,\omega)\mapsto n^{\*}(\gamma;z)(\omega) which are measurable for the σ\sigma-algebras ℬ​([0,1])×ℱθ1\mathcal{B}([0,1])\times\mathcal{F}^{1}\_{\theta} and ℬ​([0,1])×ℱγ2\mathcal{B}([0,1])\times\mathcal{F}^{2}\_{\gamma}, respectively, and such that:

* (i)

  it holds

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (3.53) |  | Mθ∗=∫01m∗​(θ;z)​dzandNγ∗=∫01n∗​(γ;z)​dz;M^{\*}\_{\theta}=\int\_{0}^{1}m^{\*}(\theta;z)\mathrm{d}z\quad\text{and}\quad N^{\*}\_{\gamma}=\int\_{0}^{1}n^{\*}(\gamma;z)\mathrm{d}z; |  |
* (ii)

  for each z∈[0,1]z\in[0,1], 𝖯\mathsf{P}-a.s.,

  |  |  |  |
  | --- | --- | --- |
  |  | m∗​(θ;z)=𝖤​[𝟏{τ∗​(z)<θ}​(fτ∗​(z)​𝟏{τ∗​(z)<σ∗}+hτ∗​(z)​𝟏{τ∗​(z)=σ∗})|ℱθ1]+𝖤​[𝟏{σ∗<θ}​𝟏{σ∗<τ∗​(z)}​gσ∗|ℱθ1]+𝟏{θ≤τ∗​(z)}​V^θ∗,1,\displaystyle\begin{aligned} m^{\*}(\theta;z)&=\mathsf{E}\Big[\mathbf{1}\_{\{\tau\_{\*}(z)<\theta\}}\Big(f\_{\tau\_{\*}(z)}\mathbf{1}\_{\{\tau\_{\*}(z)<\sigma\_{\*}\}}\!+\!h\_{\tau\_{\*}(z)}\mathbf{1}\_{\{\tau\_{\*}(z)=\sigma\_{\*}\}}\Big)\Big|\mathcal{F}^{1}\_{\theta}\Big]\\ &\quad+\mathsf{E}\Big[\mathbf{1}\_{\{\sigma\_{\*}<\theta\}}\mathbf{1}\_{\{\sigma\_{\*}<\tau\_{\*}(z)\}}g\_{\sigma\_{\*}}\Big|\mathcal{F}^{1}\_{\theta}\Big]\!+\!\mathbf{1}\_{\{\theta\leq\tau\_{\*}(z)\}}\hat{V}^{\*,1}\_{\theta},\end{aligned} |  |

  and

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | n∗​(γ;z)\displaystyle n^{\*}(\gamma;z) | =𝖤​[𝟏{σ∗​(z)<γ}​(𝟏{σ∗​(z)<τ∗}​gσ∗​(z)+hσ∗​(z)​𝟏{τ∗=σ∗​(z)})|ℱγ2]\displaystyle=\mathsf{E}\Big[\mathbf{1}\_{\{\sigma\_{\*}(z)<\gamma\}}\Big(\mathbf{1}\_{\{\sigma\_{\*}(z)<\tau\_{\*}\}}g\_{\sigma\_{\*}(z)}\!+\!h\_{\sigma\_{\*}(z)}\mathbf{1}\_{\{\tau\_{\*}=\sigma\_{\*}(z)\}}\Big)\Big|\mathcal{F}^{2}\_{\gamma}\Big] |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | +𝖤​[𝟏{τ∗<γ}​𝟏{τ∗<σ∗​(z)}​fτ∗|ℱγ2]+𝟏{γ≤σ∗​(z)}​V^γ∗,2.\displaystyle\quad+\mathsf{E}\Big[\mathbf{1}\_{\{\tau\_{\*}<\gamma\}}\mathbf{1}\_{\{\tau\_{\*}<\sigma\_{\*}(z)\}}f\_{\tau\_{\*}}\Big|\mathcal{F}^{2}\_{\gamma}\Big]\!+\!\mathbf{1}\_{\{\gamma\leq\sigma\_{\*}(z)\}}\hat{V}^{\*,2}\_{\gamma}. |  |

The result can be interpreted as an application of Fubini’s theorem, although some care is needed because the conditional expectations on the right-hand side of the equations in (ii) are not necessarily jointly measurable in (z,ω)(z,\omega) and therefore we need to consider suitable modifications m∗​(θ;z)​(ω)m^{\*}(\theta;z)(\omega) and n∗​(γ;z)​(ω)n^{\*}(\gamma;z)(\omega). Although the result is not surprising, its proof is slightly technical and we provide it in Appendix [C.2](https://arxiv.org/html/2510.15616v1#A3.SS2 "C.2. Proof of Proposition 3.14 ‣ Appendix C Remaining proofs ‣ Martingale theory for Dynkin games with asymmetric information").

###### Proposition 3.15.

Families {m∗​(θ;z),θ∈𝒯0​(𝔽1)}\{m^{\*}(\theta;z),\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})\} and {n∗​(γ;z),γ∈𝒯0​(𝔽2)}\{n^{\*}(\gamma;z),\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2})\} are of class (D)(D) and can be aggregated into optional processes (mt∗​(z))t∈[0,T](m^{\*}\_{t}(z))\_{t\in[0,T]} and (nt∗​(z))t∈[0,T](n^{\*}\_{t}(z))\_{t\in[0,T]}, respectively, for every z∈[0,1]z\in[0,1].

Furthermore, (mt∗​(z))t∈[0,T](m^{\*}\_{t}(z))\_{t\in[0,T]} is a càdlàg 𝔽1\mathbb{F}^{1}-martingale and (nt∗​(z))t∈[0,T](n^{\*}\_{t}(z))\_{t\in[0,T]} is a càdlàg 𝔽2\mathbb{F}^{2}-martingale for almost every z∈[0,1]z\in[0,1].
We also have

|  |  |  |  |
| --- | --- | --- | --- |
| (3.54) |  | Mθ∗=∫01mθ∗​(z)​dz,Nγ∗=∫01nγ∗​(z)​dz,M^{\*}\_{\theta}=\int\_{0}^{1}m^{\*}\_{\theta}(z)\mathrm{d}z,\qquad N^{\*}\_{\gamma}=\int\_{0}^{1}n^{\*}\_{\gamma}(z)\mathrm{d}z, |  |

for any (θ,γ)∈𝒯0​(𝔽1)×𝒯0​(𝔽2)(\theta,\gamma)\in\mathcal{T}\_{0}(\mathbb{F}^{1})\times\mathcal{T}\_{0}(\mathbb{F}^{2}).

###### Proof.

The class (D)(D) property is immediate because f,g,h∈ℒb​(𝖯)f,g,h\in\mathcal{L}\_{b}(\mathsf{P}). We recall that the family 𝐌ξ{\bf M}^{\xi} can be aggregated into an optional submartingale process (Mtξ,𝔽1,𝖯)t∈[0,T](M^{\xi}\_{t},\mathbb{F}^{1},\mathsf{P})\_{t\in[0,T]} (cf. Proposition [3.9](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem9 "Proposition 3.9. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) for any ξ∈𝒜0∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1}). Then we observe that taking ξt=𝟏{τ∗​(z)≤t}\xi\_{t}=\mathbf{1}\_{\{\tau\_{\*}(z)\leq t\}} in the definition of MξM^{\xi} we obtain Mθξ=m∗​(θ;z)M^{\xi}\_{\theta}=m^{\*}(\theta;z) for any θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}). Hence, for every z∈[0,1]z\in[0,1] and for ξt=𝟏{τ∗​(z)≤t}\xi\_{t}=\mathbf{1}\_{\{\tau\_{\*}(z)\leq t\}}

|  |  |  |
| --- | --- | --- |
|  | (mt∗​(z))t∈[0,T]≔(Mtξ)t∈[0,T],(m^{\*}\_{t}(z))\_{t\in[0,T]}\coloneqq(M^{\xi}\_{t})\_{t\in[0,T]}, |  |

is an 𝔽1\mathbb{F}^{1}-optional submartingale that aggregates the family {m∗​(θ;z),θ∈𝒯0​(𝔽1)}\{m^{\*}(\theta;z),\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})\}.

From ([3.53](https://arxiv.org/html/2510.15616v1#S3.E53 "In item (i) ‣ Proposition 3.14. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and from the fact that mt∗​(z)=m∗​(t;z)m^{\*}\_{t}(z)=m^{\*}(t;z), 𝖯\mathsf{P}-a.s. for any z∈[0,1]z\in[0,1] we obtain

|  |  |  |  |
| --- | --- | --- | --- |
| (3.55) |  | 𝖤​[MT∗−M0∗]=∫01𝖤​[m∗​(T;z)−m∗​(0;z)]​dz=∫01𝖤​[mT∗​(z)−m0∗​(z)]​dz.\mathsf{E}[M^{\*}\_{T}-M^{\*}\_{0}]=\int\_{0}^{1}\mathsf{E}\big[m^{\*}(T;z)-m^{\*}(0;z)\big]\mathrm{d}z=\int\_{0}^{1}\mathsf{E}[m^{\*}\_{T}(z)-m^{\*}\_{0}(z)]\mathrm{d}z. |  |

We can only guarantee the measurability of the map z↦𝖤​[mT∗​(z)−m0∗​(z)]z\mapsto\mathsf{E}[m^{\*}\_{T}(z)-m^{\*}\_{0}(z)] by referring to the measurability of (z,ω)↦[m∗​(T;z)​(ω)−m∗​(0;z)​(ω)](z,\omega)\mapsto[m^{\*}(T;z)(\omega)-m^{\*}(0;z)(\omega)] (cf. Proposition [3.14](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem14 "Proposition 3.14. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and to the fact that mT∗​(z)=m∗​(T;z)m^{\*}\_{T}(z)=m^{\*}(T;z) and m0∗​(z)=m∗​(0;z)m^{\*}\_{0}(z)=m^{\*}(0;z), 𝖯\mathsf{P}-a.s. However, the map z↦mT∗​(z)z\mapsto m^{\*}\_{T}(z) may not be measurable, hence, the order of integration on the right-hand side of ([3.55](https://arxiv.org/html/2510.15616v1#S3.E55 "In 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) cannot be interchanged.

Recall that (mt∗​(z))t∈[0,T](m^{\*}\_{t}(z))\_{t\in[0,T]} is an 𝔽1\mathbb{F}^{1}-submartingale for every z∈[0,1]z\in[0,1]. This implies that 𝖤​[mT∗​(z)−m0∗​(z)]≥0\mathsf{E}[m^{\*}\_{T}(z)-m^{\*}\_{0}(z)]\geq 0. We also note that (Mt∗)t∈[0,T](M^{\*}\_{t})\_{t\in[0,T]} is an 𝔽1\mathbb{F}^{1}-martingale, so 𝖤​[MT∗−M0∗]=0\mathsf{E}[M^{\*}\_{T}-M^{\*}\_{0}]=0. These two observations and ([3.55](https://arxiv.org/html/2510.15616v1#S3.E55 "In 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) lead to the conclusion that 𝖤​[mT∗​(z)−m0∗​(z)]=0\mathsf{E}[m^{\*}\_{T}(z)-m^{\*}\_{0}(z)]=0 for almost every z∈[0,1]z\in[0,1]. When we combine this with the submartingale property of (mt∗​(z))t∈[0,T](m^{\*}\_{t}(z))\_{t\in[0,T]}, we see that (mt∗​(z))t∈[0,T](m^{\*}\_{t}(z))\_{t\in[0,T]} is an 𝔽1\mathbb{F}^{1}-optional martingale for almost every z∈[0,1]z\in[0,1]. Then, by Corollary [A.3](https://arxiv.org/html/2510.15616v1#A1.Thmtheorem3 "Corollary A.3. ‣ Appendix A Review of aggregation results ‣ Martingale theory for Dynkin games with asymmetric information") it is indistinguishable from a càdlàg martingale: indeed for a.e. z∈[0,1]z\in[0,1], the family {mθ∗​(z),θ∈𝒯0​(𝔽1)}\{m^{\*}\_{\theta}(z),\,\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})\} can be aggregated into a càdlàg martingale (m¯tz)t∈[0,T](\bar{m}^{z}\_{t})\_{t\in[0,T]} (i.e., 𝖯​(mθ∗​(z)=m¯θz)=1\mathsf{P}(m^{\*}\_{\theta}(z)=\bar{m}^{z}\_{\theta})=1 for any θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})). Since mt∗​(z)m^{\*}\_{t}(z) and m¯tz\bar{m}^{z}\_{t} are optional processes that coincide on stopping times, they are indistinguishable [[RW00](https://arxiv.org/html/2510.15616v1#bib.bibx39), Lemma VI.5.2]. Thus, mt∗​(z)m^{\*}\_{t}(z) is itself càdlàg.

The arguments for (nt∗​(z))t∈[0,T](n^{\*}\_{t}(z))\_{t\in[0,T]} are analogous and, therefore, omitted. Equalities ([3.54](https://arxiv.org/html/2510.15616v1#S3.E54 "In Proposition 3.15. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) are
proven by combining ([3.53](https://arxiv.org/html/2510.15616v1#S3.E53 "In item (i) ‣ Proposition 3.14. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and the aggregation result.
∎

A corollary links the above result to properties of processes M0M^{0} and N0N^{0} from Proposition [3.7](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem7 "Proposition 3.7. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

###### Corollary 3.16.

The processes (Mt∧τ∗​(z)0)t∈[0,T](M^{0}\_{t\wedge\tau\_{\*}(z)})\_{t\in[0,T]} and (Nt∧σ∗​(z)0)t∈[0,T](N^{0}\_{t\wedge\sigma\_{\*}(z)})\_{t\in[0,T]} are a càdlàg 𝔽1\mathbb{F}^{1}-martingale and a càdlàg 𝔽2\mathbb{F}^{2}-martingale, respectively, for any z∈[0,1)z\in[0,1).

###### Proof.

Take any z∈[0,1]z\in[0,1] from the full measure set on which (mt∗​(z))t∈[0,T](m^{\*}\_{t}(z))\_{t\in[0,T]} constructed in Proposition [3.15](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem15 "Proposition 3.15. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") is a càdlàg 𝔽1\mathbb{F}^{1}-martingale. For any θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}), by the definition of mt∗​(z)m^{\*}\_{t}(z) we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.56) |  | mθ∧τ∗​(z)∗​(z)\displaystyle m^{\*}\_{\theta\wedge\tau\_{\*}(z)}(z) | =𝖤​[𝟏{σ∗<θ∧τ∗​(z)}​gσ∗|ℱθ∧τ∗​(z)1]+V^θ∧τ∗​(z)∗,1\displaystyle=\mathsf{E}\big[\mathbf{1}\_{\{\sigma\_{\*}<\theta\wedge\tau\_{\*}(z)\}}g\_{\sigma\_{\*}}\big|\mathcal{F}^{1}\_{\theta\wedge\tau\_{\*}(z)}\big]+\hat{V}^{\*,1}\_{\theta\wedge\tau\_{\*}(z)} |  |
|  |  | =𝖤​[∫[0,θ∧τ∗​(z))gs​dζs∗|ℱθ∧τ∗​(z)1]+V^θ∧τ∗​(z)∗,1=Mθ∧τ∗​(z)0,\displaystyle=\mathsf{E}\Big[\int\_{[0,\theta\wedge\tau\_{\*}(z))}g\_{s}\mathrm{d}\zeta^{\*}\_{s}\Big|\mathcal{F}^{1}\_{\theta\wedge\tau\_{\*}(z)}\Big]+\hat{V}^{\*,1}\_{\theta\wedge\tau\_{\*}(z)}=M^{0}\_{\theta\wedge\tau\_{\*}(z)}, |  |

where the final equality holds by the expression ([3.12](https://arxiv.org/html/2510.15616v1#S3.E12 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) for M0M^{0}.

By Proposition [3.7](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem7 "Proposition 3.7. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), (Mt0)t∈[0,T](M^{0}\_{t})\_{t\in[0,T]} is a càdlàg 𝔽1\mathbb{F}^{1}-submartingale. Hence, (Mt∧τ∗​(z)0)t∈[0,T](M^{0}\_{t\wedge\tau\_{\*}(z)})\_{t\in[0,T]} is actually a càdlàg 𝔽1\mathbb{F}^{1}-martingale, indistinguishable from (mt∧τ∗​(z)∗​(z))t∈[0,T](m^{\*}\_{t\wedge\tau\_{\*}(z)}(z))\_{t\in[0,T]} thanks to [[RW00](https://arxiv.org/html/2510.15616v1#bib.bibx39), Lemma VI.5.2]. This proves that (Mt∧τ∗​(z)0)t∈[0,T](M^{0}\_{t\wedge\tau\_{\*}(z)})\_{t\in[0,T]} is an 𝔽1\mathbb{F}^{1}-martingale for almost every z∈[0,1]z\in[0,1], but the result extends to all z∈[0,1)z\in[0,1) as follows: for any z<1z<1, there is z^∈[z,1]\hat{z}\in[z,1] for which the martingale condition holds; due to the monotonicity of z↦τ∗​(z)z\mapsto\tau\_{\*}(z), we have τ∗​(z)≤τ∗​(z^)\tau\_{\*}(z)\leq\tau\_{\*}(\hat{z}), so the martingale condition holds until time τ∗​(z)\tau\_{\*}(z) too.

An analogous argument leads to the proof of the claim for N0N^{0}.
∎

In the next proposition we determine the support of the generating processes for an optimal randomised pair (τ∗,σ∗)(\tau\_{\*},\sigma\_{\*}). We introduce a notation that is needed for the next result and is used extensively in the Appendix: given a process X∈ℒb​(𝖯)X\in\mathcal{L}\_{b}(\mathsf{P}) and a filtration 𝔾\mathbb{G}, we denote by Xo𝔾=(Xot𝔾)t∈[0,T]\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-8.522pt{o}\kern 6.10211pt}}\_{{\kern-5.64687pt\kern 6.10211pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-8.522pt{o}\kern 6.10211pt}}\_{{\kern-5.64687pt\kern 6.10211pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-5.18529pt{o}\kern 3.44402pt}}\_{{\kern-2.98877pt\kern 3.44402pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-3.91557pt{o}\kern 2.1743pt}}\_{{\kern-1.71906pt\kern 2.1743pt}}}^{\mathbb{G}}=(\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-8.522pt{o}\kern 6.10211pt}}\_{{\kern-5.64687pt\kern 6.10211pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-8.522pt{o}\kern 6.10211pt}}\_{{\kern-5.64687pt\kern 6.10211pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-5.18529pt{o}\kern 3.44402pt}}\_{{\kern-2.98877pt\kern 3.44402pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-3.91557pt{o}\kern 2.1743pt}}\_{{\kern-1.71906pt\kern 2.1743pt}}}^{\mathbb{G}}\_{t})\_{t\in[0,T]} its 𝔾\mathbb{G}-optional projection under the measure 𝖯\mathsf{P}.

###### Proposition 3.17.

Let (ξ∗,ζ∗)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\xi^{\*},\zeta^{\*})\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}) be an optimal pair and recall the optional semimartingale processes (V^t∗,1)t∈[0,T](\hat{V}^{\*,1}\_{t})\_{t\in[0,T]} and (V^t∗,2)t∈[0,T](\hat{V}^{\*,2}\_{t})\_{t\in[0,T]} from Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). Let us define

|  |  |  |
| --- | --- | --- |
|  | Yt1≔V^t∗,1−(of⋅(1−ζ⋅∗))t𝔽1−(oh⋅Δζ⋅∗)t𝔽1andYt2≔V^t∗,2−(og⋅(1−ξ⋅∗))t𝔽2−(oh⋅Δξ⋅∗)t𝔽2.\displaystyle Y^{1}\_{t}\coloneqq\hat{V}^{\*,1}\_{t}-\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}f\_{\cdot}(1-\zeta^{\*}\_{\cdot})\big)\_{t}^{\mathbb{F}^{1}}-\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}h\_{\cdot}\Delta\zeta^{\*}\_{\cdot}\big)\_{t}^{\mathbb{F}^{1}}\quad\text{and}\quad Y^{2}\_{t}\coloneqq\hat{V}^{\*,2}\_{t}-\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}g\_{\cdot}(1-\xi^{\*}\_{\cdot})\big)^{\mathbb{F}^{2}}\_{t}-\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}h\_{\cdot}\Delta\xi^{\*}\_{\cdot}\big)^{\mathbb{F}^{2}}\_{t}. |  |

Then, the following properties hold:

* (i)

  𝖯​(Yt1≤0​ and ​Yt2≥0​ for all t∈[0,T])=1\mathsf{P}\big(Y^{1}\_{t}\leq 0\text{ and }Y^{2}\_{t}\geq 0\text{ for all $t\in[0,T]$}\big)=1.
* (ii)

  We have

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (3.57) |  | ∫[0,T]Yt1​dξt∗=0and∫[0,T]Yt2​dζt∗=0,\displaystyle\int\_{[0,T]}Y^{1}\_{t}\mathrm{d}\xi^{\*}\_{t}=0\quad\text{and}\quad\int\_{[0,T]}Y^{2}\_{t}\mathrm{d}\zeta^{\*}\_{t}=0, |  |

  or, equivalently,

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (3.58) |  | ∫[0,T]𝟏{Yt1<0}​dξt∗=0and∫[0,T]𝟏{Yt2>0}​dζt∗=0.\displaystyle\int\_{[0,T]}\mathbf{1}\_{\{Y^{1}\_{t}<0\}}\mathrm{d}\xi^{\*}\_{t}=0\quad\text{and}\quad\int\_{[0,T]}\mathbf{1}\_{\{Y^{2}\_{t}>0\}}\mathrm{d}\zeta^{\*}\_{t}=0. |  |

###### Proof.

Taking τ=θ\tau=\theta and σ=γ\sigma=\gamma on the right-hand side of ([3.4](https://arxiv.org/html/2510.15616v1#S3.E4 "In Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), we have Yθ1≤0Y^{1}\_{\theta}\leq 0 and Yγ2≥0Y^{2}\_{\gamma}\geq 0 for arbitrary stopping times θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}) and γ∈𝒯0​(𝔽2)\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}). Since the process Y1Y^{1} and Y2Y^{2} are optional with respect to 𝔽1\mathbb{F}^{1} and 𝔽2\mathbb{F}^{2}, respectively, then (i) holds by repeating arguments in the proof of [[RW00](https://arxiv.org/html/2510.15616v1#bib.bibx39), Lemma VI.5.2] with the set FF therein replaced by {(t,ω):Yt1​(ω)>0}\{(t,\omega):\ Y^{1}\_{t}(\omega)>0\} and {(t,ω):Yt2​(ω)<0}\{(t,\omega):\ Y^{2}\_{t}(\omega)<0\}, respectively.

To prove (ii), let (zn)n∈ℕ⊂[0,1](z\_{n})\_{n\in\mathbb{N}}\subset[0,1] with zn↑1z\_{n}\uparrow 1 be such that (mt∗​(zn))t∈[0,T](m^{\*}\_{t}(z\_{n}))\_{t\in[0,T]} is a càdlàg 𝔽1\mathbb{F}^{1}-martingale and (nt∗​(zn))t∈[0,T](n^{\*}\_{t}(z\_{n}))\_{t\in[0,T]} is a càdlàg 𝔽2\mathbb{F}^{2}-martingale for each n∈ℕn\in\mathbb{N}. By definition of σ∗​(z)\sigma\_{\*}(z) and τ∗​(z)\tau\_{\*}(z) we have σ∗​(zn)≤σ∗​(zn+1)\sigma\_{\*}(z\_{n})\leq\sigma\_{\*}(z\_{n+1}) and τ∗​(zn)≤τ∗​(zn+1)\tau\_{\*}(z\_{n})\leq\tau\_{\*}(z\_{n+1}), with σ∗​(zn),τ∗​(zn)↑σ∗​(1),τ∗​(1)\sigma\_{\*}(z\_{n}),\tau\_{\*}(z\_{n})\uparrow\sigma\_{\*}(1),\tau\_{\*}(1) as defined in ([3.11](https://arxiv.org/html/2510.15616v1#S3.E11 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) (recall that we skip bars in the notation for the sake of readability).

Now we focus on the support of ξ∗\xi^{\*} as the result for ζ∗\zeta^{\*} can be obtained analogously.
By optional sampling 𝖤​[m0∗​(zn)]=𝖤​[mτ∗​(u)∗​(zn)]\mathsf{E}[m^{\*}\_{0}(z\_{n})]=\mathsf{E}[m^{\*}\_{\tau\_{\*}(u)}(z\_{n})] for any u∈[0,1]u\in[0,1]. Hence, integrating over [0,zn][0,z\_{n}] yields

|  |  |  |  |
| --- | --- | --- | --- |
| (3.59) |  | 𝖤​[m0∗​(zn)]=1zn​∫0zn𝖤​[mτ∗​(u)∗​(zn)]​du.\displaystyle\mathsf{E}\big[m^{\*}\_{0}(z\_{n})\big]=\frac{1}{z\_{n}}\int\_{0}^{z\_{n}}\mathsf{E}\big[m^{\*}\_{\tau\_{\*}(u)}(z\_{n})\big]\mathrm{d}u. |  |

From the definition of mt∗​(z)m^{\*}\_{t}(z) we have

|  |  |  |  |
| --- | --- | --- | --- |
| (3.60) |  | 𝖤​[m0∗​(zn)]=𝖤​[V^0∗,1]=𝖤​[V∗,1​(0)]=𝖤​[∫[0,T)(ft​(1−ζt∗)+ht​Δ​ζt∗)​dξt∗+∫[0,T)gt​(1−ξt∗)​dζt∗+hT​Δ​ζT∗​Δ​ξT∗].\displaystyle\begin{aligned} &\mathsf{E}[m^{\*}\_{0}(z\_{n})]=\mathsf{E}[\hat{V}^{\*,1}\_{0}]=\mathsf{E}[V^{\*,1}(0)]\\ &=\mathsf{E}\Big[\int\_{[0,T)}\big(f\_{t}(1-\zeta^{\*}\_{t})+h\_{t}\Delta\zeta^{\*}\_{t}\big)\mathrm{d}\xi^{\*}\_{t}+\int\_{[0,T)}g\_{t}(1-\xi^{\*}\_{t})\mathrm{d}\zeta^{\*}\_{t}+h\_{T}\Delta\zeta^{\*}\_{T}\Delta\xi^{\*}\_{T}\Big].\end{aligned} |  |

It is important to notice that the expression is independent of znz\_{n}.
For u≤znu\leq z\_{n}, using that τ∗​(u)≤τ∗​(zn)\tau\_{\*}(u)\leq\tau\_{\*}(z\_{n}) we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[mτ∗​(u)∗​(zn)]=𝖤​[𝟏{σ∗<τ∗​(u)}​gσ∗+V^τ∗​(u)∗,1]=𝖤​[∫[0,τ∗​(u))gt​dζt∗+V^τ∗​(u)∗,1​𝟏{τ∗​(u)<T}+hT​Δ​ζT∗​𝟏{τ∗​(u)=T}],\displaystyle\begin{aligned} \mathsf{E}[m^{\*}\_{\tau\_{\*}(u)}(z\_{n})]&=\mathsf{E}\big[\mathbf{1}\_{\{\sigma\_{\*}<\tau\_{\*}(u)\}}g\_{\sigma\_{\*}}+\hat{V}^{\*,1}\_{\tau\_{\*}(u)}\big]\\ &=\mathsf{E}\Big[\int\_{[0,\tau\_{\*}(u))}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\hat{V}^{\*,1}\_{\tau\_{\*}(u)}\mathbf{1}\_{\{\tau\_{\*}(u)<T\}}+h\_{T}\Delta\zeta^{\*}\_{T}\mathbf{1}\_{\{\tau\_{\*}(u)=T\}}\Big],\end{aligned} |  |

where for the second equality we integrated out the randomisation device of σ∗\sigma\_{\*} and we used that V^T∗,1=𝖤​[hT​Δ​ζT∗|ℱT1]\hat{V}^{\*,1}\_{T}=\mathsf{E}[h\_{T}\Delta\zeta^{\*}\_{T}|\mathcal{F}^{1}\_{T}], along with tower property. Integrating over u∈[0,zn]u\in[0,z\_{n}] yields

|  |  |  |  |
| --- | --- | --- | --- |
| (3.61) |  | ∫0zn𝖤​[mτ∗​(u)∗​(zn)]​du=𝖤​[∫[0,T)(zn−ξt∗)+​gt​dζt∗+∫[0,T∧τ∗​(zn))V^t∗,1​dξt∗+hT​Δ​ζT∗​(zn−ξT−∗)+],\displaystyle\begin{aligned} &\int\_{0}^{z\_{n}}\mathsf{E}[m^{\*}\_{\tau\_{\*}(u)}(z\_{n})]\mathrm{d}u\\ &=\mathsf{E}\Big[\int\_{[0,T)}(z\_{n}-\xi^{\*}\_{t})^{+}g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\int\_{[0,T\wedge\tau\_{\*}(z\_{n}))}\hat{V}^{\*,1}\_{t}\mathrm{d}\xi^{\*}\_{t}+h\_{T}\Delta\zeta^{\*}\_{T}(z\_{n}-\xi^{\*}\_{T-})^{+}\Big],\end{aligned} |  |

where we used the following formulae:

|  |  |  |
| --- | --- | --- |
|  | ∫0zn(∫[0,T)𝟏{t<τ∗​(u)}​gt​dζt∗)​du=∫[0,T)(∫0zn𝟏{ξt∗<u}​du)​gt​dζt∗=∫[0,T)(zn−ξt∗)+​gt​dζt∗,\displaystyle\int\_{0}^{z\_{n}}\Big(\int\_{[0,T)}\mathbf{1}\_{\{t<\tau\_{\*}(u)\}}g\_{t}\mathrm{d}\zeta^{\*}\_{t}\Big)\mathrm{d}u=\int\_{[0,T)}\Big(\int\_{0}^{z\_{n}}\mathbf{1}\_{\{\xi^{\*}\_{t}<u\}}\mathrm{d}u\Big)g\_{t}\mathrm{d}\zeta^{\*}\_{t}=\int\_{[0,T)}(z\_{n}-\xi^{\*}\_{t})^{+}g\_{t}\mathrm{d}\zeta^{\*}\_{t}, |  |
|  |  |  |
| --- | --- | --- |
|  | ∫0zn𝟏{τ∗​(u)=T}​du=∫0zn𝟏{ξT−∗<u}​du=(zn−ξT−∗)+.\displaystyle\int\_{0}^{z\_{n}}\mathbf{1}\_{\{\tau\_{\*}(u)=T\}}\mathrm{d}u=\int\_{0}^{z\_{n}}\mathbf{1}\_{\{\xi^{\*}\_{T-}<u\}}\mathrm{d}u=(z\_{n}-\xi^{\*}\_{T-})^{+}. |  |

Finally, inserting ([3.60](https://arxiv.org/html/2510.15616v1#S3.E60 "In 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and ([3.61](https://arxiv.org/html/2510.15616v1#S3.E61 "In 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) into ([3.59](https://arxiv.org/html/2510.15616v1#S3.E59 "In 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and letting n→∞n\to\infty yields

|  |  |  |  |
| --- | --- | --- | --- |
| (3.62) |  | 𝖤​[∫[0,T)(ft​(1−ζt∗)+ht​Δ​ζt∗)​dξt∗+∫[0,T)gt​(1−ξt∗)​dζt∗+hT​Δ​ζT∗​Δ​ξT∗]=𝖤​[∫[0,T)(1−ξt∗)​gt​dζt∗+∫[0,T)V^t∗,1​dξt∗+hT​Δ​ζT∗​Δ​ξT∗],\displaystyle\begin{aligned} &\mathsf{E}\Big[\int\_{[0,T)}\big(f\_{t}(1-\zeta^{\*}\_{t})+h\_{t}\Delta\zeta^{\*}\_{t}\big)\mathrm{d}\xi^{\*}\_{t}+\int\_{[0,T)}g\_{t}(1-\xi^{\*}\_{t})\mathrm{d}\zeta^{\*}\_{t}+h\_{T}\Delta\zeta^{\*}\_{T}\Delta\xi^{\*}\_{T}\Big]\\ &=\mathsf{E}\Big[\int\_{[0,T)}(1-\xi^{\*}\_{t})g\_{t}\mathrm{d}\zeta^{\*}\_{t}+\int\_{[0,T)}\hat{V}^{\*,1}\_{t}\mathrm{d}\xi^{\*}\_{t}+h\_{T}\Delta\zeta^{\*}\_{T}\Delta\xi^{\*}\_{T}\Big],\end{aligned} |  |

where we used that

|  |  |  |
| --- | --- | --- |
|  | ∫[0,T∧τ∗​(zn))V^t∗,1​dξt∗→n→∞∫[0,T∧τ∗​(1))V^t∗,1​dξt∗=∫[0,T)V^t∗,1​dξt∗,\int\_{[0,T\wedge\tau\_{\*}(z\_{n}))}\hat{V}^{\*,1}\_{t}\mathrm{d}\xi^{\*}\_{t}\xrightarrow{n\to\infty}\int\_{[0,T\wedge\tau\_{\*}(1))}\hat{V}^{\*,1}\_{t}\mathrm{d}\xi^{\*}\_{t}=\int\_{[0,T)}\hat{V}^{\*,1}\_{t}\mathrm{d}\xi^{\*}\_{t}, |  |

and the final equality above holds because ξt∗​(ω)=1\xi^{\*}\_{t}(\omega)=1 for t≥τ∗​(1)​(ω)t\geq\tau\_{\*}(1)(\omega).

From ([3.62](https://arxiv.org/html/2510.15616v1#S3.E62 "In 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and using optional projections and [[DM83](https://arxiv.org/html/2510.15616v1#bib.bibx16), Thm. VI.57] we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =𝖤​[∫[0,T)(V^t∗,1−ft​(1−ζt∗)−ht​Δ​ζt∗)​dξt∗]\displaystyle=\mathsf{E}\Big[\int\_{[0,T)}\big(\hat{V}^{\*,1}\_{t}-f\_{t}(1-\zeta^{\*}\_{t})-h\_{t}\Delta\zeta^{\*}\_{t}\big)\mathrm{d}\xi^{\*}\_{t}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖤[∫[0,T)(V^t∗,1−[(of⋅(1−ζ⋅∗))t𝔽1+(oh⋅Δζ⋅∗)t𝔽1]dξt∗]=𝖤[∫[0,T)Yt1dξt∗].\displaystyle=\mathsf{E}\Big[\int\_{[0,T)}\big(\hat{V}^{\*,1}\_{t}-\big[\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}f\_{\cdot}(1-\zeta^{\*}\_{\cdot})\big)\_{t}^{\mathbb{F}^{1}}+\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}h\_{\cdot}\Delta\zeta^{\*}\_{\cdot}\big)\_{t}^{\mathbb{F}^{1}}\big]\mathrm{d}\xi^{\*}\_{t}\Big]=\mathsf{E}\Big[\int\_{[0,T)}Y^{1}\_{t}\mathrm{d}\xi^{\*}\_{t}\Big]. |  |

Since we know that Yt1≤0Y^{1}\_{t}\leq 0 for all t∈[0,T]t\in[0,T], 𝖯\mathsf{P}-a.s. (item (i) above) then we conclude that the first equation in ([3.57](https://arxiv.org/html/2510.15616v1#S3.E57 "In item (ii) ‣ Proposition 3.17. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) must hold. The other one can be obtained by analogous methods and using Yt2≥0Y^{2}\_{t}\geq 0 for all t∈[0,T]t\in[0,T], 𝖯\mathsf{P}-a.s.
∎

###### Remark 3.18.

We can rephrase Proposition [3.17](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem17 "Proposition 3.17. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") using that the pair (τ∗,σ∗)(\tau\_{\*},\sigma\_{\*}) is generated by (ξ∗,ζ∗)(\xi^{\*},\zeta^{\*}) and therefore writing the processes Y1Y^{1} and Y2Y^{2} as

|  |  |  |
| --- | --- | --- |
|  | Yt1=V^t∗,1−(of⋅𝟏{σ∗>⋅})t𝔽1−(oh⋅𝟏{σ∗=⋅})t𝔽1andYt2=V^t∗,2−(og⋅𝟏{τ∗>⋅})t𝔽2−(oh⋅𝟏{τ∗=⋅})t𝔽2.\displaystyle Y^{1}\_{t}=\hat{V}^{\*,1}\_{t}-\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}f\_{\cdot}\mathbf{1}\_{\{\sigma\_{\*}>\,\cdot\}}\big)\_{t}^{\mathbb{F}^{1}}-\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}h\_{\cdot}\mathbf{1}\_{\{\sigma\_{\*}=\,\cdot\}}\big)\_{t}^{\mathbb{F}^{1}}\quad\text{and}\quad Y^{2}\_{t}=\hat{V}^{\*,2}\_{t}-\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}g\_{\cdot}\mathbf{1}\_{\{\tau\_{\*}>\,\cdot\}}\big)^{\mathbb{F}^{2}}\_{t}-\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}h\_{\cdot}\mathbf{1}\_{\{\tau\_{\*}=\,\cdot\}}\big)^{\mathbb{F}^{2}}\_{t}. |  |

Moreover, adopting a terminology for local-times of càdlàg semimartingales (cf. [[Pro05](https://arxiv.org/html/2510.15616v1#bib.bibx37), Thm. IV.7.69]) we can informally state (ii) in the above proposition by saying that the measure associated to the process t↦ξt∗​(ω)t\mapsto\xi^{\*}\_{t}(\omega) is carried by the set {t∈[0,T]:Yt1​(ω)=0}\{t\in[0,T]:Y^{1}\_{t}(\omega)=0\}, for 𝖯\mathsf{P}-a.e. ω∈Ω\omega\in\Omega. Analogously, the measure associated to the process t↦ζt∗​(ω)t\mapsto\zeta^{\*}\_{t}(\omega) is carried by the set {t∈[0,T]:Yt2​(ω)=0}\{t\in[0,T]:Y^{2}\_{t}(\omega)=0\} for 𝖯\mathsf{P}-a.e. ω∈Ω\omega\in\Omega.

Proposition [3.17](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem17 "Proposition 3.17. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") yields a characterisation of “when” the optimal randomised strategies should “activate” but it does not quantify the “amount” of stopping which is required (i.e., with what speed should the generating processes increase). This is a very difficult issue to address in general and the answer depends on the particular structure of the game. We address the question in the next corollary which should hold, in spirit, in a broader generality than its actual statement. The corollary was used in [[Smi24](https://arxiv.org/html/2510.15616v1#bib.bibx41), Ch. 6] to construct equilibrium strategies in the game proposed by [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12), Sec. 6.2] and in the working paper [[DAHP25](https://arxiv.org/html/2510.15616v1#bib.bibx11)]. Moreover, it was implicitly used in the construction of the equilibrium strategies of [[DAEG22](https://arxiv.org/html/2510.15616v1#bib.bibx9)].

Let us make a preliminary observation that V^0∗,1=M00\hat{V}^{\*,1}\_{0}=M^{0}\_{0} and V^0∗,1=N00\hat{V}^{\*,1}\_{0}=N^{0}\_{0}.

###### Corollary 3.19.

Assume that the processes

|  |  |  |  |
| --- | --- | --- | --- |
| (3.63) |  | t↦(o∫[0,⋅)gsdζs∗)t∧τ∗​(z)𝔽1andt↦(o∫[0,⋅)fsdξs∗)t∧σ∗​(z)𝔽2\displaystyle\begin{aligned} &t\mapsto\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}\int\_{[0,\,\cdot)}g\_{s}\mathrm{d}\zeta^{\*}\_{s}\Big)^{\mathbb{F}^{1}}\_{t\wedge\tau\_{\*}(z)}\quad\text{and}\quad t\mapsto\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}\int\_{[0,\,\cdot)}f\_{s}\mathrm{d}\xi^{\*}\_{s}\Big)^{\mathbb{F}^{2}}\_{t\wedge\sigma\_{\*}(z)}\end{aligned} |  |

are of bounded variation and continuous for z∈[0,1]z\in[0,1]. Then, for z∈[0,1)z\in[0,1) the processes t↦V^t∧τ∗​(z)∗,1t\mapsto\hat{V}^{\*,1}\_{t\wedge\tau\_{\*}(z)} and t↦V^t∧σ∗​(z)∗,2t\mapsto\hat{V}^{\*,2}\_{t\wedge\sigma\_{\*}(z)} are càdlàg with semimartingale decompositions given by

|  |  |  |
| --- | --- | --- |
|  | V^t∧τ∗​(z)∗,1=V^0∗,1+At1+Bt1andV^t∧σ∗​(z)∗,2=V^0∗,2+At2+Bt2,\hat{V}^{\*,1}\_{t\wedge\tau\_{\*}(z)}=\hat{V}^{\*,1}\_{0}+A^{1}\_{t}+B^{1}\_{t}\quad\text{and}\quad\hat{V}^{\*,2}\_{t\wedge\sigma\_{\*}(z)}=\hat{V}^{\*,2}\_{0}+A^{2}\_{t}+B^{2}\_{t}, |  |

where AiA^{i} is the previsible bounded variation part and BiB^{i} the martingale part, with

|  |  |  |  |
| --- | --- | --- | --- |
| (3.64) |  | At1=−(o∫[0,⋅)gsdζs∗)t∧τ∗​(z)𝔽1andBt1=Mt∧τ∗​(z)0−M00,At2=−(o∫[0,⋅)fsdξs∗)t∧σ∗​(z)𝔽2andBt2=Nt∧σ∗​(z)0−N00.\displaystyle\begin{aligned} &A^{1}\_{t}=-\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}\int\_{[0,\,\cdot)}g\_{s}\mathrm{d}\zeta^{\*}\_{s}\Big)^{\mathbb{F}^{1}}\_{t\wedge\tau\_{\*}(z)}\quad\text{and}\quad B^{1}\_{t}=M^{0}\_{t\wedge\tau\_{\*}(z)}-M^{0}\_{0},\\ &A^{2}\_{t}=-\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}\int\_{[0,\,\cdot)}f\_{s}\mathrm{d}\xi^{\*}\_{s}\Big)^{\mathbb{F}^{2}}\_{t\wedge\sigma\_{\*}(z)}\quad\text{and}\quad B^{2}\_{t}=N^{0}\_{t\wedge\sigma\_{\*}(z)}-N^{0}\_{0}.\end{aligned} |  |

###### Proof.

Let us start by noticing that for any θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}) it holds

|  |  |  |
| --- | --- | --- |
|  | (o∫[0,⋅)gsdζs∗)θ𝔽1=𝖤[∫[0,θ)gsdζs∗|ℱθ1]=𝖤[𝟏{σ∗<θ}gσ∗|ℱθ1].\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}\int\_{[0,\,\cdot)}g\_{s}\mathrm{d}\zeta^{\*}\_{s}\Big)^{\mathbb{F}^{1}}\_{\theta}=\mathsf{E}\Big[\int\_{[0,\theta)}g\_{s}\mathrm{d}\zeta^{\*}\_{s}\Big|\mathcal{F}^{1}\_{\theta}\Big]=\mathsf{E}\big[\mathbf{1}\_{\{\sigma\_{\*}<\theta\}}g\_{\sigma\_{\*}}\big|\mathcal{F}^{1}\_{\theta}\big]. |  |

By Corollary [3.16](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem16 "Corollary 3.16. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), for any z∈[0,1)z\in[0,1), the process (Mt∧τ∗​(z)0)t∈[0,T](M^{0}\_{t\wedge\tau\_{\*}(z)})\_{t\in[0,T]} is a càdlàg 𝔽1\mathbb{F}^{1}-martingale and (see Eq. ([3.56](https://arxiv.org/html/2510.15616v1#S3.E56 "In 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")))

|  |  |  |
| --- | --- | --- |
|  | Mt∧τ∗​(z)0=(o∫[0,⋅)gsdζs∗)t∧τ∗​(z)𝔽1+V^t∧τ∗​(z)∗,1.\displaystyle M^{0}\_{t\wedge\tau\_{\*}(z)}=\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}\int\_{[0,\,\cdot)}g\_{s}\mathrm{d}\zeta^{\*}\_{s}\Big)^{\mathbb{F}^{1}}\_{t\wedge\tau\_{\*}(z)}+\hat{V}^{\*,1}\_{t\wedge\tau\_{\*}(z)}. |  |

We know from Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") that t↦V^t∧τ∗​(z)∗,1t\mapsto\hat{V}^{\*,1}\_{t\wedge\tau\_{\*}(z)} is an 𝔽1\mathbb{F}^{1}-optional semi-martingale. The above equality proves that it is actually càdlàg, by the assumed continuity of the processes in ([3.63](https://arxiv.org/html/2510.15616v1#S3.E63 "In Corollary 3.19. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")). Rearranging terms we express V^t∧τ∗​(z)∗,1\hat{V}^{\*,1}\_{t\wedge\tau\_{\*}(z)} as

|  |  |  |
| --- | --- | --- |
|  | V^t∧τ∗​(z)∗,1=M00+[Mt∧τ∗​(z)0−M00]−(o∫[0,⋅)gsdζs∗)t∧τ∗​(z)𝔽1.\hat{V}^{\*,1}\_{t\wedge\tau\_{\*}(z)}=M^{0}\_{0}+\big[M^{0}\_{t\wedge\tau\_{\*}(z)}-M^{0}\_{0}\big]-\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}\int\_{[0,\,\cdot)}g\_{s}\mathrm{d}\zeta^{\*}\_{s}\Big)^{\mathbb{F}^{1}}\_{t\wedge\tau\_{\*}(z)}. |  |

Since (o∫[0,⋅)gsdζs∗)t∧τ∗​(z)𝔽1\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-7.64214pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\Big(}^{{\kern-6.96352pt{o}\kern 5.22224pt}}\_{{\kern-4.767pt\kern 5.22224pt}}}\int\_{[0,\,\cdot)}g\_{s}\mathrm{d}\zeta^{\*}\_{s}\Big)^{\mathbb{F}^{1}}\_{t\wedge\tau\_{\*}(z)} is previsible and of bounded variation, then the above formula determines uniquely the Doob-Meyer’s decomposition of V^t∧τ∗​(z)∗,1\hat{V}^{\*,1}\_{t\wedge\tau\_{\*}(z)} by, e.g., [[Pro05](https://arxiv.org/html/2510.15616v1#bib.bibx37), Thm. III.1.2].
The argument for V^∗,2\hat{V}^{\*,2} is analogous.
∎

In a nutshell, the corollary establishes a link between the optimal control ζt∗\zeta^{\*}\_{t} (resp. ξt∗\xi^{\*}\_{t}) and the bounded variation part of the Doob-Meyer decomposition of V^t∗,2\hat{V}^{\*,2}\_{t} (resp. V^t∗,1\hat{V}^{\*,1}\_{t}). When the latter is known (e.g., by PDE results in a Markovian framework) one may use the corollary to identify the optimal speed of increase for the generating process ζ∗\zeta^{\*} (resp. ξ∗\xi^{\*}).

The reader is referred to Section [5](https://arxiv.org/html/2510.15616v1#S5 "5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") to appreciate how the necessary conditions presented in this section enable us to make significant insights into two classes of games with asymmetric information. These insights pave the way for the solution of specific games by identifying objects to be modelled (player values, beliefs) as well as the structure of optimal strategies.

## 4. Sufficient conditions for a saddle point

In this section we will formulate a verification result, i.e., a set of sufficient conditions for a saddle point and the value of the game. These conditions closely resemble the necessary conditions derived earlier in this paper. Indeed,
upon close inspection, results of the previous section show that the sufficient conditions formulated below are also necessary.
To facilitate such comparisons, we employ notations aligned with those used for the necessary conditions.

The fact that our verification theorems provide conditions which are also necessary shows that these conditions are optimal, i.e., cannot be relaxed any further.
This emphasises the completeness of our derivation of necessary conditions and the strength of the sufficient conditions. We present various equivalent sets of sufficient conditions,
so that the reader may choose the most convenient one for their own specific application.

###### Remark 4.1.

The assumptions for this section can be relaxed compared to the rest of the paper and we no longer require the ordering of the payoff processes f≥h≥gf\geq h\geq g.

We start with a definition of 𝒯0\mathcal{T}\_{0} sub- and supermartingale systems, analogues of 𝐌ξ{\bf M}^{\xi} and 𝐍ζ{\bf N}^{\zeta} from Section [3.1](https://arxiv.org/html/2510.15616v1#S3.SS1 "3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). Fix a pair (ξ^,ζ^)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\hat{\xi},\hat{\zeta})\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}), an 𝔽1\mathbb{F}^{1}-progressively measurable process (𝒰t1)t∈[0,T](\mathcal{U}^{1}\_{t})\_{t\in[0,T]} and an 𝔽2\mathbb{F}^{2}-progressively measurable process (𝒰t2)t∈[0,T](\mathcal{U}^{2}\_{t})\_{t\in[0,T]}.
For any (ξ,ζ)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\xi,\zeta)\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}), consider the families 𝐌^ξ≔{M^ξ​(θ),θ∈𝒯0​(𝔽1)}\hat{\bf M}^{\xi}\coloneqq\{\hat{M}^{\xi}(\theta),\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})\} and 𝐍^ζ≔{N^ζ​(γ),γ∈𝒯0​(𝔽2)}\hat{\bf N}^{\zeta}\coloneqq\{\hat{N}^{\zeta}(\gamma),\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2})\} defined by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.1) |  | M^ξ​(θ)\displaystyle\hat{M}^{\xi}(\theta) | =𝖤​[∫[0,θ)ft​(1−ζ^t)​dξt+∫[0,θ)gt​(1−ξt)​dζ^t+∑t∈[0,θ)ht​Δ​ξt​Δ​ζ^t|ℱθ1]\displaystyle=\mathsf{E}\Big[\!\int\_{[0,\theta)}\!\!f\_{t}(1\!-\!\hat{\zeta}\_{t})\mathrm{d}\xi\_{t}\!+\!\int\_{[0,\theta)}\!\!g\_{t}(1\!-\!\xi\_{t})\mathrm{d}\hat{\zeta}\_{t}\!+\!\!\sum\_{t\in[0,\theta)}\!\!h\_{t}\Delta\xi\_{t}\Delta\hat{\zeta}\_{t}\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−ξθ−)​𝖤​[1−ζ^θ−|ℱθ1]​𝒰θ1,\displaystyle\quad+\!(1\!-\!\xi\_{\theta-})\mathsf{E}[1\!-\!\hat{\zeta}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]\mathcal{U}^{1}\_{\theta}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.2) |  | N^ζ​(γ)\displaystyle\hat{N}^{\zeta}(\gamma) | =𝖤​[∫[0,γ)ft​(1−ζt)​dξ^t+∫[0,γ)gt​(1−ξ^t)​dζt+∑t∈[0,γ)ht​Δ​ξ^t​Δ​ζt|ℱγ2]\displaystyle=\mathsf{E}\Big[\!\int\_{[0,\gamma)}\!\!f\_{t}(1\!-\!\zeta\_{t})\mathrm{d}\hat{\xi}\_{t}\!+\!\int\_{[0,\gamma)}\!\!g\_{t}(1\!-\!\hat{\xi}\_{t})\mathrm{d}\zeta\_{t}\!+\!\!\sum\_{t\in[0,\gamma)}\!\!h\_{t}\Delta\hat{\xi}\_{t}\Delta\zeta\_{t}\Big|\mathcal{F}^{2}\_{\gamma}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝖤​[1−ξ^γ−|ℱγ2]​(1−ζγ−)​𝒰γ2.\displaystyle\quad+\!\mathsf{E}[1\!-\!\hat{\xi}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}](1\!-\!\zeta\_{\gamma-})\mathcal{U}^{2}\_{\gamma}. |  |

We start with a sequence of results which bear the strongest similarity to the necessary conditions developed in the previous section. We will follow those with stronger results that allow identification of the saddle point of the game – the main aim is to replace arbitrary generating processes (ξ,ζ)(\xi,\zeta) with stopping times.

###### Theorem 4.2.

Let (𝒰t1)t∈[0,T](\mathcal{U}^{1}\_{t})\_{t\in[0,T]} and (𝒰t2)t∈[0,T](\mathcal{U}^{2}\_{t})\_{t\in[0,T]} be 𝔽1\mathbb{F}^{1}- and 𝔽2\mathbb{F}^{2}-progressively measurable process, respectively, and let (ξ^,ζ^)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\hat{\xi},\hat{\zeta})\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}). Assume that

1. (i)

   𝐌^ξ\hat{\bf M}^{\xi} is a 𝒯0​(𝔽1)\mathcal{T}\_{0}(\mathbb{F}^{1})-submartingale system for any ξ∈𝒜0∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1}),
2. (ii)

   𝐍^ζ\hat{\bf N}^{\zeta} is a 𝒯0​(𝔽2)\mathcal{T}\_{0}(\mathbb{F}^{2})-supermartingale system for any ζ∈𝒜0∘​(𝔽2)\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}),
3. (iii)

   𝖤​[Δ​ζ^T|ℱT1]​𝒰T1=𝖤​[Δ​ζ^T​hT|ℱT1]\mathsf{E}[\Delta\hat{\zeta}\_{T}|\mathcal{F}^{1}\_{T}]\,\mathcal{U}^{1}\_{T}=\mathsf{E}[\Delta\hat{\zeta}\_{T}h\_{T}|\mathcal{F}^{1}\_{T}] and 𝖤​[Δ​ξ^T|ℱT2]​𝒰T2=𝖤​[Δ​ξ^T​hT|ℱT2]\mathsf{E}[\Delta\hat{\xi}\_{T}|\mathcal{F}^{2}\_{T}]\,\mathcal{U}^{2}\_{T}=\mathsf{E}[\Delta\hat{\xi}\_{T}h\_{T}|\mathcal{F}^{2}\_{T}],
4. (iv)

   𝖤​[𝒰01]=𝖤​[𝒰02]\mathsf{E}[\mathcal{U}^{1}\_{0}]=\mathsf{E}[\mathcal{U}^{2}\_{0}].

Then the game has a value, i.e., V¯=V¯=𝖤​[𝒰01]=𝖤​[𝒰02]\overline{V}=\underline{V}=\mathsf{E}[\mathcal{U}^{1}\_{0}]=\mathsf{E}[\mathcal{U}^{2}\_{0}], see ([2.2](https://arxiv.org/html/2510.15616v1#S2.E2 "In 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")), and the randomised stopping times (τ^,σ^)∈𝒯0R​(𝔽1)×𝒯0R​(𝔽2)(\hat{\tau},\hat{\sigma})\in\mathcal{T}^{R}\_{0}(\mathbb{F}^{1})\times\mathcal{T}^{R}\_{0}(\mathbb{F}^{2}) generated by (ξ^,ζ^)(\hat{\xi},\hat{\zeta}) form a saddle point of the game.

###### Proof.

Let ξ∈𝒜0∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1}). By the submartingale property of 𝐌^ξ\hat{\bf M}^{\xi}, we have 𝖤​[M^ξ​(T)|ℱ01]≥M^ξ​(0)\mathsf{E}[\hat{M}^{\xi}(T)|\mathcal{F}^{1}\_{0}]\geq\hat{M}^{\xi}(0). Expanding the left- and right-hand sides from the definition ([4.1](https://arxiv.org/html/2510.15616v1#S4.E1 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), we have

|  |  |  |  |
| --- | --- | --- | --- |
| (4.3) |  | 𝖤​[∫[0,T)ft​(1−ζ^t)​dξt+∫[0,T)gt​(1−ξt)​dζ^t+∑t∈[0,T)ht​Δ​ξt​Δ​ζ^t+(1−ξT−)​𝖤​[1−ζ^T−|ℱT1]​𝒰T1|ℱ01]≥𝒰01.\mathsf{E}\Big[\!\int\_{[0,T)}\!\!f\_{t}(1\!-\!\hat{\zeta}\_{t})\mathrm{d}\xi\_{t}\!+\!\int\_{[0,T)}\!\!g\_{t}(1\!-\!\xi\_{t})\mathrm{d}\hat{\zeta}\_{t}\!+\!\!\sum\_{t\in[0,T)}\!\!h\_{t}\Delta\xi\_{t}\Delta\hat{\zeta}\_{t}\!+\!(1\!-\!\xi\_{T-})\mathsf{E}[1\!-\!\hat{\zeta}\_{T-}|\mathcal{F}^{1}\_{T}]\mathcal{U}^{1}\_{T}\Big|\mathcal{F}^{1}\_{0}\Big]\geq\mathcal{U}^{1}\_{0}. |  |

We note that 1−ξT−=Δ​ξT1-\xi\_{T-}=\Delta\xi\_{T} and 1−ζT−=Δ​ζT1-\zeta\_{T-}=\Delta\zeta\_{T}, and use assumption (iii) of the theorem to simplify the last term on the left:

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[(1−ξT−)​𝖤​[1−ζ^T−|ℱT1]​𝒰T1|ℱ01]=𝖤​[Δ​ξT​𝖤​[Δ​ζ^T|ℱT1]​𝒰T1|ℱ01]=𝖤​[Δ​ξT​Δ​ζ^T​hT|ℱ01].\mathsf{E}\big[(1\!-\!\xi\_{T-})\mathsf{E}[1\!-\!\hat{\zeta}\_{T-}|\mathcal{F}^{1}\_{T}]\,\mathcal{U}^{1}\_{T}\big|\mathcal{F}^{1}\_{0}\big]=\mathsf{E}\big[\Delta\xi\_{T}\,\mathsf{E}[\Delta\hat{\zeta}\_{T}|\mathcal{F}^{1}\_{T}]\,\mathcal{U}^{1}\_{T}\big|\mathcal{F}^{1}\_{0}\big]=\mathsf{E}\big[\Delta\xi\_{T}\Delta\hat{\zeta}\_{T}h\_{T}\big|\mathcal{F}^{1}\_{0}\big]. |  |

Inserting this into ([4.3](https://arxiv.org/html/2510.15616v1#S4.E3 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) yields

|  |  |  |  |
| --- | --- | --- | --- |
| (4.4) |  | 𝖤​[𝒫​(ξ,ζ^)|ℱ01]≥𝒰01,for any ξ∈𝒜0∘​(𝔽1).\mathsf{E}[\mathcal{P}(\xi,\hat{\zeta})|\mathcal{F}^{1}\_{0}]\geq\mathcal{U}^{1}\_{0},\qquad\text{for any $\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})$.} |  |

In an analogous way, we show

|  |  |  |  |
| --- | --- | --- | --- |
| (4.5) |  | 𝖤​[𝒫​(ξ^,ζ)|ℱ02]≤𝒰02,for any ζ∈𝒜0∘​(𝔽2).\mathsf{E}[\mathcal{P}(\hat{\xi},\zeta)|\mathcal{F}^{2}\_{0}]\leq\mathcal{U}^{2}\_{0},\qquad\text{for any $\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2})$.} |  |

Taking expectation on both sides of ([4.4](https://arxiv.org/html/2510.15616v1#S4.E4 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"))-([4.5](https://arxiv.org/html/2510.15616v1#S4.E5 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) with (ξ,ζ)=(ξ^,ζ^)(\xi,\zeta)=(\hat{\xi},\hat{\zeta}), and applying condition (iv) of the theorem yields

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[𝒫​(ξ^,ζ^)]≥𝖤​[𝒰01]=𝖤​[𝒰02]≥𝖤​[𝒫​(ξ^,ζ^)],\mathsf{E}[\mathcal{P}(\hat{\xi},\hat{\zeta})]\geq\mathsf{E}[\mathcal{U}^{1}\_{0}]=\mathsf{E}[\mathcal{U}^{2}\_{0}]\geq\mathsf{E}[\mathcal{P}(\hat{\xi},\hat{\zeta})], |  |

so that 𝖤​[𝒫​(ξ^,ζ^)]=𝖤​[𝒰01]=𝖤​[𝒰02]\mathsf{E}[\mathcal{P}(\hat{\xi},\hat{\zeta})]=\mathsf{E}[\mathcal{U}^{1}\_{0}]=\mathsf{E}[\mathcal{U}^{2}\_{0}]. For any (ξ,ζ)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\xi,\zeta)\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}), the inequalities ([4.4](https://arxiv.org/html/2510.15616v1#S4.E4 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"))-([4.5](https://arxiv.org/html/2510.15616v1#S4.E5 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) give

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[𝒫​(ξ^,ζ)]≤𝖤​[𝒫​(ξ^,ζ^)]≤𝖤​[𝒫​(ξ,ζ^)],\mathsf{E}[\mathcal{P}(\hat{\xi},\zeta)]\leq\mathsf{E}[\mathcal{P}(\hat{\xi},\hat{\zeta})]\leq\mathsf{E}[\mathcal{P}(\xi,\hat{\zeta})], |  |

which demonstrates that the pair (ξ^,ζ^)(\hat{\xi},\hat{\zeta}) generates a saddle point of the game. Consequently, the game has a value which equals 𝖤​[𝒫​(ξ^,ζ^)]\mathsf{E}[\mathcal{P}(\hat{\xi},\hat{\zeta})].
∎

As a corollary of the above proof we obtain the following result.

###### Corollary 4.3.

Under the assumptions of Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), 𝐌^ξ^\hat{\bf M}^{\hat{\xi}} is a 𝒯0​(𝔽1)\mathcal{T}\_{0}(\mathbb{F}^{1})-martingale system and 𝐍^ζ^\hat{\bf N}^{\hat{\zeta}} is a 𝒯0​(𝔽2)\mathcal{T}\_{0}(\mathbb{F}^{2})-martingale system.

###### Proof.

It transpires from the proof of Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") that ([4.4](https://arxiv.org/html/2510.15616v1#S4.E4 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) holds with equality for ξ=ξ^\xi=\hat{\xi}. This consequently means that ([4.3](https://arxiv.org/html/2510.15616v1#S4.E3 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) holds with equality which translates into 𝖤​[M^ξ^​(T)|ℱ01]=M^ξ^​(0)\mathsf{E}[\hat{M}^{\hat{\xi}}(T)|\mathcal{F}^{1}\_{0}]=\hat{M}^{\hat{\xi}}(0). When we recall that 𝐌^ξ^\hat{\bf M}^{\hat{\xi}} is a 𝒯0​(𝔽1)\mathcal{T}\_{0}(\mathbb{F}^{1})-submartingale system (by assumption (ii) of Theorm [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), we immediately obtain that it is a 𝒯0​(𝔽1)\mathcal{T}\_{0}(\mathbb{F}^{1})-martingale system. A similar argument applies to 𝐍^ζ^\hat{\bf N}^{\hat{\zeta}}.
∎

###### Remark 4.4 (Necessity of sufficient conditions).

Notice first that nowhere in the proof of Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") we require that (𝒰t1)t∈[0,T](\mathcal{U}^{1}\_{t})\_{t\in[0,T]} and (𝒰t2)t∈[0,T](\mathcal{U}^{2}\_{t})\_{t\in[0,T]} be stochastic processes. They can be replaced by 𝒯0​(𝔽1)\mathcal{T}\_{0}(\mathbb{F}^{1}) and 𝒯0​(𝔽2)\mathcal{T}\_{0}(\mathbb{F}^{2}) systems, and, indeed, by the families V∗,1V^{\*,1} and V∗,2V^{\*,2} in ([2.12](https://arxiv.org/html/2510.15616v1#S2.E12 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")). Then conditions (i) and (ii) are satisfied by the families 𝐌ξ{\bf M}^{\xi} and 𝐍ζ{\bf N}^{\zeta} introduced in ([3.8](https://arxiv.org/html/2510.15616v1#S3.E8 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and ([3.9](https://arxiv.org/html/2510.15616v1#S3.E9 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) (cf. Proposition [3.9](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem9 "Proposition 3.9. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")). Condition (iii) is satisfied by Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), see ([3.4](https://arxiv.org/html/2510.15616v1#S3.E4 "In Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")). Condition (iv) follows from Proposition [3.10](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem10 "Proposition 3.10. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") with λ=0\lambda=0 therein. This shows the necessity of the sufficient conditions in Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

We now study in more detail the analogy between processes (𝒰t1)t∈[0,T](\mathcal{U}^{1}\_{t})\_{t\in[0,T]} and (𝒰t2)t∈[0,T](\mathcal{U}^{2}\_{t})\_{t\in[0,T]} from Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and processes (Vt∗,1)t∈[0,T](V^{\*,1}\_{t})\_{t\in[0,T]} and (Vt∗,2)t∈[0,T](V^{\*,2}\_{t})\_{t\in[0,T]} from Section [3](https://arxiv.org/html/2510.15616v1#S3 "3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). Notations and arguments will follow parallel tracks but there are sufficient differences to merit complete statement of results and their proofs.

From now on, the pair (ξ^,ζ^)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\hat{\xi},\hat{\zeta})\in\mathcal{A}\_{0}^{\circ}(\mathbb{F}^{1})\times\mathcal{A}\_{0}^{\circ}(\mathbb{F}^{2}) and processes (𝒰t1)t∈[0,T](\mathcal{U}^{1}\_{t})\_{t\in[0,T]} and (𝒰t2)t∈[0,T](\mathcal{U}^{2}\_{t})\_{t\in[0,T]} are those introduced in Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").
Let us start by defining sets

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ^θ1\displaystyle\hat{\Gamma}^{1}\_{\theta} | ={ω∈Ω:(1−ξ^θ−​(ω))​𝖤​[1−ζ^θ−|ℱθ1]​(ω)>0},θ∈𝒯0​(𝔽1),\displaystyle=\{\omega\in\Omega:(1-\hat{\xi}\_{\theta-}(\omega))\,\mathsf{E}[1-\hat{\zeta}\_{\theta-}|\mathcal{F}^{1}\_{\theta}](\omega)>0\},\qquad\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ^γ2\displaystyle\hat{\Gamma}^{2}\_{\gamma} | ={ω∈Ω:(1−ζ^γ−​(ω))​𝖤​[1−ξ^γ−|ℱγ2]​(ω)>0},γ∈𝒯0​(𝔽2).\displaystyle=\{\omega\in\Omega:(1-\hat{\zeta}\_{\gamma-}(\omega))\,\mathsf{E}[1-\hat{\xi}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}](\omega)>0\},\qquad\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}). |  |

In analogy to ([2.6](https://arxiv.org/html/2510.15616v1#S2.E6 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")), for θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}) and γ∈𝒯0​(𝔽2)\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}) we define

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| (4.6) |  | Π^θ1\displaystyle\hat{\Pi}^{1}\_{\theta} | ≔1−ζ^θ−𝖤​[1−ζ^θ−|ℱθ1],Π^γ2\displaystyle\coloneqq\frac{1-\hat{\zeta}\_{\theta-}}{\mathsf{E}[1-\hat{\zeta}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]},\qquad\hat{\Pi}^{2}\_{\gamma} | ≔1−ξ^γ−𝖤​[1−ξ^γ−|ℱγ2],\displaystyle\coloneqq\frac{1-\hat{\xi}\_{\gamma-}}{\mathsf{E}[1-\hat{\xi}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}]}, |  |

with the ratio equal to 11 when the denominator is zero (see the explanations after ([2.6](https://arxiv.org/html/2510.15616v1#S2.E6 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) concerning this convention). The next lemma is an analogue of Proposition [3.8](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") for (ξ^,ζ^)(\hat{\xi},\hat{\zeta}), 𝒰1\mathcal{U}^{1} and 𝒰2\mathcal{U}^{2}.

###### Lemma 4.5.

Under the assumptions of Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.7) |  |  | 𝟏Γ^θ1​𝒰θ1=𝟏Γ^θ1​ess​infξ∈𝒜θ∘​(𝔽1)⁡JΠ^θ1​(ξ,ζ^θ|ℱθ1)=𝟏Γ^θ1​JΠ^θ1​(ξ^θ,ζ^θ|ℱθ1),θ∈𝒯0​(𝔽1),\displaystyle\mathbf{1}\_{\hat{\Gamma}^{1}\_{\theta}}\mathcal{U}^{1}\_{\theta}=\mathbf{1}\_{\hat{\Gamma}^{1}\_{\theta}}\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1})}J^{\hat{\Pi}^{1}\_{\theta}}(\xi,\hat{\zeta}^{\theta}|\mathcal{F}^{1}\_{\theta})=\mathbf{1}\_{\hat{\Gamma}^{1}\_{\theta}}J^{\hat{\Pi}^{1}\_{\theta}}(\hat{\xi}^{\theta},\hat{\zeta}^{\theta}|\mathcal{F}^{1}\_{\theta}),\quad\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}), |  |
|  |  | 𝟏Γ^γ2​𝒰γ2=𝟏Γ^γ2​ess​supζ∈𝒜γ∘​(𝔽2)⁡JΠ^γ2​(ξ^γ,ζ|ℱγ2)=𝟏Γ^γ2​JΠ^γ2​(ξ^γ,ζ^γ|ℱγ2),γ∈𝒯0​(𝔽2),\displaystyle\mathbf{1}\_{\hat{\Gamma}^{2}\_{\gamma}}\mathcal{U}^{2}\_{\gamma}=\mathbf{1}\_{\hat{\Gamma}^{2}\_{\gamma}}\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\gamma}(\mathbb{F}^{2})}J^{\hat{\Pi}^{2}\_{\gamma}}(\hat{\xi}^{\gamma},\zeta|\mathcal{F}^{2}\_{\gamma})=\mathbf{1}\_{\hat{\Gamma}^{2}\_{\gamma}}J^{\hat{\Pi}^{2}\_{\gamma}}(\hat{\xi}^{\gamma},\hat{\zeta}^{\gamma}|\mathcal{F}^{2}\_{\gamma}),\quad\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}), |  |

where ξ^γ\hat{\xi}^{\gamma} and ζ^θ\hat{\zeta}^{\theta} are truncated controls as in Definition [2.8](https://arxiv.org/html/2510.15616v1#S2.Thmtheorem8 "Definition 2.8. ‣ 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information").

###### Proof.

We prove the first sequence of equalities. The second one is analogous.

Fix θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}). By Corollary [4.3](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem3 "Corollary 4.3. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), 𝐌^ξ^\hat{\bf M}^{\hat{\xi}} is a 𝒯0​(𝔽1)\mathcal{T}\_{0}(\mathbb{F}^{1})-martingale system, so

|  |  |  |  |
| --- | --- | --- | --- |
| (4.8) |  | M^ξ^​(θ)=𝖤​[M^ξ^​(T)|ℱθ1].\hat{M}^{\hat{\xi}}(\theta)=\mathsf{E}[\hat{M}^{\hat{\xi}}(T)|\mathcal{F}^{1}\_{\theta}]. |  |

Arguing as in the proof of Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), we have 𝖤​[M^ξ^​(T)|ℱθ1]=𝖤​[𝒫​(ξ^,ζ^)|ℱθ1]\mathsf{E}[\hat{M}^{\hat{\xi}}(T)|\mathcal{F}^{1}\_{\theta}]=\mathsf{E}[\mathcal{P}(\hat{\xi},\hat{\zeta})|\mathcal{F}^{1}\_{\theta}]. Using the definition of M^ξ^​(θ)\hat{M}^{\hat{\xi}}(\theta) and cancelling identical terms on both sides of ([4.8](https://arxiv.org/html/2510.15616v1#S4.E8 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.9) |  |  | (1−ξ^θ−)​𝖤​[1−ζ^θ−|ℱθ1]​𝒰θ1\displaystyle(1-\hat{\xi}\_{\theta-})\mathsf{E}[1-\hat{\zeta}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]\,\mathcal{U}^{1}\_{\theta} |  |
|  |  | =𝖤​[∫[θ,T)ft​(1−ζ^t)​dξ^t+∫[θ,T)gt​(1−ξ^t)​dζ^t+∑t∈[θ,T]ht​Δ​ξ^t​Δ​ζ^t|ℱθ1]\displaystyle=\mathsf{E}\Big[\!\int\_{[\theta,T)}\!\!f\_{t}(1\!-\!\hat{\zeta}\_{t})\mathrm{d}\hat{\xi}\_{t}\!+\!\int\_{[\theta,T)}\!\!g\_{t}(1\!-\!\hat{\xi}\_{t})\mathrm{d}\hat{\zeta}\_{t}\!+\!\!\sum\_{t\in[\theta,T]}\!\!h\_{t}\Delta\hat{\xi}\_{t}\Delta\hat{\zeta}\_{t}\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  | =𝖤​[(1−ξ^θ−)​(1−ζ^θ−)​(∫[θ,T)ft​(1−ζ^tθ)​dξ^tθ+∫[θ,T)gt​(1−ξ^tθ)​dζ^tθ+∑t∈[θ,T]ht​Δ​ξ^tθ​Δ​ζ^tθ)|ℱθ1]\displaystyle=\mathsf{E}\Big[(1-\hat{\xi}\_{\theta-})(1-\hat{\zeta}\_{\theta-})\Big(\!\int\_{[\theta,T)}\!\!f\_{t}(1\!-\!\hat{\zeta}^{\theta}\_{t})\mathrm{d}\hat{\xi}^{\theta}\_{t}\!+\!\int\_{[\theta,T)}\!\!g\_{t}(1\!-\!\hat{\xi}^{\theta}\_{t})\mathrm{d}\hat{\zeta}^{\theta}\_{t}\!+\!\!\sum\_{t\in[\theta,T]}\!\!h\_{t}\Delta\hat{\xi}^{\theta}\_{t}\Delta\hat{\zeta}^{\theta}\_{t}\Big)\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  | =(1−ξ^θ−)​𝖤​[1−ζ^θ−|ℱθ1]​𝖤​[Π^θ1​(∫[θ,T)ft​(1−ζ^tθ)​dξ^tθ+∫[θ,T)gt​(1−ξ^tθ)​dζ^tθ+∑t∈[θ,T]ht​Δ​ξ^tθ​Δ​ζ^tθ)|ℱθ1]\displaystyle=(1-\hat{\xi}\_{\theta-})\mathsf{E}[1-\hat{\zeta}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]\mathsf{E}\Big[\hat{\Pi}^{1}\_{\theta}\Big(\!\int\_{[\theta,T)}\!\!f\_{t}(1\!-\!\hat{\zeta}^{\theta}\_{t})\mathrm{d}\hat{\xi}^{\theta}\_{t}\!+\!\int\_{[\theta,T)}\!\!g\_{t}(1\!-\!\hat{\xi}^{\theta}\_{t})\mathrm{d}\hat{\zeta}^{\theta}\_{t}\!+\!\!\sum\_{t\in[\theta,T]}\!\!h\_{t}\Delta\hat{\xi}^{\theta}\_{t}\Delta\hat{\zeta}^{\theta}\_{t}\Big)\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  | =(1−ξ^θ−)​𝖤​[1−ζ^θ−|ℱθ1]​JΠ^θ1​(ξ^θ,ζ^θ|ℱθ1).\displaystyle=(1-\hat{\xi}\_{\theta-})\mathsf{E}[1-\hat{\zeta}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]\,J^{\hat{\Pi}^{1}\_{\theta}}(\hat{\xi}^{\theta},\hat{\zeta}^{\theta}|\mathcal{F}^{1}\_{\theta}). |  |

On the set Γ^θ1\hat{\Gamma}^{1}\_{\theta}, the multiplicative factor on both sides of the inequality is positive, which implies

|  |  |  |  |
| --- | --- | --- | --- |
| (4.10) |  | 𝟏Γ^θ1​𝒰θ1=𝟏Γ^θ1​JΠ^θ1​(ξ^θ,ζ^θ|ℱθ1).\displaystyle\mathbf{1}\_{\hat{\Gamma}^{1}\_{\theta}}\mathcal{U}^{1}\_{\theta}=\mathbf{1}\_{\hat{\Gamma}^{1}\_{\theta}}J^{\hat{\Pi}^{1}\_{\theta}}(\hat{\xi}^{\theta},\hat{\zeta}^{\theta}|\mathcal{F}^{1}\_{\theta}). |  |

To prove the remaining assertion, take any ξ∈𝒜θ∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1}) and define (cf. ([3.20](https://arxiv.org/html/2510.15616v1#S3.E20 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")))

|  |  |  |
| --- | --- | --- |
|  | ξ¯t=ξ^t​𝟏[0,θ)​(t)+(ξ^θ−+(1−ξ^θ−)​ξt)​𝟏[θ,T]​(t).\bar{\xi}\_{t}=\hat{\xi}\_{t}\mathbf{1}\_{[0,\theta)}(t)+(\hat{\xi}\_{\theta-}+(1-\hat{\xi}\_{\theta-})\xi\_{t})\mathbf{1}\_{[\theta,T]}(t). |  |

By the submartingale property of the family 𝐌^ξ¯\hat{\bf M}^{\bar{\xi}}, we have M^ξ¯​(θ)≤𝖤​[M^ξ¯​(T)|ℱθ1]\hat{M}^{\bar{\xi}}(\theta)\leq\mathsf{E}[\hat{M}^{\bar{\xi}}(T)|\mathcal{F}^{1}\_{\theta}]. Arguing as above, this inequality implies

|  |  |  |
| --- | --- | --- |
|  | (1−ξ¯θ−)​𝖤​[1−ζ^θ−|ℱθ1]​𝒰θ1≤(1−ξ¯θ−)​𝖤​[1−ζ^θ−|ℱθ1]​JΠ^θ1​(ξ¯θ,ζ^θ|ℱθ1).(1-\bar{\xi}\_{\theta-})\mathsf{E}[1-\hat{\zeta}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]\,\mathcal{U}^{1}\_{\theta}\leq(1-\bar{\xi}\_{\theta-})\mathsf{E}[1-\hat{\zeta}\_{\theta-}|\mathcal{F}^{1}\_{\theta}]\,J^{\hat{\Pi}^{1}\_{\theta}}(\bar{\xi}^{\theta},\hat{\zeta}^{\theta}|\mathcal{F}^{1}\_{\theta}). |  |

By the definition of ξ¯\bar{\xi}, we have ξ¯θ−=ξ^θ−\bar{\xi}\_{\theta-}=\hat{\xi}\_{\theta-} and ξ¯tθ=ξt\bar{\xi}^{\theta}\_{t}=\xi\_{t} for t∈[θ,T]t\in[\theta,T], so we can conclude that

|  |  |  |
| --- | --- | --- |
|  | 𝟏Γ^θ1​𝒰θ1≤𝟏Γ^θ1​JΠ^θ1​(ξ,ζ^θ|ℱθ1).\mathbf{1}\_{\hat{\Gamma}^{1}\_{\theta}}\mathcal{U}^{1}\_{\theta}\leq\mathbf{1}\_{\hat{\Gamma}^{1}\_{\theta}}J^{\hat{\Pi}^{1}\_{\theta}}(\xi,\hat{\zeta}^{\theta}|\mathcal{F}^{1}\_{\theta}). |  |

By the arbitrariness of ξ∈𝒜θ∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1}),

|  |  |  |
| --- | --- | --- |
|  | 𝟏Γ^θ1​𝒰θ1≤ess​infξ∈𝒜θ∘​(𝔽1)⁡𝟏Γ^θ1​JΠ^θ1​(ξ,ζ^θ|ℱθ1)=𝟏Γ^θ1​ess​infξ∈𝒜θ∘​(𝔽1)⁡JΠ^θ1​(ξ,ζ^θ|ℱθ1).\mathbf{1}\_{\hat{\Gamma}^{1}\_{\theta}}\mathcal{U}^{1}\_{\theta}\leq\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1})}\mathbf{1}\_{\hat{\Gamma}^{1}\_{\theta}}J^{\hat{\Pi}^{1}\_{\theta}}(\xi,\hat{\zeta}^{\theta}|\mathcal{F}^{1}\_{\theta})=\mathbf{1}\_{\hat{\Gamma}^{1}\_{\theta}}\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1})}J^{\hat{\Pi}^{1}\_{\theta}}(\xi,\hat{\zeta}^{\theta}|\mathcal{F}^{1}\_{\theta}). |  |

Combining the inequality above with ([4.10](https://arxiv.org/html/2510.15616v1#S4.E10 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) completes the proof.
∎

Next we obtain an analogue of Proposition [3.10](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem10 "Proposition 3.10. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). Recall the notations ℱt1,2=ℱt1∩ℱt2\mathcal{F}^{1,2}\_{t}=\mathcal{F}^{1}\_{t}\cap\mathcal{F}^{2}\_{t} and 𝔽1,2=𝔽1∧𝔽2\mathbb{F}^{1,2}=\mathbb{F}^{1}\wedge\mathbb{F}^{2}.

###### Corollary 4.6.

Under the assumptions of Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), for λ∈𝒯0​(𝔽1,2)\lambda\in\mathcal{T}\_{0}(\mathbb{F}^{1,2}) we have

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[(1−ξ^λ−)​(1−ζ^λ−)​𝒰λ1|ℱλ1,2]=𝖤​[(1−ξ^λ−)​(1−ζ^λ−)​𝒰λ2|ℱλ1,2]\displaystyle\mathsf{E}\big[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})\,\mathcal{U}^{1}\_{\lambda}\big|\mathcal{F}^{1,2}\_{\lambda}\big]=\mathsf{E}\big[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})\,\mathcal{U}^{2}\_{\lambda}\big|\mathcal{F}^{1,2}\_{\lambda}\big] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝖤​[∫[λ,T)ft​(1−ζ^t)​dξ^t+∫[λ,T)gt​(1−ξ^t)​dζ^t+∑t∈[λ,T]ht​Δ​ξ^t​Δ​ζ^t|ℱλ1,2]≕U¯​(λ).\displaystyle=\mathsf{E}\Big[\!\int\_{[\lambda,T)}\!\!f\_{t}(1\!-\!\hat{\zeta}\_{t})\mathrm{d}\hat{\xi}\_{t}\!+\!\int\_{[\lambda,T)}\!\!g\_{t}(1\!-\!\hat{\xi}\_{t})\mathrm{d}\hat{\zeta}\_{t}\!+\!\!\sum\_{t\in[\lambda,T]}\!\!h\_{t}\Delta\hat{\xi}\_{t}\Delta\hat{\zeta}\_{t}\Big|\mathcal{F}^{1,2}\_{\lambda}\Big]\eqqcolon\bar{U}(\lambda). |  |

###### Proof.

From the first equality in ([4.9](https://arxiv.org/html/2510.15616v1#S4.E9 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) with θ=λ\theta=\lambda and an analogous derivation for 𝒰2\mathcal{U}^{2} we have

|  |  |  |
| --- | --- | --- |
|  | (1−ξ^λ−)​𝖤​[1−ζ^λ−|ℱλ1]​𝒰λ1=𝖤​[∫[λ,T)ft​(1−ζ^t)​dξ^t+∫[λ,T)gt​(1−ξ^t)​dζ^t+∑t∈[λ,T]ht​Δ​ξ^t​Δ​ζ^t|ℱλ1],\displaystyle(1-\hat{\xi}\_{\lambda-})\mathsf{E}[1-\hat{\zeta}\_{\lambda-}|\mathcal{F}^{1}\_{\lambda}]\,\mathcal{U}^{1}\_{\lambda}=\mathsf{E}\Big[\!\int\_{[\lambda,T)}\!\!f\_{t}(1\!-\!\hat{\zeta}\_{t})\mathrm{d}\hat{\xi}\_{t}\!+\!\int\_{[\lambda,T)}\!\!g\_{t}(1\!-\!\hat{\xi}\_{t})\mathrm{d}\hat{\zeta}\_{t}\!+\!\!\sum\_{t\in[\lambda,T]}\!\!h\_{t}\Delta\hat{\xi}\_{t}\Delta\hat{\zeta}\_{t}\Big|\mathcal{F}^{1}\_{\lambda}\Big], |  |
|  |  |  |
| --- | --- | --- |
|  | (1−ζ^λ−)​𝖤​[1−ξ^λ−|ℱλ2]​𝒰λ2=𝖤​[∫[λ,T)ft​(1−ζ^t)​dξ^t+∫[λ,T)gt​(1−ξ^t)​dζ^t+∑t∈[λ,T]ht​Δ​ξ^t​Δ​ζ^t|ℱλ2].\displaystyle(1-\hat{\zeta}\_{\lambda-})\mathsf{E}[1-\hat{\xi}\_{\lambda-}|\mathcal{F}^{2}\_{\lambda}]\,\mathcal{U}^{2}\_{\lambda}=\mathsf{E}\Big[\!\int\_{[\lambda,T)}\!\!f\_{t}(1\!-\!\hat{\zeta}\_{t})\mathrm{d}\hat{\xi}\_{t}\!+\!\int\_{[\lambda,T)}\!\!g\_{t}(1\!-\!\hat{\xi}\_{t})\mathrm{d}\hat{\zeta}\_{t}\!+\!\!\sum\_{t\in[\lambda,T]}\!\!h\_{t}\Delta\hat{\xi}\_{t}\Delta\hat{\zeta}\_{t}\Big|\mathcal{F}^{2}\_{\lambda}\Big]. |  |

As the expressions under the conditional expectations on the right-hand sides are identical, the right-hand sides are identical once conditioned on ℱλ1,2\mathcal{F}^{1,2}\_{\lambda} by the tower property. Hence,

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[(1−ξ^λ−)​𝖤​[1−ζ^λ−|ℱλ1]​𝒰λ1|ℱλ1,2]=𝖤​[(1−ζ^λ−)​𝖤​[1−ξ^λ−|ℱλ2]​𝒰λ2|ℱλ1,2].\mathsf{E}\big[(1-\hat{\xi}\_{\lambda-})\mathsf{E}[1-\hat{\zeta}\_{\lambda-}|\mathcal{F}^{1}\_{\lambda}]\,\mathcal{U}^{1}\_{\lambda}\big|\mathcal{F}^{1,2}\_{\lambda}\big]=\mathsf{E}\big[(1-\hat{\zeta}\_{\lambda-})\mathsf{E}[1-\hat{\xi}\_{\lambda-}|\mathcal{F}^{2}\_{\lambda}]\,\mathcal{U}^{2}\_{\lambda}\big|\mathcal{F}^{1,2}\_{\lambda}\big]. |  |

To conclude by the tower property, it is sufficient to recall that ξ^λ−\hat{\xi}\_{\lambda-}, 𝒰λ1\mathcal{U}^{1}\_{\lambda} are ℱλ1\mathcal{F}^{1}\_{\lambda}-measurable and ζ^λ−\hat{\zeta}\_{\lambda-}, 𝒰λ2\mathcal{U}^{2}\_{\lambda} are ℱλ2\mathcal{F}^{2}\_{\lambda}-measurable.
∎

We turn our attention to the *ex-ante* value of the game and its relationship to 𝒰1\mathcal{U}^{1} and 𝒰2\mathcal{U}^{2}. The next proposition is an analogue of Corollary [3.13](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem13 "Corollary 3.13. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

###### Proposition 4.7.

Under the assumptions of Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), for any λ∈𝒯0​(𝔽1∧𝔽2)\lambda\in\mathcal{T}\_{0}(\mathbb{F}^{1}\wedge\mathbb{F}^{2}) let

|  |  |  |
| --- | --- | --- |
|  | Πλ≔(1−ξ^λ−)​(1−ζ^λ−)𝖤​[(1−ξ^λ−)​(1−ζ^λ−)|ℱλ1,2]∈ℛ​(ℱλ1,2),\Pi\_{\lambda}\coloneqq\frac{(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})}{\mathsf{E}[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})|\mathcal{F}^{1,2}\_{\lambda}]}\in\mathcal{R}(\mathcal{F}^{1,2}\_{\lambda}), |  |

with the convention 0/0=10/0=1 as in ([2.6](https://arxiv.org/html/2510.15616v1#S2.E6 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")).

Define U​(λ)≔JΠλ​(ξ^λ,ζ^λ|ℱλ1,2)U(\lambda)\coloneqq J^{\Pi\_{\lambda}}(\hat{\xi}^{\lambda},\hat{\zeta}^{\lambda}|\mathcal{F}^{1,2}\_{\lambda}). Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.11) |  | U​(λ)\displaystyle U(\lambda) | =ess​infξ∈𝒜λ∘​(𝔽1)⁡ess​supζ∈𝒜λ∘​(𝔽2)⁡JΠλ​(ξ,ζ|ℱλ1,2)=ess​supζ∈𝒜λ∘​(𝔽2)⁡ess​infξ∈𝒜λ∘​(𝔽1)⁡JΠλ​(ξ,ζ|ℱλ1,2),\displaystyle=\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1})}\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{2})}J^{\Pi\_{\lambda}}(\xi,\zeta|\mathcal{F}^{1,2}\_{\lambda})=\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{2})}\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1})}J^{\Pi\_{\lambda}}(\xi,\zeta|\mathcal{F}^{1,2}\_{\lambda}), |  |

on the event {𝖤​[(1−ξ^λ−)​(1−ζ^λ−)|ℱλ1,2]>0}\{\mathsf{E}[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})|\mathcal{F}^{1,2}\_{\lambda}]>0\} and it holds, for i=1,2i=1,2,

|  |  |  |  |
| --- | --- | --- | --- |
| (4.12) |  | U¯​(λ)=𝖤​[(1−ξ^λ−)​(1−ζ^λ−)|ℱλ1,2]​U​(λ)=𝖤​[(1−ξ^λ−)​(1−ζ^λ−)|ℱλ1,2]​𝖤​[Πλ​𝒰λi|ℱλ1,2]=𝖤​[(1−ξ^λ−)​(1−ζ^λ−)|ℱλ1,2]​𝖤Πλ​[𝒰λi|ℱλ1,2].\displaystyle\begin{aligned} \bar{U}(\lambda)&=\mathsf{E}[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})|\mathcal{F}^{1,2}\_{\lambda}]U(\lambda)\\ &=\mathsf{E}[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})|\mathcal{F}^{1,2}\_{\lambda}]\mathsf{E}\big[\Pi\_{\lambda}\,\mathcal{U}^{i}\_{\lambda}\big|\mathcal{F}^{1,2}\_{\lambda}\big]\\ &=\mathsf{E}[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})|\mathcal{F}^{1,2}\_{\lambda}]\mathsf{E}^{\Pi\_{\lambda}}\big[\mathcal{U}^{i}\_{\lambda}\big|\mathcal{F}^{1,2}\_{\lambda}\big].\end{aligned} |  |

###### Proof.

Fix λ∈𝒯0​(𝔽1,2)\lambda\in\mathcal{T}\_{0}(\mathbb{F}^{1,2}).
Arguing as in the proof of Lemma [4.5](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem5 "Lemma 4.5. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") (cf. ([4.9](https://arxiv.org/html/2510.15616v1#S4.E9 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"))), for any ξ∈𝒜λ∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1}) we have

|  |  |  |
| --- | --- | --- |
|  | (1−ξ^λ−)​𝖤​[1−ζ^λ−|ℱλ1]​𝒰λ1\displaystyle(1-\hat{\xi}\_{\lambda-})\mathsf{E}[1-\hat{\zeta}\_{\lambda-}|\mathcal{F}^{1}\_{\lambda}]\,\mathcal{U}^{1}\_{\lambda} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝖤​[(1−ξ^λ−)​(1−ζ^λ−)​(∫[λ,T)ft​(1−ζ^tλ)​dξt+∫[λ,T)gt​(1−ξt)​dζ^tλ+∑t∈[λ,T]ht​Δ​ξt​Δ​ζ^tλ)|ℱλ1],\displaystyle\leq\mathsf{E}\Big[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})\Big(\!\int\_{[\lambda,T)}\!\!f\_{t}(1\!-\!\hat{\zeta}^{\lambda}\_{t})\mathrm{d}\xi\_{t}\!+\!\int\_{[\lambda,T)}\!\!g\_{t}(1\!-\!\xi\_{t})\mathrm{d}\hat{\zeta}^{\lambda}\_{t}\!+\!\!\sum\_{t\in[\lambda,T]}\!\!h\_{t}\Delta\xi\_{t}\Delta\hat{\zeta}^{\lambda}\_{t}\Big)\Big|\mathcal{F}^{1}\_{\lambda}\Big], |  |

with the equality for ξ=ξ^λ\xi=\hat{\xi}^{\lambda}. On both sides we take conditional expectations with respect to ℱλ1,2\mathcal{F}^{1,2}\_{\lambda} and note that the left-hand side equals U¯​(λ)\bar{U}(\lambda). Then, for any ξ∈𝒜λ∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | U¯​(λ)\displaystyle\bar{U}(\lambda) | ≤𝖤​[(1−ξ^λ−)​(1−ζ^λ−)​(∫[λ,T)ft​(1−ζ^tλ)​dξt+∫[λ,T)gt​(1−ξt)​dζ^tλ+∑t∈[λ,T]ht​Δ​ξt​Δ​ζ^tλ)|ℱλ1,2]\displaystyle\leq\mathsf{E}\Big[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})\Big(\!\int\_{[\lambda,T)}\!\!f\_{t}(1\!-\!\hat{\zeta}^{\lambda}\_{t})\mathrm{d}\xi\_{t}\!+\!\int\_{[\lambda,T)}\!\!g\_{t}(1\!-\!\xi\_{t})\mathrm{d}\hat{\zeta}^{\lambda}\_{t}\!+\!\!\sum\_{t\in[\lambda,T]}\!\!h\_{t}\Delta\xi\_{t}\Delta\hat{\zeta}^{\lambda}\_{t}\Big)\Big|\mathcal{F}^{1,2}\_{\lambda}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖤​[(1−ξ^λ−)​(1−ζ^λ−)|ℱλ1,2]​JΠλ​(ξ,ζ^λ|ℱλ1,2).\displaystyle=\mathsf{E}\big[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]J^{\Pi\_{\lambda}}(\xi,\hat{\zeta}^{\lambda}|\mathcal{F}^{1,2}\_{\lambda}). |  |

Since equality holds for ξ=ξ^λ\xi=\hat{\xi}^{\lambda}, we deduce

|  |  |  |  |
| --- | --- | --- | --- |
|  | U¯​(λ)\displaystyle\bar{U}(\lambda) | =𝖤​[(1−ξ^λ−)​(1−ζ^λ−)|ℱλ1,2]​ess​infξ∈𝒜λ∘​(𝔽1)⁡JΠλ​(ξ,ζ^λ|ℱλ1,2)\displaystyle=\mathsf{E}\big[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1})}J^{\Pi\_{\lambda}}(\xi,\hat{\zeta}^{\lambda}|\mathcal{F}^{1,2}\_{\lambda}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝖤​[(1−ξ^λ−)​(1−ζ^λ−)|ℱλ1,2]​ess​supζ∈𝒜λ∘​(𝔽2)⁡ess​infξ∈𝒜λ∘​(𝔽1)⁡JΠλ​(ξ,ζ|ℱλ1,2).\displaystyle\leq\mathsf{E}\big[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{2})}\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{1})}J^{\Pi\_{\lambda}}(\xi,\zeta|\mathcal{F}^{1,2}\_{\lambda}). |  |

Analogously, we show that

|  |  |  |
| --- | --- | --- |
|  | U¯​(λ)≥𝖤​[(1−ξ^λ−)​(1−ζ^λ−)|ℱλ1,2]​JΠλ​(ξ^λ,ζ|ℱλ1,2),\bar{U}(\lambda)\geq\mathsf{E}\big[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]J^{\Pi\_{\lambda}}(\hat{\xi}^{\lambda},\zeta|\mathcal{F}^{1,2}\_{\lambda}), |  |

for all ζ∈𝒜λ∘​(𝔽2)\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{2}) and it holds with equality for ζ=ζ^λ\zeta=\hat{\zeta}^{\lambda}. It then follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | U¯​(λ)\displaystyle\bar{U}(\lambda) | =𝖤​[(1−ξ^λ−)​(1−ζ^λ−)|ℱλ1,2]​ess​supζ∈𝒜λ∘​(𝔽2)⁡JΠλ​(ξ^λ,ζ|ℱλ1,2)\displaystyle=\mathsf{E}\big[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{2})}J^{\Pi\_{\lambda}}(\hat{\xi}^{\lambda},\zeta|\mathcal{F}^{1,2}\_{\lambda}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥𝖤​[(1−ξ^λ−)​(1−ζ^λ−)|ℱλ1,2]​ess​infξ∈𝒜λ∘​(𝔽1)⁡ess​supζ∈𝒜λ∘​(𝔽2)⁡JΠλ​(ξ,ζ|ℱλ1,2).\displaystyle\geq\mathsf{E}\big[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\circ}\_{\lambda}(\mathbb{F}^{1})}\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\lambda}(\mathbb{F}^{2})}J^{\Pi\_{\lambda}}(\xi,\zeta|\mathcal{F}^{1,2}\_{\lambda}). |  |

Combining the two inequalities we prove that the order of ess​sup\operatorname\*{ess\,sup} and ess​inf\operatorname\*{ess\,inf} can be swapped. Moreover, using that the inequalities above hold with equality for the pair (ξ^λ,ζ^λ)(\hat{\xi}^{\lambda},\hat{\zeta}^{\lambda}) we deduce ([4.11](https://arxiv.org/html/2510.15616v1#S4.E11 "In Proposition 4.7. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and the first equality in ([4.12](https://arxiv.org/html/2510.15616v1#S4.E12 "In Proposition 4.7. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")).
The second and third equalities in ([4.12](https://arxiv.org/html/2510.15616v1#S4.E12 "In Proposition 4.7. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) hold by the definition of Πλ\Pi\_{\lambda} and Corollary [4.6](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem6 "Corollary 4.6. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | U¯​(λ)\displaystyle\bar{U}(\lambda) | =𝖤​[(1−ξ^λ−)​(1−ζ^λ−)​𝒰λi|ℱλ1,2]\displaystyle=\mathsf{E}\big[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})\,\mathcal{U}^{i}\_{\lambda}\big|\mathcal{F}^{1,2}\_{\lambda}\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖤​[(1−ξ^λ−)​(1−ζ^λ−)|ℱλ1,2]​𝖤​[Πλ​𝒰λi|ℱλ1,2]=𝖤​[(1−ξ^λ−)​(1−ζ^λ−)|ℱλ1,2]​𝖤Πλ​[𝒰λi|ℱλ1,2],\displaystyle=\mathsf{E}\big[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]\mathsf{E}\big[\Pi\_{\lambda}\,\mathcal{U}^{i}\_{\lambda}\big|\mathcal{F}^{1,2}\_{\lambda}\big]=\mathsf{E}\big[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]\mathsf{E}^{\Pi\_{\lambda}}\big[\mathcal{U}^{i}\_{\lambda}\big|\mathcal{F}^{1,2}\_{\lambda}\big], |  |

upon recalling the convention 0/0=10/0=1 for Πλ\Pi\_{\lambda} and noticing that the equalities hold trivially with zero value on the event {𝖤​[(1−ξ^λ−)​(1−ζ^λ−)|ℱλ1,2]=0}\big\{\mathsf{E}\big[(1-\hat{\xi}\_{\lambda-})(1-\hat{\zeta}\_{\lambda-})\big|\mathcal{F}^{1,2}\_{\lambda}\big]=0\big\} (cf. also ([2.9](https://arxiv.org/html/2510.15616v1#S2.E9 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information"))).
∎

We now develop results in the same vein as Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") but under a different set of conditions.

###### Theorem 4.8.

Let 𝒰01\mathcal{U}^{1}\_{0} be ℱ01\mathcal{F}^{1}\_{0}-measurable and 𝒰02\mathcal{U}^{2}\_{0} be ℱ02\mathcal{F}^{2}\_{0}-measurable random variables and (ξ^,ζ^)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\hat{\xi},\hat{\zeta})\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}). Assume that

1. (i)

   for any τ∈𝒯0​(𝔽1)\tau\in\mathcal{T}\_{0}(\mathbb{F}^{1}), we have

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (4.13) |  | 𝖤​[fτ​(1−ζ^τ)+∫[0,τ)gs​dζ^s+hτ​Δ​ζ^τ|ℱ01]≥𝒰01,\mathsf{E}\Big[f\_{\tau}(1-\hat{\zeta}\_{\tau})+\int\_{[0,\tau)}g\_{s}\mathrm{d}\hat{\zeta}\_{s}+h\_{\tau}\Delta\hat{\zeta}\_{\tau}\Big|\mathcal{F}^{1}\_{0}\Big]\geq\mathcal{U}^{1}\_{0}, |  |
2. (ii)

   for any σ∈𝒯0​(𝔽2)\sigma\in\mathcal{T}\_{0}(\mathbb{F}^{2}), we have

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (4.14) |  | 𝖤​[∫[0,σ)fs​dξ^s+gσ​(1−ξ^σ)+hσ​Δ​ξ^σ|ℱ02]≤𝒰02,\mathsf{E}\Big[\int\_{[0,\sigma)}f\_{s}\mathrm{d}\hat{\xi}\_{s}+g\_{\sigma}(1-\hat{\xi}\_{\sigma})+h\_{\sigma}\Delta\hat{\xi}\_{\sigma}\Big|\mathcal{F}^{2}\_{0}\Big]\leq\mathcal{U}^{2}\_{0}, |  |
3. (iii)

   𝖤​[𝒰01]=𝖤​[𝒰02]\mathsf{E}[\mathcal{U}^{1}\_{0}]=\mathsf{E}[\mathcal{U}^{2}\_{0}].

Then the game has a value, i.e., V¯=V¯=𝖤​[𝒰01]=𝖤​[𝒰02]\overline{V}=\underline{V}=\mathsf{E}[\mathcal{U}^{1}\_{0}]=\mathsf{E}[\mathcal{U}^{2}\_{0}], and the randomised stopping times (τ^,σ^)∈𝒯0R​(𝔽1)×𝒯0R​(𝔽2)(\hat{\tau},\hat{\sigma})\in\mathcal{T}^{R}\_{0}(\mathbb{F}^{1})\times\mathcal{T}^{R}\_{0}(\mathbb{F}^{2}) generated by (ξ^,ζ^)(\hat{\xi},\hat{\zeta}) form a saddle point of the game.

###### Proof.

In order to apply arguments from the proof of Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), we need to prove ([4.3](https://arxiv.org/html/2510.15616v1#S4.E3 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) with 𝖤​[1−ζ^T−|ℱT1]​𝒰T1\mathsf{E}[1-\hat{\zeta}\_{T-}|\mathcal{F}^{1}\_{T}]\mathcal{U}^{1}\_{T} replaced by hT​Δ​ζ^Th\_{T}\Delta\hat{\zeta}\_{T} (under expectation) and the equivalent condition arising for the supermartingale system 𝐍^ζ\hat{\bf N}^{\zeta}. Those two inequalities imply ([4.4](https://arxiv.org/html/2510.15616v1#S4.E4 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"))-([4.5](https://arxiv.org/html/2510.15616v1#S4.E5 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), from which it not hard to deduce all claims in the theorem.

We will only provide details for ([4.3](https://arxiv.org/html/2510.15616v1#S4.E3 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), because arguments for 𝐍^ζ\hat{\bf N}^{\zeta} are analogous.
Take any ξ∈𝒜0∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1}) and let τ​(z)=inf{t≥0:ξt>z}∈𝒯​(𝔽1)\tau(z)=\inf\{t\geq 0:\xi\_{t}>z\}\in\mathcal{T}(\mathbb{F}^{1}). We have

|  |  |  |  |
| --- | --- | --- | --- |
| (4.15) |  | 𝖤​[∫[0,T)ft​(1−ζ^t)​dξt+∫[0,T)gt​(1−ξt)​dζ^t+∑t∈[0,T)ht​Δ​ξt​Δ​ζ^t+hT​Δ​ξT​Δ​ζ^T|ℱ01]=∫01m^ξ​(z)​dz,\mathsf{E}\Big[\!\int\_{[0,T)}\!\!f\_{t}(1\!-\!\hat{\zeta}\_{t})\mathrm{d}\xi\_{t}\!+\!\int\_{[0,T)}\!\!g\_{t}(1\!-\!\xi\_{t})\mathrm{d}\hat{\zeta}\_{t}\!+\!\!\sum\_{t\in[0,T)}\!\!h\_{t}\Delta\xi\_{t}\Delta\hat{\zeta}\_{t}\!+\!h\_{T}\Delta\xi\_{T}\Delta\hat{\zeta}\_{T}\Big|\mathcal{F}^{1}\_{0}\Big]\!=\!\int\_{0}^{1}\!\!\hat{m}^{\xi}(z)\mathrm{d}z, |  |

where, as in Proposition [3.14](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem14 "Proposition 3.14. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), (z,ω)↦m^ξ​(z,ω)(z,\omega)\mapsto\hat{m}^{\xi}(z,\omega) is a ℬ​([0,T])×ℱ01\mathcal{B}([0,T])\times\mathcal{F}^{1}\_{0}-measurable function such that for each z∈[0,1]z\in[0,1], 𝖯\mathsf{P}-a.s.

|  |  |  |
| --- | --- | --- |
|  | m^ξ​(z)=𝖤​[𝟏{τ​(z)<T}​(fτ​(z)​(1−ζ^τ​(z))+hτ​(z)​Δ​ζ^τ​(z))+∫[0,τ​(z))gs​dζ^s+𝟏{τ​(z)=T}​hT​Δ​ζ^T|ℱ01].\hat{m}^{\xi}(z)=\mathsf{E}\Big[\mathbf{1}\_{\{\tau(z)<T\}}\big(f\_{\tau(z)}(1\!-\!\hat{\zeta}\_{\tau(z)})\!+\!h\_{\tau(z)}\Delta\hat{\zeta}\_{\tau(z)}\big)\!+\!\int\_{[0,\tau(z))}g\_{s}\mathrm{d}\hat{\zeta}\_{s}\!+\!\mathbf{1}\_{\{\tau(z)=T\}}h\_{T}\Delta\hat{\zeta}\_{T}\Big|\mathcal{F}^{1}\_{0}\Big]. |  |

We recombine the indicator functions for the jump terms in the process ζ^\hat{\zeta} and use ζ^T=1\hat{\zeta}\_{T}=1 to drop the indicator function in the term involving fτ​(z)f\_{\tau(z)} to obtain

|  |  |  |
| --- | --- | --- |
|  | m^ξ​(z)=𝖤​[fτ​(z)​(1−ζ^τ​(z))+∫[0,τ​(z))gs​dζ^s+hτ​(z)​Δ​ζ^τ​(z)|ℱ01].\hat{m}^{\xi}(z)=\mathsf{E}\Big[f\_{\tau(z)}(1-\hat{\zeta}\_{\tau(z)})+\int\_{[0,\tau(z))}g\_{s}\mathrm{d}\hat{\zeta}\_{s}+h\_{\tau(z)}\Delta\hat{\zeta}\_{\tau(z)}\Big|\mathcal{F}^{1}\_{0}\Big]. |  |

From ([4.13](https://arxiv.org/html/2510.15616v1#S4.E13 "In item i ‣ Theorem 4.8. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), we further have m^ξ​(z)≥𝒰01\hat{m}^{\xi}(z)\geq\mathcal{U}^{1}\_{0}, 𝖯\mathsf{P}-a.s. Since 𝒰01\mathcal{U}^{1}\_{0} does not depend on zz, we claim that ∫01m^ξ​(z)​dz≥𝒰01\int\_{0}^{1}\hat{m}^{\xi}(z)\mathrm{d}z\geq\mathcal{U}^{1}\_{0}, 𝖯\mathsf{P}-a.s.; this is not immediate as the set of measure zero in the inequality m^ξ​(z)≥𝒰01\hat{m}^{\xi}(z)\geq\mathcal{U}^{1}\_{0} depends on zz. However, taking A={∫01m^ξ​(z)​dz<𝒰01}A=\{\int\_{0}^{1}\hat{m}^{\xi}(z)\mathrm{d}z<\mathcal{U}^{1}\_{0}\}, we have A∈ℱ01A\in\mathcal{F}^{1}\_{0} and

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[𝟏A​∫01m^ξ​(z)​dz]=∫01𝖤​[𝟏A​m^ξ​(z)]​dz≥∫01𝖤​[𝟏A​𝒰01]​dz=𝖤​[𝟏A​𝒰01],\mathsf{E}\Big[\mathbf{1}\_{A}\int\_{0}^{1}\hat{m}^{\xi}(z)\mathrm{d}z\Big]=\int\_{0}^{1}\mathsf{E}\big[\mathbf{1}\_{A}\hat{m}^{\xi}(z)\big]\mathrm{d}z\geq\int\_{0}^{1}\mathsf{E}\big[\mathbf{1}\_{A}\mathcal{U}^{1}\_{0}\big]\mathrm{d}z=\mathsf{E}\big[\mathbf{1}\_{A}\mathcal{U}^{1}\_{0}\big], |  |

where the first equality is by Fubini’s theorem. This shows that 𝖯​(A)=0\mathsf{P}(A)=0 and ∫01m^ξ​(z)​dz≥𝒰01\int\_{0}^{1}\hat{m}^{\xi}(z)\mathrm{d}z\geq\mathcal{U}^{1}\_{0}, 𝖯\mathsf{P}-a.s. Combining the latter with ([4.15](https://arxiv.org/html/2510.15616v1#S4.E15 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) we obtain ([4.3](https://arxiv.org/html/2510.15616v1#S4.E3 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) with 𝖤​[Δ​ζ^T|ℱT1]​𝒰T1\mathsf{E}[\Delta\hat{\zeta}\_{T}|\mathcal{F}^{1}\_{T}]\mathcal{U}^{1}\_{T} replaced by 𝖤​[hT​Δ​ζ^T|ℱT1]\mathsf{E}[h\_{T}\Delta\hat{\zeta}\_{T}|\mathcal{F}^{1}\_{T}] as required. Analogous arguments with the use of ([4.14](https://arxiv.org/html/2510.15616v1#S4.E14 "In item ii ‣ Theorem 4.8. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) yield the desired result also for 𝒰02\mathcal{U}^{2}\_{0}.
∎

The above theorem does not employ candidate value processes 𝒰1\mathcal{U}^{1} and 𝒰2\mathcal{U}^{2}, so it does not suggest an approach for finding an equilibrium. In the next theorem, we relax conditions (i) and (ii) from Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") to hold only for systems 𝐌^0\hat{\bf M}^{0} and 𝐍^0\hat{\bf N}^{0} which are defined in ([4.1](https://arxiv.org/html/2510.15616v1#S4.E1 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and ([4.2](https://arxiv.org/html/2510.15616v1#S4.E2 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) with ξt=ζt=𝟏{t=T}\xi\_{t}=\zeta\_{t}=\mathbf{1}\_{\{t=T\}}. That is, we consider only

|  |  |  |  |
| --- | --- | --- | --- |
|  | M^0​(θ)\displaystyle\hat{M}^{0}(\theta) | =𝖤​[∫[0,θ)gt​dζ^t|ℱθ1]+𝖤​[1−ζ^θ−|ℱθ1]​𝒰θ1,\displaystyle=\mathsf{E}\Big[\int\_{[0,\theta)}g\_{t}\mathrm{d}\hat{\zeta}\_{t}\Big|\mathcal{F}^{1}\_{\theta}\Big]+\mathsf{E}\big[1-\hat{\zeta}\_{\theta-}\big|\mathcal{F}^{1}\_{\theta}\big]\mathcal{U}^{1}\_{\theta}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | N^0​(γ)\displaystyle\hat{N}^{0}(\gamma) | =𝖤​[∫[0,γ)ft​dξ^t|ℱγ2]+𝖤​[1−ξ^γ−|ℱγ2]​𝒰γ2,\displaystyle=\mathsf{E}\Big[\int\_{[0,\gamma)}f\_{t}\mathrm{d}\hat{\xi}\_{t}\Big|\mathcal{F}^{2}\_{\gamma}\Big]+\mathsf{E}\big[1-\hat{\xi}\_{\gamma-}\big|\mathcal{F}^{2}\_{\gamma}\big]\mathcal{U}^{2}\_{\gamma}, |  |

for (θ,γ)∈𝒯0​(𝔽1)×𝒯0​(𝔽2)(\theta,\gamma)\in\mathcal{T}\_{0}(\mathbb{F}^{1})\times\mathcal{T}\_{0}(\mathbb{F}^{2}). The price to pay for such relaxation is to add conditions (iii) and (iv) which are the analogue in this context of the necessary condition (i) in Proposition [3.17](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem17 "Proposition 3.17. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

###### Theorem 4.9.

Let (𝒰t1)t∈[0,T](\mathcal{U}^{1}\_{t})\_{t\in[0,T]} and (𝒰t2)t∈[0,T](\mathcal{U}^{2}\_{t})\_{t\in[0,T]} be 𝔽1\mathbb{F}^{1}- and 𝔽2\mathbb{F}^{2}-progressively measurable processes, respectively, and let (ξ^,ζ^)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\hat{\xi},\hat{\zeta})\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}). Assume that

1. (i)

   𝐌^0\hat{\bf M}^{0} is a 𝒯0​(𝔽1)\mathcal{T}\_{0}(\mathbb{F}^{1})-submartingale system,
2. (ii)

   𝐍^0\hat{\bf N}^{0} is a 𝒯0​(𝔽2)\mathcal{T}\_{0}(\mathbb{F}^{2})-supermartingale system,
3. (iii)

   (of⋅(1−ζ^⋅))t𝔽1+(oh⋅Δζ^⋅)t𝔽1≥(o1−ζ^⋅−)t𝔽1𝒰t1\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}f\_{\cdot}(1-\hat{\zeta}\_{\cdot})\big)\_{t}^{\mathbb{F}^{1}}+\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}h\_{\cdot}\Delta\hat{\zeta}\_{\cdot}\big)\_{t}^{\mathbb{F}^{1}}\geq\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-4.5449pt{o}\kern 2.12502pt}}\_{{\kern-1.66977pt\kern 2.12502pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-4.5449pt{o}\kern 2.12502pt}}\_{{\kern-1.66977pt\kern 2.12502pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-2.64682pt{o}\kern 0.90555pt}}\_{{\kern-0.4503pt\kern 0.90555pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-2.10239pt{o}\kern 0.36111pt}}\_{{\kern 0.09413pt\kern 0.36111pt}}}1-\hat{\zeta}\_{\cdot-})\_{t}^{\mathbb{F}^{1}}\,\mathcal{U}^{1}\_{t} for all t∈[0,T]t\in[0,T], 𝖯\mathsf{P}-a.s.,
4. (iv)

   (og⋅(1−ξ^⋅))t𝔽2+(oh⋅Δξ^⋅)t𝔽2≤(o1−ξ^⋅−)t𝔽2𝒰t2\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}g\_{\cdot}(1-\hat{\xi}\_{\cdot})\big)^{\mathbb{F}^{2}}\_{t}+\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}h\_{\cdot}\Delta\hat{\xi}\_{\cdot}\big)^{\mathbb{F}^{2}}\_{t}\leq\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-4.5449pt{o}\kern 2.12502pt}}\_{{\kern-1.66977pt\kern 2.12502pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-4.5449pt{o}\kern 2.12502pt}}\_{{\kern-1.66977pt\kern 2.12502pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-2.64682pt{o}\kern 0.90555pt}}\_{{\kern-0.4503pt\kern 0.90555pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-2.10239pt{o}\kern 0.36111pt}}\_{{\kern 0.09413pt\kern 0.36111pt}}}1-\hat{\xi}\_{\cdot-})\_{t}^{\mathbb{F}^{2}}\,\mathcal{U}^{2}\_{t} for all t∈[0,T]t\in[0,T], 𝖯\mathsf{P}-a.s.,
5. (v)

   𝖤​[𝒰01]=𝖤​[𝒰02]\mathsf{E}[\mathcal{U}^{1}\_{0}]=\mathsf{E}[\mathcal{U}^{2}\_{0}].

Then the game has a value, i.e., V¯=V¯=𝖤​[𝒰01]=𝖤​[𝒰02]\overline{V}=\underline{V}=\mathsf{E}[\mathcal{U}^{1}\_{0}]=\mathsf{E}[\mathcal{U}^{2}\_{0}], and the randomised stopping times (τ^,σ^)∈𝒯0R​(𝔽1)×𝒯0R​(𝔽2)(\hat{\tau},\hat{\sigma})\in\mathcal{T}^{R}\_{0}(\mathbb{F}^{1})\times\mathcal{T}^{R}\_{0}(\mathbb{F}^{2}) generated by (ξ^,ζ^)(\hat{\xi},\hat{\zeta}) form a saddle point of the game.

###### Proof.

We will closely follow ideas of the proof of Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). We will prove ([4.4](https://arxiv.org/html/2510.15616v1#S4.E4 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and skip analogous arguments for ([4.5](https://arxiv.org/html/2510.15616v1#S4.E5 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")). The rest of the proof follows similarly as the proof of Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

Take any ξ∈𝒜0∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1}) and set τ​(z)=inf{t≥0:ξt>z}∈𝒯​(𝔽1)\tau(z)=\inf\{t\geq 0:\xi\_{t}>z\}\in\mathcal{T}(\mathbb{F}^{1}). As in ([4.15](https://arxiv.org/html/2510.15616v1#S4.E15 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) we have

|  |  |  |  |
| --- | --- | --- | --- |
| (4.16) |  | 𝖤​[∫[0,T)ft​(1−ζ^t)​dξt+∫[0,T)gt​(1−ξt)​dζ^t+∑t∈[0,T)ht​Δ​ξt​Δ​ζ^t+hT​Δ​ξT​Δ​ζT|ℱ01]=∫01m^ξ​(z)​dz\displaystyle\mathsf{E}\Big[\!\int\_{[0,T)}\!\!f\_{t}(1\!-\!\hat{\zeta}\_{t})\mathrm{d}\xi\_{t}\!+\!\int\_{[0,T)}\!\!g\_{t}(1\!-\!\xi\_{t})\mathrm{d}\hat{\zeta}\_{t}\!+\!\!\sum\_{t\in[0,T)}\!\!h\_{t}\Delta\xi\_{t}\Delta\hat{\zeta}\_{t}\!+\!h\_{T}\Delta\xi\_{T}\Delta\zeta\_{T}\Big|\mathcal{F}^{1}\_{0}\Big]=\int\_{0}^{1}\hat{m}^{\xi}(z)\mathrm{d}z |  |

where (z,ω)↦m^ξ​(z,ω)(z,\omega)\mapsto\hat{m}^{\xi}(z,\omega) is ℬ​([0,T])×ℱ01\mathcal{B}([0,T])\times\mathcal{F}^{1}\_{0}-measurable and for each z∈[0,1]z\in[0,1] we have, 𝖯\mathsf{P}-a.s.,

|  |  |  |
| --- | --- | --- |
|  | m^​(z)=𝖤​[fτ​(z)​(1−ζ^τ​(z))+∫[0,τ​(z))gs​dζ^s+hτ​(z)​Δ​ζ^τ​(z)|ℱ01].\hat{m}(z)=\mathsf{E}\Big[f\_{\tau(z)}(1-\hat{\zeta}\_{\tau(z)})+\int\_{[0,\tau(z))}g\_{s}\mathrm{d}\hat{\zeta}\_{s}+h\_{\tau(z)}\Delta\hat{\zeta}\_{\tau(z)}\Big|\mathcal{F}^{1}\_{0}\Big]. |  |

By the definition of the optional projection and the tower property of conditional expectation, for any z∈(0,1)z\in(0,1), we have

|  |  |  |  |
| --- | --- | --- | --- |
| (4.17) |  | 𝖤​[fτ​(z)​(1−ζ^τ​(z))+∫[0,τ​(z))gs​dζ^s+hτ​(z)​Δ​ζ^τ​(z)|ℱ01]=𝖤​[∫[0,τ​(z))gs​dζ^s|ℱ01]+𝖤​[𝖤​[fτ​(z)​(1−ζ^τ​(z))+hτ​(z)​Δ​ζ^τ​(z)|ℱτ​(z)1]|ℱ01]=𝖤[∫[0,τ​(z))gsdζ^s|ℱ01]+𝖤[(of⋅(1−ζ^⋅−))τ​(z)𝔽1+(oh⋅Δζ^⋅)τ​(z)𝔽1|ℱ01]≥𝖤[∫[0,τ​(z))gsdζ^s+(o1−ζ^⋅−)τ​(z)𝔽1𝒰τ​(z)1|ℱ01]=𝖤​[∫[0,τ​(z))gs​dζ^s+𝖤​[1−ζ^τ​(z)−|ℱτ​(z)1]​𝒰τ​(z)1|ℱ01]≥𝒰01,\displaystyle\begin{aligned} &\mathsf{E}\Big[f\_{\tau(z)}(1-\hat{\zeta}\_{\tau(z)})+\int\_{[0,\tau(z))}g\_{s}\mathrm{d}\hat{\zeta}\_{s}+h\_{\tau(z)}\Delta\hat{\zeta}\_{\tau(z)}\Big|\mathcal{F}^{1}\_{0}\Big]\\ &=\mathsf{E}\Big[\int\_{[0,\tau(z))}g\_{s}\mathrm{d}\hat{\zeta}\_{s}\Big|\mathcal{F}^{1}\_{0}\Big]+\mathsf{E}\big[\mathsf{E}\big[f\_{\tau(z)}(1-\hat{\zeta}\_{\tau(z)})+h\_{\tau(z)}\Delta\hat{\zeta}\_{\tau(z)}\big|\mathcal{F}^{1}\_{\tau(z)}\big]\big|\mathcal{F}^{1}\_{0}\big]\\ &=\mathsf{E}\Big[\int\_{[0,\tau(z))}g\_{s}\mathrm{d}\hat{\zeta}\_{s}\Big|\mathcal{F}^{1}\_{0}\Big]+\mathsf{E}\big[\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}f\_{\cdot}(1-\hat{\zeta}\_{\cdot-})\big)\_{\tau(z)}^{\mathbb{F}^{1}}+\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}h\_{\cdot}\Delta\hat{\zeta}\_{\cdot}\big)\_{\tau(z)}^{\mathbb{F}^{1}}\big|\mathcal{F}^{1}\_{0}\big]\\ &\geq\mathsf{E}\Big[\int\_{[0,\tau(z))}g\_{s}\mathrm{d}\hat{\zeta}\_{s}+\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}1-\hat{\zeta}\_{\cdot-}\big)^{\mathbb{F}^{1}}\_{\tau(z)}\mathcal{U}^{1}\_{\tau(z)}\Big|\mathcal{F}^{1}\_{0}\Big]\\ &=\mathsf{E}\Big[\int\_{[0,\tau(z))}g\_{s}\mathrm{d}\hat{\zeta}\_{s}+\mathsf{E}\big[1-\hat{\zeta}\_{\tau(z)-}\big|\mathcal{F}^{1}\_{\tau(z)}\big]\,\mathcal{U}^{1}\_{\tau(z)}\Big|\mathcal{F}^{1}\_{0}\Big]\geq\mathcal{U}^{1}\_{0},\end{aligned} |  |

where the first inequality is by (iii) and the last one by the submartingale property (i) and the fact that ζ^0−=0\hat{\zeta}\_{0-}=0. Analogously to the proof of Theorem [4.8](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem8 "Theorem 4.8. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") we deduce ∫01m^ξ​(z)​dz≥𝒰01\int\_{0}^{1}\hat{m}^{\xi}(z)\mathrm{d}z\geq\mathcal{U}^{1}\_{0}. In summary, combining the latter with ([4.16](https://arxiv.org/html/2510.15616v1#S4.E16 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) we have proved

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[∫[0,T)ft​(1−ζ^t)​dξt+∫[0,T)gt​(1−ξt)​dζ^t+∑t∈[0,T)ht​Δ​ξt​Δ​ζ^t+(1−ξT−)​𝖤​[1−ζ^T−|ℱT1]​hT|ℱ01]≥𝒰01.\mathsf{E}\Big[\!\int\_{[0,T)}\!\!f\_{t}(1\!-\!\hat{\zeta}\_{t})\mathrm{d}\xi\_{t}\!+\!\int\_{[0,T)}\!\!g\_{t}(1\!-\!\xi\_{t})\mathrm{d}\hat{\zeta}\_{t}\!+\!\!\sum\_{t\in[0,T)}\!\!h\_{t}\Delta\xi\_{t}\Delta\hat{\zeta}\_{t}\!+\!(1\!-\!\xi\_{T-})\mathsf{E}[1\!-\!\hat{\zeta}\_{T-}|\mathcal{F}^{1}\_{T}]h\_{T}\Big|\mathcal{F}^{1}\_{0}\Big]\geq\mathcal{U}^{1}\_{0}. |  |

That is, we have ([4.4](https://arxiv.org/html/2510.15616v1#S4.E4 "In 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")). The remaining arguments in the proof of Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") apply and yield identical statement of the existence of value and the pair (ξ^,ζ^)(\hat{\xi},\hat{\zeta}) generating a saddle point of the game.
∎

###### Remark 4.10 (A link to full information games).

Theorem [4.9](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem9 "Theorem 4.9. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") provides parallels between the asymmetric information framework of this paper and the classical theory of zero-sum stopping games of [[LM84](https://arxiv.org/html/2510.15616v1#bib.bibx34)]. In the classical setting the game has one value process 𝒰\mathcal{U} which must satisfy ft≥𝒰t≥gtf\_{t}\geq\mathcal{U}\_{t}\geq g\_{t}, which is represented by conditions (iii) and (iv). For a candidate saddle point (τ^,σ^)(\hat{\tau},\hat{\sigma}), in the setting of [[LM84](https://arxiv.org/html/2510.15616v1#bib.bibx34)] the process 𝒰t∧σ^\mathcal{U}\_{t\wedge\hat{\sigma}} must be a supermartingale while the process 𝒰t∧τ^\mathcal{U}\_{t\wedge\hat{\tau}} must be a submartingale. Those properties are analogous to conditions (i) and (ii) in our theorem, respectively. Condition (v) is unique to the asymmetric setting, providing the only link between the candidate value processes 𝒰1\mathcal{U}^{1} and 𝒰2\mathcal{U}^{2}.

## 5. Applications to two classes of games

The setting introduced above is sufficiently general to cover nearly all known examples in the literature on Dynkin games with partial and asymmetric information. Here we consider two benchmark examples that illustrate how to write more explicit formulae for the players’ subjective views and players’ equilibrium values introduced in the previous sections.

In both examples, the underlying assumption is that both players know the structure of the game, in the sense that they know which processes and random variables are involved, although they may not observe their realisations. Moreover, both players know that there is an asymmetry of information and each player knows what type of information their opponent has access to.

The first example, in Section [5.1](https://arxiv.org/html/2510.15616v1#S5.SS1 "5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information"), is borrowed from [[Grü13](https://arxiv.org/html/2510.15616v1#bib.bibx24)] which, however, only considers a Markovian setting. We discuss the non-Markovian version of the game, whose in-depth study can be found in the PhD thesis [[Smi24](https://arxiv.org/html/2510.15616v1#bib.bibx41)]. The second example in Section [5.2](https://arxiv.org/html/2510.15616v1#S5.SS2 "5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") is borrowed from [[DAEG22](https://arxiv.org/html/2510.15616v1#bib.bibx9)], where a verification theorem is formulated and then used to solve a particular case of the general problem. Our analysis provides rigorous mathematical foundations for the verification theorem in [[DAEG22](https://arxiv.org/html/2510.15616v1#bib.bibx9)] which, otherwise, was the result of an educated guess.

### 5.1. Partially observed scenarios

Let (Ω,ℱ,𝖯)=(Ω0×Ω1,ℱ0×ℱ1,𝖯0×𝖯1)(\Omega,\mathcal{F},\mathsf{P})=(\Omega^{0}\times\Omega^{1},\mathcal{F}^{0}\times\mathcal{F}^{1},\mathsf{P}^{0}\times\mathsf{P}^{1}) be a product probability space. Let (ℋt)t∈[0,T](\mathcal{H}\_{t})\_{t\in[0,T]} be a filtration on (Ω0,ℱ0)(\Omega^{0},\mathcal{F}^{0}), with ℋ0={Ω0,∅}\mathcal{H}\_{0}=\{\Omega^{0},\varnothing\}, and denote by 𝔽2=(ℱt2)t∈[0,T]\mathbb{F}^{2}=(\mathcal{F}^{2}\_{t})\_{t\in[0,T]} the 𝖯0×𝖯1\mathsf{P}^{0}\times\mathsf{P}^{1}-completion of the filtration (ℋt×{Ω1,∅})t∈[0,T](\mathcal{H}\_{t}\times\{\Omega^{1},\varnothing\})\_{t\in[0,T]} (see Appendix [D](https://arxiv.org/html/2510.15616v1#A4 "Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information") for more details).
The space (Ω1,ℱ1,𝖯1)(\Omega^{1},\mathcal{F}^{1},\mathsf{P}^{1}) hosts a random variable 𝒥\mathcal{J} taking values 0 and 11 with 𝖯​(𝒥=1)=𝖯1​(𝒥=1)=π\mathsf{P}(\mathcal{J}=1)=\mathsf{P}^{1}(\mathcal{J}=1)=\pi. The analysis for 𝒥\mathcal{J} with any finite number of values is analogous. By construction 𝒥\mathcal{J}, considered as a r.v. on (Ω,ℱ,𝖯)(\Omega,\mathcal{F},\mathsf{P}), is independent of ℱT2\mathcal{F}^{2}\_{T}. Define a filtration 𝔽1\mathbb{F}^{1} as ℱt1=ℱt2∨σ​(𝒥)\mathcal{F}^{1}\_{t}=\mathcal{F}^{2}\_{t}\vee\sigma(\mathcal{J}) and notice that ℱT1≠ℱ\mathcal{F}^{1}\_{T}\neq\mathcal{F} as the probability space must also carry the randomisation devices for both players.

Let f0,f1,g0,g1,h0,h1∈ℒb​(𝖯)f^{0},f^{1},g^{0},g^{1},h^{0},h^{1}\in\mathcal{L}\_{b}(\mathsf{P}) be 𝔽2\mathbb{F}^{2}-adapted and such that ftj≥htj≥gtjf^{j}\_{t}\geq h^{j}\_{t}\geq g^{j}\_{t}, for all t∈[0,T]t\in[0,T], 𝖯\mathsf{P}-a.s., for j=0,1j=0,1.
We set

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (5.1) |  | ft=ft𝒥≔ft0​1{𝒥=0}+ft1​1{𝒥=1},gt=gt𝒥≔gt0​1{𝒥=0}+gt1​1{𝒥=1},ht=ht𝒥≔ht0​1{𝒥=0}+ht1​1{𝒥=1}.\displaystyle\begin{split}&f\_{t}=f^{\mathcal{J}}\_{t}\coloneqq f^{0}\_{t}1\_{\{\mathcal{J}=0\}}+f^{1}\_{t}1\_{\{\mathcal{J}=1\}},\\ &g\_{t}=g^{\mathcal{J}}\_{t}\coloneqq g^{0}\_{t}1\_{\{\mathcal{J}=0\}}+g^{1}\_{t}1\_{\{\mathcal{J}=1\}},\\ &h\_{t}=h^{\mathcal{J}}\_{t}\coloneqq h^{0}\_{t}1\_{\{\mathcal{J}=0\}}+h^{1}\_{t}1\_{\{\mathcal{J}=1\}}.\end{split} | |  |

Since ℱt1⊋ℱt2\mathcal{F}^{1}\_{t}\supsetneq\mathcal{F}^{2}\_{t}, we assume that Player 1 (minimiser) is fully informed whereas Player 2 (maximiser) is partially informed because she cannot observe directly 𝒥\mathcal{J}.

Thanks to Lemma [D.4](https://arxiv.org/html/2510.15616v1#A4.Thmtheorem4 "Lemma D.4. ‣ Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information"), any strategy ξ∈𝒜0∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1}) of the fully informed player decomposes as

|  |  |  |  |
| --- | --- | --- | --- |
| (5.2) |  | ξt=ξt0​𝟏{𝒥=0}+ξt1​𝟏{𝒥=1},\displaystyle\xi\_{t}=\xi^{0}\_{t}\mathbf{1}\_{\{\mathcal{J}=0\}}+\xi^{1}\_{t}\mathbf{1}\_{\{\mathcal{J}=1\}}, |  |

with ξj∈𝒜0∘​(𝔽2)\xi^{j}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}) for j=0,1j=0,1, whereas ζ∈𝒜0∘​(𝔽2)\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}). Notice that for θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}) the same decomposition leads to
θ=θ0​𝟏{𝒥=0}+θ1​𝟏{𝒥=1}\theta=\theta\_{0}\mathbf{1}\_{\{\mathcal{J}=0\}}+\theta\_{1}\mathbf{1}\_{\{\mathcal{J}=1\}},
with θ0,θ1∈𝒯0​(𝔽2)\theta\_{0},\theta\_{1}\in\mathcal{T}\_{0}(\mathbb{F}^{2}) (see, also, [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12), Corollary 3.2]).
That motivates treating the informed player as having two types/incarnations, the *incarnation 0* and the *incarnation 11*, potentially collaborating with each other.

Subjective views. Since the above decomposition holds for an optimal (ξ∗,ζ∗)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\xi^{\*},\zeta^{\*})\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}), then the processes defined in ([2.6](https://arxiv.org/html/2510.15616v1#S2.E6 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) read (recall the convention 0/0=10/0=1)

|  |  |  |
| --- | --- | --- |
|  | Πθ∗,1=1,θ∈𝒯0​(𝔽1),\displaystyle\Pi^{\*,1}\_{\theta}=1,\quad\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}), |  |
|  |  |  |
| --- | --- | --- |
|  | Πγ∗,2=(1−ξγ−∗,0)π​(1−ξγ−∗,1)+(1−π)​(1−ξγ−∗,0)​𝟏{𝒥=0}\displaystyle\Pi^{\*,2}\_{\gamma}=\frac{(1-\xi^{\*,0}\_{\gamma-})}{\pi(1-\xi^{\*,1}\_{\gamma-})+(1-\pi)(1-\xi^{\*,0}\_{\gamma-})}\mathbf{1}\_{\{\mathcal{J}=0\}} |  |
|  |  |  |
| --- | --- | --- |
|  | +(1−ξγ−∗,1)π​(1−ξγ−∗,1)+(1−π)​(1−ξγ−∗,0)​𝟏{𝒥=1},γ∈𝒯0​(𝔽2).\displaystyle\qquad\quad+\frac{(1-\xi^{\*,1}\_{\gamma-})}{\pi(1-\xi^{\*,1}\_{\gamma-})+(1-\pi)(1-\xi^{\*,0}\_{\gamma-})}\mathbf{1}\_{\{\mathcal{J}=1\}},\quad\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}). |  |

These processes as well as equilibrium values have an intuitive representation as long as the game is *still played*, by which we mean on the events

|  |  |  |
| --- | --- | --- |
|  | {ζθ−∗<1}={σ∗≥θ},and{ξγ−∗,1∧ξγ−∗,0<1}={𝖯​(τ∗≥γ|ℱγ2)>0}.\{\zeta^{\*}\_{\theta-}<1\}=\{\sigma^{\*}\geq\theta\},\quad\text{and}\quad\{\xi^{\*,1}\_{\gamma-}\wedge\xi^{\*,0}\_{\gamma-}<1\}=\{\mathsf{P}(\tau^{\*}\geq\gamma|\mathcal{F}^{2}\_{\gamma})>0\}. |  |

For γ∈𝒯0​(𝔽2)\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}), on the event {ξγ−∗,1∧ξγ−∗,0<1}\{\xi^{\*,1}\_{\gamma-}\wedge\xi^{\*,0}\_{\gamma-}<1\}, the expression for Πγ∗,2\Pi^{\*,2}\_{\gamma} simplifies to

|  |  |  |
| --- | --- | --- |
|  | Πγ∗,2=1−pγ1−π​𝟏{𝒥=0}+pγπ​𝟏{𝒥=1},\Pi^{\*,2}\_{\gamma}=\frac{1-p\_{\gamma}}{1-\pi}\mathbf{1}\_{\{\mathcal{J}=0\}}+\frac{p\_{\gamma}}{\pi}\mathbf{1}\_{\{\mathcal{J}=1\}}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
| (5.3) |  | pγ=π​(1−ξγ−∗,1)π​(1−ξγ−∗,1)+(1−π)​(1−ξγ−∗,0).p\_{\gamma}=\frac{\pi(1-\xi^{\*,1}\_{\gamma-})}{\pi(1-\xi^{\*,1}\_{\gamma-})+(1-\pi)(1-\xi^{\*,0}\_{\gamma-})}. |  |

The random variable pγp\_{\gamma} has a meaning of a *belief* of the partially informed player: it is indeed easy to verify that

|  |  |  |  |
| --- | --- | --- | --- |
| (5.4) |  | pγ=𝖯​(𝒥=1,τ∗≥γ|ℱγ2)𝖯​(τ∗≥γ|ℱγ2)on {ξγ−∗,1∧ξγ−∗,0<1},p\_{\gamma}=\frac{\mathsf{P}(\mathcal{J}=1,\tau\_{\*}\geq\gamma|\mathcal{F}^{2}\_{\gamma})}{\mathsf{P}(\tau\_{\*}\geq\gamma|\mathcal{F}^{2}\_{\gamma})}\quad\text{on $\{\xi^{\*,1}\_{\gamma-}\wedge\xi^{\*,0}\_{\gamma-}<1\}$}, |  |

where τ∗\tau\_{\*} is the randomised stopping time generated by (ξt∗)t∈[0,T](\xi^{\*}\_{t})\_{t\in[0,T]}. We also note that the conditional probability distribution (1−pγ,pγ)(1-p\_{\gamma},p\_{\gamma}) of 𝒥\mathcal{J} is absolutely continuous with respect to the initial distribution (1−π,π)(1-\pi,\pi) with the Radon-Nikodym density given by Πγ∗,2\Pi^{\*,2}\_{\gamma}.

Equilibrium value processes. Given a stopping time γ∈𝒯0​(𝔽2)\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}) we introduce the conditional expected payoffs in each state of 𝒥\mathcal{J}, i.e., for i=0,1i=0,1,

|  |  |  |  |
| --- | --- | --- | --- |
| (5.5) |  | Li​(ξi,ζ|ℱγ2)≔𝖤​[∫[γ,T)fti​(1−ζt)​dξti+∫[γ,T)gti​(1−ξti)​dζt+∑t∈[γ,T]hti​Δ​ζt​Δ​ξti|ℱγ2].\displaystyle L^{i}(\xi^{i},\zeta|\mathcal{F}^{2}\_{\gamma})\coloneqq\mathsf{E}\Big[\int\_{[\gamma,T)}f^{i}\_{t}(1-\zeta\_{t})\mathrm{d}\xi^{i}\_{t}+\int\_{[\gamma,T)}g^{i}\_{t}(1-\xi^{i}\_{t})\mathrm{d}\zeta\_{t}+\sum\_{t\in[\gamma,T]}h^{i}\_{t}\Delta\zeta\_{t}\Delta\xi^{i}\_{t}\Big|\mathcal{F}^{2}\_{\gamma}\Big]. |  |

Recalling that ζ∗;θ\zeta^{\*;\theta} and ξ∗,i;γ\xi^{\*,i;\gamma} denote the truncation of strategies ζ∗\zeta^{\*} and ξ∗,i\xi^{\*,i} at stopping times (θ,γ)∈𝒯0​(𝔽1)×𝒯0​(𝔽2)(\theta,\gamma)\in\mathcal{T}\_{0}(\mathbb{F}^{1})\times\mathcal{T}\_{0}(\mathbb{F}^{2}), we rewrite the formulae for the equilibrium values V∗,1V^{\*,1} and V∗,2V^{\*,2} (cf., ([2.13](https://arxiv.org/html/2510.15616v1#S2.E13 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information"))) using the above notation LiL^{i}. In particular, using Lemma [E.4](https://arxiv.org/html/2510.15616v1#A5.Thmtheorem4 "Lemma E.4. ‣ Appendix E Technical results for partially observed scenarios ‣ Martingale theory for Dynkin games with asymmetric information") in the third equality below we obtain on {ζθ−∗<1}\{\zeta^{\*}\_{\theta-}<1\}

|  |  |  |  |
| --- | --- | --- | --- |
|  | V∗,1​(θ)\displaystyle V^{\*,1}(\theta) | =ess​infξ∈𝒜θ∘​(𝔽1)⁡𝖤​[∫[θ,T)ft𝒥​(1−ζt∗;θ)​dξt+∫[θ,T)gt𝒥​(1−ξt)​dζt∗;θ+∑t∈[θ,T]ht𝒥​Δ​ζt∗;θ​Δ​ξt|ℱθ1]\displaystyle=\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\Big[\int\_{[\theta,T)}f^{\mathcal{J}}\_{t}(1-\zeta^{\*;\theta}\_{t})\mathrm{d}\xi\_{t}+\int\_{[\theta,T)}g^{\mathcal{J}}\_{t}(1-\xi\_{t})\mathrm{d}\zeta^{\*;\theta}\_{t}+\sum\_{t\in[\theta,T]}h^{\mathcal{J}}\_{t}\Delta\zeta^{\*;\theta}\_{t}\Delta\xi\_{t}\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ess​infξ∈𝒜θ∘​(𝔽1)𝖤[∑i=01𝟏{𝒥=i}(∫[θi,T)fti(1−ζt∗;θi)dξti+∫[θi,T)gti(1−ξti)dζt∗;θi\displaystyle=\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1})}\mathsf{E}\Big[\sum\_{i=0}^{1}\mathbf{1}\_{\{\mathcal{J}=i\}}\Big(\int\_{[\theta\_{i},T)}f^{i}\_{t}(1-\zeta^{\*;\theta\_{i}}\_{t})\mathrm{d}\xi^{i}\_{t}+\int\_{[\theta\_{i},T)}g^{i}\_{t}(1-\xi^{i}\_{t})\mathrm{d}\zeta^{\*;\theta\_{i}}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑t∈[θi,T]htiΔζt∗;θiΔξti)|ℱθ1]\displaystyle\hskip 265.0pt+\sum\_{t\in[\theta\_{i},T]}h^{i}\_{t}\Delta\zeta^{\*;\theta\_{i}}\_{t}\Delta\xi^{i}\_{t}\Big)\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝟏{𝒥=0}​ess​infξ0∈𝒜θ0∘​(𝔽2)⁡L0​(ξ0,ζ∗;θ0|ℱθ02)+𝟏{𝒥=1}​ess​infξ1∈𝒜θ1∘​(𝔽2)⁡L1​(ξ1,ζ∗;θ1|ℱθ12).\displaystyle=\mathbf{1}\_{\{\mathcal{J}=0\}}\operatorname\*{ess\,inf}\_{\xi^{0}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta\_{0}}(\mathbb{F}^{2})}L^{0}(\xi^{0},\zeta^{\*;\theta\_{0}}|\mathcal{F}^{2}\_{\theta\_{0}})+\mathbf{1}\_{\{\mathcal{J}=1\}}\operatorname\*{ess\,inf}\_{\xi^{1}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta\_{1}}(\mathbb{F}^{2})}L^{1}(\xi^{1},\zeta^{\*;\theta\_{1}}|\mathcal{F}^{2}\_{\theta\_{1}}). |  |

From the expression for Πγ∗,2\Pi^{\*,2}\_{\gamma} we get, on {ξγ−∗,1∧ξγ−∗,0<1}\{\xi^{\*,1}\_{\gamma-}\wedge\xi^{\*,0}\_{\gamma-}<1\},

|  |  |  |  |
| --- | --- | --- | --- |
|  | V∗,2​(γ)\displaystyle V^{\*,2}(\gamma) | =ess​supζ∈𝒜γ∘​(𝔽2)⁡JΠ∗,2​(ξ∗;γ,ζ|ℱγ2)=ess​supζ∈𝒜γ∘​(𝔽2)⁡(pγ​L1​(ξ∗,1;γ,ζ|ℱγ2)+(1−pγ)​L0​(ξ∗,0;γ,ζ|ℱγ2)),\displaystyle=\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\gamma}(\mathbb{F}^{2})}J^{\Pi^{\*,2}}(\xi^{\*;\gamma},\zeta|\mathcal{F}^{2}\_{\gamma})=\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\gamma}(\mathbb{F}^{2})}\Big(p\_{\gamma}L^{1}(\xi^{\*,1;\gamma},\zeta|\mathcal{F}^{2}\_{\gamma})+(1-p\_{\gamma})L^{0}(\xi^{\*,0;\gamma},\zeta|\mathcal{F}^{2}\_{\gamma})\Big), |  |

where the second equality holds thanks to independence of ℱT2\mathcal{F}^{2}\_{T} and σ​(𝒥)\sigma(\mathcal{J}).

The derived formulae for V∗,1​(θ)V^{\*,1}(\theta) and V∗,2​(γ)V^{\*,2}(\gamma) motivate the introduction of a new notation:

|  |  |  |
| --- | --- | --- |
|  | Ui​(θi)≔ess​infξi∈𝒜θi∘​(𝔽2)⁡Li​(ξi,ζ∗;θi|ℱθi2),i=0,1,andV​(γ)=V∗,2​(γ).U^{i}(\theta\_{i})\coloneqq\operatorname\*{ess\,inf}\_{\xi^{i}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta\_{i}}(\mathbb{F}^{2})}L^{i}(\xi^{i},\zeta^{\*;\theta\_{i}}|\mathcal{F}^{2}\_{\theta\_{i}}),\ i=0,1,\quad\text{and}\quad V(\gamma)=V^{\*,2}(\gamma). |  |

Notice that these objects are well-defined on the whole Ω\Omega but hold a meaning related to the game only on the events {ζθi−∗<1}\{\zeta^{\*}\_{\theta\_{i}-}<1\} and {ξγ−∗,0∧ξγ−∗,1<1}\{\xi^{\*,0}\_{\gamma-}\wedge\xi^{\*,1}\_{\gamma-}<1\}, respectively.
Thus, Ui​(θi)U^{i}(\theta\_{i}) is the value of the game at time θi\theta\_{i} for the ii-th incarnation of the informed player, while V​(γ)V(\gamma) is the value of the game at time γ\gamma for the uninformed player. For simplicity, it is convenient to denote

|  |  |  |
| --- | --- | --- |
|  | ⟨π,ϕ⟩=π​ϕ1+(1−π)​ϕ0,for any ϕ∈ℝ2.\langle\pi,\phi\rangle=\pi\phi^{1}+(1-\pi)\phi^{0},\quad\text{for any $\phi\in\mathbb{R}^{2}$.} |  |

Then, by Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), there are 𝔽2\mathbb{F}^{2}-optional processes (Ut0)t∈[0,T](U^{0}\_{t})\_{t\in[0,T]}, (Ut1)t∈[0,T](U^{1}\_{t})\_{t\in[0,T]} and (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]} such that

|  |  |  |  |
| --- | --- | --- | --- |
| (5.6) |  | (1−ζθi−∗)​Uθii=(1−ζθi−∗)​Ui​(θi),(1-\zeta^{\*}\_{\theta\_{i}-})U^{i}\_{\theta\_{i}}=(1-\zeta^{\*}\_{\theta\_{i}-})U^{i}(\theta\_{i}), |  |

for any 𝔽2\mathbb{F}^{2}-stopping time θi\theta\_{i}, and

|  |  |  |  |
| --- | --- | --- | --- |
| (5.7) |  | ⟨π,(1−ξγ−∗)⟩​Vγ=⟨π,(1−ξγ−∗)⟩​V​(γ),\langle\pi,(1-\xi^{\*}\_{\gamma-})\rangle V\_{\gamma}=\langle\pi,(1-\xi^{\*}\_{\gamma-})\rangle V(\gamma), |  |

for any 𝔽2\mathbb{F}^{2}-stopping time γ\gamma.
Thanks to ([3.4](https://arxiv.org/html/2510.15616v1#S3.E4 "In Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")), on {ζθi−∗<1}\{\zeta^{\*}\_{\theta\_{i}-}<1\}, we identify the process (Uti)t∈[0,T](U^{i}\_{t})\_{t\in[0,T]} with the value process of the following optimal stopping problem:

|  |  |  |  |
| --- | --- | --- | --- |
| (5.8) |  | Uθii=ess​infτ∈𝒯θi​(𝔽2)⁡𝖤​[fτi​(1−ζτ∗;θi)+∫[θi,τ)gti​dζt∗;θi+hτi​Δ​ζτ∗;θi|ℱθi2]=ess​infτ∈𝒯θi​(𝔽2)⁡Li​(τ,ζ∗;θi|ℱθi2),U^{i}\_{\theta\_{i}}=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta\_{i}}(\mathbb{F}^{2})}\mathsf{E}\Big[f^{i}\_{\tau}(1-\zeta^{\*;\theta\_{i}}\_{\tau})+\int\_{[\theta\_{i},\tau)}g^{i}\_{t}\mathrm{d}\zeta^{\*;\theta\_{i}}\_{t}+h^{i}\_{\tau}\Delta\zeta^{\*;\theta\_{i}}\_{\tau}\Big|\mathcal{F}^{2}\_{\theta\_{i}}\Big]=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta\_{i}}(\mathbb{F}^{2})}L^{i}(\tau,\zeta^{\*;\theta\_{i}}|\mathcal{F}^{2}\_{\theta\_{i}}), |  |

where in the final expression we slightly abuse the notation and write Li​(τ,ζ∗;θi|ℱθi2)L^{i}(\tau,\zeta^{\*;\theta\_{i}}|\mathcal{F}^{2}\_{\theta\_{i}}) for Li​(ξ,ζ∗;θi|ℱθi2)L^{i}(\xi,\zeta^{\*;\theta\_{i}}|\mathcal{F}^{2}\_{\theta\_{i}}) with ξt=𝟏{t≥τ}\xi\_{t}=\mathbf{1}\_{\{t\geq\tau\}}. Similarly, we write on {ξγ−∗,0∧ξγ−∗,1<1}\{\xi^{\*,0}\_{\gamma-}\wedge\xi^{\*,1}\_{\gamma-}<1\}

|  |  |  |  |
| --- | --- | --- | --- |
| (5.9) |  | Vγ=ess​supσ∈𝒯γ​(𝔽2)⁡𝖤​[∫[γ,σ)⟨pt,ft​d​ξt∗;γ⟩+⟨pσ,gσ​(1−ξσ∗;γ)+hσ​Δ​ξσ∗;γ⟩|ℱγ2]=ess​supσ∈𝒯γ​(𝔽2)⁡(pγ​L1​(ξ∗,1;γ,σ|ℱγ2)+(1−pγ)​L0​(ξ∗,0;γ,σ|ℱγ2)),\displaystyle\begin{aligned} V\_{\gamma}&=\operatorname\*{ess\,sup}\_{\sigma\in\mathcal{T}\_{\gamma}(\mathbb{F}^{2})}\mathsf{E}\Big[\int\_{[\gamma,\sigma)}\big\langle p\_{t},f\_{t}\mathrm{d}\xi^{\*;\gamma}\_{t}\big\rangle+\big\langle p\_{\sigma},g\_{\sigma}(1-\xi^{\*;\gamma}\_{\sigma})+h\_{\sigma}\Delta\xi^{\*;\gamma}\_{\sigma}\big\rangle\Big|\mathcal{F}^{2}\_{\gamma}\Big]\\ &=\operatorname\*{ess\,sup}\_{\sigma\in\mathcal{T}\_{\gamma}(\mathbb{F}^{2})}\Big(p\_{\gamma}L^{1}(\xi^{\*,1;\gamma},\sigma|\mathcal{F}^{2}\_{\gamma})+(1-p\_{\gamma})L^{0}(\xi^{\*,0;\gamma},\sigma|\mathcal{F}^{2}\_{\gamma})\Big),\end{aligned} |  |

where ⟨pt,ft​d​ξt∗;γ⟩=pt​ft1​d​ξt∗,1;γ+(1−pt)​ft0​d​ξt∗,1;γ\langle p\_{t},f\_{t}\mathrm{d}\xi^{\*;\gamma}\_{t}\rangle=p\_{t}f^{1}\_{t}\mathrm{d}\xi^{\*,1;\gamma}\_{t}+(1-p\_{t})f^{0}\_{t}\mathrm{d}\xi^{\*,1;\gamma}\_{t} (and analogously for the other terms) and Li​(ξ∗,i;γ,σ|ℱγ2)L^{i}(\xi^{\*,i;\gamma},\sigma|\mathcal{F}^{2}\_{\gamma}) stands for Li​(ξ∗,i;γ,ζ|ℱγ2)L^{i}(\xi^{\*,i;\gamma},\zeta|\mathcal{F}^{2}\_{\gamma}) with ζ=𝟏{t≥σ}\zeta=\mathbf{1}\_{\{t\geq\sigma\}}.

Relationship between players’ equilibrium values and the role of the belief process. From the second statement in Remark [3.12](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem12 "Remark 3.12. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), we have the relationship

|  |  |  |
| --- | --- | --- |
|  | (1−ζγ−∗)​𝖤​[(1−ξγ−∗)​V∗,1​(γ)|ℱγ2]=𝖤​[1−ξγ−∗|ℱγ2]​(1−ζγ−∗)​V∗,2​(γ)(1-\zeta^{\*}\_{\gamma-})\mathsf{E}\big[(1-\xi^{\*}\_{\gamma-})V^{\*,1}(\gamma)|\mathcal{F}^{2}\_{\gamma}\big]=\mathsf{E}\big[1-\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}\big](1-\zeta^{\*}\_{\gamma-})V^{\*,2}(\gamma) |  |

for any γ∈𝒯​(𝔽2)\gamma\in\mathcal{T}(\mathbb{F}^{2}). Noticing that 𝖤​[1−ξγ−∗|ℱγ2]=⟨π,1−ξγ−∗⟩\mathsf{E}\big[1-\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}\big]=\langle\pi,1-\xi^{\*}\_{\gamma-}\rangle, the right-hand side reads

|  |  |  |
| --- | --- | --- |
|  | ⟨π,1−ξγ−∗⟩​(1−ζγ−∗)​V∗,2​(γ)=⟨π,1−ξγ−∗⟩​(1−ζγ−∗)​Vγ\langle\pi,1-\xi^{\*}\_{\gamma-}\rangle(1-\zeta^{\*}\_{\gamma-})V^{\*,2}(\gamma)=\langle\pi,1-\xi^{\*}\_{\gamma-}\rangle(1-\zeta^{\*}\_{\gamma-})V\_{\gamma} |  |

with the equality justified by ([5.7](https://arxiv.org/html/2510.15616v1#S5.E7 "In 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")). For the left-hand side, we write

|  |  |  |
| --- | --- | --- |
|  | (1−ζγ−∗)​𝖤​[(1−ξγ−∗)​V∗,1​(γ)|ℱγ2]\displaystyle(1-\zeta^{\*}\_{\gamma-})\mathsf{E}\big[(1-\xi^{\*}\_{\gamma-})V^{\*,1}(\gamma)\big|\mathcal{F}^{2}\_{\gamma}\big] |  |
|  |  |  |
| --- | --- | --- |
|  | =𝖤​[(1−ζγ−∗)​(𝟏{𝒥=1}​(1−ξγ−∗,1)​U1​(γ)+𝟏{𝒥=0}​(1−ξγ−∗,0)​U0​(γ))|ℱγ2]\displaystyle=\mathsf{E}\big[(1-\zeta^{\*}\_{\gamma-})\big(\mathbf{1}\_{\{\mathcal{J}=1\}}(1-\xi^{\*,1}\_{\gamma-})U^{1}(\gamma)+\mathbf{1}\_{\{\mathcal{J}=0\}}(1-\xi^{\*,0}\_{\gamma-})U^{0}(\gamma)\big)\big|\mathcal{F}^{2}\_{\gamma}\big] |  |
|  |  |  |
| --- | --- | --- |
|  | =(1−ζγ−∗)​(1−ξγ−∗,1)​Uγ1​𝖤​[𝟏{𝒥=1}|ℱγ2]+(1−ζγ−∗)​(1−ξγ−∗,0)​Uγ0​𝖤​[𝟏{𝒥=0}|ℱγ2]\displaystyle=(1-\zeta^{\*}\_{\gamma-})(1-\xi^{\*,1}\_{\gamma-})U^{1}\_{\gamma}\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=1\}}\big|\mathcal{F}^{2}\_{\gamma}\big]+(1-\zeta^{\*}\_{\gamma-})(1-\xi^{\*,0}\_{\gamma-})U^{0}\_{\gamma}\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=0\}}\big|\mathcal{F}^{2}\_{\gamma}\big] |  |
|  |  |  |
| --- | --- | --- |
|  | =(1−ζγ−∗)​(1−ξγ−∗,1)​Uγ1​π+(1−ζγ−∗)​(1−ξγ−∗,0)​Uγ0​(1−π)\displaystyle=(1-\zeta^{\*}\_{\gamma-})(1-\xi^{\*,1}\_{\gamma-})U^{1}\_{\gamma}\pi+(1-\zeta^{\*}\_{\gamma-})(1-\xi^{\*,0}\_{\gamma-})U^{0}\_{\gamma}(1-\pi) |  |
|  |  |  |
| --- | --- | --- |
|  | =⟨π,1−ξγ−∗⟩​(1−ζγ−∗)​(pγ​Uγ1+(1−pγ)​Uγ0),\displaystyle=\langle\pi,1-\xi^{\*}\_{\gamma-}\rangle(1-\zeta^{\*}\_{\gamma-})\big(p\_{\gamma}U^{1}\_{\gamma}+(1-p\_{\gamma})U^{0}\_{\gamma}\big), |  |

where the decomposition ([5.2](https://arxiv.org/html/2510.15616v1#S5.E2 "In 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) of ξ∗\xi^{\*} was used in the first inequality, ([5.6](https://arxiv.org/html/2510.15616v1#S5.E6 "In 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) in the second equality, and the last equality follows from the definition of pγp\_{\gamma}. In conclusion, we have

|  |  |  |
| --- | --- | --- |
|  | ⟨π,1−ξγ−∗⟩​(1−ζγ−∗)​(pγ​Uγ1+(1−pγ)​Uγ0)=⟨π,1−ξγ−∗⟩​(1−ζγ−∗)​Vγ,\langle\pi,1-\xi^{\*}\_{\gamma-}\rangle(1-\zeta^{\*}\_{\gamma-})\big(p\_{\gamma}U^{1}\_{\gamma}+(1-p\_{\gamma})U^{0}\_{\gamma}\big)=\langle\pi,1-\xi^{\*}\_{\gamma-}\rangle(1-\zeta^{\*}\_{\gamma-})V\_{\gamma}, |  |

which is best viewed as the equality

|  |  |  |  |
| --- | --- | --- | --- |
| (5.10) |  | ⟨pγ,Uγ⟩=Vγon the set Γγ2,\langle p\_{\gamma},U\_{\gamma}\rangle=V\_{\gamma}\qquad\text{on the set $\Gamma^{2}\_{\gamma}$,} |  |

where Γγ2\Gamma^{2}\_{\gamma} is defined in Proposition [3.8](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). This set takes an explicit form here:

|  |  |  |  |
| --- | --- | --- | --- |
| (5.11) |  | Γγ2={ξγ−∗,1∧ξγ−∗,0<1​ and ​ζγ−∗<1}.\displaystyle\Gamma^{2}\_{\gamma}=\{\xi^{\*,1}\_{\gamma-}\wedge\xi^{\*,0}\_{\gamma-}<1\text{ and }\zeta^{\*}\_{\gamma-}<1\}. |  |

That lends a natural interpretation of ([5.10](https://arxiv.org/html/2510.15616v1#S5.E10 "In 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) as being true as long as the optimally played game has positive probability to still being played at time γ\gamma.

Martingale characterisation. Take ξ=(ξ0,ξ1)∈𝒜0∘​(𝔽1)\xi=(\xi^{0},\xi^{1})\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1}) and ζ∈𝒜0∘​(𝔽2)\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}), and recall the 𝔽1\mathbb{F}^{1}-optional submartingale (Mtξ)t∈[0,T](M^{\xi}\_{t})\_{t\in[0,T]} and the 𝔽2\mathbb{F}^{2}-optional supermartingale (Ntζ)t∈[0,T](N^{\zeta}\_{t})\_{t\in[0,T]} from Proposition [3.9](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem9 "Proposition 3.9. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). They take the following form in this model: for any θ=(θ1,θ2)∈𝒯0​(𝔽1)\theta=(\theta^{1},\theta^{2})\in\mathcal{T}\_{0}(\mathbb{F}^{1}) and γ∈𝒯0​(𝔽2)\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2})

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mθξ\displaystyle M^{\xi}\_{\theta} | =∑i=01𝟏{𝒥=i}​(∫[0,θi)[(1−ζt∗)​fti+Δ​ζt∗​hti]​dξti+∫[0,θi)(1−ξti)​gti​dζt∗+(1−ξθi−i)​(1−ζθi−∗)​Uθii)\displaystyle=\sum\_{i=0}^{1}\mathbf{1}\_{\{\mathcal{J}=i\}}\Big(\int\_{[0,\theta\_{i})}\big[(1-\zeta^{\*}\_{t})f^{i}\_{t}+\Delta\zeta^{\*}\_{t}h^{i}\_{t}\big]\mathrm{d}\xi^{i}\_{t}+\int\_{[0,\theta\_{i})}(1-\xi^{i}\_{t})g^{i}\_{t}\mathrm{d}\zeta^{\*}\_{t}+(1-\xi^{i}\_{\theta\_{i}-})(1-\zeta^{\*}\_{\theta\_{i}-})U^{i}\_{\theta\_{i}}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =:𝟏{𝒥=0}Mθ0ξ0;0+𝟏{𝒥=1}Mθ1ξ1;1,\displaystyle=:\mathbf{1}\_{\{\mathcal{J}=0\}}M^{\xi^{0};0}\_{\theta\_{0}}+\mathbf{1}\_{\{\mathcal{J}=1\}}M^{\xi^{1};1}\_{\theta\_{1}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Nγζ\displaystyle N^{\zeta}\_{\gamma} | =∑i=01πi​(∫[0,γ)[(1−ζt)​fti+Δ​ζt​hti]​dξt∗,i+∫[0,γ)(1−ξt∗,i)​gti​dζt+(1−ξγ−∗,i)​(1−ζγ−)​Vγ),\displaystyle=\sum\_{i=0}^{1}\pi\_{i}\Big(\int\_{[0,\gamma)}\big[(1-\zeta\_{t})f^{i}\_{t}+\Delta\zeta\_{t}h^{i}\_{t}\big]\mathrm{d}\xi^{\*,i}\_{t}+\int\_{[0,\gamma)}(1-\xi^{\*,i}\_{t})g^{i}\_{t}\mathrm{d}\zeta\_{t}+(1-\xi^{\*,i}\_{\gamma-})(1-\zeta\_{\gamma-})V\_{\gamma}\Big), |  |

where (Mtξ;i)t∈[0,T](M^{\xi;i}\_{t})\_{t\in[0,T]}, i=0,1i=0,1, are 𝔽2\mathbb{F}^{2}-optional submartingales. When ξ\xi and ζ\zeta are chosen optimally, the processes (Mtξ∗,0;0)t∈[0,T](M^{\xi^{\*,0};0}\_{t})\_{t\in[0,T]}, (Mtξ∗,1;1)t∈[0,T](M^{\xi^{\*,1};1}\_{t})\_{t\in[0,T]} and (Ntζ∗)t∈[0,T](N^{\zeta^{\*}}\_{t})\_{t\in[0,T]} become càdlàg 𝔽2\mathbb{F}^{2}-martingales by Proposition [3.8](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). On the other hand, when ξ\xi and ζ\zeta are taken equal to zero, the above processes take the form: for t∈[0,T]t\in[0,T],

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (5.12) |  | Mt0;i\displaystyle M^{0;i}\_{t} | =∫[0,t)gsi​dζs∗+(1−ζt−∗)​Uti,i=0,1,\displaystyle=\int\_{[0,t)}g^{i}\_{s}\mathrm{d}\zeta^{\*}\_{s}+(1-\zeta^{\*}\_{t-})U^{i}\_{t},\qquad i=0,1, |  |
|  | Nt0\displaystyle N^{0}\_{t} | =∑i=01πi​(∫[0,t)fsi​dξs∗,i+(1−ξt−∗,i)​Vt).\displaystyle=\sum\_{i=0}^{1}\pi\_{i}\Big(\int\_{[0,t)}f^{i}\_{s}\mathrm{d}\xi^{\*,i}\_{s}+(1-\xi^{\*,i}\_{t-})V\_{t}\Big). |  |

Proposition [3.7](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem7 "Proposition 3.7. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") asserts that (Mt0;i)(M^{0;i}\_{t}) is a càdlàg 𝔽2\mathbb{F}^{2}-submartingale and (Nt0)(N^{0}\_{t}) is a càdlàg 𝔽2\mathbb{F}^{2}-supermartingale. These can be shown to be martingales up to the “last optimal stopping time” for the respective player in the following way. We first recall the notation ([3.10](https://arxiv.org/html/2510.15616v1#S3.E10 "In 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) and adapt it to the present setting as

|  |  |  |
| --- | --- | --- |
|  | τ¯∗i​(z)=inf{t∈[0,T]:ξt∗,i>z}andσ¯∗​(z)=inf{t∈[0,T]:ζt∗>z},\bar{\tau}\_{\*}^{i}(z)=\inf\{t\in[0,T]:\xi^{\*,i}\_{t}>z\}\quad\text{and}\quad\bar{\sigma}\_{\*}(z)=\inf\{t\in[0,T]:\zeta^{\*}\_{t}>z\}, |  |

for z∈[0,1)z\in[0,1). Corollary [3.16](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem16 "Corollary 3.16. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") then yields that (Mt∧τ¯∗i​(z)0;i)(M^{0;i}\_{t\wedge\bar{\tau}^{i}\_{\*}(z)}) is an 𝔽2\mathbb{F}^{2}-martingale for any z∈[0,1)z\in[0,1) and (Nt∧σ¯∗​(z)0)(N^{0}\_{t\wedge\bar{\sigma}\_{\*}(z)}) is an 𝔽2\mathbb{F}^{2}-martingale for any z∈[0,1)z\in[0,1). If any of the generating processes ξ∗,i\xi^{\*,i} or ζ∗\zeta^{\*} has a jump at TT, the respective processes are martingales on the full interval [0,T][0,T].

Support of optimal strategies. In line with the statement of Proposition [3.17](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem17 "Proposition 3.17. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), given an optimal pair (ξ∗,ζ∗)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\xi^{\*},\zeta^{\*})\in\mathcal{A}^{\circ}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\circ}\_{0}(\mathbb{F}^{2}), define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt1\displaystyle Y^{1}\_{t} | =∑i=01𝟏{𝒥=i}((1−ζt−∗)Uti−fti(1−ζt∗)−htiΔζt∗)=:𝟏{𝒥=0}Zt0+𝟏{𝒥=1}Zt1,\displaystyle=\sum\_{i=0}^{1}\mathbf{1}\_{\{\mathcal{J}=i\}}\big((1-\zeta^{\*}\_{t-})U^{i}\_{t}-f^{i}\_{t}(1-\zeta^{\*}\_{t})-h^{i}\_{t}\Delta\zeta^{\*}\_{t}\big)=:\mathbf{1}\_{\{\mathcal{J}=0\}}Z^{0}\_{t}+\mathbf{1}\_{\{\mathcal{J}=1\}}Z^{1}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt2\displaystyle Y^{2}\_{t} | =⟨π,1−ξt−∗⟩​Vt−⟨π,gt​(1−ξt∗)+ht​Δ​ξt∗⟩,\displaystyle=\langle\pi,1-\xi^{\*}\_{t-}\rangle V\_{t}-\langle\pi,g\_{t}(1-\xi^{\*}\_{t})+h\_{t}\Delta\xi^{\*}\_{t}\rangle, |  |

where we interpret gt​(1−ξt∗)+ht​Δ​ξt∗g\_{t}(1-\xi^{\*}\_{t})+h\_{t}\Delta\xi^{\*}\_{t} as a vector with entries gti​(1−ξt∗,i)+hti​Δ​ξt∗,ig^{i}\_{t}(1-\xi^{\*,i}\_{t})+h^{i}\_{t}\Delta\xi^{\*,i}\_{t}, i=0,1i=0,1.
These processes have a more convenient representation as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zti\displaystyle Z^{i}\_{t} | =(Uti−fti)​(1−ζt∗)+(Uti−hti)​Δ​ζt∗,i=0,1,\displaystyle=(U^{i}\_{t}-f^{i}\_{t})(1-\zeta^{\*}\_{t})+(U^{i}\_{t}-h^{i}\_{t})\Delta\zeta^{\*}\_{t},\quad i=0,1, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt2\displaystyle Y^{2}\_{t} | =∑i=01πi​((Vt−gti)​(1−ξt∗,i)+(Vt−hti)​Δ​ξt∗,i).\displaystyle=\sum\_{i=0}^{1}\pi\_{i}\big((V\_{t}-g^{i}\_{t})(1-\xi^{\*,i}\_{t})+(V\_{t}-h^{i}\_{t})\Delta\xi^{\*,i}\_{t}\big). |  |

###### Corollary 5.1.

We have Zt0≤0Z^{0}\_{t}\leq 0, Zt1≤0Z^{1}\_{t}\leq 0 and Yt2≥0Y^{2}\_{t}\geq 0 for all t∈[0,T]t\in[0,T], 𝖯\mathsf{P}-a.s. Moreover,

|  |  |  |
| --- | --- | --- |
|  | ∫[0,T]Zt0​dξt∗,0+∫[0,T]Zt1​dξt∗,1=0,and∫[0,T]Yt2​dζt∗=0.\displaystyle\int\_{[0,T]}Z^{0}\_{t}\mathrm{d}\xi^{\*,0}\_{t}+\int\_{[0,T]}Z^{1}\_{t}\mathrm{d}\xi^{\*,1}\_{t}=0,\quad\text{and}\quad\int\_{[0,T]}Y^{2}\_{t}\mathrm{d}\zeta^{\*}\_{t}=0. |  |

To better appreciate the conclusions of the above corollary, it is useful to assume that (ξt∗)t∈[0,T](\xi^{\*}\_{t})\_{t\in[0,T]} and (ζt∗)t∈[0,T](\zeta^{\*}\_{t})\_{t\in[0,T]} do not jump simultaneously for t<Tt<T. This is to be expected if fti>hti>gtif^{i}\_{t}>h^{i}\_{t}>g^{i}\_{t} for every t∈[0,T)t\in[0,T): intuitively, a simultaneous jump at time t∈[0,T)t\in[0,T) corresponds to the players stopping simultaneously at time tt with some probability; that yields a payoff htih^{i}\_{t}; each player would then prefer to delay her own jump, in order to score the more preferable payoff ftif^{i}\_{t} (for the maximiser) or gtig^{i}\_{t} (for the minimiser).
In the absence of simultaneous jumps, the statement of Corollary [5.1](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem1 "Corollary 5.1. ‣ 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") can be rewritten in a more intuitive way as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (5.13) |  |  | ∫[0,T)(Uti−fti)​(1−ζt∗)​dξt∗,i=0,\displaystyle\int\_{[0,T)}(U^{i}\_{t}-f^{i}\_{t})(1-\zeta^{\*}\_{t})\mathrm{d}\xi^{\*,i}\_{t}=0, |  |
|  |  | (UTi−hTi)​Δ​ζT∗​Δ​ξT∗,i=0,\displaystyle(U^{i}\_{T}-h^{i}\_{T})\Delta\zeta^{\*}\_{T}\Delta\xi^{\*,i}\_{T}=0, |  |

for i=0,1i=0,1, and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (5.14) |  |  | ∫[0,T)⟨π,(1−ξt−∗)⟩​(Vt−⟨pt,gt⟩)​dζt∗=0,\displaystyle\int\_{[0,T)}\langle\pi,(1-\xi^{\*}\_{t-})\rangle\big(V\_{t}-\langle p\_{t},g\_{t}\rangle\big)\mathrm{d}\zeta^{\*}\_{t}=0, |  |
|  |  | ⟨π,(1−ξT−∗)⟩​(VT−⟨pT,hT⟩)​Δ​ζT∗=0.\displaystyle\langle\pi,(1-\xi^{\*}\_{T-})\rangle\big(V\_{T}-\langle p\_{T},h\_{T}\rangle\big)\Delta\zeta^{\*}\_{T}=0. |  |

Equation ([5.14](https://arxiv.org/html/2510.15616v1#S5.E14 "In 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) shows that the uninformed player acts only when her value process (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]} coincides with the believed payoff ⟨pt,gt⟩\langle p\_{t},g\_{t}\rangle. Moreover, if the game has not ended by time TT, it must be VT=⟨pT,hT⟩V\_{T}=\langle p\_{T},h\_{T}\rangle. Similarly, equation ([5.13](https://arxiv.org/html/2510.15616v1#S5.E13 "In 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) shows that the ii-th incarnation of the informed player acts when either her value process (Uti)t∈[0,T](U^{i}\_{t})\_{t\in[0,T]} coincides with her payoff (fti)t∈[0,T](f^{i}\_{t})\_{t\in[0,T]}, or at the terminal time TT.

We now proceed to show an interesting feature of the solution of games with asymmetric information: the equilibrium value process of the opponent determines a player’s behaviour. To this end, we refer the reader to Corollary [3.19](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem19 "Corollary 3.19. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") and proceed to define objects appearing there. Let U¯ti=(1−ζt−∗)​Uti\bar{U}^{i}\_{t}=(1-\zeta^{\*}\_{t-})U^{i}\_{t}, i=0,1i=0,1, and V¯t=⟨pt,(1−ξt−∗)⟩​Vt\bar{V}\_{t}=\langle p\_{t},(1-\xi^{\*}\_{t-})\rangle V\_{t}. The optional projections in ([3.63](https://arxiv.org/html/2510.15616v1#S3.E63 "In Corollary 3.19. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")) are related to the processes

|  |  |  |
| --- | --- | --- |
|  | t↦∫[0,t)gsi​dζs∗,i=0,1,andt↦∫[0,t)⟨pt,fs​d​ξs∗⟩,t\mapsto\int\_{[0,t)}g^{i}\_{s}\mathrm{d}\zeta^{\*}\_{s},\quad i=0,1,\qquad\text{and}\qquad t\mapsto\int\_{[0,t)}\langle p\_{t},f\_{s}\mathrm{d}\xi^{\*}\_{s}\rangle, |  |

and assumed to be continuous. According to Corollary [3.19](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem19 "Corollary 3.19. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), the previsible bounded variation process in the semimartingale decomposition of each of the processes (U¯t∧τ∗​(z)i)(\bar{U}^{i}\_{t\wedge\tau\_{\*}(z)}) is equal to −∫[0,t∧τ∗​(z))gsi​dζs∗-\int\_{[0,t\wedge\tau\_{\*}(z))}g^{i}\_{s}\mathrm{d}\zeta^{\*}\_{s} for any z∈[0,1)z\in[0,1), i.e., value processes of each incarnation of the informed player determine the optimal strategy of the uninformed player. Analogously, the previsible bounded variation process in the semimartingale decomposition of the value process (V¯t∧σ∗​(z))(\bar{V}\_{t\wedge\sigma\_{\*}(z)}) of the uninformed player equals −∫[0,t∧σ∗​(z))⟨pt,fs​d​ξs∗⟩-\int\_{[0,t\wedge\sigma\_{\*}(z))}\langle p\_{t},f\_{s}\mathrm{d}\xi^{\*}\_{s}\rangle. In full generality, this may not be sufficient to find strategies of both incarnations of the informed player – particularly because processes U0U^{0}, U1U^{1} and VV are not known explicitly and, if they were, there may be multiple ways of choosing (ξ∗,ζ∗)(\xi^{\*},\zeta^{\*}) so as to satisfy the requirements of Corollary [3.19](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem19 "Corollary 3.19. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). However, this information can be combined with the supports of those strategies, see ([5.13](https://arxiv.org/html/2510.15616v1#S5.E13 "In 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")), to identify the incarnation/player who needs to act at a given time tt.

Sufficient conditions. We first rewrite assumptions of Theorem [4.9](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem9 "Theorem 4.9. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") explicitly in the form of the next corollary.

###### Corollary 5.2.

Let (U^t0)t∈[0,T](\hat{U}^{0}\_{t})\_{t\in[0,T]}, (U^t1)t∈[0,T](\hat{U}^{1}\_{t})\_{t\in[0,T]}, (V^t)t∈[0,T](\hat{V}\_{t})\_{t\in[0,T]} be 𝔽2\mathbb{F}^{2}-progressively measurable processes, let ξ^0,ξ^1,ζ^∈𝒜0∘​(𝔽2)\hat{\xi}^{0},\hat{\xi}^{1},\hat{\zeta}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}) and denote by p^t\hat{p}\_{t} an analogue of ([5.3](https://arxiv.org/html/2510.15616v1#S5.E3 "In 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) with ξ^j\hat{\xi}^{j} in place of ξ∗,j\xi^{\*,j}. Set

|  |  |  |  |
| --- | --- | --- | --- |
|  | M^t0;i\displaystyle\hat{M}^{0;i}\_{t} | =∫[0,t)gsi​dζ^s+(1−ζ^t−)​U^ti,\displaystyle=\int\_{[0,t)}g^{i}\_{s}\mathrm{d}\hat{\zeta}\_{s}+(1-\hat{\zeta}\_{t-})\hat{U}^{i}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | N^t0\displaystyle\hat{N}^{0}\_{t} | =∑i=01πi​(∫[0,t)fsi​dξ^si+(1−ξ^t−i)​V^t)=∫[0,t)⟨π,fs​d​ξ^s⟩+⟨π,1−ξ^t−⟩​V^t.\displaystyle=\sum\_{i=0}^{1}\pi\_{i}\Big(\int\_{[0,t)}f^{i}\_{s}\mathrm{d}\hat{\xi}^{i}\_{s}+(1-\hat{\xi}^{i}\_{t-})\hat{V}\_{t}\Big)=\int\_{[0,t)}\langle\pi,f\_{s}\mathrm{d}\hat{\xi}\_{s}\rangle+\langle\pi,1-\hat{\xi}\_{t-}\rangle\hat{V}\_{t}. |  |

Assume that

1. (i)

   the process (M^t0;i)t∈[0,T](\hat{M}^{0;i}\_{t})\_{t\in[0,T]} is an 𝔽2\mathbb{F}^{2}-submartingale for i=0,1i=0,1,
2. (ii)

   the process (N^t0)t∈[0,T](\hat{N}^{0}\_{t})\_{t\in[0,T]} is an 𝔽2\mathbb{F}^{2}-supermartingale,
3. (iii)

   for i=0,1i=0,1, it holds 𝖯\mathsf{P}-a.s.,

   |  |  |  |
   | --- | --- | --- |
   |  | fti+(hti−fti)​Δ​ζ^t1−ζ^t−≥U^ti,for all t∈[0,T] such that ζ^t−<1,f^{i}\_{t}+(h^{i}\_{t}-f^{i}\_{t})\frac{\Delta\hat{\zeta}\_{t}}{1-\hat{\zeta}\_{t-}}\geq\hat{U}^{i}\_{t},\quad\text{for all $t\in[0,T]$ such that $\hat{\zeta}\_{t-}<1$}, |  |
4. (iv)

   it holds 𝖯\mathsf{P}-a.s.,

   |  |  |  |
   | --- | --- | --- |
   |  | ⟨p^t,gt⟩+⟨π,(ht−gt)​Δ​ξ^t⟩⟨π,1−ξ^t−⟩≤V^t,for all t∈[0,T] such that ⟨π,1−ξ^t−⟩>0 ,\langle\hat{p}\_{t},g\_{t}\rangle+\frac{\langle\pi,(h\_{t}-g\_{t})\Delta\hat{\xi}\_{t}\rangle}{\langle\pi,1-\hat{\xi}\_{t-}\rangle}\leq\hat{V}\_{t},\quad\text{for all $t\in[0,T]$ such that $\langle\pi,1-\hat{\xi}\_{t-}\rangle>0$ }, |  |
5. (v)

   V^0=⟨π,U^0⟩\hat{V}\_{0}=\langle\pi,\hat{U}\_{0}\rangle.

Then the value of the game equals V^0\hat{V}\_{0} and a saddle point is given by ((ξ^0,ξ^1),ζ^)((\hat{\xi}^{0},\hat{\xi}^{1}),\hat{\zeta}).

We draw the attention of the reader to the fact that the above conditions are both *necessary and sufficient*. Their sufficiency is justified by Theorem [4.9](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem9 "Theorem 4.9. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). The necessity of (i)-(ii) is shown in Proposition [3.7](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem7 "Proposition 3.7. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). The necessity of (iii) and (iv) is by Corollary [5.1](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem1 "Corollary 5.1. ‣ 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information"). Condition (v) is a consequence of ([5.10](https://arxiv.org/html/2510.15616v1#S5.E10 "In 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) with γ=0\gamma=0 upon noticing that p0=πp\_{0}=\pi. By Corollary [5.1](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem1 "Corollary 5.1. ‣ 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information"), one can see that the process (ξ^ti)(\hat{\xi}^{i}\_{t}) increases only when the inequality in (iii) is an equality. Similarly, the process (ζ^t)(\hat{\zeta}\_{t}) increases only when there is equality in (iv).

We leave the adaptation of Theorem [4.2](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem2 "Theorem 4.2. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") to the reader and rephrase only Theorem [4.8](https://arxiv.org/html/2510.15616v1#S4.Thmtheorem8 "Theorem 4.8. ‣ 4. Sufficient conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

###### Corollary 5.3.

Let U^00,U^01,V^0∈ℝ\hat{U}^{0}\_{0},\hat{U}^{1}\_{0},\hat{V}\_{0}\in\mathbb{R} and ξ^0,ξ^1,ζ^∈𝒜0∘​(𝔽2)\hat{\xi}^{0},\hat{\xi}^{1},\hat{\zeta}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}). Assume that

1. (i)

   for any i=0,1i=0,1 and any τi∈𝒯​(𝔽2)\tau\_{i}\in\mathcal{T}(\mathbb{F}^{2}), we have

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (5.15) |  | 𝖤​[fτii​(1−ζ^τi)+∫[0,τi)gsi​dζ^s+hτii​Δ​ζ^τi]≥U^0i,\mathsf{E}\Big[f^{i}\_{\tau\_{i}}(1-\hat{\zeta}\_{\tau\_{i}})+\int\_{[0,{\tau\_{i}})}g^{i}\_{s}\mathrm{d}\hat{\zeta}\_{s}+h^{i}\_{\tau\_{i}}\Delta\hat{\zeta}\_{\tau\_{i}}\Big]\geq\hat{U}^{i}\_{0}, |  |
2. (ii)

   for any σ∈𝒯​(𝔽2)\sigma\in\mathcal{T}(\mathbb{F}^{2}), we have

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (5.16) |  | 𝖤​[∫[0,σ)⟨π,fs​d​ξ^s⟩+⟨π,gσ​(1−ξ^σ)+hσ​Δ​ξ^σ⟩]≤V^0,\mathsf{E}\Big[\int\_{[0,\sigma)}\langle\pi,f\_{s}\mathrm{d}\hat{\xi}\_{s}\rangle+\langle\pi,g\_{\sigma}(1-\hat{\xi}\_{\sigma})+h\_{\sigma}\Delta\hat{\xi}\_{\sigma}\rangle\Big]\leq\hat{V}\_{0}, |  |
3. (iii)

   ⟨π,U^0⟩=V^0\langle\pi,\hat{U}\_{0}\rangle=\hat{V}\_{0}.

Then the value of the game is V^0\hat{V}\_{0} and a saddle point is given by ((ξ^0,ξ^1),ζ^)((\hat{\xi}^{0},\hat{\xi}^{1}),\hat{\zeta}).

###### Remark 5.4.

It is not difficult to generalise this discussion to the case of two random variables 𝒥\mathcal{J}, 𝒦\mathcal{K}, taking values in two finite sets JJ, KK, and to payoff processes fj,k,gj,k,hj,kf^{j,k},g^{j,k},h^{j,k}, (j,k)∈J×K(j,k)\in J\times K. We could assume that all processes are adapted to a filtration 𝕄=(ℳt)t∈[0,T]\mathbb{M}=(\mathcal{M}\_{t})\_{t\in[0,T]}, that Player 1 has access to the filtration ℱt1=ℳt∨σ​(𝒥)\mathcal{F}^{1}\_{t}=\mathcal{M}\_{t}\vee\sigma(\mathcal{J}) and Player 2 has access to the filtration ℱt2=ℳt∨σ​(𝒦)\mathcal{F}^{2}\_{t}=\mathcal{M}\_{t}\vee\sigma(\mathcal{K}). All the considerations made above would continue to hold, up to using a heavier notation.

### 5.2. Partially observed dynamics

Let (Ω,ℱ,𝖯)(\Omega,\mathcal{F},\mathsf{P}) be a probability space supporting a Brownian motion (Wt)t∈[0,T](W\_{t})\_{t\in[0,T]}, players’ randomisation devices and an independent random variable 𝒥∈{0,1}\mathcal{J}\in\{0,1\} with π=𝖯​(𝒥=1)\pi=\mathsf{P}(\mathcal{J}=1). The probability space is assumed to have a product structure that allows us to apply results of Appendix [D](https://arxiv.org/html/2510.15616v1#A4 "Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information"), see also Subsection [5.1](https://arxiv.org/html/2510.15616v1#S5.SS1 "5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") for a similar construction. Denote by 𝔽W≔(ℱtW)t∈[0,T]\mathbb{F}^{W}\coloneqq(\mathcal{F}^{W}\_{t})\_{t\in[0,T]} the filtration generated by (Wt)t∈[0,T](W\_{t})\_{t\in[0,T]} augmented with 𝖯\mathsf{P}-null sets. Set ℱt=σ​(𝒥)∨ℱtW\mathcal{F}\_{t}=\sigma(\mathcal{J})\vee\mathcal{F}^{W}\_{t}, so 𝔽\mathbb{F} also satisfies the usual conditions. Let μ0,μ1\mu\_{0},\mu\_{1} and σ\sigma be sufficiently regular functions so that (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} is the unique 𝔽\mathbb{F}-adapted solution of the SDE on ℝ\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | Xt=x+∫0tμ𝒥​(Xs)​ds+∫0tσ​(Xs)​dWs,t∈[0,T].X\_{t}=x+\int\_{0}^{t}\mu\_{\mathcal{J}}(X\_{s})\mathrm{d}s+\int\_{0}^{t}\sigma(X\_{s})\mathrm{d}W\_{s},\quad t\in[0,T]. |  |

The existence of a strong solution means that there is a measurable map Γ:[0,T]×C​([0,T])×{0,1}→ℝ\Gamma:[0,T]\times C([0,T])\times\{0,1\}\to\mathbb{R} such that

|  |  |  |  |
| --- | --- | --- | --- |
| (5.17) |  | Xt​(ω)=Γ​(t,W⋅∧t​(ω),𝒥​(ω)),for (t,ω)∈[0,T]×Ω,\displaystyle X\_{t}(\omega)=\Gamma(t,W\_{\cdot\wedge t}(\omega),\mathcal{J}(\omega)),\quad\text{for $(t,\omega)\in[0,T]\times\Omega$,} |  |

see, e.g., [[IW81](https://arxiv.org/html/2510.15616v1#bib.bibx27), Ch. IV, Thm. 3.2].

Sometimes we denote X=X𝒥X=X^{\mathcal{J}} in order to emphasise the role played by 𝒥\mathcal{J} in determining the dynamics of XX. In particular, for j=0,1j=0,1, on {𝒥=j}\{\mathcal{J}=j\} we have X=XjX=X^{j}, where XjX^{j} is the solution of the SDE above with μ𝒥\mu\_{\mathcal{J}} replaced by μj\mu\_{j}. Then,

|  |  |  |  |
| --- | --- | --- | --- |
| (5.18) |  | Xtj​(ω)=Γ​(t,W⋅∧t​(ω),j)≕Γj​(t,W⋅∧t​(ω)),for (t,ω)∈[0,T]×Ω.\displaystyle X^{j}\_{t}(\omega)=\Gamma(t,W\_{\cdot\wedge t}(\omega),j)\eqqcolon\Gamma^{j}(t,W\_{\cdot\wedge t}(\omega)),\quad\text{for $(t,\omega)\in[0,T]\times\Omega$.} |  |

We assume that the 𝖯\mathsf{P}-augmentation of the filtration 𝔽Xj\mathbb{F}^{X^{j}} generated by (Xtj)t∈[0,T](X^{j}\_{t})\_{t\in[0,T]} equals 𝔽W\mathbb{F}^{W} – this is guaranteed when σ\sigma is locally uniformly non-degenerate.

In this framework, Player 2, dubbed the *uninformed player*, only observes the process (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]}, which translates formally into the filtration ℱt2=σ​(Xs,s≤t)\mathcal{F}^{2}\_{t}=\sigma(X\_{s},s\leq t) (also augmented with 𝖯\mathsf{P}-null sets). Player 1, called the *informed player*, additionally observes 𝒥\mathcal{J}, i.e., has access to the filtration ℱt1=ℱt2∨σ​(𝒥)=ℱt\mathcal{F}^{1}\_{t}=\mathcal{F}^{2}\_{t}\vee\sigma(\mathcal{J})=\mathcal{F}\_{t}, where the last equality follows from the assumption that the filtration generated by each (Xtj)t∈[0,T](X^{j}\_{t})\_{t\in[0,T]} equals 𝔽W\mathbb{F}^{W}.

Any admissible strategy ξ∈𝒜0∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1}) for the informed player decomposes as (cf. Lemma [D.4](https://arxiv.org/html/2510.15616v1#A4.Thmtheorem4 "Lemma D.4. ‣ Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information")) ξt=ξt0​𝟏{𝒥=0}+ξt1​𝟏{𝒥=1}\xi\_{t}=\xi^{0}\_{t}\mathbf{1}\_{\{\mathcal{J}=0\}}+\xi^{1}\_{t}\mathbf{1}\_{\{\mathcal{J}=1\}}, with ξj∈𝒜0∘​(𝔽W)\xi^{j}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{W}) for j=0,1j=0,1. Similarly, a stopping time θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}) decomposes as θ=θ0​𝟏{𝒥=0}+θ1​𝟏{𝒥=1}\theta=\theta\_{0}\mathbf{1}\_{\{\mathcal{J}=0\}}+\theta\_{1}\mathbf{1}\_{\{\mathcal{J}=1\}} with θ0,θ1∈𝒯0​(𝔽W)\theta\_{0},\theta\_{1}\in\mathcal{T}\_{0}(\mathbb{F}^{W}). By the right continuity of (ξtj)t∈[0,T](\xi^{j}\_{t})\_{t\in[0,T]} there is a measurable map Ξj:[0,T]×C​([0,T])→ℝ\Xi^{j}:[0,T]\times C([0,T])\to\mathbb{R} such that ξtj​(ω)=Ξj​(t,W⋅∧t​(ω))\xi^{j}\_{t}(\omega)=\Xi^{j}(t,W\_{\cdot\wedge t}(\omega)) for (t,ω)∈[0,T]×Ω(t,\omega)\in[0,T]\times\Omega. Due to the equality 𝔽W=𝔽Xj\mathbb{F}^{W}=\mathbb{F}^{X^{j}}, there is a measurable map Ξ~j:[0,T]×C​([0,T])→ℝ\tilde{\Xi}^{j}:[0,T]\times C([0,T])\to\mathbb{R} such that ξtj​(ω)=Ξ~j​(t,X⋅∧tj​(ω))\xi^{j}\_{t}(\omega)=\tilde{\Xi}^{j}(t,X^{j}\_{\cdot\wedge t}(\omega)). We further have

|  |  |  |  |
| --- | --- | --- | --- |
| (5.19) |  | 𝟏{𝒥=j}​ξtj=𝟏{𝒥=j}​Ξ~j​(t,X⋅∧tj)=𝟏{𝒥=j}​Ξ~j​(t,X⋅∧t)=𝟏{𝒥=j}​ξ~tj,\mathbf{1}\_{\{\mathcal{J}=j\}}\xi^{j}\_{t}=\mathbf{1}\_{\{\mathcal{J}=j\}}\tilde{\Xi}^{j}(t,X^{j}\_{\cdot\wedge t})=\mathbf{1}\_{\{\mathcal{J}=j\}}\tilde{\Xi}^{j}(t,X\_{\cdot\wedge t})=\mathbf{1}\_{\{\mathcal{J}=j\}}\tilde{\xi}^{j}\_{t}, |  |

where ξ~tj≔Ξ~j​(t,X⋅∧t)\tilde{\xi}^{j}\_{t}\coloneqq\tilde{\Xi}^{j}(t,X\_{\cdot\wedge t}), so (ξ~tj)t∈[0,T](\tilde{\xi}^{j}\_{t})\_{t\in[0,T]} can be computed based on the observation of the process (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]}. In other words, ξ~j∈𝒜0∘​(𝔽2)\tilde{\xi}^{j}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}),
which will prove useful in the derivation of Π∗,2\Pi^{\*,2} and the value V∗,2V^{\*,2} of Player 2. The processes ξ~j\tilde{\xi}^{j}, j=0,1j=0,1, can be interpreted as the result of the uninformed player’s calculation, while observing the process XX under the conviction that 𝒥=j\mathcal{J}=j. Similarly, for j=0,1j=0,1 we can introduce θ~j∈𝒯0​(𝔽2)\tilde{\theta}\_{j}\in\mathcal{T}\_{0}(\mathbb{F}^{2}) such that 𝟏{𝒥=j}​θj=𝟏{𝒥=j}​θ~j\mathbf{1}\_{\{\mathcal{J}=j\}}\theta\_{j}=\mathbf{1}\_{\{\mathcal{J}=j\}}\tilde{\theta}\_{j}. The construction of θ~j\tilde{\theta}\_{j} is similar to the construction of ξ~j\tilde{\xi}^{j} by considering the process t↦𝟏{θj≤t}∈𝒜0∘​(𝔽W)t\mapsto\mathbf{1}\_{\{\theta\_{j}\leq t\}}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{W}).

To derive a useful relationship between ξj\xi^{j} and ξ~j\tilde{\xi}^{j}, we define probability measures 𝖯0\mathsf{P}^{0} and 𝖯1\mathsf{P}^{1} by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.20) |  | d​𝖯0d​𝖯=11−π​𝟏{𝒥=0}andd​𝖯1d​𝖯=1π​𝟏{𝒥=1},\displaystyle\frac{\mathrm{d}\mathsf{P}^{0}}{\mathrm{d}\mathsf{P}}=\frac{1}{1-\pi}\mathbf{1}\_{\{\mathcal{J}=0\}}\quad\text{and}\quad\frac{\mathrm{d}\mathsf{P}^{1}}{\mathrm{d}\mathsf{P}}=\frac{1}{\pi}\mathbf{1}\_{\{\mathcal{J}=1\}}, |  |

and recall the following formulae for the conditional expectation under the change of measure: for a 𝖯\mathsf{P}-integrable random variable YY

|  |  |  |  |
| --- | --- | --- | --- |
| (5.21) |  | 𝖤0​[Y|ℱγ2]=(1−π)−1​𝖤​[𝟏{𝒥=0}​Y|ℱγ2](1−π)−1​𝖤​[𝟏{𝒥=0}|ℱγ2]=11−ψγ​𝖤​[Y​𝟏{𝒥=0}|ℱγ2],𝖤1​[Y|ℱγ2]=π−1​𝖤​[𝟏{𝒥=1}​Y|ℱγ2]π−1​𝖤​[𝟏{𝒥=0}|ℱγ2]=1ψγ​𝖤​[Y​𝟏{𝒥=1}|ℱγ2],\displaystyle\begin{aligned} \mathsf{E}^{0}[Y|\mathcal{F}^{2}\_{\gamma}]&=\frac{(1-\pi)^{-1}\mathsf{E}[\mathbf{1}\_{\{\mathcal{J}=0\}}Y|\mathcal{F}^{2}\_{\gamma}]}{(1-\pi)^{-1}\mathsf{E}[\mathbf{1}\_{\{\mathcal{J}=0\}}|\mathcal{F}^{2}\_{\gamma}]}=\frac{1}{1-\psi\_{\gamma}}\mathsf{E}\big[Y\mathbf{1}\_{\{\mathcal{J}=0\}}\big|\mathcal{F}^{2}\_{\gamma}\big],\\ \mathsf{E}^{1}[Y|\mathcal{F}^{2}\_{\gamma}]&=\frac{\pi^{-1}\mathsf{E}[\mathbf{1}\_{\{\mathcal{J}=1\}}Y|\mathcal{F}^{2}\_{\gamma}]}{\pi^{-1}\mathsf{E}[\mathbf{1}\_{\{\mathcal{J}=0\}}|\mathcal{F}^{2}\_{\gamma}]}=\frac{1}{\psi\_{\gamma}}\mathsf{E}\big[Y\mathbf{1}\_{\{\mathcal{J}=1\}}\big|\mathcal{F}^{2}\_{\gamma}\big],\end{aligned} |  |

where ψt≔𝖯​(𝒥=1|ℱt2)=𝖤​[𝒥|ℱt2]\psi\_{t}\coloneqq\mathsf{P}(\mathcal{J}=1|\mathcal{F}^{2}\_{t})=\mathsf{E}[\mathcal{J}|\mathcal{F}^{2}\_{t}] is the co-called posterior process, i.e., Player 2’s best estimate of the value of 𝒥\mathcal{J} based upon the observation of the process XX. This allows us to obtain the following identities:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (5.22) |  | ψt​ξ~t1\displaystyle\psi\_{t}\tilde{\xi}^{1}\_{t} | =𝖤​[𝟏{𝒥=1}​ξ~t1|ℱt2]=𝖤​[𝟏{𝒥=1}​ξt1|ℱt2]=ψt​𝖤1​[ξt1|ℱt2],\displaystyle=\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=1\}}\tilde{\xi}^{1}\_{t}\big|\mathcal{F}^{2}\_{t}\big]=\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=1\}}\xi^{1}\_{t}\big|\mathcal{F}^{2}\_{t}\big]=\psi\_{t}\mathsf{E}^{1}\big[\xi^{1}\_{t}\big|\mathcal{F}^{2}\_{t}\big], |  |
|  | (1−ψt)​ξ~t0\displaystyle(1-\psi\_{t})\tilde{\xi}^{0}\_{t} | =𝖤​[𝟏{𝒥=0}​ξ~t0|ℱt2]=𝖤​[𝟏{𝒥=0}​ξt0|ℱt2]=(1−ψt)​𝖤0​[ξt0|ℱt2].\displaystyle=\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=0\}}\tilde{\xi}^{0}\_{t}\big|\mathcal{F}^{2}\_{t}\big]=\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=0\}}\xi^{0}\_{t}\big|\mathcal{F}^{2}\_{t}\big]=(1-\psi\_{t})\mathsf{E}^{0}\big[\xi^{0}\_{t}\big|\mathcal{F}^{2}\_{t}\big]. |  |

Hence we have the relationship

|  |  |  |  |
| --- | --- | --- | --- |
| (5.23) |  | ξ~tj=𝖤j​[ξtj|ℱt2]for j=0,1.\tilde{\xi}^{j}\_{t}=\mathsf{E}^{j}\big[\xi^{j}\_{t}\big|\mathcal{F}^{2}\_{t}\big]\quad\text{for $j=0,1$.} |  |

Before specifying the payoff functions, we make some considerations about the structure of the belief process for the uninformed player.
Much of the analysis in this section repeats steps from the study in Section [5.1](https://arxiv.org/html/2510.15616v1#S5.SS1 "5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") and we therefore omit some details.

Belief process. In this framework direct observation of the process XX is informative about the nature of the true drift and the belief process for the uninformed player takes a different form compared to the previous example (where each player could only learn from the actions of her opponent – or rather the lack thereof). Given an optimal pair (ξ∗,ζ∗)∈𝒜0∘​(𝔽1)×𝒜0∘​(𝔽2)(\xi^{\*},\zeta^{\*})\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1})\times\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}) and using 𝟏{𝒥=j}​ξtj=𝟏{𝒥=j}​ξ~tj\mathbf{1}\_{\{\mathcal{J}=j\}}\xi^{j}\_{t}=\mathbf{1}\_{\{\mathcal{J}=j\}}\tilde{\xi}^{j}\_{t} with ([5.23](https://arxiv.org/html/2510.15616v1#S5.E23 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")), the processes defined in ([2.6](https://arxiv.org/html/2510.15616v1#S2.E6 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) read (recall the convention 0/0=10/0=1)

|  |  |  |
| --- | --- | --- |
|  | Πθ∗,1=1,θ∈𝒯0​(𝔽1),Πγ∗,2=(1−ξ~γ−∗,0)ψγ​(1−ξ~γ−∗,1)+(1−ψγ)​(1−ξ~γ−∗,0)​𝟏{𝒥=0}+(1−ξ~γ−∗,1)ψγ​(1−ξ~γ−∗,1)+(1−ψγ)​(1−ξ~γ−∗,0)​𝟏{𝒥=1}γ∈𝒯0​(𝔽2).\displaystyle\begin{aligned} &\Pi^{\*,1}\_{\theta}=1,\quad\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}),\\ &\Pi^{\*,2}\_{\gamma}=\frac{(1-\tilde{\xi}^{\*,0}\_{\gamma-})}{\psi\_{\gamma}(1-\tilde{\xi}^{\*,1}\_{\gamma-})+(1-\psi\_{\gamma})(1-\tilde{\xi}^{\*,0}\_{\gamma-})}\mathbf{1}\_{\{\mathcal{J}=0\}}\\ &\qquad\quad+\frac{(1-\tilde{\xi}^{\*,1}\_{\gamma-})}{\psi\_{\gamma}(1-\tilde{\xi}^{\*,1}\_{\gamma-})+(1-\psi\_{\gamma})(1-\tilde{\xi}^{\*,0}\_{\gamma-})}\mathbf{1}\_{\{\mathcal{J}=1\}}\quad\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}).\end{aligned} |  |

The dynamics of the process (ψt)t∈[0,T](\psi\_{t})\_{t\in[0,T]} can be computed explicitly and the two dimensional process (Xt,ψt)t∈[0,T](X\_{t},\psi\_{t})\_{t\in[0,T]} is ruled, under the measure 𝖯\mathsf{P}, by the SDE, for t∈[0,T]t\in[0,T]

|  |  |  |  |
| --- | --- | --- | --- |
| (5.24) |  | Xt=x+∫0t(μ0​(Xs)​(1−ψs)+μ1​(Xs)​ψs)​ds+∫0tσ​(Xs)​dBs,ψt=ψ0+∫0tw​(ψs)​ψs​(1−ψs)​dBs,\displaystyle\begin{aligned} X\_{t}&=x+\int\_{0}^{t}\big(\mu\_{0}(X\_{s})(1-\psi\_{s})+\mu\_{1}(X\_{s})\psi\_{s}\big)\mathrm{d}s+\int\_{0}^{t}\sigma(X\_{s})\mathrm{d}B\_{s},\\ \psi\_{t}&=\psi\_{0}+\int\_{0}^{t}w(\psi\_{s})\psi\_{s}(1-\psi\_{s})\mathrm{d}B\_{s},\end{aligned} |  |

where w​(z)=(μ1​(z)−μ0​(z))/σ​(z)w(z)=(\mu\_{1}(z)-\mu\_{0}(z))/\sigma(z) is the signal-to-noise ratio and (Bt)t∈[0,T](B\_{t})\_{t\in[0,T]} is a (𝔽2,𝖯)(\mathbb{F}^{2},\mathsf{P})-Brownian motion (the so-called innovation process) defined as:

|  |  |  |
| --- | --- | --- |
|  | Bt≔∫0td​Xsσ​(Xs)−∫0tμ0​(Xs)+(μ1​(Xs)−μ0​(Xs))​ψsσ​(Xs)​ds.B\_{t}\coloneqq\int\_{0}^{t}\frac{\mathrm{d}X\_{s}}{\sigma(X\_{s})}-\int\_{0}^{t}\frac{\mu\_{0}(X\_{s})+(\mu\_{1}(X\_{s})-\mu\_{0}(X\_{s}))\psi\_{s}}{\sigma(X\_{s})}\mathrm{d}s. |  |

In line with the previous section we now introduce a belief process, which features both the learning from observation of XX (via the process ψ\psi) and learning from the actions of the informed player. That is, setting

|  |  |  |  |
| --- | --- | --- | --- |
| (5.25) |  | pγ=ψγ​(1−ξ~γ−∗,1)ψγ​(1−ξ~γ−∗,1)+(1−ψγ)​(1−ξ~γ−∗,0),γ∈𝒯0​(𝔽2),\displaystyle p\_{\gamma}=\frac{\psi\_{\gamma}(1-\tilde{\xi}^{\*,1}\_{\gamma-})}{\psi\_{\gamma}(1-\tilde{\xi}^{\*,1}\_{\gamma-})+(1-\psi\_{\gamma})(1-\tilde{\xi}^{\*,0}\_{\gamma-})},\quad\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}), |  |

we express Πγ∗,2\Pi^{\*,2}\_{\gamma} on {ξ~γ−∗,0∧ξ~γ−∗,1<1}\{\tilde{\xi}^{\*,0}\_{\gamma-}\wedge\tilde{\xi}^{\*,1}\_{\gamma-}<1\} as

|  |  |  |
| --- | --- | --- |
|  | Πγ∗,2=1−pγ1−ψγ​𝟏{𝒥=0}+pγψγ​𝟏{𝒥=1},γ∈𝒯0​(𝔽2).\Pi^{\*,2}\_{\gamma}=\frac{1-p\_{\gamma}}{1-\psi\_{\gamma}}\mathbf{1}\_{\{\mathcal{J}=0\}}+\frac{p\_{\gamma}}{\psi\_{\gamma}}\mathbf{1}\_{\{\mathcal{J}=1\}},\quad\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}). |  |

Notice that p0=ψ0=𝖯​(𝒥=1)=πp\_{0}=\psi\_{0}=\mathsf{P}(\mathcal{J}=1)=\pi and we have a clear interpretation of the belief process (pt)t∈[0,T](p\_{t})\_{t\in[0,T]} as the simple calculations below demonstrate: letting Z∼U​([0,1])Z\sim U([0,1]) be Player 1’s randomisation device, we have on the event {ξ~γ−∗,0∧ξ~γ−∗,1<1}\{\tilde{\xi}^{\*,0}\_{\gamma-}\wedge\tilde{\xi}^{\*,1}\_{\gamma-}<1\}

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖯​(𝒥=1,τ∗≥γ|ℱγ2)𝖯​(τ∗≥γ|ℱγ2)\displaystyle\frac{\mathsf{P}\big(\mathcal{J}=1,\tau\_{\*}\geq\gamma\big|\mathcal{F}^{2}\_{\gamma}\big)}{\mathsf{P}\big(\tau\_{\*}\geq\gamma\big|\mathcal{F}^{2}\_{\gamma}\big)} | =𝖯​(𝒥=1,ξγ−∗,1≤Z|ℱγ2)𝖯​(𝒥=1,ξγ−∗,1≤Z|ℱγ2)+𝖯​(𝒥=0,ξγ−∗,0≤Z|ℱγ2)\displaystyle=\frac{\mathsf{P}\big(\mathcal{J}=1,\xi^{\*,1}\_{\gamma-}\leq Z\big|\mathcal{F}^{2}\_{\gamma}\big)}{\mathsf{P}\big(\mathcal{J}=1,\xi^{\*,1}\_{\gamma-}\leq Z\big|\mathcal{F}^{2}\_{\gamma}\big)+\mathsf{P}\big(\mathcal{J}=0,\xi^{\*,0}\_{\gamma-}\leq Z\big|\mathcal{F}^{2}\_{\gamma}\big)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖤​[𝟏{𝒥=1}​(1−ξγ−∗,1)|ℱγ2]𝖤​[𝟏{𝒥=1}​(1−ξγ−∗,1)|ℱγ2]+𝖤​[𝟏{𝒥=0}​(1−ξγ−∗,0)|ℱγ2]=pγ,\displaystyle=\frac{\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=1\}}(1-\xi^{\*,1}\_{\gamma-})\big|\mathcal{F}^{2}\_{\gamma}\big]}{\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=1\}}(1-\xi^{\*,1}\_{\gamma-})\big|\mathcal{F}^{2}\_{\gamma}\big]+\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=0\}}(1-\xi^{\*,0}\_{\gamma-})\big|\mathcal{F}^{2}\_{\gamma}\big]}=p\_{\gamma}, |  |

where the second equality holds because ZZ is independent of ℱγ2\mathcal{F}^{2}\_{\gamma} and the final one holds because of ([5.23](https://arxiv.org/html/2510.15616v1#S5.E23 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")). The above shows that the process (pt)t∈[0,T](p\_{t})\_{t\in[0,T]} is Player 2’s posterior probability of 𝒥=1\mathcal{J}=1 based on the observation of (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} and on the fact that the game has not ended prior to time t∈[0,T]t\in[0,T].

Equilibrium value processes. We assume that the payoff processes (ft,gt,ht)t∈[0,T](f\_{t},g\_{t},h\_{t})\_{t\in[0,T]} are defined as functions of the underlying process XX. More precisely, given measurable functions f,g,h:[0,T]×ℝd→ℝf,g,h:[0,T]\times\mathbb{R}^{d}\to\mathbb{R}, with f≥h≥gf\geq h\geq g, we set ft≔f​(t,Xt)f\_{t}\coloneqq f(t,X\_{t}), gt≔g​(t,Xt)g\_{t}\coloneqq g(t,X\_{t}) and ht≔h​(t,Xt)h\_{t}\coloneqq h(t,X\_{t}). Clearly the triplet (ft,gt,ht)t∈[0,T](f\_{t},g\_{t},h\_{t})\_{t\in[0,T]} is 𝔽2\mathbb{F}^{2}-adapted and we assume each process to be in ℒb​(𝖯)\mathcal{L}\_{b}(\mathsf{P}).

Recalling the notation X=X𝒥X=X^{\mathcal{J}} along with the fact that on the event {𝒥=j}\{\mathcal{J}=j\} the process X=XjX=X^{j} follows the dynamics d​Xtj=μj​(Xtj)​d​t+σ​(Xtj)​d​Wt\mathrm{d}X^{j}\_{t}=\mu\_{j}(X^{j}\_{t})\mathrm{d}t+\sigma(X^{j}\_{t})\mathrm{d}W\_{t}, we can formally cast the current problem in a similar (but not identical) fashion as the problem in Section [5.1](https://arxiv.org/html/2510.15616v1#S5.SS1 "5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information"). That is, we set ftj≔f​(t,Xtj)f^{j}\_{t}\coloneqq f(t,X^{j}\_{t}), gtj≔g​(t,Xtj)g^{j}\_{t}\coloneqq g(t,X^{j}\_{t}) and htj≔h​(t,Xtj)h^{j}\_{t}\coloneqq h(t,X^{j}\_{t}). It follows from ([5.18](https://arxiv.org/html/2510.15616v1#S5.E18 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) that XjX^{j} is independent of 𝒥\mathcal{J}, so the same holds for fj,gj,hjf^{j},g^{j},h^{j}. We must also notice that for ζ∗∈𝒜0∘​(𝔽2)\zeta^{\*}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}) there is a measurable map Λ:[0,T]×C​([0,T])→ℝ\Lambda:[0,T]\times C([0,T])\to\mathbb{R} such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (5.26) |  | ζt∗​(ω)\displaystyle\zeta^{\*}\_{t}(\omega) | =Λ​(t,X⋅∧t​(ω))=∑j=01𝟏{𝒥=j}​(ω)​Λ​(t,X⋅∧tj​(ω))\displaystyle=\Lambda(t,X\_{\cdot\wedge t}(\omega))=\sum\_{j=0}^{1}\mathbf{1}\_{\{\mathcal{J}=j\}}(\omega)\Lambda(t,X^{j}\_{\cdot\wedge t}(\omega)) |  |
|  |  | =∑j=01𝟏{𝒥=j}​(ω)​Λ​(t,Γj​(t,W⋅∧t​(ω)))≕∑j=01𝟏{𝒥=j}​(ω)​ζt∗,j​(ω),\displaystyle=\sum\_{j=0}^{1}\mathbf{1}\_{\{\mathcal{J}=j\}}(\omega)\Lambda\big(t,\Gamma^{j}(t,W\_{\cdot\wedge t}(\omega))\big)\eqqcolon\sum\_{j=0}^{1}\mathbf{1}\_{\{\mathcal{J}=j\}}(\omega)\zeta^{\*,j}\_{t}(\omega), |  |

where clearly ζ∗,0\zeta^{\*,0} and ζ∗,1\zeta^{\*,1} are 𝔽W\mathbb{F}^{W}-adapted and independent of 𝒥\mathcal{J}.

###### Remark 5.5.

Notice that the decomposition in ([5.26](https://arxiv.org/html/2510.15616v1#S5.E26 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) should not be interpreted as saying that the uninformed player selects ζ∗,0\zeta^{\*,0} or ζ∗,1\zeta^{\*,1} depending on whether 𝒥=0\mathcal{J}=0 or 𝒥=1\mathcal{J}=1. The uninformed player chooses ζ∗\zeta^{\*} (i.e., the map Λ​(⋅,⋅)\Lambda(\cdot,\cdot)) but the informed player “knows” the value of 𝒥\mathcal{J}. Therefore, the informed player knows the law of the realised strategy (ζt∗,j)t∈[0,T](\zeta^{\*,j}\_{t})\_{t\in[0,T]}, whereas the uninformed player can only estimate it as a mixture of the laws of ζ∗,0\zeta^{\*,0} and ζ∗,1\zeta^{\*,1}.

Recalling the decompositions ξt=ξt0​𝟏{𝒥=0}+ξt1​𝟏{𝒥=1}\xi\_{t}=\xi^{0}\_{t}\mathbf{1}\_{\{\mathcal{J}=0\}}+\xi^{1}\_{t}\mathbf{1}\_{\{\mathcal{J}=1\}}, θt=θ0​𝟏{𝒥=0}+θ1​𝟏{𝒥=1}\theta\_{t}=\theta\_{0}\mathbf{1}\_{\{\mathcal{J}=0\}}+\theta\_{1}\mathbf{1}\_{\{\mathcal{J}=1\}} and that 𝔽1=𝔽\mathbb{F}^{1}=\mathbb{F}, we have on {ζθ0−∗,0∧ζθ1−∗,1<1}\{\zeta^{\*,0}\_{\theta\_{0}-}\wedge\zeta^{\*,1}\_{\theta\_{1}-}<1\}

|  |  |  |  |
| --- | --- | --- | --- |
|  | V∗,1​(θ)\displaystyle V^{\*,1}(\theta) | =ess​infξ∈𝒜θ∘​(𝔽)⁡𝖤​[∫[θ,T)ft𝒥​(1−ζt∗;θ)​dξt+∫[θ,T)gt𝒥​(1−ξt)​dζt∗;θ+∑t∈[θ,T]ht𝒥​Δ​ζt∗;θ​Δ​ξt|ℱθ]\displaystyle=\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F})}\mathsf{E}\Big[\int\_{[\theta,T)}f^{\mathcal{J}}\_{t}(1-\zeta^{\*;\theta}\_{t})\mathrm{d}\xi\_{t}+\int\_{[\theta,T)}g^{\mathcal{J}}\_{t}(1-\xi\_{t})\mathrm{d}\zeta^{\*;\theta}\_{t}+\sum\_{t\in[\theta,T]}h^{\mathcal{J}}\_{t}\Delta\zeta^{\*;\theta}\_{t}\Delta\xi\_{t}\Big|\mathcal{F}\_{\theta}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ess​infξ∈𝒜θ∘​(𝔽)∑j=01𝟏{𝒥=j}𝖤[∫[θj,T)ftj(1−ζt∗,j;θj)dξtj+∫[θj,T)gtj(1−ξtj)dζt∗,j;θj\displaystyle=\operatorname\*{ess\,inf}\_{\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F})}\sum\_{j=0}^{1}\mathbf{1}\_{\{\mathcal{J}=j\}}\mathsf{E}\Big[\int\_{[\theta\_{j},T)}f^{j}\_{t}(1-\zeta^{\*,j;\theta\_{j}}\_{t})\mathrm{d}\xi^{j}\_{t}+\int\_{[\theta\_{j},T)}g^{j}\_{t}(1-\xi^{j}\_{t})\mathrm{d}\zeta^{\*,j;\theta\_{j}}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑t∈[θj,T]htjΔζt∗,j;θjΔξtj|ℱθ].\displaystyle\hskip 265.0pt+\sum\_{t\in[\theta\_{j},T]}h^{j}\_{t}\Delta\zeta^{\*,j;\theta\_{j}}\_{t}\Delta\xi^{j}\_{t}\Big|\mathcal{F}\_{\theta}\Big]. |  |

Since fj,gj,hj,ξj,ζ∗,jf^{j},g^{j},h^{j},\xi^{j},\zeta^{\*,j} are 𝔽W\mathbb{F}^{W}-adapted, θj\theta\_{j} is a 𝔽W\mathbb{F}^{W}-stopping time and 𝒥\mathcal{J} is independent of ℱTW\mathcal{F}^{W}\_{T}, we are allowed to use Lemma [E.4](https://arxiv.org/html/2510.15616v1#A5.Thmtheorem4 "Lemma E.4. ‣ Appendix E Technical results for partially observed scenarios ‣ Martingale theory for Dynkin games with asymmetric information") to obtain the following representation of V∗,1​(θ)V^{\*,1}(\theta) on the event {ζθ0−∗,0∧ζθ1−∗,1<1}\{\zeta^{\*,0}\_{\theta\_{0}-}\wedge\zeta^{\*,1}\_{\theta\_{1}-}<1\}:

|  |  |  |
| --- | --- | --- |
|  | V∗,1​(θ)=𝟏{𝒥=0}​ess​infξ0∈𝒜θ0∘​(𝔽W)⁡L0​(ξ0,ζ∗,0;θ0|ℱθ0W)+𝟏{𝒥=1}​ess​infξ1∈𝒜θ1∘​(𝔽W)⁡L1​(ξ1,ζ∗,1;θ1|ℱθ1W),\displaystyle V^{\*,1}(\theta)=\mathbf{1}\_{\{\mathcal{J}=0\}}\operatorname\*{ess\,inf}\_{\xi^{0}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta\_{0}}(\mathbb{F}^{W})}L^{0}(\xi^{0},\zeta^{\*,0;\theta\_{0}}|\mathcal{F}^{W}\_{\theta\_{0}})+\mathbf{1}\_{\{\mathcal{J}=1\}}\operatorname\*{ess\,inf}\_{\xi^{1}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta\_{1}}(\mathbb{F}^{W})}L^{1}(\xi^{1},\zeta^{\*,1;\theta\_{1}}|\mathcal{F}^{W}\_{\theta\_{1}}), |  |

with the same notation as in ([5.5](https://arxiv.org/html/2510.15616v1#S5.E5 "In 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")).

For the uninformed player calculations are slightly different. For γ∈𝒯0​(𝔽2)\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2}) and ζ∈𝒜γ∘​(𝔽2)\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\gamma}(\mathbb{F}^{2}),

|  |  |  |
| --- | --- | --- |
|  | JΠγ∗,2​(ξ∗;γ,ζ|ℱγ2)\displaystyle J^{\Pi^{\*,2}\_{\gamma}}\big(\xi^{\*;\gamma},\zeta\big|\mathcal{F}^{2}\_{\gamma}\big) |  |
|  |  |  |
| --- | --- | --- |
|  | =𝖤​[Πγ∗,2​(∫[γ,T)ft𝒥​(1−ζt)​dξt∗;γ+∫[γ,T)gt𝒥​(1−ξt∗;γ)​dζt+∑t∈[θ,T]ht𝒥​Δ​ζt​Δ​ξt∗;γ)|ℱγ2]\displaystyle=\mathsf{E}\Big[\Pi^{\*,2}\_{\gamma}\Big(\int\_{[\gamma,T)}f^{\mathcal{J}}\_{t}(1-\zeta\_{t})\mathrm{d}\xi^{\*;\gamma}\_{t}+\int\_{[\gamma,T)}g^{\mathcal{J}}\_{t}(1-\xi^{\*;\gamma}\_{t})\mathrm{d}\zeta\_{t}+\sum\_{t\in[\theta,T]}h^{\mathcal{J}}\_{t}\Delta\zeta\_{t}\Delta\xi^{\*;\gamma}\_{t}\Big)\Big|\mathcal{F}^{2}\_{\gamma}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =(1−pγ)​𝖤0​[∫[γ,T)ft0​(1−ζt)​dξt∗,0;γ+∫[γ,T)gt0​(1−ξt∗,0;γ)​dζt+∑t∈[θ,T]ht0​Δ​ζt​Δ​ξt∗,0;γ|ℱγ2]\displaystyle=(1-p\_{\gamma})\mathsf{E}^{0}\Big[\int\_{[\gamma,T)}f^{0}\_{t}(1-\zeta\_{t})\mathrm{d}\xi^{\*,0;\gamma}\_{t}+\int\_{[\gamma,T)}g^{0}\_{t}(1-\xi^{\*,0;\gamma}\_{t})\mathrm{d}\zeta\_{t}+\sum\_{t\in[\theta,T]}h^{0}\_{t}\Delta\zeta\_{t}\Delta\xi^{\*,0;\gamma}\_{t}\Big|\mathcal{F}^{2}\_{\gamma}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | +pγ​𝖤1​[∫[γ,T)ft1​(1−ζt)​dξt∗,1;γ+∫[γ,T)gt1​(1−ξt∗,1;γ)​dζt+∑t∈[θ,T]ht1​Δ​ζt​Δ​ξt∗,1;γ|ℱγ2]\displaystyle\quad+p\_{\gamma}\mathsf{E}^{1}\Big[\int\_{[\gamma,T)}f^{1}\_{t}(1-\zeta\_{t})\mathrm{d}\xi^{\*,1;\gamma}\_{t}+\int\_{[\gamma,T)}g^{1}\_{t}(1-\xi^{\*,1;\gamma}\_{t})\mathrm{d}\zeta\_{t}+\sum\_{t\in[\theta,T]}h^{1}\_{t}\Delta\zeta\_{t}\Delta\xi^{\*,1;\gamma}\_{t}\Big|\mathcal{F}^{2}\_{\gamma}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≕(1−pγ)​L¯0​(ξ∗,0;γ,ζ|ℱγ2)+pγ​L¯1​(ξ∗,1;γ,ζ|ℱγ2),\displaystyle\eqqcolon(1-p\_{\gamma})\bar{L}^{0}\big(\xi^{\*,0;\gamma},\zeta\big|\mathcal{F}^{2}\_{\gamma}\big)+p\_{\gamma}\bar{L}^{1}\big(\xi^{\*,1;\gamma},\zeta\big|\mathcal{F}^{2}\_{\gamma}\big), |  |

on the event {ξ~γ−∗,0∧ξ~γ−∗,1<1}\{\tilde{\xi}^{\*,0}\_{\gamma-}\wedge\tilde{\xi}^{\*,1}\_{\gamma-}<1\}, where 𝖯0\mathsf{P}^{0} and 𝖯1\mathsf{P}^{1} are probability measures defined in ([5.20](https://arxiv.org/html/2510.15616v1#S5.E20 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) and we used ([5.21](https://arxiv.org/html/2510.15616v1#S5.E21 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")). It is also worth noticing that L¯j​(ξ∗,j;γ,ζ|ℱγ2)=L¯j​(ξ~∗,j;γ,ζ|ℱγ2)\bar{L}^{j}(\xi^{\*,j;\gamma},\zeta|\mathcal{F}^{2}\_{\gamma})=\bar{L}^{j}(\tilde{\xi}^{\*,j;\gamma},\zeta|\mathcal{F}^{2}\_{\gamma}), j=0,1j=0,1, due to the identity ξ∗,j=ξ~∗,j\xi^{\*,j}=\tilde{\xi}^{\*,j} under 𝖯j\mathsf{P}^{j}.

In conclusion, we obtain, for (θ,γ)∈𝒯0​(𝔽1)×𝒯0​(𝔽2)(\theta,\gamma)\in\mathcal{T}\_{0}(\mathbb{F}^{1})\times\mathcal{T}\_{0}(\mathbb{F}^{2}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | V∗,1​(θ)\displaystyle V^{\*,1}(\theta) | =𝟏{𝒥=0}​ess​infξ0∈𝒜θ0∘​(𝔽W)⁡L0​(ξ0,ζ∗,0;θ0|ℱθ0W)+𝟏{𝒥=1}​ess​infξ1∈𝒜θ1∘​(𝔽W)⁡L1​(ξ1,ζ∗,1;θ1|ℱθ1W),\displaystyle=\mathbf{1}\_{\{\mathcal{J}=0\}}\operatorname\*{ess\,inf}\_{\xi^{0}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta\_{0}}(\mathbb{F}^{W})}L^{0}(\xi^{0},\zeta^{\*,0;\theta\_{0}}|\mathcal{F}^{W}\_{\theta\_{0}})+\mathbf{1}\_{\{\mathcal{J}=1\}}\operatorname\*{ess\,inf}\_{\xi^{1}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta\_{1}}(\mathbb{F}^{W})}L^{1}(\xi^{1},\zeta^{\*,1;\theta\_{1}}|\mathcal{F}^{W}\_{\theta\_{1}}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≕𝟏{𝒥=0}​U0​(θ0)+𝟏{𝒥=1}​U1​(θ1),\displaystyle\eqqcolon\mathbf{1}\_{\{\mathcal{J}=0\}}U^{0}(\theta\_{0})+\mathbf{1}\_{\{\mathcal{J}=1\}}U^{1}(\theta\_{1}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | V∗,2​(γ)\displaystyle V^{\*,2}(\gamma) | =ess​supζ∈𝒜γ∘​(𝔽2)⁡((1−pγ)​L¯0​(ξ∗,0;γ,ζ|ℱγ2)+pγ​L¯1​(ξ∗,1;γ,ζ|ℱγ2))≕V​(γ),\displaystyle=\operatorname\*{ess\,sup}\_{\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\gamma}(\mathbb{F}^{2})}\Big((1-p\_{\gamma})\bar{L}^{0}\big(\xi^{\*,0;\gamma},\zeta\big|\mathcal{F}^{2}\_{\gamma}\big)+p\_{\gamma}\bar{L}^{1}\big(\xi^{\*,1;\gamma},\zeta\big|\mathcal{F}^{2}\_{\gamma}\big)\Big)\eqqcolon V(\gamma), |  |

on {ζθ0−∗,0∧ζθ1−∗,1<1}\{\zeta^{\*,0}\_{\theta\_{0}-}\wedge\zeta^{\*,1}\_{\theta\_{1}-}<1\} and {ξ~γ−∗,0∧ξ~γ−∗,1<1}\{\tilde{\xi}^{\*,0}\_{\gamma-}\wedge\tilde{\xi}^{\*,1}\_{\gamma-}<1\}, respectively.

In order to apply Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") in this context, it is convenient to notice that for γ∈𝒯0​(𝔽2)\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2})

|  |  |  |  |
| --- | --- | --- | --- |
| (5.27) |  | 𝖤​[1−ξγ−∗|ℱγ2]=𝖤​[(1−ξγ−∗,0)​𝟏{𝒥=0}+(1−ξγ−∗,1)​𝟏{𝒥=1}|ℱγ2]=(1−ξ~γ−∗,0)​(1−ψγ)+(1−ξ~γ−∗,1)​ψγ,\displaystyle\begin{aligned} \mathsf{E}\big[1-\xi^{\*}\_{\gamma-}\big|\mathcal{F}^{2}\_{\gamma}\big]&=\mathsf{E}\big[(1-\xi^{\*,0}\_{\gamma-})\mathbf{1}\_{\{\mathcal{J}=0\}}+(1-\xi^{\*,1}\_{\gamma-})\mathbf{1}\_{\{\mathcal{J}=1\}}\big|\mathcal{F}^{2}\_{\gamma}\big]\\ &=(1-\tilde{\xi}^{\*,0}\_{\gamma-})(1-\psi\_{\gamma})+(1-\tilde{\xi}^{\*,1}\_{\gamma-})\psi\_{\gamma},\end{aligned} |  |

by the decomposition ξ∗=ξ∗,0​𝟏{𝒥=0}+ξ∗,1​𝟏{𝒥=1}\xi^{\*}=\xi^{\*,0}\mathbf{1}\_{\{\mathcal{J}=0\}}+\xi^{\*,1}\mathbf{1}\_{\{\mathcal{J}=1\}} and the identity ([5.22](https://arxiv.org/html/2510.15616v1#S5.E22 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")). Similarly, using ([5.26](https://arxiv.org/html/2510.15616v1#S5.E26 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) we have for θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1})

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤​[1−ζθ−∗|ℱθ1]\displaystyle\mathsf{E}\big[1-\zeta^{\*}\_{\theta-}\big|\mathcal{F}^{1}\_{\theta}\big] | =(1−ζθ0−∗,0)​𝟏{𝒥=0}+(1−ζθ1−∗,1)​𝟏{𝒥=1}.\displaystyle=(1-\zeta^{\*,0}\_{\theta\_{0}-})\mathbf{1}\_{\{\mathcal{J}=0\}}+(1-\zeta^{\*,1}\_{\theta\_{1}-})\mathbf{1}\_{\{\mathcal{J}=1\}}. |  |

Then, invoking Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") there are 𝔽W\mathbb{F}^{W}-optional processes (Ut0)t∈[0,T](U^{0}\_{t})\_{t\in[0,T]}, (Ut1)t∈[0,T](U^{1}\_{t})\_{t\in[0,T]} and an 𝔽2\mathbb{F}^{2}-optional process (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]} such that for any 𝔽W\mathbb{F}^{W}-stopping time θi\theta\_{i} and any 𝔽2\mathbb{F}^{2}-stopping time γ\gamma

|  |  |  |
| --- | --- | --- |
|  | (1−ζθi−∗,i)​Uθii=(1−ζθi−∗,i)​Ui​(θi)and⟨ψγ,(1−ξ~γ−∗)⟩​Vγ=⟨ψγ,(1−ξ~γ−∗)⟩​V​(γ),\displaystyle(1-\zeta^{\*,i}\_{\theta\_{i}-})U^{i}\_{\theta\_{i}}=(1-\zeta^{\*,i}\_{\theta\_{i}-})U^{i}(\theta\_{i})\quad\text{and}\quad\langle\psi\_{\gamma},(1-\tilde{\xi}^{\*}\_{\gamma-})\rangle V\_{\gamma}=\langle\psi\_{\gamma},(1-\tilde{\xi}^{\*}\_{\gamma-})\rangle V(\gamma), |  |

where we recall that ⟨ψγ,ϕ⟩=ψγ​ϕ1+(1−ψγ)​ϕ0\langle\psi\_{\gamma},\phi\rangle=\psi\_{\gamma}\phi^{1}+(1-\psi\_{\gamma})\phi^{0} for any ϕ∈ℝ2\phi\in\mathbb{R}^{2}.
Moreover, representations as optimal stopping problems similar to those in ([5.8](https://arxiv.org/html/2510.15616v1#S5.E8 "In 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) and ([5.9](https://arxiv.org/html/2510.15616v1#S5.E9 "In 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) continue to hold: that is

|  |  |  |  |
| --- | --- | --- | --- |
| (5.28) |  | Uθjj=ess​infτ∈𝒯θj​(𝔽W)⁡Lj​(τ,ζ∗,j;θj|ℱθjW),on {ζθj−∗,j<1},Vγ=ess​supσ∈𝒯γ​(𝔽2)⁡(pγ​L¯1​(ξ∗,1;γ,σ|ℱγ2)+(1−pγ)​L¯0​(ξ∗,0;γ,σ|ℱγ2)),on {ξ~γ−∗,0∧ξ~γ−∗,1<1},\displaystyle\begin{aligned} U^{j}\_{\theta\_{j}}&=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\theta\_{j}}(\mathbb{F}^{W})}L^{j}\big(\tau,\zeta^{\*,j;\theta\_{j}}\big|\mathcal{F}^{W}\_{\theta\_{j}}\big),\quad\text{on $\{\zeta^{\*,j}\_{\theta\_{j}-}<1\}$,}\\ V\_{\gamma}&=\operatorname\*{ess\,sup}\_{\sigma\in\mathcal{T}\_{\gamma}(\mathbb{F}^{2})}\Big(p\_{\gamma}\bar{L}^{1}\big(\xi^{\*,1;\gamma},\sigma\big|\mathcal{F}^{2}\_{\gamma}\big)+(1-p\_{\gamma})\bar{L}^{0}\big(\xi^{\*,0;\gamma},\sigma\big|\mathcal{F}^{2}\_{\gamma}\big)\Big),\quad\text{on $\{\tilde{\xi}^{\*,0}\_{\gamma-}\wedge\tilde{\xi}^{\*,1}\_{\gamma-}<1\}$},\end{aligned} |  |

where Lj​(τ,ζ∗,j;θj|ℱθjW)L^{j}\big(\tau,\zeta^{\*,j;\theta\_{j}}\big|\mathcal{F}^{W}\_{\theta\_{j}}\big) stands for Lj​(ξ,ζ∗,j;θj|ℱθjW)L^{j}\big(\xi,\zeta^{\*,j;\theta\_{j}}\big|\mathcal{F}^{W}\_{\theta\_{j}}\big) with ξt=𝟏{t≥τ}\xi\_{t}=\mathbf{1}\_{\{t\geq\tau\}} and L¯j​(ξ∗,j;γ,σ|ℱγ2)\bar{L}^{j}\big(\xi^{\*,j;\gamma},\sigma\big|\mathcal{F}^{2}\_{\gamma}\big) stands for L¯j​(ξ∗,j;γ,ζ|ℱγ2)\bar{L}^{j}\big(\xi^{\*,j;\gamma},\zeta\big|\mathcal{F}^{2}\_{\gamma}\big) with ζt=𝟏{t≥σ}\zeta\_{t}=\mathbf{1}\_{\{t\geq\sigma\}}.

Define

|  |  |  |  |
| --- | --- | --- | --- |
| (5.29) |  | U~tj≔𝖤j​[Utj|ℱt2],for j=0,1.\widetilde{U}^{j}\_{t}\coloneqq\mathsf{E}^{j}\big[U^{j}\_{t}\big|\mathcal{F}^{2}\_{t}\big],\quad\text{for $j=0,1$.} |  |

Observe that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (5.30) |  | 𝖤​[𝟏{𝒥=1}​U~t1|ℱt2]\displaystyle\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=1\}}\widetilde{U}^{1}\_{t}\big|\mathcal{F}^{2}\_{t}\big] | =ψt​U~t1=ψt​𝖤1​[Ut1|ℱt2]=𝖤​[𝟏{𝒥=1}​Ut1|ℱt2],\displaystyle=\psi\_{t}\widetilde{U}^{1}\_{t}=\psi\_{t}\mathsf{E}^{1}\big[U^{1}\_{t}\big|\mathcal{F}^{2}\_{t}\big]=\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=1\}}U^{1}\_{t}\big|\mathcal{F}^{2}\_{t}\big], |  |
|  | 𝖤​[𝟏{𝒥=0}​U~t0|ℱt2]\displaystyle\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=0\}}\widetilde{U}^{0}\_{t}\big|\mathcal{F}^{2}\_{t}\big] | =(1−ψt)​U~t0=(1−ψt)​𝖤0​[Ut0|ℱt2]=𝖤​[𝟏{𝒥=0}​Ut0|ℱt2],\displaystyle=(1-\psi\_{t})\widetilde{U}^{0}\_{t}=(1-\psi\_{t})\mathsf{E}^{0}\big[U^{0}\_{t}\big|\mathcal{F}^{2}\_{t}\big]=\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=0\}}U^{0}\_{t}\big|\mathcal{F}^{2}\_{t}\big], |  |

where we used ([5.29](https://arxiv.org/html/2510.15616v1#S5.E29 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) in the centre equalities. We will use these identities in deriving the relationship between values of the informed and uninformed players.

###### Remark 5.6.

A more explicit representation of U~j\widetilde{U}^{j} can be provided when ζt∗,j<1\zeta^{\*,j}\_{t}<1 for all t∈[0,T)t\in[0,T). Since the Brownian filtration completed with 𝖯\mathsf{P}-null sets is continuous and 𝔽Xj=𝔽W\mathbb{F}^{X^{j}}=\mathbb{F}^{W}, Theorem [3.4](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") implies that (Ut0)t∈[0,T)(U^{0}\_{t})\_{t\in[0,T)} and (Ut1)t∈[0,T)(U^{1}\_{t})\_{t\in[0,T)} are left-continuous. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
| (5.31) |  | Utj=χj​(t,X⋅∧tj),t∈[0,T],\displaystyle U^{j}\_{t}=\chi^{j}(t,X^{j}\_{\cdot\wedge t}),\quad t\in[0,T], |  |

for some measurable map χj:[0,T]×C​([0,T])→ℝ\chi^{j}:[0,T]\times C([0,T])\to\mathbb{R} which can be chosen so as to guarantee left-continuity of [0,T)∋t↦χj(t,x(⋅∧t))[0,T)\ni t\mapsto\chi^{j}(t,x(\cdot\wedge t)) for any x​(⋅)∈C​([0,T])x(\cdot)\in C([0,T]); the left-continuity at TT is not needed as this is only a single point, so the mapping can be extended to cover it in a measurable way.

This has an important consequence allowing us to construct processes U~tj\widetilde{U}^{j}\_{t} explicitly as U~tj≔χj​(t,X⋅∧t)\widetilde{U}^{j}\_{t}\coloneqq\chi^{j}(t,X\_{\cdot\wedge t}) for j=0,1j=0,1, instead of using the definition in ([5.29](https://arxiv.org/html/2510.15616v1#S5.E29 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")). Indeed, the processes (U~tj)t∈[0,T](\widetilde{U}^{j}\_{t})\_{t\in[0,T]} are 𝔽2\mathbb{F}^{2}-adapted and left-continuous everywhere apart from TT (thus optional) and the following identities trivially hold

|  |  |  |  |
| --- | --- | --- | --- |
| (5.32) |  | 𝟏{𝒥=0}​U~t0=𝟏{𝒥=0}​Ut0and𝟏{𝒥=1}​U~t1=𝟏{𝒥=1}​Ut1.\displaystyle\mathbf{1}\_{\{\mathcal{J}=0\}}\widetilde{U}^{0}\_{t}=\mathbf{1}\_{\{\mathcal{J}=0\}}U^{0}\_{t}\quad\text{and}\quad\mathbf{1}\_{\{\mathcal{J}=1\}}\widetilde{U}^{1}\_{t}=\mathbf{1}\_{\{\mathcal{J}=1\}}U^{1}\_{t}. |  |

We also observe that taking conditional expectations in ([5.32](https://arxiv.org/html/2510.15616v1#S5.E32 "In Remark 5.6. ‣ 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψt​U~t1\displaystyle\psi\_{t}\widetilde{U}^{1}\_{t} | =𝖤​[𝟏{𝒥=1}​U~t1|ℱt2]=𝖤​[𝟏{𝒥=1}​Ut1|ℱt2]=ψt​𝖤1​[Ut1|ℱt2],\displaystyle=\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=1\}}\widetilde{U}^{1}\_{t}\big|\mathcal{F}^{2}\_{t}\big]=\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=1\}}U^{1}\_{t}\big|\mathcal{F}^{2}\_{t}\big]=\psi\_{t}\mathsf{E}^{1}\big[U^{1}\_{t}\big|\mathcal{F}^{2}\_{t}\big], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−ψt)​U~t0\displaystyle(1-\psi\_{t})\widetilde{U}^{0}\_{t} | =𝖤​[𝟏{𝒥=0}​U~t0|ℱt2]=𝖤​[𝟏{𝒥=0}​Ut0|ℱt2]=(1−ψt)​𝖤0​[Ut0|ℱt2],\displaystyle=\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=0\}}\widetilde{U}^{0}\_{t}\big|\mathcal{F}^{2}\_{t}\big]=\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=0\}}U^{0}\_{t}\big|\mathcal{F}^{2}\_{t}\big]=(1-\psi\_{t})\mathsf{E}^{0}\big[U^{0}\_{t}\big|\mathcal{F}^{2}\_{t}\big], |  |

whence the relationship U~tj=𝖤j​[Utj|ℱt2]\widetilde{U}^{j}\_{t}=\mathsf{E}^{j}\big[U^{j}\_{t}\big|\mathcal{F}^{2}\_{t}\big] for j=0,1j=0,1 as in ([5.29](https://arxiv.org/html/2510.15616v1#S5.E29 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")).

This construction provides an intuitive interpretation of U~j\widetilde{U}^{j}. This is the value process of the first optimal stopping problem in ([5.28](https://arxiv.org/html/2510.15616v1#S5.E28 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) perceived by the uninformed player who only observes (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} but believes that 𝒥=j\mathcal{J}=j (irrespective of the true value of this random variable).

Relationship between the equilibrium value processes and the role of the belief process. From the second statement in Remark [3.12](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem12 "Remark 3.12. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"), we have

|  |  |  |
| --- | --- | --- |
|  | (1−ζγ−∗)​𝖤​[(1−ξγ−∗)​V∗,1​(γ)|ℱγ2]=𝖤​[1−ξγ−∗|ℱγ2]​(1−ζγ−∗)​V∗,2​(γ)(1-\zeta^{\*}\_{\gamma-})\mathsf{E}\big[(1-\xi^{\*}\_{\gamma-})V^{\*,1}(\gamma)|\mathcal{F}^{2}\_{\gamma}\big]=\mathsf{E}\big[1-\xi^{\*}\_{\gamma-}|\mathcal{F}^{2}\_{\gamma}\big](1-\zeta^{\*}\_{\gamma-})V^{\*,2}(\gamma) |  |

for any γ∈𝒯​(𝔽2)\gamma\in\mathcal{T}(\mathbb{F}^{2}). Recalling ([5.27](https://arxiv.org/html/2510.15616v1#S5.E27 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")), the right-hand side reads

|  |  |  |
| --- | --- | --- |
|  | ⟨ψγ,1−ξ~γ−∗⟩​(1−ζγ−∗)​V∗,2​(γ)=⟨ψγ,1−ξ~γ−∗⟩​(1−ζγ−∗)​Vγ.\langle\psi\_{\gamma},1-\tilde{\xi}^{\*}\_{\gamma-}\rangle(1-\zeta^{\*}\_{\gamma-})V^{\*,2}(\gamma)=\langle\psi\_{\gamma},1-\tilde{\xi}^{\*}\_{\gamma-}\rangle(1-\zeta^{\*}\_{\gamma-})V\_{\gamma}. |  |

For the left-hand side, recalling ([5.19](https://arxiv.org/html/2510.15616v1#S5.E19 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) and ([5.29](https://arxiv.org/html/2510.15616v1#S5.E29 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (5.33) |  |  | (1−ζγ−∗)​𝖤​[(1−ξγ−∗)​V∗,1​(γ)|ℱγ2]\displaystyle(1-\zeta^{\*}\_{\gamma-})\mathsf{E}\big[(1-\xi^{\*}\_{\gamma-})V^{\*,1}(\gamma)\big|\mathcal{F}^{2}\_{\gamma}\big] |  |
|  |  | =𝖤​[(1−ζγ−∗)​(𝟏{𝒥=0}​(1−ξγ−∗,0)​U0​(γ)+𝟏{𝒥=1}​(1−ξγ−∗,1)​U1​(γ))|ℱγ2]\displaystyle=\mathsf{E}\big[(1-\zeta^{\*}\_{\gamma-})\big(\mathbf{1}\_{\{\mathcal{J}=0\}}(1-\xi^{\*,0}\_{\gamma-})U^{0}(\gamma)+\mathbf{1}\_{\{\mathcal{J}=1\}}(1-\xi^{\*,1}\_{\gamma-})U^{1}(\gamma)\big)\big|\mathcal{F}^{2}\_{\gamma}\big] |  |
|  |  | =𝖤​[(1−ζγ−∗)​(𝟏{𝒥=0}​(1−ξ~γ−∗,0)​Uγ0+𝟏{𝒥=1}​(1−ξ~γ−∗,1)​Uγ1)|ℱγ2]\displaystyle=\mathsf{E}\big[(1-\zeta^{\*}\_{\gamma-})\big(\mathbf{1}\_{\{\mathcal{J}=0\}}(1-\tilde{\xi}^{\*,0}\_{\gamma-})U^{0}\_{\gamma}+\mathbf{1}\_{\{\mathcal{J}=1\}}(1-\tilde{\xi}^{\*,1}\_{\gamma-})U^{1}\_{\gamma}\big)\big|\mathcal{F}^{2}\_{\gamma}\big] |  |
|  |  | =(1−ζγ−∗)​(1−ξ~γ−∗,0)​𝖤​[𝟏{𝒥=0}​Uγ0|ℱγ2]+(1−ζγ−∗)​(1−ξ~γ−∗,1)​𝖤​[𝟏{𝒥=1}​Uγ1|ℱγ2]\displaystyle=(1-\zeta^{\*}\_{\gamma-})(1-\tilde{\xi}^{\*,0}\_{\gamma-})\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=0\}}U^{0}\_{\gamma}|\mathcal{F}^{2}\_{\gamma}\big]+(1-\zeta^{\*}\_{\gamma-})(1-\tilde{\xi}^{\*,1}\_{\gamma-})\mathsf{E}\big[\mathbf{1}\_{\{\mathcal{J}=1\}}U^{1}\_{\gamma}|\mathcal{F}^{2}\_{\gamma}\big] |  |
|  |  | =(1−ζγ−∗)​(1−ξ~γ−∗,0)​(1−ψγ)​𝖤0​[Uγ0|ℱγ2]+(1−ζγ−∗)​(1−ξ~γ−∗,1)​ψγ​𝖤1​[Uγ1|ℱγ2]\displaystyle=(1-\zeta^{\*}\_{\gamma-})(1-\tilde{\xi}^{\*,0}\_{\gamma-})(1-\psi\_{\gamma})\mathsf{E}^{0}\big[U^{0}\_{\gamma}|\mathcal{F}^{2}\_{\gamma}\big]+(1-\zeta^{\*}\_{\gamma-})(1-\tilde{\xi}^{\*,1}\_{\gamma-})\psi\_{\gamma}\mathsf{E}^{1}\big[U^{1}\_{\gamma}|\mathcal{F}^{2}\_{\gamma}\big] |  |
|  |  | =(1−ζγ−∗)​⟨ψγ,1−ξγ−∗⟩​((1−pγ)​U~γ0+pγ​U~γ1),\displaystyle=(1-\zeta^{\*}\_{\gamma-})\langle\psi\_{\gamma},1-\xi^{\*}\_{\gamma-}\rangle\Big((1-p\_{\gamma})\widetilde{U}^{0}\_{\gamma}+p\_{\gamma}\widetilde{U}^{1}\_{\gamma}\Big), |  |

where in the final expression we recalled the form of pγp\_{\gamma} from ([5.25](https://arxiv.org/html/2510.15616v1#S5.E25 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")).
Combining the above expressions we obtain

|  |  |  |
| --- | --- | --- |
|  | (1−ζγ−∗)​⟨ψγ,1−ξ~γ−∗⟩​((1−pγ)​U~γ0+pγ​U~γ1)=(1−ζγ−∗)​⟨ψγ,1−ξ~γ−∗⟩​Vγ,(1-\zeta^{\*}\_{\gamma-})\langle\psi\_{\gamma},1-\tilde{\xi}^{\*}\_{\gamma-}\rangle\Big((1-p\_{\gamma})\widetilde{U}^{0}\_{\gamma}+p\_{\gamma}\widetilde{U}^{1}\_{\gamma}\Big)=(1-\zeta^{\*}\_{\gamma-})\langle\psi\_{\gamma},1-\tilde{\xi}^{\*}\_{\gamma-}\rangle V\_{\gamma}, |  |

which reads more neatly as

|  |  |  |
| --- | --- | --- |
|  | ⟨pγ,U~γ⟩=Vγ,on the set Γγ2,\langle p\_{\gamma},\widetilde{U}\_{\gamma}\rangle=V\_{\gamma},\quad\text{on the set $\Gamma^{2}\_{\gamma}$}, |  |

where Γγ2={ξ~γ∗,1∧ξ~γ∗,0<1​ and ​ζγ∗<1}\Gamma^{2}\_{\gamma}=\{\tilde{\xi}^{\*,1}\_{\gamma}\wedge\tilde{\xi}^{\*,0}\_{\gamma}<1\text{ and }\zeta^{\*}\_{\gamma}<1\}, cf. ([5.11](https://arxiv.org/html/2510.15616v1#S5.E11 "In 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")).
The main difference with the setting from Section [5.1](https://arxiv.org/html/2510.15616v1#S5.SS1 "5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") is that therein the posterior of the uninformed player is only updated via the actions of the more informed player. Here instead, the sole observation of the underlying process XX already yields some posterior information ψ\psi about 𝒥\mathcal{J}.

Martingale characterisation. Take ξ∈𝒜0∘​(𝔽1)\xi\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{1}) with decomposition ξ=𝟏{𝒥=0}​ξ0+𝟏{𝒥=1}​ξ1\xi=\mathbf{1}\_{\{\mathcal{J}=0\}}\xi^{0}+\mathbf{1}\_{\{\mathcal{J}=1\}}\xi^{1}, where (ξ0,ξ1)∈𝒜0∘​(𝔽W)(\xi^{0},\xi^{1})\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{W}), and ζ∈𝒜0∘​(𝔽2)\zeta\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}). Recall the 𝔽1\mathbb{F}^{1}-optional submartingale (Mtξ)t∈[0,T](M^{\xi}\_{t})\_{t\in[0,T]} and the 𝔽2\mathbb{F}^{2}-optional supermartingale (Ntζ)t∈[0,T](N^{\zeta}\_{t})\_{t\in[0,T]} from Proposition [3.9](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem9 "Proposition 3.9. ‣ 3.3. Proof of Theorem 3.4 and some further results ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information"). The former reads as follows: for any θ=(θ0,θ1)∈𝒯0​(𝔽1)\theta=(\theta^{0},\theta^{1})\in\mathcal{T}\_{0}(\mathbb{F}^{1})

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mθξ\displaystyle M^{\xi}\_{\theta} | =∑i=01𝟏{𝒥=i}​(∫[0,θi)[(1−ζt∗,i)​fti+Δ​ζt∗,i​hti]​dξti+∫[0,θi)(1−ξti)​gti​dζt∗,i+(1−ξθi−i)​(1−ζθi−∗,i)​Uθii)\displaystyle=\sum\_{i=0}^{1}\mathbf{1}\_{\{\mathcal{J}=i\}}\Big(\int\_{[0,\theta\_{i})}\!\big[(1\!-\!\zeta^{\*,i}\_{t})f^{i}\_{t}\!+\!\Delta\zeta^{\*,i}\_{t}h^{i}\_{t}\big]\mathrm{d}\xi^{i}\_{t}\!+\!\int\_{[0,\theta\_{i})}(1\!-\!\xi^{i}\_{t})g^{i}\_{t}\mathrm{d}\zeta^{\*,i}\_{t}\!+\!(1\!-\!\xi^{i}\_{\theta\_{i}-})(1\!-\!\zeta^{\*,i}\_{\theta\_{i}-})U^{i}\_{\theta\_{i}}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =:𝟏{𝒥=0}Mθ0ξ0;0+𝟏{𝒥=1}Mθ1ξ1;1,\displaystyle=:\mathbf{1}\_{\{\mathcal{J}=0\}}M^{\xi^{0};0}\_{\theta\_{0}}+\mathbf{1}\_{\{\mathcal{J}=1\}}M^{\xi^{1};1}\_{\theta\_{1}}, |  |

where (Mtξ;i)t∈[0,T](M^{\xi;i}\_{t})\_{t\in[0,T]}, i=0,1i=0,1, are 𝔽1\mathbb{F}^{1}-optional submartingales.

The derivation of the expression for (Ntζ)t∈[0,T](N^{\zeta}\_{t})\_{t\in[0,T]} deserves more detail. Notice that ft≔f​(t,Xt)f\_{t}\coloneqq f(t,X\_{t}), gt≔g​(t,Xt)g\_{t}\coloneqq g(t,X\_{t}), ht≔h​(t,Xt)h\_{t}\coloneqq h(t,X\_{t}) are ℱt2\mathcal{F}^{2}\_{t}-measurable for all t∈[0,T]t\in[0,T]. Then for γ∈𝒯0​(𝔽2)\gamma\in\mathcal{T}\_{0}(\mathbb{F}^{2})

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[∫[0,γ)[ft​(1−ζt)+ht​Δ​ζt]​dξt∗|ℱγ2]\displaystyle\mathsf{E}\Big[\!\int\_{[0,\gamma)}\!\!\big[f\_{t}(1\!-\!\zeta\_{t})+h\_{t}\Delta\zeta\_{t}\big]\mathrm{d}\xi^{\*}\_{t}\Big|\mathcal{F}^{2}\_{\gamma}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =∑j=01𝖤​[𝟏{𝒥=j}​∫[0,γ)[ft​(1−ζt)+ht​Δ​ζt]​dξt∗,j|ℱγ2]\displaystyle=\sum\_{j=0}^{1}\mathsf{E}\Big[\mathbf{1}\_{\{\mathcal{J}=j\}}\int\_{[0,\gamma)}\!\!\big[f\_{t}(1\!-\!\zeta\_{t})+h\_{t}\Delta\zeta\_{t}\big]\mathrm{d}\xi^{\*,j}\_{t}\Big|\mathcal{F}^{2}\_{\gamma}\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | =∑j=01𝖤​[𝟏{𝒥=j}|ℱγ2]​∫[0,γ)[ft​(1−ζt)+ht​Δ​ζt]​dξ~t∗,j\displaystyle=\sum\_{j=0}^{1}\mathsf{E}\Big[\mathbf{1}\_{\{\mathcal{J}=j\}}\Big|\mathcal{F}^{2}\_{\gamma}\Big]\int\_{[0,\gamma)}\!\!\big[f\_{t}(1\!-\!\zeta\_{t})+h\_{t}\Delta\zeta\_{t}\big]\mathrm{d}\tilde{\xi}^{\*,j}\_{t} |  |
|  |  |  |
| --- | --- | --- |
|  | =ψγ​∫[0,γ)[ft​(1−ζt)+ht​Δ​ζt]​dξ~t∗,1+(1−ψγ)​∫[0,γ)[ft​(1−ζt)+ht​Δ​ζt]​dξ~t∗,0.\displaystyle=\psi\_{\gamma}\int\_{[0,\gamma)}\!\!\big[f\_{t}(1\!-\!\zeta\_{t})+h\_{t}\Delta\zeta\_{t}\big]\mathrm{d}\tilde{\xi}^{\*,1}\_{t}+(1-\psi\_{\gamma})\int\_{[0,\gamma)}\!\!\big[f\_{t}(1\!-\!\zeta\_{t})+h\_{t}\Delta\zeta\_{t}\big]\mathrm{d}\tilde{\xi}^{\*,0}\_{t}. |  |

Analogous calculations yield

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[∫[0,γ)gt​(1−ξ~t∗)​dζt|ℱγ2]=ψγ​∫[0,γ)gt​(1−ξ~t∗,1)​dζt+(1−ψγ)​∫[0,γ)gt​(1−ξ~t∗,0)​dζt.\mathsf{E}\Big[\int\_{[0,\gamma)}\!\!g\_{t}(1\!-\!\tilde{\xi}^{\*}\_{t})\mathrm{d}\zeta\_{t}\Big|\mathcal{F}^{2}\_{\gamma}\Big]=\psi\_{\gamma}\int\_{[0,\gamma)}\!\!g\_{t}(1\!-\!\tilde{\xi}^{\*,1}\_{t})\mathrm{d}\zeta\_{t}+(1-\psi\_{\gamma})\int\_{[0,\gamma)}\!\!g\_{t}(1\!-\!\tilde{\xi}^{\*,0}\_{t})\mathrm{d}\zeta\_{t}. |  |

Combining those expressions with ([5.27](https://arxiv.org/html/2510.15616v1#S5.E27 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Nγζ\displaystyle N^{\zeta}\_{\gamma} | =(1−ψγ)​(∫[0,γ)[ft​(1−ζt)+ht​Δ​ζt]​dξ~t∗,0+∫[0,γ)gt​(1−ξ~t∗,0)​dζt)\displaystyle=(1-\psi\_{\gamma})\Big(\int\_{[0,\gamma)}\!\!\big[f\_{t}(1\!-\!\zeta\_{t})+h\_{t}\Delta\zeta\_{t}\big]\mathrm{d}\tilde{\xi}^{\*,0}\_{t}+\int\_{[0,\gamma)}\!\!g\_{t}(1\!-\!\tilde{\xi}^{\*,0}\_{t})\mathrm{d}\zeta\_{t}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ψγ​(∫[0,γ)[ft​(1−ζt)+ht​Δ​ζt]​dξ~t∗,1+∫[0,γ)gt​(1−ξ~t∗,1)​dζt)+(1−ζγ−)​⟨ψγ,1−ξ~γ−∗⟩​Vγ.\displaystyle\quad+\psi\_{\gamma}\Big(\int\_{[0,\gamma)}\!\!\big[f\_{t}(1\!-\!\zeta\_{t})+h\_{t}\Delta\zeta\_{t}\big]\mathrm{d}\tilde{\xi}^{\*,1}\_{t}+\int\_{[0,\gamma)}\!\!g\_{t}(1\!-\!\tilde{\xi}^{\*,1}\_{t})\mathrm{d}\zeta\_{t}\Big)+\!(1\!-\!\zeta\_{\gamma-})\langle\psi\_{\gamma},1\!-\!\tilde{\xi}^{\*}\_{\gamma-}\rangle V\_{\gamma}. |  |

It is also worth noticing that by an application of Itô’s formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | Nγζ\displaystyle N^{\zeta}\_{\gamma} | =∫[0,γ)(1−ψt)​[ft​(1−ζt)+ht​Δ​ζt]​dξ~t∗,0+∫[0,γ)(1−ψt)​gt​(1−ξ~t∗,0)​dζt\displaystyle=\int\_{[0,\gamma)}\!\!(1-\psi\_{t})\big[f\_{t}(1\!-\!\zeta\_{t})+h\_{t}\Delta\zeta\_{t}\big]\mathrm{d}\tilde{\xi}^{\*,0}\_{t}+\int\_{[0,\gamma)}\!\!(1-\psi\_{t})g\_{t}(1\!-\!\tilde{\xi}^{\*,0}\_{t})\mathrm{d}\zeta\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫[0,γ)ψt​[ft​(1−ζt)+ht​Δ​ζt]​dξ~t∗,1+∫[0,γ)ψt​gt​(1−ξ~t∗,1)​dζt+(1−ζγ−)​⟨ψγ,1−ξ~γ−∗⟩​Vγ\displaystyle\quad+\int\_{[0,\gamma)}\!\!\psi\_{t}\big[f\_{t}(1\!-\!\zeta\_{t})+h\_{t}\Delta\zeta\_{t}\big]\mathrm{d}\tilde{\xi}^{\*,1}\_{t}+\int\_{[0,\gamma)}\!\!\psi\_{t}g\_{t}(1\!-\!\tilde{\xi}^{\*,1}\_{t})\mathrm{d}\zeta\_{t}\!+\!(1\!-\!\zeta\_{\gamma-})\langle\psi\_{\gamma},1\!-\!\tilde{\xi}^{\*}\_{\gamma-}\rangle V\_{\gamma} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0γ(∫[0,t)[fs​(1−ζs)+hs​Δ​ζs]​d​(ξ~s∗,1−ξ~s∗,0)+∫[0,t)gs​(ξ~s∗,0−ξ~s∗,1)​dζs)​dψt.\displaystyle\quad+\int\_{0}^{\gamma}\Big(\int\_{[0,t)}\!\!\big[f\_{s}(1\!-\!\zeta\_{s})+h\_{s}\Delta\zeta\_{s}\big]\mathrm{d}(\tilde{\xi}^{\*,1}\_{s}\!-\!\tilde{\xi}^{\*,0}\_{s})\!+\!\int\_{[0,t)}\!\!g\_{s}(\tilde{\xi}^{\*,0}\_{s}\!-\!\tilde{\xi}^{\*,1}\_{s})\mathrm{d}\zeta\_{s}\Big)\mathrm{d}\psi\_{t}. |  |

Since the integral in the last line is an 𝔽2\mathbb{F}^{2}-martingale and NζN^{\zeta} is an 𝔽2\mathbb{F}^{2}-optional supermartingale, we deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | N~γζ\displaystyle\widetilde{N}^{\zeta}\_{\gamma} | ≔∫[0,γ)(1−ψt)​[ft​(1−ζt)+ht​Δ​ζt]​dξ~t∗,0+∫[0,γ)(1−ψt)​gt​(1−ξ~t∗,0)​dζt\displaystyle\coloneqq\int\_{[0,\gamma)}\!\!(1-\psi\_{t})\big[f\_{t}(1\!-\!\zeta\_{t})+h\_{t}\Delta\zeta\_{t}\big]\mathrm{d}\tilde{\xi}^{\*,0}\_{t}+\int\_{[0,\gamma)}\!\!(1-\psi\_{t})g\_{t}(1\!-\!\tilde{\xi}^{\*,0}\_{t})\mathrm{d}\zeta\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫[0,γ)ψt​[ft​(1−ζt)+ht​Δ​ζt]​dξ~t∗,1+∫[0,γ)ψt​gt​(1−ξ~t∗,1)​dζt+(1−ζγ−)​⟨ψγ,1−ξ~γ−∗⟩​Vγ\displaystyle\quad+\int\_{[0,\gamma)}\!\!\psi\_{t}\big[f\_{t}(1\!-\!\zeta\_{t})+h\_{t}\Delta\zeta\_{t}\big]\mathrm{d}\tilde{\xi}^{\*,1}\_{t}+\int\_{[0,\gamma)}\!\!\psi\_{t}g\_{t}(1\!-\!\tilde{\xi}^{\*,1}\_{t})\mathrm{d}\zeta\_{t}\!+\!(1\!-\!\zeta\_{\gamma-})\langle\psi\_{\gamma},1\!-\!\tilde{\xi}^{\*}\_{\gamma-}\rangle V\_{\gamma} |  |

is an 𝔽2\mathbb{F}^{2}-optional supermartingale.

When ξ\xi and ζ\zeta are chosen optimally, the processes (Mtξ∗,0;0)t∈[0,T](M^{\xi^{\*,0};0}\_{t})\_{t\in[0,T]}, (Mtξ∗,1;1)t∈[0,T](M^{\xi^{\*,1};1}\_{t})\_{t\in[0,T]} become càdlàg 𝔽W\mathbb{F}^{W}-martingales and (Ntζ∗)t∈[0,T](N^{\zeta^{\*}}\_{t})\_{t\in[0,T]}, (N~tζ∗)t∈[0,T](\widetilde{N}^{\zeta^{\*}}\_{t})\_{t\in[0,T]} become càdlàg 𝔽2\mathbb{F}^{2}-martingales by Proposition [3.8](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").
Instead, when ξ\xi and ζ\zeta are taken equal to zero, the above processes take the form: for t∈[0,T]t\in[0,T],

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (5.34) |  | Mt0;i\displaystyle M^{0;i}\_{t} | =∫[0,t)gsi​dζs∗,i+(1−ζt−∗,i)​Uti,i=0,1,\displaystyle=\int\_{[0,t)}g^{i}\_{s}\mathrm{d}\zeta^{\*,i}\_{s}+(1-\zeta^{\*,i}\_{t-})U^{i}\_{t},\qquad i=0,1, |  |
|  | Nt0\displaystyle N^{0}\_{t} | =(1−ψt)​∫[0,t)fs​dξ~s∗,0+ψt​∫[0,t)fs​dξ~s∗,1+⟨ψt,1−ξ~t−∗⟩​Vt,\displaystyle=(1-\psi\_{t})\int\_{[0,t)}\!\!f\_{s}\mathrm{d}\tilde{\xi}^{\*,0}\_{s}\!+\!\psi\_{t}\int\_{[0,t)}\!\!f\_{s}\mathrm{d}\tilde{\xi}^{\*,1}\_{s}+\langle\psi\_{t},1\!-\!\tilde{\xi}^{\*}\_{t-}\rangle V\_{t}, |  |
|  | N~t0\displaystyle\widetilde{N}^{0}\_{t} | =∫[0,t)(1−ψs)​fs​dξ~s∗,0+∫[0,t)ψs​fs​dξ~s∗,1+⟨ψt,1−ξ~t−∗⟩​Vt.\displaystyle=\int\_{[0,t)}\!\!(1-\psi\_{s})f\_{s}\mathrm{d}\tilde{\xi}^{\*,0}\_{s}\!+\!\int\_{[0,t)}\!\!\psi\_{s}f\_{s}\mathrm{d}\tilde{\xi}^{\*,1}\_{s}+\langle\psi\_{t},1\!-\!\tilde{\xi}^{\*}\_{t-}\rangle V\_{t}. |  |

Proposition [3.7](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem7 "Proposition 3.7. ‣ 3.2. Auxiliary super/sub-martingale systems ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") asserts that (Mt0;i)t∈[0,T](M^{0;i}\_{t})\_{t\in[0,T]} is a càdlàg 𝔽W\mathbb{F}^{W}-submartingale and (Nt0)t∈[0,T](N^{0}\_{t})\_{t\in[0,T]} (hence also (N~t0)t∈[0,T](\widetilde{N}^{0}\_{t})\_{t\in[0,T]}) is a càdlàg 𝔽2\mathbb{F}^{2}-supermartingale. These can be shown to be martingales up to τ¯∗i​(z)\bar{\tau}^{i}\_{\*}(z) and σ¯∗​(z)\bar{\sigma}\_{\*}(z), respectively, for any z∈[0,1)z\in[0,1) by the same arguments as those employed in Section [5.1](https://arxiv.org/html/2510.15616v1#S5.SS1 "5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information").

Support of optimal strategies. In this paragraph, some minor changes, compared to the case with partially observed scenarios arise, due to the replacement of the prior π\pi with the posterior process ψt\psi\_{t}. In this spirit, it is worth noticing that since g​(t,Xt)g(t,X\_{t}) is ℱt2\mathcal{F}^{2}\_{t}-measurable

|  |  |  |  |
| --- | --- | --- | --- |
|  | (og⋅(1−ξ⋅∗))t𝔽2\displaystyle\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.98929pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\big(}^{{\kern-5.31067pt{o}\kern 3.5694pt}}\_{{\kern-3.11415pt\kern 3.5694pt}}}g\_{\cdot}(1-\xi^{\*}\_{\cdot})\big)^{\mathbb{F}^{2}}\_{t} | =𝖤​[g​(t,Xt)​(𝟏{𝒥=0}​(1−ξt∗,0)+𝟏{𝒥=1}​(1−ξt∗,1))|ℱt2]\displaystyle=\mathsf{E}\big[g(t,X\_{t})\big(\mathbf{1}\_{\{\mathcal{J}=0\}}(1-\xi^{\*,0}\_{t})+\mathbf{1}\_{\{\mathcal{J}=1\}}(1-\xi^{\*,1}\_{t})\big)\big|\mathcal{F}^{2}\_{t}\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =g​(t,Xt)​𝖤​[(𝟏{𝒥=0}​(1−ξ~t∗,0)+𝟏{𝒥=1}​(1−ξ~t∗,1))|ℱt2]=g​(t,Xt)​⟨ψt,1−ξ~t∗⟩,\displaystyle=g(t,X\_{t})\mathsf{E}\big[\big(\mathbf{1}\_{\{\mathcal{J}=0\}}(1-\tilde{\xi}^{\*,0}\_{t})+\mathbf{1}\_{\{\mathcal{J}=1\}}(1-\tilde{\xi}^{\*,1}\_{t})\big)\big|\mathcal{F}^{2}\_{t}\big]=g(t,X\_{t})\langle\psi\_{t},1-\tilde{\xi}^{\*}\_{t}\rangle, |  |

where we used ([5.27](https://arxiv.org/html/2510.15616v1#S5.E27 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")). Analogously,
(oh⋅Δξ⋅∗)t𝔽2=h(t,Xt)⟨ψt,Δξ~t∗⟩\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-4.5449pt{o}\kern 2.12502pt}}\_{{\kern-1.66977pt\kern 2.12502pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-4.5449pt{o}\kern 2.12502pt}}\_{{\kern-1.66977pt\kern 2.12502pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-2.64682pt{o}\kern 0.90555pt}}\_{{\kern-0.4503pt\kern 0.90555pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt(}^{{\kern-2.10239pt{o}\kern 0.36111pt}}\_{{\kern 0.09413pt\kern 0.36111pt}}}h\_{\cdot}\Delta\xi^{\*}\_{\cdot})^{\mathbb{F}^{2}}\_{t}=h(t,X\_{t})\langle\psi\_{t},\Delta\tilde{\xi}^{\*}\_{t}\rangle.
Then, in preparation for a statement of Proposition [3.17](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem17 "Proposition 3.17. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information") in this setting, let gt=g​(t,Xt)g\_{t}=g(t,X\_{t}), ht=h​(t,Xt)h\_{t}=h(t,X\_{t}) and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt1\displaystyle Y^{1}\_{t} | =∑i=01𝟏{𝒥=i}((1−ζt−∗,i)Uti−fti(1−ζt∗,i)−htiΔζt∗,i)=:𝟏{𝒥=0}Zt0+𝟏{𝒥=1}Zt1,\displaystyle=\sum\_{i=0}^{1}\mathbf{1}\_{\{\mathcal{J}=i\}}\big((1-\zeta^{\*,i}\_{t-})U^{i}\_{t}-f^{i}\_{t}(1-\zeta^{\*,i}\_{t})-h^{i}\_{t}\Delta\zeta^{\*,i}\_{t}\big)=:\mathbf{1}\_{\{\mathcal{J}=0\}}Z^{0}\_{t}+\mathbf{1}\_{\{\mathcal{J}=1\}}Z^{1}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt2\displaystyle Y^{2}\_{t} | =⟨ψt,1−ξ~t−∗⟩​Vt−gt​⟨ψt,1−ξ~t∗⟩−ht​⟨ψt,Δ​ξ~t∗⟩.\displaystyle=\langle\psi\_{t},1-\tilde{\xi}^{\*}\_{t-}\rangle V\_{t}-g\_{t}\langle\psi\_{t},1-\tilde{\xi}^{\*}\_{t}\rangle-h\_{t}\langle\psi\_{t},\Delta\tilde{\xi}^{\*}\_{t}\rangle. |  |

Corollary [5.1](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem1 "Corollary 5.1. ‣ 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") holds in the same form and similar considerations as in the paragraph following it apply to the present case with obvious notational changes.

###### Corollary 5.7.

We have Zt0≤0Z^{0}\_{t}\leq 0, Zt1≤0Z^{1}\_{t}\leq 0 and Yt2≥0Y^{2}\_{t}\geq 0 for all t∈[0,T]t\in[0,T], 𝖯\mathsf{P}-a.s. Moreover,

|  |  |  |
| --- | --- | --- |
|  | ∫[0,T]Zt0​dξt∗,0+∫[0,T]Zt1​dξt∗,1=0and∫[0,T]Yt2​dζt∗=0.\int\_{[0,T]}Z^{0}\_{t}\mathrm{d}\xi^{\*,0}\_{t}+\int\_{[0,T]}Z^{1}\_{t}\mathrm{d}\xi^{\*,1}\_{t}=0\quad\text{and}\quad\int\_{[0,T]}Y^{2}\_{t}\mathrm{d}\zeta^{\*}\_{t}=0. |  |

The statement of Corollary [5.7](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem7 "Corollary 5.7. ‣ 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") can be rewritten in a more intuitive way under the ansatz that no simultaneous jump of the generating processes occurs for t<Tt<T. That is:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∫[0,T)(Uti−fti)​(1−ζt∗,i)​dξt∗,i=0,\displaystyle\int\_{[0,T)}(U^{i}\_{t}-f^{i}\_{t})(1-\zeta^{\*,i}\_{t})\mathrm{d}\xi^{\*,i}\_{t}=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (UTi−hTi)​Δ​ζT∗,i​Δ​ξT∗,i=0,\displaystyle(U^{i}\_{T}-h^{i}\_{T})\Delta\zeta^{\*,i}\_{T}\Delta\xi^{\*,i}\_{T}=0, |  |

for i=0,1i=0,1, and

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∫[0,T)⟨ψt,(1−ξ~t−∗)⟩​(Vt−gt)​dζt∗=0,\displaystyle\int\_{[0,T)}\langle\psi\_{t},(1-\tilde{\xi}^{\*}\_{t-})\rangle\big(V\_{t}-g\_{t}\big)\mathrm{d}\zeta^{\*}\_{t}=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⟨ψT,(1−ξ~T−∗)⟩​(VT−hT)​Δ​ζT∗=0.\displaystyle\langle\psi\_{T},(1-\tilde{\xi}^{\*}\_{T-})\rangle\big(V\_{T}-h\_{T}\big)\Delta\zeta^{\*}\_{T}=0. |  |

The formulae above convey the intuitive idea that the ii-th incarnation of the informed player should only stop (with some probability) when the corresponding value process UiU^{i} equals the stopping payoff fif^{i}. Instead, the uninformed player should only stop (with some probability) when the value process VV equals the stopping payoff gg.

Sufficient conditions. An analogue of Corollary [5.2](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem2 "Corollary 5.2. ‣ 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") holds with non-obvious changes to the notation and assumptions. Recall that ftj=f​(t,Xtj)f^{j}\_{t}=f(t,X^{j}\_{t}), gtj=g​(t,Xtj)g^{j}\_{t}=g(t,X^{j}\_{t}), htj=h​(t,Xtj)h^{j}\_{t}=h(t,X^{j}\_{t}) and ft=f​(t,Xt)f\_{t}=f(t,X\_{t}), gt=g​(t,Xt)g\_{t}=g(t,X\_{t}), ht=h​(t,Xt)h\_{t}=h(t,X\_{t}) with X=X𝒥X=X^{\mathcal{J}}. Let Υ\varUpsilon be the class of measurable maps Φ:[0,T]×C​([0,T])→[0,1]\Phi:[0,T]\times C([0,T])\to[0,1] such that (Φ​(t,X⋅∧t))t∈[0,T](\Phi(t,X\_{\cdot\wedge t}))\_{t\in[0,T]} belongs to 𝒜0∘​(𝔽2)\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}) whereas (Φ​(t,X⋅∧t0))t∈[0,T](\Phi(t,X^{0}\_{\cdot\wedge t}))\_{t\in[0,T]} and (Φ​(t,X⋅∧t1))t∈[0,T](\Phi(t,X^{1}\_{\cdot\wedge t}))\_{t\in[0,T]} belong to 𝒜0∘​(𝔽W)\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{W}).
Then Υ\varUpsilon is the family of maps that determine admissible strategies according to ([5.19](https://arxiv.org/html/2510.15616v1#S5.E19 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) and ([5.26](https://arxiv.org/html/2510.15616v1#S5.E26 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")).

###### Corollary 5.8.

Let (Ut0)t∈[0,T](U^{0}\_{t})\_{t\in[0,T]}, (Ut1)t∈[0,T](U^{1}\_{t})\_{t\in[0,T]} be 𝔽W\mathbb{F}^{W}-progressively measurable and (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]} be 𝔽2\mathbb{F}^{2}-progressively measurable. Let Ξ^0,Ξ^1,Λ^∈Υ\hat{\Xi}^{0},\hat{\Xi}^{1},\hat{\Lambda}\in\varUpsilon. Define ξ^ti=Ξ^i​(t,X⋅∧t)\hat{\xi}^{i}\_{t}=\hat{\Xi}^{i}(t,X\_{\cdot\wedge t}) and ζ^ti=Λ^​(t,X⋅∧ti)\hat{\zeta}^{i}\_{t}=\hat{\Lambda}(t,X^{i}\_{\cdot\wedge t}) for i=0,1i=0,1; hence, ξ^i∈𝒜0∘​(𝔽2)\hat{\xi}^{i}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{2}) and ζ^i∈𝒜0∘​(𝔽W)\hat{\zeta}^{i}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{0}(\mathbb{F}^{W}). Set, for t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | M^t0;i\displaystyle\hat{M}^{0;i}\_{t} | =∫[0,t)g​(s,Xsi)​dζ^si+(1−ζ^t−i)​Uti,\displaystyle=\int\_{[0,t)}g(s,X^{i}\_{s})\mathrm{d}\hat{\zeta}^{i}\_{s}+(1-\hat{\zeta}^{i}\_{t-})U^{i}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | N^t0\displaystyle\hat{N}^{0}\_{t} | =∫[0,t)f​(s,Xs)​⟨ψs,d​ξ^s⟩+⟨ψt,1−ξ^t−⟩​Vt.\displaystyle=\int\_{[0,t)}f(s,X\_{s})\langle\psi\_{s},\mathrm{d}\hat{\xi}\_{s}\rangle+\langle\psi\_{t},1-\hat{\xi}\_{t-}\rangle V\_{t}. |  |

Assume that

1. (i)

   the process (M^t0;i)t∈[0,T](\hat{M}^{0;i}\_{t})\_{t\in[0,T]} is an 𝔽W\mathbb{F}^{W}-submartingale for i=0,1i=0,1,
2. (ii)

   the process (N^t0)t∈[0,T](\hat{N}^{0}\_{t})\_{t\in[0,T]} is an 𝔽2\mathbb{F}^{2}-supermartingale,
3. (iii)

   for i=0,1i=0,1, it holds 𝖯\mathsf{P}-a.s.,

   |  |  |  |
   | --- | --- | --- |
   |  | f​(t,Xti)+(h−f)​(t,Xti)​Δ​ζ^ti1−ζ^t−i≥Uti,for all t∈[0,T] such that ζ^t−i<1,f(t,X^{i}\_{t})+\frac{(h-f)(t,X^{i}\_{t})\Delta\hat{\zeta}^{i}\_{t}}{1-\hat{\zeta}^{i}\_{t-}}\geq U^{i}\_{t},\quad\text{for all $t\in[0,T]$ such that $\hat{\zeta}^{i}\_{t-}<1$}, |  |
4. (iv)

   it holds 𝖯\mathsf{P}-a.s.,

   |  |  |  |
   | --- | --- | --- |
   |  | g​(t,Xt)+(h−g)​(t,Xt)​⟨ψt,Δ​ξ^t⟩⟨ψt,1−ξ^t−⟩≤Vt,for all t∈[0,T] such that ⟨ψt,1−ξ^t−⟩>0,g(t,X\_{t})+\frac{(h-g)(t,X\_{t})\langle\psi\_{t},\Delta\hat{\xi}\_{t}\rangle}{\langle\psi\_{t},1-\hat{\xi}\_{t-}\rangle}\leq V\_{t},\quad\text{for all $t\in[0,T]$ such that $\langle\psi\_{t},1-\hat{\xi}\_{t-}\rangle>0$,} |  |
5. (v)

   V0=𝖤​[𝟏{𝒥=0}​U00+𝟏{𝒥=1}​U01]V\_{0}=\mathsf{E}[\mathbf{1}\_{\{\mathcal{J}=0\}}U^{0}\_{0}+\mathbf{1}\_{\{\mathcal{J}=1\}}U^{1}\_{0}].

Then the value of the game equals V0V\_{0} and a saddle point is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.35) |  | (ξt∗,0,ξt∗,1)t∈[0,T]=(Ξ^0​(t,X⋅∧t0),Ξ^1​(t,X⋅∧t1))t∈[0,T]and(ζt∗)t∈[0,T]=(Λ^​(t,X⋅∧t))t∈[0,T].(\xi^{\*,0}\_{t},\xi^{\*,1}\_{t})\_{t\in[0,T]}=\big(\hat{\Xi}^{0}(t,X^{0}\_{\cdot\wedge t}),\hat{\Xi}^{1}(t,X^{1}\_{\cdot\wedge t})\big)\_{t\in[0,T]}\quad\text{and}\quad(\zeta^{\*}\_{t})\_{t\in[0,T]}=\big(\hat{\Lambda}(t,X\_{\cdot\wedge t})\big)\_{t\in[0,T]}. |  |

We defined players’ strategies via maps in Υ\varUpsilon because each strategy appears in two guises depending on the player inspecting it. The assumptions of the corollary view the strategies through the lens of the opponent: the uninformed player considers ξ^0\hat{\xi}^{0} (resp. ξ^1\hat{\xi}^{1}) which arises when the player pretends that 𝒥=0\mathcal{J}=0 (resp. 𝒥=1\mathcal{J}=1) but observes only the process XX – these are the counterparts of ξ~0,ξ~1\tilde{\xi}^{0},\tilde{\xi}^{1} in the first part of this subsection discussing the necessary conditions; the informed player instead is able to separate the strategy of the uninformed player based on the observation of 𝒥\mathcal{J}, see ([5.26](https://arxiv.org/html/2510.15616v1#S5.E26 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")). The saddle point ([5.35](https://arxiv.org/html/2510.15616v1#S5.E35 "In Corollary 5.8. ‣ 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) requires inserting appropriate processes into the maps Ξ^0\hat{\Xi}^{0}, Ξ^1\hat{\Xi}^{1} and Λ^\hat{\Lambda} depending on the players’ filtrations. The overall idea, which is common in game theory, is that both players know the equilibrium maps Ξ^0\hat{\Xi}^{0}, Ξ^1\hat{\Xi}^{1} and Λ^\hat{\Lambda} but the uninformed player can only compute the realised trajectories of the increasing processes conditional upon the observed filtration.

Notice that the choice of the process N^0\hat{N}^{0} in the statement above is motivated by N~0\widetilde{N}^{0} in ([5.34](https://arxiv.org/html/2510.15616v1#S5.E34 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) and the equivalence between N0N^{0} and N~0\widetilde{N}^{0} therein, up to a martingale process. We avoid repeating also Corollary [5.3](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem3 "Corollary 5.3. ‣ 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information"), which holds in analogous fashion.

### 5.3. A heuristic derivation of PDE systems

Corollaries [5.2](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem2 "Corollary 5.2. ‣ 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") and [5.8](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem8 "Corollary 5.8. ‣ 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") suggest a practical approach to the actual construction of the equilibrium payoffs. Although it is unclear how to formulate a rigorous statement, we want to discuss here some natural ideas that hopefully can provide useful tools for practical solution of specific problems. We start with the problem presented in Section [5.2](https://arxiv.org/html/2510.15616v1#S5.SS2 "5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") and conclude with the game from Section [5.1](https://arxiv.org/html/2510.15616v1#S5.SS1 "5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information").

Partially observed dynamics.
Let p^t\hat{p}\_{t} be defined as in ([5.25](https://arxiv.org/html/2510.15616v1#S5.E25 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) but with ξ~∗\tilde{\xi}^{\*} replaced by ξ^\hat{\xi} from Corollary [5.8](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem8 "Corollary 5.8. ‣ 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information"). If we postulate that Utj=uj​(t,p^t,Xtj)U^{j}\_{t}=u^{j}(t,\hat{p}\_{t},X^{j}\_{t}) for j=0,1j=0,1 and Vt=v​(t,p^t,Xt)V\_{t}=v(t,\hat{p}\_{t},X\_{t}) for suitable functions uju^{j} and vv to be determined, then we can connect conditions (i)–(v) from the corollary above to an analytical problem. With a small loss of generality, let us restrict our attention to a situation where the processes ξ^i,ζ^i\hat{\xi}^{i},\hat{\zeta}^{i}, i=0.1i=0.1, are continuous. This is not overly restrictive for a characterisation of the equilibrium payoffs, thanks to approximation arguments as those exploited in, e.g., [[TV02](https://arxiv.org/html/2510.15616v1#bib.bibx43)] and [[DAMP22](https://arxiv.org/html/2510.15616v1#bib.bibx12), Sec. 5]; however, we cannot expect, in general, to find equilibrium strategies with continuous paths.

Conditions (iii) and (iv) from the corollary translate into: for i=0,1i=0,1,

|  |  |  |
| --- | --- | --- |
|  | ui​(t,π,x)≤f​(t,x)andv​(t,π,x)≥g​(t,x)for all (t,π,x)∈[0,T]×(0,1)×ℝ.\displaystyle u^{i}(t,\pi,x)\leq f(t,x)\quad\text{and}\quad v(t,\pi,x)\geq g(t,x)\quad\text{for all $(t,\pi,x)\in[0,T]\times(0,1)\times\mathbb{R}$}. |  |

These conditions suggest the players’ stopping regions. In particular, the two incarnations of the informed player should only stop in the regions

|  |  |  |
| --- | --- | --- |
|  | 𝒮i≔{(t,π,x):ui​(t,π,x)=f​(t,x)},i=0,1,\mathcal{S}^{i}\coloneqq\{(t,\pi,x):u^{i}(t,\pi,x)=f(t,x)\},\quad i=0,1, |  |

whereas the uninformed player should stop in the region

|  |  |  |
| --- | --- | --- |
|  | 𝒮≔{(t,π,x):v​(t,π,x)=g​(t,x)}.\mathcal{S}\coloneqq\{(t,\pi,x):v(t,\pi,x)=g(t,x)\}. |  |

Let ℒX,ψ\mathcal{L}\_{X,\psi} be the infinitesimal generator of the pair (Xt,ψt)(X\_{t},\psi\_{t}) defined in ([5.24](https://arxiv.org/html/2510.15616v1#S5.E24 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")). For i=0,1i=0,1, let ℒX,ψi\mathcal{L}^{i}\_{X,\psi} be the infinitesimal generator of the process (Xti,ψt)(X^{i}\_{t},\psi\_{t}). The analytical counterpart of (i) can be deduced by the following equations: for i=0,1i=0,1

|  |  |  |  |
| --- | --- | --- | --- |
| (5.36) |  | ∂tui​(t,π,x)+ℒX,ψi​ui​(t,π,x)≥0,on​{v>g},∂πui​(t,π,x)=0,on 𝒮0∪𝒮1,\displaystyle\begin{aligned} &\partial\_{t}u^{i}(t,\pi,x)+\mathcal{L}^{i}\_{X,\psi}u^{i}(t,\pi,x)\geq 0,\ \ \ \text{on}\ \{v>g\},\\ &\partial\_{\pi}u^{i}(t,\pi,x)=0,\quad\text{on $\mathcal{S}^{0}\cup\mathcal{S}^{1}$},\end{aligned} |  |

which need to be understood in an appropriate sense (e.g., in the viscosity sense) and which we derived using d​ζ^ti=0\mathrm{d}\hat{\zeta}^{i}\_{t}=0 if (t,p^t,Xti)∈{v>g}(t,\hat{p}\_{t},X^{i}\_{t})\in\{v>g\}, due to Corollary [5.7](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem7 "Corollary 5.7. ‣ 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information"). Notice that the first inequality above is the result of the diffusive dynamics of the pair (ψt,Xti)t∈[0,T](\psi\_{t},X^{i}\_{t})\_{t\in[0,T]}, whereas the second condition takes care of the bounded variation component of the optimal dynamics for the belief process (cf. ([5.25](https://arxiv.org/html/2510.15616v1#S5.E25 "In 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information"))). The latter, arises in equilibrium only due to optimal actions of the two incarnations of the informed player. Since there is no action in the set {u0<f}∩{u1<f}\{u^{0}<f\}\cap\{u^{1}<f\}, then d​p^t\mathrm{d}\hat{p}\_{t} is proportional to d​ψt\mathrm{d}\psi\_{t} (i.e., purely diffusive) whenever (t,p^t,Xt)∈{u0<f}∩{u1<f}(t,\hat{p}\_{t},X\_{t})\in\{u^{0}<f\}\cap\{u^{1}<f\}. That is why we need the second equation to hold in 𝒮0∪𝒮1\mathcal{S}^{0}\cup\mathcal{S}^{1} only. In particular, the equation says that the equilibrium payoffs of the two incarnations of the informed player are not affected by (optimal) changes in the belief process of the uninformed player.

Analogous arguments translate condition (ii) into the inequality

|  |  |  |  |
| --- | --- | --- | --- |
| (5.37) |  | ∂tv​(t,π,x)+ℒX,ψ​v​(t,π,x)≤0,on​{u0<f}∩{u1<f}.\displaystyle\partial\_{t}v(t,\pi,x)+\mathcal{L}\_{X,\psi}v(t,\pi,x)\leq 0,\quad\text{on}\ \{u^{0}<f\}\cap\{u^{1}<f\}. |  |

Here we do not need a condition on the derivative ∂πv\partial\_{\pi}v because, as argued above, in equilibrium the belief process (p^t)t∈[0,T](\hat{p}\_{t})\_{t\in[0,T]} of the uninformed player is purely diffusive whenever (t,p^t,Xt)∈{u0<f}∩{u1<f}(t,\hat{p}\_{t},X\_{t})\in\{u^{0}<f\}\cap\{u^{1}<f\}. The martingale characterisation also suggests that both inequalities ([5.36](https://arxiv.org/html/2510.15616v1#S5.E36 "In 5.3. A heuristic derivation of PDE systems ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) and ([5.37](https://arxiv.org/html/2510.15616v1#S5.E37 "In 5.3. A heuristic derivation of PDE systems ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) become strict equalities on the set {u0<f}∩{u1<f}∩{v>g}\{u^{0}<f\}\cap\{u^{1}<f\}\cap\{v>g\}. That is,

|  |  |  |  |
| --- | --- | --- | --- |
| (5.38) |  | ∂tui​(t,π,x)+ℒX,ψi​ui​(t,π,x)=0,∂tv​(t,π,x)+ℒX,ψ​v​(t,π,x)=0,\displaystyle\begin{aligned} \partial\_{t}u^{i}(t,\pi,x)+\mathcal{L}^{i}\_{X,\psi}u^{i}(t,\pi,x)&=0,\\ \partial\_{t}v(t,\pi,x)+\mathcal{L}\_{X,\psi}v(t,\pi,x)&=0,\end{aligned} |  |

for (t,π,x)∈{u0<f}∩{u1<f}∩{v>g}(t,\pi,x)\in\{u^{0}<f\}\cap\{u^{1}<f\}\cap\{v>g\}. Finally, condition (v) in Corollary [5.8](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem8 "Corollary 5.8. ‣ 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") connects the functions u0,u1u^{0},u^{1} and vv via the formula

|  |  |  |
| --- | --- | --- |
|  | v​(t,π,x)=π​u1​(t,π,x)+(1−π)​u0​(t,π,x).v(t,\pi,x)=\pi u^{1}(t,\pi,x)+(1-\pi)u^{0}(t,\pi,x). |  |

Precisely, condition (v) only give the above link for t=0t=0 and given an initial point (π,x)(\pi,x) but due to the Markovian structure of the problem, the game can be started at any time tt and from any configuration (π,x)(\pi,x) justifying the above statement.

Players’ strategies in Corollary [5.8](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem8 "Corollary 5.8. ‣ 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") are defined using maps Ξ0,Ξ1\Xi^{0},\Xi^{1} and Λ\Lambda. These maps are evaluated on ‘wrong’ processes in conditions (i)-(v) in order to imply the saddle point assertion of ([5.35](https://arxiv.org/html/2510.15616v1#S5.E35 "In Corollary 5.8. ‣ 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")). This feature is clearly visible in the equations above. In ([5.36](https://arxiv.org/html/2510.15616v1#S5.E36 "In 5.3. A heuristic derivation of PDE systems ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")), the underlying dynamics is given by XiX^{i} and the inequality must hold on {v>g}\{v>g\}, i.e., on the inaction set for the uninformed player pretending to observe XiX^{i}, hence, when ζ^i\hat{\zeta}^{i} from Corollary [5.8](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem8 "Corollary 5.8. ‣ 5.2. Partially observed dynamics ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") does not grow. Similarly, ([5.37](https://arxiv.org/html/2510.15616v1#S5.E37 "In 5.3. A heuristic derivation of PDE systems ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) holds when neither ξ^0\hat{\xi}^{0} nor ξ^1\hat{\xi}^{1} act.

We conclude by noticing that the system above is precisely the one conjectured in the verification theorem formulated in [[DAEG22](https://arxiv.org/html/2510.15616v1#bib.bibx9)], thus providing the theoretical foundation for such theorem.

Partially observed scenarios. Analogous arguments may be developed in the framework of Section [5.1](https://arxiv.org/html/2510.15616v1#S5.SS1 "5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information"). This is a useful exercise because it leads to a different type of variational problem than the one studied by Grün [[Grü13](https://arxiv.org/html/2510.15616v1#bib.bibx24)] in a Markovian formulation of the game with partially observed scenarios. Indeed, Grün obtains a single variational inequality for the value of the uninformed player whereas we obtain a system of variational inequalities which is close in spirit to those found in the PDE literature on nonzero-sum Dynkin games (e.g., [[BF74](https://arxiv.org/html/2510.15616v1#bib.bibx2)]). This is in line with our overall approach to the study of the problem.

In the framework of Section [5.1](https://arxiv.org/html/2510.15616v1#S5.SS1 "5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") let us now restrict our attention to the case of a diffusive underlying dynamics (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} in ℝd\mathbb{R}^{d} (fully known to both players) with the infinitesimal generator denoted by ℒX\mathcal{L}\_{X}. Assume that there are measurable functions fi,gi,hi:[0,T]×ℝd→ℝf^{i},g^{i},h^{i}:[0,T]\times\mathbb{R}^{d}\to\mathbb{R} such that fti=fi​(t,Xt)f^{i}\_{t}=f^{i}(t,X\_{t}), gti=gi​(t,Xt)g^{i}\_{t}=g^{i}(t,X\_{t}) and hti=hi​(t,Xt)h^{i}\_{t}=h^{i}(t,X\_{t}) for i=0,1i=0,1. Since we are only interested in heuristics, in order to convey the main ideas we postulate again that the generating processes ξ^0\hat{\xi}^{0}, ξ^1\hat{\xi}^{1} and ζ^\hat{\zeta} from Corollary [5.2](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem2 "Corollary 5.2. ‣ 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") are continuous. Recall that p^t\hat{p}\_{t} is defined as in ([5.3](https://arxiv.org/html/2510.15616v1#S5.E3 "In 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information")) but with ξ^\hat{\xi} in place of ξ∗\xi^{\*}.

If we look at equilibrium values as deterministic functions of the state dynamics (p^t,Xt)t∈[0,T](\hat{p}\_{t},X\_{t})\_{t\in[0,T]}, we must determine functions v,u0,u1:[0,T]×[0,1]×ℝd→ℝv,u^{0},u^{1}:[0,T]\times[0,1]\times\mathbb{R}^{d}\to\mathbb{R} such that Vt=v​(t,p^t,Xt)V\_{t}=v(t,\hat{p}\_{t},X\_{t}), Utj=uj​(t,p^t,Xt)U^{j}\_{t}=u^{j}(t,\hat{p}\_{t},X\_{t}), j=0,1j=0,1. Recall that the belief process p^t\hat{p}\_{t} in this framework only moves as a result of the informed player’s stopping strategy in equilibrium. By the assumed continuity of the generating processes, conditions (iii) and (iv) in Corollary [5.2](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem2 "Corollary 5.2. ‣ 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") translate into

|  |  |  |
| --- | --- | --- |
|  | ui​(t,π,x)≤fi​(t,x)andv​(t,π,x)≥π​g1​(t,x)+(1−π)​g0​(t,x),u^{i}(t,\pi,x)\leq f^{i}(t,x)\quad\text{and}\quad v(t,\pi,x)\geq\pi g^{1}(t,x)+(1-\pi)g^{0}(t,x), |  |

for (t,π,x)∈[0,T]×[0,1]×ℝd(t,\pi,x)\in[0,T]\times[0,1]\times\mathbb{R}^{d} and i=0,1i=0,1. The ‘flat-off conditions’ in Corollary [5.1](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem1 "Corollary 5.1. ‣ 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") help us identify the stopping regions for the two players. In particular, we have that the two incarnations of the informed player should stop in the sets

|  |  |  |
| --- | --- | --- |
|  | 𝒮i≔{(t,π,x):ui​(t,π,x)=fi​(t,x)},i=0,1.\mathcal{S}^{i}\coloneqq\{(t,\pi,x):u^{i}(t,\pi,x)=f^{i}(t,x)\},\quad i=0,1. |  |

Instead, the uninformed player should stop in the set

|  |  |  |
| --- | --- | --- |
|  | 𝒮≔{(t,π,x):v​(t,π,x)=π​g1​(t,x)+(1−π)​g0​(t,x)}.\mathcal{S}\coloneqq\{(t,\pi,x):v(t,\pi,x)=\pi g^{1}(t,x)+(1-\pi)g^{0}(t,x)\}. |  |

Denoting 𝒞=([0,T]×[0,1]×ℝd)∖𝒮\mathcal{C}=([0,T]\times[0,1]\times\mathbb{R}^{d})\setminus\mathcal{S}, the submartingale condition (i) in Corollary [5.2](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem2 "Corollary 5.2. ‣ 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") translates into

|  |  |  |
| --- | --- | --- |
|  | ∂tui​(t,π,x)+ℒX​ui​(t,π,x)≥0,on𝒞,\displaystyle\partial\_{t}u^{i}(t,\pi,x)+\mathcal{L}\_{X}u^{i}(t,\pi,x)\geq 0,\ \ \text{on}\ \ \mathcal{C}, |  |
|  |  |  |
| --- | --- | --- |
|  | ∂πui​(t,π,x)=0,on𝒮0∪𝒮1,\displaystyle\partial\_{\pi}u^{i}(t,\pi,x)=0,\ \ \text{on}\ \ \mathcal{S}^{0}\cup\mathcal{S}^{1}, |  |

where the second equation accounts for the fact that a change in the uninformed player’s belief should not affect the informed player’s equilibrium payoff. Analogously, the supermartingale condition in (ii) of Corollary [5.2](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem2 "Corollary 5.2. ‣ 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") reads in analytical terms as

|  |  |  |
| --- | --- | --- |
|  | ∂tv​(t,π,x)+ℒX​v​(t,π,x)≤0on{u0<f0}∩{u1<f1}.\partial\_{t}v(t,\pi,x)+\mathcal{L}\_{X}v(t,\pi,x)\leq 0\ \ \ \ \text{on}\ \ \{u^{0}<f^{0}\}\cap\{u^{1}<f^{1}\}. |  |

Finally, by the martingale characterisation we get

|  |  |  |
| --- | --- | --- |
|  | ∂tui​(t,π,x)+ℒX​ui​(t,π,x)=0and∂tv​(t,π,x)+ℒX​v​(t,π,x)=0,\partial\_{t}u^{i}(t,\pi,x)+\mathcal{L}\_{X}u^{i}(t,\pi,x)=0\ \ \text{and}\ \ \partial\_{t}v(t,\pi,x)+\mathcal{L}\_{X}v(t,\pi,x)=0, |  |

for (t,π,x)∈{u0<f}∩{u1<f}∩𝒞(t,\pi,x)\in\{u^{0}<f\}\cap\{u^{1}<f\}\cap\mathcal{C}, i=0,1i=0,1, and condition (v) in Corollary [5.2](https://arxiv.org/html/2510.15616v1#S5.Thmtheorem2 "Corollary 5.2. ‣ 5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information") reads as

|  |  |  |
| --- | --- | --- |
|  | v​(t,π,x)=π​u1​(t,π,x)+(1−π)​u0​(t,π,x),v(t,\pi,x)=\pi u^{1}(t,\pi,x)+(1-\pi)u^{0}(t,\pi,x), |  |

where, again, we refer to the Markovianity of the framework to allow for arbitrary t,π,xt,\pi,x instead of a fixed initial point in (v).

## Appendix A Review of aggregation results

We recall useful concepts from [[EK81](https://arxiv.org/html/2510.15616v1#bib.bibx20)] (see paragraph 2.11). Throughout the section, 𝔾\mathbb{G} is a filtration of sub-σ\sigma-algebras of ℱ\mathcal{F}, unless otherwise specified.

###### Definition A.1.

A family 𝐗≔{X​(θ),θ∈𝒯0​(𝔾)}{\bf X}\coloneqq\{X(\theta),\theta\in\mathcal{T}\_{0}(\mathbb{G})\} is a 𝒯0​(𝔾)\mathcal{T}\_{0}(\mathbb{G})-system if X​(θ)X(\theta) is 𝒢θ\mathcal{G}\_{\theta}-measurable for every θ∈𝒯0​(𝔾)\theta\in\mathcal{T}\_{0}(\mathbb{G}) and X​(θ1)=X​(θ2)X(\theta\_{1})=X(\theta\_{2}) on {θ1=θ2}\{\theta\_{1}=\theta\_{2}\} for any θ1,θ2∈𝒯0​(𝔾)\theta\_{1},\theta\_{2}\in\mathcal{T}\_{0}(\mathbb{G}).

(a) A 𝒯0​(𝔾)\mathcal{T}\_{0}(\mathbb{G})-system 𝐗{\bf X} is a 𝒯0​(𝔾)\mathcal{T}\_{0}(\mathbb{G})-(super/sub)martingale system if

* (i)

  𝖤​[|X​(θ)|]<∞\mathsf{E}[|X(\theta)|]<\infty for all θ∈𝒯0​(𝔾)\theta\in\mathcal{T}\_{0}(\mathbb{G}),
* (ii)

  For any θ1,θ2∈𝒯0​(𝔾)\theta\_{1},\theta\_{2}\in\mathcal{T}\_{0}(\mathbb{G}) with θ1≤θ2\theta\_{1}\leq\theta\_{2}, it holds

  |  |  |  |
  | --- | --- | --- |
  |  | 𝖤​[X​(θ2)|𝒢θ1]=X​(θ1),𝖯-a.s (for a martingale system)\displaystyle\mathsf{E}[X(\theta\_{2})|\mathcal{G}\_{\theta\_{1}}]=X(\theta\_{1}),\quad\text{$\mathsf{P}$-a.s {(for a martingale system)}} |  |
  |  |  |  |
  | --- | --- | --- |
  |  | 𝖤​[X​(θ2)|𝒢θ1]≤X​(θ1),𝖯-a.s (for a supermartingale system)\displaystyle\mathsf{E}[X(\theta\_{2})|\mathcal{G}\_{\theta\_{1}}]\leq X(\theta\_{1}),\quad\text{$\mathsf{P}$-a.s {(for a supermartingale system)}} |  |
  |  |  |  |
  | --- | --- | --- |
  |  | 𝖤​[X​(θ2)|𝒢θ1]≥X​(θ1),𝖯-a.s (for a submartingale system)\displaystyle\mathsf{E}[X(\theta\_{2})|\mathcal{G}\_{\theta\_{1}}]\geq X(\theta\_{1}),\quad\text{$\mathsf{P}$-a.s {(for a submartingale system)}} |  |

(b) A 𝒯0​(𝔾)\mathcal{T}\_{0}(\mathbb{G})-system 𝐗{\bf X} is right/left-continuous in expectation if for any decreasing/increasing sequence (θn)n∈ℕ⊂𝒯0​(𝔾)(\theta\_{n})\_{n\in\mathbb{N}}\subset\mathcal{T}\_{0}(\mathbb{G}) converging to θ∈𝒯0​(𝔾)\theta\in\mathcal{T}\_{0}(\mathbb{G}) we have

|  |  |  |
| --- | --- | --- |
|  | limn→∞𝖤​[X​(θn)]=𝖤​[X​(θ)].\lim\_{n\to\infty}\mathsf{E}[X(\theta\_{n})]=\mathsf{E}[X(\theta)]. |  |

(c) A 𝒯0​(𝔾)\mathcal{T}\_{0}(\mathbb{G})-system 𝐗{\bf X} is of class (D)(D) if the family {X​(θ),θ∈𝒯0​(𝔾)}\{X(\theta),\theta\in\mathcal{T}\_{0}(\mathbb{G})\} is uniformly integrable.

(d) A 𝔾\mathbb{G}-optional process (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} aggregates the 𝒯0​(𝔾)\mathcal{T}\_{0}(\mathbb{G})-system {X​(θ),θ∈𝒯0​(𝔾)}\{X(\theta),\theta\in\mathcal{T}\_{0}(\mathbb{G})\} if

|  |  |  |
| --- | --- | --- |
|  | 𝖯​(X​(θ)=Xθ)=1,for all θ∈𝒯0​(𝔾).\mathsf{P}(X(\theta)=X\_{\theta})=1,\quad\text{for all $\theta\in\mathcal{T}\_{0}(\mathbb{G})$}. |  |

We are also going to need the following aggregation result which combines [[EK81](https://arxiv.org/html/2510.15616v1#bib.bibx20), Prop. 2.14] and arguments from [[KS98a](https://arxiv.org/html/2510.15616v1#bib.bibx32), Thm. I.3.13].

###### Proposition A.2.

Let 𝐗≔{X​(θ),θ∈𝒯0​(𝔾)}{\bf X}\coloneqq\{X(\theta),\theta\in\mathcal{T}\_{0}(\mathbb{G})\} be a 𝒯0​(𝔾)\mathcal{T}\_{0}(\mathbb{G})-(super/sub)martingale system which is also right-continuous in expectation and of class (D)(D). There exists a càdlàg (super/sub)martingale (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} of class (D)(D) that aggregates 𝐗{\bf X}.

###### Proof.

The proof of [[EK81](https://arxiv.org/html/2510.15616v1#bib.bibx20), Prop. 2.14] can be immediately adapted to the case of a family 𝐗{\bf X} of class (D)(D), yielding a right-continuous super/sub martingale (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} of class (D)(D) that aggregates 𝐗{\bf X}. We apply arguments from [[KS98a](https://arxiv.org/html/2510.15616v1#bib.bibx32), Thm. I.3.13] (which uses Prop. 3.14 therein) to show that the process (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} has càdlàg trajectories with probability 11.
∎

Any martingale system 𝐗{\bf X} of class (D)(D) is trivially continuous in expectation, which leads to a useful corollary.

###### Corollary A.3.

If 𝐗≔{X​(θ),θ∈𝒯0​(𝔾)}{\bf X}\coloneqq\{X(\theta),\theta\in\mathcal{T}\_{0}(\mathbb{G})\} is a 𝒯0​(𝔾)\mathcal{T}\_{0}(\mathbb{G})-martingale system of class (D)(D), then there exists a càdlàg martingale (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} of class (D)(D) that aggregates 𝐗{\bf X}.

Finally, we recall a standard result from martingale theory.

###### Lemma A.4.

A 𝒯0​(𝔾)\mathcal{T}\_{0}(\mathbb{G})-system 𝐗{\bf X} is a supermartingale system if and only if

|  |  |  |  |
| --- | --- | --- | --- |
| (A.1) |  | 𝖤​[X​(τ)]≤𝖤​[X​(σ)],for every pair τ,σ∈𝒯0​(𝔾), τ≥σ.\displaystyle\mathsf{E}[X(\tau)]\leq\mathsf{E}[X(\sigma)],\quad\text{for every pair $\tau,\sigma\in\mathcal{T}\_{0}(\mathbb{G})$, $\tau\geq\sigma$}. |  |

Moreover, 𝐗{\bf X} is a martingale system if and only if ([A.1](https://arxiv.org/html/2510.15616v1#A1.E1 "In Lemma A.4. ‣ Appendix A Review of aggregation results ‣ Martingale theory for Dynkin games with asymmetric information")) holds with equality.

###### Proof.

The only if part of the claim is obvious. Now assume ([A.1](https://arxiv.org/html/2510.15616v1#A1.E1 "In Lemma A.4. ‣ Appendix A Review of aggregation results ‣ Martingale theory for Dynkin games with asymmetric information")) holds. Take σ,τ∈𝒯0​(𝔾)\sigma,\tau\in\mathcal{T}\_{0}(\mathbb{G}) with σ≤τ\sigma\leq\tau and A∈𝒢σA\in\mathcal{G}\_{\sigma}. Set θ=σ​𝟏A+τ​𝟏Ac\theta=\sigma\mathbf{1}\_{A}+\tau\mathbf{1}\_{A^{c}} so that θ∈𝒯0​(𝔾)\theta\in\mathcal{T}\_{0}(\mathbb{G}) with σ≤θ≤τ\sigma\leq\theta\leq\tau. By ([A.1](https://arxiv.org/html/2510.15616v1#A1.E1 "In Lemma A.4. ‣ Appendix A Review of aggregation results ‣ Martingale theory for Dynkin games with asymmetric information")) and the fact that 𝐗{\bf X} is a 𝒯0​(𝔾)\mathcal{T}\_{0}(\mathbb{G})-system we have

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[X​(τ)]≤𝖤​[X​(θ)]=𝖤​[X​(σ)​𝟏A+X​(τ)​𝟏Ac]⟹𝖤​[𝖤​[X​(τ)|𝒢σ]​1A]=𝖤​[X​(τ)​1A]≤𝖤​[X​(σ)​1A].\mathsf{E}[X(\tau)]\leq\mathsf{E}[X(\theta)]=\mathsf{E}[X(\sigma)\mathbf{1}\_{A}+X(\tau)\mathbf{1}\_{A^{c}}]\implies\mathsf{E}[\mathsf{E}[X(\tau)|\mathcal{G}\_{\sigma}]1\_{A}]=\mathsf{E}[X(\tau)1\_{A}]\leq\mathsf{E}[X(\sigma)1\_{A}]. |  |

By the arbitrariness of A∈𝒢σA\in\mathcal{G}\_{\sigma} we conclude that 𝖤​[X​(τ)|𝒢σ]≤X​(σ)\mathsf{E}[X(\tau)|\mathcal{G}\_{\sigma}]\leq X(\sigma).
∎

## Appendix B Upward and downward directed families

We recall that a family of non-negative random variables Υ\Upsilon is closed under pairwise maximisation if X,Y∈Υ⟹X∨Y∈ΥX,Y\in\Upsilon\implies X\vee Y\in\Upsilon. This also implies that the family is upward-directed, i.e., X,Y∈Υ⟹∃Z∈ΥX,Y\in\Upsilon\implies\exists Z\in\Upsilon such that Z≥X∨YZ\geq X\vee Y – we use the two notions interchangeably. If the family Υ\Upsilon is closed under pairwise maximisation, then ess​sup⁡{X:X∈Υ}=limn→∞Xn\operatorname\*{ess\,sup}\{X:X\in\Upsilon\}=\lim\_{n\to\infty}X\_{n}, where (Xn)n∈ℕ⊂Υ(X\_{n})\_{n\in\mathbb{N}}\subset\Upsilon is a non-decreasing sequence, see [[KS98b](https://arxiv.org/html/2510.15616v1#bib.bibx33), Thm. A.3]. Clearly the property extends to families of random variables bounded from below by a real-valued random variable. An analogue definition for downward-directed families holds in the case of random variables bounded from above.

Given a 𝒯0​(𝔾)\mathcal{T}\_{0}(\mathbb{G})-system 𝐗={X​(θ),θ∈𝒯0​(𝔾)}{\bf X}=\{X(\theta),\theta\in\mathcal{T}\_{0}(\mathbb{G})\} satisfying 𝖤​[ess​supθ∈𝒯0​(𝔾)⁡|X​(θ)|]<∞\mathsf{E}[\operatorname\*{ess\,sup}\_{\theta\in\mathcal{T}\_{0}(\mathbb{G})}|X(\theta)|]<\infty and a filtration ℍ⊂𝔾\mathbb{H}\subset\mathbb{G}, fix an arbitrary σ∈𝒯0​(ℍ)\sigma\in\mathcal{T}\_{0}(\mathbb{H}). It is a well-known fact in the optimal stopping theory that
the family

|  |  |  |
| --- | --- | --- |
|  | {𝖤​[X​(τ)|ℋσ],τ∈𝒯σ​(𝔾)}\big\{\mathsf{E}[X(\tau)|\mathcal{H}\_{\sigma}],\tau\in\mathcal{T}\_{\sigma}(\mathbb{G})\big\} |  |

is both upward-directed and downward-directed. Therefore, there are sequences (τn)n∈ℕ,(τk)k∈ℕ⊂𝒯σ​(𝔾)(\tau\_{n})\_{n\in\mathbb{N}},(\tau^{k})\_{k\in\mathbb{N}}\subset\mathcal{T}\_{\sigma}(\mathbb{G}) such that

|  |  |  |  |
| --- | --- | --- | --- |
| (B.1) |  | ess​infτ∈𝒯σ​(𝔾)⁡𝖤​[X​(τ)|ℋσ]=limn→∞𝖤​[X​(τn)|ℋσ]andess​supτ∈𝒯σ​(𝔾)⁡𝖤​[X​(τ)|ℋσ]=limk→∞𝖤​[X​(τk)|ℋσ],\displaystyle\begin{aligned} \operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\sigma}(\mathbb{G})}\mathsf{E}[X(\tau)|\mathcal{H}\_{\sigma}]=\lim\_{n\to\infty}\mathsf{E}[X(\tau\_{n})|\mathcal{H}\_{\sigma}]\quad\text{and}\quad\operatorname\*{ess\,sup}\_{\tau\in\mathcal{T}\_{\sigma}(\mathbb{G})}\mathsf{E}[X(\tau)|\mathcal{H}\_{\sigma}]=\lim\_{k\to\infty}\mathsf{E}[X(\tau^{k})|\mathcal{H}\_{\sigma}],\end{aligned} |  |

with both limits being monotone, the first one from above and the second one from below.

As a consequence, for any ρ≤σ\rho\leq\sigma, ρ,σ∈𝒯0​(ℍ)\rho,\sigma\in\mathcal{T}\_{0}(\mathbb{H}) we have by the monotone convergence theorem and the tower property of conditional expectation

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[ess​infτ∈𝒯σ​(𝔾)⁡𝖤​[X​(τ)|ℋσ]|ℋρ]=limn→∞𝖤​[X​(τn)|ℋρ]≥ess​infτ∈𝒯σ​(𝔾)⁡𝖤​[X​(τ)|ℋρ].\displaystyle\mathsf{E}\big[\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\sigma}(\mathbb{G})}\mathsf{E}[X(\tau)|\mathcal{H}\_{\sigma}]\big|\mathcal{H}\_{\rho}\big]=\lim\_{n\to\infty}\mathsf{E}[X(\tau\_{n})|\mathcal{H}\_{\rho}]\geq\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\sigma}(\mathbb{G})}\mathsf{E}[X(\tau)|\mathcal{H}\_{\rho}]. |  |

That, combined with the obvious inequality

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[ess​infτ∈𝒯σ​(𝔾)⁡𝖤​[X​(τ)|ℋσ]|ℋρ]≤ess​infτ∈𝒯σ​(𝔾)⁡𝖤​[X​(τ)|ℋρ],\mathsf{E}\big[\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\sigma}(\mathbb{G})}\mathsf{E}[X(\tau)|\mathcal{H}\_{\sigma}]\big|\mathcal{H}\_{\rho}\big]\leq\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\sigma}(\mathbb{G})}\mathsf{E}[X(\tau)|\mathcal{H}\_{\rho}], |  |

yields

|  |  |  |  |
| --- | --- | --- | --- |
| (B.2) |  | 𝖤​[ess​infτ∈𝒯σ​(𝔾)⁡𝖤​[X​(τ)|ℋσ]|ℋρ]=ess​infτ∈𝒯σ​(𝔾)⁡𝖤​[X​(τ)|ℋρ],𝖤​[ess​supτ∈𝒯σ​(𝔾)⁡𝖤​[X​(τ)|ℋσ]|ℋρ]=ess​supτ∈𝒯σ​(𝔾)⁡𝖤​[X​(τ)|ℋρ],\displaystyle\begin{aligned} &\mathsf{E}\big[\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\sigma}({\mathbb{G}})}\mathsf{E}[X(\tau)|\mathcal{H}\_{\sigma}]\big|\mathcal{H}\_{\rho}\big]=\operatorname\*{ess\,inf}\_{\tau\in\mathcal{T}\_{\sigma}({\mathbb{G}})}\mathsf{E}[X(\tau)|\mathcal{H}\_{\rho}],\\ &\mathsf{E}\big[\operatorname\*{ess\,sup}\_{\tau\in\mathcal{T}\_{\sigma}({\mathbb{G}})}\mathsf{E}[X(\tau)|\mathcal{H}\_{\sigma}]\big|\mathcal{H}\_{\rho}\big]=\operatorname\*{ess\,sup}\_{\tau\in\mathcal{T}\_{\sigma}({\mathbb{G}})}\mathsf{E}[X(\tau)|\mathcal{H}\_{\rho}],\end{aligned} |  |

where the second equality is obtained by analogous arguments as the first.

## Appendix C Remaining proofs

### C.1. Proof of Lemma [3.1](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem1 "Lemma 3.1. ‣ 3.1. Aggregation of the equilibrium dynamics ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")

Given ξ1,ξ2∈𝒜θ∘​(𝔽1)\xi^{1},\xi^{2}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1}) we want to show that there is ξ3∈𝒜θ∘​(𝔽1)\xi^{3}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1}) such that JΠθ∗,1​(ξ3,ζ∗;θ|ℱθ1)=min⁡{JΠθ∗,1​(ξ1,ζ∗;θ|ℱθ1),JΠθ∗,1​(ξ2,ζ∗;θ|ℱθ1)}J^{\Pi^{\*,1}\_{\theta}}(\xi^{3},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})=\min\{J^{\Pi^{\*,1}\_{\theta}}(\xi^{1},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta}),J^{\Pi^{\*,1}\_{\theta}}(\xi^{2},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})\}. From ([2.10](https://arxiv.org/html/2510.15616v1#S2.E10 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information")) we know that

|  |  |  |
| --- | --- | --- |
|  | A≔{ω∈Ω:JΠθ∗,1​(ξ1,ζ∗;θ|ℱθ1)​(ω)≤JΠθ∗,1​(ξ2,ζ∗;θ|ℱθ1)​(ω)}∈ℱθ1.A\coloneqq\{\omega\in\Omega:J^{\Pi^{\*,1}\_{\theta}}(\xi^{1},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})(\omega)\leq J^{\Pi^{\*,1}\_{\theta}}(\xi^{2},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})(\omega)\}\in\mathcal{F}^{1}\_{\theta}. |  |

Define ξθ−3=0\xi^{3}\_{\theta-}=0 and ξt3≔ξt1​1A+ξt2​𝟏Ac\xi^{3}\_{t}\coloneqq\xi^{1}\_{t}1\_{A}+\xi^{2}\_{t}\mathbf{1}\_{A^{c}} for t∈[θ,T]t\in[\theta,T]. It is easy to check that ξ3∈𝒜θ∘​(𝔽1)\xi^{3}\in\mathcal{A}^{\raise 1.0pt\hbox{${\scriptstyle\circ}$}}\_{\theta}(\mathbb{F}^{1}) and using ([2.10](https://arxiv.org/html/2510.15616v1#S2.E10 "In 2.1. Players’ subjective views and equilibrium values as families of random variables ‣ 2. Setting and preliminaries ‣ Martingale theory for Dynkin games with asymmetric information"))

|  |  |  |
| --- | --- | --- |
|  | JΠθ∗,1​(ξ3,ζ∗;θ|ℱθ1)=𝖤Πθ∗,1​[∫[θ,T)ft​(1−ζt∗;θ)​dξt3+∫[θ,T)gt​(1−ξt3)​dζt∗;θ+∑t∈[θ,T]ht​Δ​ζt∗;θ​Δ​ξt3|ℱθ1]=1A​𝖤Πθ∗,1​[∫[θ,T)ft​(1−ζt∗;θ)​dξt1+∫[θ,T)gt​(1−ξt1)​dζt∗;θ+∑t∈[θ,T]ht​Δ​ζt∗;θ​Δ​ξt1|ℱθ1]+𝟏Ac​𝖤Πθ∗,1​[∫[θ,T)ft​(1−ζt∗;θ)​dξt2+∫[θ,T)gt​(1−ξt2)​dζt∗;θ+∑t∈[θ,T]ht​Δ​ζt∗;θ​Δ​ξt2|ℱθ1]=1A​JΠθ∗,1​(ξ1,ζ∗;θ|ℱθ1)+𝟏Ac​JΠθ∗,1​(ξ2,ζ∗;θ|ℱθ1)=min⁡{JΠθ∗,1​(ξ1,ζ∗;θ|ℱθ1),JΠθ∗,1​(ξ2,ζ∗;θ|ℱθ1)}.\displaystyle\begin{aligned} J^{\Pi^{\*,1}\_{\theta}}(\xi^{3},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})&=\mathsf{E}^{\Pi^{\*,1}\_{\theta}}\Big[\int\_{[\theta,T)}f\_{t}(1-\zeta^{\*;\theta}\_{t})\mathrm{d}\xi^{3}\_{t}+\int\_{[\theta,T)}g\_{t}(1-\xi^{3}\_{t})\mathrm{d}\zeta^{\*;\theta}\_{t}+\sum\_{t\in[\theta,T]}h\_{t}\Delta\zeta^{\*;\theta}\_{t}\Delta\xi^{3}\_{t}\Big|\mathcal{F}^{1}\_{\theta}\Big]\\ &=1\_{A}\mathsf{E}^{\Pi^{\*,1}\_{\theta}}\Big[\int\_{[\theta,T)}f\_{t}(1-\zeta^{\*;\theta}\_{t})\mathrm{d}\xi^{1}\_{t}+\int\_{[\theta,T)}g\_{t}(1-\xi^{1}\_{t})\mathrm{d}\zeta^{\*;\theta}\_{t}+\sum\_{t\in[\theta,T]}h\_{t}\Delta\zeta^{\*;\theta}\_{t}\Delta\xi^{1}\_{t}\Big|\mathcal{F}^{1}\_{\theta}\Big]\\ &\quad+\mathbf{1}\_{A^{c}}\mathsf{E}^{\Pi^{\*,1}\_{\theta}}\Big[\int\_{[\theta,T)}f\_{t}(1-\zeta^{\*;\theta}\_{t})\mathrm{d}\xi^{2}\_{t}+\int\_{[\theta,T)}g\_{t}(1-\xi^{2}\_{t})\mathrm{d}\zeta^{\*;\theta}\_{t}+\sum\_{t\in[\theta,T]}h\_{t}\Delta\zeta^{\*;\theta}\_{t}\Delta\xi^{2}\_{t}\Big|\mathcal{F}^{1}\_{\theta}\Big]\\ &=1\_{A}J^{\Pi^{\*,1}\_{\theta}}(\xi^{1},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})+\mathbf{1}\_{A^{c}}J^{\Pi^{\*,1}\_{\theta}}(\xi^{2},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})\\ &=\min\{J^{\Pi^{\*,1}\_{\theta}}(\xi^{1},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta}),J^{\Pi^{\*,1}\_{\theta}}(\xi^{2},\zeta^{\*;\theta}|\mathcal{F}^{1}\_{\theta})\}.\end{aligned} |  |

That proves that the family is downward-directed. Hence, there is a minimising sequence using similar arguments as in Section [B](https://arxiv.org/html/2510.15616v1#A2 "Appendix B Upward and downward directed families ‣ Martingale theory for Dynkin games with asymmetric information").

The second part of the lemma is analogous. □\square

### C.2. Proof of Proposition [3.14](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem14 "Proposition 3.14. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information")

The proof requires the following auxiliary measurability result.

###### Lemma C.1.

Let X:[0,1]×Ω→ℝX:[0,1]\times\Omega\to\mathbb{R} be ℬ​([0,1])×ℱ\mathcal{B}([0,1])\times\mathcal{F}-measurable, either right- or left-continuous in the first variable and satisfying the integrability condition 𝖤​[supz∈[0,1]|Xz|]<∞\mathsf{E}[\sup\_{z\in[0,1]}|X\_{z}|]<\infty.

For any complete σ\sigma-algebra 𝒢⊆ℱ\mathcal{G}\subseteq\mathcal{F}, the process {𝖤​[Xz|𝒢],z∈[0,1]}\{\mathsf{E}[X\_{z}|\mathcal{G}],\ z\in[0,1]\} admits a ℬ​([0,1])×𝒢\mathcal{B}([0,1])\times\mathcal{G}-measurable modification, in the sense that there is a ℬ​([0,1])×𝒢\mathcal{B}([0,1])\times\mathcal{G}-measurable function YY such that, for each z∈[0,1]z\in[0,1],

|  |  |  |
| --- | --- | --- |
|  | Yz=𝖤​[Xz|𝒢],𝖯−a.s.Y\_{z}=\mathsf{E}[X\_{z}|\mathcal{G}],\quad\mathsf{P}-a.s. |  |

###### Proof.

Assume that z↦Xzz\mapsto X\_{z} is right-continuous. Let us define

|  |  |  |
| --- | --- | --- |
|  | Yzn≔∑k=02n−1𝟏[k2n,k+12n)​(z)​𝖤​[Xk+12n|𝒢]+𝟏{1}​(z)​𝖤​[X1|𝒢].Y^{n}\_{z}\coloneqq\sum\_{k=0}^{2^{n}-1}\mathbf{1}\_{[\frac{k}{2^{n}},\frac{k+1}{2^{n}})}(z)\mathsf{E}[X\_{\frac{k+1}{2^{n}}}|\mathcal{G}]+\mathbf{1}\_{\{1\}}(z)\mathsf{E}[X\_{1}|\mathcal{G}]. |  |

It is clear that Yzn​(ω)Y^{n}\_{z}(\omega) is uniquely defined for all (z,ω)∈[0,1]×Ωn(z,\omega)\in[0,1]\times\Omega\_{n}, for some Ωn∈ℱ\Omega\_{n}\in\mathcal{F} with 𝖯​(Ωn)=1\mathsf{P}(\Omega\_{n})=1. Letting Ω0≔∩n∈ℕΩn\Omega\_{0}\coloneqq\cap\_{n\in\mathbb{N}}\Omega\_{n}, the sequence {Yzn​(ω),n∈ℕ}\{Y^{n}\_{z}(\omega),n\in\mathbb{N}\} is defined for all (z,ω)∈[0,1]×Ω0(z,\omega)\in[0,1]\times\Omega\_{0} and 𝖯​(Ω0)=1\mathsf{P}(\Omega\_{0})=1. Moreover, for any a∈ℝa\in\mathbb{R}

|  |  |  |
| --- | --- | --- |
|  | {(z,ω):Yzn​(ω)>a}=⋃k=02n[k2n,k+12n)×{ω:𝖤​[Xk+12n|𝒢]​(ω)>a}∈ℬ​([0,1])×𝒢.\displaystyle\{(z,\omega):Y^{n}\_{z}(\omega)>a\}=\bigcup\_{k=0}^{2^{n}}\big[\tfrac{k}{2^{n}},\tfrac{k+1}{2^{n}}\big)\times\{\omega:\mathsf{E}[X\_{\frac{k+1}{2^{n}}}|\mathcal{G}](\omega)>a\}\in\mathcal{B}([0,1])\times\mathcal{G}. |  |

Defining Yz+​(ω)≔lim supn→∞Yzn​(ω)Y^{+}\_{z}(\omega)\coloneqq\limsup\_{n\to\infty}Y^{n}\_{z}(\omega) and Yz−​(ω)≔lim infn→∞Yzn​(ω)Y^{-}\_{z}(\omega)\coloneqq\liminf\_{n\to\infty}Y^{n}\_{z}(\omega) for (z,ω)∈[0,1]×Ω0(z,\omega)\in[0,1]\times\Omega\_{0}, it is clear that Y±Y^{\pm} is ℬ​([0,1])×𝒢\mathcal{B}([0,1])\times\mathcal{G}-measurable. It remains to show that for each z∈[0,1]z\in[0,1], Yz+=Yz−=𝖤​[Xz|𝒢]Y^{+}\_{z}=Y^{-}\_{z}=\mathsf{E}[X\_{z}|\mathcal{G}], 𝖯\mathsf{P}-a.s.

For every z∈[0,1]z\in[0,1],

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Yzn−𝖤[Xz|𝒢]|\displaystyle\big|Y^{n}\_{z}-\mathsf{E}[X\_{z}|\mathcal{G}]\big| | =|∑k=02n−1𝖤[Xk+12n−Xz|𝒢]𝟏[k2n,k+12n)(z)|≤𝖤[sup0≤λ≤1/2n|X(z+λ)∧1−Xz||𝒢].\displaystyle=\Big|\sum\_{k=0}^{2^{n}-1}\mathsf{E}\big[X\_{\frac{k+1}{2^{n}}}-X\_{z}\big|\mathcal{G}\big]\mathbf{1}\_{[\frac{k}{2^{n}},\frac{k+1}{2^{n}})}(z)\Big|\leq\mathsf{E}\big[\sup\_{0\leq\lambda\leq 1/2^{n}}\big|X\_{(z+\lambda)\wedge 1}-X\_{z}\big|\big|\mathcal{G}\big]. |  |

Let n→∞n\to\infty. By the right continuity of XzX\_{z} we have

|  |  |  |
| --- | --- | --- |
|  | limn→∞sup0≤λ≤1/2n|X(z+λ)∧1​(ω)−Xz​(ω)|=0,for all ω∈Ω.\lim\_{n\to\infty}\sup\_{0\leq\lambda\leq 1/2^{n}}\big|X\_{(z+\lambda)\wedge 1}(\omega)-X\_{z}(\omega)\big|=0,\quad\text{for all $\omega\in\Omega$}. |  |

Thanks to boundedness of XzX\_{z} we can use the conditional version of the Dominated Convergence Theorem to pass the limit inside expectation. Thus,

|  |  |  |
| --- | --- | --- |
|  | limn→∞|Yzn−𝖤[Xz|𝒢]|=0,𝖯−a.s.\lim\_{n\to\infty}\big|Y^{n}\_{z}-\mathsf{E}[X\_{z}|\mathcal{G}]\big|=0,\quad\mathsf{P}-a.s. |  |

The latter implies Yz+=Yz−=𝖤​[Xz|𝒢]Y^{+}\_{z}=Y^{-}\_{z}=\mathsf{E}[X\_{z}|\mathcal{G}], 𝖯\mathsf{P}-a.s., as needed. Then, setting Yz​(ω)≔Yz+​(ω)Y\_{z}(\omega)\coloneqq Y^{+}\_{z}(\omega) for (z,ω)∈[0,1]×Ω0(z,\omega)\in[0,1]\times\Omega\_{0} and Yz​(ω)=0Y\_{z}(\omega)=0 for (z,ω)∈[0,1]×(Ω∖Ω0)(z,\omega)\in[0,1]\times(\Omega\setminus\Omega\_{0}) concludes the proof because 𝖯​(Ω∖Ω0)=0\mathsf{P}(\Omega\setminus\Omega\_{0})=0 and 𝒢\mathcal{G} is complete.

If z↦Xzz\mapsto X\_{z} is left-continuous, the same proof as above but with

|  |  |  |
| --- | --- | --- |
|  | Yzn≔𝟏0​(z)​𝖤​[X0|𝒢]+∑k=02n−1𝟏(k2n,k+12n]​(z)​𝖤​[Xk2n|𝒢]Y^{n}\_{z}\coloneqq\mathbf{1}\_{0}(z)\mathsf{E}[X\_{0}|\mathcal{G}]+\sum\_{k=0}^{2^{n}-1}\mathbf{1}\_{(\frac{k}{2^{n}},\frac{k+1}{2^{n}}]}(z)\mathsf{E}[X\_{\frac{k}{2^{n}}}|\mathcal{G}] |  |

yields the desired result.
∎

###### Proof of Proposition [3.14](https://arxiv.org/html/2510.15616v1#S3.Thmtheorem14 "Proposition 3.14. ‣ 3.4. Structure of optimal strategies ‣ 3. Necessary conditions for a saddle point ‣ Martingale theory for Dynkin games with asymmetric information").

We only show the full argument for Mθ∗M^{\*}\_{\theta} and m∗​(θ;z)m^{\*}(\theta;z) as the one for Nγ∗N^{\*}\_{\gamma} and n∗​(γ;z)n^{\*}(\gamma;z) is analogous.
In the proof, when we refer to joint measurability in (z,ω)(z,\omega), without further specifying, we mean the measurability with respect to the σ\sigma-algebra ℬ​([0,1])×ℱθ1\mathcal{B}([0,1])\times\mathcal{F}^{1}\_{\theta} (notice that ℱθ1\mathcal{F}^{1}\_{\theta} is complete as required by Lemma [C.1](https://arxiv.org/html/2510.15616v1#A3.Thmtheorem1 "Lemma C.1. ‣ C.2. Proof of Proposition 3.14 ‣ Appendix C Remaining proofs ‣ Martingale theory for Dynkin games with asymmetric information")).

It is clear that the term 𝟏{θ≤τ∗​(z)}​V^θ∗,1\mathbf{1}\_{\{\theta\leq\tau\_{\*}(z)\}}\hat{V}^{\*,1}\_{\theta} is jointly measurable in (z,ω)(z,\omega) by the measurability of τ∗​(z)\tau\_{\*}(z). Observe that z↦τ∗​(z)z\mapsto\tau\_{\*}(z) is non-decreasing and right continuous (cf., [[RY99](https://arxiv.org/html/2510.15616v1#bib.bibx40), Ch. 0, Lemma 4.8]). Since 𝟏{τ∗​(z)<θ}​fτ∗​(z)​𝟏{τ∗​(z)<σ∗}\mathbf{1}\_{\{\tau\_{\*}(z)<\theta\}}f\_{\tau\_{\*}(z)}\mathbf{1}\_{\{\tau\_{\*}(z)<\sigma\_{\*}\}} is ℬ​([0,1])×ℱ\mathcal{B}([0,1])\times\mathcal{F}-measurable and right-continuous with respect to zz, Lemma [C.1](https://arxiv.org/html/2510.15616v1#A3.Thmtheorem1 "Lemma C.1. ‣ C.2. Proof of Proposition 3.14 ‣ Appendix C Remaining proofs ‣ Martingale theory for Dynkin games with asymmetric information") yields that the conditional expectation

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[𝟏{τ∗​(z)<θ}​fτ∗​(z)​𝟏{τ∗​(z)<σ∗}|ℱθ1]​(ω)\mathsf{E}\Big[\mathbf{1}\_{\{\tau\_{\*}(z)<\theta\}}f\_{\tau\_{\*}(z)}\mathbf{1}\_{\{\tau\_{\*}(z)<\sigma\_{\*}\}}\Big|\mathcal{F}^{1}\_{\theta}\Big](\omega) |  |

admits a jointly (z,ω)(z,\omega)-measurable modification mθ1​(z,ω)m^{1}\_{\theta}(z,\omega). The map (z,ω)↦𝟏{σ∗<θ}​𝟏{σ∗<τ∗​(z)}​gσ∗(z,\omega)\mapsto\mathbf{1}\_{\{\sigma\_{\*}<\theta\}}\mathbf{1}\_{\{\sigma\_{\*}<\tau\_{\*}(z)\}}g\_{\sigma\_{\*}} is ℬ​([0,1])×ℱ\mathcal{B}([0,1])\times\mathcal{F}-measurable but neither left nor right-continuous with respect to zz. However, {σ∗<τ∗​(z)}=⋂ϵ>0{σ∗+ϵ≤τ∗​(z)}\{\sigma\_{\*}<\tau\_{\*}(z)\}=\bigcap\_{\epsilon>0}\{\sigma\_{\*}+\epsilon\leq\tau\_{\*}(z)\} and 𝟏{σ∗+ϵ≤τ∗​(z)}\mathbf{1}\_{\{\sigma\_{\*}+\epsilon\leq\tau\_{\*}(z)\}} is right-continuous in zz, so using Lemma [C.1](https://arxiv.org/html/2510.15616v1#A3.Thmtheorem1 "Lemma C.1. ‣ C.2. Proof of Proposition 3.14 ‣ Appendix C Remaining proofs ‣ Martingale theory for Dynkin games with asymmetric information") again, we have that

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[𝟏{σ∗<θ}​𝟏{σ∗+ϵ≤τ∗​(z)}​gσ∗|ℱθ1]\mathsf{E}\Big[\mathbf{1}\_{\{\sigma\_{\*}<\theta\}}\mathbf{1}\_{\{\sigma\_{\*}+\epsilon\leq\tau\_{\*}(z)\}}g\_{\sigma\_{\*}}\Big|\mathcal{F}^{1}\_{\theta}\Big] |  |

admits a jointly (z,ω)(z,\omega)-measurable modification mθ2,ε​(z,ω)m^{2,\varepsilon}\_{\theta}(z,\omega). The dominated convergence theorem yields

|  |  |  |  |
| --- | --- | --- | --- |
| (C.1) |  | 𝖤​[𝟏{σ∗<θ}​𝟏{σ∗<τ∗​(z)}​gσ∗|ℱθ1]=limϵ↓0𝖤​[𝟏{σ∗<θ}​𝟏{σ∗+ϵ≤τ∗​(z)}​gσ∗|ℱθ1].\mathsf{E}\Big[\mathbf{1}\_{\{\sigma\_{\*}<\theta\}}\mathbf{1}\_{\{\sigma\_{\*}<\tau\_{\*}(z)\}}g\_{\sigma\_{\*}}\Big|\mathcal{F}^{1}\_{\theta}\Big]=\lim\_{\epsilon\downarrow 0}\mathsf{E}\Big[\mathbf{1}\_{\{\sigma\_{\*}<\theta\}}\mathbf{1}\_{\{\sigma\_{\*}+\epsilon\leq\tau\_{\*}(z)\}}g\_{\sigma\_{\*}}\Big|\mathcal{F}^{1}\_{\theta}\Big]. |  |

Thus, the limit mθ2​(z,ω)≔limε→0mθ2,ε​(z,ω)m^{2}\_{\theta}(z,\omega)\coloneqq\lim\_{\varepsilon\to 0}m^{2,\varepsilon}\_{\theta}(z,\omega) exists and it is a jointly (z,ω)(z,\omega)-measurable modification of the expression on the left-hand side of ([C.1](https://arxiv.org/html/2510.15616v1#A3.E1 "In C.2. Proof of Proposition 3.14 ‣ Appendix C Remaining proofs ‣ Martingale theory for Dynkin games with asymmetric information")), as a pointwise limit of measurable functions. Finally, we notice that

|  |  |  |
| --- | --- | --- |
|  | 𝟏{τ∗​(z)<θ}​𝖤​[hτ∗​(z)​𝟏{τ∗​(z)=σ∗}|ℱθ1]=𝟏{τ∗​(z)<θ}​(𝖤​[hσ∗​𝟏{τ∗​(z)≥σ∗}|ℱθ1]−𝖤​[hσ∗​𝟏{τ∗​(z)>σ∗}|ℱθ1]),\mathbf{1}\_{\{\tau\_{\*}(z)<\theta\}}\mathsf{E}\Big[h\_{\tau\_{\*}(z)}\mathbf{1}\_{\{\tau\_{\*}(z)=\sigma\_{\*}\}}\Big|\mathcal{F}^{1}\_{\theta}\Big]=\mathbf{1}\_{\{\tau\_{\*}(z)<\theta\}}\Big(\mathsf{E}\Big[h\_{\sigma\_{\*}}\mathbf{1}\_{\{\tau\_{\*}(z)\geq\sigma\_{\*}\}}\Big|\mathcal{F}^{1}\_{\theta}\Big]-\mathsf{E}\Big[h\_{\sigma\_{\*}}\mathbf{1}\_{\{\tau\_{\*}(z)>\sigma\_{\*}\}}\Big|\mathcal{F}^{1}\_{\theta}\Big]\Big), |  |

and each one of the two terms on the right-hand side admits a jointly (z,ω)(z,\omega)-measurable modification by Lemma [C.1](https://arxiv.org/html/2510.15616v1#A3.Thmtheorem1 "Lemma C.1. ‣ C.2. Proof of Proposition 3.14 ‣ Appendix C Remaining proofs ‣ Martingale theory for Dynkin games with asymmetric information") and the arguments above.

Combining the results from the paragraph we obtain existence of the jointly measurable modification (z,ω)↦m∗​(θ;z)​(ω)(z,\omega)\mapsto m^{\*}(\theta;z)(\omega) for

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[𝟏{τ∗​(z)<θ}​(fτ∗​(z)​𝟏{τ∗​(z)<σ∗}+hτ∗​(z)​𝟏{τ∗​(z)=σ∗})+𝟏{σ∗<θ}​𝟏{σ∗<τ∗​(z)}​gσ∗|ℱθ1]+𝟏{θ≤τ∗​(z)}​V^θ∗,1.\mathsf{E}\Big[\mathbf{1}\_{\{\tau\_{\*}(z)<\theta\}}\Big(f\_{\tau\_{\*}(z)}\mathbf{1}\_{\{\tau\_{\*}(z)<\sigma\_{\*}\}}+h\_{\tau\_{\*}(z)}\mathbf{1}\_{\{\tau\_{\*}(z)=\sigma\_{\*}\}}\Big)+\mathbf{1}\_{\{\sigma\_{\*}<\theta\}}\mathbf{1}\_{\{\sigma\_{\*}<\tau\_{\*}(z)\}}g\_{\sigma\_{\*}}\Big|\mathcal{F}^{1}\_{\theta}\Big]+\mathbf{1}\_{\{\theta\leq\tau\_{\*}(z)\}}\hat{V}^{\*,1}\_{\theta}. |  |

This proves the measurability of functions m∗​(θ;⋅)m^{\*}(\theta;\cdot) and n∗​(γ;⋅)n^{\*}(\gamma;\cdot) in (ii).

In order to justify (i), it is sufficient to show that 𝖤​[𝟏A​Mθ∗]=𝖤​[𝟏A​∫01m∗​(θ;z)​𝑑z]\mathsf{E}[\mathbf{1}\_{A}M^{\*}\_{\theta}]=\mathsf{E}\big[\mathbf{1}\_{A}\int\_{0}^{1}m^{\*}(\theta;z)dz\big] for A∈ℱθ1A\in\mathcal{F}^{1}\_{\theta}. Take an arbitrary A∈ℱθ1A\in\mathcal{F}^{1}\_{\theta} and write

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝖤​[𝟏A​∫01m∗​(θ;z)​dz]=∫01𝖤​[𝟏A​m∗​(θ;z)]​dz\displaystyle\mathsf{E}\big[\mathbf{1}\_{A}\int\_{0}^{1}m^{\*}(\theta;z)\mathrm{d}z\big]=\int\_{0}^{1}\mathsf{E}\big[\mathbf{1}\_{A}m^{\*}(\theta;z)\big]\mathrm{d}z |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01𝖤[𝟏A𝖤[𝟏{τ∗​(z)<θ}(fτ∗​(z)𝟏{τ∗​(z)<σ∗}+hτ∗​(z)𝟏{τ∗​(z)=σ∗})\displaystyle=\int\_{0}^{1}\!\!\mathsf{E}\Big[\mathbf{1}\_{A}\mathsf{E}\Big[\mathbf{1}\_{\{\tau\_{\*}(z)<\theta\}}\big(f\_{\tau\_{\*}(z)}\mathbf{1}\_{\{\tau\_{\*}(z)<\sigma\_{\*}\}}\!+\!h\_{\tau\_{\*}(z)}\mathbf{1}\_{\{\tau\_{\*}(z)=\sigma\_{\*}\}}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟏{σ∗<θ}𝟏{σ∗<τ∗​(z)}gσ∗|ℱθ1]+𝟏{θ≤τ∗​(z)}V^θ∗,1)]dz\displaystyle\qquad\qquad\qquad+\!\mathbf{1}\_{\{\sigma\_{\*}<\theta\}}\mathbf{1}\_{\{\sigma\_{\*}<\tau\_{\*}(z)\}}g\_{\sigma\_{\*}}\Big|\mathcal{F}^{1}\_{\theta}\Big]\!+\!\mathbf{1}\_{\{\theta\leq\tau\_{\*}(z)\}}\hat{V}^{\*,1}\_{\theta}\Big)\Big]\mathrm{d}z |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01𝖤[𝟏A(𝟏{τ∗​(z)<θ}(fτ∗​(z)𝟏{τ∗​(z)<σ∗}+hτ∗​(z)𝟏{τ∗​(z)=σ∗})\displaystyle=\int\_{0}^{1}\!\!\mathsf{E}\Big[\mathbf{1}\_{A}\Big(\mathbf{1}\_{\{\tau\_{\*}(z)<\theta\}}\big(f\_{\tau\_{\*}(z)}\mathbf{1}\_{\{\tau\_{\*}(z)<\sigma\_{\*}\}}\!+\!h\_{\tau\_{\*}(z)}\mathbf{1}\_{\{\tau\_{\*}(z)=\sigma\_{\*}\}}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟏{σ∗<θ}𝟏{σ∗<τ∗​(z)}gσ∗+𝟏{θ≤τ∗​(z)}V^θ∗,1)]dz,\displaystyle\qquad\qquad\qquad+\!\mathbf{1}\_{\{\sigma\_{\*}<\theta\}}\mathbf{1}\_{\{\sigma\_{\*}<\tau\_{\*}(z)\}}g\_{\sigma\_{\*}}\!+\!\mathbf{1}\_{\{\theta\leq\tau\_{\*}(z)\}}\hat{V}^{\*,1}\_{\theta}\Big)\Big]\mathrm{d}z, |  |

where the first equality is by Fubini’s theorem (which holds by joint measurability of (z,ω)↦m∗​(θ;z)​(ω)(z,\omega)\mapsto m^{\*}(\theta;z)(\omega)), the second equality is by (ii) and the third one is by tower property. On the other hand,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝖤​[𝟏A​Mθ∗]\displaystyle\mathsf{E}[\mathbf{1}\_{A}M^{\*}\_{\theta}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖤​[𝟏A​𝖤​[𝟏{τ∗<θ}​(fτ∗​𝟏{τ∗<σ∗}+hτ∗​𝟏{τ∗=σ∗})+𝟏{σ∗<θ}​𝟏{σ∗<τ∗}​gσ∗|ℱθ1]+𝟏A​𝟏{θ≤τ∗}​V^θ∗,1]\displaystyle=\mathsf{E}\Big[\mathbf{1}\_{A}\mathsf{E}\Big[\mathbf{1}\_{\{\tau\_{\*}<\theta\}}\big(f\_{\tau\_{\*}}\mathbf{1}\_{\{\tau\_{\*}<\sigma\_{\*}\}}+h\_{\tau\_{\*}}\mathbf{1}\_{\{\tau\_{\*}=\sigma\_{\*}\}}\big)+\mathbf{1}\_{\{\sigma\_{\*}<\theta\}}\mathbf{1}\_{\{\sigma\_{\*}<\tau\_{\*}\}}g\_{\sigma\_{\*}}\Big|\mathcal{F}^{1}\_{\theta}\Big]+\mathbf{1}\_{A}\mathbf{1}\_{\{\theta\leq\tau\_{\*}\}}\hat{V}^{\*,1}\_{\theta}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖤​[𝟏A​(𝟏{τ∗<θ}​(fτ∗​𝟏{τ∗<σ∗}+hτ∗​𝟏{τ∗=σ∗})+𝟏{σ∗<θ}​𝟏{σ∗<τ∗}​gσ∗+𝟏{θ≤τ∗}​V^θ∗,1)]\displaystyle=\mathsf{E}\Big[\mathbf{1}\_{A}\Big(\mathbf{1}\_{\{\tau\_{\*}<\theta\}}\big(f\_{\tau\_{\*}}\mathbf{1}\_{\{\tau\_{\*}<\sigma\_{\*}\}}+h\_{\tau\_{\*}}\mathbf{1}\_{\{\tau\_{\*}=\sigma\_{\*}\}}\big)+\mathbf{1}\_{\{\sigma\_{\*}<\theta\}}\mathbf{1}\_{\{\sigma\_{\*}<\tau\_{\*}\}}g\_{\sigma\_{\*}}+\mathbf{1}\_{\{\theta\leq\tau\_{\*}\}}\hat{V}^{\*,1}\_{\theta}\Big)\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01𝖤[𝟏A(𝟏{τ∗​(z)<θ}(fτ∗​(z)𝟏{τ∗​(z)<σ∗}+hτ∗​(z)𝟏{τ∗​(z)=σ∗})\displaystyle=\int\_{0}^{1}\mathsf{E}\Big[\mathbf{1}\_{A}\Big(\mathbf{1}\_{\{\tau\_{\*}(z)<\theta\}}\big(f\_{\tau\_{\*}(z)}\mathbf{1}\_{\{\tau\_{\*}(z)<\sigma\_{\*}\}}\!+\!h\_{\tau\_{\*}(z)}\mathbf{1}\_{\{\tau\_{\*}(z)=\sigma\_{\*}\}}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟏{σ∗<θ}𝟏{σ∗<τ∗​(z)}gσ∗+𝟏{θ≤τ∗​(z)}V^θ∗,1)]dz,\displaystyle\qquad\qquad\qquad+\!\mathbf{1}\_{\{\sigma\_{\*}<\theta\}}\mathbf{1}\_{\{\sigma\_{\*}<\tau\_{\*}(z)\}}g\_{\sigma\_{\*}}\!+\!\mathbf{1}\_{\{\theta\leq\tau\_{\*}(z)\}}\hat{V}^{\*,1}\_{\theta}\Big)\Big]\mathrm{d}z, |  |

where the second equality is by tower property and the third one by Fubini’s theorem, which is justified by the joint measurability in (z,ω)(z,\omega) of the expression under the expectation. This concludes the proof of (i).
∎

## Appendix D Some decompositions of processes and stopping times

In this section we obtain a handy decomposition of stochastic processes for the study of examples from Section [5](https://arxiv.org/html/2510.15616v1#S5 "5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information"). We believe most of these results to be well-known from the general theory of stochastic processes but we are unable to provide precise references for them.

Let 𝔾⊂𝔽\mathbb{G}\subset\mathbb{F} be a right-continuous filtration completed with 𝖯\mathsf{P}-null sets. Given a process X∈ℒb​(𝖯)X\in\mathcal{L}\_{b}(\mathsf{P}), we denote by Xo𝔾=(Xot𝔾)t∈[0,T]\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-8.522pt{o}\kern 6.10211pt}}\_{{\kern-5.64687pt\kern 6.10211pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-8.522pt{o}\kern 6.10211pt}}\_{{\kern-5.64687pt\kern 6.10211pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-5.18529pt{o}\kern 3.44402pt}}\_{{\kern-2.98877pt\kern 3.44402pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-3.91557pt{o}\kern 2.1743pt}}\_{{\kern-1.71906pt\kern 2.1743pt}}}^{\mathbb{G}}=(\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-8.522pt{o}\kern 6.10211pt}}\_{{\kern-5.64687pt\kern 6.10211pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-8.522pt{o}\kern 6.10211pt}}\_{{\kern-5.64687pt\kern 6.10211pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-5.18529pt{o}\kern 3.44402pt}}\_{{\kern-2.98877pt\kern 3.44402pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-3.91557pt{o}\kern 2.1743pt}}\_{{\kern-1.71906pt\kern 2.1743pt}}}^{\mathbb{G}}\_{t})\_{t\in[0,T]} its 𝔾\mathbb{G}-optional projection under the measure 𝖯\mathsf{P}, i.e., the unique 𝔾\mathbb{G}-optional process such that Xoτ𝔾​𝟏{τ<∞}=𝖤​[Xτ​𝟏{τ<∞}|𝒢τ]\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-8.522pt{o}\kern 6.10211pt}}\_{{\kern-5.64687pt\kern 6.10211pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-8.522pt{o}\kern 6.10211pt}}\_{{\kern-5.64687pt\kern 6.10211pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-5.18529pt{o}\kern 3.44402pt}}\_{{\kern-2.98877pt\kern 3.44402pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0ptX}^{{\kern-3.91557pt{o}\kern 2.1743pt}}\_{{\kern-1.71906pt\kern 2.1743pt}}}^{\mathbb{G}}\_{\tau}\mathbf{1}\_{\{\tau<\infty\}}=\mathsf{E}\big[X\_{\tau}\mathbf{1}\_{\{\tau<\infty\}}\big|\mathcal{G}\_{\tau}\big], 𝖯​-a.s.\mathsf{P}\mbox{-a.s.}, for any stopping time τ∈𝒯0​(𝔾)\tau\in\mathcal{T}\_{0}(\mathbb{G}). We recall that the optional projection Ao𝔾\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-6.06807pt{o}\kern 3.64818pt}}\_{{\kern-3.19293pt\kern 3.64818pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-6.06807pt{o}\kern 3.64818pt}}\_{{\kern-3.19293pt\kern 3.64818pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-3.05054pt{o}\kern 1.30927pt}}\_{{\kern-0.85402pt\kern 1.30927pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-2.00053pt{o}\kern 0.25926pt}}\_{{\kern 0.19598pt\kern 0.25926pt}}}^{\mathbb{G}} of a non-decreasing process AA is a submartingale because

|  |  |  |
| --- | --- | --- |
|  | Aos𝔾=𝖤​[As|𝒢s]≤𝖤​[At|𝒢s]=𝖤​[𝖤​[At|𝒢t]|𝒢s]=𝖤​[Aot𝔾|𝒢s], for ​s≤t.\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-6.06807pt{o}\kern 3.64818pt}}\_{{\kern-3.19293pt\kern 3.64818pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-6.06807pt{o}\kern 3.64818pt}}\_{{\kern-3.19293pt\kern 3.64818pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-3.05054pt{o}\kern 1.30927pt}}\_{{\kern-0.85402pt\kern 1.30927pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-2.00053pt{o}\kern 0.25926pt}}\_{{\kern 0.19598pt\kern 0.25926pt}}}^{\mathbb{G}}\_{s}=\mathsf{E}[A\_{s}|\mathcal{G}\_{s}]\leq\mathsf{E}[A\_{t}|\mathcal{G}\_{s}]=\mathsf{E}[\mathsf{E}[A\_{t}|\mathcal{G}\_{t}]|\mathcal{G}\_{s}]=\mathsf{E}[\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-6.06807pt{o}\kern 3.64818pt}}\_{{\kern-3.19293pt\kern 3.64818pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-6.06807pt{o}\kern 3.64818pt}}\_{{\kern-3.19293pt\kern 3.64818pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-3.05054pt{o}\kern 1.30927pt}}\_{{\kern-0.85402pt\kern 1.30927pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-2.00053pt{o}\kern 0.25926pt}}\_{{\kern 0.19598pt\kern 0.25926pt}}}^{\mathbb{G}}\_{t}|\mathcal{G}\_{s}],\quad\text{ for }s\leq t. |  |

The optional projection of a bounded variation process is the difference of two submartingales hence, in particular, a semi-martingale.

In the next lemma we take 𝔽=𝔾∨σ​(Θ)\mathbb{F}=\mathbb{G}\vee\sigma(\Theta), where Θ\Theta is a random variable on (Ω,ℱ,𝖯)(\Omega,\mathcal{F},\mathsf{P}) taking values in some measurable space (E,ℰ)(E,\mathcal{E}). Thats is, 𝔽\mathbb{F} is the initial enlargement of the filtration 𝔾\mathbb{G} by Θ\Theta. Notice that we do not assume independence of Θ\Theta from 𝔾\mathbb{G}.

###### Lemma D.1.

Any 𝔽\mathbb{F}-optional process (At)t∈[0,T](A\_{t})\_{t\in[0,T]} can be written as At​(ω)=A~​(t,ω,Θ​(ω))A\_{t}(\omega)=\tilde{A}(t,\omega,\Theta(\omega)), where A~\tilde{A} is ℬ​([0,T])×ℱ×ℰ\mathcal{B}([0,T])\times\mathcal{F}\times\mathcal{E}-measurable function and, for every fixed z∈Ez\in E, the process (t,ω)↦A~​(t,ω,z)(t,\omega)\mapsto\tilde{A}(t,\omega,z) is 𝔾\mathbb{G}-optional.

###### Proof.

By an adaptation of Prop. 3.3 and Cor. 3.4 in [[EI18](https://arxiv.org/html/2510.15616v1#bib.bibx19)] to a general measurable space (E,ℰ)(E,\mathcal{E}) instead of (ℝ,ℬ​(ℝ))(\mathbb{R},\mathcal{B}(\mathbb{R})), for any 𝔽\mathbb{F}-stopping time τ\tau, there is a measurable function τ′:Ω×E→[0,T]\tau^{\prime}:\Omega\times E\to[0,T] such that τ​(ω)=τ′​(ω,Θ​(ω))\tau(\omega)=\tau^{\prime}(\omega,\Theta(\omega)) and τ′​(ω,z)\tau^{\prime}(\omega,z) is a 𝔾\mathbb{G}-stopping time for any z∈Ez\in E. This implies that the statement of the lemma holds true for processes At=𝟏{t≥τ}A\_{t}=\mathbf{1}\_{\{t\geq\tau\}}, where τ\tau is an 𝔽\mathbb{F}-stopping time.

Let 𝒞\mathcal{C} be the class of ℱT\mathcal{F}\_{T}-measurable (not necessarily optional) processes (At)t∈[0,T](A\_{t})\_{t\in[0,T]} that satisfy At​(ω)=A~​(t,ω,Θ​(ω))A\_{t}(\omega)=\tilde{A}(t,\omega,\Theta(\omega)) for a measurable A~\tilde{A} such that (t,ω)↦A~​(t,ω,z)(t,\omega)\mapsto\tilde{A}(t,\omega,z) is a 𝔾\mathbb{G}-optional process for any z∈Ez\in E. From the previous paragraph, 𝒞\mathcal{C} contains constants and processes of the form At=𝟏{t≥τ}A\_{t}=\mathbf{1}\_{\{t\geq\tau\}}, where τ\tau is a 𝔽\mathbb{F}-stopping time. Recall that ({τ≤t},τ∈𝒯​(𝔽),t≥0)(\{\tau\leq t\},\tau\in\mathcal{T}(\mathbb{F}),t\geq 0) forms a π\pi-system that generates the 𝔽\mathbb{F}-optional σ\sigma-algebra ([[DM78](https://arxiv.org/html/2510.15616v1#bib.bibx15), Thm. IV.64(c)]). We claim that for any bounded sequence {(Atn​(ω))t∈[0,T],n∈ℕ}⊂𝒞\{(A^{n}\_{t}(\omega))\_{t\in[0,T]},n\in\mathbb{N}\}\subset\mathcal{C} such that Atn​(ω)↑At​(ω)A^{n}\_{t}(\omega)\uparrow A\_{t}(\omega) for all (t,ω)(t,\omega) as n→∞n\to\infty we also have At​(ω)=A~​(t,ω,Θ​(ω))A\_{t}(\omega)=\tilde{A}(t,\omega,\Theta(\omega)) for a measurable function A~​(t,ω,z)\tilde{A}(t,\omega,z) such that (t,ω)↦A~​(t,ω,z)(t,\omega)\mapsto\tilde{A}(t,\omega,z) is 𝔾\mathbb{G}-optional for any z∈Ez\in E. Then, a monotone class theorem ([[Wil91](https://arxiv.org/html/2510.15616v1#bib.bibx44), Thm. 3.14]) guarantees that 𝒞\mathcal{C}, which is also a vector space, contains every bounded 𝔽\mathbb{F}-optional process. An extension to unbounded processes is immediate by truncation and taking limits.

Let us now verify the claim about the monotone convergence of a sequence {(Atn)t∈[0,T],n∈ℕ}⊂𝒞\{(A^{n}\_{t})\_{t\in[0,T]},n\in\mathbb{N}\}\subset\mathcal{C}. For (Atn​(ω))t∈[0,T]∈𝒞(A^{n}\_{t}(\omega))\_{t\in[0,T]}\in\mathcal{C}, the function (t,ω,z)↦A~n​(t,ω,z)(t,\omega,z)\mapsto\tilde{A}^{n}(t,\omega,z) is ℬ​([0,T])×ℱ×ℰ\mathcal{B}([0,T])\times\mathcal{F}\times\mathcal{E}-measurable and satisfies: (t,ω)↦A~n​(t,ω,z)(t,\omega)\mapsto\tilde{A}^{n}(t,\omega,z) is 𝔾\mathbb{G}-optional for every z∈Ez\in E. Define A~​(t,ω,z)≔lim supn→∞A~n​(t,ω,z)\tilde{A}(t,\omega,z)\coloneqq\limsup\_{n\to\infty}\tilde{A}^{n}(t,\omega,z) so that A~\tilde{A} is ℬ​([0,T])×ℱ×ℰ\mathcal{B}([0,T])\times\mathcal{F}\times\mathcal{E}-measurable and (t,ω)↦A~t​(t,ω,z)(t,\omega)\mapsto\tilde{A}\_{t}(t,\omega,z) is 𝔾\mathbb{G}-optional for every z∈Ez\in E.
We have

|  |  |  |
| --- | --- | --- |
|  | At​(ω)=limn→∞Atn​(ω)=lim supn→∞Atn​(ω)=lim supn→∞A~n​(t,ω,Θ​(ω))=A~​(t,ω,Θ​(ω)).A\_{t}(\omega)=\lim\_{n\to\infty}A^{n}\_{t}(\omega)=\limsup\_{n\to\infty}A^{n}\_{t}(\omega)=\limsup\_{n\to\infty}\tilde{A}^{n}(t,\omega,\Theta(\omega))=\tilde{A}(t,\omega,\Theta(\omega)). |  |

Hence (At​(ω))t∈[0,T]∈𝒞(A\_{t}(\omega))\_{t\in[0,T]}\in\mathcal{C} as needed.
∎

When we specify a bit more the structure of the probability space (Ω,ℱ,𝖯)(\Omega,\mathcal{F},\mathsf{P}) we are able to obtain finer properties of the representation At​(ω)=A~​(t,ω,Θ​(ω))A\_{t}(\omega)=\tilde{A}(t,\omega,\Theta(\omega)) than in the lemma above. Assume that

|  |  |  |  |
| --- | --- | --- | --- |
| (D.1) |  | (Ω,ℱ,𝖯)=(Ω0×Ω1,ℱ0×ℱ1,𝖯0×𝖯1).\displaystyle(\Omega,\mathcal{F},\mathsf{P})=(\Omega^{0}\times\Omega^{1},\mathcal{F}^{0}\times\mathcal{F}^{1},\mathsf{P}^{0}\times\mathsf{P}^{1}). |  |

Given a filtration 𝔾0=(𝒢t0)t∈[0,T]\mathbb{G}^{0}=(\mathcal{G}^{0}\_{t})\_{t\in[0,T]} on ℱ0\mathcal{F}^{0} satisfying usual conditions let 𝔾\mathbb{G} be the 𝖯0×𝖯1\mathsf{P}^{0}\times\mathsf{P}^{1}-completion of (𝒢t0×{Ω1,∅})t∈[0,T](\mathcal{G}^{0}\_{t}\times\{\Omega^{1},\varnothing\})\_{t\in[0,T]}. Let Θ:(Ω1,ℱ1)→(E,ℰ)\Theta:(\Omega^{1},\mathcal{F}^{1})\to(E,\mathcal{E}) be measurable and let Σ​(Θ)\Sigma(\Theta) be the σ\sigma-algebra ({Ω0,∅}×Θ−1​(A),A∈ℰ)(\{\Omega^{0},\varnothing\}\times\Theta^{-1}(A),A\in\mathcal{E}) in ℱ0×ℱ1\mathcal{F}^{0}\times\mathcal{F}^{1}. Set 𝔽=𝔾∨Σ​(Θ)\mathbb{F}=\mathbb{G}\vee\Sigma(\Theta), denote by (𝔾0)o(\mathbb{G}^{0})^{o} the 𝔾0\mathbb{G}^{0}-optional σ\sigma-algebra on [0,T]×Ω0[0,T]\times\Omega^{0} and let (𝔽)o(\mathbb{F})^{o} be the 𝔽\mathbb{F}-optional σ\sigma-algebra on [0,T]×Ω[0,T]\times\Omega. In this context, σ​(Θ)≔{Θ−1​(H),H∈ℰ}\sigma(\Theta)\coloneqq\{\Theta^{-1}(H),H\in\mathcal{E}\}, with Θ−1​(H)={ω1:Θ​(ω1)∈H}\Theta^{-1}(H)=\{\omega\_{1}:\Theta(\omega\_{1})\in H\}, is the σ\sigma-algebra generated by Θ\Theta on Ω1\Omega^{1} (see, e.g., [[Hal74](https://arxiv.org/html/2510.15616v1#bib.bibx25), p. 76]). Moreover, sets of the form {(t,ω0):t≥τ​(ω0)}\{(t,\omega\_{0}):t\geq\tau(\omega\_{0})\} for 𝔾0\mathbb{G}^{0}-stopping times τ\tau generate the 𝔾0\mathbb{G}^{0}-optional σ\sigma-algebra (𝔾0)o(\mathbb{G}^{0})^{o} on [0,T]×Ω0[0,T]\times\Omega^{0} (see [[DM78](https://arxiv.org/html/2510.15616v1#bib.bibx15), Thm. IV.64(c)]).
This setting will apply to the following 3 lemmas.

###### Lemma D.2.

Assume that EE is countable. Any 𝔽\mathbb{F}-stopping time τ\tau has the representation τ​(ω)=τ′​(ω0,Θ​(ω1))\tau(\omega)=\tau^{\prime}(\omega\_{0},\Theta(\omega\_{1})) for a 𝔾0×ℰ\mathbb{G}^{0}\times\mathcal{E}-measurable function τ′\tau^{\prime} such that ω0↦τ′​(ω0,z)\omega\_{0}\mapsto\tau^{\prime}(\omega\_{0},z) is a 𝔾0\mathbb{G}^{0}-stopping time for any z∈Ez\in E.

###### Proof.

We start with an auxiliary result. Let φ:Ω→ℝ\varphi:\Omega\to\mathbb{R} be of the form φ​(ω0,ω1)=φ0​(ω0)​𝟏B​(ω1)\varphi(\omega\_{0},\omega\_{1})=\varphi\_{0}(\omega\_{0})\mathbf{1}\_{B}(\omega\_{1}), where B∈σ​(Θ)B\in\sigma(\Theta), i.e., B=Θ−1​(H)B=\Theta^{-1}(H) for some H∈ℰH\in\mathcal{E} (see, e.g., [[Hal74](https://arxiv.org/html/2510.15616v1#bib.bibx25), p. 76]) and φ0\varphi\_{0} is 𝒢t0\mathcal{G}^{0}\_{t}-measurable random variable. Then

|  |  |  |  |
| --- | --- | --- | --- |
| (D.2) |  | φ​(ω)=φ′​(ω0,Θ​(ω1))\varphi(\omega)=\varphi^{\prime}(\omega\_{0},\Theta(\omega\_{1})) |  |

for a 𝒢t0×ℰ\mathcal{G}^{0}\_{t}\times\mathcal{E}-measurable function φ′\varphi^{\prime}. Functions φ\varphi as in ([D.2](https://arxiv.org/html/2510.15616v1#A4.E2 "In Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information")) form a vector space, which is closed under monotone limits and it contains constants and indicator functions of a π\pi-system that generates 𝒢0×σ​(Θ)\mathcal{G}^{0}\times\sigma(\Theta). Hence, the representation ([D.2](https://arxiv.org/html/2510.15616v1#A4.E2 "In Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information")) extends to any ℱt\mathcal{F}\_{t}-measurable function φ\varphi thanks to the Monotone Class Theorem ([[Wil91](https://arxiv.org/html/2510.15616v1#bib.bibx44), Thm. 3.14]) and noticing that ℱt=𝒢t0×σ​(Θ)\mathcal{F}\_{t}=\mathcal{G}^{0}\_{t}\times\sigma(\Theta) in the setting of the lemma.

Without loss of generality, we assume that 𝖯1​(Θ=z)>0\mathsf{P}^{1}(\Theta=z)>0 for any z∈Ez\in E; this will simplify notation in the arguments below.
Take an 𝔽\mathbb{F}-stopping time τ\tau. It is ℱT\mathcal{F}\_{T}-measurable, so, using the first part of the proof, it has the representation τ​(ω)=τ′​(ω0,Θ​(ω1))\tau(\omega)=\tau^{\prime}(\omega\_{0},\Theta(\omega\_{1})) for a 𝒢T0×ℰ\mathcal{G}^{0}\_{T}\times\mathcal{E}-measurable function τ′\tau^{\prime}. We will show that ω0↦τ′​(ω0,z)\omega\_{0}\mapsto\tau^{\prime}(\omega\_{0},z) is a 𝔾0\mathbb{G}^{0}-stopping time for any z∈Ez\in E. To this end, fix t∈[0,T]t\in[0,T]. The function φ≔𝟏{τ≤t}\varphi\coloneqq\mathbf{1}\_{\{\tau\leq t\}} is ℱt\mathcal{F}\_{t}-measurable, so by the arguments in the first paragraph of the proof there is a 𝒢t0×ℰ\mathcal{G}^{0}\_{t}\times\mathcal{E}-measurable function φ′\varphi^{\prime} that satisfies ([D.2](https://arxiv.org/html/2510.15616v1#A4.E2 "In Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information")). Hence, we have the equality

|  |  |  |
| --- | --- | --- |
|  | {(ω0,ω1)∈Ω:τ′​(ω0,Θ​(ω1))≤t}={(ω0,ω1)∈Ω:φ′​(ω0,Θ​(ω1))=1}.\{(\omega\_{0},\omega\_{1})\in\Omega:\tau^{\prime}(\omega\_{0},\Theta(\omega\_{1}))\leq t\}=\{(\omega\_{0},\omega\_{1})\in\Omega:\varphi^{\prime}(\omega\_{0},\Theta(\omega\_{1}))=1\}. |  |

By applying the map (ω0,ω1)↦(ω0,Θ​(ω1))(\omega\_{0},\omega\_{1})\mapsto(\omega\_{0},\Theta(\omega\_{1})) and recalling that Θ\Theta is a surjective map, the above equality yields

|  |  |  |
| --- | --- | --- |
|  | {(ω0,z)∈Ω0×E:τ′​(ω0,z)≤t}={(ω0,z)∈Ω0×E:φ′​(ω0,z)=1}.\{(\omega\_{0},z)\in\Omega^{0}\times E:\tau^{\prime}(\omega\_{0},z)\leq t\}=\{(\omega\_{0},z)\in\Omega^{0}\times E:\varphi^{\prime}(\omega\_{0},z)=1\}. |  |

The set on the right-hand side is 𝒢t0×ℰ\mathcal{G}^{0}\_{t}\times\mathcal{E}-measurable by the construction of φ′\varphi^{\prime}. So is the set on the left-hand side and, by Fubini’s theorem, zz-sections of this set are 𝒢t0\mathcal{G}^{0}\_{t}-measurable, i.e.,

|  |  |  |
| --- | --- | --- |
|  | {ω0∈Ω0:τ′​(ω0,z)≤t}∈𝒢t0\{\omega\_{0}\in\Omega^{0}:\tau^{\prime}(\omega\_{0},z)\leq t\}\in\mathcal{G}^{0}\_{t} |  |

for any z∈Ez\in E. By the arbitrariness of tt, we conclude that τ′​(⋅,z)\tau^{\prime}(\cdot,z) is a 𝔾0\mathbb{G}^{0}-stopping time for any zz. We finish by commenting why we could exclude from the above analysis those z∈Ez\in E with 𝖯1​(Θ=z)=0\mathsf{P}^{1}(\Theta=z)=0: for such zz, we set τ′​(⋅,z)=0\tau^{\prime}(\cdot,z)=0.
∎

###### Lemma D.3.

We have (𝔾0)o×σ​(Θ)⊆(𝔽)o(\mathbb{G}^{0})^{o}\times\sigma(\Theta)\subseteq(\mathbb{F})^{o}. Any A:[0,T]×Ω↦ℝA:[0,T]\times\Omega\mapsto\mathbb{R} which is (𝔾0)o×σ​(Θ)(\mathbb{G}^{0})^{o}\times\sigma(\Theta)-measurable can be written as At​(ω0,ω1)=A~​(t,ω0,Θ​(ω1))A\_{t}(\omega\_{0},\omega\_{1})=\tilde{A}(t,\omega\_{0},\Theta(\omega\_{1})), where A~\tilde{A} is (𝔾0)o×ℰ(\mathbb{G}^{0})^{o}\times\mathcal{E}-measurable function. Moreover, if EE is countable then the representation holds for any 𝔽\mathbb{F}-optional process (At)t∈[0,T](A\_{t})\_{t\in[0,T]}.

###### Proof.

First we prove the representation of (𝔾0)o×σ​(Θ)(\mathbb{G}^{0})^{o}\times\sigma(\Theta)-measurable process AA.
For any 𝔾0\mathbb{G}^{0}-stopping time τ\tau and any B=Θ−1​(H)B=\Theta^{-1}(H), where H∈ℰH\in\mathcal{E}, let us first consider processes of the form

|  |  |  |  |
| --- | --- | --- | --- |
| (D.3) |  | At​(ω)=𝟏{τ​(ω0)≤t}​𝟏B​(ω1).\displaystyle A\_{t}(\omega)=\mathbf{1}\_{\{\tau(\omega\_{0})\leq t\}}\mathbf{1}\_{B}(\omega\_{1}). |  |

Then we have At​(ω)=A~​(t,ω0,Θ​(ω1))A\_{t}(\omega)=\tilde{A}(t,\omega\_{0},\Theta(\omega\_{1})) with A~​(t,ω0,z)=𝟏{τ​(ω0)≤t}​𝟏H​(z)\tilde{A}(t,\omega\_{0},z)=\mathbf{1}\_{\{\tau(\omega\_{0})\leq t\}}\mathbf{1}\_{H}(z).
Since processes of the form ([D.3](https://arxiv.org/html/2510.15616v1#A4.E3 "In Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information")) generate (𝔾0)o×σ​(Θ)(\mathbb{G}^{0})^{o}\times\sigma(\Theta), using the Monotone Class Theorem ([[Wil91](https://arxiv.org/html/2510.15616v1#bib.bibx44), Thm. 3.14]) the representation At​(ω)=A~​(t,ω0,Θ​(ω1))A\_{t}(\omega)=\tilde{A}(t,\omega\_{0},\Theta(\omega\_{1})) extends to all bounded functions A:[0,T]×Ω↦ℝA:[0,T]\times\Omega\mapsto\mathbb{R} which are measurable with respect to (𝔾0)o×σ​(Θ)(\mathbb{G}^{0})^{o}\times\sigma(\Theta). Moreover, each process of the form ([D.3](https://arxiv.org/html/2510.15616v1#A4.E3 "In Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information")) is certainly (𝔽)o(\mathbb{F})^{o}-measurable and
then we also obtain (𝔾0)o×σ​(Θ)⊆(𝔽)o(\mathbb{G}^{0})^{o}\times\sigma(\Theta)\subseteq(\mathbb{F})^{o}.

For the last statement we need to show that when EE is countable, then the 𝔽\mathbb{F}-optional σ\sigma-algebra (𝔽)o(\mathbb{F})^{o} coincides with (𝔾0)o×σ​(Θ)(\mathbb{G}^{0})^{o}\times\sigma(\Theta). The inclusion (𝔾0)o×σ​(Θ)⊆(𝔽)o(\mathbb{G}^{0})^{o}\times\sigma(\Theta)\subseteq(\mathbb{F})^{o} has already been proved. For the reverse inclusion,
we recall that the 𝔽\mathbb{F}-optional σ\sigma-algebra is generated by sets of the form {(t,ω)∈[0,T]×Ω:τ​(ω)≤t}\{(t,\omega)\in[0,T]\times\Omega:\tau(\omega)\leq t\}, where τ\tau is an 𝔽\mathbb{F}-stopping time (see [[DM78](https://arxiv.org/html/2510.15616v1#bib.bibx15), Thm. IV.64(c)]). It remains to show that such sets belong to (𝔾0)o×σ​(Θ)(\mathbb{G}^{0})^{o}\times\sigma(\Theta). To this end, we fix an 𝔽\mathbb{F}-stopping time τ\tau. By Lemma [D.2](https://arxiv.org/html/2510.15616v1#A4.Thmtheorem2 "Lemma D.2. ‣ Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information"), we have
τ​(ω)=τ′​(ω0,Θ​(ω1))\tau(\omega)=\tau^{\prime}(\omega\_{0},\Theta(\omega\_{1})) with τ′​(⋅,z)\tau^{\prime}(\cdot,z) a 𝔾0\mathbb{G}^{0}-stopping time for each z∈Ez\in E. Hence,

|  |  |  |
| --- | --- | --- |
|  | {(t,ω)∈[0,T]×Ω:τ​(ω)≤t}={(t,ω)∈[0,T]×Ω:τ′​(ω0,Θ​(ω1))≤t}=⋃z∈E({(t,ω)∈[0,T]×Ω:τ′​(ω0,z)≤t}∩{(t,ω)∈[0,T]×Ω:Θ​(ω1)=z})=⋃z∈E[({(t,ω0)∈[0,T]×Ω0:τ′​(ω0,z)≤t}×Ω1)∩([0,T]×Ω0×{ω1∈Ω1:Θ​(ω1)=z})].\displaystyle\begin{aligned} &\big\{(t,\omega)\in[0,T]\times\Omega:\tau(\omega)\leq t\big\}=\big\{(t,\omega)\in[0,T]\times\Omega:\tau^{\prime}(\omega\_{0},\Theta(\omega\_{1}))\leq t\big\}\\ &=\bigcup\_{z\in E}\Big(\big\{(t,\omega)\in[0,T]\times\Omega:\tau^{\prime}(\omega\_{0},z)\leq t\big\}\cap\{(t,\omega)\in[0,T]\times\Omega:\Theta(\omega\_{1})=z\}\Big)\\ &=\bigcup\_{z\in E}\Big[\Big(\big\{(t,\omega\_{0})\in[0,T]\times\Omega^{0}:\tau^{\prime}(\omega\_{0},z)\leq t\big\}\times\Omega^{1}\Big)\cap\Big([0,T]\times\Omega^{0}\times\{\omega\_{1}\in\Omega^{1}:\Theta(\omega\_{1})=z\}\Big)\Big].\end{aligned} |  |

Since

|  |  |  |
| --- | --- | --- |
|  | {(t,ω0)∈[0,T]×Ω0:τ′​(ω0,z)≤t}×Ω1∈(𝔾0)o×σ​(Θ)[0,T]×Ω0×{ω1∈Ω1:Θ​(ω1)=z}∈(𝔾0)o×σ​(Θ),\displaystyle\begin{aligned} \big\{(t,\omega\_{0})\in[0,T]\times\Omega^{0}:\tau^{\prime}(\omega\_{0},z)\leq t\big\}\times\Omega^{1}&\in(\mathbb{G}^{0})^{o}\times\sigma(\Theta)\\ [0,T]\times\Omega^{0}\times\{\omega\_{1}\in\Omega^{1}:\Theta(\omega\_{1})=z\}&\in(\mathbb{G}^{0})^{o}\times\sigma(\Theta),\end{aligned} |  |

we have

|  |  |  |
| --- | --- | --- |
|  | {(t,ω)∈[0,T]×Ω:τ​(ω)≤t}∈(𝔾0)o×σ​(Θ),\big\{(t,\omega)\in[0,T]\times\Omega:\tau(\omega)\leq t\big\}\in(\mathbb{G}^{0})^{o}\times\sigma(\Theta), |  |

which concludes the proof that (𝔽)o⊆(𝔾0)o×σ​(Θ)(\mathbb{F})^{o}\subseteq(\mathbb{G}^{0})^{o}\times\sigma(\Theta).
∎

###### Lemma D.4.

Consider the setting of Lemma [D.3](https://arxiv.org/html/2510.15616v1#A4.Thmtheorem3 "Lemma D.3. ‣ Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information") and assume that Θ\Theta takes at most countably many values (θi)i∈ℕ(\theta\_{i})\_{i\in\mathbb{N}}. Assume further that (At)t∈[0,T](A\_{t})\_{t\in[0,T]} is càdlàg. Then, the decomposition from Lemma [D.3](https://arxiv.org/html/2510.15616v1#A4.Thmtheorem3 "Lemma D.3. ‣ Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information") takes the form

|  |  |  |  |
| --- | --- | --- | --- |
| (D.4) |  | At​(ω0,ω1)=∑i=1∞𝟏{Θ​(ω1)=θi}​Ati​(ω0),t∈[0,T],A\_{t}(\omega\_{0},\omega\_{1})=\sum\_{i=1}^{\infty}\mathbf{1}\_{\{\Theta(\omega\_{1})=\theta\_{i}\}}A^{i}\_{t}(\omega\_{0}),\qquad t\in[0,T], |  |

for càdlàg 𝔾0\mathbb{G}^{0}-optional processes (Ati)t∈[0,T](A^{i}\_{t})\_{t\in[0,T]}, i∈ℕi\in\mathbb{N}. Moreover, the equality

|  |  |  |  |
| --- | --- | --- | --- |
| (D.5) |  | Aoτ−𝔾=𝖤​[Aτ−|𝒢τ]\displaystyle\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-6.06807pt{o}\kern 3.64818pt}}\_{{\kern-3.19293pt\kern 3.64818pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-6.06807pt{o}\kern 3.64818pt}}\_{{\kern-3.19293pt\kern 3.64818pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-3.05054pt{o}\kern 1.30927pt}}\_{{\kern-0.85402pt\kern 1.30927pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-2.00053pt{o}\kern 0.25926pt}}\_{{\kern 0.19598pt\kern 0.25926pt}}}^{\mathbb{G}}\_{\tau-}=\mathsf{E}\big[A\_{\tau-}\big|\mathcal{G}\_{\tau}\big] |  |

holds for any 𝔾\mathbb{G}-stopping time τ\tau.

###### Proof.

The decomposition ([D.4](https://arxiv.org/html/2510.15616v1#A4.E4 "In Lemma D.4. ‣ Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information")) is immediate from Lemma [D.3](https://arxiv.org/html/2510.15616v1#A4.Thmtheorem3 "Lemma D.3. ‣ Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information") with 𝔾0\mathbb{G}^{0}-optional processes (Ati)t∈[0,T](A^{i}\_{t})\_{t\in[0,T]}, i∈ℕi\in\mathbb{N}. It remains to prove that such processes are càdlàg. If 𝖯1​(Θ=θi)=0\mathsf{P}^{1}(\Theta=\theta\_{i})=0 for some index i∈ℕi\in\mathbb{N}, then the choice of (Ati)t∈[0,T](A^{i}\_{t})\_{t\in[0,T]} does not play any role and we can set it equal to 0 (we are using here that there are at most countably many such events). With no loss of generality we assume θi≠θj\theta\_{i}\neq\theta\_{j} for i≠ji\neq j so that ({Θ=θj},j∈ℕ)(\{\Theta=\theta\_{j}\},j\in\mathbb{N}) is a partition on Ω1\Omega\_{1}. Thus, for any i∈ℕi\in\mathbb{N} such that 𝖯1​(Θ=θi)>0\mathsf{P}^{1}(\Theta=\theta\_{i})>0, the 𝖯0×𝖯1\mathsf{P}^{0}\times\mathsf{P}^{1} measure of the set

|  |  |  |
| --- | --- | --- |
|  | {(ω0,ω1):Θ​(ω1)=θi​ and ​t↦At​(ω0,ω1)​ is not càdlàg ​​}\{(\omega\_{0},\omega\_{1}):\ \Theta(\omega\_{1})=\theta\_{i}\text{ and }t\mapsto A\_{t}(\omega\_{0},\omega\_{1})\text{ is not c\`{a}dl\`{a}g \!\!}\} |  |

is zero because (At)t∈[0,T](A\_{t})\_{t\in[0,T]} is càdlàg. By the decomposition ([D.4](https://arxiv.org/html/2510.15616v1#A4.E4 "In Lemma D.4. ‣ Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information")), the above set reads equivalently as

|  |  |  |
| --- | --- | --- |
|  | {(ω0,ω1):Θ​(ω1)=θi​ and ​t↦Ati​(ω0)​ is not càdlàg ​​}.\{(\omega\_{0},\omega\_{1}):\ \Theta(\omega\_{1})=\theta\_{i}\text{ and }t\mapsto A^{i}\_{t}(\omega\_{0})\text{ is not c\`{a}dl\`{a}g \!\!}\}. |  |

Since 𝖯1​(Θ=θi)>0\mathsf{P}^{1}(\Theta=\theta\_{i})>0, we must have 𝖯0​(t↦Ati​(ω0)​ is not càdlàg ​​)=0\mathsf{P}^{0}(t\mapsto A^{i}\_{t}(\omega\_{0})\text{ is not c\`{a}dl\`{a}g \!\!})=0, as claimed.

Let τ\tau be a 𝔾\mathbb{G}-stopping time. By the construction of 𝔾\mathbb{G} in the paragraph above Lemma [D.2](https://arxiv.org/html/2510.15616v1#A4.Thmtheorem2 "Lemma D.2. ‣ Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information"), τ\tau is 𝖯\mathsf{P}-a.s. equal to
(ω0,ω1)↦τ0​(ω0)(\omega\_{0},\omega\_{1})\mapsto\tau^{0}(\omega\_{0}), where τ0\tau^{0} is a 𝔾0\mathbb{G}^{0}-stopping time. We apply the decomposition ([D.4](https://arxiv.org/html/2510.15616v1#A4.E4 "In Lemma D.4. ‣ Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information"))

|  |  |  |  |
| --- | --- | --- | --- |
| (D.6) |  | 𝖤​[Aτ−|𝒢T]=𝖤​[∑i=1∞𝟏{Θ​(ω1)=θi}​Aτ0−i​(ω0)|𝒢T]=∑i=1∞𝖯​(Θ=θi)​Aτ−i,\displaystyle\mathsf{E}[A\_{\tau-}|\mathcal{G}\_{T}]=\mathsf{E}\Big[\sum\_{i=1}^{\infty}\mathbf{1}\_{\{\Theta(\omega\_{1})=\theta\_{i}\}}A^{i}\_{\tau^{0}-}(\omega\_{0})\Big|\mathcal{G}\_{T}\Big]=\sum\_{i=1}^{\infty}\mathsf{P}(\Theta=\theta\_{i})A^{i}\_{\tau-}, |  |

where the last equality follows from the fact that 𝒢T=𝒢T0×{Ω1,∅}\mathcal{G}\_{T}=\mathcal{G}^{0}\_{T}\times\{\Omega\_{1},\varnothing\} and by construction Θ\Theta is independent of 𝒢T0\mathcal{G}^{0}\_{T}; therefore, taking conditional expectation with respect to 𝒢T\mathcal{G}\_{T} is equivalent to integrating out ω1\omega\_{1}, see [[Bal17](https://arxiv.org/html/2510.15616v1#bib.bibx1), Lemma 4.1].

Using analogous arguments, for any 𝔾\mathbb{G}-stopping time τ\tau we have

|  |  |  |  |
| --- | --- | --- | --- |
| (D.7) |  | Aoτ𝔾=𝖤​[∑i=1∞𝟏{Θ=θi}​Aτi|𝒢τ]=∑i=1∞𝖯​(Θ=θi)​Aτi,\displaystyle\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-6.06807pt{o}\kern 3.64818pt}}\_{{\kern-3.19293pt\kern 3.64818pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-6.06807pt{o}\kern 3.64818pt}}\_{{\kern-3.19293pt\kern 3.64818pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-3.05054pt{o}\kern 1.30927pt}}\_{{\kern-0.85402pt\kern 1.30927pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-2.00053pt{o}\kern 0.25926pt}}\_{{\kern 0.19598pt\kern 0.25926pt}}}^{\mathbb{G}}\_{\tau}=\mathsf{E}\Big[\sum\_{i=1}^{\infty}\mathbf{1}\_{\{\Theta=\theta\_{i}\}}A^{i}\_{\tau}\Big|\mathcal{G}\_{\tau}\Big]=\sum\_{i=1}^{\infty}\mathsf{P}(\Theta=\theta\_{i})A^{i}\_{\tau}, |  |

where we implicitly extended Ati​(ω0)A^{i}\_{t}(\omega\_{0}) to the product space Ω0×Ω1\Omega\_{0}\times\Omega\_{1} in a trivial manner. The identity in ([D.7](https://arxiv.org/html/2510.15616v1#A4.E7 "In Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information")) means that the processes

|  |  |  |
| --- | --- | --- |
|  | t↦Aot𝔾 and t↦∑i=1∞𝖯​(Θ=θi)​Atit\mapsto\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-6.06807pt{o}\kern 3.64818pt}}\_{{\kern-3.19293pt\kern 3.64818pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-6.06807pt{o}\kern 3.64818pt}}\_{{\kern-3.19293pt\kern 3.64818pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-3.05054pt{o}\kern 1.30927pt}}\_{{\kern-0.85402pt\kern 1.30927pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-2.00053pt{o}\kern 0.25926pt}}\_{{\kern 0.19598pt\kern 0.25926pt}}}^{\mathbb{G}}\_{t}\quad\text{ and }\quad t\mapsto\sum\_{i=1}^{\infty}\mathsf{P}(\Theta=\theta\_{i})A^{i}\_{t} |  |

are indistinguishable. We recall that (Ati)(A^{i}\_{t}), i∈ℕi\in\mathbb{N}, are càdlàg, so for any 𝔾\mathbb{G}-stopping time τ\tau

|  |  |  |
| --- | --- | --- |
|  | Aoτ−𝔾=∑i=1∞𝖯​(Θ=θi)​Aτ−i=𝖤​[Aτ−|𝒢T],\mathchoice{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-6.06807pt{o}\kern 3.64818pt}}\_{{\kern-3.19293pt\kern 3.64818pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-6.06807pt{o}\kern 3.64818pt}}\_{{\kern-3.19293pt\kern 3.64818pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-3.05054pt{o}\kern 1.30927pt}}\_{{\kern-0.85402pt\kern 1.30927pt}}}{\hphantom{{}^{{{o}}}}{\kern-1.0pt\!A}^{{\kern-2.00053pt{o}\kern 0.25926pt}}\_{{\kern 0.19598pt\kern 0.25926pt}}}^{\mathbb{G}}\_{\tau-}=\sum\_{i=1}^{\infty}\mathsf{P}(\Theta=\theta\_{i})A^{i}\_{\tau-}=\mathsf{E}[A\_{\tau-}|\mathcal{G}\_{T}], |  |

where the last equality is by ([D.6](https://arxiv.org/html/2510.15616v1#A4.E6 "In Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information")). Then ([D.5](https://arxiv.org/html/2510.15616v1#A4.E5 "In Lemma D.4. ‣ Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information")) holds by further conditioning with respect to 𝒢τ\mathcal{G}\_{\tau}.
∎

## Appendix E Technical results for partially observed scenarios

In this section we develop useful results for the analysis performed in Section [5.1](https://arxiv.org/html/2510.15616v1#S5.SS1 "5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information"). We recall that the random variable 𝒥\mathcal{J} takes at most a countable number of values, for simplicity, a subset of ℕ\mathbb{N}.

###### Lemma E.1.

Let ℋ≔𝒢∨σ​(𝒥)\mathcal{H}\coloneqq\mathcal{G}\vee\sigma(\mathcal{J}) with 𝒥\mathcal{J} not necessarily independent of 𝒢\mathcal{G}. Then, for any ℋ\mathcal{H}-measurable XX there is a function f:Ω×ℕ→ℝf:\Omega\times\mathbb{N}\to\mathbb{R} such that ω↦f​(ω,j)\omega\mapsto f(\omega,j) is 𝒢\mathcal{G}-measurable for each j∈ℕj\in\mathbb{N} and X​(ω)=f​(ω,𝒥​(ω))X(\omega)=f(\omega,\mathcal{J}(\omega)).

###### Proof.

Let Λ\Lambda be the class of functions f:Ω×ℕ→ℝf:\Omega\times\mathbb{N}\to\mathbb{R} such that ω↦f​(ω,j)\omega\mapsto f(\omega,j) is 𝒢\mathcal{G}-measurable for each j∈ℕj\in\mathbb{N} and denote

|  |  |  |
| --- | --- | --- |
|  | Σ≔{X:X is ℋ-measurable, ​X​(ω)=f​(ω,𝒥​(ω))​for some​f∈Λ}.\Sigma\coloneqq\{X:\text{$X$ is $\mathcal{H}$-measurable, }X(\omega)=f(\omega,\mathcal{J}(\omega))\ \text{for some}\ f\in\Lambda\}. |  |

The class Σ\Sigma is a monotone class (cf., the proof of Lemma [D.1](https://arxiv.org/html/2510.15616v1#A4.Thmtheorem1 "Lemma D.1. ‣ Appendix D Some decompositions of processes and stopping times ‣ Martingale theory for Dynkin games with asymmetric information")) that contains random variables of the form X​(ω)=𝟏G​(ω)​𝟏{𝒥=j}​(ω)X(\omega)=\mathbf{1}\_{G}(\omega)\mathbf{1}\_{\{\mathcal{J}=j\}}(\omega) for G∈𝒢G\in\mathcal{G} and j∈ℕj\in\mathbb{N}. Since sets of the form G∩{𝒥=j}G\cap\{\mathcal{J}=j\} are a π\pi-system that generates ℋ\mathcal{H}, then Σ\Sigma contains all ℋ\mathcal{H}-measurable functions.
∎

Recall the notation for the symmetric difference of two sets A​△​B=(A∖B)∪(B∖A)A\triangle B=(A\setminus B)\cup(B\setminus A).

###### Lemma E.2.

With the notation of Lemma [E.1](https://arxiv.org/html/2510.15616v1#A5.Thmtheorem1 "Lemma E.1. ‣ Appendix E Technical results for partially observed scenarios ‣ Martingale theory for Dynkin games with asymmetric information") we have H∈ℋH\in\mathcal{H} if and only if there is a collection of sets (GiH)i∈ℕ⊂𝒢(G^{H}\_{i})\_{i\in\mathbb{N}}\subset\mathcal{G} such that H∩{𝒥=j}=GjH∩{𝒥=j}H\cap\{\mathcal{J}=j\}=G^{H}\_{j}\cap{\{\mathcal{J}=j\}} for all j∈ℕj\in\mathbb{N}.

If 𝒢\mathcal{G} is independent of σ​(𝒥)\sigma(\mathcal{J}) and (LiH)i∈ℕ⊂𝒢(L^{H}\_{i})\_{i\in\mathbb{N}}\subset\mathcal{G} is another collection of sets such that for all j∈ℕj\in\mathbb{N}, H∩{𝒥=j}=LjH∩{𝒥=j}H\cap\{\mathcal{J}=j\}=L^{H}\_{j}\cap{\{\mathcal{J}=j\}}, then

|  |  |  |
| --- | --- | --- |
|  | 𝖯​(⋃j∈ℕ(GjH​△​LjH))=0.\mathsf{P}\Big(\bigcup\_{j\in\mathbb{N}}(G^{H}\_{j}\triangle L^{H}\_{j})\Big)=0. |  |

###### Proof.

The ‘if’ implication in the first statement is trivial. For the ‘only if’ implication we take X=1HX=1\_{H}, so that by Lemma [E.1](https://arxiv.org/html/2510.15616v1#A5.Thmtheorem1 "Lemma E.1. ‣ Appendix E Technical results for partially observed scenarios ‣ Martingale theory for Dynkin games with asymmetric information") there is fH:Ω×ℕ→ℝf\_{H}:\Omega\times\mathbb{N}\to\mathbb{R} such that fH​(⋅,j)f\_{H}(\cdot,j) is 𝒢\mathcal{G}-measurable for each jj and X​(ω)=fH​(ω,𝒥​(ω))X(\omega)=f\_{H}(\omega,\mathcal{J}(\omega)) for all ω∈Ω\omega\in\Omega. Then, setting
GjH≔{ω∈Ω:fH​(ω,j)=1}G^{H}\_{j}\coloneqq\{\omega\in\Omega:f\_{H}(\omega,j)=1\}, j∈ℕj\in\mathbb{N},
we have

|  |  |  |
| --- | --- | --- |
|  | X​(ω)=∑j∈ℕ𝟏H∩{𝒥=j}​(ω)andX​(ω)=∑j∈ℕfH​(ω,j)​𝟏{𝒥=j}​(ω)=∑j∈ℕ𝟏GjH∩{𝒥=j}​(ω),X(\omega)=\sum\_{j\in\mathbb{N}}\mathbf{1}\_{H\cap\{\mathcal{J}=j\}}(\omega)\quad\text{and}\quad X(\omega)=\sum\_{j\in\mathbb{N}}f\_{H}(\omega,j)\mathbf{1}\_{\{\mathcal{J}=j\}}(\omega)=\sum\_{j\in\mathbb{N}}\mathbf{1}\_{G^{H}\_{j}\cap\{\mathcal{J}=j\}}(\omega), |  |

because {𝒥=j}\{\mathcal{J}=j\}, j∈ℕj\in\mathbb{N}, is a partition of Ω\Omega. This completes the proof of the first statement.

Let us now prove the uniqueness. By assumption, we have GjH∩{𝒥=j}=LjH∩{𝒥=j}G^{H}\_{j}\cap\{\mathcal{J}=j\}=L^{H}\_{j}\cap\{\mathcal{J}=j\}, for all j∈ℕj\in\mathbb{N}.
Then, (GjH∖LjH)∩{𝒥=j}=∅\big(G^{H}\_{j}\setminus L^{H}\_{j}\big)\cap\{\mathcal{J}=j\}=\varnothing, for all j∈ℕj\in\mathbb{N}. By the independence of 𝒢\mathcal{G} and 𝒥\mathcal{J} we deduce

|  |  |  |
| --- | --- | --- |
|  | 0=𝖯​((GjH∖LjH)∩{𝒥=j})=𝖯​(GjH∖LjH)​𝖯​(𝒥=j)⟹𝖯​(GjH∖LjH)=0,0=\mathsf{P}\Big(\big(G^{H}\_{j}\setminus L^{H}\_{j}\big)\cap\{\mathcal{J}=j\}\Big)=\mathsf{P}\big(G^{H}\_{j}\setminus L^{H}\_{j}\big)\mathsf{P}(\mathcal{J}=j)\implies\mathsf{P}\big(G^{H}\_{j}\setminus L^{H}\_{j}\big)=0, |  |

and analogously

|  |  |  |
| --- | --- | --- |
|  | 0=𝖯​((LjH∖GjH)∩{𝒥=j})=𝖯​(LjH∖GjH)​𝖯​(𝒥=j)⟹𝖯​(LjH∖GjH)=0,0=\mathsf{P}\Big(\big(L^{H}\_{j}\setminus G^{H}\_{j}\big)\cap\{\mathcal{J}=j\}\Big)=\mathsf{P}\big(L^{H}\_{j}\setminus G^{H}\_{j}\big)\mathsf{P}(\mathcal{J}=j)\implies\mathsf{P}\big(L^{H}\_{j}\setminus G^{H}\_{j}\big)=0, |  |

for all j∈ℕj\in\mathbb{N}. Then the second claim holds.
∎

By an application of the above results we obtain the next two facts which are fundamental for our interpretation of the model in Section [5.1](https://arxiv.org/html/2510.15616v1#S5.SS1 "5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information"). In what follows we use the notation for filtrations 𝔽1\mathbb{F}^{1} and 𝔽2\mathbb{F}^{2} introduced in Section [5.1](https://arxiv.org/html/2510.15616v1#S5.SS1 "5.1. Partially observed scenarios ‣ 5. Applications to two classes of games ‣ Martingale theory for Dynkin games with asymmetric information").

###### Lemma E.3.

Let θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}) and recall the decomposition θ=∑j∈ℕθj​𝟏{𝒥=j}\theta=\sum\_{j\in\mathbb{N}}\theta\_{j}\mathbf{1}\_{\{\mathcal{J}=j\}}, where θj∈𝒯0​(𝔽2)\theta\_{j}\in\mathcal{T}\_{0}(\mathbb{F}^{2}) for each j∈ℕj\in\mathbb{N}. Then for any A∈ℱθ1A\in\mathcal{F}^{1}\_{\theta}, there are Fj∈ℱθj2F\_{j}\in\mathcal{F}^{2}\_{\theta\_{j}}, j∈ℕj\in\mathbb{N}, such that

|  |  |  |
| --- | --- | --- |
|  | A∩{𝒥=j}=Fj∩{𝒥=j},j∈ℕ.A\cap\{\mathcal{J}=j\}=F\_{j}\cap\{\mathcal{J}=j\},\qquad j\in\mathbb{N}. |  |

###### Proof.

Since A∈ℱθ1A\in\mathcal{F}^{1}\_{\theta}, we have A∈ℱT1A\in\mathcal{F}^{1}\_{T} with A∩{θ≤t}∈ℱt1A\cap\{\theta\leq t\}\in\mathcal{F}^{1}\_{t} for all t≥0t\geq 0. Lemma [E.2](https://arxiv.org/html/2510.15616v1#A5.Thmtheorem2 "Lemma E.2. ‣ Appendix E Technical results for partially observed scenarios ‣ Martingale theory for Dynkin games with asymmetric information") guarantees that for every j∈ℕj\in\mathbb{N} and every t≥0t\geq 0, there is Fjt∈ℱt2F^{t}\_{j}\in\mathcal{F}^{2}\_{t} such that

|  |  |  |
| --- | --- | --- |
|  | (A∩{θ≤t})∩{𝒥=j}=(A∩{θj≤t})∩{𝒥=j}=Fjt∩{𝒥=j}.\big(A\cap\{\theta\leq t\}\big)\cap\{\mathcal{J}=j\}=\big(A\cap\{\theta\_{j}\leq t\}\big)\cap\{\mathcal{J}=j\}=F^{t}\_{j}\cap\{\mathcal{J}=j\}. |  |

Since all our stopping times are bounded by TT, the above equation implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | A∩{𝒥=j}\displaystyle A\cap\{\mathcal{J}=j\} | =(A∩{θ≤T})∩{𝒥=j}\displaystyle=\big(A\cap\{\theta\leq T\}\big)\cap\{\mathcal{J}=j\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(A∩{θj≤T})∩{𝒥=j}=Fj∩{𝒥=j},∀j∈ℕ\displaystyle=\big(A\cap\{\theta\_{j}\leq T\}\big)\cap\{\mathcal{J}=j\}=F\_{j}\cap\{\mathcal{J}=j\},\quad\forall j\in\mathbb{N} |  |

with Fj∈ℱT2F\_{j}\in\mathcal{F}^{2}\_{T}. However, the equations above yield for any t≥0t\geq 0

|  |  |  |
| --- | --- | --- |
|  | Fj∩{θj≤t}∩{𝒥=j}=A∩{θj≤t}∩{𝒥=j}=Fjt∩{𝒥=j}.\displaystyle F\_{j}\cap\{\theta\_{j}\leq t\}\cap\{\mathcal{J}=j\}=A\cap\{\theta\_{j}\leq t\}\cap\{\mathcal{J}=j\}=F^{t}\_{j}\cap\{\mathcal{J}=j\}. |  |

The uniqueness result in Lemma [E.2](https://arxiv.org/html/2510.15616v1#A5.Thmtheorem2 "Lemma E.2. ‣ Appendix E Technical results for partially observed scenarios ‣ Martingale theory for Dynkin games with asymmetric information") guarantees that the symmetric difference (Fj∩{θj≤t})​△​Fjt\big(F\_{j}\cap\{\theta\_{j}\leq t\}\big)\triangle F^{t}\_{j} is a 𝖯\mathsf{P}-null set. Hence, Fj∩{θj≤t}∈ℱt2F\_{j}\cap\{\theta\_{j}\leq t\}\in\mathcal{F}^{2}\_{t} by the completeness of the filtration 𝔽2\mathbb{F}^{2} and, since the inclusion holds for any t≥0t\geq 0, we have Fj∈ℱθj2F\_{j}\in\mathcal{F}^{2}\_{\theta\_{j}}.
∎

###### Lemma E.4.

Assume that ZZ is ℱT2\mathcal{F}^{2}\_{T}-measurable and integrable. Then, for any θ∈𝒯0​(𝔽1)\theta\in\mathcal{T}\_{0}(\mathbb{F}^{1}), recalling the decomposition θ=∑j∈ℕθj​𝟏{𝒥=j}\theta=\sum\_{j\in\mathbb{N}}\theta\_{j}\mathbf{1}\_{\{\mathcal{J}=j\}} for θj∈𝒯0​(𝔽2)\theta\_{j}\in\mathcal{T}\_{0}(\mathbb{F}^{2}), we have

|  |  |  |  |
| --- | --- | --- | --- |
| (E.1) |  | 𝖤​[Z|ℱθ1]=∑j∈ℕ𝖤​[Z|ℱθj2]​𝟏{𝒥=j}.\mathsf{E}[Z|\mathcal{F}^{1}\_{\theta}]=\sum\_{j\in\mathbb{N}}\mathsf{E}[Z|\mathcal{F}^{2}\_{\theta\_{j}}]\mathbf{1}\_{\{\mathcal{J}=j\}}. |  |

Consequently, for any ℱT1\mathcal{F}^{1}\_{T}-measurable and integrable Z^\hat{Z} with the decomposition Z^=∑j∈ℕ𝟏{𝒥=j}​Zj\hat{Z}=\sum\_{j\in\mathbb{N}}\mathbf{1}\_{\{\mathcal{J}=j\}}Z\_{j} and ℱT2\mathcal{F}^{2}\_{T}-measurable ZjZ\_{j}, we have

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[Z^|ℱθ1]=∑j∈ℕ𝖤​[Zj|ℱθj2]​𝟏{𝒥=j}.\mathsf{E}[\hat{Z}|\mathcal{F}^{1}\_{\theta}]=\sum\_{j\in\mathbb{N}}\mathsf{E}[Z\_{j}|\mathcal{F}^{2}\_{\theta\_{j}}]\mathbf{1}\_{\{\mathcal{J}=j\}}. |  |

###### Proof.

We need to show that the expectations of the left and right-hand sides of ([E.1](https://arxiv.org/html/2510.15616v1#A5.E1 "In Lemma E.4. ‣ Appendix E Technical results for partially observed scenarios ‣ Martingale theory for Dynkin games with asymmetric information")) multiplied by the indicator function of any set A∈ℱθ1A\in\mathcal{F}^{1}\_{\theta} are identical. Take A∈ℱθ1A\in\mathcal{F}^{1}\_{\theta}. By Lemma [E.3](https://arxiv.org/html/2510.15616v1#A5.Thmtheorem3 "Lemma E.3. ‣ Appendix E Technical results for partially observed scenarios ‣ Martingale theory for Dynkin games with asymmetric information"), it has a representation A∩{𝒥=j}=Fj∩{𝒥=j}A\cap\{\mathcal{J}=j\}=F\_{j}\cap\{\mathcal{J}=j\} for some Fj∈ℱθj2F\_{j}\in\mathcal{F}^{2}\_{\theta\_{j}}, j∈ℕj\in\mathbb{N}. We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤​[𝟏A​∑j∈ℕ𝖤​[Z|ℱθj2]​𝟏{𝒥=j}]\displaystyle\mathsf{E}\Big[\mathbf{1}\_{A}\sum\_{j\in\mathbb{N}}\mathsf{E}[Z|\mathcal{F}^{2}\_{\theta\_{j}}]\mathbf{1}\_{\{\mathcal{J}=j\}}\Big] | =𝖤​[∑j∈ℕ𝖤​[Z|ℱθj2]​𝟏Fj​𝟏{𝒥=j}]=∑j∈ℕ𝖤​[𝖤​[Z​𝟏Fj|ℱθj2]​𝟏{𝒥=j}]\displaystyle=\mathsf{E}\Big[\sum\_{j\in\mathbb{N}}\mathsf{E}[Z|\mathcal{F}^{2}\_{\theta\_{j}}]\mathbf{1}\_{F\_{j}}\mathbf{1}\_{\{\mathcal{J}=j\}}\Big]=\sum\_{j\in\mathbb{N}}\mathsf{E}\big[\mathsf{E}[Z\mathbf{1}\_{F\_{j}}|\mathcal{F}^{2}\_{\theta\_{j}}]\mathbf{1}\_{\{\mathcal{J}=j\}}\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j∈ℕ𝖤​[Z​𝟏Fj]​𝖯​(𝒥=j)=𝖤​[∑j∈ℕZ​𝟏Fj​𝟏{𝒥=j}]\displaystyle=\sum\_{j\in\mathbb{N}}\mathsf{E}[Z\mathbf{1}\_{F\_{j}}]\mathsf{P}(\mathcal{J}=j)=\mathsf{E}\Big[\sum\_{j\in\mathbb{N}}Z\mathbf{1}\_{F\_{j}}\mathbf{1}\_{\{\mathcal{J}=j\}}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝖤​[Z​𝟏A]=𝖤​[𝖤​[Z|ℱθ1]​𝟏A],\displaystyle=\mathsf{E}[Z\mathbf{1}\_{A}]=\mathsf{E}\big[\mathsf{E}[Z|\mathcal{F}^{1}\_{\theta}]\mathbf{1}\_{A}\big], |  |

where in the third and fourth equality we used the independence of ℱT2\mathcal{F}^{2}\_{T} from 𝒥\mathcal{J}.

For the second statement, we write

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[Z^|ℱθ1]=∑j∈ℕ𝟏{𝒥=j}​𝖤​[Zj|ℱθ1]=∑j∈ℕ𝟏{𝒥=j}​∑i∈ℕ𝟏{𝒥=i}​𝖤​[Zj|ℱθi2]=∑j∈ℕ𝟏{𝒥=j}​𝖤​[Zj|ℱθj2]\mathsf{E}[\hat{Z}|\mathcal{F}^{1}\_{\theta}]=\sum\_{j\in\mathbb{N}}\mathbf{1}\_{\{\mathcal{J}=j\}}\mathsf{E}[Z\_{j}|\mathcal{F}^{1}\_{\theta}]=\sum\_{j\in\mathbb{N}}\mathbf{1}\_{\{\mathcal{J}=j\}}\sum\_{i\in\mathbb{N}}\mathbf{1}\_{\{\mathcal{J}=i\}}\mathsf{E}[Z\_{j}|\mathcal{F}^{2}\_{\theta\_{i}}]=\sum\_{j\in\mathbb{N}}\mathbf{1}\_{\{\mathcal{J}=j\}}\mathsf{E}[Z\_{j}|\mathcal{F}^{2}\_{\theta\_{j}}] |  |

with the second equality justified by the first part of the lemma.
∎

## References

* [Bal17]

  P. Baldi.
  Stochastic calculus.
  Springer, 2017.
* [BF74]

  A. Bensoussan and A. Friedman.
  Nonlinear variational inequalities and differential games with
  stopping times.
  J. Funct. Anal., 16(3):305–352, 1974.
* [BFR25]

  L. Baňas, G. Ferrari, and T.A. Randrianasolo.
  Numerical approximation of Dynkin games with asymmetric
  information.
  SIAM J. Control Optim., 63(1):256–291, 2025.
* [Bil95]

  P. Billingsley.
  Probability and Measure.
  John Wiley & Sons Inc, 3 edition, 1995.
* [Bis77]

  J.-M. Bismut.
  Sur un problème de Dynkin.
  Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte
  Gebiete, 39(1):31–53, 1977.
* [CL24]

  S. Christensen and K. Lindensjö.
  General Markovian randomized equilibrium existence and construction
  in zero-sum Dynkin games for diffusions.
  arXiv:2412.09087, 2024.
* [CR09]

  P. Cardaliaguet and C. Rainer.
  Stochastic differential games with asymmetric information.
  Appl. Math. Optim., 59(1):1–36, 2009.
* [CS24]

  S. Christensen and B. Schultz.
  On the existence of Markovian randomized equilibria in Dynkin
  games of war-of-attrition-type.
  arXiv:2406.09820, 2024.
* [DAEG22]

  T. De Angelis, E. Ekström, and K. Glover.
  Dynkin games with incomplete and asymmetric information.
  Math. Oper. Res., 47(1):560–586, 2022.
* [DAGV21]

  T. De Angelis, F. Gensbittel, and S. Villeneuve.
  A Dynkin game on assets with incomplete information on the return.
  Math. Oper. Res., 46(1):28–60, 2021.
* [DAHP25]

  T. De Angelis, D. Hobson, and J. Palczewski.
  A Dynkin game with foresight.
  preprint, 2025.
* [DAMP22]

  T. De Angelis, N. Merkulov, and J. Palczewski.
  On the value of non-Markovian Dynkin games with partial and
  asymmetric information.
  Ann. Appl. Probab., 32(3):1774–1813, 2022.
* [DGM22]

  J.-P. Décamps, F. Gensbittel, and T. Mariotti.
  Mixed-strategy equilibria in the war of attrition under uncertainty.
  arXiv:2210.08848, 2022.
* [DGM24]

  J.-P. Décamps, F. Gensbittel, and T. Mariotti.
  Mixed Markov-perfect equilibria in the continuous-time war of
  attrition.
  arXiv:2407.04878, 2024.
* [DM78]

  C. Dellacherie and P.-A. Meyer.
  Probabilities and Potential.
  North-Holland Publishing Company, 1978.
* [DM83]

  C. Dellacherie and P.-A. Meyer.
  Probabilities and Potential B. Theory of Martingales.
  North-Holland Mathematics Studies 72, Elsevier Science, 1983.
* [Dom02]

  V.K. Domansky.
  Randomized optimal stopping times for a class of stopping games.
  Theory Probab. Appl., 46(4):708–717, 2002.
* [Dyn69]

  E.B. Dynkin.
  Game variant of a problem on optimal stopping.
  Soviet Math. Dokl., 10:270–274, 1969.
* [EI18]

  N. Esmaeeli and P. Imkeller.
  American options with asymmetric information and reflected BSDE.
  Bernoulli, 24(2):1394–1426, 2018.
* [EK81]

  N. El Karoui.
  Les Aspects Probabilistes Du Controle Stochastique.
  Springer Berlin Heidelberg, 1981.
* [EP08]

  E. Ekström and G. Peskir.
  Optimal stopping games for Markov processes.
  SIAM J. Control Optim., 47(2):684–702, 2008.
* [EV06]

  E. Ekström and S. Villeneuve.
  On the value of optimal stopping games.
  Ann. Appl. Probab., 16(3):1576–1596, 2006.
* [GG19]

  F. Gensbittel and C. Grün.
  Zero-sum stopping games with asymmetric information.
  Math. Oper. Res., 44(1):277–302, 2019.
* [Grü13]

  C. Grün.
  On Dynkin games with incomplete information.
  SIAM J. Control Optim., 51(5):4039–4065, 2013.
* [Hal74]

  P.R. Halmos.
  Measure theory.
  Springer-Verlag New York, 1974.
* [HL00]

  S. Hamadène and J.-P. Lepeltier.
  Reflected BSDEs and mixed game problem.
  Stochastic Process. Appl., 85(2):177–188, 2000.
* [IW81]

  N. Ikeda and S. Watanabe.
  Stochastic differential equations and diffusion processes,
  volume 24 of North-Holland Mathematical Library.
  North-Holland Publishing Co., Amsterdam, 1981.
* [Kal02]

  O. Kallenberg.
  Foundations of modern probability.
  Probability and its Applications (New York). Springer-Verlag, New
  York, second edition, 2002.
* [Kif71]

  Y. Kifer.
  Optimal stopping games.
  Theory Probab. Appl., 16:185–189, 1971.
* [Kif00]

  Y. Kifer.
  Game options.
  Finance Stoch., 4(4):443–463, 2000.
* [KP24]

  H.D. Kwon and J. Palczewski.
  Exit game with private information.
  Math. Oper. Res., 2024.
* [KS98a]

  I. Karatzas and S.E. Shreve.
  Brownian Motion and Stochastic Calculus.
  Springer, 1998.
* [KS98b]

  I. Karatzas and S.E. Shreve.
  Methods of Mathematical Finance.
  Springer-Verlag New York, 1998.
* [LM84]

  J.P Lepeltier and E.M. Maingueneau.
  Le jeu de Dynkin en théorie générale sans
  l’hypothèse de Mokobodski.
  Stochastics, 13(1-2):25–44, 1984.
* [LS05]

  R. Laraki and E. Solan.
  The value of zero-sum stopping games in continuous time.
  SIAM J. Control Optim., 43(5):1913–1922, 2005.
* [Nev75]

  J. Neveu.
  Discrete-parameter martingales.
  North-Holland Publishing Company, Amsterdam, 1975.
* [Pro05]

  P.E. Protter.
  Stochastic integration and differential equations.
  Springer, 2005.
* [RSV01]

  D. Rosenberg, E. Solan, and N. Vieille.
  Stopping games with randomized strategies.
  Probab. Theory Related Fields, 119(3):433–451, 2001.
* [RW00]

  L.C.G. Rogers and D. Williams.
  Diffusions, Markov Processes and Martingales, volume 2.
  Cambridge University Press, 2 edition, 2000.
* [RY99]

  D. Revuz and M. Yor.
  Continuous Martingales and Brownian Motion.
  Springer-Verlag Berlin Heidelberg, 1999.
* [Smi24]

  J.E. Smith.
  A Martingale Theory for a Class of Dynkin Games with Asymmetric
  Information.
  PhD thesis, University of Leeds, 2024.
* [Ste82]

  Ł. Stettner.
  Zero-sum Markov games with stopping and impulsive strategies.
  Appl. Math. Optim., 9(1):1–24, 1982.
* [TV02]

  N. Touzi and N. Vieille.
  Continuous-time Dynkin games with mixed strategies.
  SIAM J. Control Optim., 41(4):1073–1088, 2002.
* [Wil91]

  D. Williams.
  Probability with martingales.
  Cambridge University Press, 1991.
* [Yas85]

  M. Yasuda.
  On a randomized strategy in Neveu’s stopping problem.
  Stoch. Process. Appl., 21(1):159–166, 1985.