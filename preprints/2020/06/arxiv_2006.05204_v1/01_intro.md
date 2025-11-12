---
authors:
- Dmitry B. Rokhlin
doc_id: arxiv:2006.05204v1
family_id: arxiv:2006.05204
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[2006.05204] Relative utility bounds for empirically optimal portfolios'
url_abs: http://arxiv.org/abs/2006.05204v1
url_html: https://ar5iv.org/html/2006.05204v1
venue: arXiv q-fin
version: 1
year: 2020
---


Dmitry B. Rokhlin
I.I. Vorovich Institute of Mathematics, Mechanics and Computer Sciences and Regional Scientific and Educational Mathematical Center of Southern Federal University
[dbrohlin@sfedu.ru](mailto:dbrohlin@sfedu.ru)

###### Abstract.

We consider a single-period portfolio selection problem for an investor, maximizing the expected ratio of the portfolio utility and the utility of a best asset taken in hindsight. The decision rules are based on the history of stock returns with unknown distribution. Assuming that the utility function is Lipschitz or Hölder continuous (the concavity is not required), we obtain high probability utility bounds under the sole assumption that the returns are independent and identically distributed. These bounds depend only on the utility function, the number of assets and the number of observations. For concave utilities similar bounds are obtained for the portfolios produced by the exponentiated gradient method. Also we use statistical experiments to study risk and generalization properties of empirically optimal portfolios. Herein we consider a model with one risky asset and a dataset, containing the stock prices from NYSE.

###### Key words and phrases:

Portfolio selection; Relative utility; Statistical learning; Empirical utility; Generalization bounds

###### 2020 Mathematics Subject Classification:

91G10, 68Q32

The research is supported by the Russian Science Foundation, project 17-19-01038

## 1. Introduction

