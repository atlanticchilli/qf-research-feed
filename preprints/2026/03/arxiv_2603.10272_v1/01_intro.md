---
authors:
- Alexander Aue
- Sebastian Kühnert
- Gregory Rice
- Jeremy VanderDoes
doc_id: arxiv:2603.10272v1
family_id: arxiv:2603.10272
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: An operator-level ARCH Model
url_abs: http://arxiv.org/abs/2603.10272v1
url_html: https://arxiv.org/html/2603.10272v1
venue: arXiv q-fin
version: 1
year: 2026
---


Alexander Aue
Department of Statistics, University of California, Davis, CA 95616 Davis, USA, ‡[aaue@ucdavis.edu](2603.10272v1/mailto:aaue@ucdavis.edu)

Sebastian Kühnert
Department of Mathematics, Ruhr University Bochum, 44780 Bochum, Germany, \*[sebastian.kuehnert@ruhr-uni-bochum.de](2603.10272v1/mailto:sebastian.kuehnert@ruhr-uni-bochum.de)

Gregory Rice


Jeremy VanderDoes

(March 10, 2026)

###### Abstract

AutoRegressive Conditional Heteroscedasticity (ARCH) models are standard for modeling time series exhibiting volatility, with a rich literature in univariate and multivariate settings. In recent years, these models have been extended to function spaces. However, functional ARCH and generalized ARCH (GARCH) processes established in the literature have thus far been restricted to model “pointwise” variances. In this paper, we propose a new ARCH framework for data residing in general separable Hilbert spaces that accounts for the full evolution of the conditional covariance operator. We define a general operator-level ARCH model. For a simplified Constant Conditional Correlation version of the model, we establish conditions under which such models admit strictly and weakly stationary solutions, finite moments, and weak serial dependence. Additionally, we derive consistent Yule–Walker-type estimators of the infinite-dimensional model parameters. The practical relevance of the model is illustrated through simulations and a data application to high-frequency cumulative intraday returns.

MSC 2020 subject classifications: 60G10, 62F12; 62R10

Keywords: ARCH; ﬁnancial time series; functional data; parameter estimation; stationary solutions

## 1 Introduction

