---
authors:
- Mihriban Ceylan
- David J. Prömel
doc_id: arxiv:2512.16396v1
family_id: arxiv:2512.16396
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Global universal approximation with Brownian signatures
url_abs: http://arxiv.org/abs/2512.16396v1
url_html: https://arxiv.org/html/2512.16396v1
venue: arXiv q-fin
version: 1
year: 2025
---


Mihriban Ceylan
Mihriban Ceylan, University of Mannheim, Germany
[mihriban.ceylan@uni-mannheim.de](mailto:mihriban.ceylan@uni-mannheim.de)
 and 
David J. Prömel
David J. Prömel, University of Mannheim, Germany
[proemel@uni-mannheim.de](mailto:proemel@uni-mannheim.de)

(Date: December 18, 2025)

###### Abstract.

We establish LpL^{p}-type universal approximation theorems for general and non-anticipative functionals on suitable rough path spaces, showing that linear functionals acting on signatures of time-extended rough paths are dense with respect to an LpL^{p}-distance. To that end, we derive global universal approximation theorems for weighted rough path spaces. We demonstrate that these LpL^{p}-type universal approximation theorems apply in particular to Brownian motion. As a consequence, linear functionals on the signature of the time-extended Brownian motion can approximate any pp-integrable stochastic process adapted to the Brownian filtration, including solutions to stochastic differential equations.

Key words: Brownian motion; non-anticipative functional; rough path; signature; stochastic differential equation; universal approximation theorem; weighted space.

MSC 2010 Classification: Primary 60L10; Secondary: 60H10; 60J65; 91G99.

## 1. Introduction

The efficient approximation of functionals on path spaces is a key challenge in numerous areas, including machine learning, mathematical finance, and data-driven modeling of random dynamical systems. In recent years, so-called signature methods have emerged as a powerful framework for representing and approximating path-dependent functionals; see, for instance, [[ML25](https://arxiv.org/html/2512.16396v1#bib.bibx37), [BdRHO25](https://arxiv.org/html/2512.16396v1#bib.bibx4)]. The concept of signatures was introduced by K.-T. Chen [[Che54](https://arxiv.org/html/2512.16396v1#bib.bibx12)] in the 1950s and has since been extensively studied, most notably in the context of rough path theory [[LCL07](https://arxiv.org/html/2512.16396v1#bib.bibx33)]. Roughly speaking, the signature of a continuous path X:[0,T]→ℝdX\colon[0,T]\to\mathbb{R}^{d} is the collection of its iterated integrals, which is known to faithfully represent the main characteristics of the path, see [[HL10](https://arxiv.org/html/2512.16396v1#bib.bibx25), [BGLY16](https://arxiv.org/html/2512.16396v1#bib.bibx6)].

At the heart of signature methods lie universal approximation theorems, which assert that continuous functionals on suitable path spaces can be approximated arbitrarily well on compact sets by linear functionals acting on signatures; see, for example, [[LLN13](https://arxiv.org/html/2512.16396v1#bib.bibx34), [KO19](https://arxiv.org/html/2512.16396v1#bib.bibx31), [LNPA20](https://arxiv.org/html/2512.16396v1#bib.bibx36)]. Owing to these approximation properties and their rich algebraic structure, signatures are often viewed as natural analogues of polynomials on path spaces. This viewpoint has led to a wide range of applications across disciplines. In machine learning and data science, signature methods have been successfully employed for tasks such as image and texture classification [[Gra13](https://arxiv.org/html/2512.16396v1#bib.bibx24)], the generation of synthetic data [[KBPA+19](https://arxiv.org/html/2512.16396v1#bib.bibx27)], and topological data analysis [[CNO20](https://arxiv.org/html/2512.16396v1#bib.bibx14)]. In mathematical finance, signature methods have found numerous applications, including the pricing of path-dependent options [[LNPA19](https://arxiv.org/html/2512.16396v1#bib.bibx35), [LNPA20](https://arxiv.org/html/2512.16396v1#bib.bibx36), [BFZ24](https://arxiv.org/html/2512.16396v1#bib.bibx5)], model calibration [[CGSF23](https://arxiv.org/html/2512.16396v1#bib.bibx11), [CGMSF25](https://arxiv.org/html/2512.16396v1#bib.bibx10)], optimal execution [[KLA20](https://arxiv.org/html/2512.16396v1#bib.bibx28)], portfolio optimization [[CM25](https://arxiv.org/html/2512.16396v1#bib.bibx13)], and stochastic optimal control [[BBH+25](https://arxiv.org/html/2512.16396v1#bib.bibx3)].

While these signature-based universal approximation theorems are of considerable theoretical and practical interest, they are typically restricted to approximations on compact sets and to general path-dependent functionals. These limitations significantly reduce their applicability, in particular in mathematical finance and in the modeling of random dynamical systems. This issue is already apparent from the well-known fact that the sample paths of many fundamental stochastic processes, such as Brownian motion, do not belong to any fixed compact subset of a path space with positive probability. Moreover, in decision-making problems under uncertainty — such as optimal execution and portfolio selection — relevant functionals are often path-dependent but necessarily non-anticipative, since decisions can only depend on the current and past of the underlying dynamics. These considerations have motivated the development of global universal approximation theorems for both general and non-anticipative functionals, formulated either in weighted function spaces or in LpL^{p}-spaces.

In this paper, we establish LpL^{p}-type universal approximation theorems (Theorems [3.4](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem4 "Theorem 3.4 (𝐿^𝑝-universal approximation theorem on 𝐶̂_{𝑑,𝑇}^𝛼). ‣ 3.1. General functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures") and [3.13](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem13 "Theorem 3.13 (𝐿^𝑝-universal approximation theorem on Λ_𝑇^𝛼). ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures")) for both general path-dependent and non-anticipative functionals on suitable rough path spaces, formulated in terms of the classical signature. More precisely, these results show that linear functionals acting on the signatures of time-extended rough paths are dense with respect to the LpL^{p}-metric. To prove these approximation results, we derive global universal approximation theorems (Propositions [3.3](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem3 "Proposition 3.3 (Universal approximation theorem on ℬ_𝜓⁢(𝐶̂_{𝑑,𝑇}^𝛼)). ‣ 3.1. General functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures") and [3.11](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem11 "Proposition 3.11 (Universal approximation theorem on ℬ_𝜓⁢(Λ_𝑇^𝛼)). ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures")) on suitably weighted spaces of (stopped) rough paths, relying on a weighted version of the Stone–Weierstrass theorem established in [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16)]. The concept of stopped rough paths used throughout follows the standard rough path framework recently used in, e.g., [[KLA20](https://arxiv.org/html/2512.16396v1#bib.bibx28), [BPS25](https://arxiv.org/html/2512.16396v1#bib.bibx8), [CGMSF25](https://arxiv.org/html/2512.16396v1#bib.bibx10)], and can be considered as the natural analogue of stopped paths appearing in the context of functional Itô calculus; see [[CF13](https://arxiv.org/html/2512.16396v1#bib.bibx9), [Dup19](https://arxiv.org/html/2512.16396v1#bib.bibx18)].

The present work is related to recent advances on global universal approximation results for signatures. In contrast to the classical signature employed in the LpL^{p}-type universal approximation theorems established in this paper, the results in [[SA23](https://arxiv.org/html/2512.16396v1#bib.bibx38)] and [[BPS25](https://arxiv.org/html/2512.16396v1#bib.bibx8)] are derived using so-called robust signatures, which were introduced in [[CO22](https://arxiv.org/html/2512.16396v1#bib.bibx15)] as a normalized variant of the classical signature. Recall that the classical signature comes with numerical advantages like analytic formulas for expected signatures are available, whereas such tractability may be lost when working with the robust signature. Moreover, the approaches developed in [[SA23](https://arxiv.org/html/2512.16396v1#bib.bibx38)] and [[BPS25](https://arxiv.org/html/2512.16396v1#bib.bibx8)] differ substantially from the one pursued here; for a more detailed comparison, we refer to Remark [3.14](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem14 "Remark 3.14. ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures"). With regard to universal approximation theorems for weighted spaces, our analysis builds on a modification of the results in [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16)], which we extend here to the setting of stopped rough paths. In contrast to [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16)], where weakly geometric α\alpha-Hölder rough paths are considered, we work with geometric α\alpha-Hölder rough paths, which form a Polish space and are therefore more suitable for measure-theoretic arguments. A related weighted-space approximation result is obtained in [[CM25](https://arxiv.org/html/2512.16396v1#bib.bibx13)] for (Stratonovich-enhanced) stopped continuous semimartingales.

The global approximation results developed in this paper are particularly well suited to applications in stochastic analysis and mathematical finance. We show that the LpL^{p}-type universal approximation theorems apply to time-extended Brownian motion, implying that linear functionals of its signature can approximate any pp-integrable stochastic process adapted to the Brownian filtration, including solutions of stochastic differential equations. The key technical step is to verify that a required exponential moment condition holds under the Wiener measure. These results provide a rigorous theoretical foundation for the universality of signature-based models with Brownian noise, which have recently been introduced in mathematical finance as flexible alternatives to classical models using stochastic differential equations, see, e.g., [[ASS21](https://arxiv.org/html/2512.16396v1#bib.bibx1), [CGSF23](https://arxiv.org/html/2512.16396v1#bib.bibx11), [CGMSF25](https://arxiv.org/html/2512.16396v1#bib.bibx10)]. Indeed, Proposition [4.4](https://arxiv.org/html/2512.16396v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.2. Approximation of stochastic differential equations ‣ 4. Approximation properties of linear functionals on the Brownian signature ‣ Global universal approximation with Brownian signatures") shows that such models can approximate solutions of a broad class of stochastic differential equations, independently of the specific drift and diffusion structures. We refer also to [[SA23](https://arxiv.org/html/2512.16396v1#bib.bibx38), [BPS25](https://arxiv.org/html/2512.16396v1#bib.bibx8)] for related results based on robust signatures.

Organization of the paper: In Section [2](https://arxiv.org/html/2512.16396v1#S2 "2. Preliminaries ‣ Global universal approximation with Brownian signatures"), we recall the underlying concepts of weighted spaces, signatures, and rough path theory. The universal approximation theorems in LpL^{p} and weighted spaces are established in Section [3](https://arxiv.org/html/2512.16396v1#S3 "3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures"), both for general path-dependent and non-anticipative functionals on suitable rough path spaces. In Section [4](https://arxiv.org/html/2512.16396v1#S4 "4. Approximation properties of linear functionals on the Brownian signature ‣ Global universal approximation with Brownian signatures"), we demonstrate that these universal approximation results apply to pp-integrable progressively measurable stochastic processes adapted to the Brownian filtration, including solutions to stochastic differential equations.

Acknowledgments: M. Ceylan gratefully acknowledges financial support by the doctoral scholarship programme from the Avicenna-Studienwerk, Germany.

## 2. Preliminaries

In this section, we introduce the notation and essential background on weighted spaces, signatures, and rough path theory. We refer to [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), [FH20](https://arxiv.org/html/2512.16396v1#bib.bibx19), [CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16)] for a more detailed introduction to these topics.

### 2.1. Essentials on weighted spaces

Let T>0T>0 be a fixed finite time horizon and, for d∈ℕd\in\mathbb{N}, let ℝd\mathbb{R}^{d} be the standard dd-dimensional Euclidean space equipped with the norm |x|:=(∑i=1dxi2)1/2|x|:=(\sum\_{i=1}^{d}x\_{i}^{2})^{1/2} for x=(x1,…,xd)∈ℝdx=(x\_{1},\dots,x\_{d})\in\mathbb{R}^{d}. The space of continuous linear maps ff from the normed space (X,∥⋅∥X)(X,\|\,\cdot\,\|\_{X}) to the normed space (Y,∥⋅∥Y)(Y,\|\,\cdot\,\|\_{Y}) is denoted by ℒ​(X;Y)\mathcal{L}(X;Y), which is equipped with the norm ‖f‖ℒ​(X;Y):=supx∈X,‖x‖X≤1‖f​(x)‖Y\|f\|\_{\mathcal{L}(X;Y)}:=\sup\_{x\in X,\|x\|\_{X}\leq 1}\|f(x)\|\_{Y}. Furthermore, if Y=ℝY=\mathbb{R}, the topological dual space of XX, denoted by X∗X^{\ast}, is identified with ℒ​(X;ℝ)\mathcal{L}(X;\mathbb{R}). Elements of X∗X^{\ast} are linear functionals ℓ:X→ℝ\ell\colon X\to\mathbb{R} and the norm on X∗X^{\ast} is defined by ‖ℓ‖X∗:=supx∈X,‖x‖X≤1|ℓ​(x)|\|\ell\|\_{X^{\ast}}:=\sup\_{x\in X,\|x\|\_{X}\leq 1}|\ell(x)|.

For a Hausdorff topological space (X,τX)(X,\tau\_{X}) and a normed space (E,∥⋅∥E)(E,\|\,\cdot\,\|\_{E}), the space of continuous functions f:X→Ef\colon X\to E is denoted by C​(X;E)C(X;E) and Cb​(X;E)⊆C​(X;E)C\_{b}(X;E)\subseteq C(X;E) denotes the vector subspace of bounded functions. Whenever E=ℝE=\mathbb{R}, we simplify the notation to C​(X):=C​(X;ℝ)C(X):=C(X;\mathbb{R}) and Cb​(X):=Cb​(X;ℝ)C\_{b}(X):=C\_{b}(X;\mathbb{R}), respectively. We write Cbk=Cbk​(ℝm;ℒ​(ℝd;ℝm))C\_{b}^{k}=C\_{b}^{k}(\mathbb{R}^{m};\mathcal{L}(\mathbb{R}^{d};\mathbb{R}^{m})) for the space of kk-times continuously differentiable functions f:ℝm→ℒ​(ℝd;ℝm)f\colon\mathbb{R}^{m}\to\mathcal{L}(\mathbb{R}^{d};\mathbb{R}^{m}) such that ff and all its derivatives up to order kk are continuous and bounded, and equip the space Cbk=Cbk​(ℝm;ℒ​(ℝd;ℝm))C\_{b}^{k}=C\_{b}^{k}(\mathbb{R}^{m};\mathcal{L}(\mathbb{R}^{d};\mathbb{R}^{m})) with the norm

|  |  |  |
| --- | --- | --- |
|  | ‖f‖Cbk:=‖f‖∞+‖D​f‖∞+…+‖Dk​f‖∞,\|f\|\_{C\_{b}^{k}}:=\|f\|\_{\infty}+\|Df\|\_{\infty}+\ldots+\|D^{k}f\|\_{\infty}, |  |

where Dr​fD^{r}f denotes the rr-th order derivative of ff and ∥⋅∥∞\|\,\cdot\,\|\_{\infty} denotes the supremum norm on the corresponding spaces of operators.

For a measure space (X,𝒜,μ)(X,\mathcal{A},\mu) and 1≤p<∞1\leq p<\infty, the (vector-valued) Lebesgue space Lp​(X,μ;ℝd)L^{p}(X,\mu;\mathbb{R}^{d}) is defined as the space of (equivalence classes of) 𝒜\mathcal{A}-measurable functions f:X→ℝdf\colon X\to\mathbb{R}^{d} such that

|  |  |  |
| --- | --- | --- |
|  | ‖f‖Lp​(X,μ;ℝd):=(∫X|f​(x)|p​dμ​(x))1p<∞.\|f\|\_{L^{p}(X,\mu;\mathbb{R}^{d})}:=\Bigl(\int\_{X}|f(x)|^{p}\,\,\mathrm{d}\mu(x)\Bigr)^{\frac{1}{p}}<\infty. |  |

For d=1d=1, we simply write Lp​(X):=Lp​(X,μ):=Lp​(X,μ;ℝ)L^{p}(X):=L^{p}(X,\mu):=L^{p}(X,\mu;\mathbb{R}) and ∥⋅∥Lp​(X):=∥⋅∥Lp​(X,μ;ℝd)\|\cdot\|\_{L^{p}(X)}:=\|\cdot\|\_{L^{p}(X,\mu;\mathbb{R}^{d})}.

In the following, we recall the framework of weighted spaces introduced in [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16)], with slight adaptations that are crucial for our purposes. We begin by defining a weighted space and, subsequently, the corresponding weighted function space.

Let (X,τX)(X,\tau\_{X}) be a completely regular Hausdorff topological space. A function ψ:X→(0,∞)\psi\colon X\to(0,\infty) is called an admissible weight function if every pre-image KR:=ψ−1​((0,R])={x∈X:ψ​(x)≤R}K\_{R}:=\psi^{-1}((0,R])=\{x\in X:\psi(x)\leq R\} is compact with respect to τX\tau\_{X}, for all R>0R>0. In this case, we call the pair (X,ψ)(X,\psi) a weighted space.

Furthermore, we define the vector space

|  |  |  |
| --- | --- | --- |
|  | Bψ​(X):={f:X→ℝ:supx∈X|f​(x)|ψ​(x)<∞},B\_{\psi}(X):=\Bigl\{f\colon X\to\mathbb{R}:\sup\_{x\in X}\frac{|f(x)|}{\psi(x)}<\infty\Bigr\}, |  |

consisting of functions f:X→ℝf\colon X\to\mathbb{R}, whose growth is controlled by the growth of the weight function ψ:X→(0,∞)\psi\colon X\to(0,\infty), which we equip with the weighted norm ∥⋅∥ℬψ​(X)\|\,\cdot\,\|\_{\mathcal{B}\_{\psi}(X)} given by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | ‖f‖ℬψ​(X):=supx∈X|f​(x)|ψ​(x),f∈Bψ​(X).\|f\|\_{\mathcal{B}\_{\psi}(X)}:=\sup\_{x\in X}\frac{|f(x)|}{\psi(x)},\quad f\in B\_{\psi}(X). |  |

Note that the embedding Cb​(X)↪Bψ​(X)C\_{b}(X)\hookrightarrow B\_{\psi}(X) is continuous, allowing us to introduce the space

|  |  |  |
| --- | --- | --- |
|  | ℬψ​(X):=Cb​(X)¯∥⋅∥ℬψ​(X),\mathcal{B}\_{\psi}(X):=\overline{C\_{b}(X)}^{\,\|\cdot\|\_{\mathcal{B}\_{\psi}(X)}}, |  |

which is the closure of Cb​(X)C\_{b}(X) with respect to the norm ∥⋅∥ℬψ​(X)\|\,\cdot\,\|\_{\mathcal{B}\_{\psi}(X)}. Note that ℬψ​(X)\mathcal{B}\_{\psi}(X) is a Banach space with the norm ([2.1](https://arxiv.org/html/2512.16396v1#S2.E1 "In 2.1. Essentials on weighted spaces ‣ 2. Preliminaries ‣ Global universal approximation with Brownian signatures")). We refer to ℬψ​(X)\mathcal{B}\_{\psi}(X) as a weighted function space.

### 2.2. Algebraic setting for signatures

The n-fold tensor product of ℝd\mathbb{R}^{d} is given by

|  |  |  |
| --- | --- | --- |
|  | (ℝd)⊗0:=ℝand(ℝd)⊗n:=ℝd⊗…⊗ℝd⏟n,for ​n∈ℕ.(\mathbb{R}^{d})^{\otimes 0}:=\mathbb{R}\quad\text{and}\quad(\mathbb{R}^{d})^{\otimes n}:=\underbrace{\mathbb{R}^{d}\otimes\ldots\otimes\mathbb{R}^{d}}\_{n},\quad\text{for }n\in\mathbb{N}. |  |

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

is called the free Lie algebra 𝔤​(ℝd)\mathfrak{g}(\mathbb{R}^{d}) over ℝd\mathbb{R}^{d}, see e.g. [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), Section 7.3]. It is a subalgebra of T0​((ℝd))T\_{0}((\mathbb{R}^{d})), where we define for c∈ℝc\in\mathbb{R}, the tensor subalgebra Tc​((ℝd)):={𝐚=(a(n))n=0∞∈T​((ℝd)):a(0)=c}T\_{c}((\mathbb{R}^{d})):=\{\mathbf{a}=(a^{(n)})\_{n=0}^{\infty}\in T((\mathbb{R}^{d})):a^{(0)}=c\}. The free Lie group G​((ℝd)):=exp⁡(𝔤​(ℝd))G((\mathbb{R}^{d})):=\exp(\mathfrak{g}(\mathbb{R}^{d})) is defined as the tensor exponential of 𝔤​(ℝd)\mathfrak{g}(\mathbb{R}^{d}), i.e., the image of 𝔤​(ℝd)\mathfrak{g}(\mathbb{R}^{d}) under the map

|  |  |  |
| --- | --- | --- |
|  | exp⊗:T0​((ℝd))→T​((ℝd)),𝐚↦1+∑k=1∞1k!​𝐚⊗k.\exp\_{\otimes}\colon T\_{0}((\mathbb{R}^{d}))\to T((\mathbb{R}^{d})),\qquad\mathbf{a}\mapsto 1+\sum\_{k=1}^{\infty}\frac{1}{k!}\mathbf{a}^{\otimes k}. |  |

G​((ℝd))G((\mathbb{R}^{d})) is a subgroup of T1​((ℝd))T\_{1}((\mathbb{R}^{d})). In fact, (G​((ℝd)),⊗)(G((\mathbb{R}^{d})),\otimes) is a group with unit element (1,0,…,0,…)(1,0,\dots,0,\dots), and for all 𝐠=exp⊗⁡(𝐚)∈G​((ℝd))\mathbf{g}=\exp\_{\otimes}(\mathbf{a})\in G((\mathbb{R}^{d})), the inverse with respect to ⊗\otimes is given by 𝐠−1=exp⊗⁡(−𝐚)\mathbf{g}^{-1}=\exp\_{\otimes}(-\mathbf{a}), for 𝐠=exp⊗⁡(𝐚)∈G​((ℝd))\mathbf{g}=\exp\_{\otimes}(\mathbf{a})\in G((\mathbb{R}^{d})). We call elements in G​((ℝd))G((\mathbb{R}^{d})) group-like elements. For N∈ℕN\in\mathbb{N}, we define the free step-NN nilpotent Lie algebra 𝔤N​(ℝd)⊂T0N​(ℝd)\mathbf{\mathfrak{g}}^{N}(\mathbb{R}^{d})\subset T\_{0}^{N}(\mathbb{R}^{d}) with

|  |  |  |
| --- | --- | --- |
|  | 𝔤N​(ℝd):={0}⊕ℝd⊕[ℝd,ℝd]⊕…⊕[ℝd,[…,[ℝd,ℝd]]]⏟(N−1)​ brackets,\mathbf{\mathfrak{g}}^{N}(\mathbb{R}^{d}):=\{0\}\oplus\mathbb{R}^{d}\oplus[\mathbb{R}^{d},\mathbb{R}^{d}]\oplus\ldots\oplus\underbrace{[\mathbb{R}^{d},[\ldots,[\mathbb{R}^{d},\mathbb{R}^{d}]]]}\_{(N-1)\text{ brackets}}, |  |

where (𝐠,𝐡)↦[𝐠,𝐡]:=𝐠⊗𝐡−𝐡⊗𝐠∈T0N​(ℝd)(\mathbf{g},\mathbf{h})\mapsto[\mathbf{g},\mathbf{h}]:=\mathbf{g}\otimes\mathbf{h}-\mathbf{h}\otimes\mathbf{g}\in T\_{0}^{N}(\mathbb{R}^{d}) denotes the Lie bracket for 𝐠,𝐡∈TN​(ℝd)\mathbf{g},\mathbf{h}\in T^{N}(\mathbb{R}^{d}), see [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), Chapter 7.3.2 and Definition 7.25]. The image GN​(ℝd):=exp⁡(𝔤N​(ℝd))G^{N}(\mathbb{R}^{d}):=\exp(\mathbf{\mathfrak{g}}^{N}(\mathbb{R}^{d})) is a (closed) sub-Lie group of (T1N​(ℝd),⊗)(T\_{1}^{N}(\mathbb{R}^{d}),\otimes), called the free nilpotent group of step NN over ℝd\mathbb{R}^{d}, see [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), Theorem 7.30].

We define I:=(i1,…,in)I:=(i\_{1},\ldots,i\_{n}) as a nn-dimensional multi-index of non-negative integers, i.e. ij∈{1,…,d}i\_{j}\in\{1,\ldots,d\} for every j∈{1,2,…,n}j\in\{1,2,\ldots,n\}. Note that |I|:=n|I|:=n and the empty index is given by I:=∅I:=\emptyset with |I|=0|I|=0. For n≥1n\geq 1 or n≥2n\geq 2, we write I′:=(i1,…,in−1)I^{\prime}:=(i\_{1},\ldots,i\_{n-1}) and I′′:=(i1,…,in−2)I^{\prime\prime}:=(i\_{1},\ldots,i\_{n-2}), respectively. Moreover, for each |I|≥1|I|\geq 1, we set eI:=ei1⊗⋯⊗eine\_{I}:=e\_{i\_{1}}\otimes\cdots\otimes e\_{i\_{n}}.
This allows us to write 𝐚∈T​((ℝd))\mathbf{a}\in T((\mathbb{R}^{d})) (and 𝐚∈T​(ℝd)\mathbf{a}\in T(\mathbb{R}^{d})) as

|  |  |  |
| --- | --- | --- |
|  | 𝐚=∑|I|≥0⟨eI,𝐚⟩​eI,\mathbf{a}=\sum\_{|I|\geq 0}\langle e\_{I},\mathbf{a}\rangle e\_{I}, |  |

where ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle is defined as the inner product of (ℝd)⊗n(\mathbb{R}^{d})^{\otimes n} for each n≥0n\geq 0.

For two multi-indices I=(i1,…,i|I|)I=(i\_{1},\ldots,i\_{|I|}) and J=(j1,…,j|J|)J=(j\_{1},\ldots,j\_{|J|}) with entries in {1,…,d}\{1,\ldots,d\}, the shuffle product is recursively defined by

|  |  |  |
| --- | --- | --- |
|  | eI​eJ:=(eI′​eJ)⊗ei|I|+(eI​eJ′)⊗ej|J|,e\_{I}\shuffle e\_{J}:=(e\_{I^{\prime}}\shuffle e\_{J})\otimes e\_{i\_{|I|}}+(e\_{I}\shuffle e\_{J^{\prime}})\otimes e\_{j\_{|J|}}, |  |

with eI​e∅:=e∅​eI:=eIe\_{I}\shuffle e\_{\emptyset}:=e\_{\emptyset}\shuffle e\_{I}:=e\_{I}.
For all 𝐚∈G​((ℝd))\mathbf{a}\in G((\mathbb{R}^{d})), the shuffle product property holds, i.e., for two multi-indices I=(i1,…,i|I|)I=(i\_{1},\ldots,i\_{|I|}) and J=(j1,…,j|J|)J=(j\_{1},\ldots,j\_{|J|}), it holds that

|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝐚⟩​⟨eJ,𝐚⟩=⟨eI​eJ,𝐚⟩.\langle e\_{I},\mathbf{a}\rangle\langle e\_{J},\mathbf{a}\rangle=\langle e\_{I}\shuffle e\_{J},\mathbf{a}\rangle. |  |

### 2.3. Essentials on rough path theory

Let (E,∥⋅∥E)(E,\|\,\cdot\,\|\_{E}) be a normed space. For α∈(0,1]\alpha\in(0,1], the α\alpha-Hölder norm of a path X∈C​([0,T];E)X\in C([0,T];E) is given by

|  |  |  |
| --- | --- | --- |
|  | ‖X‖α:=sup0≤s<t≤T‖Xt−Xs‖E|t−s|α.\|X\|\_{\alpha}:=\sup\_{0\leq s<t\leq T}\frac{\|X\_{t}-X\_{s}\|\_{E}}{|t-s|^{\alpha}}. |  |

We write Cα​([0,T];E)C^{\alpha}([0,T];E) for the space of all paths X∈C​([0,T];E)X\in C([0,T];E) which satisfy ‖X‖α<∞\|X\|\_{\alpha}<\infty. The 11-variation of a continuous path X:[0,T]→EX\colon[0,T]\to E is defined by

|  |  |  |
| --- | --- | --- |
|  | ‖X‖1​-var:=sup𝒟⊂[0,T]∑ti∈𝒟‖Xti−Xti−1‖E,\|X\|\_{1\textup{-var}}:=\sup\_{\mathcal{D}\subset[0,T]}\sum\_{t\_{i}\in\mathcal{D}}\|X\_{t\_{i}}-X\_{t\_{i-1}}\|\_{E}, |  |

where the supremum is taken over all partitions 𝒟={0=t0<t1<⋯<tn=T}\mathcal{D}=\{0=t\_{0}<t\_{1}<\cdots<t\_{n}=T\} of the interval [0,T][0,T] and ∑ti∈𝒟\sum\_{t\_{i}\in\mathcal{D}} denotes the summation over all points in 𝒟\mathcal{D}. If ‖X‖1​-var<∞\|X\|\_{1\textup{-var}}<\infty, we say that XX is of bounded variation or of finite 11-variation on [0,T][0,T]. The space of continuous paths of bounded variation on [0,T][0,T] with values in EE is denoted by C1​-var​([0,T];E)C^{1\textup{-var}}([0,T];E).

Let ΔT:={(s,t)∈[0,T]2:s≤t}\Delta\_{T}:=\{(s,t)\in[0,T]^{2}:s\leq t\} be the standard 22-simplex. For α∈(0,1]\alpha\in(0,1] and a two-parameter function 𝕏(2):ΔT→E\mathbb{X}^{(2)}\colon\Delta\_{T}\to E, we define

|  |  |  |
| --- | --- | --- |
|  | ‖𝕏(2)‖α:=sup0≤s<t≤T‖𝕏s,t(2)‖E|t−s|α,(s,t)∈ΔT,\|\mathbb{X}^{(2)}\|\_{\alpha}:=\sup\_{0\leq s<t\leq T}\frac{\|\mathbb{X}\_{s,t}^{(2)}\|\_{E}}{|t-s|^{\alpha}},\quad(s,t)\in\Delta\_{T}, |  |

and denote by C2α​(ΔT;E)C\_{2}^{\alpha}(\Delta\_{T};E) the space of all continuous functions 𝕏(2):ΔT→E\mathbb{X}^{(2)}\colon\Delta\_{T}\to E which satisfy ‖𝕏(2)‖α<∞\|\mathbb{X}^{(2)}\|\_{\alpha}<\infty. In what follows, for a path X∈C​([0,T];ℝd)X\in C([0,T];\mathbb{R}^{d}), we will often use the shorthand notation

|  |  |  |
| --- | --- | --- |
|  | Xs,t:=Xt−Xs,(s,t)∈ΔT.X\_{s,t}:=X\_{t}-X\_{s},\quad(s,t)\in\Delta\_{T}. |  |

Let α∈(13,12]\alpha\in(\frac{1}{3},\frac{1}{2}] and X∈Cα​([0,T];ℝd)X\in C^{\alpha}([0,T];\mathbb{R}^{d}). A path Y∈Cα​([0,T];ℝm)Y\in C^{\alpha}([0,T];\mathbb{R}^{m}) is said to be controlled by XX if there exists a path Y′∈Cα​([0,T];ℒ​(ℝd;ℝm))Y^{\prime}\in C^{\alpha}([0,T];\mathcal{L}(\mathbb{R}^{d};\mathbb{R}^{m})) such that the remainder term RY∈C22​α​([0,T];ℝm)R^{Y}\in C^{2\alpha}\_{2}([0,T];\mathbb{R}^{m}) given through the relation

|  |  |  |
| --- | --- | --- |
|  | Ys,t=Ys′​Xs,t+Rs,tY,(s,t)∈ΔT,Y\_{s,t}=Y\_{s}^{\prime}X\_{s,t}+R\_{s,t}^{Y},\quad(s,t)\in\Delta\_{T}, |  |

satisfies ‖RY‖2​α<∞.\|R^{Y}\|\_{2\alpha}<\infty. The path Y′Y^{\prime} is called Gubinelli derivative of YY. The set of controlled paths (Y,Y′)(Y,Y^{\prime}) is denoted by 𝒟X2​α​([0,T];ℝm)\mathcal{D}\_{X}^{2\alpha}([0,T];\mathbb{R}^{m}), see [[FH20](https://arxiv.org/html/2512.16396v1#bib.bibx19), Definition 4.6].

For a path X∈C1​-var​([0,T];ℝd)X\in C^{1\textup{-var}}([0,T];\mathbb{R}^{d}) of finite variation, we denote by 𝕏N\mathbb{X}^{N} the signature truncated at level NN, which is given by

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,tN:=(1,∫s<u<tdXu,…,∫s<u1<…<uN<tdXu1⊗⋯⊗dXuN)∈TN​(ℝd),\mathbb{X}\_{s,t}^{N}:=\Bigl(1,\int\_{s<u<t}\,\mathrm{d}X\_{u},\ldots,\int\_{s<u\_{1}<\ldots<u\_{N}<t}\,\mathrm{d}X\_{u\_{1}}\otimes\cdots\otimes\,\mathrm{d}X\_{u\_{N}}\Bigr)\in T^{N}(\mathbb{R}^{d}), |  |

for 0≤s≤t≤T0\leq s\leq t\leq T, where the integrals are defined in a classical Riemann–Stieltjes sense. The signature 𝕏s,t\mathbb{X}\_{s,t} of the path XX on [s,t][s,t], given by

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,t:=(1,Xs,t,𝕏s,t(2),…,)∈T((ℝd)),\mathbb{X}\_{s,t}:=(1,X\_{s,t},\mathbb{X}\_{s,t}^{(2)},\ldots,)\in T((\mathbb{R}^{d})), |  |

for 0≤s≤t≤T0\leq s\leq t\leq T, where

|  |  |  |
| --- | --- | --- |
|  | 𝕏s,t(n):=∫s<u1<…<un<tdXu1⊗⋯⊗dXun\mathbb{X}\_{s,t}^{(n)}:=\int\_{s<u\_{1}<\ldots<u\_{n}<t}\,\mathrm{d}X\_{u\_{1}}\otimes\cdots\otimes\,\mathrm{d}X\_{u\_{n}} |  |

denotes the nn-th component of 𝕏s,t\mathbb{X}\_{s,t}. For s=0s=0 we simply write 𝕏t\mathbb{X}\_{t}.

Furthermore, the Carnot–Carathéodory norm ∥⋅∥c​c\|\,\cdot\,\|\_{cc} on GN​(ℝd)G^{N}(\mathbb{R}^{d}) is defined by

|  |  |  |
| --- | --- | --- |
|  | ∥𝐠∥c​c:=inf{∫0T|dXt|:X∈C1​-var([0,T];ℝd) such that 𝕏TN=𝐠},\|\mathbf{g}\|\_{cc}:=\inf\biggl\{\int\_{0}^{T}|\,\mathrm{d}X\_{t}|\,:\,X\in C^{1\textup{-var}}([0,T];\mathbb{R}^{d})\text{ such that }\mathbb{X}\_{T}^{N}=\mathbf{g}\biggr\}, |  |

for 𝐠∈GN​(ℝd)\mathbf{g}\in G^{N}(\mathbb{R}^{d}), which induces a metric via

|  |  |  |
| --- | --- | --- |
|  | dc​c​(𝐠,𝐡):=‖𝐠−1⊗𝐡‖c​c,for ​𝐠,𝐡∈GN​(ℝd).d\_{cc}(\mathbf{g},\mathbf{h}):=\|\mathbf{g}^{-1}\otimes\mathbf{h}\|\_{cc},\quad\text{for }\mathbf{g},\mathbf{h}\in G^{N}(\mathbb{R}^{d}). |  |

For α∈(0,1]\alpha\in(0,1], a continuous path 𝐗:[0,T]→G⌊1/α⌋​(ℝd)\mathbf{X}\colon[0,T]\to G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d}) of the form

|  |  |  |
| --- | --- | --- |
|  | [0,T]∋t↦𝐗t:=(1,𝕏t(1),𝕏t(2),…,𝕏t(⌊1/α⌋))∈G⌊1/α⌋​(ℝd)[0,T]\ni t\mapsto\mathbf{X}\_{t}:=\Bigl(1,\mathbb{X}^{(1)}\_{t},\mathbb{X}\_{t}^{(2)},\ldots,\mathbb{X}\_{t}^{(\lfloor 1/\alpha\rfloor)}\Bigr)\in G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d}) |  |

with 𝐗0:=𝟏:=(1,0,…,0)∈G⌊1/α⌋​(ℝd)\mathbf{X}\_{0}:=\mathbf{1}:=(1,0,\ldots,0)\in G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d}) is called weakly geometric α\alpha-Hölder rough path if the α\alpha-Hölder norm

|  |  |  |
| --- | --- | --- |
|  | ‖𝐗‖c​c,α:=sups<ts,t∈[0,T]dc​c​(𝐗s,𝐗t)|s−t|α<∞,\|\mathbf{X}\|\_{cc,\alpha}:=\sup\_{\overset{s,t\in[0,T]}{s<t}}\frac{d\_{cc}(\mathbf{X}\_{s},\mathbf{X}\_{t})}{|s-t|^{\alpha}}<\infty, |  |

where ⌊1/α⌋:=max⁡{k∈ℤ:k≤1/α}\lfloor 1/\alpha\rfloor:=\max\{k\in\mathbb{Z}\,:\,k\leq 1/\alpha\}. We denote by Cα​([0,T];G⌊1/α⌋​(ℝd))C^{\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})) the space of such weakly geometric α\alpha-Hölder rough paths, which we equip with the metric

|  |  |  |
| --- | --- | --- |
|  | dc​c,α​(𝐗,𝐘):=sups<ts,t∈[0,T]dc​c​(𝐗s,t,𝐘s,t)|s−t|α,d\_{cc,\alpha}(\mathbf{X},\mathbf{Y}):=\sup\_{\overset{s,t\in[0,T]}{s<t}}\frac{d\_{cc}(\mathbf{X}\_{s,t},\mathbf{Y}\_{s,t})}{|s-t|^{\alpha}}, |  |

for 𝐗,𝐘∈Cα​([0,T];G⌊1/α⌋​(ℝd))\mathbf{X},\mathbf{Y}\in C^{\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})), where 𝐗s,t:=𝐗s−1⊗𝐗t∈G⌊1/α⌋​(ℝd)\mathbf{X}\_{s,t}:=\mathbf{X}\_{s}^{-1}\otimes\mathbf{X}\_{t}\in G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d}). Moreover, we introduce the metric

