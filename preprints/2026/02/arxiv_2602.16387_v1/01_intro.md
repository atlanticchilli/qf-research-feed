---
authors:
- Leander Besting
- Martin Hoefer
- Lars Huth
doc_id: arxiv:2602.16387v1
family_id: arxiv:2602.16387
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Computing Tarski Fixed Points in Financial Networks
url_abs: http://arxiv.org/abs/2602.16387v1
url_html: https://arxiv.org/html/2602.16387v1
venue: arXiv q-fin
version: 1
year: 2026
---


Leander Besting
Faculty of Computer Science, RWTH Aachen University, Germany. leander.besting@rwth-aachen.de
  
Martin Hoefer
Faculty of Computer Science, RWTH Aachen University, Germany. mhoefer@cs.rwth-aachen.de
  
Lars Huth
Faculty of Computer Science, RWTH Aachen University, Germany. huth@algo.rwth-aachen.de

###### Abstract

Modern financial networks are highly connected and result in complex interdependencies of the involved institutions. In the prominent Eisenberg-Noe model [[12](https://arxiv.org/html/2602.16387v1#bib.bib19 "Systemic risk in financial systems")], a fundamental aspect is *clearing* – to determine the amount of assets available to each financial institution in the presence of potential defaults and bankruptcy. A clearing state represents a fixed point that satisfies a set of natural axioms. Existence can be established (even in broad generalizations of the model) using Tarski’s theorem.

While a *maximal* fixed point can be computed in polynomial time, the complexity of computing other fixed points is open. In this paper, we provide an efficient algorithm to compute a *minimal* fixed point that runs in strongly polynomial time. It applies in a broad generalization of the Eisenberg-Noe model with any monotone, piecewise-linear payment functions and default costs. Moreover, in this scenario we provide a polynomial-time algorithm to compute a *maximal* fixed point. For networks without default costs, we can efficiently decide the existence of fixed points in a given range.

We also study claims trading, a local network adjustment to improve clearing, when networks are evaluated with minimal clearing. We provide an efficient algorithm to decide existence of Pareto-improving trades and compute optimal ones if they exist.

## 1 Introduction

Modern financial systems exhibit highly complex debt relationships between their constituents. An important concern in these networks is systemic risk – after a shock, financial institutions become pressured to pay back (or *clear*) their debt. This leaves some of them in default. Consequently, creditors receiving little or no payments from their defaulting debtors might in turn be unable to meet their own obligations. As such, default can quickly propagate throughout the whole network. This is a realistic concern with the most well-known occurrence being the financial crisis of 2008 (and many other, less severe episodes since then).

The canonical framework to understand properties of debt clearing in financial networks is the Eisenberg-Noe model [[12](https://arxiv.org/html/2602.16387v1#bib.bib19 "Systemic risk in financial systems")]. It has, for example, been used by the European Central Bank in its STAMP€  framework for financial stress-testing [[32](https://arxiv.org/html/2602.16387v1#bib.bib59 "STAMP€: stress-test analytics for macroprudential purposes in the euro area")]. There are nn financial institutions (termed “banks” throughout), which are represented by nodes in an edge-weighted, directed graph. There are mm edges, each representing a debt claim, with an edge weight expressing the liability of the claim. Banks have (usually non-negative) external assets, which capture funds available for clearing that are not part of the claim network. The basic solution concept in the Eisenberg-Noe model is a *clearing state*, which yields an assignment of assets of banks and payments on each edge that satisfies a set of natural axioms. When a creditor bank is in default, its claims will not be valued by the liability but only the amount that the creditor will pay off in accordance with their legal requirements111In the United States, the legal framework for this is given by Chapter 11 bankruptcy [[7](https://arxiv.org/html/2602.16387v1#bib.bib55 "Bankruptcy basics")].. As one of the axioms, the Eisenberg-Noe model assumes *proportional* debt clearing, i.e., for a bank in default there is a *recovery rate* given by the ratio of total assets available to the total liabilities of the bank. The recovery rate translates directly into proportional payments for all claims where the bank is the creditor. For a more formal discussion of the model, see Section [2](https://arxiv.org/html/2602.16387v1#S2 "2 Model and Preliminaries ‣ Computing Tarski Fixed Points in Financial Networks") below.

Clearing states in the Eisenberg-Noe model are Tarski fixed points. The Knaster-Tarski theorem states that for any monotone function mapping a complete lattice to itself, the set of fixed points of the function constitutes a complete lattice. This implies, in particular, that at least one such fixed point exists and that fixed points might not be unique. The complexity of computing Tarski fixed points has been of significant interest recently, especially on the kk-dimensional grid (see, e.g., [[6](https://arxiv.org/html/2602.16387v1#bib.bib23 "Reducing Tarski to Unique Tarski (in the black-box model)"), [5](https://arxiv.org/html/2602.16387v1#bib.bib22 "Tarski lower bounds from multi-dimensional herringbones")] and the references therein).

While it is known how to compute the *maximal* fixed point in the Eisenberg-Noe model in polynomial time [[12](https://arxiv.org/html/2602.16387v1#bib.bib19 "Systemic risk in financial systems"), [27](https://arxiv.org/html/2602.16387v1#bib.bib30 "Failure and rescue in an interbank network")], we concentrate on finding every other fixed point (most notably, the *minimal* one). A maximal clearing state is desirable from a centralized perspective, since it yields pointwise maximal assets and payments for each bank and claim, respectively. However, it is unlikely that in the present multi-national financial system, a central coordination agency can dictate such assets and payments in times of crises. As such, arguably, the emergence of other clearing states is more realistic. The *minimal* one has been shown to emerge as the limit of a natural sequential clearing process [[8](https://arxiv.org/html/2602.16387v1#bib.bib16 "Decentralized clearing in financial networks")]. More generally, other clearing states can also emerge if agents update their recovery rates in a sequential fashion [[26](https://arxiv.org/html/2602.16387v1#bib.bib28 "Sequential defaulting in financial networks")]. However, to our knowledge, finding efficient algorithms to compute such clearing states or characterizing their computational complexity are important open problems.

#### Our Results and Techniques

We show that a minimal clearing state in the Eisenberg-Noe model can be computed in polynomial time. In contrast to computing the maximal one, it is not possible to formulate the problem directly as an LP. Our approach in Section [3](https://arxiv.org/html/2602.16387v1#S3 "3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") can be seen as a careful adjustment of the bottom iteration for Tarski fixed points. A naive implementation of the bottom iteration (which results, e.g., from distributed clearing processes [[8](https://arxiv.org/html/2602.16387v1#bib.bib16 "Decentralized clearing in financial networks")]) would start with the external assets at each bank and then propagate payments and assets into the system. This can take infinite time to converge to the fixed point. Instead of propagating all external assets directly, we inject external assets sequentially and simulate their (infinite) propagation by solving several carefully designed LPs. In particular, upon injection of additional assets at a node vv, our algorithm distinguishes two cases: (1) all additional assets circulate and gradually reach a “sink” bank without any solvency event, and (2) some assets keep circulating until another bank becomes solvent. Case (1) yields a linear increase in the payments of every claim, and we compute the slopes by solving a polynomial-sized system of linear equations. Then we can inject the assets at vv and compute the increase in assets and payments using the slopes. Case (2) arises if any positive portion of the assets injected at vv eventually reaches a part CC of the network that we term *flooded* – where all outgoing paths of any node eventually return to that node. More formally, consider the strongly connected components (SCCs) of the remaining network of open claims. The graph of SCCs is a DAG, and a flooded part CC is exactly a sink component of the SCC graph, which contains more than one bank. In this case, we do not inject any additional assets at vv but instead increase the payments within the sink component CC by a circulation (consistent with proportional payments) until a bank becomes solvent. This can be computed using a suitable LP. We then update the SCC graph and again attempt to inject additional assets at vv. Overall, we see that in each iteration, we either fully inject the external assets of a bank or create a solvent bank. Thus, at most 2​n2n iterations are needed.

Our algorithmic ideas turn out to be very powerful to address many generalizations of the problem. First, we relax the condition of proportional payments to the class of arbitrary *monotone and piecewise-linear* payment functions. This class includes many important examples considered in the literature recently, including edge ranking [[4](https://arxiv.org/html/2602.16387v1#bib.bib63 "Flow allocation games"), [17](https://arxiv.org/html/2602.16387v1#bib.bib14 "Seniorities and minimal clearing in financial network games"), [14](https://arxiv.org/html/2602.16387v1#bib.bib64 "Dynamic debt swapping in financial networks")] (or singleton liability priorities [[20](https://arxiv.org/html/2602.16387v1#bib.bib25 "Financial networks with singleton liability priorities")]), unit-ranking [[8](https://arxiv.org/html/2602.16387v1#bib.bib16 "Decentralized clearing in financial networks"), [4](https://arxiv.org/html/2602.16387v1#bib.bib63 "Flow allocation games"), [17](https://arxiv.org/html/2602.16387v1#bib.bib14 "Seniorities and minimal clearing in financial network games")], or priority-proportional [[22](https://arxiv.org/html/2602.16387v1#bib.bib34 "On priority-proportional payments in financial networks"), [13](https://arxiv.org/html/2602.16387v1#bib.bib21 "Financial networks, cross holdings, and limited liability")]. By using appropriate granularity, we can handle arbitrary monotone payment functions via approximation with piecewise-linear ones. The extension requires applying our algorithm and the analysis in phases, where each phase ends with reaching an interval border for the payment function of any edge. In each phase, all payments behave linearly, so slopes in case (1) and circulation in case (2) can be obtained by setting up and solving appropriate systems of linear equations. The interval borders of the payment functions limit the increase in external assets of vv in case (1), as well as the amount of the circulation in case (2).

Second, we show how to handle an extension of the model to *default costs* for insolvent banks [[27](https://arxiv.org/html/2602.16387v1#bib.bib30 "Failure and rescue in an interbank network")]. Here, the assets of each defaulting bank are additionally reduced by a constant factor. This adjustment represents a linear decrease in the assets, which can be integrated into the network. Since we monotonically increase payments and assets throughout, we (only) need to be careful when a bank vv becomes solvent. The challenge is that the fixed point function ceases to be continuous from below. Thus, a standard bottom iteration might fail to guarantee convergence to a minimal clearing state in the limit.

For each bank vv, we can represent default cost using an auxiliary claim to an auxiliary individual “sink bank” such that this bank receives the default cost. When vv becomes solvent, the default cost vanishes, we remove the auxiliary sink bank, and inject the remaining assets as additional external assets at the out-neighbors of vv. This view directly indicates how our approach of sequential injection of external assets can be extended to handle default cost.

Third, for networks without default cost, we can also compute *arbitrary* clearing states. When we consider any clearing state, the difference flow between the clearing state and a minimal clearing state is a circulation. As such, by applying case (2) of the algorithm above and iteratively “flooding” sink components (partially, in any order), we can produce any possible clearing state. We use this insight to tackle a *range clearing problem*: For a subset of relevant banks S⊆VS\subseteq V, there is a closed target interval Iv⊂ℝI\_{v}\subset\mathbb{R}, for each v∈Sv\in S. The question is whether there exists a clearing state 𝐚\mathbf{a} such that av∈Iva\_{v}\in I\_{v} for all v∈Sv\in S. We show that this problem can be solved in polynomial time.

More fundamentally, in Section [3.4](https://arxiv.org/html/2602.16387v1#S3.SS4 "3.4 Characterization and Maximal Clearing States ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") we show an interesting structural equivalence. Every financial network with piecewise-linear payment functions can be transformed into an equivalent network with priority-proportional payments. The transformation increases the representation by at most a polynomial factor. This shows the generality of priority-proportional payment functions. Moreover, it allows applying an existing algorithm for the computation of *maximal* clearing states [[22](https://arxiv.org/html/2602.16387v1#bib.bib34 "On priority-proportional payments in financial networks")] to networks with arbitrary monotone, piecewise-linear payments and default cost. However, the algorithm in [[22](https://arxiv.org/html/2602.16387v1#bib.bib34 "On priority-proportional payments in financial networks")] is technically not polynomial-time since it relies on pushing adjustment steps to the limit to compute the payments for each iteration. Instead, using our approach we can indeed implement the procedure in polynomial time.

Finally, in Section [4](https://arxiv.org/html/2602.16387v1#S4 "4 Claims Trades for Minimal Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") we study *claims trades* as a network adjustment to influence the minimal clearing state. The operation was recently formalized in [[16](https://arxiv.org/html/2602.16387v1#bib.bib47 "Algorithms for claims trading")]. In a claims trade, a given bank ww strives to buy a given claim e=(u,v)e=(u,v) from a creditor bank vv. Formally, ww should pay a return ρ\rho from its external assets to vv and become creditor of claim ee. The goal is to give liquidity to vv and raise the assets of vv in order to mitigate contagion effects as much as possible. In contrast to previous work, we focus on the scenario when the network is evaluated with a minimal clearing state.

Ideally, one would want to compute a return ρ\rho such that *both* vv and ww *strictly* benefit from the trade (w.r.t. the minimal clearing state). We show that this is impossible for all networks with strictly monotone payment functions. We show a novel characterization for banks, for which the clearing state is not unique (Lemma [7](https://arxiv.org/html/2602.16387v1#Thmlemma7 "Lemma 7. ‣ 4 Claims Trades for Minimal Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")). We then focus on creditor-positive trades, in which vv strictly profits but ww stays at least indifferent. For networks with piecewise-linear payment functions, we show how to decide in polynomial time if a creditor-positive claims trade exists, and how to compute one that maximizes the post-trade assets of vv if it exists. Our proof shows that the set of returns that yield creditor-positive trades forms a consecutive interval. Indeed, the largest such return maximizes the assets of vv, and we can find it by a combination of binary search and maximization of suitable LPs.

#### Further Related Work

Algorithmic aspects of the Eisenberg-Noe model for financial networks have become a popular topic in recent years. A *maximal* clearing state can be computed in polynomial time for proportional payments [[12](https://arxiv.org/html/2602.16387v1#bib.bib19 "Systemic risk in financial systems")], even more generally in networks with default cost [[27](https://arxiv.org/html/2602.16387v1#bib.bib30 "Failure and rescue in an interbank network")] and with priority-proportional payments [[22](https://arxiv.org/html/2602.16387v1#bib.bib34 "On priority-proportional payments in financial networks")]. It is known that decentralized update procedures (which essentially implement a bottom-iteration) converge to the *minimal* clearing state [[8](https://arxiv.org/html/2602.16387v1#bib.bib16 "Decentralized clearing in financial networks")], but these approaches do not necessarily run in polynomial time. Up to our knowledge, an efficient algorithm for minimal clearing has been derived only for networks with edge-ranking payments without default cost [[4](https://arxiv.org/html/2602.16387v1#bib.bib63 "Flow allocation games")].

The complexity of computing clearing states has also been considered in an extension of the model to credit-default swaps [[28](https://arxiv.org/html/2602.16387v1#bib.bib26 "Finding clearing payments in financial networks with credit default swaps is PPAD-complete"), [29](https://arxiv.org/html/2602.16387v1#bib.bib32 "Default ambiguity: credit default swaps create new systemic risks in financial networks")], where clearing states exist but their entries are not necessarily rational. Some notions of approximation yield PPAD-hardness results [[28](https://arxiv.org/html/2602.16387v1#bib.bib26 "Finding clearing payments in financial networks with credit default swaps is PPAD-complete")], even for constant approximation factors [[10](https://arxiv.org/html/2602.16387v1#bib.bib1 "Improved hardness results for the clearing problem in financial networks with credit default swaps"), [19](https://arxiv.org/html/2602.16387v1#bib.bib9 "Clearing financial networks with derivatives: from intractability to algorithms")]. Stronger notions of approximation even give rise to FIXP-hardness [[18](https://arxiv.org/html/2602.16387v1#bib.bib24 "Strong approximations and irrationality in financial networks with derivatives"), [20](https://arxiv.org/html/2602.16387v1#bib.bib25 "Financial networks with singleton liability priorities")].

Claims trades have recently been studied in the Eisenberg-Noe model without default cost and with *maximal* clearing [[16](https://arxiv.org/html/2602.16387v1#bib.bib47 "Algorithms for claims trading")]. Since a claims trade can be interpreted as a debt swap operation [[14](https://arxiv.org/html/2602.16387v1#bib.bib64 "Dynamic debt swapping in financial networks"), [25](https://arxiv.org/html/2602.16387v1#bib.bib20 "Debt swapping for risk mitigation in financial networks")], it is impossible that both creditor and buyer banks profit strictly. An optimal creditor-positive trade can be computed in polynomial time for proportional and edge-ranking payment functions. For general functions, it is shown how to compute approximately optimal trades. When trading either multiple incoming or multiple outgoing claims of a single bank, finding optimal trades becomes NP-hard. For incoming claims, there is a bicriteria approximation for all monotone payment functions, for outgoing the problem is NP-hard to approximate within polynomial factors even for edge-ranking functions. These results were extended and improved in a model with *fractional* claims trades, for networks with proportional payments and default cost [[15](https://arxiv.org/html/2602.16387v1#bib.bib48 "Fractional claims trades and donations in financial networks")].

Our paper is related to a growing body of work that studies structural and algorithmic properties of game-theoretic scenarios based on the Eisenberg-Noe model. Aspects that have received attention include, for example, strategic payment allocation [[4](https://arxiv.org/html/2602.16387v1#bib.bib63 "Flow allocation games"), [22](https://arxiv.org/html/2602.16387v1#bib.bib34 "On priority-proportional payments in financial networks"), [17](https://arxiv.org/html/2602.16387v1#bib.bib14 "Seniorities and minimal clearing in financial network games"), [24](https://arxiv.org/html/2602.16387v1#bib.bib27 "Network-aware strategies in financial systems")], forgiving, canceling or forwarding debt [[23](https://arxiv.org/html/2602.16387v1#bib.bib36 "Optimal bailouts and strategic debt forgiveness in financial networks"), [21](https://arxiv.org/html/2602.16387v1#bib.bib44 "Debt transfers in financial networks: complexity and equilibria"), [33](https://arxiv.org/html/2602.16387v1#bib.bib12 "Selfishly cancelling debts can reduce systemic risk")], donations [[34](https://arxiv.org/html/2602.16387v1#bib.bib11 "Reducing systemic risk in financial networks through donations")], prepayments [[36](https://arxiv.org/html/2602.16387v1#bib.bib49 "Selfishly prepaying in financial credit networks")], lending [[11](https://arxiv.org/html/2602.16387v1#bib.bib50 "What is the price for lending in financial networks?")], and more [[3](https://arxiv.org/html/2602.16387v1#bib.bib4 "Equilibria and convergence in fire sale games")]. With the exception of [[17](https://arxiv.org/html/2602.16387v1#bib.bib14 "Seniorities and minimal clearing in financial network games")], all these works consider only maximal clearing states.

More generally, there is work on the complexity of improvement measures for the clearing properties in Eisenberg-Noe financial networks, such as debt swapping [[25](https://arxiv.org/html/2602.16387v1#bib.bib20 "Debt swapping for risk mitigation in financial networks"), [14](https://arxiv.org/html/2602.16387v1#bib.bib64 "Dynamic debt swapping in financial networks")] or portfolio compression. In portfolio compression, a debt cycle is eliminated from the network. For proportional payments, this can have counter-intuitive effects [[30](https://arxiv.org/html/2602.16387v1#bib.bib39 "Portfolio compression in financial networks: incentives and systemic risk"), [35](https://arxiv.org/html/2602.16387v1#bib.bib37 "When does portfolio compression reduce systemic risk?")], and many optimization questions surrounding this operation are NP-hard [[1](https://arxiv.org/html/2602.16387v1#bib.bib38 "Optimal network compression")].

## 2 Model and Preliminaries

#### Network Model

We define a financial network ℱ=(V,E,ℓ,𝐚𝐱)\mathcal{F}=(V,E,\mathbf{\ell},\mathbf{a^{x}}). There is a set VV of nn banks, and a set EE of mm directed edges. Each edge e=(u,v)∈Ee=(u,v)\in E has a non-negative edge weight ℓe\ell\_{e} that represents the *liability* of a claim with debtor uu and creditor vv. Each bank vv has non-negative *external assets* av(x)≥0a^{(x)}\_{v}\geq 0. For simplicity, we assume that the network has no self-loops or multi-edges222These aspects can be incorporated by increasing the notational overhead. We leave the straightforward extension to the interested reader.. We define the set of outgoing and incoming claims of vv by E+​(v)={e=(v,u)∈E∣u∈V}E^{+}(v)=\{e=(v,u)\in E\mid u\in V\} and E−​(v):={e=(u,v)∈E∣u∈V}E^{-}(v):=\{e=(u,v)\in E\mid u\in V\}, respectively. The *total outgoing* and incoming liabilities of bank vv are L+​(v)=∑e∈E+​(v)ℓeL^{+}(v)=\sum\_{e\in E^{+}(v)}\ell\_{e} and L−​(v)=∑e∈E−​(v)ℓeL^{-}(v)=\sum\_{e\in E^{-}(v)}\ell\_{e}, respectively.

#### Payment Functions

The basic solution concept in the Eisenberg-Noe model is a *clearing state*, which defines a consistent set of assets au≥0a\_{u}\geq 0 for each bank u∈Vu\in V. In the standard model, each bank is assumed to clear debt *proportionally*. Thus, with assets aua\_{u}, we have a *recovery rate* min⁡(1,av/L+​(v))\min(1,a\_{v}/L^{+}(v)), such that each claim e=(u,v)e=(u,v) is cleared to the same fractional extent, i.e., pe​(au)=min⁡(1,av/L+​(v))⋅ℓep\_{e}(a\_{u})=\min(1,a\_{v}/L^{+}(v))\cdot\ell\_{e}. Using these payments, the assets have to satisfy the natural asset axioms: The *(total) assets* of each bank are given by the external assets plus the incoming payments of other banks, av(x)+∑(u,v)∈E−​(v)p(u,v)​(au)a\_{v}^{(x)}+\sum\_{(u,v)\in E^{-}(v)}p\_{(u,v)}(a\_{u}) for each v∈Vv\in V. In particular, this implies that no bank will conduct fraud by generating money or holding back assets from paying its open claims.

We consider several extensions of the model. First, we consider the model with *default cost* [[27](https://arxiv.org/html/2602.16387v1#bib.bib30 "Failure and rescue in an interbank network")]. Each bank vv has a *default rates* αv,βv∈[0,1]\alpha\_{v},\beta\_{v}\in[0,1]. If the bank is insolvent, the available assets ava\_{v} that can be used to clear debt are reduced to av(α,β)​(𝐚)=αv​av(x)+βv​∑(u,v)∈E−​(v)p(u,v)​(au)a\_{v}^{(\alpha,\beta)}(\mathbf{a})=\alpha\_{v}a\_{v}^{(x)}+\beta\_{v}\sum\_{(u,v)\in E^{-}(v)}p\_{(u,v)}(a\_{u}). The asset axioms for the vector of total assets 𝐚=(av)v∈V\mathbf{a}=(a\_{v})\_{v\in V} of the banks become

|  |  |  |  |
| --- | --- | --- | --- |
|  | av={av−​(𝐚)if av−​(𝐚)≥L+​(v) (i.e., v solvent), andav(α,β)​(𝐚)otherwise.a\_{v}=\begin{cases}a\_{v}^{-}(\mathbf{a})&\text{if $a\_{v}^{-}(\mathbf{a})\geq L^{+}(v)$ (i.e., $v$ solvent), and}\\ a\_{v}^{(\alpha,\beta)}(\mathbf{a})&\text{otherwise.}\end{cases} |  | (1) |

with the *incoming assets* of vv (before default cost reduction) given by

|  |  |  |
| --- | --- | --- |
|  | av−​(𝐚)=av(x)+∑(u,v)∈E−​(v)p(u,v)​(au).a\_{v}^{-}(\mathbf{a})=a^{(x)}\_{v}+\sum\_{(u,v)\in E^{-}(v)}p\_{(u,v)}(a\_{u}). |  |

and the reduced assets due to default cost given by

|  |  |  |
| --- | --- | --- |
|  | av(α,β)​(𝐚)=αv​av(x)+βv​∑(u,v)∈E−​(v)p(u,v)​(au).a\_{v}^{(\alpha,\beta)}(\mathbf{a})=\alpha\_{v}a^{(x)}\_{v}+\beta\_{v}\sum\_{(u,v)\in E^{-}(v)}p\_{(u,v)}(a\_{u}). |  |

We recover the standard model without default cost when αv=βv=1\alpha\_{v}=\beta\_{v}=1 for all v∈Vv\in V.

Second, we address a general class of monotone payments [[4](https://arxiv.org/html/2602.16387v1#bib.bib63 "Flow allocation games")]. Each bank uu has a *payment function* pe:ℝ→ℝp\_{e}:\mathbb{R}\to\mathbb{R} for each claim e=(u,v)e=(u,v). A payment function satisfies, for each e∈Ee\in E, u∈Uu\in U and au,ε>0a\_{u},\varepsilon>0

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | pe​(au)\displaystyle p\_{e}(a\_{u}) | ∈[0,ℓe]\displaystyle\in[0,\ell\_{e}] |  | (no edge under- or overpaid) |  | (2) |
|  | pe​(au)\displaystyle p\_{e}(a\_{u}) | ≤pe​(au+ε)\displaystyle\leq p\_{e}(a\_{u}+\varepsilon) |  | (monotonicity) |  |
|  | ∑e∈E+​(u)pe​(au)\displaystyle\sum\_{e\in E^{+}(u)}p\_{e}(a\_{u}) | =min⁡{au,L+​(u)}\displaystyle=\min\{a\_{u},L^{+}(u)\} |  | (no fraud) |  |

These constraints imply that all pep\_{e} must be continuous (since pe​(a+δ)−pe​(a)⩽δp\_{e}(a+\delta)-p\_{e}(a)\leqslant\delta for any δ>0\delta>0). The axioms are trivially fulfilled for proportional payments. Many other natural examples of payment functions from this class have been considered, e.g., priority/edge-ranking [[4](https://arxiv.org/html/2602.16387v1#bib.bib63 "Flow allocation games"), [8](https://arxiv.org/html/2602.16387v1#bib.bib16 "Decentralized clearing in financial networks")] (rank edges in an order and pay them sequentially until running out of assets), constrained equal awards or losses [[9](https://arxiv.org/html/2602.16387v1#bib.bib17 "Uniqueness of clearing payment matrices in financial networks")] (all claims receive the same payment or the same non-payment, up their liability) or priority-proportional [[22](https://arxiv.org/html/2602.16387v1#bib.bib34 "On priority-proportional payments in financial networks")] (partition edges into sets, rank sets in an order, pay edges proportionally within each set, and sequentially over sets until running out of assets). All these examples share a natural property – they are *piecewise-linear*. In this paper, we concentrate on the class of monotone, piecewise-linear payment functions.

###### Definition 1.

A *piecewise-linear* payment function pe:ℝ→ℝp\_{e}:\mathbb{R}\to\mathbb{R} for an edge e∈E+​(v)e\in E^{+}(v) is given by ke≥1k\_{e}\geq 1 interval borders 0=xe,0<xe,1<…<xe,ke=L+​(v)<xe,ke+1=∞0=x\_{e,0}<x\_{e,1}<\ldots<x\_{e,k\_{e}}=L^{+}(v)<x\_{e,k\_{e}+1}=\infty and slopes me,i≥0m\_{e,i}\geq 0 for each i=1,…,ke+1i=1,\ldots,k\_{e}+1 such that

|  |  |  |
| --- | --- | --- |
|  | pe​(a)=me,i⋅(a−xe,i−1)+pe​(xe,i−1) for any ​a∈[xe,i−1,xe,i).p\_{e}(a)=m\_{e,i}\cdot(a-x\_{e,i-1})+p\_{e}(x\_{e,i-1})\qquad\text{ for any }a\in[x\_{e,i-1},x\_{e,i}). |  |

Moreover, pep\_{e} adheres to the three axioms in ([2](https://arxiv.org/html/2602.16387v1#S2.E2 "In Payment Functions ‣ 2 Model and Preliminaries ‣ Computing Tarski Fixed Points in Financial Networks")).

Note that pe​(a)=ℓep\_{e}(a)=\ell\_{e} when a≥L+​(v)=xe,kea\geq L^{+}(v)=x\_{e,k\_{e}}. Thus me,ke+1=0m\_{e,k\_{e}+1}=0. We further define me​(a)m\_{e}(a) as the slope me,im\_{e,i} that applies for argument aa, i.e., me​(a)=me,im\_{e}(a)=m\_{e,i} such that a∈[xe,i,xe,i+1)a\in[x\_{e,i},x\_{e,i+1}). This implies that, for every v∈Vv\in V,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑e∈E+​(v)me​(a)={1 for all ​0≤a<L+​(v)0 for all ​a≥L+​(v).\sum\_{e\in E^{+}(v)}m\_{e}(a)=\begin{cases}1&\text{ for all }0\leq a<L^{+}(v)\\ 0&\text{ for all }a\geq L^{+}(v).\end{cases} |  | (3) |

For each bank’s available assets, we define the additional amount of assets until a new interval is reached by δe​(a)=min⁡{xe,i−a​∣xe,i>​a}\delta\_{e}(a)=\min\{x\_{e,i}-a\mid x\_{e,i}>a\}. We denote the total number of interval borders in ℱ\mathcal{F} by k=∑e∈Eke≥mk=\sum\_{e\in E}k\_{e}\geq m. Finally, for a given vector of total assets 𝐚\mathbf{a}, we call an edge e=(u,v)e=(u,v) *active* if me​(au)>0m\_{e}(a\_{u})>0. More generally, the *set of active edges* for 𝐚\mathbf{a} is E𝐚={e∈E∣eE\_{\mathbf{a}}=\{e\in E\mid e is active for 𝐚}\mathbf{a}\}, and the *active graph* is G𝐚=(V,E𝐚)G\_{\mathbf{a}}=(V,E\_{\mathbf{a}}). For each active edge e∈E𝐚e\in E\_{\mathbf{a}}, the *active interval* is the index ii such that pe​(av)∈[xe,i,xe,i+1)p\_{e}(a\_{v})\in[x\_{e,i},x\_{e,i+1}).

uuvvww80802020

20204040606080801001002020404060608080e=(v,u)e=(v,u)e=(v,w)e=(v,w)ava\_{v}pe​(av)p\_{e}(a\_{v})

20204040606080801001002020404060608080e=(v,u)e=(v,u)e=(v,w)e=(v,w)ava\_{v}pe​(av)p\_{e}(a\_{v})

20204040606080801001002020404060608080e=(v,u)e=(v,u)e=(v,w)e=(v,w)ava\_{v}pe​(av)p\_{e}(a\_{v})

Figure 1:  Consider the financial network displayed at the top. Payments of bank vv on each edge for edge-ranking payment functions with (v,w)(v,w) ranked first (left); proportional payment functions (middle); piecewise-linear functions with interval borders 0,50,55,90,100,∞0,50,55,90,100,\infty (right).

#### Clearing States

Given a financial network ℱ\mathcal{F} and piecewise-linear payment functions 𝐩=(pe)e∈E\mathbf{p}=(p\_{e})\_{e\in E}, a *clearing state* is simply a vector of assets 𝐚=(av)v∈V\mathbf{a}=(a\_{v})\_{v\in V} such that all asset axioms ([1](https://arxiv.org/html/2602.16387v1#S2.E1 "In Payment Functions ‣ 2 Model and Preliminaries ‣ Computing Tarski Fixed Points in Financial Networks")) are fulfilled. These axioms are fixed point conditions, since the value of ava\_{v} depends on other aua\_{u} (and potentially vice versa). Consider the space of all potential asset vectors 𝒜=⨉v∈V[0,L−​(v)+av(x)]\mathcal{A}=\bigtimes\_{v\in V}[0,L^{-}(v)+a\_{v}^{(x)}]. We define a function Φ𝐚(x)​(𝐚):𝒜→𝒜\Phi\_{\mathbf{a}^{(x)}}(\mathbf{a}):\mathcal{A}\to\mathcal{A} resulting from applying the map defined by the asset axioms ([1](https://arxiv.org/html/2602.16387v1#S2.E1 "In Payment Functions ‣ 2 Model and Preliminaries ‣ Computing Tarski Fixed Points in Financial Networks")). Φ𝐚(x)\Phi\_{\mathbf{a}^{(x)}} is monotone since all pep\_{e} are monotone. More formally, if 𝐚′≥𝐚\mathbf{a}^{\prime}\geq\mathbf{a} coordinate-wise, then Φ𝐚(x)​(𝐚′)≥Φ𝐚(x)​(𝐚)\Phi\_{\mathbf{a}^{(x)}}(\mathbf{a}^{\prime})\geq\Phi\_{\mathbf{a}^{(x)}}(\mathbf{a}) coordinate-wise. The fixed points of Φ\Phi are the clearing states. Applying the Knaster-Tarski theorem, we see that the set 𝒜f\mathcal{A}\_{f} of fixed points and the coordinate-wise ≥\geq-operation form a complete lattice.

We denote by 𝐚^\hat{\mathbf{a}} the minimal fixed point and by 𝐚ˇ\check{\mathbf{a}} the maximal one. A natural attempt towards computation of 𝐚^\hat{\mathbf{a}} is a *bottom iteration*: Starting from any 𝐚0≤𝐚^\mathbf{a}^{0}\leq\hat{\mathbf{a}} (say, av0=av(x)a\_{v}^{0}=a\_{v}^{(x)} for all v∈Vv\in V) we iteratively compute 𝐚i+1=Φ𝐚(x)​(𝐚i)≤𝐚^\mathbf{a}^{i+1}=\Phi\_{\mathbf{a}^{(x)}}(\mathbf{a}^{i})\leq\hat{\mathbf{a}}. Monotonicity directly implies that 𝐚i+1≥𝐚i\mathbf{a}^{i+1}\geq\mathbf{a}^{i}. In the model without default cost (all default rates αv=βv=1\alpha\_{v}=\beta\_{v}=1) and arbitrary monotone payment functions, it is easy to see that limi→∞𝐚i=𝐚^\lim\_{i\to\infty}\mathbf{a}^{i}=\hat{\mathbf{a}}, but there are simple instances where 𝐚i≠𝐚^\mathbf{a}^{i}\neq\hat{\mathbf{a}} for every i≥0i\geq 0. More generally, when αv\alpha\_{v} or βv<1\beta\_{v}<1 for some v∈Vv\in V, there are simple instances where limi→∞𝐚i≠𝐚^\lim\_{i\to\infty}\mathbf{a}^{i}\neq\hat{\mathbf{a}}. For example, bank vv can be solvent in 𝐚^\hat{\mathbf{a}} but insolvent in 𝐚i\mathbf{a}^{i}, for every i≥0i\geq 0. Then the limit of the total assets of vv is limi→∞avi<L+​(v)≤a^v\lim\_{i\to\infty}a\_{v}^{i}<L^{+}(v)\leq\hat{a}\_{v}. For small examples of the bottom iteration, see Examples [1](https://arxiv.org/html/2602.16387v1#Thmexample1 "Example 1. ‣ Appendix A Examples ‣ Computing Tarski Fixed Points in Financial Networks") and [1](https://arxiv.org/html/2602.16387v1#Thmexample1 "Example 1. ‣ Appendix A Examples ‣ Computing Tarski Fixed Points in Financial Networks") in Appendix [A](https://arxiv.org/html/2602.16387v1#A1 "Appendix A Examples ‣ Computing Tarski Fixed Points in Financial Networks").

#### Claims Trades

An operation to improve clearing states are claims trades. In a claims trade, we are given a claim e=(u,v)e=(u,v) and a potential buyer bank ww. The bank ww buys the claim by paying an amount of external assets ρ\rho to vv. We call ρ\rho the *return*. In turn, the creditor of the claim ee is changed from vv to ww. We assume that the return is upper bounded by ρ≤min⁡{aw(x),ℓ(u,v)}\rho\leq\min\{a^{(x)}\_{w},\ell\_{(u,v)}\}. After the trade, the external assets of ww are aw(x)−ρa\_{w}^{(x)}-\rho and the ones of vv are av(x)+ρa\_{v}^{(x)}+\rho. A claims trade can represent a *donation*, in which ww only transfers ρ\rho external assets without changing any edges in the network333To formulate donations as special cases of claims trades, we may simply assume that ww trades an auxiliary claim (u,v)(u,v) with liability aw(x)a^{(x)}\_{w} and no existing payments from an auxiliary debtor bank uu of vv..

We consider claims trades when the network is evaluated with 𝐚^\hat{\mathbf{a}}. A claims trade is called *creditor-positive* if there exists a return ρ\rho such that the assets of creditor bank vv are strictly improved and the assets of buyer bank ww remain at least the same. We call ρ\rho a *creditor-positive return*. If it exists, we look for an *optimal* one, i.e., a creditor-positive return ρ∗\rho^{\*} that maximizes the post-trade assets of vv. Note that any creditor-positive trade Pareto-improves the assets in the entire network.

## 3 Computing Clearing States

1

Input : Financial network ℱ\mathcal{F}

Output : Minimal clearing state 𝐚^\hat{\mathbf{a}}

2

𝐛(x)←𝟎\mathbf{b}^{(x)}\leftarrow\mathbf{0}, 𝐛←𝟎\mathbf{b}\leftarrow\mathbf{0}

// External and outgoing assets

3
D←{u∈V∣αu<1​ or ​βu<1}D\leftarrow\{u\in V\mid\alpha\_{u}<1\text{ or }\beta\_{u}<1\}

4
Adjust each bank u∈Du\in D with auxiliary banks, reduced external assets, redirected edges

5
while *there is bank v∈Vv\in V with bv(x)<av(x)b^{(x)}\_{v}<a^{(x)}\_{v}* do

6

// Repeated flooding of reachable sink-SCCs

7   
𝒞←\mathcal{C}\leftarrow strongly connected components (SCC) of the active graph G𝐛G\_{\mathbf{b}}

8   
G𝒞←G\_{\mathcal{C}}\leftarrow directed acyclic graph of SCCs of G𝐛G\_{\mathbf{b}}

9   
while *there is non-singleton C∈𝒞C\in\mathcal{C} that is reachable from vv and a sink in G𝒞G\_{\mathcal{C}}* do

10      
Solve Flood-LP ([5](https://arxiv.org/html/2602.16387v1#S3.E5 "In Flooding SCCs ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")), let 𝐝∗\mathbf{d}^{\*} be the optimal solution

11      
𝐛←𝐛+𝐝∗\mathbf{b}\leftarrow\mathbf{b}+\mathbf{d}^{\*}

12      
Update G𝐛G\_{\mathbf{b}}, 𝒞\mathcal{C}, and G𝒞G\_{\mathcal{C}}

13

14

// Raise external assets of vv

15   
Solve Increase-LP ([6](https://arxiv.org/html/2602.16387v1#S3.E6 "In Increasing External Assets ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")), let (δ∗,𝐝∗)(\delta^{\*},\mathbf{d}^{\*}) be an optimal solution

16   
bv(x)←bv(x)+δ∗b^{(x)}\_{v}\leftarrow b^{(x)}\_{v}+\delta^{\*} and 𝐛←𝐛+𝐝∗\mathbf{b}\leftarrow\mathbf{b}+\mathbf{d}^{\*}

17

// Adjust the network for banks with default cost

18   
forall *banks u∈Du\in D that became solvent* do

19      
bw(x)←bw(x)+pe​(bu)b\_{w}^{(x)}\leftarrow b\_{w}^{(x)}+p\_{e}(b\_{u}), for each e=(u,w)∈Ee=(u,w)\in E

20      
aw(x)←aw(x)+ℓea^{(x)}\_{w}\leftarrow a^{(x)}\_{w}+\ell\_{e}, for each e=(u,w)∈Ee=(u,w)\in E

21      
Remove all edges e=(u,w)e=(u,w) from ℱ\mathcal{F}

22

23

return *𝐛\mathbf{b}*

Algorithm 1  Computation of a minimal clearing state

### 3.1 Minimal Clearing State

In this section, we explain our algorithm to compute a minimal clearing state. The standard approach to computing minimal Tarski fixed points is a bottom iteration, but implementing this directly in financial networks is not effective. Instead of a standard bottom iteration, Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") maintains and increases a vector 𝐛(x)\mathbf{b}^{(x)} of *reduced external assets*. It starts at 𝐛(x)=𝟎\mathbf{b}^{(x)}=\mathbf{0} and approaches the vector of actual external assets from below, i.e., 𝐛(x)≤𝐚(x)\mathbf{b}^{(x)}\leq\mathbf{a}^{(x)}. In each iteration of the main while-loop, the algorithm computes an increase of reduced external assets at one vertex vv. It also maintains a vector 𝐛\mathbf{b} of total assets. For a small example run of the algorithm, see Example [3](https://arxiv.org/html/2602.16387v1#Thmexample3 "Example 3. ‣ Appendix A Examples ‣ Computing Tarski Fixed Points in Financial Networks") in Appendix [A](https://arxiv.org/html/2602.16387v1#A1 "Appendix A Examples ‣ Computing Tarski Fixed Points in Financial Networks").

For the analysis, we will maintain the invariant that at the beginning of an iteration of the main while-loop, 𝐛\mathbf{b} is a minimal clearing state of the network ℱ\mathcal{F} with the reduced external assets 𝐛(x)\mathbf{b}^{(x)}.

###### Lemma 1.

At the beginning of each iteration of the main while-loop, 𝐛(x)≤𝐚(x)\mathbf{b}^{(x)}\leq\mathbf{a}^{(x)} and 𝐛\mathbf{b} is a minimal clearing state of the financial network ℱ\mathcal{F} with external assets 𝐛(x)\mathbf{b}^{(x)}.

For clarity of exposition, we first prove correctness of our algorithm when there is no default cost, i.e., all default rates are αv=βv=1\alpha\_{v}=\beta\_{v}=1. We then outline the adjustments for general default rates in Section [3.2](https://arxiv.org/html/2602.16387v1#S3.SS2 "3.2 Default Cost ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") below. In particular, without default cost, D=∅D=\emptyset in line [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks"), we make no adjustments in lines [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks"), and we never execute lines [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")-[1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks").

For the proof of Lemma [1](https://arxiv.org/html/2602.16387v1#Thmlemma1 "Lemma 1. ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks"), the properties clearly hold in the beginning since 𝐛(x)=𝐛=𝟎\mathbf{b}^{(x)}=\mathbf{b}=\mathbf{0}. Suppose they are true at the beginning of iteration ii. We argue that the properties hold in the end of iteration ii, i.e., at the beginning of iteration i+1i+1. Our first insight shows that the minimal clearing state is non-decreasing in the external assets of each bank.

###### Lemma 2.

Consider a financial network ℱ\mathcal{F}. Suppose all banks have reduced external assets 𝟎≤𝐛(x)≤𝐚(x)\mathbf{0}\leq\mathbf{b}^{(x)}\leq\mathbf{a}^{(x)}. If au(x)>bu(x)a^{(x)}\_{u}>b^{(x)}\_{u}, then in the minimal clearing state 𝐛^\hat{\mathbf{b}} resulting from 𝐛(x)\mathbf{b}^{(x)} we have a^u>b^u\hat{a}\_{u}>\hat{b}\_{u}.

###### Proof.

For contradiction, assume that a^u≤b^u\hat{a}\_{u}\leq\hat{b}\_{u}. Consider the pointwise minimum 𝐛′=𝐚^∧𝐛^\mathbf{b}^{\prime}=\hat{\mathbf{a}}\land\hat{\mathbf{b}}, i.e., bv′=min⁡{a^v,b^v}b^{\prime}\_{v}=\min\{\hat{a}\_{v},\hat{b}\_{v}\} for all v∈Vv\in V. Since 𝐛′≤𝐛^\mathbf{b}^{\prime}\leq\hat{\mathbf{b}}, the bottom iteration shows that Φ𝐛(x)​(𝐛′)≥𝐛′\Phi\_{\mathbf{b}^{(x)}}(\mathbf{b}^{\prime})\geq\mathbf{b}^{\prime}. Now 𝐚^≥𝐛′\hat{\mathbf{a}}\geq\mathbf{b}^{\prime}, au(x)>bu(x)a^{(x)}\_{u}>b^{(x)}\_{u} and Φ\Phi is strictly monotone with respect to external assets and weakly monotone with respect to total assets. This implies that

|  |  |  |
| --- | --- | --- |
|  | Φ𝐚(x)​(𝐚^)u>Φ𝐛(x)​(𝐚^)u≥Φ𝐛(x)​(𝐛′)u≥𝐛u′=a^u.\Phi\_{\mathbf{a}^{(x)}}(\hat{\mathbf{a}})\_{u}>\Phi\_{\mathbf{b}^{(x)}}(\hat{\mathbf{a}})\_{u}\geq\Phi\_{\mathbf{b}^{(x)}}(\mathbf{b}^{\prime})\_{u}\geq\mathbf{b}^{\prime}\_{u}=\hat{a}\_{u}. |  |

Thus, 𝐚^\hat{\mathbf{a}} is not a clearing state – a contradiction.
∎

#### Flooding SCCs

Now consider the bank vv with bv(x)<av(x)b^{(x)}\_{v}<a^{(x)}\_{v} chosen for the increase in iteration ii of the main while-loop. Let us concentrate on regions of the active graph G𝐛G\_{\mathbf{b}} that are reachable from vv and strongly connected.

###### Definition 2.

We define a *phase* as a subset of asset vectors 𝒫⊆𝒜\mathcal{P}\subseteq\mathcal{A} such that for all 𝐚,𝐚′∈𝒫\mathbf{a},\mathbf{a}^{\prime}\in\mathcal{P} we have the same active edges E𝐚=E𝐚′E\_{\mathbf{a}}=E\_{\mathbf{a}^{\prime}}, and for each e∈E𝐚e\in E\_{\mathbf{a}}, the same active interval in 𝐚\mathbf{a} and 𝐚′\mathbf{a}^{\prime}.

###### Definition 3.

We say *vv causes a flood in G𝐛G\_{\mathbf{b}}* if there is a strongly connected component C⊆VC\subseteq V of G𝐛G\_{\mathbf{b}} that is (1) reachable from vv, (2) non-singleton, and (3) a sink-component, i.e., does not have outgoing edges to banks outside CC.

###### Lemma 3.

Suppose we increase the external assets of bank vv from bv(x)b^{(x)}\_{v} to bv(x)+εb^{(x)}\_{v}+\varepsilon for some positive amount 0<ε≤av(x)−bv(x)0<\varepsilon\leq a^{(x)}\_{v}-b^{(x)}\_{v}. Let 𝐛′\mathbf{b}^{\prime} be the new minimal clearing state after the increase. If vv causes a flood in G𝐛G\_{\mathbf{b}}, then 𝐛′\mathbf{b}^{\prime} cannot be in the same phase as 𝐛\mathbf{b}, for any ε>0\varepsilon>0.

###### Proof.

By Lemma [2](https://arxiv.org/html/2602.16387v1#Thmlemma2 "Lemma 2. ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks"), we know that in the minimal clearing states bv′>bvb^{\prime}\_{v}>b\_{v}. As a consequence, each active outgoing edge e=(v,w)e=(v,w) must have strictly higher payments in 𝐛′\mathbf{b}^{\prime}, i.e., pe​(bv′)>pe​(bv)p\_{e}(b^{\prime}\_{v})>p\_{e}(b\_{v}) because the slope me​(bv)>0m\_{e}(b\_{v})>0. This shows

|  |  |  |  |
| --- | --- | --- | --- |
|  | bw′\displaystyle b^{\prime}\_{w} | =bw(x)+pe​(bv′)+∑(u,w)∈Ep(u,w)​(bu′)≥bw(x)+pe​(bv′)+∑(u,w)∈Ep(u,w)​(bu)\displaystyle=b^{(x)}\_{w}+p\_{e}(b^{\prime}\_{v})+\sum\_{(u,w)\in E}p\_{(u,w)}(b^{\prime}\_{u})\geq b^{(x)}\_{w}+p\_{e}(b^{\prime}\_{v})+\sum\_{(u,w)\in E}p\_{(u,w)}(b\_{u}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | >bw(x)+pe​(bv)+∑(u,w)∈Ep(u,w)​(bu)=bw\displaystyle>b^{(x)}\_{w}+p\_{e}(b\_{v})+\sum\_{(u,w)\in E}p\_{(u,w)}(b\_{u})=b\_{w} |  |

Consider the sets of banks and active edges reachable from vv in G𝐛G\_{\mathbf{b}}. Applying the insight inductively shows that every reachable bank has strictly higher total assets, and every reachable active edge strictly higher payments in 𝐛′\mathbf{b}^{\prime} than in 𝐛\mathbf{b}, respectively.

Now, suppose for contradiction that 𝐛′>𝐛\mathbf{b}^{\prime}>\mathbf{b} and both minimal clearing states are in the same phase. Consider a non-singleton sink-SCC CC reachable from vv. For every bank w∈Cw\in C, we consider dw=bw′−bw>0d\_{w}=b^{\prime}\_{w}-b\_{w}>0. CC is not a singleton, so all banks ww in CC are insolvent. 𝐛′\mathbf{b}^{\prime} and 𝐛\mathbf{b} are in the same phase, so ([3](https://arxiv.org/html/2602.16387v1#S2.E3 "In Payment Functions ‣ 2 Model and Preliminaries ‣ Computing Tarski Fixed Points in Financial Networks")) implies that all of dwd\_{w} gets paid to out-neighbors in CC. In turn, these payments become additional incoming assets at other nodes of CC. Summing over all additional incoming assets of w∈Cw\in C from neighbors of CC, we see that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑w∈Cdw≤∑w∈C∑v′∈C(v′,w)∈E𝐛−​(w)m(v′,w)​(bv′′)⋅dv′\sum\_{w\in C}d\_{w}\leq\sum\_{w\in C}\sum\_{\begin{subarray}{c}v^{\prime}\in C\\ (v^{\prime},w)\in E\_{\mathbf{b}}^{-}(w)\end{subarray}}m\_{(v^{\prime},w)}(b^{\prime}\_{v^{\prime}})\cdot d\_{v^{\prime}} |  | (4) |

Now let ww be a node of CC that is closest to vv, and let (u,w)(u,w) be an edge on a shortest vv-ww-path in G𝐛G\_{\mathbf{b}}. Since uu is reachable from vv, we know that bu′>bub^{\prime}\_{u}>b\_{u}. If v∈Cv\in C, then we can assume u=vu=v, and since CC is non-singleton, an out-neighbor w∈Cw\in C with (v,w)∈E(v,w)\in E must exist. Let d(u,w)=p(u,w)​(bu′)−p(u,w)​(bu)d\_{(u,w)}=p\_{(u,w)}(b^{\prime}\_{u})-p\_{(u,w)}(b\_{u}), then d(u,w)>0d\_{(u,w)}>0. Since 𝐛′\mathbf{b}^{\prime} is a clearing state, the asset axiom holds for ww. As such, the additional assets dwd\_{w} are lower bounded by the sum of additional incoming assets over (u,w)(u,w) and from in-neighbors of CC, i.e.,

|  |  |  |
| --- | --- | --- |
|  | dw≥d(u,w)+∑v′∈C(v′,w)∈E𝐛−​(w)m(v′,w)​(bv′′)⋅dv′>∑v′∈C(v′,w)∈E𝐛−​(w)m(v′,w)​(bv′′)⋅dv′\displaystyle d\_{w}\geq d\_{(u,w)}+\sum\_{\begin{subarray}{c}v^{\prime}\in C\\ (v^{\prime},w)\in E\_{\mathbf{b}}^{-}(w)\end{subarray}}m\_{(v^{\prime},w)}(b^{\prime}\_{v^{\prime}})\cdot d\_{v^{\prime}}\;>\;\sum\_{\begin{subarray}{c}v^{\prime}\in C\\ (v^{\prime},w)\in E\_{\mathbf{b}}^{-}(w)\end{subarray}}m\_{(v^{\prime},w)}(b^{\prime}\_{v^{\prime}})\cdot d\_{v^{\prime}} |  |

With ([4](https://arxiv.org/html/2602.16387v1#S3.E4 "In Proof. ‣ Flooding SCCs ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")) this proves that there must be some bank w′∈Cw^{\prime}\in C such that

|  |  |  |
| --- | --- | --- |
|  | dw′<∑v′∈C(v′,w′)∈E𝐛−​(w′)m(v′,w′)​(bv′′)⋅dv′,d\_{w^{\prime}}<\sum\_{\begin{subarray}{c}v^{\prime}\in C\\ (v^{\prime},w^{\prime})\in E\_{\mathbf{b}}^{-}(w^{\prime})\end{subarray}}m\_{(v^{\prime},w^{\prime})}(b^{\prime}\_{v^{\prime}})\cdot d\_{v^{\prime}}, |  |

i.e., the additional assets of w′w^{\prime} are *strictly less* than its additional incoming assets from CC. Thus, 𝐛′\mathbf{b}^{\prime} is not a clearing state – a contradiction.
∎

𝐛′\mathbf{b}^{\prime} cannot be in the same phase as 𝐛\mathbf{b}, since raising the external assets at vv would leave only inconsistent assignments of assets for every reachable, non-singleton, sink-SCC CC. Then again, CC is reachable and external assets of vv must be increased to obtain 𝐚^\hat{\mathbf{a}}, so the assets in CC must also grow. Therefore, we have to raise the clearing state 𝐛\mathbf{b} within CC to escape the current phase and eventually enable an increase of external assets at vv. In Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks"), we raise the assets in CC by a minimal circulation that maintains the properties of a clearing state (i.e., additional incoming assets are additional outgoing assets) and suffices to advance to the next phase. This is achieved by solving the following LP. We term this a *flooding* of CC with assets. Recall that δe​(a)\delta\_{e}(a) is the smallest amount of additional assets required to advance the payment function pep\_{e} to the next interval.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Max. | ∑w∈Cdw\displaystyle\sum\_{w\in C}d\_{w} |  | | (5) |
|  | s.t. | dw=∑v′∈C(v′,w)∈E𝐛−​(w)m(v′,w)​(bv′)⋅dv′\displaystyle d\_{w}=\sum\_{\begin{subarray}{c}v^{\prime}\in C\\ (v^{\prime},w)\in E\_{\mathbf{b}}^{-}(w)\end{subarray}}m\_{(v^{\prime},w)}(b\_{v^{\prime}})\cdot d\_{v^{\prime}} | ∀w∈C\displaystyle\forall w\in C |  |
|  |  | dw≤δe​(bw)\displaystyle d\_{w}\leq\delta\_{e}(b\_{w}) | ∀e∈E𝐛+​(w)\displaystyle\forall e\in E\_{\mathbf{b}}^{+}(w) |  |
|  |  | dw≥0\displaystyle d\_{w}\geq 0 | ∀w∈C\displaystyle\forall w\in C |  |

#### Solving LP ([5](https://arxiv.org/html/2602.16387v1#S3.E5 "In Flooding SCCs ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks"))

Let us define the weighted |C|×|C||C|\times|C| adjacency matrix 𝐌\mathbf{M} for component CC with entries mv′,w=m(v′,w)​(bv′)m\_{v^{\prime},w}=m\_{(v^{\prime},w)}(b\_{v^{\prime}}). CC being a SCC and property ([3](https://arxiv.org/html/2602.16387v1#S2.E3 "In Payment Functions ‣ 2 Model and Preliminaries ‣ Computing Tarski Fixed Points in Financial Networks")) imply that 𝐌\mathbf{M} is row-stochastic and irreducible. The first set of constraints can be written as 𝐝=𝐝𝐌\mathbf{d}=\mathbf{d}\mathbf{M}. Thus, 𝐝\mathbf{d} is an eigenvector of 𝐌\mathbf{M} with eigenvalue 1. The Perron-Frobenius theorem implies 𝐝\mathbf{d} is non-negative and unique. Thus, we can construct 𝐌\mathbf{M}, compute 𝐝\mathbf{d} and scale it to the largest multiple such that all constraints dw≤δe​(bw)d\_{w}\leq\delta\_{e}(b\_{w}) are satisfied. Note that power iteration methods for approximating 𝐝\mathbf{d} might not be applicable since 𝐌\mathbf{M} is not necessarily aperiodic.

#### Increasing External Assets

Flooding of components monotonically increases the assets and changes the phase, but leaves the external assets of vv untouched. Thus, after a finite number of repetitions, we must reach a clearing state 𝐛<𝐚^\mathbf{b}<\hat{\mathbf{a}} such that all sink-SCCs reachable from vv are singletons, i.e., solvent banks. In this case, the next lemma shows that there exists a sufficiently small δ>0\delta>0 such that for any increase of external assets of vv to less than bv(x)+δb^{(x)}\_{v}+\delta, the resulting minimal clearing state 𝐛′\mathbf{b}^{\prime} remains in the phase of 𝐛\mathbf{b}.

###### Lemma 4.

Suppose we increase the external assets of bank vv from bv(x)b^{(x)}\_{v} to bv(x)+εb^{(x)}\_{v}+\varepsilon for some positive amount 0<ε≤av(x)−bv(x)0<\varepsilon\leq a^{(x)}\_{v}-b^{(x)}\_{v}. Let 𝐛′\mathbf{b}^{\prime} be the new minimal clearing state after the increase. If vv does not cause a flood in G𝐛G\_{\mathbf{b}}, there is a δ>0\delta>0 such that 𝐛′\mathbf{b}^{\prime} is in the same phase as 𝐛\mathbf{b}, for every ε<δ\varepsilon<\delta.

Proof.
Similar to our observation above, we consider the additional assets dw=bw′−bw≥0d\_{w}=b^{\prime}\_{w}-b\_{w}\geq 0. Since the external assets of vv are strictly increased, we see that dv>0d\_{v}>0. As 𝐛′\mathbf{b}^{\prime} is a minimal clearing state, we can assume all banks uu that are not reachable from vv maintain their current assets and have du=0d\_{u}=0, as they remain unaffected from the increase in external assets at vv. Assuming that 𝐛′\mathbf{b}^{\prime} and 𝐛\mathbf{b} are in the same phase, the largest increase in the external assets of vv is given by LP ([6](https://arxiv.org/html/2602.16387v1#S3.E6 "In Increasing External Assets ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")) below. The first set of equalities asserts that the increase in assets of vv is given by the additional external assets and the additional incoming assets over edges from E𝐛−​(v)E\_{\mathbf{b}}^{-}(v). Similarly, for banks that are reachable from vv, the increase in assets is given by the increase in incoming assets. Clearly, av(x)−bv(x)a\_{v}^{(x)}-b\_{v}^{(x)} is a trivial upper bound on the maximum increase. To stay in the same phase, we ensure that the (open) active interval on each edge remains the same, which yields a (strict) upper bound of δe​(bw)\delta\_{e}(b\_{w}) for each e=(u,w)∈E𝐛e=(u,w)\in E\_{\mathbf{b}}. Using weak inequalities, the optimum solution represents the supremum δ\delta as stated in the lemma. It represents the smallest increase to advance the minimal clearing state to the next phase when increasing the external assets of vv.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Max. | δ\displaystyle\delta |  | | (6) |
|  | s.t. | dv=δ+∑(u,v)∈E𝐛−​(v)m(u,v)​(bu)⋅du\displaystyle d\_{v}=\delta+\sum\_{(u,v)\in E^{-}\_{\mathbf{b}}(v)}m\_{(u,v)}(b\_{u})\cdot d\_{u} |  | |
|  |  | dw=∑(u,w)∈E𝐛−​(w)m(u,v)​(bu)⋅dw\displaystyle d\_{w}=\sum\_{(u,w)\in E^{-}\_{\mathbf{b}}(w)}m\_{(u,v)}(b\_{u})\cdot d\_{w} | for all w≠vw\neq v reachable from vv |  |
|  |  | dw=0\displaystyle d\_{w}=0 | for all w≠vw\neq v unreachable from vv |  |
|  |  | dw≤δe​(bw)\displaystyle d\_{w}\leq\delta\_{e}(b\_{w}) | ∀e∈E𝐛+​(w)\displaystyle\forall e\in E\_{\mathbf{b}}^{+}(w) |  |
|  |  | δ≤av(x)−bv(x)\displaystyle\delta\leq a^{(x)}\_{v}-b^{(x)}\_{v} |  | |
|  |  | dw≥0\displaystyle d\_{w}\geq 0 | ∀w∈V\displaystyle\forall w\in V |  |

To show correctness, we argue that the LP indeed allows a unique optimal solution (δ∗,𝐝∗)(\delta^{\*},\mathbf{d}^{\*}). We can restrict attention to the set U⊆VU\subseteq V of banks that are reachable from vv in G𝐛G\_{\mathbf{b}}. Then the first two constraints in ([6](https://arxiv.org/html/2602.16387v1#S3.E6 "In Increasing External Assets ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")) above compose a system of linear equations describing the asset increase that can be expressed by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐝=δ⋅𝐞v+𝐝​𝐌.\mathbf{d}=\delta\cdot\mathbf{e}\_{v}+\mathbf{d}\;\mathbf{M}. |  | (7) |

Here 𝐝\mathbf{d} is an |U||U|-dimensional row vector with entries dud\_{u}, 𝐞v\mathbf{e}\_{v} is an |U||U|-dimensional unit row vector with entry 11 for vv and 0 otherwise, and 𝐌\mathbf{M} is an |U||U|-dimensional square matrix with entries mu,w=m(u,w)​(bu)m\_{u,w}=m\_{(u,w)}(b\_{u}) for all (u,w)∈E𝐛,u∈U(u,w)\in E\_{\mathbf{b}},u\in U, and 0 otherwise. The vector 𝐝\mathbf{d} can be given by

|  |  |  |
| --- | --- | --- |
|  | 𝐝=(𝐈−𝐌)−1​δ⋅𝐞v.\mathbf{d}=(\mathbf{I}-\mathbf{M})^{-1}\;\delta\cdot\mathbf{e}\_{v}\kern 5.0pt. |  |

Let us observe that the inverse exists. By ([3](https://arxiv.org/html/2602.16387v1#S2.E3 "In Payment Functions ‣ 2 Model and Preliminaries ‣ Computing Tarski Fixed Points in Financial Networks")), 𝐈−𝐌\mathbf{I}-\mathbf{M} is weakly diagonally dominant. Since vv does not cause a flood, every bank u∈Uu\in U has a path to a solvent bank in G𝐛G\_{\mathbf{b}}. Rows corresponding to solvent banks are strictly diagonally dominant. These properties give rise to a chained variant of diagonal dominance [[2](https://arxiv.org/html/2602.16387v1#bib.bib2 "Weakly chained matrices, policy iteration, and impulse control")] and imply that 𝐈−𝐌\mathbf{I}-\mathbf{M} is invertible [[31](https://arxiv.org/html/2602.16387v1#bib.bib3 "A sufficient condition for nonvanishing of determinants")].

Thus, the increase in the assets of the minimal clearing state scales linearly in the increase of bv(x)b\_{v}^{(x)}. Since all active intervals of 𝐛\mathbf{b} are open, for every sufficiently small value of δ>0\delta>0, the resulting asset vector 𝐛+𝐝\mathbf{b}+\mathbf{d} indeed remains in the same phase. In particular, let

|  |  |  |
| --- | --- | --- |
|  | 𝐬=(𝐈−𝐌)−1⋅𝐞v\mathbf{s}=(\mathbf{I}-\mathbf{M})^{-1}\cdot\mathbf{e}\_{v} |  |

be the vector of slopes. For the supremum for all increases that keep 𝐛+𝐝\mathbf{b}+\mathbf{d} in the same phase, we require du=su​δ≤δ(u,w)​(bu)d\_{u}=s\_{u}\delta\leq\delta\_{(u,w)}(b\_{u}) for all (u,w)∈E𝐛(u,w)\in E\_{\mathbf{b}}, which are the fourth set of constraints in ([6](https://arxiv.org/html/2602.16387v1#S3.E6 "In Increasing External Assets ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")). Clearly, we also require δ≤av(x)−bv(x)\delta\leq a\_{v}^{(x)}-b\_{v}^{(x)}, the maximal increase in external assets of vv. The lemma follows using

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ=min⁡{av(x)−bv(x),min(u,w)∈E𝐛⁡δ(u,w)​(bu)/su}>0.∎\delta=\min\{a\_{v}^{(x)}-b\_{v}^{(x)},\min\_{(u,w)\in E\_{\mathbf{b}}}\delta\_{(u,w)}(b\_{u})/s\_{u}\}>0.\qed |  | (8) |

#### Solving LP ([6](https://arxiv.org/html/2602.16387v1#S3.E6 "In Increasing External Assets ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks"))

The proof of the previous lemma shows that to solve the LP, we can compute the set UU of reachable banks and set up the matrix (𝐈−𝐌)(\mathbf{I}-\mathbf{M}). We then solve (𝐈−𝐌)​𝐬=𝐞v(\mathbf{I}-\mathbf{M})\mathbf{s}=\mathbf{e}\_{v} (e.g., by Gaussian elimination) to obtain the slopes 𝐬\mathbf{s}, and determine δ\delta by computing the minima in ([8](https://arxiv.org/html/2602.16387v1#S3.E8 "In Increasing External Assets ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")).

#### Correctness and Polynomial Time

We are now ready to prove Lemma [1](https://arxiv.org/html/2602.16387v1#Thmlemma1 "Lemma 1. ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") as the main invariant of the algorithm.

###### Proof of Lemma [1](https://arxiv.org/html/2602.16387v1#Thmlemma1 "Lemma 1. ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks").

Consider round ii of the while-loop and the vertex vv chosen for the increase in external assets bv(x)b\_{v}^{(x)}. Suppose vv causes a flood. Lemma [3](https://arxiv.org/html/2602.16387v1#Thmlemma3 "Lemma 3. ‣ Flooding SCCs ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") shows that by repeatedly flooding the corresponding sink-SCCs, we maintain a clearing state that remains below any minimal clearing state resulting from any strict increase in bv(x)b\_{v}^{(x)}.

There can only be a finite number of flooding operations. Afterwards, the proof of Lemma [4](https://arxiv.org/html/2602.16387v1#Thmlemma4 "Lemma 4. ‣ Increasing External Assets ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") reveals that the increase in the minimal clearing state is linear in the increase in external assets of vv. We execute the smallest increase δ\delta that either yields bv(x)+δ=av(x)b\_{v}^{(x)}+\delta=a\_{v}^{(x)} or changes the phase. In any case, in the beginning of iteration i+1i+1, the vector 𝐛\mathbf{b} is again the minimal clearing state for ℱ\mathcal{F} with the larger vector of external assets 𝐛(x)\mathbf{b}^{(x)}.
∎

###### Theorem 1.

Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") computes the minimal clearing state of a given financial network without default cost in time O​((n+k)⋅(n3+m))O((n+k)\cdot(n^{3}+m)).

###### Proof.

Lemma [1](https://arxiv.org/html/2602.16387v1#Thmlemma1 "Lemma 1. ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") shows that Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") computes the correct minimal clearing state. Regarding the running time, computing the active graph can be done in time O​(n+m)O(n+m). Finding a reachable, non-singleton, sink-SCC (or verifying that none exists) can be done in time O​(n+m)O(n+m) using standard depth-first-search methods. Solving LPs ([5](https://arxiv.org/html/2602.16387v1#S3.E5 "In Flooding SCCs ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")) and ([6](https://arxiv.org/html/2602.16387v1#S3.E6 "In Increasing External Assets ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")) requires polynomial time. The running times for this are dominated by the computation of the eigenvector 𝐝∗\mathbf{d}^{\*} and solving linear equations for vector 𝐬\mathbf{s}, respectively. Each of these requires at most time O​(n3)O(n^{3}). Upon solution of any of these two LPs, we advance to a new phase or meet the desired external assets of a bank. Thus, the number of times we need to solve an LP is upper bounded by O​(n+k)O(n+k).
∎

### 3.2 Default Cost

We now turn to the extension of Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") to banks with default cost. We explain and justify the adjustments made in lines [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")-[1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") and lines [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")-[1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") of the Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks").

###### Lemma 5.

For each financial network ℱ\mathcal{F} with minimal clearing state 𝐚^\hat{\mathbf{a}} and default cost, there is a network ℱ′\mathcal{F}^{\prime} without default cost with a minimal clearing state 𝐚^′\hat{\mathbf{a}}^{\prime} equivalent to 𝐚^\hat{\mathbf{a}}.

###### Proof.

We implement default cost reductions of all banks in DD by adjusting the network ℱ\mathcal{F}.

A bank with αu=βu=0\alpha\_{u}=\beta\_{u}=0 makes no payments. Hence, we can w.l.o.g. assume it has no outgoing edges in ℱ\mathcal{F}. Omitting the default cost reduction for the assets of uu is inconsequential for the remaining clearing state.

Now consider bank uu with αu⋅βu>0\alpha\_{u}\cdot\beta\_{u}>0 that is insolvent in 𝐚^\hat{\mathbf{a}}. We adjust the network ℱ\mathcal{F} to ℱ′\mathcal{F}^{\prime} as follows. We assume uu has external assets αu​au(x)≤au(x)\alpha\_{u}a\_{u}^{(x)}\leq a\_{u}^{(x)}. We create two auxiliary banks usu\_{s} and utu\_{t}. usu\_{s} shall collect all incoming payments for uu. It then directs a (1−βu)(1-\beta\_{u})-portion to an auxiliary sink bank utu\_{t} and the remaining βv\beta\_{v}-portion to uu. Towards this end, all incoming edges (v,u)(v,u) are re-routed to (v,us)(v,u\_{s}). There are new edges e1=(us,ut)e\_{1}=(u\_{s},u\_{t}) and e2=(us,u)e\_{2}=(u\_{s},u) with liability ℓe1=(1−βu)​Lu+\ell\_{e\_{1}}=(1-\beta\_{u})L^{+}\_{u} and ℓe2=βu​Lu+\ell\_{e\_{2}}=\beta\_{u}L^{+}\_{u}. usu\_{s} has a proportional payment function. All other banks and payments remain as in ℱ\mathcal{F}. We assume that uu, usu\_{s} and utu\_{t} have no default cost in ℱ′\mathcal{F}^{\prime}.

In ℱ′\mathcal{F}^{\prime}, a default cost reduction of αu\alpha\_{u} is directly incorporated into the external assets of uu. For the reduction of βu\beta\_{u} in incoming payments, the auxiliary bank usu\_{s} splits off the default cost and sends the corresponding assets to an auxiliary sink utu\_{t}. It is straightforward to verify that 𝐚^′\hat{\mathbf{a}}^{\prime} with av′=ava\_{v}^{\prime}=a\_{v} for each v∈Vv\in V and the direct extension to the assets of auxiliary banks aus′=∑(v,u)∈Epe​(au′)a^{\prime}\_{u\_{s}}=\sum\_{(v,u)\in E}p\_{e}(a^{\prime}\_{u}) and aut′=(1−βu)​aus′a^{\prime}\_{u\_{t}}=(1-\beta\_{u})a^{\prime}\_{u\_{s}} is a clearing state in ℱ′\mathcal{F}^{\prime}. Any smaller clearing state 𝐛′\mathbf{b}^{\prime} in ℱ′\mathcal{F}^{\prime} can be mapped back to a smaller clearing state 𝐛=(bv′)v∈V\mathbf{b}=(b^{\prime}\_{v})\_{v\in V} for all v∈Vv\in V (excluding the auxiliary banks). This proves the statement for insolvent banks.

For a bank u∈Du\in D that is solvent in 𝐚^\hat{\mathbf{a}}, we have pe​(a^u)=ℓep\_{e}(\hat{a}\_{u})=\ell\_{e} for all e=(u,v)∈Ee=(u,v)\in E. We can remove all outgoing edges (u,v)∈E(u,v)\in E and raise the external assets of each out-neighbor vv by ℓ(u,v)\ell\_{(u,v)}. This creates an equivalent network ℱ′\mathcal{F}^{\prime} for which 𝐚^′=𝐚^\hat{\mathbf{a}}^{\prime}=\hat{\mathbf{a}} remains the minimal clearing state. This proves the statement for solvent banks.
∎

###### Corollary 1.

Using the adjustment in Lemma [5](https://arxiv.org/html/2602.16387v1#Thmlemma5 "Lemma 5. ‣ 3.2 Default Cost ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks"), Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") computes the minimal clearing state of a given financial network with default cost in time O​((k+n+m)⋅(n3+m))O((k+n+m)\cdot(n^{3}+m)).

###### Proof.

In the algorithm, all banks are insolvent initially. Thus, we adjust the network in lines [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")-[1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") according to Lemma [5](https://arxiv.org/html/2602.16387v1#Thmlemma5 "Lemma 5. ‣ 3.2 Default Cost ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") and apply the algorithm in network ℱ′\mathcal{F}^{\prime}, where all banks of DD have been adjusted. The introduction of sink banks utu\_{t} shows that, in particular, no (insolvent) bank u∈Du\in D can be part of any non-singleton sink-SCC. Thus, the flooding step is relevant only for components of banks without default cost.

The representation becomes problematic when a bank u∈Du\in D becomes solvent w.r.t. the liabilities in ℱ\mathcal{F}. Then all outgoing edges e∈E+​(u)e\in E^{+}(u) must now become fully paid. By Lemma [5](https://arxiv.org/html/2602.16387v1#Thmlemma5 "Lemma 5. ‣ 3.2 Default Cost ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") we can represent the payment of ℓ(u,v)\ell\_{(u,v)} of uu towards edge (u,v)(u,v) by raising the external assets of out-neighbor vv by ℓ(u,v)\ell\_{(u,v)}.

This is implemented in lines [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")-[1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") as follows. For each u∈Du\in D we test if it becomes solvent w.r.t. unadjusted network ℱ\mathcal{F} (i.e., checking if au(x)+∑(v,u)pe​(bv)≥Lu+a\_{u}^{(x)}+\sum\_{(v,u)}p\_{e}(b\_{v})\geq L^{+}\_{u}). If so, by Lemma [1](https://arxiv.org/html/2602.16387v1#Thmlemma1 "Lemma 1. ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") it is solvent in 𝐚^\hat{\mathbf{a}}. Thus, we adjust 𝐚(x)\mathbf{a}^{(x)} by removing all outgoing edges of uu and adding external assets of ℓ(u,v)\ell\_{(u,v)} to av(x)a^{(x)}\_{v}. We execute a similar adjustment for 𝐛\mathbf{b} and 𝐛(x)\mathbf{b}^{(x)}: Add the *current payments* p(u,v)​(bu)p\_{(u,v)}(b\_{u}) to bv(x)b^{(x)}\_{v} for each (u,v)∈E(u,v)\in E. This gives an equivalent representation of 𝐚^\hat{\mathbf{a}} and 𝐛\mathbf{b} after removal of the out-edges of uu. The remaining increase in payments then gets executed via an increase in external assets of the (former) out-neighbors of uu. This aligns directly with the invariant of Lemma [1](https://arxiv.org/html/2602.16387v1#Thmlemma1 "Lemma 1. ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") and proves that the algorithm remains correct for networks with default cost.

The asymptotic upper bound on the running time in Theorem [1](https://arxiv.org/html/2602.16387v1#Thmtheorem1 "Theorem 1. ‣ Correctness and Polynomial Time ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") suffers by at most mm additional iterations due to an increase of some external assets by the liability of an incoming edge.
∎

### 3.3 Arbitrary Clearing States

In this section, we show how Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") can be extended to compute arbitrary clearing states for financial networks ℱ\mathcal{F} without default cost. More formally, starting from the minimal state 𝐚^\hat{\mathbf{a}}, we show that any further application of the flooding step leads to larger clearing states. Conversely, for any given clearing state 𝐚\mathbf{a}, we observe that there exists a sequence of flooding steps starting from 𝐚^\hat{\mathbf{a}} that results in 𝐚\mathbf{a}. As such, the set of clearing states is *exactly* the set of states reachable from 𝐚^\hat{\mathbf{a}} by flooding steps. We obtain an algorithmic framework that (by suitable choice of flooding steps) is capable of computing every clearing state of ℱ\mathcal{F}.

As a potential application of this insight, we outline a *range clearing problem*: There is a given financial network ℱ\mathcal{F} and a subset S⊆VS\subseteq V of banks. For each v∈Sv\in S, there is a given interval Iv⊆[0,av(x)+L−​(v)]I\_{v}\subseteq[0,a^{(x)}\_{v}+L^{-}(v)] that specifies a desired range of total assets after clearing. The question is whether or not there exists a *range clearing state* 𝐚\mathbf{a}, i.e., a clearing state such that av∈Iva\_{v}\in I\_{v} for all banks v∈Sv\in S. We show that this problem can be solved in polynomial time in networks ℱ\mathcal{F} without default cost.

We first discuss the extension of Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") and then explain how it can be used to for the range clearing problem.

###### Corollary 2.

Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") can be extended to compute any clearing state of a given financial network ℱ\mathcal{F} without default cost in polynomial time.

###### Proof.

Suppose we are given a clearing state 𝐚\mathbf{a}. Consider any non-sink SCC CC of the active graph G𝐚G\_{\mathbf{a}} and the eigenvector 𝐝\mathbf{d} computed by LP ([5](https://arxiv.org/html/2602.16387v1#S3.E5 "In Flooding SCCs ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")). Adding to 𝐚\mathbf{a} any multiple γ​𝐝\gamma\mathbf{d} that is a feasible solution for LP ([5](https://arxiv.org/html/2602.16387v1#S3.E5 "In Flooding SCCs ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")), we maintain the property that 𝐚+γ​𝐝\mathbf{a}+\gamma\mathbf{d} is a clearing state. Thus, by repeatedly finding non-sink SCCs, computing the eigenvector 𝐝\mathbf{d}, and adding a feasible multiple to 𝐚\mathbf{a}, we can compute an increasing sequence of clearing states.

Conversely, consider any clearing state 𝐚≥𝐚^\mathbf{a}\geq\hat{\mathbf{a}} and the difference 𝐝′=𝐚−𝐚^\mathbf{d}^{\prime}=\mathbf{a}-\hat{\mathbf{a}}. Clearly, 𝐝′\mathbf{d}^{\prime} represents a circulation flow in ℱ\mathcal{F}. Moreover, for any bank with dv′>0d^{\prime}\_{v}>0, these additional assets must be paid to outgoing edges e∈E+​(v)e\in E^{+}(v). All payments must adhere to the payment functions pep\_{e}. As such, there must be payments 𝐝≤𝐝′\mathbf{d}\leq\mathbf{d}^{\prime} that represent a circulation flow within some non-sink SCC CC of G𝐚^G\_{\hat{\mathbf{a}}}. Repeating this argument, we see that 𝐝′\mathbf{d}^{\prime} is decomposable into a sequence of SCCs CC and corresponding solutions of LP ([5](https://arxiv.org/html/2602.16387v1#S3.E5 "In Flooding SCCs ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")). By a suitable choice of flooding steps, we can reach 𝐚\mathbf{a}.
∎

###### Theorem 2.

The range clearing problem can be solved in polynomial time in financial networks ℱ\mathcal{F} without default cost.

###### Proof.

To decide whether or not the instance allows a range clearing state, we first compute 𝐚^\hat{\mathbf{a}} using Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks"). If a^v∈Iv\hat{a}\_{v}\in I\_{v} for all v∈Sv\in S, then 𝐚^\hat{\mathbf{a}} is a range clearing state. If there is a bank v∈Sv\in S such that a^v>Iv\hat{a}\_{v}>I\_{v}, the minimal clearing state 𝐚^\hat{\mathbf{a}} exceeds the target interval for vv. Hence, there is no range clearing state.

In the remainder we consider the case a^v<Iv\hat{a}\_{v}<I\_{v} for at least one bank v∈Sv\in S (and a^w<Iw\hat{a}\_{w}<I\_{w} or a^w∈Iw\hat{a}\_{w}\in I\_{w} for all other banks w∈Sw\in S). For our argument we maintain the invariant that the clearing state 𝐚\mathbf{a} yields av∈Iva\_{v}\in I\_{v} or av<Iva\_{v}<I\_{v} for all v∈Sv\in S. Consider any bank vv with av<Iva\_{v}<I\_{v} and the SCC CC of the active graph G𝐚G\_{\mathbf{a}} that contains vv. If CC is a sink, it is impossible to further increase the assets of vv in a clearing state. There is no target clearing state. Otherwise, we raise the assets within CC continuously by a multiple of eigenvector 𝐝\mathbf{d} until one of two events occurs: (1) av+dv∈Iva\_{v}+d\_{v}\in I\_{v} or (2) the active graph changes. Due to monotonicity and the structure of the payment function, 𝐝\mathbf{d} represents a necessary increase in the assets to achieve av∈Iva\_{v}\in I\_{v} (which is sufficient if event (1) occurs). Clearly, if this results in aw+dw>Iwa\_{w}+d\_{w}>I\_{w} for another bank w∈S∩Cw\in S\cap C, then the interval conditions for vv and ww cannot be satisfied simultaneously and no target clearing state exists. Otherwise, we have computed a larger clearing state that maintains our invariant. The algorithm has to terminate after a finite number of iterations, after which it either reaches a range clearing state or verifies that none exists.

The number of iterations required is linear in the total number of events, which is upper bounded by the total number of breakpoints and |S|≤n|S|\leq n. As such, the asymptotic bound from Theorem [1](https://arxiv.org/html/2602.16387v1#Thmtheorem1 "Theorem 1. ‣ Correctness and Polynomial Time ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") continues to hold. Clearly, each iteration can be performed in polynomial time (choose vv, compute SCC CC, compute increase 𝐝\mathbf{d}, check conditions for all banks in C∩SC\cap S).
∎

### 3.4 Characterization and Maximal Clearing States

In this section, we briefly discuss how to compute the *maximal* clearing state 𝐚ˇ\check{\mathbf{a}}. In particular, by computing 𝐚^\hat{\mathbf{a}} and then applying flooding steps greedily to the largest extent, the arguments in Corollary [2](https://arxiv.org/html/2602.16387v1#Thmcorollary2 "Corollary 2. ‣ 3.3 Arbitrary Clearing States ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") show that a maximal clearing state 𝐚ˇ\check{\mathbf{a}} will be reached. Note that the upper bound on the running time given in Theorem [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") applies to this extended procedure as well.

Instead, in this section, we discuss a more direct approach. We show an equivalence of financial networks with general piecewise-linear payment functions to networks with *priority-proportional* functions.

###### Definition 4.

For a bank v∈Vv\in V, a collection of *priority-proportional* payment functions (pe)e∈E+​(v)(p\_{e})\_{e\in E^{+}(v)} with pe:ℝ→ℝp\_{e}:\mathbb{R}\to\mathbb{R} is given by a partition of E+​(v)E^{+}(v) into kv≥1k\_{v}\geq 1 sets (E1,…,Ekv)(E\_{1},\ldots,E\_{k\_{v}}) such that Ei∩Ej=∅E\_{i}\cap E\_{j}=\emptyset for i≠ji\neq j, ⋃iEi=E+​(v)\bigcup\_{i}E\_{i}=E^{+}(v), and for every i=1,…,kvi=1,\ldots,k\_{v} and e∈Eie\in E\_{i},

|  |  |  |
| --- | --- | --- |
|  | pe​(a)={0if ​a<xv,i−1ℓe∑e′∈Eiℓe′⋅(a−xv,i−1)if ​a∈[xv,i−1,xv,i)ℓeif ​a≥xv,i,p\_{e}(a)=\begin{cases}0&\text{if }a<x\_{v,i-1}\\ \frac{\ell\_{e}}{\sum\_{e^{\prime}\in E\_{i}}\ell\_{e^{\prime}}}\cdot(a-x\_{v,i-1})&\text{if }a\in[x\_{v,i-1},x\_{v,i})\\ \ell\_{e}&\text{if }a\geq x\_{v,i},\end{cases} |  |

where xv,i=∑j≤i∑e′∈Ejℓe′x\_{v,i}=\sum\_{j\leq i}\sum\_{e^{\prime}\in E\_{j}}\ell\_{e^{\prime}} and xv,kv+1=∞x\_{v,k\_{v}+1}=\infty.

Using priority-proportional payment functions, vv clusters its outgoing edges into sets of decreasing priority. It starts to pay all edges of class E1E\_{1} proportionally until they are fully paid. Then it uses any remaining assets to pay class E2E\_{2} proportionally, and so on. Our main insight is that in terms of clearing, the class of networks with priority-proportional functions is equivalent to the class of all networks with piecewise-linear ones.

###### Lemma 6.

For any financial network ℱ\mathcal{F} with piecewise-linear payment functions, there is a network ℱ′\mathcal{F}^{\prime} with priority-proportional payment functions such that 𝐚\mathbf{a} is a clearing state in ℱ\mathcal{F} if and only if 𝐚\mathbf{a} is a clearing state in ℱ′\mathcal{F}^{\prime}.

###### Proof.

Consider a bank vv in network ℱ\mathcal{F} and the set B=⋃e∈E+​(v){xe,i∣i=1​…,ke}B=\bigcup\_{e\in E^{+}(v)}\{x\_{e,i}\mid i=1\ldots,k\_{e}\} of positive and finite interval borders (without repetition) of payment functions of vv. Let kv=|B|k\_{v}=|B| and 0=xv,0<xv,1<…<xv,kv=L+​(v)0=x\_{v,0}<x\_{v,1}<\ldots<x\_{v,k\_{v}}=L^{+}(v) be the ordered elements of BB. We define xv,kv+1=∞x\_{v,k\_{v}+1}=\infty.

Consider an interval [xv,j−1,xv,j)[x\_{v,j-1},x\_{v,j}) for j=1,…,kvj=1,\ldots,k\_{v}. By construction, for each edge e∈E+​(v)e\in E^{+}(v) and interval index jj, there is a unique interval index je∈{1,…,ke+1}j\_{e}\in\{1,\ldots,k\_{e}+1\} such that [xv,j−1,xv,j)⊆[xe,je−1,xe,je)[x\_{v,j-1},x\_{v,j})\subseteq[x\_{e,j\_{e}-1},x\_{e,j\_{e}}). This allows to subdivide the existing interval structure for each edge. We refine every piecewise-linear payment function pep\_{e} to have exactly the intervals [xv,j−1,xv,j)[x\_{v,j-1},x\_{v,j}) for j=1,…,kvj=1,\ldots,k\_{v}, as well as the interval [xv,kv,xv,kv+1)=[L+​(v),∞)[x\_{v,k\_{v}},x\_{v,k\_{v}+1})=[L^{+}(v),\infty). More precisely,

|  |  |  |
| --- | --- | --- |
|  | pe​(a)=me,je⋅(a−pe​(xv,j−1))+pe​(xv,j−1) for any ​a∈[xv,j−1,xv,j)⊆[xe,je−1,xe,je).p\_{e}(a)=m\_{e,j\_{e}}\cdot(a-p\_{e}(x\_{v,j-1}))+p\_{e}(x\_{v,j-1})\qquad\text{ for any }a\in[x\_{v,j-1},x\_{v,j})\subseteq[x\_{e,j\_{e}-1},x\_{e,j\_{e}}). |  |

We represent each edge e=(v,w)∈E+​(v)e=(v,w)\in E^{+}(v) in ℱ′\mathcal{F}^{\prime} by “auxiliary” edges eje\_{j} between vv and ww, for j=1,…,kvj=1,\ldots,k\_{v}. The set EjE\_{j} contains exactly the auxiliary edge eje\_{j}, for each e∈E+​(v)e\in E^{+}(v). The payment functions are exactly the marginal payments that vv would assign to ee in the interval [xv,j−1,xv,j)[x\_{v,j-1},x\_{v,j}), i.e.,

|  |  |  |
| --- | --- | --- |
|  | pej​(a)={0if ​a<xv,j−1pe​(a)−pe​(xv,j−1)if ​a∈[xv,j−1,xv,j)pe​(xv,j)−pe​(xv,j−1)if ​a≥xv,jp\_{e\_{j}}(a)=\begin{cases}0&\text{if }a<x\_{v,j-1}\\ p\_{e}(a)-p\_{e}(x\_{v,j-1})&\text{if }a\in[x\_{v,j-1},x\_{v,j})\\ p\_{e}(x\_{v,j})-p\_{e}(x\_{v,j-1})&\text{if }a\geq x\_{v,j}\\ \end{cases} |  |

For every asset value av=a∈[0,L+​(v))a\_{v}=a\in[0,L^{+}(v)), and jj such that a∈[xv,j−1,xv,j)a\in[x\_{v,j-1},x\_{v,j}), we see

|  |  |  |  |
| --- | --- | --- | --- |
|  | pe​(a)\displaystyle p\_{e}(a) | =(0−pe​(xv,j−1))+(pe​(a)−pe​(xv,j−1))+0\displaystyle=(0-p\_{e}(x\_{v,j-1}))+(p\_{e}(a)-p\_{e}(x\_{v,j-1}))+0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i<j(pe​(xv,i)−pe​(xv,i−1))+(pe​(a)−pe​(xv,j−1))+∑i>j0\displaystyle=\sum\_{i<j}(p\_{e}(x\_{v,i})-p\_{e}(x\_{v,i-1}))+(p\_{e}(a)-p\_{e}(x\_{v,j-1}))+\sum\_{i>j}0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1kvpei​(a)\displaystyle=\sum\_{i=1}^{k\_{v}}p\_{e\_{i}}(a) |  |

i.e., bank vv sends the same payments to ww in both ℱ\mathcal{F} and ℱ′\mathcal{F}^{\prime}. Clearly for av≥L+​(v)a\_{v}\geq L^{+}(v) we also have pe​(a)=L+​(v)=pekv−0=∑i=1kvpei​(a)p\_{e}(a)=L^{+}(v)=p\_{e\_{k\_{v}}}-0=\sum\_{i=1}^{k\_{v}}p\_{e\_{i}}(a). Therefore, both networks have equivalent payment functions and they must also have the same clearing states.

It remains to define appropriate liabilities ℓej\ell\_{e\_{j}} such that ∑jℓej=ℓe\sum\_{j}\ell\_{e\_{j}}=\ell\_{e} and pejp\_{e\_{j}} become priority-proportional. We set

|  |  |  |
| --- | --- | --- |
|  | ℓej=me,j⋅(xv,j−xv,j−1).\ell\_{e\_{j}}=m\_{e,j}\cdot(x\_{v,j}-x\_{v,j-1}). |  |

For a≥L+​(v)a\geq L^{+}(v) this gives

|  |  |  |
| --- | --- | --- |
|  | pei​(a)=pe​(xv,i)−pe​(xv,i−1)=me,i⋅(xv,i−xv,i−1)=ℓei,p\_{e\_{i}}(a)=p\_{e}(x\_{v,i})-p\_{e}(x\_{v,i-1})=m\_{e,i}\cdot(x\_{v,i}-x\_{v,i-1})=\ell\_{e\_{i}}, |  |

for every i=1,…,kvi=1,\ldots,k\_{v}, and, hence,

|  |  |  |
| --- | --- | --- |
|  | ℓe=pe​(a)=∑i=1kvpei​(a)=∑i=1kvℓei.\ell\_{e}=p\_{e}(a)=\sum\_{i=1}^{k\_{v}}p\_{e\_{i}}(a)=\sum\_{i=1}^{k\_{v}}\ell\_{e\_{i}}. |  |

Moreover, for a∈[0,L+​(v))a\in[0,L^{+}(v))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | pej​(a)\displaystyle p\_{e\_{j}}(a) | =pe​(a)−pe​(xv,j−1)\displaystyle=p\_{e}(a)-p\_{e}(x\_{v,j-1}) |  | |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =me,j⋅(a−xe,j−1)\displaystyle=m\_{e,j}\cdot(a-x\_{e,j-1}) |  | |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =me,j∑e′∈E+​(v)me′,j⋅(a−xe,j−1)\displaystyle=\frac{m\_{e,j}}{\sum\_{e^{\prime}\in E^{+}(v)}m\_{e^{\prime},j}}\cdot(a-x\_{e,j-1}) | (by ([3](https://arxiv.org/html/2602.16387v1#S2.E3 "In Payment Functions ‣ 2 Model and Preliminaries ‣ Computing Tarski Fixed Points in Financial Networks"))) and a<L+(v))a<L^{+}(v)) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =ℓej∑e′∈E+​(v)ℓej′⋅(a−xe,j−1)\displaystyle=\frac{\ell\_{e\_{j}}}{\sum\_{e^{\prime}\in E^{+}(v)}\ell\_{e^{\prime}\_{j}}}\cdot(a-x\_{e,j-1}) | (since 0<(xv,j−xv,j−1)<∞0<(x\_{v,j}-x\_{v,j-1})<\infty for j≤kvj\leq k\_{v}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =ℓej∑ej′∈Ejℓej′⋅(a−xe,j−1)\displaystyle=\frac{\ell\_{e\_{j}}}{\sum\_{e^{\prime}\_{j}\in E\_{j}}\ell\_{e^{\prime}\_{j}}}\cdot(a-x\_{e,j-1}) |  | |

Therefore, bank vv has priority-proportional payments in ℱ′\mathcal{F}^{\prime}.

Finally, strictly speaking the network ℱ′\mathcal{F}^{\prime} is a *multi-*graph with kvk\_{v} parallel edges for each (v,w)∈E(v,w)\in E. This can be avoided by further adjusting each edge eje\_{j} as follows. Add an auxiliary bank ve,jv\_{e,j} and split eje\_{j} into two edges ej,1=(v,ve,j)e\_{j,1}=(v,v\_{e,j}) and ej,2=(ve,j,w)e\_{j,2}=(v\_{e,j},w). ve,jv\_{e,j} has no external assets and no default cost. ej,1e\_{j,1} has the same liability and payment function as eje\_{j}. The liability of ej,2e\_{j,2} is infinite. Since ej,2e\_{j,2} is the unique outgoing edge of ve,jv\_{e,j}, the payment function must be pej,2​(a)=ap\_{e\_{j,2}}(a)=a.

It is straightforward to see that pe​(a)=∑i=1kvpei​(a)=∑i=1kvpei,1​(a)=∑i=1kvpei,2​(a)p\_{e}(a)=\sum\_{i=1}^{k\_{v}}p\_{e\_{i}}(a)=\sum\_{i=1}^{k\_{v}}p\_{e\_{i,1}}(a)=\sum\_{i=1}^{k\_{v}}p\_{e\_{i,2}}(a), i.e., given the same assets, vv pays exactly the same amount to ww as in ℱ\mathcal{F}. Hence, the clearing states are equivalent to the ones in ℱ\mathcal{F} (augmented by asset values ave,j=pej​(a)a\_{v\_{e,j}}=p\_{e\_{j}}(a) for each auxiliary bank).
∎

The lemma yields a simple polynomial-time transformation to obtain the network ℱ′\mathcal{F}^{\prime} with n+O​(k​m)n+O(km) banks and O​(k​m)O(km) edges. For ℱ′\mathcal{F}^{\prime} the algorithm from [[22](https://arxiv.org/html/2602.16387v1#bib.bib34 "On priority-proportional payments in financial networks")] computes 𝐚ˇ\check{\mathbf{a}} using an extension of the standard fictitious default algorithm to compute 𝐚ˇ\check{\mathbf{a}} for proportional clearing [[27](https://arxiv.org/html/2602.16387v1#bib.bib30 "Failure and rescue in an interbank network")]. Note that the algorithm strictly speaking does not run in finite time since it involves computing payments in each iteration by an iterative procedure that repeatedly solves a system of non-linear equations and converges monotonically from above (see Algorithm 2 line 5). However, it is not difficult to see that the iterative procedure can be implemented in polynomial time by solving a sequence of feasibility LPs and a monotone descent into the priority classes per bank.

###### Corollary 3.

There is a polynomial-time algorithm to compute the maximal clearing state in every financial network with piecewise-linear (or priority-proportional) payment functions.

###### Proof.

The procedure is an efficient implementation of the top-iteration. Suppose each bank vv has a priority-proportional payment function. We maintain a counter rv∈{0,1,…,kv}r\_{v}\in\{0,1,\ldots,k\_{v}\} that indicates the highest edge class which is supposed to be completely paid for by bank vv. Intuitively, we decide if there is a feasible clearing state for the current counters 𝐫\mathbf{r}, i.e., such that for each bank vv classes 1,…,rv1,\ldots,r\_{v} are completely paid, class rv+1r\_{v}+1 is paid proportionally using the remaining assets, and classes rv+2,…,kvr\_{v}+2,\ldots,k\_{v} are not paid at all. We term this a *clearing state at 𝐫\mathbf{r}*. If we realize that this is impossible, we monotonically decrease some of the counters in the next iteration.

Initially, we set rv=kvr\_{v}=k\_{v} for all v∈Vv\in V, i.e., we assume all banks are solvent. More generally, consider an arbitrary iteration with a vector 𝐫\mathbf{r}. We set pe​(𝐚)=ℓep\_{e}(\mathbf{a})=\ell\_{e} for all 1≤i≤rv1\leq i\leq r\_{v} and each e∈Eie\in E\_{i}. If rv=kvr\_{v}=k\_{v}, then vv is meant to be solvent, so any clearing state at 𝐫\mathbf{r} must deliver sufficient assets to vv, i.e.,

|  |  |  |
| --- | --- | --- |
|  | av=av(x)+∑(u,v)∈E+​(v)pe​(au)≥xv,rv=L+​(v).a\_{v}=a\_{v}^{(x)}+\sum\_{(u,v)\in E^{+}(v)}p\_{e}(a\_{u})\geq x\_{v,r\_{v}}=L^{+}(v). |  |

If rv<kvr\_{v}<k\_{v}, then for each rv+2≤i≤kvr\_{v}+2\leq i\leq k\_{v} we set pe​(𝐚)=0p\_{e}(\mathbf{a})=0 for each e∈Eie\in E\_{i}. For the remaining class rv+1≤kvr\_{v}+1\leq k\_{v}, there must be non-negative assets available, i.e.,

|  |  |  |
| --- | --- | --- |
|  | av=αv​av(x)+βv​∑(u,v)∈E+​(v)pe​(au)≥xv,rv.a\_{v}=\alpha\_{v}a\_{v}^{(x)}+\beta\_{v}\sum\_{(u,v)\in E^{+}(v)}p\_{e}(a\_{u})\geq x\_{v,r\_{v}}. |  |

To check whether a clearing state at 𝐫\mathbf{r} exists, we relax these constraints by an offset dv≥0d\_{v}\geq 0 for each v∈Vv\in V. With the relaxed constraints we compose the natural feasibility LP ([9](https://arxiv.org/html/2602.16387v1#S3.E9 "In Proof. ‣ 3.4 Characterization and Maximal Clearing States ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")) with the objective to minimize the offsets ∑vdv\sum\_{v}d\_{v}.

If 𝐚ˇ\check{\mathbf{a}} is a clearing state at 𝐫\mathbf{r}, LP ([9](https://arxiv.org/html/2602.16387v1#S3.E9 "In Proof. ‣ 3.4 Characterization and Maximal Clearing States ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")) allows a solution without offsets and hence has an optimal value of 0. Otherwise, we maintain by induction the invariant that for any optimal solution (𝐚∗,𝐝∗)(\mathbf{a}^{\*},\mathbf{d}^{\*}) of LP ([9](https://arxiv.org/html/2602.16387v1#S3.E9 "In Proof. ‣ 3.4 Characterization and Maximal Clearing States ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")) we have 𝐚ˇ≤𝐚∗+𝐝∗\check{\mathbf{a}}\leq\mathbf{a}^{\*}+\mathbf{d}^{\*} coordinate-wise with a strict inequality for at least one entry. Since there is no clearing state at 𝐫\mathbf{r}, the available assets of at least one bank vv cannot suffice to pay the liabilities of classes 1,…,rv1,\ldots,r\_{v} in full. Thus, we require some offset dv∗>0d\_{v}^{\*}>0 to fulfill the corresponding constraint, and the optimal value of LP ([9](https://arxiv.org/html/2602.16387v1#S3.E9 "In Proof. ‣ 3.4 Characterization and Maximal Clearing States ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")) becomes strictly positive.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Min. | dv\displaystyle d\_{v} |  | | (9) |
|  | s.t. | av=av(x)+∑(u,v)∈E+​(v)pe\displaystyle a\_{v}=a\_{v}^{(x)}+\sum\_{(u,v)\in E^{+}(v)}p\_{e} | for all vv with rv=kvr\_{v}=k\_{v} |  |
|  |  | av=αv​av(x)+βv​∑(u,v)∈E+​(v)pe\displaystyle a\_{v}=\alpha\_{v}a\_{v}^{(x)}+\beta\_{v}\sum\_{(u,v)\in E^{+}(v)}p\_{e} | for all vv with rv<kvr\_{v}<k\_{v} |  |
|  |  | av+dv≥xv,rv\displaystyle a\_{v}+d\_{v}\geq x\_{v,r\_{v}} | for all v∈Vv\in V |  |
|  |  | pe=0\displaystyle p\_{e}=0 | for all e∈Eie\in E\_{i} with i≥rv+2i\geq r\_{v}+2 |  |
|  |  | pe=ℓe\displaystyle p\_{e}=\ell\_{e} | for all e∈Eie\in E\_{i} with i≤rvi\leq r\_{v} |  |
|  |  | pe=ℓe∑e′∈Erv+1ℓe′⋅(av+dv−xv,rv)\displaystyle p\_{e}=\frac{\ell\_{e}}{\sum\_{e^{\prime}\in E\_{r\_{v}+1}}\ell\_{e^{\prime}}}\cdot(a\_{v}+d\_{v}-x\_{v,r\_{v}}) | for all e∈Erv+1e\in E\_{r\_{v}+1} |  |
|  |  | pe≥0\displaystyle p\_{e}\geq 0 | for all e∈Ee\in E |  |
|  |  | dv≥0\displaystyle d\_{v}\geq 0 | for all v∈Vv\in V |  |

When the optimal value is strictly positive, we must decrease 𝐫\mathbf{r}. Consider any bank vv with strictly positive offset dv∗>0d^{\*}\_{v}>0 in the optimal solution. Clearly, if av∗+dv∗>xv,rva\_{v}^{\*}+d\_{v}^{\*}>x\_{v,r\_{v}} we can reduce δv=av∗+dv∗−xv,rv\delta\_{v}=a\_{v}^{\*}+d\_{v}^{\*}-x\_{v,r\_{v}} and raise the offsets of the out-neighbors in Erv+1E\_{r\_{v}+1} by the proportional amount δv⋅ℓe/(∑e′∈Erv+1ℓe′)\delta\_{v}\cdot\ell\_{e}/(\sum\_{e^{\prime}\in E\_{r\_{v}+1}}\ell\_{e^{\prime}}). This maintains feasibility and the objective function value. Iterating this argument, and using optimality of (𝐚∗,𝐝∗)(\mathbf{a}^{\*},\mathbf{d}^{\*}), we have w.l.o.g. that dv∗>0d\_{v}^{\*}>0 implies av∗+dv∗=xv,rva\_{v}^{\*}+d\_{v}^{\*}=x\_{v,r\_{v}}. Since by our invariant aˇv≤av∗+dv∗=xv,rv\check{a}\_{v}\leq a\_{v}^{\*}+d\_{v}^{\*}=x\_{v,r\_{v}}, it is possible (and potentially necessary) to decrease rvr\_{v} by (at least) 1. Hence, we decrease rvr\_{v} by 1 and start the next iteration. Note that this adjustment maintains the invariant.

Thus, after at most ∑v∈Vkv\sum\_{v\in V}k\_{v} iterations we reach 𝐫\mathbf{r} such that 𝐚ˇ\check{\mathbf{a}} is a clearing state at 𝐫\mathbf{r}. Then LP ([9](https://arxiv.org/html/2602.16387v1#S3.E9 "In Proof. ‣ 3.4 Characterization and Maximal Clearing States ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")) has optimal value 0. We can then compute 𝐚ˇ\check{\mathbf{a}} by solving an adjusted version of LP ([9](https://arxiv.org/html/2602.16387v1#S3.E9 "In Proof. ‣ 3.4 Characterization and Maximal Clearing States ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")). We remove all offset variables dvd\_{v} from the constraints and replace the objective function by maximizing ∑v∈Vav\sum\_{v\in V}a\_{v}. Overall, the running time is polynomial.
∎

## 4 Claims Trades for Minimal Clearing States

In this section, we consider the properties of *claims trading*, a decentralized network adjustment, when applied with *minimal* clearing. In claims trading, a bank ww can buy an edge (u,v)(u,v) by transferring some of its external assets to vv. Throughout this section, we focus on networks without default cost, i.e., αv=βv=1\alpha\_{v}=\beta\_{v}=1 for all v∈Vv\in V.

We start by showing that in a claims trade, it is impossible that *both* creditor vv and buyer ww *strictly* improve their assets. We prove this result for financial networks in which all payment functions are *strictly* monotone, i.e., pe​(au)<pe​(au+ε)p\_{e}(a\_{u})<p\_{e}(a\_{u}+\varepsilon) for every ε∈(0,ℓe−au]\varepsilon\in(0,\ell\_{e}-a\_{u}]. Our proof uses the following lemma, which states novel properties of uniqueness for clearing states in such networks.

###### Lemma 7.

Consider a bank vv in a financial network ℱ\mathcal{F} without default cost and with strictly monotone payment functions. If the clearing states are not unique w.r.t. vv (i.e., a^v≠aˇv\hat{a}\_{v}\neq\check{a}\_{v}), then a^v=0\hat{a}\_{v}=0.

###### Proof.

Let du=aˇu−a^ud\_{u}=\check{a}\_{u}-\hat{a}\_{u} be the difference in payments between the greatest and least fixed point. Moreover, let de=pe​(aˇu)−pe​(a^u)d\_{e}=p\_{e}(\check{a}\_{u})-p\_{e}(\hat{a}\_{u}) for every edge e=(u,w)∈Ee=(u,w)\in E. Consider any bank vv with dv>0d\_{v}>0. Then every node uu reachable from vv in the active graph G𝐚^G\_{\hat{\mathbf{a}}} must have du>0d\_{u}>0. Moreover, dd represents a circulation, so ∑e∈E+​(u)de=du=∑e∈E−​(u)de\sum\_{e\in E^{+}(u)}d\_{e}=d\_{u}=\sum\_{e\in E^{-}(u)}d\_{e} for every bank u∈Vu\in V. This shows that at the end of Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks"), vv must be part of a non-sink SCC. Since all payment functions are *strictly* monotone, the active graph G𝐛G\_{\mathbf{b}} is monotonically getting sparser during the execution of Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") due to solvency of banks. Moreover, since there is no default cost, the set of sinks in the network is monotonically growing. Thus, if vv is part of a non-sink SCC in the end, it must be part of a non-sink SCC throughout the entire execution of the algorithm. However, once assets of vv get raised, all non-sink SCCs reachable from vv must be flooded. As a consequence, vv can only be part of such an SCC at the end of the algorithm when a^v=0\hat{a}\_{v}=0.
∎

###### Theorem 3.

Consider a financial network ℱ\mathcal{F} without default cost and with strictly monotone payment functions. There exists no claims trade that strictly improves the assets of *both* a buyer ww and a creditor vv w.r.t. the minimal clearing state.

###### Proof.

Consider a claims trade with claim (u,v)(u,v) and buyer ww. In order to pay any return, ww must have external assets aw(x)>0a^{(x)}\_{w}>0. By Lemma [7](https://arxiv.org/html/2602.16387v1#Thmlemma7 "Lemma 7. ‣ 4 Claims Trades for Minimal Clearing States ‣ Computing Tarski Fixed Points in Financial Networks"), this implies a^w=aˇw\hat{a}\_{w}=\check{a}\_{w}.

First, suppose that a^v<aˇv\hat{a}\_{v}<\check{a}\_{v}. Then, Lemma [7](https://arxiv.org/html/2602.16387v1#Thmlemma7 "Lemma 7. ‣ 4 Claims Trades for Minimal Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") implies a^v=0\hat{a}\_{v}=0. As discussed in the proof of the lemma, vv is part of a non-sink SCC in G𝐚^G\_{\hat{\mathbf{a}}}. Moreover, ww must be unreachable from vv in G𝐚^G\_{\hat{\mathbf{a}}}. Since all payment functions are strictly monotonic, the active graph becomes only sparser for larger payments. Hence, ww remains unreachable from vv even when vv has higher assets. Consequently, it is impossible for ww to recover any portion of the return ρ\rho paid to vv by larger incoming payments. Thus, there cannot be a creditor-positive trade when a^v<aˇv\hat{a}\_{v}<\check{a}\_{v}.

Second, suppose that a^v=aˇv\hat{a}\_{v}=\check{a}\_{v}. Now, if there was such a trade, w.r.t. 𝐚^\hat{\mathbf{a}}, this trade would also strictly improve the assets of both parties w.r.t. 𝐚ˇ\check{\mathbf{a}}. This is impossible [[16](https://arxiv.org/html/2602.16387v1#bib.bib47 "Algorithms for claims trading")].
∎

### 4.1 Computing Optimal Creditor-Positive Trades

We focus on computing *creditor-positive* trades in this subsection. The main result is that existence of such trades can be decided in polynomial time for (even non-strictly) monotone, piecewise-linear payment functions. Moreover, an optimal creditor-positive return can be computed in polynomial time.

Even if there is a creditor-positive trades, it is not directly obvious that an *optimal* such return must exist as well. For example, consider the related problem of *cash injection*. The goal is to allocate MM external assets in the network to maximize the total assets. For networks with proportional payments, an optimal solution can be computed in polynomial time when the network is evaluated by the *maximal* clearing state [[23](https://arxiv.org/html/2602.16387v1#bib.bib36 "Optimal bailouts and strategic debt forgiveness in financial networks")]. For *minimal* clearing states, it is easy to see that there are simple networks where no optimal solution exists444Suppose the financial network has two components; a cycle of 2 banks and a path of n−2n-2 banks. All edges have liability 11, all banks have no external assets. Suppose we want to inject M=1M=1. Initially, 𝐚^=𝟎\hat{\mathbf{a}}=\mathbf{0}. Assigning 1−ε1-\varepsilon to the head of the path and ε\varepsilon to the banks in the cycle yields total assets of (n−2)​(1−ε)+2+ε(n-2)(1-\varepsilon)+2+\varepsilon. This expression is maximized for ε=0\varepsilon=0, but it applies only when ε∈(0,1]\varepsilon\in(0,1]. For ε=0\varepsilon=0, the total assets in 𝐚^\hat{\mathbf{a}} drop to n−2n-2. As such, there is no optimal solution.

We first analyze the structure of the set of creditor-positive returns. Let 𝐚^\hat{\mathbf{a}} be the pre-trade minimal clearing state and ρmin=pe​(a^u)\rho\_{\min}=p\_{e}(\hat{a}\_{u}) be the pre-trade payment on claim e=(u,v)e=(u,v).

###### Lemma 8.

The set of creditor-positive returns forms a (possibly empty) interval (ρmin,ρ∗](\rho\_{\min},\rho^{\*}].

###### Proof.

We denote by 𝐛^\hat{\mathbf{b}} the post-trade minimal clearing state. Suppose there exists any creditor-positive return ρ\rho.

We first show that ρ>ρmin\rho>\rho\_{\min}. Consider any creditor-positive ρ\rho. For convenience, we slightly abuse notation with pe′′=pe′​(b^y)p^{\prime}\_{e^{\prime}}=p\_{e^{\prime}}(\hat{b}\_{y}) for the post-trade payments on any edge e′=(x,y)e^{\prime}=(x,y) and pe′p\_{e^{\prime}} for the pre-trade payments. We know that b^v>a^v\hat{b}\_{v}>\hat{a}\_{v}. Also, since any creditor-positive trade represents a Pareto-improvement, the post-trade payments 𝐩′≥𝐩\mathbf{p}^{\prime}\geq\mathbf{p} coordinatewise. This implies

|  |  |  |
| --- | --- | --- |
|  | b^v=av(x)+ρ+∑e′∈E−​(v)∖{e}pe′′≥av(x)+ρ+∑e′∈E−​(v)∖{e}pe′=a^v+ρ−ρmin,\hat{b}\_{v}=a\_{v}^{(x)}+\rho+\sum\_{e^{\prime}\in E^{-}(v)\setminus\{e\}}p^{\prime}\_{e^{\prime}}\geq a\_{v}^{(x)}+\rho+\sum\_{e^{\prime}\in E^{-}(v)\setminus\{e\}}p\_{e^{\prime}}=\hat{a}\_{v}+\rho-\rho\_{\min}, |  |

so ρ>ρmin\rho>\rho\_{\min}.

For returns ρ>ρmin\rho>\rho\_{\min}, consider the post-trade network with a return ρmin\rho\_{\min} and shift additional external assets from ww to vv. Investing an additional amount of assets directly at vv instead of vv receiving (parts of) it partly after investment at ww can never hurt the assets of vv in 𝐛^\hat{\mathbf{b}}. Consequently, the post-trade assets of vv are non-decreasing in ρ\rho over the interval [ρmin,∞)[\rho\_{\min},\infty). By the same argument, the post-trade assets of ww are non-increasing in ρ\rho over the interval [ρmin,∞)[\rho\_{\min},\infty). Therefore, all creditor-positive returns must form a consecutive interval.

For ρ=ρmin\rho=\rho\_{\min} it holds 𝐛^=𝐚^\hat{\mathbf{b}}=\hat{\mathbf{a}}, since we simply exchange the same amount of incoming/external assets of vv and ww, respectively. As such, the interval is open on the left. Let us argue that the interval is closed on the right, i.e., it is (ρmin,ρ∗](\rho\_{\min},\rho^{\*}] for some ρ∗\rho^{\*} (if non-empty). Thus, if there is any creditor-positive return, an optimal return ρ∗\rho^{\*} exists.

Consider an increasing, converging sequence limi→∞ρ(i)=ρ∗\lim\_{i\to\infty}\rho^{(i)}=\rho^{\*}. All returns ρ(i)\rho^{(i)} are creditor-positive. Let 𝐛^(i)\hat{\mathbf{b}}^{(i)} be the resulting post-trade assets. Note that 𝐛(i)^\hat{\mathbf{b}^{(i)}} is coordinate-wise non-decreasing – the assets of ww remain at a^w\hat{a}\_{w}, the assets of vv are non-decreasing. As such, the assets in the entire network are non-decreasing. Upon shifting an additional amount of ε(i)=ρ(i)−ρ(i−1)\varepsilon^{(i)}=\rho^{(i)}-\rho^{(i-1)} of external assets to vv, we decrease the external assets of ww by this amount. Since both returns are creditor-positive, ww must receive additional incoming payments of ε(i)\varepsilon^{(i)} in the network. The total assets shall remain at a^w\hat{a}\_{w}, which keeps the outgoing assets fixed at min⁡{a^w,L+​(w)}\min\{\hat{a}\_{w},L^{+}(w)\}. Hence, ww cannot be part of additional flooded components, so the additional incoming payments of ε(i)\varepsilon^{(i)} must originate from the ε(i)\varepsilon^{(i)} external assets invested at vv. Since all payment functions are continuous and non-decreasing, there must be a unique largest value ρ∗\rho^{\*} for which the additional external assets invested at vv arrive completely at ww. This is the limit ρ∗\rho^{\*}, and it is also a creditor-positive return.
∎

Based on this structural insight, we proceed to show the main result of this section.

###### Theorem 4.

Consider a financial network ℱ\mathcal{F} without default cost and with piecewise-linear payment functions. For a given claim e=(u,v)e=(u,v) and a buyer ww, it can be decided in polynomial-time if a creditor-positive trade exists. If the trade exists, the optimal creditor-positive return can be computed in polynomial time.

###### Proof.

Suppose we use a return of ρmin\rho\_{\min}. As observed above, the resulting minimal clearing state is 𝐛^=𝐚^\hat{\mathbf{b}}=\hat{\mathbf{a}}. Consider the active graph G𝐛^G\_{\hat{\mathbf{b}}}. Let us increase the return ρ\rho by a sufficiently small value δ\delta and denote the resulting minimal clearing state by 𝐛^(δ)\hat{\mathbf{b}}^{(\delta)}.

First, suppose we do not pass an interval border on any edge, i.e., G𝐛^(δ)′=G𝐛^G\_{\hat{\mathbf{b}}^{(\delta)}}^{\prime}=G\_{\hat{\mathbf{b}}}. Then the effect on the minimal clearing state must be linear, i.e., the change in the assets is given by

|  |  |  |
| --- | --- | --- |
|  | 𝐝=𝐛^(δ)−𝐛^=δ⋅𝐞v−δ⋅𝐞w+𝐝​𝐌,\mathbf{d}=\hat{\mathbf{b}}^{(\delta)}-\hat{\mathbf{b}}=\delta\cdot\mathbf{e}\_{v}-\delta\cdot\mathbf{e}\_{w}+\mathbf{d}\;\mathbf{M}, |  |

where 𝐞v\mathbf{e}\_{v} and 𝐞w\mathbf{e}\_{w} are unit vectors with an entry of 1 for vv and ww, respectively, and 𝐌\mathbf{M} is the matrix of all slopes of edges in G𝐛^G\_{\hat{\mathbf{b}}} (c.f. ([7](https://arxiv.org/html/2602.16387v1#S3.E7 "In Increasing External Assets ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks")) above). 𝐝\mathbf{d} is linear in δ\delta with slopes

|  |  |  |
| --- | --- | --- |
|  | 𝐬=(𝐈−𝐌)−1⋅(𝐞v−𝐞w).\mathbf{s}=(\mathbf{I}-\mathbf{M})^{-1}\cdot(\mathbf{e}\_{v}-\mathbf{e}\_{w}). |  |

As observed in the proof of Lemma [8](https://arxiv.org/html/2602.16387v1#Thmlemma8 "Lemma 8. ‣ 4.1 Computing Optimal Creditor-Positive Trades ‣ 4 Claims Trades for Minimal Clearing States ‣ Computing Tarski Fixed Points in Financial Networks"), we have sw≤0≤svs\_{w}\leq 0\leq s\_{v}. If sw=0s\_{w}=0, we can increase the return and it will stay creditor-positive. Given that the assets of ww remain awa\_{w}, this Pareto-improve all assets in the network (and, thus, 𝐬≥𝟎\mathbf{s}\geq\mathbf{0} coordinate-wise).

An increase can be implemented very similarly as in Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks"). We adjust all payments linearly until we reach an interval border for some payment function.

Second, suppose G𝐛^G\_{\hat{\mathbf{b}}} passes an interval border upon increase of ρ\rho. More precisely, there is a positive slope of vv and slope 0 for ww, and raising the return requires a change in the active graph. If any larger creditor-positive return exists, it would further raise the assets of vv (and keep the assets of ww at awa\_{w}). This means that we first have to apply the flooding operation on all non-sink SCCs reachable from vv as in Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks") above. Then, we again determine the slopes of further increase as before and check if the slope of ww remains 0 or becomes negative.

We check the existence of a creditor-positive return as follows: Compute the slopes 𝐬\mathbf{s} for G𝐛^G\_{\hat{\mathbf{b}}}. The initial slopes must be sv>0=sws\_{v}>0=s\_{w}, otherwise no creditor-positive return exists. If they are, and G𝐛^G\_{\hat{\mathbf{b}}} is located at an interval border, flood the appropriate SCCs and check the slopes again. If they continue to be sv>0=sws\_{v}>0=s\_{w}, a creditor-positive return exists; otherwise not.

If there is a creditor-positive return, we can search iteratively by increasing the return, changing the active graph, and flooding components as long as the resulting slopes are sv>0=sws\_{v}>0=s\_{w}. It requires repeatedly solving systems of linear equations. The approach is very similar to Algorithm [1](https://arxiv.org/html/2602.16387v1#algorithm1 "In 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks"), and we obtain the same asymptotic upper bound on the running time. Alternatively, we can binary search over the interval [ρmin,min⁡{av(x),ℓe}][\rho\_{\min},\min\{a\_{v}^{(x)},\ell\_{e}\}]. Once we find a return that is creditor-positive, we refine it by computing the slopes and increasing the return until the active graph hits the next interval border. This approach is faster if ρ∗\rho^{\*} is large and there are many interval borders for small creditor-positive returns. It can be slower if there are few interval borders and ρ∗≪min⁡{av(x),ℓe}\rho^{\*}\ll\min\{a\_{v}^{(x)},\ell\_{e}\}.
∎

## References

* [1]
  H. Amini and Z. Feinstein (2023)
  Optimal network compression.
  Europ. J. Oper. Res. 306 (3),  pp. 1439–1455.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p5.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [2]
  P. Azimzadeh (2016)
  Weakly chained matrices, policy iteration, and impulse control.
  SIAM J. Numer. Anal. 54 (3),  pp. 1341––1364.
  Cited by: [§3.1](https://arxiv.org/html/2602.16387v1#S3.SS1.SSS0.Px3.p3.21 "Increasing External Assets ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks").
* [3]
  N. Bertschinger, M. Hoefer, S. Krogmann, P. Lenzner, S. Schuldenzucker, and L. Wilhelmi (2023)
  Equilibria and convergence in fire sale games.
  In Proc.\22ndConf. Auton. Agents and Multi-Agent Syst. (AAMAS),
   pp. 215–223.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p4.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [4]
  N. Bertschinger, M. Hoefer, and D. Schmand (2025)
  Flow allocation games.
  Math. Oper. Res. 50 (1),  pp. 68–89.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px1.p2.1 "Our Results and Techniques ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p1.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p4.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§2](https://arxiv.org/html/2602.16387v1#S2.SS0.SSS0.Px2.p3.6 "Payment Functions ‣ 2 Model and Preliminaries ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§2](https://arxiv.org/html/2602.16387v1#S2.SS0.SSS0.Px2.p3.9 "Payment Functions ‣ 2 Model and Preliminaries ‣ Computing Tarski Fixed Points in Financial Networks").
* [5]
  S. Brânzei, R. C. Phillips, and N. J. Recker (2025)
  Tarski lower bounds from multi-dimensional herringbones.
  In Proc.\2025Workshop Approx. Algorithms for Comb. Opt. Problems (APPROX),
   pp. 52:1–52:12.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.p3.1 "1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [6]
  X. Chen, Y. Li, and M. Yannakakis (2023)
  Reducing Tarski to Unique Tarski (in the black-box model).
  In Proc.\38thComput. Complex. Conf. (CCC),
   pp. 21:1–21:23.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.p3.1 "1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [7]
  U. S. Courts
  Bankruptcy basics.
  Note: [Online; accessed March 27, 2025]https://www.uscourts.gov/court-programs/bankruptcy/bankruptcy-basics
  Cited by: [footnote 1](https://arxiv.org/html/2602.16387v1#footnote1 "In 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [8]
  P. Csóka and J. Herings (2018)
  Decentralized clearing in financial networks.
  Manag. Sci. 64 (10),  pp. 4681–4699.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px1.p1.9 "Our Results and Techniques ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px1.p2.1 "Our Results and Techniques ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p1.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.p4.1 "1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§2](https://arxiv.org/html/2602.16387v1#S2.SS0.SSS0.Px2.p3.9 "Payment Functions ‣ 2 Model and Preliminaries ‣ Computing Tarski Fixed Points in Financial Networks").
* [9]
  P. Csóka and J. Herings (2024)
  Uniqueness of clearing payment matrices in financial networks.
  Math. Oper. Res. 49 (1),  pp. 232–250.
  Cited by: [§2](https://arxiv.org/html/2602.16387v1#S2.SS0.SSS0.Px2.p3.9 "Payment Functions ‣ 2 Model and Preliminaries ‣ Computing Tarski Fixed Points in Financial Networks").
* [10]
  S. Dohn, K. A. Hansen, and A. Klinkby (2025)
  Improved hardness results for the clearing problem in financial networks with credit default swaps.
  In Proc.\18thSymp. Algorithmic Game Theory (SAGT),
   pp. 81–98.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p2.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [11]
  B. Egressy, A. Plesner, and R. Wattenhofer (2024)
  What is the price for lending in financial networks?.
  In Proc.\25thInt. Conf. Princ. Pract. Multi-Agent Syst. (PRIMA),
   pp. 120–135.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p4.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [12]
  L. Eisenberg and T. Noe (2001)
  Systemic risk in financial systems.
  Manag. Sci. 47 (2),  pp. 236–249.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p1.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.p2.2 "1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.p4.1 "1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [Computing Tarski Fixed Points in Financial Networks](https://arxiv.org/html/2602.16387v1#id4.id1 "Computing Tarski Fixed Points in Financial Networks").
* [13]
  H. Elsinger (2009-05)
  Financial networks, cross holdings, and limited liability.
  Working Papers
  Technical Report 156, Oesterreichische Nationalbank (Austrian Central Bank).
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px1.p2.1 "Our Results and Techniques ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [14]
  H. Froese, M. Hoefer, and L. Wilhelmi (2025)
  Dynamic debt swapping in financial networks.
  In Proc.\4th Symp. Algorith. Found. Dynamic Networks (SAND),
   pp. 2:1–2:16.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px1.p2.1 "Our Results and Techniques ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p3.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p5.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [15]
  M. Hoefer, L. Huth, and L. Wilhelmi (2025)
  Fractional claims trades and donations in financial networks.
  CoRR abs/2502.06515.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p3.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [16]
  M. Hoefer, C. Ventre, and L. Wilhelmi (2024)
  Algorithms for claims trading.
  In Proc.\41stSymp. Theoret. Aspects Comput. Sci. (STACS),
   pp. 42:1–42:17.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px1.p7.9 "Our Results and Techniques ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p3.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§4](https://arxiv.org/html/2602.16387v1#S4.4.p3.3 "Proof. ‣ 4 Claims Trades for Minimal Clearing States ‣ Computing Tarski Fixed Points in Financial Networks").
* [17]
  M. Hoefer and L. Wilhelmi (2022)
  Seniorities and minimal clearing in financial network games.
  In Proc.\15thSymp. Algorithmic Game Theory (SAGT),
   pp. 187–204.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px1.p2.1 "Our Results and Techniques ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p4.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [18]
  S. Ioannidis, B. de Keijzer, and C. Ventre (2022)
  Strong approximations and irrationality in financial networks with derivatives.
  In Proc.\49thInt. Colloq. Autom. Lang. Programming (ICALP),
   pp. 76:1–76:18.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p2.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [19]
  S. Ioannidis, B. de Keijzer, and C. Ventre (2023)
  Clearing financial networks with derivatives: from intractability to algorithms.
  CoRR abs/2312.05139.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p2.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [20]
  S. Ioannidis, B. de Keijzer, and C. Ventre (2023)
  Financial networks with singleton liability priorities.
  Theor. Comput. Sci. 963,  pp. 113965.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px1.p2.1 "Our Results and Techniques ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p2.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [21]
  P. Kanellopoulos, M. Kyropoulou, and H. Zhou (2023)
  Debt transfers in financial networks: complexity and equilibria.
  In Proc.\22ndConf. Auton. Agents and Multi-Agent Syst. (AAMAS),
   pp. 260–268.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p4.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [22]
  P. Kanellopoulos, M. Kyropoulou, and H. Zhou (2024)
  On priority-proportional payments in financial networks.
  Theor. Comput. Sci. 1014,  pp. 114767.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px1.p2.1 "Our Results and Techniques ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px1.p6.1 "Our Results and Techniques ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p1.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p4.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§2](https://arxiv.org/html/2602.16387v1#S2.SS0.SSS0.Px2.p3.9 "Payment Functions ‣ 2 Model and Preliminaries ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§3.4](https://arxiv.org/html/2602.16387v1#S3.SS4.p4.6 "3.4 Characterization and Maximal Clearing States ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks").
* [23]
  P. Kanellopoulos, M. Kyropoulou, and H. Zhou (2025)
  Optimal bailouts and strategic debt forgiveness in financial networks.
  Artif. Intell. 349,  pp. 104424.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p4.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§4.1](https://arxiv.org/html/2602.16387v1#S4.SS1.p2.1 "4.1 Computing Optimal Creditor-Positive Trades ‣ 4 Claims Trades for Minimal Clearing States ‣ Computing Tarski Fixed Points in Financial Networks").
* [24]
  P. A. Papp and R. Wattenhofer (2020)
  Network-aware strategies in financial systems.
  In Proc.\47thInt. Colloq. Autom. Lang. Programming (ICALP),
   pp. 91:1–91:17.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p4.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [25]
  P. A. Papp and R. Wattenhofer (2021)
  Debt swapping for risk mitigation in financial networks.
  In Proc.\22ndConf. Econ. Comput. (EC),
   pp. 765–784.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p3.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p5.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [26]
  P. A. Papp and R. Wattenhofer (2021)
  Sequential defaulting in financial networks.
  In Proc.\12thSymp. Innov. Theoret. Comput. Sci. (ITCS),
   pp. 52:1–52:20.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.p4.1 "1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [27]
  L. Rogers and L. Veraart (2013)
  Failure and rescue in an interbank network.
  Manag. Sci. 59 (4),  pp. 882–898.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px1.p3.1 "Our Results and Techniques ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p1.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§1](https://arxiv.org/html/2602.16387v1#S1.p4.1 "1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§2](https://arxiv.org/html/2602.16387v1#S2.SS0.SSS0.Px2.p2.5 "Payment Functions ‣ 2 Model and Preliminaries ‣ Computing Tarski Fixed Points in Financial Networks"),
  [§3.4](https://arxiv.org/html/2602.16387v1#S3.SS4.p4.6 "3.4 Characterization and Maximal Clearing States ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks").
* [28]
  S. Schuldenzucker, S. Seuken, and S. Battiston (2017)
  Finding clearing payments in financial networks with credit default swaps is PPAD-complete.
  In Proc.\8thSymp. Innov. Theoret. Comput. Sci. (ITCS),
   pp. 32:1–32:20.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p2.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [29]
  S. Schuldenzucker, S. Seuken, and S. Battiston (2020)
  Default ambiguity: credit default swaps create new systemic risks in financial networks.
  Manag. Sci. 66 (5),  pp. 1981–1998.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p2.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [30]
  S. Schuldenzucker and S. Seuken (2020)
  Portfolio compression in financial networks: incentives and systemic risk.
  In Proc.\21stConf. Econ. Comput. (EC),
   pp. 79.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p5.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [31]
  P. N. Shivakumar and K. H. Chew (1974)
  A sufficient condition for nonvanishing of determinants.
  Proc. Amer. Math. Soc. 43 (1),  pp. 63–66.
  Cited by: [§3.1](https://arxiv.org/html/2602.16387v1#S3.SS1.SSS0.Px3.p3.21 "Increasing External Assets ‣ 3.1 Minimal Clearing State ‣ 3 Computing Clearing States ‣ Computing Tarski Fixed Points in Financial Networks").
* [32]
  J. H. Stéphane Dees and R. Martin (2017)
  STAMP€: stress-test analytics for macroprudential purposes in the euro area.
  External Links: [Link](https://www.ecb.europa.eu/press/conferences/shared/pdf/20170511_2nd_mp_policy/DeesHenryMartin-Stampe-Stress-Test_Analytics_for_Macroprudential_Purposes_in_the_euro_area.en.pdf)
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.p2.2 "1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [33]
  J. Tong, B. de Keijzer, and C. Ventre (2024)
  Selfishly cancelling debts can reduce systemic risk.
  In Proc.\27thEuropean Conf. Aritf. Intell. (ECAI),
   pp. 3397–3404.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p4.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [34]
  J. Tong, B. D. Keijzer, and C. Ventre (2024)
  Reducing systemic risk in financial networks through donations.
  In Proc.\27thEuropean Conf. Aritf. Intell. (ECAI),
   pp. 3405–3412.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p4.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [35]
  L. Veraart (2022)
  When does portfolio compression reduce systemic risk?.
  Math. Finance 32 (3),  pp. 727–778.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p5.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").
* [36]
  H. Zhou, Y. Wang, K. Varsos, N. Bishop, R. Savani, A. Calinescu, and M. Wooldridge (2024)
  Selfishly prepaying in financial credit networks.
  J. Artif. Intell. Res. 81,  pp. 877–906.
  Cited by: [§1](https://arxiv.org/html/2602.16387v1#S1.SS0.SSS0.Px2.p4.1 "Further Related Work ‣ 1 Introduction ‣ Computing Tarski Fixed Points in Financial Networks").

## Appendix A Examples

###### Example 1.

The bottom iteration has a rather intuitive meaning.
It corresponds to a process in which banks begin to pay off their debt with their external assets and, in each step, use those new assets that they just received.
Consider the following network

uu11vv0ww00/10/10/10/10/10/1step 0

uu11vv0ww012/1{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}\frac{1}{2}}/10/10/112/1{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}\frac{1}{2}}/1step 1

uu11vv0ww012/1\frac{1}{2}/112/1{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}\frac{1}{2}}/112/1\frac{1}{2}/1step 2

uu11vv0ww034/1{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}\frac{3}{4}}/112/1\frac{1}{2}/134/1{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}\frac{3}{4}}/1step 3

uu11vv0ww01/1{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}1}/11/1{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}1}/11/1{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}1}/1step i→∞i\to\infty

In this case each edge will see a payment of
∑i=0n(12)i\sum\_{i=0}^{n}\left(\frac{1}{2}\right)^{i} in step 2​n2n.
This is a geometric series, so all edges will have payments of 11 in the minimal clearing state.

###### Example 2.

We consider the bottom iteration in an example with default rates, where in the limit we do not reach the minimal clearing state. Consider the following network, and let αv=αw=βv=βw=1/2\alpha\_{v}=\alpha\_{w}=\beta\_{v}=\beta\_{w}=1/2.

vv11ww110/20/20/20/2step 0

vv11ww1112/2{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}\frac{1}{2}}/212/2{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}\frac{1}{2}}/2step 1

vv11ww1134/2{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}\frac{3}{4}}/234/2{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}\frac{3}{4}}/2step 2

vv11ww111/2{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}1}/21/2{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}1}/2step i→∞i\to\infty

vv11ww112/2{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}2}/22/2{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}2}/2Minimal clearing state

Throughout the iteration, both vv and ww remain insolvent, the payments on each of their incoming edges remain strictly below 1. In the limit, these payments become 1, and exactly at this point both banks become solvent. Consequently, in the minimal clearing state they are both solvent and clear all debt with payments of 2 per edge. Consequently, the limit of the iteration is not the minimal clearing state.

###### Example 3.

We will apply our algorithm to compute a minimal clearing state in the following network with edge-ranking payment functions. For bank vv the edge to ww has higher priority than the one to yy. Each bank vv is labeled with bv(x)/av(x)b^{(x)}\_{v}/a^{(x)}\_{v} and each edge e=(u,v)e=(u,v) with pe​(bu)/ℓep\_{e}(b\_{u})/\ell\_{e}.

uu0/1{\scriptstyle 0/}1vv0/2{\scriptstyle 0/}2ww0/0{\scriptstyle 0/}0yy0/0{\scriptstyle 0/}00/2\scriptstyle 0/20/2\scriptstyle 0/20/2\scriptstyle 0/20/2\scriptstyle 0/2

uuvvwwyy

uu0+1/1{\scriptstyle 0{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}+1}/}1vv0/2{\scriptstyle 0/}2ww0/0{\scriptstyle 0/}0yy0/0{\scriptstyle 0/}00+1/2\scriptstyle 0{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}+1}/20+1/2\scriptstyle 0{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}+1}/20/2\scriptstyle 0/20/2\scriptstyle 0/2

We choose uu as the first bank to insert assets.
The middle figure shows the strongly connected components.
The right figure shows the increase of payments and external assets with δ∗=1\delta^{\*}=1.

uu1/1{\scriptstyle 1/}1vv0/2{\scriptstyle 0/}2ww0/0{\scriptstyle 0/}0yy0/0{\scriptstyle 0/}01/2\scriptstyle 1/21/2\scriptstyle 1/20/2\scriptstyle 0/20/2\scriptstyle 0/2

uuvvwwyy

uu1/1{\scriptstyle 1/}1vv0+1/2{\scriptstyle 0{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}+1}/}2ww0/0{\scriptstyle 0/}0yy0/0{\scriptstyle 0/}01/2\scriptstyle 1/21+1/2\scriptstyle 1{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}+1}/20/2\scriptstyle 0/20/2\scriptstyle 0/2

The next and last bank to have its assets inserted will be vv.
The strongly connected components have not changed.
This time we can see that inserting all of vv’s external assets at once would cross the breakpoint of vv’s edge to ww.
Hence we have δ∗=1\delta^{\*}=1.

uu1/1{\scriptstyle 1/}1vv1/2{\scriptstyle 1/}2ww0/0{\scriptstyle 0/}0yy0/0{\scriptstyle 0/}01/2\scriptstyle 1/22/2\scriptstyle 2/20/2\scriptstyle 0/20/2\scriptstyle 0/2

uuvvwwyy

uu1/1{\scriptstyle 1/}1vv1/2{\scriptstyle 1/}2ww0/0{\scriptstyle 0/}0yy0/0{\scriptstyle 0/}01/2\scriptstyle 1/22/2\scriptstyle 2/20+2/2\scriptstyle 0{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\pgfsys@color@cmyk@stroke{1}{1}{0}{0}\pgfsys@color@cmyk@fill{1}{1}{0}{0}+2}/20+2/2\scriptstyle 0{\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\pgfsys@color@cmyk@stroke{1}{1}{0}{0}\pgfsys@color@cmyk@fill{1}{1}{0}{0}+2}/2

We can see that the active edges and hence the strongly connected components have changed.
There is now a flooded region {v,y}\{v,y\}.
We solve the corresponding LP and increase the payments.
Afterwards we need to update the strongly connected components.

uu1/1{\scriptstyle 1/}1vv1/2{\scriptstyle 1/}2ww0/0{\scriptstyle 0/}0yy0/0{\scriptstyle 0/}01/2\scriptstyle 1/22/2\scriptstyle 2/22/2\scriptstyle 2/22/2\scriptstyle 2/2

uuvvwwyy

uu1/1{\scriptstyle 1/}1vv1+1/2{\scriptstyle 1{\color[rgb]{0.68,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{0.68,0,0}\pgfsys@color@cmyk@stroke{0}{0.87}{0.68}{0.32}\pgfsys@color@cmyk@fill{0}{0.87}{0.68}{0.32}+1}/}2ww0/0{\scriptstyle 0/}0yy0/0{\scriptstyle 0/}01/2\scriptstyle 1/22/2\scriptstyle 2/22/2\scriptstyle 2/22/2\scriptstyle 2/2

Since there are no outgoing active edges from vv any more, we get 𝐝=𝟎\mathbf{d}=\mathbf{0} and δ∗=1\delta^{\*}=1.

uu1/1{\scriptstyle 1/}1vv2/2{\scriptstyle 2/}2ww0/0{\scriptstyle 0/}0yy0/0{\scriptstyle 0/}01/2\scriptstyle 1/22/2\scriptstyle 2/22/2\scriptstyle 2/22/2\scriptstyle 2/2

At this point all external assets have been inserted, and we have successfully computed the minimal clearing state.