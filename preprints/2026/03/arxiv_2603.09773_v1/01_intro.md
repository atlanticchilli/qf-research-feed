---
authors:
- Mihriban Ceylan
- David J. Prömel
doc_id: arxiv:2603.09773v1
family_id: arxiv:2603.09773
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Global universality via discrete-time signatures
url_abs: http://arxiv.org/abs/2603.09773v1
url_html: https://arxiv.org/html/2603.09773v1
venue: arXiv q-fin
version: 1
year: 2026
---


Mihriban Ceylan
Mihriban Ceylan, University of Mannheim, Germany
[mihriban.ceylan@uni-mannheim.de](2603.09773v1/mailto:mihriban.ceylan@uni-mannheim.de)
 and 
David J. Prömel
David J. Prömel, University of Mannheim, Germany
[proemel@uni-mannheim.de](2603.09773v1/mailto:proemel@uni-mannheim.de)

###### Abstract.

We establish global universal approximation theorems on spaces of piecewise linear paths, stating that linear functionals of the corresponding signatures are dense with respect to LpL^{p}- and weighted norms, under an integrability condition on the underlying weight function. As an application, we show that piecewise linear interpolations of Brownian motion satisfies this integrability condition. Consequently, we obtain LpL^{p}-approximation results for path-dependent functionals, random ordinary differential equations, and stochastic differential equations driven by Brownian motion.

Key words: Brownian motion; non-anticipative functional; piecewise linear interpolation; signatures; stochastic differential equation; universal approximation theorem; weighted space.

MSC 2010 Classification: Primary: 60L10; Secondary: 60H10; 60J65; 91G99.

## 1. Introduction

Approximating functionals that depend in a complex way on the entire trajectory of a data stream is a fundamental challenge across a wide range of disciplines, including machine learning, quantitative finance, and the analysis of random dynamical systems. Many quantities arising in applications, such as optimal control strategies, option prices, and predictors learned from streamed data, depend on the full history of a signal. Developing tractable and expressive representations for such path-dependent objects is therefore of central importance, both from practical and theoretical perspectives.