|  |  |  |
| --- | --- | --- |
|  | dc​c,∞​(𝐗,𝐘):=supt∈[0,T]dc​c​(𝐗t,𝐘t),d\_{cc,\infty}(\mathbf{X},\mathbf{Y}):=\sup\_{t\in[0,T]}d\_{cc}(\mathbf{X}\_{t},\mathbf{Y}\_{t}), |  |

for 𝐗,𝐘∈Cα​([0,T];G⌊1/α⌋​(ℝd)).\mathbf{X},\mathbf{Y}\in C^{\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})).

The space of geometric α\alpha-Hölder rough paths, denoted by

|  |  |  |
| --- | --- | --- |
|  | C0,α​([0,T];G⌊1/α⌋​(ℝd)),C^{0,\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})), |  |

is defined as the closure of canonical lifts of smooths paths with respect to the α\alpha-Hölder norm ∥⋅∥c​c,α\|\,\cdot\,\|\_{cc,\alpha}, that is, for every 𝐗∈C0,α​([0,T];G⌊1/α⌋​(ℝd))\mathbf{X}\in C^{0,\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})) there exist a sequence of smooth paths XnX^{n} such that

|  |  |  |
| --- | --- | --- |
|  | dc​c,α​(𝕏n,𝐗)→0​ as ​n→∞,d\_{cc,\alpha}(\mathbb{X}^{n},\mathbf{X})\to 0\text{ as }n\to\infty, |  |

where 𝕏n\mathbb{X}^{n} is the ⌊1/α⌋\lfloor 1/\alpha\rfloor-step signature of XnX^{n}. The space C0,α​([0,T];G⌊1/α⌋​(ℝd))C^{0,\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})) is equipped with the metric

|  |  |  |
| --- | --- | --- |
|  | dc​c,α′​(𝐗,𝐘):=sups<ts,t∈[0,T]dc​c​(𝐗s,t,𝐘s,t)|s−t|α′,d\_{cc,\alpha^{\prime}}(\mathbf{X},\mathbf{Y}):=\sup\_{\overset{s,t\in[0,T]}{s<t}}\frac{d\_{cc}(\mathbf{X}\_{s,t},\mathbf{Y}\_{s,t})}{|s-t|^{\alpha^{\prime}}}, |  |

for 𝐗,𝐘∈C0,α​([0,T];G⌊1/α⌋​(ℝd))\mathbf{X},\mathbf{Y}\in C^{0,\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})) and 0≤α′≤α0\leq\alpha^{\prime}\leq\alpha, where 𝐗s,t:=𝐗s−1⊗𝐗t∈G⌊1/α⌋​(ℝd)\mathbf{X}\_{s,t}:=\mathbf{X}\_{s}^{-1}\otimes\mathbf{X}\_{t}\in G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d}).

The space of geometric α\alpha-Hölder rough paths C0,α​([0,T];G⌊1/α⌋​(ℝd))C^{0,\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})) is a closed subset of the space of weakly geometric α\alpha-Hölder rough paths Cα​([0,T];G⌊1/α⌋​(ℝd))C^{\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})) and thus complete, see [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), Definition 8.19]. The distinction between geometric and weakly geometric rough paths is discussed in detail in [[FV06](https://arxiv.org/html/2512.16396v1#bib.bibx22)].

Let us introduce the truncated signature at level N>⌊1/α⌋N>\lfloor 1/\alpha\rfloor of a (weakly) geometric α\alpha-Hölder rough path 𝐗∈C0,α​([0,T];G⌊1/α⌋​(ℝd))\mathbf{X}\in C^{0,\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})) as the unique Lyons’ extension, see e.g. [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), Theorem 9.5, Corollary 9.11 (ii)], yielding a path 𝕏N:[0,T]→GN​(ℝd)\mathbb{X}^{N}\colon[0,T]\to G^{N}(\mathbb{R}^{d}). Then, 𝕏N\mathbb{X}^{N} has finite α\alpha-Hölder norm ∥⋅∥c​c,α\|\,\cdot\,\|\_{cc,\alpha} and starts with the unit element 𝟏:=(1,0,…,0)∈GN​(ℝd)\mathbf{1}:=(1,0,\ldots,0)\in G^{N}(\mathbb{R}^{d}), and the signature of 𝐗\mathbf{X} is given by

