---
authors:
- Imanol Perez Arribas
- Cristopher Salvi
- Lukasz Szpruch
doc_id: arxiv:2006.00218v2
family_id: arxiv:2006.00218
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[2006.00218] Sig-SDEs model for quantitative finance.'
url_abs: http://arxiv.org/abs/2006.00218v2
url_html: https://ar5iv.org/html/2006.00218v2
venue: arXiv q-fin
version: 2
year: 2020
---


Imanol Perez Arribas
[imanol.perez@maths.ox.ac.uk](mailto:imanol.perez@maths.ox.ac.uk)
University of OxfordAlan Turing InstituteUnited Kingdom
, 
Cristopher Salvi
[cristopher.salvi@maths.ox.ac.uk](mailto:cristopher.salvi@maths.ox.ac.uk)
University of OxfordAlan Turing InstituteUnited Kingdom
 and 
Lukasz Szpruch
[l.szpruch@ed.ac.uk](mailto:l.szpruch@ed.ac.uk)
University of EdinburghAlan Turing InstituteUnited Kingdom

(2018)

###### Abstract.

Mathematical models, calibrated to data, have become ubiquitous to make key decision processes in modern quantitative finance. In this work, we propose a novel framework for data-driven model selection by integrating a classical quantitative setup with a generative modelling approach. Leveraging the properties of the signature, a well-known path-transform from stochastic analysis that recently emerged as leading machine learning technology for learning time-series data, we develop the Sig-SDE model. Sig-SDE provides a new perspective on neural SDEs and can be calibrated to exotic financial products that depend, in a non-linear way, on the whole trajectory of asset prices. Furthermore, we our approach enables to consistently calibrate under the pricing measure ℚℚ\mathbb{Q} and real-world measure ℙℙ\mathbb{P}. Finally, we demonstrate the ability of Sig-SDE to simulate future possible market scenarios needed for computing risk profiles or hedging strategies. Importantly, this new model is underpinned by rigorous mathematical analysis, that under appropriate conditions provides theoretical guarantees for convergence of the presented algorithms.

market simulation, pricing, signatures, rough path theory

††copyright: acmcopyright††journalyear: 2018††doi: 10.1145/1122445.1122456††conference: 2020 ACM International Conference on AI in Finance; October 15–16, 2020; NY††booktitle: 2020 ACM International Conference on AI in Finance,
October 15–16, 2020, NY††price: 15.00††isbn: 978-1-4503-XXXX-X/18/06††ccs: Mathematics of computing Probability and statistics††ccs: Applied computing††ccs: Computing methodologies Machine learning

## 1. Introduction

