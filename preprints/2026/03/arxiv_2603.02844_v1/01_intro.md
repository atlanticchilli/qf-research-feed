---
authors:
- Carlos Escudero
- Felipe Lara
- Miguel Sama
doc_id: arxiv:2603.02844v1
family_id: arxiv:2603.02844
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Optimal Routing across Constant Function Market Makers with Gas Fees
url_abs: http://arxiv.org/abs/2603.02844v1
url_html: https://arxiv.org/html/2603.02844v1
venue: arXiv q-fin
version: 1
year: 2026
---


C. Escudero
Departamento de Matemáticas Fundamentales,
Universidad Nacional de Educación a Distancia, Madrid, Spain.
E-mail: cescudero@mat.uned.es, ORCID-ID: 0000-0001-9144-9097.
  
F. Lara
Instituto de Alta Investigación (IAI), Universidad
de Tarapacá, Arica, Chile. E-mail: felipelaraobreque@gmail.com;
flarao@academicos.uta.cl. Web: www.felipelara.cl, ORCID-ID: 0000-0002-9965-0921.
  
M. Sama
Departamento de Matemática Aplicada I,
Universidad Nacional de Educación a Distancia, Madrid, Spain.
E-mail: msama@ind.uned.es.

###### \vskip-34.14322pt

Abstract.
We study the optimal routing problem in decentralized exchanges built on Constant Function Market Makers when trades can be split across multiple heterogeneous pools and execution incurs fixed on-chain costs (gas fees). While prior routing formulations typically abstract from fixed activation costs, real on-chain execution presents non-negligible gas fees. They also become convex under concavity/convexity assumptions on the invariant functions. We propose a general optimization framework that allows differentiable invariant functions beyond global convexity and incorporates fixed gas fees through a mixed-integer model that induces activation thresholds. Subsequently, we introduce a relaxed formulation of this model, whereby we deduce necessary optimality conditions, obtaining an explicit Karush-Kuhn-Tucker system that links prices, fees, and activation. We further establish sufficient optimality conditions using tools from generalized convexity (pseudoconcavity/pseudoconvexity and quasilinearity), yielding a verifiable optimality characterization without requiring convex trade functions. Finally, we relate the relaxed solution to the original mixed-integer model by providing explicit approximation bounds that quantify the utility gap induced by relaxation. Our results extend the mathematical theory for routing by offering no-trade conditions in fragmented on-chain markets in the presence of gas fees.

*Keywords*: Decentralized Finance; Constant Function Market Makers; Optimal routing;
Gas fees; Karush-Kuhn-Tucker conditions; Generalized convexity.

## 1 Introduction