Conditionally heteroscedastic processes are fundamental in financial modeling. To capture their dynamics, Engle ([1982](#bib.bib12)) introduced the Autoregressive Conditional Heteroscedastic (ARCH) model, later extended by Bollerslev ([1986](#bib.bib7)) to the Generalized ARCH (GARCH) model. Extensive reviews of uni- and multivariate (G)ARCH as well as other related volatility models can be found in Andersen et al. ([2009](#bib.bib1)), Asai et al. ([2006](#bib.bib3)), Bauwens et al. ([2006](#bib.bib5)), Francq and Zakoïan ([2019](#bib.bib13)), and Gouriéroux ([1997](#bib.bib14)).

With advances in data processing and the growing availability of high-frequency financial data, functional volatility and (G)ARCH (f(G)ARCH) models have gained prominence. As a motivating example, consider observing on consecutive days k∈{1,…,N}k\in\{1,\dots,N\} the price of the S&P 500 index at a resolution of one minute. Conveniently, these observations can be viewed as a sample of curves or functions {Pk(t)\{P\_{k}(t), i∈{1,…,N},t∈[0,1]}i\in\{1,\dots,N\},\;t\in[0,1]\}, where intraday time is normalized to the unit interval; see the left panel of Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ An operator-level ARCH Model"). A transformation of particular interest are the overnight intraday log-returns Xk​(t)=log⁡Pk​(t)−log⁡Pk−1​(1)X\_{k}(t)=\log P\_{k}(t)-\log P\_{k-1}(1); see the right panel of Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ An operator-level ARCH Model"). Representation of the data as functions constructed from noisy high-dimensional intraday observations allows for the use of techniques from functional data analysis. We refer the reader to Horváth and Kokoszka ([2012](#bib.bib18)) and Hsing and Eubank ([2015](#bib.bib19)) for introductions to functional data analysis, and to Bosq ([2000](#bib.bib8)) and Bosq and Blanke ([2007](#bib.bib9)) for introductions to linear time series processes in function spaces.

![Refer to caption](2603.10272v1/)


(a) S&P 500 price curves

![Refer to caption](2603.10272v1/)


(b) S&P 500 OCIDR

Figure 1: S&P500 Data. Visualization of price (left) and overnight cumulative intraday return (right) curves based on 15-minute resolution S&P 500 stock market prices from 2018 to 2020

In seminal work, Hörmann et al. ([2013](#bib.bib16)) introduced the fARCH(1)(1) process to model conditional heteroscedasticity in functional time series data. Their model was extended to fGARCH(1,1)(1,1) by Aue et al. ([2017](#bib.bib4)), and to general fGARCH(p,q)(p,q) by Cerovecki et al. ([2019](#bib.bib10)). For further developments and modified functional GARCH and volatility models, see Andersen et al. ([2024](#bib.bib2)), Kearney et al. ([2023](#bib.bib20)), Kühnert ([2019](#bib.bib24), [2020](#bib.bib25)), Laksaci et al. ([2025](#bib.bib29)), Li et al. ([2025](#bib.bib30)), Rice et al. ([2023](#bib.bib37)), Sun and Yu ([2020](#bib.bib39)).

Henceforth, we refer to these existing models as “pointwise” f(G)ARCH (pw-f(G)ARCH) models, since they are formulated as follows: For the function spaces C​[0,1]C[0,1] and L2​[0,1]L^{2}[0,1] of continuous and square-integrable functions on [0,1],[0,1], the pw-fARCH(p)(p) model as introduced in Cerovecki et al. ([2019](#bib.bib10)) takes the form

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Xk​(t)\displaystyle X\_{k}(t) | =σk​(t)​εk​(t),σk2​(t)=δ​(t)+∑i=1pαi​(Xk−i2)​(t),k∈ℤ;𝔼⁡(ε02​(t))=1.\displaystyle=\sigma\_{k}(t)\varepsilon\_{k}(t),\quad\sigma^{2}\_{k}(t)=\delta(t)+\sum\_{i=1}^{p}\,\alpha\_{i}(X^{2}\_{k-i})(t),\quad k\in\mathbb{Z};\qquad\operatorname{\mathds{E}}(\varepsilon^{2}\_{0}(t))=1. |  | (1.1) |

Here, the model parameters are δ\delta, a positive function, and αi\alpha\_{i}, bounded linear operators mapping non-negative functions to non-negative functions, with the εk\varepsilon\_{k} being i.i.d. and centered innovations. When there exists a stationary and causal solution to ([1.1](#S1.E1 "In 1 Introduction ‣ An operator-level ARCH Model")) with finite second-order moments, the condition 𝔼⁡(ε02​(t))=1\operatorname{\mathds{E}}(\varepsilon^{2}\_{0}(t))=1 identifies σk2​(t)=Var​(Xk​(t)|ℱk−1)\sigma\_{k}^{2}(t)=\mbox{Var}(X\_{k}(t)|\mathcal{F}\_{k-1}) as the pointwise conditional variance, where ℱk=σ​(εi,i≤k)\mathcal{F}\_{k}=\sigma(\varepsilon\_{i},\;i\leq k) is the information filtration generated by the innovations.

Despite its success in numerous applications, this model has some limitations. First, it only explicitly models the serial dependence structure of the pointwise conditional variance Var​(Xk​(t)|ℱk−1)\mbox{Var}(X\_{k}(t)|\mathcal{F}\_{k-1}). For many tasks, for example the construction of a prediction set for XkX\_{k}, one wishes to estimate the full conditional covariance kernel/operator of the sequence. Under model ([1.1](#S1.E1 "In 1 Introduction ‣ An operator-level ARCH Model")), so long as it is well-defined, the conditional covariance kernel takes the form

|  |  |  |
| --- | --- | --- |
|  | Cov​(Xk​(t),Xk​(s)|ℱk−1)=𝔼⁡[Xk​(t)​Xk​(s)|ℱk−1]=σk​(t)​σk​(s)​Cε​(t,s),\mbox{Cov}\big(X\_{k}(t),X\_{k}(s)\big|\mathcal{F}\_{k-1}\big)\;=\;\operatorname{\mathds{E}}\!\big[X\_{k}(t)X\_{k}(s)\big|\mathcal{F}\_{k-1}\big]\;=\;\sigma\_{k}(t)\sigma\_{k}(s)C\_{\varepsilon}(t,s), |  |

where CεC\_{\varepsilon} is the covariance kernel of the innovations. As such, the conditional covariance forecast implied by model ([1.1](#S1.E1 "In 1 Introduction ‣ An operator-level ARCH Model")) constitutes a “rank-one update” to the covariance of the innovations, which may be overly simplistic.

Similar critiques of the multivariate diagonal GARCH model have led to a plethora of alternative models of varying complexity, including the VEC, CCC, DCC, and BEKK GARCH; see Francq and Zakoïan ([2019](#bib.bib13), Ch. 10). Analogues of these models for functional time series have not been considered, to the best of our knowledge. One potential reason for this is the fact that the identity map is not compact in general, separable Hilbert spaces; an issue that is circumvented in the formulation of pw-fARCH models. The non-compactness of the identity map prevents the user from specifying in a useful way an innovation process with identity covariance so that the conditional covariance of the model, and the model parameters, can be identified. This identifiability issue can be overcome, however, by specifying that the innovations possess some known, injective covariance operator, which is a critical idea underlying our model.

In this paper, we propose a new ARCH model, termed “operator-level ARCH”, in general separable Hilbert spaces. It provides a more direct generalization of ARCH processes to the functional setting in that the model is formulated directly for the conditional covariance operator, rather than the pointwise variance as with pw-fARCH models. Since the general model is, from a theoretical point of view, quite challenging, we focus on an operator-level counterpart of the *Constant Conditional Correlation* (CCC) ARCH model in the multivariate setting, which is more feasible. We establish conditions on the model parameters and innovations such that it admits strictly and weakly stationary solutions, refining the classical notion of the (functional) *top Lyapunov exponent* for strict stationarity to suit our general setting. Additionally, we provide sufficient conditions for the existence of finite moments and weak dependence. Our estimation approach targets the ARCH operators under known orders and relies on pseudo Yule–Walker (YW) equations. We derive consistent YW estimators for the intercept term Δ,\Delta, which is a self-adjoint and positive definite operator in our setting, and the operators αi,\alpha\_{i}, which map between operator spaces. The estimates are developed under a specific diagonal representation in finite- and infinite-dimensional settings. The identifiability issue that arises when directly deriving the YW-type equations are addressed using specific transformations of the data. In the infinite-dimensional case, we introduce a Sobolev-type condition inspired by Hall and Meister ([2007](#bib.bib15)) to quantify the approximability of infinite-dimensional operators by their finite-dimensional approximations. The estimation is conducted via Tikhonov-type pseudoinverses in the YW framework. While the theoretical properties of the estimators are well established, their complexity may present practical challenges. The applicability of the proposed methodology is illustrated through a simulation study an application to intraday log-returns.

The structure of the paper is as follows. Section [2](#S2 "2 General model and assumptions ‣ An operator-level ARCH Model") introduces the general model and outlines the main assumptions. Section [3](#S3 "3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model") introduces the corresponding CCC model and derives stationarity conditions and probabilistic properties. Section [4](#S4 "4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model") addresses parameter estimation. Section [5](#S5 "5 Simulation Study ‣ An operator-level ARCH Model") presents a simulation study and Section [6](#S6 "6 Application to Intra-Day Return Data ‣ An operator-level ARCH Model") provides applications. Section [7](#S7 "7 Discussion ‣ An operator-level ARCH Model") concludes. Additionally, the appendix contains preliminaries (Sections [A](#A1 "Appendix A Preliminaries ‣ An operator-level ARCH Model") and [B](#A2 "Appendix B Notes ‣ An operator-level ARCH Model")), and proofs of key results (Section [C](#A3 "Appendix C Proofs ‣ An operator-level ARCH Model")).

We adopt the following notation. The identity map is denoted by 𝕀\mathbb{I}. On a Cartesian product space VnV^{n}, n∈ℕn\in\mathbb{N}, we define inner product and norm by ⟨x,y⟩=∑i=1n⟨xi,yi⟩\langle x,y\rangle=\sum\_{i=1}^{n}\langle x\_{i},y\_{i}\rangle and ‖x‖2=∑i=1n‖xi‖2\|x\|^{2}=\sum\_{i=1}^{n}\|x\_{i}\|^{2} for x=(x1,…,xn)⊤,y=(y1,…,yn)⊤∈Vnx=(x\_{1},\dots,x\_{n})^{\!\top},~y=(y\_{1},\dots,y\_{n})^{\!\top}\in V^{n}, assuming VV has inner product ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle and norm ∥⋅∥\|\cdot\|. The spaces of bounded linear, Hilbert-Schmidt (H-S), and nuclear/trace-class operators from ℋ\mathcal{H} to ℋ⋆\mathcal{H}\_{\star} are respectively denoted by ℒℋ,ℋ⋆\mathcal{L}\_{\mathcal{H},\mathcal{H}\_{\star}}, 𝒮ℋ,ℋ⋆\mathcal{S}\_{\mathcal{H},\mathcal{H}\_{\star}}, and 𝒩ℋ,ℋ⋆\mathcal{N}\_{\mathcal{H},\mathcal{H}\_{\star}}, with norms ∥⋅∥ℒ,∥⋅∥𝒮,∥⋅∥𝒩\|\cdot\|\_{\mathcal{L}},\|\cdot\|\_{\mathcal{S}},\|\cdot\|\_{\mathcal{N}} and H-S inner product ⟨⋅,⋅⟩𝒮\langle\cdot,\cdot\rangle\_{\mathcal{S}}. When ℋ,ℋ⋆\mathcal{H},\mathcal{H}\_{\star} are clear, we write 𝒯\mathcal{T} for 𝒯ℋ,ℋ⋆\mathcal{T}\_{\mathcal{H},\mathcal{H}\_{\star}} and 𝒯ℋ≔𝒯ℋ,ℋ,\mathcal{T\_{H}}\coloneqq\mathcal{T}\_{\mathcal{H},\mathcal{H}}, where 𝒯∈{ℒ,𝒮,𝒩}.\mathcal{T}\in\{\mathcal{L,S,N}\}. For A∈ℒA\in\mathcal{L}, A∗A^{\ast} denotes the adjoint. Write 𝒯≥0\mathcal{T}\_{\geq 0} (𝒯>0\mathcal{T}\_{>0}) for the self-adjoint non-negative (positive) definite elements of 𝒯\mathcal{T}. For x∈ℋ,y∈ℋ⋆x\in\mathcal{H},y\in\mathcal{H}\_{\star}, the *tensor product operator* is x⊗y≔⟨x,⋅⟩​yx\otimes y\coloneqq\langle x,\cdot\rangle y, with x⊗2≔x⊗x,x^{\otimes 2}\coloneqq x\otimes x, and x⊗𝒮yx\!\otimes\_{\mathcal{S}}\!y is used when x,yx,y are H-S operators. For p∈[1,∞)p\in[1,\infty), Lℋp=Lℋp​(Ω,𝔄,ℙ)L^{p}\_{\mathcal{H}}=L^{p}\_{\mathcal{H}}(\Omega,\mathfrak{A},\mathbb{P}) is the space of X∈ℋX\in\mathcal{H} with 𝔼​‖X‖p<∞\mathbb{E}\|X\|^{p}<\infty. The *cross-covariance operator* is

|  |  |  |
| --- | --- | --- |
|  | 𝒞X,Y≔𝔼​[X−𝔼​X]⊗[Y−𝔼​Y],X∈Lℋ2,Y∈Lℋ⋆2,\mathscr{C}\_{\!X,Y}\coloneqq\mathbb{E}[X-\mathbb{E}X]\otimes[Y-\mathbb{E}Y],\quad X\in L^{2}\_{\mathcal{H}},~Y\in L^{2}\_{\mathcal{H}\_{\star}}, |  |

and the *covariance operator* is 𝒞X=𝒞X,X\mathscr{C}\_{\!X}=\mathscr{C}\_{\!X,X}, with expectation in the Bochner sense. For weakly stationary 𝑿=(Xk)\boldsymbol{X}=(X\_{k}) and jointly weakly stationary 𝑿,𝒀\boldsymbol{X},\boldsymbol{Y}, the *lag-hh-covariance* and *lag-hh-cross-covariance* operators are 𝒞𝑿h≔𝒞X0,Xh\mathscr{C}^{h}\_{\!\boldsymbol{X}}\coloneqq\mathscr{C}\_{\!X\_{0},X\_{h}} and 𝒞𝑿,𝒀h≔𝒞X0,Yh\mathscr{C}^{h}\_{\!\boldsymbol{X},\boldsymbol{Y}}\coloneqq\mathscr{C}\_{\!X\_{0},Y\_{h}}, with 𝒞𝑿≔𝒞𝑿0\mathscr{C}\_{\!\boldsymbol{X}}\coloneqq\mathscr{C}^{0}\_{\!\boldsymbol{X}} and 𝒞𝑿,𝒀≔𝒞𝑿,𝒀0\mathscr{C}\_{\!\boldsymbol{X},\boldsymbol{Y}}\coloneqq\mathscr{C}^{0}\_{\!\boldsymbol{X},\boldsymbol{Y}}. Further, 𝑿=(Xk)\boldsymbol{X}=(X\_{k}) is a *weak white noise* (WWN) if it is weakly stationary, centered, with 𝔼​‖X0‖2>0\mathbb{E}\|X\_{0}\|^{2}>0, and 𝒞𝑿h=0\mathscr{C}^{h}\_{\!\boldsymbol{X}}=0 for all h≠0h\neq 0; and a *strong white noise* (SWN) is an i.i.d. WWN. For sequences (bn),(cn)⊂ℝ(b\_{n}),(c\_{n})\subset\mathbb{R}, bn≍cnb\_{n}\asymp c\_{n} (as n→∞n\to\infty) denotes asymptotic equivalence up to constants. Unless stated otherwise, all limits are taken as N→∞N\to\infty.

## 2 General model and assumptions

Let ℋ\mathcal{H} be a separable Hilbert space equipped with the inner product ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle.

###### Definition 2.1.

We call (Xk)k∈ℤ⊂ℋ(X\_{k})\_{k\in\mathbb{Z}}\subset\mathcal{H} an *operator-level ARCH(p)(p) process* (op-ARCH(p)(p)) if

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk=Σk1/2​(εk),Σk=Δ+∑i=1pαi​(Xk−i⊗2),k∈ℤ,\displaystyle X\_{k}=\Sigma^{1/2}\_{k}(\varepsilon\_{k}),\qquad\Sigma\_{k}=\Delta+\sum\_{i=1}^{p}\,\alpha\_{i}(X^{\otimes 2}\_{k-i}),\quad k\in\mathbb{Z},\allowdisplaybreaks |  | (2.1) |

where 𝛆=(εk)\boldsymbol{\varepsilon}=(\varepsilon\_{k}) is a SWN with covariance operator 𝒞𝛆\mathscr{C}\_{\boldsymbol{\varepsilon}}, p∈ℕ,p\in\mathbb{N}, Δ∈𝒮>0,\Delta\in\mathcal{S}\_{>0}, and αi:𝒮→𝒮\alpha\_{i}:\mathcal{S}\to\mathcal{S} are bounded linear operators with αi:𝒮≥0→𝒮≥0\alpha\_{i}:\mathcal{S}\_{\geq 0}\to\mathcal{S}\_{\geq 0} for all i=1,2,…,p,i=1,2,\dots,p, with αp≠0.\alpha\_{p}\neq 0.

As in the pw-fARCH framework, we call the parameter Δ\Delta the intercept term, and the parameters α1,…,αp\alpha\_{1},\dots,\alpha\_{p} the (op-)ARCH operators. Here, Δ\Delta is a deterministic, self-adjoint, positive definite H-S operator, and each αi\alpha\_{i} is a bounded and linear operator mapping H-S to H-S operators, preserving self-adjointness and non-negative definiteness. As a consequence, Σk\Sigma\_{k} is self-adjoint and positive definite. If ([2.1](#S2.E1 "In Definition 2.1. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model")) admits a strictly stationary solution with finite second moments, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼⁡[Xk⊗2|ℱk−1]=Σk1/2​𝒞𝜺​Σk1/2,k∈ℤ,\displaystyle\operatorname{\mathds{E}}\!\big[X^{\otimes 2}\_{k}\,\big|\,\mathcal{F}\_{k-1}\big]=\Sigma^{1/2}\_{k}\mathscr{C}\_{\boldsymbol{\varepsilon}}\Sigma^{1/2}\_{k},\quad k\in\mathbb{Z}, |  | (2.2) |

so that the process exhibits conditional heteroscedasticity. Note that the model remains well-defined if Δ\Delta is merely bounded linear rather than H-S, but since consistent estimation from finite samples requires compactness, we keep the slightly stronger H-S assumption. The formula ([2.2](#S2.E2 "In 2 General model and assumptions ‣ An operator-level ARCH Model")) highlights the standard identifiability issue in GARCH models: neither Σk\Sigma\_{k} nor its defining parameters are uniquely determined by ([2.2](#S2.E2 "In 2 General model and assumptions ‣ An operator-level ARCH Model")), since unitary transformations of Σk\Sigma\_{k} and 𝒞𝜺\mathscr{C}\_{\boldsymbol{\varepsilon}} leave the conditional covariance unchanged. In multivariate GARCH models this is avoided by imposing 𝒞𝜺=𝕀\mathscr{C}\_{\boldsymbol{\varepsilon}}=\mathbb{I}, identifying Σk\Sigma\_{k} as the conditional covariance operator. In infinite-dimensional Hilbert spaces, however, the identity map 𝕀\mathbb{I} is not compact and this is not feasible. Instead, if 𝒞𝜺\mathscr{C}\_{\boldsymbol{\varepsilon}} is any known injective covariance operator, then ([2.2](#S2.E2 "In 2 General model and assumptions ‣ An operator-level ARCH Model")) uniquely identifies Σk\Sigma\_{k}. Hence, throughout we assume:

###### Assumption 2.1.

The covariance operator 𝒞𝛆\mathscr{C}\_{\boldsymbol{\varepsilon}} is known and injective.

When for example ℋ=L2​[0,1]\mathcal{H}=L^{2}[0,1], and

|  |  |  |
| --- | --- | --- |
|  | 𝒞𝜺​(f)​(t)=∫01Cε​(t,s)​f​(s)​𝑑s,\mathscr{C}\_{\boldsymbol{\varepsilon}}(f)(t)=\int\_{0}^{1}C\_{\varepsilon}(t,s)f(s)ds, |  |

for a covariance kernel CεC\_{\varepsilon}, natural choices satisfying the above are Brownian motion errors, where Cε​(t,s)=σ2​min⁡{t,s}C\_{\varepsilon}(t,s)=\sigma^{2}\min\{t,s\}, and Ornstein–Uhlenbeck errors, where Cε​(t,s)=σ​exp⁡(−θ​|t−s|).C\_{\varepsilon}(t,s)=\sigma\exp(-\theta|t-s|). Although the conditional covariance operator does not coincide with Σk\Sigma\_{k}, it can be easily recovered from it using the known 𝒞𝜺\mathscr{C}\_{\boldsymbol{\varepsilon}}.

In pw-f(G)ARCH models of higher order, Markovian state-space forms have been used to establish stationarity (cf. Cerovecki et al., [2019](#bib.bib10); Kühnert, [2020](#bib.bib25)). Our op-ARCH(p)(p) process also admits a Markovian representation, though in a more intricate form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk⊗2,[p]=Υk​(𝚫+𝚿​(Xk−1⊗2,[p])),k∈ℤ.\displaystyle X^{\otimes 2,[p]}\_{\!k}=\Upsilon\_{\!k}\big(\boldsymbol{\Delta}+\boldsymbol{\Psi}(X^{\otimes 2,[p]}\_{\!k-1})\big),\quad k\in\mathbb{Z}. |  | (2.3) |

Here Xk⊗2,[p]X^{\otimes 2,[p]}\_{\!k} collects the past pp “squared” functions, so

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk⊗2,[p]≔(Xk⊗2,Xk−1⊗2,…,Xk−p+1⊗2)⊤,\displaystyle X^{\otimes 2,[p]}\_{\!k}\coloneqq\big(X^{\otimes 2}\_{k},X^{\otimes 2}\_{k-1},\dots,X^{\otimes 2}\_{k-p+1}\big)^{\top}\!, |  | (2.4) |

with constant part 𝚫≔(Δ,0,…,0)⊤\boldsymbol{\Delta}\coloneqq(\Delta,0,\dots,0)^{\!\top}\!, 𝚿:𝒮≥0p→𝒮≥0p\boldsymbol{\Psi}:\mathcal{S}^{p}\_{\geq 0}\to\mathcal{S}^{p}\_{\geq 0} refers to the operator-valued matrix

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚿≔[α1⋯⋯⋯αp𝕀0⋯⋯00𝕀0⋯0⋮⋱⋱⋱⋮0⋯0𝕀0],\displaystyle\boldsymbol{\Psi}\coloneqq\begin{bmatrix}\alpha\_{1}&\cdots&\cdots&\cdots&\alpha\_{p}\\ \mathbb{I}&0&\cdots&\cdots&0\\ 0&\mathbb{I}&0&\cdots&0\\ \vdots&\ddots&\ddots&\ddots&\vdots\\ 0&\cdots&0&\mathbb{I}&0\end{bmatrix}, |  | (2.5) |

and Υk:𝒮≥0p→𝒮≥0p\Upsilon\_{\!k}:\mathcal{S}^{p}\_{\geq 0}\to\mathcal{S}^{p}\_{\geq 0} refers to the map defined by Υk​(A)≔(A11/2​εk⊗2​A11/2,A2,…,Ap)⊤\Upsilon\_{\!k}(A)\coloneqq(A\_{1}^{1/2}\varepsilon^{\otimes 2}\_{k}A\_{1}^{1/2},A\_{2},\dots,A\_{p})^{\top} for A=(A1,…,Ap)⊤.A=(A\_{1},\dots,A\_{p})^{\top}\!. Although the representation ([2.3](#S2.E3 "In 2 General model and assumptions ‣ An operator-level ARCH Model")) is natural, establishing stationarity is challenging: the nonlinearity of Υk\Upsilon\_{k} rules out the use of a top Lyapunov exponent (cf. Kingman, [1973](#bib.bib22); Liggett, [1985](#bib.bib31)), and the geometric moment contraction condition of Wu and Shao ([2004](#bib.bib41)), as employed in Hörmann et al. ([2013](#bib.bib16)) for pw-fARCH models, does not appear applicable to the transformation A↦Υk​(𝚫+𝚿​(A))A\mapsto\Upsilon\_{k}(\boldsymbol{\Delta}+\boldsymbol{\Psi}(A)). Nevertheless, a strictly stationary solution can still be constructed algorithmically (see Francq and Zakoïan, [2019](#bib.bib13), p. 289 for the vech\mathrm{vech} (G)ARCH case). A more tractable model that is amenable to theoretical analysis will be introduced below.

Several of the results below, including crucially methods to estimate the operators in ([2.1](#S2.E1 "In Definition 2.1. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model")), are simplified considerably by assuming the following:

###### Assumption 2.2.

𝒞𝜺\mathscr{C}\_{\boldsymbol{\varepsilon}} commutes with Σk\Sigma\_{k} in ([2.1](#S2.E1 "In Definition 2.1. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model")) for all k.k.

Assumptions [2.1](#S2.Thmassumption1 "Assumption 2.1. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model")–[2.2](#S2.Thmassumption2 "Assumption 2.2. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model") imply that Δ\Delta and the ranges of α1,…,αp\alpha\_{1},\dots,\alpha\_{p} are diagonalizable with respect to the (known) eigenbasis of 𝒞ε\mathscr{C}\_{\varepsilon}. In finite-dimensional (G)ARCH models, this is typically ensured by taking 𝒞ε=𝕀\mathscr{C}\_{\varepsilon}=\mathbb{I}. The choice of 𝒞ε\mathscr{C}\_{\varepsilon} may thus be viewed as selecting the basis that diagonalizes the conditional covariance. In the results below, we explicitly state which arguments rely on this assumption. Moreover, to delve more deeply into the structure of the op-ARCH model, and provide comparisons to other multivariate GARCH models, we use the notation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜶:𝒮≥0p→𝒮≥0,A=(A1,…,Ap)⊤↦𝜶​(A)=∑i=1pαi​(Ai),\displaystyle\boldsymbol{\alpha}:\mathcal{S}^{p}\_{\geq 0}\to\mathcal{S}\_{\geq 0},~A=(A\_{1},\dots,A\_{p})^{\top}\mapsto\boldsymbol{\alpha}(A)=\sum^{p}\_{i=1}\alpha\_{i}(A\_{i}), |  | (2.6) |

and assume the following.

###### Assumption 2.3.

The operator 𝛂\boldsymbol{\alpha} is H-S.

Let (ej)j=1∞(e\_{j})\_{j=1}^{\infty} be the eigenbasis associated to the covariance operator 𝒞𝜺\mathscr{C}\_{\boldsymbol{\varepsilon}}. Assumption [2.3](#S2.Thmassumption3 "Assumption 2.3. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model"), together with the fact that the space of H-S operators from 𝒮p\mathcal{S}^{p} to 𝒮\mathcal{S} is a separable Hilbert space yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜶=∑i=1p∑j=1∞∑k=1∞∑ℓ=1∞∑m=1∞ai​j​k​ℓ​m​[Ei​j​k⊗𝒮(eℓ⊗em)],\displaystyle\boldsymbol{\alpha}=\sum\_{i=1}^{p}\sum\_{j=1}^{\infty}\sum\_{k=1}^{\infty}\sum\_{\ell=1}^{\infty}\sum\_{m=1}^{\infty}\,a\_{ijk\ell m}\big[E\_{ijk}\!\otimes\_{\mathcal{S}}\!(e\_{\ell}\otimes e\_{m})\big], |  | (2.7) |

where Ei​j​kE\_{ijk} is the vector placing ej⊗eke\_{j}\otimes e\_{k} at position ii and zeros elsewhere. By the definitions of Σk\Sigma\_{k} in the op-ARCH(p)(p) equation and 𝜶\boldsymbol{\alpha}, and with ai​j​ℓ≔ai​j​j​ℓ​ℓ,a\_{ij\ell}\coloneqq a\_{ijj\ell\ell}, this leads to the simplified representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜶=∑i=1p∑j=1∞∑ℓ=1∞ai​j​ℓ​[Ei​j​j⊗𝒮(eℓ⊗eℓ)].\displaystyle\boldsymbol{\alpha}=\sum\_{i=1}^{p}\sum\_{j=1}^{\infty}\sum\_{\ell=1}^{\infty}\,a\_{ij\ell}\big[E\_{ijj}\!\otimes\_{\mathcal{S}}\!(e\_{\ell}\otimes e\_{\ell})\big]. |  | (2.8) |

Each component αi\alpha\_{i} of 𝜶\boldsymbol{\alpha} maps 𝒮≥0\mathcal{S}\_{\geq 0} to 𝒮≥0\mathcal{S}\_{\geq 0}, i.e. non-negative definite, self-adjoint H-S operators into itself. Thus, for any A=(A1,…,Ap)⊤∈𝒮≥0pA=(A\_{1},\dots,A\_{p})^{\top}\in\mathcal{S}^{p}\_{\geq 0}, 𝜶​(A)\boldsymbol{\alpha}(A) is self-adjoint and non-negative definite under mild conditions. To establish the latter, note that we need

|  |  |  |
| --- | --- | --- |
|  | ⟨𝜶​(A)​(x),x⟩=∑i=1p∑j=1∞∑ℓ=1∞ai​j​ℓ​⟨Ai​(ej),ej⟩​⟨x,eℓ⟩2≥ 0,x∈ℋ.\big\langle\boldsymbol{\alpha}(A)(x),x\big\rangle\;=\;\sum^{p}\_{i=1}\sum^{\infty}\_{j=1}\sum^{\infty}\_{\ell=1}\,a\_{ij\ell}\langle A\_{i}(e\_{j}),e\_{j}\rangle\langle x,e\_{\ell}\rangle^{2}\;\geq\;0,\quad x\in\mathcal{H}. |  |

Since ⟨Ai​(ej),ej⟩≥0\langle A\_{i}(e\_{j}),e\_{j}\rangle\geq 0 for all i,ji,j, a sufficient condition for 𝜶​(A)\boldsymbol{\alpha}(A) to be non-negative definite is ai​j​ℓ≥0a\_{ij\ell}\geq 0 for all i,j,ℓ.i,j,\ell.

## 3 CCC-op-ARCH model and structure

As indicated above, we now introduce a more parsimonious model. The expansion ([2.8](#S2.E8 "In 2 General model and assumptions ‣ An operator-level ARCH Model")) is the most general form of the op-ARCH operators satisfying Assumption [2.2](#S2.Thmassumption2 "Assumption 2.2. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model"). In analogy to multivariate GARCH, this is akin to a “VEC-ARCH” specification (see Francq and Zakoïan, [2019](#bib.bib13), Ch. 10.2.2). Although such a model allows for a flexible serial dependence structure, it is often considered overparameterized, challenging to estimate, and theoretically difficult to analyze. A more tractable model is obtained by retaining only the diagonal terms in ([2.8](#S2.E8 "In 2 General model and assumptions ‣ An operator-level ARCH Model")). This section is devoted to the discussion of such a model, where Assumptions [2.1](#S2.Thmassumption1 "Assumption 2.1. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model")–[2.3](#S2.Thmassumption3 "Assumption 2.3. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model") hold.

###### Definition 3.1.

We say that a process (Xk)k∈ℤ(X\_{k})\_{k\in\mathbb{Z}} is a *Constant Conditional Correlation operator-level ARCH(p)(p)* (CCC-op-ARCH(p)(p)) process if ([2.1](#S2.E1 "In Definition 2.1. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model")) holds with

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜶=∑i=1p∑ℓ=1∞ai​ℓ​ℓ​[Ei​ℓ​ℓ⊗𝒮(eℓ⊗eℓ)].\displaystyle\boldsymbol{\alpha}=\sum^{p}\_{i=1}\sum^{\infty}\_{\ell=1}\,a\_{i\ell\ell}\big[E\_{i\ell\ell}\!\otimes\_{\mathcal{S}}\!(e\_{\ell}\otimes e\_{\ell})\big]. |  | (3.1) |

This is called a “CCC” model since it assumes that 𝜶\boldsymbol{\alpha} only depends on the diagonal-terms in its expansion, while the components of the process XiX\_{i} remain “conditionally correlated” through their common dependence on 𝒞ε\mathscr{C}\_{\varepsilon}. We note that one might also consider a CCC model of the form ([2.1](#S2.E1 "In Definition 2.1. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model")) where for a compact covariance operator 𝒢\mathscr{G}, Σk=Hk1/2​𝒢​Hk1/2\Sigma\_{k}=H\_{k}^{1/2}\mathscr{G}H\_{k}^{1/2}, and HkH\_{k} satisfies the recursion on the right-hand side of ([2.1](#S2.E1 "In Definition 2.1. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model")). Under the commutativity Assumption [2.2](#S2.Thmassumption2 "Assumption 2.2. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model") and with 𝜶\boldsymbol{\alpha} following ([3.1](#S3.E1 "In Definition 3.1. ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")), this reduces to the given CCC model.

Throughout this section, (Xk)(X\_{k}) is assumed to be a CCC-op-ARCH(p)(p) model for some p∈ℕ.p\in\mathbb{N}. One of the benefits of this model is that there exists a linear Markovian form associated with it. To be precise, we have (see also Example [B.1](#A2.Thmexample1 "Example B.1. ‣ Appendix B Notes ‣ An operator-level ARCH Model"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk,d⊗2,[p]=𝚫k+𝚿k​(Xk−1,d⊗2,[p]),k∈ℤ,\displaystyle X^{\otimes 2,[p]}\_{\!k,\mathrm{d}}=\boldsymbol{\Delta}\_{k}+\boldsymbol{\Psi}\_{\!k}\big(X^{\otimes 2,[p]}\_{\!k-1,\mathrm{d}}\big),\quad k\in\mathbb{Z}, |  | (3.2) |

where Xk,d⊗2,[p]X^{\otimes 2,[p]}\_{\!k,\mathrm{d}} is the diagonal part of Xk⊗2,[p]X^{\otimes 2,[p]}\_{\!k} in ([2.4](#S2.E4 "In 2 General model and assumptions ‣ An operator-level ARCH Model")), which is for each component defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk−i+1,d⊗2≔∑ℓ=1∞⟨Xk−i+1,eℓ⟩2​(eℓ⊗eℓ),i∈{1,…,p},k∈ℤ.\displaystyle X^{\otimes 2}\_{\!k-i+1,\mathrm{d}}\coloneqq\sum^{\infty}\_{\ell=1}\,\langle X\_{k-i+1},e\_{\ell}\rangle^{2}(e\_{\ell}\otimes e\_{\ell}),\quad i\in\{1,...,p\},\;~k\in\mathbb{Z}. |  | (3.3) |

Here 𝚫k≔(ψk​(Δ),0,…,0)⊤,\boldsymbol{\Delta}\_{k}\coloneqq(\psi\_{k}(\Delta),0,\dots,0)^{\top}\!, and 𝚿k\boldsymbol{\Psi}\_{\!k} has the same form as 𝚿\boldsymbol{\Psi} in ([2.5](#S2.E5 "In 2 General model and assumptions ‣ An operator-level ARCH Model")) with each αi\alpha\_{i} replaced by ψk∘αi,\psi\_{k}\circ\alpha\_{i}, where ∘\circ refers to composition, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψk​(B)≔∑j=1∞⟨εk,ej⟩2​bj​(ej⊗ej), for ​B=∑j=1∞bj​(ej⊗ej)∈𝒮≥0.\displaystyle\psi\_{k}(B)\coloneqq\sum^{\infty}\_{j=1}\,\langle\varepsilon\_{k},e\_{j}\rangle^{2}b\_{j}(e\_{j}\otimes e\_{j}),\quad\mbox{ for }B=\sum^{\infty}\_{j=1}b\_{j}(e\_{j}\otimes e\_{j})\in\mathcal{S}\_{\geq 0}. |  | (3.4) |

It should be noted that a host of other potential, simplified models starting from ([2.8](#S2.E8 "In 2 General model and assumptions ‣ An operator-level ARCH Model")) might be considered. For ease of presentation and due to the empirical performance of the CCC-op-ARCH(p)(p) model in our analyses below, we have chosen to focus on this case. We discuss this and avenues for future research in Section [7](#S7 "7 Discussion ‣ An operator-level ARCH Model").

### 3.1 Strict stationarity

To deduce conditions under which this model admits a stationary solution, we introduce a *top Lyapunov exponent* (cf. Kingman, [1973](#bib.bib22); Liggett, [1985](#bib.bib31)). To this end, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ:ℬ𝒮≥0,dp→[0,∞),τ​(B)≔sup‖A‖𝒮p≤1,A∈𝒮≥0,dp‖B​(A)‖𝒮,\displaystyle\tau:\mathcal{B}\_{\mathcal{S}^{p}\_{\geq 0,\mathrm{d}}}\to[0,\infty),\quad\tau(B)\coloneqq\sup\_{\|A\|\_{\mathcal{S}^{p}}\leq 1,\,A\in\mathcal{S}^{p}\_{\geq 0,\mathrm{d}}}\|B(A)\|\_{\mathcal{S}}, |  | (3.5) |

where 𝒮≥0,d⊂𝒮≥0\mathcal{S}\_{\geq 0,\mathrm{d}}\subset\mathcal{S}\_{\geq 0} denotes the subset of non-negative, self-adjoint H-S operators with the diagonal form A=∑jaj​(ej⊗ej)A=\sum\_{j}a\_{j}(e\_{j}\otimes e\_{j}), and ℬ𝒮≥0,dp\mathcal{B}\_{\mathcal{S}^{p}\_{\geq 0,\mathrm{d}}} the set of bounded linear operators on 𝒮≥0,d.\mathcal{S}\_{\geq 0,\mathrm{d}}. Although the functional τ\tau does not define a norm, it satisfies several useful properties for our analysis. It is dominated by the operator norm, τ​(B)≤‖B‖ℒ\tau(B)\leq\|B\|\_{\mathcal{L}}, compatible with the H-S norm so that ‖B​(A)‖𝒮≤τ​(B)​‖A‖𝒮,\|B(A)\|\_{\mathcal{S}}\leq\tau(B)\|A\|\_{\mathcal{S}}, and sub-multiplicative, τ​(B1∘B2)≤τ​(B1)​τ​(B2)\tau(B\_{1}\circ B\_{2})\leq\tau(B\_{1})\tau(B\_{2}).

###### Proposition 3.1.

The *top Lyapunov exponent* defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ≔limk→∞1k​ln⁡τ​(𝚿k∘𝚿k−1∘⋯∘𝚿1)=limk→∞1k​𝔼⁡ln⁡τ​(𝚿k∘𝚿k−1∘⋯∘𝚿1),\displaystyle\gamma\coloneqq\lim\_{k\to\infty}\frac{1}{k}\ln\tau\big(\boldsymbol{\Psi}\_{\!k}\circ\boldsymbol{\Psi}\_{\!k-1}\circ\cdots\circ\boldsymbol{\Psi}\_{\!1}\big)\;=\;\lim\_{k\to\infty}\frac{1}{k}\operatorname{\mathds{E}}\ln\tau\big(\boldsymbol{\Psi}\_{\!k}\circ\boldsymbol{\Psi}\_{\!k-1}\circ\cdots\circ\boldsymbol{\Psi}\_{\!1}\big), |  | (3.6) |

exists with γ∈[−∞,∞)\gamma\in[-\infty,\infty), where the first limit holds almost surely. Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ=infk∈ℕ1k​𝔼⁡ln⁡τ​(𝚿k∘𝚿k−1∘⋯∘𝚿1).\displaystyle\gamma=\inf\_{k\in\mathbb{N}}\frac{1}{k}\operatorname{\mathds{E}}\ln\tau\big(\boldsymbol{\Psi}\_{\!k}\circ\boldsymbol{\Psi}\_{\!k-1}\circ\cdots\circ\boldsymbol{\Psi}\_{\!1}\big). |  | (3.7) |

###### Theorem 3.1.

If

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ<0,\displaystyle\gamma<0, |  | (3.8) |

the CCC-op-ARCH(p)(p) process (Xk)(X\_{k}) admits a strictly stationary, causal, and almost surely unique solution. The same holds for the associated process (Σk)(\Sigma\_{k}).

The condition ([3.8](#S3.E8 "In Theorem 3.1. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) is difficult to verify in practice, even with known, relatively simple, operators α1,…,αp\alpha\_{1},...,\alpha\_{p}. The following two sufficient conditions are more tractable.

###### Proposition 3.2.

Condition ([3.8](#S3.E8 "In Theorem 3.1. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) is satisfied if, for some n∈ℕn\in\mathbb{N} and ν>0\nu>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼⁡τν​(𝚿n∘𝚿n−1∘⋯∘𝚿1)< 1.\displaystyle\operatorname{\mathds{E}}\tau^{\nu}\big(\boldsymbol{\Psi}\_{\!n}\circ\boldsymbol{\Psi}\_{\!n-1}\circ\,\cdots\,\circ\boldsymbol{\Psi}\_{\!1}\big)<\,1.\allowdisplaybreaks |  | (3.9) |

More explicitly, ([3.9](#S3.E9 "In Proposition 3.2. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) is satisfied with n=pn=p and ν=1\nu=1 if

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝜶‖ℒ​𝔼⁡‖ε0‖2​∑ℓ=1pℓ​(‖𝜶‖ℒ​𝔼⁡‖ε0‖2)p−ℓ<1.\displaystyle\|\boldsymbol{\alpha}\|\_{\mathcal{L}}\operatorname{\mathds{E}}\!\|\varepsilon\_{0}\|^{2}\sum^{p}\_{\ell=1}\,\ell\big(\|\boldsymbol{\alpha}\|\_{\mathcal{L}}\operatorname{\mathds{E}}\!\|\varepsilon\_{0}\|^{2}\big)^{p-\ell}<1.\allowdisplaybreaks |  | (3.10) |

###### Remark 3.1.

* (a)

  In contrast to real-valued (G)ARCH processes (cf. Francq and Zakoïan, [2019](#bib.bib13), Theorem 2.4), the condition ([3.8](#S3.E8 "In Theorem 3.1. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) is not necessary, since norms on infinite-dimensional spaces are not equivalent (cf. Cerovecki et al., [2019](#bib.bib10), Remark 1).
* (b)

  The sufficient condition ([3.10](#S3.E10 "In Proposition 3.2. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) is convenient, but relatively crude. A sharper analysis of this constraint may further relax the requirement, which we do not pursue here. Further, as each 𝚿k\boldsymbol{\Psi}\_{\!k} contains identity maps—and hence has norm at least 11—([3.10](#S3.E10 "In Proposition 3.2. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) can, by the definition of 𝚿k\boldsymbol{\Psi}\_{\!k}, only hold for compositions 𝚿n∘𝚿n−1∘⋯∘𝚿1\boldsymbol{\Psi}\_{\!n}\circ\boldsymbol{\Psi}\_{\!n-1}\circ\cdots\circ\boldsymbol{\Psi}\_{\!1} with n≥pn\geq p (see the proof in Section [C](#A3 "Appendix C Proofs ‣ An operator-level ARCH Model")). For simplicity, we focus on the case n=pn=p.

###### Example 3.1.

Suppose p=1p=1. Then considering ([3.9](#S3.E9 "In Proposition 3.2. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) with n=1n=1 leads to the sufficient stationarity condition

|  |  |  |
| --- | --- | --- |
|  | 𝔼⁡[supj≥1a1​j​jν​⟨ε1,ej⟩2​ν]<1,\operatorname{\mathds{E}}\left[\,\sup\_{j\geq 1}a\_{1jj}^{\nu}\langle\varepsilon\_{1},e\_{j}\rangle^{2\nu}\right]<1, |  |

for some ν>0\nu>0. Moreover, one may see from this that

|  |  |  |
| --- | --- | --- |
|  | 𝔼⁡τν​(𝚿1)≤‖α1‖ℒν​𝔼⁡[supj≥1⟨ε1,ej⟩2​ν].\operatorname{\mathds{E}}\tau^{\nu}\big(\boldsymbol{\Psi}\_{\!1}\big)\leq\|{\alpha}\_{1}\|\_{\mathcal{L}}^{\nu}\operatorname{\mathds{E}}\left[\,\sup\_{j\geq 1}\langle\varepsilon\_{1},e\_{j}\rangle^{2\nu}\right]. |  |

With ν=1\nu=1, this leads to the sufficient condition ‖α1‖ℒ​‖𝒞ε‖ℒ<1\|{\alpha}\_{1}\|\_{\mathcal{L}}\|\mathscr{C}\_{\varepsilon}\|\_{\mathcal{L}}<1.

### 3.2 Existence of moments, weak dependence, and weak stationarity

Under suitable conditions, CCC-op-ARCH processes possess finite moments and display weak serial dependence. In particular, they are LpL^{p}-mm-approximable, a weak dependence notion for functional data initially introduced in Hörmann and Kokoszka ([2010](#bib.bib17)). A process (Yk)k∈ℤ⊂ℋ(Y\_{k})\_{k\in\mathbb{Z}}\subset\mathcal{H} is *LpL^{p}-mm-approximable* if (a) it admits a Bernoulli shift representation, i.e. Yk=f​(εk,εk−1,…)Y\_{k}=f(\varepsilon\_{k},\varepsilon\_{k-1},\ldots) for some i.i.d. sequence (εk)k∈ℤ(\varepsilon\_{k})\_{k\in\mathbb{Z}} taking values in a measurable space 𝕊\mathbb{S}, and a measurable mapping f:𝕊ℕ→ℋ,f:\mathbb{S}^{\mathbb{N}}\to\mathcal{H}, and (b) with Yk(m)≔f​(εk,…,εk−m+1,εk−m′,εk−m−1′,…)Y^{(m)}\_{k}\!\coloneqq f(\varepsilon\_{k},\ldots,\varepsilon\_{k-m+1},\varepsilon^{\prime}\_{k-m},\varepsilon^{\prime}\_{k-m-1},\ldots), where (εk′)k∈ℤ(\varepsilon^{\prime}\_{k})\_{k\in\mathbb{Z}} is an independent sequence of copies of ε0,\varepsilon\_{0}, and with ξY,p​(m)=(𝔼⁡‖Y0−Y0(m)‖ℋp)1/p\xi\_{Y,p}(m)=(\operatorname{\mathds{E}}\!\|Y\_{0}\!-Y^{(m)}\_{0}\|\_{\mathcal{H}}^{p})^{1/p},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑m=1∞ξY,p​(m)<∞.\displaystyle\sum^{\infty}\_{m=1}\xi\_{Y,p}(m)<\infty. |  | (3.11) |

According to (a), LpL^{p}-m-approximable processes are strictly stationary and ergodic. If ([3.11](#S3.E11 "In 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) holds with p≥2p\geq 2, then the process YkY\_{k} satisfies for example the central limit theorem. This condition is satisfied by many standard models, including functional AR and linear processes (as illustrated in Hörmann and Kokoszka, [2010](#bib.bib17)), and also pw-(G)ARCH models. The following result provides sufficient conditions for this property and for the existence of finite moments. In this result, the notation ∥⋅∥4\|\cdot\|\_{4} appears, referring to the norm of *Schatten class operators of order 4* (see Section [A](#A1 "Appendix A Preliminaries ‣ An operator-level ARCH Model")).

###### Proposition 3.3.

Let ([3.9](#S3.E9 "In Proposition 3.2. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) and (εk)⊂Lℋ2​ν(\varepsilon\_{k})\subset L^{2\nu}\_{\mathcal{H}} for the same ν\nu hold. Then:

* (a)

  𝔼⁡‖X0⊗2‖𝒮ν=𝔼⁡‖X0‖2​ν<∞\operatorname{\mathds{E}}\!\|X^{\otimes 2}\_{0}\|^{\nu}\_{\mathcal{S}}=\operatorname{\mathds{E}}\!\|X\_{0}\|^{2\nu}<\infty and 𝔼⁡‖Σ01/2‖42​ν=𝔼⁡‖Σ0‖𝒮ν<∞.\operatorname{\mathds{E}}\!\|\Sigma^{1/2}\_{0}\|^{2\nu}\_{4}=\operatorname{\mathds{E}}\!\|\Sigma\_{0}\|^{\nu}\_{\mathcal{S}}<\infty.
* (b)

  The processes XkX\_{k} and Σk1/2\Sigma^{1/2}\_{k} are L2​νL^{2\nu}-mm-, and Yk=Xk⊗2Y\_{k}=X^{\otimes 2}\_{k} and Yk=ΣkY\_{k}=\Sigma\_{k} are LνL^{\nu}-mm-approximable, each with geometrically decaying approximation errors, i.e. ξX,2​ν​(m)≤c†​ρm\xi\_{X,2\nu}(m)\leq c\_{\dagger}\rho^{m} and ξY,ν​(m)≤c†​ρm\xi\_{Y,\nu}(m)\leq c\_{\dagger}\rho^{m} for some c†>0c\_{\dagger}>0 and ρ∈(0,1)\rho\in(0,1).

###### Proposition 3.4.

Let (Xk)(X\_{k}) be a weakly stationary CCC-op-ARCH(p)(p) process. Then, (Xk)(X\_{k}) is a weak white noise. Further,
μ𝚺≔𝔼⁡(Σ0)=𝔼⁡(Σk)\mu\_{\boldsymbol{\Sigma}}\coloneqq\operatorname{\mathds{E}}(\Sigma\_{0})=\operatorname{\mathds{E}}(\Sigma\_{k}) for all k,k, with

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ𝚺=Δ+∑i=1pαi​(𝒞𝑿).\displaystyle\mu\_{\boldsymbol{\Sigma}}=\Delta+\sum^{p}\_{i=1}\alpha\_{i}(\mathscr{C}\_{\!\boldsymbol{X}}). |  | (3.12) |

In addition, if Assumption [2.2](#S2.Thmassumption2 "Assumption 2.2. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model") and also

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖∑i=1pαi​(𝒞𝜺)‖ℒ<1\displaystyle\left\|\,\sum^{p}\_{i=1}\alpha\_{i}(\mathscr{C}\_{\boldsymbol{\varepsilon}})\,\right\|\_{\mathcal{L}}<1 |  | (3.13) |

are satisfied, then μ𝚺\mu\_{\boldsymbol{\Sigma}} has the more explicit representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ𝚺=(𝕀−∑i=1pαi​(𝒞𝜺))−1​(Δ).\displaystyle\mu\_{\boldsymbol{\Sigma}}=\bigg(\boldsymbol{\mathbb{I}}-\sum^{p}\_{i=1}\,\alpha\_{i}(\mathscr{C}\_{\boldsymbol{\varepsilon}})\bigg)^{\!-1}(\Delta). |  | (3.14) |

###### Remark 3.2.

* (a)

  Eq. ([3.14](#S3.E14 "In Proposition 3.4. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) parallels the classical formula for the unconditional variance of univariate (G)ARCH models (cf. Francq and Zakoïan, [2019](#bib.bib13)). Moreover, ([3.13](#S3.E13 "In Proposition 3.4. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) may still hold even when ∑i=1p‖αi‖ℒ≥1\sum\_{i=1}^{p}\|\alpha\_{i}\|\_{\mathcal{L}}\geq 1, since ‖𝒞𝜺‖ℒ<1\|\mathscr{C}\_{\boldsymbol{\varepsilon}}\|\_{\mathcal{L}}<1 for most relevant innovation processes (e.g., the standard Brownian motion).
* (b)

  The moment condition in Proposition [3.3](#S3.Thmproposition3 "Proposition 3.3. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model") for ν≤1\nu\leq 1 is stated only for completeness and is redundant, since finite second moments of ε0\varepsilon\_{0} were already assumed.

### 3.3 Examples

We illustrate the above results with two classes of op-ARCH processes on ℋ=L2​[0,1]\mathcal{H}=L^{2}[0,1], where (εk)(\varepsilon\_{k}) denotes an i.i.d. sequence of standard Brownian motions on [0,1][0,1].

###### Example 3.2.

Let p∈ℕp\in\mathbb{N}. Consider the integral operator Δ\Delta with kernel min⁡(t,s)\min(t,s), s,t∈[0,1]s,t\in[0,1], and define αi​(A)=ai​A\alpha\_{i}(A)=a\_{i}A for A∈𝒮A\in\mathcal{S} and scalars ai≥0a\_{i}\geq 0 for 1≤i<p,1\leq i<p, and ap≠0.a\_{p}\neq 0. Then Δ∈𝒮>0\Delta\in\mathcal{S}\_{>0} and each αi∈ℒ𝒮\alpha\_{i}\in\mathcal{L}\_{\mathcal{S}} maps 𝒮≥0\mathcal{S}\_{\geq 0} to 𝒮≥0\mathcal{S}\_{\geq 0}.

* (a)

  Let p=1.p=1. Since 𝔼​‖ε0‖2=‖𝒞𝜺‖𝒩=1/2\mathbb{E}\|\varepsilon\_{0}\|^{2}=\|\mathscr{C}\_{\boldsymbol{\varepsilon}}\|\_{\mathcal{N}}=1/2 and ‖𝜶‖ℒ=a1\|\boldsymbol{\alpha}\|\_{\mathcal{L}}=a\_{1}, condition ([3.10](#S3.E10 "In Proposition 3.2. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) holds whenever a1<2a\_{1}<2. In this case, Proposition [3.3](#S3.Thmproposition3 "Proposition 3.3. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model") yields 𝔼​‖X0‖2<∞\mathbb{E}\|X\_{0}\|^{2}<\infty and 𝔼​‖Σ0‖𝒮<∞\mathbb{E}\|\Sigma\_{0}\|\_{\mathcal{S}}<\infty, so (Xk)(X\_{k}) is weakly stationary, a WWN by Proposition [3.4](#S3.Thmproposition4 "Proposition 3.4. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model"), and L2L^{2}-mm-approximable.
* (b)

  Let p=3.p=3. Here, ‖𝜶‖ℒ≤a≔a1+a2+a3\|\boldsymbol{\alpha}\|\_{\mathcal{L}}\leq a\coloneqq a\_{1}+a\_{2}+a\_{3}. Hence, ([3.10](#S3.E10 "In Proposition 3.2. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) is satisfied if

  |  |  |  |
  | --- | --- | --- |
  |  | a​(a2+4​a+12)<8,a(a^{2}+4a+12)<8, |  |

  which holds roughly for a≤0.551a\leq 0.551.

###### Example 3.3.

In the following, let

|  |  |  |
| --- | --- | --- |
|  | Δ=∑ℓ=1∞dℓ​(eℓ⊗eℓ),αi=∑ℓ=1∞ai​ℓ​ℓ​(eℓ⊗eℓ)⊗𝒮(eℓ⊗eℓ),1≤i≤p,\Delta=\sum\_{\ell=1}^{\infty}d\_{\ell}(e\_{\ell}\!\otimes\!e\_{\ell}),\quad\alpha\_{i}=\sum\_{\ell=1}^{\infty}a\_{i\ell\ell}\,(e\_{\ell}\!\otimes\!e\_{\ell})\!\otimes\_{\mathcal{S}}\!(e\_{\ell}\!\otimes\!e\_{\ell}),\quad 1\leq i\leq p, |  |

where (dℓ)(d\_{\ell}) and (ai​ℓ​ℓ)ℓ(a\_{i\ell\ell})\_{\ell} are positive, strictly decreasing, square-summable sequences. Then

|  |  |  |
| --- | --- | --- |
|  | Σk=∑ℓ=1∞Zk,ℓ​(eℓ⊗eℓ),Xk=∑ℓ=1∞Zk,ℓ1/2​⟨εk,eℓ⟩​eℓ,\Sigma\_{k}=\sum\_{\ell=1}^{\infty}Z\_{k,\ell}(e\_{\ell}\!\otimes\!e\_{\ell}),\quad X\_{k}=\sum\_{\ell=1}^{\infty}Z^{1/2}\_{k,\ell}\,\langle\varepsilon\_{k},e\_{\ell}\rangle e\_{\ell}, |  |

with

|  |  |  |
| --- | --- | --- |
|  | Zk,ℓ=dℓ+∑i=1pai​ℓ​ℓ​Zk−i,ℓ​⟨εk−i,eℓ⟩2.Z\_{k,\ell}=d\_{\ell}+\sum\_{i=1}^{p}a\_{i\ell\ell}\,Z\_{k-i,\ell}\,\langle\varepsilon\_{k-i},e\_{\ell}\rangle^{2}. |  |

To highlight structural aspects, let p=1p=1 and assume a1​ℓ​ℓ=a​ℓ−2a\_{1\ell\ell}=a\ell^{-2} for some a>0a>0. Then

|  |  |  |
| --- | --- | --- |
|  | ‖𝜶‖ℒ​𝔼​‖ε0‖2=supℓ≥1|a1​ℓ​ℓ|/2=a/2,\|\boldsymbol{\alpha}\|\_{\mathcal{L}}\,\mathbb{E}\|\varepsilon\_{0}\|^{2}\;=\;\sup\_{\ell\geq 1}|a\_{1\ell\ell}|/2\;=\;a/2, |  |

so, by Example [3.2](#S3.Thmexample2 "Example 3.2. ‣ 3.3 Examples ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model"), (Xk)(X\_{k}) is strictly stationary, L2L^{2}-mm-approximable, and a WWN when a<2a<2. Further in this case Assumption [2.2](#S2.Thmassumption2 "Assumption 2.2. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model") and ([3.13](#S3.E13 "In Proposition 3.4. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) hold. Thus, by Proposition [3.4](#S3.Thmproposition4 "Proposition 3.4. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model"),

|  |  |  |
| --- | --- | --- |
|  | μ𝚺=(𝕀−α1​(𝒞𝜺))−1​(Δ).\mu\_{\boldsymbol{\Sigma}}=\big(\boldsymbol{\mathbb{I}}-\alpha\_{1}(\mathscr{C}\_{\boldsymbol{\varepsilon}})\big)^{-1}(\Delta). |  |

## 4 Estimation in the CCC-op-ARCH model

We now turn to the estimation of the parameters α1,…,αp,\alpha\_{1},...,\alpha\_{p}, and Δ\Delta in the CCC-op-ARCH(p)(p). Henceforth, 𝑿=(Xk)⊂ℋ\boldsymbol{X}=(X\_{k})\subset\mathcal{H} refers to a stationary CCC-op-ARCH(p)(p) process that possesses finite second moments from which we have observed a stretch of length NN, X1,…,XNX\_{1},...,X\_{N}. We will assume throughout the remainder of this article that Assumption [2.2](#S2.Thmassumption2 "Assumption 2.2. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model") holds so that 𝒞ε\mathscr{C}\_{\varepsilon} and Σk\Sigma\_{k} commute. Under this assumption,

|  |  |  |
| --- | --- | --- |
|  | μ𝚺=𝔼⁡(Σk),𝒞𝑿=𝔼⁡(Xk⊗2)=μ𝚺​𝒞𝜺,Σk1/2​𝒞𝜺​Σk1/2=Σk​𝒞𝜺,k∈ℤ,\mu\_{\boldsymbol{\Sigma}}=\operatorname{\mathds{E}}(\Sigma\_{k}),\quad\mathscr{C}\_{\!\boldsymbol{X}}=\operatorname{\mathds{E}}(X\_{k}^{\otimes 2})=\mu\_{\boldsymbol{\Sigma}}\mathscr{C}\_{\boldsymbol{\varepsilon}},\quad\Sigma\_{k}^{1/2}\mathscr{C}\_{\boldsymbol{\varepsilon}}\Sigma\_{k}^{1/2}=\Sigma\_{k}\mathscr{C}\_{\boldsymbol{\varepsilon}},\quad k\in\mathbb{Z}, |  |

and the op-ARCH equations imply that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk⊗2−𝒞𝑿=Σk1/2​(εk⊗2−𝒞𝜺)​Σk1/2+(∑i=1pαi​(Xk−i⊗2−𝒞𝑿))​𝒞𝜺.\displaystyle X^{\otimes 2}\_{k}-\mathscr{C}\_{\!\boldsymbol{X}}=\Sigma^{1/2}\_{k}(\varepsilon^{\otimes 2}\_{\!k}-\mathscr{C}\_{\boldsymbol{\varepsilon}})\Sigma^{1/2}\_{k}+\bigg(\sum^{p}\_{i=1}\alpha\_{i}(X^{\otimes 2}\_{k-i}-\mathscr{C}\_{\!\boldsymbol{X}})\bigg)\mathscr{C}\_{\boldsymbol{\varepsilon}}. |  | (4.1) |

If we calculate the covariances of the above with Xk−i⊗2X^{\otimes 2}\_{k-i}, 1≤i≤p1\leq i\leq p, due to causality the covariance with the first term on the right-hand side of ([4.1](#S4.E1 "In 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")) will vanish, and the covariances with the second term may be expressed in terms of the α\alpha operators. In order to shift the nuisance operator 𝒞ε\mathscr{C}\_{\varepsilon} off of the terms containing the α\alpha’s, we proceed first by applying on the right a *Tikhonov*-regularized inverse

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞𝜺†≔(𝒞𝜺+ϑN​𝕀)−1,\displaystyle\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}\coloneqq(\mathscr{C}\_{\boldsymbol{\varepsilon}}+\vartheta\_{\!N}\mathbb{I})^{-1}, |  | (4.2) |

where 𝕀\mathbb{I} denotes the identity map and ϑN>0\vartheta\_{\!N}>0 is an asymptotically vanishing regularization parameter, i.e., ϑN→0\vartheta\_{\!N}\to 0. After this regularization, we also project onto a finite-dimensional space. Let (aj,ej)(a\_{j},e\_{j}) be the eigenpairs of 𝒞𝜺,\mathscr{C}\_{\boldsymbol{\varepsilon}}, i.e. a1≥a2≥⋯>0a\_{1}\geq a\_{2}\geq\cdots>0 are the eigenvalues associated with the eigenfunctions e1,e2,…e\_{1},e\_{2},\dots of 𝒞𝜺.\mathscr{C}\_{\boldsymbol{\varepsilon}}. Then, the projection operator onto the linear space spanned by e1,…,eK,e\_{1},\dots,e\_{K}, K∈ℕK\in\mathbb{N}, is denoted by ∐e1eK,\coprod^{e\_{K}}\_{e\_{1}}, and we define 𝒞𝜺‡≔𝒞𝜺​𝒞𝜺†.\mathscr{C}^{\ddagger}\_{\!\boldsymbol{\varepsilon}}\coloneqq\mathscr{C}\_{\boldsymbol{\varepsilon}}\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}. According again to ([4.1](#S4.E1 "In 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (Xk⊗2−𝒞𝑿)​𝒞𝜺†​∐e1eK\displaystyle\big(X^{\otimes 2}\_{k}-\mathscr{C}\_{\!\boldsymbol{X}}\big)\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}} | =Σk1/2​(εk⊗2−𝒞𝜺)​Σk1/2​𝒞𝜺†​∐e1eK+(∑i=1pαi​(Xk−i⊗2−𝒞𝑿))​𝒞𝜺‡​∐e1eK.\displaystyle\,=\,\Sigma^{1/2}\_{k}(\varepsilon^{\otimes 2}\_{\!k}-\mathscr{C}\_{\boldsymbol{\varepsilon}})\Sigma^{1/2}\_{k}\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}}\;+\;\bigg(\sum^{p}\_{i=1}\alpha\_{i}(X^{\otimes 2}\_{k-i}-\mathscr{C}\_{\!\boldsymbol{X}})\bigg)\mathscr{C}^{\ddagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}}. |  | (4.3) |

Further, let 𝑿𝜺⊗2=(Xk,𝜺⊗2)k∈ℤ⊂𝒮\boldsymbol{X}^{\otimes 2}\_{\!\boldsymbol{\varepsilon}}=(X^{\otimes 2}\_{\!k,\boldsymbol{\varepsilon}})\_{k\in\mathbb{Z}}\subset\mathcal{S} and 𝑿⊗2,[p]=(Xk⊗2,[p])k∈ℤ⊂𝒮p\boldsymbol{X}^{\otimes 2,[p]}\!=(X^{\otimes 2,[p]}\_{\!k})\_{k\in\mathbb{Z}}\subset\mathcal{S}^{p} be the processes defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk,𝜺⊗2≔Xk⊗2​𝒞𝜺†​∐e1eK, and ​Xk⊗2,[p]≔(Xk⊗2,…,Xk−p+1⊗2)⊤,k∈ℤ,\displaystyle X^{\otimes 2}\_{\!k,\boldsymbol{\varepsilon}}\coloneqq X^{\otimes 2}\_{\!k}\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}}\,,\;\mbox{ and }\;X^{\otimes 2,[p]}\_{\!k}\coloneqq(X^{\otimes 2}\_{\!k},\dots,X^{\otimes 2}\_{\!k-p+1})^{\top}\!,\quad k\in\mathbb{Z}, |  | (4.4) |

and their centered versions by

|  |  |  |  |
| --- | --- | --- | --- |
|  | X~k,𝜺⊗2≔Xk,𝜺⊗2−𝒞𝑿​𝒞𝜺†​∐e1eK, and ​X~k⊗2,[p]≔Xk⊗2,[p]−(𝒞𝑿,…,𝒞𝑿)⊤,k∈ℤ.\displaystyle\tilde{X}^{\otimes 2}\_{\!k,\boldsymbol{\varepsilon}}\coloneqq X^{\otimes 2}\_{\!k,\boldsymbol{\varepsilon}}-\,\mathscr{C}\_{\!\boldsymbol{X}}\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}}\,,\;\mbox{ and }\;\tilde{X}^{\otimes 2,[p]}\_{\!k}\coloneqq X^{\otimes 2,[p]}\_{\!k}-(\mathscr{C}\_{\!\boldsymbol{X}},\dots,\mathscr{C}\_{\!\boldsymbol{X}})^{\top}\!,\quad k\in\mathbb{Z}. |  | (4.5) |

We see according to ([4.3](#S4.E3 "In 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")) that the lag-1 cross-covariance operators 𝒟=𝒟K,N=𝒞𝑿⊗2,[p],𝑿𝜺⊗21∈𝒩𝒮p,𝒮\mathscr{D}=\mathscr{D}\_{K,N}=\mathscr{C}^{1}\_{\!\boldsymbol{X}^{\otimes 2,[p]},\boldsymbol{X}^{\otimes 2}\_{\!\boldsymbol{\varepsilon}}}\in\mathcal{N}\_{\mathcal{S}^{p}\!,\mathcal{S}} satisfy the following Yule–Walker (YW)-type equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟=𝜶​𝒞+ℛ,\displaystyle\mathscr{D}=\boldsymbol{\alpha}\mathscr{C}+\mathscr{R}, |  | (4.6) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞=𝒞𝑿⊗2,[p]∈𝒩𝒮p,\displaystyle\mathscr{C}=\mathscr{C}\_{\!\boldsymbol{X}^{\otimes 2,[p]}}\in\mathcal{N}\_{\mathcal{S}^{p}}, |  | (4.7) |

with 𝜶\boldsymbol{\alpha} from ([2.6](#S2.E6 "In 2 General model and assumptions ‣ An operator-level ARCH Model")), and where the remainder ℛ=ℛK,N\mathscr{R}=\mathscr{R}\_{K,N} is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ≔𝔼⟨X~0⊗2,[p],⋅⟩𝒮[[𝜶(X~0⊗2,[p])](𝒞𝜺‡∐e1eK−𝕀)].\displaystyle\mathscr{R}\coloneqq\operatorname{\mathds{E}}\!\big\langle\tilde{X}^{\otimes 2,[p]}\_{0},\cdot\big\rangle\_{\!\mathcal{S}}\Bigg[\,\Big[\boldsymbol{\alpha}\big(\tilde{X}^{\otimes 2,[p]}\_{0}\big)\Big]\bigg(\mathscr{C}^{\ddagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}}-\,\mathbb{I}\bigg)\Bigg]\,. |  | (4.8) |

Notice that all the operators in the YW-type equation ([4.6](#S4.E6 "In 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")) are well-defined due to causality of the involved processes and Proposition [3.3](#S3.Thmproposition3 "Proposition 3.3. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model").

If the remainder term is small, it seems natural in view of ([4.6](#S4.E6 "In 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")) to estimate 𝜶\boldsymbol{\alpha} by 𝒟^​𝒞^−1\hat{\mathscr{D}}\hat{\mathscr{C}}^{-1}. This, however, does not yield a useful estimate, as 𝜶\boldsymbol{\alpha} is not identifiable from 𝜶​𝒞\boldsymbol{\alpha}\mathscr{C} when 𝒞\mathscr{C} is not injective. For example, in ℋ=L2​[0,1]\mathcal{H}=L^{2}[0,1] with p=1p=1, the operator J∈𝒮J\in\mathcal{S} with kernel j​(s,t)=−1j(s,t)=-1 if s≤ts\leq t and j​(s,t)=1j(s,t)=1 otherwise, satisfies ⟨𝒞​(K),K⟩𝒮=0\langle\mathscr{C}(K),K\rangle\_{\mathcal{S}}=0. This issue parallels the multivariate case where, for X∈ℝdX\in\mathbb{R}^{d}, vec​(X​X⊤)∈ℝd2\mbox{vec}(XX^{\top})\in\mathbb{R}^{d^{2}} does not have a full-rank covariance matrix, while the “half-vectorization” vech​(X​X⊤)∈ℝd​(d+1)/2\mbox{vech}(XX^{\top})\in\mathbb{R}^{d(d+1)/2} typically does. In what follows, we derive estimators for the CCC-op-ARCH(p)(p) operators, that is, to reiterate, 𝜶\boldsymbol{\alpha} in ([2.8](#S2.E8 "In 2 General model and assumptions ‣ An operator-level ARCH Model")) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜶=∑i=1p∑ℓ=1∞ai​ℓ​ℓ​[Ei​ℓ​ℓ⊗𝒮(eℓ⊗eℓ)],\displaystyle\boldsymbol{\alpha}=\sum^{p}\_{i=1}\sum^{\infty}\_{\ell=1}\,a\_{i\ell\ell}\big[E\_{i\ell\ell}\!\otimes\_{\mathcal{S}}\!(e\_{\ell}\otimes e\_{\ell})\big]\,, |  | (4.9) |

based on the YW-type equation ([4.6](#S4.E6 "In 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")), suitably modified to ensure identifiability, as well as estimators for the intercept term Δ\Delta.

### 4.1 Finite-dimensional setting

Although our ultimate goal is to derive consistent estimators for the infinite-dimensional operators in ([4.9](#S4.E9 "In 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")), we begin with estimating the CCC-op-ARCH operators α1,…,αp,\alpha\_{1},\dots,\alpha\_{p}, under the simplifying assumption that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜶=𝜶K≔∑i=1p∑ℓ=1Kai​ℓ​ℓ​[Ei​ℓ​ℓ⊗𝒮(eℓ⊗eℓ)]\displaystyle\boldsymbol{\alpha}=\boldsymbol{\alpha}\_{K}\coloneqq\sum^{p}\_{i=1}\sum^{K}\_{\ell=1}\,a\_{i\ell\ell}[E\_{i\ell\ell}\!\otimes\_{\mathcal{S}}\!(e\_{\ell}\otimes e\_{\ell})]\, |  | (4.10) |

for a finite integer KK. Further, we assume that the observed curves XiX\_{i} are finite-dimensional, so that with Xk,i=⟨Xk,ei⟩:X\_{k,i}=\langle X\_{k},e\_{i}\rangle:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk=∑i=1KXk,i​ei,k∈ℤ.\displaystyle X\_{k}=\sum^{K}\_{i=1}\,X\_{k,i}e\_{i},\quad k\in\mathbb{Z}. |  | (4.11) |

The representation of XkX\_{k} yields with Xk,i​j≔Xk,i​Xk,j:X\_{k,ij}\coloneqq X\_{k,i}X\_{k,j}:

|  |  |  |
| --- | --- | --- |
|  | Xk⊗2=∑i=1K∑j=1KXk,i​j​(ei⊗ej),X^{\otimes 2}\_{k}=\sum^{K}\_{i=1}\sum^{K}\_{j=1}\,X\_{k,ij}(e\_{i}\otimes e\_{j}), |  |

implying that each Xk⊗2,[p],X^{\otimes 2,[p]}\_{k}, with p∈ℕ,p\in\mathbb{N}, is characterized by the block matrix

|  |  |  |
| --- | --- | --- |
|  | ((Xk,i​j)i,j=1K,(Xk−1,i​j)i,j=1K,…,(Xk−p+1,i​j)i,j=1K)⊤∈ℝp​K×K.\displaystyle\Big(\big(X\_{k,ij}\big)\_{i,j=1}^{K},\big(X\_{k-1,ij}\big)\_{i,j=1}^{K},\dots,\big(X\_{k-p+1,ij}\big)\_{i,j=1}^{K}\Big)^{\top}\in\mathbb{R}^{pK\times K}. |  |

Throughout, the map diag:ℝK→ℝK×K\operatorname{\mathrm{d}iag}:\mathbb{R}^{K}\to\mathbb{R}^{K\times K} and its adjoint diag∗:ℝK×K→ℝK\operatorname{\mathrm{d}iag}^{\ast}:\mathbb{R}^{K\times K}\to\mathbb{R}^{K} construct a diagonal matrix from a vector and create a vector by extracting the diagonal of the input matrix, respectively. Note that diag:ℝp​K→ℝp​K×K\operatorname{\mathrm{d}iag}:\mathbb{R}^{pK}\to\mathbb{R}^{pK\times K} and diag∗:ℝp​K×K→ℝp​K\operatorname{\mathrm{d}iag}^{\ast}:\mathbb{R}^{pK\times K}\to\mathbb{R}^{pK} are also component-wise defined, i.e. for any vectors x1,…,xp∈ℝKx\_{1},\dots,x\_{p}\in\mathbb{R}^{K} and matrices A1,…,Ap∈ℝK×K,A\_{1},\dots,A\_{p}\in\mathbb{R}^{K\times K},

|  |  |  |  |
| --- | --- | --- | --- |
|  | diag⁡(x1,…,xp)\displaystyle\operatorname{\mathrm{d}iag}(x\_{1},\dots,x\_{p}) | ≔(diag⁡(x1),…,diag⁡(xp))⊤, and\displaystyle\coloneqq\big(\operatorname{\mathrm{d}iag}(x\_{1}),\dots,\operatorname{\mathrm{d}iag}(x\_{p})\big)^{\!\top}\!,\mbox{ and } |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | diag∗⁡(A1,…,Ap)\displaystyle\operatorname{\mathrm{d}iag}^{\ast}(A\_{1},\dots,A\_{p}) | ≔(diag∗⁡(A1),…,diag∗⁡(Ap))⊤.\displaystyle\coloneqq\big(\operatorname{\mathrm{d}iag}^{\ast}(A\_{1}),\dots,\operatorname{\mathrm{d}iag}^{\ast}(A\_{p})\big)^{\!\top}\!. |  |

From ([4.10](#S4.E10 "In 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")) and ([4.11](#S4.E11 "In 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")), it follows with X~m,i​j≔Xm,i​j−𝔼⁡(Xm,i​j)\tilde{X}\_{m,ij}\coloneqq X\_{m,ij}-\operatorname{\mathds{E}}(X\_{m,ij}) for any mm:

|  |  |  |
| --- | --- | --- |
|  | diag∗⁡𝜶​𝒞​diag⁡(x1,…,xp)\displaystyle\operatorname{\mathrm{d}iag}^{\ast}\!\boldsymbol{\alpha}\mathscr{C}\!\operatorname{\mathrm{d}iag}(x\_{1},\dots,x\_{p}) |  |
|  |  |  |
| --- | --- | --- |
|  | =∑i=1p∑j=1p∑k=1Kxi(k)​diag∗⁡𝔼⁡(X~1−i,k​k​αj​(X~1−j⊗2))\displaystyle\quad=\sum^{p}\_{i=1}\sum^{p}\_{j=1}\sum^{K}\_{k=1}\,x^{(k)}\_{i}\operatorname{\mathrm{d}iag}^{\ast}\operatorname{\mathds{E}}\!\Big(\tilde{X}\_{1-i,kk}\alpha\_{j}\big(\tilde{X}^{\otimes 2}\_{1-j}\big)\Big)\allowdisplaybreaks |  |
|  |  |  |
| --- | --- | --- |
|  | =∑i=1p∑j=1p∑k=1Kxi(k)​𝔼⁡(X~1−i,k​k​(aj​11​X~1−j,11,aj​22​X~1−j,22,…,aj​K​K​X~1−j,K​K)⊤)\displaystyle\quad=\sum^{p}\_{i=1}\sum^{p}\_{j=1}\sum^{K}\_{k=1}\,x^{(k)}\_{i}\operatorname{\mathds{E}}\!\Big(\tilde{X}\_{1-i,kk}\big(a\_{j11}\tilde{X}\_{1-j,11},a\_{j22}\tilde{X}\_{1-j,22},\dots,a\_{jKK}\tilde{X}\_{1-j,KK}\big)^{\!\top}\Big) |  |
|  |  |  |
| --- | --- | --- |
|  | =𝜶d​𝒞d​(x1,…,xp),\displaystyle\quad=\boldsymbol{\alpha}\_{\mathrm{d}}\mathscr{C}\_{\mathrm{d}}(x\_{1},\dots,x\_{p}), |  |

with 𝒞d≔diag∗⁡𝒞​diag∈ℝp​K×p​K,\mathscr{C}\_{\mathrm{d}}\coloneqq\operatorname{\mathrm{d}iag}^{\ast}\mathscr{C}\operatorname{\mathrm{d}iag}\in\mathbb{R}^{pK\times pK}, and where 𝜶d∈ℝK×p​K\boldsymbol{\alpha}\_{\mathrm{d}}\in\mathbb{R}^{K\times pK} is the block matrix

|  |  |  |
| --- | --- | --- |
|  | 𝜶d≔(diag⁡(a111,a122,…,a1​K​K)​⋯​diag⁡(ap​11,ap​22,…,ap​K​K)).\boldsymbol{\alpha}\_{\mathrm{d}}\coloneqq\big(\operatorname{\mathrm{d}iag}(a\_{111},a\_{122},\dots,a\_{1KK})\;\cdots\;\operatorname{\mathrm{d}iag}(a\_{p11},a\_{p22},\dots,a\_{pKK})\big). |  |

Therefore, due to the identity ([4.6](#S4.E6 "In 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")), it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟d=𝜶d​𝒞d+ℛd,\displaystyle\mathscr{D}\_{\mathrm{d}}=\boldsymbol{\alpha}\_{\mathrm{d}}\mathscr{C}\_{\mathrm{d}}+\mathscr{R}\_{\mathrm{d}}, |  | (4.12) |

where 𝒟d≔diag∗⁡𝒟​diag∈ℝp​K×K\mathscr{D}\_{\mathrm{d}}\coloneqq\operatorname{\mathrm{d}iag}^{\ast}\!\mathscr{D}\operatorname{\mathrm{d}iag}\in\mathbb{R}^{pK\times K} and ℛd≔diag∗⁡ℛ​diag∈ℝp​K×K,\mathscr{R}\_{\mathrm{d}}\coloneqq\operatorname{\mathrm{d}iag}^{\ast}\mathscr{R}\operatorname{\mathrm{d}iag}\in\mathbb{R}^{pK\times K}, with 𝒟,ℛ\mathscr{D},\mathscr{R} from ([4.6](#S4.E6 "In 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")). Moreover, as all the coefficients of interest ai​j​j,a\_{ijj}, with 1≤i≤p,1\leq i\leq p, 1≤j≤K,1\leq j\leq K, are contained in

|  |  |  |
| --- | --- | --- |
|  | 𝜶~d≔diag∗⁡(𝜶d),\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}}\coloneqq\operatorname{\mathrm{d}iag}^{\ast}(\boldsymbol{\alpha}\_{\mathrm{d}}), |  |

we propose the estimator

|  |  |  |
| --- | --- | --- |
|  | 𝜶^d≔diag∗⁡(𝒟^d​𝒞^d−1),\displaystyle\hat{\boldsymbol{\alpha}}\_{\mathrm{d}}\coloneqq\operatorname{\mathrm{d}iag}^{\ast}\!\big(\hat{\mathscr{D}}\_{\mathrm{d}}\hat{\mathscr{C}}^{-1}\_{\mathrm{d}}\big), |  |

provided 𝒞^d≔diag∗⁡𝒞^​diag\hat{\mathscr{C}}\_{\mathrm{d}}\coloneqq\operatorname{\mathrm{d}iag}^{\ast}\hat{\mathscr{C}}\operatorname{\mathrm{d}iag} is non-singular, and 𝒟^d≔diag∗⁡𝒟^​diag\hat{\mathscr{D}}\_{\mathrm{d}}\coloneqq\operatorname{\mathrm{d}iag}^{\ast}\!\hat{\mathscr{D}}\operatorname{\mathrm{d}iag}, with

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞^≔1N​∑k=pN(Xk⊗2,[p]−m^p)⊗𝒮(Xk⊗2,[p]−m^p), and \displaystyle\hat{\mathscr{C}}\coloneqq\frac{1}{N}\sum\_{k=p}^{N}\,\big(X^{\otimes 2,[p]}\_{\!k}\!-\hat{m}\_{p}\big)\otimes\_{\mathcal{S}}\big(X^{\otimes 2,[p]}\_{\!k}-\hat{m}\_{p}\big),\mbox{ and } |  | (4.13) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟^≔1N​∑k=pN−1(Xk⊗2,[p]−m^p)⊗𝒮[(Xk+1⊗2−m^1′)​𝒞𝜺†​∐e1eK].\displaystyle\hat{\mathscr{D}}\coloneqq\frac{1}{N}\sum\_{k=p}^{N-1}\,\big(X^{\otimes 2,[p]}\_{\!k}-\hat{m}\_{p}\big)\otimes\_{\mathcal{S}}\bigg[\big(X^{\otimes 2}\_{\!k+1}-\hat{m}^{\prime}\_{1}\big)\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}}\bigg]. |  | (4.14) |

###### Assumption 4.1.

* (a)

  For all NN sufficiently large, with probability one 𝒞^d∈ℝK×K\hat{\mathscr{C}}\_{\mathrm{d}}\in\mathbb{R}^{K\times K}\! is non-singular.
* (b)

  The matrix 𝒞d∈ℝK×K\mathscr{C}\_{\mathrm{d}}\in\mathbb{R}^{K\times K} is non-singular.

###### Theorem 4.1.

Let Assumptions [2.2](#S2.Thmassumption2 "Assumption 2.2. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model"), [4.1](#S4.Thmassumption1 "Assumption 4.1. ‣ 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model"), ([4.10](#S4.E10 "In 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")), ([4.11](#S4.E11 "In 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")), and the conditions of Proposition [3.3](#S3.Thmproposition3 "Proposition 3.3. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model") with ν>4\nu>4 hold, and ϑN=O​(N−1/2)\vartheta\_{\!N}=\mathrm{O}(N^{-1/2}) with ϑN\vartheta\_{\!N} in ([4.2](#S4.E2 "In 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")) hold. Then, for any norm ∥⋅∥\|\cdot\| on ℝK×p​K,\mathbb{R}^{K\times pK},

|  |  |  |
| --- | --- | --- |
|  | ‖𝜶^d−𝜶~d‖=Oℙ​(N−1/2).\|\hat{\boldsymbol{\alpha}}\_{\mathrm{d}}-\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}}\|=\mathrm{O}\_{\operatorname{\mathds{P}}}(N^{-1/2}). |  |

The following example shows that the covariance operator of an CCC-op-ARCH process can be injective in a finite-dimensional setting.

###### Example 4.1.

Let p=1,p=1, and assume ([4.10](#S4.E10 "In 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model"))–([4.11](#S4.E11 "In 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")) hold. Suppose further that X0X\_{0} has the structure of Example [3.3](#S3.Thmexample3 "Example 3.3. ‣ 3.3 Examples ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model"), let 𝛆=(εk)\boldsymbol{\varepsilon}=(\varepsilon\_{k}) be an i.i.d. process of standard Brownian motions on [0,1][0,1], and assume a1​ℓ​ℓ<π2/12a\_{1\ell\ell}<\pi^{2}/12 for all ℓ∈ℕ\ell\in\mathbb{N}. By the Karhunen–Loève expansion (Hsing and Eubank, [2015](#bib.bib19), Theorem 7.3.5), the scores ⟨εk,eℓ⟩\langle\varepsilon\_{k},e\_{\ell}\rangle are centered Gaussian variables, independent across ℓ\ell, with variances λℓ=(ℓ−1/2)−2​π−2\lambda\_{\ell}=(\ell-1/2)^{-2}\pi^{-2}, the eigenvalues of 𝒞𝛆\mathscr{C}\_{\boldsymbol{\varepsilon}}. The structure of X0X\_{0} gives X0,ℓ​ℓ=⟨X0,eℓ⟩2=Z0,ℓ​⟨ε0,eℓ⟩2X\_{0,\ell\ell}=\langle X\_{0},e\_{\ell}\rangle^{2}=Z\_{0,\ell}\langle\varepsilon\_{0},e\_{\ell}\rangle^{2} for each ℓ∈ℕ\ell\in\mathbb{N}, where

|  |  |  |
| --- | --- | --- |
|  | Z0,ℓ=dℓ+a1​ℓ​ℓ​Z−1,ℓ​⟨ε−1,eℓ⟩2,ℓ∈ℕ,Z\_{0,\ell}=d\_{\ell}+a\_{1\ell\ell}Z\_{-1,\ell}\langle\varepsilon\_{-1},e\_{\ell}\rangle^{2},\quad\ell\in\mathbb{N}, |  |

with dℓd\_{\ell} being the coefficients in the diagonalization of Δ\Delta. Since Z0,ℓZ\_{0,\ell} is independent of ε0\varepsilon\_{0} for each ℓ\ell, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞d\displaystyle\mathscr{C}\_{\mathrm{d}} | =𝔼⁡diag∗⁡(X~0⊗2)​[diag∗⁡(X~0⊗2)]⊤\displaystyle=\operatorname{\mathds{E}}\operatorname{\mathrm{d}iag}^{\ast}(\tilde{X}\_{0}^{\otimes 2})\big[\operatorname{\mathrm{d}iag}^{\ast}(\tilde{X}\_{0}^{\otimes 2})\big]^{\top} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(𝔼⁡(X0,i​j2)−𝔼⁡(X0,i​i)​𝔼⁡(X0,j​j))i,j=1K\displaystyle=\Big(\operatorname{\mathds{E}}\!\big(X^{2}\_{0,ij}\big)-\operatorname{\mathds{E}}\!\big(X\_{0,ii}\big)\!\operatorname{\mathds{E}}\!\big(X\_{0,jj}\big)\Big)\_{i,j=1}^{K} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =diag⁡(a12​[3​𝔼⁡(Z0,12)−(𝔼⁡(Z0,1))2],…,aK2​[3​𝔼⁡(Z0,K2)−(𝔼⁡(Z0,K))2]).\displaystyle=\operatorname{\mathrm{d}iag}\!\bigg(a\_{1}^{2}\Big[3\operatorname{\mathds{E}}(Z\_{0,1}^{2})-\big(\operatorname{\mathds{E}}(Z\_{0,1})\big)^{2}\Big],\dots,a\_{K}^{2}\Big[3\operatorname{\mathds{E}}(Z\_{0,K}^{2})-\big(\operatorname{\mathds{E}}(Z\_{0,K})\big)^{2}\Big]\bigg). |  |

Strict and weak stationarity of the volatility processes (Zk,ℓ)k(Z\_{k,\ell})\_{k} are ensured since a1​ℓ​ℓ∈(0,π2/12)a\_{1\ell\ell}\in(0,\pi^{2}/12) and λℓ∈(0,4/π2]\lambda\_{\ell}\in(0,4/\pi^{2}] imply λℓ​a1​ℓ​ℓ∈(0,1)\lambda\_{\ell}a\_{1\ell\ell}\in(0,1) for all ℓ\ell, and because (cf. Francq and Zakoïan, [2019](#bib.bib13), Theorem 2.5 and Remark 2.6)

|  |  |  |
| --- | --- | --- |
|  | 𝔼⁡(Z0,ℓ)=dℓ1−λℓ​a1​ℓ​ℓ,ℓ∈ℕ.\operatorname{\mathds{E}}(Z\_{0,\ell})=\frac{d\_{\ell}}{1-\lambda\_{\ell}a\_{1\ell\ell}},\quad\ell\in\mathbb{N}. |  |

Moreover, 𝔼⁡(Z0,ℓ2)\operatorname{\mathds{E}}(Z\_{0,\ell}^{2}) exists for all ℓ\ell, as 3​λℓ2​a1​ℓ​ℓ2∈(0,1)3\lambda\_{\ell}^{2}a\_{1\ell\ell}^{2}\in(0,1), and thus λℓ​a1​ℓ​ℓ∈(0,1)\lambda\_{\ell}a\_{1\ell\ell}\in(0,1), with

|  |  |  |
| --- | --- | --- |
|  | 𝔼⁡(Z0,ℓ2)=dℓ2​(1+λℓ​a1​ℓ​ℓ)(1−λℓ​a1​ℓ​ℓ)​(1−3​λℓ2​a1​ℓ​ℓ2),ℓ∈ℕ.\operatorname{\mathds{E}}(Z\_{0,\ell}^{2})=\frac{d\_{\ell}^{2}(1+\lambda\_{\ell}a\_{1\ell\ell})}{(1-\lambda\_{\ell}a\_{1\ell\ell})(1-3\lambda\_{\ell}^{2}a\_{1\ell\ell}^{2})},\quad\ell\in\mathbb{N}. |  |

Therefore, as

|  |  |  |
| --- | --- | --- |
|  | 3​𝔼⁡(Z0,ℓ2)−(𝔼⁡(Z0,ℓ))2=2​dℓ2(1−λℓ​a1​ℓ​ℓ)2​(1−3​λℓ2​a1​ℓ​ℓ2)> 0,ℓ∈ℕ,3\operatorname{\mathds{E}}(Z\_{0,\ell}^{2})-\big(\operatorname{\mathds{E}}(Z\_{0,\ell})\big)^{2}\;=\;\frac{2d\_{\ell}^{2}}{(1-\lambda\_{\ell}a\_{1\ell\ell})^{2}(1-3\lambda\_{\ell}^{2}a\_{1\ell\ell}^{2})}\;>\;0,\quad\ell\in\mathbb{N}, |  |

it follows that 𝒞d\mathscr{C}\_{\mathrm{d}} is a diagonal matrix with strictly positive diagonal entries, and therefore is invertible.

### 4.2 Infinite-dimensional setting

To extend the results of the previous section to the infinite-dimensional setting, the operation “diag\operatorname{\mathrm{d}iag}” must be generalized. In order to do so, we consider for H-S operators A∈𝒮A\in\mathcal{S} their orthogonal series expansion in the basis (ei⊗ej).(e\_{i}\otimes e\_{j}). Further we let ℓ2=ℓ2​(ℕ)\ell^{2}=\ell^{2}(\mathbb{N}) denote the space of square-summable real valued sequences (ai)i=1∞⊂ℝ.(a\_{i})^{\infty}\_{i=1}\subset\mathbb{R}. The bounded operator diag:ℓ2→𝒮\operatorname{\mathrm{d}iag}:\ell^{2}\to\mathcal{S} and its adjoint diag∗:𝒮→ℓ2\operatorname{\mathrm{d}iag}^{\ast}:\mathcal{S}\to\ell^{2} are defined by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | diag⁡((ai)i=1∞)≔∑i=1∞ai​(ei⊗ei),\displaystyle\operatorname{\mathrm{d}iag}\big((a\_{i})^{\infty}\_{i=1}\big)\coloneqq\sum\_{i=1}^{\infty}a\_{i}(e\_{i}\otimes e\_{i})\,, |  | diag∗⁡(∑i=1∞∑j=1∞ai​j​(ei⊗ej))≔(ai​i)i=1∞.\displaystyle\operatorname{\mathrm{d}iag}^{\ast}\!\bigg(\sum\_{i=1}^{\infty}\sum\_{j=1}^{\infty}a\_{ij}(e\_{i}\otimes e\_{j})\bigg)\coloneqq(a\_{ii})^{\infty}\_{i=1}\,. |  |

Here, we assume that 𝜶\boldsymbol{\alpha} has the infinite-dimensional form ([4.9](#S4.E9 "In 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")). The YW-type equation ([4.12](#S4.E12 "In 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")) also holds here, with 𝒟d≔diag∗⁡𝒟​diag:(ℓ2)p→ℓ2\mathscr{D}\_{\mathrm{d}}\coloneqq\operatorname{\mathrm{d}iag}^{\ast}\mathscr{D}\operatorname{\mathrm{d}iag}:(\ell^{2})^{p}\to\ell^{2}, 𝒞d≔diag∗⁡𝒞​diag:(ℓ2)p→(ℓ2)p\mathscr{C}\_{\mathrm{d}}\coloneqq\operatorname{\mathrm{d}iag}^{\ast}\mathscr{C}\operatorname{\mathrm{d}iag}:(\ell^{2})^{p}\to(\ell^{2})^{p}, and ℛd≔diag∗⁡ℛ​diag:(ℓ2)p→ℓ2\mathscr{R}\_{\mathrm{d}}\coloneqq\operatorname{\mathrm{d}iag}^{\ast}\mathscr{R}\operatorname{\mathrm{d}iag}:(\ell^{2})^{p}\to\ell^{2}. The operator 𝜶d:(ℓ2)p→ℓ2\boldsymbol{\alpha}\_{\mathrm{d}}:(\ell^{2})^{p}\to\ell^{2} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜶d≔(diag⁡((a1​j​j)j=1∞)​⋯​diag⁡((ap​j​j)j=1∞)),\displaystyle\boldsymbol{\alpha}\_{\mathrm{d}}\coloneqq\big(\operatorname{\mathrm{d}iag}\!\big((a\_{1jj})^{\infty}\_{j=1}\big)\;\cdots\;\operatorname{\mathrm{d}iag}\!\big((a\_{pjj})^{\infty}\_{j=1}\big)\big), |  | (4.15) |

where each diag⁡((ai​j​j)j=1∞)\operatorname{\mathrm{d}iag}((a\_{ijj})^{\infty}\_{j=1}) is the infinite-dimensional diagonal matrix of its coefficients. Then, for any x=(x1,…,xp)⊤∈(ℓ2)px=(x\_{1},\dots,x\_{p})^{\top}\in(\ell^{2})^{p}, with xi=(xi​j)j=1∞x\_{i}=(x\_{ij})^{\infty}\_{j=1},

|  |  |  |
| --- | --- | --- |
|  | 𝜶d​(x)=(∑i=1pai​j​j​xi​j)j=1∞,\boldsymbol{\alpha}\_{\mathrm{d}}(x)=\bigg(\sum^{p}\_{i=1}a\_{ijj}x\_{ij}\bigg)^{\infty}\_{j=1}\,, |  |

which lies in ℓ2\ell^{2} whenever supi,j|ai​j​j|<∞\sup\_{i,j}|a\_{ijj}|<\infty.

Unlike in the finite-dimensional case, we cannot directly estimate all coefficients of 𝜶d\boldsymbol{\alpha}\_{\mathrm{d}}, i.e.

|  |  |  |
| --- | --- | --- |
|  | 𝜶~d≔diag∗⁡(𝜶d).\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}}\coloneqq\operatorname{\mathrm{d}iag}^{\ast}(\boldsymbol{\alpha}\_{\mathrm{d}}). |  |

We therefore adopt Tikhonov regularization and project onto a finite-dimensional subspace of dimension K∈ℕK\in\mathbb{N}, with K=KN→∞K=K\_{\!N}\to\infty as N→∞N\to\infty. To estimate 𝜶~d\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}}, we propose

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜶^d≔diag∗⁡(𝒟^d​𝒞^d†​∐c^1,dc^K,d),\displaystyle\hat{\boldsymbol{\alpha}}\_{\mathrm{d}}\coloneqq\operatorname{\mathrm{d}iag}^{\ast}\!\bigg(\hat{\mathscr{D}}\_{\mathrm{d}}\hat{\mathscr{C}}^{\dagger}\_{\mathrm{d}}\!\coprod^{\hat{c}\_{K,\mathrm{d}}}\_{\hat{c}\_{1,\mathrm{d}}}\bigg)\,, |  | (4.16) |

where 𝒟^d≔diag∗⁡𝒟^​diag\hat{\mathscr{D}}\_{\mathrm{d}}\coloneqq\operatorname{\mathrm{d}iag}^{\ast}\hat{\mathscr{D}}\operatorname{\mathrm{d}iag} with 𝒟^\hat{\mathscr{D}} in ([B.1](#A2.E1 "In Appendix B Notes ‣ An operator-level ARCH Model")),
𝒞^d≔diag∗⁡𝒞^​diag\hat{\mathscr{C}}\_{\mathrm{d}}\coloneqq\operatorname{\mathrm{d}iag}^{\ast}\hat{\mathscr{C}}\operatorname{\mathrm{d}iag} with 𝒞^\hat{\mathscr{C}} in ([B.2](#A2.E2 "In Appendix B Notes ‣ An operator-level ARCH Model")),

|  |  |  |
| --- | --- | --- |
|  | 𝒞^d†≔(𝒞^d+ϑN​𝕀)−1​ with ​ϑN→0,\hat{\mathscr{C}}^{\dagger}\_{\mathrm{d}}\coloneqq(\hat{\mathscr{C}}\_{\mathrm{d}}+\vartheta\_{\!N}\mathbb{I})^{-1}\mbox{ with }\vartheta\_{\!N}\to 0, |  |

and where (λ^j,d,c^j,d)(\hat{\lambda}\_{j,\mathrm{d}},\hat{c}\_{j,\mathrm{d}}) and (λj,d,cj,d)(\lambda\_{j,\mathrm{d}},c\_{j,\mathrm{d}}) are eigenpairs of 𝒞^d\hat{\mathscr{C}}\_{\mathrm{d}} and 𝒞d\mathscr{C}\_{\mathrm{d}}, respectively. To establish the consistency of this estimator, we impose:

###### Assumption 4.2.

There exists ξ∈ℕ\xi\in\mathbb{N} such that:

* (a)

  The dimensions of all eigenspaces of 𝒞d\mathscr{C}\_{\mathrm{d}} are bounded above by ξ;\xi;
* (b)

  For all large NN, with probability one, the eigenvalues of 𝒞^d\hat{\mathscr{C}}\_{\mathrm{d}} satisfy λ^j,d≠λ^j+1,d\hat{\lambda}\_{j,\mathrm{d}}\neq\hat{\lambda}\_{j+1,\mathrm{d}} for j=1,…,K+ξ.j=1,\dots,K+\xi.

We define (Λℓ,d)ℓ∈ℕ(\Lambda\_{\ell,\mathrm{d}})\_{\ell\in\mathbb{N}}, the reciprocal eigengaps of 𝒞d\mathscr{C}\_{\mathrm{d}} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λℓ,d≔1λℓ,d−λℓb,d,ℓ∈ℕ,\displaystyle\Lambda\_{\ell,\mathrm{d}}\coloneqq\frac{1}{\lambda\_{\ell,\mathrm{d}}-\lambda\_{\ell\_{b},\mathrm{d}}},\quad\ell\in\mathbb{N}, |  | (4.17) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓb≔inf{j>ℓ:λj,d<λℓ,d}.\displaystyle\ell\_{b}\coloneqq\inf\big\{j>\ell:\lambda\_{j,\mathrm{d}}<\lambda\_{\ell,\mathrm{d}}\big\}. |  | (4.18) |

Thus Λℓ,d\Lambda\_{\ell,\mathrm{d}} is the reciprocal eigengap between the eigenspace of cℓ,dc\_{\ell,\mathrm{d}} and the next distinct one. By Assumption [4.2](#S4.Thmassumption2 "Assumption 4.2. ‣ 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model") (a), ℓb−ℓ≤ξ\ell\_{b}-\ell\leq\xi. By part (b), the empirical analogues are

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ^ℓ,d≔1λ^ℓ,d−λ^ℓ+1,d,1≤ℓ≤K+ξ.\displaystyle\hat{\Lambda}\_{\ell,\mathrm{d}}\coloneqq\frac{1}{\hat{\lambda}\_{\ell,\mathrm{d}}-\hat{\lambda}\_{\ell+1,\mathrm{d}}}\,,\quad 1\leq\ell\leq K+\xi. |  | (4.19) |

Lemma [C.2](#A3.Thmlemma2 "Lemma C.2. ‣ Appendix C Proofs ‣ An operator-level ARCH Model") and the definitions of 𝒞^d,𝒞d\hat{\mathscr{C}}\_{\mathrm{d}},\mathscr{C}\_{\mathrm{d}} yield Λ^ℓ,d=Oℙ​(Λℓ,d)\hat{\Lambda}\_{\ell,\mathrm{d}}=\mathrm{O}\_{\operatorname{\mathds{P}}}(\Lambda\_{\ell,\mathrm{d}}) for 1≤ℓ≤K+ξ1\leq\ell\leq K+\xi (cf. Kühnert et al., [2026](#bib.bib27), Lemma A.3).

To establish consistency in the H-S norm, we impose a regularity condition that governs the approximation of 𝜶\boldsymbol{\alpha} by its finite-dimensional projections. This condition is analogous to the Sobolev-type smoothness assumptions introduced in Hall and Meister ([2007](#bib.bib15)) for deconvolution problems.

###### Assumption 4.3.

For some γ>0\gamma>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1p∑ℓ=1∞ai​ℓ​ℓ2​(1+ℓ2​γ)<∞.\displaystyle\sum^{p}\_{i=1}\sum^{\infty}\_{\ell=1}\,a^{2}\_{i\ell\ell}(1+\ell^{2\gamma})\,<\,\infty. |  | (4.20) |

We note that this assumption is stricter than 𝜶\boldsymbol{\alpha} is H-S, which is equivalent to square-summability of the coefficients. We may now state our main consistency result.

###### Theorem 4.2.

Suppose (Xk)(X\_{k}) is a CCC-op-ARCH(p)(p) process satisfying the conditions of Proposition [3.3](#S3.Thmproposition3 "Proposition 3.3. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model") for ν=4\nu=4. Further, let Assumptions [2.2](#S2.Thmassumption2 "Assumption 2.2. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model"), [2.3](#S2.Thmassumption3 "Assumption 2.3. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model"), [4.2](#S4.Thmassumption2 "Assumption 4.2. ‣ 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model"), and [4.3](#S4.Thmassumption3 "Assumption 4.3. ‣ 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model") hold. Let K=KN→∞K=K\_{\!N}\to\infty, ϑN→0\vartheta\_{\!N}\to 0 with Kγ+1/2​aK−2​ΛK,d2=O​(N1/2)K^{\gamma+1/2}a^{-2}\_{K}\Lambda^{2}\_{K,\mathrm{d}}=\mathrm{O}(N^{1/2}) and ϑN=O​(min⁡(aK,λK,d)​K−γ)\vartheta\_{\!N}=\mathrm{O}(\min(a\_{K},\lambda\_{K,\mathrm{d}})K^{-\gamma}), with γ\gamma defined in Assumption [4.3](#S4.Thmassumption3 "Assumption 4.3. ‣ 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model"). Then

|  |  |  |
| --- | --- | --- |
|  | ‖𝜶^d−𝜶~d‖𝒮=Oℙ​(K−γ).\|\hat{\boldsymbol{\alpha}}\_{\mathrm{d}}-\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}}\|\_{\mathcal{S}}=\mathrm{O}\_{\operatorname{\mathds{P}}}(K^{-\gamma}). |  |

###### Example 4.2.

Let p=1,p=1, and X0X\_{0} be as in Example [3.3](#S3.Thmexample3 "Example 3.3. ‣ 3.3 Examples ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model"), where (εk)(\varepsilon\_{k}) is a sequence of i.i.d. standard Brownian motions on [0,1][0,1], with a1​ℓ​ℓ≤π2/12a\_{1\ell\ell}\leq\pi^{2}/12 for all ℓ∈ℕ.\ell\in\mathbb{N}. Further suppose that the square-summable sequences (a1​ℓ​ℓ),(dℓ)⊂(0,∞)(a\_{1\ell\ell}),(d\_{\ell})\subset(0,\infty) of coefficients of α1\alpha\_{1} and Δ\Delta are strictly decreasing.

First, we consider the case when a1​ℓ​ℓ≍ℓ−aa\_{1\ell\ell}\asymp\ell^{-a} and dℓ≍ℓ−dd\_{\ell}\asymp\ell^{-d} as ℓ→∞\ell\to\infty for some a,d>1/2a,d>1/2. Assumptions [2.2](#S2.Thmassumption2 "Assumption 2.2. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model")–[2.3](#S2.Thmassumption3 "Assumption 2.3. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model") then hold. Since the entries of 𝒞d\mathscr{C}\_{\mathrm{d}} (cf. Example [4.1](#S4.Thmexample1 "Example 4.1. ‣ 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")) are distinct (as (λℓ)(\lambda\_{\ell}), (a1​ℓ​ℓ)(a\_{1\ell\ell}), (dℓ)(d\_{\ell}) are decreasing), Assumption [4.2](#S4.Thmassumption2 "Assumption 4.2. ‣ 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model") (a) holds, and Assumption [4.3](#S4.Thmassumption3 "Assumption 4.3. ‣ 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model") is satisfied for any γ∈(0,a−1/2)\gamma\in(0,a-1/2). Let γ=a−1/2−c\gamma=a-1/2-c for small c∈(0,a−1/2).c\in(0,a-1/2). The eigenvalues of 𝒞𝛆\mathscr{C}\_{\boldsymbol{\varepsilon}} satisfy aK≍K−2a\_{K}\asymp K^{-2}, and those of 𝒞d\mathscr{C}\_{\mathrm{d}} fulfill

|  |  |  |
| --- | --- | --- |
|  | λK,d=aK2​[3​𝔼⁡(Z0,K2)−(𝔼⁡(Z0,K))2]≍K−4​dK2≍K−(2​d+4).\lambda\_{K,\mathrm{d}}\;=\;a\_{K}^{2}\Big[3\operatorname{\mathds{E}}(Z^{2}\_{0,K})-\big(\operatorname{\mathds{E}}(Z\_{0,K})\big)^{2}\Big]\;\asymp\;K^{-4}d\_{K}^{2}\;\asymp\;K^{-(2d+4)}. |  |

Therefore, the reciprocal eigengaps satisfy ΛK,d≍K2​d+5\Lambda\_{K,\mathrm{d}}\asymp K^{2d+5}. With K=KN≍N1/2​(a−c+4​d+14)K=K\_{\!N}\asymp N^{1/2(a-c+4d+14)}, it follows

|  |  |  |
| --- | --- | --- |
|  | Kγ+1/2​aK−2​ΛK,d2≍Ka−c+4​d+14=O​(N1/2).K^{\gamma+1/2}a\_{K}^{-2}\Lambda^{2}\_{K,\mathrm{d}}\;\asymp\;K^{a-c+4d+14}\;=\;\mathrm{O}(N^{1/2}). |  |

Choosing ϑN→0\vartheta\_{\!N}\to 0 with ϑN=O​(min⁡(aK,λK,d)​K−γ)\vartheta\_{\!N}=\mathrm{O}(\min(a\_{K},\lambda\_{K,\mathrm{d}})K^{-\gamma}), Theorem [4.2](#S4.Thmtheorem2 "Theorem 4.2. ‣ 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model") gives

|  |  |  |
| --- | --- | --- |
|  | ‖𝜶^d−𝜶~d‖𝒮=Oℙ​(N−2​a−1−2​c4​a−4​c+16​d+56).\|\hat{\boldsymbol{\alpha}}\_{\mathrm{d}}-\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}}\|\_{\mathcal{S}}=\mathrm{O}\_{\operatorname{\mathds{P}}}\big(N^{-\frac{2a-1-2c}{4a-4c+16d+56}}\big). |  |

Faster rates occur for larger aa, slower decay of (λℓ)(\lambda\_{\ell}), and smaller dd. For instance, with d=1d=1, one achieves a rate near N−1/4N^{-1/4} if a=18a=18.

Now, suppose a1​ℓ​ℓ≍qℓa\_{1\ell\ell}\asymp q^{\ell} for q∈(0,1).q\in(0,1). In this case Assumption [4.3](#S4.Thmassumption3 "Assumption 4.3. ‣ 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model") holds for all γ>0\gamma>0, and hence with an appropriate choice of KN,K\_{N}, we obtain the near parametric rate N−1/2:N^{-1/2}\colon

|  |  |  |
| --- | --- | --- |
|  | ‖𝜶^d−𝜶~d‖𝒮=Oℙ​(N−1/2+ϵ), for any ​ϵ>0.\|\hat{\boldsymbol{\alpha}}\_{\mathrm{d}}-\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}}\|\_{\mathcal{S}}=\mathrm{O}\_{\operatorname{\mathds{P}}}\big(N^{-1/2+\epsilon}\big),\mbox{ for any }\epsilon>0. |  |

###### Remark 4.1.

A weak convergence result for 𝜶^d\hat{\boldsymbol{\alpha}}\_{\mathrm{d}} to a non-trivial limit is not available for the full operators in the fAR model underlying our ARCH framework (Mas, [2007](#bib.bib32), Theorem 3.2). Under technical conditions, Theorem 3.1 of the same work gives asymptotic normality for prediction errors at fixed points. In functional linear regression, which is in the context of our parameter estimation closely related, Kutta et al. ([2022](#bib.bib28)) obtain a pivotal test statistic for the slope operator under smoothness assumptions. While similar ideas might extend to our setting, we focus on weak consistency.

### 4.3 Estimation of the Intercept term

From 𝒞𝑿=μ𝚺​𝒞𝜺\mathscr{C}\_{\!\boldsymbol{X}}=\mu\_{\boldsymbol{\Sigma}}\mathscr{C}\_{\boldsymbol{\varepsilon}} and Eq. ([2.1](#S2.E1 "In Definition 2.1. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model")), it follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​𝒞𝜺=𝒞𝑿−(𝜶​(mp))​𝒞𝜺,\displaystyle\Delta\mathscr{C}\_{\boldsymbol{\varepsilon}}=\mathscr{C}\_{\!\boldsymbol{X}}-\big(\boldsymbol{\alpha}(m\_{p})\big)\mathscr{C}\_{\boldsymbol{\varepsilon}}, |  | (4.21) |

where mp≔𝔼⁡(X0⊗2,[p])m\_{p}\coloneqq\operatorname{\mathds{E}}(X^{\otimes 2,[p]}\_{0}). Accordingly, we estimate Δ\Delta by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ^≔[𝒞^𝑿−(𝜶^​(m^p))​𝒞𝜺]​𝒞𝜺†​∐e1eK,\displaystyle\hat{\Delta}\coloneqq\Big[\hat{\mathscr{C}}\_{\!\boldsymbol{X}}-\big(\boldsymbol{\hat{\alpha}}(\hat{m}\_{p})\big)\mathscr{C}\_{\boldsymbol{\varepsilon}}\Big]\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}}, |  | (4.22) |

with 𝒞^𝑿=m^1\hat{\mathscr{C}}\_{\!\boldsymbol{X}}=\hat{m}\_{1} and m^p\hat{m}\_{p} defined in ([B.3](#A2.E3 "In Appendix B Notes ‣ An operator-level ARCH Model")).

We next state a consistency result for Δ.\Delta. Since 𝒞𝜺\mathscr{C}\_{\boldsymbol{\varepsilon}} and Σk\Sigma\_{k} commute for each k,k, it holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ=∑i=1∞di​(ei⊗ei),\displaystyle\Delta=\sum\_{i=1}^{\infty}d\_{i}(e\_{i}\otimes e\_{i}), |  | (4.23) |

for some non-negative, square-summable sequence (di)(d\_{i}). Consistency of the estimation errors for Δ\Delta is also derived based on a Sobolev condition.

###### Proposition 4.1.

Let the conditions of Theorem [4.2](#S4.Thmtheorem2 "Theorem 4.2. ‣ 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model") hold. Further, for some δ>0,\delta>0, assume that the coefficients in ([4.23](#S4.E23 "In 4.3 Estimation of the Intercept term ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")) satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1∞di2​(1+i2​δ)<∞.\displaystyle\sum^{\infty}\_{i=1}\,d^{2}\_{i}(1+i^{2\delta})<\infty. |  | (4.24) |

Then, it holds that

|  |  |  |
| --- | --- | --- |
|  | ‖Δ^−Δ‖𝒮=Oℙ​(aK−1​N−1/2)+Oℙ​(K−δ)+Oℙ​(‖𝜶^−𝜶‖𝒮).\|\hat{\Delta}-\Delta\|\_{\mathcal{S}}=\mathrm{O}\_{\operatorname{\mathds{P}}}\big(a^{-1}\_{K}N^{-1/2}\big)+\mathrm{O}\_{\operatorname{\mathds{P}}}(K^{-\delta})+\mathrm{O}\_{\operatorname{\mathds{P}}}\big(\|\boldsymbol{\hat{\alpha}}-\boldsymbol{\alpha}\|\_{\mathcal{S}}\big)\,. |  |

## 5 Simulation Study

In this section, we present the results of simulation experiments that aim to illustrate the CCC-op-ARCH(p)(p) process, and evaluate the estimation procedures detailed in Section [4](#S4 "4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model"). In each of the examples below, we view (Xk)={Xi(t),k∈ℤ,t∈[0,1]}(X\_{k})=\{X\_{i}(t),\;k\in\mathbb{Z},\;t\in[0,1]\} as real-valued stochastic processes taking values in the Hilbert space ℋ=L2​[0,1]\mathcal{H}=L^{2}[0,1]. All analysis was done on a personal laptop in the R programming language; R Core Team ([2020](#bib.bib35)). Code that may be used to reproduce the the numerical work below is available at [github.com/jrvanderdoes/fungarch/](2603.10272v1/github.com/jrvanderdoes/fungarch/).

### 5.1 Implementation Details

The proposed estimators require the user to specify KK, the dimension reduction parameter, as well as the Tikhonov parameter ϑN\vartheta\_{N}. Throughout, we chose KK according to a modified total-variation-explained (TVE) criterion. Namely, with (ej)(e\_{j}) again denoting the eigenfunctions of 𝒞ε\mathscr{C}\_{\varepsilon}, and Xi,k=∑j=1k⟨Xi,ej⟩​ejX\_{i,k}=\sum\_{j=1}^{k}\langle X\_{i},e\_{j}\rangle e\_{j}, we then choose

|  |  |  |
| --- | --- | --- |
|  | K=min⁡{k:∑i=1N‖Xi−Xi,k‖2∑i=1N‖Xi‖2≤1−TVE}.K=\min\left\{k\;:\;\frac{\sum\_{i=1}^{N}\|X\_{i}-X\_{i,k}\|^{2}}{\sum\_{i=1}^{N}\|X\_{i}\|^{2}}\leq 1-\mbox{TVE}\right\}. |  |

We set TVE to 0.90.9 below, unless otherwise specified. In the subsequent application to high-frequency asset price data, a 90% TVE typically resulted in a KK in the range of 10–15.

In order to choose ϑN\vartheta\_{N}, we employ 1-step ahead cross-validation. The data of length NN are split into training and testing sets of size Nt​r​a​i​nN\_{train} and Nt​e​s​tN\_{test}. Below we use a respective 80%80\%/20%20\% split. Since the subsequent data analysis aims to forecast pointwise conditional quantiles, we chose ϑN\vartheta\_{N} in order to minimize an integrated check-loss function measuring how well Σ^i\hat{\Sigma}\_{i} may be used to predict the quantiles of XiX\_{i}. In particular, let the α\alpha level check-loss function ρα:ℝ→[0,∞)\rho\_{\alpha}:\mathbb{R}\to[0,\infty) be denoted as

|  |  |  |
| --- | --- | --- |
|  | ρα​(u)=u×(α−𝟙{u<0}).\rho\_{\alpha}(u)=u\times\big(\alpha-\mathds{1}\_{\{u<0\}}\big). |  |

Note that if a CCC-op-ARCH model has Gaussian innovations, then the pointwise conditional α\alpha quantile of Xi​(t)X\_{i}(t) is

|  |  |  |
| --- | --- | --- |
|  | Σj1/2​𝒞𝜺​Σj1/2​(t,t)×Φ−1​(αCε1/2​(t,t)).\sqrt{{\Sigma}^{1/2}\_{j}\mathscr{C}\_{\boldsymbol{\varepsilon}}{\Sigma}^{1/2}\_{j}(t,t)}\times\Phi^{-1}\left(\frac{\alpha}{C\_{\varepsilon}^{1/2}(t,t)}\right). |  |

For a given fitted CCC-op-ARCH model producing forecasts of the conditional covariance operator Σ^j\hat{\Sigma}\_{j}, viewed as a function of the parameter ϑN\vartheta\_{N} and computed with an expanding window, we then chose ϑN\vartheta\_{N} to minimize

|  |  |  |
| --- | --- | --- |
|  | CVE​r​r​(ϑN)=1Nt​e​s​t​∑j∈ test set ∫01ρα​(Σ^j1/2​𝒞𝜺​Σ^j1/2​(t,t)×Φ−1​(αCε1/2​(t,t))−Xi​(t))​dt.\mbox{CV}\_{Err}(\vartheta\_{N})=\frac{1}{N\_{test}}\sum\_{j\in\mbox{ test set }}\int\_{0}^{1}\rho\_{\alpha}\left(\sqrt{\hat{\Sigma}^{1/2}\_{j}\mathscr{C}\_{\boldsymbol{\varepsilon}}\hat{\Sigma}^{1/2}\_{j}(t,t)}\times\Phi^{-1}\left(\frac{\alpha}{C\_{\varepsilon}^{1/2}(t,t)}\right)-X\_{i}(t)\right)\mathrm{d}t. |  |

Optimizing for the Tikhonov parameter ϑN\vartheta\_{N} is somewhat computationally intensive for large pp, KK, and NN. An alternative approach that is computationally efficient, although does not necessarily lead to a consistent estimator, is to use Moore–Penrose pseudoinverses (Moore, [1920](#bib.bib33); Penrose, [1955](#bib.bib34)). In this case we modify ([4.16](#S4.E16 "In 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")) by replacing 𝒞𝜺†​∐e1eK\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}} and 𝒞^d†\hat{\mathscr{C}}^{\dagger}\_{\mathrm{d}} in the definition of 𝜶^d\hat{\boldsymbol{\alpha}}\_{\mathrm{d}} with

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞𝜺‡=∑i=1Kai−1​(ei⊗ei), and 𝒞d‡=∑i=1Kξ^i−1​(φ^i⊗φ^i),\displaystyle\mathscr{C}^{\ddagger}\_{\!\boldsymbol{\varepsilon}}=\sum\_{i=1}^{K}\,a^{-1}\_{i}(e\_{i}\otimes e\_{i})\,,\quad\mbox{ and }\quad\mathscr{C}^{\ddagger}\_{\mathrm{d}}=\sum\_{i=1}^{K}\,\hat{\xi}^{-1}\_{i}(\hat{\varphi}\_{i}\otimes\hat{\varphi}\_{i}), |  | (5.1) |

where (ξ^i,φ^i)(\hat{\xi}\_{i},\hat{\varphi}\_{i}) are eigenvalues and eigenfunctions of 𝒞^\hat{\mathscr{C}}. We also compared to this estimator in our simulation experiments.

### 5.2 Data Generation

![Refer to caption](2603.10272v1/)


(a) Example I

![Refer to caption](2603.10272v1/x4.png)


(b) Example II

Figure 2: CCC-op-ARCH Examples. (a) Uses CϵC\_{\epsilon} based on Ornstein–Uhlenbeck errors. (b) Uses CϵC\_{\epsilon} based on Brownian motion errors.

We simulated CCC-op-ARCH(p)(p) data (Xk)={Xk(t),k∈ℤ,t∈[0,1]}(X\_{k})=\{X\_{k}(t),\;k\in\mathbb{Z},\;t\in[0,1]\} as stochastic processes taking values in the space ℋ=L2​[0,1]\mathcal{H}=L^{2}[0,1]. We took the error covariance operator 𝒞𝜺\mathscr{C}\_{\boldsymbol{\varepsilon}} to be a kernel-integral operator with kernel CεC\_{\varepsilon} corresponding to either an Ornstein-Uhlenbeck (OU) process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cε​(t,s)=e−|t−s|/2,\displaystyle C\_{\varepsilon}(t,s)=e^{-|t-s|/2}, |  | (5.2) |

or a standard Brownian motion (BM)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cε​(t,s)=min⁡(t,s).\displaystyle C\_{\varepsilon}(t,s)=\min(t,s)\,. |  | (5.3) |

After generating errors with the specified covariance structure, each functional data object was simulated so that

|  |  |  |
| --- | --- | --- |
|  | Xi=Σi1/2​(εi),Σi=Δ+∑j=1pαj​(Xi−j⊗Xi−j),\displaystyle X\_{i}=\Sigma\_{i}^{1/2}(\varepsilon\_{i})\,,\quad\Sigma\_{i}=\Delta+\sum\_{j=1}^{p}\alpha\_{j}(X\_{i-j}\otimes X\_{i-j}), |  |

for i=−b,…,ni=-b,\dots,n, with b=100b=100 denoting a burn-in period that is discarded. The op-ARCH operators were constructed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | αj=∑k=1dak,j​(ek⊗ek)⊗(ek⊗ek),\displaystyle\alpha\_{j}=\sum\_{k=1}^{d}a\_{k,j}(e\_{k}\otimes e\_{k})\otimes(e\_{k}\otimes e\_{k}), |  | (5.4) |

with 𝐚j=(a1,j,…,ad,j){\bf a}\_{j}=(a\_{1,j},\dots,a\_{d,j}) denoting a vector of scale parameters. We further set Δ=𝒞ε\Delta=\mathscr{C}\_{\varepsilon}\,. In the simulations below, each functional data object is simulated on a grid of r=50r=50 equally spaced points on the unit interval [0,1][0,1]. We verified in unreported simulations that increasing the value of rr had a negligible impact on the reported results, although taking a small value of rr (r<10)(r<10) did negatively impact the results on model estimation error.

Spaghetti-rainbow plots illustrating the sample paths of CCC-op-ARCH(1)(1) processes of length N=200N=200 are shown in Figure [2](#S5.F2 "Figure 2 ‣ 5.2 Data Generation ‣ 5 Simulation Study ‣ An operator-level ARCH Model"). With λi\lambda\_{i}, i∈{1,2,..}i\in\{1,2,..\} denoting the ordered eigenvalues of 𝒞ε\mathscr{C}\_{\varepsilon}, Figure [2](#S5.F2 "Figure 2 ‣ 5.2 Data Generation ‣ 5 Simulation Study ‣ An operator-level ARCH Model")(a) uses 𝐚1=(0,1.6/λ2,1.6/λ3,1,6/λ4){\bf a}\_{1}=(0,1.6/\lambda\_{2},1.6/\lambda\_{3},1,6/\lambda\_{4}) and OU errors, and [2](#S5.F2 "Figure 2 ‣ 5.2 Data Generation ‣ 5 Simulation Study ‣ An operator-level ARCH Model")(b) uses 𝐚1=(0,1.1/λ2,1.1/λ3,1.1/λ4){\bf a}\_{1}=(0,1.1/\lambda\_{2},1.1/\lambda\_{3},1.1/\lambda\_{4}) with BM errors. These sample paths share some similarity with the real data studied in the following Section [6](#S6 "6 Application to Intra-Day Return Data ‣ An operator-level ARCH Model"), including periods of volatility/heteroscedasticity.

### 5.3 Consistency Results

![Refer to caption](2603.10272v1/MPvT.png)

![Refer to caption](2603.10272v1/MPvT_large.png)

Figure 3:  Relative absolute error eN,αe\_{N,\alpha} for Tikhonov versus Moore Penrose-based estimators for simulated CCC-op-ARCH(1)(1) data. The left-hand panel considers a low-dimensional setting, and the right-hand panel shows a high-dimensional setting.

We first present results on the consistency properties of the estimators proposed in Section [4](#S4 "4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model"). For each setting, we generated samples with sample sizes NN independently 500500 times, with N∈{50,100,250,500,750}N\in\{50,100,250,500,750\}, using OU errors ([5.2](#S5.E2 "In 5.2 Data Generation ‣ 5 Simulation Study ‣ An operator-level ARCH Model")). We considered the αj\alpha\_{j} as in ([5.4](#S5.E4 "In 5.2 Data Generation ‣ 5 Simulation Study ‣ An operator-level ARCH Model")), with either 𝐚j=(0.7,0.7){\bf a}\_{j}=(0.7,0.7), which we term “low-dimensional”, and 𝐚j=(1,1/22,…,1/202){\bf a}\_{j}=(1,1/2^{2},...,1/20^{2}), which we term “high-dimensional”.

![Refer to caption](2603.10272v1/convergence_A1.png)


(a) Relative estimation error eN,αe\_{N,\alpha} as a function of NN with simulated CCC-op-ARCH(1)(1) data.

![Refer to caption](2603.10272v1/x5.png)


(b) Relative estimation error eN,αe\_{N,\alpha} as a function of NN with simulated CCC-op-ARCH(5)(5) data.

![Refer to caption](2603.10272v1/convergence_delta.png)


(c) Relative estimation error eN,Δe\_{N,\Delta} as a function of NN with simulated CCC-op-ARCH(1)(1) data.

Figure 4: Estimation Consistency. Relative absolute error for estimation of Δ\Delta and the αj\alpha\_{j}’s of CCC-op-ARCH(1)(1) and CCC-op-ARCH(5)(5) models in the low-dimensional setting.

Figure [3](#S5.F3 "Figure 3 ‣ 5.3 Consistency Results ‣ 5 Simulation Study ‣ An operator-level ARCH Model") and [4](#S5.F4 "Figure 4 ‣ 5.3 Consistency Results ‣ 5 Simulation Study ‣ An operator-level ARCH Model") show plots of the relative absolute error between Δ\Delta and Δ^\hat{\Delta}

|  |  |  |  |
| --- | --- | --- | --- |
|  | eN,Δ=1500​∑s=1500‖Δ−Δ^s,N‖‖Δ‖.\displaystyle e\_{N,\Delta}=\frac{1}{500}\sum\_{s=1}^{500}\frac{\|\Delta-\hat{\Delta}\_{s,N}\|}{\|\Delta\|}\,. |  | (5.5) |

as well as for α\alpha and α^\hat{\alpha},

|  |  |  |  |
| --- | --- | --- | --- |
|  | eN,α=1500​∑s=1500∑i=1p‖αi−α^i,s,N‖‖αi‖,\displaystyle e\_{N,\alpha}=\frac{1}{500}\sum\_{s=1}^{500}\sum\_{i=1}^{p}\frac{\|\alpha\_{i}-\hat{\alpha}\_{i,s,N}\|}{\|\alpha\_{i}\|}\,, |  | (5.6) |

for increasing values of NN.

Figure [3](#S5.F3 "Figure 3 ‣ 5.3 Consistency Results ‣ 5 Simulation Study ‣ An operator-level ARCH Model") illustrates the difference in estimation error from using either the Tikhonov or Moore–Penrose inverses in defining the estimator. We observed that in the low-dimensional setting, the Moore–Penrose estimator tended to perform somewhat better, whereas in the high-dimensional case the performance between the two methods was more comparable. We note that the cross-validation criteria for determining ϑN\vartheta\_{\!N} does not intend to optimize the normed estimation error for the αj\alpha\_{j}, but rather attempts to improve quantile forecasting.

Figure [4](#S5.F4 "Figure 4 ‣ 5.3 Consistency Results ‣ 5 Simulation Study ‣ An operator-level ARCH Model") shows plots of eN,Δe\_{N,\Delta} and eN,αe\_{N,\alpha} in the low-dimensional setting for CCC-op-ARCH(1)(1) and CCC-op-ARCH(5)(5) data. We observed decreasing estimation error as a function of NN in each setting, as expected. Further, we also saw apparently consistent estimation of α1\alpha\_{1} by fitting a CCC-op-ARCH(5)(5) model to CCC-op-ARCH(1)(1) data (see Figure [4](#S5.F4 "Figure 4 ‣ 5.3 Consistency Results ‣ 5 Simulation Study ‣ An operator-level ARCH Model")(a)).

## 6 Application to Intra-Day Return Data

ARCH models are most commonly applied to model financial return data. We considered intra-day price data of the Exchange-Traded-fund SPY that tracks the S&P500 index. The returns were created by converting the stock prices into overnight cumulative intraday returns.

###### Definition 6.1.

Let Pj​(t)P\_{j}(t), j=0,…,Nj=0,\dots,N, be the price of a financial asset at time tt on day jj. The overnight cumulative intraday returns (OCIDRs) are defined as

|  |  |  |
| --- | --- | --- |
|  | Rj​(t)=100​(log⁡Pj​(t)−log⁡Pj−1​(1)),j=1,…,N,t∈[0,1].R\_{j}(t)=100\left(\log P\_{j}(t)-\log P\_{j-1}(1)\right),\quad j=1,\dots,N,\quad t\in[0,1]\,. |  |

The specific data we considered were obtained over two 3 year periods, 2018–2020 and 2022–2024, at a resolution of one observation every 1010 minutes (r=39r=39). The full sample had a size of N=735N=735 (2018–2020) and N=717N=717 (2022–2024). These data and the resulting OCIDR curves in 2018–2020 are illustrated in Figure [1](#S1.F1 "Figure 1 ‣ 1 Introduction ‣ An operator-level ARCH Model").

We took as the goal of this analysis to compare the proposed model along with several other methods to forecast conditional quantiles (Value-at-Risk) of the curves RjR\_{j}, and to evaluate the goodness-of-fit of the CCC-op-ARCH model to the data. After fitting a CCC-op-ARCH(p)(p) model, the lower α\alpha quantile curve forecast of Rj​(t)R\_{j}(t) is

|  |  |  |
| --- | --- | --- |
|  | V^j,α​(t)=Σ^j1/2​𝒞𝜺​Σ^j1/2​(t,t)×Φ−1​(αCε1/2​(t,t)),t∈[0,1],\displaystyle\hat{V}\_{j,\alpha}(t)=\sqrt{\hat{\Sigma}^{1/2}\_{j}\mathscr{C}\_{\boldsymbol{\varepsilon}}\hat{\Sigma}^{1/2}\_{j}(t,t)}\times\Phi^{-1}\left(\frac{\alpha}{C\_{\varepsilon}^{1/2}(t,t)}\right),\quad t\in[0,1], |  |

where Φ−1\Phi^{-1} is the quantile function of the standard normal distribution. In addition to comparing to the pointwise “historical” quantile computed from all the previous observations, we also fit a pw-fARCH(1)(1) model as in ([1.1](#S1.E1 "In 1 Introduction ‣ An operator-level ARCH Model")), using the estimation method of Cerovecki et al. ([2019](#bib.bib10)), and forecast the α\alpha quantile curve as V^j,α​(t)=σ^i​(t)​Φ−1​(α).\hat{V}\_{j,\alpha}(t)=\hat{\sigma}\_{i}(t)\Phi^{-1}(\alpha).

![Refer to caption](2603.10272v1/x6.png)


(a) Data And Forecast

![Refer to caption](2603.10272v1/)


(b) OCIDR curves and Forecasts

![Refer to caption](2603.10272v1/)


(c) Zoomed Forecast

Figure 5:  Plots of the curves V^j,0.05​(⋅)\hat{V}\_{j,0.05}(\cdot) for the CCC-op-ARCH(p)(p) models, p∈{1,5}p\in\{1,5\}, as well as the historical and pw-fARCH(1)(1) model along side the observed OCIDR curves for a particularly volatile period in the S&P 500 index including the COVID-19 Lockdown period in March, 2020.

In order to assess the accuracy of these quantile curve forecasts, we split each data set into a training set based on the first two years (Nt​r​a​i​n=482N\_{train}=482, 2018–2020 and Nt​r​a​i​n=465N\_{train}=465, 2022–2024) and then forecast a third year of data (Nt​e​s​t=253N\_{test}=253, 2018–2020 and Nt​e​s​t=252N\_{test}=252, 2022–2024), which we called the test set. Each quantile function was forecasted one step ahead using an expanding window, and the average (integrated) violation rate of each model was computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​Rα=1Nt​e​s​t​∑j∈ test set ∫01𝟙{Rj​(t)<V^j,α​(t)}​dt.\displaystyle VR\_{\alpha}=\frac{1}{N\_{test}}\sum\_{j\in\text{ test set }}\int\_{0}^{1}\mathds{1}\_{\{R\_{j}(t)<\hat{V}\_{j,\alpha}(t)\}}\,\mathrm{d}t. |  | (6.1) |

Table [1](#S6.T1 "Table 1 ‣ 6 Application to Intra-Day Return Data ‣ An operator-level ARCH Model") provides the observed average violation rates for each model for the nominal levels α=0.01\alpha=0.01 and α=0.05\alpha=0.05. We noticed that the CCC-op-ARCH(1)(1), CCC-op-ARCH(5)(5), and pw-fARCH(1)(1) models exhibited reasonably accurate coverage probabilities for the α=0.05\alpha=0.05 level, withstanding the highly volatile S&P500 (2018–2020) sample, especially relative to the historical quantile forecast. The CCC-op-ARCH(5)(5) and pw-fARCH(1)(1) model performed well at the α=0.01\alpha=0.01 level, with CCC-op-ARCH(5)(5) performing the best overall.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | CCC-op-ARCH(1)(1) | CCC-op-ARCH(5)(5) | pw-fARCH(1)(1) | Historical |
| Nominal α=0.05\alpha=0.05 | | | |  |
| S&P500 (2018–2020) | 0.130 | 0.037 | 0.080 | 0.103 |
| S&P500 (2022–2024) | 0.049 | 0.031 | 0.033 | 0.017 |
| Nominal α=0.01\alpha=0.01 | | | |  |
| S&P500 (2018–2020) | 0.098 | 0.015 | 0.048 | 0.038 |
| S&P500 (2022–2024) | 0.027 | 0.010 | 0.007 | 0.003 |

Table 1: One-step ahead average violation rates V​RVR computed as in equation ([6.1](#S6.E1 "In 6 Application to Intra-Day Return Data ‣ An operator-level ARCH Model")) for OCIDRs based on fitting two years (expanding) of data, and forecasting one-day ahead for a third year.



![Refer to caption](2603.10272v1/x9.png)


(a) 2022-2024

![Refer to caption](2603.10272v1/x10.png)


(b) 2018-2020

Figure 6: Comparisons of the average conditional quantile forecast curves V¯0.05\bar{V}\_{0.05} computed as in ([6.2](#S6.E2 "In 6 Application to Intra-Day Return Data ‣ An operator-level ARCH Model")) for each model. The left-hand panel is estimated from the 2022–2024 sample and the right-hand is estimated from the 2018–2020 sample.

To further measure the fidelity of these forecasts to the data and contrast the forecasts of the models, we also computed the average quantile curve

|  |  |  |  |
| --- | --- | --- | --- |
|  | V¯α​(t)=1Nt​e​s​t​∑j∈ test setV^j,α​(t)\displaystyle\bar{V}\_{\alpha}(t)=\frac{1}{N\_{test}}\sum\_{j\in\text{ test set}}\hat{V}\_{j,\alpha}(t) |  | (6.2) |

for each model. These curves are shown with α=0.05\alpha=0.05 in Figure [6](#S6.F6 "Figure 6 ‣ 6 Application to Intra-Day Return Data ‣ An operator-level ARCH Model") for each of the S&P 500 samples. We observed that for 2022–2024 sample, the CCC-op-ARCH models tended to estimate a larger contrast between the variance of the curves at the beginning and end of the day, especially when compared to the pw-fARCH(1)(1) model. In the 2018–2020 sample, the average curves V¯α​(t)\bar{V}\_{\alpha}(t) were somewhat flatter for each model, although in this case only the CCC-op-ARCH(5)(5) produced forecasts with approximately nominal coverage.

![Refer to caption](2603.10272v1/x11.png)


(a) CCC-op-ARCH(1)(1) Residuals

![Refer to caption](2603.10272v1/x12.png)


(b) CCC-op-ARCH(5)(5) Residuals

Figure 7: Plots of residual curves computed from the CCC-op-ARCH(p)(p) models as defined in ([6.3](#S6.E3 "In 6 Application to Intra-Day Return Data ‣ An operator-level ARCH Model")).

In order to assess the goodness-of-fit of the estimated CCC-op-ARCH models, we computed model residuals by applying a Moore–Penrose style pseudoinverse of Σ^i\hat{\Sigma}\_{i} to XiX\_{i}. Specifically, letting

|  |  |  |
| --- | --- | --- |
|  | Σ^i†=∑j=1K⟨Σ^i​(ej),ej⟩−1​(ej⊗ej),\hat{\Sigma}\_{i}^{\dagger}=\sum\_{j=1}^{K}\,\langle\hat{\Sigma}\_{i}(e\_{j}),e\_{j}\rangle^{-1}(e\_{j}\otimes e\_{j}), |  |

we defined residual curves

|  |  |  |  |
| --- | --- | --- | --- |
|  | ε^i​(t)=Σ^i†​(Xi)​(t),t∈[0,1],i∈{1+p,…,N}.\displaystyle\hat{\varepsilon}\_{i}(t)=\hat{\Sigma}\_{i}^{\dagger}(X\_{i})(t),\quad t\in[0,1],\quad i\in\{1+p,...,N\}. |  | (6.3) |

Plots of these residuals computed from CCC-op-ARCH(p)(p) models with p∈{1,5}p\in\{1,5\} are shown in Figure [7](#S6.F7 "Figure 7 ‣ 6 Application to Intra-Day Return Data ‣ An operator-level ARCH Model"). Visually CCC-op-ARCH(1)(1) residuals appeared to retain some volatility. To evaluate for remaining conditional heteroscedasticity in the residuals, we investigated for serial correlation in the sequence of squared residual curves Yi​(⋅)=ε^i2​(⋅)Y\_{i}(\cdot)=\hat{\varepsilon}\_{i}^{2}(\cdot). In particular, we computed the *Spherical AutoCorrelation Function* (SACF),

|  |  |  |
| --- | --- | --- |
|  | ρ~h=1N​∑i=1+pN−h⟨Yi−μ‖Yi−μ‖,Yi+h−μ‖Yi+h−μ‖⟩,\tilde{\rho}\_{h}=\frac{1}{N}\sum\_{i=1+p}^{N-h}\left\langle\frac{Y\_{i}-\mu}{\|Y\_{i}-\mu\|},\frac{Y\_{i+h}-\mu}{\|Y\_{i+h}-\mu\|}\right\rangle, |  |

as introduced in Yeh et al. ([2023](#bib.bib42)), which is a robust estimator of autocorrelation in sequences of curves. We additionally applied the white noise test of Kokoszka et al. ([2017](#bib.bib23)) to the squared residual curves (see Kim et al., [2023](#bib.bib21), for a review of these methods).

Plots of ρ~h\tilde{\rho}\_{h} as a function of hh are shown in Figure [8](#S6.F8 "Figure 8 ‣ 6 Application to Intra-Day Return Data ‣ An operator-level ARCH Model") for the squared residual curves derived from the S&P 500 data (2018–2020). While the original squared OCIDR curves Ri2R\_{i}^{2} as well as the squared residuals from the CCC-op-ARCH(1)(1) model exhibit strong serial correlation, the squared residuals from the CCC-op-ARCH(5)(5) model appear to be reasonably uncorrelated. Table [2](#S6.T2 "Table 2 ‣ 6 Application to Intra-Day Return Data ‣ An operator-level ARCH Model") shows the pp-values of white noise tests applied to the squared residual series, which also support the conclusion that the CCC-op-ARCH(1)(1) model does not entirely explain the observed conditional heteroscedasticity in the data, while the CCC-op-ARCH(5)(5) model appears to fit the data well. The results were similar for the other sample considered.

|  |  |  |  |
| --- | --- | --- | --- |
| Test | Original  Data2 | CCC-op-ARCH(1)(1)  Residuals2 | CCC-op-ARCH(5)(5)  Residuals2 |
| Maximal Lag == 3 | <0.001 | <0.001 | 0.070 |
| Maximal Lag == 10 | <0.001 | <0.001 | 0.280 |

Table 2: pp-values of the white noise of Kokoszka et al. ([2017](#bib.bib23)) applied to the squared residuals of models fit to the S&P 500 data 2018–2020 data. The results were similar 2022–2024 sample.



![Refer to caption](2603.10272v1/x_orig_wn.png)


(a) SACF of original Data

![Refer to caption](2603.10272v1/x_hat_wn.png)


(b) SACF of original squared Data

![Refer to caption](2603.10272v1/x13.png)


(c) CCC-op-ARCH(1)(1) model squared residuals

![Refer to caption](2603.10272v1/e_hat5_wn.png)


(d) CCC-op-ARCH(5)(5) model squared residuals

Figure 8: SACF Plots. Estimation of SACF for the original and CCC-op-ARCH models of the S&P 500 data, 2018–2020.

## 7 Discussion

This article introduces an ARCH model for processes taking values in general separable Hilbert spaces which we call operator-level ARCH (op-ARCH) models. A key advantage of this over previous functional conditional heteroscedasticity models is that it models the complete conditional covariance function, rather than only the pointwise variance. We establish sufficient conditions for strict stationarity. Weak stationarity and the existence of finite moments and weak dependence are also discussed. Consistent operator estimates are derived both in the finite- and infinite-dimensional setting via a Yule-Walker (YW) approach. An identifiability issue complicates the direct application of YW-type equations, even under Tikhonov regularization for ill-posedness. To address this, we propose a CCC-operator-level ARCH model, which permits consistent estimation via modified YW-type equations. In finite dimensions, parametric rates are achieved, while in infinite dimensions, explicit rates depending on eigenvalue decay and operator approximation are established. An example illustrating near-parametric rates in the infinite-dimensional case is given. After detailing several aspects of implementing the proposed methods, we present results of Monte-Carlo simulation experiments, which suggest that the proposed estimators indeed appear to be consistent. In an application to cumulative intra-day return curves, the CCC-op-ARCH(5)(5) model appeared to perform well in explaining/modeling the observed heteroscedasticity in the curves, and provides alternative forecasts of the daily volatility of the curves when compared to existing pointwise models.

The model may be extended to arbitrary separable Banach spaces, drawing on the estimation frameworks of Ruiz-Medina and Álvarez-Liébana ([2019](#bib.bib38)) and Dette et al. ([2020](#bib.bib11)). Further, it would be valuable to generalize our estimation procedure to more general H-S operators. Finally, extending the theory to operator-valued GARCH processes appears promising, and work in this direction is ongoing.

Our attention was focused with regards to estimation in the “diagonal situation” ([3.1](#S3.E1 "In Definition 3.1. ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")). Although our preliminary investigations suggest that, as in the multivariate setting, the full “VEC” model in ([2.8](#S2.E8 "In 2 General model and assumptions ‣ An operator-level ARCH Model")) is challenging to work with, other potential models are possible. These might include analogs of the BEKK, CCC, and DCC multivariate GARCH models, see Francq and Zakoïan ([2019](#bib.bib13), Ch. 10). We leave this as a broad avenue for future research.

#### Acknowledgements

Parts of the article were written while Sebastian Kühnert was employed at University of California, Davis.

#### Funding

Alexander Aue was partially supported by NSF DMS 2515821. Sebastian Kühnert was partially supported by TRR 391 Spatio-temporal Statistics for the Transition of Energy and Transport (Project number 520388526) funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation). Gregory Rice was partially supported by the Discovery Grant RGPIN 50503-11525 3100 105 from the Natural Science and Engineering Research Council of Canada.

## References

* Andersen et al. (2009)

  Andersen, T., R. Davis, J.-P. Kreiss, and T. Mikosch (2009).
  Handbook of Financial Time Series.
  Berlin: Springer.
* Andersen et al. (2024)

  Andersen, T. G., T. Su, V. Todorov, and Z. Zhang (2024).
  Intraday periodic volatility curves.
  Journal of the American Statistical Association 119(546), 1181–1191.
* Asai et al. (2006)

  Asai, M., M. McAleer, and J. Yu (2006).
  Multivariate stochastic volatility: A review.
  Econometric Reviews 25(2-3), 145–175.
* Aue et al. (2017)

  Aue, A., L. Horváth, and D. Pellatt (2017).
  Functional generalized autoregressive conditional heteroskedasticity.
  Journal of Time Series Analysis 38, 3–21.
* Bauwens et al. (2006)

  Bauwens, L., S. Laurent, and J. V. K. Rombouts (2006).
  Multivariate GARCH models: A survey.
  Journal of Applied Econometrics 21(1), 79–109.
* Billingsley (1995)

  Billingsley, P. (1995).
  Probability and Measure (3 ed.).
  New York: Wiley.
* Bollerslev (1986)

  Bollerslev, T. (1986).
  Generalized autoregressive conditional heteroskedasticity.
  Journal of Econometrics 31, 307–327.
* Bosq (2000)

  Bosq, D. (2000).
  Linear Processes in Function Spaces.
  Lecture Notes in Statistics. New York: Springer.
* Bosq and Blanke (2007)

  Bosq, D. and D. Blanke (2007).
  Inference and Prediction in Large Dimensions.
  Wiley Series in Probability and Statistics. Chichester, UK: John Wiley & Sons.
* Cerovecki et al. (2019)

  Cerovecki, C., C. Francq, S. Hörmann, and J.-M. Zakoïan (2019).
  Functional GARCH models: The quasi-likelihood approach and its applications.
  Journal of Econometrics 209(2), 353–375.
* Dette et al. (2020)

  Dette, H., K. Kokot, and A. Aue (2020).
  Functional data analysis in the banach space of continuous functions.
  Annals of Statistics 48(2), 1168–1192.
* Engle (1982)

  Engle, R. (1982).
  Autoregressive conditional heteroskedasticity with estimates of the variance of U.K. inflation.
  Econometrica 50(4), 987–1008.
* Francq and Zakoïan (2019)

  Francq, C. and J.-M. Zakoïan (2019).
  GARCH Models: Structure, Statistical Inference and Financial Applications. (2 ed.).
  Chichester: John Wiley & Sons Ltd.
* Gouriéroux (1997)

  Gouriéroux, C. (1997).
  ARCH Models and Financial Applications.
  New York: Springer.
* Hall and Meister (2007)

  Hall, P. and A. Meister (2007).
  A ridge-parameter approach to deconvolution.
  Annals of Statistics 35(4), 1535–1558.
* Hörmann et al. (2013)

  Hörmann, S., L. Horváth, and R. Reeder (2013).
  A functional version of the ARCH model.
  Econometric Theory 29(2), 267–288.
* Hörmann and Kokoszka (2010)

  Hörmann, S. and P. Kokoszka (2010).
  Weakly dependent functional data.
  Annals of Statistics 38, 1845–1884.
* Horváth and Kokoszka (2012)

  Horváth, L. and P. Kokoszka (2012).
  Inference for Functional Data with Applications.
  New York: Springer.
* Hsing and Eubank (2015)

  Hsing, T. and R. Eubank (2015).
  Theoretical Foundations of Functional Data Analysis, with an Introduction to Linear Operators.
  West Sussex: Wiley.
* Kearney et al. (2023)

  Kearney, F., H. L. Shang, and Y. Zhao (2023).
  Intraday fx volatility-curve forecasting with functional GARCH approaches.
  <https://arxiv.org/abs2311.18477>.
* Kim et al. (2023)

  Kim, M., P. Kokoszka, and G. Rice (2023).
  White noise testing for functional time series.
  Statistics Surveys 17, 119–168.
* Kingman (1973)

  Kingman, J. F. C. (1973).
  Subadditive ergodic theory.
  The Annals of Probability 1(6), 883–899.
* Kokoszka et al. (2017)

  Kokoszka, P., G. Rice, and H. L. Shang (2017).
  Inference for the autocovariance of a functional time series under conditional heteroscedasticity.
  Journal of Multivariate Analysis 162, 32–50.
* Kühnert (2019)

  Kühnert, S. (2019).
  Über funktionale ARCH- und GARCH-Zeitreihen.
  Ph. D. thesis, University of Rostock.
* Kühnert (2020)

  Kühnert, S. (2020).
  Functional ARCH and GARCH models: A Yule-Walker approach.
  Electronic Journal of Statistics 14(2), 4321–4360.
* Kühnert (2024)

  Kühnert, S. (2024).
  Estimating lagged (cross-)covariance operators of LpL^{p}-mm-approximable processes in Cartesian product Hilbert spaces.
  Journal of Time Series Analysis 46(3), 582–595.
* Kühnert et al. (2026)

  Kühnert, S., G. Rice, and A. Aue (2026).
  Estimating invertible processes in Hilbert spaces, with applications to functional ARMA processes.
  Bernoulli 32(2), 1523–1546.
* Kutta et al. (2022)

  Kutta, T., G. Dierickx, and H. Dette (2022).
  Statistical inference for the slope parameter in functional linear regression.
  Electronic Journal of Statistics 16(2), 5980–6042.
* Laksaci et al. (2025)

  Laksaci, A., F. Alshahrani, I. M. Almanjahie, and Z. Kaid (2025).
  Nonparametric multifunctional GARCH time series data analysis: Application to dynamic forecasting in financial data.
  AIMS Mathematics 10(11), 26459–26483.
* Li et al. (2025)

  Li, Z., H. Sun, and J. Liu (2025).
  A functional GARCH model with multiple constant parameters. Computational Economics.
* Liggett (1985)

  Liggett, T. (1985).
  An improved subadditive ergodic theorem.
  Annals of Probability 13(4), 1279–1285.
* Mas (2007)

  Mas, A. (2007).
  Weak convergence in the functional autoregressive model.
  Journal of Multivariate Analysis 98(6), 1231–1261.
* Moore (1920)

  Moore, E. H. (1920).
  On the reciprocal of the general algebraic matrix.
  Bulletin of the American Mathematical Society 26, 294–295.
* Penrose (1955)

  Penrose, R. (1955).
  A generalized inverse for matrices.
  Mathematical Proceedings of the Cambridge Philosophical Society 51(3), 406–413.
* R Core Team (2020)

  R Core Team (2020).
  R: A Language and Environment for Statistical Computing.
  Vienna, Austria: R Foundation for Statistical Computing.
* Reimherr (2015)

  Reimherr, M. (2015).
  Functional regression with repeated eigenvalues.
  Statistics & Probability Letters 107, 62–70.
* Rice et al. (2023)

  Rice, G., T. Wirjanto, and Y. Zhao (2023).
  Exploring volatility of crude oil intraday return curves: A functional GARCH-X model.
  Journal of Commodity Markets 32, 100361.
* Ruiz-Medina and Álvarez-Liébana (2019)

  Ruiz-Medina, M. and J. Álvarez-Liébana (2019).
  Strongly consistent autoregressive predictors in abstract Banach spaces.
  Journal of Multivariate Analysis 170, 186–201.
* Sun and Yu (2020)

  Sun, H. and B. Yu (2020).
  Volatility asymmetry in functional threshold GARCH model.
  Journal of Time Series Analysis 41(1), 95–109.
* Weidmann (1980)

  Weidmann, J. (1980).
  Linear Operators in Hilbert spaces.
  Graduate Texts in Mathematics, 68. New York-Berlin: Springer.
* Wu and Shao (2004)

  Wu, W. and X. Shao (2004).
  Limit theorems for iterated random functions.
  Journal of Applied Probability 41(2), 425–436.
* Yeh et al. (2023)

  Yeh, C.-K., G. Rice, and J. A. Dubin (2023).
  Functional spherical autocorrelation: A robust estimate of the autocorrelation of a functional time series.
  Electronic Journal of Statistics 17(1), 650 – 687.

## Appendix A Preliminaries

This section presents a few fundamental features required for our proofs. A compact operator A:ℋ→ℋ⋆,A:\mathcal{H}\to\mathcal{H}\_{\star}, where ℋ\mathcal{H} and ℋ⋆\mathcal{H}\_{\star} are separable Hilbert spaces, belongs to the *Schatten class of order* 1≤p<∞,1\leq p<\infty, denoted by 𝒮p,ℋ,ℋ⋆\mathcal{S}\_{p,\mathcal{H},\mathcal{H}\_{\star}} if its singular values s1​(A)≥s2​(A)≥⋯≥0s\_{1}(A)\geq s\_{2}(A)\geq\dots\geq 0 are pp-summable. The class 𝒮p,ℋ,ℋ⋆\mathcal{S}\_{p,\mathcal{H},\mathcal{H}\_{\star}} is equipped with the norm

|  |  |  |
| --- | --- | --- |
|  | ‖A‖p≔(∑i=1∞sip​(A))1/p,A∈𝒮p,ℋ,ℋ⋆.\|A\|\_{p}\coloneqq\bigg(\sum\_{i=1}^{\infty}s\_{i}^{p}(A)\bigg)^{\!1/p}\!,\quad A\in\mathcal{S}\_{p,\mathcal{H},\mathcal{H}\_{\star}}. |  |

The spaces of nuclear and H-S operators are 𝒩ℋ,ℋ⋆=𝒮1,ℋ,ℋ⋆\mathcal{N}\_{\mathcal{H},\mathcal{H}\_{\star}}=\mathcal{S}\_{1,\mathcal{H},\mathcal{H}\_{\star}} and 𝒮ℋ,ℋ⋆=𝒮2,ℋ,ℋ⋆\mathcal{S}\_{\mathcal{H},\mathcal{H}\_{\star}}=\mathcal{S}\_{2,\mathcal{H},\mathcal{H}\_{\star}}, respectively, and the space of bounded linear operators ℒℋ,ℋ⋆\mathcal{L}\_{\mathcal{H},\mathcal{H}\_{\star}} is denoted by 𝒮∞,ℋ,ℋ⋆\mathcal{S}\_{\infty,\mathcal{H},\mathcal{H}\_{\star}}, with norm ∥⋅∥∞≔∥⋅∥ℒ.\|\cdot\|\_{\infty}\coloneqq\|\cdot\|\_{\mathcal{L}}. It is well known that 𝒮q,ℋ,ℋ⋆⊊𝒮p,ℋ,ℋ⋆\mathcal{S}\_{q,\mathcal{H},\mathcal{H}\_{\star}}\subsetneq\mathcal{S}\_{p,\mathcal{H},\mathcal{H}\_{\star}} and ∥⋅∥p≤∥⋅∥q\|\cdot\|\_{p}\leq\|\cdot\|\_{q} for all 1≤p<q≤∞.1\leq p<q\leq\infty. These operators fulfill the following Hölder-type inequality (Weidmann, [1980](#bib.bib40), Section 7).

###### Lemma A.1.

Let ℋ1,ℋ2,ℋ3\mathcal{H}\_{1},\mathcal{H}\_{2},\mathcal{H}\_{3} be Hilbert spaces, and let p,q,r∈[1,∞]p,q,r\in[1,\infty] with 1p+1q=1r\tfrac{1}{p}+\tfrac{1}{q}=\tfrac{1}{r}, and 1∞≔0.\tfrac{1}{\infty}\coloneqq 0. Then, for any A∈𝒮p,ℋ2,ℋ3A\in\mathcal{S}\_{p,\mathcal{H}\_{2},\mathcal{H}\_{3}} and B∈𝒮q,ℋ1,ℋ2,B\in\mathcal{S}\_{q,\mathcal{H}\_{1},\mathcal{H}\_{2}}, it holds that A​B∈𝒮r,ℋ1,ℋ3AB\in\mathcal{S}\_{r,\mathcal{H}\_{1},\mathcal{H}\_{3}}, with

|  |  |  |
| --- | --- | --- |
|  | ‖A​B‖r≤‖A‖p​‖B‖q.\|AB\|\_{r}\leq\|A\|\_{p}\,\|B\|\_{q}. |  |

The next auxiliary result is a direct consequence of the properties of the given operators and norms, and we therefore omit the proof.

###### Lemma A.2.

Let m,n∈ℕ,m,n\in\mathbb{N}, suppose BjB\_{j} are bounded linear operators between Banach spaces, and let
Ci​jC\_{ij} be H-S operators for 1≤i≤m1\leq i\leq m, 1≤j≤n1\leq j\leq n. Then, the following holds:

* (a)

  The vector (B1​⋯​Bn)(B\_{1}\,\cdots\,B\_{n}) is a bounded linear operator between Banach spaces, with

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ‖(B1​⋯​Bn)‖ℒ≤∑i=1n‖Bi‖ℒ.\displaystyle\|(B\_{1}\,\cdots\,B\_{n})\|\_{\mathcal{L}}\leq\sum\_{i=1}^{n}\|B\_{i}\|\_{\mathcal{L}}\,. |  | (A.1) |
* (b)

  The matrix 𝑪≔(Ci​j)i,j=1m,n\boldsymbol{C}\coloneqq(C\_{ij})^{m,n}\_{i,j=1} is H-S, with

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ‖𝑪‖𝒮2=∑i=1m∑j=1n‖Ci​j‖𝒮2.\displaystyle\|\boldsymbol{C}\|^{2}\_{\mathcal{S}}=\sum\_{i=1}^{m}\sum\_{j=1}^{n}\|C\_{ij}\|^{2}\_{\mathcal{S}}\,. |  | (A.2) |

## Appendix B Notes

In the following, we illustrate the validity of the Markovian forms in the op-ARCH and the CCC-op-ARCH model.

###### Example B.1.

Let p=2.p=2.

* (a)

  From the definition of Σ0\Sigma\_{0} in the op-ARCH equation ([2.1](#S2.E1 "In Definition 2.1. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model")) and the elements introduced in Section [2](#S2 "2 General model and assumptions ‣ An operator-level ARCH Model"), it follows that

  |  |  |  |
  | --- | --- | --- |
  |  | 𝚫+𝚿​(X−1⊗2,[2])=[Δ0]+[α1α2𝕀0]​[X−1⊗2X−2⊗2]=[Δ+∑i=13αi​(X−i⊗2)X−1⊗2]=[Σ0X−1⊗2].\displaystyle\boldsymbol{\Delta}+\boldsymbol{\Psi}\big(X^{\otimes 2,[2]}\_{\!-1}\big)\;=\;\begin{bmatrix}\Delta\\ 0\end{bmatrix}+\begin{bmatrix}\alpha\_{1}\!&\!\alpha\_{2}\\ \mathbb{I}\!&\!0\\ \end{bmatrix}\!\!\begin{bmatrix}X^{\otimes 2}\_{-1}\\ X^{\otimes 2}\_{-2}\end{bmatrix}\;=\;\begin{bmatrix}\Delta+\sum^{3}\_{i=1}\alpha\_{i}(X^{\otimes 2}\_{-i})\\ X^{\otimes 2}\_{-1}\end{bmatrix}\;=\;\begin{bmatrix}\Sigma\_{0}\\ X^{\otimes 2}\_{-1}\end{bmatrix}. |  |

  Consequently, it holds indeed

  |  |  |  |
  | --- | --- | --- |
  |  | Υ0​(𝚫+𝚿​(X−1⊗2,[2]))=[Σ01/2​ε0⊗2​Σ01/2X−1⊗2]=[X0⊗2X−1⊗2]=X0⊗2,[2],\displaystyle\Upsilon\_{\!0}\big(\boldsymbol{\Delta}+\boldsymbol{\Psi}\big(X^{\otimes 2,[2]}\_{\!-1}\big)\big)\;=\;\begin{bmatrix}\Sigma^{1/2}\_{0}\varepsilon^{\otimes 2}\_{0}\Sigma^{1/2}\_{0}\\ X^{\otimes 2}\_{-1}\end{bmatrix}\;=\;\begin{bmatrix}X^{\otimes 2}\_{0}\\ X^{\otimes 2}\_{-1}\end{bmatrix}\;=\;X^{\otimes 2,[2]}\_{0}, |  |

  which is the Markovian form ([2.3](#S2.E3 "In 2 General model and assumptions ‣ An operator-level ARCH Model")) of the general op-ARCH(2)(2) model.
* (b)

  Let (Xk)(X\_{k}) be the CCC-op-ARCH(2)(2) process with operators

  |  |  |  |
  | --- | --- | --- |
  |  | Δ=∑j=1∞dj​(ej⊗ej),αi=∑j=1∞ai​j​j​(ej⊗ej)⊗𝒮(ej⊗ej),i=1,2,\Delta=\sum^{\infty}\_{j=1}d\_{j}(e\_{j}\otimes e\_{j}),\quad\alpha\_{i}=\sum^{\infty}\_{j=1}a\_{ijj}\,(e\_{j}\otimes e\_{j})\otimes\_{\mathcal{S}}(e\_{j}\otimes e\_{j}),\quad i=1,2, |  |

  where (dj)(d\_{j}), (a1​j​j)j(a\_{1jj})\_{j}, and (a2​j​j)j(a\_{2jj})\_{j} are square-summable sequences. By ([2.1](#S2.E1 "In Definition 2.1. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model")), and using

  |  |  |  |
  | --- | --- | --- |
  |  | ε0=∑ℓ=1∞⟨ε0,eℓ⟩​eℓ,Xn,d⊗2=∑ℓ=1∞⟨Xn,eℓ⟩2​(eℓ⊗eℓ),\varepsilon\_{0}=\sum^{\infty}\_{\ell=1}\,\langle\varepsilon\_{0},e\_{\ell}\rangle e\_{\ell},\quad X^{\otimes 2}\_{n,\mathrm{d}}=\sum^{\infty}\_{\ell=1}\,\langle X\_{n},e\_{\ell}\rangle^{2}(e\_{\ell}\otimes e\_{\ell}), |  |

  we obtain for any mm,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ⟨X0,em⟩2\displaystyle\langle X\_{0},e\_{m}\rangle^{2} | =⟨ε0,em⟩2​⟨Σ01/2​(em),em⟩2\displaystyle=\langle\varepsilon\_{0},e\_{m}\rangle^{2}\,\big\langle\Sigma\_{0}^{1/2}(e\_{m}),e\_{m}\big\rangle^{2} |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | =⟨ε0,em⟩2​[dm+a1​m​m​⟨X−1,em⟩2+a2​m​m​⟨X−2,em⟩2].\displaystyle=\langle\varepsilon\_{0},e\_{m}\rangle^{2}\Big[d\_{m}+a\_{1mm}\langle X\_{-1},e\_{m}\rangle^{2}+a\_{2mm}\langle X\_{-2},e\_{m}\rangle^{2}\Big]. |  |

  Consequently, by the definition of ψ0\psi\_{0} in ([3.4](#S3.E4 "In 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) and αi0=ψ0​(αi​(⋅))\alpha\_{i}^{0}=\psi\_{0}(\alpha\_{i}(\cdot)), i=1,2i=1,2, we obtain

  |  |  |  |
  | --- | --- | --- |
  |  | X0,d⊗2,[2]=[X0,d⊗2X−1,d⊗2]=[ψ0​(Δ)0]+[α10α20𝕀0]​[X−1,d⊗2X−2,d⊗2]=𝚫0+𝚿0​(X−1,d⊗2,[2]),X^{\otimes 2,[2]}\_{0,\mathrm{d}}\;=\;\begin{bmatrix}X^{\otimes 2}\_{0,\mathrm{d}}\\[3.00003pt] X^{\otimes 2}\_{-1,\mathrm{d}}\end{bmatrix}\;=\;\begin{bmatrix}\psi\_{0}(\Delta)\\[3.00003pt] 0\end{bmatrix}+\begin{bmatrix}\alpha\_{1}^{0}&\alpha\_{2}^{0}\\ \mathbb{I}&0\end{bmatrix}\begin{bmatrix}X^{\otimes 2}\_{-1,\mathrm{d}}\\[3.00003pt] X^{\otimes 2}\_{-2,\mathrm{d}}\end{bmatrix}\;=\;\boldsymbol{\Delta}\_{0}+\boldsymbol{\Psi}\_{\!0}\big(X^{\otimes 2,[2]}\_{-1,\mathrm{d}}\big), |  |

  which confirms the Markovian representation of the CCC-op-ARCH(2)(2) model for p=2p=2.

The estimates for 𝒞\mathscr{C} and 𝒟\mathscr{D} are based on a sample X1,…,XNX\_{1},\dots,X\_{N} of 𝑿=(Xk)⊂ℋ,\boldsymbol{X}=(X\_{k})\subset\mathcal{H}, with sample size N,N, defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞^≔1N​∑k=pN(Xk⊗2,[p]−m^p)⊗𝒮(Xk⊗2,[p]−m^p),\displaystyle\hat{\mathscr{C}}\coloneqq\frac{1}{N}\sum\_{k=p}^{N}\,\big(X^{\otimes 2,[p]}\_{\!k}\!-\hat{m}\_{p}\big)\otimes\_{\mathcal{S}}\big(X^{\otimes 2,[p]}\_{\!k}-\hat{m}\_{p}\big), |  | (B.1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟^≔1N​∑k=pN−1(Xk⊗2,[p]−m^p)⊗𝒮[(Xk+1⊗2−m^1′)​𝒞𝜺†​∐e1eK],\displaystyle\hat{\mathscr{D}}\coloneqq\frac{1}{N}\sum\_{k=p}^{N-1}\,\big(X^{\otimes 2,[p]}\_{\!k}-\hat{m}\_{p}\big)\otimes\_{\mathcal{S}}\bigg[\big(X^{\otimes 2}\_{\!k+1}-\hat{m}^{\prime}\_{1}\big)\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}}\,\bigg], |  | (B.2) |

respectively, with first moment estimates

|  |  |  |  |
| --- | --- | --- | --- |
|  | m^p≔1N​∑ℓ=pNXℓ⊗2,[p],m^1′≔1N​∑ℓ=pN−1Xℓ+1⊗2.\displaystyle\hat{m}\_{p}\coloneqq\frac{1}{N}\sum\_{\ell=p}^{N}X^{\otimes 2,[p]}\_{\ell},\qquad\hat{m}^{\prime}\_{1}\coloneqq\frac{1}{N}\sum\_{\ell=p}^{N-1}X^{\otimes 2}\_{\ell+1}. |  | (B.3) |

## Appendix C Proofs

Proving our results requires the consistent estimation of means and (lagged) (cross-)covariance operators. To this end, we formulate the following auxiliary results.

###### Lemma C.1.

Under the conditions of Proposition [3.3](#S3.Thmproposition3 "Proposition 3.3. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model") for ν=2\nu=2, for m^p\hat{m}\_{p} in ([B.3](#A2.E3 "In Appendix B Notes ‣ An operator-level ARCH Model")) holds

|  |  |  |
| --- | --- | --- |
|  | 𝔼⁡‖m^p−mp‖𝒮2=O​(N−1).\displaystyle\operatorname{\mathds{E}}\!\|\hat{m}\_{p}-m\_{p}\|^{2}\_{\mathcal{S}}=\mathrm{O}(N^{-1}). |  |

###### Proof.

The claim follows from mp=(m1,…,m1)⊤,m\_{p}=(m\_{1},\dots,m\_{1})^{\top}\!, 𝔼⁡‖m^p−mp‖𝒮2=p​𝔼⁡‖m^1−m1‖𝒮2,\operatorname{\mathds{E}}\!\|\hat{m}\_{p}-m\_{p}\|^{2}\_{\mathcal{S}}=p\operatorname{\mathds{E}}\!\|\hat{m}\_{1}-m\_{1}\|^{2}\_{\mathcal{S}}, and m1=𝒞𝑿,m\_{1}=\mathscr{C}\_{\!\boldsymbol{X}}, together with L2L^{2}-mm-approximability of 𝑿⊗2\boldsymbol{X}^{\otimes 2} by Proposition [3.3](#S3.Thmproposition3 "Proposition 3.3. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model"), and Kühnert ([2024](#bib.bib26), Theorem 3.1).
∎

###### Lemma C.2.

Let the conditions of Proposition [3.3](#S3.Thmproposition3 "Proposition 3.3. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model") for ν=4\nu=4 hold. Then, for the estimators 𝒞^\hat{\mathscr{C}} and 𝒟^\hat{\mathscr{D}} in ([B.1](#A2.E1 "In Appendix B Notes ‣ An operator-level ARCH Model"))–([B.2](#A2.E2 "In Appendix B Notes ‣ An operator-level ARCH Model")) holds

|  |  |  |
| --- | --- | --- |
|  | ‖𝒞^−𝒞‖𝒮=Oℙ​(N−1/2),‖𝒟^−𝒟‖𝒮=Oℙ​(aK−2​N−1/2).\displaystyle\|\hat{\mathscr{C}}-\mathscr{C}\|\_{\mathcal{S}}=\mathrm{O}\_{\operatorname{\mathds{P}}}(N^{-1/2}),\qquad\|\hat{\mathscr{D}}-\mathscr{D}\|\_{\mathcal{S}}=\mathrm{O}\_{\operatorname{\mathds{P}}}\big(a^{-2}\_{K}N^{-1/2}\big). |  |

###### Proof.

Due to L4L^{4}-mm-approximability of (Xk⊗2)(X^{\otimes 2}\_{\!k}) by Proposition [3.3](#S3.Thmproposition3 "Proposition 3.3. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model"), which transfers to the process (Xk⊗2,[p])k(X^{\otimes 2,[p]}\_{k})\_{k}, the claim holds for the estimator 𝒞^′\hat{\mathscr{C}}^{\prime} based on the true first moment mpm\_{p} instead of m^p\hat{m}\_{p} (Kühnert, [2024](#bib.bib26), Theorem 3.1). Moreover, according to the definitions of 𝒞^′,\hat{\mathscr{C}}^{\prime}, 𝒞^\hat{\mathscr{C}} and Xk⊗2,[p]X^{\otimes 2,[p]}\_{k}, the identity (a−b)⊗(c−d)=a⊗c−a⊗d−b⊗c+b⊗d(a-b)\otimes(c-d)=a\otimes c-a\otimes d-b\otimes c+b\otimes d, and ‖a⊗b‖𝒮=‖a‖​‖b‖\|a\otimes b\|\_{\mathcal{S}}=\|a\|\|b\| along with the Cauchy–Schwarz inequality, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝒞^−𝒞^′‖𝒮\displaystyle\|\hat{\mathscr{C}}-\hat{\mathscr{C}}^{\prime}\|\_{\mathcal{S}} | ≤1N​(∑k=pN‖m^p−mp‖𝒮​[2​‖Xk⊗2,[p]‖𝒮+‖m^p‖𝒮+‖mp‖𝒮])\displaystyle\leq\frac{1}{N}\left(\sum^{N}\_{k=p}\,\|\hat{m}\_{p}-m\_{p}\|\_{\mathcal{S}}\left[2\big\|X^{\otimes 2,[p]}\_{k}\big\|\_{\mathcal{S}}+\|\hat{m}\_{p}\|\_{\mathcal{S}}+\|m\_{p}\|\_{\mathcal{S}}\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =‖m^p−mp‖𝒮​[2N​(∑k=pN(∑ℓ=1p‖Xk+1−ℓ‖2)1/2)+‖m^p‖𝒮+‖mp‖𝒮].\displaystyle=\|\hat{m}\_{p}-m\_{p}\|\_{\mathcal{S}}\left[\frac{2}{N}\left(\sum^{N}\_{k=p}\left(\sum^{p}\_{\ell=1}\|X\_{k+1-\ell}\|^{2}\right)^{\!1/2}\right)+\|\hat{m}\_{p}\|\_{\mathcal{S}}+\|m\_{p}\|\_{\mathcal{S}}\right]. |  |

Further, since ‖Xk+1−ℓ‖=Oℙ​(1)\|X\_{k+1-\ell}\|=\mathrm{O}\_{\operatorname{\mathds{P}}}(1) for all k,ℓ,k,\ell, ‖mp‖𝒮2=p​‖m1‖𝒮2,\|m\_{p}\|^{2}\_{\mathcal{S}}=p\|m\_{1}\|^{2}\_{\mathcal{S}}, and ‖m^p−mp‖𝒮2=Oℙ​(N−1)\|\hat{m}\_{p}-m\_{p}\|^{2}\_{\mathcal{S}}=\mathrm{O}\_{\operatorname{\mathds{P}}}(N^{-1}) by Lemma [C.1](#A3.Thmlemma1 "Lemma C.1. ‣ Appendix C Proofs ‣ An operator-level ARCH Model"), we conclude ‖𝒞^−𝒞^′‖𝒮=Oℙ​(N−1/2).\|\hat{\mathscr{C}}-\hat{\mathscr{C}}^{\prime}\|\_{\mathcal{S}}=\mathrm{O}\_{\operatorname{\mathds{P}}}(N^{-1/2}). Hence, in fact

|  |  |  |
| --- | --- | --- |
|  | ‖𝒞^−𝒞‖𝒮≤‖𝒞^−𝒞^′‖𝒮+‖𝒞^′−𝒞‖𝒮=Oℙ​(N−1/2).\|\hat{\mathscr{C}}-\mathscr{C}\|\_{\mathcal{S}}\;\leq\;\|\hat{\mathscr{C}}-\hat{\mathscr{C}}^{\prime}\|\_{\mathcal{S}}+\|\hat{\mathscr{C}}^{\prime}-\mathscr{C}\|\_{\mathcal{S}}\;=\;\mathrm{O}\_{\operatorname{\mathds{P}}}(N^{-1/2}). |  |

We now turn to 𝒟\mathscr{D}. The L4L^{4}-mm-approximability of (Xk⊗2)(X^{\otimes 2}\_{k}) carries over to the process (Xk,𝜺⊗2)k(X^{\otimes 2}\_{k,\boldsymbol{\varepsilon}})\_{k}, where Xk,𝜺⊗2=Xk⊗2​𝒞𝜺†​∐e1eKX^{\otimes 2}\_{k,\boldsymbol{\varepsilon}}=X^{\otimes 2}\_{k}\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod\_{e\_{1}}^{e\_{K}}, since 𝒞𝜺†​∐e1eK\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod\_{e\_{1}}^{e\_{K}} is deterministic for any K,NK,N, and

|  |  |  |
| --- | --- | --- |
|  | ‖𝒞𝜺†​∐e1eK‖ℒ=sup1≤j≤K(aj+ϑN)−1=(aK+ϑN)−1≤aK−1.\bigg\|\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod\_{e\_{1}}^{e\_{K}}\bigg\|\_{\mathcal{L}}\;=\;\sup\_{1\leq j\leq K}(a\_{j}+\vartheta\_{\!N})^{-1}=(a\_{K}+\vartheta\_{\!N})^{-1}\;\leq\;a\_{K}^{-1}. |  |

Following the proof of Kühnert ([2024](#bib.bib26), Theorem 3.1), and using sub-multiplicativity of the operator norm, we find that for the estimator 𝒟^′\hat{\mathscr{D}}^{\prime} based on m1m\_{1} instead of m^1,\hat{m}\_{1}, it holds

|  |  |  |
| --- | --- | --- |
|  | ‖𝒟^′−𝒟‖𝒮=Oℙ​(aK−2​N−1/2),\|\hat{\mathscr{D}}^{\prime}-\mathscr{D}\|\_{\mathcal{S}}=\mathrm{O}\_{\operatorname{\mathds{P}}}\big(a\_{K}^{-2}N^{-1/2}\big), |  |

and by arguments analogous to above, the same rate holds for ‖𝒟^−𝒟‖𝒮\|\hat{\mathscr{D}}-\mathscr{D}\|\_{\mathcal{S}} as claimed.
∎

###### Proof of Proposition [3.1](#S3.Thmproposition1 "Proposition 3.1. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model").

The existence of the top Lyapunov exponent γ\gamma follows from Theorem 1.10 of Liggett ([1985](#bib.bib31)), whose assumptions must be verified. To this end, define

|  |  |  |
| --- | --- | --- |
|  | Xm,n≔ln⁡τ​(𝚿n−1∘𝚿n−2∘⋯∘𝚿m),0≤m<n,\displaystyle X\_{m,n}\coloneqq\ln\tau\big(\boldsymbol{\Psi}\_{\!n-1}\circ\boldsymbol{\Psi}\_{\!n-2}\circ\,\cdots\,\circ\boldsymbol{\Psi}\_{\!m}\big),\quad 0\leq m<n, |  |

where τ\tau denotes the functional in ([3.5](#S3.E5 "In 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) and 𝚿ℓ\boldsymbol{\Psi}\_{\!\ell} the maps in the Markovian representation ([3.2](#S3.E2 "In 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) of the CCC-op-ARCH(p)(p) model.

By the definition of 𝚿0,\boldsymbol{\Psi}\_{\!0}, we obtain for any A=(A1,…,Ap)⊤∈𝒮≥0,dp:A=(A\_{1},\dots,A\_{p})^{\top}\in\mathcal{S}^{p}\_{\geq 0,\mathrm{d}}\colon

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ2​(𝚿0)\displaystyle\tau^{2}(\boldsymbol{\Psi}\_{\!0}) | =sup‖A‖𝒮p≤1,A∈𝒮≥0,dp‖∑i=1pψ0​(αi​(Ai))‖𝒮2+∑i=1p−1‖Ai‖2\displaystyle=\sup\_{\|A\|\_{\mathcal{S}^{p}}\leq 1,\,A\in\mathcal{S}^{p}\_{\geq 0,\mathrm{d}}}\bigg\|\sum\_{i=1}^{p}\psi\_{0}(\alpha\_{i}(A\_{i}))\bigg\|^{2}\_{\mathcal{S}}\,+\,\sum\_{i=1}^{p-1}\|A\_{i}\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤1+sup‖A‖𝒮p≤1,A∈𝒮≥0,dp‖∑i=1pψ0​(αi​(Ai))‖𝒮2.\displaystyle\leq 1\,+\,\sup\_{\|A\|\_{\mathcal{S}^{p}}\leq 1,\,A\in\mathcal{S}^{p}\_{\geq 0,\mathrm{d}}}\bigg\|\sum\_{i=1}^{p}\psi\_{0}(\alpha\_{i}(A\_{i}))\bigg\|^{2}\_{\mathcal{S}}\,. |  |

Further, by the definition of ψ0\psi\_{0} and 𝜶=(α1​⋯​αp):𝒮p→𝒮\boldsymbol{\alpha}=(\alpha\_{1}~\cdots~\alpha\_{p}):\mathcal{S}^{p}\to\mathcal{S} in ([3.1](#S3.E1 "In Definition 3.1. ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")), elementary conversions yield

|  |  |  |
| --- | --- | --- |
|  | ‖∑i=1pψ0​(αi​(Ai))‖𝒮≤‖ε0‖2​‖𝜶​(A)‖𝒮≤‖ε0‖2​‖𝜶‖ℒ​‖A‖𝒮.\displaystyle\bigg\|\sum\_{i=1}^{p}\psi\_{0}(\alpha\_{i}(A\_{i}))\bigg\|\_{\mathcal{S}}\leq\,\|\varepsilon\_{0}\|^{2}\|\boldsymbol{\alpha}(A)\|\_{\mathcal{S}}\,\leq\,\|\varepsilon\_{0}\|^{2}\|\boldsymbol{\alpha}\|\_{\mathcal{L}}\|A\|\_{\mathcal{S}}\,. |  |

Hence, using ln⁡(1+x)≤x\ln(1+x)\leq x for x≥0,x\geq 0, and since ε0\varepsilon\_{0} has finite second moments, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼⁡(max⁡(0,X0,1))≤‖𝜶‖ℒ​𝔼⁡‖ε0‖2<∞.\displaystyle\operatorname{\mathds{E}}\!\big(\max(0,X\_{0,1})\big)\;\leq\;\|\boldsymbol{\alpha}\|\_{\mathcal{L}}\operatorname{\mathds{E}}\!\|\varepsilon\_{0}\|^{2}~<~\infty. |  | (C.1) |

Moreover, sub-multiplicativity of τ\tau implies sub-additivity in the sense that

|  |  |  |  |
| --- | --- | --- | --- |
|  | X0,n≤Xm,n+X0,m,0<m<n,\displaystyle X\_{0,n}\leq X\_{m,n}+X\_{0,m},\quad 0<m<n, |  | (C.2) |

and since all factors are i.i.d., we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Xm,m+k)k∈ℕ=d(Xm+1,m+k+1)k∈ℕ,m≥1,\displaystyle(X\_{m,m+k})\_{k\in\mathbb{N}}\,\stackrel{{\scriptstyle d}}{{=}}\,(X\_{m+1,m+k+1})\_{k\in\mathbb{N}},\qquad m\geq 1, |  | (C.3) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (Xn​k,(n+1)​k)n∈ℕ​ is strictly stationary for each ​k≥1.\displaystyle(X\_{nk,(n+1)k})\_{n\in\mathbb{N}}\text{ is strictly stationary for each }k\geq 1. |  | (C.4) |

By substituting ([C.1](#A3.E1 "In Proof of Proposition 3.1. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")) for (1.3) in Liggett ([1985](#bib.bib31)), and noting that ([C.2](#A3.E2 "In Proof of Proposition 3.1. ‣ Appendix C Proofs ‣ An operator-level ARCH Model"))–([C.4](#A3.E4 "In Proof of Proposition 3.1. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")) correspond to their conditions (1.7)–(1.9), respectively, all assumptions of their Theorem 1.10 are satisfied (see also their remarks on p. 1280). Thus, γ\gamma in ([3.6](#S3.E6 "In Proposition 3.1. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) exists, and the identity stated there holds. Finally, ([3.7](#S3.E7 "In Proposition 3.1. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) follows directly from Fekete’s sub-additive lemma.
∎

###### Proof of Theorem [3.1](#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model").

The proof is inspired by Cerovecki et al. ([2019](#bib.bib10)). Multiple applications of the Markovian form ([3.2](#S3.E2 "In 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) yield, by linearity of 𝚿k\boldsymbol{\Psi}\_{\!k},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk,d⊗2,[p]=𝚫k+∑ℓ=1∞𝚿k,ℓ​(𝚫k−ℓ),\displaystyle X^{\otimes 2,[p]}\_{\!k,\mathrm{d}}=\boldsymbol{\Delta}\_{k}+\sum\_{\ell=1}^{\infty}\boldsymbol{\Psi}\_{\!k,\ell}(\boldsymbol{\Delta}\_{k-\ell}), |  | (C.5) |

provided the series convergences almost surely (a.s.), and where 𝚿k,ℓ\boldsymbol{\Psi}\_{\!k,\ell} is defined as a composition of ℓ\ell factors through

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚿k,ℓ≔𝚿k∘𝚿k−1∘⋯∘𝚿k−ℓ+1,ℓ∈ℕ.\displaystyle\boldsymbol{\Psi}\_{\!k,\ell}\coloneqq\boldsymbol{\Psi}\_{\!k}\circ\boldsymbol{\Psi}\_{\!k-1}\circ\cdots\circ\boldsymbol{\Psi}\_{\!k-\ell+1},\quad\ell\in\mathbb{N}. |  | (C.6) |

By the definition of 𝚫k−ℓ\boldsymbol{\Delta}\_{k-\ell} in ([3.2](#S3.E2 "In 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model"))–([3.4](#S3.E4 "In 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")), using Δ=∑jdj​(ej⊗ej)\Delta=\sum\_{j}d\_{j}(e\_{j}\otimes e\_{j}) with positive square-summable sequence (dj)(d\_{j}) and non-degeneracy of the innovations by injectivity of the covariance operator (Assumption [2.1](#S2.Thmassumption1 "Assumption 2.1. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model")), we have ‖𝚫k−ℓ‖𝒮2=∑j⟨εk−ℓ,ej⟩4​dj2>0​a.s.,\|\boldsymbol{\Delta}\_{k-\ell}\|^{2}\_{\mathcal{S}}=\sum\_{j}\langle\varepsilon\_{k-\ell},e\_{j}\rangle^{4}d\_{j}^{2}>0~\text{a.s.}, thus 𝔼⁡‖𝚫k−ℓ‖𝒮≤‖Δ‖ℒ​𝔼⁡‖εk−ℓ‖2<∞\operatorname{\mathds{E}}\!\|\boldsymbol{\Delta}\_{k-\ell}\|\_{\mathcal{S}}\leq\|\Delta\|\_{\mathcal{L}}\operatorname{\mathds{E}}\!\|\varepsilon\_{k-\ell}\|^{2}<\infty, and in turn ln⁡‖𝚫k−ℓ‖𝒮∈(−∞,∞)\ln\|\boldsymbol{\Delta}\_{k-\ell}\|\_{\mathcal{S}}\in(-\infty,\infty) a.s. Subsequently, 1ℓ​ln⁡‖𝚫k−ℓ‖𝒮→0\frac{1}{\ell}\ln\|\boldsymbol{\Delta}\_{k-\ell}\|\_{\mathcal{S}}\to 0 a.s. as ℓ→∞.\ell\to\infty. By the definition of γ\gamma in ([3.6](#S3.E6 "In Proposition 3.1. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")), due to properties of τ\tau, and as (𝚿k)(\boldsymbol{\Psi}\_{\!k}) is i.i.d., it holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supℓ→∞1ℓ​ln⁡‖𝚿k,ℓ​(𝚫k−ℓ)‖𝒮\displaystyle\limsup\_{\ell\rightarrow\infty}\frac{1}{\ell}\ln\big\|\boldsymbol{\Psi}\_{\!k,\ell}(\boldsymbol{\Delta}\_{k-\ell})\big\|\_{\mathcal{S}} | ≤lim supℓ→∞1ℓ​ln⁡τ​(𝚿k,ℓ)+lim supℓ→∞1ℓ​ln⁡‖𝚫k−ℓ‖𝒮\displaystyle\leq\,\limsup\_{\ell\rightarrow\infty}\frac{1}{\ell}\ln\tau(\boldsymbol{\Psi}\_{\!k,\ell})\,+\,\limsup\_{\ell\rightarrow\infty}\frac{1}{\ell}\ln\!\|\boldsymbol{\Delta}\_{k-\ell}\|\_{\mathcal{S}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =γa.s.\displaystyle=\gamma\quad\mbox{a.s.} |  |

Hence, by ([3.8](#S3.E8 "In Theorem 3.1. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")),

|  |  |  |
| --- | --- | --- |
|  | lim supℓ→∞‖𝚿k,ℓ​(𝚫k−ℓ)‖𝒮1/ℓ≤eγ< 1a.s.,\limsup\_{\ell\to\infty}\big\|\boldsymbol{\Psi}\_{\!k,\ell}(\boldsymbol{\Delta}\_{k-\ell})\big\|\_{\mathcal{S}}^{1/\ell}\;\leq\;e^{\gamma}\;<\;1\quad\text{a.s.}, |  |

so the series in ([C.5](#A3.E5 "In Proof of Theorem 3.1. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")) converges almost surely by Cauchy’s rule, which guarantees the existence of a solution (Xk,d⊗2,[p])k(X^{\otimes 2,[p]}\_{\!k,\mathrm{d}})\_{k} to ([3.2](#S3.E2 "In 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) for the CCC-op-ARCH(p)(p) model. By causality and Billingsley ([1995](#bib.bib6), Theorem 36.4), this solution is strictly stationary, transferring to (Σk)(\Sigma\_{k}) as Σk∈σ​(Xk−1,d⊗2,[p])\Sigma\_{k}\in\sigma(X^{\otimes 2,[p]}\_{\!k-1,\mathrm{d}}), and to (Xk)(X\_{k}) via Xk=Σk1/2​(εk)X\_{k}=\Sigma\_{k}^{1/2}(\varepsilon\_{k}).

To show almost sure uniqueness of the solution, let (Yk)(Y\_{k}) be another solution of ([3.2](#S3.E2 "In 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")). For each kk and NN,

|  |  |  |
| --- | --- | --- |
|  | Yk=Xk,d,N⊗2,[p]+𝚿k,N​(Xk,d,N−1⊗2,[p]), where ​Xk,d,N⊗2,[p]≔𝚫k+∑ℓ=1N𝚿k,N​(𝚫k−ℓ).Y\_{k}=X^{\otimes 2,[p]}\_{\!k,\mathrm{d},N}+\boldsymbol{\Psi}\_{\!k,N}\big(X^{\otimes 2,[p]}\_{\!k,\mathrm{d},N-1}\big),\quad\mbox{ where~}X^{\otimes 2,[p]}\_{\!k,\mathrm{d},N}\coloneqq\boldsymbol{\Delta}\_{k}+\sum\_{\ell=1}^{N}\boldsymbol{\Psi}\_{\!k,N}(\boldsymbol{\Delta}\_{k-\ell}). |  |

Subsequently, due to the fact that γ<0\gamma<0 implies (as N→∞N\to\infty)

|  |  |  |
| --- | --- | --- |
|  | ‖Xk,d,N⊗2,[p]−Xk,d⊗2,[p]‖𝒮→0andτ​(𝚿k,N)→0a.s.,\big\|X^{\otimes 2,[p]}\_{\!k,\mathrm{d},N}-X^{\otimes 2,[p]}\_{\!k,\mathrm{d}}\big\|\_{\mathcal{S}}\to 0\quad\text{and}\quad\tau(\boldsymbol{\Psi}\_{\!k,N})\to 0\quad\text{a.s.}, |  |

we obtain

|  |  |  |
| --- | --- | --- |
|  | ‖Yk−Xk,d⊗2,[p]‖𝒮≤‖Xk,d,N⊗2,[p]−Xk,d⊗2,[p]‖𝒮+τ​(𝚿k,N)​‖Yk−N−1‖𝒮⟶N→∞0a.s.\displaystyle\big\|Y\_{k}-X^{\otimes 2,[p]}\_{\!k,\mathrm{d}}\big\|\_{\mathcal{S}}\;\leq\;\big\|X^{\otimes 2,[p]}\_{\!k,\mathrm{d},N}-X^{\otimes 2,[p]}\_{\!k,\mathrm{d}}\big\|\_{\mathcal{S}}\,+\,\tau(\boldsymbol{\Psi}\_{\!k,N})\|Y\_{k-N-1}\|\_{\mathcal{S}}~\stackrel{{\scriptstyle N\to\infty}}{{\longrightarrow}}~0\quad\text{a.s.} |  |

Thus, as the distribution of ‖Yk−N−1‖ℒ\|Y\_{k-N-1}\|\_{\mathcal{L}} is independent of NN, the solution is almost surely unique.
∎

###### Proof of Proposition [3.2](#S3.Thmproposition2 "Proposition 3.2. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model").

For n∈ℕn\in\mathbb{N} and ν>0,\nu>0, with 𝚿n,n=𝚿n∘𝚿n−1∘⋯∘𝚿1,\boldsymbol{\Psi}\_{\!n,n}=\boldsymbol{\Psi}\_{\!n}\circ\boldsymbol{\Psi}\_{\!n-1}\circ\cdots\circ\boldsymbol{\Psi}\_{\!1}, and using the representation ([3.7](#S3.E7 "In Proposition 3.1. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")), and Jensen’s inequality, it follows that

|  |  |  |
| --- | --- | --- |
|  | n​ν​γ≤ν​𝔼⁡ln⁡τ​(𝚿n,n)=𝔼⁡ln⁡τν​(𝚿n,n)≤ln⁡𝔼⁡τν​(𝚿n,n).\displaystyle n\nu\gamma\;\leq\;\nu\operatorname{\mathds{E}}\ln\tau(\boldsymbol{\Psi}\_{\!n,n})\;=\;\operatorname{\mathds{E}}\ln\tau^{\nu}(\boldsymbol{\Psi}\_{\!n,n})\;\leq\;\ln\operatorname{\mathds{E}}\tau^{\nu}(\boldsymbol{\Psi}\_{\!n,n})\,. |  |

Hence, ([3.9](#S3.E9 "In Proposition 3.2. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) implies ([3.8](#S3.E8 "In Theorem 3.1. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")).

Next, we show that ([3.10](#S3.E10 "In Proposition 3.2. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) implies ([3.9](#S3.E9 "In Proposition 3.2. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")). For illustrative purposes, first consider the case p=3.p=3. Then, for the composition of the operator-valued matrices 𝚿k\boldsymbol{\Psi}\_{\!k} in the Markovian form via the functions ψk,\psi\_{k}, with αk,i≔ψk∘αi,\alpha\_{k,i}\coloneqq\psi\_{k}\circ\alpha\_{i}, for 𝚿3,3=𝚿3∘𝚿2∘𝚿1\boldsymbol{\Psi}\_{\!3,3}=\boldsymbol{\Psi}\_{\!3}\circ\boldsymbol{\Psi}\_{\!2}\circ\boldsymbol{\Psi}\_{\!1} holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚿3,3\displaystyle\boldsymbol{\Psi}\_{\!3,3} | =[α3,1α3,2α3,3𝕀000𝕀0]​[α2,1α2,2α2,3𝕀000𝕀0]​[α1,1α1,2α1,3𝕀000𝕀0]\displaystyle\!=\!\!\begin{bmatrix}\alpha\_{3,1}\!\!&\!\alpha\_{3,2}\!\!&\!\alpha\_{3,3}\\ \mathbb{I}\!\!&\!0\!\!&\!0\\ 0\!\!&\!\mathbb{I}\!\!&\!0\end{bmatrix}\!\!\begin{bmatrix}\alpha\_{2,1}\!\!&\!\alpha\_{2,2}\!\!&\!\alpha\_{2,3}\\ \mathbb{I}\!\!&\!0\!\!&\!0\\ 0\!\!&\!\mathbb{I}\!\!&\!0\end{bmatrix}\!\!\begin{bmatrix}\alpha\_{1,1}\!\!&\!\alpha\_{1,2}\!\!&\!\alpha\_{1,3}\\ \mathbb{I}\!\!&\!0\!\!&\!0\\ 0\!\!&\!\mathbb{I}\!\!&\!0\end{bmatrix} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =[α3,1​(α2,1​α1,1+α2,2)+α3,2​α1,1+α3,3α3,1​(α2,1​α1,2+α2,3)+α3,2​α1,2α3,1​α2,1​α1,3+α3,2​α1,3α2,1​α1,1+α2,2α2,1​α1,2+α2,3α2,1​α1,3α1,1α1,2α1,3]\displaystyle\!=\!\!\begin{bmatrix}\alpha\_{3,1}(\alpha\_{2,1}\alpha\_{1,1}\!+\!\alpha\_{2,2})\!+\!\alpha\_{3,2}\alpha\_{1,1}\!+\!\alpha\_{3,3}\!\!&\!\alpha\_{3,1}(\alpha\_{2,1}\alpha\_{1,2}\!+\!\alpha\_{2,3})\!+\!\alpha\_{3,2}\alpha\_{1,2}\!\!&\!\alpha\_{3,1}\alpha\_{2,1}\alpha\_{1,3}\!+\!\alpha\_{3,2}\alpha\_{1,3}\\ \alpha\_{2,1}\alpha\_{1,1}\!+\!\alpha\_{2,2}\!\!&\!\alpha\_{2,1}\alpha\_{1,2}\!+\!\alpha\_{2,3}\!\!&\!\alpha\_{2,1}\alpha\_{1,3}\\ \alpha\_{1,1}\!\!&\!\alpha\_{1,2}\!\!&\!\alpha\_{1,3}\end{bmatrix} |  |

This structure is also given for general p.p. Namely, for the entries 𝚿p,p;i,j,\boldsymbol{\Psi}\_{\!p,p;i,j}, 1≤i,j≤p,1\leq i,j\leq p, of 𝚿p,p=𝚿p∘𝚿p−1∘⋯∘𝚿1\boldsymbol{\Psi}\_{\!p,p}=\boldsymbol{\Psi}\_{\!p}\circ\boldsymbol{\Psi}\_{\!p-1}\circ\cdots\circ\boldsymbol{\Psi}\_{\!1} for general p,p, holds by putting αk,ℓ=0\alpha\_{k,\ell}=0 for ℓ>p:\ell>p\colon

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝚿p,p;p,j\displaystyle\boldsymbol{\Psi}\_{\!p,p;p,j} | =α1,j,\displaystyle=\alpha\_{1,j}, | 1≤j≤p,\displaystyle\quad 1\leq j\leq p, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝚿p,p;p−ℓ,j\displaystyle\boldsymbol{\Psi}\_{\!p,p;p-\ell,j} | =(∑k=1ℓαℓ+1,k​𝚿p,p;p−ℓ+k,j)+αℓ+1,j+1,\displaystyle=\bigg(\sum^{\ell}\_{k=1}\alpha\_{\ell+1,k}\boldsymbol{\Psi}\_{\!p,p;p-\ell+k,j}\bigg)+\alpha\_{\ell+1,j+1}, | 1≤ℓ<p,1≤j≤p.\displaystyle\quad 1\leq\ell<p,~1\leq j\leq p. |  |

Further, by the definition of αk,i,\alpha\_{k,i}, for any i,k,i,k, it holds ‖αk,i‖ℒ≤‖𝜶‖ℒ​‖εk‖2,\|\alpha\_{k,i}\|\_{\mathcal{L}}\leq\|\boldsymbol{\alpha}\|\_{\mathcal{L}}\|\varepsilon\_{k}\|^{2}, and for any A=(A1,…,Ap)∈𝒮pA=(A\_{1},\dots,A\_{p})\in\mathcal{S}^{p} with ‖A‖𝒮≤1,\|A\|\_{\mathcal{S}}\leq 1, also

|  |  |  |
| --- | --- | --- |
|  | ‖∑i=1pαk,i​(Ai)‖𝒮≤‖𝜶‖ℒ​‖εk‖2.\bigg\|\sum^{p}\_{i=1}\alpha\_{k,i}(A\_{i})\bigg\|\_{\mathcal{S}}\leq\|\boldsymbol{\alpha}\|\_{\mathcal{L}}\|\varepsilon\_{k}\|^{2}. |  |

This along with the structure of 𝚿p,p\boldsymbol{\Psi}\_{\!p,p} (see the structure above for p=3),p=3), sub-multiplicativity of the given operators, and the fact that (εk)⊂L2(\varepsilon\_{k})\subset L^{2} is i.i.d., gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼⁡τ​(𝚿p,p)\displaystyle\operatorname{\mathds{E}}\tau(\boldsymbol{\Psi}\_{\!p,p}) | ≤𝔼⁡(sup‖A‖𝒮≤1‖𝚿p,p​(A)‖𝒮)\displaystyle\leq\operatorname{\mathds{E}}\!\bigg(\sup\_{\|A\|\_{\mathcal{S}}\leq 1}\!\big\|\boldsymbol{\Psi}\_{\!p,p}(A)\big\|\_{\mathcal{S}}\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖𝜶‖ℒ​𝔼⁡‖ε0‖2​∑ℓ=0p−1(p−ℓ)​(‖𝜶‖ℒ​𝔼⁡‖ε0‖2)ℓ.\displaystyle\leq\|\boldsymbol{\alpha}\|\_{\mathcal{L}}\operatorname{\mathds{E}}\!\|\varepsilon\_{0}\|^{2}\sum^{p-1}\_{\ell=0}\,(p-\ell)\big(\|\boldsymbol{\alpha}\|\_{\mathcal{L}}\operatorname{\mathds{E}}\!\|\varepsilon\_{0}\|^{2}\big)^{\ell}\,. |  |

Since this identity matches the claim, the proof is complete.
∎

###### Proof of Proposition [3.3](#S3.Thmproposition3 "Proposition 3.3. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model").

Throughout the entire proof, let ν>0.\nu>0. Further,

|  |  |  |
| --- | --- | --- |
|  | cn,ν≔{1,ν∈(0,1],nν−1,ν>1,n∈ℕ.\displaystyle c\_{n,\nu}\coloneqq\begin{cases}1,&\nu\in(0,1],\\ n^{\nu-1},&\nu>1,\end{cases}\qquad n\in\mathbb{N}. |  |

(a)  We first show that the diagonal part X0,d⊗2X^{\otimes 2}\_{0,\mathrm{d}} of X0⊗2X^{\otimes 2}\_{0} has a finite 2​ν2\nuth moment. Since τ\tau is compatible with the H-S norm, and sub-multiplicative, ([C.5](#A3.E5 "In Proof of Theorem 3.1. ‣ Appendix C Proofs ‣ An operator-level ARCH Model"))–([C.6](#A3.E6 "In Proof of Theorem 3.1. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")) and elementary inequalities yield, using cm,ν​cn,ν=cm​n,νc\_{m,\nu}c\_{n,\nu}=c\_{mn,\nu} for any m,nm,n and cm,ν≤cn,νc\_{m,\nu}\leq c\_{n,\nu} for m<nm<n, the upper bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖X0,d⊗2,[p]‖𝒮ν\displaystyle\big\|X^{\otimes 2,[p]}\_{0,\mathrm{d}}\big\|^{\nu}\_{\mathcal{S}} | ≤c3,ν​[‖𝚫0‖𝒮ν+(∑ℓ=1n−1τ​(𝚿0,ℓ)​‖𝚫−ℓ‖𝒮)ν+(∑ℓ=n∞τ​(𝚿0,ℓ)​‖𝚫−ℓ‖𝒮)ν]\displaystyle\leq c\_{3,\nu}\bigg[\,\|\boldsymbol{\Delta}\_{0}\|^{\nu}\_{\mathcal{S}}+\bigg(\sum\_{\ell=1}^{n-1}\tau(\boldsymbol{\Psi}\_{\!0,\ell})\|\boldsymbol{\Delta}\_{-\ell}\|\_{\mathcal{S}}\bigg)^{\!\nu}+\bigg(\sum\_{\ell=n}^{\infty}\tau(\boldsymbol{\Psi}\_{\!0,\ell})\|\boldsymbol{\Delta}\_{-\ell}\|\_{\mathcal{S}}\bigg)^{\!\nu}\,\bigg] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤c3​n,ν​[‖𝚫0‖𝒮ν+∑ℓ=1n−1‖𝚫−ℓ‖𝒮ν​∏m=1ℓτν​(𝚿1−m)+(∑ℓ=n∞τ​(𝚿0,ℓ)​‖𝚫−ℓ‖𝒮)ν].\displaystyle\leq c\_{3n,\nu}\bigg[\,\|\boldsymbol{\Delta}\_{0}\|^{\nu}\_{\mathcal{S}}+\sum\_{\ell=1}^{n-1}\|\boldsymbol{\Delta}\_{-\ell}\|^{\nu}\_{\mathcal{S}}\prod\_{m=1}^{\ell}\,\tau^{\nu}(\boldsymbol{\Psi}\_{\!1-m})+\bigg(\sum\_{\ell=n}^{\infty}\tau(\boldsymbol{\Psi}\_{\!0,\ell})\|\boldsymbol{\Delta}\_{-\ell}\|\_{\mathcal{S}}\bigg)^{\!\nu}\,\bigg]. |  | (C.7) |

For the first term (cf. the proof of Theorem [3.1](#S3.Thmtheorem1 "Theorem 3.1. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼⁡‖𝚫0‖𝒮ν≤‖Δ‖ℒν​𝔼⁡‖ε0‖2​ν<∞.\displaystyle\operatorname{\mathds{E}}\!\|\boldsymbol{\Delta}\_{0}\|^{\nu}\_{\mathcal{S}}\;\leq\;\|\Delta\|^{\nu}\_{\mathcal{L}}\operatorname{\mathds{E}}\!\|\varepsilon\_{0}\|^{2\nu}\;<\;\infty. |  | (C.8) |

Moreover, by arguments from Proposition [3.1](#S3.Thmproposition1 "Proposition 3.1. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼⁡τν​(𝚿0)≤c2,ν/2​(1+‖𝜶‖ℒν​𝔼⁡‖ε0‖2​ν)<∞.\displaystyle\operatorname{\mathds{E}}\tau^{\nu}(\boldsymbol{\Psi}\_{\!0})\;\leq\;c\_{2,\nu/2}\big(1+\|\boldsymbol{\alpha}\|^{\nu}\_{\mathcal{L}}\operatorname{\mathds{E}}\!\|\varepsilon\_{0}\|^{2\nu}\big)\;<\;\infty. |  | (C.9) |

Since 𝚫k,𝚿k∈σ​(εk)\boldsymbol{\Delta}\_{k},\boldsymbol{\Psi}\_{\!k}\in\sigma(\varepsilon\_{k}), the sequences (𝚫k)(\boldsymbol{\Delta}\_{k}) and (𝚿k)(\boldsymbol{\Psi}\_{\!k}) are i.i.d., and independent across different time indices. Hence, for the second term in ([C.7](#A3.E7 "In Proof of Proposition 3.3. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")),

|  |  |  |
| --- | --- | --- |
|  | 𝔼⁡(∑ℓ=1n−1‖𝚫−ℓ‖𝒮ν​∏m=1ℓτν​(𝚿1−m))=𝔼⁡‖𝚫0‖𝒮ν​∑ℓ=1n−1[𝔼⁡τν​(𝚿0)]ℓ<∞.\displaystyle\operatorname{\mathds{E}}\bigg(\sum\_{\ell=1}^{n-1}\|\boldsymbol{\Delta}\_{-\ell}\|^{\nu}\_{\mathcal{S}}\prod\_{m=1}^{\ell}\,\tau^{\nu}(\boldsymbol{\Psi}\_{\!1-m})\bigg)\;=\;\operatorname{\mathds{E}}\!\|\boldsymbol{\Delta}\_{0}\|^{\nu}\_{\mathcal{S}}\sum\_{\ell=1}^{n-1}\big[\operatorname{\mathds{E}}\tau^{\nu}(\boldsymbol{\Psi}\_{\!0})\big]^{\ell}\;<\;\infty. |  |

We now treat the last term of ([C.7](#A3.E7 "In Proof of Proposition 3.3. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")). The condition ([3.9](#S3.E9 "In Proposition 3.2. ‣ 3.1 Strict stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξn,ν≔𝔼⁡τν​(𝚿n,n)<1,\displaystyle\xi\_{n,\nu}\coloneqq\operatorname{\mathds{E}}\tau^{\nu}(\boldsymbol{\Psi}\_{\!n,n})<1, |  | (C.10) |

where 𝚿k,ℓ=𝚿k∘𝚿k−1∘⋯∘𝚿k−ℓ+1\boldsymbol{\Psi}\_{\!k,\ell}=\boldsymbol{\Psi}\_{\!k}\circ\boldsymbol{\Psi}\_{\!k-1}\circ\cdots\circ\boldsymbol{\Psi}\_{\!k-\ell+1}. To use this structure, we decompose each 𝚿0,ℓ\boldsymbol{\Psi}\_{\!0,\ell} into a part whose length is a multiple of nn and a remainder. Therefore, by writing ℓ=⌊ℓ/n⌋​n+ℓmodn,\ell=\lfloor\ell/n\rfloor n+\ell\bmod n, we obtain the factorization

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚿0,ℓ\displaystyle\boldsymbol{\Psi}\_{\!0,\ell} | =(𝚿0∘𝚿−1∘⋯∘𝚿−⌊ℓ/n⌋​n+1)∘(𝚿−⌊ℓ/n⌋​n∘⋯∘𝚿−ℓ+1)\displaystyle=\big(\boldsymbol{\Psi}\_{\!0}\circ\boldsymbol{\Psi}\_{\!-1}\circ\cdots\circ\boldsymbol{\Psi}\_{\!-\lfloor\ell/n\rfloor n+1}\big)\circ\big(\boldsymbol{\Psi}\_{\!-\lfloor\ell/n\rfloor n}\circ\cdots\circ\boldsymbol{\Psi}\_{\!-\ell+1}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝚿0,⌊ℓ/n⌋​n∘𝚿−⌊ℓ/n⌋​n,ℓmodn.\displaystyle=\boldsymbol{\Psi}\_{\!0,\lfloor\ell/n\rfloor n}\circ\boldsymbol{\Psi}\_{\!-\lfloor\ell/n\rfloor n,\;\ell\bmod n}. |  |

The first composition contains exactly ⌊ℓ/n⌋​n\lfloor\ell/n\rfloor n operators and thus consists of ⌊ℓ/n⌋\lfloor\ell/n\rfloor blocks of length nn, while the second contains the remainder ℓmodn\ell\bmod n terms. By using sub-multiplicativity of τ\tau, independence, and ([C.9](#A3.E9 "In Proof of Proposition 3.3. ‣ Appendix C Proofs ‣ An operator-level ARCH Model"))–([C.10](#A3.E10 "In Proof of Proposition 3.3. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")), we therefore obtain for any ν∈(0,1],\nu\in(0,1], since |ξn,ν|<1,|\xi\_{n,\nu}|<1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼(∑ℓ=n∞τ(𝚿0,ℓ)∥𝚫−ℓ∥𝒮)ν\displaystyle\operatorname{\mathds{E}}\bigg(\sum\_{\ell=n}^{\infty}\tau(\boldsymbol{\Psi}\_{\!0,\ell})\|\boldsymbol{\Delta}\_{-\ell}\|\_{\mathcal{S}}\bigg)^{\!\nu} | ≤𝔼⁡‖𝚫0‖𝒮ν​∑ℓ=n∞𝔼⁡τν​(𝚿0,ℓ)\displaystyle\leq\operatorname{\mathds{E}}\!\|\boldsymbol{\Delta}\_{0}\|^{\nu}\_{\mathcal{S}}\sum\_{\ell=n}^{\infty}\operatorname{\mathds{E}}\tau^{\nu}(\boldsymbol{\Psi}\_{\!0,\ell}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼⁡‖𝚫0‖𝒮ν​(∑k=1n−1[𝔼⁡τν​(𝚿0)]k)​∑ℓ=1∞ξn,νℓ\displaystyle\leq\operatorname{\mathds{E}}\!\|\boldsymbol{\Delta}\_{0}\|^{\nu}\_{\mathcal{S}}\bigg(\sum\_{k=1}^{n-1}\big[\operatorname{\mathds{E}}\tau^{\nu}(\boldsymbol{\Psi}\_{\!0})\big]^{k}\bigg)\sum\_{\ell=1}^{\infty}\,\xi^{\ell}\_{n,\nu} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <∞,\displaystyle<\infty, |  |

and for ν>1\nu>1, the Minkowski’s inequality yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼(∑ℓ=n∞τ(𝚿0,ℓ)∥𝚫−ℓ∥𝒮)ν\displaystyle\operatorname{\mathds{E}}\bigg(\sum\_{\ell=n}^{\infty}\tau(\boldsymbol{\Psi}\_{\!0,\ell})\|\boldsymbol{\Delta}\_{-\ell}\|\_{\mathcal{S}}\bigg)^{\!\nu} | ≤𝔼⁡‖𝚫0‖𝒮ν​(∑ℓ=n∞[𝔼⁡τν​(𝚿0,ℓ)]1/ν)ν\displaystyle\leq\operatorname{\mathds{E}}\!\|\boldsymbol{\Delta}\_{0}\|^{\nu}\_{\mathcal{S}}\bigg(\sum\_{\ell=n}^{\infty}\big[\operatorname{\mathds{E}}\tau^{\nu}(\boldsymbol{\Psi}\_{\!0,\ell})\big]^{1/\nu}\bigg)^{\!\nu} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼⁡‖𝚫0‖𝒮ν​(∑k=1n−1[𝔼⁡τν​(𝚿0)]k)​(∑ℓ=1∞ξn,νℓ/ν)ν\displaystyle\leq\operatorname{\mathds{E}}\!\|\boldsymbol{\Delta}\_{0}\|^{\nu}\_{\mathcal{S}}\bigg(\sum\_{k=1}^{n-1}\big[\operatorname{\mathds{E}}\tau^{\nu}(\boldsymbol{\Psi}\_{\!0})\big]^{k}\bigg)\bigg(\sum\_{\ell=1}^{\infty}\,\xi\_{n,\nu}^{\ell/\nu}\bigg)^{\!\nu} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <∞.\displaystyle<\infty. |  |

Altogether, all expectations in ([C.7](#A3.E7 "In Proof of Proposition 3.3. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")) are finite, and consequently, 𝔼⁡‖X0,d⊗2,[p]‖𝒮ν<∞.\operatorname{\mathds{E}}\!\|X^{\otimes 2,[p]}\_{0,\mathrm{d}}\|^{\nu}\_{\mathcal{S}}<\infty. Next, due to Σk=Δ+𝜶​(Xk−1⊗2,[p]),\Sigma\_{k}=\Delta+\boldsymbol{\alpha}(X^{\otimes 2,[p]}\_{k-1}), and since 𝜶\boldsymbol{\alpha} annihilates the off-diagonal part of Xk−1⊗2,[p]X^{\otimes 2,[p]}\_{k-1} (see ([3.1](#S3.E1 "In Definition 3.1. ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model"))), under our assumptions, it holds

|  |  |  |
| --- | --- | --- |
|  | 𝔼⁡‖Σ0‖𝒮ν≤c2,ν​(‖Δ‖𝒮ν+‖𝜶‖ℒν​𝔼⁡‖X0,d⊗2,[p]‖𝒮ν)<∞.\displaystyle\operatorname{\mathds{E}}\!\|\Sigma\_{0}\|^{\nu}\_{\mathcal{S}}\;\leq\;c\_{2,\nu}\Big(\|\Delta\|^{\nu}\_{\mathcal{S}}+\|\boldsymbol{\alpha}\|^{\nu}\_{\mathcal{L}}\operatorname{\mathds{E}}\!\|X^{\otimes 2,[p]}\_{0,\mathrm{d}}\|^{\nu}\_{\mathcal{S}}\Big)~<~\infty. |  |

Further, since ‖Σ01/2‖4=‖Σ0‖𝒮1/2\|\Sigma^{1/2}\_{0}\|\_{4}=\|\Sigma\_{0}\|^{1/2}\_{\mathcal{S}}, we obtain 𝔼⁡‖Σ01/2‖42​ν<∞\operatorname{\mathds{E}}\!\|\Sigma^{1/2}\_{0}\|^{2\nu}\_{4}<\infty. Finally, as ‖X0⊗2‖𝒮=‖X0‖2\|X^{\otimes 2}\_{0}\|\_{\mathcal{S}}=\|X\_{0}\|^{2} and X0=Σ01/2​(ε0),X\_{0}=\Sigma^{1/2}\_{0}(\varepsilon\_{0}), with Σ0\Sigma\_{0} being independent of ε0\varepsilon\_{0}, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼⁡‖X0⊗2‖𝒮ν=𝔼⁡‖X0‖2​ν≤𝔼⁡‖Σ01/2‖42​ν​𝔼⁡‖ε0‖2​ν=𝔼⁡‖Σ0‖𝒮ν​𝔼⁡‖ε0‖2​ν<∞.\displaystyle\operatorname{\mathds{E}}\!\|X^{\otimes 2}\_{0}\|^{\nu}\_{\mathcal{S}}\;=\;\operatorname{\mathds{E}}\!\|X\_{0}\|^{2\nu}\;\leq\;\operatorname{\mathds{E}}\!\|\Sigma^{1/2}\_{0}\|^{2\nu}\_{4}\operatorname{\mathds{E}}\!\|\varepsilon\_{0}\|^{2\nu}\;=\;\operatorname{\mathds{E}}\!\|\Sigma\_{0}\|^{\nu}\_{\mathcal{S}}\operatorname{\mathds{E}}\!\|\varepsilon\_{0}\|^{2\nu}~<~\infty. |  |

(b)  Here too, as a preliminary step, we focus on the diagonal part Xk,d⊗2X^{\otimes 2}\_{k,\mathrm{d}} of Xk⊗2.X^{\otimes 2}\_{k}. By definition of each 𝚿m\boldsymbol{\Psi}\_{\!m} it holds 𝚿k,ℓ=𝚿k∘𝚿k−1∘⋯∘𝚿k−ℓ+1=f​(εk,εk−1,…,εk−ℓ+1)\boldsymbol{\Psi}\_{\!k,\ell}=\boldsymbol{\Psi}\_{\!k}\circ\boldsymbol{\Psi}\_{\!k-1}\circ\cdots\circ\boldsymbol{\Psi}\_{\!k-\ell+1}=f(\varepsilon\_{k},\varepsilon\_{k-1},\dots,\varepsilon\_{k-\ell+1}) for some measurable function f.f. Therefore, 𝚿k,ℓ(m)=f​(εk,εk−1,…,εk−m+1,εm′,εm−1′,…,εm−ℓ+1′)\boldsymbol{\Psi}^{(m)}\_{\!k,\ell}=f(\varepsilon\_{k},\varepsilon\_{k-1},\dots,\varepsilon\_{k-m+1},\varepsilon^{\prime}\_{m},\varepsilon^{\prime}\_{m-1},\dots,\varepsilon^{\prime}\_{m-\ell+1}) in the spirit of LpL^{p}-mm-approximability (cf. Section [3.2](#S3.SS2 "3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")). Since 𝚫−ℓ\boldsymbol{\Delta}\_{-\ell} depends only on ε−ℓ\varepsilon\_{-\ell}, with 𝚫−ℓ′\boldsymbol{\Delta}^{\prime}\_{-\ell} defined analogously but using ε−ℓ′\varepsilon^{\prime}\_{-\ell}, it follows from ([C.5](#A3.E5 "In Proof of Theorem 3.1. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | X0,d⊗2,[p]−X0,d⊗2,[p],(m)\displaystyle X^{\otimes 2,[p]}\_{0,\mathrm{d}}-X^{\otimes 2,[p],(m)}\_{0,\mathrm{d}} | =∑ℓ>m[𝚿0,ℓ​(𝚫−ℓ)−𝚿0,ℓ(m)​(𝚫−ℓ′)],m∈ℕ.\displaystyle=\sum\_{\ell>m}\Big[\boldsymbol{\Psi}\_{\!0,\ell}(\boldsymbol{\Delta}\_{-\ell})-\boldsymbol{\Psi}^{(m)}\_{\!0,\ell}(\boldsymbol{\Delta}^{\prime}\_{-\ell})\Big],\quad m\in\mathbb{N}. |  |

Since 𝚿0,ℓ\boldsymbol{\Psi}\_{\!0,\ell} and 𝚫−ℓ\boldsymbol{\Delta}\_{-\ell} are independent, and as 𝚿0,ℓ​(𝚫−ℓ)=d𝚿0,ℓ(m)​(𝚫−ℓ′)\boldsymbol{\Psi}\_{\!0,\ell}(\boldsymbol{\Delta}\_{-\ell})\stackrel{{\scriptstyle d}}{{=}}\boldsymbol{\Psi}^{(m)}\_{\!0,\ell}(\boldsymbol{\Delta}^{\prime}\_{-\ell}) and 𝚫−ℓ=d𝚫0\boldsymbol{\Delta}\_{-\ell}\stackrel{{\scriptstyle d}}{{=}}\boldsymbol{\Delta}\_{0} for any ℓ,m\ell,m, we obtain for any ν>0\nu>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼⁡‖𝚿0,ℓ​(𝚫−ℓ)−𝚿0,ℓ(m)​(𝚫−ℓ′)‖𝒮ν\displaystyle\operatorname{\mathds{E}}\!\big\|\boldsymbol{\Psi}\_{\!0,\ell}(\boldsymbol{\Delta}\_{-\ell})-\boldsymbol{\Psi}^{(m)}\_{\!0,\ell}(\boldsymbol{\Delta}^{\prime}\_{-\ell})\big\|^{\nu}\_{\mathcal{S}} | ≤2​c2,ν​𝔼⁡τν​(𝚿0,ℓ)​𝔼⁡‖𝚫0‖𝒮ν\displaystyle\leq 2c\_{2,\nu}\operatorname{\mathds{E}}\tau^{\nu}(\boldsymbol{\Psi}\_{\!0,\ell})\operatorname{\mathds{E}}\!\|\boldsymbol{\Delta}\_{0}\|^{\nu}\_{\mathcal{S}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​c2,ν​‖Δ‖ℒν​𝔼⁡‖ε0‖2​ν​(𝔼⁡τν​(𝚿0))ℓmodn​ξn,ν⌊ℓ/n⌋.\displaystyle\leq 2c\_{2,\nu}\|\Delta\|^{\nu}\_{\mathcal{L}}\operatorname{\mathds{E}}\!\|\varepsilon\_{0}\|^{2\nu}\big(\operatorname{\mathds{E}}\tau^{\nu}(\boldsymbol{\Psi}\_{\!0})\big)^{\ell\bmod n}\xi^{\lfloor\ell/n\rfloor}\_{n,\nu}. |  |

Further, according to |ξn,ν|<1|\xi\_{n,\nu}|<1,

|  |  |  |
| --- | --- | --- |
|  | ∑ℓ>mξn,ν⌊ℓ/n⌋≤n​∑ℓ>m(ξn,ν1/n)ℓ∝(ξn,ν1/n)m,\sum\_{\ell>m}\xi^{\lfloor\ell/n\rfloor}\_{n,\nu}\;\leq\;n\sum\_{\ell>m}(\xi^{1/n}\_{n,\nu})^{\ell}\;\propto\;(\xi^{1/n}\_{n,\nu})^{m}, |  |

and since ((𝔼⁡τν​(𝚿0))ℓmodn)ℓ((\operatorname{\mathds{E}}\tau^{\nu}(\boldsymbol{\Psi}\_{\!0}))^{\ell\bmod n})\_{\ell} is uniformly bounded by some CC, for ν∈(0,1]\nu\in(0,1],

|  |  |  |
| --- | --- | --- |
|  | 𝔼⁡‖X0,d⊗2,[p]−X0,d⊗2,[p],(m)‖𝒮ν≤ 2​C​‖Δ‖ℒν​𝔼⁡‖ε0‖2​ν​∑ℓ>mξn,ν⌊ℓ/n⌋∝(ξn,ν1/n)m.\displaystyle\operatorname{\mathds{E}}\!\big\|X^{\otimes 2,[p]}\_{0,\mathrm{d}}-X^{\otimes 2,[p],(m)}\_{0,\mathrm{d}}\big\|^{\nu}\_{\mathcal{S}}\;\leq\;2C\|\Delta\|^{\nu}\_{\mathcal{L}}\operatorname{\mathds{E}}\!\|\varepsilon\_{0}\|^{2\nu}\sum\_{\ell>m}\xi^{\lfloor\ell/n\rfloor}\_{n,\nu}\;\propto\;(\xi^{1/n}\_{n,\nu})^{m}. |  |

Thus (Xk,d⊗2,[p])k(X^{\otimes 2,[p]}\_{k,\mathrm{d}})\_{k} is LνL^{\nu}-mm-approximable with geometrically decaying approximation errors for ν∈(0,1]\nu\in(0,1]. The case ν>1\nu>1 follows analogously (cf. proof of part (a)).

This property transfers to (Σk)(\Sigma\_{k}) because Σk=Δ+𝜶​(Xk−1⊗2,[p]),\Sigma\_{k}=\Delta+\boldsymbol{\alpha}(X^{\otimes 2,[p]}\_{k-1}), Σk(m)≔Δ+𝜶​(Xk−1⊗2,[p],(m))\Sigma^{(m)}\_{k}\coloneqq\Delta+\boldsymbol{\alpha}(X^{\otimes 2,[p],(m)}\_{k-1}) and the observations in part (a) lead to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼⁡‖Σ0−Σ0(m)‖𝒮ν\displaystyle\operatorname{\mathds{E}}\!\big\|\Sigma\_{0}-\Sigma^{(m)}\_{0}\big\|^{\nu}\_{\mathcal{S}} | ≤‖𝜶‖ℒν​𝔼⁡‖X0,d⊗2,[p]−X0,d⊗2,[p],(m)‖𝒮ν.\displaystyle\leq\|\boldsymbol{\alpha}\|^{\nu}\_{\mathcal{L}}\operatorname{\mathds{E}}\!\big\|X^{\otimes 2,[p]}\_{0,\mathrm{d}}-X^{\otimes 2,[p],(m)}\_{0,\mathrm{d}}\big\|^{\nu}\_{\mathcal{S}}. |  |

Further, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼⁡‖Σ01/2−(Σ01/2)(m)‖42​ν\displaystyle\operatorname{\mathds{E}}\!\big\|\Sigma^{1/2}\_{0}-(\Sigma^{1/2}\_{0})^{(m)}\big\|^{2\nu}\_{4} | ≤𝔼⁡‖Σ0−Σ0(m)‖𝒮ν,\displaystyle\leq\operatorname{\mathds{E}}\!\big\|\Sigma\_{0}-\Sigma^{(m)}\_{0}\big\|^{\nu}\_{\mathcal{S}}, |  |

where ∥⋅∥4\|\cdot\|\_{4} is the norm of the Schatten class operators of order 4, and with Xk(m)≔(Σk1/2)(m)​(εk),X^{(m)}\_{k}\coloneqq(\Sigma^{1/2}\_{k})^{(m)}(\varepsilon\_{k}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼⁡‖X0−X0(m)‖2​ν\displaystyle\operatorname{\mathds{E}}\!\big\|X\_{0}-X^{(m)}\_{0}\big\|^{2\nu}\! | ≤𝔼⁡‖Σ01/2−(Σ01/2)(m)‖42​ν​𝔼⁡‖ε0‖2​ν,\displaystyle\leq\operatorname{\mathds{E}}\!\big\|\Sigma^{1/2}\_{0}-(\Sigma^{1/2}\_{0})^{(m)}\big\|^{2\nu}\_{4}\operatorname{\mathds{E}}\!\|\varepsilon\_{0}\|^{2\nu}, |  |

so the claims for (Σk1/2)(\Sigma^{1/2}\_{k}) and (Xk)(X\_{k}) hold. Finally, the claim for (Xk⊗2)(X^{\otimes 2}\_{k}) follows from, e.g., Hörmann and Kokoszka ([2010](#bib.bib17), Lemma 2.1).
∎

###### Proof of Proposition [3.4](#S3.Thmproposition4 "Proposition 3.4. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model").

Recall that (Xk)(X\_{k}) is a CCC-op-ARCH(p)(p) process that is weakly stationary, i.e., 𝔼⁡(X0)=𝔼⁡(Xk)\operatorname{\mathds{E}}(X\_{0})=\operatorname{\mathds{E}}(X\_{k}) for all kk and 𝒞Xk,Xℓ=𝒞X0,Xℓ−k\mathscr{C}\_{X\_{k},X\_{\ell}}=\mathscr{C}\_{X\_{0},X\_{\ell-k}} for all k,ℓ.k,\ell.

Since X0=Σ01/2​(ε0)X\_{0}=\Sigma^{1/2}\_{0}(\varepsilon\_{0}) and Σ0\Sigma\_{0} and ε0\varepsilon\_{0} are independent, (Xk)(X\_{k}) is centered. Moreover, independence of εn\varepsilon\_{n} and Σm\Sigma\_{m} for n>mn>m implies 𝒞Xk,Xℓ=0\mathscr{C}\_{X\_{k},X\_{\ell}}=0 for k≠ℓk\neq\ell, and positive definiteness of Σ0\Sigma\_{0} yields 𝔼⁡‖X0‖2=𝔼⁡⟨Σ0​(ε0),ε0⟩>0.\operatorname{\mathds{E}}\!\|X\_{0}\|^{2}=\operatorname{\mathds{E}}\langle\Sigma\_{0}(\varepsilon\_{0}),\varepsilon\_{0}\rangle>0. Hence, (Xk)(X\_{k}) is a WWN.

Since expectation commutes with bounded linear operators, weak stationarity gives

|  |  |  |
| --- | --- | --- |
|  | 𝔼⁡(Σk)=Δ+∑i=1pαi​(𝔼⁡(Xk−i⊗2))=Δ+∑i=1pαi​(𝒞𝑿),k∈ℤ,\operatorname{\mathds{E}}(\Sigma\_{k})\;=\;\Delta+\sum\_{i=1}^{p}\alpha\_{i}(\operatorname{\mathds{E}}(X^{\otimes 2}\_{k-i}))\;=\;\Delta+\sum\_{i=1}^{p}\alpha\_{i}(\mathscr{C}\_{\!\boldsymbol{X}}),\quad k\in\mathbb{Z}, |  |

establishing 𝝁𝚺=𝔼⁡(Σ0)=𝔼⁡(Σk)\boldsymbol{\mu}\_{\boldsymbol{\Sigma}}=\operatorname{\mathds{E}}(\Sigma\_{0})=\operatorname{\mathds{E}}(\Sigma\_{k}) for all kk and the representation ([3.12](#S3.E12 "In Proposition 3.4. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")).

To obtain the explicit form of 𝝁𝚺\boldsymbol{\mu}\_{\boldsymbol{\Sigma}}, note that Assumption [2.2](#S2.Thmassumption2 "Assumption 2.2. ‣ 2 General model and assumptions ‣ An operator-level ARCH Model") implies 𝒞𝑿=𝝁𝚺​𝒞𝜺.\mathscr{C}\_{\!\boldsymbol{X}}=\boldsymbol{\mu}\_{\boldsymbol{\Sigma}}\mathscr{C}\_{\boldsymbol{\varepsilon}}. Combined with ([3.1](#S3.E1 "In Definition 3.1. ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")), this gives αi​(𝒞𝑿)=𝝁𝚺​αi​(𝒞𝜺)\alpha\_{i}(\mathscr{C}\_{\!\boldsymbol{X}})=\boldsymbol{\mu}\_{\boldsymbol{\Sigma}}\alpha\_{i}(\mathscr{C}\_{\boldsymbol{\varepsilon}}) for all i.i. Inserting this into ([3.12](#S3.E12 "In Proposition 3.4. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")) and using ([3.13](#S3.E13 "In Proposition 3.4. ‣ 3.2 Existence of moments, weak dependence, and weak stationarity ‣ 3 CCC-op-ARCH model and structure ‣ An operator-level ARCH Model")), the resulting Neumann series converges and we obtain

|  |  |  |
| --- | --- | --- |
|  | μ𝚺=Δ+μ𝚺​∑i=1pαi​(𝒞𝜺)=(𝕀−∑i=1pαi​(𝒞𝜺))−1​(Δ).\displaystyle\mu\_{\boldsymbol{\Sigma}}\;=\;\Delta+\mu\_{\boldsymbol{\Sigma}}\sum\_{i=1}^{p}\alpha\_{i}(\mathscr{C}\_{\boldsymbol{\varepsilon}})\;=\;\bigg(\mathbb{I}-\sum\_{i=1}^{p}\alpha\_{i}(\mathscr{C}\_{\boldsymbol{\varepsilon}})\bigg)^{-1}(\Delta). |  |

Thus, all claims follow.
∎

###### Proof of Theorem [4.1](#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model").

From the definition of 𝜶^d,\hat{\boldsymbol{\alpha}}\_{\mathrm{d}}, ([4.12](#S4.E12 "In 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")), and 𝜶~d=diag∗⁡(𝜶d),\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}}=\operatorname{\mathrm{d}iag}^{\ast}(\boldsymbol{\alpha}\_{\mathrm{d}}), it follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜶^d−𝜶~d=diag∗⁡(𝒟^d​[𝒞^d−1−𝒞d−1])+diag∗⁡((𝒟^d−𝒟d)​𝒞d−1)+diag∗⁡(ℛd​𝒞d−1),\displaystyle\hat{\boldsymbol{\alpha}}\_{\mathrm{d}}-\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}}=\operatorname{\mathrm{d}iag}^{\ast}\!\Big(\hat{\mathscr{D}}\_{\mathrm{d}}\big[\hat{\mathscr{C}}^{-1}\_{\mathrm{d}}-\mathscr{C}^{-1}\_{\mathrm{d}}\big]\Big)+\operatorname{\mathrm{d}iag}^{\ast}\!\Big((\hat{\mathscr{D}}\_{\mathrm{d}}-\mathscr{D}\_{\mathrm{d}})\mathscr{C}^{-1}\_{\mathrm{d}}\Big)+\operatorname{\mathrm{d}iag}^{\ast}\!\Big(\mathscr{R}\_{\mathrm{d}}\mathscr{C}^{-1}\_{\mathrm{d}}\Big), |  | (C.11) |

where the inverses are well-defined for sufficiently large NN by Assumption [4.1](#S4.Thmassumption1 "Assumption 4.1. ‣ 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model"). Let ∥⋅∥\|\cdot\| be the induced matrix norm. Note that 𝒞d=diag∗⁡𝒞​diag\mathscr{C}\_{\mathrm{d}}=\operatorname{\mathrm{d}iag}^{\ast}\!\mathscr{C}\operatorname{\mathrm{d}iag}, 𝒟d=diag∗⁡𝒟​diag\mathscr{D}\_{\mathrm{d}}=\operatorname{\mathrm{d}iag}^{\ast}\!\mathscr{D}\operatorname{\mathrm{d}iag}, and ℛd=diag∗⁡ℛ​diag\mathscr{R}\_{\mathrm{d}}=\operatorname{\mathrm{d}iag}^{\ast}\!\mathscr{R}\operatorname{\mathrm{d}iag} (with analogous empirical versions). For the remainder ℛ\mathscr{R} in ([4.8](#S4.E8 "In 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")), it follows from 𝜶=𝜶K\boldsymbol{\alpha}=\boldsymbol{\alpha}\_{K} in ([4.10](#S4.E10 "In 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")), the operator definitions, the H-S norm, and ϑN=O​(N−1/2)\vartheta\_{\!N}=\mathrm{O}(N^{-1/2}), as in the proof of Proposition [4.1](#S4.Thmproposition1 "Proposition 4.1. ‣ 4.3 Estimation of the Intercept term ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ℛ‖𝒩\displaystyle\|\mathscr{R}\|\_{\mathcal{N}} | ≤𝔼⁡‖X~0⊗2,[p]‖𝒮​‖[𝜶K​(X~0⊗2,[p])]​(𝒞𝜺‡​∐e1eK−𝕀)‖𝒮\displaystyle\leq\operatorname{\mathds{E}}\!\big\|\tilde{X}^{\otimes 2,[p]}\_{0}\big\|\_{\mathcal{S}}\,\bigg\|\Big[\boldsymbol{\alpha}\_{K}\big(\tilde{X}^{\otimes 2,[p]}\_{0}\big)\Big]\bigg(\mathscr{C}^{\ddagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}}\,-\;\mathbb{I}\bigg)\bigg\|\_{\mathcal{S}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ϑN​aK−1​𝔼⁡‖X~0⊗2,[p]‖𝒮​(∑m=1K‖∑i=1p∑ℓ=1Kai​ℓ​⟨X~1−i⊗2,eℓ⊗eℓ⟩𝒮​(eℓ⊗eℓ)​(em)‖2)1/2\displaystyle\leq\vartheta\_{\!N}a^{-1}\_{K}\operatorname{\mathds{E}}\!\big\|\tilde{X}^{\otimes 2,[p]}\_{0}\big\|\_{\mathcal{S}}\,\Bigg(\sum^{K}\_{m=1}\,\bigg\|\sum^{p}\_{i=1}\sum^{K}\_{\ell=1}\,a\_{i\ell}\langle\tilde{X}^{\otimes 2}\_{1-i},e\_{\ell}\otimes e\_{\ell}\rangle\_{\!\mathcal{S}}\,(e\_{\ell}\otimes e\_{\ell})(e\_{m})\bigg\|^{2}\Bigg)^{\!\!1/2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ϑN​aK−1​𝔼⁡‖X~0⊗2,[p]‖𝒮​‖𝜶K​(X~0⊗2,[p])‖𝒮\displaystyle=\vartheta\_{\!N}a^{-1}\_{\!K}\operatorname{\mathds{E}}\!\big\|\tilde{X}^{\otimes 2,[p]}\_{0}\big\|\_{\mathcal{S}}\big\|\boldsymbol{\alpha}\_{K}\big(\tilde{X}^{\otimes 2,[p]}\_{0}\big)\big\|\_{\mathcal{S}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ϑN​aK−1​‖𝜶K‖𝒮​𝔼⁡‖X~0⊗2,[p]‖𝒮2\displaystyle\leq\vartheta\_{\!N}a^{-1}\_{\!K}\|\boldsymbol{\alpha}\_{K}\|\_{\mathcal{S}}\operatorname{\mathds{E}}\!\big\|\tilde{X}^{\otimes 2,[p]}\_{0}\big\|^{2}\_{\mathcal{S}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =O​(N−1/2).\displaystyle=\mathrm{O}(N^{-1/2})\,. |  |

Subsequently, by the definition of ℛd,\mathscr{R}\_{\mathrm{d}}, and due to elementary conversions, we have

|  |  |  |
| --- | --- | --- |
|  | ‖ℛd‖≤‖diag‖ℒ2​‖ℛ‖𝒩=O​(N−1/2).\displaystyle\|\mathscr{R}\_{\mathrm{d}}\|\;\leq\;\|\!\operatorname{\mathrm{d}iag}\!\|^{2}\_{\mathcal{L}}\,\|\mathscr{R}\|\_{\mathcal{N}}\;=\;\mathrm{O}(N^{-1/2}). |  |

Hence, due to ‖𝒞^−𝒞‖=Oℙ​(N−1/2)\|\hat{\mathscr{C}}-\mathscr{C}\|=\mathrm{O}\_{\operatorname{\mathds{P}}}(N^{-1/2}) and ‖𝒟^−𝒟‖=Oℙ​(N−1/2)\|\hat{\mathscr{D}}-\mathscr{D}\|=\mathrm{O}\_{\operatorname{\mathds{P}}}(N^{-1/2}) for fixed KK by Lemma [C.2](#A3.Thmlemma2 "Lemma C.2. ‣ Appendix C Proofs ‣ An operator-level ARCH Model"), and the definition of 𝒞d,𝒟d\mathscr{C}\_{\mathrm{d}},\mathscr{D}\_{\mathrm{d}}, along with their empirical counterparts, it holds

|  |  |  |
| --- | --- | --- |
|  | max⁡{‖𝒟^d−𝒟d‖,‖𝒞^d−𝒞d‖,‖ℛd‖}=Oℙ​(N−1/2).\max\Big\{\,\|\hat{\mathscr{D}}\_{\mathrm{d}}-\mathscr{D}\_{\mathrm{d}}\|,\,\|\hat{\mathscr{C}}\_{\mathrm{d}}-\mathscr{C}\_{\mathrm{d}}\|,\,\|\mathscr{R}\_{\mathrm{d}}\|\Big\}=\mathrm{O}\_{\operatorname{\mathds{P}}}(N^{-1/2}). |  |

Further, with EN≔𝒞d−1​(𝒞^d−𝒞d),E\_{N}\coloneqq\mathscr{C}^{-1}\_{\mathrm{d}}(\hat{\mathscr{C}}\_{\mathrm{d}}-\mathscr{C}\_{\mathrm{d}}), where 𝒞d\mathscr{C}\_{\mathrm{d}} is non-singular, it holds 𝒞^d=𝒞d​(𝕀+EN).\hat{\mathscr{C}}\_{\mathrm{d}}=\mathscr{C}\_{\mathrm{d}}(\mathbb{I}+E\_{N}). The Neumann series

|  |  |  |
| --- | --- | --- |
|  | (𝕀+EN)−1=∑k=0∞(−EN)k,\big(\mathbb{I}+E\_{N}\big)^{-1}=\sum^{\infty}\_{k=0}\,(-E\_{N})^{k}, |  |

with EN0≔𝕀,E^{0}\_{N}\coloneqq\mathbb{I}, converges (for k→∞k\to\infty) with high probability as ‖EN‖=Oℙ​(N−1/2).\|E\_{N}\|=\mathrm{O}\_{\operatorname{\mathds{P}}}(N^{-1/2}). Thus, due to sub-multiplicativity of the induced matrix norm and the triangle inequality, it holds

|  |  |  |
| --- | --- | --- |
|  | ‖𝒞^d−1−𝒞d−1‖=‖((𝕀+EN)−1−𝕀)​𝒞d−1‖≤‖EN‖​‖𝒞d−1‖​∑k=0∞‖EN‖k=Oℙ​(N−1/2).\displaystyle\big\|\hat{\mathscr{C}}^{-1}\_{\mathrm{d}}-\mathscr{C}^{-1}\_{\mathrm{d}}\big\|\;=\;\big\|\big((\mathbb{I}+E\_{N})^{-1}-\mathbb{I}\big)\mathscr{C}^{-1}\_{\mathrm{d}}\big\|\;\leq\;\|E\_{N}\|\big\|\mathscr{C}^{-1}\_{\mathrm{d}}\big\|\sum^{\infty}\_{k=0}\|E\_{N}\|^{k}\;=\;\mathrm{O}\_{\operatorname{\mathds{P}}}(N^{-1/2})\,. |  |

Combining all above with the identity ([C.11](#A3.E11 "In Proof of Theorem 4.1. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")), together with the triangle inequality and sub-multiplicativity, the claim follows for the induced matrix norm. Further, as all norms on finite-dimensional spaces are equivalent, the result extends to any matrix norm.
∎

###### Proof of Theorem [4.2](#S4.Thmtheorem2 "Theorem 4.2. ‣ 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model").

Recall that 𝒟^d=diag∗⁡𝒟^​diag\hat{\mathscr{D}}\_{\mathrm{d}}=\operatorname{\mathrm{d}iag}^{\ast}\hat{\mathscr{D}}\,\operatorname{\mathrm{d}iag} and 𝒞^d=diag∗⁡𝒞^​diag\hat{\mathscr{C}}\_{\mathrm{d}}=\operatorname{\mathrm{d}iag}^{\ast}\hat{\mathscr{C}}\,\operatorname{\mathrm{d}iag}, where 𝒟^\hat{\mathscr{D}} and 𝒞^\hat{\mathscr{C}} are given in ([B.1](#A2.E1 "In Appendix B Notes ‣ An operator-level ARCH Model")) and ([B.2](#A2.E2 "In Appendix B Notes ‣ An operator-level ARCH Model")), respectively. Also, 𝒞^d†=(𝒞^d+ϑN​𝕀)−1\hat{\mathscr{C}}^{\dagger}\_{\mathrm{d}}=(\hat{\mathscr{C}}\_{\mathrm{d}}+\vartheta\_{\!N}\mathbb{I})^{-1} with ϑN→0\vartheta\_{\!N}\to 0 and ϑN>0\vartheta\_{\!N}>0. The eigenpairs (λ^j,d,c^j,d)(\hat{\lambda}\_{j,\mathrm{d}},\hat{c}\_{j,\mathrm{d}}) and (λj,d,cj,d)(\lambda\_{j,\mathrm{d}},c\_{j,\mathrm{d}}) correspond to 𝒞^d\hat{\mathscr{C}}\_{\mathrm{d}} and 𝒞d\mathscr{C}\_{\mathrm{d}}, respectively, with λ^1,d>⋯>λ^K,d>λ^K+1,d≥0\hat{\lambda}\_{1,\mathrm{d}}>\dots>\hat{\lambda}\_{K,\mathrm{d}}>\hat{\lambda}\_{K+1,\mathrm{d}}\geq 0 by Assumption [4.2](#S4.Thmassumption2 "Assumption 4.2. ‣ 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model") (b), where all λj,d\lambda\_{j,\mathrm{d}} are positive due to injectivity of 𝒞d\mathscr{C}\_{\mathrm{d}}. Define 𝒞d†≔(𝒞d+ϑN​𝕀)−1\mathscr{C}^{\dagger}\_{\mathrm{d}}\coloneqq(\mathscr{C}\_{\mathrm{d}}+\vartheta\_{\!N}\mathbb{I})^{-1}, 𝒞d‡≔𝒞d​𝒞d†\mathscr{C}^{\ddagger}\_{\mathrm{d}}\coloneqq\mathscr{C}\_{\mathrm{d}}\mathscr{C}^{\dagger}\_{\mathrm{d}}, and let 𝜶pK\boldsymbol{\alpha}^{K}\_{p} be the finite-dimensional diagonal operator in ([4.10](#S4.E10 "In 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")). Moreover, 𝜶d,K\boldsymbol{\alpha}\_{\mathrm{d},K} denotes 𝜶d\boldsymbol{\alpha}\_{\mathrm{d}} with ai​j=0a\_{ij}=0 for j>Kj>K, and set 𝜶~d,K≔diag∗⁡(𝜶d,K)\tilde{\boldsymbol{\alpha}}\_{\mathrm{d},K}\coloneqq\operatorname{\mathrm{d}iag}^{\ast}(\boldsymbol{\alpha}\_{\mathrm{d},K}). Then, using definitions ([4.15](#S4.E15 "In 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model"))–([4.16](#S4.E16 "In 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")), the YW-type equation ([4.12](#S4.E12 "In 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")), 𝜶~d=diag∗⁡(𝜶d)\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}}=\operatorname{\mathrm{d}iag}^{\ast}(\boldsymbol{\alpha}\_{\mathrm{d}}), and standard conversions, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜶^d−𝜶~d\displaystyle\hat{\boldsymbol{\alpha}}\_{\mathrm{d}}-\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}} | =diag∗⁡((𝒟^d−𝒟d)​𝒞^d†​∐c^1,dc^K,d)+diag∗⁡(𝒟d​(𝒞^d†​∐c^1,dc^K,d−𝒞d†​∐c1,dcK,d))\displaystyle=\operatorname{\mathrm{d}iag}^{\ast}\!\Bigg(\big(\hat{\mathscr{D}}\_{\mathrm{d}}-\mathscr{D}\_{\mathrm{d}}\big)\hat{\mathscr{C}}^{\dagger}\_{\mathrm{d}}\!\coprod^{\hat{c}\_{K,\mathrm{d}}}\_{\hat{c}\_{1,\mathrm{d}}}\Bigg)\,+\,\operatorname{\mathrm{d}iag}^{\ast}\Bigg(\mathscr{D}\_{\mathrm{d}}\bigg(\hat{\mathscr{C}}^{\dagger}\_{\mathrm{d}}\!\coprod^{\hat{c}\_{K,\mathrm{d}}}\_{\hat{c}\_{1,\mathrm{d}}}-\,\mathscr{C}^{\dagger}\_{\mathrm{d}}\!\coprod^{c\_{K,\mathrm{d}}}\_{c\_{1,\mathrm{d}}}\bigg)\Bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +diag∗⁡(ℛd​𝒞d†​∐c1,dcK,d)+diag∗⁡(𝜶d,K​(𝒞d‡​∐c1,dcK,d−𝕀))+𝜶~dK−𝜶~d,\displaystyle\phantom{=~}+\operatorname{\mathrm{d}iag}^{\ast}\!\Bigg(\mathscr{R}\_{\mathrm{d}}\mathscr{C}^{\dagger}\_{\mathrm{d}}\!\coprod^{c\_{K,\mathrm{d}}}\_{c\_{1,\mathrm{d}}}\Bigg)\,+\,\operatorname{\mathrm{d}iag}^{\ast}\!\Bigg(\boldsymbol{\alpha}\_{\mathrm{d},K}\bigg(\mathscr{C}^{\ddagger}\_{\mathrm{d}}\!\coprod^{c\_{K,\mathrm{d}}}\_{c\_{1,\mathrm{d}}}-\mathbb{I}\bigg)\Bigg)+\,\tilde{\boldsymbol{\alpha}}^{K}\_{\mathrm{d}}-\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}}\,, |  |

where ℛdK\mathscr{R}^{K}\_{\mathrm{d}} denotes the remainder from Theorem [4.1](#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model"). By the triangle inequality, the operator-valued Hölder’s inequality, and since diag∗\operatorname{\mathrm{d}iag}^{\ast} is a bounded linear operator with ‖diag∗‖ℒ=1,\|\operatorname{\mathrm{d}iag}^{\ast}\!\|\_{\mathcal{L}}=1,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖𝜶^d−𝜶~d‖𝒮≤‖𝒟^d−𝒟d‖𝒮​‖𝒞^d†​∐c^1,dc^K,d‖ℒ+‖𝒟d‖𝒮​‖𝒞^d†​∐c^1,dc^K,d−𝒞d†​∐c1,dcK,d‖ℒ+‖ℛdK‖𝒮​‖𝒞d†​∐c1,dcK,d‖ℒ+‖𝜶d,K​(𝒞d‡​∐c1,dcK,d−𝕀)‖𝒮+‖𝜶~d−𝜶~dK‖𝒮.\displaystyle\begin{split}\big\|\hat{\boldsymbol{\alpha}}\_{\mathrm{d}}-\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}}\big\|\_{\mathcal{S}}&\leq\|\hat{\mathscr{D}}\_{\mathrm{d}}-\mathscr{D}\_{\mathrm{d}}\|\_{\mathcal{S}}\,\bigg\|\hat{\mathscr{C}}^{\dagger}\_{\mathrm{d}}\!\coprod^{\hat{c}\_{K,\mathrm{d}}}\_{\hat{c}\_{1,\mathrm{d}}}\bigg\|\_{\mathcal{L}}+\,\|\mathscr{D}\_{\mathrm{d}}\|\_{\mathcal{S}}\,\bigg\|\hat{\mathscr{C}}^{\dagger}\_{\mathrm{d}}\!\coprod^{\hat{c}\_{K,\mathrm{d}}}\_{\hat{c}\_{1,\mathrm{d}}}\,-\;\mathscr{C}^{\dagger}\_{\mathrm{d}}\!\coprod^{c\_{K,\mathrm{d}}}\_{c\_{1,\mathrm{d}}}\bigg\|\_{\mathcal{L}}\\ &\phantom{\leq~}+\big\|\mathscr{R}^{K}\_{\mathrm{d}}\big\|\_{\mathcal{S}}\,\bigg\|\mathscr{C}^{\dagger}\_{\mathrm{d}}\!\coprod^{c\_{K,\mathrm{d}}}\_{c\_{1,\mathrm{d}}}\bigg\|\_{\mathcal{L}}+\,\bigg\|\,\boldsymbol{\alpha}\_{\mathrm{d},K}\bigg(\mathscr{C}^{\ddagger}\_{\mathrm{d}}\!\coprod^{c\_{K,\mathrm{d}}}\_{c\_{1,\mathrm{d}}}-\;\mathbb{I}\bigg)\bigg\|\_{\mathcal{S}}+\,\big\|\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}}-\tilde{\boldsymbol{\alpha}}^{K}\_{\mathrm{d}}\big\|\_{\mathcal{S}}\,.\end{split} | |  | (C.12) |

In the following, we analyze each quantity in ([C.12](#A3.E12 "In Proof of Theorem 4.2. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")), where several arguments are inspired by proofs in Kühnert et al. ([2026](#bib.bib27)). First, from the definition of the operator norm, our pseudoinverses and our projection operators, it follows for any K,N:K,N:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝒞^d†​∐c^1,dc^K,d‖ℒ=(λ^K,d+ϑN)−1,‖𝒞d†​∐c1,dcK,d‖ℒ=(λK,d+ϑN)−1.\displaystyle\bigg\|\hat{\mathscr{C}}^{\dagger}\_{\mathrm{d}}\!\coprod^{\hat{c}\_{K,\mathrm{d}}}\_{\hat{c}\_{1,\mathrm{d}}}\bigg\|\_{\mathcal{L}}=(\hat{\lambda}\_{K,\mathrm{d}}+\vartheta\_{\!N})^{-1},\qquad\bigg\|\mathscr{C}^{\dagger}\_{\mathrm{d}}\!\coprod^{c\_{K,\mathrm{d}}}\_{c\_{1,\mathrm{d}}}\bigg\|\_{\mathcal{L}}=(\lambda\_{K,\mathrm{d}}+\vartheta\_{\!N})^{-1}\,. |  | (C.13) |

By the definition of 𝒟d,\mathscr{D}\_{\mathrm{d}}, due to elementary conversions, and ‖diag‖ℒ=1,\|\operatorname{\mathrm{d}iag}\|\_{\mathcal{L}}=1, it holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝒟d‖𝒮≤‖𝒟d‖𝒩≤‖𝒟‖𝒩≤‖𝒞𝜺†​∐e1eK‖ℒ​𝔼⁡‖X0⊗2,[p]‖​‖X1⊗2‖=O​(aK−2).\displaystyle\|\mathscr{D}\_{\mathrm{d}}\|\_{\mathcal{S}}\;\leq\;\|\mathscr{D}\_{\mathrm{d}}\|\_{\mathcal{N}}\;\leq\;\|\mathscr{D}\|\_{\mathcal{N}}\;\leq\;\bigg\|\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod\_{e\_{1}}^{e\_{K}}\bigg\|\_{\mathcal{L}}\operatorname{\mathds{E}}\!\big\|X^{\otimes 2,[p]}\_{0}\big\|\big\|X^{\otimes 2}\_{1}\big\|\;=\;\mathrm{O}(a^{-2}\_{K})\,. |  | (C.14) |

Furthermore, with KbK\_{b} in the definition of ΛK,d=(λK,d−λKb,d)−1\Lambda\_{K,\mathrm{d}}=(\lambda\_{K,\mathrm{d}}-\lambda\_{K\_{b},\mathrm{d}})^{-1} in ([4.17](#S4.E17 "In 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")), we get

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖𝒞^d†​∐c^1,dc^K,d−𝒞d†​∐c1,dcK,d‖ℒ\displaystyle\bigg\|\hat{\mathscr{C}}^{\dagger}\_{\mathrm{d}}\!\coprod^{\hat{c}\_{K,\mathrm{d}}}\_{\hat{c}\_{1,\mathrm{d}}}\,-\;\mathscr{C}^{\dagger}\_{\mathrm{d}}\!\coprod^{c\_{K,\mathrm{d}}}\_{c\_{1,\mathrm{d}}}\bigg\|\_{\mathcal{L}} | ≤‖𝒞^d†​∐c^1,dc^Kb−1,d−𝒞d†​∐c1,dcKb−1,d‖ℒ+‖𝒞^d†​∐c^K+1,dc^Kb−1,d−𝒞d†​∐cK+1,dcKb−1,d‖ℒ.\displaystyle\leq\,\bigg\|\hat{\mathscr{C}}^{\dagger}\_{\mathrm{d}}\!\!\coprod^{\hat{c}\_{K\_{b}-1,\mathrm{d}}}\_{\hat{c}\_{1,\mathrm{d}}}-\;\mathscr{C}^{\dagger}\_{\mathrm{d}}\!\!\coprod^{c\_{K\_{b}-1,\mathrm{d}}}\_{c\_{1,\mathrm{d}}}\bigg\|\_{\mathcal{L}}+\,\bigg\|\hat{\mathscr{C}}^{\dagger}\_{\mathrm{d}}\!\!\coprod^{\hat{c}\_{K\_{b}-1,\mathrm{d}}}\_{\hat{c}\_{K+1,\mathrm{d}}}-\;\mathscr{C}^{\dagger}\_{\mathrm{d}}\!\!\coprod^{c\_{K\_{b}-1,\mathrm{d}}}\_{c\_{K+1,\mathrm{d}}}\bigg\|\_{\mathcal{L}}\,. |  | (C.15) |

Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝒞^d†​∐c^1,dc^Kb−1,d−𝒞d†​∐c1,dcKb−1,d‖ℒ≤‖∑i=1Kb−1(λ^i,d+ϑN)−1​[(c^i,d⊗c^i,d)−(ci,d⊗ci,d)]‖ℒ+‖∑i=1Kb−1[(λ^i,d+ϑN)−1−(λi,d+ϑN)−1]​(ci,d⊗ci,d)‖ℒ.\displaystyle\begin{split}\bigg\|\,\hat{\mathscr{C}}^{\dagger}\_{\mathrm{d}}\!\!\coprod^{\hat{c}\_{K\_{b}-1,\mathrm{d}}}\_{\hat{c}\_{1,\mathrm{d}}}-\;\mathscr{C}^{\dagger}\_{\mathrm{d}}\!\!\coprod^{c\_{K\_{b}-1,\mathrm{d}}}\_{c\_{1,\mathrm{d}}}\bigg\|\_{\mathcal{L}}&\leq\,\bigg\|\sum^{K\_{b}-1}\_{i=1}\,(\hat{\lambda}\_{i,\mathrm{d}}+\vartheta\_{\!N})^{-1}\Big[(\hat{c}\_{i,\mathrm{d}}\otimes\hat{c}\_{i,\mathrm{d}})-(c\_{i,\mathrm{d}}\otimes c\_{i,\mathrm{d}})\Big]\bigg\|\_{\mathcal{L}}\\ &\qquad\;\,+\,\bigg\|\sum^{K\_{b}-1}\_{i=1}\,\Big[(\hat{\lambda}\_{i,\mathrm{d}}+\vartheta\_{\!N})^{-1}-(\lambda\_{i,\mathrm{d}}+\vartheta\_{\!N})^{-1}\Big](c\_{i,\mathrm{d}}\otimes c\_{i,\mathrm{d}})\bigg\|\_{\mathcal{L}}.\end{split} | |  |

Further, by Reimherr ([2015](#bib.bib36), Lemmas 3.1–3.2), ∥⋅∥ℒ≤∥⋅∥𝒮,\|\cdot\|\_{\mathcal{L}}\leq\|\cdot\|\_{\mathcal{S}}, (∑kak)1/2≤∑kak1/2(\sum\_{k}a\_{k})^{1/2}\leq\sum\_{k}a\_{k}^{1/2} for non-negative aka\_{k}, ΛK,d=ΛKb−1,d,\Lambda\_{K,\mathrm{d}}=\Lambda\_{K\_{b}-1,\mathrm{d}}, Kb≤K+ξK\_{b}\leq K+\xi by Assumption [4.2](#S4.Thmassumption2 "Assumption 4.2. ‣ 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model") (a), and basic conversions, with the empirical reciprocal eigengaps Λ^K,d=(λ^K,d−λ^K+1,d)−1\hat{\Lambda}\_{K,\mathrm{d}}=(\hat{\lambda}\_{K,\mathrm{d}}-\hat{\lambda}\_{K+1,\mathrm{d}})^{-1} in ([4.19](#S4.E19 "In 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")), it holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝒞^d†​∐c^1,dc^Kb−1,d−𝒞d†​∐c1,dcKb−1,d‖ℒ\displaystyle\bigg\|\,\hat{\mathscr{C}}^{\dagger}\_{\mathrm{d}}\!\!\coprod^{\hat{c}\_{K\_{b}-1,\mathrm{d}}}\_{\hat{c}\_{1,\mathrm{d}}}-\;\mathscr{C}^{\dagger}\_{\mathrm{d}}\!\!\coprod^{c\_{K\_{b}-1,\mathrm{d}}}\_{c\_{1,\mathrm{d}}}\bigg\|\_{\mathcal{L}} | ≤2​(λ^Kb−1,d+ϑN)−1​Kb1/2​‖𝒞^d−𝒞d‖ℒ\displaystyle\leq 2(\hat{\lambda}\_{K\_{b}-1,\mathrm{d}}+\vartheta\_{\!N})^{-1}K^{1/2}\_{b}\,\|\hat{\mathscr{C}}\_{\mathrm{d}}-\mathscr{C}\_{\mathrm{d}}\|\_{\mathcal{L}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×(Λ^Kb−1,d+ΛKb−1,d+(λKb−1,d+ϑN)−1+1)\displaystyle\qquad\;\,\times\Big(\hat{\Lambda}\_{K\_{b}-1,\mathrm{d}}+\Lambda\_{K\_{b}-1,\mathrm{d}}+(\lambda\_{K\_{b}-1,\mathrm{d}}+\vartheta\_{\!N})^{-1}+1\Big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤2​Λ^Kb−1,d​(K+ξ)1/2​‖𝒞^d−𝒞d‖ℒ​(Λ^Kb−1,d+2​ΛK,d+1).\displaystyle\leq 2\hat{\Lambda}\_{K\_{b}-1,\mathrm{d}}\,(K+\xi)^{1/2}\,\|\hat{\mathscr{C}}\_{\mathrm{d}}-\mathscr{C}\_{\mathrm{d}}\|\_{\mathcal{L}}\,\big(\hat{\Lambda}\_{K\_{b}-1,\mathrm{d}}+2\Lambda\_{K,\mathrm{d}}+1\big). |  | (C.16) |

Moreover, analogous arguments and Kb−K≤ξK\_{b}-K\leq\xi yield

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖𝒞^d†​∐c^K+1,dc^Kb−1,d−𝒞d†​∐cK+1,dcKb−1,d‖ℒ\displaystyle\bigg\|\,\hat{\mathscr{C}}^{\dagger}\_{\mathrm{d}}\!\!\coprod^{\hat{c}\_{K\_{b}-1,\mathrm{d}}}\_{\hat{c}\_{K+1,\mathrm{d}}}-\;\mathscr{C}^{\dagger}\_{\mathrm{d}}\!\!\coprod^{c\_{K\_{b}-1,\mathrm{d}}}\_{c\_{K+1,\mathrm{d}}}\bigg\|\_{\mathcal{L}} | ≤2​Λ^Kb−1,d​ξ1/2​‖𝒞^d−𝒞d‖ℒ​(Λ^Kb−1,d+2​ΛK,d+1).\displaystyle\leq 2\hat{\Lambda}\_{K\_{b}-1,\mathrm{d}}\,\xi^{1/2}\,\|\hat{\mathscr{C}}\_{\mathrm{d}}-\mathscr{C}\_{\mathrm{d}}\|\_{\mathcal{L}}\big(\hat{\Lambda}\_{K\_{b}-1,\mathrm{d}}+2\Lambda\_{K,\mathrm{d}}+1\big). |  | (C.17) |

Notice that Λ^Kb−1,d\hat{\Lambda}\_{K\_{b}-1,\mathrm{d}} is well-defined due to Kb−1≤K+ξK\_{b}-1\leq K+\xi and Assumption [4.2](#S4.Thmassumption2 "Assumption 4.2. ‣ 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model") (b).

The remainder ℛdK\mathscr{R}^{K}\_{\mathrm{d}} is identical to ℛd\mathscr{R}\_{\mathrm{d}} in the proof of Theorem [4.1](#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model"), where we deduced

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ℛdK‖𝒮≤ϑN​aK−1​‖diag‖ℒ2​‖𝜶K‖𝒮​𝔼⁡‖X~0⊗2,[p]‖𝒮2=O​(ϑN​aK−1).\displaystyle\big\|\mathscr{R}^{K}\_{\mathrm{d}}\big\|\_{\mathcal{S}}\leq\vartheta\_{\!N}a^{-1}\_{\!K}\|\!\operatorname{\mathrm{d}iag}\!\|^{2}\_{\mathcal{L}}\,\|\boldsymbol{\alpha}\_{K}\|\_{\mathcal{S}}\operatorname{\mathds{E}}\!\big\|\tilde{X}^{\otimes 2,[p]}\_{0}\big\|^{2}\_{\mathcal{S}}=\mathrm{O}\big(\vartheta\_{\!N}a^{-1}\_{\!K}\big)\,. |  | (C.18) |

Similar arguments as in the proof of Theorem [4.1](#S4.Thmtheorem1 "Theorem 4.1. ‣ 4.1 Finite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model") and the definition of 𝜶d,K\boldsymbol{\alpha}\_{\mathrm{d},K} yield

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝜶d,K​(𝒞d‡​∐c1,dcK,d−𝕀)‖𝒮\displaystyle\bigg\|\boldsymbol{\alpha}\_{\mathrm{d},K}\bigg(\mathscr{C}^{\ddagger}\_{\mathrm{d}}\!\coprod^{c\_{K,\mathrm{d}}}\_{c\_{1,\mathrm{d}}}-\;\mathbb{I}\bigg)\Big\|\_{\mathcal{S}} | =(∑m=1K(λm,d​(λm,d+ϑN)−1−1)2​‖𝜶d,K​(cm,d)‖2)1/2\displaystyle=\bigg(\sum^{K}\_{m=1}\big(\lambda\_{m,\mathrm{d}}(\lambda\_{m,\mathrm{d}}+\vartheta\_{\!N})^{-1}-1\big)^{2}\,\big\|\boldsymbol{\alpha}\_{\mathrm{d},K}(c\_{m,\mathrm{d}})\big\|^{2}\bigg)^{\!1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ϑN​λK,d−1​(∑m=1K‖𝜶d,K​(cm,d)‖2)1/2\displaystyle\leq\vartheta\_{\!N}\lambda^{-1}\_{K,\mathrm{d}}\bigg(\sum^{K}\_{m=1}\,\big\|\boldsymbol{\alpha}\_{\mathrm{d},K}(c\_{m,\mathrm{d}})\big\|^{2}\bigg)^{\!1/2} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤ϑN​λK,d−1​‖𝜶d,K‖𝒮=O​(ϑN​λK,d−1).\displaystyle\leq\vartheta\_{\!N}\lambda^{-1}\_{K,\mathrm{d}}\,\big\|\boldsymbol{\alpha}\_{\mathrm{d},K}\big\|\_{\mathcal{S}}=\mathrm{O}\big(\vartheta\_{\!N}\lambda^{-1}\_{K,\mathrm{d}}\big)\,. |  | (C.19) |

Furthermore, due to the definition of the H-S norm and Assumption [4.3](#S4.Thmassumption3 "Assumption 4.3. ‣ 4.2 Infinite-dimensional setting ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model"), it holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝜶~d−𝜶~dK‖𝒮2=∑i=1p∑ℓ>Kai​ℓ​ℓ2≤K−2​γ​∑i=1p∑ℓ>Kai​ℓ​ℓ2​(1+ℓ2​γ)=O​(K−2​γ).\displaystyle\big\|\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}}-\tilde{\boldsymbol{\alpha}}^{K}\_{\mathrm{d}}\big\|^{2}\_{\mathcal{S}}\;=\;\sum^{p}\_{i=1}\sum\_{\ell>K}\,a^{2}\_{i\ell\ell}\;\leq\;K^{-2\gamma}\sum^{p}\_{i=1}\sum\_{\ell>K}\,a^{2}\_{i\ell\ell}(1+\ell^{2\gamma})\;=\;\mathrm{O}(K^{-2\gamma})\,. |  | (C.20) |

Overall, by combining ([C.13](#A3.E13 "In Proof of Theorem 4.2. ‣ Appendix C Proofs ‣ An operator-level ARCH Model"))–([C.20](#A3.E20 "In Proof of Theorem 4.2. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")) with ([C.12](#A3.E12 "In Proof of Theorem 4.2. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")), and using that (λK,d+ϑN)−1≤ΛK,d(\lambda\_{K,\mathrm{d}}+\vartheta\_{\!N})^{-1}\leq\Lambda\_{K,\mathrm{d}} and (λ^K,d+ϑN)−1≤Λ^K,d=Oℙ​(ΛK,d),(\hat{\lambda}\_{K,\mathrm{d}}+\vartheta\_{\!N})^{-1}\leq\hat{\Lambda}\_{K,\mathrm{d}}=\mathrm{O}\_{\operatorname{\mathds{P}}}(\Lambda\_{K,\mathrm{d}}), together with Lemma [C.2](#A3.Thmlemma2 "Lemma C.2. ‣ Appendix C Proofs ‣ An operator-level ARCH Model"), it holds

|  |  |  |
| --- | --- | --- |
|  | ‖𝜶^d−𝜶~d‖𝒮≤Oℙ​(K1/2​aK−2​ΛK,d2​N−1/2)+O​(ϑN​aK−1)+O​(ϑN​λK,d−1)+O​(K−γ).\displaystyle\big\|\hat{\boldsymbol{\alpha}}\_{\mathrm{d}}-\tilde{\boldsymbol{\alpha}}\_{\mathrm{d}}\big\|\_{\mathcal{S}}\leq\mathrm{O}\_{\operatorname{\mathds{P}}}\big(K^{1/2}a^{-2}\_{K}\Lambda^{2}\_{K,\mathrm{d}}N^{-1/2}\big)+\mathrm{O}\big(\vartheta\_{\!N}a^{-1}\_{\!K}\big)+\mathrm{O}\big(\vartheta\_{\!N}\lambda^{-1}\_{K,\mathrm{d}}\big)+\mathrm{O}(K^{-\gamma})\,. |  |

Thus, as Kγ+1/2​aK−2​ΛK,d2=O​(N1/2)K^{\gamma+1/2}a^{-2}\_{K}\Lambda^{2}\_{K,\mathrm{d}}=\mathrm{O}(N^{1/2}) and ϑN=O​(min⁡(aK,λK,d)​K−γ),\vartheta\_{\!N}=\mathrm{O}(\min(a\_{K},\lambda\_{K,\mathrm{d}})K^{-\gamma}), the claim is proved.
∎

###### Proof of Proposition [4.1](#S4.Thmproposition1 "Proposition 4.1. ‣ 4.3 Estimation of the Intercept term ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model").

First, let ΔK≔∑i=1Kdi​(ei⊗ei)\Delta\_{K}\coloneqq\sum\_{i=1}^{K}d\_{i}(e\_{i}\otimes e\_{i}) with KK as in the definition of the estimator Δ^\hat{\Delta} in Eq. ([4.22](#S4.E22 "In 4.3 Estimation of the Intercept term ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")). Then,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖Δ^−Δ‖𝒮\displaystyle\|\hat{\Delta}-\Delta\|\_{\mathcal{S}} | ≤‖Δ^−ΔK​𝒞𝜺‡​∐e1eK‖𝒮+‖ΔK​(𝒞𝜺‡​∐e1eK−𝕀)‖𝒮+‖Δ−ΔK‖𝒮.\displaystyle\leq\bigg\|\hat{\Delta}-\Delta\_{K}\mathscr{C}^{\ddagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}}\bigg\|\_{\mathcal{S}}+\bigg\|\Delta\_{K}\bigg(\mathscr{C}^{\ddagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}}-\mathbb{I}\bigg)\bigg\|\_{\mathcal{S}}+\|\Delta-\Delta\_{K}\|\_{\mathcal{S}}\,. |  | (C.21) |

Moreover, with
𝒞𝜺†=(𝒞𝜺+ϑN​𝕀)−1\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}=(\mathscr{C}\_{\boldsymbol{\varepsilon}}+\vartheta\_{\!N}\mathbb{I})^{-1} and 𝒞𝜺‡≔𝒞𝜺​𝒞𝜺†\mathscr{C}^{\ddagger}\_{\!\boldsymbol{\varepsilon}}\coloneqq\mathscr{C}\_{\boldsymbol{\varepsilon}}\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}, we have

|  |  |  |
| --- | --- | --- |
|  | ‖𝒞𝜺†​∐e1eK‖ℒ=sup1≤j≤K(aj+ϑN)−1≤aK−1,‖𝒞𝜺‡​∐e1eK‖ℒ=sup1≤j≤Kaj​(aj+ϑN)−1≤1.\bigg\|\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}\coprod^{e\_{K}}\_{e\_{1}}\bigg\|\_{\mathcal{L}}=\sup\_{1\leq j\leq K}(a\_{j}+\vartheta\_{\!N})^{-1}\leq a^{-1}\_{K},\qquad\bigg\|\mathscr{C}^{\ddagger}\_{\!\boldsymbol{\varepsilon}}\coprod^{e\_{K}}\_{e\_{1}}\bigg\|\_{\mathcal{L}}=\sup\_{1\leq j\leq K}a\_{j}(a\_{j}+\vartheta\_{\!N})^{-1}\leq 1. |  |

For the first term in ([C.21](#A3.E21 "In Proof of Proposition 4.1. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")), using ([4.21](#S4.E21 "In 4.3 Estimation of the Intercept term ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")), the definition of Δ^\hat{\Delta} in ([4.22](#S4.E22 "In 4.3 Estimation of the Intercept term ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")), the triangle inequality, and the operator-valued Hölder inequality, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Δ^−Δ​𝒞𝜺‡​∐e1eK‖𝒮\displaystyle\bigg\|\hat{\Delta}-\Delta\mathscr{C}^{\ddagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}}\bigg\|\_{\mathcal{S}} | ≤‖𝒞^𝑿−𝒞𝑿‖𝒮​‖𝒞𝜺†​∐e1eK‖ℒ+‖𝜶^​(m^p)−𝜶​(mp)‖𝒮​‖𝒞𝜺‡​∐e1eK‖ℒ\displaystyle\leq\|\hat{\mathscr{C}}\_{\!\boldsymbol{X}}-\mathscr{C}\_{\!\boldsymbol{X}}\|\_{\mathcal{S}}\,\bigg\|\mathscr{C}^{\dagger}\_{\!\boldsymbol{\varepsilon}}\coprod^{e\_{K}}\_{e\_{1}}\bigg\|\_{\mathcal{L}}+\big\|\boldsymbol{\hat{\alpha}}(\hat{m}\_{p})-\boldsymbol{\alpha}(m\_{p})\big\|\_{\mathcal{S}}\,\bigg\|\mathscr{C}^{\ddagger}\_{\!\boldsymbol{\varepsilon}}\coprod^{e\_{K}}\_{e\_{1}}\bigg\|\_{\mathcal{L}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤aK−1​‖𝒞^𝑿−𝒞𝑿‖𝒮+‖𝜶^−𝜶‖𝒮​‖m^p‖𝒮+‖𝜶‖𝒮​‖m^p−mp‖𝒮\displaystyle\leq a^{-1}\_{K}\|\hat{\mathscr{C}}\_{\!\boldsymbol{X}}-\mathscr{C}\_{\!\boldsymbol{X}}\|\_{\mathcal{S}}+\|\boldsymbol{\hat{\alpha}}-\boldsymbol{\alpha}\|\_{\mathcal{S}}\|\hat{m}\_{p}\|\_{\mathcal{S}}+\|\boldsymbol{\alpha}\|\_{\mathcal{S}}\|\hat{m}\_{p}-m\_{p}\|\_{\mathcal{S}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Oℙ​(aK−1​N−1/2)+Oℙ​(‖𝜶^−𝜶‖𝒮).\displaystyle=\mathrm{O}\_{\operatorname{\mathds{P}}}\big(a^{-1}\_{K}N^{-1/2}\big)+\mathrm{O}\_{\operatorname{\mathds{P}}}\big(\|\boldsymbol{\hat{\alpha}}-\boldsymbol{\alpha}\|\_{\mathcal{S}}\big). |  | (C.22) |

For the second term in ([C.21](#A3.E21 "In Proof of Proposition 4.1. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")), noting that (ei)(e\_{i}) is a complete orthonormal system, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ΔK​(𝒞𝜺‡​∐e1eK−𝕀)‖𝒮2\displaystyle\bigg\|\Delta\_{K}\bigg(\mathscr{C}^{\ddagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}}-\mathbb{I}\bigg)\bigg\|^{2}\_{\mathcal{S}} | =∑j=1∞‖∑i=1Kdi​(ei⊗ei)​(𝒞𝜺‡​∐e1eK−𝕀)​(ej)‖2\displaystyle=\sum^{\infty}\_{j=1}\bigg\|\sum^{K}\_{i=1}d\_{i}(e\_{i}\otimes e\_{i})\bigg(\mathscr{C}^{\ddagger}\_{\!\boldsymbol{\varepsilon}}\!\coprod^{e\_{K}}\_{e\_{1}}-\mathbb{I}\bigg)(e\_{j})\bigg\|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j=1K(aj​(aj+ϑN)−1−1)2​‖∑i=1Kdi​(ei⊗ei)​(ej)‖2\displaystyle=\sum^{K}\_{j=1}\Big(a\_{j}(a\_{j}+\vartheta\_{\!N})^{-1}-1\Big)^{\!2}\bigg\|\sum^{K}\_{i=1}d\_{i}(e\_{i}\otimes e\_{i})(e\_{j})\bigg\|^{2}\allowdisplaybreaks |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ϑN2​aK−2​∑j=1K‖∑i=1Kdi​(ei⊗ei)​(ej)‖2\displaystyle\leq\vartheta^{2}\_{\!N}a^{-2}\_{\!K}\sum^{K}\_{j=1}\bigg\|\sum^{K}\_{i=1}d\_{i}(e\_{i}\otimes e\_{i})(e\_{j})\bigg\|^{2}\allowdisplaybreaks |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =ϑN2​aK−2​‖ΔK‖𝒮2.\displaystyle=\vartheta^{2}\_{\!N}a^{-2}\_{\!K}\|\Delta\_{K}\|^{2}\_{\mathcal{S}}. |  | (C.23) |

For the last term in ([C.21](#A3.E21 "In Proof of Proposition 4.1. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")), condition ([4.24](#S4.E24 "In Proposition 4.1. ‣ 4.3 Estimation of the Intercept term ‣ 4 Estimation in the CCC-op-ARCH model ‣ An operator-level ARCH Model")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Δ−ΔK‖𝒮2=∑i>Kdi2≤K−2​δ​∑i>Kdi2​(1+i2​δ)=O​(K−2​δ).\displaystyle\|\Delta-\Delta\_{K}\|^{2}\_{\mathcal{S}}\;=\;\sum\_{i>K}d^{2}\_{i}\;\leq\;K^{-2\delta}\sum\_{i>K}d^{2}\_{i}(1+i^{2\delta})\;=\;\mathrm{O}(K^{-2\delta}). |  | (C.24) |

Finally, substituting ([C.22](#A3.E22 "In Proof of Proposition 4.1. ‣ Appendix C Proofs ‣ An operator-level ARCH Model"))–([C.24](#A3.E24 "In Proof of Proposition 4.1. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")) into ([C.21](#A3.E21 "In Proof of Proposition 4.1. ‣ Appendix C Proofs ‣ An operator-level ARCH Model")), and using ϑN=O​(aK​K−δ),\vartheta\_{\!N}=\mathrm{O}(a\_{K}K^{-\delta}), where K=KN→∞,K=K\_{\!N}\to\infty, together with supK‖ΔK‖𝒮≤‖Δ‖𝒮<∞\sup\_{K}\|\Delta\_{K}\|\_{\mathcal{S}}\leq\|\Delta\|\_{\mathcal{S}}<\infty, the claim follows.
∎

BETA