|  |  |  |
| --- | --- | --- |
|  | [0,T]∋t↦𝕏t=(1,𝕏t(1),𝕏t(2),…,𝕏t(⌊1/α⌋),…,𝕏t(N),…).[0,T]\ni t\mapsto\mathbb{X}\_{t}=\Bigl(1,\mathbb{X}^{(1)}\_{t},\mathbb{X}^{(2)}\_{t},\ldots,\mathbb{X}\_{t}^{(\lfloor 1/\alpha\rfloor)},\ldots,\mathbb{X}\_{t}^{(N)},\ldots\Bigl). |  |

###### Remark 2.1.

Note that we equip the space of geometric α\alpha-Hölder rough paths with a weaker topology than the norm topology, to obtain an admissible weight function, i.e., the closed unit ball is then compact (the pre-image KR=ψ−1​((0,R])K\_{R}=\psi^{-1}((0,R]) is then compact w.r.t. the weaker topology). More precisely, in [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16), p. 37] it is discussed that the space C0,α​([0,T];G⌊1/α⌋​(ℝd))C^{0,\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})) equipped with the metric dc​c,α′d\_{cc,\alpha^{\prime}} and the weight function

|  |  |  |
| --- | --- | --- |
|  | ψ​(𝐗):=exp⁡(β​‖𝐗‖c​c,αγ)\psi(\mathbf{X}):=\exp(\beta\|\mathbf{X}\|\_{cc,\alpha}^{\gamma}) |  |

is a weighted space for some β>0\beta>0 and γ≥⌊1/α⌋\gamma\geq\lfloor 1/\alpha\rfloor, which follows from the compact embedding

|  |  |  |
| --- | --- | --- |
|  | (C0,α​([0,T];G⌊1/α⌋​(ℝd)),dc​c,α)↪(C0,α′​([0,T];G⌊1/α⌋​(ℝd)),dc​c,α′)(C^{0,\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})),d\_{cc,\alpha})\hookrightarrow(C^{0,\alpha^{\prime}}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d})),d\_{cc,\alpha^{\prime}}) |  |

for 0<α′<α≤10<\alpha^{\prime}<\alpha\leq 1, see [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16), Remark A.7 (i) and p. 37]. We refer to [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16)] for an extensive discussion of the weaker topologies on the space of geometric α\alpha-Hölder rough paths, including the weak-∗\ast-topology.

## 3. Global approximation with rough path signatures

In this section, we establish LpL^{p}-type universal approximation theorems for linear functionals acting on signatures of time-extended rough paths. Our approach builds on the universal approximation theorem for weighted spaces proven in [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16)]. We begin by deriving a universal approximation result for pp-integrable functionals on the rough path space and then present an analogous theorem for pp-integrable non-anticipative functionals.

### 3.1. General functionals

In this subsection, we consider the space (C^d,Tα,ℬ​(C^d,Tα))(\widehat{C}\_{d,T}^{\alpha},\mathcal{B}(\widehat{C}\_{d,T}^{\alpha})) of time-extended rough paths, which is defined as

|  |  |  |
| --- | --- | --- |
|  | C^d,Tα:={𝐗^∈C0,α​([0,T];G⌊1/α⌋​(ℝd+1)):⟨e0,𝐗^t⟩:=t​ for all ​t∈[0,T]},\widehat{C}\_{d,T}^{\alpha}:=\Bigl\{\widehat{\mathbf{X}}\in C^{0,\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d+1})):\langle e\_{0},\widehat{\mathbf{X}}\_{t}\rangle:=t\text{ for all }t\in[0,T]\Bigr\}, |  |

that is, the subspace of C0,α​([0,T];G⌊1/α⌋​(ℝd+1))C^{0,\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d+1})), where the 0-th coordinate represents the running time, for α∈(0,1)\alpha\in(0,1). The space (C^d,Tα,ℬ​(C^d,Tα))(\widehat{C}\_{d,T}^{\alpha},\mathcal{B}(\widehat{C}\_{d,T}^{\alpha})) is equipped with the α′\alpha^{\prime}-Hölder metric dc​c,α′d\_{cc,\alpha^{\prime}} for some 0<α′<α0<\alpha^{\prime}<\alpha and let ν\nu be a finite Borel measure on (C^d,Tα,ℬ​(C^d,Tα))(\widehat{C}\_{d,T}^{\alpha},\mathcal{B}(\widehat{C}\_{d,T}^{\alpha})), i.e. ν​(C^d,Tα)<∞\nu(\widehat{C}\_{d,T}^{\alpha})<\infty, where ℬ​(C^d,Tα)\mathcal{B}(\widehat{C}\_{d,T}^{\alpha}) denotes the Borel σ\sigma-algebra on C^d,Tα\widehat{C}\_{d,T}^{\alpha}. Moreover, in what follows, we work with the weight function

|  |  |  |  |
| --- | --- | --- | --- |
| (3.1) |  | ψ​(𝐗^):=exp⁡(β​‖𝐗^‖c​c,αγ)\psi(\widehat{\mathbf{X}}):=\exp(\beta\|\widehat{\mathbf{X}}\|\_{cc,\alpha}^{\gamma}) |  |

for some β>0\beta>0 and γ≥⌊1/α⌋\gamma\geq\lfloor 1/\alpha\rfloor. Note that, by Remark [2.1](https://arxiv.org/html/2512.16396v1#S2.Thmtheorem1 "Remark 2.1. ‣ 2.3. Essentials on rough path theory ‣ 2. Preliminaries ‣ Global universal approximation with Brownian signatures"), the space C^d,Tα\widehat{C}\_{d,T}^{\alpha} equipped with dc​c,α′d\_{cc,\alpha^{\prime}} is a weighted space.

###### Remark 3.1.

The signature of a (rough) path determines the path only up to so-called tree-like equivalence; see [[HL10](https://arxiv.org/html/2512.16396v1#bib.bibx25), [BGLY16](https://arxiv.org/html/2512.16396v1#bib.bibx6)]. By augmenting the path with time in the 0-th coordinate, the signature of the resulting time-extended (rough) path uniquely determines the original path up to translation. This property is essential for applying a Stone–Weierstrass theorem in order to obtain universal approximation results for linear functionals on signatures. Although adding time is a natural and commonly used choice, this uniqueness feature can be achieved by extending a (rough) path with any strictly monotone one-dimensional path.

###### Remark 3.2.

We emphasize that, in contrast to [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16)], we do not work with the space of weakly geometric α\alpha-Hölder rough paths, but rather with the space of geometric α\alpha-Hölder rough paths. The reason is that the latter forms a Polish space. Consequently, a geometric α\alpha-Hölder rough path 𝐗\mathbf{X} can be regarded as a C0,α​([0,T];G⌊1/α⌋​(ℝd))C^{0,\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d}))-valued random variable, and its law μ𝐗\mu\_{\mathbf{X}} is then a Borel measure on the corresponding Borel σ\sigma-algebra; see [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), Appendix A1].

To derive LpL^{p}-type universal approximation theorems for linear functionals acting on signatures of time-extended rough paths, we rely on a slight modification of the universal approximation result for weighted spaces established in [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16), Theorem 5.4].

###### Proposition 3.3 (Universal approximation theorem on ℬψ​(C^d,Tα)\mathcal{B}\_{\psi}(\widehat{C}\_{d,T}^{\alpha})).

Let ψ\psi be the weight function given in ([3.1](https://arxiv.org/html/2512.16396v1#S3.E1 "In 3.1. General functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures")). Then, the linear span of the set

|  |  |  |
| --- | --- | --- |
|  | {𝐗^↦⟨eI,𝕏^T⟩:I∈{0,…,d}N,N∈ℕ0}\Bigl\{\widehat{\mathbf{X}}\mapsto\langle e\_{I},\widehat{\mathbb{X}}\_{T}\rangle:I\in\{0,\ldots,d\}^{N},N\in\mathbb{N}\_{0}\Bigr\} |  |

is dense in ℬψ​(C^d,Tα)\mathcal{B}\_{\psi}(\widehat{C}\_{d,T}^{\alpha}), i.e., for every map f∈ℬψ​(C^d,Tα)f\in\mathcal{B}\_{\psi}(\widehat{C}\_{d,T}^{\alpha}) and every ε>0\varepsilon>0 there exists a linear function ℓ:T​((ℝd+1))→ℝ\boldsymbol{\ell}\colon T((\mathbb{R}^{d+1}))\to\mathbb{R} of the form 𝕏^T↦ℓ​(𝕏^T):=∑|I|≤NℓI​⟨eI,𝕏^T⟩\widehat{\mathbb{X}}\_{T}\mapsto\boldsymbol{\ell}(\widehat{\mathbb{X}}\_{T}):=\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{X}}\_{T}\rangle, for some N∈ℕ0N\in\mathbb{N}\_{0} and ℓI∈ℝ\ell\_{I}\in\mathbb{R}, such that

|  |  |  |
| --- | --- | --- |
|  | sup𝐗^∈C^d,Tα|f​(𝐗^)−ℓ​(𝕏^T)|ψ​(𝐗^)<ε.\sup\_{\widehat{\mathbf{X}}\in\widehat{C}\_{d,T}^{\alpha}}\frac{|f(\widehat{\mathbf{X}})-\boldsymbol{\ell}(\widehat{\mathbb{X}}\_{T})|}{\psi(\widehat{\mathbf{X}})}<\varepsilon. |  |

###### Proof.

The proof follows line by line the proof of [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16), Theorem 5.4] by replacing the space of weakly geometric rough paths by the space of geometric rough paths. It relies on the weighted real-valued Stone–Weierstrass theorem established in [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16), Theorem 3.9].
∎

We are now in a position to state a global universal approximation theorem for linear functionals acting on signatures of time-extended rough paths in the space Lp​(C^d,Tα)L^{p}(\widehat{C}\_{d,T}^{\alpha}).

###### Theorem 3.4 (LpL^{p}-universal approximation theorem on C^d,Tα\widehat{C}\_{d,T}^{\alpha}).

