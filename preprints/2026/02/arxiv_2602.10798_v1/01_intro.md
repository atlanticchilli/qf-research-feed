---
authors:
- Philippe Bergault
- Yadh Hafsi
- Leandro Sánchez-Betancourt
doc_id: arxiv:2602.10798v1
family_id: arxiv:2602.10798
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Trading in CEXs and DEXs with Priority Fees and Stochastic Delays
url_abs: http://arxiv.org/abs/2602.10798v1
url_html: https://arxiv.org/html/2602.10798v1
venue: arXiv q-fin
version: 1
year: 2026
---


Philippe Bergault
CEREMADE, Université Paris Dauphine-PSL

Yadh Hafsi
Yadh Hafsi acknowledges support of the Chaire Risque Financiers, Société Générale, at École Polytechnique. He also acknowledges support from the Institut Europlace de Finance (IEF).
CMAP, École Polytechnique

Leandro Sánchez-Betancourt

###### Abstract

We develop a mixed control framework that combines absolutely continuous controls with impulse interventions subject to stochastic execution delays.
The model extends current impulse control formulations by allowing (i) the controller to choose the mean of the stochastic delay of their impulses, and allowing (ii) for multiple pending orders, so that several impulses can be submitted and executed asynchronously at random times.
The framework is motivated by an optimal trading problem between centralized (CEX) and decentralized (DEX) exchanges. In DEXs, traders control the distribution of the execution delay through the priority fee paid, introducing a fundamental trade-off between delays, uncertainty, and costs.
We study the optimal trading problem of a trader exploiting trading signals in CEXs and DEXs.
From a mathematical perspective, we derive the associated dynamic programming principle of this new class of impulse control problems, and establish the viscosity properties of the corresponding quasi-variational inequalities. From a financial perspective, our model provides insights on how to carry out execution across CEXs and DEXs, highlighting how traders manage latency risk optimally through priority fee selection.
We show that employing the optimal priority fee has a significant outperformance over non-strategic fee selection.

Keywords: Impulse control with delay, priority fees, optimal trading, mixed-control, viscosity solutions, decentralised finance, automated market makers.

## 1 Introduction

The interplay between trading speed, execution uncertainty, and market structure has become increasingly prominent with the rise of decentralized exchanges (DEXs). Currently, within the crypto space, DEXs operate alongside traditional centralized exchanges (CEXs). In DEXs, traders face a fundamental trade-off between immediacy and execution risk, as the timing (position in queue) of order execution is subject to a stochastic delay that can be shortened by offering a “priority fee” to the miners. This motivates the need for the development of mathematical tools capable of capturing decision-making under delayed (and to some extent controlled) uncertain executions.
In this paper, we develop theory for a new type of impulse control problem with stochastic delay in which the controller can influence the stochastic delay of the execution of their impulses through a control variable.
We extend the literature in two key directions: (i) enabling control over the mean of the stochastic delay of the impulses, and (ii) allowing for multiple pending orders within the impulse control with stochastic delay framework. From a financial perspective, our framework provides a novel formulation for optimal trading between CEXs and DEXs, where the trader strategically selects priority fees to manage execution speed and risk.