Over the past decade, the signature of a path has emerged as a powerful and flexible framework for addressing such problems. Originally introduced by K.-T. Chen [[Che54](#bib.bibx11)] and later developed extensively within the rough path theory initiated by Lyons [[Lyo07](#bib.bibx34)], the signature provides a systematic representation of a path in terms of its iterated integrals. Roughly speaking, the signature of a path is defined as the infinite collection of all its iterated integrals. This collection of features captures interactions between the components of the path across time and uniquely characterizes the path up to tree-like equivalence; see [[HL10](#bib.bibx27), [BGLY16](#bib.bibx5)]. Owing to its rich algebraic structure, the signature possesses a fundamental universality property: linear combinations of signature coordinates are dense in spaces of continuous path functionals on compact subsets of path space; see, for example, [[LLN13](#bib.bibx32), [KBPA+19](#bib.bibx29), [LNPA19](#bib.bibx33)]. In this sense, signatures play a role analogous to classical polynomials: they form a universal feature class for continuous path-dependent functionals. Thanks to this universality and their favorable algebraic properties, signature-based methods have found numerous applications. They are widely used in machine learning for the analysis of sequential data, such as image and texture classification, the generation of synthetic data and topological data analysis, and in mathematical finance for tasks such as derivative pricing, model calibration, and stochastic control; see, for instance, [[Gra13](#bib.bibx26), [KBPA+19](#bib.bibx29), [LNPA19](#bib.bibx33), [CNO20](#bib.bibx13), [ML25](#bib.bibx35), [BBH+25](#bib.bibx3), [BdRHO25](#bib.bibx4)].

Despite these strong theoretical guarantees, two fundamental challenges arise when applying signature-based methods in practice.

First, in most relevant settings the signature cannot be computed exactly. Even for classical stochastic processes such as Brownian motion, iterated integrals cannot be evaluated pathwise in closed form. Consequently, practical implementations must rely on suitable approximations. A natural and structurally consistent approach is to start from discrete-time observations of the underlying signal. In practice, one typically has access only to a finite collection of observations rather than to the full continuous trajectory. To reconstruct a continuous object from such data, a common approach is to employ piecewise linear interpolation. This yields a continuous path that preserves the temporal ordering and increment structure of the observed signal while remaining computationally tractable.
In particular, dedicated implementations such as the `iisignature` library demonstrate that signatures and log-signatures of discretely sampled paths can be computed at relatively high truncation levels and in moderate dimensions with practical runtimes [[RG18](#bib.bibx36)].

This intrinsic discreteness has led to increasing interest in discrete-time formulations of signatures. In reservoir computing, discrete-time signature-based systems have been used to explain universality phenomena in recurrent neural networks [[CGG+21](#bib.bibx10)]. In mathematical finance, discrete-time variants of the signature have been employed to extract features directly from time series, to price exotic derivatives, and in stochastic control applications [[AN21](#bib.bibx1), [LNPA19](#bib.bibx33), [BBH+25](#bib.bibx3)]. More broadly, truncated signatures of discretely sampled paths yield finite-dimensional representations of sequential data and have been successfully used as feature maps in a variety of contexts [[Fer21](#bib.bibx21)].

Second, classical universal approximation theorems for signatures are typically formulated for continuous functionals on compact subsets of path space. While mathematically natural, this restriction can be limiting in many relevant settings. In probabilistic models, for example, sample paths of processes such as Brownian motion do not lie in any fixed compact subset with positive probability. The same phenomenon persists for discretely observed paths and their piecewise linear interpolations, whose trajectories are not naturally confined to compact sets.

These observations motivate the development of global approximation results for signatures of discretely observed paths. In particular, it is natural to study approximation in weighted function spaces and in LpL^{p}-spaces, which provide a flexible framework for controlling the growth of functionals outside compact sets. Establishing such global universal approximation results extends the classical compact-set theory and better reflects the requirements arising in probabilistic modeling, machine learning, and quantitative finance.

In this paper, we establish global universal approximation theorems for linear functionals of the signature on spaces of piecewise linear paths, as their arise from discrete-time observations or in numerical approximation. We first prove density results in weighted function spaces (Proposition [3.1](#S3.Thmtheorem1 "Proposition 3.1 (Universal approximation theorem on ℬ_𝜓⁢(𝒞̂^𝜋)). ‣ 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures") and Proposition [3.4](#S3.Thmtheorem4 "Proposition 3.4 (Universal approximation theorem on ℬ_𝜓(Λ_𝑇^𝜋)). ‣ 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures")) and, subsequently, derive LpL^{p}-type universal approximation theorems under a suitable integrability condition on the underlying weight function (Theorem [3.5](#S3.Thmtheorem5 "Theorem 3.5 (𝐿^𝑝-convergence). ‣ 3.2. Approximation of 𝐿^𝑝-functionals via signatures ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures")). The weighted framework is inspired by and adapted from recent developments in [[CST26](#bib.bibx17)]. In particular, our density results rely on the weighted Stone–Weierstraß theorem established therein, which we extend to the setting of piecewise linear paths. Our LpL^{p}-approximation results are then formulated directly on path spaces generated by discrete-time data.

To position our contribution within the existing literature, we emphasize that, in contrast to density results in weighted function spaces and LpL^{p}-type approximation results obtained in the continuous setting for geometric rough paths (see, e.g., [[SA23](#bib.bibx37), [BPS25](#bib.bibx7), [CM25](#bib.bibx12), [CP25](#bib.bibx15), [CFL+26](#bib.bibx9)]), our framework is intrinsically discrete and built on piecewise linear interpolations of discretely observed signals. In particular, our results are not an immediate consequence of the continuous-time framework developed in [[CP25](#bib.bibx15)], see Remark [3.6](#S3.Thmtheorem6 "Remark 3.6. ‣ 3.2. Approximation of 𝐿^𝑝-functionals via signatures ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures"), for a more detailed discussion.

The strength of the discrete global framework becomes particularly apparent in probabilistic applications. In particular, we verify the required integrability condition for piecewise linearly interpolated Brownian motion. This yields LpL^{p}-approximation results for continuous (non-anticipative) functionals of Brownian motion as well as for solutions to ordinary differential equations driven by Brownian paths. Moreover, recent continuous-time results such as [[CP25](#bib.bibx15)] show that solutions to stochastic differential equations driven by Brownian motion, as well as functionals on the Brownian rough path, can be approximated in LpL^{p} by linear functionals of the Brownian signature. In the present discrete-time setting, we show that these linear functionals acting on the Brownian signature can themselves be approximated by the same linear functionals evaluated on the signature of the piecewise linearly interpolated Brownian motion (Lemma [4.4](#S4.Thmtheorem4 "Lemma 4.4. ‣ 4.2.2. Approximation of SDEs ‣ 4.2. Approximation of random ordinary differential equations and stochastic differential equations ‣ 4. Universal approximation via discrete-time signatures of Brownian motion ‣ Global universality via discrete-time signatures")). As a consequence, functionals on the Brownian rough path, as well as solutions to stochastic differential equations driven by Brownian motion, can be approximated by linear functionals of the signatures of linearly interpolated Brownian paths.

Organization of the paper:
In Section [2](#S2 "2. Preliminaries ‣ Global universality via discrete-time signatures") we recall the essential concepts regarding signatures and rough path theory. In Section [3](#S3 "3. Global universal approximation ‣ Global universality via discrete-time signatures"), the universal approximation theorems on spaces of piecewise linear paths are established, stating that linear functionals of the corresponding signatures are dense with respect to LpL^{p}- and weighted norms, under an integrability condition on the underlying weight function. In Section [4](#S4 "4. Universal approximation via discrete-time signatures of Brownian motion ‣ Global universality via discrete-time signatures"), we show that piecewise linear interpolations of Brownian motion satisfies this integrability condition and derive LpL^{p}-approximation results for path-dependent functionals, random ODEs and SDEs driven by Brownian motion.

Acknowledgments: M. Ceylan gratefully acknowledges financial support by the doctoral scholarship programme from the Avicenna-Studienwerk, Germany, and D.J. Prömel his affiliation with the Department of Mathematics at King’s College London, United Kingdom.

## 2. Preliminaries

First we recall some essentials on signatures and rough path theory, where we refer to [[FV10](#bib.bibx25), [FH20](#bib.bibx22)] for a more detailed introduction.

### 2.1. Algebraic setting for signatures

For d∈ℕd\in\mathbb{N}, let ℝd\mathbb{R}^{d} be the standard dd-dimensional Euclidean space equipped with the norm |x|ℝd:=(∑i=1dxi2)1/2|x|\_{\mathbb{R}^{d}}:=(\sum\_{i=1}^{d}x\_{i}^{2})^{1/2} for x=(x1,…,xd)∈ℝdx=(x\_{1},\dots,x\_{d})\in\mathbb{R}^{d}. When the underlying space is clear from context, we simply write |x||x| instead of |x|ℝd|x|\_{\mathbb{R}^{d}}.

The n-fold tensor product of ℝd\mathbb{R}^{d} is given by

|  |  |  |
| --- | --- | --- |
|  | (ℝd)⊗0:=ℝand(ℝd)⊗n:=ℝd⊗⋯⊗ℝd⏟n,for ​n∈ℕ.(\mathbb{R}^{d})^{\otimes 0}:=\mathbb{R}\quad\text{and}\quad(\mathbb{R}^{d})^{\otimes n}:=\underbrace{\mathbb{R}^{d}\otimes\cdots\otimes\mathbb{R}^{d}}\_{n},\quad\text{for }n\in\mathbb{N}. |  |

Let (e1,…,ed)(e\_{1},\ldots,e\_{d}) be the canonical basis of ℝd\mathbb{R}^{d}. It is well-known that {ei1⊗⋯⊗ein:i1,…,in∈{1,…,d}}\{e\_{i\_{1}}\otimes\cdots\otimes e\_{i\_{n}}:i\_{1},\ldots,i\_{n}\in\{1,\ldots,d\}\} is a canonical basis for (ℝd)⊗n(\mathbb{R}^{d})^{\otimes n} and we denote by e∅e\_{\emptyset} the basis element of (ℝd)⊗0(\mathbb{R}^{d})^{\otimes 0}.
Then, every a(n)∈(ℝd)⊗na^{(n)}\in(\mathbb{R}^{d})^{\otimes n} admits the coordinate representation

|  |  |  |
| --- | --- | --- |
|  | a(n)=∑i1,…,in=1dai1,…,in​ei1⊗⋯⊗ein,a^{(n)}=\sum\_{i\_{1},\dots,i\_{n}=1}^{d}a\_{i\_{1},\dots,i\_{n}}\,e\_{i\_{1}}\otimes\cdots\otimes e\_{i\_{n}}, |  |

and we equip (ℝd)⊗n(\mathbb{R}^{d})^{\otimes n} with the usual Euclidean norm

|  |  |  |
| --- | --- | --- |
|  | |a(n)|(ℝd)⊗n:=(∑i1,…,in=1d|ai1,…,in|2)1/2,for ​a(n)∈(ℝd)⊗n.|a^{(n)}|\_{(\mathbb{R}^{d})^{\otimes n}}:=\bigg(\sum\_{i\_{1},\ldots,i\_{n}=1}^{d}|a\_{i\_{1},\ldots,i\_{n}}|^{2}\bigg)^{1/2},\quad\text{for }a^{(n)}\in(\mathbb{R}^{d})^{\otimes n}. |  |

When no confusion may arise, we write |a(n)||a^{(n)}| instead of |a(n)|(ℝd)⊗n|a^{(n)}|\_{(\mathbb{R}^{d})^{\otimes n}}.

For d∈ℕd\in\mathbb{N}, the extended tensor algebra on ℝd\mathbb{R}^{d} is defined as

|  |  |  |
| --- | --- | --- |
|  | T​((ℝd)):={𝐚:=(a(0),…,a(n),…):a(n)∈(ℝd)⊗n},T((\mathbb{R}^{d})):=\Bigl\{\mathbf{a}:=(a^{(0)},\ldots,a^{(n)},\ldots):a^{(n)}\in(\mathbb{R}^{d})^{\otimes n}\Bigr\}, |  |

and a(i)a^{(i)} is called tensor of level ii. We equip T​((ℝd))T((\mathbb{R}^{d})) with the standard addition “++”, tensor multiplication “⊗\otimes”, and scalar multiplication “⋅\cdot” defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐚+𝐛\displaystyle\mathbf{a}+\mathbf{b} | :=(a(0)+b(0),…,a(n)+b(n),…),\displaystyle:=\Bigl(a^{(0)}+b^{(0)},\ldots,a^{(n)}+b^{(n)},\ldots\Bigr), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐚⊗𝐛\displaystyle\mathbf{a}\otimes\mathbf{b} | :=(c(0),…,c(n),…),\displaystyle:=\Bigl(c^{(0)},\ldots,c^{(n)},\ldots\Bigr), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | λ⋅𝐚\displaystyle\lambda\cdot\mathbf{a} | :=(λ​a(0),…,λ​a(n),…),\displaystyle:=\Bigl(\lambda a^{(0)},\ldots,\lambda a^{(n)},\ldots\Bigr), |  |

for 𝐚=(a(n))n=0∞,𝐛=(b(n))n=0∞∈T​((ℝd))\mathbf{a}=(a^{(n)})\_{n=0}^{\infty},\mathbf{b}=(b^{(n)})\_{n=0}^{\infty}\in T((\mathbb{R}^{d})) and λ∈ℝ\lambda\in\mathbb{R}, where c(n):=∑k=0na(k)⊗b(n−k)c^{(n)}:=\sum\_{k=0}^{n}a^{(k)}\otimes b^{(n-k)}. Let us remark that (T​((ℝd)),+,⋅,⊗)(T((\mathbb{R}^{d})),+,\cdot,\otimes) is a real non-commutative algebra with neutral element 𝟏=(1,0,…,0,…)\mathbf{1}=(1,0,\ldots,0,\ldots). Similarly, we define the truncated tensor algebra of order N∈ℕN\in\mathbb{N} by

|  |  |  |
| --- | --- | --- |
|  | TN​(ℝd):={𝐚∈T​((ℝd)):a(n)=0,∀n>N},T^{N}(\mathbb{R}^{d}):=\Bigl\{\mathbf{a}\in T((\mathbb{R}^{d})):a^{(n)}=0,\forall n>N\Bigr\}, |  |

which we equip with the norm

|  |  |  |
| --- | --- | --- |
|  | ‖𝐚‖TN​(ℝd):=maxn=0,…,N⁡|a(n)|(ℝd)⊗n,for ​𝐚=(a(n))n=0N∈TN​(ℝd).\|\mathbf{a}\|\_{T^{N}(\mathbb{R}^{d})}:=\max\_{n=0,\ldots,N}|a^{(n)}|\_{(\mathbb{R}^{d})^{\otimes n}},\quad\text{for }\mathbf{a}=(a^{(n)})\_{n=0}^{N}\in T^{N}(\mathbb{R}^{d}). |  |

Note that TN​(ℝd)T^{N}(\mathbb{R}^{d}) has dimension ∑i=0Ndi=\sum\_{i=0}^{N}d^{i}= (dN+1−1)/(d−1)(d^{N+1}-1)/(d-1). Additionally, we define the tensor algebra T​(ℝd)=⋃n∈ℕTn​(ℝd)T(\mathbb{R}^{d})=\bigcup\_{n\in\mathbb{N}}T^{n}(\mathbb{R}^{d}) and consider the truncated tensor subalgebras T0N​(ℝd),T1N​(ℝd)⊂TN​(ℝd)T\_{0}^{N}(\mathbb{R}^{d}),T\_{1}^{N}(\mathbb{R}^{d})\subset T^{N}(\mathbb{R}^{d}) of elements 𝐚∈TN​(ℝd)\mathbf{a}\in T^{N}(\mathbb{R}^{d}) with a(0)=0,a(0)=1a^{(0)}=0,a^{(0)}=1, respectively. Observe that T1N​(ℝd)T\_{1}^{N}(\mathbb{R}^{d}) is a Lie group under ⊗\otimes, with unit element 𝟏=(1,0,…,0)\mathbf{1}=(1,0,\ldots,0).

The Lie algebra that is generated from {𝐞1,…,𝐞d}\{\mathbf{e}\_{1},\dots,\mathbf{e}\_{d}\}, where 𝐞i:=(0,ei,0,…)∈T​(ℝd)\mathbf{e}\_{i}:=(0,e\_{i},0,\dots)\in T(\mathbb{R}^{d}), and the commutator bracket

|  |  |  |
| --- | --- | --- |
|  | [𝐚,𝐛]=𝐚⊗𝐛−𝐛⊗𝐚,𝐚,𝐛∈T​(ℝd),[\mathbf{a},\mathbf{b}]=\mathbf{a}\otimes\mathbf{b}-\mathbf{b}\otimes\mathbf{a},\qquad\mathbf{a},\mathbf{b}\in T(\mathbb{R}^{d}), |  |

is called the free Lie algebra 𝔤​(ℝd)\mathfrak{g}(\mathbb{R}^{d}) over ℝd\mathbb{R}^{d}, see e.g. [[FV10](#bib.bibx25), Section 7.3]. It is a subalgebra of T0​((ℝd))T\_{0}((\mathbb{R}^{d})), where we define for c∈ℝc\in\mathbb{R}, the tensor subalgebra Tc​((ℝd)):={𝐚=(a(n))n=0∞∈T​((ℝd)):a(0)=c}T\_{c}((\mathbb{R}^{d})):=\{\mathbf{a}=(a^{(n)})\_{n=0}^{\infty}\in T((\mathbb{R}^{d})):a^{(0)}=c\}. The free Lie group G​((ℝd)):=exp⁡(𝔤​(ℝd))G((\mathbb{R}^{d})):=\exp(\mathfrak{g}(\mathbb{R}^{d})) is defined as the tensor exponential of 𝔤​(ℝd)\mathfrak{g}(\mathbb{R}^{d}), i.e., the image of 𝔤​(ℝd)\mathfrak{g}(\mathbb{R}^{d}) under the map

|  |  |  |
| --- | --- | --- |
|  | exp⊗:T0​((ℝd))→T​((ℝd)),𝐚↦1+∑k=1∞1k!​𝐚⊗k.\exp\_{\otimes}\colon T\_{0}((\mathbb{R}^{d}))\to T((\mathbb{R}^{d})),\qquad\mathbf{a}\mapsto 1+\sum\_{k=1}^{\infty}\frac{1}{k!}\mathbf{a}^{\otimes k}. |  |

G​((ℝd))G((\mathbb{R}^{d})) is a subgroup of T1​((ℝd))T\_{1}((\mathbb{R}^{d})). In fact, (G​((ℝd)),⊗)(G((\mathbb{R}^{d})),\otimes) is a group with unit element (1,0,…,0,…)(1,0,\dots,0,\dots), and for all 𝐠=exp⊗⁡(𝐚)∈G​((ℝd))\mathbf{g}=\exp\_{\otimes}(\mathbf{a})\in G((\mathbb{R}^{d})), the inverse with respect to ⊗\otimes is given by 𝐠−1=exp⊗⁡(−𝐚)\mathbf{g}^{-1}=\exp\_{\otimes}(-\mathbf{a}), for 𝐠=exp⊗⁡(𝐚)∈G​((ℝd))\mathbf{g}=\exp\_{\otimes}(\mathbf{a})\in G((\mathbb{R}^{d})). We call elements in G​((ℝd))G((\mathbb{R}^{d})) group-like elements. For N∈ℕN\in\mathbb{N}, we define the free step-NN nilpotent Lie algebra 𝔤N​(ℝd)⊂T0N​(ℝd)\mathbf{\mathfrak{g}}^{N}(\mathbb{R}^{d})\subset T\_{0}^{N}(\mathbb{R}^{d}) with

|  |  |  |
| --- | --- | --- |
|  | 𝔤N​(ℝd):={0}⊕ℝd⊕[ℝd,ℝd]⊕⋯⊕[ℝd,[…,[ℝd,ℝd]]]⏟(N−1)​ brackets,\mathbf{\mathfrak{g}}^{N}(\mathbb{R}^{d}):=\{0\}\oplus\mathbb{R}^{d}\oplus[\mathbb{R}^{d},\mathbb{R}^{d}]\oplus\cdots\oplus\underbrace{[\mathbb{R}^{d},[\ldots,[\mathbb{R}^{d},\mathbb{R}^{d}]]]}\_{(N-1)\text{ brackets}}, |  |

where (𝐠,𝐡)↦[𝐠,𝐡]:=𝐠⊗𝐡−𝐡⊗𝐠∈T0N​(ℝd)(\mathbf{g},\mathbf{h})\mapsto[\mathbf{g},\mathbf{h}]:=\mathbf{g}\otimes\mathbf{h}-\mathbf{h}\otimes\mathbf{g}\in T\_{0}^{N}(\mathbb{R}^{d}) denotes the Lie bracket for 𝐠,𝐡∈TN​(ℝd)\mathbf{g},\mathbf{h}\in T^{N}(\mathbb{R}^{d}), see [[FV10](#bib.bibx25), Chapter 7.3.2 and Definition 7.25]. The image GN​(ℝd):=exp⁡(𝔤N​(ℝd))G^{N}(\mathbb{R}^{d}):=\exp(\mathbf{\mathfrak{g}}^{N}(\mathbb{R}^{d})) is a (closed) sub-Lie group of (T1N​(ℝd),⊗)(T\_{1}^{N}(\mathbb{R}^{d}),\otimes), called the free nilpotent group of step NN over ℝd\mathbb{R}^{d}, see [[FV10](#bib.bibx25), Theorem 7.30].

We define I:=(i1,…,in)I:=(i\_{1},\ldots,i\_{n}) as a nn-dimensional multi-index of non-negative integers, i.e. ij∈{1,…,d}i\_{j}\in\{1,\ldots,d\} for every j∈{1,2,…,n}j\in\{1,2,\ldots,n\}. Note that |I|:=n|I|:=n and the empty index is given by I:=∅I:=\emptyset with |I|=0|I|=0. For n≥1n\geq 1 or n≥2n\geq 2, we write I′:=(i1,…,in−1)I^{\prime}:=(i\_{1},\ldots,i\_{n-1}) and I′′:=(i1,…,in−2)I^{\prime\prime}:=(i\_{1},\ldots,i\_{n-2}), respectively. Moreover, for each |I|≥1|I|\geq 1, we set eI:=ei1⊗⋯⊗eine\_{I}:=e\_{i\_{1}}\otimes\cdots\otimes e\_{i\_{n}}. This allows us to write 𝐚∈T​((ℝd))\mathbf{a}\in T((\mathbb{R}^{d})) (and 𝐚∈T​(ℝd)\mathbf{a}\in T(\mathbb{R}^{d})) as

|  |  |  |
| --- | --- | --- |
|  | 𝐚=∑|I|≥0⟨eI,𝐚⟩​eI,\mathbf{a}=\sum\_{|I|\geq 0}\langle e\_{I},\mathbf{a}\rangle e\_{I}, |  |

where ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle is defined as the inner product of (ℝd)⊗n(\mathbb{R}^{d})^{\otimes n} for each n≥0n\geq 0.

For two multi-indices I=(i1,…,i|I|)I=(i\_{1},\ldots,i\_{|I|}) and J=(j1,…,j|J|)J=(j\_{1},\ldots,j\_{|J|}) with entries in {1,…,d}\{1,\ldots,d\}, the shuffle product is recursively defined by

|  |  |  |
| --- | --- | --- |
|  | eI​eJ:=(eI′​eJ)⊗ei|I|+(eI​eJ′)⊗ej|J|,e\_{I}\shuffle e\_{J}:=(e\_{I^{\prime}}\shuffle e\_{J})\otimes e\_{i\_{|I|}}+(e\_{I}\shuffle e\_{J^{\prime}})\otimes e\_{j\_{|J|}}, |  |

with eI​e∅:=e∅​eI:=eIe\_{I}\shuffle e\_{\emptyset}:=e\_{\emptyset}\shuffle e\_{I}:=e\_{I}. For all 𝐚∈G​((ℝd))\mathbf{a}\in G((\mathbb{R}^{d})), the shuffle product property holds, i.e., for two multi-indices I=(i1,…,i|I|)I=(i\_{1},\ldots,i\_{|I|}) and J=(j1,…,j|J|)J=(j\_{1},\ldots,j\_{|J|}), it holds that

|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝐚⟩​⟨eJ,𝐚⟩=⟨eI​eJ,𝐚⟩.\langle e\_{I},\mathbf{a}\rangle\langle e\_{J},\mathbf{a}\rangle=\langle e\_{I}\shuffle e\_{J},\mathbf{a}\rangle. |  |

### 2.2. Essentials on rough path theory

The space of continuous linear maps ff from the normed space (X,∥⋅∥X)(X,\|\cdot\|\_{X}) to the normed space (Y,∥⋅∥Y)(Y,\|\cdot\|\_{Y}) is denoted by ℒ​(X;Y)\mathcal{L}(X;Y), which is equipped with the norm ‖f‖ℒ​(X;Y):=supx∈X,‖x‖X≤1‖f​(x)‖Y\|f\|\_{\mathcal{L}(X;Y)}:=\sup\_{x\in X,\|x\|\_{X}\leq 1}\|f(x)\|\_{Y}. Furthermore, if Y=ℝY=\mathbb{R}, the topological dual space of XX, denoted by X∗X^{\ast}, is identified with ℒ​(X;ℝ)\mathcal{L}(X;\mathbb{R}). Elements of X∗X^{\ast} are linear functionals ℓ:X→ℝ\ell\colon X\to\mathbb{R} and the norm on X∗X^{\ast} is defined by ‖ℓ‖X∗:=supx∈X,‖x‖X≤1|ℓ​(x)|\|\ell\|\_{X^{\ast}}:=\sup\_{x\in X,\|x\|\_{X}\leq 1}|\ell(x)|.

For a Hausdorff topological space (X,τX)(X,\tau\_{X}) and a normed space (E,∥⋅∥E)(E,\|\cdot\|\_{E}), the space of continuous functions f:X→Ef\colon X\to E is denoted by C​(X;E)C(X;E) and Cb​(X;E)⊆C​(X;E)C\_{b}(X;E)\subseteq C(X;E) denotes the vector subspace of bounded functions. Whenever E=ℝE=\mathbb{R}, we simplify the notation to C​(X):=C​(X;ℝ)C(X):=C(X;\mathbb{R}) and Cb​(X):=Cb​(X;ℝ)C\_{b}(X):=C\_{b}(X;\mathbb{R}), respectively. We write Cbk=Cbk​(ℝm;ℒ​(ℝd;ℝm))C\_{b}^{k}=C\_{b}^{k}(\mathbb{R}^{m};\mathcal{L}(\mathbb{R}^{d};\mathbb{R}^{m})) for the space of kk-times continuously differentiable functions f:ℝm→ℒ​(ℝd;ℝm)f\colon\mathbb{R}^{m}\to\mathcal{L}(\mathbb{R}^{d};\mathbb{R}^{m}) such that ff and all its derivatives up to order kk are continuous and bounded, and equip the space Cbk=Cbk​(ℝm;ℒ​(ℝd;ℝm))C\_{b}^{k}=C\_{b}^{k}(\mathbb{R}^{m};\mathcal{L}(\mathbb{R}^{d};\mathbb{R}^{m})) with the norm

|  |  |  |
| --- | --- | --- |
|  | ‖f‖Cbk:=‖f‖∞+‖D​f‖∞+…+‖Dk​f‖∞,\|f\|\_{C\_{b}^{k}}:=\|f\|\_{\infty}+\|Df\|\_{\infty}+\ldots+\|D^{k}f\|\_{\infty}, |  |

where Dr​fD^{r}f denotes the rr-th order derivative of ff and ∥⋅∥∞\|\cdot\|\_{\infty} denotes the supremum norm on the corresponding spaces of operators.

For a measure space (X,𝒜,μ)(X,\mathcal{A},\mu) and 1≤p<∞1\leq p<\infty, the (vector-valued) Lebesgue space Lp​(X,μ;ℝd)L^{p}(X,\mu;\mathbb{R}^{d}) is defined as the space of (equivalence classes of) 𝒜\mathcal{A}-measurable functions f:X→ℝdf\colon X\to\mathbb{R}^{d} such that

|  |  |  |
| --- | --- | --- |
|  | ‖f‖Lp​(X,μ;ℝd):=(∫X|f​(x)|p​dμ​(x))1p<∞.\|f\|\_{L^{p}(X,\mu;\mathbb{R}^{d})}:=\Bigl(\int\_{X}|f(x)|^{p}\,\,\mathrm{d}\mu(x)\Bigr)^{\frac{1}{p}}<\infty. |  |

For d=1d=1, we simply write Lp​(X):=Lp​(X,μ):=Lp​(X,μ;ℝ)L^{p}(X):=L^{p}(X,\mu):=L^{p}(X,\mu;\mathbb{R}) and ∥⋅∥Lp​(X):=∥⋅∥Lp​(X,μ;ℝ)\|\cdot\|\_{L^{p}(X)}:=\|\cdot\|\_{L^{p}(X,\mu;\mathbb{R})}.

Let T>0T>0 be a fixed finite time horizon, then we define the 11-variation of a path X:[0,T]→ℝdX\colon[0,T]\to\mathbb{R}^{d} by

|  |  |  |
| --- | --- | --- |
|  | ‖X‖1​-var:=sup𝒟⊂[0,T](∑ti∈𝒟|Xti−Xti−1|),\|X\|\_{1\textup{-var}}:=\sup\_{\mathcal{D}\subset[0,T]}\Bigl(\sum\_{t\_{i}\in\mathcal{D}}|X\_{t\_{i}}-X\_{t\_{i-1}}|\Bigr), |  |

where the supremum is taken over all partitions 𝒟={0=t0<t1<⋯<tn=T}\mathcal{D}=\{0=t\_{0}<t\_{1}<\cdots<t\_{n}=T\} of the interval [0,T][0,T] and ∑ti∈𝒟\sum\_{t\_{i}\in\mathcal{D}} denotes the summation over all points in 𝒟\mathcal{D}. Then, if ‖X‖1​-var<∞\|X\|\_{1\textup{-var}}<\infty, we say that XX is of bounded variation or of finite 11-variation on [0,T][0,T]. The space of continuous paths of bounded variation on [0,T][0,T] with values in ℝd\mathbb{R}^{d} is denoted by C1​-var​([0,T];ℝd)C^{1\textup{-var}}([0,T];\mathbb{R}^{d}).

Let π={ti}i=0n={0=t0<⋯<tn=T}\pi=\{t\_{i}\}\_{i=0}^{n}=\{0=t\_{0}<\cdots<t\_{n}=T\} be a partition of the interval [0,T][0,T]. Further, fix an initial value x0∈ℝdx\_{0}\in\mathbb{R}^{d}, and let X:π→ℝdX\colon\pi\to\mathbb{R}^{d} be such that X0=x0X\_{0}=x\_{0}. The continuous bounded variation path Xπ:[0,T]→ℝdX^{\pi}\colon[0,T]\to\mathbb{R}^{d} is given by {Xtk}k=0n\{X\_{t\_{k}}\}\_{k=0}^{n} and a linear interpolation in between:

|  |  |  |
| --- | --- | --- |
|  | Xtπ=Xtk+t−tktk+1−tk​(Xtk+1−Xtk),t∈[tk,tk+1],k=0,…,n−1.X^{\pi}\_{t}=X\_{t\_{k}}+\frac{t-t\_{k}}{t\_{k+1}-t\_{k}}(X\_{t\_{k+1}}-X\_{t\_{k}}),\quad t\in[t\_{k},t\_{k+1}],\quad k=0,\ldots,n-1. |  |

The time-extended continuous path X^π:[0,T]→ℝd+1\widehat{X}^{\pi}\colon[0,T]\to\mathbb{R}^{d+1} with bounded variation is given by

|  |  |  |
| --- | --- | --- |
|  | X^tk:=(tk,Xtk),\widehat{X}\_{t\_{k}}:=(t\_{k},X\_{t\_{k}}), |  |

and for the values in between we again use a linear interpolation

|  |  |  |
| --- | --- | --- |
|  | X^tπ=X^tk+t−tktk+1−tk​(X^tk+1−X^tk),t∈[tk,tk+1],k=0,…,n−1.\widehat{X}^{\pi}\_{t}=\widehat{X}\_{t\_{k}}+\frac{t-t\_{k}}{t\_{k+1}-t\_{k}}(\widehat{X}\_{t\_{k+1}}-\widehat{X}\_{t\_{k}}),\quad t\in[t\_{k},t\_{k+1}],\quad k=0,\ldots,n-1. |  |

We denote by 𝒞π:={Xπ:X:π→ℝd,X0=x0}\mathcal{C}^{\pi}:=\{X^{\pi}:X\colon\pi\to\mathbb{R}^{d},X\_{0}=x\_{0}\} the space of bounded variation paths with fixed initial value x0∈ℝdx\_{0}\in\mathbb{R}^{d} constructed by a linear interpolation and by

|  |  |  |
| --- | --- | --- |
|  | 𝒞^π:={X^π:X:π→ℝd,X0=x0}\widehat{\mathcal{C}}^{\pi}:=\{\widehat{X}^{\pi}:X\colon\pi\to\mathbb{R}^{d},X\_{0}=x\_{0}\} |  |

the corresponding space of time-extended paths.

Observe that the spaces 𝒞π\mathcal{C}^{\pi} and 𝒞^π\widehat{\mathcal{C}}^{\pi} are subspaces of the space of paths with bounded variation.

We define the signature of a continuous path of bounded variation as follows: Let X∈C1​-var​([0,T];ℝd)X\in C^{1\textup{-var}}([0,T];\mathbb{R}^{d}) be a path of bounded variation. Then, we denote its signature truncated at level NN on [s,t]⊂[0,T][s,t]\subset[0,T] by

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,tN:=(1,∫s<u<tdXu,…,∫s<u1<…<uN<tdXu1⊗⋯⊗dXuN)∈TN​(ℝd),\mathbb{X}\_{s,t}^{N}:=\Bigl(1,\int\_{s<u<t}\,\mathrm{d}X\_{u},\ldots,\int\_{s<u\_{1}<\ldots<u\_{N}<t}\,\mathrm{d}X\_{u\_{1}}\otimes\cdots\otimes\,\mathrm{d}X\_{u\_{N}}\Bigr)\in T^{N}(\mathbb{R}^{d}), |  |

for 0≤s≤t≤T0\leq s\leq t\leq T, where the integrals are defined via Riemann–Stieltjes integration, and

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,t:=(1,𝕏s,t(1),𝕏s,t(2),…,𝕏s,t(N),…)∈T​((ℝd)),\mathbb{X}\_{s,t}:=(1,\mathbb{X}\_{s,t}^{(1)},\mathbb{X}\_{s,t}^{(2)},\ldots,\mathbb{X}\_{s,t}^{(N)},\ldots)\in T((\mathbb{R}^{d})), |  |

the signature, where

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,t(n):=∫s<u1<…<un<tdXu1⊗⋯⊗dXun\mathbb{X}\_{s,t}^{(n)}:=\int\_{s<u\_{1}<\ldots<u\_{n}<t}\,\mathrm{d}X\_{u\_{1}}\otimes\cdots\otimes\,\mathrm{d}X\_{u\_{n}} |  |

denotes the nn-th component of 𝕏s,t\mathbb{X}\_{s,t}. For s=0s=0 we simply write 𝕏t\mathbb{X}\_{t}.

Further, for a normed space (E,∥⋅∥E)(E,\|\cdot\|\_{E}) and α∈(0,1]\alpha\in(0,1], the α\alpha-Hölder norm of a path X∈C​([0,T];E)X\in C([0,T];E) is given by

|  |  |  |
| --- | --- | --- |
|  | ‖X‖α:=sup0≤s<t≤T‖Xt−Xs‖E|t−s|α.\|X\|\_{\alpha}:=\sup\_{0\leq s<t\leq T}\frac{\|X\_{t}-X\_{s}\|\_{E}}{|t-s|^{\alpha}}. |  |

We write Cα​([0,T];E)C^{\alpha}([0,T];E) for the space of paths X∈C​([0,T];E)X\in C([0,T];E) which satisfy ‖X‖α<∞\|X\|\_{\alpha}<\infty and call this space the space of α\alpha-Hölder continuous paths.

The corresponding metric, we denote by

|  |  |  |
| --- | --- | --- |
|  | dα​(X,Y):=sups<ts,t∈[0,T]‖Xs,t−Ys,t‖E|t−s|α,d\_{\alpha}(X,Y):=\sup\_{\overset{s,t\in[0,T]}{s<t}}\frac{\|X\_{s,t}-Y\_{s,t}\|\_{E}}{|t-s|^{\alpha}}, |  |

where Xs,t:=Xt−XsX\_{s,t}:=X\_{t}-X\_{s} for paths X,Y:[0,T]→EX,Y\colon[0,T]\to E, with the same initial point X0=Y0=x0,X\_{0}=Y\_{0}=x\_{0}, x0∈ℝdx\_{0}\in\mathbb{R}^{d}. Moreover, we define the metric

|  |  |  |
| --- | --- | --- |
|  | d∞​(X,Y):=supt∈[0,T]‖Xt−Yt‖E,d\_{\infty}(X,Y):=\sup\_{t\in[0,T]}\|X\_{t}-Y\_{t}\|\_{E}, |  |

for paths X,Y:[0,T]→EX,Y\colon[0,T]\to E, with X0=Y0=x0X\_{0}=Y\_{0}=x\_{0}.

###### Remark 2.1.

Observe that by constructing paths through linear interpolation, these paths are even Lipschitz continuous and thus 11-Hölder continuous. This allows us to equip this space with the 11-Hölder norm. Consequently, the spaces 𝒞π\mathcal{C}^{\pi} and 𝒞^π\widehat{\mathcal{C}}^{\pi} can be regarded as subspaces of the space of 11-Hölder continuous paths. Furthermore, as the space of 11-Hölder continuous paths is itself a subspace of the space of α\alpha-Hölder continuous paths, 𝒞π\mathcal{C}^{\pi} and 𝒞^π\widehat{\mathcal{C}}^{\pi} can be equipped with any α\alpha-Hölder norm for any α∈(0,1]\alpha\in(0,1]. Finally, note that these spaces are also Polish, as all paths in 𝒞π\mathcal{C}^{\pi} and 𝒞^π\widehat{\mathcal{C}}^{\pi} are piecewise linear.

In the following we denote by 𝕏π:=(1,Xπ,𝕏π,(2),…)\mathbb{X}^{\pi}:=(1,X^{\pi},\mathbb{X}^{\pi,(2)},\ldots) and 𝕏^π:=(1,X^π,𝕏^π,(2),…)\widehat{\mathbb{X}}^{\pi}:=(1,\widehat{X}^{\pi},\widehat{\mathbb{X}}^{\pi,(2)},\ldots) the signature of paths in 𝒞π\mathcal{C}^{\pi} and 𝒞^π\widehat{\mathcal{C}}^{\pi}, respectively, where the signature is defined as the tensor series of iterated (Riemann–Stieltjes) integrals. For N∈ℕN\in\mathbb{N}, the signature of 𝕏^π\widehat{\mathbb{X}}^{\pi} truncated at level NN is the path t↦𝕏^tπ,Nt\mapsto\widehat{\mathbb{X}}^{\pi,N}\_{t} defined by computing all iterated integrals up to order NN.

The Carnot–Carathéodory norm ∥⋅∥c​c\|\cdot\|\_{cc} on GN​(ℝd)G^{N}(\mathbb{R}^{d}) is defined by

|  |  |  |
| --- | --- | --- |
|  | ∥𝐠∥c​c:=inf{∫0T|dXt|:X∈C1​-var([0,T];ℝd)such that𝕏TN=𝐠},\|\mathbf{g}\|\_{cc}:=\inf\biggl\{\int\_{0}^{T}|\,\mathrm{d}X\_{t}|\,:X\in C^{1\textup{-var}}([0,T];\mathbb{R}^{d})~\text{such that}~\mathbb{X}\_{T}^{N}=\mathbf{g}\biggr\}, |  |

for 𝐠∈GN​(ℝd)\mathbf{g}\in G^{N}(\mathbb{R}^{d}). This norm induces a metric via

|  |  |  |
| --- | --- | --- |
|  | dc​c​(𝐠,𝐡):=‖𝐠−1⊗𝐡‖c​c,d\_{cc}(\mathbf{g},\mathbf{h}):=\|\mathbf{g}^{-1}\otimes\mathbf{h}\|\_{cc}, |  |

for 𝐠,𝐡∈GN​(ℝd)\mathbf{g},\mathbf{h}\in G^{N}(\mathbb{R}^{d}).

For paths of lower regularity, i.e. for paths of finite α\alpha-Hölder norm with α∈(0,1]\alpha\in(0,1], it is necessary to work within the framework of rough path theory. In particular, we recall the definition of (weakly) geometric α\alpha-Hölder rough paths.

For α∈(0,1]\alpha\in(0,1], a continuous path 𝐗:[0,T]→G⌊1/α⌋​(ℝd)\mathbf{X}\colon[0,T]\to G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d}) of the form

|  |  |  |
| --- | --- | --- |
|  | [0,T]∋t↦𝐗t:=(1,Xt,𝕏t(2),…,𝕏t(⌊1/α⌋))∈G⌊1/α⌋​(ℝd)[0,T]\ni t\mapsto\mathbf{X}\_{t}:=(1,X\_{t},\mathbb{X}\_{t}^{(2)},\ldots,\mathbb{X}\_{t}^{(\lfloor 1/\alpha\rfloor)})\in G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d}) |  |

with 𝐗0:=𝟏:=(1,0,…,0)∈G⌊1/α⌋​(ℝd)\mathbf{X}\_{0}:=\mathbf{1}:=(1,0,\ldots,0)\in G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d}) is called geometric α\alpha-Hölder rough path if the α\alpha-Hölder rough path norm

|  |  |  |
| --- | --- | --- |
|  | ‖𝐗‖c​c,α:=sups<ts,t∈[0,T]dc​c​(𝐗s,𝐗t)|s−t|α\|\mathbf{X}\|\_{cc,\alpha}:=\sup\_{\overset{s,t\in[0,T]}{s<t}}\frac{d\_{cc}(\mathbf{X}\_{s},\mathbf{X}\_{t})}{|s-t|^{\alpha}} |  |

is finite. We denote by C0α​([0,T];G⌊1/α⌋​(ℝd))C\_{0}^{\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})) the space of such geometric α\alpha-Hölder rough paths, which we equip with the metric

|  |  |  |
| --- | --- | --- |
|  | dc​c,α​(𝐗,𝐘):=sups<ts,t∈[0,T]dc​c​(𝐗s,t,𝐘s,t)|s−t|α,d\_{cc,\alpha}(\mathbf{X},\mathbf{Y}):=\sup\_{\overset{s,t\in[0,T]}{s<t}}\frac{d\_{cc}(\mathbf{X}\_{s,t},\mathbf{Y}\_{s,t})}{|s-t|^{\alpha}}, |  |

for 𝐗,𝐘∈C0α​([0,T];G⌊1/α⌋​(ℝd))\mathbf{X},\mathbf{Y}\in C\_{0}^{\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})), where 𝐗s,t:=𝐗s−1⊗𝐗t∈G⌊1/α⌋​(ℝd)\mathbf{X}\_{s,t}:=\mathbf{X}\_{s}^{-1}\otimes\mathbf{X}\_{t}\in G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d}). Moreover, we define the metric

|  |  |  |
| --- | --- | --- |
|  | dc​c,∞​(𝐗,𝐘):=supt∈[0,T]dc​c​(𝐗t,𝐘t),d\_{cc,\infty}(\mathbf{X},\mathbf{Y}):=\sup\_{t\in[0,T]}d\_{cc}(\mathbf{X}\_{t},\mathbf{Y}\_{t}), |  |

for 𝐗,𝐘∈C0α​([0,T];G⌊1/α⌋​(ℝd)).\mathbf{X},\mathbf{Y}\in C\_{0}^{\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})).

For α∈(0,1]\alpha\in(0,1], let 𝐗∈C0α​([0,T];G⌊1/α⌋​(ℝd))\mathbf{X}\in C\_{0}^{\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})) be a geometric α\alpha-Hölder rough path. Then, the truncated signature of 𝐗\mathbf{X} is defined as the unique path extension of 𝐗\mathbf{X} yielding a path

|  |  |  |
| --- | --- | --- |
|  | 𝕏N:[0,T]→GN​(ℝd),\mathbb{X}^{N}\colon[0,T]\to G^{N}(\mathbb{R}^{d}), |  |

for N>⌊1/α⌋N>\lfloor 1/\alpha\rfloor specified by Lyons’ extension theorem. Then, 𝕏N\mathbb{X}^{N} has finite α\alpha-Hölder norm ∥⋅∥c​c,α\|\cdot\|\_{cc,\alpha} and starts with the unit element 𝟏∈GN​(ℝd)\mathbf{1}\in G^{N}(\mathbb{R}^{d}). The signature of 𝐗\mathbf{X} is given by

|  |  |  |
| --- | --- | --- |
|  | [0,T]∋t↦𝕏t:=(1,𝕏t(1),…,𝕏t(⌊1/α⌋),…,𝕏t(N),…).[0,T]\ni t\mapsto\mathbb{X}\_{t}:=(1,\mathbb{X}\_{t}^{(1)},\ldots,\mathbb{X}\_{t}^{(\lfloor 1/\alpha\rfloor)},\ldots,\mathbb{X}\_{t}^{(N)},\ldots). |  |

Note that for X^π∈𝒞^π\widehat{X}^{\pi}\in\widehat{\mathcal{C}}^{\pi}, 𝐗^π:=(1,X^π)\widehat{\mathbf{X}}^{\pi}:=(1,\widehat{X}^{\pi}) is a geometric 11-Hölder rough path, that is 𝐗^tπ=(1,X^tπ)∈G1​(ℝd+1)\widehat{\mathbf{X}}\_{t}^{\pi}=(1,\widehat{X}\_{t}^{\pi})\in G^{1}(\mathbb{R}^{d+1}) and has finite α\alpha-Hölder rough path norm for any α∈(0,1]\alpha\in(0,1]. Therefore, 𝕏^tπ,N\widehat{\mathbb{X}}\_{t}^{\pi,N} is the canonical lift of 𝐗^tπ\widehat{\mathbf{X}}\_{t}^{\pi} to a path with values in GN​(ℝd+1)G^{N}(\mathbb{R}^{d+1}) (due to the integration by parts rule), and is α\alpha-Hölder continuous, i.e., 𝕏^π,N∈C0α​([0,T];GN​(ℝd+1))\widehat{\mathbb{X}}^{\pi,N}\in C\_{0}^{\alpha}([0,T];G^{N}(\mathbb{R}^{d+1})), for any α∈(0,1]\alpha\in(0,1].

## 3. Global universal approximation

In this section, we explore the approximation of LpL^{p}-functionals using linear combinations of signatures in discrete time. This approach is based on the concept of global universal approximation theorems (UAT) on weighted function spaces, as introduced in [[CST26](#bib.bibx17)].

### 3.1. Universal approximation on weighted spaces

We start by introducing the concept of weighted spaces, which will be crucial for obtaining a global universal approximation result. Unlike the standard universal approximation theorem, see for instance [[LNPA19](#bib.bibx33), [KO19](#bib.bibx30)] for the universality result on bounded variation spaces, this global version extends beyond the constraint of compact sets. We follow the weighted space framework of [[CST26](#bib.bibx17)], where the authors demonstrated that the space of weakly geometric rough paths forms a weighted space with an appropriate weight function. Similarly, we aim to show that the space 𝒞^π\widehat{\mathcal{C}}^{\pi} and the space of stopped paths, introduced later, are also weighted spaces, and in turn to deduce a universal approximation result on weighted spaces using the *weighted Stone–Weierstraß theorem* introduced in [[CST26](#bib.bibx17)].

To begin, we recall the framework of weighted function spaces. First, we define the weighted space, which then allows to define the corresponding weighted function space.

Let (X,τX)(X,\tau\_{X}) be a completely regular Hausdorff topological space. A function ψ:X→(0,∞)\psi\colon X\to(0,\infty) is called an admissible weight function if every pre-image KR:=ψ−1​((0,R])={x∈X:ψ​(x)≤R}K\_{R}:=\psi^{-1}((0,R])=\{x\in X:\psi(x)\leq R\} is compact with respect to τX\tau\_{X}, for all R>0R>0. In this case, we call the pair (X,ψ)(X,\psi) a weighted space.

Furthermore, we define the vector space

|  |  |  |
| --- | --- | --- |
|  | Bψ​(X):={f:X→ℝ:supx∈X|f​(x)|ψ​(x)<∞},B\_{\psi}(X):=\Bigl\{f\colon X\to\mathbb{R}:\sup\_{x\in X}\frac{|f(x)|}{\psi(x)}<\infty\Bigr\}, |  |

consisting of functions f:X→ℝf\colon X\to\mathbb{R}, whose growth is controlled by the growth of the weight function ψ:X→(0,∞)\psi\colon X\to(0,\infty), which we equip with the weighted norm ∥⋅∥ℬψ​(X)\|\cdot\|\_{\mathcal{B}\_{\psi}(X)} given by

|  |  |  |  |
| --- | --- | --- | --- |
| (3.1) |  | ‖f‖ℬψ​(X):=supx∈X|f​(x)|ψ​(x),f∈Bψ​(X).\|f\|\_{\mathcal{B}\_{\psi}(X)}:=\sup\_{x\in X}\frac{|f(x)|}{\psi(x)},\quad f\in B\_{\psi}(X). |  |

Note that the embedding Cb​(X)↪Bψ​(X)C\_{b}(X)\hookrightarrow B\_{\psi}(X) is continuous, allowing us to introduce the space

|  |  |  |
| --- | --- | --- |
|  | ℬψ​(X):=Cb​(X)¯∥⋅∥ℬψ​(X),\mathcal{B}\_{\psi}(X):=\overline{C\_{b}(X)}^{\,\|\cdot\|\_{\mathcal{B}\_{\psi}(X)}}, |  |

which is the closure of Cb​(X)C\_{b}(X) with respect to the norm ∥⋅∥ℬψ​(X)\|\cdot\|\_{\mathcal{B}\_{\psi}(X)}. Note that ℬψ​(X)\mathcal{B}\_{\psi}(X) is a Banach space with the norm ([3.1](#S3.E1 "In 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures")). We refer to ℬψ​(X)\mathcal{B}\_{\psi}(X) as a weighted function space.

In the following let us discuss, why the space 𝒞^π\widehat{\mathcal{C}}^{\pi}, equipped with the α′\alpha^{\prime}-Hölder norm for 0≤α′<α≤10\leq\alpha^{\prime}<\alpha\leq 1, is a weighted space. To this end, we define the weight function

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | ψ:𝒞^π→(0,∞),ψ​(X^π):=exp⁡(β​‖X^π‖αγ),\psi\colon\widehat{\mathcal{C}}^{\pi}\to(0,\infty),\quad\psi(\widehat{X}^{\pi}):=\exp(\beta\|\widehat{X}^{\pi}\|\_{\alpha}^{\gamma}), |  |

for some β>0\beta>0, γ≥1\gamma\geq 1 and α∈(0,1]\alpha\in(0,1]. This choice of the weight function is motivated by the weighted Stone–Weierstraß theorem, see [[CST26](#bib.bibx17), Theorem 3.9]. As discussed before, we can equip the space 𝒞^π\widehat{\mathcal{C}}^{\pi} with any α\alpha-Hölder norm. To ensure the space becomes a weighted space, we equip it with a weaker topology than the norm topology. In particular, we equip this space with the α′\alpha^{\prime}-Hölder norm for some 0≤α′<α≤10\leq\alpha^{\prime}<\alpha\leq 1. This is necessary to obtain an admissible weight function, i.e., to ensure that the closed unit ball

|  |  |  |
| --- | --- | --- |
|  | KR:={X^π∈𝒞^π:exp⁡(β​‖X^π‖αγ)≤R}K\_{R}:=\{\widehat{X}^{\pi}\in\widehat{\mathcal{C}}^{\pi}:\exp(\beta\|\widehat{X}^{\pi}\|\_{\alpha}^{\gamma})\leq R\} |  |

is compact w.r.t. the weaker topology. As we can compactly embed α\alpha-Hölder spaces into α′\alpha^{\prime}-Hölder spaces, for 0≤α′<α≤10\leq\alpha^{\prime}<\alpha\leq 1, we thus obtain that the weight function is admissible (see [[CST26](#bib.bibx17), Example 2.3]). Therefore, we can apply the weighted Stone–Weierstraß theorem, to obtain a global universal approximation theorem. Hence, let us state the universal approximation theorem on ℬψ​(𝒞^π)\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi}).

###### Proposition 3.1 (Universal approximation theorem on ℬψ​(𝒞^π)\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi})).

Let ψ\psi be defined as in ([3.2](#S3.E2 "In 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures")). Then, the linear span of the set

|  |  |  |
| --- | --- | --- |
|  | {X^π↦⟨eI,𝕏^Tπ⟩:I∈{0,…,d}N,N∈ℕ0}\Bigl\{\widehat{X}^{\pi}\mapsto\langle e\_{I},\widehat{\mathbb{X}}^{\pi}\_{T}\rangle:I\in\{0,\ldots,d\}^{N},~N\in\mathbb{N}\_{0}\Bigr\} |  |

is dense in ℬψ​(𝒞^π)\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi}), i.e., for every map f∈ℬψ​(𝒞^π)f\in\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi}) and every ε>0\varepsilon>0 there exists a linear function ℓ:T​((ℝd+1))→ℝ\boldsymbol{\ell}\colon T((\mathbb{R}^{d+1}))\to\mathbb{R} of the form 𝕏^Tπ↦ℓ​(𝕏^Tπ):=∑0≤|I|≤NℓI​⟨eI,𝕏^Tπ⟩\widehat{\mathbb{X}}^{\pi}\_{T}\mapsto\boldsymbol{\ell}(\widehat{\mathbb{X}}^{\pi}\_{T}):=\sum\_{0\leq|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{X}}^{\pi}\_{T}\rangle, with some N∈ℕ0N\in\mathbb{N}\_{0} and ℓI∈ℝ\ell\_{I}\in\mathbb{R}, such that

|  |  |  |
| --- | --- | --- |
|  | supX^π∈𝒞^π|f​(X^π)−ℓ​(𝕏^Tπ)|ψ​(X^π)<ε.\sup\_{\widehat{X}^{\pi}\in\widehat{\mathcal{C}}^{\pi}}\frac{|f(\widehat{X}^{\pi})-\boldsymbol{\ell}(\widehat{\mathbb{X}}^{\pi}\_{T})|}{\psi(\widehat{X}^{\pi})}<\varepsilon. |  |

###### Proof.

The proof follows a similar structure to that of [[CST26](#bib.bibx17), Theorem 5.4], where the authors show the result for weakly geometric α\alpha-Hölder rough path space. However, since we focus on piecewise linearly interpolated paths, certain arguments require modification. In particular, we will use the equivalence of the norms |⋅|ℝd+1|\cdot|\_{\mathbb{R}^{d+1}} and ∥⋅∥c​c\|\cdot\|\_{cc} on G1​(ℝd+1)G^{1}(\mathbb{R}^{d+1}) and that for paths of bounded variation, the signature is uniquely determined by the path itself.

We want to apply the weighted Stone–Weierstraß theorem given in [[CST26](#bib.bibx17)]. Therefore, we have to show that the set

|  |  |  |
| --- | --- | --- |
|  | 𝒜:=span⁡{X^π↦⟨eI,𝕏^Tπ⟩:I∈{0,…,d}N,N∈ℕ0}⊆ℬψ​(𝒞^π)\mathcal{A}:=\operatorname{span}\{\widehat{X}^{\pi}\mapsto\langle e\_{I},\widehat{\mathbb{X}}^{\pi}\_{T}\rangle:I\in\{0,\ldots,d\}^{N},N\in\mathbb{N}\_{0}\}\subseteq\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi}) |  |

is a vector subspace and point-separating of ψ\psi-moderate growth, which vanishes nowhere. Let us start by showing that 𝒜⊆ℬψ​(𝒞^π)\mathcal{A}\subseteq\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi}) is a vector subspace. Therefore, fix some a∈𝒜a\in\mathcal{A} with X^π↦a​(X^π):=⟨eI,𝕏^Tπ⟩∈ℝ\widehat{X}^{\pi}\mapsto a(\widehat{X}^{\pi}):=\langle e\_{I},\widehat{\mathbb{X}}^{\pi}\_{T}\rangle\in\mathbb{R}, for some I∈{0,…,d}NI\in\{0,\ldots,d\}^{N} and N∈ℕ0N\in\mathbb{N}\_{0}. For some fixed R>0R>0 the pre-image KR=ψ−1​((0,R])K\_{R}=\psi^{-1}((0,R]) is bounded with respect to ∥⋅∥α\|\cdot\|\_{\alpha}. As ℬψ​(𝒞^π)\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi}) is the same for each dα′d\_{\alpha^{\prime}}, α′∈[0,α)∪{∞}\alpha^{\prime}\in[0,\alpha)\cup\{\infty\}, see [[CST26](#bib.bibx17)], we show the claim for d∞.d\_{\infty}.

Note that by Theorem 7.44 in [[FV10](#bib.bibx25)] all homogeneous norms are equivalent on GN​(ℝd+1)G^{N}(\mathbb{R}^{d+1}). In particular, the Carnot–Carathéodory norm and the norm ‖𝐚‖=maxi=1,…,N⁡|𝐚(i)|(ℝd+1)⊗i1i\|\mathbf{a}\|=\max\_{i=1,\ldots,N}|\mathbf{a}^{(i)}|\_{(\mathbb{R}^{d+1})^{\otimes i}}^{\frac{1}{i}} are homogeneous and thus equivalent. For N=1N=1 this translates to the equivalence of the norms ∥⋅∥c​c\|\cdot\|\_{cc} and |⋅|ℝd+1|\cdot|\_{\mathbb{R}^{d+1}} on G1​(ℝd+1)G^{1}(\mathbb{R}^{d+1}). Therefore, this yields that the map

|  |  |  |
| --- | --- | --- |
|  | ι:(𝒞^π,d∞)→(C0α​([0,T];G1​(ℝd+1)),dc​c,∞)viaX^π↦𝐗^π,\iota\colon(\widehat{\mathcal{C}}^{\pi},d\_{\infty})\to(C\_{0}^{\alpha}([0,T];G^{1}(\mathbb{R}^{d+1})),d\_{cc,\infty})\quad\text{via}\quad\widehat{X}^{\pi}\mapsto\widehat{\mathbf{X}}^{\pi}, |  |

is continuous. Moreover, observe that 𝕏^π,N\widehat{\mathbb{X}}^{\pi,N} satisfies the following ODE on TN​(ℝd+1)T^{N}(\mathbb{R}^{d+1}):

|  |  |  |
| --- | --- | --- |
|  | d​𝕏^tπ,N=𝕏^tπ,N⊗d​X^tπ,𝕏^0π,N=𝟏∈GN​(ℝd+1).\,\mathrm{d}\widehat{\mathbb{X}}\_{t}^{\pi,N}=\widehat{\mathbb{X}}\_{t}^{\pi,N}\otimes\,\mathrm{d}\widehat{X}\_{t}^{\pi},\quad\widehat{\mathbb{X}}\_{0}^{\pi,N}=\mathbf{1}\in G^{N}(\mathbb{R}^{d+1}). |  |

This can also be viewed as a rough differential equation (RDE) (see [[CPSF25](#bib.bibx16), (C.4)] for a similar argument), i.e.,

|  |  |  |
| --- | --- | --- |
|  | d​𝕏^tπ,N=𝕏^tπ,N⊗d​𝐗^tπ,𝕏^0π,N=𝟏∈GN​(ℝd+1).\,\mathrm{d}\widehat{\mathbb{X}}\_{t}^{\pi,N}=\widehat{\mathbb{X}}\_{t}^{\pi,N}\otimes\,\mathrm{d}\widehat{\mathbf{X}}\_{t}^{\pi},\quad\widehat{\mathbb{X}}\_{0}^{\pi,N}=\mathbf{1}\in G^{N}(\mathbb{R}^{d+1}). |  |

Then, it follows by [[FV10](#bib.bibx25), Corollary 10.40] that

|  |  |  |
| --- | --- | --- |
|  | (ι​(KR),dc​c,∞)∋𝐗^π↦𝕏^π,N∈(C0α​([0,T];GN​(ℝd+1)),dc​c,∞)(\iota(K\_{R}),d\_{cc,\infty})\ni\widehat{\mathbf{X}}^{\pi}\mapsto\widehat{\mathbb{X}}^{\pi,N}\in(C\_{0}^{\alpha}([0,T];G^{N}(\mathbb{R}^{d+1})),d\_{cc,\infty}) |  |

is continuous on ι​(KR)\iota(K\_{R}). Thus,

|  |  |  |
| --- | --- | --- |
|  | (KR,d∞)∋X^π↦𝕏^π,N∈(C0α​([0,T];GN​(ℝd+1)),dc​c,∞)(K\_{R},d\_{\infty})\ni\widehat{X}^{\pi}\mapsto\widehat{\mathbb{X}}^{\pi,N}\in(C\_{0}^{\alpha}([0,T];G^{N}(\mathbb{R}^{d+1})),d\_{cc,\infty}) |  |

is continuous on KRK\_{R}, as a composition of continuous maps. In addition, we know that the evaluation map

|  |  |  |
| --- | --- | --- |
|  | (C0α​([0,T];GN​(ℝd+1)),dc​c,∞)∋𝕏^π,N↦𝕏^Tπ,N∈(GN​(ℝd+1),dc​c)(C\_{0}^{\alpha}([0,T];G^{N}(\mathbb{R}^{d+1})),d\_{cc,\infty})\ni\widehat{\mathbb{X}}^{\pi,N}\mapsto\widehat{\mathbb{X}}\_{T}^{\pi,N}\in(G^{N}(\mathbb{R}^{d+1}),d\_{cc}) |  |

is continuous on KRK\_{R}. Since the composition of continuous functions is again continuous, we obtain that the map

|  |  |  |
| --- | --- | --- |
|  | (KR,d∞)∋X^π↦𝕏^Tπ,N∈(GN​(ℝd+1),dc​c)(K\_{R},d\_{\infty})\ni\widehat{X}^{\pi}\mapsto\widehat{\mathbb{X}}^{\pi,N}\_{T}\in(G^{N}(\mathbb{R}^{d+1}),d\_{cc}) |  |

is continuous on KRK\_{R}. Altogether, we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.3) |  | (KR,d∞)∋X^π↦a​(X^π)=⟨eI,𝕏^Tπ⟩∈ℝ(K\_{R},d\_{\infty})\ni\widehat{X}^{\pi}\mapsto a(\widehat{X}^{\pi})=\langle e\_{I},\widehat{\mathbb{X}}^{\pi}\_{T}\rangle\in\mathbb{R} |  |

is continuous on KRK\_{R} by the linearity of aa. Hence a|KR∈C​(KR)a\_{|\_{K\_{R}}}\in C(K\_{R}) for all R>0R>0 since RR was chosen arbitrarily.

Using the ball-box estimate [[FV10](#bib.bibx25), Proposition 7.49, Proposition 7.45], we get

|  |  |  |
| --- | --- | --- |
|  | ‖𝕏^Tπ,N−𝕏^0π,N‖TN​(ℝd+1)≤C1​max⁡{dc​c​(𝕏^Tπ,N,𝕏^0π,N),dc​c​(𝕏^Tπ,N,𝕏^0π,N)N}\|\widehat{\mathbb{X}}\_{T}^{\pi,N}-\widehat{\mathbb{X}}\_{0}^{\pi,N}\|\_{T^{N}(\mathbb{R}^{d+1})}\leq C\_{1}\max\Bigl\{d\_{cc}(\widehat{\mathbb{X}}\_{T}^{\pi,N},\widehat{\mathbb{X}}\_{0}^{\pi,N}),d\_{cc}(\widehat{\mathbb{X}}\_{T}^{\pi,N},\widehat{\mathbb{X}}\_{0}^{\pi,N})^{N}\Bigr\} |  |

for some constant C1≥1C\_{1}\geq 1, we have for every X^π∈𝒞^π\widehat{X}^{\pi}\in\widehat{\mathcal{C}}^{\pi},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |a​(X^π)|\displaystyle|a(\widehat{X}^{\pi})| | =|⟨eI,𝕏^Tπ⟩|≤‖𝕏^Tπ,N‖TN​(ℝd+1)≤‖𝕏^Tπ,N−𝕏^0π,N‖TN​(ℝd+1)+1\displaystyle=|\langle e\_{I},\widehat{\mathbb{X}}\_{T}^{\pi}\rangle|\leq\|\widehat{\mathbb{X}}\_{T}^{\pi,N}\|\_{T^{N}(\mathbb{R}^{d+1})}\leq\|\widehat{\mathbb{X}}\_{T}^{\pi,N}-\widehat{\mathbb{X}}\_{0}^{\pi,N}\|\_{T^{N}(\mathbb{R}^{d+1})}+1 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C1​(dc​c​(𝕏^Tπ,N,𝕏^0π,N)N+2).\displaystyle\leq C\_{1}(d\_{cc}(\widehat{\mathbb{X}}\_{T}^{\pi,N},\widehat{\mathbb{X}}\_{0}^{\pi,N})^{N}+2). |  |

Using the inequality dc​c​(𝕏^sπ,N,𝕏^tπ,N)≤CN,α​dc​c​(𝐗^sπ,𝐗^tπ)d\_{cc}(\widehat{\mathbb{X}}\_{s}^{\pi,N},\widehat{\mathbb{X}}\_{t}^{\pi,N})\leq C\_{N,\alpha}d\_{cc}(\widehat{\mathbf{X}}^{\pi}\_{s},\widehat{\mathbf{X}}^{\pi}\_{t}) for some constant CN,α>0C\_{N,\alpha}>0 (see [[FV10](#bib.bibx25), Theorem 9.5]), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | |a​(X^π)|\displaystyle|a(\widehat{X}^{\pi})| | ≤C1​(dc​c​(𝕏^Tπ,N,𝕏^0π,N)N+2)\displaystyle\leq C\_{1}(d\_{cc}(\widehat{\mathbb{X}}\_{T}^{\pi,N},\widehat{\mathbb{X}}\_{0}^{\pi,N})^{N}+2) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C1​(Tα​N​(sup0≤s<t≤Tdc​c​(𝕏^sπ,N,𝕏^tπ,N)|t−s|α)N+2)\displaystyle\leq C\_{1}\Bigl(T^{\alpha N}\Bigl(\sup\_{0\leq s<t\leq T}\frac{d\_{cc}(\widehat{\mathbb{X}}\_{s}^{\pi,N},\widehat{\mathbb{X}}\_{t}^{\pi,N})}{|t-s|^{\alpha}}\Bigr)^{N}+2\Bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C1​(CN,αN​Tα​N​(sup0≤s<t≤Tdc​c​(𝐗^sπ,𝐗^tπ)|t−s|α)N+2).\displaystyle\leq C\_{1}\Bigl(C\_{N,\alpha}^{N}T^{\alpha N}\Bigl(\sup\_{0\leq s<t\leq T}\frac{d\_{cc}(\widehat{\mathbf{X}}\_{s}^{\pi},\widehat{\mathbf{X}}\_{t}^{\pi})}{|t-s|^{\alpha}}\Bigr)^{N}+2\Bigr). |  |

Using the equivalence of the norms ∥⋅∥c​c\|\cdot\|\_{cc} and |⋅|ℝd+1|\cdot|\_{\mathbb{R}^{d+1}} on G1​(ℝd+1)G^{1}(\mathbb{R}^{d+1}), i.e. dc​c​(𝐗^sπ,𝐗^tπ)≤C2​|X^tπ−X^sπ|ℝd+1d\_{cc}(\widehat{\mathbf{X}}\_{s}^{\pi},\widehat{\mathbf{X}}\_{t}^{\pi})\leq C\_{2}|\widehat{X}\_{t}^{\pi}-\widehat{X}\_{s}^{\pi}|\_{\mathbb{R}^{d+1}} for some constant C2>0C\_{2}>0, yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | |a​(X^π)|\displaystyle|a(\widehat{X}^{\pi})| | ≤C1(CN,αNTα​N(sup0≤s<t≤Tdc​c​(𝐗^sπ,𝐗^tπ)|t−s|α)N+2)\displaystyle\leq C\_{1}\Bigl(C\_{N,\alpha}^{N}T^{\alpha N}\Bigl(\sup\_{0\leq s<t\leq T}\frac{d\_{cc}(\widehat{\mathbf{X}}\_{s}^{\pi},\widehat{\mathbf{X}}\_{t}^{\pi})}{|t-s|^{\alpha}}\Bigr)^{N}+2\Bigl) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C1(CN,αNC2NTα​N(sup0≤s<t≤T|X^tπ−X^sπ|ℝd+1|t−s|α)N+2)\displaystyle\leq C\_{1}\Bigl(C\_{N,\alpha}^{N}C\_{2}^{N}T^{\alpha N}\Bigl(\sup\_{0\leq s<t\leq T}\frac{|\widehat{X}\_{t}^{\pi}-\widehat{X}\_{s}^{\pi}|\_{\mathbb{R}^{d+1}}}{|t-s|^{\alpha}}\Bigr)^{N}+2\Bigl) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =C1​(CN,αN​C2N​Tα​N​‖X^π‖αN+2).\displaystyle=C\_{1}(C\_{N,\alpha}^{N}C\_{2}^{N}T^{\alpha N}\|\widehat{X}^{\pi}\|\_{\alpha}^{N}+2). |  |

Thus,

|  |  |  |
| --- | --- | --- |
|  | limR→∞supX^π∈𝒞^π\KR|a​(X^π)|ψ​(X^π)≤C1​supX^π∈𝒞^π\KR(CN,αNC2NTα​N∥X^π∥αN+2)exp⁡(β​‖X^π‖αγ)=0,\lim\_{R\to\infty}\sup\_{\widehat{X}^{\pi}\in\widehat{\mathcal{C}}^{\pi}\backslash K\_{R}}\frac{|a(\widehat{X}^{\pi})|}{\psi(\widehat{X}^{\pi})}\leq C\_{1}\sup\_{\widehat{X}^{\pi}\in\widehat{\mathcal{C}}^{\pi}\backslash K\_{R}}\frac{\Bigl(C\_{N,\alpha}^{N}C\_{2}^{N}T^{\alpha N}\|\widehat{X}^{\pi}\|\_{\alpha}^{N}+2\Bigl)}{\exp(\beta\|\widehat{X}^{\pi}\|\_{\alpha}^{\gamma})}=0, |  |

as the exponential function grows faster than any polynomial. Then, by Lemma 2.7 (ii) in [[CST26](#bib.bibx17)] (or Theorem 2.7 in [[DT10](#bib.bibx19)]) it follows that a∈ℬψ​(𝒞^π)a\in\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi}) and thus 𝒜⊆ℬψ​(𝒞^π)\mathcal{A}\subseteq\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi}). For the point separation we need to show that

|  |  |  |
| --- | --- | --- |
|  | 𝒜~:=span⁡{X^π↦⟨(eI​e0⊗k)⊗e0,𝕏^Tπ⟩:I∈{0,…,d}N,k∈ℕ0,N∈{0,1}}⊆𝒜\displaystyle\tilde{\mathcal{A}}:=\operatorname{span}\{\widehat{X}^{\pi}\mapsto\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{X}}^{\pi}\_{T}\rangle:I\in\{0,\ldots,d\}^{N},k\in\mathbb{N}\_{0},N\in\{0,1\}\}\subseteq\mathcal{A} |  |

is point-separating such that X^π↦exp⁡(|a~​(X^π)|)∈ℬψ​(𝒞^π)\widehat{X}^{\pi}\mapsto\exp(|\tilde{a}(\widehat{X}^{\pi})|)\in\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi}) for all a~∈ℬψ​(𝒞^π)\tilde{a}\in\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi}). In contrast to [[CST26](#bib.bibx17)] we consider paths of bounded variation, where higher order lifts are uniquely determined by the first order. Therefore, we have to show that for X^π,Y^π∈𝒞^π\widehat{X}^{\pi},\widehat{Y}^{\pi}\in\widehat{\mathcal{C}}^{\pi} distinct that there exists some k∈ℕ0k\in\mathbb{N}\_{0}, N∈{0,1}N\in\{0,1\} and I∈{0,…,d}NI\in\{0,\ldots,d\}^{N}, such that

|  |  |  |
| --- | --- | --- |
|  | ⟨(eI​e0⊗k)⊗e0,𝕏^Tπ⟩≠⟨(eI​e0⊗k)⊗e0,𝕐^Tπ⟩.\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{X}}^{\pi}\_{T}\rangle\neq\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{Y}}^{\pi}\_{T}\rangle. |  |

As in [[CST26](#bib.bibx17)] we can proceed by a proof of contradiction. Thus assume that for every k∈ℕ0k\in\mathbb{N}\_{0}, N∈{0,1}N\in\{0,1\} and I∈{0,…,d}NI\in\{0,\ldots,d\}^{N} it holds that

|  |  |  |
| --- | --- | --- |
|  | ⟨(eI​e0⊗k)⊗e0,𝕏^Tπ⟩=⟨(eI​e0⊗k)⊗e0,𝕐^Tπ⟩.\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{X}}^{\pi}\_{T}\rangle=\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{Y}}^{\pi}\_{T}\rangle. |  |

By the shuffle property, we observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨(eI​e0⊗k)⊗e0,𝕏^Tπ⟩\displaystyle\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{X}}^{\pi}\_{T}\rangle | =∫0T⟨eI​e0⊗k,𝕏^tπ⟩​dt=∫0T⟨eI,𝕏^tπ⟩​⟨e0⊗k,𝕏^tπ⟩​dt\displaystyle=\int\_{0}^{T}\langle e\_{I}\shuffle e\_{0}^{\otimes k},\widehat{\mathbb{X}}^{\pi}\_{t}\rangle\,\mathrm{d}t=\int\_{0}^{T}\langle e\_{I},\widehat{\mathbb{X}}^{\pi}\_{t}\rangle\langle e\_{0}^{\otimes k},\widehat{\mathbb{X}}^{\pi}\_{t}\rangle\,\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0T⟨eI,𝕏^tπ⟩​tkk!​dt,\displaystyle=\int\_{0}^{T}\langle e\_{I},\widehat{\mathbb{X}}^{\pi}\_{t}\rangle\frac{t^{k}}{k!}\,\mathrm{d}t, |  |

for all X^π∈𝒞^π\widehat{X}^{\pi}\in\widehat{\mathcal{C}}^{\pi}. Hence, we can conclude that for every k∈ℕ0k\in\mathbb{N}\_{0}, N∈{0,1}N\in\{0,1\} and I∈{0,…,d}NI\in\{0,\ldots,d\}^{N} we obtain

|  |  |  |
| --- | --- | --- |
|  | ∫0T⟨eI,𝕏^tπ−𝕐^tπ⟩​tkk!​dt=0.\int\_{0}^{T}\langle e\_{I},\widehat{\mathbb{X}}^{\pi}\_{t}-\widehat{\mathbb{Y}}^{\pi}\_{t}\rangle\frac{t^{k}}{k!}\,\mathrm{d}t=0. |  |

By [[BB11](#bib.bibx2), Corollary 4.24], we then deduce that ⟨eI,𝕏^tπ⟩=⟨eI,𝕐^tπ⟩\langle e\_{I},\widehat{\mathbb{X}}\_{t}^{\pi}\rangle=\langle e\_{I},\widehat{\mathbb{Y}}\_{t}^{\pi}\rangle for all I∈{0,…,d}NI\in\{0,\ldots,d\}^{N}, N∈{0,1}N\in\{0,1\}. This contradicts the assumption that X^π,Y^π\widehat{X}^{\pi},\widehat{Y}^{\pi} are distinct. Thus, we conclude that 𝒜~\tilde{\mathcal{A}} is point-separating. Therefore, as we consider continuous paths of bounded variation, it is enough to consider N∈{0,1}N\in\{0,1\} and k∈ℕ0k\in\mathbb{N}\_{0}.

Lastly, we have to show that exp⁡(λ​|a~​(⋅)|)∈ℬψ​(𝒞^π)\exp(\lambda|\tilde{a}(\cdot)|)\in\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi}). This is precisely the step where the choice of the exponential weight function, as given in ([3.2](#S3.E2 "In 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures")), becomes crucial. Therefore, let us fix some (X^π↦a~​(X^π)=ℓ​(𝕏^Tπ))∈𝒜~(\widehat{X}^{\pi}\mapsto\tilde{a}(\widehat{X}^{\pi})=\ell(\widehat{\mathbb{X}}^{\pi}\_{T}))\in\tilde{\mathcal{A}} with

|  |  |  |
| --- | --- | --- |
|  | ℓ​(𝕏^Tπ)=∑|I|≤N∑k=0KaI,k​⟨(eI​e0⊗k)⊗e0,𝕏^Tπ⟩,\ell(\widehat{\mathbb{X}}^{\pi}\_{T})=\sum\_{|I|\leq N}\sum\_{k=0}^{K}a\_{I,k}\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{X}}^{\pi}\_{T}\rangle, |  |

for some K∈ℕ0K\in\mathbb{N}\_{0}, N∈{0,1}N\in\{0,1\} and aI,k∈ℝa\_{I,k}\in\mathbb{R}. Then, by similar arguments as for ([3.3](#S3.E3 "In Proof. ‣ 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures")), we have exp(|a~(⋅)|)|KR∈C(KR)\exp(|\tilde{a}(\cdot)|)\_{|\_{K\_{R}}}\in C(K\_{R}) for all R>0R>0.

Moreover, using the ball-box estimate, as before, it follows that

|  |  |  |
| --- | --- | --- |
|  | |a~​(X^π)|=|ℓ​(𝕏^Tπ)|≤C1​‖ℓ‖TN+K+1​(ℝd+1)∗​(Tα​(K+1)​N​CN,αN​(sup0≤s<t≤Tdc​c​(𝐗^sπ,𝐗^tπ)|t−s|α)N+1),\displaystyle|\tilde{a}(\widehat{X}^{\pi})|=|\ell(\widehat{\mathbb{X}}\_{T}^{\pi})|\leq C\_{1}\|\ell\|\_{T^{N+K+1}(\mathbb{R}^{d+1})^{\ast}}\Bigl(T^{\alpha(K+1)N}C\_{N,\alpha}^{N}\Bigl(\sup\_{0\leq s<t\leq T}\frac{d\_{cc}(\widehat{\mathbf{X}}\_{s}^{\pi},\widehat{\mathbf{X}}\_{t}^{\pi})}{|t-s|^{\alpha}}\Bigr)^{N}+1\Bigr), |  |

for some constants C1,CN,α>0C\_{1},C\_{N,\alpha}>0. Using the equivalence of the norms ‖𝐗^π‖c​c\|\widehat{\mathbf{X}}^{\pi}\|\_{cc} and |X^π|ℝd+1|\widehat{X}^{\pi}|\_{\mathbb{R}^{d+1}} with some constant C2>0C\_{2}>0, yields

|  |  |  |
| --- | --- | --- |
|  | C1​‖ℓ‖TN+K+1​(ℝd+1)∗​(Tα​(K+1)​N​CN,αN​(sup0≤s<t≤Tdc​c​(𝐗^sπ,𝐗^tπ)|t−s|α)N+1)\displaystyle C\_{1}\|\ell\|\_{T^{N+K+1}(\mathbb{R}^{d+1})^{\ast}}\Bigl(T^{\alpha(K+1)N}C\_{N,\alpha}^{N}\Bigl(\sup\_{0\leq s<t\leq T}\frac{d\_{cc}(\widehat{\mathbf{X}}\_{s}^{\pi},\widehat{\mathbf{X}}\_{t}^{\pi})}{|t-s|^{\alpha}}\Bigr)^{N}+1\Bigr) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤C1​‖ℓ‖TN+K+1​(ℝd+1)∗​(Tα​(K+1)​N​CN,αN​C2N​(sup0≤s<t≤T|X^tπ−X^sπ|ℝd+1|t−s|α)N+1)\displaystyle\quad\leq C\_{1}\|\ell\|\_{T^{N+K+1}(\mathbb{R}^{d+1})^{\ast}}\Bigl(T^{\alpha(K+1)N}C\_{N,\alpha}^{N}C^{N}\_{2}\Bigl(\sup\_{0\leq s<t\leq T}\frac{|\widehat{X}\_{t}^{\pi}-\widehat{X}\_{s}^{\pi}|\_{\mathbb{R}^{d+1}}}{|t-s|^{\alpha}}\Bigr)^{N}+1\Bigr) |  |
|  |  |  |
| --- | --- | --- |
|  | =C1​‖ℓ‖TN+K+1​(ℝd+1)∗​(Tα​(K+1)​N​CN,αN​C2N​‖X^π‖αN+1).\displaystyle\quad=C\_{1}\|\ell\|\_{T^{N+K+1}(\mathbb{R}^{d+1})^{\ast}}\Bigl(T^{\alpha(K+1)N}C\_{N,\alpha}^{N}C^{N}\_{2}\|\widehat{X}^{\pi}\|^{N}\_{\alpha}+1\Bigr). |  |

Then, for C:=max⁡(C1​CN,αN​C2N​‖ℓ‖TN+K+1​(ℝd+1)∗​Tα​(K+1)​N,C1​‖ℓ‖TN+K+1​(ℝd+1)∗)C:=\max(C\_{1}C\_{N,\alpha}^{N}C^{N}\_{2}\|\ell\|\_{T^{N+K+1}(\mathbb{R}^{d+1})^{\ast}}T^{\alpha(K+1)N},C\_{1}\|\ell\|\_{T^{N+K+1}(\mathbb{R}^{d+1})^{\ast}}), we obtain

|  |  |  |
| --- | --- | --- |
|  | limR→∞supX^π∈𝒞^π\KRexp⁡(λ​|a~​(X^π)|)ψ​(X^π)≤limR→∞supX^π∈𝒞^π\KRexp⁡(λ​C​(‖X^π‖αN+1)−β​‖X^π‖αγ)=0,\lim\_{R\to\infty}\sup\_{\widehat{X}^{\pi}\in\widehat{\mathcal{C}}^{\pi}\backslash K\_{R}}\frac{\exp(\lambda|\tilde{a}(\widehat{X}^{\pi})|)}{\psi(\widehat{X}^{\pi})}\leq\lim\_{R\to\infty}\sup\_{\widehat{X}^{\pi}\in\widehat{\mathcal{C}}^{\pi}\backslash K\_{R}}\exp(\lambda C(\|\widehat{X}^{\pi}\|^{N}\_{\alpha}+1)-\beta\|\widehat{X}^{\pi}\|\_{\alpha}^{\gamma})=0, |  |

for λ<βC\lambda<\frac{\beta}{C} small enough and since the exponent tends to −∞-\infty as R→∞R\to\infty and using that γ≥1≥N\gamma\geq 1\geq N, the last equality follows and thus we have by Lemma 2.7 (ii) in [[CST26](#bib.bibx17)] that exp⁡(λ​|a~​(⋅)|)∈ℬψ​(𝒞^π)\exp(\lambda|\tilde{a}(\cdot)|)\in\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi}) for any a~∈𝒜~.\tilde{a}\in\tilde{\mathcal{A}}.

Lastly, we show that 𝒜~\tilde{\mathcal{A}} vanishes nowhere. Using the map (X^π↦a~​(X^π):=⟨(e∅​e0⊗0)⊗e0,𝕏^Tπ⟩)∈𝒜~(\widehat{X}^{\pi}\mapsto\tilde{a}(\widehat{X}^{\pi}):=\langle(e\_{\emptyset}\shuffle e\_{0}^{\otimes 0})\otimes e\_{0},\widehat{\mathbb{X}}^{\pi}\_{T}\rangle)\in\tilde{\mathcal{A}}, then a~​(X^π)=∫0Tdt=T≠0\tilde{a}(\widehat{X}^{\pi})=\int\_{0}^{T}\,\mathrm{d}t=T\neq 0, for all X^π∈𝒞^π\widehat{X}^{\pi}\in\widehat{\mathcal{C}}^{\pi}. Then, by the weighted real-valued Stone–Weierstraß theorem, it follows that 𝒜\mathcal{A} is dense in ℬψ​(𝒞^π)\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi}). All in all, we see that the proof is very similar to the proof of Theorem 5.4 in [[CST26](#bib.bibx17)].
∎

We aim to establish a similar result for the space of stopped paths, which plays a fundamental role in functional Itô calculus, see [[CF13](#bib.bibx8), [Dup19](#bib.bibx20)], and also in rough path settings, see e.g. [[BPS25](#bib.bibx7), [CM25](#bib.bibx12)]. To this end, let us first introduce this space and recall the notion of a non-anticipative path functional.

The space of stopped paths in 𝒞^π\widehat{\mathcal{C}}^{\pi} is defined by

|  |  |  |
| --- | --- | --- |
|  | ΛTπ:=⋃t∈[0,T]𝒞^tπ:=⋃t∈[0,T]{X^[0,t]π∈𝒞^π:X^sπ=(s,Xsπ)​for all​s∈[0,t]}.\Lambda^{\pi}\_{T}:=\bigcup\_{t\in[0,T]}\widehat{\mathcal{C}}^{\pi}\_{t}:=\bigcup\_{t\in[0,T]}\{\widehat{X}^{\pi}\_{[0,t]}\in\widehat{\mathcal{C}}^{\pi}:\widehat{X}^{\pi}\_{s}=(s,X^{\pi}\_{s})~\text{for all}~s\in[0,t]\}. |  |

We equip this space with the metric (cf. [[CF13](#bib.bibx8), Section 2.2])

|  |  |  |
| --- | --- | --- |
|  | dΛ,α′​(X^[0,t]π,Y^[0,s]π):=|t−s|+dα′;[0,t]​(X^[0,t]π,Y^[0,t]π,s),s≤t,0≤α′<α,d\_{\Lambda,\alpha^{\prime}}(\widehat{X}^{\pi}\_{[0,t]},\widehat{Y}^{\pi}\_{[0,s]}):=|t-s|+d\_{\alpha^{\prime};[0,t]}(\widehat{X}\_{[0,t]}^{\pi},\widehat{Y}\_{[0,t]}^{\pi,s}),\quad s\leq t,\quad 0\leq\alpha^{\prime}<\alpha, |  |

where we denote by X^π,t\widehat{X}^{\pi,t} the process (X^π,t)u=(u,Xuπ,t)(\widehat{X}^{\pi,t})\_{u}=(u,X^{\pi,t}\_{u}), i.e., the process where XπX^{\pi} is stopped at time tt but the time-augmentation is not stopped.

Moreover, we call a map f:ΛTπ→ℝf\colon\Lambda^{\pi}\_{T}\to\mathbb{R} a non-anticipative functional if it is measurable. It is called continuous if f:ΛTπ→ℝf\colon\Lambda^{\pi}\_{T}\to\mathbb{R} is continuous with respect to the metric dΛ,α′d\_{\Lambda,\alpha^{\prime}}. Observe that the topology on the metric space (ΛTπ,dΛ,α′)(\Lambda^{\pi}\_{T},d\_{\Lambda,\alpha^{\prime}}) coincides with the final topology induced by the quotient map

|  |  |  |  |
| --- | --- | --- | --- |
| (3.4) |  | φ:[0,T]×𝒞^π→ΛTπ,φ​(t,X^π)=X^[0,t]π,\varphi\colon[0,T]\times\widehat{\mathcal{C}}^{\pi}\to\Lambda^{\pi}\_{T},\qquad\varphi(t,\widehat{X}^{\pi})=\widehat{X}^{\pi}\_{[0,t]}, |  |

where X^[0,t]π\widehat{X}^{\pi}\_{[0,t]} means that we restrict X^π\widehat{X}^{\pi}, which is defined on [0,T][0,T], to the sub-interval [0,t],t≤T[0,t],t\leq T. Here we omit the proof that the topologies coincide as the proof is very similar to the proof given in [[BHRS23](#bib.bibx6), Lemma A.1].

###### Remark 3.2.

The space ΛTπ\Lambda^{\pi}\_{T} is Polish (see [[LG94](#bib.bibx31)] and [[BHRS23](#bib.bibx6), Appendix A] for the proof for similar spaces).

To obtain a global universal approximation result on ΛTπ\Lambda\_{T}^{\pi}, we need to show that (ΛTπ,ψ)(\Lambda\_{T}^{\pi},\psi) is a weighted space. To that end, we consider the following weight function

|  |  |  |  |
| --- | --- | --- | --- |
| (3.5) |  | ψ​(X^[0,t]π):=exp⁡(β​‖X^[0,T]π,t‖αγ)\psi(\widehat{X}^{\pi}\_{[0,t]}):=\exp(\beta\|\widehat{X}^{\pi,t}\_{[0,T]}\|\_{\alpha}^{\gamma}) |  |

with γ≥1\gamma\geq 1 and β>0\beta>0.

###### Lemma 3.3.

Let 0≤α′<α≤10\leq\alpha^{\prime}<\alpha\leq 1 and let ψ\psi be defined as in ([3.5](#S3.E5 "In 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures")). Then KR:=ψ−1​((0,R])={X^[0,t]π∈ΛTπ:ψ​(X^[0,t]π)≤R}K\_{R}:=\psi^{-1}((0,R])=\{\widehat{X}^{\pi}\_{[0,t]}\in\Lambda^{\pi}\_{T}:\psi(\widehat{X}^{\pi}\_{[0,t]})\leq R\} is compact w.r.t. the quotient topology and (ΛTπ,ψ)(\Lambda\_{T}^{\pi},\psi) is a weighted space.

###### Proof.

First observe that by the definition of the quotient map φ\varphi, we have

|  |  |  |
| --- | --- | --- |
|  | KR=φ​([0,T]×{X^[0,T]π,t∈𝒞^π:ψ​(X^[0,t]π)≤R}).K\_{R}=\varphi\Bigl([0,T]\times\{\widehat{X}^{\pi,t}\_{[0,T]}\in\widehat{\mathcal{C}}^{\pi}:\psi(\widehat{X}^{\pi}\_{[0,t]})\leq R\}\Bigr). |  |

Since φ\varphi is continuous, we only need to show that [0,T]×{X^[0,T]π,t∈𝒞^π:ψ​(X^[0,t]π)≤R}[0,T]\times\{\widehat{X}^{\pi,t}\_{[0,T]}\in\widehat{\mathcal{C}}^{\pi}:\psi(\widehat{X}^{\pi}\_{[0,t]})\leq R\} is compact in [0,T]×𝒞^π[0,T]\times\widehat{\mathcal{C}}^{\pi} to obtain the compactness of KRK\_{R}. Therefore, observe that the sets {X^[0,T]π,t∈𝒞^π:ψ​(X^[0,t]π)≤R}\{\widehat{X}^{\pi,t}\_{[0,T]}\in\widehat{\mathcal{C}}^{\pi}:\psi(\widehat{X}\_{[0,t]}^{\pi})\leq R\} are equicontinuous and pointwise bounded. Using that α\alpha-Hölder spaces are compactly embedded in α′\alpha^{\prime}-Hölder spaces for α′<α\alpha^{\prime}<\alpha (cf. [[CST26](#bib.bibx17), Theorem A.4]), we obtain that the sets {X^[0,T]π,t∈𝒞^π:ψ​(X^[0,t]π)≤R}\{\widehat{X}^{\pi,t}\_{[0,T]}\in\widehat{\mathcal{C}}^{\pi}:\psi(\widehat{X}^{\pi}\_{[0,t]})\leq R\} are, by the Arzèla–Ascoli theorem, see e.g. [[Fol99](#bib.bibx23), Theorem 4.43], compact w.r.t. the α′\alpha^{\prime}-Hölder norm. Since φ\varphi is continuous, KRK\_{R} is also compact for any R>0R>0 due to Tychonoff’s theorem. Thus, (ΛTπ,ψ)(\Lambda^{\pi}\_{T},\psi) is a weighted space.
∎

###### Proposition 3.4 (Universal approximation theorem on ℬψ(ΛTπ\mathcal{B}\_{\psi}(\Lambda\_{T}^{\pi})).

Let ψ\psi be defined as in ([3.5](#S3.E5 "In 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures")). Then, the linear span of the set

|  |  |  |
| --- | --- | --- |
|  | {X^[0,t]π→⟨eI,𝕏^tπ⟩:I∈{0,…,d}N,N∈ℕ0}\Bigl\{\widehat{X}^{\pi}\_{[0,t]}\to\langle e\_{I},\widehat{\mathbb{X}}^{\pi}\_{t}\rangle:I\in\{0,\ldots,d\}^{N},N\in\mathbb{N}\_{0}\Bigr\} |  |

is dense in ℬψ​(ΛTπ)\mathcal{B}\_{\psi}(\Lambda\_{T}^{\pi}), i.e., for every map f∈ℬψ​(ΛTπ)f\in\mathcal{B}\_{\psi}(\Lambda\_{T}^{\pi}) and every ε>0\varepsilon>0, there exists a linear function ℓ:T​((ℝd+1))→ℝ\boldsymbol{\ell}\colon T((\mathbb{R}^{d+1}))\to\mathbb{R} of the form 𝕏^tπ↦ℓ​(𝕏^tπ):=∑|I|≤NℓI​⟨eI,𝕏^tπ⟩\widehat{\mathbb{X}}^{\pi}\_{t}\mapsto\boldsymbol{\ell}(\widehat{\mathbb{X}}^{\pi}\_{t}):=\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{X}}^{\pi}\_{t}\rangle, with some N∈ℕ0N\in\mathbb{N}\_{0} and ℓI∈ℝ\ell\_{I}\in\mathbb{R}, such that

|  |  |  |
| --- | --- | --- |
|  | supX^[0,t]π∈ΛTπ|f​(X^[0,t]π)−ℓ​(𝕏^tπ)|ψ​(X^[0,t]π)<ε.\sup\_{\widehat{X}^{\pi}\_{[0,t]}\in\Lambda\_{T}^{\pi}}\frac{|f(\widehat{X}^{\pi}\_{[0,t]})-\boldsymbol{\ell}(\widehat{\mathbb{X}}^{\pi}\_{t})|}{\psi(\widehat{X}^{\pi}\_{[0,t]})}<\varepsilon. |  |

###### Proof.

First note that Lemma [3.3](#S3.Thmtheorem3 "Lemma 3.3. ‣ 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures") implies that (ΛTπ,ψ)(\Lambda\_{T}^{\pi},\psi) is a weighted space. Hence, we may apply the weighted Stone–Weierstraß theorem introduced in [[CST26](#bib.bibx17), Theorem 3.9]. It therefore suffices to verify that 𝒜:=span⁡{X^[0,t]π↦⟨eI,𝕏^tπ⟩:I∈{0,…,d}N,N∈ℕ0}⊆ℬψ​(ΛTπ)\mathcal{A}:=\operatorname{span}\{\widehat{X}^{\pi}\_{[0,t]}\mapsto\langle e\_{I},\widehat{\mathbb{X}}\_{t}^{\pi}\rangle:I\in\{0,\ldots,d\}^{N},N\in\mathbb{N}\_{0}\}\subseteq\mathcal{B}\_{\psi}(\Lambda\_{T}^{\pi}) is a vector subspace and point-separating of ψ\psi-moderate growth, which vanishes nowhere. To that end, we need to prove that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜~\displaystyle\widetilde{\mathcal{A}} | :=span({X^[0,t]π↦⟨e∅,𝕏^tπ⟩}\displaystyle:=\operatorname{span}\Bigl(\Bigl\{\widehat{X}^{\pi}\_{[0,t]}\mapsto\langle e\_{\emptyset},\widehat{\mathbb{X}}^{\pi}\_{t}\rangle\Bigr\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∪{X^[0,t]π↦⟨(eIe0⊗k)⊗e0,𝕏^tπ⟩:k∈ℕ0,N∈{0,1},I∈{0,…,d}N})⊆𝒜,\displaystyle\qquad\cup\Bigl\{\widehat{X}^{\pi}\_{[0,t]}\mapsto\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{X}}^{\pi}\_{t}\rangle:\begin{matrix}k\in\mathbb{N}\_{0},\,N\in\{0,1\},\\ I\in\{0,\ldots,d\}^{N}\end{matrix}\Bigr\}\Bigr)\subseteq\mathcal{A}, |  |

is a point-separating and nowhere vanishing vector subspace of ψ\psi-moderate growth. The claim follows by combining the arguments of Proposition [3.1](#S3.Thmtheorem1 "Proposition 3.1 (Universal approximation theorem on ℬ_𝜓⁢(𝒞̂^𝜋)). ‣ 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures") with those of [[CP25](#bib.bibx15), Proposition 3.11], and we therefore omit the details.
∎

### 3.2. Approximation of LpL^{p}-functionals via signatures

We present global universal approximation theorems for LpL^{p}-functionals. Building on the universal approximation results for weighted function spaces from the previous subsection (Proposition [3.1](#S3.Thmtheorem1 "Proposition 3.1 (Universal approximation theorem on ℬ_𝜓⁢(𝒞̂^𝜋)). ‣ 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures") and Proposition [3.4](#S3.Thmtheorem4 "Proposition 3.4 (Universal approximation theorem on ℬ_𝜓(Λ_𝑇^𝜋)). ‣ 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures")), we now additionally impose an integrability condition on the weight function ψ\psi, thereby extending the result to LpL^{p}-functionals.

###### Theorem 3.5 (LpL^{p}-convergence).

Let p>1p>1.

1. (i)

   Let (𝒞^π,ℬ​(𝒞^π))(\widehat{\mathcal{C}}^{\pi},\mathcal{B}(\widehat{\mathcal{C}}^{\pi})) be a Borel space with finite measure ν\nu. Let ψ\psi be defined as in ([3.2](#S3.E2 "In 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures")) and ∫𝒞^πψp​dν<∞\int\_{\widehat{\mathcal{C}}^{\pi}}\psi^{p}\,\mathrm{d}\nu<\infty. Moreover, consider the set

   |  |  |  |
   | --- | --- | --- |
   |  | ℒ:={fℓ|fℓ:X^π↦ℓ(𝕏^Tπ)=∑|I|≤NℓI⟨eI,𝕏^Tπ⟩,ℓI∈ℝ,N∈ℕ0,X^π∈𝒞^π}.\mathcal{L}:=\Bigl\{f\_{\ell}|~f\_{\ell}\colon\widehat{X}^{\pi}\mapsto\boldsymbol{\ell}(\widehat{\mathbb{X}}\_{T}^{\pi})=\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{X}}\_{T}^{\pi}\rangle,~\ell\_{I}\in\mathbb{R},~N\in\mathbb{N}\_{0},~\widehat{X}^{\pi}\in\widehat{\mathcal{C}}^{\pi}\Bigr\}. |  |

   Then, for every f∈Lp​(𝒞^π;ν)f\in L^{p}(\widehat{\mathcal{C}}^{\pi};\nu) and for every ε>0\varepsilon>0, there exists a functional fℓ∈ℒf\_{\ell}\in\mathcal{L} such that

   |  |  |  |
   | --- | --- | --- |
   |  | ‖f−fℓ‖Lp​(𝒞^π)<ε.\|f-f\_{\ell}\|\_{L^{p}(\widehat{\mathcal{C}}^{\pi})}<\varepsilon. |  |
2. (ii)

   Let (ΛTπ,ℬ​(ΛTπ))(\Lambda\_{T}^{\pi},\mathcal{B}(\Lambda\_{T}^{\pi})) be a Borel space with finite measure ν\nu. Let ψ\psi be defined as in ([3.5](#S3.E5 "In 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures")) and ∫ΛTπψp​dν<∞\int\_{\Lambda\_{T}^{\pi}}\psi^{p}\,\mathrm{d}\nu<\infty. Moreover, consider the set

   |  |  |  |
   | --- | --- | --- |
   |  | ℒΛ:={fℓ|fℓ:X^[0,t]π↦ℓ(𝕏^tπ)=∑|I|≤NℓI⟨eI,𝕏^tπ⟩,ℓI∈ℝ,N∈ℕ0,X^[0,t]π∈ΛTπ}.\mathcal{L}\_{\Lambda}:=\Bigl\{f\_{\ell}|~f\_{\ell}\colon\widehat{X}\_{[0,t]}^{\pi}\mapsto\boldsymbol{\ell}(\widehat{\mathbb{X}}\_{t}^{\pi})=\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{X}}\_{t}^{\pi}\rangle,~\ell\_{I}\in\mathbb{R},~N\in\mathbb{N}\_{0},~\widehat{X}\_{[0,t]}^{\pi}\in\Lambda\_{T}^{\pi}\Bigr\}. |  |

   Then, for every f∈Lp​(ΛTπ;ν)f\in L^{p}(\Lambda\_{T}^{\pi};\nu) and for every ε>0\varepsilon>0, there exists a functional fℓ∈ℒΛf\_{\ell}\in\mathcal{L}\_{\Lambda} such that

   |  |  |  |
   | --- | --- | --- |
   |  | ‖f−fℓ‖Lp​(ΛTπ)<ε.\|f-f\_{\ell}\|\_{L^{p}(\Lambda\_{T}^{\pi})}<\varepsilon. |  |

###### Proof.

(i) Let f∈Lp​(𝒞^π;ν)f\in L^{p}(\widehat{\mathcal{C}}^{\pi};\nu). Fix ε>0\varepsilon>0.

Step 1: For any K>0K>0, we can define the function fK​(x):=1{|f​(x)|≤K}​(x)​f​(x)f\_{K}(x):=1\_{\{|f(x)|\leq K\}}(x)f(x) for which we have ‖f−fK‖Lp​(𝒞^π)→0\|f-f\_{K}\|\_{L^{p}(\widehat{\mathcal{C}}^{\pi})}\to 0 as K→∞K\to\infty by dominated convergence. Therefore, there is a Kε>0K^{\varepsilon}>0 such that ‖f−fKε‖Lp​(𝒞^π)≤ε3\|f-f\_{K^{\varepsilon}}\|\_{L^{p}(\widehat{\mathcal{C}}^{\pi})}\leq\frac{\varepsilon}{3}.

Step 2: By Lusin’s theorem [[DMP03](#bib.bibx18), Theorem 2.5.17], there is a closed set Cε⊂𝒞^πC^{\varepsilon}\subset\widehat{\mathcal{C}}^{\pi}, such that fKεf\_{K^{\varepsilon}} restricted to CεC^{\varepsilon} is continuous and ν​(𝒞^π∖Cε)≤εp(6​Kε)p\nu(\widehat{\mathcal{C}}^{\pi}\setminus C^{\varepsilon})\leq\frac{\varepsilon^{p}}{(6K^{\varepsilon})^{p}}. By Tietze’s extension theorem [[Fri82](#bib.bibx24), Theorem 3.6.3], there is a continuous extension fε∈Cb​(𝒞^π,[−Kε,Kε])f^{\varepsilon}\in C\_{b}(\widehat{\mathcal{C}}^{\pi},[-K^{\varepsilon},K^{\varepsilon}]) of fKε,f\_{K^{\varepsilon}}, such that

|  |  |  |
| --- | --- | --- |
|  | ‖fKε−fε‖Lp​(𝒞^π)p=∫𝒞^π∖Cε|fKε−fε|p​dν≤(2​Kε)p​ν​(𝒞^π∖Cε)≤(ε3)p.\|f\_{K^{\varepsilon}}-f^{\varepsilon}\|\_{L^{p}(\widehat{\mathcal{C}}^{\pi})}^{p}=\int\_{\widehat{\mathcal{C}}^{\pi}\setminus C^{\varepsilon}}|f\_{K^{\varepsilon}}-f^{\varepsilon}|^{p}\,\mathrm{d}\nu\leq(2K^{\varepsilon})^{p}\nu(\widehat{\mathcal{C}}^{\pi}\setminus C^{\varepsilon})\leq\Bigl(\frac{\varepsilon}{3}\Bigr)^{p}. |  |

Step 3: Moreover, since by the definition of the weighted function space ℬψ​(𝒞^π)\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi}) it holds that Cb​(𝒞^π)⊆ℬψ​(𝒞^π)C\_{b}(\widehat{\mathcal{C}}^{\pi})\subseteq\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi}), by Proposition [3.1](#S3.Thmtheorem1 "Proposition 3.1 (Universal approximation theorem on ℬ_𝜓⁢(𝒞̂^𝜋)). ‣ 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures") we can approximate fεf^{\varepsilon} by a linear combination of the signature. More precisely, setting M=∫𝒞^πψp​dν<∞M=\int\_{\widehat{\mathcal{C}}^{\pi}}\psi^{p}\,\mathrm{d}\nu<\infty we have

|  |  |  |
| --- | --- | --- |
|  | ‖fε−fℓ‖ℬψ​(𝒞^π)p=(supX^π∈𝒞^π|fε​(X^π)−ℓ​(𝕏^Tπ)|ψ​(X^π))p<εp3p​M.\|{f}^{\varepsilon}-f\_{\ell}\|^{p}\_{\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi})}=\Bigl(\sup\_{\widehat{X}^{\pi}\in\widehat{\mathcal{C}}^{\pi}}\frac{|{f}^{\varepsilon}(\widehat{X}^{\pi})-\boldsymbol{\ell}(\widehat{\mathbb{X}}\_{T}^{\pi})|}{\psi(\widehat{X}^{\pi})}\Bigr)^{p}<\frac{\varepsilon^{p}}{3^{p}M}. |  |

Hence, we get

|  |  |  |
| --- | --- | --- |
|  | ‖fε−fℓ‖Lp​(𝒞^π)p≤∫𝒞^πψp​dν​‖fε−fℓ‖ℬψ​(𝒞^π)p<(ε3)p.\|{f}^{\varepsilon}-f\_{\ell}\|^{p}\_{L^{p}(\widehat{\mathcal{C}}^{\pi})}\leq\int\_{\widehat{\mathcal{C}}^{\pi}}\psi^{p}\,\mathrm{d}\nu~\|{f}^{\varepsilon}-f\_{\ell}\|^{p}\_{\mathcal{B}\_{\psi}(\widehat{\mathcal{C}}^{\pi})}<\Bigl(\frac{\varepsilon}{3}\Bigr)^{p}. |  |

Altogether, we obtain

|  |  |  |
| --- | --- | --- |
|  | ‖f−fℓ‖Lp​(𝒞^π)≤‖f−fKε‖Lp​(𝒞^π)+‖fKε−fε‖Lp​(𝒞^π)+‖fε−fℓ‖Lp​(𝒞^π)<ε,\|f-f\_{\ell}\|\_{L^{p}(\widehat{\mathcal{C}}^{\pi})}\leq\|f-f\_{K^{\varepsilon}}\|\_{L^{p}(\widehat{\mathcal{C}}^{\pi})}+\|f\_{K^{\varepsilon}}-f^{\varepsilon}\|\_{L^{p}(\widehat{\mathcal{C}}^{\pi})}+\|{f}^{\varepsilon}-f\_{\ell}\|\_{L^{p}(\widehat{\mathcal{C}}^{\pi})}<\varepsilon, |  |

which concludes the proof.

(ii) The proof follows along the same lines as in (i), where in Step 3, we use Proposition [3.4](#S3.Thmtheorem4 "Proposition 3.4 (Universal approximation theorem on ℬ_𝜓(Λ_𝑇^𝜋)). ‣ 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures").
∎

###### Remark 3.6.

Note that the assumption ∫𝒞^πψp​dν<∞\int\_{\widehat{\mathcal{C}}^{\pi}}\psi^{p}\,\mathrm{d}\nu<\infty, with ψ​(X^π)=exp⁡(β​‖X^π‖αγ)\psi(\widehat{X}^{\pi})=\exp\Big(\beta\|\widehat{X}^{\pi}\|\_{\alpha}^{\gamma}\Big), represents an exponential moment condition. Such a condition is crucial for establishing LpL^{p}-convergence with the method developed here.

While our analysis is carried out in a discrete-time setting, several recent works establish LpL^{p}-type universal approximation theorems on spaces of weakly geometric rough paths. In [[CP25](#bib.bibx15)], a similar LpL^{p}-universal approximation theorem is derived within the framework of the geometric α\alpha-Hölder rough path space, assuming the pp-integrability of the weight function ψ​(𝐗^)=exp⁡(β​‖𝐗^‖c​c,αγ)\psi(\widehat{\mathbf{X}})=\exp(\beta\|\widehat{\mathbf{X}}\|\_{cc,\alpha}^{\gamma}) on rough path space. Despite the similarity of the two settings, our discrete-time results do not follow directly from [[CP25](#bib.bibx15)]. Indeed, while the LpL^{p}-approximation result can formally be transferred via pushforward arguments together with the canonical embedding of the space of piecewise linearly interpolated paths into the space of geometric α\alpha-Hölder rough paths C^d,Tα\widehat{C}\_{d,T}^{\alpha}, this argument does not extend to the weighted setting. The reason is that the weighted universal approximation theorem requires the corresponding functional to belong to the weighted space ℬψ​(C^d,Tα)\mathcal{B}\_{\psi}(\widehat{C}\_{d,T}^{\alpha}), which entails uniform control in the weighted supremum norm induced by the weight function ψ\psi. After composition with the canonical embedding map, however, such control is obtained only on the image of the embedding. In general, this does not imply that the induced functional remains controlled by the weight function on the entire space C^d,Tα\widehat{C}\_{d,T}^{\alpha}. Consequently, the weighted structure is not preserved when passing from continuous to discretely generated path spaces, and a separate discrete-time analysis is required.

We also note that LpL^{p}-approximation results on the geometric rough path space have been obtained under a different type of assumptions, namely under an infinite radius of convergence condition, see [[CFL+26](#bib.bibx9)]. Similarly, there are LpL^{p}-type results for so-called robust signatures, which were introduced in [[CO22](#bib.bibx14)]. However, compared to our approach in [[BPS25](#bib.bibx7)] they use a Stone–Weierstraß argument for robust signatures, and in [[SA23](#bib.bibx37)] they use a monotone class argument.

## 4. Universal approximation via discrete-time signatures of Brownian motion

In this section, we show that the piecewise linear interpolation of a Brownian motion satisfies the required integrability condition, which yields LpL^{p}-approximation results for measurable and continuous Brownian path functionals by linear functionals of the signature of its piecewise linear interpolation. Moreover, we extend the approximation to solutions of random ordinary differential equations and stochastic differential equations driven by Brownian motion.

Throughout this section, let WW be a dd-dimensional Brownian motion, defined on a probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}), with a filtration (ℱt)t∈[0,T](\mathcal{F}\_{t})\_{t\in[0,T]}, satisfying the usual conditions, i.e., completeness and right-continuity. We consider a nested sequence of partitions πn={tin}i=0Nn\pi\_{n}=\{t\_{i}^{n}\}\_{i=0}^{N\_{n}} of [0,T][0,T] with vanishing mesh size, i.e. πn⊂πn+1\pi\_{n}\subset\pi\_{n+1} and |πn|→0|\pi\_{n}|\to 0 as n→∞n\to\infty, and denote by WπnW^{\pi\_{n}} the piecewise linear interpolation of WW along πn\pi\_{n}.

### 4.1. Approximation of path functionals

We apply the universal approximation result of Theorem [3.5](#S3.Thmtheorem5 "Theorem 3.5 (𝐿^𝑝-convergence). ‣ 3.2. Approximation of 𝐿^𝑝-functionals via signatures ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures") to stochastic path functionals of Brownian motion.
More precisely, we show that measurable and continuous (possibly non-anticipative) functionals of a Brownian path can be approximated in
LpL^{p} by linear functionals of the signature of its piecewise linear interpolation.

###### Corollary 4.1.

Let α∈(13,12)\alpha\in(\frac{1}{3},\frac{1}{2}). Let WW be a dd-dimensional Brownian motion. Fix n∈ℕn\in\mathbb{N} and let WπnW^{\pi\_{n}} denote the piecewise linear interpolation of WW along πn\pi\_{n}. Set W^t:=(t,Wt)\widehat{W}\_{t}:=(t,W\_{t}) and W^tπn:=(t,Wtπn)\widehat{W}^{\pi\_{n}}\_{t}:=(t,W^{\pi\_{n}}\_{t}), t∈[0,T]t\in[0,T].

1. (i)

   Let f​(W^πn)∈Lp​(Ω)f(\widehat{W}^{\pi\_{n}})\in L^{p}(\Omega) with f:𝒞^πn→ℝf\colon\widehat{\mathcal{C}}^{\pi\_{n}}\to\mathbb{R}. Then for every ε>0\varepsilon>0 there exists a linear functional ℓ:T​((ℝd+1))→ℝ\boldsymbol{\ell}\colon T((\mathbb{R}^{d+1}))\to\mathbb{R} of the form 𝕎^Tπn↦∑|I|≤NℓI​⟨eI,𝕎^Tπn⟩\widehat{\mathbb{W}}^{\pi\_{n}}\_{T}\mapsto\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{W}}^{\pi\_{n}}\_{T}\rangle, for some N∈ℕ0N\in\mathbb{N}\_{0} and ℓI∈ℝ\ell\_{I}\in\mathbb{R}, such that

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​[|f​(W^πn)−ℓ​(𝕎^Tπn)|p]<εp.\mathbb{E}[|f(\widehat{W}^{\pi\_{n}})-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{T}^{\pi\_{n}})|^{p}]<\varepsilon^{p}. |  |
2. (ii)

   Let f∈Lp​(ΛTπn)f\in L^{p}(\Lambda\_{T}^{\pi\_{n}}). Then for every ε>0\varepsilon>0 there exists a linear functional ℓ:T​((ℝd+1))→ℝ\boldsymbol{\ell}\colon T((\mathbb{R}^{d+1}))\to\mathbb{R} of the form 𝕎^tπn↦∑|I|≤NℓI​⟨eI,𝕎^tπn⟩\widehat{\mathbb{W}}\_{t}^{\pi\_{n}}\mapsto\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{W}}^{\pi\_{n}}\_{t}\rangle, for some N∈ℕ0N\in\mathbb{N}\_{0} and ℓI∈ℝ\ell\_{I}\in\mathbb{R}, such that

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​[∫0T|f​(W^[0,t]πn)−ℓ​(𝕎^tπn)|p​dt]<εp.\mathbb{E}\Bigl[\int\_{0}^{T}\big|f(\widehat{W}^{\pi\_{n}}\_{[0,t]})-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{t})\big|^{p}\,\mathrm{d}t\Bigr]<\varepsilon^{p}. |  |

###### Proof.

(i) We apply Theorem [3.5](#S3.Thmtheorem5 "Theorem 3.5 (𝐿^𝑝-convergence). ‣ 3.2. Approximation of 𝐿^𝑝-functionals via signatures ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures"). To do so, it remains to verify the exponential moment condition for the law ν:=μW^πn\nu:=\mu\_{\widehat{W}^{\pi\_{n}}}, i.e. 𝔼​[exp⁡(p​β​‖W^πn‖αγ)]<∞\mathbb{E}[\exp(p\beta\|\widehat{W}^{\pi\_{n}}\|\_{\alpha}^{\gamma})]<\infty for γ≥1\gamma\geq 1 and β>0\beta>0. Although for the present corollary it is enough to establish this condition for the fixed partition πn\pi\_{n}, we obtain it from the stronger uniform estimate along the nested sequence (πn)n∈ℕ(\pi\_{n})\_{n\in\mathbb{N}}. To that end, first observe that, as mentioned in the proof of Proposition [3.1](#S3.Thmtheorem1 "Proposition 3.1 (Universal approximation theorem on ℬ_𝜓⁢(𝒞̂^𝜋)). ‣ 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures"), on G1​(ℝd+1)G^{1}(\mathbb{R}^{d+1}) the norm |⋅|ℝd+1|\cdot|\_{\mathbb{R}^{d+1}} is equivalent to the norm ∥⋅∥c​c\|\cdot\|\_{cc} for some constant C1>0C\_{1}>0. Using this, we observe that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.1) |  | ‖W^πn‖α\displaystyle\|\widehat{W}^{\pi\_{n}}\|\_{\alpha} | =sup0≤s<t≤T|W^s,tπn|ℝd+1|t−s|α≤C1​sup0≤s<t≤T‖𝐖^s,tπn‖c​c|t−s|α≤C1​sup0≤s<t≤T‖𝕎^s,tπn,2‖c​c|t−s|α\displaystyle=\sup\_{0\leq s<t\leq T}\frac{|\widehat{W}^{\pi\_{n}}\_{s,t}|\_{\mathbb{R}^{d+1}}}{|t-s|^{\alpha}}\leq C\_{1}\sup\_{0\leq s<t\leq T}\frac{\|\widehat{\mathbf{W}}^{\pi\_{n}}\_{s,t}\|\_{cc}}{|t-s|^{\alpha}}\leq C\_{1}\sup\_{0\leq s<t\leq T}\frac{\|\widehat{\mathbb{W}}^{\pi\_{n},2}\_{s,t}\|\_{cc}}{|t-s|^{\alpha}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C1​supn=1,…,∞sup0≤s<t≤T‖𝕎^s,tπn,2‖c​c|t−s|α=C1​supn=1,…,∞‖𝕎^πn,2‖c​c,α,\displaystyle\leq C\_{1}\sup\_{n=1,\ldots,\infty}\sup\_{0\leq s<t\leq T}\frac{\|\widehat{\mathbb{W}}^{\pi\_{n},2}\_{s,t}\|\_{cc}}{|t-s|^{\alpha}}=C\_{1}\sup\_{n=1,\ldots,\infty}\|\widehat{\mathbb{W}}^{\pi\_{n},2}\|\_{cc,\alpha}, |  |

where we used [[FV10](#bib.bibx25), Theorem 9.5]. Then, by [[FV10](#bib.bibx25), Theorem 13.18] there exists a positive random variable M<∞M<\infty a.s. with Gaussian tails such that for every α∈[0,1/2)\alpha\in[0,1/2) it holds that supn=1,…,∞‖𝕎^πn,2‖c​c,α≤M\sup\_{n=1,\ldots,\infty}\|\widehat{\mathbb{W}}^{\pi\_{n},2}\|\_{cc,\alpha}\leq M. Thus, by [[FV10](#bib.bibx25), Lemma A.17], it can be implied that supn=1,…,∞‖𝕎^πn,2‖c​c,α\sup\_{n=1,\ldots,\infty}\|\widehat{\mathbb{W}}^{\pi\_{n},2}\|\_{cc,\alpha} satisfies the Gaussian integrability, that is, there exists a constant η>0\eta>0 such that the exponential moments are finite for γ=2\gamma=2, i.e.,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[exp⁡(η​(supn=1,…,∞‖𝕎^πn,2‖c​c,α)2)]≤𝔼​[exp⁡(η​M2)]<∞.\mathbb{E}\Bigl[\exp\Bigl(\eta(\sup\_{n=1,\ldots,\infty}\|\widehat{\mathbb{W}}^{\pi\_{n},2}\|\_{cc,\alpha})^{2}\Bigr)\Bigr]\leq\mathbb{E}\Bigl[\exp\Bigl(\eta M^{2}\Bigr)\Bigr]<\infty. |  |

This yields, that the exponential moment condition is fulfilled if we consider the linear interpolation of a Brownian motion, that is,

|  |  |  |  |
| --- | --- | --- | --- |
| (4.2) |  | ∫𝒞^πnψp​dν=𝔼​[exp⁡(β​p​‖W^πn‖α2)]≤𝔼​[exp⁡(C12​β​p​(supn=1,…,∞‖𝕎^πn,2‖c​c,α)2)]<∞,\int\_{\widehat{\mathcal{C}}^{\pi\_{n}}}\psi^{p}\,\mathrm{d}\nu=\mathbb{E}\Bigl[\exp\Bigl(\beta p\|\widehat{W}^{\pi\_{n}}\|\_{\alpha}^{2}\Bigr)\Bigr]\leq\mathbb{E}\Bigl[\exp\Bigl(C\_{1}^{2}\beta p(\sup\_{n=1,\ldots,\infty}\|\widehat{\mathbb{W}}^{\pi\_{n},2}\|\_{cc,\alpha})^{2}\Bigr)\Bigr]<\infty, |  |

by taking β∈(0,ηC12​p],\beta\in(0,\frac{\eta}{C\_{1}^{2}p}], where C1>0C\_{1}>0 as in ([4.1](#S4.E1 "In Proof. ‣ 4.1. Approximation of path functionals ‣ 4. Universal approximation via discrete-time signatures of Brownian motion ‣ Global universality via discrete-time signatures")) and ν=μW^πn\nu=\mu\_{\widehat{W}^{\pi\_{n}}} is the law of W^πn\widehat{W}^{\pi\_{n}}. Further, since f​(W^πn)∈Lp​(Ω)f(\widehat{W}^{\pi\_{n}})\in L^{p}(\Omega),

|  |  |  |
| --- | --- | --- |
|  | ∫𝒞^πn|f|p​dν=𝔼​[|f​(W^πn)|p]<∞,\int\_{\widehat{\mathcal{C}}^{\pi\_{n}}}|f|^{p}\,\mathrm{d}\nu=\mathbb{E}[|f(\widehat{W}^{\pi\_{n}})|^{p}]<\infty, |  |

that is, f∈Lp​(𝒞^πn)f\in L^{p}(\widehat{\mathcal{C}}^{\pi\_{n}}). Hence, Theorem [3.5](#S3.Thmtheorem5 "Theorem 3.5 (𝐿^𝑝-convergence). ‣ 3.2. Approximation of 𝐿^𝑝-functionals via signatures ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures") yields that there exists a functional fℓ∈ℒf\_{\ell}\in\mathcal{L} such that ‖f−fℓ‖Lp​(𝒞^πn)<ε\|f-f\_{\ell}\|\_{L^{p}(\widehat{\mathcal{C}}^{\pi\_{n}})}<\varepsilon,
and, therefore,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|f​(W^πn)−ℓ​(𝕎^Tπn)|p]=‖f−fℓ‖Lp​(𝒞^πn)p<εp.\mathbb{E}[|f(\widehat{W}^{\pi\_{n}})-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{T})|^{p}]=\|f-f\_{\ell}\|^{p}\_{L^{p}(\widehat{\mathcal{C}}^{\pi\_{n}})}<\varepsilon^{p}. |  |

(ii) Let ν:=(d​t⊗μW^πn)∘φ−1\nu:=(dt\otimes\mu\_{\widehat{W}^{\pi\_{n}}})\circ\varphi^{-1} be the push-forward measure on (ΛTπn,ℬ​(ΛTπn))(\Lambda\_{T}^{\pi\_{n}},\mathcal{B}(\Lambda\_{T}^{\pi\_{n}})), where φ​(t,W^πn)=W^[0,t]πn\varphi(t,\widehat{W}^{\pi\_{n}})=\widehat{W}^{\pi\_{n}}\_{[0,t]} is the quotient map as given in ([3.4](#S3.E4 "In 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures")).

Note that, by the continuity of φ\varphi, see e.g. [[BHRS23](#bib.bibx6), Lemma A.1], ν\nu is then a well-defined Borel measure. Moreover, by a change of measure result, we observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΛTπnψp​dν\displaystyle\int\_{\Lambda\_{T}^{\pi\_{n}}}\psi^{p}\,\mathrm{d}\nu | =∫𝒞^πn∫0T(ψ∘φ)​(t,W^πn)​dt​dμW^πn\displaystyle=\int\_{\widehat{\mathcal{C}}^{\pi\_{n}}}\int\_{0}^{T}(\psi\circ\varphi)(t,\widehat{W}^{\pi\_{n}})\,\mathrm{d}t\,\mathrm{d}\mu\_{\widehat{W}^{\pi\_{n}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0Tψ​(W^[0,t]πn)p​dt]\displaystyle=\mathbb{E}\Bigl[\int\_{0}^{T}\psi(\widehat{W}^{\pi\_{n}}\_{[0,t]})^{p}\,\mathrm{d}t\Bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0Texp⁡(p​β​‖W^[0,T]πn,t‖αγ)​dt]\displaystyle=\mathbb{E}\Bigl[\int\_{0}^{T}\exp(p\beta\|\widehat{W}^{\pi\_{n},t}\_{[0,T]}\|\_{\alpha}^{\gamma})\,\mathrm{d}t\Bigr] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.3) |  |  | ≤T​𝔼​[supt∈[0,T]exp⁡(p​β​‖W^[0,T]πn,t‖αγ)]\displaystyle\leq T\mathbb{E}\Bigl[\sup\_{t\in[0,T]}\exp(p\beta\|\widehat{W}^{\pi\_{n},t}\_{[0,T]}\|\_{\alpha}^{\gamma})\Bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =T​𝔼​[exp⁡(p​β​‖W^[0,T]πn‖αγ)]\displaystyle=T\mathbb{E}\Bigl[\exp(p\beta\|\widehat{W}^{\pi\_{n}}\_{[0,T]}\|\_{\alpha}^{\gamma})\Bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤T​𝔼​[exp⁡(C1γ​β​p​(supn=1,…,∞‖𝕎^πn,2‖c​c,α)γ)]<∞,\displaystyle\leq T\mathbb{E}\Bigl[\exp\Bigl(C\_{1}^{\gamma}\beta p(\sup\_{n=1,\ldots,\infty}\|\widehat{\mathbb{W}}^{\pi\_{n},2}\|\_{cc,\alpha})^{\gamma}\Bigr)\Bigr]<\infty, |  |

for β∈(0,ηC1γ​p]\beta\in(0,\frac{\eta}{C\_{1}^{\gamma}p}] and γ=2\gamma=2, where C1>0C\_{1}>0 as in ([4.1](#S4.E1 "In Proof. ‣ 4.1. Approximation of path functionals ‣ 4. Universal approximation via discrete-time signatures of Brownian motion ‣ Global universality via discrete-time signatures")) and where we used

|  |  |  |
| --- | --- | --- |
|  | supt∈[0,T]‖W^[0,T]πn,t‖α=‖W^[0,T]πn‖α.\sup\_{t\in[0,T]}\|\widehat{W}^{\pi\_{n},t}\_{[0,T]}\|\_{\alpha}=\|\widehat{W}^{\pi\_{n}}\_{[0,T]}\|\_{\alpha}. |  |

Thus, the integrability condition given in Theorem [3.5](#S3.Thmtheorem5 "Theorem 3.5 (𝐿^𝑝-convergence). ‣ 3.2. Approximation of 𝐿^𝑝-functionals via signatures ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures") is satisfied, and therefore there exists a functional fℓ∈ℒΛf\_{\ell}\in\mathcal{L}\_{\Lambda} such that

|  |  |  |
| --- | --- | --- |
|  | ‖f−fℓ‖Lp​(ΛTπn)p<εp.\|f-f\_{\ell}\|\_{L^{p}(\Lambda\_{T}^{\pi\_{n}})}^{p}<\varepsilon^{p}. |  |

Thus, there exists a linear functional ℓ\boldsymbol{\ell} on the signature of W^πn\widehat{W}^{\pi\_{n}} such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|f​(W^[0,t]πn)−ℓ​(𝕎^tπn)|p​dt]=∫𝒞^πn∫0T|f−fℓ|p​dt​dμW^πn=‖f−fℓ‖Lp​(ΛTπn)p<εp.\mathbb{E}\Bigl[\int\_{0}^{T}|f(\widehat{W}^{\pi\_{n}}\_{[0,t]})-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t}^{\pi\_{n}})|^{p}\,\mathrm{d}t\Bigr]=\int\_{\widehat{\mathcal{C}}^{\pi\_{n}}}\int\_{0}^{T}|f-f\_{\ell}|^{p}\,\mathrm{d}t\,\mathrm{d}\mu\_{\widehat{W}^{\pi\_{n}}}=\|f-f\_{\ell}\|\_{L^{p}(\Lambda\_{T}^{\pi\_{n}})}^{p}<\varepsilon^{p}. |  |

∎

###### Corollary 4.2.

Let α∈(13,12)\alpha\in(\frac{1}{3},\frac{1}{2}). Let WW be a dd-dimensional Brownian motion and let WπnW^{\pi\_{n}} denote the piecewise linear interpolation of WW along πn\pi\_{n}. Set W^t:=(t,Wt)\widehat{W}\_{t}:=(t,W\_{t}) and W^tπn:=(t,Wtπn)\widehat{W}^{\pi\_{n}}\_{t}:=(t,W^{\pi\_{n}}\_{t}), t∈[0,T]t\in[0,T].

1. (i)

   Let f:C​([0,T];ℝd+1)→ℝf\colon C([0,T];\mathbb{R}^{d+1})\to\mathbb{R} be a measurable and continuous functional. Assume
     
   f​(W^πn)∈Lp​(Ω)f(\widehat{W}^{\pi\_{n}})\in L^{p}(\Omega) for all n∈ℕn\in\mathbb{N} and that (|f​(W^πn)|p)n∈ℕ(|f(\widehat{W}^{\pi\_{n}})|^{p})\_{n\in\mathbb{N}} is uniformly integrable. Then, for every ε>0\varepsilon>0 there exists n0∈ℕn\_{0}\in\mathbb{N} such that for all n≥n0n\geq n\_{0} there exists a linear functional ℓ:T​((ℝd+1))→ℝ\boldsymbol{\ell}\colon T((\mathbb{R}^{d+1}))\to\mathbb{R} of the form 𝕎^Tπn↦∑|I|≤NℓI​⟨eI,𝕎^Tπn⟩\widehat{\mathbb{W}}\_{T}^{\pi\_{n}}\mapsto\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{W}}^{\pi\_{n}}\_{T}\rangle, for some N∈ℕ0N\in\mathbb{N}\_{0} and ℓI∈ℝ\ell\_{I}\in\mathbb{R}, such that

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​[|f​(W^)−ℓ​(𝕎^Tπn)|p]<εp.\mathbb{E}[|f(\widehat{W})-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{T}^{\pi\_{n}})|^{p}]<\varepsilon^{p}. |  |
2. (ii)

   Let f:[0,T]×C​([0,T];ℝd+1)→ℝf\colon[0,T]\times C([0,T];\mathbb{R}^{d+1})\to\mathbb{R} be a measurable, continuous, non-anticipative functional. Assume f​(t,W^πn)∈Lp​([0,T]×Ω)f(t,\widehat{W}^{\pi\_{n}})\in L^{p}([0,T]\times\Omega) for all n∈ℕn\in\mathbb{N} and that (|f​(t,W^πn)|p)n∈ℕ(|f(t,\widehat{W}^{\pi\_{n}})|^{p})\_{n\in\mathbb{N}} is uniformly integrable. Then, for every ε>0\varepsilon>0 there exists n0∈ℕn\_{0}\in\mathbb{N} such that for all n≥n0n\geq n\_{0} there exists a linear functional ℓ:T​((ℝd+1))→ℝ\boldsymbol{\ell}\colon T((\mathbb{R}^{d+1}))\to\mathbb{R} of the form 𝕎^tπn↦∑|I|≤NℓI​⟨eI,𝕎^tπn⟩\widehat{\mathbb{W}}\_{t}^{\pi\_{n}}\mapsto\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{W}}^{\pi\_{n}}\_{t}\rangle, for some N∈ℕ0N\in\mathbb{N}\_{0} and ℓI∈ℝ\ell\_{I}\in\mathbb{R}, such that

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​[∫0T|f​(t,W^)−ℓ​(𝕎^tπn)|p​dt]<εp.\mathbb{E}\Bigl[\int\_{0}^{T}\big|f(t,\widehat{W})-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{t})\big|^{p}\,\mathrm{d}t\Bigr]<\varepsilon^{p}. |  |

###### Proof.

(i) Fix ε>0\varepsilon>0. Since WW has continuous paths and WπnW^{\pi\_{n}} is the piecewise linear interpolation on a partition with |πn|→0|\pi\_{n}|\to 0, we have supt∈[0,T]|W^tπn−W^t|→0\sup\_{t\in[0,T]}|\widehat{W}\_{t}^{\pi\_{n}}-\widehat{W}\_{t}|\to 0 a.s. as n→∞n\to\infty. By continuity of ff, it follows that f​(W^πn)→f​(W^)f(\widehat{W}^{\pi\_{n}})\to f(\widehat{W}) a.s., hence also in probability. Since (|f​(W^πn)|p)n∈ℕ(|f(\widehat{W}^{\pi\_{n}})|^{p})\_{n\in\mathbb{N}} is uniformly integrable and f​(W^πn)→f​(W^)f(\widehat{W}^{\pi\_{n}})\to f(\widehat{W}) in probability, [[Kal02](#bib.bibx28), Proposition 4.12] implies that there exists n0∈ℕn\_{0}\in\mathbb{N} such that, for all n≥n0n\geq n\_{0},

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|f​(W^)−f​(W^πn)|p]<(ε2)p.\mathbb{E}\bigl[|f(\widehat{W})-f(\widehat{W}^{\pi\_{n}})|^{p}\bigr]<\Bigl(\frac{\varepsilon}{2}\Bigr)^{p}. |  |

Fix n≥n0n\geq n\_{0} and let ν:=μW^πn\nu:=\mu\_{\widehat{W}^{\pi\_{n}}} denote the law of W^πn\widehat{W}^{\pi\_{n}} on (𝒞^πn,ℬ​(𝒞^πn))(\widehat{\mathcal{C}}^{\pi\_{n}},\mathcal{B}(\widehat{\mathcal{C}}^{\pi\_{n}})). Then,

|  |  |  |
| --- | --- | --- |
|  | ∫𝒞^πn|f|p​dμW^πn=𝔼​[|f​(W^πn)|p]<∞,\int\_{\widehat{\mathcal{C}}^{\pi\_{n}}}|f|^{p}\,\mathrm{d}\mu\_{\widehat{W}^{\pi\_{n}}}=\mathbb{E}[|f(\widehat{W}^{\pi\_{n}})|^{p}]<\infty, |  |

which yields that f∈Lp​(𝒞^πn)f\in L^{p}(\widehat{\mathcal{C}}^{\pi\_{n}}).
By ([4.2](#S4.E2 "In Proof. ‣ 4.1. Approximation of path functionals ‣ 4. Universal approximation via discrete-time signatures of Brownian motion ‣ Global universality via discrete-time signatures")), the exponential moment condition is satisfied by the law of W^πn\widehat{W}^{\pi\_{n}}. Therefore, Theorem [3.5](#S3.Thmtheorem5 "Theorem 3.5 (𝐿^𝑝-convergence). ‣ 3.2. Approximation of 𝐿^𝑝-functionals via signatures ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures") yields that there exists a functional fℓ∈ℒf\_{\ell}\in\mathcal{L} such that

|  |  |  |
| --- | --- | --- |
|  | ‖f−fℓ‖Lp​(𝒞^πn)p<(ε2)p.\|f-f\_{\ell}\|\_{L^{p}(\widehat{\mathcal{C}}^{\pi\_{n}})}^{p}<\Bigl(\frac{\varepsilon}{2}\Bigr)^{p}. |  |

Moreover, there exists a linear functional ℓ\boldsymbol{\ell} on the signature of W^πn\widehat{W}^{\pi\_{n}} such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|f​(W^πn)−ℓ​(𝕎^Tπn)|p]<(ε2)p,\mathbb{E}[|f(\widehat{W}^{\pi\_{n}})-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{T}^{\pi\_{n}})|^{p}]<\Bigl(\frac{\varepsilon}{2}\Bigr)^{p}, |  |

since

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|f​(W^πn)−ℓ​(𝕎^Tπn)|p]=∫𝒞^πn|f−fℓ|p​dμW^πn=‖f−fℓ‖Lp​(𝒞^πn)p<(ε2)p.\mathbb{E}[|f(\widehat{W}^{\pi\_{n}})-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{T}^{\pi\_{n}})|^{p}]=\int\_{\widehat{\mathcal{C}}^{\pi\_{n}}}|f-f\_{\ell}|^{p}\,\mathrm{d}\mu\_{\widehat{W}^{\pi\_{n}}}=\|f-f\_{\ell}\|\_{L^{p}(\widehat{\mathcal{C}}^{\pi\_{n}})}^{p}<\Bigl(\frac{\varepsilon}{2}\Bigr)^{p}. |  |

Altogether, using the Minkowski inequality, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|f​(W^)−ℓ​(𝕎^Tπn)|p]1p≤𝔼​[|f​(W^)−f​(W^πn)|p]1p+𝔼​[|f​(W^πn)−ℓ​(𝕎^Tπn)|p]1p<ε,\displaystyle\mathbb{E}[|f(\widehat{W})-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{T})|^{p}]^{\frac{1}{p}}\leq\mathbb{E}[|f(\widehat{W})-f(\widehat{W}^{\pi\_{n}})|^{p}]^{\frac{1}{p}}+\mathbb{E}[|f(\widehat{W}^{\pi\_{n}})-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{T})|^{p}]^{\frac{1}{p}}<\varepsilon, |  |

for nn large enough. This yields the claim.

(ii) Fix ε>0\varepsilon>0. As above, supu∈[0,T]|W^uπn−W^u|→0\sup\_{u\in[0,T]}|\widehat{W}\_{u}^{\pi\_{n}}-\widehat{W}\_{u}|\to 0 a.s. as n→∞n\to\infty. By continuity of ff it follows that f​(⋅,W^πn)→f​(⋅,W^)f(\cdot,\widehat{W}^{\pi\_{n}})\to f(\cdot,\widehat{W}) (d​t⊗ℙ)(\mathrm{d}t\otimes\mathbb{P})-a.s., hence in (d​t⊗ℙ)(\mathrm{d}t\otimes\mathbb{P})-measure. Since (|f​(t,W^πn)|p)n∈ℕ(|f(t,\widehat{W}^{\pi\_{n}})|^{p})\_{n\in\mathbb{N}} is uniformly integrable and f​(t,W^πn)→f​(t,W^)f(t,\widehat{W}^{\pi\_{n}})\to f(t,\widehat{W}) in (d​t⊗ℙ)(\mathrm{d}t\otimes\mathbb{P})-measure, by [[Kal02](#bib.bibx28), Proposition 4.12] there exists n0∈ℕn\_{0}\in\mathbb{N} such that for all n≥n0n\geq n\_{0},

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|f​(t,W^)−f​(t,W^πn)|p​𝑑t]<(ε2)p.\mathbb{E}\Bigl[\int\_{0}^{T}|f(t,\widehat{W})-f(t,\widehat{W}^{\pi\_{n}})|^{p}\,dt\Bigr]<\Bigl(\frac{\varepsilon}{2}\Bigr)^{p}. |  |

Fix n≥n0n\geq n\_{0}. Let ν:=(d​t⊗μW^πn)∘φ−1\nu:=(\mathrm{d}t\otimes\mu\_{\widehat{W}^{\pi\_{n}}})\circ\varphi^{-1} be the push-forward measure on (ΛTπn,ℬ​(ΛTπn))(\Lambda\_{T}^{\pi\_{n}},\mathcal{B}(\Lambda\_{T}^{\pi\_{n}})), where φ​(t,W^πn)=W^[0,t]πn\varphi(t,\widehat{W}^{\pi\_{n}})=\widehat{W}^{\pi\_{n}}\_{[0,t]} is the quotient map as given in ([3.4](#S3.E4 "In 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures")).

Since ff is non-anticipative, it factors through φ\varphi, i.e. there exists a measurable F:ΛTπn→ℝF\colon\Lambda\_{T}^{\pi\_{n}}\to\mathbb{R} such that f=F∘φf=F\circ\varphi, then F​(W^[0,t]πn)=f​(t,W^πn)F(\widehat{W}\_{[0,t]}^{\pi\_{n}})=f(t,\widehat{W}^{\pi\_{n}}). Then, we have that F∈Lp​(ΛTπn;ν)F\in L^{p}(\Lambda\_{T}^{\pi\_{n}};\nu), since

|  |  |  |
| --- | --- | --- |
|  | ∫ΛTπn|F|p​dν=∫𝒞^πn∫0T|(F∘φ)​(t,W^πn)|p​dt​dμW^πn=𝔼​[∫0T|f​(t,W^πn)|p​dt]<∞.\int\_{\Lambda\_{T}^{\pi\_{n}}}|F|^{p}\,\mathrm{d}\nu=\int\_{\widehat{\mathcal{C}}^{\pi\_{n}}}\int\_{0}^{T}|(F\circ\varphi)(t,\widehat{W}^{\pi\_{n}})|^{p}\,\mathrm{d}t\,\mathrm{d}\mu\_{\widehat{W}^{\pi\_{n}}}=\mathbb{E}\Bigl[\int\_{0}^{T}|f(t,\widehat{W}^{\pi\_{n}})|^{p}\,\mathrm{d}t\Bigr]<\infty. |  |

Moreover, by ([4.3](#S4.E3 "In Proof. ‣ 4.1. Approximation of path functionals ‣ 4. Universal approximation via discrete-time signatures of Brownian motion ‣ Global universality via discrete-time signatures")) the exponential moment condition is satisfied for ν\nu and therefore by Theorem [3.5](#S3.Thmtheorem5 "Theorem 3.5 (𝐿^𝑝-convergence). ‣ 3.2. Approximation of 𝐿^𝑝-functionals via signatures ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures") there exists a functional fℓ∈ℒΛf\_{\ell}\in\mathcal{L}\_{\Lambda} such that

|  |  |  |
| --- | --- | --- |
|  | ‖F−fℓ‖Lp​(ΛTπn)p<(ε2)p.\|F-f\_{\ell}\|\_{L^{p}(\Lambda\_{T}^{\pi\_{n}})}^{p}<\Bigl(\frac{\varepsilon}{2}\Bigr)^{p}. |  |

Thus, there exists a linear functional ℓ\boldsymbol{\ell} on the signature of W^πn\widehat{W}^{\pi\_{n}} such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|f​(t,W^πn)−ℓ​(𝕎^tπn)|p​dt]<(ε2)p,\mathbb{E}\Bigl[\int\_{0}^{T}|f(t,\widehat{W}^{\pi\_{n}})-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t}^{\pi\_{n}})|^{p}\,\mathrm{d}t\Bigr]<\Bigl(\frac{\varepsilon}{2}\Bigr)^{p}, |  |

since

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T|f​(t,W^πn)−ℓ​(𝕎^tπn)|p​dt]\displaystyle\mathbb{E}\Bigl[\int\_{0}^{T}|f(t,\widehat{W}^{\pi\_{n}})-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t}^{\pi\_{n}})|^{p}\,\mathrm{d}t\Bigr] | =∫𝒞^πn∫0T|(F∘φ−fℓ∘φ)​(t,W^πn)|p​dt​dμW^πn\displaystyle=\int\_{\widehat{\mathcal{C}}^{\pi\_{n}}}\int\_{0}^{T}|(F\circ\varphi-f\_{\ell}\circ\varphi)(t,\widehat{W}^{\pi\_{n}})|^{p}\,\mathrm{d}t\,\mathrm{d}\mu\_{\widehat{W}^{\pi\_{n}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫ΛTπn|F−fℓ|p​dν\displaystyle=\int\_{\Lambda\_{T}^{\pi\_{n}}}|F-f\_{\ell}|^{p}\,\mathrm{d}\nu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =‖F−fℓ‖Lp​(ΛTπn)p<(ε2)p.\displaystyle=\|F-f\_{\ell}\|\_{L^{p}(\Lambda\_{T}^{\pi\_{n}})}^{p}<\Bigl(\frac{\varepsilon}{2}\Bigr)^{p}. |  |

Combining with the first step and using Minkowski’s inequality gives the claim.
∎

### 4.2. Approximation of random ordinary differential equations and stochastic differential equations

In this subsection we show that we can approximate solutions to random ordinary differentiable equations (ODEs) and stochastic differential equations (SDEs) by linear functionals acting on the time-extended signature of piecewise linearly interpolated Brownian motion.

#### 4.2.1. Approximation of random ODEs

Fix n∈ℕn\in\mathbb{N} and consider the random ODE

|  |  |  |  |
| --- | --- | --- | --- |
| (4.4) |  | Ytπn=y0+∫0tμ​(s,Ysπn)​ds+∫0tσ​(s,Ysπn)​dWsπn,t∈[0,T],Y^{\pi\_{n}}\_{t}=y\_{0}+\int\_{0}^{t}\mu(s,Y^{\pi\_{n}}\_{s})\,\mathrm{d}s+\int\_{0}^{t}\sigma(s,Y^{\pi\_{n}}\_{s})\,\mathrm{d}W^{\pi\_{n}}\_{s},\quad t\in[0,T], |  |

where y0∈ℝmy\_{0}\in\mathbb{R}^{m}, μ:[0,T]×ℝm→ℝm\mu\colon[0,T]\times\mathbb{R}^{m}\to\mathbb{R}^{m} and σ:[0,T]×ℝm→ℝm×d\sigma\colon[0,T]\times\mathbb{R}^{m}\to\mathbb{R}^{m\times d} are continuous functions and WπnW^{\pi\_{n}} is the piecewise linear interpolation along πn\pi\_{n}.

###### Theorem 4.3.

Let 2≤p<∞2\leq p<\infty. Fix n∈ℕn\in\mathbb{N}. Suppose that μ,σ\mu,\sigma satisfy

|  |  |  |
| --- | --- | --- |
|  | |μ​(t,x)|+|σ​(t,x)|≤C​(1+|x|),x∈ℝm,|\mu(t,x)|+|\sigma(t,x)|\leq C(1+|x|),\quad x\in\mathbb{R}^{m}, |  |

for some constant C>0C>0 and are globally Lipschitz continuous. Then, for every ε>0\varepsilon>0 there exists
a linear functional ℓ:T​((ℝd+1))→ℝm\boldsymbol{\ell}\colon T((\mathbb{R}^{d+1}))\to\mathbb{R}^{m} of the form 𝕎^tπn↦∑|I|≤NℓI​⟨eI,𝕎^tπn⟩\widehat{\mathbb{W}}\_{t}^{\pi\_{n}}\mapsto\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{W}}^{\pi\_{n}}\_{t}\rangle, for some N∈ℕ0N\in\mathbb{N}\_{0} and ℓI∈ℝm\ell\_{I}\in\mathbb{R}^{m}, such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|Ytπn−ℓ​(𝕎^tπn)|p​𝑑t]<εp,\mathbb{E}\Bigl[\int\_{0}^{T}|Y\_{t}^{\pi\_{n}}-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{t})|^{p}\,dt\Bigr]<\varepsilon^{p}, |  |

###### Proof.

For notational simplicity assume m=1m=1.

We rewrite the ODE ([4.4](#S4.E4 "In 4.2.1. Approximation of random ODEs ‣ 4.2. Approximation of random ordinary differential equations and stochastic differential equations ‣ 4. Universal approximation via discrete-time signatures of Brownian motion ‣ Global universality via discrete-time signatures")) as an ODE driven by the time-extended linear interpolated Brownian motion, by considering σ^:[0,T]×ℝ→ℝ1×(d+1)\widehat{\sigma}\colon[0,T]\times\mathbb{R}\to\mathbb{R}^{1\times(d+1)} with

|  |  |  |
| --- | --- | --- |
|  | σ^=(μ1,σ1,⋯,σd),\widehat{\sigma}=\begin{pmatrix}\mu\_{1},&\sigma\_{1},&\cdots&,\sigma\_{d}\end{pmatrix}, |  |

then

|  |  |  |
| --- | --- | --- |
|  | d​Ytπn=σ^​(t,Ytπn)​d​W^tπ.\,\mathrm{d}Y\_{t}^{\pi\_{n}}=\widehat{\sigma}(t,Y\_{t}^{\pi\_{n}})\,\mathrm{d}\widehat{W}\_{t}^{\pi}. |  |

Let Φ​(W^[0,t]πn):=Ytπn\Phi(\widehat{W}^{\pi\_{n}}\_{[0,t]}):=Y\_{t}^{\pi\_{n}} denote the solution map on stopped paths. Let φ​(t,W^πn)=W^[0,t]πn\varphi(t,\widehat{W}^{\pi\_{n}})=\widehat{W}^{\pi\_{n}}\_{[0,t]} be the quotient map as defined in ([3.4](#S3.E4 "In 3.1. Universal approximation on weighted spaces ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures")) and define the finite Borel measure ν:=(d​t⊗μW^πn)∘φ−1\nu:=(\mathrm{d}t\otimes\mu\_{\widehat{W}^{\pi\_{n}}})\circ\varphi^{-1} on (ΛTπn,ℬ​(ΛTπn))(\Lambda\_{T}^{\pi\_{n}},\mathcal{B}(\Lambda\_{T}^{\pi\_{n}})). Then, by definition of ν\nu,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΛTπn|Φ|p​dν\displaystyle\int\_{\Lambda\_{T}^{\pi\_{n}}}|\Phi|^{p}\,\mathrm{d}\nu | =∫𝒞^πn∫0T|(Φ∘φ)​(t,W^πn)|p​dt​dμW^πn\displaystyle=\int\_{\widehat{\mathcal{C}}^{\pi\_{n}}}\int\_{0}^{T}|(\Phi\circ\varphi)(t,\widehat{W}^{\pi\_{n}})|^{p}\,\mathrm{d}t\,\mathrm{d}\mu\_{\widehat{W}^{\pi\_{n}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0T|Φ​(W^[0,t]πn)|p​dt]\displaystyle=\mathbb{E}\Bigl[\int\_{0}^{T}|\Phi(\widehat{W}^{\pi\_{n}}\_{[0,t]})|^{p}\,\mathrm{d}t\Bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0T|Ytπn|p​dt]\displaystyle=\mathbb{E}\Bigl[\int\_{0}^{T}|Y\_{t}^{\pi\_{n}}|^{p}\,\mathrm{d}t\Bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤T​𝔼​[supt∈[0,T]|Ytπn|p]<∞,\displaystyle\leq T\mathbb{E}\Bigl[\sup\_{t\in[0,T]}|Y\_{t}^{\pi\_{n}}|^{p}\Bigr]<\infty, |  |

where we used that 𝔼​[supt∈[0,T]|Ytπn|p]<∞\mathbb{E}[\sup\_{t\in[0,T]}|Y\_{t}^{\pi\_{n}}|^{p}]<\infty, which follows from global Lipschitz continuity and linear growth of μ,σ\mu,\sigma. Hence Φ∈Lp​(ΛTπn)\Phi\in L^{p}(\Lambda\_{T}^{\pi\_{n}}).

Since the exponential moment condition required in Theorem [3.5](#S3.Thmtheorem5 "Theorem 3.5 (𝐿^𝑝-convergence). ‣ 3.2. Approximation of 𝐿^𝑝-functionals via signatures ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures") (ii) holds on (ΛTπn,ν)(\Lambda\_{T}^{\pi\_{n}},\nu) for linear interpolated Brownian motions, see ([4.3](#S4.E3 "In Proof. ‣ 4.1. Approximation of path functionals ‣ 4. Universal approximation via discrete-time signatures of Brownian motion ‣ Global universality via discrete-time signatures")), Theorem [3.5](#S3.Thmtheorem5 "Theorem 3.5 (𝐿^𝑝-convergence). ‣ 3.2. Approximation of 𝐿^𝑝-functionals via signatures ‣ 3. Global universal approximation ‣ Global universality via discrete-time signatures") (ii) yields fℓ∈ℒΛf\_{\ell}\in\mathcal{L}\_{\Lambda} such that

|  |  |  |
| --- | --- | --- |
|  | ‖Φ−fℓ‖Lp​(ΛTπn)<ε.\|\Phi-f\_{\ell}\|\_{L^{p}(\Lambda\_{T}^{\pi\_{n}})}<\varepsilon. |  |

This ensures that the solution YπnY^{\pi\_{n}} can be approximated by a linear combination of the signature of W^πn\widehat{W}^{\pi\_{n}}, since

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T|Ytπn−ℓ​(𝕎^tπn)|p​dt]\displaystyle\mathbb{E}\Bigl[\int\_{0}^{T}|Y\_{t}^{\pi\_{n}}-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{t})|^{p}\,\mathrm{d}t\Bigr] | =∫𝒞^πn∫0T|(Φ∘φ−fℓ∘φ)​(t,W^πn)|p​dt​dμW^πn\displaystyle=\int\_{\widehat{\mathcal{C}}^{\pi\_{n}}}\int\_{0}^{T}|(\Phi\circ\varphi-f\_{\ell}\circ\varphi)(t,\widehat{W}^{\pi\_{n}})|^{p}\,\mathrm{d}t\,\mathrm{d}\mu\_{\widehat{W}^{\pi\_{n}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫ΛTπn|Φ−fℓ|p​dν\displaystyle=\int\_{\Lambda\_{T}^{\pi\_{n}}}|\Phi-f\_{\ell}|^{p}\,\mathrm{d}\nu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =‖Φ−fℓ‖Lp​(ΛTπn)p<εp.\displaystyle=\|\Phi-f\_{\ell}\|^{p}\_{L^{p}(\Lambda\_{T}^{\pi\_{n}})}<\varepsilon^{p}. |  |

This concludes the proof.
∎

#### 4.2.2. Approximation of SDEs

To approximate solutions of SDEs by linear functionals of signatures of piecewise linear interpolated Brownian paths, we proceed in two steps. First, we show that for any fixed linear functional ℓ\boldsymbol{\ell} the quantity ℓ​(𝕎^πn)\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}) converges to ℓ​(𝕎^)\boldsymbol{\ell}(\widehat{\mathbb{W}}) in LpL^{p}, where 𝕎^\widehat{\mathbb{W}} denotes the (time-extended) Brownian signature and 𝕎^πn\widehat{\mathbb{W}}^{\pi\_{n}} the signature of the time-extended piecewise linear interpolation along πn\pi\_{n}. Second, we combine this stability with a global universal approximation result for Brownian signatures from [[CP25](#bib.bibx15)].

We briefly recall the notion of the Brownian signature. Let WW be a dd-dimensional Brownian motion. Its Stratonovich lift to a geometric rough path is given by

|  |  |  |
| --- | --- | --- |
|  | 𝐖t=(1,Wt,∫0tWs⊗∘dWs),t∈[0,T],\mathbf{W}\_{t}=\Bigl(1,W\_{t},\int\_{0}^{t}W\_{s}\otimes\circ\mathrm{d}W\_{s}\Bigr),\quad t\in[0,T], |  |

where the stochastic integral ∫0tWs⊗∘dWs\int\_{0}^{t}W\_{s}\otimes\circ\,\mathrm{d}W\_{s} is defined as a classical Stratonovich integral. It is well known that 𝐖t\mathbf{W}\_{t} takes values in G2​(ℝd)G^{2}(\mathbb{R}^{d}) and is almost surely a geometric α\alpha-Hölder rough path for any α∈(13,12)\alpha\in(\frac{1}{3},\frac{1}{2}). We denote by 𝐖^\widehat{\mathbf{W}} the time-extended Stratonovich-enhanced Brownian rough path and by 𝕎^\widehat{\mathbb{W}} its associated signature, which coincides with iterated Stratonovich integrals. We refer to 𝐖^\widehat{\mathbf{W}} and 𝕎^\widehat{\mathbb{W}} as the (time-extended) Brownian rough path and (time-extended) Brownian signature, respectively.

###### Lemma 4.4.

Let α∈(13,12)\alpha\in(\frac{1}{3},\frac{1}{2}) and p>1p>1. Let WW be a dd-dimensional Brownian motion, W^=(⋅,W)\widehat{W}=(\cdot,W) be the time-extended Brownian motion and 𝕎^\widehat{\mathbb{W}} be the corresponding time-extended Brownian signature. Let 𝕎^πn\widehat{\mathbb{W}}^{\pi\_{n}} be the signature of the piecewise linear interpolated Brownian motion W^πn∈𝒞^πn\widehat{W}^{\pi\_{n}}\in\widehat{\mathcal{C}}^{\pi\_{n}} along πn\pi\_{n}. Then,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|ℓ​(𝕎^t)−ℓ​(𝕎^tπn)|p​dt]1p→0,n→∞,\mathbb{E}\Bigl[\int\_{0}^{T}|\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t}^{\pi\_{n}})|^{p}\,\mathrm{d}t\Bigr]^{\frac{1}{p}}\to 0,\qquad n\to\infty, |  |

with ℓ=∑|I|≤NℓI​eI\boldsymbol{\ell}=\sum\_{|I|\leq N}\ell\_{I}e\_{I}, ℓI∈ℝ\ell\_{I}\in\mathbb{R}.

###### Proof.

Let I∈{0,…,d}NI\in\{0,\ldots,d\}^{N} be a multi-index of length N≥0N\geq 0. Then, using the ball-box estimate [[FV10](#bib.bibx25), Proposition 7.49, Proposition 7.45] and Theorem 9.5 in [[FV10](#bib.bibx25)], we have for some constant C1≥1C\_{1}\geq 1 and CN,α>0C\_{N,\alpha}>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |⟨eI,𝕎^t⟩−⟨eI,𝕎^tπn⟩|\displaystyle|\langle e\_{I},\widehat{\mathbb{W}}\_{t}\rangle-\langle e\_{I},\widehat{\mathbb{W}}^{\pi\_{n}}\_{t}\rangle| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖𝕎^tN−𝕎^tπn,N‖TN​(ℝd+1)\displaystyle\leq\|\widehat{\mathbb{W}}^{N}\_{t}-\widehat{\mathbb{W}}^{\pi\_{n},N}\_{t}\|\_{T^{N}(\mathbb{R}^{d+1})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C1​max⁡{dc​c​(𝕎^tN,𝕎^tπn,N)​max⁡{1,‖𝕎^tN‖c​cN−1},dc​c​(𝕎^tN,𝕎^tπn,N)N}\displaystyle\leq C\_{1}\max\{d\_{cc}(\widehat{\mathbb{W}}\_{t}^{N},\widehat{\mathbb{W}}\_{t}^{\pi\_{n},N})\max\{1,\|\widehat{\mathbb{W}}\_{t}^{N}\|^{N-1}\_{cc}\},d\_{cc}(\widehat{\mathbb{W}}\_{t}^{N},\widehat{\mathbb{W}}\_{t}^{\pi\_{n},N})^{N}\} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.5) |  |  | ≤C1max{Tαsup0≤s<t≤Tdc​c​(𝕎^s,tN,𝕎^s,tπn,N)|t−s|αmax{1,Tα​(N−1)(sup0≤s<t≤T‖𝕎^s,tN‖c​c|t−s|α)N−1},\displaystyle\leq C\_{1}\max\Bigl\{T^{\alpha}\sup\_{0\leq s<t\leq T}\frac{d\_{cc}(\widehat{\mathbb{W}}\_{s,t}^{N},\widehat{\mathbb{W}}\_{s,t}^{\pi\_{n},N})}{|t-s|^{\alpha}}\max\Bigl\{1,T^{\alpha(N-1)}\Bigl(\sup\_{0\leq s<t\leq T}\frac{\|\widehat{\mathbb{W}}\_{s,t}^{N}\|\_{cc}}{|t-s|^{\alpha}}\Bigr)^{N-1}\Bigr\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Tα​N(sup0≤s<t≤Tdc​c​(𝕎^s,tN,𝕎^s,tπn,N)|t−s|α)N}\displaystyle\qquad\qquad T^{\alpha N}\Bigl(\sup\_{0\leq s<t\leq T}\frac{d\_{cc}(\widehat{\mathbb{W}}\_{s,t}^{N},\widehat{\mathbb{W}}\_{s,t}^{\pi\_{n},N})}{|t-s|^{\alpha}}\Bigr)^{N}\Bigr\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C1max{CN,αTαsup0≤s<t≤Tdc​c​(𝐖^s,t,𝕎^s,tπn,2)|t−s|αmax{1,Tα​(N−1)CN,αN−1∥𝐖^∥c​c,αN−1},\displaystyle\leq C\_{1}\max\Bigl\{C\_{N,\alpha}T^{\alpha}\sup\_{0\leq s<t\leq T}\frac{d\_{cc}(\widehat{\mathbf{W}}\_{s,t},\widehat{\mathbb{W}}\_{s,t}^{\pi\_{n},2})}{|t-s|^{\alpha}}\max\Bigl\{1,T^{\alpha(N-1)}C\_{N,\alpha}^{N-1}\|\widehat{\mathbf{W}}\|\_{cc,\alpha}^{N-1}\Bigr\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | CN,αNTα​N(sup0≤s<t≤Tdc​c​(𝐖^s,t,𝕎^s,tπn,2)|t−s|α)N}.\displaystyle\qquad\qquad C\_{N,\alpha}^{N}T^{\alpha N}\Bigl(\sup\_{0\leq s<t\leq T}\frac{d\_{cc}(\widehat{\mathbf{W}}\_{s,t},\widehat{\mathbb{W}}\_{s,t}^{\pi\_{n},2})}{|t-s|^{\alpha}}\Bigr)^{N}\Bigr\}. |  |

Now, let ℓ=∑|I|≤NℓI​eI\boldsymbol{\ell}=\sum\_{|I|\leq N}\ell\_{I}e\_{I} for some N∈ℕ0N\in\mathbb{N}\_{0} and ℓI∈ℝ\ell\_{I}\in\mathbb{R}. Denote by ℓ~:=max⁡{|ℓI|:ℓI∈ℝ,I∈{0,…,d}N,N∈ℕ0}\tilde{\ell}:=\max\{|\ell\_{I}|:\ell\_{I}\in\mathbb{R},I\in\{0,\ldots,d\}^{N},N\in\mathbb{N}\_{0}\} and let D=∑n=0N(d+1)nD=\sum\_{n=0}^{N}(d+1)^{n} be the number of multi-indices contained in ∑|I|≤NeI\sum\_{|I|\leq N}e\_{I}.

Using that x↦|x|px\mapsto|x|^{p} is convex, we have for t∈[0,T]t\in[0,T]

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|ℓ​(𝕎^t)−ℓ​(𝕎^tπn)|p]\displaystyle\mathbb{E}\Bigl[\bigl|\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{t})\bigr|^{p}\Bigr] | =𝔼​[|∑|I|≤NℓI​(⟨eI,𝕎^t⟩−⟨eI,𝕎^tπn⟩)|p]\displaystyle=\mathbb{E}\Bigl[\Bigl|\sum\_{|I|\leq N}\ell\_{I}\bigl(\langle e\_{I},\widehat{\mathbb{W}}\_{t}\rangle-\langle e\_{I},\widehat{\mathbb{W}}^{\pi\_{n}}\_{t}\rangle\bigr)\Bigr|^{p}\Bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ℓ~p​Dp−1​∑|I|≤N𝔼​[|⟨eI,𝕎^t⟩−⟨eI,𝕎^tπn⟩|p].\displaystyle\leq\tilde{\ell}^{p}D^{p-1}\sum\_{|I|\leq N}\mathbb{E}\Bigl[\Bigl|\langle e\_{I},\widehat{\mathbb{W}}\_{t}\rangle-\langle e\_{I},\widehat{\mathbb{W}}^{\pi\_{n}}\_{t}\rangle\Bigr|^{p}\Bigr]. |  |

Moreover, by the preceding estimate on each coordinate, see ([4.2.2](#S4.Ex44 "Proof. ‣ 4.2.2. Approximation of SDEs ‣ 4.2. Approximation of random ordinary differential equations and stochastic differential equations ‣ 4. Universal approximation via discrete-time signatures of Brownian motion ‣ Global universality via discrete-time signatures")), for every multi-index II we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |⟨eI,𝕎^t⟩−⟨eI,𝕎^tπn⟩|≤\displaystyle\Bigl|\langle e\_{I},\widehat{\mathbb{W}}\_{t}\rangle-\langle e\_{I},\widehat{\mathbb{W}}^{\pi\_{n}}\_{t}\rangle\Bigr|\leq | C|I|,α,T​(1+Tα​(|I|−1)​C|I|,α|I|−1​‖𝐖^‖c​c,α|I|−1)​dc​c,α​(𝐖^,𝕎^πn,2)\displaystyle C\_{|I|,\alpha,T}\Bigl(1+T^{\alpha(|I|-1)}C\_{|I|,\alpha}^{|I|-1}\|\widehat{\mathbf{W}}\|\_{cc,\alpha}^{|I|-1}\Bigr)\,d\_{cc,\alpha}\!\bigl(\widehat{\mathbf{W}},\widehat{\mathbb{W}}^{\pi\_{n},2}\bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(C|I|,α,T)|I|​dc​c,α​(𝐖^,𝕎^πn,2)|I|,\displaystyle\quad+(C\_{|I|,\alpha,T})^{|I|}\,d\_{cc,\alpha}\!\bigl(\widehat{\mathbf{W}},\widehat{\mathbb{W}}^{\pi\_{n},2}\bigr)^{|I|}, |  |

where we set C|I|,α,T:=C1​C|I|,α​TαC\_{|I|,\alpha,T}:=C\_{1}C\_{|I|,\alpha}T^{\alpha}. Hence, for t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|ℓ​(𝕎^t)−ℓ​(𝕎^tπn)|p]\displaystyle\mathbb{E}\Bigl[\bigl|\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{t})\bigr|^{p}\Bigr] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2p−1ℓ~pDp−1∑|I|≤N((C|I|,α,T)p𝔼[(1+Tα​(|I|−1)C|I|,α|I|−1∥𝐖^∥c​c,α|I|−1)2​p]12𝔼[dc​c,α(𝐖^,𝕎^πn,2)2​p]12\displaystyle\leq 2^{p-1}\tilde{\ell}^{p}D^{p-1}\sum\_{|I|\leq N}\Bigl((C\_{|I|,\alpha,T})^{p}\,\mathbb{E}\Bigl[\Bigl(1+T^{\alpha(|I|-1)}C\_{|I|,\alpha}^{|I|-1}\|\widehat{\mathbf{W}}\|\_{cc,\alpha}^{|I|-1}\Bigr)^{2p}\Bigr]^{\frac{1}{2}}\mathbb{E}\Bigl[d\_{cc,\alpha}\!\bigl(\widehat{\mathbf{W}},\widehat{\mathbb{W}}^{\pi\_{n},2}\bigr)^{2p}\Bigr]^{\frac{1}{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | +(C|I|,α,T)|I|​p𝔼[dc​c,α(𝐖^,𝕎^πn,2)|I|​p])\displaystyle\qquad\qquad\qquad+(C\_{|I|,\alpha,T})^{|I|p}\,\mathbb{E}\Bigl[d\_{cc,\alpha}\!\bigl(\widehat{\mathbf{W}},\widehat{\mathbb{W}}^{\pi\_{n},2}\bigr)^{|I|p}\Bigr]\Bigr) |  |
|  |  |  |
| --- | --- | --- |
|  | =:Cn.\displaystyle=:C\_{n}. |  |

By Corollary 13.21 in [[FV10](#bib.bibx25)], we have

|  |  |  |
| --- | --- | --- |
|  | dc​c,α​(𝐖^,𝕎^πn,2)=sup0≤s<t≤Tdc​c​(𝐖^s,t,𝕎^s,tπn,2)|t−s|α→0,d\_{cc,\alpha}(\widehat{\mathbf{W}},\widehat{\mathbb{W}}^{\pi\_{n},2})=\sup\_{0\leq s<t\leq T}\frac{d\_{cc}(\widehat{\mathbf{W}}\_{s,t},\widehat{\mathbb{W}}\_{s,t}^{\pi\_{n},2})}{|t-s|^{\alpha}}\to 0, |  |

as n→∞n\to\infty in LqL^{q} for every q∈[1,∞)q\in[1,\infty). Moreover,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(1+Tα​(|I|−1)​C|I|,α|I|−1​‖𝐖^‖c​c,α|I|−1)2​p]≤22​p−1+22​p−1​Tα​p​(|I|−1)​C|I|,α2​(|I|−1)​𝔼​[‖𝐖^‖c​c,α2​p​(|I|−1)]<∞,\displaystyle\mathbb{E}\Bigl[(1+T^{\alpha(|I|-1)}C\_{|I|,\alpha}^{|I|-1}\|\widehat{\mathbf{W}}\|\_{cc,\alpha}^{|I|-1})^{2p}\Bigr]\leq 2^{2p-1}+2^{2p-1}T^{\alpha p(|I|-1)}C\_{|I|,\alpha}^{2(|I|-1)}\mathbb{E}[\|\widehat{\mathbf{W}}\|\_{cc,\alpha}^{2p(|I|-1)}]<\infty, |  |

since ‖𝐖^‖c​c,α\|\widehat{\mathbf{W}}\|\_{cc,\alpha} has finite moments, see [[FH20](#bib.bibx22), Proposition 3.4] and [[FV10](#bib.bibx25), Lemma A.17]. Therefore, we obtain Cn→0C\_{n}\to 0 as n→∞.n\to\infty.

Since CnC\_{n} does not depend on tt, the above estimate holds uniformly for all t∈[0,T]t\in[0,T] and, in turn by Fubini’s theorem, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|ℓ​(𝕎^t)−ℓ​(𝕎^tπn)|p​dt]=∫0T𝔼​[|ℓ​(𝕎^t)−ℓ​(𝕎^tπn)|p]​dt≤∫0TCn​dt=T​Cn→0,\mathbb{E}\Bigl[\int\_{0}^{T}|\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{t})|^{p}\,\mathrm{d}t\Bigr]=\int\_{0}^{T}\mathbb{E}\Bigl[|\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{t})|^{p}\Bigr]\,\mathrm{d}t\leq\int\_{0}^{T}C\_{n}\,\mathrm{d}t=TC\_{n}\to 0, |  |

as n→∞.n\to\infty.
∎

###### Remark 4.5.

Our result establishes that linear functionals of the Brownian signature can be approximated by the same linear functionals evaluated on the signatures of linearly interpolated Brownian paths. Together with Corollary 4.3 in [[CP25](#bib.bibx15)], this implies that LpL^{p}-functionals on Brownian rough paths can be approximated by linear combinations of discrete-time signatures.

Using Lemma [4.4](#S4.Thmtheorem4 "Lemma 4.4. ‣ 4.2.2. Approximation of SDEs ‣ 4.2. Approximation of random ordinary differential equations and stochastic differential equations ‣ 4. Universal approximation via discrete-time signatures of Brownian motion ‣ Global universality via discrete-time signatures"), we can conclude the approximation of solutions to stochastic differential equations by linear functionals on the linearly interpolated Brownian signature.

###### Corollary 4.6.

Let 2≤p<∞2\leq p<\infty. Consider the stochastic differential equation

|  |  |  |  |
| --- | --- | --- | --- |
| (4.6) |  | Yt=y0+∫0tμ​(s,Ys)​ds+∫0tσ​(s,Ys)​dWs,t∈[0,T],Y\_{t}=y\_{0}+\int\_{0}^{t}\mu(s,Y\_{s})\,\mathrm{d}s+\int\_{0}^{t}\sigma(s,Y\_{s})\,\mathrm{d}W\_{s},\quad t\in[0,T], |  |

where y0∈ℝmy\_{0}\in\mathbb{R}^{m}, μ:[0,T]×ℝm→ℝm\mu\colon[0,T]\times\mathbb{R}^{m}\to\mathbb{R}^{m} and σ:[0,T]×ℝm→ℝm×d\sigma\colon[0,T]\times\mathbb{R}^{m}\to\mathbb{R}^{m\times d} are continuous functions, and ∫0tσ​(s,Ys)​dWs\int\_{0}^{t}\sigma(s,Y\_{s})\,\mathrm{d}W\_{s} is defined as an Itô integral. Suppose there exists a unique (strong) solution YY to the SDE ([4.6](#S4.E6 "In Corollary 4.6. ‣ 4.2.2. Approximation of SDEs ‣ 4.2. Approximation of random ordinary differential equations and stochastic differential equations ‣ 4. Universal approximation via discrete-time signatures of Brownian motion ‣ Global universality via discrete-time signatures")) and that μ,σ\mu,\sigma satisfy the linear growth condition

|  |  |  |
| --- | --- | --- |
|  | |μ​(t,x)|+|σ​(t,x)|≤C​(1+|x|),x∈ℝm,|\mu(t,x)|+|\sigma(t,x)|\leq C(1+|x|),\quad x\in\mathbb{R}^{m}, |  |

for some constant C>0C>0.

Then, for every ε>0\varepsilon>0 there exists a linear function ℓ:T​((ℝd+1))→ℝm\boldsymbol{\ell}\colon T((\mathbb{R}^{d+1}))\to\mathbb{R}^{m} of the form 𝕎^tπn↦ℓ​(𝕎^tπn):=∑|I|≤NℓI​⟨eI,𝕎^tπn⟩\widehat{\mathbb{W}}^{\pi\_{n}}\_{t}\mapsto\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{t}):=\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{W}}^{\pi\_{n}}\_{t}\rangle, for some N∈ℕ0N\in\mathbb{N}\_{0} and ℓI∈ℝm\ell\_{I}\in\mathbb{R}^{m}, and n0∈ℕn\_{0}\in\mathbb{N} such that for all n≥n0n\geq n\_{0},

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|Yt−ℓ​(𝕎^tπn)|p​dt]<εp.\mathbb{E}\Bigl[\int\_{0}^{T}|Y\_{t}-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{t})|^{p}\,\mathrm{d}t\Bigr]<\varepsilon^{p}. |  |

###### Proof.

By Proposition 4.4 in [[CP25](#bib.bibx15)] we know that we can approximate solutions to SDEs driven by Brownian motions by some linear functional of the Brownian signature, i.e., for every ε>0\varepsilon>0 there exists some linear functional ℓ\boldsymbol{\ell}, such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|Yt−ℓ​(𝕎^t)|p​dt]1p<ε.\mathbb{E}\Bigl[\int\_{0}^{T}|Y\_{t}-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})|^{p}\,\mathrm{d}t\Bigr]^{\frac{1}{p}}<\varepsilon. |  |

Moreover, by Lemma [4.4](#S4.Thmtheorem4 "Lemma 4.4. ‣ 4.2.2. Approximation of SDEs ‣ 4.2. Approximation of random ordinary differential equations and stochastic differential equations ‣ 4. Universal approximation via discrete-time signatures of Brownian motion ‣ Global universality via discrete-time signatures"), for this fixed ℓ\boldsymbol{\ell} we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|ℓ​(𝕎^t)−ℓ​(𝕎^tπn)|p​dt]1/p→0,n→∞,\mathbb{E}\Bigl[\int\_{0}^{T}|\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{t})|^{p}\,\mathrm{d}t\Bigr]^{1/p}\to 0,\qquad n\to\infty, |  |

so there exists n0∈ℕn\_{0}\in\mathbb{N} such that for all n≥n0n\geq n\_{0},

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|ℓ​(𝕎^t)−ℓ​(𝕎^tπn)|p​dt]1/p<ε/2.\mathbb{E}\Bigl[\int\_{0}^{T}|\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{t})|^{p}\,\mathrm{d}t\Bigr]^{1/p}<\varepsilon/2. |  |

Therefore, by Minkowski’s inequality for all n≥n0n\geq n\_{0},

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|Yt−ℓ​(𝕎^tπn)|p​dt]1/p≤𝔼​[∫0T|Yt−ℓ​(𝕎^t)|p​dt]1/p+𝔼​[∫0T|ℓ​(𝕎^t)−ℓ​(𝕎^tπn)|p​dt]1/p<ε,\mathbb{E}\Bigl[\int\_{0}^{T}|Y\_{t}-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{t})|^{p}\,\mathrm{d}t\Bigr]^{1/p}\leq\mathbb{E}\Bigl[\int\_{0}^{T}|Y\_{t}-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})|^{p}\,\mathrm{d}t\Bigr]^{1/p}+\mathbb{E}\Bigl[\int\_{0}^{T}|\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})-\boldsymbol{\ell}(\widehat{\mathbb{W}}^{\pi\_{n}}\_{t})|^{p}\,\mathrm{d}t\Bigr]^{1/p}<\varepsilon, |  |

which implies the claim.
∎

## References

* [AN21]

  Takanori Adachi and Yusuke Naritomi, *Discrete signature and its
  application to finance*, arXiv preprint arXiv:2112.09342 (2021).
* [BB11]

  Haim Brezis and Haim Brézis, *Functional analysis, Sobolev spaces
  and partial differential equations*, vol. 2, Springer, 2011.
* [BBH+25]

  Peter Bank, Christian Bayer, Paul P. Hager, Sebastian Riedel, and Tobias Nauen,
  *Stochastic control with signatures*, SIAM Journal on Control and
  Optimization 63 (2025), no. 5, 3189–3218.
* [BdRHO25]

  Christian Bayer, Goncalo dos Reis, Blanka Horvath, and Harald Oberhauser,
  *Signature Methods in Finance*, first ed., Springer Finance,
  Springer Cham, 2025.
* [BGLY16]

  Horatio Boedihardjo, Xi Geng, Terry Lyons, and Danyu Yang, *The signature
  of a rough path: uniqueness*, Adv. Math. 293 (2016), 720–737.
* [BHRS23]

  Christian Bayer, Paul P. Hager, Sebastian Riedel, and John Schoenmakers,
  *Optimal stopping with signatures*, The Annals of Applied Probability
  33 (2023), no. 1, 238–273.
* [BPS25]

  Christian Bayer, Luca Pelizzari, and John Schoenmakers, *Primal and dual
  optimal stopping with signatures*, Finance Stoch. 29 (2025), no. 4,
  981–1014.
* [CF13]

  Rama Cont and David-Antoine Fournié, *Functional Itô calculus and
  stochastic integral representation of martingales*, The Annals of Probability
  41 (2013), no. 1.
* [CFL+26]

  Ilya Chevyrev, Emilio Ferrucci, Darrick Lee, Terry Lyons, Harald Oberhauser,
  and Nikolas Tapia, *Orthogonal polynomials on path-space*, arXiv
  preprint arXiv:2602.18808 (2026).
* [CGG+21]

  Christa Cuchiero, Lukas Gonon, Lyudmila Grigoryeva, Juan-Pablo Ortega, and
  Josef Teichmann, *Discrete-time signatures and randomness in reservoir
  computing*, IEEE Transactions on Neural Networks and Learning Systems
  33 (2021), no. 11, 6321–6330.
* [Che54]

  Kuo-Tsai Chen, *Iterated integrals and exponential homomorphisms*, Proc.
  London Math. Soc. (3) 4 (1954), 502–512.
* [CM25]

  Christa Cuchiero and Janka Möller, *Signature methods in stochastic
  portfolio theory*, SIAM Journal on Financial Mathematics 16 (2025),
  no. 4, 1239–1303.
* [CNO20]

  Ilya Chevyrev, Vidit Nanda, and Harald Oberhauser, *Persistence Paths
  and Signature Features in Topological Data Analysis*, IEEE
  Transactions on Pattern Analysis & Machine Intelligence 42 (2020),
  no. 01, 192–202.
* [CO22]

  Ilya Chevyrev and Harald Oberhauser, *Signature moments to characterize
  laws of stochastic processes*, Journal of Machine Learning Research
  23 (2022), no. 176, 1–42.
* [CP25]

  Mihriban Ceylan and David J. Prömel, *Global universal approximation
  with Brownian signatures*, arXiv preprint arXiv:2512.16396 (2025).
* [CPSF25]

  Christa Cuchiero, Francesca Primavera, and Sara Svaluto-Ferro, *Universal
  approximation theorems for continuous functions of càdlàg paths and
  Lévy-type signature models*, Finance Stoch. 29 (2025), no. 2,
  289–342.
* [CST26]

  Christa Cuchiero, Philipp Schmocker, and Josef Teichmann, *Global
  universal approximation of functional input maps on weighted spaces*,
  Constructive Approximation (2026), 1–76.
* [DMP03]

  Zdzisław Denkowski, Stanislaw Migórski, and Nikolas Papageorgiou, *An
  introduction to nonlinear analysis: Theory*, SpringerLink Bücher, Boston,
  MA, 2003 (eng).
* [DT10]

  Philipp Dörsek and Josef Teichmann, *A semigroup point of view on
  splitting schemes for stochastic (partial) differential equations*, arXiv
  preprint arXiv:1011.2651 (2010).
* [Dup19]

  Bruno Dupire, *Functional Itô calculus*, Quant. Finance 19
  (2019), no. 5, 721–729.
* [Fer21]

  Adeline Fermanian, *Embedding and learning with signatures*, Computational
  Statistics & Data Analysis 157 (2021), 107148.
* [FH20]

  Peter K. Friz and Martin Hairer, *A course on rough paths: with an
  introduction to regularity structures*, second edition ed., Universitext,
  Cham, Switzerland, 2020 (eng).
* [Fol99]

  Gerald B. Folland, *Real analysis: modern techniques and their
  applications*, 2. ed. ed., A Wiley-Interscience publication, New York
  Weinheim [u.a., 1999 (eng).
* [Fri82]

  Avner Friedman, *Foundations of modern analysis*, Courier Corporation,
  1982.
* [FV10]

  Peter K. Friz and Nicolas B. Victoir, *Multidimensional stochastic
  processes as rough paths: theory and applications*, Cambridge studies in
  advanced mathematics; 120, Cambridge, 2010 (eng).
* [Gra13]

  Benjamin Graham, *Sparse arrays of signatures for online character
  recognition*, arXiv preprint arXiv:1308.0371 (2013).
* [HL10]

  Ben Hambly and Terry Lyons, *Uniqueness for the signature of a path of
  bounded variation and the reduced path group*, Ann. of Math. (2) 171
  (2010), no. 1, 109–167.
* [Kal02]

  Olav Kallenberg, *Foundations of modern probability*, 2. ed. ed.,
  Probability and its applications, New York, NY Berlin Heidelberg [u.a., 2002
  (eng).
* [KBPA+19]

  Patrick Kidger, Patric Bonnier, Imanol Perez Arribas, Cristopher Salvi, and
  Terry Lyons, *Deep signature transforms*, 33rd Conference on Neural
  Information Processing Systems (NeurIPS 2019), 32 (2019).
* [KO19]

  Franz J. Király and Harald Oberhauser, *Kernels for sequentially
  ordered data*, J. Mach. Learn. Res. 20 (2019), Paper No. 31, 45.
* [LG94]

  Jean-François Le Gall, *A path-valued Markov process and its
  connections with partial differential equations*, First European Congress of
  Mathematics Paris, July 6–10, 1992: Vol. II: Invited Lectures (Part 2),
  Springer, 1994, pp. 185–212.
* [LLN13]

  Daniel Levin, Terry Lyons, and Hao Ni, *Learning from the past, predicting
  the statistics for the future, learning an evolving system*, arXiv preprint
  arXiv:1309.0260 (2013).
* [LNPA19]

  Terry Lyons, Sina Nejad, and Imanol Perez Arribas, *Numerical method for
  model-free pricing of exotic derivatives in discrete time using rough path
  signatures*, Appl. Math. Finance 26 (2019), no. 6, 583–597.
* [Lyo07]

  Terry J Lyons, *Differential equations driven by rough paths: École
  d’été de probabilités de saint-flour xxxiv-2004*, no. 1908,
  Springer, 2007.
* [ML25]

  Andrew McLeod and Terry Lyons, *Signature methods in machine learning*,
  EMS Surv. Math. Sci., 2025.
* [RG18]

  Jeremy Reizenstein and Benjamin Graham, *The iisignature library:
  efficient calculation of iterated-integral signatures and log signatures*,
  arXiv preprint arXiv:1802.08252 (2018).
* [SA23]

  A. Schell and R. Alaifari, *Nonparametric Regression of Stochastic
  Processes via Signatures*, ETH Zurich, Research Report No. 2023-45
  (2023).

BETA