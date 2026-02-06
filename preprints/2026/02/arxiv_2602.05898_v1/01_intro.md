---
authors:
- Mihriban Ceylan
- Anna P. Kwossek
- David J. Prömel
doc_id: arxiv:2602.05898v1
family_id: arxiv:2602.05898
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Universal approximation with signatures of non-geometric rough paths
url_abs: http://arxiv.org/abs/2602.05898v1
url_html: https://arxiv.org/html/2602.05898v1
venue: arXiv q-fin
version: 1
year: 2026
---


Mihriban Ceylan
Mihriban Ceylan, University of Mannheim, Germany
[mihriban.ceylan@uni-mannheim.de](mailto:mihriban.ceylan@uni-mannheim.de)
, 
Anna P. Kwossek
Anna P. Kwossek, University of Vienna, Austria
[anna.paula.kwossek@univie.ac.at](mailto:anna.paula.kwossek@univie.ac.at)
 and 
David J. Prömel
David J. Prömel, University of Mannheim, Germany
[proemel@uni-mannheim.de](mailto:proemel@uni-mannheim.de)

###### Abstract.

We establish a universal approximation theorem for signatures of rough paths that are not necessarily weakly geometric. By extending the path with time and its rough path bracket terms, we prove that linear functionals of the signature of the resulting rough paths approximate continuous functionals on rough path spaces uniformly on compact sets. Moreover, we construct the signature of a path extended by its pathwise quadratic variation terms based on general pathwise stochastic integration à la Föllmer, in particular, allowing for pathwise Itô, Stratonovich, and backward Itô integration. In a probabilistic setting, we obtain a universal approximation result for linear functionals of the signature of continuous semimartingales extended by the quadratic variation terms, defined via stochastic Itô integration. Numerical examples illustrate the use of signatures when the path is extended by time and quadratic variation in the context of model calibration and option pricing in mathematical finance.

Key words: signature; universal approximation; rough path; pathwise stochastic integration; semimartingale; model calibration; pricing of financial derivatives.

MSC 2020 Classification: Primary: 60L10; Secondary: 60H05; 60G17; 91G60.

## 1. Introduction

Many quantities that occur from real-world dynamics or complex mathematical models are analytically intractable, making it practically unavoidable to approximate them by simpler, numerically tractable ones that can be fitted to data. In this regard, it is very relevant, for example, for machine learning tasks, quantitative finance, and data analysis in general, to “faithfully” summarize time series data in an efficient and computable way. In response, in recent years, an increasingly active strand of research has been concerned with developing and applying data-driven methods based on the *signature of a path*, which turns out to be a very suitable feature map for streamed data.

In mathematical finance, the applications are manifold and include, among others, asset pricing of European [[Arr18](https://arxiv.org/html/2602.05898v1#bib.bibx7), [LNPA19](https://arxiv.org/html/2602.05898v1#bib.bibx45), [LNPA20](https://arxiv.org/html/2602.05898v1#bib.bibx46)] and American options [[BFZ22](https://arxiv.org/html/2602.05898v1#bib.bibx13), [BHRS23](https://arxiv.org/html/2602.05898v1#bib.bibx15), [BPS25](https://arxiv.org/html/2602.05898v1#bib.bibx16)], detection of market anomalies [[AGTZ22](https://arxiv.org/html/2602.05898v1#bib.bibx3)], optimal execution [[KLA20](https://arxiv.org/html/2602.05898v1#bib.bibx41), [CPASB22](https://arxiv.org/html/2602.05898v1#bib.bibx26)], portfolio optimization [[FHW23](https://arxiv.org/html/2602.05898v1#bib.bibx30), [CM25](https://arxiv.org/html/2602.05898v1#bib.bibx25)], and calibration of financial models [[ASS21](https://arxiv.org/html/2602.05898v1#bib.bibx9), [CGSF23](https://arxiv.org/html/2602.05898v1#bib.bibx21), [CGMSF25](https://arxiv.org/html/2602.05898v1#bib.bibx20)]. For a comprehensive exposition of this fast-growing field, we refer to [[BdRHO25](https://arxiv.org/html/2602.05898v1#bib.bibx11)]. Beyond mathematical finance, signature-based techniques have been applied to machine learning in a variety of contexts, including computer vision, natural language processing, and medical data analysis; see, for instance, [[CK26](https://arxiv.org/html/2602.05898v1#bib.bibx24), [ML25](https://arxiv.org/html/2602.05898v1#bib.bibx48)] and the references therein.

The signature of a path was first introduced by Chen [[Che57](https://arxiv.org/html/2602.05898v1#bib.bibx22), [Che77](https://arxiv.org/html/2602.05898v1#bib.bibx23)] and plays a prominent role in rough path theory, initiated by Lyons [[Lyo98](https://arxiv.org/html/2602.05898v1#bib.bibx47)], which provides a rich mathematical framework for analyzing complex evolving systems driven by irregular signals. Formally, the signature of a path X:[0,T]→ℝdX\colon[0,T]\to\mathbb{R}^{d} is defined as the collection of all the iterated integrals of the path X=(X1,…,Xd)X=(X^{1},\dots,X^{d}) against itself, that is,

|  |  |  |
| --- | --- | --- |
|  | ∫0<t1<…<tn<TdXt1i1​⋯​dXtnin,\int\_{0<t\_{1}<\ldots<t\_{n}<T}\mathrm{d}X^{i\_{1}}\_{t\_{1}}\cdots\mathrm{d}X^{i\_{n}}\_{t\_{n}}, |  |

for i1,…,in∈{1,…,d}i\_{1},\ldots,i\_{n}\in\{1,\ldots,d\} and all n∈ℕn\in\mathbb{N}. Assuming the integrals are well-defined, using a suitable notion of integration, the signature summarizes the full evolution and interactions of the components of the path effectively: the signature is known to provide an intriguing nonlinear characterization of the path that is unique up to tree-like equivalence, see [[HL10](https://arxiv.org/html/2602.05898v1#bib.bibx38), [BGLY16](https://arxiv.org/html/2602.05898v1#bib.bibx14)]. Importantly, due to the rich algebraic structure, that is immediate given a suitable notion of integration, the signature comes with an intriguing universal approximation property: linear functionals of the signature approximate continuous functionals of the path arbitrarily well on compact sets, analogously to polynomials approximating continuous real valued functions; see, e.g., [[LLN13](https://arxiv.org/html/2602.05898v1#bib.bibx44), [LNPA20](https://arxiv.org/html/2602.05898v1#bib.bibx46), [CPSF25](https://arxiv.org/html/2602.05898v1#bib.bibx27)]. This universality result lies at the heart of most signature-based methods.

When considering smooth paths X:[0,T]→ℝdX\colon[0,T]\to\mathbb{R}^{d}, the signature is canonically defined via Riemann–Stieltjes integration. When, however, considering paths of low regularity, such as the sample paths of Brownian motion, or more generally, of semimartingales, one cannot rely on Riemann–Stieltjes (or Young) integration, and typically turns to stochastic calculus. Here, the notion of integral becomes ambiguous, with Itô and Stratonovich integration being the most common choices. Once a probabilistic structure is fixed, one can then construct the second-order iterated integrals

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,t(2):=(∫s<t1<t2<tdXt1i1​dXt2i2)i1,i2∈{1,…,d}for ​s,t∈[0,T],\mathbb{X}\_{s,t}^{(2)}:=\bigg(\int\_{s<t\_{1}<t\_{2}<t}\mathrm{d}X^{i\_{1}}\_{t\_{1}}\mathrm{d}X^{i\_{2}}\_{t\_{2}}\bigg)\_{i\_{1},i\_{2}\in\{1,\ldots,d\}}\quad\text{for }s,t\in[0,T], |  |

for almost every sample path XX of a continuous semimartingale.

As the Stratonovich integral satisfies first-order calculus (as does the Riemann–Stieltjes integral for smooth paths), using that notion of integration gives rise to a *weakly geometric* rough path (X,𝕏(2))(X,\mathbb{X}^{(2)}) that is to be understood in the sense of rough path theory; see, e.g., [[LCL07](https://arxiv.org/html/2602.05898v1#bib.bibx43), [FV10](https://arxiv.org/html/2602.05898v1#bib.bibx32)]. Classically, in the rough path literature, the signature of a (weakly geometric) rough path is defined via Lyons’ extension theorem [[LCL07](https://arxiv.org/html/2602.05898v1#bib.bibx43)]; see Definition [2.3](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem3 "Definition 2.3. ‣ 2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths") and also, for example,  [[LLN13](https://arxiv.org/html/2602.05898v1#bib.bibx44), [CPSF25](https://arxiv.org/html/2602.05898v1#bib.bibx27)]. Enhancing a weakly geometric rough path, we inherently obtain the desired algebraic, and also geometric, properties of the signature. In particular, the signature is a group-like element and, therefore, satisfies the shuffle property. As a consequence, the linear span of the signature components forms a point-separating algebra. This in turn allows to apply the Stone–Weierstrass theorem to deduce the above-mentioned universal approximation property.

In mathematical finance, Itô integration is typically the more natural choice of stochastic integration, as the Itô integral preserves the martingale property, which also underlies the principle of no-arbitrage, and allows for a transparent financial interpretation—for instance when used to model the capital gains process. Itô integration is preferred also in continuous-time econometric analysis, see [[BRSF25](https://arxiv.org/html/2602.05898v1#bib.bibx19)] for an application of signatures, as well as for model order reduction, as pointed out, for instance, in [[BR24](https://arxiv.org/html/2602.05898v1#bib.bibx17)]. Moreover, the signature associated with Itô integration can offer statistical advantages; see [[GWZZ25](https://arxiv.org/html/2602.05898v1#bib.bibx35)] for a comparison of the statistical consistency of the Lasso estimator using the signature based on Itô and based on Stratonovich integration.

If one constructs the second-order iterated integrals 𝕏(2)\mathbb{X}^{(2)} as above, now using Itô integration, the resulting rough path (X,𝕏(2))(X,\mathbb{X}^{(2)}) is in general *not* weakly geometric. The associated signature then is not a group-like valued path, but a path that takes values in the extended tensor algebra. In particular, the shuffle property does not hold and the Stone–Weierstrass theorem cannot be immediately applied to deduce the universal approximation property.

The aim of this paper is to present universal approximation theorems for signatures of rough paths that are not necessarily weakly geometric. We thereby provide a theoretical foundation for approximations based on the Itô signature, which is conceptually natural from the perspective of mathematical finance. Moreover, our work contributes to a recent line of research that has been concerned with deriving universal approximation results for signatures of general rough paths. For instance, see [[HBS24](https://arxiv.org/html/2602.05898v1#bib.bibx36)] for a universal approximation result for polynomial functionals of the signature of rough paths, and see [[AF25](https://arxiv.org/html/2602.05898v1#bib.bibx2)], where they consider the branched signature based on the branched rough path framework in the sense of [[Gub10](https://arxiv.org/html/2602.05898v1#bib.bibx34)].

In Section [2](https://arxiv.org/html/2602.05898v1#S2 "2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths"), we consider signatures of general rough paths which are not necessarily weakly geometric, and in the pp-variation regularity regime for p∈(2,3)p\in(2,3). We show that linear functionals of the signature of rough paths approximate continuous functionals on rough path spaces uniformly on subsets of compacts, when the paths is extended by time and its rough path brackets. More precisely, and related to the natural Itô–Stratonovich correction for semimartingales (see also [[BC19](https://arxiv.org/html/2602.05898v1#bib.bibx10), [BFT26](https://arxiv.org/html/2602.05898v1#bib.bibx12)]), our approach is to start with a rough path, and to extend the underlying path by time and its rough path bracket terms. We then lift the extended path to a rough path, and define its signature via Lyons’ extension theorem. Although this increases the dimension of the path, it ensures that the resulting signature satisfies the so-called *quasi shuffle property* (see Proposition [2.6](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem6 "Proposition 2.6 (Quasi-shuffle property). ‣ 2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths")), and that the linear span of its components does form a point-separating algebra. As a consequence, we are able to deduce the universal approximation property of linear functionals of the signature; see Theorem [2.8](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem8 "Theorem 2.8. ‣ 2.4. Universal approximation with signatures of general rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths"). This universal approximation theorem extends the classical one for signatures of weakly geometric rough paths, and allows to consider signatures of such general rough paths as a linear regression basis for continuous path functionals. For completeness, we also provide in Appendix [A](https://arxiv.org/html/2602.05898v1#A1 "Appendix A Proof of Theorem 2.11 ‣ Universal approximation with signatures of non-geometric rough paths") a direct proof of the universal approximation theorem for signatures of time-extended weakly geometric rough paths.

As an example that fits into this framework, in Section [3](https://arxiv.org/html/2602.05898v1#S3 "3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths"), we introduce a notion of a signature constructed via general pathwise stochastic integration that can be seen as a generalization of Föllmer integration [[Föl81](https://arxiv.org/html/2602.05898v1#bib.bibx31)]. For this purpose, we make use of the path property γ\gamma-(RIE), which has been studied in [[DKP25](https://arxiv.org/html/2602.05898v1#bib.bibx28)], and which ensures that the path, that is continuous and of finite pp-variation for some p∈(2,3)p\in(2,3), extends canonically to a (not necessarily weakly geometric) rough path, where the lift is given as limits of Riemann sums. For such paths, we define the *γ\gamma-signature* as Lyons’ extension of this canonical rough path, which coincides with the collection of iterated rough integrals of controlled paths with respect to the rough path. (We present a rigorous proof of this statement for general continuous pp-rough paths, p∈(2,3)p\in(2,3), in Appendix [C](https://arxiv.org/html/2602.05898v1#A3 "Appendix C On Lyons’ extension theorem ‣ Universal approximation with signatures of non-geometric rough paths").) We remark that the pathwise integrals exist as limits of general Riemann sums along suitable sequences of partitions, thus yielding a unifying framework for pathwise Stratonovich, Itô and backward Itô integration. Corollary [3.10](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem10 "Corollary 3.10. ‣ 3.3. A universal approximation theorem with 𝜸-signatures ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") then states the corresponding universal approximation property of linear functionals of the γ\gamma-signature of paths extended by time and their rough path bracket terms. In this setting, the rough path bracket is closely linked to Föllmer’s notion of pathwise quadratic variation.

In Section [4](https://arxiv.org/html/2602.05898v1#S4 "4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths"), the deterministic theory is translated into the probabilistic setting using stochastic integration. In particular, we consider the Itô signature of continuous semimartingales, that is, the collection of iterated integrals defined via Itô integration, and obtain a universal approximation theorem for linear functionals of the Itô signature of continuous semimartingales extended by time and their quadratic variation terms; see Corollary [4.5](https://arxiv.org/html/2602.05898v1#S4.Thmtheorem5 "Corollary 4.5. ‣ 4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths").

One may now pose the question when it is actually advantageous in practice to extend the path additionally by its quadratic (co)-variation. Therefore, in Section [5](https://arxiv.org/html/2602.05898v1#S5 "5. Numerical examples ‣ Universal approximation with signatures of non-geometric rough paths"), we finally provide numerical examples to briefly showcase the implications of using Itô signatures in applications in finance: we consider calibration to time-series data, payoff approximation, and pricing tasks for options that naturally depend on quadratic variation.

Organization of the paper: In Section [2](https://arxiv.org/html/2602.05898v1#S2 "2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths") we develop the framework for signatures of rough paths and derive a universal approximation theorem using rough paths that are not necessarily weakly geometric, and where the path is extended by its rough path bracket terms. Section [3](https://arxiv.org/html/2602.05898v1#S3 "3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") introduces the notion of γ\gamma-signatures, based on general pathwise stochastic integration, and presents corresponding universal approximation results. In Section [4](https://arxiv.org/html/2602.05898v1#S4 "4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths") we translate these findings to the probabilistic setting of continuous semimartingales and obtain a universal approximation theorem for Itô signatures of continuous semimartingales. Section [5](https://arxiv.org/html/2602.05898v1#S5 "5. Numerical examples ‣ Universal approximation with signatures of non-geometric rough paths") provides numerical experiments on signature-based approaches for calibration and option pricing, using paths extended by time and quadratic variation. Finally, Appendices [A](https://arxiv.org/html/2602.05898v1#A1 "Appendix A Proof of Theorem 2.11 ‣ Universal approximation with signatures of non-geometric rough paths")–[D](https://arxiv.org/html/2602.05898v1#A4 "Appendix D Some additional results in rough path theory ‣ Universal approximation with signatures of non-geometric rough paths") contain proofs that have been postponed, and auxiliary results from rough path theory.

Acknowledgments: The authors would like to thank C. Cuchiero for her helpful suggestions during the preparation of this paper. M. Ceylan gratefully acknowledges financial support by the doctoral scholarship programme from the Avicenna-Studienwerk, Germany.

## 2. The signature of rough paths

We will first recall some essentials from the theory of signatures and rough paths, which we divide into the algebraic and analytic concepts. For a more detailed introduction, we refer to [[LCL07](https://arxiv.org/html/2602.05898v1#bib.bibx43), [FV10](https://arxiv.org/html/2602.05898v1#bib.bibx32)].

### 2.1. Algebraic setting for signatures

The *tensor algebra* and the *extended tensor algebra* on ℝd\mathbb{R}^{d} are defined by

|  |  |  |
| --- | --- | --- |
|  | T​(ℝd):=⨁n=0∞(ℝd)⊗nandT​((ℝd)):=∏n=0∞(ℝd)⊗n,T(\mathbb{R}^{d}):=\bigoplus\_{n=0}^{\infty}(\mathbb{R}^{d})^{\otimes n}\qquad\text{and}\qquad T((\mathbb{R}^{d})):=\prod\_{n=0}^{\infty}(\mathbb{R}^{d})^{\otimes n}, |  |

where (ℝd)⊗n(\mathbb{R}^{d})^{\otimes n} denotes the nn-fold tensor product of ℝd\mathbb{R}^{d}, with the convention (ℝd)⊗0:=ℝ(\mathbb{R}^{d})^{\otimes 0}:=\mathbb{R}.

We equip T​((ℝd))T((\mathbb{R}^{d})) with the standard addition ++, tensor multiplication ⊗\otimes and scalar multiplication, which is defined for 𝐚=(a(n))n=0∞,𝐛=(b(n))n=0∞∈T​((ℝd))\mathbf{a}=(a^{(n)})\_{n=0}^{\infty},\mathbf{b}=(b^{(n)})\_{n=0}^{\infty}\in T((\mathbb{R}^{d})), λ∈ℝ\lambda\in\mathbb{R}, by setting

|  |  |  |
| --- | --- | --- |
|  | 𝐚+𝐛:=(a(n)+b(n))n=0∞,𝐚⊗𝐛:=(∑i+j=na(i)⊗b(j))n=0∞,andλ​𝐚:=(λ​a(n))n=0∞.\displaystyle\mathbf{a}+\mathbf{b}:=(a^{(n)}+b^{(n)})\_{n=0}^{\infty},\quad\mathbf{a}\otimes\mathbf{b}:=\bigg(\sum\_{i+j=n}a^{(i)}\otimes b^{(j)}\bigg)\_{n=0}^{\infty},\quad\text{and}\quad\lambda\mathbf{a}:=(\lambda a^{(n)})\_{n=0}^{\infty}. |  |

These operations induce analogous operations on T​(ℝd)T(\mathbb{R}^{d}) and TN​(ℝd)T^{N}(\mathbb{R}^{d}) defined below.

We observe that (T​((ℝd)),+,⋅,⊗)(T((\mathbb{R}^{d})),+,\cdot,\otimes) is a real non-commutative algebra. The neutral element is (1,0,…,0,…)(1,0,\dots,0,\dots).

Let (e1,…,ed)(e\_{1},\ldots,e\_{d}) be the canonical basis of ℝd\mathbb{R}^{d}. The Lie algebra that is generated by {𝐞1,…,𝐞d}\{\mathbf{e}\_{1},\dots,\mathbf{e}\_{d}\}, where 𝐞i:=(0,ei,0,…)∈T​(ℝd)\mathbf{e}\_{i}:=(0,e\_{i},0,\dots)\in T(\mathbb{R}^{d}), and the commutator bracket

|  |  |  |
| --- | --- | --- |
|  | [𝐚,𝐛]=𝐚⊗𝐛−𝐛⊗𝐚,𝐚,𝐛∈T​(ℝd),[\mathbf{a},\mathbf{b}]=\mathbf{a}\otimes\mathbf{b}-\mathbf{b}\otimes\mathbf{a},\qquad\mathbf{a},\mathbf{b}\in T(\mathbb{R}^{d}), |  |

is called the *free Lie algebra* 𝔤​(ℝd)\mathfrak{g}(\mathbb{R}^{d}) over ℝd\mathbb{R}^{d}, see e.g. [[FV10](https://arxiv.org/html/2602.05898v1#bib.bibx32), Section 7.3]. It is a subalgebra of T0​((ℝd))T\_{0}((\mathbb{R}^{d})), where we define for c∈ℝc\in\mathbb{R}, the tensor subalgebra Tc​((ℝd)):={𝐚=(a(n))n=0∞∈T​((ℝd)):a(0)=c}T\_{c}((\mathbb{R}^{d})):=\{\mathbf{a}=(a^{(n)})\_{n=0}^{\infty}\in T((\mathbb{R}^{d})):a^{(0)}=c\}.

The *free Lie group* G​((ℝd)):=exp⁡(𝔤​(ℝd))G((\mathbb{R}^{d})):=\exp(\mathfrak{g}(\mathbb{R}^{d})) is defined as the tensor exponential of 𝔤​(ℝd)\mathfrak{g}(\mathbb{R}^{d}), i.e., its image under the map

|  |  |  |
| --- | --- | --- |
|  | exp⊗:T0​((ℝd))→T​((ℝd)),𝐚↦1+∑k=1∞1k!​𝐚⊗k.\exp\_{\otimes}\colon T\_{0}((\mathbb{R}^{d}))\to T((\mathbb{R}^{d})),\qquad\mathbf{a}\mapsto 1+\sum\_{k=1}^{\infty}\frac{1}{k!}\mathbf{a}^{\otimes k}. |  |

G​((ℝd))G((\mathbb{R}^{d})) is a subgroup of T1​((ℝd))T\_{1}((\mathbb{R}^{d})). In fact, (G​((ℝd)),⊗)(G((\mathbb{R}^{d})),\otimes) is a group with unit element (1,0,…,0,…)(1,0,\dots,0,\dots), and for all 𝐠=exp⊗⁡(𝐚)∈G​((ℝd))\mathbf{g}=\exp\_{\otimes}(\mathbf{a})\in G((\mathbb{R}^{d})), the inverse with respect to ⊗\otimes is given by 𝐠−1=exp⊗⁡(−𝐚)\mathbf{g}^{-1}=\exp\_{\otimes}(-\mathbf{a}), for 𝐠=exp⊗⁡(𝐚)∈G​((ℝd))\mathbf{g}=\exp\_{\otimes}(\mathbf{a})\in G((\mathbb{R}^{d})). We call elements in G​((ℝd))G((\mathbb{R}^{d})) *group-like* elements.

For N∈ℕN\in\mathbb{N}, the *truncated tensor algebra* on ℝd\mathbb{R}^{d} is defined by

|  |  |  |
| --- | --- | --- |
|  | TN​(ℝd):=⨁n=0N(ℝd)⊗n.T^{N}(\mathbb{R}^{d}):=\bigoplus\_{n=0}^{N}(\mathbb{R}^{d})^{\otimes n}. |  |

For any 𝐚=(a(n))n=0N∈TN​(ℝd)\mathbf{a}=(a^{(n)})\_{n=0}^{N}\in T^{N}(\mathbb{R}^{d}), we set

|  |  |  |
| --- | --- | --- |
|  | |𝐚|TN​(ℝd):=maxn=0,…,N⁡|a(n)|(ℝd)⊗n,|\mathbf{a}|\_{T^{N}(\mathbb{R}^{d})}:=\max\_{n=0,\dots,N}|a^{(n)}|\_{(\mathbb{R}^{d})^{\otimes n}}, |  |

where we write |⋅||\cdot| for the Euclidean norm, on ℝd\mathbb{R}^{d} or (ℝd)⊗n(\mathbb{R}^{d})^{\otimes n} for some n∈ℕn\in\mathbb{N}. We consider the maps Π(n):T​((ℝd))→(ℝd)⊗n\Pi\_{(n)}\colon T((\mathbb{R}^{d}))\to(\mathbb{R}^{d})^{\otimes n} and ΠN:T​((ℝd))→TN​(ℝd)\Pi\_{N}\colon T((\mathbb{R}^{d}))\to T^{N}(\mathbb{R}^{d}), where Π(n)​(𝐚)=a(n)\Pi\_{(n)}(\mathbf{a})=a^{(n)} and ΠN​(𝐚)=(a(0),…,a(N))\Pi\_{N}(\mathbf{a})=(a^{(0)},\dots,a^{(N)}), for 𝐚=(a(n))n=0∞∈T​((ℝd))\mathbf{a}=(a^{(n)})\_{n=0}^{\infty}\in T((\mathbb{R}^{d})). We set for c∈ℝc\in\mathbb{R}, TcN​(ℝd):={ΠN​(𝐚):𝐚∈Tc​((ℝd))}T\_{c}^{N}(\mathbb{R}^{d}):=\{\Pi\_{N}(\mathbf{a}):\mathbf{a}\in T\_{c}((\mathbb{R}^{d}))\}. Then T1N​(ℝd)T\_{1}^{N}(\mathbb{R}^{d}) is a Lie group under the tensor multiplication ⊗\otimes, truncated at level NN. We equip T1N​(ℝd)T\_{1}^{N}(\mathbb{R}^{d}) with the metric

|  |  |  |
| --- | --- | --- |
|  | ρ​(𝐚,𝐛):=|𝐚−𝐛|TN​(ℝd)=maxn=1,…,N⁡|(a−b)(n)|(ℝd)⊗n,\rho(\mathbf{a},\mathbf{b}):=|\mathbf{a}-\mathbf{b}|\_{T^{N}(\mathbb{R}^{d})}=\max\_{n=1,\ldots,N}|(a-b)^{(n)}|\_{(\mathbb{R}^{d})^{\otimes n}}, |  |

for 𝐚=(a(n))n=0N,𝐛=(b(n))n=0N∈T1N​(ℝd)\mathbf{a}=(a^{(n)})\_{n=0}^{N},\mathbf{b}=(b^{(n)})\_{n=0}^{N}\in T\_{1}^{N}(\mathbb{R}^{d}), which arises from the norm on TN​(ℝd)T^{N}(\mathbb{R}^{d}).

The *free nilpotent Lie algebra* and the *free nilpotent Lie group of order NN* are defined by 𝔤N​(ℝd):=ΠN​(𝔤​(ℝd))\mathfrak{g}^{N}(\mathbb{R}^{d}):=\Pi\_{N}(\mathfrak{g}(\mathbb{R}^{d})) and GN​(ℝd):=ΠN​(G​((ℝd)))G^{N}(\mathbb{R}^{d}):=\Pi\_{N}(G((\mathbb{R}^{d}))), respectively. That is,

|  |  |  |
| --- | --- | --- |
|  | 𝔤N​(ℝd)={0}⊕ℝd⊕[ℝd,ℝd]⊕⋯⊕[ℝd,[ℝd,…​[ℝd,ℝd]]]⏟N−1 brackets⊆T0N​(ℝd).\mathfrak{g}^{N}(\mathbb{R}^{d})=\{0\}\oplus\mathbb{R}^{d}\oplus[\mathbb{R}^{d},\mathbb{R}^{d}]\oplus\dots\oplus\underbrace{[\mathbb{R}^{d},[\mathbb{R}^{d},\dots[\mathbb{R}^{d},\mathbb{R}^{d}]]]}\_{\text{$N-1$ brackets}}\subseteq T\_{0}^{N}(\mathbb{R}^{d}). |  |

Then GN​(ℝd)G^{N}(\mathbb{R}^{d}) is a subgroup of T1N​(ℝd)T\_{1}^{N}(\mathbb{R}^{d}) with respect to ⊗\otimes.

Defining the truncated tensor exponential via the corresponding (finite) power series in the truncated tensor algebra, we have that GN​(ℝd)=exp⊗N⁡(𝔤N​(ℝd))G^{N}(\mathbb{R}^{d})=\exp\_{\otimes}^{N}(\mathfrak{g}^{N}(\mathbb{R}^{d})).

Now, let I=(i1,…,i|I|)I=(i\_{1},\ldots,i\_{|I|}) be a multi-index (with entries in {1,…,d}\{1,\dots,d\}) of length |I||I|. We recall the canonical basis (e1,…,ed)(e\_{1},\dots,e\_{d}) of ℝd\mathbb{R}^{d}, and set eI:=ei1⊗⋯⊗ei|I|e\_{I}:=e\_{i\_{1}}\otimes\dots\otimes e\_{i\_{|I|}}. If |I|=1|I|=1, set I′=∅I^{\prime}=\emptyset, if |I|≥1|I|\geq 1, I′=(i1,…,i|I|−1)I^{\prime}=(i\_{1},\ldots,i\_{|I|-1}). Moreover, we denote by e∅e\_{\emptyset} the basis element of (ℝd)⊗0(\mathbb{R}^{d})^{\otimes 0} and set |∅|:=0|\emptyset|:=0. This allows to write 𝐚∈T​((ℝd))\mathbf{a}\in T((\mathbb{R}^{d})) (and 𝐚∈T​(ℝd)\mathbf{a}\in T(\mathbb{R}^{d})) as

|  |  |  |
| --- | --- | --- |
|  | 𝐚=∑|I|≥0aI​eI,\mathbf{a}=\sum\_{|I|\geq 0}a\_{I}e\_{I}, |  |

for some aI∈ℝa\_{I}\in\mathbb{R}.

Furthermore, for 𝐚∈T​(ℝd)\mathbf{a}\in T(\mathbb{R}^{d}) and 𝐛∈T​((ℝd))\mathbf{b}\in T((\mathbb{R}^{d})), we set

|  |  |  |
| --- | --- | --- |
|  | ⟨𝐚,𝐛⟩:=∑|I|≥0⟨aI,bI⟩.\langle\mathbf{a},\mathbf{b}\rangle:=\sum\_{|I|\geq 0}\langle a\_{I},b\_{I}\rangle. |  |

where ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle is defined as the inner product of (ℝd)⊗n(\mathbb{R}^{d})^{\otimes n} for each n≥0n\geq 0. Then (eI){I:|I|=n}(e\_{I})\_{\{I:|I|=n\}} is the canonical orthonormal basis of (ℝd)⊗n(\mathbb{R}^{d})^{\otimes n} with respect to this inner product and we write aI:=⟨eI,𝐚⟩:=⟨eI,Π(|I|)​(𝐚)⟩a\_{I}:=\langle e\_{I},\mathbf{a}\rangle:=\langle e\_{I},\Pi\_{(|I|)}(\mathbf{a})\rangle.

Associating ℓ∈T​(ℝd)\ell\in T(\mathbb{R}^{d}) with a linear functional ⟨ℓ,⋅⟩:T​((ℝd))→ℝ\langle\ell,\cdot\rangle\colon T((\mathbb{R}^{d}))\to\mathbb{R}, we write

|  |  |  |
| --- | --- | --- |
|  | ⟨ℓ,𝐚⟩:=∑0≤|I|≤NℓI​⟨eI,𝐚⟩,𝐚∈T​((ℝd)),\langle\ell,\mathbf{a}\rangle:=\sum\_{0\leq|I|\leq N}\ell\_{I}\langle e\_{I},\mathbf{a}\rangle,\qquad\mathbf{a}\in T((\mathbb{R}^{d})), |  |

for ℓ=∑0≤|I|≤NℓI​eI\ell=\sum\_{0\leq|I|\leq N}\ell\_{I}e\_{I}, where ℓI:=⟨eI,ℓ⟩∈ℝ\ell\_{I}:=\langle e\_{I},\ell\rangle\in\mathbb{R} and N∈ℕ0N\in\mathbb{N}\_{0}.

For two multi-indices I=(i1,…,i|I|)I=(i\_{1},\ldots,i\_{|I|}), J=(j1,…,j|J|)J=(j\_{1},\ldots,j\_{|J|}) with entries in {1,…,d}\{1,\ldots,d\}, the *shuffle product* is recursively defined by

|  |  |  |
| --- | --- | --- |
|  | eI​eJ:=(eI′​eJ)⊗ei|I|+(eI​eJ′)⊗ej|J|,e\_{I}\shuffle e\_{J}:=(e\_{I^{\prime}}\shuffle e\_{J})\otimes e\_{i\_{|I|}}+(e\_{I}\shuffle e\_{J^{\prime}})\otimes e\_{j\_{|J|}}, |  |

with eI​e∅:=e∅​eI:=eIe\_{I}\shuffle e\_{\emptyset}:=e\_{\emptyset}\shuffle e\_{I}:=e\_{I}. For 𝐚,𝐛∈T​(ℝd)\mathbf{a},\mathbf{b}\in T(\mathbb{R}^{d}), we set

|  |  |  |
| --- | --- | --- |
|  | a​b=∑|I|,|J|≥0aI​bJ​(eI​eJ)a\shuffle b=\sum\_{|I|,|J|\geq 0}a\_{I}b\_{J}(e\_{I}\shuffle e\_{J}) |  |

and for 𝐚,𝐛∈T​((ℝd))\mathbf{a},\mathbf{b}\in T((\mathbb{R}^{d})), we set

|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝐚𝐛⟩=⟨eI,Π(|I|)​(𝐚)​Π(|I|)​(𝐛)⟩.\langle e\_{I},\mathbf{a}\shuffle\mathbf{b}\rangle=\langle e\_{I},\Pi\_{(|I|)}(\mathbf{a})\Pi\_{(|I|)}(\mathbf{b})\rangle. |  |

For all 𝐚∈G​((ℝd))\mathbf{a}\in G((\mathbb{R}^{d})), the *shuffle product property* holds, i.e., for two multi-indices I=(i1,…,i|I|)I=(i\_{1},\ldots,i\_{|I|}), J=(j1,…,j|J|)J=(j\_{1},\ldots,j\_{|J|}), it holds that

|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝐚⟩​⟨eJ,𝐚⟩=⟨eI​eJ,𝐚⟩.\langle e\_{I},\mathbf{a}\rangle\langle e\_{J},\mathbf{a}\rangle=\langle e\_{I}\shuffle e\_{J},\mathbf{a}\rangle. |  |

### 2.2. Essentials on rough path theory

A *partition* 𝒫\mathcal{P} of an interval [s,t][s,t] is a finite set of points between and including the points ss and tt, i.e., 𝒫={s=u0<u1<⋯<uN=t}\mathcal{P}=\{s=u\_{0}<u\_{1}<\cdots<u\_{N}=t\} for some N∈ℕN\in\mathbb{N}, and its mesh size is denoted by |𝒫|:=max⁡{|ui+1−ui|:i=0,…,N−1}|\mathcal{P}|:=\max\{|u\_{i+1}-u\_{i}|\,:\,i=0,\ldots,N-1\}.

Throughout, we let T>0T>0 be a fixed finite time horizon. We let ΔT:={(s,t)∈[0,T]2:s≤t}\Delta\_{T}:=\{(s,t)\in[0,T]^{2}\,:\,s\leq t\} denote the standard 22-simplex.

We shall write a≲ba\lesssim b to mean that there exists a constant C>0C>0 such that a≤C​ba\leq Cb. The constant CC may depend on the normed space, e.g. through its dimension or regularity parameters.

For a normed space (E,|⋅|)(E,|\cdot|), we let C​([0,T];E)C([0,T];E) denote the set of continuous paths from [0,T][0,T] to EE. For X∈C​([0,T];E)X\in C([0,T];E), the supremum seminorm of the path XX is given by

|  |  |  |
| --- | --- | --- |
|  | ‖X‖∞:=supt∈[0,T]|Xt|,\|X\|\_{\infty}:=\sup\_{t\in[0,T]}|X\_{t}|, |  |

and for p≥1p\geq 1, the pp-variation of the path XX is given by

|  |  |  |
| --- | --- | --- |
|  | ‖X‖p:=‖X‖p,[0,T]with‖X‖p,[s,t]:=(sup𝒫⊂[s,t]∑[u,v]∈𝒫|Xv−Xu|p)1p,(s,t)∈ΔT,\|X\|\_{p}:=\|X\|\_{p,[0,T]}\qquad\text{with}\qquad\|X\|\_{p,[s,t]}:=\bigg(\sup\_{\mathcal{P}\subset[s,t]}\sum\_{[u,v]\in\mathcal{P}}|X\_{v}-X\_{u}|^{p}\bigg)^{\frac{1}{p}},\quad(s,t)\in\Delta\_{T}, |  |

where the supremum is taken over all possible partitions 𝒫\mathcal{P} of the interval [s,t][s,t]. We recall that, given a path XX, we have that ‖X‖p<∞\|X\|\_{p}<\infty if and only if there exists a control function cc such that111Here and throughout, we adopt the convention that 00:=0\frac{0}{0}:=0.

|  |  |  |
| --- | --- | --- |
|  | sup(u,v)∈ΔT|Xv−Xu|pc​(u,v)<∞.\sup\_{(u,v)\in\Delta\_{T}}\frac{|X\_{v}-X\_{u}|^{p}}{c(u,v)}<\infty. |  |

We write Cp​-var=Cp​-var​([0,T];E)C^{p\textup{-var}}=C^{p\textup{-var}}([0,T];E) for the space of paths X∈C​([0,T];E)X\in C([0,T];E) which satisfy ‖X‖p<∞\|X\|\_{p}<\infty. Moreover, for a path X∈C​([0,T];ℝd)X\in C([0,T];\mathbb{R}^{d}), we will often use the shorthand notation:

|  |  |  |
| --- | --- | --- |
|  | Xs,t:=Xt−Xs,for(s,t)∈ΔT.X\_{s,t}:=X\_{t}-X\_{s},\qquad\text{for}\quad(s,t)\in\Delta\_{T}. |  |

For r≥1r\geq 1 and a two-parameter function 𝕏(2):ΔT→E\mathbb{X}^{(2)}\colon\Delta\_{T}\to E, we further define

|  |  |  |
| --- | --- | --- |
|  | ‖𝕏(2)‖r:=‖𝕏(2)‖r,[0,T]with‖𝕏(2)‖r,[s,t]:=(sup𝒫⊂[s,t]∑[u,v]∈𝒫|𝕏u,v(2)|r)1r,(s,t)∈ΔT.\|\mathbb{X}^{(2)}\|\_{r}:=\|\mathbb{X}^{(2)}\|\_{r,[0,T]}\qquad\text{with}\qquad\|\mathbb{X}^{(2)}\|\_{r,[s,t]}:=\bigg(\sup\_{\mathcal{P}\subset[s,t]}\sum\_{[u,v]\in\mathcal{P}}|\mathbb{X}^{(2)}\_{u,v}|^{r}\bigg)^{\frac{1}{r}},\quad(s,t)\in\Delta\_{T}. |  |

We write C2r​-var=C2r​-var​(ΔT;E)C\_{2}^{r\textup{-var}}=C\_{2}^{r\textup{-var}}(\Delta\_{T};E) for the space of continuous functions 𝕏(2):ΔT→E\mathbb{X}^{(2)}\colon\Delta\_{T}\to E which satisfy ‖𝕏(2)‖r<∞\|\mathbb{X}^{(2)}\|\_{r}<\infty.

For p∈[2,3)p\in[2,3), a pair 𝐗=(X,𝕏(2))\mathbf{X}=(X,\mathbb{X}^{(2)}) is called a *(continuous) rough path* over ℝd\mathbb{R}^{d} if

1. (i)

   X∈Cp​-var​([0,T];ℝd)X\in C^{p\textup{-var}}([0,T];\mathbb{R}^{d}) and 𝕏(2)∈C2p2​-var​(ΔT;ℝd×d)\mathbb{X}^{(2)}\in C\_{2}^{\frac{p}{2}\textup{-var}}(\Delta\_{T};\mathbb{R}^{d\times d}), and
2. (ii)

   Chen’s relation: 𝕏s,t(2)=𝕏s,u(2)+𝕏u,t(2)+Xs,u⊗Xu,t\mathbb{X}^{(2)}\_{s,t}=\mathbb{X}^{(2)}\_{s,u}+\mathbb{X}^{(2)}\_{u,t}+X\_{s,u}\otimes X\_{u,t} holds for all 0≤s≤u≤t≤T0\leq s\leq u\leq t\leq T.

In component form, condition (ii) states that (𝕏(2))s,ti​j=(𝕏(2))s,ui​j+(𝕏(2))u,ti​j+Xs,ui​Xu,tj(\mathbb{X}^{(2)})^{ij}\_{s,t}=(\mathbb{X}^{(2)})^{ij}\_{s,u}+(\mathbb{X}^{(2)})^{ij}\_{u,t}+X^{i}\_{s,u}X^{j}\_{u,t} for every ii and jj. We will denote the space of rough paths by 𝒞p=𝒞p​([0,T];ℝd)\mathcal{C}^{p}=\mathcal{C}^{p}([0,T];\mathbb{R}^{d}). On the space 𝒞p​([0,T];ℝd)\mathcal{C}^{p}([0,T];\mathbb{R}^{d}), we use the natural seminorm

|  |  |  |
| --- | --- | --- |
|  | ‖𝐗‖p:=‖𝐗‖p,[0,T]with‖𝐗‖p,[s,t]:=‖X‖p,[s,t]+‖𝕏(2)‖p2,[s,t]\|\mathbf{X}\|\_{p}:=\|\mathbf{X}\|\_{p,[0,T]}\qquad\text{with}\qquad\|\mathbf{X}\|\_{p,[s,t]}:=\|X\|\_{p,[s,t]}+\|\mathbb{X}^{(2)}\|\_{\frac{p}{2},[s,t]} |  |

for (s,t)∈ΔT(s,t)\in\Delta\_{T}.

Let p∈(2,3)p\in(2,3) and q>0q>0 such that 2/p+1/q>12/p+1/q>1, and X∈Cp​-var​([0,T];ℝd)X\in C^{p\text{-var}}([0,T];\mathbb{R}^{d}). We say that a pair (Y,Y′)(Y,Y^{\prime}) is a *controlled path* (with respect to XX), if

|  |  |  |
| --- | --- | --- |
|  | Y∈Cp​-var​([0,T];ℝd×n),Y′∈Cq​-var​([0,T];ℒ​(ℝd;ℝd×n)),andRY∈C2r​-var​(ΔT;ℝd×n),Y\in C^{p\text{-var}}([0,T];\mathbb{R}^{d\times n}),\quad Y^{\prime}\in C^{q\text{-var}}([0,T];\mathcal{L}(\mathbb{R}^{d};\mathbb{R}^{d\times n})),\quad\text{and}\quad R^{Y}\in C^{r\text{-var}}\_{2}(\Delta\_{T};\mathbb{R}^{d\times n}), |  |

where RYR^{Y} is defined by

|  |  |  |
| --- | --- | --- |
|  | Ys,t=Ys′​Xs,t+Rs,tYfor all(s,t)∈ΔT,Y\_{s,t}=Y^{\prime}\_{s}X\_{s,t}+R^{Y}\_{s,t}\qquad\text{for all}\quad(s,t)\in\Delta\_{T}, |  |

and 1/r=1/p+1/q1/r=1/p+1/q. We write 𝒞Xp,q=𝒞Xp,q​([0,T];ℝd×n)\mathscr{C}^{p,q}\_{X}=\mathscr{C}^{p,q}\_{X}([0,T];\mathbb{R}^{d\times n}) for the space of ℝd×n\mathbb{R}^{d\times n}-valued controlled paths, which becomes a Banach space when equipped with the norm

|  |  |  |
| --- | --- | --- |
|  | (Y,Y′)↦|Y0|+|Y0′|+‖Y′‖q,[0,T]+‖RY‖r,[0,T].(Y,Y^{\prime})\mapsto|Y\_{0}|+|Y^{\prime}\_{0}|+\|Y^{\prime}\|\_{q,[0,T]}+\|R^{Y}\|\_{r,[0,T]}. |  |

When p=qp=q, r=p2r=\frac{p}{2}, we write 𝒞Xp=𝒞Xp,p2\mathscr{C}^{p}\_{X}=\mathscr{C}^{p,\frac{p}{2}}\_{X}.

Further, for p≥1p\geq 1, and N∈ℕN\in\mathbb{N}, the pp-variation of 𝕏N:[0,T]→TN​(ℝd)\mathbb{X}^{N}\colon[0,T]\to T^{N}(\mathbb{R}^{d}) is given by

|  |  |  |
| --- | --- | --- |
|  | ‖𝕏N‖p,[s,t]:=max1≤m≤N​sup𝒫⊂[s,t](∑[u,v]∈𝒫|Π(m)​(𝕏u,vN)|pm)mp,(s,t)∈ΔT,\|\mathbb{X}^{N}\|\_{p,[s,t]}:=\max\_{1\leq m\leq N}\sup\_{\mathcal{P}\subset[s,t]}\bigg(\sum\_{[u,v]\in\mathcal{P}}|\Pi\_{(m)}(\mathbb{X}^{N}\_{u,v})|^{\frac{p}{m}}\bigg)^{\frac{m}{p}},\qquad(s,t)\in\Delta\_{T}, |  |

where now 𝕏s,tN:=(𝕏sN)−1⊗𝕏tN\mathbb{X}^{N}\_{s,t}:=(\mathbb{X}^{N}\_{s})^{-1}\otimes\mathbb{X}^{N}\_{t}, (s,t)∈ΔT(s,t)\in\Delta\_{T}, and we write ‖𝕏N‖p:=‖𝕏N‖p,[0,T]\|\mathbb{X}^{N}\|\_{p}:=\|\mathbb{X}^{N}\|\_{p,[0,T]}.

For 𝕏N,𝕏~N:[0,T]→TN​(ℝd)\mathbb{X}^{N},\widetilde{\mathbb{X}}^{N}\colon[0,T]\to T^{N}(\mathbb{R}^{d}), we define the pp-variation distance

|  |  |  |
| --- | --- | --- |
|  | ∥𝕏N;𝕏~N∥p,[s,t]:=∥𝕏N−𝕏~N∥p,[s,t],(s,t)∈ΔT,\|\mathbb{X}^{N};\widetilde{\mathbb{X}}^{N}\|\_{p,[s,t]}:=\|\mathbb{X}^{N}-\widetilde{\mathbb{X}}^{N}\|\_{p,[s,t]},\qquad(s,t)\in\Delta\_{T}, |  |

and we write ∥𝕏N;𝕏~N∥p=∥𝕏N;𝕏~N∥p,[0,T]\|\mathbb{X}^{N};\widetilde{\mathbb{X}}^{N}\|\_{p}=\|\mathbb{X}^{N};\widetilde{\mathbb{X}}^{N}\|\_{p,[0,T]}.

Moreover, a continuous function 𝕏N:[0,T]→TN​(ℝd)\mathbb{X}^{N}\colon[0,T]\to T^{N}(\mathbb{R}^{d}) is called a *multiplicative functional* if 𝕏s,t0=1\mathbb{X}^{0}\_{s,t}=1 and Chen’s relation holds:

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,uN⊗𝕏u,tN=𝕏s,tN,0≤s≤u≤t≤T.\mathbb{X}^{N}\_{s,u}\otimes\mathbb{X}^{N}\_{u,t}=\mathbb{X}^{N}\_{s,t},\qquad 0\leq s\leq u\leq t\leq T. |  |

We equip GN​(ℝd)G^{N}(\mathbb{R}^{d}) with the (inhomogeneous) subspace topology of TN​(ℝd)T^{N}(\mathbb{R}^{d}). In the literature, the (homogeneous) pp-variation of a GN​(ℝd)G^{N}(\mathbb{R}^{d})-valued path is often defined in terms of the Carnot–Carathéodory metric, see e.g. [[FV10](https://arxiv.org/html/2602.05898v1#bib.bibx32), Chapter 8]. This is consistent because the induced topology on GN​(ℝd)G^{N}(\mathbb{R}^{d}) coincides with the one induced by the Carnot–Carathéodory metric, see e.g. [[FV10](https://arxiv.org/html/2602.05898v1#bib.bibx32), Section 8.1.2 and 8.1.3].

A continuous path 𝕏⌊p⌋:[0,T]→G⌊p⌋​(ℝd)\mathbb{X}^{\lfloor p\rfloor}\colon[0,T]\to G^{\lfloor p\rfloor}(\mathbb{R}^{d}) is called a *weakly geometric rough path*, if 𝕏0⌊p⌋=𝟏\mathbb{X}^{\lfloor p\rfloor}\_{0}=\mathbf{1} and ∥𝟏;𝕏⌊p⌋∥p<∞\|\mathbf{1};\mathbb{X}^{\lfloor p\rfloor}\|\_{p}<\infty, where 𝟏:=(1,0,…,0)∈T⌊p⌋​(ℝd)\mathbf{1}:=(1,0,\dots,0)\in T^{\lfloor p\rfloor}(\mathbb{R}^{d}). We will denote the space of weakly geometric continuous rough paths by Cop​-var=Cop​-var​([0,T];G⌊p⌋​(ℝd))C\_{o}^{p\textup{-var}}=C\_{o}^{p\textup{-var}}([0,T];G^{\lfloor p\rfloor}(\mathbb{R}^{d})) and equip it with the distance ∥⋅;⋅∥p\|\cdot\hskip 1.0pt;\cdot\|\_{p}.

An algebraic condition for a rough path to be weakly geometric is that the symmetric part of the rough path lift is determined by the increments of the path.

###### Lemma 2.1.

Let p∈(2,3)p\in(2,3). Let (X,𝕏(2))∈𝒞p​([0,T];ℝd)(X,\mathbb{X}^{(2)})\in\mathcal{C}^{p}([0,T];\mathbb{R}^{d}) be a continuous rough path such that 𝕊​(𝕏0,t(2))=12​X0,t⊗X0,t\mathbb{S}(\mathbb{X}^{(2)}\_{0,t})=\frac{1}{2}X\_{0,t}\otimes X\_{0,t}, t∈[0,T]t\in[0,T], where we consider the decomposition into the symmetric and the antisymmetric part given by

|  |  |  |
| --- | --- | --- |
|  | 𝕏0,t(2)=𝕊​(𝕏0,t(2))+𝔸​(𝕏0,t(2)):=12​(𝕏0,t(2)+(𝕏0,t(2))⊤)+12​(𝕏0,t(2)−(𝕏0,t(2))⊤),\mathbb{X}^{(2)}\_{0,t}=\mathbb{S}(\mathbb{X}^{(2)}\_{0,t})+\mathbb{A}(\mathbb{X}^{(2)}\_{0,t}):=\frac{1}{2}(\mathbb{X}^{(2)}\_{0,t}+(\mathbb{X}^{(2)}\_{0,t})^{\top})+\frac{1}{2}(\mathbb{X}^{(2)}\_{0,t}-(\mathbb{X}^{(2)}\_{0,t})^{\top}), |  |

where (⋅)⊤(\cdot)^{\top} denotes matrix transposition. Then 𝕏2\mathbb{X}^{2} is a weakly geometric rough path, i.e., 𝕏2∈Cop​-var\mathbb{X}^{2}\in C^{p\textup{-var}}\_{o}, where 𝕏2\mathbb{X}^{2} is defined by

|  |  |  |
| --- | --- | --- |
|  | 𝕏t2:=(1,X0,t,𝕏0,t(2)),t∈[0,T].\mathbb{X}^{2}\_{t}:=(1,X\_{0,t},\mathbb{X}^{(2)}\_{0,t}),\qquad t\in[0,T]. |  |

###### Proof.

Recall that G2​(ℝd)=exp⊗2⁡(𝔤2​(ℝd))G^{2}(\mathbb{R}^{d})=\exp\_{\otimes}^{2}(\mathfrak{g}^{2}(\mathbb{R}^{d})), where 𝔤2​(ℝd)={0}⊕ℝd⊕[ℝd,ℝd]\mathfrak{g}^{2}(\mathbb{R}^{d})=\{0\}\oplus\mathbb{R}^{d}\oplus[\mathbb{R}^{d},\mathbb{R}^{d}]. It holds that [ℝd,ℝd]=span⁡{ei⊗ej−ej⊗ei:1≤i,j≤d}[\mathbb{R}^{d},\mathbb{R}^{d}]=\operatorname{span}\{e\_{i}\otimes e\_{j}-e\_{j}\otimes e\_{i}:1\leq i,j\leq d\}. Therefore [ℝd,ℝd][\mathbb{R}^{d},\mathbb{R}^{d}] equals the set of antisymmetric d×dd\times d-matrices and it follows that, for any t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | 𝕏t2=(1,X0,t,12​X0,t⊗X0,t+𝔸​(𝕏0,t(2)))=exp⊗2⁡(0,X0,t,𝔸​(𝕏0,t(2)))∈G2​(ℝd).\mathbb{X}^{2}\_{t}=\bigg(1,X\_{0,t},\frac{1}{2}X\_{0,t}\otimes X\_{0,t}+\mathbb{A}(\mathbb{X}^{(2)}\_{0,t})\bigg)=\exp\_{\otimes}^{2}(0,X\_{0,t},\mathbb{A}(\mathbb{X}^{(2)}\_{0,t}))\in G^{2}(\mathbb{R}^{d}). |  |

Finally, since (X,𝕏(2))∈𝒞p​([0,T];ℝd)(X,\mathbb{X}^{(2)})\in\mathcal{C}^{p}([0,T];\mathbb{R}^{d}), it particularly holds that ∥𝟏;𝕏2∥p<∞\|\mathbf{1};\mathbb{X}^{2}\|\_{p}<\infty.
∎

###### Remark 2.2.

This condition is a consequence of “first order calculus” and therefore valid in the context of stochastic Stratonovich integration.

### 2.3. Definition and properties of signatures

By Lyons’ extension theorem, see e.g. [[LCL07](https://arxiv.org/html/2602.05898v1#bib.bibx43), Theorem 3.7], any multiplicative functional 𝕏m:[0,T]→Tm​(ℝd)\mathbb{X}^{m}\colon[0,T]\to T^{m}(\mathbb{R}^{d}) with finite pp-variation for m≥⌊p⌋m\geq\lfloor p\rfloor—i.e., 𝕏(i)\mathbb{X}^{(i)}, i≤mi\leq m, is of finite p/ip/i-variation, controlled by a control function cc—admits a unique extension to a multiplicative functional 𝕏:[0,T]→T​((ℝd))\mathbb{X}\colon[0,T]\to T((\mathbb{R}^{d})) with finite pp-variation, for p≥1p\geq 1. More precisely, for any N>⌊p⌋N>\lfloor p\rfloor, there exists a unique continuous function 𝕏(N):[0,T]→(ℝd)⊗N\mathbb{X}^{(N)}\colon[0,T]\to(\mathbb{R}^{d})^{\otimes N} such that,

|  |  |  |
| --- | --- | --- |
|  | (1,X0,⋅,,𝕏(2),…,𝕏(⌊p⌋),…,𝕏(N),…)∈T​((ℝd))(1,X\_{0,\cdot,},\mathbb{X}^{(2)},\ldots,\mathbb{X}^{(\lfloor p\rfloor)},\ldots,\mathbb{X}^{(N)},\ldots)\in T((\mathbb{R}^{d})) |  |

is a multiplicative functional with finite pp-variation, i.e., ΠN​(𝕏)\Pi\_{N}(\mathbb{X}) is of finite pp-variation for any NN, controlled by cc, and is called *Lyons’ extension*.

In particular, any weakly geometric rough path admits a unique extension to a path of finite pp-variation with values in GN​(ℝd)G^{N}(\mathbb{R}^{d}) with N>⌊p⌋N>\lfloor p\rfloor, see e.g. [[FV10](https://arxiv.org/html/2602.05898v1#bib.bibx32), Theorem 9.5], which allows us to define the signature of XX as follows:

###### Definition 2.3.

Let p≥1p\geq 1 and 𝕏o,⌊p⌋∈Cop​-var​([0,T];G⌊p⌋​(ℝd))\mathbb{X}^{o,\lfloor p\rfloor}\in C\_{o}^{p\textup{-var}}([0,T];G^{\lfloor p\rfloor}(\mathbb{R}^{d})). The *signature* of XX is defined as the unique path

|  |  |  |
| --- | --- | --- |
|  | 𝕏o:[0,T]→G​((ℝd)),\mathbb{X}^{o}\colon[0,T]\to G((\mathbb{R}^{d})), |  |

such that for all N>⌊p⌋N>\lfloor p\rfloor, ΠN​(𝕏o)=𝕏o,N\Pi\_{N}(\mathbb{X}^{o})=\mathbb{X}^{o,N}, where 𝕏o,N\mathbb{X}^{o,N} denotes the extension of 𝕏o,⌊p⌋\mathbb{X}^{o,\lfloor p\rfloor} in GN​(ℝd)G^{N}(\mathbb{R}^{d}). In particular, 𝕏o\mathbb{X}^{o} is the unique path extension of 𝕏o,⌊p⌋\mathbb{X}^{o,\lfloor p\rfloor} specified by Lyons’ extension theorem.

Now, let 𝐗=(X,𝕏(2))∈𝒞p​([0,T];ℝd)\mathbf{X}=(X,\mathbb{X}^{(2)})\in\mathcal{C}^{p}([0,T];\mathbb{R}^{d}), p∈(2,3)p\in(2,3), be a rough path, and let 𝕏\mathbb{X} be Lyons’ extension of 𝐗\mathbf{X} to T​((ℝd))T((\mathbb{R}^{d})), i.e., 𝕏:[0,T]→T​((ℝd))\mathbb{X}\colon[0,T]\to T((\mathbb{R}^{d})), which by Proposition [C.1](https://arxiv.org/html/2602.05898v1#A3.Thmtheorem1 "Proposition C.1. ‣ Appendix C On Lyons’ extension theorem ‣ Universal approximation with signatures of non-geometric rough paths") coincides with the collection of iterated rough integrals of controlled paths with respect to 𝐗\mathbf{X}, that is, for N≥3N\geq 3,

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,t(N)=∫st𝕏s,r(N−1)⊗d𝐗r(s,t)∈ΔT.\mathbb{X}\_{s,t}^{(N)}=\int\_{s}^{t}\mathbb{X}\_{s,r}^{(N-1)}\otimes\mathrm{d}\mathbf{X}\_{r}\qquad(s,t)\in\Delta\_{T}. |  |

The rough integral is defined in Lemma [D.1](https://arxiv.org/html/2602.05898v1#A4.Thmtheorem1 "Lemma D.1 (Proposition 2.4 in [ALP24]). ‣ Appendix D Some additional results in rough path theory ‣ Universal approximation with signatures of non-geometric rough paths") and Remark [D.2](https://arxiv.org/html/2602.05898v1#A4.Thmtheorem2 "Remark D.2. ‣ Appendix D Some additional results in rough path theory ‣ Universal approximation with signatures of non-geometric rough paths"), considering G=XG=X so that G′=IdG^{\prime}=I\_{d} is the identity matrix and RG=0R^{G}=0, and the integral reduces to the classical notion of the rough integral of the controlled path (F,F′)(F,F^{\prime}) against the rough path 𝐗\mathbf{X}.

Further, let [𝐗]t:=X0,t⊗X0,t−(𝕏0,t(2)+(𝕏0,t(2))⊤)[\mathbf{X}]\_{t}:=X\_{0,t}\otimes X\_{0,t}-(\mathbb{X}^{(2)}\_{0,t}+(\mathbb{X}^{(2)}\_{0,t})^{\top}), t∈[0,T]t\in[0,T], be the rough path bracket of 𝐗\mathbf{X}, and set

|  |  |  |
| --- | --- | --- |
|  | Q​(X):=([𝐗]11,…,[𝐗]1​d,[𝐗]22,…,[𝐗]2​d,…,[𝐗]d​d).Q(X):=([\mathbf{X}]^{11},\dots,[\mathbf{X}]^{1d},[\mathbf{X}]^{22},\dots,[\mathbf{X}]^{2d},\dots,[\mathbf{X}]^{dd}). |  |

We define X^:=(⋅,X,Q​(X))∈Cp​-var​([0,T];ℝd^)\widehat{X}:=(\cdot,X,Q(X))\in C^{p\textup{-var}}([0,T];\mathbb{R}^{\hat{d}}), with d^=1+d+d​(d+1)2\hat{d}=1+d+\frac{d(d+1)}{2}, and note that X^\widehat{X} can be canonically lifted to a rough path 𝐗^=(X^,𝕏^(2))∈𝒞p​([0,T];ℝd^)\widehat{\mathbf{X}}=(\widehat{X},\widehat{\mathbb{X}}^{(2)})\in\mathcal{C}^{p}([0,T];\mathbb{R}^{\hat{d}}) since Q​(X)Q(X) is a path of finite p/2p/2-variation so that (𝕏^s,t(2))i​j:=∫stX^s,ri​dX^rj(\widehat{\mathbb{X}}^{(2)}\_{s,t})^{ij}:=\int\_{s}^{t}\widehat{X}^{i}\_{s,r}\,\mathrm{d}\widehat{X}^{j}\_{r}, for i,j∉{1,…,d}i,j\notin\{1,\dots,d\}, exist as Young integrals, and (𝕏^s,t(2))i​j:=(𝕏s,t(2))i​j(\widehat{\mathbb{X}}^{(2)}\_{s,t})^{ij}:=(\mathbb{X}^{(2)}\_{s,t})^{ij}, for i,j=1,…,di,j=1,\dots,d. We denote by 𝕏^\widehat{\mathbb{X}} Lyons’ extension of 𝐗^\widehat{\mathbf{X}}.

We write (e0,e1,…,ed,ε11,…,ε1​d,ε22,…,ε2​d,…,εd​d)(e\_{0},e\_{1},\ldots,e\_{d},\varepsilon\_{11},\ldots,\varepsilon\_{1d},\varepsilon\_{22},\ldots,\varepsilon\_{2d},\ldots,\varepsilon\_{dd}) :=(e0,e1,…,ed,ed+1,…,ed^−1):=(e\_{0},e\_{1},\ldots,e\_{d},e\_{d+1},\ldots,e\_{\hat{d}-1}) for the canonical basis of ℝd^\mathbb{R}^{\hat{d}}, i.e., we use the index 0 to denote the time component, and εi​j\varepsilon\_{ij} for the component of X^\widehat{X} referring to [𝐗]i​j[\mathbf{X}]^{ij}, so that ⟨εi​j,𝕏^t⟩:=[𝐗]ti​j\langle\varepsilon\_{ij},\widehat{\mathbb{X}}\_{t}\rangle:=[\mathbf{X}]^{ij}\_{t}, i,j=1,…,di,j=1,\ldots,d, i≤ji\leq j, t∈[0,T]t\in[0,T]. We set εj​i:=εi​j\varepsilon\_{ji}:=\varepsilon\_{ij} and observe that ⟨eI⊗ei,𝕏^t⟩=∫0t⟨eI,𝕏^s⟩​dX^si\langle e\_{I}\otimes e\_{i},\widehat{\mathbb{X}}\_{t}\rangle=\int\_{0}^{t}\langle e\_{I},\widehat{\mathbb{X}}\_{s}\rangle\,\mathrm{d}\widehat{X}\_{s}^{i}, for i∈{0,d+1,…,d^−1}i\in\{0,d+1,\ldots,{\hat{d}-1}\}, is well-defined as an integral with respect to X^i\widehat{X}^{i}.

We further note that t↦⟨e0,𝕏^t⟩t\mapsto\langle e\_{0},\widehat{\mathbb{X}}\_{t}\rangle is strictly monotonically increasing. This is necessary so that 𝕏^T\widehat{\mathbb{X}}\_{T} uniquely characterizes 𝐗^\widehat{\mathbf{X}}, see e.g. [[HL10](https://arxiv.org/html/2602.05898v1#bib.bibx38), [BGLY16](https://arxiv.org/html/2602.05898v1#bib.bibx14)].

See the proof of condition (iii) in Theorem [2.11](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem11 "Theorem 2.11. ‣ 2.5. Discussion on approximation with weakly geometric rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths") for a similar argument for signatures 𝕏^o\widehat{\mathbb{X}}^{o} of time extended weakly geometric rough paths, and the proof of condition (iii) in Theorem [2.8](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem8 "Theorem 2.8. ‣ 2.4. Universal approximation with signatures of general rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths") for signatures 𝕏^\widehat{\mathbb{X}} of general rough paths extended by time and the rough path bracket terms.

Further, let 𝕏^o\widehat{\mathbb{X}}^{o} be Lyons’ extension of (1,X^,𝕏^(2)+12​[𝐗^])(1,\widehat{X},\widehat{\mathbb{X}}^{(2)}+\frac{1}{2}[\widehat{\mathbf{X}}]), that then is a group-like valued path, i.e., 𝕏^o:[0,T]→G​((ℝd^))\widehat{\mathbb{X}}^{o}\colon[0,T]\to G((\mathbb{R}^{\hat{d}})), see Definition [2.3](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem3 "Definition 2.3. ‣ 2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths").

Extending the path XX to X^\widehat{X} by the rough path bracket terms yields that the components of the signature of the non-weakly geometric rough path 𝕏^\widehat{\mathbb{X}} can be represented as linear functionals of the signature of the weakly geometric rough path 𝕏^o\widehat{\mathbb{X}}^{o}.

###### Proposition 2.4.

Let 𝐗=(X,𝕏(2))∈𝒞p​([0,T];ℝd)\mathbf{X}=(X,\mathbb{X}^{(2)})\in\mathcal{C}^{p}([0,T];\mathbb{R}^{d}), p∈(2,3)p\in(2,3), be a rough path, and X^:=(⋅,X,Q​(X))\widehat{X}:=(\cdot,X,Q(X)) be the path extended by time and the rough path bracket terms, and 𝐗^=(X^,𝕏^(2))∈𝒞p​([0,T];ℝd^)\widehat{\mathbf{X}}=(\widehat{X},\widehat{\mathbb{X}}^{(2)})\in\mathcal{C}^{p}([0,T];\mathbb{R}^{\hat{d}}) be the corresponding rough path. Further, let 𝕏^\widehat{\mathbb{X}} be Lyons’ extension of (1,X^,𝕏^(2))∈Cop​-var​([0,T];T2​(ℝd^))(1,\widehat{X},\widehat{\mathbb{X}}^{(2)})\in C\_{o}^{p\textup{-var}}([0,T];T^{2}(\mathbb{R}^{\hat{d}})). Then, for any multi-index II, there exists ℓI∈T​(ℝd^)\ell^{I}\in T(\mathbb{R}^{\hat{d}}) such that

|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝕏^t⟩=⟨ℓI,𝕏^to⟩,t∈[0,T],\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle=\langle\ell^{I},\widehat{\mathbb{X}}^{o}\_{t}\rangle,\qquad t\in[0,T], |  |

where 𝕏^o:[0,T]→G​((ℝd^))\widehat{\mathbb{X}}^{o}\colon[0,T]\to G((\mathbb{R}^{\hat{d}})) denotes the group-like valued path that is Lyons’ extension of (1,X^,𝕏^(2)+12​[𝐗^])∈Cop​-var​([0,T];G2​(ℝd^))(1,\widehat{X},\widehat{\mathbb{X}}^{(2)}+\frac{1}{2}[\widehat{\mathbf{X}}])\in C\_{o}^{p\textup{-var}}([0,T];G^{2}(\mathbb{R}^{\hat{d}})), and ℓI\ell^{I} is recursively defined by

|  |  |  |
| --- | --- | --- |
|  | ℓI:=ℓI′⊗ei|I|−12​ℓ(I′)′⊗εi|I′|​i|I|,\ell^{I}:=\ell^{I^{\prime}}\otimes e\_{i\_{|I|}}-\frac{1}{2}\ell^{(I^{\prime})^{\prime}}\otimes\varepsilon\_{i\_{|I^{\prime}|}i\_{|I|}}, |  |

with ℓ∅:=e∅\ell^{\emptyset}:=e\_{\emptyset}, ℓ(i1):=e(i1)\ell^{(i\_{1})}:=e\_{(i\_{1})}, and εi|I′|​i|I|:=0\varepsilon\_{i\_{|I^{\prime}|}i\_{|I|}}:=0, for i|I′|,i|I|∉{1,…,d}i\_{|I^{\prime}|},i\_{|I|}\notin\{1,\dots,d\}.

###### Proof.

We show the statement for t=Tt=T. For |I|=0|I|=0 and |I|=1|I|=1, considering ℓI:=eI\ell^{I}:=e\_{I}, we have that ⟨eI,𝕏^T⟩=⟨ℓI,𝕏^To⟩\langle e\_{I},\widehat{\mathbb{X}}\_{T}\rangle=\langle\ell^{I},\widehat{\mathbb{X}}^{o}\_{T}\rangle by definition of Lyons’ extension.

For |I|=2|I|=2, i.e., I=(i1,i2)I=(i\_{1},i\_{2}), i1,i2∈{0,…,d^−1}i\_{1},i\_{2}\in\{0,\ldots,\hat{d}-1\}, we obtain that ℓI=eI−12​εi1​i2\ell^{I}=e\_{I}-\frac{1}{2}\varepsilon\_{i\_{1}i\_{2}}.

Now let |I|=3|I|=3, i.e., I=(i1,i2,i3)I=(i\_{1},i\_{2},i\_{3}). Then, taking the limit along any sequence of partitions 𝒫\mathcal{P} of [0,T][0,T] with vanishing mesh size, we note that

|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝕏^T⟩\displaystyle\langle e\_{I},\widehat{\mathbb{X}}\_{T}\rangle |  |
|  |  |  |
| --- | --- | --- |
|  | =lim|𝒫|→0∑[u,v]∈𝒫(𝕏^0,u(2))i1​i2​X^u,vi3+X^0,ui1​(𝕏^u,v(2))i2​i3\displaystyle\quad=\lim\_{|\mathcal{P}|\to 0}\sum\_{[u,v]\in\mathcal{P}}(\widehat{\mathbb{X}}^{(2)}\_{0,u})^{i\_{1}i\_{2}}\widehat{X}^{i\_{3}}\_{u,v}+\widehat{X}^{i\_{1}}\_{0,u}(\widehat{\mathbb{X}}^{(2)}\_{u,v})^{i\_{2}i\_{3}} |  |
|  |  |  |
| --- | --- | --- |
|  | =lim|𝒫|→0∑[u,v]∈𝒫(𝕏^0,uo,(2))i1​i2−12[𝐗^]0,ui1​i2)X^i3u,v+X^i10,u((𝕏^u,vo,(2))i2​i3−12[𝐗^]u,vi2​i3)\displaystyle\quad=\lim\_{|\mathcal{P}|\to 0}\sum\_{[u,v]\in\mathcal{P}}(\widehat{\mathbb{X}}^{o,(2)}\_{0,u})^{i\_{1}i\_{2}}-\frac{1}{2}[\widehat{\mathbf{X}}]^{i\_{1}i\_{2}}\_{0,u})\widehat{X}^{i\_{3}}\_{u,v}+\widehat{X}^{i\_{1}}\_{0,u}((\widehat{\mathbb{X}}^{o,(2)}\_{u,v})^{i\_{2}i\_{3}}-\frac{1}{2}[\widehat{\mathbf{X}}]^{i\_{2}i\_{3}}\_{u,v}) |  |
|  |  |  |
| --- | --- | --- |
|  | =⟨eI,𝕏^To⟩−12​∫0T[𝐗^]0,ti1​i2​dX^ti3−12​∫0TX^0,ti1​d​[𝐗^]ti2​i3\displaystyle\quad=\langle e\_{I},\widehat{\mathbb{X}}^{o}\_{T}\rangle-\frac{1}{2}\int\_{0}^{T}[\widehat{\mathbf{X}}]^{i\_{1}i\_{2}}\_{0,t}\,\mathrm{d}\widehat{X}^{i\_{3}}\_{t}-\frac{1}{2}\int\_{0}^{T}\widehat{X}^{i\_{1}}\_{0,t}\,\mathrm{d}[\widehat{\mathbf{X}}]^{i\_{2}i\_{3}}\_{t} |  |
|  |  |  |
| --- | --- | --- |
|  | =⟨eI,𝕏^To⟩−12​⟨εi1​i2⊗ei3,𝕏^To⟩−12​⟨ei1⊗εi2​i3,𝕏^To⟩\displaystyle\quad=\langle e\_{I},\widehat{\mathbb{X}}^{o}\_{T}\rangle-\frac{1}{2}\langle\varepsilon\_{i\_{1}i\_{2}}\otimes e\_{i\_{3}},\widehat{\mathbb{X}}^{o}\_{T}\rangle-\frac{1}{2}\langle e\_{i\_{1}}\otimes\varepsilon\_{i\_{2}i\_{3}},\widehat{\mathbb{X}}^{o}\_{T}\rangle |  |
|  |  |  |
| --- | --- | --- |
|  | =⟨ℓI,𝕏^To⟩,\displaystyle\quad=\langle\ell^{I},\widehat{\mathbb{X}}^{o}\_{T}\rangle, |  |

for ℓI:=eI−12​εi1​i2⊗ei3−12​ei1⊗εi2​i3=ℓ(i1,i2)⊗ei3−12​ei1⊗εi2​i3\ell^{I}:=e\_{I}-\frac{1}{2}\varepsilon\_{i\_{1}i\_{2}}\otimes e\_{i\_{3}}-\frac{1}{2}e\_{i\_{1}}\otimes\varepsilon\_{i\_{2}i\_{3}}=\ell^{(i\_{1},i\_{2})}\otimes e\_{i\_{3}}-\frac{1}{2}e\_{i\_{1}}\otimes\varepsilon\_{i\_{2}i\_{3}}, where the latter two integrals exist as Young integrals because [𝐗^][\widehat{\mathbf{X}}] is a path of finite p/2p/2-variation. We apply an inductive argument: Assuming that the claim holds true for any n<Nn<N, for N>3N>3, we now let n≥Nn\geq N. Let II be a multi-index with entries in {0,…,d^−1}\{0,\dots,\hat{d}-1\} of length nn. Then,

|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝕏^T⟩\displaystyle\langle e\_{I},\widehat{\mathbb{X}}\_{T}\rangle |  |
|  |  |  |
| --- | --- | --- |
|  | =lim|𝒫|→0∑[u,v]∈𝒫⟨eI′,𝕏^u⟩​X^u,vin+⟨e(I′)′,𝕏^u⟩​(𝕏^u,v(2))in−1​in\displaystyle\quad=\lim\_{|\mathcal{P}|\to 0}\sum\_{[u,v]\in\mathcal{P}}\langle e\_{I^{\prime}},\widehat{\mathbb{X}}\_{u}\rangle\widehat{X}^{i\_{n}}\_{u,v}+\langle e\_{(I^{\prime})^{\prime}},\widehat{\mathbb{X}}\_{u}\rangle(\widehat{\mathbb{X}}^{(2)}\_{u,v})^{i\_{n-1}i\_{n}} |  |
|  |  |  |
| --- | --- | --- |
|  | =lim|𝒫|→0∑[u,v]∈𝒫⟨ℓI′,𝕏^uo⟩​X^u,vin+⟨ℓ(I′)′,𝕏^uo⟩​((𝕏^u,vo,(2))in−1​in−12​[𝐗^]u,vin−1​in)\displaystyle\quad=\lim\_{|\mathcal{P}|\to 0}\sum\_{[u,v]\in\mathcal{P}}\langle\ell^{I^{\prime}},\widehat{\mathbb{X}}^{o}\_{u}\rangle\widehat{X}^{i\_{n}}\_{u,v}+\langle\ell^{(I^{\prime})^{\prime}},\widehat{\mathbb{X}}^{o}\_{u}\rangle((\widehat{\mathbb{X}}^{o,(2)}\_{u,v})^{i\_{n-1}i\_{n}}-\frac{1}{2}[\widehat{\mathbf{X}}]\_{u,v}^{i\_{n-1}i\_{n}}) |  |
|  |  |  |
| --- | --- | --- |
|  | =lim|𝒫|→0∑[u,v]∈𝒫⟨ℓ(I′)′⊗ein−1,𝕏^uo⟩​X^u,vin−12​⟨ℓ((I′)′)′⊗εin−2​in−1,𝕏^uo⟩​X^u,vin\displaystyle\quad=\lim\_{|\mathcal{P}|\to 0}\sum\_{[u,v]\in\mathcal{P}}\langle\ell^{(I^{\prime})^{\prime}}\otimes e\_{i\_{n-1}},\widehat{\mathbb{X}}^{o}\_{u}\rangle\widehat{X}^{i\_{n}}\_{u,v}-\frac{1}{2}\langle\ell^{((I^{\prime})^{\prime})^{\prime}}\otimes\varepsilon\_{i\_{n-2}i\_{n-1}},\widehat{\mathbb{X}}^{o}\_{u}\rangle\widehat{X}^{i\_{n}}\_{u,v} |  |
|  |  |  |
| --- | --- | --- |
|  | +⟨ℓ(I′)′,𝕏^uo⟩​(𝕏^o,(2))u,vin−1​in−12​lim|𝒫|→0∑[u,v]∈𝒫⟨ℓ(I′)′,𝕏^uo⟩​[𝐗^]u,vin−1​in\displaystyle\qquad+\langle\ell^{(I^{\prime})^{\prime}},\widehat{\mathbb{X}}^{o}\_{u}\rangle(\widehat{\mathbb{X}}^{o,(2)})\_{u,v}^{i\_{n-1}i\_{n}}-\frac{1}{2}\lim\_{|\mathcal{P}|\to 0}\sum\_{[u,v]\in\mathcal{P}}\langle\ell^{(I^{\prime})^{\prime}},\widehat{\mathbb{X}}^{o}\_{u}\rangle[\widehat{\mathbf{X}}]^{i\_{n-1}i\_{n}}\_{u,v} |  |
|  |  |  |
| --- | --- | --- |
|  | =⟨ℓ(I′)′⊗ein−1⊗ein,𝕏^To⟩−12​⟨ℓ((I′)′)′⊗εin−2​in−1⊗ein,𝕏^To⟩−12​⟨ℓ(I′)′⊗εin−1​in,𝕏^To⟩\displaystyle\quad=\langle\ell^{(I^{\prime})^{\prime}}\otimes e\_{i\_{n-1}}\otimes e\_{i\_{n}},\widehat{\mathbb{X}}^{o}\_{T}\rangle-\frac{1}{2}\langle\ell^{((I^{\prime})^{\prime})^{\prime}}\otimes\varepsilon\_{i\_{n-2}i\_{n-1}}\otimes e\_{i\_{n}},\widehat{\mathbb{X}}^{o}\_{T}\rangle-\frac{1}{2}\langle\ell^{(I^{\prime})^{\prime}}\otimes\varepsilon\_{i\_{n-1}i\_{n}},\widehat{\mathbb{X}}^{o}\_{T}\rangle |  |
|  |  |  |
| --- | --- | --- |
|  | =⟨ℓI′⊗ein−12​ℓ(I′)′⊗εin−1​in,𝕏^To⟩,\displaystyle\quad=\langle\ell^{I^{\prime}}\otimes e\_{i\_{n}}-\frac{1}{2}\ell^{(I^{\prime})^{\prime}}\otimes\varepsilon\_{i\_{n-1}i\_{n}},\widehat{\mathbb{X}}^{o}\_{T}\rangle, |  |

where we again used that the integral w.r.t. [𝐗^][\widehat{\mathbf{X}}] exists as a Young integral because [𝐗^][\widehat{\mathbf{X}}] is a path of finite p/2p/2-variation.
∎

The signature of a weakly geometric rough path (1,X,𝕏o,(2))(1,X,\mathbb{X}^{o,(2)}) is a group-like valued path and therefore satisfies the shuffle property. It turns out that extending the path XX to X^\widehat{X} by the rough path bracket terms yields that the signature defined via Lyons’ extension admits the so-called quasi-shuffle property, see [[Hof00](https://arxiv.org/html/2602.05898v1#bib.bibx39)]. This allows us to prove the universal approximation theorem for the signature of non-weakly geometric rough paths in Theorem [2.8](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem8 "Theorem 2.8. ‣ 2.4. Universal approximation with signatures of general rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths").

###### Definition 2.5.

For every two multi-indices II, JJ with entries in {0,…,d^−1}\{0,\ldots,\hat{d}-1\}, we define the *quasi-shuffle product* by

|  |  |  |
| --- | --- | --- |
|  | eI​~​eJ=(eI′​~​eJ)⊗ei|I|+(eI​~​eJ′)⊗ej|J|+(eI′​~​eJ′)⊗εi|I|​j|J|,e\_{I}\widetilde{\shuffle}e\_{J}=(e\_{I^{\prime}}\widetilde{\shuffle}e\_{J})\otimes e\_{i\_{|I|}}+(e\_{I}\widetilde{\shuffle}e\_{J^{\prime}})\otimes e\_{j\_{|J|}}+(e\_{I^{\prime}}\widetilde{\shuffle}e\_{J^{\prime}})\otimes\varepsilon\_{i\_{|I|}j\_{|J|}}, |  |

with eI​~​e∅=e∅​~​eI=eIe\_{I}\widetilde{\shuffle}e\_{\emptyset}=e\_{\emptyset}\widetilde{\shuffle}e\_{I}=e\_{I}.

###### Proposition 2.6 (Quasi-shuffle property).

Let I,JI,J be two multi-indices with entries in {0,…,d^−1}\{0,\dots,\hat{d}-1\}. Let 𝐗=(X,𝕏(2))∈𝒞p​([0,T];ℝd)\mathbf{X}=(X,\mathbb{X}^{(2)})\in\mathcal{C}^{p}([0,T];\mathbb{R}^{d}), p∈(2,3)p\in(2,3), be a rough path, and X^:=(⋅,X,Q​(X))\widehat{X}:=(\cdot,X,Q(X)) be the extended path. Further, let 𝕏^\widehat{\mathbb{X}} be Lyons’ extension of (1,X^,𝕏^(2))∈Cop​-var​([0,T];T2​(ℝd^))(1,\widehat{X},\widehat{\mathbb{X}}^{(2)})\in C\_{o}^{p\textup{-var}}([0,T];T^{2}(\mathbb{R}^{\hat{d}})). Then,

|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝕏^t⟩​⟨eJ,𝕏^t⟩=⟨eI​~​eJ,𝕏^t⟩,t∈[0,T].\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle\langle e\_{J},\widehat{\mathbb{X}}\_{t}\rangle=\langle e\_{I}\widetilde{\shuffle}e\_{J},\widehat{\mathbb{X}}\_{t}\rangle,\qquad t\in[0,T]. |  |

###### Remark 2.7.

For the quasi-shuffle property to hold, we actually do not need to extend the path XX by the time-component but only by its rough path bracket terms Q​(X)Q(X).

###### Proof.

Since ⟨e∅,𝕏^⟩=1\langle e\_{\emptyset},\widehat{\mathbb{X}}\rangle=1, the statement immediately holds true for I=∅I=\emptyset or J=∅J=\emptyset. Now let |I|+|J|=2|I|+|J|=2, I,J≠∅I,J\neq\emptyset, i.e., I=(i)I=(i), J=(j)J=(j), i,j∈{0,…,d^−1}i,j\in\{0,\ldots,\hat{d}-1\}. Then, for t∈[0,T]t\in[0,T], we have by Proposition [2.4](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem4 "Proposition 2.4. ‣ 2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths") that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ei,𝕏^t⟩​⟨ej,𝕏^t⟩\displaystyle\langle e\_{i},\widehat{\mathbb{X}}\_{t}\rangle\langle e\_{j},\widehat{\mathbb{X}}\_{t}\rangle | =⟨ei,𝕏^to⟩​⟨ej,𝕏^to⟩\displaystyle=\langle e\_{i},\widehat{\mathbb{X}}^{o}\_{t}\rangle\langle e\_{j},\widehat{\mathbb{X}}^{o}\_{t}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨ei​ej,𝕏^to⟩\displaystyle=\langle e\_{i}\shuffle e\_{j},\widehat{\mathbb{X}}^{o}\_{t}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨e(i,j),𝕏^to⟩+⟨e(j,i),𝕏^to⟩\displaystyle=\langle e\_{(i,j)},\widehat{\mathbb{X}}^{o}\_{t}\rangle+\langle e\_{(j,i)},\widehat{\mathbb{X}}^{o}\_{t}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨e(i,j),𝕏^t⟩+12​⟨εi​j,𝕏^t⟩+⟨e(j,i),𝕏^t⟩+12​⟨εj​i,𝕏^t⟩\displaystyle=\langle e\_{(i,j)},\widehat{\mathbb{X}}\_{t}\rangle+\frac{1}{2}\langle\varepsilon\_{ij},\widehat{\mathbb{X}}\_{t}\rangle+\langle e\_{(j,i)},\widehat{\mathbb{X}}\_{t}\rangle+\frac{1}{2}\langle\varepsilon\_{ji},\widehat{\mathbb{X}}\_{t}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨(ei​~​e∅)⊗ej,𝕏^t⟩+⟨(e∅​~​ej)⊗ei,𝕏^t⟩+⟨(e∅​~​e∅)⊗εi​j,𝕏^t⟩\displaystyle=\langle(e\_{i}\widetilde{\shuffle}e\_{\emptyset})\otimes e\_{j},\widehat{\mathbb{X}}\_{t}\rangle+\langle(e\_{\emptyset}\widetilde{\shuffle}e\_{j})\otimes e\_{i},\widehat{\mathbb{X}}\_{t}\rangle+\langle(e\_{\emptyset}\widetilde{\shuffle}e\_{\emptyset})\otimes\varepsilon\_{ij},\widehat{\mathbb{X}}\_{t}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨ei​~​ej,𝕏^t⟩,\displaystyle=\langle e\_{i}\widetilde{\shuffle}e\_{j},\widehat{\mathbb{X}}\_{t}\rangle, |  |

where we note that εj​i=εi​j\varepsilon\_{ji}=\varepsilon\_{ij} for i≤ji\leq j, and εi​j=0\varepsilon\_{ij}=0 for i,j∉{1,…,d}.i,j\notin\{1,\dots,d\}.

We apply an inductive argument: We assume that the claim holds true for any I,JI,J such that |I|+|J|<n|I|+|J|<n, n>2n>2 and let I,JI,J be such that |I|+|J|≤n|I|+|J|\leq n, I,J≠∅I,J\neq\emptyset.

We start by noting that ⟨eI,𝕏^⟩\langle e\_{I},\widehat{\mathbb{X}}\rangle is a controlled path w.r.t. X^\widehat{X}.

We consider (Y,Y′)∈𝒞X^p(Y,Y^{\prime})\in\mathscr{C}^{p}\_{\widehat{X}} to be the controlled path given by Y∈Cp​-var​([0,T];ℒ​(ℝd^;ℝ2))Y\in C^{p\textup{-var}}([0,T];\mathcal{L}(\mathbb{R}^{\hat{d}};\mathbb{R}^{2})), where

|  |  |  |
| --- | --- | --- |
|  | Ym​n={⟨eI′,𝕏^⟩,if ​m=1,n=i|I|,⟨eJ′,𝕏^⟩,if ​m=2,n=j|J|,0,otherwise.Y^{mn}=\begin{cases}\langle e\_{I^{\prime}},\widehat{\mathbb{X}}\rangle,&\text{if }m=1,\,n=i\_{|I|},\\ \langle e\_{J^{\prime}},\widehat{\mathbb{X}}\rangle,&\text{if }m=2,\,n=j\_{|J|},\\ 0,&\text{otherwise}.\end{cases} |  |

Since 𝕏^tN:=∫0t𝕏^rN−1⊗d𝐗^r\widehat{\mathbb{X}}^{N}\_{t}:=\int\_{0}^{t}\widehat{\mathbb{X}}^{N-1}\_{r}\otimes\mathrm{d}\widehat{\mathbf{X}}\_{r} is a rough integral against 𝐗^=(X^,𝕏^(2))∈𝒞p​([0,T];ℝd^)\widehat{\mathbf{X}}=(\widehat{X},\widehat{\mathbb{X}}^{(2)})\in\mathcal{C}^{p}([0,T];\mathbb{R}^{\hat{d}}), the projection onto the tensor product (ℝd)⊗N(\mathbb{R}^{d})^{\otimes N}, ΠN​(𝕏^N)\Pi\_{N}(\widehat{\mathbb{X}}^{N}), is the rough integral of the controlled path (ΠN−1​(𝕏^N),ΠN−2​(𝕏^N))(\Pi\_{N-1}(\widehat{\mathbb{X}}^{N}),\Pi\_{N-2}(\widehat{\mathbb{X}}^{N})) against 𝐗^\widehat{\mathbf{X}}. That is, for any multi-index II, we have that

|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝕏^t⟩=lim|𝒫|→0∑[u,v]∈𝒫∩[0,t]⟨eI′,𝕏^u⟩​Xu,vi|I|+⟨e(I′)′,𝕏^u⟩​𝕏^u,v(2),i|I′|​i|I|.\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle=\lim\_{|\mathcal{P}|\to 0}\sum\_{[u,v]\in\mathcal{P}\cap[0,t]}\langle e\_{I^{\prime}},\widehat{\mathbb{X}}\_{u}\rangle X^{i\_{|I|}}\_{u,v}+\langle e\_{(I^{\prime})^{\prime}},\widehat{\mathbb{X}}\_{u}\rangle\widehat{\mathbb{X}}^{(2),i\_{|I^{\prime}|}i\_{|I|}}\_{u,v}. |  |

Particularly, it then is Yt′∈ℒ​(ℝd;ℒ​(ℝd;ℝ2))Y^{\prime}\_{t}\in\mathcal{L}(\mathbb{R}^{d};\mathcal{L}(\mathbb{R}^{d};\mathbb{R}^{2})), given by (Yt′)1​i​j=⟨e(I′)′,𝕏^t⟩(Y^{\prime}\_{t})^{1ij}=\langle e\_{(I^{\prime})^{\prime}},\widehat{\mathbb{X}}\_{t}\rangle for i=i|I′|i=i\_{|I^{\prime}|}, j=i|I|j=i\_{|I|}, and (Yt′)2​i​j=⟨e(J′)′,𝕏^t⟩(Y^{\prime}\_{t})^{2ij}=\langle e\_{(J^{\prime})^{\prime}},\widehat{\mathbb{X}}\_{t}\rangle for i=j|J′|i=j\_{|J^{\prime}|}, j=j|J|j=j\_{|J|}, (Yt′)m​i​j=0(Y^{\prime}\_{t})^{mij}=0 otherwise, m=1,2m=1,2, i,j=0,…,d^−1i,j=0,\dots,\hat{d}-1. This gives us that

|  |  |  |
| --- | --- | --- |
|  | Zt=lim|𝒫|→0∑[u,v]∈𝒫∩[0,t]Yu​Xu,v+Yu′​𝕏^u,v(2)=lim|𝒫|→0∑[u,v]∈𝒫∩[0,t]𝒵u,v,\displaystyle Z\_{t}=\lim\_{|\mathcal{P}|\to 0}\sum\_{[u,v]\in\mathcal{P}\cap[0,t]}Y\_{u}X\_{u,v}+Y^{\prime}\_{u}\widehat{\mathbb{X}}^{(2)}\_{u,v}=\lim\_{|\mathcal{P}|\to 0}\sum\_{[u,v]\in\mathcal{P}\cap[0,t]}\mathcal{Z}\_{u,v}, |  |

with

|  |  |  |
| --- | --- | --- |
|  | 𝒵u,v:=(⟨eI′,𝕏^u⟩​Xu,vi|I|+⟨e(I′)′,𝕏^u⟩​𝕏^u,v(2),i|I′|​i|I|,⟨eJ′,𝕏^u⟩​Xu,vj|J|+⟨e(J′)′,𝕏^u⟩​𝕏^u,v(2),j|J′|​j|J|)⊤,\mathcal{Z}\_{u,v}:=(\langle e\_{I^{\prime}},\widehat{\mathbb{X}}\_{u}\rangle X^{i\_{|I|}}\_{u,v}+\langle e\_{(I^{\prime})^{\prime}},\widehat{\mathbb{X}}\_{u}\rangle\widehat{\mathbb{X}}^{(2),i\_{|I^{\prime}|}i\_{|I|}}\_{u,v},\langle e\_{J^{\prime}},\widehat{\mathbb{X}}\_{u}\rangle X^{j\_{|J|}}\_{u,v}+\langle e\_{(J^{\prime})^{\prime}},\widehat{\mathbb{X}}\_{u}\rangle\widehat{\mathbb{X}}^{(2),j\_{|J^{\prime}|}j\_{|J|}}\_{u,v})^{\top}, |  |

where we have used that (Yu′​𝕏^u,v(2))m=∑i∑j(Yu′)m​i​j​𝕏^u,v(2),i​j(Y^{\prime}\_{u}\widehat{\mathbb{X}}^{(2)}\_{u,v})^{m}=\sum\_{i}\sum\_{j}(Y^{\prime}\_{u})^{mij}\widehat{\mathbb{X}}\_{u,v}^{(2),ij}.

Then, Z:=∫Y​d𝐗^Z:=\int Y\,\mathrm{d}\widehat{\mathbf{X}} is the rough integral of YY against 𝐗^\widehat{\mathbf{X}}, which equals Z=(Z1,Z2)⊤=(⟨eI,𝕏^⟩,⟨eJ,𝕏^⟩)⊤Z=(Z^{1},Z^{2})^{\top}=(\langle e\_{I},\widehat{\mathbb{X}}\rangle,\langle e\_{J},\widehat{\mathbb{X}}\rangle)^{\top}.

As a controlled path, ZZ can now be canonically lifted to a rough path 𝐙=(Z,ℤ)\mathbf{Z}=(Z,\mathbb{Z}), with ℤs,t:=∫stZr⊗Zr−Zs⊗Zs,t\mathbb{Z}\_{s,t}:=\int\_{s}^{t}Z\_{r}\otimes Z\_{r}-Z\_{s}\otimes Z\_{s,t}, (s,t)∈ΔT(s,t)\in\Delta\_{T}, where the integral is defined as in Lemma [D.1](https://arxiv.org/html/2602.05898v1#A4.Thmtheorem1 "Lemma D.1 (Proposition 2.4 in [ALP24]). ‣ Appendix D Some additional results in rough path theory ‣ Universal approximation with signatures of non-geometric rough paths").

Using the Itô-formula for rough paths, see e.g. [[FH20](https://arxiv.org/html/2602.05898v1#bib.bibx29), Proposition 5.8], for f​(Z)=Z1⋅Z2f(Z)=Z^{1}\cdot Z^{2}, we thus obtain that

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | ⟨eI,𝕏^t⟩​⟨eJ,𝕏^t⟩=∫0t(Z2,Z1)r​d𝐙r+12​[𝐙]t12+12​[𝐙]t21=∫0t(Z2,Z1)r​dZr+[𝐙]t12,\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle\langle e\_{J},\widehat{\mathbb{X}}\_{t}\rangle=\int\_{0}^{t}(Z^{2},Z^{1})\_{r}\,\mathrm{d}\mathbf{Z}\_{r}+\frac{1}{2}[\mathbf{Z}]^{12}\_{t}+\frac{1}{2}[\mathbf{Z}]^{21}\_{t}=\int\_{0}^{t}(Z^{2},Z^{1})\_{r}\,\mathrm{d}Z\_{r}+[\mathbf{Z}]^{12}\_{t}, |  |

where the latter integral is well defined as a rough integral against the controlled path (Z,Y)(Z,Y), see also [[ACLP23](https://arxiv.org/html/2602.05898v1#bib.bibx1), Lemma A.4].

Due to the associativity of the rough integral, see [[ACLP23](https://arxiv.org/html/2602.05898v1#bib.bibx1), Proposition A.2], we have

|  |  |  |  |
| --- | --- | --- | --- |
| (2.2) |  | ∫0t(Z2,Z1)r​dZr=∫0t(Z2,Z1)r​Yr​d𝐗^r=∫0t(0,…,0,⟨eJ,𝕏^r⟩​⟨eI′,𝕏^r⟩,0,…,0,⟨eI,𝕏^r⟩​⟨eJ′,𝕏^r⟩,0,…,0)​d𝐗^r=∫0t(0,…,0,⟨eJ​~​eI′,𝕏^r⟩,0,…,0,⟨eI​~​eJ′,𝕏^r⟩,0,…,0)​d𝐗^r=⟨(eJ​~​eI′)⊗ei|I|,𝕏^t⟩+⟨(eI​~​eJ′)⊗ej|J|,𝕏^t⟩,\begin{split}\int\_{0}^{t}(Z^{2},Z^{1})\_{r}\,\mathrm{d}Z\_{r}&=\int\_{0}^{t}(Z^{2},Z^{1})\_{r}Y\_{r}\,\mathrm{d}\widehat{\mathbf{X}}\_{r}\\ &=\int\_{0}^{t}(0,\dots,0,\langle e\_{J},\widehat{\mathbb{X}}\_{r}\rangle\langle e\_{I^{\prime}},\widehat{\mathbb{X}}\_{r}\rangle,0,\dots,0,\langle e\_{I},\widehat{\mathbb{X}}\_{r}\rangle\langle e\_{J^{\prime}},\widehat{\mathbb{X}}\_{r}\rangle,0,\dots,0)\,\mathrm{d}\widehat{\mathbf{X}}\_{r}\\ &=\int\_{0}^{t}(0,\dots,0,\langle e\_{J}\widetilde{\shuffle}e\_{I^{\prime}},\widehat{\mathbb{X}}\_{r}\rangle,0,\dots,0,\langle e\_{I}\widetilde{\shuffle}e\_{J^{\prime}},\widehat{\mathbb{X}}\_{r}\rangle,0,\dots,0)\,\mathrm{d}\widehat{\mathbf{X}}\_{r}\\ &=\langle(e\_{J}\widetilde{\shuffle}e\_{I^{\prime}})\otimes e\_{i\_{|I|}},\widehat{\mathbb{X}}\_{t}\rangle+\langle(e\_{I}\widetilde{\shuffle}e\_{J^{\prime}})\otimes e\_{j\_{|J|}},\widehat{\mathbb{X}}\_{t}\rangle,\end{split} |  |

where we used the induction hypothesis in the second last step.

By definition, it holds that eJ​~​eI′=(eJ​~​e(I′)′)⊗ei|I′|+(eJ′​~​eI′)⊗ej|J|+(eJ′​~​e(I′)′)⊗εj|J|​i|I′|e\_{J}\widetilde{\shuffle}e\_{I^{\prime}}=(e\_{J}\widetilde{\shuffle}e\_{(I^{\prime})^{\prime}})\otimes e\_{i\_{|I^{\prime}|}}+(e\_{J^{\prime}}\widetilde{\shuffle}e\_{I^{\prime}})\otimes e\_{j\_{|J|}}+(e\_{J^{\prime}}\widetilde{\shuffle}e\_{(I^{\prime})^{\prime}})\otimes\varepsilon\_{j\_{|J|}i\_{|I^{\prime}|}}. So setting Ut:=(0,…,0,⟨eJ​~​eI′,𝕏^t⟩,0,…,0,⟨eI​~​eJ′,𝕏^t⟩,0,…,0)U\_{t}:=(0,\dots,0,\langle e\_{J}\widetilde{\shuffle}e\_{I^{\prime}},\widehat{\mathbb{X}}\_{t}\rangle,0,\dots,0,\langle e\_{I}\widetilde{\shuffle}e\_{J^{\prime}},\widehat{\mathbb{X}}\_{t}\rangle,0,\dots,0), we observe that Ut′∈ℒ​(ℝd^;ℒ​(ℝd^;ℝ))U^{\prime}\_{t}\in\mathcal{L}(\mathbb{R}^{\hat{d}};\mathcal{L}(\mathbb{R}^{\hat{d}};\mathbb{R})), given by (Ut′)i|I′|​j=⟨eJ​~​e(I′)′,𝕏^t⟩(U^{\prime}\_{t})^{i\_{|I^{\prime}|}j}=\langle e\_{J}\widetilde{\shuffle}e\_{(I^{\prime})^{\prime}},\widehat{\mathbb{X}}\_{t}\rangle, (Ut′)j|J|​j=⟨eJ′​~​eI′,𝕏^t⟩(U^{\prime}\_{t})^{j\_{|J|}j}=\langle e\_{J^{\prime}}\widetilde{\shuffle}e\_{I^{\prime}},\widehat{\mathbb{X}}\_{t}\rangle, and (Ut′)k​j=⟨eJ′​~​e(I′)′,𝕏^t⟩(U^{\prime}\_{t})^{kj}=\langle e\_{J^{\prime}}\widetilde{\shuffle}e\_{(I^{\prime})^{\prime}},\widehat{\mathbb{X}}\_{t}\rangle, for kk such that ek=εj|J|​i|I′|e\_{k}=\varepsilon\_{j\_{|J|}i\_{|I^{\prime}|}}, for j=i|I|j=i\_{|I|}. Similarly for j=j|J|j=j\_{|J|}, and otherwise it is (Ut′)i​j=0(U^{\prime}\_{t})^{ij}=0. By a similar line of argument as above, it then follows the last step.

Further, by [[ACLP23](https://arxiv.org/html/2602.05898v1#bib.bibx1), Lemma B.1], we have that222In writing Yu⊗YuY\_{u}\otimes Y\_{u}, we technically mean the 44-tensor whose i​j​k​ℓijk\ell component is given by [Yu⊗Yu]i​j​k​ℓ=(Yu)i​j​(Yu)k​ℓ[Y\_{u}\otimes Y\_{u}]^{ijk\ell}=(Y\_{u})^{ij}(Y\_{u})^{k\ell}, and we interpret the “multiplication” (Yu⊗Yu)​[𝐗^]u,v(Y\_{u}\otimes Y\_{u})[\widehat{\mathbf{X}}]\_{u,v} as the matrix whose i​kik component is given by [(Yu⊗Yu)[𝐗^]u,vi​k=∑j=1d∑ℓ=1d(Yu)i​j(Yu)k​ℓ[𝐗^]u,vj​ℓ[(Y\_{u}\otimes Y\_{u})[\widehat{\mathbf{X}}]\_{u,v}^{ik}=\sum\_{j=1}^{d}\sum\_{\ell=1}^{d}(Y\_{u})^{ij}(Y\_{u})^{k\ell}[\widehat{\mathbf{X}}]^{j\ell}\_{u,v}.

|  |  |  |
| --- | --- | --- |
|  | [𝐙]t=∫0t(Yr⊗Yr)​d​[𝐗^]r=lim|𝒫|→0∑[u,v]∈𝒫(Yu⊗Yu)​[𝐗^]u,v,[\mathbf{Z}]\_{t}=\int\_{0}^{t}(Y\_{r}\otimes Y\_{r})\,\mathrm{d}[\widehat{\mathbf{X}}]\_{r}=\lim\_{|\mathcal{P}|\to 0}\sum\_{[u,v]\in\mathcal{P}}(Y\_{u}\otimes Y\_{u})[\widehat{\mathbf{X}}]\_{u,v}, |  |

and by definition of YY, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
| (2.3) |  | [𝐙]t12=[𝐙]t21=∫0t⟨eI′,𝕏^r⟩​⟨eJ′,𝕏^r⟩​d​[𝐗^]ri|I|​j|J|=⟨(eI′​~​eJ′)⊗εi|I|​j|J|,𝕏^t⟩,[\mathbf{Z}]\_{t}^{12}=[\mathbf{Z}]\_{t}^{21}=\int\_{0}^{t}\langle e\_{I^{\prime}},\widehat{\mathbb{X}}\_{r}\rangle\langle e\_{J^{\prime}},\widehat{\mathbb{X}}\_{r}\rangle\,\mathrm{d}[\widehat{\mathbf{X}}]^{i\_{|I|}j\_{|J|}}\_{r}=\langle(e\_{I^{\prime}}\widetilde{\shuffle}e\_{J^{\prime}})\otimes\varepsilon\_{i\_{|I|}j\_{|J|}},\widehat{\mathbb{X}}\_{t}\rangle, |  |

where we again used the induction hypothesis in the last step.

Finally, combining ([2.1](https://arxiv.org/html/2602.05898v1#S2.E1 "In Proof. ‣ 2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths")), ([2.2](https://arxiv.org/html/2602.05898v1#S2.E2 "In Proof. ‣ 2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths")) and ([2.3](https://arxiv.org/html/2602.05898v1#S2.E3 "In Proof. ‣ 2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths")), yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨eI,𝕏^t⟩​⟨eJ,𝕏^t⟩\displaystyle\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle\langle e\_{J},\widehat{\mathbb{X}}\_{t}\rangle | =⟨(eJ​~​eI′)⊗ei|I|,𝕏^t⟩+⟨(eI​~​eJ′)⊗ej|J|,𝕏^t⟩+⟨(eI′​~​eJ′)⊗εi|I|​j|J|,𝕏^t⟩\displaystyle=\langle(e\_{J}\widetilde{\shuffle}e\_{I^{\prime}})\otimes e\_{i\_{|I|}},\widehat{\mathbb{X}}\_{t}\rangle+\langle(e\_{I}\widetilde{\shuffle}e\_{J^{\prime}})\otimes e\_{j\_{|J|}},\widehat{\mathbb{X}}\_{t}\rangle+\langle(e\_{I^{\prime}}\widetilde{\shuffle}e\_{J^{\prime}})\otimes\varepsilon\_{i\_{|I|}j\_{|J|}},\widehat{\mathbb{X}}\_{t}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨eI​~​eJ,𝕏^t⟩.\displaystyle=\langle e\_{I}\widetilde{\shuffle}e\_{J},\widehat{\mathbb{X}}\_{t}\rangle. |  |

∎

### 2.4. Universal approximation with signatures of general rough paths

We now present the pathwise universal approximation theorem of the signature of a general, i.e., not necessarily, weakly geometric rough path via Lyons’ lift, as an extension of the classical result to a more general class of signatures. The proof is based on an application of the Stone–Weierstrass theorem, which requires that the linear span of the signature forms an algebra, making use of the quasi shuffle property. For this, we formulate the universal approximation theorem on the subspace of rough paths extended by time and the rough path bracket terms, defined by

|  |  |  |
| --- | --- | --- |
|  | 𝒞^p​([0,T];ℝd^):={(X^,𝕏^(2))∈𝒞p​([0,T];ℝd^):(X,𝕏(2))∈𝒞p​([0,T];ℝd),X^=(⋅,X,Q​(X))}.\widehat{\mathcal{C}}^{p}([0,T];\mathbb{R}^{\hat{d}}):=\{(\widehat{X},\widehat{\mathbb{X}}^{(2)})\in\mathcal{C}^{p}([0,T];\mathbb{R}^{\hat{d}}):(X,\mathbb{X}^{(2)})\in\mathcal{C}^{p}([0,T];\mathbb{R}^{d}),\widehat{X}=(\cdot,X,Q(X))\}. |  |

###### Theorem 2.8.

Let p∈(2,3)p\in(2,3), and let K⊂𝒞^p​([0,T];ℝd^)K\subset\widehat{\mathcal{C}}^{p}([0,T];\mathbb{R}^{\hat{d}}) be a compact subset, bounded with respect to the rough path norm, and consider a continuous function f:K→ℝf\colon K\to\mathbb{R}. Further for some L>0L>0, let KL⊂KK\_{L}\subset K be the subset defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | KL:={𝐗^=(X^,𝕏^(2))∈K:\displaystyle K\_{L}:=\{\widehat{\mathbf{X}}=(\widehat{X},\widehat{\mathbb{X}}^{(2)})\in K:\, | ∥(X^,𝕏^(2))∥p+∥[𝐗^]∥p2≤L}.\displaystyle\|(\widehat{X},\widehat{\mathbb{X}}^{(2)})\|\_{p}+\|[\widehat{\mathbf{X}}]\|\_{\frac{p}{2}}\leq L\}. |  |

Then, for every ε>0\varepsilon>0, there exists a linear functional ℓ∈T​(ℝd^)\ell\in T(\mathbb{R}^{\hat{d}}) such that

|  |  |  |
| --- | --- | --- |
|  | sup𝐗^∈KL|f​(𝐗^)−⟨ℓ,𝕏^T⟩|<ε,\sup\_{\widehat{\mathbf{X}}\in K\_{L}}|f(\widehat{\mathbf{X}})-\langle\ell,\widehat{\mathbb{X}}\_{T}\rangle|<\varepsilon, |  |

where 𝕏^\widehat{\mathbb{X}} denotes the signature of 𝐗^\widehat{\mathbf{X}} given by Lyons’ extension theorem to T​((ℝd^))T((\mathbb{R}^{\hat{d}})).

###### Proof.

The result follows by an application of the Stone–Weierstrass theorem to the set

|  |  |  |
| --- | --- | --- |
|  | 𝒜:=span⁡{KL∋𝐗^↦⟨eI,𝕏^T⟩∈ℝ:I∈{0,…,d^−1}N,N∈ℕ0}.\mathcal{A}:=\operatorname{span}\{K\_{L}\ni\widehat{\mathbf{X}}\mapsto\langle e\_{I},\widehat{\mathbb{X}}\_{T}\rangle\in\mathbb{R}:I\in\{0,\ldots,\hat{d}-1\}^{N},N\in\mathbb{N}\_{0}\}. |  |

Therefore we have to show that 𝒜\mathcal{A}

1. (i)

   is a vector subspace of C​(KL;ℝ)C(K\_{L};\mathbb{R}),
2. (ii)

   is a subalgebra and contains a non-zero constant function, and
3. (iii)

   separates points.

*(i):* First, we note that any rough path 𝐗^=(X^,𝕏^(2))∈𝒞p​([0,T];ℝd^)\widehat{\mathbf{X}}=(\widehat{X},\widehat{\mathbb{X}}^{(2)})\in\mathcal{C}^{p}([0,T];\mathbb{R}^{\hat{d}}) canonically extends to a weakly geometric rough path via

|  |  |  |  |
| --- | --- | --- | --- |
|  | ι:𝐗^↦𝕏^o,2\displaystyle\iota\colon\widehat{\mathbf{X}}\mapsto\widehat{\mathbb{X}}^{o,2} | :=(1,X^0,⋅,𝕏^0,⋅o,(2))\displaystyle:=(1,\widehat{X}\_{0,\cdot},\mathbb{\widehat{X}}^{o,(2)}\_{0,\cdot}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | :=(1,X^0,⋅,𝕏^0,⋅(2)+12​[𝐗^]),\displaystyle:=(1,\widehat{X}\_{0,\cdot},\mathbb{\widehat{X}}^{(2)}\_{0,\cdot}+\frac{1}{2}[\widehat{\mathbf{X}}]), |  |

that is, ι​(𝐗^)∈(Cop​-var​([0,T];G2​(ℝd^)),dp​-var)\iota(\widehat{\mathbf{X}})\in(C\_{o}^{p\textup{-var}}([0,T];G^{2}(\mathbb{R}^{\hat{d}})),d\_{p\textup{-var}}). Further, we observe that for any 𝐗^∈KL\widehat{\mathbf{X}}\in K\_{L}, it holds that

|  |  |  |
| --- | --- | --- |
|  | ‖𝕏^o,(2)‖p2≤‖𝕏^(2)‖p2+‖[𝐗^]‖p2≤L,\|\widehat{\mathbb{X}}^{o,(2)}\|\_{\frac{p}{2}}\leq\|\widehat{\mathbb{X}}^{(2)}\|\_{\frac{p}{2}}+\|[\widehat{\mathbf{X}}]\|\_{\frac{p}{2}}\leq L, |  |

thus we can embed KLK\_{L} into ι​(KL):={ι​(𝐗^):𝐗^∈KL}\iota(K\_{L}):=\{\iota(\widehat{\mathbf{X}}):\widehat{\mathbf{X}}\in K\_{L}\}, which is a subset of the compact set KL2:={𝕏^o,2:∥𝟏;𝕏^o,2∥p≤L}K\_{L}^{2}:=\{\widehat{\mathbb{X}}^{o,2}:\|\mathbf{1};\widehat{\mathbb{X}}^{o,2}\|\_{p}\leq L\} of Cop​-var​([0,T];G2​(ℝd^))C\_{o}^{p\textup{-var}}([0,T];G^{2}(\mathbb{R}^{\hat{d}})).

Because

|  |  |  |
| --- | --- | --- |
|  | (𝒞p([0,T];ℝd^),dp,p2​-var)∋𝐗^↦[𝐗^]∈(Cp2​-var([0,T];ℝd^),∥⋅;⋅∥p2)(\mathcal{C}^{p}([0,T];\mathbb{R}^{\hat{d}}),d\_{p,\frac{p}{2}\textup{-var}})\ni\widehat{\mathbf{X}}\mapsto[\widehat{\mathbf{X}}]\in(C^{\frac{p}{2}\textup{-var}}([0,T];\mathbb{R}^{\hat{d}}),\|\cdot\,;\cdot\|\_{\frac{p}{2}}) |  |

is continuous with respect to dp,p2​-var:=∥⋅−⋅∥p+∥⋅−⋅∥p2d\_{p,\frac{p}{2}\textup{-var}}:=\|\cdot-\cdot\|\_{p}+\|\cdot-\cdot\|\_{\frac{p}{2}}, see Proposition [D.4](https://arxiv.org/html/2602.05898v1#A4.Thmtheorem4 "Proposition D.4. ‣ Appendix D Some additional results in rough path theory ‣ Universal approximation with signatures of non-geometric rough paths"), we notice that

|  |  |  |
| --- | --- | --- |
|  | (K,dp,p2​-var)∋𝐗^=(X^,𝕏^(2))↦(1,X^0,⋅,𝕏^0,⋅(2)+12​[𝐗^])∈(Cop​-var​([0,T];T2​(ℝd^)),dp​-var)(K,d\_{p,\frac{p}{2}\textup{-var}})\ni\widehat{\mathbf{X}}=(\widehat{X},\widehat{\mathbb{X}}^{(2)})\mapsto(1,\widehat{X}\_{0,\cdot},\widehat{\mathbb{X}}^{(2)}\_{0,\cdot}+\frac{1}{2}[\widehat{\mathbf{X}}])\in(C\_{o}^{p\textup{-var}}([0,T];T^{2}(\mathbb{R}^{\hat{d}})),d\_{p\textup{-var}}) |  |

is continuous so that

|  |  |  |
| --- | --- | --- |
|  | (KL,dp,p2​-var)∋𝐗^=(X^,𝕏^(2))↦𝕏^o,2∈(ι​(KL),dp​-var)(K\_{L},d\_{p,\frac{p}{2}\textup{-var}})\ni\widehat{\mathbf{X}}=(\widehat{X},\widehat{\mathbb{X}}^{(2)})\mapsto\widehat{\mathbb{X}}^{o,2}\in(\iota(K\_{L}),d\_{p\textup{-var}}) |  |

is continuous. By [[FV10](https://arxiv.org/html/2602.05898v1#bib.bibx32), Corollary 9.11], the map 𝕏^o,2↦⟨eI,𝕏^To⟩\widehat{\mathbb{X}}^{o,2}\mapsto\langle e\_{I},\widehat{\mathbb{X}}^{o}\_{T}\rangle is continuous on bounded sets for every multi-index II with respect to dp​-vard\_{p\textup{-var}}. More precisely, the map

|  |  |  |
| --- | --- | --- |
|  | (ι​(KL),dp​-var)∋𝕏^o,2↦𝕏^o,N∈(Cop​-var​([0,T];GN​(ℝd^)),dp​-var),(\iota(K\_{L}),d\_{p\textup{-var}})\ni\widehat{\mathbb{X}}^{o,2}\mapsto\widehat{\mathbb{X}}^{o,N}\in(C\_{o}^{p\textup{-var}}([0,T];G^{N}(\mathbb{R}^{\hat{d}})),d\_{p\textup{-var}}), |  |

is continuous with respect to dp​-vard\_{p\textup{-var}}, for every N≥3N\geq 3. Moreover, the evaluation map

|  |  |  |
| --- | --- | --- |
|  | (Cop​-var​([0,T];GN​(ℝd^)),dp​-var)∋𝕏^o,N↦𝕏^To,N∈(GN​(ℝd^),ρ)(C\_{o}^{p\textup{-var}}([0,T];G^{N}(\mathbb{R}^{\hat{d}})),d\_{p\textup{-var}})\ni\widehat{\mathbb{X}}^{o,N}\mapsto\widehat{\mathbb{X}}^{o,N}\_{T}\in(G^{N}(\mathbb{R}^{\hat{d}}),\rho) |  |

is continuous, where ρ\rho denotes the metric induced by the norm on T1N​(ℝd^)T\_{1}^{N}(\mathbb{R}^{\hat{d}}). Here, we used that we can equip GN​(ℝd^)G^{N}(\mathbb{R}^{\hat{d}}) with the metric ρ\rho, see e.g. [[FV10](https://arxiv.org/html/2602.05898v1#bib.bibx32), Remark 7.31].

Since 𝕏^To,N↦⟨eI,𝕏^To⟩\widehat{\mathbb{X}}^{o,N}\_{T}\mapsto\langle e\_{I},\widehat{\mathbb{X}}^{o}\_{T}\rangle is continuous for any multi-index II, we can thus conclude that the map

|  |  |  |
| --- | --- | --- |
|  | (GN​(ℝd^),ρ)∋𝕏^To,N↦⟨eI,𝕏^To⟩∈ℝ(G^{N}(\mathbb{R}^{\hat{d}}),\rho)\ni\widehat{\mathbb{X}}^{o,N}\_{T}\mapsto\langle e\_{I},\widehat{\mathbb{X}}\_{T}^{o}\rangle\in\mathbb{R} |  |

is continuous, and so is

|  |  |  |
| --- | --- | --- |
|  | (KL,dp,p2​-var)∋𝐗^=(X^,𝕏^(2))↦⟨eI,𝕏^To⟩∈ℝ.(K\_{L},d\_{p,\frac{p}{2}\textup{-var}})\ni\widehat{\mathbf{X}}=(\widehat{X},\widehat{\mathbb{X}}^{(2)})\mapsto\langle e\_{I},\widehat{\mathbb{X}}^{o}\_{T}\rangle\in\mathbb{R}. |  |

By Proposition [2.4](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem4 "Proposition 2.4. ‣ 2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths"), for every multi-index I∈{0,…,d^−1}NI\in\{0,\ldots,\hat{d}-1\}^{N}, N∈ℕ0N\in\mathbb{N}\_{0}, there exists ℓI∈T​(ℝd^)\ell^{I}\in T(\mathbb{R}^{\hat{d}}) such that ⟨eI,𝕏^T⟩=⟨ℓI,𝕏^To⟩\langle e\_{I},\widehat{\mathbb{X}}\_{T}\rangle=\langle\ell^{I},\widehat{\mathbb{X}}^{o}\_{T}\rangle. This finally yields that

|  |  |  |
| --- | --- | --- |
|  | (KL,dp,p2​-var)∋𝐗^↦⟨eI,𝕏^T⟩∈ℝ(K\_{L},d\_{p,\frac{p}{2}\textup{-var}})\ni\widehat{\mathbf{X}}\mapsto\langle e\_{I},\widehat{\mathbb{X}}\_{T}\rangle\in\mathbb{R} |  |

is continuous with respect to dp,p2​-vard\_{p,\frac{p}{2}\textup{-var}}.

*(ii):* By Proposition [2.6](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem6 "Proposition 2.6 (Quasi-shuffle property). ‣ 2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths"), the quasi-shuffle property holds and thus 𝒜\mathcal{A} is a subalgebra. Moreover, since ⟨e∅,𝕏^T⟩=1\langle e\_{\emptyset},\widehat{\mathbb{X}}\_{T}\rangle=1, it contains a non-zero constant function.

*(iii):* For the point separation, let us consider 𝐗^=(X^,𝕏^(2))\widehat{\mathbf{X}}=(\widehat{X},\widehat{\mathbb{X}}^{(2)}), 𝐘^=(Y^,𝕐^(2))∈KL\widehat{\mathbf{Y}}=(\widehat{Y},\widehat{\mathbb{Y}}^{(2)})\in K\_{L}, with 𝐗^≠𝐘^\widehat{\mathbf{X}}\neq\widehat{\mathbf{Y}}. We show that there exists a k∈ℕk\in\mathbb{N}, I∈{0,…,d^−1}NI\in\{0,\ldots,\hat{d}-1\}^{N}, N∈{0,1,2}N\in\{0,1,2\}, such that

|  |  |  |
| --- | --- | --- |
|  | ⟨(eI​e0⊗k)⊗e0,𝕏^T⟩≠⟨(eI​e0⊗k)⊗e0,𝕐^T⟩.\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{X}}\_{T}\rangle\neq\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{Y}}\_{T}\rangle. |  |

We proceed with a proof by contradiction. Assume that for all k∈ℕk\in\mathbb{N}, I∈{0,…,d^−1}NI\in\{0,\ldots,\hat{d}-1\}^{N}, N∈{0,1,2}N\in\{0,1,2\}, we have

|  |  |  |
| --- | --- | --- |
|  | ⟨(eI​e0⊗k)⊗e0,𝕏^T⟩=⟨(eI​e0⊗k)⊗e0,𝕐^T⟩.\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{X}}\_{T}\rangle=\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{Y}}\_{T}\rangle. |  |

We first note that

|  |  |  |
| --- | --- | --- |
|  | ⟨e0⊗k,𝕏^t⟩=tkk!.\langle e\_{0}^{\otimes k},\widehat{\mathbb{X}}\_{t}\rangle=\frac{t^{k}}{k!}. |  |

Moreover, using the quasi-shuffle property of 𝕏^\widehat{\mathbb{X}}, see Definition [2.5](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem5 "Definition 2.5. ‣ 2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths"), we have that

|  |  |  |
| --- | --- | --- |
|  | ⟨eI​~​e0⊗k,𝕏^t⟩=⟨eI​e0⊗k,𝕏^t⟩,\langle e\_{I}\widetilde{\shuffle}e\_{0}^{\otimes k},\widehat{\mathbb{X}}\_{t}\rangle=\langle e\_{I}\shuffle e\_{0}^{\otimes k},\widehat{\mathbb{X}}\_{t}\rangle, |  |

because ⟨εi​0,𝕏^⟩=0\langle\varepsilon\_{i0},\widehat{\mathbb{X}}\rangle=0 for any i=0,…,d^−1i=0,\dots,\hat{d}-1, i.e., the quasi-shuffle product and the shuffle product coincide. Hence, by e.g. [[CPSF25](https://arxiv.org/html/2602.05898v1#bib.bibx27), Proposition C.5],

|  |  |  |
| --- | --- | --- |
|  | ⟨(eI​~​e0⊗k)⊗e0,𝕏^T⟩=∫0T⟨eI​~​e0⊗k,𝕏^t⟩​dt=∫0T⟨eI,𝕏^t⟩​⟨e0⊗k,𝕏^t⟩​dt=∫0T⟨eI,𝕏^t⟩​tkk!​dt.\langle(e\_{I}\widetilde{\shuffle}e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{X}}\_{T}\rangle=\int\_{0}^{T}\langle e\_{I}\widetilde{\shuffle}e\_{0}^{\otimes k},\widehat{\mathbb{X}}\_{t}\rangle\,\mathrm{d}t=\int\_{0}^{T}\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle\langle e\_{0}^{\otimes k},\widehat{\mathbb{X}}\_{t}\rangle\,\mathrm{d}t=\int\_{0}^{T}\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle\frac{t^{k}}{k!}\,\mathrm{d}t. |  |

Similarly, we have

|  |  |  |
| --- | --- | --- |
|  | ⟨(eI​e0⊗k)⊗e0,𝕐^T⟩=∫0T⟨eI,𝕐^t⟩​tkk!​dt.\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{Y}}\_{T}\rangle=\int\_{0}^{T}\langle e\_{I},\widehat{\mathbb{Y}}\_{t}\rangle\frac{t^{k}}{k!}\,\mathrm{d}t. |  |

By [[Bre11](https://arxiv.org/html/2602.05898v1#bib.bibx18), Corollary 4.24] and because ⟨eI,𝕏^0⟩=⟨eI,𝕐^0⟩=0\langle e\_{I},\widehat{\mathbb{X}}\_{0}\rangle=\langle e\_{I},\widehat{\mathbb{Y}}\_{0}\rangle=0, it then follows that

|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝕏^t⟩=⟨eI,𝕐^t⟩,\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle=\langle e\_{I},\widehat{\mathbb{Y}}\_{t}\rangle, |  |

for all t∈[0,T]t\in[0,T] and all I∈{0,…,d^−1}NI\in\{0,\ldots,\hat{d}-1\}^{N}, N∈{0,1,2}N\in\{0,1,2\}. However, this contradicts the assumption that 𝐗^,𝐘^\widehat{\mathbf{X}},\widehat{\mathbf{Y}} are distinct. Thus we can conclude that 𝒜\mathcal{A} is point-separating.
∎

###### Remark 2.9.

Similarly, one can derive the universal approximation property also when considering functionals of stopped rough paths. The space of stopped rough paths is defined by ΛT=⋃t∈[0,T]𝒞^p​([0,t];ℝd^)\Lambda\_{T}=\bigcup\_{t\in[0,T]}\widehat{\mathcal{C}}^{p}([0,t];\mathbb{R}^{\hat{d}}) with the semi-metric dΛT​(𝐗^[0,t],𝐘^[0,s]):=|t−s|+dp​-var;[0,t∨s]​(𝐗t^[0,t∨s],𝐘s^[0,t∨s])d\_{\Lambda\_{T}}(\widehat{\mathbf{X}}\_{[0,t]},\widehat{\mathbf{Y}}\_{[0,s]}):=|t-s|+d\_{p\textup{-var};[0,t\vee s]}(\widehat{\mathbf{X}^{t}}\_{[0,t\vee s]},\widehat{\mathbf{Y}^{s}}\_{[0,t\vee s]}). Here 𝐗^[0,t]\widehat{\mathbf{X}}\_{[0,t]} denotes the restriction of 𝐗^\widehat{\mathbf{X}}, that is defined on [0,T][0,T], to the sub-interval [0,t][0,t], t≤Tt\leq T, and 𝐗t^\widehat{\mathbf{X}^{t}} denotes the stopped rough path. More precisely, Xt^\widehat{X^{t}} is the process (Xt^)s=(s,Xst,Q​(Xst))(\widehat{X^{t}})\_{s}=(s,X^{t}\_{s},Q(X\_{s}^{t})), s∈[0,T]s\in[0,T], that is, the process where we stop the path XX and the bracket process Q​(X)Q(X), but not the time-extension, and 𝐗t^\widehat{\mathbf{X}^{t}} denotes the rough path lift of Xt^\widehat{X^{t}}, see e.g. [[KLA20](https://arxiv.org/html/2602.05898v1#bib.bibx41), [CM25](https://arxiv.org/html/2602.05898v1#bib.bibx25), [BPS25](https://arxiv.org/html/2602.05898v1#bib.bibx16)] for similar definitions. This then allows to approximate non-anticipative path-functionals f:ΛT→ℝf\colon\Lambda\_{T}\to\mathbb{R} by linear functionals of the signature on subsets of compact sets.

###### Remark 2.10.

If the bracket is strictly increasing, i.e., t↦[𝐗]tt\mapsto[\mathbf{X}]\_{t} is strictly increasing (for at least one component [𝐗]i​j[\mathbf{X}]^{ij}, i,j∈{1,…,d}i,j\in\{1,\ldots,d\}), it suffices to extend the path only by the bracket terms, so to consider only X^=(X,Q​(X))\widehat{X}=(X,Q(X)). In particular, the quasi-shuffle property and Proposition [2.4](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem4 "Proposition 2.4. ‣ 2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths") still hold true. For point separation one may then apply the same arguments using, for some fixed i,j∈{1,…,d}i,j\in\{1,\dots,d\}, ⟨(eI​εi​j⊗k)⊗εi​j,𝕏^T⟩\langle(e\_{I}\shuffle\varepsilon\_{ij}^{\otimes k})\otimes\varepsilon\_{ij},\,\widehat{\mathbb{X}}\_{T}\rangle, for ⟨εi​j,𝕏^γ,π⟩=[𝐗]i​j\langle\varepsilon\_{ij},\widehat{\mathbb{X}}^{\gamma,\pi}\rangle=[\mathbf{X}]^{ij}.

And if the bracket is given as a linear functional of the time component and the path components of XX, i.e., [𝐗]ti​j=∑|I|≤1aIi​j​⟨eI,𝕏^t⟩[\mathbf{X}]\_{t}^{ij}=\sum\_{|I|\leq 1}a^{ij}\_{I}\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle, where II is a multi-index taking values in {0,…,d}\{0,\dots,d\}, it suffices to extend the path only by time, so to consider only X^=(⋅,X)\widehat{X}=(\cdot,X).

### 2.5. Discussion on approximation with weakly geometric rough paths

When considering weakly geometric rough paths, Theorem [2.8](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem8 "Theorem 2.8. ‣ 2.4. Universal approximation with signatures of general rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths") clearly can be applied because the rough path bracket of a weakly geometric rough path is equal to zero. Extending the path by its rough path brackets is therefore redundant. In this case, it is already known that the universal approximation theorem holds for only time-extended weakly geometric rough paths. That is, continuous functionals of time-extended weakly geometric rough paths can be approximated arbitrarily well on compact sets by linear functionals of its signature.

For completeness, let us recall and prove the universal approximation theorem for time-extended weakly geometric rough paths. (A direct proof can be found in Appendix [A](https://arxiv.org/html/2602.05898v1#A1 "Appendix A Proof of Theorem 2.11 ‣ Universal approximation with signatures of non-geometric rough paths").) For this, we consider the subspace of time-extended weakly geometric rough paths, defined by

|  |  |  |
| --- | --- | --- |
|  | C^op​-var​([0,T];G2​(ℝ1+d)):={𝕏^o,2∈Cop​-var​([0,T];G2​(ℝ1+d)):⟨e0,𝕏^to,2⟩=t,t∈[0,T]}.\widehat{C}\_{o}^{p\textup{-var}}([0,T];G^{2}(\mathbb{R}^{1+d})):=\{\widehat{\mathbb{X}}^{o,2}\in C\_{o}^{p\textup{-var}}([0,T];G^{2}(\mathbb{R}^{1+d})):\langle e\_{0},\widehat{\mathbb{X}}^{o,2}\_{t}\rangle=t,\,t\in[0,T]\}. |  |

###### Theorem 2.11.

Let p∈(2,3)p\in(2,3). Let K⊂C^op​-var​([0,T];G2​(ℝ1+d))K\subset\widehat{C}\_{o}^{p\textup{-var}}([0,T];G^{2}(\mathbb{R}^{1+d})) be a compact subset, bounded with respect to the pp-variation norm, and consider a continuous function f:K→ℝf\colon K\to\mathbb{R}. Then for every ε>0\varepsilon>0, there exists a linear functional ℓ∈T​(ℝ1+d)\ell\in T(\mathbb{R}^{1+d}) such that

|  |  |  |
| --- | --- | --- |
|  | sup𝕏^o,2∈K|f​(𝕏^o,2)−⟨ℓ,𝕏^To⟩|<ε,\sup\_{\widehat{\mathbb{X}}^{o,2}\in K}|f(\widehat{\mathbb{X}}^{o,2})-\langle\ell,\widehat{\mathbb{X}}^{o}\_{T}\rangle|<\varepsilon, |  |

where 𝕏^o\widehat{\mathbb{X}}^{o} denotes the signature of X^:=Π(1)​(𝕏^o,2)\widehat{X}:=\Pi\_{(1)}(\widehat{\mathbb{X}}^{o,2}).

###### Proof.

We first notice that it is equivalent to consider the space of weakly geometric rough paths taken as a subset of the rough path space instead of taken as the space of continuous paths with finite pp-variation and taking values in G2​(ℝ1+d)G^{2}(\mathbb{R}^{1+d}). The proof then follows by an application of Theorem [2.8](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem8 "Theorem 2.8. ‣ 2.4. Universal approximation with signatures of general rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths"): The rough path bracket of a weakly geometric rough path is equal to zero. Thus, for L>0L>0 large enough, KLK\_{L} does coincide with KK. It is therefore actually sufficient to reduce the extended path to X^=(⋅,X)\widehat{X}=(\cdot,X), i.e., d^=d+1\hat{d}=d+1, which then implies the claim.
∎

## 3. The signature using general pathwise stochastic integration

In this section, we give an example that fits into the framework developed in the previous section. We introduce a notion of signatures using the path assumption Property γ\gamma-(RIE), which allows to construct pathwise (iterated) integrals as limits of general Riemann sums. It is an extension of Property (RIE), which has been established in detail in [[DKP25](https://arxiv.org/html/2602.05898v1#bib.bibx28)]. We now give the path properties and the statements required in this paper. For the proofs and an equivalent and more intuitive characterization of the path property, we refer to [[DKP25](https://arxiv.org/html/2602.05898v1#bib.bibx28)].

### 3.1. On Property 𝜸\boldsymbol{\gamma}-(RIE)

###### Property 𝜸\boldsymbol{\gamma}-(RIE).

Let X∈C​([0,T];ℝd)X\in C([0,T];\mathbb{R}^{d}), γ∈[0,1]\gamma\in[0,1], p∈(2,3)p\in(2,3), and π=(πn)n∈ℕ\pi=(\pi^{n})\_{n\in\mathbb{N}}, with πn={0=t0n<t1n<⋯<tNnn=T}\pi^{n}=\{0=t^{n}\_{0}<t^{n}\_{1}<\dots<t^{n}\_{N\_{n}}=T\}, n∈ℕn\in\mathbb{N}, be a sequence of partitions of the interval [0,T][0,T] such that sup{|Xtkn,tk+1n|:k=0,…,Nn−1}\sup\{|X\_{t^{n}\_{k},t^{n}\_{k+1}}|\,:k=0,\dots,N\_{n}-1\} converges to 0 as n→∞n\to\infty. We assume that

1. (i)

   the Riemann sums

   |  |  |  |
   | --- | --- | --- |
   |  | ∫0tXr⊗dγ,πn​Xr:=∑k=0Nn−1(Xtkn+γ​Xtkn,tk+1n)⊗Xtkn∧t,tk+1n∧t,t∈[0,T],\int\_{0}^{t}X\_{r}\otimes\mathrm{d}^{\gamma,\pi^{n}}X\_{r}:=\sum\_{k=0}^{N\_{n}-1}(X\_{t^{n}\_{k}}+\gamma X\_{t^{n}\_{k},t^{n}\_{k+1}})\otimes X\_{t^{n}\_{k}\wedge t,t^{n}\_{k+1}\wedge t},\quad t\in[0,T], |  |

   converge uniformly as n→∞n\to\infty to a limit, which we denote by ∫0tXr⊗dγ,π​Xr\int\_{0}^{t}X\_{r}\otimes\mathrm{d}^{\gamma,\pi}X\_{r},
2. (ii)

   there exists a control function cc such that

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (3.1) |  | sup(s,t)∈ΔT|Xs,t|pc​(s,t)+supn∈ℕsup0≤k<ℓ≤Nn|(∫0⋅Xr⊗dγ,πn​Xr)tkn,tℓn−Xtkn⊗Xtkn,tℓn|p2c​(tkn,tℓn)≲1.\sup\_{(s,t)\in\Delta\_{T}}\frac{|X\_{s,t}|^{p}}{c(s,t)}+\sup\_{n\in\mathbb{N}}\sup\_{0\leq k<\ell\leq N\_{n}}\frac{|(\int\_{0}^{\cdot}X\_{r}\otimes\mathrm{d}^{\gamma,\pi^{n}}X\_{r})\_{t^{n}\_{k},t^{n}\_{\ell}}-X\_{t^{n}\_{k}}\otimes X\_{t^{n}\_{k},t^{n}\_{\ell}}|^{\frac{p}{2}}}{c(t^{n}\_{k},t^{n}\_{\ell})}\lesssim 1. |  |

We say that a path X∈C​([0,T];ℝd)X\in C([0,T];\mathbb{R}^{d}) satisfies *Property γ\gamma-(RIE)* relative to γ\gamma, pp and π\pi if γ\gamma, pp, π\pi and XX together satisfy Property γ\gamma-(RIE).

###### Proposition 3.1 (Proposition 2.9 in [[DKP25](https://arxiv.org/html/2602.05898v1#bib.bibx28)]).

Suppose that X∈C​([0,T];ℝd)X\in C([0,T];\mathbb{R}^{d}) satisfies Property γ\gamma-(RIE) relative to some γ∈[0,1]\gamma\in[0,1], p∈(2,3)p\in(2,3) and a sequence of partitions π=(πn)n∈ℕ\pi=(\pi^{n})\_{n\in\mathbb{N}}. Then, XX canonically extends to a continuous rough path 𝐗γ,π:=(X,𝕏γ,π,(2))∈𝒞p​([0,T];ℝd)\mathbf{X}^{\gamma,\pi}:=(X,\mathbb{X}^{\gamma,\pi,(2)})\in\mathcal{C}^{p}([0,T];\mathbb{R}^{d}), where

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | 𝕏s,tγ,π,(2):=∫0tXr⊗dγ,π​Xr−∫0sXr⊗dγ,π​Xr−Xs⊗Xs,t,(s,t)∈ΔT.\mathbb{X}^{\gamma,\pi,(2)}\_{s,t}:=\int\_{0}^{t}X\_{r}\otimes\mathrm{d}^{\gamma,\pi}X\_{r}-\int\_{0}^{s}X\_{r}\otimes\mathrm{d}^{\gamma,\pi}X\_{r}-X\_{s}\otimes X\_{s,t},\qquad(s,t)\in\Delta\_{T}. |  |

We note that 𝐗0,π\mathbf{X}^{0,\pi} corresponds to the Itô-rough path lift, 𝐗12,π\mathbf{X}^{\frac{1}{2},\pi} corresponds to the Stratonovich-rough path lift, and 𝐗1,π\mathbf{X}^{1,\pi} corresponds to the backward Itô rough path lift of a stochastic process, since the “iterated integral” 𝕏0,π,(2)\mathbb{X}^{0,\pi,(2)}, 𝕏12,π,(2)\mathbb{X}^{\frac{1}{2},\pi,(2)}, and 𝕏1,π,(2)\mathbb{X}^{1,\pi,(2)} is given as a limit of left-point, mid-point, and right-point Riemann sums, analogously to the stochastic Itô, Stratonovich, and backward Itô integral, respectively, see [[FH20](https://arxiv.org/html/2602.05898v1#bib.bibx29), Chapter 5.4] on backward rough integration for Brownian motion, and Section [4](https://arxiv.org/html/2602.05898v1#S4 "4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths").

When assuming Property γ\gamma-(RIE) for a path XX, we will always work with the rough path 𝐗γ,π=(X,𝕏γ,π,(2))\mathbf{X}^{\gamma,\pi}=(X,\mathbb{X}^{\gamma,\pi,(2)}) defined via ([3.2](https://arxiv.org/html/2602.05898v1#S3.E2 "In Proposition 3.1 (Proposition 2.9 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths")).

###### Lemma 3.2 (Lemma 2.10 in [[DKP25](https://arxiv.org/html/2602.05898v1#bib.bibx28)]).

Suppose that X∈C​([0,T];ℝd)X\in C([0,T];\mathbb{R}^{d}) satisfies Property γ\gamma-(RIE) relative to some γ∈[0,1]\gamma\in[0,1], p∈(2,3)p\in(2,3) and a sequence of partitions πn={0=t0n<⋯<tNnn=T}\pi^{n}=\{0=t^{n}\_{0}<\dots<t^{n}\_{N\_{n}}=T\}, n∈ℕn\in\mathbb{N}. Let 1≤i,j≤d1\leq i,j\leq d, and define for γ=12\gamma=\frac{1}{2}, [Xi,Xj]γ,π:=0[X^{i},X^{j}]^{\gamma,\pi}:=0, and for γ≠12\gamma\neq\frac{1}{2},

|  |  |  |
| --- | --- | --- |
|  | [Xi,Xj]tγ,π:=Xti​Xtj−X0i​X0j−∫0tXri​dγ,π​Xrj−∫0tXrj​dγ,π​Xri,t∈[0,T].[X^{i},X^{j}]^{\gamma,\pi}\_{t}:=X^{i}\_{t}X^{j}\_{t}-X^{i}\_{0}X^{j}\_{0}-\int\_{0}^{t}X^{i}\_{r}\,\mathrm{d}^{\gamma,\pi}X^{j}\_{r}-\int\_{0}^{t}X^{j}\_{r}\,\mathrm{d}^{\gamma,\pi}X^{i}\_{r},\qquad t\in[0,T]. |  |

Then, [Xi,Xj]γ,π[X^{i},X^{j}]^{\gamma,\pi} is a continuous function and

|  |  |  |
| --- | --- | --- |
|  | [Xi,Xj]tγ,π=limn→∞[Xi,Xj]tγ,πn:=limn→∞(1−2​γ)​∑k=0Nn−1Xtkn∧t,tk+1n∧ti​Xtkn∧t,tk+1n∧tj,t∈[0,T].[X^{i},X^{j}]^{\gamma,\pi}\_{t}=\lim\_{n\to\infty}[X^{i},X^{j}]^{\gamma,\pi^{n}}\_{t}:=\lim\_{n\to\infty}(1-2\gamma)\sum\_{k=0}^{N\_{n}-1}X^{i}\_{t^{n}\_{k}\wedge t,t^{n}\_{k+1}\wedge t}X^{j}\_{t^{n}\_{k}\wedge t,t^{n}\_{k+1}\wedge t},\quad t\in[0,T]. |  |

The sequence ([Xi,Xj]γ,πn)n∈ℕ([X^{i},X^{j}]^{\gamma,\pi^{n}})\_{n\in\mathbb{N}} has uniformly bounded 11-variation and, thus, [Xi,Xj]γ,π[X^{i},X^{j}]^{\gamma,\pi} has finite 11-variation. We write [X]γ,π=[X,X]γ,π=([Xi,Xj]γ,π)1≤i,j≤d[X]^{\gamma,\pi}=[X,X]^{\gamma,\pi}=([X^{i},X^{j}]^{\gamma,\pi})\_{1\leq i,j\leq d}, and, analogously, [X]γ,πn[X]^{\gamma,\pi^{n}}, n∈ℕn\in\mathbb{N}.

By a slight extension (to allow non-nested partitions) of [[ALP24](https://arxiv.org/html/2602.05898v1#bib.bibx6), Proposition 2.18], the rough path bracket [𝐗γ,π][\mathbf{X}^{\gamma,\pi}] coincides with (1−2​γ)​[X](1-2\gamma)[X], where [X][X] denotes the quadratic variation of XX along π\pi in the sense of Föllmer [[Föl81](https://arxiv.org/html/2602.05898v1#bib.bibx31)], equal to [X]γ,π[X]^{\gamma,\pi}.

We will actually continue working under Property γ\gamma-(RIE), as it is more general, but we briefly want to point out the theoretical relation to Property (RIE), which has been introduced in [[PP16](https://arxiv.org/html/2602.05898v1#bib.bibx49)] and [[ACLP23](https://arxiv.org/html/2602.05898v1#bib.bibx1)].

###### Property (RIE).

Let X∈C​([0,T];ℝd)X\in C([0,T];\mathbb{R}^{d}), p∈(2,3)p\in(2,3), and π=(πn)n∈ℕ\pi=(\pi^{n})\_{n\in\mathbb{N}}, with πn={0=t0n<t1n<⋯<tNnn=T}\pi^{n}=\{0=t^{n}\_{0}<t^{n}\_{1}<\dots<t^{n}\_{N\_{n}}=T\}, n∈ℕn\in\mathbb{N}, be a sequence of partitions of the interval [0,T][0,T] such that sup{|Xtkn,tk+1n|:k=0,…,Nn−1}\sup\{|X\_{t^{n}\_{k},t^{n}\_{k+1}}|\,:k=0,\dots,N\_{n}-1\} converges to 0 as n→∞n\to\infty. We assume that

1. (i)

   the left-point Riemann sums

   |  |  |  |
   | --- | --- | --- |
   |  | ∫0tXr⊗dπn​Xr:=∑k=0Nn−1Xtkn⊗Xtkn∧t,tk+1n∧t,t∈[0,T],\int\_{0}^{t}X\_{r}\otimes\mathrm{d}^{\pi^{n}}X\_{r}:=\sum\_{k=0}^{N\_{n}-1}X\_{t^{n}\_{k}}\otimes X\_{t^{n}\_{k}\wedge t,t^{n}\_{k+1}\wedge t},\quad t\in[0,T], |  |

   converge uniformly as n→∞n\to\infty to a limit, which we denote by ∫0tXr⊗dπ​Xr\int\_{0}^{t}X\_{r}\otimes\mathrm{d}^{\pi}X\_{r},
2. (ii)

   there exists a control function cc such that

   |  |  |  |
   | --- | --- | --- |
   |  | sup(s,t)∈ΔT|Xs,t|pc​(s,t)+supn∈ℕsup0≤k<ℓ≤Nn|(∫0⋅Xr⊗dπn​Xr)tkn,tℓn−Xtkn⊗Xtkn,tℓn|p2c​(tkn,tℓn)≲1.\sup\_{(s,t)\in\Delta\_{T}}\frac{|X\_{s,t}|^{p}}{c(s,t)}+\sup\_{n\in\mathbb{N}}\sup\_{0\leq k<\ell\leq N\_{n}}\frac{|(\int\_{0}^{\cdot}X\_{r}\otimes\mathrm{d}^{\pi^{n}}X\_{r})\_{t^{n}\_{k},t^{n}\_{\ell}}-X\_{t^{n}\_{k}}\otimes X\_{t^{n}\_{k},t^{n}\_{\ell}}|^{\frac{p}{2}}}{c(t^{n}\_{k},t^{n}\_{\ell})}\lesssim 1. |  |

We say that a path X∈C​([0,T];ℝd)X\in C([0,T];\mathbb{R}^{d}) satisfies *Property (RIE)* relative to pp and π\pi if pp, π\pi and XX together satisfy Property (RIE).

###### Lemma 3.3 (Lemma 2.16 in [[DKP25](https://arxiv.org/html/2602.05898v1#bib.bibx28)]).

Let X∈C​([0,T];ℝd)X\in C([0,T];\mathbb{R}^{d}), γ∈[0,1]\gamma\in[0,1], p∈(2,3)p\in(2,3) and π=(πn)n∈ℕ\pi=(\pi^{n})\_{n\in\mathbb{N}} be a sequence of partitions.

1. (i)

   Suppose γ≠12\gamma\neq\frac{1}{2}. Then, XX satisfies Property (RIE) (i) relative to π\pi if and only if XX satisfies Property γ\gamma-(RIE) (i) relative to γ\gamma and π\pi, and XX satisfies Property (RIE) (ii) relative to pp and π\pi if and only if XX satisfies Property γ\gamma-(RIE) (ii) relative to γ\gamma, pp and π\pi.
2. (ii)

   Suppose γ=12\gamma=\frac{1}{2}. If XX satisfies Property (RIE) (i) relative to π\pi, then XX satisfies Property γ\gamma-(RIE) (i) relative to γ\gamma and π\pi, and if XX satisfies Property (RIE) (ii) relative to pp and π\pi, then XX satisfies Property γ\gamma-(RIE) (ii) relative to γ\gamma, pp and π\pi.

Analogously to Property (RIE), see [[AKLP25a](https://arxiv.org/html/2602.05898v1#bib.bibx4), Proposition 2.12], Property γ\gamma-(RIE) is stable under perturbation by a path of finite qq-variation for q∈(1,2)q\in(1,2), which then falls into the regime of Young integration. The proof of the following lemma can be found in Appendix [B](https://arxiv.org/html/2602.05898v1#A2 "Appendix B Proof of Lemma 3.4 ‣ Universal approximation with signatures of non-geometric rough paths").

###### Lemma 3.4.

Suppose that X∈C​([0,T];ℝd)X\in C([0,T];\mathbb{R}^{d}) satisfies Property γ\gamma-(RIE) relative to some γ∈[0,1]\gamma\in[0,1], p∈(2,3)p\in(2,3) and a sequence of partitions π=(πn)n∈ℕ\pi=(\pi^{n})\_{n\in\mathbb{N}}. Let φ∈Cq​-var​([0,T];ℝd)\varphi\in C^{q\textup{-var}}([0,T];\mathbb{R}^{d}) for some q∈[1,2)q\in[1,2) such that 1/p+1/q>11/p+1/q>1 and sup{|φtkn,tk+1n|:k=0,…,Nn−1}\sup\{|\varphi\_{t^{n}\_{k},t^{n}\_{k+1}}|:k=0,\dots,N\_{n}-1\} converges to 0 as n→∞n\to\infty. Then the path X^=X+φ\widehat{X}=X+\varphi satisfies Property γ\gamma-(RIE) relative to γ\gamma, pp and π\pi.

### 3.2. The 𝜸\boldsymbol{\gamma}-signature

We now show that the canonical rough path under Property γ\gamma-(RIE) can be corrected to a weakly geometric rough path by adding the pathwise quadratic variation term, which seems natural when comparing stochastic Itô and Stratonovich integration.

###### Lemma 3.5.

Suppose that X∈C​([0,T];ℝd)X\in C([0,T];\mathbb{R}^{d}) satisfies Property γ\gamma-(RIE) relative to some γ∈[0,1]\gamma\in[0,1], p∈(2,3)p\in(2,3) and a sequence of partitions π=(πn)n∈ℕ\pi=(\pi^{n})\_{n\in\mathbb{N}}. Let (X,𝕏γ,π,o,(2))∈𝒞p​([0,T];ℝd)(X,\mathbb{X}^{\gamma,\pi,o,(2)})\in\mathcal{C}^{p}([0,T];\mathbb{R}^{d}) be a continuous rough path, with 𝕏γ,π,o,(2):ΔT→ℝd\mathbb{X}^{\gamma,\pi,o,(2)}\colon\Delta\_{T}\to\mathbb{R}^{d} given by

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,tγ,π,o,(2):=𝕏s,tγ,π,(2)+12​[X]s,tγ,π,(s,t)∈ΔT,\mathbb{X}^{\gamma,\pi,o,(2)}\_{s,t}:=\mathbb{X}^{\gamma,\pi,(2)}\_{s,t}+\frac{1}{2}[X]^{\gamma,\pi}\_{s,t},\qquad(s,t)\in\Delta\_{T}, |  |

where 𝕏γ,π,(2)\mathbb{X}^{\gamma,\pi,(2)} is the canonical rough path lift defined in Proposition [3.1](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem1 "Proposition 3.1 (Proposition 2.9 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") and [X]γ,π[X]^{\gamma,\pi} is defined in Lemma [3.2](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem2 "Lemma 3.2 (Lemma 2.10 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths"). Then, 𝕏γ,π,o,2:[0,T]→G2​(ℝd)\mathbb{X}^{\gamma,\pi,o,2}\colon[0,T]\to G^{2}(\mathbb{R}^{d}) is a weakly geometric rough path, where we define

|  |  |  |
| --- | --- | --- |
|  | 𝕏tγ,π,o,2:=(1,X0,t,𝕏0,tγ,π,o,(2)),t∈[0,T].\mathbb{X}^{\gamma,\pi,o,2}\_{t}:=(1,X\_{0,t},\mathbb{X}^{\gamma,\pi,o,(2)}\_{0,t}),\qquad t\in[0,T]. |  |

###### Proof.

Since 𝕏γ,π,(2)\mathbb{X}^{\gamma,\pi,(2)} has finite p2\frac{p}{2}-variation and [Xi,Xj]γ,π[X^{i},X^{j}]^{\gamma,\pi} has finite 11-variation, 𝕏γ,π,o,(2)\mathbb{X}^{\gamma,\pi,o,(2)} has finite p2\frac{p}{2}-variation, see Proposition [3.1](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem1 "Proposition 3.1 (Proposition 2.9 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") and Lemma [3.2](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem2 "Lemma 3.2 (Lemma 2.10 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths"), and particularly, ∥𝟏;𝕏γ,π,o,2∥p<∞\|\mathbf{1};\mathbb{X}^{\gamma,\pi,o,2}\|\_{p}<\infty.

We show that 𝕊​(𝕏0,tγ,π,o,(2))=12​X0,t⊗X0,t\mathbb{S}(\mathbb{X}^{\gamma,\pi,o,(2)}\_{0,t})=\frac{1}{2}X\_{0,t}\otimes X\_{0,t}, for any t∈[0,T]t\in[0,T], where 𝕊\mathbb{S} denotes the symmetric part of the matrix. Then applying Lemma [2.1](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem1 "Lemma 2.1. ‣ 2.2. Essentials on rough path theory ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths"), the proof is complete.

By definition, it holds that, for any 1≤i,j≤d1\leq i,j\leq d and any t∈[0,T]t\in[0,T],

|  |  |  |
| --- | --- | --- |
|  | (𝕏0,tγ,π,o,(2))i​j+(𝕏0,tγ,π,o,(2))j​i\displaystyle(\mathbb{X}^{\gamma,\pi,o,(2)}\_{0,t})^{ij}+(\mathbb{X}^{\gamma,\pi,o,(2)}\_{0,t})^{ji} |  |
|  |  |  |
| --- | --- | --- |
|  | =∫0tXri​dγ,π​Xrj−X0i​X0,tj+12​[Xi,Xj]tγ,π+∫0tXrj​dγ,π​Xri−X0j​X0,ti+12​[Xj,Xi]tγ,π\displaystyle\quad=\int\_{0}^{t}X\_{r}^{i}\,\mathrm{d}^{\gamma,\pi}X\_{r}^{j}-X\_{0}^{i}X\_{0,t}^{j}+\frac{1}{2}[X^{i},X^{j}]^{\gamma,\pi}\_{t}+\int\_{0}^{t}X\_{r}^{j}\,\mathrm{d}^{\gamma,\pi}X\_{r}^{i}-X\_{0}^{j}X\_{0,t}^{i}+\frac{1}{2}[X^{j},X^{i}]^{\gamma,\pi}\_{t} |  |
|  |  |  |
| --- | --- | --- |
|  | =limn→∞∑k=0Nn−1(Xtkni+γ​Xtkn,tk+1ni)​Xtkn∧t,tk+1n∧tj+(12−γ)​Xtkn,tk+1ni​Xtkn∧t,tk+1n∧tj−X0i​X0,tj\displaystyle\quad=\lim\_{n\to\infty}\sum\_{k=0}^{N\_{n}-1}(X^{i}\_{t^{n}\_{k}}+\gamma X^{i}\_{t^{n}\_{k},t^{n}\_{k+1}})X^{j}\_{t^{n}\_{k}\wedge t,t^{n}\_{k+1}\wedge t}+(\frac{1}{2}-\gamma)X^{i}\_{t^{n}\_{k},t^{n}\_{k+1}}X^{j}\_{t^{n}\_{k}\wedge t,t^{n}\_{k+1}\wedge t}-X\_{0}^{i}X\_{0,t}^{j} |  |
|  |  |  |
| --- | --- | --- |
|  | +limn→∞∑k=0Nn−1(Xtknj+γ​Xtkn,tk+1nj)​Xtkn∧t,tk+1n∧ti+(12−γ)​Xtkn,tk+1nj​Xtkn∧t,tk+1n∧ti−X0j​X0,ti\displaystyle\qquad+\lim\_{n\to\infty}\sum\_{k=0}^{N\_{n}-1}(X^{j}\_{t^{n}\_{k}}+\gamma X^{j}\_{t^{n}\_{k},t^{n}\_{k+1}})X^{i}\_{t^{n}\_{k}\wedge t,t^{n}\_{k+1}\wedge t}+(\frac{1}{2}-\gamma)X^{j}\_{t^{n}\_{k},t^{n}\_{k+1}}X^{i}\_{t^{n}\_{k}\wedge t,t^{n}\_{k+1}\wedge t}-X\_{0}^{j}X\_{0,t}^{i} |  |
|  |  |  |
| --- | --- | --- |
|  | =limn→∞∑k=0Nn−112​(Xtkni+Xtk+1ni)​Xtkn,tk+1nj−X0i​X0,tj\displaystyle\quad=\lim\_{n\to\infty}\sum\_{k=0}^{N\_{n}-1}\frac{1}{2}(X^{i}\_{t^{n}\_{k}}+X^{i}\_{t^{n}\_{k+1}})X^{j}\_{t^{n}\_{k},t^{n}\_{k+1}}-X\_{0}^{i}X\_{0,t}^{j} |  |
|  |  |  |
| --- | --- | --- |
|  | +limn→∞∑k=0Nn−112​(Xtknj+Xtk+1nj)​Xtkn,tk+1ni−X0j​X0,ti\displaystyle\qquad+\lim\_{n\to\infty}\sum\_{k=0}^{N\_{n}-1}\frac{1}{2}(X^{j}\_{t^{n}\_{k}}+X^{j}\_{t^{n}\_{k+1}})X^{i}\_{t^{n}\_{k},t^{n}\_{k+1}}-X\_{0}^{j}X\_{0,t}^{i} |  |
|  |  |  |
| --- | --- | --- |
|  | =Xti​Xtj−X0i​X0j−X0i​X0,tj−X0j​X0,ti\displaystyle\quad=X\_{t}^{i}X\_{t}^{j}-X\_{0}^{i}X\_{0}^{j}-X\_{0}^{i}X\_{0,t}^{j}-X\_{0}^{j}X\_{0,t}^{i} |  |
|  |  |  |
| --- | --- | --- |
|  | =X0,ti​X0,tj.\displaystyle\quad=X\_{0,t}^{i}X\_{0,t}^{j}. |  |

∎

###### Remark 3.6.

Since [X]12,π=0[X]^{\frac{1}{2},\pi}=0, see Lemma [3.2](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem2 "Lemma 3.2 (Lemma 2.10 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths"), we notice that 𝕏12,π,o,(2)=𝕏12,π,(2)\mathbb{X}^{\frac{1}{2},\pi,o,(2)}=\mathbb{X}^{\frac{1}{2},\pi,(2)}, which implies that (1,X0,⋅,𝕏0,⋅12,π,(2))∈Cop​-var​([0,T];G2​(ℝd))(1,X\_{0,\cdot},\mathbb{X}^{\frac{1}{2},\pi,(2)}\_{0,\cdot})\in C^{p\textup{-var}}\_{o}([0,T];G^{2}(\mathbb{R}^{d})). That is, the Stratonovich-type rough path is indeed a weakly geometric rough path, which is very reasonable.

Further, for any γ∈[0,1]\gamma\in[0,1], it holds that 𝕏γ,π,o,(2)=𝕏12,π,(2)\mathbb{X}^{\gamma,\pi,o,(2)}=\mathbb{X}^{\frac{1}{2},\pi,(2)}.

###### Remark 3.7.

If XX satisfies Property γ\gamma-(RIE), one can consider the signature 𝕏γ,π,o\mathbb{X}^{\gamma,\pi,o} of XX defined in Definition [2.3](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem3 "Definition 2.3. ‣ 2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths") as the unique path extension of 𝕏γ,π,o,2\mathbb{X}^{\gamma,\pi,o,2}. This then coincides with 𝕏12,π,o\mathbb{X}^{\frac{1}{2},\pi,o}, the unique path extension of (1,X0,⋅,𝕏12,π,(2))(1,X\_{0,\cdot},\mathbb{X}^{\frac{1}{2},\pi,(2)}).

Now, we define the signature as the collection of all iterated integrals over a fixed interval associated to a sufficiently regular path. Here, we utilize Property γ\gamma-(RIE) and the corresponding iterated integral, which allows for a unifying framework for Itô-type and Stratonovich-type signatures.

To that end, we assume that the path XX satisfies Property γ\gamma-(RIE) relative to γ\gamma, pp and π\pi, and define the signature 𝕏γ,π\mathbb{X}^{\gamma,\pi} of XX using Lyons’ extension theorem on T​((ℝd))T((\mathbb{R}^{d})), see e.g. [[LCL07](https://arxiv.org/html/2602.05898v1#bib.bibx43), Theorem 3.7]. More precisely, we note that (1,X0,⋅,𝕏γ,π,(2)):[0,T]→T2​(ℝd)(1,X\_{0,\cdot},\mathbb{X}^{\gamma,\pi,(2)})\colon[0,T]\to T^{2}(\mathbb{R}^{d}) is a multiplicative functional of finite pp-variation controlled by cc, i.e., |Xs,t|≲c​(s,t)|X\_{s,t}|\lesssim c(s,t), |𝕏s,tγ,π,(2)|≲c​(s,t)|\mathbb{X}^{\gamma,\pi,(2)}\_{s,t}|\lesssim c(s,t), (s,t)∈ΔT(s,t)\in\Delta\_{T}, where 𝕏tγ,π,(2):=∫0tX0,r⊗dγ,π​Xr:=∫0tXr⊗dγ,π​Xr−X0⊗X0,t\mathbb{X}^{\gamma,\pi,(2)}\_{t}:=\int\_{0}^{t}X\_{0,r}\otimes\mathrm{d}^{\gamma,\pi}X\_{r}:=\int\_{0}^{t}X\_{r}\otimes\mathrm{d}^{\gamma,\pi}X\_{r}-X\_{0}\otimes X\_{0,t}, and cc is the control function for which ([3.1](https://arxiv.org/html/2602.05898v1#S3.E1 "In item (ii) ‣ Property γ-(RIE). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths")) holds, see Proposition [3.1](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem1 "Proposition 3.1 (Proposition 2.9 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths"). Applying Lyons’ extension theorem, for every N≥3N\geq 3, there exists a unique continuous path 𝕏γ,π,(N):[0,T]→(ℝd)⊗N\mathbb{X}^{\gamma,\pi,(N)}\colon[0,T]\to(\mathbb{R}^{d})^{\otimes N} such that

|  |  |  |
| --- | --- | --- |
|  | (1,X0,⋅,𝕏γ,π,(2),…,𝕏γ,π,(N),…)∈T​((ℝd))(1,X\_{0,\cdot},\mathbb{X}^{\gamma,\pi,(2)},\dots,\mathbb{X}^{\gamma,\pi,(N)},\dots)\in T((\mathbb{R}^{d})) |  |

is a multiplicative functional with finite pp-variation, that is, in particular, |𝕏s,tγ,(N)|≲c​(s,t)Np|\mathbb{X}\_{s,t}^{\gamma,(N)}|\lesssim c(s,t)^{\frac{N}{p}}, (s,t)∈ΔT(s,t)\in\Delta\_{T}, for any N≥1N\geq 1.

Proposition [C.1](https://arxiv.org/html/2602.05898v1#A3.Thmtheorem1 "Proposition C.1. ‣ Appendix C On Lyons’ extension theorem ‣ Universal approximation with signatures of non-geometric rough paths") now states that Lyons’ extension 𝕏γ,π:[0,T]→T​((ℝd))\mathbb{X}^{\gamma,\pi}\colon[0,T]\to T((\mathbb{R}^{d})) coincides with the collection of iterated rough integrals of controlled paths with respect to 𝐗γ,π=(X,𝕏γ,π,(2))\mathbf{X}^{\gamma,\pi}=(X,\mathbb{X}^{\gamma,\pi,(2)}), that is, for N≥3N\geq 3,

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,tγ,π,(N)=∫st𝕏s,rγ,π,(N−1)⊗d𝐗rγ,π,(s,t)∈ΔT,\mathbb{X}\_{s,t}^{\gamma,\pi,(N)}=\int\_{s}^{t}\mathbb{X}\_{s,r}^{\gamma,\pi,(N-1)}\otimes\mathrm{d}\mathbf{X}\_{r}^{\gamma,\pi},\qquad(s,t)\in\Delta\_{T}, |  |

where the rough integral is defined in Lemma [D.1](https://arxiv.org/html/2602.05898v1#A4.Thmtheorem1 "Lemma D.1 (Proposition 2.4 in [ALP24]). ‣ Appendix D Some additional results in rough path theory ‣ Universal approximation with signatures of non-geometric rough paths").

We notice that due to Theorem [D.3](https://arxiv.org/html/2602.05898v1#A4.Thmtheorem3 "Theorem D.3. ‣ Appendix D Some additional results in rough path theory ‣ Universal approximation with signatures of non-geometric rough paths"), the integral exists as a limit of Riemann sums along π\pi. Moreover, for any multi-index I=(i1,…,iN)I=(i\_{1},\dots,i\_{N}) of length NN, because ⟨eI,⋅⟩:(ℝd)⊗N→ℝ\langle e\_{I},\cdot\rangle\colon(\mathbb{R}^{d})^{\otimes N}\to\mathbb{R} is continuous, we observe that

|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝕏s,tγ,π⟩=⟨eI,𝕏s,tγ,π,(N)⟩\displaystyle\langle e\_{I},\mathbb{X}^{\gamma,\pi}\_{s,t}\rangle=\langle e\_{I},\mathbb{X}^{\gamma,\pi,(N)}\_{s,t}\rangle |  |
|  |  |  |
| --- | --- | --- |
|  | =⟨eI,limn→∞∑k=0Nn−1(𝕏s,tknγ,π,(N−1)+γ​(𝕏s,tk+1nγ,π,(N−1)−𝕏s,tknγ,π,(N−1)))⊗Xtkn∨s,tk+1n∧t⟩\displaystyle\quad=\langle e\_{I},\lim\_{n\to\infty}\sum\_{k=0}^{N\_{n}-1}\bigl(\mathbb{X}^{\gamma,\pi,(N-1)}\_{s,t^{n}\_{k}}+\gamma(\mathbb{X}^{\gamma,\pi,(N-1)}\_{s,t^{n}\_{k+1}}-\mathbb{X}^{\gamma,\pi,(N-1)}\_{s,t^{n}\_{k}})\bigr)\otimes X\_{t^{n}\_{k}\vee s,t^{n}\_{k+1}\wedge t}\rangle |  |
|  |  |  |
| --- | --- | --- |
|  | =limn→∞∑k=0Nn−1⟨eI,(𝕏s,tknγ,π,(N−1)+γ​(𝕏s,tk+1nγ,π,(N−1)−𝕏s,tknγ,π,(N−1)))⊗Xtkn∨s,tk+1n∧t⟩,\displaystyle\quad=\lim\_{n\to\infty}\sum\_{k=0}^{N\_{n}-1}\langle e\_{I},(\mathbb{X}^{\gamma,\pi,(N-1)}\_{s,t^{n}\_{k}}+\gamma(\mathbb{X}^{\gamma,\pi,(N-1)}\_{s,t^{n}\_{k+1}}-\mathbb{X}^{\gamma,\pi,(N-1)}\_{s,t^{n}\_{k}}))\otimes X\_{t^{n}\_{k}\vee s,t^{n}\_{k+1}\wedge t}\rangle, |  |

for (s,t)∈ΔT(s,t)\in\Delta\_{T}. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨eI,𝕏s,tγ,π⟩\displaystyle\langle e\_{I},\mathbb{X}^{\gamma,\pi}\_{s,t}\big\rangle | =limn→∞∑k=0Nn−1⟨eI′,𝕏s,tknγ,π,(N−1)+γ​(𝕏s,tk+1nγ,π,(N−1)−𝕏s,tknγ,π,(N−1))⟩​Xtkn∨s,tk+1n∧tiN,\displaystyle=\lim\_{n\to\infty}\sum\_{k=0}^{N\_{n}-1}\langle e\_{I^{\prime}},\mathbb{X}^{\gamma,\pi,(N-1)}\_{s,t^{n}\_{k}}+\gamma(\mathbb{X}^{\gamma,\pi,(N-1)}\_{s,t^{n}\_{k+1}}-\mathbb{X}^{\gamma,\pi,(N-1)}\_{s,t^{n}\_{k}})\rangle\,X^{i\_{N}}\_{t^{n}\_{k}\vee s,t^{n}\_{k+1}\wedge t}, |  |

which yields that

|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝕏s,tγ,π⟩=∫st⟨eI′,𝕏s,rγ,π⟩​dγ,π​XriN,\langle e\_{I},\mathbb{X}^{\gamma,\pi}\_{s,t}\big\rangle=\int\_{s}^{t}\langle e\_{I^{\prime}},\mathbb{X}^{\gamma,\pi}\_{s,r}\big\rangle\,\,\mathrm{d}^{\gamma,\pi}X^{i\_{N}}\_{r}, |  |

where the integral on the right-hand side is well-defined as a rough integral with respect to a controlled path and exists as a limit of Riemann sums along π\pi, see Lemma [D.1](https://arxiv.org/html/2602.05898v1#A4.Thmtheorem1 "Lemma D.1 (Proposition 2.4 in [ALP24]). ‣ Appendix D Some additional results in rough path theory ‣ Universal approximation with signatures of non-geometric rough paths"), Remark [D.2](https://arxiv.org/html/2602.05898v1#A4.Thmtheorem2 "Remark D.2. ‣ Appendix D Some additional results in rough path theory ‣ Universal approximation with signatures of non-geometric rough paths") and Theorem [D.3](https://arxiv.org/html/2602.05898v1#A4.Thmtheorem3 "Theorem D.3. ‣ Appendix D Some additional results in rough path theory ‣ Universal approximation with signatures of non-geometric rough paths"), because r↦⟨eI′,𝕏s,rγ,π⟩r\mapsto\langle e\_{I^{\prime}},\mathbb{X}^{\gamma,\pi}\_{s,r}\rangle is a controlled path w.r.t. XX on [s,t][s,t] and so is XiNX^{i\_{N}}.

This allows us to define the *γ\gamma-signature* as follows.

###### Definition 3.8.

Suppose that X∈C​([0,T];ℝd)X\in C([0,T];\mathbb{R}^{d}) satisfies Property γ\gamma-(RIE) relative to some γ∈[0,1]\gamma\in[0,1], p∈(2,3)p\in(2,3) and a sequence of partitions π=(πn)n∈ℕ\pi=(\pi^{n})\_{n\in\mathbb{N}}.

We recursively set

|  |  |  |
| --- | --- | --- |
|  | ⟨e∅,𝕏tγ,π⟩:=1,⟨eI,𝕏tγ,π⟩:=X0,ti1,I=(i1),\displaystyle\langle e\_{\emptyset},\mathbb{X}^{\gamma,\pi}\_{t}\rangle:=1,\quad\langle e\_{I},\mathbb{X}^{\gamma,\pi}\_{t}\rangle:=X\_{0,t}^{i\_{1}},\quad I=(i\_{1}), |  |
|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝕏tγ,π⟩:=∫0tXri1​dγ,π​Xri2−X0i1​X0,ti2=(𝕏0,tγ,π,(2))i1​i2,I=(i1,i2),\displaystyle\langle e\_{I},\mathbb{X}^{\gamma,\pi}\_{t}\rangle:=\int\_{0}^{t}X^{i\_{1}}\_{r}\,\mathrm{d}^{\gamma,\pi}X^{i\_{2}}\_{r}-X\_{0}^{i\_{1}}X\_{0,t}^{i\_{2}}=(\mathbb{X}^{\gamma,\pi,(2)}\_{0,t})^{i\_{1}i\_{2}},\quad I=(i\_{1},i\_{2}), |  |
|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝕏tγ,π⟩:=∫0t⟨eI′,𝕏rγ,π⟩​dγ,π​Xri|I|\displaystyle\langle e\_{I},\mathbb{X}^{\gamma,\pi}\_{t}\rangle:=\int\_{0}^{t}\langle e\_{I^{\prime}},\mathbb{X}\_{r}^{\gamma,\pi}\rangle\,\mathrm{d}^{\gamma,\pi}X\_{r}^{i\_{|I|}} |  |
|  |  |  |
| --- | --- | --- |
|  | =limn→∞∑k=0Nn−1(⟨eI′,𝕏tknγ,π⟩+γ​(⟨eI′,𝕏tk+1nγ,π⟩−⟨eI′,𝕏tknγ,π⟩))​Xtkn∧t,tk+1n∧ti|I|,\displaystyle\qquad\qquad=\lim\_{n\to\infty}\sum\_{k=0}^{N\_{n}-1}(\langle e\_{I^{\prime}},\mathbb{X}^{\gamma,\pi}\_{t^{n}\_{k}}\rangle+\gamma(\langle e\_{I^{\prime}},\mathbb{X}^{\gamma,\pi}\_{t^{n}\_{k+1}}\rangle-\langle e\_{I^{\prime}},\mathbb{X}^{\gamma,\pi}\_{t^{n}\_{k}}\rangle))X^{i\_{|I|}}\_{t^{n}\_{k}\wedge t,t^{n}\_{k+1}\wedge t}, |  |

where the integral exists as a rough integral of controlled paths, for I=(i1,…,i|I|)I=(i\_{1},\ldots,i\_{|I|}), |I|>2|I|>2, and t∈[0,T]t\in[0,T]. Then 𝕏γ,π:[0,T]→T​((ℝd))\mathbb{X}^{\gamma,\pi}\colon[0,T]\to T((\mathbb{R}^{d})) is well-defined and is called the *γ\gamma-signature* of XX. Its projection 𝕏γ,π,N\mathbb{X}^{\gamma,\pi,N} on TN​(ℝd)T^{N}(\mathbb{R}^{d}) is given by

|  |  |  |
| --- | --- | --- |
|  | 𝕏tγ,π,N=ΠN​(𝕏tγ,π)=∑|I|≤N⟨eI,𝕏tγ,π⟩​eI,\mathbb{X}^{\gamma,\pi,N}\_{t}=\Pi\_{N}(\mathbb{X}^{\gamma,\pi}\_{t})=\sum\_{|I|\leq N}\langle e\_{I},\mathbb{X}^{\gamma,\pi}\_{t}\rangle e\_{I}, |  |

and called *γ\gamma-signature of XX truncated at level NN*, which takes values in TN​(ℝd)T^{N}(\mathbb{R}^{d}) for all t∈[0,T]t\in[0,T]. The increments of the γ\gamma-signature 𝕏γ,π\mathbb{X}^{\gamma,\pi} are defined by

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,tγ,π:=(𝕏sγ,π)−1⊗𝕏tγ,π,(s,t)∈ΔT.\mathbb{X}^{\gamma,\pi}\_{s,t}:=(\mathbb{X}^{\gamma,\pi}\_{s})^{-1}\otimes\mathbb{X}^{\gamma,\pi}\_{t},\qquad(s,t)\in\Delta\_{T}. |  |

###### Remark 3.9.

Remark [3.6](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem6 "Remark 3.6. ‣ 3.2. The 𝜸-signature ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") states that

|  |  |  |
| --- | --- | --- |
|  | Π2​(𝕏tγ,π,o)=𝕏tγ,π,o,2=(1,X0,t,𝕏0,tγ,π,o,(2))=(1,X0,t,𝕏0,t12,π,(2))=Π2​(𝕏t12,π),\Pi\_{2}(\mathbb{X}^{\gamma,\pi,o}\_{t})=\mathbb{X}^{\gamma,\pi,o,2}\_{t}=(1,X\_{0,t},\mathbb{X}^{\gamma,\pi,o,(2)}\_{0,t})=(1,X\_{0,t},\mathbb{X}^{\frac{1}{2},\pi,(2)}\_{0,t})=\Pi\_{2}(\mathbb{X}^{\frac{1}{2},\pi}\_{t}), |  |

that is, if XX satisfies Property γ\gamma-(RIE), the signature of the corresponding weakly geometric rough path truncated at level 22 and the 1/21/2-signature of XX truncated at level 22 coincide. Moreover, since the γ\gamma-signature is defined to be the unique Lyons’ extension, the 1/21/2-signature 𝕏12,π\mathbb{X}^{\frac{1}{2},\pi} is a group-like valued path, i.e., 𝕏t12,π∈G​((ℝd))\mathbb{X}^{\frac{1}{2},\pi}\_{t}\in G((\mathbb{R}^{d})), and coincides with the signature of the weakly geometric rough path 𝕏γ,π,o,2=𝕏12,π,o,2=(1,X0,⋅,𝕏12,π)\mathbb{X}^{\gamma,\pi,o,2}=\mathbb{X}^{\frac{1}{2},\pi,o,2}=(1,X\_{0,\cdot},\mathbb{X}^{\frac{1}{2},\pi}), see Definition [2.3](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem3 "Definition 2.3. ‣ 2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths").

Now, suppose that X∈C​([0,T];ℝd)X\in C([0,T];\mathbb{R}^{d}) satisfies Property γ\gamma-(RIE) relative to some γ∈[0,1]\gamma\in[0,1], p∈(2,3)p\in(2,3) and a sequence of partitions π=(πn)n∈ℕ\pi=(\pi^{n})\_{n\in\mathbb{N}}. We set

|  |  |  |  |
| --- | --- | --- | --- |
| (3.3) |  | X^:=(⋅,X,Qγ,π​(X))∈C​([0,T];ℝd^),\widehat{X}:=(\cdot,X,Q^{\gamma,\pi}(X))\in C([0,T];\mathbb{R}^{\hat{d}}), |  |

where d^=1+d+d​(d+1)2\hat{d}=1+d+\frac{d(d+1)}{2}, and

|  |  |  |
| --- | --- | --- |
|  | Qγ,π​(X):=([X1,X1]γ,π,…,[X1,Xd]γ,π,[X2,X2]γ,π,…,[X2,Xd]γ,π,…,[Xd,Xd]γ,π).Q^{\gamma,\pi}(X):=([X^{1},X^{1}]^{\gamma,\pi},\dots,[X^{1},X^{d}]^{\gamma,\pi},[X^{2},X^{2}]^{\gamma,\pi},\dots,[X^{2},X^{d}]^{\gamma,\pi},\dots,[X^{d},X^{d}]^{\gamma,\pi}). |  |

We first notice that X^\widehat{X} is the path extended by its rough path bracket and time, as introduced in Section [2.3](https://arxiv.org/html/2602.05898v1#S2.SS3 "2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths"), because [𝐗γ,π]=[X]γ,π[\mathbf{X}^{\gamma,\pi}]=[X]^{\gamma,\pi}. We also recall that [X]12,π=0[X]^{\frac{1}{2},\pi}=0, see Lemma [3.2](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem2 "Lemma 3.2 (Lemma 2.10 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths"), that is, if γ=12\gamma=\frac{1}{2}, we may consider X^=(⋅,X)\widehat{X}=(\cdot,X), and we have that d^=1+d\hat{d}=1+d.

It follows by applying Lemma [3.2](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem2 "Lemma 3.2 (Lemma 2.10 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths"), and Lemma [3.4](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") to (⋅,0,0)+(0,X,0)+(0,0,Qγ,π​(X))(\cdot,0,0)+(0,X,0)+(0,0,Q^{\gamma,\pi}(X)) that X^\widehat{X} satisfies Property γ\gamma-(RIE) relative to γ\gamma, pp and π\pi.

As before we use e0e\_{0} for the time component and εi​j\varepsilon\_{ij} for the component of X^\widehat{X} referring to [Xi,Xj]γ,π[X^{i},X^{j}]^{\gamma,\pi}, i.e. ⟨εi​j,𝕏^tγ,π⟩:=[Xi,Xj]tγ,π\langle\varepsilon\_{ij},\widehat{\mathbb{X}}\_{t}^{\gamma,\pi}\rangle:=[X^{i},X^{j}]\_{t}^{\gamma,\pi}, i,j=1,…,di,j=1,\ldots,d, i≤ji\leq j, t∈[0,T]t\in[0,T].

### 3.3. A universal approximation theorem with 𝜸\boldsymbol{\gamma}-signatures

As an example of Theorem [2.8](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem8 "Theorem 2.8. ‣ 2.4. Universal approximation with signatures of general rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths"), the universal approximation property holds true for the γ\gamma-signature of paths satisfying Property γ\gamma-(RIE) for γ∈[0,1]\gamma\in[0,1], γ≠12\gamma\neq\frac{1}{2}.

###### Corollary 3.10.

Let γ∈[0,1]\gamma\in[0,1], γ≠12\gamma\neq\frac{1}{2}, p∈(2,3)p\in(2,3) and π=(πn)n∈ℕ\pi=(\pi^{n})\_{n\in\mathbb{N}} be a sequence of partitions of the interval [0,T][0,T]. Let K⊂𝒞^p​([0,T];ℝd^)K\subset\widehat{\mathcal{C}}^{p}([0,T];\mathbb{R}^{\hat{d}}) be a compact subset, bounded with respect to the rough path norm, and consider a continuous function f:K→ℝf\colon K\to\mathbb{R}. Further, for some L>0L>0, let Kγ,π,L⊂KK\_{\gamma,\pi,L}\subset K be the subset defined by

|  |  |  |
| --- | --- | --- |
|  | Kγ,π,L:={𝐗^γ,π=(X^,𝕏^γ,π,(2))∈K:X​ satisfies Property γ-(RIE) relative to γ, pand ​π​ such that ​‖(X^,𝕏^γ,π,(2))‖p+‖[X^]γ,π‖p2≤L}.\displaystyle K\_{\gamma,\pi,L}:=\Biggl\{\widehat{\mathbf{X}}^{\gamma,\pi}=(\widehat{X},\widehat{\mathbb{X}}^{\gamma,\pi,(2)})\in K\,:\,\begin{aligned} &X\text{ satisfies Property $\gamma$-{(RIE)} relative to $\gamma$, $p$}\\ &\text{and }\pi\text{ such that }\|(\widehat{X},\widehat{\mathbb{X}}^{\gamma,\pi,(2)})\|\_{p}+\|[\widehat{X}]^{\gamma,\pi}\|\_{\frac{p}{2}}\leq L\end{aligned}\Biggr\}. |  |

Then for every ε>0\varepsilon>0, there exists a linear functional ℓγ∈T​(ℝd^)\ell^{\gamma}\in T(\mathbb{R}^{\hat{d}}) such that

|  |  |  |
| --- | --- | --- |
|  | sup𝐗^γ,π∈Kγ,π,L|f​(𝐗^γ,π)−⟨ℓγ,𝕏^Tγ,π⟩|<ε,\sup\_{\widehat{\mathbf{X}}^{\gamma,\pi}\in K\_{\gamma,\pi,L}}|f(\widehat{\mathbf{X}}^{\gamma,\pi})-\langle\ell^{\gamma},\widehat{\mathbb{X}}^{\gamma,\pi}\_{T}\rangle|<\varepsilon, |  |

where 𝕏^γ,π\widehat{\mathbb{X}}^{\gamma,\pi} denotes the γ\gamma-signature of X^\widehat{X}.

###### Proof.

We only need to check that Kγ,π,L⊂KLK\_{\gamma,\pi,L}\subset K\_{L}, where KLK\_{L} denotes the set defined in Theorem [2.8](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem8 "Theorem 2.8. ‣ 2.4. Universal approximation with signatures of general rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths"). Then the claim follows immediately from Theorem [2.8](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem8 "Theorem 2.8. ‣ 2.4. Universal approximation with signatures of general rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths").

Let 𝐗^γ,π=(X^,𝕏^γ,π,(2))∈Kγ,π,L\widehat{\mathbf{X}}^{\gamma,\pi}=(\widehat{X},\widehat{\mathbb{X}}^{\gamma,\pi,(2)})\in K\_{\gamma,\pi,L}. Since XX satisfies Property γ\gamma-(RIE) relative to γ\gamma, pp and π\pi, it holds that 𝐗γ,π=(X,𝕏γ,π,(2))∈𝒞p​([0,T];ℝd)\mathbf{X}^{\gamma,\pi}=(X,\mathbb{X}^{\gamma,\pi,(2)})\in\mathcal{C}^{p}([0,T];\mathbb{R}^{d}), see Proposition [3.1](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem1 "Proposition 3.1 (Proposition 2.9 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths"). Further, by [[ALP24](https://arxiv.org/html/2602.05898v1#bib.bibx6), Proposition 2.18], we have that the rough path bracket [𝐗γ,π][\mathbf{X}^{\gamma,\pi}] coincides with (1−2​γ)​[X](1-2\gamma)[X], where [X][X] denotes the quadratic variation of XX along π\pi in the sense of Föllmer, equal to [X]γ,π[X]^{\gamma,\pi}, which yields that [𝐗γ,π]=[X]γ,π[\mathbf{X}^{\gamma,\pi}]=[X]^{\gamma,\pi}, i.e. Q​(X)=Qγ,π​(X)Q(X)=Q^{\gamma,\pi}(X). Also, X^\widehat{X} satisfies Property γ\gamma-(RIE), see Lemma [3.4](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths"), so that [𝐗^γ,π]=[X^]γ,π[\widehat{\mathbf{X}}^{\gamma,\pi}]=[\widehat{X}]^{\gamma,\pi}, and thus, 𝕏^γ,π∈KL\widehat{\mathbb{X}}^{\gamma,\pi}\in K\_{L}.
∎

We immediately obtain the following corollary. Assuming that the path satisfies Property 1/21/2-(RIE), by Remark [3.6](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem6 "Remark 3.6. ‣ 3.2. The 𝜸-signature ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths"), the Stratonovich-type lift is weakly geometric, and the statement also applies directly to the time-extended Stratonovich-type signature.

###### Corollary 3.11.

Let K⊂C^op​-var​([0,T];G2​(ℝ1+d))K\subset\widehat{C}\_{o}^{p\textup{-var}}([0,T];G^{2}(\mathbb{R}^{1+d})) be a compact subset, bounded with respect to the pp-variation norm, and consider a continuous function f:K→ℝf\colon K\to\mathbb{R}. Further, define

|  |  |  |
| --- | --- | --- |
|  | K12,π:={𝕏^2∈K:X​ satisfies Property 1/2-(RIE) relative to p and πsuch that ​𝕏^(1)=X^0,⋅​ and ​𝕏^(2)=𝕏^12,π,(2)}.\displaystyle K\_{\frac{1}{2},\pi}:=\Biggl\{\widehat{\mathbb{X}}^{2}\in K\,:\,\begin{aligned} &X\text{ satisfies Property $1/2$-{(RIE)} relative to $p$ and $\pi$}\\ &\text{such that }\widehat{\mathbb{X}}^{(1)}=\widehat{X}\_{0,\cdot}\text{ and }\widehat{\mathbb{X}}^{(2)}=\widehat{\mathbb{X}}^{\frac{1}{2},\pi,(2)}\\ \end{aligned}\Biggr\}. |  |

Then for every ε>0\varepsilon>0, there exists a linear functional ℓ∈T​(ℝ1+d)\ell\in T(\mathbb{R}^{1+d}) such that

|  |  |  |
| --- | --- | --- |
|  | sup𝕏^12,π,2∈K12,π|f​(𝕏^12,π,2)−⟨ℓ,𝕏^T12,π⟩|<ε.\sup\_{\widehat{\mathbb{X}}^{\frac{1}{2},\pi,2}\in K\_{\frac{1}{2},\pi}}|f(\widehat{\mathbb{X}}^{\frac{1}{2},\pi,2})-\langle\ell,\widehat{\mathbb{X}}^{\frac{1}{2},\pi}\_{T}\rangle|<\varepsilon. |  |

## 4. Application to continuous semimartingales

In this section, we apply the deterministic theory developed in Section [2](https://arxiv.org/html/2602.05898v1#S2 "2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths") and Section [3.3](https://arxiv.org/html/2602.05898v1#S3.SS3 "3.3. A universal approximation theorem with 𝜸-signatures ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") to continuous semimartingales.

In fact, continuous semimartingales fit well into the theory of signatures when adopting the notion of stochastic integration. That is, the signature can be defined as the collection of iterated integrals via stochastic integration. Because it is obeying first order calculus, one usually considers Stratonovich integration, which almost surely coincides with Lyons’ lift, thus classically implying a universal approximation theorem for continuous path functionals.

Throughout, let X=(Xt)t∈[0,T]X=(X\_{t})\_{t\in[0,T]} be a dd-dimensional continuous semimartingale, defined on a probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) with a filtration (ℱt)t∈[0,T](\mathcal{F}\_{t})\_{t\in[0,T]} satisfying the usual conditions, i.e., completeness and right-continuity.

###### Definition 4.1.

Let XX be a dd-dimensional continuous semimartingale. Its *Stratonovich signature* is the stochastic process 𝕏∘=(𝕏t∘)t∈[0,T]\mathbb{X}^{\circ}=(\mathbb{X}^{\circ}\_{t})\_{t\in[0,T]} with values in T1​((ℝd))T\_{1}((\mathbb{R}^{d})), whose components are recursively defined by

|  |  |  |
| --- | --- | --- |
|  | ⟨e∅,𝕏t∘⟩:=1,⟨eI,𝕏t∘⟩:=∫0t⟨eI′,𝕏r∘⟩∘dXri|I|,\langle e\_{\emptyset},\mathbb{X}^{\circ}\_{t}\rangle:=1,\qquad\langle e\_{I},\mathbb{X}^{\circ}\_{t}\rangle:=\int\_{0}^{t}\langle e\_{I^{\prime}},\mathbb{X}^{\circ}\_{r}\rangle\circ\mathrm{d}X\_{r}^{i\_{|I|}}, |  |

for each I=(i1,…,i|I|)I=(i\_{1},\dots,i\_{|I|}) and t∈[0,T]t\in[0,T], where ∘\circ denotes the Stratonovich integral. Its projection 𝕏∘,≤N\mathbb{X}^{\circ,\leq N} on TN​(ℝd)T^{N}(\mathbb{R}^{d}) is given by

|  |  |  |
| --- | --- | --- |
|  | 𝕏t∘,N=ΠN​(𝕏t∘)=∑|I|≤N⟨eI,𝕏t∘⟩​eI,\mathbb{X}^{\circ,N}\_{t}=\Pi\_{N}(\mathbb{X}^{\circ}\_{t})=\sum\_{|I|\leq N}\langle e\_{I},\mathbb{X}^{\circ}\_{t}\rangle e\_{I}, |  |

and called *Stratonovich signature of XX truncated at level NN*, which takes values in GN​(ℝd)G^{N}(\mathbb{R}^{d}) for all t∈[0,T]t\in[0,T]. The increments of the Stratonovich signature 𝕏∘\mathbb{X}^{\circ} are defined by

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,t∘:=(𝕏s∘)−1⊗𝕏t∘,(s,t)∈ΔT.\mathbb{X}^{\circ}\_{s,t}:=(\mathbb{X}^{\circ}\_{s})^{-1}\otimes\mathbb{X}^{\circ}\_{t},\qquad(s,t)\in\Delta\_{T}. |  |

It turns out that, if the semimartingale XX satisfies Property γ\gamma-(RIE) relative to γ∈[0,1]\gamma\in[0,1], p∈(2,3)p\in(2,3) and a suitable sequence of partitions, we obtain a canonical signature which corresponds ℙ\mathbb{P}-almost surely with the signature defined via Lyons’ lift and the Stratonovich signature.

###### Lemma 4.2.

Let γ∈[0,1]\gamma\in[0,1], let p∈(2,3)p\in(2,3) and let πn={τkn}\pi^{n}=\{\tau^{n}\_{k}\}, n∈ℕn\in\mathbb{N}, be a sequence of adapted partitions (so that each τkn\tau^{n}\_{k} is a stopping time), such that for almost every ω∈Ω\omega\in\Omega, (πn​(ω))n∈ℕ(\pi^{n}(\omega))\_{n\in\mathbb{N}} is a sequence of (finite) partitions of [0,T][0,T] with vanishing mesh size.

Let XX be a continuous dd-dimensional semimartingale, and suppose that for almost every ω∈Ω\omega\in\Omega, sup{|Xτkn​(ω),τk+1n​(ω)(ω)|:k=0,…,Nn−1}\sup\{|X\_{\tau^{n}\_{k}(\omega),\tau^{n}\_{k+1}(\omega)}(\omega)|\,:k=0,\dots,N\_{n}-1\} converges to 0 as n→∞n\to\infty, and that the sample path X​(ω)X(\omega) satisfies Property γ\gamma-(RIE) relative to γ\gamma, pp and (πn​(ω))n∈ℕ(\pi^{n}(\omega))\_{n\in\mathbb{N}}.

1. (i)

   The random weakly geometric rough path pathwise defined via Proposition [3.1](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem1 "Proposition 3.1 (Proposition 2.9 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") for γ=12\gamma=\frac{1}{2} and the random weakly geometric rough path pathwise defined via Lemma [3.5](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.2. The 𝜸-signature ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") for γ∈[0,1]\gamma\in[0,1] coincide ℙ\mathbb{P}-almost surely.
2. (ii)

   The random weakly geometric rough path pathwise defined via Lemma [3.5](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.2. The 𝜸-signature ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") and the Stratonovich signature of XX truncated at level 22 coincide ℙ\mathbb{P}-almost surely.
3. (iii)

   The random signature 𝕏o\mathbb{X}^{o} pathwise defined via Definition [2.3](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem3 "Definition 2.3. ‣ 2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths"), or more precisely, Remark [3.7](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem7 "Remark 3.7. ‣ 3.2. The 𝜸-signature ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths"), the random signature 𝕏12,π\mathbb{X}^{\frac{1}{2},\pi} pathwise defined via Definition [3.8](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem8 "Definition 3.8. ‣ 3.2. The 𝜸-signature ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") and the Stratonovich signature 𝕏∘\mathbb{X}^{\circ} of XX coincide ℙ\mathbb{P}-almost surely.

###### Proof.

*(i):* By Lemma [3.3](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem3 "Lemma 3.3 (Lemma 2.16 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths"), we know that if a path satisfies Property γ\gamma-(RIE) relative to some γ∈[0,1]\gamma\in[0,1], then it particularly satisfies Property 1/21/2-(RIE). Then the claim holds true because of Lemma [2.1](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem1 "Lemma 2.1. ‣ 2.2. Essentials on rough path theory ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths") and 𝕏0,t12,π,(2)=𝕏0,t12,π,o,(2)\mathbb{X}^{\frac{1}{2},\pi,(2)}\_{0,t}=\mathbb{X}^{\frac{1}{2},\pi,o,(2)}\_{0,t}, t∈[0,T]t\in[0,T].

*(ii):* By construction, the pathwise rough integral ∫0tXr​(ω)⊗dγ,π​Xr​(ω)\int\_{0}^{t}X\_{r}(\omega)\otimes\mathrm{d}^{\gamma,\pi}X\_{r}(\omega) constructed via Property γ\gamma-(RIE) is given by the limit as n→∞n\to\infty of Riemann sums:

|  |  |  |
| --- | --- | --- |
|  | ∑k=0Nn−1(Xτkn​(ω)​(ω)+γ​Xτkn​(ω),τk+1n​(ω))⊗Xτkn​(ω)∧t,τk+1n​(ω)∧t​(ω).\sum\_{k=0}^{N\_{n}-1}(X\_{\tau^{n}\_{k}(\omega)}(\omega)+\gamma X\_{\tau^{n}\_{k}(\omega),\tau^{n}\_{k+1}(\omega)})\otimes X\_{\tau^{n}\_{k}(\omega)\wedge t,\tau^{n}\_{k+1}(\omega)\wedge t}(\omega). |  |

Suppose that γ=12\gamma=\frac{1}{2}. Then it is known that these Riemann sums converge uniformly in probability to the Stratonovich integral ∫0tXr⊗∘dXr\int\_{0}^{t}X\_{r}\otimes\circ\mathrm{d}X\_{r}, see e.g. [[Pro05](https://arxiv.org/html/2602.05898v1#bib.bibx50), Chapter II, Theorem 21, Theorem 22]. And the result follows from the (almost sure) uniqueness of limits; see also part (i) of [[DKP25](https://arxiv.org/html/2602.05898v1#bib.bibx28), Lemma 4.3].

Suppose that γ≠12\gamma\neq\frac{1}{2}. Then adding [X​(ω)]0,tγ,πn[X(\omega)]^{\gamma,\pi^{n}}\_{0,t},

|  |  |  |
| --- | --- | --- |
|  | ∑k=0Nn−1(Xτkn​(ω)​(ω)+γ​Xτkn​(ω),τk+1n​(ω))⊗Xτkn​(ω)∧t,τk+1n​(ω)∧t​(ω)\displaystyle\sum\_{k=0}^{N\_{n}-1}(X\_{\tau^{n}\_{k}(\omega)}(\omega)+\gamma X\_{\tau^{n}\_{k}(\omega),\tau^{n}\_{k+1}(\omega)})\otimes X\_{\tau^{n}\_{k}(\omega)\wedge t,\tau^{n}\_{k+1}(\omega)\wedge t}(\omega) |  |
|  |  |  |
| --- | --- | --- |
|  | +12​(1−2​γ)​Xτkn​(ω)∧t,τk+1n​(ω)∧t​(ω)⊗Xτkn​(ω)∧t,τk+1n​(ω)∧t​(ω)\displaystyle\qquad+\frac{1}{2}(1-2\gamma)X\_{\tau^{n}\_{k}(\omega)\wedge t,\tau^{n}\_{k+1}(\omega)\wedge t}(\omega)\otimes X\_{\tau^{n}\_{k}(\omega)\wedge t,\tau^{n}\_{k+1}(\omega)\wedge t}(\omega) |  |
|  |  |  |
| --- | --- | --- |
|  | =∑k=0Nn−1(Xτkn​(ω)​(ω)+12​Xτkn​(ω)∧t,τk+1n​(ω)∧t)⊗Xτkn​(ω)∧t,τk+1n​(ω)∧t​(ω)\displaystyle\quad=\sum\_{k=0}^{N\_{n}-1}(X\_{\tau^{n}\_{k}(\omega)}(\omega)+\frac{1}{2}X\_{\tau^{n}\_{k}(\omega)\wedge t,\tau^{n}\_{k+1}(\omega)\wedge t})\otimes X\_{\tau^{n}\_{k}(\omega)\wedge t,\tau^{n}\_{k+1}(\omega)\wedge t}(\omega) |  |
|  |  |  |
| --- | --- | --- |
|  | +γ(Xτkn​(ω),τk+1n​(ω))−Xτkn​(ω)∧t,τk+1n​(ω)∧t(ω))⊗Xτkn​(ω)∧t,τk+1n​(ω)∧t(ω),\displaystyle\qquad+\gamma(X\_{\tau^{n}\_{k}(\omega),\tau^{n}\_{k+1}(\omega)})-X\_{\tau^{n}\_{k}(\omega)\wedge t,\tau^{n}\_{k+1}(\omega)\wedge t}(\omega))\otimes X\_{\tau^{n}\_{k}(\omega)\wedge t,\tau^{n}\_{k+1}(\omega)\wedge t}(\omega), |  |

which again converges uniformly in probability to the Stratonovich integral ∫0tXr⊗∘dXr\int\_{0}^{t}X\_{r}\otimes\circ\,\mathrm{d}X\_{r}.

*(iii):* By (i), we have that 𝕏0,t12,π,(2)=𝕏0,t12,π,o,(2)\mathbb{X}\_{0,t}^{\frac{1}{2},\pi,(2)}=\mathbb{X}\_{0,t}^{\frac{1}{2},\pi,o,(2)}, t∈[0,T]t\in[0,T]. And since Lyons’ lift is unique, the random signatures pathwise defined via Definition [2.3](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem3 "Definition 2.3. ‣ 2.3. Definition and properties of signatures ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths") (Lyons’ lift of the weakly geometric rough path) and via Definition [3.8](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem8 "Definition 3.8. ‣ 3.2. The 𝜸-signature ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") (1/21/2-signature) coincide ℙ\mathbb{P}-almost surely, noting that the 1/21/2-signature coincides with the Lyons’ extension of (1,X^,𝕏^12,π,(2))(1,\widehat{X},\widehat{\mathbb{X}}^{\frac{1}{2},\pi,(2)}), see Definition [3.8](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem8 "Definition 3.8. ‣ 3.2. The 𝜸-signature ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") and Appendix [C](https://arxiv.org/html/2602.05898v1#A3 "Appendix C On Lyons’ extension theorem ‣ Universal approximation with signatures of non-geometric rough paths").

By (ii), the random weakly geometric rough path and the Stratonovich signature of XX truncated at level 22 coincide ℙ\mathbb{P}-almost surely, and take values in G2​(ℝd)G^{2}(\mathbb{R}^{d}). Since Lyons’ lift is unique, see [[FV10](https://arxiv.org/html/2602.05898v1#bib.bibx32), Theorem 9.5], and the Stratonovich signature of XX truncated at any level N≥3N\geq 3 takes values in GN​(ℝd)G^{N}(\mathbb{R}^{d}), and so does the random signature truncated at level NN pathwise defined via Lyons’ lift of the weakly geometric rough path, the proof is complete.
∎

###### Corollary 4.3.

Let XX be a dd-dimensional continuous semimartingale, X^:=(⋅,X)\widehat{X}:=(\cdot,X), and let 𝒮(2):={𝕏^∘,2​(ω):ω∈Ω}\mathcal{S}^{(2)}:=\{\widehat{\mathbb{X}}^{\circ,2}(\omega):\omega\in\Omega\}. Further, let p∈(2,3)p\in(2,3) and K⊂C^op​-var​([0,T];G2​(ℝ1+d))K\subset\widehat{C}\_{o}^{p\textup{-var}}([0,T];G^{2}(\mathbb{R}^{1+d})) be a compact subset of the subspace of time-extended weakly geometric rough paths, see Theorem [2.11](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem11 "Theorem 2.11. ‣ 2.5. Discussion on approximation with weakly geometric rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths"), bounded with respect to the pp-variation norm, and consider a continuous function f:K→ℝf\colon K\to\mathbb{R}. Then for every ε>0\varepsilon>0, there exists a linear functional ℓ∈T​(ℝ1+d)\ell\in T(\mathbb{R}^{1+d}) such that for almost every ω∈Ω\omega\in\Omega,

|  |  |  |
| --- | --- | --- |
|  | |f​(𝕏^∘,2​(ω))−⟨ℓ,𝕏^T∘​(ω)⟩|<εfor all𝕏^∘,2​(ω)∈K∩𝒮(2),|f(\widehat{\mathbb{X}}^{\circ,2}(\omega))-\langle\ell,\widehat{\mathbb{X}}^{\circ}\_{T}(\omega)\rangle|<\varepsilon\qquad\text{for all}\quad\widehat{\mathbb{X}}^{\circ,2}(\omega)\in K\cap\mathcal{S}^{(2)}, |  |

where 𝕏^∘\widehat{\mathbb{X}}^{\circ} denotes the Stratonovich signature of X^\widehat{X}.

Analogously to the Stratonovich signature, we now define the Itô signature of a continuous semimartingale via iterated stochastic Itô integration, which may be the preferred choice from a modeling perspective when having, for example, a financial application in mind.

###### Definition 4.4.

Let XX be a dd-dimensional continuous semimartingale. Its *Itô signature* is the stochastic process 𝕏=(𝕏t)t∈[0,T]\mathbb{X}=(\mathbb{X}\_{t})\_{t\in[0,T]} with values in T1​((ℝd))T\_{1}((\mathbb{R}^{d})), whose components are recursively defined by

|  |  |  |
| --- | --- | --- |
|  | ⟨e∅,𝕏t⟩:=1,⟨eI,𝕏t∞⟩:=∫0t⟨eI′,𝕏r⟩​dXri|I|,\langle e\_{\emptyset},\mathbb{X}\_{t}\rangle:=1,\qquad\langle e\_{I},\mathbb{X}^{\infty}\_{t}\rangle:=\int\_{0}^{t}\langle e\_{I^{\prime}},\mathbb{X}\_{r}\rangle\,\mathrm{d}X\_{r}^{i\_{|I|}}, |  |

for each I=(i1,…,i|I|)I=(i\_{1},\dots,i\_{|I|}) and t∈[0,T]t\in[0,T], where the integral is given as an Itô integral. Its projection 𝕏N\mathbb{X}^{N} on TN​(ℝd)T^{N}(\mathbb{R}^{d}) is given by

|  |  |  |
| --- | --- | --- |
|  | 𝕏tN=ΠN​(𝕏t)=∑|I|≤N⟨eI,𝕏t⟩​eI,\mathbb{X}^{N}\_{t}=\Pi\_{N}(\mathbb{X}\_{t})=\sum\_{|I|\leq N}\langle e\_{I},\mathbb{X}\_{t}\rangle e\_{I}, |  |

and called *Itô signature of XX truncated at level NN*. The increments of the signature 𝕏∞\mathbb{X}^{\infty} are defined by

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,t:=(𝕏s)−1⊗𝕏t,(s,t)∈ΔT.\mathbb{X}\_{s,t}:=(\mathbb{X}\_{s})^{-1}\otimes\mathbb{X}\_{t},\qquad(s,t)\in\Delta\_{T}. |  |

Due to Theorem [2.8](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem8 "Theorem 2.8. ‣ 2.4. Universal approximation with signatures of general rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths"), we can now formulate a probabilistic version of the universal approximation theorem, using the notion of the Itô signature.

###### Corollary 4.5.

Let XX be a dd-dimensional continuous semimartingale. We define the random variable

|  |  |  |
| --- | --- | --- |
|  | X^:=(⋅,X,Q​(X)),\widehat{X}:=(\cdot,X,Q(X)), |  |

with values in C​([0,T];ℝd^)C([0,T];\mathbb{R}^{\hat{d}}) for d^=1+d+d​(d+1)2\hat{d}=1+d+\frac{d(d+1)}{2}, where

|  |  |  |
| --- | --- | --- |
|  | Q​(X):=([X1,X1],…,[X1,Xd],[X2,X2],…,[X2,Xd],…,[Xd,Xd]),Q(X):=([X^{1},X^{1}],\ldots,[X^{1},X^{d}],[X^{2},X^{2}],\ldots,[X^{2},X^{d}],\ldots,[X^{d},X^{d}]), |  |

where [X]=([Xi,Xj])1≤i,j≤d[X]=([X^{i},X^{j}])\_{1\leq i,j\leq d} denotes the quadratic (co-)variation of XX. Let p∈(2,3)p\in(2,3). For some L>0L>0, let

|  |  |  |
| --- | --- | --- |
|  | 𝒮L(2):={𝐗^​(ω)=(X^​(ω),𝕏^(2)​(ω)):ω∈Ω,(X​(ω),𝕏(2)​(ω))∈𝒞p​([0,T];ℝd),X^​(ω)=(⋅,X​(ω),Q​(X)​(ω)),‖(X^​(ω),𝕏^(2)​(ω))‖p+‖[X^]​(ω)‖p2≤L},\displaystyle\mathcal{S}^{(2)}\_{L}:=\left\{\widehat{\mathbf{X}}(\omega)=(\widehat{X}(\omega),\widehat{\mathbb{X}}^{(2)}(\omega))\,:\,\begin{aligned} &\omega\in\Omega,\,(X(\omega),\mathbb{X}^{(2)}(\omega))\in\mathcal{C}^{p}([0,T];\mathbb{R}^{d}),\\ &\widehat{X}(\omega)=(\cdot,X(\omega),Q(X)(\omega)),\\ &\|(\widehat{X}(\omega),\widehat{\mathbb{X}}^{(2)}(\omega))\|\_{p}+\|[\widehat{X}](\omega)\|\_{\frac{p}{2}}\leq L\end{aligned}\right\}, |  |

where 𝕏s,t(2):=∫st(Xr−Xs)⊗dXr\mathbb{X}^{(2)}\_{s,t}:=\int\_{s}^{t}(X\_{r}-X\_{s})\otimes\mathrm{d}X\_{r}, (s,t)∈ΔT(s,t)\in\Delta\_{T}, similarly we define 𝕏^(2)\widehat{\mathbb{X}}^{(2)}. Further, let K⊂𝒞^p​([0,T];ℝd^)K\subset\widehat{\mathcal{C}}^{p}([0,T];\mathbb{R}^{\hat{d}}) be a compact subset of the subspace of rough paths extended by time and the bracket terms, bounded with respect to the rough path norm, and consider a continuous function f:K→ℝf\colon K\to\mathbb{R}. Then for every ε>0\varepsilon>0, there exists a linear functional ℓ∈T​(ℝd^)\ell\in T(\mathbb{R}^{\hat{d}}) such that for almost every ω∈Ω\omega\in\Omega,

|  |  |  |
| --- | --- | --- |
|  | |f​(𝐗^​(ω))−⟨ℓ,𝕏^T​(ω)⟩|<εfor all𝐗^​(ω)∈K∩𝒮L(2),|f(\widehat{\mathbf{X}}(\omega))-\langle\ell,\widehat{\mathbb{X}}\_{T}(\omega)\rangle|<\varepsilon\qquad\text{for all}\quad\widehat{\mathbf{X}}(\omega)\in K\cap\mathcal{S}^{(2)}\_{L}, |  |

where 𝕏^\widehat{\mathbb{X}} denotes the Itô signature of X^\widehat{X}.

###### Proof.

We use that a semimartingale can be lifted to a random rough path via its iterated Itô integrals, see e.g. [[FZ18](https://arxiv.org/html/2602.05898v1#bib.bibx33), Theorem 6.5], and that the corresponding rough path bracket coincides almost surely with the quadratic variation of the semimartingale, see e.g. [[FH20](https://arxiv.org/html/2602.05898v1#bib.bibx29), Remark 2.7]. The claim then immediately follows from the pathwise universal approximation theorem for linear functionals of the signature of general rough paths, which is Theorem [2.8](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem8 "Theorem 2.8. ‣ 2.4. Universal approximation with signatures of general rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths").
∎

###### Remark 4.6.

For example, in the case where X=WX=W is a (correlated) dd-dimensional Brownian motion with correlation matrix ρ\rho, the quadratic (co-)variation is [W]ti​j=ρi​j​t[W]^{ij}\_{t}=\rho\_{ij}t, t∈[0,T]t\in[0,T], i,j=1,…,di,j=1,\ldots,d. That is, the quadratic variation is a linear function in time, and coincides almost surely with the rough path bracket of the random Itô rough path. Consequently, see also Remark [2.10](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem10 "Remark 2.10. ‣ 2.4. Universal approximation with signatures of general rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths"), in Brownian settings it is sufficient to consider only the time-extended Brownian motion W^=(⋅,W)\widehat{W}=(\cdot,W) (i.e., without extending by quadratic variation), and a universal approximation result formulated analogously to Corollary [4.5](https://arxiv.org/html/2602.05898v1#S4.Thmtheorem5 "Corollary 4.5. ‣ 4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths") holds true.

It turns out that, if the semimartingale XX satisfies Property 0-(RIE), which is equivalent to Property (RIE), see Lemma [3.3](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem3 "Lemma 3.3 (Lemma 2.16 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths"), then the 0-signature and the Itô signature coincide almost surely. In particular, for almost every ω∈Ω\omega\in\Omega, the limits of left-point Riemann sums exist ω\omega-wise.

###### Lemma 4.7.

Let p∈(2,3)p\in(2,3) and let πn={τkn}\pi^{n}=\{\tau^{n}\_{k}\}, n∈ℕn\in\mathbb{N}, be a sequence of adapted partitions (so that each τkn\tau^{n}\_{k} is a stopping time), such that for almost every ω∈Ω\omega\in\Omega, (πn​(ω))n∈ℕ(\pi^{n}(\omega))\_{n\in\mathbb{N}} is a sequence of (finite) partitions of [0,T][0,T] with vanishing mesh size.

Let XX be a dd-dimensional continuous semimartingale, and suppose that for almost every ω∈Ω\omega\in\Omega, sup{|Xτkn​(ω),τk+1n​(ω)(ω)|:k=0,…,Nn−1}\sup\{|X\_{\tau^{n}\_{k}(\omega),\tau^{n}\_{k+1}(\omega)}(\omega)|\,:k=0,\dots,N\_{n}-1\} converges to 0 as n→∞n\to\infty, and that the sample path X​(ω)X(\omega) satisfies Property 0-(RIE) relative to pp and (πn​(ω))n∈ℕ(\pi^{n}(\omega))\_{n\in\mathbb{N}}.

1. (i)

   The random rough path pathwise defined via Proposition [3.1](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem1 "Proposition 3.1 (Proposition 2.9 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") for γ=0\gamma=0 and the Itô signature of XX truncated at level 22 coincide ℙ\mathbb{P}-almost surely.
2. (ii)

   The random 0-signature 𝕏0,π\mathbb{X}^{0,\pi} pathwise defined via Definition [3.8](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem8 "Definition 3.8. ‣ 3.2. The 𝜸-signature ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") and the Itô signature 𝕏\mathbb{X} of XX coincide ℙ\mathbb{P}-almost surely.

###### Proof.

*(i):* Since Property 0-(RIE) and Property (RIE) are equivalent, see also Lemma [3.3](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem3 "Lemma 3.3 (Lemma 2.16 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths"), this is the statement of part (i) of [[AKLP25a](https://arxiv.org/html/2602.05898v1#bib.bibx4), Lemma 3.1].

*(ii):* Since the 0-signature coincides with then Lyons’ lift of the rough path (1,X0,⋅,𝕏0,π,(2))(1,X\_{0,\cdot},\mathbb{X}^{0,\pi,(2)}), see Definition [3.8](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem8 "Definition 3.8. ‣ 3.2. The 𝜸-signature ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") and Appendix [C](https://arxiv.org/html/2602.05898v1#A3 "Appendix C On Lyons’ extension theorem ‣ Universal approximation with signatures of non-geometric rough paths"), and by (i) the random rough path pathwise defined via Proposition  [3.1](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem1 "Proposition 3.1 (Proposition 2.9 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") and the Itô signature of XX truncated at level 22 coincide ℙ\mathbb{P}-almost surely, we have by the uniqueness of Lyons’ lift, that the signatures coincide ℙ\mathbb{P}-almost surely.
∎

Moreover, if the semimartingale XX satisfies Property γ\gamma-(RIE), the pathwise quadratic variation and the stochastic quadratic variation coincide almost surely.

###### Lemma 4.8.

Let γ∈[0,1]\gamma\in[0,1], p∈(2,3)p\in(2,3) and let πn={τkn}\pi^{n}=\{\tau^{n}\_{k}\}, n∈ℕn\in\mathbb{N}, be a sequence of adapted partitions (so that each τkn\tau^{n}\_{k} is a stopping time), such that for almost every ω∈Ω\omega\in\Omega, (πn​(ω))n∈ℕ(\pi^{n}(\omega))\_{n\in\mathbb{N}} is a sequence of (finite) partitions of [0,T][0,T] with vanishing mesh size.

Let XX be a dd-dimensional continuous semimartingale, and suppose that for almost every ω∈Ω\omega\in\Omega, sup{|Xτkn​(ω),τk+1n​(ω)(ω)|:k=0,…,Nn−1}\sup\{|X\_{\tau^{n}\_{k}(\omega),\tau^{n}\_{k+1}(\omega)}(\omega)|\,:k=0,\dots,N\_{n}-1\} converges to 0 as n→∞n\to\infty, and that the sample path X​(ω)X(\omega) satisfies Property γ\gamma-(RIE) relative to γ\gamma, pp and (πn​(ω))n∈ℕ(\pi^{n}(\omega))\_{n\in\mathbb{N}}. We define the random variable

|  |  |  |
| --- | --- | --- |
|  | X^:=(⋅,X,(1−2​γ)​Q​(X)),\widehat{X}:=(\cdot,X,(1-2\gamma)Q(X)), |  |

with values in C​([0,T];ℝd^)C([0,T];\mathbb{R}^{\hat{d}}) for d^=1+d+d​(d+1)2\hat{d}=1+d+\frac{d(d+1)}{2}, where

|  |  |  |
| --- | --- | --- |
|  | Q​(X):=([X1,X1],…,[X1,Xd],[X2,X2],…,[X2,Xd],…,[Xd,Xd]),Q(X):=([X^{1},X^{1}],\ldots,[X^{1},X^{d}],[X^{2},X^{2}],\ldots,[X^{2},X^{d}],\ldots,[X^{d},X^{d}]), |  |

where [X]=([Xi,Xj])1≤i,j≤d[X]=([X^{i},X^{j}])\_{1\leq i,j\leq d} denotes the quadratic (co-)variation of XX. Then X^\widehat{X} and the random variable that is pathwise defined via ([3.3](https://arxiv.org/html/2602.05898v1#S3.E3 "In 3.2. The 𝜸-signature ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths")) coincide ℙ\mathbb{P}-almost surely.

###### Proof.

This clearly holds true for γ=12\gamma=\frac{1}{2}. Therefore suppose that γ≠12\gamma\neq\frac{1}{2}. By definition, the pathwise quadratic variation [Xi​(ω),Xj​(ω)]γ,π[X^{i}(\omega),X^{j}(\omega)]^{\gamma,\pi} is given by the limit as n→∞n\to\infty of:

|  |  |  |
| --- | --- | --- |
|  | (1−2​γ)​∑k=0Nn−1Xτkn​(ω)∧t,τk+1n​(ω)∧ti​(ω)​Xτkn​(ω)∧t,τk+1n​(ω)∧tj​(ω).(1-2\gamma)\sum\_{k=0}^{N\_{n}-1}X^{i}\_{\tau^{n}\_{k}(\omega)\wedge t,\tau^{n}\_{k+1}(\omega)\wedge t}(\omega)X^{j}\_{\tau^{n}\_{k}(\omega)\wedge t,\tau^{n}\_{k+1}(\omega)\wedge t}(\omega). |  |

We know that these sums converge uniformly (in t∈[0,T]t\in[0,T]) in probability to the quadratic variation (1−2​γ)​[Xi,Xj](1-2\gamma)[X^{i},X^{j}], see e.g. [[Pro05](https://arxiv.org/html/2602.05898v1#bib.bibx50), Chapter II, Theorem 22]. By taking a subsequence, if necessary, it follows the (almost sure) uniqueness of limits.
∎

As a consequence of Corollary [3.10](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem10 "Corollary 3.10. ‣ 3.3. A universal approximation theorem with 𝜸-signatures ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") (or Corollary [4.5](https://arxiv.org/html/2602.05898v1#S4.Thmtheorem5 "Corollary 4.5. ‣ 4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths")), Lemma [4.7](https://arxiv.org/html/2602.05898v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths") and Lemma [4.8](https://arxiv.org/html/2602.05898v1#S4.Thmtheorem8 "Lemma 4.8. ‣ 4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths"), we formulate universality of the Itô signature of a continuous semimartingale, whose sample paths almost surely satisfy Property 0-(RIE) or, equivalently, Property (RIE), that is, so that the Itô signature almost surely exists as collection of iterated integrals, where the integral exists as limit of pathwise left-point Riemann sums. This holds true for various semimartingales relative to suitable sequences of partitions. We refer to [[AKLP25a](https://arxiv.org/html/2602.05898v1#bib.bibx4), Section 3].

###### Corollary 4.9 (Universal approximation theorem for the Itô signature).

Let p∈(2,3)p\in(2,3) and let πn={τkn}\pi^{n}=\{\tau^{n}\_{k}\}, n∈ℕn\in\mathbb{N}, be a sequence of adapted partitions (so that each τkn\tau^{n}\_{k} is a stopping time), such that for almost every ω∈Ω\omega\in\Omega, (πn​(ω))n∈ℕ(\pi^{n}(\omega))\_{n\in\mathbb{N}} is a sequence of (finite) partitions of [0,T][0,T] with vanishing mesh size.

Let XX be a dd-dimensional continuous semimartingale, and suppose that for almost every ω∈Ω\omega\in\Omega, sup{|Xτkn​(ω),τk+1n​(ω)(ω)|:k=0,…,Nn−1}\sup\{|X\_{\tau^{n}\_{k}(\omega),\tau^{n}\_{k+1}(\omega)}(\omega)|\,:k=0,\dots,N\_{n}-1\} converges to 0 as n→∞n\to\infty, and that the sample path X​(ω)X(\omega) satisfies Property 0-(RIE) relative to pp and (πn​(ω))n∈ℕ(\pi^{n}(\omega))\_{n\in\mathbb{N}}.

Let X^:=(⋅,X,Q​(X))\widehat{X}:=(\cdot,X,Q(X)), where Q​(X)Q(X) is defined as in Corollary [4.5](https://arxiv.org/html/2602.05898v1#S4.Thmtheorem5 "Corollary 4.5. ‣ 4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths"), and 𝒮(2):={(X^,𝕏^(2))​(ω):ω∈Ω}\mathcal{S}^{(2)}:=\{(\widehat{X},\widehat{\mathbb{X}}^{(2)})(\omega):\omega\in\Omega\}, where 𝕏^s,t(2):=∫st(X^r−X^s)⊗dX^r\widehat{\mathbb{X}}^{(2)}\_{s,t}:=\int\_{s}^{t}(\widehat{X}\_{r}-\widehat{X}\_{s})\otimes\mathrm{d}\widehat{X}\_{r}, (s,t)∈ΔT(s,t)\in\Delta\_{T}. Further, let K⊂𝒞^p​-var​([0,T];ℝd^)K\subset\widehat{\mathcal{C}}^{p\textup{-var}}([0,T];\mathbb{R}^{\hat{d}}) be a compact subset of the subspace of rough paths extended by time and the bracket terms, bounded with respect to the rough path norm, and consider a continuous function f:K→ℝf\colon K\to\mathbb{R}. For some L>0L>0, let K0,π,L⊂KK\_{0,\pi,L}\subset K be the subset defined by

|  |  |  |
| --- | --- | --- |
|  | K0,π,L:={(X^,𝕏^0,π,(2))∈K:X​ satisfies Property 0-(RIE) relative to p and πsuch that ​‖(X^,𝕏^0,π,(2))‖p+‖[X^]0,π‖p2≤L}.\displaystyle K\_{0,\pi,L}:=\Biggl\{(\widehat{X},\widehat{\mathbb{X}}^{0,\pi,(2)})\in K\,:\,\begin{aligned} &X\text{ satisfies Property $0$-{(RIE)} relative to $p$ and $\pi$}\\ &\text{such that }\|(\widehat{X},\widehat{\mathbb{X}}^{0,\pi,(2)})\|\_{p}+\|[\widehat{X}]^{0,\pi}\|\_{\frac{p}{2}}\leq L\end{aligned}\Biggr\}. |  |

Then for every ε>0\varepsilon>0, there exists a linear functional ℓ∈T​(ℝd^)\ell\in T(\mathbb{R}^{\hat{d}}) such that for almost every ω∈Ω\omega\in\Omega,

|  |  |  |
| --- | --- | --- |
|  | |f​((X^,𝕏^(2))​(ω))−⟨ℓ,𝕏^T​(ω)⟩|<εfor all(X^,𝕏^(2))​(ω)∈K0,π,L∩𝒮(2),|f((\widehat{X},\widehat{\mathbb{X}}^{(2)})(\omega))-\langle\ell,\widehat{\mathbb{X}}\_{T}(\omega)\rangle|<\varepsilon\qquad\text{for all}\quad(\widehat{X},\widehat{\mathbb{X}}^{(2)})(\omega)\in K\_{0,\pi,L}\cap\mathcal{S}^{(2)}, |  |

where 𝕏^\widehat{\mathbb{X}} denotes the Itô signature of X^\widehat{X}.

###### Proof.

We use that for almost every ω∈Ω\omega\in\Omega, the random 0-signature of X^​(ω)\widehat{X}(\omega) and the Itô signature 𝕏^​(ω)\widehat{\mathbb{X}}(\omega) coincide, see Lemma [4.8](https://arxiv.org/html/2602.05898v1#S4.Thmtheorem8 "Lemma 4.8. ‣ 4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths") and part (ii) of Lemma [4.7](https://arxiv.org/html/2602.05898v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths"). The claim then immediately follows from the pathwise universal approximation theorem for linear functionals of the γ\gamma-signature, which is Corollary [3.10](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem10 "Corollary 3.10. ‣ 3.3. A universal approximation theorem with 𝜸-signatures ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths").

Alternatively, one could use Corollary [4.5](https://arxiv.org/html/2602.05898v1#S4.Thmtheorem5 "Corollary 4.5. ‣ 4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths") to prove the claim.
∎

###### Remark 4.10.

An analogous result also holds true when considering the Stratonovich signature of XX instead of the Itô signature of XX (also if almost all sample paths only satisfy Property 1/21/2-(RIE)). This can be shown using the results of the previous sections. This is, however, weaker than the classical universal approximation theorem stated in Corollary [4.3](https://arxiv.org/html/2602.05898v1#S4.Thmtheorem3 "Corollary 4.3. ‣ 4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths") since we impose an assumption on the sample paths of the semimartingale to allow for a statement about the Itô signature.

###### Remark 4.11.

Similar to Remark [4.6](https://arxiv.org/html/2602.05898v1#S4.Thmtheorem6 "Remark 4.6. ‣ 4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths"), for example, for a correlated dd-dimensional Brownian motion XX, the quadratic (co-)variation is actually a linear function in time. Consequently, it suffices to consider only the time-extended path (⋅,X)(\cdot,X), and a universal approximation result formulated analogously to Corollary [4.9](https://arxiv.org/html/2602.05898v1#S4.Thmtheorem9 "Corollary 4.9 (Universal approximation theorem for the Itô signature). ‣ 4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths") holds true.

With Remark [4.6](https://arxiv.org/html/2602.05898v1#S4.Thmtheorem6 "Remark 4.6. ‣ 4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths") (and Remark [4.11](https://arxiv.org/html/2602.05898v1#S4.Thmtheorem11 "Remark 4.11. ‣ 4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths")) in mind, when approximating continuous functionals using the Brownian signature, we expect the Itô signature and the Stratonovich signature of the time-extended Brownian motion to perform equally well because both do satisfy the universal approximation property.

## 5. Numerical examples

As seen in the previous section, the universal approximation property holds true for (linear functionals of) the Stratonovich signature of the time-extended path, whereas for the Itô signature we need to consider the path extended by time and its quadratic (co)-variation. This naturally leads to the question when it is beneficial in practice to extend the path additionally by its quadratic (co-)variation. Therefore, we conclude the study of Itô signatures with a numerical analysis that illustrates briefly the practical implications of using Itô signatures in the context of mathematical finance.333The code used to generate the results in this section is available at <https://github.com/mihribanceylan/Ito-signatures-Calibration-and-Pricing>.

We consider calibration to time-series data, payoff approximation, and pricing tasks for options that naturally depend on quadratic variation. In particular, we cover options on realized volatility, as well as covariance and correlation swaps and calls. Throughout these experiments, we find the following: When assuming that the underlying price dynamics are driven by Brownian motion whose quadratic variation is equal to time, here: Heston model, it turns out that—as one may expect—both the Itô and the Stratonovich signature achieve very small approximation errors in this setting, with only minor quantitative differences.

When assuming that the underlying price dynamics are time-changed or when considering payoffs that depend explicitly on realized variance, covariance, or correlation, Itô feature maps perform noticeably better – due to the quadratic variation extension – in the sense that we observe substantially lower test errors and more accurate prices.

In each experiment, we compare Stratonovich and Itô feature maps under a common protocol (same truncation level, regularization, and train/test split). For the Itô features, we extend the driving path by time and quadratic variation or, in Brownian settings, only by time as we classically do it for the Stratonovich features. These numerical experiments aim at demonstrating that the Itô signature results in better out-of-sample performance when the quadratic variation actually contains additional information of the path.

A classical problem in mathematical finance, that we do not address here, is the hedging of financial derivatives, for example the mean variance optimal hedging problem. Since the profit of a trading strategy is defined in terms of an Itô integral and the Itô integral can naturally be written as a linear functional of the Itô signature, it might be worth exploring at some point the performance of Itô signatures for the hedging problem, or more precisely, for a linearized version of that problem which has already been studied in [[LNPA20](https://arxiv.org/html/2602.05898v1#bib.bibx46)] in the context of signatures.

### 5.1. Calibration of signature models

We first consider the calibration of a signature model to simulated time-series data and take a similar approach as in [[CGSF23](https://arxiv.org/html/2602.05898v1#bib.bibx21)]. We fix a time horizon T>0T>0, and let X=(X1,…,Xd)X=(X^{1},\dots,X^{d}) be a dd-dimensional continuous local martingale. We then consider the extended process X^\widehat{X} with values in ℝd^\mathbb{R}^{\hat{d}}, where d^\hat{d} denotes the dimension of the extended path. We fix a truncation level N≥1N\geq 1 and denote by 𝕏^tN\widehat{\mathbb{X}}^{N}\_{t} the truncated signature of X^\widehat{X} at time tt at level NN. The model we want to calibrate is a signature model, see e.g. [[CGSF23](https://arxiv.org/html/2602.05898v1#bib.bibx21)], of the form

|  |  |  |
| --- | --- | --- |
|  | S​(ℓ)t=S0+∑0<|I|≤NℓI​⟨eI,𝕏^t⟩,ℓI∈ℝ,S(\ell)\_{t}=S\_{0}+\sum\_{0<|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle,\quad\ell\_{I}\in\mathbb{R}, |  |

where we set ℓ∅:=S0\ell\_{\emptyset}:=S\_{0}. We fix a time grid 0=t0<t1<…<tn=T0=t\_{0}<t\_{1}<\ldots<t\_{n}=T, and observe a price path (Sti)i=1n(S\_{t\_{i}})\_{i=1}^{n} on this grid, where n≥1n\geq 1 denotes the number of time steps between 0 and TT. The calibration problem consists of finding ℓ∗∈ℝd∗\ell^{\ast}\in\mathbb{R}^{d^{\ast}} such that the loss function

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lα​(ℓ)\displaystyle L\_{\alpha}(\ell) | :=∑i=1n(S​(ℓ)ti−Sti)2+α​‖ℓ‖1\displaystyle:=\sum\_{i=1}^{n}\big(S(\ell)\_{t\_{i}}-S\_{t\_{i}}\big)^{2}+\alpha\|\ell\|\_{1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1n(S0+∑0<|I|≤NℓI​⟨eI,𝕏^ti⟩−Sti)2+α​‖ℓ‖1,\displaystyle=\sum\_{i=1}^{n}\bigg(S\_{0}+\sum\_{0<|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{X}}\_{t\_{i}}\rangle-S\_{t\_{i}}\bigg)^{2}+\alpha\|\ell\|\_{1}, |  |

is minimized, where d∗:=d^N+1−1dd^{\ast}:=\frac{\hat{d}^{N+1}-1}{d} is the dimension of the signature truncated at level NN and α​‖ℓ‖1\alpha\|\ell\|\_{1} denotes a fixed L1L^{1} penalization, so we perform a Lasso regression.

We train on one trajectory on the time interval [0,T][0,T] with T=1T=1, n=2000n=2000, and test on 10001000 different realizations on [0,0.5][0,0.5]. To assess the accuracy, we report mean squared errors (MSEs) between the predicted and observed trajectories, i.e.,

|  |  |  |
| --- | --- | --- |
|  | 1n​∑i=1n(S​(ℓ∗)ti−Sti)2,\frac{1}{n}\sum\_{i=1}^{n}(S(\ell^{\ast})\_{t\_{i}}-S\_{t\_{i}})^{2}, |  |

on both the training trajectory (in-sample MSE) and the test trajectories (out-of-sample MSE), where the latter is computed as an average of the MSEs on the 10001000 test paths. For the computation of the signature we use available packages, e.g. the package `iisignature` developed by [[RG20](https://arxiv.org/html/2602.05898v1#bib.bibx51)], or `esig`444https://pypi.org/project/esig/. Throughout, both feature maps use the same penalty α=10−5\alpha=10^{-5}, and the same train and test paths.

###### Example 5.1 (Heston model).

We generate time series (via an Euler scheme) from the Heston stochastic volatility model under the physical measure ℙ\mathbb{P}

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St\displaystyle\,\mathrm{d}S\_{t} | =μ​St​d​t+St​Vt​d​Wt,\displaystyle=\mu S\_{t}\,\mathrm{d}t+S\_{t}\sqrt{V\_{t}}\,\mathrm{d}W\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vt\displaystyle\,\mathrm{d}V\_{t} | =κ​(θ−Vt)​d​t+σ​Vt​d​Bt,\displaystyle=\kappa(\theta-V\_{t})\,\mathrm{d}t+\sigma\sqrt{V\_{t}}\,\mathrm{d}B\_{t}, |  |

with [B,W]t=ρ​t[B,W]\_{t}=\rho t, ρ∈[−1,1],\rho\in[-1,1], see [[Hes93](https://arxiv.org/html/2602.05898v1#bib.bibx37)]. We set the model parameters to be

|  |  |  |
| --- | --- | --- |
|  | {S0,V0,μ,κ,θ,σ,ρ}:={1,0.08,0.001,0.5,0.15,0.25,−0.5}.\{S\_{0},V\_{0},\mu,\kappa,\theta,\sigma,\rho\}:=\{1,0.08,0.001,0.5,0.15,0.25,-0.5\}. |  |

We work under an equivalent local martingale measure ℚ\mathbb{Q}, and specify the processes WℚW^{\mathbb{Q}} and BℚB^{\mathbb{Q}} by

|  |  |  |
| --- | --- | --- |
|  | d​Wtℚ=d​StSt​Vt,d​Btℚ=d​Vtσ​Vt.\,\mathrm{d}W^{\mathbb{Q}}\_{t}=\frac{\,\mathrm{d}S\_{t}}{S\_{t}\sqrt{V\_{t}}},\qquad\,\mathrm{d}B\_{t}^{\mathbb{Q}}=\frac{\,\mathrm{d}V\_{t}}{\sigma\sqrt{V\_{t}}}. |  |

Then, WℚW^{\mathbb{Q}} and BℚB^{\mathbb{Q}} are Brownian motions with respect to ℚ\mathbb{Q} with correlation ρ\rho, and the dynamics of (S,V)(S,V) can be written as d​St=St​Vt​d​Wtℚ\,\mathrm{d}S\_{t}=S\_{t}\sqrt{V\_{t}}\,\mathrm{d}W\_{t}^{\mathbb{Q}} and d​Vt=σ​Vt​d​Btℚ\,\mathrm{d}V\_{t}=\sigma\sqrt{V\_{t}}\,\mathrm{d}B^{\mathbb{Q}}\_{t}. We now aim to approximate these dynamics with signature models with (Wℚ,Bℚ)(W^{\mathbb{Q}},B^{\mathbb{Q}}) being the underlying process. To this end, we consider two signature models: one based on Stratonovich signatures, the other based on Itô signatures of the time extended path X^=(⋅,Wℚ,Bℚ)\widehat{X}=(\cdot,W^{\mathbb{Q}},B^{\mathbb{Q}}). More precisely, we calibrate the following signature models:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SStrat​(ℓ)t\displaystyle S^{\text{Strat}}(\ell)\_{t} | =S0+∑|I|≤NℓI​⟨e~I,𝕏^tStrat⟩=S0+∫0t∑|I|≤NℓI​⟨eI,𝕏^rStrat⟩​d​Wrℚ,\displaystyle=S\_{0}+\sum\_{|I|\leq N}\ell\_{I}\langle\tilde{e}\_{I},\widehat{\mathbb{X}}\_{t}^{\text{Strat}}\rangle=S\_{0}+\int\_{0}^{t}\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{X}}^{\text{Strat}}\_{r}\rangle\,\mathrm{d}W^{\mathbb{Q}}\_{r}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | SItô​(ℓ)t\displaystyle S^{\text{It\^{o}}}(\ell)\_{t} | =S0+∑|I|≤NℓI​⟨eI⊗e1,𝕏^tItô⟩=S0+∫0t∑|I|≤NℓI​⟨eI,𝕏^rItô⟩​d​Wrℚ,\displaystyle=S\_{0}+\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I}\otimes e\_{1},\widehat{\mathbb{X}}\_{t}^{\text{It\^{o}}}\rangle=S\_{0}+\int\_{0}^{t}\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{X}}^{\text{It\^{o}}}\_{r}\rangle\,\mathrm{d}W^{\mathbb{Q}}\_{r}, |  |

where e~I=eI⊗e1−12​ρi|I|​1​eI′⊗e0\tilde{e}\_{I}=e\_{I}\otimes e\_{1}-\frac{1}{2}\rho\_{i\_{|I|}1}e\_{I^{\prime}}\otimes e\_{0}, ρi|I|​1\rho\_{i\_{|I|}1} is the correlation between X^i|I|\widehat{X}^{i\_{|I|}} and the Brownian motion WℚW^{\mathbb{Q}}. Here, we choose N=2N=2 and S0=1S\_{0}=1 and obtain the following results:

![Refer to caption](train_heston.png)


(a) In-sample.

![Refer to caption](heston_test.png)


(b) Out-of-sample.

Figure 1. Regression on the price of the Heston model as defined above.

Figure [1](https://arxiv.org/html/2602.05898v1#S5.F1 "Figure 1 ‣ Example 5.1 (Heston model). ‣ 5.1. Calibration of signature models ‣ 5. Numerical examples ‣ Universal approximation with signatures of non-geometric rough paths") illustrates that the Heston model can be approximated very closely by signature models using the Stratonovich and the Itô signature. We observe an in-sample MSE of order 10−810^{-8} and 10−710^{-7} and out-of-sample MSE of order 10−510^{-5} and 10−510^{-5} for the Stratonovich signature and Itô signature, respectively.

As stated in Remark [4.6](https://arxiv.org/html/2602.05898v1#S4.Thmtheorem6 "Remark 4.6. ‣ 4. Application to continuous semimartingales ‣ Universal approximation with signatures of non-geometric rough paths"), when the model is driven by Brownian motion, that is, when one considers the Brownian signature, it is sufficient to extend the path by time, and both Itô and Stratonovich features achieve comparably small errors (with a slightly better performance for the Stratonovich signature model in our experiments).

###### Example 5.2 (Singular time-changed SDE).

As a toy example, to mimic volatility dynamics with singular time changes—that appear for instance in hyper-rough Heston-type models with non-absolutely continuous quadratic variation, see e.g. [[JDC24](https://arxiv.org/html/2602.05898v1#bib.bibx40)]—we consider a one-dimensional SDE driven by a Brownian motion time-changed by a Cantor clock, see [[ASJ18](https://arxiv.org/html/2602.05898v1#bib.bibx8), Example 1 and Section 6] and the general framework for SDEs driven by time-changed semimartingales in [[Kob11](https://arxiv.org/html/2602.05898v1#bib.bibx42)]:

|  |  |  |
| --- | --- | --- |
|  | d​St=σ​(St)​d​WC​(t),\,\mathrm{d}S\_{t}=\sigma(S\_{t})\,\mathrm{d}W\_{C(t)}, |  |

where C:[0,1]→[0,1]C\colon[0,1]\to[0,1] is the Cantor function. In our experiment, we choose σ​(x)=1+0.3​tanh⁡(x)\sigma(x)=1+0.3\tanh(x). On the time grid, we simulate C​(t)C(t), generate WC​(t)W\_{C(t)} with increments Δ​WC∼𝒩​(0,Δ​C),\Delta W\_{C}\sim\mathcal{N}(0,\Delta C), and use an Euler scheme to simulate SS. For the Stratonovich signature we take the time-extended path X^t=(t,WC​(t))∈ℝ2\widehat{X}\_{t}=(t,W\_{C(t)})\in\mathbb{R}^{2}, t∈[0,1]t\in[0,1]; for the Itô signature we additionally include the quadratic variation (QV) and take X^t=(t,WC​(t),C​(t))∈ℝ3\widehat{X}\_{t}=(t,W\_{C(t)},C(t))\in\mathbb{R}^{3}, t∈[0,1]t\in[0,1]. We consider the following signature models:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SStrat​(ℓ)t\displaystyle S^{\text{Strat}}(\ell)\_{t} | =S0+∑|I|≤NℓI​⟨eI,𝕏^tStrat⟩,\displaystyle=S\_{0}+\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{X}}^{\text{Strat}}\_{t}\rangle, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | SItô​(ℓ)t\displaystyle S^{\text{It\^{o}}}(\ell)\_{t} | =S0+∑|I|≤N−1ℓI​⟨eI⊗e1,𝕏^tItô⟩=S0+∫0t∑|I|≤N−1ℓI​⟨eI,𝕏^rItô⟩​d​WC​(r),\displaystyle=S\_{0}+\sum\_{|I|\leq N-1}\ell\_{I}\langle e\_{I}\otimes e\_{1},\widehat{\mathbb{X}}^{\text{It\^{o}}}\_{t}\rangle=S\_{0}+\int\_{0}^{t}\sum\_{|I|\leq N-1}\ell\_{I}\langle e\_{I},\widehat{\mathbb{X}}^{\text{It\^{o}}}\_{r}\rangle\,\mathrm{d}W\_{C(r)}, |  |

where e1e\_{1} corresponds to the component WCW\_{C} of X^\widehat{X}, 𝕏^Strat\widehat{\mathbb{X}}^{\text{Strat}} denotes the Stratonovich signature of X^=(⋅,WC)\widehat{X}=(\cdot,W\_{C}) and 𝕏^Itô\widehat{\mathbb{X}}^{\text{It\^{o}}} denotes the Itô signature of X^=(⋅,WC,C)\widehat{X}=(\cdot,W\_{C},C). We observe that the signature model using the Stratonovich signature cannot be expressed in terms of an Itô-SDE, as was the case in Example [5.1](https://arxiv.org/html/2602.05898v1#S5.Thmtheorem1 "Example 5.1 (Heston model). ‣ 5.1. Calibration of signature models ‣ 5. Numerical examples ‣ Universal approximation with signatures of non-geometric rough paths"). This is due to the fact that the Cantor time-change is not absolutely continuous with respect to time. However, using the Itô signature, the corresponding signature model can be written as an Itô SDE driven by the time-changed Brownian motion, which suggests that the Itô signature is the more natural choice when considering such singular time changes.

For our numerical experiment we choose N=2N=2 and S0=0S\_{0}=0 and obtain the following results:

![Refer to caption](train_cantor.png)


(a) In-sample.

![Refer to caption](test_cantor_2.png)


(b) Out-of-sample.

Figure 2. Regression on the price of a singular time-changed SDE as defined above.

Figure [2](https://arxiv.org/html/2602.05898v1#S5.F2 "Figure 2 ‣ Example 5.2 (Singular time-changed SDE). ‣ 5.1. Calibration of signature models ‣ 5. Numerical examples ‣ Universal approximation with signatures of non-geometric rough paths") illustrates that the signature model using the Itô signature approximates the model more closely than the one using the Stratonovich signature out-of-sample: Both are able to follow the stepped pattern but one can observe that the Itô model results in a path that is more closely aligned with the target path.

The in-sample MSE is of order 10−610^{-6} and 10−510^{-5} and the out-of-sample MSE is of order 10−410^{-4} and 10−210^{-2} when using the Itô signature and the Stratonovich signature, respectively. These findings are consistent with the idea that extending the path by the quadratic variation [WC]t=C​(t)[W\_{C}]\_{t}=C(t), as we do it for the Itô signature, here actually is advantageous because it contains additional information about the variation of the path that is missing in the Stratonovich signature. This now suggests (and this was the reason we considered this model), and might be worth exploring in future work, that when considering price dynamics that exhibit jumps, signature models based on Itô signatures may also perform better compared to models based on Stratonovich signatures, again because the quadratic variation would contain additional information about the variation of the path (including jumps).

### 5.2. Payoff approximation and pricing

In this subsection we study signature-based approximation and pricing for payoffs that depend explicitly on quadratic (co-)variation, such as options on realized volatility and correlation or covariance swaps and calls.

In this setting, since the quadratic variation appears naturally here, we expect the Itô signature to perform particularly well.

This motivated us to compare two set-ups: for single-asset payoffs we consider the Stratonovich signature of the time-extended path (t,log⁡Sti)(t,\log S\_{t}^{i}) and the Itô signature of the path extended by time and quadratic variation (t,log⁡Sti,[log⁡Si]t)(t,\log S\_{t}^{i},[\log S^{i}]\_{t}), i=1,2i=1,2. For correlation and covariance payoffs we analogously consider the Stratonovich signature of (t,log⁡St1,log⁡St2)(t,\log S\_{t}^{1},\log S\_{t}^{2}) and the Itô signature of the path extended by time and quadratic (co-)variation (t,log⁡St1,log⁡St2,[log⁡S1]t,[log⁡S1,log⁡S2]t,[log⁡S2]t)(t,\log S\_{t}^{1},\log S\_{t}^{2},[\log S^{1}]\_{t},[\log S^{1},\log S^{2}]\_{t},[\log S^{2}]\_{t}).

The payoffs are defined via log-price increments on an equidistant grid 0=t0<t1<…<tn=T0=t\_{0}<t\_{1}<\ldots<t\_{n}=T, where we set T=1T=1 and n=252n=252, thinking of approximately 252252 trading days in one year. We write Xti=log⁡StiX\_{t}^{i}=\log S\_{t}^{i}, and set Δ​Xki=Xtk+1i−Xtki\Delta X\_{k}^{i}=X^{i}\_{t\_{k+1}}-X^{i}\_{t\_{k}}, k=0,…,n−1k=0,\ldots,n-1. The realized variance and realized volatility for asset ii are then defined by

|  |  |  |
| --- | --- | --- |
|  | RVarTi:=∑k=0n−1(Δ​Xki)2,RVTi:=∑k=0n−1(Δ​Xki)2,i=1,2,\mathrm{RVar}^{i}\_{T}:=\sum\_{k=0}^{n-1}(\Delta X\_{k}^{i})^{2},\qquad\mathrm{RV}^{i}\_{T}:=\sqrt{\sum\_{k=0}^{n-1}(\Delta X\_{k}^{i})^{2}},\qquad i=1,2, |  |

and we consider the payoffs

|  |  |  |
| --- | --- | --- |
|  | RVswapi=RVarTi−KRVari,RVcalli=(RVTi−KRVi)+,i=1,2,\mathrm{RVswap}^{i}=\mathrm{RVar}\_{T}^{i}-\mathrm{K}^{i}\_{\mathrm{RVar}},\qquad\mathrm{RVcall}^{i}=(\mathrm{RV}\_{T}^{i}-\mathrm{K}^{i}\_{\mathrm{RV}})^{+},\qquad i=1,2, |  |

where the strikes KRVari\mathrm{K}^{i}\_{\mathrm{RVar}} and KRVi\mathrm{K}^{i}\_{\mathrm{RV}} are determined from the training sample. For the two-asset payoffs, we use

|  |  |  |
| --- | --- | --- |
|  | CovT=∑k=0n−1Δ​Xk1​Δ​Xk2,CorrT=∑k=0n−1Δ​Xk1​Δ​Xk2∑k=0n−1(Δ​Xk1)2​∑k=0n−1(Δ​Xk2)2,\mathrm{Cov}\_{T}=\sum\_{k=0}^{n-1}\Delta X\_{k}^{1}\Delta X\_{k}^{2},\qquad\mathrm{Corr}\_{T}=\frac{\sum\_{k=0}^{n-1}\Delta X\_{k}^{1}\Delta X\_{k}^{2}}{\sqrt{\sum\_{k=0}^{n-1}(\Delta X\_{k}^{1})^{2}}\sqrt{\sum\_{k=0}^{n-1}(\Delta X\_{k}^{2})^{2}}}, |  |

and consider the payoffs

|  |  |  |  |
| --- | --- | --- | --- |
|  | CovSwap\displaystyle\mathrm{CovSwap} | =CovT−KCov,CovCall=(CovT−KCov)+,\displaystyle=\mathrm{Cov}\_{T}-\mathrm{K\_{Cov}},\quad\mathrm{CovCall}=(\mathrm{Cov}\_{T}-\mathrm{K\_{Cov}})^{+}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | CorrSwap\displaystyle\mathrm{CorrSwap} | =CorrT−KCorr,CorrCall=(CorrT−KCorr)+,\displaystyle=\mathrm{Corr}\_{T}-\mathrm{K\_{Corr}},\quad\mathrm{CorrCall}=(\mathrm{Corr}\_{T}-\mathrm{K\_{Corr}})^{+}, |  |

where again the strikes KCov\mathrm{K\_{Cov}} and KCorr\mathrm{K\_{Corr}} are determined from the training sample.

Let X^\widehat{X} denote the driving path used for signature features (time-extended for Stratonovich; extended by time and quadratic (co-)variation for Itô), and let 𝕏^N\widehat{\mathbb{X}}^{N} be its signature truncated at level N=2N=2. For a training set of size Ntrain=15000N\_{\mathrm{train}}=15000 consisting of i.i.d. paths {X^i}i=1Ntrain\{\widehat{X}^{i}\}\_{i=1}^{N\_{\mathrm{train}}} with corresponding payoffs F​(Xi)F(X^{i}), we fit (separately for each feature map) a linear model on signature features via ridge regression:

|  |  |  |
| --- | --- | --- |
|  | ℓ∗∈arg⁡minℓ∈ℝd∗⁡Lα​(ℓ),Lα​(ℓ):=1Ntrain​∑i=1Ntrain(F​(X(i))−⟨ℓ,𝕏^N,i⟩)2+α​‖ℓ‖22,\ell^{\ast}\;\in\;\arg\min\_{\ell\in\mathbb{R}^{d^{\ast}}}\;L\_{\alpha}(\ell),\qquad L\_{\alpha}(\ell):=\frac{1}{N\_{\mathrm{train}}}\sum\_{i=1}^{N\_{\mathrm{train}}}\Big(F(X^{(i)})-\langle\ell,\widehat{\mathbb{X}}^{N,i}\rangle\Big)^{2}\;+\;\alpha\|\ell\|\_{2}^{2}, |  |

with α=10−6\alpha=10^{-6} and 𝕏^N,i\widehat{\mathbb{X}}^{N,i} denoting the truncated signature of the ii-th path. We then evaluate the model on an independent test set of size Ntest=5000N\_{\text{test}}=5000, consisting of i.i.d. paths {X^i}i=1Ntest\{\widehat{X}^{i}\}\_{i=1}^{N\_{\text{test}}} and report the resulting out-of-sample MSEs. Pricing is then performed on an independent sample, generated by Monte Carlo simulation {X^MCj}j=1NMC\{\widehat{X}^{j}\_{\mathrm{MC}}\}\_{j=1}^{N\_{\mathrm{MC}}} of size NMC=25000N\_{\mathrm{MC}}=25000, via

|  |  |  |
| --- | --- | --- |
|  | P^=1NMC​∑j=1NMC⟨ℓ∗,𝕏^MCN,j⟩,\widehat{P}=\frac{1}{N\_{\mathrm{MC}}}\sum\_{j=1}^{N\_{\mathrm{MC}}}\langle\ell^{\ast},\widehat{\mathbb{X}}^{N,j}\_{\mathrm{MC}}\rangle, |  |

and we compare P^\widehat{P} to the Monte Carlo price 1NMC​∑j=1NMCF​(XMCj)\frac{1}{N\_{\mathrm{MC}}}\sum\_{j=1}^{N\_{\mathrm{MC}}}F(X^{j}\_{\mathrm{MC}}), which we take as a benchmark, and also include its 95%95\% confidence interval.

###### Example 5.3.

We consider a two-asset Heston model given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sti\displaystyle\,\mathrm{d}S\_{t}^{i} | =μi​Sti​d​t+Sti​Vti​d​Bti,\displaystyle=\mu^{i}S\_{t}^{i}\,\mathrm{d}t+S\_{t}^{i}\sqrt{V\_{t}^{i}}\,\mathrm{d}B\_{t}^{i}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vti\displaystyle\,\mathrm{d}V\_{t}^{i} | =κi​(θi−Vti)​d​t+σi​Vti​d​Wti,i=1,2,\displaystyle=\kappa^{i}(\theta^{i}-V\_{t}^{i})\,\mathrm{d}t+\sigma^{i}\sqrt{V\_{t}^{i}}\,\mathrm{d}W\_{t}^{i},\quad i=1,2, |  |

with [B1,B2]t=0.3​t[B^{1},B^{2}]\_{t}=0.3t, [W1,W2]t=0.5​t[W^{1},W^{2}]\_{t}=0.5t, [B1,W1]t=−0.6​t[B^{1},W^{1}]\_{t}=-0.6t and [B2,W2]t=−0.5​t[B^{2},W^{2}]\_{t}=-0.5t. Moreover, we set

|  |  |  |
| --- | --- | --- |
|  | {S01,S02,V01,V02,μ1,μ2,κ1,κ2,θ1,θ2,σ1,σ2}\displaystyle\{S\_{0}^{1},S\_{0}^{2},V\_{0}^{1},V\_{0}^{2},\mu^{1},\mu^{2},\kappa^{1},\kappa^{2},\theta^{1},\theta^{2},\sigma^{1},\sigma^{2}\} |  |
|  |  |  |
| --- | --- | --- |
|  | ={100,80,0.04,0.09,0.0,0.0,2.0,1.8,0.04,0.09,0.5,0.6}.\displaystyle=\{100,80,0.04,0.09,0.0,0.0,2.0,1.8,0.04,0.09,0.5,0.6\}. |  |

![Refer to caption](prices_vs_true_lines_heston.png)


(a) Prices from signature-regressed payoffs and MC price.

![Refer to caption](mse_boxplots_per_payoff_heston_new.png)


(b) Boxplots of out-of-sample MSEs.

Figure 3. Signature-based payoff regression and pricing under the two-asset Heston model as defined above.

Figure [3(b)](https://arxiv.org/html/2602.05898v1#S5.F3.sf2 "In Figure 3 ‣ Example 5.3. ‣ 5.2. Payoff approximation and pricing ‣ 5. Numerical examples ‣ Universal approximation with signatures of non-geometric rough paths") shows that, for any payoff, using the Itô signature results in smaller out-of-sample MSEs than using the Stratonovich signature. The boxplots also indicate both a smaller bias and a smaller out-of-sample variance. The prices, see Figure [3(a)](https://arxiv.org/html/2602.05898v1#S5.F3.sf1 "In Figure 3 ‣ Example 5.3. ‣ 5.2. Payoff approximation and pricing ‣ 5. Numerical examples ‣ Universal approximation with signatures of non-geometric rough paths"), estimated via the Itô signature, essentially coincide with the Monte Carlo price, and lie within the 95%95\% confidence interval. The prices, estimated via the Stratonovich signature, are systematically biased—especially for the two-asset payoffs (CovSwap/CovCall and CorrSwap/CorrCall), where some prices also lie outside the confidence interval. This underlines the advantage of extending the path by quadratic variation, as we do it for the Itô features, because this allows to directly access [log⁡S1][\log S^{1}], [log⁡S2][\log S^{2}], [log⁡S1,log⁡S2][\log S^{1},\log S^{2}] in the regression, which are exactly the statistics the payoffs we consider depend on. Using the Stratonovich signature of the time-extended path, this is not the case and the information has to be inferred from the iterated integrals of order up to 22.

###### Example 5.4.

We consider a two-asset singular time-changed SDE (with time-change given by the Cantor clock),

|  |  |  |
| --- | --- | --- |
|  | d​Sti=σ​(Sti)​d​WC​(t)i,i=1,2,\,\mathrm{d}S\_{t}^{i}=\sigma(S\_{t}^{i})\,\mathrm{d}W\_{C(t)}^{i},\quad i=1,2, |  |

with [WC1,WC2]t=ρ​C​(t)[W\_{C}^{1},W\_{C}^{2}]\_{t}=\rho\,C(t), ρ=0.6\rho=0.6, σ​(Sti)=νi​Sti\sigma(S\_{t}^{i})=\nu\_{i}S\_{t}^{i}, νi∈ℝ\nu\_{i}\in\mathbb{R}. In our experiments, we set

|  |  |  |
| --- | --- | --- |
|  | S01=100,S02=80,ν1=0.20,ν2=0.30.S^{1}\_{0}=100,\qquad S^{2}\_{0}=80,\qquad\nu\_{1}=0.20,\qquad\nu\_{2}=0.30. |  |

![Refer to caption](prices_vs_true_lines_Cantor.png)


(a) Prices from signature-regressed payoffs and MC price.

![Refer to caption](mse_boxplots_per_payoff_cantor.png)


(b) Boxplots of out-of-sample MSEs.

Figure 4. Signature-based payoff regression and pricing under the two-asset singular-time changed SDE described above.

In this model, the differences between using Itô signatures and Stratonovich signatures become even more clear. When using the Itô signature, the out-of-sample MSEs are minimal, and the prices lie within the 95%95\% MC confidence interval, for any payoff considered. When using the Stratonovich signature, however, the out-of-sample MSEs are significantly larger, see Figure [4(b)](https://arxiv.org/html/2602.05898v1#S5.F4.sf2 "In Figure 4 ‣ Example 5.4. ‣ 5.2. Payoff approximation and pricing ‣ 5. Numerical examples ‣ Universal approximation with signatures of non-geometric rough paths"), and the prices do not lie within the confidence interval for any payoff considered, see Figure [4(a)](https://arxiv.org/html/2602.05898v1#S5.F4.sf1 "In Figure 4 ‣ Example 5.4. ‣ 5.2. Payoff approximation and pricing ‣ 5. Numerical examples ‣ Universal approximation with signatures of non-geometric rough paths").

## Appendix A Proof of Theorem [2.11](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem11 "Theorem 2.11. ‣ 2.5. Discussion on approximation with weakly geometric rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths")

In this appendix, for completeness, we present the proof of the universal approximation theorem using time-extended weakly geometric rough paths (Theorem [2.11](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem11 "Theorem 2.11. ‣ 2.5. Discussion on approximation with weakly geometric rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths")).

###### Proof of Theorem [2.11](https://arxiv.org/html/2602.05898v1#S2.Thmtheorem11 "Theorem 2.11. ‣ 2.5. Discussion on approximation with weakly geometric rough paths ‣ 2. The signature of rough paths ‣ Universal approximation with signatures of non-geometric rough paths").

The result follows by an application of the Stone–Weierstrass theorem to the set

|  |  |  |
| --- | --- | --- |
|  | 𝒜:=span⁡{K∋𝕏^o,2↦⟨eI,𝕏^To⟩∈ℝ:I∈{0,…,d}N,N∈ℕ0}.\mathcal{A}:=\operatorname{span}\{K\ni\widehat{\mathbb{X}}^{o,2}\mapsto\langle e\_{I},\widehat{\mathbb{X}}^{o}\_{T}\rangle\in\mathbb{R}:I\in\{0,\ldots,d\}^{N},N\in\mathbb{N}\_{0}\}. |  |

Therefore, we have to show that 𝒜\mathcal{A}

1. (i)

   is a vector subspace of C​(K;ℝ)C(K;\mathbb{R}),
2. (ii)

   is a subalgebra and contains a non-zero constant function, and
3. (iii)

   separates points.

*(i):* By [[FV10](https://arxiv.org/html/2602.05898v1#bib.bibx32), Corollary 9.11], the map 𝕏^o,2↦⟨eI,𝕏^To⟩\widehat{\mathbb{X}}^{o,2}\mapsto\langle e\_{I},\widehat{\mathbb{X}}^{o}\_{T}\rangle is continuous on bounded sets for every multi-index II with respect to dp​-var:=∥⋅;⋅∥pd\_{p\textup{-var}}:=\|\cdot\,;\cdot\|\_{p}. More precisely, the map

|  |  |  |
| --- | --- | --- |
|  | (K,dp​-var)∋𝕏^o,2↦𝕏^o,N∈(Cop​-var​([0,T];GN​(ℝ1+d)),dp​-var),(K,d\_{p\textup{-var}})\ni\widehat{\mathbb{X}}^{o,2}\mapsto\widehat{\mathbb{X}}^{o,N}\in(C\_{o}^{p\textup{-var}}([0,T];G^{N}(\mathbb{R}^{1+d})),d\_{p\textup{-var}}), |  |

is continuous on KK with respect to dp​-vard\_{p\textup{-var}}, for every N≥3N\geq 3. Moreover, the evaluation map

|  |  |  |
| --- | --- | --- |
|  | (Cop​-var​([0,T];GN​(ℝ1+d)),dp​-var)∋𝕏^o,N↦𝕏^To,N∈(GN​(ℝ1+d),ρ)(C\_{o}^{p\textup{-var}}([0,T];G^{N}(\mathbb{R}^{1+d})),d\_{p\textup{-var}})\ni\widehat{\mathbb{X}}^{o,N}\mapsto\widehat{\mathbb{X}}^{o,N}\_{T}\in(G^{N}(\mathbb{R}^{1+d}),\rho) |  |

is continuous, where ρ\rho denotes the metric induced by the norm on T1N​(ℝ1+d)T\_{1}^{N}(\mathbb{R}^{1+d}). Here, we used that we can equip GN​(ℝ1+d)G^{N}(\mathbb{R}^{1+d}) with the metric ρ\rho, see e.g. [[FV10](https://arxiv.org/html/2602.05898v1#bib.bibx32), Remark 7.31]. This yields that the map

|  |  |  |
| --- | --- | --- |
|  | (K,dp​-var)∋𝕏^o,2↦𝕏^To,N∈(GN​(ℝ1+d),ρ)(K,d\_{p\textup{-var}})\ni\widehat{\mathbb{X}}^{o,2}\mapsto\widehat{\mathbb{X}}^{o,N}\_{T}\in(G^{N}(\mathbb{R}^{1+d}),\rho) |  |

is continuous. Since 𝕏^To,N↦⟨eI,𝕏^To⟩\widehat{\mathbb{X}}^{o,N}\_{T}\mapsto\langle e\_{I},\widehat{\mathbb{X}}^{o}\_{T}\rangle is continuous for any multi-index II, we can thus conclude that the map

|  |  |  |
| --- | --- | --- |
|  | (K,dp​-var)∋𝕏^o,2↦⟨eI,𝕏^To⟩∈ℝ(K,d\_{p\textup{-var}})\ni\widehat{\mathbb{X}}^{o,2}\mapsto\langle e\_{I},\widehat{\mathbb{X}}\_{T}^{o}\rangle\in\mathbb{R} |  |

is continuous with respect to dp​-vard\_{p\textup{-var}}.

*(ii):* Since 𝕏^To\widehat{\mathbb{X}}^{o}\_{T} is a group-like element, i.e., 𝕏^To∈G​((ℝ1+d))\widehat{\mathbb{X}}^{o}\_{T}\in G((\mathbb{R}^{1+d})), the shuffle property holds, and thus 𝒜\mathcal{A} is a subalgebra. Moreover, since ⟨e∅,𝕏^To⟩=1\langle e\_{\emptyset},\widehat{\mathbb{X}}^{o}\_{T}\rangle=1, it contains a non-zero constant function.

*(iii):* For the point separation, let us consider 𝕏^o,2\widehat{\mathbb{X}}^{o,2}, 𝕐^o,2∈K\widehat{\mathbb{Y}}^{o,2}\in K with 𝕏^o,2≠𝕐^o,2\widehat{\mathbb{X}}^{o,2}\neq\widehat{\mathbb{Y}}^{o,2}. We show that there exists a k∈ℕk\in\mathbb{N}, I∈{0,…,d}NI\in\{0,\ldots,d\}^{N}, N∈{0,1,2}N\in\{0,1,2\}, such that

|  |  |  |
| --- | --- | --- |
|  | ⟨(eI​e0⊗k)⊗e0,𝕏^To⟩≠⟨(eI​e0⊗k)⊗e0,𝕐^To⟩.\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{X}}^{o}\_{T}\rangle\neq\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{Y}}^{o}\_{T}\rangle. |  |

We proceed with a proof by contradiction. Assume that for all k∈ℕk\in\mathbb{N}, I∈{0,…,d}NI\in\{0,\ldots,d\}^{N}, N∈{0,1,2}N\in\{0,1,2\}, we have

|  |  |  |
| --- | --- | --- |
|  | ⟨(eI​e0⊗k)⊗e0,𝕏^To⟩=⟨(eI​e0⊗k)⊗e0,𝕐^To⟩.\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{X}}^{o}\_{T}\rangle=\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{Y}}^{o}\_{T}\rangle. |  |

We first note that

|  |  |  |
| --- | --- | --- |
|  | ⟨e0⊗k,𝕏^to⟩=tkk!.\langle e\_{0}^{\otimes k},\widehat{\mathbb{X}}^{o}\_{t}\rangle=\frac{t^{k}}{k!}. |  |

Moreover, using the shuffle property, we have by e.g. [[CPSF25](https://arxiv.org/html/2602.05898v1#bib.bibx27), Proposition C.5], that

|  |  |  |
| --- | --- | --- |
|  | ⟨(eI​e0⊗k)⊗e0,𝕏^To⟩=∫0T⟨eI,𝕏^to⟩​⟨e0⊗k,𝕏^to⟩​dt=∫0T⟨eI,𝕏^to⟩​tkk!​dt.\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{X}}^{o}\_{T}\rangle=\int\_{0}^{T}\langle e\_{I},\widehat{\mathbb{X}}^{o}\_{t}\rangle\langle e\_{0}^{\otimes k},\widehat{\mathbb{X}}^{o}\_{t}\rangle\,\mathrm{d}t=\int\_{0}^{T}\langle e\_{I},\widehat{\mathbb{X}}^{o}\_{t}\rangle\frac{t^{k}}{k!}\,\mathrm{d}t. |  |

Similarly, we have

|  |  |  |
| --- | --- | --- |
|  | ⟨(eI​e0⊗k)⊗e0,𝕐^To⟩=∫0T⟨eI,𝕐^to⟩​tkk!​dt.\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{Y}}^{o}\_{T}\rangle=\int\_{0}^{T}\langle e\_{I},\widehat{\mathbb{Y}}^{o}\_{t}\rangle\frac{t^{k}}{k!}\,\mathrm{d}t. |  |

By [[Bre11](https://arxiv.org/html/2602.05898v1#bib.bibx18), Corollary 4.24] and because ⟨eI,𝕏^0o⟩=⟨eI,𝕐^0o⟩=0\langle e\_{I},\widehat{\mathbb{X}}^{o}\_{0}\rangle=\langle e\_{I},\widehat{\mathbb{Y}}^{o}\_{0}\rangle=0, it then follows that

|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝕏^to⟩=⟨eI,𝕐^to⟩,\langle e\_{I},\widehat{\mathbb{X}}^{o}\_{t}\rangle=\langle e\_{I},\widehat{\mathbb{Y}}^{o}\_{t}\rangle, |  |

for all t∈[0,T]t\in[0,T] and all I∈{0,…,d}NI\in\{0,\ldots,d\}^{N}, N∈{0,1,2}N\in\{0,1,2\}. However, this contradicts the assumption that 𝕏^o,2\widehat{\mathbb{X}}^{o,2}, 𝕐^o,2\widehat{\mathbb{Y}}^{o,2} are distinct. Thus, we can conclude that 𝒜\mathcal{A} is point-separating.
∎

## Appendix B Proof of Lemma [3.4](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths")

In this appendix we present the proof of the auxiliary Lemma [3.4](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths").

###### Proof of Lemma [3.4](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths").

For γ≠12\gamma\neq\frac{1}{2}, the statement follows from Lemma [3.3](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem3 "Lemma 3.3 (Lemma 2.16 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths") and [[AKLP25a](https://arxiv.org/html/2602.05898v1#bib.bibx4), Proposition 2.12].

Suppose that γ=12\gamma=\frac{1}{2}. We need to verify that the integral

|  |  |  |
| --- | --- | --- |
|  | ∫0tX^r⊗d12,πn​X^r=∫0tXr⊗d12,πn​Xr+∫0tXr⊗d12,πn​φr+∫0tφr⊗d12,πn​Xr+∫0tφr⊗d12,πn​φr,\int\_{0}^{t}\widehat{X}\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}\widehat{X}\_{r}=\int\_{0}^{t}X\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}X\_{r}+\int\_{0}^{t}X\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}\varphi\_{r}+\int\_{0}^{t}\varphi\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}X\_{r}+\int\_{0}^{t}\varphi\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}\varphi\_{r}, |  |

converges as n→∞n\to\infty to the limit

|  |  |  |
| --- | --- | --- |
|  | ∫0tX^r⊗d12,π​Xr=∫0tXr⊗d12,π​Xr+∫0tXr⊗d12,π​φr+∫0tφr⊗d12,π​Xr+∫0tφr⊗d12,π​φr,\int\_{0}^{t}\widehat{X}\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi}X\_{r}=\int\_{0}^{t}X\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi}X\_{r}+\int\_{0}^{t}X\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi}\varphi\_{r}+\int\_{0}^{t}\varphi\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi}X\_{r}+\int\_{0}^{t}\varphi\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi}\varphi\_{r}, |  |

uniformly in t∈[0,T]t\in[0,T], where the latter three integrals are given as Young integrals.

Since XX satisfies Property 1/21/2-(RIE), we have that

|  |  |  |
| --- | --- | --- |
|  | ‖∫0⋅Xr⊗d12,πn​Xr−∫0⋅Xr⊗d12,π​Xr‖∞⟶0asn→∞.\bigg\|\int\_{0}^{\cdot}X\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}X\_{r}-\int\_{0}^{\cdot}X\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi}X\_{r}\bigg\|\_{\infty}\longrightarrow 0\qquad\text{as}\qquad n\to\infty. |  |

Define X¯n\bar{X}^{n} and φ¯n\bar{\varphi}^{n} as the piecewise linear interpolation of XX and φ\varphi, respectively, along π=(πn)n∈ℕ\pi=(\pi^{n})\_{n\in\mathbb{N}}. Then, it holds for any t∈[0,T]t\in[0,T] that

|  |  |  |
| --- | --- | --- |
|  | ∫0tXr⊗d12,πn​φr=∑k=0Nn−1(Xtkn+12​Xtkn,tk+1n)⊗φtkn∧t,tk+1n∧t=∫0tX¯rn⊗dφr.\int\_{0}^{t}X\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}\varphi\_{r}=\sum\_{k=0}^{N\_{n}-1}(X\_{t^{n}\_{k}}+\frac{1}{2}X\_{t^{n}\_{k},t^{n}\_{k+1}})\otimes\varphi\_{t^{n}\_{k}\wedge t,t^{n}\_{k+1}\wedge t}=\int\_{0}^{t}\bar{X}^{n}\_{r}\otimes\mathrm{d}\varphi\_{r}. |  |

Let p′>pp^{\prime}>p such that 1/p′+1/q>11/p^{\prime}+1/q>1. By the standard estimate for Young integrals—see e.g. [[FZ18](https://arxiv.org/html/2602.05898v1#bib.bibx33), Proposition 2.4]—we have for all t∈[0,T]t\in[0,T], that

|  |  |  |
| --- | --- | --- |
|  | |∫0tXr⊗d12,πn​φr−∫0tXr⊗d12,π​φr|≲‖X¯n−X‖p′​‖φ‖q.\bigg\lvert\int\_{0}^{t}X\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}\varphi\_{r}-\int\_{0}^{t}X\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi}\varphi\_{r}\bigg\rvert\lesssim\|\bar{X}^{n}-X\|\_{p^{\prime}}\|\varphi\|\_{q}. |  |

It follows by interpolation—see e.g. [[FV10](https://arxiv.org/html/2602.05898v1#bib.bibx32), Proposition 5.5]—that

|  |  |  |
| --- | --- | --- |
|  | ‖X¯n−X‖p′≤‖X¯n−X‖∞1−pp′​‖X¯n−X‖ppp′.\|\bar{X}^{n}-X\|\_{p^{\prime}}\leq\|\bar{X}^{n}-X\|\_{\infty}^{1-\frac{p}{p^{\prime}}}\|\bar{X}^{n}-X\|\_{p}^{\frac{p}{p^{\prime}}}. |  |

Since X¯n\bar{X}^{n} converges uniformly to XX as n→∞n\to\infty, and supn∈ℕ‖X¯n‖p<∞\sup\_{n\in\mathbb{N}}\|\bar{X}^{n}\|\_{p}<\infty, we deduce that

|  |  |  |
| --- | --- | --- |
|  | ‖∫0⋅Xr⊗d12,πn​φr−∫0⋅Xr⊗d12,π​φr‖∞⟶ 0asn⟶∞.\bigg\|\int\_{0}^{\cdot}X\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}\varphi\_{r}-\int\_{0}^{\cdot}X\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi}\varphi\_{r}\bigg\|\_{\infty}\,\longrightarrow\,0\qquad\text{as}\quad n\,\longrightarrow\,\infty. |  |

Similarly, for each t∈[0,T]t\in[0,T], it holds that

|  |  |  |
| --- | --- | --- |
|  | |∫0tφr⊗d12,πn​Xr−∫0tφr⊗d12,π​Xr|≲‖φ¯n−φ‖q​‖X‖p,\bigg|\int\_{0}^{t}\varphi\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}X\_{r}-\int\_{0}^{t}\varphi\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi}X\_{r}\bigg|\lesssim\|\bar{\varphi}^{n}-\varphi\|\_{q}\|X\|\_{p}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | |∫0tφr⊗d12,πn​φr−∫0tφr⊗d12,π​φr|≲‖φ¯n−φ‖q​‖φ‖q,\bigg|\int\_{0}^{t}\varphi\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}\varphi\_{r}-\int\_{0}^{t}\varphi\_{r}\otimes\mathrm{d}^{\frac{1}{2},\pi}\varphi\_{r}\bigg|\lesssim\|\bar{\varphi}^{n}-\varphi\|\_{q}\|\varphi\|\_{q}, |  |

and, since ‖φ¯n−φ‖q→0\|\bar{\varphi}^{n}-\varphi\|\_{q}\to 0 as n→∞n\to\infty, we infer the required convergence.

We further aim to find a control function cc such that

|  |  |  |  |
| --- | --- | --- | --- |
| (B.1) |  | sup(s,t)∈ΔT|X^s,t|pc​(s,t)+supn∈ℕsup0≤k<ℓ≤Nn|∫tkntℓnX^u⊗d12,πn​X^u−X^tkn⊗X^tkn,tk+1n|p2c​(tkn,tℓn)≲1,\sup\_{(s,t)\in\Delta\_{T}}\frac{|\widehat{X}\_{s,t}|^{p}}{c(s,t)}+\sup\_{n\in\mathbb{N}}\,\sup\_{0\leq k<\ell\leq N\_{n}}\frac{|\int\_{t^{n}\_{k}}^{t^{n}\_{\ell}}\widehat{X}\_{u}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}\widehat{X}\_{u}-\widehat{X}\_{t^{n}\_{k}}\otimes\widehat{X}\_{t^{n}\_{k},t^{n}\_{k+1}}|^{\frac{p}{2}}}{c(t\_{k}^{n},t\_{\ell}^{n})}\lesssim 1, |  |

where

|  |  |  |
| --- | --- | --- |
|  | ∫tkntℓnX^u⊗d12,πn​X^u−X^tkn⊗X^tkn,tk+1n=∫tkntℓnX^tkn,u⊗d12,πn​X^u\displaystyle\int\_{t^{n}\_{k}}^{t^{n}\_{\ell}}\widehat{X}\_{u}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}\widehat{X}\_{u}-\widehat{X}\_{t^{n}\_{k}}\otimes\widehat{X}\_{t^{n}\_{k},t^{n}\_{k+1}}=\int\_{t^{n}\_{k}}^{t^{n}\_{\ell}}\widehat{X}\_{t^{n}\_{k},u}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}\widehat{X}\_{u} |  |
|  |  |  |
| --- | --- | --- |
|  | =∫tkntℓnXtkn,u⊗d12,πn​Xu+∫tkntℓnXtkn,u⊗d12,πn​φu\displaystyle\quad=\int\_{t^{n}\_{k}}^{t^{n}\_{\ell}}X\_{t^{n}\_{k},u}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}X\_{u}+\int\_{t^{n}\_{k}}^{t^{n}\_{\ell}}X\_{t^{n}\_{k},u}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}\varphi\_{u} |  |
|  |  |  |
| --- | --- | --- |
|  | +∫tkntℓnφtkn,u⊗d12,πn​Xu+∫tkntℓnφtkn,u⊗d12,πn​φu.\displaystyle\qquad+\int\_{t^{n}\_{k}}^{t^{n}\_{\ell}}\varphi\_{t^{n}\_{k},u}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}X\_{u}+\int\_{t^{n}\_{k}}^{t^{n}\_{\ell}}\varphi\_{t^{n}\_{k},u}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}\varphi\_{u}. |  |

Let cXc\_{X} be the control function with respect to which XX satisfies Property γ\gamma-(RIE), and define moreover the control function cφc\_{\varphi}, given by cφ​(s,t)=‖φ‖q,[s,t]qc\_{\varphi}(s,t)=\|\varphi\|\_{q,[s,t]}^{q} for (s,t)∈ΔT(s,t)\in\Delta\_{T}.

We have from Property 1/21/2-(RIE) that

|  |  |  |
| --- | --- | --- |
|  | sup(s,t)∈ΔT|X^s,t|pcX​(s,t)+cφ​(s,t)≲sup(s,t)∈ΔT|Xs,t|pcX​(s,t)+sup(s,t)∈ΔT|φs,t|pcφ​(s,t)≲1,\sup\_{(s,t)\in\Delta\_{T}}\frac{|\widehat{X}\_{s,t}|^{p}}{c\_{X}(s,t)+c\_{\varphi}(s,t)}\lesssim\sup\_{(s,t)\in\Delta\_{T}}\frac{|X\_{s,t}|^{p}}{c\_{X}(s,t)}+\sup\_{(s,t)\in\Delta\_{T}}\frac{|\varphi\_{s,t}|^{p}}{c\_{\varphi}(s,t)}\lesssim 1, |  |

and that

|  |  |  |
| --- | --- | --- |
|  | supn∈ℕsup0≤k<ℓ≤Nn|∫tkntℓnXu⊗d12,πn​Xu−Xtkn⊗Xtkn,tk+1n|p2cX​(tkn,tℓn)≲1.\sup\_{n\in\mathbb{N}}\,\sup\_{0\leq k<\ell\leq N\_{n}}\frac{|\int\_{t\_{k}^{n}}^{t\_{\ell}^{n}}X\_{u}\otimes\mathrm{d}^{\frac{1}{2},\pi^{n}}X\_{u}-X\_{t^{n}\_{k}}\otimes X\_{t^{n}\_{k},t^{n}\_{k+1}}|^{\frac{p}{2}}}{c\_{X}(t\_{k}^{n},t\_{\ell}^{n})}\lesssim 1. |  |

By the standard estimate for Young integrals (see e.g. [[FZ18](https://arxiv.org/html/2602.05898v1#bib.bibx33), Proposition 2.4]), for every n∈ℕn\in\mathbb{N} and 0≤k<ℓ≤Nn0\leq k<\ell\leq N\_{n}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∫tkntℓnX¯tkn,un⊗dφu|p2\displaystyle\bigg|\int\_{t\_{k}^{n}}^{t\_{\ell}^{n}}\bar{X}\_{t\_{k}^{n},u}^{n}\otimes\mathrm{d}\varphi\_{u}\bigg|^{\frac{p}{2}} | ≲‖X¯n‖p,[tkn,tℓn]p2​‖φ‖q,[tkn,tℓn]p2\displaystyle\lesssim\|\bar{X}^{n}\|\_{p,[t\_{k}^{n},t\_{\ell}^{n}]}^{\frac{p}{2}}\|\varphi\|\_{q,[t\_{k}^{n},t\_{\ell}^{n}]}^{\frac{p}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖X‖p,[tkn,tℓn]p2​‖φ‖q,[tkn,tℓn]p2≤cX​(tkn,tℓn)12​cφ​(tkn,tℓn)p2​q,\displaystyle\leq\|X\|\_{p,[t\_{k}^{n},t\_{\ell}^{n}]}^{\frac{p}{2}}\|\varphi\|\_{q,[t\_{k}^{n},t\_{\ell}^{n}]}^{\frac{p}{2}}\leq c\_{X}(t\_{k}^{n},t\_{\ell}^{n})^{\frac{1}{2}}c\_{\varphi}(t\_{k}^{n},t\_{\ell}^{n})^{\frac{p}{2q}}, |  |

and we can similarly obtain

|  |  |  |
| --- | --- | --- |
|  | |∫tkntℓnφ¯tkn,un⊗dXu|p2≲cX​(tkn,tℓn)12​cφ​(tkn,tℓn)p2​q\bigg|\int\_{t\_{k}^{n}}^{t\_{\ell}^{n}}\bar{\varphi}^{n}\_{t\_{k}^{n},u}\otimes\mathrm{d}X\_{u}\bigg|^{\frac{p}{2}}\lesssim c\_{X}(t\_{k}^{n},t\_{\ell}^{n})^{\frac{1}{2}}c\_{\varphi}(t\_{k}^{n},t\_{\ell}^{n})^{\frac{p}{2q}} |  |

and

|  |  |  |
| --- | --- | --- |
|  | |∫tkntℓnφ¯tkn,un⊗dφu|p2≲cφ​(tkn,tℓn)pq.\bigg|\int\_{t\_{k}^{n}}^{t\_{\ell}^{n}}\bar{\varphi}\_{t\_{k}^{n},u}^{n}\otimes\mathrm{d}\varphi\_{u}\bigg|^{\frac{p}{2}}\lesssim c\_{\varphi}(t\_{k}^{n},t\_{\ell}^{n})^{\frac{p}{q}}. |  |

Since p∈(2,3)p\in(2,3) and q∈[1,2)q\in[1,2), we have that 1/2+p/2​q>11/2+p/2q>1 and p/q>1p/q>1, and it follows that the maps (s,t)↦cX​(s,t)12​cφ​(s,t)p2​q(s,t)\mapsto c\_{X}(s,t)^{\frac{1}{2}}c\_{\varphi}(s,t)^{\frac{p}{2q}} and (s,t)↦cφ​(s,t)pq(s,t)\mapsto c\_{\varphi}(s,t)^{\frac{p}{q}} are superadditive and thus control functions. We deduce that ([B.1](https://arxiv.org/html/2602.05898v1#A2.E1 "In Proof of Lemma 3.4. ‣ Appendix B Proof of Lemma 3.4 ‣ Universal approximation with signatures of non-geometric rough paths")) holds with a control function cc of the form

|  |  |  |
| --- | --- | --- |
|  | c​(s,t)=C​(cX​(s,t)+cφ​(s,t)+cX​(s,t)12​cφ​(s,t)p2​q+cφ​(s,t)pq),(s,t)∈ΔT,c(s,t)=C\Big(c\_{X}(s,t)+c\_{\varphi}(s,t)+c\_{X}(s,t)^{\frac{1}{2}}c\_{\varphi}(s,t)^{\frac{p}{2q}}+c\_{\varphi}(s,t)^{\frac{p}{q}}\Big),\qquad(s,t)\in\Delta\_{T}, |  |

where C>0C>0 is a suitable constant which depends only on pp and qq.
∎

## Appendix C On Lyons’ extension theorem

We prove that Lyons’ extension of a rough path (that is not necessarily weakly geometric) for p∈(2,3)p\in(2,3), see e.g. [[LCL07](https://arxiv.org/html/2602.05898v1#bib.bibx43), Theorem 3.7], coincides with the collection of iterated integrals defined via rough integration with respect to controlled paths.

###### Proposition C.1.

Let p∈(2,3)p\in(2,3). Let 𝐗=(X,𝕏(2))\mathbf{X}=(X,\mathbb{X}^{(2)}) be a rough path such that

|  |  |  |
| --- | --- | --- |
|  | |Xs,t|≲c​(s,t)1p,|𝕏s,t(2)|≲c​(s,t)2p,(s,t)∈ΔT,|X\_{s,t}|\lesssim c(s,t)^{\frac{1}{p}},\qquad|\mathbb{X}^{(2)}\_{s,t}|\lesssim c(s,t)^{\frac{2}{p}},\qquad(s,t)\in\Delta\_{T}, |  |

for some control function cc. For (s,t)∈ΔT(s,t)\in\Delta\_{T}, N>2N>2, consider the iterated integral of order NN, i.e., 𝕏s,t(N):=∫st(𝕏s,⋅(N−1))r⊗d𝐗\mathbb{X}^{(N)}\_{s,t}:=\int\_{s}^{t}(\mathbb{X}^{(N-1)}\_{s,\cdot})\_{r}\otimes\mathrm{d}\mathbf{X} as a rough integral of r↦(𝕏s,⋅(N−1))r=𝕏s,r(N−1)r\mapsto(\mathbb{X}^{(N-1)}\_{s,\cdot})\_{r}=\mathbb{X}^{(N-1)}\_{s,r}, which is a controlled path w.r.t. XX on [s,t][s,t], with respect to 𝐗\mathbf{X}. (For the definition of the rough integral, we particularly refer to Remark [D.2](https://arxiv.org/html/2602.05898v1#A4.Thmtheorem2 "Remark D.2. ‣ Appendix D Some additional results in rough path theory ‣ Universal approximation with signatures of non-geometric rough paths").) Then,

|  |  |  |
| --- | --- | --- |
|  | (s,t)↦(1,Xs,t,𝕏s,t(2),…,𝕏s,t(N))∈TN​(ℝd)(s,t)\mapsto(1,X\_{s,t},\mathbb{X}^{(2)}\_{s,t},\dots,\mathbb{X}^{(N)}\_{s,t})\in T^{N}(\mathbb{R}^{d}) |  |

satisfies |𝕏s,t(N)|≲c​(s,t)Np|\mathbb{X}^{(N)}\_{s,t}|\lesssim c(s,t)^{\frac{N}{p}}, (s,t)∈ΔT(s,t)\in\Delta\_{T}, and coincides with Lyons’ extension of (1,Xs,t,𝕏s,t(2))(1,X\_{s,t},\mathbb{X}^{(2)}\_{s,t}) to TN​(ℝd)T^{N}(\mathbb{R}^{d}), as given in e.g. [[LCL07](https://arxiv.org/html/2602.05898v1#bib.bibx43), Theorem 3.7], for any N>2N>2.

###### Proof.

Let N=3N=3. We note that

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,v(N−1)−𝕏s,u(N−1)=𝕏s,v(2)−𝕏s,u(2)=𝕏u,v(2)+Xs,u⊗Xu,v,s≤u≤v≤t.\mathbb{X}^{(N-1)}\_{s,v}-\mathbb{X}^{(N-1)}\_{s,u}=\mathbb{X}^{(2)}\_{s,v}-\mathbb{X}^{(2)}\_{s,u}=\mathbb{X}^{(2)}\_{u,v}+X\_{s,u}\otimes X\_{u,v},\qquad s\leq u\leq v\leq t. |  |

That is, r↦𝕏s,r(2)r\mapsto\mathbb{X}^{(2)}\_{s,r} is a controlled path w.r.t. XX on [s,t][s,t], with (𝕏s,⋅(2))u′=Xs,u(\mathbb{X}^{(2)}\_{s,\cdot})^{\prime}\_{u}=X\_{s,u} and Ru,v𝕏s,⋅(2)=𝕏u,v(2)R^{\mathbb{X}^{(2)}\_{s,\cdot}}\_{u,v}=\mathbb{X}^{(2)}\_{u,v}.

To show the existence of the rough integral of a controlled path with respect to a rough path, we set Au,v:=𝕏s,u(2)⊗Xu,v+(𝕏s,⋅(2))u′⊗𝕏u,v(2)A\_{u,v}:=\mathbb{X}^{(2)}\_{s,u}\otimes X\_{u,v}+(\mathbb{X}^{(2)}\_{s,\cdot})^{\prime}\_{u}\otimes\mathbb{X}^{(2)}\_{u,v} and δ​Au,v,w:=Au,w−Au,v−Av,w\delta A\_{u,v,w}:=A\_{u,w}-A\_{u,v}-A\_{v,w} for s≤u≤v≤w≤ts\leq u\leq v\leq w\leq t. We then have that

|  |  |  |
| --- | --- | --- |
|  | |δ​Au,v,w|\displaystyle|\delta A\_{u,v,w}| |  |
|  |  |  |
| --- | --- | --- |
|  | =|−Ru,v𝕏s,⋅(2)⊗Xv,w−((𝕏s,⋅(2))v′−(𝕏s,⋅(2))u′)⊗𝕏v,w(2)|\displaystyle\quad=|-R^{\mathbb{X}^{(2)}\_{s,\cdot}}\_{u,v}\otimes X\_{v,w}-((\mathbb{X}^{(2)}\_{s,\cdot})^{\prime}\_{v}-(\mathbb{X}^{(2)}\_{s,\cdot})^{\prime}\_{u})\otimes\mathbb{X}^{(2)}\_{v,w}| |  |
|  |  |  |
| --- | --- | --- |
|  | =|−𝕏u,v(2)⊗Xv,w−Xu,v⊗𝕏v,w(2)|\displaystyle\quad=|-\mathbb{X}^{(2)}\_{u,v}\otimes X\_{v,w}-X\_{u,v}\otimes\mathbb{X}^{(2)}\_{v,w}| |  |
|  |  |  |
| --- | --- | --- |
|  | ≲c​(u,v)2p​c​(v,w)1p+c​(u,v)1p​c​(v,w)2p≲c​(u,w)3p.\displaystyle\quad\lesssim c(u,v)^{\frac{2}{p}}c(v,w)^{\frac{1}{p}}+c(u,v)^{\frac{1}{p}}c(v,w)^{\frac{2}{p}}\lesssim c(u,w)^{\frac{3}{p}}. |  |

Therefore, by the sewing lemma, we obtain the estimate

|  |  |  |
| --- | --- | --- |
|  | |𝕏s,t(3)|=|∫st(𝕏s,⋅(2))r⊗d𝐗r|=|∫st(𝕏s,⋅(2))r⊗d𝐗r−(𝕏s,⋅(2))s⊗Xs,t−(𝕏s,⋅(2))s′⊗𝕏s,t(2)|≲c​(s,t)3p,|\mathbb{X}^{(3)}\_{s,t}|=\bigg|\int\_{s}^{t}(\mathbb{X}^{(2)}\_{s,\cdot})\_{r}\otimes\mathrm{d}\mathbf{X}\_{r}\bigg|=\bigg|\int\_{s}^{t}(\mathbb{X}^{(2)}\_{s,\cdot})\_{r}\otimes\mathrm{d}\mathbf{X}\_{r}-(\mathbb{X}^{(2)}\_{s,\cdot})\_{s}\otimes X\_{s,t}-(\mathbb{X}^{(2)}\_{s,\cdot})^{\prime}\_{s}\otimes\mathbb{X}^{(2)}\_{s,t}\bigg|\lesssim c(s,t)^{\frac{3}{p}}, |  |

for (s,t)∈ΔT(s,t)\in\Delta\_{T}.

We apply an inductive argument: Assuming that the claim holds true for any n<Nn<N, for N>3N>3, we now let n≤Nn\leq N. We begin by noting that r↦Yr:=𝕏s,r(n−1)r\mapsto Y\_{r}:=\mathbb{X}^{(n-1)}\_{s,r} is a controlled path w.r.t. XX on [s,t][s,t] (as a rough integral) and we observe that, by Chen’s relation,

|  |  |  |
| --- | --- | --- |
|  | Yv−Yu=𝕏s,v(n−1)−𝕏s,u(n−1)=∑j=0n−3𝕏s,u(j)⊗𝕏u,v(n−1−j)+𝕏s,u(n−2)⊗Xu,v,Y\_{v}-Y\_{u}=\mathbb{X}^{(n-1)}\_{s,v}-\mathbb{X}^{(n-1)}\_{s,u}=\sum\_{j=0}^{n-3}\mathbb{X}^{(j)}\_{s,u}\otimes\mathbb{X}^{(n-1-j)}\_{u,v}+\mathbb{X}^{(n-2)}\_{s,u}\otimes X\_{u,v}, |  |

for s≤u≤v≤ts\leq u\leq v\leq t. That is, Yu′=𝕏s,u(n−2)Y^{\prime}\_{u}=\mathbb{X}^{(n-2)}\_{s,u}, and Ru,vY=∑j=0n−3𝕏s,u(j)⊗𝕏u,v(n−1−j)R^{Y}\_{u,v}=\sum\_{j=0}^{n-3}\mathbb{X}^{(j)}\_{s,u}\otimes\mathbb{X}^{(n-1-j)}\_{u,v}. Analogously to above, we derive for Au,v:=Yu⊗Xu,v+Yu′⊗𝕏u,v(2)A\_{u,v}:=Y\_{u}\otimes X\_{u,v}+Y^{\prime}\_{u}\otimes\mathbb{X}^{(2)}\_{u,v} and δ​Au,v,w:=Au,w−Au,v−Av,w\delta A\_{u,v,w}:=A\_{u,w}-A\_{u,v}-A\_{v,w} that

|  |  |  |
| --- | --- | --- |
|  | |δ​Au,v,w|=|−Ru,vY⊗Xv,w−Yu,v′⊗𝕏v,w(2)|\displaystyle|\delta A\_{u,v,w}|=|-R^{Y}\_{u,v}\otimes X\_{v,w}-Y^{\prime}\_{u,v}\otimes\mathbb{X}^{(2)}\_{v,w}| |  |
|  |  |  |
| --- | --- | --- |
|  | =|−(∑j=0n−3𝕏s,u(j)⊗𝕏u,v(n−1−j))⊗Xv,w−(∑j=0n−3𝕏s,u(j)⊗𝕏u,v(n−2−j))⊗𝕏v,w(2)|\displaystyle\quad=\bigg|-(\sum\_{j=0}^{n-3}\mathbb{X}^{(j)}\_{s,u}\otimes\mathbb{X}^{(n-1-j)}\_{u,v})\otimes X\_{v,w}-(\sum\_{j=0}^{n-3}\mathbb{X}^{(j)}\_{s,u}\otimes\mathbb{X}^{(n-2-j)}\_{u,v})\otimes\mathbb{X}^{(2)}\_{v,w}\bigg| |  |
|  |  |  |
| --- | --- | --- |
|  | =|−(∑j=0n−3𝕏s,u(j)⊗(𝕏u,v(n−1−j)⊗Xv,w+𝕏u,v(n−2−j)⊗𝕏v,w(2))|\displaystyle\quad=\bigg|-(\sum\_{j=0}^{n-3}\mathbb{X}^{(j)}\_{s,u}\otimes(\mathbb{X}^{(n-1-j)}\_{u,v}\otimes X\_{v,w}+\mathbb{X}^{(n-2-j)}\_{u,v}\otimes\mathbb{X}^{(2)}\_{v,w})\bigg| |  |
|  |  |  |
| --- | --- | --- |
|  | ≲∑j=0n−3c​(s,u)jp​(c​(u,v)n−1−jp​c​(v,w)1p+c​(u,v)n−2−jp​c​(v,w)2p)\displaystyle\quad\lesssim\sum\_{j=0}^{n-3}c(s,u)^{\frac{j}{p}}(c(u,v)^{\frac{n-1-j}{p}}c(v,w)^{\frac{1}{p}}+c(u,v)^{\frac{n-2-j}{p}}c(v,w)^{\frac{2}{p}}) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∑j=0n−3c​(s,t)jp​c​(u,v)n−1−jp​c​(v,w)1p+c​(s,t)jp​c​(u,v)n−2−jp​c​(v,w)2p\displaystyle\quad\leq\sum\_{j=0}^{n-3}c(s,t)^{\frac{j}{p}}c(u,v)^{\frac{n-1-j}{p}}c(v,w)^{\frac{1}{p}}+c(s,t)^{\frac{j}{p}}c(u,v)^{\frac{n-2-j}{p}}c(v,w)^{\frac{2}{p}} |  |
|  |  |  |
| --- | --- | --- |
|  | =∑j=0n−3w1,1,jα1,1​(u,v)​w1,2α1,2​(v,w)+w2,1,jα2,1​(u,v)​w2,2α2,2​(v,w),\displaystyle\quad=\sum\_{j=0}^{n-3}w\_{1,1,j}^{\alpha\_{1,1}}(u,v)w\_{1,2}^{\alpha\_{1,2}}(v,w)+w\_{2,1,j}^{\alpha\_{2,1}}(u,v)w\_{2,2}^{\alpha\_{2,2}}(v,w), |  |

where

|  |  |  |
| --- | --- | --- |
|  | w1,1,j=c​(s,t)pn−1−j​jp​c,α1,1=n−1−jp,w1,2=c,α1,2=1p,\displaystyle w\_{1,1,j}=c(s,t)^{\frac{p}{n-1-j}\frac{j}{p}}c,\quad\alpha\_{1,1}=\frac{n-1-j}{p},\quad w\_{1,2}=c,\quad\alpha\_{1,2}=\frac{1}{p}, |  |
|  |  |  |
| --- | --- | --- |
|  | w2,1,j=c​(s,t)pn−2−j​jp​c,α2,1=n−2−jp,w2,2=c,α2,2=2p.\displaystyle w\_{2,1,j}=c(s,t)^{\frac{p}{n-2-j}\frac{j}{p}}c,\quad\alpha\_{2,1}=\frac{n-2-j}{p},\quad w\_{2,2}=c,\quad\alpha\_{2,2}=\frac{2}{p}. |  |

Then, by the generalized sewing lemma, see e.g. [[FZ18](https://arxiv.org/html/2602.05898v1#bib.bibx33), Theorem 2.5], we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝕏s,t(n)|\displaystyle|\mathbb{X}^{(n)}\_{s,t}| | =|∫st(𝕏s,⋅(n−1))r⊗d𝐗r|\displaystyle=\bigg|\int\_{s}^{t}(\mathbb{X}^{(n-1)}\_{s,\cdot})\_{r}\otimes\mathrm{d}\mathbf{X}\_{r}\bigg| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =|∫st(𝕏s,⋅(n−1))r⊗d𝐗r−(𝕏s,⋅(n−1))s⊗Xs,t−(𝕏s,⋅(n−1))s′⊗𝕏s,t(n−1)|\displaystyle=\bigg|\int\_{s}^{t}(\mathbb{X}^{(n-1)}\_{s,\cdot})\_{r}\otimes\mathrm{d}\mathbf{X}\_{r}-(\mathbb{X}^{(n-1)}\_{s,\cdot})\_{s}\otimes X\_{s,t}-(\mathbb{X}^{(n-1)}\_{s,\cdot})^{\prime}\_{s}\otimes\mathbb{X}^{(n-1)}\_{s,t}\bigg| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≲∑j=0n−3w1,1,jα1,1​(s,t)​w1,2α1,2​(s,t)+w2,1,jα2,1​(s,t)​w2,2α2,2​(s,t)\displaystyle\lesssim\sum\_{j=0}^{n-3}w\_{1,1,j}^{\alpha\_{1,1}}(s,t)w\_{1,2}^{\alpha\_{1,2}}(s,t)+w\_{2,1,j}^{\alpha\_{2,1}}(s,t)w\_{2,2}^{\alpha\_{2,2}}(s,t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j=0n−3c​(s,t)jp​c​(s,t)n−1−jp​c​(s,t)1p+c​(s,t)jp​c​(s,t)n−2−jp​c​(s,t)2p\displaystyle=\sum\_{j=0}^{n-3}c(s,t)^{\frac{j}{p}}c(s,t)^{\frac{n-1-j}{p}}c(s,t)^{\frac{1}{p}}+c(s,t)^{\frac{j}{p}}c(s,t)^{\frac{n-2-j}{p}}c(s,t)^{\frac{2}{p}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≲nc​(s,t)np.\displaystyle\lesssim\_{n}c(s,t)^{\frac{n}{p}}. |  |

Further, we notice that (s,t)↦(1,Xs,t,𝕏s,t(2),…,𝕏s,t(N))∈TN​(ℝd)(s,t)\mapsto(1,X\_{s,t},\mathbb{X}^{(2)}\_{s,t},\dots,\mathbb{X}^{(N)}\_{s,t})\in T^{N}(\mathbb{R}^{d}) is a multiplicative functional by definition.

Now take 𝕏~N\widetilde{\mathbb{X}}^{N} to be Lyons’ extension of (1,Xs,t,𝕏s,t(2))(1,X\_{s,t},\mathbb{X}^{(2)}\_{s,t}) to TN​(ℝd)T^{N}(\mathbb{R}^{d}) for any N>3N>3. We know that both 𝕏3\mathbb{X}^{3} and 𝕏~3\widetilde{\mathbb{X}}^{3} are of finite pp-variation controlled by cc. Since 𝕏2=𝕏~2\mathbb{X}^{2}=\widetilde{\mathbb{X}}^{2}, it holds that

|  |  |  |
| --- | --- | --- |
|  | |𝕏s,t3−𝕏~s,t3|=|𝕏s,t(3)−𝕏~s,t(3)|≤C​c​(s,t)3p,(s,t)∈ΔT,|\mathbb{X}^{3}\_{s,t}-\widetilde{\mathbb{X}}^{3}\_{s,t}|=|\mathbb{X}^{(3)}\_{s,t}-\widetilde{\mathbb{X}}^{(3)}\_{s,t}|\leq Cc(s,t)^{\frac{3}{p}},\qquad(s,t)\in\Delta\_{T}, |  |

where CC denotes the sum of the two implicit multiplicative constants in the regularity estimates of 𝕏(3)\mathbb{X}^{(3)} and 𝕏~(3)\widetilde{\mathbb{X}}^{(3)}, respectively. By [[LCL07](https://arxiv.org/html/2602.05898v1#bib.bibx43), Lemma 3.4], the map (s,t)↦𝕏s,t(3)−𝕏~s,t(3)(s,t)\mapsto\mathbb{X}^{(3)}\_{s,t}-\widetilde{\mathbb{X}}^{(3)}\_{s,t} is additive in (ℝd)⊗3(\mathbb{R}^{d})^{\otimes 3}, so that the path 𝕏0,⋅(3)−𝕏~0,⋅(3)\mathbb{X}^{(3)}\_{0,\cdot}-\widetilde{\mathbb{X}}^{(3)}\_{0,\cdot} is of finite p/3p/3-variation in (ℝd)⊗3(\mathbb{R}^{d})^{\otimes 3} starting at zero. Due to the regularity of cc and since p/3<1p/3<1, it then follows that (s,t)↦𝕏s,t(3)−𝕏~s,t(3)(s,t)\mapsto\mathbb{X}^{(3)}\_{s,t}-\widetilde{\mathbb{X}}^{(3)}\_{s,t} is equal to zero, that is 𝕏3\mathbb{X}^{3} equals 𝕏(3)\mathbb{X}^{(3)}. We apply an induction argument on NN: Because the arguments carry through, we conclude that 𝕏N=𝕏~N\mathbb{X}^{N}=\widetilde{\mathbb{X}}^{N} for any N≥1N\geq 1, which completes the proof.
∎

## Appendix D Some additional results in rough path theory

We recall and extend some essential results on rough integration and rough paths.

###### Lemma D.1 (Proposition 2.4 in [[ALP24](https://arxiv.org/html/2602.05898v1#bib.bibx6)]).

Let 𝐗=(X,𝕏)∈𝒞p​([0,T];ℝd)\mathbf{X}=(X,\mathbb{X})\in\mathcal{C}^{p}([0,T];\mathbb{R}^{d}) and let (F,F′),(G,G′)∈𝒞Xp(F,F^{\prime}),(G,G^{\prime})\in\mathscr{C}^{p}\_{X} be controlled paths with remainders RFR^{F} and RGR^{G}, respectively. Then the limit

|  |  |  |  |
| --- | --- | --- | --- |
| (D.1) |  | ∫0TFr​dGr:=lim|𝒫|→0∑[s,t]∈𝒫Fs​Gs,t+Fs′​Gs′​𝕏s,t\int\_{0}^{T}F\_{r}\,\mathrm{d}G\_{r}:=\lim\_{|\mathcal{P}|\to 0}\sum\_{[s,t]\in\mathcal{P}}F\_{s}G\_{s,t}+F^{\prime}\_{s}G^{\prime}\_{s}\mathbb{X}\_{s,t} |  |

exists along every sequence of partitions 𝒫\mathcal{P} of [0,T][0,T] with mesh size |𝒫|→0|\mathcal{P}|\to 0, and comes with the estimate

|  |  |  |
| --- | --- | --- |
|  | |∫stFr​dGr−Fs​Gs,t−Fs′​Gs′​𝕏s,t|\displaystyle\bigg|\int\_{s}^{t}F\_{r}\,\mathrm{d}G\_{r}-F\_{s}G\_{s,t}-F^{\prime}\_{s}G^{\prime}\_{s}\mathbb{X}\_{s,t}\bigg| |  |
|  |  |  |
| --- | --- | --- |
|  | ≤C(∥F′∥∞(∥G′∥p,[s,t)p+∥X∥p,[s,t)p)2p∥X∥p,[s,t]+∥F∥p,[s,t)∥RG∥p2,[s,t]\displaystyle\quad\leq C\Big(\|F^{\prime}\|\_{\infty}(\|G^{\prime}\|\_{p,[s,t)}^{p}+\|X\|\_{p,[s,t)}^{p})^{\frac{2}{p}}\|X\|\_{p,[s,t]}+\|F\|\_{p,[s,t)}\|R^{G}\|\_{\frac{p}{2},[s,t]} |  |
|  |  |  |
| --- | --- | --- |
|  | +∥RF∥p2,[s,t)∥G′∥∞∥X∥p,[s,t]+∥F′G′∥p,[s,t)∥𝕏∥p2,[s,t]),\displaystyle\quad\quad\quad\quad+\|R^{F}\|\_{\frac{p}{2},[s,t)}\|G^{\prime}\|\_{\infty}\|X\|\_{p,[s,t]}+\|F^{\prime}G^{\prime}\|\_{p,[s,t)}\|\mathbb{X}\|\_{\frac{p}{2},[s,t]}\Big), |  |

for every (s,t)∈ΔT(s,t)\in\Delta\_{T}, where the constant CC depends only on pp.

###### Remark D.2.

For m,n>1m,n>1, suppose that F∈Cp​-var​([0,T];(ℝd)⊗m−1)F\in C^{p\textup{-var}}([0,T];(\mathbb{R}^{d})^{\otimes m-1}), F′∈Cp​-var​([0,T];(ℝd)⊗m)F^{\prime}\in C^{p\textup{-var}}([0,T];(\mathbb{R}^{d})^{\otimes m}), G∈Cp​-var​([0,T];(ℝd)⊗n−1)G\in C^{p\textup{-var}}([0,T];(\mathbb{R}^{d})^{\otimes n-1}), G′∈Cp​-var​([0,T];(ℝd)⊗n)G^{\prime}\in C^{p\textup{-var}}([0,T];(\mathbb{R}^{d})^{\otimes n}). Then,

|  |  |  |
| --- | --- | --- |
|  | ∫0TFr​dGr:=∫0TFr⊗dGr:=lim|𝒫|→0∑[s,t]∈𝒫Fs⊗Gs,t+(Fs′⊗Gs′)​𝕏s,t,\int\_{0}^{T}F\_{r}\,\mathrm{d}G\_{r}:=\int\_{0}^{T}F\_{r}\otimes\mathrm{d}G\_{r}:=\lim\_{|\mathcal{P}|\to 0}\sum\_{[s,t]\in\mathcal{P}}F\_{s}\otimes G\_{s,t}+(F^{\prime}\_{s}\otimes G^{\prime}\_{s})\mathbb{X}\_{s,t}, |  |

relative to the rough path 𝐗=(X,𝕏)\mathbf{X}=(X,\mathbb{X}). In writing Fs′⊗Gs,t′F^{\prime}\_{s}\otimes G^{\prime}\_{s,t}, we technically mean the m+nm+n-tensor whose component is given by [Fs′⊗Gs′]i1​…​im​j1​…​jn=(Fs′)i1​…​im​(Gs′)j1​…​jn[F^{\prime}\_{s}\otimes G^{\prime}\_{s}]^{i\_{1}\dots i\_{m}j\_{1}\dots j\_{n}}=(F^{\prime}\_{s})^{i\_{1}\dots i\_{m}}(G^{\prime}\_{s})^{j\_{1}\dots j\_{n}}, and we interpret the “multiplication” (Fs′⊗Gs′)​𝕏s,t(F^{\prime}\_{s}\otimes G^{\prime}\_{s})\mathbb{X}\_{s,t} as the matrix whose (m−1)+(n−1)(m-1)+(n-1) component is given by [(Fs′⊗Gs′)​𝕏s,t]i1​…​im−1​j1​…​jn−1=∑i∑j(Fs′)i1​…​im−1​i​(Gs′)j1​…​jn−1​j​𝕏i​j[(F^{\prime}\_{s}\otimes G^{\prime}\_{s})\mathbb{X}\_{s,t}]^{i\_{1}\dots i\_{m-1}j\_{1}\dots j\_{n-1}}=\sum\_{i}\sum\_{j}(F^{\prime}\_{s})^{i\_{1}\dots i\_{m-1}i}(G^{\prime}\_{s})^{j\_{1}\dots j\_{n-1}j}\mathbb{X}^{ij}.

Property γ\gamma-(RIE) not only ensures the existence of a suitable rough path lift of a path, but also allows the rough integral to be expressed as a limit of Riemann sums, depending on γ\gamma. The next theorem is a slight generalization of [[DKP25](https://arxiv.org/html/2602.05898v1#bib.bibx28), Theorem 2.12].

###### Theorem D.3.

Let p∈(2,3)p\in(2,3), and let πn={0=t0n<t1n<⋯<tNnn=T}\pi^{n}=\{0=t^{n}\_{0}<t^{n}\_{1}<\dots<t^{n}\_{N\_{n}}=T\}, n∈ℕn\in\mathbb{N}, be a sequence of partitions such that |πn|→0|\pi^{n}|\to 0 as n→∞n\to\infty. Suppose that X∈C​([0,T];ℝd)X\in C([0,T];\mathbb{R}^{d}) satisfies Property γ\gamma-(RIE) relative to some γ∈[0,1]\gamma\in[0,1], pp and π=(πn)n∈ℕ\pi=(\pi^{n})\_{n\in\mathbb{N}}, and let 𝐗γ,π\mathbf{X}^{\gamma,\pi} be the canonical rough path lift of XX, as constructed in Proposition [3.1](https://arxiv.org/html/2602.05898v1#S3.Thmtheorem1 "Proposition 3.1 (Proposition 2.9 in [DKP25]). ‣ 3.1. On Property 𝜸-(RIE) ‣ 3. The signature using general pathwise stochastic integration ‣ Universal approximation with signatures of non-geometric rough paths"). Let q>0q>0 be such that 2/p+1/q>12/p+1/q>1 and let (F,F′),(G,G′)∈𝒞Xp,q(F,F^{\prime}),(G,G^{\prime})\in\mathscr{C}^{p,q}\_{X} be controlled paths with respect to XX. Then, the limit

|  |  |  |
| --- | --- | --- |
|  | ∫0tFr​dGr=limn→∞∑k=0Nn−1(Ftkn+γ​Ftkn,tk+1n)​Gtkn∧t,tk+1n∧t,\int\_{0}^{t}F\_{r}\,\mathrm{d}G\_{r}=\lim\_{n\to\infty}\sum\_{k=0}^{N\_{n}-1}(F\_{t^{n}\_{k}}+\gamma F\_{t^{n}\_{k},t^{n}\_{k+1}})G\_{t^{n}\_{k}\wedge t,t^{n}\_{k+1}\wedge t}, |  |

exists, where the convergence holds uniformly for t∈[0,T]t\in[0,T], and it coincides with the rough integral of (F,F′)(F,F^{\prime}) against (G,G′)(G,G^{\prime}) as defined in ([D.1](https://arxiv.org/html/2602.05898v1#A4.E1 "In Lemma D.1 (Proposition 2.4 in [ALP24]). ‣ Appendix D Some additional results in rough path theory ‣ Universal approximation with signatures of non-geometric rough paths")).

###### Proof.

By Lemma [D.1](https://arxiv.org/html/2602.05898v1#A4.Thmtheorem1 "Lemma D.1 (Proposition 2.4 in [ALP24]). ‣ Appendix D Some additional results in rough path theory ‣ Universal approximation with signatures of non-geometric rough paths"), the rough integral of (F,F′)(F,F^{\prime}) against (G,G′)(G,G^{\prime}) (relative to 𝐗γ,π\mathbf{X}^{\gamma,\pi}) exists.

We denote by (F¯n)n∈ℕ(\bar{F}^{n})\_{n\in\mathbb{N}}, (G¯n)n∈ℕ(\bar{G}^{n})\_{n\in\mathbb{N}} and (X¯n)n∈ℕ(\bar{X}^{n})\_{n\in\mathbb{N}} the piecewise linear interpolation of FF, GG and XX, respectively, along π=(πn)n∈ℕ\pi=(\pi^{n})\_{n\in\mathbb{N}}. Thus, (F¯n,F′)(\bar{F}^{n},F^{\prime}) and (G¯n,G′)(\bar{G}^{n},G^{\prime}) are controlled by X¯n\bar{X}^{n}, with remainders Rs,tF¯n=F¯s,tn−Fs′​X¯s,tnR^{\bar{F}^{n}}\_{s,t}=\bar{F}^{n}\_{s,t}-F^{\prime}\_{s}\bar{X}^{n}\_{s,t} and Rs,tG¯n=G¯s,tn−Gs′​X¯s,tnR^{\bar{G}^{n}}\_{s,t}=\bar{G}^{n}\_{s,t}-G^{\prime}\_{s}\bar{X}^{n}\_{s,t}, (s,t)∈ΔT(s,t)\in\Delta\_{T}, respectively. As shown in the proof of [[PP16](https://arxiv.org/html/2602.05898v1#bib.bibx49), Theorem 4.19], if p′>pp^{\prime}>p and q′>qq^{\prime}>q such that 2/p′+1/q′>12/p^{\prime}+1/q^{\prime}>1, then (F¯n,F′,RF¯n)(\bar{F}^{n},F^{\prime},R^{\bar{F}^{n}}) converges in (q′,p′,r′)(q^{\prime},p^{\prime},r^{\prime})-variation to (F,F′,RF)(F,F^{\prime},R^{F}), where 1/r′=1/p′+1/q′1/r^{\prime}=1/p^{\prime}+1/q^{\prime}.

Since the sequence (X¯n)n∈ℕ(\bar{X}^{n})\_{n\in\mathbb{N}} has uniformly bounded pp-variation and X¯n\bar{X}^{n} converges uniformly to XX as n→∞n\to\infty, it follows by interpolation that X¯n\bar{X}^{n} converges to XX with respect to the p′p^{\prime}-variation norm, i.e., ‖X¯n−X‖p′→0\|\bar{X}^{n}-X\|\_{p^{\prime}}\to 0 as n→∞n\to\infty. It follows similarly using [[DKP25](https://arxiv.org/html/2602.05898v1#bib.bibx28), Lemma 2.11] that ∥(𝕏¯n,(2)−(𝕏γ,π,(2)+12[X]γ,π)∥p′2→0\|(\bar{\mathbb{X}}^{n,(2)}-(\mathbb{X}^{\gamma,\pi,(2)}+\frac{1}{2}[X]^{\gamma,\pi})\|\_{\frac{p^{\prime}}{2}}\to 0 and, hence, that ‖(X¯n,𝕏¯n,(2))−(X,𝕏γ,π,(2)+12​[X]γ,π)‖p′→0\|(\bar{X}^{n},\bar{\mathbb{X}}^{n,(2)})-(X,\mathbb{X}^{\gamma,\pi,(2)}+\frac{1}{2}[X]^{\gamma,\pi})\|\_{p^{\prime}}\to 0 as n→∞n\to\infty; analogously for (G,G′,RG)(G,G^{\prime},R^{G}).

It follows from [[AKLP25b](https://arxiv.org/html/2602.05898v1#bib.bibx5), Lemma A.2] that

|  |  |  |  |
| --- | --- | --- | --- |
| (D.2) |  | ∫0tF¯rn​dG¯rn⟶∫0tFr​dGras ​n⟶∞,\int\_{0}^{t}\bar{F}^{n}\_{r}\,\mathrm{d}\bar{G}^{n}\_{r}\longrightarrow\int\_{0}^{t}F\_{r}\,\mathrm{d}G\_{r}\qquad\text{as }n\longrightarrow\infty, |  |

where the convergence is uniform in t∈[0,T]t\in[0,T]. Note that in ([D.2](https://arxiv.org/html/2602.05898v1#A4.E2 "In Proof. ‣ Appendix D Some additional results in rough path theory ‣ Universal approximation with signatures of non-geometric rough paths")) the integral ∫0tFun​dG¯u\int\_{0}^{t}F^{n}\_{u}\,\mathrm{d}\bar{G}\_{u} is defined relative to the rough path (X¯n,𝕏¯n,(2))(\bar{X}^{n},\bar{\mathbb{X}}^{n,(2)}), whilst the limiting rough integral ∫0tFu​dGu\int\_{0}^{t}F\_{u}\,\mathrm{d}G\_{u} is defined relative to (X,𝕏γ,π,(2)+12​[X]γ,π)(X,\mathbb{X}^{\gamma,\pi,(2)}+\frac{1}{2}[X]^{\gamma,\pi}).

But, for every t∈[0,T]t\in[0,T], it holds that

|  |  |  |
| --- | --- | --- |
|  | limn→∞∫0tF¯rn​dG¯rn\displaystyle\lim\_{n\to\infty}\int\_{0}^{t}\bar{F}^{n}\_{r}\,\mathrm{d}\bar{G}^{n}\_{r} |  |
|  |  |  |
| --- | --- | --- |
|  | =limn→∞∑k=0Nn−1(Ftkn+12​Ftkn,tk+1n)​Gtkn∧t,tk+1n∧t\displaystyle\quad=\lim\_{n\to\infty}\sum\_{k=0}^{N\_{n}-1}(F\_{t^{n}\_{k}}+\frac{1}{2}F\_{t^{n}\_{k},t^{n}\_{k+1}})G\_{t^{n}\_{k}\wedge t,t^{n}\_{k+1}\wedge t} |  |
|  |  |  |
| --- | --- | --- |
|  | =limn→∞(∑k=0Nn−1(Ftkn+γ​Ftkn,tk+1n)​Gtkn∧t,tk+1n∧t+12​(1−2​γ)​∑k=0Nn−1Ftkn,tk+1n​Gtkn∧t,tk+1n∧t).\displaystyle\quad=\lim\_{n\to\infty}\Big(\sum\_{k=0}^{N\_{n}-1}(F\_{t^{n}\_{k}}+\gamma F\_{t^{n}\_{k},t^{n}\_{k+1}})G\_{t^{n}\_{k}\wedge t,t^{n}\_{k+1}\wedge t}+\frac{1}{2}(1-2\gamma)\sum\_{k=0}^{N\_{n}-1}F\_{t^{n}\_{k},t^{n}\_{k+1}}G\_{t^{n}\_{k}\wedge t,t^{n}\_{k+1}\wedge t}\Big). |  |

Since (F,F′),(G,G′)∈𝒞Xp,q(F,F^{\prime}),(G,G^{\prime})\in\mathscr{C}^{p,q}\_{X}, it is immediate that the second term on the right-hand side converges to 12​∫0tFs′​Gs′​d​[X]sγ,π\frac{1}{2}\int\_{0}^{t}F^{\prime}\_{s}G^{\prime}\_{s}\,\mathrm{d}[X]^{\gamma,\pi}\_{s}, t∈[0,T]t\in[0,T].

Then, we have that

|  |  |  |
| --- | --- | --- |
|  | limn→∞∑k=0Nn−1(Ftkn+γ​Ftkn,tk+1n)​Gtkn∧t,tk+1n∧t\displaystyle\lim\_{n\to\infty}\sum\_{k=0}^{N\_{n}-1}(F\_{t^{n}\_{k}}+\gamma F\_{t^{n}\_{k},t^{n}\_{k+1}})G\_{t^{n}\_{k}\wedge t,t^{n}\_{k+1}\wedge t} |  |
|  |  |  |
| --- | --- | --- |
|  | =limn→∞∫0tF¯rn​dGrn−12​∫0tFr′​Gr′​d​[X]rγ,π\displaystyle\quad=\lim\_{n\to\infty}\int\_{0}^{t}\bar{F}^{n}\_{r}\,\mathrm{d}G^{n}\_{r}-\frac{1}{2}\int\_{0}^{t}F^{\prime}\_{r}G^{\prime}\_{r}\,\mathrm{d}[X]^{\gamma,\pi}\_{r} |  |
|  |  |  |
| --- | --- | --- |
|  | =∫0tFr​dGr−12​∫0tFr′​Gr′​d​[X]rγ,π\displaystyle\quad=\int\_{0}^{t}F\_{r}\,\mathrm{d}G\_{r}-\frac{1}{2}\int\_{0}^{t}F^{\prime}\_{r}G^{\prime}\_{r}\,\mathrm{d}[X]^{\gamma,\pi}\_{r} |  |
|  |  |  |
| --- | --- | --- |
|  | =lim|𝒫|→0∑[u,v]∈𝒫Fu​Gu,v+Fu′​Gu′​(𝕏γ,π,(2)+12​[X]γ,π)u,v−12​lim|𝒫|→0∑[u,v]∈𝒫Fu′​Gu′​[X]u,vγ,π\displaystyle\quad=\lim\_{|\mathcal{P}|\to 0}\sum\_{[u,v]\in\mathcal{P}}F\_{u}G\_{u,v}+F^{\prime}\_{u}G^{\prime}\_{u}(\mathbb{X}^{\gamma,\pi,(2)}+\frac{1}{2}[X]^{\gamma,\pi})\_{u,v}-\frac{1}{2}\lim\_{|\mathcal{P}|\to 0}\sum\_{[u,v]\in\mathcal{P}}F^{\prime}\_{u}G^{\prime}\_{u}[X]^{\gamma,\pi}\_{u,v} |  |
|  |  |  |
| --- | --- | --- |
|  | =lim|𝒫|→0∑[u,v]∈𝒫Fu​Gu,v+Fu′​Gu′​𝕏u,vγ,π,(2)\displaystyle\quad=\lim\_{|\mathcal{P}|\to 0}\sum\_{[u,v]\in\mathcal{P}}F\_{u}G\_{u,v}+F^{\prime}\_{u}G^{\prime}\_{u}\mathbb{X}^{\gamma,\pi,(2)}\_{u,v} |  |
|  |  |  |
| --- | --- | --- |
|  | =∫0tFr​dGr,\displaystyle\quad=\int\_{0}^{t}F\_{r}\,\mathrm{d}G\_{r}, |  |

where the limit is taken over any sequence of partitions 𝒫\mathcal{P} of [0,t][0,t] with vanishing mesh size.
∎

The following proposition states that the map mapping a rough path to its rough path bracket is continuous.

###### Proposition D.4.

Let p∈(2,3)p\in(2,3). The map

|  |  |  |
| --- | --- | --- |
|  | 𝒞p​([0,T];ℝd)∋𝐗=(X,𝕏(2))↦[𝐗]∈Cp2​([0,T];ℝd)\mathcal{C}^{p}([0,T];\mathbb{R}^{d})\ni\mathbf{X}=(X,\mathbb{X}^{(2)})\mapsto[\mathbf{X}]\in C^{\frac{p}{2}}([0,T];\mathbb{R}^{d}) |  |

is continuous, where the rough path bracket [𝐗][\mathbf{X}] of a rough path 𝐗=(X,𝕏(2))\mathbf{X}=(X,\mathbb{X}^{(2)}) is defined by [𝐗]t:=X0,t⊗X0,t−(𝕏0,t(2)+(𝕏0,t(2))⊤)[\mathbf{X}]\_{t}:=X\_{0,t}\otimes X\_{0,t}-(\mathbb{X}^{(2)}\_{0,t}+(\mathbb{X}^{(2)}\_{0,t})^{\top}), t∈[0,T]t\in[0,T].

###### Proof.

Let 𝐗n=(Xn,𝕏n,(2))\mathbf{X}^{n}=(X^{n},\mathbb{X}^{n,(2)}), n∈ℕn\in\mathbb{N}, 𝐗=(X,𝕏(2))\mathbf{X}=(X,\mathbb{X}^{(2)}) be rough paths such that

|  |  |  |
| --- | --- | --- |
|  | ∥𝐗n;𝐗∥p=∥Xn−X∥p+∥𝕏n,(2)−𝕏(2)∥p2⟶0asn→∞.\|\mathbf{X}^{n};\mathbf{X}\|\_{p}=\|X^{n}-X\|\_{p}+\|\mathbb{X}^{n,(2)}-\mathbb{X}^{(2)}\|\_{\frac{p}{2}}\longrightarrow 0\qquad\text{as}\quad n\to\infty. |  |

We first have that

|  |  |  |
| --- | --- | --- |
|  | ‖𝕏n,(2)+(𝕏n,(2))⊤−(𝕏(2)+(𝕏(2))⊤)‖p2≲‖𝕏n,(2)−𝕏(2)‖p2.\|\mathbb{X}^{n,(2)}+(\mathbb{X}^{n,(2)})^{\top}-(\mathbb{X}^{(2)}+(\mathbb{X}^{(2)})^{\top})\|\_{\frac{p}{2}}\lesssim\|\mathbb{X}^{n,(2)}-\mathbb{X}^{(2)}\|\_{\frac{p}{2}}. |  |

Further, it holds that

|  |  |  |
| --- | --- | --- |
|  | |Xs,tn⊗Xs,tn−Xs,t⊗Xs,t|p2≲|Xs,tn⊗(Xs,tn−Xs,t)|p2+|(Xs,tn−Xs,t)⊗Xs,t|p2\displaystyle|X^{n}\_{s,t}\otimes X^{n}\_{s,t}-X\_{s,t}\otimes X\_{s,t}|^{\frac{p}{2}}\lesssim|X^{n}\_{s,t}\otimes(X^{n}\_{s,t}-X\_{s,t})|^{\frac{p}{2}}+|(X^{n}\_{s,t}-X\_{s,t})\otimes X\_{s,t}|^{\frac{p}{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≲(|Xs,tn|p2+|Xs,t|p2)​|Xs,tn−Xs,t|p2\displaystyle\quad\lesssim(|X^{n}\_{s,t}|^{\frac{p}{2}}+|X\_{s,t}|^{\frac{p}{2}})|X^{n}\_{s,t}-X\_{s,t}|^{\frac{p}{2}} |  |

for any (s,t)∈ΔT(s,t)\in\Delta\_{T}. Thus, by the Cauchy–Schwarz inequality,

|  |  |  |
| --- | --- | --- |
|  | ‖Xn⊗Xn−X⊗X‖p2p2\displaystyle\|X^{n}\otimes X^{n}-X\otimes X\|\_{\frac{p}{2}}^{\frac{p}{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | =sup𝒫∑[s,t]∈𝒫|Xs,tn⊗Xs,tn−Xs,t⊗Xs,t|p2\displaystyle\quad=\sup\_{\mathcal{P}}\sum\_{[s,t]\in\mathcal{P}}|X^{n}\_{s,t}\otimes X^{n}\_{s,t}-X\_{s,t}\otimes X\_{s,t}|^{\frac{p}{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≲sup𝒫∑[s,t]∈𝒫(|Xs,tn|p2+|Xs,t|p2)​|Xs,tn−Xs,t|p2\displaystyle\quad\lesssim\sup\_{\mathcal{P}}\sum\_{[s,t]\in\mathcal{P}}(|X^{n}\_{s,t}|^{\frac{p}{2}}+|X\_{s,t}|^{\frac{p}{2}})|X^{n}\_{s,t}-X\_{s,t}|^{\frac{p}{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≲sup𝒫(∑[s,t]∈𝒫(|Xs,tn|p+|Xs,t|p))12​(∑[s,t]∈𝒫|Xs,tn−Xs,t|p)12\displaystyle\quad\lesssim\sup\_{\mathcal{P}}\bigg(\sum\_{[s,t]\in\mathcal{P}}(|X^{n}\_{s,t}|^{p}+|X\_{s,t}|^{p})\bigg)^{\frac{1}{2}}\bigg(\sum\_{[s,t]\in\mathcal{P}}|X^{n}\_{s,t}-X\_{s,t}|^{p}\bigg)^{\frac{1}{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≲(‖Xn‖pp2+‖X‖pp2)​‖Xn−X‖pp2.\displaystyle\quad\lesssim(\|X^{n}\|\_{p}^{\frac{p}{2}}+\|X\|\_{p}^{\frac{p}{2}})\|X^{n}-X\|\_{p}^{\frac{p}{2}}. |  |

This implies that

|  |  |  |
| --- | --- | --- |
|  | ‖[𝐗n]−[𝐗]‖p2≲(‖Xn‖p+‖X‖p)​‖Xn−X‖p+‖𝕏n,(2)−𝕏(2)‖p2⟶0asn→∞,\|[\mathbf{X}^{n}]-[\mathbf{X}]\|\_{\frac{p}{2}}\lesssim(\|X^{n}\|\_{p}+\|X\|\_{p})\|X^{n}-X\|\_{p}+\|\mathbb{X}^{n,(2)}-\mathbb{X}^{(2)}\|\_{\frac{p}{2}}\longrightarrow 0\qquad\text{as}\quad n\to\infty, |  |

therefore, 𝐗↦[𝐗]\mathbf{X}\mapsto[\mathbf{X}] is continuous.
∎

## References

* [ACLP23]

  Andrew L. Allan, Christa Cuchiero, Chong Liu, and David J. Prömel,
  *Model-free portfolio theory: a rough path approach*, Math. Finance
  33 (2023), no. 3, 709–765.
* [AF25]

  Munawar Ali and Qi Feng, *Branched signature model*, arXiv preprint
  arXiv:2511.00018 (2025).
* [AGTZ22]

  Erdinc Akyildirim, Matteo Gambara, Josef Teichmann, and Syang Zhou,
  *Applications of Signature Methods to Market Anomaly Detection*, arXiv
  preprint arXiv:2201.02441 (2022).
* [AKLP25a]

  Andrew L. Allan, Anna P. Kwossek, Chong Liu, and David J. Prömel,
  *Pathwise convergence of the Euler scheme for rough and stochastic
  differential equations*, J. Lond. Math. Soc. (2) 112 (2025), no. 3,
  Paper No. e70297, 51.
* [AKLP25b]

  Andrew L. Allan, Anna P. Kwossek, Chong Liu, and David J. Prömel,
  *Pathwise analysis of log-optimal portfolios*, arXiv preprint
  arXiv:2507.18232 (2025).
* [ALP24]

  Andrew L. Allan, Chong Liu, and David J. Prömel, *A càdlàg
  rough path foundation for robust finance*, Finance Stoch. 28 (2024),
  215–257.
* [Arr18]

  Imanol Perez Arribas, *Derivatives pricing using signature payoffs*, arXiv
  preprint arXiv:1809.09466 (2018).
* [ASJ18]

  Yacine Aït-Sahalia and Jean Jacod, *Semimartingale: Itô or not?*,
  Stochastic Processes and their Applications 128 (2018), no. 1,
  233–254.
* [ASS21]

  Imanol Perez Arribas, Cristopher Salvi, and Lukasz Szpruch, *Sig-SDEs
  model for quantitative finance*, Proceedings of the First ACM International
  Conference on AI in Finance (New York, NY, USA), ICAIF ’20, Association for
  Computing Machinery, 2021.
* [BC19]

  Horatio Boedihardjo and Ilya Chevyrev, *An isomorphism between branched
  and geometric rough paths*, Ann. Inst. Henri Poincaré Probab. Stat.
  55 (2019), no. 2, 1131–1148.
* [BdRHO25]

  Christian Bayer, Goncalo dos Reis, Blanka Horvath, and Harald Oberhauser,
  *Signature Methods in Finance*, first ed., Springer Finance,
  Springer Cham, 2025.
* [BFT26]

  Carlo Bellingeri, Emilio Ferrucci, and Nikolas Tapia, *Branched Itô
  formula and natural Itô-Stratonovich isomorphism*, Adv. Math.
  484 (2026), Paper No. 110687, 87.
* [BFZ22]

  Erhan Bayraktar, Qi Feng, and Zhaoyu Zhang, *Deep Signature Algorithm for
  Path-Dependent American option pricing*, arXiv preprint arXiv:2211.11691
  (2022).
* [BGLY16]

  Horatio Boedihardjo, Xi Geng, Terry Lyons, and Danyu Yang, *The signature
  of a rough path: uniqueness*, Adv. Math. 293 (2016), 720–737.
* [BHRS23]

  Christian Bayer, Paul P. Hager, Sebastian Riedel, and John Schoenmakers,
  *Optimal stopping with signatures*, Ann. Appl. Probab. 33
  (2023), no. 1, 238–273.
* [BPS25]

  Christian Bayer, Luca Pelizzari, and John Schoenmakers, *Primal and dual
  optimal stopping with signatures*, Finance Stoch. 29 (2025), no. 4,
  981–1014.
* [BR24]

  Christian Bayer and Martin Redmann, *Dimension reduction for path
  signatures*, arXiv preprint arXiv:2412.14723 (2024).
* [Bre11]

  Haim Brezis, *Functional analysis, Sobolev spaces and partial
  differential equations*, Universitext, Springer, New York, 2011.
* [BRSF25]

  Federico M. Bandi, Roberto Renò, and Sara Svaluto-Ferro, *Local
  signature-based expansions*, arXiv preprint arXiv:2504.06351 (2025).
* [CGMSF25]

  Christa Cuchiero, Guido Gazzani, Janka Möller, and Sara Svaluto-Ferro,
  *Joint calibration to SPX and VIX options with signature-based
  models*, Math. Finance 35 (2025), no. 1, 161–213.
* [CGSF23]

  Christa Cuchiero, Guido Gazzani, and Sara Svaluto-Ferro, *Signature-based
  models: theory and calibration*, SIAM J. Financial Math. 14 (2023),
  no. 3, 910–957.
* [Che57]

  Kuo-Tsai Chen, *Integration of paths, geometric invariants and a
  generalized Baker-Hausdorff formula*, Ann. of Math. (2) 65
  (1957), 163–178.
* [Che77]

  Kuo Tsai Chen, *Iterated path integrals*, Bull. Amer. Math. Soc.
  83 (1977), no. 5, 831–879.
* [CK26]

  Ilya Chevyrev and Andrey Kormilitzin, *A Primer on the Signature
  Method in Machine Learning*, Signature Methods in Finance, Springer
  Finance, Springer, Cham, 2026, pp. 3–64.
* [CM25]

  Christa Cuchiero and Janka Möller, *Signature methods in stochastic
  portfolio theory*, SIAM Journal on Financial Mathematics 16 (2025),
  no. 4, 1239–1303.
* [CPASB22]

  Álvaro Cartea, Imanol Pérez Arribas, and Leandro
  Sánchez-Betancourt, *Double-execution strategies using path
  signatures*, SIAM J. Financial Math. 13 (2022), no. 4, 1379–1417.
* [CPSF25]

  Christa Cuchiero, Francesca Primavera, and Sara Svaluto-Ferro, *Universal
  approximation theorems for continuous functions of càdlàg paths and
  Lévy-type signature models*, Finance Stoch. 29 (2025), no. 2,
  289–342.
* [DKP25]

  Purba Das, Anna P. Kwossek, and David J. Prömel, *A rough path
  approach to pathwise stochastic integration à la Föllmer*, arXiv
  preprint arXiv:2507.17363 (2025).
* [FH20]

  Peter K. Friz and Martin Hairer, *A course on rough paths: with an
  introduction to regularity structures*, second edition ed., Universitext,
  Cham, Switzerland, 2020.
* [FHW23]

  Owen Futter, Blanka Horvath, and Magnus Wiese, *Signature Trading: A
  Path-Dependent Extension of the Mean-Variance Framework with
  Exogenous Signals*, arXiv preprint arXiv:2308.15135 (2023).
* [Föl81]

  H. Föllmer, *Calcul d’Itô sans probabilités*, Seminar on
  Probability, XV (Univ. Strasbourg, Strasbourg, 1979/1980)
  (French), Lecture Notes in Math., vol. 850, Springer, Berlin, 1981,
  pp. 143–150.
* [FV10]

  Peter K. Friz and Nicolas B. Victoir, *Multidimensional stochastic
  processes as rough paths*, Cambridge Studies in Advanced Mathematics, vol.
  120, Cambridge University Press, Cambridge, 2010, Theory and applications.
* [FZ18]

  Peter K. Friz and Huilin Zhang, *Differential equations driven by rough
  paths with jumps*, J. Differential Equations 264 (2018), no. 10,
  6226–6301.
* [Gub10]

  Massimiliano Gubinelli, *Ramification of rough paths*, J. Differential
  Equations 248 (2010), no. 4, 693–721.
* [GWZZ25]

  Xin Guo, Binnan Wang, Ruixun Zhang, and Chaoyi Zhao, *On consistency of
  signature using Lasso*, Oper. Res. 73 (2025), no. 5, 2530–2549.
* [HBS24]

  Fabian A. Harang, Fred Espen Benth, and Fride Straum, *Universal
  approximation on non-geometric rough paths and applications to financial
  derivatives pricing*, arXiv preprint arXiv:2412.16009 (2024).
* [Hes93]

  Steven L Heston, *A closed-form solution for options with stochastic
  volatility with applications to bond and currency options*, The review of
  financial studies 6 (1993), no. 2, 327–343.
* [HL10]

  Ben Hambly and Terry Lyons, *Uniqueness for the signature of a path of
  bounded variation and the reduced path group*, Ann. of Math. (2) 171
  (2010), no. 1, 109–167.
* [Hof00]

  Michael E. Hoffman, *Quasi-shuffle products*, J. Algebraic Combin.
  11 (2000), no. 1, 49–68.
* [JDC24]

  Eduardo Abi Jaber and Nathan De Carvalho, *Reconciling rough volatility
  with jumps*, SIAM Journal on Financial Mathematics 15 (2024), no. 3,
  785–823.
* [KLA20]

  Jasdeep Kalsi, Terry Lyons, and Imanol Perez Arribas, *Optimal execution
  with rough path signatures*, SIAM J. Financial Math. 11 (2020),
  no. 2, 470–493.
* [Kob11]

  Kei Kobayashi, *Stochastic calculus for a time-changed semimartingale and
  the associated stochastic differential equations*, Journal of Theoretical
  Probability 24 (2011), no. 3, 789–820.
* [LCL07]

  Terry J. Lyons, Michael Caruana, and Thierry Lévy, *Differential
  equations driven by rough paths*, Lecture Notes in Mathematics, vol. 1908,
  Springer, Berlin, 2007, Lectures from the 34th Summer School on Probability
  Theory held in Saint-Flour, July 6–24, 2004, With an introduction concerning
  the Summer School by Jean Picard.
* [LLN13]

  Daniel Levin, Terry Lyons, and Hao Ni, *Learning from the past, predicting
  the statistics for the future, learning an evolving system*, arXiv preprint
  arXiv:1309.0260 (2013).
* [LNPA19]

  Terry Lyons, Sina Nejad, and Imanol Perez Arribas, *Numerical method for
  model-free pricing of exotic derivatives in discrete time using rough path
  signatures*, Appl. Math. Finance 26 (2019), no. 6, 583–597.
* [LNPA20]

  by same author, *Non-parametric pricing and hedging of exotic derivatives*, Appl.
  Math. Finance 27 (2020), no. 6, 457–494.
* [Lyo98]

  Terry J. Lyons, *Differential equations driven by rough signals*, Rev.
  Mat. Iberoamericana 14 (1998), no. 2, 215–310.
* [ML25]

  Andrew McLeod and Terry Lyons, *Signature methods in machine learning*,
  EMS Surv. Math. Sci., 2025.
* [PP16]

  Nicolas Perkowski and David J. Prömel, *Pathwise stochastic integrals
  for model free finance*, Bernoulli 22 (2016), no. 4, 2486–2520.
* [Pro05]

  Philip E. Protter, *Stochastic integration and differential equations*,
  Stochastic Modelling and Applied Probability, vol. 21, Springer-Verlag,
  Berlin, 2005, Second edition. Version 2.1, Corrected third printing.
* [RG20]

  Jeremy F. Reizenstein and Benjamin Graham, *Algorithm 1004: the
  iisignature library: efficient calculation of iterated-integral signatures
  and log signatures*, ACM Trans. Math. Software 46 (2020), no. 1,
  Art. 8, 21.