A detailed summary of our contributions is as follows.
Mathematically, we introduce a framework that handles multiple pending orders within the class of impulse control problems with stochastic delay. Furthermore, we allow the controller to choose the mean of the random delay of each of their impulses. We combine a regular control, which models continuous trading on the CEX, with an impulse control, which models discrete order submissions to the DEX. Technically, adding the regular control means that between two impulse decisions, the state is continuously controlled with its own associated optimization. On the impulse side, closest to our work are [[20](https://arxiv.org/html/2602.10798v1#bib.bib31 "Optimal stopping with delayed information"), [19](https://arxiv.org/html/2602.10798v1#bib.bib18 "Optimal stochastic impulse control with delayed reaction"), [7](https://arxiv.org/html/2602.10798v1#bib.bib22 "Impulse control problem on finite horizon with execution delay")], where the authors investigate optimal stopping/impulse control problems with deterministic delay. In [[19](https://arxiv.org/html/2602.10798v1#bib.bib18 "Optimal stochastic impulse control with delayed reaction")], an infinite-horizon setting is considered with deterministic delay and an arbitrary number of pending orders, while [[7](https://arxiv.org/html/2602.10798v1#bib.bib22 "Impulse control problem on finite horizon with execution delay")] treats a finite-horizon problem with any finite number of pending orders. In these deterministic-delay models, the main technical burden comes from enforcing the associated boundary and consistency conditions induced by the fixed delay. By contrast, [[11](https://arxiv.org/html/2602.10798v1#bib.bib1 "Optimal execution with stochastic delay")] consider stochastic execution delay where the delay mechanism is exogenous and not a control variable. The controller chooses order submission times and sizes, while execution latency is governed by a given Poisson process, leading to a different structure in the intervention operator. The closest to our work is [[11](https://arxiv.org/html/2602.10798v1#bib.bib1 "Optimal execution with stochastic delay")], where the authors introduced an impulse control with uncontrolled stochastic delay and one pending order. Here, on the other hand, we control the mean of the stochastic delay and we allow for a finite number of pending orders.
Regarding the option of the controller to choose the mean of the stochastic delay, the closest work we are aware of is [[3](https://arxiv.org/html/2602.10798v1#bib.bib10 "Mean-field games of speedy information access with observation costs")], who deal with a Markov decision process and a discrete-time version of a controlled deterministic delay (in their framework this is called observation delay). As far as we are aware, our framework is the first to address optimal execution with random latency in which the trader can influence the mean of the latency distribution.

From a financial point of view and to the best of our knowledge, our work is the first to study optimal trading between centralised exchanges (CEX) and decentralised exchanges (DEX) employing the key degree of freedom that liquidity takers have when choosing the “priority fee” of their orders. We find the optimal decision boundaries that traders should employ when selecting the priority fee attached to their orders. Furthermore, we show how these regions change with time, inventory, and price discrepancies.
As expected, the performance of the trader increases with the number of priority fees they consider, but we find that this performance plateaus fairly quickly, which implies that entertaining a finite number of priority fees is close to optimal.
Within the CEX-DEX trading context, closest to our work are [[6](https://arxiv.org/html/2602.10798v1#bib.bib15 "DeFi arbitrage in hedged liquidity tokens"), [8](https://arxiv.org/html/2602.10798v1#bib.bib7 "Execution and statistical arbitrage with signals in multiple automated market makers"), [9](https://arxiv.org/html/2602.10798v1#bib.bib3 "Decentralised finance and automated market making: execution and speculation"), [15](https://arxiv.org/html/2602.10798v1#bib.bib5 "Model-free hedging of impermanent loss in geometric mean market makers with proportional transaction fees"), [17](https://arxiv.org/html/2602.10798v1#bib.bib6 "Arbitrage on decentralized exchanges"), [18](https://arxiv.org/html/2602.10798v1#bib.bib14 "Optimal trading in automatic market makers with deep learning")]. However, none of these works accounted for execution delay and the crucial (and yet understudied) role of the priority fees. To the best of our knowledge, this is the first framework to study trading in DEXs accounting for priority fees and execution delay.

The remainder of the paper proceeds as follows. Section [2](https://arxiv.org/html/2602.10798v1#S2 "2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays") formulates the mixed control problem with stochastic execution delay. Section [3](https://arxiv.org/html/2602.10798v1#S3 "3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays") establishes the dynamic programming principle and characterizes the value function via the associated Hamilton–Jacobi–Bellman quasi-variational inequality, showing that it is the unique viscosity solution of the HJBQVI. Section [4](https://arxiv.org/html/2602.10798v1#S4 "4 CEX-DEX Optimal Trading Problem ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays") applies the framework to an optimal trading problem in which the agent trades continuously on a centralized exchange and discretely on a decentralized exchange. It also provides numerical illustrations and studies how the optimal strategy varies across model specifications and parameter choices.

#### Notation.

For x∈ℝkx\in\mathbb{R}^{k}, where kk is determined by the context, ‖x‖\|x\| denotes its Euclidean norm, and Br​(x)B\_{r}(x) represents the open ball centred at xx with radius r>0r>0. The scalar product is denoted by ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle, and for a vector x∈ℝkx\in\mathbb{R}^{k}, its transpose is denoted by x⊤x^{\top}. For a set A⊂ℝkA\subset\mathbb{R}^{k}, ∂A\partial A denotes its boundary. For a function φ:ℝ+×ℝd×ℝk→ℝ\varphi:\mathbb{R}\_{+}\times\mathbb{R}^{d}\times\mathbb{R}^{k}\to\mathbb{R}, the gradient and Hessian matrix are denoted by D​φD\varphi and D2​φD^{2}\varphi, respectively, whenever they are well-defined. Lastly, ℕ⋆={1,2,3,…}\mathbb{N}^{\star}=\{1,2,3,\dots\}.

## 2 Problem Formulation

We consider a trading horizon T>0T>0 and a complete filtered probability space (Ω,ℱ={ℱt}t≥0,ℙ)(\Omega,\mathcal{F}=\{\mathcal{F}\_{t}\}\_{t\geq 0},\mathbb{P}), where {ℱt}t≥0\{\mathcal{F}\_{t}\}\_{t\geq 0} is a right-continuous filtration. We assume that the filtration 𝔽\mathbb{F} supports a qq-dimensional Brownian motion WW together with a collection of point processes (Ni)i∈ℐ(N^{i})\_{i\in\mathcal{I}} with ℐ=⟦1,N⟧\mathcal{I}=\llbracket 1,N\rrbracket, where N∈ℕ⋆N\in\mathbb{N}^{\star}.

For each i∈⟦1,N⟧i\in\llbracket 1,N\rrbracket, the sequence (Tni)n≥1(T^{i}\_{n})\_{n\geq 1}
defines a Poisson process with intensity ℓi>0\ell\_{i}>0. We take

|  |  |  |
| --- | --- | --- |
|  | Nti=∑n=0+∞𝟙{Tni≤t},∀i∈ℐ,N^{i}\_{t}=\sum\_{n=0}^{+\infty}\mathds{1}\_{\{T^{i}\_{n}\leq t\}},\quad\forall i\in{\cal I}, |  |

with convention N0−i=0N^{i}\_{0-}=0.
Let 𝔾0\mathbb{G}^{0} be the filtration associated to WW and the collection of NN point processes (Ni)i∈ℐ(N^{i})\_{i\in{\cal I}} such that

|  |  |  |
| --- | --- | --- |
|  | 𝒢t0:=σ((Ws)0≤s≤t,(Nsi)0≤s≤t:i={1,…,N}).\mathcal{G}^{0}\_{t}:=\sigma\Big((W\_{s})\_{0\leq s\leq t},\;(N^{i}\_{s})\_{0\leq s\leq t}:\;i=\{1,\dots,N\}\Big). |  |

The natural filtration associated with WW and
(Ni)1≤i≤N(N^{i})\_{1\leq i\leq N} is then given by the usual augmentation

|  |  |  |
| --- | --- | --- |
|  | 𝒢t:=⋂u>t(𝒢u 0∨𝒩0),t≥0,\mathcal{G}\_{t}:=\bigcap\_{u>t}\big(\mathcal{G}\_{u}^{\,0}\vee\mathcal{N}\_{0}\big),\quad t\geq 0, |  |

where 𝒩0\mathcal{N}\_{0} denotes the ℙ\mathbb{P}-null sets of ℱ\mathcal{F}.

Here NN represents the number of available priority fees. In practice, agents transacting on a blockchain may choose any positive priority fee to attach to a given action (for instance, a swap on an AMM or a simple transfer). For tractability, we restrict this choice to a finite set of NN possible priority fee levels. This discretization is a mild modelling simplification: it does not alter the qualitative behaviour of the system nor the nature of the results, but it allows us to work with a well-defined and finite family of point processes.

We work in a setup with up to KK pending orders and with each order the controller may choose one of the NN expected delays with an associated fee.
Each fee level corresponds to an expected execution delay, although the actual execution time is random.
For i∈{1,…,N}i\in\{1,\dots,N\}, the cost of priority fee ii is denoted by 𝔭i>0\mathfrak{p}\_{i}>0, and the associated expected execution delay is ℓi>0\ell\_{i}>0.
For convenience we assume that if i<ji<j then 𝔭i<𝔭j\mathfrak{p}\_{i}<\mathfrak{p}\_{j} and ℓi>ℓj\ell\_{i}>\ell\_{j}.
We define the fee vector 𝔭={𝔭1,…,𝔭N}\mathfrak{p}=\{\mathfrak{p}\_{1},\dots,\mathfrak{p}\_{N}\} and the delay vector 𝔩={ℓ1,…,ℓN}\mathfrak{l}=\{\ell\_{1},\dots,\ell\_{N}\}.

To describe the agent’s discrete trading decisions, we introduce an impulse control

|  |  |  |
| --- | --- | --- |
|  | (τn,In,ξn)n≥1,(\tau\_{n},I\_{n},\xi\_{n})\_{n\geq 1}, |  |

which specifies the sequence of intervention times, priority fee indexes, and order sizes. Formally, (τn,In,ξn)n≥1(\tau\_{n},I\_{n},\xi\_{n})\_{n\geq 1} consists of a non-decreasing sequence of 𝔾\mathbb{G}-stopping times (intervention times) τn≤T\tau\_{n}\leq T, priority indexes In∈ℐI\_{n}\in\mathcal{I}, and impulse actions ξn∈𝒰:=[−V^,V^]\xi\_{n}\in{\cal U}:=[-\hat{V},\hat{V}] for V^>0\hat{V}>0. These impulse actions represent the volume to be executed (positive for buys orders and negative for sells). For a given (τn,In)(\tau\_{n},I\_{n}), let mm (which depends on τn\tau\_{n}) be such that Tm−1In≤τn<TmInT^{I\_{n}}\_{m-1}\leq\tau\_{n}<T^{I\_{n}}\_{m}, then, define τ~n=TmIn\tilde{\tau}\_{n}=T^{I\_{n}}\_{m}. In words, τ~n\tilde{\tau}\_{n} is the next time after τn\tau\_{n} where we observe a jump from the point process NInN^{I\_{n}}. In what follows we use the notation ⋅~\tilde{\cdot} to denote execution times.

In addition to impulse decisions, the agent controls an absolutely continuous trading rate. We denote by ν=(νt)t∈[0,T]\nu=(\nu\_{t})\_{t\in[0,T]} a 𝔾\mathbb{G}-progressively measurable càdlàg process such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0Tνs2​𝑑s]<+∞.\mathbb{E}\Big[\int\_{0}^{T}\nu\_{s}^{2}\,ds\Big]<+\infty. |  |

We interpret νt\nu\_{t} as the signed continuous trading speed at time tt on the centralized exchange (CEX). Formally, the agent’s control is the pair

|  |  |  |
| --- | --- | --- |
|  | α:=((νt)t∈[0,T],(τn,In,ξn)n≥1).\alpha:=\Big((\nu\_{t})\_{t\in[0,T]},(\tau\_{n},I\_{n},\xi\_{n})\_{n\geq 1}\Big). |  |

We introduce the 𝔾\mathbb{G}-adapted process ι​(⋅,α)\iota(\cdot,\alpha), such that ι​(t,α)\iota(t,\alpha) returns the ordered indexes of the
pending orders at time tt under strategy α\alpha

|  |  |  |
| --- | --- | --- |
|  | ι​(t,α):={n≥1:τn≤t<τ~n}.\iota(t,\alpha):=\{n\geq 1:\tau\_{n}\leq t<\tilde{\tau}\_{n}\}. |  |

Let k​(⋅,α)k(\cdot,\alpha) be a 𝔾\mathbb{G}-adapted process defined by k​(t,α):=card⁡(ι​(t,α))k(t,\alpha):=\operatorname{card}(\iota(t,\alpha)),
so that k​(t,α)∈⟦0,K⟧k(t,\alpha)\in\llbracket 0,K\rrbracket represents the number of pending actions at time t∈[0,T]t\in[0,T].
We define the pending orders as

|  |  |  |
| --- | --- | --- |
|  | 𝔓​(t,α):=(Ii,ξi)i∈ι​(t,α).\mathfrak{P}(t,\alpha):=(I\_{i},\xi\_{i})\_{i\in\iota(t,\alpha)}. |  |

We introduce the KK-dimensional vectors representing, respectively, the number of pending orders at each priority level and the associated pending volumes, defined by

|  |  |  |
| --- | --- | --- |
|  | 𝔦​(t,α)=(∑i∈ι​(t,α)𝟙{Ii=1},…,∑i∈ι​(t,α)𝟙{Ii=K})​and​𝔳​(t,α)=(∑i∈ι​(t,α)ξi​ 1{Ii=1},…,∑i∈ι​(t,α)ξi​ 1{Ii=K}).\begin{aligned} \mathfrak{i}(t,\alpha)=\bigg(\sum\_{i\in\iota(t,\alpha)}\mathds{1}\_{\{I\_{i}=1\}},\dots,\sum\_{i\in\iota(t,\alpha)}\mathds{1}\_{\{I\_{i}=K\}}\bigg)~~\text{and}~~\mathfrak{v}(t,\alpha)=\bigg(\sum\_{i\in\iota(t,\alpha)}\xi\_{i}\,\mathds{1}\_{\{I\_{i}=1\}},\dots,\sum\_{i\in\iota(t,\alpha)}\xi\_{i}\,\mathds{1}\_{\{I\_{i}=K\}}\bigg).\end{aligned} |  |

In the above, we use the convention that ∑i∈∅\sum\_{i\in\emptyset} is zero. Lastly, we let

|  |  |  |
| --- | --- | --- |
|  | p​(t,α)=(𝔦​(t,α),𝔳​(t,α)).p(t,\alpha)=\big(\mathfrak{i}(t,\alpha),\mathfrak{v}(t,\alpha)\big)\,. |  |

Therefore, the set of admissible strategies for KK pending orders is

|  |  |  |
| --- | --- | --- |
|  | 𝒜K={α=((νt)t∈[0,T],(τn,In,ξn⏟intervention time, priority index, volume)n≥1):for ​n≥1,In∈ℐ,ξn∈𝒰,ν​is càdlàg 𝔾-progressively measurable,𝔼​[∫0Tνs2​ds]<+∞,k(t,α)≤K for all t∈[0,T], and τn are ordered 𝔾-stopping times}.\begin{aligned} \mathcal{A}\_{K}=\bigg\{\alpha=\big((\nu\_{t})\_{t\in[0,T]},(\hskip-50.00008pt\underbrace{\tau\_{n},I\_{n},\xi\_{n}}\_{\text{intervention time, priority index, volume}}\hskip-50.00008pt)\_{n\geq 1}\big):\,&\text{for }n\geq 1,\,I\_{n}\in\mathcal{I},\,\,\xi\_{n}\in{\cal U},\,\nu~\text{is càdlàg $\mathbb{G}$-progressively measurable,}\\ \mathbb{E}\bigg[\int\_{0}^{T}\nu^{2}\_{s}\mathrm{d}s\bigg]<+\infty&,\;k(t,\alpha)\leq K\text{ for all }t\in[0,T],\text{ and }\tau\_{n}\text{ are ordered $\mathbb{G}$-stopping times}\bigg\}\,.\end{aligned} |  |

With a slight abuse of notation, the set of admissible strategies at time t∈[0,T)t\in[0,T) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜K​(t)={α=((νs)s∈[t,T],(τn,In,ξn)n≥1)∈𝒜K:τ1≥t}.\displaystyle\mathcal{A}\_{K}(t)=\Big\{\alpha=\big((\nu\_{s})\_{s\in[t,T]},(\tau\_{n},I\_{n},\xi\_{n})\_{n\geq 1}\big)\in\mathcal{A}\_{K}\,:\,\tau\_{1}\geq t\Big\}\,. |  | (1) |

###### Lemma 2.1.

Let α=((νt)t∈[0,T],(τn,In,ξn)n≥1)∈𝒜K\alpha=\big((\nu\_{t})\_{t\in[0,T]},(\tau\_{n},I\_{n},\xi\_{n})\_{n\geq 1}\big)\in\mathcal{A}\_{K}. The following two properties hold.

1. 1.

   (τ~n)n∈ℕ(\tilde{\tau}\_{n})\_{n\in\mathbb{N}} are 𝔾\mathbb{G}-stopping times.
2. 2.

   (τ~n−τn)n∈ℕ(\tilde{\tau}\_{n}-\tau\_{n})\_{n\in\mathbb{N}} are a collection random variables such that τ~n−τn\tilde{\tau}\_{n}-\tau\_{n} is exponentially distributed with parameter ℓIn\ell\_{I\_{n}}.

###### Proof.

The proof follows from Lemma 3.1 in [[11](https://arxiv.org/html/2602.10798v1#bib.bib1 "Optimal execution with stochastic delay")]. For part (ii) the result follows from the memoryless property of exponential random variables.
∎

The objective of the agent is to trade optimally over the time horizon [0,T][0,T]. We introduce the set

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕀m={(i1,…,iN)∈⟦0,K⟧N:∑j=1Nij=m},\mathbb{I}\_{m}=\bigg\{(i\_{1},\dots,i\_{N})\in{\llbracket 0,K\rrbracket}^{N}\,:\,\sum\_{j=1}^{N}i\_{j}=m\bigg\}\,, |  | (2) |

which gathers all possible configurations of m∈⟦0,K⟧m\in{\llbracket 0,K\rrbracket} pending orders per priority index.
Similarly,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕍1={(v1,…,vN)∈𝒰N:∃j∈⟦1,N⟧​ s.t. ​vj≠0​ and ​vi=0​ for ​i≠j,i∈⟦1,N⟧},\mathbb{V}\_{1}=\Big\{(v\_{1},\dots,v\_{N})\in\mathcal{U}^{N}\,:\,\exists j\in\llbracket 1,N\rrbracket\text{ s.t. }v\_{j}\neq 0\text{ and }v\_{i}=0\text{ for }i\neq j,\quad i\in\llbracket 1,N\rrbracket\Big\}\,, |  | (3) |

and for m∈{2,…,K}m\in\{2,\dots,K\}, we define 𝕍m\mathbb{V}\_{m} recursively as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕍m=𝕍m−1+𝕍1={v+w:v∈𝕍m−1,w∈𝕍1}.\mathbb{V}\_{m}=\mathbb{V}\_{m-1}+\mathbb{V}\_{1}=\big\{v+w\,:\,v\in\mathbb{V}\_{m-1},\,\,w\in\mathbb{V}\_{1}\big\}\,. |  | (4) |

As a convention, we set 𝕀0=∅\mathbb{I}\_{0}=\varnothing, 𝕍0=∅\mathbb{V}\_{0}=\varnothing. We define the sets 𝕀\mathbb{I} and 𝕍\mathbb{V} as

|  |  |  |
| --- | --- | --- |
|  | 𝕀:=⋃0≤m≤K​𝕀m​and​𝕍:=⋃0≤m≤K​𝕍m.\mathbb{I}:=\underset{0\leq m\leq K}{\bigcup}\mathbb{I}\_{m}~~\text{and}~~\mathbb{V}:=\underset{0\leq m\leq K}{\bigcup}\mathbb{V}\_{m}. |  |

Let PP denote the function

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(t,u,𝔦)\displaystyle P(t,u,\mathfrak{i}) | =∑i=1N𝔦i​(1−𝟙{Nui>Nti}),∀ 0≤t≤u≤T,𝔦∈𝕀.\displaystyle=\sum\_{i=1}^{N}\mathfrak{i}\_{i}\left(1-\mathds{1}\_{\{N^{i}\_{u}>N^{i}\_{t}\}}\right),\quad\forall\;0\leq t\leq u\leq T,\;\mathfrak{i}\in\mathbb{I}. |  |

Intuitively, if the vector 𝔦\mathfrak{i} encodes the set of pending orders at time tt, then P​(t,u,𝔦)P(t,u,\mathfrak{i}) represents the number of those initial orders that remain pending at time u≥tu\geq t.
We also define the pending volume to be

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,u,𝔳)\displaystyle V(t,u,\mathfrak{v}) | =∑i=1N|𝔳i|​(1−𝟙{Nui>Nti}),∀ 0≤t≤u≤T,𝔳∈𝕍.\displaystyle=\sum\_{i=1}^{N}|\mathfrak{v}\_{i}|\left(1-\mathds{1}\_{\{N^{i}\_{u}>N^{i}\_{t}\}}\right),\quad\forall\;0\leq t\leq u\leq T,\;\mathfrak{v}\in\mathbb{V}. |  |

Based on these quantities, we introduce the admissible control set

|  |  |  |
| --- | --- | --- |
|  | 𝒜K,𝔦,𝔳​(t)={α=((νs)s∈[t,T],(τn,In,ξn)n≥1)∈𝒜K​(t):k​(s,α)≤K−P​(t−,s,𝔦)​and​V​(t,s,𝔳)≤V¯,∀s∈[t,T]},\begin{aligned} \mathcal{A}\_{K,\mathfrak{i},\mathfrak{v}}(t)=\Big\{\alpha=\big((\nu\_{s})\_{s\in[t,T]},(\tau\_{n},I\_{n},\xi\_{n})\_{n\geq 1}\big)\in\mathcal{A}\_{K}(t):k(s,\alpha)\leq K-P(t^{-},s,\mathfrak{i})~\text{and}~V(t,s,\mathfrak{v})\leq\bar{V},~\forall s\in[t,T]\Big\},\end{aligned} |  |

with the convention 𝒜K,𝔦,0​(0):=𝒜K\mathcal{A}\_{K,\mathfrak{i},0}(0):=\mathcal{A}\_{K}, for all 𝔦∈𝕀\mathfrak{i}\in\mathbb{I}. The quantity V¯\bar{V} is a trading constraint; such constraint is not necessarily the inventory because we are not restricted to an optimal liquidation problem. The condition V​(t,s,𝔳)≤V¯V(t,s,\mathfrak{v})\leq\bar{V} establishes that the pending volume waiting to be executed in the AMM cannot exceed V¯\bar{V}.

At execution τ~n\tilde{\tau}\_{n}, the controlled càdlàg state X=(Xt)t∈[0,T]X=(X\_{t})\_{t\in[0,T]} jumps according to a measurable impulse map Γ\Gamma. For t∈[0,T]t\in[0,T] and a given policy α∈𝒜K​(t)\alpha\in{\cal A}\_{K}(t), the dynamics of the dd-dimensional state process XX are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Xut,x,α\displaystyle X^{t,x,\alpha}\_{u} | =x+∫tub​(s,Xst,x,α,νs)​ds+∫tuσ​(s,Xst,x,α,νs)​dWs+∑t≤τ~n≤u(Γ​(τ~n,Xτ~n−t,x,α,ξn)−Xτ~n−t,x,α),\displaystyle=x+\int\_{t}^{u}b(s,X^{t,x,\alpha}\_{s},\nu\_{s})\,\mathrm{d}s+\int\_{t}^{u}\sigma(s,X^{t,x,\alpha}\_{s},\nu\_{s})\,\mathrm{d}W\_{s}+\sum\_{t\leq\tilde{\tau}\_{n}\leq u}\big(\Gamma(\tilde{\tau}\_{n},X^{t,x,\alpha}\_{\tilde{\tau}\_{n}^{-}},\xi\_{n})-X^{t,x,\alpha}\_{\tilde{\tau}\_{n}^{-}}\big), |  | (5) |

for t∈[0,T]t\in[0,T], with measurable coefficients b:[0,T]×ℝd×ℝ→ℝdb:[0,T]\times\mathbb{R}^{d}\times\mathbb{R}\to\mathbb{R}^{d}, σ:[0,T]×ℝd×ℝ→ℝd×q\sigma:[0,T]\times\mathbb{R}^{d}\times\mathbb{R}\to\mathbb{R}^{d\times q},
Γ:[0,T]×ℝd×𝒰→ℝd\Gamma:[0,T]\times\mathbb{R}^{d}\times{\cal U}\to\mathbb{R}^{d}.

Let t∈[0,T]t\in[0,T] and (x,𝔦,𝔳)∈𝒟(x,\mathfrak{i},\mathfrak{v})\in{\cal D}, where 𝒟{\cal D} defines the following domain

|  |  |  |
| --- | --- | --- |
|  | 𝒟:={(x,𝔦,𝔳):x∈ℝd,𝔦∈𝕀,𝔳∈𝕍,∑i|𝔳i|<V¯}.{\cal D}:=\Big\{(x,\mathfrak{i},\mathfrak{v}):x\in\mathbb{R}^{d},\;\mathfrak{i}\in\mathbb{I},\;\mathfrak{v}\in\mathbb{V},\;\sum\_{i}|\mathfrak{v}\_{i}|<\bar{V}\Big\}. |  |

Here, the elements (𝔦,𝔳)=(0𝕀,0𝕍)(\mathfrak{i},\mathfrak{v})=(0\_{\mathbb{I}},0\_{\mathbb{V}}) denote the absence of pending orders. Let f:[0,T]×ℝ×ℝd→ℝf:[0,T]\times\mathbb{R}\times\mathbb{R}^{d}\to\mathbb{R} be a running reward, g:ℝd→ℝg:\mathbb{R}^{d}\to\mathbb{R} a terminal payoff, and
c:[0,T]×ℝd×𝒰×𝕀→ℝ+c:[0,T]\times\mathbb{R}^{d}\times{\cal U}\times\mathbb{I}\to\mathbb{R}\_{+} an intervention cost. For any admissible control α∈𝒜K,𝔦,𝔳​(t)\alpha\in{\cal A}\_{K,\mathfrak{i},\mathfrak{v}}(t), we define the performance criterion

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,x,α)=𝔼​[∫tTf​(s,Xst,x,α,νs)​ds+g​(XTt,x,α)−∑n≥1:τ~n∈(t,T]c​(τ~n,Xτ~n−t,x,α,ξn,In)].J(t,x,\alpha)=\mathbb{E}\bigg[\int\_{t}^{T}f(s,X^{t,x,\alpha}\_{s},\nu\_{s})\,\mathrm{d}s+g(X^{t,x,\alpha}\_{T})-\sum\_{n\geq 1:\,\tilde{\tau}\_{n}\in(t,T]}c(\tilde{\tau}\_{n},X^{t,x,\alpha}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})\bigg]. |  | (6) |

The associated value function is then given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t,x,𝔦,𝔳):=supα∈𝒜K,𝔦,𝔳​(t)J​(t,x,α),∀(t,x,𝔦,𝔳)∈[0,T]×𝒟.v(t,x,\mathfrak{i},\mathfrak{v}):=\sup\_{\alpha\in{\cal A}\_{K,\mathfrak{i},\mathfrak{v}}(t)}J(t,x,\alpha),\quad\forall(t,x,\mathfrak{i},\mathfrak{v})\in[0,T]\times{\cal D}. |  | (7) |

In particular, when there are no pending orders, the state reduces to
(x,0𝕀,0𝕍)∈𝒟(x,0\_{\mathbb{I}},0\_{\mathbb{V}})\in{\cal D}, and the value function defined in ([7](https://arxiv.org/html/2602.10798v1#S2.E7 "In 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) coincides with the one obtained under 𝒜K,0,0​(t)\mathcal{A}\_{K,0,0}(t).

###### Assumption 2.1.

We assume that the following holds.

* (A1)

  The maps bb, Γ\Gamma, ff, gg and cc are Borel measurable. Moreover, cc is continuous, nonnegative,
  and verifies c​(t,x,0,i)=0c(t,x,0,i)=0 for all (t,x,i)∈[0,T]×ℝd×⟦1,N⟧(t,x,i)\in[0,T]\times\mathbb{R}^{d}\times\llbracket 1,N\rrbracket.
* (A2)

  There exists L>0L>0 such that, for all
  t∈[0,T]t\in[0,T], (a,a′)∈ℝ2(a,a^{\prime})\in\mathbb{R}^{2}, (x,x′)∈(ℝd)2(x,x^{\prime})\in(\mathbb{R}^{d})^{2} and ξ∈𝒰\xi\in{\cal U},

  |  |  |  |
  | --- | --- | --- |
  |  | ‖b​(t,x,a)−b​(t,x′,a′)‖+‖σ​(t,x,a)−σ​(t,x′,a′)‖+‖Γ​(t,x,ξ)−Γ​(t,x′,ξ)‖≤L​(‖x−x′‖+L​|a−a′|).\|b(t,x,a)-b(t,x^{\prime},a^{\prime})\|+\|\sigma(t,x,a)-\sigma(t,x^{\prime},a^{\prime})\|+\|\Gamma(t,x,\xi)-\Gamma(t,x^{\prime},\xi)\|\leq L(\|x-x^{\prime}\|+L|a-a^{\prime}|). |  |
* (A3)

  There exists C0>0C\_{0}>0 such that, for all (t,x,a,ζ)∈[0,T]×ℝd×ℝ×𝒰(t,x,a,\zeta)\in[0,T]\times\mathbb{R}^{d}\times\mathbb{R}\times{\cal U} and all i∈⟦1,N⟧i\in\llbracket 1,N\rrbracket,

  |  |  |  |
  | --- | --- | --- |
  |  | ‖b​(t,x,a)‖+‖σ​(t,x,a)‖+‖Γ​(t,x,ξ)‖+|c​(t,x,ξ,i)|≤C0​(1+‖x‖+|a|+‖ξ‖).\|b(t,x,a)\|+\|\sigma(t,x,a)\|+\|\Gamma(t,x,\xi)\|+|c(t,x,\xi,i)|\leq C\_{0}\big(1+\|x\|+|a|+\|\xi\|\big). |  |
* (A4)

  There exists Lf,Lg>0L\_{f},L\_{g}>0 such that, for all t∈[0,T]t\in[0,T], x,x′∈ℝdx,x^{\prime}\in\mathbb{R}^{d} and a∈ℝa\in\mathbb{R},

  |  |  |  |
  | --- | --- | --- |
  |  | |f​(t,x,a)−f​(t,x′,a)|≤Lf​(1+|a|)​‖x−x′‖​and​|g​(x)−g​(x′)|≤Lg​‖x−x′‖.|f(t,x,a)-f(t,x^{\prime},a)|\leq L\_{f}(1+|a|)\,\|x-x^{\prime}\|~~\textrm{and}~~|g(x)-g(x^{\prime})|\leq L\_{g}\,\|x-x^{\prime}\|. |  |
* (A5)

  For all (t,𝔦,𝔳)∈[0,T]×𝕀×𝕍(t,\mathfrak{i},\mathfrak{v})\in[0,T]\times\mathbb{I}\times\mathbb{V}, we have that

  |  |  |  |
  | --- | --- | --- |
  |  | supα∈𝒜K,𝔦,𝔳​(t)𝔼​[∫tT|f​(s,0,νs)|​ds]≤+∞.\sup\_{\alpha\in{\cal A}\_{K,\mathfrak{i},\mathfrak{v}}(t)}\mathbb{E}\left[\int\_{t}^{T}|f(s,0,\nu\_{s})|\,\mathrm{d}s\right]\leq+\infty. |  |
* (A6)

  There exists λ>0\lambda>0 such that, for all (t,x,a)∈[0,T]×ℝd×ℝ(t,x,a)\in[0,T]\times\mathbb{R}^{d}\times\mathbb{R} and all ζ∈ℝd\zeta\in\mathbb{R}^{d},

  |  |  |  |
  | --- | --- | --- |
  |  | ζ⊤​σ​σ⊤​(t,x,a)​ζ≥λ​‖ζ‖2.\zeta^{\top}\sigma\sigma^{\top}(t,x,a)\,\zeta\;\geq\;\lambda\,\|\zeta\|^{2}. |  |

In the remainder of this work, the assumptions in [2.1](https://arxiv.org/html/2602.10798v1#S2.ThmAssumption1 "Assumption 2.1. ‣ 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays") hold. We now state the existence and uniqueness result for the controlled process XX.

###### Proposition 2.2.

Let t∈[0,T]t\in[0,T]. For any ℱt{\cal F}\_{t}-measurable random variable ξ\xi valued in ℝ+\mathbb{R}\_{+} such that 𝔼​(|ξ|p)<+∞\mathbb{E}(|\xi|^{p})<+\infty, for some p>1p>1, the SDE ([5](https://arxiv.org/html/2602.10798v1#S2.E5 "In 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) admits a unique strong solution Xt,ξ,αX^{t,\xi,\alpha} under the assumptions (A1)–(A5). Moreover, there exists CT>0C\_{T}>0 such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[sup0≤u≤T​‖Xut,ξ,α‖p]≤CT​(1+𝔼​(|ξ|p)).\mathbb{E}\bigg[\underset{0\leq u\leq T}{\sup}\|X^{t,\xi,\alpha}\_{u}\|^{p}\bigg]\leq C\_{T}\big(1+\mathbb{E}(|\xi|^{p})\big). |  |

###### Proof.

The proof is standard and it follows closely the arguments in [[22](https://arxiv.org/html/2602.10798v1#bib.bib20 "Stochastic integration and differential equations"), Chapter V].
∎

We conclude this section by stating the growth bounds satisfied by the value function.

###### Lemma 2.3 (Quadratic growth).

There exists positive constants C1,C2>0C\_{1},C\_{2}>0 such that, for all
(t,x,𝔦,𝔳)∈[0,T]×𝒟(t,x,\mathfrak{i},\mathfrak{v})\in[0,T]\times{\cal D},

|  |  |  |  |
| --- | --- | --- | --- |
|  | C1​(1+‖x‖)≤|v​(t,x,𝔦,𝔳)|≤C2​(1+‖x‖2).C\_{1}\bigl(1+\|x\|\bigr)\;\leq\;|v(t,x,\mathfrak{i},\mathfrak{v})|\;\leq\;C\_{2}\bigl(1+\|x\|^{2}\bigr). |  | (8) |

###### Proof.

The result follows from the growth conditions on ff, gg and cc, the moment bounds for the solution of the SDE ([5](https://arxiv.org/html/2602.10798v1#S2.E5 "In 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) from Proposition [2.2](https://arxiv.org/html/2602.10798v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays"), the finite jump activity of (Ni)i∈⟦1,K⟧(N^{i})\_{i\in\llbracket 1,K\rrbracket} and the boundedness of ξ\xi.
∎

## 3 Viscosity Characterization of the Value Function

In what follows we drop the argument of a mathematical object if it is the empty set.

### 3.1 Dynamic programming principle

###### Theorem 3.1 (Dynamic Programming Principle).

The value function vv defined in ([7](https://arxiv.org/html/2602.10798v1#S2.E7 "In 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) satisfy the dynamic programming principle (DPP).
That is, for (t,x)∈[0,T]×𝒟(t,x)\in[0,T]\times{\cal D}, and τ∈𝒯t,T\tau\in\mathcal{T}\_{t,T}, which is the set of 𝔾\mathbb{G}-stopping times valued in [t,T][t,T], we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t,x,𝔦,𝔳)=supα∈𝒜K,𝔦,𝔳​(t)𝔼​[∫tτf​(s,Xst,x,α,νs)​ds−∑τ~n∈(t,τ]c​(τ~n,Xτ~n−t,x,α,ξn,In)+v​(τ,Xτt,x,α,p​(τ,α))].v(t,x,\mathfrak{i},\mathfrak{v})=\sup\_{\alpha\in{\cal A}\_{K,\mathfrak{i},\mathfrak{v}}(t)}\mathbb{E}\Bigg[\int\_{t}^{\tau}f\big(s,X\_{s}^{t,x,\alpha},\nu\_{s}\big)\,\mathrm{d}s-\sum\_{\tilde{\tau}\_{n}\in(t,\tau]}c(\tilde{\tau}\_{n},X^{t,x,\alpha}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})+v\left(\tau,X\_{\tau}^{t,x,\alpha},p(\tau,\alpha)\right)\Bigg]. |  | (9) |

In other words, the following two statements hold.

1. 1.

   (DPP1) For all α∈𝒜K,𝔦,𝔳​(t)\alpha\in{\cal A}\_{K,\mathfrak{i},\mathfrak{v}}(t) and for all stopping times τ\tau valued in [t,T][t,T],

   |  |  |  |
   | --- | --- | --- |
   |  | v​(t,x,𝔦,𝔳)≥𝔼​[∫tτf​(s,Xst,x,α,νs)​ds−∑τ~n∈(t,τ]c​(τ~n,Xτ~n−t,x,α,ξn,In)+v​(τ,Xτt,x,α,p​(τ,α))].v(t,x,\mathfrak{i},\mathfrak{v})\geq\mathbb{E}\Bigg[\int\_{t}^{\tau}f\big(s,X\_{s}^{t,x,\alpha},\nu\_{s}\big)\,\mathrm{\mathrm{d}}s-\sum\_{\tilde{\tau}\_{n}\in(t,\tau]}c(\tilde{\tau}\_{n},X^{t,x,\alpha}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})+v\left(\tau,X\_{\tau}^{t,x,\alpha},p(\tau,\alpha)\right)\Bigg]. |  |
2. 2.

   (DPP2) For every ε>0\varepsilon>0, there exists αε∈𝒜K,𝔦,𝔳​(t)\alpha^{\varepsilon}\in{\cal A}\_{K,\mathfrak{i},\mathfrak{v}}(t) such that for all stopping times τ\tau valued in [t,T][t,T],

   |  |  |  |
   | --- | --- | --- |
   |  | v​(t,x,𝔦,𝔳)−ε≤𝔼​[∫tτf​(s,Xst,x,αε,νs)​ds−∑τ~n∈(t,τ]c​(τ~n,Xτ~n−t,x,αε,ξn,In)+v​(τ,Xτt,x,αε,p​(τ,αε))].v(t,x,\mathfrak{i},\mathfrak{v})-\varepsilon\leq\mathbb{E}\Bigg[\int\_{t}^{\tau}f\big(s,X\_{s}^{t,x,\alpha^{\varepsilon}},\nu\_{s}\big)\,\mathrm{\mathrm{d}}s-\sum\_{\tilde{\tau}\_{n}\in(t,\tau]}c(\tilde{\tau}\_{n},X^{t,x,\alpha^{\varepsilon}}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})+v\left(\tau,X\_{\tau}^{t,x,\alpha^{\varepsilon}},p(\tau,\alpha^{\varepsilon})\right)\Bigg]. |  |

###### Proof.

(1) Let (t,x,𝔦,𝔳)∈[0,T]×𝒟(t,x,\mathfrak{i},\mathfrak{v})\in[0,T]\times{\cal D}, ε>0\varepsilon>0, τ∈𝒯t,T\tau\in\mathcal{T}\_{t,T}, and α∈𝒜K,𝔦,𝔳​(t)\alpha\in\mathcal{A}\_{K,\mathfrak{i},\mathfrak{v}}(t). For any ω∈Ω\omega\in\Omega, there exists an ε\varepsilon-optimal control αε,ω∈𝒜K,p​(τ​(ω),α​(ω))​(τ​(ω))\alpha^{\varepsilon,\omega}\in{\cal A}\_{K,p(\tau(\omega),\alpha(\omega))}(\tau(\omega)) for
vv at

|  |  |  |
| --- | --- | --- |
|  | (τ​(ω),Xτ​(ω)t,x,α​(ω),p​(τ​(ω),α​(ω)))\big(\tau(\omega),X^{t,x,\alpha(\omega)}\_{\tau(\omega)},p(\tau(\omega),\alpha(\omega))\big) |  |

such that

|  |  |  |
| --- | --- | --- |
|  | v​(τ​(ω),Xτ​(ω)t,x,α​(ω),p​(τ​(ω),α​(ω)))−ε≤J​(τ​(ω),Xτ​(ω)t,x,α​(ω),α¯ε​(ω)).v\big(\tau(\omega),X^{t,x,\alpha(\omega)}\_{\tau(\omega)},p(\tau(\omega),\alpha(\omega))\big)-\varepsilon\leq J\big(\tau(\omega),X^{t,x,\alpha(\omega)}\_{\tau(\omega)},\bar{\alpha}^{\varepsilon}(\omega)\big). |  |

By measurable selection arguments (see [[5](https://arxiv.org/html/2602.10798v1#bib.bib23 "Stochastic optimal control: the discrete-time case"), Chapter VII]),
there exists
α¯ε∈𝒜K,p​(τ,α)​(τ)\bar{\alpha}^{\varepsilon}\in{\cal A}\_{K,p(\tau,\alpha)}(\tau)
such that

|  |  |  |
| --- | --- | --- |
|  | α¯ε​(ω)=αε,ω​(ω)for almost all ​ω∈Ω.\bar{\alpha}^{\varepsilon}(\omega)=\alpha^{\varepsilon,\omega}(\omega)\quad\text{for almost all }\omega\in\Omega. |  |

In other words,

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(τ,Xτt,x,α,p​(τ,α))−ε≤J​(τ,Xτt,x,α,α¯ε).v\big(\tau,X^{t,x,\alpha}\_{\tau},p(\tau,\alpha)\big)-\varepsilon\leq J\big(\tau,X^{t,x,\alpha}\_{\tau},\bar{\alpha}^{\varepsilon}\big). |  | (10) |

We define the strategy α~ε\tilde{\alpha}^{\varepsilon} as

|  |  |  |
| --- | --- | --- |
|  | α~uε={αu, if ​u<τ,α¯uε, otherwise.\displaystyle\tilde{\alpha}^{\varepsilon}\_{u}=\left\{\begin{array}[]{ll}\alpha\_{u},&\quad\text{ if }u<\tau,\\ \bar{\alpha}^{\varepsilon}\_{u},&\quad\text{ otherwise}.\end{array}\right. |  |

Note that α~ε∈𝒜K,𝔦,𝔳​(t)\tilde{\alpha}^{\varepsilon}\in{\cal A}\_{K,\mathfrak{i},\mathfrak{v}}(t). Indeed, progressive measurability follows from the fact that if
α\alpha and α~\tilde{\alpha} are progressively measurable and τ\tau is a stopping time,
then

|  |  |  |
| --- | --- | --- |
|  | u↦1l{u<τ}​αu+1l{u≥τ}​α¯uεu\mapsto\mbox{1\hskip-2.5ptl}\_{\{u<\tau\}}\alpha\_{u}+\mbox{1\hskip-2.5ptl}\_{\{u\geq\tau\}}\bar{\alpha}^{\varepsilon}\_{u} |  |

is progressively measurable. Feasibility and integrability hold on [t,τ)[t,\tau)
by admissibility of α\alpha, and on [τ,T][\tau,T] by admissibility of α¯ε\bar{\alpha}^{\varepsilon}. Additionally, the number of impulses is respected because
α¯ε∈𝒜K,p​(τ,α)​(τ)\bar{\alpha}^{\varepsilon}\in\mathcal{A}\_{K,p(\tau,\alpha)}(\tau). The non-accumulation property is preserved by
construction (see [[19](https://arxiv.org/html/2602.10798v1#bib.bib18 "Optimal stochastic impulse control with delayed reaction"), Chapter IX]).
Now using the law of iterated conditional expectations and ([10](https://arxiv.org/html/2602.10798v1#S3.E10 "In Proof. ‣ 3.1 Dynamic programming principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")), we get that

|  |  |  |
| --- | --- | --- |
|  | J​(t,x,α~ε)≥𝔼​[∫tτf​(s,Xst,x,α~ε,νs)​ds−∑n≥1:τ~n∈(t,τ]c​(τ~n,Xτ~n−t,x,α~ε,ξn,In)+v​(τ,Xτt,x,α~ε,p​(τ,α~ε))]−ε≥𝔼​[∫tτf​(s,Xst,x,α,νs)​ds−∑n≥1:τ~n∈(t,τ]c​(τ~n,Xτ~n−t,x,α,ξn,In)+v​(τ,Xτt,x,α,p​(τ,α))]−ε.\begin{aligned} J(t,x,\tilde{\alpha}^{\varepsilon})&\geq\mathbb{E}\bigg[\int\_{t}^{\tau}f(s,X^{t,x,\tilde{\alpha}^{\varepsilon}}\_{s},\nu\_{s})\,\mathrm{d}s-\sum\_{n\geq 1:\,\tilde{\tau}\_{n}\in(t,\tau]}c(\tilde{\tau}\_{n},X^{t,x,\tilde{\alpha}^{\varepsilon}}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})+v\left(\tau,X\_{\tau}^{t,x,\tilde{\alpha}^{\varepsilon}},p(\tau,\tilde{\alpha}^{\varepsilon})\right)\bigg]-\varepsilon\\ &\geq\mathbb{E}\bigg[\int\_{t}^{\tau}f(s,X^{t,x,\alpha}\_{s},\nu\_{s})\,\mathrm{d}s-\sum\_{n\geq 1:\,\tilde{\tau}\_{n}\in(t,\tau]}c(\tilde{\tau}\_{n},X^{t,x,\alpha}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})+v\left(\tau,X\_{\tau}^{t,x,\alpha},p(\tau,\alpha)\right)\bigg]-\varepsilon.\end{aligned} |  |

The last inequality holds as α¯\bar{\alpha} coincides with α\alpha up to time τ\tau. This completes the proof since α\alpha, τ\tau, and ε\varepsilon are arbitrary.

(2) Let (t,x,𝔦,𝔳)∈[0,T]×𝒟(t,x,\mathfrak{i},\mathfrak{v})\in[0,T]\times{\cal D} and τ∈𝒯t,T\tau\in\mathcal{T}\_{t,T}. For α∈𝒜K,𝔦,𝔳​(t)\alpha\in\mathcal{A}\_{K,\mathfrak{i},\mathfrak{v}}(t), the law of iterated conditional expectations gives

|  |  |  |
| --- | --- | --- |
|  | J​(t,x,α)=𝔼[∫tτf(s,Xst,x,α,νs)ds−∑n≥1:τ~n∈(t,τ]c(τ~n,Xτ~n−t,x,α,ξn,In)+𝔼[∫τTf(s,Xst,x,α,νs)ds−∑n≥1:τ~n∈(τ,T]c(τ~n,Xτ~n−t,x,α,ξn,In)+g(XTt,x,α)∣ℱτ]].\begin{split}J(t,x,\alpha)&=\mathbb{E}\bigg[\int\_{t}^{\tau}f(s,X^{t,x,\alpha}\_{s},\nu\_{s})\,\mathrm{d}s-\sum\_{n\geq 1:\,\tilde{\tau}\_{n}\in(t,\tau]}c(\tilde{\tau}\_{n},X^{t,x,\alpha}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})\\ &\quad\qquad+\mathbb{E}\Big[\int\_{\tau}^{T}f(s,X^{t,x,\alpha}\_{s},\nu\_{s})\,\mathrm{d}s-\sum\_{n\geq 1:\,\tilde{\tau}\_{n}\in(\tau,T]}c(\tilde{\tau}\_{n},X^{t,x,\alpha}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})+g(X^{t,x,\alpha}\_{T})\mid{\cal F}\_{\tau}\Big]\bigg].\end{split} |  |

Using the memoryless property of the exponential delays (Lemma [2.1](https://arxiv.org/html/2602.10798v1#S2.Thmtheorem1 "Lemma 2.1. ‣ 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")), we obtain the joint Markov property of (Xut,x,α,p​(u,α))u≥t\big(X^{t,x,\alpha}\_{u},p(u,\alpha)\big)\_{u\geq t}. Combined with the pathwise uniqueness of Xt,x,αX^{t,x,\alpha} (Proposition [2.2](https://arxiv.org/html/2602.10798v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")), this yields

|  |  |  |
| --- | --- | --- |
|  | J​(t,x,α)=𝔼​[∫tτf​(s,Xst,x,α,νs)​ds−∑n≥1:τ~n∈(t,τ]c​(τ~n,Xτ~n−t,x,α,ξn,In)+J​(τ,Xτt,x,α,α)]≤𝔼​[∫tτf​(s,Xst,x,α,νs)​ds−∑n≥1:τ~n∈(t,θ]c​(τ~n,Xτ~n−t,x,α,ξn,In)+v​(τ,Xτt,x,α,p​(τ,α))].\begin{split}J(t,x,\alpha)&=\mathbb{E}\bigg[\int\_{t}^{\tau}f(s,X^{t,x,\alpha}\_{s},\nu\_{s})\,\mathrm{d}s-\sum\_{n\geq 1:\,\tilde{\tau}\_{n}\in(t,\tau]}c(\tilde{\tau}\_{n},X^{t,x,\alpha}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})+J\left(\tau,X\_{\tau}^{t,x,\alpha},\alpha\right)\bigg]\\ &\leq\mathbb{E}\bigg[\int\_{t}^{\tau}f(s,X^{t,x,\alpha}\_{s},\nu\_{s})\,\mathrm{d}s-\sum\_{n\geq 1:\,\tilde{\tau}\_{n}\in(t,\theta]}c(\tilde{\tau}\_{n},X^{t,x,\alpha}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})+v\left(\tau,X\_{\tau}^{t,x,\alpha},p(\tau,\alpha)\right)\bigg].\end{split} |  |

Since the control α\alpha is arbitrary, it follows that

|  |  |  |
| --- | --- | --- |
|  | v​(t,x,𝔦,𝔳)≤supα∈𝒜K,𝔦,𝔳​(t)𝔼​[∫tτf​(s,Xst,x,α,νs)​ds−∑τ~n∈(t,τ]c​(τ~n,Xτ~n−t,x,α,ξn,In)+v​(τ,Xτt,x,α,p​(τ,α))].\begin{aligned} v(t,x,\mathfrak{i},\mathfrak{v})\leq\sup\_{\alpha\in{\cal A}\_{K,\mathfrak{i},\mathfrak{v}}(t)}\mathbb{E}\Bigg[\int\_{t}^{\tau}f\big(s,X\_{s}^{t,x,\alpha},\nu\_{s}\big)\,\mathrm{\mathrm{d}}s-\sum\_{\tilde{\tau}\_{n}\in(t,\tau]}c(\tilde{\tau}\_{n},X^{t,x,\alpha}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})+v\left(\tau,X\_{\tau}^{t,x,\alpha},p(\tau,\alpha)\right)\Bigg].\end{aligned} |  |

∎

### 3.2 PDE Characterization and Comparison Principle

Building on the problem formulation in Section [2](https://arxiv.org/html/2602.10798v1#S2 "2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays"), we consider the following Hamilton-Jacobi-Bellman quasi-variational inequalities for vv on the domain [0,T]×𝒟[0,T]\times{\cal D}. If ∑i=1N⟨𝔦,ei⟩<K\sum\_{i=1}^{N}\langle\mathfrak{i},e\_{i}\rangle<K, then the QVI that characterizes the control problem in ([7](https://arxiv.org/html/2602.10798v1#S2.E7 "In 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | min{\displaystyle\min\bigg\{ | −∂v∂t(t,x,𝔦,𝔳)−supa∈ℝHa(t,x,𝔦,𝔳,v,∂v∂x,∂2v∂x2),(v−ℳv)(t,x,𝔦,𝔳)}=0,\displaystyle-\frac{\partial v}{\partial t}(t,x,\mathfrak{i},\mathfrak{v})-\sup\_{a\in\mathbb{R}}H^{a}\Big(t,x,\mathfrak{i},\mathfrak{v},v,\tfrac{\partial v}{\partial x},\tfrac{\partial^{2}v}{\partial x^{2}}\Big)\,,\,\big(v-\mathcal{M}v\big)(t,x,\mathfrak{i},\mathfrak{v})\bigg\}=0, |  | (11) |

where the non-local intervention operator ℳ:𝒞​([0,T]×𝒟)→𝒞​([0,T]×𝒟)\mathcal{M}:\mathcal{C}([0,T]\times{\cal D})\rightarrow\mathcal{C}([0,T]\times{\cal D}) is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳ​φ​(t,x,𝔦,𝔳):=sup(ξ,i)∈𝒰×⟦1,K⟧φ​(t,x,𝔦+ei,𝔳+ξ​ei),\mathcal{M}\varphi(t,x,\mathfrak{i},\mathfrak{v}):=\sup\_{(\xi,i)\in{\cal U}\times{\llbracket 1,K\rrbracket}}\varphi(t,x,\mathfrak{i}+e\_{i},\mathfrak{v}+\xi e\_{i}), |  | (12) |

the Hamiltonian Ha:[0,T]×𝒟×𝒞​([0,T]×𝒟)3→ℝH^{a}:[0,T]\times{\cal D}\times\mathcal{C}([0,T]\times{\cal D})^{3}\rightarrow\mathbb{R} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ha​(t,x,𝔦,𝔳,φ,∂φ∂x,∂2φ∂x2)=ℒa​φ​(t,x,𝔦,𝔳)⏟infinitesimal generator+𝒥​φ​(t,x,𝔦,𝔳)⏟execution of pending orders+f​(t,x,a)⏟running rewards,\begin{split}&H^{a}\Big(t,x,\mathfrak{i},\mathfrak{v},\varphi,\tfrac{\partial\varphi}{\partial x},\tfrac{\partial^{2}\varphi}{\partial x^{2}}\Big)=\underbrace{\mathcal{L}^{a}\varphi(t,x,\mathfrak{i},\mathfrak{v})}\_{\text{infinitesimal generator}}\;+\;\underbrace{\mathcal{J}\varphi(t,x,\mathfrak{i},\mathfrak{v})}\_{\text{execution of pending orders}}\;+\;\underbrace{f(t,x,a)}\_{\text{running rewards}},\end{split} |  | (13) |

the partial differential operator ℒa:[0,T]×ℝd×𝒞1,2​([0,T]×𝒟)→𝒞​([0,T]×𝒟)\mathcal{L}^{a}:[0,T]\times\mathbb{R}^{d}\times\mathcal{C}^{1,2}([0,T]\times{\cal D})\rightarrow\mathcal{C}([0,T]\times{\cal D}) is given by

|  |  |  |
| --- | --- | --- |
|  | ℒa​φ​(t,x,𝔦,𝔳):=12​Tr​(σ​σ⊤​(t,x,a)​∂2φ∂x2​(t,x,𝔦,𝔳))+⟨b​(t,x,a),∂φ∂x​(t,x,𝔦,𝔳)⟩,\begin{split}\mathcal{L}^{a}\varphi(t,x,\mathfrak{i},\mathfrak{v}):=\frac{1}{2}\,\mathrm{Tr}\Big(\sigma\sigma^{\top}(t,x,a)\,\frac{\partial^{2}\varphi}{\partial x^{2}}(t,x,\mathfrak{i},\mathfrak{v})\Big)+\Big\langle b(t,x,a),\frac{\partial\varphi}{\partial x}(t,x,\mathfrak{i},\mathfrak{v})\Big\rangle,\end{split} |  |

for a∈ℝa\in\mathbb{R}, and the execution operator 𝒥:[0,T]×ℝd×𝒞1,2​([0,T]×𝒟)→𝒞​([0,T]×𝒟)\mathcal{J}:[0,T]\times\mathbb{R}^{d}\times\mathcal{C}^{1,2}([0,T]\times{\cal D})\rightarrow\mathcal{C}([0,T]\times{\cal D}) is

|  |  |  |
| --- | --- | --- |
|  | 𝒥​v​(t,x,𝔦,𝔳):=∑i=1N𝟙{⟨𝔦,ei⟩>0}​ℓi​(φ​(t,Γ​(t,x,⟨𝔳,ei⟩),𝔦−⟨𝔦,ei⟩​ei,𝔳−⟨𝔳,ei⟩​ei)−φ​(t,x,𝔦,𝔳)−c​(t,x,⟨𝔦,ei⟩,⟨𝔳,ei⟩)).\begin{aligned} \mathcal{J}v(t,x,\mathfrak{i},\mathfrak{v}):=\sum\_{i=1}^{N}\mathds{1}\_{\{\langle\mathfrak{i},e\_{i}\rangle>0\}}\,\ell\_{i}\Big(\varphi\big(t,\Gamma(t,x,\langle\mathfrak{v},e\_{i}\rangle),\mathfrak{i}-\langle\mathfrak{i},e\_{i}\rangle e\_{i},\mathfrak{v}-\langle\mathfrak{v},e\_{i}\rangle e\_{i}\big)-\varphi(t,x,\mathfrak{i},\mathfrak{v})-c(t,x,\langle\mathfrak{i},e\_{i}\rangle,\langle\mathfrak{v},e\_{i}\rangle)\Big).\end{aligned} |  |

Lastly, if ∑i=1N⟨𝔦,ei⟩=K\sum\_{i=1}^{N}\langle\mathfrak{i},e\_{i}\rangle=K, the value function vv on [0,T]×𝒟[0,T]\times{\cal D} is associated to

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∂v∂t​(t,x,𝔦,𝔳)−supa∈ℝHa​(t,x,𝔦,𝔳,v,∂v∂x,∂2v∂x2)=0.\begin{split}-\frac{\partial v}{\partial t}(t,x,\mathfrak{i},\mathfrak{v})&-\sup\_{a\in\mathbb{R}}H^{a}\Big(t,x,\mathfrak{i},\mathfrak{v},v,\tfrac{\partial v}{\partial x},\tfrac{\partial^{2}v}{\partial x^{2}}\Big)=0.\end{split} |  | (14) |

In the equations above, we use the convention that if m−⟨𝔦,ei⟩m-\langle\mathfrak{i},e\_{i}\rangle is zero, then we drop the arguments in 𝔦,𝔳\mathfrak{i},\mathfrak{v}.

###### Remark 3.2.

One could extend our framework and allow for marked point processes instead of the simple point processes we consider. That is, considering (Tni,Rni)n≥1(T^{i}\_{n},R^{i}\_{n})\_{n\geq 1} instead of (Tni)n≥1(T^{i}\_{n})\_{n\geq 1} for i∈ℐi\in\mathcal{I}. In such a setup, similar to [[11](https://arxiv.org/html/2602.10798v1#bib.bib1 "Optimal execution with stochastic delay")], we could modulate the impulse operator with the mark RniR^{i}\_{n} associated with a given execution time TniT^{i}\_{n}. In such a case, the only variation from the equations above would be in the 𝒥\mathcal{J} operator, where one would have an expectation term weighting over the possible values of the marks.

For any locally bounded function vv on [0,T]×𝒟[0,T]\times{\cal D}, we denote by v∗v^{\*} and v∗v\_{\*}
its upper- and lower-semicontinuous envelopes, defined for every
(t,x,𝔦,𝔳)∈[0,T]×𝒟(t,x,\mathfrak{i},\mathfrak{v})\in[0,T]\times{\cal D} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | v∗​(t,x,𝔦,𝔳):=lim sup(t′,x′)→(t,x)v​(t′,x′,𝔦,𝔳)​and​v∗​(t,x,𝔦,𝔳):=lim inf(t′,x′)→(t,x)v​(t′,x′,𝔦,𝔳).v^{\*}(t,x,\mathfrak{i},\mathfrak{v}):=\limsup\_{\begin{subarray}{c}(t^{\prime},x^{\prime})\to(t,x)\end{subarray}}v(t^{\prime},x^{\prime},\mathfrak{i},\mathfrak{v})~~\text{and}~~v\_{\*}(t,x,\mathfrak{i},\mathfrak{v}):=\liminf\_{\begin{subarray}{c}(t^{\prime},x^{\prime})\to(t,x)\end{subarray}}v(t^{\prime},x^{\prime},\mathfrak{i},\mathfrak{v}). |  | (15) |

It is clear that
v∗≤v≤v∗v\_{\*}\leq v\leq v^{\*},
that v∗v^{\*} (resp. v∗v\_{\*})
is upper (resp. lower) semicontinuous,
and that v∗=v∗=vv^{\*}=v\_{\*}=v
at all continuity points of vv.

###### Definition 3.3 (Viscosity solution).

We say that a family of locally bounded functions vv define a viscosity supersolution (resp. subsolution) of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) on [0,T)×𝒟[0,T)\times{\cal D} if it satisfies:

1. 1.

   For (t,x,𝔦,𝔳)∈[0,T)×𝒟(t,x,\mathfrak{i},\mathfrak{v})\in[0,T)\times{\cal D} and any smooth test function φ∈C1,2​([0,T]×𝒟)\varphi\in C^{1,2}([0,T]\times{\cal D}) such that (v∗−φ)(v\_{\*}-\varphi) attains a local minimum (resp. (v∗−φ)(v^{\*}-\varphi) attains a local maximum) at (t,x,𝔦,𝔳)(t,x,\mathfrak{i},\mathfrak{v}) over the set [t,t+δ)×Bδ​(x)×⟦1,K⟧K×Bδ​(𝔳)⊂[0,T)×𝒟[t,t+\delta)\times B\_{\delta}(x)\times\llbracket 1,K\rrbracket^{K}\times B\_{\delta}(\mathfrak{v})\subset[0,T)\times{\cal D} for some δ>0\delta>0, we have

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | min{\displaystyle\min\bigg\{ | −∂φ∂t(t,x,𝔦,𝔳)−supa∈ℝHa(t,x,𝔦,𝔳,φ,∂φ∂x,∂2φ∂x2),(φ−ℳφ)(t,x,𝔦,𝔳)}≥0(resp.≤),\displaystyle-\frac{\partial\varphi}{\partial t}(t,x,\mathfrak{i},\mathfrak{v})-\sup\_{a\in\mathbb{R}}H^{a}\Big(t,x,\mathfrak{i},\mathfrak{v},\varphi,\tfrac{\partial\varphi}{\partial x},\tfrac{\partial^{2}\varphi}{\partial x^{2}}\Big)\,,\,\big(\varphi-\mathcal{M}\varphi\big)(t,x,\mathfrak{i},\mathfrak{v})\bigg\}\geq 0\,(\text{resp.}\leq), |  |
2. 2.

   Additionally, for any (t,x,𝔦,𝔳)∈[0,T)×𝒟(t,x,\mathfrak{i},\mathfrak{v})\in[0,T)\times{\cal D} and any smooth test function φ∈C1,2​([0,T]×𝒟)\varphi\in C^{1,2}([0,T]\times{\cal D}) such that (v∗−φ)(v\_{\*}-\varphi) attains a local minimum (resp. (v∗−φ)(v^{\*}-\varphi) attains a local maximum) at (t,x,𝔦,𝔳)(t,x,\mathfrak{i},\mathfrak{v}) over the set [t,t+δ)×Bδ​(x)×⟦1,K⟧K×Bδ​(𝔳)⊂[0,T)×𝒟[t,t+\delta)\times B\_{\delta}(x)\times\llbracket 1,K\rrbracket^{K}\times B\_{\delta}(\mathfrak{v})\subset[0,T)\times{\cal D} for some δ>0\delta>0, we have

   |  |  |  |
   | --- | --- | --- |
   |  | −∂φ∂t​(t,x,𝔦,𝔳)−supa∈ℝHa(t,x,𝔦,𝔳,φ,∂φ∂x,∂2φ∂x2)≥0(resp.≤).\begin{split}-\frac{\partial\varphi}{\partial t}(t,x,\mathfrak{i},\mathfrak{v})&-\sup\_{a\in\mathbb{R}}H^{a}\Big(t,x,\mathfrak{i},\mathfrak{v},\varphi,\tfrac{\partial\varphi}{\partial x},\tfrac{\partial^{2}\varphi}{\partial x^{2}}\Big)\geq 0\,(\text{resp.}\leq).\end{split} |  |

The first part of the definition covers the case ∑i=1N⟨𝔦,ei⟩<K\sum\_{i=1}^{N}\langle\mathfrak{i},e\_{i}\rangle<K and the second the case ∑i=1N⟨𝔦,ei⟩=K\sum\_{i=1}^{N}\langle\mathfrak{i},e\_{i}\rangle=K. A locally bounded function vv define a viscosity solution if it is both a viscosity supersolution and subsolution of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")).

###### Proposition 3.4.

The value function vv is a viscosity solution of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")). Additionally,

|  |  |  |
| --- | --- | --- |
|  | v​(T−,x,𝔦,𝔳)=v​(T,x,𝔦,𝔳)=g​(x),∀(x,𝔦,𝔳)∈𝒟.v(T^{-},x,\mathfrak{i},\mathfrak{v})=v(T,x,\mathfrak{i},\mathfrak{v})=g(x),\quad\forall(x,\mathfrak{i},\mathfrak{v})\in{\cal D}. |  |

###### Proof.

Refer to Appendix [A](https://arxiv.org/html/2602.10798v1#A1 "Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").

∎

###### Theorem 3.5 (Comparison principle).

If ww is a viscosity subsolution of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and
vv
is a viscosity supersolution of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")), such that

|  |  |  |
| --- | --- | --- |
|  | w∗​(T,x,𝔦,𝔳)≤v∗​(T,x,𝔦,𝔳),w^{\*}(T,x,\mathfrak{i},\mathfrak{v})\leq v\_{\*}(T,x,\mathfrak{i},\mathfrak{v}), |  |

for all (t,x,𝔦,𝔳)∈[0,T]×𝒟(t,x,\mathfrak{i},\mathfrak{v})\in[0,T]\times{\cal D}, then w≤vw\leq v on [0,T]×𝒟[0,T]\times{\cal D}. Additionally, the unique viscosity solution of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) is continuous on [0,T]×𝒟[0,T]\times{\cal D} associated to the terminal condition v​(T,x,𝔦,𝔳)=g​(x),v(T,x,\mathfrak{i},\mathfrak{v})=g(x), for all (x,𝔦,𝔳)∈𝒟(x,\mathfrak{i},\mathfrak{v})\in{\cal D}.

###### Proof.

Refer to Appendix [A](https://arxiv.org/html/2602.10798v1#A1 "Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").

∎

### 3.3 On the Smooth-Fit Principle

To apply the free-boundary regularity results of [[21](https://arxiv.org/html/2602.10798v1#bib.bib30 "Optimal stopping, free boundary, and american option in a jump-diffusion model"), [16](https://arxiv.org/html/2602.10798v1#bib.bib25 "Smooth fit principle for impulse control of multidimensional diffusion processes")] to our mixed control and impulse problem with execution delay, one needs to strengthen the assumptions in [2.1](https://arxiv.org/html/2602.10798v1#S2.ThmAssumption1 "Assumption 2.1. ‣ 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays"). The viscosity framework developed earlier guarantees existence and uniqueness of the value function, but it does not in itself yield differentiability or regularity of the intervention boundary. The analysis of [[16](https://arxiv.org/html/2602.10798v1#bib.bib25 "Smooth fit principle for impulse control of multidimensional diffusion processes")] requires additional smoothness on the local dynamics, on the impulse mechanism, and on the cost structure so that the quasi-variational inequality admits a classical free-boundary interpretation. Recall that if ∑i=1N⟨𝔦,ei⟩<K\sum\_{i=1}^{N}\langle\mathfrak{i},e\_{i}\rangle<K, then the following QVI is linked to the value function defined in ([7](https://arxiv.org/html/2602.10798v1#S2.E7 "In 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")):

|  |  |  |
| --- | --- | --- |
|  | min⁡{−∂v∂t​(t,x,𝔦,𝔳)−supa∈ℝHa​(t,x,𝔦,𝔳,v,∂v∂x,∂2v∂x2),v​(t,x,𝔦,𝔳)−ℳ​v​(t,x,𝔦,𝔳)}=0.\min\Big\{-\frac{\partial v}{\partial t}(t,x,\mathfrak{i},\mathfrak{v})-\sup\_{a\in\mathbb{R}}H^{a}\big(t,x,\mathfrak{i},\mathfrak{v},v,\tfrac{\partial v}{\partial x},\tfrac{\partial^{2}v}{\partial x^{2}}\big),\;v(t,x,\mathfrak{i},\mathfrak{v})-\mathcal{M}v(t,x,\mathfrak{i},\mathfrak{v})\Big\}=0. |  |

On the continuation region, the dynamics are governed purely by the continuous control aa, which enters the PDE through a pointwise Hamiltonian maximization:

|  |  |  |
| --- | --- | --- |
|  | −∂v∂t​(t,x,𝔦,𝔳)=supa∈ℝHa​(t,x,𝔦,𝔳,v,∂v∂x,∂2v∂x2).-\tfrac{\partial v}{\partial t}(t,x,\mathfrak{i},\mathfrak{v})=\sup\_{a\in\mathbb{R}}H^{a}\big(t,x,\mathfrak{i},\mathfrak{v},v,\tfrac{\partial v}{\partial x},\tfrac{\partial^{2}v}{\partial x^{2}}\big). |  |

The absolutely continuous control therefore acts only inside the continuation region

|  |  |  |
| --- | --- | --- |
|  | 𝒞𝔦,𝔳={(t,x):v​(t,x,𝔦,𝔳)>ℳ​v​(t,x,𝔦,𝔳)},\mathcal{C}^{\mathfrak{i},\mathfrak{v}}=\big\{(t,x):v(t,x,\mathfrak{i},\mathfrak{v})>\mathcal{M}v(t,x,\mathfrak{i},\mathfrak{v})\big\}, |  |

and plays a local role, in contrast with impulses that generate nonlocal jumps. In particular, the continuous control affects neither the structure nor the smoothness of the impulse operator ℳ\mathcal{M}, but it determines the parabolic operator governing the value function inside the no-action region. If we further assume that the drift, diffusion, and running cost are 𝒞1+β\mathcal{C}^{1+\beta} in the spatial variable (uniformly in (t,a,𝔦,𝔳)(t,a,\mathfrak{i},\mathfrak{v})), and that the terminal reward is 𝒞2+β\mathcal{C}^{2+\beta}, then we would expect the nonlinear HJB operator

|  |  |  |
| --- | --- | --- |
|  | F​(t,x,𝔦,𝔳,r,q,p,X):=−q−supa∈𝒜Ha​(t,x,𝔦,𝔳,r,p,X)F(t,x,\mathfrak{i},\mathfrak{v},r,q,p,X):=-q-\sup\_{a\in\mathcal{A}}H^{a}(t,x,\mathfrak{i},\mathfrak{v},r,p,X) |  |

to be uniformly parabolic with Hölder-continuous coefficients, as required in the interior Schauder theory. Likewise, if we assume that the impulse transition map Γ​(t,x,i,ξ)\Gamma(t,x,i,\xi) is locally Lipschitz in in (t,x,ξ)(t,x,\xi), and nondegenerate, and that the impulse cost c​(t,x,ξ,i)c(t,x,\xi,i) is strictly positive for ξ≠0\xi\neq 0, and satisfies a subadditivity condition preventing the accumulation of infinitely many impulses over finite time, then these assumptions ensure the regularity of the impulse operator. Moreover, if the minimization defining ℳ​v​(t,x,𝔦,𝔳)\mathcal{M}v(t,x,\mathfrak{i},\mathfrak{v}) admits a unique minimizer ξ⋆​(t,x,𝔦,𝔳)\xi^{\star}(t,x,\mathfrak{i},\mathfrak{v}) that is locally bounded in (t,x)(t,x) for every (t,x,𝔦,𝔳)∈[0,T]×𝒟(t,x,\mathfrak{i},\mathfrak{v})\in[0,T]\times\mathcal{D}, then the structure of the impulse component aligns with the conditions imposed in [[16](https://arxiv.org/html/2602.10798v1#bib.bib25 "Smooth fit principle for impulse control of multidimensional diffusion processes")]. Under these strengthened assumptions, the following regularity result applies: the value function is 𝒞1\mathcal{C}^{1} on the entire domain and 𝒞2\mathcal{C}^{2} on the continuation region. In particular, the free boundary

|  |  |  |
| --- | --- | --- |
|  | ∂𝒞𝔦,𝔳:={(t,x):v​(t,x,𝔦,𝔳)=ℳ​v​(t,x,𝔦,𝔳)}\partial\mathcal{C}^{\mathfrak{i},\mathfrak{v}}:=\big\{(t,x):v(t,x,\mathfrak{i},\mathfrak{v})=\mathcal{M}v(t,x,\mathfrak{i},\mathfrak{v})\big\} |  |

satisfies both value matching and smooth fit

|  |  |  |
| --- | --- | --- |
|  | v=ℳ​v​and​Dx​v=Dx​(ℳ​v).v=\mathcal{M}v~~\text{and}~~D\_{x}v=D\_{x}(\mathcal{M}v). |  |

Moreover the free boundary is 𝒞1\mathcal{C}^{1} in (t,x)(t,x).

###### Remark 3.6.

We expect the nonlocal integral term generated by these exogenous jumps to preserve the same interior regularity as the diffusion part.

In the trading problem considered in Section [4](https://arxiv.org/html/2602.10798v1#S4 "4 CEX-DEX Optimal Trading Problem ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays") of this paper, the optimal strategy for each pending-order configuration (𝔦,𝔳)(\mathfrak{i},\mathfrak{v}) is characterized by a smooth free-boundary in (t,x)(t,x) that separates the region where the agent continues with the absolutely continuous control from the region where it becomes optimal to submit a DEX order with a given priority fee and size. Under the smooth-fit property, one would expect the marginal value with respect to xx to coincide on both sides of this boundary when transitioning from the pre- to the post-impulse state.

## 4 CEX-DEX Optimal Trading Problem

### 4.1 Model Setup

Using the setup above, we consider the case of NN priority fees and KK pending orders. For simplicity, we include the base fee (which is a flat fee paid by all takers in the DEX) in the “priority fee” paid by the controller.
Here, we consider the case of a two dimensional ℙ\mathbb{P}-Brownian motion W=(WZ,WS)W=(W^{Z},W^{S}). Let t∈[0,T]t\in[0,T] and y=(s,q,z,𝔦,𝔳)∈𝒟y=(s,q,z,\mathfrak{i},\mathfrak{v})\in{\cal D}, where 𝒟{\cal D} defines the following domain

|  |  |  |
| --- | --- | --- |
|  | 𝒟:={(s,q,z,𝔦,𝔳):(s,q,z)∈ℝ+2×ℝ,𝔦∈𝕀,𝔳∈𝕍}.{\cal D}:=\{(s,q,z,\mathfrak{i},\mathfrak{v}):(s,q,z)\in\mathbb{R}\_{+}^{2}\times\mathbb{R},\;\mathfrak{i}\in\mathbb{I},\;\mathfrak{v}\in\mathbb{V}\}. |  |

For an execution strategy α∈𝒜K,𝔦,𝔳​(t)\alpha\in{\cal A}\_{K,\mathfrak{i},\mathfrak{v}}(t),
the trader monitors the controlled state variable XX such that

|  |  |  |
| --- | --- | --- |
|  | Xα=(Sα,Qα,Zα).X^{\alpha}=(S^{\alpha},Q^{\alpha},Z^{\alpha}). |  |

The agent observes the external price in a centralised venue which we call SS and that follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sut,s,α=s+σS​(WuS−WtS),u∈[t,T],S^{t,s,\alpha}\_{u}=s+\sigma^{S}\,\big(W^{S}\_{u}-W^{S}\_{t}\big)\,,\quad u\in[t,T], |  | (16) |

where s∈ℝ+s\in\mathbb{R}\_{+} is the value of StS\_{t}. The pool midprice, denoted by ZZ, evolves as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zut,z,s,α=z+∫tuκ​(Srt,s,α−Zrt,z,s,α)​dr+σZ​(WuZ−WtZ)+∑τ~n≤uh​(ξn,Zτ~n−t,z,s,α),u∈[t,T],Z^{t,z,s,\alpha}\_{u}=z+\int\_{t}^{u}\kappa(S^{t,s,\alpha}\_{r}-Z^{t,z,s,\alpha}\_{r})\,\mathrm{d}r+\sigma^{Z}\,\big(W^{Z}\_{u}-W^{Z}\_{t}\big)+\sum\_{\tilde{\tau}\_{n}\leq u}h(\xi\_{n},Z^{t,z,s,\alpha}\_{\tilde{\tau}^{-}\_{n}})\,\,,\quad u\in[t,T], |  | (17) |

where z∈ℝ+z\in\mathbb{R}\_{+} is the value of ZtZ\_{t}. In what follows, we drop the starting values of the controlled processes for ease of the notation. Here, the function hh is given by h​(ξ,Z)=ψ​(Z)​ξh(\xi,Z)=\psi(Z)\,\xi, and the function ψ\psi (which approximates the transaction price [[9](https://arxiv.org/html/2602.10798v1#bib.bib3 "Decentralised finance and automated market making: execution and speculation")]) is ψ​(Z)=2​Z3/2/d\psi(Z)=2\,Z^{3/2}/d where dd is the depth of the DEX. Here, the drift term ∫tuκ​(Srα−Zrα)​dr\int\_{t}^{u}\kappa\,(S\_{r}^{\alpha}-Z\_{r}^{\alpha})\,\mathrm{d}r models mean reversion of the DEX state toward the CEX price SαS^{\alpha}: the parameter κ>0\kappa>0 quantifies the speed at which arbitrageurs realign prices across venues. The Brownian component ∫tuσZ​dWrZ\int\_{t}^{u}\sigma^{Z}\,\mathrm{d}W\_{r}^{Z} captures exogenous/noise-trader activity. Finally, the jump term ∑τ~n≤uh​(ξn,Zτ~n−α)\sum\_{\tilde{\tau}\_{n}\leq u}h(\xi\_{n},Z^{\alpha}\_{\tilde{\tau}\_{n}^{-}}) accounts for the instantaneous impact of the agent’s discrete DEX trades executed at times τ~n\tilde{\tau}\_{n}. The impact is linear in ξ\xi, increases with the current level ZZ, and is attenuated by the constant-product pool depth dd. The inventory of the agent is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Quα=q+∫tuνr​dr⏟trading in CEX+∑n:τ~n≤uξn⏟trading in DEX,u∈[t,T],Q^{\alpha}\_{u}=q+\underbrace{\int\_{t}^{u}\nu\_{r}\,\mathrm{d}r}\_{\text{trading in CEX}}+\underbrace{\sum\_{n:\,\tilde{\tau}\_{n}\leq u}\xi\_{n}}\_{\text{trading in DEX}}\,\,,\quad u\in[t,T], |  | (18) |

where q∈ℝq\in\mathbb{R} is the inventory of the agent at time tt, and the cash accumulated from time tt to time uu is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cuα=−∫tuνr​(Srα+k​νr)​dr⏟trading in CEX+∑n:τ~n≤u(γ​(ξn,Zτ~i−α)−𝔭In)⏟trading in DEX,u∈[t,T],C^{\alpha}\_{u}=\underbrace{-\int\_{t}^{u}\nu\_{r}\,\left(S^{\alpha}\_{r}+k\,\nu\_{r}\right)\mathrm{d}r}\_{\text{trading in CEX}}+\underbrace{\sum\_{n:\,\tilde{\tau}\_{n}\leq u}\big(\gamma(\xi\_{n},Z^{\alpha}\_{\tilde{\tau}^{-}\_{i}})-\mathfrak{p}\_{I\_{n}}\big)}\_{\text{trading in DEX}}\,\,,\quad u\in[t,T], |  | (19) |

where

|  |  |  |
| --- | --- | --- |
|  | γ​(ξ,z)=d2ξ−d​1/z+d​z.\gamma(\xi,z)=\frac{d^{2}}{\xi-d\,\sqrt{1/z}}+d\,\sqrt{z}\,. |  |

The formula for γ\gamma is the closed-form expression for the execution cost of a trade of size ξn\xi\_{n} in the DEX.

The elements (𝔦,𝔳)=(0𝕀,0𝕍)(\mathfrak{i},\mathfrak{v})=(0\_{\mathbb{I}},0\_{\mathbb{V}}) denote the absence of pending orders. For y=(s,q,z,𝔦,𝔳)y=(s,q,z,\mathfrak{i},\mathfrak{v}) and for control ν\nu, we consider the following running reward ff and terminal payoff gg

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(t,y,ν)\displaystyle f(t,y,\nu) | :=−ν​(s+k​ν)−ϕ​q2​and​g​(y):=q​s−Ξ​q2,\displaystyle:=-\nu\,\left(s+k\,\nu\right)-\phi\,q^{2}~~\text{and}~~g(y):=q\,s-\Xi\,q^{2}, |  |

with k>0k>0 and ϕ,Ξ≥0\phi,\Xi\geq 0.
Lastly, the intervention cost cc is

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(τ~n,Zτ~n−α,ξn,In):=γ​(ξn,Zτ~n−α)−𝔭In,c(\tilde{\tau}\_{n},Z^{\alpha}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})\;:=\;\gamma(\xi\_{n},Z^{\alpha}\_{\tilde{\tau}^{-}\_{n}})-\mathfrak{p}\_{I\_{n}}\,, |  | (20) |

where for simplicity we exclude base fees as these could absorbed in the priority fees vector 𝔭\mathfrak{p}.111The framework is flexible enough to accommodate strategic fees [[2](https://arxiv.org/html/2602.10798v1#bib.bib8 "Optimal dynamic fees in automated market makers")] or alternative designs [[10](https://arxiv.org/html/2602.10798v1#bib.bib9 "Strategic bonding curves in automated market makers")]. More precisely, one can add here any deterministic map that adjusts costs depending on the transaction size ξn\xi\_{n} or the state of the pool. We leave these generalizations out for simplicity. 
For any admissible control α∈𝒜K,𝔦,𝔳​(t)\alpha\in{\cal A}\_{K,\mathfrak{i},\mathfrak{v}}(t), we define the performance criterion
Formally, for any admissible control α∈𝒜K,𝔦,𝔳​(t)\alpha\in{\cal A}\_{K,\mathfrak{i},\mathfrak{v}}(t), we define the performance criterion

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,y,α)=𝔼t,y​[−∫tTνr​(Srα+k​νr)​dr+QTα​STα−Ξ​(QTα)2−∑τ~n∈(t,T]c​(τ~n,Zτ~nα,ξn,In)−ϕ​∫tT(Qrα)2​dr].\begin{aligned} J(t,y,\alpha)=\mathbb{E}\_{t,y}\Bigg[-\int\_{t}^{T}\nu\_{r}\,\left(S^{\alpha}\_{r}+k\,\nu\_{r}\right)\mathrm{d}r\,+Q^{\alpha}\_{T}\,S^{\alpha}\_{T}-\Xi\,\big(Q^{\alpha}\_{T}\big)^{2}-\sum\_{\tilde{\tau}\_{n}\in(t,T]}c(\tilde{\tau}\_{n},Z^{\alpha}\_{\tilde{\tau}\_{n}},\xi\_{n},I\_{n})-\phi\,\int\_{t}^{T}\big(Q^{\alpha}\_{r}\big)^{2}\,\mathrm{d}r\Bigg].\end{aligned} |  | (21) |

The associated value function is then given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t,y):=supα∈𝒜K,𝔦,𝔳​(t)J​(t,y,α).v(t,y):=\sup\_{\alpha\in{\cal A}\_{K,\mathfrak{i},\mathfrak{v}}(t)}J(t,y,\alpha). |  | (22) |

In particular, when there are no pending orders, the state reduces to
y0=(s,q,z,0𝕀,0𝕍)∈𝒟y\_{0}=(s,q,z,0\_{\mathbb{I}},0\_{\mathbb{V}})\in{\cal D}, and the value function defined in ([7](https://arxiv.org/html/2602.10798v1#S2.E7 "In 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) coincides with the one obtained under 𝒜K,0,0​(t)\mathcal{A}\_{K,0,0}(t).

###### Notation 4.1.

The conditional expectation given (Stα=s,Qtα=q,Ztα=z)(S^{\alpha}\_{t}=s,Q^{\alpha}\_{t}=q,Z^{\alpha}\_{t}=z) under the probability measure ℙ\mathbb{P} is denoted by

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,y[⋅]=𝔼ℙ[⋅|Stα=s,Qt−α=q,Ztα=z].\mathbb{E}\_{t,y}[\cdot]=\mathbb{E}^{\mathbb{P}}\Big[\cdot\Big|S^{\alpha}\_{t}=s,Q^{\alpha}\_{t^{-}}=q,Z^{\alpha}\_{t}=z\Big]. |  |

Next, we characterize the HJB equation associated with v​(t,y)v(t,y). If ∑i=1N⟨𝔦,ei⟩<K\sum\_{i=1}^{N}\langle\mathfrak{i},e\_{i}\rangle<K, then the QVI that is linked to the value function is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | min{\displaystyle\min\bigg\{ | −∂v∂t(t,y)−supν∈ℝHν(t,y,v,∂v∂x,∂2v∂x2),(v−ℳv)(t,y)}=0,\displaystyle-\frac{\partial v}{\partial t}(t,y)-\sup\_{\nu\in\mathbb{R}}H^{\nu}\Big(t,y,v,\tfrac{\partial v}{\partial x},\tfrac{\partial^{2}v}{\partial x^{2}}\Big)\,,\,\big(v-\mathcal{M}v\big)(t,y)\bigg\}=0, |  | (23) |

where ℳ:𝒞​([0,T]×𝒟)→𝒞​([0,T]×𝒟)\mathcal{M}:\mathcal{C}([0,T]\times{\cal D})\rightarrow\mathcal{C}([0,T]\times{\cal D}) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳ​φ​(t,y):=sup(ξ,i)∈[−V¯,V¯]×⟦1,K⟧φ​(t,s,q,z,𝔦+ei,𝔳+ξ​ei),\mathcal{M}\varphi(t,y):=\sup\_{(\xi,i)\in[-\bar{V},\bar{V}]\times{\llbracket 1,K\rrbracket}}\varphi(t,s,q,z,\mathfrak{i}+e\_{i},\mathfrak{v}+\xi e\_{i}), |  | (24) |

and the Hamiltonian Hν:[0,T]×𝒟×𝒞​([0,T]×𝒟)3→ℝH^{\nu}:[0,T]\times{\cal D}\times\mathcal{C}([0,T]\times{\cal D})^{3}\rightarrow\mathbb{R} is

|  |  |  |
| --- | --- | --- |
|  | Hν​(t,y,φ,∂φ∂x,∂2φ∂x2)=ℒν​φ​(t,y)+𝒥​φ​(t,y)−ϕ​q2−ν​(s+k​ν),\displaystyle H^{\nu}\Big(t,y,\varphi,\tfrac{\partial\varphi}{\partial x},\tfrac{\partial^{2}\varphi}{\partial x^{2}}\Big)=\mathcal{L}^{\nu}\varphi(t,y)+\mathcal{J}\varphi(t,y)-\phi\,q^{2}-\nu(s+k\,\nu), |  |

with infinitesimal generator

|  |  |  |
| --- | --- | --- |
|  | ℒν​φ​(t,y):=κ​(s−z)​∂v∂z​(t,y)+12​(σZ)2​∂2v∂z2​(t,y)+12​(σS)2​∂2v∂s2​(t,y)+ν​∂v∂q​(t,y),\begin{split}\mathcal{L}^{\nu}\varphi(t,y):=\kappa(s-z)\,\frac{\partial v}{\partial z}(t,y)+\frac{1}{2}(\sigma^{Z})^{2}\frac{\partial^{2}v}{\partial z^{2}}(t,y)+\frac{1}{2}(\sigma^{S})^{2}\frac{\partial^{2}v}{\partial s^{2}}(t,y)+\nu\,\frac{\partial v}{\partial q}(t,y),\end{split} |  |

execution operator of pending orders

|  |  |  |
| --- | --- | --- |
|  | 𝒥​v​(t,y):=∑i=1N𝟙{𝔦i>0}​ℓi​(φ​(t,Γ​(t,s,q,z,ξi),𝔦−𝔦i​ei,𝔳−ξi​ei)−φ​(t,y)+c​(t,s,q,z,𝔦i,ξi)),\mathcal{J}v(t,y):=\sum\_{i=1}^{N}\mathds{1}\_{\{\mathfrak{i}\_{i}>0\}}\,\ell\_{i}\Big(\varphi\big(t,\Gamma(t,s,q,z,\xi\_{i}),\mathfrak{i}-\mathfrak{i}\_{i}e\_{i},\mathfrak{v}-\xi\_{i}e\_{i}\big)-\varphi(t,y)+c(t,s,q,z,\mathfrak{i}\_{i},\xi\_{i})\Big), |  |

where ξi:=⟨𝔳,ei⟩\xi\_{i}:=\langle\mathfrak{v},e\_{i}\rangle, 𝔦i:=⟨𝔦,ei⟩\mathfrak{i}\_{i}:=\langle\mathfrak{i},e\_{i}\rangle and the impulse operator Γ\Gamma is

|  |  |  |
| --- | --- | --- |
|  | Γ​(t,s,q,z,ξ)=(s,q+ξ,z+h​(ξ,z)).\Gamma(t,s,q,z,\xi)=(s,q+\xi,z+h(\xi,z)). |  |

If ∑i=1N⟨𝔦,ei⟩=K\sum\_{i=1}^{N}\langle\mathfrak{i},e\_{i}\rangle=K, the value function vv on [0,T]×𝒟[0,T]\times{\cal D} is associated to

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∂v∂t​(t,y)−supν∈ℝHν​(t,y,v,∂v∂x,∂2v∂x2)=0.\begin{split}-\frac{\partial v}{\partial t}(t,y)&-\sup\_{\nu\in\mathbb{R}}H^{\nu}\Big(t,y,v,\tfrac{\partial v}{\partial x},\tfrac{\partial^{2}v}{\partial x^{2}}\Big)=0.\end{split} |  | (25) |

Lastly, from the first order optimality condition we have ν∗=(2​k)−1​(∂v∂q−s)\nu^{\*}=(2\,k)^{-1}(\frac{\partial v}{\partial q}-s).

### 4.2 Numerical Results

We employ the values of model parameters in [[1](https://arxiv.org/html/2602.10798v1#bib.bib11 "Equilibrium reward for liquidity providers in automated market makers")] which are calibrated to ETH-USDC market data.222See [[13](https://arxiv.org/html/2602.10798v1#bib.bib4 "Deviations from tradition: stylized facts in the era of defi")] for a recent article studying the stylized facts of prices, liquidity, and order flow in DEXs.  More precisely, we take S0=Z0=2820S\_{0}=Z\_{0}=2820, σS=0.0569×S0\sigma^{S}=0.0569\times S\_{0}, κ=1\kappa=1, σZ=0.00569×S0\sigma^{Z}=0.00569\times S\_{0}. The depth is d=50,000d=50,000 ETH. The agent-specific aversion parameters are Ξ=1\Xi=1 and ϕ=1\phi=1.
Lastly, to obtain the value function we use standard numerical schemes.
For the fees and delays vectors, we consider the following. For experiments having N≥1N\geq 1 priority fees, we take the fee vector to be 𝔭={𝔭1,p1+200,…,𝔭1+200​N}\mathfrak{p}=\{\mathfrak{p}\_{1},p\_{1}+200,\dots,\mathfrak{p}\_{1}+200\,N\} with 𝔭1=100\mathfrak{p}\_{1}=100, and the delay vector is 𝔩={ℓ1,ℓ1+0.5,…,ℓ1+0.5​N}\mathfrak{l}=\{\ell\_{1},\ell\_{1}+0.5,\dots,\ell\_{1}+0.5\,N\} and ℓ1=2\ell\_{1}=2.

#### Optimal trading strategy

Figure [1](https://arxiv.org/html/2602.10798v1#S4.F1 "Figure 1 ‣ Optimal trading strategy ‣ 4.2 Numerical Results ‣ 4 CEX-DEX Optimal Trading Problem ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays") shows the value function and the corresponding exercise region for when the inventory is zero (q=0q=0).

![Refer to caption](x1.png)

![Refer to caption](x2.png)

Figure 1: Value function and exercise region as a function of the CEX and DEX prices (s,z)(s,z) for q=0q=0.

The continuation region in Figure [1](https://arxiv.org/html/2602.10798v1#S4.F1 "Figure 1 ‣ Optimal trading strategy ‣ 4.2 Numerical Results ‣ 4 CEX-DEX Optimal Trading Problem ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays") forms a diagonal band around s=zs=z, where prices are closely aligned and it is optimal to wait, while the exercise region lies outside this band and expands as the divergence between the two prices increases. This is similar to the exit region found in [[4](https://arxiv.org/html/2602.10798v1#bib.bib2 "Optimal exit time for liquidity providers in automated market makers")] for when LPs find it optimal to exit the pool; in the present context, the region modulates the trading activity of the liquidity taker. This symmetry highlights that execution becomes optimal precisely when the price discrepancy between the two venues is sufficiently large, and not on the price direction. This reflects an arbitrage-driven incentive to trade whenever CEX and DEX prices dislocate.

Figure [2](https://arxiv.org/html/2602.10798v1#S4.F2 "Figure 2 ‣ Optimal trading strategy ‣ 4.2 Numerical Results ‣ 4 CEX-DEX Optimal Trading Problem ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays") illustrates the sensitivity of the optimal trading rate ν∗\nu^{\*} to the CEX price and the inventory (z=2700z=2700).

![Refer to caption](x3.png)


Figure 2: Optimal trading rate ν∗\nu^{\*} as a function of the CEX price ss and the inventory qq for z=2700z=2700 and t=0.1t=0.1.

The plot indicates that the optimal trading rate ν∗\nu^{\*} depends primarily on the inventory, with only a weak sensitivity to the CEX price level. This is consistent with the fact that, under our specification, CEX prices are martingales, so there is no directional expected return to exploit through ss. As a result, the trading rate is mainly driven by the inventory objective and its associated constraint.

#### Inventory

Figure [3](https://arxiv.org/html/2602.10798v1#S4.F3 "Figure 3 ‣ Inventory ‣ 4.2 Numerical Results ‣ 4 CEX-DEX Optimal Trading Problem ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays") explores the effect of the inventory in the priority fees. We take the inventory to be large and positive q=40q=40 (negative case is analogous).

![Refer to caption](x4.png)


(a) t=t0t=t\_{0}

![Refer to caption](x5.png)


(b) t=t1t=t\_{1}

![Refer to caption](x6.png)


(c) t=t2t=t\_{2}

Figure 3: Exercise and continuation regions as a function of the CEX and DEX prices (s,z)(s,z) at time indices t0<t1<t2t\_{0}<t\_{1}<t\_{2} for q=40q=40. Here, t0=0.2t\_{0}=0.2, t1=0.5t\_{1}=0.5, and t2=0.8t\_{2}=0.8.

We see that the exercise region becomes one-sided, this is because the trader does not wish to acquire more inventory and the main incentive is to bring qq closer to zero towards the end of the time horizon TT. As time passes (from left panel to right panel), the urgency to bring inventory closer to zero shifts the exercise region to be more and more aggressive.

#### Priority fees

Figure [4](https://arxiv.org/html/2602.10798v1#S4.F4 "Figure 4 ‣ Priority fees ‣ 4.2 Numerical Results ‣ 4 CEX-DEX Optimal Trading Problem ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays") illustrates the optimal priority fee policy. As the terminal time is approached, the continuation region progressively shrinks, while the exercise regions associated with positive priority fees expand. As one would expect, higher priority fees are reserved for when dislocations are larger. This is because the trader wishes to ensure that the arbitrage opportunity is attainable.

![Refer to caption](x7.png)


(a) t=t0t=t\_{0}

![Refer to caption](x8.png)


(b) t=t1t=t\_{1}

![Refer to caption](x9.png)


(c) t=t2t=t\_{2}

Figure 4: Priority fees as a function of the CEX and DEX prices (s,z)(s,z) at time indices t0<t1<t2t\_{0}<t\_{1}<t\_{2} for q=0q=0. Here, t0=0.2t\_{0}=0.2, t1=0.5t\_{1}=0.5, and t2=0.8t\_{2}=0.8.

The plots also reflect the increasing urgency to liquidate positions as time passes: states for which it was optimal to wait at earlier times are gradually replaced by decisions to pay for execution priority. In particular, higher priority fee levels become optimal closer to the terminal condition, indicating that the agent is willing to incur larger execution costs in order to reduce liquidation risk.

Figure [5](https://arxiv.org/html/2602.10798v1#S4.F5 "Figure 5 ‣ Priority fees ‣ 4.2 Numerical Results ‣ 4 CEX-DEX Optimal Trading Problem ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays") shows the effect of increasing exogenous arrival intensities on the optimal priority fee policy.

![Refer to caption](x10.png)


(a) 𝔩=𝔩0\mathfrak{l}=\mathfrak{l}\_{0}

![Refer to caption](x11.png)


(b) 𝔩=𝔩1\mathfrak{l}=\mathfrak{l}\_{1}

![Refer to caption](x12.png)


(c) 𝔩=𝔩2\mathfrak{l}=\mathfrak{l}\_{2}

Figure 5: Priority fee regions for increasing exogenous arrival intensities at the CEX and DEX at time t=0.5t=0.5. From left to right, all arrival intensities are jointly increased 𝔩2<𝔩1<𝔩0\mathfrak{l}\_{2}<\mathfrak{l}\_{1}<\mathfrak{l}\_{0}.

As arrival intensities increase, and hence expected execution delays decrease, the regions associated with lower priority fees expand, while those corresponding to higher priority fees shrink. Economically, this means that when execution becomes faster even at low priority levels, the marginal benefit of paying for additional priority is reduced. Consequently, the agent optimally relies more often on lower priority fees, since similar execution speed can be achieved at a lower cost.

In the next experiment we study the additional benefits the controller gets when entertaining more priority fees in their control problem. We start from a single priority level and then increase the number of available priority levels to N∈{1,2,3,5,7,10,30,50}N\in\{1,2,3,5,7,10,30,50\}. For each additional level, we add one more fee-intensity pair, where both the priority fee and its corresponding execution intensity are increased by a fixed increment relative to the previous level (see the start of this section for details).
Figure [6](https://arxiv.org/html/2602.10798v1#S4.F6 "Figure 6 ‣ Priority fees ‣ 4.2 Numerical Results ‣ 4 CEX-DEX Optimal Trading Problem ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays") reports the norm of the value function v0:(s,q,z,𝔦,𝔳)↦v​(0,s,q,z,𝔦,𝔳)v\_{0}:(s,q,z,\mathfrak{i},\mathfrak{v})\mapsto v(0,s,q,z,\mathfrak{i},\mathfrak{v}) at time t=0t=0 computed on the full (s,q,z)(s,q,z) grid (with 𝔦=0𝕀\mathfrak{i}=0\_{\mathbb{I}} and 𝔳=0𝕍\mathfrak{v}=0\_{\mathbb{V}}).

![Refer to caption](x13.png)


Figure 6: ‖v0‖\|v\_{0}\| over all states as a function of the number of priority fee levels.

The figure shows that, as the number of priority-fee options increases, the value function improves relative to the benchmark with a single priority fee, which we interpret as higher attainable profit from having finer control over execution speed and latency risk. We see that the outperformance rapidly plateaus, in fact, beyond thirty, the outperformance of employing additional priority fees becomes negligible.

Lastly, we compare the performance of the optimal priority-fee policy against that from a randomized baseline within the same mixed-control QVI. In both cases, we use the continuous CEX control ν∗\nu^{\*} and the same intervention times. The only modification is the fee choice upon intervention: the optimal policy selects the maximizing priority level, while the randomized baseline draws the fee index J∼Unif​{1,…,N}J\sim\mathrm{Unif}\{1,\dots,N\} (with the remaining impulse decision rule unchanged), with N=3N=3. We estimate the randomized strategy by averaging over 100 independent samples. Using ‖v0‖\|v\_{0}\| over all states as the metric, the optimal policy improves the value function by 18.2%18.2\% relative to the random-fee baseline.

## 5 Conclusions

We introduced a new type of mixed control problem where the agent is allowed
to choose the expected delay of the execution of the impulses. The associated value function to this optimization problem is shown to satisfy a system of variational Hamilton–Jacobi–Bellman inequalities in the viscosity sense. Moreover, we establish uniqueness of the solution to this HJB-QVI. We apply our formulation to the problem of optimal trading between CEX and DEX, where the agent chooses the priority fee attached to the orders sent to the DEX. We find the optimal priority fee as a function of time, inventories, and price dislocations between the CEX and the DEX. Our results show that the outperformance one gets from employing more priority fees rapidly plateaus, and that the optimal fee selection brings about significant outperformance over a non-strategic fee selection.
To the best of our knowledge, this is the first time this appears in the growing literature on AMMs.

## Comments

For the purpose of open access, the authors have applied a CC BY public copyright licence to any author accepted manuscript version arising from this submission.

## References

* [1]
  A. Aqsha, P. Bergault, and L. Sánchez-Betancourt (2025)
  Equilibrium reward for liquidity providers in automated market makers.
  arXiv preprint arXiv:2503.22502.
  Cited by: [§4.2](https://arxiv.org/html/2602.10798v1#S4.SS2.p1.12 "4.2 Numerical Results ‣ 4 CEX-DEX Optimal Trading Problem ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [2]
  L. Baggiani, M. Herdegen, and L. Sánchez-Betancourt (2025)
  Optimal dynamic fees in automated market makers.
  arXiv preprint arXiv:2506.02869.
  Cited by: [footnote 1](https://arxiv.org/html/2602.10798v1#footnote1 "In 4.1 Model Setup ‣ 4 CEX-DEX Optimal Trading Problem ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [3]
  D. Becherer, C. Reisinger, and J. Tam (2023)
  Mean-field games of speedy information access with observation costs.
  arXiv preprint arXiv:2309.07877.
  Cited by: [§1](https://arxiv.org/html/2602.10798v1#S1.p2.1 "1 Introduction ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [4]
  P. Bergault, S. Bieber, and L. Sánchez-Betancourt (2025)
  Optimal exit time for liquidity providers in automated market makers.
  arXiv preprint arXiv:2509.06510.
  Cited by: [§4.2](https://arxiv.org/html/2602.10798v1#S4.SS2.SSS0.Px1.p2.1 "Optimal trading strategy ‣ 4.2 Numerical Results ‣ 4 CEX-DEX Optimal Trading Problem ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [5]
  D. P. Bertsekas and S. E. Shreve (1978)
  Stochastic optimal control: the discrete-time case.
  Mathematics in Science and Engineering, Vol. 139, Academic Press, New York.
  Cited by: [§3.1](https://arxiv.org/html/2602.10798v1#S3.SS1.1.p1.9 "Proof. ‣ 3.1 Dynamic programming principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [6]
  M. Bichuch and Z. Feinstein (2024)
  DeFi arbitrage in hedged liquidity tokens.
  arXiv preprint arXiv:2409.11339.
  Cited by: [§1](https://arxiv.org/html/2602.10798v1#S1.p3.1 "1 Introduction ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [7]
  B. Bruder and H. Pham (2009)
  Impulse control problem on finite horizon with execution delay.
  Stochastic Processes and their Applications 119 (5),  pp. 1436–1469.
  External Links: ISSN 0304-4149,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.spa.2008.07.007)
  Cited by: [§1](https://arxiv.org/html/2602.10798v1#S1.p2.1 "1 Introduction ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [8]
  Á. Cartea, F. Drissi, and M. Monga (2023)
  Execution and statistical arbitrage with signals in multiple automated market makers.
  In 2023 IEEE 43rd International Conference on Distributed Computing Systems Workshops (ICDCSW),
   pp. 37–42.
  Cited by: [§1](https://arxiv.org/html/2602.10798v1#S1.p3.1 "1 Introduction ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [9]
  Á. Cartea, F. Drissi, and M. Monga (2025)
  Decentralised finance and automated market making: execution and speculation.
  Journal of Economic Dynamics and Control 177,  pp. 105134.
  External Links: ISSN 0165-1889,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.jedc.2025.105134),
  [Link](https://www.sciencedirect.com/science/article/pii/S0165188925001009)
  Cited by: [§1](https://arxiv.org/html/2602.10798v1#S1.p3.1 "1 Introduction ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays"),
  [§4.1](https://arxiv.org/html/2602.10798v1#S4.SS1.p1.29 "4.1 Model Setup ‣ 4 CEX-DEX Optimal Trading Problem ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [10]
  Á. Cartea, F. Drissi, L. Sánchez-Betancourt, D. Siska, and L. Szpruch (2024)
  Strategic bonding curves in automated market makers.
  Available at SSRN 5018420.
  Cited by: [footnote 1](https://arxiv.org/html/2602.10798v1#footnote1 "In 4.1 Model Setup ‣ 4 CEX-DEX Optimal Trading Problem ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [11]
  Á. Cartea and L. Sánchez-Betancourt (2023)
  Optimal execution with stochastic delay.
  Finance and Stochastics 27 (1),  pp. 1–47.
  Cited by: [§1](https://arxiv.org/html/2602.10798v1#S1.p2.1 "1 Introduction ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays"),
  [§2](https://arxiv.org/html/2602.10798v1#S2.1.p1.1 "Proof. ‣ 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays"),
  [Remark 3.2](https://arxiv.org/html/2602.10798v1#S3.Thmtheorem2.p1.6.6 "Remark 3.2. ‣ 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [12]
  M. Crandall, H. Ishii, and P.-L. Lions (1992)
  User’s guide to viscosity solutions of second order partial differential equations.
  Bulletin of the American Mathematical Society 27,  pp. 1–67.
  Cited by: [§A.3](https://arxiv.org/html/2602.10798v1#A1.SS3.2.p1.50 "Proof. ‣ A.3 Uniqueness and Continuity Result ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [13]
  D. M. Di Nosse, F. Gatta, F. Lillo, and S. Jaimungal (2025)
  Deviations from tradition: stylized facts in the era of defi.
  arXiv preprint arXiv:2510.22834.
  Cited by: [footnote 2](https://arxiv.org/html/2602.10798v1#footnote2 "In 4.2 Numerical Results ‣ 4 CEX-DEX Optimal Trading Problem ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [14]
  W. H. Fleming and H. M. Soner (2006)
  Controlled markov processes and viscosity solutions.
  2nd edition, Stochastic Modelling and Applied Probability, Vol. 25, Springer, New York.
  External Links: [Document](https://dx.doi.org/10.1007/0-387-31071-1)
  Cited by: [§A.3](https://arxiv.org/html/2602.10798v1#A1.SS3.SSS0.Px2.p1.17 "Case 2: ‣ A.3 Uniqueness and Continuity Result ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [15]
  M. Fukasawa, B. Maire, and M. Wunsch (2024)
  Model-free hedging of impermanent loss in geometric mean market makers with proportional transaction fees.
  Applied Mathematical Finance 31 (2),  pp. 108–129.
  Cited by: [§1](https://arxiv.org/html/2602.10798v1#S1.p3.1 "1 Introduction ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [16]
  X. Guo and G. Wu (2009)
  Smooth fit principle for impulse control of multidimensional diffusion processes.
  SIAM Journal on Control and Optimization 48 (2),  pp. 594–617.
  External Links: [Document](https://dx.doi.org/10.1137/080716001)
  Cited by: [§3.3](https://arxiv.org/html/2602.10798v1#S3.SS3.p1.1 "3.3 On the Smooth-Fit Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays"),
  [§3.3](https://arxiv.org/html/2602.10798v1#S3.SS3.p3.14 "3.3 On the Smooth-Fit Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [17]
  X. D. He, C. Yang, and Y. Zhou (2025)
  Arbitrage on decentralized exchanges.
  arXiv preprint arXiv:2507.08302.
  Cited by: [§1](https://arxiv.org/html/2602.10798v1#S1.p3.1 "1 Introduction ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [18]
  S. Jaimungal, Y. F. Saporito, M. O. Souza, and Y. Thamsten (2023)
  Optimal trading in automatic market makers with deep learning.
  arXiv preprint arXiv:2304.02180.
  Cited by: [§1](https://arxiv.org/html/2602.10798v1#S1.p3.1 "1 Introduction ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [19]
  B. Oksendal and A. Sulem (2008)
  Optimal stochastic impulse control with delayed reaction.
  Applied Mathematics and Optimization 58 (2),  pp. 243–255.
  Cited by: [§1](https://arxiv.org/html/2602.10798v1#S1.p2.1 "1 Introduction ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays"),
  [§3.1](https://arxiv.org/html/2602.10798v1#S3.SS1.1.p1.19 "Proof. ‣ 3.1 Dynamic programming principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [20]
  B. Oksendal (2005)
  Optimal stopping with delayed information.
  Stochastics and Dynamics 05 (02),  pp. 271–280.
  External Links: [Document](https://dx.doi.org/10.1142/S0219493705001419)
  Cited by: [§1](https://arxiv.org/html/2602.10798v1#S1.p2.1 "1 Introduction ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [21]
  H. Pham (1997)
  Optimal stopping, free boundary, and american option in a jump-diffusion model.
  Applied Mathematics and Optimization 35 (2),  pp. 145–164.
  Cited by: [§3.3](https://arxiv.org/html/2602.10798v1#S3.SS3.p1.1 "3.3 On the Smooth-Fit Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [22]
  P.E. Protter (2005)
  Stochastic integration and differential equations.
  Stochastic Modelling and Applied Probability, Springer Berlin Heidelberg.
  External Links: ISBN 9783540003137,
  LCCN 89026265
  Cited by: [§2](https://arxiv.org/html/2602.10798v1#S2.2.p1.1 "Proof. ‣ 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [23]
  W. Rudin (1976)
  Principles of mathematical analysis.
  3rd edition, McGraw-Hill, New York.
  Cited by: [§A.1](https://arxiv.org/html/2602.10798v1#A1.SS1.8.p2.15 "Proof. ‣ A.1 Viscosity Solution ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").
* [24]
  R. C. Seydel (2009)
  Existence and uniqueness of viscosity solutions for qvi associated with impulse control of jump-diffusions.
  Stochastic Processes and their Applications 119 (10),  pp. 3719–3748.
  External Links: ISSN 0304-4149,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.spa.2009.07.004)
  Cited by: [Remark A.8](https://arxiv.org/html/2602.10798v1#A1.Thmtheorem8.p1.1.1 "Remark A.8. ‣ Proof. ‣ A.3 Uniqueness and Continuity Result ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays").

## Appendix A Proofs of the Results in Section [3](https://arxiv.org/html/2602.10798v1#S3 "3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")

### A.1 Viscosity Solution

We now provide detailed proofs of Proposition [3.4](https://arxiv.org/html/2602.10798v1#S3.Thmtheorem4 "Proposition 3.4. ‣ 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays"). We first present the proofs on the domain [0,T)×𝒟[0,T)\times{\cal D}, and then address separately the case corresponding to the terminal condition at time TT.

###### Lemma A.1.

The impulse operator ℳ{\cal M} maps 𝒞​([0,T]×𝒟){\cal C}([0,T]\times{\cal D}) into 𝒞​([0,T]×𝒟){\cal C}([0,T]\times{\cal D}).

###### Proof.

Let φ∈𝒞​([0,T]×𝒟)\varphi\in{\cal C}([0,T]\times{\cal D}), ε>0\varepsilon>0, i∈⟦1,K⟧i\in\llbracket 1,K\rrbracket and (t,x,𝔦,𝔳)∈[0,T)×𝒟(t,x,\mathfrak{i},\mathfrak{v})\in[0,T)\times{\cal D}. Then, for any h∈ℝ+nh\in\mathbb{R}\_{+}^{n} and ξ∈𝒰\xi\in{\cal U},

|  |  |  |
| --- | --- | --- |
|  | −ε<φ​(t+⟨𝔥,e1⟩,x+h,𝔦+ei,𝔳+ξ​ei)−φ​(t,x,𝔦+ei,𝔳+ξ​ei)<ε,-\varepsilon<\varphi(t+\langle\mathfrak{h},e\_{1}\rangle,x+h,\mathfrak{i}+e\_{i},\mathfrak{v}+\xi e\_{i})-\varphi(t,x,\mathfrak{i}+e\_{i},\mathfrak{v}+\xi e\_{i})<\varepsilon, |  |

for a sufficiently small ‖h‖<δ\|h\|<\delta thanks to the continuity of φ\varphi on [0,T]×𝒟[0,T]\times{\cal D}. Hence,

|  |  |  |
| --- | --- | --- |
|  | φ​(t,x,𝔦+ei,𝔳+ξ​ei)−ε<φ​(t+⟨𝔥,e1⟩,x+h,𝔦+ei,𝔳+ξ​ei)<φ​(t,x,𝔦+ei,𝔳+ξ​ei)+ε.\varphi(t,x,\mathfrak{i}+e\_{i},\mathfrak{v}+\xi e\_{i})-\varepsilon<\varphi(t+\langle\mathfrak{h},e\_{1}\rangle,x+h,\mathfrak{i}+e\_{i},\mathfrak{v}+\xi e\_{i})<\varphi(t,x,\mathfrak{i}+e\_{i},\mathfrak{v}+\xi e\_{i})+\varepsilon. |  |

Since ξ\xi is arbitrary, we obtain

|  |  |  |
| --- | --- | --- |
|  | ℳ​φ​(t,x,𝔦,𝔳)−ε≤ℳ​φ​(t,x+y,𝔦,𝔳)≤ℳ​φ​(t,x,𝔦,𝔳)+ε,{\cal M}\varphi(t,x,\mathfrak{i},\mathfrak{v})-\varepsilon\leq{\cal M}\varphi(t,x+y,\mathfrak{i},\mathfrak{v})\leq{\cal M}\varphi(t,x,\mathfrak{i},\mathfrak{v})+\varepsilon, |  |

by taking the infimum for a sufficiently small ‖h‖<δ\|h\|<\delta.
∎

###### Proposition A.2.

The value function vv is a viscosity super-solution of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) on [0,T)×𝒟[0,T)\times{\cal D}.

###### Proof.

Fix (t0,x0,𝔦0,𝔳0)∈[0,T)×𝒟(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\in[0,T)\times{\cal D}. We consider the case where ∑i=1N⟨𝔦0,ei⟩<K\sum\_{i=1}^{N}\langle\mathfrak{i}\_{0},e\_{i}\rangle<K. Now let φ∈C1,2​([0,T]×𝒟)\varphi\in C^{1,2}([0,T]\times{\cal D}) be such that
v∗​(t0,x0,𝔦0,𝔳0)=φ​(t0,x0,𝔦0,𝔳0)v\_{\*}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})=\varphi(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0}) and
v∗−φv\_{\*}-\varphi attains a local minimum at this point. In other words, there exists r0>0r\_{0}>0 such that

|  |  |  |
| --- | --- | --- |
|  | v∗​(t,x,𝔦0,𝔳0)≥φ​(t,x,𝔦0,𝔳0),∀(t,x)∈B¯r0​(t0,x0).v\_{\*}(t,x,\mathfrak{i}\_{0},\mathfrak{v}\_{0})\geq\varphi(t,x,\mathfrak{i}\_{0},\mathfrak{v}\_{0}),\quad\forall(t,x)\in\bar{B}\_{r\_{0}}(t\_{0},x\_{0}). |  |

By definition of v∗​(t0,x0,𝔦0,𝔳0)v\_{\*}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0}), there exists a sequence (tm,xm)∈[0,T)×ℝd(t\_{m},x\_{m})\in[0,T)\times\mathbb{R}^{d} such that
(tm,xm)→(t0,x0)(t\_{m},x\_{m})\to(t\_{0},x\_{0}) and v​(tm,xm,𝔦0,𝔳0)→v∗​(t0,x0,𝔦0,𝔳0)v(t\_{m},x\_{m},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\to v\_{\*}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})
as m→∞m\to\infty. By the continuity of φ\varphi, we also have

|  |  |  |
| --- | --- | --- |
|  | γm:=v​(tm,xm,𝔦0,𝔳0)−φ​(tm,xm,𝔦0,𝔳0)​→m→+∞​0.\gamma\_{m}:=v(t\_{m},x\_{m},\mathfrak{i}\_{0},\mathfrak{v}\_{0})-\varphi(t\_{m},x\_{m},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\underset{m\to+\infty}{\to}0. |  |

Set τ0=tn\tau\_{0}=t\_{n}, τn=+∞\tau\_{n}=+\infty for all n≥1n\geq 1 and choose (𝔦0,ξ0)(\mathfrak{i}\_{0},\xi\_{0}) arbitrarily in ⟦1,K⟧×ℝ+\llbracket 1,K\rrbracket\times\mathbb{R}\_{+} such that the control
α=((νs)s∈[0,T],(τn,In,ξn)n≥1)\alpha=\big((\nu\_{s})\_{s\in[0,T]},(\tau\_{n},I\_{n},\xi\_{n})\_{n\geq 1}\big)
is admissible, i.e. α∈𝒜K,𝔦0,𝔳0​(tm)\alpha\in\mathcal{A}\_{K,\mathfrak{i}\_{0},\mathfrak{v}\_{0}}(t\_{m}).

Consider the case where ξ0=0\xi\_{0}=0. Let the trading speed ν\nu be constant over time and equal to some a∈ℝa\in\mathbb{R}. Then αm∈𝒜K,𝔦0,𝔳0​(tm)\alpha\_{m}\in\mathcal{A}\_{K,\mathfrak{i}\_{0},\mathfrak{v}\_{0}}(t\_{m}). We denote by Xstm,xm,αmX^{t\_{m},x\_{m},\alpha\_{m}}\_{s} the associated controlled process.
Let τm\tau\_{m} be the stopping time defined by θm:=inf{s≥tm:Xstm,xm,αm∉B¯r0​(xm)}∧τ~02∧T\theta\_{m}:=\inf\{s\geq t\_{m}:X^{t\_{m},x\_{m},\alpha\_{m}}\_{s}\notin\bar{B}\_{r\_{0}}(x\_{m})\}\wedge\frac{\tilde{\tau}\_{0}}{2}\wedge T. Let (hm)m≥1(h\_{m})\_{m\geq 1} be a strictly positive sequence such that hm​→m→+∞​0h\_{m}\underset{m\to+\infty}{\to}0 and γm/hm​→m→+∞​0.\gamma\_{m}/h\_{m}\underset{m\to+\infty}{\to}0. We apply the dynamic programming principle (DPP) (see Theorem [3.1](https://arxiv.org/html/2602.10798v1#S3.Thmtheorem1 "Theorem 3.1 (Dynamic Programming Principle). ‣ 3.1 Dynamic programming principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) at time t~m:=θm∧(tm+hm)\tilde{t}\_{m}:=\theta\_{m}\wedge(t\_{m}+h\_{m}), we have that

|  |  |  |
| --- | --- | --- |
|  | v(tm,xm,𝔦0,𝔳0)≥𝔼[∫tmt~mf(s,Xstm,xm,αm,a)ds−∑τ~n∈(tm,t~m]c(τ~n,Xτ~n−tm,x,αm,ξn,In)+v(t~m,Xt~mtm,xm,αm,p(t~m,αm))]−ε.\begin{aligned} v(t\_{m},x\_{m},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\geq\mathbb{E}\bigg[&\int\_{t\_{m}}^{\tilde{t}\_{m}}f\big(s,X\_{s}^{t\_{m},x\_{m},\alpha\_{m}},a\big)\,\mathrm{\mathrm{d}}s-\sum\_{\tilde{\tau}\_{n}\in(t\_{m},\tilde{t}\_{m}]}c(\tilde{\tau}\_{n},X^{t\_{m},x,\alpha\_{m}}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})+v(\tilde{t}\_{m},X\_{\tilde{t}\_{m}}^{t\_{m},x\_{m},\alpha\_{m}},p(\tilde{t}\_{m},\alpha\_{m}))\bigg]-\varepsilon.\end{aligned} |  |

Since v≥v∗≥φv\geq v\_{\*}\geq\varphi, we get

|  |  |  |
| --- | --- | --- |
|  | φ(tm,xm,𝔦0,𝔳0)+γm≥𝔼[∫tmt~mf(s,Xstm,xm,αm,a)ds−∑τ~n∈(tm,t~m]c(τ~n,Xτ~n−tm,x,αm,ξn,In)+φ(t~m,Xt~mtm,xm,αm,p(t~m,αm))]−ε.\begin{aligned} \varphi(t\_{m},x\_{m},\mathfrak{i}\_{0},\mathfrak{v}\_{0})+\gamma\_{m}\geq\mathbb{E}\bigg[&\int\_{t\_{m}}^{\tilde{t}\_{m}}f\big(s,X\_{s}^{t\_{m},x\_{m},\alpha\_{m}},a\big)\,\mathrm{\mathrm{d}}s-\sum\_{\tilde{\tau}\_{n}\in(t\_{m},\tilde{t}\_{m}]}c(\tilde{\tau}\_{n},X^{t\_{m},x,\alpha\_{m}}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})+\varphi(\tilde{t}\_{m},X\_{\tilde{t}\_{m}}^{t\_{m},x\_{m},\alpha\_{m}},p(\tilde{t}\_{m},\alpha\_{m}))\bigg]-\varepsilon.\end{aligned} |  |

Applying Itô’s formula to the process s↦φ​(s,Xstm,xm,αm,p​(s,αm))s\mapsto\varphi\big(s,X\_{s}^{t\_{m},x\_{m},\alpha\_{m}},p(s,\alpha\_{m})\big) on the interval [tm,t~m][t\_{m},\tilde{t}\_{m}] under ξ0=0\xi\_{0}=0, and dividing the resulting identity by hmh\_{m}, we obtain

|  |  |  |
| --- | --- | --- |
|  | γmhm+𝔼[1hm∫tmt~m((−∂φ∂t−ℒaφ)(s,Xstm,xm,αm,p(s,αm))−f(s,Xstm,xm,αm,a)+∑i=1N𝟙{⟨𝔦​(s,αm),ei⟩>0}ℓic(s,Xstm,xm,αm,⟨𝔦(s,αm),ei⟩,⟨𝔳(s,αm),ei⟩)−∑i=1N𝟙{⟨𝔦​(s,αm),ei⟩>0}ℓi(φ(s,Γ(s,Xstm,xm,αm,⟨𝔳(s,αm),ei⟩),𝔦(s,αm)−⟨𝔦(s,αm),ei⟩ei,𝔳(s,αm)−⟨𝔳(s,αm),ei⟩ei)−φ(s,Xstm,xm,αm,p(s,αm))))ds]≥0,\begin{aligned} &\frac{\gamma\_{m}}{h\_{m}}+\mathbb{E}\Bigg[\frac{1}{h\_{m}}\int\_{t\_{m}}^{\tilde{t}\_{m}}\bigg(\Big(-\frac{\partial\varphi}{\partial t}-\mathcal{L}^{a}\varphi\Big)(s,X^{t\_{m},x\_{m},\alpha\_{m}}\_{s},p(s,\alpha\_{m}))-f\big(s,X^{t\_{m},x\_{m},\alpha\_{m}}\_{s},a\big)+\sum\_{i=1}^{N}\mathds{1}\_{\{\langle\mathfrak{i}(s,\alpha\_{m}),e\_{i}\rangle>0\}}\,\ell\_{i}c\big(s,X^{t\_{m},x\_{m},\alpha\_{m}}\_{s},\langle\mathfrak{i}(s,\alpha\_{m}),e\_{i}\rangle,\langle\mathfrak{v}(s,\alpha\_{m}),e\_{i}\rangle\big)\\ &-\sum\_{i=1}^{N}\mathds{1}\_{\{\langle\mathfrak{i}(s,\alpha\_{m}),e\_{i}\rangle>0\}}\,\ell\_{i}\Big(\varphi\big(s,\Gamma(s,X^{t\_{m},x\_{m},\alpha\_{m}}\_{s},\langle\mathfrak{v}(s,\alpha\_{m}),e\_{i}\rangle),\mathfrak{i}(s,\alpha\_{m})-\langle\mathfrak{i}(s,\alpha\_{m}),e\_{i}\rangle e\_{i},\mathfrak{v}(s,\alpha\_{m})-\langle\mathfrak{v}(s,\alpha\_{m}),e\_{i}\rangle e\_{i}\big)-\varphi\big(s,X^{t\_{m},x\_{m},\alpha\_{m}}\_{s},p(s,\alpha\_{m})\big)\Big)\bigg)\mathrm{d}s\,\Bigg]\geq 0,\end{aligned} |  |

after observing that the stochastic integral term vanishes when taking expectations, as its integrand is bounded from the growth conditions in Assumptions [2.1](https://arxiv.org/html/2602.10798v1#S2.ThmAssumption1 "Assumption 2.1. ‣ 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays"). The dynamics of Xtm,x,αmX^{t\_{m},x,\alpha\_{m}} between tmt\_{m} and t~m\tilde{t}\_{m} are therefore governed by the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xutm,xm,αm\displaystyle X^{t\_{m},x\_{m},\alpha\_{m}}\_{u} | =x+∫tub​(s,Xstm,xm,αm,a)​ds+∫tuσ​(s,Xstm,xm,αm,a)​dWs,∀u∈[tm,t~m].\displaystyle=x+\int\_{t}^{u}b(s,X^{t\_{m},x\_{m},\alpha\_{m}}\_{s},a)\,\mathrm{d}s+\int\_{t}^{u}\sigma(s,X^{t\_{m},x\_{m},\alpha\_{m}}\_{s},a)\,\mathrm{d}W\_{s},\quad\forall u\in[t\_{m},\tilde{t}\_{m}]. |  |

Therefore, the trajectory Xstm,xm,αmX^{t\_{m},x\_{m},\alpha\_{m}}\_{s} is almost surely continuous tmt\_{m} and t~m\tilde{t}\_{m}. We deduce that for mm sufficiently large, it holds that θm=tm+hm\theta\_{m}=t\_{m}+h\_{m} almost surely. Now let Δ​Ni(m):=Ntm+hmi−Ntmi\Delta N\_{i}^{(m)}:=N^{i}\_{t\_{m}+h\_{m}}-N^{i}\_{t\_{m}} be the number of execution opportunities for priority level ii
on (tn,T](t\_{n},T]. Hence, we have that Δ​Ni(m)∼Poisson​(ℓi​hm)\Delta N\_{i}^{(m)}\sim\mathrm{Poisson}(\ell\_{i}h\_{m}), and

|  |  |  |
| --- | --- | --- |
|  | ℙ​(Δ​Ni(m)≥1)=1−e−ℓi​hm≤ℓi​hm​→m→+∞​0.\mathbb{P}\Big(\Delta N\_{i}^{(m)}\geq 1\Big)=1-e^{-\ell\_{i}h\_{m}}\leq\ell\_{i}h\_{m}\underset{m\to+\infty}{\to}0. |  |

Since ξ0=0\xi\_{0}=0, there are no new orders from our control on (tm,t~m](t\_{m},\tilde{t}\_{m}]. Consequently,

|  |  |  |
| --- | --- | --- |
|  | limm→+∞ℙ​(p​(s,αm)=(𝔦0,𝔳0),∀s∈(tm,t~m])=1.\lim\_{m\to+\infty}\mathbb{P}\Big(p(s,\alpha\_{m})=(\mathfrak{i}\_{0},\mathfrak{v}\_{0}),~~\forall s\in(t\_{m},\tilde{t}\_{m}]\Big)=1. |  |

Applying the mean value theorem, −∂φ∂t​(s,Xstm,xm,αm,𝔦0,𝔳0)−Ha​(s,Xstm,xm,αm,𝔦0,𝔳0,φ,∂φ∂x,∂2φ∂x2)-\frac{\partial\varphi}{\partial t}(s,X^{t\_{m},x\_{m},\alpha\_{m}}\_{s},\mathfrak{i}\_{0},\mathfrak{v}\_{0})-H^{a}(s,X^{t\_{m},x\_{m},\alpha\_{m}}\_{s},\mathfrak{i}\_{0},\mathfrak{v}\_{0},\varphi,\frac{\partial\varphi}{\partial x},\frac{\partial^{2}\varphi}{\partial x^{2}})
then converges almost surely to

|  |  |  |
| --- | --- | --- |
|  | −∂φ∂t​(t0,x0,𝔦0,𝔳0)−Ha​(t0,x0,𝔦0,𝔳0,φ,∂φ∂x,∂2φ∂x2),-\frac{\partial\varphi}{\partial t}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})-H^{a}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0},\varphi,\tfrac{\partial\varphi}{\partial x},\tfrac{\partial^{2}\varphi}{\partial x^{2}}), |  |

as m→+∞m\to+\infty. In addition, it is uniformly bounded by a constant independent of mm. Therefore, by the dominated convergence theorem, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∂φ∂t​(t0,x0,𝔦0,𝔳0)−Ha​(t0,x0,𝔦0,𝔳0,φ,∂φ∂x,∂2φ∂x2)≥0.\begin{split}-\frac{\partial\varphi}{\partial t}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})-H^{a}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0},\varphi,\tfrac{\partial\varphi}{\partial x},\tfrac{\partial^{2}\varphi}{\partial x^{2}})\geq 0.\end{split} |  | (26) |

The desired result follows from the arbitrariness of a∈ℝa\in\mathbb{R}.

Let us now examine the case ξ0>0\xi\_{0}>0. In what follows, we make no specific assumption on the trading speed ν\nu. We apply the DPP again at time t~m:=θm∧(tm+hm)\tilde{t}\_{m}:=\theta\_{m}\wedge(t\_{m}+h\_{m}), we have that

|  |  |  |
| --- | --- | --- |
|  | v(tm,xm,𝔦0,𝔳0)≥𝔼[∫tmt~mf​(s,Xstm,xm,αm,νs)​ds−∑τ~n∈(t,t~m]c​(τ~n,Xτ~n−t,x,αm,ξn,In)+v(t~m,Xt~mtm,xm,αm,𝔦(t~m,αm)+eI0,𝔳(t~m,αm)+ξ0eI0)]−ε.\begin{split}v(t\_{m},x\_{m},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\geq\mathbb{E}\bigg[&\int\_{t\_{m}}^{\tilde{t}\_{m}}f\big(s,X\_{s}^{t\_{m},x\_{m},\alpha\_{m}},\nu\_{s}\big)\,\mathrm{\mathrm{d}}s-\sum\_{\tilde{\tau}\_{n}\in(t,\tilde{t}\_{m}]}c(\tilde{\tau}\_{n},X^{t,x,\alpha\_{m}}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})\\ &+v\big(\tilde{t}\_{m},X\_{\tilde{t}\_{m}}^{t\_{m},x\_{m},\alpha\_{m}},\mathfrak{i}(\tilde{t}\_{m},\alpha\_{m})+e\_{I\_{0}},\mathfrak{v}(\tilde{t}\_{m},\alpha\_{m})+\xi\_{0}e\_{I\_{0}}\big)\bigg]-\varepsilon.\end{split} |  |

Knowing that v≥v∗≥φv\geq v\_{\*}\geq\varphi and letting mm go to infinity, get that

|  |  |  |
| --- | --- | --- |
|  | v(t0,x0,𝔦0,𝔳0)≥𝔼[φ(t0,x0,𝔦0+eI0,𝔳0+ξ0eI0)]−ε.\begin{split}v(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\geq\mathbb{E}\bigg[&\varphi\big(t\_{0},x\_{0},\mathfrak{i}\_{0}+e\_{I\_{0}},\mathfrak{v}\_{0}+\xi\_{0}e\_{I\_{0}}\big)\bigg]-\varepsilon.\end{split} |  |

The last inequality hold for every (ξ,i)∈𝒰×⟦1,K⟧(\xi,i)\in{\cal U}\times{\llbracket 1,K\rrbracket}. Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | v(t0,x0,𝔦0,𝔳0)≥𝔼[sup(ξ,I)∈𝒰×⟦1,K⟧φ(t0,x0,𝔦0+eI0,𝔳0+ξ0eI0)]−ε≥ℳφ(t0,x0,𝔦0,𝔳0)−ε.\begin{split}v(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\geq\mathbb{E}\bigg[&\sup\_{(\xi,I)\in{\cal U}\times{\llbracket 1,K\rrbracket}}\varphi\big(t\_{0},x\_{0},\mathfrak{i}\_{0}+e\_{I\_{0}},\mathfrak{v}\_{0}+\xi\_{0}e\_{I\_{0}}\big)\bigg]-\varepsilon\geq\mathcal{M}\varphi(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})-\varepsilon.\end{split} |  | (27) |

Combining ([26](https://arxiv.org/html/2602.10798v1#A1.E26 "In Proof. ‣ A.1 Viscosity Solution ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([27](https://arxiv.org/html/2602.10798v1#A1.E27 "In Proof. ‣ A.1 Viscosity Solution ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")), and using the arbitrariness of ε\varepsilon, concludes the proof. The case where ∑i=1N⟨𝔦0,ei⟩=K\sum\_{i=1}^{N}\langle\mathfrak{i}\_{0},e\_{i}\rangle=K is handled similarly to the first part of the proof.
∎

###### Proposition A.3.

The value function vv is a viscosity sub-solution of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) on [0,T)×𝒟[0,T)\times{\cal D}.

###### Proof.

Fix (t0,x0,𝔦0,𝔳0)∈[0,T)×𝒟(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\in[0,T)\times{\cal D}. As in the previous case, we detail the proof only when ∑i=1N⟨𝔦0,ei⟩<K\sum\_{i=1}^{N}\langle\mathfrak{i}\_{0},e\_{i}\rangle<K, since the arguments for the equality case ∑i=1N⟨𝔦0,ei⟩=K\sum\_{i=1}^{N}\langle\mathfrak{i}\_{0},e\_{i}\rangle=K follow directly by the same reasoning. Let φ∈C1,2​([0,T]×𝒟)\varphi\in C^{1,2}([0,T]\times{\cal D}) be such that
v∗​(t0,x0,𝔦0,𝔳0)=φ​(t0,x0,𝔦0,𝔳0)v^{\*}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})=\varphi(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0}) and
v∗−φv^{\*}-\varphi attains a local maximum at this point. In other words, there exists r0>0r\_{0}>0 such that

|  |  |  |
| --- | --- | --- |
|  | v∗​(t,x,𝔦0,𝔳0)≤φ​(t,x,𝔦0,𝔳0),∀(t,x)∈B¯r0​(t0,x0).v^{\*}(t,x,\mathfrak{i}\_{0},\mathfrak{v}\_{0})\leq\varphi(t,x,\mathfrak{i}\_{0},\mathfrak{v}\_{0}),\quad\forall(t,x)\in\bar{B}\_{r\_{0}}(t\_{0},x\_{0}). |  |

If (v∗−ℳ​v∗)​(t0,x0,𝔦0,𝔳0)≤0(v^{\*}-\mathcal{M}v^{\*})(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\leq 0, the subsolution condition is immediately satisfied. Now assume that (v∗−ℳ​v∗)​(t0,x0,𝔦0,𝔳0)>0(v^{\*}-\mathcal{M}v^{\*})(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})>0 and that there exists η>0\eta>0 such that

|  |  |  |
| --- | --- | --- |
|  | −∂φ∂t​(t0,x0,𝔦0,𝔳0)−supa∈ℝHa​(t0,x0,𝔦0,𝔳0,φ,∂φ∂x,∂2φ∂x2)>η​and​(φ−ℳ​φ)​(t0,x0,𝔦0,𝔳0)>η.-\frac{\partial\varphi}{\partial t}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})-\sup\_{a\in\mathbb{R}}H^{a}\Big(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0},\varphi,\tfrac{\partial\varphi}{\partial x},\tfrac{\partial^{2}\varphi}{\partial x^{2}}\Big)>\eta~~\text{and}~~\big(\varphi-\mathcal{M}\varphi\big)(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})>\eta. |  |

Note that, by Assumptions [2.1](https://arxiv.org/html/2602.10798v1#S2.ThmAssumption1 "Assumption 2.1. ‣ 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays"), the functions bb, σ\sigma, Γ\Gamma, cc and ff are continuous in (t,x,a)(t,x,a) and satisfy linear growth conditions.
The term

|  |  |  |
| --- | --- | --- |
|  | (t,x,a)↦∑i=1N𝟙{⟨𝔦0,ei⟩>0}​ℓi​(φ​(t,Γ​(t,x,⟨𝔳0,ei⟩),𝔦0−⟨𝔦0,ei⟩​ei,𝔳−⟨𝔳0,ei⟩​ei)−φ​(t,x,𝔦0,𝔳0)+c​(t,x,⟨𝔦0,ei⟩,⟨𝔳0,ei⟩))\begin{aligned} (t,x,a)\mapsto\sum\_{i=1}^{N}\mathds{1}\_{\{\langle\mathfrak{i}\_{0},e\_{i}\rangle>0\}}\,\ell\_{i}\Big(\varphi\big(t,\Gamma(t,x,\langle\mathfrak{v}\_{0},e\_{i}\rangle),\mathfrak{i}\_{0}-\langle\mathfrak{i}\_{0},e\_{i}\rangle e\_{i},\mathfrak{v}-\langle\mathfrak{v}\_{0},e\_{i}\rangle e\_{i}\big)-\varphi(t,x,\mathfrak{i}\_{0},\mathfrak{v}\_{0})+c(t,x,\langle\mathfrak{i}\_{0},e\_{i}\rangle,\langle\mathfrak{v}\_{0},e\_{i}\rangle)\Big)\end{aligned} |  |

involves only finitely many indices and continuous mappings, and is therefore continuous as well.
Assumptions [2.1](https://arxiv.org/html/2602.10798v1#S2.ThmAssumption1 "Assumption 2.1. ‣ 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays") guarantee that σ​σ⊤\sigma\sigma^{\top} is uniformly elliptic and jointly continuous, implying continuity of the trace term (t,x,a)↦12​Tr​(σ​σ⊤​(t,x,a)​∂2φ∂x2​(t,x,𝔦0,𝔳0))(t,x,a)\mapsto\frac{1}{2}\,\mathrm{Tr}\Big(\sigma\sigma^{\top}(t,x,a)\,\frac{\partial^{2}\varphi}{\partial x^{2}}(t,x,\mathfrak{i}\_{0},\mathfrak{v}\_{0})\Big). Hence, the differential operator ℒa​φ\mathcal{L}^{a}\varphi is continuous in (t,x,a)(t,x,a) for each fixed (𝔦0,𝔳0)(\mathfrak{i}\_{0},\mathfrak{v}\_{0}). Since ℝ\mathbb{R} is locally compact, Berge’s maximum theorem (see [[23](https://arxiv.org/html/2602.10798v1#bib.bib24 "Principles of mathematical analysis")]) ensures that the infinimum over aa preserves continuity. Thus, HH and ℳ​φ{\cal M}\varphi (see Lemma [A.1](https://arxiv.org/html/2602.10798v1#A1.Thmtheorem1 "Lemma A.1. ‣ A.1 Viscosity Solution ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) are continuous in all their arguments, and

|  |  |  |
| --- | --- | --- |
|  | (t,x)↦−∂φ∂t​(t,x,𝔦0,𝔳0)−supa∈ℝHa​(t,x,𝔦0,𝔳0,φ,∂φ∂x,∂2φ∂x2)​and​(t,x)↦(φ−ℳ​φ)​(t,x,𝔦0,𝔳0)(t,x)\mapsto-\frac{\partial\varphi}{\partial t}(t,x,\mathfrak{i}\_{0},\mathfrak{v}\_{0})-\sup\_{a\in\mathbb{R}}H^{a}\Big(t,x,\mathfrak{i}\_{0},\mathfrak{v}\_{0},\varphi,\tfrac{\partial\varphi}{\partial x},\tfrac{\partial^{2}\varphi}{\partial x^{2}}\Big)~~\text{and}~~(t,x)\mapsto\big(\varphi-\mathcal{M}\varphi\big)(t,x,\mathfrak{i}\_{0},\mathfrak{v}\_{0}) |  |

are continuous. Consequently, there exists 0<r1<r00<r\_{1}<r\_{0} such that t0+r1<Tt\_{0}+r\_{1}<T and

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∂φ∂t​(t,x,𝔦0,𝔳0)−supa∈ℝHa​(t,x,𝔦0,𝔳0,φ,∂φ∂x,∂2φ∂x2)>η​and​(φ−ℳ​φ)​(t,x,𝔦0,𝔳0)>η,-\frac{\partial\varphi}{\partial t}(t,x,\mathfrak{i}\_{0},\mathfrak{v}\_{0})-\sup\_{a\in\mathbb{R}}H^{a}\Big(t,x,\mathfrak{i}\_{0},\mathfrak{v}\_{0},\varphi,\tfrac{\partial\varphi}{\partial x},\tfrac{\partial^{2}\varphi}{\partial x^{2}}\Big)>\eta~~\text{and}~~\big(\varphi-\mathcal{M}\varphi\big)(t,x,\mathfrak{i}\_{0},\mathfrak{v}\_{0})>\eta, |  | (28) |

for all (t,x)∈B¯r1​(t0,x0)(t,x)\in\bar{B}\_{r\_{1}}(t\_{0},x\_{0}). By definition of the upper semi-continuous enveloppe v∗​(t0,x0,𝔦0,𝔳0)v^{\*}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0}), there exists a sequence (tm,xm)∈[0,T)×ℝd(t\_{m},x\_{m})\in[0,T)\times\mathbb{R}^{d} such that
(tm,xm)→(t0,x0)(t\_{m},x\_{m})\to(t\_{0},x\_{0}) and v​(tm,xm,𝔦0,𝔳0)→v∗​(t0,x0,𝔦0,𝔳0)v(t\_{m},x\_{m},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\to v^{\*}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})
as m→+∞m\to+\infty. By the continuity of φ\varphi, we get

|  |  |  |
| --- | --- | --- |
|  | γm:=v​(tm,xm,𝔦0,𝔳0)−φ​(tm,xm,𝔦0,𝔳0)​→m→+∞​0.\gamma\_{m}:=v(t\_{m},x\_{m},\mathfrak{i}\_{0},\mathfrak{v}\_{0})-\varphi(t\_{m},x\_{m},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\underset{m\to+\infty}{\to}0. |  |

Let ε>0\varepsilon>0 and (hm)m≥1(h\_{m})\_{m\geq 1} be a strictly positive sequence such that hm​→m→+∞​0h\_{m}\underset{m\to+\infty}{\to}0 and γm/hm​→m→+∞​0.\gamma\_{m}/h\_{m}\underset{m\to+\infty}{\to}0. Define θm\theta\_{m} as the first exit time of the controlled state
(s,Xstm,xm,αmε)(s,X\_{s}^{t\_{m},x\_{m},\alpha\_{m}^{\varepsilon}})
from B¯r1​(t0,x0)\bar{B}\_{r\_{1}}(t\_{0},x\_{0}), truncated at tm+hmt\_{m}+h\_{m}. In other words,

|  |  |  |
| --- | --- | --- |
|  | θm:=inf{s≥tm:(s,Xstm,xm,αmε)∉B¯r1​(t0,x0)}∧τ~02∧(tm+hm)∧T.\theta\_{m}:=\inf\Big\{s\geq t\_{m}:\ \big(s,X\_{s}^{t\_{m},x\_{m},\alpha\_{m}^{\varepsilon}}\big)\notin\bar{B}\_{r\_{1}}(t\_{0},x\_{0})\Big\}\wedge\frac{\tilde{\tau}\_{0}}{2}\wedge(t\_{m}+h\_{m})\wedge T. |  |

We apply the dynamic programming principle (DPP2) (see Theorem [3.1](https://arxiv.org/html/2602.10798v1#S3.Thmtheorem1 "Theorem 3.1 (Dynamic Programming Principle). ‣ 3.1 Dynamic programming principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) at time t~m:=θm∧(tm+hm)\tilde{t}\_{m}:=\theta\_{m}\wedge(t\_{m}+h\_{m}), there exists a control αmε:=((νs)s∈[0,T],(τn,In,ξn)n≥1)\alpha^{\varepsilon}\_{m}:=\big((\nu\_{s})\_{s\in[0,T]},(\tau\_{n},I\_{n},\xi\_{n})\_{n\geq 1}\big) such that

|  |  |  |
| --- | --- | --- |
|  | v​(tm,xm,𝔦0,𝔳0)≤𝔼​[∫tmt~mf​(s,Xstm,xm,αmε,νs)​ds−∑τ~n∈(tm,t~m]c​(τ~n,Xτ~n−tm,x,αmε,ξn,In)+v​(t~m,Xt~mtm,xm,αmε,p​(t~m,αmε))]+ε.\begin{aligned} v(t\_{m},x\_{m},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\leq\mathbb{E}\bigg[\int\_{t\_{m}}^{\tilde{t}\_{m}}f\big(s,X\_{s}^{t\_{m},x\_{m},\alpha\_{m}^{\varepsilon}},\nu\_{s}\big)\,\mathrm{d}s-\sum\_{\tilde{\tau}\_{n}\in(t\_{m},\tilde{t}\_{m}]}c(\tilde{\tau}\_{n},X^{t\_{m},x,\alpha\_{m}^{\varepsilon}}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})+v\big(\tilde{t}\_{m},X\_{\tilde{t}\_{m}}^{t\_{m},x\_{m},\alpha\_{m}^{\varepsilon}},p(\tilde{t}\_{m},\alpha\_{m}^{\varepsilon})\big)\bigg]+\varepsilon.\end{aligned} |  |

Subtracting φ​(tm,xm,𝔦0,𝔳0)\varphi(t\_{m},x\_{m},\mathfrak{i}\_{0},\mathfrak{v}\_{0}) and using v∗≤φv^{\*}\leq\varphi on B¯r1​(t0,x0)\bar{B}\_{r\_{1}}(t\_{0},x\_{0}) gives

|  |  |  |
| --- | --- | --- |
|  | γm≤𝔼[∫tmt~mf(s,Xstm,xm,αmε,νs)ds−∑τ~n∈(tm,t~m]c(τ~n,Xτ~n−tm,x,αmε,ξn,In)+φ(t~m,Xt~mtm,xm,αmε,p(t~m,αmε))−φ(tm,xm,𝔦0,𝔳0)]+ε.\begin{split}\gamma\_{m}\leq&\mathbb{E}\bigg[\int\_{t\_{m}}^{\tilde{t}\_{m}}f\big(s,X\_{s}^{t\_{m},x\_{m},\alpha\_{m}^{\varepsilon}},\nu\_{s}\big)\,\mathrm{d}s-\sum\_{\tilde{\tau}\_{n}\in(t\_{m},\tilde{t}\_{m}]}c(\tilde{\tau}\_{n},X^{t\_{m},x,\alpha\_{m}^{\varepsilon}}\_{\tilde{\tau}^{-}\_{n}},\xi\_{n},I\_{n})\\ &\qquad+\varphi\big(\tilde{t}\_{m},X\_{\tilde{t}\_{m}}^{t\_{m},x\_{m},\alpha\_{m}^{\varepsilon}},p(\tilde{t}\_{m},\alpha\_{m}^{\varepsilon})\big)-\varphi(t\_{m},x\_{m},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\bigg]+\varepsilon.\end{split} |  |

Applying Itô’s formula to φ\varphi on [tm,t~m][t\_{m},\tilde{t}\_{m}] and taking expectations yields ,

|  |  |  |
| --- | --- | --- |
|  | γm≤𝔼​[∫tmt~m∂φ∂t​(s,Xstm,xm,αmε,p​(s,αmε))+Hνs​(s,Xstm,xm,αmε,p​(s,αmε),φ,∂φ∂x,∂2φ∂x2)​d​s]+ε.\gamma\_{m}\leq\mathbb{E}\bigg[\int\_{t\_{m}}^{\tilde{t}\_{m}}\frac{\partial\varphi}{\partial t}(s,X\_{s}^{t\_{m},x\_{m},\alpha\_{m}^{\varepsilon}},p(s,\alpha\_{m}^{\varepsilon}))+H^{\nu\_{s}}\big(s,X\_{s}^{t\_{m},x\_{m},\alpha\_{m}^{\varepsilon}},p(s,\alpha\_{m}^{\varepsilon}),\varphi,\tfrac{\partial\varphi}{\partial x},\tfrac{\partial^{2}\varphi}{\partial x^{2}}\big)\,\mathrm{d}s\bigg]+\varepsilon. |  |

Since (φ−ℳ​φ)>η(\varphi-{\cal M}\varphi)>\eta on B¯r1​(t0,x0)\bar{B}\_{r\_{1}}(t\_{0},x\_{0}), impulses strictly decrease the continuation value of φ\varphi.
Thus, for ε\varepsilon and mm small enough, αmε\alpha\_{m}^{\varepsilon} involves no intervention on (tm,t~m](t\_{m},\tilde{t}\_{m}] and ℙ​(p​(s,αmε)​→m→+∞​(𝔦0,𝔳0),∀s∈[tm,t~m])=1\mathbb{P}\Big(p(s,\alpha\_{m}^{\varepsilon})\underset{m\to+\infty}{\to}(\mathfrak{i}\_{0},\mathfrak{v}\_{0}),~~\forall s\in[t\_{m},\tilde{t}\_{m}]\Big)=1. Hence, by ([28](https://arxiv.org/html/2602.10798v1#A1.E28 "In Proof. ‣ A.1 Viscosity Solution ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")), we get

|  |  |  |
| --- | --- | --- |
|  | γm≤−η​𝔼​[t~m−tm]+ε.\gamma\_{m}\leq-\eta\,\mathbb{E}[\tilde{t}\_{m}-t\_{m}]+\varepsilon. |  |

Since 𝔼​[t~m−tm]≤hm\mathbb{E}[\tilde{t}\_{m}-t\_{m}]\leq h\_{m}, taking ε=η2​hm\varepsilon=\tfrac{\eta}{2}h\_{m} gives

|  |  |  |
| --- | --- | --- |
|  | γm≤−η2​hm.\gamma\_{m}\leq-\tfrac{\eta}{2}h\_{m}. |  |

Dividing by hmh\_{m} and sending m→+∞m\to+\infty leads to a contradiction.
∎

### A.2 Terminal Condition

We now turn to the analysis of the terminal condition.

###### Proposition A.4.

The value function vv defined in ([7](https://arxiv.org/html/2602.10798v1#S2.E7 "In 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) satisfies

|  |  |  |
| --- | --- | --- |
|  | v​(T−,x,𝔦,𝔳)=v​(T,x,𝔦,𝔳)=g​(x),∀(x,𝔦,𝔳)∈𝒟.v(T^{-},x,\mathfrak{i},\mathfrak{v})=v(T,x,\mathfrak{i},\mathfrak{v})=g(x),\quad\forall(x,\mathfrak{i},\mathfrak{v})\in{\cal D}. |  |

###### Proof.

Let (x,𝔦,𝔳)∈𝒟(x,\mathfrak{i},\mathfrak{v})\in{\cal D} and a sequence (tn)n≥1(t\_{n})\_{n\geq 1} such that limn→+∞​tn=T\underset{n\to+\infty}{\lim}t\_{n}=T. By the DPP at τ=T\tau=T, there exists αnε∈𝒜K,𝔦,𝔳​(tn)\alpha\_{n}^{\varepsilon}\in\mathcal{A}\_{K,\mathfrak{i},\mathfrak{v}}(t\_{n}) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(tn,x,αnε)−ε≤v​(tn,x,𝔦,𝔳)≤J​(tn,x,αnε),J(t\_{n},x,\alpha\_{n}^{\varepsilon})-\varepsilon\leq v(t\_{n},x,\mathfrak{i},\mathfrak{v})\leq J(t\_{n},x,\alpha\_{n}^{\varepsilon}), |  | (29) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | J(tn,x,αnε)=𝔼[\displaystyle J(t\_{n},x,\alpha\_{n}^{\varepsilon})=\mathbb{E}\bigg[ | ∫tnTf(s,Xstn,x,αnε,νs)ds−∑τ~m∈(tn,T]c(τ~m,Xτ~m−tn,x,αnε,ξm,Im)+v(T,XTT,x,αnε,p(T,αnε))].\displaystyle\int\_{t\_{n}}^{T}f(s,X^{t\_{n},x,\alpha\_{n}^{\varepsilon}}\_{s},\nu\_{s})\mathrm{d}s-\sum\_{\tilde{\tau}\_{m}\in(t\_{n},T]}c(\tilde{\tau}\_{m},X^{t\_{n},x,\alpha\_{n}^{\varepsilon}}\_{\tilde{\tau}^{-}\_{m}},\xi\_{m},I\_{m})+v(T,X^{T,x,\alpha\_{n}^{\varepsilon}}\_{T},p(T,\alpha\_{n}^{\varepsilon}))\bigg]. |  |

Note that, for notational simplicity, we omit writing the dependence of (ν,(ξm,Im)m≥1)\big(\nu,(\xi\_{m},I\_{m})\_{m\geq 1}\big) on ε\varepsilon. Set hn:=T−tn↓0h\_{n}:=T-t\_{n}\downarrow 0. By the continuity and growth conditions on ff (see Assumptions [2.1](https://arxiv.org/html/2602.10798v1#S2.ThmAssumption1 "Assumption 2.1. ‣ 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and the moment bounds for XαX^{\alpha} (see Proposition [2.2](https://arxiv.org/html/2602.10798v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")),

|  |  |  |
| --- | --- | --- |
|  | ∫tnTf​(s,Xstn,x,αnε,νs)​ds→n→∞L10.\int\_{t\_{n}}^{T}f(s,X^{t\_{n},x,\alpha\_{n}^{\varepsilon}}\_{s},\nu\_{s})\mathrm{d}s\xrightarrow[n\to\infty]{L^{1}}0. |  |

Let Δ​Ni(n):=NTi−Ntni\Delta N\_{i}^{(n)}:=N^{i}\_{T}-N^{i}\_{t\_{n}}. We have that Δ​Ni(n)∼Poisson​(ℓi​hn)\Delta N\_{i}^{(n)}\sim\mathrm{Poisson}(\ell\_{i}h\_{n}). Hence,

|  |  |  |
| --- | --- | --- |
|  | ℙ​(Δ​Ni(n)≥1)=1−e−ℓi​hn≤ℓi​hn→n→∞0.\mathbb{P}\Big(\Delta N\_{i}^{(n)}\geq 1\Big)=1-e^{-\ell\_{i}h\_{n}}\leq\ell\_{i}h\_{n}\xrightarrow[n\to\infty]{}0. |  |

By admissibility and the
growth bound on cc, then by linearity of expectation and nonnegativity,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∑τ~m∈(tn,T]c​(τ~m,Xτ~mtn,x,αnε,ξm,Im)]\displaystyle\mathbb{E}\bigg[\sum\_{\tilde{\tau}\_{m}\in(t\_{n},T]}c(\tilde{\tau}\_{m},X^{t\_{n},x,\alpha\_{n}^{\varepsilon}}\_{\tilde{\tau}\_{m}},\xi\_{m},I\_{m})\bigg] | ≤𝔼​[Cc​(1+suptn≤u≤T​‖Xutn,x,αnε‖+V¯)]​𝔼​[∑i=1NΔ​Ni(n)]\displaystyle\leq\mathbb{E}\bigg[C\_{c}\Big(1+\underset{t\_{n}\leq u\leq T}{\sup}\|X^{t\_{n},x,\alpha\_{n}^{\varepsilon}}\_{u}\|+\bar{V}\Big)\bigg]\mathbb{E}\bigg[\sum\_{i=1}^{N}\Delta N\_{i}^{(n)}\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Cc​(1+𝔼​[suptn≤u≤T​‖Xutn,x,αnε‖]+V¯)​(∑i=1Nℓi)​hn→n→∞0.\displaystyle=C\_{c}\Bigg(1+\mathbb{E}\bigg[\underset{t\_{n}\leq u\leq T}{\sup}\|X^{t\_{n},x,\alpha\_{n}^{\varepsilon}}\_{u}\|\bigg]+\bar{V}\Bigg)\Big(\sum\_{i=1}^{N}\ell\_{i}\Big)\,h\_{n}\xrightarrow[n\to\infty]{}0. |  |

Since limn→+∞​XTtn,x,α=x\underset{n\to+\infty}{\lim}X^{t\_{n},x,\alpha}\_{T}=x in probability, the dominated convergence yields

|  |  |  |
| --- | --- | --- |
|  | limn→+∞J​(tn,x,αnε)=𝔼​[v​(T,XTT,x,αnε,p​(T,αnε))]=v​(T,x,𝔦,𝔳)=g​(x)\lim\_{n\to+\infty}J(t\_{n},x,\alpha\_{n}^{\varepsilon})=\mathbb{E}\Big[v(T,X^{T,x,\alpha\_{n}^{\varepsilon}}\_{T},p(T,\alpha\_{n}^{\varepsilon}))\Big]=v(T,x,\mathfrak{i},\mathfrak{v})=g(x) |  |

Hence, by applying inequality ([29](https://arxiv.org/html/2602.10798v1#A1.E29 "In Proof. ‣ A.2 Terminal Condition ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and noting that ε\varepsilon can be chosen arbitrarily, we obtain the desired result.
∎

### A.3 Uniqueness and Continuity Result

The detailed proofs of Theorem [3.5](https://arxiv.org/html/2602.10798v1#S3.Thmtheorem5 "Theorem 3.5 (Comparison principle). ‣ 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays") are presented below.

###### Definition A.5 (Strict supersolution).

For η>0\eta>0, we say that a family of locally bounded functions vv define a viscosity η\eta- strict supersolution of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) on [0,T)×𝒟[0,T)\times{\cal D} if it satisfies:

1. 1.

   For (t,x,𝔦,𝔳)∈[0,T)×𝒟(t,x,\mathfrak{i},\mathfrak{v})\in[0,T)\times{\cal D} and any smooth test function φ∈C1,2​([0,T]×𝒟)\varphi\in C^{1,2}([0,T]\times{\cal D}) such that (v∗−φ)(v\_{\*}-\varphi) attains a local minimum at (t,x,𝔦,𝔳)(t,x,\mathfrak{i},\mathfrak{v}) over the set [t,t+δ)×Bδ​(x)×⟦1,K⟧K×Bδ​(𝔳)⊂[0,T)×𝒟[t,t+\delta)\times B\_{\delta}(x)\times\llbracket 1,K\rrbracket^{K}\times B\_{\delta}(\mathfrak{v})\subset[0,T)\times{\cal D} for some δ>0\delta>0, we have

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | min{\displaystyle\min\bigg\{ | −∂φ∂t(t,x,𝔦,𝔳)−supa∈ℝHa(t,x,𝔦,𝔳,φ,∂φ∂x,∂2φ∂x2),(φ−ℳφ)(t,x,𝔦,𝔳)}>η,\displaystyle-\frac{\partial\varphi}{\partial t}(t,x,\mathfrak{i},\mathfrak{v})-\sup\_{a\in\mathbb{R}}H^{a}\Big(t,x,\mathfrak{i},\mathfrak{v},\varphi,\tfrac{\partial\varphi}{\partial x},\tfrac{\partial^{2}\varphi}{\partial x^{2}}\Big)\,,\,\big(\varphi-\mathcal{M}\varphi\big)(t,x,\mathfrak{i},\mathfrak{v})\bigg\}>\eta, |  |
2. 2.

   Additionally, for any (t,x,𝔦,𝔳)∈[0,T)×𝒟(t,x,\mathfrak{i},\mathfrak{v})\in[0,T)\times{\cal D} and any smooth test function φ∈C1,2​([0,T]×𝒟)\varphi\in C^{1,2}([0,T]\times{\cal D}) such that (v∗−φ)(v\_{\*}-\varphi) attains a local minimum at (t,x,𝔦,𝔳)(t,x,\mathfrak{i},\mathfrak{v}) over the set [t,t+δ)×Bδ​(x)×⟦1,K⟧K×Bδ​(𝔳)⊂[0,T)×𝒟[t,t+\delta)\times B\_{\delta}(x)\times\llbracket 1,K\rrbracket^{K}\times B\_{\delta}(\mathfrak{v})\subset[0,T)\times{\cal D} for some δ>0\delta>0, we have

   |  |  |  |
   | --- | --- | --- |
   |  | −∂φ∂t​(t,x,𝔦,𝔳)−supa∈ℝHa​(t,x,𝔦,𝔳,φ,∂φ∂x,∂2φ∂x2)>η.\begin{split}-\frac{\partial\varphi}{\partial t}(t,x,\mathfrak{i},\mathfrak{v})&-\sup\_{a\in\mathbb{R}}H^{a}\Big(t,x,\mathfrak{i},\mathfrak{v},\varphi,\tfrac{\partial\varphi}{\partial x},\tfrac{\partial^{2}\varphi}{\partial x^{2}}\Big)>\eta.\end{split} |  |

The first part of the definition covers the case ∑i=1N⟨𝔦,ei⟩<K\sum\_{i=1}^{N}\langle\mathfrak{i},e\_{i}\rangle<K and the second the case ∑i=1N⟨𝔦,ei⟩=K\sum\_{i=1}^{N}\langle\mathfrak{i},e\_{i}\rangle=K.

###### Lemma A.6.

Let v:[0,T]×𝒟→ℝv:[0,T]\times{\cal D}\to\mathbb{R} be a viscosity supersolution of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")). Define

|  |  |  |
| --- | --- | --- |
|  | m​(𝔦):=∑j=1N⟨𝔦,ej⟩∈{0,…,K}​and​Λ¯:=∑j=1Nℓj.m(\mathfrak{i}):=\sum\_{j=1}^{N}\langle\mathfrak{i},e\_{j}\rangle\in\{0,\dots,K\}~~\text{and}~~\bar{\Lambda}:=\sum\_{j=1}^{N}\ell\_{j}. |  |

Then, for any η>0\eta>0, there exists an η\eta-strict viscosity supersolution vηv^{\eta} of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) such that

|  |  |  |
| --- | --- | --- |
|  | vη​(t,x,𝔦,𝔳)=v​(t,x,𝔦,𝔳)+η​ϕ1​(t,𝔦)+η​ϕ2​(t,x),v^{\eta}(t,x,\mathfrak{i},\mathfrak{v})=v(t,x,\mathfrak{i},\mathfrak{v})+\eta\,\phi\_{1}(t,\mathfrak{i})+\eta\,\phi\_{2}(t,x), |  |

with (t,x,𝔦,𝔳)∈[0,T]×𝒟(t,x,\mathfrak{i},\mathfrak{v})\in[0,T]\times{\cal D} and

|  |  |  |
| --- | --- | --- |
|  | ϕ1​(t,𝔦):=(1+K​Λ¯)​(T−t)+(K−m​(𝔦))​and​ϕ2​(t,x):=12​eL​(T−t)​(1+‖x‖2),\phi\_{1}(t,\mathfrak{i}):=(1+K\bar{\Lambda})(T-t)+(K-m(\mathfrak{i}))~~\text{and}~~\phi\_{2}(t,x):=\frac{1}{2}e^{L(T-t)}\bigl(1+\|x\|^{2}\bigr), |  |

where L>0L>0. Additionally, there exist constants C1,C2>0C\_{1},C\_{2}>0, independent of η\eta, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t,x,𝔦,𝔳)+η​C1​‖x‖2≤vη​(t,x,𝔦,𝔳)≤v​(t,x,𝔦,𝔳)+η​C2​(1+‖x‖2).v(t,x,\mathfrak{i},\mathfrak{v})+\eta\,C\_{1}\|x\|^{2}\;\leq\;v^{\eta}(t,x,\mathfrak{i},\mathfrak{v})\;\leq\;v(t,x,\mathfrak{i},\mathfrak{v})+\eta\,C\_{2}(1+\|x\|^{2}). |  | (30) |

###### Proof.

Fix (t,x,𝔦,𝔳)∈[0,T]×𝒟(t,x,\mathfrak{i},\mathfrak{v})\in[0,T]\times{\cal D} and η>0\eta>0. As in the previous case, we detail the proof only when ∑i=1N⟨𝔦,ei⟩<K\sum\_{i=1}^{N}\langle\mathfrak{i},e\_{i}\rangle<K. Let φη∈C1,2​([0,T]×𝒟)\varphi^{\eta}\in C^{1,2}([0,T]\times{\cal D}) be such that
v∗η​(t,x,𝔦,𝔳)=φη​(t,x,𝔦,𝔳)v^{\eta}\_{\*}(t,x,\mathfrak{i},\mathfrak{v})=\varphi^{\eta}(t,x,\mathfrak{i},\mathfrak{v}) and
v∗η−φηv^{\eta}\_{\*}-\varphi^{\eta} attains a local maximum at this point. In other words, there exists r0>0r\_{0}>0 such that

|  |  |  |
| --- | --- | --- |
|  | v∗η​(t′,x′,𝔦,𝔳)≤φη​(t′,x′,𝔦,𝔳),∀(t′,x′)∈B¯r0​(t,x).v^{\eta}\_{\*}(t^{\prime},x^{\prime},\mathfrak{i},\mathfrak{v})\leq\varphi^{\eta}(t^{\prime},x^{\prime},\mathfrak{i},\mathfrak{v}),\quad\forall(t^{\prime},x^{\prime})\in\bar{B}\_{r\_{0}}(t,x). |  |

Let φ:[0,T]×𝒟→ℝ\varphi:[0,T]\times{\cal D}\to\mathbb{R} be defined as follows

|  |  |  |
| --- | --- | --- |
|  | φ​(t′,x′,𝔦,𝔳):=φη​(t′,x′,𝔦,𝔳)−η​ϕ1​(t′,𝔦)−η​ϕ2​(t′,x′),∀(t′,x′)∈B¯r0​(t,x).\varphi(t^{\prime},x^{\prime},\mathfrak{i},\mathfrak{v}):=\varphi^{\eta}(t^{\prime},x^{\prime},\mathfrak{i},\mathfrak{v})-\eta\,\phi\_{1}(t^{\prime},\mathfrak{i})-\eta\,\phi\_{2}(t^{\prime},x^{\prime}),\quad\forall(t^{\prime},x^{\prime})\in\bar{B}\_{r\_{0}}(t,x). |  |

Note that φη∈C1,2​([0,T]×𝒟)\varphi^{\eta}\in C^{1,2}([0,T]\times{\cal D}),
v∗​(t,x,𝔦,𝔳)=φ​(t,x,𝔦,𝔳)v^{\*}(t,x,\mathfrak{i},\mathfrak{v})=\varphi(t,x,\mathfrak{i},\mathfrak{v}) and
v∗−φv^{\*}-\varphi attains a local maximum at (t,x,𝔦,𝔳)(t,x,\mathfrak{i},\mathfrak{v}). For any admissible impulse (ξ,j)∈𝒰×⟦1,K⟧(\xi,j)\in{\cal U}\times{\llbracket 1,K\rrbracket} and (t′,x′)∈B¯r0​(t,x)(t^{\prime},x^{\prime})\in\bar{B}\_{r\_{0}}(t,x),

|  |  |  |
| --- | --- | --- |
|  | ϕ1​(t′,𝔦)−ϕ1​(t′,𝔦+ej)=(K−m​(𝔦))−(K−m​(𝔦)−1)=1,\phi\_{1}(t^{\prime},\mathfrak{i})-\phi\_{1}(t^{\prime},\mathfrak{i}+e\_{j})=(K-m(\mathfrak{i}))-(K-m(\mathfrak{i})-1)=1, |  |

while ϕ2\phi\_{2} is independent of (𝔦,𝔳)(\mathfrak{i},\mathfrak{v}). Hence,

|  |  |  |
| --- | --- | --- |
|  | φη​(t′,x′,𝔦,𝔳)−φη​(t′,x′,𝔦+ej,𝔳+ξ​ej)=φ​(t′,x′,𝔦,𝔳)−φ​(t′,x′,𝔦+ej,𝔳+ξ​ej)+η,∀(t′,x′)∈B¯r0​(t,x).\varphi^{\eta}(t^{\prime},x^{\prime},\mathfrak{i},\mathfrak{v})-\varphi^{\eta}(t^{\prime},x^{\prime},\mathfrak{i}+e\_{j},\mathfrak{v}+\xi e\_{j})=\varphi(t^{\prime},x^{\prime},\mathfrak{i},\mathfrak{v})-\varphi(t^{\prime},x^{\prime},\mathfrak{i}+e\_{j},\mathfrak{v}+\xi e\_{j})+\eta,\quad\forall(t^{\prime},x^{\prime})\in\bar{B}\_{r\_{0}}(t,x). |  |

Since vv is a viscosity supersolution, φ≥ℳ​φ\varphi\geq{\cal M}\varphi, and taking the supremum over
(ξ,j)(\xi,j) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | φη​(t′,x′,𝔦,𝔳)≥ℳ​φη​(t′,x′,𝔦,𝔳)+η,∀(t′,x′)∈B¯r0​(t,x).\varphi^{\eta}(t^{\prime},x^{\prime},\mathfrak{i},\mathfrak{v})\geq{\cal M}\varphi^{\eta}(t^{\prime},x^{\prime},\mathfrak{i},\mathfrak{v})+\eta,\quad\forall(t^{\prime},x^{\prime})\in\bar{B}\_{r\_{0}}(t,x). |  | (31) |

Additionally, we have that

|  |  |  |
| --- | --- | --- |
|  | −∂φ∂t​(t′,x′,𝔦,𝔳)−supa∈ℝHa​(t′,x′,𝔦,𝔳,φ,∂φ∂x,∂2φ∂x2)≥0,∀(t′,x′)∈B¯r0​(t,x).-\frac{\partial\varphi}{\partial t}(t^{\prime},x^{\prime},\mathfrak{i},\mathfrak{v})-\sup\_{a\in\mathbb{R}}H^{a}\Big(t^{\prime},x^{\prime},\mathfrak{i},\mathfrak{v},\varphi,\tfrac{\partial\varphi}{\partial x},\tfrac{\partial^{2}\varphi}{\partial x^{2}}\Big)\geq 0,\quad\forall(t^{\prime},x^{\prime})\in\bar{B}\_{r\_{0}}(t,x). |  |

Note that ℒa​ϕ1=0\mathcal{L}^{a}\phi\_{1}=0 for all a∈ℝa\in\mathbb{R} and ∂ϕ1∂t=−(1+K​Λ¯)\frac{\partial\phi\_{1}}{\partial t}=-(1+K\bar{\Lambda}), while the
execution operator satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝒥​ϕ1​(t′,x′,𝔦,𝔳)=∑j=1N1l{⟨𝔦,ej⟩>0}​ℓj​(⟨𝔦,ej⟩−c​(t′,x′,⟨𝔦,ei⟩,⟨𝔳,ei⟩))≤K​Λ¯,∀(t′,x′)∈B¯r0​(t,x).{\cal J}\phi\_{1}(t^{\prime},x^{\prime},\mathfrak{i},\mathfrak{v})=\sum\_{j=1}^{N}\mbox{1\hskip-2.5ptl}\_{\{\langle\mathfrak{i},e\_{j}\rangle>0\}}\ell\_{j}\Big(\langle\mathfrak{i},e\_{j}\rangle-c(t^{\prime},x^{\prime},\langle\mathfrak{i},e\_{i}\rangle,\langle\mathfrak{v},e\_{i}\rangle)\Big)\leq K\bar{\Lambda},\quad\forall(t^{\prime},x^{\prime})\in\bar{B}\_{r\_{0}}(t,x). |  |

Thus −∂ϕ1∂t−supa∈ℝℒa​ϕ1−𝒥​ϕ1≥1.-\frac{\partial\phi\_{1}}{\partial t}-\sup\_{a\in\mathbb{R}}\mathcal{L}^{a}\phi\_{1}-{\cal J}\phi\_{1}\geq 1. Second, using Assumptions [2.1](https://arxiv.org/html/2602.10798v1#S2.ThmAssumption1 "Assumption 2.1. ‣ 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays"), there exists C>0C>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supa∈ℝℒa​ϕ2+𝒥​ϕ2≤C​eL​(T−t′)​(1+‖x′‖+‖x′‖2)​and−∂ϕ2∂t=L2​eL​(T−t′)​(1+‖x′‖2),\sup\_{a\in\mathbb{R}}\mathcal{L}^{a}\phi\_{2}+{\cal J}\phi\_{2}\leq Ce^{L(T-t^{\prime})}(1+\|x^{\prime}\|+\|x^{\prime}\|^{2})~~\text{and}~~-\frac{\partial\phi\_{2}}{\partial t}=\frac{L}{2}e^{L(T-t^{\prime})}(1+\|x^{\prime}\|^{2}), |  | (32) |

for all (t′,x′)∈B¯r0​(t,x)(t^{\prime},x^{\prime})\in\bar{B}\_{r\_{0}}(t,x). Choosing LL large enough yields
−∂ϕ2∂t−supa∈ℝℒa​ϕ2−J​ϕ2≥0.-\frac{\partial\phi\_{2}}{\partial t}-\sup\_{a\in\mathbb{R}}\mathcal{L}^{a}\phi\_{2}-J\phi\_{2}\geq 0. Combining the two estimates shows that

|  |  |  |
| --- | --- | --- |
|  | −∂∂t​(ϕ1+ϕ2)−supa∈ℝℒa​(ϕ1+ϕ2)−𝒥​(ϕ1+ϕ2)≥1,-\frac{\partial}{\partial t}(\phi\_{1}+\phi\_{2})-\sup\_{a\in\mathbb{R}}\mathcal{{\cal L}}^{a}(\phi\_{1}+\phi\_{2})-{\cal J}(\phi\_{1}+\phi\_{2})\geq 1, |  |

which implies, after multiplication by η\eta, that

|  |  |  |
| --- | --- | --- |
|  | −∂φη∂t​(t′,x′,𝔦,𝔳)−supa∈ℝHa​(t′,x′,𝔦,𝔳,φη,∂φη∂x,∂2φη∂x2)≥η,∀(t′,x′)∈B¯r0​(t,x).-\frac{\partial\varphi^{\eta}}{\partial t}(t^{\prime},x^{\prime},\mathfrak{i},\mathfrak{v})-\sup\_{a\in\mathbb{R}}H^{a}\Big(t^{\prime},x^{\prime},\mathfrak{i},\mathfrak{v},\varphi^{\eta},\tfrac{\partial\varphi^{\eta}}{\partial x},\tfrac{\partial^{2}\varphi^{\eta}}{\partial x^{2}}\Big)\geq\eta,\quad\forall(t^{\prime},x^{\prime})\in\bar{B}\_{r\_{0}}(t,x). |  |

Hence, vηv^{\eta} is a strict supersolution of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")). The growth result follows directly from ([32](https://arxiv.org/html/2602.10798v1#A1.E32 "In Proof. ‣ A.3 Uniqueness and Continuity Result ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")).
∎

###### Theorem A.7.

If ww is a viscosity subsolution of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and
vv
is a viscosity supersolution of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")), such that

|  |  |  |
| --- | --- | --- |
|  | w∗​(T,x,𝔦,𝔳)≤v∗​(T,x,𝔦,𝔳),w^{\*}(T,x,\mathfrak{i},\mathfrak{v})\leq v\_{\*}(T,x,\mathfrak{i},\mathfrak{v}), |  |

for all (t,x,𝔦,𝔳)∈[0,T]×𝒟(t,x,\mathfrak{i},\mathfrak{v})\in[0,T]\times{\cal D}, then w≤vw\leq v on [0,T]×𝒟[0,T]\times{\cal D}.

###### Proof.

Let ww be a viscosity subsolution and vv a viscosity supersolution of
([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) in the sense of Definition [3.3](https://arxiv.org/html/2602.10798v1#S3.Thmtheorem3 "Definition 3.3 (Viscosity solution). ‣ 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays"), and assume that

|  |  |  |  |
| --- | --- | --- | --- |
|  | w∗​(T,x,𝔦,𝔳)≤v∗​(T,x,𝔦,𝔳),∀(x,𝔦,𝔳)∈𝒟.w^{\*}(T,x,\mathfrak{i},\mathfrak{v})\leq v\_{\*}(T,x,\mathfrak{i},\mathfrak{v}),\quad\forall(x,\mathfrak{i},\mathfrak{v})\in{\cal D}. |  | (33) |

Our goal is to show that ϱ:=sup(t,x,𝔦,𝔳)∈[0,T]×𝒟v∗η​(t,x,𝔦,𝔳)−w∗​(t,x,𝔦,𝔳)≤0\varrho:=\sup\_{(t,x,\mathfrak{i},\mathfrak{v})\in[0,T]\times{\cal D}}v^{\eta}\_{\*}(t,x,\mathfrak{i},\mathfrak{v})-w^{\*}(t,x,\mathfrak{i},\mathfrak{v})\leq 0, where v∗ηv^{\eta}\_{\*} has been introduced in Lemma [A.6](https://arxiv.org/html/2602.10798v1#A1.Thmtheorem6 "Lemma A.6. ‣ A.3 Uniqueness and Continuity Result ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays") for η>0\eta>0. Assume by contradiction that ϱ>0\varrho>0. Using the growth results in Lemma [2.3](https://arxiv.org/html/2602.10798v1#S2.Thmtheorem3 "Lemma 2.3 (Quadratic growth). ‣ 2 Problem Formulation ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays"), we get that

|  |  |  |
| --- | --- | --- |
|  | v∗η​(t,x,𝔦,𝔳)−w∗​(t,x,𝔦,𝔳)≤C1​(1+‖x‖)−C2​‖x‖2,∀(t,x,𝔦,𝔳)∈[0,T]×𝒟.v^{\eta}\_{\*}(t,x,\mathfrak{i},\mathfrak{v})-w^{\*}(t,x,\mathfrak{i},\mathfrak{v})\leq C\_{1}(1+\|x\|)-C\_{2}\|x\|^{2},\quad\forall(t,x,\mathfrak{i},\mathfrak{v})\in[0,T]\times{\cal D}. |  |

In particular, lim‖x‖→+∞v∗η​(t,x,𝔦,𝔳)−w∗​(t,x,𝔦,𝔳)=−∞\lim\_{\|x\|\to+\infty}v^{\eta}\_{\*}(t,x,\mathfrak{i},\mathfrak{v})-w^{\*}(t,x,\mathfrak{i},\mathfrak{v})=-\infty. Additionally, by ([33](https://arxiv.org/html/2602.10798v1#A1.E33 "In Proof. ‣ A.3 Uniqueness and Continuity Result ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")), the supremum is cannot be attained at terminal time TT. Therefore, the supremum of v∗η−w∗v^{\eta}\_{\*}-w^{\*} is attained an interior point (t0,x0,𝔦0,𝔳0)∈𝒪⊂[0,T)×Bx0​(X¯)×𝕀×𝕍⊂[0,T]×𝒟(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\in{\cal O}\subset[0,T)\times B\_{x\_{0}}(\bar{X})\times\mathbb{I}\times\mathbb{V}\subset[0,T]\times{\cal D}, with X¯>0\bar{X}>0. In other words, we have ϱ=v∗η​(t0,x0,𝔦0,𝔳0)−w∗​(t0,x0,𝔦0,𝔳0)\varrho=v^{\eta}\_{\*}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})-w^{\*}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0}). Let k≥1k\geq 1 and define, for all (t,x,x′,𝔦,𝔳)∈[0,T]×ℝd×𝒟(t,x,x^{\prime},\mathfrak{i},\mathfrak{v})\in[0,T]\times\mathbb{R}^{d}\times{\cal D},

|  |  |  |
| --- | --- | --- |
|  | Fk​(t,x,x′,𝔦,𝔳):=v∗η​(t,x,𝔦,𝔳)−w∗​(t,x′,𝔦,𝔳)−dk​(x,x′),F\_{k}(t,x,x^{\prime},\mathfrak{i},\mathfrak{v}):=v^{\eta}\_{\*}(t,x,\mathfrak{i},\mathfrak{v})-w^{\*}(t,x^{\prime},\mathfrak{i},\mathfrak{v})-d\_{k}(x,x^{\prime}), |  |

where dk​(x,x′):=k2​(‖x−x′‖2+‖x−x′‖4)d\_{k}(x,x^{\prime}):=\frac{k}{2}\big(\|x-x^{\prime}\|^{2}+\|x-x^{\prime}\|^{4}\big). Moreover, define

|  |  |  |
| --- | --- | --- |
|  | ϱk:=sup(t,x,𝔦,𝔳)∈[0,T]×ℝd×𝒟​Fk​(t,x,x′,𝔦,𝔳).\varrho\_{k}:=\underset{(t,x,\mathfrak{i},\mathfrak{v})\in[0,T]\times\mathbb{R}^{d}\times{\cal D}}{\sup}F\_{k}(t,x,x^{\prime},\mathfrak{i},\mathfrak{v}). |  |

Since FkF\_{k} is upper semi-continuous and coercive, its supremum is
attained, for all k∈ℕk\in\mathbb{N}, at some point (t^k,x^k,x^k′,𝔦^k,𝔳^k)∈[0,T]×ℝd×𝒟(\hat{t}\_{k},\hat{x}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})\in[0,T]\times\mathbb{R}^{d}\times{\cal D}. By means of the Bolzano–Weierstrass theorem, there exists a subsequence (t^nk,x^nk,x^nk′,𝔦^nk,𝔳^nk)k≥0\big(\hat{t}\_{n\_{k}},\hat{x}\_{n\_{k}},\hat{x}^{\prime}\_{n\_{k}},\hat{\mathfrak{i}}\_{n\_{k}},\hat{\mathfrak{v}}\_{n\_{k}}\big)\_{k\geq 0} that converges to a point
(t^0,x^0,x^0′,𝔦^0,𝔳^0)(\hat{t}\_{0},\hat{x}\_{0},\hat{x}^{\prime}\_{0},\hat{\mathfrak{i}}\_{0},\hat{\mathfrak{v}}\_{0}) as k→+∞k\to+\infty. In the following, we will continue using kk as an index instead of nkn\_{k} to avoid the proliferation of indices. For kk large
enough, we can then assume that t^k<T\hat{t}\_{k}<T. By definition of FkF\_{k}, we have the following inequality

|  |  |  |
| --- | --- | --- |
|  | Fk​(t^0,x^0,x^0,𝔦^0,𝔳^0)≤Fk​(t^k,x^k,x^k′,𝔦^k,𝔳^k).F\_{k}(\hat{t}\_{0},\hat{x}\_{0},\hat{x}\_{0},\hat{\mathfrak{i}}\_{0},\hat{\mathfrak{v}}\_{0})\leq F\_{k}(\hat{t}\_{k},\hat{x}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k}). |  |

In particular, we have

|  |  |  |
| --- | --- | --- |
|  | k2​(‖x^k−x^k′‖2+‖x^k−x^k′‖4)≤−v∗η​(t^0,x^0,𝔦^0,𝔳^0)+w∗​(t^0,x^0,𝔦^0,𝔳^0)+v∗η​(t^k,x^k,𝔦^k,𝔳^k)−w∗​(t^k,x^k′,𝔦^k,𝔳^k).\frac{k}{2}\big(\|\hat{x}\_{k}-\hat{x}^{\prime}\_{k}\|^{2}+\|\hat{x}\_{k}-\hat{x}^{\prime}\_{k}\|^{4}\big)\leq-v^{\eta}\_{\*}(\hat{t}\_{0},\hat{x}\_{0},\hat{\mathfrak{i}}\_{0},\hat{\mathfrak{v}}\_{0})+w^{\*}(\hat{t}\_{0},\hat{x}\_{0},\hat{\mathfrak{i}}\_{0},\hat{\mathfrak{v}}\_{0})+v^{\eta}\_{\*}(\hat{t}\_{k},\hat{x}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})-w^{\*}(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k}). |  |

As v∗ηv^{\eta}\_{\*} and w∗w^{\*} are continuous on the compact set 𝒪{\cal O}, there exists C>0C>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖x^k−x^k′‖2+‖x^k−x^k′‖4≤Ck.\|\hat{x}\_{k}-\hat{x}^{\prime}\_{k}\|^{2}+\|\hat{x}\_{k}-\hat{x}^{\prime}\_{k}\|^{4}\leq\frac{C}{k}. |  | (34) |

Letting kk go to +∞+\infty, we find x^0=x^0′\hat{x}\_{0}=\hat{x}^{\prime}\_{0}. Finally, we show that ϱk\varrho\_{k} tends to ϱ\varrho when kk goes to +∞+\infty. Note that

|  |  |  |
| --- | --- | --- |
|  | ϱ=v∗η​(t0,x0,𝔦0,𝔳0)−w∗​(t0,x0,𝔦0,𝔳0)=Hk​(t0,x0,x0,𝔦0,𝔳0)≤Hk​(t^k,x^k,x^k′,𝔦k,𝔳k).\varrho=v^{\eta}\_{\*}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})-w^{\*}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})=H\_{k}(t\_{0},x\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\leq H\_{k}(\hat{t}\_{k},\hat{x}\_{k},\hat{x}^{\prime}\_{k},\mathfrak{i}\_{k},\mathfrak{v}\_{k}). |  |

Therefore, ϱ≤ϱk\varrho\leq\varrho\_{k}. Moreover, we
have

|  |  |  |
| --- | --- | --- |
|  | ϱk=v∗η​(t^k,x^k,𝔦^k,𝔳^k)−w∗​(t^k,x^k′,𝔦^k,𝔳^k)−k2​‖x^k−x^k′‖4≤v∗η​(t^k,x^k,𝔦^k,𝔳^k)−w∗​(t^k,x^k′,𝔦^k,𝔳^k).\varrho\_{k}=v^{\eta}\_{\*}(\hat{t}\_{k},\hat{x}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})-w^{\*}(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})-\frac{k}{2}\|\hat{x}\_{k}-\hat{x}^{\prime}\_{k}\|^{4}\leq v^{\eta}\_{\*}(\hat{t}\_{k},\hat{x}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})-w^{\*}(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k}). |  |

Since v∗ηv^{\eta}\_{\*} and w∗w^{\*} are upper and lower semi-continuous on [0,T]×𝒟[0,T]\times{\cal D}, we get that

|  |  |  |
| --- | --- | --- |
|  | limk→+∞v∗η​(t^k,x^k,𝔦^k,𝔳^k)−w∗​(t^k,x^k′,𝔦^k,𝔳^k)=v∗η​(t^0,x^0′,𝔦^0,𝔳^0)−w∗​(t^0,x^0′,𝔦^0,𝔳^0)≤ϱ.\lim\_{k\rightarrow+\infty}v^{\eta}\_{\*}(\hat{t}\_{k},\hat{x}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})-w^{\*}(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})=v^{\eta}\_{\*}(\hat{t}\_{0},\hat{x}^{\prime}\_{0},\hat{\mathfrak{i}}\_{0},\hat{\mathfrak{v}}\_{0})-w^{\*}(\hat{t}\_{0},\hat{x}^{\prime}\_{0},\hat{\mathfrak{i}}\_{0},\hat{\mathfrak{v}}\_{0})\leq\varrho. |  |

We conclude that limk→+∞ϱk=ϱ\lim\_{k\rightarrow+\infty}\varrho\_{k}=\varrho and
limk→+∞‖x^k−x^k′‖4=0\lim\_{k\rightarrow+\infty}\|\hat{x}\_{k}-\hat{x}^{\prime}\_{k}\|^{4}=0. Moreover, we
have

|  |  |  |
| --- | --- | --- |
|  | v∗η​(t^0,x^0′,𝔦^0,𝔳^0)−w∗​(t^0,x^0′,𝔦^0,𝔳^0)=ϱ.v^{\eta}\_{\*}(\hat{t}\_{0},\hat{x}^{\prime}\_{0},\hat{\mathfrak{i}}\_{0},\hat{\mathfrak{v}}\_{0})-w^{\*}(\hat{t}\_{0},\hat{x}^{\prime}\_{0},\hat{\mathfrak{i}}\_{0},\hat{\mathfrak{v}}\_{0})=\varrho. |  |

Applying Theorem 3.23.2 from [[12](https://arxiv.org/html/2602.10798v1#bib.bib27 "User’s guide to viscosity solutions of second order partial differential equations")] at the point
(t^k,x^k,x^k′,𝔦^k,𝔳^k)(\hat{t}\_{k},\hat{x}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k}) yields the existence of two symmetric matrices Mk,Mk′∈ℝd×dM\_{k},M^{\prime}\_{k}\in\mathbb{R}^{d\times d} in the superjet set J2,+J^{2,+} of v∗ηv^{\eta}\_{\*} and the subjet set J2,−J^{2,-} of w∗w^{\*} such that

|  |  |  |
| --- | --- | --- |
|  | (∂dk∂x,Mk)∈J2,+​v∗η​(t^k,x^k,𝔦^k,𝔳^k)​and​(−∂dk∂x′,Mk′)∈J2,−​w∗​(t^k,x^k′,𝔦^k,𝔳^k)\Big(\frac{\partial d\_{k}}{\partial x},M\_{k}\Big)\in J^{2,+}v^{\eta}\_{\*}(\hat{t}\_{k},\hat{x}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})~~\textrm{and}~~\Big(-\frac{\partial d\_{k}}{\partial x^{\prime}},M^{\prime}\_{k}\Big)\in J^{2,-}w^{\*}(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k}) |  |

and the following inequality holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Mk00−Mk′)≤A+1k​A2, with ​A=D2​dk​(x^k,x^k′)=(k​I−k​I−k​Ik​I),\begin{split}\left(\begin{array}[]{cc}M\_{k}&0\\ 0&-M^{\prime}\_{k}\\ \end{array}\right)\leq A+\frac{1}{k}A^{2},\textrm{ with }A=D^{2}d\_{k}(\hat{x}\_{k},\hat{x}^{\prime}\_{k})=\begin{pmatrix}kI&-kI\\ -kI&kI\end{pmatrix}\end{split}, |  | (35) |

where II is the identity matrix. Using the relationship between superjets along with the supersolution properties of v∗ηv^{\eta}\_{\*} established in Lemma [A.6](https://arxiv.org/html/2602.10798v1#A1.Thmtheorem6 "Lemma A.6. ‣ A.3 Uniqueness and Continuity Result ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays"), we deduce from Ishii’s Lemma that

|  |  |  |  |
| --- | --- | --- | --- |
|  | η≤min⁡{−supa∈ℝHa​(t^k,x^k,𝔦^k,𝔳^k,v∗η,∂dk∂x,Mk),(v∗η−ℳ​v∗η)​(t^k,x^k,𝔦^k,𝔳^k)},\eta\leq\min\Big\{-\sup\_{a\in\mathbb{R}}H^{a}\Big(\hat{t}\_{k},\hat{x}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k},v^{\eta}\_{\*},\tfrac{\partial d\_{k}}{\partial x},M\_{k}\Big),\;\big(v^{\eta}\_{\*}-\mathcal{M}v^{\eta}\_{\*}\big)(\hat{t}\_{k},\hat{x}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})\Big\}, |  | (36) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≥min⁡{−supa∈ℝHa​(t^k,x^k′,𝔦^k,𝔳^k,w∗,−∂dk∂x′,Mk′),(w∗−ℳ​w∗)​(t^k,x^k′,𝔦^k,𝔳^k)},0\geq\min\Big\{-\sup\_{a\in\mathbb{R}}H^{a}\Big(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k},w^{\*},-\tfrac{\partial d\_{k}}{\partial x^{\prime}},M^{\prime}\_{k}\Big),\;\big(w^{\*}-\mathcal{M}w^{\*}\big)(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})\Big\}, |  | (37) |

###### Remark A.8.

We use the local definition of viscosity sub- and supersolutions, where test
functions touch the candidate solution locally.
Under the present assumptions, this notion is equivalent to the global
definition for HJB-QVI inequalities. We refer to [[24](https://arxiv.org/html/2602.10798v1#bib.bib28 "Existence and uniqueness of viscosity solutions for qvi associated with impulse control of jump-diffusions")] for a detailed discussion.

It follows from the supersolution property that

|  |  |  |  |
| --- | --- | --- | --- |
|  | v∗η​(t0,x0,𝔦0,𝔳0)≥ℳ​v∗η​(t0,x0,𝔦0,𝔳0).v^{\eta}\_{\*}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0})\geq{\cal M}v^{\eta}\_{\*}(t\_{0},x\_{0},\mathfrak{i}\_{0},\mathfrak{v}\_{0}). |  | (38) |

#### Case 1:

w∗​(t^k,x^k′,𝔦^k,𝔳^k)≤ℳ​w∗​(t^k,x^k′,𝔦^k,𝔳^k)w^{\*}(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})\leq{\cal M}w^{\*}(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k}). Then

|  |  |  |
| --- | --- | --- |
|  | Δ:=w∗​(t^k,x^k′,𝔦^k,𝔳^k)−v∗η​(t^k,x^k,𝔦^k,𝔳^k)≤ℳ​w∗​(t^k,x^k′,𝔦^k,𝔳^k)−ℳ​v∗η​(t^k,x^k,𝔦^k,𝔳^k).\Delta:=w^{\*}(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})-v^{\eta}\_{\*}(\hat{t}\_{k},\hat{x}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})\leq{\cal M}w^{\*}(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})-{\cal M}v^{\eta}\_{\*}(\hat{t}\_{k},\hat{x}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k}). |  |

By the definition of ℳ{\cal M}, for ε>0\varepsilon>0, there exists (ξ∗,j∗)∈𝒰×⟦1,K⟧(\xi^{\ast},j^{\ast})\in{\cal U}\times\llbracket 1,K\rrbracket
such that

|  |  |  |
| --- | --- | --- |
|  | ℳ​w∗​(t^k,x^k′,𝔦^k,𝔳^k)≤w∗​(t^k,x^k′,𝔦^k+ej∗,𝔳^k+ξ∗​ej∗)−ε.{\cal M}w^{\*}(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})\leq w^{\*}(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k}+e\_{j^{\ast}},\hat{\mathfrak{v}}\_{k}+\xi^{\ast}e\_{j^{\ast}})-\varepsilon. |  |

Additionally, we have that

|  |  |  |
| --- | --- | --- |
|  | ℳ​v∗η​(t^k,x^k,𝔦^k,𝔳^k)≥v∗η​(t^k,x^k,𝔦^k+ej∗,𝔳^k+ξ∗​ej∗){\cal M}v^{\eta}\_{\*}(\hat{t}\_{k},\hat{x}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})\geq v^{\eta}\_{\*}(\hat{t}\_{k},\hat{x}\_{k},\hat{\mathfrak{i}}\_{k}+e\_{j^{\ast}},\hat{\mathfrak{v}}\_{k}+\xi^{\ast}e\_{j^{\ast}}) |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | Δ≤w∗​(t^k,x^k′,𝔦^k+ej∗,𝔳k+ξ∗​ej∗)−v∗η​(t^k,x^k,𝔦^k+ej∗,𝔳^k+ξ∗​ej∗)−ε≤Δ−ε,\Delta\leq w^{\*}(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k}+e\_{j^{\ast}},\mathfrak{v}\_{k}+\xi^{\ast}e\_{j^{\ast}})-v^{\eta}\_{\*}(\hat{t}\_{k},\hat{x}\_{k},\hat{\mathfrak{i}}\_{k}+e\_{j^{\ast}},\hat{\mathfrak{v}}\_{k}+\xi^{\ast}e\_{j^{\ast}})-\varepsilon\leq\Delta-\varepsilon, |  |

which leads to a contradiction.

#### Case 2:

w∗​(t^k,x^k′,𝔦^k,𝔳^k)>ℳ​w∗​(t^k,x^k′,𝔦^k,𝔳^k)w^{\*}(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k})>{\cal M}w^{\*}(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k}). It follows from inequalities ([36](https://arxiv.org/html/2602.10798v1#A1.E36 "In Proof. ‣ A.3 Uniqueness and Continuity Result ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([37](https://arxiv.org/html/2602.10798v1#A1.E37 "In Proof. ‣ A.3 Uniqueness and Continuity Result ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | η≤−supa∈ℝHa​(t^k,x^k,𝔦^k,𝔳^k,v∗η,∂dk∂x,Mk),and​0≥−supa∈ℝHa​(t^k,x^k′,𝔦^k,𝔳^k,w∗,−∂dk∂x′,Mk′).\eta\leq-\sup\_{a\in\mathbb{R}}H^{a}\Big(\hat{t}\_{k},\hat{x}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k},v^{\eta}\_{\*},\tfrac{\partial d\_{k}}{\partial x},M\_{k}\Big),~~\text{and}~~0\geq-\sup\_{a\in\mathbb{R}}H^{a}\Big(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k},w^{\*},-\tfrac{\partial d\_{k}}{\partial x^{\prime}},M^{\prime}\_{k}\Big). |  | (39) |

Fix R>0R>0 and introduce the truncated Hamiltonian

|  |  |  |
| --- | --- | --- |
|  | HR:=sup|a|≤RHa.H\_{R}:=\sup\_{|a|\leq R}H^{a}. |  |

By replacing supa∈ℝHa\sup\_{a\in\mathbb{R}}H^{a} with HRH\_{R} in the above inequalities, the supremum is taken
over a compact set and the comparison argument applies similarly. By definition of the supremum and using ([39](https://arxiv.org/html/2602.10798v1#A1.E39 "In Case 2: ‣ A.3 Uniqueness and Continuity Result ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")), there exists akϵ:=aϵ​(t^k,x^k′,𝔦^k,𝔳^k,w∗,−∂dk∂x′,Mk′)∈[−R,R]a^{\epsilon}\_{k}:=a^{\epsilon}\Big(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k},w^{\*},-\tfrac{\partial d\_{k}}{\partial x^{\prime}},M^{\prime}\_{k}\Big)\in[-R,R] for each k∈ℕk\in\mathbb{N} such that

|  |  |  |
| --- | --- | --- |
|  | η≤−Hakϵ​(t^k,x^k,𝔦^k,𝔳^k,v∗η,∂dk∂x,Mk)+Hakϵ​(t^k,x^k′,𝔦^k,𝔳^k,w∗,−∂dk∂x′,Mk′)−ϵ.\begin{split}\eta&\leq-H^{a^{\epsilon}\_{k}}\Big(\hat{t}\_{k},\hat{x}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k},v^{\eta}\_{\*},\tfrac{\partial d\_{k}}{\partial x},M\_{k}\Big)+H^{a^{\epsilon}\_{k}}\Big(\hat{t}\_{k},\hat{x}^{\prime}\_{k},\hat{\mathfrak{i}}\_{k},\hat{\mathfrak{v}}\_{k},w^{\*},-\tfrac{\partial d\_{k}}{\partial x^{\prime}},M^{\prime}\_{k}\Big)-\epsilon.\end{split} |  |

Moreover, since the above inequality remains valid when the supremum in
the Hamiltonian is restricted to a sufficiently large compact set,
the sequence (akϵ)k∈ℕ(a\_{k}^{\epsilon})\_{k\in\mathbb{N}} may be chosen bounded. By the Bolzano-Weierstrass theorem, there exists a subsequence,
still denoted (akϵ)k∈ℕ(a\_{k}^{\epsilon})\_{k\in\mathbb{N}}, converging to some a0ϵ∈ℝa^{\epsilon}\_{0}\in\mathbb{R}.
Sending k→+∞k\to+\infty is therefore justified for fixed RR. Letting R→+∞R\to+\infty and using the monotone convergence
HR​→R→+∞​HH\_{R}\underset{R\to+\infty}{\to}H (see [[14](https://arxiv.org/html/2602.10798v1#bib.bib21 "Controlled markov processes and viscosity solutions"), Chapter III]),
we recover the inequality for the original Hamiltonian. Sending kk to +∞+\infty, we get by continuity of bb and σ\sigma and inequality ([35](https://arxiv.org/html/2602.10798v1#A1.E35 "In Proof. ‣ A.3 Uniqueness and Continuity Result ‣ Appendix A Proofs of the Results in Section 3 ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) that

|  |  |  |
| --- | --- | --- |
|  | η≤limk→+∞12​⟨(Mk00−Mk′)​(σ​(t^k,x^k,akϵ),σ​(t^k,x^k′,akϵ))⊤,(σ​(t^k,x^k,akϵ),σ​(t^k,x^k′,akϵ))⟩+𝒥​(w∗−v∗η)​(t^0,x^0,𝔦^0,𝔳^0)−ϵ≤limk→+∞12​⟨(A+1k​A2)​(σ​(t^k,x^k,akϵ),σ​(t^k,x^k′,akϵ))⊤,(σ​(t^k,x^k,akϵ),σ​(t^k,x^k′,akϵ))⟩=limk→+∞32​k​(σ​(t^k,x^k,akϵ)−σ​(t^k,x^k′,akϵ))⊤​(σ​(t^k,x^k,akϵ)−σ​(t^k,x^k′,akϵ))≤32​C.\begin{split}\eta&\leq\lim\_{k\to+\infty}\frac{1}{2}\Big\langle\left(\begin{array}[]{cc}M\_{k}&0\\ 0&-M^{\prime}\_{k}\end{array}\right)\big(\sigma(\hat{t}\_{k},\hat{x}\_{k},a^{\epsilon}\_{k}),\sigma(\hat{t}\_{k},\hat{x}^{\prime}\_{k},a^{\epsilon}\_{k})\big)^{\top},\big(\sigma(\hat{t}\_{k},\hat{x}\_{k},a^{\epsilon}\_{k}),\sigma(\hat{t}\_{k},\hat{x}^{\prime}\_{k},a^{\epsilon}\_{k})\big)\Big\rangle\\ &\qquad+\mathcal{J}(w^{\*}-v^{\eta}\_{\*})(\hat{t}\_{0},\hat{x}\_{0},\hat{\mathfrak{i}}\_{0},\hat{\mathfrak{v}}\_{0})-\epsilon\\ &\leq\lim\_{k\to+\infty}\frac{1}{2}\Big\langle\big(A+\frac{1}{k}A^{2}\big)\big(\sigma(\hat{t}\_{k},\hat{x}\_{k},a^{\epsilon}\_{k}),\sigma(\hat{t}\_{k},\hat{x}^{\prime}\_{k},a^{\epsilon}\_{k})\big)^{\top},\big(\sigma(\hat{t}\_{k},\hat{x}\_{k},a^{\epsilon}\_{k}),\sigma(\hat{t}\_{k},\hat{x}^{\prime}\_{k},a^{\epsilon}\_{k})\big)\Big\rangle\\ &=\lim\_{k\to+\infty}\frac{3}{2}k\big(\sigma(\hat{t}\_{k},\hat{x}\_{k},a^{\epsilon}\_{k})-\sigma(\hat{t}\_{k},\hat{x}^{\prime}\_{k},a^{\epsilon}\_{k})\big)^{\top}\big(\sigma(\hat{t}\_{k},\hat{x}\_{k},a^{\epsilon}\_{k})-\sigma(\hat{t}\_{k},\hat{x}^{\prime}\_{k},a^{\epsilon}\_{k})\big)\\ &\leq\frac{3}{2}C.\end{split} |  |

This leads to a contradiction since η\eta is arbitrary.
∎

###### Lemma A.9.

The viscosity solution of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) is unique and continuous on [0,T]×𝒟[0,T]\times{\cal D}.

###### Proof.

Let uu and u~\tilde{u} be viscosity solutions of ([11](https://arxiv.org/html/2602.10798v1#S3.E11 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) and ([14](https://arxiv.org/html/2602.10798v1#S3.E14 "In 3.2 PDE Characterization and Comparison Principle ‣ 3 Viscosity Characterization of the Value Function ‣ Trading in CEXs and DEXs with Priority Fees and Stochastic Delays")) with the same terminal condition. The comparison principle applied to (u,u~)(u,\tilde{u}) and (u~,u)(\tilde{u},u) yields u=u~u=\tilde{u}, so the solution is unique. Let uu be the unique solution. The envelopes u∗u^{\ast} and u∗u\_{\ast} are respectively a subsolution and a supersolution with identical terminal data. Comparison gives u∗≤u∗u^{\ast}\leq u\_{\ast}, while u∗≤u∗u\_{\ast}\leq u^{\ast} holds. Hence u∗=u∗=uu^{\ast}=u\_{\ast}=u and uu is continuous on [0,T]×𝒟[0,T]\times{\cal D}.
∎