We consider a single-period portfolio selection problem, where the decision rules are based on the history of stock returns. It is assumed that the returns are independent and identically distributed, but their distribution is unknown. We represent investor’s preferences by an expected utility and use the sample average approximation (SAA) (see, e.g., [[17](#bib.bib17)]) for the solution of the related expected utility maximization problem. In the terminology of the statistical learning theory our main goal is to obtain high-probability bounds (generalization bounds or utility bounds) for the difference between the optimal utility value and the true utility of the empirically optimal portfolio (estimation error), as well as for the difference between the true utility and the empirical utility for such portfolio.

Let us mention two specific features of the problem under consideration, which make some difficulties in an application of standard results. First, some classical utility functions, like the power function, are neither bounded nor globally Lipschitz. Second, most classical models, like the Black-Scholes, assume that the returns are unbounded. Similar unbounded problems appear in general learning theory: see [[6](#bib.bib6)] and a lot of references therein. They require some additional assumptions, problem reformulations and the development of special tools.

In the present paper we pass to the *relative* utility maximization, where the objective function equals to the expected ratio of the utility u𝑢u of some portfolio to the utility of the best portfolio for the returns, which are known in hindsight. This allows to avoid any assumption on the returns, besides the i.i.d. hypothesis. As for u𝑢u, we assume that it belongs to the class of positive, non-decreasing functions, satisfying the global Lipschitz or Hölder condition, and some specific condition, regarding its behavior at zero and infinity. The power function satisfies these assumptions. For the same problem with a concave utility function we study the estimation error for the portfolio produced by the stochastic version of the exponentiated gradient algorithm of [[18](#bib.bib18)].

The obtained utility bounds contain only those quantities, which are known for the investor: the number of return observations; the number of stocks; constants, related to the utility function; and a data-dependent quantity in the case of the exponentiated gradient algorithm: Theorems [1](#Thmtheorem1 "Theorem 1. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios") – [3](#Thmtheorem3 "Theorem 3. ‣ 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios").

Passing to the relative utility certainly affects investor’s attitude towards risk. In the case of one risky asset it appears, that an investor with the relative utility is more risk averse than in the case of the ordinary utility. However, in the case of multiple risky assets our empirical results show that the situation can be the opposite. Furthermore, we present simple statistical experiments demonstrating that typically it is impossible to get a reliable estimate of the optimal portfolio on the base of daily historical observations. A related phenomenon, which was mainly demonstrated for the risk-return modeling of investor’s preferences, is known as the fragility of SAA in portfolio optimization: see [[1](#bib.bib1)] and references therein.

Let us mention some papers, considering single-period portfolio selection problems in the statistical learning framework. In [[8](#bib.bib8), [10](#bib.bib10)], the authors studied the influence of the portfolio constraints on the out-of-sample performance. The papers [[10](#bib.bib10), [11](#bib.bib11)] presented out-of-sample bounds for the loss probabilities of the portfolios, satisfying some empirical VaR- and CVaR-type constraints. The regularization and cross validation methods were applied to the mean-variance and mean-CVaR problems in [[1](#bib.bib1)]. One can also find in [[1](#bib.bib1)] several other references to the works, considering the regularization methods. In [[2](#bib.bib2)] the authors considered an expected utility maximization problem with side information and applied a regularization to obtain out-of-sample guarantees for the certainty equivalent of the out-of-sample portfolio value.

The rest of the paper is organized as follows. In Section [2](#S2 "2. Problem formulation ‣ Relative utility bounds for empirically optimal portfolios") we state the problem and mention the consistency of the SAA method. Section [3](#S3 "3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios") contains the main result of the paper: Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios"), which gives upper bounds for the expected maximum of an empirical process, associated to the relative utility function. The Lipschitz and Hölder cases are studied separately. In both cases we consider the Rademacher complexity of the class of relative utility functions, parametrized by the portfolio weights. In the Lipshitz case this quantity is estimated by the Talagrand contraction lemma and the Massart lemma, in the Hölder case we consider the packing numbers and the Dudley entropy integral. The obtained estimates directly lead to high-probability utility bounds via the concentration inequalities. Section [4](#S4 "4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios") presents similar bounds for the portfolios produced by the stochastic exponentiated gradient algorithm of [[18](#bib.bib18)]. Here we combine its online version with the online-to-batch conversion scheme: see [[22](#bib.bib22)].

Sections [5](#S5 "5. Power utility: the case of one risky asset ‣ Relative utility bounds for empirically optimal portfolios") and [6](#S6 "6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios") deal with statistical experiments, related to the analysis of risk and generalization properties of empirically optimal portfolios. Section [5](#S5 "5. Power utility: the case of one risky asset ‣ Relative utility bounds for empirically optimal portfolios") considers the case of one risky asset, obeying the discrete Black-Scholes model, while in Section [6](#S6 "6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios") we analyze a dataset, containing daily stock returns form NYSE. The conclusions are already briefly described above. Here we additionally indicate the utilized solution methods for the empirical utility maximization problems. In Section [5](#S5 "5. Power utility: the case of one risky asset ‣ Relative utility bounds for empirically optimal portfolios") the problem is one-dimensional, and it is solved simply via the bisection method. In Section [6](#S6 "6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios") we propose a greedy modification of the stochastic exponentiated gradient algorithm to solve the correspondent is multidimensional problem. For logarithmic utility the results are compared with [[4](#bib.bib4), [13](#bib.bib13)]. The code for Sections [5](#S5 "5. Power utility: the case of one risky asset ‣ Relative utility bounds for empirically optimal portfolios"), [6](#S6 "6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios") is available at <https://github.com/drokhlin/Relative_utility_bounds_code>.

## 2. Problem formulation

Let (sk1,…,skd)superscriptsubscript𝑠𝑘1…superscriptsubscript𝑠𝑘𝑑(s\_{k}^{1},\dots,s\_{k}^{d}) be strictly positive prices of d𝑑d assets (stocks) at time moments k=0,…,n+1𝑘

0…𝑛1k=0,\dots,n+1, and let rkj=sij/sk−1jsuperscriptsubscript𝑟𝑘𝑗superscriptsubscript𝑠𝑖𝑗superscriptsubscript𝑠𝑘1𝑗r\_{k}^{j}=s\_{i}^{j}/s\_{k-1}^{j}, j=1,…,d𝑗

1…𝑑j=1,\dots,d, k=1,…,n+1𝑘

1…𝑛1k=1,\dots,n+1 be the total daily returns (price relatives). At time n𝑛n an investor distributes his wealth Xn=1subscript𝑋𝑛1X\_{n}=1 between these assets based on the price history (r1,…,rn)subscript𝑟1…subscript𝑟𝑛(r\_{1},\dots,r\_{n}). In other words, he selects a portfolio (γn1,…,γnd)superscriptsubscript𝛾𝑛1…superscriptsubscript𝛾𝑛𝑑(\gamma\_{n}^{1},\dots,\gamma\_{n}^{d}), where γnj​(r1,…,rn)≥0superscriptsubscript𝛾𝑛𝑗subscript𝑟1…subscript𝑟𝑛0\gamma\_{n}^{j}(r\_{1},\dots,r\_{n})\geq 0 is the number of units of the asset j𝑗j to be bought. So, the wealth will be distributed between d𝑑d assets in accordance with the fractions (or weights)

|  |  |  |
| --- | --- | --- |
|  | νn=(γnj​snjXn)j=1d∈Δ={z≥0:∑j=1dzj=1}.subscript𝜈𝑛superscriptsubscriptsuperscriptsubscript𝛾𝑛𝑗superscriptsubscript𝑠𝑛𝑗subscript𝑋𝑛𝑗1𝑑Δconditional-set𝑧0superscriptsubscript𝑗1𝑑subscript𝑧𝑗1\nu\_{n}=\left(\frac{\gamma\_{n}^{j}s\_{n}^{j}}{X\_{n}}\right)\_{j=1}^{d}\in\Delta=\left\{z\geq 0:\sum\_{j=1}^{d}z\_{j}=1\right\}. |  |

At time n+1𝑛1n+1 the wealth becomes

|  |  |  |
| --- | --- | --- |
|  | Xn+1=⟨γn,sn+1⟩=⟨νn,rn+1⟩.subscript𝑋𝑛1  subscript𝛾𝑛subscript𝑠𝑛1  subscript𝜈𝑛subscript𝑟𝑛1X\_{n+1}=\langle\gamma\_{n},s\_{n+1}\rangle=\langle\nu\_{n},r\_{n+1}\rangle. |  |

By ⟨a,b⟩

𝑎𝑏\langle a,b\rangle we denote the usual scalar product in ℝdsuperscriptℝ𝑑\mathbb{R}^{d}.

Our standing assumptions concern the investor utility function and the returns.

###### Assumption 1.

Investor’s utility function u:(0,∞)↦(0,∞):𝑢maps-to00u:(0,\infty)\mapsto(0,\infty) is non-decreasing and continuous.

###### Assumption 2.

The return vectors (rk1,…,rkd)superscriptsubscript𝑟𝑘1…superscriptsubscript𝑟𝑘𝑑(r\_{k}^{1},\dots,r\_{k}^{d}), k=1,…,n+1𝑘

1…𝑛1k=1,\dots,n+1 are independent and identically distributed.

Consider the single-period optimization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(ν)=𝖤​f​(ν,rn+1):=𝖤​u​(⟨ν,rn+1⟩)u​(rn+1∗)→maxν∈Δ,rn+1∗:=max1≤j≤d⁡rn+1j.formulae-sequence𝑈𝜈𝖤𝑓𝜈subscript𝑟𝑛1assign𝖤𝑢  𝜈subscript𝑟𝑛1𝑢superscriptsubscript𝑟𝑛1→subscript𝜈Δassignsuperscriptsubscript𝑟𝑛1subscript1𝑗𝑑subscriptsuperscript𝑟𝑗𝑛1U(\nu)=\mathsf{E}f(\nu,r\_{n+1}):=\mathsf{E}\frac{u(\langle\nu,r\_{n+1}\rangle)}{u\left(r\_{n+1}^{\*}\right)}\to\max\_{\nu\in\Delta},\qquad r\_{n+1}^{\*}:=\max\_{1\leq j\leq d}r^{j}\_{n+1}. |  | (2.1) |

The objective function U​(ν)𝑈𝜈U(\nu) of this problem equals to the expected ratio of the utility u𝑢u of some portfolio ν𝜈\nu to the utility of the best portfolio taken in hindsight, that is, under the assumption that the values rn+1subscript𝑟𝑛1r\_{n+1} are known.
In the latter case the investor simply takes an asset with the largest return. Since u𝑢u is non-decreasing, the relative utility f𝑓f takes values in (0,1]01(0,1]. The set ΔΔ\Delta is compact and the function U𝑈U is continuous, as follows from the continuity of ν↦f​(ν,r)maps-to𝜈𝑓𝜈𝑟\nu\mapsto f(\nu,r) and the dominated convergence theorem. Hence an optimal solution ν∗superscript𝜈\nu^{\*} of ([2.1](#S2.E1 "In 2. Problem formulation ‣ Relative utility bounds for empirically optimal portfolios")) exists.

It is natural to consider the empirical utility maximization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | U^n​(ν)=f^n​(ν,rn+1)=1n​∑k=1nu​(⟨ν,rk⟩)u​(rk∗)→maxν∈Δ.subscript^𝑈𝑛𝜈subscript^𝑓𝑛𝜈subscript𝑟𝑛11𝑛superscriptsubscript𝑘1𝑛𝑢  𝜈subscript𝑟𝑘𝑢subscriptsuperscript𝑟𝑘→subscript𝜈Δ\widehat{U}\_{n}(\nu)=\widehat{f}\_{n}(\nu,r\_{n+1})=\frac{1}{n}\sum\_{k=1}^{n}\frac{u(\langle\nu,r\_{k}\rangle)}{u(r^{\*}\_{k})}\to\max\_{\nu\in\Delta}. |  | (2.2) |

Clearly, this problem also has an optimal solution ν^nsubscript^𝜈𝑛\widehat{\nu}\_{n}.

Furthermore, consider the empirical process ν↦Gn​(ν)=U^n​(ν)−U​(ν).maps-to𝜈subscript𝐺𝑛𝜈subscript^𝑈𝑛𝜈𝑈𝜈\nu\mapsto G\_{n}(\nu)=\widehat{U}\_{n}(\nu)-U(\nu). Using the inequalities

|  |  |  |
| --- | --- | --- |
|  | U^n​(ν∗)≤U^n​(ν^n),U​(ν^n)≤U​(ν∗),formulae-sequencesubscript^𝑈𝑛superscript𝜈subscript^𝑈𝑛subscript^𝜈𝑛𝑈subscript^𝜈𝑛𝑈superscript𝜈\widehat{U}\_{n}(\nu^{\*})\leq\widehat{U}\_{n}(\widehat{\nu}\_{n}),\quad U(\widehat{\nu}\_{n})\leq U(\nu^{\*}), |  |

we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(ν∗)−U​(ν^n)≤U​(ν∗)−U^n​(ν∗)+U^n​(ν^n)−U​(ν^n)≤U​(ν∗)−U^n​(ν∗)+supν∈ΔGn​(ν),𝑈superscript𝜈𝑈subscript^𝜈𝑛𝑈superscript𝜈subscript^𝑈𝑛superscript𝜈subscript^𝑈𝑛subscript^𝜈𝑛𝑈subscript^𝜈𝑛𝑈superscript𝜈subscript^𝑈𝑛superscript𝜈subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈\displaystyle U(\nu^{\*})-U(\widehat{\nu}\_{n})\leq U(\nu^{\*})-\widehat{U}\_{n}(\nu^{\*})+\widehat{U}\_{n}(\widehat{\nu}\_{n})-U(\widehat{\nu}\_{n})\leq U(\nu^{\*})-\widehat{U}\_{n}(\nu^{\*})+\sup\_{\nu\in\Delta}G\_{n}(\nu), |  | (2.3) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | U^n​(ν^n)−U​(ν∗)≤U^n​(ν^n)−U​(ν^n)≤supν∈ΔGn​(ν).subscript^𝑈𝑛subscript^𝜈𝑛𝑈superscript𝜈subscript^𝑈𝑛subscript^𝜈𝑛𝑈subscript^𝜈𝑛subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈\displaystyle\widehat{U}\_{n}(\widehat{\nu}\_{n})-U(\nu^{\*})\leq\widehat{U}\_{n}(\widehat{\nu}\_{n})-U(\widehat{\nu}\_{n})\leq\sup\_{\nu\in\Delta}G\_{n}(\nu). |  | (2.4) |

Note, that when νnsubscript𝜈𝑛\nu\_{n} is random, by U​(νn)𝑈subscript𝜈𝑛U(\nu\_{n}) we mean the conditional expectation:

|  |  |  |
| --- | --- | --- |
|  | U(νn)=𝖤(f(νn,rn+1)|r1,…,rn)).U(\nu\_{n})=\mathsf{E}\left(f(\nu\_{n},r\_{n+1})|r\_{1},\dots,r\_{n}\right)). |  |

This quantity can be called the ‘‘true utility’’ of νnsubscript𝜈𝑛\nu\_{n} by analogy to the ‘‘true risk’’ in machine learning: see [[23](#bib.bib23)].

In learning theory the difference U​(ν∗)−U​(ν^n)𝑈superscript𝜈𝑈subscript^𝜈𝑛U(\nu^{\*})-U(\widehat{\nu}\_{n}) is called an estimation error: [[23](#bib.bib23)]. It describes the performance of the empirical utility maximizer ν^nsubscript^𝜈𝑛\widehat{\nu}\_{n}. The quantity U^n​(ν^n)subscript^𝑈𝑛subscript^𝜈𝑛\widehat{U}\_{n}(\widehat{\nu}\_{n}) can be regarded as a statistical estimate of the true utility U​(ν^n)𝑈subscript^𝜈𝑛U(\widehat{\nu}\_{n}) of ν^nsubscript^𝜈𝑛\widehat{\nu}\_{n}. This estimate is always optimistically biased:

|  |  |  |
| --- | --- | --- |
|  | 𝖤​U​(ν^n)≤U​(ν∗)=𝖤​U^n​(ν∗)≤𝖤​U^n​(ν^n).𝖤𝑈subscript^𝜈𝑛𝑈superscript𝜈𝖤subscript^𝑈𝑛superscript𝜈𝖤subscript^𝑈𝑛subscript^𝜈𝑛\mathsf{E}U(\widehat{\nu}\_{n})\leq U(\nu^{\*})=\mathsf{E}\widehat{U}\_{n}(\nu^{\*})\leq\mathsf{E}\widehat{U}\_{n}(\widehat{\nu}\_{n}). |  |

The difference 𝖤​U^n​(ν^n)−𝖤​U​(ν^n)≥0𝖤subscript^𝑈𝑛subscript^𝜈𝑛𝖤𝑈subscript^𝜈𝑛0\mathsf{E}\widehat{U}\_{n}(\widehat{\nu}\_{n})-\mathsf{E}U(\widehat{\nu}\_{n})\geq 0 is known as optimizer’s curse: [[26](#bib.bib26), [19](#bib.bib19)].

We see that the key quantity is the supremum of the empirical process Gnsubscript𝐺𝑛G\_{n}. By the strong law of large numbers Gn​(ν)→0→subscript𝐺𝑛𝜈0G\_{n}(\nu)\to 0 a.s. for a fixed ν𝜈\nu. Moreover, since the function ν↦u​(⟨ν,r⟩)/u​(r∗)maps-to𝜈𝑢

𝜈𝑟𝑢superscript𝑟\nu\mapsto u(\langle\nu,r\rangle)/u(r^{\*}) is continuous and bounded, the convergence is uniform:

|  |  |  |
| --- | --- | --- |
|  | supν∈Δ|Gn​(ν)|→0​a.s.,n→∞formulae-sequence→subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈0a.s.,→𝑛\sup\_{\nu\in\Delta}|G\_{n}(\nu)|\to 0\ \textrm{a.s.,}\quad n\to\infty |  |

by [[25](#bib.bib25), Theorem 7.53]. From ([2.3](#S2.E3 "In 2. Problem formulation ‣ Relative utility bounds for empirically optimal portfolios")), ([2.4](#S2.E4 "In 2. Problem formulation ‣ Relative utility bounds for empirically optimal portfolios")) we see that

|  |  |  |
| --- | --- | --- |
|  | U​(ν∗)≤lim infn→∞U​(ν^n),lim supn→∞U^n​(ν^n)≤U​(ν∗).formulae-sequence𝑈superscript𝜈subscriptlimit-infimum→𝑛𝑈subscript^𝜈𝑛subscriptlimit-supremum→𝑛subscript^𝑈𝑛subscript^𝜈𝑛𝑈superscript𝜈U(\nu^{\*})\leq\liminf\_{n\to\infty}U(\widehat{\nu}\_{n}),\quad\limsup\_{n\to\infty}\widehat{U}\_{n}(\widehat{\nu}\_{n})\leq U(\nu^{\*}). |  |

The reverse inequalities U​(ν∗)≥U​(ν^n)𝑈superscript𝜈𝑈subscript^𝜈𝑛U(\nu^{\*})\geq U(\widehat{\nu}\_{n}),

|  |  |  |
| --- | --- | --- |
|  | lim infn→∞U^n​(ν^n)≥lim infn→∞U^n​(ν∗)=U​(ν∗)subscriptlimit-infimum→𝑛subscript^𝑈𝑛subscript^𝜈𝑛subscriptlimit-infimum→𝑛subscript^𝑈𝑛superscript𝜈𝑈superscript𝜈\liminf\_{n\to\infty}\widehat{U}\_{n}(\widehat{\nu}\_{n})\geq\liminf\_{n\to\infty}\widehat{U}\_{n}(\nu^{\*})=U(\nu^{\*}) |  |

imply that U^n​(ν^n)→U​(ν∗),→subscript^𝑈𝑛subscript^𝜈𝑛𝑈superscript𝜈\widehat{U}\_{n}(\widehat{\nu}\_{n})\to U(\nu^{\*}), U​(ν^n)→U​(ν∗)→𝑈subscript^𝜈𝑛𝑈superscript𝜈U(\widehat{\nu}\_{n})\to U(\nu^{\*}), n→∞→𝑛n\to\infty a.s.
without further assumptions. Thus, the method of empirical utility maximization is consistent: see the definition in [[28](#bib.bib28), Chapter 3], where the convergence in probability is considered. In the next section we provide non-asymptotic bounds for Gnsubscript𝐺𝑛G\_{n}.

## 3. Utility bounds

Let us represent the supremum of the empirical process Gnsubscript𝐺𝑛G\_{n} in the form

|  |  |  |
| --- | --- | --- |
|  | supν∈ΔGn​(ν)=𝖤​supν∈ΔGn​(ν)+supν∈ΔGn​(ν)−𝖤​supν∈ΔGn​(ν).subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈𝖤subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈𝖤subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈\sup\_{\nu\in\Delta}G\_{n}(\nu)=\mathsf{E}\sup\_{\nu\in\Delta}G\_{n}(\nu)+\sup\_{\nu\in\Delta}G\_{n}(\nu)-\mathsf{E}\sup\_{\nu\in\Delta}G\_{n}(\nu). |  |

Put Rn=(r1,…,rn)subscript𝑅𝑛subscript𝑟1…subscript𝑟𝑛R\_{n}=(r\_{1},\dots,r\_{n}), Φ​(Rn)=supν∈ΔGn​(ν)Φsubscript𝑅𝑛subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈\Phi(R\_{n})=\sup\_{\nu\in\Delta}G\_{n}(\nu). We have

|  |  |  |
| --- | --- | --- |
|  | |Φ(r1,…,r~k,…,rn)−Φ(r1,…,rk,…,rn)|=|supν(1m∑i≠ku​(⟨ν,ri⟩)u​(ri∗)−U(ν)+1mu​(⟨ν,r~k⟩)u​(r~k∗))\displaystyle|\Phi(r\_{1},\dots,\tilde{r}\_{k},\dots,r\_{n})-\Phi(r\_{1},\dots,r\_{k},\dots,r\_{n})|=\left|\sup\_{\nu}\left(\frac{1}{m}\sum\_{i\neq k}\frac{u(\langle\nu,r\_{i}\rangle)}{u(r\_{i}^{\*})}-U(\nu)+\frac{1}{m}\frac{u(\langle\nu,\tilde{r}\_{k}\rangle)}{u(\tilde{r}\_{k}^{\*})}\right)\right. |  |
|  |  |  |
| --- | --- | --- |
|  | −supν(1m∑i≠ku​(⟨ν,ri⟩)u​(ri∗)−U(ν)+1mu​(⟨ν,rk⟩)u​(rk∗))|≤supν|1mu​(⟨ν,r~k⟩)u​(r~k∗)−1mu​(⟨ν,rk⟩)u​(rk∗)|≤1m.\displaystyle-\left.\sup\_{\nu}\left(\frac{1}{m}\sum\_{i\neq k}\frac{u(\langle\nu,r\_{i}\rangle)}{u(r\_{i}^{\*})}-U(\nu)+\frac{1}{m}\frac{u(\langle\nu,r\_{k}\rangle)}{u(r\_{k}^{\*})}\right)\right|\leq\sup\_{\nu}\left|\frac{1}{m}\frac{u(\langle\nu,\tilde{r}\_{k}\rangle)}{u(\tilde{r}\_{k}^{\*})}-\frac{1}{m}\frac{u(\langle\nu,r\_{k}\rangle)}{u(r\_{k}^{\*})}\right|\leq\frac{1}{m}. |  |

By the McDiarmid concentration inequality (see [[20](#bib.bib20), Theorem D.8]) this bounded differences property implies that

|  |  |  |
| --- | --- | --- |
|  | 𝖯​(supνGn​(ν)−𝖤​supνGn​(ν)≥ε)=𝖯​(Φ​(Rn)−𝖤​Φ​(Rn)≥ε)≤e−2​m​ε2,𝖯subscriptsupremum𝜈subscript𝐺𝑛𝜈𝖤subscriptsupremum𝜈subscript𝐺𝑛𝜈𝜀𝖯Φsubscript𝑅𝑛𝖤Φsubscript𝑅𝑛𝜀superscript𝑒2𝑚superscript𝜀2\mathsf{P}\left(\sup\_{\nu}G\_{n}(\nu)-\mathsf{E}\sup\_{\nu}G\_{n}(\nu)\geq\varepsilon\right)=\mathsf{P}(\Phi(R\_{n})-\mathsf{E}\Phi(R\_{n})\geq\varepsilon)\leq e^{-2m\varepsilon^{2}}, |  |

or, equivalently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖯​(supνGn​(ν)−𝖤​supνGn​(ν)≥12​n​ln⁡1δ)≤δ.𝖯subscriptsupremum𝜈subscript𝐺𝑛𝜈𝖤subscriptsupremum𝜈subscript𝐺𝑛𝜈12𝑛1𝛿𝛿\mathsf{P}\left(\sup\_{\nu}G\_{n}(\nu)-\mathsf{E}\sup\_{\nu}G\_{n}(\nu)\geq\sqrt{\frac{1}{2n}\ln\frac{1}{\delta}}\right)\leq\delta. |  | (3.1) |

For the difference U​(ν∗)−U^n​(ν∗)𝑈superscript𝜈subscript^𝑈𝑛superscript𝜈U(\nu^{\*})-\widehat{U}\_{n}(\nu^{\*}) we have a similar estimate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖯​(U​(ν∗)−U^n​(ν∗)≥12​n​ln⁡1δ)≤δ,𝖯𝑈superscript𝜈subscript^𝑈𝑛superscript𝜈12𝑛1𝛿𝛿\mathsf{P}\left(U(\nu^{\*})-\widehat{U}\_{n}(\nu^{\*})\geq\sqrt{\frac{1}{2n}\ln\frac{1}{\delta}}\right)\leq\delta, |  | (3.2) |

which follows from the Hoeffding inequality [[20](#bib.bib20), Theorem D.2]: a special case of the McDiarmid inequality.

Note, that to get the inequalities ([3.1](#S3.E1 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")), ([3.2](#S3.E2 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) we need not impose any growth assumptions on u𝑢u. This is an advantage of the relative utility. Let us formulate the obtained result more explicitly.

###### Theorem 1.

With probability at least 1−δ1𝛿1-\delta we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | U​(ν∗)−U​(ν^n)𝑈superscript𝜈𝑈subscript^𝜈𝑛\displaystyle U(\nu^{\*})-U(\widehat{\nu}\_{n}) | ≤𝖤​supν∈ΔGn​(ν)+2n​ln⁡2δ,absent𝖤subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈2𝑛2𝛿\displaystyle\leq\mathsf{E}\sup\_{\nu\in\Delta}G\_{n}(\nu)+\sqrt{\frac{2}{n}\ln\frac{2}{\delta}}, |  | (3.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | U^n​(ν^n)−U​(ν^n)subscript^𝑈𝑛subscript^𝜈𝑛𝑈subscript^𝜈𝑛\displaystyle\widehat{U}\_{n}(\widehat{\nu}\_{n})-U(\widehat{\nu}\_{n}) | ≤𝖤​supν∈ΔGn​(ν)+12​n​ln⁡1δ.absent𝖤subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈12𝑛1𝛿\displaystyle\leq\mathsf{E}\sup\_{\nu\in\Delta}G\_{n}(\nu)+\sqrt{\frac{1}{2n}\ln\frac{1}{\delta}}. |  | (3.4) |

The distinction in constants in the right-hand sides of ([3.3](#S3.E3 "In Theorem 1. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")), ([3.4](#S3.E4 "In Theorem 1. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) is due to the fact that we applied both inequalities ([3.1](#S3.E1 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")), ([3.2](#S3.E2 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) to ([2.3](#S2.E3 "In 2. Problem formulation ‣ Relative utility bounds for empirically optimal portfolios")) and only the first one to ([2.4](#S2.E4 "In 2. Problem formulation ‣ Relative utility bounds for empirically optimal portfolios")). In the first case the following argumentation is used: if

|  |  |  |
| --- | --- | --- |
|  | 𝖯​(ξi≥12​n​ln⁡1δ)≤δ,i=1,2,formulae-sequence𝖯subscript𝜉𝑖12𝑛1𝛿𝛿𝑖  12\mathsf{P}\left(\xi\_{i}\geq\sqrt{\frac{1}{2n}\ln\frac{1}{\delta}}\right)\leq\delta,\quad i=1,2, |  |

then

|  |  |  |
| --- | --- | --- |
|  | 𝖯​(ξ1+ξ2≥2​12​n​ln⁡2δ)≤∑i=12𝖯​(ξi≥12​n​ln⁡1δ/2)≤δ.𝖯subscript𝜉1subscript𝜉2212𝑛2𝛿superscriptsubscript𝑖12𝖯subscript𝜉𝑖12𝑛1𝛿2𝛿\mathsf{P}\left(\xi\_{1}+\xi\_{2}\geq 2\sqrt{\frac{1}{2n}\ln\frac{2}{\delta}}\right)\leq\sum\_{i=1}^{2}\mathsf{P}\left(\xi\_{i}\geq\sqrt{\frac{1}{2n}\ln\frac{1}{\delta/2}}\right)\leq\delta. |  |

Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios") contains the main result of the paper: the upper bounds for 𝖤​supν∈ΔGn​(ν)𝖤subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈\mathsf{E}\sup\_{\nu\in\Delta}G\_{n}(\nu).

###### Theorem 2.

Assume that the utility function u𝑢u is uniformly Hölder continuous on (0,∞)0(0,\infty):

|  |  |  |  |
| --- | --- | --- | --- |
|  | |u​(x)−u​(y)|≤K​|x−y|α𝑢𝑥𝑢𝑦𝐾superscript𝑥𝑦𝛼|u(x)-u(y)|\leq K|x-y|^{\alpha} |  | (3.5) |

with some α∈(0,1]𝛼01\alpha\in(0,1], K>0𝐾0K>0. Assume further that

|  |  |  |  |
| --- | --- | --- | --- |
|  | A:=supx>0xαu​(x)<∞.assign𝐴subscriptsupremum𝑥0superscript𝑥𝛼𝑢𝑥A:=\sup\_{x>0}\frac{x^{\alpha}}{u(x)}<\infty. |  | (3.6) |

Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝖤​supν∈ΔGn​(ν)𝖤subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈\displaystyle\mathsf{E}\sup\_{\nu\in\Delta}G\_{n}(\nu) | ≤2​A​K​2​ln⁡dn,α=1,formulae-sequenceabsent2𝐴𝐾2𝑑𝑛𝛼1\displaystyle\leq 2AK\sqrt{\frac{2\ln d}{n}},\quad\alpha=1, |  | (3.7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝖤​supν∈ΔGn​(ν)𝖤subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈\displaystyle\mathsf{E}\sup\_{\nu\in\Delta}G\_{n}(\nu) | ≤C​A​K​d−1α​n,α∈(0,1),formulae-sequenceabsent𝐶𝐴𝐾𝑑1𝛼𝑛𝛼01\displaystyle\leq CAK\sqrt{\frac{d-1}{\alpha n}},\quad\alpha\in(0,1), |  | (3.8) |

where C>0𝐶0C>0 is an absolute constant.

*Proof*. Let εisubscript𝜀𝑖\varepsilon\_{i}, i=1,…,n𝑖

1…𝑛i=1,\dots,n be independent Rademacher random variables: 𝖯​(εi=1)=𝖯​(εi=−1)=1/2𝖯subscript𝜀𝑖1𝖯subscript𝜀𝑖112\mathsf{P}(\varepsilon\_{i}=1)=\mathsf{P}(\varepsilon\_{i}=-1)=1/2, which are also independent from r1,…,rn

subscript𝑟1…subscript𝑟𝑛r\_{1},\dots,r\_{n}. Consider the empirical Rademacher complexity (see , e.g., [[20](#bib.bib20)])

|  |  |  |
| --- | --- | --- |
|  | ℛ^(ℱ∘Rn)=1n𝖤(supν∈Δ∑i=1nεiu​(⟨ν,ri⟩)u​(ri∗)|Rn)\widehat{\mathcal{R}}(\mathcal{F}\circ R\_{n})=\frac{1}{n}\mathsf{E}\left(\sup\_{\nu\in\Delta}\sum\_{i=1}^{n}\varepsilon\_{i}\frac{u(\langle\nu,r\_{i}\rangle)}{u(r\_{i}^{\*})}\biggl{|}R\_{n}\right) |  |

of the set of functions ℱ={r↦u​(⟨ν,r⟩)/u​(r∗):ν∈Δ}ℱconditional-setmaps-to𝑟𝑢

𝜈𝑟𝑢superscript𝑟𝜈Δ\mathcal{F}=\{r\mapsto u(\langle\nu,r\rangle)/u(r^{\*}):\nu\in\Delta\} with respect to the random sequence Rn=(r1,…,rn)subscript𝑅𝑛subscript𝑟1…subscript𝑟𝑛R\_{n}=(r\_{1},\dots,r\_{n}). In fact we compute the Rademacher complexity of the following set of n𝑛n-dimensional vectors:

|  |  |  |
| --- | --- | --- |
|  | ℱ∘Rn:={(u​(⟨ν,r1⟩)u​(r1∗),…,u(⟨ν,rn⟩u​(rn∗)):ν∈Δ}.\mathcal{F}\circ R\_{n}:=\left\{\left(\frac{u(\langle\nu,r\_{1}\rangle)}{u(r\_{1}^{\*})},\dots,\frac{u(\langle\nu,r\_{n}\rangle}{u(r\_{n}^{\*})}\right):\nu\in\Delta\right\}. |  |

For clarity recall (see [[23](#bib.bib23)]) that the Rademacher complexity of a set C⊂ℝn𝐶superscriptℝ𝑛C\subset\mathbb{R}^{n} is defined by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ^​(C)=1n​𝖤​supa∈C∑i=1nεi​ai.^ℛ𝐶1𝑛𝖤subscriptsupremum𝑎𝐶superscriptsubscript𝑖1𝑛subscript𝜀𝑖subscript𝑎𝑖\displaystyle\widehat{\mathcal{R}}(C)=\frac{1}{n}\mathsf{E}\sup\_{a\in C}\sum\_{i=1}^{n}\varepsilon\_{i}a\_{i}. |  | (3.9) |

Let us consider the case α=1𝛼1\alpha=1. The symmetrization argument ([[27](#bib.bib27), Lemma 7.4]) gives the bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤​supν∈ΔGn​(ν)≤2​𝖤​ℛ^​(ℱ∘Rn).𝖤subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈2𝖤^ℛℱsubscript𝑅𝑛\mathsf{E}\sup\_{\nu\in\Delta}G\_{n}(\nu)\leq 2\mathsf{E}\widehat{\mathcal{R}}(\mathcal{F}\circ R\_{n}). |  | (3.10) |

For Ψ​(x,r)=u​(x)/u​(r∗)Ψ𝑥𝑟𝑢𝑥𝑢superscript𝑟\Psi(x,r)=u(x)/u(r^{\*}), r∗=max1≤i≤d⁡risuperscript𝑟subscript1𝑖𝑑superscript𝑟𝑖r^{\*}=\max\_{1\leq i\leq d}r^{i} we have

|  |  |  |
| --- | --- | --- |
|  | |Ψ​(x,r)−Ψ​(y,r)|≤Ku​(r∗)​|x−y|.Ψ𝑥𝑟Ψ𝑦𝑟𝐾𝑢superscript𝑟𝑥𝑦|\Psi(x,r)-\Psi(y,r)|\leq\frac{K}{u(r^{\*})}|x-y|. |  |

Literally following the proof of Talagrand’s contraction lemma, given in [[20](#bib.bib20), Lemma 5.7], we get the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ^​(ℱ∘Rn)^ℛℱsubscript𝑅𝑛\displaystyle\widehat{\mathcal{R}}(\mathcal{F}\circ R\_{n}) | =1n​𝖤​(supν∈Δ∑i=1nεi​Ψ​(⟨ν,ri⟩,ri)|Rn)≤Kn​𝖤​(supν∈Δ∑i=1nεi​⟨ν,ri⟩ri∗|Rn)absent1𝑛𝖤conditionalsubscriptsupremum𝜈Δsuperscriptsubscript𝑖1𝑛subscript𝜀𝑖Ψ  𝜈subscript𝑟𝑖 subscript𝑟𝑖subscript𝑅𝑛𝐾𝑛𝖤conditionalsubscriptsupremum𝜈Δsuperscriptsubscript𝑖1𝑛subscript𝜀𝑖  𝜈subscript𝑟𝑖 superscriptsubscript𝑟𝑖subscript𝑅𝑛\displaystyle=\frac{1}{n}\mathsf{E}\left(\sup\_{\nu\in\Delta}\sum\_{i=1}^{n}\varepsilon\_{i}\Psi(\langle\nu,r\_{i}\rangle,r\_{i})\biggr{|}R\_{n}\right)\leq\frac{K}{n}\mathsf{E}\left(\sup\_{\nu\in\Delta}\sum\_{i=1}^{n}\varepsilon\_{i}\frac{\langle\nu,r\_{i}\rangle}{r\_{i}^{\*}}\biggr{|}R\_{n}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =K​ℛ^​(ℋ∘Rn),ℋ:={r↦⟨ν,r⟩/r∗:ν∈Δ}.formulae-sequenceabsent𝐾^ℛℋsubscript𝑅𝑛assignℋconditional-setmaps-to𝑟  𝜈𝑟 superscript𝑟𝜈Δ\displaystyle=K\widehat{\mathcal{R}}(\mathcal{H}\circ R\_{n}),\quad\mathcal{H}:=\{r\mapsto\langle\nu,r\rangle/r^{\*}:\nu\in\Delta\}. |  | (3.11) |

Note, that the only difference with the Talagrand contraction lemma is that the Lipschitz constant for x↦Ψ​(x,r)maps-to𝑥Ψ𝑥𝑟x\mapsto\Psi(x,r) depends on r𝑟r.

The Rademacher complexity of the set ℋℋ\mathcal{H} equals to the Rademacher complexity of its extreme points (as follows from [[23](#bib.bib23), Lemma 26.7]), corresponding to the vectors of the standard basis: ν∈{e1,…,ed}𝜈subscript𝑒1…subscript𝑒𝑑\nu\in\{e\_{1},\dots,e\_{d}\}, ei=(δi​j)j=1dsubscript𝑒𝑖superscriptsubscriptsubscript𝛿𝑖𝑗𝑗1𝑑e\_{i}=(\delta\_{ij})\_{j=1}^{d}, where δi​jsubscript𝛿𝑖𝑗\delta\_{ij} is Kronecker symbol. Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ^​(ℋ∘Rn)=ℛ^​(r1u​(r∗),…,rdu​(r∗)).^ℛℋsubscript𝑅𝑛^ℛsuperscript𝑟1𝑢superscript𝑟…superscript𝑟𝑑𝑢superscript𝑟\widehat{\mathcal{R}}(\mathcal{H}\circ R\_{n})=\widehat{\mathcal{R}}\left(\frac{r^{1}}{u(r^{\*})},\dots,\frac{r^{d}}{u(r^{\*})}\right). |  | (3.12) |

Here rj/u(r∗)=(r1j/u(r1∗),…,(rnj/u(rn∗))∈ℝnr^{j}/u(r^{\*})=(r^{j}\_{1}/u(r^{\*}\_{1}),\dots,(r^{j}\_{n}/u(r^{\*}\_{n}))\in\mathbb{R}^{n} are the normalized trajectories of the returns, and the right-hand side of ([3.12](#S3.E12 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) is computed in accordance with ([3.9](#S3.E9 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")). The Rademacher complexity of a finite set of vectors can be estimated by Massart’s lemma (see [[20](#bib.bib20), Theorem 3.7]). Applying this lemma to the right-hand side of ([3.12](#S3.E12 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")), we get the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ^​(r1u​(r∗),…,rdu​(r∗))≤An​2​ln⁡d,^ℛsuperscript𝑟1𝑢superscript𝑟…superscript𝑟𝑑𝑢superscript𝑟𝐴𝑛2𝑑\widehat{\mathcal{R}}\left(\frac{r^{1}}{u(r^{\*})},\dots,\frac{r^{d}}{u(r^{\*})}\right)\leq\frac{A}{\sqrt{n}}\sqrt{2\ln d}, |  | (3.13) |

since by ([3.6](#S3.E6 "In Theorem 2. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")),

|  |  |  |
| --- | --- | --- |
|  | ‖rj/u​(r∗)‖2=∑k=1n(rkju​(rk∗))2≤A​n,subscriptnormsuperscript𝑟𝑗𝑢superscript𝑟2superscriptsubscript𝑘1𝑛superscriptsubscriptsuperscript𝑟𝑗𝑘𝑢subscriptsuperscript𝑟𝑘2𝐴𝑛\|r^{j}/u(r^{\*})\|\_{2}=\sqrt{\sum\_{k=1}^{n}\left(\frac{r^{j}\_{k}}{u(r^{\*}\_{k})}\right)^{2}}\leq A\sqrt{n}, |  |

where ‖a‖2=∑i=1nai2subscriptnorm𝑎2superscriptsubscript𝑖1𝑛superscriptsubscript𝑎𝑖2\|a\|\_{2}=\sqrt{\sum\_{i=1}^{n}a\_{i}^{2}} is the l2subscript𝑙2l\_{2}-norm.
The inequality ([3.7](#S3.E7 "In Theorem 2. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) now follows from ([3.10](#S3.E10 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) – ([3.13](#S3.E13 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")).

In the case α<1𝛼1\alpha<1 first note that for fixed Rnsubscript𝑅𝑛R\_{n} the process

|  |  |  |
| --- | --- | --- |
|  | Zn​(ν)=1n​∑k=1nεk​u​(⟨ν,rk⟩)u​(rk∗)subscript𝑍𝑛𝜈1𝑛superscriptsubscript𝑘1𝑛subscript𝜀𝑘𝑢  𝜈subscript𝑟𝑘𝑢superscriptsubscript𝑟𝑘Z\_{n}(\nu)=\frac{1}{n}\sum\_{k=1}^{n}\varepsilon\_{k}\frac{u(\langle\nu,r\_{k}\rangle)}{u(r\_{k}^{\*})} |  |

is subgaussian (see [[27](#bib.bib27), Definition 5.20]) with respect to the data dependent pseudometric

|  |  |  |
| --- | --- | --- |
|  | ρ​(ν,ν′)=1n​(∑k=1n(u​(⟨ν,rk⟩)u​(rk∗)−u​(⟨ν′,rk⟩)u​(rk∗))2)1/2,𝜌𝜈superscript𝜈′1𝑛superscriptsuperscriptsubscript𝑘1𝑛superscript𝑢  𝜈subscript𝑟𝑘𝑢superscriptsubscript𝑟𝑘𝑢  superscript𝜈′subscript𝑟𝑘𝑢superscriptsubscript𝑟𝑘212\rho(\nu,\nu^{\prime})=\frac{1}{n}\left(\sum\_{k=1}^{n}\left(\frac{u(\langle\nu,r\_{k}\rangle)}{u(r\_{k}^{\*})}-\frac{u(\langle\nu^{\prime},r\_{k}\rangle)}{u(r\_{k}^{\*})}\right)^{2}\right)^{1/2}, |  |

defined on ΔΔ\Delta. That is,

|  |  |  |
| --- | --- | --- |
|  | 𝖤​(eλ​(Zn​(ν)−Zn​(ν′))|Rn)=∏i=1n𝖤​[exp⁡(λn​εi​u​(⟨ν,rk⟩)−u​(⟨ν′,rk⟩)u​(rk∗))|Rn]≤eλ2​ρ2​(ν,ν′)/2.𝖤conditionalsuperscript𝑒𝜆subscript𝑍𝑛𝜈subscript𝑍𝑛superscript𝜈′subscript𝑅𝑛superscriptsubscriptproduct𝑖1𝑛𝖤delimited-[]conditional𝜆𝑛subscript𝜀𝑖𝑢  𝜈subscript𝑟𝑘𝑢  superscript𝜈′subscript𝑟𝑘𝑢superscriptsubscript𝑟𝑘subscript𝑅𝑛superscript𝑒superscript𝜆2superscript𝜌2𝜈superscript𝜈′2\displaystyle\mathsf{E}\left(e^{\lambda(Z\_{n}(\nu)-Z\_{n}(\nu^{\prime}))}\biggr{|}R\_{n}\right)=\prod\_{i=1}^{n}\mathsf{E}\left[\exp\left(\frac{\lambda}{n}\varepsilon\_{i}\frac{u(\langle\nu,r\_{k}\rangle)-u(\langle\nu^{\prime},r\_{k}\rangle)}{u(r\_{k}^{\*})}\right)\biggr{|}R\_{n}\right]\leq e^{\lambda^{2}\rho^{2}(\nu,\nu^{\prime})/2}. |  |

Here we used an elementary inequality 𝖤​eλ​εi​a≤eλ2​a2/2𝖤superscript𝑒𝜆subscript𝜀𝑖𝑎superscript𝑒superscript𝜆2superscript𝑎22\mathsf{E}e^{\lambda\varepsilon\_{i}a}\leq e^{\lambda^{2}a^{2}/2}: [[29](#bib.bib29), Example 2.3].

A set N⊂Δ𝑁ΔN\subset\Delta is called ϵitalic-ϵ\epsilon-dispersed if ρ​(ν,ν′)≥ϵ𝜌𝜈superscript𝜈′italic-ϵ\rho(\nu,\nu^{\prime})\geq\epsilon for ν,ν′∈N

𝜈superscript𝜈′
𝑁\nu,\nu^{\prime}\in N with ν≠ν′𝜈superscript𝜈′\nu\neq\nu^{\prime}. Let D​(Δ,ρ,ϵ)𝐷Δ𝜌italic-ϵD(\Delta,\rho,\epsilon) be the ϵitalic-ϵ\epsilon-packing number of (Δ,ρ)Δ𝜌(\Delta,\rho):

|  |  |  |
| --- | --- | --- |
|  | D(Δ,ρ,ϵ)=sup{|N|:N is an ϵ-dispersed}.D(\Delta,\rho,\epsilon)=\sup\{|N|:N\textrm{ is an }\epsilon\textrm{-dispersed}\}. |  |

Here |N|𝑁|N| is the cardinality of N𝑁N. The conditional expectation of the supremum of Znsubscript𝑍𝑛Z\_{n} is bounded by the Dudley entropy integral ([[5](#bib.bib5), Corollary 13.2]):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ^​(ℱ∘Rn)=𝖤​(supν∈ΔZn​(ν)|Rn)≤12​∫0d/2ln⁡D​(Δ,ρ,ϵ)​𝑑ϵ,^ℛℱsubscript𝑅𝑛𝖤conditionalsubscriptsupremum𝜈Δsubscript𝑍𝑛𝜈subscript𝑅𝑛12superscriptsubscript0𝑑2𝐷Δ𝜌italic-ϵdifferential-ditalic-ϵ\widehat{\mathcal{R}}(\mathcal{F}\circ R\_{n})=\mathsf{E}\left(\sup\_{\nu\in\Delta}Z\_{n}(\nu)|R\_{n}\right)\leq 12\int\_{0}^{d/2}\sqrt{\ln D(\Delta,\rho,\epsilon)}\,d\epsilon, |  | (3.14) |

where d𝑑d is the diameter of ΔΔ\Delta.

Conditions ([3.5](#S3.E5 "In Theorem 2. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")), ([3.6](#S3.E6 "In Theorem 2. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) imply that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(ν,ν′)𝜌𝜈superscript𝜈′\displaystyle\rho(\nu,\nu^{\prime}) | ≤Kn​(∑k=1n|⟨ν−ν′,rk⟩|2​αu2​(rk∗))1/2≤Kn​(∑k=1n(rk∗)2​α​‖ν−ν′‖12​αu2​(rk∗))1/2absent𝐾𝑛superscriptsuperscriptsubscript𝑘1𝑛superscript  𝜈superscript𝜈′subscript𝑟𝑘2𝛼superscript𝑢2superscriptsubscript𝑟𝑘12𝐾𝑛superscriptsuperscriptsubscript𝑘1𝑛superscriptsuperscriptsubscript𝑟𝑘2𝛼superscriptsubscriptnorm𝜈superscript𝜈′12𝛼superscript𝑢2superscriptsubscript𝑟𝑘12\displaystyle\leq\frac{K}{n}\left(\sum\_{k=1}^{n}\frac{|\langle\nu-\nu^{\prime},r\_{k}\rangle|^{2\alpha}}{u^{2}(r\_{k}^{\*})}\right)^{1/2}\leq\frac{K}{n}\left(\sum\_{k=1}^{n}\frac{(r\_{k}^{\*})^{2\alpha}\|\nu-\nu^{\prime}\|\_{1}^{2\alpha}}{u^{2}(r\_{k}^{\*})}\right)^{1/2} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤K​An​‖ν−ν′‖1α,absent𝐾𝐴𝑛superscriptsubscriptnorm𝜈superscript𝜈′1𝛼\displaystyle\leq\frac{KA}{\sqrt{n}}\|\nu-\nu^{\prime}\|\_{1}^{\alpha},\quad |  | (3.15) |

where ‖a‖1=∑j=1d|aj|subscriptnorm𝑎1superscriptsubscript𝑗1𝑑subscript𝑎𝑗\|a\|\_{1}=\sum\_{j=1}^{d}|a\_{j}| is the the l1subscript𝑙1l\_{1}-norm.
For the ϵitalic-ϵ\epsilon-packing number of ΔΔ\Delta with the metric, induced by ∥⋅∥1\|\cdot\|\_{1}, we have the inequality
D(Δ,∥⋅∥1,ϵ)≤(5/ϵ)d−1D(\Delta,\|\cdot\|\_{1},\epsilon)\leq\left(5/\epsilon\right)^{d-1}
(see [[9](#bib.bib9), Proposition C.1]). From ([3.15](#S3.E15 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) it follows that if ρ​(ν,ν′)≥ϵ𝜌𝜈superscript𝜈′italic-ϵ\rho(\nu,\nu^{\prime})\geq\epsilon then

|  |  |  |
| --- | --- | --- |
|  | ‖ν−ν′‖1≥(n​εK​A)1/α.subscriptnorm𝜈superscript𝜈′1superscript𝑛𝜀𝐾𝐴1𝛼\|\nu-\nu^{\prime}\|\_{1}\geq\left(\frac{\sqrt{n}\varepsilon}{KA}\right)^{1/\alpha}. |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | D(Δ,ρ,ϵ)≤D(Δ,∥⋅∥1,(n​ϵK​A)1/α)≤5d−1(K​An​ϵ)(d−1)/α.D(\Delta,\rho,\epsilon)\leq D\left(\Delta,\|\cdot\|\_{1},\left(\frac{\sqrt{n}\epsilon}{KA}\right)^{1/\alpha}\right)\leq 5^{d-1}\left(\frac{KA}{\sqrt{n}\epsilon}\right)^{(d-1)/\alpha}. |  | (3.16) |

Furthermore, by ([3.15](#S3.E15 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) the diameter of ΔΔ\Delta with respect to ρ𝜌\rho is estimated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d≤2α​K​An,𝑑superscript2𝛼𝐾𝐴𝑛d\leq 2^{\alpha}\frac{KA}{\sqrt{n}}, |  | (3.17) |

since ‖ν−ν′‖1≤‖ν‖1+‖ν′‖1≤2subscriptnorm𝜈superscript𝜈′1subscriptnorm𝜈1subscriptnormsuperscript𝜈′12\|\nu-\nu^{\prime}\|\_{1}\leq\|\nu\|\_{1}+\|\nu^{\prime}\|\_{1}\leq 2.
Let us substitute the estimates ([3.16](#S3.E16 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")), ([3.17](#S3.E17 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) into ([3.14](#S3.E14 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")), and perform the change of variables z=n​ε/(2α−1​K​A)𝑧𝑛𝜀superscript2𝛼1𝐾𝐴z=\sqrt{n}\varepsilon/(2^{\alpha-1}KA):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ^​(ℱ∘Sn)^ℛℱsubscript𝑆𝑛\displaystyle\widehat{\mathcal{R}}(\mathcal{F}\circ S\_{n}) | ≤12​∫02α−1​K​A/nln⁡(5d−1​(K​An​ϵ)(d−1)/α)​𝑑ϵabsent12superscriptsubscript0superscript2𝛼1𝐾𝐴𝑛superscript5𝑑1superscript𝐾𝐴𝑛italic-ϵ𝑑1𝛼differential-ditalic-ϵ\displaystyle\leq 12\int\_{0}^{2^{\alpha-1}KA/\sqrt{n}}\sqrt{\ln\left(5^{d-1}\left(\frac{KA}{\sqrt{n}\epsilon}\right)^{(d-1)/\alpha}\right)}\,d\epsilon |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​d−1α​∫02α−1​K​A/nln⁡(5α​K​An​ϵ)​𝑑ϵabsent12𝑑1𝛼superscriptsubscript0superscript2𝛼1𝐾𝐴𝑛superscript5𝛼𝐾𝐴𝑛italic-ϵdifferential-ditalic-ϵ\displaystyle=12\sqrt{\frac{d-1}{\alpha}}\int\_{0}^{2^{\alpha-1}KA/\sqrt{n}}\sqrt{\ln\left(5^{\alpha}\frac{KA}{\sqrt{n}\epsilon}\right)}\,d\epsilon |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​d−1α​2α−1​K​An​∫01ln⁡5α2α−1​z​𝑑z≤C1​K​A​d−1α​n,absent12𝑑1𝛼superscript2𝛼1𝐾𝐴𝑛superscriptsubscript01superscript5𝛼superscript2𝛼1𝑧differential-d𝑧subscript𝐶1𝐾𝐴𝑑1𝛼𝑛\displaystyle=12\sqrt{\frac{d-1}{\alpha}}\frac{2^{\alpha-1}KA}{\sqrt{n}}\int\_{0}^{1}\sqrt{\ln\frac{5^{\alpha}}{2^{\alpha-1}z}}\,dz\leq C\_{1}KA\sqrt{\frac{d-1}{\alpha n}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | C1subscript𝐶1\displaystyle C\_{1} | =12​∫01ln⁡5z​𝑑z.absent12superscriptsubscript015𝑧differential-d𝑧\displaystyle=12\int\_{0}^{1}\sqrt{\ln\frac{5}{z}}\,dz. |  |

Together with ([3.10](#S3.E10 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) this completes the proof (C=2​C1𝐶2subscript𝐶1C=2C\_{1}). ∎

In a most natural way condition ([3.6](#S3.E6 "In Theorem 2. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) is satisfied by the power utility function u​(x)=xα𝑢𝑥superscript𝑥𝛼u(x)=x^{\alpha}, α∈(0,1]𝛼01\alpha\in(0,1]. This function also satisfies ([3.5](#S3.E5 "In Theorem 2. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) with K=1𝐾1K=1, as easily follows from the inequality ([[12](#bib.bib12), Appendix A, Lemma 5.1])

|  |  |  |
| --- | --- | --- |
|  | (x+y)α≤xα+yα,x,y>0.formulae-sequencesuperscript𝑥𝑦𝛼  superscript𝑥𝛼superscript𝑦𝛼𝑥𝑦0(x+y)^{\alpha}\leq x^{\alpha}+y^{\alpha},\quad x,y>0. |  |

For u​(x)=xα𝑢𝑥superscript𝑥𝛼u(x)=x^{\alpha} the problem ([2.1](#S2.E1 "In 2. Problem formulation ‣ Relative utility bounds for empirically optimal portfolios")) reduces to the optimization of the ordinary power utility function after the price normalization:

|  |  |  |
| --- | --- | --- |
|  | U​(ν)=𝖤​⟨ν,rn+1/rn+1∗⟩α.𝑈𝜈𝖤superscript  𝜈subscript𝑟𝑛1superscriptsubscript𝑟𝑛1 𝛼U(\nu)=\mathsf{E}\langle\nu,r\_{n+1}/r\_{n+1}^{\*}\rangle^{\alpha}. |  |

The power utility is natural in one more respect: the relative utility ([3.1](#S3.E1 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) in this case is independent of investor’s wealth x𝑥x:

|  |  |  |
| --- | --- | --- |
|  | 𝖤​u​(x​⟨ν,rn+1⟩)u​(x​rn+1∗)=𝖤​⟨ν,rn+1/rn+1∗⟩α.𝖤𝑢𝑥  𝜈subscript𝑟𝑛1𝑢𝑥superscriptsubscript𝑟𝑛1𝖤superscript  𝜈subscript𝑟𝑛1superscriptsubscript𝑟𝑛1 𝛼\mathsf{E}\frac{u(x\langle\nu,r\_{n+1}\rangle)}{u\left(xr\_{n+1}^{\*}\right)}=\mathsf{E}\langle\nu,r\_{n+1}/r\_{n+1}^{\*}\rangle^{\alpha}. |  |

This means that one can consider the problems ([2.1](#S2.E1 "In 2. Problem formulation ‣ Relative utility bounds for empirically optimal portfolios")), ([2.2](#S2.E2 "In 2. Problem formulation ‣ Relative utility bounds for empirically optimal portfolios")) dynamically in an online manner. At each step the investor will act myopically similar to the case of the ordinary logarithmic utility.

###### Remark 1.

Under additional assumptions condition ([3.6](#S3.E6 "In Theorem 2. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) on the utility function can be relaxed. In fact we need only the upper bound for rk∗/u​(rk∗)superscriptsubscript𝑟𝑘𝑢superscriptsubscript𝑟𝑘r\_{k}^{\*}/u(r\_{k}^{\*}). Thus, if there exists a riskless asset (cash) with rk=1subscript𝑟𝑘1r\_{k}=1, then the supremum in ([3.6](#S3.E6 "In Theorem 2. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) can be taken over [1,∞)1[1,\infty). Furthermore, if the returns are bounded, then the supremum can be taken over a finite interval. In this case usually it is enough to consider the Lipschitz case α=1𝛼1\alpha=1.

###### Remark 2.

Theorems [1](#Thmtheorem1 "Theorem 1. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios"), [2](#Thmtheorem2 "Theorem 2. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios") give high probability error bounds. From ([2.3](#S2.E3 "In 2. Problem formulation ‣ Relative utility bounds for empirically optimal portfolios")), ([2.4](#S2.E4 "In 2. Problem formulation ‣ Relative utility bounds for empirically optimal portfolios")) it follows that

|  |  |  |
| --- | --- | --- |
|  | max⁡{U​(ν∗)−𝖤​U​(ν^n),𝖤​(U^n​(ν^n)−U​(ν^n))}≤𝖤​supν∈ΔGn​(ν),𝑈superscript𝜈𝖤𝑈subscript^𝜈𝑛𝖤subscript^𝑈𝑛subscript^𝜈𝑛𝑈subscript^𝜈𝑛𝖤subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈\displaystyle\max\{U(\nu^{\*})-\mathsf{E}U(\widehat{\nu}\_{n}),\mathsf{E}(\widehat{U}\_{n}(\widehat{\nu}\_{n})-U(\widehat{\nu}\_{n}))\}\leq\mathsf{E}\sup\_{\nu\in\Delta}G\_{n}(\nu), |  |

Thus, Theorem 2 provides also error bounds in expectation.

###### Remark 3.

The obtained error bounds are of order n−1/2superscript𝑛12n^{-1/2}. In general the main assumption, which allows to obtain O​(1/n)𝑂1𝑛O(1/n) bounds, is the strong concavity of U𝑈U: [[24](#bib.bib24), [21](#bib.bib21)]. However, such assumption requires additional conditions on the returns risubscript𝑟𝑖r\_{i}, which we want to avoid in the present paper.

## 4. Stochastic exponentiated gradient algorithm

In this section we additionally assume that the utility function u𝑢u is concave. Recall that the subdifferential of −u𝑢-u at any point y∈(0,∞)𝑦0y\in(0,\infty) is an interval:

|  |  |  |
| --- | --- | --- |
|  | ∂(−u)​(y)=[−D−​u​(y),−D+​u​(y)],𝑢𝑦subscript𝐷𝑢𝑦subscript𝐷𝑢𝑦\partial(-u)(y)=[-D\_{-}u(y),-D\_{+}u(y)], |  |

where D−​u​(y)subscript𝐷𝑢𝑦D\_{-}u(y) and D+​u​(y)subscript𝐷𝑢𝑦D\_{+}u(y) are the left and right derivatives: see [[16](#bib.bib16), Chap. I]. We have D−​u​(y)≥D+​u​(y)≥0subscript𝐷𝑢𝑦subscript𝐷𝑢𝑦0D\_{-}u(y)\geq D\_{+}u(y)\geq 0, as u𝑢u is non-decreasing.

We use the exponentiated gradient (EG) algorithm of [[18](#bib.bib18)] to solve the empirical utility maximization problem ([2.2](#S2.E2 "In 2. Problem formulation ‣ Relative utility bounds for empirically optimal portfolios")). Consider the empirical distribution generated by the sample (r1,…,rn)subscript𝑟1…subscript𝑟𝑛(r\_{1},\dots,r\_{n}), and a random variable r^^𝑟\widehat{r} with this distribution:

|  |  |  |
| --- | --- | --- |
|  | 𝖯^​(r^=rk)=1n,k=1,…,n.formulae-sequence^𝖯^𝑟subscript𝑟𝑘1𝑛𝑘  1…𝑛\widehat{\mathsf{P}}(\widehat{r}=r\_{k})=\frac{1}{n},\quad k=1,\dots,n. |  |

Put

|  |  |  |
| --- | --- | --- |
|  | r¯n=min1≤k≤n⁡min1≤i≤d⁡rki,r¯n=max1≤k≤n⁡max1≤i≤d⁡rkiformulae-sequencesubscript¯𝑟𝑛subscript1𝑘𝑛subscript1𝑖𝑑superscriptsubscript𝑟𝑘𝑖subscript¯𝑟𝑛subscript1𝑘𝑛subscript1𝑖𝑑superscriptsubscript𝑟𝑘𝑖\underline{r}\_{n}=\min\_{1\leq k\leq n}\min\_{1\leq i\leq d}r\_{k}^{i},\quad\overline{r}\_{n}=\max\_{1\leq k\leq n}\max\_{1\leq i\leq d}r\_{k}^{i} |  |

and consider the convex functions

|  |  |  |
| --- | --- | --- |
|  | ν↦fj​(ν)=1−u​(⟨ν,r^j⟩)u​(r^j∗):Δ↦[0,1].:maps-to𝜈subscript𝑓𝑗𝜈1𝑢  𝜈subscript^𝑟𝑗𝑢superscriptsubscript^𝑟𝑗maps-toΔ01\nu\mapsto f\_{j}(\nu)=1-\frac{u(\langle\nu,\widehat{r}\_{j}\rangle)}{u(\widehat{r}\_{j}^{\*})}:\Delta\mapsto[0,1]. |  |

From the description of their subdifferentials:

|  |  |  |
| --- | --- | --- |
|  | ∂fj​(ν)={γu​(r^j∗)​r^j:γ∈[−D−​u​(⟨ν,r^j⟩),−D+​u​(⟨ν,r^j⟩)]}subscript𝑓𝑗𝜈conditional-set𝛾𝑢superscriptsubscript^𝑟𝑗subscript^𝑟𝑗𝛾subscript𝐷𝑢  𝜈subscript^𝑟𝑗subscript𝐷𝑢  𝜈subscript^𝑟𝑗\partial f\_{j}(\nu)=\left\{\frac{\gamma}{u(\widehat{r}\_{j}^{\*})}\widehat{r}\_{j}:\gamma\in[-D\_{-}u(\langle\nu,\widehat{r}\_{j}\rangle),-D\_{+}u(\langle\nu,\widehat{r}\_{j}\rangle)]\right\} |  |

and the inequalities 0<r¯n≤⟨ν,r^j⟩0subscript¯𝑟𝑛

𝜈subscript^𝑟𝑗0<\underline{r}\_{n}\leq\langle\nu,\widehat{r}\_{j}\rangle, j=1,…,n,𝑗

1…𝑛j=1,\dots,n, we see that the absolute values of the subgradient components are bounded by the constant

|  |  |  |
| --- | --- | --- |
|  | Ln=D−​u​(r¯n)⋅maxr¯n≤x≤r¯n⁡xu​(x)=D−​u​(r¯n)⋅r¯nu​(r¯n).subscript𝐿𝑛⋅subscript𝐷𝑢subscript¯𝑟𝑛subscriptsubscript¯𝑟𝑛𝑥subscript¯𝑟𝑛𝑥𝑢𝑥⋅subscript𝐷𝑢subscript¯𝑟𝑛subscript¯𝑟𝑛𝑢subscript¯𝑟𝑛L\_{n}=D\_{-}u(\underline{r}\_{n})\cdot\max\_{\underline{r}\_{n}\leq x\leq\overline{r}\_{n}}\frac{x}{u(x)}=D\_{-}u(\underline{r}\_{n})\cdot\frac{\overline{r}\_{n}}{u(\overline{r}\_{n})}. |  |

Indeed, u​(x)/x𝑢𝑥𝑥u(x)/x is non-increasing: [[16](#bib.bib16), Proposition 1.1.4], and the subdifferential mapping is monotone:

|  |  |  |
| --- | --- | --- |
|  | γ1≤γ2wheneverγi∈∂(−u)​(yi),0<y1<y2,formulae-sequencesubscript𝛾1  subscript𝛾2wheneverformulae-sequencesubscript𝛾𝑖𝑢subscript𝑦𝑖0subscript𝑦1subscript𝑦2\gamma\_{1}\leq\gamma\_{2}\quad\textrm{whenever}\quad\gamma\_{i}\in\partial(-u)(y\_{i}),\quad 0<y\_{1}<y\_{2}, |  |

see [[16](#bib.bib16), Theorem 4.2.1]. It follows that the functions fjsubscript𝑓𝑗f\_{j} are Lnsubscript𝐿𝑛L\_{n}-Lipschitz with respect to l1subscript𝑙1l\_{1}-norm: see [[22](#bib.bib22), Lemma 2.6].

Apply the exponentiated gradient algorithm to f1,…,fm

subscript𝑓1…subscript𝑓𝑚f\_{1},\dots,f\_{m}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ν0isuperscriptsubscript𝜈0𝑖\displaystyle\nu\_{0}^{i} | =1/d,i=1,…,d,formulae-sequenceabsent1𝑑𝑖  1…𝑑\displaystyle=1/d,\quad i=1,\dots,d, |  | (4.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ajisuperscriptsubscript𝑎𝑗𝑖\displaystyle a\_{j}^{i} | =νj−1i​exp⁡(η​D−​u​(⟨νj−1,r^j⟩)u​(r^j∗)​r^ji),νji=aji∑l=1dajl,formulae-sequenceabsentsuperscriptsubscript𝜈𝑗1𝑖𝜂subscript𝐷𝑢  subscript𝜈𝑗1subscript^𝑟𝑗𝑢superscriptsubscript^𝑟𝑗superscriptsubscript^𝑟𝑗𝑖superscriptsubscript𝜈𝑗𝑖superscriptsubscript𝑎𝑗𝑖superscriptsubscript𝑙1𝑑superscriptsubscript𝑎𝑗𝑙\displaystyle=\nu\_{j-1}^{i}\exp\left(\eta\frac{D\_{-}u(\langle\nu\_{j-1},\widehat{r}\_{j}\rangle)}{u(\widehat{r}\_{j}^{\*})}\widehat{r}\_{j}^{i}\right),\quad\nu\_{j}^{i}=\frac{a\_{j}^{i}}{\sum\_{l=1}^{d}a\_{j}^{l}}, |  | (4.2) |

i=1,…,d𝑖

1…𝑑i=1,\dots,d, j=1,…,m−1𝑗

1…𝑚1j=1,\dots,m-1, where η>0𝜂0\eta>0 is a parameter. Note that,

|  |  |  |
| --- | --- | --- |
|  | −D−​u​(⟨νj−1,r^j⟩)u​(r^j∗)​r^j∈∂fj​(ν).subscript𝐷𝑢  subscript𝜈𝑗1subscript^𝑟𝑗𝑢superscriptsubscript^𝑟𝑗subscript^𝑟𝑗subscript𝑓𝑗𝜈-\frac{D\_{-}u(\langle\nu\_{j-1},\widehat{r}\_{j}\rangle)}{u(\widehat{r}\_{j}^{\*})}\widehat{r}\_{j}\in\partial f\_{j}(\nu). |  |

For a moment assume that r^j∈(0,∞)dsubscript^𝑟𝑗superscript0𝑑\widehat{r}\_{j}\in(0,\infty)^{d} is an arbitrary sequence. The basic problem of the
online convex optimization theory is to find a sequence ν0,…,νm−1

subscript𝜈0…subscript𝜈𝑚1\nu\_{0},\dots,\nu\_{m-1} such that νj−1subscript𝜈𝑗1\nu\_{j-1} does not depend on fj,…,fm

subscript𝑓𝑗…subscript𝑓𝑚f\_{j},\dots,f\_{m} and the regret

|  |  |  |
| --- | --- | --- |
|  | Regretm​(ν)=∑j=1mfj​(νj−1)−∑j=1mfj​(ν)=∑j=1mu​(⟨ν,r^j⟩)u​(r^j∗)−∑j=1mu​(⟨νj−1,r^j⟩)u​(r^j∗)subscriptRegret𝑚𝜈superscriptsubscript𝑗1𝑚subscript𝑓𝑗subscript𝜈𝑗1superscriptsubscript𝑗1𝑚subscript𝑓𝑗𝜈superscriptsubscript𝑗1𝑚𝑢  𝜈subscript^𝑟𝑗𝑢superscriptsubscript^𝑟𝑗superscriptsubscript𝑗1𝑚𝑢  subscript𝜈𝑗1subscript^𝑟𝑗𝑢superscriptsubscript^𝑟𝑗\textrm{Regret}\_{m}(\nu)=\sum\_{j=1}^{m}f\_{j}(\nu\_{j-1})-\sum\_{j=1}^{m}f\_{j}(\nu)=\sum\_{j=1}^{m}\frac{u(\langle\nu,\widehat{r}\_{j}\rangle)}{u(\widehat{r}\_{j}^{\*})}-\sum\_{j=1}^{m}\frac{u(\langle\nu\_{j-1},\widehat{r}\_{j}\rangle)}{u(\widehat{r}\_{j}^{\*})} |  |

is small uniformly over ν∈Δ𝜈Δ\nu\in\Delta. It is well known that the EG algorithm with η=ln⁡dm​1Ln𝜂𝑑𝑚1subscript𝐿𝑛\eta=\sqrt{\frac{\ln d}{m}}\frac{1}{L\_{n}} ensures the estimate

|  |  |  |  |
| --- | --- | --- | --- |
|  | Regretm​(ν)≤2​Ln​m​ln⁡d,subscriptRegret𝑚𝜈2subscript𝐿𝑛𝑚𝑑\textrm{Regret}\_{m}(\nu)\leq 2L\_{n}\sqrt{m}\sqrt{\ln d}, |  | (4.3) |

see [[22](#bib.bib22), Corollary 2.14] (a constant is corrected).

For an i.i.d. random sequence r^jsubscript^𝑟𝑗\widehat{r}\_{j} we can apply to ([4.1](#S4.E1 "In 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios")), ([4.2](#S4.E2 "In 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios")) the online-to-batch conversion scheme: [[22](#bib.bib22), Chap. 5]. In this case it is natural to call ([4.1](#S4.E1 "In 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios")), ([4.2](#S4.E2 "In 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios")) the stochastic exponentiated gradient (SEG) algorithm. Denote by 𝖤^^𝖤\widehat{\mathsf{E}} is the expectation with respect to the empirical distribution of r1,…,rn

subscript𝑟1…subscript𝑟𝑛r\_{1},\dots,r\_{n}. For any fixed ν𝜈\nu,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖤^​u​(⟨ν,r^j⟩)u​(r^j∗)=1n​∑k=1nu​(⟨ν,rk⟩)u​(rk∗)=U^n​(ν).^𝖤𝑢  𝜈subscript^𝑟𝑗𝑢superscriptsubscript^𝑟𝑗1𝑛superscriptsubscript𝑘1𝑛𝑢  𝜈subscript𝑟𝑘𝑢superscriptsubscript𝑟𝑘subscript^𝑈𝑛𝜈\widehat{\mathsf{E}}\frac{u(\langle\nu,\widehat{r}\_{j}\rangle)}{u(\widehat{r}\_{j}^{\*})}=\frac{1}{n}\sum\_{k=1}^{n}\frac{u(\langle\nu,r\_{k}\rangle)}{u(r\_{k}^{\*})}=\widehat{U}\_{n}(\nu). |  | (4.4) |

Furthermore, since νj−1subscript𝜈𝑗1\nu\_{j-1} is σ​(r^1,…,r^j−1)𝜎subscript^𝑟1…subscript^𝑟𝑗1\sigma(\widehat{r}\_{1},\dots,\widehat{r}\_{j-1})-measurable, we have

|  |  |  |
| --- | --- | --- |
|  | 𝖤^u​(⟨νj−1,r^j⟩)u​(r^j∗)=𝖤^𝖤^(u​(⟨νj−1,r^j⟩)u​(r^j∗)|r^1,…,r^j−1)=𝖤^1n∑k=1nu​(⟨νj−1,rk⟩)u​(rk∗),\widehat{\mathsf{E}}\frac{u(\langle\nu\_{j-1},\widehat{r}\_{j}\rangle)}{u(\widehat{r}\_{j}^{\*})}=\widehat{\mathsf{E}}\widehat{\mathsf{E}}\left(\frac{u(\langle\nu\_{j-1},\widehat{r}\_{j}\rangle)}{u(\widehat{r}\_{j}^{\*})}\biggl{|}\widehat{r}\_{1},\dots,\widehat{r}\_{j-1}\right)=\widehat{\mathsf{E}}\frac{1}{n}\sum\_{k=1}^{n}\frac{u(\langle\nu\_{j-1},r\_{k}\rangle)}{u(r\_{k}^{\*})}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1m​𝖤^​∑j=1mu​(⟨νj−1,rj⟩)u​(rj∗)1𝑚^𝖤superscriptsubscript𝑗1𝑚𝑢  subscript𝜈𝑗1subscript𝑟𝑗𝑢superscriptsubscript𝑟𝑗\displaystyle\frac{1}{m}\widehat{\mathsf{E}}\sum\_{j=1}^{m}\frac{u(\langle\nu\_{j-1},r\_{j}\rangle)}{u(r\_{j}^{\*})} | =1m​∑j=1m𝖤^​1n​∑k=1nu​(⟨νj−1,rk⟩)u​(rk∗)=1n​∑k=1n𝖤^​1m​∑j=1mu​(⟨νj−1,rk⟩)u​(rk∗)absent1𝑚superscriptsubscript𝑗1𝑚^𝖤1𝑛superscriptsubscript𝑘1𝑛𝑢  subscript𝜈𝑗1subscript𝑟𝑘𝑢superscriptsubscript𝑟𝑘1𝑛superscriptsubscript𝑘1𝑛^𝖤1𝑚superscriptsubscript𝑗1𝑚𝑢  subscript𝜈𝑗1subscript𝑟𝑘𝑢superscriptsubscript𝑟𝑘\displaystyle=\frac{1}{m}\sum\_{j=1}^{m}\widehat{\mathsf{E}}\frac{1}{n}\sum\_{k=1}^{n}\frac{u(\langle\nu\_{j-1},r\_{k}\rangle)}{u(r\_{k}^{\*})}=\frac{1}{n}\sum\_{k=1}^{n}\widehat{\mathsf{E}}\frac{1}{m}\sum\_{j=1}^{m}\frac{u(\langle\nu\_{j-1},r\_{k}\rangle)}{u(r\_{k}^{\*})} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤𝖤^​1n​∑k=1nu​(⟨ν¯m,rk⟩)u​(rk∗)=𝖤^​U^n​(ν¯m),absent^𝖤1𝑛superscriptsubscript𝑘1𝑛𝑢  subscript¯𝜈𝑚subscript𝑟𝑘𝑢superscriptsubscript𝑟𝑘^𝖤subscript^𝑈𝑛subscript¯𝜈𝑚\displaystyle\leq\widehat{\mathsf{E}}\frac{1}{n}\sum\_{k=1}^{n}\frac{u(\langle\overline{\nu}\_{m},r\_{k}\rangle)}{u(r\_{k}^{\*})}=\widehat{\mathsf{E}}\widehat{U}\_{n}(\overline{\nu}\_{m}), |  | (4.5) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν¯m=1m​∑j=0m−1νj.subscript¯𝜈𝑚1𝑚superscriptsubscript𝑗0𝑚1subscript𝜈𝑗\overline{\nu}\_{m}=\frac{1}{m}\sum\_{j=0}^{m-1}\nu\_{j}. |  | (4.6) |

In these calculations r1,…,rn

subscript𝑟1…subscript𝑟𝑛r\_{1},\dots,r\_{n} are regarded as constants. Note that νjsubscript𝜈𝑗\nu\_{j}, ν¯msubscript¯𝜈𝑚\overline{\nu}\_{m} depend also on n𝑛n, but we suppress this dependence in the notation.

From ([4.3](#S4.E3 "In 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios")) – ([4.5](#S4.E5 "In 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios")) we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​Ln​ln⁡dm≥𝖤^​Regretm​(ν)m2subscript𝐿𝑛𝑑𝑚^𝖤subscriptRegret𝑚𝜈𝑚\displaystyle 2L\_{n}\sqrt{\frac{\ln d}{m}}\geq\widehat{\mathsf{E}}\frac{\textrm{Regret}\_{m}(\nu)}{m} | =1m​𝖤^​∑j=1m(u​(⟨ν,r^j⟩)u​(r^j∗)−u​(⟨νj−1,r^j⟩)u​(r^j∗))≥U^n​(ν)−𝖤^​U^n​(ν¯m).absent1𝑚^𝖤superscriptsubscript𝑗1𝑚𝑢  𝜈subscript^𝑟𝑗𝑢superscriptsubscript^𝑟𝑗𝑢  subscript𝜈𝑗1subscript^𝑟𝑗𝑢superscriptsubscript^𝑟𝑗subscript^𝑈𝑛𝜈^𝖤subscript^𝑈𝑛subscript¯𝜈𝑚\displaystyle=\frac{1}{m}\widehat{\mathsf{E}}\sum\_{j=1}^{m}\left(\frac{u(\langle\nu,\widehat{r}\_{j}\rangle)}{u(\widehat{r}\_{j}^{\*})}-\frac{u(\langle\nu\_{j-1},\widehat{r}\_{j}\rangle)}{u(\widehat{r}\_{j}^{\*})}\right)\geq\widehat{U}\_{n}(\nu)-\widehat{\mathsf{E}}\widehat{U}\_{n}(\overline{\nu}\_{m}). |  |

In particular, for an empirical utility maximizer ν^nsubscript^𝜈𝑛\widehat{\nu}\_{n},

|  |  |  |  |
| --- | --- | --- | --- |
|  | U^n​(ν^n)≤𝖤^​U^n​(ν¯m)+2​Ln​ln⁡dm≤U^n​(ν¯m)+12​n​ln⁡1δ+2​Ln​ln⁡dmsubscript^𝑈𝑛subscript^𝜈𝑛^𝖤subscript^𝑈𝑛subscript¯𝜈𝑚2subscript𝐿𝑛𝑑𝑚subscript^𝑈𝑛subscript¯𝜈𝑚12𝑛1𝛿2subscript𝐿𝑛𝑑𝑚\widehat{U}\_{n}(\widehat{\nu}\_{n})\leq\widehat{\mathsf{E}}\widehat{U}\_{n}(\overline{\nu}\_{m})+2L\_{n}\sqrt{\frac{\ln d}{m}}\leq\widehat{U}\_{n}(\overline{\nu}\_{m})+\sqrt{\frac{1}{2n}\ln\frac{1}{\delta}}+2L\_{n}\sqrt{\frac{\ln d}{m}} |  | (4.7) |

with probability at least 1−δ1𝛿1-\delta by Hoeffding’s inequality ([[20](#bib.bib20), Theorem D.2]):

|  |  |  |
| --- | --- | --- |
|  | 𝖯^​(𝖤^​U^n​(ν¯m)−U^n​(ν¯m)≥ε)=𝖯^​(1n​∑k=1nu​(⟨ν¯m,rk⟩)u​(rk∗)−𝖤^​1n​∑k=1nu​(⟨ν¯m,rk⟩)u​(rk∗)≥ε)≤e−2​ε2​n^𝖯^𝖤subscript^𝑈𝑛subscript¯𝜈𝑚subscript^𝑈𝑛subscript¯𝜈𝑚𝜀^𝖯1𝑛superscriptsubscript𝑘1𝑛𝑢  subscript¯𝜈𝑚subscript𝑟𝑘𝑢superscriptsubscript𝑟𝑘^𝖤1𝑛superscriptsubscript𝑘1𝑛𝑢  subscript¯𝜈𝑚subscript𝑟𝑘𝑢superscriptsubscript𝑟𝑘𝜀superscript𝑒2superscript𝜀2𝑛\displaystyle\widehat{\mathsf{P}}(\widehat{\mathsf{E}}\widehat{U}\_{n}(\overline{\nu}\_{m})-\widehat{U}\_{n}(\overline{\nu}\_{m})\geq\varepsilon)=\widehat{\mathsf{P}}\left(\frac{1}{n}\sum\_{k=1}^{n}\frac{u(\langle\overline{\nu}\_{m},r\_{k}\rangle)}{u(r\_{k}^{\*})}-\widehat{\mathsf{E}}\frac{1}{n}\sum\_{k=1}^{n}\frac{u(\langle\overline{\nu}\_{m},r\_{k}\rangle)}{u(r\_{k}^{\*})}\geq\varepsilon\right)\leq e^{-2\varepsilon^{2}n} |  |

with ε=12​n​ln⁡1δ𝜀12𝑛1𝛿\varepsilon=\sqrt{\frac{1}{2n}\ln\frac{1}{\delta}}.

We now able to provide for ν¯msubscript¯𝜈𝑚\overline{\nu}\_{m} an analog of inequality ([3.3](#S3.E3 "In Theorem 1. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(ν∗)−U​(ν¯m)𝑈superscript𝜈𝑈subscript¯𝜈𝑚\displaystyle U(\nu^{\*})-U(\overline{\nu}\_{m}) | =U​(ν∗)−U^n​(ν∗)+U^n​(ν∗)−U^n​(νn)+U^n​(νn)−U^n​(ν¯m)+U^n​(ν¯m)−U​(ν¯m)absent𝑈superscript𝜈subscript^𝑈𝑛superscript𝜈subscript^𝑈𝑛superscript𝜈subscript^𝑈𝑛subscript𝜈𝑛subscript^𝑈𝑛subscript𝜈𝑛subscript^𝑈𝑛subscript¯𝜈𝑚subscript^𝑈𝑛subscript¯𝜈𝑚𝑈subscript¯𝜈𝑚\displaystyle=U(\nu^{\*})-\widehat{U}\_{n}(\nu^{\*})+\widehat{U}\_{n}(\nu^{\*})-\widehat{U}\_{n}(\nu\_{n})+\widehat{U}\_{n}(\nu\_{n})-\widehat{U}\_{n}(\overline{\nu}\_{m})+\widehat{U}\_{n}(\overline{\nu}\_{m})-U(\overline{\nu}\_{m}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(U​(ν∗)−U^n​(ν∗))+(U^n​(νn)−U^n​(ν¯m))+supν∈ΔGn​(ν).absent𝑈superscript𝜈subscript^𝑈𝑛superscript𝜈subscript^𝑈𝑛subscript𝜈𝑛subscript^𝑈𝑛subscript¯𝜈𝑚subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈\displaystyle\leq(U(\nu^{\*})-\widehat{U}\_{n}(\nu^{\*}))+(\widehat{U}\_{n}(\nu\_{n})-\widehat{U}\_{n}(\overline{\nu}\_{m}))+\sup\_{\nu\in\Delta}G\_{n}(\nu). |  |

Applying ([3.2](#S3.E2 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")), ([4.7](#S4.E7 "In 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios")) and ([3.1](#S3.E1 "In 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios")) respectively to the tree terms in the right-hand side, we get the following result.

###### Theorem 3.

Assume that the function u𝑢u is concave. Then for the average portfolio ([4.6](#S4.E6 "In 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios")), produced by the SEG algorithm ([4.1](#S4.E1 "In 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios")), ([4.2](#S4.E2 "In 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios")), with probability at least 1−3​δ13𝛿1-3\delta the following estimate holds true:

|  |  |  |
| --- | --- | --- |
|  | U​(ν∗)−U​(ν¯m)≤𝖤​supν∈ΔGn​(ν)+3​12​n​ln⁡1δ+2​Ln​ln⁡dm.𝑈superscript𝜈𝑈subscript¯𝜈𝑚𝖤subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈312𝑛1𝛿2subscript𝐿𝑛𝑑𝑚\displaystyle U(\nu^{\*})-U(\overline{\nu}\_{m})\leq\mathsf{E}\sup\_{\nu\in\Delta}G\_{n}(\nu)+3\sqrt{\frac{1}{2n}\ln\frac{1}{\delta}}+2L\_{n}\sqrt{\frac{\ln d}{m}}. |  |

Certainly, the estimates of Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios") still can be applied to 𝖤​supν∈ΔGn​(ν)𝖤subscriptsupremum𝜈Δsubscript𝐺𝑛𝜈\mathsf{E}\sup\_{\nu\in\Delta}G\_{n}(\nu). Thus, Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios") gives a high-probability bound for the estimation error of the stochastic exponentiated gradient algorithm. The value of m𝑚m can be taken sufficiently large to get for the estimation error of ν¯msubscript¯𝜈𝑚\overline{\nu}\_{m} the bound of the same order as for the exact empirical utility maximizer ν^nsubscript^𝜈𝑛\widehat{\nu}\_{n}. The mentioned value of m𝑚m is data dependent, since the Lipschitz constant Lnsubscript𝐿𝑛L\_{n} depends on the returns (r1,…,rn)subscript𝑟1…subscript𝑟𝑛(r\_{1},\dots,r\_{n}). Note, that we need no new data to generate an arbitrary large sample r^1,…,r^m

subscript^𝑟1…subscript^𝑟𝑚\widehat{r}\_{1},\dots,\widehat{r}\_{m} used in the SEG algorithm.

## 5. Power utility: the case of one risky asset

Consider the case d=2𝑑2d=2. In this section we will put upper indexes in brackets. Assume that the investor can keep money in cash: rt(1)=1subscriptsuperscript𝑟1𝑡1r^{(1)}\_{t}=1, or invest in a risky asset, whose daily returns are log-normal and follow the discrete-time Black-Scholes model:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rk(2)=exp⁡(μ−σ2/2T+σT​Zk),k=1,…,n.formulae-sequencesuperscriptsubscript𝑟𝑘2𝜇superscript𝜎22𝑇𝜎𝑇subscript𝑍𝑘𝑘  1…𝑛r\_{k}^{(2)}=\exp\left(\frac{\mu-\sigma^{2}/2}{T}+\frac{\sigma}{\sqrt{T}}Z\_{k}\right),\quad\quad k=1,\dots,n. |  | (5.1) |

Here T=252𝑇252T=252 is the number of trading days in a year; Zksubscript𝑍𝑘Z\_{k} are independent standard normal variables: Zk∼N​(0,1)similar-tosubscript𝑍𝑘𝑁01Z\_{k}\sim N(0,1); n𝑛n is the sample size, which we assume to be multiple of T𝑇T. Put μ=0.15𝜇0.15\mu=0.15, which corresponds to

|  |  |  |
| --- | --- | --- |
|  | 𝖤​∏k=1Trk(2)=eμ≈1.162𝖤superscriptsubscriptproduct𝑘1𝑇superscriptsubscript𝑟𝑘2superscript𝑒𝜇1.162\mathsf{E}\prod\_{k=1}^{T}r\_{k}^{(2)}=e^{\mu}\approx 1.162 |  |

annual expected return for the risky asset, and σ=0.45𝜎0.45\sigma=0.45. We have

|  |  |  |
| --- | --- | --- |
|  | ln⁡rk(2)∼N​(μ−σ2/2T,σT)=N​(1.93⋅10−4,2.83⋅10−2).similar-tosuperscriptsubscript𝑟𝑘2𝑁𝜇superscript𝜎22𝑇𝜎𝑇𝑁⋅1.93superscript104⋅2.83superscript102\ln r\_{k}^{(2)}\sim N\left(\frac{\mu-\sigma^{2}/2}{T},\frac{\sigma}{\sqrt{T}}\right)=N(1.93\cdot 10^{-4},2.83\cdot 10^{-2}). |  |

In this section we assume that u​(x)=xα𝑢𝑥superscript𝑥𝛼u(x)=x^{\alpha}, α∈(0,1]𝛼01\alpha\in(0,1]. The the relative empirical utility maximization problem ([2.2](#S2.E2 "In 2. Problem formulation ‣ Relative utility bounds for empirically optimal portfolios")) takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(ν(2))=1n​∑k=1n⟨ν,rk/rk∗⟩α=1n​∑k=1n(1max⁡{1,rk(2)}+rk(2)−1max⁡{1,rk(2)}​ν(2))α→maxν(2)∈[0,1].𝜓superscript𝜈21𝑛superscriptsubscript𝑘1𝑛superscript  𝜈subscript𝑟𝑘superscriptsubscript𝑟𝑘 𝛼1𝑛superscriptsubscript𝑘1𝑛superscript11superscriptsubscript𝑟𝑘2superscriptsubscript𝑟𝑘211superscriptsubscript𝑟𝑘2superscript𝜈2𝛼→subscriptsuperscript𝜈201\psi(\nu^{(2)})=\frac{1}{n}\sum\_{k=1}^{n}\langle\nu,r\_{k}/r\_{k}^{\*}\rangle^{\alpha}=\frac{1}{n}\sum\_{k=1}^{n}\left(\frac{1}{\max\{1,r\_{k}^{(2)}\}}+\frac{r\_{k}^{(2)}-1}{\max\{1,r\_{k}^{(2)}\}}\nu^{(2)}\right)^{\alpha}\to\max\_{\nu^{(2)}\in[0,1]}. |  | (5.2) |

For comparison consider also the ordinary empirical utility:

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ​(ν(2))=1n​∑k=1n⟨ν,rk⟩α=1n​∑k=1n(1+(rk(2)−1)​ν(2))α→maxν(2)∈[0,1].𝜑superscript𝜈21𝑛superscriptsubscript𝑘1𝑛superscript  𝜈subscript𝑟𝑘 𝛼1𝑛superscriptsubscript𝑘1𝑛superscript1superscriptsubscript𝑟𝑘21superscript𝜈2𝛼→subscriptsuperscript𝜈201\varphi(\nu^{(2)})=\frac{1}{n}\sum\_{k=1}^{n}\langle\nu,r\_{k}\rangle^{\alpha}=\frac{1}{n}\sum\_{k=1}^{n}\left(1+(r\_{k}^{(2)}-1)\nu^{(2)}\right)^{\alpha}\to\max\_{\nu^{(2)}\in[0,1]}. |  | (5.3) |

For a large n=T⋅103=2.52⋅105𝑛⋅𝑇superscript103⋅2.52superscript105n=T\cdot 10^{3}=2.52\cdot 10^{5} we applied to φ′​(ν2),ψ′​(ν2)

superscript𝜑′subscript𝜈2superscript𝜓′subscript𝜈2\varphi^{\prime}(\nu\_{2}),\psi^{\prime}(\nu\_{2}) the bisection method optimize.bisect from the module scipy (Python) with the default tolerance parameter. The results, averaged over 100 realizations of (rk(2))k=1nsuperscriptsubscriptsuperscriptsubscript𝑟𝑘2𝑘1𝑛(r\_{k}^{(2)})\_{k=1}^{n}, are presented in Table [1](#S5.T1 "Table 1 ‣ 5. Power utility: the case of one risky asset ‣ Relative utility bounds for empirically optimal portfolios").

Table 1. Average optimal weight ν(2)superscript𝜈2\nu^{(2)} of the risky asset

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| α𝛼\alpha | 0.001 | 0.01 | 0.1 | 0.2 | 0.3 | 0.5 | 0.75 | 0.9 |
| Ordinary power  utility, φ𝜑\varphi | 0.7380 | 0.7448 | 0.8188 | 0.9118 | 0.9775 | 1 | 1 | 1 |
| Relative power  utility, ψ𝜓\psi | 0.7376 | 0.7397 | 0.7637 | 0.7961 | 0.8367 | 0.9245 | 0.9909 | 1 |

We see that the relative utility makes the investor more risk averse. This property can be easily explained. Instead of the power utility function consider a differentiable increasing concave function u𝑢u. Without loss of generality, we can assume that u​(1)=1𝑢11u(1)=1. For the expected utilities, corresponding to ([5.2](#S5.E2 "In 5. Power utility: the case of one risky asset ‣ Relative utility bounds for empirically optimal portfolios")), ([5.3](#S5.E3 "In 5. Power utility: the case of one risky asset ‣ Relative utility bounds for empirically optimal portfolios")), we have

|  |  |  |
| --- | --- | --- |
|  | ψ′​(ν(2)):=∂U​(ν)∂ν(2)=𝖤​(u′​(1+(r(2)−1)​ν(2))u​(max⁡{1,r(2)})​(r(2)−1))assignsuperscript𝜓′superscript𝜈2𝑈𝜈superscript𝜈2𝖤superscript𝑢′1superscript𝑟21superscript𝜈2𝑢1superscript𝑟2superscript𝑟21\displaystyle\psi^{\prime}(\nu^{(2)}):=\frac{\partial U(\nu)}{\partial\nu^{(2)}}=\mathsf{E}\left(\frac{u^{\prime}(1+(r^{(2)}-1)\nu^{(2)})}{u(\max\{1,r^{(2)}\})}(r^{(2)}-1)\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =𝖤​(u′​(1+(r(2)−1)​ν(2))​(r(2)−1)​I{r(2)≤1})+𝖤​(u′​(1+(r(2)−1)​ν(2))u​(r(2))​(r(2)−1)​I{r(2)>1})absent𝖤superscript𝑢′1superscript𝑟21superscript𝜈2superscript𝑟21subscript𝐼superscript𝑟21𝖤superscript𝑢′1superscript𝑟21superscript𝜈2𝑢superscript𝑟2superscript𝑟21subscript𝐼superscript𝑟21\displaystyle=\mathsf{E}\left(u^{\prime}(1+(r^{(2)}-1)\nu^{(2)})(r^{(2)}-1)I\_{\{r^{(2)}\leq 1\}}\right)+\mathsf{E}\left(\frac{u^{\prime}(1+(r^{(2)}-1)\nu^{(2)})}{u(r^{(2)})}(r^{(2)}-1)I\_{\{r^{(2)}>1\}}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝖤(u′(1+(r(2)−1)ν(2))(r(2)−1))=∂U~​(ν)∂ν(2)=:φ′(ν(2)),\displaystyle\leq\mathsf{E}\left(u^{\prime}(1+(r^{(2)}-1)\nu^{(2)})(r^{(2)}-1)\right)=\frac{\partial\widetilde{U}(\nu)}{\partial\nu^{(2)}}=:\varphi^{\prime}(\nu^{(2)}), |  |

where U~​(ν)=𝖤​u​(⟨ν,r⟩)~𝑈𝜈𝖤𝑢

𝜈𝑟\widetilde{U}(\nu)=\mathsf{E}u(\langle\nu,r\rangle) is the ordinary expected utility. The functions ψ′superscript𝜓′\psi^{\prime}, φ′superscript𝜑′\varphi^{\prime} are decreasing. It follows that the zero of ψ′superscript𝜓′\psi^{\prime} is smaller than the zero of φ′superscript𝜑′\varphi^{\prime} (for simplicity we assume that a zero is unique). A similar argumentation works for the empirical utilities.

However, in the next section we will see that the discussed property is not universal. In a model with several risky assets the optimal portfolio, corresponding to the relative power utility, can be more risky, than for the ordinary utility.

Next we argue that if the price of a risky asset follows the Black-Scholes model, neither 101010 nor 100100100 years are enough to make any reliable conclusions concerning the optimal value ν(∗,2)superscript𝜈2\nu^{(\*,2)} on the basis of daily historical prices.

For α=0.2𝛼0.2\alpha=0.2 in the left panels of Fig. [1](#S5.F1 "Figure 1 ‣ 5. Power utility: the case of one risky asset ‣ Relative utility bounds for empirically optimal portfolios") we show the histograms of the optimal weight ν^n(2)subscriptsuperscript^𝜈2𝑛\widehat{\nu}^{(2)}\_{n} of the risky asset for 200 realizations of daily returns (rk(2))k=1nsuperscriptsubscriptsuperscriptsubscript𝑟𝑘2𝑘1𝑛(r\_{k}^{(2)})\_{k=1}^{n}, where n=252⋅10k𝑛⋅252superscript10𝑘n=252\cdot 10^{k}, k=1,2,3𝑘

123k=1,2,3. To estimate the true utility U​(ν)𝑈𝜈U(\nu) of ν^^𝜈\widehat{\nu} we used the empirical mean U^N​(ν)subscript^𝑈𝑁𝜈\widehat{U}\_{N}(\nu) with very large N=107𝑁superscript107N=10^{7}. The histogram of linearly transformed true utilities (U​(ν^)−U​(w0))⋅104⋅𝑈^𝜈𝑈subscript𝑤0superscript104(U(\widehat{\nu})-U(w\_{0}))\cdot 10^{4}, w0=(1,0)subscript𝑤010w\_{0}=(1,0) are shown in the right panels in Fig. [1](#S5.F1 "Figure 1 ‣ 5. Power utility: the case of one risky asset ‣ Relative utility bounds for empirically optimal portfolios"). In the same way we obtained the estimates of the optimal weight of the risky asset: ν∗,2≈0.81superscript𝜈

20.81\nu^{\*,2}\approx 0.81, and its utility

|  |  |  |  |
| --- | --- | --- | --- |
|  | (U​(ν^∗)−U​(w0))⋅104≈0.42.⋅𝑈superscript^𝜈𝑈subscript𝑤0superscript1040.42(U(\widehat{\nu}^{\*})-U(w\_{0}))\cdot 10^{4}\approx 0.42. |  | (5.4) |

![Refer to caption](/html/2006.05204/assets/one_risky_hist.png)


Figure 1. Histograms of optimal weight ν^n(2)subscriptsuperscript^𝜈2𝑛\widehat{\nu}^{(2)}\_{n} of the risky asset (left panels) and of
linearly transformed true utility (U​(ν^n)−U​(w0))⋅104⋅𝑈subscript^𝜈𝑛𝑈subscript𝑤0superscript104(U(\widehat{\nu}\_{n})-U(w\_{0}))\cdot 10^{4}, w0=(1,0)subscript𝑤010w\_{0}=(1,0) (right panels) for 200 realizations of daily returns (rk(2))k=1nsuperscriptsubscriptsuperscriptsubscript𝑟𝑘2𝑘1𝑛(r\_{k}^{(2)})\_{k=1}^{n} for n=252⋅10k𝑛⋅252superscript10𝑘n=252\cdot 10^{k}, k=1,2,3𝑘

123k=1,2,3. The case of relative power utility with α=0.2𝛼0.2\alpha=0.2.

We see that optimal portfolio weights very slowly concentrate near the optimal value. In particular for
n=252⋅10𝑛⋅25210n=252\cdot 10 in most cases ν^n(2)superscriptsubscript^𝜈𝑛2\widehat{\nu}\_{n}^{(2)} simply takes the extreme values 0 and 1. Only for n=252⋅103𝑛⋅252superscript103n=252\cdot 10^{3} the largest peak is near the optimum. But even in this case it is blurred. Note, however, that the true utilities of ν^n(2)superscriptsubscript^𝜈𝑛2\widehat{\nu}\_{n}^{(2)} demonstrate somewhat better concentration near the optimum ([5.4](#S5.E4 "In 5. Power utility: the case of one risky asset ‣ Relative utility bounds for empirically optimal portfolios")). These conclusions are not specific for the relative power utility or for a specific value of α𝛼\alpha. For for other values of α𝛼\alpha, and for the ordinary power or logarithmic utilities the results will be similar.

Note that the slow concentration phenomenon (which is related to the fragility of SAA in portfolio optimization: [[1](#bib.bib1)]) does not contradict Theorems [1](#Thmtheorem1 "Theorem 1. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios"), [2](#Thmtheorem2 "Theorem 2. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios"). Roughly speaking, these theorems give the estimate

|  |  |  |
| --- | --- | --- |
|  | U​(ν∗)−U​(w0)≤U​(ν^n)−U​(w0)+O​(1n)𝑈superscript𝜈𝑈subscript𝑤0𝑈subscript^𝜈𝑛𝑈subscript𝑤0𝑂1𝑛U(\nu^{\*})-U(w\_{0})\leq U(\widehat{\nu}\_{n})-U(w\_{0})+O\left(\frac{1}{\sqrt{n}}\right) |  |

with high probability. From ([5.4](#S5.E4 "In 5. Power utility: the case of one risky asset ‣ Relative utility bounds for empirically optimal portfolios")) it follows that we need n𝑛n at least of order 108superscript10810^{8} to get a nontrivial lower bound for U​(ν^n)−U​(w0)𝑈subscript^𝜈𝑛𝑈subscript𝑤0U(\widehat{\nu}\_{n})-U(w\_{0}).

## 6. Experiments with NYSE data

We considered two datasets, containing daily stock returns form the New-York Stock Exchange (NYSE):

* •

  NYSE1: Contains 5651 daily returns of 36 stocks for the period ending in 1984,
* •

  NYSE2: Contains 11178 daily returns of 19 stocks for the period ending in 2006.

Both datasets were taken from
<http://www.cs.bme.hu/~oti/portfolio/data.html>. NYSE1 is a classical dataset, considered in many papers, starting from [[7](#bib.bib7)] (see the references in [[13](#bib.bib13), [14](#bib.bib14)]). NYSE2 was first analized in [[13](#bib.bib13)], where the authors also proposed a simple greedy algorithm for the empirical logarithmic utility maximization:

|  |  |  |
| --- | --- | --- |
|  | 1n​∑k=1nln⁡⟨ν,rk⟩→maxν∈Δ.→1𝑛superscriptsubscript𝑘1𝑛𝜈subscript𝑟𝑘subscript𝜈Δ\frac{1}{n}\sum\_{k=1}^{n}\ln\langle\nu,r\_{k}\rangle\to\max\_{\nu\in\Delta}. |  |

In this paper we are interested in an application of the exponentited gradient (EG) algorithm. Note that already in [[15](#bib.bib15)] this algorithm was applied to the NYSE1 dataset and the logarithmic utility. However, our goal here is different: we want to solve the problem ([2.2](#S2.E2 "In 2. Problem formulation ‣ Relative utility bounds for empirically optimal portfolios")). Unfortunately we were unable to do this using the algorithm in the form ([4.1](#S4.E1 "In 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios")), ([4.2](#S4.E2 "In 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios")) or with time-varying learning rate η𝜂\eta (e.g., applying the doubling trick: see [[22](#bib.bib22)]). So, we propose its modification: the greedy doubly stochastic exponentiated gradient (GDSEG) algorithm. For clarity we present its pseudocode for the power utility u​(x)=xα𝑢𝑥superscript𝑥𝛼u(x)=x^{\alpha}.

Greedy doubly stochastic exponentiated gradient algorithm (GDSEG) for the power utility

1:η¯>0¯𝜂0\overline{\eta}>0: an upper bound for learning rate; n\_attempts: an upper bound for the number of attempts to improve a current portfolio; threshold: an improvement threshold; {rki:k∈{1,…,n},i∈{1,…,d}}conditional-setsuperscriptsubscript𝑟𝑘𝑖formulae-sequence𝑘1…𝑛𝑖1…𝑑\{r\_{k}^{i}:k\in\{1,\dots,n\},i\in\{1,\dots,d\}\}: an array of daily returns; α∈(0,1]𝛼01\alpha\in(0,1]

2:νi:=1/dassignsuperscript𝜈𝑖1𝑑\nu^{i}:=1/d, i=1,…,d𝑖

1…𝑑i=1,\dots,d

3:if the relative utility is considered then

4:     rki:=rki/maxj=1d⁡(rkj)assignsuperscriptsubscript𝑟𝑘𝑖superscriptsubscript𝑟𝑘𝑖superscriptsubscript𝑗1𝑑superscriptsubscript𝑟𝑘𝑗r\_{k}^{i}:=r\_{k}^{i}/\max\_{j=1}^{d}(r\_{k}^{j}), i=1,…,d𝑖

1…𝑑i=1,\dots,d, k=1,…,n𝑘

1…𝑛k=1,\dots,n

5:end if

6:attempt:=0assignattempt0\texttt{attempt}:=0

7:while attempt≤n\_attemptsattemptn\_attempts\texttt{attempt}\leq\texttt{n\\_attempts} do

8:     Choose k∈{1,…,n}𝑘1…𝑛k\in\{1,\dots,n\} uniformly at random

9:     Choose η∈[0,η¯]𝜂0¯𝜂\eta\in[0,\overline{\eta}] uniformly at random

10:     ai:=νi​exp⁡(η​rki/⟨ν,rk⟩1−α),wi:=ai∑j=1daj,formulae-sequenceassignsuperscript𝑎𝑖superscript𝜈𝑖𝜂superscriptsubscript𝑟𝑘𝑖superscript

𝜈subscript𝑟𝑘
1𝛼assignsuperscript𝑤𝑖superscript𝑎𝑖superscriptsubscript𝑗1𝑑superscript𝑎𝑗a^{i}:=\nu^{i}\exp\left(\eta r\_{k}^{i}/\langle\nu,r\_{k}\rangle^{1-\alpha}\right),\quad w^{i}:=\frac{a^{i}}{\sum\_{j=1}^{d}a^{j}},

11:     attempt:=attempt+1assignattemptattempt1\texttt{attempt}:=\texttt{attempt}+1

12:     if 1n​∑t=1n⟨w,rt⟩α≥1n​∑t=1n⟨ν,rt⟩α+threshold1𝑛superscriptsubscript𝑡1𝑛superscript

𝑤subscript𝑟𝑡
𝛼1𝑛superscriptsubscript𝑡1𝑛superscript

𝜈subscript𝑟𝑡
𝛼threshold\frac{1}{n}\sum\_{t=1}^{n}\langle w,r\_{t}\rangle^{\alpha}\geq\frac{1}{n}\sum\_{t=1}^{n}\langle\nu,r\_{t}\rangle^{\alpha}+\texttt{threshold} then

13:         ν:=wassign𝜈𝑤\nu:=w, attempt:=0assignattempt0\texttt{attempt}:=0

14:     end if

15:end while

16:an optimal portfolio ν𝜈\nu

The algorithm accepts either the original returns rksubscript𝑟𝑘r\_{k}, or the scaled returns rk/rk∗subscript𝑟𝑘superscriptsubscript𝑟𝑘r\_{k}/r\_{k}^{\*}. The first case corresponds to the traditional power utility, the second one to the relative power utility. At each point ν𝜈\nu the algorithm tries to make a step according to line 9, corresponding to ([4.2](#S4.E2 "In 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios")), where the return rksubscript𝑟𝑘r\_{k} and the learning rate are taken randomly by sampling k𝑘k and η𝜂\eta from the uniform distributions over {1,…,n}1…𝑛\{1,\dots,n\} and [0,η¯]0¯𝜂[0,\overline{\eta}] respectively. In fact, this is a step of a stochastic gradient method with random learning rate. That’s why we call the algorithm ‘‘doubly stochastic’’. Furthermore, the step will be actually performed only if the value of the objective function for the new portfolio w𝑤w surpasses the current value by a threshold: line 11. The algorithm stops if no such improvement is obtained for some predefined number of attempts: n\_attempts.

For the logarithmic utility one should put α=0𝛼0\alpha=0, and substitute in line 11 the power function by the logarithm. We do not consider the relative utility in this case.

The algorithm was applied to NYSE1 and NYSE2 datasets with the following parameters: η¯=1¯𝜂1\overline{\eta}=1, n\_attempts=104n\_attemptssuperscript104\texttt{n\\_attempts}=10^{4}, threshold=10−10thresholdsuperscript1010\texttt{threshold}=10^{-10}.
The number of iterations and the results depend on the seed parameter. The average number of attempts to improve the current portfolio for 30 runs of the algorithm was about 283⋅103⋅283superscript103283\cdot 10^{3} for NYSE1 and 73⋅103⋅73superscript10373\cdot 10^{3} for NYSE2. In both cases the output portfolio ν𝜈\nu concentrates only on few stocks: 5 for NYSE1 and 3 for NYSE2.
We drop νisuperscript𝜈𝑖\nu^{i} with νi<0.001superscript𝜈𝑖0.001\nu^{i}<0.001 and normalize the results:

|  |  |  |
| --- | --- | --- |
|  | νi:=νi​I{νi≥0.001}∑j=1dνj​I{νj≥0.001}.assignsuperscript𝜈𝑖superscript𝜈𝑖subscript𝐼superscript𝜈𝑖0.001superscriptsubscript𝑗1𝑑superscript𝜈𝑗subscript𝐼superscript𝜈𝑗0.001\nu^{i}:=\frac{\nu^{i}I\_{\{\nu^{i}\geq 0.001\}}}{\sum\_{j=1}^{d}\nu^{j}I\_{\{\nu^{j}\geq 0.001\}}}. |  |

For the logarithmic utility the results can be compared with those of [[4](#bib.bib4), [13](#bib.bib13)]. In Tables [2](#S6.T2 "Table 2 ‣ 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios"), [3](#S6.T3 "Table 3 ‣ 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios") we present minimal and maximal values for each weight, obtained in 30 runs of the GDSEG algorithm. The accumulated wealth Xn=∏t=1n⟨ν,rt⟩subscript𝑋𝑛superscriptsubscriptproduct𝑡1𝑛

𝜈subscript𝑟𝑡X\_{n}=\prod\_{t=1}^{n}\langle\nu,r\_{t}\rangle, in fact, does not depend on a particular output ν𝜈\nu:

|  |  |  |
| --- | --- | --- |
|  | NYSE1:X5651≈250.6,annual return: ​1.279;:NYSE1subscript𝑋5651  250.6annual return: 1.279\textrm{NYSE${}\_{1}$}:X\_{5651}\approx 250.6,\quad\textrm{annual return: }1.279; |  |

|  |  |  |
| --- | --- | --- |
|  | NYSE2:X11178≈4100.8,annual return: ​1.206.:NYSE2subscript𝑋11178  4100.8annual return: 1.206\textrm{NYSE${}\_{2}$}:X\_{11178}\approx 4100.8,\quad\textrm{annual return: }1.206. |  |

The annual return is computed by the formula Xn252/nsuperscriptsubscript𝑋𝑛252𝑛X\_{n}^{252/n}.

Table 2. Optimal weights for the logarithmic utility, NYSE1: 30 experiments of the GDSEG algorithm

|  |  |  |
| --- | --- | --- |
| Stock | Weight  [[4](#bib.bib4)] | Weight  GDSEG, [min,max][\min,\max] |
| comme | 0.2767 | [0.2766,0.2770]0.27660.2770[0.2766,0.2770] |
| espey | 0.1953 | [0.1952,0.1956]0.19520.1956[0.1952,0.1956] |
| iroqu | 0.0927 | [0.0925,0.0929]0.09250.0929[0.0925,0.0929] |
| kinar | 0.2507 | [0.2506,0.2508]0.25060.2508[0.2506,0.2508] |
| meico | 0.1845 | [0.1842,0.1847]0.18420.1847[0.1842,0.1847] |




Table 3. Optimal weights for the logarithmic utility, NYSE2: 30 experiments of the GDSEG algorithm

|  |  |  |
| --- | --- | --- |
| Stock | Weight  [[13](#bib.bib13)] | Weight  GDSEG, [min,max][\min,\max] |
| hp | 0.177 | [0.1771,0.1776]0.17710.1776[0.1771,0.1776] |
| morris | 0.747 | [0.7468,0.7472]0.74680.7472[0.7468,0.7472] |
| schlum | 0.076 | [0.0753,0.0757]0.07530.0757[0.0753,0.0757] |

In general the GDSEG algorithm need not be so stable. For the power utility u​(x)=xα𝑢𝑥superscript𝑥𝛼u(x)=x^{\alpha}
we implemented the following strategy: take an output ν𝜈\nu, corresponding to the largest value of the empirical utility function obtained in 10 experiments. The results for NYSE2 dataset are presented in Table [4](#S6.T4 "Table 4 ‣ 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios"). In the sequel we concentrate only on NYSE2.

Table 4. NYSE2: optimal portfolio weights, corresponding to the largest value of the empirical power utility function obtained in 10 experiments of the GDSEG algorithm; the accumulated wealth Xnsubscript𝑋𝑛X\_{n}, n=11178𝑛11178n=11178; the annual returns and the annual volatilities of these portfolios

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | | Ordinary utility | | | | Relative utility | | |  |
| α𝛼\alpha | Stocks | Weights | Xnsubscript𝑋𝑛X\_{n} | Ann  ret. | Ann.  volat. | Weights | Xnsubscript𝑋𝑛X\_{n} | Ann.  ret. | Ann.  volat. |
| 0.010.010.01 | hp  morris  schlum | 0.1792  0.7518  0.0690 | 4100.4 | 1.206 | 0.234 | 0.1782  0.7523  0.0695 | 4100.4 | 1.206 | 0.234 |
| 0.10.10.1 | hp  morris  schlum | 0.1762  0.7766  0.0473 | 4091.2 | 1.206 | 0.237 | 0.1617  0.7882  0.0501 | 4085.7 | 1.206 | 0.238 |
| 0.20.20.2 | hp  morris | 0.1779  0.8221 | 4035.7 | 1.206 | 0.245 | 0.1476  0.8524 | 3999.7 | 1.206 | 0.248 |
| 0.30.30.3 | hp  morris | 0.1589  0.8411 | 4016.1 | 1.206 | 0.247 | 0.1069  0.8931 | 3912.5 | 1.205 | 0.253 |
| 0.50.50.5 | hp  morris | 0.0972  0.9028 | 3885.4 | 1.205 | 0.254 | 0  1 | 3496.7 | 1.202 | 0.270 |
| 0.750.750.75 | morris | 1 | 3496.7 | 1.202 | 0.269 | 1 | 3496.7 | 1.202 | 0.270 |

Note that as α𝛼\alpha is growing, the utility maximizer concentrates more on one stock. This effect is stronger for the relative utility. Such behavior can be qualified as more risky: see the annual volatility of portfolio returns in Table [4](#S6.T4 "Table 4 ‣ 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios"). This quantity is defined as the empirical standard deviation of (⟨ν^n,rk⟩)k=1nsuperscriptsubscript

subscript^𝜈𝑛subscript𝑟𝑘
𝑘1𝑛(\langle\widehat{\nu}\_{n},r\_{k}\rangle)\_{k=1}^{n}, multiplied by 252252\sqrt{252}. For the log-optimal portfolio from Table [3](#S6.T3 "Table 3 ‣ 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios") it equals to 0.233.

Data used in the above calculations can be considered as a realization of some multidimensional stochastic process. From the example considered in Section [5](#S5 "5. Power utility: the case of one risky asset ‣ Relative utility bounds for empirically optimal portfolios") it is clear that the values of an empirical utility function can be very sensitive to such realizations. To get more insight on the risk and generalization properties of empirically optimal portfolios, let us try to describe the stock prices by the multidimensional Black-Scholes model:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sti=Sti​μi​d​t+Sti​∑j=1mσi​j​d​Wtj,i=1,…,d,formulae-sequence𝑑superscriptsubscript𝑆𝑡𝑖superscriptsubscript𝑆𝑡𝑖superscript𝜇𝑖𝑑𝑡superscriptsubscript𝑆𝑡𝑖superscriptsubscript𝑗1𝑚superscript𝜎𝑖𝑗𝑑superscriptsubscript𝑊𝑡𝑗𝑖  1…𝑑dS\_{t}^{i}=S\_{t}^{i}\mu^{i}dt+S\_{t}^{i}\sum\_{j=1}^{m}\sigma^{ij}\,dW\_{t}^{j},\quad i=1,\dots,d, |  | (6.1) |

where (W1,…,Wm)superscript𝑊1…superscript𝑊𝑚(W^{1},\dots,W^{m}) is a standard Wiener process, μ𝜇\mu is the drift vector and σ𝜎\sigma is the volatility matrix. Solving the system of stochastic differential equations ([6.1](#S6.E1 "In 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios")), we get

|  |  |  |
| --- | --- | --- |
|  | Sti=S0i​exp⁡((μi−12​∑j=1m(σi​j)2)​t+∑j=1mσi​j​Wtj),i=1,…,d.formulae-sequencesuperscriptsubscript𝑆𝑡𝑖superscriptsubscript𝑆0𝑖superscript𝜇𝑖12superscriptsubscript𝑗1𝑚superscriptsuperscript𝜎𝑖𝑗2𝑡superscriptsubscript𝑗1𝑚superscript𝜎𝑖𝑗subscriptsuperscript𝑊𝑗𝑡𝑖  1…𝑑S\_{t}^{i}=S\_{0}^{i}\exp\left(\left(\mu^{i}-\frac{1}{2}\sum\_{j=1}^{m}(\sigma^{ij})^{2}\right)t+\sum\_{j=1}^{m}\sigma^{ij}W^{j}\_{t}\right),\quad i=1,\dots,d. |  |

If t=1𝑡1t=1 corresponds to one year, then the daily log-returns should be approximated as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡rki=(αi−12​∑j=1m(σi​j)2)​h+∑j=1mσi​j​(Wk​hj−W(k−1)​hj),h=1/252,k=1,…,n.formulae-sequencesuperscriptsubscript𝑟𝑘𝑖superscript𝛼𝑖12superscriptsubscript𝑗1𝑚superscriptsuperscript𝜎𝑖𝑗2ℎsuperscriptsubscript𝑗1𝑚superscript𝜎𝑖𝑗subscriptsuperscript𝑊𝑗𝑘ℎsubscriptsuperscript𝑊𝑗𝑘1ℎformulae-sequenceℎ1252𝑘  1…𝑛\ln r\_{k}^{i}=\left(\alpha^{i}-\frac{1}{2}\sum\_{j=1}^{m}(\sigma^{ij})^{2}\right)h+\sum\_{j=1}^{m}\sigma^{ij}(W^{j}\_{kh}-W^{j}\_{(k-1)h}),\quad h=1/252,\quad k=1,\dots,n. |  | (6.2) |

We estimated the expectation vector and the covariance matrix

|  |  |  |
| --- | --- | --- |
|  | (αi​h−12​∑j=1m(σi​j)2​h)i=1d,(∑k=1mσi​k​σk​j​h)i,j=1d  superscriptsubscriptsuperscript𝛼𝑖ℎ12superscriptsubscript𝑗1𝑚superscriptsuperscript𝜎𝑖𝑗2ℎ𝑖1𝑑superscriptsubscriptsuperscriptsubscript𝑘1𝑚superscript𝜎𝑖𝑘superscript𝜎𝑘𝑗ℎ  𝑖𝑗 1𝑑\left(\alpha^{i}h-\frac{1}{2}\sum\_{j=1}^{m}(\sigma^{ij})^{2}h\right)\_{i=1}^{d},\qquad\left(\sum\_{k=1}^{m}\sigma^{ik}\sigma^{kj}h\right)\_{i,j=1}^{d} |  |

of (ln⁡rki)i=1dsuperscriptsubscriptsuperscriptsubscript𝑟𝑘𝑖𝑖1𝑑(\ln r\_{k}^{i})\_{i=1}^{d} for NYSE2 dataset, using the numpy module. This allows to generate the artificial data by ([6.2](#S6.E2 "In 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios")). For the empirically optimal portfolios from Tables [3](#S6.T3 "Table 3 ‣ 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios"), [4](#S6.T4 "Table 4 ‣ 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios"), as well as for the portfolio with uniform weights: w=(1/d,…,1/d)𝑤1𝑑…1𝑑w=(1/d,\dots,1/d), d=19𝑑19d=19, we computed some statistical characteristics of the annual accumulated wealth X252subscript𝑋252X\_{252}, using these data. The results are collected in Table [5](#S6.T5 "Table 5 ‣ 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios"). This table mainly demonstrates the risk properties of empirically optimal portfolios. For example, as α𝛼\alpha growth, the portfolios become more risky: their expectations and standard deviations increase, but medians decrease. The portfolios, corresponding to the relative power utility are more risky than for the ordinary one, in contrast to the example in Section [5](#S5 "5. Power utility: the case of one risky asset ‣ Relative utility bounds for empirically optimal portfolios"), but in accordance with Table [4](#S6.T4 "Table 4 ‣ 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios"): see again the annual volatility columns.

Table 5. Statistical characteristics of the annual accumulated wealth X252subscript𝑋252X\_{252} for the portfolios from Table [4](#S6.T4 "Table 4 ‣ 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios") for the artificial data ([6.2](#S6.E2 "In 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios")) with the parameters, estimated for NYSE2. Averaging was performed over 106superscript10610^{6} realizations, generated by the Black-Scholes model.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Portfolio | Mean | Median | Std.  deviation | 5-th  percentile | 95-th  percentile |
| uniform | 1.165 | 1.152 | 0.183 | 0.891 | 1.487 |
| log-optimal | 1.240 | 1.207 | 0.294 | 0.820 | 1.772 |
| α=0.01𝛼0.01\alpha=0.01  ordinary  relative | 1.240  1.240 | 1.207  1.207 | 0.295  0.295 | 0.819  0.819 | 1.775  1.775 |
| α=0.1𝛼0.1\alpha=0.1  ordinary  relative | 1.241  1.242 | 1.207  1.207 | 0.299  0.300 | 0.815  0.814 | 1.785  1.787 |
| α=0.2𝛼0.2\alpha=0.2  ordinary  relative | 1.243  1.244 | 1.206  1.206 | 0.310  0.314 | 0.805  0.801 | 1.808  1.815 |
| α=0.3𝛼0.3\alpha=0.3  ordinary  relative | 1.244  1.245 | 1.206  1.205 | 0.312  0.320 | 0.803  0.794 | 1.812  1.828 |
| α=0.5𝛼0.5\alpha=0.5  ordinary  relative | 1.245  1.247 | 1.205  1.202 | 0.322  0.342 | 0.793  0.771 | 1.831  1.872 |

The considered dataset is favorable for the investor: the stock prices are growing (on average). Moreover, the performance is evaluated with respect to a concrete model. However, even in this case the investment decisions, based on the historical data, are risky. For example, from Table [5](#S6.T5 "Table 5 ‣ 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios") we see that for the log-optimal portfolio there is 5% chance to loose more than 18% of an initial wealth within 1 year.

Note that the means are larger than the medians. This is in line with [[13](#bib.bib13)], where it is explained that typically Xnsubscript𝑋𝑛X\_{n} is less then the 𝖤​Xn𝖤subscript𝑋𝑛\mathsf{E}X\_{n} for log-optimal portfolios. We see also that the medians give good estimates for the annual returns from Table [4](#S6.T4 "Table 4 ‣ 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios").

Finally, we tried to estimate the true utility of the empirically optimal portfolios, constructed for trajectories of the Black-Scholes model. We used the same method as in Section [5](#S5 "5. Power utility: the case of one risky asset ‣ Relative utility bounds for empirically optimal portfolios"), but with the GDSEG algorithm instead of bisection. Namely, for α=0.2𝛼0.2\alpha=0.2 we considered 200 trajectories (r1,…,rn)subscript𝑟1…subscript𝑟𝑛(r\_{1},\dots,r\_{n}), n=11178𝑛11178n=11178 generated by the Black-Scholes model ([6.2](#S6.E2 "In 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios")) with parameters, estimated for NYSE2 dataset. For each trajectory the empirically optimal portfolio was computed by the GDSEG algorithm (we picked the best portfolio in 10 experiments).

For a fixed trajectory the optimal portfolio concentrated on a few number of stock (from 1 to 4). For illustration purposes in Fig. [2](#S6.F2 "Figure 2 ‣ 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios")(a) we show the average weight of each stock over 200 optimal portfolios. As in Table [3](#S6.T3 "Table 3 ‣ 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios"), the largest average weights have the stocks with numbers 9 (hp), 16 (morris), 18 (schlum). The next two positions occupy 12 (jnj) and 14 (merck).

The true utility of each portfolio was evaluated by the empirical mean, computed for a large sample: n=107𝑛superscript107n=10^{7}. In Fig. [2](#S6.F2 "Figure 2 ‣ 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios")(b), similar to left panels in Fig. [1](#S5.F1 "Figure 1 ‣ 5. Power utility: the case of one risky asset ‣ Relative utility bounds for empirically optimal portfolios"), we see a large cluster of very good portfolios. However, the the concentration is far from perfect. Let us mention also that the median (≈1.45absent1.45\approx 1.45) of the true utility is greater than the mean (≈1.40absent1.40\approx 1.40).

![Refer to caption](/html/2006.05204/assets/hist_2.png)


Figure 2. Relative power utility with α=0.2𝛼0.2\alpha=0.2. (a) Average weight of each stock in empirically optimal portfolio over 200 realizations of the Black-Scholes model ([6.2](#S6.E2 "In 6. Experiments with NYSE data ‣ Relative utility bounds for empirically optimal portfolios")); (b) Histogram of the evaluated true utility for the same 200 optimal portfolios.

## 7. Conclusion

In this paper we studied generalization properties of the empirically optimal portfolios for the relative utility maximization problem. We obtained high probability bounds for the estimation error and for the difference between the empirical and true utilities. Similar bounds were obtained for the portfolios, produced by the stochastic exponentiated gradient algorithm. The only assumptions, imposed on the returns is the i.i.d. hypothesis. The obtained bounds depend only the information available to the investor. We also performed some statistical experiments, demonstrating risk and generalization properties of the empirically optimal portfolios. For a multidimensional problem we proposed the greedy doubly stochastic exponentiated gradient (GDSEG) algorithm.

Let us mention some topics for further study.

* •

  In Theorems [1](#Thmtheorem1 "Theorem 1. ‣ 3. Utility bounds ‣ Relative utility bounds for empirically optimal portfolios") – [3](#Thmtheorem3 "Theorem 3. ‣ 4. Stochastic exponentiated gradient algorithm ‣ Relative utility bounds for empirically optimal portfolios") we considered the case of relative utility functions. To obtain similar bounds for ordinary utilities, in general one need to analyze the tails of the return distributions. In addition, the results of [[6](#bib.bib6)] should be useful for analysis of this problem.
* •

  The proposed GDSEG algorithm was enough for our purposes, but it requires large amount of calculations. It may be interesting to study this algorithm and its improvements in more detail.
* •

  Using side information is an important method for the construction of successful portfolio strategies. The recent papers [[3](#bib.bib3), [2](#bib.bib2)] contain theoretical and practical ideas that can be employed to study this problem in the statistical learning framework.

## References

* [1]

  G.-Y. Ban, N. El Karoui, and A.E.B. Lim.
  Machine learning and portfolio optimization.
  Management Science, 64(3):1136–1154, 2018.
* [2]

  T. Bazier-Matte and E. Delage.
  Generalization bounds for regularized portfolio selection with market
  side information.
  INFOR: Information Systems and Operational Research,
  58(2):374–401, 2020.
* [3]

  D. Bertsimas and N. Kallus.
  From predictive to prescriptive analytics.
  Management Science, 66(3):1025–1044, 2020.
* [4]

  A. Borodin, R. El-Yaniv, and V. Gogan.
  On the competitive theory and practice of portfolio selection
  (extended abstract).
  In G.H. Gonnet and A. Viola, editors, LATIN 2000: Theoretical
  Informatics, pages 173–196, Berlin, Heidelberg, 2000. Springer.
* [5]

  S. Boucheron, G. Lugosi, and P. Massart.
  Concentration inequalities: A nonasymptotic theory of
  independence.
  Oxford University Press, Oxford, 2013.
* [6]

  C. Cortes, S. Greenberg, and M. Mohri.
  Relative deviation learning bounds and generalization with unbounded
  loss functions.
  Ann. Math. Artif. Intell., 85:45–70, 2019.
* [7]

  T.M. Cover.
  Universal portfolios.
  Mathematical Finance, 1(1):1–29, 1991.
* [8]

  V. DeMiguel, L. Garlappi, F.J. Nogales, and R. Uppal.
  A generalized approach to portfolio optimization: Improving
  performance by constraining portfolio norms.
  Management Science, 55(5):798–812, 2009.
* [9]

  S. Ghosal and A. van der Vaart.
  Fundamentals of Nonparametric Bayesian Inference.
  Cambridge University Press, Cambridge, 2017.
* [10]

  J. Gotoh and A. Takeda.
  On the role of norm constraints in portfolio selection.
  Comput. Manag. Sci., 8:323–353, 2011.
* [11]

  J. Gotoh and A. Takeda.
  Minimizing loss probability bounds for portfolio selection.
  European Journal of Operational Research, 217(2):371 – 380,
  2012.
* [12]

  A. Gut.
  Probability: a graduate course.
  Springer, New York, 2013.
* [13]

  L. Györfi, G. Ottucsák, and A. Urbán.
  Empirical log-optimal portfolio selections: a survey.
  In Machine learning for financial engineering, pages 81–118.
  World Scientific, 2012.
* [14]

  L. Györfi, G. Ottucsák, and H. Walk.
  The growth optimal investment strategy is secure, too.
  In G. Consigli, D. Kuhn, and P. Brandimarte, editors, Optimal
  Financial Decision Making under Uncertainty, pages 201–223. Springer
  International Publishing, Cham, 2017.
* [15]

  D.P. Helmbold, R.E. Schapire, Y. Singer, and M.K. Warmuth.
  On-line portfolio selection using multiplicative updates.
  Mathematical Finance, 8(4):325–347, 1998.
* [16]

  J.-B. Hiriart-Urruty and C. Lemaréchal.
  Convex Analysis and Minimization Algorithms.
  Springer-Verlag, Berlin, 1993.
* [17]

  S. Kim, R. Pasupathy, and S. G. Henderson.
  A guide to sample average approximation.
  In M.C. Fu, editor, Handbook of Simulation Optimization, pages
  207–243. Springer, New York, 2015.
* [18]

  J. Kivinen and M.K. Warmuth.
  Exponentiated gradient versus gradient descent for linear predictors.
  Information and computation, 132(1):1–63, 1997.
* [19]

  D. Kuhn, P.M. Esfahani, V.A. Nguyen, and S. Shafieezadeh-Abadeh.
  Wasserstein distributionally robust optimization: Theory and
  applications in machine learning.
  In INFORMS TutORials in Operations Research, chapter 6, pages
  130–166. 2019.
* [20]

  M. Mohri, A. Rostamizadeh, and A. Talwalkar.
  Foundations of Machine Learning.
  The MIT Press, Cambridge, MA, 2018.
* [21]

  A. Rakhlin, O. Shamir, and K. Sridharan.
  Making gradient descent optimal for strongly convex stochastic
  optimization.
  In Int. Conf. Mach. Learn., pages 449–456, 2012.
* [22]

  S. Shalev-Shwartz.
  Online learning and online convex optimization.
  Foundations and Trends® in Machine Learning,
  4(2):107–194, 2012.
* [23]

  S. Shalev-Shwartz and S. Ben-David.
  Understanding Machine Learning: From Theory to Algorithms.
  Cambridge University Press, New York, 2014.
* [24]

  S. Shalev-Shwartz, O. Shamir, N. Srebro, and K. Sridharan.
  Learnability, stability and uniform convergence.
  Journal of Machine Learning Research, 11:2635–2670, 2010.
* [25]

  A. Shapiro, D. Dentcheva, and A. Ruszczynski.
  Lectures on Stochastic Programming: Modeling and Theory, Second
  Edition.
  SIAM, Philadelphia, 2014.
* [26]

  J.E. Smith and R.L. Winkler.
  The optimizer’s curse: Skepticism and postdecision surprise in
  decision analysis.
  Management Science, 52(3):311–322, 2006.
* [27]

  R. van Handel.
  APC 550: Probability in high dimension.
  Lecture Notes. Princeton University,
  https://web.math.princeton.edu/ rvan/APC550.pdf, 2016.
* [28]

  V. Vapnik.
  Statistical learning theory.
  Wiley, New York, 1998.
* [29]

  M.J. Wainwright.
  High-dimensional statistics: A non-asymptotic viewpoint.
  Cambridge University Press, Cambridge, 2019.

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/2006.05204)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2006.05204)
[View original  
on arXiv](https://arxiv.org/abs/2006.05204)[►](javascript: void(0))