---
authors:
- Mario Ghossoub
- Qinghua Ren
- Ruodu Wang
doc_id: arxiv:2510.18236v1
family_id: arxiv:2510.18236
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes
url_abs: http://arxiv.org/abs/2510.18236v1
url_html: https://arxiv.org/html/2510.18236v1
venue: arXiv q-fin
version: 1
year: 2025
---


Mario Ghossoub
Department of Statistics and Actuarial Science,
University of Waterloo,
Waterloo, Ontario, Canada.
E-mail: [mario.ghossoub@uwaterloo.ca](mailto:mario.ghossoub@uwaterloo.ca).
  
Qinghua Ren
Department of Statistics and Actuarial Science,
University of Waterloo,
Waterloo, Ontario, Canada.
E-mail: [qinghua.ren@uwaterloo.ca](mailto:qinghua.ren@uwaterloo.ca).
  
Ruodu Wang
Department of Statistics and Actuarial Science,
University of Waterloo,
Waterloo, Ontario, Canada.
E-mail: [wang@uwaterloo.ca](mailto:wang@uwaterloo.ca).

###### Abstract

We study Pareto-optimal risk sharing in economies with heterogeneous attitudes toward risk, where agents’ preferences are modeled by distortion risk measures. Building on comonotonic and counter-monotonic improvement results, we show that agents with similar attitudes optimally share risks comonotonically (risk-averse) or counter-monotonically (risk-seeking). We show how the general nn-agent problem can be reduced to a two-agent formulation between representative risk-averse and risk-seeking agents, characterized by the infimal convolution of their distortion risk measures. Within this two-agent framework, we establish necessary and sufficient conditions for the existence of optimal allocations, and we identify when the infimal convolution yields an unbounded value. When existence fails, we analyze the problem under nonnegative allocation constraints, and we characterize optima explicitly, under piecewise-linear distortion functions and Bernoulli-type risks. Our findings suggest that the optimal allocation structure is governed by the relative strength of risk aversion versus risk seeking behavior, as intuition would suggest.

## 1 Introduction

