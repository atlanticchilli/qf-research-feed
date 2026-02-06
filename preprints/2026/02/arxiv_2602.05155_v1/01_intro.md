---
authors:
- Heather N. Fogarty
- Sooie-Hoe Loke
- Nicholas F. Marshall
- Enrique A. Thomann
doc_id: arxiv:2602.05155v1
family_id: arxiv:2602.05155
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Optimal Risk-Sharing Rules in Network-based Decentralized Insurance
url_abs: http://arxiv.org/abs/2602.05155v1
url_html: https://arxiv.org/html/2602.05155v1
venue: arXiv q-fin
version: 1
year: 2026
---


Heather N. Fogarty
[fogartyh@oregonstate.edu](mailto:fogartyh@oregonstate.edu)
Department of Mathematics, Oregon State University
, 
Sooie-Hoe Loke
[sooiehoe.loke@mtsu.edu](mailto:sooiehoe.loke@mtsu.edu)
Department of Mathematical Sciences, Middle Tennessee State University
, 
Nicholas F. Marshall
[marsnich@oregonstate.edu](mailto:marsnich@oregonstate.edu)
Department of Mathematics, Oregon State University
 and 
Enrique A. Thomann
[thomann@math.oregonstate.edu](mailto:thomann@math.oregonstate.edu)
Department of Mathematics, Oregon State University

###### Abstract.

This paper studies decentralized risk-sharing on networks. In particular, we consider a model where agents are nodes in a given network structure. Agents directly connected by edges in the network are referred to as friends. We study actuarially fair risk-sharing under the assumption that only friends can share risk, and we characterize the optimal signed linear risk-sharing rule in this network setting. Subsequently, we consider a special case of this model where all the friends of an agent take on an equal share of the agent’s risk, and establish a connection to the graph Laplacian. Our results are illustrated with several examples.

###### Key words and phrases:

Decentralized insurance, risk-sharing, peer-to-peer insurance, graph Laplacian

## 1. Introduction