The question of finding a parsimonious model that well represents empirical data has been of paramount importance in quantitative finance. The modelling choice is dictated by the desire to fit and explain the available data, but is also subject to computational considerations. Inevitably, all models can only provide an approximation to reality, and the risk of using inadequate ones is hard to detect.
A classical approach consists in fixing a class of parametric models, with a number of parameters that is significantly smaller than the number of available data points. Next, in the process called calibration, the goal is to solve a data-dependent optimization problem yielding an optimal choice of model parameters. The main challenge, of course, is to decide what class of models one should choose from. The theory of statistical learning (Vapnik, [2013](#bib.bib29)) tell us that to simple models cannot fit the data, and to complex one are not expected to generalise to unseen observations. In modern machine learning approaches, one usually starts by defining a highly oveparametrised model from some universality class, exhibiting a number of parameters often exceeding the number of data points, and let (stochastic) gradient algorithms find the best configuration of parameters yielding a calibrated model. In this work, we find a middle ground between the two approaches. We develop a new framework for systematic model selection that exhibits universal approximation properties, and we provide a explicit solution to the optimization used in its calibration, that completely removes the need to deploy expensive gradient descent algorithms. Importantly the class of models that we consider builds upon classical risk models that are well underpinned by research on quantitative finance.

The mathematical object at the core of this work is the expected signature of a path, whose properties are well-understood in the field of stochastic analysis. It allows to identify a linear structure underpinning the high non-linearity of the sequential data we work with. This linear structure leads to a massive speed-up of calibration, pricing, and generation of future scenarios. Our approach provides a new systematic model selection mechanism, that can also be deployed to calibrate classical non-Markovian models in a computationally efficient way. Signatures have been deployed to solve various tasks in mathematical finance, such as options pricing and hedging (Lyons
et al., [2019](#bib.bib23), [2020](#bib.bib24)), high frequency optimal execution (Kalsi
et al., [2020](#bib.bib15); Cartea et al., [2020](#bib.bib5)) and others (Lyons
et al., [2014](#bib.bib25); Gyurkó et al., [2013](#bib.bib13)). They have also been applied in several areas of machine learning (Kidger et al., [2019](#bib.bib17); Yang
et al., [2015](#bib.bib31), [2016a](#bib.bib32), [2016c](#bib.bib34), [2016b](#bib.bib33), [2017](#bib.bib35); Xie
et al., [2017](#bib.bib30); Li et al., [2017](#bib.bib22); Chevyrev and
Oberhauser, [2018](#bib.bib7); Király and
Oberhauser, [2016](#bib.bib20)).

### 1.1. Sig-SDE Model

Let X:[0,T]→ℝd:𝑋→0𝑇superscriptℝ𝑑X:[0,T]\to\mathbb{R}^{d} denote the price process of an arbitrary financial asset under the pricing measure ℚℚ\mathbb{Q}. To ensure the no-arbitrage assumption is not violated, X𝑋X typically is given by the solution of the following Stochastic Differential Equation (SDE)

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | d​Xt=Σt​d​Wt,X0=x,formulae-sequence𝑑subscript𝑋𝑡subscriptΣ𝑡𝑑subscript𝑊𝑡subscript𝑋0𝑥dX\_{t}=\Sigma\_{t}dW\_{t},\quad X\_{0}=x\,, |  |

where W𝑊W is a one-dimensional Brownian motion and ΣtsubscriptΣ𝑡\Sigma\_{t} is an adapted process (the volatility process). Model ([1](#S1.E1 "In 1.1. Sig-SDE Model ‣ 1. Introduction ‣ Sig-SDEs model for quantitative finance.")) accommodates many standard risk models used e.g: the classical Black–Scholes model assumes that volatility is proportional to the spot price, i.e. Σt:=σ​XtassignsubscriptΣ𝑡𝜎subscript𝑋𝑡\Sigma\_{t}:=\sigma X\_{t} with σ∈ℝ𝜎ℝ\sigma\in\mathbb{R} constant; the local volatility model assumes that Σt:=σ​(t,Xt)​XtassignsubscriptΣ𝑡𝜎𝑡subscript𝑋𝑡subscript𝑋𝑡\Sigma\_{t}:=\sigma(t,X\_{t})X\_{t}, where σ​(⋅,⋅)𝜎⋅⋅\sigma(\cdot,\cdot) (called local volatility surface) depends on both time and spot. Hence, it is a generalisation of the Black–Scholes model;
various stochastic volatility model assume that Σt:=σt​XtassignsubscriptΣ𝑡subscript𝜎𝑡subscript𝑋𝑡\Sigma\_{t}:=\sigma\_{t}X\_{t} with σt2superscriptsubscript𝜎𝑡2\sigma\_{t}^{2} following some diffusion process;
the SABR model chooses Σt:=σt​XtβassignsubscriptΣ𝑡subscript𝜎𝑡superscriptsubscript𝑋𝑡𝛽\Sigma\_{t}:=\sigma\_{t}X\_{t}^{\beta}, with β∈[0,1]𝛽01\beta\in[0,1] and where σtsubscript𝜎𝑡\sigma\_{t} follows a diffusion process.

A natural question would be whether one can find a model for the volatility process ΣtsubscriptΣ𝑡\Sigma\_{t} that is large enough to include all the classical models such as the ones mentioned above and that would allow for systematic a data driven model selection. We will require such a model to satisfy the following requirements:

1. (1)

   Universality. The model should be able to approximate arbitrarily well the dynamics of classical models.
2. (2)

   Efficient calibration. Given market prices for a family of options, it should be possible to efficiently calibrate the model so that it correctly prices the family of options.
3. (3)

   Fast pricing. Ideally, it should be possible to quickly price (potentially exotic) options under the model without using Monte Carlo techniques.
4. (4)

   Efficient simulation. Sampling trajectories from the model should be computationally cheap and efficient.

An example of a model that satisfies point 1. above is a neural network model, where the volatility process ΣtsubscriptΣ𝑡\Sigma\_{t} is approximated by a neural network 𝒩​𝒩θ​(t,(Ws)s∈[0,t])𝒩superscript𝒩𝜃𝑡subscriptsubscript𝑊𝑠𝑠0𝑡\mathcal{NN}^{\theta}(t,(W\_{s})\_{s\in[0,t]}) with parameters θ𝜃\theta. Such a model would be able to approximate a rich class of classical models. However, the calibration and pricing of such models would involve performing multiple Monte Carlo simulations on each epoch, which might be expensive if done naively. See however, (Cuchiero
et al., [2020](#bib.bib8); Gierjatowicz P., [2020](#bib.bib11)).

The aim of this paper is to propose a model for asset price dynamics that, we believe, satisfies all four points above. Our technique models the volatility process ΣtsubscriptΣ𝑡\Sigma\_{t} as

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | Σt=⟨ℓN,𝕎^0,t⟩subscriptΣ𝑡  superscriptℓ𝑁subscript^𝕎  0𝑡\Sigma\_{t}=\langle\ell^{N},\widehat{\mathbb{W}}\_{0,t}\rangle |  |

where ℓNsuperscriptℓ𝑁\ell^{N} is the model parameters and 𝕎^0,tsubscript^𝕎

0𝑡\widehat{\mathbb{W}}\_{0,t} is the signature (c.f definition [2.6](#S2.Thmtheorem6 "Definition 2.6 (Signature). ‣ 2.3. Signatures ‣ 2. Notation and preliminaries ‣ Sig-SDEs model for quantitative finance.")) of the stochastic process W^t:=(t,Wt)assignsubscript^𝑊𝑡𝑡subscript𝑊𝑡\widehat{W}\_{t}:=(t,W\_{t}). The motivation for choosing the signature as the main building block of this paper is anchored in a very powerful result for universal approximation of functions based on the celebrated Stone-Weierstrass Theorem that we present next in an informal manner (for more technical details see (Fermanian, [2019](#bib.bib9), Proposition 3))

###### Theorem 1.1.

Consider a compact set K𝐾K of continuous ℝdsuperscriptℝ𝑑\mathbb{R}^{d}-valued paths. Denote by S𝑆S the function that maps a path X𝑋X from K𝐾K to its signature 𝕏𝕏\mathbb{X}. Let f:K→ℝ:𝑓→𝐾ℝf:K\to\mathbb{R} be any any continuous functions. Then, for any ϵ>0italic-ϵ0\epsilon>0 and any path X∈K𝑋𝐾X\in K, there exists a linear function l∞superscript𝑙l^{\infty} acting on the signature such that

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | ‖f​(X)−⟨l∞,𝕏⟩‖∞<ϵsubscriptnorm𝑓𝑋  superscript𝑙𝕏italic-ϵ||f(X)-\langle l^{\infty},\mathbb{X}\rangle||\_{\infty}<\epsilon |  |

In other words, any continuous function on a compact set of paths can be uniformly well approximated by a linear combination of terms of the signature. This universal approximation property is similar to the one provided by Neural Networks (NN). However, as we will discuss below, NN models depend on a very large collection of parameters that need to be optimized via expensive back-propagation-based techniques, whilst the optimization needed in our Sig-SDE model consists of a simple linear regression on the terms of the signature. In this way, the signature can be thought of as a feature map for paths that provides a linear basis for the space of continuous functions on paths. In the setting of SDEs, sample paths are Brownian and solutions are images of these sample trajectories by a continuous functions that one wishes to approximate from a set of observations. Our Sig-SDE model will rely upon the universality of the signature to approximate such functions acting on Brownian trajectories. Importantly, the signature of a realisation of a semimartingale provides a unique representation of the sample trajectory (Hambly and Lyons, [2010](#bib.bib14); Boedihardjo et al., [2016](#bib.bib3)). Similarly, the expected signature – i.e. the collection of the expectations of the iterated integrals – provides a unique representation of the law of the semimartingale (Chevyrev
et al., [2016](#bib.bib6)).

Note that model calibration is an example of generative modelling (Goodfellow et al., [2014](#bib.bib12); Kingma and
Welling, [2013](#bib.bib19)).
Indeed, recall that if one knew prices of traded liquid derivatives, then one can approximate the pricing measure from market data (Breeden and
Litzenberger, [1978](#bib.bib4); Lyons
et al., [2019](#bib.bib23)). We denote this measure by ℚr​e​a​lsuperscriptℚ𝑟𝑒𝑎𝑙\mathbb{Q}^{real}.

We know that when equation ([1](#S1.E1 "In 1.1. Sig-SDE Model ‣ 1. Introduction ‣ Sig-SDEs model for quantitative finance.")) admits a strong solution then there exists a measurable map G:ℝ×C​([0,T])→C​([0,T]):𝐺→ℝ𝐶0𝑇𝐶0𝑇G:\mathbb{R}\times C([0,T])\rightarrow C([0,T]) such that

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | X=G​(x,(Ws)s∈[0,T])𝑋𝐺𝑥subscriptsubscript𝑊𝑠𝑠0𝑇X=G(x,(W\_{s})\_{s\in[0,T]}) |  |

as shown in (Karatzas and
Shreve, [2012](#bib.bib16), Corollary 3.23). If Gtsubscript𝐺𝑡G\_{t} denotes the projection of G𝐺G given by Xt:=Gt​(ξ,(Ws)s∈[0,t])assignsubscript𝑋𝑡subscript𝐺𝑡𝜉subscriptsubscript𝑊𝑠𝑠0𝑡X\_{t}:=G\_{t}(\xi,(W\_{s})\_{s\in[0,t]}), then one can view ([1](#S1.E1 "In 1.1. Sig-SDE Model ‣ 1. Introduction ‣ Sig-SDEs model for quantitative finance.")) as a generative model that maps μ0subscript𝜇0\mu\_{0} supported on ℝdsuperscriptℝ𝑑\mathbb{R}^{d} into (Gt)#​μ0=Qtθsubscriptsubscript𝐺𝑡#subscript𝜇0superscriptsubscript𝑄𝑡𝜃(G\_{t})\_{\#}\mu\_{0}=Q\_{t}^{\theta}. Note that by construction G𝐺G is a casual transport map i.e a transport map that is adapted to the filtration ℱtsubscriptℱ𝑡\mathcal{F}\_{t} (Acciaio et al., [2019](#bib.bib2)). In practice, one is interested in finding such a transport map from a family of parametrised functions Gθsuperscript𝐺𝜃G^{\theta}. One then looks for a θ𝜃\theta such that G#θ​μ0subscriptsuperscript𝐺𝜃#subscript𝜇0G^{\theta}\_{\#}\mu\_{0} is a good approximation of Qr​e​a​lsuperscript𝑄𝑟𝑒𝑎𝑙Q^{real} with respect to a metric specified by the user. In this paper the family of transport maps Gθsuperscript𝐺𝜃G^{\theta} is given by linear functions on signatures (or linear functionals below).

## 2. Notation and preliminaries

We begin by introducing some notation and preliminary results that are used in this paper.

### 2.1. Multi-indices

###### Definition 2.1.

Let d∈ℕ𝑑ℕd\in\mathbb{N}. For any n≥0𝑛0n\geq 0, we call an n𝑛n-dimensional d𝑑d-multi-index any n𝑛n-tuple of non-negative integers of the form K=(k1,…,kn)𝐾subscript𝑘1…subscript𝑘𝑛K=(k\_{1},\ldots,k\_{n}) such that ki∈{1,…,d}subscript𝑘𝑖1…𝑑k\_{i}\in\{1,\ldots,d\} for all i∈{1,…,n}𝑖1…𝑛i\in\{1,\ldots,n\}. We denote its length by |K|=n𝐾𝑛|K|=n. The empty multi-index is denoted by øitalic-ø\o. We denote by ℐdsubscriptℐ𝑑\mathcal{I}\_{d} the set of all d𝑑d-multi-indices, and by ℐdn⊂ℐdsubscriptsuperscriptℐ𝑛𝑑subscriptℐ𝑑\mathcal{I}^{n}\_{d}\subset\mathcal{I}\_{d} the set of all d𝑑d-multi-indices of length at most n∈ℕ𝑛ℕn\in\mathbb{N}.

###### Definition 2.2 (Concatenation of multi-indices).

Let I=(i1,…,ip)𝐼subscript𝑖1…subscript𝑖𝑝I=(i\_{1},\ldots,i\_{p}) and J=(j1,…,jq)𝐽subscript𝑗1…subscript𝑗𝑞J=(j\_{1},\ldots,j\_{q}) be any two multi-indices in ℐdsubscriptℐ𝑑\mathcal{I}\_{d}. Their concatenation product ⊗tensor-product\otimes as the multi-index I⊗J=(i1,…,im,j1,…,jn)∈ℐdtensor-product𝐼𝐽subscript𝑖1…subscript𝑖𝑚subscript𝑗1…subscript𝑗𝑛subscriptℐ𝑑I\otimes J=(i\_{1},\ldots,i\_{m},j\_{1},\ldots,j\_{n})\in\mathcal{I}\_{d}.

###### Example 2.3.

1. (1)

   (1,3)⊗(2,2)=(1,3,2,2)tensor-product13221322(1,3)\otimes(2,2)=(1,3,2,2).
2. (2)

   (2,1,3)⊗(1)=(2,1,3,1)tensor-product21312131(2,1,3)\otimes(1)=(2,1,3,1).
3. (3)

   (2,2)⊗ø=(2,2)tensor-product22italic-ø22(2,2)\otimes\o=(2,2).

### 2.2. Linear functionals

###### Definition 2.4 (Linear functional).

For a given d≥1𝑑1d\geq 1, a linear functional is a (possibly infinite) sequence of real numbers indexed by multi-indices in ℐdsubscriptℐ𝑑\mathcal{I}\_{d} of the following form

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | F={F(K)∈ℝ:K∈ℐd}.𝐹conditional-setsuperscript𝐹𝐾ℝ𝐾subscriptℐ𝑑F=\{F^{(K)}\in\mathbb{R}:K\in\mathcal{I}\_{d}\}. |  |

We note that a multi-index K∈ℐd𝐾subscriptℐ𝑑K\in\mathcal{I}\_{d} is always a linear functional. Both concatenation ⊗tensor-product\otimes and can be extended by linearity to operations on linear functionals. We will now define two basic operations on linear functionals that will be used throughout the paper.

###### Definition 2.5.

For any two linear functionals F,G

𝐹𝐺F,G and any real numbers α,β∈ℝ

𝛼𝛽
ℝ\alpha,\beta\in\mathbb{R} define

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | α​F+β​G={α​F(K)+β​G(K)∈ℝ:K∈ℐd}𝛼𝐹𝛽𝐺conditional-set𝛼superscript𝐹𝐾𝛽superscript𝐺𝐾ℝ𝐾subscriptℐ𝑑\alpha F+\beta G=\{\alpha F^{(K)}+\beta G^{(K)}\in\mathbb{R}:K\in\mathcal{I}\_{d}\} |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | ⟨F,G⟩=∑K∈ℐdF(K)​G(K)∈ℝ  𝐹𝐺 subscript𝐾subscriptℐ𝑑superscript𝐹𝐾superscript𝐺𝐾ℝ\langle F,G\rangle=\sum\_{K\in\mathcal{I}\_{d}}F^{(K)}G^{(K)}\in\mathbb{R} |  |

### 2.3. Signatures

Rough paths theory can be briefly described as a non-linear extension of the classical theory of controlled differential equations which is robust enough to allow a deterministic treatment of stochastic differential equations controlled by much rougher signals than semi-martingales (Lyons
et al., [2007](#bib.bib27)).

###### Definition 2.6 (Signature).

Let X:[0,T]→ℝd:𝑋→0𝑇superscriptℝ𝑑X:[0,T]\to\mathbb{R}^{d} be a continuous semimartingale. The Signature of X𝑋X over a time interval [s,t]⊂[0,T]𝑠𝑡0𝑇[s,t]\subset[0,T] is the linear functional 𝕏s,t:={𝕏s,t(K)∈ℝ:K∈ℐd}assignsubscript𝕏

𝑠𝑡conditional-setsuperscriptsubscript𝕏

𝑠𝑡𝐾ℝ𝐾subscriptℐ𝑑\mathbb{X}\_{s,t}:=\{\mathbb{X}\_{s,t}^{(K)}\in\mathbb{R}:K\in\mathcal{I}\_{d}\}, such that 𝕏s,t(ø)=1superscriptsubscript𝕏

𝑠𝑡italic-ø1\mathbb{X}\_{s,t}^{(\o)}=1 and so that for any n≥1𝑛1n\geq 1 and K=K^⊗a∈ℐdn𝐾tensor-product^𝐾𝑎subscriptsuperscriptℐ𝑛𝑑K=\widehat{K}\otimes a\in\mathcal{I}^{n}\_{d}, with a∈{1,…,d}𝑎1…𝑑a\in\{1,\ldots,d\} and K^∈ℐdn−1^𝐾subscriptsuperscriptℐ𝑛1𝑑\widehat{K}\in\mathcal{I}^{n-1}\_{d} we have

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | 𝕏s,t(K)=∫st𝕏s,u(K^)∘𝑑𝕏u(a)superscriptsubscript𝕏  𝑠𝑡𝐾superscriptsubscript𝑠𝑡subscriptsuperscript𝕏^𝐾  𝑠𝑢differential-dsubscriptsuperscript𝕏𝑎𝑢\mathbb{X}\_{s,t}^{(K)}=\int\_{s}^{t}\mathbb{X}^{(\widehat{K})}\_{s,u}\circ d\mathbb{X}^{(a)}\_{u} |  |

where the integral is to be interpreted in the Stratonovich sense.

###### Example 2.7.

Let X:[0,T]→ℝ2:𝑋→0𝑇superscriptℝ2X:[0,T]\to\mathbb{R}^{2} be a semimartingale.

1. (1)

   𝕏s,t(1)=Xt(1)−Xs(1)superscriptsubscript𝕏
   𝑠𝑡1superscriptsubscript𝑋𝑡1superscriptsubscript𝑋𝑠1\mathbb{X}\_{s,t}^{(1)}=X\_{t}^{(1)}-X\_{s}^{(1)}.
2. (2)

   𝕏s,t(1,2)=∫stXs,u(1)∘𝑑Xu(2)superscriptsubscript𝕏
   𝑠𝑡12superscriptsubscript𝑠𝑡superscriptsubscript𝑋
   𝑠𝑢1differential-dsuperscriptsubscript𝑋𝑢2\mathbb{X}\_{s,t}^{(1,2)}=\int\_{s}^{t}X\_{s,u}^{(1)}\circ dX\_{u}^{(2)}.
3. (3)

   𝕏s,t(2,2)=12​(Xs(2)−Xt(2))2superscriptsubscript𝕏
   𝑠𝑡2212superscriptsuperscriptsubscript𝑋𝑠2superscriptsubscript𝑋𝑡22\mathbb{X}\_{s,t}^{(2,2)}=\frac{1}{2}(X\_{s}^{(2)}-X\_{t}^{(2)})^{2}.

A more detailed overview of signatures is included in Appendix [A](#A1 "Appendix A Overview of signatures ‣ Sig-SDEs model for quantitative finance.").

## 3. Signature Model

In this section we define the Signature Model for asset price dynamics that we propose in this paper. The goal is to approximate the volatility process ΣtsubscriptΣ𝑡\Sigma\_{t} (that is a continuous function on the driving Brownian path) by a linear functional on the signature of the Brownian path.

###### Definition 3.1 (Signature Model).

Let W𝑊W be a one-dimensional Brownian motion. Let N∈ℕ𝑁ℕN\in\mathbb{N} be the order of the Signature Model. The Signature Model of parameter ℓ={ℓ(K):K∈ℐ2N}ℓconditional-setsuperscriptℓ𝐾𝐾subscriptsuperscriptℐ𝑁2\ell=\{\ell^{(K)}:K\in\mathcal{I}^{N}\_{2}\} is given by Σt:=⟨ℓ,𝕎^0,t⟩assignsubscriptΣ𝑡

ℓsubscript^𝕎

0𝑡\Sigma\_{t}:=\langle\ell,\widehat{\mathbb{W}}\_{0,t}\rangle, where 𝕎^^𝕎\widehat{\mathbb{W}} denotes the signature of Wadd-timesuperscript𝑊add-timeW^{\text{add-time}}. In other words, the asset price dynamics are given by

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | d​Xt=⟨ℓ,𝕎^0,t⟩​d​Wt,X0=x∈ℝ.formulae-sequence𝑑subscript𝑋𝑡  ℓsubscript^𝕎  0𝑡 𝑑subscript𝑊𝑡subscript𝑋0𝑥ℝdX\_{t}=\langle\ell,\widehat{\mathbb{W}}\_{0,t}\rangle dW\_{t},\quad X\_{0}=x\in\mathbb{R}. |  |

We note that the Signature Model has two components: the hyperparameter N∈ℕ𝑁ℕN\in\mathbb{N}, and the model parameter ℓℓ\ell. Intuitively, the hyperparameter N𝑁N plays a similar role to the width of a layer in a neural network. The larger this value is, the richer the range of market dynamics the Signature Models can generate. Once the value of N𝑁N is fixed, the challenge is to find a suitable model parameter ℓℓ\ell. Again, in analogy with neural networks, ℓℓ\ell plays the role of the weights of the network.

The Signature Model possesses the universality property, in the sense that given a classical model, there exists a Signature Model that can approximate its dynamics to a given accuracy (Levin
et al., [2013](#bib.bib21)).

We show in the upcoming Sections [5](#S5 "5. Simulation ‣ Sig-SDEs model for quantitative finance.")-[7](#S7 "7. Calibration ‣ Sig-SDEs model for quantitative finance.") that (a) the Signature Model is efficient to simulate, (b) it is efficient to calibrate, and (c) exotic options can be priced fast under the Signature Model.

###### Remark 1.

The Signature Model introduced in Definition [3.1](#S3.Thmtheorem1 "Definition 3.1 (Signature Model). ‣ 3. Signature Model ‣ Sig-SDEs model for quantitative finance.") assumes that the source of noise (i.e. the Brownian motion W𝑊W) is one-dimensional. This was done for simplicity, but the authors would like to emphasise that the model generalises in a straightforward way to multi-dimensional Brownian motion.

## 4. Numerical experiments

We now demonstrate the feasibility of our methodology as outlined in Sections [5](#S5 "5. Simulation ‣ Sig-SDEs model for quantitative finance.")-[7](#S7 "7. Calibration ‣ Sig-SDEs model for quantitative finance."). Throughout this section, we work with the Signature Model

|  |  |  |
| --- | --- | --- |
|  | d​Xt=⟨ℓ,𝕎^0,t⟩​d​Wt,X0=1formulae-sequence𝑑subscript𝑋𝑡  ℓsubscript^𝕎  0𝑡 𝑑subscript𝑊𝑡subscript𝑋01dX\_{t}=\langle\ell,\widehat{\mathbb{W}}\_{0,t}\rangle dW\_{t},\quad X\_{0}=1 |  |

with ℓ={ℓ(K):K∈ℐ2N}ℓconditional-setsuperscriptℓ𝐾𝐾superscriptsubscriptℐ2𝑁\ell=\{\ell^{(K)}:K\in\mathcal{I}\_{2}^{N}\}. We fix N=4𝑁4N=4. Therefore, the model has 1+2+22+23+24=3112superscript22superscript23superscript24311+2+2^{2}+2^{3}+2^{4}=31 parameters that need to be calibrated. We also fix the terminal maturity T=1𝑇1T=1.

In this section we will show experiments for the calibration of the model, pricing of options under the signature model and simulation. Sections [5](#S5 "5. Simulation ‣ Sig-SDEs model for quantitative finance.")-[7](#S7 "7. Calibration ‣ Sig-SDEs model for quantitative finance.") will then include the technical details of how calibration, pricing and simulation of signatures model are done.

### 4.1. Calibration

![Refer to caption](/html/2006.00218/assets/signature_model.png)

Figure 1. Error analysis between the option prices of the real model and the calibrated Signature Model.

\Description

Error analysis.

We assume that the family of options available on the market are a mixture of vanilla and exotic options, given as follows:

* •

  Vanilla call options with strikes K=0.5,0.6,…,1,1.𝐾
  0.50.6…11K=0.5,0.6,\ldots,1,1. and maturities t=0.4,0.45,0.5,…,0.9,0.95,1𝑡
  0.40.450.5…0.90.951t=0.4,0.45,0.5,\ldots,0.9,0.95,1:

  |  |  |  |
  | --- | --- | --- |
  |  | Φ:=max⁡(Xt−K,0).assignΦsubscript𝑋𝑡𝐾0\Phi:=\max(X\_{t}-K,0). |  |
* •

  Variance options with strikes K=0.01,0.015,…,0.035,0.04𝐾
  0.010.015…0.0350.04K=0.01,0.015,\ldots,0.035,0.04 and maturities t=0.4,0.45,0.5,…,0.9,0.95,1𝑡
  0.40.450.5…0.90.951t=0.4,0.45,0.5,\ldots,0.9,0.95,1:

  |  |  |  |
  | --- | --- | --- |
  |  | Φ:=max⁡(⟨X⟩t−K,0).assignΦsubscriptdelimited-⟨⟩𝑋𝑡𝐾0\Phi:=\max(\langle X\rangle\_{t}-K,0). |  |

  where ⟨X⟩delimited-⟨⟩𝑋\langle X\rangle is the quadratic variation of X𝑋X.
* •

  Down-and-Out barrier call options with maturity 1, strikes K=0.9,0.92,0.94,…,1.01,1.03𝐾
  0.90.920.94…1.011.03K=0.9,0.92,0.94,\ldots,1.01,1.03 and barrier levels L=0.6,0.62,0.64,…,0.88,0.9𝐿
  0.60.620.64…0.880.9L=0.6,0.62,0.64,\ldots,0.88,0.9:

  |  |  |  |
  | --- | --- | --- |
  |  | Φ:={max⁡(Xt−K,0)if ​mins∈[0,t]⁡Xs>L0else.assignΦcasessubscript𝑋𝑡𝐾0if subscript𝑠0𝑡subscript𝑋𝑠𝐿0else\Phi:=\begin{cases}\max(X\_{t}-K,0)&\mbox{if }\min\_{s\in[0,t]}X\_{s}>L\\ 0&\mbox{else}.\end{cases} |  |

The option prices are generated from a Black-Scholes model with volatility σ=0.2𝜎0.2\sigma=0.2:

|  |  |  |
| --- | --- | --- |
|  | d​Xt=σ​Xt​d​Wt.𝑑subscript𝑋𝑡𝜎subscript𝑋𝑡𝑑subscript𝑊𝑡dX\_{t}=\sigma X\_{t}dW\_{t}. |  |

The optimisation ([14](#S7.E14 "In 7. Calibration ‣ Sig-SDEs model for quantitative finance.")) was then solved to calibrate the model parameters ℓ={ℓ(K):K∈ℐ2N}ℓconditional-setsuperscriptℓ𝐾𝐾superscriptsubscriptℐ2𝑁\ell=\{\ell^{(K)}:K\in\mathcal{I}\_{2}^{N}\}.

Figure [1](#S4.F1 "Figure 1 ‣ 4.1. Calibration ‣ 4. Numerical experiments ‣ Sig-SDEs model for quantitative finance.") shows the absolute error between the real option prices and the option prices of the calibrated model, for the different option types.

### 4.2. Simulation

![Refer to caption](/html/2006.00218/assets/simulation.png)

Figure 2. 1,000 realisations of the calibrated Signature Model.

\Description

Simulation.

Once the Signature Model has been calibrated to the available option prices, we can use Algorithm [1](#algorithm1 "In 5. Simulation ‣ Sig-SDEs model for quantitative finance.") to simulate realisations of the calibrated Signature Model. Figure [2](#S4.F2 "Figure 2 ‣ 4.2. Simulation ‣ 4. Numerical experiments ‣ Sig-SDEs model for quantitative finance.") shows 1,000 realisations of the Signature Model.

### 4.3. Pricing

![Refer to caption](/html/2006.00218/assets/pricing.png)

Figure 3. Error analysis between the option prices of the real model and the calibrated Signature Model.

\Description

Error analysis.

We will now use the calibrated Signature Model to price a new set of options that was not used in the calibration step. This set of option consists of Down-and-In barrier put options with barriers levels L=0.7,0.71,…,0.81,0.82𝐿

0.70.71…0.810.82L=0.7,0.71,\ldots,0.81,0.82 and strikes K=0.9,0.92,…,1.01,1.03𝐾

0.90.92…1.011.03K=0.9,0.92,\ldots,1.01,1.03:

|  |  |  |
| --- | --- | --- |
|  | Φ:={max⁡(K−Xt,0)if ​mins∈[0,t]⁡Xs<L0else.assignΦcases𝐾subscript𝑋𝑡0if subscript𝑠0𝑡subscript𝑋𝑠𝐿0else\Phi:=\begin{cases}\max(K-X\_{t},0)&\mbox{if }\min\_{s\in[0,t]}X\_{s}<L\\ 0&\mbox{else}.\end{cases} |  |

Figure [3](#S4.F3 "Figure 3 ‣ 4.3. Pricing ‣ 4. Numerical experiments ‣ Sig-SDEs model for quantitative finance.") shows the absolute error of the prices under the Signature Model, compared to the real prices.

As we see, the calibrated model is able to generate accurate prices for these new exotic options. The error is highest when the barrier is close to the strike price, as expected.

## 5. Simulation

This section will address the question of simulation efficiency of Signature Models. We begin by stating the following two results. The first result rewrites the differential equation ([9](#S3.E9 "In Definition 3.1 (Signature Model). ‣ 3. Signature Model ‣ Sig-SDEs model for quantitative finance.")) solely in terms of the lead-lag signature of the Brownian motion, 𝕎^0,tL​Lsuperscriptsubscript^𝕎

0𝑡𝐿𝐿\mathbb{\widehat{W}}\_{0,t}^{LL}. Here 𝕎^L​Lsuperscript^𝕎𝐿𝐿\widehat{\mathbb{W}}^{LL} denotes the lead-lag transformation of W^^𝑊\widehat{W}, see Appendix [B](#A2 "Appendix B Time and Lead-lag transformation ‣ Sig-SDEs model for quantitative finance."). We use the lead-lag transformation because it allows us to rewrite Itô integrals as certain Stratonovich integrals, which in turn can be written as linear functions on signatures. The second result guarantees that the computational cost of computing 𝕎^0,tL​Lsuperscriptsubscript^𝕎

0𝑡𝐿𝐿\mathbb{\widehat{W}}\_{0,t}^{LL} is the same as the cost of computing {𝕎^0,sL​L; 0≤s≤t}

superscriptsubscript^𝕎

0𝑠𝐿𝐿 0
𝑠𝑡\{\mathbb{\widehat{W}}\_{0,s}^{LL}\;;\;0\leq s\leq t\}. These two results lead to Algorithm [1](#algorithm1 "In 5. Simulation ‣ Sig-SDEs model for quantitative finance."), which provides an efficient algorithm to sample from a Signature Model.

###### Proposition 5.1 ((Lyons et al., [2019](#bib.bib23), Lemma 3.11)).

Let X𝑋X follow a Signature Model with parameter ℓ={ℓ(K):K∈ℐ2N}ℓconditional-setsuperscriptℓ𝐾𝐾subscriptsuperscriptℐ𝑁2\ell=\{\ell^{(K)}:K\in\mathcal{I}^{N}\_{2}\}. Then, X𝑋X is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | Xt=⟨x​(ø)+ℓ⊗(4),𝕎^0,tL​L⟩subscript𝑋𝑡  𝑥italic-øtensor-productℓ4superscriptsubscript^𝕎  0𝑡𝐿𝐿X\_{t}=\langle x(\o)+\ell\otimes(4),\widehat{\mathbb{W}}\_{0,t}^{LL}\rangle |  |

where ℓ⊗(4)={K⊗(4):K∈ℓ}tensor-productℓ4conditional-settensor-product𝐾4𝐾ℓ\ell\otimes(4)=\{K\otimes(4):K\in\ell\}, x=X0∈ℝ𝑥subscript𝑋0ℝx=X\_{0}\in\mathbb{R}, and 𝕎^L​Lsuperscript^𝕎𝐿𝐿\widehat{\mathbb{W}}^{LL} denotes the lead-lag transformation, introduced in Definition [B.1](#A2.Thmtheorem1 "Definition B.1 (Lead-lag transformation). ‣ Appendix B Time and Lead-lag transformation ‣ Sig-SDEs model for quantitative finance."), of the 2-dimensional process W^=(t,Wt)^𝑊𝑡subscript𝑊𝑡\widehat{W}=(t,W\_{t}).

###### Theorem 5.2 (Chen’s identity, (Lyons, [1998](#bib.bib26), Theorem 2.12)).

Let 0≤s≤t0𝑠𝑡0\leq s\leq t. Then, for each multi-index K∈ℐd𝐾subscriptℐ𝑑K\in\mathcal{I}\_{d} we have

|  |  |  |  |
| --- | --- | --- | --- |
| (11) |  | 𝕎^0,tL​L,(K)=∑I,J∈ℐdI⊗J=K𝕎^0,tL​L,(I)⋅𝕎^0,tL​L,(J)superscriptsubscript^𝕎  0𝑡  𝐿𝐿𝐾subscript    𝐼𝐽 subscriptℐ𝑑tensor-product𝐼𝐽𝐾⋅superscriptsubscript^𝕎  0𝑡  𝐿𝐿𝐼superscriptsubscript^𝕎  0𝑡  𝐿𝐿𝐽\widehat{\mathbb{W}}\_{0,t}^{LL,(K)}=\sum\_{\begin{subarray}{c}I,J\in\mathcal{I}\_{d}\\ I\otimes J=K\end{subarray}}\widehat{\mathbb{W}}\_{0,t}^{LL,(I)}\cdot\widehat{\mathbb{W}}\_{0,t}^{LL,(J)} |  |

where for any multi-index K∈ℐd𝐾subscriptℐ𝑑K\in\mathcal{I}\_{d} we used the notation 𝕎^0,tL​L,(K)=⟨K,𝕎^0,tL​L⟩superscriptsubscript^𝕎

0𝑡

𝐿𝐿𝐾

𝐾superscriptsubscript^𝕎

0𝑡𝐿𝐿\widehat{\mathbb{W}}\_{0,t}^{LL,(K)}=\langle K,\widehat{\mathbb{W}}\_{0,t}^{LL}\rangle.

These two results lead to Algorithm [1](#algorithm1 "In 5. Simulation ‣ Sig-SDEs model for quantitative finance."). We note there are a number of publicly available software packages to compute signatures, such as esig 111<https://pypi.org/project/esig/>, iisignature 222<https://github.com/bottler/iisignature>, (Reizenstein and
Graham, [2020](#bib.bib28)) and signatory 333<https://github.com/patrick-kidger/signatory>, (Kidger and Lyons, [2020](#bib.bib18)).

Parameters : 
D={ti}i=1n𝐷superscriptsubscriptsubscript𝑡𝑖𝑖1𝑛D=\{t\_{i}\}\_{i=1}^{n} with 0=t0<t1<…<tn−1<tn=T0subscript𝑡0subscript𝑡1…subscript𝑡𝑛1subscript𝑡𝑛𝑇0=t\_{0}<t\_{1}<\ldots<t\_{n-1}<t\_{n}=T: sampling times.

ℓ={ℓ(K):K∈ℐ4N}ℓconditional-setsuperscriptℓ𝐾𝐾subscriptsuperscriptℐ𝑁4\ell=\{\ell^{(K)}:K\in\mathcal{I}^{N}\_{4}\}: Signature Model parameter.

x∈ℝ𝑥ℝx\in\mathbb{R}: initial spot price.

Output: A sample path {Xtk}k=0nsuperscriptsubscriptsubscript𝑋subscript𝑡𝑘𝑘0𝑛\{X\_{t\_{k}}\}\_{k=0}^{n} from the Signature Model.

1
Simulate a one-dimensional Brownian motion at the sampling times {Wti}i=0nsuperscriptsubscriptsubscript𝑊subscript𝑡𝑖𝑖0𝑛\{W\_{t\_{i}}\}\_{i=0}^{n}.

2
Apply the lead-lag transformation ([25](#A2.E25 "In Definition B.1 (Lead-lag transformation). ‣ Appendix B Time and Lead-lag transformation ‣ Sig-SDEs model for quantitative finance.")) to W^^𝑊\widehat{W} to obtain W^L​Lsuperscript^𝑊𝐿𝐿\widehat{W}^{LL}.

3
𝕎^0,0L​L←{F(K):K∈ℐ4N+1}←subscriptsuperscript^𝕎𝐿𝐿

00conditional-setsuperscript𝐹𝐾𝐾superscriptsubscriptℐ4𝑁1\widehat{\mathbb{W}}^{LL}\_{0,0}\leftarrow\{F^{(K)}:K\in\mathcal{I}\_{4}^{N+1}\} with F(ø)=1superscript𝐹italic-ø1F^{(\o)}=1 and F(K)=0superscript𝐹𝐾0F^{(K)}=0 for K≠ø𝐾italic-øK\neq\o.

4
X0←x←subscript𝑋0𝑥X\_{0}\leftarrow x.

5
for *k=1,…,n𝑘

1…𝑛k=1,\ldots,n* do

6      
Compute the signature 𝕎^tk−1,tkL​L={𝕎^tk−1,tkL​L,(K):K∈ℐ4N+1}subscriptsuperscript^𝕎𝐿𝐿

subscript𝑡𝑘1subscript𝑡𝑘conditional-setsuperscriptsubscript^𝕎

subscript𝑡𝑘1subscript𝑡𝑘

𝐿𝐿𝐾𝐾superscriptsubscriptℐ4𝑁1\widehat{\mathbb{W}}^{LL}\_{t\_{k-1},t\_{k}}=\{\widehat{\mathbb{W}}\_{t\_{k-1},t\_{k}}^{LL,(K)}:K\in\mathcal{I}\_{4}^{N+1}\}.

7      
Use Chen’s identity (Theorem [5.2](#S5.Thmtheorem2 "Theorem 5.2 (Chen’s identity, (Lyons, 1998, Theorem 2.12)). ‣ 5. Simulation ‣ Sig-SDEs model for quantitative finance.")) to compute the signature 𝕎^0,tkL​L←{𝕎^0,tkL​L,K:K∈ℐ4N+1}←subscriptsuperscript^𝕎𝐿𝐿

0subscript𝑡𝑘conditional-setsuperscriptsubscript^𝕎

0subscript𝑡𝑘

𝐿𝐿𝐾𝐾superscriptsubscriptℐ4𝑁1\widehat{\mathbb{W}}^{LL}\_{0,t\_{k}}\leftarrow\{\widehat{\mathbb{W}}\_{0,t\_{k}}^{LL,K}:K\in\mathcal{I}\_{4}^{N+1}\}

8      
Use proposition [5.1](#S5.Thmtheorem1 "Proposition 5.1 ((Lyons et al., 2019, Lemma 3.11)). ‣ 5. Simulation ‣ Sig-SDEs model for quantitative finance.") to get Xtk←⟨x​(ø)+ℓ⊗(4),𝕎^0,tkL​L⟩←subscript𝑋subscript𝑡𝑘

𝑥italic-øtensor-productℓ4superscriptsubscript^𝕎

0subscript𝑡𝑘𝐿𝐿X\_{t\_{k}}\leftarrow\langle x(\o)+\ell\otimes(4),\widehat{\mathbb{W}}\_{0,t\_{k}}^{LL}\rangle.

9 end for

return *{Xtk}k=0nsuperscriptsubscriptsubscript𝑋subscript𝑡𝑘𝑘0𝑛\{X\_{t\_{k}}\}\_{k=0}^{n}.*

Algorithm 1 Sampling from a Signature Model.

## 6. Pricing

This section will show that exotic options can be priced fast under a Signature Model. This will be done via a two step procedure. First, it was shown in (Lyons
et al., [2019](#bib.bib23), [2020](#bib.bib24)) that prices of exotic options can be approximated with arbitrary precision by a special class of payoffs called signature payoffs, defined below. Hence, we will assume that the exotic option to be priced is a signature payoff, defined as follows.

###### Definition 6.1 (Signature payoffs).

A signature payoff of maturity T>0𝑇0T>0 and parameter f={f(K):K∈ℐ3N}𝑓conditional-setsuperscript𝑓𝐾𝐾subscriptsuperscriptℐ𝑁3f=\{f^{(K)}:K\in\mathcal{I}^{N}\_{3}\} is a payoff that pays at time T𝑇T an amount given by ⟨f,𝕏^0,T⟩

𝑓subscript^𝕏

0𝑇\langle f,\mathbb{\widehat{X}}\_{0,T}\rangle.

Second, the price of a signature payoff is ⟨f,𝔼​[𝕏^0,T]⟩

𝑓𝔼delimited-[]subscript^𝕏

0𝑇\langle f,\mathbb{E}[\mathbb{\widehat{X}}\_{0,T}]\rangle. To price a signature payoff, all we need is 𝔼​[[]​𝕏^0,T]𝔼delimited-[]


subscript^𝕏

0𝑇\mathbb{E}\left[[\right]\mathbb{\widehat{X}}\_{0,T}], which doesn’t depend on the signature payoff itself. In particular, it may be reused to price other signature payoffs.

We now explicitly derive the expected signature 𝔼​[[]​𝕏^0,T]𝔼delimited-[]


subscript^𝕏

0𝑇\mathbb{E}\left[[\right]\mathbb{\widehat{X}}\_{0,T}] in terms of the model parameters and the expected signature of the lead-lag Brownian motion 𝔼​[[]​𝕎^0,TL​L]𝔼delimited-[]


subscriptsuperscript^𝕎𝐿𝐿

0𝑇\mathbb{E}\left[[\right]\mathbb{\widehat{W}}^{LL}\_{0,T}].

###### Proposition 6.2.

Let X𝑋X be a Signature Model of order N∈ℕ𝑁ℕN\in\mathbb{N} with parameter ℓ={ℓ(K):K∈ℐ2N}ℓconditional-setsuperscriptℓ𝐾𝐾subscriptsuperscriptℐ𝑁2\ell=\{\ell^{(K)}:K\in\mathcal{I}^{N}\_{2}\}. Consider the following linear functionals P1=(1)subscript𝑃11P\_{1}=(1) and P2=ℓ⊗(4)subscript𝑃2tensor-productℓ4P\_{2}=\ell\otimes(4). Consider any multi-index I=(i1,…,in)∈ℐ2n𝐼subscript𝑖1…subscript𝑖𝑛superscriptsubscriptℐ2𝑛I=(i\_{1},\ldots,i\_{n})\in\mathcal{I}\_{2}^{n} such that n≤N𝑛𝑁n\leq N. Then

|  |  |  |  |
| --- | --- | --- | --- |
| (12) |  | 𝕏s,t(I)=⟨CI​(ℓ),𝕎^s,tL​L⟩superscriptsubscript𝕏  𝑠𝑡𝐼  subscript𝐶𝐼ℓsuperscriptsubscript^𝕎  𝑠𝑡𝐿𝐿\mathbb{X}\_{s,t}^{(I)}=\langle C\_{I}(\ell),\widehat{\mathbb{W}}\_{s,t}^{LL}\rangle |  |

where CI​(ℓ)subscript𝐶𝐼ℓC\_{I}(\ell) is given explicitly in closed-form by

|  |  |  |  |
| --- | --- | --- | --- |
| (13) |  | CI​(ℓ)=(…​((Pi1≻Pi2)≻Pi3)≻…≻Pin)subscript𝐶𝐼ℓsucceeds…succeedssucceedssubscript𝑃subscript𝑖1subscript𝑃subscript𝑖2subscript𝑃subscript𝑖3…succeedssubscript𝑃subscript𝑖𝑛C\_{I}(\ell)=(\ldots((P\_{i\_{1}}\succ P\_{i\_{2}})\succ P\_{i\_{3}})\succ\ldots\succ P\_{i\_{n}}) |  |

###### Proof.

By Proposition [5.1](#S5.Thmtheorem1 "Proposition 5.1 ((Lyons et al., 2019, Lemma 3.11)). ‣ 5. Simulation ‣ Sig-SDEs model for quantitative finance.") we know that if X𝑋X follows a Signature Model with parameter ℓ={ℓ(K):K∈ℐ2N}ℓconditional-setsuperscriptℓ𝐾𝐾subscriptsuperscriptℐ𝑁2\ell=\{\ell^{(K)}:K\in\mathcal{I}^{N}\_{2}\} then

|  |  |  |
| --- | --- | --- |
|  | Xt=⟨x​(ø)+ℓ⊗(4),𝕎^0,tL​L⟩subscript𝑋𝑡  𝑥italic-øtensor-productℓ4superscriptsubscript^𝕎  0𝑡𝐿𝐿X\_{t}=\langle x(\o)+\ell\otimes(4),\widehat{\mathbb{W}}\_{0,t}^{LL}\rangle |  |

Let I=(i1,…,in)𝐼subscript𝑖1…subscript𝑖𝑛I=(i\_{1},\ldots,i\_{n}) be any multi-index in ℐ2nsuperscriptsubscriptℐ2𝑛\mathcal{I}\_{2}^{n} such that n≤N𝑛𝑁n\leq N. If n=1𝑛1n=1 then I=(i1)𝐼subscript𝑖1I=(i\_{1}) and we necessarily one of the following two options must hold

* •

  If i1=1subscript𝑖11i\_{1}=1 then 𝕏s,t(i1)=t−s=𝕎^s,tL​L,(1)=⟨P1,𝕎^s,tL​L⟩superscriptsubscript𝕏
  𝑠𝑡subscript𝑖1𝑡𝑠superscriptsubscript^𝕎
  𝑠𝑡
  𝐿𝐿1
  subscript𝑃1superscriptsubscript^𝕎
  𝑠𝑡𝐿𝐿\mathbb{X}\_{s,t}^{(i\_{1})}=t-s=\widehat{\mathbb{W}}\_{s,t}^{LL,(1)}=\langle P\_{1},\widehat{\mathbb{W}}\_{s,t}^{LL}\rangle
* •

  If i1=2subscript𝑖12i\_{1}=2 then 𝕏s,t(i1)=Xt−Xs=⟨ℓ⊗(4),𝕎^s,tL​L⟩=⟨P2,𝕎^s,tL​L⟩superscriptsubscript𝕏
  𝑠𝑡subscript𝑖1subscript𝑋𝑡subscript𝑋𝑠
  tensor-productℓ4superscriptsubscript^𝕎
  𝑠𝑡𝐿𝐿
  subscript𝑃2superscriptsubscript^𝕎
  𝑠𝑡𝐿𝐿\mathbb{X}\_{s,t}^{(i\_{1})}=X\_{t}-X\_{s}=\langle\ell\otimes(4),\widehat{\mathbb{W}}\_{s,t}^{LL}\rangle=\langle P\_{2},\widehat{\mathbb{W}}\_{s,t}^{LL}\rangle.

Hence the statement holds for n=1𝑛1n=1. Let’s assume by induction that the statement holds for any 1≤n≤N1𝑛𝑁1\leq n\leq N. We write I=J⊗(in)𝐼tensor-product𝐽subscript𝑖𝑛I=J\otimes(i\_{n}) with in∈{1,2}subscript𝑖𝑛12i\_{n}\in\{1,2\} and J=(i1,…,in−1)∈ℐ2n−1𝐽subscript𝑖1…subscript𝑖𝑛1superscriptsubscriptℐ2𝑛1J=(i\_{1},\ldots,i\_{n-1})\in\mathcal{I}\_{2}^{n-1}. Clearly |(in)|,|J|<n

subscript𝑖𝑛𝐽
𝑛|(i\_{n})|,|J|<n, therefore by induction hypothesis

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,t(in)=⟨C(in)​(ℓ),𝕎^s,tL​L⟩=⟨Pin,𝕎^s,tL​L⟩superscriptsubscript𝕏  𝑠𝑡subscript𝑖𝑛  subscript𝐶subscript𝑖𝑛ℓsuperscriptsubscript^𝕎  𝑠𝑡𝐿𝐿  subscript𝑃subscript𝑖𝑛superscriptsubscript^𝕎  𝑠𝑡𝐿𝐿\mathbb{X}\_{s,t}^{(i\_{n})}=\langle C\_{(i\_{n})}(\ell),\widehat{\mathbb{W}}\_{s,t}^{LL}\rangle=\langle P\_{i\_{n}},\widehat{\mathbb{W}}\_{s,t}^{LL}\rangle |  |

and

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,t(J)=⟨CJ​(ℓ),𝕎^s,tL​L⟩=⟨(…​(Pi1≻Pi2)≻…≻Pin−1),𝕎^s,tL​L⟩superscriptsubscript𝕏  𝑠𝑡𝐽  subscript𝐶𝐽ℓsuperscriptsubscript^𝕎  𝑠𝑡𝐿𝐿  succeeds…succeedssubscript𝑃subscript𝑖1subscript𝑃subscript𝑖2…succeedssubscript𝑃subscript𝑖𝑛1superscriptsubscript^𝕎  𝑠𝑡𝐿𝐿\displaystyle\mathbb{X}\_{s,t}^{(J)}=\langle C\_{J}(\ell),\widehat{\mathbb{W}}\_{s,t}^{LL}\rangle=\langle(\ldots(P\_{i\_{1}}\succ P\_{i\_{2}})\succ\ldots\succ P\_{i\_{n-1}}),\widehat{\mathbb{W}}\_{s,t}^{LL}\rangle |  |

By definition of the signature (see [2.6](#S2.Thmtheorem6 "Definition 2.6 (Signature). ‣ 2.3. Signatures ‣ 2. Notation and preliminaries ‣ Sig-SDEs model for quantitative finance.")) we know that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝕏s,t(I)superscriptsubscript𝕏  𝑠𝑡𝐼\displaystyle\mathbb{X}\_{s,t}^{(I)} | =∫st𝕏s,u(J)∘𝑑𝕏u(in)absentsuperscriptsubscript𝑠𝑡superscriptsubscript𝕏  𝑠𝑢𝐽differential-dsuperscriptsubscript𝕏𝑢subscript𝑖𝑛\displaystyle=\int\_{s}^{t}\mathbb{X}\_{s,u}^{(J)}\circ d\mathbb{X}\_{u}^{(i\_{n})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫st⟨CJ​(ℓ),𝕎^s,tL​L⟩∘d​⟨C(in)​(ℓ),𝕎^s,tL​L⟩absentsuperscriptsubscript𝑠𝑡  subscript𝐶𝐽ℓsuperscriptsubscript^𝕎  𝑠𝑡𝐿𝐿 𝑑  subscript𝐶subscript𝑖𝑛ℓsuperscriptsubscript^𝕎  𝑠𝑡𝐿𝐿\displaystyle=\int\_{s}^{t}\langle C\_{J}(\ell),\widehat{\mathbb{W}}\_{s,t}^{LL}\rangle\circ d\langle C\_{(i\_{n})}(\ell),\widehat{\mathbb{W}}\_{s,t}^{LL}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨CJ​(ℓ)≻C(in)​(ℓ),𝕎^s,tL​L⟩absentdelimited-⟨⟩succeedssubscript𝐶𝐽ℓ  subscript𝐶subscript𝑖𝑛ℓsuperscriptsubscript^𝕎  𝑠𝑡𝐿𝐿\displaystyle=\langle C\_{J}(\ell)\succ C\_{(i\_{n})}(\ell),\widehat{\mathbb{W}}\_{s,t}^{LL}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨(…​(Pi1≻Pi2)≻…≻Pin−1)≻Pin,𝕎^s,tL​L⟩absentdelimited-⟨⟩succeedssucceeds…succeedssubscript𝑃subscript𝑖1subscript𝑃subscript𝑖2…succeedssubscript𝑃subscript𝑖𝑛1  subscript𝑃subscript𝑖𝑛superscriptsubscript^𝕎  𝑠𝑡𝐿𝐿\displaystyle=\langle(\ldots(P\_{i\_{1}}\succ P\_{i\_{2}})\succ\ldots\succ P\_{i\_{n-1}})\succ P\_{i\_{n}},\widehat{\mathbb{W}}\_{s,t}^{LL}\rangle |  |

which concludes the induction.
∎

## 7. Calibration

We will now address the task of calibrating a Signature Model. We assume that the market has a family of options {Φi}i=1nsuperscriptsubscriptsubscriptΦ𝑖𝑖1𝑛\{\Phi\_{i}\}\_{i=1}^{n} whose market prices {pi}i=1nsuperscriptsubscriptsubscript𝑝𝑖𝑖1𝑛\{p\_{i}\}\_{i=1}^{n} are observable. Typically {Φi}i=1nsuperscriptsubscriptsubscriptΦ𝑖𝑖1𝑛\{\Phi\_{i}\}\_{i=1}^{n} will contain vanilla options, together with some exotic options such as various variance or barrier products. Fix N∈ℕ𝑁ℕN\in\mathbb{N} be the order of the Signature Model. The challenge here is to find the model parameter ℓ={ℓ(K):K∈ℐ2N}ℓconditional-setsuperscriptℓ𝐾𝐾superscriptsubscriptℐ2𝑁\ell=\{\ell^{(K)}:K\in\mathcal{I}\_{2}^{N}\} that best fits the data, in the sense that the prices of ΦisubscriptΦ𝑖\Phi\_{i}, under the Signature Model with parameter ℓℓ\ell, are approximately given by the observed market prices pisubscript𝑝𝑖p\_{i}.

Following Section [6](#S6 "6. Pricing ‣ Sig-SDEs model for quantitative finance."), we assume that the options ΦisubscriptΦ𝑖\Phi\_{i} are given by signature options. Therefore, we assume that we can write ΦisubscriptΦ𝑖\Phi\_{i} by

|  |  |  |
| --- | --- | --- |
|  | Φi=⟨φi,𝕏^0,T⟩,φi={φi(K):K∈ℐ2N}.formulae-sequencesubscriptΦ𝑖  subscript𝜑𝑖subscript^𝕏  0𝑇subscript𝜑𝑖conditional-setsuperscriptsubscript𝜑𝑖𝐾𝐾superscriptsubscriptℐ2𝑁\Phi\_{i}=\langle\varphi\_{i},\widehat{\mathbb{X}}\_{0,T}\rangle,\quad\varphi\_{i}=\{\varphi\_{i}^{(K)}:K\in\mathcal{I}\_{2}^{N}\}. |  |

The minimisation problem we aim to solve now is the following:

|  |  |  |  |
| --- | --- | --- | --- |
| (14) |  | minℓ={ℓ(K):K∈ℐ2N}​∑i=1n(⟨φi,𝔼​[𝕏^0,T]⟩−pi)2.subscriptℓconditional-setsuperscriptℓ𝐾𝐾superscriptsubscriptℐ2𝑁superscriptsubscript𝑖1𝑛superscript  subscript𝜑𝑖𝔼delimited-[]subscript^𝕏  0𝑇 subscript𝑝𝑖2\min\_{\ell=\{\ell^{(K)}:K\in\mathcal{I}\_{2}^{N}\}}\sum\_{i=1}^{n}\left(\langle\varphi\_{i},\mathbb{E}[\widehat{\mathbb{X}}\_{0,T}]\rangle-p\_{i}\right)^{2}. |  |

where 𝔼​[𝕏^0,T]𝔼delimited-[]subscript^𝕏

0𝑇\mathbb{E}[\widehat{\mathbb{X}}\_{0,T}] is the expected signature of the Signature Model with parameter ℓ={ℓ(K):K∈ℐ2N}ℓconditional-setsuperscriptℓ𝐾𝐾superscriptsubscriptℐ2𝑁\ell=\{\ell^{(K)}:K\in\mathcal{I}\_{2}^{N}\}.

By Proposition [6.2](#S6.Thmtheorem2 "Proposition 6.2. ‣ 6. Pricing ‣ Sig-SDEs model for quantitative finance."), the price of ΦisubscriptΦ𝑖\Phi\_{i}, which is given by ⟨φi,𝔼​[𝕏^0,T]⟩

subscript𝜑𝑖𝔼delimited-[]subscript^𝕏

0𝑇\langle\varphi\_{i},\mathbb{E}[\widehat{\mathbb{X}}\_{0,T}]\rangle, can be written as a polynomial on ℓ(K)superscriptℓ𝐾\ell^{(K)}. Hence, the optimisation ([14](#S7.E14 "In 7. Calibration ‣ Sig-SDEs model for quantitative finance.")) is rewritten as a minimisation of a polynomial of variables ℓ(K)superscriptℓ𝐾\ell^{(K)}, for K∈ℐ2N𝐾superscriptsubscriptℐ2𝑁K\in\mathcal{I}\_{2}^{N}.

If the number of parameters ℓ(K)superscriptℓ𝐾\ell^{(K)} is large compared to the number of available option prices, the optimisation problem might be overparametrised and there will be multiple solutions to ([14](#S7.E14 "In 7. Calibration ‣ Sig-SDEs model for quantitative finance.")). In this case, we are in the robust finance setting where there are multiple equivalent martingale measures that fit to the data. If the number of parameters ℓ(K)superscriptℓ𝐾\ell^{(K)} is small, however, we are in the setting of classical mathematical finance modeling and there will in general be a unique solution to ([14](#S7.E14 "In 7. Calibration ‣ Sig-SDEs model for quantitative finance.")).

## 8. Conclusion

In this paper we have proposed a new model for asset price dynamics called the signature model. This model was develop with the objective of satisfying the following properties:

1. (1)

   Universality.
2. (2)

   Efficiency of calibration to vanilla and exotic options.
3. (3)

   Fast pricing of vanilla and exotic options.
4. (4)

   Efficiency of simulation.

Due to the rich properties of signatures, the signature model satisfies all four properties and is, therefore, capable of generating realistic paths without sacrificing the computational feasibility of calibration, pricing and simulation.

Although this paper has focused on the risk-neutral measure ℚℚ\mathbb{Q}, it can also be used to learn the real-world measure ℙℙ\mathbb{P}. One would first calibrate to the risk-neutral measure ℚℚ\mathbb{Q} and then learn the drift.

###### Acknowledgements.

This work was supported by The Alan Turing Institute under the EPSRC grant EP/N510129/1.

## References

* (1)
* Acciaio et al. (2019)

  Beatrice Acciaio, Julio
  Backhoff-Veraguas, and Anastasiia Zalashko.
  2019.
  Causal optimal transport and its links to
  enlargement of filtrations and continuous-time stochastic optimization.
  *Stochastic Processes and their Applications*
  (2019).
* Boedihardjo et al. (2016)

  Horatio Boedihardjo, Xi
  Geng, Terry Lyons, and Danyu Yang.
  2016.
  The signature of a rough path: uniqueness.
  *Advances in Mathematics*
  293 (2016), 720–737.
* Breeden and
  Litzenberger (1978)

  Douglas T Breeden and
  Robert H Litzenberger. 1978.
  Prices of state-contingent claims implicit in
  option prices.
  *Journal of business* (1978),
  621–651.
* Cartea et al. (2020)

  Álvaro Cartea, Imanol
  Perez Arribas, and Leandro Sánchez-Betancourt.
  2020.
  Optimal Execution of Foreign Securities: A
  Double-Execution Problem with Signatures and Machine Learning.
  *Available at SSRN* (2020).
* Chevyrev
  et al. (2016)

  Ilya Chevyrev, Terry
  Lyons, et al. 2016.
  Characteristic functions of measures on geometric
  rough paths.
  *The Annals of Probability*
  44, 6 (2016),
  4049–4082.
* Chevyrev and
  Oberhauser (2018)

  Ilya Chevyrev and Harald
  Oberhauser. 2018.
  Signature moments to characterize laws of
  stochastic processes.
  *arXiv preprint arXiv:1810.10971*
  (2018).
* Cuchiero
  et al. (2020)

  Christa Cuchiero, Wahid
  Khosrawi, and Josef Teichmann.
  2020.
  A generative adversarial network approach to
  calibration of local stochastic volatility models.
  *arXiv preprint arXiv:2005.02505*
  (2020).
* Fermanian (2019)

  Adeline Fermanian.
  2019.
  Embedding and learning with signatures.
  *arXiv preprint arXiv:1911.13211*
  (2019).
* Flint
  et al. (2016)

  Guy Flint, Ben Hambly,
  and Terry Lyons. 2016.
  Discretely sampled signals and the rough Hoff
  process.
  *Stochastic Processes and their Applications*
  126, 9 (2016),
  2593–2614.
* Gierjatowicz P. (2020)

  M. Siska D. Szpruch L. Gierjatowicz P.,
  Sabate-Vidales. 2020.
  Robust Pricing and Hedging with neural SDEs.
  *to appear* (2020).
* Goodfellow et al. (2014)

  Ian Goodfellow, Jean
  Pouget-Abadie, Mehdi Mirza, Bing Xu,
  David Warde-Farley, Sherjil Ozair,
  Aaron Courville, and Yoshua Bengio.
  2014.
  Generative adversarial nets. In
  *Advances in neural information processing
  systems*. 2672–2680.
* Gyurkó et al. (2013)

  Lajos Gergely Gyurkó,
  Terry Lyons, Mark Kontkowski, and
  Jonathan Field. 2013.
  Extracting information from the signature of a
  financial data stream.
  *arXiv preprint arXiv:1307.7244*
  (2013).
* Hambly and Lyons (2010)

  Ben Hambly and Terry
  Lyons. 2010.
  Uniqueness for the signature of a path of bounded
  variation and the reduced path group.
  *Annals of Mathematics*
  (2010), 109–167.
* Kalsi
  et al. (2020)

  Jasdeep Kalsi, Terry
  Lyons, and Imanol Perez Arribas.
  2020.
  Optimal execution with rough path signatures.
  *SIAM Journal on Financial Mathematics*
  11, 2 (2020),
  470–493.
* Karatzas and
  Shreve (2012)

  Ioannis Karatzas and
  Steven Shreve. 2012.
  *Brownian motion and stochastic calculus.
  Vol. Vol. 113*.
  Springer Science & Business Media.
* Kidger et al. (2019)

  Patrick Kidger, Patric
  Bonnier, Imanol Perez Arribas, Cristopher
  Salvi, and Terry Lyons.
  2019.
  Deep Signature Transforms. In
  *Advances in Neural Information Processing
  Systems*. 3099–3109.
* Kidger and Lyons (2020)

  Patrick Kidger and Terry
  Lyons. 2020.
  Signatory: differentiable computations of the
  signature and logsignature transforms, on both CPU and GPU.
  *arXiv preprint arXiv:2001.00706*
  (2020).
* Kingma and
  Welling (2013)

  Diederik P Kingma and
  Max Welling. 2013.
  Auto-encoding variational bayes.
  *arXiv preprint arXiv:1312.6114*
  (2013).
* Király and
  Oberhauser (2016)

  Franz J Király and
  Harald Oberhauser. 2016.
  Kernels for sequentially ordered data.
  *arXiv preprint arXiv:1601.08169*
  (2016).
* Levin
  et al. (2013)

  Daniel Levin, Terry
  Lyons, and Hao Ni. 2013.
  Learning from the past, predicting the statistics
  for the future, learning an evolving system.
  *arXiv preprint arXiv:1309.0260*
  (2013).
* Li et al. (2017)

  Chenyang Li, Xin Zhang,
  and Lianwen Jin. 2017.
  Lpsnet: A novel log path signature feature based
  hand gesture recognition framework. In *Proceedings
  of the IEEE International Conference on Computer Vision Workshops*.
  631–639.
* Lyons
  et al. (2019)

  Terry Lyons, Sina Nejad,
  and Imanol Perez Arribas.
  2019.
  Nonparametric pricing and hedging of exotic
  derivatives.
  *arXiv preprint arXiv:1905.00711*
  (2019).
* Lyons
  et al. (2020)

  Terry Lyons, Sina Nejad,
  and Imanol Perez Arribas.
  2020.
  Numerical Method for Model-free Pricing of Exotic
  Derivatives in Discrete Time Using Rough Path Signatures.
  *Applied Mathematical Finance*
  (2020), 1–15.
* Lyons
  et al. (2014)

  Terry Lyons, Hao Ni,
  and Harald Oberhauser. 2014.
  A feature set for streams and an application to
  high-frequency financial tick data. In *Proceedings
  of the 2014 International Conference on Big Data Science and Computing*.
  1–8.
* Lyons (1998)

  Terry J Lyons.
  1998.
  Differential equations driven by rough signals.
  *Revista Matemática Iberoamericana*
  14, 2 (1998),
  215–310.
* Lyons
  et al. (2007)

  Terry J Lyons, Michael
  Caruana, and Thierry Lévy.
  2007.
  *Differential equations driven by rough
  paths*.
  Springer.
* Reizenstein and
  Graham (2020)

  Jeremy F Reizenstein and
  Benjamin Graham. 2020.
  Algorithm 1004: The iisignature library: Efficient
  calculation of iterated-integral signatures and log signatures.
  *ACM Transactions on Mathematical Software
  (TOMS)* 46, 1 (2020),
  1–21.
* Vapnik (2013)

  Vladimir Vapnik.
  2013.
  *The nature of statistical learning
  theory*.
  Springer science & business media.
* Xie
  et al. (2017)

  Zecheng Xie, Zenghui Sun,
  Lianwen Jin, Hao Ni, and
  Terry Lyons. 2017.
  Learning spatial-semantic context with fully
  convolutional recurrent network for online handwritten chinese text
  recognition.
  *IEEE transactions on pattern analysis and
  machine intelligence* 40, 8
  (2017), 1903–1917.
* Yang
  et al. (2015)

  Weixin Yang, Lianwen Jin,
  and Manfei Liu. 2015.
  Chinese character-level writer identification using
  path signature feature, DropStroke and deep CNN. In
  *2015 13th International Conference on Document
  Analysis and Recognition (ICDAR)*. IEEE, 546–550.
* Yang
  et al. (2016a)

  Weixin Yang, Lianwen Jin,
  and Manfei Liu. 2016a.
  Deepwriterid: An end-to-end online text-independent
  writer identification system.
  *IEEE Intelligent Systems*
  31, 2 (2016),
  45–53.
* Yang
  et al. (2016b)

  Weixin Yang, Lianwen Jin,
  Hao Ni, and Terry Lyons.
  2016b.
  Rotation-free online handwritten character
  recognition using dyadic path signature features, hanging normalization, and
  deep neural network. In *2016 23rd International
  Conference on Pattern Recognition (ICPR)*. IEEE,
  4083–4088.
* Yang
  et al. (2016c)

  Weixin Yang, Lianwen Jin,
  Dacheng Tao, Zecheng Xie, and
  Ziyong Feng. 2016c.
  DropSample: A new training method to enhance deep
  convolutional neural networks for large-scale unconstrained handwritten
  Chinese character recognition.
  *Pattern Recognition* 58
  (2016), 190–203.
* Yang
  et al. (2017)

  Weixin Yang, Terry Lyons,
  Hao Ni, Cordelia Schmid,
  Lianwen Jin, and Jiawei Chang.
  2017.
  Leveraging the path signature for skeleton-based
  human action recognition.
  *arXiv preprint arXiv:1707.03993*
  (2017).

## Appendix A Overview of signatures

In this section we state some of the main properties of signatures that are used in this paper.

###### Definition A.1 (Shuffle of multi-indices).

For any two multi-indices I,J∈ℐd

𝐼𝐽
subscriptℐ𝑑I,J\in\mathcal{I}\_{d} and 111-dimensional multi-indices a,b∈ℐd1={1,…,d}

𝑎𝑏
superscriptsubscriptℐ𝑑11…𝑑a,b\in\mathcal{I}\_{d}^{1}=\{1,\ldots,d\} we define the shuffle product recursively as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| (15) |  | ø​I=I​ø=Iitalic-ø𝐼𝐼italic-ø𝐼\o\shuffle I=I\shuffle\o=I |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
| (16) |  | (I⊗a)​(J⊗b)=((I⊗a)​J)⊗b+(I​(J⊗b))⊗atensor-product𝐼𝑎tensor-product𝐽𝑏tensor-producttensor-product𝐼𝑎𝐽𝑏tensor-product𝐼tensor-product𝐽𝑏𝑎(I\otimes a)\shuffle(J\otimes b)=((I\otimes a)\shuffle J)\otimes b+(I\shuffle(J\otimes b))\otimes a |  |

###### Example A.2.

We have the following examples for ℐ4subscriptℐ4\mathcal{I}\_{4}:

1. (1)

   (1,2)​(3)=(1,2,3)+(1,3,2)+(3,1,2)123123132312(1,2)\shuffle(3)=(1,2,3)+(1,3,2)+(3,1,2).
2. (2)

   (1,2)​(3,4)=2⋅(1,2,2,4)+(1,2,4,2)+(2,1,2,4)+(2,1,4,2)+(2,4,1,2)1234⋅212241242212421422412(1,2)\shuffle(3,4)=2\cdot(1,2,2,4)+(1,2,4,2)+(2,1,2,4)+(2,1,4,2)+(2,4,1,2).
3. (3)

   (2,1)​ø=(2,1)21italic-ø21(2,1)\shuffle\o=(2,1).
4. (4)

   ø​(2,1)=(2,1)italic-ø2121\o\shuffle(2,1)=(2,1).

###### Proposition A.3 (Shuffle identity).

Let X:[0,T]→ℝd:𝑋→0𝑇superscriptℝ𝑑X:[0,T]\to\mathbb{R}^{d} be a continuous semimartingale. For any two multi-indices I,J∈ℐd

𝐼𝐽
subscriptℐ𝑑I,J\in\mathcal{I}\_{d} the following identity on the Signature of X𝑋X holds

|  |  |  |  |
| --- | --- | --- | --- |
| (17) |  | ⟨I​J,𝕏s,t⟩=⟨I,𝕏s,t⟩⋅⟨J,𝕏s,t⟩:=𝕏s,t(I)⋅𝕏s,t(J)  𝐼𝐽subscript𝕏  𝑠𝑡 ⋅  𝐼subscript𝕏  𝑠𝑡  𝐽subscript𝕏  𝑠𝑡assign⋅superscriptsubscript𝕏  𝑠𝑡𝐼superscriptsubscript𝕏  𝑠𝑡𝐽\langle I\shuffle J,\mathbb{X}\_{s,t}\rangle=\langle I,\mathbb{X}\_{s,t}\rangle\cdot\langle J,\mathbb{X}\_{s,t}\rangle:=\mathbb{X}\_{s,t}^{(I)}\cdot\mathbb{X}\_{s,t}^{(J)} |  |

###### Proof.

Theorem 2.15 in (Lyons
et al., [2007](#bib.bib27)).
∎

###### Proposition A.4 (Uniqueness of the Signature).

Let X:[0,T]→ℝd:𝑋→0𝑇superscriptℝ𝑑X:[0,T]\to\mathbb{R}^{d}, Y:[0,T]→ℝd:𝑌→0𝑇superscriptℝ𝑑Y:[0,T]\to\mathbb{R}^{d} be two continuous semimartingales. Then

|  |  |  |  |
| --- | --- | --- | --- |
| (18) |  | ∀t∈[0,T],Xt=Yt⇔∀K∈ℐd,𝕏s,t(K)=𝕐s,t(K)iffformulae-sequencefor-all𝑡0𝑇subscript𝑋𝑡subscript𝑌𝑡formulae-sequencefor-all𝐾subscriptℐ𝑑subscriptsuperscript𝕏𝐾  𝑠𝑡subscriptsuperscript𝕐𝐾  𝑠𝑡\forall t\in[0,T],X\_{t}=Y\_{t}\iff\forall K\in\mathcal{I}\_{d},\mathbb{X}^{(K)}\_{s,t}=\mathbb{Y}^{(K)}\_{s,t} |  |

###### Proof.

See main result in (Hambly and Lyons, [2010](#bib.bib14)).
∎

###### Proposition A.5 (Factorial decay).

Given a semimartingale X:[0,T]→ℝd:𝑋→0𝑇superscriptℝ𝑑X:[0,T]\to\mathbb{R}^{d}, for any time interval [s,t]⊂[0,T]𝑠𝑡0𝑇[s,t]\subset[0,T] and any multi-index K∈ℐd𝐾subscriptℐ𝑑K\in\mathcal{I}\_{d} such that |K|=n𝐾𝑛|K|=n

|  |  |  |  |
| --- | --- | --- | --- |
| (19) |  | |𝕏s,t(K)|=O​(1n!)subscriptsuperscript𝕏𝐾  𝑠𝑡𝑂1𝑛\big{|}\mathbb{X}^{(K)}\_{s,t}\big{|}=O\left(\frac{1}{n!}\right) |  |

###### Proof.

Proposition 2.2 in (Lyons
et al., [2007](#bib.bib27)).
∎

###### Definition A.6.

For a given time interval [0,T]0𝑇[0,T] we call a continuous, surjective, increasing function ψ:[0,T]→[0,T]:𝜓→0𝑇0𝑇\psi:[0,T]\to[0,T] a time-reparametrization.

###### Proposition A.7 (Invariance to time-reparametrizations).

Let X:[0,T]→ℝd:𝑋→0𝑇superscriptℝ𝑑X:[0,T]\to\mathbb{R}^{d} be a semimartingale and ψ:[0,T]→[0,T]:𝜓→0𝑇0𝑇\psi:[0,T]\to[0,T] be a time-reparametrization. Then the Signature of X𝑋X has the following invariance property

|  |  |  |  |
| --- | --- | --- | --- |
| (20) |  | 𝕏s,t=𝕏ψ​(s),ψ​(t)​∀s,t∈[0,T]​ such that ​s<tformulae-sequencesubscript𝕏  𝑠𝑡subscript𝕏  𝜓𝑠𝜓𝑡for-all𝑠𝑡0𝑇 such that 𝑠𝑡\mathbb{X}\_{s,t}=\mathbb{X}\_{\psi(s),\psi(t)}\hskip 5.69046pt\forall s,t\in[0,T]\text{ such that }s<t |  |

###### Definition A.8 (Half-Shuffle).

Let F𝐹F and G𝐺G be any two linear functionals. We define their half-shuffle product ≻succeeds\succ on 𝕏s,tsubscript𝕏

𝑠𝑡\mathbb{X}\_{s,t} as the following (Stratonovich) iterated integral on the real line

|  |  |  |  |
| --- | --- | --- | --- |
| (21) |  | ⟨F≻G,𝕏s,t⟩=∫st⟨F,𝕏s,u⟩∘d​⟨G,𝕏s,u⟩delimited-⟨⟩succeeds𝐹  𝐺subscript𝕏  𝑠𝑡superscriptsubscript𝑠𝑡  𝐹subscript𝕏  𝑠𝑢 𝑑  𝐺subscript𝕏  𝑠𝑢\langle F\succ G,\mathbb{X}\_{s,t}\rangle=\int\_{s}^{t}\langle F,\mathbb{X}\_{s,u}\rangle\circ d\,\langle G,\mathbb{X}\_{s,u}\rangle |  |

Let 𝔹𝔹\mathbb{B} be a 222-dimensional Brownian motion, defined for example on the interval [0,1]01[0,1]. Consider two linear functionals F={F(K):K∈ℐd}𝐹conditional-setsuperscript𝐹𝐾𝐾subscriptℐ𝑑F=\{F^{(K)}:K\in\mathcal{I}\_{d}\} and G={G(K):K∈ℐd}𝐺conditional-setsuperscript𝐺𝐾𝐾subscriptℐ𝑑G=\{G^{(K)}:K\in\mathcal{I}\_{d}\} defined as

|  |  |  |  |
| --- | --- | --- | --- |
| (22) |  | F(K)={1if ​K=(1,2)0otherwisesuperscript𝐹𝐾cases1if 𝐾120otherwiseF^{(K)}=\left\{\begin{array}[]{ll}1&\mbox{if }K=(1,2)\\ 0&\mbox{otherwise}\end{array}\right. |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
| (23) |  | G(K)={1if ​K=(2,1)0otherwisesuperscript𝐺𝐾cases1if 𝐾210otherwiseG^{(K)}=\left\{\begin{array}[]{ll}1&\mbox{if }K=(2,1)\\ 0&\mbox{otherwise}\end{array}\right. |  |

Then the following quantity

|  |  |  |  |
| --- | --- | --- | --- |
| (24) |  | 𝒜s,t=12⟨F≻G−G≻F,𝔹s,t⟩\mathcal{A}\_{s,t}=\frac{1}{2}\big{\langle}F\succ G-G\succ F,\mathbb{B}\_{s,t}\big{\rangle} |  |

is the Levy area of the Brownian motion 𝔹𝔹\mathbb{B} on [s,t]⊂[0,1]𝑠𝑡01[s,t]\subset[0,1].

#### A.0.1. Expected signature

We will now define the expected signature of a semimartingale.

###### Definition A.9 (Expected signature).

Let X:[0,T]→ℝd:𝑋→0𝑇superscriptℝ𝑑X:[0,T]\to\mathbb{R}^{d} be a continuous semimartingale, and let 𝕏s,t={𝕏s,t(K)∈ℝ:K∈ℐd}subscript𝕏

𝑠𝑡conditional-setsuperscriptsubscript𝕏

𝑠𝑡𝐾ℝ𝐾subscriptℐ𝑑\mathbb{X}\_{s,t}=\{\mathbb{X}\_{s,t}^{(K)}\in\mathbb{R}:K\in\mathcal{I}\_{d}\} be its signature. The expected signature of X𝑋X is defined by

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝕏s,t]:={𝔼​[𝕏s,t(K)]∈ℝ:K∈ℐd}.assign𝔼delimited-[]subscript𝕏  𝑠𝑡conditional-set𝔼delimited-[]superscriptsubscript𝕏  𝑠𝑡𝐾ℝ𝐾subscriptℐ𝑑\mathbb{E}[\mathbb{X}\_{s,t}]:=\{\mathbb{E}[\mathbb{X}\_{s,t}^{(K)}]\in\mathbb{R}:K\in\mathcal{I}\_{d}\}. |  |

The expected signature – i.e. the expectation of the iterated integrals ([8](#S2.E8 "In Definition 2.6 (Signature). ‣ 2.3. Signatures ‣ 2. Notation and preliminaries ‣ Sig-SDEs model for quantitative finance.")) – behaves analogously to the moments of random variables, in the sense that under certain assumptions it characterises the law of the stochastic process:

###### Theorem A.10 ((Chevyrev et al., [2016](#bib.bib6))).

Let X:[0,T]→ℝd:𝑋→0𝑇superscriptℝ𝑑X:[0,T]\to\mathbb{R}^{d} be a semimartingale. Then, under certain assumptions (see (Chevyrev
et al., [2016](#bib.bib6))) the expected signature 𝔼​[𝕏0,T]𝔼delimited-[]subscript𝕏

0𝑇\mathbb{E}[\mathbb{X}\_{0,T}] characterises the law of X𝑋X.

## Appendix B Time and Lead-lag transformation

![Refer to caption](/html/2006.00218/assets/leadlag.png)

Figure 4. Lead-lag transformation of a Brownian motion.

\Description

Lead-lag path.

The invariance of the signature of a semimartingale to time reparametrizations allows to handle irregularly sampled sample paths (prices etc.) by completely eliminating the need to retain information about the original time-parametrization. Nonetheless, for the pricing of many options, especially ones resulting from payoffs calculated pathwise (such as integrals for American options), the time represents an important information that we are required to retain. To do so it suffices to augment the state space of the input semimartingale X𝑋X by adding time t𝑡t as an extra dimension to get Xtadd-time=(t,Xt)subscriptsuperscript𝑋add-time𝑡𝑡subscript𝑋𝑡X^{\text{add-time}}\_{t}=(t,X\_{t}).

We report another basic transformation that can be applied to semimartingales and that will be useful in the sequel of the paper: the lead-lag transformation. This transformation allows us to write Itô integrals as linear functions on the signature of the lead-lag transformed path.

###### Definition B.1 (Lead-lag transformation).

Let Z:[0,T]→ℝd:𝑍→0𝑇superscriptℝ𝑑Z:[0,T]\to\mathbb{R}^{d} be a semimartingale. For each partition D={ti}i⊂[0,T]𝐷subscriptsubscript𝑡𝑖𝑖0𝑇D=\{t\_{i}\}\_{i}\subset[0,T] of mesh size |D|𝐷|D|, define the piecewise linear path ZD:[0,T]→ℝ2​d:superscript𝑍𝐷→0𝑇superscriptℝ2𝑑Z^{D}:[0,T]\to\mathbb{R}^{2d} given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (25) |  |  | Z2​k​T/2​nD:=(Ztk,Ztk),assignsuperscriptsubscript𝑍2𝑘𝑇2𝑛𝐷subscript𝑍subscript𝑡𝑘subscript𝑍subscript𝑡𝑘\displaystyle Z\_{2kT/2n}^{D}:=(Z\_{t\_{k}},Z\_{t\_{k}}), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (26) |  |  | Z(2​k+1)​T/2​nD:=(Ztk,Ztk+1)assignsuperscriptsubscript𝑍2𝑘1𝑇2𝑛𝐷subscript𝑍subscript𝑡𝑘subscript𝑍subscript𝑡𝑘1\displaystyle Z\_{(2k+1)T/2n}^{D}:=(Z\_{t\_{k}},Z\_{t\_{k+1}}) |  |

and linear interpolation in between. Figure [4](#A2.F4 "Figure 4 ‣ Appendix B Time and Lead-lag transformation ‣ Sig-SDEs model for quantitative finance.") shows the lead-lag transformation of a Brownian motion. As we see, the lead component leads the lag component, hence the name. The lead component can be seen as the future of the path, and the lag component as the past.

Denote by ℤDsuperscriptℤ𝐷\mathbb{Z}^{D} the signature of ZDsuperscript𝑍𝐷Z^{D}. Then, we define the lead-lag transformation of Z𝑍Z, denoted by ℤL​Lsuperscriptℤ𝐿𝐿\mathbb{Z}^{LL}, as the limit of signatures of ℤDsuperscriptℤ𝐷\mathbb{Z}^{D}:

|  |  |  |
| --- | --- | --- |
|  | ℤL​L:=lim|D|→0ℤD.assignsuperscriptℤ𝐿𝐿subscript→𝐷0superscriptℤ𝐷\mathbb{Z}^{LL}:=\lim\_{|D|\rightarrow 0}\mathbb{Z}^{D}. |  |

The work in (Flint
et al., [2016](#bib.bib10)) showed the convergence of this limit and studied some of its properties.

### B.1. Expected signature of the lead-lag Brownian motion

###### Definition B.2.

Let I=(i1,…,in)∈missing​I3n𝐼subscript𝑖1…subscript𝑖𝑛missingsubscriptsuperscript𝐼𝑛3I=(i\_{1},\ldots,i\_{n})\in\mathcal{\mathcal{missing}}{I}^{n}\_{3} be a multi-index. We denote by 𝒫​(I)𝒫𝐼\mathcal{P}(I) the set of all possible tuples of non-empty multi-indices from ℐ3n−1subscriptsuperscriptℐ𝑛13\mathcal{I}^{n-1}\_{3} such that their concatenation is equal to I𝐼I and their length doesn’t exceed 222, i.e.

|  |  |  |
| --- | --- | --- |
|  | 𝒫​(I)={(I1,…,Ik)∈(ℐ3n−1)k:I1⊗…⊗Ik=I​ and ​|Ij|∈{1,2}}𝒫𝐼conditional-setsubscript𝐼1…subscript𝐼𝑘superscriptsubscriptsuperscriptℐ𝑛13𝑘tensor-productsubscript𝐼1…subscript𝐼𝑘𝐼 and subscript𝐼𝑗12\mathcal{P}(I)=\{(I\_{1},\ldots,I\_{k})\in(\mathcal{I}^{n-1}\_{3})^{k}:I\_{1}\otimes\ldots\otimes I\_{k}=I\text{ and }|I\_{j}|\in\{1,2\}\} |  |

###### Example B.3.

1. (1)

   𝒫​((1,2,3))={(1,2,3),(1,(2,3)),((1,2),3)}𝒫123123123123\mathcal{P}((1,2,3))=\{(1,2,3),(1,(2,3)),((1,2),3)\}.
2. (2)

   𝒫​((1,3,2,2))={(1,3,2,2),(1,(3,2),2),(1,3,(2,2)),((1,3),2,2),((1,3),(2,2))}\begin{aligned} \mathcal{P}((1,3,2,2))=&\{(1,3,2,2),(1,(3,2),2),(1,3,(2,2)),\\
   &((1,3),2,2),((1,3),(2,2))\}\end{aligned}
3. (3)

   𝒫​((3,2))={(3,2),((3,2))}𝒫323232\mathcal{P}((3,2))=\{(3,2),((3,2))\}.

###### Definition B.4 (Exponential of a linear functional).

Let F={F(K)∈ℝ:K∈ℐd}𝐹conditional-setsuperscript𝐹𝐾ℝ𝐾subscriptℐ𝑑F=\{F^{(K)}\in\mathbb{R}:K\in\mathcal{I}\_{d}\} be a linear functional. We define the exponential of F𝐹F as the following linear functional

|  |  |  |  |
| --- | --- | --- | --- |
| (27) |  | exp⁡(F)=(ø)+∑k=1∞1k!​F⊗k𝐹italic-øsuperscriptsubscript𝑘11𝑘superscript𝐹tensor-productabsent𝑘\exp(F)=(\o)+\sum\_{k=1}^{\infty}\frac{1}{k!}F^{\otimes k} |  |

where for any k≥1,F⊗k=F⊗…⊗Fformulae-sequence𝑘1superscript𝐹tensor-productabsent𝑘tensor-product𝐹…𝐹k\geq 1,F^{\otimes k}=F\otimes\ldots\otimes F for k𝑘k times.

###### Proposition B.5.

Define the function α:ℐ3→ℐ3:𝛼→subscriptℐ3subscriptℐ3\alpha:\mathcal{I}\_{3}\to\mathcal{I}\_{3} that maps a multi-index to another multi-index in the following way: ∀I∈ℐ3for-all𝐼subscriptℐ3\forall I\in\mathcal{I}\_{3}

|  |  |  |  |
| --- | --- | --- | --- |
| (28) |  | α​(I)={(1)if ​I=(1)(2)if ​I∈{(2),(3)}−12​(1)if ​I=(2,3)12​(1)if ​I=(3,2)0⋅(ø)otherwise𝛼𝐼cases1if 𝐼12if 𝐼23121if 𝐼23121if 𝐼32⋅0italic-øotherwise\alpha(I)=\left\{\begin{array}[]{ll}(1)&\mbox{if }I=(1)\\ (2)&\mbox{if }I\in\{(2),(3)\}\\ -\frac{1}{2}(1)&\mbox{if }I=(2,3)\\ \frac{1}{2}(1)&\mbox{if }I=(3,2)\\ 0\cdot(\o)&\mbox{otherwise}\end{array}\right. |  |

Given a final time T𝑇T define the linear functional 𝐄T:=exp⁡(T+T2​(2,2))assignsubscript𝐄𝑇𝑇𝑇222\mathbf{E}\_{T}:=\exp(T+\frac{T}{2}(2,2)). Then we have the explicit closed-form expression for the Expected Signature of the lead-lag Brownian motion: given any multi-index I∈ℐ3𝐼subscriptℐ3I\in\mathcal{I}\_{3}

|  |  |  |  |
| --- | --- | --- | --- |
| (29) |  | 𝔼​[𝕎^0,TL​L,(I)]=∑(I1,…,Ik)∈𝒫​(I)⟨α​(I1)⊗…⊗α​(Ik),𝐄T⟩𝔼delimited-[]superscriptsubscript^𝕎  0𝑇  𝐿𝐿𝐼subscriptsubscript𝐼1…subscript𝐼𝑘𝒫𝐼  tensor-product𝛼subscript𝐼1…𝛼subscript𝐼𝑘subscript𝐄𝑇\mathbb{E}\left[\mathbb{\widehat{W}}\_{0,T}^{LL,(I)}\right]=\sum\_{(I\_{1},\ldots,I\_{k})\in\mathcal{P}(I)}\mathbf{\langle}\alpha(I\_{1})\otimes\ldots\otimes\alpha(I\_{k}),\mathbf{E}\_{T}\rangle |  |

###### Proof.

Follows from (Lyons
et al., [2019](#bib.bib23), Lemma B.1) and the fact that 𝔼​[𝕎^0,T]=𝐄T𝔼delimited-[]subscript^𝕎

0𝑇subscript𝐄𝑇\mathbb{E}[\widehat{\mathbb{W}}\_{0,T}]=\mathbf{E}\_{T}.
∎

###### Example B.6.

If I=(3,2,3)𝐼323I=(3,2,3), 𝒫​(I)={(3,2,3),((3,2),3),(3,(2,3))}𝒫𝐼323323323\mathcal{P}(I)=\{(3,2,3),((3,2),3),(3,(2,3))\}. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝕎^0,TL​L,(I)]𝔼delimited-[]superscriptsubscript^𝕎  0𝑇  𝐿𝐿𝐼\displaystyle\mathbb{E}\left[\mathbb{\widehat{W}}\_{0,T}^{LL,(I)}\right] | =⟨α​(3)⊗α​(2)⊗α​(3),𝐄T⟩absent  tensor-producttensor-product𝛼3𝛼2𝛼3subscript𝐄𝑇\displaystyle=\langle\alpha(3)\otimes\alpha(2)\otimes\alpha(3),\mathbf{E}\_{T}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +α((3,2))⊗α(3),𝐄T⟩\displaystyle\ \ \ +\alpha((3,2))\otimes\alpha(3),\mathbf{E}\_{T}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +α(3)⊗α((2,3)),𝐄T⟩\displaystyle\ \ \ +\alpha(3)\otimes\alpha((2,3)),\mathbf{E}\_{T}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝐄T(2,2,2)+12​𝐄T(1,2)−12​𝐄T(2,1).absentsuperscriptsubscript𝐄𝑇22212superscriptsubscript𝐄𝑇1212superscriptsubscript𝐄𝑇21\displaystyle=\mathbf{E}\_{T}^{(2,2,2)}+\frac{1}{2}\mathbf{E}\_{T}^{(1,2)}-\frac{1}{2}\mathbf{E}\_{T}^{(2,1)}. |  |

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/2006.00218)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2006.00218)
[View original  
on arXiv](https://arxiv.org/abs/2006.00218)[►](javascript: void(0))