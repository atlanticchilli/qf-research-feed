---
authors:
- Alexander Dimitrov
- Christoph Kühn
doc_id: arxiv:2602.15177v1
family_id: arxiv:2602.15177
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Optimal investment under capital gains taxes
url_abs: http://arxiv.org/abs/2602.15177v1
url_html: https://arxiv.org/html/2602.15177v1
venue: arXiv q-fin
version: 1
year: 2026
---


Alexander Dimitrov
Institute of Mathematics, Goethe University Frankfurt, D-60054 Frankfurt a.M., Germany, e-mail: {dimitrov, ckuehn}@math.uni-frankfurt.de
  
Christoph Kühn11footnotemark: 1

###### Abstract

We generalize classical results on the existence of optimal portfolios in discrete time frictionless market models to models with capital gains taxes.
We consider the realistic but mathematically challenging rule that losses do not trigger negative taxes but can only be offset against potential gains in the future.
Central to the analysis is a well-known phenomenon from arbitrage-free markets with proportional transaction costs that does not exist in arbitrage-free frictionless markets: an investment in specific quantities of stocks that is completely riskless but may provide an advantage over holding money in the bank account. As a result of this phenomenon, on an infinite probability space, no-arbitrage does not imply that the set of attainable terminal
wealth is closed in probability. We show closedness under the slightly stronger no unbounded non-substitutable
investment with bounded risk condition.

As a by-product, we provide a proof that in discrete time frictionless models with
short-selling constraints, no-arbitrage implies that the set of attainable terminal wealth is closed in probability—even if there are redundant stocks.

|  |
| --- |
| Keywords: utility maximization, capital gains taxes, limited use of losses |
| Mathematics Subject Classification (2020): 91G10, 91B16, 60G99, 90C25 |

## 1 Introduction