Let ψ\psi be the weight function given in ([3.1](https://arxiv.org/html/2512.16396v1#S3.E1 "In 3.1. General functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures")), p>1p>1, and ∫C^d,Tαψp​dν<∞\int\_{\widehat{C}\_{d,T}^{\alpha}}\psi^{p}\,\mathrm{d}\nu<\infty. Moreover, we consider the set

|  |  |  |
| --- | --- | --- |
|  | ℒ:={fℓ:fℓ:𝐗^↦ℓ(𝕏^T)=∑|I|≤NℓI⟨eI,𝕏^T⟩,ℓI∈ℝ,N∈ℕ0,𝐗^∈C^d,Tα}.\mathcal{L}:=\Bigl\{f\_{\ell}\,:\,f\_{\ell}\colon\widehat{\mathbf{X}}\mapsto\boldsymbol{\ell}(\widehat{\mathbb{X}}\_{T})=\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{X}}\_{T}\rangle,\,\ell\_{I}\in\mathbb{R},\,N\in\mathbb{N}\_{0},\,\widehat{\mathbf{X}}\in\widehat{C}\_{d,T}^{\alpha}\Bigr\}. |  |

Then, for every f∈Lp​(C^d,Tα)f\in L^{p}(\widehat{C}\_{d,T}^{\alpha}) and for every ε>0\varepsilon>0, there exists a functional fℓ∈ℒf\_{\ell}\in\mathcal{L} such that

|  |  |  |
| --- | --- | --- |
|  | ‖f−fℓ‖Lp​(C^d,Tα)<ε.\|f-f\_{\ell}\|\_{L^{p}(\widehat{C}\_{d,T}^{\alpha})}<\varepsilon. |  |

###### Proof.

Let f∈Lp​(C^d,Tα,ν)f\in L^{p}(\widehat{C}\_{d,T}^{\alpha},\nu) and fix ε>0\varepsilon>0.

Step 1. For any K>0K>0, we can define the function fK​(x):=1{|f​(x)|≤K}​(x)​f​(x)f\_{K}(x):=1\_{\{|f(x)|\leq K\}}(x)f(x) for which we have ‖f−fK‖Lp​(C^d,Tα)→0\|f-f\_{K}\|\_{L^{p}(\widehat{C}\_{d,T}^{\alpha})}\to 0 as K→∞K\to\infty by dominated convergence. Therefore, there is a Kε>0K^{\varepsilon}>0 such that

|  |  |  |
| --- | --- | --- |
|  | ‖f−fKε‖Lp​(C^d,Tα)≤ε3.\|f-f\_{K^{\varepsilon}}\|\_{L^{p}(\widehat{C}\_{d,T}^{\alpha})}\leq\frac{\varepsilon}{3}. |  |

Step 2. By Lusin’s theorem [[DMP03](https://arxiv.org/html/2512.16396v1#bib.bibx17), Theorem 2.5.17], there is a closed set Cε⊂C^d,TαC^{\varepsilon}\subset\widehat{C}\_{d,T}^{\alpha}, such that fKεf\_{K^{\varepsilon}} restricted to CεC^{\varepsilon} is continuous and ν​(C^d,Tα∖Cε)≤εp(6​Kε)p\nu(\widehat{C}\_{d,T}^{\alpha}\setminus C^{\varepsilon})\leq\frac{\varepsilon^{p}}{(6K^{\varepsilon})^{p}}. By Tietze’s extension theorem [[Fri82](https://arxiv.org/html/2512.16396v1#bib.bibx21), Theorem 3.6.3], there is a continuous extension fε∈Cb​(C^d,Tα;[−Kε,Kε])f^{\varepsilon}\in C\_{b}(\widehat{C}\_{d,T}^{\alpha};[-K^{\varepsilon},K^{\varepsilon}]) of fKε,f\_{K^{\varepsilon}}, such that

|  |  |  |
| --- | --- | --- |
|  | ‖fKε−fε‖Lp​(C^d,Tα)p=∫C^d,Tα∖Cε|fKε−fε|p​dν≤(2​Kε)p​ν​(C^d,Tα∖Cε)≤(ε3)p.\|f\_{K^{\varepsilon}}-f^{\varepsilon}\|\_{L^{p}(\widehat{C}\_{d,T}^{\alpha})}^{p}=\int\_{\widehat{C}\_{d,T}^{\alpha}\setminus C^{\varepsilon}}|f\_{K^{\varepsilon}}-f^{\varepsilon}|^{p}\,\mathrm{d}\nu\leq(2K^{\varepsilon})^{p}\nu(\widehat{C}\_{d,T}^{\alpha}\setminus C^{\varepsilon})\leq\Bigl(\frac{\varepsilon}{3}\Bigr)^{p}. |  |

Step 3. Moreover, since by the definition of the weighted function space ℬψ\mathcal{B}\_{\psi} it holds that Cb​(C^d,Tα)⊆ℬψ​(C^d,Tα)C\_{b}(\widehat{C}\_{d,T}^{\alpha})\subseteq\mathcal{B}\_{\psi}(\widehat{C}\_{d,T}^{\alpha}), by Proposition [3.3](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem3 "Proposition 3.3 (Universal approximation theorem on ℬ_𝜓⁢(𝐶̂_{𝑑,𝑇}^𝛼)). ‣ 3.1. General functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures") we can approximate fεf^{\varepsilon} by a linear function on the signature. More precisely, set M:=∫C^d,Tαψp​dν<∞M:=\int\_{\widehat{C}^{\alpha}\_{d,T}}\psi^{p}\,\mathrm{d}\nu<\infty, then we have

|  |  |  |
| --- | --- | --- |
|  | ‖fε−fℓ‖ℬψ​(C^d,Tα)p=(sup𝐗^∈C^d,Tα|fε​(𝐗^)−ℓ​(𝕏^T)|ψ​(𝐗^))p<εp3p​M.\|{f}^{\varepsilon}-f\_{\ell}\|^{p}\_{\mathcal{B}\_{\psi}(\widehat{C}\_{d,T}^{\alpha})}=\Bigl(\sup\_{\widehat{\mathbf{X}}\in\widehat{C}\_{d,T}^{\alpha}}\frac{|{f}^{\varepsilon}(\widehat{\mathbf{X}})-\boldsymbol{\ell}(\widehat{\mathbb{X}}\_{T})|}{\psi(\widehat{\mathbf{X}})}\Bigr)^{p}<\frac{\varepsilon^{p}}{3^{p}M}. |  |

Hence, we get

|  |  |  |
| --- | --- | --- |
|  | ‖fε−fℓ‖Lp​(C^d,Tα)p≤∫C^d,Tαψp​dν​‖fε−fℓ‖ℬψ​(C^d,Tα)p<(ε3)p.\|{f}^{\varepsilon}-f\_{\ell}\|^{p}\_{L^{p}(\widehat{C}\_{d,T}^{\alpha})}\leq\int\_{\widehat{C}\_{d,T}^{\alpha}}\psi^{p}\,\mathrm{d}\nu~\|{f}^{\varepsilon}-f\_{\ell}\|^{p}\_{\mathcal{B}\_{\psi}(\widehat{C}\_{d,T}^{\alpha})}<\Bigl(\frac{\varepsilon}{3}\Bigr)^{p}. |  |

Hence, combining Step 1-3 reveals that

|  |  |  |
| --- | --- | --- |
|  | ‖f−fℓ‖Lp​(C^d,Tα)≤‖f−fKε‖Lp​(C^d,Tα)+‖fKε−fε‖Lp​(C^d,Tα)+‖fε−fℓ‖Lp​(C^d,Tα)<ε,\|f-f\_{\ell}\|\_{L^{p}(\widehat{C}\_{d,T}^{\alpha})}\leq\|f-f\_{K^{\varepsilon}}\|\_{L^{p}(\widehat{C}\_{d,T}^{\alpha})}+\|f\_{K^{\varepsilon}}-f^{\varepsilon}\|\_{L^{p}(\widehat{C}\_{d,T}^{\alpha})}+\|{f}^{\varepsilon}-f\_{\ell}\|\_{L^{p}(\widehat{C}\_{d,T}^{\alpha})}<\varepsilon, |  |

which concludes the proof.
∎

###### Remark 3.5.

Note that the integrability condition ∫C^d,Tαψp​dν<∞\int\_{\widehat{C}\_{d,T}^{\alpha}}\psi^{p}\,\mathrm{d}\nu<\infty, with the weight function ψ​(𝐗^)=exp⁡(β​‖𝐗^‖c​c,αγ)\psi(\widehat{\mathbf{X}})=\exp\!\bigl(\beta\|\widehat{\mathbf{X}}\|\_{cc,\alpha}^{\gamma}\bigr), corresponds to an exponential moment condition.

### 3.2. Non-anticipative functionals

In this subsection, we derive a global universal approximation theorem on the space of stopped α\alpha-Hölder rough paths. To that end, for α∈(0,1)\alpha\in(0,1) we consider

|  |  |  |
| --- | --- | --- |
|  | C^d,tα:={𝐗^[0,t]∈C0,α​([0,T];G⌊1/α⌋​(ℝd+1)):⟨e0,𝐗^s⟩:=s​ for all ​s∈[0,t]},\widehat{C}\_{d,t}^{\alpha}:=\Bigl\{\widehat{\mathbf{X}}\_{[0,t]}\in C^{0,\alpha}([0,T];G^{\lfloor 1/\alpha\rfloor}(\mathbb{R}^{d+1})):\langle e\_{0},\widehat{\mathbf{X}}\_{s}\rangle:=s\text{ for all }s\in[0,t]\Bigr\}, |  |

where 𝐗^[0,t]\widehat{\mathbf{X}}\_{[0,t]} stands for the rough path 𝐗^\widehat{\mathbf{X}}, which is defined on [0,T][0,T], restricted to the sub-interval [0,t][0,t], for t∈[0,T]t\in[0,T]. Furthermore, we require the notion of stopped rough paths. For related definitions, we refer, for example, to [[KLA20](https://arxiv.org/html/2512.16396v1#bib.bibx28), [BPS25](https://arxiv.org/html/2512.16396v1#bib.bibx8)] in the rough path setting and to [[CM25](https://arxiv.org/html/2512.16396v1#bib.bibx13)] in a rough semimartingale framework. We also note that spaces of stopped paths already appear in the context of functional Itô calculus; see [[CF13](https://arxiv.org/html/2512.16396v1#bib.bibx9), [Dup19](https://arxiv.org/html/2512.16396v1#bib.bibx18)].

###### Definition 3.6.

Let α∈(0,1]\alpha\in(0,1], t∈[0,T]t\in[0,T], and let 𝐗^[0,t]∈C^d,tα\widehat{\mathbf{X}}\_{[0,t]}\in\widehat{C}\_{d,t}^{\alpha} be a geometric α\alpha-Hölder rough path. We define the stopped rough path at time tt, 𝐗^[0,T]t∈C^d,Tα\widehat{\mathbf{X}}^{t}\_{[0,T]}\in\widehat{C}\_{d,T}^{\alpha}, as follows.

Set N:=⌊1/α⌋N:=\lfloor 1/\alpha\rfloor. By geometricity, there exists a sequence of smooth time-extended paths X^sn:=(s,Xsn)\widehat{X}^{n}\_{s}:=(s,X^{n}\_{s}) on [0,t][0,t] such that their canonical lifts 𝕏^n\widehat{\mathbb{X}}^{n} (i.e. their signatures truncated at level NN) converge to 𝐗^\widehat{\mathbf{X}} on [0,t][0,t] in the α\alpha-Hölder rough path metric dc​c,αd\_{cc,\alpha}. For r∈[0,T]r\in[0,T] we define the stopped smooth paths

|  |  |  |
| --- | --- | --- |
|  | X^rn,t:=(r,Xrn,t):=(r,Xr∧tn),r∈[0,T],\widehat{X}^{n,t}\_{r}:=(r,X^{n,t}\_{r}):=(r,X^{n}\_{r\wedge t}),\qquad r\in[0,T], |  |

i.e. the time-extension is not stopped, and let 𝕏^n,t\widehat{\mathbb{X}}^{n,t} be their canonical lifts on [0,T][0,T]. We then set

|  |  |  |
| --- | --- | --- |
|  | 𝐗^[0,T]t:=limn→∞𝕏^[0,T]n,t,\widehat{\mathbf{X}}^{t}\_{[0,T]}:=\lim\_{n\to\infty}\widehat{\mathbb{X}}^{n,t}\_{[0,T]}, |  |

where the limit is taken in dc​c,αd\_{cc,\alpha}. In particular, (𝐗^t)s=𝐗^s(\widehat{\mathbf{X}}^{t})\_{s}=\widehat{\mathbf{X}}\_{s} for all s∈[0,t]s\in[0,t].

###### Definition 3.7.

The space ΛTα\Lambda\_{T}^{\alpha} of stopped geometric α\alpha-Hölder rough paths is defined by

|  |  |  |
| --- | --- | --- |
|  | ΛTα:=⋃t∈[0,T]C^d,tα\Lambda\_{T}^{\alpha}:=\bigcup\_{t\in[0,T]}\widehat{C}\_{d,t}^{\alpha} |  |

and equipped with the metric

|  |  |  |
| --- | --- | --- |
|  | dΛ,α′​(𝐗^[0,t],𝐘^[0,s])=|t−s|+dc​c,α′;[0,t]​(𝐗^[0,t]t,𝐘^[0,t]s),s≤t,d\_{\Lambda,\alpha^{\prime}}(\widehat{\mathbf{X}}\_{[0,t]},\widehat{\mathbf{Y}}\_{[0,s]})=|t-s|+d\_{cc,\alpha^{\prime};[0,t]}(\widehat{\mathbf{X}}^{t}\_{[0,t]},\widehat{\mathbf{Y}}^{s}\_{[0,t]}),\quad s\leq t, |  |

for some 0<α′<α0<\alpha^{\prime}<\alpha.

###### Remark 3.8.

We observe that the topology on the metric space (ΛTα,dΛ,α′)(\Lambda\_{T}^{\alpha},d\_{\Lambda,\alpha^{\prime}}) coincides with the final topology (or quotient topology) induced by the quotient map

|  |  |  |
| --- | --- | --- |
|  | φ:[0,T]×C^d,Tα→ΛTα,φ​(t,𝐗^):=𝐗^[0,t].\varphi\colon[0,T]\times\widehat{C}^{\alpha}\_{d,T}\to\Lambda\_{T}^{\alpha},\qquad\varphi(t,\widehat{\mathbf{X}}):=\widehat{\mathbf{X}}\_{[0,t]}. |  |

Moreover, the space ΛTα\Lambda^{\alpha}\_{T} is Polish, see [[BHRS23](https://arxiv.org/html/2512.16396v1#bib.bibx7), Lemma A.1].

To obtain a global universal approximation result on ΛTα\Lambda\_{T}^{\alpha}, we must verify that (ΛTα,ψ)(\Lambda\_{T}^{\alpha},\psi) forms a weighted space. For this purpose, we consider the weight function

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | ψ​(𝐗^[0,t]):=exp⁡(β​‖𝐗^[0,T]t‖c​c,αγ),𝐗^[0,t]∈ΛTα,\psi(\widehat{\mathbf{X}}\_{[0,t]}):=\exp(\beta\|\widehat{\mathbf{X}}^{t}\_{[0,T]}\|\_{cc,\alpha}^{\gamma}),\quad\widehat{\mathbf{X}}\_{[0,t]}\in\Lambda\_{T}^{\alpha}, |  |

for some β>0\beta>0 and γ≥⌊1/α⌋\gamma\geq\lfloor 1/\alpha\rfloor.

###### Lemma 3.9.

Let 0<α′<α<10<\alpha^{\prime}<\alpha<1 and suppose that ψ\psi is defined as in ([3.2](https://arxiv.org/html/2512.16396v1#S3.E2 "In 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures")). Then, KR:=ψ−1​((0,R])={𝐗^[0,t]∈ΛTα:ψ​(𝐗^[0,t])≤R}K\_{R}:=\psi^{-1}((0,R])=\{\widehat{\mathbf{X}}\_{[0,t]}\in\Lambda\_{T}^{\alpha}:\psi(\widehat{\mathbf{X}}\_{[0,t]})\leq R\} is compact with respect to the quotient topology and (ΛTα,ψ)(\Lambda\_{T}^{\alpha},\psi) is a weighted space.

###### Proof.

First observe that by the definition of the quotient map φ\varphi, we have

|  |  |  |
| --- | --- | --- |
|  | KR=φ​([0,T]×{𝐗^[0,T]t∈C^d,Tα:ψ​(𝐗^[0,t])≤R}).K\_{R}=\varphi\Bigl([0,T]\times\{\widehat{\mathbf{X}}^{t}\_{[0,T]}\in\widehat{C}\_{d,T}^{\alpha}:\psi(\widehat{\mathbf{X}}\_{[0,t]})\leq R\}\Bigr). |  |

Since φ\varphi is continuous, we only need to show that

|  |  |  |
| --- | --- | --- |
|  | [0,T]×{𝐗^[0,T]t∈C^d,Tα:ψ​(𝐗^[0,t])≤R}[0,T]\times\{\widehat{\mathbf{X}}^{t}\_{[0,T]}\in\widehat{C}\_{d,T}^{\alpha}:\psi(\widehat{\mathbf{X}}\_{[0,t]})\leq R\} |  |

is compact in [0,T]×C^d,Tα[0,T]\times\widehat{C}\_{d,T}^{\alpha} to obtain the compactness of KRK\_{R}.

Therefore, observe that the sets {𝐗^[0,T]t∈C^d,Tα:ψ​(𝐗^[0,t])≤R}\{\widehat{\mathbf{X}}^{t}\_{[0,T]}\in\widehat{C}\_{d,T}^{\alpha}:\psi(\widehat{\mathbf{X}}\_{[0,t]})\leq R\} are equicontinuous and pointwise bounded. Using that geometric α\alpha-Hölder rough path spaces are compactly embedded in geometric α′\alpha^{\prime}-Hölder rough path spaces for α′<α\alpha^{\prime}<\alpha (cf. [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16)]), we obtain that the sets {𝐗^[0,T]t∈C^d,Tα:ψ​(𝐗^[0,t])≤R}\{\widehat{\mathbf{X}}^{t}\_{[0,T]}\in\widehat{C}\_{d,T}^{\alpha}:\psi(\widehat{\mathbf{X}}\_{[0,t]})\leq R\} are, by the Arzèla–Ascoli theorem, see e.g. [[Fol99](https://arxiv.org/html/2512.16396v1#bib.bibx20), Theorem 4.43], compact with respect to the α′\alpha^{\prime}-Hölder norm. Since φ\varphi is continuous, KRK\_{R} is also compact for any R>0R>0 due to Tychonoff’s theorem. Thus, (ΛTα,ψ)(\Lambda\_{T}^{\alpha},\psi) is a weighted space. See also [[BPS25](https://arxiv.org/html/2512.16396v1#bib.bibx8), Lemma 2.10] for a similar proof.
∎

###### Definition 3.10.

A map f:ΛTα→ℝf\colon\Lambda\_{T}^{\alpha}\to\mathbb{R} is called a non-anticipative functional if ff is measurable. A map f:ΛTα→ℝf\colon\Lambda\_{T}^{\alpha}\to\mathbb{R} is called continuous if ff is continuous with respect to the metric dΛ,α′d\_{\Lambda,\alpha^{\prime}}.

With these preparations in place, we can establish a global universal approximation result on ℬψ​(ΛTα)\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha}).

###### Proposition 3.11 (Universal approximation theorem on ℬψ​(ΛTα)\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha})).

Let ψ\psi be defined as in ([3.2](https://arxiv.org/html/2512.16396v1#S3.E2 "In 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures")). Then, the linear span of the set

|  |  |  |
| --- | --- | --- |
|  | {𝐗^[0,t]↦⟨eI,𝕏^t⟩:I∈{0,…,d}N,N∈ℕ0}\Bigl\{\widehat{\mathbf{X}}\_{[0,t]}\mapsto\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle:I\in\{0,\ldots,d\}^{N},N\in\mathbb{N}\_{0}\Bigr\} |  |

is dense in ℬψ​(ΛTα)\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha}), i.e., for every map f∈ℬψ​(ΛTα)f\in\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha}) and every ε>0\varepsilon>0 there exists a linear function ℓ:T​((ℝd+1))→ℝ\boldsymbol{\ell}\colon T((\mathbb{R}^{d+1}))\to\mathbb{R} of the form 𝕏^t↦ℓ​(𝕏^t):=∑|I|≤NℓI​⟨eI,𝕏^t⟩\widehat{\mathbb{X}}\_{t}\mapsto\boldsymbol{\ell}(\widehat{\mathbb{X}}\_{t}):=\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle, for some N∈ℕ0N\in\mathbb{N}\_{0} and ℓI∈ℝ\ell\_{I}\in\mathbb{R}, such that

|  |  |  |
| --- | --- | --- |
|  | sup𝐗^[0,t]∈ΛTα|f​(𝐗^[0,t])−ℓ​(𝕏^t)|ψ​(𝐗^[0,t])<ε.\sup\_{\widehat{\mathbf{X}}\_{[0,t]}\in\Lambda\_{T}^{\alpha}}\frac{|f(\widehat{\mathbf{X}}\_{[0,t]})-\boldsymbol{\ell}(\widehat{\mathbb{X}}\_{t})|}{\psi(\widehat{\mathbf{X}}\_{[0,t]})}<\varepsilon. |  |

###### Proof.

First note that, since (ΛTα,ψ)(\Lambda\_{T}^{\alpha},\psi) is a weighted space by Lemma [3.9](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem9 "Lemma 3.9. ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures"), we are able to apply the weighted real-valued Stone–Weierstrass theorem, stated in [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16), Theorem 3.9]. The proof proceeds similarly to the argument used in the proof of [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16), Theorem 5.4], where we need to apply the weighted real-valued Stone–Weierstrass theorem to

|  |  |  |
| --- | --- | --- |
|  | 𝒜:=span⁡{𝐗^[0,t]↦⟨eI,𝕏^t⟩:I∈{0,…,d}N,N∈ℕ0}.\mathcal{A}:=\operatorname{span}\Bigl\{\widehat{\mathbf{X}}\_{[0,t]}\mapsto\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle:I\in\{0,\ldots,d\}^{N},\,N\in\mathbb{N}\_{0}\Bigr\}. |  |

Therefore, we need to prove that 𝒜⊆ℬψ​(ΛTα)\mathcal{A}\subseteq\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha}) is a vector subspace and a subalgebra that is point separating and nowhere vanishing of ψ\psi-moderate growth, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜~\displaystyle\widetilde{\mathcal{A}} | :=span({𝐗^[0,t]↦⟨e∅,𝕏^t⟩}\displaystyle:=\operatorname{span}\Bigl(\Bigl\{\widehat{\mathbf{X}}\_{[0,t]}\mapsto\langle e\_{\emptyset},\widehat{\mathbb{X}}\_{t}\rangle\Bigr\} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.3) |  |  | ∪{𝐗^[0,t]↦⟨(eIe0⊗k)⊗e0,𝕏^t⟩:k∈ℕ0,N∈{0,…,⌊1/α⌋},I∈{0,…,d}N})\displaystyle\qquad\cup\Bigl\{\widehat{\mathbf{X}}\_{[0,t]}\mapsto\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{X}}\_{t}\rangle:\begin{matrix}k\in\mathbb{N}\_{0},\,N\in\{0,\ldots,\lfloor 1/\alpha\rfloor\},\\ I\in\{0,\ldots,d\}^{N}\end{matrix}\Bigr\}\Bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⊆𝒜,\displaystyle\subseteq\mathcal{A}, |  |

is a possible candidate for the point separating and nowhere vanishing vector subspace of ψ\psi-moderate growth.

In order to prove that 𝒜⊆ℬψ​(ΛTα)\mathcal{A}\subseteq\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha}) is a vector subspace, we fix some a∈𝒜a\in\mathcal{A} of the form ΛTα∋𝐗^[0,t]↦a​(𝐗^[0,t]):=⟨eI,𝕏^t⟩∈ℝ\Lambda\_{T}^{\alpha}\ni\widehat{\mathbf{X}}\_{[0,t]}\mapsto a(\widehat{\mathbf{X}}\_{[0,t]}):=\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle\in\mathbb{R}, for some I∈{0,…,d}NI\in\{0,\ldots,d\}^{N} and N∈ℕ0N\in\mathbb{N}\_{0}.

We note that by [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16), Lemma 5.1], it suffices to show the claim for the metric dΛ,∞:=|⋅−⋅|+dc​c,∞;[0,t]d\_{\Lambda,\infty}:=|\ \cdot-\cdot\ |+d\_{cc,\infty;[0,t]}, which is topologically equivalent to dΛ,α′d\_{\Lambda,\alpha^{\prime}} on ΛTα\Lambda\_{T}^{\alpha}. Therefore, recall that by Remark [3.8](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem8 "Remark 3.8. ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures") the topology on (ΛTα,dΛ,∞)(\Lambda\_{T}^{\alpha},d\_{\Lambda,\infty}) coincides with the quotient topology induced by the map

|  |  |  |
| --- | --- | --- |
|  | φ:[0,T]×C^d,Tα→ΛTα,φ​(t,𝐗^)=𝐗^[0,t],\varphi\colon[0,T]\times\widehat{C}\_{d,T}^{\alpha}\to\Lambda\_{T}^{\alpha},\qquad\varphi(t,\widehat{\mathbf{X}})=\widehat{\mathbf{X}}\_{[0,t]}, |  |

where here we equip C^d,Tα\widehat{C}\_{d,T}^{\alpha} with the metric dc​c,∞d\_{cc,\infty}. Then, a map f:ΛTα→ℝf\colon\Lambda\_{T}^{\alpha}\to\mathbb{R} is continuous if and only if the composition f∘φ:[0,T]×C^d,Tα→ℝf\circ\varphi\colon[0,T]\times\widehat{C}\_{d,T}^{\alpha}\to\mathbb{R} is continuous. Thus, it suffices to prove continuity of a¯:=a∘φ\bar{a}:=a\circ\varphi. Therefore, we fix some R>0R>0 and observe that the pre-image KR:=ψ−1​((0,R])K\_{R}:=\psi^{-1}((0,R]) is bounded with respect to dΛ,αd\_{\Lambda,\alpha}.

For (t,𝐗^)∈[0,T]×C^d,Tα(t,\widehat{\mathbf{X}})\in[0,T]\times\widehat{C}\_{d,T}^{\alpha}, we have

|  |  |  |
| --- | --- | --- |
|  | a¯​(t,𝐗^)=a​(φ​(t,𝐗^))=a​(𝐗^[0,t])=⟨eI,𝕏^t⟩.\bar{a}(t,\widehat{\mathbf{X}})=a(\varphi(t,\widehat{\mathbf{X}}))=a(\widehat{\mathbf{X}}\_{[0,t]})=\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle. |  |

Now, let K~R⊂C^d,Tα\widetilde{K}\_{R}\subset\widehat{C}\_{d,T}^{\alpha} be a subset bounded with respect to the α\alpha-Hölder norm ∥⋅∥c​c,α\|\,\cdot\,\|\_{cc,\alpha}. Then, it follows from [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), Corollary 10.40] that the map

|  |  |  |
| --- | --- | --- |
|  | (K~R,dc​c,∞)∋𝐗^↦𝕏^N∈(C0,α​([0,T];GN​(ℝd+1)),dc​c,∞)(\widetilde{K}\_{R},d\_{cc,\infty})\ni\widehat{\mathbf{X}}\quad\mapsto\quad\widehat{\mathbb{X}}^{N}\in(C^{0,\alpha}([0,T];G^{N}(\mathbb{R}^{d+1})),d\_{cc,\infty}) |  |

is continuous on K~R\widetilde{K}\_{R} with respect to dc​c,∞d\_{cc,\infty}. This together with the continuity of the evaluation map

|  |  |  |
| --- | --- | --- |
|  | (C0,α​([0,T];GN​(ℝd+1)),dc​c,∞)∋𝕏^N↦𝕏^tN∈(GN​(ℝd+1),dc​c)(C^{0,\alpha}([0,T];G^{N}(\mathbb{R}^{d+1})),d\_{cc,\infty})\ni\widehat{\mathbb{X}}^{N}\quad\mapsto\quad\widehat{\mathbb{X}}^{N}\_{t}\in(G^{N}(\mathbb{R}^{d+1}),d\_{cc}) |  |

shows that the map

|  |  |  |
| --- | --- | --- |
|  | (K~R,dc​c,∞)∋𝐗^↦𝕏^tN∈(GN​(ℝd+1),dc​c)(\widetilde{K}\_{R},d\_{cc,\infty})\ni\widehat{\mathbf{X}}\quad\mapsto\quad\widehat{\mathbb{X}}^{N}\_{t}\in(G^{N}(\mathbb{R}^{d+1}),d\_{cc}) |  |

is continuous on K~R\widetilde{K}\_{R} with respect to dc​c,∞d\_{cc,\infty}. Then, it also follows that

|  |  |  |
| --- | --- | --- |
|  | ([0,T]×K~R,dprod)∋(t,𝐗^)↦𝕏^tN∈(GN​(ℝd+1),dc​c),([0,T]\times\widetilde{K}\_{R},d\_{\textup{prod}})\ni(t,\widehat{\mathbf{X}})\quad\mapsto\quad\widehat{\mathbb{X}}\_{t}^{N}\in(G^{N}(\mathbb{R}^{d+1}),d\_{cc}), |  |

is continuous on [0,T]×K~R[0,T]\times\widetilde{K}\_{R} with respect to the product metric dprod:=|⋅−⋅|+dc​c,∞d\_{\textup{prod}}:=|\,\cdot-\cdot\,|+d\_{cc,\infty}. Further, since linear functions on the finite dimensional space GN​(ℝd+1)G^{N}(\mathbb{R}^{d+1}) are continuous, it follows that the map

|  |  |  |  |
| --- | --- | --- | --- |
| (3.4) |  | ([0,T]×K~R,dprod)∋(t,𝐗^)↦a¯​(t,𝐗^)=⟨eI,𝕏^t⟩∈ℝ([0,T]\times\widetilde{K}\_{R},d\_{\textup{prod}})\ni(t,\widehat{\mathbf{X}})\quad\mapsto\quad\bar{a}(t,\widehat{\mathbf{X}})=\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle\in\mathbb{R} |  |

is continuous on [0,T]×K~R[0,T]\times\widetilde{K}\_{R} with respect to the product metric dprodd\_{\textup{prod}}. We now choose

|  |  |  |
| --- | --- | --- |
|  | K~R={𝐗^[0,T]t∈C^d,Tα:ψ​(𝐗^[0,t])≤R},\widetilde{K}\_{R}=\{\widehat{\mathbf{X}}^{t}\_{[0,T]}\in\widehat{C}\_{d,T}^{\alpha}:\psi(\widehat{\mathbf{X}}\_{[0,t]})\leq R\}, |  |

which, is bounded with respect to ∥⋅∥c​c,α\|\,\cdot\,\|\_{cc,\alpha}. Then, by construction

|  |  |  |
| --- | --- | --- |
|  | KR=φ​([0,T]×K~R),K\_{R}=\varphi\Bigl([0,T]\times\widetilde{K}\_{R}\Bigr), |  |

and the topology on KRK\_{R} is the quotient topology induced by φR:=φ|[0,T]×K~R\varphi\_{R}:=\varphi|\_{[0,T]\times\widetilde{K}\_{R}}. Since a¯|[0,T]×K~R=a|KR∘φR\bar{a}|\_{[0,T]\times\widetilde{K}\_{R}}=a|\_{K\_{R}}\circ\varphi\_{R}, is continuous, we then obtain that the map

|  |  |  |
| --- | --- | --- |
|  | (KR,dΛ,∞)∋𝐗^[0,t]↦a​(𝐗^[0,t])=⟨eI,𝕏^t⟩∈ℝ(K\_{R},d\_{\Lambda,\infty})\ni\widehat{\mathbf{X}}\_{[0,t]}\quad\mapsto\quad a(\widehat{\mathbf{X}}\_{[0,t]})=\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle\in\mathbb{R} |  |

is continuous on KRK\_{R} with respect to dΛ,∞d\_{\Lambda,\infty}. Since R>0R>0 was chosen arbitrarily, this shows that a|KR∈C​(KR)a|\_{K\_{R}}\in C(K\_{R}), for all R>0R>0.

Moreover, using the ball-box-estimate (see [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), Proposition 7.49]), we have

|  |  |  |
| --- | --- | --- |
|  | ‖g−h‖TN​(ℝd+1)≤C1​max⁡(dc​c​(g,h)​max⁡(1,‖g‖c​cN−1),dc​c​(g,h)N)\|g-h\|\_{T^{N}(\mathbb{R}^{d+1})}\leq C\_{1}\max\left(d\_{cc}(g,h)\max\Bigl(1,\|g\|\_{cc}^{N-1}\right),d\_{cc}(g,h)^{N}\Bigr) |  |

