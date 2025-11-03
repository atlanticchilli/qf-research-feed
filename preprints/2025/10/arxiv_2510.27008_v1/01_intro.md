---
authors:
- Fabian Raoul Pieroth
- Ole Petersen
- Martin Bichler
doc_id: arxiv:2510.27008v1
family_id: arxiv:2510.27008
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Algorithmic Predation: Equilibrium Analysis in Dynamic Oligopolies with Smooth
  Market Sharing'
url_abs: http://arxiv.org/abs/2510.27008v1
url_html: https://arxiv.org/html/2510.27008v1
venue: arXiv q-fin
version: 1
year: 2025
---


[![[Uncaptioned image]](x1.png) Fabian R. Pieroth](https://orcid.org/0000-0002-5712-1706)
fabian.pieroth@tum.de
School of Computation, Information and Technology,
Technical University of Munich,
Munich, Germany
These authors contributed equally to this work.

[![[Uncaptioned image]](x2.png) Ole Petersen](https://orcid.org/0009-0005-7099-5685)
ole.petersen@tum.de
School of Computation, Information and Technology,
Technical University of Munich,
Munich, Germany
Listen Labs, San Francisco, CA, US

[![[Uncaptioned image]](x3.png) Martin Bichler](https://orcid.org/0000-0001-5491-2935)
bichler@cit.tum.de
School of Computation, Information and Technology,
Technical University of Munich,
Munich, Germany

###### Abstract

Predatory pricing – where a firm strategically lowers prices to undermine competitors – is a contentious topic in dynamic oligopoly theory, with scholars debating practical relevance and the existence of predatory equilibria. Although finite-horizon dynamic models have long been proposed to capture the strategic intertemporal incentives of oligopolists, the existence and form of equilibrium strategies in settings that allow for firm exit (drop-outs following loss-making periods) have remained an open question. We focus on the seminal dynamic oligopoly model by Selten (1965) that introduces the subgame perfect equilibrium and analyzes smooth market sharing. Equilibrium can be derived analytically in models that do not allow for dropouts, but not in models that can lead to predatory pricing. In this paper, we leverage recent advances in deep reinforcement learning to compute and verify equilibria in finite-horizon dynamic oligopoly games.
Our experiments reveal two key findings: first, state-of-the-art deep reinforcement learning algorithms reliably converge to equilibrium in both perfect- and imperfect-information oligopoly models; second, when firms face asymmetric cost structures, the resulting equilibria exhibit predatory pricing behavior. These results demonstrate that predatory pricing can emerge as a rational equilibrium strategy across a broad variety of model settings. By providing equilibrium analysis of finite-horizon dynamic oligopoly models with drop-outs, our study answers a decade-old question and offers new insights for competition authorities and regulators.

*Keywords* predatory prcing ⋅\cdot
oligopoly ⋅\cdot
dynamic game ⋅\cdot
equilibrium learning

## 1 Introduction

Predatory pricing is loosely defined as a firm’s deliberate reduction of prices to levels that, while not necessarily below cost, are unsustainable for potential or existing competitors in the long run.
In dynamic oligopoly competition, the strategic behavior associated with predatory pricing manifests as a dominant player systematically lowering prices to deter entry or push competitors out of the market (Gates et al., [1995](https://arxiv.org/html/2510.27008v1#bib.bib1)).

Antitrust laws, such as the Sherman Antitrust Act in the U.S. and Article 102 of the Treaty on the Functioning of the European Union (TFEU), address abusive practices like predatory pricing. For example, Article 102 of the TFEU prohibits a dominant firm from ”directly or indirectly imposing unfair purchase or selling prices.”
However, whether predatory pricing is a concern in practice has long been controversial.
DiLorenzo ([1992](https://arxiv.org/html/2510.27008v1#bib.bib2)) argues that while a firm might be able to successfully price other firms out of the market, there is no evidence to support the theory that the virtual monopoly could then raise prices. Also, courts have been skeptical of predatory pricing claims. For example, the U.S. Supreme Court has set high hurdles to antitrust claims based on predatory pricing theory (May, [1994](https://arxiv.org/html/2510.27008v1#bib.bib3)). On the other hand, the US Department of Justice argues that predatory pricing is a real problem, courts are out of date, and too skeptical (Bolton et al., [1999](https://arxiv.org/html/2510.27008v1#bib.bib4)).
Predatory pricing has received renewed attention due to the presence of automated pricing agents in legal studies (Leslie, [2023](https://arxiv.org/html/2510.27008v1#bib.bib5); Cheng and Nowag, [2023](https://arxiv.org/html/2510.27008v1#bib.bib6)). Although a considerable body of scholarship aims to explain how algorithms can collude to fix prices (Bichler et al., [2025](https://arxiv.org/html/2510.27008v1#bib.bib7)), almost no literature discusses anti-competitive behavior of algorithmic agents in the form of predatory pricing.

In this article, we address two related problems:
First, can we expect algorithmic pricing agents in a dynamic or multi-stage oligopoly model to converge to an equilibrium? We focus on state-of-the-art deep reinforcement learning (DRL) algorithms as they constitute prime candidates for pricing agents in the field (Deng et al., [2024](https://arxiv.org/html/2510.27008v1#bib.bib8)). Convergence to an equilibrium is far from obvious, because we know that learning algorithms do not converge to equilibrium even in simple static games (Sanders et al., [2018](https://arxiv.org/html/2510.27008v1#bib.bib9)). Even less is known for multi-stage games. We draw on a recent approach to verify whether a strategy profile resulting from the interaction of DRL agents is a Nash equilibrium (Pieroth et al., [2025](https://arxiv.org/html/2510.27008v1#bib.bib10)). Second, we aim to understand in which environments we can expect a predatory equilibrium to emerge, and when this is not the case.

### 1.1 Dynamic Oligopoly Competition

Dynamic oligopoly models are well-suited to study predatory pricing, as firms interact over discrete time, repeatedly setting prices. Current choices influence future outcomes through mechanisms like demand inertia or strategic responses (Milgrom, [1990](https://arxiv.org/html/2510.27008v1#bib.bib11)). Firms must be able to accumulate revenue over time, enabling recoupment of early losses, and must have the option to exit, drop out, or withdraw from the market to avoid further losses (Telser, [1966](https://arxiv.org/html/2510.27008v1#bib.bib12)).

These interactions are often modeled as infinite-horizon stochastic games, where the Nash equilibrium (NE) (Nash, [1950](https://arxiv.org/html/2510.27008v1#bib.bib13)) serves as the primary solution concept. Assuming complete information, these models can be solved using dynamic programming techniques, resulting in Markov Perfect Equilibria (MPE), a refinement of the NE (Maskin and Tirole, [1988](https://arxiv.org/html/2510.27008v1#bib.bib14)). Previous literature showed the existence of MPEs displaying predatory behavior due to evasion of fixed costs or competitive advantage (Cabral and Riordan, [1994](https://arxiv.org/html/2510.27008v1#bib.bib15); Besanko et al., [2011](https://arxiv.org/html/2510.27008v1#bib.bib16); Rey et al., [2022](https://arxiv.org/html/2510.27008v1#bib.bib17)).

Markov perfect equilibria (MPE) are not stable to small changes in payoffs and can shift discontinuously (Fudenberg and Kreps, [1993](https://arxiv.org/html/2510.27008v1#bib.bib18), 518). Closed-form solutions are rare; instead, dynamic programming methods are used (Pakes and McGuire, [1992](https://arxiv.org/html/2510.27008v1#bib.bib19)), though convergence is not guaranteed and multiple MPEs may exist. By excluding history-dependent strategies, MPEs can miss key dynamics in settings with learning or private information.
These methods also face practical limits: they require discrete state and action spaces, full observability, and are difficult to extend to continuous or imperfect-information environments without high computational cost.

Deep reinforcement learning (DRL) methods such as PPO (Schulman et al., [2017](https://arxiv.org/html/2510.27008v1#bib.bib20)) can handle continuous action and state spaces, as well as imperfect information. Pieroth et al. ([2025](https://arxiv.org/html/2510.27008v1#bib.bib10)) use DRL with self-play to learn candidate equilibria in multi-stage games, verifying convergence to a Nash equilibrium ex-post. These techniques constitute a breakthrough as they allow for equilibrium computation in finite-horizon, dynamic game-theoretical models. We build on this framework and present its first application for equilibrium analysis in dynamic oligopoly models.

### 1.2 Contributions

We study the dynamic oligopoly model of Selten ([1965](https://arxiv.org/html/2510.27008v1#bib.bib21)), where NN firms produce a homogeneous good over a finite horizon TT ([Section˜3.2](https://arxiv.org/html/2510.27008v1#S3.SS2 "3.2 Dynamic oligopoly model ‣ 3 The Model ‣ Algorithmic Predation: Equilibrium Analysis in Dynamic Oligopolies with Smooth Market Sharing")). Firms set prices from an interval, and market shares (demands) evolve based on price differences relative to the market average. This demand inertia – capturing brand loyalty, switching costs, or network effects (Besanko et al., [2011](https://arxiv.org/html/2510.27008v1#bib.bib16)) – leads to *smooth market sharing*, where small price cuts yield small market share gains. Unlike Bertrand competition (Bertrand, [1883](https://arxiv.org/html/2510.27008v1#bib.bib22)), this avoids the paradox of prices being driven to marginal cost. Selten’s model yields more realistic pricing dynamics and has become influential for analyzing industries with limited price responsiveness, such as gasoline retail, banking, and telecommunications.

We compare two market models: firms either exit the market if unprofitable, like in contestable markets with a low barrier to entry, or persist despite losses. The model by Selten ([1965](https://arxiv.org/html/2510.27008v1#bib.bib21)) does not allow for dropouts, which are central to the analysis of predatory prices. The model with dropouts could lead to predatory pricing, where surviving firms capture increased market share and charge higher prices. However, if this can happen in equilibrium in a finite-horizon model is unkown. Although models with dropouts have been discussed (Bylka et al., [2000](https://arxiv.org/html/2510.27008v1#bib.bib23)), this feature of the model is known to make the equilibrium analysis challenging. Each additional state grows the state space and numerical methods based on dynamic programming become very slow.

We examine two information settings: in the perfect-information case, firms observe all demands after each round; in the imperfect-information case, they only observe current demand. This reflects real-world differences across markets, such as high transparency in gasoline or financial markets (Assad et al., [2020](https://arxiv.org/html/2510.27008v1#bib.bib24); Madhavan, [2000](https://arxiv.org/html/2510.27008v1#bib.bib25)) versus limited visibility in airlines or manufacturing (Escobari and Lee, [2014](https://arxiv.org/html/2510.27008v1#bib.bib26)). While Selten ([1965](https://arxiv.org/html/2510.27008v1#bib.bib21)) solved the perfect-information case without dropouts, we provide an analytical characterization of the Nash equilibrium under imperfect information without dropouts. No analytical solution exists when dropouts are allowed.

We draw on the framework by Pieroth et al. ([2025](https://arxiv.org/html/2510.27008v1#bib.bib10)) to compute a candidate approximate equilibrium strategy using Deep Reinforcement Learning (DRL), which is verified ex-post to confirm that it is indeed an approximate Nash equilibrium. These equilibrium guarantees are central to deep equlibrium learning and they allow us to verify Nash equilibria in finite-horizon games. The types of dynamic finite-horizon models in this paper could not be solved so far.

This paper is the first application of deep equilibrium learning techniques in dynamic oligopolies leading to novel and policy-relevant insights. In particular, we show that predatory pricing arises as an equilibrium strategy in a wide variety of settings when firms can exit the market. That predatory pricing is possible in finite-horizon dynamic oligopoly competition models wtih continuous actions was an open question and we provide an affirmative answer to this policy-relevant question.

The welfare analysis yields some counterintuitive results. While competition increases welfare in standard Bertrand oligopolies, this is not necessarily the case with smooth market sharing by Selten ([1965](https://arxiv.org/html/2510.27008v1#bib.bib21)). Specifically, we find that predatory behavior leading to competitor exit can, under certain conditions, improve overall welfare. This occurs because the short-term aggressive pricing during predation often outweighs the subsequent higher prices during the recoupment phase. Additionally, exits typically involve less efficient firms, thereby raising market efficiency. These results challenge traditional antitrust perspectives, indicating that reductions in competition might somemathptmxyield welfare benefits, particularly when balanced against short recoupment windows and efficiency gains from market exits.

## 2 Related work

This section reviews related work on equilibrium analysis and learning dynamics in dynamic oligopoly models.
Dynamic oligopoly markets have been studied extensively in the literature (Fudenberg and Tirole, [2013](https://arxiv.org/html/2510.27008v1#bib.bib27); Gerpott and Berends, [2022](https://arxiv.org/html/2510.27008v1#bib.bib28)).

A foundational dynamic oligopoly model was introduced by Selten ([1965](https://arxiv.org/html/2510.27008v1#bib.bib21)), who considered price competition with discrete time steps, finite horizon, complete information, and continuous demand. Selten explicitly characterized a deterministic subgame perfect equilibrium in a finite-horizon complete-information game, which was influential for subsequent analyses (Phlips and Richard, [1989](https://arxiv.org/html/2510.27008v1#bib.bib29); Farrell and Shapiro, [1988](https://arxiv.org/html/2510.27008v1#bib.bib30); Bayer and Chan, [2007](https://arxiv.org/html/2510.27008v1#bib.bib31)).
We extend his work and derive an equilibrium considering also imperfect information of firms.

Maskin and Tirole ([1988](https://arxiv.org/html/2510.27008v1#bib.bib14)) proposed an infinite-horizon model with alternating moves to study dynamic oligopolies, which focuses on long-run strategic considerations.
Several studies addressed predatory pricing within dynamic oligopolies in this framework (Cabral and Riordan, [1994](https://arxiv.org/html/2510.27008v1#bib.bib15); Besanko et al., [2014](https://arxiv.org/html/2510.27008v1#bib.bib32); Rey et al., [2022](https://arxiv.org/html/2510.27008v1#bib.bib17)). Despite their insights, these models often rely on strong assumptions, such as independent stage-wise demand, finite pay-off structures, or limited action spaces, limiting their ability to capture dynamic pricing behaviors. In contrast, our model incorporates interdependent demand and allows for continuous prices, enabling richer strategic patterns.

Finite-horizon models are arguably a good fit for the analysis of predatory pricing, as the strategic analysis of firms rarely considers an infinite horizon. They are less sensitive to discount factors or changes in the parameters of the game and an important complement to infinite-horizon and perfect-information models, for which numerical methods such as value function iteration have been available for a long time (Pakes and McGuire, [1992](https://arxiv.org/html/2510.27008v1#bib.bib19)). However, solving finite-horizon models is challenging. Bylka et al. ([2000](https://arxiv.org/html/2510.27008v1#bib.bib23)) introduced dropout mechanisms, creating strategic discontinuities, which evaded equilibrium analysis so far.
Furthermore, as the state space grows, numerical methods based on dynamic programming become slow quickly. Our approach, employing DRL, provides a way to find equilibrium even if the model allows dropouts, continuous actions, and states.

Equilibrium learning offers an alternative numerical approach to finding equilibrium. It explores how equilibrium can emerge from agents that maximize their payoff while competing with each other (Fudenberg and Levine, [1999](https://arxiv.org/html/2510.27008v1#bib.bib33)). Almost the entire literature is focused on static, complete-information games. Unfortunately, learning dynamics does not necessarily converge to a Nash equilibrium (Milionis et al., [2023](https://arxiv.org/html/2510.27008v1#bib.bib34); Mazumdar et al., [2020](https://arxiv.org/html/2510.27008v1#bib.bib35); Daskalakis et al., [2010](https://arxiv.org/html/2510.27008v1#bib.bib36)).
Several recent studies have demonstrated the convergence of learning algorithms to equilibrium in static auction and oligopoly pricing models (Bichler et al., [2023](https://arxiv.org/html/2510.27008v1#bib.bib37); Şeref Ahunbay and
Bichler, [2024](https://arxiv.org/html/2510.27008v1#bib.bib38)).

We build our study on a new methodology recently introduced by Pieroth et al. ([2025](https://arxiv.org/html/2510.27008v1#bib.bib10)). They use deep [reinforcement learning](https://arxiv.org/html/2510.27008v1#id1) ([RL](https://arxiv.org/html/2510.27008v1#id1)) agents in self-play to compute candidate equilibrium profiles in multi-stage games with a finite horizon and continuous observations and actions. Importantly, they propose a verification algorithm that provides an upper bound on the computed candidate’s distance to equilibrium. This enables an ex-post verification of the learned strategies, offering guarantees even when there are none about convergence a priori.
We extend their work by studying dynamic oligopoly markets and computing novel approximate equilibrium strategies under various information structures and market rules. Additionally, we derive a novel equilibrium analytically, further contributing to the understanding of strategic behavior in these complex environments. This is the first work analyzing dynamic oligopoly models with this new equilibrium learning approach.

## 3 The Model

We first outline the formal framework for [multi-agent reinforcement learning](https://arxiv.org/html/2510.27008v1#id6) ([MARL](https://arxiv.org/html/2510.27008v1#id6)) and a suitable solution concept. Afterward, we introduce the dynamic oligopoly model considered.

### 3.1 Partially observable Markov games

We model the dynamic oligopoly as a [partially observable Markov game](https://arxiv.org/html/2510.27008v1#id4) ([POMG](https://arxiv.org/html/2510.27008v1#id4)), a generalization of a [partially observable Markov decision process](https://arxiv.org/html/2510.27008v1#id3) ([POMDP](https://arxiv.org/html/2510.27008v1#id3)) for multiple agents (Albrecht et al., [2024](https://arxiv.org/html/2510.27008v1#bib.bib39), Chapter 3.4).
Formally, a [POMG](https://arxiv.org/html/2510.27008v1#id4) is a tuple ⟨𝒮,𝒜,𝒯,𝒩,𝐫,T,O,𝚽,μ⟩\langle\mathcal{S},\mathcal{A},\mathcal{T},\mathcal{N},\mathbf{r},T,O,\mathbf{\Phi},\mu\rangle. Agents i∈𝒩={1,…,N}i\in\mathcal{N}=\{1,\ldots,N\} collectively interact with an environment described by its state st∈𝒮s\_{t}\in\mathcal{S} at time tt. In each timestep, agents receive an observation oti=Φi​(st)o\_{t}^{i}=\Phi\_{i}(s\_{t}) with oti∈Oio\_{t}^{i}\in O\_{i} and O=×i∈𝒩OiO=\times\_{i\in\mathcal{N}}O\_{i}. Subsequently, they choose an action ati∈𝒜ia\_{t}^{i}\in\mathcal{A}\_{i} according to their policy (or strategy) πi:Oi→Δ​(𝒜i)\pi\_{i}:O\_{i}\rightarrow\Delta(\mathcal{A}\_{i}), where 𝒜=×i∈𝒩𝒜i\mathcal{A}=\times\_{i\in\mathcal{N}}\mathcal{A}\_{i} and Δ​(X)\Delta(X) is the set of probability distributions over a set XX. We denote the set of agent ii’s policies by Σi={πi|πi:Oi→Δ​(𝒜i)}\Sigma\_{i}=\left\{\pi\_{i}|\pi\_{i}:O\_{i}\rightarrow\Delta(\mathcal{A}\_{i})\right\}. A policy is deterministic if it maps each observation otio\_{t}^{i} on a specific action ati∈𝒜ia\_{t}^{i}\in\mathcal{A}\_{i}. The environment transitions to a new state st+1∼𝒯​(st,at1,…,atN)s\_{t+1}\sim\mathcal{T}(s\_{t},a\_{t}^{1},\ldots,a\_{t}^{N}) and rewards each agent ii with rti=ri​(st,at1,…,atN,st+1)r\_{t}^{i}=r\_{i}(s\_{t},a\_{t}^{1},\ldots,a\_{t}^{N},s\_{t+1}). The goal of each agent is to maximize its expected cumulative reward or utility Ui​(π1,…,πN)=𝔼​[∑t=1Trti]U\_{i}(\pi\_{1},\ldots,\pi\_{N})=\mathbb{E}\left[\sum\_{t=1}^{T}r\_{t}^{i}\right]. The game starts in an initial state s1∼μs\_{1}\sim\mu and ends after TT timesteps.

We want to find an (approximate) [Nash equilibrium](https://arxiv.org/html/2510.27008v1#id5) ([NE](https://arxiv.org/html/2510.27008v1#id5)). A set of policies (also called strategy profile) π𝒩∗≡{π1∗,…,πN∗}\pi^{\*}\_{\mathcal{N}}\equiv\{\pi^{\*}\_{1},\ldots,\pi^{\*}\_{N}\} is a ε\varepsilon-NE of a [POMG](https://arxiv.org/html/2510.27008v1#id4) if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπi∈ΣiUi​(πi,π−i∗)−Ui​(π𝒩∗)≤ε∀i∈𝒩,\displaystyle\sup\_{\pi\_{i}\in\Sigma\_{i}}U\_{i}(\pi\_{i},\pi^{\*}\_{-i})-U\_{i}(\pi^{\*}\_{\mathcal{N}})\leq\varepsilon\quad\forall i\in\mathcal{N}, |  | (1) |

where π−i≡π𝒩∖{i}\pi\_{-i}\equiv\pi\_{\mathcal{N}\setminus\{i\}}. The strategy profile π∗\pi^{\*} is denoted simply as a [NE](https://arxiv.org/html/2510.27008v1#id5) if ε=0\varepsilon=0.

### 3.2 Dynamic oligopoly model

Set of agents 𝒩={1,…,N}\mathcal{N}=\{1,\dots,N\}

Number of rounds TT

For each agent ii: initial demand D1iD\_{1}^{i}, unit production cost cic\_{i}, policy πi\pi\_{i}, observation function Φi\Phi\_{i}

for t=1,2,…,Tt=1,2,\dots,T do

for i∈𝒩i\in\mathcal{N} do

ii observes oti=Φi​(st)=Φi​(t,Dt1,…,DtN)o\_{t}^{i}=\Phi\_{i}(s\_{t})=\Phi\_{i}(t,D\_{t}^{1},\dots,D\_{t}^{N})

ii selects a price pti∼πi​(oti)p\_{t}^{i}\sim\pi\_{i}(o\_{t}^{i})

ii sells quantity qti=Dti−ptiq\_{t}^{i}=D\_{t}^{i}-p\_{t}^{i}

ii receives reward rti=(pti−ci)​qtir\_{t}^{i}=(p\_{t}^{i}-c\_{i})q\_{t}^{i}

end for

Compute the average price as p¯t=1N​∑j∈𝒩ptj\bar{p}\_{t}=\frac{1}{N}\sum\_{j\in\mathcal{N}}p\_{t}^{j}

for i∈𝒩i\in\mathcal{N} do

Compute the price difference Δ​pti=pti−p¯t\Delta p\_{t}^{i}=p\_{t}^{i}-\bar{p}\_{t}

Transition demand to Dt+1i=Dti−Δ​ptiD\_{t+1}^{i}=D\_{t}^{i}-\Delta p\_{t}^{i}

Optionally, drop out ii if Dt+1i<ciD\_{t+1}^{i}<c\_{i} (see [Eq.˜2](https://arxiv.org/html/2510.27008v1#S3.E2 "In 3.2 Dynamic oligopoly model ‣ 3 The Model ‣ Algorithmic Predation: Equilibrium Analysis in Dynamic Oligopolies with Smooth Market Sharing"))

end for

end for

Reward each agent ii with Ui=∑t=1TrtiU\_{i}=\sum\_{t=1}^{T}r\_{t}^{i}

Algorithm 1  Dynamic oligopoly game studied in this work.

We study an oligopoly model (see [Algorithm˜1](https://arxiv.org/html/2510.27008v1#alg1 "In 3.2 Dynamic oligopoly model ‣ 3 The Model ‣ Algorithmic Predation: Equilibrium Analysis in Dynamic Oligopolies with Smooth Market Sharing")) based on Selten ([1965](https://arxiv.org/html/2510.27008v1#bib.bib21)), and incorporate a dropout mechanism inspired by Bylka et al. ([2000](https://arxiv.org/html/2510.27008v1#bib.bib23)). Further, we introduce a novel imperfect information setting that considers uncertainty in real-world markets. The model consists of NN firms producing a homogeneous good over a fixed time horizon TT. Each firm ii has a constant unit production cost cic\_{i} and an initial demand D1iD\_{1}^{i}.
DtiD\_{t}^{i} is assumed to be the intercept of the inverse demand curve, that is, it represents the price at which the quantity demanded drops to zero. In each period tt, firms simultaneously set prices ptip\_{t}^{i} from a continuous interval. Based on a linear demand model, firm ii sells a quantity of Dti−ptiD\_{t}^{i}-p\_{t}^{i} units, yielding a profit of rti=(pti−ci)​(Dti−pti)r\_{t}^{i}=(p\_{t}^{i}-c\_{i})(D\_{t}^{i}-p\_{t}^{i}).
After all prices are set in period tt, a below average price for firm ii attracts more customers, leading to increased demand Dt+1i=Dti+p¯t−ptiD\_{t+1}^{i}=D\_{t}^{i}+\bar{p}\_{t}-p\_{t}^{i}, where p¯t=1N​∑j=1Nptj\bar{p}\_{t}=\frac{1}{N}\sum\_{j=1}^{N}p\_{t}^{j} is the average price in period tt. The effect that not all customers immediately switch to the firm with the lowest price is demand inertia (Selten ([1965](https://arxiv.org/html/2510.27008v1#bib.bib21)) and can be due to switching costs or behavioral effects such as brand loyalty.

In the formulation as a [POMG](https://arxiv.org/html/2510.27008v1#id4), the state sts\_{t} includes the demand of each firm DtiD\_{t}^{i} and the current period tt. The action space 𝒜i=[ci,pmax]\mathcal{A}\_{i}=[c\_{i},p\_{\text{max}}] comprises all possible prices ptip\_{t}^{i} that firm ii can set, where the lower bound prevents selling at a loss and the upper bound pmaxp\_{\text{max}} is the monopolistic price. Agents 𝒩\mathcal{N}, the reward function 𝐫\mathbf{r}, transition function 𝒯\mathcal{T}, and the time horizon TT align with the model description.

We consider two different information settings. The first is the fully observable case Φi​(st)=st=(t,Dt1,Dt2,…,DtN)\Phi\_{i}(s\_{t})=s\_{t}=(t,D\_{t}^{1},D\_{t}^{2},\dots,D\_{t}^{N}), where the firms observe the entire state, as in Selten ([1965](https://arxiv.org/html/2510.27008v1#bib.bib21)) and Bylka et al. ([2000](https://arxiv.org/html/2510.27008v1#bib.bib23)). The second is the partially observable case, where firms only observe demand at the current time tt, that is, Φi​(st)=t\Phi\_{i}(s\_{t})=t. This setting is relevant for markets where firms lack precise demand information, such as in online retail markets (van de Geer et al., [2019](https://arxiv.org/html/2510.27008v1#bib.bib40)) or ticket sales in the entertainment industry (Courty, [2000](https://arxiv.org/html/2510.27008v1#bib.bib41)). Such conditions are common in which firms protect their demand data and must infer their own demand from historical data (van de Geer et al., [2019](https://arxiv.org/html/2510.27008v1#bib.bib40)).

A unique deterministic [NE](https://arxiv.org/html/2510.27008v1#id5) of the form pi​(Dt1,…,DtN,t)=λ1,t,i+Dti⋅λ2,t,ip\_{i}(D\_{t}^{1},\ldots,D\_{t}^{N},t)=\lambda\_{1,t,i}+D\_{t}^{i}\cdot\lambda\_{2,t,i} is known for the case of complete observability (Selten, [1965](https://arxiv.org/html/2510.27008v1#bib.bib21)).
To study predatory behavior, we extend Selten’s model with a dropout mechanism inspired by Bylka et al. ([2000](https://arxiv.org/html/2510.27008v1#bib.bib23)). However, since the number of customers of a firm is the *area under the demand curve* rather than the demand itself, we preserve the total area under the demand curve after dropouts, yielding the following demand update:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | D~t+1i\displaystyle\tilde{D}\_{t+1}^{i} | =Dti+pt¯−pti\displaystyle=D\_{t}^{i}+\bar{p\_{t}}-p\_{t}^{i}\> |  | (2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Jt\displaystyle J\_{t} | ={i∈𝒩|D~t+1i<ci}\displaystyle=\{i\in\mathcal{N}|\tilde{D}\_{t+1}^{i}<c\_{i}\} |  | (3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | D¯t+1i\displaystyle\bar{D}\_{t+1}^{i} | ={D~t+1i​ if ​i∈𝒩∖Jt0​ otherwise\displaystyle=\begin{cases}\tilde{D}\_{t+1}^{i}\text{ if }i\in\mathcal{N}\setminus J\_{t}\\ 0\text{ otherwise}\end{cases}\> |  | (4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Dt+1i\displaystyle D\_{t+1}^{i} | =(D¯t+1i)2+D¯t+1i∑k∈𝒩∖JtD¯t+1k⋅∑j∈Jt(D~t+1j)2\displaystyle=\sqrt{\left(\bar{D}\_{t+1}^{i}\right)^{2}+\frac{\bar{D}\_{t+1}^{i}}{\sum\_{k\in\mathcal{N}\setminus J\_{t}}\bar{D}\_{t+1}^{k}}\cdot\sum\_{j\in J\_{t}}\left(\tilde{D}\_{t+1}^{j}\right)^{2}}\> |  | (5) |

Increasing prices in a stage increases short-term profits at the cost of losing market share in subsequent periods due to demand inertia. Capturing an early market share advantage thus yields significant benefits over multiple future periods. These competing incentives typically result in aggressive pricing early on, followed by price increases toward the end of the finite horizon.

Introducing the possibility that firms may permanently exit the market amplifies these competitive dynamics. Specifically, the irreversible threat of market exit leads to even more aggressive pricing initially, as firms aim to survive and eliminate competitors. Once rivals are pushed out, the remaining firms gain additional market share, further enabling price increases in later rounds. The combination of demand inertia, stage-wise monopoly incentives, and the credible threat of permanent market exit makes Selten’s extended framework particularly suitable for studying predatory behavior. Moreover, the complexity introduced by a finite time horizon, interdependent demands, and dropout mechanisms has prevented analytical equilibrium analysis so far.

## 4 Analytical equilibrium analysis of the dynamic model without demand observation

We derive a deterministic [NE](https://arxiv.org/html/2510.27008v1#id5) in the partially observable dynamic oligopoly without dropouts, complementing the one derived by Selten ([1965](https://arxiv.org/html/2510.27008v1#bib.bib21)) for fully observable markets:

###### Theorem 1.

Consider a dynamic oligopoly model with NN firms, unit production costs cic\_{i}, initial demand D1iD\_{1}^{i}, and time horizon TT. The model assumes no demand observation, i.e., Φi​(st)=t\Phi\_{i}(s\_{t})=t, and no dropouts.
Then, any solution to the following system of equations constitutes a deterministic [NE](https://arxiv.org/html/2510.27008v1#id5):

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (Dti−2​pti+ci)−∑τ=t+1T((pτi−ci)⋅N−1N)\displaystyle(D\_{t}^{i}-2p\_{t}^{i}+c\_{i})-\sum\_{\tau=t+1}^{T}\left((p\_{\tau}^{i}-c\_{i})\cdot\frac{N-1}{N}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =0∀i∈𝒩,1≤t≤T\displaystyle\hskip 102.43008pt=0\quad\forall i\in\mathcal{N},1\leq t\leq T |  | (6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | Dt+1i=Dti−pti+1N​∑j∈𝒩ptj∀i∈𝒩,1≤t<T,\displaystyle D\_{t+1}^{i}=D\_{t}^{i}-p\_{t}^{i}+\frac{1}{N}\sum\_{j\in\mathcal{N}}p\_{t}^{j}\quad\forall i\in\mathcal{N},1\leq t<T, |  | (7) |

where the constraints are Dti≥0D\_{t}^{i}\geq 0 and ci≤pti<pmaxc\_{i}\leq p\_{t}^{i}<p\_{\text{max}} for 1≤t≤T1\leq t\leq T and i∈𝒩i\in\mathcal{N}.

###### Proof sketch.

[Equation˜7](https://arxiv.org/html/2510.27008v1#S4.E7 "In Theorem 1. ‣ 4 Analytical equilibrium analysis of the dynamic model without demand observation ‣ Algorithmic Predation: Equilibrium Analysis in Dynamic Oligopolies with Smooth Market Sharing") follows from the demand update step. We then observe that the rewards are continuously differentiable. [Theorem˜1](https://arxiv.org/html/2510.27008v1#S4.Ex1 "Theorem 1. ‣ 4 Analytical equilibrium analysis of the dynamic model without demand observation ‣ Algorithmic Predation: Equilibrium Analysis in Dynamic Oligopolies with Smooth Market Sharing") is derived from the first-order condition d​Uid​pti=0\frac{dU\_{i}}{dp\_{t}^{i}}=~0, which gives us a necessary condition for a NE. We further check the second-order condition for a solution of the first-order condition, giving us a sufficient condition for a NE.
∎

## 5 Learning in Markov Games

Classical [RL](https://arxiv.org/html/2510.27008v1#id1) algorithms solve [Markov decision processes](https://arxiv.org/html/2510.27008v1#id2), where a single agent interacts with the environment. A straightforward approach to extend these algorithms to [POMGs](https://arxiv.org/html/2510.27008v1#id4) is self-play. Here, independent instances of a single-agent [RL](https://arxiv.org/html/2510.27008v1#id1) algorithm are employed for each agent, all interacting within the same environment (Albrecht et al., [2024](https://arxiv.org/html/2510.27008v1#bib.bib39), Chapter 9.3.2).
We consider policy gradient algorithms, where each agent’s policy πθi(oi)=π(⋅|o,θi)\pi\_{\theta\_{i}}(o\_{i})=\pi(\cdot|o,\theta\_{i}) is parameterized by a neural network with parameters θi\theta\_{i}. For continuous action spaces, the network outputs parameters of a continuous distribution, e.g., a normal or beta distribution. Parameters are updated simultaneously for all agents in each iteration according to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θi←θi+α​∇θiUi​(πθi,{πθj}j∈𝒩∖{i})\displaystyle\theta\_{i}\leftarrow\theta\_{i}+\alpha\nabla\_{\theta\_{i}}U\_{i}(\pi\_{\theta\_{i}},\{\pi\_{\theta\_{j}}\}\_{j\in{\mathcal{N}\setminus\{i\}}}) |  | (8) |

The policy gradient ∇θiUi\nabla\_{\theta\_{i}}U\_{i} can be estimated from a batch of game trajectories using the Reinforce algorithm or its variants Sutton and Barto ([2018](https://arxiv.org/html/2510.27008v1#bib.bib42)), such as [proximal policy optimization](https://arxiv.org/html/2510.27008v1#id7) ([PPO](https://arxiv.org/html/2510.27008v1#id7)). In this work, we use both Reinforce and [PPO](https://arxiv.org/html/2510.27008v1#id7) as implemented by Raffin et al. ([2021](https://arxiv.org/html/2510.27008v1#bib.bib43)).
After training, a pure strategy is extracted by selecting the most likely action.

### 5.1 Measuring closeness to equilibrium

We assess convergence to approximate [NE](https://arxiv.org/html/2510.27008v1#id5) with a novel verification algorithm for multi-stage games with continuous states and actions introduced by Pieroth et al. ([2025](https://arxiv.org/html/2510.27008v1#bib.bib10)).
Given the learned strategy profile π𝒩\pi\_{\mathcal{N}}, it estimates the best-response utility supπi∈ΣiUi​(πi,π−i)\sup\_{\pi\_{i}\in\Sigma\_{i}}U\_{i}(\pi\_{i},\pi\_{-i}) by discretizing the action- and observation spaces of agent ii and building up a game tree from the view of a single agent. For a given discretization K∈ℕK\in\mathbb{N}, it estimates the best-response utility by searching over a finite set of step functions ΣiK\Sigma\_{i}^{K}. Given large enough KK, one has supπi∈ΣiKUi​(πi,π−i)≈supπi∈ΣiUi​(πi,π−i)\sup\_{\pi\_{i}\in\Sigma\_{i}^{K}}U\_{i}(\pi\_{i},\pi\_{-i})\approx\sup\_{\pi\_{i}\in\Sigma\_{i}}U\_{i}(\pi\_{i},\pi\_{-i}). We define the brute-force utility loss for each agent i∈𝒩i\in\cal{N} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒbf,i=supπi∈ΣiKUi​(πi,π−i)−Ui​(πi,π−i).\displaystyle\mathcal{L}\_{\text{bf},i}=\sup\_{\pi\_{i}\in\Sigma\_{i}^{K}}U\_{i}(\pi\_{i},\pi\_{-i})-U\_{i}(\pi\_{i},\pi\_{-i}). |  | (9) |

The size of the game tree to build for this loss at a discretization KK scales exponentially in TT, limiting the analysis to T=4T=4 for K=32K=32. Further, the brute-force verifier can only verify whether a given strategy profile is close to a [NE](https://arxiv.org/html/2510.27008v1#id5) but not compute an approximate [NE](https://arxiv.org/html/2510.27008v1#id5) itself.

Since the interpretation of the utility loss depends on the utility scale, we also report the normalized brute-force utility loss ℒbf,norm,i=ℒbf,i/maxπi∈ΣiK⁡Ui​(πi,π−i)\mathcal{L}\_{\text{bf,norm},i}=\mathcal{L}\_{\text{bf},i}/\max\_{\pi\_{i}\in\Sigma\_{i}^{K}}U\_{i}(\pi\_{i},\pi\_{-i})

### 5.2 Measuring predatory behavior and its effects

Ordover and Willig ([1981](https://arxiv.org/html/2510.27008v1#bib.bib44)) characterize predatory pricing as a deliberate sacrifice of profits relative to a feasible, less aggressive action, followed by a recoupment of those losses once competitors exit the market. We develop a metric to measure the predatory incentive for each agent ii under strategy profile π\pi, following that definition, employing the known analytical equilibrium strategies without dropouts as a baseline.

Denote by τi=min⁡{t:an opponent drops out}\tau\_{i}=\min\{t:\text{an opponent drops out}\} the first period in which an opponent exits. Let rti,equr^{i,\text{equ}}\_{t} represent agent ii’s reward at time step tt when all agents follow the equilibrium strategy without dropouts for the whole game, and rti,πr^{i,\pi}\_{t} the corresponding reward under strategy profile π\pi. Then, the predatory incentive for agent ii is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | PIi​(π):=−∑t<τimax⁡{0,rti,equ−rti,π}⏟sacrifice+∑t≥τmax⁡{0,rti,π−rti,equ}⏟recoupment.\displaystyle\text{PI}\_{i}(\pi):=\underbrace{-\sum\_{t<\tau\_{i}}\max\{0,r^{i,\text{equ}}\_{t}-r^{i,\pi}\_{t}\}}\_{\text{sacrifice}}+\underbrace{\sum\_{t\geq\tau}\max\{0,r^{i,\pi}\_{t}-r^{i,\text{equ}}\_{t}\}}\_{\text{recoupment}}. |  | (10) |

The first sum captures profit sacrificed before the rival’s exit, while the second sum measures subsequent recoupment gains. The use of the maximum operator ensures that only deliberate sacrifices and corresponding recoupment gains count toward the predatory incentive. If no opponent exists, we set PIi​(π)=0\text{PI}\_{i}(\pi)=0.
A strictly positive predatory incentive (PIi​(π)>0\text{PI}\_{i}(\pi)>0) indicates that agent ii’s strategy, which induces an opponent’s market exit, is ex-ante profitable relative to the non-exclusionary equilibrium benchmark. Conversely, a non-positive value (PIi​(π)≤0\text{PI}\_{i}(\pi)\leq 0) implies that the observed pricing path lacks exclusionary justification.

To quantify the welfare implications of predatory pricing, we calculate total welfare of a strategy profile π\pi as the sum of consumer surplus and producer surplus over all periods: Wπ=∑t=1T(CStπ+PStπ)W^{\pi}=\sum\_{t=1}^{T}\left(\text{CS}\_{t}^{\pi}+\text{PS}\_{t}^{\pi}\right) (Belleflamme and
Peitz, [2010](https://arxiv.org/html/2510.27008v1#bib.bib45), p. 24). The producer surplus PStπ=∑i∈𝒩rti,π\text{PS}\_{t}^{\pi}=\sum\_{i\in\mathcal{N}}r^{i,\pi}\_{t} is the sum of all rewards.
The consumer surplus CStπ:=∑i∈𝒩(Dti−pti)​qti=∑i∈𝒩(Dti−pti)2\text{CS}\_{t}^{\pi}:=\sum\_{i\in\mathcal{N}}(D\_{t}^{i}-p\_{t}^{i})q\_{t}^{i}=\sum\_{i\in\mathcal{N}}(D\_{t}^{i}-p\_{t}^{i})^{2} is the consumer’s willingness to pay minus the price, following a linear demand model.

We measure welfare harm from predatory pricing by comparing welfare levels under dropout-enabled scenarios to the welfare in the corresponding analytical equilibrium without dropouts π∗\pi^{\*}, reporting the welfare difference Δ​Wπ:=Wπ−Wπ∗\Delta W^{\pi}:=W^{\pi}-W^{\pi^{\*}}.

## 6 Numerical equilibrium analysis experiments

In our numerical experiments, we conduct an equilibrium analysis of the introduced oligopolistic market to address three central questions: First, does predatory behavior emerge as a rational equilibrium strategy when firms can exit the market, and is it more profitable for the predator than the analytical equilibrium without dropouts? Second, how does predation affect consumer and producer welfare? And third, how sensitive are these outcomes to the information structure, specifically whether firms fully observe rivals’ demand or operate under partial observability?

### 6.1 Experimental design

We consider the dynamic oligopoly from [Section˜3.2](https://arxiv.org/html/2510.27008v1#S3.SS2 "3.2 Dynamic oligopoly model ‣ 3 The Model ‣ Algorithmic Predation: Equilibrium Analysis in Dynamic Oligopolies with Smooth Market Sharing") with N=3N=3 agents, an initial demand of D1i=1D\_{1}^{i}=1 for all i∈𝒩i\in\mathcal{N}, and a time horizon of T=4T=4 stages. We evaluate brute-force utility loss, predatory incentives, and welfare differences across all combinations of the independent variables: *information setting* (fully vs. partially observable), *learning algorithm* ([PPO](https://arxiv.org/html/2510.27008v1#id7) vs. Reinforce), and *production costs*. For the latter, we examine asymmetries by fixing c1=c2=0.8c\_{1}=c\_{2}=0.8 and varying c0c\_{0} over [0.42,0.95][0.42,0.95] in 60 equidistant steps, yielding cost vectors 𝐜=[c0,0.8,0.8]\mathbf{c}=[c\_{0},0.8,0.8].

We use a beta distribution for the action distribution, as suggested by (Petrazzini and
Antonelo, [2021](https://arxiv.org/html/2510.27008v1#bib.bib46)), with a fully connected network (3 linear layers, 64 units, SeLu activation) for all agents and algorithms. Each algorithm runs for 1,0001,000 iterations with 20,00020,000 trajectories per iteration at a learning rate of 8.57⋅10−48.57\cdot 10^{-4} for PPO and 2.864⋅10−42.864\cdot 10^{-4} for Reinforce. To improve accuracy, we divide the learning rate by eight for PPO and by two for Reinforce every 250250 iterations.

Training via self-play requires approximately 1010 minutes per run for [PPO](https://arxiv.org/html/2510.27008v1#id7) and 66 minutes for Reinforce on our hardware (GeForce RTX 2080 Ti, 12 Gb RAM). To cover the experimental design, we conduct 1,2001,200 training runs (55 seeds × 22 information settings × 6060 production costs × 22 algorithms), which can run in parallel.

### 6.2 Results

We now present the results of our equilibrium analysis. After a convergence analysis, we examine the emergence of distinct market regimes and predatory pricing behavior, followed by an evaluation of their welfare implications and sensitivity to the information structure.

![Refer to caption](x4.png)


Figure 1: Strategy profile learned by [PPO](https://arxiv.org/html/2510.27008v1#id7) in the partially observable case with dropouts for specific cost scenario c0=0.51c\_{0}=0.51 and c1=c2=0.8c\_{1}=c\_{2}=0.8. Recall that with partial observability, a deterministic probabilistic strategy is fully characterized by TT prices. If an agent drops out in a round, the graph stops at that round.

Equilibrium convergence and market regimes: Table [1](https://arxiv.org/html/2510.27008v1#S6.T1 "Table 1 ‣ 6.2 Results ‣ 6 Numerical equilibrium analysis experiments ‣ Algorithmic Predation: Equilibrium Analysis in Dynamic Oligopolies with Smooth Market Sharing") shows that both PPO and Reinforce reliably converge to approximate equilibria with ε≤0.032\varepsilon\leq 0.032 for all configurations studied. Therefore, we can confidently consider the following analyses as equilibrium analyses.

Varying agent 0’s unit cost c0c\_{0} determines its competitive position, resulting in four distinct market regimes: *dominance*, *predation*, *competition*, and *marginalization*. In the *dominance* regime, agent 0 leverages its significant cost advantage to eliminate both competitors. Under *predation*, agent 0 pushes out one rival and shares the market with the other. As its cost advantage decreases, all agents remain active, producing stable *competition*. Finally, when agent 0 is severely disadvantaged, it is driven out by its rivals, defining the *marginalization* regime. These regimes are marked in Figures [2](https://arxiv.org/html/2510.27008v1#S6.F2 "Figure 2 ‣ 6.2 Results ‣ 6 Numerical equilibrium analysis experiments ‣ Algorithmic Predation: Equilibrium Analysis in Dynamic Oligopolies with Smooth Market Sharing") and [3](https://arxiv.org/html/2510.27008v1#S6.F3 "Figure 3 ‣ 6.2 Results ‣ 6 Numerical equilibrium analysis experiments ‣ Algorithmic Predation: Equilibrium Analysis in Dynamic Oligopolies with Smooth Market Sharing") and constitute the main tipping points in behavior.

|  |  | 0.42≤c0<0.6850.42\leq c\_{0}<0.685 | | 0.685≤c0≤0.950.685\leq c\_{0}\leq 0.95 | |
| --- | --- | --- | --- | --- | --- |
|  |  | maxc0⁡ℒbf\max\_{c\_{0}}\mathcal{L}\_{\text{bf}} | maxc0⁡ℒbf, norm\max\_{c\_{0}}\mathcal{L}\_{\text{bf, norm}} | maxc0⁡ℒbf\max\_{c\_{0}}\mathcal{L}\_{\text{bf}} | maxc0⁡ℒbf, norm\max\_{c\_{0}}\mathcal{L}\_{\text{bf, norm}} |
| PPO (FO) | Agent 0 | 0.032 | 0.048 | 0.001 | 1.000 |
| Agents 1 & 2 | 0.010 | 0.496 | 0.007 | 0.143 |
| PPO (PO) | Agent 0 | 0.019 | 0.050 | 0.000 | 1.000 |
| Agents 1 & 2 | 0.009 | 0.477 | 0.007 | 0.101 |
| REINFORCE (FO) | Agent 0 | 0.021 | 0.046 | 0.000 | 1.000 |
| Agents 1 & 2 | 0.008 | 0.440 | 0.003 | 0.093 |
| REINFORCE (PO) | Agent 0 | 0.021 | 0.045 | 0.001 | 1.000 |
| Agents 1 & 2 | 0.007 | 0.411 | 0.007 | 0.080 |

Table 1: The maximum of the brute force (ℒbf\mathcal{L}\_{\text{bf}}) and normalized brute-force (ℒbf, norm\mathcal{L}\_{\text{bf, norm}}) losses for the unit cost vector [c0,0.8,0.8][c\_{0},0.8,0.8] over all random seed, algorithms, and information settings (FO: Fully observable, PO: Partially observable). Agent 0 is reported separately from agents 11 and 22 because only its unit cost c0c\_{0} is varied, leading to asymmetric payoffs. Two cost regimes are distinguished to highlight a normalization artifact: When c0c\_{0} is very low or very high, agent 0’s or agent 11 or 22’s best-response utility approaches zero, causing even minor absolute deviations (e.g. <0.001<0.001) to inflate the normalized loss ℒbf,norm\mathcal{L}\_{\text{bf,norm}} close to 11. This inflated value does not reflect poor convergence but rather a diminishing denominator. We therefore gray out such values.

Emergence of predatory behavior: [Figure˜1](https://arxiv.org/html/2510.27008v1#S6.F1 "In 6.2 Results ‣ 6 Numerical equilibrium analysis experiments ‣ Algorithmic Predation: Equilibrium Analysis in Dynamic Oligopolies with Smooth Market Sharing") shows a strategy profile where agent 0 learned predatory pricing, leveraging its significant competitive advantage. Initially, agent 0 sets prices close to its production cost, sacrificing short-term profits to push agent 22 out by the third round. Subsequently, agents 0 and 11 raise their prices in the duopoly that follows. This predatory pricing differs substantially from the analytical equilibrium without dropouts, in which agent 0 gradually increases prices and agents 11 and 22 price symmetrically and decrease slightly over time.

[Figure˜2](https://arxiv.org/html/2510.27008v1#S6.F2 "In 6.2 Results ‣ 6 Numerical equilibrium analysis experiments ‣ Algorithmic Predation: Equilibrium Analysis in Dynamic Oligopolies with Smooth Market Sharing") illustrates how predatory incentives depend on agent 0’s cost c0c\_{0}, marking the regimes of *dominance*, *predation*, *competition*, and *marginalization*. During *dominance*, agent 0 has a strong positive predatory incentive, reflecting significant profitability from monopolizing the market. Predatory incentives decline sharply but remain positive in the *predation* regime, as agent 0 benefits by forcing one competitor out. Agents 11 and 22 also exhibit positive incentives here, as one survives and profits from increased market share. During *competition*, no agents exit, resulting in zero predatory incentives. In the *marginalization* regime, agents 11 and 22 show increased incentives, aggressively pushing the disadvantaged agent 0 from the market.

![Refer to caption](x5.png)


(a) Agent 0

![Refer to caption](x6.png)


(b) Agent 11

![Refer to caption](x7.png)


(c) Agent 22

Figure 2: The predatory incentives P​Ii​(π)PI\_{i}(\pi) for agents i∈{1,2,3}i\in\{1,2,3\} and learned strategy profiles π\pi over the different costs c0c\_{0}, information structures, and algorithms. The bold line represents the mean, and the colored shaded area represents the standard deviation over five seeds. The bottom bar indicates the regime, determined by a majority vote over all algorithms, information settings, and random seeds.

Overall, these findings demonstrate that predatory pricing is rational, consistently emerges in equilibrium, and can be robustly learned through independent reinforcement learning algorithms.

Welfare effects of predation: Having established the emergence of predatory behavior, we now assess its welfare implications by comparing the learned strategies (with dropouts) against the analytical equilibrium strategies (without dropouts). The effects of predation on welfare are disputed, as some scholars argue predation reduces consumer welfare by eliminating competition, while others suggest short recoupment phases or uncertain exits may sometimes benefit welfare.

[Figure˜3](https://arxiv.org/html/2510.27008v1#S6.F3 "In 6.2 Results ‣ 6 Numerical equilibrium analysis experiments ‣ Algorithmic Predation: Equilibrium Analysis in Dynamic Oligopolies with Smooth Market Sharing") summarizes the welfare differences in terms of producer surplus (Δ​P​Sπ\Delta PS^{\pi}), consumer surplus (Δ​C​Sπ\Delta CS^{\pi}), and total welfare (Δ​Wπ\Delta W^{\pi}). Producer surplus differences largely mirror the predatory incentives: substantial surplus during *dominance*, moderate but positive surplus in *predation*, minimal surplus in *competition*, and an initially sharp increase followed by a decline in *marginalization*. This decrease at high costs occurs because agent 0 becomes too uncompetitive to influence the market significantly even when remaining active in the analytical benchmark.

Consumer surplus differences in [Fig.˜3(b)](https://arxiv.org/html/2510.27008v1#S6.F3.sf2 "In Figure 3 ‣ 6.2 Results ‣ 6 Numerical equilibrium analysis experiments ‣ Algorithmic Predation: Equilibrium Analysis in Dynamic Oligopolies with Smooth Market Sharing") show distinct patterns. During *competition*, differences remain small. Entering *marginalization*, a notable initial increase occurs due to aggressive price cutting by agents 11 and 22 to eliminate agent 0, but this advantage diminishes as cost differences widen, the sacrifice phase becomes less costly, and the recoupment phase becomes more dominant. A similar effect arises entering *predation*, reflecting high initial sacrifice costs. Another sharp increase occurs as *dominance* begins, followed by a gradual decrease as agent 0 leverages its monopoly power earlier and more effectively.

The total welfare difference in [Fig.˜3(c)](https://arxiv.org/html/2510.27008v1#S6.F3.sf3 "In Figure 3 ‣ 6.2 Results ‣ 6 Numerical equilibrium analysis experiments ‣ Algorithmic Predation: Equilibrium Analysis in Dynamic Oligopolies with Smooth Market Sharing") closely follows the consumer surplus pattern. Interestingly, predation-driven exits sometimes enhance overall welfare, especially when inefficient firms exit and aggressive initial price cuts outweigh later price increases. These results indicate that reduced competition can, under certain conditions, lead to better welfare outcomes, challenging traditional antitrust perspectives focused strictly on maximizing competition.

Finally, we observe no significant differences between the fully observable and partially observable settings. Both yield identical market regimes and very similar welfare outcomes, confirming that predatory pricing dynamics primarily depend on timing strategies rather than the granularity of demand information.

![Refer to caption](x8.png)


(a) Producer surplus difference Δ​P​Sπ\Delta PS^{\pi}

![Refer to caption](x9.png)


(b) Consumer surplus difference Δ​C​Sπ\Delta CS^{\pi}

![Refer to caption](x10.png)


(c) Welfare difference

Figure 3: The producer surplus, consumer surplus, and overall welfare (Δ​Wπ\Delta W^{\pi}) differences for a learned strategy profile π\pi and the analytical equilibrium strategies π∗\pi^{\*} without dropout under different costs c0c\_{0}, information structures, and algorithms. The bold line represents the mean and the shaded area the standard deviation over five seeds. The bottom bar indicates the regime, determined by a majority vote over all algorithms, information settings, and random seeds.

These nuanced welfare effects and intricate patterns highlight the importance of using finite-horizon, continuous-action models, which uniquely capture critical timing and trade-off dynamics inaccessible to infinite-horizon or coarser discretized models.

## 7 Conclusion

We analyze predatory pricing behavior in a dynamic oligopoly model extending the seminal framework introduced by Selten ([1965](https://arxiv.org/html/2510.27008v1#bib.bib21)). By integrating deep reinforcement learning techniques with numerical equilibrium verification, we successfully identify and confirm approximate Nash equilibria that capture realistic predatory strategies. Our finite-horizon model with continuous price-setting addresses previously unresolved questions, allowing us to rigorously analyze the timing of predatory actions and the complex trade-offs between short-term sacrifices and subsequent recoupment. Our results demonstrate that predatory behavior is not only rational and emerges robustly in equilibrium, but also can yield counterintuitive welfare benefits under certain conditions. Specifically, short-term aggressive pricing combined with the removal of inefficient competitors may improve overall market efficiency. These findings challenge conventional antitrust wisdom, underscoring the importance of nuanced analyses that account for timing, cost structures, and competitive dynamics in evaluating market regulation and policy.

## References

* Gates et al. [1995]

  Susan Gates, Paul Milgrom, and John Roberts.
  Deterring predation in telecommunications: Are line-of-business
  restraints needed?
  *Managerial and Decision Economics*, 16(4):427–438, 1995.
* DiLorenzo [1992]

  Thomas J DiLorenzo.
  *The myth of predatory pricing*.
  Cato Institute, 1992.
* May [1994]

  Keith Allen May.
  Brooke group ltd. v. brown & williamson tobacco corp.: A victory for
  consumer welfare under the robinson-patman act.
  *U. Rich. L. Rev.*, 28:507, 1994.
* Bolton et al. [1999]

  Patrick Bolton, Joseph F Brodley, and Michael H Riordan.
  Predatory pricing: Strategic theory and legal policy.
  *Geo. LJ*, 88:2239, 1999.
* Leslie [2023]

  Christopher R Leslie.
  Predatory pricing algorithms.
  *NYUL Rev.*, 98:49, 2023.
* Cheng and Nowag [2023]

  Thomas K Cheng and Julian Nowag.
  Algorithmic predation and exclusion.
  *U. Pa. J. Bus. L.*, 25:41, 2023.
* Bichler et al. [2025]

  Martin Bichler, Julius Durmann, and Matthias Oberlechner.
  Algorithmic pricing and algorithmic collusion.
  *Business & Information Systems Engineering*, to appear, 2025.
* Deng et al. [2024]

  Shidi Deng, Maximilian Schiffer, and Martin Bichler.
  On the existence of algorithmic collusion in dynamic pricing with
  deep reinforcement learning.
  *Conference on Wirtschaftsinformatik*, 2024.
* Sanders et al. [2018]

  James BT Sanders, J Doyne Farmer, and Tobias Galla.
  The prevalence of chaotic dynamics in games with many players.
  *Scientific Reports*, 8(1):1–13, 2018.
* Pieroth et al. [2025]

  Fabian Raoul Pieroth, Nils Kohring, and Martin Bichler.
  Deep reinforcement learning for equilibrium computation in
  multi-stage auctions and contests.
  *Management Science*, 2025.
* Milgrom [1990]

  Paul Milgrom.
  New theories of predatory pricing.
  *Industrial structure in the new industrial economics*, 1990.
* Telser [1966]

  L. G. Telser.
  Cutthroat Competition and the Long Purse.
  *The Journal of Law & Economics*, 9:259–277, 1966.
* Nash [1950]

  John Fs Nash.
  Equilibrium points in n-person games.
  *Proceedings of the national academy of sciences*, 36(1):48–49, 1950.
* Maskin and Tirole [1988]

  Eric Maskin and Jean Tirole.
  A theory of dynamic oligopoly, ii: Price competition, kinked demand
  curves, and edgeworth cycles.
  *Econometrica: Journal of the Econometric Society*, pages
  571–599, 1988.
* Cabral and Riordan [1994]

  Luis Cabral and Michael Riordan.
  The Learning Curve, Market Dominance, and Predatory
  Pricing.
  *Econometrica*, 62(5):1115–40, 1994.
* Besanko et al. [2011]

  David Besanko, Ulrich Doraszelski, and Yaroslav Kryukov.
  The Economics of Predation: What Drives Pricing When
  There is Learning-by-Doing?
  *GSIA Working Papers*, (E8), 2011.
* Rey et al. [2022]

  Patrick Rey, Yossi Spiegel, and Konrad O. Stahl.
  A Dynamic Model of Predation.
  2022.
* Fudenberg and Kreps [1993]

  Drew Fudenberg and David M Kreps.
  Learning mixed equilibria.
  *Games and Economic Behavior*, 5(3):320–367, 1993.
* Pakes and McGuire [1992]

  Ariel Pakes and Paul McGuire.
  Computing markov perfect nash equilibria: Numerical implications of a
  dynamic differentiated product model, 1992.
* Schulman et al. [2017]

  John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov.
  Proximal policy optimization algorithms.
  *CoRR*, abs/1707.06347, 2017.
* Selten [1965]

  Reinhard Selten.
  Spieltheoretische Behandlung Eines Oligopolmodells Mit
  Nachfrageträgheit: Teil I: Bestimmung Des Dynamischen
  Preisgleichgewichts.
  *Zeitschrift für die gesamte Staatswissenschaft / Journal of
  Institutional and Theoretical Economics*, 121(2):301–324, 1965.
* Bertrand [1883]

  Jean Bertrand.
  Théorie mathématique de la richesse sociale.
  *Journal des Savants*, (68):499–508, 1883.
* Bylka et al. [2000]

  Stanisław Bylka, Stanisław Ambroszkiewicz, and Jan Komar.
  Discrete time dynamic game model for price competition in an
  oligopoly.
  *Annals of Operations Research*, 97(1):69–89, 2000.
* Assad et al. [2020]

  Stephanie Assad, Robert Clark, Daniel Ershov, and Lei Xu.
  Algorithmic pricing and competition: Empirical evidence from the
  german retail gasoline market.
  CESifo Working Paper 8521, CESifo, 2020.
  Available at SSRN: <https://ssrn.com/abstract=3682021> or
  <http://dx.doi.org/10.2139/ssrn.3682021>.
* Madhavan [2000]

  Ananth Madhavan.
  Market microstructure: A survey.
  *Journal of Financial Markets*, 3(3):205–258, 2000.
  ISSN 1386-4181.
  doi:[https://doi.org/10.1016/S1386-4181(00)00007-0](https://doi.org/https://doi.org/10.1016/S1386-4181(00)00007-0).
  URL
  <https://www.sciencedirect.com/science/article/pii/S1386418100000070>.
* Escobari and Lee [2014]

  Diego Escobari and Jim Lee.
  Demand uncertainty and capacity utilization in airlines.
  *Empirical Economics*, 47, 08 2014.
  doi:[10.1007/s00181-013-0725-2](https://doi.org/10.1007/s00181-013-0725-2).
* Fudenberg and Tirole [2013]

  Drew Fudenberg and Jean Tirole.
  *Dynamic models of oligopoly*.
  Routledge, 2013.
* Gerpott and Berends [2022]

  Torsten J. Gerpott and Jan Berends.
  Competitive pricing on online markets: A literature review.
  *Journal of Revenue and Pricing Management*, 21(6):596–622, December 2022.
* Phlips and Richard [1989]

  Louis Phlips and Jean-Francois Richard.
  A dynamic oligopoly model with demand inertia and inventories.
  *Mathematical Social Sciences*, 18(1):1–32,
  1989.
* Farrell and Shapiro [1988]

  Joseph Farrell and Carl Shapiro.
  Dynamic competition with switching costs.
  *The RAND Journal of Economics*, pages 123–137, 1988.
* Bayer and Chan [2007]

  Ralph-C Bayer and Mickey Chan.
  Network externalities, demand inertia and dynamic pricing in an
  experimental oligopoly market.
  *Economic Record*, 83(263):405–415, 2007.
* Besanko et al. [2014]

  David Besanko, Ulrich Doraszelski, and Yaroslav Kryukov.
  The economics of predation: What drives pricing when there is
  learning-by-doing?
  *American Economic Review*, 104(3):868–897,
  2014.
* Fudenberg and Levine [1999]

  Drew Fudenberg and David K. Levine.
  *The Theory of Learning in Games*, volume 2 of *MIT
  Press Series on Economic Learning and Social Evolution*.
  MIT Press, Cambridge, 2. edition, 1999.
* Milionis et al. [2023]

  Jason Milionis, Christos Papadimitriou, Georgios Piliouras, and Kelly
  Spendlove.
  An impossibility theorem in game dynamics.
  *Proceedings of the National Academy of Sciences*, 120(41):e2305349120, October 2023.
* Mazumdar et al. [2020]

  Eric Mazumdar, Lillian J. Ratliff, Michael I. Jordan, and S. Shankar Sastry.
  Policy-Gradient Algorithms Have No Guarantees of Convergence
  in Linear Quadratic Games.
  In *International Conference on Autonomous Agents and
  Multi Agent Systems (AAMAS)*, AAMAS ’20, pages 860–868,
  Richland, SC, May 2020. International Foundation for Autonomous Agents and
  Multiagent Systems.
* Daskalakis et al. [2010]

  Constantinos Daskalakis, Rafael Frongillo, Christos H Papadimitriou, George
  Pierrakos, and Gregory Valiant.
  On learning algorithms for Nash equilibria.
  In *International Symposium on Algorithmic Game Theory*, pages
  114–125. Springer, 2010.
* Bichler et al. [2023]

  Martin Bichler, Stephan B. Lunowa, Matthias Oberlechner, Fabian R. Pieroth, and
  Barbara Wohlmuth.
  On the Convergence of Learning Algorithms in Bayesian
  Auction Games, November 2023.
* Şeref Ahunbay and
  Bichler [2024]

  Mete Şeref Ahunbay and Martin Bichler.
  On the Uniqueness of Bayesian Coarse Correlated Equilibria in
  Standard First-Price and All-Pay Auctions, January 2024.
* Albrecht et al. [2024]

  Stefano V. Albrecht, Filippos Christianos, and Lukas Schäfer.
  *Multi-Agent Reinforcement Learning: Foundations and Modern
  Approaches*.
  MIT Press, 2024.
  URL <https://www.marl-book.com>.
* van de Geer et al. [2019]

  Ruben van de Geer, Arnoud V. den Boer, Christopher Bayliss, Christine S. M.
  Currie, Andria Ellina, Malte Esders, Alwin Haensel, Xiao Lei, Kyle D. S.
  Maclean, Antonio Martinez-Sykora, Asbjørn Nilsen Riseth, Fredrik
  Ødegaard, and Simos Zachariades.
  Dynamic pricing and learning with competition: Insights from the
  dynamic pricing challenge at the 2017 INFORMS RM & pricing conference.
  *Journal of Revenue and Pricing Management*, 18(3):185–203, June 2019.
* Courty [2000]

  Pascal Courty.
  An economic guide to ticket pricing in the entertainment industry.
  *Recherches Économiques de Louvain / Louvain Economic Review*,
  66(2):167–192, 2000.
  ISSN 07704518, 17821495.
  URL <http://www.jstor.org/stable/40724285>.
* Sutton and Barto [2018]

  Richard S Sutton and Andrew G Barto.
  *Reinforcement Learning: An Introduction*.
  A Bradford Book, Cambridge, Massachusetts, 2 edition, 2018.
* Raffin et al. [2021]

  Antonin Raffin, Ashley Hill, Adam Gleave, Anssi Kanervisto, Maximilian
  Ernestus, and Noah Dormann.
  Stable-Baselines3: Reliable Reinforcement Learning
  Implementations.
  *Journal of Machine Learning Research*, 22(268):1–8, 2021.
* Ordover and Willig [1981]

  Janusz A. Ordover and Robert D. Willig.
  An Economic Definition of Predation: Pricing and
  Product Innovation.
  *The Yale Law Journal*, 91(1):8–53, 1981.
* Belleflamme and
  Peitz [2010]

  Paul Belleflamme and Martin Peitz.
  *Industrial Organization: Markets and Strategies*.
  Cambridge University Press, 1 edition, January 2010.
* Petrazzini and
  Antonelo [2021]

  Irving G. B. Petrazzini and Eric A. Antonelo.
  Proximal policy optimization with continuous bounded action space via
  the beta distribution, 2021.
  URL <https://arxiv.org/abs/2111.02202>.

RL
:   reinforcement learning

MDP
:   Markov decision process

POMDP
:   partially observable Markov decision process

POMG
:   partially observable Markov game

NE
:   Nash equilibrium

MARL
:   multi-agent reinforcement learning

PPO
:   proximal policy optimization