---
authors:
- Bruno Bouchard
- Adil Reghai
- Benjamin Virrion
doc_id: arxiv:2005.12593v1
family_id: arxiv:2005.12593
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[2005.12593] Computation of Expected Shortfall by fast detection of worst
  scenarios'
url_abs: http://arxiv.org/abs/2005.12593v1
url_html: https://ar5iv.org/html/2005.12593v1
venue: arXiv q-fin
version: 1
year: 2020
---


Bruno Bouchard111CEREMADE, CNRS, Université Paris Dauphine, PSL University., Adil Reghai222Natixis., Benjamin Virrion333Natixis and CEREMADE, CNRS, Université Paris Dauphine, PSL University.,,{}^{\;\>,}444The authors would like to thank Nicolas Baradel for helping with the code, Rida Mahi and Mathieu Bernardo from the Natixis Quantitative Research Teams for providing the first results and ideas on the Fast Detection Algorithm, and finally William Leduc for providing all the necessary data to obtain the different book parameters.

###### Abstract

We consider a multi-step algorithm for the computation of the historical expected shortfall such as defined by the Basel Minimum Capital Requirements for Market Risk.
At each step of the algorithm, we use Monte Carlo simulations to reduce the number of historical scenarios that potentially belong to the set of worst scenarios. The number of simulations increases as the number of candidate scenarios is reduced and the distance between them diminishes. For the most naive scheme, we show that the 𝕃psuperscript𝕃𝑝{{\mathbb{L}}}^{p}-error of the estimator of the Expected Shortfall is bounded by a linear combination of the probabilities of inversion of favorable and unfavorable scenarios at each step, and of the last step Monte Carlo error associated to each scenario. By using concentration inequalities, we then show that, for sub-gamma pricing errors, the probabilities of inversion converge at an exponential rate in the number of simulated paths. We then propose an adaptative version in which the algorithm improves step by step its knowledge on the unknown parameters of interest: mean and variance of the Monte Carlo estimators of the different scenarios. Both schemes can be optimized by using dynamic programming algorithms that can be solved off-line.
To our knowledge, these are the first non-asymptotic bounds for such estimators. Our hypotheses are weak enough to allow for the use of estimators for the different scenarios and steps based on the same random variables, which, in practice, reduces considerably the computational effort. First numerical tests are performed.

Keywords: Expected Shortfall, ranking and selection, sequential design, Bayesian filter.

## 1 Introduction