for each g,h∈GN​(ℝd+1)g,h\in G^{N}(\mathbb{R}^{d+1}) and some constant C1≥1C\_{1}\geq 1 and by choosing g=𝕏^0Ng=\widehat{\mathbb{X}}^{N}\_{0} and h=𝕏^tNh=\widehat{\mathbb{X}}^{N}\_{t} we obtain for every 𝐗^[0,t]∈ΛTα\widehat{\mathbf{X}}\_{[0,t]}\in\Lambda\_{T}^{\alpha} that

|  |  |  |
| --- | --- | --- |
|  | |a​(𝐗^[0,t])|=|⟨eI,𝕏^t⟩|≤‖𝕏^tN‖TN​(ℝd+1)≤‖𝕏^tN−𝕏^0N‖TN​(ℝd+1)+1≤C1​(dc​c​(𝕏^tN,𝕏^0N)N+2).|a(\widehat{\mathbf{X}}\_{[0,t]})|=|\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle|\leq\|\widehat{\mathbb{X}}^{N}\_{t}\|\_{T^{N}(\mathbb{R}^{d+1})}\leq\|\widehat{\mathbb{X}}^{N}\_{t}-\widehat{\mathbb{X}}^{N}\_{0}\|\_{T^{N}(\mathbb{R}^{d+1})}+1\leq C\_{1}\Bigl(d\_{cc}(\widehat{\mathbb{X}}^{N}\_{t},\widehat{\mathbb{X}}^{N}\_{0})^{N}+2\Bigr). |  |

Using the inequality dc​c​(𝕏^uN,𝕏^sN)≤CN,α​dc​c​((𝐗^t)u,(𝐗^t)s)d\_{cc}(\widehat{\mathbb{X}}^{N}\_{u},\widehat{\mathbb{X}}^{N}\_{s})\leq C\_{N,\alpha}d\_{cc}((\widehat{\mathbf{X}}^{t})\_{u},(\widehat{\mathbf{X}}^{t})\_{s}) for all 𝐗^[0,t]∈ΛTα\widehat{\mathbf{X}}\_{[0,t]}\in\Lambda\_{T}^{\alpha} and some constant CN,α>0C\_{N,\alpha}>0 (see [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), Theorem 9.5] for the pp-variation case, which carries over to the α\alpha-Hölder setting by [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), p. 182]), we further obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |a​(𝐗^[0,t])|\displaystyle|a(\widehat{\mathbf{X}}\_{[0,t]})| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C1​(dc​c​(𝕏^tN,𝕏^0N)N+2)≤C1​(Tα​N​(supu,s∈[0,T],u<sdc​c​(𝕏^uN,𝕏^sN)|s−u|α)N+2)\displaystyle\quad\leq C\_{1}\Bigl(d\_{cc}(\widehat{\mathbb{X}}^{N}\_{t},\widehat{\mathbb{X}}^{N}\_{0})^{N}+2\Bigr)\leq C\_{1}\Bigl(T^{\alpha N}\Bigl(\sup\_{u,s\in[0,T],\,u<s}\frac{d\_{cc}(\widehat{\mathbb{X}}^{N}\_{u},\widehat{\mathbb{X}}^{N}\_{s})}{|s-u|^{\alpha}}\Bigr)^{N}+2\Bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C1​(CN,αN​Tα​N​(supu,s∈[0,T],u<sdc​c​((𝐗^t)u,(𝐗^t)s)|s−u|α)N+2)\displaystyle\quad\leq C\_{1}\Bigl(C^{N}\_{N,\alpha}T^{\alpha N}\Bigl(\sup\_{u,s\in[0,T],\,u<s}\frac{d\_{cc}((\widehat{\mathbf{X}}^{t})\_{u},(\widehat{\mathbf{X}}^{t})\_{s})}{|s-u|^{\alpha}}\Bigr)^{N}+2\Bigr) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.5) |  |  | =C1​(CN,αN​Tα​N​‖𝐗^[0,T]t‖c​c,αN+2).\displaystyle\quad=C\_{1}\Bigl(C^{N}\_{N,\alpha}T^{\alpha N}\|\widehat{\mathbf{X}}\_{[0,T]}^{t}\|\_{cc,\alpha}^{N}+2\Bigr). |  |

Thus, we conclude that,

|  |  |  |
| --- | --- | --- |
|  | limR→∞sup𝐗^[0,t]∈ΛTα∖KR|a​(𝐗^[0,t])|ψ​(𝐗^[0,t])≤C1​limR→∞sup𝐗^[0,t]∈ΛTα∖KRCN,αN​Tα​N​‖𝐗^[0,T]t‖c​c,αN+2exp⁡(β​‖𝐗^[0,T]t‖c​c,αγ)=0,\lim\_{R\rightarrow\infty}\sup\_{\widehat{\mathbf{X}}\_{[0,t]}\in\Lambda\_{T}^{\alpha}\setminus K\_{R}}\frac{|a(\widehat{\mathbf{X}}\_{[0,t]})|}{\psi(\widehat{\mathbf{X}}\_{[0,t]})}\leq C\_{1}\lim\_{R\rightarrow\infty}\sup\_{\widehat{\mathbf{X}}\_{[0,t]}\in\Lambda\_{T}^{\alpha}\setminus K\_{R}}\frac{C^{N}\_{N,\alpha}T^{\alpha N}\|\widehat{\mathbf{X}}\_{[0,T]}^{t}\|^{N}\_{cc,\alpha}+2}{\exp\Bigl(\beta\|\widehat{\mathbf{X}}\_{[0,T]}^{t}\|\_{cc,\alpha}^{\gamma}\Bigr)}=0, |  |

since the exponential function dominates any polynomial. It follows from Lemma [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16), Lemma 2.7] that a∈ℬψ​(ΛTα)a\in\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha}), which shows that 𝒜⊆ℬψ​(ΛTα)\mathcal{A}\subseteq\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha}).

Moreover, we observe that 𝒜\mathcal{A} is by the shuffle property a subalgebra of ℬψ​(ΛTα)\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha}). In order to show that 𝒜\mathcal{A} is point separating and nowhere vanishing of ψ\psi-moderate growth, we claim that the vector subspace 𝒜~⊆𝒜\widetilde{\mathcal{A}}\subseteq\mathcal{A} defined in ([3.2](https://arxiv.org/html/2512.16396v1#S3.Ex22 "Proof. ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures")) is point separating, nowhere vanishing, and for every a~∈𝒜~\tilde{a}\in\widetilde{\mathcal{A}} there exists some λ>0\lambda>0 such that exp⁡(λ​|a~​(⋅)|)∈ℬψ​(ΛTα)\exp(\lambda|\tilde{a}(\cdot)|)\in\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha}).

For the former, let 𝐘^[0,t],𝐙^[0,t]∈ΛTα\widehat{\mathbf{Y}}\_{[0,t]},\widehat{\mathbf{Z}}\_{[0,t]}\in\Lambda\_{T}^{\alpha} be distinct. By contradiction, let us assume that for every k∈ℕ0k\in\mathbb{N}\_{0}, N∈{0,…,⌊1/α⌋}N\in\{0,\ldots,\lfloor 1/\alpha\rfloor\}, and I∈{0,…,d}NI\in\{0,\ldots,d\}^{N} it holds that

|  |  |  |
| --- | --- | --- |
|  | ⟨(eI​e0⊗k)⊗e0,𝕐^t⟩=⟨(eI​e0⊗k)⊗e0,ℤ^t⟩,\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{Y}}\_{t}\rangle=\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{Z}}\_{t}\rangle, |  |

where we observe, using the shuffle property, that

|  |  |  |  |
| --- | --- | --- | --- |
| (3.6) |  | ⟨(eI​e0⊗k)⊗e0,𝕏^t⟩=∫0t⟨eI​e0⊗k,𝕏^s⟩​ds=∫0t⟨eI,𝕏^s⟩​⟨e0⊗k,𝕏^s⟩​ds=∫0t⟨eI,𝕏^s⟩​skk!​ds,\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{X}}\_{t}\rangle=\int\_{0}^{t}\langle e\_{I}\shuffle e\_{0}^{\otimes k},\widehat{\mathbb{X}}\_{s}\rangle\,\mathrm{d}s=\int\_{0}^{t}\langle e\_{I},\widehat{\mathbb{X}}\_{s}\rangle\langle e\_{0}^{\otimes k},\widehat{\mathbb{X}}\_{s}\rangle\,\mathrm{d}s=\int\_{0}^{t}\langle e\_{I},\widehat{\mathbb{X}}\_{s}\rangle\frac{s^{k}}{k!}\,\mathrm{d}s, |  |

for all 𝐗^[0,t]∈ΛTα\widehat{\mathbf{X}}\_{[0,t]}\in\Lambda\_{T}^{\alpha}. Thus, we conclude for every k∈ℕ0k\in\mathbb{N}\_{0}, N∈{0,…,⌊1/α⌋}N\in\{0,\ldots,\lfloor 1/\alpha\rfloor\}, and I∈{0,…,d}NI\in\{0,\ldots,d\}^{N} that

|  |  |  |
| --- | --- | --- |
|  | ∫0t⟨eI,𝕐^s−ℤ^s⟩​skk!​ds=0.\int\_{0}^{t}\langle e\_{I},\widehat{\mathbb{Y}}\_{s}-\widehat{\mathbb{Z}}\_{s}\rangle\frac{s^{k}}{k!}\,\mathrm{d}s=0. |  |

By [[BB11](https://arxiv.org/html/2512.16396v1#bib.bibx2), Corollary 4.24], we then deduce that

|  |  |  |
| --- | --- | --- |
|  | ⟨eI,𝕐^s⟩=⟨eI,ℤ^s⟩,\langle e\_{I},\widehat{\mathbb{Y}}\_{s}\rangle=\langle e\_{I},\widehat{\mathbb{Z}}\_{s}\rangle, |  |

for all s∈[0,t]s\in[0,t] and all I∈{0,…,d}NI\in\{0,\ldots,d\}^{N}, N∈{0,1,…,⌊1/α⌋}N\in\{0,1,\ldots,\lfloor 1/\alpha\rfloor\}. This contradicts our assumption that 𝐘^[0,t]\widehat{\mathbf{Y}}\_{[0,t]} and 𝐙^[0,t]\widehat{\mathbf{Z}}\_{[0,t]} are distinct, and shows that 𝒜~\widetilde{\mathcal{A}} is point separating.

Further, we observe that 𝒜~\widetilde{\mathcal{A}} vanishes nowhere. Indeed, by using the map

|  |  |  |
| --- | --- | --- |
|  | (𝐗^[0,t]↦a~​(𝐗^[0,t]):=⟨e∅,𝕏^t⟩+⟨(e∅​e0⊗0)⊗e0,𝕏^t⟩)∈𝒜~,\big(\widehat{\mathbf{X}}\_{[0,t]}\mapsto\tilde{a}(\widehat{\mathbf{X}}\_{[0,t]}):=\langle e\_{\emptyset},\widehat{\mathbb{X}}\_{t}\rangle+\langle(e\_{\emptyset}\shuffle e\_{0}^{\otimes 0})\otimes e\_{0},\widehat{\mathbb{X}}\_{t}\rangle\big)\in\widetilde{\mathcal{A}}, |  |

we observe that a~​(𝐗^[0,t])=1+∫0tds=1+t≠0\tilde{a}(\widehat{\mathbf{X}}\_{[0,t]})=1+\int\_{0}^{t}\,\mathrm{d}s=1+t\neq 0, for all 𝐗^[0,t]∈ΛTα\widehat{\mathbf{X}}\_{[0,t]}\in\Lambda\_{T}^{\alpha}.

Now, to show that for every a~∈𝒜~\tilde{a}\in\widetilde{\mathcal{A}} there exists some λ>0\lambda>0 such that exp⁡(λ​|a~​(⋅)|)∈ℬψ​(ΛTα)\exp(\lambda|\tilde{a}(\cdot)|)\in\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha}) we fix some (𝐗^[0,t]↦a~​(𝐗^[0,t])=l​(𝕏^t))∈𝒜~\big(\widehat{\mathbf{X}}\_{[0,t]}\mapsto\tilde{a}(\widehat{\mathbf{X}}\_{[0,t]})=l(\widehat{\mathbb{X}}\_{t})\big)\in\widetilde{\mathcal{A}} with linear function

|  |  |  |
| --- | --- | --- |
|  | l​(𝕏^t)=a∅​⟨e∅,𝕏^t⟩+∑0≤|I|≤N∑k=0KaI,k​⟨(eI​e0⊗k)⊗e0,𝕏^t⟩,l(\widehat{\mathbb{X}}\_{t})=a\_{\emptyset}\langle e\_{\emptyset},\widehat{\mathbb{X}}\_{t}\rangle+\sum\_{0\leq|I|\leq N}\sum\_{k=0}^{K}a\_{I,k}\langle(e\_{I}\shuffle e\_{0}^{\otimes k})\otimes e\_{0},\widehat{\mathbb{X}}\_{t}\rangle, |  |

for some K∈ℕ0K\in\mathbb{N}\_{0} and N∈{0,…,⌊1/α⌋}N\in\{0,\ldots,\lfloor 1/\alpha\rfloor\} and aI,k,a∅∈ℝa\_{I,k},a\_{\emptyset}\in\mathbb{R}. Then, by similar arguments as for ([3.4](https://arxiv.org/html/2512.16396v1#S3.E4 "In Proof. ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures")), we have exp⁡(|λ​a~​(⋅)|)|KR∈C​(KR)\exp(|\lambda\widetilde{a}(\cdot)|)|\_{K\_{R}}\in C(K\_{R}), for all λ,R>0\lambda,R>0. In addition, by the same reasoning as in ([3.2](https://arxiv.org/html/2512.16396v1#S3.Ex35 "Proof. ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures")), together with the explicit form of the elements of 𝒜~\widetilde{\mathcal{A}} in ([3.6](https://arxiv.org/html/2512.16396v1#S3.E6 "In Proof. ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures")), we deduce for all 𝐗^[0,t]∈ΛTα\widehat{\mathbf{X}}\_{[0,t]}\in\Lambda\_{T}^{\alpha} that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |a~​(𝐗^[0,t])|\displaystyle|\tilde{a}(\widehat{\mathbf{X}}\_{[0,t]})| | =|l​(𝕏^t)|≤C1​‖l‖TN+K+1​(ℝd+1)∗​(Tα​(K+1)​N​supu,s∈[0,T],u<s(dc​c​(𝕏^uN,𝕏^sN)|s−u|α)N+1)\displaystyle=|l(\widehat{\mathbb{X}}\_{t})|\leq C\_{1}\|l\|\_{T^{N+K+1}(\mathbb{R}^{d+1})^{\*}}\Bigl(T^{\alpha(K+1)N}\sup\_{u,s\in[0,T],\,u<s}\Bigl(\frac{d\_{cc}(\widehat{\mathbb{X}}^{N}\_{u},\widehat{\mathbb{X}}^{N}\_{s})}{|s-u|^{\alpha}}\Bigr)^{N}+1\Bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C1​‖l‖TN+K+1​(ℝd+1)∗​(CN,αN​Tα​(K+1)​N​(supu,s∈[0,T],u<sdc​c​((𝐗^t)u,(𝐗^t)s)|s−u|α)N+1)\displaystyle\leq C\_{1}\|l\|\_{T^{N+K+1}(\mathbb{R}^{d+1})^{\*}}\Bigl(C^{N}\_{N,\alpha}T^{\alpha(K+1)N}\Bigl(\sup\_{u,s\in[0,T],\,u<s}\frac{d\_{cc}((\widehat{\mathbf{X}}^{t})\_{u},(\widehat{\mathbf{X}}^{t})\_{s})}{|s-u|^{\alpha}}\Bigr)^{N}+1\Bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =C1​‖l‖TN+K+1​(ℝd+1)∗​(CN,αN​Tα​(K+1)​N​‖𝐗^[0,T]t‖c​c,αN+1).\displaystyle=C\_{1}\|l\|\_{T^{N+K+1}(\mathbb{R}^{d+1})^{\*}}\Bigl(C^{N}\_{N,\alpha}T^{\alpha(K+1)N}\|\widehat{\mathbf{X}}^{t}\_{[0,T]}\|\_{cc,\alpha}^{N}+1\Bigr). |  |

Then, for C2:=max⁡(C1​‖l‖TN+K+1​(ℝd+1)∗​CN,αN​Tα​(K+1)​N,C1​‖l‖TN+K+1​(ℝd+1)∗)>0C\_{2}:=\max(C\_{1}\|l\|\_{T^{N+K+1}(\mathbb{R}^{d+1})^{\*}}C^{N}\_{N,\alpha}T^{\alpha(K+1)N},C\_{1}\|l\|\_{T^{N+K+1}(\mathbb{R}^{d+1})^{\*}})>0, we have

|  |  |  |
| --- | --- | --- |
|  | limR→∞sup𝐗^[0,t]∈ΛTα∖KRexp⁡(λ​|a~​(𝐗^[0,t])|)ψ​(𝐗^[0,t])≤limR→∞sup𝐗^[0,t]∈ΛTα∖KRexp⁡(λ​C2​(‖𝐗^[0,T]t‖c​c,αN+1))exp⁡(β​‖𝐗^[0,T]t‖c​c,αγ)=0,\lim\_{R\rightarrow\infty}\sup\_{\widehat{\mathbf{X}}\_{[0,t]}\in\Lambda\_{T}^{\alpha}\setminus K\_{R}}\frac{\exp(\lambda|\tilde{a}(\widehat{\mathbf{X}}\_{[0,t]})|)}{\psi(\widehat{\mathbf{X}}\_{[0,t]})}\leq\lim\_{R\rightarrow\infty}\sup\_{\widehat{\mathbf{X}}\_{[0,t]}\in\Lambda\_{T}^{\alpha}\setminus K\_{R}}\frac{\exp(\lambda C\_{2}(\|\widehat{\mathbf{X}}\_{[0,T]}^{t}\|\_{cc,\alpha}^{N}+1))}{\exp(\beta\|\widehat{\mathbf{X}}\_{[0,T]}^{t}\|\_{cc,\alpha}^{\gamma})}=0, |  |

where the last equality follows by choosing λ<β/C2\lambda<\beta/C\_{2} small enough ensuring that the denominator tends faster to infinity than the nominator (as γ≥⌊1/α⌋≥N\gamma\geq\lfloor 1/\alpha\rfloor\geq N). Hence, by [[CST25](https://arxiv.org/html/2512.16396v1#bib.bibx16), Lemma 2.7] it follows that exp⁡(λ​|a~​(⋅)|)∈ℬψ​(ΛTα)\exp(\lambda|\tilde{a}(\cdot)|)\in\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha}) which holds true for any a~∈𝒜~\tilde{a}\in\widetilde{\mathcal{A}}.

Hence, we can apply the weighted real-valued Stone–Weierstrass theorem to conclude that 𝒜\mathcal{A} is dense in ℬψ​(ΛTα)\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha}).
∎

###### Remark 3.12.

A related universal approximation result on weighted spaces is established in [[CM25](https://arxiv.org/html/2512.16396v1#bib.bibx13), Theorem 2.20]. There, the authors consider the space of (Stratonovich-enhanced) stopped continuous semimartingales together with their associated signatures, rather than the full stopped rough path space studied in Proposition [3.11](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem11 "Proposition 3.11 (Universal approximation theorem on ℬ_𝜓⁢(Λ_𝑇^𝛼)). ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures").

We are now in a position to formulate a global universal approximation theorem in a suitable Lp​(ΛTα)L^{p}(\Lambda\_{T}^{\alpha})-space. For this purpose, we work on the space (ΛTα,ℬ​(ΛTα))(\Lambda\_{T}^{\alpha},\mathcal{B}(\Lambda\_{T}^{\alpha})) equipped with a finite Borel measure ν\nu, where ℬ​(ΛTα)\mathcal{B}(\Lambda\_{T}^{\alpha}) denotes the Borel σ\sigma-algebra on ΛTα\Lambda\_{T}^{\alpha}.

###### Theorem 3.13 (LpL^{p}-universal approximation theorem on ΛTα\Lambda\_{T}^{\alpha}).

Let ψ\psi be defined as in ([3.2](https://arxiv.org/html/2512.16396v1#S3.E2 "In 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures")), p>1p>1, and ∫ΛTαψp​dν<∞\int\_{\Lambda\_{T}^{\alpha}}\psi^{p}\,\mathrm{d}\nu<\infty. Moreover, consider the set

|  |  |  |
| --- | --- | --- |
|  | ℒΛ:={fℓ|fℓ:𝐗^[0,t]↦ℓ(𝕏^t)=∑|I|≤NℓI⟨eI,𝕏^t⟩,ℓI∈ℝ,N∈ℕ0,𝐗^[0,t]∈ΛTα}.\mathcal{L}\_{\Lambda}:=\Bigl\{f\_{\ell}|~f\_{\ell}\colon\widehat{\mathbf{X}}\_{[0,t]}\mapsto\boldsymbol{\ell}(\widehat{\mathbb{X}}\_{t})=\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle,\ell\_{I}\in\mathbb{R},\,N\in\mathbb{N}\_{0},\,\widehat{\mathbf{X}}\_{[0,t]}\in\Lambda\_{T}^{\alpha}\Bigr\}. |  |

Then, for every f∈Lp​(ΛTα)f\in L^{p}(\Lambda\_{T}^{\alpha}) and for every ε>0\varepsilon>0 there exists a functional fℓ∈ℒΛf\_{\ell}\in\mathcal{L}\_{\Lambda} such that

|  |  |  |
| --- | --- | --- |
|  | ‖f−fℓ‖Lp​(ΛTα)<ε.\|f-f\_{\ell}\|\_{L^{p}(\Lambda\_{T}^{\alpha})}<\varepsilon. |  |

###### Proof.

Since ΛTα\Lambda\_{T}^{\alpha} is Polish, see Remark [3.8](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem8 "Remark 3.8. ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures"), Lusin’s theorem and Tietze’s extension theorem apply verbatim as in Theorem [3.4](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem4 "Theorem 3.4 (𝐿^𝑝-universal approximation theorem on 𝐶̂_{𝑑,𝑇}^𝛼). ‣ 3.1. General functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures"), and we obtain that for every f∈Lp​(ΛTα,ν)f\in L^{p}(\Lambda\_{T}^{\alpha},\nu) and every ε>0\varepsilon>0, there exist Kε>0K^{\varepsilon}>0 and a bounded continuous function fε∈Cb​(ΛTα;[−Kε,Kε])f^{\varepsilon}\in C\_{b}(\Lambda\_{T}^{\alpha};[-K^{\varepsilon},K^{\varepsilon}]) with ‖f−fε‖Lp​(ΛTα)<ε/2\|f-f^{\varepsilon}\|\_{L^{p}(\Lambda\_{T}^{\alpha})}<\varepsilon/2.

By definition Cb​(ΛTα)⊆ℬψ​(ΛTα)C\_{b}(\Lambda\_{T}^{\alpha})\subseteq\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha}) and, using Proposition [3.11](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem11 "Proposition 3.11 (Universal approximation theorem on ℬ_𝜓⁢(Λ_𝑇^𝛼)). ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures"), we can approximate fεf^{\varepsilon} in ℬψ​(ΛTα)\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha}) by a linear function on the signature, i.e.

|  |  |  |
| --- | --- | --- |
|  | ‖fε−fℓ‖ℬψ​(ΛTα)p=(sup𝐗^[0,t]∈ΛTα|fε​(𝐗^[0,t])−ℓ​(𝕏^t)|ψ​(𝐗^[0,t]))p<εp2p​M,\|{f}^{\varepsilon}-f\_{\ell}\|^{p}\_{\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha})}=\Bigl(\sup\_{\widehat{\mathbf{X}}\_{[0,t]}\in\Lambda\_{T}^{\alpha}}\frac{|{f}^{\varepsilon}(\widehat{\mathbf{X}}\_{[0,t]})-\boldsymbol{\ell}(\widehat{\mathbb{X}}\_{t})|}{\psi(\widehat{\mathbf{X}}\_{[0,t]})}\Bigr)^{p}<\frac{\varepsilon^{p}}{2^{p}M}, |  |