Capital gains taxes have a major impact on investors’ returns, and their influence on optimal investment decisions has been well studied
in the financial economics literature.
In an influential early contribution, Dybvig and Koo [[11](https://arxiv.org/html/2602.15177v1#bib.bib11)] analyze a multiperiod utility maximization problem under the so-called exact tax basis or specific share identification method. This corresponds to the tax legislation in many countries, especially in the U.S., and seems economically to be the most reasonable tax basis: when an investor wants to reduce a position, she
explicitly identifies which shares—purchased at which time and at which price—are being sold and thus relevant for taxation.
The model was further developed by Damman, Spatt, and Zhang [[8](https://arxiv.org/html/2602.15177v1#bib.bib8), [9](https://arxiv.org/html/2602.15177v1#bib.bib9)], among many others, using the average tax basis and including a tax-deferred account. The average tax basis simplifies tax payments by considering an average purchasing price of identical shares in the portfolio.

In the earlier financial economics literature, tax systems with the full use of losses (FUL) have been considered, that is, overall losses in a year lead to negative tax payments, so-called tax credits. More realistic is the limited use of losses (LUL), that is, losses do not trigger negative taxes but can only be offset against potential gains in the future. Optimal portfolios with LUL compared to FUL are analyzed by Ehling, Gallmeyer, Srivastava, Tompaidis, and Yang [[12](https://arxiv.org/html/2602.15177v1#bib.bib12)] and Fischer and Gallmeyer [[13](https://arxiv.org/html/2602.15177v1#bib.bib13)].
Haugh, Iyengar, and Wang [[15](https://arxiv.org/html/2602.15177v1#bib.bib15)] apply the duality method based on relaxing the adaptedness constraint of stochastic controls
to obtain dual upper bounds for the value of an utility maximization problem. The method allows to evaluate heuristic strategies in problems with a
rather large number of assets and time periods.

Moreover, several advanced continuous time portfolio optimization problems with taxes have been analyzed:
In their pioneering work, Jouini, Koehl, and Touzi [[16](https://arxiv.org/html/2602.15177v1#bib.bib16), [17](https://arxiv.org/html/2602.15177v1#bib.bib17)] derive first-order conditions for
optimal consumption plans with the first in first out (FIFO) tax basis and a quite general tax code, but only with a deterministic stock price process.
In Ben Tahar, Soner, and Touzi [[1](https://arxiv.org/html/2602.15177v1#bib.bib1), [2](https://arxiv.org/html/2602.15177v1#bib.bib2)] the continuous time Merton problem for the average tax basis, FUL, and non-zero transaction costs is analyzed. It is shown that the value function is the unique viscosity solution of the corresponding
dynamic programming equation.
Cai, Chen, and Dai [[4](https://arxiv.org/html/2602.15177v1#bib.bib4)] and
Bian, Chen, Dai, and Qian [[3](https://arxiv.org/html/2602.15177v1#bib.bib3)] consider the same problem without transaction costs. They show that the value function is the minimal viscosity solution of the corresponding dynamic programming equation and approximate it by value functions of the problem with constraint trading rates. For the original problem, the analysis is based on ε{\varepsilon}-optimal strategies.
In Seifried [[28](https://arxiv.org/html/2602.15177v1#bib.bib28)] the continuous time optimization problem is solved for the LUL, but for a tax-deferred account, that is, taxes are only paid at maturity.

Nevertheless, a comprehensive mathematical theory for market models with taxes, comparable to those for frictionless markets and for markets with proportional transaction costs, is still lacking. This paper aims to contribute to closing this gap and to relate tax models to transaction costs models. Of course, tax legislation varies from country to country, but there are two core principles: taxes are realization-based, that is, they are paid
when gains are realized by selling securities and not when they arise on paper; and there is a limited use of losses (LUL) as described above.
We consider a model that captures this, but for simplicity, we abstract from many other detailed tax regulations that would distract from the mathematical core of the problem. We work with the exact tax basis, which is a natural choice for a theoretical analysis.

In a model with the full use of losses (FUL), the after-tax wealth is affine linear in the trading strategy, specifying the number of stocks in the portfolio, and the model can be formally expressed as a transaction costs model by issuing at each point in time new artificial securities (see Kühn [[19](https://arxiv.org/html/2602.15177v1#bib.bib19), Section 5]). But LUL, that we consider in the current paper, makes the after-tax wealth non-linear in the trading strategy, which is why many standard arguments from the theory of proportional transaction costs are not applicable. On the other hand, a useful property of LUL is that the after-tax wealth cannot exceed the wealth of the same trading strategy but without taxes. This estimate plays a key role in the paper. In addition, under LUL, the no-arbitrage property is equivalent to that in the corresponding frictionless market. By contrast, with FUL, the after-tax wealth may exceed that of a tax-exempt investor, and the no-arbitrage property is even stronger than that under no taxes (cf. [[19](https://arxiv.org/html/2602.15177v1#bib.bib19), Remark 2.2]).

In the present paper, we first examine the closedness of the set of attainable terminal wealth in the LUL tax model, which forms the basis for the further analysis of optimal portfolios. On a finite probability space, this set is always closed—with respect to the supremum norm and even if the model would allow for an arbitrage (Proposition [3.2](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")). For the general case, however, no-arbitrage alone does not imply that the set of attainable terminal wealth is closed in probability as in discrete time frictionless markets (see Example [3.1](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem1 "Example 3.1 (∄ optimal strategy). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")).

Namely, in models with taxes, one runs into a phenomenon well-known from models with proportional transaction costs. Let us describe this phenomenon in detail. First note that both transaction costs and taxes tend to make portfolio rebalancing disadvantageous. In the first case, an investment needs time to amortize trading costs, and in the second case, realizing book profits can trigger (earlier) tax payments. Now, there can exist an investment in specific quantities of stocks
that, in the first period, leads to the same pre-tax return as the bank account for sure.
On the one hand, a debt-financed purchase of these stocks is riskless in the first period (both for a tax-exempt and a taxable investor).
On the other hand, this purchase can lead to unrealized book profits and realized losses of the same amount at time 11. In the future,
this could provide an advantage for the taxable investor over doing nothing in the first period, since it could help her to defer or even avoid paying taxes. Consequently, with limited initial information, the investor can buy arbitrarily many of these stocks financed with debt at time 0 and then, based on additional information, sell the shares that are not needed at time 11—without any risk. On an infinite probability space, this can destroy the closedness of the set of attainable terminal wealth. The reason is that the amount of purchases at time 0 that could provide a tax advantage need not be bounded ex ante. Exactly the same phenomenon was observed by Schachermayer [[27](https://arxiv.org/html/2602.15177v1#bib.bib27), Example 3.1] in the context of arbitrage-free transaction costs models. By contrast, in an arbitrage-free frictionless market, the phenomenon cannot occur since there, an “advantage” boils down to a higher wealth expressed in terms of monetary units.
Consequently, in discrete time frictionless models, no-arbitrage already implies that the set of attainable terminal wealth is closed in probability (Dalang, Morton, and Willinger [[7](https://arxiv.org/html/2602.15177v1#bib.bib7)]).

To rule out the phenomenon described above, we introduce the no unbounded non-substitutable investment with bounded risk (NUIBR) condition, which is slightly stronger than no-arbitrage and under which the set of attainable terminal wealth turns out to be closed in probability (Theorem [3.6](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem6 "Theorem 3.6. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")).
Then, in Section [4](https://arxiv.org/html/2602.15177v1#S4 "4 Utility maximization ‣ Optimal investment under capital gains taxes"), we analyze the utility maximization problem of terminal wealth, which requires the above closedness property (guaranteed, e.g., by NUIBR). We work with a utility function that takes the value −∞-\infty for a negative terminal wealth, which seems to be quite natural. The utility function has to satisfy only minimal assumptions, that is, it has to be nondecreasing and concave, but it need not even be differentiable. First, we show that the value function is finite if and only if the value function of the corresponding problem without taxes is finite (Proposition [4.2](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")). Then, under the assumptions that the set of attainable terminal wealth is closed in probability and the value function is finite, we show that an optimal strategy always exists (Theorem [4.3](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")). This generalizes Rásonyi and Stettner [[24](https://arxiv.org/html/2602.15177v1#bib.bib24), Theorem 1.1] for frictionless models. Example [4.12](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem12 "Example 4.12 (Non-uniqueness of maximizers). ‣ 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes") shows that the optimal strategy need not be unique.
We note that in continuous time, Kramkov and Schachermayer [[21](https://arxiv.org/html/2602.15177v1#bib.bib21), Example 5.2] provide a counterexample showing that the closedness of the set of attainable terminal wealth—there, it is guaranteed by NFLVR—does not imply that the finite supremum over expected utilities is attained. The counterexample justifies the stronger assumptions on the utility function made for the continuous time maximzation problem in [[21](https://arxiv.org/html/2602.15177v1#bib.bib21)].

As a by-product, we generalize Rásonyi and Stettner [[24](https://arxiv.org/html/2602.15177v1#bib.bib24), Theorem 1.1] to frictionless markets with short-selling constraints.
We obtain a different integrable majorant for the utilities of attainable terminal wealth, that may be of independent interest:
Let x>0x>0 and d∈ℕd\in{\mathbb{N}} denotes the number of risky assets.
Then, in an arbitrage-free one-period model, there exists a trading strategy with initial capital (2d+1−1)​x(2^{d+1}-1)x whose terminal wealth dominates PP-a.s. the terminal wealth of any strategy with initial capital xx and PP-a.s. nonnegative wealth. The result directly extends to a TT-period model, where the required initial capital increases to (2d+1−1)T​x(2^{d+1}-1)^{T}x.
Since the value function is finite for all positive initial capitals if it is finite for initial capital xx, the utility of the dominating strategy
is an integrable majorant of all utilities that can be achieved with initial capital xx.
The proof in [[24](https://arxiv.org/html/2602.15177v1#bib.bib24), Theorem 1.1] relies on a similar one-period estimate, but with an integrable majorant which need not be the utility of an attainable terminal wealth for some initial capital. This is the reason why their estimate cannot be directly extended to a multiperiod model. To make their result applicable to the multiperiod case, [[24](https://arxiv.org/html/2602.15177v1#bib.bib24)] establish a dynamic programming principle and consider one-period majorants with regard to the value function instead of the utility function.

## 2 The model

Throughout the paper, we fix a terminal time T∈ℕT\in{\mathbb{N}} and a filtered probability space (Ω,ℱ,(ℱt)t=0,1,…,T,P)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t=0,1,\ldots,T},P). (In)equalities between random variables are understood almost surely unless stated otherwise. In contexts involving random sets, however, “a.s.” is written explicitly.
There are d∈ℕd\in{\mathbb{N}} non-shortable risky assets with adapted price processes Sj=(Stj)t=0,1,…,TS^{j}=(S^{j}\_{t})\_{t=0,1,\ldots,T}, j=1,…,dj=1,\ldots,d. In addition, the investor can both lend to and borrow from a bank account at the same interest rate modeled by the nonnegative adapted process r=(rt)t=1,…,Tr=(r\_{t})\_{t=1,\ldots,T}. That is, rtr\_{t} is the interest rate between t−1t-1 and tt. It seems to be reasonable to assume that rtr\_{t} is even ℱt−1\mathcal{F}\_{t-1}-measurable, but mathematically this is not used anywhere in the paper.
Following the notation in [[11](https://arxiv.org/html/2602.15177v1#bib.bib11)], Ni,t,j∈L0​(ℱt;ℝ+)N\_{i,t,j}\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}\_{+}) denotes the number of assets of type j∈{1,…,d}j\in\{1,\ldots,d\} that are bought at time i∈{0,…,T−1}i\in\{0,\ldots,T-1\} and kept in the portfolio at least after trading
at time t∈{i,…,T}t\in\{i,\ldots,T\}. Here, L0​(ℱt;ℝ+)L^{0}(\mathcal{F}\_{t};{\mathbb{R}}\_{+}) denotes the space of equivalence classes of ℱt\mathcal{F}\_{t}-measurable ℝ+{\mathbb{R}}\_{+}-valued random
variables, equipped with the topology of convergence in probability.
By the implicit assumption that an asset cannot be bought and resold at the same time, Ni,i,jN\_{i,i,j} is the number of shares of type jj purchased at time ii. Short-selling is excluded, and one has the constraint

|  |  |  |
| --- | --- | --- |
|  | Nt,t,j≥Nt,t+1,j≥…≥Nt,T,j=0for ​t=0,…,T−1,\displaystyle N\_{t,t,j}\geq N\_{t,t+1,j}\geq\ldots\geq N\_{t,T,j}=0\quad\mbox{for\ }t=0,\ldots,T-1, |  |

which forces liquidation at TT. The set of all such strategies NN is denoted by 𝒩\mathcal{N}.
For brevity we sometimes write SS for the vector (S1,…,Sd)(S^{1},\ldots,S^{d}), Ni,tN\_{i,t} for the vector (Ni,t,1,…,Ni,t,d)(N\_{i,t,1},\ldots,N\_{i,t,d}), and denote by ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle and |⋅||\cdot| the scalar product and the Euclidean norm in ℝd{\mathbb{R}}^{d}, respectively. By ηt∈L0​(ℱt;ℝ)\eta\_{t}\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}) we denote the number of monetary units after paying taxes and trading at time tt. First, we define the accumulated realized profits and losses by

|  |  |  |  |
| --- | --- | --- | --- |
|  | G0:=0,Gt:=∑u=1t(ηu−1​ru+∑i=0u−1⟨Ni,u−1−Ni,u,Su−Si⟩),t≥1.\displaystyle G\_{0}:=0,\quad G\_{t}:=\sum\_{u=1}^{t}\left(\eta\_{u-1}r\_{u}+\sum\_{i=0}^{u-1}\langle N\_{i,u-1}-N\_{i,u},S\_{u}-S\_{i}\rangle\right),\quad t\geq 1. |  | (2.1) |

This means that taxes on the interest payments of the bank account cannot be deferred.
Then, the tax payment stream with limited use of losses (LUL) is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πt:=α​maxu=0,1,…,t⁡Gu,t≥0,\displaystyle\Pi\_{t}:=\alpha\max\_{u=0,1,\ldots,t}G\_{u},\quad t\geq 0, |  | (2.2) |

where α∈[0,1)\alpha\in[0,1) is the constant tax rate. A strategy (η,N)(\eta,N) is called self-financing for the initial capital x∈ℝx\in{\mathbb{R}} iff η−1=x\eta\_{-1}=x and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηt−ηt−1=rt​ηt−1​1(t≥1)+⟨∑i=0t−1(Ni,t−1−Ni,t)−Nt,t,St⟩−(Πt−Πt−1)​1(t≥1),t≥0.\displaystyle\eta\_{t}-\eta\_{t-1}=r\_{t}\eta\_{t-1}1\_{(t\geq 1)}+\left\langle\sum\_{i=0}^{t-1}(N\_{i,t-1}-N\_{i,t})-N\_{t,t},S\_{t}\right\rangle-(\Pi\_{t}-\Pi\_{t-1})1\_{(t\geq 1)},\quad t\geq 0. |  | (2.3) |

We note that given x∈ℝx\in{\mathbb{R}} and N∈𝒩N\in\mathcal{N}, definition ([2.1](https://arxiv.org/html/2602.15177v1#S2.E1 "In 2 The model ‣ Optimal investment under capital gains taxes"))-([2.3](https://arxiv.org/html/2602.15177v1#S2.E3 "In 2 The model ‣ Optimal investment under capital gains taxes")) yields an explicit construction of a unique adapted process η=:η(x,N)\eta=:\eta(x,N) such that (η,N)(\eta,N) is self-financing with initial capital xx. This is because GtG\_{t} and thus Πt\Pi\_{t} do not depend on ηt\eta\_{t}.
For every α∈[0,1)\alpha\in[0,1), the terminal wealth is denoted by

|  |  |  |
| --- | --- | --- |
|  | Vα​(x,N):=ηT.\displaystyle V^{\alpha}(x,N):=\eta\_{T}. |  |

For the special case of a frictionless market, i.e., α=0\alpha=0, the wealth process can be defined by

|  |  |  |
| --- | --- | --- |
|  | Vt0​(x,N):=ηt+⟨∑i=0tNi,t,St⟩,t=0,1,…,T.\displaystyle V^{0}\_{t}(x,N):=\eta\_{t}+\left\langle\sum\_{i=0}^{t}N\_{i,t},S\_{t}\right\rangle,\quad t=0,1,\ldots,T. |  |

It satisfies the recursion V00​(x,N)=xV\_{0}^{0}(x,N)=x and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt0​(x,N)=(1+rt)​Vt−10​(x,N)+⟨∑i=0t−1Ni,t−1,St−(1+rt)​St−1⟩,t=1,…,T.V\_{t}^{0}(x,N)=(1+r\_{t})V\_{t-1}^{0}(x,N)+\left\langle\sum\_{i=0}^{t-1}N\_{i,t-1},S\_{t}-(1+r\_{t})S\_{t-1}\right\rangle,\quad t=1,\ldots,T. |  | (2.4) |

By contrast, for α>0\alpha>0, there is no canonical one-dimensional wealth for t<Tt<T, as there is no one-to-one relation between
a stock position Ni,t,jN\_{i,t,j} with unrealized gain Ni,t,j​(Stj−Sij)N\_{i,t,j}(S^{j}\_{t}-S^{j}\_{i}) and a taxed amount in the bank account.

###### Remark 2.1.

Natural generalizations are to introduce dividends or to limit tax payments to a subset of time points in {1,…,T}\{1,\ldots,T\}.
We refrain from doing so to avoid complicating the notation, but we stress that the main results of the paper would still hold.

###### Definition 2.2.

The model satisfies the no-arbitrage (NA) condition iff for every N∈𝒩N\in\mathcal{N} the following implication holds:

|  |  |  |
| --- | --- | --- |
|  | Vα​(0,N)≥0a.s.⟹Vα​(0,N)=0a.s.\displaystyle V^{\alpha}(0,N)\geq 0\quad\mbox{a.s.}\quad\implies\quad V^{\alpha}(0,N)=0\quad\mbox{a.s.} |  |

###### Lemma 2.3.

The following basic properties hold.

1. (i)

   Let x∈ℝx\in{\mathbb{R}} and N∈𝒩N\in\mathcal{N}. The process η\eta from ([2.3](https://arxiv.org/html/2602.15177v1#S2.E3 "In 2 The model ‣ Optimal investment under capital gains taxes")) that makes (η,N)(\eta,N) self-financing for the initial capital xx satisfies

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ηt=x+Gt−Πt−∑i=0t⟨Ni,t,Si⟩,t=0,1,…,T.\displaystyle\eta\_{t}=x+G\_{t}-\Pi\_{t}-\sum\_{i=0}^{t}\langle N\_{i,t},S\_{i}\rangle,\quad t=0,1,\ldots,T. |  | (2.5) |
2. (ii)

   The terminal wealth is positive homogeneous in (x,N)(x,N), i.e., for all λ∈ℝ+\lambda\in{\mathbb{R}}\_{+}, x∈ℝx\in{\mathbb{R}}, and N∈𝒩N\in\mathcal{N}, we have Vα​(λ​x,λ​N)=λ​Vα​(x,N)V^{\alpha}(\lambda x,\lambda N)=\lambda V^{\alpha}(x,N).
3. (iii)

   For every x∈ℝx\in\mathbb{R} and every N∈𝒩N\in\mathcal{N}, we have that Vα​(x,N)≤V0​(x,N)V^{\alpha}(x,N)\leq V^{0}(x,N).
4. (iv)

   The terminal wealth is concave in (x,N)(x,N), i.e., for all λ∈[0,1]\lambda\in[0,1], x(1),x(2)∈ℝx^{(1)},x^{(2)}\in{\mathbb{R}}, and N(1),N(2)∈𝒩N^{(1)},N^{(2)}\in\mathcal{N}, we have

   |  |  |  |
   | --- | --- | --- |
   |  | Vα​(λ​x(1)+(1−λ)​x(2),λ​N(1)+(1−λ)​N(2))≥λ​Vα​(x(1),N(1))+(1−λ)​Vα​(x(2),N(2)),\displaystyle V^{\alpha}(\lambda x^{(1)}+(1-\lambda)x^{(2)},\lambda N^{(1)}+(1-\lambda)N^{(2)})\geq\lambda V^{\alpha}(x^{(1)},N^{(1)})+(1-\lambda)V^{\alpha}(x^{(2)},N^{(2)}), |  |

   and thus for all x∈ℝx\in{\mathbb{R}}, the set {Vα​(x,N):N∈𝒩}−L0​(ℱT;ℝ+)\{V^{\alpha}(x,N)\ :\ N\in\mathcal{N}\}-L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+}) is convex.
5. (v)

   The NA condition holds if and only if it holds for the corresponding tax-free model.

###### Proof.

Ad (i)(i). Follows by considering the increments between t−1t-1 and tt.

Ad (i​i)(ii). Using ([2.3](https://arxiv.org/html/2602.15177v1#S2.E3 "In 2 The model ‣ Optimal investment under capital gains taxes")), it can easily be shown by induction on tt that the mapping (x,N)↦ηt​(x,N)(x,N)\mapsto\eta\_{t}(x,N), where η\eta is given by ([2.3](https://arxiv.org/html/2602.15177v1#S2.E3 "In 2 The model ‣ Optimal investment under capital gains taxes")), is positive homogenous.

Ad (i​i​i)(iii). Let us show by induction that ηt0≥ηtα\eta^{0}\_{t}\geq\eta^{\alpha}\_{t} for t=0,…,Tt=0,\ldots,T, where η0\eta^{0} and ηα\eta^{\alpha} are given by the self-financing
condition with tax rates 0 and α\alpha, respectively. The base case t=0t=0 is trivial. Suppose that we have shown the assertion for all s<ts<t. We get Gtα≤Gt0G^{\alpha}\_{t}\leq G^{0}\_{t}, and the claim immediately follows from ([2.5](https://arxiv.org/html/2602.15177v1#S2.E5 "In item 1 ‣ Lemma 2.3. ‣ 2 The model ‣ Optimal investment under capital gains taxes")).

Ad (i​v)(iv). For λ∈[0,1]\lambda\in[0,1], x(1),x(2)∈ℝx^{(1)},x^{(2)}\in\mathbb{R}, and N(1),N(2)∈𝒩N^{(1)},N^{(2)}\in\mathcal{N} define x:=λ​x(1)+(1−λ)​x(2)x:=\lambda x^{(1)}+(1-\lambda)x^{(2)} and N:=λ​N(1)+(1−λ)​N(2)N:=\lambda N^{(1)}+(1-\lambda)N^{(2)}. Let us prove by induction the stronger claim that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηt​(x,N)≥λ​ηt​(x(1),N(1))+(1−λ)​ηt​(x(2),N(2))for​t=0,…,T.\displaystyle\eta\_{t}(x,N)\geq\lambda\eta\_{t}(x^{(1)},N^{(1)})+(1-\lambda)\eta\_{t}(x^{(2)},N^{(2)})\quad\mbox{for}\ t=0,\ldots,T. |  | (2.6) |

The base case t=0t=0 is trivial. Suppose that we have shown ([2.6](https://arxiv.org/html/2602.15177v1#S2.E6 "In Proof. ‣ 2 The model ‣ Optimal investment under capital gains taxes")) for every time s<ts<t.
On the set {Πt​(N)=Πt−1​(N)}\{\Pi\_{t}(N)=\Pi\_{t-1}(N)\}, we use the self-financing condition ([2.3](https://arxiv.org/html/2602.15177v1#S2.E3 "In 2 The model ‣ Optimal investment under capital gains taxes")) and ([2.6](https://arxiv.org/html/2602.15177v1#S2.E6 "In Proof. ‣ 2 The model ‣ Optimal investment under capital gains taxes")) for t−1t-1 to get

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | ηt​(x,N)−λ​ηt​(x(1),N(1))−(1−λ)​ηt​(x(2),N(2))\displaystyle\eta\_{t}(x,N)-\lambda\eta\_{t}(x^{(1)},N^{(1)})-(1-\lambda)\eta\_{t}(x^{(2)},N^{(2)}) |  |
|  |  | ≥\displaystyle\geq | λ​(Πt​(x(1),N(1))−Πt−1​(x(1),N(1)))+(1−λ)​(Πt​(x(2),N(2))−Πt−1​(x(2),N(2)))≥ 0.\displaystyle\lambda(\Pi\_{t}(x^{(1)},N^{(1)})-\Pi\_{t-1}(x^{(1)},N^{(1)}))+(1-\lambda)(\Pi\_{t}(x^{(2)},N^{(2)})-\Pi\_{t-1}(x^{(2)},N^{(2)}))\ \geq\ 0. |  |

On the set {Πt​(x,N)>Πt−1​(x,N)}\{\Pi\_{t}(x,N)>\Pi\_{t-1}(x,N)\}, we use ([2.5](https://arxiv.org/html/2602.15177v1#S2.E5 "In item 1 ‣ Lemma 2.3. ‣ 2 The model ‣ Optimal investment under capital gains taxes")), Πt​(x(j),N(j))≥α​Gt​(x(j),N(j))\Pi\_{t}(x^{(j)},N^{(j)})\geq\alpha G\_{t}(x^{(j)},N^{(j)}) for j=1,2j=1,2, ([2.6](https://arxiv.org/html/2602.15177v1#S2.E6 "In Proof. ‣ 2 The model ‣ Optimal investment under capital gains taxes")) for all s<ts<t, and r≥0r\geq 0 to conclude that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | ηt​(x,N)−λ​ηt​(x(1),N(1))−(1−λ)​ηt​(x(2),N(2))\displaystyle\eta\_{t}(x,N)-\lambda\eta\_{t}(x^{(1)},N^{(1)})-(1-\lambda)\eta\_{t}(x^{(2)},N^{(2)}) |  |
|  |  | =\displaystyle= | ∑s=1trs​(ηs−1​(x,N)−λ​ηs−1​(x(1),N(1))−(1−λ)​ηs−1​(x(2),N(2)))−Πt​(x,N)\displaystyle\sum\_{s=1}^{t}r\_{s}(\eta\_{s-1}(x,N)-\lambda\eta\_{s-1}(x^{(1)},N^{(1)})-(1-\lambda)\eta\_{s-1}(x^{(2)},N^{(2)}))-\Pi\_{t}(x,N) |  |
|  |  |  | +λ​Πt​(x(1),N(1))+(1−λ)​Πt​(x(2),N(2))\displaystyle+\lambda\Pi\_{t}(x^{(1)},N^{(1)})+(1-\lambda)\Pi\_{t}(x^{(2)},N^{(2)}) |  |
|  |  | ≥\displaystyle\geq | ∑s=1t(1−α)​rs​(ηs−1​(x,N)−λ​ηs−1​(x(1),N(1))−(1−λ)​ηs−1​(x(2),N(2)))\displaystyle\sum\_{s=1}^{t}(1-\alpha)r\_{s}(\eta\_{s-1}(x,N)-\lambda\eta\_{s-1}(x^{(1)},N^{(1)})-(1-\lambda)\eta\_{s-1}(x^{(2)},N^{(2)})) |  |
|  |  | ≥\displaystyle\geq | 0.\displaystyle 0. |  |

Ad (v)(v). This follows from part (iii) and from the fact that the frictionless market allows for an arbitrage in a single period if it does not satisfy NA.
∎

###### Remark 2.4.

The proof of Lemma [2.3](https://arxiv.org/html/2602.15177v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2 The model ‣ Optimal investment under capital gains taxes")(iv) shows that for concavity, which is essential for the further analysis, one needs that rt≥0r\_{t}\geq 0.
Otherwise, it may happen that the absence of taxes due to an unavoidable realization of losses is disadvantageous if they have to be paid later.

## 3 Closedness

The following example shows that NA alone does not imply that the set of attainable terminal wealth is closed in probability. Furthermore, the supremum in a log-utility maximization problem is not attained.
The basic idea, already described in the introduction, is that in the first period the stock has the same return as the bank account for sure, but
a debt-financed purchase at time 0 provides a tax advantage if the stock return between 11 and 22 is higher than the interest rate
and a part of the stocks are sold at time 22.

###### Example 3.1 (∄\nexists optimal strategy).

Let T=3T=3, α∈(0,1)\alpha\in(0,1), and r∈ℝ+∖{0}r\in{\mathbb{R}}\_{+}\setminus\{0\}. We introduce the random variables YY, Z2Z\_{2}, and Z3Z\_{3} with
(conditional) probabilities P​(Y=k)=22−kP(Y=k)=2^{2-k}, P​(Z2=ck|Y=k)=p1,kP(Z\_{2}=c\_{k}\ |\ Y=k)=p\_{1,k}, P​(Z2=−r/k|Y=k)=1−p1,kP(Z\_{2}=-r/k\ |\ Y=k)=1-p\_{1,k},
P(Z3=ck|Y=k,Z2=ck)=p2,kP(Z\_{3}=c\_{k}\ |\ Y=k,Z\_{2}=c\_{k})=p\_{2,k}, P(Z3=−r/k|Y=k,Z2=ck)=1−p2,kP(Z\_{3}=-r/k\ |\ Y=k,Z\_{2}=c\_{k})=1-p\_{2,k}, and
P(Z3=−1−r|Y=k,Z2=−r/k)=1P(Z\_{3}=-1-r\ |\ Y=k,Z\_{2}=-r/k)=1 for all k∈ℕk\in{\mathbb{N}} with k≥3k\geq 3, where ck:=(k−2)​(2​r+r2)/(k​(1+r))c\_{k}:=(k-2)(2r+r^{2})/\left(k(1+r)\right). The probabilities p1,k,p2,k∈(0,1)p\_{1,k},p\_{2,k}\in(0,1) for k≥3k\geq 3 are not yet specified. The filtration is given by ℱ0={∅,Ω}\mathcal{F}\_{0}=\{\emptyset,\Omega\}, ℱ1=σ​(Y)\mathcal{F}\_{1}=\sigma(Y), ℱ2=σ​(Y,Z2)\mathcal{F}\_{2}=\sigma(Y,Z\_{2}), and ℱ3=σ​(Y,Z2,Z3)\mathcal{F}\_{3}=\sigma(Y,Z\_{2},Z\_{3}).

We have a single stock with price process (St)t=0,1,2,3(S\_{t})\_{t=0,1,2,3} given by S0=1S\_{0}=1, S1=1+rS\_{1}=1+r, S2=(1+r)​(1+r+Z2)S\_{2}=(1+r)(1+r+Z\_{2}), and S3=(1+r)​(1+r+Z2)​(1+r+Z3)S\_{3}=(1+r)(1+r+Z\_{2})(1+r+Z\_{3}). The interest rate process (rt)t=1,2,3(r\_{t})\_{t=1,2,3} is given by r1=r2=rr\_{1}=r\_{2}=r and r3=r​1{Z2>0}r\_{3}=r1\_{\{Z\_{2}>0\}}. The model obviously satisfies NA. Consider the utility maximization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(1):=supN∈𝒩𝔼​[ln⁡(Vα​(1,N)−α)]\displaystyle u(1):=\sup\_{N\in\mathcal{N}}\mathbb{E}[\ln(V^{\alpha}(1,N)-\alpha)] |  | (3.1) |

with the convention that ln⁡(x):=−∞\ln(x):=-\infty for x≤0x\leq 0 and 𝔼​[ln⁡(Vα​(1,N)−α)]:=−∞\mathbb{E}[\ln(V^{\alpha}(1,N)-\alpha)]:=-\infty if 𝔼​[ln−⁡(Vα​(1,N)−α)]=∞\mathbb{E}[\ln^{-}(V^{\alpha}(1,N)-\alpha)]=\infty. In addition, we consider the auxiliary frictionless maximization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | u~​(1):=supN~∈𝒩~𝔼​[ln⁡((1−α)​V0​(1,N~)+α−α)],\displaystyle\widetilde{u}(1):=\sup\_{\widetilde{N}\in\widetilde{\mathcal{N}}}\mathbb{E}[\ln((1-\alpha)V^{0}(1,\widetilde{N})+\alpha-\alpha)], |  | (3.2) |

where 𝒩~\widetilde{\mathcal{N}} is the set of strategies with regard to the larger filtration given by ℱ~0=ℱ~1=ℱ1\widetilde{\mathcal{F}}\_{0}=\widetilde{\mathcal{F}}\_{1}=\mathcal{F}\_{1}, ℱ~2=ℱ2\widetilde{\mathcal{F}}\_{2}=\mathcal{F}\_{2}, and ℱ~3=ℱ3\widetilde{\mathcal{F}}\_{3}=\mathcal{F}\_{3}.

Now, we choose the probabilities p1,kp\_{1,k} and p2,kp\_{2,k} such that the set of maximizers of the frictionless problem ([3.2](https://arxiv.org/html/2602.15177v1#S3.E2 "In Example 3.1 (∄ optimal strategy). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) is given by {N~∈𝒩~:N~0,1+N~1,1=YandN~0,2+N~1,2+N~2,2=Y/21{Z2>0}}=:ℳ~≠∅\{\widetilde{N}\in\widetilde{\mathcal{N}}\ :\ \widetilde{N}\_{0,1}+\widetilde{N}\_{1,1}=Y\ \mbox{and}\ \widetilde{N}\_{0,2}+\widetilde{N}\_{1,2}+\widetilde{N}\_{2,2}=Y/21\_{\{Z\_{2}>0\}}\}=:\widetilde{\mathcal{M}}\not=\emptyset.
This means that the amounts invested in the stock during the second and third period are uniquely determined by optimality, whereas the amount invested during the first period is arbitrary.
To see that this is possible, we first turn to discounted values by adding the constant −𝔼​[ln⁡((1+r)2​(1+r​1{Z2>0}))]-\mathbb{E}[\ln((1+r)^{2}(1+r1\_{\{Z\_{2}>0\}}))] to ([3.2](https://arxiv.org/html/2602.15177v1#S3.E2 "In Example 3.1 (∄ optimal strategy). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")).
For strategies from ℳ~\widetilde{\mathcal{M}}, the frictionless wealth is nondecreasing for sure, and thus the discounted terminal wealth is bounded away from zero uniformly in Y​(ω)Y(\omega), ω∈Ω\omega\in\Omega. In addition, it is uniformly bounded from above. Given Y​(ω)Y(\omega), we have a complete market with a unique equivalent martingale measure QQ. The optimality condition that the marginal utility is proportional to d​Q/d​PdQ/dP
(see, e.g., [[21](https://arxiv.org/html/2602.15177v1#bib.bib21), Theorem 2.0]) leads to 33 equations with 33 unknown that have a unique solution. Without the first period, the market is non-redundant, and the 33-dimensional maximizer (N~0,1+N~1,1,(N~0,2+N~1,2+N~2,2)​1{Z2>0},(N~0,2+N~1,2+N~2,2)​1{Z2<0})(\widetilde{N}\_{0,1}+\widetilde{N}\_{1,1},(\widetilde{N}\_{0,2}+\widetilde{N}\_{1,2}+\widetilde{N}\_{2,2})1\_{\{Z\_{2}>0\}},(\widetilde{N}\_{0,2}+\widetilde{N}\_{1,2}+\widetilde{N}\_{2,2})1\_{\{Z\_{2}<0\}}) is unique.

Next observe that by 𝒩⊆𝒩~\mathcal{N}\subseteq\widetilde{\mathcal{N}} and by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vα​(1,N)=1+G3α−Π3≤(1−α)​[1+G3α]+α≤(1−α)​V0​(1,N)+αfor all​N∈𝒩,\displaystyle V^{\alpha}(1,N)=1+G\_{3}^{\alpha}-\Pi\_{3}\leq(1-\alpha)\left[1+G\_{3}^{\alpha}\right]+\alpha\leq(1-\alpha)V^{0}(1,N)+\alpha\quad\mbox{for all}\ N\in\mathcal{N}, |  | (3.3) |

we have u~​(1)≥u​(1)\widetilde{u}(1)\geq u(1). To show equality, we consider the sequence (Nn)n∈ℕ⊆𝒩(N^{n})\_{n\in{\mathbb{N}}}\subseteq\mathcal{N} given by N0,0n:=nN^{n}\_{0,0}:=n, N0,1n:=Y​1{Y≤n}N^{n}\_{0,1}:=Y1\_{\{Y\leq n\}}, N0,2n:=Y/21{Y≤n,Z2>0}N^{n}\_{0,2}:=Y/21\_{\{Y\leq n,Z\_{2}>0\}}, N1,1n:=0N^{n}\_{1,1}:=0, and N2,2n:=0N^{n}\_{2,2}:=0.
By the choice of ckc\_{k}, we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (k−1)​(2​r+r2)=k2​(2​r+ck+r2+r​ck)for all ​k≥3,\displaystyle(k-1)(2r+r^{2})=\frac{k}{2}\left(2r+c\_{k}+r^{2}+rc\_{k}\right)\quad\mbox{for all }k\geq 3, |  | (3.4) |

which guarantees that the strategies NnN^{n} satisfy G2​(Nn)=0G\_{2}(N^{n})=0, G3​(Nn)>0G\_{3}(N^{n})>0 on {Y≤n,Z2>0}\{Y\leq n,Z\_{2}>0\} and η2​(Nn)=η3​(Nn)\eta\_{2}(N^{n})=\eta\_{3}(N^{n}), G2​(Nn)=G3​(Nn)>0G\_{2}(N^{n})=G\_{3}(N^{n})>0 on {Y≤n,Z2<0}\{Y\leq n,Z\_{2}<0\}. Hence, by the choice of r3r\_{3}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vα​(1,Nn)=(1−α)​V0​(1,Nn)+αon​{Y≤n}.\displaystyle V^{\alpha}(1,N^{n})=(1-\alpha)V^{0}(1,N^{n})+\alpha\quad\mbox{on}\ \{Y\leq n\}. |  | (3.5) |

This means that on {Y≤n}\{Y\leq n\}, strategy NnN^{n} pays taxes prematurely only when the interest rate vanishes afterwards.
Since ln⁡(Vα​(1,Nn)−α)\ln(V^{\alpha}(1,N^{n})-\alpha) is bounded from both sides uniformly in n∈ℕn\in{\mathbb{N}}, ([3.3](https://arxiv.org/html/2602.15177v1#S3.E3 "In Example 3.1 (∄ optimal strategy). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) and ([3.5](https://arxiv.org/html/2602.15177v1#S3.E5 "In Example 3.1 (∄ optimal strategy). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) imply that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ln⁡(Vα​(1,Nn)−α)]→u~​(1)as​n→∞,\displaystyle\mathbb{E}[\ln(V^{\alpha}(1,N^{n})-\alpha)]\to\widetilde{u}(1)\quad\mbox{as}\ n\to\infty, |  |

which yields u​(1)=u~​(1)u(1)=\widetilde{u}(1). Together with inequality ([3.3](https://arxiv.org/html/2602.15177v1#S3.E3 "In Example 3.1 (∄ optimal strategy). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) and the fact that the set of maximizers of ([3.2](https://arxiv.org/html/2602.15177v1#S3.E2 "In Example 3.1 (∄ optimal strategy). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) is given
by ℳ~\widetilde{\mathcal{M}}, this implies that any maximizer of ([3.1](https://arxiv.org/html/2602.15177v1#S3.E1 "In Example 3.1 (∄ optimal strategy). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) must satisfy the following conditions:

1. (i)

   N0,1+N1,1=YN\_{0,1}+N\_{1,1}=Y, N0,2+N1,2+N2,2=Y/21{Z2>0}N\_{0,2}+N\_{1,2}+N\_{2,2}=Y/21\_{\{Z\_{2}>0\}},
2. (ii)

   Vα​(1,N)=(1−α)​V0​(1,N)+αV^{\alpha}(1,N)=(1-\alpha)V^{0}(1,N)+\alpha.

Let us show that no such N∈𝒩N\in\mathcal{N} exists. Assume that N∈𝒩N\in\mathcal{N} satisfies (i). W.l.o.g. we can assume that N0,0≥1N\_{0,0}\geq 1, that is, the initial capital is invested in the stock and not in the bank account with the same return.
Since N0,0N\_{0,0} is non-random, there exists k∈ℕk\in{\mathbb{N}} with k>2​N0,0k>2N\_{0,0}, and one has P​(Y=k,Z2>0)>0P(Y=k,Z\_{2}>0)>0.
On the set {Y=k,Z2>0}\{Y=k,Z\_{2}>0\}, the loss pool immediately before stocks are sold at time 22 is (k−1)​(2​r+r2)−r​N1,1(k-1)(2r+r^{2})-rN\_{1,1}, which coincides with k/2​(1+r)​(r+ck)−r​(N1,1−k/2)k/2(1+r)(r+c\_{k})-r(N\_{1,1}-k/2) by ([3.4](https://arxiv.org/html/2602.15177v1#S3.E4 "In Example 3.1 (∄ optimal strategy). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")).
On the other hand, on {Y=k,Z2>0}\{Y=k,Z\_{2}>0\}, one has that N1,1>k/2N\_{1,1}>k/2, and k/2k/2 stocks are sold at time 22. Thus, even if one takes the stocks purchased at time 11, which have the lower book profit (1+r)​(r+ck)(1+r)(r+c\_{k}) per share, taxes must be paid prematurely. Then, it follows by r3>0r\_{3}>0 on {Z2>0}\{Z\_{2}>0\} that P​((1−α)​V0​(1,N)+α>Vα​(1,N))>0P((1-\alpha)V^{0}(1,N)+\alpha>V^{\alpha}(1,N))>0. Thus, NN does not satisfy (ii), and the supremum in ([3.1](https://arxiv.org/html/2602.15177v1#S3.E1 "In Example 3.1 (∄ optimal strategy). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) is not attained.

Furthermore, for an arbitrary N~∈ℳ~\widetilde{N}\in\widetilde{\mathcal{M}}, one has Vα​(1,Nn)→(1−α)​V0​(1,N~)+αV^{\alpha}(1,N^{n})\to(1-\alpha)V^{0}(1,\widetilde{N})+\alpha in probability as n→∞n\to\infty, which shows that {Vα​(1,N):N∈𝒩}−L0​(ℱT;ℝ+)\{V^{\alpha}(1,N):N\in\mathcal{N}\}-L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+}) is not closed in probability.

On the other hand, for a finite probability space, the set of attainable terminal wealth is always closed—even if NA does not hold.

###### Proposition 3.2.

Let |Ω|<∞|\Omega|<\infty and x∈ℝx\in{\mathbb{R}}. Then, {Vα​(x,N):N∈𝒩}−L0​(ℱT;ℝ+)\{V^{\alpha}(x,N):N\in\mathcal{N}\}-L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+}) is closed (with respect to the supremum norm).

###### Proof.

We consider a family of artificial linear tax rules with tax rebates for realized losses. For each tax rule, there is a random subset of time points in {1,…,T}\{1,\ldots,T\}, and outside this random set no taxes are paid. To formalize this, let (τt)t=1,…,T(\tau\_{t})\_{t=1,\ldots,T} be an adapted {0,…,T}\{0,\ldots,T\}-valued process with τ1≤…≤τT\tau\_{1}\leq\ldots\leq\tau\_{T}, τt≤t\tau\_{t}\leq t, and ττt=τt\tau\_{\tau\_{t}}=\tau\_{t} for τt≥1\tau\_{t}\geq 1. For a given strategy NN, we define the tax process by Πt(τ):=α​Gτt\Pi^{(\tau)}\_{t}:=\alpha G\_{\tau\_{t}}, where GG is given in ([2.1](https://arxiv.org/html/2602.15177v1#S2.E1 "In 2 The model ‣ Optimal investment under capital gains taxes")), and the corresponding self-financing position in the bank account with initial capital xx is given in ([2.3](https://arxiv.org/html/2602.15177v1#S2.E3 "In 2 The model ‣ Optimal investment under capital gains taxes")). The latter is denoted by η(τ)​(N)\eta^{(\tau)}(N). We note that—as in the original model—the recursive construction is explicit since GtG\_{t} does not depend on ηt\eta\_{t}. The random variable τt\tau\_{t} is interpreted as the last time in {0,1,…,t}\{0,1,\ldots,t\} at which taxes on accumulated realized gains and losses are paid (since G0=0G\_{0}=0, τt=0\tau\_{t}=0 means that no taxes are payed up to time tt). Of course, it can happen that gains and losses are not taxed at all under such a rule. Let us show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vα​(x,N)=minτ⁡ηT(τ)​(N),\displaystyle V^{\alpha}(x,N)=\min\_{\tau}\eta^{(\tau)}\_{T}(N), |  | (3.6) |

where the minimum is taken over the finite set of all tax rules described above. The inequality “≥\geq” is obvious since for a fixed strategy NN, the LUL tax process coincides with the tax process of the artificial tax rule with τt⋆:=min⁡{s∈{0,…,t}:Gs​(N)=maxu=0,…,t⁡Gu​(N)}\tau^{\star}\_{t}:=\min\{s\in\{0,\ldots,t\}:G\_{s}(N)=\max\_{u=0,\ldots,t}G\_{u}(N)\}.
To show “≤\leq”, we start with an arbitrary tax rule τ\tau and define the tax rule

|  |  |  |
| --- | --- | --- |
|  | τt1:={τtif​τt≥21if​τt≤1​and​G1>00if​τt≤1​and​G1≤0,t≥1.\displaystyle\tau^{1}\_{t}:=\left\{\begin{array}[]{ll}\tau\_{t}&\textrm{if}\ \tau\_{t}\geq 2\\ 1&\textrm{if}\ \tau\_{t}\leq 1\ \mbox{and}\ G\_{1}>0\\ 0&\textrm{if}\ \tau\_{t}\leq 1\ \mbox{and}\ G\_{1}\leq 0\\ \end{array},\quad t\geq 1.\right. |  |

By {τ11=1}={G1>0}\{\tau^{1}\_{1}=1\}=\{G\_{1}>0\} and by r≥0r\geq 0, it follows that ηT(τ1)​(N)≤ηT(τ)​(N)\eta^{(\tau^{1})}\_{T}(N)\leq\eta^{(\tau)}\_{T}(N). Analogously, we construct the tax rule

|  |  |  |
| --- | --- | --- |
|  | τt2:={τt1if​τt1≥3​or​t=12if​τt1≤2​and​t≥2​and​G2>0∨G1τ11if​τt1≤2​and​t≥2​and​G2≤0∨G1,t≥1,\displaystyle\tau^{2}\_{t}:=\left\{\begin{array}[]{ll}\tau^{1}\_{t}&\textrm{if}\ \tau^{1}\_{t}\geq 3\ \mbox{or}\ t=1\\ 2&\textrm{if}\ \tau^{1}\_{t}\leq 2\ \mbox{and}\ t\geq 2\ \mbox{and}\ G\_{2}>0\vee G\_{1}\\ \tau^{1}\_{1}&\textrm{if}\ \tau^{1}\_{t}\leq 2\ \mbox{and}\ t\geq 2\ \mbox{and}\ G\_{2}\leq 0\vee G\_{1}\\ \end{array},\quad t\geq 1,\right. |  |

where the process GG is that associated with the tax rule τ1\tau^{1}.
After TT steps we arrive at τ⋆\tau^{\star}, and Vα​(x,N)=ηT(τ⋆)​(N)≤ηT(τ)​(N)V^{\alpha}(x,N)=\eta^{(\tau^{\star})}\_{T}(N)\leq\eta^{(\tau)}\_{T}(N) is proven for
all τ\tau.

Now, we identify a strategy N∈𝒩N\in\mathcal{N} with the vector consisting of the nonnegative values of Nt,t,jN\_{t,t,j}, t=0,…,T−1t=0,\ldots,T-1, j=1,…,dj=1,\ldots,d, and Ni,t−1,j−Ni,t,jN\_{i,t-1,j}-N\_{i,t,j}, i=0,…,T−1i=0,\ldots,T-1, t=i+1,…,Tt=i+1,\ldots,T, j=1,…,dj=1,\ldots,d, on every atom of the σ\sigma-algebra ℱt\mathcal{F}\_{t} (see, e.g., Kallsen and Muhle-Karbe [[18](https://arxiv.org/html/2602.15177v1#bib.bib18), proof of Theorem 3.2] for such an identification). The inequality Ni,t−1,j−Ni,t,j≤Ni,i,j−∑u=i+1t−1(Ni,u−1,j−Ni,u,j)N\_{i,t-1,j}-N\_{i,t,j}\leq N\_{i,i,j}-\sum\_{u=i+1}^{t-1}(N\_{i,u-1,j}-N\_{i,u,j}) for t≥i+1t\geq i+1 has to hold for any decreasing sequence of atoms of ℱi,…,ℱt\mathcal{F}\_{i},\ldots,\mathcal{F}\_{t} (with equality for t=Tt=T). With this identification, 𝒩\mathcal{N} is a polyhedral convex cone in ℝk{\mathbb{R}}^{k} with some suitable k∈ℕk\in{\mathbb{N}}, and
the mapping N↦ηT(τ)​(N)−ηT(τ)​(0)N\mapsto\eta^{(\tau)}\_{T}(N)-\eta^{(\tau)}\_{T}(0) from 𝒩⊆ℝk\mathcal{N}\subseteq{\mathbb{R}}^{k} to ℝ|Ω|{\mathbb{R}}^{|\Omega|} is linear for τ\tau fixed. The latter follows from a decomposition of ηT(τ)​(N)\eta^{(\tau)}\_{T}(N) analogously to Kühn [[19](https://arxiv.org/html/2602.15177v1#bib.bib19), Equations (3.2)/(3.3)] that is for the linear tax rule with τt=t\tau\_{t}=t. We leave it to the reader to write this down in detail.
Since the image of a polyhedral convex cone in ℝk{\mathbb{R}}^{k} under a linear mapping is again a polyhedral convex cone (see, e.g., Rockafellar [[25](https://arxiv.org/html/2602.15177v1#bib.bib25), Theorem 19.3]), the set {ηT(τ)​(N):N∈𝒩}−{ηT(τ)​(0)}−L0​(ℱT;ℝ+)\{\eta^{(\tau)}\_{T}(N):N\in\mathcal{N}\}-\{\eta^{(\tau)}\_{T}(0)\}-L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+}) is a polyhedral convex cone and thus closed for every τ\tau. By ([3.6](https://arxiv.org/html/2602.15177v1#S3.E6 "In Proof. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")), one has
that {Vα​(x,N):N∈𝒩}−L0​(ℱT;ℝ+)=∩τ({ηT(τ)​(N):N∈𝒩}−L0​(ℱT;ℝ+))\{V^{\alpha}(x,N):N\in\mathcal{N}\}-L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+})=\cap\_{\tau}\left(\{\eta^{(\tau)}\_{T}(N):N\in\mathcal{N}\}-L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+})\right), and the intersection is closed as well.
∎

We introduce a slightly stronger no-arbitrage condition under which the set of attainable terminal wealth is closed in probability (Theorem [3.6](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem6 "Theorem 3.6. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")). For this, we need the following definition.

###### Definition 3.3 (Reaction function).

Let Ω~:=Ω×ℝ+T​(T+1)/2​d\widetilde{\Omega}:=\Omega\times{\mathbb{R}}^{T(T+1)/2d}\_{+} and

|  |  |  |
| --- | --- | --- |
|  | ℱ~t:=ℱt⊗ℬ​(ℝ+(t+1)​(t+2)/2​d)⊗{∅,ℝ+T​(T+1)/2​d−(t+1)​(t+2)/2​d},t=0,…,T−1.\displaystyle\widetilde{\mathcal{F}}\_{t}:=\mathcal{F}\_{t}\otimes\mathcal{B}({\mathbb{R}}^{(t+1)(t+2)/2d}\_{+})\otimes\{\emptyset,{\mathbb{R}}^{T(T+1)/2d-(t+1)(t+2)/2d}\_{+}\},\quad t=0,\ldots,T-1. |  |

A reaction function R=(Ri,t,j)i=0,…,T−1,t=i,…,T−1,j=1,…,dR=(R\_{i,t,j})\_{i=0,\ldots,T-1,t=i,\ldots,T-1,j=1,\ldots,d} is a mapping R:Ω~→ℝ+T​(T+1)/2​dR:\widetilde{\Omega}\to{\mathbb{R}}^{T(T+1)/2d}\_{+} such that Ri,t,jR\_{i,t,j} is ℱ~t\widetilde{\mathcal{F}}\_{t}-measurable and Ri,t,j≥Ri,t+1,jR\_{i,t,j}\geq R\_{i,t+1,j} for i=0,…,T−1,t=i,…,T−1,j=1,…,di=0,\ldots,T-1,t=i,\ldots,T-1,j=1,\ldots,d.
Given a strategy N∈𝒩N\in\mathcal{N}, it delivers the strategy NR∈𝒩N^{R}\in\mathcal{N} with

|  |  |  |
| --- | --- | --- |
|  | Ni,t,jR​(ω)=Ri,t,j​(ω,N0,0​(ω),N0,1​(ω),N1,1,N0,2​(ω),…,Nt,t​(ω),y),i≤t≤T−1,\displaystyle N^{R}\_{i,t,j}(\omega)=R\_{i,t,j}(\omega,N\_{0,0}(\omega),N\_{0,1}(\omega),N\_{1,1},N\_{0,2}(\omega),\ldots,N\_{t,t}(\omega),y),\quad i\leq t\leq T-1, |  |

and Ni,T,jR​(ω)=0N^{R}\_{i,T,j}(\omega)=0, where N0,0​(ω)N\_{0,0}(\omega), for example, denotes the vector (N0,0,1​(ω),…,N0,0,d​(ω))(N\_{0,0,1}(\omega),\ldots,N\_{0,0,d}(\omega)), and the RHS does not depend on y∈ℝ+T​(T+1)/2​d−(t+1)​(t+2)/2​dy\in{\mathbb{R}}^{T(T+1)/2d-(t+1)(t+2)/2d}\_{+} since Ri,t,jR\_{i,t,j} is ℱ~t\widetilde{\mathcal{F}}\_{t}-measurable.

Reaction functions were introduced by Witsenhausen [[29](https://arxiv.org/html/2602.15177v1#bib.bib29)] and are nowadays a standard tool in game theory.
Here, the interpretation is that Ni,t,jR​(ω)N^{R}\_{i,t,j}(\omega) may depend on the information about ω\omega at time tt and on the actions of the strategy NN up to time tt. But, it cannot be contingent on actions of NN after tt or on actions on paths that are not realized. By a slight abuse of notation, we denote the ℝ+{\mathbb{R}}\_{+}-valued random variable Ni,t,jRN^{R}\_{i,t,j} by Ri,t,j​(N)R\_{i,t,j}(N).

We recall that a set of real-valued random variables ℳ\mathcal{M} is bounded in L0L^{0} iff supX∈ℳP​(|X|>a)→0\sup\_{X\in\mathcal{M}}P(|X|>a)\to 0 as a→∞a\to\infty.

###### Definition 3.4.

The market model satisfies the no unbounded non-substitutable investment with bounded risk (NUIBR) condition iff for every initial capital x∈ℝx\in{\mathbb{R}},
there exists a reaction function RR with Vα​(x,R​(N))≥Vα​(x,N)V^{\alpha}(x,R(N))\geq V^{\alpha}(x,N) a.s. for all N∈𝒩N\in\mathcal{N} such that for all K∈ℝ+K\in{\mathbb{R}}\_{+}

|  |  |  |  |
| --- | --- | --- | --- |
|  | conv​{maxi=0,…,T−1,j=1,…,d⁡Ri,i,j​(N):N∈𝒩​with​Vα​(x,N)≥−K​a.s.}​is bounded in​L0.\displaystyle{\rm conv}\left\{\max\_{i=0,\ldots,{T-1},\ j=1,\ldots,d}R\_{i,i,j}(N)\ :\ N\in\mathcal{N}\ \mbox{with}\ V^{\alpha}(x,N)\geq-K\ \mbox{a.s.}\right\}\ \mbox{is bounded in}\ L^{0}. |  | (3.9) |

A concise interpretation of the condition is that after eliminating trades that are not strictly required from the strategies, the remaining trading volumes cannot explode if the worst-case risk of the strategies is bounded.

###### Remark 3.5.

For a detailed discussion, we first observe that NUIBR implies NA: If N∈𝒩N\in\mathcal{N} is an arbitrage, then there exists an ε>0{\varepsilon}>0 such that P​(Vα​(0,N)≥ε)≥εP(V^{\alpha}(0,N)\geq{\varepsilon})\geq{\varepsilon}. Since Vα​(0,⋅)V^{\alpha}(0,\cdot) is positive homogenous (Lemma [2.3](https://arxiv.org/html/2602.15177v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2 The model ‣ Optimal investment under capital gains taxes")(ii)) and the asset prices are finite random variables, ([3.9](https://arxiv.org/html/2602.15177v1#S3.E9 "In Definition 3.4. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) cannot hold for x=0x=0 and K=0K=0—regardless how the reaction function is chosen.

In the special case of a frictionless market, that is, α=0\alpha=0, we have that NUIBR is equivalent to NA. Namely, going back to Schachermayer [[26](https://arxiv.org/html/2602.15177v1#bib.bib26)], for each period, the ℝd{\mathbb{R}}^{d} can be decomposed into a set of null-strategies and an orthogonal complement. Redundant securities lead to a non-trivial set of null-strategies. This decomposition is generalized to short-selling constraints in the current paper (see ([3.10](https://arxiv.org/html/2602.15177v1#S3.E10 "In 3 Closedness ‣ Optimal investment under capital gains taxes"))/([3.12](https://arxiv.org/html/2602.15177v1#S3.E12 "In 3 Closedness ‣ Optimal investment under capital gains taxes"))). The orthogonal complement is replaced by a set of “purely non-reversible” trades. Then, one can choose the reaction function RR such that R​(N)R(N) realizes only the purely non-reversible part of the trades of the original strategy NN, and ([3.9](https://arxiv.org/html/2602.15177v1#S3.E9 "In Definition 3.4. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) holds under NA (see Lemma [3.10](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem10 "Lemma 3.10. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")(iii)).

By contrast, with taxes, there can be trades that are strictly required to attain a given terminal wealth, but do not directly trigger a risk—even if NA holds, see Example [3.1](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem1 "Example 3.1 (∄ optimal strategy). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes"). The condition NUIBR does not rule out these trades but limits them.

If ([3.9](https://arxiv.org/html/2602.15177v1#S3.E9 "In Definition 3.4. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) were only assumed for x=0x=0 and K=0K=0, then it would already follow from NA (by choosing R=0R=0).
The requirement that ([3.9](https://arxiv.org/html/2602.15177v1#S3.E9 "In Definition 3.4. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) holds for every K∈ℝ+K\in{\mathbb{R}}\_{+} is in the spirit of the no unbounded profit with bounded risk (NUPBR) condition since it is also based on worst‑case losses. This means, the purely algebraic NA condition is strengthened, with its topological component being the weakest possible.

###### Theorem 3.6.

If the market satisfies the NUIBR condition, the stock prices are nonnegative, and the random variables rtr\_{t}, t=1,…,Tt=1,\ldots,T, are bounded, then 𝒱α​(x):={Vα​(x,N):N∈𝒩}−L0​(ℱT;ℝ+)\mathcal{V}^{\alpha}(x):=\{V^{\alpha}(x,N)\ :\ N\in\mathcal{N}\}-L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+}) is closed with respect to the convergence in probability.

The proof of the theorem requires some preparation. As already announced in Remark [3.5](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem5 "Remark 3.5. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes"), we need a decomposition of a strategy into a reversible part and a “purely nonreversible part”.
It turns out that it is sufficient to do this decomposition period by period and on a pre-tax basis. Since we have short-selling constraints, we cannot apply orthogonal projections but we can work with the decomposition in Kühn and Molitor [[20](https://arxiv.org/html/2602.15177v1#bib.bib20)] developed for transaction costs models.

For any t∈{0,…,T−1}t\in\{0,\ldots,T-1\}, we define the (convex) cone of reversible strategies at time tt by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛt:={β∈L0​(ℱt;ℝ+d):⟨β,St+1−(1+r)​St⟩=0​ a.s.}.\displaystyle\mathcal{R}\_{t}:=\{\beta\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}\_{+}^{d})\ :\ \langle\beta,S\_{t+1}-(1+r)S\_{t}\rangle=0\text{ a.s.}\}. |  | (3.10) |

###### Lemma 3.7 (Lemma 3.3 and Lemma 3.4 in Kühn and Molitor [[20](https://arxiv.org/html/2602.15177v1#bib.bib20)]).

For every β∈L0​(ℱt;ℝ+d)\beta\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}^{d}\_{+}), there exists a unique (up to null sets) decomposition β=pt​(β)+qt​(β)\beta=p\_{t}(\beta)+q\_{t}(\beta) such that pt​(β)∈ℛtp\_{t}(\beta)\in\mathcal{R}\_{t} and qt​(β)∈L0​(ℱt;ℝ+d)q\_{t}(\beta)\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}^{d}\_{+}) satisfies
|qt​(β)|≤|β′||q\_{t}(\beta)|\leq|\beta^{\prime}| for all β′∈L0​(ℱt;ℝ+d)\beta^{\prime}\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}^{d}\_{+}) with β−β′∈ℛt\beta-\beta^{\prime}\in\mathcal{R}\_{t}. The decomposition is positive homogenous in the sense that qt​(μ​β)=μ​qt​(β)q\_{t}(\mu\beta)=\mu q\_{t}(\beta) for all μ∈L0​(ℱt;ℝ+)\mu\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}\_{+}) and β∈L0​(ℱt;ℝ+d)\beta\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}^{d}\_{+}), and it
is continuous in the sense that for all (βn)n∈ℕ⊆L0​(ℱt;ℝ+d)(\beta^{n})\_{n\in{\mathbb{N}}}\subseteq L^{0}(\mathcal{F}\_{t};{\mathbb{R}}^{d}\_{+}) and all β∈L0​(ℱt;ℝ+d)\beta\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}^{d}\_{+})

|  |  |  |  |
| --- | --- | --- | --- |
|  | βn→β​a.s. as​n→∞⟹qt​(βn)→qt​(β)​a.s. as​n→∞.\displaystyle\beta^{n}\to\beta\ \mbox{a.s. as}\ n\to\infty\quad\implies\quad q\_{t}(\beta^{n})\to q\_{t}(\beta)\ \mbox{a.s. as}\ n\to\infty. |  | (3.11) |

###### Proof.

By interpreting β\beta as “orders” in the transaction costs model and observing that ℛt\mathcal{R}\_{t} is closed in probability, we can directly apply the lemmas. We note that in the proof of [[20](https://arxiv.org/html/2602.15177v1#bib.bib20), Lemma 3.4], Equation (3.12) is neither used nor required for the subsequent arguments.
∎

Now, for each t∈{0,…,T−1}t\in\{0,\ldots,T-1\}, we can define the set of purely nonreversible strategies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒫t:={β∈L0​(ℱt;ℝ+d):qt​(β)=β},\displaystyle\mathcal{P}\_{t}:=\{\beta\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}\_{+}^{d})\ :\ q\_{t}(\beta)=\beta\}, |  | (3.12) |

which is closed in probability by ([3.11](https://arxiv.org/html/2602.15177v1#S3.E11 "In Lemma 3.7 (Lemma 3.3 and Lemma 3.4 in Kühn and Molitor [20]). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")).

For the convenience of the reader, we recall two key lemmas that are applied in the following.

###### Lemma 3.8 (Komlos’ lemma, Lemma A1.1 of [[10](https://arxiv.org/html/2602.15177v1#bib.bib10)]).

Let (fn)n∈ℕ⊆L0​(ℱt;ℝ+)(f\_{n})\_{n\in\mathbb{N}}\subseteq L^{0}(\mathcal{F}\_{t};{\mathbb{R}}\_{+}) be a sequence such that the set conv​{fn:n∈ℕ}{\rm conv}\{f\_{n}\ :\ n\in{\mathbb{N}}\} is bounded in L0L^{0}. Then, there exist a sequence (gn)n∈ℕ(g\_{n})\_{n\in\mathbb{N}} with gn∈conv​{fk:k≥n}g\_{n}\in{\rm conv}\penalty 10000\ \{f\_{k}\ :\ k\geq n\} and g∈L0​(ℱt;ℝ+)g\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}\_{+})
such that gn→gg\_{n}\to g a.s. as n→∞n\to\infty.

###### Lemma 3.9 (Lemma A.2 of [[27](https://arxiv.org/html/2602.15177v1#bib.bib27)]).

Let t∈{0,…,T}t\in\{0,\ldots,T\}. For a sequence (fn)n∈ℕ⊆L0​(ℱt;ℝ+d)(f\_{n})\_{n\in\mathbb{N}}\subseteq L^{0}(\mathcal{F}\_{t};{\mathbb{R}}^{d}\_{+}), there is a random subsequence (τk)k∈ℕ(\tau\_{k})\_{k\in\mathbb{N}}, i.e.,
a strictly increasing sequence of ℕ\mathbb{N}-valued ℱt\mathcal{F}\_{t}-measurable random variables such that the sequence of random variables (gk)k∈ℕ(g\_{k})\_{k\in\mathbb{N}} given by gk​(ω):=fτk​(ω)​(ω)g\_{k}(\omega):=f\_{\tau\_{k}(\omega)}(\omega), k∈ℕk\in\mathbb{N}, converges a.s. in the
one-point-compactification ℝ+d∪{∞}{\mathbb{R}}^{d}\_{+}\cup\{\infty\} to a random variable f∈L0​(ℱt;ℝ+d∪{∞})f\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}^{d}\_{+}\cup\{\infty\}). In fact, we may find the subsequence such that

|  |  |  |
| --- | --- | --- |
|  | |f|=lim supn→∞|fn|a.s.,\displaystyle|f|=\limsup\_{n\to\infty}|f\_{n}|\quad\text{a.s.}, |  |

where |∞|=∞|\infty|=\infty.

###### Lemma 3.10.

For every t=0,…,T−1t=0,\ldots,T-1, we define the set
𝒩t:={N∈𝒩:Ni,i=0​ for all​i<t}\mathcal{N}\_{t}:=\{N\in\mathcal{N}\ :\ N\_{i,i}=0\text{ for all}\ i<t\} and the
random variable

|  |  |  |  |
| --- | --- | --- | --- |
|  | εt:=essinf{\displaystyle{\varepsilon}\_{t}:={\rm essinf}\{ | ε​1A+∞​1Ac∈L0​(ℱt;[0,∞]):∃ε∈L0​(ℱt;[0,1])​∃A∈ℱt​∃N∈𝒩t​ with\displaystyle{\varepsilon}1\_{A}+\infty 1\_{A^{c}}\in L^{0}(\mathcal{F}\_{t};[0,\infty])\ :\ \exists{\varepsilon}\in L^{0}(\mathcal{F}\_{t};[0,1])\hskip 4.30554pt\exists A\in\mathcal{F}\_{t}\hskip 4.30554pt\exists N\in\mathcal{N}\_{t}\text{ with } |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Nt,t∈𝒫t and |Nt,t|=1A s.t. P(V0(0,N)≤−ε∣ℱt)≤ε}\displaystyle N\_{t,t}\in\mathcal{P}\_{t}\text{ and }|N\_{t,t}|=1\_{A}\text{ s.t. }P(V^{0}(0,N)\leq-{\varepsilon}\mid\mathcal{F}\_{t})\leq{\varepsilon}\} |  |

If the model satisfies NA (cf. Lemma [2.3](https://arxiv.org/html/2602.15177v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2 The model ‣ Optimal investment under capital gains taxes")(v)), we have the following results:

1. (i)

   For every t∈{0,…,T−1}t\in\{0,\ldots,T-1\} and every N∈𝒩tN\in\mathcal{N}\_{t} with Nt,t∈𝒫tN\_{t,t}\in\mathcal{P}\_{t}, we have
   P​(V0​(0,N)≤−εt​|Nt,t||ℱt)≥εtP(V^{0}(0,N)\leq-{\varepsilon}\_{t}|N\_{t,t}|\ |\ \mathcal{F}\_{t})\geq{\varepsilon}\_{t} on {|Nt,t|>0}{\{|N\_{t,t}|>0\}},
2. (ii)

   εt>0{\varepsilon}\_{t}>0 for t=0,…,T−1t=0,\ldots,T-1,
3. (iii)

   For every sequence (Nn)n⊆𝒩(N^{n})\_{n}\subseteq\mathcal{N} with lim infn→∞V0​(0,Nn)>−∞\liminf\_{n\to\infty}V^{0}(0,N^{n})>-\infty a.s., we have
     
   lim supn→∞|qt​(∑i=0tNi,tn)|<∞\limsup\_{n\to\infty}|q\_{t}(\sum\_{i=0}^{t}N^{n}\_{i,t})|<\infty a.s. for t=0,…,T−1t=0,\ldots,T-1.

###### Proof.

Ad (i)(i). Fix t∈{0,…,T−1}t\in\{0,\ldots,T-1\} and assume by contradiction that there exists N∈𝒩tN\in\mathcal{N}\_{t} with Nt,t∈𝒫tN\_{t,t}\in\mathcal{P}\_{t} such that P​(BN)>0P(B\_{N})>0 for
BN:={P​(V0​(0,N)≤−εt​|Nt,t||ℱt)<εt}∩{|Nt,t|>0}B\_{N}:=\{P(V^{0}(0,N)\leq-{\varepsilon}\_{t}|N\_{t,t}|\ |\ \mathcal{F}\_{t})<{\varepsilon}\_{t}\}\cap\{|N\_{t,t}|>0\}.
By homogeneity, we may assume |Nt,t|=1{|Nt,t|>0}|N\_{t,t}|=1\_{\{|N\_{t,t}|>0\}}.
Observe that the triplet (1,{|Nt,t|>0},N)(1,\{|N\_{t,t}|>0\},N) satisfies the conditions in the essential infimum.
Thus, we must have

|  |  |  |  |
| --- | --- | --- | --- |
|  | BN⊆{|Nt,t|>0}⊆{εt<∞}a.s\displaystyle B\_{N}\subseteq\{|N\_{t,t}|>0\}\subseteq\{{\varepsilon}\_{t}<\infty\}\quad\mbox{a.s} |  | (3.13) |

Define the random variable

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | K\displaystyle K | :=\displaystyle:= | inf{k∈ℕ: 1BN(P(−εt<V0(0,N)≤−εt+1k|ℱt)+1k)\displaystyle\inf\left\{k\in\mathbb{N}\ :\ 1\_{B\_{N}}(P(-{\varepsilon}\_{t}<V^{0}(0,N)\leq-{\varepsilon}\_{t}+\frac{1}{k}\ |\ \mathcal{F}\_{t})+\frac{1}{k})\right. |  |
|  |  |  | ≤1BNεt−P​(V0​(0,N)≤−εt|ℱt)2}.\displaystyle\qquad\qquad\qquad\left.\leq 1\_{B\_{N}}\frac{{\varepsilon}\_{t}-P(V^{0}(0,N)\leq-{\varepsilon}\_{t}\ |\ \mathcal{F}\_{t})}{2}\right\}. |  |

Since 1BN​(P​(−εt​<V0​(0,N)≤−εt+1/k|​ℱt)+1/k)1\_{B\_{N}}(P(-{\varepsilon}\_{t}<V^{0}(0,N)\leq-{\varepsilon}\_{t}+1/k\ |\ \mathcal{F}\_{t})+1/k) converges to 0 a.s. as k→∞k\to\infty, the infimum is attained (and thus finite) a.s.
We set εt′=(εt−1/K)​1BN+∞​1BNc{\varepsilon}\_{t}^{\prime}=({\varepsilon}\_{t}-1/K)1\_{B\_{N}}+\infty 1\_{B\_{N}^{c}}. Using that {K=k}∈ℱt\{K=k\}\in\mathcal{F}\_{t}, k∈ℕk\in{\mathbb{N}}, we get

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | 1BN​P​(V0​(0,N)≤−εt′|ℱt)\displaystyle 1\_{B\_{N}}P(V^{0}(0,N)\leq-{\varepsilon}\_{t}^{\prime}\ |\ \mathcal{F}\_{t}) |  |
|  |  | =\displaystyle= | 1BN​P​(V0​(0,N)≤−εt|ℱt)+1BN​P​(−εt​<V0​(0,N)≤−εt+1K|​ℱt)\displaystyle 1\_{B\_{N}}P(V^{0}(0,N)\leq-{\varepsilon}\_{t}\ |\ \mathcal{F}\_{t})+1\_{B\_{N}}P(-{\varepsilon}\_{t}<V^{0}(0,N)\leq-{\varepsilon}\_{t}+\frac{1}{K}\ |\ \mathcal{F}\_{t}) |  |
|  |  | ≤\displaystyle\leq | 1BN​εt+P​(V0​(0,N)≤−εt|ℱt)2+1BN​εt−P​(V0​(0,N)≤−εt|ℱt)2−1BN​1K\displaystyle 1\_{B\_{N}}\frac{{\varepsilon}\_{t}+P(V^{0}(0,N)\leq-{\varepsilon}\_{t}\ |\ \mathcal{F}\_{t})}{2}+1\_{B\_{N}}\frac{{\varepsilon}\_{t}-P(V^{0}(0,N)\leq-{\varepsilon}\_{t}\ |\ \mathcal{F}\_{t})}{2}-1\_{B\_{N}}\frac{1}{K} |  |
|  |  | =\displaystyle= | 1BN​εt′.\displaystyle 1\_{B\_{N}}{\varepsilon}\_{t}^{\prime}. |  |

By the minimality of εt{\varepsilon}\_{t}, this implies εt′≥εt{\varepsilon}\_{t}^{\prime}\geq{\varepsilon}\_{t}. Because of ([3.13](https://arxiv.org/html/2602.15177v1#S3.E13 "In Proof. ‣ Lemma 3.10. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) and K<∞K<\infty, we obtain a contradiction.

Ad (i​i)(ii) and (i​i​i)(iii).
First observe that for every N∈𝒩N\in\mathcal{N} the strategy defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | N^s,s:=qs​(∑i=0sNi,s)​ and ​N^s,s+1:=0​ for ​s=0,…,T−1,\displaystyle\widehat{N}\_{s,s}:=q\_{s}\left(\sum\_{i=0}^{s}N\_{i,s}\right)\text{ and }\widehat{N}\_{s,s+1}:=0\text{ for }s=0,\ldots,T-1, |  | (3.14) |

satisfies V0​(x,N)=V0​(x,N^)V^{0}(x,N)=V^{0}(x,\widehat{N}) for all x∈ℝx\in{\mathbb{R}}.
Let us prove (i​i)(ii) and the assertion (i​i​i)(iii) with 𝒩t\mathcal{N}\_{t} instead of 𝒩\mathcal{N} by a joint backwards induction
on t=T−1,…,0t=T-1,\ldots,0. The case t=T−1t=T-1 is a special case of the induction step.
  
Suppose we have already shown that εs>0{\varepsilon}\_{s}>0
for all s=t+1,…,T−1s=t+1,\ldots,T-1 and that we have shown (i​i​i)(iii) for all sequences (Nn)n⊆𝒩t+1(N^{n})\_{n}\subseteq\mathcal{N}\_{t+1} with lim infn→∞V0​(0,Nn)>−∞\liminf\_{n\to\infty}V^{0}(0,N^{n})>-\infty. Now let us prove that εt>0{\varepsilon}\_{t}>0. It is easy to see that εt{\varepsilon}\_{t} is defined over a minimum-stable set.
Thus, there exists a sequence
(εn,An,Nn)n∈ℕ⊆L0​(ℱt;[0,1])×ℱt×𝒩t({\varepsilon}\_{n},A\_{n},N^{n})\_{n\in{\mathbb{N}}}\subseteq L^{0}(\mathcal{F}\_{t};[0,1])\times\mathcal{F}\_{t}\times\mathcal{N}\_{t} with Nt,tn∈𝒫t,|Nt,tn|=1An↑1{εt<∞}N^{n}\_{t,t}\in\mathcal{P}\_{t},|N^{n}\_{t,t}|=1\_{A\_{n}}\uparrow 1\_{\{{\varepsilon}\_{t}<\infty\}},
εn​1An+∞​1Anc↓εt{\varepsilon}\_{n}1\_{A\_{n}}+\infty 1\_{A^{c}\_{n}}\downarrow{\varepsilon}\_{t} a.s.
and P​(V0​(0,Nn)≤−εn|ℱt)≤εnP(V^{0}(0,N^{n})\leq-{\varepsilon}\_{n}\ |\ \mathcal{F}\_{t})\leq{\varepsilon}\_{n} for all n∈ℕn\in{\mathbb{N}}.
Thus

|  |  |  |
| --- | --- | --- |
|  | P​({V0​(0,Nn)≤−εn}∩Bt|ℱt)≤εn​1Bt, where ​Bt:={εt=0}.\displaystyle P(\{V^{0}(0,N^{n})\leq-{\varepsilon}\_{n}\}\cap B\_{t}\ |\ \mathcal{F}\_{t})\leq{\varepsilon}\_{n}1\_{B\_{t}},\mbox{\ where }B\_{t}:=\{{\varepsilon}\_{t}=0\}. |  |

In particular, by defining μn:=(V0​(0,Nn​1Bt))+\mu\_{n}:=(V^{0}(0,N^{n}1\_{B\_{t}}))^{+}, we get V0​(0,Nn​1Bt)−μn→0V^{0}(0,N^{n}1\_{B\_{t}})-\mu\_{n}\to 0 in probability. We transform each NnN^{n} according to ([3.14](https://arxiv.org/html/2602.15177v1#S3.E14 "In Proof. ‣ Lemma 3.10. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) into N^n\widehat{N}^{n} and obtain a.s.-convergence by passing to a subsequence.

Since |N^t,tn​1Bt|=|Nt,tn​1Bt|=1Bt∩An↑1Bt|\widehat{N}\_{t,t}^{n}1\_{B\_{t}}|=|N^{n}\_{t,t}1\_{B\_{t}}|=1\_{B\_{t}\cap A\_{n}}\uparrow 1\_{B\_{t}}, we can apply Lemma [3.9](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem9 "Lemma 3.9 (Lemma A.2 of [27]). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes") to obtain a measurable subsequence (τk)k(\tau\_{k})\_{k} such that N^t,tτk​1Bt\widehat{N}^{\tau\_{k}}\_{t,t}1\_{B\_{t}} converges to some β∈L0​(ℱt;ℝ+d)\beta\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}\_{+}^{d}) with |β|=1Bt|\beta|=1\_{B\_{t}}. Now define the strategies N(1)∈𝒩tN^{(1)}\in\mathcal{N}\_{t} via Nt,t(1)=βN^{(1)}\_{t,t}=\beta and Ni,u(1)=0N^{(1)}\_{i,u}=0 for (i,u)≠(t,t)(i,u)\neq(t,t) and

|  |  |  |
| --- | --- | --- |
|  | Ni,u(2),n:={N^i,un if ​t+1≤i≤u0 otherwise\displaystyle{N}^{(2),n}\_{i,u}:=\left\{\begin{array}[]{ll}\widehat{N}^{n}\_{i,u}&\text{ if }t+1\leq i\leq u\\ 0&\text{ otherwise}\end{array}\right. |  |

Then by linearity of N↦V0​(0,N)N\mapsto V^{0}(0,N), we have V0​(0,N(2),τk​1Bt)−1Bt​μτk→−V0​(0,N(1)​1Bt)​ a.s.V^{0}(0,{N}^{(2),\tau\_{k}}1\_{B\_{t}})-1\_{B\_{t}}{\mu}\_{\tau\_{k}}\to-V^{0}(0,N^{(1)}1\_{B\_{t}})\text{ a.s.}
Using the induction hypotheses (i​i​i)(iii) on (N(2),τk​1Bt)k⊆𝒩t+1({N}^{(2),\tau\_{k}}1\_{B\_{t}})\_{k}\subseteq\mathcal{N}\_{t+1} in combination with Lemma [3.8](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem8 "Lemma 3.8 (Komlos’ lemma, Lemma A1.1 of [10]). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes") we can deduce the existence of N(2)∈𝒩t+1{N}^{(2)}\in\mathcal{N}\_{t+1} and μ∈L0​(ℱT;ℝ+){\mu}\in L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+}) such that
V0​(0,N(2)​1Bt)−μ​1Bt=−V0​(0,N(1)​1Bt)V^{0}(0,{N}^{(2)}1\_{B\_{t}})-{\mu}1\_{B\_{t}}=-V^{0}(0,{N}^{(1)}1\_{B\_{t}}).
Since 𝒫t\mathcal{P}\_{t} is closed in probability (Lemma [3.7](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem7 "Lemma 3.7 (Lemma 3.3 and Lemma 3.4 in Kühn and Molitor [20]). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) and |Nt,t(1)​1Bt|=1|N^{(1)}\_{t,t}1\_{B\_{t}}|=1 on BtB\_{t}, we know that Nt,t(1)​1Bt∈𝒫tN^{(1)}\_{t,t}1\_{B\_{t}}\in\mathcal{P}\_{t} and P​(V0​(0,N(1)​1Bt)≠0|ℱt)>0P(V^{0}(0,N^{(1)}1\_{B\_{t}})\neq 0\ |\ \mathcal{F}\_{t})>0 on BtB\_{t}. Now assume by contradiction that P​(Bt)>0P(B\_{t})>0. Then, P​(V0​(0,N(1)​1Bt)≠0)>0P(V^{0}(0,N^{(1)}1\_{B\_{t}})\neq 0)>0.
If P​(V0​(0,N(1)​1Bt)<0)=0P(V^{0}(0,N^{(1)}1\_{B\_{t}})<0)=0, then N(1)​1BtN^{(1)}1\_{B\_{t}} is an arbitrage, otherwise, if P​(V0​(0,N(1)​1Bt)<0)>0P(V^{0}(0,N^{(1)}1\_{B\_{t}})<0)>0, then N(2)​1{V0​(N(1)​1Bt)<0}N^{(2)}1\_{\{V^{0}(N^{(1)}1\_{B\_{t}})<0\}} is an arbitrage, since {V0​(0,N(1)​1Bt)<0}∈ℱt+1\{V^{0}(0,N^{(1)}1\_{B\_{t}})<0\}\in\mathcal{F}\_{t+1}.
This contradicts NA, and thus {εt=0}\{{\varepsilon}\_{t}=0\} must be a null set.

Under the induction hypothesis and given that (i​i)(ii) holds for tt, we now establish (i​i​i)(iii) for all sequences (Nn)n⊆𝒩t(N^{n})\_{n}\subseteq\mathcal{N}\_{t} with lim infn→∞V0​(0,Nn)>−∞\liminf\_{n\to\infty}V^{0}(0,N^{n})>-\infty a.s. Let (Nn)n⊆𝒩t(N^{n})\_{n}\subseteq\mathcal{N}\_{t} and define for each nn the corresponding strategy N^n\widehat{N}^{n} given by the transformation ([3.14](https://arxiv.org/html/2602.15177v1#S3.E14 "In Proof. ‣ Lemma 3.10. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")).
Define the set At:={lim supn→∞|N^t,tn|=∞}A\_{t}:=\{\limsup\_{n\to\infty}|\widehat{N}\_{t,t}^{n}|=\infty\}
and suppose that P​(At)>0P(A\_{t})>0.
Define a measurable subsequence by τ0:=0\tau\_{0}:=0 and τk:=min⁡{n>τk−1:1At​|N^t,tn|≥1At​k}\tau\_{k}:=\min\{n>\tau\_{k-1}:1\_{A\_{t}}|\widehat{N}^{n}\_{t,t}|\geq 1\_{A\_{t}}k\}.
Now observe that by εt>0{\varepsilon}\_{t}>0, the sequence
(infn≥kV0​(0,N^τn)+εt​|N^t,tτk|)k∈ℕ(\inf\_{n\geq k}V^{0}(0,\widehat{N}^{\tau\_{n}})+{\varepsilon}\_{t}|\widehat{N}\_{t,t}^{\tau\_{k}}|)\_{k\in\mathbb{N}} converges a.s. to ∞\infty on AtA\_{t} as k→∞k\to\infty, which implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | limk→∞P​({V0​(0,N^τk)+εt​|N^t,tτk|≤0}∩At)=0.\displaystyle\lim\_{k\to\infty}P(\{V^{0}(0,\widehat{N}^{\tau\_{k}})+{\varepsilon}\_{t}|\widehat{N}^{\tau\_{k}}\_{t,t}|\leq 0\}\cap A\_{t})=0. |  | (3.16) |

On the other hand, our assumption P​(At)>0P(A\_{t})>0 together with (i)(i) and (i​i)(ii) yield

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[P​({V0​(0,N^τk)+εt​|N^t,tτk|≤0}∩At|ℱt)]≥𝔼​[εt​1At]>0∀k∈ℕ\displaystyle\mathbb{E}[P(\{V^{0}(0,\widehat{N}^{\tau\_{k}})+{\varepsilon}\_{t}|\widehat{N}\_{t,t}^{\tau\_{k}}|\leq 0\}\cap A\_{t}\ |\ \mathcal{F}\_{t})]\geq\mathbb{E}[{\varepsilon}\_{t}1\_{A\_{t}}]>0\quad\forall k\in\mathbb{N} |  |

which contradicts ([3.16](https://arxiv.org/html/2602.15177v1#S3.E16 "In Proof. ‣ Lemma 3.10. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")).
Therefore,
lim supn→∞|N^t,tn|<∞\limsup\_{n\to\infty}|\widehat{N}\_{t,t}^{n}|<\infty a.s.
Now consider the sequence N^(2),n⊆𝒩t+1\widehat{N}^{(2),n}\subseteq\mathcal{N}\_{t+1} defined by

|  |  |  |
| --- | --- | --- |
|  | N^i,u(2),n:={N^i,unfor ​1≤t+1≤i≤u0otherwise\displaystyle\widehat{N}^{(2),n}\_{i,u}:=\left\{\begin{array}[]{ll}\widehat{N}^{n}\_{i,u}&\text{for }1\leq t+1\leq i\leq u\\ 0&\text{otherwise}\end{array}\right. |  |

Since lim supn→∞|N^t,tn|<∞\limsup\_{n\to\infty}|\widehat{N}\_{t,t}^{n}|<\infty and lim infn→∞V0​(0,N^n)>−∞\liminf\_{n\to\infty}V^{0}(0,\widehat{N}^{n})>-\infty a.s., the linearity of the mapping N↦V0​(0,N)N\mapsto V^{0}(0,N) implies that lim infn→∞V0​(0,N^(2),n)>−∞\liminf\_{n\to\infty}V^{0}(0,\widehat{N}^{(2),n})>-\infty a.s. as well. Applying the induction hypothesis to (N^(2),n)n∈ℕ(\widehat{N}^{(2),n})\_{n\in{\mathbb{N}}} shows that lim supn→∞|N^i,in|<∞\limsup\_{n\to\infty}|\widehat{N}^{n}\_{i,i}|<\infty for i=t,t+1,…,T−1i=t,t+1,\ldots,T-1 which completes the proof.
∎

###### Lemma 3.11.

For every strategy N∈𝒩N\in\mathcal{N} there exists a strategy N~∈𝒩\widetilde{N}\in\mathcal{N} that realizes losses in the sense that

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Sij>Stj}⊆{N~i,t,j=0}a.s.,i=0,…,T−1,t=i+1,…,T,j=1,…,d,\displaystyle\{S^{j}\_{i}>S^{j}\_{t}\}\subseteq\{\widetilde{N}\_{i,t,j}=0\}\quad\mbox{a.s.},\quad i=0,\ldots,T-1,t=i+1,\ldots,T,j=1,\ldots,d, |  | (3.18) |

with the property Vα​(x,N)≤Vα​(x,N~)V^{\alpha}(x,N)\leq V^{\alpha}(x,\widetilde{N}) a.s. for all x∈ℝx\in{\mathbb{R}}.

###### Proof.

Let x∈ℝx\in{\mathbb{R}} and N∈𝒩N\in\mathcal{N}. We recursively modify the strategy period by period to include wash sales when it does not realize losses. Define N(0):=NN^{(0)}:=N and given N(u−1)∈𝒩N^{(u-1)}\in\mathcal{N}, define N(u)∈𝒩N^{(u)}\in\mathcal{N}, u=1,…,T−1u=1,\ldots,T-1, by

|  |  |  |
| --- | --- | --- |
|  | Ni,t,j(u):={Ni,t,j(u−1) if ​i≤t<u​ or ​u<i≤t1{Suj≥Sij}​Ni,t,j(u−1) if ​i<u≤tNu,t,j(u−1)+∑s=0u−11{Suj<Ssj}​Ns,t,j(u−1) if ​i=u≤t\displaystyle N^{(u)}\_{i,t,j}:=\left\{\begin{array}[]{ll}N^{(u-1)}\_{i,t,j}&\text{ if }i\leq t<u\text{ or }u<i\leq t\\ 1\_{\{S\_{u}^{j}\geq S\_{i}^{j}\}}N^{(u-1)}\_{i,t,j}&\text{ if }i<u\leq t\\ N^{(u-1)}\_{u,t,j}+\sum\_{s=0}^{u-1}1\_{\{S\_{u}^{j}<S\_{s}^{j}\}}N^{(u-1)}\_{s,t,j}&\text{ if }i=u\leq t\end{array}\right. |  |

It is straightforward to verify that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑s=1t∑i=0s−1⟨Ni,s−1(u−1)−Ni,s(u−1),Ss−Si⟩≥∑s=1t∑i=0s−1⟨Ni,s−1(u)−Ni,s(u),Ss−Si⟩,t=1,…,T.\displaystyle\sum\_{s=1}^{t}\sum\_{i=0}^{s-1}\langle N^{(u-1)}\_{i,s-1}-N^{(u-1)}\_{i,s},S\_{s}-S\_{i}\rangle\geq\sum\_{s=1}^{t}\sum\_{i=0}^{s-1}\langle N^{(u)}\_{i,s-1}-N^{(u)}\_{i,s},S\_{s}-S\_{i}\rangle,\quad t=1,\ldots,T. |  | (3.20) |

Let us prove by induction on t=0,…,Tt=0,\ldots,T that ηt​(N(u−1))≤ηt​(N(u))\eta\_{t}(N^{(u-1)})\leq\eta\_{t}(N^{(u)}). The base case t=0t=0 holds by η0​(N(u−1))=x−⟨N0,0(u−1),S0⟩=x−⟨N0,0(u),S0⟩=η0​(N(u))\eta\_{0}(N^{(u-1)})=x-\langle N\_{0,0}^{(u-1)},S\_{0}\rangle=x-\langle N\_{0,0}^{(u)},S\_{0}\rangle=\eta\_{0}(N^{(u)}). Suppose that we have shown ηs​(N(u−1))≤ηs​(N(u))\eta\_{s}(N^{(u-1)})\leq\eta\_{s}(N^{(u)}) for every s<ts<t. We want to prove that ηt​(N(u−1))≤ηt​(N(u))\eta\_{t}(N^{(u-1)})\leq\eta\_{t}(N^{(u)}) holds.
Since ∑i=0sNi,s(u−1)=∑i=0sNi,s(u)\sum\_{i=0}^{s}N^{(u-1)}\_{i,s}=\sum\_{i=0}^{s}N^{(u)}\_{i,s} for s=0,…,Ts=0,\ldots,T, we derive from the self-financing condition ([2.3](https://arxiv.org/html/2602.15177v1#S2.E3 "In 2 The model ‣ Optimal investment under capital gains taxes")) and the induction hypothesis for s=t−1s=t-1 that on the set {Πt​(N(u))=Πt−1​(N(u))}\{\Pi\_{t}(N^{(u)})=\Pi\_{t-1}(N^{(u)})\} it holds that ηt​(N(u−1))≤ηt​(N(u))\eta\_{t}(N^{(u-1)})\leq\eta\_{t}(N^{(u)}).

By ηt=x+∑s=0t(rs​ηs−1​1(s≥1)+⟨∑i=0s−1(Ni,s−1−Ni,s)−Ns,s,Ss⟩)−Πt\eta\_{t}=x+\sum\_{s=0}^{t}(r\_{s}\eta\_{s-1}1\_{(s\geq 1)}+\langle\sum\_{i=0}^{s-1}(N\_{i,s-1}-N\_{i,s})-N\_{s,s},S\_{s}\rangle)-\Pi\_{t} and ∑i=0sNi,s(u−1)=∑i=0sNi,s(u)\sum\_{i=0}^{s}N^{(u-1)}\_{i,s}=\sum\_{i=0}^{s}N^{(u)}\_{i,s} for s=0,…,Ts=0,\ldots,T, we get

|  |  |  |
| --- | --- | --- |
|  | ηt​(N(u))−ηt​(N(u−1))=∑s=1trs​(ηs−1​(N(u))−ηs−1​(N(u−1)))−Πt​(N(u))+Πt​(N(u−1)).\displaystyle\eta\_{t}(N^{(u)})-\eta\_{t}(N^{(u-1)})=\sum\_{s=1}^{t}r\_{s}(\eta\_{s-1}(N^{(u)})-\eta\_{s-1}(N^{(u-1)}))-\Pi\_{t}(N^{(u)})+\Pi\_{t}(N^{(u-1)}). |  |

On the set {Πt​(N(u))>Πt−1​(N(u))}\{\Pi\_{t}(N^{(u)})>\Pi\_{t-1}(N^{(u)})\}, we have Πt​(N(u))=α​Gt​(N(u))\Pi\_{t}(N^{(u)})=\alpha G\_{t}(N^{(u)}). Since α​Gt​(N(u−1))≤Πt​(N(u−1))\alpha G\_{t}(N^{(u-1)})\leq\Pi\_{t}(N^{(u-1)}), it follows from ([3.20](https://arxiv.org/html/2602.15177v1#S3.E20 "In Proof. ‣ Lemma 3.11. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) that

|  |  |  |
| --- | --- | --- |
|  | ηt​(N(u))−ηt​(N(u−1))≥∑s=1t(1−α)​rs​(ηs−1​(N(u))−ηs−1​(N(u−1)))≥0,\displaystyle\eta\_{t}(N^{(u)})-\eta\_{t}(N^{(u-1)})\geq\sum\_{s=1}^{t}(1-\alpha)r\_{s}(\eta\_{s-1}(N^{(u)})-\eta\_{s-1}(N^{(u-1)}))\geq 0, |  |

where for the second inequality we use the induction hypothesis for all s<ts<t and r≥0r\geq 0. We conclude that Vα​(x,N)≤Vα​(x,N(1))≤…≤Vα​(x,N(T−1))V^{\alpha}(x,N)\leq V^{\alpha}(x,N^{(1)})\leq\ldots\leq V^{\alpha}(x,N^{(T-1)}). Since N(T−1)N^{(T-1)} satisfies ([3.18](https://arxiv.org/html/2602.15177v1#S3.E18 "In Lemma 3.11. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) by construction, we are done.
∎

###### Lemma 3.12.

Suppose that the stock prices are nonnegative and there exists r¯∈ℝ+\overline{r}\in{\mathbb{R}}\_{+} such that maxt=1,…,T⁡rt≤r¯\max\_{t=1,\ldots,T}r\_{t}\leq\overline{r} a.s.
For x∈ℝx\in{\mathbb{R}} and N∈𝒩N\in\mathcal{N}, we define

|  |  |  |
| --- | --- | --- |
|  | Lt​(N):=((−x)∨0+∑s=0t−1⟨qs​(∑i=0sNi,s),Ss⟩)​(1+r¯)T,t=0,…,T.\displaystyle L\_{t}(N):=\left((-x)\vee 0+\sum\_{s=0}^{t-1}\left\langle q\_{s}\left(\sum\_{i=0}^{s}N\_{i,s}\right),S\_{s}\right\rangle\right)(1+\overline{r})^{T},\quad t=0,\ldots,T. |  |

with the usual convention ∑s=0−1…:=0\sum\_{s=0}^{-1}\ldots:=0. For a strategy N∈𝒩N\in\mathcal{N} and a {0,…,T}\{0,\ldots,T\}-valued stopping time τ\tau, we define the stopped strategy by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ni,t(τ):=Ni,t​1{τ>t},i=0,…,T−1,t=i,…,T.\displaystyle N^{(\tau)}\_{i,t}:=N\_{i,t}1\_{\{\tau>t\}},\quad i=0,\ldots,T-1,\ t=i,\ldots,T. |  | (3.21) |

The following statements hold:

1. (i)

   Lt​(N(τ))=Lt∧τ​(N)L\_{t}(N^{(\tau)})=L\_{t\wedge\tau}(N), t=0,…,Tt=0,\ldots,T
2. (ii)

   For every N∈𝒩N\in\mathcal{N} that realizes losses in the sense of ([3.18](https://arxiv.org/html/2602.15177v1#S3.E18 "In Lemma 3.11. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")), we have Vα​(x,N)≥−LT​(N)V^{\alpha}(x,N)\geq-L\_{T}(N).

The random variable Lt​(N)L\_{t}(N) can be interpreted as an ℱt−1\mathcal{F}\_{t-1}-measurable upper bound for losses if stocks are liquidated at time tt after the strategy NN has been followed. Since it is known one step in advance, it allows to control maximal losses.

###### Proof.

(i)(i) Follows from qs​(0)=0q\_{s}(0)=0 (Lemma [3.7](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem7 "Lemma 3.7 (Lemma 3.3 and Lemma 3.4 in Kühn and Molitor [20]). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")).

(i​i)(ii) Let N∈𝒩N\in\mathcal{N} satisfy ([3.18](https://arxiv.org/html/2602.15177v1#S3.E18 "In Lemma 3.11. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")).
The accumulated realized gains of the stocks can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | ∑s=1t∑u=0s−1⟨Nu,s−1−Nu,s,Ss−Su⟩=∑u=1t⟨Su−Su−1,∑i=0u−1Ni,u−1⟩−∑i=0t⟨Ni,t,St−minu=i,…,t⁡Su⟩.\displaystyle\sum\_{s=1}^{t}\sum\_{u=0}^{s-1}\langle N\_{u,s-1}-N\_{u,s},S\_{s}-S\_{u}\rangle=\sum\_{u=1}^{t}\langle S\_{u}-S\_{u-1},\sum\_{i=0}^{u-1}N\_{i,u-1}\rangle-\sum\_{i=0}^{t}\langle N\_{i,t},S\_{t}-\min\_{u=i,\ldots,t}S\_{u}\rangle. |  |

We define the strategy N^\widehat{N} by N^t,t:=∑i=0tNi,t\widehat{N}\_{t,t}:=\sum\_{i=0}^{t}N\_{i,t}, N^t,t+1=0\widehat{N}\_{t,t+1}=0 and obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑s=1t∑u=0s−1⟨Nu,s−1−Nu,s,Ss−Su⟩≤∑s=1t∑u=0s−1⟨N^u,s−1−N^u,s,Ss−Su⟩,t=1,…,T.\displaystyle\sum\_{s=1}^{t}\sum\_{u=0}^{s-1}\langle N\_{u,s-1}-N\_{u,s},S\_{s}-S\_{u}\rangle\leq\sum\_{s=1}^{t}\sum\_{u=0}^{s-1}\langle\widehat{N}\_{u,s-1}-\widehat{N}\_{u,s},S\_{s}-S\_{u}\rangle,\quad t=1,\ldots,T. |  | (3.22) |

By repeating the arguments in the proof of Lemma [3.11](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem11 "Lemma 3.11. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes"), ([3.22](https://arxiv.org/html/2602.15177v1#S3.E22 "In Proof. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) yields that Vα​(x,N)≥Vα​(x,N^)V^{\alpha}(x,N)\geq V^{\alpha}(x,\widehat{N}). Therefore, we can and do assume w.l.o.g. that
Nt,t+1=0N\_{t,t+1}=0 for all t=0,…,T−1t=0,\ldots,T-1. Since now NN immediately realizes its gains and losses, it is possible to define a meaningful one dimensional wealth process (Vt)t=0,…,T(V\_{t})\_{t=0,\ldots,T} by the recursion V0=x{V}\_{0}=x and

|  |  |  |
| --- | --- | --- |
|  | Vt=(1+rt)​Vt−1+⟨Nt−1,t−1,St−(1+rt)​St−1⟩\displaystyle{V}\_{t}=(1+r\_{t}){V}\_{t-1}+\langle{N}\_{t-1,t-1},S\_{t}-(1+r\_{t})S\_{t-1}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | −α​[(1+rt)​Vt−1+⟨Nt−1,t−1,St−(1+rt)​St−1⟩−Vt−1⋆]+,t≥1,\displaystyle\qquad\ -\alpha\left[(1+r\_{t}){V}\_{t-1}+\langle{N}\_{t-1,t-1},S\_{t}-(1+r\_{t})S\_{t-1}\rangle-{V}^{\star}\_{t-1}\right]^{+},\quad t\geq 1, |  | (3.23) |

where Vt−1⋆:=maxs=0,…,t−1⁡Vs{V}^{\star}\_{t-1}:=\max\_{s=0,\ldots,t-1}{V}\_{s}. It is straightforward to check that VT=Vα​(x,N){V}\_{T}=V^{\alpha}(x,{N}). In addition, one has V0≥x∧0V\_{0}\geq x\wedge 0 and by S≥0S\geq 0,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vt≥\displaystyle{V}\_{t}\geq | min⁡{Vt−1⋆,(1+rt)​Vt−1+⟨Nt−1,t−1,St−(1+rt)​St−1⟩}\displaystyle\min\{{V}^{\star}\_{t-1},(1+r\_{t}){V}\_{t-1}+\langle{N}\_{t-1,t-1},S\_{t}-(1+r\_{t})S\_{t-1}\rangle\} |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | min⁡{Vt−1⋆,(1+rt)​Vt−1+⟨qt−1​(Nt−1,t−1),St−(1+rt)​St−1⟩}\displaystyle\min\{{V}^{\star}\_{t-1},(1+r\_{t}){V}\_{t-1}+\langle q\_{t-1}({N}\_{t-1,t-1}),S\_{t}-(1+r\_{t})S\_{t-1}\rangle\} |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≥\displaystyle\geq | min⁡{x∧0,(1+rt)​[Vt−1−⟨qt−1​(Nt−1,t−1),St−1⟩]},t=1,…,T.\displaystyle\min\{x\wedge 0,(1+r\_{t})\left[{V}\_{t-1}-\langle q\_{t-1}({N}\_{t-1,t-1}),S\_{t-1}\rangle\right]\},\quad t=1,\ldots,T. |  |  |

By 0≤maxt=1,…,T⁡rt≤r¯0\leq\max\_{t=1,\ldots,T}r\_{t}\leq\overline{r} and ⟨qt−1​(Nt−1,t−1),St−1⟩≥0\langle q\_{t-1}({N}\_{t-1,t-1}),S\_{t-1}\rangle\geq 0 for t=1,…,Tt=1,\ldots,T, this recursive bound gives us (i​i)(ii).
∎

We are now ready to prove Theorem [3.6](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem6 "Theorem 3.6. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes").

###### Proof of Theorem [3.6](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem6 "Theorem 3.6. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes").

Suppose that the market satisfies NUIBR, the stock prices are nonnegative, and the interest rates are bounded. We note that NUIBR implies NA (Remark [3.5](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem5 "Remark 3.5. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")), and we can apply Lemma [3.10](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem10 "Lemma 3.10. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes").

Fix x∈ℝx\in{\mathbb{R}} and let RR be a reaction function such that ([3.9](https://arxiv.org/html/2602.15177v1#S3.E9 "In Definition 3.4. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) holds for all K∈ℝ+K\in{\mathbb{R}}\_{+}.
To simplify the notation we define |N|𝒩:=maxt=0,…,T−1,j=1,…,d⁡Nt,t,j|N|\_{\mathcal{N}}:=\max\_{t=0,\ldots,T-1,j=1,\ldots,d}N\_{t,t,j} and for each K∈ℝ+K\in{\mathbb{R}}\_{+} we define the set 𝒞R,K:=conv{|R(N)|𝒩:N∈𝒩withVα(x,N)≥−Ka.s.}\mathcal{C}\_{R,K}:=\mbox{conv}\{|R(N)|\_{\mathcal{N}}\ :\ N\in\mathcal{N}\ \mbox{with}\ V^{\alpha}(x,N)\geq-K\ \mbox{a.s.}\}.

Let (Nn,μn)n∈ℕ⊆𝒩×L0​(ℱT;ℝ+)(N^{n},\mu\_{n})\_{n\in{\mathbb{N}}}\subseteq\mathcal{N}\times L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+}) be a sequence such that Vα​(x,Nn)−μn→fV^{\alpha}(x,N^{n})-\mu\_{n}\to f in probability. By passing to a subsequence we can and do assume a.s.-convergence. By Lemma [3.11](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem11 "Lemma 3.11. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes"), we may further assume that for every n∈ℕn\in\mathbb{N}, the strategy NnN^{n} realizes losses in the sense of ([3.18](https://arxiv.org/html/2602.15177v1#S3.E18 "In Lemma 3.11. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")).

We know from Lemma [2.3](https://arxiv.org/html/2602.15177v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2 The model ‣ Optimal investment under capital gains taxes")(iii) and Lemma [3.12](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem12 "Lemma 3.12. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")(ii) that V0​(x,Nn)≥Vα​(x,Nn)≥−LT​(Nn)V^{0}(x,N^{n})\geq V^{\alpha}(x,N^{n})\geq-L\_{T}(N^{n}) for all n∈ℕn\in\mathbb{N}.
Since lim infn→∞V0​(0,Nn)≥f−V0​(x,0)>−∞\liminf\_{n\to\infty}V^{0}(0,N^{n})\geq f-V^{0}(x,0)>-\infty a.s., Lemma [3.10](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem10 "Lemma 3.10. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")(iii) guarantees that Lt:=supn∈ℕLt​(Nn)<∞L\_{t}:=\sup\_{n\in\mathbb{N}}L\_{t}(N^{n})<\infty a.s. for t=0,…,Tt=0,\ldots,T. Note that LtL\_{t} is nondecreasing in tt. For every k∈ℕk\in{\mathbb{N}} choose Mk∈[(−x)∨0,∞)M\_{k}\in[(-x)\vee 0,\infty) such that P​(LT>Mk)≤1/k2P(L\_{T}>M\_{k})\leq 1/k^{2} and define the stopping times τk:=inf{t∈{0,…,T−1}:Lt+1>Mk}∧T\tau\_{k}:=\inf\{t\in\{0,\ldots,T-1\}:L\_{t+1}>M\_{k}\}\wedge T. For every n∈ℕn\in\mathbb{N}, we define the stopped strategies Nn,k:=(Nn)(τk)N^{n,k}:=(N^{n})^{(\tau\_{k})} according to ([3.21](https://arxiv.org/html/2602.15177v1#S3.E21 "In Lemma 3.12. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")). Now,
Lemma [3.12](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem12 "Lemma 3.12. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes") guarantees that for all n,k∈ℕn,k\in\mathbb{N} we have Vα​(x,Nn,k)≥−MkV^{\alpha}(x,N^{n,k})\geq-M\_{k}.
Since P​(Vα​(x,Nn)≠Vα​(x,Nn,n))≤P​(LT>Mn)≤1/n2P(V^{\alpha}(x,N^{n})\not=V^{\alpha}(x,N^{n,n}))\leq P(L\_{T}>M\_{n})\leq 1/n^{2}, we know by the convergence of Vα​(x,Nn)−μnV^{\alpha}(x,N^{n})-\mu\_{n} and the Borel-Cantelli lemma that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vα​(x,Nn,n)−μn→fa.s.as ​n→∞.\displaystyle V^{\alpha}(x,N^{n,n})-\mu\_{n}\to f\quad\mbox{a.s.}\quad\mbox{as }n\to\infty. |  | (3.24) |

Let us prove that conv{|R(Nl,l)|𝒩:l∈ℕ}\mbox{conv}\{|R(N^{l,l})|\_{\mathcal{N}}\ :\ l\in\mathbb{N}\} is bounded in L0L^{0}. Fix ε>0{\varepsilon}>0 and choose k∈ℕk\in\mathbb{N} such that 1/k2≤ε/21/k^{2}\leq{\varepsilon}/2.
Since 𝒞R,Mk\mathcal{C}\_{R,M\_{k}} is bounded in L0L^{0}, there exists Cε/2>0C\_{{\varepsilon}/2}>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supX∈𝒞R,MkP​(X>Cε/2)≤ε2.\displaystyle\sup\_{X\in\mathcal{C}\_{R,M\_{k}}}P(X>C\_{{\varepsilon}/2})\leq\frac{{\varepsilon}}{2}. |  | (3.25) |

For l≥kl\geq k, we have Nl,l=Nl,kN^{l,l}=N^{l,k} on the set {LT≤Mk}\{L\_{T}\leq M\_{k}\}, and thus the definition of R​(Nl,l)R(N^{l,l}) guarantees that
R​(Nl,l)=R​(Nl,k)R(N^{l,l})=R(N^{l,k}). Let ∑l=1mλl|R(Nl,l)|𝒩∈conv{|R(Nl,l)|𝒩:l∈ℕ}\sum\_{l=1}^{m}\lambda\_{l}|R(N^{l,l})|\_{\mathcal{N}}\in\mbox{conv}\{|R(N^{l,l})|\_{\mathcal{N}}\ :\ l\in\mathbb{N}\}. We get

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  | P​(∑l=1mλl​|R​(Nl,l)|𝒩>Cε/2)\displaystyle P(\sum\_{l=1}^{m}\lambda\_{l}|R(N^{l,l})|\_{\mathcal{N}}>C\_{{\varepsilon}/2}) |  | (3.26) |
|  |  | ≤\displaystyle\leq | P​(LT>Mk)+P​({LT≤Mk}∩{∑l=1mλl|R​(Nl,l)|𝒩>Cε/2})\displaystyle P(L\_{T}>M\_{k})+P(\{L\_{T}\leq M\_{k}\}\cap\{\sum\_{l=1}^{m}\lambda\_{l}|R(N^{l,l})|\_{\mathcal{N}}>C\_{{\varepsilon}/2}\}) |  |
|  |  | ≤\displaystyle\leq | 1k2+P​({LT≤Mk}∩{∑l=1mλl|R​(Nl,l)|𝒩>Cε/2})\displaystyle\frac{1}{k^{2}}+P(\{L\_{T}\leq M\_{k}\}\cap\{\sum\_{l=1}^{m}\lambda\_{l}|R(N^{l,l})|\_{\mathcal{N}}>C\_{{\varepsilon}/2}\}) |  |
|  |  | =\displaystyle= | 1k2+P​({LT≤Mk}∩{∑l=1k−1λl|R​(Nl,l)|𝒩+∑l=kmλl​|R​(Nl,k)|𝒩>Cε/2})\displaystyle\frac{1}{k^{2}}+P(\{L\_{T}\leq M\_{k}\}\cap\{\sum\_{l=1}^{k-1}\lambda\_{l}|R(N^{l,l})|\_{\mathcal{N}}+\sum\_{l=k}^{m}\lambda\_{l}|R(N^{l,k})|\_{\mathcal{N}}>C\_{{\varepsilon}/2}\}) |  |
|  |  | ≤\displaystyle\leq | ε,\displaystyle{\varepsilon}, |  |

where the last inequality holds by ([3.25](https://arxiv.org/html/2602.15177v1#S3.E25 "In Proof of Theorem 3.6. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) since ∑l=0k−1λl​|R​(Nl,l)|𝒩+∑l=kmλl​|R​(Nl,k)|𝒩∈𝒞R,Mk\sum\_{l=0}^{k-1}\lambda\_{l}|R(N^{l,l})|\_{\mathcal{N}}+\sum\_{l=k}^{m}\lambda\_{l}|R(N^{l,k})|\_{\mathcal{N}}\in\mathcal{C}\_{R,M\_{k}}.
We have now shown that conv​{Ri,t,j​(Nl,l):l∈ℕ}\mbox{conv}\{R\_{i,t,j}(N^{l,l})\ :\ l\in\mathbb{N}\} is bounded in L0L^{0} for every 0≤i≤t≤T−10\leq i\leq t\leq T-1 and for every j=1,…,dj=1,\ldots,d. By Lemma [3.8](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem8 "Lemma 3.8 (Komlos’ lemma, Lemma A1.1 of [10]). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes"), applied successively to each component of (R​(Nn,n))n∈ℕ(R(N^{n,n}))\_{n\in{\mathbb{N}}}, there exists a sequence of convex weights (λnn,…,λJnn)n∈ℕ(\lambda\_{n}^{n},\ldots,\lambda^{n}\_{J\_{n}})\_{n\in\mathbb{N}} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=nJnλkn​R​(Nk,k)→N∈𝒩a.s.as​n→∞.\displaystyle\sum\_{k=n}^{J\_{n}}\lambda\_{k}^{n}R(N^{k,k})\to{N}\in\mathcal{N}\quad\text{a.s.}\quad\mbox{as}\ n\to\infty. |  | (3.27) |

By assumption, we have Vα​(x,R​(Nk,k))≥Vα​(x,Nk,k)V^{\alpha}(x,R(N^{k,k}))\geq V^{\alpha}(x,N^{k,k}) for all k∈ℕk\in\mathbb{N}. Together with the concavity of Vα​(⋅,⋅)V^{\alpha}(\cdot,\cdot), it implies that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vα​(x,∑k=nJnλkn​R​(Nk,k))\displaystyle V^{\alpha}(x,\sum\_{k=n}^{J\_{n}}\lambda\_{k}^{n}R(N^{k,k})) | ≥\displaystyle\geq | ∑k=nJnλkn​Vα​(x,R​(Nk,k))\displaystyle\sum\_{k=n}^{J\_{n}}\lambda\_{k}^{n}V^{\alpha}(x,R(N^{k,k})) |  |
|  |  | ≥\displaystyle\geq | ∑k=nJnλkn​Vα​(x,Nk,k)\displaystyle\sum\_{k=n}^{J\_{n}}\lambda\_{k}^{n}V^{\alpha}(x,N^{k,k}) |  |
|  |  | ≥\displaystyle\geq | ∑k=nJnλkn​(Vα​(x,Nk,k)−μk)for all ​n∈ℕ.\displaystyle\sum\_{k=n}^{J\_{n}}\lambda\_{k}^{n}(V^{\alpha}(x,N^{k,k})-{\mu}\_{k})\quad\quad\mbox{for all\ }n\in{\mathbb{N}}. |  |

By ([3.24](https://arxiv.org/html/2602.15177v1#S3.E24 "In Proof of Theorem 3.6. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) the RHS converges to ff a.s. as n→∞n\to\infty and by ([3.27](https://arxiv.org/html/2602.15177v1#S3.E27 "In Proof of Theorem 3.6. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes"))
the LHS converges to Vα​(x,N)V^{\alpha}(x,N) a.s. as n→∞n\to\infty. We obtain that
Vα​(x,N)≥fV^{\alpha}(x,N)\geq f, hence f∈𝒱α​(x)f\in\mathcal{V}^{\alpha}(x).
∎

###### Corollary 3.13.

If there are no redundant stocks in the sense that ℛt={0}\mathcal{R}\_{t}=\{0\} for all t=0,1,…,T−1t=0,1,\dots,T-1, then the market model satisfies the NUIBR condition and the set 𝒱α​(x)\mathcal{V}^{\alpha}(x) is closed with respect to the convergence in probability.

###### Proof.

Let us fix x∈ℝx\in{\mathbb{R}}, K∈ℝ+K\in{\mathbb{R}}\_{+} and show that ([3.9](https://arxiv.org/html/2602.15177v1#S3.E9 "In Definition 3.4. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) holds with reaction function Ri,t,j​(N):=Ni,t,jR\_{i,t,j}(N):=N\_{i,t,j}. By Lemma [2.3](https://arxiv.org/html/2602.15177v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2 The model ‣ Optimal investment under capital gains taxes")(iv), the
set {∑i=0T−1∑j=1dNi,i,j:N∈𝒩​with​Vα​(x,N)≥−K​a.s.}\left\{\sum\_{i=0}^{T-1}\sum\_{j=1}^{d}N\_{i,i,j}\ :\ N\in\mathcal{N}\ \text{with}\ V^{\alpha}(x,N)\geq-K\ \text{a.s.}\right\} is convex. This means that, by maxi=0,…,T−1,j=1,…,d⁡Ni,i,j≤∑i=0T−1∑j=1dNi,i,j\max\_{i=0,\ldots,T-1,\ j=1,\ldots,d}N\_{i,i,j}\leq\sum\_{i=0}^{T-1}\sum\_{j=1}^{d}N\_{i,i,j}, the convex hull in ([3.9](https://arxiv.org/html/2602.15177v1#S3.E9 "In Definition 3.4. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) is not required if the reaction function is the identity.
We have to show that the above set is L0L^{0}-bounded. Assume by contradiction that there are t∈{0,…,T−1}t\in\{0,\ldots,T-1\}, j∈{1,…,d}j\in\{1,\ldots,d\}, ε>0{\varepsilon}>0, and a sequence (Nn)n∈ℕ⊆𝒩(N^{n})\_{n\in\mathbb{N}}\subseteq\mathcal{N} with Vα​(x,Nn)≥−KV^{\alpha}(x,N^{n})\geq-K a.s. and
P​(Nt,t,jn>n)>ε{P}\left(N^{n}\_{t,t,j}>n\right)>{\varepsilon} for all n∈ℕn\in{\mathbb{N}}. Since qt​(⋅)q\_{t}(\cdot) is the identity by ℛt={0}\mathcal{R}\_{t}=\{0\},
Vα​(x,Nn)≥−KV^{\alpha}(x,N^{n})\geq-K a.s. for all n∈ℕn\in{\mathbb{N}} implies that lim supn→∞Nt,t,jn≤lim supn→∞(∑i=0tNi,t,jn)<∞\limsup\_{n\to\infty}N^{n}\_{t,t,j}\leq\limsup\_{n\to\infty}\left(\sum\_{i=0}^{t}N^{n}\_{i,t,j}\right)<\infty a.s. by
Lemma [2.3](https://arxiv.org/html/2602.15177v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2 The model ‣ Optimal investment under capital gains taxes")(iii) and Lemma [3.10](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem10 "Lemma 3.10. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")(iii), a contradiction.

The closedness of 𝒱α​(x)\mathcal{V}^{\alpha}(x) does not follow directly from Theorem [3.6](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem6 "Theorem 3.6. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes"), since we no longer assume S≥0S\geq 0 and r≤r¯∈ℝ+r\leq\overline{r}\in\mathbb{R}\_{+}. However, the proof is similar and even simpler since it is sufficient to argue only with the strategies of the original sequence.
Let (Nn,μn)n∈ℕ⊆𝒩×L0​(ℱT;ℝ+)(N^{n},\mu\_{n})\_{n\in{\mathbb{N}}}\subseteq\mathcal{N}\times L^{0}(\mathcal{F}\_{T};\mathbb{R}\_{+}) be a sequence such that Vα​(x,Nn)−μn→fV^{\alpha}(x,N^{n})-\mu\_{n}\to f in probability as n→∞n\to\infty. Passing to a subsequence, we may assume a.s.-convergence. Since qt​(⋅)q\_{t}(\cdot) is the identity, we obtain again by Lemma [2.3](https://arxiv.org/html/2602.15177v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2 The model ‣ Optimal investment under capital gains taxes")(iii) and Lemma [3.10](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem10 "Lemma 3.10. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")(iii) that lim supn→∞Nt,t,jn<∞\limsup\_{n\to\infty}N^{n}\_{t,t,j}<\infty for all t=0,…,T−1t=0,\dots,T-1, j=1,…,dj=1,\ldots,d. This implies that the set conv​{maxi=0,…,T−1,j=1,…,d⁡Ni,i,jn:n∈ℕ}\mbox{conv}\left\{\,\max\_{i=0,\ldots,T-1,\ j=1,\ldots,d}N^{n}\_{i,i,j}\ :\ n\in\mathbb{N}\right\} is bounded in L0L^{0}. We may now proceed exactly as in the proof of Theorem [3.6](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem6 "Theorem 3.6. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")
after Equation ([3.26](https://arxiv.org/html/2602.15177v1#S3.E26 "In Proof of Theorem 3.6. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")) by taking the reaction function Ri,t,j​(N)=Ni,t,jR\_{i,t,j}(N)=N\_{i,t,j} and replacing (Nn,n)n∈ℕ(N^{n,n})\_{n\in{\mathbb{N}}} by (Nn)n∈ℕ(N^{n})\_{n\in{\mathbb{N}}}.
∎

## 4 Utility maximization

We analyze the utility maximization problem under the natural constraint that the terminal wealth must be nonnegative.
Apart from this, we impose only minimal assumptions on the utility function:

###### Assumption 4.1.

Let U:ℝ→ℝ∪{−∞}U:{\mathbb{R}}\to{\mathbb{R}}\cup\{-\infty\} be a function that takes the value −∞-\infty on ℝ−∖{0}{\mathbb{R}}\_{-}\setminus\{0\}, whose restriction to ℝ+∖{0}{\mathbb{R}}\_{+}\setminus\{0\} is ℝ{\mathbb{R}}-valued, nondecreasing, and concave, and that satisfies U​(0)=limx↘0U​(x)U(0)=\lim\_{x\searrow 0}U(x).

We introduce the sets

|  |  |  |
| --- | --- | --- |
|  | 𝒜α​(x):={N∈𝒩:Vα​(x,N)≥0​ a.s.}\displaystyle\mathcal{A}^{\alpha}(x):=\{N\in\mathcal{N}\ :\ V^{\alpha}(x,N)\geq 0\text{ a.s.}\} |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝒱≥0α​(x):={Vα​(x,N):N∈𝒜α​(x)}−L0​(ℱT;ℝ+).\displaystyle\mathcal{V}\_{\geq 0}^{\alpha}(x):=\{V^{\alpha}(x,N)\ :\ N\in\mathcal{A}^{\alpha}(x)\}-L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+}). |  |

For x∈ℝ+∖{0}x\in{\mathbb{R}}\_{+}\setminus\{0\}, N∈𝒩N\in\mathcal{N} we define the expected utility as

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[U​(Vα​(x,N))]:=𝔼​[U+​(Vα​(x,N))]−𝔼​[U−​(Vα​(x,N))]\displaystyle\mathbb{E}[U(V^{\alpha}(x,N))]:=\mathbb{E}[U^{+}(V^{\alpha}(x,N))]-\mathbb{E}[U^{-}(V^{\alpha}(x,N))] |  |

with the convention 𝔼​[U​(Vα​(x,N))]:=−∞\mathbb{E}[U(V^{\alpha}(x,N))]:=-\infty if 𝔼​[U−​(Vα​(x,N))]=∞\mathbb{E}[U^{-}(V^{\alpha}(x,N))]=\infty, and consider the maximization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | uα​(x):=supN∈𝒜α​(x)𝔼​[U​(Vα​(x,N))].\displaystyle u^{\alpha}(x):=\sup\_{N\in\mathcal{A}^{\alpha}(x)}\mathbb{E}[U(V^{\alpha}(x,N))]. |  | (4.1) |

In frictionless markets, that is α=0\alpha=0, it is a well-known result that u0​(x)<∞u^{0}(x)<\infty for some x>0x>0 implies that u0​(x)<∞u^{0}(x)<\infty for all x>0x>0. We extend this result to the tax rate α<1\alpha<1.

###### Proposition 4.2.

If there exists α0∈[0,1)\alpha\_{0}\in[0,1) and x0>0x\_{0}>0 such that uα0​(x0)<∞u^{\alpha\_{0}}(x\_{0})<\infty, then

|  |  |  |
| --- | --- | --- |
|  | uα​(x)<∞∀x>0∀α∈[0,1).\displaystyle u^{\alpha}(x)<\infty\quad\forall x>0\quad\forall\alpha\in[0,1). |  |

###### Proof.

We only have to show that for a fixed α∈(0,1)\alpha\in(0,1) and a fixed x>0x>0, uα​(x)<∞u^{\alpha}(x)<\infty implies that u0​(x)<∞u^{0}(x)<\infty. The rest follows from
Rásonyi and Stettner [[24](https://arxiv.org/html/2602.15177v1#bib.bib24), Remark 1.1] and Lemma [2.3](https://arxiv.org/html/2602.15177v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2 The model ‣ Optimal investment under capital gains taxes")(iii).

Step 1: For N∈𝒜0​(x)N\in\mathcal{A}^{0}(x) define the process ξt:=∑s=1t1{Vs0​(x,N)≥0}\xi\_{t}:=\sum\_{s=1}^{t}1\_{\{V^{0}\_{s}(x,N)\geq 0\}}. Let us show that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vα​(x,N~)≥(1−α)ξT​V0​(x,N),where​N~t,t:=(1−α)ξt​∑i=0tNi,t,N~t,t+1:=0\displaystyle V^{\alpha}(x,\widetilde{N})\geq(1-\alpha)^{\xi\_{T}}V^{0}(x,N),\quad\mbox{where}\ \widetilde{N}\_{t,t}:=(1-\alpha)^{\xi\_{t}}\sum\_{i=0}^{t}N\_{i,t},\ \widetilde{N}\_{t,t+1}:=0 |  | (4.2) |

for t=0,…,T−1t=0,\ldots,T-1. Since N~\widetilde{N} realizes gains and losses immediately, it is possible to define, as in ([3](https://arxiv.org/html/2602.15177v1#S3.Ex32 "Proof. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")), a meaningful one-dimensional wealth process V¯\overline{V} of N~\widetilde{N} by the recursion V¯0=x\overline{V}\_{0}=x and

|  |  |  |
| --- | --- | --- |
|  | V¯t=(1+rt)​V¯t−1+⟨N~t−1,t−1,St−(1+rt)​St−1⟩\displaystyle\overline{V}\_{t}=(1+r\_{t})\overline{V}\_{t-1}+\langle\widetilde{N}\_{t-1,t-1},S\_{t}-(1+r\_{t})S\_{t-1}\rangle |  |
|  |  |  |
| --- | --- | --- |
|  | −α​[(1+rt)​V¯t−1+⟨N~t−1,t−1,St−(1+rt)​St−1⟩−V¯t−1⋆]+,t=1,…,T,\displaystyle\qquad\ -\alpha\left[(1+r\_{t})\overline{V}\_{t-1}+\langle\widetilde{N}\_{t-1,t-1},S\_{t}-(1+r\_{t})S\_{t-1}\rangle-\overline{V}^{\star}\_{t-1}\right]^{+},\quad t=1,\ldots,T, |  |

where V¯t−1⋆:=maxs=0,…,t−1⁡V¯s\overline{V}^{\star}\_{t-1}:=\max\_{s=0,\ldots,t-1}\overline{V}\_{s}.
We note that by α<1\alpha<1, after the payment of taxes the wealth still attains its running maximum.
On the other hand, we define the fictitious wealth process V¯\underline{V} of N~\widetilde{N} that would occur with a wealth tax due at the end of each period—but only when the wealth is nonnegative—by V¯0=x\underline{V}\_{0}=x and

|  |  |  |
| --- | --- | --- |
|  | V¯t=(1+rt)​V¯t−1+⟨N~t−1,t−1,St−(1+rt)​St−1⟩\displaystyle\underline{V}\_{t}=(1+r\_{t})\underline{V}\_{t-1}+\langle\widetilde{N}\_{t-1,t-1},S\_{t}-(1+r\_{t})S\_{t-1}\rangle |  |
|  |  |  |
| --- | --- | --- |
|  | −α​[(1+rt)​V¯t−1+⟨N~t−1,t−1,St−(1+rt)​St−1⟩]+,t=1,…,T.\displaystyle\qquad\ -\alpha\left[(1+r\_{t})\underline{V}\_{t-1}+\langle\widetilde{N}\_{t-1,t-1},S\_{t}-(1+r\_{t})S\_{t-1}\rangle\right]^{+},\quad t=1,\ldots,T. |  |

Using that V¯t−1⋆≥x>0\overline{V}^{\star}\_{t-1}\geq x>0 and α<1\alpha<1, one shows by induction on tt that V¯t≥V¯t\overline{V}\_{t}\geq\underline{V}\_{t} for t=0,…,Tt=0,\ldots,T.
Then, let us show by induction on tt that V¯t=(1−α)ξt​Vt0​(x,N)\underline{V}\_{t}=(1-\alpha)^{\xi\_{t}}V^{0}\_{t}(x,N) for t=0,…,Tt=0,\ldots,T. Assume that the assertion is already proven for t−1t-1.
We use that Vt0​(x,N)V^{0}\_{t}(x,N) satisfies the recursion given in ([2.4](https://arxiv.org/html/2602.15177v1#S2.E4 "In 2 The model ‣ Optimal investment under capital gains taxes")) and make first the observation that (1+rt)​V¯t−1+⟨N~t−1,t−1,St−(1+rt)​St−1⟩≥0(1+r\_{t})\underline{V}\_{t-1}+\langle\widetilde{N}\_{t-1,t-1},S\_{t}-(1+r\_{t})S\_{t-1}\rangle\geq 0 iff Vt0​(x,N)≥0V^{0}\_{t}(x,N)\geq 0, which then implies the assertion for tt. Putting together we arrive at ([4.2](https://arxiv.org/html/2602.15177v1#S4.E2 "In Proof. ‣ Proposition 4.2. ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")).

Step 2: Now, we can again apply the above mentioned argument by Rásonyi and Stettner [[24](https://arxiv.org/html/2602.15177v1#bib.bib24), Remark 1.1],
which we briefly repeat for the convenience of the reader. Suppose that uα​(x)<∞u^{\alpha}(x)<\infty and assume by contradiction that u0​(x)=∞u^{0}(x)=\infty. The latter means that there exists a sequence (Nn)n∈ℕ⊆𝒜0​(x)(N^{n})\_{n\in{\mathbb{N}}}\subseteq\mathcal{A}^{0}(x) with 𝔼​[U−​(V0​(x,Nn))]<∞\mathbb{E}[U^{-}(V^{0}(x,N^{n}))]<\infty for all n∈ℕn\in{\mathbb{N}} and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[U​(V0​(x,Nn))]→∞as​n→∞.\displaystyle\mathbb{E}[U(V^{0}(x,N^{n}))]\to\infty\quad\mbox{as}\ n\to\infty. |  | (4.3) |

One considers the strategies Nn/2N^{n}/2, which satisfy (1−α)T​V0​(x,Nn/2)=(1−α)T/2​(V0​(x,Nn)+x​∏t=1T(1+rt))(1-\alpha)^{T}V^{0}(x,N^{n}/2)=(1-\alpha)^{T}/2(V^{0}(x,N^{n})+x\prod\_{t=1}^{T}(1+r\_{t})). Since UU is concave, we have that

|  |  |  |
| --- | --- | --- |
|  | U​((1−α)T​V0​(x,Nn/2))\displaystyle U((1-\alpha)^{T}V^{0}(x,N^{n}/2)) |  |
|  |  |  |
| --- | --- | --- |
|  | ≥12​(1−α)T​U​(V0​(x,Nn))+(1−12​(1−α)T)​U​((1−α)T2−(1−α)T​x​∏t=1T(1+rt)).\displaystyle\geq\frac{1}{2}(1-\alpha)^{T}U(V^{0}(x,N^{n}))+\left(1-\frac{1}{2}(1-\alpha)^{T}\right)U\left(\frac{(1-\alpha)^{T}}{2-(1-\alpha)^{T}}x\prod\_{t=1}^{T}(1+r\_{t})\right). |  |

Since

|  |  |  |
| --- | --- | --- |
|  | U​((1−α)T2−(1−α)T​x​∏t=1T(1+rt))≥U​((1−α)T2−(1−α)T​x)>−∞,\displaystyle U\left(\frac{(1-\alpha)^{T}}{2-(1-\alpha)^{T}}x\prod\_{t=1}^{T}(1+r\_{t})\right)\geq U\left(\frac{(1-\alpha)^{T}}{2-(1-\alpha)^{T}}x\right)>-\infty, |  |

([4.3](https://arxiv.org/html/2602.15177v1#S4.E3 "In Proof. ‣ Proposition 4.2. ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")) implies that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[U​((1−α)T​V0​(x,Nn/2))]→∞as​n→∞.\displaystyle\mathbb{E}[U((1-\alpha)^{T}V^{0}(x,N^{n}/2))]\to\infty\quad\mbox{as}\ n\to\infty. |  |

Because of inequality ([4.2](https://arxiv.org/html/2602.15177v1#S4.E2 "In Proof. ‣ Proposition 4.2. ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")) applied to N:=Nn/2N:=N^{n}/2, this would only be possible if uα​(x)=∞u^{\alpha}(x)=\infty.
∎

###### Theorem 4.3.

Let α∈[0,1)\alpha\in[0,1) and x>0x>0. Suppose the market satisfies the NA condition, and that the set 𝒱≥0α​(x)\mathcal{V}\_{\geq 0}^{\alpha}(x) is closed in probability. If uα​(x)<∞u^{\alpha}(x)<\infty,
then there exists an optimal strategy N∈𝒜α​(x)N\in\mathcal{A}^{\alpha}(x), that is,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[U​(Vα​(x,N))]=uα​(x).\displaystyle\mathbb{E}[U(V^{\alpha}(x,N))]=u^{\alpha}(x). |  |

We have the following lemma that generalizes Rásonyi and Stettner [[24](https://arxiv.org/html/2602.15177v1#bib.bib24), Theorem 1.1] to markets with short-selling constraints.

###### Lemma 4.4.

Let α=0\alpha=0 and x∈ℝx\in{\mathbb{R}}. Suppose that the market, that can be identified with a frictionless market with short-selling constraints, satisfies NA. Then, the set {V​(x,N):N∈𝒩}−L0​(ℱT;ℝ+)\{V(x,N)\ :\ N\in\mathcal{N}\}-L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+}) is closed in probability. If, in addition,
x>0x>0 and u0​(x)<∞u^{0}(x)<\infty, then there exists an optimal strategy.

###### Proof.

Under NA, closedness follows from ([3.14](https://arxiv.org/html/2602.15177v1#S3.E14 "In Proof. ‣ Lemma 3.10. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")), Lemma [3.10](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem10 "Lemma 3.10. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")(iii), and Lemma [3.8](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem8 "Lemma 3.8 (Komlos’ lemma, Lemma A1.1 of [10]). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes").
Thus, the set 𝒱0​(x)\mathcal{V}^{0}(x) is closed in probability for every x>0x>0, and if u0​(x)<∞u^{0}(x)<\infty, an optimizer exists by Theorem [4.3](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes").
∎

To the best of our knowledge, there is no rigorous proof of the first assertion of Lemma [4.4](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes") in the literature.
But, in continuous time, there is the related result of Czichowsky and Schweizer [[6](https://arxiv.org/html/2602.15177v1#bib.bib6), Corollary 4.7] that the set of stochastic integrals with integrands taking values in a given random convex set is closed with regard to the semimartingale topology.
This is used by Pulido [[23](https://arxiv.org/html/2602.15177v1#bib.bib23)] to derive a FTAP for locally bounded asset price processes under short-selling constraints.
Since the assumptions in the discrete time arbitrage theory are weaker, the results in [[23](https://arxiv.org/html/2602.15177v1#bib.bib23)] cannot be applied to prove the first assertion of Lemma [4.4](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes").

###### Lemma 4.5 (Key Lemma).

Assume that the corresponding tax-free market satisfies NA and u0​(x)<∞u^{0}(x)<\infty for some x>0x>0. Then, for every x>0x>0 there exist x^>0\widehat{x}>0 and N^∈𝒜0​(x^)\widehat{N}\in\mathcal{A}^{0}(\widehat{x}) such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[U+​(V0​(x^,N^))]<∞andV0​(x,N)≤V0​(x^,N^)∀N∈𝒜0​(x).\displaystyle\mathbb{E}[U^{+}(V^{0}(\widehat{x},\widehat{N}))]<\infty\quad\mbox{and}\quad V^{0}(x,N)\leq V^{0}(\widehat{x},\widehat{N})\quad\forall N\in\mathcal{A}^{0}(x). |  |

It is easy to see that the existence of such a dominating terminal wealth directly leads to the desired result:

###### Proof of Theorem [4.3](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem3 "Theorem 4.3. ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes") given that Lemma [4.5](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem5 "Lemma 4.5 (Key Lemma). ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes") holds.

First, observe that the assumptions NA and uα​(x)<∞u^{\alpha}(x)<\infty for some x>0x>0 do not depend on the choice of α∈[0,1)\alpha\in[0,1) (Lemma [2.3](https://arxiv.org/html/2602.15177v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2 The model ‣ Optimal investment under capital gains taxes")(v) and Proposition [4.2](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")). We find a sequence (Nn)n∈ℕ⊆𝒜α​(x)(N^{n})\_{n\in{\mathbb{N}}}\subseteq\mathcal{A}^{\alpha}(x) such that

|  |  |  |
| --- | --- | --- |
|  | limn→∞𝔼​[U​(Vα​(x,Nn))]=uα​(x).\displaystyle\lim\_{n\to\infty}\mathbb{E}[U(V^{\alpha}(x,N^{n}))]=u^{\alpha}(x). |  |

From Lemma [2.3](https://arxiv.org/html/2602.15177v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2 The model ‣ Optimal investment under capital gains taxes")(iii) and Lemma [4.5](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem5 "Lemma 4.5 (Key Lemma). ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes") we know that

|  |  |  |
| --- | --- | --- |
|  | 0≤supn∈ℕVα​(x,Nn)≤supn∈ℕV0​(x,Nn)≤V0​(x^,N^)for some ​x^>0​ and ​N^∈𝒜0​(x^).\displaystyle 0\leq\sup\_{n\in\mathbb{N}}V^{\alpha}(x,N^{n})\leq\sup\_{n\in\mathbb{N}}V^{0}(x,N^{n})\leq V^{0}(\widehat{x},\widehat{N})\quad\mbox{for some }\widehat{x}>0\mbox{ and }\widehat{N}\in\mathcal{A}^{0}(\widehat{x}). |  |

With Lemma [3.8](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem8 "Lemma 3.8 (Komlos’ lemma, Lemma A1.1 of [10]). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes"), we get a sequence (V~nα)n∈ℕ(\widetilde{V}^{\alpha}\_{n})\_{n\in{\mathbb{N}}}
with

|  |  |  |
| --- | --- | --- |
|  | V~nα∈conv​{Vα​(x,Nk):k≥n},n∈ℕ,such that ​V~nα→V~αa.s. as ​n→∞\displaystyle\widetilde{V}\_{n}^{\alpha}\in\mbox{conv}\{V^{\alpha}(x,N^{k})\ :\ k\geq n\},\ n\in{\mathbb{N}},\quad\mbox{such that }\widetilde{V}\_{n}^{\alpha}\to\widetilde{V}^{\alpha}\quad\mbox{a.s. as }n\to\infty |  |

for some V~α∈L0​(ℱT;ℝ+)\widetilde{V}^{\alpha}\in L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+}). By concavity of UU, it follows that lim supn→∞𝔼​[U​(V~nα)]≥uα​(x)\limsup\_{n\to\infty}\mathbb{E}[U(\widetilde{V}\_{n}^{\alpha})]\geq u^{\alpha}(x).
Since 𝒱≥0α​(x)\mathcal{V}\_{\geq 0}^{\alpha}(x) is convex, we obtain (V~nα)n∈ℕ⊆𝒱≥0α​(x)(\widetilde{V}^{\alpha}\_{n})\_{n\in{\mathbb{N}}}\subseteq\mathcal{V}\_{\geq 0}^{\alpha}(x), that is, for all n∈ℕn\in\mathbb{N}, there exist N~n∈𝒜α​(x)\widetilde{N}^{n}\in\mathcal{A}^{\alpha}(x) and μ~n∈L0​(ℱT;ℝ+)\widetilde{\mu}\_{n}\in L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+}) such that V~nα=Vα​(x,N~n)−μ~n\widetilde{V}^{\alpha}\_{n}=V^{\alpha}(x,\widetilde{N}^{n})-\widetilde{\mu}\_{n}.
Since 𝒱≥0α​(x)\mathcal{V}\_{\geq 0}^{\alpha}(x) is
closed in probability by assumption, there is an N~∈𝒜α​(x)\widetilde{N}\in\mathcal{A}^{\alpha}(x) such that Vα​(x,N~)≥V~αV^{\alpha}(x,\widetilde{N})\geq\widetilde{V}^{\alpha}.
Since UU is nondecreasing we get

|  |  |  |
| --- | --- | --- |
|  | supn∈ℕU​(V~nα)≤supn∈ℕU​(Vα​(x,N~n))≤U+​(V0​(x^,N^)).\sup\_{n\in{\mathbb{N}}}U(\widetilde{V}\_{n}^{\alpha})\leq\sup\_{n\in{\mathbb{N}}}U(V^{\alpha}(x,\widetilde{N}^{n}))\leq U^{+}(V^{0}(\widehat{x},\widehat{N})). |  |

We now use the lemma of Fatou and the continuity of UU to arrive at

|  |  |  |
| --- | --- | --- |
|  | uα​(x)≤lim supn→∞𝔼​[U​(V~nα)]≤𝔼​[lim supn→∞U​(V~nα)]=𝔼​[U​(V~α)]≤𝔼​[U​(Vα​(x,N~))].u^{\alpha}(x)\leq\limsup\_{n\to\infty}\mathbb{E}[U(\widetilde{V}\_{n}^{\alpha})]\leq\mathbb{E}[\limsup\_{n\to\infty}U(\widetilde{V}\_{n}^{\alpha})]=\mathbb{E}[U(\widetilde{V}^{\alpha})]\leq\mathbb{E}[U(V^{\alpha}(x,\widetilde{N}))]. |  |

∎

### 4.1 Proof of Lemma [4.5](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem5 "Lemma 4.5 (Key Lemma). ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")

From now on we work with the corresponding frictionless market.
For a strategy N∈𝒜0​(x)N\in\mathcal{A}^{0}(x) we introduce the normalized one-period strategy defined
by

|  |  |  |  |
| --- | --- | --- | --- |
|  | βt​(N):=1Vt0​(x,N)​qt​(∑s=0tNs,t),t=0,…,T−1,\displaystyle\beta\_{t}(N):=\frac{1}{V^{0}\_{t}(x,N)}q\_{t}\left(\sum\_{s=0}^{t}N\_{s,t}\right),\qquad t=0,\ldots,T-1, |  | (4.4) |

with the convention βt​(N):=0\beta\_{t}(N):=0 on {Vt0​(x,N)=0}\{V^{0}\_{t}(x,N)=0\}. Under NA, we have P​(Vt0​(x,N)<0)=0P(V^{0}\_{t}(x,N)<0)=0 and {Vt0​(x,N)=0}⊆{VT0​(x,N)=0}\{V^{0}\_{t}(x,N)=0\}\subseteq\{V^{0}\_{T}(x,N)=0\} a.s., and the definition allows us to rewrite the frictionless wealth process from ([2.4](https://arxiv.org/html/2602.15177v1#S2.E4 "In 2 The model ‣ Optimal investment under capital gains taxes")) as a product:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt0​(x,N)=x​∏s=1t(1+rs+⟨βs−1​(N),Ss−(1+rs)​Ss−1⟩)\displaystyle V\_{t}^{0}(x,N)=x\prod\_{s=1}^{t}(1+r\_{s}+\langle\beta\_{s-1}(N),S\_{s}-(1+r\_{s})S\_{s-1}\rangle) |  | (4.5) |

with (a.s.) nonnegative factors.

Before we can begin our proof we need to introduce random sets.

###### Definition 4.6.

Fix t∈{0,…,T−1}t\in\{0,\ldots,T-1\} and consider the probability space (Ω,ℱt,ℙ)(\Omega,\mathcal{F}\_{t},\mathbb{P}).
A set-valued mapping M:Ω⇉ℝnM:\Omega\rightrightarrows{\mathbb{R}}^{n} is called an ℱt\mathcal{F}\_{t}-measurable random set if for every open set O⊆ℝnO\subseteq{\mathbb{R}}^{n} we have

|  |  |  |
| --- | --- | --- |
|  | M−1​(O):={ω∈Ω:M​(ω)∩O≠∅}∈ℱt.\displaystyle M^{-1}(O):=\{\omega\in\Omega\ :\ M(\omega)\cap O\neq\emptyset\}\in\mathcal{F}\_{t}. |  |

Furthermore, an ℱt\mathcal{F}\_{t}-measurable random set MM is called closed-valued (resp. compact-valued) if for every ω∈Ω\omega\in\Omega the
set M​(ω)M(\omega) is closed (resp. compact) with regard to the Euclidean norm in ℝn{\mathbb{R}}^{n}.
We denote by L0​(ℱt;M)L^{0}(\mathcal{F}\_{t};M) the space of equivalence classes of ℱt\mathcal{F}\_{t}-measurable random vectors taking values in MM a.s.

###### Note 4.7.

Let MM be a non-empty closed-valued ℱt\mathcal{F}\_{t}-measurable random set. For each ω∈Ω\omega\in\Omega, the dimension of M​(ω)⊆ℝnM(\omega)\subseteq{\mathbb{R}}^{n} is defined as the maximal number of linear independent elements of M​(ω)M(\omega).
Then, the mapping dim​(M){\rm dim}(M) that sends each ω∈Ω\omega\in\Omega to the dimension of M​(ω)M(\omega) is ℱt\mathcal{F}\_{t}-measurable.

###### Proof.

Closed-valued random sets have a Castaing representation, meaning that there exist a sequence (Xn)n∈ℕ(X\_{n})\_{n\in{\mathbb{N}}} of ℱt\mathcal{F}\_{t}-measurable ℝn{\mathbb{R}}^{n}-valued random variables such that M​(ω)={Xn​(ω):n∈ℕ}¯M(\omega)=\overline{\{X\_{n}(\omega)\ :\ n\in{\mathbb{N}}\}} for all ω∈Ω\omega\in\Omega (see, e.g., Pennanen and Perkkioe [[22](https://arxiv.org/html/2602.15177v1#bib.bib22), Theorem 1.27]). Define X∞:=0X\_{\infty}:=0, τ1​(ω):=inf{n∈ℕ:Xn​(ω)≠0}\tau\_{1}(\omega):=\inf\{n\in{\mathbb{N}}\ :\ X\_{n}(\omega)\neq 0\} and τk​(ω):=inf{n∈ℕ:Xn​(ω)∉span​{Xτ1​(ω),…,Xτk−1​(ω)}}\tau\_{k}(\omega):=\inf\{n\in{\mathbb{N}}\ :\ X\_{n}(\omega)\not\in{\rm span}\{X\_{\tau\_{1}}(\omega),\ldots,X\_{\tau\_{k-1}}(\omega)\}\}. We get dim(M)​(ω)=dim({Xn​(ω):n∈ℕ})=∑k=1n1{τk<∞}​(ω)\dim(M)(\omega)=\dim(\{X\_{n}(\omega)\ :\ n\in{\mathbb{N}}\})=\sum\_{k=1}^{n}1\_{\{\tau\_{k}<\infty\}}(\omega).
∎

###### Lemma 4.8.

For every t=0,…,T−1t=0,\ldots,T-1, we define the set

|  |  |  |
| --- | --- | --- |
|  | At:={βt∈𝒫t: 1+rt+1+⟨βt,St+1−(1+rt+1)​St⟩≥0​ a.s.}\displaystyle A\_{t}:=\{\beta\_{t}\in\mathcal{P}\_{t}\ :\ 1+r\_{t+1}+\langle\beta\_{t},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle\geq 0\text{ a.s.}\} |  |

Under NA, we have that there exists a compact-valued ℱt\mathcal{F}\_{t}-measurable random set Mt:Ω⇉ℝdM\_{t}:\Omega\rightrightarrows{\mathbb{R}}^{d} such that
At=L0​(ℱt;Mt)A\_{t}=L^{0}(\mathcal{F}\_{t};M\_{t}).

###### Proof.

Since 𝒫t\mathcal{P}\_{t} is closed in probability by ([3.11](https://arxiv.org/html/2602.15177v1#S3.E11 "In Lemma 3.7 (Lemma 3.3 and Lemma 3.4 in Kühn and Molitor [20]). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")), we get that AtA\_{t} is closed in probability. For all βt1,βt2∈At\beta^{1}\_{t},\beta^{2}\_{t}\in A\_{t} and for all M∈ℱtM\in\mathcal{F}\_{t}, we know by Lemma [3.7](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem7 "Lemma 3.7 (Lemma 3.3 and Lemma 3.4 in Kühn and Molitor [20]). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes") that 1M​βt1+1Mc​βt2∈𝒫t1\_{M}\beta^{1}\_{t}+1\_{M^{c}}\beta^{2}\_{t}\in\mathcal{P}\_{t}, and thus 1M​βt1+1Mc​βt2∈At1\_{M}\beta^{1}\_{t}+1\_{M^{c}}\beta^{2}\_{t}\in A\_{t}. By [[22](https://arxiv.org/html/2602.15177v1#bib.bib22), Theorem 1.60], we get the existence of a closed-valued
ℱt\mathcal{F}\_{t}-measurable random set Mt′M^{\prime}\_{t} such that At=L0​(ℱt;Mt′)A\_{t}=L^{0}(\mathcal{F}\_{t};M^{\prime}\_{t}). We use Mt′M^{\prime}\_{t} to construct a compact-valued random set. For this,
let βt∈At\beta\_{t}\in A\_{t} and assume P​(|βt|>0)>0P(|\beta\_{t}|>0)>0. The random variable ⟨βt,St+1−(1+rt+1)​St⟩​∏s=t+2T(1+rs)\langle\beta\_{t},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle\prod\_{s=t+2}^{T}(1+r\_{s}) is an attainable terminal wealth with initial capital 0 and a strategy from 𝒩t\mathcal{N}\_{t},
thus by (i) and (ii) of Lemma [3.10](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem10 "Lemma 3.10. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes")

|  |  |  |
| --- | --- | --- |
|  | P​({⟨βt,St+1−(1+rt+1)​St⟩​∏s=t+2T(1+rs)≤−εt​|βt|}∩{|βt|>0})≥𝔼​[εt​1{|βt|>0}]>0.\displaystyle P(\{\langle\beta\_{t},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle\prod\_{s=t+2}^{T}(1+r\_{s})\leq-{\varepsilon}\_{t}|\beta\_{t}|\}\cap\{|\beta\_{t}|>0\})\geq\mathbb{E}[{\varepsilon}\_{t}1\_{\{|\beta\_{t}|>0\}}]>0. |  |

Since βt∈At\beta\_{t}\in A\_{t}, this is only possible if |βt|≤εt−1∏s=t+1T(1+rs)=:Kt|\beta\_{t}|\leq{{\varepsilon}\_{t}^{-1}}\prod\_{s=t+1}^{T}(1+r\_{s})=:K\_{t} a.s., where Kt∈L0​(ℱT;ℝ+)K\_{t}\in L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+}).
We take a representative ξ\xi of essinfℱt​Kt∈L0​(ℱt;ℝ+){\rm essinf}\_{\mathcal{F}\_{t}}K\_{t}\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}\_{+}) (cf., e.g., [[22](https://arxiv.org/html/2602.15177v1#bib.bib22), Corollary B.22]) and observe that |βt|≤ξ|\beta\_{t}|\leq\xi a.s. because βt\beta\_{t} is ℱt\mathcal{F}\_{t}-measurable.
The ball B​(0,ξ)B(0,\xi) with origin 0 and random radius ξ\xi and Mt:=Mt′∩B​(0,ξ)M\_{t}:=M^{\prime}\_{t}\cap B(0,\xi) are compact-valued ℱt\mathcal{F}\_{t}-measurable random sets.
In addition, we have that At⊆L0​(ℱt;B​(0,ξ))A\_{t}\subseteq L^{0}(\mathcal{F}\_{t};B(0,\xi)). It follows that L0​(ℱt;Mt′)=At⊆L0​(ℱt;B​(0,ξ))∩L0​(ℱt;Mt′)=L0​(ℱt;B​(0,ξ)∩Mt′)L^{0}(\mathcal{F}\_{t};M^{\prime}\_{t})=A\_{t}\subseteq L^{0}(\mathcal{F}\_{t};B(0,\xi))\cap L^{0}(\mathcal{F}\_{t};M^{\prime}\_{t})=L^{0}(\mathcal{F}\_{t};B(0,\xi)\cap M^{\prime}\_{t}) and thus At=L0​(ℱt;Mt)A\_{t}=L^{0}(\mathcal{F}\_{t};M\_{t}).
∎

###### Lemma 4.9.

For any compact-valued ℱt\mathcal{F}\_{t}-measurable random set K:Ω⇉ℝdK:\Omega\rightrightarrows{\mathbb{R}}^{d} with 0∈K0\in K and dim(K)≤k\dim(K)\leq k a.s. we can find ℱt\mathcal{F}\_{t}-measurable
random variables (Yi)i=1,…,k(Y^{i})\_{i=1,\ldots,k} with Yi​(ω)∈K​(ω)Y^{i}(\omega)\in K(\omega) for all ω∈Ω\omega\in\Omega, i=1,…,ki=1,\ldots,k such that for all Y∈L0​(ℱt;K)Y\in L^{0}(\mathcal{F}\_{t};K) there exist λi∈L0​(ℱt;[−2i−1,2i−1])\lambda\_{i}\in L^{0}(\mathcal{F}\_{t};[-2^{i-1},2^{i-1}]) with

|  |  |  |
| --- | --- | --- |
|  | Y=∑i=1kλi​Yia.s.\displaystyle Y=\sum\_{i=1}^{k}\lambda\_{i}Y^{i}\quad\text{a.s.} |  |

###### Proof.

Let us prove this result by induction on the maximal value the random variable dim(K)\dim(K) can take. The base case k=0k=0 is trivial. If dim(K)=0\dim(K)=0 a.s. then K={0}K=\{0\} a.s., and the statement holds.

Now assume that the claim has already been proven for all compact-valued ℱt\mathcal{F}\_{t}-measurable random sets K~\widetilde{K} with 0∈K~0\in\widetilde{K} and dim(K~)≤k−1\dim(\widetilde{K})\leq k-1 a.s. for some k∈{1,…,d}k\in\{1,\ldots,d\}.
Let KK be a compact-valued ℱt\mathcal{F}\_{t}-measurable random set with 0∈K0\in K and dim(K)≤k\dim(K)\leq k a.s. Let us first identify a random variable that maximizes the Euclidean norm in KK. Since KK is compact-valued this is equivalent to maximizing the function

|  |  |  |
| --- | --- | --- |
|  | hK​(x,ω):=|x|−δK​(ω)​(x)={|x|if ​x∈K​(ω),−∞otherwise\displaystyle h\_{K}(x,\omega):=|x|-\delta\_{K(\omega)}(x)=\left\{\begin{array}[]{ll}|x|&\text{if }x\in K(\omega),\\ -\infty&\text{otherwise}\end{array}\right. |  |

Note that −hK-h\_{K} is a normal integrand as defined in, e.g., [[22](https://arxiv.org/html/2602.15177v1#bib.bib22), Section 1.1.2]. For every ω∈Ω\omega\in\Omega define Km​a​x​(ω):=argmaxx​hK​(x,ω)K\_{max}(\omega):=\text{argmax}\_{x}h\_{K}(x,\omega). By [[22](https://arxiv.org/html/2602.15177v1#bib.bib22), Corollary 1.23], KmaxK\_{\max} is a closed-valued random set and by construction, we have
Kmax​(ω)⊆K​(ω)K\_{\max}(\omega)\subseteq K(\omega) for all ω∈Ω\omega\in\Omega. Compact-valued random sets admit
a measurable selection ([[22](https://arxiv.org/html/2602.15177v1#bib.bib22), Corollary 1.28]) in the sense that there exists an ℱt\mathcal{F}\_{t}-measurable random variable YkY^{k} with Yk​(ω)∈Kmax​(ω)Y^{k}(\omega)\in K\_{\max}(\omega) for all ω∈Ω\omega\in\Omega.
Given such a YkY^{k}, we define the functions

|  |  |  |
| --- | --- | --- |
|  | λ​(x,ω):={⟨x,Yk​(ω)⟩|Yk​(ω)|2if ​Yk​(ω)≠0,0if ​Yk​(ω)=0\displaystyle\lambda(x,\omega):=\left\{\begin{array}[]{ll}\frac{\langle x,Y^{k}(\omega)\rangle}{|Y^{k}(\omega)|^{2}}&\text{if }Y^{k}(\omega)\neq 0,\\ 0&\text{if }Y^{k}(\omega)=0\end{array}\right. |  |

and G​(x,ω):=x−λ​(x,ω)​Yk​(ω)G(x,\omega):=x-\lambda(x,\omega)Y^{k}(\omega), which is the projection of xx onto the orthogonal complement of Yk​(ω)Y^{k}(\omega). It is easy to check that G​(⋅,ω)G(\cdot,\omega) is continuous for every ω∈Ω\omega\in\Omega, and that G​(x,⋅)G(x,\cdot) is measurable for every x∈ℝdx\in{\mathbb{R}}^{d}.
By [[22](https://arxiv.org/html/2602.15177v1#bib.bib22), Theorem 1.9], the mapping ω↦K~​(ω):=G​(K​(ω),ω)\omega\mapsto\widetilde{K}(\omega):=G(K(\omega),\omega) is measurable and dim(K~)=(dim(K)−1)∨0≤k−1\dim(\widetilde{K})=(\dim(K)-1)\vee 0\leq k-1 a.s. By compactness of K​(ω)K(\omega) for every ω∈Ω\omega\in\Omega and continuity of G​(⋅,ω)G(\cdot,\omega) for every ω∈Ω\omega\in\Omega, we obtain that K~​(ω)=G​(K​(ω),ω)\widetilde{K}(\omega)=G(K(\omega),\omega) is compact for every ω∈Ω\omega\in\Omega. Since 0∈K~0\in\widetilde{K}, we can apply the induction hypothesis to K~\widetilde{K} and find ℱt\mathcal{F}\_{t}-measurable random variables (Y~i)i=1,…,k−1(\widetilde{Y}^{i})\_{i=1,\ldots,k-1} with Y~i​(ω)∈K~​(ω)\widetilde{Y}^{i}(\omega)\in\widetilde{K}(\omega) for all ω∈Ω\omega\in\Omega, i=1,…,k−1i=1,\ldots,k-1 such that for every Y~∈L0​(ℱt;K~),\widetilde{Y}\in L^{0}(\mathcal{F}\_{t};\widetilde{K}), there exist λ~i∈L0​(ℱt;[−2i−1,2i−1])\widetilde{\lambda}\_{i}\in L^{0}(\mathcal{F}\_{t};[-2^{i-1},2^{i-1}]), i=1,…,k−1i=1,\ldots,k-1, with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y~=∑i=1k−1λ~i​Y~ia.s.\displaystyle\widetilde{Y}=\sum\_{i=1}^{k-1}\widetilde{\lambda}\_{i}\widetilde{Y}^{i}\quad\mbox{a.s.} |  | (4.8) |

Again using [[22](https://arxiv.org/html/2602.15177v1#bib.bib22), Theorem 1.9] and the fact that the intersection of two closed-valued random sets is a closed-valued random set, we have that for each i=1,…,k−1i=1,\ldots,k-1, Ci​(ω):=(G−1​(⋅,ω)​(Y~i​(ω)))∩K​(ω)C^{i}(\omega):=(G^{-1}(\cdot,\omega)(\widetilde{Y}^{i}(\omega)))\cap K(\omega) defines a compact-valued random set. Since Y~i​(ω)∈K~​(ω)\widetilde{Y}^{i}(\omega)\in\widetilde{K}(\omega) we have Ci​(ω)≠∅C^{i}(\omega)\neq\emptyset for all ω∈Ω\omega\in\Omega, i=1,…,k−1i=1,\ldots,k-1.
Again by [[22](https://arxiv.org/html/2602.15177v1#bib.bib22), Corollary 1.28], we can choose ℱt\mathcal{F}\_{t}-measurable random variables YiY^{i} with Yi​(ω)∈Ci​(ω)Y^{i}(\omega)\in C^{i}(\omega) for all ω∈Ω\omega\in\Omega and i=1,…,k−1i=1,\ldots,k-1. Now, let YY be representative of an element of L0​(ℱt;K)L^{0}(\mathcal{F}\_{t};K). The mapping ω↦λ​(Y​(ω),ω)\omega\mapsto\lambda(Y(\omega),\omega) is an ℱt\mathcal{F}\_{t}-measurable random variable that we denote by λ​(Y)\lambda(Y).
By construction, Y−λ​(Y)​Yk∈K~Y-\lambda(Y)Y^{k}\in\widetilde{K} a.s., and by ([4.8](https://arxiv.org/html/2602.15177v1#S4.E8 "In Proof. ‣ 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")), there exist λi∈L0​(ℱt;[−2i−1,2i−1])\lambda\_{i}\in L^{0}(\mathcal{F}\_{t};[-2^{i-1},2^{i-1}]) for i=1,…,k−1i=1,\ldots,k-1 such that

|  |  |  |
| --- | --- | --- |
|  | Y−λ​(Y)​Yk=∑i=1k−1λi​Y~i=∑i=1k−1λi​(Yi−λ​(Yi)​Yk)=∑i=1k−1λi​Yi−(∑i=1k−1λi​λ​(Yi))​Yka.s.\displaystyle Y-\lambda(Y)Y^{k}=\sum\_{i=1}^{k-1}\lambda\_{i}\widetilde{Y}^{i}=\sum\_{i=1}^{k-1}\lambda\_{i}({Y}^{i}-\lambda({Y}^{i}){Y}^{k})=\sum\_{i=1}^{k-1}\lambda\_{i}{Y}^{i}-\left(\sum\_{i=1}^{k-1}\lambda\_{i}\lambda({Y}^{i})\right)Y^{k}\quad\mbox{a.s.} |  |

The kk-th weight is set to λk:=λ​(Y)−∑i=1k−1λi​λ​(Yi)\lambda\_{k}:=\lambda(Y)-\sum\_{i=1}^{k-1}\lambda\_{i}\lambda({Y}^{i}).
Since YkY^{k} maximizes the Euclidean norm in KK, we have |λ​(Y)|≤1|\lambda(Y)|\leq 1 a.s. and |λ​(Yi)|≤1|\lambda(Y^{i})|\leq 1 for i=1,…,ki=1,\ldots,k. This guarantees that
|λk|≤1+∑i=1k−12i−1=2k−1|\lambda\_{k}|\leq 1+\sum\_{i=1}^{k-1}2^{i-1}=2^{k-1} a.s., which finishes the proof.
∎

β1\beta^{1}β2\beta^{2}Y2Y^{2}Y~1\widetilde{Y}^{1}Y1Y^{1}


(a) The vector Y2Y^{2} maximizes the Euclidean norm on AtA\_{t} and Y~1\widetilde{Y}^{1} that on the orthogonal projection of AtA\_{t} along Y2Y^{2}. Y1∈AtY^{1}\in A\_{t} is a vector that is projected on Y~1\widetilde{Y}^{1}.

β1\beta^{1}β2\beta^{2}Y1−Y2Y^{1}-Y^{2}−Y1+Y2-Y^{1}+Y^{2}Y1+Y2Y^{1}+Y^{2}−Y1−Y2-Y^{1}-Y^{2}


(b) The parallelogram with vertices ±Y1±Y2\pm Y^{1}\pm Y^{2} does not contain the set AtA\_{t}, but the larger one with vertices ±Y1±2​Y2\pm Y^{1}\pm 2Y^{2} does.

Figure 1: The set At⊆ℝ+2A\_{t}\subseteq{\mathbb{R}}\_{+}^{2} for two non-redundant stocks. Its boundary is given by the blue curve.

We are now ready to prove Lemma [4.5](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem5 "Lemma 4.5 (Key Lemma). ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes").

###### Proof of Lemma [4.5](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem5 "Lemma 4.5 (Key Lemma). ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes").

Let t∈{0,…,T−1}t\in\{0,\ldots,T-1\}. By Lemma [4.8](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem8 "Lemma 4.8. ‣ 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes"), we can apply Lemma [4.9](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem9 "Lemma 4.9. ‣ 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes") to the random set that is generated by AtA\_{t} and obtain: there are βti∈At\beta^{i}\_{t}\in A\_{t}, i=1,…,di=1,\ldots,d, such that for all βt∈At\beta\_{t}\in A\_{t} there exist λi∈L0​(ℱt;[−2i−1,2i−1])\lambda\_{i}\in L^{0}(\mathcal{F}\_{t};[-2^{i-1},2^{i-1}]) with βt=∑i=1dλi​βti\beta\_{t}=\sum\_{i=1}^{d}\lambda\_{i}\beta^{i}\_{t}.
For each t=0,…,T−1t=0,\ldots,T-1 we define the one-period normalized strategy

|  |  |  |
| --- | --- | --- |
|  | β^t:=∑i=1d2i−12d+1−1​βti∈L0​(ℱt;ℝ+d).\displaystyle\widehat{\beta}\_{t}:=\sum\_{i=1}^{d}\frac{2^{i-1}}{2^{d+1}-1}\beta^{i}\_{t}\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}^{d}\_{+}). |  |

As dynamic strategy, we consider N^∈𝒩\widehat{N}\in\mathcal{N} such that βt​(N^)\beta\_{t}(\widehat{N}) from ([4.4](https://arxiv.org/html/2602.15177v1#S4.E4 "In 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")), with initial capital x^:=(2d+1−1)T​x\widehat{x}:=(2^{d+1}-1)^{T}x, coincides with qt​(β^t)q\_{t}(\widehat{\beta}\_{t}) for each t=0,…,T−1t=0,\ldots,T-1. By ([4.5](https://arxiv.org/html/2602.15177v1#S4.E5 "In 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")), the wealth process reads

|  |  |  |
| --- | --- | --- |
|  | Vt0​(x^,N^)=x^​∏s=1t(1+rs+⟨β^s−1,Ss−(1+rs)​Ss−1⟩),t=0,…,T.V^{0}\_{t}(\widehat{x},\widehat{N})=\widehat{x}\prod\_{s=1}^{t}(1+r\_{s}+\langle\widehat{\beta}\_{s-1},S\_{s}-(1+r\_{s})S\_{s-1}\rangle),\quad t=0,\ldots,T. |  |

This means, the dominating wealth is constructed by starting with initial capital x^\widehat{x} and investing the product of β^t\widehat{\beta}\_{t} and the wealth at the beginning of each period in the stocks.

Let N∈𝒜0​(x)N\in\mathcal{A}^{0}(x) and define βt​(N)\beta\_{t}(N) as in ([4.4](https://arxiv.org/html/2602.15177v1#S4.E4 "In 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")) with initial capital xx. Under NA, one has βt​(N)∈At\beta\_{t}(N)\in A\_{t} for all t=0,…,T−1t=0,\ldots,T-1. This implies that for a fixed t=0,…,T−1t=0,\ldots,T-1 there exist λiN∈L0​(ℱt;[−2i−1,2i−1])\lambda^{N}\_{i}\in L^{0}(\mathcal{F}\_{t};[-2^{i-1},2^{i-1}]) such that

|  |  |  |
| --- | --- | --- |
|  | βt​(N)=∑i=1dλiN​βti.\displaystyle\beta\_{t}(N)=\sum\_{i=1}^{d}\lambda^{N}\_{i}\beta^{i}\_{t}. |  |

Next observe that we have the estimates:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |⟨βti,St+1−(1+rt+1)​St⟩|≤2​(1+rt+1)+⟨βti,St+1−(1+rt+1)​St⟩,i=1,…,d,\displaystyle|\langle\beta^{i}\_{t},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle|\leq 2(1+r\_{t+1})+\langle\beta^{i}\_{t},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle,\quad i=1,\ldots,d, |  | (4.9) |

which can be checked separately on the sets
{0≥⟨βti,St+1−(1+rt+1)​St⟩}\{0\geq\langle\beta^{i}\_{t},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle\} and
{0<⟨βti,St+1−(1+rt+1)​St⟩}\{0<\langle\beta^{i}\_{t},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle\}, using the property 1+rt+1+⟨βti,St+1−(1+rt+1)​St⟩≥01+r\_{t+1}+\langle\beta^{i}\_{t},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle\geq 0. We obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | ≤\displaystyle\leq | 1+rt+1+⟨βt​(N),St+1−(1+rt+1)​St⟩\displaystyle 1+r\_{t+1}+\langle\beta\_{t}(N),S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle |  |
|  |  | =\displaystyle= | 1+rt+1+∑i=1dλiN​⟨βti,St+1−(1+rt+1)​St⟩\displaystyle 1+r\_{t+1}+\sum\_{i=1}^{d}\lambda^{N}\_{i}\langle\beta^{i}\_{t},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle |  |
|  |  | ≤\displaystyle\leq | 1+rt+1+∑i=1d|λiN|​|⟨βti,St+1−(1+rt+1)​St⟩|\displaystyle 1+r\_{t+1}+\sum\_{i=1}^{d}|\lambda^{N}\_{i}||\langle\beta^{i}\_{t},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle| |  |
|  |  | ≤\displaystyle\leq | 1+rt+1+∑i=1d2i−1​(2​(1+rt+1)+⟨βti,St+1−(1+rt+1)​St⟩)\displaystyle 1+r\_{t+1}+\sum\_{i=1}^{d}2^{i-1}(2(1+r\_{t+1})+\langle\beta^{i}\_{t},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle) |  |
|  |  | =\displaystyle= | (1+rt+1)​(2d+1−1)+⟨∑i=1d2i−1​βti,St+1−(1+rt+1)​St⟩\displaystyle(1+r\_{t+1})(2^{d+1}-1)+\langle\sum\_{i=1}^{d}2^{i-1}\beta^{i}\_{t},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle |  |
|  |  | =\displaystyle= | (2d+1−1)​(1+rt+1+⟨β^t,St+1−(1+rt+1)​St⟩),t=0,…,T−1,\displaystyle(2^{d+1}-1)(1+r\_{t+1}+\langle\widehat{\beta}\_{t},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle),\quad t=0,\ldots,T-1, |  |

where the third inequality is by ([4.9](https://arxiv.org/html/2602.15177v1#S4.E9 "In Proof of Lemma 4.5. ‣ 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")). With the product representation of the wealth process from ([4.5](https://arxiv.org/html/2602.15177v1#S4.E5 "In 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")), we can multiply both sides over all tt and obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | VT0​(x,N)\displaystyle V\_{T}^{0}(x,N) | =\displaystyle= | x​∏t=0T−1(1+rt+1+⟨βt​(N),St+1−(1+rt+1)​St⟩)\displaystyle x\prod\_{t=0}^{T-1}(1+r\_{t+1}+\langle\beta\_{t}(N),S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle) |  |
|  |  | ≤\displaystyle\leq | x​∏t=0T−1(2d+1−1)​(1+rt+1+⟨β^t,St+1−(1+rt+1)​St⟩)\displaystyle x\prod\_{t=0}^{T-1}(2^{d+1}-1)(1+r\_{t+1}+\langle\widehat{\beta}\_{t},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle) |  |
|  |  | =\displaystyle= | VT0​(x^,N^).\displaystyle V^{0}\_{T}(\widehat{x},\widehat{N}). |  |

Applying ([4.1](https://arxiv.org/html/2602.15177v1#S4.Ex39 "Proof of Lemma 4.5. ‣ 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")) to N=0N=0 yields that VT0​(x^,N^)≥x​∏t=1T(1+rt)≥xV^{0}\_{T}(\widehat{x},\widehat{N})\geq x\prod\_{t=1}^{T}(1+r\_{t})\geq x and thus 𝔼​[U−​(V0​(x^,N^))]<∞\mathbb{E}[U^{-}(V^{0}(\widehat{x},\widehat{N}))]<\penalty 10000\ \infty. Then, Proposition [4.2](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes") yields that 𝔼​[U+​(V0​(x^,N^))]<∞\mathbb{E}[U^{+}(V^{0}(\widehat{x},\widehat{N}))]<\infty. Since x^\widehat{x} and N^\widehat{N} do not depend on NN, we are done.
∎

###### Remark 4.10.

Let us interpret our line of argument and compare it with that of Rásonyi and Stettner [[24](https://arxiv.org/html/2602.15177v1#bib.bib24)].
We show that the (random) polytope with vertices (2i−1​Yi)i=1,…,k(2^{i-1}Y^{i})\_{i=1,\ldots,k} and (−2i−1​Yi)i=1,…,k(-2^{i-1}Y^{i})\_{i=1,\ldots,k} contains AtA\_{t} (cf. Lemma [4.9](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem9 "Lemma 4.9. ‣ 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes") and Figure [1(b)](https://arxiv.org/html/2602.15177v1#S4.F1.sf2 "In Figure 1 ‣ 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")). Then, we can use that for nonnegative weights λi∈[0,2i−1]\lambda\_{i}\in[0,2^{i-1}], one
has λi​⟨Yi,St+1−(1+rt+1)​St⟩≤2i−1​[1+rt+1+⟨Yi,St+1−(1+rt+1)​St⟩]\lambda\_{i}\langle Y^{i},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle\leq 2^{i-1}\left[1+r\_{t+1}+\langle Y^{i},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle\right] and for negative weights λi∈[−2i−1,0)\lambda\_{i}\in[-2^{i-1},0), one still has the weaker estimate λi​⟨Yi,St+1−(1+rt+1)​St⟩≤2i−1​[2​(1+rt+1)+⟨Yi,St+1−(1+rt+1)​St⟩]\lambda\_{i}\langle Y^{i},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle\leq 2^{i-1}\left[2(1+r\_{t+1})+\langle Y^{i},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle\right]. Both holds since ⟨Yi,St+1−(1+rt+1)​St⟩≥−(1+rt+1)\langle Y^{i},S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle\geq-(1+r\_{t+1}) by Yi∈AtY^{i}\in A\_{t}.
Putting together, we can construct a one-period strategy that requires a multiple of the initial capital, but then dominates (a.s.) all other strategies. The multiple only depends on dd, which is the reason why the estimate can be extended in a straightforward way to multiperiod models.

In the proof of Rásonyi and Stettner [[24](https://arxiv.org/html/2602.15177v1#bib.bib24), Lemma 2.3], a similar estimate is provided. But they estimate against a maximum of finitely many trading gains of strategies from AtA\_{t}, which is itself in general no trading gain.
This is the reason why their approach to obtain an integrable majorant does not directly extend to the multiperiod model, and they apply other arguments instead.

There is yet another estimate in the monograph of Föllmer and Schied [[14](https://arxiv.org/html/2602.15177v1#bib.bib14), proof of Theorem 3.3]. Under the constraint that stock prices are nonnegative, a strategy with larger initial capital is constructed whose wealth dominates (a.s.) that of all strategies with initial capital 11. But, the required initial capital depends on the initial stock prices, which would be random from the second period onward, and thus, the result also does not extend directly to multiple periods.

###### Remark 4.11.

To include short-selling in the model with taxes, it would be natural to introduce random variables Ni,t,j′N^{\prime}\_{i,t,j} that specify the short-positions in the stocks separately. As in the model of Constantinides [[5](https://arxiv.org/html/2602.15177v1#bib.bib5), Subsection 4.1] with the FUL tax rule, the investor could
divest a stock from her portfolio but defer the tax payments due by trading in a market for short sell contracts.
Since this does not seem to be a quite realistic option, especially for retail investors, we exclude short-selling of the stocks.

However, mathematically, the short-selling constraints are used in only two places. In Theorem [3.6](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem6 "Theorem 3.6. ‣ 3 Closedness ‣ Optimal investment under capital gains taxes") we assume that S≥0S\geq 0, which means that shortable stocks would have to be bounded from above as well.
Furthermore, the decomposition into reversible and purely nonreversible strategies is under short-selling constraints.
This decomposition is an alternative to the orthogonal projection on the set of reversible strategies that can (only) be used in the case without short-selling constraints, in which strategies form a linear space.
But, the decomposition can also be applied to to the unconstraint problem by identifying it with an artificial constraint problem that has double the number of stocks:
for β,β′∈L0​(ℱt;ℝ+d)\beta,\beta^{\prime}\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}\_{+}^{d}), the gains are given by ⟨β,St+1−(1+rt+1)​St⟩+⟨β′,(1+rt+1)​St−St+1⟩\langle\beta,S\_{t+1}-(1+r\_{t+1})S\_{t}\rangle+\langle\beta^{\prime},(1+r\_{t+1})S\_{t}-S\_{t+1}\rangle. Applying Lemma [3.7](https://arxiv.org/html/2602.15177v1#S3.Thmtheorem7 "Lemma 3.7 (Lemma 3.3 and Lemma 3.4 in Kühn and Molitor [20]). ‣ 3 Closedness ‣ Optimal investment under capital gains taxes") to the artificial model, we obtain a purely nonreversible part qt​(β,β′)∈L0​(ℱt;ℝ+2​d)q\_{t}(\beta,\beta^{\prime})\in L^{0}(\mathcal{F}\_{t};{\mathbb{R}}\_{+}^{2d}) that possesses the necessary properties. However, (q​(β,β′)j−qt​(β,β′)j+d)j=1,…,d(q(\beta,\beta^{\prime})^{j}-q\_{t}(\beta,\beta^{\prime})^{j+d})\_{j=1,\ldots,d} need not coincide with the orthogonal projection of (βj−(β′)j)j=1,…,d(\beta^{j}-(\beta^{\prime})^{j})\_{j=1,\ldots,d} since for the latter, the components of the reversible and the purely nonreversible parts need not have the same sign as those of the strategy itself.

If the market is frictionless and contains no redundant securities, and the utility function is strictly concave, then the maximizer is unique ([[24](https://arxiv.org/html/2602.15177v1#bib.bib24), Theorem 1.2]). In the following, we show that with taxes there can be multiple maximizers even if the corresponding frictionless market model has no redundant securities in the sense that ℛt={0}\mathcal{R}\_{t}=\{0\} for all t=0,1,…,T−1t=0,1,\ldots,T-1. The minimalist example is a deterministic two-period model with d=1d=1, α∈(0,1)\alpha\in(0,1), x=1x=1, r>0r>0, S0=1S\_{0}=1, S1=1+aS\_{1}=1+a, and S2=(1+a)2S\_{2}=(1+a)^{2}, where a∈((1−α)​r,r)a\in((1-\alpha)r,r) is given by the solution of the equation

|  |  |  |
| --- | --- | --- |
|  | (1+a)2​(1−α)+α=(1+(1−α)​r)2.\displaystyle(1+a)^{2}(1-\alpha)+\alpha=(1+(1-\alpha)r)^{2}. |  |

Both investing the entire initial capital in the bank account and investing it in the stock are optimal, regardless of the utility function. However, the drawback of the example is that any debt-financed investment in stocks leads to sure losses.
One might be led to conjecture that in a model with a single stock, maximizers are unique in those periods where there is a positive probability of outperforming the bank account.
We therefore provide a more sophisticated example showing that this is not the case. By concavity of Vα​(x,⋅)V^{\alpha}(x,\cdot) (Lemma [2.3](https://arxiv.org/html/2602.15177v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2 The model ‣ Optimal investment under capital gains taxes")(iv)), the optimal terminal wealth has to be unique if the utility function is strictly concave.
But, two different strategies (and their convex combinations) generate the same optimal terminal wealth.

###### Example 4.12 (Non-uniqueness of maximizers).

Let T=3T=3, d=1d=1, α∈(0,1/9)\alpha\in(0,1/9), x=1x=1, Ω={ω1,ω2}\Omega=\{\omega\_{1},\omega\_{2}\} with P​({ω1})=P​({ω2})=1/2P(\{\omega\_{1}\})=P(\{\omega\_{2}\})=1/2, and ω\omega is revealed at time 22. The interest rate is constant r∈(0,1/3)r\in(0,1/3), and the price process of the single stock is given by S0=1S\_{0}=1, S1=1+aS\_{1}=1+a, S2​(ω1)=(1+a)​(1+4​r)S\_{2}(\omega\_{1})=(1+a)(1+4r), S2​(ω2)=(1+a)​(1−r)S\_{2}(\omega\_{2})=(1+a)(1-r), S3​(ω1)=(1+a)​(1+4​r)​(1+b)S\_{3}(\omega\_{1})=(1+a)(1+4r)(1+b), and S3​(ω2)=0S\_{3}(\omega\_{2})=0. The parameters aa and bb are not yet specified. They should be strictly smaller than rr, but r−ar-a and r−br-b should be small. This means that in the first and third period, the stock’s deterministic return is lower than the interest rate, but the advantage from deferring taxes would outweigh the difference.

First, we let λ≥1\lambda\geq 1 and consider the strategy NλN^{\lambda} with N0,0λ:=N0,1λ:=1N^{\lambda}\_{0,0}:=N^{\lambda}\_{0,1}:=1, N0,2λ:=1{ω1}N^{\lambda}\_{0,2}:=1\_{\{\omega\_{1}\}}, N1,1λ:=λ−1N^{\lambda}\_{1,1}:=\lambda-1, N1,2λ:=3/4​(λ−1)​1{ω1}N^{\lambda}\_{1,2}:=3/4(\lambda-1)1\_{\{\omega\_{1}\}}, and N2,2λ:=0N^{\lambda}\_{2,2}:=0. This means, the initial capital 11 is invested in the stock, λ−1\lambda-1 stocks are additionally purchased on credit at time 11, and at time 22 on {ω1}\{\omega\_{1}\}, the investor sells as many stocks as possible without triggering immediate tax payments. The stocks bought at 11 that have lower book profits (if a>0a>0) she sells first. If r−b>0r-b>0
is small enough such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1+4​r)​(1+b)​(1−α)+α>(1+(1−α)​4​r)​(1+(1−α)​r),\displaystyle(1+4r)(1+b)(1-\alpha)+\alpha>(1+(1-\alpha)4r)(1+(1-\alpha)r), |  | (4.11) |

this dominates a strategy that pay taxes already at time 22. We denote by r¯\underline{r} the unique number bb that satisfies ([4.11](https://arxiv.org/html/2602.15177v1#S4.E11 "In Example 4.12 (Non-uniqueness of maximizers). ‣ 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")) with equality. We note that r¯∈((1−α)​r,r)\underline{r}\in((1-\alpha)r,r).

We want to construct a second strategy N~λ\widetilde{N}^{\lambda} with N~0,0λ>1\widetilde{N}^{\lambda}\_{0,0}>1 but N~1,1λ<λ−1\widetilde{N}^{\lambda}\_{1,1}<\lambda-1 (for λ>1\lambda>1) that allows to sell more stocks at time 22 without triggering immediate tax payments because of larger realized losses in the bank account. We want to choose the parameters aa and bb (that do not depend on λ\lambda) such that Vα​(1,N~λ)=Vα​(1,Nλ)V^{\alpha}(1,\widetilde{N}^{\lambda})=V^{\alpha}(1,N^{\lambda}) for all λ≥1\lambda\geq 1. The requirement that Vα​(1,N~λ)​(ω2)V^{\alpha}(1,\widetilde{N}^{\lambda})(\omega\_{2}) coincides with Vα​(1,Nλ)​(ω2)=(1+a)​(1−(2​λ−1)​r)V^{\alpha}(1,N^{\lambda})(\omega\_{2})=(1+a)(1-(2\lambda-1)r) leads to the equation

|  |  |  |
| --- | --- | --- |
|  | (N~0,0λ−1)​[(1+a)​(1−r)−(1+r)2]\displaystyle(\widetilde{N}^{\lambda}\_{0,0}-1)\left[(1+a)(1-r)-(1+r)^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +(N~1,1λ−(λ−1))​[(1+a)​(1−r)−(1+a)​(1+r)]=0,\displaystyle+(\widetilde{N}^{\lambda}\_{1,1}-(\lambda-1))\left[(1+a)(1-r)-(1+a)(1+r)\right]=0, |  | (4.12) |

using that no taxes are paid on {ω2}\{\omega\_{2}\} if N~0,1λ≥1\widetilde{N}^{\lambda}\_{0,1}\geq 1. Now, we compare the realized losses of the candidate strategy N~λ\widetilde{N}^{\lambda} and NλN^{\lambda} up to time 22 on {ω1}\{\omega\_{1}\}. By ([4.12](https://arxiv.org/html/2602.15177v1#S4.Ex41 "Example 4.12 (Non-uniqueness of maximizers). ‣ 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")), the difference reads

|  |  |  |
| --- | --- | --- |
|  | (N~0,0λ−1)​(2​r+r2)+(N~1,1λ−(λ−1))​(1+a)​r\displaystyle(\widetilde{N}^{\lambda}\_{0,0}-1)(2r+r^{2})+(\widetilde{N}^{\lambda}\_{1,1}-(\lambda-1))(1+a)r |  |
|  |  |  |
| --- | --- | --- |
|  | =(N~0,0λ−1)​[2​r+r2−(1+a)​r​(1+a)​(1−r)−(1+r)2(1+a)​(1−r)−(1+a)​(1+r)]\displaystyle=(\widetilde{N}^{\lambda}\_{0,0}-1)\left[2r+r^{2}-(1+a)r\frac{(1+a)(1-r)-(1+r)^{2}}{(1+a)(1-r)-(1+a)(1+r)}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =:(N~0,0λ−1)[2r+r2−(1+a)rg(a)]\displaystyle=:(\widetilde{N}^{\lambda}\_{0,0}-1)\left[2r+r^{2}-(1+a)rg(a)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =:(N~0,0λ−1)L(a).\displaystyle=:(\widetilde{N}^{\lambda}\_{0,0}-1)L(a). |  | (4.13) |

We observe that L​(a)L(a) is positive since 2​r+r2−(1+a)​r​g​(a)=2​r+r2−(3​r−a+r2+a​r)/2>02r+r^{2}-(1+a)rg(a)=2r+r^{2}-(3r-a+r^{2}+ar)/2>0 for a∈((1−α)​r,r)a\in((1-\alpha)r,r).
By ([4.12](https://arxiv.org/html/2602.15177v1#S4.Ex42 "Example 4.12 (Non-uniqueness of maximizers). ‣ 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")) and again ([4.12](https://arxiv.org/html/2602.15177v1#S4.Ex41 "Example 4.12 (Non-uniqueness of maximizers). ‣ 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")), we can express the difference Vα​(1,N~λ)​(ω1)−Vα​(1,Nλ)​(ω1)V^{\alpha}(1,\widetilde{N}^{\lambda})(\omega\_{1})-V^{\alpha}(1,N^{\lambda})(\omega\_{1}) as a function ff of N~0,0λ−1>0\widetilde{N}^{\lambda}\_{0,0}-1>0. Crucial is that the function does not depend on λ\lambda.
After being taxed at time 33, there are gains from three investment intervals to compare, from 0 to 33, from 11 to 22, and from 11 to 33:

|  |  |  |
| --- | --- | --- |
|  | f​(N~0,0λ−1)\displaystyle f(\widetilde{N}^{\lambda}\_{0,0}-1) |  |
|  |  |  |
| --- | --- | --- |
|  | =(N~0,0λ−1)​(1−α)​[(1+a)​(1+4​r)​(1+b)−(1+r)3]\displaystyle=(\widetilde{N}^{\lambda}\_{0,0}-1)(1-\alpha)\left[(1+a)(1+4r)(1+b)-(1+r)^{3}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | +(N~0,0λ−1)​L​(a)(1+a)​4​r​(1−α)​(1+a)​[(1+4​r)​(1+r)−(1+r)2]\displaystyle+\frac{(\widetilde{N}^{\lambda}\_{0,0}-1)L(a)}{(1+a)4r}(1-\alpha)(1+a)\left[(1+4r)(1+r)-(1+r)^{2}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | +[−(N~0,0λ−1)​g​(a)−(N~0,0λ−1)​L​(a)(1+a)​4​r]​(1−α)​(1+a)​[(1+4​r)​(1+b)−(1+r)2]\displaystyle+\left[-(\widetilde{N}^{\lambda}\_{0,0}-1)g(a)-\frac{(\widetilde{N}^{\lambda}\_{0,0}-1)L(a)}{(1+a)4r}\right](1-\alpha)(1+a)\left[(1+4r)(1+b)-(1+r)^{2}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =:(N~0,0λ−1)A+(N~0,0λ−1)​L​(a)(1+a)​4​rB+[−(N~0,0λ−1)g(a)−(N~0,0λ−1)​L​(a)(1+a)​4​r]C.\displaystyle=:(\widetilde{N}^{\lambda}\_{0,0}-1)A+\frac{(\widetilde{N}^{\lambda}\_{0,0}-1)L(a)}{(1+a)4r}B+\left[-(\widetilde{N}^{\lambda}\_{0,0}-1)g(a)-\frac{(\widetilde{N}^{\lambda}\_{0,0}-1)L(a)}{(1+a)4r}\right]C. |  |

Since ff is linear, it vanishes if its slope, that depends on aa and bb, is zero. For a=ra=r and b<rb<r, one has that g​(a)=1g(a)=1, A=CA=C, and B>AB>A.
Thus, the slope is positive.
For b=rb=r and a<ra<r, we have B=CB=C and A<CA<C. Together with g​(a)≥1g(a)\geq 1 and C>0C>0, this implies that the slope is negative.
Now, we vary aa between r¯\underline{r} and rr and set b=r¯+r−ab=\underline{r}+r-a. As the slope is negative for a=r¯a=\underline{r} and positive for a=ra=r, there exists an intermediate value such that f=0f=0. We take such an intermediate value for aa and bb. Next, the strategy N~λ\widetilde{N}^{\lambda} is formally defined.
First, we define N~0,0λ\widetilde{N}^{\lambda}\_{0,0} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (N~0,0λ−1)​g​(a)+(N~0,0λ−1)​L​(a)(1+a)​4​r=3/4​(λ−1).\displaystyle(\widetilde{N}^{\lambda}\_{0,0}-1)g(a)+\frac{(\widetilde{N}^{\lambda}\_{0,0}-1)L(a)}{(1+a)4r}=3/4(\lambda-1). |  | (4.14) |

Given N~0,0λ\widetilde{N}^{\lambda}\_{0,0}, N~1,1λ\widetilde{N}^{\lambda}\_{1,1} is derived from ([4.12](https://arxiv.org/html/2602.15177v1#S4.Ex41 "Example 4.12 (Non-uniqueness of maximizers). ‣ 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")).
We complete the definition by setting N~0,1λ:=N~0,0λ\widetilde{N}^{\lambda}\_{0,1}:=\widetilde{N}^{\lambda}\_{0,0}, N~0,2λ:=N~0,0λ​1{ω1}\widetilde{N}^{\lambda}\_{0,2}:=\widetilde{N}^{\lambda}\_{0,0}1\_{\{\omega\_{1}\}}, N~1,2λ​(ω2):=0\widetilde{N}^{\lambda}\_{1,2}(\omega\_{2}):=0, and
N~2,2λ:=0\widetilde{N}^{\lambda}\_{2,2}:=0. By ([4.14](https://arxiv.org/html/2602.15177v1#S4.E14 "In Example 4.12 (Non-uniqueness of maximizers). ‣ 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")), the formal definition of N~λ\widetilde{N}^{\lambda} is in line with its earlier description.
If ω1\omega\_{1} occurs, just the stocks with the lower book profits are completely liquidated at time 22.
We arrive at Vα​(1,N~λ)=Vα​(1,Nλ)V^{\alpha}(1,\widetilde{N}^{\lambda})=V^{\alpha}(1,N^{\lambda}) (and by linearity of ff, all convex combinations of NλN^{\lambda} and N~λ\widetilde{N}^{\lambda} have the same terminal wealth as well). We observe that NλN^{\lambda} and N~λ\widetilde{N}^{\lambda} differ for λ>1\lambda>1.

Now, we consider a strategy NN with λ:=N0,0<1\lambda:=N\_{0,0}<1. Either NN can be strictly dominated by another strategy or we must have that
N1,1=N2,2=0N\_{1,1}=N\_{2,2}=0, N0,1=N0,0N\_{0,1}=N\_{0,0}, and N0,2=N0,0​1{ω1}N\_{0,2}=N\_{0,0}1\_{\{\omega\_{1}\}}. We denote this strategy by NλN^{\lambda} for λ<1\lambda<1. Indeed, by the choice of a,ba,b, an investor who wants to buy debt-financed stocks is indifferent between buying a part of them already at time 0 or buying the entire position only at time 11. This makes a strategy with N0,0<x=1N\_{0,0}<x=1 and N1,1>0N\_{1,1}>0 strictly suboptimal because
the situation is similar but the strategy has to pay taxes on the gains in the bank account already at time 11. Since strategies with N0,0≥1N\_{0,0}\geq 1 are also dominated, we arrive at

|  |  |  |
| --- | --- | --- |
|  | {Vα​(1,N):N∈𝒩}−L0​(ℱT;ℝ+)={Vα​(1,Nλ):λ∈ℝ+}−L0​(ℱT;ℝ+),\displaystyle\{V^{\alpha}(1,N)\ :\ N\in\mathcal{N}\}-L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+})=\{V^{\alpha}(1,N^{\lambda})\ :\ \lambda\in{\mathbb{R}}\_{+}\}-L^{0}(\mathcal{F}\_{T};{\mathbb{R}}\_{+}), |  |

and a utility maximization problem boils down to a one-dimensional maximization problem over λ\lambda.
Considered as functions of λ\lambda the terms Vα​(1,Nλ)​(ω1)V^{\alpha}(1,N^{\lambda})(\omega\_{1}) and Vα​(1,Nλ)​(ω2)V^{\alpha}(1,N^{\lambda})(\omega\_{2}) are differentiable at λ=2\lambda=2,
and the derivatives at this point, denoted by y1y\_{1} and y2y\_{2}, satisfy y1>0>y2y\_{1}>0>y\_{2} and y1>−y2y\_{1}>-y\_{2}. The latter follows from (1−α)​3​r​(1+(1−α)​r)>2​r​(1+r)(1-\alpha)3r(1+(1-\alpha)r)>2r(1+r).
In addition, one has Vα​(1,N2)​(ω1)>Vα​(1,N2)​(ω2)=(1+a)​(1−3​r)​(1+r)>0V^{\alpha}(1,N^{2})(\omega\_{1})>V^{\alpha}(1,N^{2})(\omega\_{2})=(1+a)(1-3r)(1+r)>0.
Now, we can take an arbitrary utility function UU that satisfies Assumption [4.1](https://arxiv.org/html/2602.15177v1#S4.Thmtheorem1 "Assumption 4.1. ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes") and that is differentable at Vα​(1,N2)​(ω1)V^{\alpha}(1,N^{2})(\omega\_{1}), Vα​(1,N2)​(ω2)V^{\alpha}(1,N^{2})(\omega\_{2}) with

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​y1​U′​(Vα​(1,N2)​(ω1))+12​y2​U′​(Vα​(1,N2)​(ω2))=0.\displaystyle\frac{1}{2}y\_{1}U^{\prime}(V^{\alpha}(1,N^{2})(\omega\_{1}))+\frac{1}{2}y\_{2}U^{\prime}(V^{\alpha}(1,N^{2})(\omega\_{2}))=0. |  | (4.15) |

By construction of the parameters a,ba,b, we have that Vα​(1,N(1−β)​λ1+β​λ2)≥Vα​(1,(1−β)​Nλ1+β​Nλ2)V^{\alpha}(1,N^{(1-\beta)\lambda\_{1}+\beta\lambda\_{2}})\geq V^{\alpha}(1,(1-\beta)N^{\lambda\_{1}}+\beta N^{\lambda\_{2}}) for all λ1,λ2≥0\lambda\_{1},\lambda\_{2}\geq 0, β∈[0,1]\beta\in[0,1]. Together with Lemma [2.3](https://arxiv.org/html/2602.15177v1#S2.Thmtheorem3 "Lemma 2.3. ‣ 2 The model ‣ Optimal investment under capital gains taxes")(iv), this implies that the
mappings λ↦Vα​(1,Nλ)​(ωi)\lambda\mapsto V^{\alpha}(1,N^{\lambda})(\omega\_{i}), i=1,2i=1,2 are concave. Therefore, ([4.15](https://arxiv.org/html/2602.15177v1#S4.E15 "In Example 4.12 (Non-uniqueness of maximizers). ‣ 4.1 Proof of Lemma 4.5 ‣ 4 Utility maximization ‣ Optimal investment under capital gains taxes")) implies that 𝔼​[U​(Vα​(1,N2))]=supN∈𝒩𝔼​[U​(Vα​(1,N))]\mathbb{E}[U(V^{\alpha}(1,N^{2}))]=\sup\_{N\in\mathcal{N}}\mathbb{E}[U(V^{\alpha}(1,N))]. Since N2N^{2} and N~2\widetilde{N}^{2} generate the same terminal wealth, we are done.

## References

* [1]

  Ben Tahar, I., Soner, H.M., and Touzi, N.: The dynamic programming equation for the problem of optimal
  investment under capital gains taxes. SIAM J. Control Optim., 46, 1779–1801 (2007).
* [2]

  Ben Tahar, I., Soner, H.M., and Touzi, N.: Merton problem with taxes: Characterization, computation, and approximation.
  SIAM J. Finan. Math., 1, 366–395 (2010).
* [3]

  Bian, B., Chen, X., Dai, M., and Qian, S.: Penalty method for portfolio selection with capital gains tax.
  Mathematical Finance, 31, 1013–1055 (2021)
* [4]

  Cai, J., Chen, X., and Dai, M.: Portfolio Selection with Capital Gains Tax, Recursive Utility, and Regime Switching.
  Management Science , 64, 2308–2324 (2018)
* [5]

  Constantinides, G. M.: Capital Market Equilibrium with Personal Tax. Econometrica, 51, 611–636 (1983)
* [6]

  Czichowsky, C., Schweizer, M.: Closedness in the semimartingale topology for spaces of stochastic integrals with constrained integrands. In
  Séminaire de Probabilités XLIII, Berlin, Heidelberg: Springer, pp. 413–436 (2010)
* [7]

  Dalang, R.C., Morton, A., and Willinger, W.: Equivalent martingale measures and no-arbitrage in stochastic securities market models.
  Stoch. Stoch. Rep., 29, 185–201 (1990)
* [8]

  Dammon, R.M., Spatt, C.S., and Zhang, H.H.: Optimal Consumption and Investment with Capital Gains Taxes. Review of Financial Studies,
  14, 583–616 (2001)
* [9]

  Dammon, R.M., Spatt, C.S., and Zhang, H.H.:
  Optimal Asset Location and Allocation with Taxable and Tax-Deferred Investing.
  Journal of Finance, 59, 999–1037 (2004)
* [10]
   Delbaen, F., Schachermayer, W.: A general version of the fundamental theorem of asset pricing. Mathematische Annalen, 300, 463–520 (1994)
* [11]

  Dybvig, P., Koo, H.: Investment with taxes. Working paper, Washington University, St. Louis, MO (1996)
* [12]

  Ehling, P., Gallmeyer, M., Srivastava, S., Tompaidis, S., and Yang, C.:
  Portfolio Tax Trading with Carryover Losses.
  Management Science, 64, 4156–4176 (2018)
* [13]

  Fischer, M., Gallmeyer, M.: Taxable and Tax-Deferred Investing with the Limited Use of Losses. Review of Finance, 21, 1847–1873 (2017)
* [14]

  Föllmer, H., Schied, A.: Stochastic Finance: An Introduction in Discrete Time, 4th edn., Walter de Gruyter, Berlin (2016)
* [15]

  Haugh, M., Iyengar, G., and Wang, C.: Tax-Aware Dynamic Asset Allocation. Operations Research, 64, 849–866 (2016)
* [16]

  Jouini, E., Koehl, P.-F., and Touzi, N.: Optimal investment with taxes: an optimal control problem with endogenous delay.
  Nonlinear Anal., 37, 31–56 (1999)
* [17]

  Jouini, E., Koehl, P.-F., and Touzi, N.: Optimal investment with taxes: an existence result. J. Math. Econ., 33, 373–388 (2000)
* [18]

  Kallsen, J., Muhle-Karbe, J.: Existence of shadow prices in finite probability spaces.
  Math. Meth. Oper. Res., 73, 251–262 (2011)
* [19]

  Kühn, C.: How local in time is the no-arbitrage property under capital gains taxes? Math. Finan. Econ., 13, 329–358 (2019)
* [20]

  Kühn, C., Molitor, A. Prospective strict no-arbitrage and the fundamental theorem of asset pricing under transaction costs. Finance and Stochastics, 23, 1049–1077. (2019)
* [21]
   Kramkov, D., Schachermayer, W.: The asymptotic elasticity of utility functions and optimal investment in incomplete markets.
  Ann. Appl. Probab., 9, 904–950 (1999)
* [22]

  Pennanen, T., Perkkiö, A.-P.: Convex Stochastic Optimization: Dynamic Programming and Duality in Discrete Time, Springer (2024)
* [23]

  Pulido, S.: The fundamental theorem of asset pricing, the hedging problem and maximal claims in financial markets with short sales prohibitions.
  Ann. Appl. Probab., 24, 54–75, (2014)
* [24]

  Rásonyi, M., Stettner, L.: On the Existence of Optimal Portfolios for the Utility Maximization Problem in Discrete Time Financial Market Models. In
  Kabanov, Y., Liptser, R., and Stoyanov, J. (eds.), From Stochastic Calculus to Mathematical Finance. Berlin, Heidelberg: Springer, pp. 589–608 (2005)
* [25]

  Rockafellar, R.T.: Convex Analysis, Princeton University Press (1970)
* [26]
   Schachermayer, W.: A Hilbert space proof of the fundamental theorem of asset pricing in finite discrete time.
  Insur. Math. Econ., 11, 249–257 (1992)
* [27]
   Schachermayer, W.: The fundamental theorem of asset pricing under proportional transaction costs in finite discrete time. Mathematical Finance, 14, 19–48 (2004)
* [28]
   Seifried, F.: Optimal Investment with Deferred Capital Gains Taxes. Mathematical Methods of Operations Research, 71,
  181–199 (2010)
* [29]
   Witsenhausen, H.S.: On Information Structures, Feedback and Causality. SIAM Journal on Control, 9, 149–160 (1971)