The Basel Minimum Capital Requirements for Market Risk [[4](#bib.bib4)] has brought two main changes in the way that investment banks need to compute their capital requirements.
Expected Shortfall (ESES{\rm ES}) replaces Value at Risk (VaR) as the main risk indicator for the computation of capital requirements. The advantages of ES over VaR have been brought forward in Artzner et al. [[2](#bib.bib2)], and Expected Shortfall is now considered by most researchers and practitioners as superior to VaR as a risk measure, because it respects the sub-additivity axiom, see [[1](#bib.bib1), [2](#bib.bib2), [23](#bib.bib23)].
The second main change is that the number of required daily computations of ESES{\rm ES} has been multiplied by a factor of up to 90. Where banks used to need to compute one VaR per day, they now need to compute up to three ESES{\rm ES} per liquidity horizon and risk class, as well as three ESES{\rm ES} per liquidity horizon for all risk classes combined.
The above has triggered several works on the fast computation of ESES{\rm ES}.

Mathematically, if V𝑉V is a random variable modeling the level of loss555All over this paper, we measure the performances in terms of losses. A positive number is a loss, a negative number is a gain. of a portfolio that will be known at a future time, and 0<α<10𝛼10<\alpha<1, the expected shortfall of level α∈(0,1)𝛼01\alpha\in(0,1) is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESα:=1α​∫0αVaRγ​(V)​𝑑γ,assignsubscriptES𝛼1𝛼superscriptsubscript0𝛼subscriptVaR𝛾𝑉differential-d𝛾{\rm ES}\_{\alpha}:=\frac{1}{\alpha}\int\_{0}^{\alpha}{\rm VaR}\_{\gamma}({V})d\gamma, |  | (1) |

where VaRγsubscriptVaR𝛾{\rm VaR}\_{\gamma} is the Value at Risk at level γ𝛾\gamma, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRγ​(V):=max⁡{x∈ℝ:ℙ​[V≥x]>γ}.assignsubscriptVaR𝛾𝑉:𝑥ℝℙdelimited-[]𝑉𝑥𝛾{\rm VaR}\_{\gamma}\left({V}\right):={\max\left\{x\in\mathbb{R}:{\mathbb{P}}[V\geq x]>\gamma\right\}}. |  | (2) |

Nearly all of the literature concentrates on studying the ESES{\rm ES} by using parametric, non-parametric or semi-parametric approaches to approximate the distribution of V𝑉{V} based on historical data. See in particular [[9](#bib.bib9), [11](#bib.bib11), [12](#bib.bib12), [15](#bib.bib15), [16](#bib.bib16), [19](#bib.bib19), [20](#bib.bib20), [21](#bib.bib21), [24](#bib.bib24), [25](#bib.bib25), [26](#bib.bib26), [27](#bib.bib27)]. Another approach consists in using the fact that V𝑉V is the risk neutral value of a book, and therefore of the form 𝔼​[P|S]𝔼delimited-[]conditional𝑃𝑆\mathbb{E}[P|S] in which S𝑆S is a random variable associated to market parameters and P𝑃P represents the future (discounted) payoffs of the book. This suggests using a nested Monte Carlo approach : simulate a set of values in the distribution of S𝑆S (outer scenarios), and, for each simulation of S𝑆S, compute a Monte Carlo estimator of 𝔼​[P|S]𝔼delimited-[]conditional𝑃𝑆{\mathbb{E}}[P|S] by using simulations in the conditional distribution (inner scenarios). This is for instance the approach of [[8](#bib.bib8), [13](#bib.bib13)].

But, as defined in the regulatory document of Basel [[4](#bib.bib4)], the expected shortfall is based on ns=253subscript𝑛𝑠253n\_{s}=253 scenarios of market parameters s=(si)i≤nsssubscriptsuperscripts𝑖𝑖subscript𝑛𝑠{\rm s}=({\rm s}^{i})\_{i\leq n\_{s}} that are generated in a deterministic way. Therefore, S𝑆S is just uniformly distributed in the sequence ss{\rm s} and there is no need for simulating outer scenarios. Since V𝑉V is defined by a pricing formula 𝔼​[P|S]𝔼delimited-[]conditional𝑃𝑆\mathbb{E}[P|S] that is fully described by the value of S𝑆S, there is also no room for approximating the law of V𝑉V based on historical data, if we are only interested by the requirements of [[4](#bib.bib4)].
The only issue is to compute in an efficient way the loss impacts (μi)i≤nssubscriptsuperscript𝜇𝑖𝑖subscript𝑛𝑠(\mu^{i})\_{i\leq n\_{s}} of the book,

|  |  |  |
| --- | --- | --- |
|  | μi:=(𝔼​[P|S=si]−𝔼​[P|S=s0]),i=1​…,ns,formulae-sequenceassignsuperscript𝜇𝑖𝔼delimited-[]conditional𝑃𝑆superscripts𝑖𝔼delimited-[]conditional𝑃𝑆superscripts0𝑖  1…subscript𝑛𝑠\mu^{i}:=\left(\mathbb{E}[P|S={\rm s}^{i}]-\mathbb{E}[P|S={\rm s}^{0}]\right),\;i=1\ldots,n\_{s}, |  |

in which s0superscripts0{\rm s}^{0} is the current value of the market parameters, and then compute the average over the nw=6subscript𝑛𝑤6n\_{w}=6 worst impacts, say

|  |  |  |  |
| --- | --- | --- | --- |
|  | ES=1nw​∑i=1nwμi,ES1subscript𝑛𝑤superscriptsubscript𝑖1subscript𝑛𝑤superscript𝜇𝑖{\rm ES}=\frac{1}{n\_{w}}\sum\_{i=1}^{n\_{w}}\mu^{i}, |  | (3) |

if, for ease of notations, we assume that

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ1≥μ2≥⋯≥μns−1≥μns.superscript𝜇1superscript𝜇2⋯superscript𝜇subscript𝑛𝑠1superscript𝜇subscript𝑛𝑠\mu^{1}\geq\mu^{2}\geq\cdots\geq\mu^{n\_{s}-1}\geq\mu^{n\_{s}}. |  | (4) |

Methods that are in line with the above have also been studied, in particular in [[17](#bib.bib17), [22](#bib.bib22)] in which the authors define a distance on the space of scenarios induced by the distance between their risk factors. Starting with the original outer-level scenarios (called “prediction points”), they determine “design points” that are included in their convex hull. Inner-level paths are simulated in order to evaluate the portfolio value at the design points. These values are then used to establish a metamodel of the portfolio price with respect to the risk factors, and this metamodel is then used to select among the prediction points those that are most likely to be part of the worst scenarios set. They are then added to the design points, and evaluated by using inner-level simulations, after which the metamodel is updated.

These methods are very smart but neglect one important point for practitioners: the cost of launching a pricer is high, as it typically entails instanciating thousands of objects at initialization, as well as volatility surface calibrations and sometimes even graphical interfaces. Furthermore, these pricers usually do not have the flexibility to add dynamically, at each inner-level pricing, new paths to a given scenario. Therefore, we do not allow ourselves to adapt our strategies at such a level of granularity.

Instead, we will consider strategies that only entail L𝐿L-levels of sets of simulations, where L𝐿L is typically quite low, so as not to pay too many times the overhead of launching the pricer and/or calibrating the required volatility surfaces.
We also do not use any concept of distance between scenarios induced by their risk factors. Although this enables [[17](#bib.bib17)] and [[22](#bib.bib22)] to obtain better empirical convergence rates, we see at least one problem with this approach: at the scale of a bank, the space of risk factors is both of a very high dimension (a few thousands) and with a very complex geometry (the payoffs of the portfolio’s derivative products are usually non-convex, and path-dependent), so that it is very difficult to establish a model describing the proximity of scenarios in a robust way.

We thus study a relatively simple procedure that also has the advantage of allowing us to establish non-asymptotic bounds on the 𝕃psuperscript𝕃𝑝\mathbb{L}^{p}-error of our estimator, in the spirit of the simplest ranking by mean procedures, see e.g. [[3](#bib.bib3), [5](#bib.bib5), [6](#bib.bib6), [14](#bib.bib14)]. It consists in using a first set of simulated paths to provide a crude estimation of the impact factors μisuperscript𝜇𝑖\mu^{i}. These first estimators are ranked to select the q1<nssubscript𝑞1subscript𝑛𝑠q\_{1}<n\_{s} outer-level scenarios with the highest estimated impact values. Then, only the impact values of these q1subscript𝑞1q\_{1} pre-selected scenarios are estimated again by using the previous estimators together with a new set of simulated paths. Among these new estimators we select the scenarios with the q2<q1subscript𝑞2subscript𝑞1q\_{2}<q\_{1} highest estimated impact factors. And so on. After L≥2𝐿2L\geq 2 steps, L𝐿L being small in practice, we just keep the mean of the six highest estimated impacts.

The rationale behind this is that a first crude estimation should be sufficient to rule out a large part of the scenarios from the candidates of being in the 666 worst ones, because the corresponding values should be far enough. While the number of candidates reduces, one can expect that the differences between the corresponding impacts diminish as well and that more Monte Carlo simulations are needed to differentiate them. Under an indifference zone hypothesis, similar to the one used in the above mentioned paper, and a sub-gamma distribution assumption, the convergence is exponential in the number of simulations used at the different steps and of order 1/2121/2 in the total number of simulations. See Proposition [2.2](#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") and Corollary [2.3](#S2.Thmtheorem3 "Corollary 2.3. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") below.

The optimal number of additional paths that should be used at each step to minimize the strong estimation error, given a maximal computational cost, can be determined by a simple dynamic programming algorithm, that can be solved off-line, see Section [2.4](#S2.SS4 "2.4 Optimal a-priori allocation by deterministic dynamic programming based on fixed a-priori bounds ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios"). In theory, this requires the a priori knowledge of the means and covariances of our estimators, which are obviously not known in practice. However, one can easily define a version based on a robust specification of the error. One can also take advantage of the different simulation sets to improve our prior on the true hidden parameters. This leads to a natural adaptative algorithm, see Section [3](#S3 "3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), for which convergence is also proved, see Proposition [3.3](#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.1 Error bounds and convergence for predictable strategies ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios"). Estimating the optimal policy associated to this adaptative algorithm is costly but can be done off-line by using a neural network approximation combined with a backward dynamic programming algorithm. We explain how this can be done in Section [3.3](#S3.SS3 "3.3 Example of numerical implementation using neural networks ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios") (further details are in Appendix [B](#A2 "Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios")).

The rest of the paper is organized as follows. Section [2](#S2 "2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") is dedicated to the most naive deterministic algorithm. In particular, Section [2.5](#S2.SS5 "2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") gives a very easy to use two levels algorithm for the case where the impacts decrease linearly in the scenarios’ rank order. The adaptative version of the algorithm is presented in Section [3](#S3 "3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios"). Finally, we perform first numerical tests in Section [4](#S4 "4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios").

## 2 Algorithm with a deterministic effort allocation

In this section, we describe the simplest version of the algorithm. It uses a pre-defined deterministic number of simulations. We establish a strong 𝕃psuperscript𝕃𝑝{\mathbb{L}}^{p}-error bound and discuss several ways of choosing the optimal strategy for minimizing this error.

### 2.1 The algorithm

From now on, we assume that 𝔼​[P|S=s0]𝔼delimited-[]conditional𝑃𝑆superscripts0{\mathbb{E}}[P|S={\rm s}^{0}] is known perfectly and set it to 00 for ease of notations. As explained above, the algorithm relies on the idea of selecting progressively the scenarios that will be used for the computation of the Expected Shortfall. Namely, let P|s:=(P|si)i≤nsP\_{|\rm s}:=(P\_{|\rm s^{i}})\_{i\leq n\_{s}} be a nssubscript𝑛𝑠n\_{s}-dimensional random variable such that each P|siP\_{|{\rm s}^{i}} has the law of P𝑃P given S=si𝑆superscripts𝑖S={\rm s}^{i}.
We first simulate independent copies (Pj1,…,Pjns)j≥1subscriptsuperscriptsubscript𝑃𝑗1…superscriptsubscript𝑃𝑗subscript𝑛𝑠𝑗1(P\_{j}^{1},\ldots,P\_{j}^{n\_{s}})\_{j\geq 1} of P|sP\_{|\rm s} and compute the Monte Carlo estimators of 𝔼​[P|S=si]𝔼delimited-[]conditional𝑃𝑆superscripts𝑖{\mathbb{E}}[P|S={\rm s}^{i}], i≤ns𝑖subscript𝑛𝑠i\leq n\_{s}:

|  |  |  |
| --- | --- | --- |
|  | μ^1i:=1N1​∑j=1N1Pji​ for ​i≤ns,assignsubscriptsuperscript^𝜇𝑖11subscript𝑁1superscriptsubscript𝑗1subscript𝑁1superscriptsubscript𝑃𝑗𝑖 for 𝑖subscript𝑛𝑠\hat{\mu}^{i}\_{1}:=\frac{1}{N\_{1}}\sum\_{j=1}^{N\_{1}}P\_{j}^{i}\;\mbox{ for }i\leq n\_{s}, |  |

for some N1≥1subscript𝑁11N\_{1}\geq 1.
Among these random variables, we then select the ones that are the most likely to coincide with the worst scenarios s1,…,snw

superscripts1…superscriptssubscript𝑛𝑤{\rm s}^{1},\ldots,{\rm s}^{n\_{w}}, for some 1≤nw<ns1subscript𝑛𝑤subscript𝑛𝑠1\leq n\_{w}<n\_{s}.
To do this, one considers the (random) permutation 𝔪1subscript𝔪1{\mathfrak{m}}\_{1} on [[1,ns]]delimited-[]1subscript𝑛𝑠[\![1,n\_{s}]\!] such that the components of (μ^1𝔪1​(i))i≤nssubscriptsuperscriptsubscript^𝜇1subscript𝔪1𝑖𝑖subscript𝑛𝑠\left(\hat{\mu}\_{1}^{{\mathfrak{m}}\_{1}(i)}\right)\_{i\leq n\_{s}} are in decreasing order:

|  |  |  |
| --- | --- | --- |
|  | {μ^1𝔪1​(1)≥μ^1𝔪1​(2)≥…≥μ^1𝔪1​(ns),𝔪1​(i)<𝔪1​(i′)​ if ​μ^1𝔪1​(i)=μ^1𝔪1​(i′)​ for ​1≤i<i′≤ns,casessuperscriptsubscript^𝜇1subscript𝔪11superscriptsubscript^𝜇1subscript𝔪12…superscriptsubscript^𝜇1subscript𝔪1subscript𝑛𝑠subscript𝔪1𝑖subscript𝔪1superscript𝑖′ if superscriptsubscript^𝜇1subscript𝔪1𝑖superscriptsubscript^𝜇1subscript𝔪1superscript𝑖′ for 1𝑖superscript𝑖′subscript𝑛𝑠\left\{\begin{array}[]{l}\hat{\mu}\_{1}^{{\mathfrak{m}}\_{1}(1)}\geq\hat{\mu}\_{1}^{{\mathfrak{m}}\_{1}(2)}\geq\ldots\geq\hat{\mu}\_{1}^{{\mathfrak{m}}\_{1}(n\_{s})},\\ {\mathfrak{m}}\_{1}(i)<{\mathfrak{m}}\_{1}(i^{\prime})\;\mbox{ if }\hat{\mu}\_{1}^{{\mathfrak{m}}\_{1}(i)}=\hat{\mu}\_{1}^{{\mathfrak{m}}\_{1}(i^{\prime})}\mbox{ for }1\leq i<i^{\prime}\leq n\_{s},\end{array}\right. |  |

and only keep the indexes (𝔪1​(ℓ))ℓ≤q1subscriptsubscript𝔪1ℓℓsubscript𝑞1({\mathfrak{m}}\_{1}(\ell))\_{\ell\leq q\_{1}} of the corresponding q1≥nwsubscript𝑞1subscript𝑛𝑤q\_{1}\geq n\_{w} highest values, i.e. the indexes belonging to

|  |  |  |
| --- | --- | --- |
|  | ℑ1:=ℑ0∩𝔪1​([[1,q1]])​ in which ​ℑ0:=[[1,ns]].assignsubscriptℑ1subscriptℑ0subscript𝔪1delimited-[]1subscript𝑞1 in which subscriptℑ0assigndelimited-[]1subscript𝑛𝑠{\mathfrak{I}}\_{1}:={\mathfrak{I}}\_{0}\cap{\mathfrak{m}}\_{1}([\![1,q\_{1}]\!])\;\mbox{ in which }{\mathfrak{I}}\_{0}:=[\![1,n\_{s}]\!]. |  |

We then iterate the above procedure on the scenarios in ℑ1subscriptℑ1{\mathfrak{I}}\_{1} and so on. Namely, we fix L≥1𝐿1L\geq 1 different thresholds (qℓ)ℓ=0,…,L−1subscriptsubscript𝑞ℓℓ

0…𝐿1(q\_{\ell})\_{\ell=0,\ldots,L{-1}} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | nw=:qL−1≤⋯≤q0:=ns.\displaystyle{n\_{w}=:q\_{L-1}}{\leq}\cdots{\leq}q\_{0}:=n\_{s}. |  | (5) |

Assuming that ℑℓ−1subscriptℑℓ1{\mathfrak{I}}\_{\ell-1} is given, for some 1≤ℓ−1≤L−11ℓ1𝐿11\leq\ell-1\leq L-{1}, we compute the estimators666Note from the considerations below that only the elements (μ^ℓi)i∈ℑℓ−1subscriptsubscriptsuperscript^𝜇𝑖ℓ𝑖subscriptℑℓ1(\hat{\mu}^{i}\_{\ell})\_{i\in{\mathfrak{I}}\_{\ell-1}} are needed in practice, the others are only defined here because they will be used in our proofs.

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ^ℓi:=1Nℓ​∑j=1NℓPji​ for ​i≤ns,assignsubscriptsuperscript^𝜇𝑖ℓ1subscript𝑁ℓsuperscriptsubscript𝑗1subscript𝑁ℓsuperscriptsubscript𝑃𝑗𝑖 for 𝑖subscript𝑛𝑠\hat{\mu}^{i}\_{\ell}:=\frac{1}{N\_{\ell}}\sum\_{j=1}^{N\_{\ell}}P\_{j}^{i}\;\mbox{ for }i\leq n\_{s}, |  | (6) |

for some Nℓ≥Nℓ−1subscript𝑁ℓsubscript𝑁ℓ1N\_{\ell}\geq N\_{\ell-1}.
If ℓ≤L−1ℓ𝐿1\ell\leq L-1, we consider the (random) permutation 𝔪ℓ:[[1,qℓ−1]]↦ℑℓ−1:subscript𝔪ℓmaps-todelimited-[]1subscript𝑞ℓ1subscriptℑℓ1{\mathfrak{m}}\_{\ell}:[\![1,q\_{\ell-1}]\!]\mapsto{\mathfrak{I}}\_{\ell-1} such that the components of (μ^ℓi)i∈ℑℓ−1subscriptsuperscriptsubscript^𝜇ℓ𝑖𝑖subscriptℑℓ1\left(\hat{\mu}\_{\ell}^{i}\right)\_{i\in{\mathfrak{I}}\_{\ell-1}} are in decreasing order

|  |  |  |  |
| --- | --- | --- | --- |
|  | {μ^ℓ𝔪ℓ​(1)≥μ^ℓ𝔪ℓ​(2)≥…≥μ^ℓ𝔪ℓ​(qℓ−1),𝔪ℓ​(i)<𝔪ℓ​(i′)​ if ​μ^ℓ𝔪ℓ​(i)=μ^ℓ𝔪ℓ​(i′)​ for ​1≤i<i′≤ns,casessuperscriptsubscript^𝜇ℓsubscript𝔪ℓ1superscriptsubscript^𝜇ℓsubscript𝔪ℓ2…superscriptsubscript^𝜇ℓsubscript𝔪ℓsubscript𝑞ℓ1subscript𝔪ℓ𝑖subscript𝔪ℓsuperscript𝑖′ if superscriptsubscript^𝜇ℓsubscript𝔪ℓ𝑖superscriptsubscript^𝜇ℓsubscript𝔪ℓsuperscript𝑖′ for 1𝑖superscript𝑖′subscript𝑛𝑠\left\{\begin{array}[]{l}\hat{\mu}\_{\ell}^{{\mathfrak{m}}\_{\ell}(1)}\geq\hat{\mu}\_{\ell}^{{\mathfrak{m}}\_{\ell}(2)}\geq\ldots\geq\hat{\mu}\_{\ell}^{{\mathfrak{m}}\_{\ell}(q\_{\ell-1})},\\ {\mathfrak{m}}\_{\ell}(i)<{\mathfrak{m}}\_{\ell}(i^{\prime})\;\mbox{ if }\hat{\mu}\_{\ell}^{{\mathfrak{m}}\_{\ell}(i)}=\hat{\mu}\_{\ell}^{{\mathfrak{m}}\_{\ell}(i^{\prime})}\mbox{ for }1\leq i<i^{\prime}\leq n\_{s},\end{array}\right. |  | (7) |

and only keep the elements in

|  |  |  |
| --- | --- | --- |
|  | ℑℓ:=ℑℓ−1∩𝔪ℓ​([[1,qℓ]])assignsubscriptℑℓsubscriptℑℓ1subscript𝔪ℓdelimited-[]1subscript𝑞ℓ{\mathfrak{I}}\_{\ell}:={\mathfrak{I}}\_{\ell-1}\cap{\mathfrak{m}}\_{\ell}([\![1,q\_{\ell}]\!]) |  |

for the next step. If ℓ=Lℓ𝐿\ell=L, we just compute the final estimator of the ESES{\rm ES} given by

|  |  |  |
| --- | --- | --- |
|  | ES^:=1nw​∑i=1nwμ^L𝔪L−1​(i)=1nw​∑i∈ℑL−1μ^Li.assign^ES1subscript𝑛𝑤superscriptsubscript𝑖1subscript𝑛𝑤superscriptsubscript^𝜇𝐿subscript𝔪𝐿1𝑖1subscript𝑛𝑤subscript𝑖subscriptℑ𝐿1superscriptsubscript^𝜇𝐿𝑖\widehat{\rm ES}:=\frac{1}{n\_{w}}\sum\_{i=1}^{n\_{w}}\hat{\mu}\_{L}^{{\mathfrak{m}}\_{{L-1}}(i)}=\frac{1}{n\_{w}}\sum\_{i\in{\mathfrak{I}}\_{{L-1}}}\hat{\mu}\_{L}^{i}. |  |

Note that only the L−1𝐿1L-1-first steps are used to select the worth scenarios, the step L𝐿L is a pure Monte Carlo step. Again, the general idea is to reduce little by little the number of candidate scenarios to be part of the worst ones. As the number of candidates diminishes, one increases the number of simulated paths so as to reduce the variance of our Monte Carlo estimators and be able to differentiate between potentially closer true values of the associated conditional expectations.

###### Remark 2.1.

Note that, given j𝑗j, we do not assume that the Pjisubscriptsuperscript𝑃𝑖𝑗P^{i}\_{j}, i≤ns𝑖subscript𝑛𝑠i\leq n\_{s}, are independent. The simulations associated to different scenarios are in general not independent. Moreover, the μ^ℓisubscriptsuperscript^𝜇𝑖ℓ\hat{\mu}^{i}\_{\ell}, ℓ≤Lℓ𝐿\ell\leq L, use the same simulated paths, only the number of used simulations changes. Both permit to reduce the computational cost, by allowing the use of the same simulations of the underlying processes across scenarios and steps.

### 2.2 General a-priori bound on the 𝕃psuperscript𝕃𝑝{\mathbb{L}}^{p} error

In this section, we first provide a general 𝕃psuperscript𝕃𝑝{\mathbb{L}}^{p} estimate of the error. A more tractable formulation will be provided in Corollary [2.3](#S2.Thmtheorem3 "Corollary 2.3. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") under an additional sub-gamma distribution assumption.

From now on, we assume that P|s∈𝕃pP\_{|{\rm s}}\in{\mathbb{L}}^{p} for all p≥1𝑝1p\geq 1, and we use the notations777The element qLsubscript𝑞𝐿q\_{L} and N0subscript𝑁0N\_{0} are defined for notational convenience, they never appear in our algorithm. To fix ideas, they can be set to qL=nwsubscript𝑞𝐿subscript𝑛𝑤q\_{L}=n\_{w} and N0=0subscript𝑁00N\_{0}=0 all over this paper.

|  |  |  |
| --- | --- | --- |
|  | q:=(q0,q1,…,qL)​ , ​N=(N0,N1,…,NL)assign𝑞subscript𝑞0subscript𝑞1…subscript𝑞𝐿 , 𝑁subscript𝑁0subscript𝑁1…subscript𝑁𝐿\displaystyle q:=({q\_{0}},q\_{1},\ldots,q\_{{L}})\;\mbox{ , }\;N=(N\_{0},N\_{1},\ldots,N\_{L}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​qℓ:=qℓ−1−qℓ​ and ​δ​Nℓ:=Nℓ−Nℓ−1​, for ​1≤ℓ≤L,assign𝛿subscript𝑞ℓsubscript𝑞ℓ1subscript𝑞ℓ and 𝛿subscript𝑁ℓassignsubscript𝑁ℓsubscript𝑁ℓ1, for 1ℓ𝐿\displaystyle\delta q\_{\ell}:=q\_{\ell-1}-q\_{\ell}\;\mbox{ and }\;\delta N\_{\ell}:=N\_{\ell}-N\_{\ell-1}\mbox{, for }1\leq\ell\leq L, |  | (8) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​μ^ℓi:=∑j=Nℓ−1+1NℓPjiδ​Nℓ=Nℓ​μ^ℓi−Nℓ−1​μ^ℓ−1iδ​Nℓ, for 1≤i≤ns,formulae-sequenceassign𝛿subscriptsuperscript^𝜇𝑖ℓsuperscriptsubscript𝑗subscript𝑁ℓ11subscript𝑁ℓsubscriptsuperscript𝑃𝑖𝑗𝛿subscript𝑁ℓsubscript𝑁ℓsubscriptsuperscript^𝜇𝑖ℓsubscript𝑁ℓ1subscriptsuperscript^𝜇𝑖ℓ1𝛿subscript𝑁ℓ for 1≤i≤ns,\displaystyle\delta\hat{\mu}^{i}\_{\ell}:=\frac{\sum\_{j=N\_{\ell-1}+1}^{N\_{\ell}}P^{i}\_{j}}{\delta N\_{\ell}}=\frac{N\_{\ell}\hat{\mu}^{i}\_{\ell}-N\_{\ell-1}\hat{\mu}^{i}\_{\ell-1}}{\delta N\_{\ell}},\mbox{ for $1\leq i\leq n\_{s}$,} |  | (9) |

with the convention 0/0=00000/0=0.

###### Proposition 2.2.

For all p≥1𝑝1p\geq 1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|ES−ES^|p]1p≤𝔼superscriptdelimited-[]superscriptES^ES𝑝1𝑝absent\displaystyle\mathbb{E}\left[\left|{\rm ES}-\widehat{\rm ES}\right|^{p}\right]^{\frac{1}{p}}\leq | ∑ℓ=1L−1(δ​qℓ)1p​max(i,k)∈[[1,nw]]×[[qℓ+1,ns]]⁡(μi−μk)​ℙ​[μ^ℓk>μ^ℓi]1psuperscriptsubscriptℓ1𝐿1superscript𝛿subscript𝑞ℓ1𝑝subscript𝑖𝑘delimited-[]1subscript𝑛𝑤delimited-[]subscript𝑞ℓ1subscript𝑛𝑠superscript𝜇𝑖superscript𝜇𝑘ℙsuperscriptdelimited-[]superscriptsubscript^𝜇ℓ𝑘superscriptsubscript^𝜇ℓ𝑖1𝑝\displaystyle\sum\_{\ell=1}^{L-1}(\delta q\_{\ell})^{\frac{1}{p}}\max\_{(i,k)\in[\![1,{n\_{w}}]\!]\times[\![q\_{\ell}+1,n\_{s}]\!]}(\mu^{i}-\mu^{k}){\mathbb{P}}[\hat{\mu}\_{\ell}^{k}>\hat{\mu}\_{\ell}^{i}]^{\frac{1}{p}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +1nw​δ​NLNL​max1≤i1<⋯<inw≤ns​(∑j=1nw𝔼​[|δ​μ^Lij−μij|p]1p)1subscript𝑛𝑤𝛿subscript𝑁𝐿subscript𝑁𝐿1subscript𝑖1⋯subscript𝑖subscript𝑛𝑤subscript𝑛𝑠superscriptsubscript𝑗1subscript𝑛𝑤𝔼superscriptdelimited-[]superscript𝛿subscriptsuperscript^𝜇subscript𝑖𝑗𝐿superscript𝜇subscript𝑖𝑗𝑝1𝑝\displaystyle+\frac{1}{n\_{w}}\frac{\delta N\_{L}}{N\_{L}}\underset{1\leq i\_{1}<\cdots<i\_{{n\_{w}}}\leq n\_{s}}{\max}\left(\sum\_{j=1}^{{n\_{w}}}{\mathbb{E}}\left[\left|\delta\hat{\mu}^{i\_{j}}\_{L}-\mu^{i\_{j}}\right|^{p}\right]^{\frac{1}{p}}\right) |  | (10) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1nw​NL−1NL​∑i=1ns𝔼​[|μ^L−1i−μi|p]1p.1subscript𝑛𝑤subscript𝑁𝐿1subscript𝑁𝐿superscriptsubscript𝑖1subscript𝑛𝑠𝔼superscriptdelimited-[]superscriptsuperscriptsubscript^𝜇𝐿1𝑖superscript𝜇𝑖𝑝1𝑝\displaystyle+\frac{1}{n\_{w}}\frac{N\_{L-1}}{N\_{L}}\sum\_{i=1}^{{n\_{s}}}{\mathbb{E}}\left[\left|\hat{\mu}\_{L-1}^{{i}}-\mu^{{i}}\right|^{p}\right]^{\frac{1}{p}}. |  |

Before providing the proof of this general estimate, let us make some comments. The last two terms in ([10](#S2.E10 "In Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")) are natural as they are due to the Monte Carlo error made on the estimation of the various conditional expectations that can enter, after the (L−1)𝐿1(L-1)-levels selection procedure, in the estimation of ESES{\rm ES}. Note that it corresponds to the estimation errors using the cumulated number of Monte Carlo simulations NL−1subscript𝑁𝐿1N\_{L-1} of step L−1𝐿1L-1 and the number NL−NL−1subscript𝑁𝐿subscript𝑁𝐿1N\_{L}-N\_{L-1} of simulations used only for the last step. In practice, these numbers should be sufficiently large. The first term involves the quantities max(i,k)∈[[1,nw]]×[[qℓ+1,ns]]⁡(μi−μk)​ℙ​[μ^ℓk>μ^ℓi]1psubscript𝑖𝑘delimited-[]1subscript𝑛𝑤delimited-[]subscript𝑞ℓ1subscript𝑛𝑠superscript𝜇𝑖superscript𝜇𝑘ℙsuperscriptdelimited-[]superscriptsubscript^𝜇ℓ𝑘superscriptsubscript^𝜇ℓ𝑖1𝑝\max\_{(i,k)\in[\![1,{n\_{w}}]\!]\times[\![q\_{\ell}+1,n\_{s}]\!]}(\mu^{i}-\mu^{k}){\mathbb{P}}[\hat{\mu}\_{\ell}^{k}>\hat{\mu}\_{\ell}^{i}]^{\frac{1}{p}} with ℓ=1,…,L−1ℓ

1…𝐿1\ell=1,\ldots,L-1. Each term corresponds to the situation in which an element i∈[[1,nw]]𝑖delimited-[]1subscript𝑛𝑤i\in[\![1,n\_{w}]\!] gets out the set of selected indexes ℑℓsubscriptℑℓ{\mathfrak{I}}\_{\ell} exactly at the ℓℓ\ell-th step. In the worst situation, it is replaced by an element of index k𝑘k larger than qℓsubscript𝑞ℓq\_{\ell} and this can happen only if μ^ℓk>μ^ℓisuperscriptsubscript^𝜇ℓ𝑘superscriptsubscript^𝜇ℓ𝑖\hat{\mu}\_{\ell}^{k}>\hat{\mu}\_{\ell}^{i}. The probability of this event is controlled by the number of Monte Carlo simulations Nℓsubscript𝑁ℓN\_{\ell} used at the step ℓℓ\ell but also by the distance between the two scenarios. More specifically, for ℓℓ\ell small, one expects that ℙ​[μ^ℓk>μ^ℓi]ℙdelimited-[]superscriptsubscript^𝜇ℓ𝑘superscriptsubscript^𝜇ℓ𝑖{\mathbb{P}}[\hat{\mu}\_{\ell}^{k}>\hat{\mu}\_{\ell}^{i}] is small because the law of P|skP\_{|{{\rm s}\_{k}}} is concentrated far away from where the law of P|siP\_{|{{\rm s}\_{i}}} is. This quantity potentially increases with ℓℓ\ell, as we reduce the number of selected indexes. This should be compensated by an increase in the number of used Monte Carlo simulations. Otherwise stated, we expect to balance the various terms of
([10](#S2.E10 "In Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")) by considering a suitable increasing sequence (Nℓ)ℓ≤Lsubscriptsubscript𝑁ℓℓ𝐿(N\_{\ell})\_{\ell\leq L}.

Obviously, ([10](#S2.E10 "In Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")) implies that the algorithm converges as Nℓ→∞→subscript𝑁ℓN\_{\ell}\to\infty for all ℓ≤Lℓ𝐿\ell\leq L, see Proposition [3.3](#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.1 Error bounds and convergence for predictable strategies ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios") below for a proof in a more general framework.

###### Proof of Proposition [2.2](#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios").

We split the error into a permutation and a Monte Carlo error:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[|ES−ES^|p]1p≤𝔼superscriptdelimited-[]superscriptES^ES𝑝1𝑝absent\displaystyle\mathbb{E}\left[\left|{\rm ES}-\widehat{\rm ES}\right|^{p}\right]^{\frac{1}{p}}\leq | 𝔼​[|1nw​∑i≤nwμi−μ𝔪L−1​(i)|p]1p+𝔼​[|1nw​∑i≤nwμ^L𝔪L−1​(i)−μ𝔪L−1​(i)|p]1p.𝔼superscriptdelimited-[]superscript1subscript𝑛𝑤subscript𝑖subscript𝑛𝑤superscript𝜇𝑖superscript𝜇subscript𝔪𝐿1𝑖𝑝1𝑝𝔼superscriptdelimited-[]superscript1subscript𝑛𝑤subscript𝑖subscript𝑛𝑤superscriptsubscript^𝜇𝐿subscript𝔪𝐿1𝑖superscript𝜇subscript𝔪𝐿1𝑖𝑝1𝑝\displaystyle{\mathbb{E}}\left[\left|\frac{1}{n\_{w}}\sum\_{i\leq n\_{w}}\mu^{i}-\mu^{{\mathfrak{m}}\_{L-1}(i)}\right|^{p}\right]^{\frac{1}{p}}+{\mathbb{E}}\left[\left|\frac{1}{n\_{w}}\sum\_{i\leq n\_{w}}\hat{\mu}\_{L}^{{\mathfrak{m}}\_{L-1}(i)}-\mu^{{\mathfrak{m}}\_{L-1}(i)}\right|^{p}\right]^{\frac{1}{p}}. |  | (11) |

Let us first look at the second term which corresponds to a Monte Carlo error. We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|1nw​∑i≤nwμ^L𝔪L−1​(i)−μ𝔪L−1​(i)|p]1p≤𝔼superscriptdelimited-[]superscript1subscript𝑛𝑤subscript𝑖subscript𝑛𝑤superscriptsubscript^𝜇𝐿subscript𝔪𝐿1𝑖superscript𝜇subscript𝔪𝐿1𝑖𝑝1𝑝absent\displaystyle{\mathbb{E}}\left[\left|\frac{1}{n\_{w}}\sum\_{i\leq n\_{w}}\hat{\mu}\_{L}^{{\mathfrak{m}}\_{L-1}(i)}-\mu^{{\mathfrak{m}}\_{L-1}(i)}\right|^{p}\right]^{\frac{1}{p}}\leq | NL−1NL​1nw​𝔼​[|∑i≤nwμ^L−1𝔪L−1​(i)−μ𝔪L−1​(i)|p]1psubscript𝑁𝐿1subscript𝑁𝐿1subscript𝑛𝑤𝔼superscriptdelimited-[]superscriptsubscript𝑖subscript𝑛𝑤superscriptsubscript^𝜇𝐿1subscript𝔪𝐿1𝑖superscript𝜇subscript𝔪𝐿1𝑖𝑝1𝑝\displaystyle\frac{N\_{L-1}}{N\_{L}}\frac{1}{n\_{w}}{\mathbb{E}}\left[\left|\sum\_{i\leq n\_{w}}\hat{\mu}\_{L-1}^{{\mathfrak{m}}\_{L-1}(i)}-\mu^{{\mathfrak{m}}\_{L-1}(i)}\right|^{p}\right]^{\frac{1}{p}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +NL−NL−1NL​1nw​𝔼​[|∑i≤nw∑j=NL−1+1NLP^j𝔪L−1​(i)NL−NL−1−μ𝔪L−1​(i)|p]1psubscript𝑁𝐿subscript𝑁𝐿1subscript𝑁𝐿1subscript𝑛𝑤𝔼superscriptdelimited-[]superscriptsubscript𝑖subscript𝑛𝑤superscriptsubscript𝑗subscript𝑁𝐿11subscript𝑁𝐿superscriptsubscript^𝑃𝑗subscript𝔪𝐿1𝑖subscript𝑁𝐿subscript𝑁𝐿1superscript𝜇subscript𝔪𝐿1𝑖𝑝1𝑝\displaystyle+\frac{N\_{L}-N\_{L-1}}{N\_{L}}\frac{1}{n\_{w}}{\mathbb{E}}\left[\left|\sum\_{i\leq n\_{w}}\frac{\sum\_{j=N\_{L-1}+1}^{N\_{L}}\hat{P}\_{j}^{{\mathfrak{m}}\_{L-1}(i)}}{N\_{L}-N\_{L-1}}-\mu^{{\mathfrak{m}}\_{L-1}(i)}\right|^{p}\right]^{\frac{1}{p}} |  |

in which

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|∑i≤nwμ^L−1𝔪L−1​(i)−μ𝔪L−1​(i)|p]1p𝔼superscriptdelimited-[]superscriptsubscript𝑖subscript𝑛𝑤superscriptsubscript^𝜇𝐿1subscript𝔪𝐿1𝑖superscript𝜇subscript𝔪𝐿1𝑖𝑝1𝑝\displaystyle{\mathbb{E}}\left[\left|\sum\_{i\leq n\_{w}}\hat{\mu}\_{L-1}^{{\mathfrak{m}}\_{L-1}(i)}-\mu^{{\mathfrak{m}}\_{L-1}(i)}\right|^{p}\right]^{\frac{1}{p}} | ≤∑i≤ns𝔼​[|μ^L−1i−μi|p]1p,absentsubscript𝑖subscript𝑛𝑠𝔼superscriptdelimited-[]superscriptsuperscriptsubscript^𝜇𝐿1𝑖superscript𝜇𝑖𝑝1𝑝\displaystyle\leq\sum\_{i\leq n\_{s}}{\mathbb{E}}\left[\left|\hat{\mu}\_{L-1}^{i}-\mu^{i}\right|^{p}\right]^{\frac{1}{p}}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|∑i≤nw∑j=NL−1+1NLP^j𝔪L−1​(i)NL−NL−1−μ𝔪L−1​(i)|p]1p=𝔼[𝔼[|∑i≤nwδμ^L𝔪L−1​(i)−μ𝔪L−1​(i)|p|𝔪L−1]]1p≤(max1≤i1<…<inw≤ns​𝔼​[|∑j=1nwδ​μ^Lij−μij|p])1p≤max1≤i1<…<inw≤ns​∑j=1nw𝔼​[|δ​μ^Lij−μij|p]1p.\begin{split}{\mathbb{E}}\left[\left|\sum\_{i\leq n\_{w}}\frac{\sum\_{j=N\_{L-1}+1}^{N\_{L}}\hat{P}\_{j}^{{\mathfrak{m}}\_{L-1}(i)}}{N\_{L}-N\_{L-1}}-\mu^{{\mathfrak{m}}\_{L-1}(i)}\right|^{p}\right]^{\frac{1}{p}}&={\mathbb{E}}\left[{\mathbb{E}}\left[\left|\sum\_{i\leq n\_{w}}\delta\hat{\mu}\_{L}^{{\mathfrak{m}}\_{L-1}(i)}-\mu^{{\mathfrak{m}}\_{L-1}(i)}\right|^{p}\middle|{\mathfrak{m}}\_{L-1}\right]\right]^{\frac{1}{p}}\\ &\leq\left(\underset{1\leq i\_{1}<...<i\_{n\_{w}}\leq n\_{s}}{\max}{\mathbb{E}}\left[\left|\sum\_{j=1}^{n\_{w}}\delta\hat{\mu}\_{L}^{i\_{j}}-\mu^{i\_{j}}\right|^{p}\right]\right)^{\frac{1}{p}}\\ &\leq\underset{1\leq i\_{1}<...<i\_{n\_{w}}\leq n\_{s}}{\max}\sum\_{j=1}^{n\_{w}}{\mathbb{E}}\left[\left|\delta\hat{\mu}\_{L}^{i\_{j}}-\mu^{i\_{j}}\right|^{p}\right]^{\frac{1}{p}}.\end{split} |  |

To discuss the first term in the right-hand side of ([11](#S2.E11 "In Proof of Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")), the permutation error, let us first define Sq​[A]subscriptS𝑞delimited-[]𝐴{\rm S}\_{q}[A] as the collection of the q𝑞q smallest elements of a set A⊂ℕ𝐴ℕA\subset{\mathbb{N}}. If i∈[[1,nw]]∩ℑℓ−1∖ℑℓ𝑖delimited-[]1subscript𝑛𝑤subscriptℑℓ1subscriptℑℓi\in[\![1,n\_{w}]\!]\cap{\mathfrak{I}}\_{\ell-1}\setminus{\mathfrak{I}}\_{\ell}, then i∈Sqℓ​[ℑℓ−1]∖ℑℓ𝑖subscriptSsubscript𝑞ℓdelimited-[]subscriptℑℓ1subscriptℑℓi\in{\rm S}\_{q\_{\ell}}[{\mathfrak{I}}\_{\ell-1}]\setminus{\mathfrak{I}}\_{\ell} and therefore there exists ki∈ℛℓ:=ℑℓ∖Sqℓ​[ℑℓ−1]subscript𝑘𝑖subscriptℛℓassignsubscriptℑℓsubscriptSsubscript𝑞ℓdelimited-[]subscriptℑℓ1k\_{i}\in{\mathcal{R}\_{\ell}}:={\mathfrak{I}}\_{\ell}\setminus{\rm S}\_{q\_{\ell}}[{\mathfrak{I}}\_{\ell-1}]. Thus, on the set {{i1,…,iJ}=(ℑℓ−1∖ℑℓ)∩[[1,nw]]}subscript𝑖1…subscript𝑖𝐽subscriptℑℓ1subscriptℑℓdelimited-[]1subscript𝑛𝑤\{\{i\_{1},\ldots,i\_{J}\}=({\mathfrak{I}}\_{\ell-1}\setminus{\mathfrak{I}}\_{\ell})\cap[\![1,n\_{w}]\!]\}, one can define
𝔨ℓ​(i1):=max⁡ℛℓassignsubscript𝔨ℓsubscript𝑖1subscriptℛℓ{\mathfrak{k}}\_{\ell}(i\_{1}):=\max{\mathcal{R}\_{\ell}}
and 𝔨ℓ​(ij+1):=max⁡{k<𝔨ℓ​(ij):k∈ℛℓ}assignsubscript𝔨ℓsubscript𝑖𝑗1:𝑘subscript𝔨ℓsubscript𝑖𝑗𝑘subscriptℛℓ{\mathfrak{k}}\_{\ell}(i\_{j+1}):=\max\{k<{\mathfrak{k}}\_{\ell}(i\_{j})\leavevmode\nobreak\ :\leavevmode\nobreak\ k\in{\mathcal{R}\_{\ell}}\} for j+1≤J𝑗1𝐽j+1\leq J. Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | {i∈ℑℓ−1∖ℑℓ}⊂{μ^ℓ𝔨ℓ​(i)>μ^ℓi}​ and ​|ℛℓ|≤qℓ−1−qℓ,𝑖subscriptℑℓ1subscriptℑℓsuperscriptsubscript^𝜇ℓsubscript𝔨ℓ𝑖superscriptsubscript^𝜇ℓ𝑖 and subscriptℛℓsubscript𝑞ℓ1subscript𝑞ℓ\displaystyle\{i\in{\mathfrak{I}}\_{\ell-1}\setminus{\mathfrak{I}}\_{\ell}\}\subset\{\hat{\mu}\_{\ell}^{{\mathfrak{k}}\_{\ell}(i)}>\hat{\mu}\_{\ell}^{i}\}\;\mbox{ and }\;|{\mathcal{R}\_{\ell}}|\leq q\_{\ell-1}-q\_{\ell}, |  | (12) |

since ℛℓ⊂ℑℓ−1∖Sqℓ​[ℑℓ−1]subscriptℛℓsubscriptℑℓ1subscriptSsubscript𝑞ℓdelimited-[]subscriptℑℓ1{\mathcal{R}\_{\ell}}\subset{\mathfrak{I}}\_{\ell-1}\setminus{\rm S}\_{q\_{\ell}}[{\mathfrak{I}}\_{\ell-1}] and |ℑℓ−1|=qℓ−1subscriptℑℓ1subscript𝑞ℓ1|{\mathfrak{I}}\_{\ell-1}|=q\_{\ell-1}. Let 𝐀q,q′subscript𝐀

𝑞superscript𝑞′{\mathbf{A}}\_{q,q^{\prime}} denote the collection of subsets A𝐴A of [[q+1,ns]]delimited-[]𝑞1subscript𝑛𝑠[\![q+1,n\_{s}]\!] such that |A|=q′𝐴superscript𝑞′|A|=q^{\prime}.
Then, it follows from ([4](#S1.E4 "In 1 Introduction ‣ Computation of Expected Shortfall by fast detection of worst scenarios")), Hölder’s inequality and ([12](#S2.E12 "In Proof of Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")) that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|1nw​∑i≤nwμi−μ𝔪L−1​(i)|p]1p≤1nw​∑i≤nw∑ℓ=1L−1𝔼​[|(μi−μ𝔨ℓ​(i))​𝟏{i∈ℑℓ−1∖ℑℓ}|p]1p≤maxi≤nw​∑ℓ=1L−1𝔼​[|(μi−μ𝔨ℓ​(i))​𝟏{i∈ℑℓ−1∖ℑℓ}|p]1p≤maxi≤nw​∑ℓ=1L−1(maxA⊂𝐀qℓ,δ​qℓ​∑k∈A𝔼​[|(μi−μk)|p​𝟏{i∈ℑℓ−1∖ℑℓ,𝔨ℓ​(i)=k}])1p≤∑ℓ=1L−1(δ​qℓ)1p​max(i,k)∈[[1,nw]]×[[qℓ+1,ns]]⁡(μi−μk)​ℙ​[μ^ℓk>μ^ℓi]1p.𝔼superscriptdelimited-[]superscript1subscript𝑛𝑤subscript𝑖subscript𝑛𝑤superscript𝜇𝑖superscript𝜇subscript𝔪𝐿1𝑖𝑝1𝑝1subscript𝑛𝑤subscript𝑖subscript𝑛𝑤superscriptsubscriptℓ1𝐿1𝔼superscriptdelimited-[]superscriptsuperscript𝜇𝑖superscript𝜇subscript𝔨ℓ𝑖subscript1𝑖subscriptℑℓ1subscriptℑℓ𝑝1𝑝𝑖subscript𝑛𝑤superscriptsubscriptℓ1𝐿1𝔼superscriptdelimited-[]superscriptsuperscript𝜇𝑖superscript𝜇subscript𝔨ℓ𝑖subscript1𝑖subscriptℑℓ1subscriptℑℓ𝑝1𝑝𝑖subscript𝑛𝑤superscriptsubscriptℓ1𝐿1superscriptsubscript𝐴subscript𝐀  subscript𝑞ℓ𝛿subscript𝑞ℓsubscript𝑘𝐴𝔼delimited-[]superscriptsuperscript𝜇𝑖superscript𝜇𝑘𝑝subscript1formulae-sequence𝑖subscriptℑℓ1subscriptℑℓsubscript𝔨ℓ𝑖𝑘1𝑝superscriptsubscriptℓ1𝐿1superscript𝛿subscript𝑞ℓ1𝑝subscript𝑖𝑘delimited-[]1subscript𝑛𝑤delimited-[]subscript𝑞ℓ1subscript𝑛𝑠superscript𝜇𝑖superscript𝜇𝑘ℙsuperscriptdelimited-[]superscriptsubscript^𝜇ℓ𝑘superscriptsubscript^𝜇ℓ𝑖1𝑝\begin{split}{\mathbb{E}}\left[\left|\frac{1}{n\_{w}}\sum\_{i\leq n\_{w}}\mu^{i}-\mu^{{\mathfrak{m}}\_{L-1}(i)}\right|^{p}\right]^{\frac{1}{p}}&\leq\frac{1}{n\_{w}}\sum\_{i\leq n\_{w}}\sum\_{\ell=1}^{L-1}{\mathbb{E}}\left[\left|(\mu^{i}-\mu^{{\mathfrak{k}}\_{\ell}(i)}){\mathbf{1}}\_{\{i\in{\mathfrak{I}}\_{\ell-1}\setminus{\mathfrak{I}}\_{\ell}\}}\right|^{p}\right]^{\frac{1}{p}}\\ &\leq\underset{i\leq n\_{w}}{\max}\sum\_{\ell=1}^{L-1}{\mathbb{E}}\left[\left|(\mu^{i}-\mu^{{\mathfrak{k}}\_{\ell}(i)}){\mathbf{1}}\_{\{i\in{\mathfrak{I}}\_{\ell-1}\setminus{\mathfrak{I}}\_{\ell}\}}\right|^{p}\right]^{\frac{1}{p}}\\ &\leq\underset{i\leq n\_{w}}{\max}\sum\_{\ell=1}^{L-1}\left(\max\_{A\subset{\mathbf{A}}\_{q\_{\ell},\delta q\_{\ell}}}\sum\_{k\in A}{\mathbb{E}}\left[\left|(\mu^{i}-\mu^{k})\right|^{p}{\mathbf{1}}\_{\{i\in{\mathfrak{I}}\_{\ell-1}\setminus{\mathfrak{I}}\_{\ell},{\mathfrak{k}}\_{\ell}(i)=k\}}\right]\right)^{\frac{1}{p}}\\ &\leq\sum\_{\ell=1}^{L-1}\left(\delta q\_{\ell}\right)^{\frac{1}{p}}\max\_{(i,k)\in[\![1,{n\_{w}}]\!]\times[\![q\_{\ell}+1,{n\_{s}}]\!]}(\mu^{i}-\mu^{k}){\mathbb{P}}[\hat{\mu}\_{\ell}^{k}>\hat{\mu}\_{\ell}^{i}]^{\frac{1}{p}}.\end{split} |  |

∎

### 2.3 Error bound for Sub-Gamma distributions

To illustrate how the general error bound of Proposition [2.2](#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") can be used in practice to decide of the sequence (qℓ,Nℓ)ℓsubscriptsubscript𝑞ℓsubscript𝑁ℓℓ(q\_{\ell},N\_{\ell})\_{\ell}, we now consider the case where the components of P|sP\_{|{\rm s}} have sub-gamma distributions, and apply Bernstein’s inequality in ([10](#S2.E10 "In Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")), see e.g. [[7](#bib.bib7), Chapter 2]. This requires the following assumption.

###### Assumption 1.

There exists c∈ℝ+𝑐subscriptℝc\in{\mathbb{R}}\_{+} such that the random variables Z​[i,k]:=(P|si−μi)−(P|sk−μk)Z[i,k]:=(P\_{|{\rm s}^{i}}-\mu^{i})-(P\_{|{\rm s}^{k}}-\mu^{k}), i,k≤ns

𝑖𝑘
subscript𝑛𝑠i,k\leq n\_{s}, satisfy Bernstein’s condition :

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|Z​[i,k]|p]≤p!​cp−22​𝔼​[Z​[i,k]2],i,k≤ns, for all ​p≥3.formulae-sequence𝔼delimited-[]superscript𝑍𝑖𝑘𝑝  𝑝superscript𝑐𝑝22𝔼delimited-[]𝑍superscript𝑖𝑘2𝑖formulae-sequence𝑘subscript𝑛𝑠 for all 𝑝3\mathbb{E}\left[\left|Z[i,k]\right|^{p}\right]\leq\frac{p!\;c^{p-2}}{2}\mathbb{E}\left[Z[i,k]^{2}\right],\;i,k\leq n\_{s},\;\mbox{ for all }p\geq 3. |  |

From now on, we shall assume that the constant c𝑐c is known. It can usually be estimated in practice.

###### Corollary 2.3.

Assume that Assumption [1](#Thmassumption1 "Assumption 1. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") holds. Then, for all p≥1𝑝1p\geq 1,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[|ES−ES^|p]1p≤𝔼superscriptdelimited-[]superscriptES^ES𝑝1𝑝absent\displaystyle\mathbb{E}\left[\left|{\rm ES}-\widehat{\rm ES}\right|^{p}\right]^{\frac{1}{p}}\leq | Fp​(q,N)subscriptF𝑝𝑞𝑁\displaystyle{\rm F}\_{p}(q,N) |  | (13) |

in which

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fp​(q,N):=assignsubscriptF𝑝𝑞𝑁absent\displaystyle{\rm F}\_{p}(q,N):= | ∑ℓ=1L−1(δ​qℓ)1p​max(i,k)∈[[1,nw]]×[[qℓ+1,ns]]⁡(μi−μk)​e−Nℓ​(μi−μk)22​p​(σi​k2+c​(μi−μk))superscriptsubscriptℓ1𝐿1superscript𝛿subscript𝑞ℓ1𝑝subscript𝑖𝑘delimited-[]1subscript𝑛𝑤delimited-[]subscript𝑞ℓ1subscript𝑛𝑠superscript𝜇𝑖superscript𝜇𝑘superscript𝑒subscript𝑁ℓsuperscriptsuperscript𝜇𝑖superscript𝜇𝑘22𝑝superscriptsubscript𝜎𝑖𝑘2𝑐superscript𝜇𝑖superscript𝜇𝑘\displaystyle\sum\_{\ell=1}^{L-1}(\delta q\_{\ell})^{\frac{1}{p}}\max\_{(i,k)\in[\![1,{n\_{w}}]\!]\times[\![q\_{\ell}+1,{n\_{s}}]\!]}(\mu^{i}-\mu^{k})e^{-\frac{N\_{\ell}(\mu^{i}-\mu^{k})^{2}}{2p(\sigma\_{ik}^{2}+c(\mu^{i}-\mu^{k}))}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +1nw​δ​NLNL​max1≤i1<…<inw≤ns​∑j=1nw(Cp,σ​p​σijp(δ​NL)p2+Cp,c​p​cp(δ​NL)p)1p1subscript𝑛𝑤𝛿subscript𝑁𝐿subscript𝑁𝐿1subscript𝑖1…subscript𝑖subscript𝑛𝑤subscript𝑛𝑠superscriptsubscript𝑗1subscript𝑛𝑤superscriptsubscript𝐶  𝑝𝜎𝑝superscriptsubscript𝜎subscript𝑖𝑗𝑝superscript𝛿subscript𝑁𝐿𝑝2subscript𝐶  𝑝𝑐𝑝superscript𝑐𝑝superscript𝛿subscript𝑁𝐿𝑝1𝑝\displaystyle+\frac{1}{n\_{w}}\frac{\delta N\_{L}}{N\_{L}}\underset{1\leq i\_{1}<...<i\_{{{n\_{w}}}}\leq{n\_{s}}}{\max}\sum\_{j=1}^{{n\_{w}}}\left(C\_{p,\sigma}\frac{p\sigma\_{i\_{j}}^{p}}{(\delta N\_{L})^{\frac{p}{2}}}+C\_{p,c}\frac{pc^{p}}{(\delta N\_{L})^{p}}\right)^{\frac{1}{p}} |  | (14) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1nw​NL−1NL​∑i=1ns(Cp,σ​p​σip(NL−1)p2+Cp,c​p​cp(NL−1)p)1p1subscript𝑛𝑤subscript𝑁𝐿1subscript𝑁𝐿superscriptsubscript𝑖1subscript𝑛𝑠superscriptsubscript𝐶  𝑝𝜎𝑝superscriptsubscript𝜎𝑖𝑝superscriptsubscript𝑁𝐿1𝑝2subscript𝐶  𝑝𝑐𝑝superscript𝑐𝑝superscriptsubscript𝑁𝐿1𝑝1𝑝\displaystyle+\frac{1}{n\_{w}}\frac{N\_{L-1}}{N\_{L}}\sum\_{i=1}^{{n\_{s}}}\left(C\_{p,\sigma}\frac{p\sigma\_{i}^{p}}{(N\_{L-1})^{\frac{p}{2}}}+C\_{p,c}\frac{pc^{p}}{(N\_{L-1})^{p}}\right)^{\frac{1}{p}} |  |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | {σi​k2:=Var​[P|si−P|sk]​ and ​σi2:=Var​[P|si],i,k≤nsCp,σ:=2p−1​Γ​(p2)​ and ​Cp,c:=4p​Γ​(p)\begin{split}\begin{cases}\sigma\_{ik}^{2}:={\rm Var}[P\_{|{\rm s}^{i}}-P\_{|{\rm s}^{k}}]\;\mbox{ and }\;\sigma\_{i}^{2}:={\rm Var}[P\_{|{\rm s}^{i}}],\;i,k\leq n\_{s}\\ C\_{p,\sigma}:=2^{p-1}\Gamma\left(\frac{p}{2}\right)\;\mbox{ and }\;C\_{p,c}:=4^{p}\Gamma\left(p\right)\end{cases}\end{split} |  | (15) |

where ΓΓ\Gamma is the Gamma function defined by

|  |  |  |
| --- | --- | --- |
|  | Γ​(y)=∫0+∞xy−1​e−x​𝑑x,y>0.formulae-sequenceΓ𝑦superscriptsubscript0superscript𝑥𝑦1superscript𝑒𝑥differential-d𝑥𝑦0\Gamma\left(y\right)=\int\_{0}^{+\infty}x^{y-1}e^{-x}dx,\;y>0. |  |

The upper-bound of Corollary [2.3](#S2.Thmtheorem3 "Corollary 2.3. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") has two advantages on Proposition [2.2](#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios"). First, the dependence on (qℓ,Nℓ)ℓ≥0subscriptsubscript𝑞ℓsubscript𝑁ℓℓ0(q\_{\ell},N\_{\ell})\_{\ell\geq 0} is more explicit. It depends on unknown quantities, but we can estimate (at least rough) confidence intervals for them, see e.g. Section [2.4](#S2.SS4 "2.4 Optimal a-priori allocation by deterministic dynamic programming based on fixed a-priori bounds ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") below. Second, as we will see in the next section, it allows one to define a tractable deterministic optimal control problem satisfying a dynamic programming principle, or even simple heuristics (see Section [2.5](#S2.SS5 "2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")), to select an appropriate sequence (qℓ,Nℓ)ℓ≥0subscriptsubscript𝑞ℓsubscript𝑁ℓℓ0(q\_{\ell},N\_{\ell})\_{\ell\geq 0}.

###### Proof of Corollary [2.3](#S2.Thmtheorem3 "Corollary 2.3. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios").

The first term in ([14](#S2.E14 "In Corollary 2.3. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")) is an upper-bound for the first term in the right-hand side of ([10](#S2.E10 "In Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")), see [[7](#bib.bib7), Theorem 2.1]. As for the two other terms in ([10](#S2.E10 "In Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")), we use the usual argument, for i≤ns𝑖subscript𝑛𝑠i\leq n\_{s},

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|δ​μ^Li−μi|p]=∫0∞p​xp−1​ℙ​[|δ​μ^Li−μi|≥x]​𝑑x𝔼delimited-[]superscript𝛿superscriptsubscript^𝜇𝐿𝑖superscript𝜇𝑖𝑝superscriptsubscript0𝑝superscript𝑥𝑝1ℙdelimited-[]𝛿superscriptsubscript^𝜇𝐿𝑖superscript𝜇𝑖𝑥differential-d𝑥{\mathbb{E}}\left[\left|\delta\hat{\mu}\_{L}^{i}-\mu^{i}\right|^{p}\right]=\int\_{0}^{\infty}px^{p-1}{\mathbb{P}}[|\delta\hat{\mu}\_{L}^{i}-\mu^{i}|\geq x]dx |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|μ^L−1i−μi|p]=∫0∞p​xp−1​ℙ​[|μ^L−1i−μi|≥x]​𝑑x,𝔼delimited-[]superscriptsuperscriptsubscript^𝜇𝐿1𝑖superscript𝜇𝑖𝑝superscriptsubscript0𝑝superscript𝑥𝑝1ℙdelimited-[]superscriptsubscript^𝜇𝐿1𝑖superscript𝜇𝑖𝑥differential-d𝑥{\mathbb{E}}\left[\left|\hat{\mu}\_{L-1}^{i}-\mu^{i}\right|^{p}\right]=\int\_{0}^{\infty}px^{p-1}{\mathbb{P}}[|\hat{\mu}\_{L-1}^{i}-\mu^{i}|\geq x]dx, |  |

and then appeal to [[7](#bib.bib7), Theorem 2.1] again to deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|δ​μ^Li−μi|p]≤𝔼delimited-[]superscript𝛿superscriptsubscript^𝜇𝐿𝑖superscript𝜇𝑖𝑝absent\displaystyle{\mathbb{E}}\left[\left|\delta\hat{\mu}\_{L}^{i}-\mu^{i}\right|^{p}\right]\leq | ∫0∞p​xp−1​e−δ​NL​x22​(σi2+c​x)​𝑑xsuperscriptsubscript0𝑝superscript𝑥𝑝1superscript𝑒𝛿subscript𝑁𝐿superscript𝑥22superscriptsubscript𝜎𝑖2𝑐𝑥differential-d𝑥\displaystyle\int\_{0}^{\infty}px^{p-1}e^{-\frac{\delta N\_{L}x^{2}}{2(\sigma\_{i}^{2}+cx)}}dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ∫0∞p​xp−1​e−δ​NL​x24​σi2​𝟏{x≤σi2c}​𝑑x+∫0∞p​xp−1​e−δ​NL​x4​c​𝟏{x>σi2c}​𝑑xsuperscriptsubscript0𝑝superscript𝑥𝑝1superscript𝑒𝛿subscript𝑁𝐿superscript𝑥24superscriptsubscript𝜎𝑖2subscript1𝑥superscriptsubscript𝜎𝑖2𝑐differential-d𝑥superscriptsubscript0𝑝superscript𝑥𝑝1superscript𝑒𝛿subscript𝑁𝐿𝑥4𝑐subscript1𝑥superscriptsubscript𝜎𝑖2𝑐differential-d𝑥\displaystyle\int\_{0}^{\infty}px^{p-1}e^{-\frac{\delta N\_{L}x^{2}}{4\sigma\_{i}^{2}}}{\mathbf{1}}\_{\{x\leq\frac{\sigma\_{i}^{2}}{c}\}}dx+\int\_{0}^{\infty}px^{p-1}e^{-\frac{\delta N\_{L}x}{4c}}{\mathbf{1}}\_{\{x>\frac{\sigma\_{i}^{2}}{c}\}}dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | p​(σi2)p2(δ​NL)p2​∫0∞yp−1​e−y24​𝑑y+p​cp(δ​NL)p​∫0∞yp−1​e−y4​𝑑y,𝑝superscriptsubscriptsuperscript𝜎2𝑖𝑝2superscript𝛿subscript𝑁𝐿𝑝2superscriptsubscript0superscript𝑦𝑝1superscript𝑒superscript𝑦24differential-d𝑦𝑝superscript𝑐𝑝superscript𝛿subscript𝑁𝐿𝑝superscriptsubscript0superscript𝑦𝑝1superscript𝑒𝑦4differential-d𝑦\displaystyle\frac{p(\sigma^{2}\_{i})^{\frac{p}{2}}}{(\delta N\_{L})^{\frac{p}{2}}}\int\_{0}^{\infty}y^{p-1}e^{-\frac{y^{2}}{4}}dy+\frac{pc^{p}}{(\delta N\_{L})^{p}}\int\_{0}^{\infty}y^{p-1}e^{-\frac{y}{4}}dy, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | p​σip(δ​NL)p2​2p−1​Γ​(p2)+p​cp(δ​NL)p​4p​Γ​(p),𝑝superscriptsubscript𝜎𝑖𝑝superscript𝛿subscript𝑁𝐿𝑝2superscript2𝑝1Γ𝑝2𝑝superscript𝑐𝑝superscript𝛿subscript𝑁𝐿𝑝superscript4𝑝Γ𝑝\displaystyle\frac{p\sigma\_{i}^{p}}{(\delta N\_{L})^{\frac{p}{2}}}2^{p-1}\Gamma\left(\frac{p}{2}\right)+\frac{pc^{p}}{(\delta N\_{L})^{p}}4^{p}\Gamma(p), |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|μ^L−1i−μi|p]≤𝔼delimited-[]superscriptsuperscriptsubscript^𝜇𝐿1𝑖superscript𝜇𝑖𝑝absent\displaystyle{\mathbb{E}}\left[\left|\hat{\mu}\_{L-1}^{i}-\mu^{i}\right|^{p}\right]\leq | ∫0∞p​xp−1​e−NL−1​x22​(σi2+c​x)​𝑑xsuperscriptsubscript0𝑝superscript𝑥𝑝1superscript𝑒subscript𝑁𝐿1superscript𝑥22superscriptsubscript𝜎𝑖2𝑐𝑥differential-d𝑥\displaystyle\int\_{0}^{\infty}px^{p-1}e^{-\frac{N\_{L-1}x^{2}}{2(\sigma\_{i}^{2}+cx)}}dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ∫0∞p​xp−1​e−NL−1​x24​σi2​𝟏{x≤σi2c}​𝑑x+∫0∞p​xp−1​e−NL−1​x4​c​𝟏{x>σi2c}​𝑑xsuperscriptsubscript0𝑝superscript𝑥𝑝1superscript𝑒subscript𝑁𝐿1superscript𝑥24superscriptsubscript𝜎𝑖2subscript1𝑥superscriptsubscript𝜎𝑖2𝑐differential-d𝑥superscriptsubscript0𝑝superscript𝑥𝑝1superscript𝑒subscript𝑁𝐿1𝑥4𝑐subscript1𝑥superscriptsubscript𝜎𝑖2𝑐differential-d𝑥\displaystyle\int\_{0}^{\infty}px^{p-1}e^{-\frac{N\_{L-1}x^{2}}{4\sigma\_{i}^{2}}}{\mathbf{1}}\_{\{x\leq\frac{\sigma\_{i}^{2}}{c}\}}dx+\int\_{0}^{\infty}px^{p-1}e^{-\frac{N\_{L-1}x}{4c}}{\mathbf{1}}\_{\{x>\frac{\sigma\_{i}^{2}}{c}\}}dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | p​(σi2)p2(NL−1)p2​∫0∞yp−1​e−y24​𝑑y+p​cp(NL−1)p​∫0∞yp−1​e−y4​𝑑y,𝑝superscriptsubscriptsuperscript𝜎2𝑖𝑝2superscriptsubscript𝑁𝐿1𝑝2superscriptsubscript0superscript𝑦𝑝1superscript𝑒superscript𝑦24differential-d𝑦𝑝superscript𝑐𝑝superscriptsubscript𝑁𝐿1𝑝superscriptsubscript0superscript𝑦𝑝1superscript𝑒𝑦4differential-d𝑦\displaystyle\frac{p(\sigma^{2}\_{i})^{\frac{p}{2}}}{(N\_{L-1})^{\frac{p}{2}}}\int\_{0}^{\infty}y^{p-1}e^{-\frac{y^{2}}{4}}dy+\frac{pc^{p}}{(N\_{L-1})^{p}}\int\_{0}^{\infty}y^{p-1}e^{-\frac{y}{4}}dy, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | p​σip(NL−1)p2​2p−1​Γ​(p2)+p​cp(NL−1)p​4p​Γ​(p).𝑝superscriptsubscript𝜎𝑖𝑝superscriptsubscript𝑁𝐿1𝑝2superscript2𝑝1Γ𝑝2𝑝superscript𝑐𝑝superscriptsubscript𝑁𝐿1𝑝superscript4𝑝Γ𝑝\displaystyle\frac{p\sigma\_{i}^{p}}{(N\_{L-1})^{\frac{p}{2}}}2^{p-1}\Gamma\left(\frac{p}{2}\right)+\frac{pc^{p}}{(N\_{L-1})^{p}}4^{p}\Gamma\left(p\right). |  |

∎

###### Remark 2.4.

If the (μ^ℓi)i≤nssubscriptsubscriptsuperscript^𝜇𝑖ℓ𝑖subscript𝑛𝑠(\hat{\mu}^{i}\_{\ell})\_{i\leq n\_{s}} and (δ​μ^ℓi)i≤nssubscript𝛿subscriptsuperscript^𝜇𝑖ℓ𝑖subscript𝑛𝑠(\delta\hat{\mu}^{i}\_{\ell})\_{i\leq n\_{s}} are Gaussian, which is the case asymptotically, then the bound of Corollary [2.3](#S2.Thmtheorem3 "Corollary 2.3. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") remains valid with c=0𝑐0c=0. This fact will be used later on for simplifying our numerical algorithms.

### 2.4 Optimal a-priori allocation by deterministic dynamic programming based on fixed a-priori bounds

Given N:=(Nℓ)0≤ℓ≤Lassign𝑁subscriptsubscript𝑁ℓ0ℓ𝐿N:=(N\_{\ell})\_{0\leq\ell\leq L} and q=(qℓ)0≤ℓ≤L−1𝑞subscriptsubscript𝑞ℓ0ℓ𝐿1q=(q\_{\ell})\_{0\leq\ell\leq L-1}, the total computation cost is

|  |  |  |
| --- | --- | --- |
|  | C​(q,N):=∑ℓ=0L−1qℓ​(Nℓ+1−Nℓ)assignC𝑞𝑁superscriptsubscriptℓ0𝐿1subscript𝑞ℓsubscript𝑁ℓ1subscript𝑁ℓ{\rm C}(q,N):=\sum\_{\ell=0}^{L-1}q\_{\ell}(N\_{\ell+1}-N\_{\ell}) |  |

with the convention N0:=0assignsubscript𝑁00N\_{0}:=0. Let 𝒩𝒩{\mathcal{N}} denote the collection of non-decreasing sequences N:=(Nℓ)0≤ℓ≤Lassign𝑁subscriptsubscript𝑁ℓ0ℓ𝐿N:=(N\_{\ell})\_{0\leq\ell\leq L} with values in ℕℕ{\mathbb{N}} such that N0=0subscript𝑁00N\_{0}=0, and let 𝒬𝒬{\mathcal{Q}} denote the collections of non-increasing sequences888We write (qℓ)0≤ℓ≤Lsubscriptsubscript𝑞ℓ0ℓ𝐿(q\_{\ell})\_{0\leq\ell\leq L} for convenience also qLsubscript𝑞𝐿q\_{L} will never play any role. q=(qℓ)0≤ℓ≤L𝑞subscriptsubscript𝑞ℓ0ℓ𝐿q=(q\_{\ell})\_{0\leq\ell\leq L} with values in [[nw,ns]]delimited-[]subscript𝑛𝑤subscript𝑛𝑠[\![n\_{w},n\_{s}]\!] satisfying ([5](#S2.E5 "In 2.1 The algorithm ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")). In this section, we fix a total effort K>0𝐾0K>0 and recall how Fp​(q,N)subscriptF𝑝𝑞𝑁{\rm F}\_{p}(q,N), as defined in ([14](#S2.E14 "In Corollary 2.3. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")), can be minimized
over the collection 𝒜𝒜{\mathcal{A}} of sequences (N,q)∈𝒩×𝒬𝑁𝑞𝒩𝒬(N,q)\in{\mathcal{N}}\times{\mathcal{Q}} satisfying C​(N,q)≤KC𝑁𝑞𝐾{\rm C}(N,q)\leq K by using a standard dynamic programming approach.

Given (q¯,N¯)∈𝒬×𝒩¯𝑞¯𝑁𝒬𝒩(\bar{q},\bar{N})\in{\mathcal{Q}}\times{\mathcal{N}} and 0≤ℓ≤L−10ℓ𝐿1{0\leq}\ell{\leq}{L-1}, we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fp​(ℓ,q¯,N¯):=assignsubscriptF𝑝ℓ¯𝑞¯𝑁absent\displaystyle{\rm F}\_{p}(\ell,\bar{q},\bar{N}):= | 1nw​δ​N¯LN¯L​max1≤i1<…<inw≤ns​∑j=1nw(Cp,σ​p​σijp(δ​N¯L)p2+Cp,c​p​cp(δ​N¯L)p)1p1subscript𝑛𝑤𝛿subscript¯𝑁𝐿subscript¯𝑁𝐿1subscript𝑖1…subscript𝑖subscript𝑛𝑤subscript𝑛𝑠superscriptsubscript𝑗1subscript𝑛𝑤superscriptsubscript𝐶  𝑝𝜎𝑝subscriptsuperscript𝜎𝑝subscript𝑖𝑗superscript𝛿subscript¯𝑁𝐿𝑝2subscript𝐶  𝑝𝑐𝑝superscript𝑐𝑝superscript𝛿subscript¯𝑁𝐿𝑝1𝑝\displaystyle\frac{1}{n\_{w}}\frac{\delta\bar{N}\_{L}}{\bar{N}\_{L}}\underset{1\leq i\_{1}<...<i\_{{n\_{w}}}\leq{n\_{s}}}{\max}\sum\_{j=1}^{{n\_{w}}}\left(C\_{p,\sigma}\frac{p\sigma^{p}\_{i\_{j}}}{(\delta\bar{N}\_{L})^{\frac{p}{2}}}+C\_{p,c}\frac{pc^{p}}{(\delta\bar{N}\_{L})^{p}}\right)^{\frac{1}{p}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +1nw​N¯L−1N¯L​∑i=1ns(Cp,σ​p​σip(N¯L−1)p2+Cp,c​p​cp(N¯L−1)p)1p+𝟏{ℓ<L−1}​∑ℓ′=ℓ+1L−1fp​(q¯ℓ′,q¯ℓ′−1,N¯ℓ′),1subscript𝑛𝑤subscript¯𝑁𝐿1subscript¯𝑁𝐿superscriptsubscript𝑖1subscript𝑛𝑠superscriptsubscript𝐶  𝑝𝜎𝑝subscriptsuperscript𝜎𝑝𝑖superscriptsubscript¯𝑁𝐿1𝑝2subscript𝐶  𝑝𝑐𝑝superscript𝑐𝑝superscriptsubscript¯𝑁𝐿1𝑝1𝑝subscript1ℓ𝐿1superscriptsubscriptsuperscriptℓ′ℓ1𝐿1subscript𝑓𝑝subscript¯𝑞superscriptℓ′subscript¯𝑞superscriptℓ′1subscript¯𝑁superscriptℓ′\displaystyle+\frac{1}{n\_{w}}\frac{\bar{N}\_{L-1}}{\bar{N}\_{L}}\sum\_{i=1}^{{n\_{s}}}\left(C\_{p,\sigma}\frac{p\sigma^{p}\_{i}}{(\bar{N}\_{L-1})^{\frac{p}{2}}}+C\_{p,c}\frac{pc^{p}}{(\bar{N}\_{L-1})^{p}}\right)^{\frac{1}{p}}+{\mathbf{1}}\_{\{\ell<L-1\}}\sum\_{\ell^{\prime}=\ell+1}^{L-1}f\_{p}(\bar{q}\_{\ell^{\prime}},\bar{q}\_{\ell^{\prime}-1},\bar{N}\_{\ell^{\prime}}), |  | (16) |

where

|  |  |  |
| --- | --- | --- |
|  | fp​(q¯ℓ′,q¯ℓ′−1,N¯ℓ′):=(δ​q¯ℓ′)1p​max(i,k)∈[[1,nw]]×[[q¯ℓ′+1,ns]]⁡(μi−μk)​e−N¯ℓ′​(μi−μk)22​p​(σi​k2+c​(μi−μk)),assignsubscript𝑓𝑝subscript¯𝑞superscriptℓ′subscript¯𝑞superscriptℓ′1subscript¯𝑁superscriptℓ′superscript𝛿subscript¯𝑞superscriptℓ′1𝑝subscript𝑖𝑘delimited-[]1subscript𝑛𝑤delimited-[]subscript¯𝑞superscriptℓ′1subscript𝑛𝑠superscript𝜇𝑖superscript𝜇𝑘superscript𝑒subscript¯𝑁superscriptℓ′superscriptsuperscript𝜇𝑖superscript𝜇𝑘22𝑝superscriptsubscript𝜎𝑖𝑘2𝑐superscript𝜇𝑖superscript𝜇𝑘f\_{p}(\bar{q}\_{\ell^{\prime}},\bar{q}\_{\ell^{\prime}-1},\bar{N}\_{\ell^{\prime}}):=(\delta\bar{q}\_{\ell^{\prime}})^{\frac{1}{p}}\max\_{(i,k)\in[\![1,n\_{w}]\!]\times[\![\bar{q}\_{\ell^{\prime}}+1,n\_{s}]\!]}(\mu^{i}-\mu^{k})e^{-\frac{\bar{N}\_{\ell^{\prime}}(\mu^{i}-\mu^{k})^{2}}{2p(\sigma\_{ik}^{2}+c(\mu^{i}-\mu^{k}))}}, |  |

and define

|  |  |  |
| --- | --- | --- |
|  | F^p​(ℓ,q¯,N¯)=min(q¯′,N¯′)∈𝒜​(ℓ,q¯,N¯)⁡Fp​(ℓ,q¯′,N¯′)subscript^F𝑝ℓ¯𝑞¯𝑁subscriptsuperscript¯𝑞′superscript¯𝑁′𝒜ℓ¯𝑞¯𝑁subscriptF𝑝ℓsuperscript¯𝑞′superscript¯𝑁′\displaystyle\hat{\rm F}\_{p}(\ell,\bar{q},\bar{N})=\min\_{(\bar{q}^{\prime},\bar{N}^{\prime})\in{\mathcal{A}}(\ell,\bar{q},\bar{N})}{\rm F}\_{p}(\ell,\bar{q}^{\prime},\bar{N}^{\prime}) |  |

where999In the following, we only write 𝒜​(0)𝒜0{\mathcal{A}}(0) for ℓ=0ℓ0\ell=0 as it does not depend on (q¯,N¯)¯𝑞¯𝑁(\bar{q},\bar{N}).

|  |  |  |
| --- | --- | --- |
|  | 𝒜​(ℓ,q¯,N¯):={(q¯′,N¯′)∈𝒬×𝒩:(q¯l′,N¯l′)0≤l≤ℓ=(q¯l,N¯l)0≤l≤ℓ​ and ​C​(q¯′,N¯′)≤K},ℓ≥0.formulae-sequenceassign𝒜ℓ¯𝑞¯𝑁conditional-setsuperscript¯𝑞′superscript¯𝑁′𝒬𝒩subscriptsubscriptsuperscript¯𝑞′𝑙subscriptsuperscript¯𝑁′𝑙0𝑙ℓsubscriptsubscript¯𝑞𝑙subscript¯𝑁𝑙0𝑙ℓ and Csuperscript¯𝑞′superscript¯𝑁′𝐾ℓ0{\mathcal{A}}(\ell,\bar{q},\bar{N}):=\{(\bar{q}^{\prime},\bar{N}^{\prime})\in{\mathcal{Q}}\times{\mathcal{N}}:(\bar{q}^{\prime}\_{l},\bar{N}^{\prime}\_{l})\_{{0}\leq l\leq\ell}=(\bar{q}\_{l},\bar{N}\_{l})\_{{0}\leq l\leq\ell}\mbox{ and }\;{\rm C}(\bar{q}^{\prime},\bar{N}^{\prime})\leq K\}\;,\;\ell\geq{0}. |  |

Then, the dynamic programming principle implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^p​(ℓ,q¯,N¯)=subscript^F𝑝ℓ¯𝑞¯𝑁absent\displaystyle\hat{\rm F}\_{p}(\ell,\bar{q},\bar{N})= | min(q¯′,N¯′)∈𝒜​(ℓ,q¯,N¯)⁡[F^p​(ℓ+1,q¯′,N¯′)+fp​(q¯ℓ+1′,q¯ℓ,N¯ℓ+1′)], for ​0≤ℓ<L−1.  subscriptsuperscript¯𝑞′superscript¯𝑁′𝒜ℓ¯𝑞¯𝑁subscript^F𝑝ℓ1superscript¯𝑞′superscript¯𝑁′subscript𝑓𝑝subscriptsuperscript¯𝑞′ℓ1subscript¯𝑞ℓsubscriptsuperscript¯𝑁′ℓ1 for 0 ℓ𝐿1\displaystyle\min\_{(\bar{q}^{\prime},\bar{N}^{\prime})\in{\mathcal{A}}(\ell,\bar{q},\bar{N})}\left[\hat{\rm F}\_{p}(\ell+1,\bar{q}^{\prime},\bar{N}^{\prime})+f\_{p}(\bar{q}^{\prime}\_{\ell+1},\bar{q}\_{\ell},\bar{N}^{\prime}\_{\ell+1})\right],\;\mbox{ for }0\leq\ell<{L-1}. |  |

This reduces the search for an optimal selection of (N¯,q¯)¯𝑁¯𝑞(\bar{N},\bar{q}) to L−1𝐿1L-1 one-step optimization problems, which is much simpler to solve than the optimization problem associated to the left-hand side of ([13](#S2.E13 "In Corollary 2.3. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")).

In practice, the exact values of (μi,σi2)i≤nssubscriptsuperscript𝜇𝑖subscriptsuperscript𝜎2𝑖𝑖subscript𝑛𝑠(\mu^{i},\sigma^{2}\_{i})\_{i\leq n\_{s}} and (σi​k2)i,k≤nssubscriptsubscriptsuperscript𝜎2𝑖𝑘

𝑖𝑘
subscript𝑛𝑠(\sigma^{2}\_{ik})\_{i,k\leq n\_{s}} are not known. However, one can consider robust versions of the above. For instance, if we know that there exists some (δq¯,δq¯)q≤nssubscript¯subscript𝛿𝑞¯subscript𝛿𝑞𝑞subscript𝑛𝑠(\underline{\delta\_{q}},\overline{\delta\_{q}})\_{q\leq n\_{s}} and σ¯2superscript¯𝜎2\overline{\sigma}^{2} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | {0≤δq¯≤μi−μk≤δq¯,(i,k)∈[[1,nw]]×[[q+1,ns]]σi2∨σk2∨σi​k2≤σ¯2,(i,k)∈[[1,nw]]×[[nw+1,ns]],casesformulae-sequence0¯subscript𝛿𝑞superscript𝜇𝑖superscript𝜇𝑘¯subscript𝛿𝑞𝑖𝑘delimited-[]1subscript𝑛𝑤delimited-[]𝑞1subscript𝑛𝑠formulae-sequencesuperscriptsubscript𝜎𝑖2superscriptsubscript𝜎𝑘2superscriptsubscript𝜎𝑖𝑘2superscript¯𝜎2𝑖𝑘delimited-[]1subscript𝑛𝑤delimited-[]subscript𝑛𝑤1subscript𝑛𝑠\displaystyle\left\{\begin{array}[]{c}0\leq\underline{\delta\_{q}}\leq\mu^{i}-\mu^{k}\leq\overline{\delta\_{q}},\;(i,k)\in[\![1,n\_{w}]\!]\times[\![q+1,n\_{s}]\!]\\ \sigma\_{i}^{2}\vee\sigma\_{k}^{2}\vee\sigma\_{ik}^{2}\leq\overline{\sigma}^{2},\;(i,k)\in[\![1,n\_{w}]\!]\times[\![n\_{w}+1,n\_{s}]\!],\end{array}\right. |  | (19) |

then one can similarly minimize the upper-bound of FpsubscriptF𝑝{\rm F}\_{p} defined as

|  |  |  |
| --- | --- | --- |
|  | δ​N¯LN¯L​(Cp,σ​p​σ¯p(δ​N¯L)p2+Cp,c​p​cp(δ​N¯L)p)+nsnw​N¯L−1N¯L​(Cp,σ​p​σ¯p(N¯L−1)p2+Cp,c​p​cp(N¯L−1)p)𝛿subscript¯𝑁𝐿subscript¯𝑁𝐿subscript𝐶  𝑝𝜎𝑝superscript¯𝜎𝑝superscript𝛿subscript¯𝑁𝐿𝑝2subscript𝐶  𝑝𝑐𝑝superscript𝑐𝑝superscript𝛿subscript¯𝑁𝐿𝑝subscript𝑛𝑠subscript𝑛𝑤subscript¯𝑁𝐿1subscript¯𝑁𝐿subscript𝐶  𝑝𝜎𝑝superscript¯𝜎𝑝superscriptsubscript¯𝑁𝐿1𝑝2subscript𝐶  𝑝𝑐𝑝superscript𝑐𝑝superscriptsubscript¯𝑁𝐿1𝑝\displaystyle\frac{\delta\bar{N}\_{L}}{\bar{N}\_{L}}\left(C\_{p,\sigma}\frac{p\overline{\sigma}^{p}}{(\delta\bar{N}\_{L})^{\frac{p}{2}}}+C\_{p,c}\frac{pc^{p}}{(\delta\bar{N}\_{L})^{p}}\right)+\frac{n\_{s}}{n\_{w}}\frac{\bar{N}\_{L-1}}{\bar{N}\_{L}}\left(C\_{p,\sigma}\frac{p\overline{\sigma}^{p}}{(\bar{N}\_{L-1})^{\frac{p}{2}}}+C\_{p,c}\frac{pc^{p}}{(\bar{N}\_{L-1})^{p}}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | +𝟏{ℓ<L−1}​∑ℓ′=ℓL−1f~p​(q¯ℓ′,q¯ℓ′−1,N¯ℓ′),subscript1ℓ𝐿1superscriptsubscriptsuperscriptℓ′ℓ𝐿1subscript~𝑓𝑝subscript¯𝑞superscriptℓ′subscript¯𝑞superscriptℓ′1subscript¯𝑁superscriptℓ′\displaystyle+{\mathbf{1}}\_{\{\ell<L-1\}}\sum\_{\ell^{\prime}=\ell}^{L-1}\tilde{f}\_{p}(\bar{q}\_{\ell^{\prime}},\bar{q}\_{\ell^{\prime}-1},\bar{N}\_{\ell^{\prime}}), |  |

with

|  |  |  |
| --- | --- | --- |
|  | f~p​(q¯ℓ′,q¯ℓ′−1,N¯ℓ′):=(δ​q¯ℓ′)1p​maxδ¯q¯ℓ′≤δ≤δ¯q¯ℓ′⁡δ​e−N¯ℓ′​δ22​p​(σ¯2+c​δ).assignsubscript~𝑓𝑝subscript¯𝑞superscriptℓ′subscript¯𝑞superscriptℓ′1subscript¯𝑁superscriptℓ′superscript𝛿subscript¯𝑞superscriptℓ′1𝑝subscriptsubscript¯𝛿subscript¯𝑞superscriptℓ′𝛿subscript¯𝛿subscript¯𝑞superscriptℓ′𝛿superscript𝑒subscript¯𝑁superscriptℓ′superscript𝛿22𝑝superscript¯𝜎2𝑐𝛿\tilde{f}\_{p}(\bar{q}\_{\ell^{\prime}},\bar{q}\_{\ell^{\prime}-1},\bar{N}\_{\ell^{\prime}}):=(\delta\bar{q}\_{\ell^{\prime}})^{\frac{1}{p}}\max\_{\underline{\delta}\_{{\overline{q}\_{\ell^{\prime}}}}\leq\delta\leq\overline{\delta}\_{{\overline{q}}\_{\ell^{\prime}}}}\;\delta e^{-\frac{\bar{N}\_{\ell^{\prime}}\delta^{2}}{2p(\overline{\sigma}^{2}+c\delta)}}. |  |

This corresponds to a worst case scenario, when only the a priori bounds (δq¯,δq¯)q≤nssubscript¯subscript𝛿𝑞¯subscript𝛿𝑞𝑞subscript𝑛𝑠(\underline{\delta\_{q}},\overline{\delta\_{q}})\_{q\leq n\_{s}} and σ¯2superscript¯𝜎2\overline{\sigma}^{2} are known.
In the above, one can also impose that q𝑞q takes values in a given subset of Q𝑄Q of 𝒬𝒬{\mathcal{Q}}. In this case, we will only need to know (δq¯,δq¯)q∈Q¯subscript¯subscript𝛿𝑞¯subscript𝛿𝑞𝑞¯𝑄(\underline{\delta\_{q}},\overline{\delta\_{q}})\_{q\in\bar{Q}}.

We refer to Section [4](#S4 "4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios") below for numerical tests that show that such an algorithm seems to perform pretty well. Note that the optimization can be done off-line.

### 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size

Inspired by [[3](#bib.bib3), [5](#bib.bib5), [6](#bib.bib6), [14](#bib.bib14)], we assume here that we know the value of a constant δ0>0subscript𝛿00\delta\_{0}>0 such that the impacts of the nwsubscript𝑛𝑤n\_{w} worst scenarios have values that are separated by at least (k−nw)​δ0𝑘subscript𝑛𝑤subscript𝛿0(k-n\_{w})\delta\_{0} from the k𝑘k-th worst scenario, for k>nw𝑘subscript𝑛𝑤k>n\_{w}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μnw−μk≥(k−nw)​δ0,∀k∈[[nw+1,ns]].formulae-sequencesuperscript𝜇subscript𝑛𝑤superscript𝜇𝑘𝑘subscript𝑛𝑤subscript𝛿0for-all𝑘delimited-[]subscript𝑛𝑤1subscript𝑛𝑠\mu^{{n\_{w}}}-\mu^{{k}}\geq\left(k-n\_{w}\right)\delta\_{0},\;\forall\;k\in[\![n\_{w}+1,n\_{s}]\!]. |  | (20) |

To illustrate this, we plot on Figures [2](#S2.F2 "Figure 2 ‣ 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")-[4](#S2.F4 "Figure 4 ‣ 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") the curves k↦|μnw−μk|maps-to𝑘superscript𝜇subscript𝑛𝑤superscript𝜇𝑘k\mapsto|\mu^{{n\_{w}}}-\mu^{{k}}| for different formerly used test books of Natixis.
We see that they are more flat on the interval [100,120]100120[100,120], so that a rather conservative value would be the minimum (over the different books) of (μ100−μ120)/20superscript𝜇100superscript𝜇12020(\mu^{100}-\mu^{120})/20. Another choice in practice could be to take the ratio (μnw−μ100)/(100−nw)superscript𝜇subscript𝑛𝑤superscript𝜇100100subscript𝑛𝑤(\mu^{n\_{w}}-\mu^{100})/(100-n\_{w}) which amounts to considering only the first part of the curve, and neglecting points that are anyway far from the worst scenarios.

![Refer to caption](/html/2005.12593/assets/F2XX_mu_fig_bare.png)


Figure 1:  k↦|μnw−μk|maps-to𝑘superscript𝜇subscript𝑛𝑤superscript𝜇𝑘k\mapsto|\mu^{{n\_{w}}}-\mu^{{k}}| for Book #1

![Refer to caption](/html/2005.12593/assets/F5C4_mu_fig_bare.png)


Figure 2:  k↦|μnw−μk|maps-to𝑘superscript𝜇subscript𝑛𝑤superscript𝜇𝑘k\mapsto|\mu^{{n\_{w}}}-\mu^{{k}}| for Book #2



![Refer to caption](/html/2005.12593/assets/F785A_mu_fig_bare.png)


Figure 3:  k↦|μnw−μk|maps-to𝑘superscript𝜇subscript𝑛𝑤superscript𝜇𝑘k\mapsto|\mu^{{n\_{w}}}-\mu^{{k}}| for Book #3

![Refer to caption](/html/2005.12593/assets/F785I_mu_fig_bare.png)


Figure 4:  k↦|μnw−μk|maps-to𝑘superscript𝜇subscript𝑛𝑤superscript𝜇𝑘k\mapsto|\mu^{{n\_{w}}}-\mu^{{k}}| for Book #4

We now consider a simplified version of the algorithm of Section [2.1](#S2.SS1 "2.1 The algorithm ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") where we only do one intermediate “fast pricing” (meaning N1subscript𝑁1N\_{1} rather small) and one final “full pricing” (meaning N2subscript𝑁2N\_{2} large). In theory, this corresponds to L=3𝐿3L=3 with q2=nwsubscript𝑞2subscript𝑛𝑤q\_{2}=n\_{w}, δ​N3=0𝛿subscript𝑁30\delta N\_{3}=0 and δ​N2→∞→𝛿subscript𝑁2\delta N\_{2}\to\infty. As δ​N2→∞→𝛿subscript𝑁2\delta N\_{2}\to\infty, the second and third terms in ([14](#S2.E14 "In Corollary 2.3. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")) vanish, as well as the component of the first term corresponding to ℓ=2ℓ2\ell=2. We therefore neglect them. In practice, we only take N2subscript𝑁2N\_{2} large enough (and given) from the point of view of the bank, and minimize over (q1,N1)subscript𝑞1subscript𝑁1(q\_{1},N\_{1}) the remaining term in ([14](#S2.E14 "In Corollary 2.3. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")):

|  |  |  |
| --- | --- | --- |
|  | F1∞​(q1):=(ns−q1)1p​max(i,k)∈[[1,nw]]×[[q1+1,ns]]⁡(μi−μk)​e−N1​(μi−μk)22​p​(σ¯2+c​(μi−μk)),assignsuperscriptsubscript𝐹1subscript𝑞1superscriptsubscript𝑛𝑠subscript𝑞11𝑝subscript𝑖𝑘delimited-[]1subscript𝑛𝑤delimited-[]subscript𝑞11subscript𝑛𝑠superscript𝜇𝑖superscript𝜇𝑘superscript𝑒subscript𝑁1superscriptsuperscript𝜇𝑖superscript𝜇𝑘22𝑝superscript¯𝜎2𝑐superscript𝜇𝑖superscript𝜇𝑘\displaystyle F\_{1}^{\infty}(q\_{1}):=(n\_{s}-q\_{1})^{\frac{1}{p}}\max\_{(i,k)\in[\![1,n\_{w}]\!]\times[\![q\_{1}+1,n\_{s}]\!]}(\mu^{i}-\mu^{k})e^{-\frac{N\_{1}(\mu^{i}-\mu^{k})^{2}}{2p(\overline{\sigma}^{2}+c(\mu^{i}-\mu^{k}))}}, |  |

in which σ¯¯𝜎\bar{\sigma} is estimated to be as in ([19](#S2.E19 "In 2.4 Optimal a-priori allocation by deterministic dynamic programming based on fixed a-priori bounds ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")),
under the computation cost constraint

|  |  |  |
| --- | --- | --- |
|  | C​(N1,q1)=q1​(N2−N1)+ns​N1≤KCsubscript𝑁1subscript𝑞1subscript𝑞1subscript𝑁2subscript𝑁1subscript𝑛𝑠subscript𝑁1𝐾{\rm C}\left(N\_{1},q\_{1}\right)=q\_{1}(N\_{2}-N\_{1})+n\_{s}N\_{1}\leq K |  |

for some given maximal cost K∈ℕ∗𝐾superscriptℕK\in{\mathbb{N}}^{\*}.

For N1subscript𝑁1N\_{1} (or K𝐾K) large enough, the condition ([20](#S2.E20 "In 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")) leads to minimizing over q1∈[[nw,ns]]∩[1,K/N2]subscript𝑞1delimited-[]subscript𝑛𝑤subscript𝑛𝑠1𝐾subscript𝑁2q\_{1}\in[\![n\_{w},n\_{s}]\!]\cap[1,K/N\_{2}] the upper-bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | h0p​(q1):=(ns−q1)1p×(q1+1−nw)​δ0​exp⁡(−(K−q1​N2)​(q1+1−nw)2​δ022​p​(ns−q1)​(σ¯2+c​(q1+1−nw)​δ0)).assignsubscriptsuperscriptℎ𝑝0subscript𝑞1superscriptsubscript𝑛𝑠subscript𝑞11𝑝subscript𝑞11subscript𝑛𝑤subscript𝛿0𝐾subscript𝑞1subscript𝑁2superscriptsubscript𝑞11subscript𝑛𝑤2superscriptsubscript𝛿022𝑝subscript𝑛𝑠subscript𝑞1superscript¯𝜎2𝑐subscript𝑞11subscript𝑛𝑤subscript𝛿0h^{p}\_{0}(q\_{1}):=(n\_{s}-q\_{1})^{{\frac{1}{p}}}\times(q\_{1}+1-n\_{w})\delta\_{0}\exp\left(-\frac{\left(K-q\_{1}N\_{2}\right)(q\_{1}+1-n\_{w})^{2}\delta\_{0}^{2}}{2p(n\_{s}{-q\_{1}})\left(\overline{\sigma}^{2}+c\left(q\_{1}+1-n\_{w}\right)\delta\_{0}\right)}\right). |  | (21) |

The optimal q1∗superscriptsubscript𝑞1q\_{1}^{\*} can then be found easily by performing a one-dimensional numerical minimization. Upon replacing ns−q1subscript𝑛𝑠subscript𝑞1n\_{s}{-q\_{1}} by nssubscript𝑛𝑠n\_{s} in the denominator of the exponential term, which provides a further upper-bound, the optimum can even be computed explicitly, see Appendix [A](#A1 "Appendix A Proxy of the optimal strategy for the heuristic (21) ‣ Computation of Expected Shortfall by fast detection of worst scenarios"). This provides a very easy to use algorithm.

Considering the case p=1𝑝1p=1, let us now perform first numerical tests to see if the proxy based on h01superscriptsubscriptℎ01h\_{0}^{1} is far from F1∞subscriptsuperscript𝐹1F^{\infty}\_{1}. We use the parameters of Tables [1](#S2.T1 "Table 1 ‣ 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") and [2](#S2.T2 "Table 2 ‣ 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") below and μi=−i​δ0superscript𝜇𝑖𝑖subscript𝛿0\mu^{i}=-i\delta\_{0}, i≤ns𝑖subscript𝑛𝑠i\leq n\_{s}, where δ0:=(μnw−μ100)/(100−nw)assignsubscript𝛿0superscript𝜇subscript𝑛𝑤superscript𝜇100100subscript𝑛𝑤\delta\_{0}:=(\mu^{n\_{w}}-\mu^{100})/(100-n\_{w}) for the μisuperscript𝜇𝑖\mu^{i}s of Figure [6](#S2.F6 "Figure 6 ‣ 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios"). In particular, we take c=0𝑐0c=0, see Remark [2.4](#S2.Thmtheorem4 "Remark 2.4. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios").

In Figure [5](#S2.F5 "Figure 5 ‣ 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), the two increasing curves show the optimum q1∗superscriptsubscript𝑞1q\_{1}^{\*} (right axis) as found when applying the deterministic dynamic programming algorithm (dashed line) of Section [2.4](#S2.SS4 "2.4 Optimal a-priori allocation by deterministic dynamic programming based on fixed a-priori bounds ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") associated to the real sample book curve of Figure [6](#S2.F6 "Figure 6 ‣ 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), and the heuristic (solid line) based on ([21](#S2.E21 "In 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")). The two decreasing curves show the corresponding F1∞​(q1∗)subscriptsuperscript𝐹1superscriptsubscript𝑞1F^{\infty}\_{1}(q\_{1}^{\*}) (left axis) found when applying the deterministic dynamic programming algorithm (dotted line) and the heuristic (dashdot line). We see that the heuristic and the real minimizer are extremely close. The noise in the lines associated to the dynamic programming algorithm are due to grid effects.

![Refer to caption](/html/2005.12593/assets/q_star_vs_K_bare_real_mu_keep_final.png)


Figure 5: q1∗superscriptsubscript𝑞1q\_{1}^{\*} vs K𝐾K for the distribution of Figure [6](#S2.F6 "Figure 6 ‣ 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")



|  |  |
| --- | --- |
| δ0subscript𝛿0\delta\_{0} | 2 766 |
| c𝑐c | 0 |
| σ¯¯𝜎\bar{\sigma} | 2​(1−ρ)× 2 200 00021𝜌2200000\sqrt{2(1-\rho)}\times\,2\,200\,000 |
| ρ𝜌\rho | 0.60.60.6 |
| nssubscript𝑛𝑠n\_{s} | 253 |
| nwsubscript𝑛𝑤n\_{w} | 6 |

Table 1:  Sample Book Parameters



|  |  |
| --- | --- |
| K𝐾K | 107superscript10710^{7} |
| N2subscript𝑁2N\_{2} | 105superscript10510^{5} |

Table 2:  Computing Power

![Refer to caption](/html/2005.12593/assets/raw_mu_graph_bare.png)


Figure 6: Sample book distribution : i↦μimaps-to𝑖superscript𝜇𝑖i\mapsto\mu^{i} for i≤ns𝑖subscript𝑛𝑠i\leq n\_{s}

## 3 Adaptative algorithm

Although the true value θ∘=(μ∘,Σ∘)subscript𝜃subscript𝜇subscriptΣ\theta\_{\circ}=(\mu\_{\circ},\Sigma\_{\circ}) of the vector of means and of the covariance matrix of P|sP\_{|\rm s} are unknown, we can set on it a prior distribution, e.g. based on previous Monte Carlo experiments, rather than just working on robust bounds as in the end of Section [2.4](#S2.SS4 "2.4 Optimal a-priori allocation by deterministic dynamic programming based on fixed a-priori bounds ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios"). Since the estimation of ESES{\rm ES} uses Monte Carlo simulations of P|sP\_{|\rm s}, the knowledge of these quantities can be improved along the different steps ℓℓ\ell of our estimation procedure. This suggests an adaptative algorithm for the optimization of the numerical effort allocation, in which we learn progressively the true value of these parameters, or part of them.
From now on, we therefore view the true value of the parameters as a random variable θ~:=(μ~,Σ~)assign~𝜃~𝜇~Σ\tilde{\theta}:=(\tilde{\mu},\tilde{\Sigma}) on which a prior law ν0subscript𝜈0\nu\_{0} is set. At each step ℓℓ\ell, new Monte Carlo simulations will allow us to update this prior, and our strategy for the next steps accordingly.

### 3.1 Error bounds and convergence for predictable strategies

Let us first adapt the proof of Proposition [2.2](#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") and Corollary [2.3](#S2.Thmtheorem3 "Corollary 2.3. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") to the case where controls are not deterministic but stochastic processes. Given a stochastic process α𝛼\alpha with values in 𝒬×𝒩𝒬𝒩{\mathcal{Q}}\times{\mathcal{N}}, we set (qα,Nα):=αassignsuperscript𝑞𝛼superscript𝑁𝛼𝛼(q^{\alpha},N^{\alpha}):=\alpha where qαsuperscript𝑞𝛼q^{\alpha} and Nαsuperscript𝑁𝛼N^{\alpha} are respectively 𝒬𝒬{\mathcal{Q}} and 𝒩𝒩{\mathcal{N}}-valued. We then define μ^α=(μ^ℓα)ℓ≤Lsuperscript^𝜇𝛼subscriptsubscriptsuperscript^𝜇𝛼ℓℓ𝐿\hat{\mu}^{\alpha}=(\hat{\mu}^{\alpha}\_{\ell})\_{\ell\leq L}, (ℑℓα,𝔪ℓα)ℓ≤Lsubscriptsubscriptsuperscriptℑ𝛼ℓsubscriptsuperscript𝔪𝛼ℓℓ𝐿({\mathfrak{I}}^{\alpha}\_{\ell},{\mathfrak{m}}^{\alpha}\_{\ell})\_{\ell\leq L} as in Section [2.1](#S2.SS1 "2.1 The algorithm ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") except that we see μ^ℓαsubscriptsuperscript^𝜇𝛼ℓ\hat{\mu}^{\alpha}\_{\ell} as a qℓαsubscriptsuperscript𝑞𝛼ℓq^{\alpha}\_{\ell}-dimensional random variables with entries given by (μ^ℓα,i)i∈ℑℓαsubscriptsubscriptsuperscript^𝜇

𝛼𝑖ℓ𝑖subscriptsuperscriptℑ𝛼ℓ(\hat{\mu}^{\alpha,i}\_{\ell})\_{i\in{\mathfrak{I}}^{\alpha}\_{\ell}}. We use the same convention for δ​μ^ℓα𝛿subscriptsuperscript^𝜇𝛼ℓ\delta\hat{\mu}^{\alpha}\_{\ell}, recall ([9](#S2.E9 "In 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")). We say that α𝛼\alpha is admissible if it is predictable with respect to (ℱℓα)ℓ≤Lsubscriptsubscriptsuperscriptℱ𝛼ℓℓ𝐿({\mathcal{F}}^{\alpha}\_{\ell})\_{\ell\leq L} in which ℱ0αsubscriptsuperscriptℱ𝛼0{\mathcal{F}}^{\alpha}\_{0} is trivial and ℱℓα=ℱℓ−1α∨σ​(Pji,(i,j)∈ℑℓα×[[1,Nℓα]])subscriptsuperscriptℱ𝛼ℓsubscriptsuperscriptℱ𝛼ℓ1𝜎

superscriptsubscript𝑃𝑗𝑖𝑖𝑗
subscriptsuperscriptℑ𝛼ℓdelimited-[]1subscriptsuperscript𝑁𝛼ℓ{\mathcal{F}}^{\alpha}\_{\ell}={\mathcal{F}}^{\alpha}\_{\ell-1}\vee\sigma(P\_{j}^{i},(i,j)\in{\mathfrak{I}}^{\alpha}\_{\ell}\times[\![1,N^{\alpha}\_{\ell}]\!]). We call 𝒜adsuperscript𝒜ad{\mathcal{A}}^{\rm ad} the collection of such processes. Then, one defines

|  |  |  |
| --- | --- | --- |
|  | ES^α:=1nw​∑i=1nwμ^Lα,𝔪L−1α​(i),α∈𝒜ad.formulae-sequenceassignsuperscript^ES𝛼1subscript𝑛𝑤superscriptsubscript𝑖1subscript𝑛𝑤subscriptsuperscript^𝜇  𝛼superscriptsubscript𝔪𝐿1𝛼𝑖𝐿𝛼superscript𝒜ad\widehat{\rm ES}^{\alpha}:=\frac{1}{n\_{w}}\sum\_{i=1}^{n\_{w}}\hat{\mu}^{\alpha,{\mathfrak{m}}\_{L-1}^{\alpha}(i)}\_{L},\;\alpha\in{\mathcal{A}}^{\rm ad}. |  |

The true value of the expected shortfall is now also written as a random variable

|  |  |  |
| --- | --- | --- |
|  | ES~:=1nw​∑i=1nwμ~𝔪~​(i),assign~ES1subscript𝑛𝑤superscriptsubscript𝑖1subscript𝑛𝑤superscript~𝜇~𝔪𝑖\widetilde{\rm ES}:=\frac{1}{n\_{w}}\sum\_{i=1}^{n\_{w}}\tilde{\mu}^{\tilde{\mathfrak{m}}(i)}, |  |

in which 𝔪~~𝔪\tilde{\mathfrak{m}} is the random permutation such that

|  |  |  |
| --- | --- | --- |
|  | {μ~𝔪~​(1)≥μ~𝔪~​(2)≥…≥μ~𝔪~​(ns),𝔪~​(i)<𝔪~​(i′)​ if ​μ~𝔪~​(i)=μ~𝔪~​(i′)​ for ​1≤i<i′≤ns.casessuperscript~𝜇~𝔪1superscript~𝜇~𝔪2…superscript~𝜇~𝔪subscript𝑛𝑠~𝔪𝑖~𝔪superscript𝑖′ if superscript~𝜇~𝔪𝑖superscript~𝜇~𝔪superscript𝑖′ for 1𝑖superscript𝑖′subscript𝑛𝑠\left\{\begin{array}[]{l}\tilde{\mu}^{\tilde{\mathfrak{m}}(1)}\geq\tilde{\mu}^{\tilde{\mathfrak{m}}(2)}\geq\ldots\geq\tilde{\mu}^{\tilde{\mathfrak{m}}(n\_{s})},\\ \tilde{\mathfrak{m}}(i)<\tilde{\mathfrak{m}}(i^{\prime})\;\mbox{ if }\tilde{\mu}^{\tilde{\mathfrak{m}}(i)}=\tilde{\mu}^{\tilde{\mathfrak{m}}(i^{\prime})}\mbox{ for }1\leq i<i^{\prime}\leq n\_{s}.\end{array}\right. |  |

We let ℳℳ{\mathcal{M}} be a collection of laws on ℝns×𝕊nssuperscriptℝsubscript𝑛𝑠superscript𝕊subscript𝑛𝑠{\mathbb{R}}^{n\_{s}}\times{\mathbb{S}}^{n\_{s}}, where 𝕊nssuperscript𝕊subscript𝑛𝑠{\mathbb{S}}^{n\_{s}} denotes the collection of covariance matrices of size nssubscript𝑛𝑠n\_{s}. Given ν∈ℳ𝜈ℳ\nu\in{\mathcal{M}}, we denote by 𝔼νsuperscript𝔼𝜈{\mathbb{E}}^{\nu} the expectation operator given that θ~~𝜃\tilde{\theta} admits the law ν𝜈\nu. When ν𝜈\nu is a Dirac mass, we retrieve the situation of Section [2](#S2 "2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") (up to re-ordering in a deterministic way the components of μ𝜇\mu).

We first provide a natural extension of Proposition [2.2](#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios").

###### Proposition 3.1.

For all p≥1𝑝1p\geq 1, ν∈ℳ𝜈ℳ\nu\in{\mathcal{M}}, and α∈𝒜ad𝛼superscript𝒜ad\alpha\in{\mathcal{A}}^{\rm ad},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼ν​[|ES~−ES^α|p]1p≤superscript𝔼𝜈superscriptdelimited-[]superscript~ESsuperscript^ES𝛼𝑝1𝑝absent\displaystyle\mathbb{E}^{\nu}\left[\left|\widetilde{\rm ES}-\widehat{\rm ES}^{\alpha}\right|^{p}\right]^{\frac{1}{p}}\leq | 1nw​𝔼ν​[|∑i∈ℑL−1αμ^Lα,i−μ~i|p]1p1subscript𝑛𝑤superscript𝔼𝜈superscriptdelimited-[]superscriptsubscript𝑖superscriptsubscriptℑ𝐿1𝛼superscriptsubscript^𝜇𝐿  𝛼𝑖superscript~𝜇𝑖𝑝1𝑝\displaystyle\frac{1}{n\_{w}}{\mathbb{E}}^{\nu}\left[\left|\sum\_{i\in{\mathfrak{I}}\_{L-1}^{\alpha}}\hat{\mu}\_{L}^{\alpha,i}-\tilde{\mu}^{{i}}\right|^{p}\right]^{\frac{1}{p}} |  | (22) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +\displaystyle+ | ∑ℓ=1L−1𝔼ν[δqℓαmax(i,k)∈𝔪~ℓ−1α​([[1,nw]]×[[qℓα+1,qℓ−1α]])(μ~i−μ~k)pℙν[μ^ℓα,k>μ^ℓα,i|ℱℓ−1α∨σ(θ~)]]1p,\displaystyle{\sum\_{\ell=1}^{L-1}{\mathbb{E}}^{\nu}\left[\delta q^{\alpha}\_{\ell}\max\_{(i,k)\in\tilde{\mathfrak{m}}^{\alpha}\_{\ell-1}([\![1,n\_{w}]\!]\times[\![q^{\alpha}\_{\ell}+1,q^{\alpha}\_{\ell-1}]\!])}(\tilde{\mu}^{i}-\tilde{\mu}^{k})^{p}{\mathbb{P}}^{\nu}[\hat{\mu}\_{\ell}^{\alpha,k}>\hat{\mu}\_{\ell}^{\alpha,i}|{\mathcal{F}}^{\alpha}\_{\ell-1}\vee\sigma(\tilde{\theta})]\right]^{\frac{1}{p}}}, |  |

with the convention max∅=0subscript0\max\_{\emptyset}=0 and in which 𝔪~ℓ−1αsubscriptsuperscript~𝔪𝛼ℓ1\tilde{\mathfrak{m}}^{\alpha}\_{\ell-1} is defined as 𝔪~~𝔪\tilde{\mathfrak{m}} but on the subset ℑℓ−1αsubscriptsuperscriptℑ𝛼ℓ1{\mathfrak{I}}^{\alpha}\_{\ell-1} instead of ℑ0α=[[1,ns]]subscriptsuperscriptℑ𝛼0delimited-[]1subscript𝑛𝑠{\mathfrak{I}}^{\alpha}\_{0}=[\![1,n\_{s}]\!].

###### Proof.

We proceed as in the proof of Proposition [2.2](#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") to obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ν​[|ES~−ES^α|p]1p≤superscript𝔼𝜈superscriptdelimited-[]superscript~ESsuperscript^ES𝛼𝑝1𝑝absent\displaystyle\mathbb{E}^{\nu}\left[\left|\widetilde{\rm ES}-\widehat{\rm ES}^{\alpha}\right|^{p}\right]^{\frac{1}{p}}\leq | 𝔼ν​[|1nw​∑i≤nwμ^Lα,𝔪L−1α​(i)−μ~𝔪L−1α​(i)|p]1p+𝔼ν​[|1nw​∑i≤nwμ~𝔪~​(i)−μ~𝔪L−1α​(i)|p]1p,superscript𝔼𝜈superscriptdelimited-[]superscript1subscript𝑛𝑤subscript𝑖subscript𝑛𝑤superscriptsubscript^𝜇𝐿  𝛼subscriptsuperscript𝔪𝛼𝐿1𝑖superscript~𝜇subscriptsuperscript𝔪𝛼𝐿1𝑖𝑝1𝑝superscript𝔼𝜈superscriptdelimited-[]superscript1subscript𝑛𝑤subscript𝑖subscript𝑛𝑤superscript~𝜇~𝔪𝑖superscript~𝜇subscriptsuperscript𝔪𝛼𝐿1𝑖𝑝1𝑝\displaystyle{\mathbb{E}}^{\nu}\left[\left|\frac{1}{n\_{w}}\sum\_{i\leq n\_{w}}\hat{\mu}\_{L}^{\alpha,{\mathfrak{m}}^{\alpha}\_{L-1}(i)}-\tilde{\mu}^{{\mathfrak{m}}^{\alpha}\_{L-1}(i)}\right|^{p}\right]^{\frac{1}{p}}+{\mathbb{E}}^{\nu}\left[\left|\frac{1}{n\_{w}}\sum\_{i\leq n\_{w}}\tilde{\mu}^{\tilde{\mathfrak{m}}(i)}-\tilde{\mu}^{{\mathfrak{m}}^{\alpha}\_{L-1}(i)}\right|^{p}\right]^{\frac{1}{p}}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ν​[|1nw​∑i≤nwμ^Lα,𝔪L−1α​(i)−μ~𝔪L−1α​(i)|p]1psuperscript𝔼𝜈superscriptdelimited-[]superscript1subscript𝑛𝑤subscript𝑖subscript𝑛𝑤superscriptsubscript^𝜇𝐿  𝛼subscriptsuperscript𝔪𝛼𝐿1𝑖superscript~𝜇subscriptsuperscript𝔪𝛼𝐿1𝑖𝑝1𝑝\displaystyle{\mathbb{E}}^{\nu}\left[\left|\frac{1}{n\_{w}}\sum\_{i\leq n\_{w}}\hat{\mu}\_{L}^{\alpha,{\mathfrak{m}}^{\alpha}\_{L-1}(i)}-\tilde{\mu}^{{\mathfrak{m}}^{\alpha}\_{L-1}(i)}\right|^{p}\right]^{\frac{1}{p}} | =1nw​𝔼ν​[|∑i∈ℑL−1αμ^Lα,i−μ~i|p]1p.absent1subscript𝑛𝑤superscript𝔼𝜈superscriptdelimited-[]superscriptsubscript𝑖superscriptsubscriptℑ𝐿1𝛼superscriptsubscript^𝜇𝐿  𝛼𝑖superscript~𝜇𝑖𝑝1𝑝\displaystyle=\frac{1}{n\_{w}}{\mathbb{E}}^{\nu}\left[\left|\sum\_{i\in{\mathfrak{I}}\_{L-1}^{\alpha}}\hat{\mu}\_{L}^{\alpha,i}-\tilde{\mu}^{i}\right|^{p}\right]^{\frac{1}{p}}. |  |

We define 𝔨ℓαsubscriptsuperscript𝔨𝛼ℓ{\mathfrak{k}}^{\alpha}\_{\ell} as 𝔨ℓsubscript𝔨ℓ{\mathfrak{k}}\_{\ell} in the proof of Proposition [2.2](#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") for the strategy α𝛼\alpha, with ℛℓsubscriptℛℓ\mathcal{R}\_{\ell} replaced by ℛℓαsubscriptsuperscriptℛ𝛼ℓ\mathcal{R}^{\alpha}\_{\ell} :=assign:= ℑℓα∖𝔪~​(Sqℓα​[𝔪~−1​(ℑℓ−1)])subscriptsuperscriptℑ𝛼ℓ~𝔪subscriptSsubscriptsuperscript𝑞𝛼ℓdelimited-[]superscript~𝔪1subscriptℑℓ1{\mathfrak{I}}^{\alpha}\_{\ell}\setminus\tilde{\mathfrak{m}}({\rm S}\_{q^{\alpha}\_{\ell}}[\tilde{\mathfrak{m}}^{-1}({\mathfrak{I}}\_{\ell-1})]). Then,

|  |  |  |
| --- | --- | --- |
|  | 𝔼ν​[|1nw​∑i≤nwμ~𝔪~​(i)−μ~𝔪L−1α​(i)|p]1psuperscript𝔼𝜈superscriptdelimited-[]superscript1subscript𝑛𝑤subscript𝑖subscript𝑛𝑤superscript~𝜇~𝔪𝑖superscript~𝜇subscriptsuperscript𝔪𝛼𝐿1𝑖𝑝1𝑝\displaystyle{\mathbb{E}}^{\nu}\left[\left|\frac{1}{n\_{w}}\sum\_{i\leq n\_{w}}\tilde{\mu}^{\tilde{\mathfrak{m}}(i)}-\tilde{\mu}^{{\mathfrak{m}}^{\alpha}\_{L-1}(i)}\right|^{p}\right]^{\frac{1}{p}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝔼ν​[|1nw​∑i≤nw∑ℓ=1L−1(μ~𝔪~​(i)−μ~𝔨ℓα​(𝔪~​(i)))​𝟏{𝔪~​(i)∈ℑℓ−1α∖ℑℓα}|p]1pabsentsuperscript𝔼𝜈superscriptdelimited-[]superscript1subscript𝑛𝑤subscript𝑖subscript𝑛𝑤superscriptsubscriptℓ1𝐿1superscript~𝜇~𝔪𝑖superscript~𝜇subscriptsuperscript𝔨𝛼ℓ~𝔪𝑖subscript1~𝔪𝑖subscriptsuperscriptℑ𝛼ℓ1subscriptsuperscriptℑ𝛼ℓ𝑝1𝑝\displaystyle\leq{\mathbb{E}}^{\nu}\left[\left|\frac{1}{n\_{w}}\sum\_{i\leq n\_{w}}\sum\_{\ell=1}^{L-1}(\tilde{\mu}^{\tilde{\mathfrak{m}}(i)}-\tilde{\mu}^{{\mathfrak{k}}^{\alpha}\_{\ell}(\tilde{\mathfrak{m}}(i))}){\mathbf{1}}\_{\{\tilde{\mathfrak{m}}(i)\in{\mathfrak{I}}^{\alpha}\_{\ell-1}\setminus{\mathfrak{I}}^{\alpha}\_{\ell}\}}\right|^{p}\right]^{\frac{1}{p}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤1nw​∑ℓ=1L−1∑i≤nw𝔼ν​[|(μ~𝔪~​(i)−μ~𝔨ℓα​(𝔪~​(i)))|p​𝟏{𝔪~​(i)∈ℑℓ−1α∖ℑℓα}]1pabsent1subscript𝑛𝑤superscriptsubscriptℓ1𝐿1subscript𝑖subscript𝑛𝑤superscript𝔼𝜈superscriptdelimited-[]superscriptsuperscript~𝜇~𝔪𝑖superscript~𝜇subscriptsuperscript𝔨𝛼ℓ~𝔪𝑖𝑝subscript1~𝔪𝑖subscriptsuperscriptℑ𝛼ℓ1subscriptsuperscriptℑ𝛼ℓ1𝑝\displaystyle\leq\frac{1}{n\_{w}}\sum\_{\ell=1}^{L-1}\sum\_{i\leq n\_{w}}{\mathbb{E}}^{\nu}\left[\left|(\tilde{\mu}^{\tilde{\mathfrak{m}}(i)}-\tilde{\mu}^{{\mathfrak{k}}^{\alpha}\_{\ell}(\tilde{\mathfrak{m}}(i))})\right|^{p}{\mathbf{1}}\_{\{\tilde{\mathfrak{m}}(i)\in{\mathfrak{I}}^{\alpha}\_{\ell-1}\setminus{\mathfrak{I}}^{\alpha}\_{\ell}\}}\right]^{\frac{1}{p}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤1nw​∑ℓ=1L−1∑i≤nw𝔼ν​[∑k∈𝔪~ℓ−1α​([[qℓα+1,qℓ−1α]])𝔼ν​[|(μ~𝔪~​(i)−μ~k)|p​𝟏{𝔪~​(i)∈ℑℓ−1α∖ℑℓα,𝔨ℓα​(𝔪~​(i))=k}|ℱℓ−1α∨σ​(θ~)]]1pabsent1subscript𝑛𝑤superscriptsubscriptℓ1𝐿1subscript𝑖subscript𝑛𝑤superscript𝔼𝜈superscriptdelimited-[]subscript𝑘subscriptsuperscript~𝔪𝛼ℓ1delimited-[]subscriptsuperscript𝑞𝛼ℓ1subscriptsuperscript𝑞𝛼ℓ1superscript𝔼𝜈delimited-[]conditionalsuperscriptsuperscript~𝜇~𝔪𝑖superscript~𝜇𝑘𝑝subscript1formulae-sequence~𝔪𝑖subscriptsuperscriptℑ𝛼ℓ1subscriptsuperscriptℑ𝛼ℓsubscriptsuperscript𝔨𝛼ℓ~𝔪𝑖𝑘subscriptsuperscriptℱ𝛼ℓ1𝜎~𝜃1𝑝\displaystyle\leq{\frac{1}{n\_{w}}\sum\_{\ell=1}^{L-1}\sum\_{i\leq n\_{w}}{\mathbb{E}}^{\nu}\left[\sum\_{k\in\tilde{\mathfrak{m}}^{\alpha}\_{\ell-1}([\![q^{\alpha}\_{\ell}+1,q^{\alpha}\_{\ell-1}]\!])}{\mathbb{E}}^{\nu}\left[\left|(\tilde{\mu}^{\tilde{\mathfrak{m}}(i)}-\tilde{\mu}^{k})\right|^{p}{\mathbf{1}}\_{\{\tilde{\mathfrak{m}}(i)\in{\mathfrak{I}}^{\alpha}\_{\ell-1}\setminus{\mathfrak{I}}^{\alpha}\_{\ell},{\mathfrak{k}}^{\alpha}\_{\ell}(\tilde{\mathfrak{m}}(i))=k\}}|{\mathcal{F}}^{\alpha}\_{\ell-1}\vee\sigma(\tilde{\theta})\right]\right]^{\frac{1}{p}}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∑ℓ=1L−1𝔼ν[δqℓαmax(i,k)∈𝔪~ℓ−1α​([[1,nw]]×[[qℓα+1,qℓ−1α]])(μ~i−μ~k)pℙν[μ^ℓα,k>μ^ℓα,i|ℱℓ−1α∨σ(θ~)]]1p.\displaystyle{\leq\sum\_{\ell=1}^{L-1}{\mathbb{E}}^{\nu}\left[\delta q^{\alpha}\_{\ell}\max\_{(i,k)\in\tilde{\mathfrak{m}}^{\alpha}\_{\ell-1}([\![1,n\_{w}]\!]\times[\![q^{\alpha}\_{\ell}+1,q^{\alpha}\_{\ell-1}]\!])}(\tilde{\mu}^{i}-\tilde{\mu}^{k})^{p}{\mathbb{P}}^{\nu}[\hat{\mu}\_{\ell}^{\alpha,k}>\hat{\mu}\_{\ell}^{\alpha,i}|{\mathcal{F}}^{\alpha}\_{\ell-1}\vee\sigma(\tilde{\theta})]\right]^{\frac{1}{p}}.} |  |

∎

###### Remark 3.2.

Note that, when α𝛼\alpha is deterministic and ν𝜈\nu is concentrated on a Dirac, the right-hand side of ([22](#S3.E22 "In Proposition 3.1. ‣ 3.1 Error bounds and convergence for predictable strategies ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios")) is bounded from above by

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 1nw​δ​NLαNLα​max1≤ii<…<inw≤ns​∑j=1nw𝔼ν​[|δ​μ^Lα,ij−μ~ij|p]1p+1nw​NL−1αNLα​∑i=1ns𝔼ν​[|μ^L−1α,i−μ~i|p]1p1subscript𝑛𝑤𝛿superscriptsubscript𝑁𝐿𝛼superscriptsubscript𝑁𝐿𝛼1subscript𝑖𝑖…subscript𝑖subscript𝑛𝑤subscript𝑛𝑠superscriptsubscript𝑗1subscript𝑛𝑤superscript𝔼𝜈superscriptdelimited-[]superscript𝛿subscriptsuperscript^𝜇  𝛼subscript𝑖𝑗𝐿superscript~𝜇subscript𝑖𝑗𝑝1𝑝1subscript𝑛𝑤superscriptsubscript𝑁𝐿1𝛼superscriptsubscript𝑁𝐿𝛼superscriptsubscript𝑖1subscript𝑛𝑠superscript𝔼𝜈superscriptdelimited-[]superscriptsubscriptsuperscript^𝜇  𝛼𝑖𝐿1superscript~𝜇𝑖𝑝1𝑝\displaystyle\frac{1}{n\_{w}}\frac{\delta N\_{L}^{\alpha}}{N\_{L}^{\alpha}}\underset{1\leq i\_{i}<...<i\_{n\_{w}}\leq n\_{s}}{\max}\sum\_{j=1}^{n\_{w}}{\mathbb{E}}^{\nu}\left[\left|\delta\hat{\mu}^{\alpha,i\_{j}}\_{L}-\tilde{\mu}^{i\_{j}}\right|^{p}\right]^{\frac{1}{p}}+\frac{1}{n\_{w}}\frac{N\_{L-1}^{\alpha}}{N\_{L}^{\alpha}}\sum\_{i=1}^{n\_{s}}{\mathbb{E}}^{\nu}\left[\left|\hat{\mu}^{\alpha,i}\_{L-1}-\tilde{\mu}^{i}\right|^{p}\right]^{\frac{1}{p}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +\displaystyle+ | ∑i=1ns∑ℓ=1L−1(δqℓα)1p𝔼ν[max(i,k)∈𝔪~​[[1,nw]]×[[qℓα+1,ns]](μ~i−μ~k)pℙν[μ^ℓα,k>μ^ℓα,i|ℱℓ−1α∨σ(θ~)]]1p,\displaystyle\sum\_{i=1}^{n\_{s}}\sum\_{\ell=1}^{L-1}\left(\delta q^{\alpha}\_{\ell}\right)^{\frac{1}{p}}{\mathbb{E}}^{\nu}\left[\max\_{(i,k)\in\tilde{\mathfrak{m}}[\![1,n\_{w}]\!]\times[\![q^{\alpha}\_{\ell}+1,n\_{s}]\!]}(\tilde{\mu}^{i}-\tilde{\mu}^{k})^{p}{\mathbb{P}}^{\nu}[\hat{\mu}\_{\ell}^{\alpha,k}>\hat{\mu}\_{\ell}^{\alpha,i}|{\mathcal{F}}^{\alpha}\_{\ell-1}\vee\sigma(\tilde{\theta})]\right]^{\frac{1}{p}}, |  |

which coincides with the bound of Proposition [2.2](#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.2 General a-priori bound on the 𝕃^𝑝 error ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")

The above guarantees the convergence of the algorithm.

###### Proposition 3.3.

Let (Kn)n≥1⊂ℕ∗subscriptsuperscript𝐾𝑛𝑛1superscriptℕ(K^{n})\_{n\geq 1}\subset{\mathbb{N}}^{\*} be a sequence converging to infinity and let (αn)n≥1subscriptsuperscript𝛼𝑛𝑛1(\alpha^{n})\_{n\geq 1} be a sequence in 𝒜adsuperscript𝒜ad{\mathcal{A}}^{\rm ad} such that
C​(qαn,Nαn)≤KnCsuperscript𝑞superscript𝛼𝑛superscript𝑁superscript𝛼𝑛superscript𝐾𝑛{\rm C}(q^{\alpha^{n}},N^{\alpha^{n}})\leq K^{n} for each n≥1𝑛1n\geq 1. Assume further that
min1≤ℓ≤L⁡Nℓαn→∞→subscript1ℓ𝐿subscriptsuperscript𝑁superscript𝛼𝑛ℓ\min\_{1\leq\ell\leq L}N^{\alpha^{n}}\_{\ell}\to\infty a.s.
Let ν𝜈\nu be concentrated on the Dirac mass on θ∘subscript𝜃\theta\_{\circ}. Then,

|  |  |  |
| --- | --- | --- |
|  | 𝔼ν​[|ES~−ES^αn|p]→0​ as n→∞.→superscript𝔼𝜈delimited-[]superscript~ESsuperscript^ESsuperscript𝛼𝑛𝑝0 as n→∞.\mathbb{E}^{\nu}\left[\left|\widetilde{\rm ES}-\widehat{\rm ES}^{\alpha^{n}}\right|^{p}\right]\to 0\;\;\mbox{ as $n\to\infty$.} |  |

###### Proof.

It suffices to use the fact that, for some Cp>0subscript𝐶𝑝0C\_{p}>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ν​[|μ^ℓαn,i−μ~i|p]superscript𝔼𝜈delimited-[]superscriptsuperscriptsubscript^𝜇ℓ  superscript𝛼𝑛𝑖superscript~𝜇𝑖𝑝\displaystyle{\mathbb{E}}^{\nu}\left[\left|\hat{\mu}\_{\ell}^{\alpha^{n},i}-\tilde{\mu}^{i}\right|^{p}\right] | ≤Cp​𝔼ν​[δ​NℓαnNℓαn​𝔼ν​[|δ​μ^ℓαn,i−μ∘i|p|ℱℓ−1αn]]+Cp​𝔼ν​[Nℓ−1αnNℓαn​|μ^ℓ−1αn,i−μ∘i|p],absentsubscript𝐶𝑝superscript𝔼𝜈delimited-[]𝛿subscriptsuperscript𝑁superscript𝛼𝑛ℓsubscriptsuperscript𝑁superscript𝛼𝑛ℓsuperscript𝔼𝜈delimited-[]conditionalsuperscript𝛿superscriptsubscript^𝜇ℓ  superscript𝛼𝑛𝑖subscriptsuperscript𝜇𝑖𝑝subscriptsuperscriptℱsuperscript𝛼𝑛ℓ1subscript𝐶𝑝superscript𝔼𝜈delimited-[]subscriptsuperscript𝑁superscript𝛼𝑛ℓ1subscriptsuperscript𝑁superscript𝛼𝑛ℓsuperscriptsuperscriptsubscript^𝜇ℓ1  superscript𝛼𝑛𝑖subscriptsuperscript𝜇𝑖𝑝\displaystyle\leq C\_{p}{\mathbb{E}}^{\nu}\left[\frac{\delta N^{\alpha^{n}}\_{\ell}}{N^{\alpha^{n}}\_{\ell}}{\mathbb{E}}^{\nu}\left[\left|\delta\hat{\mu}\_{\ell}^{\alpha^{n},i}-\mu^{i}\_{\circ}\right|^{p}|{\mathcal{F}}^{\alpha^{n}}\_{\ell-1}\right]\right]+C\_{p}{\mathbb{E}}^{\nu}\left[\frac{N^{\alpha^{n}}\_{\ell-1}}{N^{\alpha^{n}}\_{\ell}}\left|\hat{\mu}\_{\ell-1}^{\alpha^{n},i}-\mu^{i}\_{\circ}\right|^{p}\right], |  |

in which

|  |  |  |
| --- | --- | --- |
|  | δ​NℓαnNℓαn​𝔼ν​[|δ​μ^ℓαn,i−μ∘i|p|ℱℓ−1αn]→0,ν∘−a.s.,formulae-sequence→𝛿subscriptsuperscript𝑁superscript𝛼𝑛ℓsubscriptsuperscript𝑁superscript𝛼𝑛ℓsuperscript𝔼𝜈delimited-[]conditionalsuperscript𝛿superscriptsubscript^𝜇ℓ  superscript𝛼𝑛𝑖subscriptsuperscript𝜇𝑖𝑝subscriptsuperscriptℱsuperscript𝛼𝑛ℓ1  0subscript𝜈as\frac{\delta N^{\alpha^{n}}\_{\ell}}{N^{\alpha^{n}}\_{\ell}}{\mathbb{E}}^{\nu}\left[\left|\delta\hat{\mu}\_{\ell}^{\alpha^{n},i}-\mu^{i}\_{\circ}\right|^{p}|{\mathcal{F}}^{\alpha^{n}}\_{\ell-1}\right]\to 0,\;\nu\_{\circ}-{\rm a.s.}, |  |

for all ℓ>1ℓ1\ell>1 and i≤ns𝑖subscript𝑛𝑠i\leq n\_{s}. By induction, this implies that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ν​[|μ^ℓαn,i−μ~i|p]=𝔼ν​[|μ^ℓαn,i−μ∘i|p]→0superscript𝔼𝜈delimited-[]superscriptsuperscriptsubscript^𝜇ℓ  superscript𝛼𝑛𝑖superscript~𝜇𝑖𝑝superscript𝔼𝜈delimited-[]superscriptsuperscriptsubscript^𝜇ℓ  superscript𝛼𝑛𝑖subscriptsuperscript𝜇𝑖𝑝→0{\mathbb{E}}^{\nu}\left[\left|\hat{\mu}\_{\ell}^{\alpha^{n},i}-\tilde{\mu}^{i}\right|^{p}\right]={\mathbb{E}}^{\nu}\left[\left|\hat{\mu}\_{\ell}^{\alpha^{n},i}-\mu^{i}\_{\circ}\right|^{p}\right]\to 0 |  |

for all ℓ≤Lℓ𝐿\ell\leq L and i≤ns𝑖subscript𝑛𝑠i\leq n\_{s}. Moreover, for some C>0𝐶0C>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ν​[(μ~i−μ~k)p​ℙν​[μ^ℓαn,k>μ^ℓαn,i|ℱℓ−1α∨σ​(θ~)]]superscript𝔼𝜈delimited-[]superscriptsuperscript~𝜇𝑖superscript~𝜇𝑘𝑝superscriptℙ𝜈delimited-[]superscriptsubscript^𝜇ℓ  superscript𝛼𝑛𝑘conditionalsuperscriptsubscript^𝜇ℓ  superscript𝛼𝑛𝑖subscriptsuperscriptℱ𝛼ℓ1𝜎~𝜃\displaystyle{\mathbb{E}}^{\nu}\left[(\tilde{\mu}^{i}-\tilde{\mu}^{k})^{p}{\mathbb{P}}^{\nu}[\hat{\mu}\_{\ell}^{\alpha^{n},k}>\hat{\mu}\_{\ell}^{\alpha^{n},i}|{\mathcal{F}}^{\alpha}\_{\ell-1}\vee\sigma(\tilde{\theta})]\right] | ≤C​𝟏{μ∘i−μ∘k>0}​𝔼ν​[|μ^ℓαn,i−μ^ℓαn,k−(μ∘i−μ∘k)|]μ∘i−μ∘k→0absent𝐶subscript1subscriptsuperscript𝜇𝑖subscriptsuperscript𝜇𝑘0superscript𝔼𝜈delimited-[]superscriptsubscript^𝜇ℓ  superscript𝛼𝑛𝑖superscriptsubscript^𝜇ℓ  superscript𝛼𝑛𝑘subscriptsuperscript𝜇𝑖subscriptsuperscript𝜇𝑘subscriptsuperscript𝜇𝑖subscriptsuperscript𝜇𝑘→0\displaystyle\leq C{\mathbf{1}}\_{\{\mu^{i}\_{\circ}-\mu^{k}\_{\circ}>0\}}\frac{{\mathbb{E}}^{\nu}[|\hat{\mu}\_{\ell}^{\alpha^{n},i}-\hat{\mu}\_{\ell}^{\alpha^{n},k}-(\mu^{i}\_{\circ}-\mu^{k}\_{\circ})|]}{\mu^{i}\_{\circ}-\mu^{k}\_{\circ}}\to 0 |  |

for all i<k𝑖𝑘i<k and ℓ≤L−1ℓ𝐿1\ell\leq L-1.
∎

Using the fact that a control α∈𝒜ad𝛼superscript𝒜ad\alpha\in{\mathcal{A}}^{\rm ad} is predictable, one can then proceed as in the proof of Corollary [2.3](#S2.Thmtheorem3 "Corollary 2.3. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") to derive a more tractable upper-bound. It appeals to the following version of Assumption [1](#Thmassumption1 "Assumption 1. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios").

###### Assumption 2.

There exists c>0𝑐0c>0 such that, for all ν∈ℳ𝜈ℳ\nu\in{\mathcal{M}},

|  |  |  |
| --- | --- | --- |
|  | 𝔼ν[|Z[i,k]|p|σ(θ~)]≤p!​cp−22𝔼ν[Z[i,k]2|σ(θ~)]ν−a.s., for all i,k≤ns,p≥3.\mathbb{E}^{\nu}\left[\left|Z[i,k]\right|^{p}|\sigma(\tilde{\theta})\right]\leq\frac{p!\;c^{p-2}}{2}\mathbb{E}^{\nu}\left[Z[i,k]^{2}|\sigma(\tilde{\theta})\right]\;\nu-{\rm a.s.},\;\mbox{ for all }\;i,k\leq n\_{s},\;p\geq 3. |  |

###### Corollary 3.4.

Let Assumption [2](#Thmassumption2 "Assumption 2. ‣ 3.1 Error bounds and convergence for predictable strategies ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios") holds. Then, for all p≥1𝑝1p\geq 1, α∈𝒜ad𝛼superscript𝒜ad\alpha\in{\mathcal{A}}^{\rm ad} and ν∈ℳ𝜈ℳ\nu\in{\mathcal{M}},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ν​[|ES~−ES^α|p]1p≤superscript𝔼𝜈superscriptdelimited-[]superscript~ESsuperscript^ES𝛼𝑝1𝑝absent\displaystyle\mathbb{E}^{\nu}\left[\left|\widetilde{\rm ES}-\widehat{\rm ES}^{\alpha}\right|^{p}\right]^{\frac{1}{p}}\leq | Fpad​(α,ν)subscriptsuperscriptFad𝑝𝛼𝜈\displaystyle{\rm F}^{\rm ad}\_{p}(\alpha,\nu) |  |

in which

|  |  |  |
| --- | --- | --- |
|  | Fpad​(α,ν):=1nw​𝔼ν​[|∑i∈ℑL−1αμ^Lα,i−μ~i|p]1p+∑ℓ=1L−1𝔼ν​[fpad​(ℓ,α,θ~)]1passignsubscriptsuperscriptFad𝑝𝛼𝜈1subscript𝑛𝑤superscript𝔼𝜈superscriptdelimited-[]superscriptsubscript𝑖superscriptsubscriptℑ𝐿1𝛼superscriptsubscript^𝜇𝐿  𝛼𝑖superscript~𝜇𝑖𝑝1𝑝superscriptsubscriptℓ1𝐿1superscript𝔼𝜈superscriptdelimited-[]subscriptsuperscript𝑓ad𝑝ℓ𝛼~𝜃1𝑝{\rm F}^{\rm ad}\_{p}(\alpha,\nu):=\frac{1}{n\_{w}}{\mathbb{E}}^{\nu}\left[\left|\sum\_{i\in{\mathfrak{I}}\_{L-1}^{\alpha}}\hat{\mu}\_{L}^{\alpha,i}-\tilde{\mu}^{i}\right|^{p}\right]^{\frac{1}{p}}+\sum\_{\ell=1}^{L-1}{\mathbb{E}}^{\nu}\left[f^{\rm ad}\_{p}(\ell,\alpha,\tilde{\theta})\right]^{\frac{1}{p}} |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | fpad(ℓ,α,θ~):=δqℓαmax(i,k)∈𝔪~ℓ−1α​([[1,nw]]×[[qℓα+1,qℓ−1α]])(μ~i−μ~k)p(e−δ​Nℓα​(ρℓα​[i,k])22​(σ~i​k2+c​ρℓα​[i,k])𝟏{ρℓα​[i,k]≥0}+𝟏{ρℓα​[i,k]<0})f^{\rm ad}\_{p}(\ell,\alpha,\tilde{\theta}):=\delta q^{\alpha}\_{\ell}\max\_{(i,k)\in{\tilde{\mathfrak{m}}^{\alpha}\_{\ell-1}([\![1,n\_{w}]\!]\times[\![q^{\alpha}\_{\ell}+1,q^{\alpha}\_{\ell-1}]\!])}}(\tilde{\mu}^{i}-\tilde{\mu}^{k})^{p}\left(e^{-\frac{\delta N^{\alpha}\_{\ell}(\rho^{\alpha}\_{\ell}[i,k])^{2}}{2(\tilde{\sigma}\_{ik}^{2}+c\rho^{\alpha}\_{\ell}[i,k])}}{\mathbf{1}}\_{\{\rho^{\alpha}\_{\ell}[i,k]\geq 0\}}+{\mathbf{1}}\_{\{\rho^{\alpha}\_{\ell}[i,k]<0\}}\right) |  | (23) |

with

|  |  |  |
| --- | --- | --- |
|  | ρℓα​[i,k]:=μ~i−μ~k+Nℓ−1αδ​Nℓα​(μ^ℓ−1α,i−μ^ℓ−1α,k)​ for ℓ≥1 and i,k≤ns.assignsubscriptsuperscript𝜌𝛼ℓ𝑖𝑘superscript~𝜇𝑖superscript~𝜇𝑘subscriptsuperscript𝑁𝛼ℓ1𝛿subscriptsuperscript𝑁𝛼ℓsuperscriptsubscript^𝜇ℓ1  𝛼𝑖superscriptsubscript^𝜇ℓ1  𝛼𝑘 for ℓ≥1 and i,k≤ns.\rho^{\alpha}\_{\ell}[i,k]:=\tilde{\mu}^{i}-\tilde{\mu}^{k}+\frac{N^{\alpha}\_{\ell-1}}{\delta N^{\alpha}\_{\ell}}(\hat{\mu}\_{\ell-1}^{\alpha,i}-\hat{\mu}\_{\ell-1}^{\alpha,k})\mbox{ for $\ell\geq 1$ and $i,k\leq n\_{s}$.} |  |

###### Proof.

We use Bernstein’s inequality, see [[7](#bib.bib7), Theorem 2.1], conditionally to ℱℓ−1α∨σ​(θ~)subscriptsuperscriptℱ𝛼ℓ1𝜎~𝜃{\mathcal{F}}^{\alpha}\_{\ell-1}\vee\sigma(\tilde{\theta}), to deduce that

|  |  |  |
| --- | --- | --- |
|  | ℙν​[μ^ℓα,k>μ^ℓα,i|ℱℓ−1α∨σ​(θ~)]superscriptℙ𝜈delimited-[]superscriptsubscript^𝜇ℓ  𝛼𝑘conditionalsuperscriptsubscript^𝜇ℓ  𝛼𝑖subscriptsuperscriptℱ𝛼ℓ1𝜎~𝜃\displaystyle{\mathbb{P}}^{\nu}[\hat{\mu}\_{\ell}^{\alpha,k}>\hat{\mu}\_{\ell}^{\alpha,i}|{\mathcal{F}}^{\alpha}\_{\ell-1}\vee\sigma(\tilde{\theta})] |  |
|  |  |  |
| --- | --- | --- |
|  | =ℙν​[δ​μ^ℓα,k−μ~k−(δ​μ^ℓα,i−μ~i)>Nℓ−1αδ​Nℓα​(μ^ℓ−1α,i−μ^ℓ−1α,k)−(μ~k−μ~i)|ℱℓ−1α∨σ​(θ~)]absentsuperscriptℙ𝜈delimited-[]𝛿superscriptsubscript^𝜇ℓ  𝛼𝑘superscript~𝜇𝑘𝛿superscriptsubscript^𝜇ℓ  𝛼𝑖superscript~𝜇𝑖subscriptsuperscript𝑁𝛼ℓ1𝛿subscriptsuperscript𝑁𝛼ℓsuperscriptsubscript^𝜇ℓ1  𝛼𝑖superscriptsubscript^𝜇ℓ1  𝛼𝑘conditionalsuperscript~𝜇𝑘superscript~𝜇𝑖subscriptsuperscriptℱ𝛼ℓ1𝜎~𝜃\displaystyle={\mathbb{P}}^{\nu}[\delta\hat{\mu}\_{\ell}^{\alpha,k}-\tilde{\mu}^{k}-(\delta\hat{\mu}\_{\ell}^{\alpha,i}-\tilde{\mu}^{i})>\frac{N^{\alpha}\_{\ell-1}}{\delta N^{\alpha}\_{\ell}}(\hat{\mu}\_{\ell-1}^{\alpha,i}-\hat{\mu}\_{\ell-1}^{\alpha,k})-(\tilde{\mu}^{k}-\tilde{\mu}^{i})|{\mathcal{F}}^{\alpha}\_{\ell-1}\vee\sigma(\tilde{\theta})] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤e−δ​Nℓα​(ρℓα​[i,k])22​(σ~i​k2+c​ρℓα​[i,k])​𝟏{ρℓα​[i,k]≥0}+𝟏{ρℓα​[i,k]<0}.absentsuperscript𝑒𝛿subscriptsuperscript𝑁𝛼ℓsuperscriptsubscriptsuperscript𝜌𝛼ℓ𝑖𝑘22superscriptsubscript~𝜎𝑖𝑘2𝑐subscriptsuperscript𝜌𝛼ℓ𝑖𝑘subscript1subscriptsuperscript𝜌𝛼ℓ𝑖𝑘0subscript1subscriptsuperscript𝜌𝛼ℓ𝑖𝑘0\displaystyle\leq e^{-\frac{\delta N^{\alpha}\_{\ell}(\rho^{\alpha}\_{\ell}[i,k])^{2}}{2(\tilde{\sigma}\_{ik}^{2}+c\rho^{\alpha}\_{\ell}[i,k])}}{\mathbf{1}}\_{\{\rho^{\alpha}\_{\ell}[i,k]\geq 0\}}+{\mathbf{1}}\_{\{\rho^{\alpha}\_{\ell}[i,k]<0\}}. |  |

∎

### 3.2 A generic progressive learning algorithm

Let us now describe how the result of Corollary [3.4](#S3.Thmtheorem4 "Corollary 3.4. ‣ 3.1 Error bounds and convergence for predictable strategies ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios") can be turned into a (stochastic) dynamic programming algorithm, in the spirit of Section [2.4](#S2.SS4 "2.4 Optimal a-priori allocation by deterministic dynamic programming based on fixed a-priori bounds ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), that can be implemented in practice.

By Jensen’s inequality, the upper-bound of Corollary [3.4](#S3.Thmtheorem4 "Corollary 3.4. ‣ 3.1 Error bounds and convergence for predictable strategies ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios") can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ν​[|ES~−ES^α|p]≤Fpad​(0,α,ν)psuperscript𝔼𝜈delimited-[]superscript~ESsuperscript^ES𝛼𝑝subscriptsuperscriptFad𝑝superscript0𝛼𝜈𝑝{\mathbb{E}}^{\nu}\left[\left|\widetilde{\rm ES}-\widehat{\rm ES}^{\alpha}\right|^{p}\right]\leq{\rm F}^{\rm ad}\_{p}(0,\alpha,\nu)^{p} |  | (24) |

where

|  |  |  |
| --- | --- | --- |
|  | Fpad​(0,α,ν):=𝔼ν​[|1nw​∑i∈ℑL−1αμ^Lα,i−μ~i|p+∑ℓ=1L−1fpad​(ℓ,α,θ~)],assignsubscriptsuperscriptFad𝑝0𝛼𝜈superscript𝔼𝜈delimited-[]superscript1subscript𝑛𝑤subscript𝑖superscriptsubscriptℑ𝐿1𝛼superscriptsubscript^𝜇𝐿  𝛼𝑖superscript~𝜇𝑖𝑝superscriptsubscriptℓ1𝐿1subscriptsuperscript𝑓ad𝑝ℓ𝛼~𝜃{\rm F}^{\rm ad}\_{p}(0,\alpha,\nu):={\mathbb{E}}^{\nu}\left[\left|\frac{1}{n\_{w}}\sum\_{i\in{\mathfrak{I}}\_{L-1}^{\alpha}}\hat{\mu}\_{L}^{\alpha,i}-\tilde{\mu}^{i}\right|^{p}+\sum\_{\ell=1}^{L-1}f^{\rm ad}\_{p}(\ell,\alpha,\tilde{\theta})\right], |  |

to which we can associate the optimal control problem101010Only the conditional law given ℱℓαsubscriptsuperscriptℱ𝛼ℓ{\mathcal{F}}^{\alpha}\_{\ell} of the components of θ~~𝜃\tilde{\theta} corresponding to indexes in ℑℓαsubscriptsuperscriptℑ𝛼ℓ{\mathfrak{I}}^{\alpha}\_{\ell} play a role in the definition of F^pad​(ℓ,α,ν)subscriptsuperscript^Fad𝑝ℓ𝛼𝜈\hat{\rm F}^{\rm ad}\_{p}(\ell,\alpha,\nu) and Fpad​(ℓ,α,ν)subscriptsuperscriptFad𝑝ℓ𝛼𝜈{\rm F}^{\rm ad}\_{p}(\ell,\alpha,\nu) below. To avoid introducing new complex notations, we shall indifferently take ν𝜈\nu or only the conditional law of the corresponding components as an argument, depending on the context.

|  |  |  |
| --- | --- | --- |
|  | F^pad​(ℓ,α,ν)=ess​infα′∈𝒜ad​(ℓ,α)Fpad​(ℓ,α′,ν)​ for 0≤ℓ≤L−1, ν∈ℳ and α∈𝒜ad,subscriptsuperscript^Fad𝑝ℓ𝛼𝜈esssubscriptinfimumsuperscript𝛼′superscript𝒜adℓ𝛼subscriptsuperscriptFad𝑝ℓsuperscript𝛼′𝜈 for 0≤ℓ≤L−1, ν∈ℳ and α∈𝒜ad,\displaystyle\hat{\rm F}^{\rm ad}\_{p}(\ell,\alpha,\nu)={\rm ess}\!\!\!\!\inf\_{\alpha^{\prime}\in{\mathcal{A}}^{\rm ad}(\ell,\alpha)}{\rm F}^{\rm ad}\_{p}(\ell,\alpha^{\prime},\nu)\;\;\mbox{ for $0\leq\ell\leq L-1$, $\nu\in{\mathcal{M}}$ and $\alpha\in{\mathcal{A}}^{\rm ad}$,} |  |

where

|  |  |  |
| --- | --- | --- |
|  | 𝒜ad​(ℓ,α):={α′=(q′,N′)∈𝒜ad:(αl′)0≤l≤ℓ=(αl)0≤l≤ℓ​ and​C​(q′,N′)≤K}assignsuperscript𝒜adℓ𝛼conditional-setsuperscript𝛼′superscript𝑞′superscript𝑁′superscript𝒜adsubscriptsubscriptsuperscript𝛼′𝑙0𝑙ℓsubscriptsubscript𝛼𝑙0𝑙ℓ andCsuperscript𝑞′superscript𝑁′𝐾{\mathcal{A}}^{\rm ad}(\ell,\alpha):=\{\alpha^{\prime}=(q^{\prime},N^{\prime})\in{\mathcal{A}}^{\rm ad}:(\alpha^{\prime}\_{l})\_{0\leq l\leq\ell}=(\alpha\_{l})\_{0\leq l\leq\ell}\mbox{ and}\;{\rm C}(q^{\prime},N^{\prime})\leq K\} |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fpad​(ℓ,α′,ν)subscriptsuperscriptFad𝑝ℓsuperscript𝛼′𝜈\displaystyle{\rm F}^{\rm ad}\_{p}(\ell,\alpha^{\prime},\nu) | :=𝔼ν​[|1nw​∑i∈ℑL−1α′μ^Lα′,i−μ~i|p+𝟏{ℓ<L−1}​∑l=ℓ+1L−1fpad​(l,α′,θ~)|ℱℓα′].assignabsentsuperscript𝔼𝜈delimited-[]superscript1subscript𝑛𝑤subscript𝑖superscriptsubscriptℑ𝐿1superscript𝛼′superscriptsubscript^𝜇𝐿  superscript𝛼′𝑖superscript~𝜇𝑖𝑝conditionalsubscript1ℓ𝐿1superscriptsubscript𝑙ℓ1𝐿1subscriptsuperscript𝑓ad𝑝𝑙superscript𝛼′~𝜃subscriptsuperscriptℱsuperscript𝛼′ℓ\displaystyle:={\mathbb{E}}^{\nu}\left[\left|\frac{1}{n\_{w}}\sum\_{i\in{\mathfrak{I}}\_{L-1}^{\alpha^{\prime}}}\hat{\mu}\_{L}^{\alpha^{\prime},i}-\tilde{\mu}^{i}\right|^{p}+{{\mathbf{1}}\_{\{\ell<L-1\}}}\sum\_{l=\ell+1}^{L-1}f^{\rm ad}\_{p}(l,\alpha^{\prime},\tilde{\theta})\leavevmode\nobreak\ \Bigg{|}\leavevmode\nobreak\ {\mathcal{F}}^{\alpha^{\prime}}\_{\ell}\right]. |  |

It admits a dynamic programming principle that involves a Bayesian update of the prior law on θ~~𝜃\tilde{\theta} at each step of the algorithm, see e.g. [[10](#bib.bib10)].

Let us first observe that, from step ℓℓ\ell on, our bound only involves the components of θ~~𝜃\tilde{\theta} associated to the indexes in ℑℓαsubscriptsuperscriptℑ𝛼ℓ{\mathfrak{I}}^{\alpha}\_{\ell}. We therefore set

|  |  |  |
| --- | --- | --- |
|  | θ~ℓα=(μ~ℓα,Σ~ℓα):=𝒯ℑℓ−1αℑℓα​(θ~ℓ−1α),ℓ≥1, with ​θ~0α:=θ~formulae-sequencesubscriptsuperscript~𝜃𝛼ℓsubscriptsuperscript~𝜇𝛼ℓsubscriptsuperscript~Σ𝛼ℓassignsubscriptsuperscript𝒯subscriptsuperscriptℑ𝛼ℓsubscriptsuperscriptℑ𝛼ℓ1subscriptsuperscript~𝜃𝛼ℓ1formulae-sequenceℓ1assign with subscriptsuperscript~𝜃𝛼0~𝜃\tilde{\theta}^{\alpha}\_{\ell}=(\tilde{\mu}^{\alpha}\_{\ell},\tilde{\Sigma}^{\alpha}\_{\ell}):={\cal T}^{{\mathfrak{I}}^{\alpha}\_{\ell}}\_{{\mathfrak{I}}^{\alpha}\_{\ell-1}}(\tilde{\theta}^{\alpha}\_{\ell-1}),\;\ell\geq 1,\;\mbox{ with }\tilde{\theta}^{\alpha}\_{0}:=\tilde{\theta} |  |

where, for two subsets A′⊂A⊂[[1,ns]]superscript𝐴′𝐴delimited-[]1subscript𝑛𝑠A^{\prime}\subset A\subset[\![1,n\_{s}]\!] and (μ,Σ)=((μi)i∈A,(Σi​j)i,j∈A)𝜇Σsubscriptsuperscript𝜇𝑖𝑖𝐴subscriptsuperscriptΣ𝑖𝑗

𝑖𝑗
𝐴(\mu,\Sigma)=((\mu^{i})\_{i\in A},(\Sigma^{ij})\_{i,j\in A}), we define

|  |  |  |
| --- | --- | --- |
|  | 𝒯AA′​(μ,Σ)=((μi)i∈A′,(Σi​j)i,j∈A′).subscriptsuperscript𝒯superscript𝐴′𝐴𝜇Σsubscriptsuperscript𝜇𝑖𝑖superscript𝐴′subscriptsuperscriptΣ𝑖𝑗  𝑖𝑗 superscript𝐴′{\cal T}^{A^{\prime}}\_{A}(\mu,\Sigma)=((\mu^{i})\_{i\in A^{\prime}},(\Sigma^{ij})\_{i,j\in A^{\prime}}). |  |

This means that the update of the prior can be restricted to a reduced number of components of θ~~𝜃\tilde{\theta}. This explains why we will concentrate on minimizing this upper-bound rather than directly the left-hand side of ([24](#S3.E24 "In 3.2 A generic progressive learning algorithm ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios")), which would lead to a very high-dimensional optimal control problem, at each step ℓℓ\ell. This way, we expect to reduce very significantly the computation cost of the corresponding “optimal” strategy.

In order to make the updating rule explicit, we use the following assumption.

###### Assumption 3.

Given ν0∈ℳsubscript𝜈0ℳ\nu\_{0}\in{\mathcal{M}}, there exists a measure m𝑚m, such that, for all α∈𝒜ad𝛼superscript𝒜ad\alpha\in{\mathcal{A}}^{\rm ad} and 1≤ℓ≤L1ℓ𝐿{1}\leq\ell\leq L, the law of Iℓα:=(Pji,(i,j)∈ℑℓ−1α×[[Nℓ−1α+1,Nℓα]])assignsubscriptsuperscript𝐼𝛼ℓ

superscriptsubscript𝑃𝑗𝑖𝑖𝑗
subscriptsuperscriptℑ𝛼ℓ1delimited-[]subscriptsuperscript𝑁𝛼ℓ11subscriptsuperscript𝑁𝛼ℓI^{\alpha}\_{\ell}:=(P\_{j}^{i},(i,j)\in{\mathfrak{I}}^{\alpha}\_{{\ell-1}}\times[\![N^{\alpha}\_{\ell-1}+1,N^{\alpha}\_{\ell}]\!]) given ℱℓ−1α∨σ​(θ~)subscriptsuperscriptℱ𝛼ℓ1𝜎~𝜃{\mathcal{F}}^{\alpha}\_{\ell-1}\vee\sigma(\tilde{\theta}) admits ν0subscript𝜈0\nu\_{0}-a.s. the density
gℓα​(⋅,θ~ℓ−1α):=g​(⋅,ℑℓ−1α,Nℓ−1α,Nℓα,θ~ℓ−1α)assignsubscriptsuperscript𝑔𝛼ℓ⋅subscriptsuperscript~𝜃𝛼ℓ1𝑔⋅subscriptsuperscriptℑ𝛼ℓ1subscriptsuperscript𝑁𝛼ℓ1subscriptsuperscript𝑁𝛼ℓsubscriptsuperscript~𝜃𝛼ℓ1g^{\alpha}\_{\ell}(\cdot,\tilde{\theta}^{\alpha}\_{{\ell-1}}):=g(\cdot,{\mathfrak{I}}^{\alpha}\_{{\ell-1}},N^{\alpha}\_{\ell-1},N^{\alpha}\_{\ell},\tilde{\theta}^{\alpha}\_{{\ell-1}}) with respect to m𝑚m, in which g𝑔g is a bounded measurable map111111As for measurability, we identify ℑℓ−1αsubscriptsuperscriptℑ𝛼ℓ1{\mathfrak{I}}^{\alpha}\_{{\ell-1}} to the element of ℝnssuperscriptℝsubscript𝑛𝑠{\mathbb{R}}^{n\_{s}} with i𝑖i-th entry given by 𝟏{i∈ℑℓ−1α}subscript1𝑖subscriptsuperscriptℑ𝛼ℓ1{\mathbf{1}}\_{\{i\in{\mathfrak{I}}^{\alpha}\_{{\ell-1}}\}}., that is continuous in its first argument, uniformly in the other ones. Moreover, for all α∈𝒜ad𝛼superscript𝒜ad\alpha\in{\mathcal{A}}^{\rm ad} and ℓ≤Lℓ𝐿\ell\leq L, the law of θ~~𝜃\tilde{\theta} given ℱℓαsubscriptsuperscriptℱ𝛼ℓ{\mathcal{F}}^{\alpha}\_{\ell} belongs to ℳℳ{\mathcal{M}} ν0subscript𝜈0\nu\_{0}-a.s.

Under this assumption, we can compute the law νℓα,ℓ−1subscriptsuperscript𝜈

𝛼ℓ1ℓ{\nu^{\alpha,\ell-1}\_{\ell}} of θ~ℓ−1α=𝒯ℓ−1α​(θ~)subscriptsuperscript~𝜃𝛼ℓ1subscriptsuperscript𝒯𝛼ℓ1~𝜃\tilde{\theta}^{\alpha}\_{{\ell-1}}={{\cal T}^{\alpha}\_{\ell-1}(\tilde{\theta})} given ℱℓαsubscriptsuperscriptℱ𝛼ℓ{\mathcal{F}}^{\alpha}\_{\ell} in terms of its counterpart νℓ−1αsubscriptsuperscript𝜈𝛼ℓ1\nu^{\alpha}\_{\ell-1} given ℱℓ−1αsubscriptsuperscriptℱ𝛼ℓ1{\mathcal{F}}^{\alpha}\_{\ell-1},
in which
𝒯ℓ−1α:=𝒯ℑℓ−2αℑℓ−1α∘⋯∘𝒯ℑ0αℑ1α.assignsubscriptsuperscript𝒯𝛼ℓ1subscriptsuperscript𝒯subscriptsuperscriptℑ𝛼ℓ1subscriptsuperscriptℑ𝛼ℓ2⋯subscriptsuperscript𝒯subscriptsuperscriptℑ𝛼1subscriptsuperscriptℑ𝛼0{\cal T}^{\alpha}\_{\ell-1}:={\cal T}^{{\mathfrak{I}}^{\alpha}\_{\ell-1}}\_{{\mathfrak{I}}^{\alpha}\_{\ell-2}}\circ\cdots\circ{\cal T}^{{\mathfrak{I}}^{\alpha}\_{1}}\_{{\mathfrak{I}}^{\alpha}\_{0}}.
It is given by

|  |  |  |
| --- | --- | --- |
|  | νℓα,ℓ−1=𝒰12​(ℓ,α,νℓ−1α)subscriptsuperscript𝜈  𝛼ℓ1ℓsuperscript𝒰12ℓ𝛼subscriptsuperscript𝜈𝛼ℓ1{\nu^{\alpha,\ell-1}\_{\ell}}={\mathcal{U}}^{\frac{1}{2}}(\ell,\alpha,\nu^{\alpha}\_{\ell-1}) |  |

with ν0α=νsubscriptsuperscript𝜈𝛼0𝜈\nu^{\alpha}\_{0}=\nu and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒰12​(ℓ,α,νℓ−1α)​(A):=∫𝒟ℓ−1αgℓα​(Iℓα,θ)​𝟏{θ∈A}​νℓ−1α​(d​θ)∫𝒟ℓ−1αgℓα​(Iℓα,θ)​νℓ−1α​(d​θ)assignsuperscript𝒰12ℓ𝛼subscriptsuperscript𝜈𝛼ℓ1𝐴subscriptsubscriptsuperscript𝒟𝛼ℓ1subscriptsuperscript𝑔𝛼ℓsubscriptsuperscript𝐼𝛼ℓ𝜃subscript1𝜃𝐴subscriptsuperscript𝜈𝛼ℓ1𝑑𝜃subscriptsubscriptsuperscript𝒟𝛼ℓ1subscriptsuperscript𝑔𝛼ℓsubscriptsuperscript𝐼𝛼ℓ𝜃subscriptsuperscript𝜈𝛼ℓ1𝑑𝜃\displaystyle{\mathcal{U}}^{\frac{1}{2}}(\ell,\alpha,\nu^{\alpha}\_{\ell-1})(A):=\frac{\int\_{{\cal D}^{\alpha}\_{\ell-1}}g^{\alpha}\_{\ell}(I^{\alpha}\_{\ell},{\theta}){\mathbf{1}}\_{\{{\theta}\in A\}}{\nu^{\alpha}\_{\ell-1}}(d\theta)}{\int\_{{\cal D}^{\alpha}\_{\ell-1}}g^{\alpha}\_{\ell}(I^{\alpha}\_{\ell},{\theta})\nu^{\alpha}\_{\ell-1}(d\theta)} |  | (25) |

for a Borel set A𝐴A of
𝒟ℓ−1α:=𝒯ℓ−1α​(ℝns×𝕊ns).assignsubscriptsuperscript𝒟𝛼ℓ1subscriptsuperscript𝒯𝛼ℓ1superscriptℝsubscript𝑛𝑠superscript𝕊subscript𝑛𝑠{\cal D}^{\alpha}\_{\ell-1}:={\cal T}^{\alpha}\_{\ell-1}({\mathbb{R}}^{n\_{s}}\times{\mathbb{S}}^{n\_{s}}).
From this, one can deduce the law νℓαsubscriptsuperscript𝜈𝛼ℓ{\nu^{\alpha}\_{\ell}} of θ~ℓα=𝒯ℓα​(θ~)subscriptsuperscript~𝜃𝛼ℓsubscriptsuperscript𝒯𝛼ℓ~𝜃\tilde{\theta}^{\alpha}\_{{\ell}}={{\cal T}^{\alpha}\_{\ell}(\tilde{\theta})} given ℱℓαsubscriptsuperscriptℱ𝛼ℓ{\mathcal{F}}^{\alpha}\_{\ell}, in the form

|  |  |  |
| --- | --- | --- |
|  | νℓα=𝒰​(ℓ,α,νℓ−1α),subscriptsuperscript𝜈𝛼ℓ𝒰ℓ𝛼subscriptsuperscript𝜈𝛼ℓ1{\nu^{\alpha}\_{\ell}}={\mathcal{U}}(\ell,\alpha,\nu^{\alpha}\_{\ell-1}), |  |

by simply integrating on the components corresponding to indexes that are not in ℑℓαsubscriptsuperscriptℑ𝛼ℓ{\mathfrak{I}}^{\alpha}\_{\ell} (meaning that 𝒰𝒰{\mathcal{U}} is explicit in terms of 𝒰12superscript𝒰12{\mathcal{U}}^{\frac{1}{2}}).

We are now in position to state our dynamic programming principle, see e.g. [[10](#bib.bib10)]. Again, note that the law of fpad​(ℓ+1,α′,θ~)subscriptsuperscript𝑓ad𝑝ℓ1superscript𝛼′~𝜃f^{\rm ad}\_{p}(\ell{+1},\alpha^{\prime},\tilde{\theta}) given ℱℓα′subscriptsuperscriptℱsuperscript𝛼′ℓ{\mathcal{F}}^{\alpha^{\prime}}\_{\ell} depends on θ~~𝜃\tilde{\theta} only through θ~ℓα′subscriptsuperscript~𝜃superscript𝛼′ℓ\tilde{\theta}^{\alpha^{\prime}}\_{\ell}. For ease of notations, we identify all measures to an element of ℳℳ{\mathcal{M}} (even if it supported by a space smaller than ℝns×𝕊nssuperscriptℝsubscript𝑛𝑠superscript𝕊subscript𝑛𝑠{\mathbb{R}}^{n\_{s}}\times{\mathbb{S}}^{n\_{s}}).

###### Proposition 3.5.

Let Assumption [3](#Thmassumption3 "Assumption 3. ‣ 3.2 A generic progressive learning algorithm ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios") hold. Then, for all α∈𝒜ad𝛼superscript𝒜ad\alpha\in{\mathcal{A}}^{\rm ad}, 0≤ℓ≤L−20ℓ𝐿20\leq\ell\leq L-2 and ν∈ℳ𝜈ℳ\nu\in{\mathcal{M}},

|  |  |  |
| --- | --- | --- |
|  | F^pad​(ℓ,α,ν)=ess​infα′∈𝒜ad​(ℓ,α)𝔼ν​[F^pad​(ℓ+1,α′,𝒰​(ℓ+1,α′,ν))+fpad​(ℓ+1,α′,θ~)|ℱℓα].subscriptsuperscript^Fad𝑝ℓ𝛼𝜈esssubscriptinfimumsuperscript𝛼′superscript𝒜adℓ𝛼superscript𝔼𝜈delimited-[]subscriptsuperscript^Fad𝑝ℓ1superscript𝛼′𝒰ℓ1superscript𝛼′𝜈conditionalsubscriptsuperscript𝑓ad𝑝ℓ1superscript𝛼′~𝜃subscriptsuperscriptℱ𝛼ℓ\displaystyle\hat{\rm F}^{\rm ad}\_{p}(\ell,\alpha,\nu)={\rm ess}\!\!\!\!\inf\_{\alpha^{\prime}\in{\mathcal{A}}^{\rm ad}(\ell,\alpha)}{\mathbb{E}}^{\nu}[\hat{\rm F}^{\rm ad}\_{p}(\ell+1,\alpha^{\prime},{\mathcal{U}}(\ell+1,\alpha^{\prime},\nu))+f^{\rm ad}\_{p}(\ell+1,\alpha^{\prime},\tilde{\theta})|{\mathcal{F}}^{\alpha}\_{\ell}]. |  |

In principle, this dynamic programming algorithm allows one to estimate numerically the optimal policy α⋆superscript𝛼⋆\alpha^{\star} in a feed-back form, off-line. Importantly, solving this problem given an initial prior ν0subscript𝜈0\nu\_{0} is very different from first estimating the parameter θ~~𝜃\tilde{\theta} and then solving the control problem as if θ~~𝜃\tilde{\theta} was given. In the first case, we take into account the risk due to the uncertainly on the true value of θ~~𝜃\tilde{\theta}, not in the second one.

###### Remark 3.6.

In practice, the algorithm requires estimating and manipulating the law of a high-dimensional parameter, at least at the first steps. But the above can be modified by changing the filtration (ℱℓα)ℓ≤Lsubscriptsubscriptsuperscriptℱ𝛼ℓℓ𝐿({\mathcal{F}}^{\alpha}\_{\ell})\_{\ell\leq L} in (ℱ¯ℓα)ℓ≤Lsubscriptsubscriptsuperscript¯ℱ𝛼ℓℓ𝐿(\bar{\mathcal{F}}^{\alpha}\_{\ell})\_{\ell\leq L} with ℱ¯ℓαsubscriptsuperscript¯ℱ𝛼ℓ\bar{\mathcal{F}}^{\alpha}\_{\ell} == σ​(𝟏ℓ≥τα​Pji,(i,j)∈ℑℓα×[[1,Nℓα]])𝜎

subscript1ℓsuperscript𝜏𝛼superscriptsubscript𝑃𝑗𝑖𝑖𝑗
subscriptsuperscriptℑ𝛼ℓdelimited-[]1subscriptsuperscript𝑁𝛼ℓ\sigma({\mathbf{1}}\_{\ell\geq\tau^{\alpha}}P\_{j}^{i},(i,j)\in{\mathfrak{I}}^{\alpha}\_{\ell}\times[\![1,N^{\alpha}\_{\ell}]\!]) with τα:=inf{l≤L:qlα≤ρ}assignsuperscript𝜏𝛼infimumconditional-set𝑙𝐿subscriptsuperscript𝑞𝛼𝑙𝜌\tau^{\alpha}:=\inf\{l\leq L:q^{\alpha}\_{l}\leq\rho\} for some ρ>0𝜌0\rho>0. In this case, no additional information is considered up to step ταsuperscript𝜏𝛼\tau^{\alpha}, the update of the prior only takes place from step ταsuperscript𝜏𝛼\tau^{\alpha} on and it only concerns θ~τααsubscriptsuperscript~𝜃𝛼superscript𝜏𝛼\tilde{\theta}^{\alpha}\_{\tau^{\alpha}} whose dimension is controlled by ρ𝜌\rho. As for the first steps of the algorithm, namely before τρsuperscript𝜏𝜌\tau^{\rho}, one can replace fpadsubscriptsuperscript𝑓ad𝑝f^{\rm ad}\_{p} by a robust version in the spirit of Section [2.4](#S2.SS4 "2.4 Optimal a-priori allocation by deterministic dynamic programming based on fixed a-priori bounds ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios").

###### Remark 3.7.

The algorithm also requires knowing the conditional density gℓαsubscriptsuperscript𝑔𝛼ℓg^{\alpha}\_{\ell}. Although, P|sP\_{|{\rm s}} can be simulated, its conditional density is not known in general. However, one can use a proxy and/or again modify the flow of information to reduce to a more explicit situation. Let us consider the situation in which (ℱℓα)ℓ≤Lsubscriptsubscriptsuperscriptℱ𝛼ℓℓ𝐿({\mathcal{F}}^{\alpha}\_{\ell})\_{\ell\leq L} is replaced by (ℱ¯ℓα)ℓ≤Lsubscriptsubscriptsuperscript¯ℱ𝛼ℓℓ𝐿(\bar{\mathcal{F}}^{\alpha}\_{\ell})\_{\ell\leq L} with ℱ¯ℓαsubscriptsuperscript¯ℱ𝛼ℓ\bar{\mathcal{F}}^{\alpha}\_{\ell} == ℱ¯ℓ−1α∨σ​(δ​μ^ℓα,i,i∈ℑℓα)subscriptsuperscript¯ℱ𝛼ℓ1𝜎

𝛿subscriptsuperscript^𝜇

𝛼𝑖ℓ𝑖
subscriptsuperscriptℑ𝛼ℓ\bar{\mathcal{F}}^{\alpha}\_{\ell-1}\vee\sigma(\delta\hat{\mu}^{{\alpha},i}\_{\ell},i\in{\mathfrak{I}}^{\alpha}\_{\ell}) and ℱ¯0αsubscriptsuperscript¯ℱ𝛼0\bar{\mathcal{F}}^{\alpha}\_{0} is trivial. Then, conditionally to ℱ¯ℓ−1α∨σ​(θ~ℓ−1α)subscriptsuperscript¯ℱ𝛼ℓ1𝜎subscriptsuperscript~𝜃𝛼ℓ1\bar{\mathcal{F}}^{\alpha}\_{\ell-1}\vee\sigma(\tilde{\theta}^{\alpha}\_{\ell-1}), δ​Nℓα​(Σ~ℓα)−1​(δ​μ^ℓα−μ~ℓα)𝛿subscriptsuperscript𝑁𝛼ℓsuperscriptsubscriptsuperscript~Σ𝛼ℓ1𝛿subscriptsuperscript^𝜇𝛼ℓsubscriptsuperscript~𝜇𝛼ℓ\sqrt{\delta N^{\alpha}\_{\ell}}(\tilde{\Sigma}^{\alpha}\_{\ell})^{-1}\left(\delta\hat{\mu}^{\alpha}\_{\ell}-\tilde{\mu}^{\alpha}\_{\ell}\right) is asymptotically Gaussian as δ​Nℓα𝛿subscriptsuperscript𝑁𝛼ℓ\delta N^{\alpha}\_{\ell} increases to infinity. In practice, we can do as if δ​Nℓα​(Σ~ℓα)−1​(δ​μ^ℓα−μ~ℓα)𝛿subscriptsuperscript𝑁𝛼ℓsuperscriptsubscriptsuperscript~Σ𝛼ℓ1𝛿subscriptsuperscript^𝜇𝛼ℓsubscriptsuperscript~𝜇𝛼ℓ\sqrt{\delta N^{\alpha}\_{\ell}}(\tilde{\Sigma}^{\alpha}\_{\ell})^{-1}\left(\delta\hat{\mu}^{\alpha}\_{\ell}-\tilde{\mu}^{\alpha}\_{\ell}\right) was actually following a standard Gaussian distribution, conditionally to θ~ℓαsubscriptsuperscript~𝜃𝛼ℓ\tilde{\theta}^{\alpha}\_{\ell} and ℱℓ−1αsubscriptsuperscriptℱ𝛼ℓ1{\mathcal{F}}^{\alpha}\_{\ell-1}, which provides an explicit formula for the conditional density g¯ℓαsubscriptsuperscript¯𝑔𝛼ℓ\bar{g}^{\alpha}\_{\ell} of δ​μ^ℓα𝛿subscriptsuperscript^𝜇𝛼ℓ\delta\hat{\mu}^{\alpha}\_{\ell} given θ~ℓ−1αsubscriptsuperscript~𝜃𝛼ℓ1\tilde{\theta}^{\alpha}\_{\ell-1} and ℱℓ−1αsubscriptsuperscriptℱ𝛼ℓ1{\mathcal{F}}^{\alpha}\_{\ell-1}, to be plugged into ([25](#S3.E25 "In 3.2 A generic progressive learning algorithm ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios")). Namely, the updating procedure takes the form

|  |  |  |
| --- | --- | --- |
|  | νℓα=𝒰ˇ​(ℓ,α,νℓ−1α)subscriptsuperscript𝜈𝛼ℓˇ𝒰ℓ𝛼subscriptsuperscript𝜈𝛼ℓ1\nu^{\alpha}\_{\ell}=\check{\mathcal{U}}(\ell,\alpha,\nu^{\alpha}\_{\ell-1}) |  |

where 𝒰ˇˇ𝒰\check{\mathcal{U}} is explicit.

Then, if the initial prior ν0subscript𝜈0\nu\_{0} is such that (μ~,Σ~)~𝜇~Σ(\tilde{\mu},\tilde{\Sigma}) is a Normal-inverse-Wishart distribution, all the posterior distribution νℓαsubscriptsuperscript𝜈𝛼ℓ\nu^{\alpha}\_{\ell}, ℓ≤Lℓ𝐿\ell\leq L, are such that (μ~,Σ~)~𝜇~Σ(\tilde{\mu},\tilde{\Sigma}) remains in the class of Normal-inverse-Wishart distributions with parameters that can computed explicitly from our simulations. Namely, if, given ℱ¯ℓαsubscriptsuperscript¯ℱ𝛼ℓ\bar{\mathcal{F}}^{\alpha}\_{\ell}, Σ~~Σ\tilde{\Sigma} has the distribution121212Hereafter 𝒲𝚒−1​(Σ)subscriptsuperscript𝒲1𝚒Σ{\cal W}^{-1}\_{{\mathtt{i}}}(\Sigma) stands for the Inverse-Wishart distribution with degree of freedom 𝚒𝚒{\mathtt{i}} and scale matrix ΣΣ\Sigma, while 𝒩​(𝚖,Σ)𝒩𝚖Σ{\cal N}({\mathtt{m}},\Sigma) is the Gaussian distribution with mean 𝚖𝚖{\mathtt{m}} and covariance matrix ΣΣ\Sigma. 𝒲𝚒ℓα−1​(Σℓα)superscriptsubscript𝒲subscriptsuperscript𝚒𝛼ℓ1subscriptsuperscriptΣ𝛼ℓ{\cal W}\_{{\mathtt{i}}^{\alpha}\_{\ell}}^{-1}(\Sigma^{\alpha}\_{\ell}) and μ~~𝜇\tilde{\mu} has the distribution 𝒩​(𝚖ℓα,Σ~/𝚔ℓα)𝒩subscriptsuperscript𝚖𝛼ℓ~Σsubscriptsuperscript𝚔𝛼ℓ{\cal N}({\mathtt{m}}^{\alpha}\_{\ell},\tilde{\Sigma}/{\mathtt{k}}^{\alpha}\_{\ell}) given Σ~~Σ\tilde{\Sigma}, then the coefficients corresponding to the law given ℱ¯ℓ+1αsubscriptsuperscript¯ℱ𝛼ℓ1\bar{\mathcal{F}}^{\alpha}\_{\ell+1} are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | {𝚒ℓ+1α=𝚒ℓα+δ​Nℓ+1α,𝚔ℓ+1α=𝚔ℓα+δ​Nℓ+1α,𝚖ℓ+1α=1κℓα+δ​Nℓ+1α​[κℓα​𝒯ℑℓαℑℓ+1α​(𝚖ℓα)+δ​Nℓ+1α​δ​μ^ℓ+1α]Σℓ+1α=𝒯ℑℓαℑℓ+1α​(Σℓα)+∑j=Nℓα+1Nℓ+1α(𝒯ℓ+1α​(Pj)−δ​μ^ℓ+1α)​(𝒯ℓ+1α​(Pj)−δ​μ^ℓ+1α)⊤+κℓα​δ​Nℓ+1ακℓα+δ​Nℓ+1α​(𝒯ℑℓαℑℓ+1α​(𝚖ℓα)−δ​μ^ℓ+1α)​(𝒯ℑℓαℑℓ+1α​(𝚖ℓα)−δ​μ^ℓ+1α)⊤,casessubscriptsuperscript𝚒𝛼ℓ1absentformulae-sequence  subscriptsuperscript𝚒𝛼ℓ𝛿subscriptsuperscript𝑁𝛼ℓ1subscriptsuperscript𝚔𝛼ℓ1 subscriptsuperscript𝚔𝛼ℓ𝛿subscriptsuperscript𝑁𝛼ℓ1subscriptsuperscript𝚖𝛼ℓ11subscriptsuperscript𝜅𝛼ℓ𝛿subscriptsuperscript𝑁𝛼ℓ1delimited-[]subscriptsuperscript𝜅𝛼ℓsubscriptsuperscript𝒯subscriptsuperscriptℑ𝛼ℓ1subscriptsuperscriptℑ𝛼ℓsubscriptsuperscript𝚖𝛼ℓ𝛿subscriptsuperscript𝑁𝛼ℓ1𝛿subscriptsuperscript^𝜇𝛼ℓ1subscriptsuperscriptΣ𝛼ℓ1absentsubscriptsuperscript𝒯subscriptsuperscriptℑ𝛼ℓ1subscriptsuperscriptℑ𝛼ℓsubscriptsuperscriptΣ𝛼ℓsuperscriptsubscript𝑗subscriptsuperscript𝑁𝛼ℓ1subscriptsuperscript𝑁𝛼ℓ1subscriptsuperscript𝒯𝛼ℓ1subscript𝑃𝑗𝛿subscriptsuperscript^𝜇𝛼ℓ1superscriptsubscriptsuperscript𝒯𝛼ℓ1subscript𝑃𝑗𝛿subscriptsuperscript^𝜇𝛼ℓ1topmissing-subexpressionsubscriptsuperscript𝜅𝛼ℓ𝛿subscriptsuperscript𝑁𝛼ℓ1subscriptsuperscript𝜅𝛼ℓ𝛿subscriptsuperscript𝑁𝛼ℓ1subscriptsuperscript𝒯subscriptsuperscriptℑ𝛼ℓ1subscriptsuperscriptℑ𝛼ℓsubscriptsuperscript𝚖𝛼ℓ𝛿subscriptsuperscript^𝜇𝛼ℓ1superscriptsubscriptsuperscript𝒯subscriptsuperscriptℑ𝛼ℓ1subscriptsuperscriptℑ𝛼ℓsubscriptsuperscript𝚖𝛼ℓ𝛿subscriptsuperscript^𝜇𝛼ℓ1top\displaystyle\left\{\begin{array}[]{rl}{\mathtt{i}}^{\alpha}\_{\ell+1}=&{\mathtt{i}}^{\alpha}\_{\ell}+\delta N^{\alpha}\_{\ell+1},\;{\mathtt{k}}^{\alpha}\_{\ell+1}={\mathtt{k}}^{\alpha}\_{\ell}+\delta N^{\alpha}\_{\ell+1},\;{\mathtt{m}}^{\alpha}\_{\ell+1}=\frac{1}{\kappa^{\alpha}\_{\ell}+\delta N^{\alpha}\_{\ell+1}}\left[\kappa^{\alpha}\_{\ell}{\cal T}^{{\mathfrak{I}}^{\alpha}\_{\ell+1}}\_{{\mathfrak{I}}^{\alpha}\_{\ell}}({\mathtt{m}}^{\alpha}\_{\ell})+\delta N^{\alpha}\_{\ell+1}\delta\hat{\mu}^{\alpha}\_{\ell+1}\right]\\ \Sigma^{\alpha}\_{\ell+1}=&{\cal T}^{{\mathfrak{I}}^{\alpha}\_{\ell+1}}\_{{\mathfrak{I}}^{\alpha}\_{\ell}}(\Sigma^{\alpha}\_{\ell})+\sum\_{j=N^{\alpha}\_{\ell}+1}^{N^{\alpha}\_{\ell+1}}({\cal T}^{\alpha}\_{\ell+1}(P\_{j})-\delta\hat{\mu}^{\alpha}\_{\ell+1})({\cal T}^{\alpha}\_{\ell+1}(P\_{j})-\delta\hat{\mu}^{\alpha}\_{\ell+1})^{\top}\\ &+\frac{\kappa^{\alpha}\_{\ell}\delta N^{\alpha}\_{\ell+1}}{\kappa^{\alpha}\_{\ell}+\delta N^{\alpha}\_{\ell+1}}({\cal T}^{{\mathfrak{I}}^{\alpha}\_{\ell+1}}\_{{\mathfrak{I}}^{\alpha}\_{\ell}}({\mathtt{m}}^{\alpha}\_{\ell})-\delta\hat{\mu}^{\alpha}\_{\ell+1})({\cal T}^{{\mathfrak{I}}^{\alpha}\_{\ell+1}}\_{{\mathfrak{I}}^{\alpha}\_{\ell}}({\mathtt{m}}^{\alpha}\_{\ell})-\delta\hat{\mu}^{\alpha}\_{\ell+1})^{\top},\end{array}\right. |  | (29) |

see e.g. [[18](#bib.bib18), Section 9]. Later on, we shall write the corresponding law as 𝒩​𝒲−1​(𝚙ℓ+1α)𝒩superscript𝒲1subscriptsuperscript𝚙𝛼ℓ1{\cal NW}^{-1}(\mathtt{p}^{\alpha}\_{\ell+1}) with

|  |  |  |
| --- | --- | --- |
|  | 𝚙ℓ+1α:=(𝚖ℓ+1α,𝚔ℓ+1α,𝚒ℓ+1α,Σℓ+1α).assignsubscriptsuperscript𝚙𝛼ℓ1subscriptsuperscript𝚖𝛼ℓ1subscriptsuperscript𝚔𝛼ℓ1subscriptsuperscript𝚒𝛼ℓ1subscriptsuperscriptΣ𝛼ℓ1\mathtt{p}^{\alpha}\_{\ell+1}:=({\mathtt{m}}^{\alpha}\_{\ell+1},{\mathtt{k}}^{\alpha}\_{\ell+1},{\mathtt{i}}^{\alpha}\_{\ell+1},\Sigma^{\alpha}\_{\ell+1}). |  |

### 3.3 Example of numerical implementation using neural networks

In this section, we aim at solving the version of the dynamic programming equation of Proposition [3.5](#S3.Thmtheorem5 "Proposition 3.5. ‣ 3.2 A generic progressive learning algorithm ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), using an initial Normal-inverse-Wishart prior and the approximate updating procedure suggested in Remark [3.7](#S3.Thmtheorem7 "Remark 3.7. ‣ 3.2 A generic progressive learning algorithm ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios"):

|  |  |  |
| --- | --- | --- |
|  | Fˇpad​(ℓ,α,ν)=ess​infα′∈𝒜ad​(ℓ,α)𝔼ν​[Fˇpad​(ℓ+1,α′,𝒰ˇ​(ℓ+1,α′,ν))+fpad​(ℓ+1,α′,θ~)|ℱ¯ℓα],subscriptsuperscriptˇFad𝑝ℓ𝛼𝜈esssubscriptinfimumsuperscript𝛼′superscript𝒜adℓ𝛼superscript𝔼𝜈delimited-[]subscriptsuperscriptˇFad𝑝ℓ1superscript𝛼′ˇ𝒰ℓ1superscript𝛼′𝜈conditionalsubscriptsuperscript𝑓ad𝑝ℓ1superscript𝛼′~𝜃subscriptsuperscript¯ℱ𝛼ℓ\displaystyle\check{\rm F}^{\rm ad}\_{p}(\ell,\alpha,\nu)={\rm ess}\!\!\!\!\inf\_{\alpha^{\prime}\in{\mathcal{A}}^{\rm ad}(\ell,\alpha)}{\mathbb{E}}^{\nu}[\check{\rm F}^{\rm ad}\_{p}(\ell+1,\alpha^{\prime},\check{\mathcal{U}}(\ell+1,\alpha^{\prime},\nu))+f^{\rm ad}\_{p}(\ell+1,\alpha^{\prime},\tilde{\theta})|\bar{\mathcal{F}}^{\alpha}\_{\ell}], |  |

with 𝒰ˇˇ𝒰\check{\mathcal{U}} as in Remark [3.7](#S3.Thmtheorem7 "Remark 3.7. ‣ 3.2 A generic progressive learning algorithm ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios") and

|  |  |  |
| --- | --- | --- |
|  | Fˇpad​(L−1,α,ν):=𝔼ν​[|1nw​∑i∈ℑL−1α′μ^Lα′,i−μ~i|p|ℱ¯L−1α].assignsubscriptsuperscriptˇFad𝑝𝐿1𝛼𝜈superscript𝔼𝜈delimited-[]conditionalsuperscript1subscript𝑛𝑤subscript𝑖superscriptsubscriptℑ𝐿1superscript𝛼′superscriptsubscript^𝜇𝐿  superscript𝛼′𝑖superscript~𝜇𝑖𝑝subscriptsuperscript¯ℱ𝛼𝐿1\check{\rm F}^{\rm ad}\_{p}(L-1,\alpha,\nu):={\mathbb{E}}^{\nu}\left[\left|\frac{1}{n\_{w}}\sum\_{i\in{\mathfrak{I}}\_{L-1}^{\alpha^{\prime}}}\hat{\mu}\_{L}^{\alpha^{\prime},i}-\tilde{\mu}^{i}\right|^{p}\leavevmode\nobreak\ \Bigg{|}\leavevmode\nobreak\ \bar{\mathcal{F}}^{\alpha}\_{L-1}\right]. |  |

It would be tempting to use a standard grid-based approximation. However, to turn this problem in a Markovian one, one needs to let the value function at step ℓℓ\ell depend on qℓαsubscriptsuperscript𝑞𝛼ℓq^{\alpha}\_{\ell}, Nℓαsubscriptsuperscript𝑁𝛼ℓN^{\alpha}\_{\ell}, Cℓαsubscriptsuperscript𝐶𝛼ℓC^{\alpha}\_{\ell}, μ^ℓαsubscriptsuperscript^𝜇𝛼ℓ\hat{\mu}^{\alpha}\_{\ell} and 𝚙ℓαsubscriptsuperscript𝚙𝛼ℓ\mathtt{p}^{\alpha}\_{\ell}, where Cℓαsubscriptsuperscript𝐶𝛼ℓC^{\alpha}\_{\ell} is the running cost of strategy α𝛼\alpha up to level ℓℓ\ell, defined for ℓ≠0ℓ0\ell\neq 0 by Cℓα=∑l=0ℓ−1qlα​δ​Nl+1αsubscriptsuperscript𝐶𝛼ℓsuperscriptsubscript𝑙0ℓ1subscriptsuperscript𝑞𝛼𝑙𝛿subscriptsuperscript𝑁𝛼𝑙1C^{\alpha}\_{\ell}=\sum\_{l=0}^{\ell-1}q^{\alpha}\_{l}\delta N^{\alpha}\_{l+1} and C0α=0subscriptsuperscript𝐶𝛼00C^{\alpha}\_{0}=0. The dimension is then 1+1+1+qℓα+(1+qℓα+1+(qℓα)2)111subscriptsuperscript𝑞𝛼ℓ1subscriptsuperscript𝑞𝛼ℓ1superscriptsubscriptsuperscript𝑞𝛼ℓ21+1+1+q^{\alpha}\_{\ell}+(1+q^{\alpha}\_{\ell}+1+(q^{\alpha}\_{\ell})^{2}). Even for qℓα=20subscriptsuperscript𝑞𝛼ℓ20q^{\alpha}\_{\ell}=20, the corresponding space is already much too big to construct a reasonable grid on it. We therefore suggest using a neural network approximation.
Let us consider a family of bounded continuous functions {ϕx,x∈X}

subscriptitalic-ϕxx
X\{\phi\_{{\rm x}},{\rm x}\in{\rm X}\}, XX{\rm X} being a compact subset of ℝdXsuperscriptℝsubscript𝑑X{\mathbb{R}}^{d\_{{\rm X}}} for some dX≥1subscript𝑑X1d\_{{\rm X}}\geq 1, such that, for all q,δ​q≤ns

𝑞𝛿𝑞
subscript𝑛𝑠q,\delta q\leq n\_{s} and N,δ​N≥1

𝑁𝛿𝑁
1N,\delta N\geq 1,

|  |  |  |
| --- | --- | --- |
|  | ϕ⋅​(δ​q,δ​N,q,N,C,⋅):(x,μ,𝚙)∈X×ℝq×ℝ3+q+q2↦ϕx​(δ​q,δ​N,q,N,C,μ,𝚙)∈ℝ​ is continuous.:subscriptitalic-ϕ⋅𝛿𝑞𝛿𝑁𝑞𝑁𝐶⋅x𝜇𝚙Xsuperscriptℝ𝑞superscriptℝ3𝑞superscript𝑞2maps-tosubscriptitalic-ϕx𝛿𝑞𝛿𝑁𝑞𝑁𝐶𝜇𝚙ℝ is continuous.\phi\_{\cdot}(\delta q,\delta N,q,N,C,\cdot):({\rm x},\mu,\mathtt{p})\in{\rm X}\times{\mathbb{R}}^{q}\times{\mathbb{R}}^{3+q+q^{2}}\mapsto\phi\_{{\rm x}}(\delta q,\delta N,q,N,C,\mu,\mathtt{p})\in{\mathbb{R}}\;\mbox{ is continuous.} |  |

We then fix a family {αk}k≤k¯subscriptsuperscript𝛼𝑘𝑘¯𝑘\{\alpha^{k}\}\_{k\leq\bar{k}} of deterministic paths of 𝒜​(0)𝒜0{\mathcal{A}}(0) and simulate independent copies {θ~j}j≤j¯subscriptsuperscript~𝜃𝑗𝑗¯𝑗\{\tilde{\theta}^{j}\}\_{j\leq\bar{j}} of θ~~𝜃\tilde{\theta} according to ν0subscript𝜈0\nu\_{0}, a Normal-inverse-Wishart distribution 𝒩​𝒲−1​(𝚙0)𝒩superscript𝒲1subscript𝚙0{\cal NW}^{-1}(\mathtt{p}\_{0}). For each j𝑗j, we consider an i.i.d. sequence (Pj′j,1,…,Pj′j,ns)j′≥1subscriptsuperscriptsubscript𝑃superscript𝑗′

𝑗1…superscriptsubscript𝑃superscript𝑗′

𝑗subscript𝑛𝑠superscript𝑗′1(P\_{j^{\prime}}^{j,1},\ldots,P\_{j^{\prime}}^{j,n\_{s}})\_{j^{\prime}\geq 1} in the law 𝒩​(μ~j,Σ~j)𝒩superscript~𝜇𝑗superscript~Σ𝑗{\mathcal{N}}(\tilde{\mu}^{j},\tilde{\Sigma}^{j}) with θ~j=:(μ~j,Σ~j)\tilde{\theta}^{j}=:(\tilde{\mu}^{j},\tilde{\Sigma}^{j}). We take these sequences independent and independent of θ~~𝜃\tilde{\theta}.
For each k𝑘k and j𝑗j, we denote by (μ^ℓk,j)ℓ≤Lsubscriptsubscriptsuperscript^𝜇

𝑘𝑗ℓℓ𝐿(\hat{\mu}^{k,j}\_{\ell})\_{\ell\leq L}, (𝚙~ℓk,j)ℓ≤Lsubscriptsubscriptsuperscript~𝚙

𝑘𝑗ℓℓ𝐿(\tilde{\mathtt{p}}^{k,j}\_{\ell})\_{\ell\leq L} and (ℑℓk,j)ℓ≤Lsubscriptsuperscriptsubscriptℑℓ

𝑘𝑗ℓ𝐿({\mathfrak{I}}\_{\ell}^{k,j})\_{\ell\leq L} the paths (μ^ℓαk)ℓ≤Lsubscriptsubscriptsuperscript^𝜇superscript𝛼𝑘ℓℓ𝐿(\hat{\mu}^{\alpha^{k}}\_{\ell})\_{\ell\leq L}, (𝚙ℓαk)ℓ≤Lsubscriptsubscriptsuperscript𝚙superscript𝛼𝑘ℓℓ𝐿(\mathtt{p}^{\alpha^{k}}\_{\ell})\_{\ell\leq L} and (ℑℓαk)ℓ≤Lsubscriptsuperscriptsubscriptℑℓsuperscript𝛼𝑘ℓ𝐿({\mathfrak{I}}\_{\ell}^{\alpha^{k}})\_{\ell\leq L} associated to the j𝑗j-th sequence (Pj′j,1,…,Pj′j,ns)j′≥1subscriptsuperscriptsubscript𝑃superscript𝑗′

𝑗1…superscriptsubscript𝑃superscript𝑗′

𝑗subscript𝑛𝑠superscript𝑗′1(P\_{j^{\prime}}^{j,1},\ldots,P\_{j^{\prime}}^{j,n\_{s}})\_{j^{\prime}\geq 1} and the control αksuperscript𝛼𝑘\alpha^{k}. Similarly, we write fpad,k,j​(ℓ,⋅)superscriptsubscript𝑓𝑝

ad𝑘𝑗ℓ⋅f\_{p}^{{\rm ad},k,j}(\ell,\cdot) to denote the function fpad​(ℓ,⋅)superscriptsubscript𝑓𝑝adℓ⋅f\_{p}^{\rm ad}(\ell,\cdot) defined as in ([23](#S3.E23 "In Corollary 3.4. ‣ 3.1 Error bounds and convergence for predictable strategies ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios")) but in terms of ℑℓ−1k,jsuperscriptsubscriptℑℓ1

𝑘𝑗{\mathfrak{I}}\_{\ell-1}^{k,j} in place of ℑℓ−1αsuperscriptsubscriptℑℓ1𝛼{\mathfrak{I}}\_{\ell-1}^{\alpha}.
Given an integer r≥1𝑟1r\geq 1, we first compute xˇL−1subscriptˇx𝐿1\check{\rm x}\_{L-1} as the argmin over x∈XxX{\rm x}\in{\rm X} of

|  |  |  |
| --- | --- | --- |
|  | ∑k=1k¯∑j=1j¯|𝔼L−1νL−1k,j​[|1nw​∑i∈ℑL−1k,j(μ^Lk,j)i−μ~i|p]−ϕx​(0,δ​NLαk,qL−1αk,NL−1αk,CL−1αk,μ^L−1k,j,𝚙L−1k,j)|rsuperscriptsubscript𝑘1¯𝑘superscriptsubscript𝑗1¯𝑗superscriptsubscriptsuperscript𝔼subscriptsuperscript𝜈  𝑘𝑗𝐿1𝐿1delimited-[]superscript1subscript𝑛𝑤subscript𝑖superscriptsubscriptℑ𝐿1  𝑘𝑗superscriptsuperscriptsubscript^𝜇𝐿  𝑘𝑗𝑖superscript~𝜇𝑖𝑝subscriptitalic-ϕx0𝛿subscriptsuperscript𝑁superscript𝛼𝑘𝐿subscriptsuperscript𝑞superscript𝛼𝑘𝐿1subscriptsuperscript𝑁superscript𝛼𝑘𝐿1subscriptsuperscript𝐶superscript𝛼𝑘𝐿1subscriptsuperscript^𝜇  𝑘𝑗𝐿1subscriptsuperscript𝚙  𝑘𝑗𝐿1𝑟\sum\_{k=1}^{\bar{k}}\sum\_{j=1}^{\bar{j}}\left|{\mathbb{E}}^{\nu^{k,j}\_{L-1}}\_{L-1}\left[\left|\frac{1}{n\_{w}}\sum\_{i\in{\mathfrak{I}}\_{L-1}^{k,j}}(\hat{\mu}\_{L}^{{k},j})^{i}-\tilde{\mu}^{i}\right|^{p}\right]-\phi\_{{\rm x}}(0,{\delta N^{\alpha^{k}}\_{L}},q^{\alpha^{k}}\_{L-1},N^{\alpha^{k}}\_{L-1},C^{\alpha^{k}}\_{L-1},\hat{\mu}^{k,j}\_{L-1},\mathtt{p}^{k,j}\_{L-1})\right|^{r} |  |

in which 𝔼L−1νL−1k,jsubscriptsuperscript𝔼subscriptsuperscript𝜈

𝑘𝑗𝐿1𝐿1{\mathbb{E}}^{\nu^{k,j}\_{L-1}}\_{L-1} means that the expectation is taken only over μ~~𝜇\tilde{\mu} according to the law νL−1k,jsubscriptsuperscript𝜈

𝑘𝑗𝐿1\nu^{k,j}\_{L-1}, i.e. 𝒩​𝒲−1​(𝚙L−1k,j)𝒩superscript𝒲1subscriptsuperscript𝚙

𝑘𝑗𝐿1{\cal NW}^{-1}(\mathtt{p}^{k,j}\_{{L-1}}), and (⋅)isuperscript⋅𝑖(\cdot)^{i} means that we take the i𝑖i-th component of the vector in the brackets.
Then, for any α∈𝒜ad𝛼superscript𝒜ad\alpha\in{\mathcal{A}}^{\rm ad},
we set

|  |  |  |
| --- | --- | --- |
|  | ϕˇL−1​(qL−1α,NL−1α,CL−1α,⋅):=min(0,δ​N)∈A​(L−1,α)⁡ϕxˇL−1​(0,δ​N,qL−1α,NL−1α,CL−1α,⋅),assignsubscriptˇitalic-ϕ𝐿1subscriptsuperscript𝑞𝛼𝐿1subscriptsuperscript𝑁𝛼𝐿1subscriptsuperscript𝐶𝛼𝐿1⋅subscript0𝛿𝑁A𝐿1𝛼subscriptitalic-ϕsubscriptˇx𝐿10𝛿𝑁subscriptsuperscript𝑞𝛼𝐿1subscriptsuperscript𝑁𝛼𝐿1subscriptsuperscript𝐶𝛼𝐿1⋅\check{\phi}\_{L-1}(q^{\alpha}\_{L-1},N^{\alpha}\_{L-1},C^{\alpha}\_{L-1},\cdot):=\min\_{{\left(0,\delta N\right)}\in{\rm A}(L-1,\alpha)}\phi\_{\check{\rm x}\_{L-1}}(0,\delta N,q^{\alpha}\_{L-1},N^{\alpha}\_{L-1},{C^{\alpha}\_{L-1}},\cdot), |  |

where

|  |  |  |
| --- | --- | --- |
|  | A​(L−1,α):={(δ​q,δ​N)∈{0}×ℕ:CL−1α+nw​δ​N≤K}.assignA𝐿1𝛼conditional-set𝛿𝑞𝛿𝑁0ℕsubscriptsuperscript𝐶𝛼𝐿1subscript𝑛𝑤𝛿𝑁𝐾{\rm A}(L-1,\alpha):=\{(\delta q,\delta N)\in\{0\}\times{\mathbb{N}}:C^{\alpha}\_{L-1}+n\_{w}\delta N\leq K\}. |  |

Given ϕˇℓ+1subscriptˇitalic-ϕℓ1\check{\phi}\_{\ell+1} for some ℓ≤L−2ℓ𝐿2\ell\leq L-2, we then compute a minimizer xˇℓ∈XsubscriptˇxℓX\check{\rm x}\_{\ell}\in{\rm X} of

|  |  |  |
| --- | --- | --- |
|  | ∑k=1k¯∑j=1j¯|𝔼ℓνℓk,j[ϕˇℓ+1(qℓ+1αk,Nℓ+1αk,Cℓ+1αk,μ^ℓ+1k,𝚙ℓ+1k)+fpad,k,j(ℓ+1,αk,θ~)]−ϕx(δqℓ+1αk,δNℓ+1αk,qℓαk,Nℓαk,Cℓαk,μ^ℓk,j,𝚙ℓk,j)|r,superscriptsubscript𝑘1¯𝑘superscriptsubscript𝑗1¯𝑗superscriptsubscriptsuperscript𝔼subscriptsuperscript𝜈  𝑘𝑗ℓℓdelimited-[]subscriptˇitalic-ϕℓ1subscriptsuperscript𝑞superscript𝛼𝑘ℓ1subscriptsuperscript𝑁superscript𝛼𝑘ℓ1subscriptsuperscript𝐶superscript𝛼𝑘ℓ1subscriptsuperscript^𝜇𝑘ℓ1subscriptsuperscript𝚙𝑘ℓ1subscriptsuperscript𝑓  ad𝑘𝑗𝑝ℓ1superscript𝛼𝑘~𝜃subscriptitalic-ϕx𝛿subscriptsuperscript𝑞superscript𝛼𝑘ℓ1𝛿subscriptsuperscript𝑁superscript𝛼𝑘ℓ1subscriptsuperscript𝑞superscript𝛼𝑘ℓsubscriptsuperscript𝑁superscript𝛼𝑘ℓsubscriptsuperscript𝐶superscript𝛼𝑘ℓsubscriptsuperscript^𝜇  𝑘𝑗ℓsubscriptsuperscript𝚙  𝑘𝑗ℓ𝑟\begin{split}\sum\_{k=1}^{\bar{k}}\sum\_{j=1}^{\bar{j}}&\bigg{|}{\mathbb{E}}^{\nu^{k,j}\_{\ell}}\_{\ell}\left[\check{\phi}\_{\ell+1}(q^{\alpha^{k}}\_{\ell+1},N^{\alpha^{k}}\_{\ell+1},C^{\alpha^{k}}\_{\ell+1},\hat{\mu}^{k}\_{\ell+1},\mathtt{p}^{k}\_{\ell+1})+f^{{\rm ad},k,j}\_{p}(\ell+1,\alpha^{k},\tilde{\theta})\right]\\ &-\phi\_{{\rm x}}(\delta q^{\alpha^{k}}\_{\ell+1},\delta N^{\alpha^{k}}\_{\ell+1},q^{\alpha^{k}}\_{\ell},N^{\alpha^{k}}\_{\ell},C^{\alpha^{k}}\_{\ell},\hat{\mu}^{k,j}\_{\ell},\mathtt{p}^{k,j}\_{\ell})\bigg{|}^{r},\end{split} |  |

where 𝔼ℓνℓk,jsubscriptsuperscript𝔼subscriptsuperscript𝜈

𝑘𝑗ℓℓ{\mathbb{E}}^{\nu^{k,j}\_{\ell}}\_{\ell} means that the expectation is computed over (μ^ℓ+1αk,𝚙ℓ+1αk,θ~,𝔪~ℓαk)subscriptsuperscript^𝜇superscript𝛼𝑘ℓ1subscriptsuperscript𝚙superscript𝛼𝑘ℓ1~𝜃subscriptsuperscript~𝔪superscript𝛼𝑘ℓ(\hat{\mu}^{\alpha^{k}}\_{\ell+1},\mathtt{p}^{\alpha^{k}}\_{\ell+1},\tilde{\theta},\tilde{\mathfrak{m}}^{\alpha^{k}}\_{\ell}) given (μ^ℓk,𝚙ℓk)=(μ^ℓk,j,𝚙ℓk,j)subscriptsuperscript^𝜇𝑘ℓsubscriptsuperscript𝚙𝑘ℓsubscriptsuperscript^𝜇

𝑘𝑗ℓsubscriptsuperscript𝚙

𝑘𝑗ℓ(\hat{\mu}^{k}\_{\ell},\mathtt{p}^{k}\_{\ell})=(\hat{\mu}^{k,j}\_{\ell},\mathtt{p}^{k,j}\_{\ell}) and using the prior νℓk,jsubscriptsuperscript𝜈

𝑘𝑗ℓ\nu^{k,j}\_{\ell} on θ~~𝜃\tilde{\theta} associated to 𝚙ℓk,jsubscriptsuperscript𝚙

𝑘𝑗ℓ\mathtt{p}^{k,j}\_{\ell}. Then, we set

|  |  |  |
| --- | --- | --- |
|  | ϕˇℓ​(qℓα,Nℓα,Cℓα,⋅):=min(δ​q,δ​N)∈A​(ℓ,α)⁡ϕxˇℓ​(δ​q,δ​N,qℓα,Nℓα,Cℓα,⋅),assignsubscriptˇitalic-ϕℓsubscriptsuperscript𝑞𝛼ℓsubscriptsuperscript𝑁𝛼ℓsubscriptsuperscript𝐶𝛼ℓ⋅subscript𝛿𝑞𝛿𝑁Aℓ𝛼subscriptitalic-ϕsubscriptˇxℓ𝛿𝑞𝛿𝑁subscriptsuperscript𝑞𝛼ℓsubscriptsuperscript𝑁𝛼ℓsubscriptsuperscript𝐶𝛼ℓ⋅\check{\phi}\_{\ell}(q^{\alpha}\_{\ell},N^{\alpha}\_{\ell},C^{\alpha}\_{\ell},\cdot):=\min\_{{\left(\delta q,\delta N\right)}\in{\rm A}(\ell,\alpha)}\phi\_{\check{\rm x}\_{\ell}}(\delta q,\delta N,q^{\alpha}\_{\ell},N^{\alpha}\_{\ell},{C^{\alpha}\_{\ell}},\cdot), |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(ℓ,α)Aℓ𝛼\displaystyle{\rm A}(\ell,\alpha) | :={(δ​q,δ​N)∈[[0,qℓα−nw]]×ℕ:Cℓα+(qℓα−δ​q)​δ​N≤K},ℓ<L−2,formulae-sequenceassignabsentconditional-set𝛿𝑞𝛿𝑁delimited-[]0subscriptsuperscript𝑞𝛼ℓsubscript𝑛𝑤ℕsubscriptsuperscript𝐶𝛼ℓsubscriptsuperscript𝑞𝛼ℓ𝛿𝑞𝛿𝑁𝐾ℓ𝐿2\displaystyle:=\{(\delta q,\delta N)\in[\![{0},q^{\alpha}\_{\ell}-{n\_{w}}]\!]\times{\mathbb{N}}:{C^{\alpha}\_{\ell}}+{(q^{\alpha}\_{\ell}-\delta q)}\delta N\leq K\},\;\ell<L-2, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(L−2,α)A𝐿2𝛼\displaystyle{\rm A}(L-2,\alpha) | :={(δ​q,δ​N)∈{qℓα−nw}×ℕ:CL−1α+(qL−2α−δ​q)​δ​N≤K},assignabsentconditional-set𝛿𝑞𝛿𝑁subscriptsuperscript𝑞𝛼ℓsubscript𝑛𝑤ℕsubscriptsuperscript𝐶𝛼𝐿1subscriptsuperscript𝑞𝛼𝐿2𝛿𝑞𝛿𝑁𝐾\displaystyle:=\{(\delta q,\delta N)\in\{q^{\alpha}\_{\ell}-n\_{w}\}\times{\mathbb{N}}:{C^{\alpha}\_{L-1}}+{(q^{\alpha}\_{L-2}-\delta q)}\delta N\leq K\}, |  |

and so on until obtaining ϕ0​(ns,0,0,0,𝚙0)subscriptitalic-ϕ0subscript𝑛𝑠000subscript𝚙0\phi\_{{0}}({n\_{s},0},0,0,\mathtt{p}\_{0}). By continuity of ϕ⋅​(⋅)subscriptitalic-ϕ⋅⋅\phi\_{\cdot}(\cdot) and compactness of XX{\rm X} and A​(ℓ,α)Aℓ𝛼{\rm A}(\ell,\alpha) for α𝛼\alpha given, the minimum is achieved in the above, possibly not unique, and one can choose a measurable map aℓ⋆subscriptsuperscripta⋆ℓ{\rm a}^{\star}\_{{\ell}} such that

|  |  |  |
| --- | --- | --- |
|  | aℓ⋆​(qℓα,Nℓα,Cℓα,⋅)∈arg​min(δ​q,δ​N)∈A​(ℓ,α)⁡ϕxˇℓN​(δ​q,δ​N,qℓα,Nℓα,Cℓα,⋅)subscriptsuperscripta⋆ℓsubscriptsuperscript𝑞𝛼ℓsubscriptsuperscript𝑁𝛼ℓsubscriptsuperscript𝐶𝛼ℓ⋅argsubscript𝛿𝑞𝛿𝑁Aℓ𝛼subscriptitalic-ϕsubscriptsuperscriptˇ𝑥𝑁ℓ𝛿𝑞𝛿𝑁subscriptsuperscript𝑞𝛼ℓsubscriptsuperscript𝑁𝛼ℓsubscriptsuperscript𝐶𝛼ℓ⋅{\rm a}^{\star}\_{{\ell}}(q^{\alpha}\_{\ell},N^{\alpha}\_{\ell},C^{\alpha}\_{\ell},\cdot)\in\mbox{arg}\min\_{{\left(\delta q,\delta N\right)}\in{\rm A}(\ell,\alpha)}\phi\_{\check{x}^{N}\_{\ell}}(\delta q,\delta N,q^{\alpha}\_{\ell},N^{\alpha}\_{\ell},{C^{\alpha}\_{\ell}},\cdot) |  |

for all α∈𝒜ad𝛼superscript𝒜ad\alpha\in{\mathcal{A}}^{\rm ad}. Then, given the parameter 𝚙0subscript𝚙0\mathtt{p}\_{0} of our initial prior ν0subscript𝜈0\nu\_{0}, our estimator of the optimal policy is given by α⋆=(q⋆,N⋆)superscript𝛼⋆superscript𝑞⋆superscript𝑁⋆\alpha^{\star}=(q^{\star},N^{\star}) defined by induction by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (δ​q1⋆,δ​N1⋆)𝛿subscriptsuperscript𝑞⋆1𝛿subscriptsuperscript𝑁⋆1\displaystyle(\delta q^{\star}\_{1},\delta N^{\star}\_{1}) | =a0⋆​(ns,0,0,0,𝚙0)​ and ​(δ​qℓ+1⋆,δ​Nℓ+1⋆)=aℓ⋆​(qℓ⋆,Nℓ⋆,Cℓ⋆,μ^ℓα⋆,𝚙ℓα⋆)​ for ​0<ℓ<L.absentsubscriptsuperscripta⋆0subscript𝑛𝑠000subscript𝚙0 and 𝛿subscriptsuperscript𝑞⋆ℓ1𝛿subscriptsuperscript𝑁⋆ℓ1subscriptsuperscripta⋆ℓsubscriptsuperscript𝑞⋆ℓsubscriptsuperscript𝑁⋆ℓsubscriptsuperscript𝐶⋆ℓsubscriptsuperscript^𝜇superscript𝛼⋆ℓsubscriptsuperscript𝚙superscript𝛼⋆ℓ for 0ℓ𝐿\displaystyle={\rm a}^{\star}\_{{0}}(n\_{s},0,0,0,\mathtt{p}\_{0})\;\mbox{ and }\;(\delta q^{\star}\_{\ell+1},\delta N^{\star}\_{\ell+1})={\rm a}^{\star}\_{{\ell}}(q^{\star}\_{\ell},N^{\star}\_{\ell},C^{\star}\_{\ell},\hat{\mu}^{\alpha^{\star}}\_{\ell},\mathtt{p}^{\alpha^{\star}}\_{\ell})\;\mbox{ for }0<\ell<L. |  |

Note that the above algorithm for the estimation of the optimal control only requires off-line simulations according to the initial prior ν0subscript𝜈0\nu\_{0}. It is certainly costly but does not require to evaluate the real financial book, it can be trained on a proxy, and can be done off-line. It can be combined with the approach of Remark [3.6](#S3.Thmtheorem6 "Remark 3.6. ‣ 3.2 A generic progressive learning algorithm ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios") to reduce the computation time. In order to prepare for the use of a different initial prior, one can also slightly adapt the above algorithm by considering different initial values of 𝚙0subscript𝚙0\mathtt{p}\_{0} (e.g. drawn from another distribution around 𝚙0subscript𝚙0\mathtt{p}\_{0}), so as to estimate ϕˇ0subscriptˇitalic-ϕ0\check{\phi}\_{0} not only at the point 𝚙0subscript𝚙0\mathtt{p}\_{0}. When applied to the real book, the update of the prior according to ([29](#S3.E29 "In Remark 3.7. ‣ 3.2 A generic progressive learning algorithm ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios")) leads to an additional cost that is negligible with respect to the simulation of the book. It leads to the computation of new priors associated to the financial book at hand, that can be used for a new estimation of the optimal policy or simply as a new initial prior for the next computation of the ESES{\rm ES}.

An example of a simple practical implementation is detailed in Appendix [B](#A2 "Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), while numerical tests are performed in Section [4](#S4 "4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios").

## 4 Numerical Experiments

This section is dedicated to first numerical tests of the different algorithms presented in the previous sections. The settings of the experiments are as follows. We first choose a Normal-inverse-Wishart prior distribution ν0subscript𝜈0\nu\_{0} with parameters 𝚙0:=(𝚖0,𝚔0,𝚒0,Σ0)assignsubscript𝚙0subscript𝚖0subscript𝚔0subscript𝚒0subscriptΣ0\mathtt{p}\_{0}:=({\mathtt{m}}\_{0},{\mathtt{k}}\_{0},{\mathtt{i}}\_{0},\Sigma\_{0}). The vector 𝚖0subscript𝚖0{\mathtt{m}}\_{0} is represented on Figure [6](#S2.F6 "Figure 6 ‣ 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") with 𝚖0i=μisuperscriptsubscript𝚖0𝑖superscript𝜇𝑖{\mathtt{m}}\_{0}^{i}=\mu^{i}, i≤ns𝑖subscript𝑛𝑠i\leq n\_{s}, and Σ0=(𝚒0−ns−1)​ΣsubscriptΣ0subscript𝚒0subscript𝑛𝑠1Σ\Sigma\_{0}=({\mathtt{i}}\_{0}-n\_{s}-1)\Sigma where ΣΣ\Sigma has entries

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Σi​i=4.84×1012​ if ​i=jΣi​j=ρ×4.84×1012​ if ​i≠j,casessuperscriptΣ𝑖𝑖4.84superscript1012 if 𝑖𝑗otherwisesuperscriptΣ𝑖𝑗𝜌4.84superscript1012 if 𝑖𝑗otherwise\begin{cases}\Sigma^{ii}=4.84\times 10^{12}\textnormal{ if }i=j\\ \Sigma^{ij}=\rho\times 4.84\times 10^{12}\textnormal{ if }i\neq j,\end{cases} |  | (30) |

with ρ=0.6𝜌0.6\rho=0.6 or ρ=0𝜌0\rho=0 depending on the experiments below.
As for 𝚔0subscript𝚔0{\mathtt{k}}\_{0} and 𝚒0subscript𝚒0{\mathtt{i}}\_{0}, they are chosen equal to 300, meaning that we have a low confidence in our prior. The computing power is K=107𝐾superscript107K=10^{7}.

We apply the four different algorithms on 5 000 runs (i.e. 5 000 independent implementations of each algorithm). For each run, we

* •

  first simulate a value for the real scenarios and covariance matrices (μ~,Σ~)∼𝒩​𝒲−1​(𝚙0)similar-to~𝜇~Σ𝒩superscript𝒲1subscript𝚙0\left(\tilde{\mu},\tilde{\Sigma}\right)\sim\mathcal{NW}^{-1}(\mathtt{p}\_{0}),
* •

  apply each of the four algorithms, with simulated prices following P|s∼𝒩​(μ~,Σ~)P\_{{|{\rm s}}}\sim{\mathcal{N}}\left(\tilde{\mu},{\tilde{\Sigma}}\right),
* •

  for each algorithm, we measure the relative error E​S^−ES~ES~^𝐸𝑆~ES~ES\frac{\widehat{ES}-\widetilde{\rm ES}}{\widetilde{\rm ES}} and the error ES^−ES~^ES~ES\widehat{\rm ES}-\widetilde{\rm ES}, where ES~=1nw​∑i=1nwμ~𝔪~​(i)~ES1subscript𝑛𝑤superscriptsubscript𝑖1subscript𝑛𝑤superscript~𝜇~𝔪𝑖\widetilde{\rm ES}=\frac{1}{n\_{w}}\sum\_{i=1}^{n\_{w}}\tilde{\mu}^{\tilde{\mathfrak{m}}(i)}.

The four algorithms that we compare are:

* •

  A Uniform Pricing Algorithm: All the scenarios are priced with K/ns𝐾subscript𝑛𝑠K/n\_{s} Monte Carlo simulations, and the estimator ES^^ES\widehat{\rm ES} is the average of the nw=6subscript𝑛𝑤6n\_{w}=6 worst scenarios. This is the most naive method, with only one step and where all scenarios are priced with an equal number of Monte Carlo simulations. It serves as a benchmark.
* •

  The Heuristic Algorithm: We use the 2-levels strategy described in Section [2.5](#S2.SS5 "2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") with the book sample parameters of Table [1](#S2.T1 "Table 1 ‣ 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") and the computation parameters of Table [2](#S2.T2 "Table 2 ‣ 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios"). We do not evaluate the constant c𝑐c of Assumption [1](#Thmassumption1 "Assumption 1. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") but simply set it to 00, see Remark [2.4](#S2.Thmtheorem4 "Remark 2.4. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios"). The optimal strategy is given by (q0,q1,N1,N2)=(253,68,17 297,100 000)subscript𝑞0subscript𝑞1subscript𝑁1subscript𝑁22536817297100000\left(q\_{0},q\_{1},N\_{1},N\_{2}\right)=(253,68,17\,297,100\,000).
* •

  The Deterministic Algorithm: We run the deterministic algorithm of Section [2.4](#S2.SS4 "2.4 Optimal a-priori allocation by deterministic dynamic programming based on fixed a-priori bounds ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") optimized with μ=𝚖0𝜇subscript𝚖0\mu={\mathtt{m}}\_{0} as the values of the scenarios, ΣΣ\Sigma with ρ=0.6𝜌0.6\rho=0.6 as the covariance matrix and L=4𝐿4L=4. Note that using the real mean parameter as an entry for optimization is quite favorable for this algorithm, although the “true” parameter of each run will actually deviate from this mean value. This gives us the strategy (q0,q1,q2,q3,N0,N1,N2,N3,N4)=(253,35,10,6,0,6 000,44 000,44 000,1 235 666)subscript𝑞0subscript𝑞1subscript𝑞2subscript𝑞3subscript𝑁0subscript𝑁1subscript𝑁2subscript𝑁3subscript𝑁4253351060600044000440001235666\left(q\_{0},q\_{1},q\_{2},q\_{3},N\_{0},N\_{1},N\_{2},N\_{3},N\_{4}\right)=\left(253,35,10,6,0,6\,000,44\,000,44\,000,1\,235\,666\right), which we apply to each run.
* •

  The Adaptative Algorithm: We do the training part of the adaptative algorithm using our prior 𝚙0:=(𝚖0,𝚔0,𝚒0,Σ0)assignsubscript𝚙0subscript𝚖0subscript𝚔0subscript𝚒0subscriptΣ0\mathtt{p}\_{0}:=({\mathtt{m}}\_{0},{\mathtt{k}}\_{0},{\mathtt{i}}\_{0},\Sigma\_{0}), with ρ=0.6𝜌0.6\rho=0.6, as parameters and L=4𝐿4L=4. We use a very simple one hidden-layer neural network. It could certainly be improved by using a more sophisticated multi-layers neural network, but this version will be enough for our discussion. Details on the implementation are given in the Appendix [B](#A2 "Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios").
  Once this is done, we apply the optimal adaptative strategy on each run.

### 4.1 Positively correlated scenarios ρ=0.6𝜌0.6\rho=0.6

In this first experiment, the simulated runs use the values ρ=0.6𝜌0.6\rho=0.6 and 𝚒0=𝚔0=300subscript𝚒0subscript𝚔0300{\mathtt{i}}\_{0}={\mathtt{k}}\_{0}=300.

To get an idea of how much noise is added to the average scenario values in our simulations, we plot in Figure [7](#S4.F7 "Figure 7 ‣ 4.1 Positively correlated scenarios 𝜌=0.6 ‣ 4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios") the prior value 𝚖0isuperscriptsubscript𝚖0𝑖{\mathtt{m}}\_{0}^{i} for each scenario of index i≤ns𝑖subscript𝑛𝑠i\leq n\_{s} (this is the line) and the first 202020 μ~jisubscriptsuperscript~𝜇𝑖𝑗\tilde{\mu}^{i}\_{j} out of the 5 00050005\,000 runs for each scenario (these are the points).

![Refer to caption](/html/2005.12593/assets/scenario_values_graph.png)


Figure 7: True value of μ∘subscript𝜇\mu\_{\circ} and simulations of μ~~𝜇\tilde{\mu}

For the adaptative algorithm, the three mostly used strategies are:

* •

  (q0,q1,q2,q3,N1,N2,N3,N4)=(253,40,25,6,8 399,97 995,172 504,577 252)subscript𝑞0subscript𝑞1subscript𝑞2subscript𝑞3subscript𝑁1subscript𝑁2subscript𝑁3subscript𝑁425340256839997995172504577252\left(q\_{0},q\_{1},q\_{2},q\_{3},N\_{1},N\_{2},N\_{3},N\_{4}\right)=\left(253,40,25,6,8\,399,97\,995,172\,504,577\,252\right)
* •

  (q0,q1,q2,q3,N1,N2,N3,N4)=(253,40,30,6,8 399,99 733,148 560,608 040)subscript𝑞0subscript𝑞1subscript𝑞2subscript𝑞3subscript𝑁1subscript𝑁2subscript𝑁3subscript𝑁425340306839999733148560608040\left(q\_{0},q\_{1},q\_{2},q\_{3},N\_{1},N\_{2},N\_{3},N\_{4}\right)=\left(253,40,30,6,8\,399,99\,733,148\,560,608\,040\right)
* •

  (q0,q1,q2,q3,N1,N2,N3,N4)=(253,40,30,6,8 399,75 033,123 860,748 007)subscript𝑞0subscript𝑞1subscript𝑞2subscript𝑞3subscript𝑁1subscript𝑁2subscript𝑁3subscript𝑁425340306839975033123860748007\left(q\_{0},q\_{1},q\_{2},q\_{3},N\_{1},N\_{2},N\_{3},N\_{4}\right)=\left(253,40,30,6,8\,399,75\,033,123\,860,748\,007\right)

Compared to the deterministic algorithm, we see that the adaptative one uses much less Monte Carlo simulations at the final steps and focuses more on the intermediate steps to select the worst scenarios. The deterministic algorithm is also more aggressive in the choice of q1subscript𝑞1q\_{1} and q2subscript𝑞2q\_{2}. This can be easily explained by the fact that the latter believes that the real distribution is not far from the solid curve on Figure [7](#S4.F7 "Figure 7 ‣ 4.1 Positively correlated scenarios 𝜌=0.6 ‣ 4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios") (up to standard deviation) while the adaptative one only knows a much more diffuse distribution corresponding to the cloud of points of Figure [7](#S4.F7 "Figure 7 ‣ 4.1 Positively correlated scenarios 𝜌=0.6 ‣ 4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios") since his level of uncertainty is quite high for our choice 𝚒0=𝚔0=300subscript𝚒0subscript𝚔0300{\mathtt{i}}\_{0}={\mathtt{k}}\_{0}=300.

On Figures [11](#S4.F11 "Figure 11 ‣ 4.1 Positively correlated scenarios 𝜌=0.6 ‣ 4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios")-[11](#S4.F11 "Figure 11 ‣ 4.1 Positively correlated scenarios 𝜌=0.6 ‣ 4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), we plot the histograms of the relative errors. We see that the distribution is tightest for the deterministic algorithm, followed quite closely by the adaptative algorithm. Both of them perform very well. As expected, the uniform algorithm is very poor. Note that the heuristic one already very significantly improves the uniform algorithm, although it does not reach the precision of the two most sophisticated algorithms (without surprise). Because of the huge uncertainty mentioned above, the adaptative algorithm is rather conservative while the deterministic algorithm makes full profit of essentially knowing the correct distribution, and performs better. We will see in our second experiment that things will change when we will deviate from the parameters used for optimizing the deterministic algorithm (by simply passing from ρ=0.6𝜌0.6\rho=0.6 to ρ=0𝜌0\rho=0 in the simulated runs).

![Refer to caption](/html/2005.12593/assets/er_dist_ind_ad_rho_0-6.png)


Figure 8: Relative Error for Adaptative Algorithm

![Refer to caption](/html/2005.12593/assets/er_dist_ind_det_rho_0-6.png)


Figure 9: Relative Error for Determinist Algorithm

![Refer to caption](/html/2005.12593/assets/er_dist_ind_heur_1_rho_0-6.png)


Figure 10: Relative Error for Heuristic Algorithm

![Refer to caption](/html/2005.12593/assets/er_dist_ind_uni_rho_0-6.png)


Figure 11: Relative Error for Uniform Algorithm

In Table [3](#S4.T3 "Table 3 ‣ 4.1 Positively correlated scenarios 𝜌=0.6 ‣ 4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), we provide the 𝕃1superscript𝕃1{\mathbb{L}}^{1} and relative errors (with standard deviations), the 𝕃2superscript𝕃2{\mathbb{L}}^{2} error and the number of correct selections, that is the number of runs for which a given algorithm has chosen the correct worst 6 scenarios. In terms of 𝕃1superscript𝕃1{\mathbb{L}}^{1} or 𝕃2superscript𝕃2{\mathbb{L}}^{2} error, the relative performance of the algorithms is as above. However, if we look at the number of correct selections, we see that the adaptive algorithm performs better than the other 3 algorithms. Again, by comparing the strategies of the deterministic and the adaptive algorithms, we see that those of the adaptative algorithm are more conservative on the ranking and filtering part versus the final pricing as it puts relatively more Monte Carlo simulations to detect the correct scenarios and relatively less for their estimation.

| Algorithm | 𝕃1superscript𝕃1{\mathbb{L}}^{1} Err. | 𝕃1superscript𝕃1{\mathbb{L}}^{1} Err. Std | Rel. Err. (%) | Rel. Err. Std (%) | 𝕃2superscript𝕃2{\mathbb{L}}^{2} Err. | Correct Selections |
| --- | --- | --- | --- | --- | --- | --- |
| Ad. Alg. | 1 891 | 20.4 | 0.623 | 0.00886 | 2377 | 4247 |
| Det. Alg. | 1 411 | 16.1 | 0.465 | 0.00693 | 1813 | 3499 |
| Heur. Alg. | 4 562 | 50.2 | 1.49 | 0.0234 | 5779 | 4054 |
| Unif. Alg. | 7 269 | 81.6 | 2.38 | 0.0348 | 9279 | 3500 |

Table 3: Errors for ρ=0.6𝜌0.6\rho=0.6

In Figures [12](#S4.F12.1 "Figure 12 ‣ 4.1 Positively correlated scenarios 𝜌=0.6 ‣ 4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), we plot the function x↦ℙ​[X>5000−x]maps-to𝑥ℙdelimited-[]𝑋5000𝑥x\mapsto\mathbb{P}[X>5000-x] where X𝑋X is the absolute error of the algorithm on a run.

![Refer to caption](/html/2005.12593/assets/L1_all_cdf_06.png)


Figure 12: Tail Distribution of the errors. First top lines: Uniform and Heuristic algorithms, respectively. Solid line: Adaptative algorithm. Dotted line: Deterministic algorithm.

In Figure [13](#S4.F13 "Figure 13 ‣ 4.1 Positively correlated scenarios 𝜌=0.6 ‣ 4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), we provide, for the first 4 runs, the values and real ranks of the 6 worst scenarios selected by each algorithm. The numbers displayed are the true ranks of the selected scenarios given by μ~~𝜇\tilde{\mu} and their y-coordinate is the value obtained when running the algorithm. “Real” is the real values as sampled.

![Refer to caption](/html/2005.12593/assets/numbers_graph.png)


Figure 13: Worst Scenarios Ranks and Values

### 4.2 Uncorrelated scenarios ρ=0𝜌0\rho=0

We now do the numerical test with ρ=0𝜌0\rho=0 as the true correlation. The deterministic and adaptative algorithm are still trained with ρ=0.6𝜌0.6\rho=0.6, but P|sP\_{|{\rm s}} is simulated using ρ=0𝜌0\rho=0.

On Figures [17](#S4.F17 "Figure 17 ‣ 4.2 Uncorrelated scenarios 𝜌=0 ‣ 4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios")-[17](#S4.F17 "Figure 17 ‣ 4.2 Uncorrelated scenarios 𝜌=0 ‣ 4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), we show the histograms of the relative errors. We see that the distribution of the relative errors is now tightest for the adaptative method, followed by the deterministic method, then by the heuristic and the uniform methods. Furthermore, we see that the distribution corresponding to the deterministic method is significantly biased to the left. This is actually true for all algorithms, but at a less significant level. This suggests that we now have a large part of the error that does not come from the final pricing error, but from errors in the selection of scenarios.

![Refer to caption](/html/2005.12593/assets/er_dist_ind_ad_rho_0.png)


Figure 14: Relative Error for Adaptative Algorithm

![Refer to caption](/html/2005.12593/assets/er_dist_ind_det_rho_0.png)


Figure 15: Relative Error for Determinist Algorithm

![Refer to caption](/html/2005.12593/assets/er_dist_ind_heur_1_rho_0.png)


Figure 16: Relative Error for Heuristic Algorithm

![Refer to caption](/html/2005.12593/assets/er_dist_ind_uni_rho_0.png)


Figure 17: Relative Error for Uniform Algorithm

In Table [4](#S4.T4 "Table 4 ‣ 4.2 Uncorrelated scenarios 𝜌=0 ‣ 4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), we provide the 𝕃1superscript𝕃1{\mathbb{L}}^{1} and relative errors (with standard deviations), the 𝕃2superscript𝕃2{\mathbb{L}}^{2} error and the number of correct selections for the 4 algorithms. For all algorithms, compared to the case ρ=0.6𝜌0.6\rho=0.6, we see that we have simultaneously a lower number of correct selections of scenarios (which we could expect to increase the errors) and a lower 𝕃1superscript𝕃1{\mathbb{L}}^{1} error. This surprising result is explained by the fact that lowering the correlation has two effects. The filtering and ranking part of the algorithm becomes harder, as can be seen from Corollary [2.3](#S2.Thmtheorem3 "Corollary 2.3. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios"). This explains why the number of correct selections becomes lower. However, we compute at the end an average over the nwsubscript𝑛𝑤n\_{w} worst scenarios and the error on this average is lower when the pricings are uncorrelated compared to the case where they exhibit a positive correlation.

The adaptative algorithm has now simultaneously the lowest 𝕃1superscript𝕃1{\mathbb{L}}^{1} and 𝕃2superscript𝕃2{\mathbb{L}}^{2} errors, as well as the highest number of correct selections. We see that it is especially good in 𝕃2superscript𝕃2{\mathbb{L}}^{2} error, so we expect it to present a very low number of large errors. As, by construction, it has been trained to detect misspecifications of the parameters, it now has a clear advantage on the deterministic algorithm which does not see it. This results in an improvement of almost 20% of the 𝕃2superscript𝕃2{\mathbb{L}}^{2} error.

Following the above reasoning, we understand that, compared to the previous experiment, the final pricing error now plays a smaller role and the ranking and selection error a bigger role, which explains why the histogram of the errors for the determinist algorithm is strongly biased to the left, as it now incorrectly selects scenarios more often.

| Algorithm | 𝕃1superscript𝕃1{\mathbb{L}}^{1} Err. | 𝕃1superscript𝕃1{\mathbb{L}}^{1} Err. Std | Rel. Err. (%) | Rel. Err. Std (%) | 𝕃2superscript𝕃2{\mathbb{L}}^{2} Err. | Correct Selections |
| --- | --- | --- | --- | --- | --- | --- |
| Ad. Alg. | 1 083 | 11.8 | 0.27 | 0.00294 | 1 366 | 3 930 |
| Det. Alg. | 1 175 | 17.5 | 0.293 | 0.00448 | 1 705 | 3 202 |
| Heur. Alg. | 2 547 | 28.33 | 0.628 | 0.00700 | 3 240 | 3 753 |
| Unif. Alg. | 4 062 | 44.7 | 1.00 | 0.0111 | 5 147 | 3 102 |

Table 4: Errors for ρ=0𝜌0\rho=0

In Figures [18](#S4.F18.1 "Figure 18 ‣ 4.2 Uncorrelated scenarios 𝜌=0 ‣ 4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), we plot the function x↦ℙ​[X>5000−x]maps-to𝑥ℙdelimited-[]𝑋5000𝑥x\mapsto\mathbb{P}[X>5000-x] where X𝑋X is the absolute error of the algorithm on a run. As was suggested by the 𝕃2superscript𝕃2{\mathbb{L}}^{2} errors of Table [4](#S4.T4 "Table 4 ‣ 4.2 Uncorrelated scenarios 𝜌=0 ‣ 4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), we see that the tail distribution of errors is lowest for the adaptative algorithm, followed by the deterministic algorithm (for big errors), and then by the heuristic and uniform algorithms.

![Refer to caption](/html/2005.12593/assets/L1_all_cdf_0.png)


Figure 18: Tail Distribution of the errors. First top lines: Uniform and Heuristic algorithms, respectively. Solid line: Adaptative algorithm. Dotted line: Determinist algorithm

## 5 Conclusion

We propose in this paper different algorithms for the computation of the expected shortfall based on given historical scenarios. All are multi-steps algorithms that use Monte Carlo simulations to reduce the number of historical scenarios that potentially belong to the set of worst scenarios. We provide explicit error bounds and we test them on simulated data deviating from the true values of the historical impacts used for computing the associated optimal strategies. The first algorithm is a very easy to implement 222-steps algorithm that already provides relatively small errors on our numerical tests. A four step deterministic dynamic programming algorithm performs very well when real datas are not far from the parameters used in the optimization procedure. It seems even to be quite robust, as shown by our numerical test in the case where the true correlation parameter is not the one used for computing the optimal policy. Finally, we propose an adaptative algorithm that aims at learning the true value of the parameters at the different steps of the algorithm. Our first numerical tests suggest that it is more conservative than the deterministic one, but probably more robust to parameters misspecifications, as expected. The version we use is built on a very simple one hidden layer neural network and can certainly be considerably improved for industrial purposes.

## References

* [1]

  Carlo Acerbi and Dirk Tasche.
  On the coherence of expected shortfall.
  Journal of Banking & Finance, 26(7):1487–1503, 2002.
* [2]

  Philippe Artzner, Freddy Delbaen, Jean-Marc Eber, and David Heath.
  Coherent measures of risk.
  Mathematical finance, 9(3):203–228, 1999.
* [3]

  Raghu Raj Bahadur and Herbert Robbins.
  The problem of the greater mean.
  The Annals of Mathematical Statistics, pages 469–487, 1950.
* [4]

  Basel Committee on Banking Supervision.
  Minimum capital requirements for market risk.
  2016.
* [5]

  Robert E Bechhofer.
  A single-sample multiple decision procedure for ranking means of
  normal populations with known variances.
  The Annals of Mathematical Statistics, pages 16–39, 1954.
* [6]

  Robert E Bechhofer, Charles W Dunnett, and Milton Sobel.
  A tow-sample multiple decision procedure for ranking means of normal
  populations with a common unknown variance.
  Biometrika, 41(1-2):170–176, 1954.
* [7]

  Bernard Bercu, Bernard Delyon, and Emmanuel Rio.
  Concentration inequalities for sums and martingales.
  Springer, 2015.
* [8]

  Mark Broadie, Yiping Du, and Ciamac C Moallemi.
  Efficient risk estimation via nested sequential simulation.
  Management Science, 57(6):1172–1194, 2011.
* [9]

  Simon A Broda, Jochen Krause, and Marc S Paolella.
  Approximating expected shortfall for heavy-tailed distributions.
  Econometrics and statistics, 8:184–203, 2018.
* [10]

  David Easley and Nicholas M Kiefer.
  Controlling a stochastic process with unknown parameters.
  Econometrica: Journal of the Econometric Society, pages
  1045–1064, 1988.
* [11]

  Robert J Elliott and Hong Miao.
  Var and expected shortfall: a non-normal regime switching framework.
  Quantitative Finance, 9(6):747–755, 2009.
* [12]

  Christian Francq and Jean-Michel Zakoïan.
  Multi-level conditional var estimation in dynamic models.
  In Modeling Dependence in Econometrics, pages 3–19. Springer,
  2014.
* [13]

  Michael B Gordy and Sandeep Juneja.
  Nested simulation in portfolio risk measurement.
  Management Science, 56(10):1833–1848, 2010.
* [14]

  Shanti S Gupta and S Panchapakesan.
  Sequential ranking and selection procedures.
  Handbook of sequential analysis, pages 363–380, 1991.
* [15]

  Lennart Hoogerheide and Herman K van Dijk.
  Bayesian forecasting of value at risk and expected shortfall using
  adaptive importance sampling.
  International Journal of Forecasting, 26(2):231–247, 2010.
* [16]

  Jochen Krause and Marc S Paolella.
  A fast, accurate method for value-at-risk and expected shortfall.
  Econometrics, 2(2):98–122, 2014.
* [17]

  Ming Liu and Jeremy Staum.
  Stochastic kriging for efficient nested simulation of expected
  shortfall.
  Journal of Risk, 12(3):3, 2010.
* [18]

  Kevin P Murphy.
  Conjugate bayesian analysis of the gaussian distribution.
  cs.ubc.ca/∼similar-to\simmurphyk/Papers/bayesGauss.pdf.
* [19]

  Saralees Nadarajah, Bo Zhang, and Stephen Chan.
  Estimation methods for expected shortfall.
  Quantitative Finance, 14(2):271–291, 2014.
* [20]

  Luis Ortiz-Gracia and Cornelis W Oosterlee.
  Efficient var and expected shortfall computations for nonlinear
  portfolios within the delta-gamma approach.
  Applied Mathematics and Computation, 244:16–31, 2014.
* [21]

  Franco Peracchi and Andrei V Tanase.
  On estimating the conditional expected shortfall.
  Applied Stochastic Models in Business and Industry,
  24(5):471–493, 2008.
* [22]

  Jimmy Risk and Michael Ludkovski.
  Sequential design and spatial modeling for portfolio tail risk
  measurement.
  SIAM Journal on Financial Mathematics, 9(4):1137–1174, 2018.
* [23]

  R Tyrrell Rockafellar and Stanislav Uryasev.
  Conditional value-at-risk for general loss distributions.
  Journal of banking & finance, 26(7):1443–1471, 2002.
* [24]

  Jules Sadefo Kamdem.
  Value-at-risk and expected shortfall for linear portfolios with
  elliptically distributed risk factors.
  International Journal of Theoretical and Applied Finance,
  8(05):537–551, 2005.
* [25]

  Jean-Guy Simonato.
  The performance of johnson distributions for computingvalue at risk
  and expected shortfall.
  The Journal of Derivatives, 19(1):7–24, 2011.
* [26]

  Keming Yu, A Allay, Shanchao Yang, and D Hand.
  Kernel quantile-based estimation of expected shortfall.
  2010.
* [27]

  Meng-Lan Yueh and Mark CW Wong.
  Analytical var and expected shortfall for quadratic portfolios.
  The Journal of Derivatives, 17(3):33–44, 2010.

## Appendix A Proxy of the optimal strategy for the heuristic ([21](#S2.E21 "In 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios"))

In the case p=1𝑝1p=1, ([21](#S2.E21 "In 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios")) can even be further simplified by using the upper-bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | h~01​(q1)≤max⁡{h~1​(q1);h~2​(q1)}subscriptsuperscript~ℎ10subscript𝑞1subscript~ℎ1subscript𝑞1subscript~ℎ2subscript𝑞1\displaystyle\tilde{h}^{1}\_{0}(q\_{1})\leq\max\{\tilde{h}\_{1}(q\_{1});\tilde{h}\_{2}(q\_{1})\} |  | (31) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | h~1​(q1)subscript~ℎ1subscript𝑞1\displaystyle\tilde{h}\_{1}(q\_{1}) | :=ns​(q1+1−nw)​δ0​exp⁡(−(K−q1​N2)​(q1+1−nw)​δ04​ns​c)assignabsentsubscript𝑛𝑠subscript𝑞11subscript𝑛𝑤subscript𝛿0𝐾subscript𝑞1subscript𝑁2subscript𝑞11subscript𝑛𝑤subscript𝛿04subscript𝑛𝑠𝑐\displaystyle:=n\_{s}\left(q\_{1}+1-n\_{w}\right)\delta\_{0}\exp\left(-\frac{\left(K-q\_{1}N\_{2}\right)(q\_{1}+1-n\_{w})\delta\_{0}}{4n\_{s}c}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | h~2​(q1)subscript~ℎ2subscript𝑞1\displaystyle\tilde{h}\_{2}(q\_{1}) | :=ns​(ns−nw)​δ0​exp⁡(−(K−q1​N2)​((q1+1−nw)​δ0)24​ns​σ¯2).assignabsentsubscript𝑛𝑠subscript𝑛𝑠subscript𝑛𝑤subscript𝛿0𝐾subscript𝑞1subscript𝑁2superscriptsubscript𝑞11subscript𝑛𝑤subscript𝛿024subscript𝑛𝑠superscript¯𝜎2\displaystyle:=n\_{s}\left(n\_{s}-n\_{w}\right)\delta\_{0}\exp\left(-\frac{\left(K-q\_{1}N\_{2}\right)((q\_{1}+1-n\_{w})\delta\_{0})^{2}}{4n\_{s}\overline{\sigma}^{2}}\right). |  |

The right-hand side of ([31](#A1.E31 "In Appendix A Proxy of the optimal strategy for the heuristic (21) ‣ Computation of Expected Shortfall by fast detection of worst scenarios")) is now tractable for minimization.
Given,

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Δ:=(K−(nw−1)​N2)2−32​ns​N2​cδ0B:=σ¯2c​δ0+nw−1q12,∗:=max⁡(nw−13+2​K3​N2,nw)q11,1,∗:=max⁡(3​(nw−1)4+K−Δ4​N2,nw)q11,2,∗:=max⁡(3​(nw−1)4+K+Δ4​N2,nw)casesassignΔsuperscript𝐾subscript𝑛𝑤1subscript𝑁2232subscript𝑛𝑠subscript𝑁2𝑐subscript𝛿0otherwiseassign𝐵superscript¯𝜎2𝑐subscript𝛿0subscript𝑛𝑤1otherwiseassignsuperscriptsubscript𝑞1  2subscript𝑛𝑤132𝐾3subscript𝑁2subscript𝑛𝑤otherwiseassignsuperscriptsubscript𝑞1  113subscript𝑛𝑤14𝐾Δ4subscript𝑁2subscript𝑛𝑤otherwiseassignsuperscriptsubscript𝑞1  123subscript𝑛𝑤14𝐾Δ4subscript𝑁2subscript𝑛𝑤otherwise\begin{cases}\Delta:=\left(K-\left(n\_{w}-1\right)N\_{2}\right)^{2}-\frac{32n\_{s}N\_{2}c}{\delta\_{0}}\\ B:=\frac{\bar{\sigma}^{2}}{c\delta\_{0}}+n\_{w}-1\\ q\_{1}^{2,\*}:=\max\left(\frac{n\_{w}-1}{3}+\frac{2K}{3N\_{2}},n\_{w}\right)\\ q\_{1}^{1,1,\*}:=\max\left(\frac{3\left(n\_{w}-1\right)}{4}+\frac{K-\sqrt{\Delta}}{4N\_{2}},n\_{w}\right)\\ q\_{1}^{1,2,\*}:=\max\left(\frac{3\left(n\_{w}-1\right)}{4}+\frac{K+\sqrt{\Delta}}{4N\_{2}},n\_{w}\right)\end{cases} |  | (32) |

the optimal policy q1hsubscriptsuperscript𝑞ℎ1q^{h}\_{1} is defined by the following table131313We optimize here over real positive numbers.:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Cond. on B𝐵B | Cond. ΔΔ\Delta | Cond. q12,∗superscriptsubscript𝑞1  2q\_{1}^{2,\*} | Cond. q11,1,∗superscriptsubscript𝑞1  11q\_{1}^{1,1,\*} | Cond. q11,2,∗superscriptsubscript𝑞1  12q\_{1}^{1,2,\*} | Choice of q1hsuperscriptsubscript𝑞1ℎq\_{1}^{h} |
| ≥nsabsentsubscript𝑛𝑠\geq n\_{s} |  |  |  |  | q1h:=q12,∗assignsuperscriptsubscript𝑞1ℎsuperscriptsubscript𝑞1  2q\_{1}^{h}:=q\_{1}^{2,\*} |
| ≤nwabsentsubscript𝑛𝑤\leq n\_{w} | >0absent0>0 |  |  |  | q1h:=argminq1∈{nw,q11,2,∗}​h01​(q1)assignsuperscriptsubscript𝑞1ℎsubscript𝑞1subscript𝑛𝑤superscriptsubscript𝑞1  12argminsuperscriptsubscriptℎ01subscript𝑞1q\_{1}^{h}:=\underset{q\_{1}\in\{n\_{w},q\_{1}^{1,2,\*}\}}{\textnormal{argmin}}h\_{0}^{1}(q\_{1}) |
| ≤nwabsentsubscript𝑛𝑤\leq n\_{w} | ≤0absent0\leq 0 |  |  |  | q1h:=nwassignsuperscriptsubscript𝑞1ℎsubscript𝑛𝑤q\_{1}^{h}:=n\_{w} |
| nw<⋅<nsn\_{w}<\cdot<n\_{s} | >0absent0>0 | ≤Babsent𝐵\leq B | ≤Babsent𝐵\leq B | ≤Babsent𝐵\leq B | q1h:=argminq1∈{q12,∗,B}​h01​(q1)assignsuperscriptsubscript𝑞1ℎsubscript𝑞1superscriptsubscript𝑞1  2𝐵argminsuperscriptsubscriptℎ01subscript𝑞1q\_{1}^{h}:=\underset{q\_{1}\in\{q\_{1}^{2,\*},B\}}{\textnormal{argmin}}h\_{0}^{1}(q\_{1}) |
| nw<⋅<nsn\_{w}<\cdot<n\_{s} | >0absent0>0 | ≤Babsent𝐵\leq B | ≤Babsent𝐵\leq B | ≥Babsent𝐵\geq B | q1h:=argminq1∈{q12,∗,q11,2,∗}​h01​(q1)assignsuperscriptsubscript𝑞1ℎsubscript𝑞1superscriptsubscript𝑞1  2superscriptsubscript𝑞1  12argminsuperscriptsubscriptℎ01subscript𝑞1q\_{1}^{h}:=\underset{q\_{1}\in\{q\_{1}^{2,\*},q\_{1}^{1,2,\*}\}}{\textnormal{argmin}}h\_{0}^{1}(q\_{1}) |
| nw<⋅<nsn\_{w}<\cdot<n\_{s} | >0absent0>0 | ≤Babsent𝐵\leq B | ≥Babsent𝐵\geq B | ≥Babsent𝐵\geq B | q1h:=argminq1∈{q12,∗,B,q11,2,∗}​h01​(q1)assignsuperscriptsubscript𝑞1ℎsubscript𝑞1superscriptsubscript𝑞1  2𝐵superscriptsubscript𝑞1  12argminsuperscriptsubscriptℎ01subscript𝑞1q\_{1}^{h}:=\underset{q\_{1}\in\{q\_{1}^{2,\*},B,q\_{1}^{1,2,\*}\}}{\textnormal{argmin}}h\_{0}^{1}(q\_{1}) |
| nw<⋅<nsn\_{w}<\cdot<n\_{s} | >0absent0>0 | ≥Babsent𝐵\geq B | ≤Babsent𝐵\leq B | ≤Babsent𝐵\leq B | q1h:=Bassignsuperscriptsubscript𝑞1ℎ𝐵q\_{1}^{h}:=B |
| nw<⋅<nsn\_{w}<\cdot<n\_{s} | >0absent0>0 | ≥Babsent𝐵\geq B |  | ≥Babsent𝐵\geq B | q1h:=argminq1∈{B,q11,2,∗}​h01​(q1)assignsuperscriptsubscript𝑞1ℎsubscript𝑞1𝐵superscriptsubscript𝑞1  12argminsuperscriptsubscriptℎ01subscript𝑞1q\_{1}^{h}:=\underset{q\_{1}\in\{B,q\_{1}^{1,2,\*}\}}{\textnormal{argmin}}h\_{0}^{1}(q\_{1}) |
| nw<⋅<nsn\_{w}<\cdot<n\_{s} | ≤0absent0\leq 0 | ≤Babsent𝐵\leq B |  |  | q1h:=argminq1∈{q12,∗,B}​h01​(q1)assignsuperscriptsubscript𝑞1ℎsubscript𝑞1superscriptsubscript𝑞1  2𝐵argminsuperscriptsubscriptℎ01subscript𝑞1q\_{1}^{h}:=\underset{q\_{1}\in\{q\_{1}^{2,\*},B\}}{\textnormal{argmin}}h\_{0}^{1}(q\_{1}) |
| nw<⋅<nsn\_{w}<\cdot<n\_{s} | ≤0absent0\leq 0 | ≥Babsent𝐵\geq B |  |  | q1h:=Bassignsuperscriptsubscript𝑞1ℎ𝐵q\_{1}^{h}:=B |

Table 5: Optimal q1hsuperscriptsubscript𝑞1ℎq\_{1}^{h} for h~01subscriptsuperscript~ℎ10\tilde{h}^{1}\_{0}.

For simplicity, let us consider the case c=0𝑐0c=0, see Remark [2.4](#S2.Thmtheorem4 "Remark 2.4. ‣ 2.3 Error bound for Sub-Gamma distributions ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios").

On Figure [19](#A1.F19 "Figure 19 ‣ Appendix A Proxy of the optimal strategy for the heuristic (21) ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), the square is q11,2,∗=52.41superscriptsubscript𝑞1

1252.41q\_{1}^{1,2,\*}=52.41, the circle is q12,∗=68.33superscriptsubscript𝑞1

268.33q\_{1}^{2,\*}=68.33 and the cross is the real optimum q1∗=71superscriptsubscript𝑞171q\_{1}^{\*}=71 of h01subscriptsuperscriptℎ10h^{1}\_{0}, for the parameters of Tables [1](#S2.T1 "Table 1 ‣ 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios") and [2](#S2.T2 "Table 2 ‣ 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios"). We see that we actually almost reach the correct minimum. It corresponds (up to rounding) to N11,∗=23723superscriptsubscript𝑁1

123723N\_{1}^{1,\*}=23723, N12,∗=17148superscriptsubscript𝑁1

217148N\_{1}^{2,\*}=17148, N1∗=15934superscriptsubscript𝑁115934N\_{1}^{\*}=15934.

![Refer to caption](/html/2005.12593/assets/S215A_compromise_between_q_and_N_mc_bare.png)


Figure 19: Square: h01​(q11,2,∗)superscriptsubscriptℎ01superscriptsubscript𝑞1

12h\_{0}^{1}(q\_{1}^{1,2,\*}). Circle: h01​(q12,∗)superscriptsubscriptℎ01superscriptsubscript𝑞1

2h\_{0}^{1}(q\_{1}^{2,\*}). Cross: h01​(q1∗)superscriptsubscriptℎ01superscriptsubscript𝑞1h\_{0}^{1}(q\_{1}^{\*}).

Using the same set of parameters, we plot on Figure [20](#A1.F20 "Figure 20 ‣ Appendix A Proxy of the optimal strategy for the heuristic (21) ‣ Computation of Expected Shortfall by fast detection of worst scenarios") the two functions h01superscriptsubscriptℎ01h\_{0}^{1} and h~1subscript~ℎ1\tilde{h}\_{1}. Although these two functions have values of different orders of magnitude, their shapes are quite close, which explains why we manage to obtain a relatively good approximation for the minimizer.

![Refer to caption](/html/2005.12593/assets/S215A_h_0_max_h_1_h_2_bias_bare.png)


Figure 20: Solid line : h01superscriptsubscriptℎ01h\_{0}^{1}. Dashed line : h~1subscript~ℎ1\tilde{h}\_{1}.

## Appendix B Precise implementation of the neural network algorithm

In this Appendix, we describe in more details how the neural network approximation of the optimal policy of the adaptative algorithm is constructed. All the parameters values are given in Tables [6](#A2.T6 "Table 6 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), [7](#A2.T7 "Table 7 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios") and [8](#A2.T8 "Table 8 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios") below.

### B.1 Initialization

* •

  In practice, the neural network input’s size depends on the window size q𝑞q. Therefore, we need to train different neural networks for each window size. In order to get enough points to train each of these neural networks, we have chosen the grid

  |  |  |  |
  | --- | --- | --- |
  |  | qg=[6,10,15,20,25,30,35,40,45,50,60,70,80,90,100,150,200,253]subscript𝑞𝑔 610152025303540455060708090100150200253q\_{g}=[6,10,15,20,25,30,35,40,45,50,60,70,80,90,100,150,200,253] |  |

  of possible values for q𝑞q.
* •

  We simulate independent copies {θ~j}j≤j​\_​bar={(μ~j,Σ~j)}j≤j​\_​barsubscriptsuperscript~𝜃𝑗𝑗j\_barsubscriptsuperscript~𝜇𝑗superscript~Σ𝑗𝑗j\_bar\{\tilde{\theta}^{j}\}\_{j\leq{\rm j\\_bar}}=\{(\tilde{\mu}^{j},\tilde{\Sigma}^{j})\}\_{j\leq{\rm j\\_bar}} of θ~~𝜃\tilde{\theta}, where j\_bar is given in Table [8](#A2.T8 "Table 8 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios"). For each 1≤j≤1𝑗absent1\leq j\leq j\_bar, Σ~jsuperscript~Σ𝑗\tilde{\Sigma}^{j} is an inverse-Wishart of parameters 𝚒0,Σ0
  subscript𝚒0subscriptΣ0{\mathtt{i}}\_{0},\Sigma\_{0}, and μ~jsuperscript~𝜇𝑗\tilde{\mu}^{j} is a Gaussian random vector of mean 𝚖0subscript𝚖0{\mathtt{m}}\_{0} and covariance matrix Σ~j/𝚔0superscript~Σ𝑗subscript𝚔0\tilde{\Sigma}^{j}/{\mathtt{k}}\_{0}. The parameters 𝚒0,𝚔0
  subscript𝚒0subscript𝚔0{\mathtt{i}}\_{0},{\mathtt{k}}\_{0} and Σ0subscriptΣ0\Sigma\_{0} are defined in Table [8](#A2.T8 "Table 8 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios") and ([30](#S4.E30 "In 4 Numerical Experiments ‣ Computation of Expected Shortfall by fast detection of worst scenarios")), while 𝚖0i=μisubscriptsuperscript𝚖𝑖0superscript𝜇𝑖{\mathtt{m}}^{i}\_{0}=\mu^{i}, i≤ns𝑖subscript𝑛𝑠i\leq n\_{s}, with the μisuperscript𝜇𝑖\mu^{i}’s of Figure [6](#S2.F6 "Figure 6 ‣ 2.5 Simplified 2-levels algorithm for a linear indifference zone’s size ‣ 2 Algorithm with a deterministic effort allocation ‣ Computation of Expected Shortfall by fast detection of worst scenarios").

### B.2 Strategy Generation

To generate the deterministic strategies (αk)k≤k​\_​barsubscriptsuperscript𝛼𝑘𝑘k\_bar(\alpha^{k})\_{k\leq{\rm k\\_bar}}, where k\_bar is given in Table [8](#A2.T8 "Table 8 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), we proceed as follows.

* •

  For each 1≤k≤1𝑘absent1\leq k\leqk\_bar, we simulate L+1𝐿1L+1 uniform random variables (Un)n=0Lsuperscriptsubscriptsubscript𝑈𝑛𝑛0𝐿\left(U\_{n}\right)\_{n=0}^{L} between 00 and 111. We sort them in increasing order (Us​(n))n=0Lsuperscriptsubscriptsubscript𝑈𝑠𝑛𝑛0𝐿\left(U\_{s(n)}\right)\_{n=0}^{L} and define a cost Kℓ:=K​(Us​(ℓ)−Us​(ℓ−1))assignsubscript𝐾ℓ𝐾subscript𝑈𝑠ℓsubscript𝑈𝑠ℓ1K\_{\ell}:=K(U\_{s(\ell)}-U\_{s(\ell-1)}) when 1≤ℓ≤L−11ℓ𝐿11\leq\ell\leq L-1, and KL=K​(Us​(0)+1−Us​(L−1))subscript𝐾𝐿𝐾subscript𝑈𝑠01subscript𝑈𝑠𝐿1K\_{L}=K(U\_{s(0)}+1-U\_{s(L-1)}). The idea is that we select L+1𝐿1L+1 points randomly on a cercle of total length K𝐾K: we choose one of these points, and starting from it, the computational power that we will use at each level 1≤ℓ≤L−11ℓ𝐿11\leq\ell\leq L-1 is the length of the arc between the previous and the next point. For the last step, we take K𝐾K times the length between the points L−1𝐿1L-1 and 00, so as to put, in average, twice more computational power on this last step.
* •

  Once we have the computational cost for each step, we can choose the qℓsubscript𝑞ℓq\_{\ell} for each strategy, so that we can deduce δ​Nℓ+1:=Kℓ/qℓassign𝛿subscript𝑁ℓ1subscript𝐾ℓsubscript𝑞ℓ\delta N\_{\ell+1}{:=K\_{\ell}/q\_{\ell}}. For ℓ=0ℓ0\ell=0, we choose q\_index0=18subscriptq\_index018\textnormal{q\\_index}\_{0}={18}, where 181818 is the number of terms in the grid qgsubscript𝑞𝑔q\_{g}, which therefore gives q0=qg​[q\_index0]=nssubscript𝑞0subscript𝑞𝑔delimited-[]subscriptq\_index0subscript𝑛𝑠q\_{0}=q\_{g}[\textnormal{q\\_index}\_{0}]=n\_{s}. For ℓ=L−1ℓ𝐿1\ell=L-1, we choose q\_indexL−1=0subscriptq\_index𝐿10\textnormal{q\\_index}\_{L-1}=0, that is, qL−1=nwsubscript𝑞𝐿1subscript𝑛𝑤q\_{L-1}=n\_{w}. For 1≤ℓ≤L−21ℓ𝐿21\leq\ell\leq L-2, we choose q\_indexℓsubscriptq\_indexℓ\textnormal{q\\_index}\_{\ell} as a random integer between [L−ℓ,q\_indexℓ−1−1]𝐿ℓsubscriptq\_indexℓ11[L-\ell,\textnormal{q\\_index}\_{\ell-1}-1]. The choice of qℓsubscript𝑞ℓq\_{\ell} is then qℓ=qg​[q\_indexℓ]subscript𝑞ℓsubscript𝑞𝑔delimited-[]subscriptq\_indexℓq\_{\ell}=q\_{g}[\textnormal{q\\_index}\_{\ell}]. We check that the sequence (Nℓ)1≤ℓ≤Lsubscriptsubscript𝑁ℓ1ℓ𝐿(N\_{\ell})\_{1\leq\ell\leq L} is non-decreasing. If this is the case, we keep it, if not, we reject it and do another run.

### B.3 Forward Pass

The next step is to generate all prices and execute for each k𝑘k and each j𝑗j the strategy k𝑘k.

* •

  For 1≤j≤j\_bar1𝑗j\_bar1\leq j\leq\textnormal{j\\_bar}, 1≤k≤k\_bar1𝑘k\_bar1\leq k\leq\textnormal{k\\_bar} and 1≤ℓ≤L1ℓ𝐿1\leq\ell\leq L, we simulate δ​Nℓk𝛿superscriptsubscript𝑁ℓ𝑘\delta N\_{\ell}^{k} Gaussian variables (Pj′j,1,…,Pj′j,ns)j′=Nℓ−1kNℓksuperscriptsubscriptsuperscriptsubscript𝑃superscript𝑗′
  𝑗1…superscriptsubscript𝑃superscript𝑗′
  𝑗subscript𝑛𝑠superscript𝑗′superscriptsubscript𝑁ℓ1𝑘superscriptsubscript𝑁ℓ𝑘\left(P\_{j^{\prime}}^{j,1},\ldots,P\_{j^{\prime}}^{j,n\_{s}}\right)\_{j^{\prime}=N\_{\ell-1}^{k}}^{N\_{\ell}^{k}} of mean μ~jsuperscript~𝜇𝑗\tilde{\mu}^{j} and covariance matrix Σ~jsuperscript~Σ𝑗\tilde{\Sigma}^{j} (independently across j𝑗j and k𝑘k).
* •

  We then update μ^ℓk,j,𝚖ℓk,j,𝚒ℓk,j,𝚔ℓk,j,Σℓk,j
  superscriptsubscript^𝜇ℓ
  𝑘𝑗superscriptsubscript𝚖ℓ
  𝑘𝑗superscriptsubscript𝚒ℓ
  𝑘𝑗superscriptsubscript𝚔ℓ
  𝑘𝑗superscriptsubscriptΣℓ
  𝑘𝑗\hat{\mu}\_{\ell}^{k,j},{\mathtt{m}}\_{\ell}^{k,j},{\mathtt{i}}\_{\ell}^{k,j},{\mathtt{k}}\_{\ell}^{k,j},\Sigma\_{\ell}^{k,j} accordingly, recall ([29](#S3.E29 "In Remark 3.7. ‣ 3.2 A generic progressive learning algorithm ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios")).
* •

  Updating Σℓk,jsuperscriptsubscriptΣℓ
  𝑘𝑗\Sigma\_{\ell}^{k,j} from level ℓ−1ℓ1\ell-1 to level ℓℓ\ell can use a lot of memory. Indeed, ∑j=Nℓα+1Nℓ+1α(𝒯ℓ+1α​(Pj)−δ​μ^ℓ+1α)​(𝒯ℓ+1α​(Pj)−δ​μ^ℓ+1α)⊤superscriptsubscript𝑗subscriptsuperscript𝑁𝛼ℓ1subscriptsuperscript𝑁𝛼ℓ1subscriptsuperscript𝒯𝛼ℓ1subscript𝑃𝑗𝛿subscriptsuperscript^𝜇𝛼ℓ1superscriptsubscriptsuperscript𝒯𝛼ℓ1subscript𝑃𝑗𝛿subscriptsuperscript^𝜇𝛼ℓ1top\sum\_{j=N^{\alpha}\_{\ell}+1}^{N^{\alpha}\_{\ell+1}}({\cal T}^{\alpha}\_{\ell+1}(P\_{j})-\delta\hat{\mu}^{\alpha}\_{\ell+1})({\cal T}^{\alpha}\_{\ell+1}(P\_{j})-\delta\hat{\mu}^{\alpha}\_{\ell+1})^{\top} consists in δ​Nℓ+1α×|qℓ+1|2𝛿superscriptsubscript𝑁ℓ1𝛼superscriptsubscript𝑞ℓ12\delta N\_{\ell+1}^{\alpha}\times|q\_{\ell+1}|^{2} terms, which can quickly exceed memory limits. Therefore, we do the sum with only N\_memory\_new\_pricings\_opt terms at a time, see Table [8](#A2.T8 "Table 8 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios") below.

### B.4 Computation of f\_precompute, running\_costs and admissible\_sets

* •

  In order to speed up the computation time, we now precompute several values that will be used many times afterwards. First, we compute f\_precompute(ℓ,k,j)ℓ𝑘𝑗(\ell,k,j) as f1ad​(ℓ,⋅)subscriptsuperscript𝑓ad1ℓ⋅f^{\rm ad}\_{1}(\ell,\cdot) at the point corresponding to (k,j)𝑘𝑗(k,j) except that, in the definition of f1ad​(ℓ,⋅)subscriptsuperscript𝑓ad1ℓ⋅f^{\rm ad}\_{1}(\ell,\cdot), we replace the random permutation 𝔪~~𝔪\tilde{\mathfrak{m}} by its estimation from the previous step, μ~~𝜇\tilde{\mu} by its average under the posterior distribution at ℓ+1ℓ1\ell+1, and σ~~𝜎\tilde{\sigma} by its estimation at step ℓ+1ℓ1\ell+1.
* •

  We compute running\_cost​(ℓ,k):=Cℓαkassignrunning\_costℓ𝑘subscriptsuperscript𝐶superscript𝛼𝑘ℓ\textnormal{running\\_cost}(\ell,k):=C^{\alpha^{k}}\_{\ell} of each k𝑘k at step ℓℓ\ell.
* •

  We restrict the set of possible actions at step ℓℓ\ell, given that we have followed the strategy k𝑘k so far, to admissible\_sets​(ℓ,k)admissible\_setsℓ𝑘\textnormal{admissible\\_sets}(\ell,k) defined as the collection of {(δqℓ+1k′,δNℓ+1k′)\{(\delta q\_{\ell+1}^{k^{\prime}},\delta N\_{\ell+1}^{k^{\prime}}), k′≤k\_bar}k^{\prime}\leq{\rm k\\_bar}\}, such that

  |  |  |  |
  | --- | --- | --- |
  |  | qℓk+δ​qℓ+1k′∈qg,Nℓ+1k′>Nℓk,running\_cost​(ℓ,k)+qℓk​δ​Nℓ+1k′≤max1≤k′′≤k¯​running\_cost​(ℓ+1,k′′).formulae-sequencesuperscriptsubscript𝑞ℓ𝑘𝛿superscriptsubscript𝑞ℓ1superscript𝑘′subscript𝑞𝑔formulae-sequencesuperscriptsubscript𝑁ℓ1superscript𝑘′superscriptsubscript𝑁ℓ𝑘running\_costℓ𝑘superscriptsubscript𝑞ℓ𝑘𝛿superscriptsubscript𝑁ℓ1superscript𝑘′1superscript𝑘′′¯𝑘running\_costℓ1superscript𝑘′′q\_{\ell}^{k}+\delta q\_{\ell+1}^{k^{\prime}}\in q\_{g},\;N\_{\ell+1}^{k^{\prime}}>N\_{\ell}^{k},\;\textnormal{running\\_cost}(\ell,k)+q\_{\ell}^{k}\delta N\_{\ell+1}^{k^{\prime}}\leq\underset{1\leq k^{\prime\prime}\leq\bar{k}}{\max}\textnormal{running\\_cost}(\ell+1,k^{\prime\prime}). |  |

  The last condition avoids inducing a strategy with a running cost that is not present in our data set, when doing the one step optimization.

### B.5 Computation of the final expectations

We first pre-compute the quantities

|  |  |  |
| --- | --- | --- |
|  | 𝔼LνLk,j​[|1nw​∑i∈ℑL−1k,j(μ^Lk,j)i−μ~i|]subscriptsuperscript𝔼subscriptsuperscript𝜈  𝑘𝑗𝐿𝐿delimited-[]1subscript𝑛𝑤subscript𝑖superscriptsubscriptℑ𝐿1  𝑘𝑗superscriptsuperscriptsubscript^𝜇𝐿  𝑘𝑗𝑖superscript~𝜇𝑖{\mathbb{E}}^{\nu^{k,j}\_{L}}\_{L}\left[\left|\frac{1}{n\_{w}}\sum\_{i\in{\mathfrak{I}}\_{L-1}^{k,j}}(\hat{\mu}\_{L}^{{k},j})^{i}-\tilde{\mu}^{i}\right|\right] |  |

by Monte Carlo using Nesubscript𝑁𝑒N\_{e} simulations. As the simulation of an inverse-Wishart random variable is significantly slower than the simulation of a Gaussian random variable, we only simulate 1 inverse-Wishart for Npsubscript𝑁𝑝N\_{p} Gaussians. The values of Nesubscript𝑁𝑒N\_{e} and Npsubscript𝑁𝑝N\_{p} are given by N\_mu\_tildes\_simulated and N\_wishart\_proportion of Table [8](#A2.T8 "Table 8 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios"). The estimation is called expectationLk,jsuperscriptsubscriptexpectation𝐿

𝑘𝑗\textnormal{expectation}\_{L}^{k,j}.

### B.6 Training of the neural network at level L𝐿L

* •

  We use a neural network with one inner layer with 256 neurons and 1 output layer with 1 neuron to fit (expectationLk,j)j≤j​\_​bar,k≤k​\_​barsubscriptsuperscriptsubscriptexpectation𝐿
  𝑘𝑗formulae-sequence𝑗j\_bar𝑘k\_bar(\textnormal{expectation}\_{L}^{k,j})\_{j\leq{\rm j\\_bar},k\leq{\rm k\\_bar}}. The neurons of the inner layer consist of the composition of the softplus function with an affine transformation of the inputs.
* •

  We initialize the neural network parameters using a Xavier initialization. We then train the neural network by selecting a random new batch every N\_batch\_change\_proportion. This random new batch is composed of the samples indexed by 1≤𝔪a​(j)≤j\_batch1subscript𝔪𝑎𝑗j\_batch1\leq{\mathfrak{m}}\_{a}(j)\leq\textnormal{j\\_batch} and strategies indexed by 1≤𝔪b​(k)≤k\_batch1subscript𝔪𝑏𝑘k\_batch1\leq{\mathfrak{m}}\_{b}(k)\leq\textnormal{k\\_batch}, where 𝔪asubscript𝔪𝑎{\mathfrak{m}}\_{a} and 𝔪bsubscript𝔪𝑏{\mathfrak{m}}\_{b} are uniform random permutations of [[1,j​\_​bar]]delimited-[]1j\_bar[\![1,{\rm j\\_bar}]\!] and [[1,k​\_​bar]]delimited-[]1k\_bar[\![1,{\rm k\\_bar}]\!]. For each batch, the algorithm used for the training is the standard gradient descent of Tensorflow. We do N\_Iter training steps in total. The learning rate used is given in Table [7](#A2.T7 "Table 7 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios"). In order to bring the input values of the parameters close to 00 and 111, we renormalize them according to the values in Table [6](#A2.T6 "Table 6 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios").

### B.7 Computation of the expectations at level L−1𝐿1L-1

We now estimate

|  |  |  |
| --- | --- | --- |
|  | 𝔼L−1νL−1k,j​[ϕˇL​(qLαk,NLαk,CLαk,μ^Lk,𝚙Lk)]subscriptsuperscript𝔼subscriptsuperscript𝜈  𝑘𝑗𝐿1𝐿1delimited-[]subscriptˇitalic-ϕ𝐿subscriptsuperscript𝑞superscript𝛼𝑘𝐿subscriptsuperscript𝑁superscript𝛼𝑘𝐿subscriptsuperscript𝐶superscript𝛼𝑘𝐿subscriptsuperscript^𝜇𝑘𝐿subscriptsuperscript𝚙𝑘𝐿{\mathbb{E}}^{\nu^{k,j}\_{L-1}}\_{L-1}\left[\check{\phi}\_{L}(q^{\alpha^{k}}\_{L},N^{\alpha^{k}}\_{L},C^{\alpha^{k}}\_{L},\hat{\mu}^{k}\_{L},\mathtt{p}^{k}\_{L})\right] |  |

where ϕˇLsubscriptˇitalic-ϕ𝐿\check{\phi}\_{L} is the fit of (expectationLk,j)j≤j​\_​bar,k≤k​\_​barsubscriptsuperscriptsubscriptexpectation𝐿

𝑘𝑗formulae-sequence𝑗j\_bar𝑘k\_bar(\textnormal{expectation}\_{L}^{k,j})\_{j\leq{\rm j\\_bar},k\leq{\rm k\\_bar}} from the previous step. The most cpu demanding part is no more the simulation of the inverse-Wisharts, but the updates of the parameters of the inverse-Wishart. Therefore, we simulate as many Gaussian random variables as inverse-Wishart random variables, with Nesubscript𝑁𝑒N\_{e} given by N\_mu\_tildes\_simulated\_non\_final\_level of Table [8](#A2.T8 "Table 8 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios").

For our computations, we need to update ΣL−1k,jsubscriptsuperscriptΣ

𝑘𝑗𝐿1\Sigma^{k,j}\_{L-1} to the corresponding posterior parameter according to ([29](#S3.E29 "In Remark 3.7. ‣ 3.2 A generic progressive learning algorithm ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios")). This can however lead to an enormous amount of multiplications and additions. Therefore, instead of updating the whole matrix, we only update the diagonal terms according to ([29](#S3.E29 "In Remark 3.7. ‣ 3.2 A generic progressive learning algorithm ‣ 3 Adaptative algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios")) and estimate non diagonal terms by keeping the correlation terms equal to the ones of ΣL−1k,jsubscriptsuperscriptΣ

𝑘𝑗𝐿1\Sigma^{k,j}\_{L-1}.
This enables us to approximately gain a factor of qLksuperscriptsubscript𝑞𝐿𝑘q\_{L}^{k} in speed in this critical step.

### B.8 Training of the neural network at level L−1𝐿1L-1

* •

  To fit the expectation of the previous step, we use a neural network with the same structure as in level L𝐿L, with the same cost function.
* •

  The initialization, choice of batches, and training of the neural network are the same as for the level L𝐿L. The number of iteration, learning rate, and renormalization constants are given in Tables [6](#A2.T6 "Table 6 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios"), [8](#A2.T8 "Table 8 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios") and [7](#A2.T7 "Table 7 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios").
* •

  We take j\_batch=min⁡(j\_batch\_size,j\_bar)j\_batchj\_batch\_sizej\_bar\textnormal{j\\_batch}=\min\left(\textnormal{j\\_batch\\_size},\textnormal{j\\_bar}\right) and k\_batch=min⁡(k\_batch\_size,k\_bar)k\_batchk\_batch\_sizek\_bar\textnormal{k\\_batch}=\min\left(\textnormal{k\\_batch\\_size},\textnormal{k\\_bar}\right), where j\_batch\_size and k\_batch\_size are defined in Table [8](#A2.T8 "Table 8 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios").

### B.9 Computation of the expectations at levels 0≤ℓ≤L−20ℓ𝐿20\leq\ell\leq L-2

* •

  The expectations at step ℓℓ\ell are computed by Monte Carlo after replacing the value function at step ℓ+1ℓ1\ell+1 by its neural network approximation, and f1ad​(ℓ,⋅)subscriptsuperscript𝑓ad1ℓ⋅f^{\rm ad}\_{1}(\ell,\cdot) by f\_precompute(ℓ,⋅)ℓ⋅(\ell,\cdot).
* •

  We simulate as many Gaussian random variables as inverse-Wishart random variables, with Nesubscript𝑁𝑒N\_{e} given by N\_mu\_tildes\_simulated\_non\_final\_level of Table [8](#A2.T8 "Table 8 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios").
* •

  We not not fully update Σℓk,jsubscriptsuperscriptΣ
  𝑘𝑗ℓ\Sigma^{k,j}\_{\ell} to the corresponding posterior parameter but proceed as in level L−1𝐿1L-1.

### B.10 Training of neural networks at levels 0≤ℓ≤L−20ℓ𝐿20\leq\ell\leq L-2

* •

  We now have to optimize over qℓk∈qgsuperscriptsubscript𝑞ℓ𝑘subscript𝑞𝑔q\_{\ell}^{k}\in q\_{g}. Therefore, we must now train up to |qg|subscript𝑞𝑔|q\_{g}| different neural networks (with different inputs’ sizes). In practice, we only train neural networks indexed by q∈(qℓk)1≤k≤k\_bar⊂qg𝑞subscriptsuperscriptsubscript𝑞ℓ𝑘1𝑘k\_barsubscript𝑞𝑔q\in(q\_{\ell}^{k})\_{1\leq k\leq\textnormal{k\\_bar}}\subset q\_{g}, that is, for all the choices of q𝑞q that are obtained by at least one strategy at level ℓℓ\ell.
* •

  We must also choose a δ​N𝛿𝑁\delta N that should be added as an entry of the neural network before optimizing. Furthermore, to help the neural networks converge, we decided to add f\_precompute​(ℓ,j,k)f\_precomputeℓ𝑗𝑘\textnormal{f\\_precompute}(\ell,j,k) as an input.
* •

  The loss function and the structure of the neural network is as above, and we still use Xavier initialization, and bring the inputs of the neural networks to reasonable values close to 0 and 1 by renormalizing them using the constants of Table [6](#A2.T6 "Table 6 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios").
* •

  Compared to levels L𝐿L and L−1𝐿1L-1, the choice of batches is slightly different. Indeed, to train a neural network associated to q∈qg𝑞subscript𝑞𝑔q\in q\_{g}, we only use strategies such that qℓk=qsuperscriptsubscript𝑞ℓ𝑘𝑞q\_{\ell}^{k}=q. To do so, we first define Sq={k∈[[1,k​\_​bar]]:qℓk=q}subscript𝑆𝑞conditional-set𝑘delimited-[]1k\_barsuperscriptsubscript𝑞ℓ𝑘𝑞S\_{q}=\{k\in[\![1,{\rm k\\_bar}]\!]:q\_{\ell}^{k}=q\}. We then define k\_batch=min⁡(k\_batch\_size,|Sq|)k\_batchk\_batch\_sizesubscript𝑆𝑞\textnormal{k\\_batch}=\min\left(\textnormal{k\\_batch\\_size},|S\_{q}|\right) and j\_batch=min⁡(j\_batch\_size,j​\_​bar)j\_batchj\_batch\_sizej\_bar\textnormal{j\\_batch}=\min\left(\textnormal{j\\_batch\\_size},{\rm j\\_bar}\right). We then proceed nearly identically as for levels L𝐿L and L−1𝐿1L-1. We select a new batch every N\_batch\_change\_proportion, composed of indices 1≤𝔪a​(j)≤j\_batch1subscript𝔪𝑎𝑗j\_batch1\leq{\mathfrak{m}}\_{a}(j)\leq\textnormal{j\\_batch}, 1≤𝔪b​(k)≤k\_batch1subscript𝔪𝑏𝑘k\_batch1\leq{\mathfrak{m}}\_{b}(k)\leq\textnormal{k\\_batch}, where 𝔪asubscript𝔪𝑎{\mathfrak{m}}\_{a} and 𝔪bsubscript𝔪𝑏{\mathfrak{m}}\_{b} are uniform random permutations of [[1,j​\_​bar]]delimited-[]1j\_bar[\![1,{\rm j\\_bar}]\!] and Sqsubscript𝑆𝑞S\_{q}. For each batch, the algorithm used for the training is again the standard gradient descent of Tensorflow.
* •

  Compared to levels L𝐿L and L−1𝐿1L-1, we found that making the neural networks converge was much harder. In particular, the learning rate had to be really fine tuned. In order to automatize the process, for each q𝑞q, we proceed as follows. We do not intanciate one, but
    
  number\_of\_neural\_networks\_for\_learning\_rate\_test neural networks. For each of these neural networks, we do N\_Iter\_learning\_rate\_test training steps, but use different learning rates for each. For the first neural network, we use base\_learning\_rate as the learning rate, for the second,
    
  base\_learning\_rate/10, and for the k𝑘k-th, base\_learning\_rate/10k−1base\_learning\_ratesuperscript10𝑘1\textnormal{base\\_learning\\_rate}/10^{k-1}. For each of these neural networks, we store at each iteration step the log error. Once the N\_Iter\_learning\_rate\_test training steps have been done for each of these neural networks, we keep the neural network instance that has the lowest average log error. If it is the k𝑘k-th neural network, we then train it again for N\_Iter training steps, using as learning rate base\_learning\_rate/10kbase\_learning\_ratesuperscript10𝑘\textnormal{base\\_learning\\_rate}/10^{k}.

### B.11 Parallelization

In practice, we parallelize the forward pass according to the strategy indices k𝑘k. We run thread\_batch\_size processes in parallel, where thread\_batch\_size is defined in Table [8](#A2.T8 "Table 8 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios").

At a given level ℓℓ\ell, the computation of expectationℓk,jsuperscriptsubscriptexpectationℓ

𝑘𝑗\textnormal{expectation}\_{\ell}^{k,j} can be parallelized according to the sample indices j𝑗j. In practice, we run number\_of\_threads\_for\_level\_expectations number of processes in parallel, where number\_of\_threads\_for\_level\_expectations is defined in Table [8](#A2.T8 "Table 8 ‣ B.12 Normalization constants, implementation parameters, and learning rates ‣ Appendix B Precise implementation of the neural network algorithm ‣ Computation of Expected Shortfall by fast detection of worst scenarios").

For a given level, the training of each neural network corresponding to a given q∈qg𝑞subscript𝑞𝑔q\in q\_{g} can be done independently. Therefore, at a given level, we multiprocessed our code in order to train all the neural networks in parallel.

### B.12 Normalization constants, implementation parameters, and learning rates

| Level | q | m | ΣΣ\Sigma | N | running\_cost | f\_precompute |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 6 | 106superscript10610^{6} | 1012superscript101210^{12} | 104superscript10410^{4} | 107superscript10710^{7} | 105superscript10510^{5} |
| 2 | 6 | 106superscript10610^{6} | 1012superscript101210^{12} | 104superscript10410^{4} | 107superscript10710^{7} | 105superscript10510^{5} |
| 3 | 6 | 106superscript10610^{6} | 1012superscript101210^{12} | 104superscript10410^{4} | 105superscript10510^{5} | 106superscript10610^{6} |
| 4 | 6 | 106superscript10610^{6} | 1011superscript101110^{11} | 104superscript10410^{4} | 105superscript10510^{5} | 106superscript10610^{6} |

Table 6: Inputs’ renormalization constants by Level



| Level | q | base\_learning\_rate | Level | q | base\_learning\_rate |
| --- | --- | --- | --- | --- | --- |
| 1 | 6 | 10−9superscript10910^{-9} | 2 | 6 | 10−9superscript10910^{-9} |
| 1 | 10 | 10−9superscript10910^{-9} | 2 | 10 | 10−9superscript10910^{-9} |
| 1 | 15 | 10−9superscript10910^{-9} | 2 | 15 | 10−9superscript10910^{-9} |
| 1 | 20 | 10−9superscript10910^{-9} | 2 | 20 | 10−9superscript10910^{-9} |
| 1 | 25 | 10−9superscript10910^{-9} | 2 | 25 | 10−9superscript10910^{-9} |
| 1 | 30 | 10−9superscript10910^{-9} | 2 | 30 | 10−9superscript10910^{-9} |
| 1 | 35 | 10−9superscript10910^{-9} | 2 | 35 | 10−9superscript10910^{-9} |
| 1 | 40 | 10−9superscript10910^{-9} | 2 | 40 | 10−9superscript10910^{-9} |
| 1 | 45 | 10−9superscript10910^{-9} | 2 | 45 | 10−9superscript10910^{-9} |
| 1 | 50 | 10−9superscript10910^{-9} | 2 | 50 | 10−9superscript10910^{-9} |
| 1 | 60 | 10−9superscript10910^{-9} | 2 | 60 | 10−9superscript10910^{-9} |
| 1 | 70 | 10−9superscript10910^{-9} | 2 | 70 | 10−9superscript10910^{-9} |
| 1 | 80 | 10−9superscript10910^{-9} | 2 | 80 | 10−9superscript10910^{-9} |
| 1 | 90 | 10−9superscript10910^{-9} | 2 | 90 | 10−9superscript10910^{-9} |
| 1 | 100 | 10−9superscript10910^{-9} | 2 | 100 | 10−9superscript10910^{-9} |
| 1 | 150 | 10−9superscript10910^{-9} | 2 | 150 | 10−9superscript10910^{-9} |
| 1 | 200 | 10−10superscript101010^{-10} | 2 | 200 | 10−10superscript101010^{-10} |
| 1 | 253 | 10−10superscript101010^{-10} | 2 | 253 | 10−10superscript101010^{-10} |
| 3 | 6 | 10−7superscript10710^{-7} | 4 | 6 | 10−7superscript10710^{-7} |

Table 7: Neural network base learning rates

|  |  |
| --- | --- |
| Parameter | Value |
| j\_batch\_size | 4 |
| k\_batch\_size | 4 |
| N\_batch\_change\_proportion | 1 000 |
| N\_iter\_show\_proportion | 100 |
| smaller\_learning\_rate\_proportion | 10 |
| N\_Iter\_smaller\_learning\_rate | 10 000 |
| L | 4 |
| n\_s | 253 |
| n\_w | 6 |
| k\_bar | 200 |
| j\_bar | 40 |
| i\_0 | 300 |
| k\_0 | 300 |
| Σ0subscriptΣ0\Sigma\_{0} | (300−253−1)​Σ3002531Σ(300-253-1)\Sigma |
| N\_wishart\_proportion | 1 000 |
| N\_mu\_tildes\_simulated | 1 000 000 |
| thread\_batch\_size | 4 |
| number\_of\_threads\_for\_level\_expectations | 4 |
| thread\_batch\_size\_for\_level\_expectations | 4 |
| p | 1 |
| r | 2 |
| c | 0 |
| N\_Iter | 1 000 000 |
| N\_Iter\_learning\_rate\_test | 100 000 |
| number\_of\_neural\_networks\_for\_learning\_rate\_test | 4 |
| K | 10 000 000 |
| N\_mu\_tildes\_simulated\_non\_final\_level | 1 000 |
| N\_memory\_new\_pricings\_opt | 100 |

Table 8: Implementation parameters

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/2005.12593)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2005.12593)
[View original  
on arXiv](https://arxiv.org/abs/2005.12593)[►](javascript: void(0))