Decentralized Finance (DeFi) has emerged as a new paradigm for the provision of
financial services through permissionless and transparent blockchain-based
protocols [[23](#bib.bib23), [31](#bib.bib31)]. A core building block of DeFi markets are Automated Market Makers
(AMMs), which replace the traditional order book mechanism by on-chain
liquidity pools governed by deterministic pricing rules. Among the different
classes of AMMs, Constant Function Market Makers (CFMMs) have attracted
particular attention due to their mathematical tractability and economic
relevance. In a CFMM, the state of a liquidity pool is characterized by a vector
of reserves whose evolution is constrained by an invariant function, and asset
prices arise endogenously from the gradient of this invariant.

In mathematical terms, a CFMM maintains a set of reserves (R1,…,Rn)(R^{1},\ldots,R^{n}) of nn different assets in such a way that it keeps invariant a given function

|  |  |  |
| --- | --- | --- |
|  | φ​(R1,…,Rn)=k,\varphi(R^{1},\ldots,R^{n})=k, |  |

henceforth denoted as *trade function*, which is usually assumed to be continuously differentiable and to possess a well-defined convexity. The constant k>0k>0 is given by the initialization of the CFMM. Examples include the constant-product formula φ​(x,y)=x​y\varphi(x,y)=xy used in Uniswap v2 [[2](#bib.bib2)] (for newer versions of Uniswap see [[1](#bib.bib1), [3](#bib.bib3), [4](#bib.bib4)]) and the constant-sum form φ​(x,y)=x+y\varphi(x,y)=x+y, which arises
as a theoretical benchmark for stablecoin exchanges [[20](#bib.bib20)]. This structure fixes how exchanges between a user and the CFMM are performed. In particular, it permits an autonomous relative valuation of assets, giving an implicit pricing rule that is derived from the gradient ∇φ​(R1,…,Rn)\nabla\varphi(R^{1},\ldots,R^{n}), which determines marginal exchange rates. Hence the assumption of differentiability. Other examples of CFMMs include Balancer [[28](#bib.bib28)] and Curve [[20](#bib.bib20)].

The mathematical foundations of CFMMs have been rigorously developed in recent
years. In particular, Angeris, Chitra, and coworkers [[6](#bib.bib6), [7](#bib.bib7), [9](#bib.bib9)]
formalized CFMM trading as a convex optimization problem under suitable
regularity and convexity assumptions on the invariant function, providing
fundamental insights into pricing, arbitrage, and optimal trade execution.
Subsequent works extended this framework to multi-asset pools, routing across
multiple markets, and algorithmic execution strategies
[[8](#bib.bib8), [16](#bib.bib16), [19](#bib.bib19)].

In realistic DeFi ecosystems, as these last three references outline, trading does not occur within a single
liquidity pool. Instead, traders face a fragmented market composed of
heterogeneous CFMMs, each characterized by its own invariant function, reserve
composition, and fee structure. Optimal execution may therefore require splitting a trade across several pools, giving rise to the *optimal routing problem*. These previous formulations are based on convex optimization
techniques by imposing global convexity or concavity assumptions on
the invariant functions [[5](#bib.bib5), [9](#bib.bib9)]. These assumptions restrict the admissible design
space of CFMMs and are not always economically or technologically justified. However, most existing theoretical results rely on convexity hypotheses because they guarantee global optimality [[25](#bib.bib25)]. This limits the applicability of the
analysis to a narrower class of invariant functions, but is something that can be circumvented by means of nonconvex optimization methods [[22](#bib.bib22)].

A second structural feature of decentralized markets that challenges standard models is the presence of fixed execution costs. On-chain trades incur
*gas fees*, which must be paid whenever a transaction interacts with a
liquidity pool, independently of the traded volume. These costs fundamentally alter optimal routing decisions. From a financial perspective, gas fees expand no-trade
regions, suppress arbitrage opportunities, and interact with liquidity
fragmentation in non-trivial ways. Related phenomena have been discussed in the literature, including miner extractable value (MEV) and other inefficiencies in DeFi markets
[[13](#bib.bib13), [14](#bib.bib14), [15](#bib.bib15)]. However, despite their importance, fixed execution costs are often either neglected or
handled heuristically [[18](#bib.bib18)], and their interaction with the
underlying mathematical structure of CFMMs remains insufficiently understood to the best of our knowledge.

The aim of this paper is to address these limitations by developing a general
optimization-theoretic framework for optimal routing across multiple
heterogeneous CFMMs that (i) allows differentiable invariant functions beyond
global convexity assumptions, and (ii) explicitly incorporates gas fees through
market activation variables and capacity constraints.

### Our contribution

Our contributions in this work can be summarized as follows.

* •

  We formulate the optimal routing problem across multiple CFMMs in the presence of fixed gas fees and without convexity assumptions. This is done at the price of introducing market activation variables and
  bounded trade constraints. The resulting model captures some essential features of on-chain execution while remaining amenable to rigorous mathematical analysis through the introduction of a relaxation approximation.
* •

  For the relaxed routing problem, we derive *necessary optimality
  conditions* in the form of a Karush-Kuhn-Tucker (KKT) system under a
  Kurcyusz-Robinson-Zowe-type constraint qualification adapted to the structure
  of CFMM trading constraints. This characterization explicitly links marginal
  utilities, pool prices, fees, and activations.
* •

  Using tools from generalized convexity, we establish *sufficient
  optimality conditions* without assuming global convexity of the invariant functions. In particular, under pseudoconcavity of the utilities and
  quasilinearity of the trade functions, the KKT conditions are shown to be both
  necessary and sufficient for global optimality.
* •

  We analyze the relationship between the relaxed routing problem and the
  original mixed-integer formulation with fixed activation costs. Explicit
  approximation bounds are derived, quantifying the utility loss induced by the
  relaxation and providing a rigorous interpretation of relaxed routing solutions.

Overall, our results extend the mathematical theory of CFMM routing beyond convex models and provide a mathematical framework for understanding the impact of gas fees on optimal trading and no-trade conditions in fragmented decentralized markets.

## 2 Preliminaries

We denote ℝ+:=[0,+∞[\mathbb{R}\_{+}:=[0,+\infty[ and ℝ++:=]0,+∞[\mathbb{R}\_{++}:=\,]0,+\infty[, thus ℝ+n:=(ℝ+)n\mathbb{R}^{n}\_{+}:=(\mathbb{R}\_{+})^{n} and ℝ++n:=(ℝ++)n\mathbb{R}^{n}\_{++}:=(\mathbb{R}\_{++})^{n}, respectively. We use the usual notations ≥\geq componentwise (see [[21](#bib.bib21)]), that is,

|  |  |  |
| --- | --- | --- |
|  | x≥y⟺xi≥yi,\displaystyle~~x\geq y~\Longleftrightarrow~x\_{i}\geq y\_{i}, |  |
|  |  |  |
| --- | --- | --- |
|  | x⪈y⟺xi≥yi,x≠y,\displaystyle~~x\gneq y~\Longleftrightarrow~x\_{i}\geq y\_{i},\,x\neq y, |  |
|  |  |  |
| --- | --- | --- |
|  | x>y⟺xi>yi,\displaystyle~~x>y~\Longleftrightarrow~x\_{i}>y\_{i}, |  |

for every i=1,…,ni=1,\ldots,n.

Given any extended-valued function h:ℝn→ℝ¯:=ℝ∪{±∞}h:\mathbb{R}^{n}\rightarrow\overline{\mathbb{R}}:=\mathbb{R}\cup\{\pm\infty\}, it is indicated by epi​h:={(x,t)∈ℝn×ℝ:h​(x)≤t}{\rm epi}\,h:=\{(x,t)\in\mathbb{R}^{n}\times\mathbb{R}:h(x)\leq t\} the epigraph of hh, by Sλ​(h):={x∈ℝn:h​(x)≤λ}S\_{\lambda}(h):=\{x\in\mathbb{R}^{n}:h(x)\leq\lambda\} the sublevel set of hh at the height λ∈ℝ\lambda\in\mathbb{R}, by Wλ​(h):={x∈ℝn:h​(x)≥λ}W\_{\lambda}(h):=\{x\in\mathbb{R}^{n}:h(x)\geq\lambda\} the upper level set of hh at the height λ∈ℝ\lambda\in\mathbb{R}, and by argminℝn​h{\rm argmin}\_{\mathbb{R}^{n}}h the set
of all minimal points of hh on ℝn\mathbb{R}^{n}.

A function hh with convex domain is said to be

* (a)(a)

  convex if, given any x,y∈dom​hx,y\in\mathrm{dom}\,h, then

  |  |  |  |
  | --- | --- | --- |
  |  | h​(λ​x+(1−λ)​y)≤λ​h​(x)+(1−λ)​h​(y),∀λ∈[0,1],h(\lambda x+(1-\lambda)y)\leq\lambda h(x)+(1-\lambda)h(y),~\forall~\lambda\in[0,1], |  |
* (b)(b)

  quasiconvex if, given any x,y∈dom​hx,y\in\mathrm{dom}\,h, then

  |  |  |  |
  | --- | --- | --- |
  |  | h​(λ​x+(1−λ)​y)≤max⁡{h​(x),h​(y)},∀λ∈[0,1],h(\lambda x+(1-\lambda)y)\leq\max\{h(x),h(y)\},~\forall~\lambda\in[0,1], |  |

Every convex function is quasiconvex, but the reverse statement does not hold as the function h​(x)=x3h(x)=x^{3} shows. Recall that

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​is​convex\displaystyle h~\mathrm{is~convex} | ⟺epi​h​is​a​convex​set;\displaystyle\Longleftrightarrow\,\mathrm{epi}\,h~\mathrm{is~a~convex~set;} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | h​is​quasiconvex\displaystyle h~\mathrm{is~quasiconvex} | ⟺Sλ​(h)​is​a​convex​set​for​all​λ∈ℝ.\displaystyle\Longleftrightarrow\,S\_{\lambda}(h)~\mathrm{is~a~convex~set~for~all~}\lambda\in\mathbb{R}. |  |

Quasiconvex functions appear in many applications from different fields as, for instance, in Economics and Financial Theory, especially in consumer preference theory (see [[17](#bib.bib17), [29](#bib.bib29)]), since quasiconcavity is the mathematical formulation of the natural assumption of a tendency to diversification on the consumers.

It is said that hh is quasilinear if hh is quasiconvex and −h-h is quasiconvex.
As a consequence, its sublevel set Sλ​(h)S\_{\lambda}(h) and its upper level
sets Wλ​(h)W\_{\lambda}(h) are convex for all λ∈ℝ\lambda\in\mathbb{R} (see
[[12](#bib.bib12), Theorem 3.3.1]).

Let K⊆ℝnK\subseteq\mathbb{R}^{n} be a convex set and h:K→ℝh:K\rightarrow\mathbb{R} be a differentiable function. Then, the following assertions hold:

* (i)(i)

  hh is quasiconvex if and only if for every x,y∈Kx,y\in K, we have (see [[10](#bib.bib10)] and [[11](#bib.bib11), Theorem 3.11]) that

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | h​(x)≤h​(y)⟹⟨∇h​(y),x−y⟩≤0;h(x)\leq h(y)~\Longrightarrow~\langle\nabla h(y),x-y\rangle\leq 0; |  | (2.1) |
* (i​i)(ii)

  hh is quasilinear if and only if for every x,y∈Kx,y\in K, we have (see [[12](#bib.bib12), Theorem 3.3.6])

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | h​(x)=h​(y)⟹⟨∇h​(y),x−y⟩=0.h(x)=h(y)~\Longrightarrow~\langle\nabla h(y),x-y\rangle=0. |  | (2.2) |

Let h:ℝn→ℝh:\mathbb{R}^{n}\rightarrow\mathbb{R} be a differentiable function. Then hh is said to be pseudoconvex (see [[27](#bib.bib27)]) if

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨∇h​(x),y−x⟩≥0⟹h​(y)≥h​(x).\langle\nabla h(x),y-x\rangle\geq 0~\Longrightarrow~h(y)\geq h(x). |  | (2.3) |

A function hh is pseudoconcave if −h-h is pseudoconvex. Furthermore, if hh is pseudoconvex, then every local minimum is global minimum [[12](#bib.bib12), Theorem 3.2.5], a property that quasiconvex functions do not have.

For a further study on generalized convexity, we refer to [[10](#bib.bib10), [11](#bib.bib11), [12](#bib.bib12), [24](#bib.bib24), [27](#bib.bib27), [30](#bib.bib30)] among others.

## 3 Optimal Routing with Gas Fee

Our basic framework is that of [[8](#bib.bib8)], which we summarize in the following. We consider a system of m∈ℕm\in\mathbb{N}, m≥1m\geq 1, number of CFMMs, which trades multiple tokens (or crypto-assets) from an universe of n∈ℕn\in\mathbb{N}, n≥2n\geq 2, tokens. Let nn be the specific number of tokens that we could trade. Each market ii has ni∈ℕn\_{i}\in\mathbb{N} tokens with ni∈{2,…,n}n\_{i}\in\{2,\ldots,n\} for each i∈{1,…,m}i\in\{1,\ldots,m\}, and each market ii is associated with a connectivity matrix Ai∈ℝn×niA^{i}\in\mathbb{R}^{n\times n\_{i}}, with i∈{1,…,m}i\in\{1,\ldots,m\}, which relates the global index of a token to its local index. Specifically, Aj​ki=1A\_{jk}^{i}=1 when the global token jj corresponds to the local index k∈{1,…,ni}k\in\{1,\ldots,n\_{i}\} in each CFMM ii.

Each CFMM ii has a quantity of reserves Ri∈ℝ+niR^{i}\in\mathbb{R}\_{+}^{n\_{i}} and requires a relative tax payment of γi∈]0,1[\gamma\_{i}\in\,]0,1[ for each trade. We recall that the CFMM ii accepts a proposed trade (xi,yi)∈ℝ+ni×ℝ+ni(x^{i},y^{i})\in\mathbb{R}\_{+}^{n\_{i}}\times\mathbb{R}\_{+}^{n\_{i}} when its trade function φi:ℝ+ni→ℝ\varphi\_{i}:\mathbb{R}\_{+}^{n\_{i}}\rightarrow\mathbb{R} satisfies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | φi​(Ri+γi​yi−xi)=φi​(Ri).\varphi\_{i}(R^{i}+\gamma\_{i}y^{i}-x^{i})=\varphi\_{i}(R^{i}). |  | (3.1) |

Based on [[8](#bib.bib8), Section 5], we are interested in finding a set of valid trades that maximizes the utility of the trader u:ℝn→ℝu:\mathbb{R}^{n}\rightarrow\mathbb{R} in the presence of gas fees q∈ℝ+mq\in\mathbb{R}\_{+}^{m}, where each qi∈ℝ+q\_{i}\in\mathbb{R}\_{+} corresponds to CFMM ii. The gas fee is the cost of recording a trade in the blockchain network, which will be assumed to be fixed for simplicity. We also introduce bi∈ℝ++nib^{i}\in\mathbb{R}\_{++}^{n\_{i}}, where bkib\_{k}^{i} is the maximum amount of asset kk that the trader can buy from CFMM ii. Hence, the optimal routing problem with gas fee is given by (see [[8](#bib.bib8), Section 5])

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | maximize |  | u​(Ψ)−⟨q,η⟩\displaystyle u(\Psi)-\langle q,\eta\rangle |  | (𝒫​(𝐛,q)\mathcal{P}(\mathbf{b},q)) |
|  |  | subject to |  | Ψ=∑i=1mAi​(xi−yi),\displaystyle\Psi=\sum\_{i=1}^{m}A^{i}(x^{i}-y^{i}), |  |
|  |  | φi​(Ri+γi​yi−xi)=φi​(Ri),\displaystyle\varphi\_{i}(R^{i}+\gamma\_{i}y^{i}-x^{i})=\varphi\_{i}(R^{i}), |  | | |
|  |  | 0≤xi≤Ri,\displaystyle 0\leq x^{i}\leq R^{i}, |  | | |
|  |  | 0≤yi≤ηi​bi,\displaystyle 0\leq y^{i}\leq\eta\_{i}b^{i}, |  | | |
|  |  | ηi∈{0,1},∀i∈{1,…,m}.\displaystyle\eta\_{i}\in\{0,1\},~\forall~i\in\{1,\ldots,m\}. |  | | |

In this model, ηi∈{0,1}\eta\_{i}\in\{0,1\} serves as a binary activation indicator for CFMM ii, taking the value ηi=1\eta\_{i}=1 when a trade is executed in pool ii, and ηi=0\eta\_{i}=0 otherwise. The inequality constraint yi≤ηi​biy^{i}\leq\eta\_{i}b^{i} smoothly enforces market activation by bounding trade amounts yiy^{i} by bib^{i} when active (ηi=1\eta\_{i}=1) while requiring yi=0y^{i}=0 when inactive. Our notation emphasizes the crucial parameters 𝐛:=(b1,…,bm)\mathbf{b}:=(b^{1},\ldots,b^{m}) (activation bounds) and qq (vector of gas fees), which are fundamental to the analysis.

Furthermore, we assume that bi∈ℝ++nib^{i}\in\mathbb{R}\_{++}^{n\_{i}} for all i∈{1,…,m}i\in\{1,\ldots,m\}, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | bki≠0,∀i∈{1,…,m},∀k∈{1,…,ni}.b\_{k}^{i}\neq 0,~~\forall~i\in\{1,\ldots,m\},~\forall~k\in\{1,\ldots,n\_{i}\}. |  | (3.2) |

The assumption ([3.2](#S3.E2 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) means that each CFMM i∈{1,…,m}i\in\{1,\ldots,m\} allows for a positive maximal injection bkib^{i}\_{k} of the cryptoasset k∈{1,…,ni}k\in\{1,\ldots,n\_{i}\}.

Following [[8](#bib.bib8)], we relax the parameters 0≤ηi≤10\leq\eta\_{i}\leq 1, in order to obtain a more computable form of the problem, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | maximizeu​(Ψ)−⟨q,η⟩subject toΨ=∑i=1mAi​(xi−yi),φi​(Ri+γi​yi−xi)=φi​(Ri),0≤xi≤Ri,0≤yi≤ηi​bi,0≤ηi≤1,∀i∈{1,…,m}.\begin{array}[]{ll}\text{maximize}&u(\Psi)-\langle q,\eta\rangle\\ \text{subject to}&\Psi=\displaystyle{\sum\_{i=1}^{m}A^{i}}{(x^{i}-y^{i})},\\ &\varphi\_{i}(R^{i}+\gamma\_{i}{y^{i}}-{x^{i}})=\varphi\_{i}(R^{i}),\\ &0\leq x^{i}\leq R^{i},\\ &0\leq y^{i}\leq\eta\_{i}b^{i},\\ &0\leq\eta\_{i}\leq 1,~\forall~i\in\{1,\ldots,m\}.\end{array} |  | (𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)) |

We use the notation

|  |  |  |
| --- | --- | --- |
|  | (𝐱,𝐲,η)=(x1,…,xm,y1,…,ym,η1,…,ηm)∈∏i=1mℝ+ni×∏i=1mℝ+ni×[0,1]m,(\mathbf{x},\mathbf{y},\mathbf{\eta})=(x^{1},\ldots,x^{m},y^{1},\ldots,y^{m},\eta\_{1},\ldots,\eta\_{m})\in\prod\limits\_{i=1}^{m}\mathbb{R}\_{+}^{n\_{i}}\times\prod\limits\_{i=1}^{m}\mathbb{R}\_{+}^{n\_{i}}\times[0,1]^{m}, |  |

where [0,1]m:=∏i=1m[0,1][0,1]^{m}:=\prod\limits\_{i=1}^{m}[0,1] while 𝐱:=(x1,…,xm)\mathbf{x}:=(x^{1},\ldots,x^{m}), 𝐲:=(y1,…,ym)\mathbf{y}:=(y^{1},\ldots,y^{m}) and η:=(η1,…,ηm)\eta:=(\eta\_{1},\ldots,\eta\_{m}) denote, respectively, a potential trade and the vector of market activation relaxed parameters. We stress that the relaxed activation variables do not represent executable
strategies *per se*, but serve as analytical proxies to characterize optimality
and approximation properties.

In the same way, by A:=(A1,…,Am):∏i=1mℝni→ℝnA:=(A^{1},\ldots,A^{m}):\prod\limits\_{i=1}^{m}\mathbb{R}^{n\_{i}}\rightarrow\mathbb{R}^{n} we denote the linear operator defined by

|  |  |  |
| --- | --- | --- |
|  | A​(𝐱)=∑i=1mAi​xi,A(\mathbf{x})={\sum\_{i=1}^{m}A^{i}x^{i}}, |  |

Then, problem ([𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)](#S3.Ex2 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) can be equivalently written as:

|  |  |  |
| --- | --- | --- |
|  | maximize(u∘A)​(𝐱−𝐲)−⟨q,η⟩subject toφi​(Ri+γi​yi−xi)−φi​(Ri)=0,0≤xi≤Ri,yi−ηi​bi≤0,0≤yi,0≤ηi≤1,∀i∈{1,…,m},\begin{array}[]{ll}\text{maximize}&(u\circ A)(\mathbf{x}-\mathbf{y})-\langle q,\eta\rangle\\ \text{subject to}&\varphi\_{i}(R^{i}+\gamma\_{i}{y^{i}}-{x^{i}})-\varphi\_{i}(R^{i})=0,\\ &0\leq x^{i}\leq R^{i},\\ &y^{i}-\eta\_{i}b^{i}\leq 0,\\ &0\leq y^{i},\\ &0\leq\eta\_{i}\leq 1,~\forall~i\in\{1,\ldots,m\},\end{array} |  |

which we can model as an equivalent minimization problem with equality and inequality constraints:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minimizef​(𝐱,𝐲,η):=(−u∘A)​(𝐱−𝐲)+⟨q,η⟩subject toGi​(𝐱,𝐲,η):=yi−ηi​bi≤0,Hi​(𝐱,𝐲,η):=φi​(Ri+γi​yi−xi)−φi​(Ri)=0,∀i=1,…,m,(𝐱,𝐲,η)∈𝐒^,\begin{array}[]{ll}\text{minimize}&f(\mathbf{x},\mathbf{y},\eta):=(-u\circ A)(\mathbf{x}-\mathbf{y})+\langle q,\eta\rangle\\ \text{subject to}&G\_{i}(\mathbf{x},\mathbf{y},\eta):=y^{i}-\eta\_{i}b^{i}\leq 0,\\ &H\_{i}(\mathbf{x},\mathbf{y},\eta):=\varphi\_{i}(R^{i}+\gamma\_{i}y^{i}-x^{i})-\varphi\_{i}(R^{i})=0,\\ &\forall~i=1,\dots,m,\\ &(\mathbf{x},\mathbf{y},\eta)\in\widehat{\mathbf{S}},\end{array} |  | (𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)) |

where f:∏i=1mℝ+ni×∏i=1mℝ+ni×[0,1]m→ℝf:\prod\limits\_{i=1}^{m}\mathbb{R}\_{+}^{n\_{i}}\times\prod\limits\_{i=1}^{m}\mathbb{R}\_{+}^{n\_{i}}\times[0,1]^{m}\rightarrow\mathbb{R}, Gi:∏i=1mℝ+ni×∏i=1mℝ+ni×[0,1]m→𝒵\mathbf{\ }G\_{i}:\prod\limits\_{i=1}^{m}\mathbb{R}\_{+}^{n\_{i}}\times\prod\limits\_{i=1}^{m}\mathbb{R}\_{+}^{n\_{i}}\times[0,1]^{m}\rightarrow\mathcal{Z}, Hi:∏i=1mℝ+ni×∏i=1mℝ+ni×[0,1]m→ℝmH\_{i}:\prod\limits\_{i=1}^{m}\mathbb{R}\_{+}^{n\_{i}}\times\prod\limits\_{i=1}^{m}\mathbb{R}\_{+}^{n\_{i}}\times[0,1]^{m}\rightarrow\mathbb{R}^{m} and the feasible set is

|  |  |  |
| --- | --- | --- |
|  | 𝐒^:={(𝐱,𝐲,η): 0≤xi≤Ri, ​0≤yi, ​0≤ηi≤1,∀i∈{1,…,m}}.\mathbf{\hat{S}}:=\left\{\mathbf{(x,y,}\eta\mathbf{)}:\,0\leq x^{i}\leq R^{i},\text{ }0\leq{y^{i}},\text{ }0\leq\eta\_{i}\leq 1,~\forall~i\in\{1,\ldots,m\}\right\}. |  |

### 3.1 Necessary Optimality Conditions

Under the stated conditions, all problems can be solved by applying standard results (see, for example, [[26](#bib.bib26), Theorem 2.3]).

Throughout this paper, we assume that the utility function uu and the market functions φi\varphi\_{i} are differentiable for every i=1,…,mi=1,\ldots,m, that (𝐱¯,𝐲¯,η¯)∈𝐒^({\bf\bar{x}},{\bf\bar{y}},\bar{\eta})\mathbf{\in\hat{S}} is a solution to problem ([𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)](#S3.Ex6 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and that (𝐱,𝐲,η)∈∏i=1mℝni×∏i=1mℝni×[0,1]m\mathbf{(x,y,}\eta\mathbf{)\in}\prod\limits\_{i=1}^{m}\mathbb{R}^{n\_{i}}\times\prod\limits\_{i=1}^{m}\mathbb{R}^{n\_{i}}\times[0,1]^{m} is an arbitrary direction, respectively. We also consider the following assumptions:

* •

  Positiveness of reserve and maximum of tendered baskets,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝐑,𝐛∈∏i=1mℝ++ni.\mathbf{R,b\in}\prod\limits\_{i=1}^{m}\mathbb{R}\_{++}^{n\_{i}}. |  | (3.3) |
* •

  Non-overlapping support (see [[5](#bib.bib5), Section 3.2]), that is, the following complementary condition is verified for every trade

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 0≤x¯i⊥y¯i≥0⟺x¯i≥0,y¯i≥0, x¯jiy¯ji=0,∀i,j,0\leq\bar{x}^{i}\bot\bar{y}^{i}\geq 0~\Longleftrightarrow~\bar{x}^{i}\geq 0,\,\bar{y}^{i}\geq 0\text{, }\bar{x}\_{j}^{i}\,\bar{y}\_{j}^{i}=0,~\forall~i,j, |  | (3.4) |

  where i∈{1,…,m}i\in\{1,\ldots,m\} and j∈{1,…,ni}j\in\{1,\ldots,n\_{i}\}.
* •

  Increasing behavior of trading and utility functions (see [[22](#bib.bib22)]):

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∇u​(x)≥0​ for every ​x∈ℝn,\displaystyle~\nabla u(x)\geq 0~\text{ for every }x\in\mathbb{R}^{n}, |  | (3.5) |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∇φi​(x)⪈0​ ​for every ​x>0​ and every ​i∈{1,…,m},\displaystyle\nabla\varphi\_{i}(x)\gneq 0\text{ }\ \text{for every }x>0\text{ and every }i\in\{1,\ldots,m\}, |  | (3.6) |

  where the last one implies that φi\varphi\_{i} is strictly increasing with respect to at least one component and, in particular,

  |  |  |  |
  | --- | --- | --- |
  |  | x≥y>0⟹φi​(x)≥φi​(y)​for every ​i=1,…,m.x\geq y>0~\Longrightarrow~\varphi\_{i}(x)\geq\varphi\_{i}(y)\ \text{for every }i=1,\ldots,m. |  |

We define the price vector (see [[5](#bib.bib5)]) and the updated price vector by

|  |  |  |
| --- | --- | --- |
|  | Pi:=∇φi​(Ri), for every ​i=1,…,m,\displaystyle P^{i}:=\nabla\varphi\_{i}(R^{i}),\ \text{ for every }i=1,\ldots,m, |  |
|  |  |  |
| --- | --- | --- |
|  | P¯i:=∇φi​(Ri+γi​y¯i−x¯i), for every ​i=1,…,m.\displaystyle\bar{P}^{i}:=\nabla\varphi\_{i}(R^{i}+\gamma\_{i}{\bar{y}^{i}}-{\bar{x}^{i}}),\text{ for every }i=1,\ldots,m. |  |

Under condition ([3.6](#S3.E6 "In 3rd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), Pi,P¯i≠0P^{i},\bar{P}^{i}\neq 0 for every i=1,…,mi=1,\ldots,m.

###### Remark 3.1.

Under the stated conditions, problem ([𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)](#S3.Ex6 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) is solvable and has at least one solution (𝐱¯,𝐲¯,η¯)\left(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta}\right) by applying standard results (see, e.g., [[26](#bib.bib26), Theorem 2.3 ]).
Furthermore, if η¯i=0\bar{\eta}\_{i}=0, then x¯i=y¯i=0\bar{x}^{i}=\bar{y}^{i}=0.

Conversely, if x¯i=y¯i=0\bar{x}^{i}=\bar{y}^{i}=0 for every i∈{1,…,m}i\in\{1,\dots,m\}, i.e., 𝐱¯=𝐲¯=𝟎\mathbf{\bar{x}}=\mathbf{\bar{y}}=\mathbf{0}, then η¯=0\mathbf{\bar{\eta}}=0. Otherwise, if some 0<η¯r≤10<\bar{\eta}\_{r}\leq 1, we have

|  |  |  |
| --- | --- | --- |
|  | f​(𝟎,𝟎,0)=−u​(A​(𝟎))<−u​(A​(𝟎))+qr​η¯r≤f​(𝟎,𝟎,η¯),f(\mathbf{0},\mathbf{0},0)=-u\left(A(\mathbf{0})\right)<-u\left(A(\mathbf{0})\right)+q\_{r}\bar{\eta}\_{r}\leq f(\mathbf{0},\mathbf{0},\bar{\eta}), |  |

which violates optimality.

A necessary condition is given by a standard multiplier rule [[26](#bib.bib26), Theorem 5.3]: Assume that (𝐱¯,𝐲¯,η¯)(\mathbf{\bar{x}},\mathbf{\mathbf{\bar{y}},}\bar{\eta}) solves problem ([𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)](#S3.Ex6 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and a constraint qualification holds, in particular, if the Kurcyusz-Robinson-Zowe (KRZ) constraint qualification is verified:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∇G​(𝐱¯,𝐲¯,η¯)∇H​(𝐱¯,𝐲¯,η¯))​cone(𝐒^−(𝐱¯,𝐲¯,η¯))+cone(∏i=1mℝ+ni+{G​(𝐱¯,𝐲¯,η¯)}0)\displaystyle\left(\begin{array}[]{c}\nabla G({\bf\bar{x}},{\bf\bar{y}},\bar{\eta})\\ \nabla H({\bf\bar{x}},{\bf\bar{y}},\bar{\eta})\end{array}\right)\operatornamewithlimits{cone}(\mathbf{\hat{S}}-({\bf\bar{x}},{\bf\bar{y}},\bar{\eta}))+\operatornamewithlimits{cone}\left(\begin{array}[]{c}\prod\limits\_{i=1}^{m}\mathbb{R}\_{+}^{n\_{i}}+\left\{G({\bf\bar{x}},{\bf\bar{y}},\bar{\eta})\right\}\\ 0\end{array}\right) |  | (3.11) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =(∏i=1mℝniℝm),\displaystyle=\left(\begin{array}[]{c}\prod\limits\_{i=1}^{m}\mathbb{R}^{n\_{i}}\\ \mathbb{R}^{m}\end{array}\right), |  | (3.14) |

then the following multiplier rule is verified: Find ((𝐱¯,𝐲¯,η¯),(μ1,…,μm),λ)∈𝐒^×(∏i=1mℝ+n)×ℝm\left(\left(\mathbf{\bar{x}},\mathbf{\mathbf{\bar{y}},}\bar{\eta}\right),\left(\mu^{1},\ldots,\mu^{m}\right),\lambda\right)\in\mathbf{\hat{S}}\times\left(\prod\limits\_{i=1}^{m}\mathbb{R}\_{+}^{n}\right)\times\mathbb{R}^{m} such that

|  |  |  |
| --- | --- | --- |
|  | (∇f​(𝐱¯,𝐲¯,η¯)+∑i=1m(μi)⊤​∇Gi​(𝐱¯,𝐲¯,η¯)+∑i=1mλi​∇Hi​(𝐱¯,𝐲¯,η¯))​(𝐱−𝐱¯,𝐲−𝐲¯,η−η¯)≥0,\displaystyle\!\!\left(\!\nabla f(\mathbf{\bar{x},\bar{y},}\bar{\eta}\mathbf{)}\!+\!\!\sum\limits\_{i=1}^{m}(\mu^{i})^{\top}\nabla G\_{i}(\mathbf{\bar{x},\bar{y},}\bar{\eta})\!+\!\!\sum\limits\_{i=1}^{m}\lambda\_{i}\nabla H\_{i}(\mathbf{\bar{x},\bar{y},}\bar{\eta})\!\right)\!(\mathbf{x-\bar{x}\mathbf{,y-\bar{y}\mathbf{,}}}\eta\mathbf{-}\bar{\eta})\geq 0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (μi)⊤​Gi​(𝐱¯,𝐲¯,η¯)=0, for every ​i=1,…,m,\displaystyle(\mu^{i})^{\top}G\_{i}(\mathbf{\bar{x},\bar{y},}\bar{\eta})=0,\ \text{ for every }i=1,\ldots,m, |  | (3.15) |
|  |  |  |
| --- | --- | --- |
|  | Hi​(𝐱¯,𝐲¯,η¯)=0​for every ​i=1,…,m, and ​(𝐱,𝐲,η)∈𝐒^​ arbitrary.\displaystyle H\_{i}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})=0\ \text{for every }i=1,\ldots,m,\text{ and }(\mathbf{x},\mathbf{\mathbf{y},}\eta)\in\mathbf{\hat{S}}\text{ arbitrary.} |  |

In the following, we note that, by a direct calculation, we have

|  |  |  |
| --- | --- | --- |
|  | ∇f​(𝐱¯,𝐲¯,η¯)​(𝐱,𝐲,η)=∑i=1m∇u​(A​(𝐱¯−𝐲¯))​Ai​yi−∑i=1m∇u​(A​(𝐱¯−𝐲¯))​Ai​xi+q⋅η,\displaystyle\nabla f(\mathbf{\bar{x},\bar{y},}\bar{\eta})({\bf x},{\bf y},\eta)=\sum\_{i=1}^{m}\nabla u\left(A(\mathbf{\bar{x}}-\mathbf{\bar{y}})\right)A^{i}y^{i}-{\sum\_{i=1}^{m}}\nabla u\left(A(\mathbf{\bar{x}}-\mathbf{\bar{y}})\right)A^{i}x^{i}+q\cdot\eta, |  |
|  |  |  |
| --- | --- | --- |
|  | ∇Gi​(𝐱¯,𝐲¯,η¯)​(𝐱,𝐲,η)=yi−ηi​bi,\displaystyle\nabla G\_{i}(\mathbf{\bar{x},\bar{y},}\bar{\eta})(\mathbf{x,y,}\eta)=y^{i}-\eta\_{i}b^{i}, |  |
|  |  |  |
| --- | --- | --- |
|  | ∇Hi​(𝐱¯,𝐲¯,η¯)​(𝐱,𝐲,η)=−∇φi​(𝐑+γ​𝐲¯−𝐱¯)​xi+γi​∇φi​(𝐑+γ​𝐲¯−𝐱¯)​yi,\displaystyle\nabla H\_{i}(\mathbf{\bar{x},\bar{y},}\bar{\eta})(\mathbf{x,y,}\eta)=-\nabla\varphi\_{i}(\mathbf{R}+\gamma\mathbf{\bar{y}}-\mathbf{\bar{x})}x^{i}\mathbf{+}\gamma\_{i}\nabla\varphi\_{i}(\mathbf{R}+\gamma\mathbf{\bar{y}}-\mathbf{\bar{x})}y^{i}, |  |

for every i∈{1,…,m}i\in\{1,\ldots,m\}.

In the next result, we establish conditions for which the constraint qualification ([3.14](#S3.E14 "In 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) is verified.

###### Proposition 3.1.

Assume that properties ([3.3](#S3.E3 "In 1st item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and ([3.6](#S3.E6 "In 3rd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) hold. Let (𝐱¯,𝐲¯,η¯)(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta}) be a solution to ([𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)](#S3.Ex6 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) satisfying ([3.4](#S3.E4 "In 2nd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")). Then, constraint qualification ([3.14](#S3.E14 "In 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) holds at (𝐱¯,𝐲¯,η¯)=(𝟎,𝟎,0)(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})=(\mathbf{0},\mathbf{0},0). Moreover, when (𝐱¯,𝐲¯,η¯)≠(𝟎,𝟎,0)(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\neq(\mathbf{0},\mathbf{0},0), condition ([3.14](#S3.E14 "In 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) is also satisfied if the following additional property holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0<bji−y¯ji≤2γi​Rji​with​y¯ji>0,∀j∈{1,…,ni},∀i∈{1,…,m}.0<b\_{j}^{i}-\bar{y}\_{j}^{i}\leq\frac{2}{\gamma\_{i}}R\_{j}^{i}~\text{with}~\bar{y}\_{j}^{i}>0,~\forall~j\in\{1,\ldots,n\_{i}\},~\forall~i\in\{1,\ldots,m\}. |  | (3.16) |

###### Proof.

Condition ([3.14](#S3.E14 "In 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) is equivalent to: For every ((z1,…,zn),t)∈∏i=1mℝni×ℝ((z^{1},\ldots,z^{n}),t)\in\!\prod\limits\_{i=1}^{m}\mathbb{R}^{n\_{i}}\times\mathbb{R} we can take α,β∈ℝ+\alpha,\beta\in\mathbb{R}\_{+}, (𝐱,𝐲,η)∈𝐒^({\bf x},{\bf y},\eta)\in\mathbf{\hat{S}} and c,d∈∏i=1mℝ+nic,d\in\prod\limits\_{i=1}^{m}\mathbb{R}\_{+}^{n\_{i}} such that

|  |  |  |
| --- | --- | --- |
|  | zi=∇Gi​(𝐱¯,𝐲¯,η¯)​(α​(xi−x¯i,yi−y¯i,ηi−η¯i))+β​(ci+{Gi​(𝐱¯,𝐲¯,η¯)}),ti=∇Hi​(𝐱¯,𝐲¯,η¯)​(α​(xi−x¯i,yi−y¯i,ηi−η¯i)).\begin{array}[]{l}z^{i}=\nabla G\_{i}({\bf\bar{x}},{\bf\bar{y}},\bar{\eta})(\alpha(x^{i}-\bar{x}^{i},y^{i}-\bar{y}^{i},\eta\_{i}-\bar{\eta}\_{i}))+\beta(c^{i}+\left\{G\_{i}({\bf\bar{x}},{\bf\bar{y}},\bar{\eta})\right\}),\\ t\_{i}=\nabla H\_{i}({\bf\bar{x}},{\bf\bar{y}},\bar{\eta})(\alpha(x^{i}-\bar{x}^{i},y^{i}-\bar{y}^{i},\eta\_{i}-\bar{\eta}\_{i})).\end{array} |  |

Indeed, by a direct calculation, the latter is equivalent to: There exist 0≤xi≤Ri0\leq x^{i}\leq R^{i}, 0≤yi0\leq y^{i} and 0≤ηi≤10\leq\eta\_{i}\leq 1 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
|  | zji=α​((yji−y¯ji)−(ηi−η¯i)​bji)+β​(cji+y¯ji−η¯i​bji),\displaystyle z\_{j}^{i}=\alpha\left((y^{i}\_{j}-\bar{y}^{i}\_{j})-(\eta\_{i}-\bar{\eta}\_{i})b^{i}\_{j}\right)+\beta(c^{i}\_{j}+\bar{y}^{i}\_{j}-\bar{\eta}\_{i}b^{i}\_{j}), |  | (3.17a) |
|  | ti=α​(P¯i)⊤​(−(xi−x¯i)+γi​(yi−y¯i)),\displaystyle\,t\_{i}=\alpha(\bar{P}^{i})^{\top}\left(-(x^{i}-\bar{x}^{i})+\gamma\_{i}(y^{i}-\bar{y}^{i})\right), |  | (3.17b) |
| for every i∈{1,…,m}i\in\{1,\ldots,m\} and every j∈{1,…,ni}j\in\{1,\ldots,n\_{i}\}. | | | |

Without loss of generality, in the sequel we consider a fixed i∈{1,…,m}i\in\{1,\ldots,m\}. By hypothesis ([3.6](#S3.E6 "In 3rd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), we can assume

|  |  |  |
| --- | --- | --- |
|  | P¯ki≠0,\bar{P}\_{k}^{i}\neq 0, |  |

for some k∈{1,…,ni}k\in\{1,\ldots,n\_{i}\}. Then, we consider the following cases:

If η¯i=0\bar{\eta}\_{i}=0, then (x¯i,y¯i)=(0,0)(\bar{x}^{i},\bar{y}^{i})=(0,0) by Remark [3.1](#S3.Thmremark1 "Remark 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"). In this case, equations ([3.17a](#S3.E17.1 "In 3.17 ‣ Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and ([3.17b](#S3.E17.2 "In 3.17 ‣ Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) reduce to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | zi\displaystyle z^{i} | =α​(yi−ηi​bi)+β​ci,\displaystyle=\alpha\left(y^{i}-\eta\_{i}b^{i}\right)+\beta c^{i}, |  | (3.18a) |
|  | ti\displaystyle t\_{i} | =α​(P¯i)⊤​(−xi+γi​yi).\displaystyle=\alpha(\bar{P}^{i})^{\top}\left(-x^{i}+\gamma\_{i}y^{i}\right). |  | (3.18b) |
| Setting α=β\alpha=\beta, equation ([3.18a](#S3.E18.1 "In 3.18 ‣ Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) simplifies to | | | | |

|  |  |  |  |
| --- | --- | --- | --- |
|  | zi=α​(yi+ci−ηi​bi).z^{i}=\alpha\left(y^{i}+c^{i}-\eta\_{i}b^{i}\right). |  | (3.19) |

We may assume ηi​bi−yi∈int​(ℝ+ni)\eta\_{i}b^{i}-y^{i}\in\mathrm{int}(\mathbb{R}\_{+}^{n\_{i}}), for instance choosing yi=12​ηi​bi∈int​(ℝ+ni)y^{i}=\frac{1}{2}\eta\_{i}b^{i}\in\mathrm{int}(\mathbb{R}\_{+}^{n\_{i}}) with ηi>0\eta\_{i}>0. On the other
hand, we can define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ci=ηi​bi−yi+1α​zi=12​ηi​bi+1α​zi≥0,c^{i}=\eta\_{i}b^{i}-y^{i}+\frac{1}{\alpha}z^{i}=\frac{1}{2}\eta\_{i}b^{i}+\frac{1}{\alpha}z^{i}\geq 0, |  | (3.20) |

which holds for sufficiently large α\alpha, thus there exists α1>0\alpha\_{1}>0 such
that ([3.20](#S3.E20 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) for every α≥α1\alpha\geq\alpha\_{1}.

Let xi=γi​yi−1α​tiP¯ki​ek=12​γi​ηi​bi−1α​tiP¯ki​ekx^{i}=\gamma\_{i}y^{i}-\dfrac{1}{\alpha}\frac{t\_{i}}{\bar{P}\_{k}^{i}}e^{k}=\frac{1}{2}\gamma\_{i}\eta\_{i}b^{i}-\dfrac{1}{\alpha}\frac{t\_{i}}{\bar{P}\_{k}^{i}}e^{k}, where eke^{k} (with ejk=δj​ke\_{j}^{k}=\delta\_{jk}) is the
kk-th standard basis vector. Without loss of generality we consider yi=12​ηi​bi≤Riy^{i}=\frac{1}{2}\eta\_{i}b^{i}\leq R^{i}. Thus, taking ηi\eta\_{i} small enough, we have

|  |  |  |
| --- | --- | --- |
|  | xi=γi​yi−1α​tiP¯ki​ek≤12​γi​ηi​bi≤Ri.x^{i}=\gamma\_{i}y^{i}-\frac{1}{\alpha}\frac{t\_{i}}{\bar{P}\_{k}^{i}}e^{k}\leq\frac{1}{2}\gamma\_{i}\eta\_{i}b^{i}\leq R^{i}. |  |

At the same time there exists α2>0\alpha\_{2}>0 large enough such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi=γi​yi−1α​tiP¯ki​ek≥0,for​all​α≥α2.x^{i}=\gamma\_{i}y^{i}-\frac{1}{\alpha}\frac{t\_{i}}{\bar{P}\_{k}^{i}}e^{k}\geq 0,\mathrm{~for~all~}\alpha\geq\alpha\_{2}. |  | (3.21) |

Taking α:=max⁡{α1,α2}>0\alpha:=\max\{\alpha\_{1},\alpha\_{2}\}>0 and substituting ([3.20](#S3.E20 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and ([3.21](#S3.E21 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) into ([3.19](#S3.E19 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and ([3.18b](#S3.E18.2 "In 3.18 ‣ Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), we obtain:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | α​(yi+(ηi​bi+ziα−yi)−ηi​bi)\displaystyle\alpha(y^{i}+(\eta\_{i}b^{i}+\frac{z^{i}}{\alpha}-y^{i})-\eta\_{i}b^{i}) | =zi,\displaystyle=z^{i}, |  | (3.22) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | α​(P¯i)⊤​(−(γi​yi−1α​tiP¯ki​ek)+γi​yi)\displaystyle\alpha(\bar{P}^{i})^{\top}(-(\gamma\_{i}y^{i}-\frac{1}{\alpha}\frac{t\_{i}}{\bar{P}\_{k}^{i}}e^{k})+\gamma\_{i}y^{i}) | =ti.\displaystyle=t\_{i}. |  | (3.23) |

Thus, equations ([3.18a](#S3.E18.1 "In 3.18 ‣ Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and ([3.18b](#S3.E18.2 "In 3.18 ‣ Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) are satisfied, that is, the constraint qualification condition holds at (𝐱¯,𝐲¯,η¯)=(0,0,0)(\bar{\mathbf{x}},\bar{\mathbf{y}},\bar{\eta})=(0,0,0).

Let us analyze the case when η¯i≠0\bar{\eta}\_{i}\neq 0. If η¯i≠0\bar{\eta}\_{i}\neq 0, then by a similar reasoning as before we consider α=β\alpha=\beta, thus replacing in ([3.17a](#S3.E17.1 "In 3.17 ‣ Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and ([3.17b](#S3.E17.2 "In 3.17 ‣ Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
|  | zi=α​(yi−ηi​bi+ci),\displaystyle z^{i}=\alpha(y^{i}-\eta\_{i}b^{i}+c^{i}), |  | (3.24a) |
|  | ti=α​(P¯i)⊤​(−(xi−x¯i)+γi​(yi−y¯i)).\displaystyle t\_{i}=\alpha(\bar{P}^{i})^{\top}(-(x^{i}-\bar{x}^{i})+\gamma\_{i}(y^{i}-\bar{y}^{i})). |  | (3.24b) |

In this case, if yi=12​(y¯i+bi)y^{i}=\frac{1}{2}(\bar{y}^{i}+b^{i}) and ηi=1\eta\_{i}=1, then yi−y¯i=12​(bi−y¯i)∈int​(ℝ+ni)y^{i}-\bar{y}^{i}=\dfrac{1}{2}\left(b^{i}-\bar{y}^{i}\right)\in{\rm int}(\mathbb{R}\_{+}^{n\_{i}}) by ([3.16](#S3.E16 "In Proposition 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), and we can assure that ci:=12​(bi−y¯i)+ziα∈ℝ+nic^{i}:=\dfrac{1}{2}\left(b^{i}-\bar{y}^{i}\right)+\frac{z^{i}}{\alpha}\in\mathbb{R}\_{+}^{n\_{i}} and

|  |  |  |
| --- | --- | --- |
|  | xi:=x¯i+γi​(yi−y¯i)−1α​tiP¯ki​ek=x¯i+γi2​(bi−y¯i)−1α​tiP¯ki​ek∈ℝ+ni,x^{i}:=\bar{x}^{i}+\gamma\_{i}(y^{i}-\bar{y}^{i})-\frac{1}{\alpha}\frac{t\_{i}}{\bar{P}\_{k}^{i}}e^{k}=\bar{x}^{i}+\frac{\gamma\_{i}}{2}(b^{i}-\bar{y}^{i})-\frac{1}{\alpha}\frac{t\_{i}}{\bar{P}\_{k}^{i}}e^{k}\in\mathbb{R}\_{+}^{n\_{i}}, |  |

for α>0\alpha>0 big enough. Furthermore, we can assure that xi≤Rix^{i}\leq R^{i} if

|  |  |  |  |
| --- | --- | --- | --- |
|  | x¯i+γi2​(bi−y¯i)≤Ri⟺2​x¯i+γi​(bi−y¯i)≤2​Ri.\bar{x}^{i}+\dfrac{\gamma\_{i}}{2}(b^{i}-\bar{y}^{i})\leq R^{i}~\Longleftrightarrow~2\bar{x}^{i}+\gamma\_{i}(b^{i}-\bar{y}^{i})\leq 2R^{i}. |  | (3.25) |

By the complementary condition ([3.4](#S3.E4 "In 2nd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), relation ([3.25](#S3.E25 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) is equivalent to 2​x¯ji≤2​Rji2\bar{x}\_{j}^{i}\leq 2R\_{j}^{i} for every jj such that x¯ji>0\bar{x}\_{j}^{i}>0, which is evident, and γi​(bji−y¯ji)≤2​Rji\gamma\_{i}(b\_{j}^{i}-\bar{y}\_{j}^{i})\leq 2R\_{j}^{i} for y¯ji>0\bar{y}\_{j}^{i}>0, which holds in virtue of assumption ([3.16](#S3.E16 "In Proposition 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")).
∎

In the following result, we give an explicit form for the KKT system ([3.29](#S3.E29 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")). Furthermore, in order to avoid confusion with variables, we emphasize that we denote partial derivatives by

|  |  |  |
| --- | --- | --- |
|  | Dk​u≡∂u/∂xk.D\_{k}u\equiv\partial u/\partial x\_{k}. |  |

###### Theorem 3.1.

Assume that properties ([3.3](#S3.E3 "In 1st item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), ([3.5](#S3.E5 "In 3rd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), and ([3.6](#S3.E6 "In 3rd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) hold. Also, let (𝐱¯,𝐲¯,η¯)∈𝐒^(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\in\mathbf{\hat{S}} be a solution to ([𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)](#S3.Ex6 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) satisfying ([3.4](#S3.E4 "In 2nd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and ([3.16](#S3.E16 "In Proposition 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) whenever (𝐱¯,𝐲¯,η¯)≠(𝟎,𝟎,0)(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\neq(\mathbf{0},\mathbf{0},0). Then, there exist μ=(μ1,…,μm)∈∏i=1mℝ+ni\mu=(\mu^{1},\ldots,\mu^{m})\in\prod\_{i=1}^{m}\mathbb{R}\_{+}^{n\_{i}} and α∈ℝ+m\alpha\in\mathbb{R}\_{+}^{m} such that for each i∈{1,…,m}i\in\{1,\ldots,m\}, we have:

* (a)(a)

  If η¯i=0\bar{\eta}\_{i}=0, then (x¯i,y¯i)=(0,0)(\bar{x}^{i},\bar{y}^{i})=(0,0)
  and the associated KKT condition is given by

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | αi​(P¯i)⊤≥∇u​(𝟎)​Ai≥γi​αi​(P¯i)⊤−(μi)⊤,qi−(μi)⊤​bi≥0.\begin{array}[]{l}\alpha\_{i}(\bar{P}^{i})^{\top}\geq\nabla u(\mathbf{0})A^{i}\geq\gamma\_{i}\alpha\_{i}(\bar{P}^{i})^{\top}-(\mu^{i})^{\top},\\ \hskip 35.56593ptq\_{i}-(\mu^{i})^{\top}b^{i}\geq 0.\end{array} |  | (3.26) |
* (b)(b)

  If η¯i≠0\bar{\eta}\_{i}\neq 0, then the associated KKT condition is given by

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | αi​P¯ji≥∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji≥γi​αi​P¯ji+μji,when ​x¯ji=y¯ji=0,∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji=γi​αi​P¯ji+μji,when ​x¯ji=0,y¯ji>0,∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji=αi​P¯ji,when ​0<x¯ji<Rji, ​y¯ji=0,∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji≥αi​P¯ji,when ​x¯ji=Rji​, ​y¯ji=0,(μi)⊤​(y¯i−η¯i​bi)=0,qi−(μi)⊤​bi=0,φi​(Ri+γi​y¯i−x¯i)=φi​(Ri).\!\!\!\!\!\!\!\!\!\!\!\!\begin{array}[]{ll}\alpha\_{i}\bar{P}\_{j}^{i}\geq\sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}\geq\gamma\_{i}\alpha\_{i}\bar{P}\_{j}^{i}+\mu\_{j}^{i},&\!\!\!\!\text{when }\bar{x}\_{j}^{i}=\bar{y}\_{j}^{i}=0,\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}=\gamma\_{i}\alpha\_{i}\bar{P}\_{j}^{i}+\mu\_{j}^{i},&\!\!\!\!\text{when }\bar{x}\_{j}^{i}=0,\bar{y}\_{j}^{i}>0,\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}=\alpha\_{i}\bar{P}\_{j}^{i},&\!\!\!\!\text{when }0<\bar{x}\_{j}^{i}<R\_{j}^{i},\text{ }\bar{y}\_{j}^{i}=0,\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}\geq\alpha\_{i}\bar{P}\_{j}^{i},&\!\!\!\!\text{when }\bar{x}\_{j}^{i}=R\_{j}^{i}\text{, }\bar{y}\_{j}^{i}=0,\vskip 6.0pt plus 2.0pt minus 2.0pt\\ (\mu^{i})^{\top}\left(\bar{y}^{i}-\bar{\eta}\_{i}b^{i}\right)=0,&\vskip 6.0pt plus 2.0pt minus 2.0pt\\ q\_{i}-(\mu^{i})^{\top}b^{i}=0,&\vskip 6.0pt plus 2.0pt minus 2.0pt\\ \varphi\_{i}(R^{i}+\gamma\_{i}{\bar{y}^{i}}-{\bar{x}^{i}})=\varphi\_{i}(R^{i}).&\end{array} |  | (3.27) |

###### Proof.

By Proposition [3.1](#S3.Thmpr1 "Proposition 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"), the constraint qualification (KRZ) holds and, applying [[26](#bib.bib26), Theorem 5.6], it follows that the system ([3.15](#S3.E15 "In 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) holds for (𝐱¯,𝐲¯,η¯)(\mathbf{\bar{x}},\mathbf{\mathbf{\bar{y}},}\bar{\eta}). Hence, there there exist (μ1,…,μm)∈∏i=1mℝ+ni(\mu^{1},\ldots,\mu^{m})\in\prod\_{i=1}^{m}\mathbb{R}\_{+}^{n\_{i}} and λ∈ℝm\lambda\in\mathbb{R}^{m} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
|  | ∑i=1m[∇u(A(𝐱¯−𝐲¯))Ai(−(xi−x¯i)+(yi−y¯i))+qi(ηi−η¯i)\displaystyle\sum\limits\_{i=1}^{m}\bigg[\nabla u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A^{i}(-(x^{i}-\bar{x}^{i})+(y^{i}-\bar{y}^{i}))+q\_{i}(\eta\_{i}-\bar{\eta}^{i}) |  |
|  | (μi)⊤[(yi−y¯i)−(ηi−η¯i)bi]+λi(P¯i)⊤(−(xi−x¯i)+γi(yi−y¯i))]≥0,\displaystyle\quad(\mu^{i})^{\top}\left[(y^{i}-\bar{y}^{i})-(\eta\_{i}-\bar{\eta}\_{i})b^{i}\right]+\lambda\_{i}(\bar{P}^{i})^{\top}(-(x^{i}-\bar{x}^{i})+\gamma\_{i}(y^{i}-\bar{y}^{i}))\bigg]\geq 0, |  |
|  | (μi)⊤​(y¯i−η¯i​bi)=0,for every ​i=1,…,m,\displaystyle(\mu^{i})^{\top}(\bar{y}^{i}-\bar{\eta}\_{i}b^{i})=0,\quad\text{for every }i=1,\ldots,m, |  | (3.28a) |
|  | φi​(Ri+γi​y¯i−x¯i)=φi​(Ri)for every ​i=1,…,m,\displaystyle\varphi\_{i}(R^{i}+\gamma\_{i}\bar{y}^{i}-\bar{x}^{i})=\varphi\_{i}(R^{i})\quad\text{for every }i=1,\ldots,m, |  |
|  | and ​(𝐱,𝐲,η)∈𝐒^​ arbitrary.\displaystyle\text{and }(\mathbf{x},\mathbf{y},\eta)\in\mathbf{\hat{S}}\text{ arbitrary.} |  |

This is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | | | |
|  | ∑i=1m[(−∇u​(A​(𝐱¯−𝐲¯))​Ai−λi​(P¯i)⊤)​(xi−x¯i)]+∑i=1m[(qi−(μi)⊤​bi)​(ηi−η¯i)]\displaystyle\sum\_{i=1}^{m}\bigg[(-\nabla u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A^{i}-\lambda\_{i}(\bar{P}^{i})^{\top})\left(x^{i}-\bar{x}^{i}\right)\bigg]+\sum\_{i=1}^{m}\bigg[(q\_{i}-(\mu^{i})^{\top}b^{i})\left(\eta\_{i}-\bar{\eta}\_{i}\right)\bigg] |  |
|  | +∑i=1m[(∇u​(A​(𝐱¯−𝐲¯))​Ai+γi​λi​(P¯i)⊤+(μi)⊤)​(yi−y¯i)]≥0,\displaystyle\quad+\sum\_{i=1}^{m}\bigg[(\nabla u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A^{i}+\gamma\_{i}\lambda\_{i}(\bar{P}^{i})^{\top}+(\mu^{i})^{\top})\left(y^{i}-\bar{y}^{i}\right)\bigg]\geq 0,\vskip 6.0pt plus 2.0pt minus 2.0pt |  | (3.29a) |
|  | (μi)⊤​(y¯i−η¯i​bi)=0,for every ​i=1,…,m,\displaystyle(\mu^{i})^{\top}\left(\bar{y}^{i}-\bar{\eta}\_{i}b^{i}\right)=0,\quad\text{for every }i=1,\ldots,m,\vskip 6.0pt plus 2.0pt minus 2.0pt |  | (3.29b) |
|  | φi​(Ri+γi​y¯i−x¯i)=φi​(Ri)for every ​i=1,…,m,\displaystyle\varphi\_{i}(R^{i}+\gamma\_{i}\bar{y}^{i}-\bar{x}^{i})=\varphi\_{i}(R^{i})\quad\text{for every }i=1,\ldots,m, |  |
|  | and ​(𝐱,𝐲,η)∈𝐒^​ arbitrary.\displaystyle\text{and }(\mathbf{x},\mathbf{y},\eta)\in\mathbf{\hat{S}}\text{ arbitrary.} |  | (3.29c) |

Since the first inequality holds for all xi,yi∈ℝ+nix^{i},y^{i}\in\mathbb{R}\_{+}^{n\_{i}} and all η∈[0,1]m\eta\in[0,1]^{m}, the previous conditions can be equivalently studied on each market. Therefore, for each market i=1,…,mi=1,\ldots,m, the following conditions must hold:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (−∇u​(A​(𝐱¯−𝐲¯))​Ai−λi​(P¯i)⊤)​(xi−x¯i)≥0for all ​xi≥0,\displaystyle\left(-\nabla u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A^{i}-\lambda\_{i}(\bar{P}^{i})^{\top}\right)\left(x^{i}-\bar{x}^{i}\right)\geq 0\quad\text{for all }x^{i}\geq 0, |  | (3.30) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (∇u​(A​(𝐱¯−𝐲¯))​Ai+γi​λi​(P¯i)⊤+(μi)⊤)​(yi−y¯i)≥0for all ​yi≥0,\displaystyle\left(\nabla u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A^{i}+\gamma\_{i}\lambda\_{i}(\bar{P}^{i})^{\top}+(\mu^{i})^{\top}\right)\left(y^{i}-\bar{y}^{i}\right)\geq 0\quad\text{for all }y^{i}\geq 0, |  | (3.31) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (qi−(μi)⊤​bi)​(ηi−η¯i)≥0for all ​ηi≥0,\displaystyle\left(q\_{i}-(\mu^{i})^{\top}b^{i}\right)\left(\eta\_{i}-\bar{\eta}\_{i}\right)\geq 0\quad\text{for all }\eta\_{i}\geq 0, |  | (3.32) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (μi)⊤​(y¯i−η¯i​bi)=0,\displaystyle~(\mu^{i})^{\top}(\bar{y}^{i}-\bar{\eta}\_{i}b^{i})=0, |  | (3.33) |

and equivalently on each asset for the first two equations,

|  |  |  |  |
| --- | --- | --- | --- |
|  | (−∑k=1nDku((A(𝐱¯−𝐲¯))Ak​ji−λiP¯ji)(xji−x¯ji)≥0for all xji≥0,\displaystyle\left(-\sum\_{k=1}^{n}D\_{k}u((A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}-\lambda\_{i}\bar{P}\_{j}^{i}\right)\left(x\_{j}^{i}-\bar{x}\_{j}^{i}\right)\geq 0\quad\text{for all }x\_{j}^{i}\geq 0, |  | (3.34) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji+γi​λi​P¯ji+μji)​(yji−y¯ji)≥0​ for all ​yji≥0,\displaystyle\left(\sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}+\gamma\_{i}\lambda\_{i}\bar{P}\_{j}^{i}+\mu\_{j}^{i}\right)\left(y\_{j}^{i}-\bar{y}\_{j}^{i}\right)\geq 0~\text{ for all }y\_{j}^{i}\geq 0, |  | (3.35) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (qi−(μi)⊤​bi)​(ηi−η¯i)≥0​for all ​ηi≥0,\displaystyle\,\left(q\_{i}-(\mu^{i})^{\top}b^{i}\right)\left(\eta\_{i}-\bar{\eta}\_{i}\right)\geq 0~\text{for all }\eta\_{i}\geq 0, |  | (3.36) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (μi)⊤​(y¯i−η¯i​bi)=0,\displaystyle~(\mu^{i})^{\top}(\bar{y}^{i}-\bar{\eta}\_{i}b^{i})=0, |  | (3.37) |

for every j=1,…,nij=1,\ldots,n\_{i}.

In general, if η¯i>0\bar{\eta}\_{i}>0, then ηi−η¯i\eta\_{i}-\bar{\eta}\_{i} can be indistinctly strictly positive or strictly negative so, from ([3.36](#S3.E36 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and ([3.37](#S3.E37 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | qi−(μi)⊤​bi=0,\displaystyle q\_{i}-(\mu^{i})^{\top}b^{i}=0, |  | (3.38) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (μi)⊤​y¯i=η¯i​(μi)⊤​bi.\displaystyle\hskip 17.07182pt\,(\mu^{i})^{\top}\bar{y}^{i}=\bar{\eta}\_{i}(\mu^{i})^{\top}b^{i}. |  | (3.39) |

On the other hand, if η¯i=0\bar{\eta}\_{i}=0, then from ([3.36](#S3.E36 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) we get (qi−(μi)⊤​bi)​ηi≥0(q\_{i}-(\mu^{i})^{\top}b^{i})\eta\_{i}\geq 0 for all ηi≥0\eta\_{i}\geq 0, thus ([3.36](#S3.E36 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | qi−(μi)⊤​bi≥0.q\_{i}-(\mu^{i})^{\top}b^{i}\geq 0. |  | (3.40) |

Therefore, we can distinguish two cases based on the activation of the market.

(i)(i): When η¯i=0\bar{\eta}\_{i}=0, i.e., the market ii is inactive, thus Remark [3.1](#S3.Thmremark1 "Remark 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") implies that x¯i=y¯i=0\bar{x}^{i}=\bar{y}^{i}=0. As previously discussed, condition ([3.36](#S3.E36 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) is equivalent to ([3.38](#S3.E38 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), while condition ([3.37](#S3.E37 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) is automatically satisfied.

On the other hand, conditions ([3.34](#S3.E34 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and ([3.35](#S3.E35 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) are equivalent to

|  |  |  |
| --- | --- | --- |
|  | −∇u​(𝟎)​Ai−λi​(P¯i)⊤≥0,∇u​(𝟎)​Ai+γi​λi​(P¯i)⊤+(μi)⊤≥0.\begin{array}[]{c}-\nabla u(\mathbf{0})A^{i}-\lambda\_{i}(\bar{P}^{i})^{\top}\geq 0,\\ \nabla u(\mathbf{0})A^{i}+\gamma\_{i}\lambda\_{i}(\bar{P}^{i})^{\top}+(\mu^{i})^{\top}\geq 0.\end{array} |  |

From the first inequality, we have −λi​(P¯i)⊤≥∇u​(𝟎)​Ai-\lambda\_{i}(\bar{P}^{i})^{\top}\geq\nabla u(\mathbf{0})A^{i}, which implies:

|  |  |  |
| --- | --- | --- |
|  | −λi​P¯ji≥∑k=1nDk​u​(𝟎)​Ak​jifor every ​j∈{1,…,ni}.-\lambda\_{i}\bar{P}\_{j}^{i}\geq\sum\_{k=1}^{n}D\_{k}u(\mathbf{0})A\_{kj}^{i}\quad\text{for every }j\in\{1,\ldots,n\_{i}\}. |  |

Since Dk​u​(0)≥0D\_{k}u(0)\geq 0, P¯ji≥0\bar{P}\_{j}^{i}\geq 0 by hypotheses ([3.5](#S3.E5 "In 3rd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and ([3.6](#S3.E6 "In 3rd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), and Ak​ji≥0A\_{kj}^{i}\geq 0 by definition, it follows that λi≤0\lambda\_{i}\leq 0. Consequently, ([3.1](#S3.Ex3a "Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | |λi|​(P¯i)⊤≥∇u​(𝟎)​Ai≥γi​|λi|​(P¯i)⊤−(μi)⊤.|\lambda\_{i}|(\bar{P}^{i})^{\top}\geq\nabla u(\mathbf{0})A^{i}\geq\gamma\_{i}|\lambda\_{i}|(\bar{P}^{i})^{\top}-(\mu^{i})^{\top}. |  |

This proves that the KKT system ([3.28a](#S3.E28.1 "In 3.28 ‣ Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) is equivalent to ([3.26](#S3.E26 "In item (a) ‣ Theorem 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")).

(i​i)(ii): When η¯i≠0\bar{\eta}\_{i}\not=0, we distinguish traded assets indices. For each j∈{1,…,ni}j\in\{1,\ldots,n\_{i}\} and based on the complementary condition ([3.4](#S3.E4 "In 2nd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), we have the following cases:

* •

  If x¯ji=y¯ji=0\bar{x}\_{j}^{i}=\bar{y}\_{j}^{i}=0, then

  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  |  | | | | | |
  |  | −∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji−λi​P¯ji\displaystyle-\sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}-\lambda\_{i}\bar{P}\_{j}^{i} | ≥\displaystyle\geq | 0​,\displaystyle 0\text{, } |  |
  |  | ∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji+γi​λi​P¯ji+μji\displaystyle\sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}+\gamma\_{i}\lambda\_{i}\bar{P}\_{j}^{i}+\mu\_{j}^{i} | ≥\displaystyle\geq | 0​,\displaystyle 0\text{, } |  |
  | and, following the same reasoning as before, that is equivalent to | | | | | |

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | |λi|P¯ji≥∑k=1nDku((A(𝐱¯−𝐲¯))Ak​ji≥γi|λi|P¯ji+μji.\lvert\lambda\_{i}\rvert\bar{P}\_{j}^{i}\geq\sum\_{k=1}^{n}D\_{k}u((A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}\geq\gamma\_{i}\lvert\lambda\_{i}\rvert\bar{P}\_{j}^{i}+\mu\_{j}^{i}. |  | (3.42) |
* •

  If x¯ji=0\bar{x}\_{j}^{i}=0 and y¯ji>0\bar{y}\_{j}^{i}>0, then ([3.34](#S3.E34 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and ([3.35](#S3.E35 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) are equivalent to

  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  |  | −∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji−λi​P¯ji\displaystyle-\sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}-\lambda\_{i}\bar{P}\_{j}^{i} | ≥\displaystyle\geq | 0​,\displaystyle 0\text{, } |  | (3.43) |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | ∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji+γi​λi​P¯ji+μji\displaystyle\sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}+\gamma\_{i}\lambda\_{i}\bar{P}\_{j}^{i}+\mu\_{j}^{i} | =\displaystyle= | 0.\displaystyle 0. |  |

  As before, from the first equation we deduce that λi≤0\lambda\_{i}\leq 0. Furthermore, the inequality follows from the equality since

  |  |  |  |
  | --- | --- | --- |
  |  | ∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji=γi​|λi|​P¯ji−μji≤γi​|λi|​P¯ji≤|λi|​P¯ji=−λi​P¯ji,\sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}=\gamma\_{i}\lvert\lambda\_{i}\rvert\bar{P}\_{j}^{i}-\mu\_{j}^{i}\leq\gamma\_{i}\lvert\lambda\_{i}\rvert\bar{P}\_{j}^{i}\leq\lvert\lambda\_{i}\rvert\bar{P}\_{j}^{i}=-\lambda\_{i}\bar{P}\_{j}^{i}, |  |

  thus ([3.43](#S3.E43 "In 2nd item ‣ Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) is equivalent to

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji+γi​λi​P¯ji+μji=0.\sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}+\gamma\_{i}\lambda\_{i}\bar{P}\_{j}^{i}+\mu\_{j}^{i}=0. |  | (3.44) |
* •

  If Rji>x¯ji>0R\_{j}^{i}>\bar{x}\_{j}^{i}>0 and y¯ji=0\bar{y}\_{j}^{i}=0, then ([3.34](#S3.E34 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and ([3.35](#S3.E35 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) are equivalent to

  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  |  | −∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji−λi​P¯ji\displaystyle-\sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}-\lambda\_{i}\bar{P}\_{j}^{i} | =\displaystyle= | 0​,\displaystyle 0\text{, } |  | (3.45) |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | ∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji+γi​λi​P¯ji+μji\displaystyle\sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}+\gamma\_{i}\lambda\_{i}\bar{P}\_{j}^{i}+\mu\_{j}^{i} | ≥\displaystyle\geq | 0.\displaystyle 0. |  |

  Using ([3.5](#S3.E5 "In 3rd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) in the first equation, we deduce that λi≤0\lambda\_{i}\leq 0, and

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji=|λi|​P¯ji≥γi​|λi|​P¯ji≥γi​|λi|​P¯ji−μji.\sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}=\lvert\lambda\_{i}\rvert\bar{P}\_{j}^{i}\geq\gamma\_{i}\lvert\lambda\_{i}\rvert\bar{P}\_{j}^{i}\geq\gamma\_{i}\lvert\lambda\_{i}\rvert\bar{P}\_{j}^{i}-\mu\_{j}^{i}. |  | (3.46) |
* •

  If x¯ji=Rji\bar{x}\_{j}^{i}=R\_{j}^{i} and y¯ji=0\bar{y}\_{j}^{i}=0, then this situation cannot hold for every asset, that is, there exists k≠jk\neq j such that xki=Rkix\_{k}^{i}=R\_{k}^{i}. Indeed, if otherwise x¯i=Ri\bar{x}^{i}=R^{i}, then φi​(Ri)=φi​(0)\varphi\_{i}(R^{i})=\varphi\_{i}(0), which contradicts ([3.6](#S3.E6 "In 3rd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")). This implies λi≤0\lambda\_{i}\leq 0.

  Since in this case, ([3.34](#S3.E34 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and ([3.35](#S3.E35 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) are equivalent to

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | −∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji−λi​P¯ji\displaystyle-\sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}-\lambda\_{i}\bar{P}\_{j}^{i} | ≤\displaystyle\leq | 0,\displaystyle 0, |  |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | ∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji+γi​λi​P¯ji+μji\displaystyle\sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}+\gamma\_{i}\lambda\_{i}\bar{P}\_{j}^{i}+\mu\_{j}^{i} | ≥\displaystyle\geq | 0,\displaystyle 0, |  |

  then, the condition reduces to

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∑k=1nDk​u​(A​(𝐱¯−𝐲¯))​Ak​ji≥|λi|​P¯ji.\sum\_{k=1}^{n}D\_{k}u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))A\_{kj}^{i}\geq|\lambda\_{i}|\bar{P}\_{j}^{i}. |  | (3.47) |

Finally, relation (LABEL:KKT\_etai\_1) follows from ([3.42](#S3.E42 "In 1st item ‣ Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), ([3.44](#S3.E44 "In 2nd item ‣ Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), ([3.46](#S3.E46 "In 3rd item ‣ Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), ([3.47](#S3.E47 "In 4th item ‣ Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), and condition ([3.34](#S3.E34 "In Proof. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")).
∎

We analyze the KKT conditions of Theorem [3.1](#S3.Thmthr1 "Theorem 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") below.

###### Remark 3.2.

Some useful insights can be derived from the KKT conditions. Consider, for instance, part (a) of Theorem [3.1](#S3.Thmthr1 "Theorem 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"). Under the same assumptions as in this theorem, the optimality system yields the following bound for the multipliers:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μji≤qibji,∀j∈{1,…,ni},∀i∈{1,…,m}.\mu\_{j}^{i}\leq\frac{q\_{i}}{b\_{j}^{i}},~\forall~j\in\{1,\dots,n\_{i}\},~\forall~i\in\{1,\dots,m\}. |  | (3.48) |

The core result of part (a) of Theorem [3.1](#S3.Thmthr1 "Theorem 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") is equation ([3.26](#S3.E26 "In item (a) ‣ Theorem 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), which characterizes the optimality of refraining from trading entirely. From this condition, it becomes clear that the no-trade region expands with larger positive values of the multipliers. Moreover, inequality ([3.48](#S3.E48 "In Remark 3.2. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) shows that each multiplier is bounded above by a constant proportional to the gas fee and inversely proportional to the activation bound. Therefore, the gas fees enlarge the no-trading region, which is a reasonable effect. Further discussion on the conditions that favor no trading will be continued in Section [4](#S4 "4 No-trade Characterization with Gas Fees ‣ Optimal Routing across Constant Function Market Makers with Gas Fees").

Furthermore, part (b) of Theorem [3.1](#S3.Thmthr1 "Theorem 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") corresponds to the case η¯i>0\bar{\eta}\_{i}>0. There, the KKT condition (μi)⊤​(y¯i−η¯i​bi)=0(\mu^{i})^{\top}(\bar{y}^{i}-\bar{\eta}\_{i}b^{i})=0 is equivalent to

|  |  |  |
| --- | --- | --- |
|  | μji​y¯ji=μji​η¯i​bji,\mu\_{j}^{i}\bar{y}\_{j}^{i}=\mu\_{j}^{i}\bar{\eta}\_{i}b\_{j}^{i}, |  |

Consequently, the optimal trades associated with strictly positive
multipliers are determined,

|  |  |  |  |
| --- | --- | --- | --- |
|  | μji>0⟹y¯ji=η¯i​bji.\mu\_{{j}}^{i}>0~\Longrightarrow~\bar{y}\_{{j}}^{i}=\bar{\eta}\_{{i}}b\_{{j}}^{i}. |  | (3.49) |

###### Remark 3.3.

The technical assumption ([3.16](#S3.E16 "In Proposition 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) has important financial consequences:

* (i)(i)

  Integer Solution Penalty: The condition 𝐛−𝐲¯>0\mathbf{b}-\mathbf{\bar{y}}>0 in ([3.16](#S3.E16 "In Proposition 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) penalizes integer solutions when η¯i,\bar{\eta}\_{i}, qi>0q\_{i}>0, since it necessarily implies η¯i≠1\bar{\eta}\_{i}\neq 1 for all i∈{1,…,m}i\in\{1,\ldots,m\}. In this sense, under assumption ([3.16](#S3.E16 "In Proposition 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), every solution (𝐱¯,𝐲¯,η¯)∈𝐒^(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\in\mathbf{\hat{S}} of problem ([𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)](#S3.Ex2 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) is a KKT point by Theorem [3.1](#S3.Thmthr1 "Theorem 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"). Therefore, if η¯i>0\bar{\eta}\_{i}>0, it follows from ([3.49](#S3.E49 "In Remark 3.2. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) that η¯i≠1\bar{\eta}\_{{i}}\neq 1 (unless μi=0\mu^{i}=0). In this case qi=0q\_{i}=0 by condition (LABEL:KKT\_etai\_1), which corresponds to a market with no gas fee. Hence, for a market with a gas fee and trade, necessarily η¯i≠1\bar{\eta}\_{{i}}\neq 1 and at least one trade satisfies y¯ji=η¯i​bji\bar{y}\_{{j}}^{i}=\bar{\eta}\_{i}b\_{j}^{i}. However, let us emphasize that this does not necessarily imply that all positive trades are saturated, i.e., y¯ji=η¯i​bji\bar{y}\_{{j}}^{i}=\bar{\eta}\_{{i}}b\_{{j}}^{i}; in fact, numerical examples show situations with trades y¯ji∈(0,η¯i​bji)\bar{y}\_{{j}}^{i}\in(0,\bar{\eta}\_{i}b\_{{j}}^{i}).
* (i​i)(ii)

  Tender Size Limit: The condition bji−y¯ji≤2γi​Rjib\_{j}^{i}-\bar{y}\_{j}^{i}\leq\frac{2}{\gamma\_{i}}R\_{j}^{i} imposes an upper bound on the maximum tender size. This holds particularly when bi≤2γi​Rib^{i}\leq\frac{2}{\gamma\_{i}}R^{i}.

### 3.2 Sufficient Optimality Conditions

We provide sufficient conditions without convexity assumptions neither on the utility function uu nor the trade functions φi\varphi\_{i}. To that end, let K⊆ℝnK\subseteq\mathbb{R}^{n} and C⊆ℝmC\subseteq\mathbb{R}^{m} be two nonempty sets and g:ℝn→ℝmg:\mathbb{R}^{n}\rightarrow\mathbb{R}^{m} be a differentiable mapping.

It is said that gg is CC-quasiconvex at x¯∈K\overline{x}\in K with respect to KK if for all x∈Kx\in K (see [[26](#bib.bib26), Definition 5.12]), the following implication holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(x)−g​(x¯)∈C⟹∇g​(x¯)​(x−x¯)∈C.g(x)-g(\bar{x})\in C~\Longrightarrow~\nabla g(\bar{x})(x-\bar{x})\in C. |  | (3.50) |

A sufficient optimality condition is given in the next result.

###### Theorem 3.2.

Assume that ff is pseudoconcave (thus −f-f is pseudoconvex) and φi\varphi\_{i} is quasilinear for every i=1,…,mi=1,\ldots,m. If (𝐱¯,𝐲¯,η¯)∈𝐒^(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\in\mathbf{\hat{S}} verifies optimality system ([3.26](#S3.E26 "In item (a) ‣ Theorem 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and (LABEL:KKT\_etai\_1), then it solves problem ([𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)](#S3.Ex6 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")).

###### Proof.

We apply [[26](#bib.bib26), Corollary 5.15]. In first place, given the set

|  |  |  |
| --- | --- | --- |
|  | C^:=(ℝ−\{0})×(−(∏i=1mℝ+ni)+cone({G​(𝐱¯,𝐲¯,η¯)})−cone({G​(𝐱¯,𝐲¯,η¯)}))×{0},\widehat{C}:=(\mathbb{R}\_{-}\backslash\{0\})\times\!\left(\!-\!\left(\prod\limits\_{i=1}^{m}\mathbb{R}\_{+}^{n\_{i}}\!\right)\!+\operatornamewithlimits{cone}(\{G(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\})-\operatornamewithlimits{cone}(\{G(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\})\!\right)\times\{0\}, |  |

let us prove that (−f,G,H)(-f,G,H) is C^\widehat{C}-quasiconvex at (𝐱¯,𝐲¯,η¯)(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta}) with respect to 𝐒^\mathbf{\hat{S}}. That is, we will prove that for every (𝐱,𝐲,η)∈𝐒^\left(\mathbf{x},\mathbf{y},\eta\right)\in\mathbf{\hat{S}}, we have

|  |  |  |
| --- | --- | --- |
|  | (−f,G,H)​(𝐱,𝐲,η)−(−f,G,H)​(𝐱¯,𝐲¯,η¯)∈C^\displaystyle\hskip 25.6073pt(-f,G,H)(\mathbf{x},\mathbf{y},\eta)-(-f,G,H)(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\in\widehat{C} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟹∇(−f,G,H)​(𝐱¯,𝐲¯,η¯)​(𝐱−𝐱¯,𝐲−𝐲¯,η−η¯)∈C^.\displaystyle\Longrightarrow~\nabla(-f,G,H)(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\left(\mathbf{x-\bar{x}},\mathbf{y-\bar{y}},\eta-\bar{\eta}\right)\in\widehat{C}. |  | (3.51) |

Relation ([3.51](#S3.E51 "In Proof. ‣ 3.2 Sufficient Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) can be expressed by components as follows:

* (i)(i)

  If −f​(𝐱,𝐲,η)+f​(𝐱¯,𝐲¯,η¯)∈ℝ−\{0}-f(\mathbf{x},\mathbf{y},\eta)+f(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\in\mathbb{R}\_{-}\backslash\{0\}, then

  |  |  |  |
  | --- | --- | --- |
  |  | −∇f​(𝐱¯,𝐲¯,η¯)​(𝐱−𝐱¯,𝐲−𝐲¯,η−η¯)∈ℝ−\{0}.-\nabla f(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\left(\mathbf{x-\bar{x}},\mathbf{y-\bar{y}},\eta-\bar{\eta}\right)\in\mathbb{R}\_{-}\backslash\{0\}. |  |
* (i​i)(ii)

  If

  |  |  |  |
  | --- | --- | --- |
  |  | Gi​(𝐱,𝐲,η)−Gi​(𝐱¯,𝐲¯,η¯)∈\displaystyle G\_{i}(\mathbf{x},\mathbf{y},\eta)-G\_{i}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\in |  |
  |  |  |  |
  | --- | --- | --- |
  |  | −(∏i=1mℝ+ni)+cone({Gi​(𝐱¯,𝐲¯,η¯)})−cone({Gi​(𝐱¯,𝐲¯,η¯)}),\displaystyle-\left(\prod\limits\_{i=1}^{m}\mathbb{R}\_{+}^{n\_{i}}\right)+\operatornamewithlimits{cone}(\{G\_{i}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\})-\operatornamewithlimits{cone}(\{G\_{i}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\}), |  |

  then

  |  |  |  |
  | --- | --- | --- |
  |  | ∇Gi​(𝐱¯,𝐲¯,η¯)​(𝐱−𝐱¯,𝐲−𝐲¯,η−η¯)∈\displaystyle\nabla G\_{i}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})(\mathbf{x-\bar{x}},\mathbf{y-\bar{y}},\eta-\bar{\eta})\in |  |
  |  |  |  |
  | --- | --- | --- |
  |  | −(∏i=1mℝ+ni)+cone({Gi​(𝐱¯,𝐲¯,η¯)})−cone({Gi​(𝐱¯,𝐲¯,η¯)})\displaystyle-\left(\prod\limits\_{i=1}^{m}\mathbb{R}\_{+}^{n\_{i}}\right)+\operatornamewithlimits{cone}(\{G\_{i}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\})-\operatornamewithlimits{cone}(\{G\_{i}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\}) |  |

  for every i=1,…,mi=1,\ldots,m.
* (i​i​i)(iii)

  If Hi​(𝐱,𝐲,η)=Hi​(𝐱¯,𝐲¯,η¯)H\_{i}(\mathbf{x},\mathbf{y},\eta)=H\_{i}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta}), then ∇Hi​(𝐱¯,𝐲¯,η¯)​(𝐱−𝐱¯,𝐲−𝐲¯,η−η¯)=0\nabla H\_{i}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})(\mathbf{x}-{\bf\bar{x}},\mathbf{y}-{\bf\bar{y}},\eta-\bar{\eta})=0 for every i=1,…,mi=1,\ldots,m.

Then, let us prove the previous conditions one by one:

* (i)(i):

  Let (𝐱,𝐲,η)∈𝐒^(\mathbf{x},\mathbf{y},\eta)\in\mathbf{\hat{S}} (𝐱≠𝐲\mathbf{x}\neq\mathbf{y} always). Then, since ff is pseudoconcave

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | −f​(𝐱,𝐲,η)+f​(𝐱¯,𝐲¯,η¯)\displaystyle-f(\mathbf{x},\mathbf{y},\eta)+f(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta}) | ∈−ℝ−\{0}⟺−f​(𝐱¯,𝐲¯,η¯)>−f​(𝐱,𝐲,η)\displaystyle\,\in-\mathbb{R}\_{-}\backslash\{0\}\Longleftrightarrow-f(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})>-f(\mathbf{x},\mathbf{y},\eta) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ⟹([2.3](#S2.E3 "In 2 Preliminaries ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"))−∇f​(𝐱¯,𝐲¯,η¯)​(𝐱−𝐱¯,𝐲−𝐲¯,η−η¯)<0\displaystyle\overset{\eqref{pseudoconvex}}{\Longrightarrow}-\nabla f(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})(\mathbf{x-\bar{x}},\mathbf{y-\bar{y}},\eta-\bar{\eta})<0 |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ⟺−∇f​(𝐱¯,𝐲¯,η¯)​(𝐱−𝐱¯,𝐲−𝐲¯,η−η¯)∈−ℝ−\{0},\displaystyle\Longleftrightarrow-\nabla f(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})(\mathbf{x-\bar{x}},\mathbf{y-\bar{y}},\eta-\bar{\eta})\in-\mathbb{R}\_{-}\backslash\{0\}, |  |

  thus (i)(i) holds.
* (i​i)(ii):

  Let (𝐱,𝐲,η)∈𝐒^(\mathbf{x},\mathbf{y},\eta)\in\mathbf{\hat{S}}. Since GiG\_{i} is convex (affine), we have

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∇Gi​(𝐱¯,𝐲¯,η¯)​(𝐱−𝐱¯,𝐲−𝐲¯,η−η¯)\displaystyle\nabla G\_{i}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})(\mathbf{x-\bar{x}},\mathbf{y-\bar{y}},\eta-\bar{\eta}) | =Gi​(𝐱,𝐲,η)−Gi​(𝐱¯,𝐲¯,η¯)\displaystyle=G\_{i}(\mathbf{x},\mathbf{y},\eta)-G\_{i}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta}) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =yi−y¯i−(ηi−η¯i)​bi,\displaystyle=y^{i}-\bar{y}^{i}-\left(\eta\_{i}-\bar{\eta}\_{i}\right)b^{i}, |  |

  for every (𝐱,𝐲,η)∈𝐒^(\mathbf{x},\mathbf{y},\eta)\in\mathbf{\hat{S}}, thus the
  implication is obvious.
* (i​i​i)(iii):

  Let (𝐱,𝐲,η)∈𝐒^(\mathbf{x},\mathbf{y},\eta)\in\mathbf{\hat{S}}. Then, applying the quasilinearity of φi\varphi\_{i}, we have

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | Hi​(𝐱,𝐲,η)=Hi​(𝐱¯,𝐲¯,η¯)⟺φi​(Ri+γi​yi−xi)=φi​(Ri+γi​y¯i−x¯i)\displaystyle H\_{i}(\mathbf{x},\mathbf{y},\eta)=H\_{i}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\,\Longleftrightarrow\varphi\_{i}(R^{i}+\gamma\_{i}y^{i}-x^{i})=\varphi\_{i}(R^{i}+\gamma\_{i}\bar{y}^{i}-\bar{x}^{i}) |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ⟹([2.2](#S2.E2 "In item (⁢ii) ‣ 2 Preliminaries ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"))​∇φi​(Ri+γi​y¯i−x¯i)​(γi​(yi−y¯i)−(xi−x¯i))=0\displaystyle\overset{\eqref{char:quasilinear}}{\Longrightarrow}\nabla\varphi\_{i}(R^{i}+\gamma\_{i}\bar{y}^{i}-\bar{x}^{i})(\gamma\_{i}(y^{i}-\bar{y}^{i})-(x^{i}-\bar{x}^{i}))=0 |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ⟺γi​∇φi​(Ri+γi​y¯i−x¯i)​(yi−y¯i)−∇φi​(Ri+γi​y¯i−x¯i)​(xi−x¯i)=0\displaystyle\Longleftrightarrow\gamma\_{i}\nabla\varphi\_{i}(R^{i}+\gamma\_{i}\bar{y}^{i}-\bar{x}^{i})(y^{i}-\bar{y}^{i})-\nabla\varphi\_{i}(R^{i}+\gamma\_{i}\bar{y}^{i}-\bar{x}^{i})(x^{i}-\bar{x}^{i})=0 |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ⟺∇Hi​(𝐱¯,𝐲¯,η¯)​(𝐱−𝐱¯,𝐲−𝐲¯,η−η¯)=0,\displaystyle\Longleftrightarrow\nabla H\_{i}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})(\mathbf{x-\bar{x}},\mathbf{y-\bar{y}},\eta-\bar{\eta})=0, |  |

  and (i​i​i)(iii) holds.

Therefore, (−f,G,H)(-f,G,H) is C^\widehat{C}-quasiconvex at (𝐱¯,𝐲¯,η¯)(\mathbf{\bar{x},\bar{y},}\bar{\eta}) and, consequently, if KKT conditions ([3.26](#S3.E26 "In item (a) ‣ Theorem 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and (LABEL:KKT\_etai\_1) are verified for that point, then the point (𝐱¯,𝐲¯,η¯)(\mathbf{\bar{x},\bar{y},}\bar{\eta}) is optimal for problem ([𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)](#S3.Ex6 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) by [[26](#bib.bib26), Corollary 5.15].
∎

As a consequence of Theorems [3.1](#S3.Thmthr1 "Theorem 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") and [3.2](#S3.Thmthr2 "Theorem 3.2. ‣ 3.2 Sufficient Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") we can establish a general characterization of optimal points for problem ([𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)](#S3.Ex2 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")).

###### Theorem 3.3.

Assume that properties ([3.3](#S3.E3 "In 1st item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), ([3.5](#S3.E5 "In 3rd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), and ([3.6](#S3.E6 "In 3rd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) are verified, ff is pseudoconcave, and φi\varphi\_{i} is quasilinear for every i=1,…,mi=1,\ldots,m. Suppose that (𝐱¯,𝐲¯,η¯)∈𝐒^(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\in\mathbf{\hat{S}} satisfies ([3.4](#S3.E4 "In 2nd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and ([3.16](#S3.E16 "In Proposition 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")). Then, the following assertions are equivalent:

* (a)(a)

  (𝐱¯,𝐲¯,η¯)(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta}) solves problem ([𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)](#S3.Ex6 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")).
* (b)(b)

  (𝐱¯,𝐲¯,η¯)(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta}) verifies the optimality system ([3.26](#S3.E26 "In item (a) ‣ Theorem 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and (LABEL:KKT\_etai\_1).

In the next remark, we analyze the scope of the approximate problem (𝒫r​(𝐛,q))(\mathcal{P}^{r}(\mathbf{b},q)) in relation to problem (𝒫​(𝐛,q))(\mathcal{P}(\mathbf{b},q)).

###### Remark 3.4.

The approximate solution (𝐱¯,𝐲¯,η¯)∈𝐒(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\in\mathbf{S} to the relaxed problem (𝒫r​(𝐛,q))(\mathcal{P}^{r}(\mathbf{b},q)) differs
from a solution (𝐱~,𝐲~,η~)(\mathbf{\tilde{x}},\mathbf{\tilde{y}},\tilde{\eta}) of
the original problem (𝒫​(𝐛,q))(\mathcal{P}(\mathbf{b},q)) in different aspects. For
instance, this approximation could not incorporate the fixed gas fee penalty because η¯i\bar{\eta}\_{i} does not necessarily belong to {0,1}\{0,1\}. In fact, if equation ([3.16](#S3.E16 "In Proposition 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) is satisfied, then we saw in Remark [3.3](#S3.Thmremark3 "Remark 3.3. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") that η¯i<1\bar{\eta}\_{i}<1 for all i∈{1,…,m}i\in\{1,\ldots,m\}. In this case, the associated fee ∑i=1mqi​η¯i\sum\_{i=1}^{m}q\_{i}\bar{\eta}\_{i} does not match the true fee ∑η~i>0qi\sum\_{\tilde{\eta}\_{i}>0}q\_{i}, which can lead to utility trade-offs.

To properly compare these solutions, let us consider any feasible point

|  |  |  |
| --- | --- | --- |
|  | (𝐱,𝐲,η)∈∏i=1m[0,Ri]×∏i=1m[0,bi]×{0,1}m(\mathbf{x},\mathbf{y},\eta)\in\prod\_{i=1}^{m}[0,R^{i}]\times\prod\_{i=1}^{m}[0,b^{i}]\times\left\{0,1\right\}^{m} |  |

of (𝒫​(𝐛,q))(\mathcal{P}(\mathbf{b},q)), which by construction is also feasible for
(𝒫r​(𝐛,q))(\mathcal{P}^{r}(\mathbf{b},q)). For such points, the following inequality
holds:

|  |  |  |
| --- | --- | --- |
|  | −u​(A​(𝐱¯−𝐲¯))+∑i=1mqi​η¯i≤−u​(A​(𝐱−𝐲))+∑i=1mqi​ηi.-u(A(\mathbf{\bar{x}-\bar{y}}))+\sum\_{i=1}^{m}q\_{i}\bar{\eta}\_{i}\leq-u(A(\mathbf{x-y}))+\sum\_{i=1}^{m}q\_{i}\eta\_{i}. |  |

That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −u​(A​(𝐱¯−𝐲¯))\displaystyle-u(A(\mathbf{\bar{x}-\bar{y}})) | −(−u​(A​(𝐱−𝐲)))≤∑i=1mqi​(ηi−η¯i)=∑ηi>0qi​(1−η¯i)−∑ηi=0qi​η¯i\displaystyle\,-(-u(A(\mathbf{x-y})))\leq\sum\_{i=1}^{m}q\_{i}\left(\eta\_{i}-\bar{\eta}\_{i}\right)=\sum\_{\eta\_{i}>0}q\_{i}\left(1-\bar{\eta}\_{i}\right)-\sum\_{\eta\_{i}=0}q\_{i}\bar{\eta}\_{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤qmax​∑ηi>01−qmin​∑i=1mη¯i=qmax​‖η‖0−qmin​‖η¯‖1\displaystyle\leq q\_{\max}\sum\_{\eta\_{i}>0}1-q\_{\min}\sum\_{i=1}^{m}\bar{\eta}\_{i}\,=\,q\_{\max}\|\eta\|\_{0}-q\_{\min}\|\bar{\eta}\|\_{1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =qmax​(‖η‖0−‖η¯‖1)+(qmax−qmin)​‖η¯‖1,\displaystyle=q\_{\max}(\|\eta\|\_{0}-\|\bar{\eta}\|\_{1})+(q\_{\max}-q\_{\min})\|\bar{\eta}\|\_{1}, |  |

where qmax=maxi=1,…,m​qiq\_{\max}=\underset{i=1,\ldots,m}{\max}q\_{i}, qmin=mini=1,…,m​qiq\_{\min}=\underset{i=1,\ldots,m}{\min}q\_{i}, ‖η‖0=#​{i:ηi>0}\|\eta\|\_{0}=\#\{i:\eta\_{i}>0\} is
the ℓ0\ell\_{0} pseudo-norm, and ‖η‖1=∑i=1m|ηi|\|\eta\|\_{1}=\sum\_{i=1}^{m}|\eta\_{i}| is the ℓ1\ell\_{1}-norm. In terms of maximizing the utility, this
corresponds to

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(A​(𝐱¯−𝐲¯))≥u​(A​(𝐱−𝐲))−(qmax​(‖η‖0−‖η¯‖1)+(qmax−qmin)​‖η¯‖1).u(A(\mathbf{\bar{x}-\bar{y}}))\geq u(A(\mathbf{x-y}))-(q\_{\max}(\|\eta\|\_{0}-\|\bar{\eta}\|\_{1})+(q\_{\max}-q\_{\min})\|\bar{\eta}\|\_{1}). |  | (3.52) |

This holds for every (𝐱,𝐲,η)(\mathbf{x},\mathbf{y},\eta). In particular, we can take (𝐱,𝐲)(\mathbf{x},\mathbf{y}) to be the solution to the following utility maximization problem, which considers the active markets given by η\eta, that is,

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | maximize |  | u​(Ψ)\displaystyle u(\Psi) |  | (𝒫η​(𝐛,q){\mathcal{P}}^{\eta}({\mathbf{b}},q)) |
|  |  | subject to |  | Ψ=∑i=1mAi​(xi−yi),\displaystyle\Psi=\sum\_{i=1}^{m}A^{i}(x^{i}-y^{i}), |  |
|  |  | yi≤𝟏{η>0}​bi,\displaystyle y^{i}\leq\mathbf{1}\_{\{\eta>0\}}b^{i}, |  | | |
|  |  | φi​(Ri+γi​yi−xi)=φi​(Ri),\displaystyle\varphi\_{i}(R^{i}+\gamma\_{i}y^{i}-x^{i})=\varphi\_{i}(R^{i}), |  | | |
|  |  | 0≤xi≤Ri,0≤yi,∀i∈{1,…,m},\displaystyle 0\leq x^{i}\leq R^{i},\quad 0\leq y^{i},\ \forall~i\in\{1,\ldots,m\}, |  | | |

where

|  |  |  |
| --- | --- | --- |
|  | 1{η>0}:={1ηi>0,0otherwise.1\_{\{\eta>0\}}:=\left\{\begin{array}[]{cc}1&\eta\_{i}>0,\\ 0&\text{otherwise.}\end{array}\right. |  |

If ε=qmax​(‖η‖0−‖η¯‖1)+(qmax−qmin)​‖η¯‖1>0\varepsilon=q\_{\max}(\|\eta\|\_{0}-\|\bar{\eta}\|\_{1})+(q\_{\max}-q\_{\min})\|\bar{\eta}\|\_{1}>0, then (𝐱¯,𝐲¯)(\mathbf{\bar{x}},\mathbf{\bar{y}}) corresponds to an ε\varepsilon-approximate solution of the problem. If ε≤0\varepsilon\leq 0, then the solution corresponds to the exact case. Let (𝐱~,𝐲~)(\mathbf{\tilde{x}},\mathbf{\tilde{y}}) denotes the solution to problem (𝒫η¯​(𝐛,q))(\mathcal{P}^{\bar{\eta}}(\mathbf{b},q)), that is, we allow transactions provided that η¯i>0\bar{\eta}\_{i}>0. Then,
by ([3.52](#S3.E52 "In Remark 3.4. ‣ 3.2 Sufficient Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(A​(𝐱~−𝐲~))≥u​(A​(𝐱¯−𝐲¯))≥u​(A​(𝐱~−𝐲~))−ε​(q,η¯),u(A(\mathbf{\tilde{x}}-\mathbf{\tilde{y}}))\geq u(A(\mathbf{\bar{x}}-\mathbf{\bar{y}}))\geq u(A(\mathbf{\tilde{x}}-\mathbf{\tilde{y}}))-\varepsilon(q,\bar{\eta})\ , |  | (3.53) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ε​(q,η¯):=qmax​(‖η¯‖0−‖η¯‖1)+(qmax−qmin)​‖η¯‖1.\varepsilon(q,\bar{\eta}):=q\_{\max}(\|\bar{\eta}\|\_{0}-\|\bar{\eta}\|\_{1})+(q\_{\max}-q\_{\min})\|\bar{\eta}\|\_{1}. |  | (3.54) |

As ‖η¯‖∞≤1\|\bar{\eta}\|\_{\infty}\leq 1, ‖η¯‖0−‖η¯‖1≥0\|\bar{\eta}\|\_{0}-\|\bar{\eta}\|\_{1}\geq 0 since each |η¯i|≤1|\bar{\eta}\_{i}|\leq 1 implies ‖η¯‖1≤‖η¯‖0\|\bar{\eta}\|\_{1}\leq\|\bar{\eta}\|\_{0}, therefore ε​(q,η¯)≥0\varepsilon(q,\bar{\eta})\geq 0 and (𝐱¯,𝐲¯)(\mathbf{\bar{x}},\mathbf{\bar{y}}) constitutes an ε​(q,η¯)\varepsilon(q,\bar{\eta})-approximate solution to (𝒫η¯​(𝐛,q))(\mathcal{P}^{\bar{\eta}}(\mathbf{b},q)). Depending on the magnitude of ε​(q,η¯)\varepsilon(q,\bar{\eta}), this approximate solution may be acceptable for problem (𝒫η¯​(𝐛,q))(\mathcal{P}^{\bar{\eta}}(\mathbf{b},q)).

We formalize this observation in the following result.

###### Theorem 3.4.

Let (𝐱˘,𝐲˘,η˘)∈∏i=1m[0,Ri]×∏i=1m[0,bi]×{0,1}m(\mathbf{\breve{x}},\mathbf{\breve{y}},\breve{\eta})\in\prod\_{i=1}^{m}[0,R^{i}]\times\prod\_{i=1}^{m}[0,b^{i}]\times\{0,1\}^{m} and (𝐱¯,𝐲¯,η¯)∈∏i=1m[0,Ri]×∏i=1m[0,bi]×[0,1]m(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\in\prod\_{i=1}^{m}[0,R^{i}]\times\prod\_{i=1}^{m}[0,b^{i}]\times[0,1]^{m} be solutions to the problems (𝒫r​(𝐛,q))(\mathcal{P}^{r}(\mathbf{b},q)) and
(𝒫​(𝐛,q))(\mathcal{P}(\mathbf{b},q)), respectively. Let (𝐱~,𝐲~,1{η¯>0})∈∏i=1m[0,Ri]×∏i=1m[0,bi]×{0,1}m(\mathbf{\tilde{x}},\mathbf{\tilde{y}},1\_{\left\{\bar{\eta}>0\right\}})\in\prod\_{i=1}^{m}[0,R^{i}]\times\prod\_{i=1}^{m}[0,b^{i}]\times\{0,1\}^{m} where (𝐱~,𝐲~)(\mathbf{\tilde{x}},\mathbf{\tilde{y}}) corresponds to solution of problem (𝒫η¯​(𝐛,q))(\mathcal{P}^{\bar{\eta}}(\mathbf{b},q)). Then,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |h​(𝐱~,𝐲~,η¯)−h​(𝐱˘,𝐲˘,η˘)|≤ε​(q,η¯),\left|h(\mathbf{\tilde{x}},\mathbf{\tilde{y}},\bar{\eta})-h(\mathbf{\breve{x}},\mathbf{\breve{y}},\breve{\eta})\right|\leq\varepsilon(q,\bar{\eta}), |  | (3.55) |

where h​(𝐱,𝐲,η):=u​(A​(𝐱−𝐲))−∑ηi>0qih(\mathbf{x},\mathbf{y},\eta):=u(A(\mathbf{x}-\mathbf{y}))-\sum\_{\eta\_{i}>0}q\_{i}, corresponds to the objective functional of problem (𝒫​(𝐛,q))(\mathcal{P}(\mathbf{b},q)), that is, (𝐱~,𝐲~,1{η¯>0})(\mathbf{\tilde{x}},\mathbf{\tilde{y}},1\_{\left\{\bar{\eta}>0\right\}}) is an ε​(q,η¯)\varepsilon(q,\bar{\eta})-approximate solution to problem (𝒫​(𝐛,q))(\mathcal{P}(\mathbf{b},q)), where ε​(q,η¯)=qmax​(‖η¯‖0−‖η¯‖1)+(qmax−qmin)​‖η¯‖1\varepsilon(q,\bar{\eta})=q\_{\max}\left(\|\bar{\eta}\|\_{0}-\|\bar{\eta}\|\_{1}\right)+\left(q\_{\max}-q\_{\min}\right)\|\bar{\eta}\|\_{1}.

###### Proof.

Taking into account the optimality of (𝐱¯,𝐲¯,η¯)(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta}) and (𝐱˘,𝐲˘,η˘)(\mathbf{\breve{x}},\mathbf{\breve{y}},\breve{\eta}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(A​(𝐱¯−𝐲¯))−∑i=1mη¯i​qi≥u​(A​(𝐱˘−𝐲˘))−∑η˘i>0qi≥u​(A​(𝐱~−𝐲~))−∑η¯i>0qi,u(A(\mathbf{\bar{x}-\bar{y}}))-\sum\limits\_{i=1}^{m}\bar{\eta}\_{i}q\_{i}\geq u(A(\mathbf{\breve{x}}-\mathbf{\breve{y}}))-\sum\limits\_{\breve{\eta}\_{i}>0}q\_{i}\geq u(A(\mathbf{\tilde{x}-\tilde{y}}))-\sum\limits\_{\bar{\eta}\_{i}>0}q\_{i}, |  | (3.56) |

that we can rewrite

|  |  |  |
| --- | --- | --- |
|  | hr​(𝐱¯,𝐲¯,η¯)≥h​(𝐱˘,𝐲˘,η˘)≥h​(𝐱~,𝐲~,η¯),h^{r}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\geq h(\mathbf{\breve{x}},\mathbf{\breve{y}},\breve{\eta})\geq h(\mathbf{\tilde{x}},\mathbf{\tilde{y}},\bar{\eta}), |  |

where hr​(𝐱¯,𝐲¯,η¯):=u​(A​(𝐱¯−𝐲¯))−∑i=1mη¯i​qi.h^{r}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta}):=u(A(\mathbf{\bar{x}-\bar{y}}))-\sum\limits\_{i=1}^{m}\bar{\eta}\_{i}q\_{i}. From this,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |h(𝐱˘,𝐲˘,η˘)−h(𝐱~,𝐲~,η¯)|≤|hr(𝐱¯,𝐲¯,η¯)−h(𝐱~,𝐲~,η¯)|.|h(\mathbf{\breve{x}},\mathbf{\breve{y}},\breve{\eta})-h(\mathbf{\tilde{x}},\mathbf{\tilde{y}},\bar{\eta})\rvert\leq\lvert h^{r}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})-h(\mathbf{\tilde{x}},\mathbf{\tilde{y}},\bar{\eta})\rvert. |  | (3.57) |

Now, since u​(A​(𝐱¯−𝐲¯))≤u​(A​(𝐱~−𝐲~))u(A(\mathbf{\bar{x}-\bar{y}}))\leq u(A(\mathbf{\tilde{x}-\tilde{y}})), we get

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |hr​(𝐱¯,𝐲¯,η¯)−h​(𝐱~,𝐲~,η¯)|\displaystyle\left|h^{r}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})-h(\mathbf{\tilde{x}},\mathbf{\tilde{y}},\bar{\eta})\right| | =\displaystyle= | hr​(𝐱¯,𝐲¯,η¯)−h​(𝐱~,𝐲~,η¯)\displaystyle h^{r}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})-h(\mathbf{\tilde{x}},\mathbf{\tilde{y}},\bar{\eta}) |  |
|  |  | =\displaystyle= | u​(A​(𝐱¯−𝐲¯))−u​(A​(𝐱~−𝐲~))+∑η¯i>0qi−∑η¯i>0η¯i​qi\displaystyle u(A(\mathbf{\bar{x}-\bar{y}}))-u(A(\mathbf{\tilde{x}-\tilde{y}}))+\sum\limits\_{\bar{\eta}\_{i}>0}q\_{i}-\sum\limits\_{\bar{\eta}\_{i}>0}\bar{\eta}\_{i}q\_{i} |  |
|  |  | ≤\displaystyle\leq | ∑η¯i>0(1−η¯i)​qi\displaystyle\sum\limits\_{\bar{\eta}\_{i}>0}(1-\bar{\eta}\_{i})q\_{i} |  |

From Remark [3.4](#S3.Thmremark4 "Remark 3.4. ‣ 3.2 Sufficient Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"), ∑η¯i>0(1−η¯i)​qi≤ε​(q,η¯)\sum\limits\_{\bar{\eta}\_{i}>0}(1-\bar{\eta}\_{i})q\_{i}\leq\varepsilon(q,\bar{\eta}), using ([3.57](#S3.E57 "In Proof. ‣ 3.2 Sufficient Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"))
we finally get

|  |  |  |
| --- | --- | --- |
|  | |hr​(𝐱¯,𝐲¯,η¯)−h​(𝐱~,𝐲~,η¯)|≤ε​(q,η¯).\left|h^{r}(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})-h(\mathbf{\tilde{x}},\mathbf{\tilde{y}},\bar{\eta})\right|\leq\varepsilon(q,\bar{\eta}). |  |

∎

We finish this section with the following remark regarding the technical assumption of pseudoconvexity for the composition function f=−u∘Af=-u\circ A.

###### Remark 3.5.

In Theorems [3.2](#S3.Thmthr2 "Theorem 3.2. ‣ 3.2 Sufficient Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") and [3.3](#S3.Thmthr3 "Theorem 3.3. ‣ 3.2 Sufficient Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"), we are assuming that
the function f​(𝐱,𝐲,η)=−u∘A​(𝐱−𝐲)+⟨q,η⟩f(\mathbf{x},\mathbf{y},\eta)=-u\circ A(\mathbf{x}-\mathbf{y})+\langle q,\eta\rangle is pseudoconvex. This assumption is not
restrictive as we analyze below. Indeed, simplifying notation, if v:ℝm→v:\mathbb{R}^{m}\rightarrow ℝ\mathbb{R} is pseudoconvex (v≡−uv\equiv-u) and A:ℝn→ℝmA:\mathbb{R}^{n}\rightarrow\mathbb{R}^{m} is a linear operator, then the
function h:=v∘Ah:=v\circ A is pseudoconvex. Let x1,x2∈ℝmx\_{1},x\_{2}\in\mathbb{R}^{m}
be such that h​(x1)<h​(x2)h(x\_{1})<h(x\_{2}). Then,

|  |  |  |
| --- | --- | --- |
|  | h​(x1)<h​(x2)⟺v​(A​x1)<v​(A​x2)⟹∇v​(A​x2)​(A​x1−A​x2)<0​ (​v​ pseudoconvex)⟹∇v​(A​x2)​A​(x1−x2)<0⟺∇h​(x2)​(x1−x2)<0,\begin{array}[]{ll}h(x\_{1})<h(x\_{2})&\Longleftrightarrow\,v(Ax\_{1})<v(Ax\_{2})\\ &\Longrightarrow\,\nabla v(Ax\_{2})(Ax\_{1}-Ax\_{2})<0\text{ (}v\text{ pseudoconvex)}\\ &\Longrightarrow\,\nabla v(Ax\_{2})A(x\_{1}-x\_{2})<0\\ &\Longleftrightarrow\,\nabla h(x\_{2})(x\_{1}-x\_{2})<0,\end{array} |  |

and h=v∘Ah=v\circ A is pseudoconvex.

## 4 No-trade Characterization with Gas Fees

A no-trade condition prevents arbitrage by ensuring that for every solution (𝐱¯,𝐲¯,η¯)∈𝐒^(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})\in\mathbf{\hat{S}} to problem ([𝒫​(𝐛,q)\mathcal{P}(\mathbf{b},q)](#S3.Ex1 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), we have (𝐱¯,𝐲¯)=(𝟎,𝟎)(\mathbf{\bar{x}},\mathbf{\bar{y}})=(\mathbf{0},\mathbf{0}), which implies that η¯=0\bar{\eta}=0 by Remark [3.1](#S3.Thmremark1 "Remark 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"). As a consequence, we have the following definition of no-trade for the optimal
routing problem.

###### Definition 4.1.

It is said that a no-trade condition is verified in the optimal routing problem when (𝐱¯,𝐲¯,η¯)=(𝟎,𝟎,0)(\mathbf{\bar{x}},\mathbf{\bar{y},\bar{\eta}})=(\mathbf{0},\mathbf{0},0) is the unique solution of ([𝒫​(𝐛,q)\mathcal{P}(\mathbf{b},q)](#S3.Ex1 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")).

Since (𝟎,𝟎,0)(\mathbf{0},\mathbf{0},0) is a feasible solution for problem ([𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)](#S3.Ex6 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), it is indeed a valid solution if the no-trade condition holds.
Therefore, we can apply our earlier analysis to problem ([𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)](#S3.Ex6 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) in order
to derive properties under the assumption that the no-trade condition is
satisfied.

###### Theorem 4.1.

Assume properties
([3.3](#S3.E3 "In 1st item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), ([3.5](#S3.E5 "In 3rd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), and ([3.6](#S3.E6 "In 3rd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) are verified. Consider the following statements:

* (a)(a)

  The no-trade condition is satisfied.
* (b)(b)

  P¯i∈Kiγi,qi,bi\bar{P}^{i}\in K\_{i}^{\gamma\_{i},q\_{i},b^{i}} for every i∈{1,…,m}i\in\{1,\ldots,m\}, where

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Kiγi,qi,bi:={z∈ℝn:αi​z≥(Ai)⊤​∇u​(𝟎)⊤≥γi​αi​z−μi,for some ​(αi,μi)∈ℝ+×ℝ+n​ and ​qi≥(μi)⊤​bi}.K\_{i}^{\gamma\_{i},q\_{i},b^{i}}:=\left\{\begin{array}[]{l}z\in\mathbb{R}^{n}:\,\alpha\_{i}z\geq(A^{i})^{\top}\nabla u(\mathbf{0})^{\top}\geq\gamma\_{i}\alpha\_{i}z-\mu^{i},\\ \text{for some }(\alpha\_{i},\mu^{i})\in\mathbb{R}\_{+}\times\mathbb{R}\_{+}^{n}\text{ and }q\_{i}\geq(\mu^{i})^{\top}b^{i}\end{array}\right\}. |  | (4.1) |

Then, (a)⇒(b)(a)\Rightarrow(b). If, in addition, ff is pseudoconcave and φi\varphi\_{i} is quasilinear for every i=1,…,mi=1,\ldots,m, then (b)⇒(a)(b)\Rightarrow(a).

###### Proof.

(a)⇒(b)(a)\Rightarrow(b): we apply Theorem [3.1](#S3.Thmthr1 "Theorem 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") (the necessary KKT conditions). The point (𝐱¯,𝐲¯,η¯)=(𝟎,𝟎,0)(\mathbf{\bar{x}},\mathbf{\bar{y}},\bar{\eta})=(\mathbf{0},\mathbf{0},0) trivially satisfies ([3.4](#S3.E4 "In 2nd item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) and ([3.16](#S3.E16 "In Proposition 3.1. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), as bi>>0b^{i}>>0 by condition ([3.3](#S3.E3 "In 1st item ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")). In this case, η¯i=0\bar{\eta}\_{i}=0 for every i=1,…,mi=1,\ldots,m.

For a generic i∈{1,…,m}i\in\{1,\ldots,m\}, the following condition holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | {αi​(P¯i)⊤≥∇u​(𝟎)​Ai≥γi​αi​(P¯i)⊤−(μi)⊤,qi−(μi)⊤​bi≥0.\begin{cases}\alpha\_{i}(\bar{P}^{i})^{\top}\geq\nabla u(\mathbf{0})A^{i}\geq\gamma\_{i}\alpha\_{i}(\bar{P}^{i})^{\top}-(\mu^{i})^{\top},\\ q\_{i}-(\mu^{i})^{\top}b^{i}\geq 0.\end{cases} |  | (4.2) |

and this condition is equivalent to ([4.2](#S4.E2 "In Proof. ‣ 4 No-trade Characterization with Gas Fees ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")).

(b)⇒(a)(b)\Rightarrow(a): Directly by applying Theorem [3.2](#S3.Thmthr2 "Theorem 3.2. ‣ 3.2 Sufficient Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") (sufficient KKT conditions).
∎

###### Remark 4.1.

A geometric interpretation of Theorem [4.1](#S4.Thmthr1 "Theorem 4.1. ‣ 4 No-trade Characterization with Gas Fees ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")(b)(b) is that the
set in ([4.1](#S4.E1 "In item (b) ‣ Theorem 4.1. ‣ 4 No-trade Characterization with Gas Fees ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) implies that the prices belong to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pi∈Kiγi+∏j=1n[−qibji,0],∀i∈{1,…,m},P^{i}\in K\_{i}^{\gamma\_{i}}+\prod\_{j=1}^{n}\left[-\frac{q\_{i}}{b\_{j}^{i}},0\right],~\forall~i\in\{1,\ldots,m\}, |  | (4.3) |

where Kiγi:={z∈ℝn:γi​νi​z≤Ai​∇u​(0)≤νi​z, for some ​νi∈ℝ}K\_{i}^{\gamma\_{i}}:=\{z\in\mathbb{R}^{n}:\,\gamma\_{i}\nu\_{i}z\leq A\_{i}\nabla u(0)\leq\nu\_{i}z,\text{ for some }\nu\_{i}\in\mathbb{R}\}. Hence, each price PiP^{i} belongs to the set KiγiK\_{i}^{\gamma\_{i}} perturbed by an interval that depends on the fixed costs qiq\_{i} of the markets and the trade limits bjib\_{j}^{i} for all j∈{1,…,ni}j\in\{1,\ldots,n\_{i}\}.

This can be deduced from the second inequality in ([4.1](#S4.E1 "In item (b) ‣ Theorem 4.1. ‣ 4 No-trade Characterization with Gas Fees ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")). Indeed, from ([4.1](#S4.E1 "In item (b) ‣ Theorem 4.1. ‣ 4 No-trade Characterization with Gas Fees ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) we derive that

|  |  |  |
| --- | --- | --- |
|  | −∑k=1nμki​bki≥−qi⟹−μji≥−qibji+∑k≠jμki​bkibji≥−qibji,∀j=1,…,ni.-\sum\_{k=1}^{n}\mu\_{k}^{i}b\_{k}^{i}\geq-q\_{i}\Longrightarrow-\mu\_{j}^{i}\geq-\frac{q\_{i}}{b\_{j}^{i}}+\sum\_{k\neq j}\mu\_{k}^{i}\frac{b\_{k}^{i}}{b\_{j}^{i}}\geq-\frac{q\_{i}}{b\_{j}^{i}},~\forall~j=1,\ldots,n\_{i}. |  |

Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | αi​(P¯i)⊤≥∇u​(0)​Ai≥γi​αi​(P¯i)⊤−(μi)⊤\displaystyle\alpha\_{i}(\bar{P}^{i})^{\top}\geq\nabla u(0)A^{i}\geq\gamma\_{i}\alpha\_{i}(\bar{P}^{i})^{\top}-(\mu^{i})^{\top} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟹([4.2](#S4.E2 "In Proof. ‣ 4 No-trade Characterization with Gas Fees ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"))\displaystyle\overset{\eqref{no:trade}}{\implies} | αi​P¯ji≥(∇u​(0)​Ai)j≥γi​αi​P¯ji−qibji.\displaystyle\alpha\_{i}\bar{P}\_{j}^{i}\geq(\nabla u(0)A^{i})\_{j}\geq\gamma\_{i}\alpha\_{i}\bar{P}\_{j}^{i}-\frac{q\_{i}}{b\_{j}^{i}}. |  |

Then, ([4.3](#S4.E3 "In Remark 4.1. ‣ 4 No-trade Characterization with Gas Fees ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) holds.

###### Remark 4.2.

To the best of our knowledge, the no-trade characterization for the optimal routing model with gas fees is a novel contribution to the literature, even in the single-market case. Previous works have derived no-trade conditions under different assumptions:

* (i)(i)

  In [[8](#bib.bib8), Section 3], the no-trade condition is established for a convex relaxation of the optimal routing problem without gas fees, so the market conditions were simpler.
* (i​i)(ii)

  For the single-market case, [[5](#bib.bib5)] derives the no-trade condition for the relaxed convex problem, while [[22](#bib.bib22)] extends this result to the original non-convex formulation.

In all cases, our model recovers the no-trade condition when the gas fee is zero, thereby extending the previous results. This also aligns with Remarks [3.2](#S3.Thmremark2 "Remark 3.2. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") and [4.1](#S4.Thmremark1 "Remark 4.1. ‣ 4 No-trade Characterization with Gas Fees ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"), confirming that gas fees introduce an additional term in the no-trade region, consequently expanding it and preventing arbitrage opportunities.

## 5 Interpretations and Numerical Experiments

In this section, we describe two numerical experiments we have performed in order to exemplify our theoretical results. Their outcomes facilitate the financial interpretation of the statements in the previous sections.

###### Example 5.1.

For our first example, we study the influence of the gas fee in the no-trade
region. For that we consider a simple model with a single market m=1m=1, six
tokens n=6n=6, and a linear utility u​(z)=πT​zu(z)=\pi^{T}z based on the one proposed
in [[5](#bib.bib5), Section 5.3], and studied in [[22](#bib.bib22), Section 5.2]. In the present context, we can write the problem as a particular
instance of problem ([𝒫r​(𝐛,q)\mathcal{P}^{r}(\mathbf{b},q)](#S3.Ex2 "In 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), but we omit superscripts for notational
simplification, so it reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maximizeπT​(x−y)−q​ηsubject toy−η​b≤0,φ​(R+γ​y−x)−φ​(R)=0,0≤x≤R, ​0≤yi, ​0≤η≤1.\begin{array}[]{ll}\text{maximize}&\pi^{T}(x-y)-q\eta\\ \text{subject to}&y-\eta b\leq 0,\\ &\varphi(R+\gamma{y}-{x})-\varphi(R)=0,\\ &0\leq x\leq R,\text{ }0\leq{y^{i}},\text{ }0\leq\eta\leq 1.\end{array} |  | (5.1) |

With respect to the model in [[5](#bib.bib5)], three news elements
are considered herein: the activation variable η∈ℝ\eta\in\mathbb{R}, the
gas fee q∈ℝq\in\mathbb{R}, and the tender basket bound b∈ℝ6b\in\mathbb{R}^{6}.
We consider the same data as in the references, a discount rate γ=0.9\gamma=0.9
and a vector of reserves

|  |  |  |
| --- | --- | --- |
|  | R=(1,3,2,5,7,6).R=(1,3,2,5,7,6). |  |

Following Remark [3.3](#S3.Thmremark3 "Remark 3.3. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"), we take b=2​R/γb=2R/\gamma which is
consistent with the theory. The vector π∈ℝ6\pi\in\mathbb{R}^{6} models the
trader private prices and, following the example given in [[22](#bib.bib22)], we assume
that these prices are parametrized by

|  |  |  |
| --- | --- | --- |
|  | π=π​(t,s)≡(t​p1,s​p2,…,p6)​ for some scalars ​t,s∈[0,2],\pi=\pi(t,s)\equiv(tp\_{1},sp\_{2},...,p\_{6})\text{ for some scalars }t,s\in\left[0,2\right], |  |

where the vector of scaled market prices p∈ℝ6\ p\in\mathbb{R}^{6} is given by its components pi=Pi/P6=∇φ​(R)i/∇φ​(R)6p\_{i}=P\_{i}/P\_{6}=\nabla\varphi(R)\_{i}/\nabla\varphi(R)\_{6}. In this way, the market and trader prices coincide for s=t=1s=t=1, so it is expected that the no-trade region is located around this value. We
compare two types of market functions. On one hand, the geometric mean

|  |  |  |
| --- | --- | --- |
|  | φgm​(x)=∏i=1nxi1/n\varphi\_{\mathrm{gm}}(x)=\prod\limits\_{i=1}^{n}x\_{i}^{1/n} |  |

and, on the other, the weighted quasi-arithmetic mean introduced in [[22](#bib.bib22)],

|  |  |  |
| --- | --- | --- |
|  | φqm​(x)=exp⁡(W0​{2n​[∑i=1n(xi+1)2​ln⁡(xi+1)]}/2)−1,\varphi\_{\mathrm{qm}}(x)=\exp\left(W\_{0}\left\{\frac{2}{n}\left[\sum\_{i=1}^{n}(x\_{i}+1)^{2}\ln(x\_{i}+1)\right]\right\}\bigg/2\ \right)-1, |  |

where W0​(⋅)W\_{0}(\cdot) is the principal branch of the Lambert omega function. The motivation to introduce this market function is described in [[22](#bib.bib22)], and is connected to the fact that it is neither convex nor concave.

In both cases, all the hypotheses for the equivalence between (a) and (b) in the statement of Theorem [4.1](#S4.Thmthr1 "Theorem 4.1. ‣ 4 No-trade Characterization with Gas Fees ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") are verified, since uu is increasing and linear, thus pseudoconvex, and φgm\varphi\_{\mathrm{gm}} and φqm\varphi\_{\mathrm{qm}} are increasing and quasilinear, see [[22](#bib.bib22)]. We numerically compute the optimal trades by solving the corresponding problem ([5.1](#S5.E1 "In Example 5.1. ‣ 5 Interpretations and Numerical Experiments ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) for a equispaced grid of points partitioning [0,2]×[0,2]\left[0,2\right]\times\left[0,2\right] and different values of the gas fee; then we identify when the
no-trade condition is verified. Before showing our results, we note that
some parameter values might be unrealistic in practice, as we have selected them for the sake of illustration. Numerical problems are
solved by means of the SciPy optimization library [[32](#bib.bib32)].

The numerical results in Figures [1](#S5.F1 "Figure 1 ‣ 5 Interpretations and Numerical Experiments ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") and [2](#S5.F2 "Figure 2 ‣ 5 Interpretations and Numerical Experiments ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") confirm that gas fees increase the size of the no-trade region in both cases. Comparing the market functions reveals that the weighted quasi-arithmetic mean generates a larger no-trade region for this particular example. In terms of the market activation function η​(t,s)\eta(t,s), the geometric mean produces a smoother profile, while the quasi-arithmetic mean exhibits a piecewise constant, nonsmooth pattern. This difference leads to more frequent market activations (η​(t,s)=1\eta(t,s)=1) in the neighborhood of the no-trade region boundary, as can be seen by comparing Figures [3](#S5.F3 "Figure 3 ‣ 5 Interpretations and Numerical Experiments ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") and [4](#S5.F4 "Figure 4 ‣ 5 Interpretations and Numerical Experiments ‣ Optimal Routing across Constant Function Market Makers with Gas Fees").

###### Example 5.2.

In the second example, we consider an optimal routing problem with m=5m=5
markets and n=3n=3 tokens. In this case, we analyze the linear utility model studied in [[8](#bib.bib8), Section 4]; in particular, we consider
the same network topology, see Figure [6](#S5.F6 "Figure 6 ‣ 5 Interpretations and Numerical Experiments ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"), where the markets (also the market functions and reserves) follow the Roman numbering system. The discount rates are taken to be γi=0.99\gamma\_{i}=0.99, a small value in practice, but we have selected it for the sake of illustrating the no-trade condition. See Table [1](#S5.T1 "Table 1 ‣ 5 Interpretations and Numerical Experiments ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") for these as well as the rest of data. We consider
the specific linear utility problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maximizeπT​(∑i=15Ai​(xi−yi))−∑i=15qi​ηisubject toyi≤ηi​bi,φi​(Ri+γi​yi−xi)=φi​(Ri),0≤xi≤Ri, ​0≤yi,0≤ηi≤1,∀i∈{1,…,5}.\begin{array}[]{ll}\text{maximize}&\pi^{T}\left({\sum\limits\_{i=1}^{5}A^{i}}{(x^{i}-y^{i})}\right)-\sum\limits\_{i=1}^{5}q\_{i}\eta\_{i}\\ \text{subject to}&y^{i}\leq\eta\_{i}b^{i},\\ &\varphi\_{i}(R^{i}+\gamma\_{i}{y^{i}}-{x^{i}})=\varphi\_{i}(R^{i}),\\ &0\leq x^{i}\leq R^{i},\text{ }0\leq{y^{i}},\\ &0\leq\eta\_{i}\leq 1,~\forall~i\in\{1,\ldots,5\}.\end{array} |  | (5.2) |

As in the previous example, we take bi=2​Ri/γib^{i}=2R^{i}/\gamma\_{i}, which is consistent with the theory by Remark [3.3](#S3.Thmremark3 "Remark 3.3. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"). To carry out a similar experiment as before, we consider the following vectors of local prices corresponding to each market:

|  |  |  |
| --- | --- | --- |
|  | P1=(0.16881825,1.68818239,0.16881823),\displaystyle P^{1}=(0.16881825,1.68818239,0.16881823), |  |
|  |  |  |
| --- | --- | --- |
|  | P2=(0.15811388,1.58113882),\displaystyle P^{2}=(0.15811388,1.58113882), |  |
|  |  |  |
| --- | --- | --- |
|  | P3=(1.58113882,0.15811388),\displaystyle P^{3}=(1.58113882,0.15811388), |  |
|  |  |  |
| --- | --- | --- |
|  | P4=(0.79056903,0.3162274),\displaystyle P^{4}=(0.79056903,0.3162274), |  |
|  |  |  |
| --- | --- | --- |
|  | P5=(1,1),\displaystyle P^{5}=(1,1), |  |

which have been numerically calculated. We model the trader private prices for the three different tokens as a uniparametric perturbation of the local price in Market 1, in particular

|  |  |  |
| --- | --- | --- |
|  | π=(t​P11,P21,P31)​ for some ​t∈[0.2,9].\pi=(tP\_{1}^{1},P\_{2}^{1},P\_{3}^{1})\text{ for some }t\in[0.2,9]. |  |

The gas fee is fixed at qi=0.01q\_{i}=0.01. As previously, the assumptions of Theorem [4.1](#S4.Thmthr1 "Theorem 4.1. ‣ 4 No-trade Characterization with Gas Fees ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") are fulfilled, and therefore we can apply it to find out the conditions under which there is no trade. Specifically, setting t=1t=1 and using the geometric approach given by equation ([4.3](#S4.E3 "In Remark 4.1. ‣ 4 No-trade Characterization with Gas Fees ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")), the no-trade condition implies that there exists a vector (α1,α2,α3,α4,α5)∈ℝ+5(\alpha\_{1},\alpha\_{2},\alpha\_{3},\alpha\_{4},\alpha\_{5})\in\mathbb{R}\_{+}^{5} such that the following inequalities hold for each market:

Market 1

|  |  |  |
| --- | --- | --- |
|  | {α1​γ1​P11−q1b11≤P11≤α1​P11,α1​γ1​P21−q2b21≤P21≤α1​P21,α1​γ1​P31−q3b31≤P31≤α1​P31.\begin{cases}\alpha\_{1}\gamma\_{1}P\_{1}^{1}-\frac{q\_{1}}{b\_{1}^{1}}\leq P\_{1}^{1}\leq\alpha\_{1}P\_{1}^{1},\\ \alpha\_{1}\gamma\_{1}P\_{2}^{1}-\frac{q\_{2}}{b\_{2}^{1}}\leq P\_{2}^{1}\leq\alpha\_{1}P\_{2}^{1},\\ \alpha\_{1}\gamma\_{1}P\_{3}^{1}-\frac{q\_{3}}{b\_{3}^{1}}\leq P\_{3}^{1}\leq\alpha\_{1}P\_{3}^{1}.\end{cases} |  |

Market 2

|  |  |  |
| --- | --- | --- |
|  | {α2​γ2​P12−q2b12≤P11≤α2​P12,α2​γ2​P22−q2b22≤P21≤α2​P22.\begin{cases}\alpha\_{2}\gamma\_{2}P\_{1}^{2}-\frac{q\_{2}}{b\_{1}^{2}}\leq P\_{1}^{1}\leq\alpha\_{2}P\_{1}^{2},\\ \alpha\_{2}\gamma\_{2}P\_{2}^{2}-\frac{q\_{2}}{b\_{2}^{2}}\leq P\_{2}^{1}\leq\alpha\_{2}P\_{2}^{2}.\end{cases} |  |

Market 3

|  |  |  |
| --- | --- | --- |
|  | {α3​γ3​P13−q3b13≤P21≤α3​P13,α3​γ3​P23−q3b23≤P31≤α3​P23.\begin{cases}\alpha\_{3}\gamma\_{3}P\_{1}^{3}-\frac{q\_{3}}{b\_{1}^{3}}\leq P\_{2}^{1}\leq\alpha\_{3}P\_{1}^{3},\\ \alpha\_{3}\gamma\_{3}P\_{2}^{3}-\frac{q\_{3}}{b\_{2}^{3}}\leq P\_{3}^{1}\leq\alpha\_{3}P\_{2}^{3}.\end{cases} |  |

Market 4

|  |  |  |
| --- | --- | --- |
|  | {α4​γ4​P14−q4b14≤P11≤α4​P14,α4​γ4​P24−q4b24≤P31≤α4​P24.\begin{cases}\alpha\_{4}\gamma\_{4}P\_{1}^{4}-\frac{q\_{4}}{b\_{1}^{4}}\leq P\_{1}^{1}\leq\alpha\_{4}P\_{1}^{4},\\ \alpha\_{4}\gamma\_{4}P\_{2}^{4}-\frac{q\_{4}}{b\_{2}^{4}}\leq P\_{3}^{1}\leq\alpha\_{4}P\_{2}^{4}.\end{cases} |  |

Market 5

|  |  |  |
| --- | --- | --- |
|  | {α5​γ5​P15−q5b15≤P11≤α5​P15,α5​γ5​P25−q5b25≤P31≤α5​P25.\begin{cases}\alpha\_{5}\gamma\_{5}P\_{1}^{5}-\frac{q\_{5}}{b\_{1}^{5}}\leq P\_{1}^{1}\leq\alpha\_{5}P\_{1}^{5},\\ \alpha\_{5}\gamma\_{5}P\_{2}^{5}-\frac{q\_{5}}{b\_{2}^{5}}\leq P\_{3}^{1}\leq\alpha\_{5}P\_{2}^{5}.\end{cases} |  |

Through direct computation, we verify that the parameter values α1=1\alpha\_{1}=1, α2=α3=P12P22=P12P13≈1.0677\alpha\_{2}=\alpha\_{3}=\frac{P\_{1}^{2}}{P\_{2}^{2}}=\frac{P\_{1}^{2}}{P\_{1}^{3}}\approx 1.0677, α5=P11\alpha\_{5}=P\_{1}^{1} satisfy the no-trade
conditions for Markets 1, 2, 3, and 5, while Market 4 presents an unsolvable condition. The second inequality requires:

|  |  |  |  |
| --- | --- | --- | --- |
|  | α4≥max⁡{P11P14,P31P24}≈0.53385,\alpha\_{4}\geq\max\left\{\frac{P\_{1}^{1}}{P\_{1}^{4}},\frac{P\_{3}^{1}}{P\_{2}^{4}}\right\}\approx 0.53385, |  | (5.3) |

which contradicts the first equation. Numerical verification confirms this
incompatibility:

|  |  |  |  |
| --- | --- | --- | --- |
|  | α4​γ4​P14−q4b41≥0.53385×0.7115−2.25×10−4>0.1688=P31.\alpha\_{4}\gamma\_{4}P\_{1}^{4}-\frac{q\_{4}}{b\_{4}^{1}}\geq 0.53385\times 0.7115-2.25\times 10^{-4}>0.1688=P\_{3}^{1}. |  | (5.4) |

Consequently, in a neighborhood of t=1t=1, we observe no trading activity in Markets 1, 2, 3, and 5, while arbitrage opportunities in Market 4. Numerical experiments with a 200-point grid confirms this behavior, see Figure [5](#S5.F5 "Figure 5 ‣ 5 Interpretations and Numerical Experiments ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"). Furthermore Market 5 remains inactive for t∈[0.2,0.9].t\in[0.2,0.9].
This can also be checked from market activations, see Figure [7](#S5.F7 "Figure 7 ‣ 5 Interpretations and Numerical Experiments ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"), where η¯3​(t)≈0.25\bar{\eta}\_{3}(t)\approx 0.25 for
t∈[0.2,0.9]t\in[0.2,0.9]. We can check that no market is purely active, η¯i​(t)<1\bar{\eta}\_{i}(t)<1, so y¯i<bi\bar{y}^{i}<b^{i} for every i=1,…,5i=1,\ldots,5, and constraint qualification ([3.14](#S3.E14 "In 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")) holds in the whole parameter range, while the optimality conditions are still valid. Consequently, the trade behavior follows by Remark [3.3](#S3.Thmremark3 "Remark 3.3. ‣ 3.1 Necessary Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees").(i), as
numerically verified for Market 1 in Figure [8](#S5.F8 "Figure 8 ‣ 5 Interpretations and Numerical Experiments ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"). For Market 4, enforcing no-trade conditions requires either reducing the discount rate γ4\gamma\_{4} or increasing the gas fee q4.q\_{4}. In the second case, we can enforce the no-trade condition on Market 4 by taking

|  |  |  |  |
| --- | --- | --- | --- |
|  | q4≥max⁡{(P31P24​γ4​P14−P11)​b14,(P31P24​γ4​P24−P31)​b24}=9.3788.q\_{4}\geq\max\left\{\left(\frac{P\_{3}^{1}}{P\_{2}^{4}}\gamma\_{4}P\_{1}^{4}-P\_{1}^{1}\right)b\_{1}^{4},\left(\frac{P\_{3}^{1}}{P\_{2}^{4}}\gamma\_{4}P\_{2}^{4}-P\_{3}^{1}\right)b\_{2}^{4}\right\}=9.3788. |  | (5.5) |

Setting q4=9.4q\_{4}=9.4 establishes a no-trade region, effectively deactivating Market 4, see Figure [9](#S5.F9 "Figure 9 ‣ 5 Interpretations and Numerical Experiments ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"). The numerical computation of the no-trade interval gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | [0.907537688442211,1.0844221105527638],[0.907537688442211,1.0844221105527638], |  | (5.6) |

see Figure [10](#S5.F10 "Figure 10 ‣ 5 Interpretations and Numerical Experiments ‣ Optimal Routing across Constant Function Market Makers with Gas Fees").

In a second experiment, we numerically validate Remark [3.4](#S3.Thmremark4 "Remark 3.4. ‣ 3.2 Sufficient Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees")
and consequently Theorem [3.4](#S3.Thmthr4 "Theorem 3.4. ‣ 3.2 Sufficient Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"). Given a solution (𝐱¯,𝐲¯,η¯)(\bar{\mathbf{x}},\bar{\mathbf{y}},\bar{\eta}) to the relaxed problem (𝒫r​(𝐛,q))(\mathcal{P}^{r}(\mathbf{b},q)), we compare (𝐱¯,𝐲¯)(\bar{\mathbf{x}},\bar{\mathbf{y}}) with the
solution (𝐱~,𝐲~)(\tilde{\mathbf{x}},\tilde{\mathbf{y}}) of the problem (𝒫η¯​(𝐛,q))(\mathcal{P}^{\bar{\eta}}(\mathbf{b},q)), for which the activation of the market is determined by η¯\bar{\eta}. We consider different constant gas fees qi∈{0.01,0.1,0.5,1}q\_{i}\in\{0.01,0.1,0.5,1\}. Following Remark [3.4](#S3.Thmremark4 "Remark 3.4. ‣ 3.2 Sufficient Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"), the solution (𝐱¯,𝐲¯)(\bar{\mathbf{x}},\bar{\mathbf{y}}) is an ε​(q,η¯)\varepsilon(q,\bar{\eta})-approximate solution to 𝒫η¯​(𝐛,q)\mathcal{P}^{\bar{\eta}}(\mathbf{b},q), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ε​(q,η¯):=q​(‖η¯‖0−‖η¯‖1).\varepsilon(q,\bar{\eta}):=q\left(\|\bar{\eta}\|\_{0}-\|\bar{\eta}\|\_{1}\right). |  | (5.7) |

This implies that the utility difference between both solutions should be
small and, by stability arguments, the trades should satisfy (𝐱¯,𝐲¯)≈(𝐱~,𝐲~)(\bar{\mathbf{x}},\bar{\mathbf{y}})\approx(\tilde{\mathbf{x}},\tilde{\mathbf{y}}) when
qq is sufficiently small for a moderate number of markets, as is the case in our
example. This result has practical significance because, by Theorem [3.4](#S3.Thmthr4 "Theorem 3.4. ‣ 3.2 Sufficient Optimality Conditions ‣ 3 Optimal Routing with Gas Fee ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"),
(𝐱~,𝐲~,1{η¯>0})\left(\mathbf{\tilde{x}},\mathbf{\tilde{y}},1\_{\left\{\bar{\eta}>0\right\}}\right) is an ε​(q,η¯)\varepsilon(q,\bar{\eta})-approximate solution to the original problem (𝒫​(𝐛,q))(\mathcal{P}(\mathbf{b},q)), with ε​(q,η¯)\varepsilon(q,\bar{\eta}) being an a priori
computable bound. Our numerical computations, obtained under identical experimental conditions, confirm these theoretical observations.
Figures [11](#S5.F11 "Figure 11 ‣ 5 Interpretations and Numerical Experiments ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") and [12](#S5.F12 "Figure 12 ‣ 5 Interpretations and Numerical Experiments ‣ Optimal Routing across Constant Function Market Makers with Gas Fees") demonstrate that for q=0.01q=0.01,
both utilities and trades are virtually identical. However, as the gas fees increase and ε​(q,η¯)\varepsilon(q,\bar{\eta})
becomes significantly larger, we observe noticeable divergences between these quantities. In this sense, in Figure [11](#S5.F11 "Figure 11 ‣ 5 Interpretations and Numerical Experiments ‣ Optimal Routing across Constant Function Market Makers with Gas Fees"), the staircase-like discontinuities in some of the plots are explained by the nature of the ℓ0\ell\_{0} pseudonorm and the term ∑η¯i>0qi\sum\limits\_{\bar{\eta}\_{i}>0}q\_{i}.

![Refer to caption](2603.02844v1/FIGURES/Ex1_gm_A.png)


Figure 1: Example 1: No-trade region for the geometric mean function φgm\varphi\_{\mathrm{gm}}.

![Refer to caption](2603.02844v1/FIGURES/Ex1_qm_A.png)


Figure 2: Example 1: No-trade region for the weighted quasi-arithmetic mean function φqm\varphi\_{\mathrm{qm}}.

![Refer to caption](2603.02844v1/FIGURES/Ex1_gm_B.png)


Figure 3: Example 1: Activation of the market for φgm\varphi\_{\mathrm{gm}}.

![Refer to caption](2603.02844v1/FIGURES/Ex1_qm_B.png)


Figure 4: Example 1: Activation of the market for φqm\varphi\_{\mathrm{qm}}.

![Refer to caption](2603.02844v1/FIGURES/Ex2_trades_q001_B.png)


Figure 5: Example 2: Optimal trades (qi=0.01)(q\_{i}=0.01).

![Refer to caption](2603.02844v1/FIGURES/Ex2_topology.png)


Figure 6: Example 2: Market network topology.

![Refer to caption](2603.02844v1/FIGURES/Ex2_activation_markets_q001.png)


Figure 7: Example 2: Activation of markets (qi=0.01)(q\_{i}=0.01).

![Refer to caption](2603.02844v1/FIGURES/Ex2_Market1_OptimalTenderedBasket_q001.png)


Figure 8: Example 2: Optimal tendered basket in Market 1 (qi=0.01)(q\_{i}=0.01).

![Refer to caption](2603.02844v1/FIGURES/Ex2_trades_q4_94.png)


Figure 9: Example 2: Optimal trades (qi=0.01,i≠4,q4=9.4)(q\_{i}=0.01,\ i\neq 4,q\_{4}=9.4).

![Refer to caption](2603.02844v1/FIGURES/Ex_2_Notrade_region_q4_94.png)


Figure 10: Example 2: No-trade region (qi=0.01,i≠4;q4=9.4)(q\_{i}=0.01,\ i\neq 4;\ q\_{4}=9.4).




Table 1: Example 2: Local market data.

| CFMM | Trading function φi\varphi\_{i} | Discount rate γi\gamma\_{i} | Local reserves RiR^{i} |
| --- | --- | --- | --- |
| II | φ1​(R)=(R1w1​R2w2​R3w3)1/(w1+w2+w3)\varphi\_{1}(R)=\left(R\_{1}^{w\_{1}}R\_{2}^{w\_{2}}R\_{3}^{w\_{3}}\right)^{1/(w\_{1}+w\_{2}+w\_{3})} | 0.99 | (3,0.2,1)(3,0.2,1) |
|  | (weighted geometric mean), w=(3,2,1)w=(3,2,1) |  |  |
| I​III | φ2​(R)=R1​R2\varphi\_{2}(R)=\sqrt{R\_{1}R\_{2}} | 0.99 | (10,1)(10,1) |
|  | (geometric mean) |  |  |
| I​I​IIII | φ3​(R)=R1​R2\varphi\_{3}(R)=\sqrt{R\_{1}R\_{2}} | 0.99 | (1,10)(1,10) |
|  | (geometric mean) |  |  |
| I​VIV | φ4​(R)=R1​R2\varphi\_{4}(R)=\sqrt{R\_{1}R\_{2}} | 0.99 | (20,50)(20,50) |
|  | (geometric mean) |  |  |
| VV | φ5​(R)=R1+R2\varphi\_{5}(R)=R\_{1}+R\_{2} | 0.99 | (10,10)(10,10) |
|  | (arithmetic mean) |  |  |



![Refer to caption](2603.02844v1/FIGURES/Ex2_utility_combined_q001.png)


(a) qi=0.01q\_{i}=0.01

![Refer to caption](2603.02844v1/FIGURES/Ex2_utility_combined_q01.png)


(b) qi=0.1q\_{i}=0.1

![Refer to caption](2603.02844v1/FIGURES/Ex2_utility_combined_q05.png)


(c) qi=0.5q\_{i}=0.5

![Refer to caption](2603.02844v1/FIGURES/Ex2_utility_combined_q1.png)


(d) qi=1q\_{i}=1

Figure 11: Utility plots for different gas fee qiq\_{i} values.



![Refer to caption](2603.02844v1/FIGURES/Ex2_trades_comparison_q001.png)


(a) qi=0.01q\_{i}=0.01

![Refer to caption](2603.02844v1/FIGURES/Ex2_trades_comparison_q01.png)


(b) qi=0.1q\_{i}=0.1

![Refer to caption](2603.02844v1/FIGURES/Ex2_trades_comparison_q05.png)


(c) qi=0.5q\_{i}=0.5

![Refer to caption](2603.02844v1/FIGURES/Ex2_trades_comparison_q1.png)


(d) qi=1q\_{i}=1

Figure 12: Trade comparisons for different gas fee qiq\_{i} values.

## 6 Conclusions

We have studied the optimal routing problem across multiple heterogeneous CFMMs in the presence of fixed execution costs modeling gas fees. The resulting optimization problem departs from classical
convex formulations by combining nonconvex trading constraints with market
activation decisions, which are introduced to enforce the effect of those fees.

Our first contribution has been the derivation of necessary optimality conditions for a relaxation approximation of the routing problem under mild regularity assumptions.
By establishing a KKT system under an appropriate KRZ constraint qualification, we obtained an explicit
characterization of optimal trades linking marginal utilities, pool prices,
fees, and activation variables. This analysis highlights the role of gas fees in
expanding the no-trade region and in shaping optimal routing decisions across
fragmented liquidity pools.

We have further shown that global optimality can be characterized without
imposing global convexity assumptions on the invariant functions. Using tools
from generalized convexity, we established sufficient optimality conditions
under pseudoconcavity of the utilities and quasilinearity of the trade functions. This result extends existing CFMM routing theory beyond convex
models, allowing for a broader class of admissible invariant functions while
preserving optimality.

A rigorous comparison between the relaxed routing problem and the original
mixed-integer formulation with fixed activation costs was also provided.
Explicit approximation bounds were derived, quantifying the utility gap induced
by relaxation and clarifying the conditions under which relaxed solutions offer
meaningful approximations to the original problem. This analysis also provides a
theoretical justification for relaxation-based approaches potentially usable in related questions.

From a financial perspective, our results offer a mathematical interpretation of
how fixed execution costs suppress arbitrage opportunities in decentralized exchanges. The framework developed in this paper thus contributes to a deeper understanding of no-trade conditions and execution frictions in DeFi markets.

All in all, our results contribute to the growing literature
that bridges optimization theory and decentralized market design, showing how
execution frictions fundamentally reshape optimal trading behavior even in
deterministic, on-chain environments.
Several directions for future research naturally arise from them. Extensions to stochastic utility formulations or dynamic routing under uncertainty would further enrich the model. Additionally, the integration of alternative execution constraints or protocol-specific
features may provide further insights into optimal trading and market design in decentralized financial systems.

Acknowledgements:
Part of this work was carried out when the authors were visiting the Vietnam Institute for Advanced Study in Mathematics (VIASM) throughout March and April 2025; the authors would like to thank VIASM for its hospitality during this period. This research has been partially supported by ANID–Chile under project Fondecyt Regular 1241040 (Lara), by MICIU / AEI / 10.13039 / 501100011033 / and by ERDF, EU (Projects PID2024-156273NA-I00 (Sama) and PID2024-158823NB-I00 (Escudero)), by MICIU / AEI / 10.13039 / 501100011033 / European Union NextGenerationEU / PRTR (Project CPP2024-011557 (Escudero and Sama)), and by COST (European Cooperation in Science and Technology) through COST Action Stochastica CA24104 (Escudero).

## References

* [1]

  H. Adams, M. Salem, N. Zinsmeister, S. Reynolds, A. Adams, W. Pote, M. Toda, A. Henshaw, E. Williams, D. Robinson, Uniswap v4 core [draft]. Technical report, (2023).
* [2]

  H. Adams, N. Zinsmeister, D. Robinson, Uniswap v2 core. Technical Report, (2020).
* [3]

  H. Adams, N. Zinsmeister, M. Salem, R. Keefer, D. Robinson, Uniswap v3 core. Technical Report, (2021).
* [4]

  H. Adams, N. Zinsmeister, M. Toda, E. Williams, X. Wan, M. Leibowitz, W. Pote, A. Lin, E. Zhong, Z. Yang, R. Campbell, A. Karys, D. Robinson, UniswapX. Technical report, (2023).
* [5]

  G. Angeris, A. Agrawal, A. Evans, T. Chitra, S. Boyd, Constant function market makers: multi-asset trades via convex optimization. In: D.A. Tran et al. (eds): “Handbook on Blockchain”, Springer Optimization and Its Applications, Vol. 194, Springer, (2022).
* [6]

  G. Angeris, T. Chitra, Improved price oracles: constant function
  market makers. In: Proc. 2nd ACM Conf. Adv. in Financial Tech., Pages
  80–91, https://doi.org/10.1145/3419614.3423251, (2020).
* [7]

  G. Angeris, T. Chitra, A. Evans, When does the tail wag the dog? Curvature and market making, Cryptoeconomic Systems, 2 (1), https://doi.org/10.21428/58320208.e9e6b7ce, (2022).
* [8]

  G. Angeris, A. Evans, T. Chitra, S. Boyd, Optimal routing for constant function market makers. In: EC ’22: Proc. 23rd ACM Conference on Econ. Comp., July 2022, 115–128, (2022).
* [9]

  G. Angeris, H.-T. Kao, R. Chiang, C. Noyes, T. Chitra, An analysis of Uniswap markets, Cryptoeconomic Systems, 0 (1), https://doi.org/10.21428/58320208.c9738e64, (2021).
* [10]

  K.J. Arrow, A.C. Enthoven, Quasiconcave programming, Econometrica, 29, 779–800, (1961).
* [11]

  M. Avriel, W.E. Diewert, S. Schaible, I. Zang. “Generalized Concavity”. SIAM, Philadelphia, (2010).
* [12]

  A. Cambini, L. Martein. “Generalized Convexity and Optimization”. Springer-Verlag, Berlin-Heidelberg, (2009).
* [13]

  A. Capponi, R. Jia, The adoption of blockchain-based decentralized exchanges, arXiv:2103.08842, (2021).
* [14]

  A. Capponi, R. Jia, Y. Wang, Maximal extractable value and allocative inefficiencies in public blockchains, Journal of Financial Economics, 172, 104132, (2025).
* [15]

  A. Capponi, R. Jia, B. Zhu, The paradox of just-in-time liquidity in decentralized exchanges: More providers can sometimes mean less liquidity, arXiv:2311.18164, (2023).
* [16]

  T. Chitra, K. Kulkarni, K. Srinivasan, Optimal routing in the presence of hooks:
  three case studies, arXiv: 2502.02059, (2025).
* [17]

  G. Debreu. “Theory of Value”. John Wiley, New York, (1959).
* [18]

  T. Diamandis, G. Angeris, The convex geometry of network flows, arXiv:2408.12761, (2024).
* [19]

  T. Diamandis, M. Resnick, T. Chitra, G. Angeris, An efficient algorithm for optimal routing through constant function market makers. In: F. Baldimtsi and C. Cachin (eds): “Financial Cryptography and Data Security”. Lecture Notes in Computer Science, Vol. 13951, Springer, Cham, (2024).
* [20]

  M.Egorov, StableSwap – efficient mechanism for stablecoin liquidity, https://berkeley-defi.github.io/assets/material/StableSwap.pdf, (2019).
* [21]

  M. Ehrgott. “Multicriteria Optimization”. Vol. 491, Springer Science &\& Business Media, (2005).
* [22]

  C. Escudero, F. Lara, M. Sama, Optimal trade characterizations of multi-asset crypto-financial markets, arXiv: 2405.06854, (2024).
* [23]

  E. Gobet, A. Melachrinos, Decentralized finance & blockchain technology, SIAM Financial Mathematics and Engineering 2023, (2023).
* [24]

  N. Hadjisavvas, S. Komlosi, S. Schaible. “Handbook of Generalized Convexity and Generalized Monotonicity”. Springer-Verlag, Boston, (2005).
* [25]

  J.-B. Hiriart-Urruty, C. Lemaréchal. “Fundamentals of Convex Analysis”. Springer-Verlag, Berlin, Second Edition, (2004).
* [26]

  J. Jahn. “Introduction to the Theory of Nonlinear Optimization”. Springer Nature, (2020).
* [27]

  O.L. Mangasarian, Pseudo-convex functions, J. SIAM Control, Ser. A, 3, 281–290, (1965).
* [28]

  F. Martinelli, N. Mushegian, A non-custodial portfolio manager, liquidity provider, and price sensor, https://docs.balancer.fi/whitepaper.pdf, (2019).
* [29]

  A. Mas-Colell, M.D. Whinston, J.R. Green. “Microeconomic Theory”. Oxford University Press, Oxford, (1995).
* [30]

  S. Schaible, W.T. Ziemba. “Generalized Concavity in Optimization and Economics”. Academic Press, (1981).
* [31]

  D.A. Tran, M.T. Thai, B. Krishnamachari, “Handbook on Blockchains”. Springer Optimization and Its Applications, Vol. 194,
  Springer, (2022).
* [32]

  P. Virtanen, et al., SciPy 1.0: Fundamental algorithms for scientific computing in Python, Nature Methods, 17 (13), 261–272, (2020).

BETA