Risk-sharing has been extensively studied in actuarial science.
Early works on the mathematical analysis of risk-sharing include work in the 1960s by Borch [[6](https://arxiv.org/html/2602.05155v1#bib.bib6), [7](https://arxiv.org/html/2602.05155v1#bib.bib7), [8](https://arxiv.org/html/2602.05155v1#bib.bib8)], who coined the term non-olet risk-sharing, where a central authority pools the agents’ risks and then redistributes them without taking into account the origins of the risks in the pool. From a mathematical perspective, this means that while the risk-sharing rule of each agent may depend on individual parameters, it is only a function of the aggregate losses.

Recently, decentralized insurance models have attracted considerable attention in the actuarial research community. In these models, agents share risk among each other with limited or no role for a central authority; see [[21](https://arxiv.org/html/2602.05155v1#bib.bib21), [23](https://arxiv.org/html/2602.05155v1#bib.bib23)] for a systematic mathematical treatment of decentralized insurance. While technological, economic, and social developments have created a renewed interest in decentralized insurance models, there already exist historical examples of such risk-sharing schemes. A prominent example is Takaful, which is an Islamic-compliant form of insurance based on mutual assistance, where participants contribute to a common pool to cover losses, rather than transferring risk to an insurer; see [[25](https://arxiv.org/html/2602.05155v1#bib.bib25)]. Decentralized insurance models have also found a variety of modern applications, including cyber insurance contracts [[20](https://arxiv.org/html/2602.05155v1#bib.bib20)], cooperative insurance [[13](https://arxiv.org/html/2602.05155v1#bib.bib13)], and, recently, have been used by governments to manage catastrophic risks, especially related to climate change and extreme weather events [[3](https://arxiv.org/html/2602.05155v1#bib.bib3)].

In this paper, we are specifically interested in peer-to-peer (P2P) insurance, which is a model where agents directly exchange risk. The mathematical foundations of P2P insurance are an active area of research, with common topics of examination including optimization conditions [[1](https://arxiv.org/html/2602.05155v1#bib.bib1), [15](https://arxiv.org/html/2602.05155v1#bib.bib15), [16](https://arxiv.org/html/2602.05155v1#bib.bib16), [27](https://arxiv.org/html/2602.05155v1#bib.bib27)], development of new risk-sharing models [[4](https://arxiv.org/html/2602.05155v1#bib.bib4), [17](https://arxiv.org/html/2602.05155v1#bib.bib17), [22](https://arxiv.org/html/2602.05155v1#bib.bib22), [24](https://arxiv.org/html/2602.05155v1#bib.bib24)], and analysis of existing risk-sharing models [[2](https://arxiv.org/html/2602.05155v1#bib.bib2), [14](https://arxiv.org/html/2602.05155v1#bib.bib14), [18](https://arxiv.org/html/2602.05155v1#bib.bib18), [19](https://arxiv.org/html/2602.05155v1#bib.bib19)].
A key difference between centralized insurance models and P2P models is that P2P insurance enables arrangements where participants do not share risk with every other agent, which can be modeled using a network whose nodes are agents and whose edges represent potential risk-sharing relationships. From the network theory perspective, non-olet risk-sharing corresponds to a star graph, where the central node is the central authority, while unrestricted P2P risk-sharing corresponds to a complete graph,
see Figure [1](https://arxiv.org/html/2602.05155v1#S1.F1 "Figure 1 ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance").

|  |  |  |
| --- | --- | --- |
| Star graph | Complete graph | Barbell graph |

Figure 1. Many works on P2P insurance either perform non-olet risk pooling (represented by the star graph) or unrestricted risk-sharing (represented by the complete graph). In this work, we consider networks with general structures such as the Barbell graph.

While a substantial body of work on P2P insurance has emerged, particularly over the past decade, the theoretical foundations of P2P risk-sharing on networks remain underdeveloped; notable examples include
[[10](https://arxiv.org/html/2602.05155v1#bib.bib10)], which examines decentralized insurance on a random network,
and [[11](https://arxiv.org/html/2602.05155v1#bib.bib11)] that considers optimal row and column stochastic risk-sharing rules on networks.

In this paper, we study optimal risk-sharing on networks inspired by [[22](https://arxiv.org/html/2602.05155v1#bib.bib22)], which considers optimal unrestricted (signed) linear risk-sharing, which corresponds to risk-sharing on a complete graph.
In particular, [[22](https://arxiv.org/html/2602.05155v1#bib.bib22)] characterizes the linear actuarially fair risk-sharing rule that is optimal in the sense that it minimizes the sum of variances of each agent’s loss after risk-sharing. Subsequently, [[27](https://arxiv.org/html/2602.05155v1#bib.bib27)] proves that, among all risk-sharing rules, the optimal risk-sharing rule is an affine function of the
residual risks (formed by subtracting the mean from each loss random variable).
Recently, [[26](https://arxiv.org/html/2602.05155v1#bib.bib26)] shows that actuarially fair Pareto-optimal risk-sharing rules are in one-to-one correspondence with the fixed points of a specific function. Some of the aforementioned works have been extended to multi-period risk-sharing [[1](https://arxiv.org/html/2602.05155v1#bib.bib1)] and a continuous time setting
[[5](https://arxiv.org/html/2602.05155v1#bib.bib5)].

### 1.1. Main contributions

In this paper, we consider a variance minimization problem for a network-based, actuarially fair, linear risk-sharing rule, which can be applied to any connected network. In this context, the main contributions of this paper are as follows: (1) We characterize the optimal (signed) allocation, in Theorem [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem1 "Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), for connected networks, extending results in [[22](https://arxiv.org/html/2602.05155v1#bib.bib22)] which are only valid for complete graphs; (2) We establish a novel connection to the graph Laplacian in the special case that risk is proportionally shared among agents with a common node, as demonstrated in Theorem [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem2 "Theorem 2.2 (Friends take an equal share of risk). ‣ 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"); and (3) We obtain necessary and sufficient conditions for the positivity of risk allocation for complete graphs (Proposition [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmproposition1 "Proposition 2.1. ‣ 2.5.1. Nonnegativity Conditions for 𝑨_∗ for the case of the complete graph ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")), and for risk-sharing rules modeled using the graph Laplacian, (Proposition [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmlemma2 "Lemma 2.2. ‣ 2.5.2. Nonnegativity conditions for 𝑨̂ ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")).

### 1.2. Preliminaries

In this section, we give a precise mathematical definition of risk-sharing.
Let 𝑿=(X1,…,Xn)⊤\boldsymbol{X}=(X\_{1},\ldots,X\_{n})^{\top} be a nonnegative random vector whose ii-th entry XiX\_{i} represents the loss of agent ii. Let 𝝁=𝔼​[𝑿]\boldsymbol{\mu}=\mathbb{E}[\boldsymbol{X}] denote the mean of 𝑿\boldsymbol{X} and

|  |  |  |
| --- | --- | --- |
|  | 𝚺=Var⁡(𝑿):=𝔼​[(𝑿−𝔼​[𝑿])​(𝑿−𝔼​[𝑿])⊤],\boldsymbol{\Sigma}=\operatorname{Var}(\boldsymbol{X}):=\mathbb{E}\left[(\boldsymbol{X}-\mathbb{E}[\boldsymbol{X}])(\boldsymbol{X}-\mathbb{E}[\boldsymbol{X}])^{\top}\right], |  |

denote the covariance matrix of 𝑿\boldsymbol{X}. Throughout this paper, we assume that 𝚺\boldsymbol{\Sigma} is a positive definite, and therefore invertible, matrix.

A risk-sharing rule HH is a function H:ℝn→ℝnH:\mathbb{R}^{n}\rightarrow\mathbb{R}^{n} that satisfies the following full-allocation property.

###### Definition 1.1.

A function H:ℝn→ℝnH:\mathbb{R}^{n}\to\mathbb{R}^{n} satisfies the full-allocation property if

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nHi​(𝑿)=∑i=1nXi,\sum\_{i=1}^{n}H\_{i}(\boldsymbol{X})=\sum\_{i=1}^{n}X\_{i}, |  |

almost surely, where Hi​(𝑿)H\_{i}(\boldsymbol{X}) denotes the ii-th entry of H​(𝑿)H(\boldsymbol{X}).

An example of a risk-sharing rule is the linear rule H:ℝn→ℝnH:\mathbb{R}^{n}\to\mathbb{R}^{n} by

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | H​(𝑿)=𝑨​𝑿,H(\boldsymbol{X})=\boldsymbol{AX}, |  |

where 𝑨=(ai​j)∈ℝn×n\boldsymbol{A}=(a\_{ij})\in\mathbb{R}^{n\times n} is any matrix whose columns sum to 11, that is, 𝟏⊤​𝑨=𝟏⊤\boldsymbol{1}^{\top}\boldsymbol{A}=\boldsymbol{1}^{\top}, where 𝟏\boldsymbol{1} is a column vector of ones.

Note that some papers require risk-sharing functions to be nonnegative, which corresponds to the property that agents cannot profit from the loss of another agent. Under such an assumption, the matrix 𝑨\boldsymbol{A} in ([1](https://arxiv.org/html/2602.05155v1#S1.E1 "In 1.2. Preliminaries ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) would be restricted to a column stochastic matrix. In this paper, we make no such assumption, which allows us to characterize risk-sharing allocations that take negative values. Practically speaking, a risk-sharing scheme involving signed exchanges is analogous to financial models that allow agents to buy and short-sell financial instruments. Conditions for achieving nonnegative risk-sharing rules are discussed in §[2.5](https://arxiv.org/html/2602.05155v1#S2.SS5 "2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance").

As customary, we also impose that the risk-sharing rules are *actuarially fair* according to the following definition.

###### Definition 1.2.

A risk-sharing rule H:ℝn→ℝnH:\mathbb{R}^{n}\to\mathbb{R}^{n} is actuarially fair if

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[H​(𝑿)]=𝔼​[𝑿].\mathbb{E}[H(\boldsymbol{X})]=\mathbb{E}[\boldsymbol{X}]. |  |

### 1.3. Prior work

Recall that 𝝁=𝔼​[𝑿]\boldsymbol{\mu}=\mathbb{E}[\boldsymbol{X}] is the mean vector and 𝚺=Var⁡(𝑿)\boldsymbol{\Sigma}=\operatorname{Var}(\boldsymbol{X}) is the covariance matrix of 𝑿\boldsymbol{X}. Feng, Liu, and Taylor [[22](https://arxiv.org/html/2602.05155v1#bib.bib22)] consider the following optimization problem for a linear risk-sharing rule H​(𝑿)=𝑨​𝑿H(\boldsymbol{X})=\boldsymbol{A}\boldsymbol{X}:

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | {minimize12​tr⁡(𝑨​𝚺​𝑨⊤)subject to𝟏⊤​𝑨=𝟏⊤,𝑨​𝝁=𝝁,\begin{cases}\text{minimize}&\frac{1}{2}\operatorname{tr}(\boldsymbol{A}\boldsymbol{\Sigma}\boldsymbol{A}^{\top})\\ \text{subject to}&\boldsymbol{1}^{\top}\boldsymbol{A}=\boldsymbol{1}^{\top},\quad\boldsymbol{A}\boldsymbol{\mu}=\boldsymbol{\mu},\end{cases} |  |

where the optimization is taken over 𝑨∈ℝn×n\boldsymbol{A}\in\mathbb{R}^{n\times n}.
The objective function in this optimization problem is half the sum of the variances of the agents’ losses after risk-sharing, as given by

|  |  |  |
| --- | --- | --- |
|  | 12​tr⁡(𝑨​𝚺​𝑨⊤)=12​tr⁡Var⁡(𝑨​𝑿)=12​∑i=1nVar⁡(Hi​(𝑿)).\frac{1}{2}\operatorname{tr}(\boldsymbol{A}\boldsymbol{\Sigma}\boldsymbol{A}^{\top})=\frac{1}{2}\operatorname{tr}\operatorname{Var}(\boldsymbol{AX})=\frac{1}{2}\sum\_{i=1}^{n}\operatorname{Var}(H\_{i}(\boldsymbol{X})). |  |

The first constraint 𝟏⊤​𝑨=𝟏⊤\boldsymbol{1}^{\top}\boldsymbol{A}=\boldsymbol{1}^{\top} enforces full-allocation (Definition [1.1](https://arxiv.org/html/2602.05155v1#S1.Thmdefinition1 "Definition 1.1. ‣ 1.2. Preliminaries ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")), and the second constraint 𝑨​𝝁=𝝁\boldsymbol{A}\boldsymbol{\mu}=\boldsymbol{\mu} ensures actuarial fairness (Definition [1.2](https://arxiv.org/html/2602.05155v1#S1.Thmdefinition2 "Definition 1.2. ‣ 1.2. Preliminaries ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")).
We emphasize again that H​(𝑿)=𝑨​𝑿H(\boldsymbol{X})=\boldsymbol{A}\boldsymbol{X} is allowed to be a signed risk-sharing rule and 𝑨\boldsymbol{A} may have some negative entries, see §[2.6.1](https://arxiv.org/html/2602.05155v1#S2.SS6.SSS1 "2.6.1. Agents with losses with means at different scales ‣ 2.6. Examples where optimal matrices have negative entries ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")
for an example where negative entries arise. The following result characterizes the solution to the optimization problem ([2](https://arxiv.org/html/2602.05155v1#S1.E2 "In 1.3. Prior work ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")).

###### Theorem 1.1 (Feng, Liu, Taylor [[22](https://arxiv.org/html/2602.05155v1#bib.bib22)]).

The optimization problem ([2](https://arxiv.org/html/2602.05155v1#S1.E2 "In 1.3. Prior work ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) has a unique solution

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | 𝑨∗=1n​𝟏𝟏⊤+1a​(𝑰−1n​𝟏𝟏⊤)​𝝁​𝝁⊤​𝚺−1,\boldsymbol{A}\_{\*}=\frac{1}{n}\boldsymbol{1}\boldsymbol{1}^{\top}+\frac{1}{a}\left(\boldsymbol{I}-\frac{1}{n}\boldsymbol{1}\boldsymbol{1}^{\top}\right)\boldsymbol{\mu\mu}^{\top}\boldsymbol{\Sigma}^{-1}, |  |

where a=𝛍⊤​𝚺−1​𝛍a=\boldsymbol{\mu}^{\top}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}.

The proof of this result is based on Lagrange multipliers, see [[22](https://arxiv.org/html/2602.05155v1#bib.bib22)] for details. In this paper, we consider a generalization of the optimization problem ([2](https://arxiv.org/html/2602.05155v1#S1.E2 "In 1.3. Prior work ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) that allows for network-based constraints.

## 2. Main results

### 2.1. Only friends share risk

As above, let 𝑿\boldsymbol{X} be an nn-dimensional loss vector with mean 𝝁\boldsymbol{\mu} and covariance 𝚺\boldsymbol{\Sigma}. Assume that there is an underlying simple undirected graph G=(V,E)G=(V,E) whose vertices V={1,…,n}V=\{1,\ldots,n\} correspond to the agents, and whose edge set EE, which consists of unordered pairs of distinct vertices {i,j}\{i,j\}, represents friendships between the agents. Let di=#​{j∈V:{i,j}∈E}d\_{i}=\#\{j\in V:\{i,j\}\in E\} denote the degree of vertex ii. Throughout this paper, we assume that the number of agents n≥2n\geq 2 to avoid a trivial situation. In this paper, we consider the following network-based constraint.

###### Definition 2.1 (Only friends share risk).

Let H:ℝn→ℝnH:\mathbb{R}^{n}\to\mathbb{R}^{n} be a risk-sharing rule. We say that HH has the property that only friends share risk if, for each fixed i∈{1,…,n}i\in\{1,\ldots,n\}, we have

|  |  |  |
| --- | --- | --- |
|  | Hi​(𝒙)=fi​(xi,xj1,…,xjdi),H\_{i}(\boldsymbol{x})=f\_{i}\left(x\_{i},x\_{j\_{1}},\ldots,x\_{j\_{d\_{i}}}\right), |  |

for some function fi:ℝdi+1→ℝf\_{i}:\mathbb{R}^{d\_{i}+1}\to\mathbb{R}, where 𝒙=(x1,…,xn)\boldsymbol{x}=(x\_{1},\ldots,x\_{n}) and j1,…,jdij\_{1},\ldots,j\_{d\_{i}} is an enumeration of the vertices {j∈V:{i,j}∈E}\{j\in V:\{i,j\}\in E\}.

We consider the following optimization problem for a linear risk-sharing rule H​(𝑿)=𝑨​𝑿H(\boldsymbol{X})=\boldsymbol{A}\boldsymbol{X} where only friends share risk:

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | {minimize12​tr⁡(𝑨​𝚺​𝑨⊤)subject to𝟏⊤​𝑨=𝟏⊤,𝑨​𝝁=𝝁,ai​j≠0⟹{i,j}∈E,\begin{cases}\text{minimize}&\frac{1}{2}\operatorname{tr}(\boldsymbol{A}\boldsymbol{\Sigma}\boldsymbol{A}^{\top})\\ \text{subject to}&\boldsymbol{1}^{\top}\boldsymbol{A}=\boldsymbol{1}^{\top},\quad\boldsymbol{A}\boldsymbol{\mu}=\boldsymbol{\mu},\quad a\_{ij}\not=0\implies\{i,j\}\in E,\end{cases} |  |

where the optimization is taken over the matrix 𝑨=(ai​j)∈ℝn×n\boldsymbol{A}=(a\_{ij})\in\mathbb{R}^{n\times n}. As in
§[1.3](https://arxiv.org/html/2602.05155v1#S1.SS3 "1.3. Prior work ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), the objective function of the optimization is half the sum of the variance of the losses after risk-sharing, the constraint 𝟏⊤​𝑨=𝟏⊤\boldsymbol{1}^{\top}\boldsymbol{A}=\boldsymbol{1}^{\top} enforces full allocation (Definition
[1.1](https://arxiv.org/html/2602.05155v1#S1.Thmdefinition1 "Definition 1.1. ‣ 1.2. Preliminaries ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")), and the constraint 𝑨​𝝁=𝝁\boldsymbol{A}\boldsymbol{\mu}=\boldsymbol{\mu} enforces actuarial fairness (Definition [1.2](https://arxiv.org/html/2602.05155v1#S1.Thmdefinition2 "Definition 1.2. ‣ 1.2. Preliminaries ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")). The final constraint, which says that ai​j≠0a\_{ij}\not=0 implies that {i,j}∈E\{i,j\}\in E, enforces that only friends share risk (Definition [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmdefinition1 "Definition 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")). The following result characterizes the solution to this optimization problem.

###### Theorem 2.1 (Only friends share risk).

The optimization problem ([4](https://arxiv.org/html/2602.05155v1#S2.E4 "In 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) has a unique solution

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | 𝑨∗=1n​𝟏𝟏⊤+(𝑰−1n​𝟏𝟏⊤)​(1a​𝝁​𝝁⊤+𝚪​(1a​𝚺−1​𝝁​𝝁⊤−𝑰))​𝚺−1,\boldsymbol{A}\_{\*}=\frac{1}{n}\boldsymbol{11}^{\top}+\left(\boldsymbol{I}-\frac{1}{n}\boldsymbol{11}^{\top}\right)\left(\frac{1}{a}\boldsymbol{\mu\mu}^{\top}+\boldsymbol{\Gamma}\left(\frac{1}{a}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu\mu}^{\top}-\boldsymbol{I}\right)\right)\boldsymbol{\Sigma}^{-1}, |  |

where a=𝛍⊤​𝚺−1​𝛍a=\boldsymbol{\mu}^{\top}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu} and 𝚪=(γi​j)∈ℝn×n\boldsymbol{\Gamma}=(\gamma\_{ij})\in\mathbb{R}^{n\times n} satisfies γi​j=0\gamma\_{ij}=0 when i=ji=j or {i,j}∈E\{i,j\}\in E, and the other entries are determined by the linear system of equations

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | ((𝑰−1n​𝟏𝟏⊤)​(𝚪​(1a​𝚺−1​𝝁​𝝁⊤−𝑰)+1a​𝝁​𝝁⊤)​𝚺−1+1n​𝟏𝟏⊤)i​j=0,\left(\left(\boldsymbol{I}-\frac{1}{n}\boldsymbol{11}^{\top}\right)\left(\boldsymbol{\Gamma}\left(\frac{1}{a}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu\mu}^{\top}-\boldsymbol{I}\right)+\frac{1}{a}\boldsymbol{\mu\mu}^{\top}\right)\boldsymbol{\Sigma}^{-1}+\frac{1}{n}\boldsymbol{11}^{\top}\right)\_{ij}=0, |  |

for all i≠ji\not=j such that {i,j}∉E\{i,j\}\not\in E.

The proof of Theorem [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem1 "Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") is given in §[3](https://arxiv.org/html/2602.05155v1#S3 "3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"). Note that if (i1,j1),…,(im,jm)(i\_{1},j\_{1}),\ldots,(i\_{m},j\_{m}) is an enumeration of {(i,j)∈{1,…,n}2:i≠j∧{i,j}∉E\{(i,j)\in\{1,\ldots,n\}^{2}:i\not=j\wedge\{i,j\}\not\in E}, then, ([6](https://arxiv.org/html/2602.05155v1#S2.E6 "In Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) is a linear system of mm equations and mm unknowns γi1​j1,…,γim​jm\gamma\_{i\_{1}j\_{1}},\ldots,\gamma\_{i\_{m}j\_{m}}. See Remark [3.1](https://arxiv.org/html/2602.05155v1#S3.Thmremark1 "Remark 3.1 (Computation of 𝚪). ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") for a discussion about the computation of 𝚪\boldsymbol{\Gamma}.

###### Remark 2.1.

Note that Theorem [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem1 "Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") is an extension of Theorem [1.1](https://arxiv.org/html/2602.05155v1#S1.Thmtheorem1 "Theorem 1.1 (Feng, Liu, Taylor [22]). ‣ 1.3. Prior work ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"). Indeed, in the case of a complete graph, ([6](https://arxiv.org/html/2602.05155v1#S2.E6 "In Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) is a vacuous requirement and 𝚪=𝟎\boldsymbol{\Gamma}=\boldsymbol{0}.
Thus 𝑨∗\boldsymbol{A}\_{\*} defined in ([5](https://arxiv.org/html/2602.05155v1#S2.E5 "In Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) agrees with 𝑨∗\boldsymbol{A}\_{\*} defined in ([3](https://arxiv.org/html/2602.05155v1#S1.E3 "In Theorem 1.1 (Feng, Liu, Taylor [22]). ‣ 1.3. Prior work ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")).

### 2.2. Examples of Theorem [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem1 "Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")

In the following, we illustrate Theorem [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem1 "Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") through several examples.
In each example, for a given mean vector 𝝁\boldsymbol{\mu}, covariance matrix 𝚺\boldsymbol{\Sigma}, and graph G=(V,E)G=(V,E), we use Theorem [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem1 "Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") to determine the unique 𝑨∗\boldsymbol{A}\_{\*} that solves the optimization problem ([4](https://arxiv.org/html/2602.05155v1#S2.E4 "In 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")), and report the value of the objective function for the optimal 𝑨∗\boldsymbol{A}\_{\*}.

#### 2.2.1. Complete graph

To establish a basis of comparison, we start by considering a complete graph with uncorrelated unit mean and variance losses. Since the network is fully connected, the optimization problem
([4](https://arxiv.org/html/2602.05155v1#S2.E4 "In 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) is equivalent to the optimization problem
([2](https://arxiv.org/html/2602.05155v1#S1.E2 "In 1.3. Prior work ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) considered in [[22](https://arxiv.org/html/2602.05155v1#bib.bib22)]. Here, we have

|  |  |  |
| --- | --- | --- |
|  | 𝝁=𝟏𝚺=𝑰 1234𝑨∗=[14141414141414141414141414141414],\boldsymbol{\mu}=\boldsymbol{1}\quad\boldsymbol{\Sigma}=\boldsymbol{I}\quad\raisebox{-0.45pt}{ \hbox to56.86pt{\vbox to56.86pt{\pgfpicture\makeatletter\hbox{\quad\lower-28.43068pt\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\pgfsys@setlinewidth{\the\pgflinewidth}\pgfsys@invoke{ }\nullfont\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }{{}} \par{{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{21.33957pt}\pgfsys@curveto{6.89111pt}{25.14546pt}{3.8059pt}{28.23068pt}{0.0pt}{28.23068pt}\pgfsys@curveto{-3.8059pt}{28.23068pt}{-6.89111pt}{25.14546pt}{-6.89111pt}{21.33957pt}\pgfsys@curveto{-6.89111pt}{17.53368pt}{-3.8059pt}{14.44846pt}{0.0pt}{14.44846pt}\pgfsys@curveto{3.8059pt}{14.44846pt}{6.89111pt}{17.53368pt}{6.89111pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{1}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{21.33957pt}\pgfsys@curveto{49.57025pt}{25.14546pt}{46.48503pt}{28.23068pt}{42.67914pt}{28.23068pt}\pgfsys@curveto{38.87325pt}{28.23068pt}{35.78802pt}{25.14546pt}{35.78802pt}{21.33957pt}\pgfsys@curveto{35.78802pt}{17.53368pt}{38.87325pt}{14.44846pt}{42.67914pt}{14.44846pt}\pgfsys@curveto{46.48503pt}{14.44846pt}{49.57025pt}{17.53368pt}{49.57025pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{2}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{-21.33957pt}\pgfsys@curveto{49.57025pt}{-17.53368pt}{46.48503pt}{-14.44846pt}{42.67914pt}{-14.44846pt}\pgfsys@curveto{38.87325pt}{-14.44846pt}{35.78802pt}{-17.53368pt}{35.78802pt}{-21.33957pt}\pgfsys@curveto{35.78802pt}{-25.14546pt}{38.87325pt}{-28.23068pt}{42.67914pt}{-28.23068pt}\pgfsys@curveto{46.48503pt}{-28.23068pt}{49.57025pt}{-25.14546pt}{49.57025pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{3}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{-21.33957pt}\pgfsys@curveto{6.89111pt}{-17.53368pt}{3.8059pt}{-14.44846pt}{0.0pt}{-14.44846pt}\pgfsys@curveto{-3.8059pt}{-14.44846pt}{-6.89111pt}{-17.53368pt}{-6.89111pt}{-21.33957pt}\pgfsys@curveto{-6.89111pt}{-25.14546pt}{-3.8059pt}{-28.23068pt}{0.0pt}{-28.23068pt}\pgfsys@curveto{3.8059pt}{-28.23068pt}{6.89111pt}{-25.14546pt}{6.89111pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{4}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{7.09108pt}{21.33948pt}\pgfsys@lineto{35.58788pt}{21.33948pt}\pgfsys@moveto{42.67886pt}{14.2484pt}\pgfsys@lineto{42.67896pt}{-14.2484pt}\pgfsys@moveto{35.58788pt}{-21.33948pt}\pgfsys@lineto{7.09108pt}{-21.33948pt}\pgfsys@moveto{0.0pt}{-14.2484pt}\pgfsys@lineto{0.0pt}{14.2484pt}\pgfsys@stroke\pgfsys@invoke{ } \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{37.66481pt}{-16.32532pt}\pgfsys@lineto{5.01414pt}{16.32532pt}\pgfsys@stroke\pgfsys@invoke{ } {{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{37.66481pt}{16.32532pt}\pgfsys@lineto{5.01414pt}{-16.32532pt}\pgfsys@stroke\pgfsys@invoke{ } \par \pgfsys@invoke{ }\pgfsys@endscope{}{}{}\hss}\pgfsys@discardpath\pgfsys@invoke{ }\pgfsys@endscope\hss}}\endpgfpicture}}}\quad\boldsymbol{A}\_{\*}=\begin{bmatrix}\frac{1}{4}&\frac{1}{4}&\frac{1}{4}&\frac{1}{4}\\[2.0pt] \frac{1}{4}&\frac{1}{4}&\frac{1}{4}&\frac{1}{4}\\[2.0pt] \frac{1}{4}&\frac{1}{4}&\frac{1}{4}&\frac{1}{4}\\[2.0pt] \frac{1}{4}&\frac{1}{4}&\frac{1}{4}&\frac{1}{4}\end{bmatrix}, |  |

and 12​tr⁡(𝑨∗​𝚺​𝑨∗⊤)=12=0.5\frac{1}{2}\operatorname{tr}(\boldsymbol{A}\_{\*}\boldsymbol{\Sigma}\boldsymbol{A}\_{\*}^{\top})=\frac{1}{2}=0.5.

#### 2.2.2. Complete graph with one edge removed

We modify the previous example by removing the edge {2,4}\{2,4\} so that agents 22 and 44 are not allowed to share risk:

|  |  |  |
| --- | --- | --- |
|  | 𝝁=𝟏𝚺=𝑰 1234𝑨∗=[15310153103102531001531015310310031025],\boldsymbol{\mu}=\boldsymbol{1}\quad\boldsymbol{\Sigma}=\boldsymbol{I}\quad\raisebox{-0.45pt}{ \hbox to56.86pt{\vbox to56.86pt{\pgfpicture\makeatletter\hbox{\quad\lower-28.43068pt\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\pgfsys@setlinewidth{\the\pgflinewidth}\pgfsys@invoke{ }\nullfont\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }{{}} \par{{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{21.33957pt}\pgfsys@curveto{6.89111pt}{25.14546pt}{3.8059pt}{28.23068pt}{0.0pt}{28.23068pt}\pgfsys@curveto{-3.8059pt}{28.23068pt}{-6.89111pt}{25.14546pt}{-6.89111pt}{21.33957pt}\pgfsys@curveto{-6.89111pt}{17.53368pt}{-3.8059pt}{14.44846pt}{0.0pt}{14.44846pt}\pgfsys@curveto{3.8059pt}{14.44846pt}{6.89111pt}{17.53368pt}{6.89111pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{1}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{21.33957pt}\pgfsys@curveto{49.57025pt}{25.14546pt}{46.48503pt}{28.23068pt}{42.67914pt}{28.23068pt}\pgfsys@curveto{38.87325pt}{28.23068pt}{35.78802pt}{25.14546pt}{35.78802pt}{21.33957pt}\pgfsys@curveto{35.78802pt}{17.53368pt}{38.87325pt}{14.44846pt}{42.67914pt}{14.44846pt}\pgfsys@curveto{46.48503pt}{14.44846pt}{49.57025pt}{17.53368pt}{49.57025pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{2}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{-21.33957pt}\pgfsys@curveto{49.57025pt}{-17.53368pt}{46.48503pt}{-14.44846pt}{42.67914pt}{-14.44846pt}\pgfsys@curveto{38.87325pt}{-14.44846pt}{35.78802pt}{-17.53368pt}{35.78802pt}{-21.33957pt}\pgfsys@curveto{35.78802pt}{-25.14546pt}{38.87325pt}{-28.23068pt}{42.67914pt}{-28.23068pt}\pgfsys@curveto{46.48503pt}{-28.23068pt}{49.57025pt}{-25.14546pt}{49.57025pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{3}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{-21.33957pt}\pgfsys@curveto{6.89111pt}{-17.53368pt}{3.8059pt}{-14.44846pt}{0.0pt}{-14.44846pt}\pgfsys@curveto{-3.8059pt}{-14.44846pt}{-6.89111pt}{-17.53368pt}{-6.89111pt}{-21.33957pt}\pgfsys@curveto{-6.89111pt}{-25.14546pt}{-3.8059pt}{-28.23068pt}{0.0pt}{-28.23068pt}\pgfsys@curveto{3.8059pt}{-28.23068pt}{6.89111pt}{-25.14546pt}{6.89111pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{4}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{7.09108pt}{21.33948pt}\pgfsys@lineto{35.58788pt}{21.33948pt}\pgfsys@moveto{42.67886pt}{14.2484pt}\pgfsys@lineto{42.67896pt}{-14.2484pt}\pgfsys@moveto{35.58788pt}{-21.33948pt}\pgfsys@lineto{7.09108pt}{-21.33948pt}\pgfsys@moveto{0.0pt}{-14.2484pt}\pgfsys@lineto{0.0pt}{14.2484pt}\pgfsys@stroke\pgfsys@invoke{ } \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{37.66481pt}{-16.32532pt}\pgfsys@lineto{5.01414pt}{16.32532pt}\pgfsys@stroke\pgfsys@invoke{ } \par \pgfsys@invoke{ }\pgfsys@endscope{}{}{}\hss}\pgfsys@discardpath\pgfsys@invoke{ }\pgfsys@endscope\hss}}\endpgfpicture}}}\quad\boldsymbol{A}\_{\*}=\begin{bmatrix}\frac{1}{5}&\frac{3}{10}&\frac{1}{5}&\frac{3}{10}\\[2.0pt] \frac{3}{10}&\frac{2}{5}&\frac{3}{10}&0\\[2.0pt] \frac{1}{5}&\frac{3}{10}&\frac{1}{5}&\frac{3}{10}\\[2.0pt] \frac{3}{10}&0&\frac{3}{10}&\frac{2}{5}\end{bmatrix}, |  |

and
12​tr⁡(𝑨∗​𝚺​𝑨∗⊤)=35=0.6\frac{1}{2}\operatorname{tr}(\boldsymbol{A}\_{\*}\boldsymbol{\Sigma}\boldsymbol{A}\_{\*}^{\top})=\frac{3}{5}=0.6. The entries (2,4)(2,4) and (4,2)(4,2) of 𝑨∗\boldsymbol{A}\_{\*} are equal to zero since agents 22 and 44 cannot exchange risk, and the value of the objective function has slightly increased due to the additional restriction.

#### 2.2.3. Positive correlated losses

We further modify the previous example by changing the covariance matrix 𝚺\boldsymbol{\Sigma} such that some losses are positively correlated:

|  |  |  |
| --- | --- | --- |
|  | 𝝁=𝟏𝚺=[113013131130013113130131] 1234𝑨∗=[17514175145142751401751417514514051427],\boldsymbol{\mu}=\boldsymbol{1}\quad\boldsymbol{\Sigma}=\begin{bmatrix}1&\frac{1}{3}&0&\frac{1}{3}\\[2.0pt] \frac{1}{3}&1&\frac{1}{3}&0\\[2.0pt] 0&\frac{1}{3}&1&\frac{1}{3}\\[2.0pt] \frac{1}{3}&0&\frac{1}{3}&1\end{bmatrix}\quad\raisebox{-0.45pt}{ \hbox to56.86pt{\vbox to56.86pt{\pgfpicture\makeatletter\hbox{\quad\lower-28.43068pt\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\pgfsys@setlinewidth{\the\pgflinewidth}\pgfsys@invoke{ }\nullfont\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }{{}} \par{{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{21.33957pt}\pgfsys@curveto{6.89111pt}{25.14546pt}{3.8059pt}{28.23068pt}{0.0pt}{28.23068pt}\pgfsys@curveto{-3.8059pt}{28.23068pt}{-6.89111pt}{25.14546pt}{-6.89111pt}{21.33957pt}\pgfsys@curveto{-6.89111pt}{17.53368pt}{-3.8059pt}{14.44846pt}{0.0pt}{14.44846pt}\pgfsys@curveto{3.8059pt}{14.44846pt}{6.89111pt}{17.53368pt}{6.89111pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{1}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{21.33957pt}\pgfsys@curveto{49.57025pt}{25.14546pt}{46.48503pt}{28.23068pt}{42.67914pt}{28.23068pt}\pgfsys@curveto{38.87325pt}{28.23068pt}{35.78802pt}{25.14546pt}{35.78802pt}{21.33957pt}\pgfsys@curveto{35.78802pt}{17.53368pt}{38.87325pt}{14.44846pt}{42.67914pt}{14.44846pt}\pgfsys@curveto{46.48503pt}{14.44846pt}{49.57025pt}{17.53368pt}{49.57025pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{2}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{-21.33957pt}\pgfsys@curveto{49.57025pt}{-17.53368pt}{46.48503pt}{-14.44846pt}{42.67914pt}{-14.44846pt}\pgfsys@curveto{38.87325pt}{-14.44846pt}{35.78802pt}{-17.53368pt}{35.78802pt}{-21.33957pt}\pgfsys@curveto{35.78802pt}{-25.14546pt}{38.87325pt}{-28.23068pt}{42.67914pt}{-28.23068pt}\pgfsys@curveto{46.48503pt}{-28.23068pt}{49.57025pt}{-25.14546pt}{49.57025pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{3}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{-21.33957pt}\pgfsys@curveto{6.89111pt}{-17.53368pt}{3.8059pt}{-14.44846pt}{0.0pt}{-14.44846pt}\pgfsys@curveto{-3.8059pt}{-14.44846pt}{-6.89111pt}{-17.53368pt}{-6.89111pt}{-21.33957pt}\pgfsys@curveto{-6.89111pt}{-25.14546pt}{-3.8059pt}{-28.23068pt}{0.0pt}{-28.23068pt}\pgfsys@curveto{3.8059pt}{-28.23068pt}{6.89111pt}{-25.14546pt}{6.89111pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{4}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{7.09108pt}{21.33948pt}\pgfsys@lineto{35.58788pt}{21.33948pt}\pgfsys@moveto{42.67886pt}{14.2484pt}\pgfsys@lineto{42.67896pt}{-14.2484pt}\pgfsys@moveto{35.58788pt}{-21.33948pt}\pgfsys@lineto{7.09108pt}{-21.33948pt}\pgfsys@moveto{0.0pt}{-14.2484pt}\pgfsys@lineto{0.0pt}{14.2484pt}\pgfsys@stroke\pgfsys@invoke{ } \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{37.66481pt}{-16.32532pt}\pgfsys@lineto{5.01414pt}{16.32532pt}\pgfsys@stroke\pgfsys@invoke{ } \par \pgfsys@invoke{ }\pgfsys@endscope{}{}{}\hss}\pgfsys@discardpath\pgfsys@invoke{ }\pgfsys@endscope\hss}}\endpgfpicture}}}\quad\boldsymbol{A}\_{\*}=\begin{bmatrix}\frac{1}{7}&\frac{5}{14}&\frac{1}{7}&\frac{5}{14}\\[2.0pt] \frac{5}{14}&\frac{2}{7}&\frac{5}{14}&0\\[2.0pt] \frac{1}{7}&\frac{5}{14}&\frac{1}{7}&\frac{5}{14}\\[2.0pt] \frac{5}{14}&0&\frac{5}{14}&\frac{2}{7}\end{bmatrix}, |  |

and 12​tr⁡(𝑨∗​𝚺​𝑨∗⊤)=1921≈0.905\frac{1}{2}\operatorname{tr}(\boldsymbol{A}\_{\*}\boldsymbol{\Sigma}\boldsymbol{A}\_{\*}^{\top})=\frac{19}{21}\approx 0.905. Adding positive correlation between the losses makes it harder to effectively share risk due to the increased chance of simultaneous loss, which results in an increase of the objective function.

#### 2.2.4. Negative correlated losses

Finally, we modify the previous example by changing the covariance matrix 𝚺\boldsymbol{\Sigma} such that some losses are negatively correlated:

|  |  |  |
| --- | --- | --- |
|  | 𝝁=𝟏𝚺=[1−130−13−131−1300−131−13−130−131] 1234𝑨∗=[523134652313461346102313460523134652313461346013461023],\boldsymbol{\mu}=\boldsymbol{1}\quad\boldsymbol{\Sigma}=\left[\begin{array}[]{rrrr}1&-\frac{1}{3}&0&-\frac{1}{3}\\[2.0pt] -\frac{1}{3}&1&-\frac{1}{3}&0\\[2.0pt] 0&-\frac{1}{3}&1&-\frac{1}{3}\\[2.0pt] -\frac{1}{3}&0&-\frac{1}{3}&1\end{array}\right]\quad\raisebox{-0.45pt}{ \hbox to56.86pt{\vbox to56.86pt{\pgfpicture\makeatletter\hbox{\quad\lower-28.43068pt\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\pgfsys@setlinewidth{\the\pgflinewidth}\pgfsys@invoke{ }\nullfont\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }{{}} \par{{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{21.33957pt}\pgfsys@curveto{6.89111pt}{25.14546pt}{3.8059pt}{28.23068pt}{0.0pt}{28.23068pt}\pgfsys@curveto{-3.8059pt}{28.23068pt}{-6.89111pt}{25.14546pt}{-6.89111pt}{21.33957pt}\pgfsys@curveto{-6.89111pt}{17.53368pt}{-3.8059pt}{14.44846pt}{0.0pt}{14.44846pt}\pgfsys@curveto{3.8059pt}{14.44846pt}{6.89111pt}{17.53368pt}{6.89111pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{1}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{21.33957pt}\pgfsys@curveto{49.57025pt}{25.14546pt}{46.48503pt}{28.23068pt}{42.67914pt}{28.23068pt}\pgfsys@curveto{38.87325pt}{28.23068pt}{35.78802pt}{25.14546pt}{35.78802pt}{21.33957pt}\pgfsys@curveto{35.78802pt}{17.53368pt}{38.87325pt}{14.44846pt}{42.67914pt}{14.44846pt}\pgfsys@curveto{46.48503pt}{14.44846pt}{49.57025pt}{17.53368pt}{49.57025pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{2}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{-21.33957pt}\pgfsys@curveto{49.57025pt}{-17.53368pt}{46.48503pt}{-14.44846pt}{42.67914pt}{-14.44846pt}\pgfsys@curveto{38.87325pt}{-14.44846pt}{35.78802pt}{-17.53368pt}{35.78802pt}{-21.33957pt}\pgfsys@curveto{35.78802pt}{-25.14546pt}{38.87325pt}{-28.23068pt}{42.67914pt}{-28.23068pt}\pgfsys@curveto{46.48503pt}{-28.23068pt}{49.57025pt}{-25.14546pt}{49.57025pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{3}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{-21.33957pt}\pgfsys@curveto{6.89111pt}{-17.53368pt}{3.8059pt}{-14.44846pt}{0.0pt}{-14.44846pt}\pgfsys@curveto{-3.8059pt}{-14.44846pt}{-6.89111pt}{-17.53368pt}{-6.89111pt}{-21.33957pt}\pgfsys@curveto{-6.89111pt}{-25.14546pt}{-3.8059pt}{-28.23068pt}{0.0pt}{-28.23068pt}\pgfsys@curveto{3.8059pt}{-28.23068pt}{6.89111pt}{-25.14546pt}{6.89111pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{4}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{7.09108pt}{21.33948pt}\pgfsys@lineto{35.58788pt}{21.33948pt}\pgfsys@moveto{42.67886pt}{14.2484pt}\pgfsys@lineto{42.67896pt}{-14.2484pt}\pgfsys@moveto{35.58788pt}{-21.33948pt}\pgfsys@lineto{7.09108pt}{-21.33948pt}\pgfsys@moveto{0.0pt}{-14.2484pt}\pgfsys@lineto{0.0pt}{14.2484pt}\pgfsys@stroke\pgfsys@invoke{ } \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{37.66481pt}{-16.32532pt}\pgfsys@lineto{5.01414pt}{16.32532pt}\pgfsys@stroke\pgfsys@invoke{ } \par \pgfsys@invoke{ }\pgfsys@endscope{}{}{}\hss}\pgfsys@discardpath\pgfsys@invoke{ }\pgfsys@endscope\hss}}\endpgfpicture}}}\quad\boldsymbol{A}\_{\*}=\begin{bmatrix}\frac{5}{23}&\frac{13}{46}&\frac{5}{23}&\frac{13}{46}\\[2.0pt] \frac{13}{46}&\frac{10}{23}&\frac{13}{46}&0\\[2.0pt] \frac{5}{23}&\frac{13}{46}&\frac{5}{23}&\frac{13}{46}\\[2.0pt] \frac{13}{46}&0&\frac{13}{46}&\frac{10}{23}\end{bmatrix}, |  |

and 12​tr⁡(𝑨∗​𝚺​𝑨∗⊤)=1969≈0.275\frac{1}{2}\operatorname{tr}(\boldsymbol{A}\_{\*}\boldsymbol{\Sigma}\boldsymbol{A}\_{\*}^{\top})=\frac{19}{69}\approx 0.275. The negative correlations make risk-sharing more effective, so the objective function decreases relative to the previous example.

###### Remark 2.2.

So far, the basic examples of 𝑨∗\boldsymbol{A}\_{\*} above have been symmetric matrices with nonnegative entries. We emphasize that neither property holds in general.
For additional, more general, examples of Theorem [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem1 "Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") see §[2.6](https://arxiv.org/html/2602.05155v1#S2.SS6 "2.6. Examples where optimal matrices have negative entries ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") and §[2.7](https://arxiv.org/html/2602.05155v1#S2.SS7 "2.7. Barbell network example ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance").

### 2.3. Friends take equal shares of risk

In this section, we study a special case of the network optimization problem ([4](https://arxiv.org/html/2602.05155v1#S2.E4 "In 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")), where friends of an agent take on an equal share of the agent’s risk. Due to this additional restriction, the objective function will, in general, increase compared to the previous unrestricted model, in exchange for equitably distributing risk between friends.

###### Definition 2.2 (Friends take an equal share of risk).

Let H​(𝑿)=𝑨​𝑿H(\boldsymbol{X})=\boldsymbol{A}\boldsymbol{X} be a linear risk-sharing rule, for matrix 𝑨=(ai​j)∈ℝn×n\boldsymbol{A}=(a\_{ij})\in\mathbb{R}^{n\times n}. We say that the risk-sharing rule has the property that friends take an equal share of risk if

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | ai1​j=ai2​j,∀{i1,j},{i2,j}∈E.a\_{i\_{1}j}=a\_{i\_{2}j},\quad\forall\{i\_{1},j\},\{i\_{2},j\}\in E. |  |

Informally speaking, this definition ensures that each of the friends of agent jj takes an equal share of the loss XjX\_{j} of agent jj. In terms of the matrix 𝑨\boldsymbol{A}, this definition imposes the condition that all the nonzero off-diagonal entries in each column are the same. This assumption is motivated by the network reciprocal contract with maximum contribution as studied in [[10](https://arxiv.org/html/2602.05155v1#bib.bib10)].
Taking these restrictions into account, the optimization problem for the risk-sharing rule H​(𝑿)=𝑨​𝑿H(\boldsymbol{X})=\boldsymbol{A}\boldsymbol{X} becomes

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | {minimize12​tr⁡(𝑨​𝚺​𝑨⊤)subject to𝟏⊤​𝑨=𝟏⊤,𝑨​𝝁=𝝁,ai​j≠0⟹{i,j}∈E,ai1​j=ai2​j,∀{i1,j},{i2,j}∈E,\begin{cases}\text{minimize}&\frac{1}{2}\operatorname{tr}(\boldsymbol{A}\boldsymbol{\Sigma}\boldsymbol{A}^{\top})\\ \text{subject to}&\boldsymbol{1}^{\top}\boldsymbol{A}=\boldsymbol{1}^{\top},\quad\boldsymbol{A}\boldsymbol{\mu}=\boldsymbol{\mu},\quad a\_{ij}\not=0\implies\{i,j\}\in E,\\ &a\_{i\_{1}j}=a\_{i\_{2}j},\quad\forall\{i\_{1},j\},\{i\_{2},j\}\in E,\end{cases} |  |

where the minimization is taken over all 𝑨=(ai​j)∈ℝn×n.\boldsymbol{A}=(a\_{ij})\in\mathbb{R}^{n\times n}.

Before stating our second main result, we review some standard concepts related to the graph Laplacian 𝑳\boldsymbol{L} of a graph. For this,
recall that the adjacency matrix 𝑾=(wi​j)∈ℝn×n\boldsymbol{W}=(w\_{ij})\in\mathbb{R}^{n\times n} of the graph G=(V,E)G=(V,E) with vertices V={1,…,n}V=\{1,\ldots,n\} is the n×nn\times n matrix with entries

|  |  |  |
| --- | --- | --- |
|  | wi​j={1,{i,j}∈E,0,otherwise.w\_{ij}=\begin{cases}1,&\{i,j\}\in E,\\ 0,&\text{otherwise}.\end{cases} |  |

The graph Laplacian 𝑳\boldsymbol{L} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | 𝑳=𝑫−𝑾,\boldsymbol{L=D-W}, |  |

where 𝑫=diag⁡(d1,…,dn)\boldsymbol{D}=\operatorname{diag}(d\_{1},\ldots,d\_{n}) is the diagonal matrix with diagonal entries did\_{i} given by the degree of agent ii.
Finally, recall that a graph is connected if there is a path between any two vertices, where a path between ii and jj is a sequence of edges {i1,i2}\{i\_{1},i\_{2}\}, {i2,i3}\{i\_{2},i\_{3}\}, {i3,i4},…,{im−1,im}\{i\_{3},i\_{4}\},\ldots,\{i\_{m-1},i\_{m}\} such that i=i1i=i\_{1} and j=imj=i\_{m}.

Our next result characterizes the solution to the optimization problem ([8](https://arxiv.org/html/2602.05155v1#S2.E8 "In 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) for the risk-sharing rule H​(𝑿)=𝑨​𝑿H(\boldsymbol{X})=\boldsymbol{A}\boldsymbol{X} for connected graphs.

###### Theorem 2.2 (Friends take an equal share of risk).

The optimization problem ([8](https://arxiv.org/html/2602.05155v1#S2.E8 "In 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) has a unique solution

|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | 𝑨^=𝑰−c^​𝑳​𝑴−1,forc^=tr⁡(𝚺​𝑳​𝑴−1)tr⁡(𝑳​𝑴−1​𝚺​𝑴−1​𝑳),\boldsymbol{\hat{A}}=\boldsymbol{I}-\hat{c}\boldsymbol{L}\boldsymbol{M}^{-1},\quad\text{for}\quad\hat{c}=\frac{\operatorname{tr}\left(\boldsymbol{\Sigma}\boldsymbol{L}\boldsymbol{M}^{-1}\right)}{\operatorname{tr}\left(\boldsymbol{L}\boldsymbol{M}^{-1}\boldsymbol{\Sigma}\boldsymbol{M}^{-1}\boldsymbol{L}\right)}, |  |

where 𝐌=diag⁡(μ1,…,μn)\boldsymbol{M}=\operatorname{diag}(\mu\_{1},\ldots,\mu\_{n}), and 𝐋\boldsymbol{L} is the graph Laplacian.

###### Proof of Theorem [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem2 "Theorem 2.2 (Friends take an equal share of risk). ‣ 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance").

First, we derive the general form of a risk-sharing matrix 𝑨=(ai​j)∈ℝn×n\boldsymbol{A}=(a\_{ij})\in\mathbb{R}^{n\times n} that satisfies the constraints of ([8](https://arxiv.org/html/2602.05155v1#S2.E8 "In 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")).
Together, the conditions
ai​j≠0⟹{i,j}∈Ea\_{ij}\not=0\implies\{i,j\}\in E and
ai1​j=ai2​j,∀{i1,j},{i2,j}∈Ea\_{i\_{1}j}=a\_{i\_{2}j},\forall\{i\_{1},j\},\{i\_{2},j\}\in E
imply that

|  |  |  |
| --- | --- | --- |
|  | ai​j={tjfor ​i=jsjfor ​{i,j}∈E0otherwise,a\_{ij}=\begin{cases}t\_{j}&\text{for }i=j\\ s\_{j}&\text{for }\{i,j\}\in E\\ 0&\text{otherwise},\end{cases} |  |

for some values t1,…,tn∈ℝt\_{1},\ldots,t\_{n}\in\mathbb{R} and s1,…,sn∈ℝs\_{1},\ldots,s\_{n}\in\mathbb{R}.
Further taking into account the constraint 𝟏⊤​𝑨=𝟏⊤\boldsymbol{1}^{\top}\boldsymbol{A}=\boldsymbol{1}^{\top}, we have

|  |  |  |
| --- | --- | --- |
|  | ti=1−di​si,t\_{i}=1-d\_{i}s\_{i}, |  |

where did\_{i} is the degree of vertex ii. So, in matrix notation, 𝑨\boldsymbol{A} is of the form

|  |  |  |  |
| --- | --- | --- | --- |
| (11) |  | 𝑨=𝑰−𝑳​𝑺,\boldsymbol{A}=\boldsymbol{I}-\boldsymbol{L}\boldsymbol{S}, |  |

where 𝑳\boldsymbol{L} is the graph Laplacian defined in ([9](https://arxiv.org/html/2602.05155v1#S2.E9 "In 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")), and 𝑺=diag⁡(s1,…,sn)\boldsymbol{S}=\operatorname{diag}(s\_{1},\ldots,s\_{n}).
Next, we consider the constraint
𝑨​𝝁=𝝁\boldsymbol{A}\boldsymbol{\mu}=\boldsymbol{\mu}, which together with ([11](https://arxiv.org/html/2602.05155v1#S2.E11 "In Proof of Theorem 2.2. ‣ 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) yields the equation

|  |  |  |
| --- | --- | --- |
|  | 𝝁−𝑳​𝑺​𝝁=𝝁,\boldsymbol{\mu}-\boldsymbol{L}\boldsymbol{S}\boldsymbol{\mu}=\boldsymbol{\mu}, |  |

or equivalently 𝑳​𝑺​𝝁=𝟎\boldsymbol{L}\boldsymbol{S}\boldsymbol{\mu}=\boldsymbol{0}.
As the underlying graph is connected by assumption, the Laplacian 𝑳\boldsymbol{L} has a one-dimensional null space spanned by the all-ones vector 𝟏\boldsymbol{1}, see for example,
[[12](https://arxiv.org/html/2602.05155v1#bib.bib12), Chapter 1.3]. Thus, the risk-sharing rule is actuarily fair only when 𝑺​𝝁=c​𝟏\boldsymbol{S}\boldsymbol{\mu}=c\boldsymbol{1} for some constant c∈ℝc\in\mathbb{R}. It follows that

|  |  |  |  |
| --- | --- | --- | --- |
| (12) |  | 𝑨=𝑰−c​𝑳​𝑴−1,\boldsymbol{A}=\boldsymbol{I}-c\boldsymbol{L}\boldsymbol{M}^{-1}, |  |

where 𝑴=diag⁡(μ1,…,μn)\boldsymbol{M}=\operatorname{diag}(\mu\_{1},\ldots,\mu\_{n}) and c∈ℝc\in\mathbb{R}.

Next, we optimize the parameter c∈ℝc\in\mathbb{R}.
Substituting ([12](https://arxiv.org/html/2602.05155v1#S2.E12 "In Proof of Theorem 2.2. ‣ 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) into the objective function
of the optimization problem ([8](https://arxiv.org/html/2602.05155v1#S2.E8 "In 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")), and
using the linearity of the trace, and the fact that the trace of a matrix is equal to the trace of its transpose, gives

|  |  |  |
| --- | --- | --- |
|  | 12​tr⁡(𝑨​𝚺​𝑨⊤)=12​tr⁡(𝚺)−c​tr⁡(𝑳​𝑴−1​𝚺)+12​c2​tr⁡(𝑳​𝑴−1​𝚺​𝑴−1​𝑳).\frac{1}{2}\operatorname{tr}(\boldsymbol{A}\boldsymbol{\Sigma}\boldsymbol{A}^{\top})=\frac{1}{2}\operatorname{tr}\left(\boldsymbol{\Sigma}\right)-c\operatorname{tr}(\boldsymbol{L}\boldsymbol{M}^{-1}\boldsymbol{\Sigma})+\frac{1}{2}c^{2}\operatorname{tr}(\boldsymbol{L}\boldsymbol{M}^{-1}\boldsymbol{\Sigma}\boldsymbol{M}^{-1}\boldsymbol{L}). |  |

Setting the derivative of this expression with respect to cc equal to zero and solving for the critical point c^\hat{c} gives

|  |  |  |  |
| --- | --- | --- | --- |
| (13) |  | c^=tr⁡(𝚺​𝑳​𝑴−1)tr⁡(𝑳​𝑴−1​𝚺​𝑴−1​𝑳).\hat{c}=\frac{\operatorname{tr}\left(\boldsymbol{\Sigma}\boldsymbol{L}\boldsymbol{M}^{-1}\right)}{\operatorname{tr}\left(\boldsymbol{L}\boldsymbol{M}^{-1}\boldsymbol{\Sigma}\boldsymbol{M}^{-1}\boldsymbol{L}\right)}. |  |

Since the objective function is convex, this critical point is its minimum, and the proof is complete.
∎

Note that if the graph GG is not connected, then this theorem can be applied to each connected component of the graph.

###### Remark 2.3 (Special cases of Theorem [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem2 "Theorem 2.2 (Friends take an equal share of risk). ‣ 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")).

When the losses are uncorrelated and 𝚺=diag⁡(σ12,…,σn2)\boldsymbol{\Sigma}=\operatorname{diag}(\sigma\_{1}^{2},\ldots,\sigma\_{n}^{2}) we have

|  |  |  |
| --- | --- | --- |
|  | c^=∑i=1ndi​μi−1​σi2∑i=1n(di2+di)​σi2​μi−2.\hat{c}=\frac{\sum\_{i=1}^{n}d\_{i}\mu\_{i}^{-1}\sigma\_{i}^{2}}{\sum\_{i=1}^{n}(d\_{i}^{2}+d\_{i})\sigma\_{i}^{2}\mu\_{i}^{-2}}. |  |

Furthermore, if the underlying graph is dd-regular (meaning that each vertex ii has degree di=dd\_{i}=d), and the loss random vector 𝑿\boldsymbol{X} has i.i.d. entries such that the mean 𝝁=μ​𝟏\boldsymbol{\mu}=\mu\boldsymbol{1} and variance 𝚺=σ2​𝑰\boldsymbol{\Sigma}=\sigma^{2}\boldsymbol{I}, then

|  |  |  |
| --- | --- | --- |
|  | c^=d​μ−1​σ2(d2+d)​σ2​μ−2=μd+1,and𝑨^=𝑰−1d+1​𝑳,\hat{c}=\frac{d\mu^{-1}\sigma^{2}}{(d^{2}+d)\sigma^{2}\mu^{-2}}=\frac{\mu}{d+1},\qquad\text{and}\qquad\boldsymbol{\hat{A}}=\boldsymbol{I}-\frac{1}{d+1}\boldsymbol{L}, |  |

which corresponds to each agent ii sharing their loss equally with their friends: agent ii keeps 1/(d+1)1/(d+1) of their own loss, and each of their dd friends takes 1/(d+1)1/(d+1) agent ii’s loss.

### 2.4. Examples of Theorem [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem2 "Theorem 2.2 (Friends take an equal share of risk). ‣ 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")

In the following, we revisit three examples from
§[2.2](https://arxiv.org/html/2602.05155v1#S2.SS2 "2.2. Examples of Theorem 2.1 ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") to illustrate how 𝑨^\boldsymbol{\hat{A}} from Theorem [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem2 "Theorem 2.2 (Friends take an equal share of risk). ‣ 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") differs from 𝑨∗\boldsymbol{A}\_{\*} from Theorem [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem1 "Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance").
In each example, we restate the mean vector 𝝁\boldsymbol{\mu}, covariance matrix 𝚺\boldsymbol{\Sigma}, and graph G=(V,E)G=(V,E), and use Theorem [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem2 "Theorem 2.2 (Friends take an equal share of risk). ‣ 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")
to determine the unique 𝑨^\boldsymbol{\hat{A}} that solves the optimization problem ([8](https://arxiv.org/html/2602.05155v1#S2.E8 "In 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")), and report the value of 12​tr⁡(𝑨^​𝚺​𝑨^⊤)\frac{1}{2}\operatorname{tr}(\boldsymbol{\hat{A}}\boldsymbol{\Sigma}\boldsymbol{\hat{A}}^{\top}).

#### 2.4.1. Complete graph

For the complete graph with uncorrelated losses with unit mean and variance, see
§[2.2.1](https://arxiv.org/html/2602.05155v1#S2.SS2.SSS1 "2.2.1. Complete graph ‣ 2.2. Examples of Theorem 2.1 ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), the optimal solution 𝑨∗\boldsymbol{A}\_{\*} already fulfills the condition that friends take an equal share of risk, so the optimal risk-sharing matrix 𝑨^\boldsymbol{\hat{A}} does not change from 𝑨∗.\boldsymbol{A}\_{\*}. This example shows how networks in the dd-regular and i.i.d. case of Remark [2.3](https://arxiv.org/html/2602.05155v1#S2.Thmremark3 "Remark 2.3 (Special cases of Theorem 2.2). ‣ 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") already share risk equally among friends.

#### 2.4.2. Complete graph with one edge removed

Next, we revisit the example from
§[2.2.2](https://arxiv.org/html/2602.05155v1#S2.SS2.SSS2 "2.2.2. Complete graph with one edge removed ‣ 2.2. Examples of Theorem 2.1 ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") of a complete graph with one edge removed and uncorrelated losses. Here, we have

|  |  |  |
| --- | --- | --- |
|  | 𝝁=𝟏𝚺=𝑰 1234𝑨^=[1651851851851849518051851816518518051849],\boldsymbol{\mu}=\boldsymbol{1}\quad\boldsymbol{\Sigma}=\boldsymbol{I}\quad\raisebox{-0.45pt}{ \hbox to56.86pt{\vbox to56.86pt{\pgfpicture\makeatletter\hbox{\quad\lower-28.43068pt\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\pgfsys@setlinewidth{\the\pgflinewidth}\pgfsys@invoke{ }\nullfont\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }{{}} \par{{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{21.33957pt}\pgfsys@curveto{6.89111pt}{25.14546pt}{3.8059pt}{28.23068pt}{0.0pt}{28.23068pt}\pgfsys@curveto{-3.8059pt}{28.23068pt}{-6.89111pt}{25.14546pt}{-6.89111pt}{21.33957pt}\pgfsys@curveto{-6.89111pt}{17.53368pt}{-3.8059pt}{14.44846pt}{0.0pt}{14.44846pt}\pgfsys@curveto{3.8059pt}{14.44846pt}{6.89111pt}{17.53368pt}{6.89111pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{1}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{21.33957pt}\pgfsys@curveto{49.57025pt}{25.14546pt}{46.48503pt}{28.23068pt}{42.67914pt}{28.23068pt}\pgfsys@curveto{38.87325pt}{28.23068pt}{35.78802pt}{25.14546pt}{35.78802pt}{21.33957pt}\pgfsys@curveto{35.78802pt}{17.53368pt}{38.87325pt}{14.44846pt}{42.67914pt}{14.44846pt}\pgfsys@curveto{46.48503pt}{14.44846pt}{49.57025pt}{17.53368pt}{49.57025pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{2}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{-21.33957pt}\pgfsys@curveto{49.57025pt}{-17.53368pt}{46.48503pt}{-14.44846pt}{42.67914pt}{-14.44846pt}\pgfsys@curveto{38.87325pt}{-14.44846pt}{35.78802pt}{-17.53368pt}{35.78802pt}{-21.33957pt}\pgfsys@curveto{35.78802pt}{-25.14546pt}{38.87325pt}{-28.23068pt}{42.67914pt}{-28.23068pt}\pgfsys@curveto{46.48503pt}{-28.23068pt}{49.57025pt}{-25.14546pt}{49.57025pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{3}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{-21.33957pt}\pgfsys@curveto{6.89111pt}{-17.53368pt}{3.8059pt}{-14.44846pt}{0.0pt}{-14.44846pt}\pgfsys@curveto{-3.8059pt}{-14.44846pt}{-6.89111pt}{-17.53368pt}{-6.89111pt}{-21.33957pt}\pgfsys@curveto{-6.89111pt}{-25.14546pt}{-3.8059pt}{-28.23068pt}{0.0pt}{-28.23068pt}\pgfsys@curveto{3.8059pt}{-28.23068pt}{6.89111pt}{-25.14546pt}{6.89111pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{4}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{7.09108pt}{21.33948pt}\pgfsys@lineto{35.58788pt}{21.33948pt}\pgfsys@moveto{42.67886pt}{14.2484pt}\pgfsys@lineto{42.67896pt}{-14.2484pt}\pgfsys@moveto{35.58788pt}{-21.33948pt}\pgfsys@lineto{7.09108pt}{-21.33948pt}\pgfsys@moveto{0.0pt}{-14.2484pt}\pgfsys@lineto{0.0pt}{14.2484pt}\pgfsys@stroke\pgfsys@invoke{ } \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{37.66481pt}{-16.32532pt}\pgfsys@lineto{5.01414pt}{16.32532pt}\pgfsys@stroke\pgfsys@invoke{ } \par \pgfsys@invoke{ }\pgfsys@endscope{}{}{}\hss}\pgfsys@discardpath\pgfsys@invoke{ }\pgfsys@endscope\hss}}\endpgfpicture}}}\quad\boldsymbol{\hat{A}}=\begin{bmatrix}\frac{1}{6}&\frac{5}{18}&\frac{5}{18}&\frac{5}{18}\\[2.0pt] \frac{5}{18}&\frac{4}{9}&\frac{5}{18}&0\\[2.0pt] \frac{5}{18}&\frac{5}{18}&\frac{1}{6}&\frac{5}{18}\\[2.0pt] \frac{5}{18}&0&\frac{5}{18}&\frac{4}{9}\end{bmatrix}, |  |

and 12​tr⁡(𝑨^​𝚺​𝑨^⊤)=1118≈0.611\frac{1}{2}\operatorname{tr}(\boldsymbol{\hat{A}}\boldsymbol{\Sigma}\boldsymbol{\hat{A}}^{\top})=\frac{11}{18}\approx 0.611.
The optimal trace slightly increases compared to the original example, while the new optimized risk-sharing matrix now meets the friends take equal shares of risk condition.

#### 2.4.3. Positive correlation

Next, we revisit the case of the network with positively correlated losses and one missing edge (§[2.2.3](https://arxiv.org/html/2602.05155v1#S2.SS2.SSS3 "2.2.3. Positive correlated losses ‣ 2.2. Examples of Theorem 2.1 ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")).
Here, we have

|  |  |  |
| --- | --- | --- |
|  | 𝝁=𝟏𝚺=[113013131130013113130131] 1234𝑨^=[538113811381138113881911380113811385381138113801138819],\boldsymbol{\mu}=\boldsymbol{1}\quad\boldsymbol{\Sigma}=\begin{bmatrix}1&\frac{1}{3}&0&\frac{1}{3}\\[2.0pt] \frac{1}{3}&1&\frac{1}{3}&0\\[2.0pt] 0&\frac{1}{3}&1&\frac{1}{3}\\[2.0pt] \frac{1}{3}&0&\frac{1}{3}&1\end{bmatrix}\quad\raisebox{-0.45pt}{ \hbox to56.86pt{\vbox to56.86pt{\pgfpicture\makeatletter\hbox{\quad\lower-28.43068pt\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\pgfsys@setlinewidth{\the\pgflinewidth}\pgfsys@invoke{ }\nullfont\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }{{}} \par{{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{21.33957pt}\pgfsys@curveto{6.89111pt}{25.14546pt}{3.8059pt}{28.23068pt}{0.0pt}{28.23068pt}\pgfsys@curveto{-3.8059pt}{28.23068pt}{-6.89111pt}{25.14546pt}{-6.89111pt}{21.33957pt}\pgfsys@curveto{-6.89111pt}{17.53368pt}{-3.8059pt}{14.44846pt}{0.0pt}{14.44846pt}\pgfsys@curveto{3.8059pt}{14.44846pt}{6.89111pt}{17.53368pt}{6.89111pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{1}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{21.33957pt}\pgfsys@curveto{49.57025pt}{25.14546pt}{46.48503pt}{28.23068pt}{42.67914pt}{28.23068pt}\pgfsys@curveto{38.87325pt}{28.23068pt}{35.78802pt}{25.14546pt}{35.78802pt}{21.33957pt}\pgfsys@curveto{35.78802pt}{17.53368pt}{38.87325pt}{14.44846pt}{42.67914pt}{14.44846pt}\pgfsys@curveto{46.48503pt}{14.44846pt}{49.57025pt}{17.53368pt}{49.57025pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{2}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{-21.33957pt}\pgfsys@curveto{49.57025pt}{-17.53368pt}{46.48503pt}{-14.44846pt}{42.67914pt}{-14.44846pt}\pgfsys@curveto{38.87325pt}{-14.44846pt}{35.78802pt}{-17.53368pt}{35.78802pt}{-21.33957pt}\pgfsys@curveto{35.78802pt}{-25.14546pt}{38.87325pt}{-28.23068pt}{42.67914pt}{-28.23068pt}\pgfsys@curveto{46.48503pt}{-28.23068pt}{49.57025pt}{-25.14546pt}{49.57025pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{3}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{-21.33957pt}\pgfsys@curveto{6.89111pt}{-17.53368pt}{3.8059pt}{-14.44846pt}{0.0pt}{-14.44846pt}\pgfsys@curveto{-3.8059pt}{-14.44846pt}{-6.89111pt}{-17.53368pt}{-6.89111pt}{-21.33957pt}\pgfsys@curveto{-6.89111pt}{-25.14546pt}{-3.8059pt}{-28.23068pt}{0.0pt}{-28.23068pt}\pgfsys@curveto{3.8059pt}{-28.23068pt}{6.89111pt}{-25.14546pt}{6.89111pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{4}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{7.09108pt}{21.33948pt}\pgfsys@lineto{35.58788pt}{21.33948pt}\pgfsys@moveto{42.67886pt}{14.2484pt}\pgfsys@lineto{42.67896pt}{-14.2484pt}\pgfsys@moveto{35.58788pt}{-21.33948pt}\pgfsys@lineto{7.09108pt}{-21.33948pt}\pgfsys@moveto{0.0pt}{-14.2484pt}\pgfsys@lineto{0.0pt}{14.2484pt}\pgfsys@stroke\pgfsys@invoke{ } \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{37.66481pt}{-16.32532pt}\pgfsys@lineto{5.01414pt}{16.32532pt}\pgfsys@stroke\pgfsys@invoke{ } \par \pgfsys@invoke{ }\pgfsys@endscope{}{}{}\hss}\pgfsys@discardpath\pgfsys@invoke{ }\pgfsys@endscope\hss}}\endpgfpicture}}}\quad\boldsymbol{\hat{A}}=\begin{bmatrix}\frac{5}{38}&\frac{11}{38}&\frac{11}{38}&\frac{11}{38}\\[2.0pt] \frac{11}{38}&\frac{8}{19}&\frac{11}{38}&0\\[2.0pt] \frac{11}{38}&\frac{11}{38}&\frac{5}{38}&\frac{11}{38}\\[2.0pt] \frac{11}{38}&0&\frac{11}{38}&\frac{8}{19}\end{bmatrix}, |  |

and 12​tr⁡(𝑨^​𝚺​𝑨^⊤)=107114≈0.938.\frac{1}{2}\operatorname{tr}(\boldsymbol{\hat{A}}\boldsymbol{\Sigma}\boldsymbol{\hat{A}}^{\top})=\frac{107}{114}\approx 0.938.
Once again, there is a slight increase in the objective, relative to the result in §[2.2.3](https://arxiv.org/html/2602.05155v1#S2.SS2.SSS3 "2.2.3. Positive correlated losses ‣ 2.2. Examples of Theorem 2.1 ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), as a consequence of the additional condition that friends take an equal share of risk.

#### 2.4.4. Negative correlation

Finally, revisit the case of the network with negatively correlated losses and one missing edge
(§[2.2.4](https://arxiv.org/html/2602.05155v1#S2.SS2.SSS4 "2.2.4. Negative correlated losses ‣ 2.2. Examples of Theorem 2.1 ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")). Here, we have

|  |  |  |
| --- | --- | --- |
|  | 𝝁=𝟏𝚺=[1−130−13−131−1300−131−13−130−131] 1234𝑨^=[523134652313461346102313460523134652313461346013461023],\boldsymbol{\mu}=\boldsymbol{1}\quad\boldsymbol{\Sigma}=\begin{bmatrix}1&-\frac{1}{3}&0&-\frac{1}{3}\\[2.0pt] -\frac{1}{3}&1&-\frac{1}{3}&0\\[2.0pt] 0&-\frac{1}{3}&1&-\frac{1}{3}\\[2.0pt] -\frac{1}{3}&0&-\frac{1}{3}&1\end{bmatrix}\quad\raisebox{-0.45pt}{ \hbox to56.86pt{\vbox to56.86pt{\pgfpicture\makeatletter\hbox{\quad\lower-28.43068pt\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\pgfsys@setlinewidth{\the\pgflinewidth}\pgfsys@invoke{ }\nullfont\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }{{}} \par{{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{21.33957pt}\pgfsys@curveto{6.89111pt}{25.14546pt}{3.8059pt}{28.23068pt}{0.0pt}{28.23068pt}\pgfsys@curveto{-3.8059pt}{28.23068pt}{-6.89111pt}{25.14546pt}{-6.89111pt}{21.33957pt}\pgfsys@curveto{-6.89111pt}{17.53368pt}{-3.8059pt}{14.44846pt}{0.0pt}{14.44846pt}\pgfsys@curveto{3.8059pt}{14.44846pt}{6.89111pt}{17.53368pt}{6.89111pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{1}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{21.33957pt}\pgfsys@curveto{49.57025pt}{25.14546pt}{46.48503pt}{28.23068pt}{42.67914pt}{28.23068pt}\pgfsys@curveto{38.87325pt}{28.23068pt}{35.78802pt}{25.14546pt}{35.78802pt}{21.33957pt}\pgfsys@curveto{35.78802pt}{17.53368pt}{38.87325pt}{14.44846pt}{42.67914pt}{14.44846pt}\pgfsys@curveto{46.48503pt}{14.44846pt}{49.57025pt}{17.53368pt}{49.57025pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{2}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{-21.33957pt}\pgfsys@curveto{49.57025pt}{-17.53368pt}{46.48503pt}{-14.44846pt}{42.67914pt}{-14.44846pt}\pgfsys@curveto{38.87325pt}{-14.44846pt}{35.78802pt}{-17.53368pt}{35.78802pt}{-21.33957pt}\pgfsys@curveto{35.78802pt}{-25.14546pt}{38.87325pt}{-28.23068pt}{42.67914pt}{-28.23068pt}\pgfsys@curveto{46.48503pt}{-28.23068pt}{49.57025pt}{-25.14546pt}{49.57025pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{3}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{-21.33957pt}\pgfsys@curveto{6.89111pt}{-17.53368pt}{3.8059pt}{-14.44846pt}{0.0pt}{-14.44846pt}\pgfsys@curveto{-3.8059pt}{-14.44846pt}{-6.89111pt}{-17.53368pt}{-6.89111pt}{-21.33957pt}\pgfsys@curveto{-6.89111pt}{-25.14546pt}{-3.8059pt}{-28.23068pt}{0.0pt}{-28.23068pt}\pgfsys@curveto{3.8059pt}{-28.23068pt}{6.89111pt}{-25.14546pt}{6.89111pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{4}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{7.09108pt}{21.33948pt}\pgfsys@lineto{35.58788pt}{21.33948pt}\pgfsys@moveto{42.67886pt}{14.2484pt}\pgfsys@lineto{42.67896pt}{-14.2484pt}\pgfsys@moveto{35.58788pt}{-21.33948pt}\pgfsys@lineto{7.09108pt}{-21.33948pt}\pgfsys@moveto{0.0pt}{-14.2484pt}\pgfsys@lineto{0.0pt}{14.2484pt}\pgfsys@stroke\pgfsys@invoke{ } \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{37.66481pt}{-16.32532pt}\pgfsys@lineto{5.01414pt}{16.32532pt}\pgfsys@stroke\pgfsys@invoke{ } \par \pgfsys@invoke{ }\pgfsys@endscope{}{}{}\hss}\pgfsys@discardpath\pgfsys@invoke{ }\pgfsys@endscope\hss}}\endpgfpicture}}}\quad\boldsymbol{\hat{A}}=\begin{bmatrix}\frac{5}{23}&\frac{13}{46}&\frac{5}{23}&\frac{13}{46}\\[2.0pt] \frac{13}{46}&\frac{10}{23}&\frac{13}{46}&0\\[2.0pt] \frac{5}{23}&\frac{13}{46}&\frac{5}{23}&\frac{13}{46}\\[2.0pt] \frac{13}{46}&0&\frac{13}{46}&\frac{10}{23}\\ \end{bmatrix}, |  |

and 12​tr⁡(𝑨^​𝚺​𝑨^⊤)≈0.551\frac{1}{2}\operatorname{tr}(\boldsymbol{\hat{A}}\boldsymbol{\Sigma}\boldsymbol{\hat{A}}^{\top})\approx 0.551. Once again, there is a slight increase in the objective, relative to the result in §[2.2.4](https://arxiv.org/html/2602.05155v1#S2.SS2.SSS4 "2.2.4. Negative correlated losses ‣ 2.2. Examples of Theorem 2.1 ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") as a consequence of the additional condition that friends take an equal share of risk.

### 2.5. Nonnegativity Conditions

In this section, we develop conditions for the nonnegativity of the optimal risk-sharing matrices 𝑨∗\boldsymbol{A}\_{\*} and 𝑨^\boldsymbol{\hat{A}}. While these matrices sometimes naturally have nonnegative entries (such as in the examples considered in §[2.2](https://arxiv.org/html/2602.05155v1#S2.SS2 "2.2. Examples of Theorem 2.1 ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") and §[2.4](https://arxiv.org/html/2602.05155v1#S2.SS4 "2.4. Examples of Theorem 2.2 ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")), in general, negative entries may arise in both optimization problems.

This section is organized as follows: in §[2.5.1](https://arxiv.org/html/2602.05155v1#S2.SS5.SSS1 "2.5.1. Nonnegativity Conditions for 𝑨_∗ for the case of the complete graph ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") we give conditions for the nonnegativity of 𝑨∗\boldsymbol{A}\_{\*} for the case of the complete graph, and in §[2.5.2](https://arxiv.org/html/2602.05155v1#S2.SS5.SSS2 "2.5.2. Nonnegativity conditions for 𝑨̂ ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") we provide conditions for the nonnegativity of 𝑨^\boldsymbol{\hat{A}}.

#### 2.5.1. Nonnegativity Conditions for 𝑨∗\boldsymbol{A}\_{\*} for the case of the complete graph

In the following lemmas, we state conditions on 𝝁\boldsymbol{\mu} and 𝚺\boldsymbol{\Sigma}
such that the optimal 𝑨∗\boldsymbol{A}\_{\*} defined by Theorem [1.1](https://arxiv.org/html/2602.05155v1#S1.Thmtheorem1 "Theorem 1.1 (Feng, Liu, Taylor [22]). ‣ 1.3. Prior work ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") (or equivalently, defined by Theorem [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem1 "Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") for the case of the complete graph) has nonnegative entries. We start by considering the simplified case where 𝚺\boldsymbol{\Sigma} is a scaled identity matrix, before considering the general case.

###### Lemma 2.1.

Assume that 𝚺=c​𝐈\boldsymbol{\Sigma}=c\boldsymbol{I} for some c>0,c>0, and let 𝛍¯:=(min1≤j≤n⁡μj)​𝟏.\underline{\boldsymbol{\mu}}:=(\min\_{1\leq j\leq n}\mu\_{j})\boldsymbol{1}. Then, all entries of the matrix 𝐀∗\boldsymbol{A}\_{\*} defined in Theorem [1.1](https://arxiv.org/html/2602.05155v1#S1.Thmtheorem1 "Theorem 1.1 (Feng, Liu, Taylor [22]). ‣ 1.3. Prior work ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") are nonnegative if and only if

|  |  |  |
| --- | --- | --- |
|  | ‖𝝁−𝝁¯‖1​‖𝝁‖∞≤‖𝝁‖22.\|\boldsymbol{\mu}-\underline{\boldsymbol{\mu}}\|\_{1}\|\boldsymbol{\mu}\|\_{\infty}\leq\|\boldsymbol{\mu}\|\_{2}^{2}. |  |

###### Proof of Lemma [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmlemma1 "Lemma 2.1. ‣ 2.5.1. Nonnegativity Conditions for 𝑨_∗ for the case of the complete graph ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance").

Since 𝚺=c​𝑰\boldsymbol{\Sigma}=c\boldsymbol{I}, we have

|  |  |  |
| --- | --- | --- |
|  | 𝑨∗=1n​𝟏𝟏⊤+(𝑰−1n​𝟏𝟏⊤)​𝝁​𝝁⊤𝝁⊤​𝝁.\boldsymbol{A}\_{\*}=\frac{1}{n}\boldsymbol{1}\boldsymbol{1}^{\top}+\left(\boldsymbol{I}-\frac{1}{n}\boldsymbol{1}\boldsymbol{1}^{\top}\right)\frac{\boldsymbol{\mu}\boldsymbol{\mu}^{\top}}{\boldsymbol{\mu}^{\top}\boldsymbol{\mu}}. |  |

Thus, all of the entries of 𝑨∗\boldsymbol{A}\_{\*} are nonnegative if and only if

|  |  |  |
| --- | --- | --- |
|  | 0≤1n+μj‖𝝁‖22​(μi−1n​‖𝝁‖1),∀i,j∈{1,…,n}.0\leq\frac{1}{n}+\frac{\mu\_{j}}{\|\boldsymbol{\mu}\|\_{2}^{2}}\left(\mu\_{i}-\frac{1}{n}\|\boldsymbol{\mu}\|\_{1}\right),\quad\forall i,j\in\{1,\ldots,n\}. |  |

Rearranging terms, the condition for nonnegative entries is

|  |  |  |  |
| --- | --- | --- | --- |
| (14) |  | μj​(‖𝝁‖1−n​μi)≤‖𝝁‖22,∀i,j∈{1,…,n}.\mu\_{j}(\|\boldsymbol{\mu}\|\_{1}-n\mu\_{i})\leq\|\boldsymbol{\mu}\|\_{2}^{2},\quad\forall i,j\in\{1,\ldots,n\}. |  |

The result follows from maximizing the left-hand side over ii and jj. Indeed, the maximum over ii occurs when

|  |  |  |
| --- | --- | --- |
|  | ‖𝝁‖1−n​μi=‖𝝁‖1−n​(min1≤k≤n⁡μk)=‖𝝁−𝝁¯‖1,\|\boldsymbol{\mu}\|\_{1}-n\mu\_{i}=\|\boldsymbol{\mu}\|\_{1}-n\left(\min\_{1\leq k\leq n}\mu\_{k}\right)=\|\boldsymbol{\mu}-\underline{\boldsymbol{\mu}}\|\_{1}, |  |

and the maximum over jj occurs when μj=‖𝝁‖∞\mu\_{j}=\|\boldsymbol{\mu}\|\_{\infty}.
∎

Next, we consider the case where 𝚺\boldsymbol{\Sigma} is an arbitrary positive definite matrix.

###### Proposition 2.1.

Assume that 𝚺\boldsymbol{\Sigma} is positive definite. Let
𝛍¯:=(min1≤j≤n⁡μj)​𝟏\underline{\boldsymbol{\mu}}:=(\min\_{1\leq j\leq n}\mu\_{j})\boldsymbol{1} and 𝛍¯:=(max1≤j≤n⁡μj)​𝟏\overline{\boldsymbol{\mu}}:=(\max\_{1\leq j\leq n}\mu\_{j})\boldsymbol{1}. Define

|  |  |  |
| --- | --- | --- |
|  | a:=min1≤j≤n(𝚺−1𝝁)jandb:=max1≤j≤n(𝚺−1𝝁)j.a:=\min\_{1\leq j\leq n}(\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu})\_{j}\quad\text{and}\quad b:=\max\_{1\leq j\leq n}(\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu})\_{j}. |  |

Then, all the entries of the matrix 𝐀∗\boldsymbol{A}\_{\*} defined in Theorem [1.1](https://arxiv.org/html/2602.05155v1#S1.Thmtheorem1 "Theorem 1.1 (Feng, Liu, Taylor [22]). ‣ 1.3. Prior work ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") are nonnegative if and only if

|  |  |  |
| --- | --- | --- |
|  | max⁡{−a​‖𝝁−𝝁¯‖1,b​‖𝝁−𝝁¯‖1}≤𝝁⊤​𝚺−1​𝝁.\max\left\{-a\|\boldsymbol{\mu}-\overline{\boldsymbol{\mu}}\|\_{1},b\|\boldsymbol{\mu}-\underline{\boldsymbol{\mu}}\|\_{1}\right\}\leq\boldsymbol{\mu}^{\top}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}. |  |

###### Proof of Lemma [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmproposition1 "Proposition 2.1. ‣ 2.5.1. Nonnegativity Conditions for 𝑨_∗ for the case of the complete graph ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance").

Recall that

|  |  |  |
| --- | --- | --- |
|  | 𝑨∗=1n​𝟏𝟏⊤+1𝝁⊤​𝚺​𝝁​(𝑰−1n​𝟏𝟏⊤)​𝝁​𝝁⊤​𝚺−1.\boldsymbol{A}\_{\*}=\frac{1}{n}\boldsymbol{1}\boldsymbol{1}^{\top}+\frac{1}{\boldsymbol{\mu}^{\top}\boldsymbol{\Sigma}\boldsymbol{\mu}}\left(\boldsymbol{I}-\frac{1}{n}\boldsymbol{1}\boldsymbol{1}^{\top}\right)\boldsymbol{\mu\mu}^{\top}\boldsymbol{\Sigma}^{-1}. |  |

Thus, all of the entries of 𝑨∗\boldsymbol{A}\_{\*} are nonnegative if and only if

|  |  |  |
| --- | --- | --- |
|  | 0≤1n+(𝚺−1​𝝁)j𝝁⊤​𝚺​𝝁​(μi−1n​‖𝝁‖1)∀i,j∈{1,…,n}.0\leq\frac{1}{n}+\frac{\left(\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}\right)\_{j}}{\boldsymbol{\mu}^{\top}\boldsymbol{\Sigma}\boldsymbol{\mu}}\left(\mu\_{i}-\frac{1}{n}\|\boldsymbol{\mu}\|\_{1}\right)\quad\forall i,j\in\{1,\ldots,n\}. |  |

Rearranging terms, the condition for nonnegative entries is

|  |  |  |
| --- | --- | --- |
|  | (𝚺−1​𝝁)j​(‖𝝁‖1−n​μi)≤𝝁⊤​𝚺​𝝁∀i,j∈{1,…,n}.\left(\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}\right)\_{j}\left(\|\boldsymbol{\mu}\|\_{1}-n\mu\_{i}\right)\leq\boldsymbol{\mu}^{\top}\boldsymbol{\Sigma}\boldsymbol{\mu}\quad\forall i,j\in\{1,\ldots,n\}. |  |

We proceed as above, maximizing the left-hand side over ii and jj and denote by (i∗,j∗)(i^{\*},j^{\*}) the indices at which the maximum occurs. If (𝚺−1​𝝁)j∗≥0\left(\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}\right)\_{j^{\*}}\geq 0, then

|  |  |  |
| --- | --- | --- |
|  | max1≤i,j≤n⁡((𝚺−1​𝝁)j​(‖𝝁‖1−n​μi))=(𝚺−1​𝝁)j∗​‖𝝁−𝝁¯‖1.\max\_{1\leq i,j\leq n}\left(\left(\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}\right)\_{j}\left(\|\boldsymbol{\mu}\|\_{1}-n\mu\_{i}\right)\right)=(\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu})\_{j^{\*}}\|\boldsymbol{\mu}-\underline{\boldsymbol{\mu}}\|\_{1}. |  |

Otherwise, if (𝚺−1​𝝁)j∗<0\left(\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}\right)\_{j^{\*}}<0, then

|  |  |  |
| --- | --- | --- |
|  | max1≤i,j≤n⁡((𝚺−1​𝝁)j​(‖𝝁‖1−n​μi))=−(𝚺−1​𝝁)j∗​‖𝝁−𝝁¯‖1.\max\_{1\leq i,j\leq n}\left(\left(\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}\right)\_{j}\left(\|\boldsymbol{\mu}\|\_{1}-n\mu\_{i}\right)\right)=-(\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu})\_{j^{\*}}\|\boldsymbol{\mu}-\overline{\boldsymbol{\mu}}\|\_{1}. |  |

Taking the maximum of these two cases gives the result.
∎

#### 2.5.2. Nonnegativity conditions for 𝑨^\boldsymbol{\hat{A}}

In the following, we consider a condition for the nonnegativity of the optimal risk-sharing matrix 𝑨^\boldsymbol{\hat{A}} defined in Theorem [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem2 "Theorem 2.2 (Friends take an equal share of risk). ‣ 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") for the case where friends take an equal share of risk.

###### Lemma 2.2.

Under the hypotheses of Theorem [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem2 "Theorem 2.2 (Friends take an equal share of risk). ‣ 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), assume that 𝐀^=𝐈−c^​𝐋​𝐌−1\boldsymbol{\hat{A}}=\boldsymbol{I}-\hat{c}\boldsymbol{L}\boldsymbol{M}^{-1} is defined
by ([10](https://arxiv.org/html/2602.05155v1#S2.E10 "In Theorem 2.2 (Friends take an equal share of risk). ‣ 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")). Then 𝐀^\boldsymbol{\hat{A}} has all nonnegative entries if and only if

|  |  |  |
| --- | --- | --- |
|  | 1≥c^​diμi≥0,1\geq\hat{c}\frac{d\_{i}}{\mu\_{i}}\geq 0,\quad |  |

for all 1≤i≤n.1\leq i\leq n.

###### Proof.

Let 𝑨^=𝑰−c^​𝑳​𝑴−1\boldsymbol{\hat{A}}=\boldsymbol{I}-\hat{c}\boldsymbol{LM}^{-1}, where c^\hat{c} is defined by ([10](https://arxiv.org/html/2602.05155v1#S2.E10 "In Theorem 2.2 (Friends take an equal share of risk). ‣ 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")).
First, we consider the off-diagonal entries of 𝑨^\boldsymbol{\hat{A}}. When i≠ji\not=j we have

|  |  |  |
| --- | --- | --- |
|  | (𝑨^)i​j=(𝑰−c^​𝑳​𝑴−1)i​j={c^μj,{i,j}∈E,0,{i,j}∉E.(\boldsymbol{\hat{A}})\_{ij}=(\boldsymbol{I}-\hat{c}\boldsymbol{LM}^{-1})\_{ij}=\begin{cases}\frac{\hat{c}}{\mu\_{j}},&\{i,j\}\in E,\\ 0,&\{i,j\}\notin E.\end{cases} |  |

Since we assumed the underlying graph is connected and consists of n≥2n\geq 2 nodes, there is at least one edge, and since the losses are nonnegative random variables with positive variance, each mean μj>0\mu\_{j}>0. It follows that the off-diagonal entries of 𝑨^\boldsymbol{\hat{A}} are nonnegative if and only if c^≥0\hat{c}\geq 0.
Next, we consider the diagonal entries of 𝑨^\boldsymbol{\hat{A}}. We have

|  |  |  |
| --- | --- | --- |
|  | (𝑨^)i​i=(𝑰−c^​𝑳​𝑴−1)i​i=1−c^​diμi,(\boldsymbol{\hat{A}})\_{ii}=(\boldsymbol{I}-\hat{c}\boldsymbol{LM}^{-1})\_{ii}=1-\hat{c}\frac{d\_{i}}{\mu\_{i}}, |  |

which is nonnegative if and only if c^​(di/μi)≤1\hat{c}(d\_{i}/\mu\_{i})\leq 1. Combining the inequalities from the off-diagonal and diagonal cases completes the proof.
∎

Let Cov⁡(X,Y)=𝔼​[(X−𝔼​[X])​(Y−𝔼​[Y])]\operatorname{Cov}(X,Y)=\mathbb{E}\left[\left(X-\mathbb{E}[X]\right)\left(Y-\mathbb{E}[Y]\right)\right] denote the covariance of XX and YY.

###### Corollary 2.1.

The condition c^≥0\hat{c}\geq 0 is equivalent to the condition

|  |  |  |
| --- | --- | --- |
|  | ∑{i,j}∈ECov⁡(Xi,Xj)​(1μi+1μj)≤∑i=1ndi​σi2μi.\sum\_{\{i,j\}\in E}\operatorname{Cov}(X\_{i},X\_{j})\left(\frac{1}{\mu\_{i}}+\frac{1}{\mu\_{j}}\right)\leq\sum\_{i=1}^{n}\frac{d\_{i}\sigma\_{i}^{2}}{\mu\_{i}}. |  |

###### Proof.

Recall that

|  |  |  |
| --- | --- | --- |
|  | c^=tr⁡(𝚺​𝑳​𝑴−1)tr⁡(𝑳​𝑴−1​𝚺​𝑴−1​𝑳).\hat{c}=\frac{\operatorname{tr}\left(\boldsymbol{\Sigma}\boldsymbol{L}\boldsymbol{M}^{-1}\right)}{\operatorname{tr}\left(\boldsymbol{L}\boldsymbol{M}^{-1}\boldsymbol{\Sigma}\boldsymbol{M}^{-1}\boldsymbol{L}\right)}. |  |

The term in the denominator of this expression

|  |  |  |
| --- | --- | --- |
|  | tr⁡(𝑳​𝑴−1​𝚺​𝑴−1​𝑳)=tr⁡[(𝑳​𝑴−1​𝚺12)​(𝑳​𝑴−1​𝚺12)⊤]=‖𝑳​𝑴−1​𝚺12‖F2\operatorname{tr}(\boldsymbol{LM}^{-1}\boldsymbol{\Sigma M}^{-1}\boldsymbol{L})=\operatorname{tr}[(\boldsymbol{LM}^{-1}\boldsymbol{\Sigma}^{\frac{1}{2}})(\boldsymbol{LM}^{-1}\boldsymbol{\Sigma}^{\frac{1}{2}})^{\top}]=\|\boldsymbol{LM}^{-1}\boldsymbol{\Sigma}^{\frac{1}{2}}\|\_{F}^{2} |  |

is a squared norm and is always nonnegative.
In the numerator, we have

|  |  |  |
| --- | --- | --- |
|  | tr⁡(𝚺​𝑳​𝑴−1)=∑i=1ndi​σi2−∑j:{i,j}∈ECov⁡(Xi,Xj)μi.\operatorname{tr}(\boldsymbol{\Sigma LM}^{-1})=\sum\_{i=1}^{n}\frac{d\_{i}\sigma^{2}\_{i}-\sum\_{j:\{i,j\}\in E}\operatorname{Cov}(X\_{i},X\_{j})}{\mu\_{i}}. |  |

For this sum to be nonnegative, we require

|  |  |  |
| --- | --- | --- |
|  | ∑{i,j}∈ECov⁡(Xi,Xj)​(1μi+1μj)≤∑i=1ndi​σi2μi,\sum\_{\{i,j\}\in E}\operatorname{Cov}(X\_{i},X\_{j})\left(\frac{1}{\mu\_{i}}+\frac{1}{\mu\_{j}}\right)\leq\sum\_{i=1}^{n}\frac{d\_{i}\sigma\_{i}^{2}}{\mu\_{i}}, |  |

as was to be shown.
∎

###### Remark 2.4.

As a consequence of Corollary [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmcorollary1 "Corollary 2.1. ‣ 2.5.2. Nonnegativity conditions for 𝑨̂ ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), we note that a sufficient condition for the nonnegativity of c^\hat{c} is that
for all {i,j}∈E,\{i,j\}\in E, Cov⁡(Xi,Xj)≤min⁡{σi2,σj2}.\operatorname{Cov}(X\_{i},X\_{j})\leq\min\{\sigma\_{i}^{2},\sigma\_{j}^{2}\}.

The above corollary and remark demonstrate how the nonnegativity of off-diagonal entries is dependent on covariance relative to expected losses.
In particular, we note the following result for a simple 2-agent network as it will serve as the basis for some examples in §[2.6](https://arxiv.org/html/2602.05155v1#S2.SS6 "2.6. Examples where optimal matrices have negative entries ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"). Here, a 2-agent network has graph G=(V,E),G=(V,E), with vertices V={1,2}V=\{1,2\} and edges E={(1,2)}.E=\{(1,2)\}.

###### Corollary 2.2.

In the case of a 2-agent network, the constant
c^\hat{c} is nonnegative if and only if c^≤μi\hat{c}\leq\mu\_{i} for i={1,2}i=\{1,2\} and

|  |  |  |
| --- | --- | --- |
|  | Cov⁡(X1,X2)≤σ12​μ2+σ22​μ1μ1+μ2.\operatorname{Cov}(X\_{1},X\_{2})\leq\frac{\sigma\_{1}^{2}\mu\_{2}+\sigma\_{2}^{2}\mu\_{1}}{\mu\_{1}+\mu\_{2}}. |  |

Corollary [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmcorollary2 "Corollary 2.2. ‣ 2.5.2. Nonnegativity conditions for 𝑨̂ ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") is an immediate consequence of Lemma [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmlemma2 "Lemma 2.2. ‣ 2.5.2. Nonnegativity conditions for 𝑨̂ ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") and Corollary [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmcorollary1 "Corollary 2.1. ‣ 2.5.2. Nonnegativity conditions for 𝑨̂ ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance").

### 2.6. Examples where optimal matrices have negative entries

In this section, we provide some examples where optimal risk-sharing matrices 𝑨∗\boldsymbol{A}\_{\*} and 𝑨^\boldsymbol{\hat{A}} have entries that are negative. Additionally, we illustrate how network-based restrictions can eliminate negative entries in some cases.

#### 2.6.1. Agents with losses with means at different scales

First, we consider an example where a negative entry appears due to the conditions of Lemma [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmlemma1 "Lemma 2.1. ‣ 2.5.1. Nonnegativity Conditions for 𝑨_∗ for the case of the complete graph ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") being violated. In particular, we consider a complete graph on three vertices with losses whose covariance matrix is the identity, but that have means at different scales. We have

|  |  |  |
| --- | --- | --- |
|  | 𝝁=[1414]𝚺=𝑰 123𝑨∗=[8527367273−5273882737927343273100273127273235273],\boldsymbol{\mu}=\begin{bmatrix}\frac{1}{4}\\ 1\\ 4\end{bmatrix}\quad\boldsymbol{\Sigma}=\boldsymbol{I}\quad\raisebox{-0.45pt}{ \hbox to56.86pt{\vbox to56.86pt{\pgfpicture\makeatletter\hbox{\quad\lower-28.43068pt\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\pgfsys@setlinewidth{\the\pgflinewidth}\pgfsys@invoke{ }\nullfont\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }{{}} \par{{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{28.23068pt}{21.33957pt}\pgfsys@curveto{28.23068pt}{25.14546pt}{25.14546pt}{28.23068pt}{21.33957pt}{28.23068pt}\pgfsys@curveto{17.53368pt}{28.23068pt}{14.44846pt}{25.14546pt}{14.44846pt}{21.33957pt}\pgfsys@curveto{14.44846pt}{17.53368pt}{17.53368pt}{14.44846pt}{21.33957pt}{14.44846pt}\pgfsys@curveto{25.14546pt}{14.44846pt}{28.23068pt}{17.53368pt}{28.23068pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{21.33957pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{18.83957pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{1}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{-21.33957pt}\pgfsys@curveto{49.57025pt}{-17.53368pt}{46.48503pt}{-14.44846pt}{42.67914pt}{-14.44846pt}\pgfsys@curveto{38.87325pt}{-14.44846pt}{35.78802pt}{-17.53368pt}{35.78802pt}{-21.33957pt}\pgfsys@curveto{35.78802pt}{-25.14546pt}{38.87325pt}{-28.23068pt}{42.67914pt}{-28.23068pt}\pgfsys@curveto{46.48503pt}{-28.23068pt}{49.57025pt}{-25.14546pt}{49.57025pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{2}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{-21.33957pt}\pgfsys@curveto{6.89111pt}{-17.53368pt}{3.8059pt}{-14.44846pt}{0.0pt}{-14.44846pt}\pgfsys@curveto{-3.8059pt}{-14.44846pt}{-6.89111pt}{-17.53368pt}{-6.89111pt}{-21.33957pt}\pgfsys@curveto{-6.89111pt}{-25.14546pt}{-3.8059pt}{-28.23068pt}{0.0pt}{-28.23068pt}\pgfsys@curveto{3.8059pt}{-28.23068pt}{6.89111pt}{-25.14546pt}{6.89111pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{3}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{24.51064pt}{14.99706pt}\pgfsys@lineto{39.5077pt}{-14.99706pt}\pgfsys@moveto{35.58788pt}{-21.33948pt}\pgfsys@lineto{7.09108pt}{-21.33948pt}\pgfsys@moveto{3.17116pt}{-14.99706pt}\pgfsys@lineto{18.16832pt}{14.99706pt}\pgfsys@stroke\pgfsys@invoke{ } \par\par \pgfsys@invoke{ }\pgfsys@endscope{}{}{}\hss}\pgfsys@discardpath\pgfsys@invoke{ }\pgfsys@endscope\hss}}\endpgfpicture}}}\quad\boldsymbol{A}\_{\*}=\left[\begin{array}[]{rrr}\frac{85}{273}&\frac{67}{273}&-\frac{5}{273}\\[2.0pt] \frac{88}{273}&\frac{79}{273}&\frac{43}{273}\\[2.0pt] \frac{100}{273}&\frac{127}{273}&\frac{235}{273}\end{array}\right], |  |

and 12​tr⁡(𝑨∗​𝚺​𝑨∗⊤)=1926≈0.731\frac{1}{2}\operatorname{tr}(\boldsymbol{A}\_{\*}\boldsymbol{\Sigma}\boldsymbol{A}\_{\*}^{\top})=\frac{19}{26}\approx 0.731. Recall that, when the covariance matrix 𝚺\boldsymbol{\Sigma} is a multiple of the identity, we can apply Lemma [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmlemma1 "Lemma 2.1. ‣ 2.5.1. Nonnegativity Conditions for 𝑨_∗ for the case of the complete graph ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), and thus the entries 𝑨∗\boldsymbol{A}\_{\*} are nonnegative if and only if

|  |  |  |
| --- | --- | --- |
|  | ‖𝝁−𝝁¯‖1​‖𝝁‖∞≤‖𝝁‖22where𝝁¯:=(min1≤j≤n⁡μj)​𝟏.\|\boldsymbol{\mu}-\underline{\boldsymbol{\mu}}\|\_{1}\|\boldsymbol{\mu}\|\_{\infty}\leq\|\boldsymbol{\mu}\|\_{2}^{2}\quad\text{where}\quad\underline{\boldsymbol{\mu}}:=\left(\min\_{1\leq j\leq n}\mu\_{j}\right)\boldsymbol{1}. |  |

Here,

|  |  |  |
| --- | --- | --- |
|  | ‖𝝁−𝝁¯‖1​‖𝝁‖∞=‖𝝁−14​𝟏‖1​(4)=18>17.0625=27316=‖𝝁‖22,\|\boldsymbol{\mu}-\underline{\boldsymbol{\mu}}\|\_{1}\|\boldsymbol{\mu}\|\_{\infty}=\left\|\boldsymbol{\mu}-\frac{1}{4}\boldsymbol{1}\right\|\_{1}(4)=18>17.0625=\frac{273}{16}=\|\boldsymbol{\mu}\|\_{2}^{2}, |  |

so the necessary and sufficient condition of Lemma [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmlemma1 "Lemma 2.1. ‣ 2.5.1. Nonnegativity Conditions for 𝑨_∗ for the case of the complete graph ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") is not met.

#### 2.6.2. Restricting risk-sharing to maintain nonnegativity

By adding the restriction that agents 11 and 33 cannot exchange risk, we
can eliminate the negative entry from the previous example. We have

|  |  |  |
| --- | --- | --- |
|  | 𝝁=[1414]𝚺=𝑰 123𝑨∗=[1838538020381338538020383338],\boldsymbol{\mu}=\begin{bmatrix}\frac{1}{4}\\ 1\\ 4\end{bmatrix}\quad\boldsymbol{\Sigma}=\boldsymbol{I}\quad\raisebox{-0.45pt}{ \hbox to56.86pt{\vbox to56.86pt{\pgfpicture\makeatletter\hbox{\quad\lower-28.43068pt\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\pgfsys@setlinewidth{\the\pgflinewidth}\pgfsys@invoke{ }\nullfont\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }{{}} \par{{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{28.23068pt}{21.33957pt}\pgfsys@curveto{28.23068pt}{25.14546pt}{25.14546pt}{28.23068pt}{21.33957pt}{28.23068pt}\pgfsys@curveto{17.53368pt}{28.23068pt}{14.44846pt}{25.14546pt}{14.44846pt}{21.33957pt}\pgfsys@curveto{14.44846pt}{17.53368pt}{17.53368pt}{14.44846pt}{21.33957pt}{14.44846pt}\pgfsys@curveto{25.14546pt}{14.44846pt}{28.23068pt}{17.53368pt}{28.23068pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{21.33957pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{18.83957pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{1}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{-21.33957pt}\pgfsys@curveto{49.57025pt}{-17.53368pt}{46.48503pt}{-14.44846pt}{42.67914pt}{-14.44846pt}\pgfsys@curveto{38.87325pt}{-14.44846pt}{35.78802pt}{-17.53368pt}{35.78802pt}{-21.33957pt}\pgfsys@curveto{35.78802pt}{-25.14546pt}{38.87325pt}{-28.23068pt}{42.67914pt}{-28.23068pt}\pgfsys@curveto{46.48503pt}{-28.23068pt}{49.57025pt}{-25.14546pt}{49.57025pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{2}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{-21.33957pt}\pgfsys@curveto{6.89111pt}{-17.53368pt}{3.8059pt}{-14.44846pt}{0.0pt}{-14.44846pt}\pgfsys@curveto{-3.8059pt}{-14.44846pt}{-6.89111pt}{-17.53368pt}{-6.89111pt}{-21.33957pt}\pgfsys@curveto{-6.89111pt}{-25.14546pt}{-3.8059pt}{-28.23068pt}{0.0pt}{-28.23068pt}\pgfsys@curveto{3.8059pt}{-28.23068pt}{6.89111pt}{-25.14546pt}{6.89111pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{3}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{24.51064pt}{14.99706pt}\pgfsys@lineto{39.5077pt}{-14.99706pt}\pgfsys@moveto{35.58788pt}{-21.33948pt}\pgfsys@lineto{7.09108pt}{-21.33948pt}\pgfsys@stroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope{}{}{}\hss}\pgfsys@discardpath\pgfsys@invoke{ }\pgfsys@endscope\hss}}\endpgfpicture}}}\quad\boldsymbol{A}\_{\*}=\begin{bmatrix}\frac{18}{38}&\frac{5}{38}&0\\[2.0pt] \frac{20}{38}&\frac{13}{38}&\frac{5}{38}\\[2.0pt] 0&\frac{20}{38}&\frac{33}{38}\end{bmatrix}, |  |

and 12​tr⁡(𝑨∗​𝚺​𝑨∗⊤)=1619≈0.842\frac{1}{2}\operatorname{tr}(\boldsymbol{A}\_{\*}\boldsymbol{\Sigma}\boldsymbol{A}\_{\*}^{\top})=\frac{16}{19}\approx 0.842. Note that since we have restricted the choices of 𝑨∗\boldsymbol{A}\_{\*}, the objective function
12​tr⁡(𝑨∗​𝚺​𝑨∗⊤)\frac{1}{2}\operatorname{tr}(\boldsymbol{A}\_{\*}\boldsymbol{\Sigma}\boldsymbol{A}\_{\*}^{\top})
has slightly increased, but now we maintain nonnegativity.

#### 2.6.3. Sharing risk equally among friends to maintain nonnegativity

Here, we show a different way to achieve nonnegativity
that does not require altering the network structure as in §[2.6.2](https://arxiv.org/html/2602.05155v1#S2.SS6.SSS2 "2.6.2. Restricting risk-sharing to maintain nonnegativity ‣ 2.6. Examples where optimal matrices have negative entries ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"). Instead, we require friends take an equal share of risk (as in Definition [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmdefinition2 "Definition 2.2 (Friends take an equal share of risk). ‣ 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")).
Here, 𝝁,\boldsymbol{\mu}, 𝚺,\boldsymbol{\Sigma}, and the network structure are the same as in §[2.6.1](https://arxiv.org/html/2602.05155v1#S2.SS6.SSS1 "2.6.1. Agents with losses with means at different scales ‣ 2.6. Examples where optimal matrices have negative entries ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), and use Theorem [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem2 "Theorem 2.2 (Friends take an equal share of risk). ‣ 2.3. Friends take equal shares of risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") to compute the optimal risk-sharing matrix where friends take an equal share of risk. For this example, we have

|  |  |  |
| --- | --- | --- |
|  | 𝝁=[1414]𝚺=𝑰 123​𝑨^=[7394391391639313913916394393739]c^=439,\boldsymbol{\mu}=\begin{bmatrix}\frac{1}{4}\\ 1\\ 4\end{bmatrix}\quad\boldsymbol{\Sigma}=\boldsymbol{I}\quad\raisebox{-0.45pt}{ \hbox to56.86pt{\vbox to56.86pt{\pgfpicture\makeatletter\hbox{\quad\lower-28.43068pt\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\pgfsys@setlinewidth{\the\pgflinewidth}\pgfsys@invoke{ }\nullfont\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }{{}} \par{{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{28.23068pt}{21.33957pt}\pgfsys@curveto{28.23068pt}{25.14546pt}{25.14546pt}{28.23068pt}{21.33957pt}{28.23068pt}\pgfsys@curveto{17.53368pt}{28.23068pt}{14.44846pt}{25.14546pt}{14.44846pt}{21.33957pt}\pgfsys@curveto{14.44846pt}{17.53368pt}{17.53368pt}{14.44846pt}{21.33957pt}{14.44846pt}\pgfsys@curveto{25.14546pt}{14.44846pt}{28.23068pt}{17.53368pt}{28.23068pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{21.33957pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{18.83957pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{1}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{-21.33957pt}\pgfsys@curveto{49.57025pt}{-17.53368pt}{46.48503pt}{-14.44846pt}{42.67914pt}{-14.44846pt}\pgfsys@curveto{38.87325pt}{-14.44846pt}{35.78802pt}{-17.53368pt}{35.78802pt}{-21.33957pt}\pgfsys@curveto{35.78802pt}{-25.14546pt}{38.87325pt}{-28.23068pt}{42.67914pt}{-28.23068pt}\pgfsys@curveto{46.48503pt}{-28.23068pt}{49.57025pt}{-25.14546pt}{49.57025pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{2}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{-21.33957pt}\pgfsys@curveto{6.89111pt}{-17.53368pt}{3.8059pt}{-14.44846pt}{0.0pt}{-14.44846pt}\pgfsys@curveto{-3.8059pt}{-14.44846pt}{-6.89111pt}{-17.53368pt}{-6.89111pt}{-21.33957pt}\pgfsys@curveto{-6.89111pt}{-25.14546pt}{-3.8059pt}{-28.23068pt}{0.0pt}{-28.23068pt}\pgfsys@curveto{3.8059pt}{-28.23068pt}{6.89111pt}{-25.14546pt}{6.89111pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{3}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{24.51064pt}{14.99706pt}\pgfsys@lineto{39.5077pt}{-14.99706pt}\pgfsys@moveto{35.58788pt}{-21.33948pt}\pgfsys@lineto{7.09108pt}{-21.33948pt}\pgfsys@moveto{3.17116pt}{-14.99706pt}\pgfsys@lineto{18.16832pt}{14.99706pt}\pgfsys@stroke\pgfsys@invoke{ } \par\par \pgfsys@invoke{ }\pgfsys@endscope{}{}{}\hss}\pgfsys@discardpath\pgfsys@invoke{ }\pgfsys@endscope\hss}}\endpgfpicture}}}\boldsymbol{\hat{A}}=\begin{bmatrix}\frac{7}{39}&\frac{4}{39}&\frac{1}{39}\\[2.0pt] \frac{16}{39}&\frac{31}{39}&\frac{1}{39}\\[2.0pt] \frac{16}{39}&\frac{4}{39}&\frac{37}{39}\end{bmatrix}\quad\hat{c}=\frac{4}{39}, |  |

and 12​tr⁡(𝑨^​𝚺​𝑨^⊤)=2526≈0.962.\frac{1}{2}\operatorname{tr}(\boldsymbol{\hat{A}}\boldsymbol{\Sigma}\boldsymbol{\hat{A}}^{\top})=\frac{25}{26}\approx 0.962.
Note that although this network fails to meet the nonnegativity conditions as stated in Lemma [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmlemma1 "Lemma 2.1. ‣ 2.5.1. Nonnegativity Conditions for 𝑨_∗ for the case of the complete graph ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), it satisfies those in Lemma [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmlemma2 "Lemma 2.2. ‣ 2.5.2. Nonnegativity conditions for 𝑨̂ ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance").

While the condition that friends take an equal share of risk prevents a negative entry in this example, next we demonstrate two cases where friends take an equal share of risk, but the conditions of Lemma [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmlemma2 "Lemma 2.2. ‣ 2.5.2. Nonnegativity conditions for 𝑨̂ ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") fail, which results in negative entries in 𝑨^.\boldsymbol{\hat{A}}.

#### 2.6.4. Negative off-diagonal entries

Here we show an example where c^\hat{c} is negative, and the condition of Corollary [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmcorollary2 "Corollary 2.2. ‣ 2.5.2. Nonnegativity conditions for 𝑨̂ ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") is violated, which results in a negative entry for 𝑨^\boldsymbol{\hat{A}}. Here, we have

|  |  |  |
| --- | --- | --- |
|  | 𝝁=[15]𝚺=[133192]c^=−3518𝑨^=[5318−718−35182518],\boldsymbol{\mu}=\begin{bmatrix}1\\ 5\end{bmatrix}\quad\boldsymbol{\Sigma}=\begin{bmatrix}1&3\\[2.0pt] 3&\frac{19}{2}\end{bmatrix}\quad\hat{c}=-\frac{35}{18}\quad\boldsymbol{\hat{A}}=\begin{bmatrix}\frac{53}{18}&-\frac{7}{18}\\[2.0pt] -\frac{35}{18}&\frac{25}{18}\end{bmatrix}, |  |

and 12​tr⁡(𝑨^​𝚺​𝑨^⊤)=32972≈4.57.\frac{1}{2}\operatorname{tr}(\boldsymbol{\hat{A}}\boldsymbol{\Sigma}\boldsymbol{\hat{A}}^{\top})=\frac{329}{72}\approx 4.57.
Indeed, referring to Corollary [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmcorollary2 "Corollary 2.2. ‣ 2.5.2. Nonnegativity conditions for 𝑨̂ ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"),

|  |  |  |
| --- | --- | --- |
|  | Cov⁡(X1,X2)=3>2912=σ12​μ2+σ22​μ1μ1+μ2.\operatorname{Cov}(X\_{1},X\_{2})=3>\frac{29}{12}=\frac{\sigma\_{1}^{2}\mu\_{2}+\sigma\_{2}^{2}\mu\_{1}}{\mu\_{1}+\mu\_{2}}. |  |

Since the covariance value exceeds the bounds for a nonnegative c^,\hat{c}, the off-diagonal entries are negative (see the Proof of Lemma [2.2](https://arxiv.org/html/2602.05155v1#S2.Thmlemma2 "Lemma 2.2. ‣ 2.5.2. Nonnegativity conditions for 𝑨̂ ‣ 2.5. Nonnegativity Conditions ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")).

#### 2.6.5. Negative diagonal entry

Here we show an example where c^>μ1d1,\hat{c}>\frac{\mu\_{1}}{d\_{1}}, resulting in a negative diagonal entry.
We have:

|  |  |  |
| --- | --- | --- |
|  | 𝝁=𝟏𝚺=diag⁡(1,8,8,8) 1234​c^=920𝑨^=[−720920920920920112000920011200920001120],\boldsymbol{\mu}=\boldsymbol{1}\quad\boldsymbol{\Sigma}=\operatorname{diag}(1,8,8,8)\quad\raisebox{-0.45pt}{ \hbox to56.86pt{\vbox to56.86pt{\pgfpicture\makeatletter\hbox{\quad\lower-28.43068pt\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\pgfsys@setlinewidth{\the\pgflinewidth}\pgfsys@invoke{ }\nullfont\hbox to0.0pt{\pgfsys@beginscope\pgfsys@invoke{ }{{}} \par{{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{21.33957pt}\pgfsys@curveto{6.89111pt}{25.14546pt}{3.8059pt}{28.23068pt}{0.0pt}{28.23068pt}\pgfsys@curveto{-3.8059pt}{28.23068pt}{-6.89111pt}{25.14546pt}{-6.89111pt}{21.33957pt}\pgfsys@curveto{-6.89111pt}{17.53368pt}{-3.8059pt}{14.44846pt}{0.0pt}{14.44846pt}\pgfsys@curveto{3.8059pt}{14.44846pt}{6.89111pt}{17.53368pt}{6.89111pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{1}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{21.33957pt}\pgfsys@curveto{49.57025pt}{25.14546pt}{46.48503pt}{28.23068pt}{42.67914pt}{28.23068pt}\pgfsys@curveto{38.87325pt}{28.23068pt}{35.78802pt}{25.14546pt}{35.78802pt}{21.33957pt}\pgfsys@curveto{35.78802pt}{17.53368pt}{38.87325pt}{14.44846pt}{42.67914pt}{14.44846pt}\pgfsys@curveto{46.48503pt}{14.44846pt}{49.57025pt}{17.53368pt}{49.57025pt}{21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{18.11736pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{2}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{49.57025pt}{-21.33957pt}\pgfsys@curveto{49.57025pt}{-17.53368pt}{46.48503pt}{-14.44846pt}{42.67914pt}{-14.44846pt}\pgfsys@curveto{38.87325pt}{-14.44846pt}{35.78802pt}{-17.53368pt}{35.78802pt}{-21.33957pt}\pgfsys@curveto{35.78802pt}{-25.14546pt}{38.87325pt}{-28.23068pt}{42.67914pt}{-28.23068pt}\pgfsys@curveto{46.48503pt}{-28.23068pt}{49.57025pt}{-25.14546pt}{49.57025pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{42.67914pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{40.17914pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{3}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} {{}}\hbox{\hbox{{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{{}{{{}}}{{}}{}{}{}{}{}{}{}{}{}{\pgfsys@beginscope\pgfsys@invoke{ }\definecolor[named]{pgffillcolor}{rgb}{1,1,1}\pgfsys@color@gray@fill{1}\pgfsys@invoke{ }{}\pgfsys@moveto{6.89111pt}{-21.33957pt}\pgfsys@curveto{6.89111pt}{-17.53368pt}{3.8059pt}{-14.44846pt}{0.0pt}{-14.44846pt}\pgfsys@curveto{-3.8059pt}{-14.44846pt}{-6.89111pt}{-17.53368pt}{-6.89111pt}{-21.33957pt}\pgfsys@curveto{-6.89111pt}{-25.14546pt}{-3.8059pt}{-28.23068pt}{0.0pt}{-28.23068pt}\pgfsys@curveto{3.8059pt}{-28.23068pt}{6.89111pt}{-25.14546pt}{6.89111pt}{-21.33957pt}\pgfsys@closepath\pgfsys@moveto{0.0pt}{-21.33957pt}\pgfsys@fillstroke\pgfsys@invoke{ } \pgfsys@invoke{ }\pgfsys@endscope}{{{{}}\pgfsys@beginscope\pgfsys@invoke{ }\pgfsys@transformcm{1.0}{0.0}{0.0}{1.0}{-2.5pt}{-24.56178pt}\pgfsys@invoke{ }\hbox{{\definecolor{pgfstrokecolor}{rgb}{0,0,0}\pgfsys@color@rgb@stroke{0}{0}{0}\pgfsys@invoke{ }\pgfsys@color@rgb@fill{0}{0}{0}\pgfsys@invoke{ }\hbox{{4}} }}\pgfsys@invoke{ }\pgfsys@endscope}}} \pgfsys@invoke{ }\pgfsys@endscope}}} \par{{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{7.09108pt}{21.33948pt}\pgfsys@lineto{35.58788pt}{21.33948pt}\pgfsys@stroke\pgfsys@invoke{ } {{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{37.66481pt}{-16.32532pt}\pgfsys@lineto{5.01414pt}{16.32532pt}\pgfsys@stroke\pgfsys@invoke{ } {{}}{}{{}} {{{{{}}{}{}{}{}{{}}}}}{}{{{{{}}{}{}{}{}{{}}}}}{{}}{}{}{}{}\pgfsys@moveto{0.0pt}{14.2484pt}\pgfsys@lineto{0.0pt}{-14.2484pt}\pgfsys@stroke\pgfsys@invoke{ } \par \pgfsys@invoke{ }\pgfsys@endscope{}{}{}\hss}\pgfsys@discardpath\pgfsys@invoke{ }\pgfsys@endscope\hss}}\endpgfpicture}}}\hat{c}=\frac{9}{20}\quad\boldsymbol{\hat{A}}=\begin{bmatrix}-\frac{7}{20}&\frac{9}{20}&\frac{9}{20}&\frac{9}{20}\\[2.0pt] \frac{9}{20}&\frac{11}{20}&0&0\\[2.0pt] \frac{9}{20}&0&\frac{11}{20}&0\\[2.0pt] \frac{9}{20}&0&0&\frac{11}{20}\end{bmatrix}, |  |

and 12​tr⁡(𝑨^​𝚺​𝑨^⊤)=25740=6.425\frac{1}{2}\operatorname{tr}(\boldsymbol{\hat{A}}\boldsymbol{\Sigma}\boldsymbol{\hat{A}}^{\top})=\frac{257}{40}=6.425.
Indeed, when i=1i=1

|  |  |  |
| --- | --- | --- |
|  | μidi=13<c^=920\frac{\mu\_{i}}{d\_{i}}=\frac{1}{3}<\hat{c}=\frac{9}{20} |  |

so 𝑨^\boldsymbol{\hat{A}} has a negative diagonal entry.

### 2.7. Barbell network example

Here, we illustrate how organizing agents in a network structure where agents are connected if they have similar expected losses can avoid negative entries in the optimal risk-sharing matrix. Suppose that there are 66 agents whose random losses have mean vector and covariance matrix

|  |  |  |
| --- | --- | --- |
|  | 𝝁=[114166464]⊤and𝚺=𝑰,\boldsymbol{\mu}=\begin{bmatrix}1&1&4&16&64&64\end{bmatrix}^{\top}\quad\text{and}\quad\boldsymbol{\Sigma}=\boldsymbol{I}, |  |

respectively. First, we assume all agents are allowed to share risk in a fully-connected network, and we use Theorem [1.1](https://arxiv.org/html/2602.05155v1#S1.Thmtheorem1 "Theorem 1.1 (Feng, Liu, Taylor [22]). ‣ 1.3. Prior work ‣ 1. Introduction ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") to compute the optimal risk-sharing matrix 𝑨∗\boldsymbol{A}\_{\*}, see Figure [2](https://arxiv.org/html/2602.05155v1#S2.F2 "Figure 2 ‣ 2.7. Barbell network example ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") (left).

![Refer to caption](x1.png)

![Refer to caption](x2.png)

Figure 2. A heat map visualization of the optimal 𝑨∗\boldsymbol{A}\_{\*} for a fully-connected network (left), and 𝑨∗\boldsymbol{A}\_{\*} for the barbell network (right).

Observe that negative entries arise in the matrix locations corresponding to the risk exchange between the agents
with mean 11 and mean 6464 losses. Next, we restrict risk-sharing to the following barbell network

|  |  |  |
| --- | --- | --- |
|  | 213654 |  |

and use Theorem [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem1 "Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") to compute the optimal risk-sharing matrix 𝑨∗\boldsymbol{A}\_{\*}, where only friends in the barbell network share risk, see Figure [2](https://arxiv.org/html/2602.05155v1#S2.F2 "Figure 2 ‣ 2.7. Barbell network example ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") (right).
In this barbell network, agents are connected if their expected losses are within a factor of four of each other, which, in this case, eliminates the negative entries.
This example motivates further study both of nonnegativity conditions for network-based risk-sharing as well as processes for constructing risk-sharing networks based on the distribution of agents’ losses, see §[4](https://arxiv.org/html/2602.05155v1#S4 "4. Summary and Discussion ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") for further discussion.

## 3. Proof of main result

This section is organized as follows. First, in §[3.1](https://arxiv.org/html/2602.05155v1#S3.SS1 "3.1. Notation ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"),
we introduce notation. Second, in §[3.2](https://arxiv.org/html/2602.05155v1#S3.SS2 "3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), we prove Theorem [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem1 "Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance").

### 3.1. Notation

We introduce some tensor algebra notation used in the proofs below. The tensor product 𝑨⊗𝑩\boldsymbol{A}\otimes\boldsymbol{B} of two matrices 𝑨\boldsymbol{A} and 𝑩\boldsymbol{B} of respective sizes m×nm\times n and p×qp\times q is the m​p×n​qmp\times nq matrix

|  |  |  |
| --- | --- | --- |
|  | 𝑨⊗𝑩=[a11​𝑩…a1​n​𝑩⋮⋱⋮am​1​𝑩…am​n​𝑩].\boldsymbol{A}\otimes\boldsymbol{B}=\begin{bmatrix}a\_{11}\boldsymbol{B}&\dots&a\_{1n}\boldsymbol{B}\\ \vdots&\ddots&\vdots\\ a\_{m1}\boldsymbol{B}&\dots&a\_{mn}\boldsymbol{B}\end{bmatrix}. |  |

Let 𝑪\boldsymbol{C} and 𝑫\boldsymbol{D} be matrices of dimensions m×nm\times n and q×nq\times n, respectively. The (column) concatenation 𝑪⊕𝑫\boldsymbol{C}\oplus\boldsymbol{D} is the (m+q)×n(m+q)\times n matrix

|  |  |  |
| --- | --- | --- |
|  | 𝑪⊕𝑫=[𝑪𝑫].\boldsymbol{C}\oplus\boldsymbol{D}=\begin{bmatrix}\boldsymbol{C}\\ \boldsymbol{D}\end{bmatrix}. |  |

Let 𝑬=(ei​j)\boldsymbol{E}=(e\_{ij}) be an m×nm\times n matrix. The (column) vectorization of 𝑬,\boldsymbol{E}, denoted vec​(𝑬),\text{vec}(\boldsymbol{E}), is the m​nmn-dimensional column vector

|  |  |  |
| --- | --- | --- |
|  | vec​(𝑬)=[e11e21⋯​em​1e12…em​2…e1​n…em​n]⊤.\mathrm{vec}(\boldsymbol{E})=\begin{bmatrix}e\_{11}&e\_{21}&\cdots e\_{m1}&e\_{12}&\dots&e\_{m2}&\dots&e\_{1n}&\dots&e\_{mn}\end{bmatrix}^{\top}. |  |

If 𝑭=(fi​j)\boldsymbol{F}=(f\_{ij}) and 𝑮=(gi​j)\boldsymbol{G}=(g\_{ij}) are m×nm\times n matrices, then 𝑭⊙𝑮\boldsymbol{F}\odot\boldsymbol{G} denotes the entrywise product those (i,j)(i,j)-th entry is

|  |  |  |
| --- | --- | --- |
|  | (𝑭⊙𝑮)i​j=fi​j​gi​j.(\boldsymbol{F}\odot\boldsymbol{G})\_{ij}=f\_{ij}g\_{ij}. |  |

### 3.2. Proof of Theorem [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem1 "Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")

The proof of Theorem [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem1 "Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") is divided into three steps. First, in Step [3.1](https://arxiv.org/html/2602.05155v1#S3.Thmstep1 "Step 3.1. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), we transform the optimization problem ([4](https://arxiv.org/html/2602.05155v1#S2.E4 "In 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) into a quadratic program that only has equality constraints. Second, in Step [3.2](https://arxiv.org/html/2602.05155v1#S3.Thmstep2 "Step 3.2. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), we justify that this quadratic program has a unique solution determined by the KKT conditions. Third, in Step [3.3](https://arxiv.org/html/2602.05155v1#S3.Thmstep3 "Step 3.3. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), we rewrite the KKT conditions for the transformed problem in the notation of the original optimization problem.

Recall that 𝑿\boldsymbol{X} is the nonnegative nn-dimensional random vector with mean 𝝁\boldsymbol{\mu} and covariance matrix 𝚺\boldsymbol{\Sigma}, and that G=(V,E)G=(V,E) is an undirected graph whose vertices V={1,…,n}V=\{1,\ldots,n\} correspond to agents. Let 𝑾\boldsymbol{W} denote the adjacency matrix of GG. Set

|  |  |  |
| --- | --- | --- |
|  | 𝒁=𝟏𝟏⊤−𝑾−𝑰,\boldsymbol{Z}=\boldsymbol{1}\boldsymbol{1}^{\top}-\boldsymbol{W}-\boldsymbol{I}, |  |

to be an indicator for the absence of an edge. Then, the optimization problem ([4](https://arxiv.org/html/2602.05155v1#S2.E4 "In 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
| (15) |  | {minimize12​tr⁡(𝑨​𝚺​𝑨⊤)subject to𝑨​𝝁=𝝁,𝟏⊤​𝑨=𝟏⊤,𝑨⊙𝒁=𝟎,\begin{cases}\text{minimize}&\frac{1}{2}\operatorname{tr}(\boldsymbol{A}\boldsymbol{\Sigma}\boldsymbol{A}^{\top})\\ \text{subject to}&\boldsymbol{A}\boldsymbol{\mu}=\boldsymbol{\mu},\quad\boldsymbol{1}^{\top}\boldsymbol{A}=\boldsymbol{1}^{\top},\quad\boldsymbol{A}\odot\boldsymbol{Z}=\boldsymbol{0},\end{cases} |  |

where 𝑨⊙𝒁\boldsymbol{A}\odot\boldsymbol{Z} enforces the constraint that only friends can share risk. The following result rewrites ([15](https://arxiv.org/html/2602.05155v1#S3.E15 "In 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) as a quadratic program that only has equality constraints.

###### Step 3.1.

Set

|  |  |  |
| --- | --- | --- |
|  | 𝒙:=vec​(𝑨),𝑸:=𝚺⊗𝑰,and𝒄:=𝝁⊕𝟏n⊕𝟎m,\boldsymbol{x}:=\mathrm{vec}(\boldsymbol{A}),\qquad\boldsymbol{Q}:=\boldsymbol{\Sigma}\otimes\boldsymbol{I},\qquad\text{and}\qquad\boldsymbol{c}:=\boldsymbol{\mu}\oplus\boldsymbol{1}\_{n}\oplus\boldsymbol{0}\_{m}, |  |

where 𝟏n\boldsymbol{1}\_{n} denotes and nn-dimensional column vector of ones, and 𝟎m\boldsymbol{0}\_{m} denotes and mm-dimensional column vector of zeros.
Define 𝐁:=𝐁𝛍⊕𝐁𝟏⊕𝐁𝟎\boldsymbol{B}:=\boldsymbol{B}\_{\boldsymbol{\mu}}\oplus\boldsymbol{B}\_{\boldsymbol{1}}\oplus\boldsymbol{B}\_{\boldsymbol{0}}, where

|  |  |  |
| --- | --- | --- |
|  | 𝑩𝝁:=(⨁i=1nμi​𝑰)⊤,𝑩𝟏:=⨁i=1n(𝟎(i−1)​n⊕𝟏n⊕𝟎n2−i​n)⊤,𝑩𝟎:=⨁i=1m𝒆ji⊤,\boldsymbol{B}\_{\boldsymbol{\mu}}:=\left(\bigoplus\_{i=1}^{n}\mu\_{i}\boldsymbol{I}\right)^{\top},\quad\boldsymbol{B}\_{\boldsymbol{1}}:=\bigoplus\_{i=1}^{n}\left(\boldsymbol{0}\_{(i-1)n}\oplus\boldsymbol{1}\_{n}\oplus\boldsymbol{0}\_{n^{2}-in}\right)^{\top},\quad\boldsymbol{B}\_{\boldsymbol{0}}:=\bigoplus\_{i=1}^{m}\boldsymbol{e}\_{j\_{i}}^{\top}, |  |

where 𝐞i\boldsymbol{e}\_{i} is the ii-th standard basis vector of dimension n2n^{2}, and
j1,…,jmj\_{1},\ldots,j\_{m} are the indices of the nonzero entries of vec​(𝐙)\mathrm{vec}(\boldsymbol{Z}).
Then, the optimization problem

|  |  |  |  |
| --- | --- | --- | --- |
| (16) |  | {minimize12​𝒙⊤​𝑸​𝒙subject to𝑩​𝒙=𝒄\begin{cases}\text{minimize}&\frac{1}{2}\boldsymbol{x}^{\top}\boldsymbol{Qx}\\ \text{subject to}&\boldsymbol{Bx}=\boldsymbol{c}\end{cases} |  |

is equivalent to ([15](https://arxiv.org/html/2602.05155v1#S3.E15 "In 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) in the sense that if 𝐱∗=vec​(𝐀∗)\boldsymbol{x}\_{\*}=\mathrm{vec}(\boldsymbol{A}\_{\*}), then 𝐱∗\boldsymbol{x}\_{\*} is in the optimal set of ([16](https://arxiv.org/html/2602.05155v1#S3.E16 "In Step 3.1. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) if and only if 𝐀∗\boldsymbol{A}\_{\*} is in the optimal set of ([15](https://arxiv.org/html/2602.05155v1#S3.E15 "In 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")).

###### Proof of Step [3.1](https://arxiv.org/html/2602.05155v1#S3.Thmstep1 "Step 3.1. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance").

First, we show that
𝒙⊤​𝑸​𝒙=tr⁡(𝑨​𝚺​𝑨).\boldsymbol{x}^{\top}\boldsymbol{Q}\boldsymbol{x}=\operatorname{tr}(\boldsymbol{A}\boldsymbol{\Sigma}\boldsymbol{A}).
By the definition of 𝒙\boldsymbol{x} and 𝑸\boldsymbol{Q}, we have

|  |  |  |
| --- | --- | --- |
|  | 𝒙⊤𝑸𝒙=∑k1,k2=1n2vec(𝑨)k1(𝚺⊗𝑰)k1​k2vec(𝑨)k2.\boldsymbol{x}^{\top}\boldsymbol{Q}\boldsymbol{x}=\sum\_{k\_{1},k\_{2}=1}^{n^{2}}\operatorname{vec}(\boldsymbol{A})\_{k\_{1}}(\boldsymbol{\Sigma}\otimes\boldsymbol{I})\_{k\_{1}k\_{2}}\operatorname{vec}(\boldsymbol{A})\_{k\_{2}}. |  |

By writing k1=i1+n​(j1−1)k\_{1}=i\_{1}+n(j\_{1}-1) and k2=i2+n​(j2−1)k\_{2}=i\_{2}+n(j\_{2}-1), it follows from the definition of vectorization and the tensor product that

|  |  |  |
| --- | --- | --- |
|  | ∑k1,k2=1n2vec(𝑨)k1(𝚺⊗𝑰)k1​k2vec(𝑨)k2=∑i1,j1,i2,j2=1nai1​j1σj1​j2δi1​i2ai2​j2,\sum\_{k\_{1},k\_{2}=1}^{n^{2}}\operatorname{vec}(\boldsymbol{A})\_{k\_{1}}(\boldsymbol{\Sigma}\otimes\boldsymbol{I})\_{k\_{1}k\_{2}}\operatorname{vec}(\boldsymbol{A})\_{k\_{2}}=\sum\_{i\_{1},j\_{1},i\_{2},j\_{2}=1}^{n}a\_{i\_{1}j\_{1}}\sigma\_{j\_{1}j\_{2}}\delta\_{i\_{1}i\_{2}}a\_{i\_{2}j\_{2}}, |  |

where ai​ja\_{ij}, σi​j\sigma\_{ij}, and δi​j\delta\_{ij} denote the entries 𝑨\boldsymbol{A}, 𝚺\boldsymbol{\Sigma}, and 𝑰\boldsymbol{I}, respectively. Using the fact that δi​j=1\delta\_{ij}=1 when i=ji=j and δi​j=0\delta\_{ij}=0 otherwise gives

|  |  |  |
| --- | --- | --- |
|  | ∑i1,j1,i2,j2=1nai1​j1​σj1​j2​δi1​i2​ai2​j2=∑i1,j1,j2=1nai1​j1​σj1​j2​ai1​j2=tr⁡(𝑨​𝚺​𝑨⊤),\sum\_{i\_{1},j\_{1},i\_{2},j\_{2}=1}^{n}a\_{i\_{1}j\_{1}}\sigma\_{j\_{1}j\_{2}}\delta\_{i\_{1}i\_{2}}a\_{i\_{2}j\_{2}}=\sum\_{i\_{1},j\_{1},j\_{2}=1}^{n}a\_{i\_{1}j\_{1}}\sigma\_{j\_{1}j\_{2}}a\_{i\_{1}j\_{2}}=\operatorname{tr}(\boldsymbol{A}\boldsymbol{\Sigma}\boldsymbol{A}^{\top}), |  |

where the final inequality follows from the definition of matrix multiplication and the trace.

Next, we will show the equivalence of the constraints.
Recall that

|  |  |  |
| --- | --- | --- |
|  | 𝑩:=𝑩𝝁⊕𝑩𝟏⊕𝑩𝟎and𝒄=𝝁⊕𝟏n⊕𝟎m.\boldsymbol{B}:=\boldsymbol{B}\_{\boldsymbol{\mu}}\oplus\boldsymbol{B}\_{\boldsymbol{1}}\oplus\boldsymbol{B}\_{\boldsymbol{0}}\quad\text{and}\quad\boldsymbol{c}=\boldsymbol{\mu}\oplus\boldsymbol{1}\_{n}\oplus\boldsymbol{0}\_{m}. |  |

First, we will show the constraint 𝑩𝝁​𝒙=𝝁\boldsymbol{B}\_{\boldsymbol{\mu}}\boldsymbol{x}=\boldsymbol{\mu} is equivalent to 𝑨​𝝁=𝝁\boldsymbol{A}\boldsymbol{\mu}=\boldsymbol{\mu} by showing 𝑩𝝁​𝒙=𝑨​𝝁\boldsymbol{B}\_{\boldsymbol{\mu}}\boldsymbol{x}=\boldsymbol{A}\boldsymbol{\mu}. Fix i∈{1,…,n}i\in\{1,\ldots,n\}. We have

|  |  |  |
| --- | --- | --- |
|  | (𝑩𝝁​𝒙)i=∑k1=1n2(𝑩𝝁)i,k1​xk1.(\boldsymbol{B}\_{\boldsymbol{\mu}}\boldsymbol{x})\_{i}=\sum\_{k\_{1}=1}^{n^{2}}(\boldsymbol{B}\_{\boldsymbol{\mu}})\_{i,k\_{1}}x\_{k\_{1}}. |  |

If we write k1=i1+n​(j1−1)k\_{1}=i\_{1}+n(j\_{1}-1), then by the definition of 𝑩𝝁\boldsymbol{B}\_{\boldsymbol{\mu}} we have

|  |  |  |
| --- | --- | --- |
|  | ∑k1=1n2(𝑩𝝁)i,k1​xk1=∑i1,j1=1nμi1​δi​j1​ai1​j1,\sum\_{k\_{1}=1}^{n^{2}}(\boldsymbol{B}\_{\boldsymbol{\mu}})\_{i,k\_{1}}x\_{k\_{1}}=\sum\_{i\_{1},j\_{1}=1}^{n}\mu\_{i\_{1}}\delta\_{ij\_{1}}a\_{i\_{1}j\_{1}}, |  |

where δi​j,ai​j\delta\_{ij},a\_{ij} denote the entries of 𝑰,𝑨\boldsymbol{I},\boldsymbol{A}, respectively. Using the fact that δi​j=1\delta\_{ij}=1 if i=ji=j and δi​j=0\delta\_{ij}=0 otherwise gives

|  |  |  |
| --- | --- | --- |
|  | ∑i1,j1=1nμi1​δi​j1​ai1​j1=∑i1=1nμi1​ai1​i=(𝑨​𝝁)i,\sum\_{i\_{1},j\_{1}=1}^{n}\mu\_{i\_{1}}\delta\_{ij\_{1}}a\_{i\_{1}j\_{1}}=\sum\_{i\_{1}=1}^{n}\mu\_{i\_{1}}a\_{i\_{1}i}=(\boldsymbol{A}\boldsymbol{\mu})\_{i}, |  |

which establishes the equivalence to the first constraint. Second, we show that 𝑩𝟏​𝒙=𝟏n\boldsymbol{B}\_{\boldsymbol{1}}\boldsymbol{x}=\boldsymbol{1}\_{n} is equivalent to 𝟏n⊤​𝑨=𝟏n\boldsymbol{1}\_{n}^{\top}\boldsymbol{A}=\boldsymbol{1}\_{n} by showing 𝑩𝟏​𝒙=𝑨⊤​𝟏n\boldsymbol{B}\_{\boldsymbol{1}}\boldsymbol{x}=\boldsymbol{A}^{\top}\boldsymbol{1}\_{n}. Fix an index i∈{1,…,n}i\in\{1,\ldots,n\}. We have

|  |  |  |
| --- | --- | --- |
|  | (𝑩𝟏​𝒙)i=∑k1n2(𝑩𝟏)i,k1​xk1.(\boldsymbol{B}\_{\boldsymbol{1}}\boldsymbol{x})\_{i}=\sum\_{k\_{1}}^{n^{2}}\left(\boldsymbol{B}\_{\boldsymbol{1}}\right)\_{i,k\_{1}}x\_{k\_{1}}. |  |

By writing k1=i1+n​(j1−1)k\_{1}=i\_{1}+n(j\_{1}-1) and using the definition of 𝑩𝟏\boldsymbol{B}\_{\boldsymbol{1}}, we have

|  |  |  |
| --- | --- | --- |
|  | ∑k1n2(𝑩𝟏)i,k1​xk1=∑i1,j2=1nδi​j1​ai1​j1,\sum\_{k\_{1}}^{n^{2}}\left(\boldsymbol{B}\_{\boldsymbol{1}}\right)\_{i,k\_{1}}x\_{k\_{1}}=\sum\_{i\_{1},j\_{2}=1}^{n}\delta\_{ij\_{1}}a\_{i\_{1}j\_{1}}, |  |

where δi​j=1\delta\_{ij}=1 if i=ji=j and δi​j=0\delta\_{ij}=0 otherwise, and ai​ja\_{ij} are the entries of 𝑨\boldsymbol{A}. Since

|  |  |  |
| --- | --- | --- |
|  | ∑i1,j2=1nδi​j1​ai1​j1=∑i1=1nai1​i=(𝑨⊤​𝟏)i,\sum\_{i\_{1},j\_{2}=1}^{n}\delta\_{ij\_{1}}a\_{i\_{1}j\_{1}}=\sum\_{i\_{1}=1}^{n}a\_{i\_{1}i}=(\boldsymbol{A}^{\top}\boldsymbol{1})\_{i}, |  |

the equivalence of the second constraint is established. Finally, we show that
𝑩𝟎​𝒙=𝟎m\boldsymbol{B}\_{\boldsymbol{0}}\boldsymbol{x}=\boldsymbol{0}\_{m} is equivalent to 𝑨⊙𝒁=𝟎\boldsymbol{A}\odot\boldsymbol{Z}=\boldsymbol{0}.
The entrywise product in the final constraint 𝑨⊙𝒁=𝟎\boldsymbol{A}\odot\boldsymbol{Z}=\boldsymbol{0} can be directly vectorized as

|  |  |  |
| --- | --- | --- |
|  | vec⁡(𝒁)⊙vec⁡(𝑨)=vec⁡(𝒁)⊙𝒙=vec⁡(𝟎).\operatorname{vec}(\boldsymbol{Z})\odot\operatorname{vec}(\boldsymbol{A})=\operatorname{vec}(\boldsymbol{Z})\odot\boldsymbol{x}=\operatorname{vec}(\boldsymbol{0}). |  |

Recall that j1,…,jmj\_{1},\ldots,j\_{m} are the indices of the nonzero entries of 𝒁\boldsymbol{Z}, so the
vec⁡(𝒁)⊙𝒙=vec⁡(𝟎)\operatorname{vec}(\boldsymbol{Z})\odot\boldsymbol{x}=\operatorname{vec}(\boldsymbol{0}) is equivalent to
xji=0x\_{j\_{i}}=0 for i∈{1,…,m}i\in\{1,\ldots,m\}. Since (𝑩𝟎​𝒙)i=xji(\boldsymbol{B}\_{\boldsymbol{0}}\boldsymbol{x})\_{i}=x\_{j\_{i}}, the equivalence of the final constraint is established, which completes the proof.
∎

###### Step 3.2.

In addition to the notation introduced in Step [3.1](https://arxiv.org/html/2602.05155v1#S3.Thmstep1 "Step 3.1. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), assume that 𝚺\boldsymbol{\Sigma} is positive definite. Then, the quadratic program

|  |  |  |  |
| --- | --- | --- | --- |
| (17) |  | {minimize12​𝒙⊤​𝑸​𝒙subject to𝑩​𝒙=𝒄\begin{cases}\text{minimize}&\frac{1}{2}\boldsymbol{x}^{\top}\boldsymbol{Qx}\\ \text{subject to}&\boldsymbol{Bx}=\boldsymbol{c}\end{cases} |  |

has a unique solution 𝐱∗\boldsymbol{x}\_{\*} characterized by the KKT conditions

|  |  |  |  |
| --- | --- | --- | --- |
| (18) |  | [𝑸𝑩⊤𝑩𝟎]​[𝒙∗𝝂∗]=[𝟎𝒄],\begin{bmatrix}\boldsymbol{Q}&\boldsymbol{B}^{\top}\\ \boldsymbol{B}&\boldsymbol{0}\end{bmatrix}\begin{bmatrix}\boldsymbol{x}\_{\*}\\ \boldsymbol{\nu}\_{\*}\end{bmatrix}=\begin{bmatrix}\boldsymbol{0}\\ \boldsymbol{c}\end{bmatrix}, |  |

where 𝛎∗\boldsymbol{\nu}\_{\*} are Lagrange multipliers.

###### Proof of Step [3.2](https://arxiv.org/html/2602.05155v1#S3.Thmstep2 "Step 3.2. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance").

First, we argue that this optimization has a unique solution. Since the admissible set of points that satisfy the constraints contains vec⁡(𝑰)\operatorname{vec}(\boldsymbol{I}), the optimal set is nonempty. Recall that if the objective function in a convex optimization problem is strictly convex, the optimal set contains at most one point, see [[9](https://arxiv.org/html/2602.05155v1#bib.bib9), Section 4.2].
Since 𝚺\boldsymbol{\Sigma} and 𝑰\boldsymbol{I} are both positive definite, their tensor product 𝑸=𝚺⊗𝑰\boldsymbol{Q}=\boldsymbol{\Sigma}\otimes\boldsymbol{I} is positive definite since the eigenvalues of
𝚺⊗𝑰\boldsymbol{\Sigma}\otimes\boldsymbol{I} are products of the eigenvalues of 𝚺\boldsymbol{\Sigma} and 𝑰\boldsymbol{I}. It follows that 12​𝒙⊤​𝑸​𝒙\frac{1}{2}\boldsymbol{x}^{\top}\boldsymbol{Q}\boldsymbol{x} is strictly convex, and thus ([17](https://arxiv.org/html/2602.05155v1#S3.E17 "In Step 3.2. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) has a unique solution.

Second, we justify that the KKT conditions
([18](https://arxiv.org/html/2602.05155v1#S3.E18 "In Step 3.2. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) characterize the solution. The fact that the KKT conditions for the optimization can be written as ([18](https://arxiv.org/html/2602.05155v1#S3.E18 "In Step 3.2. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) follows from [[9](https://arxiv.org/html/2602.05155v1#bib.bib9), Example 5.1]. The objective function is convex and differentiable, and the problem does not have inequality constraints. Therefore, the KKT conditions are necessary and sufficient conditions for (𝒙∗,𝝂∗)(\boldsymbol{x}\_{\*},\boldsymbol{\nu}\_{\*}) to be primal and dual optimal, with zero duality gap, see [[9](https://arxiv.org/html/2602.05155v1#bib.bib9), Page 244].
∎

Finally, to complete the proof of Theorem [2.1](https://arxiv.org/html/2602.05155v1#S2.Thmtheorem1 "Theorem 2.1 (Only friends share risk). ‣ 2.1. Only friends share risk ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), we write the KKT conditions ([18](https://arxiv.org/html/2602.05155v1#S3.E18 "In Step 3.2. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) of the transformed problem using the notation of the original optimization problem.

###### Step 3.3.

The optimization problem

|  |  |  |  |
| --- | --- | --- | --- |
| (19) |  | {minimize12​tr⁡(𝑨​𝚺​𝑨⊤)subject to𝑨​𝝁=𝝁,𝟏⊤​𝑨=𝟏⊤,𝑨⊙𝒁=𝟎,\begin{cases}\text{minimize}&\frac{1}{2}\operatorname{tr}(\boldsymbol{A}\boldsymbol{\Sigma}\boldsymbol{A}^{\top})\\ \text{subject to}&\boldsymbol{A}\boldsymbol{\mu}=\boldsymbol{\mu},\quad\boldsymbol{1}^{\top}\boldsymbol{A}=\boldsymbol{1}^{\top},\quad\boldsymbol{A}\odot\boldsymbol{Z}=\boldsymbol{0},\end{cases} |  |

has a unique solution

|  |  |  |
| --- | --- | --- |
|  | 𝑨∗=1n​𝟏𝟏⊤+(𝑰−1n​𝟏𝟏⊤)​(1a​𝝁​𝝁⊤+𝚪​(1a​𝚺−1​𝝁​𝝁⊤−𝑰))​𝚺−1,\boldsymbol{A}\_{\*}=\frac{1}{n}\boldsymbol{11}^{\top}+\left(\boldsymbol{I}-\frac{1}{n}\boldsymbol{11}^{\top}\right)\left(\frac{1}{a}\boldsymbol{\mu\mu}^{\top}+\boldsymbol{\Gamma}\left(\frac{1}{a}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu\mu}^{\top}-\boldsymbol{I}\right)\right)\boldsymbol{\Sigma}^{-1}, |  |

where a=𝛍⊤​𝚺−1​𝛍a=\boldsymbol{\mu}^{\top}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu} and 𝚪=(γi​j)∈ℝn×n\boldsymbol{\Gamma}=(\gamma\_{ij})\in\mathbb{R}^{n\times n} is defined as follows: we have γi​j=0\gamma\_{ij}=0 when i=ji=j or {i,j}∈E\{i,j\}\in E, and the other entries are determined by the linear system of equations

|  |  |  |  |
| --- | --- | --- | --- |
| (20) |  | ((𝑰−1n​𝟏𝟏⊤)​(𝚪​(1a​𝚺−1​𝝁​𝝁⊤−𝑰)+1a​𝝁​𝝁⊤)​𝚺−1+1n​𝟏𝟏⊤)i​j=0\left(\left(\boldsymbol{I}-\frac{1}{n}\boldsymbol{11}^{\top}\right)\left(\boldsymbol{\Gamma}\left(\frac{1}{a}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu\mu}^{\top}-\boldsymbol{I}\right)+\frac{1}{a}\boldsymbol{\mu\mu}^{\top}\right)\boldsymbol{\Sigma}^{-1}+\frac{1}{n}\boldsymbol{11}^{\top}\right)\_{ij}=0 |  |

for all i≠ji\not=j such that {i,j}∉E\{i,j\}\not\in E.

###### Proof of Step [3.3](https://arxiv.org/html/2602.05155v1#S3.Thmstep3 "Step 3.3. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance").

The KKT conditions ([18](https://arxiv.org/html/2602.05155v1#S3.E18 "In Step 3.2. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) from Step [3.2](https://arxiv.org/html/2602.05155v1#S3.Thmstep2 "Step 3.2. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") can be written as

|  |  |  |
| --- | --- | --- |
|  | 𝑸​𝒙∗+𝑩⊤​𝝂∗=𝟎,and𝑩​𝒙∗=𝒄.\boldsymbol{Q}\boldsymbol{x}\_{\*}+\boldsymbol{B}^{\top}\boldsymbol{\nu}\_{\*}=\boldsymbol{0},\quad\text{and}\quad\boldsymbol{B}\boldsymbol{x}\_{\*}=\boldsymbol{c}. |  |

Let 𝑨∗\boldsymbol{A}\_{\*} be the n×nn\times n matrix such that 𝒙∗=vec⁡(𝑨∗)\boldsymbol{x}\_{\*}=\operatorname{vec}(\boldsymbol{A}\_{\*}). Previously, in the Proof of Step [3.1](https://arxiv.org/html/2602.05155v1#S3.Thmstep1 "Step 3.1. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance"), we established the equivalence of the constraint 𝑩​𝒙∗=𝒄\boldsymbol{B}\boldsymbol{x}\_{\*}=\boldsymbol{c} to the three constraints:

|  |  |  |
| --- | --- | --- |
|  | 𝑨​𝝁=𝝁,𝟏⊤​𝑨=𝟏⊤,𝑨⊙𝒁=𝟎.\boldsymbol{A}\boldsymbol{\mu}=\boldsymbol{\mu},\quad\boldsymbol{1}^{\top}\boldsymbol{A}=\boldsymbol{1}^{\top},\quad\boldsymbol{A}\odot\boldsymbol{Z}=\boldsymbol{0}. |  |

Next, we rewrite the equation 𝑸​𝒙∗+𝑩⊤​𝝂∗=𝟎\boldsymbol{Q}\boldsymbol{x}\_{\*}+\boldsymbol{B}^{\top}\boldsymbol{\nu}\_{\*}=\boldsymbol{0} in terms of 𝑨\boldsymbol{A}. Next, introduce a convenient notation for the Lagrange multipliers 𝝂∗\boldsymbol{\nu}\_{\*}

|  |  |  |
| --- | --- | --- |
|  | 𝝂∗=(−𝜷)⊕(−𝝀)⊕𝜸,\boldsymbol{\nu}\_{\*}=(-\boldsymbol{\beta})\oplus(-\boldsymbol{\lambda})\oplus\boldsymbol{\gamma}, |  |

where 𝜷∈ℝn\boldsymbol{\beta}\in\mathbb{R}^{n}, 𝝀∈ℝn\boldsymbol{\lambda}\in\mathbb{R}^{n}, and 𝜸∈ℝm\boldsymbol{\gamma}\in\mathbb{R}^{m}, where mm is the number of nonzero entries of 𝒁\boldsymbol{Z}. Fix k1∈{1,…,n2}k\_{1}\in\{1,\ldots,n^{2}\}. If we write k1=i1+n​(j1−1)k\_{1}=i\_{1}+n(j\_{1}-1) for i1,j1∈{1,…,n}i\_{1},j\_{1}\in\{1,\ldots,n\}, then by the definition of 𝑸\boldsymbol{Q} and 𝑩\boldsymbol{B},

|  |  |  |
| --- | --- | --- |
|  | (𝑸​𝒙∗)k1+(𝑩⊤​𝝂∗)k1=(𝑨​𝚺−𝟏​𝝀⊤−𝜷​𝝁⊤+𝚪)i1​j1,(\boldsymbol{Q}\boldsymbol{x}\_{\*})\_{k\_{1}}+(\boldsymbol{B}^{\top}\boldsymbol{\nu}\_{\*})\_{k\_{1}}=\left(\boldsymbol{A\Sigma}-\boldsymbol{1\lambda}^{\top}-\boldsymbol{\beta\mu}^{\top}+\boldsymbol{\Gamma}\right)\_{i\_{1}j\_{1}}, |  |

where 𝚪=(γi​j)∈ℝn×n\boldsymbol{\Gamma}=(\gamma\_{ij})\in\mathbb{R}^{n\times n} is defined as follows: we have γi​j=0\gamma\_{ij}=0 when i=ji=j or {i,j}∈E\{i,j\}\in E, and the other mm entries of 𝚪\boldsymbol{\Gamma} each of which corresponds to one of the mm entries of 𝜸\boldsymbol{\gamma}.
With this notation, it follows that 𝑸​𝒙∗+𝑩⊤​𝝂∗=𝟎\boldsymbol{Q}\boldsymbol{x}\_{\*}+\boldsymbol{B}^{\top}\boldsymbol{\nu}\_{\*}=\boldsymbol{0}
is equivalent to

|  |  |  |
| --- | --- | --- |
|  | 𝑨​𝚺−𝟏​𝝀⊤−𝜷​𝝁⊤+𝚪=𝟎.\boldsymbol{A\Sigma}-\boldsymbol{1\lambda}^{\top}-\boldsymbol{\beta\mu}^{\top}+\boldsymbol{\Gamma}=\boldsymbol{0}. |  |

Solving for 𝑨\boldsymbol{A} gives

|  |  |  |  |
| --- | --- | --- | --- |
| (21) |  | 𝑨=(𝟏​𝝀⊤+𝜷​𝝁⊤−𝚪)​𝚺−1.\boldsymbol{A}=(\boldsymbol{1\lambda}^{\top}+\boldsymbol{\beta\mu}^{\top}-\boldsymbol{\Gamma})\boldsymbol{\Sigma}^{-1}. |  |

Using the constraint 𝟏⊤​𝑨=𝟏⊤\boldsymbol{1}^{\top}\boldsymbol{A}=\boldsymbol{1}^{\top} and solving for 𝝀⊤\boldsymbol{\lambda}^{\top} yields

|  |  |  |
| --- | --- | --- |
|  | 𝝀⊤=1n​(𝟏⊤​𝚺−𝟏⊤​𝜷​𝝁⊤+𝟏⊤​𝚪).\boldsymbol{\lambda}^{\top}=\frac{1}{n}(\boldsymbol{1}^{\top}\boldsymbol{\Sigma}-\boldsymbol{1}^{\top}\boldsymbol{\beta\mu}^{\top}+\boldsymbol{1}^{\top}\boldsymbol{\Gamma}). |  |

Substituting this formula for 𝝀⊤\boldsymbol{\lambda}^{\top} into ([21](https://arxiv.org/html/2602.05155v1#S3.E21 "In Proof of Step 3.3. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
| (22) |  | 𝑨=1n​𝟏𝟏⊤+(𝑰−1n​𝟏𝟏⊤)​𝜷​𝝁⊤​𝚺−1−(𝑰−1n​𝟏𝟏⊤)​𝚪​𝚺−1.\boldsymbol{A}=\frac{1}{n}\boldsymbol{11}^{\top}+\left(\boldsymbol{I}-\frac{1}{n}\boldsymbol{11}^{\top}\right)\boldsymbol{\beta\mu}^{\top}\boldsymbol{\Sigma}^{-1}-\left(\boldsymbol{I}-\frac{1}{n}\boldsymbol{11}^{\top}\right)\boldsymbol{\Gamma}\boldsymbol{\Sigma}^{-1}. |  |

Using the constraint 𝑨​𝝁=𝝁\boldsymbol{A\mu}=\boldsymbol{\mu} and solving for 𝜷\boldsymbol{\beta} gives

|  |  |  |
| --- | --- | --- |
|  | 𝜷=(𝝁+𝚪​𝚺−1​𝝁)​(𝝁⊤​𝚺−1​𝝁)−1+c​𝟏,\boldsymbol{\beta}=(\boldsymbol{\mu}+\boldsymbol{\Gamma}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu})(\boldsymbol{\mu}^{\top}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu})^{-1}+c\boldsymbol{1}, |  |

where cc is some scalar. If we define a:=𝝁⊤​𝚺−1​𝝁a:=\boldsymbol{\mu}^{\top}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}, then

|  |  |  |
| --- | --- | --- |
|  | 𝜷=1a​(𝝁+𝚪​𝚺−1​𝝁)+c​𝟏.\boldsymbol{\beta}=\frac{1}{a}(\boldsymbol{\mu}+\boldsymbol{\Gamma}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu})+c\boldsymbol{1}. |  |

Substituting this formula for 𝜷\boldsymbol{\beta} in ([22](https://arxiv.org/html/2602.05155v1#S3.E22 "In Proof of Step 3.3. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) gives

|  |  |  |  |
| --- | --- | --- | --- |
| (23) |  | 𝑨=1n​𝟏𝟏⊤+(𝑰−1n​𝟏𝟏⊤)​(1a​𝝁​𝝁⊤+𝚪​(1a​𝚺−1​𝝁​𝝁⊤−𝑰))​𝚺−1.\boldsymbol{A}=\frac{1}{n}\boldsymbol{11}^{\top}+\left(\boldsymbol{I}-\frac{1}{n}\boldsymbol{11}^{\top}\right)\left(\frac{1}{a}\boldsymbol{\mu\mu}^{\top}+\boldsymbol{\Gamma}\left(\frac{1}{a}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu\mu}^{\top}-\boldsymbol{I}\right)\right)\boldsymbol{\Sigma}^{-1}. |  |

Using the constraint 𝒁⊙𝑨=𝟎\boldsymbol{Z}\odot\boldsymbol{A}=\boldsymbol{0}, we observe that

|  |  |  |  |
| --- | --- | --- | --- |
| (24) |  | 𝒁⊙(1n​𝟏𝟏⊤+(𝑰−1n​𝟏𝟏⊤)​(1a​𝝁​𝝁⊤+𝚪​(1a​𝚺−1​𝝁​𝝁⊤−𝑰))​𝚺−1)=𝟎.\boldsymbol{Z}\odot\left(\frac{1}{n}\boldsymbol{11}^{\top}+\left(\boldsymbol{I}-\frac{1}{n}\boldsymbol{11}^{\top}\right)\left(\frac{1}{a}\boldsymbol{\mu\mu}^{\top}+\boldsymbol{\Gamma}\left(\frac{1}{a}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu\mu}^{\top}-\boldsymbol{I}\right)\right)\boldsymbol{\Sigma}^{-1}\right)=\boldsymbol{0}. |  |

Using the fact that
𝒁=𝟏𝟏⊤−𝑾−𝑰\boldsymbol{Z}=\boldsymbol{1}\boldsymbol{1}^{\top}-\boldsymbol{W}-\boldsymbol{I}
is an indicator function for the absence of an edge,
we can write out the equations ([24](https://arxiv.org/html/2602.05155v1#S3.E24 "In Proof of Step 3.3. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) explicitly as

|  |  |  |  |
| --- | --- | --- | --- |
| (25) |  | ((𝑰−1n​𝟏𝟏⊤)​(𝚪​(1a​𝚺−1​𝝁​𝝁⊤−𝑰)+1a​𝝁​𝝁⊤)​𝚺−1+1n​𝟏𝟏⊤)i​j=0\left(\left(\boldsymbol{I}-\frac{1}{n}\boldsymbol{11}^{\top}\right)\left(\boldsymbol{\Gamma}\left(\frac{1}{a}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu\mu}^{\top}-\boldsymbol{I}\right)+\frac{1}{a}\boldsymbol{\mu\mu}^{\top}\right)\boldsymbol{\Sigma}^{-1}+\frac{1}{n}\boldsymbol{11}^{\top}\right)\_{ij}=0 |  |

for all i≠ji\not=j such that {i,j}∉E\{i,j\}\not\in E.

∎

###### Remark 3.1 (Computation of 𝚪\boldsymbol{\Gamma}).

The linear system of equations ([25](https://arxiv.org/html/2602.05155v1#S3.E25 "In Proof of Step 3.3. ‣ 3.2. Proof of Theorem 2.1 ‣ 3. Proof of main result ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance")) that determines the nonzero entries of 𝚪∈ℝn×n\boldsymbol{\Gamma}\in\mathbb{R}^{n\times n} consists of selected equations of a linear system of the form 𝑬​𝚪​𝑭=𝑮\boldsymbol{E}\boldsymbol{\Gamma}\boldsymbol{F}=\boldsymbol{G} where 𝑬,𝑭,𝑮∈ℝn×n\boldsymbol{E},\boldsymbol{F},\boldsymbol{G}\in\mathbb{R}^{n\times n} are given matrices.
We can write this linear system in matrix-vector form using tensor algebra notation. In particular, we have

|  |  |  |
| --- | --- | --- |
|  | 𝑬​𝚪​𝑭=𝑮⇔(𝑭⊤⊗𝑬)​vec⁡(𝚪)=vec⁡(𝑮).\boldsymbol{E}\boldsymbol{\Gamma}\boldsymbol{F}=\boldsymbol{G}\quad\iff\quad(\boldsymbol{F}^{\top}\otimes\boldsymbol{E})\operatorname{vec}(\boldsymbol{\Gamma})=\operatorname{vec}(\boldsymbol{G}). |  |

By selecting an m×mm\times m principal submatrix of 𝑭⊤⊗𝑬\boldsymbol{F}^{\top}\otimes\boldsymbol{E} and the corresponding mm elements of vec⁡(𝑮)\operatorname{vec}(\boldsymbol{G}), where mm is the number of i≠ji\not=j such that {i,j}∉E\{i,j\}\not\in E, one arrives at a linear system in standard matrix vector form, which can be directly solved using standard methods. Finally, we note that this direct approach to computing 𝚪\boldsymbol{\Gamma} involves constructing an n2×n2n^{2}\times n^{2} matrix 𝑭⊤⊗𝑬\boldsymbol{F}^{\top}\otimes\boldsymbol{E}, which may be prohibitive for large nn. In such cases, the linear system could be solved iteratively instead.

## 4. Summary and Discussion

In this paper, we consider optimal linear actuarially fair P2P risk-sharing on any connected graph without additional restrictions. When a complete graph is considered, our results agree with prior results of Feng, Liu, and Taylor [[22](https://arxiv.org/html/2602.05155v1#bib.bib22)]. However, the results presented in this paper also apply to arbitrary connected graphs, which enables the restriction that only friends can share risk.

We further examine risk-sharing rules with the additional condition that friends of agent ii take an equal fractional share of the risk of agent ii. In this case, the optimal linear risk-sharing rule is related to the graph Laplacian 𝑳\boldsymbol{L}.

We also identify necessary and sufficient conditions for nonnegativity of the entries of the optimal linear risk-sharing matrix for certain cases. For complete networks with no additional restrictions, the mean vector 𝝁\boldsymbol{\mu} and covariance matrix 𝚺\boldsymbol{\Sigma} determine nonnegativity, while for any rules that enforce the friends share equal risk assumption, conditions are in terms of the degree of each node in the network, the mean vector, and the covariance matrix.

The theoretical results are illustrated through several examples that demonstrate the versatility and utility of these new approaches to linear P2P risk-sharing rules. Costs and benefits, as measured by the sum of variance after risk-sharing, are discussed. Examples illustrate that, although negative entries may appear in the optimal linear rule over complete graphs, restricting the optimization by disconnecting nodes associated with negative entries can result in exclusively nonnegative entries. The provided examples and analysis establish several options for risk-sharing networks depending on which properties, such as nonnegativity, equal risk shared between friends, or the lowest possible overall variance after risk-sharing, would be most beneficial to the specific risk pool.

Our results motivate several questions for further study. First, it may be interesting to consider the connection between network structure and the willingness of agents to join a P2P insurance network. For example, participants may be more willing to join a risk-sharing network if they only share risk with other agents whose losses have expectation and variance within a certain range of their own. The barbell example in Section [2.7](https://arxiv.org/html/2602.05155v1#S2.SS7 "2.7. Barbell network example ‣ 2. Main results ‣ Optimal Risk-Sharing Rules in Network-based Decentralized Insurance") demonstrates a network constructed based on mitigating risk-sharing between agents with extreme differences in expectation, although different assumptions or guidelines for establishing connections in a risk-sharing network may produce different results or require new assumptions to preserve willingness to join. One consideration of interest is preferential attachment, where economic parameters of the agents outside of expectation alone affect how a network is formed. It may also be of interest to extend our network risk-sharing models to consider multiple periods or continuous time rather than the static models examined in this paper.

## References

* [1]

  Samal Abdikerimova, Tim J Boonen, and Runhuan Feng.
  Multiperiod peer-to-peer risk sharing.
  Journal of Risk and Insurance, 91(4):943–982, 2024.
* [2]

  Samal Abdikerimova and Runhuan Feng.
  Peer-to-peer multi-risk insurance and mutual aid.
  European Journal of Operational Research, 299(2):735–749, 2022.
* [3]

  Andreas Bollmann and Shaun S Wang.
  International catastrophe pooling for extreme weather.
  Society of Actuaries, 2019.
* [4]

  Tim J Boonen and Ka Long Chiu.
  Peer-to-peer risk-sharing schemes with heterogeneity and infinite-mean losses.
  Available at SSRN 5013193, 2025.
* [5]

  Tim J Boonen and Ziqi Zhou.
  Robust peer-to-peer risk sharing in continuous time.
  Available at SSRN 5957416, 2025.
* [6]

  Karl Borch.
  An attempt to determine the optimum amount of stop loss reinsurance.
  Transactions of the 16th International Congress of Actuaries, 2:597–610, 1960.
* [7]

  Karl Borch.
  Equilibrium in a reinsurance market.
  Econometrica, pages 424–444, 1962.
* [8]

  Karl Borch.
  General equilibrium in the economics of uncertainty.
  In Risk and Uncertainty: Proceedings of a Conference held by the International Economic Association, pages 247–264. Springer, 1968.
* [9]

  Stephen P Boyd and Lieven Vandenberghe.
  Convex optimization.
  Cambridge University Press, 2004.
* [10]

  Arthur Charpentier, Lariosse Kouakou, Matthias Löwe, Philipp Ratz, and Franck Vermet.
  Collaborative insurance sustainability and network structure.
  arXiv preprint arXiv:2107.02764, 2021.
* [11]

  Arthur Charpentier and Philipp Ratz.
  Linear risk sharing on networks.
  arXiv preprint arXiv:2509.21411, 2025.
* [12]

  Fan RK Chung.
  Spectral graph theory, volume 92.
  American Mathematical Soc., 1997.
* [13]

  Gian Paolo Clemente, Susanna Levantesi, and Gabriella Piscopo.
  Risk sharing rule and safety loading in a peer to peer cooperative insurance model.
  Decisions in Economics and Finance, pages 1–14, 2024.
* [14]

  Michel Denuit.
  Investing in your own and peers’ risks: The simple analytics of P2P insurance.
  European Actuarial Journal, 10(2):335–359, 2020.
* [15]

  Michel Denuit and Jan Dhaene.
  Convex order and comonotonic conditional mean risk sharing.
  Insurance: Mathematics and Economics, 51(2):265–270, 2012.
* [16]

  Michel Denuit, Jan Dhaene, Mario Ghossoub, and Christian Y Robert.
  Comonotonicity and pareto optimality, with application to collaborative insurance.
  Insurance: Mathematics and Economics, 120:1–16, 2025.
* [17]

  Michel Denuit, Jan Dhaene, and Christian Y Robert.
  Risk‐sharing rules and their properties, with applications to peer‐to‐peer insurance.
  Journal of Risk and Insurance, 89(3):615–667, June 2022.
* [18]

  Michel Denuit and Christian Y Robert.
  From risk sharing to pure premium for a large number of heterogeneous losses.
  Insurance: Mathematics and Economics, 96:116–126, 2021.
* [19]

  Michel Denuit and Christian Y Robert.
  Risk sharing under the dominant peer-to-peer property and casualty insurance business models.
  Risk Management and Insurance Review, 24(2):181–205, 2021.
* [20]

  Matthias A Fahrenwaldt, Stefan Weber, and Kerstin Weske.
  Pricing of cyber insurance contracts in a network model.
  ASTIN Bulletin: The Journal of the IAA, 48(3):1175–1218, 2018.
* [21]

  Runhuan Feng.
  Decentralized insurance.
  In Decentralized Insurance: Technical Foundation of Business Models, pages 119–139. Springer, 2023.
* [22]

  Runhuan Feng, Chongda Liu, and Stephen Taylor.
  Peer-to-peer risk sharing with an application to flood risk pooling.
  Annals of Operations Research, 321(1):813–842, 2023.
* [23]

  Runhuan Feng, Ming Liu, and Ning Zhang.
  A unified theory of decentralized insurance.
  Insurance: Mathematics and Economics, 119:157–178, 2024.
* [24]

  Susanna Levantesi and Gabriella Piscopo.
  Mutual peer-to-peer insurance: The allocation of risk.
  Journal of Co-operative Organization and Management, 10(1):100154, 2022.
* [25]

  Adnan Malik and Karim Ullah.
  Introduction to takaful, volume 10.
  Springer, 2019.
* [26]

  Fallou Niakh.
  A fixed point approach for computing actuarially fair pareto optimal risk-sharing rules.
  European Actuarial Journal, 15(1):297–334, 2025.
* [27]

  Jiajie Yang and Wei Wei.
  On the optimality of linear residual risk sharing.
  ASTIN Bulletin: The Journal of the IAA, pages 1–23, 2024.