where M:=∫ΛTαψp​dν<∞M:=\int\_{\Lambda\_{T}^{\alpha}}\psi^{p}\,\mathrm{d}\nu<\infty. As in Proposition [3.11](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem11 "Proposition 3.11 (Universal approximation theorem on ℬ_𝜓⁢(Λ_𝑇^𝛼)). ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures"), this yields an LpL^{p}-approximation of ff by such linear combinations, that is,

|  |  |  |
| --- | --- | --- |
|  | ‖fε−fℓ‖Lp​(ΛTα)p≤∫ΛTαψp​dν​‖fε−fℓ‖ℬψ​(ΛTα)p<(ε2)p,\|{f}^{\varepsilon}-f\_{\ell}\|^{p}\_{L^{p}(\Lambda\_{T}^{\alpha})}\leq\int\_{\Lambda\_{T}^{\alpha}}\psi^{p}\,\mathrm{d}\nu~\|{f}^{\varepsilon}-f\_{\ell}\|^{p}\_{\mathcal{B}\_{\psi}(\Lambda\_{T}^{\alpha})}<\Bigl(\frac{\varepsilon}{2}\Bigr)^{p}, |  |

which proves the claim.
∎

###### Remark 3.14.

In contrast to the classical signature employed in Theorem [3.13](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem13 "Theorem 3.13 (𝐿^𝑝-universal approximation theorem on Λ_𝑇^𝛼). ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures"), the LpL^{p}-universal approximation theorems in [[SA23](https://arxiv.org/html/2512.16396v1#bib.bibx38)] and [[BPS25](https://arxiv.org/html/2512.16396v1#bib.bibx8)] are established using so-called robust signatures, which were introduced in [[CO22](https://arxiv.org/html/2512.16396v1#bib.bibx15)] as a normalized variant of the classical signature. Moreover, the approaches developed in [[SA23](https://arxiv.org/html/2512.16396v1#bib.bibx38)] and [[BPS25](https://arxiv.org/html/2512.16396v1#bib.bibx8)] differ substantially from the proof of Theorem [3.13](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem13 "Theorem 3.13 (𝐿^𝑝-universal approximation theorem on Λ_𝑇^𝛼). ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures").

More specifically, [[SA23](https://arxiv.org/html/2512.16396v1#bib.bibx38)] exploits that linear functionals of the bounded signature form a rich algebra of measurable functions that generates the σ\sigma-algebra of the underlying (subsets of the) classical path space; a monotone class argument then yields L2L^{2}-density of linear signature functionals among all square-integrable measurable random variables. By contrast, [[BPS25](https://arxiv.org/html/2512.16396v1#bib.bibx8)] reduces the approximation of general LpL^{p}-functionals to that of bounded continuous ones and combines suitable weight functions — used to control the tail behavior of the underlying measure on the rough path space — with a Stone–Weierstrass theorem for robust signatures.

## 4. Approximation properties of linear functionals on the Brownian signature

In this section, we demonstrate that the LpL^{p}-universal approximation theorems (Theorem [3.4](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem4 "Theorem 3.4 (𝐿^𝑝-universal approximation theorem on 𝐶̂_{𝑑,𝑇}^𝛼). ‣ 3.1. General functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures") and Theorem [3.13](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem13 "Theorem 3.13 (𝐿^𝑝-universal approximation theorem on Λ_𝑇^𝛼). ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures")) apply to the (time-extended) Brownian motions, allowing to approximate fairly general stochastic processes, like solutions to stochastic differential equations, by linear combinations of the random signatures of (time-extended) Brownian motions. To that end, the central step is to show that the exponential moment condition, required in Theorem [3.4](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem4 "Theorem 3.4 (𝐿^𝑝-universal approximation theorem on 𝐶̂_{𝑑,𝑇}^𝛼). ‣ 3.1. General functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures") and Theorem [3.13](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem13 "Theorem 3.13 (𝐿^𝑝-universal approximation theorem on Λ_𝑇^𝛼). ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures"), is satisfied for the Wiener measure, which determines the law of a Brownian motion. For related approximation result for stochastic processes using the robust signature, we refer to [[SA23](https://arxiv.org/html/2512.16396v1#bib.bibx38), [BPS25](https://arxiv.org/html/2512.16396v1#bib.bibx8)].

Throughout the present section, let W=(Wt)t∈[0,T]W=(W\_{t})\_{t\in[0,T]} be a dd-dimensional Brownian motion, defined on a probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}), with a filtration (ℱt)t∈[0,T](\mathcal{F}\_{t})\_{t\in[0,T]} satisfying the usual conditions, i.e., completeness and right-continuity. For an introduction to stochastic processes and stochastic calculus, we refer, e.g., to the classical textbook [[KS91](https://arxiv.org/html/2512.16396v1#bib.bibx32)].

Recall that, for a Brownian motion WW, there is a canonical choice for a random geometric rough path lift 𝐖\mathbf{W} of WW given by

|  |  |  |
| --- | --- | --- |
|  | 𝐖t:=(1,Wt,∫0tWs⊗∘dWs),t∈[0,T],\mathbf{W}\_{t}:=\bigg(1,W\_{t},\int\_{0}^{t}W\_{s}\otimes\circ\,\mathrm{d}W\_{s}\bigg),\quad t\in[0,T], |  |

where the stochastic integral ∫0tWs⊗∘dWs\int\_{0}^{t}W\_{s}\otimes\circ\,\mathrm{d}W\_{s} is defined as a classical Stratonovich integral. Note that 𝐖t\mathbf{W}\_{t} takes values in G2​(ℝd)G^{2}(\mathbb{R}^{d}) for all t∈[0,T]t\in[0,T], see e.g. [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), Exercise 13.10], and the Stratonovich-enhanced Brownian rough path 𝐖\mathbf{W} is, almost surely, a geometric α\alpha-Hölder rough path for α∈(13,12)\alpha\in(\frac{1}{3},\frac{1}{2}). In the following, we denote the time-extended Stratonovich-enhanced Brownian rough path by 𝐖^\widehat{\mathbf{W}} and 𝕎^\widehat{\mathbb{W}} its associated signature, which, by definition of the signature of a geometric rough path, corresponds to the unique Lyons’ lift of 𝐖^\widehat{\mathbf{W}} and coincides with iterated Stratonovich integrals, see [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), Exercise 17.2]. We call 𝐖^\widehat{\mathbf{W}} and 𝕎^\widehat{\mathbb{W}} the (time-extended) Brownian rough path and the (time-extended) Brownian signature, respectively.

Furthermore, we introduce the filtration ℱt𝐖:=σ​({𝐖s:s≤t},𝒩)\mathcal{F}\_{t}^{\mathbf{W}}:=\sigma(\{\mathbf{W}\_{s}:s\leq t\},\mathcal{N}) for t∈[0,T]t\in[0,T] and 𝒩\mathcal{N} containing all ℙ\mathbb{P}-null sets, i.e., the natural augmented filtration generated by 𝐖\mathbf{W}. We denote by ℋp\mathcal{H}^{p} the space of (ℱt𝐖)(\mathcal{F}^{\mathbf{W}}\_{t})-progressively measurable processes AA such that

|  |  |  |
| --- | --- | --- |
|  | ‖A‖ℋpp:=𝔼​[∫0T|At|p​dt]<∞.\|A\|\_{\mathcal{H}^{p}}^{p}:=\mathbb{E}\Bigl[\int\_{0}^{T}|A\_{t}|^{p}\,\mathrm{d}t\Bigr]<\infty. |  |

###### Remark 4.1.

Note that ℱt𝐖=σ({𝐖s:s≤t},𝒩)=σ({Ws:s≤t},𝒩)=:ℱtW\mathcal{F}\_{t}^{\mathbf{W}}=\sigma(\{\mathbf{W}\_{s}:s\leq t\},\mathcal{N})=\sigma(\{W\_{s}:s\leq t\},\mathcal{N})=:\mathcal{F}\_{t}^{W} for t∈[0,T]t\in[0,T], that is, the natural augmented filtration generated by 𝐖\mathbf{W} and by WW coincide, see e.g. the proof of [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), Proposition 13.11].

In Section [3](https://arxiv.org/html/2512.16396v1#S3 "3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures") we introduced the notion of a stopped rough path in general, see Definition [3.6](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem6 "Definition 3.6. ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures"). We now specialise this construction to the time-extended Brownian rough path and present an explicit description of its coordinates.

###### Example 4.2.

By Definition [3.6](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem6 "Definition 3.6. ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures") the stopped Brownian rough path 𝐖^[0,T]t\widehat{\mathbf{W}}^{t}\_{[0,T]} is given by (𝐖^t)s:=𝐖^s(\widehat{\mathbf{W}}^{t})\_{s}:=\widehat{\mathbf{W}}\_{s} for all s∈[0,t]s\in[0,t] and for all r∈[t,T]r\in[t,T] we have

|  |  |  |
| --- | --- | --- |
|  | ⟨eI,(𝐖^t)r⟩={r,for ​I=(0)12​r2,for ​I=(0,0)⟨eI,𝐖^t⟩,for ​I=(i)​ or ​I=(j,i),i∈{1,…,d},j∈{0,…,d}r⋅⟨ei,𝐖^t⟩−⟨e(0,i),𝐖^t⟩,for ​I=(i,0),i∈{1,…,d},\langle e\_{I},(\widehat{\mathbf{W}}^{t})\_{r}\rangle=\begin{cases}r,&\text{for }I=(0)\\[10.0pt] \frac{1}{2}r^{2},&\text{for }I=(0,0)\\[10.0pt] \langle e\_{I},\widehat{\mathbf{W}}\_{t}\rangle,&\text{for }I=(i)\text{ or }I=(j,i),i\in\{1,\ldots,d\},\\ &j\in\{0,\ldots,d\}\\[10.0pt] r\cdot\langle e\_{i},\widehat{\mathbf{W}}\_{t}\rangle-\langle e\_{(0,i)},\widehat{\mathbf{W}}\_{t}\rangle,&\text{for }I=(i,0),i\in\{1,\ldots,d\},\end{cases} |  |

where the last line follows by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨e(i,0),(𝐖^t)r⟩\displaystyle\langle e\_{(i,0)},(\widehat{\mathbf{W}}^{t})\_{r}\rangle | =∫0r⟨ei,𝐖^st⟩​ds\displaystyle=\int\_{0}^{r}\langle e\_{i},\widehat{\mathbf{W}}^{t}\_{s}\rangle\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0t⟨ei,𝐖^st⟩​ds+∫tr⟨ei,𝐖^t⟩​ds\displaystyle=\int\_{0}^{t}\langle e\_{i},\widehat{\mathbf{W}}^{t}\_{s}\rangle\,\mathrm{d}s+\int\_{t}^{r}\langle e\_{i},\widehat{\mathbf{W}}\_{t}\rangle\,\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨e(i,0),𝐖^t⟩+(r−t)​⟨ei,𝐖^t⟩\displaystyle=\langle e\_{(i,0)},\widehat{\mathbf{W}}\_{t}\rangle+(r-t)\langle e\_{i},\widehat{\mathbf{W}}\_{t}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨e(i,0),𝐖^t⟩+r​⟨ei,𝐖^t⟩−⟨e0,𝐖^t⟩​⟨ei,𝐖^t⟩\displaystyle=\langle e\_{(i,0)},\widehat{\mathbf{W}}\_{t}\rangle+r\langle e\_{i},\widehat{\mathbf{W}}\_{t}\rangle-\langle e\_{0},\widehat{\mathbf{W}}\_{t}\rangle\langle e\_{i},\widehat{\mathbf{W}}\_{t}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨e(i,0),𝐖^t⟩+r​⟨ei,𝐖^t⟩−⟨e0​ei,𝐖^t⟩\displaystyle=\langle e\_{(i,0)},\widehat{\mathbf{W}}\_{t}\rangle+r\langle e\_{i},\widehat{\mathbf{W}}\_{t}\rangle-\langle e\_{0}\shuffle e\_{i},\widehat{\mathbf{W}}\_{t}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =⟨e(i,0),𝐖^t⟩+r​⟨ei,𝐖^t⟩−⟨e(0,i),𝐖^t⟩−⟨e(i,0),𝐖^t⟩\displaystyle=\langle e\_{(i,0)},\widehat{\mathbf{W}}\_{t}\rangle+r\langle e\_{i},\widehat{\mathbf{W}}\_{t}\rangle-\langle e\_{(0,i)},\widehat{\mathbf{W}}\_{t}\rangle-\langle e\_{(i,0)},\widehat{\mathbf{W}}\_{t}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =r​⟨ei,𝐖^t⟩−⟨e(0,i),𝐖^t⟩.\displaystyle=r\langle e\_{i},\widehat{\mathbf{W}}\_{t}\rangle-\langle e\_{(0,i)},\widehat{\mathbf{W}}\_{t}\rangle. |  |

### 4.1. Universal approximation with Brownian signatures

In this subsection, we establish that any functional f​(𝐖^)∈Lp​(Ω,ℙ)f(\widehat{\mathbf{W}})\in L^{p}(\Omega,\mathbb{P}), as well as any stochastic process f​(𝐖^[0,⋅])∈ℋpf(\widehat{\mathbf{W}}\_{[0,\cdot]})\in\mathcal{H}^{p}, can be approximated by linear functionals acting on the (time-extended) Brownian signature.

###### Corollary 4.3.

Let α∈(1/3,1/3)\alpha\in(1/3,1/3), let WW be a Brownian motion, W^=(⋅,W)\widehat{W}=(\cdot,W) be the time-extended Brownian motion and 𝐖^\widehat{\mathbf{W}} be the corresponding time-extended Brownian rough path.

1. (i)

   Let f​(𝐖^)∈Lp​(Ω;ℙ)f(\widehat{\mathbf{W}})\in L^{p}(\Omega;\mathbb{P}) with f:C^d,Tα→ℝf\colon\widehat{C}\_{d,T}^{\alpha}\to\mathbb{R}. Then, for every ε>0\varepsilon>0 there exists a linear function ℓ:T​((ℝd+1))→ℝ\boldsymbol{\ell}\colon T((\mathbb{R}^{d+1}))\to\mathbb{R} of the form 𝕎^T↦ℓ​(𝕎^T):=∑|I|≤NℓI​⟨eI,𝕎^T⟩\widehat{\mathbb{W}}\_{T}\mapsto\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{T}):=\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{W}}\_{T}\rangle, for some N∈ℕ0N\in\mathbb{N}\_{0} and ℓI∈ℝ\ell\_{I}\in\mathbb{R}, such that

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​[|f​(𝐖^)−ℓ​(𝕎^T)|p]<ε.\mathbb{E}[|f(\widehat{\mathbf{W}})-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{T})|^{p}]<\varepsilon. |  |
2. (ii)

   Let f​(𝐖^[0,⋅])∈ℋpf(\widehat{\mathbf{W}}\_{[0,\cdot]})\in\mathcal{H}^{p} with f:ΛTα→ℝf\colon\Lambda\_{T}^{\alpha}\to\mathbb{R}. Then, for every ε>0\varepsilon>0 there exists a linear function ℓ:T​((ℝd+1))→ℝ\boldsymbol{\ell}\colon T((\mathbb{R}^{d+1}))\to\mathbb{R} of the form 𝕎^t↦ℓ​(𝕎^t):=∑|I|≤NℓI​⟨eI,𝕏^t⟩\widehat{\mathbb{W}}\_{t}\mapsto\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t}):=\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{X}}\_{t}\rangle, for some N∈ℕ0N\in\mathbb{N}\_{0} and ℓI∈ℝ\ell\_{I}\in\mathbb{R}, such that

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​[∫0T|f​(𝐖^[0,t])−ℓ​(𝕎^t)|p​dt]<ε.\mathbb{E}\Bigl[\int\_{0}^{T}|f(\widehat{\mathbf{W}}\_{[0,t]})-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})|^{p}\,\mathrm{d}t\Bigr]<\varepsilon. |  |

###### Proof.

*(i):* As discussed in [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), Appendix A.1], the Brownian rough path 𝐖^\widehat{\mathbf{W}} can be seen as a C0,α​([0,T];G2​(ℝd+1))C^{0,\alpha}([0,T];G^{2}(\mathbb{R}^{d+1}))-valued random variable and its law μ𝐖^\mu\_{\widehat{\mathbf{W}}} is a Borel probability measure on C0,α​([0,T];G2​(ℝd+1))C^{0,\alpha}([0,T];G^{2}(\mathbb{R}^{d+1})), see also [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), p. 358]. Thus, when working on the space C^d,Tα\widehat{C}\_{d,T}^{\alpha} of time-extended geometric rough paths, we take ν:=μ𝐖^\nu:=\mu\_{\widehat{\mathbf{W}}}. Then, we observe that since f​(𝐖^)∈Lp​(Ω;ℙ)f(\widehat{\mathbf{W}})\in L^{p}(\Omega;\mathbb{P}), we have that

|  |  |  |
| --- | --- | --- |
|  | ∫C^d,Tα|f|p​dμ𝐖^=𝔼​[|f​(𝐖^)|p]<∞,\displaystyle\int\_{\widehat{C}\_{d,T}^{\alpha}}|f|^{p}\,\mathrm{d}\mu\_{\widehat{\mathbf{W}}}=\mathbb{E}[|f(\widehat{\mathbf{W}})|^{p}]<\infty, |  |

that is, f∈Lp​(C^d,Tα;μ𝐖^)f\in L^{p}(\widehat{C}\_{d,T}^{\alpha};\mu\_{\widehat{\mathbf{W}}}).

In order to apply Theorem [3.4](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem4 "Theorem 3.4 (𝐿^𝑝-universal approximation theorem on 𝐶̂_{𝑑,𝑇}^𝛼). ‣ 3.1. General functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures"), we have to verify that the time-extended Brownian rough path 𝐖^\widehat{\mathbf{W}} satisfies the exponential moment condition given by ∫C^d,Tαψp​dν<∞\int\_{\widehat{C}\_{d,T}^{\alpha}}\psi^{p}\,\mathrm{d}\nu<\infty, with ψ​(𝐖^)=exp⁡(β​p​‖𝐖^‖c​c,αγ)\psi(\widehat{\mathbf{W}})=\exp(\beta p\|\widehat{\mathbf{W}}\|\_{cc,\alpha}^{\gamma}) for γ≥⌊1/α⌋\gamma\geq\lfloor 1/\alpha\rfloor, β>0\beta>0, and α∈(1/3,1/2)\alpha\in(1/3,1/2).