In classical risk-sharing problems with risk‐averse agents, Pareto‐optimal allocations are comonotonic under mild conditions, as a result of the classical comonotonic improvement theorem of Landsberger and Meilijson, ([1994](https://arxiv.org/html/2510.18236v1#bib.bib20)). On the other hand, when only risk‐seeking agents are involved, inter-agent gambling arises, thereby leading to counter‐monotonic allocations, as shown in Lauzier et al., ([2023](https://arxiv.org/html/2510.18236v1#bib.bib22), [2025](https://arxiv.org/html/2510.18236v1#bib.bib21)).
This contrast naturally leads to the question of how heterogeneous preferences shape optimal allocations in markets that comprise both risk‐averse and risk‐seeking participants, a more realistic assumption in practice. A simple conjecture is that the optimal allocation structure is determined by the relative strength of risk aversion versus risk seeking behavior.

The exchange of risk between agents with mixed risk attitudes remains theoretically underdeveloped. In the literature, risk sharing has been studied primarily in markets with homogeneous preference classes, e.g., all risk-averse, all risk-seeking, or all quantile-type agents. For risk-averse agents, optimal allocations have been characterized in various frameworks, from the seminal work by Borch, ([1962](https://arxiv.org/html/2510.18236v1#bib.bib7)) within the context of risk-averse Expected-Utility (EU) agents, to the case of convex risk measures in Barrieu and El Karoui, ([2005](https://arxiv.org/html/2510.18236v1#bib.bib4)) and Jouini et al., ([2008](https://arxiv.org/html/2510.18236v1#bib.bib19)), all showing comonotonicity of optimal allocations. The results can also be extended to non-monotone risk measures (Acciaio, ([2007](https://arxiv.org/html/2510.18236v1#bib.bib1)) and Filipović and Svindland, ([2008](https://arxiv.org/html/2510.18236v1#bib.bib12))) and quasi-convex risk measures (Mastrogiacomo and Rosazza Gianin, ([2015](https://arxiv.org/html/2510.18236v1#bib.bib25))). For more developments on efficient risk sharing with monetary and convex risk measures or concave utility functionals, see Heath and Ku, ([2004](https://arxiv.org/html/2510.18236v1#bib.bib17)), Tsanakas, ([2009](https://arxiv.org/html/2510.18236v1#bib.bib28)), and Ghossoub and Zhu, ([2024](https://arxiv.org/html/2510.18236v1#bib.bib16)), for instance. Although risk aversion serves as a foundational and tractable assumption in theory, empirical observations frequently reveal risk-seeking attitudes in practice. Building upon the counter-monotonic improvement theorem of Lauzier et al., ([2025](https://arxiv.org/html/2510.18236v1#bib.bib21)), the recent work of Ghossoub et al., ([2024](https://arxiv.org/html/2510.18236v1#bib.bib14), [2025](https://arxiv.org/html/2510.18236v1#bib.bib15)) provided a systematic study of risk sharing among risk-seeking agents with distortion risk measures. They showed that counter-monotonic allocations are optimal in this setting, and they provided some insight into computing the inf-convolution (infimal convolution) of concave risk measures. Beyond convexity or concavity, risk-sharing problems have also been examined in quantile-based and more general distortion risk-metrics frameworks; see Embrechts et al., ([2018](https://arxiv.org/html/2510.18236v1#bib.bib10)), Weber, ([2018](https://arxiv.org/html/2510.18236v1#bib.bib31)) and Lauzier et al., ([2024](https://arxiv.org/html/2510.18236v1#bib.bib23)).

The relationship between heterogeneous risk attitudes and the existence of Pareto optima or competitive equilibria remains an open and challenging question. One should remark that the presence of non-convex preferences can cause technical problems since the existence of optima can fail in this setting. The market that combines risk-averse agents and risk-seeking agents is of particular interest; see Araujo et al., ([2017](https://arxiv.org/html/2510.18236v1#bib.bib2), [2018](https://arxiv.org/html/2510.18236v1#bib.bib3)),
Herings and Yang, ([2022](https://arxiv.org/html/2510.18236v1#bib.bib18)), and Beißner and Werner, ([2023](https://arxiv.org/html/2510.18236v1#bib.bib6)). In a finite-state exchange economy, Araujo et al., ([2017](https://arxiv.org/html/2510.18236v1#bib.bib2)) proved the existence of individually rational Pareto optima even in the presence of non-convex preferences, and they suggested that risk-averse agents exhibit comonotonic sharing, while risk-seeking agents bet on the allocation of risk. Within the framework of distortion risk measures, we obtain analogous results. Moreover, rather than providing only qualitative statements, we deliver quantitative characterizations via the inf-convolution. Beißner et al., ([2024](https://arxiv.org/html/2510.18236v1#bib.bib5)) studied a pure-exchange economy without aggregate uncertainty, considering two agents who maximize their rank-dependent utility (RDU), with concave utility functions and arbitrary (possibly nonconvex) probability distortion functions. They derived a closed-form characterization of Pareto-optimal allocations in this general setting. Our paper also touches on a related risk-sharing problem with a constant aggregate. Although distortion risk measures can be viewed as a subclass of RDU with linear utility, the results of Beißner et al., ([2024](https://arxiv.org/html/2510.18236v1#bib.bib5)) cannot be directly extended to our framework, as they require strict concavity of the utility functions.

To overcome the challenges arising from mixed risk attitudes in the market, we study a finite-agent economy with heterogeneous risk attitudes, where the agents’ preferences are represented by distortion risk measures. For such preferences, risk attitudes are characterized by their probability distortion functions. We analyze Pareto-optimal allocations through the tool of inf-convolution. Our first step is to reduce the multi-agent problem into a 22-agent problem, where one agent acts as the representative agent of the risk-averse participants, and the other acts as the representative agent of the risk-seeking participants (Theorem [1](https://arxiv.org/html/2510.18236v1#Thmtheorem1 "Theorem 1. ‣ 3 Problem reduction ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")). Zooming in on the reduced 22-agent problem, we provide necessary and sufficient conditions for the existence of optimal allocations. Since unbounded optimal allocations may not exist for risk-seeking agents due to excessive gambling, we consider separately the case where the allocations are possibly signed and the case of nonnegative allocations; the latter corresponds to the economically relevant assumption that no agents can profit from an aggregate pure loss. We offer several explicit characterizations of the inf-convolution and optimal allocations under some assumptions on the distortion functions. As another main contribution, we show that, indeed, the relative strength of risk aversion and risk seeking of the representative agents determines the structure of the optimal allocations for the original market, formalizing the aforementioned simple conjecture.

The rest of this paper is structured as follows. Section [2](https://arxiv.org/html/2510.18236v1#S2 "2 Problem formulation ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") formulates the risk-sharing problem that we consider in this paper. Section [3](https://arxiv.org/html/2510.18236v1#S3 "3 Problem reduction ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") presents an nn-agent setting with mixed attitudes (risk-averse and risk-seeking agents), and shows how the problem reduces to a two-agent formulation, which motivates the analysis in Sections [4](https://arxiv.org/html/2510.18236v1#S4 "4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") and [5](https://arxiv.org/html/2510.18236v1#S5 "5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"). Regarding constraints on the feasible allocation set, Section [4](https://arxiv.org/html/2510.18236v1#S4 "4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") considers general allocation sets and establishes our main existence result for optimal allocations, while Section [5](https://arxiv.org/html/2510.18236v1#S5 "5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") focuses on positive allocation sets. Several results extend beyond the specific risk-averse/risk-seeking setting. Section [6](https://arxiv.org/html/2510.18236v1#S6 "6 Applications to the original problem ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") integrates these results to resolve the nn-agent problem in certain settings. Finally, Section [7](https://arxiv.org/html/2510.18236v1#S7 "7 Conclusion ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") concludes.

## 2 Problem formulation

Let 𝒳\mathcal{X} be a convex cone of random variables on an atomless probability space (Ω,ℱ,ℙ)\left(\Omega,\mathcal{F},\mathbb{P}\right). Consider a setting with n∈ℕn\in\mathbb{N} agents who share a random variable X∈𝒳X\in\mathcal{X}, representing the aggregate risk, without central authority involvement. Write [n]={1,…,n}[n]=\{1,\dots,n\}.
Positive and negative values of random variables represent losses and surpluses, respectively.
We denote by FX:ℝ↦[0,1]F\_{X}:\mathbb{R}\mapsto[0,1] the cumulative distribution function of XX, and by SX:ℝ↦[0,1]S\_{X}:\mathbb{R}\mapsto[0,1] the survival function of XX.
Let UXU\_{X} be a uniform random variable on [0,1][0,1], such that FX−1​(UX)=XF\_{X}^{-1}(U\_{X})=X almost surely. The existence of UXU\_{X} for a general XX is guaranteed; see Lemma A.32 of Föllmer and Schied, ([2016](https://arxiv.org/html/2510.18236v1#bib.bib13)).
We consider a one-period economy, where an aggregate risk XX is redistributed among the agents at the end of the period.
For a given X∈𝒳X\in\mathcal{X} and n∈ℕn\in\mathbb{N}, the set of allocations of XX is

|  |  |  |
| --- | --- | --- |
|  | 𝔸n​(X)={(X1,…,Xn)∈𝒳n:∑i=1nXi=X}.\mathbb{A}\_{n}(X)=\left\{(X\_{1},\ldots,X\_{n})\in\mathcal{X}^{n}:\sum\_{i=1}^{n}X\_{i}=X\right\}. |  |

That is, the set of allocations of XX includes all possible divisions of XX among the nn agents. Note that the choice of 𝒳\mathcal{X} may impose constraints on the admissible allocations. In this paper, the space 𝒳\mathcal{X} can be chosen as the space L∞L^{\infty} of bounded random variables or the space L+L^{+} of nonnegative random variables. The choice will be specified in each context.

We next impose some dependence structures on admissible allocations.
A random vector (X,Y)(X,Y) is said to be comonotonic (resp. counter-monotonic) if
(X​(ω)−X​(ω′))​(Y​(ω)−Y​(ω′))≥0​(resp.≤0)(X(\omega)-X(\omega^{\prime}))(Y(\omega)-Y(\omega^{\prime}))\geq 0~(\mbox{resp.}~\leq 0) for all ω,ω′∈Ω\omega,\omega^{\prime}\in\Omega.
An nn-tuple (X1,…,Xn)(X\_{1},\ldots,X\_{n}) is called comonotonic (resp. counter-monotonic) if each pair of its components is comonotonic (resp. counter-monotonic).
For results on and applications of these concepts in actuarial science, see Dhaene et al., ([2002](https://arxiv.org/html/2510.18236v1#bib.bib9)) on comonotonicity and Dhaene and Denuit, ([1999](https://arxiv.org/html/2510.18236v1#bib.bib8)) and Lauzier et al., ([2023](https://arxiv.org/html/2510.18236v1#bib.bib22)) on counter-monotonicity.

The preference of each agent is represented by a distortion risk measure
ρh:𝒳↦ℝ\rho\_{h}:\mathcal{X}\mapsto\mathbb{R}, defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh​(X)=∫X​dh∘ℙ=∫0∞h​(ℙ​(X>x))​dx+∫−∞0(hi​(ℙ​(X>x))−h​(1))​dx,\displaystyle\rho\_{h}(X)=\int X\mathrm{d}h\circ\mathbb{P}=\int\_{0}^{\infty}h(\mathbb{P}(X>x))\,\mathrm{d}x+\int\_{-\infty}^{0}(h\_{i}(\mathbb{P}(X>x))-h(1))\,\mathrm{d}x, |  | (1) |

where hh is in the set ℋ\mathcal{H}
of all normalized distortion functions, i.e.,

|  |  |  |
| --- | --- | --- |
|  | ℋ={h:[0,1]→[0,1]∣h​ is increasing, ​h​(0)=0​ and ​h​(1)=1}.\mathcal{H}=\{h:[0,1]\rightarrow[0,1]\mid h\text{ is increasing, }h(0)=0\text{ and }h(1)=1\}. |  |

If h∈ℋh\in\mathcal{H}, then ρh\rho\_{h} is also called a dual utility of Yaari, ([1987](https://arxiv.org/html/2510.18236v1#bib.bib32)).
In the dual theory, the distortion function provides a full characterization of risk aversion: a Yarri agent is (strongly) risk-averse if and only if hh is concave (Yaari, ([1987](https://arxiv.org/html/2510.18236v1#bib.bib32))). Similarly,
risk seeking corresponds to convexity of hh. We omit “strong” in risk aversion and risk seeking, which is the only sense that we consider in this paper (weak risk aversion is different from strong risk aversion for distortion risk measures).

If one drops the normalization requirement of h​(1)=1h(1)=1 and monotonicity of hh, we obtain the more general class of distortion riskmetrics (see Wang et al., ([2020](https://arxiv.org/html/2510.18236v1#bib.bib30))) ρh\rho\_{h} with h∈ℋBVh\in\mathcal{H}^{\mathrm{BV}}, where

|  |  |  |
| --- | --- | --- |
|  | ℋBV={h:[0,1]→ℝ∣h​ is bounded variation and ​h​(0)=0}.\mathcal{H}^{\mathrm{BV}}=\{h:[0,1]\rightarrow\mathbb{R}\mid h\text{ is bounded variation and }h(0)=0\}. |  |

This broader class is introduced as it will be useful in the subsequent analysis.

Our goal is to study Pareto-optimal allocations among the nn agents in this market. An allocation (X1,…,Xn)∈𝔸n​(X)(X\_{1},\dots,X\_{n})\in\mathbb{A}\_{n}(X) is said to be Pareto optimal in 𝔸n​(X)\mathbb{A}\_{n}(X) if for any (Y1,…,Yn)∈𝔸n​(X)(Y\_{1},\dots,Y\_{n})\in\mathbb{A}\_{n}(X) satisfying ρhi​(Yi)≤ρhi​(Xi)\rho\_{h\_{i}}(Y\_{i})\leq\rho\_{h\_{i}}(X\_{i}) for all i∈[n]i\in[n], we have ρi​(Yi)=ρi​(Xi)\rho\_{i}\left(Y\_{i}\right)=\rho\_{i}\left(X\_{i}\right), for all i∈[n]i\in[n].
That is, no agent can strictly improve their position without worsening that of another.

An alternative method of finding Pareto optima is via the tool of infimal convolution. The inf-convolution □i=1n​ρhi\square\_{i=1}^{n}\rho\_{h\_{i}} of nn risk measures ρh1,…,ρhn\rho\_{h\_{1}},\dots,\rho\_{h\_{n}} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | □i=1nρhi​(X)=inf{∑i=1nρi​(Xi):(X1,…,Xn)∈𝔸n​(X)},X∈𝒳.\displaystyle\mathop{\square}\displaylimits\_{i=1}^{n}\rho\_{h\_{i}}(X)=\inf\left\{\sum\_{i=1}^{n}\rho\_{i}\left(X\_{i}\right):\left(X\_{1},\dots,X\_{n}\right)\in\mathbb{A}\_{n}(X)\right\},\quad X\in\mathcal{X}. |  | (2) |

That is, the inf-convolution of nn risk measures is the infimum over aggregate risk values for all possible allocations.
An allocation (X1,…,Xn)(X\_{1},\dots,X\_{n}) is said to be optimal in 𝔸n​(X)\mathbb{A}\_{n}(X) if it attains the infimum, i.e.,
□i=1n​ρhi​(X)=∑i=1nρhi​(Xi)\square\_{i=1}^{n}\rho\_{h\_{i}}(X)=\sum\_{i=1}^{n}\rho\_{h\_{i}}(X\_{i}). It is immediate that every optimal allocation is Pareto optimal.
Moreover, when 𝒳=L∞\mathcal{X}=L^{\infty}, the converse also holds and Pareto optimality coincides with optimality through inf-convolution, because of translation invariance of the risk measures (see Proposition 1 of Embrechts et al., ([2018](https://arxiv.org/html/2510.18236v1#bib.bib10))). By contrast, the converse may not hold if 𝒳\mathcal{X} is chosen as L+L^{+}. Both cases will be considered in the subsequent analysis; see Section [4](https://arxiv.org/html/2510.18236v1#S4 "4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")
and Section [5](https://arxiv.org/html/2510.18236v1#S5 "5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").

A particularly useful property of distortion risk measures is the following duality. For any X∈𝒳X\in\mathcal{X}, we have ρh​(−X)=−ρh~​(X)\rho\_{h}(-X)=-\rho\_{\widetilde{h}}(X), where h~​(t)=1−h​(1−t)\widetilde{h}(t)=1-h(1-t), t∈[0,1]t\in[0,1], is the dual function of hh.
Consequently, an optimal allocation (X1∗,…,Xn∗)(X\_{1}^{\*},\ldots,X\_{n}^{\*}) that attains the infimum in ([2](https://arxiv.org/html/2510.18236v1#S2.E2 "In 2 Problem formulation ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) also solves the utility maximization problem:

|  |  |  |
| --- | --- | --- |
|  | sup{∑i=1nρh~i​(−Xi):(−X1,…,−Xn)∈𝔸n​(−X)},X∈𝒳,\displaystyle\sup\left\{\sum\_{i=1}^{n}\rho\_{\widetilde{h}\_{i}}\left(-X\_{i}\right):\left(-X\_{1},\dots,-X\_{n}\right)\in\mathbb{A}\_{n}(-X)\right\},\quad X\in\mathcal{X}, |  |

and here ρh~i\rho\_{\widetilde{h}\_{i}} can be interpreted as agent ii’s utility functional in the theory of Yaari, ([1987](https://arxiv.org/html/2510.18236v1#bib.bib32)).
That is, a risk sharing minimizer is simultaneously a utility maximizer under the dual distortions. In this paper, we adopt the risk sharing perspective and focus on minimizing the aggregate risk across all agents.

In a manner similar to the inf-convolution of risk measures, we define the inf-convolution of real functions, adopting the same notation.
Given nn distortion functions hi∈ℋh\_{i}\in\mathcal{H} for i∈[n]i\in[n], their inf-convolution □i=1nhi​(x):[0,1]↦ℝ\mathop{\square}\displaylimits\_{i=1}^{n}h\_{i}(x):[0,1]\mapsto\mathbb{R} is defined as

|  |  |  |
| --- | --- | --- |
|  | □i=1nhi​(x)=inf{∑i=1nhi​(xi):xi∈[0,1]​for​i∈[n];∑i=1nxi=x}.\displaystyle\mathop{\square}\displaylimits\_{i=1}^{n}h\_{i}(x)=\inf\left\{\sum\_{i=1}^{n}h\_{i}(x\_{i}):x\_{i}\in[0,1]\ \text{for}\ i\in[n];~\sum\_{i=1}^{n}x\_{i}=x\right\}. |  |

Note that the □i=1nhi\mathop{\square}\displaylimits\_{i=1}^{n}h\_{i} is not necessarily a distortion function since □i=1nhi​(1)=1\mathop{\square}\displaylimits\_{i=1}^{n}h\_{i}(1)=1 does not always hold.
Throughout the paper, we write ⋁i=1nxi=max⁡{x1,…,xn}\bigvee\_{i=1}^{n}x\_{i}=\max\{x\_{1},\dots,x\_{n}\} and ⋀i=1nxi=min⁡{x1,…,xn}\bigwedge\_{i=1}^{n}x\_{i}=\min\{x\_{1},\dots,x\_{n}\} for any x1,…,xn∈ℝx\_{1},\dots,x\_{n}\in\mathbb{R}, and these operation are naturally extended to functions.

## 3 Problem reduction

Our goal is to understand how the coexistence of risk‐averse and risk‐seeking behaviors shapes Pareto‐optimal allocations. Specifically, suppose that nn agents share a total risk XX. The first mm are risk averse, with concave distortion functions hi,i∈[m]h\_{i},i\in[m], and the remaining n−mn-m are risk seeking with convex distortion functions hi,i∈[n]∖[m]h\_{i},i\in[n]\setminus[m].
The following theorem shows that under some mild conditions, this nn-agent risk-sharing problem can always be reduced to an equivalent two‐agent problem.
Specifically, let g1=⋀i=1mhig\_{1}=\bigwedge\_{i=1}^{m}h\_{i} and g2=□j=m+1n​hjg\_{2}=\square\_{j=m+1}^{n}h\_{j}.
These two are indeed the representative risk preferences for the risk-averse and risk-seeking groups, as shown in Theorem [1](https://arxiv.org/html/2510.18236v1#Thmtheorem1 "Theorem 1. ‣ 3 Problem reduction ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").
The key insight of this reduction is that the collective behavior of each class can be represented by a single “aggregate” distortion, so the optimal allocation can be studied through a two-distortion formulation. Before moving to the result, we first introduce the following set:

|  |  |  |
| --- | --- | --- |
|  | 𝒳⟂={X∈𝒳:there exists a uniform random variable U independent of​X}.\mathcal{X}^{\perp}=\{X\in\mathcal{X}:\text{there exists a uniform random variable $U$ independent of}\,X\}. |  |

For more discussions on 𝒳⟂\mathcal{X}^{\perp}, in particular its relation to 𝒳\mathcal{X},
we refer to Section 5 of Liu et al., ([2020](https://arxiv.org/html/2510.18236v1#bib.bib24)).

###### Theorem 1.

Let 𝒳=L+\mathcal{X}=L^{+}. Assume that hi∈ℋh\_{i}\in\mathcal{H} are continuous for all i∈[n]i\in[n], with hih\_{i} concave for i∈[m]i\in[m] and hjh\_{j} convex for j∈[n]∖[m]j\in[n]\setminus[m].
For X∈𝒳⟂X\in\mathcal{X}^{\perp}, let
(X1∗,…,Xn∗)∈𝔸n​(X)(X\_{1}^{\*},\ldots,X\_{n}^{\*})\in\mathbb{A}\_{n}(X) be an optimal allocation. Then the following holds:

* (i)

  If hih\_{i} is strictly concave for i∈[m]i\in[m]
  and hjh\_{j} is strictly convex for j∈[n]∖[m]j\in[n]\setminus[m], then the vector (X1∗,…,Xm∗)(X\_{1}^{\*},\ldots,X\_{m}^{\*}) is comonotonic and the vector (Xm+1∗,…,Xn∗)(X\_{m+1}^{\*},\ldots,X\_{n}^{\*}) is counter-monotonic.
* (ii)

  It holds that

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | □i=1nρhi​(X)=ρg1​□ρg2​(X).\displaystyle\mathop{\square}\displaylimits\_{i=1}^{n}\rho\_{h\_{i}}(X)=\rho\_{g\_{1}}\mathop{\square}\displaylimits\rho\_{g\_{2}}(X). |  | (3) |

###### Proof.

(i) The comonotonicity of (X1∗,…,Xm∗)(X\_{1}^{\*},\ldots,X\_{m}^{\*}) follows directly from the comonotonic improvement theorem of Landsberger and Meilijson, ([1994](https://arxiv.org/html/2510.18236v1#bib.bib20)), while the counter-monotonicity of (Xm+1∗,…,Xn∗)(X\_{m+1}^{\*},\ldots,X\_{n}^{\*}) follows from the counter-monotonic improvement theorem of Lauzier et al., ([2025](https://arxiv.org/html/2510.18236v1#bib.bib21)).

(ii)
For X∈𝒳⟂X\in\mathcal{X}^{\perp},

|  |  |  |  |
| --- | --- | --- | --- |
|  | □i=1nρhi​(X)=\displaystyle\mathop{\square}\displaylimits\_{i=1}^{n}\rho\_{h\_{i}}(X)= | inf{∑i=1mρhi​(Xi)+∑i=m+1nρhi​(Xi):(X1,…,Xn)∈𝔸n​(X)}\displaystyle\inf\left\{\sum\_{i=1}^{m}\rho\_{h\_{i}}(X\_{i})+\sum\_{i=m+1}^{n}\rho\_{h\_{i}}(X\_{i}):(X\_{1},\dots,X\_{n})\in\mathbb{A}\_{n}(X)\right\} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =inf{□i=1mρhi​(Y)+□i=m+1nρhi​(Z):(Y,Z)∈𝔸2​(X)}\displaystyle=\inf\left\{\mathop{\square}\displaylimits\_{i=1}^{m}\rho\_{h\_{i}}(Y)+\mathop{\square}\displaylimits\_{i=m+1}^{n}\rho\_{h\_{i}}(Z):(Y,Z)\in\mathbb{A}\_{2}(X)\right\} |  | (4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =inf{□i=1mρhi​(Y′)+□i=m+1nρhi​(Z′):(Y′,Z′)∈𝔸2​(X)​and​Z′∈𝒳⟂}\displaystyle=\inf\left\{\mathop{\square}\displaylimits\_{i=1}^{m}\rho\_{h\_{i}}(Y^{\prime})+\mathop{\square}\displaylimits\_{i=m+1}^{n}\rho\_{h\_{i}}(Z^{\prime}):(Y^{\prime},Z^{\prime})\in\mathbb{A}\_{2}(X)~\text{and}~Z^{\prime}\in\mathcal{X}^{\perp}\right\} |  | (5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =inf{ρg1​(Y)+ρg2​(Z):(Y,Z)∈𝔸2​(X)}\displaystyle=\inf\left\{\rho\_{g\_{1}}(Y)+\rho\_{g\_{2}}(Z):(Y,Z)\in\mathbb{A}\_{2}(X)\right\} |  | (6) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ρg1​□ρg2​(X).\displaystyle=\rho\_{g\_{1}}\mathop{\square}\displaylimits\rho\_{g\_{2}}(X). |  |

Applying Theorem 2 of Ghossoub et al., ([2024](https://arxiv.org/html/2510.18236v1#bib.bib14)) to □i=m+1nρhi​(Z)\mathop{\square}\displaylimits\_{i=m+1}^{n}\rho\_{h\_{i}}(Z) in ([4](https://arxiv.org/html/2510.18236v1#S3.E4 "In 3 Problem reduction ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) requires Z∈𝒳⟂Z\in\mathcal{X}^{\perp}.
We now show that it suffices to assume X∈𝒳⟂X\in\mathcal{X}^{\perp}.
Indeed, for any (Y,Z)∈𝔸2​(X)(Y,Z)\in\mathbb{A}\_{2}(X), there exists (Y′,Z′)∈𝔸2​(X)(Y^{\prime},Z^{\prime})\in\mathbb{A}\_{2}(X) and a standard uniform random variable UU
such that (X,Y,Z)​=𝑑​(X,Y′,Z′)(X,Y,Z)\overset{d}{=}(X,Y^{\prime},Z^{\prime}) and UU is independent of (X,Y′,Z′)(X,Y^{\prime},Z^{\prime}); see Lemma 2 of Lauzier et al., ([2025](https://arxiv.org/html/2510.18236v1#bib.bib21)).
The allocation (Y′,Z′)∈𝔸2​(X)(Y^{\prime},Z^{\prime})\in\mathbb{A}\_{2}(X) can be constructed as follows.
Since X∈𝒳⟂X\in\mathcal{X}^{\perp}, there exists a standard uniform random variable UU independent of XX, then we can generate i.i.d. standard uniform random variables U1,U2U\_{1},U\_{2} independent of UU.
Let

|  |  |  |
| --- | --- | --- |
|  | Y′=FY∣X−1​(U1∣X1)​and​Z′=FZ∣X,Y−1​(U2∣X,Y′),Y^{\prime}=F\_{Y\mid X}^{-1}\left(U\_{1}\mid X\_{1}\right)~\text{and}~Z^{\prime}=F\_{Z\mid X,Y}^{-1}\left(U\_{2}\mid X,Y^{\prime}\right), |  |

where FY∣X−1(⋅∣y)F\_{Y\mid X}^{-1}(\cdot\mid y) is the conditional quantile function of YY given Y1=yY\_{1}=y and FZ∣X,Y−1(⋅∣x,y)F\_{Z\mid X,Y}^{-1}\left(\cdot\mid x,y\right) is the quantile function of ZZ given (X,Y)=(x,y)∈ℝ+2\left(X,Y\right)=\left(x,y\right)\in\mathbb{R}\_{+}^{2}. By construction, we have (X,Y,Z)=d(X,Y′,Z′)\left(X,Y,Z\right)\stackrel{{\scriptstyle\mathrm{d}}}{{=}}\left(X,Y^{\prime},Z^{\prime}\right) and Y′+Z′=Y+Z=XY^{\prime}+Z^{\prime}=Y+Z=X.
By Proposition 1 of Liu et al., ([2020](https://arxiv.org/html/2510.18236v1#bib.bib24))
and uniformly continuity of ρh\rho\_{h}, the constrained inf-convolution □i=m+1nρhi\mathop{\square}\displaylimits\_{i=m+1}^{n}\rho\_{h\_{i}}
is law-invariant; thus ([5](https://arxiv.org/html/2510.18236v1#S3.E5 "In 3 Problem reduction ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) follows.
Also, Theorem 3 of Ghossoub et al., ([2024](https://arxiv.org/html/2510.18236v1#bib.bib14)) identifies the inner inf-convolution in ([6](https://arxiv.org/html/2510.18236v1#S3.E6 "In 3 Problem reduction ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")):

|  |  |  |
| --- | --- | --- |
|  | □i=1mρhi​(X)=ρg1​(X)​and​□i=m+1nρhi​(X)=ρg2​(X)​for​X∈𝒳⟂,\mathop{\square}\displaylimits\_{i=1}^{m}\rho\_{h\_{i}}(X)=\rho\_{g\_{1}}(X)~\text{and}~\mathop{\square}\displaylimits\_{i=m+1}^{n}\rho\_{h\_{i}}(X)=\rho\_{g\_{2}}(X)~\text{for}~X\in\mathcal{X}^{\perp}, |  |

with concave distortion functions hih\_{i}, i∈[m]i\in[m] and
convex distortion functions hih\_{i}, i∈[n]∖[m]i\in[n]\setminus[m].
∎

The first part of Theorem [1](https://arxiv.org/html/2510.18236v1#Thmtheorem1 "Theorem 1. ‣ 3 Problem reduction ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") also holds for the expected utility model; see Lauzier et al., ([2025](https://arxiv.org/html/2510.18236v1#bib.bib21)). This can be generalized to other decision models accounting for risk-averse and risk-seeking behaviors.
In Theorem [1](https://arxiv.org/html/2510.18236v1#Thmtheorem1 "Theorem 1. ‣ 3 Problem reduction ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"), g1g\_{1} is concave and g2g\_{2} is convex. Equation ([3](https://arxiv.org/html/2510.18236v1#S3.E3 "In item (ii) ‣ Theorem 1. ‣ 3 Problem reduction ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) shows that, under appropriate assumptions,
the nn-agent problem reduces to risk sharing between a representative risk-averse agent with distortion function g1g\_{1} and a representative risk-seeking agent with distortion function g2g\_{2}.
The intuition behind this result is that agents with similar risk attitudes can be treated collectively: among the risk-averse agents, comonotonic allocations are optimal, while among the risk-seeking agents, counter-monotonic allocations are optimal. Hence, the only remaining complexity lies in how the total risk is divided between these two representative agents.

It is important to note that g2g\_{2}, being the inf-convolution of several convex distortion functions, is not necessarily a distortion function. In fact, one typically has g2​(1)<1g\_{2}(1)<1 unless all underlying hi,i∈[n]h\_{i},i\in[n] are the identity. Let g^2=g2/g2​(1)\hat{g}\_{2}=g\_{2}/g\_{2}(1) the normalization of g2g\_{2}. Clearly, such normalization would not change the preferences of the agent and a Pareto-optimal allocation for agents using ρg1\rho\_{g\_{1}} and ρg2\rho\_{g\_{2}} is also Pareto optimal for agents using ρg1\rho\_{g\_{1}} and ρg^2\rho\_{\hat{g}\_{2}}. This observation motivates the next step of our analysis, where we examine the detailed two-agent model in detail, showing how the form of distortion functions drives the optimal risk sharing.

## 4 Allocations in the whole space

In this section, we consider an economy with two agents who may have different risk preferences.
As shown by Example [1](https://arxiv.org/html/2510.18236v1#Thmexample1 "Example 1. ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") below, a Pareto-optimal allocation may fail to exist in the presence of risk-seeking behavior; this is a known phenomenon of risk-seeking agents.
One possible resolution is to impose constraints on admissible allocations.
Our first step, however, is to identify conditions on the distortion functions under which a Pareto-optimal allocation exists even without any external constraints. Throughout this section, we will work on the space 𝒳=L∞\mathcal{X}=L^{\infty}.
In Section [5](https://arxiv.org/html/2510.18236v1#S5 "5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"), we turn to the setting with boundedness constraints on each individual allocation, where the existence of the inf-convolution is guaranteed.

###### Example 1.

Consider two agents sharing a sure amount X=1X=1. Agent 1 is extremely risk-seeking with h1​(x)=𝟙{x=1}h\_{1}(x)=\mathbb{1}\_{\{x=1\}}, and Agent 2 is risk-averse with distortion h2​(x)=xh\_{2}(x)=\sqrt{x}. Fix any event A∈ℱA\in\mathcal{F} with 0<ℙ​(A)<10<\mathbb{P}(A)<1 and an arbitrary scalar a>0a>0, consider the allocation
(X1,X2)=(a​𝟙A, 1−a​𝟙A)(X\_{1},X\_{2})=(a\,\mathbb{1}\_{A},\;1-a\,\mathbb{1}\_{A}).
A direct calculation yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​(a​𝟙A)+ρh2​(1−a​𝟙A)=1−a​h~2​(ℙ​(A)).\displaystyle\rho\_{h\_{1}}(a\mathbb{1}\_{A})+\rho\_{h\_{2}}(1-a\mathbb{1}\_{A})=1-a\,\widetilde{h}\_{2}(\mathbb{P}(A)). |  | (7) |

Since h~2​(ℙ​(A))>0\widetilde{h}\_{2}\!\big(\mathbb{P}(A)\big)>0, the right-hand side of ([7](https://arxiv.org/html/2510.18236v1#S4.E7 "In Example 1. ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) tends to −∞-\infty as a→∞a\to\infty. Thus, by taking unbounded bets on AA, the total measured risk can be driven arbitrarily negative. Intuitively, any gamble of the form a​𝟙Aa\,\mathbb{1}\_{A} with 0<ℙ​(A)<10<\mathbb{P}(A)<1 is perceived by Agent 1 as perfectly safe, no matter how large aa is. The balancing position 1−a​𝟙A1-a\,\mathbb{1}\_{A} falls to Agent 2, whose concave distortion function evaluates this exposure ever more negatively.
Together, this makes the pair drive the total risk down without bound. Hence, a Pareto-optimal allocation fails to exist because one side can always “game” the allocation by scaling up risky bets.

### 4.1 Two general agents

We now present our first main result, which establishes necessary and sufficient conditions for the existence of a well-defined optimal risk sharing value between two agents with heterogeneous distortion preferences.

###### Theorem 2.

Suppose that 𝒳=L∞\mathcal{X}=L^{\infty}.
For any h1h\_{1}, h2∈ℋh\_{2}\in\mathcal{H}, the following are equivalent.

1. (i)

   h1​□h2​(1)=1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)=1; equivalently, h1≥h~2h\_{1}\geq\widetilde{h}\_{2}.
2. (ii)

   ρh1​□ρh2​(c)=c\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(c)=c for any c∈ℝc\in\mathbb{R}.
3. (iii)

   ρh1​□ρh2​(X)>−∞\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)>-\infty holds for any X∈𝒳X\in\mathcal{X}.
4. (iv)

   ρh1​□ρh2​(X)>−∞\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)>-\infty holds for some X∈𝒳X\in\mathcal{X}.

###### Proof.

(i) →\rightarrow (ii):
Note that the condition h1​□h2​(1)=1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)=1 is equivalent to h1≥h~2h\_{1}\geq\widetilde{h}\_{2} on [0,1][0,1]. This implies that ρh1​(Y)≥ρh~2​(Y)\rho\_{h\_{1}}(Y)\geq\rho\_{\widetilde{h}\_{2}}(Y) for any Y∈L∞Y\in{L}^{\infty}.
Using translation invariance of ρh2\rho\_{h\_{2}}, we obtain

|  |  |  |
| --- | --- | --- |
|  | ρh1​□ρh2​(c)=infY∈𝒳{ρh1​(Y)+ρh2​(c−Y)}=infY∈𝒳{c+ρh1​(Y)−ρh~2​(Y)}≥c.\displaystyle\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(c)=\inf\_{Y\in\mathcal{X}}\left\{\rho\_{h\_{1}}(Y)+\rho\_{h\_{2}}(c-Y)\right\}=\inf\_{Y\in\mathcal{X}}\left\{c+\rho\_{h\_{1}}(Y)-\rho\_{\widetilde{h}\_{2}}(Y)\right\}\geq c. |  |

On the other hand, it is always the case that ρh1​□ρh2​(c)≤c\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(c)\leq c, for c∈ℝc\in\mathbb{R}. Hence, the equality follows.

(ii) →\rightarrow (iii):
Take X∈𝒳X\in\mathcal{X} and Z=X−ess​-​inf​X≥0Z=X-\mathrm{ess\mbox{-}inf}X\geq 0. By monotonicity of ρh2\rho\_{h\_{2}}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​□ρh2​(X)\displaystyle\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X) | =ρh1​□ρh2​(Z+ess​-​inf​X)\displaystyle=\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(Z+\mathrm{ess\mbox{-}inf}X) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =infY∈𝒳{ρh1​(Y)+ρh2​(Z+ess​-​inf​X−Y)}\displaystyle=\inf\_{Y\in\mathcal{X}}\left\{\rho\_{h\_{1}}(Y)+\rho\_{h\_{2}}(Z+\mathrm{ess\mbox{-}inf}X-Y)\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥infY∈𝒳{ρh1​(Y)+ρh2​(ess​-​inf​X−Y)}\displaystyle\geq\inf\_{Y\in\mathcal{X}}\left\{\rho\_{h\_{1}}(Y)+\rho\_{h\_{2}}(\mathrm{ess\mbox{-}inf}X-Y)\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ρh1​□ρh2​(ess​-​inf​X)=ess​-​inf​X>−∞.\displaystyle=\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(\mathrm{ess\mbox{-}inf}X)=\mathrm{ess\mbox{-}inf}X>-\infty. |  |

(iii) →\rightarrow (iv): Immediate.

(iv) →\rightarrow (i):
We argue by contradiction. Assume that h1​□h2​(1)<1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)<1, i.e.,
there exists m∈[0,1]m\in[0,1] such that h1​(m)<h~2​(m)h\_{1}(m)<\widetilde{h}\_{2}(m).
Construct a zero-sum allocation (Y,−Y)(Y,-Y) with Y=2​a​𝟙A−aY=2a\mathbb{1}\_{A}-a, a>0a>0 and ℙ​(A)=m\mathbb{P}(A)=m.
Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​□ρh2​(0)\displaystyle\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(0) | ≤ρh1​(2​a​𝟙A−a)+ρh2​(2​a​𝟙Ac−a)\displaystyle\leq\rho\_{h\_{1}}(2a\mathbb{1}\_{A}-a)+\rho\_{h\_{2}}(2a\mathbb{1}\_{A^{c}}-a) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​a​h1​(ℙ​(A))+2​a​h2​(1−ℙ​(A))−2​a\displaystyle=2ah\_{1}(\mathbb{P}(A))+2ah\_{2}(1-\mathbb{P}(A))-2a |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​a​(h1​(m)−h~2​(m)).\displaystyle=2a(h\_{1}(m)-\widetilde{h}\_{2}(m)). |  |

As a→∞a\rightarrow\infty, ρh1​□ρh2​(0)→−∞\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(0)\rightarrow-\infty.
For any X∈𝒳X\in\mathcal{X},
by the fact of X≤ess​-​sup​XX\leq\mathrm{ess\mbox{-}sup}X, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​□ρh2​(X)\displaystyle\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X) | ≤ρh1​□ρh2​(0)+ess​-​sup​X=−∞,\displaystyle\leq\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(0)+\mathrm{ess\mbox{-}sup}X=-\infty, |  |

which leads to a contradiction. Therefore, we conclude h1​(x)≥h~2​(x)h\_{1}(x)\geq\widetilde{h}\_{2}(x) for x∈[0,1]x\in[0,1], which implies that h1​□h2​(1)=1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)=1.
∎

In fact, condition (i) in Theorem [2](https://arxiv.org/html/2510.18236v1#Thmtheorem2 "Theorem 2. ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") captures a dominance of caution over speculation in the perception of risk, when both risk-averse and risk-seeking behaviors coexist. This condition requires that the cautious agent’s loss weights are strong enough to offset the other’s optimism at each quantile level, in the sense that h1h\_{1} never falls below the dual h~2\widetilde{h}\_{2}.
As a result, this condition prevents the “gambling” agent from driving the total risk value to −∞-\infty. Without this no-free-gambling condition, the risk-sharing mechanism may fail, allowing one agent to absorb all risk without sufficient penalty.

###### Remark 1.

Theorem [2](https://arxiv.org/html/2510.18236v1#Thmtheorem2 "Theorem 2. ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") yields a criterion for when the inf-convolution of two distortion risk measures cannot admit a finite and attainable minimum. If h1​□h2​(1)<1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)<1, then ρh1​□ρh2​(X)=−∞\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)=-\infty holds for any X∈𝒳X\in\mathcal{X}, implying that the inf-convolution cannot be exact at XX.

We now highlight several well-known instances that Theorem [2](https://arxiv.org/html/2510.18236v1#Thmtheorem2 "Theorem 2. ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") recovers.

###### Example 2 (Two risk-averse agents).

If both h1h\_{1} and h2h\_{2} are concave, then condition (i) in Theorem [2](https://arxiv.org/html/2510.18236v1#Thmtheorem2 "Theorem 2. ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") is satisfied; i.e., h1≥h~2h\_{1}\geq\widetilde{h}\_{2} since h~2\widetilde{h}\_{2} is convex. In particular, for a constant total risk, any risk-free split is Pareto optimal.

###### Example 3 (Two risk-seeking agents).

If both h1h\_{1} and h2h\_{2} are convex and neither is the identity, then h1<h~2h\_{1}<\widetilde{h}\_{2} since h~2\widetilde{h}\_{2} is concave. By Theorem [2](https://arxiv.org/html/2510.18236v1#Thmtheorem2 "Theorem 2. ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"), it follows that

|  |  |  |
| --- | --- | --- |
|  | ρh1​□ρh2​(X)=−∞,for​X∈𝒳,\displaystyle\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)=-\infty,\ \text{for}\ X\in\mathcal{X}, |  |

which is consistent with the result established in Proposition 2 of Ghossoub et al., ([2024](https://arxiv.org/html/2510.18236v1#bib.bib14)).

###### Example 4 (Inf-convolution of VaRs).

By Corollary 2 of Embrechts et al., ([2018](https://arxiv.org/html/2510.18236v1#bib.bib10)), for α1,α2≥0\alpha\_{1},\alpha\_{2}\geq 0, we have

|  |  |  |
| --- | --- | --- |
|  | VaRα1​□VaRα2​(X)=VaRα1+α2​(X),for​X∈𝒳.\displaystyle\mathrm{VaR}\_{\alpha\_{1}}\mathop{\square}\displaylimits\mathrm{VaR}\_{\alpha\_{2}}(X)=\mathrm{VaR}\_{\alpha\_{1}+\alpha\_{2}}(X),\ \text{for}\ X\in\mathcal{X}. |  |

Note that for α≥1\alpha\geq 1, VaRα​(X)=−∞\mathrm{VaR}\_{\alpha}(X)=-\infty for X∈𝒳X\in\mathcal{X}. Therefore,
if α1+α2≥1\alpha\_{1}+\alpha\_{2}\geq 1, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRα1​□VaRα2​(X)=−∞,for​X∈𝒳.\displaystyle\mathrm{VaR}\_{\alpha\_{1}}\mathop{\square}\displaylimits\mathrm{VaR}\_{\alpha\_{2}}(X)=-\infty,\ \text{for}\ X\in\mathcal{X}. |  | (8) |

This conclusion also follows directly from Theorem [2](https://arxiv.org/html/2510.18236v1#Thmtheorem2 "Theorem 2. ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"). In this case, the two agents are associated with distortion functions h1​(x)=𝟙{x>α1}h\_{1}(x)=\mathbb{1}\_{\left\{x>\alpha\_{1}\right\}} and h2​(x)=𝟙{x>α2}h\_{2}(x)=\mathbb{1}\_{\left\{x>\alpha\_{2}\right\}}, respectively. Indeed, h1​□h2​(1)=0≠1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)=0\neq 1 with α1+α2≥1\alpha\_{1}+\alpha\_{2}\geq 1, and Theorem [2](https://arxiv.org/html/2510.18236v1#Thmtheorem2 "Theorem 2. ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") then yields ([8](https://arxiv.org/html/2510.18236v1#S4.E8 "In Example 4 (Inf-convolution of VaRs). ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")).

As a direct application of Theorem [2](https://arxiv.org/html/2510.18236v1#Thmtheorem2 "Theorem 2. ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"), we now investigate the special case where one agent’s distortion function is the dual of the other’s.
This setting is of particular interest because the pair (h,h~)(h,\widetilde{h}) acts as a “mirror” on the same risk. Valuing a loss with hh equals (up to sign) valuing a gain with the dual h~\widetilde{h}.
The following proposition shows that, under this mirror setting, the inf-convolution is always well-defined, and it even reduces to a particularly simple form when one agent is risk averse (the mirror agent is necessarily risk seeking).

###### Proposition 1.

Suppose that 𝒳=L∞\mathcal{X}=L^{\infty}.
For any h∈ℋh\in\mathcal{H} and X∈𝒳X\in\mathcal{X}, the following hold.

1. (i)

   |ρh​□ρh~​(X)|≤∥X∥∞\lvert\rho\_{h}\mathop{\square}\displaylimits\rho\_{\widetilde{h}}(X)\rvert\leq\lVert X\rVert\_{\infty}.
2. (ii)

   ρh​□ρh~​(X)>−∞\rho\_{h}\mathop{\square}\displaylimits\rho\_{\widetilde{h}}(X)>-\infty.
3. (iii)

   ρh​□ρh~​(c)=c\rho\_{h}\mathop{\square}\displaylimits\rho\_{\widetilde{h}}(c)=c for any constant c∈ℝc\in\mathbb{R}.
4. (iv)

   If hh or h~\widetilde{h} is concave, then
   ρh​□ρh~=ρh​□h~=ρh∧h~\rho\_{h}\mathop{\square}\displaylimits\rho\_{\widetilde{h}}=\rho\_{h\mathop{\square}\displaylimits\widetilde{h}}=\rho\_{h\wedge\widetilde{h}}.

###### Proof.

(i). For any h∈ℋh\in\mathcal{H}, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh​□ρh~​(X)=\displaystyle\rho\_{h}\mathop{\square}\displaylimits\rho\_{\widetilde{h}}(X)= | infY∈𝒳{ρh​(Y)+ρh~​(X−Y)}=infY∈𝒳{ρh​(Y)−ρh​(Y−X)}.\displaystyle\inf\_{Y\in\mathcal{X}}\left\{\rho\_{h}(Y)+\rho\_{\widetilde{h}}(X-Y)\right\}=\inf\_{Y\in\mathcal{X}}\left\{\rho\_{h}(Y)-\rho\_{h}(Y-X)\right\}. |  |

Then we have

|  |  |  |
| --- | --- | --- |
|  | |ρh​□ρh~​(X)|≤infY∈𝒳{|ρh​(Y)−ρh​(Y−X)|}≤∥X∥∞.\displaystyle\lvert\rho\_{h}\mathop{\square}\displaylimits\rho\_{\widetilde{h}}(X)\rvert\leq\inf\_{Y\in\mathcal{X}}\left\{\lvert\rho\_{h}(Y)-\rho\_{h}(Y-X)\rvert\right\}\leq\lVert X\rVert\_{\infty}. |  |

The second inequality holds since ρh\rho\_{h} is lipschitz-continuous with respect to L∞L^{\infty} -norm.

(ii) and (iii) follow directly from Theorem [2](https://arxiv.org/html/2510.18236v1#Thmtheorem2 "Theorem 2. ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"), since h​□h~​(1)=1h\mathop{\square}\displaylimits\widetilde{h}(1)=1.

(iv). Without loss of generality, we assume that hh is concave. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh​□ρh~​(X)\displaystyle\rho\_{h}\mathop{\square}\displaylimits\rho\_{\widetilde{h}}(X) | =infY∈𝒳{ρh​(Y)+ρh~​(X−Y)}\displaystyle=\inf\_{Y\in\mathcal{X}}\left\{\rho\_{h}(Y)+\rho\_{\widetilde{h}}(X-Y)\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥infY∈𝒳{ρh​(Y)+ρh~​(X)+ρh~​(−Y)}=ρh~​(X).\displaystyle\geq\inf\_{Y\in\mathcal{X}}\left\{\rho\_{h}(Y)+\rho\_{\widetilde{h}}(X)+\rho\_{\widetilde{h}}(-Y)\right\}=\rho\_{\widetilde{h}}(X). |  |

Also, ρh​□ρh~≤ρh~\rho\_{h}\mathop{\square}\displaylimits\rho\_{\widetilde{h}}\leq\rho\_{\widetilde{h}} holds. Thus, we obtain ρh​□ρh~=ρh~\rho\_{h}\mathop{\square}\displaylimits\rho\_{\widetilde{h}}=\rho\_{\widetilde{h}}.
A symmetric argument applies if h~\widetilde{h} is concave.
Consequently, we obtain ρh​□ρh~=ρh∧h~\rho\_{h}\mathop{\square}\displaylimits\rho\_{\widetilde{h}}=\rho\_{h\wedge\widetilde{h}}.

Next, we show that ρh∧h~=ρh​□​h~\rho\_{h\wedge\widetilde{h}}=\rho\_{h\square\widetilde{h}}. Note that h​□​h~​(1)=1h\square\widetilde{h}(1)=1, and hence it suffices to show that h∧h~=h​□​h~h\wedge\widetilde{h}=h\square\widetilde{h}. Let g​(y)=h​(y)−h​(1−x+y)g(y)=h(y)-h(1-x+y), for each x∈[0,1]x\in[0,1]. Then g​(y)g(y) is non-decreasing in y∈[0,x]y\in[0,x] due to concavity of hh.
Therefore, g​(y)g(y) attains its infimum at the endpoints y=0y=0. Then it follows that

|  |  |  |
| --- | --- | --- |
|  | h​□​h~​(x)=inf0≤y≤x{h​(y)+h~​(x−y)}=1+inf0≤y≤x{h​(y)−h​(1−x+y)}=h~​(x).\displaystyle h\square\widetilde{h}(x)=\inf\_{0\leq y\leq x}\left\{h(y)+\widetilde{h}(x-y)\right\}=1+\inf\_{0\leq y\leq x}\left\{h(y)-h(1-x+y)\right\}=\widetilde{h}(x). |  |

Similarly, if h~\widetilde{h} is concave, we have h​□​h~​(x)=h​(x)h\square\widetilde{h}(x)=h(x).
∎

### 4.2 One risk-averse agent and one risk-seeking agent

To approach a solution to ([3](https://arxiv.org/html/2510.18236v1#S3.E3 "In item (ii) ‣ Theorem 1. ‣ 3 Problem reduction ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")), we now analyze the two-agent setting in detail.
The following theorem identifies structural conditions on the distortion functions under which the inf-convolution admits a simple representation, including cases in which one agent is risk averse or risk seeking.

###### Theorem 3.

Suppose that 𝒳=L∞\mathcal{X}=L^{\infty} and
h1,h2∈ℋh\_{1},h\_{2}\in\mathcal{H}. The following hold.

* (i)

  If h1∧h2h\_{1}\wedge h\_{2} is concave, then ρh1​□ρh2=ρh1​□h2=ρh1∧h2\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}=\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}=\rho\_{h\_{1}\wedge h\_{2}}.
* (ii)

  If h2h\_{2} is convex, then ρh1​□ρh2=ρh2\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}=\rho\_{h\_{2}} if and only if h1​□h2​(1)=1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)=1.

###### Proof.

(i)
By concavity of h1∧h2h\_{1}\wedge h\_{2}, we have

|  |  |  |
| --- | --- | --- |
|  | h1​□h2≥(h1∧h2)​□(h1∧h2)=h1∧h2.\displaystyle h\_{1}\mathop{\square}\displaylimits h\_{2}\geq(h\_{1}\wedge h\_{2})\mathop{\square}\displaylimits(h\_{1}\wedge h\_{2})=h\_{1}\wedge h\_{2}. |  |

On the other hand, it is clear that h1​□h2≤h1∧h2h\_{1}\mathop{\square}\displaylimits h\_{2}\leq h\_{1}\wedge h\_{2}. Hence, we conclude h1​□h2=h1∧h2h\_{1}\mathop{\square}\displaylimits h\_{2}=h\_{1}\wedge h\_{2}. Then it suffices to show ρh1​□ρh2=ρh1∧h2\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}=\rho\_{h\_{1}\wedge h\_{2}}. For X∈𝒳X\in\mathcal{X} and
(X1,X2)∈𝔸2​(X)(X\_{1},X\_{2})\in\mathbb{A}\_{2}(X), we have

|  |  |  |
| --- | --- | --- |
|  | ρh1​(X1)+ρh2​(X2)≥ρh1∧h2​(X1)+ρh1∧h2​(X2)≥ρh1∧h2​(X).\displaystyle\rho\_{h\_{1}}(X\_{1})+\rho\_{h\_{2}}(X\_{2})\geq\rho\_{h\_{1}\wedge h\_{2}}(X\_{1})+\rho\_{h\_{1}\wedge h\_{2}}(X\_{2})\geq\rho\_{h\_{1}\wedge h\_{2}}(X). |  |

This implies that ρh1​□ρh2≥ρh1∧h2\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}\geq\rho\_{h\_{1}\wedge h\_{2}}.
The last inequality follows from the equivalence between concavity of h1∧h2h\_{1}\wedge h\_{2} and subadditivity of ρh1∧h2\rho\_{h\_{1}\wedge h\_{2}}; see Theorem 3 of Wang et al., ([2020](https://arxiv.org/html/2510.18236v1#bib.bib30)).
Furthermore, ρh1​□ρh2≤ρh1∧h2\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}\leq\rho\_{h\_{1}\wedge h\_{2}} holds. Therefore, the desired result is obtained.

(ii) “If”: Note that h1​□h2​(1)=1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)=1 is equivalent to h1≥h~2h\_{1}\geq\widetilde{h}\_{2}. For any X,Y∈𝒳X,Y\in\mathcal{X},
it follows that

|  |  |  |
| --- | --- | --- |
|  | ρh1​(Y)+ρh2​(X−Y)≥ρh1​(Y)+ρh2​(X)−ρh~2​(Y)≥ρh2​(X).\displaystyle\rho\_{h\_{1}}(Y)+\rho\_{h\_{2}}(X-Y)\geq\rho\_{h\_{1}}(Y)+\rho\_{h\_{2}}(X)-\rho\_{\widetilde{h}\_{2}}(Y)\geq\rho\_{h\_{2}}(X). |  |

The second inequality holds due to the convexity of h2h\_{2}.
The above result implies that ρh1​□ρh2≥ρh2\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}\geq\rho\_{h\_{2}}. Also, it is immediate that ρh1​□ρh2≤ρh2\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}\leq\rho\_{h\_{2}}. Hence, the equality holds.

“Only if”: Let X=𝟙AX=\mathbb{1}\_{A} and x=ℙ​(A)x=\mathbb{P}(A).
Take an allocation (X1,X2)(X\_{1},X\_{2}) of XX as: X1=𝟙BX\_{1}=\mathbb{1}\_{B}
and X2=𝟙A∖BX\_{2}=\mathbb{1}\_{A\setminus B}. Write y=ℙ​(B)y=\mathbb{P}(B). Then it follows that

|  |  |  |
| --- | --- | --- |
|  | ρh1​(X1)+ρh2​(X2)=h1​(y)+h2​(x−y)​and​ρh2​(X)=h2​(x).\displaystyle\rho\_{h\_{1}}(X\_{1})+\rho\_{h\_{2}}(X\_{2})=h\_{1}(y)+h\_{2}(x-y)\ \text{and}\ \rho\_{h\_{2}}(X)=h\_{2}(x). |  |

By the condition ρh1​□ρh2=ρh2\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}=\rho\_{h\_{2}}, we have h1​(y)+h2​(x−y)≥h2​(x)h\_{1}(y)+h\_{2}(x-y)\geq h\_{2}(x) for any x∈[0,1]x\in[0,1]. Consequently,
h1​(y)+h2​(1−y)≥1h\_{1}(y)+h\_{2}(1-y)\geq 1 for any y∈[0,1]y\in[0,1], implying that h1​□h2​(1)=1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)=1.
∎

Theorem [3](https://arxiv.org/html/2510.18236v1#Thmtheorem3 "Theorem 3. ‣ 4.2 One risk-averse agent and one risk-seeking agent ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") provides some insights for the mixed two-agent case (one risk-averse and one risk-seeking). In particular, if the existence condition h1​□h2​(1)=1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)=1 holds, i.e., the level of risk aversion dominates the level of risk seeking, then the allocation (X1,X2)=(0,X)(X\_{1},X\_{2})=(0,X) is optimal.
Intuitively, the “force” of caution of the risk-averse agent exceeds the “force” of gambling of the risk-seeking agent in this setting. As a result, the efficient arrangement is that the risk-seeking agent absorbs the entire uncertain part of the risk and the risk-averse agent holds the safe position.

It is important to note that in both cases in Theorem [3](https://arxiv.org/html/2510.18236v1#Thmtheorem3 "Theorem 3. ‣ 4.2 One risk-averse agent and one risk-seeking agent ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") and throughout Example [2](https://arxiv.org/html/2510.18236v1#Thmexample2 "Example 2 (Two risk-averse agents). ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")–[4](https://arxiv.org/html/2510.18236v1#Thmexample4 "Example 4 (Inf-convolution of VaRs). ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") (with existence conditions), the identity

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​□ρh2=ρh1​□h2\displaystyle\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}=\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}} |  | (9) |

always holds.
A natural question to ask is whether this relationship still holds in more general settings, especially when two agents’ are neither risk-averse nor risk-seeking.
In fact, the equality is not universal. Example [5](https://arxiv.org/html/2510.18236v1#Thmexample5 "Example 5 (𝜌_ℎ₁⁢□{𝜌_ℎ₂}=𝜌_{ℎ₁⁢□{ℎ₂}} does not always hold.). ‣ 4.2 One risk-averse agent and one risk-seeking agent ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") shows that if both agents have subadditive distortion functions, then equality ([9](https://arxiv.org/html/2510.18236v1#S4.E9 "In 4.2 One risk-averse agent and one risk-seeking agent ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) may fail once concavity is lost.

###### Example 5 (ρh1​□ρh2=ρh1​□h2\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}=\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}} does not always hold.).

Suppose that two agents share the same risk preference h∈ℋh\in\mathcal{H}, where hh is continuous and subadditive but not concave on [0,1][0,1].
Then there exists x,y∈[0,1]x,y\in[0,1] such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​h​(x/2+y/2)<h​(x)+h​(y).\displaystyle 2h(x/2+y/2)<h(x)+h(y). |  | (10) |

Consider the total risk X=𝟙A+𝟙BX=\mathbb{1}\_{A}+\mathbb{1}\_{B} with ℙ​(A)=ℙ​(B)=x/2+y/2\mathbb{P}(A)=\mathbb{P}(B)=x/2+y/2 and ℙ​(A∩B)=y\mathbb{P}(A\cap B)=y. Define an allocation (Y,Z)(Y,Z)
of XX with Y=𝟙AY=\mathbb{1}\_{A} and Z=𝟙BZ=\mathbb{1}\_{B}.
By ([10](https://arxiv.org/html/2510.18236v1#S4.E10 "In Example 5 (𝜌_ℎ₁⁢□{𝜌_ℎ₂}=𝜌_{ℎ₁⁢□{ℎ₂}} does not always hold.). ‣ 4.2 One risk-averse agent and one risk-seeking agent ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")), we can obtain that

|  |  |  |
| --- | --- | --- |
|  | ρh​(Y)+ρh​(Z)<ρh​(X)=h​(ℙ​(A∪B))+h​(ℙ​(A∩B)).\displaystyle\rho\_{h}(Y)+\rho\_{h}(Z)<\rho\_{h}(X)=h(\mathbb{P}(A\cup B))+h(\mathbb{P}(A\cap B)). |  |

Therefore, for such XX, we have ρh​□ρh​(X)<ρh​(X)=ρh​□h​(X)\rho\_{h}\mathop{\square}\displaylimits\rho\_{h}(X)<\rho\_{h}(X)=\rho\_{h\mathop{\square}\displaylimits h}(X). The equality holds due to subadditivity of hh, implying h​□h=hh\mathop{\square}\displaylimits h=h. Below we give a concrete example.
Let h​(x)=max⁡{x,2​x−x2}h(x)=\max\left\{\sqrt{x},2x-x^{2}\right\} for x∈[0,1]x\in[0,1]. Clearly, both x\sqrt{x} and 2​x−x22x-x^{2} are subadditive, hence
h​(x)h(x) is subadditive. Consider X=𝟙A+𝟙BX=\mathbb{1}\_{A}+\mathbb{1}\_{B} with ℙ​(A)=ℙ​(B)=0.38\mathbb{P}(A)=\mathbb{P}(B)=0.38 and ℙ​(A∩B)=0.26\mathbb{P}(A\cap B)=0.26.
Then we can calculate

|  |  |  |
| --- | --- | --- |
|  | ρh​(Y)+ρh​(Z)=2​h​(0.38)=1.233<ρh​(X)=h​(0.5)+h​(0.26)=1.260.\rho\_{h}(Y)+\rho\_{h}(Z)=2h(0.38)=1.233<\rho\_{h}(X)=h(0.5)+h(0.26)=1.260. |  |

Whereas the results in this section are presented for generality on the space 𝒳=L∞\mathcal{X}=L^{\infty}, the subsequent sections will focus on 𝒳=L+\mathcal{X}=L^{+}, the set of nonnegative random variables, where only nonnegative allocations are admissible to ensure well-defined risk-sharing problems.

## 5 Nonnegative allocations

Without any constraints on the allocation set, an optimal allocation may fail to exist under certain conditions, for instance, when h1​(x)<h~2​(x)h\_{1}(x)<\widetilde{h}\_{2}(x) on [0,1][0,1], as shown in Theorem [2](https://arxiv.org/html/2510.18236v1#Thmtheorem2 "Theorem 2. ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"). In this section, we consider the setting 𝒳=L+\mathcal{X}=L^{+}; that is, both the aggregate risk and the admissible allocations are required to be nonnegative.
This setting is economically intuitive: it means that for each agent, there cannot be
any profit from an aggregate pure loss. It is a natural assumption in many applications, such as peer-to-peer insurance.

Even with the nonnegativity constraint, solving ρh1​□ρh2\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}} with heterogeneous preferences can be challenging.
In this section, we proceed in two directions:
(i) we study the inf-convolution for specific structural classes of distortion functions h1h\_{1} and h2h\_{2};
(ii) we evaluate ρh1​□ρh2​(X)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X) for tractable classes of risks XX (e.g., Bernoulli-type random variables) without specifying the distortion type.
These studies also include, as notable special cases, settings with one risk-averse and one risk-seeking agent.

### 5.1 Two agents with special distortion functions

In analyzing risk sharing with specific preference classes, we focus on the relationship between the constrained inf-convolution ρh1​□ρh2\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}} and the benchmark ρh1​□h2\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}. We identify when this benchmark provides an upper bound for ρh1​□ρh2\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}} and when this bound is attained. Using ρh1​□h2\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}
as the benchmark is natural since, in all known tractable settings such as risk-averse/risk-seeking pairs and quantile-based specifications, one has the identity ([9](https://arxiv.org/html/2510.18236v1#S4.E9 "In 4.2 One risk-averse agent and one risk-seeking agent ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")).

An assumption of monotonicity of optimizers for h1​□h2h\_{1}\mathop{\square}\displaylimits h\_{2} would be important in the subsequent analysis.

###### Assumption COIN.

Let h1,h2∈ℋh\_{1},h\_{2}\in\mathcal{H}.
There exists an increasing function ff with x−f​(x)x-f(x) increasing such that h1​(f​(x))+h2​(x−f​(x))=h1​□h2​(x)h\_{1}(f(x))+h\_{2}(x-f(x))=h\_{1}\mathop{\square}\displaylimits h\_{2}(x).

Clearly, Assumption [COIN](https://arxiv.org/html/2510.18236v1#Thmassumption0.Thmassumptionalt1 "Assumption COIN. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") ensures that the optimal split of xx moves monotonically as xx increases; equivalently, there exists an increasing selector ff with a co-increasing residual x↦x−f​(x)x\mapsto x-f(x).
In particular, when both h1h\_{1} and h2h\_{2} are strictly convex, such selector exists; see Lemma 2 of Ghossoub et al., ([2024](https://arxiv.org/html/2510.18236v1#bib.bib14)).

###### Remark 2.

The importance of Assumption [COIN](https://arxiv.org/html/2510.18236v1#Thmassumption0.Thmassumptionalt1 "Assumption COIN. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") arises precisely when one attempts to achieves the benchmark value ρh1​□h2​(X)\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X) through an explicit allocation construction. To attain ρh1​□h2​(X)\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X), one would naturally construct an allocation (X1,X2)(X\_{1},X\_{2}) of XX so that the tail of each component corresponds to the optimal split of the tail of XX. This requires that the splitting function ff, which determines how the tail mass of XX is divided between X1X\_{1} and X2X\_{2}, moves monotonically with the tail level. Assumption [COIN](https://arxiv.org/html/2510.18236v1#Thmassumption0.Thmassumptionalt1 "Assumption COIN. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") ensures that the benchmark allocation is well-defined.

The following theorem shows that under Assumption [COIN](https://arxiv.org/html/2510.18236v1#Thmassumption0.Thmassumptionalt1 "Assumption COIN. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"), the constrained inf-convolution ρh1​□ρh2\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}} can always be bounded by ρh1​□h2\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}.

###### Theorem 4.

Suppose that Assumption [COIN](https://arxiv.org/html/2510.18236v1#Thmassumption0.Thmassumptionalt1 "Assumption COIN. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") holds and 𝒳=L+\mathcal{X}=L^{+}. For X∈𝒳X\in\mathcal{X}, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​□h2​□ρh1​□h2​(X)≤ρh1​□ρh2​(X)≤ρh1​□h2​(X).\displaystyle\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}\mathop{\square}\displaylimits\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X)\leq\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)\leq\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X). |  | (11) |

###### Proof.

Since h1​□h2≤min⁡{h1,h2}h\_{1}\mathop{\square}\displaylimits h\_{2}\leq\min\left\{h\_{1},h\_{2}\right\}, the monotonicity of distortion risk measures yields
the first inequality. It remains to show that ρh1​□ρh2​(X)≤ρh1​□h2​(X)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)\leq\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X).
For X≥0X\geq 0 and n∈ℕn\in\mathbb{N}, define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xn=∑i=0n​2n−1i2n​𝟙{i2n<X≤i+12n}+n​𝟙{X≥n},\displaystyle X\_{n}=\sum\_{i=0}^{n2^{n}-1}\frac{i}{2^{n}}\mathbb{1}\_{\left\{\frac{i}{2^{n}}<X\leq\frac{i+1}{2^{n}}\right\}}+n\mathbb{1}\_{\left\{X\geq n\right\}}, |  | (12) |

so that Xn↑XX\_{n}\uparrow X. Equivalently, ([12](https://arxiv.org/html/2510.18236v1#S5.E12 "In 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"))
can be formulated as:

|  |  |  |
| --- | --- | --- |
|  | Xn=12n​∑k=1n​2n𝟙Ank,where​Ank={X≥k2n},k∈[2n​n].\displaystyle X\_{n}=\frac{1}{2^{n}}\sum\_{k=1}^{n2^{n}}\mathbb{1}\_{A\_{n}^{k}},~\text{where}~A\_{n}^{k}=\left\{X\geq\frac{k}{2^{n}}\right\},k\in[2^{n}n]. |  |

Clearly, Ank⊆Ank−1A\_{n}^{k}\subseteq A\_{n}^{{k-1}} for k∈[2n​n]∖[1]k\in[2^{n}n]\setminus[1]. Hence, (𝟙An1,…,𝟙An2n​n)(\mathbb{1}\_{A\_{n}^{1}},\dots,\mathbb{1}\_{A\_{n}^{2^{n}n}}) is comonotonic.
Write pnk=ℙ​(Ank)p\_{n}^{k}=\mathbb{P}(A\_{n}^{k}) and 𝒮nk=arg⁡min0≤t≤pnk⁡{h1​(t)+h2​(pnk−t)}\mathcal{S}\_{n}^{k}=\operatorname\*{\arg\min}\_{0\leq t\leq p\_{n}^{k}}\left\{h\_{1}(t)+h\_{2}(p\_{n}^{k}-t)\right\} for k∈[2n​n]k\in[2^{n}n].
Let
unk∈𝒮nku\_{n}^{k}\in\mathcal{S}\_{n}^{k} be the selector within Assumption [COIN](https://arxiv.org/html/2510.18236v1#Thmassumption0.Thmassumptionalt1 "Assumption COIN. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") such that
unku\_{n}^{k} and pnk−xnkp\_{n}^{k}-x\_{n}^{k} are non-increasing in kk.
By comonotonic additivity of ρh1​□h2\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}},
it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​□h2​(Xn)\displaystyle\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X\_{n}) | =12n​∑k=1n​2nρh1​□h2​(𝟙Ank)=12n​∑k=1n​2nh1​□h2​(pnk)\displaystyle=\frac{1}{2^{n}}\sum\_{k=1}^{n2^{n}}\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(\mathbb{1}\_{A\_{n}^{k}})=\frac{1}{2^{n}}\sum\_{k=1}^{n2^{n}}{h\_{1}\mathop{\square}\displaylimits h\_{2}}(p\_{n}^{k}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12n​∑k=1n​2n(h1​(unk)+h2​(pnk−unk)).\displaystyle=\frac{1}{2^{n}}\sum\_{k=1}^{n2^{n}}(h\_{1}(u\_{n}^{k})+h\_{2}(p\_{n}^{k}-u\_{n}^{k})). |  |

Our goal is to construct an allocation (Yn,Zn)∈A2​(Xn)(Y\_{n},Z\_{n})\in A\_{2}(X\_{n}) such that ρh1​(Yn)+ρh1​(Zn)=ρh1​□h2​(Xn)\rho\_{h\_{1}}(Y\_{n})+\rho\_{h\_{1}}(Z\_{n})=\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X\_{n}) for each n∈ℕn\in\mathbb{N}.
Define the sets

|  |  |  |
| --- | --- | --- |
|  | Bnk=Bnk+1∪{FXn​(k2n)≤UXn<FXn​(k2n)+(unk−unk+1)},k=1,…,2n​n−1,\displaystyle B\_{n}^{k}=B\_{n}^{k+1}\cup\left\{F\_{X\_{n}}\left(\frac{k}{2^{n}}\right)\leq U\_{X\_{n}}<F\_{X\_{n}}\left(\frac{k}{2^{n}}\right)+(u\_{n}^{k}-u\_{n}^{k+1})\right\},~k=1,\dots,2^{n}n-1, |  |
|  |  |  |
| --- | --- | --- |
|  | Bn2n​n={FXn​(n)≤UXn<FXn​(n)+un2n​n}.\displaystyle B\_{n}^{2^{n}n}=\left\{F\_{X\_{n}}(n)\leq U\_{X\_{n}}<F\_{X\_{n}}(n)+u\_{n}^{2^{n}n}\right\}. |  |

Then for all k∈[2n​n]k\in[2^{n}n], we have
ℙ​(Bnk)=unk.\mathbb{P}(B\_{n}^{k})=u\_{n}^{k}.
It can also be verified that
Bnk⊆Bnk−1B\_{n}^{k}\subseteq B\_{n}^{k-1} and Ank\Bnk⊆Ank−1\Bnk−1A\_{n}^{k}\backslash B\_{n}^{k}\subseteq A\_{n}^{k-1}\backslash B\_{n}^{k-1} for k∈[2n​n]∖[1]k\in[2^{n}n]\setminus[1].
Define the allocation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yn=12n​∑k=1n​2n𝟙Bnk​and​Zn=12n​∑k=1n​2n𝟙Ank\Bnk.\displaystyle Y\_{n}=\frac{1}{2^{n}}\sum\_{k=1}^{n2^{n}}\mathbb{1}\_{B\_{n}^{k}}~\text{and}~Z\_{n}=\frac{1}{2^{n}}\sum\_{k=1}^{n2^{n}}\mathbb{1}\_{A\_{n}^{k}\backslash B\_{n}^{k}}. |  | (13) |

Clearly, Yn+Zn=XnY\_{n}+Z\_{n}=X\_{n} for each nn.
Moreover, comonotonic additivity leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​(Yn)+ρh2​(Zn)\displaystyle\rho\_{h\_{1}}(Y\_{n})+\rho\_{h\_{2}}(Z\_{n}) | =12n​∑k=1n​2n(h1​(ℙ​(Bnk))+h2​(ℙ​(Ank)−ℙ​(Bnk)))\displaystyle=\frac{1}{2^{n}}\sum\_{k=1}^{n2^{n}}\big(h\_{1}(\mathbb{P}(B\_{n}^{k}))+h\_{2}(\mathbb{P}(A\_{n}^{k})-\mathbb{P}(B\_{n}^{k}))\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12n​∑k=1n​2n(h1​(unk)+h2​(pnk−unk))\displaystyle=\frac{1}{2^{n}}\sum\_{k=1}^{n2^{n}}\big({h\_{1}}(u\_{n}^{k})+h\_{2}(p\_{n}^{k}-u\_{n}^{k})\big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =12n​∑k=1n​2nh1​□h2​(pnk)=ρh1​□h2​(Xn).\displaystyle=\frac{1}{2^{n}}\sum\_{k=1}^{n2^{n}}h\_{1}\mathop{\square}\displaylimits h\_{2}(p\_{n}^{k})=\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X\_{n}). |  | (14) |

Consequently, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​□ρh2​(X)\displaystyle\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X) | =limn→∞ρh1​□ρh2​(Xn)\displaystyle=\lim\_{n\rightarrow\infty}\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X\_{n}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤limn→∞(ρh1​(Yn)+ρh2​(Zn))=limn→∞ρh1​□h2​(Xn)=ρh1​□h2​(X).\displaystyle\leq\lim\_{n\rightarrow\infty}\big(\rho\_{h\_{1}}(Y\_{n})+\rho\_{h\_{2}}(Z\_{n})\big)=\lim\_{n\rightarrow\infty}\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X\_{n})=\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X). |  |

The first equality holds since ρh1​□ρh2\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}} is continuous from below; see Lemma [2](https://arxiv.org/html/2510.18236v1#Thmlemma2 "Lemma 2. ‣ Appendix B Basic properties of the constrained inf-convolution ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") in Appendix [A](https://arxiv.org/html/2510.18236v1#A1 "Appendix A Details in Example 8 ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")
for more details. Therefore, the result implies that ρh1​□ρh2​(X)≤ρh1​□h2​(X)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)\leq\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X).
∎

As we can see, Theorem [4](https://arxiv.org/html/2510.18236v1#Thmtheorem4 "Theorem 4. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") is non-constructive and it does not specify an allocation that attains the upper bound ρh1​□h2​(X)\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X). On an atomless space, however, when there exists a uniform random variable independent of XX, the attainable allocation is available; see Lemma 3 of Lauzier et al., ([2025](https://arxiv.org/html/2510.18236v1#bib.bib21)).

As noted earlier, Assumption [COIN](https://arxiv.org/html/2510.18236v1#Thmassumption0.Thmassumptionalt1 "Assumption COIN. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") holds whenever both h1h\_{1} and h2h\_{2} are convex; however, convexity is not required. There exists nonconvex pairs (h1,h2)(h\_{1},h\_{2}) that still admits such an increasing minimizer, as demonstrated in Example [6](https://arxiv.org/html/2510.18236v1#Thmexample6 "Example 6. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") involving a risk-averse agent and a risk-seeking agent. Therefore, Theorem [4](https://arxiv.org/html/2510.18236v1#Thmtheorem4 "Theorem 4. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") applies strictly beyond the convex setting.

###### Example 6.

Let g1​(x)=max⁡{0,4/3​(x−1/4)}g\_{1}(x)=\max\left\{0,4/3(x-1/4)\right\} and
g2​(x)=min⁡{8/7​x,1}g\_{2}(x)=\min\left\{8/7x,1\right\}
for x∈[0,1]x\in[0,1].
Clearly, g1g\_{1} is convex and g2g\_{2} is concave with g2≤g~1g\_{2}\leq\widetilde{g}\_{1}.
Then we can calculate
g1​□g2​(x)=max⁡{0,8/7​(x−1/4)}.g\_{1}\mathop{\square}\displaylimits g\_{2}(x)=\max\left\{0,8/7(x-1/4)\right\}.
Define f​(x)=min⁡{x,1/4}f(x)=\min\left\{x,1/4\right\}, thus x−f​(x)=max⁡{0,x−1/4}x-f(x)=\max\left\{0,x-1/4\right\}. Both f​(x)f(x) and x−f​(x)x-f(x) are non-decreasing; see Figure [1](https://arxiv.org/html/2510.18236v1#S5.F1 "Figure 1 ‣ Example 6. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") for a detailed illustration.
It can be verified that
g1​(f​(x))+g2​(x−f​(x))=g1​□g2​(x)g\_{1}(f(x))+g\_{2}(x-f(x))=g\_{1}\mathop{\square}\displaylimits g\_{2}(x) for x∈[0,1]x\in[0,1].

![Refer to caption](x1.png)


a g1,g2g\_{1},g\_{2} and g1​□g2g\_{1}\mathop{\square}\displaylimits g\_{2}

![Refer to caption](x2.png)


b Optimizer for g1​□g2g\_{1}\mathop{\square}\displaylimits g\_{2}

Figure 1: An illustration of g1​□g2g\_{1}\mathop{\square}\displaylimits g\_{2} with a=1/4a=1/4 and b=7/8b=7/8

In fact, the second inequality in ([11](https://arxiv.org/html/2510.18236v1#S5.E11 "In Theorem 4. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) becomes an equality when the two agents’ distortion functions are of the type described in Example [6](https://arxiv.org/html/2510.18236v1#Thmexample6 "Example 6. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").
Before stating that result, we provide a technical lemma that will be used in the sequel, which analyzes risk sharing between a VaR agent and a distortion agent.
The result also generalizes Theorem 5.3 of Wang and Wei, ([2020](https://arxiv.org/html/2510.18236v1#bib.bib29)).
To make the statement more precise, we introduce the following notation. For h∈ℋh\in\mathcal{H}, let α​(h)=sup{t∈[0,1]:h​(t)=0}\alpha(h)=\sup\left\{t\in[0,1]:h(t)=0\right\}. The function

|  |  |  |
| --- | --- | --- |
|  | h^​(t)=h​((t+α​(h))∧1),t∈[0,1]\hat{h}(t)=h((t+\alpha(h))\wedge 1),\ \ t\in[0,1] |  |

is called the active part of hh. Additionally, let ha​(t)=h​((t−a)+)h^{a}(t)=h((t-a)\_{+}) for t∈[0,1]t\in[0,1] and a∈[0,1]a\in[0,1].

###### Lemma 1.

Suppose that h∈ℋh\in\mathcal{H} and 𝒳=L+\mathcal{X}=L^{+}. For any α∈[0,1]\alpha\in[0,1] and
X∈𝒳X\in\mathcal{X}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRα​□ρh​(X)=ρhα​(X).\displaystyle\mathrm{VaR}\_{\alpha}\mathop{\square}\displaylimits\rho\_{h}(X)=\rho\_{h^{\alpha}}(X). |  | (15) |

###### Proof.

We first show that VaRα​□​ρh​(X)≥ρhα​(X)\mathrm{VaR}\_{\alpha}\square\rho\_{h}(X)\geq\rho\_{h^{\alpha}}(X). For any allocation (Y,X−Y)(Y,X-Y) of XX with 0≤Y≤X0\leq Y\leq X, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRα​(Y)+ρh​(X−Y)\displaystyle\mathrm{VaR}\_{\alpha}(Y)+\rho\_{h}(X-Y) | =VaRα​(Y)+∫01VaRβ​(X−Y)​dh​(β)\displaystyle=\mathrm{VaR}\_{\alpha}(Y)+\int\_{0}^{1}\mathrm{VaR}\_{\beta}(X-Y)\mathrm{d}h(\beta) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01−αVaRα​(Y)+VaRβ​(X−Y)​d​h​(β)\displaystyle=\int\_{0}^{1-\alpha}\mathrm{VaR}\_{\alpha}(Y)+\mathrm{VaR}\_{\beta}(X-Y)\mathrm{d}h(\beta) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫1−α1VaRα​(Y)+VaRβ​(X−Y)​d​h​(β)\displaystyle\quad+\int\_{1-\alpha}^{1}\mathrm{VaR}\_{\alpha}(Y)+\mathrm{VaR}\_{\beta}(X-Y)\mathrm{d}h(\beta) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥∫01−αVaRα+β​(X)​dh​(β)\displaystyle\geq\int\_{0}^{1-\alpha}\mathrm{VaR}\_{\alpha+\beta}(X)\mathrm{d}h(\beta) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫01VaRβ′​(X)​dh​((β′−α)+)=ρhα​(X).\displaystyle=\int\_{0}^{1}\mathrm{VaR}\_{\beta^{\prime}}(X)\mathrm{d}h((\beta^{\prime}-\alpha)\_{+})=\rho\_{h^{\alpha}}(X). |  |

The inequality is due to 0≤Y≤X0\leq Y\leq X and
VaRα+β​(X1+X2)≤VaRα​(X1)+VaRβ​(X2)\mathrm{VaR}\_{\alpha+\beta}(X\_{1}+X\_{2})\leq\mathrm{VaR}\_{\alpha}(X\_{1})+\mathrm{VaR}\_{\beta}(X\_{2}) for X1,X2∈𝒳X\_{1},X\_{2}\in\mathcal{X}; see Corollary 1 of Embrechts et al., ([2018](https://arxiv.org/html/2510.18236v1#bib.bib10)).

Next we show that VaRα​□​ρh​(X)≤ρhα​(X)\mathrm{VaR}\_{\alpha}\square\rho\_{h}(X)\leq\rho\_{h\_{\alpha}}(X). Note that VaRα​(X​𝟙{UX>1−α})=0\mathrm{VaR}\_{\alpha}\left(X\mathbb{1}\_{\left\{U\_{X}>1-\alpha\right\}}\right)=0. By straightforward calculation, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRα​□​ρh​(X)\displaystyle\mathrm{VaR}\_{\alpha}\square\rho\_{h}(X) | ≤VaRα​(X​𝟙{UX>1−α})+ρh​(X​𝟙{UX≤1−α})\displaystyle\leq\mathrm{VaR}\_{\alpha}\left(X\mathbb{1}\_{\left\{U\_{X}>1-\alpha\right\}}\right)+\rho\_{h}\left(X\mathbb{1}\_{\left\{U\_{X}\leq 1-\alpha\right\}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0∞h​(ℙ​(X​𝟙{UX≤1−α}>t))​dt\displaystyle=\int\_{0}^{\infty}h\left(\mathbb{P}\left(X\mathbb{1}\_{\left\{U\_{X}\leq 1-\alpha\right\}}>t\right)\right)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0∞h​(ℙ​({X>t}∩{UX≤1−α}))​dt\displaystyle=\int\_{0}^{\infty}h\left(\mathbb{P}\left(\left\{X>t\right\}\cap\left\{U\_{X}\leq 1-\alpha\right\}\right)\right)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0∞h​((ℙ​(X>t)−α)+)​dt=ρhα​(X).\displaystyle=\int\_{0}^{\infty}h\left((\mathbb{P}(X>t)-\alpha)\_{+}\right)\mathrm{d}t=\rho\_{h^{\alpha}}(X). |  |

Therefore, the desired result is obtained.
∎

###### Remark 3.

For any α∈[0,1]\alpha\in[0,1], we denote by gαg^{\alpha} the distortion function of VaRα\mathrm{VaR}\_{\alpha}, i.e., gα​(x)=𝟙{x>α}g^{\alpha}(x)=\mathbb{1}\_{\left\{x>\alpha\right\}}. Clearly, gα​□h​(x)=hα​(x)g^{\alpha}\mathop{\square}\displaylimits h(x)=h^{\alpha}(x) for x∈[0,1]x\in[0,1]. Therefore, ([15](https://arxiv.org/html/2510.18236v1#S5.E15 "In Lemma 1. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) in fact states that
ρgα​□ρh​(X)=ρgα​□h​(X)\rho\_{g^{\alpha}}\mathop{\square}\displaylimits\rho\_{h}(X)=\rho\_{g^{\alpha}\mathop{\square}\displaylimits h}(X) for X∈𝒳X\in\mathcal{X}.

We now investigate the structure of optimal allocations in a two-agent risk sharing setting involving one risk-averse and one risk-seeking participant, where both agents are characterized by piecewise linear distortion functions, as generalized from Example [6](https://arxiv.org/html/2510.18236v1#Thmexample6 "Example 6. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").
In the next proposition, the distortion functions g1g\_{1} and g2g\_{2} correspond to a left-tail Expected Shortfall (see Embrechts et al., ([2015](https://arxiv.org/html/2510.18236v1#bib.bib11))) and an Expected Shortfall, respectively.

###### Proposition 2.

Suppose that 𝒳=L+\mathcal{X}=L^{+}. Let h1​(x)=max⁡{0,(x−a)/(1−a)}h\_{1}(x)=\max\left\{0,(x-a)/(1-a)\right\} and
h2​(x)=min⁡{x/b,1}h\_{2}(x)=\min\left\{x/b,1\right\}
for x∈[0,1]x\in[0,1], where a,b∈(0,1)a,b\in(0,1) and a+b≥1a+b\geq 1.
Then

|  |  |  |
| --- | --- | --- |
|  | ρh1​□ρh2​(X)=ρh1​□h2​(X)=ρh​(X)​ for all X∈𝒳,\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)=\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X)=\rho\_{h}(X)\mbox{~~~for all $X\in\mathcal{X}$}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | h​(x)=max⁡{0,(x−a)/b},x∈[0,1].h(x)=\max\left\{0,(x-a)/b\right\},~~~x\in[0,1]. |  |

Moreover, an optimal allocation (X1,X2)(X\_{1},X\_{2})
of XX is given by

|  |  |  |
| --- | --- | --- |
|  | X1=X​𝟙{UX≥1−a},and​X2=X​𝟙{UX<1−a}.\displaystyle X\_{1}=X\mathbb{1}\_{\left\{U\_{X}\geq 1-a\right\}},~\text{and}~X\_{2}=X\mathbb{1}\_{\left\{U\_{X}<1-a\right\}}. |  |

###### Proof.

Clearly, α​(h1)=a\alpha(h\_{1})=a and h^1​(x)=min⁡{x/(1−a),1}\hat{h}\_{1}(x)=\min\left\{x/(1-a),1\right\}.
We can calculate

|  |  |  |  |
| --- | --- | --- | --- |
|  | h1​□h2​(x)=max⁡{0,(x−a)/b}=h2a​(x)=h​(x),x∈[0,1].\displaystyle h\_{1}\mathop{\square}\displaylimits h\_{2}(x)=\max\left\{0,(x-a)/b\right\}=h\_{2}^{a}(x)=h(x),~~~x\in[0,1]. |  | (16) |

By Lemma [1](https://arxiv.org/html/2510.18236v1#Thmlemma1 "Lemma 1. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"), it follows that

|  |  |  |
| --- | --- | --- |
|  | VaRa​□ρh^1​(X)=ρh1​(X).\displaystyle\operatorname{VaR}\_{a}\mathop{\square}\displaylimits\rho\_{\hat{h}\_{1}}(X)=\rho\_{h\_{1}}(X). |  |

Note that by using Lemma 2 of Liu et al., ([2020](https://arxiv.org/html/2510.18236v1#bib.bib24)), we can see that inf-convolutions are associative. Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​□ρh2​(X)\displaystyle\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X) | =(VaRa​□ρh^1)​□ρh2​(X)\displaystyle=(\operatorname{VaR}\_{a}\mathop{\square}\displaylimits\rho\_{\hat{h}\_{1}})\mathop{\square}\displaylimits\rho\_{h\_{2}}(X) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =VaRa​□(ρh^1​□ρh2)​(X)=VaRa​□ρh2​(X)=ρh1​□h2​(X),\displaystyle=\operatorname{VaR}\_{a}\mathop{\square}\displaylimits(\rho\_{\hat{h}\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}})(X)=\operatorname{VaR}\_{a}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)=\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X), |  |

where the last equality follows from Lemma [1](https://arxiv.org/html/2510.18236v1#Thmlemma1 "Lemma 1. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") and ([16](https://arxiv.org/html/2510.18236v1#S5.E16 "In 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")).

Next, we find the optimal allocation.
Let f​(x)=min⁡{x,a}f(x)=\min\left\{x,a\right\}, so that x−f​(x)=max⁡{0,x−a}x-f(x)=\max\left\{0,x-a\right\}. Both f​(x)f(x) and x−f​(x)x-f(x) are non-decreasing.
It can be verified that
h1​(f​(x))+h2​(x−f​(x))=h1​□h2​(x)h\_{1}(f(x))+h\_{2}(x-f(x))=h\_{1}\mathop{\square}\displaylimits h\_{2}(x) for x∈[0,1]x\in[0,1].
Then it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​(X1)\displaystyle\rho\_{h\_{1}}(X\_{1}) | =∫0∞h1​(ℙ​(X​𝟙{UX≥1−a}>t))​dt\displaystyle=\int\_{0}^{\infty}h\_{1}(\mathbb{P}(X\mathbb{1}\_{\left\{U\_{X}\geq 1-a\right\}}>t))\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0∞h1​(ℙ​({X>t}∩{UX≥1−a}))​dt\displaystyle=\int\_{0}^{\infty}h\_{1}(\mathbb{P}(\left\{X>t\right\}\cap\left\{U\_{X}\geq 1-a\right\}))\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0∞h1​(ℙ​(UX≥max⁡{FX​(t),1−a}))​dt\displaystyle=\int\_{0}^{\infty}h\_{1}(\mathbb{P}(U\_{X}\geq\max\left\{F\_{X}(t),1-a\right\}))\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0∞h1​(min⁡{a,SX​(t)})​dt=∫0∞h1​(f​(SX​(t)))​dt.\displaystyle=\int\_{0}^{\infty}h\_{1}(\min\left\{a,S\_{X}(t)\right\})\mathrm{d}t=\int\_{0}^{\infty}h\_{1}(f(S\_{X}(t)))\mathrm{d}t. |  |

Similarly, we have ρh2​(X2)=∫0∞h1​(SX​(t)−f​(SX​(t)))​dt\rho\_{h\_{2}}(X\_{2})=\int\_{0}^{\infty}h\_{1}(S\_{X}(t)-f(S\_{X}(t)))\mathrm{d}t.
This implies that ρh1​(X1)+ρh2​(X2)=ρh1​□h2​(X)\rho\_{h\_{1}}(X\_{1})+\rho\_{h\_{2}}(X\_{2})=\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X).
∎

Although Proposition [2](https://arxiv.org/html/2510.18236v1#Thmproposition2 "Proposition 2. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") covers only a subset of the mixed (one risk-averse and one risk-seeking) cases, it extends part (ii) of Theorem [3](https://arxiv.org/html/2510.18236v1#Thmtheorem3 "Theorem 3. ‣ 4.2 One risk-averse agent and one risk-seeking agent ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") by removing the constraint of h1​□​h2​(1)=1h\_{1}\square h\_{2}(1)=1.
A further implication of Proposition [2](https://arxiv.org/html/2510.18236v1#Thmproposition2 "Proposition 2. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") is that comonotonic allocations cannot be optimal unless the parameters satisfy a+b=1a+b=1.
In particular, when the degree of risk seeking exceeds that of risk aversion, counter-monotonic allocations would strictly outperform comonotonic ones, as stated in Proposition [3](https://arxiv.org/html/2510.18236v1#Thmproposition3 "Proposition 3. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").

###### Proposition 3.

Suppose that 𝒳=L+\mathcal{X}=L^{+}, h1h\_{1} is concave, and h2h\_{2} is convex. Then

* (i)

  h1​□h2=h2h\_{1}\mathop{\square}\displaylimits h\_{2}=h\_{2} if and only if h1​□h2​(1)=1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)=1.
* (ii)

  If h1​□h2​(1)<1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)<1, then a comonotonic allocation of X∈𝒳X\in\mathcal{X} is never optimal.

###### Proof.

(i) “Only if” part is trivial.
We only show “if” part.
The condition of h1​□h2​(1)=1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)=1 is equivalent with h1≥h~2h\_{1}\geq\widetilde{h}\_{2}. For any x∈[0,1]x\in[0,1] and y∈[0,x]y\in[0,x], we have

|  |  |  |
| --- | --- | --- |
|  | h1​(y)≥1−h2​(1−y)≥h2​(x)−h2​(x−y).\displaystyle h\_{1}(y)\geq 1-h\_{2}(1-y)\geq h\_{2}(x)-h\_{2}(x-y). |  |

The second inequality holds due to convexity of h2h\_{2}. Thus, this implies h1​□h2=h2h\_{1}\mathop{\square}\displaylimits h\_{2}=h\_{2}.

(ii) If there exists a comonotonic optimal allocation, then ρh1​□ρh2​(X)=ρh2​(X)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)=\rho\_{h\_{2}}(X). This implies that h1​□h2=h2h\_{1}\mathop{\square}\displaylimits h\_{2}=h\_{2}, and hence h1​□h2​(1)=1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)=1 by result of (i), contradicting the assumption that h1​□h2​(1)<1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)<1.
∎

Proposition [3](https://arxiv.org/html/2510.18236v1#Thmproposition3 "Proposition 3. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") shows that in the presence of a sufficiently strong risk-seeking (i.e., when h1​□h2​(1)<1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)<1), comonotonic allocations fail to be optimal.
Example [7](https://arxiv.org/html/2510.18236v1#Thmexample7 "Example 7. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") below illustrates highlights how this effect arises under power-function distortion functions.

###### Example 7.

Set h1​(x)=1−(1−x)2h\_{1}(x)=1-(1-x)^{2} and h2​(x)=x3h\_{2}(x)=x^{3} for x∈[0,1]x\in[0,1] and let X∼Bernoulli​(p)X\sim\text{Bernoulli}(p) for p∈[0,1]p\in[0,1]. For any comonotonic allocation (X1,X2)(X\_{1},X\_{2}) of XX, it holds that

|  |  |  |
| --- | --- | --- |
|  | ρh1​(X1)+ρh2​(X2)≥ρh1∧h2​(X)=h2​(p).\displaystyle\rho\_{h\_{1}}(X\_{1})+\rho\_{h\_{2}}(X\_{2})\geq\rho\_{h\_{1}\wedge h\_{2}}(X)=h\_{2}(p). |  |

By straightforward calculation, we have

|  |  |  |
| --- | --- | --- |
|  | h1​□h2​(x)=h2​(x)​𝟙{x≤23}+(h1​(f​(x))+h2​(x−f​(x)))​𝟙{x>23},\displaystyle h\_{1}\mathop{\square}\displaylimits h\_{2}(x)=h\_{2}(x)\mathbb{1}\_{\left\{x\leq\sqrt{\frac{2}{3}}\right\}}+(h\_{1}(f(x))+h\_{2}(x-f(x)))\mathbb{1}\_{\left\{x>\sqrt{\frac{2}{3}}\right\}}, |  |

where f​(x)=(3​x−1−7−6​x)/3f(x)=(3x-1-\sqrt{7-6x})/3. It can be seen from Figure [2](https://arxiv.org/html/2510.18236v1#S5.F2 "Figure 2 ‣ Example 7. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") that h1​□h2​(x)<h2​(x)h\_{1}\mathop{\square}\displaylimits h\_{2}(x)<h\_{2}(x) for x>2/3x>\sqrt{2/3}.
Take X1′=𝟙AX\_{1}^{\prime}=\mathbb{1}\_{A} and X2′=𝟙BX\_{2}^{\prime}=\mathbb{1}\_{B}, where AA and BB are disjoint,
ℙ​(A∪B)=p\mathbb{P}(A\cup B)=p and satisfies h1​(ℙ​(A))+h2​(ℙ​(B))=h1​□h2​(p)h\_{1}(\mathbb{P}(A))+h\_{2}(\mathbb{P}(B))=h\_{1}\mathop{\square}\displaylimits h\_{2}(p).
Clearly, (X1′,X2′)(X\_{1}^{\prime},X\_{2}^{\prime}) is a counter-monotonic allocation of XX. For p>2/3p>\sqrt{2/3}, we can derive that

|  |  |  |
| --- | --- | --- |
|  | ρh1​(X1′)+ρh2​(X2′)=h1​□h2​(p)<h2​(p).\displaystyle\rho\_{h\_{1}}(X\_{1}^{\prime})+\rho\_{h\_{2}}(X\_{2}^{\prime})=h\_{1}\mathop{\square}\displaylimits h\_{2}(p)<h\_{2}(p). |  |

Hence, a comonotonic allocation (X1,X2)(X\_{1},X\_{2}) is never optimal.

![Refer to caption](x3.png)


Figure 2: An illustration of Example [7](https://arxiv.org/html/2510.18236v1#Thmexample7 "Example 7. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").

### 5.2 Two agents sharing a Bernoulli-type risk

In this subsection, we consider a simple setting of two agents sharing a Bernoulli random risk with unrestricted risk preferences. In this binary setting, the inf-convolution and optimal allocations admit closed-form solutions. Furthermore, we explore how these insights extend to richer risk distributions.

###### Theorem 5.

Suppose that h1,h2∈ℋh\_{1},h\_{2}\in\mathcal{H} and
𝒳=L+\mathcal{X}=L^{+}. For any A∈ℱA\in\mathcal{F} and a∈ℝ+a\in\mathbb{R}\_{+}, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​□ρh2​(a​𝟙A)=ρh1​□h2​(a​𝟙A)=a​h1​□h2​(ℙ​(A)).\displaystyle\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(a\mathbb{1}\_{A})=\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(a\mathbb{1}\_{A})=ah\_{1}\mathop{\square}\displaylimits h\_{2}(\mathbb{P}(A)). |  | (17) |

Moreover, a Pareto-optimal allocation is given by X1=a​𝟙BX\_{1}=a\mathbb{1}\_{B} and X2=a​𝟙A∖BX\_{2}=a\mathbb{1}\_{A\setminus B} satisfying h1​(ℙ​(B))+h2​(ℙ​(A∖B))=h1​□h2​(ℙ​(A))h\_{1}(\mathbb{P}(B))+h\_{2}(\mathbb{P}(A\setminus B))=h\_{1}\mathop{\square}\displaylimits h\_{2}(\mathbb{P}(A)).

###### Proof.

By the positive homogeneity of ρh1​□h2\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}, it is trivial to verify the second equality in ([17](https://arxiv.org/html/2510.18236v1#S5.E17 "In Theorem 5. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")).
To show the first equality, we first state that ρh1​□ρh2​(a​𝟙A)≥ρh1​□h2​(a​𝟙A)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(a\mathbb{1}\_{A})\geq\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(a\mathbb{1}\_{A}).
With 0≤Y≤a​𝟙A0\leq Y\leq a\mathbb{1}\_{A}, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​(Y)+ρh2​(a​𝟙A−Y)\displaystyle\rho\_{h\_{1}}(Y)+\rho\_{h\_{2}}(a\mathbb{1}\_{A}-Y) | =∫0∞h1​(ℙ​(Y>t))​dt+∫0∞h2​(ℙ​(a​𝟙A−Y>t))​dt\displaystyle=\int\_{0}^{\infty}h\_{1}(\mathbb{P}(Y>t))\mathrm{d}t+\int\_{0}^{\infty}h\_{2}(\mathbb{P}(a\mathbb{1}\_{A}-Y>t))\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0ah1​(ℙ​(Y≥t))​dt+∫0ah2​(ℙ​(a−Y>t|A)​ℙ​(A))​dt\displaystyle=\int\_{0}^{a}h\_{1}(\mathbb{P}(Y\geq t))\mathrm{d}t+\int\_{0}^{a}h\_{2}(\mathbb{P}(a-Y>t|A)\mathbb{P}(A))\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0ah1​(ℙ​(Y≥t))​dt+∫0ah2​(ℙ​(Y​<t|​A)​ℙ​(A))​dt\displaystyle=\int\_{0}^{a}h\_{1}(\mathbb{P}(Y\geq t))\mathrm{d}t+\int\_{0}^{a}h\_{2}(\mathbb{P}(Y<t|A)\mathbb{P}(A))\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0ah1​(ℙ​(Y≥t))​dt+∫0ah2​(ℙ​({Y<t}∩A))​dt\displaystyle=\int\_{0}^{a}h\_{1}(\mathbb{P}(Y\geq t))\mathrm{d}t+\int\_{0}^{a}h\_{2}(\mathbb{P}(\{Y<t\}\cap A))\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥∫0ah1​□h2​(ℙ​(A))​d​t=a​h1​□h2​(ℙ​(A)),\displaystyle\geq\int\_{0}^{a}h\_{1}\mathop{\square}\displaylimits h\_{2}(\mathbb{P}(A))\mathrm{d}t=ah\_{1}\mathop{\square}\displaylimits h\_{2}(\mathbb{P}(A)), |  |

where we used ℙ​(Y≥t)+ℙ​({Y<t}∩A)≥ℙ​(A).\mathbb{P}(Y\geq t)+\mathbb{P}(\{Y<t\}\cap A)\geq\mathbb{P}(A).
Thus, we have ρh1​□ρh2​(𝟙A)≥a​h1​□h2​(ℙ​(A))\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(\mathbb{1}\_{A})\geq ah\_{1}\mathop{\square}\displaylimits h\_{2}(\mathbb{P}(A)).

Next, we show the converse direction. Take an allocation (X1,X2)(X\_{1},X\_{2}) of XX as X1=a​𝟙BX\_{1}=a\mathbb{1}\_{B} and X2=a​𝟙CX\_{2}=a\mathbb{1}\_{C}, where B∪C=AB\cup C=A, B∩C=∅B\cap C=\varnothing and
h1​(ℙ​(B))+h2​(ℙ​(C))=a​h1​□h2​(ℙ​(A))h\_{1}(\mathbb{P}(B))+h\_{2}(\mathbb{P}(C))=ah\_{1}\mathop{\square}\displaylimits h\_{2}(\mathbb{P}(A)),
we have
ρh1​(X1)+ρh2​(X2)=a​h1​□h2​(ℙ​(A))\rho\_{h\_{1}}(X\_{1})+\rho\_{h\_{2}}(X\_{2})=ah\_{1}\mathop{\square}\displaylimits h\_{2}(\mathbb{P}(A)). Consequently, ρh1​□ρh2​(a​𝟙A)≤ρh1​□h2​(a​𝟙A)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(a\mathbb{1}\_{A})\leq\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(a\mathbb{1}\_{A}) holds for any a∈ℝ+a\in\mathbb{R}\_{+}.
∎

Notably, Theorem [5](https://arxiv.org/html/2510.18236v1#Thmtheorem5 "Theorem 5. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") does not rely on any concavity or convexity assumptions about the distortion functions. Moreover, it characterizes how the total probability mass ℙ​(A)\mathbb{P}(A) is divided between the two agents so as to minimize the total risk value, with the splitting probabilities determined by
h1​□h2h\_{1}\mathop{\square}\displaylimits h\_{2}.
To gain intuition, we provide an example to see how the optimal split changes when one agent is risk averse and the other is risk seeking, particularly in cases where the dominance condition h1≥h~2h\_{1}\geq\widetilde{h}\_{2} fails.
Example [8](https://arxiv.org/html/2510.18236v1#Thmexample8 "Example 8. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") illustrates this behavior explicitly, showing how the share of risk held by each agent varies with the total probability level ℙ​(A)\mathbb{P}(A).

###### Example 8.

Suppose that h1​(x)=1−(1−x)αh\_{1}(x)=1-(1-x)^{\alpha} and h2​(x)=xβh\_{2}(x)=x^{\beta} with 1<α<β1<\alpha<\beta. Clearly, h1h\_{1} is concave, h2h\_{2} is convex, and h1≤h~2h\_{1}\leq\widetilde{h}\_{2}. Let p0=(α/β)1β−1p\_{0}=(\alpha/\beta)^{\frac{1}{\beta-1}} and
(𝟙B,𝟙A∖B)(\mathbb{1}\_{B},\mathbb{1}\_{A\setminus B}) be an optimal allocation of 𝟙A\mathbb{1}\_{A}.
We can show that

1. (i)

   If ℙ​(A)≤p0\mathbb{P}(A)\leq p\_{0}, then ℙ​(B)=0\mathbb{P}(B)=0 and ℙ​(A\B)=ℙ​(A)\mathbb{P}(A\backslash B)=\mathbb{P}(A), so the risk-seeking agent bear the entire risk.
2. (ii)

   If ℙ​(A)>p0\mathbb{P}(A)>p\_{0}, then as ℙ​(A)\mathbb{P}(A) increases,
   ℙ​(B)\mathbb{P}(B) increases strictly, while ℙ​(A\B)\mathbb{P}(A\backslash B) falls strictly. In this case, the risk‐averse agent begins to take on an increasing share of the risk, while the risk‐seeker’s share correspondingly shrinks.

The proof is non-trivial and the details are provided in Proposition [8](https://arxiv.org/html/2510.18236v1#Thmproposition8 "Proposition 8. ‣ Appendix A Details in Example 8 ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") of Appendix [A](https://arxiv.org/html/2510.18236v1#A1 "Appendix A Details in Example 8 ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").
For the special case α=2\alpha=2 and β=3\beta=3, Figure [3](https://arxiv.org/html/2510.18236v1#S5.F3 "Figure 3 ‣ Example 8. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") illustrates the trend of ℙ​(B)\mathbb{P}(B) and ℙ​(A∖B)\mathbb{P}(A\setminus B) as ℙ​(A)\mathbb{P}(A) varies.

![Refer to caption](x4.png)


Figure 3: An illustration of Example [8](https://arxiv.org/html/2510.18236v1#Thmexample8 "Example 8. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").

It is clear that examining an economy without aggregate uncertainty, where the total endowment is constant, is a special case of Theorem [5](https://arxiv.org/html/2510.18236v1#Thmtheorem5 "Theorem 5. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"); as shown in the following corollary.

###### Corollary 1.

Suppose that 𝒳=L+\mathcal{X}=L^{+}. For any a∈ℝ+a\in\mathbb{R}\_{+}, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​□ρh2​(a)=a​h1​□h2​(1).\displaystyle\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(a)=ah\_{1}\mathop{\square}\displaylimits h\_{2}(1). |  | (18) |

Moreover, a Pareto-optimal allocation is given by X1=𝟙BX\_{1}=\mathbb{1}\_{B} and X2=𝟙A∖BX\_{2}=\mathbb{1}\_{A\setminus B} with h1​(ℙ​(B))+h2​(ℙ​(A∖B))=h1​□h2​(1)h\_{1}(\mathbb{P}(B))+h\_{2}(\mathbb{P}(A\setminus B))=h\_{1}\mathop{\square}\displaylimits h\_{2}(1).

The result directly follows from Theorem [5](https://arxiv.org/html/2510.18236v1#Thmtheorem5 "Theorem 5. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") by taking A=ΩA=\Omega. If additionally h1≥h~2h\_{1}\geq\widetilde{h}\_{2}, implying that h1​□h2​(1)=1h\_{1}\mathop{\square}\displaylimits h\_{2}(1)=1, then ρh1​□ρh2​(a)=a\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(a)=a for any positive constant aa. In this case, any constant split (b,a−b)(b,a-b) with 0≤b≤a0\leq b\leq a is Pareto optimal.

In fact, the equality ([18](https://arxiv.org/html/2510.18236v1#S5.E18 "In Corollary 1. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) relies on the richness of the probability space to ensure that ℙ​(B)\mathbb{P}(B) can achieve the infimum.
On non-atomless space (e.g., finite probability space), the required probability level may be unattainable and the equality can fail; see more details in Example [9](https://arxiv.org/html/2510.18236v1#Thmexample9 "Example 9 (Counter-example in a finite probability space). ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").

###### Example 9 (Counter-example in a finite probability space).

Define a probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}), where Ω={ω1,ω2}\Omega=\left\{\omega\_{1},\omega\_{2}\right\}, and ℙ\mathbb{P} is such that ℙ​({ω1})=1/6\mathbb{P}(\left\{\omega\_{1}\right\})=1/6, ℙ​({ω2})=5/6\mathbb{P}(\left\{\omega\_{2}\right\})=5/6.
Suppose that two agents have distortion functions given by

|  |  |  |
| --- | --- | --- |
|  | h1​(x)={2​xx∈[0,0.5]1x∈[0.5,1];h2​(x)={0x∈[0,2/3]3​x−2x∈[2/3,1].\displaystyle{h}\_{1}(x)=\begin{cases}2x&x\in[0,0.5]\\ 1&x\in[0.5,1];\end{cases}~~\ h\_{2}(x)=\begin{cases}0&x\in[0,2/3]\\ 3x-2&x\in[2/3,1].\end{cases} |  |

We can show that

|  |  |  |
| --- | --- | --- |
|  | h1​□h2​(x)={0x∈[0,2/3]2​x−4/3x∈[2/3,1].\displaystyle h\_{1}\mathop{\square}\displaylimits h\_{2}(x)=\begin{cases}0&x\in[0,2/3]\\ 2x-4/3&x\in[2/3,1].\end{cases} |  |

Assume that two agents are sharing a constant 11. The only possible allocation (X1,X2)(X\_{1},X\_{2}) of 11 is in the form of (a​𝟙{ω1}+b​𝟙{ω2},(1−a)​𝟙{ω1}+(1−b)​𝟙{ω2})(a\mathbb{1}\_{\left\{\omega\_{1}\right\}}+b\mathbb{1}\_{\left\{\omega\_{2}\right\}},(1-a)\mathbb{1}\_{\left\{\omega\_{1}\right\}}+(1-b)\mathbb{1}\_{\left\{\omega\_{2}\right\}}), where 0≤a,b≤10\leq a,b\leq 1. If a≤ba\leq b, then
ρh1​(X1)+ρh2​(X2)=a+(b−a)​h2​(5/6)+(1−b)+(b−a)​h1​(1/6)=1\rho\_{h\_{1}}(X\_{1})+\rho\_{h\_{2}}(X\_{2})=a+(b-a)h\_{2}(5/6)+(1-b)+(b-a)h\_{1}(1/6)=1.
If a≥ba\geq b, then
ρh1​(X1)+ρh2​(X2)=b+(a−b)​h1​(1/6)+(1−a)+(a−b)​h2​(5/6)=1−1/6​(a−b)≥5/6\rho\_{h\_{1}}(X\_{1})+\rho\_{h\_{2}}(X\_{2})=b+(a-b)h\_{1}(1/6)+(1-a)+(a-b)h\_{2}(5/6)=1-1/6(a-b)\geq 5/6. Also, it is straightforward to verify that ρh1​□h2​(1)=2/3\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(1)=2/3.
This shows that ρh1​□ρh2​(1)>ρh1​□h2​(1)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(1)>\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(1).

Having established the equality ([17](https://arxiv.org/html/2510.18236v1#S5.E17 "In Theorem 5. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) for indicator risks, we now turn to more complex distributions. When the total risk involves multiple components rather than a single Bernoulli variable, the exact equality no longer necessarily holds.
Even so, this broader setting yields useful insights, particularly regarding whether and when the inf-convolution can still attain the benchmark value.
Proposition [4](https://arxiv.org/html/2510.18236v1#Thmproposition4 "Proposition 4. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") demonstrates that such attainability persists in a structured class of random risks. Specifically, when the total risk is composed of disjoint indicator components, there always exists a feasible allocation achieving the value of ρh1​□h2\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}.

###### Proposition 4.

Suppose that h1,h2∈ℋh\_{1},h\_{2}\in\mathcal{H} and 𝒳=L+\mathcal{X}=L^{+}.
Let X=a​𝟙A+b​𝟙BX=a\mathbb{1}\_{A}+b\mathbb{1}\_{B}, where
A,B∈ℱA,B\in\mathcal{F} are disjoint and a,b∈ℝ+a,b\in\mathbb{R}\_{+} are constants. Then it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​□ρh2​(X)≤ρh1​□h2​(X).\displaystyle\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)\leq\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X). |  | (19) |

###### Proof.

Without loss of generality, we assume that a≤ba\leq b. Then XX can be reformulated as X=a​𝟙A′+(b−a)​𝟙B′X=a\mathbb{1}\_{A^{\prime}}+(b-a)\mathbb{1}\_{B^{\prime}}, where A′=A∪BA^{\prime}=A\cup B and B′=BB^{\prime}=B. clearly, B′⊆A′B^{\prime}\subseteq A^{\prime}, which implies that (a​𝟙A′,(b−a)​𝟙B′)(a\mathbb{1}\_{A^{\prime}},(b-a)\mathbb{1}\_{B^{\prime}}) is comonotonic.
Let p1=ℙ​(A′)p\_{1}=\mathbb{P}(A^{\prime}) and p2=ℙ​(B′)p\_{2}=\mathbb{P}(B^{\prime}). By comonotonic additivity of ρh1​□h2\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}, we have

|  |  |  |
| --- | --- | --- |
|  | ρh1​□h2​(X)=a​h1​□h2​(p1)+(b−a)​h1​□h2​(p2).\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X)=a{h\_{1}\mathop{\square}\displaylimits h\_{2}}(p\_{1})+(b-a){h\_{1}\mathop{\square}\displaylimits h\_{2}}(p\_{2}). |  |

Define the set

|  |  |  |
| --- | --- | --- |
|  | Si={t∈[0,pi]:h1​(t)+h2​(pi−t)=h1​□h2​(pi)}.S\_{i}=\left\{t\in[0,p\_{i}]:h\_{1}(t)+h\_{2}(p\_{i}-t)=h\_{1}\mathop{\square}\displaylimits h\_{2}(p\_{i})\right\}. |  |

Let ui∈Siu\_{i}\in S\_{i} for each i∈[2]i\in[2].
Our aim is to construct an allocation (Y,Z)(Y,Z) of XX such that ρh1​(Y)+ρh2​(Z)=a​h1​□h2​(p1)+(b−a)​h1​□h2​(p2)\rho\_{h\_{1}}(Y)+\rho\_{h\_{2}}(Z)=ah\_{1}\mathop{\square}\displaylimits h\_{2}(p\_{1})+(b-a)h\_{1}\mathop{\square}\displaylimits h\_{2}(p\_{2}).
We construct an allocation of XX as follows:

|  |  |  |
| --- | --- | --- |
|  | Y=a​𝟙C+b​𝟙D​ and ​Z=a​𝟙A′\C+b​𝟙B′\D​ with ​ℙ​(C)=u1​ and ​ℙ​(D)=u2.\displaystyle Y=a\mathbb{1}\_{C}+b\mathbb{1}\_{D}\ \text{ and }\ Z=a\mathbb{1}\_{A^{\prime}\backslash C}+b\mathbb{1}\_{B^{\prime}\backslash D}\ \text{ with }\ \mathbb{P}(C)=u\_{1}\ \text{ and }\ \mathbb{P}(D)=u\_{2}. |  |

In fact, the construction of CC and
DD vary with the magnitude relationship between u1u\_{1} and u2u\_{2}, as well as p1−u1p\_{1}-u\_{1} and p2−u2p\_{2}-u\_{2}.
Next, we will show the details about how to construct CC and
DD in different cases. We consider the following three cases.

Case 1: u1≤u2u\_{1}\leq u\_{2} and p1−u1≤p2−u2p\_{1}-u\_{1}\leq p\_{2}-u\_{2}. This case cannot happen unless ℙ​(A)=0\mathbb{P}(A)=0, then it reduces to Theorem [5](https://arxiv.org/html/2510.18236v1#Thmtheorem5 "Theorem 5. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"). Therefore, ([19](https://arxiv.org/html/2510.18236v1#S5.E19 "In Proposition 4. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) holds trivially.

Case 2: u1≤u2u\_{1}\leq u\_{2} and p1−u1≥p2−u2p\_{1}-u\_{1}\geq p\_{2}-u\_{2}. It implies that u1≤u2u\_{1}\leq u\_{2} since p1≥p2p\_{1}\geq p\_{2}.
Take C⊆BC\subseteq B with ℙ​(C)=u1\mathbb{P}(C)=u\_{1} and D=C∪ED=C\cup E with E⊆B′\CE\subseteq B^{\prime}\backslash C and ℙ​(E)=u2−u1\mathbb{P}(E)=u\_{2}-u\_{1}. Hence, ℙ​(D)=u2\mathbb{P}(D)=u\_{2}. Also, we have B′\D⊆A′\CB^{\prime}\backslash D\subseteq A^{\prime}\backslash C.

Case 3: u1≥u2u\_{1}\geq u\_{2} and p1−u1≥p2−u2p\_{1}-u\_{1}\geq p\_{2}-u\_{2}. Thus, u1≥u2≥p2−p1+u1u\_{1}\geq u\_{2}\geq p\_{2}-p\_{1}+u\_{1}.
Let D⊆B′D\subseteq B^{\prime} with ℙ​(D)=u2\mathbb{P}(D)=u\_{2}. The take C=D∪EC=D\cup E and E⊆A′\B′E\subseteq A^{\prime}\backslash B^{\prime} with ℙ​(E)=u1−u2\mathbb{P}(E)=u\_{1}-u\_{2}. Hence, ℙ​(C)=u1\mathbb{P}(C)=u\_{1}.
In this case, we have B′\D⊆A′\CB^{\prime}\backslash D\subseteq A^{\prime}\backslash C.

Case 4: u1≥u2u\_{1}\geq u\_{2} and p1−u1≤p2−u2p\_{1}-u\_{1}\leq p\_{2}-u\_{2}. It implies that u1≥p1−p2+u2u\_{1}\geq p\_{1}-p\_{2}+u\_{2}.
Let D⊆B′D\subseteq B^{\prime} with ℙ​(D)=u2\mathbb{P}(D)=u\_{2}.
Take C=D∪(A′\B′)∪EC=D\cup(A^{\prime}\backslash B^{\prime})\cup E and E⊆B′\DE\subseteq B^{\prime}\backslash D with ℙ​(E)=u1−u2−(p1−p2)\mathbb{P}(E)=u\_{1}-u\_{2}-(p\_{1}-p\_{2}). Thus, we have ℙ​(C)=u1\mathbb{P}(C)=u\_{1} and A′\C⊆B′\DA^{\prime}\backslash C\subseteq B^{\prime}\backslash D.

By above constructions, both (a​𝟙C,(b−a)​𝟙D)(a\mathbb{1}\_{C},(b-a)\mathbb{1}\_{D}) and (a​𝟙A′\C,(b−a)​𝟙B′\D)(a\mathbb{1}\_{A^{\prime}\backslash C},(b-a)\mathbb{1}\_{B^{\prime}\backslash D}) are comonotonic since the underlying events are nested. Then it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​(Y)+ρh2​(Z)\displaystyle\rho\_{h\_{1}}(Y)+\rho\_{h\_{2}}(Z) | =a​(h1​(u1)+h1​(u2))+(b−a)​(h2​(p1−u1)+h2​(p2−u2))\displaystyle=a\big(h\_{1}(u\_{1})+h\_{1}(u\_{2})\big)+(b-a)\big(h\_{2}(p\_{1}-u\_{1})+h\_{2}(p\_{2}-u\_{2})\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =a​h1​□h2​(p1)+(b−a)​h1​□h2​(p2)=ρh1​□h2​(X).\displaystyle=ah\_{1}\mathop{\square}\displaylimits h\_{2}(p\_{1})+(b-a)h\_{1}\mathop{\square}\displaylimits h\_{2}(p\_{2})=\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X). |  |

Consequently, ρh1​□ρh2​(X)≤ρh1​□h2​(X)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)\leq\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X).
∎

By translation invariance, one typically has ρh1​□ρh2​(𝟙A+c)≤ρh1​□h2​(𝟙A)+c\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(\mathbb{1}\_{A}+c)\leq\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(\mathbb{1}\_{A})+c for any constant cc, where the bound comes from handling the constant and the indicator separately.
Using Theorem [4](https://arxiv.org/html/2510.18236v1#Thmproposition4 "Proposition 4. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"), a tighter bound can be obtained by treating the constant as an additional layer over a disjoint set; see Corollary [2](https://arxiv.org/html/2510.18236v1#Thmcorollary2 "Corollary 2. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").

###### Corollary 2.

Suppose that h1,h2∈ℋh\_{1},h\_{2}\in\mathcal{H} and c∈ℝ+c\in\mathbb{R}\_{+}. For any A∈ℱA\in\mathcal{F}, it holds that

|  |  |  |
| --- | --- | --- |
|  | max⁡{h1​□h2​(ℙ​(A)),c​h1​□h2​(1)}≤ρh1​□ρh2​(𝟙A+c)≤ρh1​□h2​(𝟙A+c).\max\left\{h\_{1}\mathop{\square}\displaylimits h\_{2}(\mathbb{P}(A)),c\,h\_{1}\mathop{\square}\displaylimits h\_{2}(1)\right\}\leq\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(\mathbb{1}\_{A}+c)\leq\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(\mathbb{1}\_{A}+c). |  |

###### Proof.

The first inequality directly follows from Theorem [5](https://arxiv.org/html/2510.18236v1#Thmtheorem5 "Theorem 5. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").
It is immediate to show the second inequality by applying Theorem [4](https://arxiv.org/html/2510.18236v1#Thmproposition4 "Proposition 4. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") and replacing B=AcB=A^{c} and a=1+c=1+ba=1+c=1+b.
∎

The following proposition provides some results for random variables XX satisfying ℙ​(X>0)≤a\mathbb{P}(X>0)\leq a for some a∈[0,1]a\in[0,1]. We first introduce some notations for convenient. For any h1,h2∈ℋh\_{1},h\_{2}\in\mathcal{H}, let
xc=sup{x∈[0,1]:h1​□h2​(x)=h2​(x)}x\_{c}=\sup\left\{x\in[0,1]:h\_{1}\mathop{\square}\displaylimits h\_{2}(x)=h\_{2}(x)\right\} and xd=sup{x>0:h2+′​(x)≤1}x\_{d}=\sup\left\{x>0:{h\_{2}}\_{+}^{\prime}(x)\leq 1\right\}.

###### Proposition 5.

Suppose that 𝒳=L+\mathcal{X}=L^{+} and h1,h2∈ℋh\_{1},h\_{2}\in\mathcal{H}.
For X∈𝒳X\in\mathcal{X} with ℙ​(X>0)≤α\mathbb{P}(X>0)\leq\alpha, α∈[0,1)\alpha\in[0,1),
the following hold.

1. (i)

   If h1​□h2h\_{1}\mathop{\square}\displaylimits h\_{2} is convex and α≤1/2\alpha\leq 1/2, then ρh1​□ρh2​(X)≥ρh1​□h2​(X)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)\geq\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X).
2. (ii)

   If
   h2h\_{2} is convex and α≤xc/2\alpha\leq x\_{c}/2, then ρh1​□ρh2​(X)=ρh2​(X)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)=\rho\_{h\_{2}}(X).
3. (iii)

   If h1h\_{1} is concave, h2h\_{2} is convex and α≤max⁡{xc/2,xd}\alpha\leq\max\left\{x\_{c}/2,x\_{d}\right\},
   then ρh1​□ρh2​(X)=ρh2​(X)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)=\rho\_{h\_{2}}(X).

###### Proof.

(i) For any allocation (X1,X2)∈𝔸2​(X)(X\_{1},X\_{2})\in\mathbb{A}\_{2}(X) and a∈(0,∞)a\in(0,\infty), we have 𝔼​(X2∧a)+𝔼​(X1∧a)≥𝔼​(X∧a)\mathbb{E}(X\_{2}\wedge a)+\mathbb{E}(X\_{1}\wedge a)\geq\mathbb{E}(X\wedge a), implying that

|  |  |  |
| --- | --- | --- |
|  | ∫0a(ℙ​(X1>t)+ℙ​(X2>t))​dt≥∫0aℙ​(X>t)​dt.\int\_{0}^{a}(\mathbb{P}(X\_{1}>t)+\mathbb{P}(X\_{2}>t))\mathrm{d}t\geq\int\_{0}^{a}\mathbb{P}(X>t)\mathrm{d}t. |  |

By integral majorization theorem (Peajcariaac and Tong,, [1992](https://arxiv.org/html/2510.18236v1#bib.bib26), Theorem 12.15) and convexity of h1​□h2h\_{1}\mathop{\square}\displaylimits h\_{2}, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0ah1​□h2​(ℙ​(X1>t)+ℙ​(X2>t))​d​t≥∫0ah1​□h2​(ℙ​(X>t))​d​t.\displaystyle\int\_{0}^{a}h\_{1}\mathop{\square}\displaylimits h\_{2}(\mathbb{P}(X\_{1}>t)+\mathbb{P}(X\_{2}>t))\mathrm{d}t\geq\int\_{0}^{a}h\_{1}\mathop{\square}\displaylimits h\_{2}(\mathbb{P}(X>t))\mathrm{d}t. |  | (20) |

Note that ℙ​(X>0)≤1/2\mathbb{P}(X>0)\leq 1/2 ensures that h1​□h2h\_{1}\mathop{\square}\displaylimits h\_{2} is well-defined.
Then it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​(X1)+ρh2​(X2)\displaystyle\rho\_{h\_{1}}(X\_{1})+\rho\_{h\_{2}}(X\_{2}) | =∫0∞h1​(ℙ​(X1>t))+h2​(ℙ​(X2>t))​d​t\displaystyle=\int\_{0}^{\infty}h\_{1}(\mathbb{P}(X\_{1}>t))+h\_{2}(\mathbb{P}(X\_{2}>t))\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥∫0∞h1​□h2​(ℙ​(X1>t)+ℙ​(X2>t))​d​t≥ρh1​□h2​(X),\displaystyle\geq\int\_{0}^{\infty}h\_{1}\mathop{\square}\displaylimits h\_{2}(\mathbb{P}(X\_{1}>t)+\mathbb{P}(X\_{2}>t))\mathrm{d}t\geq\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X), |  |

which implies that ρh1​□ρh2​(X)≥ρh1​□h2​(X)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)\geq\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X).

(ii) Clearly, ρh1​□ρh2​(X)≤ρh2​(X)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)\leq\rho\_{h\_{2}}(X). It suffices to show the converse direction.
We first show that for any x≤x0x\leq x\_{0}, it holds that h1​□​h2​(x)=h2​(x)h\_{1}\square h\_{2}(x)=h\_{2}(x). By definition of x0x\_{0}, it follows that fx0​(y):=h1​(y)+h2​(x0−y)−h2​(x0)≥0f\_{x\_{0}}(y):=h\_{1}(y)+h\_{2}(x\_{0}-y)-h\_{2}(x\_{0})\geq 0 for y≤x0y\leq x\_{0}. Then for x≤x0x\leq x\_{0}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | h1​(y)+h2​(x−y)−h2​(x)=fx0​(y)−h2​(x0−y)+h2​(x−y)+h2​(x0)−h2​(x)≥0.\displaystyle h\_{1}(y)+h\_{2}(x-y)-h\_{2}(x)=f\_{x\_{0}}(y)-h\_{2}(x\_{0}-y)+h\_{2}(x-y)+h\_{2}(x\_{0})-h\_{2}(x)\geq 0. |  | (21) |

The inequality ([21](https://arxiv.org/html/2510.18236v1#S5.E21 "In 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) holds due to convexity of h2h\_{2}, implying that h2​(x0)−h2​(x)≥h2​(x0−y)−h2​(x−y)h\_{2}(x\_{0})-h\_{2}(x)\geq h\_{2}(x\_{0}-y)-h\_{2}(x-y).
For any allocation (X1,X2)∈𝔸2​(X)(X\_{1},X\_{2})\in\mathbb{A}\_{2}(X), it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​(X1)+ρh2​(X2)\displaystyle\rho\_{h\_{1}}(X\_{1})+\rho\_{h\_{2}}(X\_{2}) | ≥∫0∞h1​□h2​(ℙ​(X1>t)+ℙ​(X2>t))​d​t\displaystyle\geq\int\_{0}^{\infty}h\_{1}\mathop{\square}\displaylimits h\_{2}(\mathbb{P}(X\_{1}>t)+\mathbb{P}(X\_{2}>t))\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0∞h2​(ℙ​(X1>t)+ℙ​(X2>t))​dt\displaystyle=\int\_{0}^{\infty}h\_{2}(\mathbb{P}(X\_{1}>t)+\mathbb{P}(X\_{2}>t))\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥∫0∞h2​(ℙ​(X>t))​dt=ρh2​(X).\displaystyle\geq\int\_{0}^{\infty}h\_{2}(\mathbb{P}(X>t))\mathrm{d}t=\rho\_{h\_{2}}(X). |  |

The equality holds due to ℙ​(X>0)≤x0/2\mathbb{P}(X>0)\leq x\_{0}/2, which implies that
h1​□h2​(g1​(t)+g2​(t))=h2​(g1​(t)+g2​(t))h\_{1}\mathop{\square}\displaylimits h\_{2}(g\_{1}(t)+g\_{2}(t))=h\_{2}(g\_{1}(t)+g\_{2}(t)) for t≥0t\geq 0.
The second inequality follows from ([20](https://arxiv.org/html/2510.18236v1#S5.E20 "In 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) and convexity of h2h\_{2}.
Thus, it follows that
ρh1​□ρh2​(X)≥ρh2​(X)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)\geq\rho\_{h\_{2}}(X) for
any X∈𝒳X\in\mathcal{X} with ℙ​(X>0)≤x0/2\mathbb{P}(X>0)\leq x\_{0}/2. Therefore, the desired result is obtained.

(iii) Following from (ii), it suffices to show that the result holds for α=xd\alpha=x\_{d}.
For any allocation (X1,X2)(X\_{1},X\_{2}) of X∈𝒳X\in\mathcal{X}, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∫0∞h1​(ℙ​(X1>t))​dt+∫0∞h2​(ℙ​(X2>t))​dt\displaystyle\int\_{0}^{\infty}h\_{1}(\mathbb{P}(X\_{1}>t))\mathrm{d}t+\int\_{0}^{\infty}h\_{2}(\mathbb{P}(X\_{2}>t))\mathrm{d}t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≥∫0∞(ℙ​(X1>t)+h2​(ℙ​(X>t))+h2+′​(ℙ​(X>t))​(ℙ​(X2>t)−ℙ​(X>t)))​dt.\displaystyle\geq\int\_{0}^{\infty}\left(\mathbb{P}(X\_{1}>t)+h\_{2}(\mathbb{P}(X>t))+{h\_{2}}\_{+}^{\prime}(\mathbb{P}(X>t))(\mathbb{P}(X\_{2}>t)-\mathbb{P}(X>t))\right)\mathrm{d}t. |  | (22) |

The inequality holds due to concavity of h1h\_{1} and convexity of h2h\_{2}, implying that h1​(x)≥xh\_{1}(x)\geq x and
h2​(y)≥h2​(x)+h2+′​(x)​(y−x)h\_{2}(y)\geq h\_{2}(x)+{h\_{2}}\_{+}^{\prime}(x)(y-x) for any x,y∈[0,1]x,y\in[0,1]; see Theorem 25.1 of Rockafellar, ([1970](https://arxiv.org/html/2510.18236v1#bib.bib27)).
Next we show it always holds that h2+′​(ℙ​(X>t))≤1{h\_{2}}\_{+}^{\prime}(\mathbb{P}(X>t))\leq 1.
If xd=0x\_{d}=0, then h2h\_{2} is the identity function and h2+′​(x)=1{h\_{2}}\_{+}^{\prime}(x)=1. If xd>0x\_{d}>0, then h2+′​(ℙ​(X>t))≤1{h\_{2}}\_{+}^{\prime}(\mathbb{P}(X>t))\leq 1 since ℙ​(X>0)≤xd\mathbb{P}(X>0)\leq x\_{d}.
By the fact of ℙ​(X2>t)≤ℙ​(X>t)\mathbb{P}(X\_{2}>t)\leq\mathbb{P}(X>t) for t>0t>0 and ([22](https://arxiv.org/html/2510.18236v1#S5.E22 "In 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρh1​(X1)+ρh2​(X2)\displaystyle\rho\_{h\_{1}}(X\_{1})+\rho\_{h\_{2}}(X\_{2}) | ≥∫0∞(h2​(ℙ​(X>t))+ℙ​(X1>t)+ℙ​(X2>t)−ℙ​(X>t))​dt\displaystyle\geq\int\_{0}^{\infty}\left(h\_{2}(\mathbb{P}(X>t))+\mathbb{P}(X\_{1}>t)+\mathbb{P}(X\_{2}>t)-\mathbb{P}(X>t)\right)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0∞h2​(ℙ​(X>t))​dt=ρh2​(X).\displaystyle=\int\_{0}^{\infty}h\_{2}(\mathbb{P}(X>t))\mathrm{d}t=\rho\_{h\_{2}}(X). |  |

The above result implies that ρh1​□ρh2​(X)=ρh2​(X)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)=\rho\_{h\_{2}}(X) with ℙ​(X>0)≤xd\mathbb{P}(X>0)\leq x\_{d}. Consequently, the desired result is obtained.
∎

Proposition [5](https://arxiv.org/html/2510.18236v1#Thmproposition5 "Proposition 5. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") shows that
when the loss probability is sufficiently small, the efficient arrangement assigns the entire risky slice to the risk-seeking agent. Intuitively, small-probability losses are nearly “free” under a convex distortion function, so letting the risk-seeker absorb them minimizes the total risk value. Moreover, if the condition h1≥h2~h\_{1}\geq\widetilde{h\_{2}} holds, the relative strength of risk aversion over risk seeking is strong enough that the optimal arrangement assigns the entire risk (not just the small layer) to the risk-seeking agent; see Theorem [2](https://arxiv.org/html/2510.18236v1#Thmtheorem2 "Theorem 2. ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").

## 6 Applications to the original problem

In this section, we return to the nn-agent risk-sharing problem and demonstrate how the results established in Sections [4](https://arxiv.org/html/2510.18236v1#S4 "4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") and [5](https://arxiv.org/html/2510.18236v1#S5 "5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") can be applied to characterize optimal allocations in mixed economies, including both risk-averse and risk-seeking agents.
Recall that g1=⋀i=1mhig\_{1}=\bigwedge\_{i=1}^{m}h\_{i} and g2=□j=m+1n​hjg\_{2}=\square\_{j=m+1}^{n}h\_{j} for m≤nm\leq n.

###### Proposition 6.

Let 𝒳=L+\mathcal{X}=L^{+}. Assume that hi∈ℋh\_{i}\in\mathcal{H} are continuous for all i∈[n]i\in[n], with hih\_{i} concave for i∈[m]i\in[m] and hjh\_{j} convex for j∈[n]∖[m]j\in[n]\setminus[m], where m≤nm\leq n.
If g1≥h~ig\_{1}\geq\widetilde{h}\_{i} for some i∈[n]∖[m]i\in[n]\setminus[m],
then for any X∈𝒳⟂X\in\mathcal{X}^{\perp}, we have

|  |  |  |
| --- | --- | --- |
|  | □i=1nρhi​(X)=ρg2​(X).\displaystyle\mathop{\square}\displaylimits\_{i=1}^{n}\rho\_{h\_{i}}(X)=\rho\_{g\_{2}}(X). |  |

###### Proof.

We first note that the inf-convolution □i=1nρhi​(X)\mathop{\square}\displaylimits\_{i=1}^{n}\rho\_{h\_{i}}(X) is associative; see Lemma 2 of Liu et al., ([2020](https://arxiv.org/html/2510.18236v1#bib.bib24)).
Without loss of generality, we assume g1≥h~m+1g\_{1}\geq\widetilde{h}\_{m+1}.
By Theorem [3](https://arxiv.org/html/2510.18236v1#Thmtheorem3 "Theorem 3. ‣ 4.2 One risk-averse agent and one risk-seeking agent ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"), we have ρg1​□ρhm+1​(X)=ρhm+1​(X)\rho\_{g\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{m+1}}(X)=\rho\_{h\_{m+1}}(X). Thus,

|  |  |  |
| --- | --- | --- |
|  | □i=1nρhi​(X)=ρg1​□ρhm+1​□…​□ρhn​(X)=ρg2​(X).\displaystyle\mathop{\square}\displaylimits\_{i=1}^{n}\rho\_{h\_{i}}(X)=\rho\_{g\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{m+1}}\mathop{\square}\displaylimits\dots\mathop{\square}\displaylimits\rho\_{h\_{n}}(X)=\rho\_{g\_{2}}(X). |  |

Therefore, the desired result is obtained.
∎

Proposition [6](https://arxiv.org/html/2510.18236v1#Thmproposition6 "Proposition 6. ‣ 6 Applications to the original problem ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") states that
if the least risk-averse agent in the cautious group is more conservative than at least one risk-seeking agent is adventurous (formally, if g1≥h~ig\_{1}\geq\widetilde{h}\_{i}
for some convex hih\_{i}), then the efficient split assigns all the randomness to the risk-seeking side.
Intuitively, once there exists a single risk-seeker willing to absorb the entire uncertain part when they are sharing the risk with the most tolerant risk-averse agent, the problem effectively turns into a “betting game” among the risk-seeking agents.
In this case, the optimal allocation is counter-monotonic, that is, risk-averse agents bear nothing and
risk-seekers bet on who takes the total risk.

When such dominance condition fails and the risk seeking dominates risk aversion, the optimal risk sharing would change accordingly.
As we know, a full analysis with arbitrary distortion functions is challenging, so we focus on a tractable subclass of piecewise linear distortions.
Building on the two-agent analysis in Section [5](https://arxiv.org/html/2510.18236v1#S5 "5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"), the following proposition provides explicit formulas for the nn-agent inf-convolution across different settings.

###### Proposition 7.

Suppose that 𝒳=L+\mathcal{X}=L^{+} and m,n∈ℕm,n\in\mathbb{N}. Let hi​(x)=min⁡{x/bi,1}h\_{i}(x)=\min\left\{x/b\_{i},1\right\} for i∈[m]i\in[m] and
hi​(x)=max⁡{0,(x−ai)/(1−ai)}h\_{i}(x)=\max\left\{0,(x-a\_{i})/(1-a\_{i})\right\} for i∈[n]∖[m]i\in[n]\setminus[m] over x∈[0,1]x\in[0,1], where ai,bi∈(0,1)a\_{i},b\_{i}\in(0,1) with ∑i=m+1nai≤1\sum\_{i=m+1}^{n}a\_{i}\leq 1. Denote by b=⋁i=1mbib=\bigvee\_{i=1}^{m}b\_{i}.
Then the following hold for X∈𝒳⟂X\in\mathcal{X}^{\perp}.

* (i)

  If ai+b≤1a\_{i}+b\leq 1 for some i∈[n]\[m]i\in[n]\backslash[m], then

  |  |  |  |
  | --- | --- | --- |
  |  | □i=1nρhi​(X)=ρg​(X),where​g​(t)=max⁡{0,t−∑i=m+1nai1−⋁i=m+1nai},t∈[0,1].\displaystyle\mathop{\square}\displaylimits\_{i=1}^{n}\rho\_{h\_{i}}(X)=\rho\_{g}(X),~\text{where}~g(t)=\max\left\{0,\frac{t-\sum\_{i=m+1}^{n}a\_{i}}{1-\bigvee\_{i=m+1}^{n}a\_{i}}\right\},~t\in[0,1]. |  |
* (ii)

  If ⋀i=m+1nai+b>1\bigwedge\_{i=m+1}^{n}a\_{i}+b>1, then

  |  |  |  |
  | --- | --- | --- |
  |  | □i=1nρhi​(X)=ρg​(X),where​g​(t)=max⁡{0,t−∑i=m+1naib},t∈[0,1].\displaystyle\mathop{\square}\displaylimits\_{i=1}^{n}\rho\_{h\_{i}}(X)=\rho\_{g}(X),~\text{where}~g(t)=\max\left\{0,\frac{t-\sum\_{i=m+1}^{n}a\_{i}}{b}\right\},~t\in[0,1]. |  |

###### Proof.

Let ℓ​(t)=max⁡{0,(t−∑i=m+1nai)/(1−⋁i=m+1nai)}\ell(t)=\max\left\{0,(t-\sum\_{i=m+1}^{n}a\_{i})/({1-\bigvee\_{i=m+1}^{n}a\_{i}})\right\}.
It is straightforward to verity that □i=m+1nhi​(x)=ℓ​(x)\mathop{\square}\displaylimits\_{i=m+1}^{n}h\_{i}(x)=\ell(x).

(i) The result directly follows from Proposition [6](https://arxiv.org/html/2510.18236v1#Thmproposition6 "Proposition 6. ‣ 6 Applications to the original problem ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").

(ii) To make presentations more precise, we first introduce some notations, define

|  |  |  |
| --- | --- | --- |
|  | ℓ1​(x)=max⁡{0,x−∑i=m+1nai1−∑i=m+1nai},and​ℓ2​(x)=min⁡{x1−⋁i=m+1nai,1}​t∈[0,1].\displaystyle\ell\_{1}(x)=\max\left\{0,\frac{x-\sum\_{i=m+1}^{n}a\_{i}}{1-\sum\_{i=m+1}^{n}a\_{i}}\right\},~\text{and}~\ell\_{2}(x)=\min\left\{\frac{x}{1-\bigvee\_{i=m+1}^{n}a\_{i}},1\right\}~t\in[0,1]. |  |

Then it can be verified that ℓ1​□ℓ2​(x)=ℓ​(x)\ell\_{1}\mathop{\square}\displaylimits\ell\_{2}(x)=\ell(x) for x∈[0,1]x\in[0,1].
Note that ⋀i=m+1nai+b>1\bigwedge\_{i=m+1}^{n}a\_{i}+b>1 implies that ∑i=m+1nai+b>1\sum\_{i=m+1}^{n}a\_{i}+b>1.
By Proposition [2](https://arxiv.org/html/2510.18236v1#Thmproposition2 "Proposition 2. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρℓ1​□ρℓ2​(X)=ρℓ​(X).\displaystyle\rho\_{\ell\_{1}}\mathop{\square}\displaylimits\rho\_{\ell\_{2}}(X)=\rho\_{\ell}(X). |  | (23) |

Let h=⋀i=1mhih=\bigwedge\_{i=1}^{m}h\_{i}.
It follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | □i=1nρhi​(X)\displaystyle\mathop{\square}\displaylimits\_{i=1}^{n}\rho\_{h\_{i}}(X) | =ρh​□(□i=m+1nρhi)​(X)=ρh​□ρℓ​(X)=ρh​□(ρℓ1​□ρℓ2)​(X)\displaystyle=\rho\_{h}\mathop{\square}\displaylimits\left(\mathop{\square}\displaylimits\_{i=m+1}^{n}\rho\_{h\_{i}}\right)(X)=\rho\_{h}\mathop{\square}\displaylimits\rho\_{\ell}(X)=\rho\_{h}\mathop{\square}\displaylimits\left(\rho\_{\ell\_{1}}\mathop{\square}\displaylimits\rho\_{\ell\_{2}}\right)(X) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ρh​□ρℓ1​(X)=ρℓ​(X),\displaystyle=\rho\_{h}\mathop{\square}\displaylimits\rho\_{\ell\_{1}}(X)=\rho\_{\ell}(X), |  |

where ℓ​(t)=h​□ℓ1​(t)=max⁡{0,(t−∑i=m+1nai)/b}\ell(t)=h\mathop{\square}\displaylimits\ell\_{1}(t)=\max\left\{0,(t-\sum\_{i=m+1}^{n}a\_{i})/b\right\}.
The first equality follows from Theorem [2](https://arxiv.org/html/2510.18236v1#Thmtheorem2 "Theorem 2. ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").
By applying ([23](https://arxiv.org/html/2510.18236v1#S6.E23 "In 6 Applications to the original problem ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) and Proposition [2](https://arxiv.org/html/2510.18236v1#Thmproposition2 "Proposition 2. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"), we obtain the last three equalities.
∎

As shown in Proposition [7](https://arxiv.org/html/2510.18236v1#Thmproposition7 "Proposition 7. ‣ 6 Applications to the original problem ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"), when risk aversion dominates sufficiently, the risk-seeking group absorbs all randomness, consistent with Proposition [6](https://arxiv.org/html/2510.18236v1#Thmproposition6 "Proposition 6. ‣ 6 Applications to the original problem ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").
In contrast, when risk seeking dominates risk aversion, as described by condition (ii), the pattern of optimal risk sharing changes substantially. The risk-averse participants continue to share risk comonotonically within their own group, but they would collectively bet with the risk-seeking group. The resulting allocation is counter-monotonic across groups, reflecting a betting structure in which the risk-seeking side and the risk-averse side effectively compete over who absorbs the uncertainty.

## 7 Conclusion

In this paper, we study risk sharing in economies where agents need not be all risk-averse or all risk-seeking.
This mixed setting is economically important with capturing the coexistence of cautious and speculative participants, and mathematically challenging because the underlying distortion risk measures are neither all convex nor all concave.

With mixed attitudes in place (some are risk-averse and others are risk-seeking), we establish a two-agent reduction by aggregating risk attitudes on each side into representative distortions; see Theorem [1](https://arxiv.org/html/2510.18236v1#Thmtheorem1 "Theorem 1. ‣ 3 Problem reduction ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes"). The reduced problem can be solved via the inf-convolution ρh1​□ρh2\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}.
One of our main results (Theorem [2](https://arxiv.org/html/2510.18236v1#Thmtheorem2 "Theorem 2. ‣ 4.1 Two general agents ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) provides necessary and sufficient conditions for existence of optimal allocations.
When the conditions hold, the concave-convex case admits explicit solutions, in which the risk-seeking side bears all the risk, as shown in Theorem [3](https://arxiv.org/html/2510.18236v1#Thmtheorem3 "Theorem 3. ‣ 4.2 One risk-averse agent and one risk-seeking agent ‣ 4 Allocations in the whole space ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes").

We also consider the case of
restricted allocations that are nonnegative. This setting ensure a well-defined risk sharing problem and corresponds to the natural assumption of no profit from pure losses.
We compare the constrained value ρh1​□ρh2​(X)\rho\_{h\_{1}}\mathop{\square}\displaylimits\rho\_{h\_{2}}(X)
with the benchmark ρh1​□h2​(X)\rho\_{h\_{1}\mathop{\square}\displaylimits h\_{2}}(X).
Our analysis yields constructive bounds and equality conditions for specific distortion families (Theorems [4](https://arxiv.org/html/2510.18236v1#Thmtheorem4 "Theorem 4. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") and Proposition [2](https://arxiv.org/html/2510.18236v1#Thmproposition2 "Proposition 2. ‣ 5.1 Two agents with special distortion functions ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")) and for canonical risks (Theorems [5](https://arxiv.org/html/2510.18236v1#Thmtheorem5 "Theorem 5. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") and Proposition [4](https://arxiv.org/html/2510.18236v1#Thmproposition4 "Proposition 4. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")). Finally, we apply these results to resolve the original multi-agent problem.

## Acknowledgements

Mario Ghossoub acknowledges financial support from the Natural Sciences and Engineering Research Council of Canada (RGPIN-2024-03744). Ruodu Wang acknowledges financial support from the Natural Sciences and Engineering Research Council of Canada (RGPIN-2024-03728, CRC-2022-00141).

## References

* Acciaio, (2007)

  Acciaio, B. (2007).
  Optimal risk sharing with non-monotone monetary functionals.
  Finance and Stochastics, 11(2):267–289.
* Araujo et al., (2017)

  Araujo, A., Bonnisseau, J.-M., Chateauneuf, A., and Novinski, R. (2017).
  Optimal sharing with an infinite number of commodities in the presence of optimistic and pessimistic agents.
  Economic Theory, 63:131–157.
* Araujo et al., (2018)

  Araujo, A., Chateauneuf, A., Gama, J. P., and Novinski, R. (2018).
  General equilibrium with uncertainty loving preferences.
  Econometrica, 86(5):1859–1871.
* Barrieu and El Karoui, (2005)

  Barrieu, P. and El Karoui, N. (2005).
  Inf-convolution of risk measures and optimal risk transfer.
  Finance and stochastics, 9(2):269–298.
* Beißner et al., (2024)

  Beißner, P., Boonen, T., and Ghossoub, M. (2024).
  (No-)betting pareto optima under rank-dependent utility.
  Mathematics of Operations Research, 49(3):1452–1471.
* Beißner and Werner, (2023)

  Beißner, P. and Werner, J. (2023).
  Optimal allocations with α\alpha-maxmin utilities, choquet expected utilities, and prospect theory.
  Theoretical Economics, 18(3):993–1022.
* Borch, (1962)

  Borch, K. (1962).
  Equilibrium in a Reinsurance Market.
  Econometrica, 30(3):424–444.
* Dhaene and Denuit, (1999)

  Dhaene, J. and Denuit, M. (1999).
  The safest dependence structure among risks.
  Insurance: Mathematics and Economics, 25(1):11–21.
* Dhaene et al., (2002)

  Dhaene, J., Denuit, M., Goovaerts, M. J., Kaas, R., and Vyncke, D. (2002).
  The concept of comonotonicity in actuarial science and finance: theory.
  Insurance: Mathematics and Economics, 31(1):3–33.
* Embrechts et al., (2018)

  Embrechts, P., Liu, H., and Wang, R. (2018).
  Quantile-Based Risk Sharing.
  Operations Research, 66(4):936–949.
* Embrechts et al., (2015)

  Embrechts, P., Wang, B., and Wang, R. (2015).
  Aggregation-robustness and model uncertainty of regulatory risk measures.
  Finance and Stochastics, 19(4):763–790.
* Filipović and Svindland, (2008)

  Filipović, D. and Svindland, G. (2008).
  Optimal Capital and Risk Allocations for Law-and Cash-Invariant Convex Functions.
  Finance and Stochastics, 12:423–439.
* Föllmer and Schied, (2016)

  Föllmer, H. and Schied, A. (2016).
  Stochastic finance: an introduction in discrete time.
  Walter de Gruyter.
* Ghossoub et al., (2024)

  Ghossoub, M., Ren, Q., and Wang, R. (2024).
  Counter-monotonic risk sharing with heterogeneous distortion risk measures.
  arXiv preprint arXiv:2412.00655.
* Ghossoub et al., (2025)

  Ghossoub, M., Ren, Q., and Wang, R. (2025).
  Counter-monotonic risk allocations and distortion risk measures.
  Scandinavian Actuarial Journal, pages 1–24.
* Ghossoub and Zhu, (2024)

  Ghossoub, M. and Zhu, M. B. (2024).
  Efficiency in pure-exchange economies with risk-averse monetary utilities.
  Mathematical Finance.
* Heath and Ku, (2004)

  Heath, D. and Ku, H. (2004).
  Pareto equilibria with coherent measures of risk.
  Mathematical Finance: An International Journal of Mathematics, Statistics and Financial Economics, 14(2):163–172.
* Herings and Yang, (2022)

  Herings, P. and Yang, Z. (2022).
  Competitive equilibria in incomplete markets with risk loving preferences.
  CentER Discussion Paper.
* Jouini et al., (2008)

  Jouini, E., Schachermayer, W., and Touzi, N. (2008).
  Optimal risk sharing for law invariant monetary utility functions.
  Mathematical Finance, 18(2):269–292.
* Landsberger and Meilijson, (1994)

  Landsberger, M. and Meilijson, I. (1994).
  Co-monotone allocations, Bickel-Lehmann dispersion and the Arrow-Pratt measure of risk aversion.
  Annals of Operations Research, 52:97–106.
* Lauzier et al., (2025)

  Lauzier, J.-G., Lin, L., Peter, W., and Wang, R. (2025).
  Optimal risk sharing, equilibria, and welfare with empirically realistic risk attitudes.
  arXiv preprint arXiv:2401.03328.
* Lauzier et al., (2023)

  Lauzier, J.-G., Lin, L., and Wang, R. (2023).
  Pairwise counter-monotonicity.
  Insurance: Mathematics and Economics, 111:279–287.
* Lauzier et al., (2024)

  Lauzier, J.-G., Lin, L., and Wang, R. (2024).
  Risk sharing, measuring variability, and distortion riskmetrics.
  Mathematical Finance.
* Liu et al., (2020)

  Liu, P., Wang, R., and Wei, L. (2020).
  Is the inf-convolution of law-invariant preferences law-invariant?
  Insurance: Mathematics and Economics, 91:144–154.
* Mastrogiacomo and Rosazza Gianin, (2015)

  Mastrogiacomo, E. and Rosazza Gianin, E. (2015).
  Pareto optimal allocations and optimal risk sharing for quasiconvex risk measures.
  Mathematics and Financial Economics, 9(2):149–167.
* Peajcariaac and Tong, (1992)

  Peajcariaac, J. E. and Tong, Y. L. (1992).
  Convex functions, partial orderings, and statistical applications.
  Academic Press.
* Rockafellar, (1970)

  Rockafellar, R. T. (1970).
  Convex analysis.
  Princeton University Press.
* Tsanakas, (2009)

  Tsanakas, A. (2009).
  To split or not to split: Capital allocation with convex risk measures.
  Insurance: Mathematics and Economics, 44(2):268–277.
* Wang and Wei, (2020)

  Wang, R. and Wei, Y. (2020).
  Characterizing optimal allocations in quantile-based risk sharing.
  Insurance: Mathematics and Economics, 93:288–300.
* Wang et al., (2020)

  Wang, R., Wei, Y., and Willmot, G. E. (2020).
  Characterization, robustness, and aggregation of signed choquet integrals.
  Mathematics of Operations Research, 45(3):993–1015.
* Weber, (2018)

  Weber, S. (2018).
  Solvency II, or how to sweep the downside risk under the carpet.
  Insurance: Mathematics and economics, 82:191–200.
* Yaari, (1987)

  Yaari, M. E. (1987).
  The dual theory of choice under risk.
  Econometrica, 55(1):95–115.

## Appendix A Details in Example [8](https://arxiv.org/html/2510.18236v1#Thmexample8 "Example 8. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")

The details in Example [8](https://arxiv.org/html/2510.18236v1#Thmexample8 "Example 8. ‣ 5.2 Two agents sharing a Bernoulli-type risk ‣ 5 Nonnegative allocations ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") are guaranteed by the following proposition.

###### Proposition 8.

Suppose that h1​(x)=1−(1−x)αh\_{1}(x)=1-(1-x)^{\alpha} and h2​(x)=xβh\_{2}(x)=x^{\beta} for x∈[0,1]x\in[0,1]
with 1<α<β1<\alpha<\beta. Let p0=(α/β)1β−1p\_{0}=(\alpha/\beta)^{\frac{1}{\beta-1}}. Then there exists y∗​(x)y^{\*}(x) such that h1​(y∗​(x))+h2​(x−y∗​(x))=h1​□h2​(x)h\_{1}(y^{\*}(x))+h\_{2}(x-y^{\*}(x))=h\_{1}\mathop{\square}\displaylimits h\_{2}(x).
Moreover,

1. (i)

   If x≤p0x\leq p\_{0}, y∗​(x)=0y^{\*}(x)=0 and x−y∗​(x)=xx-y^{\*}(x)=x.
2. (ii)

   If x>p0x>p\_{0}, y∗​(x)y^{\*}(x) satisfies that α​(1−y∗​(x))α−1=β​(x−y∗​(x))β−1\alpha(1-y^{\*}(x))^{\alpha-1}=\beta(x-y^{\*}(x))^{\beta-1}. Moreover, y∗​(x)y^{\*}(x) is increasing and x−y∗​(x)x-y^{\*}(x) is decreasing.

###### Proof.

Let g​(y)=h1​(y)+h2​(x−y)g(y)=h\_{1}(y)+h\_{2}(x-y) for x∈[0,1]x\in[0,1] and y∈[0,x]y\in[0,x]. Then

|  |  |  |
| --- | --- | --- |
|  | g′​(y)=h1′​(y)−h2′​(x−y)=α​(1−y)α−1−β​(x−y)β−1.\displaystyle g^{\prime}(y)=h\_{1}^{\prime}(y)-h\_{2}^{\prime}(x-y)=\alpha(1-y)^{\alpha-1}-\beta(x-y)^{\beta-1}. |  |

Let R​(y)=α​(1−y)α−1β​(x−y)β−1R(y)=\frac{\alpha(1-y)^{\alpha-1}}{\beta(x-y)^{\beta-1}}. By straightforward calculation, we have

|  |  |  |
| --- | --- | --- |
|  | ln⁡R​(y)=ln⁡α−ln⁡β+(α−1)​ln⁡(1−y)−(β−1)​ln⁡(x−y)​and​(ln⁡R​(y))′=β−1x−y−α−11−y.\displaystyle\ln R(y)=\ln\alpha-\ln\beta+(\alpha-1)\ln(1-y)-(\beta-1)\ln(x-y)\ \text{and}\ (\ln R(y))^{\prime}=\frac{\beta-1}{x-y}-\frac{\alpha-1}{1-y}. |  |

Since α<β\alpha<\beta, (ln⁡R​(y))′>0(\ln R(y))^{\prime}>0, thus ln⁡R​(y)\ln R(y) is increasing. Also, ln⁡R​(0)=ln⁡α−ln⁡β−(β−1)​ln⁡x\ln R(0)=\ln\alpha-\ln\beta-(\beta-1)\ln x.
Next, we consider two cases:

1. (i)

   If x≤p0x\leq p\_{0}, then ln⁡R​(y)≥ln⁡R​(0)≥0\ln R(y)\geq\ln R(0)\geq 0 for y∈[0,x]y\in[0,x]. This implies that R​(y)≥1R(y)\geq 1 and g′​(y)≥0g^{\prime}(y)\geq 0, thus g​(y)g(y) is increasing. Hence, the infimum of g​(y)g(y) over y∈[0,x]y\in[0,x] attains at y∗=0y^{\*}=0.
2. (ii)

   If x>p0x>p\_{0}, then ln⁡R​(0)<0\ln R(0)<0 and ln⁡R​(y)→+∞\ln R(y)\rightarrow+\infty as y↓xy\downarrow x. Thus, g′​(y)g^{\prime}(y) would be first less than zero and then cross zero. Then first order condition gives:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | g′​(y∗)=h1′​(y∗)−h2′​(x−y∗)=α​(1−y∗)α−1−β​(x−y∗)β−1=0.\displaystyle g^{\prime}(y^{\*})=h\_{1}^{\prime}(y^{\*})-h\_{2}^{\prime}(x-y^{\*})=\alpha(1-y^{\*})^{\alpha-1}-\beta(x-y^{\*})^{\beta-1}=0. |  | (24) |

   Write F​(x,y∗)=α​(1−y∗)α−1−β​(x−y∗)β−1F(x,y^{\*})=\alpha(1-y^{\*})^{\alpha-1}-\beta(x-y^{\*})^{\beta-1}. Then it follows that

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | d​y∗d​x\displaystyle\frac{\mathrm{d}y^{\*}}{\mathrm{d}x} | =−∂F/∂x∂F​∂y=β​(β−1)​(x−y∗)β−2β​(β−1)​(x−y∗)β−2−α​(α−1)​(1−y∗)α−2=11−α−1β−1​x−y∗1−y∗>0.\displaystyle=-\frac{\partial F/\partial x}{\partial F\ \partial y}=\frac{\beta(\beta-1)(x-y^{\*})^{\beta-2}}{\beta(\beta-1)(x-y^{\*})^{\beta-2}-\alpha(\alpha-1)(1-y^{\*})^{\alpha-2}}=\frac{1}{1-\frac{\alpha-1}{\beta-1}\frac{x-y^{\*}}{1-y^{\*}}}>0. |  |

   The last equality can be obtained from
   ([24](https://arxiv.org/html/2510.18236v1#A1.E24 "In item (ii) ‣ Appendix A Details in Example 8 ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes")).
   By straightforward calculation,
   we have

   |  |  |  |
   | --- | --- | --- |
   |  | d​(x−y∗)d​x=1−d​y∗d​x=−(α−1)​(x−y∗)(β−1)​(1−y∗)−(α−1)​(x−y∗)<0.\displaystyle\frac{\mathrm{d}(x-y^{\*})}{\mathrm{d}x}=1-\frac{\mathrm{d}y^{\*}}{\mathrm{d}x}=\frac{-(\alpha-1)(x-y^{\*})}{(\beta-1)(1-y^{\*})-(\alpha-1)(x-y^{\*})}<0. |  |

Consequently, the desired result is obtained.
∎

## Appendix B Basic properties of the constrained inf-convolution

Let (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) be an atomless probability space and 𝒳=L+\mathcal{X}=L^{+} be the set
of nonnegative random variables in this space.
For risk functionals ρ1,ρ2:𝒳↦[0,∞)\rho\_{1},\rho\_{2}:\mathcal{X}\mapsto[0,\infty), define the constrained inf-convolution

|  |  |  |
| --- | --- | --- |
|  | ρ1​□ρ2​(X)=inf{ρ1​(Y)+ρ2​(X−Y),0≤Y≤X},X∈𝒳.\rho\_{1}\mathop{\square}\displaylimits\rho\_{2}(X)=\inf\left\{\rho\_{1}(Y)+\rho\_{2}(X-Y),0\leq Y\leq X\right\},~~X\in\mathcal{X}. |  |

The constraint 0≤Y≤X0\leq Y\leq X ensures Y,X−Y∈𝒳Y,X-Y\in\mathcal{X}.
Here we record several properties that can pass from ρ1\rho\_{1} and ρ2\rho\_{2} to their constrained inf-convolution
ρ1​□ρ2\rho\_{1}\mathop{\square}\displaylimits\rho\_{2}.
Our focus in this appendix is the constrained formulation. The corresponding properties in the unconstrained case have been well studied in Liu et al., ([2020](https://arxiv.org/html/2510.18236v1#bib.bib24)).

###### Lemma 2.

Suppose that 𝒳=L+\mathcal{X}=L^{+} and X∈𝒳X\in\mathcal{X}.
Let ρ1,ρ2\rho\_{1},\rho\_{2} be two risk functionals.

1. (i)

   If ρ1\rho\_{1} and ρ2\rho\_{2} are monotone, then ρ1​□​ρ2\rho\_{1}\square\rho\_{2} is monotone.
2. (ii)

   If ρ1\rho\_{1} and ρ2\rho\_{2} are uniformly continuous, then ρ1​□​ρ2\rho\_{1}\square\rho\_{2} is uniformly continuous.
3. (iii)

   If ρ1\rho\_{1} and ρ2\rho\_{2} are monotone and one of them is continuous from above, then ρ1​□​ρ2\rho\_{1}\square\rho\_{2} is continuous from above.

###### Proof.

1. (i)

   Suppose that X,Y∈𝒳X,Y\in\mathcal{X} with X≤YX\leq Y. For any ε>0\varepsilon>0, there exists ZY∈𝒳Z\_{Y}\in\mathcal{X} such that 0≤ZY≤Y0\leq Z\_{Y}\leq Y and
   ρ\_1(Z\_Y)+ρ\_2(Y-Z\_Y)≤ρ\_1 □ ρ\_2(Y)+ε.
   Let Z~=ZY∧X\widetilde{Z}=Z\_{Y}\wedge X (so 0≤Z~≤X0\leq\widetilde{Z}\leq X). Thus, Z~≤ZY\widetilde{Z}\leq Z\_{Y} and X−Z~≤Y−ZYX-\widetilde{Z}\leq Y-Z\_{Y}.
   Then
   ρ\_1 □ ρ\_2(X)≤ρ\_1(~Z)+ρ\_2(X-~Z)≤ρ\_1(Z\_Y)+ρ\_2(Y-Z\_Y)≤ρ\_1 □ ρ\_2(Y)+ε.
   Since ε>0\varepsilon>0 is arbitrary, we obtain ρ1​□ρ2​(X)≤ρ1​□ρ2​(Y)\rho\_{1}\mathop{\square}\displaylimits\rho\_{2}(X)\leq\rho\_{1}\mathop{\square}\displaylimits\rho\_{2}(Y).
2. (ii)

   Since ρ1\rho\_{1} and ρ2\rho\_{2} are uniformly continuous, for any ε>0\varepsilon>0, there exists δi\delta\_{i} for i=1,2i=1,2 such that for all X,Y∈𝒳X,Y\in\mathcal{X}, ‖X−Y‖⩽δi\|X-Y\|\leqslant\delta\_{i} implies |ρi​(X)−ρi​(Y)|⩽ε/3\left|\rho\_{i}(X)-\rho\_{i}(Y)\right|\leqslant\varepsilon/3.
   By definition of ρ1​□ρ2\rho\_{1}\mathop{\square}\displaylimits\rho\_{2}, there exists ZX∈[0,X]Z\_{X}\in[0,X] such that ρ1​(ZX)+ρ2​(X−ZX)≤ρ1​□ρ2​(X)+ε/3\rho\_{1}(Z\_{X})+\rho\_{2}(X-Z\_{X})\leq\rho\_{1}\mathop{\square}\displaylimits\rho\_{2}(X)+\varepsilon/3.
   Let Z′=ZX∧YZ^{\prime}=Z\_{X}\wedge Y and
   δ=min⁡{δ1,δ2/2}\delta=\min\left\{\delta\_{1},\delta\_{2}/2\right\}.
   For any X,Y∈𝒳X,Y\in\mathcal{X} with ‖X−Y‖⩽δ1\|X-Y\|\leqslant\delta\_{1}, we have
   ∥Z’-Z\_X∥ ≤∥X-Y∥≤δ and  ∥(X-Z\_X)-(Y-Z’)∥≤∥X-Y∥+∥Z’-Z\_X∥ ≤δ\_2.
   Then it follows that

   |  |  |  |
   | --- | --- | --- |
   |  | |ρ1​□ρ2​(X)−ρ1​□ρ2​(Y)|\displaystyle|\rho\_{1}\mathop{\square}\displaylimits\rho\_{2}(X)-\rho\_{1}\mathop{\square}\displaylimits\rho\_{2}(Y)| |  |
   |  |  |  |
   | --- | --- | --- |
   |  | ≤|ρ1​(ZX)+ρ2​(X−ZX)−ρ1​(Z′)−ρ2​(Y−Z′)|+ε/3\displaystyle\leq|\rho\_{1}(Z\_{X})+\rho\_{2}(X-Z\_{X})-\rho\_{1}(Z^{\prime})-\rho\_{2}(Y-Z^{\prime})|+\varepsilon/3 |  |
   |  |  |  |
   | --- | --- | --- |
   |  | ≤|ρ1​(ZX)−ρ1​(Z′)|+|ρ2​(X−ZX)−ρ2​(Y−Z′)|+ε/3≤ε.\displaystyle\leq|\rho\_{1}(Z\_{X})-\rho\_{1}(Z^{\prime})|+|\rho\_{2}(X-Z\_{X})-\rho\_{2}(Y-Z^{\prime})|+\varepsilon/3\leq\varepsilon. |  |

   Hence, ρ1​□ρ2\rho\_{1}\mathop{\square}\displaylimits\rho\_{2} is uniformly continuous.
3. (iii)

   Without loss of generality, we assume ρ2\rho\_{2} is continuous from above.
   By part (i), we have ρ1​□​ρ2\rho\_{1}\square\rho\_{2} is monotone. Let {Xn}n∈ℕ\left\{X\_{n}\right\}\_{n\in\mathbb{N}} be a sequence in 𝒳\mathcal{X} such that Xn↓XX\_{n}\downarrow X as n→∞n\rightarrow\infty.
   For any ε>0\varepsilon>0 and choose Z∈𝒳Z\in\mathcal{X} with 0≤Z≤X0\leq Z\leq X such that
   ρ\_1(Z)+ρ\_2(X-Z) ≤ρ\_1 □ ρ\_2(X)+ε.

   Since Xn↓XX\_{n}\downarrow X and Z≤XZ\leq X, we have Z≤XnZ\leq X\_{n} for all nn. Hence,
   lim sup\_n→∞ ρ\_1 □ρ\_2(X\_n) ≤ρ\_1(Z)+lim sup\_n→∞ ρ\_2(X\_n-Z)=ρ\_1(Z)+ρ\_2(X-Z) .
   Thus, lim supn→∞ρ1​□​ρ2​(Xn)≤ρ1​□​ρ2​(X)\limsup\_{n\rightarrow\infty}\rho\_{1}\square\rho\_{2}\left(X\_{n}\right)\leq\rho\_{1}\square\rho\_{2}\left(X\right).
   On the other hand, since ρ1​□​ρ2\rho\_{1}\square\rho\_{2} is monotone, we have ρ1​□​ρ2​(Xn)⩾ρ1​□​ρ2​(X)\rho\_{1}\square\rho\_{2}\left(X\_{n}\right)\geqslant\rho\_{1}\square\rho\_{2}(X). This implies
   lim\_n →∞ ρ\_1 □ρ\_2(X\_n)=ρ\_1 □ρ\_2(X).
   Hence, ρ1​□​ρ2\rho\_{1}\square\rho\_{2} is continuous from above.

The desired result is obtained.
∎

Lemma [2](https://arxiv.org/html/2510.18236v1#Thmlemma2 "Lemma 2. ‣ Appendix B Basic properties of the constrained inf-convolution ‣ Optimal Allocations with Distortion Risk Measures and Mixed Risk Attitudes") shows that monotonicity of ρ1​□ρ2\rho\_{1}\mathop{\square}\displaylimits\rho\_{2} under nonnegative allocations requires both ρ1\rho\_{1} and ρ2\rho\_{2} to be monotone. For general allocation sets, one monotone component is sufficient, as shown in Lemma 1 of Liu et al., ([2020](https://arxiv.org/html/2510.18236v1#bib.bib24)). The example below demonstrates that this sufficiency fails when allocations are constrained to be nonnegative.

###### Example 10.

Take (Ω,ℱ,ℙ)=([0,1],ℬ​([0,1]),λ)(\Omega,\mathcal{F},\mathbb{P})=([0,1],\mathcal{B}([0,1]),\lambda) where λ\lambda is the Lebesgue measure.
Let B⊂[0,1]B\subset[0,1] satisfy λ​(B)=12\lambda(B)=\frac{1}{2}.
Define two risk functionals ρ1​(X)=1−𝟙{X∼Bernoulli⁡(12)}\rho\_{1}(X)=1-\mathbb{1}\_{\left\{X\sim\operatorname{Bernoulli}\left(\frac{1}{2}\right)\right\}} and ρ2​(X)=𝔼​[X]\rho\_{2}(X)=\mathbb{E}[X].
Set

|  |  |  |
| --- | --- | --- |
|  | X=c​𝟙B​ with ​c∈(0,1)​ and ​Y=𝟙B.X=c\mathbb{1}\_{B}~\text{ with }c\in(0,1)~\text{ and }~Y=\mathbb{1}\_{B}. |  |

Clearly 0≤X≤Y0\leq X\leq Y.
Any feasible 0≤Z≤X0\leq Z\leq X satisfies Z=0Z=0 on BcB^{c} and 0≤Z≤c<10\leq Z\leq c<1 on BB.
Hence ρ1​(Z)=1\rho\_{1}(Z)=1 for all 0≤Z≤X0\leq Z\leq X.
Therefore,

|  |  |  |
| --- | --- | --- |
|  | ρ1​□ρ2​(X)=ρ1​(X)+ρ2​(0)=1>ρ1​(Y)+ρ2​(0)=0≥ρ1​□ρ2​(Y).\rho\_{1}\mathop{\square}\displaylimits\rho\_{2}(X)=\rho\_{1}(X)+\rho\_{2}(0)=1>\rho\_{1}(Y)+\rho\_{2}(0)=0\geq\rho\_{1}\mathop{\square}\displaylimits\rho\_{2}(Y). |  |

In this case, ρ1​□ρ2\rho\_{1}\mathop{\square}\displaylimits\rho\_{2} is not monotone.