To that end, we define the α\alpha-Hölder rough path norm

|  |  |  |
| --- | --- | --- |
|  | ‖|𝐗^|‖α:=‖X^‖α+‖𝕏^(2)‖2​α=sup0≤s<t≤T|X^s,t||t−s|α+sup0≤s<t≤T|𝕏^s,t(2)||t−s|2​α,{|\kern-1.07639pt|\kern-1.07639pt|\widehat{\mathbf{X}}|\kern-1.07639pt|\kern-1.07639pt|}\_{\alpha}:=\|\widehat{X}\|\_{\alpha}+\sqrt{\|\widehat{\mathbb{X}}^{(2)}\|\_{2\alpha}}=\sup\_{0\leq s<t\leq T}\frac{|\widehat{X}\_{s,t}|}{|t-s|^{\alpha}}+\sqrt{\sup\_{0\leq s<t\leq T}\frac{|\widehat{\mathbb{X}}^{(2)}\_{s,t}|}{|t-s|^{2\alpha}}}, |  |

for 𝐗^∈C0α​([0,T];G2​(ℝd+1))\widehat{\mathbf{X}}\in C\_{0}^{\alpha}([0,T];G^{2}(\mathbb{R}^{d+1})) and α∈(13,12)\alpha\in(\frac{1}{3},\frac{1}{2}). Note that this norm is equivalent to the norm ‖𝐗^‖c​c,α\|\widehat{\mathbf{X}}\|\_{cc,\alpha} on G2​(ℝd+1)G^{2}(\mathbb{R}^{d+1}) (with constant C>0C>0), see [[FH20](https://arxiv.org/html/2512.16396v1#bib.bibx19), p.22].

Then, the fact that ‖|𝐖^|‖α{|\kern-1.07639pt|\kern-1.07639pt|\widehat{\mathbf{W}}|\kern-1.07639pt|\kern-1.07639pt|}\_{\alpha} has Gaussian tails, as shown in [[FH20](https://arxiv.org/html/2512.16396v1#bib.bibx19), Propositions 3.4 and 3.5], together with the Gaussian integrability criterion in [[FV10](https://arxiv.org/html/2512.16396v1#bib.bibx23), Lemma A.17], ensures the existence of a constant η>0\eta>0 such that exponential moments are finite for γ=2\gamma=2, i.e.,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[exp⁡(η∣‖𝐖^‖|α2)]<∞.\mathbb{E}\Bigl[\exp\Bigl(\eta{|\kern-1.07639pt|\kern-1.07639pt|\widehat{\mathbf{W}}|\kern-1.07639pt|\kern-1.07639pt|}\_{\alpha}^{2}\Bigr)\Bigr]<\infty. |  |

Hence, we obtain

|  |  |  |
| --- | --- | --- |
|  | ∫C^d,Tαψp​dμ𝐖^=𝔼​[exp⁡(β​p​‖𝐖^‖c​c,αγ)]≤𝔼​[exp⁡(β​p​Cγ∣‖𝐖^‖|αγ)]<∞,\int\_{\widehat{C}\_{d,T}^{\alpha}}\psi^{p}\,\mathrm{d}\mu\_{\widehat{\mathbf{W}}}=\mathbb{E}\Bigl[\exp\Bigl(\beta p\|\widehat{\mathbf{W}}\|\_{cc,\alpha}^{\gamma}\Bigr)\Bigr]\leq\mathbb{E}\Bigl[\exp\Bigl(\beta p\,C^{\gamma}{|\kern-1.07639pt|\kern-1.07639pt|\widehat{\mathbf{W}}|\kern-1.07639pt|\kern-1.07639pt|}\_{\alpha}^{\gamma}\Bigr)\Bigr]<\infty, |  |

for γ=2\gamma=2 and β∈(0,ηCγ​p]\beta\in(0,\frac{\eta}{C^{\gamma}p}]; see also [[FH20](https://arxiv.org/html/2512.16396v1#bib.bibx19), Theorem 11.9].

Therefore, Theorem [3.4](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem4 "Theorem 3.4 (𝐿^𝑝-universal approximation theorem on 𝐶̂_{𝑑,𝑇}^𝛼). ‣ 3.1. General functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures") yields that for every ε>0\varepsilon>0 there exists a functional fℓ∈ℒf\_{\ell}\in\mathcal{L} such that

|  |  |  |
| --- | --- | --- |
|  | ‖f−fℓ‖Lp​(C^d,Tα)<ε.\|f-f\_{\ell}\|\_{L^{p}(\widehat{C}\_{d,T}^{\alpha})}<\varepsilon. |  |

In particular, this implies that, for every ε>0\varepsilon>0 there exists a linear function ℓ\boldsymbol{\ell} on the Brownian signature, such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|f​(𝐖^)−ℓ​(𝕎^T)|p]=∫C^d,Tα|f​(𝐖^)−fℓ​(𝐖^)|p​dμ𝐖^=‖f−fℓ‖Lp​(C^d,Tα)<ε.\mathbb{E}[|f(\widehat{\mathbf{W}})-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{T})|^{p}]=\int\_{\widehat{C}\_{d,T}^{\alpha}}|f(\widehat{\mathbf{W}})-f\_{\ell}(\widehat{\mathbf{W}})|^{p}\,\mathrm{d}\mu\_{\widehat{\mathbf{W}}}=\|f-f\_{\ell}\|\_{L^{p}(\widehat{C}\_{d,T}^{\alpha})}<\varepsilon. |  |

*(ii):* On the space (ΛTα,ℬ​(ΛTα))(\Lambda\_{T}^{\alpha},\mathcal{B}(\Lambda\_{T}^{\alpha})), we let ν\nu be the push-forward measure of d​t⊗d​μ𝐖^\,\mathrm{d}t\otimes\,\mathrm{d}\mu\_{\widehat{\mathbf{W}}} under the surjective map

|  |  |  |
| --- | --- | --- |
|  | φ:[0,T]×C^d,Tα→ΛTα,(t,𝐖^)↦𝐖^[0,t],\varphi\colon[0,T]\times\widehat{C}\_{d,T}^{\alpha}\to\Lambda\_{T}^{\alpha},\quad(t,\widehat{\mathbf{W}})\mapsto\widehat{\mathbf{W}}\_{[0,t]}, |  |

that is, ν:=(d​t⊗d​μ𝐖^)∘φ−1\nu:=(\,\mathrm{d}t\otimes\,\mathrm{d}\mu\_{\widehat{\mathbf{W}}})\circ\varphi^{-1}.

We first show that f​(𝐖^[0,⋅])∈Lp​(ΛTα)f(\widehat{\mathbf{W}}\_{[0,\cdot]})\in L^{p}(\Lambda\_{T}^{\alpha}). By a change of measure result, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖f‖Lp​(ΛTα)\displaystyle\|f\|\_{L^{p}(\Lambda\_{T}^{\alpha})} | =∫ΛTα|f|p​dν\displaystyle=\int\_{\Lambda\_{T}^{\alpha}}|f|^{p}\,\mathrm{d}\nu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫C^d,Tα∫0T|(f∘φ)​(t,𝐖^)|p​dt​dμ𝐖^\displaystyle=\int\_{\widehat{C}\_{d,T}^{\alpha}}\int\_{0}^{T}|(f\circ\varphi)(t,\widehat{\mathbf{W}})|^{p}\,\mathrm{d}t\,\mathrm{d}\mu\_{\widehat{\mathbf{W}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0T|f​(𝐖^[0,t])|p​dt]<∞,\displaystyle=\mathbb{E}\Bigl[\int\_{0}^{T}|f(\widehat{\mathbf{W}}\_{[0,t]})|^{p}\,\mathrm{d}t\Bigr]<\infty, |  |

since f​(𝐖^[0,⋅])∈ℋpf(\widehat{\mathbf{W}}\_{[0,\cdot]})\in\mathcal{H}^{p} by assumption. Next, we verify the exponential moment condition as required in Theorem [3.13](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem13 "Theorem 3.13 (𝐿^𝑝-universal approximation theorem on Λ_𝑇^𝛼). ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures"). By a change of measure result, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΛTαψp​dν\displaystyle\int\_{\Lambda\_{T}^{\alpha}}\psi^{p}\,\mathrm{d}\nu | =∫C^d,Tα∫0T((ψ∘φ)​(t,𝐖^))p​dt​dμ𝐖^\displaystyle=\int\_{\widehat{C}\_{d,T}^{\alpha}}\int\_{0}^{T}((\psi\circ\varphi)(t,\widehat{\mathbf{W}}))^{p}\,\mathrm{d}t\,\mathrm{d}\mu\_{\widehat{\mathbf{W}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0Tψ​(𝐖^[0,t])p​dt]\displaystyle=\mathbb{E}\Bigl[\int\_{0}^{T}\psi(\widehat{\mathbf{W}}\_{[0,t]})^{p}\,\mathrm{d}t\Bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0Texp⁡(β​p​‖𝐖^[0,T]t‖c​c,αγ)​dt]\displaystyle=\mathbb{E}\Bigl[\int\_{0}^{T}\exp\Bigl(\beta p\|\widehat{\mathbf{W}}^{t}\_{[0,T]}\|\_{cc,\alpha}^{\gamma}\Bigr)\,\mathrm{d}t\Bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤T​𝔼​[supt∈[0,T]exp⁡(β​p​‖𝐖^[0,T]t‖c​c,αγ)]\displaystyle\leq T\mathbb{E}\Bigl[\sup\_{t\in[0,T]}\exp\Bigl(\beta p\|\widehat{\mathbf{W}}^{t}\_{[0,T]}\|\_{cc,\alpha}^{\gamma}\Bigr)\Bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =T​𝔼​[exp⁡(β​p​‖𝐖^[0,T]‖c​c,αγ)]\displaystyle=T\mathbb{E}\Bigl[\exp\Bigl(\beta p\|\widehat{\mathbf{W}}\_{[0,T]}\|\_{cc,\alpha}^{\gamma}\Bigr)\Bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤T​𝔼​[exp⁡(β​p​Cγ∣‖𝐖^‖|αγ)]<∞,\displaystyle\leq T\mathbb{E}\Bigl[\exp\Bigl(\beta p\,C^{\gamma}{|\kern-1.07639pt|\kern-1.07639pt|\widehat{\mathbf{W}}|\kern-1.07639pt|\kern-1.07639pt|}\_{\alpha}^{\gamma}\Bigr)\Bigr]<\infty, |  |

for γ=2\gamma=2 and β∈(0,ηCγ​p]\beta\in(0,\frac{\eta}{C^{\gamma}p}], where we used that

|  |  |  |
| --- | --- | --- |
|  | supt∈[0,T]‖𝐖^[0,T]t‖c​c,α=‖𝐖^[0,T]‖c​c,α.\sup\_{t\in[0,T]}\|\widehat{\mathbf{W}}^{t}\_{[0,T]}\|\_{cc,\alpha}=\|\widehat{\mathbf{W}}\_{[0,T]}\|\_{cc,\alpha}. |  |

Therefore, by Theorem [3.13](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem13 "Theorem 3.13 (𝐿^𝑝-universal approximation theorem on Λ_𝑇^𝛼). ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures") for every ε>0\varepsilon>0 there exists a functional fℓ∈ℒΛf\_{\ell}\in\mathcal{L}\_{\Lambda} such that

|  |  |  |
| --- | --- | --- |
|  | ‖f−fℓ‖Lp​(ΛTα)<ε.\|f-f\_{\ell}\|\_{L^{p}(\Lambda\_{T}^{\alpha})}<\varepsilon. |  |

Consequently, for every ε>0\varepsilon>0 there exists a linear function ℓ\boldsymbol{\ell} on the Brownian signature, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T|f​(𝐖^[0,t])−ℓ​(𝕎^t)|p​dt]\displaystyle\mathbb{E}\Bigl[\int\_{0}^{T}|f(\widehat{\mathbf{W}}\_{[0,t]})-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})|^{p}\,\mathrm{d}t\Bigr] | =∫C^d,Tα∫0T|(f∘φ−fℓ∘φ)​(t,𝐖^)|p​dt​dμ𝐖^\displaystyle=\int\_{\widehat{C}\_{d,T}^{\alpha}}\int\_{0}^{T}|(f\circ\varphi-f\_{\ell}\circ\varphi)(t,\widehat{\mathbf{W}})|^{p}\,\mathrm{d}t\,\mathrm{d}\mu\_{\widehat{\mathbf{W}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫ΛTα|f−fℓ|p​dν\displaystyle=\int\_{\Lambda\_{T}^{\alpha}}|f-f\_{\ell}|^{p}\,\mathrm{d}\nu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =‖f−fℓ‖Lp​(ΛTα)<ε,\displaystyle=\|f-f\_{\ell}\|\_{L^{p}(\Lambda\_{T}^{\alpha})}<\varepsilon, |  |

where again we used a change of measure result. This concludes the proof.
∎

### 4.2. Approximation of stochastic differential equations

In this subsection, we show that solutions to stochastic differential equations (SDEs) driven by Brownian motions can be approximated by linear combinations of time-extended Brownian signatures.

###### Proposition 4.4.

Let 2≤p<∞2\leq p<\infty. Consider the stochastic differential equation

|  |  |  |  |
| --- | --- | --- | --- |
| (4.1) |  | Yt=y0+∫0tμ​(s,Ys)​ds+∫0tσ​(s,Ys)​dWs,t∈[0,T],Y\_{t}=y\_{0}+\int\_{0}^{t}\mu(s,Y\_{s})\,\mathrm{d}s+\int\_{0}^{t}\sigma(s,Y\_{s})\,\mathrm{d}W\_{s},\quad t\in[0,T], |  |

where y0∈ℝmy\_{0}\in\mathbb{R}^{m}, μ:[0,T]×ℝm→ℝm\mu\colon[0,T]\times\mathbb{R}^{m}\to\mathbb{R}^{m} and σ:[0,T]×ℝm→ℝm×d\sigma\colon[0,T]\times\mathbb{R}^{m}\to\mathbb{R}^{m\times d} are continuous functions, and ∫0tσ​(s,Ys)​dWs\int\_{0}^{t}\sigma(s,Y\_{s})\,\mathrm{d}W\_{s} is defined as an Itô integral. Suppose there exists a unique (strong) solution YY to the SDE ([4.1](https://arxiv.org/html/2512.16396v1#S4.E1 "In Proposition 4.4. ‣ 4.2. Approximation of stochastic differential equations ‣ 4. Approximation properties of linear functionals on the Brownian signature ‣ Global universal approximation with Brownian signatures")) and that μ,σ\mu,\sigma satisfy the linear growth condition

|  |  |  |
| --- | --- | --- |
|  | |μ​(t,x)|+|σ​(t,x)|≤C​(1+|x|),x∈ℝm,|\mu(t,x)|+|\sigma(t,x)|\leq C(1+|x|),\quad x\in\mathbb{R}^{m}, |  |

for some constant C>0C>0.

Then, for every ε>0\varepsilon>0 there exists a linear function ℓ:T​((ℝd+1))→ℝ\boldsymbol{\ell}\colon T((\mathbb{R}^{d+1}))\to\mathbb{R} of the form 𝕎^t↦ℓ​(𝕎^t):=∑|I|≤NℓI​⟨eI,𝕎^t⟩\widehat{\mathbb{W}}\_{t}\mapsto\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t}):=\sum\_{|I|\leq N}\ell\_{I}\langle e\_{I},\widehat{\mathbb{W}}\_{t}\rangle, for some N∈ℕ0N\in\mathbb{N}\_{0} and ℓI∈ℝ\ell\_{I}\in\mathbb{R}, such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|Yt−ℓ​(𝕎^t)|p​dt]<ε.\mathbb{E}\Bigl[\int\_{0}^{T}|Y\_{t}-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})|^{p}\,\mathrm{d}t\Bigr]<\varepsilon. |  |

###### Proof.

Step 1. It is well-known that SDEs with coefficients satisfying a linear growth condition admit solutions that are uniformly bounded in Lp​(Ω,ℙ)L^{p}(\Omega,\mathbb{P}), i.e.,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supt∈[0,T]|Yt|p]<∞,\mathbb{E}\Bigl[\sup\_{t\in[0,T]}|Y\_{t}|^{p}\Bigr]<\infty, |  |

see, for instance, the argument in [[Klo92](https://arxiv.org/html/2512.16396v1#bib.bibx29), Theorem 4.5.3].

Following a similar construction as in the proof of [[HS12](https://arxiv.org/html/2512.16396v1#bib.bibx26), Proposition 1.1], for every compact set K⊂[0,T]×ℝmK\subset[0,T]\times\mathbb{R}^{m} and ε>0\varepsilon>0, there exist smooth functions με\mu^{\varepsilon} and σε\sigma^{\varepsilon} with compact support such that

|  |  |  |
| --- | --- | --- |
|  | sup(t,y)∈[0,T]×ℝm|με​(t,y)−μ​(t,y)|+sup(t,y)∈[0,T]×ℝm|σε​(t,y)−σ​(t,y)|≤ε,\sup\_{(t,y)\in[0,T]\times\mathbb{R}^{m}}|\mu^{\varepsilon}(t,y)-\mu(t,y)|\,+\sup\_{(t,y)\in[0,T]\times\mathbb{R}^{m}}|\sigma^{\varepsilon}(t,y)-\sigma(t,y)|\leq\varepsilon, |  |

|  |  |  |
| --- | --- | --- |
|  | |με​(t,y)|+|σε​(t,y)|≤C​(2+|y|),t∈[0,T],y∈ℝm,|\mu^{\varepsilon}(t,y)|+|\sigma^{\varepsilon}(t,y)|\leq C(2+|y|),\quad t\in[0,T],y\in\mathbb{R}^{m}, |  |

where the constant CC is as given in the assumptions of this proposition. Consider the approximating SDE

|  |  |  |
| --- | --- | --- |
|  | Ytε=y0+∫0tμε​(s,Ysε)​ds+∫0tσε​(s,Ysε)​dWs,t∈[0,T].Y\_{t}^{\varepsilon}=y\_{0}+\int\_{0}^{t}\mu^{\varepsilon}(s,Y\_{s}^{\varepsilon})\,\,\mathrm{d}s+\int\_{0}^{t}\sigma^{\varepsilon}(s,Y\_{s}^{\varepsilon})\,\,\mathrm{d}W\_{s},\qquad t\in[0,T]. |  |

By [[KN88](https://arxiv.org/html/2512.16396v1#bib.bibx30), Theorem A], the process (Ytε)t∈[0,T](Y\_{t}^{\varepsilon})\_{t\in[0,T]} admits a unique strong solution, and we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supt∈[0,T]|Ytε−Yt|p]≤ε2p​T.\mathbb{E}\Bigl[\sup\_{t\in[0,T]}|Y\_{t}^{\varepsilon}-Y\_{t}|^{p}\Bigr]\leq\frac{\varepsilon}{2^{p}T}. |  |

Using the uniform LpL^{p}-boundedness of YY, we deduce

|  |  |  |  |
| --- | --- | --- | --- |
| (4.2) |  | 𝔼​[supt∈[0,T]|Ytε|p]≤2p−1​(𝔼​[supt∈[0,T]|Ytε−Yt|p]+𝔼​[supt∈[0,T]|Yt|p])<∞.\mathbb{E}\Bigl[\sup\_{t\in[0,T]}|Y\_{t}^{\varepsilon}|^{p}\Bigr]\leq 2^{p-1}\Bigl(\mathbb{E}\Bigl[\sup\_{t\in[0,T]}|Y\_{t}^{\varepsilon}-Y\_{t}|^{p}\Bigr]+\mathbb{E}\Bigl[\sup\_{t\in[0,T]}|Y\_{t}|^{p}\Bigr]\Bigr)<\infty. |  |

Step 2. We next rewrite YtεY\_{t}^{\varepsilon} as the solution of a Stratonovich SDE. Using the usual Itô–Stratonovich correction, we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Ytε\displaystyle\,\mathrm{d}Y\_{t}^{\varepsilon} | =με​(t,Ytε)​d​t+σε​(t,Ytε)​d​Wt\displaystyle=\mu^{\varepsilon}(t,Y\_{t}^{\varepsilon})\,\mathrm{d}t+\sigma^{\varepsilon}(t,Y\_{t}^{\varepsilon})\,\mathrm{d}W\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(με​(t,Ytε)−12​σε​(t,Ytε)​∂σε∂y​(t,Ytε))​d​t+σε​(t,Ytε)∘d​Wt\displaystyle=(\mu^{\varepsilon}(t,Y\_{t}^{\varepsilon})-\frac{1}{2}\sigma^{\varepsilon}(t,Y\_{t}^{\varepsilon})\frac{\partial\sigma^{\varepsilon}}{\partial y}(t,Y\_{t}^{\varepsilon}))\,\mathrm{d}t+\sigma^{\varepsilon}(t,Y\_{t}^{\varepsilon})\circ\,\mathrm{d}W\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =μ~ε​(t,Ytε)​d​t+σε​(t,Ytε)∘d​Wt,\displaystyle=\tilde{\mu}^{\varepsilon}(t,Y\_{t}^{\varepsilon})\,\mathrm{d}t+\sigma^{\varepsilon}(t,Y\_{t}^{\varepsilon})\circ\,\mathrm{d}W\_{t}, |  |

where ∘\circ denotes Stratonovich integration and μ~ε\tilde{\mu}^{\varepsilon} is a modification of με\mu^{\varepsilon} by the additional drift term. Introducing the time-extended Brownian motion W^t=(t,Wt)\widehat{W}\_{t}=(t,W\_{t}), we may rewrite the SDE in the compact Stratonovich form

|  |  |  |  |
| --- | --- | --- | --- |
| (4.3) |  | d​Ytε=σ^ε​(t,Ytε)∘d​W^t,\mathrm{d}Y^{\varepsilon}\_{t}=\widehat{\sigma}^{\varepsilon}(t,Y^{\varepsilon}\_{t})\circ\,\mathrm{d}\widehat{W}\_{t}, |  |

where σ^ε\widehat{\sigma}^{\varepsilon} now also contains the drift term μ~ε\tilde{\mu}^{\varepsilon}, i.e., σ^ε:[0,T]×ℝm→ℝm×(d+1)\widehat{\sigma}^{\varepsilon}\colon[0,T]\times\mathbb{R}^{m}\to\mathbb{R}^{m\times(d+1)} with

|  |  |  |
| --- | --- | --- |
|  | σ^ε=(μ~1εσ11ε⋯σ1​dεμ~2εσ21ε⋯σ2​dε⋮⋮⋱⋮μ~mεσm​1ε⋯σm​dε).\widehat{\sigma}^{\varepsilon}=\begin{pmatrix}\tilde{\mu}^{\varepsilon}\_{1}&\sigma^{\varepsilon}\_{11}&\cdots&\sigma^{\varepsilon}\_{1d}\\ \tilde{\mu}^{\varepsilon}\_{2}&\sigma^{\varepsilon}\_{21}&\cdots&\sigma^{\varepsilon}\_{2d}\\ \vdots&\vdots&\ddots&\vdots\\ \tilde{\mu}^{\varepsilon}\_{m}&\sigma^{\varepsilon}\_{m1}&\cdots&\sigma^{\varepsilon}\_{md}\end{pmatrix}. |  |

By construction we have σ^ε∈Cb3​([0,T]×ℝm;ℒ​(ℝd+1,ℝm))\widehat{\sigma}^{\varepsilon}\in C\_{b}^{3}([0,T]\times\mathbb{R}^{m};\mathcal{L}(\mathbb{R}^{d+1},\mathbb{R}^{m})). Hence, by [[FH20](https://arxiv.org/html/2512.16396v1#bib.bibx19), Theorem 8.3], the associated rough differential equation (RDE), given by

|  |  |  |  |
| --- | --- | --- | --- |
| (4.4) |  | d​Ytε=σ^ε​(t,Ytε)​d​𝐖^t,\mathrm{d}Y\_{t}^{\varepsilon}=\widehat{\sigma}^{\varepsilon}(t,Y\_{t}^{\varepsilon})\,\mathrm{d}\widehat{\mathbf{W}}\_{t}, |  |

driven by the time-extended Brownian rough path 𝐖^\widehat{\mathbf{W}}, is well-posed and admits a unique global solution.

Moreover, by [[FH20](https://arxiv.org/html/2512.16396v1#bib.bibx19), Theorem 9.1], ([4.3](https://arxiv.org/html/2512.16396v1#S4.E3 "In Proof. ‣ 4.2. Approximation of stochastic differential equations ‣ 4. Approximation properties of linear functionals on the Brownian signature ‣ Global universal approximation with Brownian signatures")) can be solved pathwise almost surely as a RDE solution (Ytε​(ω),σ^ε​(t,Ytε​(ω)))∈𝒟W​(ω)2​α(Y\_{t}^{\varepsilon}(\omega),\widehat{\sigma}^{\varepsilon}(t,Y\_{t}^{\varepsilon}(\omega)))\in\mathcal{D}^{2\alpha}\_{W(\omega)} of ([4.4](https://arxiv.org/html/2512.16396v1#S4.E4 "In Proof. ‣ 4.2. Approximation of stochastic differential equations ‣ 4. Approximation properties of linear functionals on the Brownian signature ‣ Global universal approximation with Brownian signatures")).

Step 3. Let Φ:ΛTα→ℝm\Phi\colon\Lambda\_{T}^{\alpha}\to\mathbb{R}^{m} denote the solution map to ([4.4](https://arxiv.org/html/2512.16396v1#S4.E4 "In Proof. ‣ 4.2. Approximation of stochastic differential equations ‣ 4. Approximation properties of linear functionals on the Brownian signature ‣ Global universal approximation with Brownian signatures")), i.e. Φ​(𝐖^[0,t])=Ytε.\Phi(\widehat{\mathbf{W}}\_{[0,t]})=Y\_{t}^{\varepsilon}. Then,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΛTα|Φ|p​dν\displaystyle\int\_{\Lambda\_{T}^{\alpha}}|\Phi|^{p}\,\mathrm{d}\nu | =∫C^d,Tα∫0T|(Φ∘φ)​(t,𝐖^)|p​dt​dμ𝐖^\displaystyle=\int\_{\widehat{C}\_{d,T}^{\alpha}}\int\_{0}^{T}|(\Phi\circ\varphi)(t,\widehat{\mathbf{W}})|^{p}\,\mathrm{d}t\,\mathrm{d}\mu\_{\widehat{\mathbf{W}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0T|Φ​(𝐖^[0,t])|p​dt]\displaystyle=\mathbb{E}\Bigl[\int\_{0}^{T}|\Phi(\widehat{\mathbf{W}}\_{[0,t]})|^{p}\,\mathrm{d}t\Bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[∫0T|Ytε|p​dt]\displaystyle=\mathbb{E}\Bigl[\int\_{0}^{T}|Y\_{t}^{\varepsilon}|^{p}\,\mathrm{d}t\Bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤T​𝔼​[supt∈[0,T]|Ytε|p]<∞,\displaystyle\leq T\mathbb{E}\Bigl[\sup\_{t\in[0,T]}|Y\_{t}^{\varepsilon}|^{p}\Bigr]<\infty, |  |

where we used a change of measure result and ([4.2](https://arxiv.org/html/2512.16396v1#S4.E2 "In Proof. ‣ 4.2. Approximation of stochastic differential equations ‣ 4. Approximation properties of linear functionals on the Brownian signature ‣ Global universal approximation with Brownian signatures")). Thus, Φ∈Lp​(ΛTα)\Phi\in L^{p}(\Lambda\_{T}^{\alpha}) and we may apply Theorem [3.13](https://arxiv.org/html/2512.16396v1#S3.Thmtheorem13 "Theorem 3.13 (𝐿^𝑝-universal approximation theorem on Λ_𝑇^𝛼). ‣ 3.2. Non-anticipative functionals ‣ 3. Global approximation with rough path signatures ‣ Global universal approximation with Brownian signatures"). Therefore, for every ε>0\varepsilon>0 there exists a functional fℓ∈ℒΛf\_{\ell}\in\mathcal{L}\_{\Lambda}, such that

|  |  |  |
| --- | --- | --- |
|  | ‖Φ−fℓ‖Lp​(ΛTα)<ε2p.\|\Phi-f\_{\ell}\|\_{L^{p}(\Lambda\_{T}^{\alpha})}<\frac{\varepsilon}{2^{p}}. |  |

This yields that there exists a linear function ℓ\boldsymbol{\ell} on the Brownian signature, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T|Ytε−ℓ​(𝕎^t)|p​dt]\displaystyle\mathbb{E}\Bigl[\int\_{0}^{T}|Y\_{t}^{\varepsilon}-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})|^{p}\,\mathrm{d}t\Bigr] | =𝔼​[∫0T|Φ​(𝐖^[0,t])−fℓ​(𝐖^[0,t])|p​dt]\displaystyle=\mathbb{E}\Bigl[\int\_{0}^{T}|\Phi(\widehat{\mathbf{W}}\_{[0,t]})-f\_{\ell}(\widehat{\mathbf{W}}\_{[0,t]})|^{p}\,\mathrm{d}t\Bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫C^d,Tα∫0T|(Φ∘φ−fℓ∘φ)​(t,𝐖^)|p​dt​dμ𝐖^\displaystyle=\int\_{\widehat{C}\_{d,T}^{\alpha}}\int\_{0}^{T}|(\Phi\circ\varphi-f\_{\ell}\circ\varphi)(t,\widehat{\mathbf{W}})|^{p}\,\mathrm{d}t\,\mathrm{d}\mu\_{\widehat{\mathbf{W}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫ΛTα|Φ−fℓ|p​dν\displaystyle=\int\_{\Lambda\_{T}^{\alpha}}|\Phi-f\_{\ell}|^{p}\,\mathrm{d}\nu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =‖Φ−fℓ‖Lp​(ΛTα)<ε2p,\displaystyle=\|\Phi-f\_{\ell}\|\_{L^{p}(\Lambda\_{T}^{\alpha})}<\frac{\varepsilon}{2^{p}}, |  |

where we used a change of measure result. Finally, combining steps 11-33 and using the triangle inequality, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|Yt−ℓ​(𝕎^t)|p​dt]\displaystyle\mathbb{E}\Bigl[\int\_{0}^{T}|Y\_{t}-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})|^{p}\,\mathrm{d}t\Bigr] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2p−1​(𝔼​[∫0T|Yt−Ytε|p​dt]+𝔼​[∫0T|Ytε−ℓ​(𝕎^t)|p​dt])\displaystyle\leq 2^{p-1}\Bigl(\mathbb{E}\Bigl[\int\_{0}^{T}|Y\_{t}-Y\_{t}^{\varepsilon}|^{p}\,\mathrm{d}t\Bigr]+\mathbb{E}\Bigl[\int\_{0}^{T}|Y\_{t}^{\varepsilon}-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})|^{p}\,\mathrm{d}t\Bigr]\Bigr) |  |
|  |  |  |
| --- | --- | --- |
|  | ≤2p−1​(T​𝔼​[supt∈[0,T]|Yt−Ytε|p]+𝔼​[∫0T|Ytε−ℓ​(𝕎^t)|p​dt])\displaystyle\leq 2^{p-1}\Bigl(T\mathbb{E}\Bigl[\sup\_{t\in[0,T]}|Y\_{t}-Y\_{t}^{\varepsilon}|^{p}\Bigr]+\mathbb{E}\Bigl[\int\_{0}^{T}|Y\_{t}^{\varepsilon}-\boldsymbol{\ell}(\widehat{\mathbb{W}}\_{t})|^{p}\,\mathrm{d}t\Bigr]\Bigr) |  |
|  |  |  |
| --- | --- | --- |
|  | <T​ε2​T+ε2\displaystyle<T\frac{\varepsilon}{2T}+\frac{\varepsilon}{2} |  |
|  |  |  |
| --- | --- | --- |
|  | <ε,\displaystyle<\varepsilon, |  |

which yields the desired result.
∎

###### Remark 4.5.

Proposition [4.4](https://arxiv.org/html/2512.16396v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.2. Approximation of stochastic differential equations ‣ 4. Approximation properties of linear functionals on the Brownian signature ‣ Global universal approximation with Brownian signatures") can alternatively be proved by a direct application of Corollary [4.3](https://arxiv.org/html/2512.16396v1#S4.Thmtheorem3 "Corollary 4.3. ‣ 4.1. Universal approximation with Brownian signatures ‣ 4. Approximation properties of linear functionals on the Brownian signature ‣ Global universal approximation with Brownian signatures") *(ii)*. Indeed, on the canonical Wiener space, any (ℱtW)(\mathcal{F}\_{t}^{W})-progressively measurable process Y∈ℋpY\in\mathcal{H}^{p} (in particular, strong solutions of Itô SDEs under standard assumptions on the coefficients) can be written in the form

|  |  |  |
| --- | --- | --- |
|  | Yt=f​(W^[0,t]),t∈[0,T],Y\_{t}=f\big(\widehat{W}\_{[0,t]}\big),\quad t\in[0,T], |  |

for some non-anticipative functional ff, where W^t=(t,Wt)\widehat{W}\_{t}=(t,W\_{t}) denotes the time-extended Brownian motion, cf. [[KS91](https://arxiv.org/html/2512.16396v1#bib.bibx32), Chapter 5.3.D]. If 𝐖^\widehat{\mathbf{W}} is the time-extended Stratonovich-enhanced Brownian rough path and π1\pi\_{1} its first-level projection, then W^[0,t]=π1​(𝐖^[0,t])\widehat{W}\_{[0,t]}=\pi\_{1}(\widehat{\mathbf{W}}\_{[0,t]}), and thus

|  |  |  |
| --- | --- | --- |
|  | Yt=f(W^[0,t])=f(π1(𝐖^[0,t]))=:Φ(𝐖^[0,t]).Y\_{t}=f(\widehat{W}\_{[0,t]})=f(\pi\_{1}(\widehat{\mathbf{W}}\_{[0,t]}))=:\Phi(\widehat{\mathbf{W}}\_{[0,t]}). |  |

Hence, YY fits into the setting of Corollary [4.3](https://arxiv.org/html/2512.16396v1#S4.Thmtheorem3 "Corollary 4.3. ‣ 4.1. Universal approximation with Brownian signatures ‣ 4. Approximation properties of linear functionals on the Brownian signature ‣ Global universal approximation with Brownian signatures") *(ii)*, which then yields an ℋp\mathcal{H}^{p}-approximation of YY by linear functionals on the time-extended Brownian signature.

We note, however, that making the representation Yt=f​(W^[0,t])Y\_{t}=f(\widehat{W}\_{[0,t]}) fully rigorous requires a careful measurability analysis for progressively measurable processes with respect to the topology induced by the rough path type distance used on ΛTα\Lambda\_{T}^{\alpha}; cf. [[BBH+25](https://arxiv.org/html/2512.16396v1#bib.bibx3), Section 4.2]. For this reason, we have opted for the proof of Proposition [4.4](https://arxiv.org/html/2512.16396v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.2. Approximation of stochastic differential equations ‣ 4. Approximation properties of linear functionals on the Brownian signature ‣ Global universal approximation with Brownian signatures") based on classical results from the theory of stochastic differential equations and rough paths.

###### Remark 4.6.

Recently, so-called signature-based models have been introduced in mathematical finance in [[CGSF23](https://arxiv.org/html/2512.16396v1#bib.bibx11), [CGMSF25](https://arxiv.org/html/2512.16396v1#bib.bibx10)]; see also [[ASS21](https://arxiv.org/html/2512.16396v1#bib.bibx1)]. These models offer several favorable features compared to classical approaches, which are typically based on stochastic differential equations, for describing financial markets. More precisely, signature models represent the underlying dynamics as linear functionals acting on the random signature of a driving noise process, with the time-extended Brownian motion being the most commonly used example. Proposition [4.4](https://arxiv.org/html/2512.16396v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.2. Approximation of stochastic differential equations ‣ 4. Approximation properties of linear functionals on the Brownian signature ‣ Global universal approximation with Brownian signatures") demonstrates the universality of Brownian signature models: they are capable of approximating solutions to a broad class of stochastic differential equations, independently of the specific drift and diffusion structures.

## References

* [ASS21]

  Imanol Perez Arribas, Cristopher Salvi, and Lukasz Szpruch, *Sig-SDEs
  model for quantitative finance*, Proceedings of the First ACM International
  Conference on AI in Finance (New York, NY, USA), ICAIF ’20, Association for
  Computing Machinery, 2021.
* [BB11]

  Haim Brezis and Haim Brézis, *Functional analysis, sobolev spaces and
  partial differential equations*, vol. 2, Springer, 2011.
* [BBH+25]

  Peter Bank, Christian Bayer, Paul P. Hager, Sebastian Riedel, and Tobias Nauen,
  *Stochastic control with signatures*, SIAM J. Control Optim. 63
  (2025), no. 5, 3189–3218.
* [BdRHO25]

  Christian Bayer, Goncalo dos Reis, Blanka Horvath, and Harald Oberhauser,
  *Signature Methods in Finance*, first ed., Springer Finance,
  Springer Cham, 2025.
* [BFZ24]

  Erhan Bayraktar, Qi Feng, and Zhaoyu Zhang, *Deep signature algorithm for
  multidimensional path-dependent options*, SIAM J. Financial Math. 15
  (2024), no. 1, 194–214.
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
* [CGMSF25]

  Christa Cuchiero, Guido Gazzani, Janka Möller, and Sara Svaluto-Ferro,
  *Joint calibration to SPX and VIX options with signature-based
  models*, Math. Finance 35 (2025), no. 1, 161–213.
* [CGSF23]

  Christa Cuchiero, Guido Gazzani, and Sara Svaluto-Ferro, *Signature-based
  models: Theory and calibration*, SIAM Journal on Financial Mathematics
  14 (2023), no. 3, 910–957.
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
* [CST25]

  Christa Cuchiero, Philipp Schmocker, and Josef Teichmann, *Global
  universal approximation of functional input maps on weighted spaces*, arXiv
  preprint arXiv:2306.03303v5 (2025).
* [DMP03]

  Zdzisław Denkowski, Stanislaw Migórski, and Nikolas Papageorgiou, *An
  introduction to nonlinear analysis: Theory*, SpringerLink Bücher, Boston,
  MA, 2003.
* [Dup19]

  Bruno Dupire, *Functional Itô calculus*, Quant. Finance 19
  (2019), no. 5, 721–729.
* [FH20]

  Peter K. Friz and Martin Hairer, *A course on rough paths: with an
  introduction to regularity structures*, second edition ed., Universitext,
  Cham, Switzerland, 2020.
* [Fol99]

  Gerald B. Folland, *Real analysis: modern techniques and their
  applications*, 2. ed. ed., A Wiley-Interscience publication, New York
  Weinheim, 1999.
* [Fri82]

  Avner Friedman, *Foundations of modern analysis*, Courier Corporation,
  1982.
* [FV06]

  Peter Friz and Nicolas Victoir, *A note on the notion of geometric rough
  paths*, Probab. Theory Related Fields 136 (2006), no. 3, 395–416.
* [FV10]

  Peter K. Friz and Nicolas B. Victoir, *Multidimensional stochastic
  processes as rough paths: theory and applications*, Cambridge studies in
  advanced mathematics; 120, Cambridge, 2010.
* [Gra13]

  Benjamin Graham, *Sparse arrays of signatures for online character
  recognition*, ArXiv Preprint arXiv:1308.0371 (2013).
* [HL10]

  Ben Hambly and Terry Lyons, *Uniqueness for the signature of a path of
  bounded variation and the reduced path group*, Ann. of Math. (2) 171
  (2010), no. 1, 109–167.
* [HS12]

  Martina Hofmanová and Jan Seidler, *On weak solutions of stochastic
  differential equations*, Stoch. Anal. Appl. 30 (2012), no. 1,
  100–121.
* [KBPA+19]

  Patrick Kidger, Patric Bonnier, Imanol Perez Arribas, Cristopher Salvi, and
  Terry Lyons, *Deep signature transforms*, 33rd Conference on Neural
  Information Processing Systems (NeurIPS 2019), 32 (2019).
* [KLA20]

  Jasdeep Kalsi, Terry Lyons, and Imanol Perez Arribas, *Optimal execution
  with rough path signatures*, SIAM J. Financial Math. 11 (2020),
  no. 2, 470–493.
* [Klo92]

  Peter E. Kloeden, *Numerical solution of stochastic differential
  equations*, Applications of Mathematics, Stochastic Modelling and Applied
  Probability; 23, Berlin, Heidelberg, 1992.
* [KN88]

  H. Kaneko and S. Nakao, *A note on approximation for stochastic
  differential equations*, Séminaire de Probabilités, XXII, Lecture
  Notes in Math., vol. 1321, Springer, Berlin, 1988, pp. 155–162.
* [KO19]

  Franz J. Király and Harald Oberhauser, *Kernels for sequentially
  ordered data*, J. Mach. Learn. Res. 20 (2019), Paper No. 31, 45.
* [KS91]

  Ioannis Karatzas and Steven E. Shreve, *Brownian motion and stochastic
  calculus*, second ed., Graduate Texts in Mathematics, vol. 113,
  Springer-Verlag, New York, 1991.
* [LCL07]

  Terry J. Lyons, Michael Caruana, and Thierry Lévy, *Differential
  equations driven by rough paths*, Lecture Notes in Mathematics, vol. 1908,
  Springer, Berlin, 2007, Lectures from the 34th Summer School on Probability
  Theory held in Saint-Flour, July 6–24, 2004, With an introduction concerning
  the Summer School by Jean Picard.
* [LLN13]

  Daniel Levin, Terry Lyons, and Hao Ni, *Learning from the past, predicting
  the statistics for the future, learning an evolving system*, ArXiv Preprint
  arXiv:1309.0260 (2013).
* [LNPA19]

  Terry Lyons, Sina Nejad, and Imanol Perez Arribas, *Numerical method for
  model-free pricing of exotic derivatives in discrete time using rough path
  signatures*, Appl. Math. Finance 26 (2019), no. 6, 583–597.
* [LNPA20]

  by same author, *Non-parametric pricing and hedging of exotic derivatives*, Appl.
  Math. Finance 27 (2020), no. 6, 457–494.
* [ML25]

  Andrew McLeod and Terry Lyons, *Signature methods in machine learning*,
  EMS Surv. Math. Sci., 2025.
* [SA23]

  A. Schell and R. Alaifari, *Nonparametric Regression of Stochastic
  Processes via Signatures*, ETH Zurich, Research Report No. 2023-45
  (2023).