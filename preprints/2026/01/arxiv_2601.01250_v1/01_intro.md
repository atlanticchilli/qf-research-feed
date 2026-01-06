---
authors:
- Miryana Grigorova
- James Wheeldon
doc_id: arxiv:2601.01250v1
family_id: arxiv:2601.01250
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'European Options in Market Models with Multiple Defaults: the BSDE approach'
url_abs: http://arxiv.org/abs/2601.01250v1
url_html: https://arxiv.org/html/2601.01250v1
venue: arXiv q-fin
version: 1
year: 2026
---


Miryana Grigorova
Corresponding Author, Email: miryana.grigorova@warwick.ac.uk, Department of Statistics, University of Warwick
  
James Wheeldon
Email: james.wheeldon@warwick.ac.uk, Department of Statistics, University of Warwick
  
Acknowledgements: We thank Marie-Claire Quenez for helpful discussions.

(January 3, 2026)

###### Abstract

We study non-linear Backward Stochastic Differential Equations (BSDEs) driven by a Brownian motion and pp default martingales. The driver of the BSDE with multiple default jumps can take a generalized form involving an optional finite variation process. We first show existence and uniqueness. We then establish comparison and strict comparison results for these BSDEs, under a suitable assumption on the driver. In the case of a linear driver, we derive an explicit formula for the first component of the BSDE using an adjoint exponential semimartingale. The representation depends on whether the finite variation process is predictable or only optional. We apply our results to the problem of pricing and hedging a European option in a linear complete market with two defaultable assets and in a non-linear complete market with pp defaultable assets. Two examples of the latter market model are provided: an example where the seller of the option is a large investor influencing the probability of default of a single asset and an example where the large seller’s strategy affects the default probabilities of all pp assets.

Keywords: BSDEs with Multiple Default Jumps, Generalized Driver, Comparison Theorem, European Option, Non-linear Market, Optional Dividend Process.

## 1 Introduction

In this paper, we consider BSDEs with multiple default jumps and explore some applications in a financial context. BSDEs were first introduced by Bismut [[4](https://arxiv.org/html/2601.01250v1#bib.bib4)], who studied the linear case in relation to stochastic control. Pardoux and Peng [[19](https://arxiv.org/html/2601.01250v1#bib.bib19)] established the well-posedness of non-linear BSDEs with Lipschitz drivers in a Brownian filtration.

BSDEs incorporating both continuous and jump components have also been studied in the literature (cf., e.g., [[21](https://arxiv.org/html/2601.01250v1#bib.bib21)], [[20](https://arxiv.org/html/2601.01250v1#bib.bib20)], [[1](https://arxiv.org/html/2601.01250v1#bib.bib1)], [[7](https://arxiv.org/html/2601.01250v1#bib.bib7)], [[18](https://arxiv.org/html/2601.01250v1#bib.bib18)]). In [[7](https://arxiv.org/html/2601.01250v1#bib.bib7)], BSDEs with a single default jump are studied and applied in a financial context (for developments in the incomplete single default framework, we refer to [[14](https://arxiv.org/html/2601.01250v1#bib.bib14), [15](https://arxiv.org/html/2601.01250v1#bib.bib15)]).

In the present paper, we consider BSDEs driven by a Brownian motion and pp compensated default martingales, each associated with a default time τi>0\tau\_{i}>0 and an intensity process λi=(λti)t∈[0,T]\lambda^{i}=(\lambda\_{t}^{i})\_{t\in[0,T]} for i∈{1,…,p}i\in\{1,\ldots,p\}. We develop new *a priori* estimates and establish the existence and uniqueness of the solution to the BSDE with multiple default jumps.

We consider an optional (not necessarily predictable), right-continuous left-limited (rcll) process DD of finite variation which enters into the driver of the BSDE, leading to a generalized form of the driver: g​(t,y,z,k1,…,kp)​d​t+d​Dtg(t,y,z,k^{1},\ldots,k^{p})dt+dD\_{t}. This modeling choice is motivated by the fact that, in markets with defaultable securities, contingent claims often give rise to intermediate cash flows, particularly at the time of default, as observed in [[2](https://arxiv.org/html/2601.01250v1#bib.bib2)].

We extend the definition of λ\lambda-linear drivers introduced in [[7](https://arxiv.org/html/2601.01250v1#bib.bib7)] to the general case of λ(p)\lambda^{(p)}-linear drivers, where λ(p)\lambda^{(p)} refers to the vector of pp intensity processes λ1,…,λp\lambda^{1},\ldots,\lambda^{p}. When the driver gg is λ(p)\lambda^{(p)}-linear, we derive an explicit representation of the solution to the BSDE with multiple default jumps using an associated adjoint semimartingale. This representation depends on whether the process DD is predictable or only optional. We also prove a comparison result and a strict comparison result under suitable assumptions on the driver, where we distinguish again the case where DD is predictable and the case where DD is only optional.

We present two financial applications of this model: one in which the market is linear and complete, and another in which the market is complete but non-linear. In both cases, we assume the existence of a risk-free asset, a default-free (jump-free) risky asset, and two or more defaultable assets. We focus on pricing and hedging a European contingent claim with terminal payoff η\eta at maturity T>0T>0, and with intermediate ‘dividends’ modeled by the process DD, where DD represents an exogenous cumulative process. The process DD is not necessarily predictable. In the second example, the market is non-linear, with the non-linearity arising from imperfections caused by a large seller whose strategy influences default probabilities.

In the non-linear market setting with pp defaults, we show that the price of the contingent claim is X⋅,Tg​(η,D)X\_{\cdot,T}^{g}(\eta,D), where X⋅,Tg​(η,D)X\_{\cdot,T}^{g}(\eta,D) denotes the solution to the non-linear BSDE with multiple default jumps, terminal time TT, terminal condition η\eta, and generalized driver of the form g​(t,y,z,k1,…,kp)​d​t+d​Dtg(t,y,z,k^{1},\ldots,k^{p})dt+dD\_{t}. This gives rise to a non-linear pricing system 𝐗g:(η,D)↦X⋅,Tg​(η,D)\mathbf{X}^{g}:(\eta,D)\mapsto X\_{\cdot,T}^{g}(\eta,D), whose properties we study. When DD is fixed, we define the associated (g,D)(g,D)-conditional evaluation by ℰ⋅,Tg,D​(η)≔X⋅,Tg​(η,D)\mathscr{E}\_{\cdot,T}^{g,D}(\eta)\coloneqq X\_{\cdot,T}^{g}(\eta,D) for η∈L2​(𝒢T),\eta\in L^{2}(\mathcal{G}\_{T}), and provide its main properties.

The remainder of the paper is organized as follows:
  
Section [2](https://arxiv.org/html/2601.01250v1#S2 "2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") is dedicated to the study of the BSDE with pp default jumps and generalized driver.
In Subsection [2.1](https://arxiv.org/html/2601.01250v1#S2.SS1 "2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), we define the BSDE with pp default jumps and generalized λ(p)\lambda^{(p)}-driver (allowing for an intermediate optional finite variational process DD); in Subsection [2.2](https://arxiv.org/html/2601.01250v1#S2.SS2 "2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), we prove existence and uniqueness, and study the case where the generalized λ(p)\lambda^{(p)}-driver is linear; in Subsection [2.3](https://arxiv.org/html/2601.01250v1#S2.SS3 "2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), we establish comparison and strict comparison results under suitable assumptions on the driver. Section [3](https://arxiv.org/html/2601.01250v1#S3 "3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") is dedicated to the applications to pricing and hedging a European option in complete linear and non-linear markets. In Subsection [3.1](https://arxiv.org/html/2601.01250v1#S3.SS1 "3.1 Pricing in a Linear Financial Market with two Defaultable Risky Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), we present an example of a linear and complete market; in Subsection [3.2](https://arxiv.org/html/2601.01250v1#S3.SS2 "3.2 Pricing in a Non-linear Complete Market with 𝑝 Defaultable Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), we present the non-linear  complete market with pp defaults, and study properties of the associated non-linear pricing system for a European option; in Subsection [3.3](https://arxiv.org/html/2601.01250v1#S3.SS3 "3.3 Example: Large Seller who Affects the 𝑖-th Default Probability ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), we provide a particular case of a non-linear complete market where a large seller influences the probability of default of one (defaultable) risky asset and, in Subsection [3.4](https://arxiv.org/html/2601.01250v1#S3.SS4 "3.4 Example: Large Seller who Affects all 𝑝 Default Probabilities ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), we consider the example where the large seller’s trading strategy influences the probabilities of default of all pp (defaultable) assets.

## 2 The Underlying Probability Setup

In the sequel, we fix T>0T>0 to be the finite time horizon. Let (Ω,ℱ,P)(\Omega,\mathcal{F},P) be a complete probability space, and let (Wt)t∈[0,T](W\_{t})\_{t\in[0,T]} be a one-dimensional Brownian motion. Let 𝔽≔(ℱt)t∈[0,T]\mathbb{F}\coloneqq(\mathcal{F}\_{t})\_{t\in[0,T]} denote the augmented filtration generated by WW. Inequalities and equalities between random variables are to be understood in the almost sure (a.s.) sense with respect to PP.

Let p∈ℕ∖{0}p\in\mathbb{N}\setminus\{0\}, and let τ1,τ2,…,τp\tau\_{1},\tau\_{2},\ldots,\tau\_{p} be positive random times. We assume that, for each i∈{1,…,p}i\in\{1,\ldots,p\}, the random time τi\tau\_{i} has a continuous distribution, and that P​(τi≠τj)=1P(\tau\_{i}\neq\tau\_{j})=1 for all i,j∈{1,…,p}i,j\in\{1,\ldots,p\} with i≠ji\neq j. Moreover, we assume that the pp default times are strictly ordered, i.e., τ1<τ2<⋯<τp\tau\_{1}<\tau\_{2}<\cdots<\tau\_{p}. We will interpret τi\tau\_{i} as the ii-th default (or ii-th credit event) time. For i∈{1,…,p}i\in\{1,\ldots,p\} and t∈[0,T]t\in[0,T], we define Nti≔𝟙{τi≤t}N\_{t}^{i}\coloneqq\mathbbm{1}\_{\{\tau\_{i}\leq t\}}.

For each i∈{1,…,p}i\in\{1,\ldots,p\}, let 𝔽i≔(ℱti)t∈[0,T]\mathbb{F}^{i}\coloneqq(\mathcal{F}\_{t}^{i})\_{t\in[0,T]} denote the smallest right-continuous filtration making τi\tau\_{i} an 𝔽i\mathbb{F}^{i}-stopping time. We define the enlarged filtration 𝔾≔𝔽∨𝔽1∨⋯∨𝔽p\mathbb{G}\coloneqq\mathbb{F}\vee\mathbb{F}^{1}\vee\cdots\vee\mathbb{F}^{p}. The filtration 𝔾\mathbb{G} is, in fact, the augmented filtration generated by WW and the default indicator processes N1,N2,…,NpN^{1},N^{2},\ldots,N^{p}. We assume that the 𝔽\mathbb{F}-Brownian motion WW remains a 𝔾\mathbb{G}-Brownian motion.

By definition, for each ii, the process Ni=(Nti)t∈[0,T]N^{i}=(N\_{t}^{i})\_{t\in[0,T]} is non-decreasing, 𝔾\mathbb{G}-adapted, and thus a 𝔾\mathbb{G}-submartingale. Let Λi=(Λti)\Lambda^{i}=(\Lambda\_{t}^{i}) denote the 𝔾\mathbb{G}-predictable compensator of NiN^{i}. Note that the process (Λt∧τii)(\Lambda\_{t\wedge\tau\_{i}}^{i}) is the 𝔾\mathbb{G}-predictable compensator of (Nt∧τii)(N\_{t\wedge\tau\_{i}}^{i}). By the uniqueness of the predictable compensator, we have Λt∧τii=Λti\Lambda\_{t\wedge\tau\_{i}}^{i}=\Lambda^{i}\_{t} for t≥0t\geq 0 a.s.

We further assume that each process Λi\Lambda^{i} is absolutely continuous with respect to the Lebesgue measure. This implies the existence of a non-negative 𝔾\mathbb{G}-predictable process (λti)t∈[0,T](\lambda\_{t}^{i})\_{t\in[0,T]}, called the ii-th *intensity process*, such that Λti=∫0tλsi​𝑑s\Lambda\_{t}^{i}=\int\_{0}^{t}\lambda\_{s}^{i}ds, for t∈[0,T]t\in[0,T].
Since Λti=Λt∧τii\Lambda\_{t}^{i}=\Lambda\_{t\wedge\tau\_{i}}^{i}, it follows that λti=0\lambda\_{t}^{i}=0 for t>τit>\tau\_{i}.

For each i∈{1,…,p}i\in\{1,\ldots,p\}, we define the 𝔾\mathbb{G}-compensated default martingale MiM^{i} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mti=Nti−∫0tλsi​𝑑s,M\_{t}^{i}=N\_{t}^{i}-\int\_{0}^{t}\lambda\_{s}^{i}ds, |  | (2.1) |

for all t∈[0,T]t\in[0,T].

### 2.1 BSDEs with Multiple Default Jumps

We define the following:

* •

  𝒫\mathcal{P} is the predictable σ\sigma-algebra on Ω×[0,T]\Omega\times[0,T].
* •

  𝒮T2\mathcal{S}\_{T}^{2} is the set of 𝔾\mathbb{G}-adapted right-continuous left-limited (rcll) processes φ\varphi such that 𝔼​[sup0≤t≤T|φt|2]<+∞\mathbb{E}[\sup\_{0\leq t\leq T}|\varphi\_{t}|^{2}]<+\infty.
* •

  𝒜T2\mathcal{A}\_{T}^{2} is the set of real-valued finite variation rcll 𝔾\mathbb{G}-adapted processes AA, with 𝔼​[(∫0T|d​At|)2]<∞\mathbb{E}[(\int\_{0}^{T}|dA\_{t}|)^{2}]<\infty and such that A0=0A\_{0}=0.
* •

  𝒜p,T2\mathcal{A}\_{p,T}^{2} is the subset of all predictable processes in 𝒜T2\mathcal{A}\_{T}^{2}.
* •

  ℋT2\mathcal{H}\_{T}^{2} is the space of all 𝔾\mathbb{G}-predictable processes endowed with ‖Z‖2≔𝔼​[∫0T|Zt|2​𝑑t]<∞\|Z\|^{2}\coloneqq\mathbb{E}[\int\_{0}^{T}|Z\_{t}|^{2}dt]<\infty.
* •

  ℋλi,T2\mathcal{H}\_{\lambda^{i},T}^{2} is the space L2​(Ω×[0,T],𝒫,λt​d​P⊗d​t)L^{2}(\Omega\times[0,T],\mathcal{P},\lambda\_{t}dP\otimes dt) equipped with the scalar product ⟨U,V⟩λi≔𝔼​[∫0TUt​Vt​λti​𝑑t]<∞\langle U,V\rangle\_{\lambda^{i}}\coloneqq\mathbb{E}[\int\_{0}^{T}U\_{t}V\_{t}\lambda\_{t}^{i}dt]<\infty. For all U∈ℋλi,T2U\in\mathcal{H}\_{\lambda^{i},T}^{2} we define ‖U‖λi2≔𝔼​[∫0T|Ut|2​λti​𝑑t]<∞\|U\|\_{\lambda^{i}}^{2}\coloneqq\mathbb{E}[\int\_{0}^{T}|U\_{t}|^{2}\lambda\_{t}^{i}dt]<\infty.

If it is obvious that we are working under the finite time horizon TT, we might drop the TT subscript from the above notation.

As the 𝔾\mathbb{G}-intensity λti\lambda\_{t}^{i} disappears for t>τit>\tau\_{i} we have for all U∈ℋλi2U\in\mathcal{H}\_{\lambda^{i}}^{2} ‖U‖λi2=𝔼​[∫0T∧τi|Ut|2​λti​𝑑t]\|U\|\_{\lambda^{i}}^{2}=\mathbb{E}[\int\_{0}^{T\wedge\tau\_{i}}|U\_{t}|^{2}\lambda\_{t}^{i}dt] (hence, the values of UU after τi\tau\_{i} do not intervene in the computation of ‖U‖λi2\|U\|\_{\lambda^{i}}^{2}).

For our framework of multiple defaults, we recall the martingale representation property from [[11](https://arxiv.org/html/2601.01250v1#bib.bib11)] (see also [[12](https://arxiv.org/html/2601.01250v1#bib.bib12)] Theorem 107).

###### Theorem 2.1 (Martingale Representation Property):

For any (ℙ,𝔾)(\mathbb{P},\mathbb{G})-square-integrable martingale (mt)t∈[0,T](m\_{t})\_{t\in[0,T]} there exist unique 𝔾\mathbb{G}-predictable processes z∈ℋT2z\in\mathcal{H}\_{T}^{2} and ki∈ℋλi,T2k^{i}\in\mathcal{H}\_{\lambda^{i},T}^{2} for all i∈{1,…,p}i\in\{1,\ldots,p\}, such that the following martingale representation property holds,

|  |  |  |  |
| --- | --- | --- | --- |
|  | mt=m0+∫0tzs​𝑑Ws+∑i=1p∫0tksi​𝑑Msi.m\_{t}=m\_{0}+\int\_{0}^{t}z\_{s}dW\_{s}+\sum\_{i=1}^{p}\int\_{0}^{t}k\_{s}^{i}dM\_{s}^{i}. |  | (2.2) |

In the following definition, we extend the notion of λ\lambda-driver from [[7](https://arxiv.org/html/2601.01250v1#bib.bib7)] in order to account for multiple default jumps. For simplicity we denote by λ(p)\lambda^{(p)} the vector (λ1,…,λp)′(\lambda^{1},\ldots,\lambda^{p})^{\prime} of default intensities. Here the notation ′ is for the transposition of the vector.

###### Definition 2.2 (λ(p)\lambda^{(p)}-Admissible Driver):

We say that a function gg is a driver if g:Ω×[0,T]×ℝ2+p→ℝg:\Omega\times[0,T]\times\mathbb{R}^{2+p}\rightarrow\mathbb{R} with (ω,t,y,z,k1,…,kp)↦g​(ω,t,y,z,k1,…,kp)(\omega,t,y,z,k^{1},\ldots,k^{p})\mapsto g(\omega,t,y,z,k^{1},\ldots,k^{p}) is a 𝒫⊗ℬ​(ℝ2+p)\mathcal{P}\otimes\mathcal{B}(\mathbb{R}^{2+p})-measurable function such that g​(⋅,⋅,0,0,…,0)∈ℋT2g(\cdot,\cdot,0,0,\ldots,0)\in\mathcal{H}\_{T}^{2}. The driver gg is said to be λ(p)\lambda^{(p)}-admissible if there exists a constant C≥0C\geq 0 such that for d​P⊗d​tdP\otimes dt-almost every (ω,t)(\omega,t), for all (y1,z1,k11,…,k1p)(y\_{1},z\_{1},k\_{1}^{1},\ldots,k\_{1}^{p}), (y2,z2,k21,…,k2p)(y\_{2},z\_{2},k\_{2}^{1},\ldots,k\_{2}^{p}) we have,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |g​(ω,t,y1,z1,k11,…,k1p)−g​(ω,t,y2,z2,k21,…,k2p)|≤C​(|y1−y2|+|z1−z2|+∑i=1pλti​(ω)​|k1i−k2i|).|g(\omega,t,y\_{1},z\_{1},k\_{1}^{1},\ldots,k\_{1}^{p})-g(\omega,t,y\_{2},z\_{2},k\_{2}^{1},\ldots,k\_{2}^{p})|\leq\\ C\left(|y\_{1}-y\_{2}|+|z\_{1}-z\_{2}|+\sum\_{i=1}^{p}\sqrt{\lambda\_{t}^{i}(\omega)}|k\_{1}^{i}-k\_{2}^{i}|\right). |  | (2.3) |

###### Remark 2.3:

From the condition in ([2.3](https://arxiv.org/html/2601.01250v1#S2.E3 "In Definition 2.2 (𝜆^(𝑝)-Admissible Driver): ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) we have that for each (y,z,k1,…,kp)(y,z,k^{1},\ldots,k^{p}), g​(t,y,z,k1,…,kj,kj+1,…,kp)=g​(t,y,z,0,…,0,kj+1,…,kp)g(t,y,z,k^{1},\ldots,k^{j},k^{j+1},\ldots,k^{p})=g(t,y,z,0,\ldots,0,k^{j+1},\ldots,k^{p}) for t>τjt>\tau\_{j} d​P⊗d​tdP\otimes dt-a.e., where we have used the fact that λj\lambda^{j} disappears after τj\tau\_{j} and the assumption that the stopping times τ1,…,τp\tau\_{1},\ldots,\tau\_{p} are ordered. Hence, on the set {t>τj}\{t>\tau\_{j}\}, the λ(p)\lambda^{(p)}-admissible driver gg does not depend on k1,…,kjk^{1},\ldots,k^{j}.

###### Definition 2.4 (BSDE with a λ(p)\lambda^{(p)}-Admissible Driver):

Let gg be a λ(p)\lambda^{(p)}-admissible driver and let η∈L2​(𝒢T)\eta\in L^{2}(\mathcal{G}\_{T}). A process (Y,Z,K1,…,Kp)(Y,Z,K^{1},\ldots,K^{p}) in 𝒮T2×ℋT2×ℋλ1,T2×⋯×ℋλp,T2\mathcal{S}\_{T}^{2}\times\mathcal{H}\_{T}^{2}\times\mathcal{H}\_{\lambda^{1},T}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p},T}^{2} is said to be a solution of the BSDE with pp default jumps, with a terminal time TT, a λ(p)\lambda^{(p)}-admissible driver gg, and a terminal condition η\eta, if it satisfies the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​Yt=g​(t,Yt,Zt,Kt1,…,Ktp)​d​t−Zt​d​Wt−∑i=1pKti​d​Mti,YT=η.-dY\_{t}=g(t,Y\_{t},Z\_{t},K\_{t}^{1},\ldots,K\_{t}^{p})dt-Z\_{t}dW\_{t}-\sum\_{i=1}^{p}K\_{t}^{i}dM\_{t}^{i},\quad Y\_{T}=\eta. |  | (2.4) |

As we will see later, when dealing with (possibly non-linear) pricing problems in markets with defaults, contingent claims might generate intermediate cash flows. These may arise, for instance, from promised dividends, which can be modeled as a stream of continuous or discrete random cash flows received by the claim holder, or from a recovery process, which provides a recovery payoff in the event that a default occurs before time TT. It is convenient to ‘wrap’ these various sources of intermediate cash flows into a single ‘dividend’ process DD, where DD is assumed to be optional (but not necessarily predictable), right-continuous with left limits (rcll), and of finite variation.

Thus, we are interested in BSDEs with generalized drivers which include a process D∈𝒜T2D\in\mathcal{A}\_{T}^{2}.

###### Definition 2.5 (BSDE with a *Generalized* λ(p)\lambda^{(p)}-Admissible Driver):

Let gg be a λ(p)\lambda^{(p)}-admissible driver, let η∈L2​(𝒢T)\eta\in L^{2}(\mathcal{G}\_{T}), and let D∈𝒜T2D\in\mathcal{A}\_{T}^{2}. A process (Y,Z,K1,…,Kp)(Y,Z,K^{1},\ldots,K^{p}) in 𝒮T2×ℋT2×ℋλ1,T2×⋯×ℋλp,T2\mathcal{S}\_{T}^{2}\times\mathcal{H}\_{T}^{2}\times\mathcal{H}\_{\lambda^{1},T}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p},T}^{2} is said to be a solution of the BSDE with pp default jumps, with a terminal time TT, a generalized λ(p)\lambda^{(p)}-admissible driver g​(t,y,z,k1,…,kp)​d​t+d​Dtg(t,y,z,k^{1},\ldots,k^{p})\,dt+dD\_{t}, and a terminal condition η\eta, if it satisfies the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​Yt=g​(t,Yt,Zt,Kt1,…,Ktp)​d​t+d​Dt−Zt​d​Wt−∑i=1pKti​d​Mti,YT=η.-dY\_{t}=g(t,Y\_{t},Z\_{t},K\_{t}^{1},\ldots,K\_{t}^{p})\,dt+dD\_{t}-Z\_{t}\,dW\_{t}-\sum\_{i=1}^{p}K\_{t}^{i}\,dM\_{t}^{i},\quad Y\_{T}=\eta. |  | (2.5) |

We emphasize that, in Equation ([2.5](https://arxiv.org/html/2601.01250v1#S2.E5 "In Definition 2.5 (BSDE with a Generalized 𝜆^(𝑝)-Admissible Driver): ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), the process DD is a finite variational, rcll, adapted process such that D0=0D\_{0}=0 and its total variation is integrable. This implies that DD has at most a countable number of jumps and admits the canonical decomposition D=A−A′D=A-A^{\prime}, where AA and A′A^{\prime} are integrable, non-decreasing, rcll, adapted processes starting at zero (i.e., A0=A0′=0A\_{0}=A^{\prime}\_{0}=0), and such that the mutual singularity condition d​At⟂d​At′dA\_{t}\perp dA^{\prime}\_{t} is satisfied (cf., e.g., Proposition A.7 in [[8](https://arxiv.org/html/2601.01250v1#bib.bib8)]). In the case where DD is predictable, the processes AA and A′A^{\prime} are also predictable.

###### Proposition 2.6:

If D∈𝒜T2D\in\mathcal{A}\_{T}^{2}, then there exist a unique (predictable) process D′∈𝒜p,T2D^{\prime}\in\mathcal{A}\_{p,T}^{2} and unique (predictable) processes θ1∈ℋλ1,T2\theta^{1}\in\mathcal{H}\_{\lambda^{1},T}^{2}, θ2∈ℋλ2,T2\theta^{2}\in\mathcal{H}\_{\lambda^{2},T}^{2}, …\ldots , θp∈ℋλp,T2\theta^{p}\in\mathcal{H}\_{\lambda^{p},T}^{2}, such that for all t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt=Dt′+∑i=1p∫0tθsi​𝑑Nsi.D\_{t}=D\_{t}^{\prime}+\sum\_{i=1}^{p}\int\_{0}^{t}\theta\_{s}^{i}dN\_{s}^{i}. |  | (2.6) |

###### Proof.

As D∈𝒜T2D\in\mathcal{A}\_{T}^{2}, we have the canonical decomposition D=A−A^D=A-\hat{A}, where A,A^A,\hat{A} are non-decreasing processes in 𝒜T2\mathcal{A}\_{T}^{2}, such that d​At⊥d​A^dA\_{t}\bot d\hat{A}. By applying Lemma [A.1](https://arxiv.org/html/2601.01250v1#A1.Thmtheorem1 "Lemma A.1: ‣ Appendix A Some Technical Lemmas ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") to AA and A^\hat{A}, we get, that AA and A^\hat{A} can be uniquely decomposed as,

|  |  |  |
| --- | --- | --- |
|  | At=Bt+∑i=1p∫0tψsi​𝑑Nsi,A\_{t}=B\_{t}+\sum\_{i=1}^{p}\int\_{0}^{t}\psi\_{s}^{i}dN\_{s}^{i}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | A^t=B^t+∑i=1p∫0tψ^si​𝑑Nsi,\hat{A}\_{t}=\hat{B}\_{t}+\sum\_{i=1}^{p}\int\_{0}^{t}\hat{\psi}\_{s}^{i}dN\_{s}^{i}, |  |

where (Bt)(B\_{t}) and (B^t)(\hat{B}\_{t}) are predictable (non-decreasing) and in 𝒜p,T2\mathcal{A}\_{p,T}^{2}, and for each i∈{1,…,p}i\in\{1,\ldots,p\}, (ψti)(\psi\_{t}^{i}) and (ψ^ti)(\hat{\psi}\_{t}^{i}) are in ℋλi,T2\mathcal{H}\_{\lambda^{i},T}^{2}. By setting Dt′≔Bt−B^tD\_{t}^{\prime}\coloneqq B\_{t}-\hat{B}\_{t}, and, for each i∈{1,…,p}i\in\{1,\ldots,p\}, θti≔ψti−ψ^ti\theta\_{t}^{i}\coloneqq\psi\_{t}^{i}-\hat{\psi}\_{t}^{i}, we get the desired property.
∎

### 2.2 BSDE with Multiple Default Jumps: Properties

We begin by establishing *a priori* estimates for BSDEs with pp default jumps. For β>0\beta>0, ϕ∈ℋT2\phi\in\mathcal{H}\_{T}^{2}, and ki∈ℋλi,T2k^{i}\in\mathcal{H}\_{\lambda^{i},T}^{2}, we introduce the following: ‖ϕ‖β2≔𝔼​[∫0Teβ​t​ϕt2​𝑑t]\|\phi\|\_{\beta}^{2}\coloneqq\mathbb{E}[\int\_{0}^{T}e^{\beta t}\phi\_{t}^{2}\,dt], ‖k1‖λ1,β2≔𝔼​[∫0Teβ​t​(kt1)2​λt1​𝑑t],…,‖kp‖λp,β2≔𝔼​[∫0Teβ​t​(ktp)2​λtp​𝑑t]\|k^{1}\|\_{\lambda^{1},\beta}^{2}\coloneqq\mathbb{E}[\int\_{0}^{T}e^{\beta t}(k\_{t}^{1})^{2}\lambda\_{t}^{1}\,dt],\ldots,\|k^{p}\|\_{\lambda^{p},\beta}^{2}\coloneqq\mathbb{E}[\int\_{0}^{T}e^{\beta t}(k\_{t}^{p})^{2}\lambda\_{t}^{p}\,dt], and ‖k(p)‖λ(p),β2≔∑i=1p‖ki‖λi,β2=𝔼​[∫0Teβ​t​∑i=1p(kti)2​λti​d​t]\|k^{(p)}\|\_{\lambda^{(p)},\beta}^{2}\coloneqq\sum\_{i=1}^{p}\|k^{i}\|\_{\lambda^{i},\beta}^{2}=\mathbb{E}[\int\_{0}^{T}e^{\beta t}\sum\_{i=1}^{p}(k\_{t}^{i})^{2}\lambda\_{t}^{i}\,dt].

#### 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps

###### Proposition 2.7:

Let η\eta, η^∈L2​(𝒢T)\hat{\eta}\in L^{2}(\mathcal{G}\_{T}). Let gg, g^\hat{g} be two λ(p)\lambda^{(p)}-admissible drivers. Let C>0C>0 be a λ(p)\lambda^{(p)}-constant associated to gg. Let DD be an optional process belonging to 𝒜T2\mathcal{A}\_{T}^{2}.
Let (Y,Z,K1,…,Kp)(Y,Z,K^{1},\ldots,K^{p}) and (Y^,Z^,K^1,…,K^p)(\hat{Y},\hat{Z},\hat{K}^{1},\ldots,\hat{K}^{p}) be solutions to the BSDEs associated with terminal time T>0T>0, generalized drivers g​(t,y,z,k1,…,kp)​d​t+d​Dtg(t,y,z,k^{1},\ldots,k^{p})dt+dD\_{t} and g^​(t,y^,z^,k^1,…,k^p)+d​Dt\hat{g}(t,\hat{y},\hat{z},\hat{k}^{1},\ldots,\hat{k}^{p})+dD\_{t} respectively, and terminal conditions η\eta and η^\hat{\eta} respectively.
Let η¯≔η−η^\bar{\eta}\coloneqq\eta-\hat{\eta}. For s∈[0,T]s\in[0,T], we denote Y¯s≔Ys−Y^s\bar{Y}\_{s}\coloneqq Y\_{s}-\hat{Y}\_{s}, Z¯s≔Zs−Z^s\bar{Z}\_{s}\coloneqq Z\_{s}-\hat{Z}\_{s}, and for each i∈{1,…,p}i\in\{1,\ldots,p\}, we denote K¯si≔Ksi−K^si\bar{K}\_{s}^{i}\coloneqq K\_{s}^{i}-\hat{K}\_{s}^{i}.

Let ξ\xi, β>0\beta>0 be such that β≥p+2ξ+2​C\beta\geq\frac{p+2}{\xi}+2C and ξ≤1C2\xi\leq\frac{1}{C^{2}}. Then, for each t∈[0,T]t\in[0,T], it holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | eβ​tY¯t2≤𝔼[eβ​Tη¯2|𝒢t]+ξ 𝔼[∫tTeβ​sg¯s2ds | 𝒢t]a.s.,e^{\beta t}\bar{Y}\_{t}^{2}\leq\mathbb{E}\left[e^{\beta T}\bar{\eta}^{2}\middle|\mathcal{G}\_{t}\right]+\xi\text{ }\mathbb{E}\left[\int\_{t}^{T}e^{\beta s}\bar{g}\_{s}^{2}ds\text{ }\middle|\text{ }\mathcal{G}\_{t}\right]\quad\text{a.s.}, |  | (2.7) |

where g¯s≔g​(s,Y^s,Z^s,K^s1​…,K^sp)−g^​(s,Y^s,Z^s,K^s1​…,K^sp)\bar{g}\_{s}\coloneqq g(s,\hat{Y}\_{s},\hat{Z}\_{s},\hat{K}\_{s}^{1}\ldots,\hat{K}\_{s}^{p})-\hat{g}(s,\hat{Y}\_{s},\hat{Z}\_{s},\hat{K}\_{s}^{1}\ldots,\hat{K}\_{s}^{p}). Further,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Y¯‖β2≤T​[eβ​T​𝔼​[η¯2]+ξ​ ​‖g¯‖β2].\|\bar{Y}\|\_{\beta}^{2}\leq T\left[e^{\beta T}\mathbb{E}[\bar{\eta}^{2}]+\xi\text{ }\|\bar{g}\|\_{\beta}^{2}\right]. |  | (2.8) |

Moreover, if ξ<1C2\xi<\frac{1}{C^{2}}, we have,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Z¯‖β2+‖K¯(p)‖λ(p),β2≤1(1−C2​ξ)​[eβ​T​𝔼​[η¯2]+ξ​ ​‖g¯‖β2].\|\bar{Z}\|\_{\beta}^{2}+\|\bar{K}^{(p)}\|\_{\lambda^{(p)},\beta}^{2}\leq\frac{1}{(1-C^{2}\xi)}\left[e^{\beta T}\mathbb{E}[\bar{\eta}^{2}]+\xi\text{ }\|\bar{g}\|\_{\beta}^{2}\right]. |  | (2.9) |

###### Proof.

Using Itô’s formula applied to the semimartingale (eβ​s​Y¯s2)(e^{\beta s}\bar{Y}\_{s}^{2}) between tt and TT, we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | eβ​T​Y¯T2=eβ​t​Y¯t2+β​∫tTeβ​s​Y¯s−2​𝑑s+2​∫tTeβ​s​Y¯s−​𝑑Y¯s+∫tTeβ​s​d​⟨Y¯c⟩s+∑t<s≤T(eβ​s​Y¯s2−eβ​s​Y¯s−2−2​eβ​s​Y¯s−​Δ​Y¯s).\displaystyle\begin{aligned} e^{\beta T}\bar{Y}\_{T}^{2}&=e^{\beta t}\bar{Y}\_{t}^{2}+\beta\int\_{t}^{T}e^{\beta s}\bar{Y}\_{s-}^{2}ds+2\int\_{t}^{T}e^{\beta s}\bar{Y}\_{s-}d\bar{Y}\_{s}\\ &\quad+\int\_{t}^{T}e^{\beta s}d\langle\bar{Y}^{c}\rangle\_{s}+\sum\_{t<s\leq T}\left(e^{\beta s}\bar{Y}\_{s}^{2}-e^{\beta s}\bar{Y}\_{s-}^{2}-2e^{\beta s}\bar{Y}\_{s-}\Delta\bar{Y}\_{s}\right).\end{aligned} |  | (2.10) |

Further computation (noting that the d​DtdD\_{t} terms cancel) leads to,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 2​∫tTeβ​s​Y¯s−​𝑑Y¯s=−2​∫tTeβ​s​Y¯s−​(g​(s,Ys,Zs,Ks1,…,Ksp)−g^​(s,Y^s,Z^s,K^s1,…,K^sp))​𝑑s+2​∫tTeβ​s​Y¯s−​Z¯s​𝑑Ws+2​∫tTeβ​s​Y¯s−​∑i=1pK¯si​d​Msi,\displaystyle\begin{aligned} 2\int\_{t}^{T}e^{\beta s}\bar{Y}\_{s-}d\bar{Y}\_{s}&=-2\int\_{t}^{T}e^{\beta s}\bar{Y}\_{s-}(g(s,Y\_{s},Z\_{s},K\_{s}^{1},\ldots,K\_{s}^{p})-\hat{g}(s,\hat{Y}\_{s},\hat{Z}\_{s},\hat{K}\_{s}^{1},\ldots,\hat{K}\_{s}^{p}))ds\\ &\quad+2\int\_{t}^{T}e^{\beta s}\bar{Y}\_{s-}\bar{Z}\_{s}dW\_{s}+2\int\_{t}^{T}e^{\beta s}\bar{Y}\_{s-}\sum\_{i=1}^{p}\bar{K}\_{s}^{i}dM\_{s}^{i},\end{aligned} |  | (2.11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∫tTeβ​s​d​⟨Y¯c⟩s=∫tTeβ​s​Z¯s2​𝑑s,\displaystyle\quad\quad\int\_{t}^{T}e^{\beta s}d\langle\bar{Y}^{c}\rangle\_{s}=\int\_{t}^{T}e^{\beta s}\bar{Z}\_{s}^{2}ds, |  | (2.12) |

and the ‘jump term’,

|  |  |  |
| --- | --- | --- |
|  | ∑t<s≤T(eβ​s​Y¯s2−eβ​s​Y¯s−2−2​eβ​s​Y¯s−​Δ​Y¯s)=∑t<s≤Teβ​s​(Y¯s−Y¯s−)2.\displaystyle\sum\_{t<s\leq T}\left(e^{\beta s}\bar{Y}\_{s}^{2}-e^{\beta s}\bar{Y}\_{s-}^{2}-2e^{\beta s}\bar{Y}\_{s-}\Delta\bar{Y}\_{s}\right)=\sum\_{t<s\leq T}e^{\beta s}(\bar{Y}\_{s}-\bar{Y}\_{s-})^{2}. |  |

Since P​(τi=τj)=0P(\tau\_{i}=\tau\_{j})=0 for all i,j∈{1,…,p}i,j\in\{1,\ldots,p\} such that i≠ji\neq j, we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑t<s≤T(eβ​s​Y¯s2−eβ​s​Y¯s−2−2​eβ​s​Y¯s−​Δ​Y¯s)=∑t<s≤Teβ​s​(Y¯s−Y¯s−)2=∫tTeβ​s​∑i=1p(K¯si)2​d​Nsi=∫tTeβ​s​∑i=1p(K¯si)2​d​Msi+∫tTeβ​s​∑i=1p(K¯si)2​λsi​d​s.\displaystyle\begin{aligned} &\sum\_{t<s\leq T}(e^{\beta s}\bar{Y}\_{s}^{2}-e^{\beta s}\bar{Y}\_{s-}^{2}-2e^{\beta s}\bar{Y}\_{s-}\Delta\bar{Y}\_{s})=\sum\_{t<s\leq T}e^{\beta s}(\bar{Y}\_{s}-\bar{Y}\_{s-})^{2}\\ &=\int\_{t}^{T}e^{\beta s}\sum\_{i=1}^{p}(\bar{K}\_{s}^{i})^{2}dN\_{s}^{i}\\ &=\int\_{t}^{T}e^{\beta s}\sum\_{i=1}^{p}(\bar{K}\_{s}^{i})^{2}dM\_{s}^{i}+\int\_{t}^{T}e^{\beta s}\sum\_{i=1}^{p}(\bar{K}\_{s}^{i})^{2}\lambda\_{s}^{i}ds.\end{aligned} |  | (2.13) |

Plugging ([2.11](https://arxiv.org/html/2601.01250v1#S2.E11 "In Proof. ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), ([2.12](https://arxiv.org/html/2601.01250v1#S2.E12 "In Proof. ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), and ([2.13](https://arxiv.org/html/2601.01250v1#S2.E13 "In Proof. ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), into ([2.10](https://arxiv.org/html/2601.01250v1#S2.E10 "In Proof. ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | eβ​t​Y¯t2+β​∫tTeβ​s​Y¯s−2​𝑑s+∫tTeβ​s​(Z¯s2+∑i=1p(K¯si)2​λsi)​𝑑s=eβ​T​Y¯T2​ +2​∫tTeβ​s​Y¯s−​(g​(s,Ys,Zs,Ks1,…,Ksp)−g^​(s,Y^s,Z^s,K^s1,…,K^sp))​𝑑s−2​∫tTeβ​s​Y¯s−​Z¯s​𝑑Ws−2​∑i=1p∫tTeβ​s​Y¯s−​K¯si​𝑑Msi−∑i=1p∫tTeβ​s​(K¯si)2​𝑑Msi.\displaystyle\begin{aligned} e^{\beta t}\bar{Y}\_{t}^{2}&+\beta\int\_{t}^{T}e^{\beta s}\bar{Y}\_{s-}^{2}ds+\int\_{t}^{T}e^{\beta s}\left(\bar{Z}\_{s}^{2}+\sum\_{i=1}^{p}(\bar{K}\_{s}^{i})^{2}\lambda\_{s}^{i}\right)ds=e^{\beta T}\bar{Y}\_{T}^{2}\text{ }+\\ &2\int\_{t}^{T}e^{\beta s}\bar{Y}\_{s-}(g(s,Y\_{s},Z\_{s},K\_{s}^{1},\ldots,K\_{s}^{p})-\hat{g}(s,\hat{Y}\_{s},\hat{Z}\_{s},\hat{K}\_{s}^{1},\ldots,\hat{K}\_{s}^{p}))ds\\ &-2\int\_{t}^{T}e^{\beta s}\bar{Y}\_{s-}\bar{Z}\_{s}dW\_{s}-2\sum\_{i=1}^{p}\int\_{t}^{T}e^{\beta s}\bar{Y}\_{s-}\bar{K}\_{s}^{i}dM\_{s}^{i}-\sum\_{i=1}^{p}\int\_{t}^{T}e^{\beta s}(\bar{K}\_{s}^{i})^{2}dM\_{s}^{i}.\end{aligned} |  | (2.14) |

Taking the conditional expectation given 𝒢t\mathcal{G}\_{t} in ([2.14](https://arxiv.org/html/2601.01250v1#S2.E14 "In Proof. ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) results in,

|  |  |  |  |
| --- | --- | --- | --- |
|  | eβ​t​Y¯t2+𝔼[β∫tTeβ​sY¯s−2ds+∫tTeβ​s(Z¯s2+∑i=1p(K¯si)2λsi)ds|𝒢t]=𝔼[eβ​TY¯T2|𝒢t]+2𝔼[∫tTeβ​sY¯s−(g(s,Ys,Zs,Ks1,…,Ksp)−g^(s,Y^s,Z^s,K^s1,…,K^sp))ds|𝒢t].\displaystyle\begin{aligned} e^{\beta t}\bar{Y}\_{t}^{2}&+\mathbb{E}\left[\beta\int\_{t}^{T}e^{\beta s}\bar{Y}\_{s-}^{2}ds+\int\_{t}^{T}e^{\beta s}\left(\bar{Z}\_{s}^{2}+\sum\_{i=1}^{p}(\bar{K}\_{s}^{i})^{2}\lambda\_{s}^{i}\right)ds\middle|\mathcal{G}\_{t}\right]\\ &=\mathbb{E}\left[e^{\beta T}\bar{Y}\_{T}^{2}\middle|\mathcal{G}\_{t}\right]\\ &+2\mathbb{E}\left[\int\_{t}^{T}e^{\beta s}\bar{Y}\_{s-}(g(s,Y\_{s},Z\_{s},K\_{s}^{1},\ldots,K\_{s}^{p})-\hat{g}(s,\hat{Y}\_{s},\hat{Z}\_{s},\hat{K}\_{s}^{1},\ldots,\hat{K}\_{s}^{p}))ds\middle|\mathcal{G}\_{t}\right].\end{aligned} |  | (2.15) |

Now,

|  |  |  |
| --- | --- | --- |
|  | g​(s,Ys,Zs,Ks1,…,Ksp)−g^​(s,Y^s,Z^s,K^s1,…,K^sp)=g​(s,Ys,Zs,Ks1,…,Ksp)−g​(s,Y^s,Z^s,K^s1,…,K^sp)+g¯s.g(s,Y\_{s},Z\_{s},K\_{s}^{1},\ldots,K\_{s}^{p})-\hat{g}(s,\hat{Y}\_{s},\hat{Z}\_{s},\hat{K}\_{s}^{1},\ldots,\hat{K}\_{s}^{p})\\ =g(s,Y\_{s},Z\_{s},K\_{s}^{1},\ldots,K\_{s}^{p})-g(s,\hat{Y}\_{s},\hat{Z}\_{s},\hat{K}\_{s}^{1},\ldots,\hat{K}\_{s}^{p})+\bar{g}\_{s}. |  |

Since gg is a λ(p)\lambda^{(p)}-admissible driver, it satisfies condition ([2.3](https://arxiv.org/html/2601.01250v1#S2.E3 "In Definition 2.2 (𝜆^(𝑝)-Admissible Driver): ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")); hence,

|  |  |  |
| --- | --- | --- |
|  | |g​(s,Ys,Zs,Ks1,…,Ksp)−g^​(s,Y^s,Z^s,K^s1,…,K^sp)|≤C​|Y¯s|+C​|Z¯s|+C​∑i=1p|K¯si|​λsi+|g¯s|.|g(s,Y\_{s},Z\_{s},K\_{s}^{1},\ldots,K\_{s}^{p})-\hat{g}(s,\hat{Y}\_{s},\hat{Z}\_{s},\hat{K}\_{s}^{1},\ldots,\hat{K}\_{s}^{p})|\\ \leq C|\bar{Y}\_{s}|+C|\bar{Z}\_{s}|+C\sum\_{i=1}^{p}|\bar{K}\_{s}^{i}|\sqrt{\lambda\_{s}^{i}}+|\bar{g}\_{s}|. |  |

For all y,z,a,k1,λ1,…,kp,λpy,z,a,k^{1},\lambda^{1},\ldots,k^{p},\lambda^{p} and ϵ>0\epsilon>0 we have the elementary inequalities,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​y​(C​z+C​∑i=1pki​λi+a)\displaystyle 2y\left(Cz+C\sum\_{i=1}^{p}k^{i}\sqrt{\lambda^{i}}+a\right) | ≤y2ϵ2+ϵ2​(C​z+C​∑i=1pki​λi+a)2\displaystyle\leq\frac{y^{2}}{\epsilon^{2}}+\epsilon^{2}\left(Cz+C\sum\_{i=1}^{p}k^{i}\sqrt{\lambda^{i}}+a\right)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤y2ϵ2+(p+2)​ϵ2​(C2​z2+C2​∑i=1p(ki)2​λi+a2).\displaystyle\leq\frac{y^{2}}{\epsilon^{2}}+(p+2)\epsilon^{2}\left(C^{2}z^{2}+C^{2}\sum\_{i=1}^{p}(k^{i})^{2}\lambda^{i}+a^{2}\right). |  |

Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫tTeβ​s​2​Y¯s−​(g​(s,Ys,Zs,Ks1,…,Ksp)−g^​(s,Y^s,Z^s,K^s1,…,K^sp))​𝑑s≤(2​C+1ϵ2)​∫tTeβ​s​Y¯s−2​𝑑s+(p+2)​C2​ϵ2​∫tTeβ​s​(Z¯s2+∑i=1p(K¯si)2​λsi)​𝑑s+(p+2)​ϵ2​∫tTeβ​s​g¯s2​𝑑s.\displaystyle\begin{aligned} &\int\_{t}^{T}e^{\beta s}2\bar{Y}\_{s-}(g(s,Y\_{s},Z\_{s},K\_{s}^{1},\ldots,K\_{s}^{p})-\hat{g}(s,\hat{Y}\_{s},\hat{Z}\_{s},\hat{K}\_{s}^{1},\ldots,\hat{K}\_{s}^{p}))ds\\ &\leq\left(2C+\frac{1}{\epsilon^{2}}\right)\int\_{t}^{T}e^{\beta s}\bar{Y}\_{s-}^{2}ds+(p+2)C^{2}\epsilon^{2}\int\_{t}^{T}e^{\beta s}\left(\bar{Z}\_{s}^{2}+\sum\_{i=1}^{p}(\bar{K}\_{s}^{i})^{2}\lambda\_{s}^{i}\right)ds\\ &\quad+(p+2)\epsilon^{2}\int\_{t}^{T}e^{\beta s}\bar{g}\_{s}^{2}ds.\end{aligned} |  | (2.16) |

Setting ξ≔(p+2)​ϵ2>0\xi\coloneqq(p+2)\epsilon^{2}>0, and using inequality ([2.16](https://arxiv.org/html/2601.01250v1#S2.E16 "In Proof. ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) in ([2.15](https://arxiv.org/html/2601.01250v1#S2.E15 "In Proof. ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), we have,

|  |  |  |  |
| --- | --- | --- | --- |
|  | eβ​tY¯t2≤𝔼[eβ​Tη¯2|𝒢t]+𝔼[(2C+p+2ξ−β)∫tTeβ​sY¯s−2ds|𝒢t]+𝔼[(C2ξ−1)∫tTeβ​s(Z¯s2+∑i=1p(K¯si)2λsi)ds|𝒢t]+𝔼[ξ∫tTeβ​sg¯s2ds|𝒢t].\displaystyle\begin{aligned} &e^{\beta t}\bar{Y}\_{t}^{2}\leq\mathbb{E}[e^{\beta T}\bar{\eta}^{2}|\mathcal{G}\_{t}]+\mathbb{E}\left[\left(2C+\frac{p+2}{\xi}-\beta\right)\int\_{t}^{T}e^{\beta s}\bar{Y}\_{s-}^{2}ds\middle|\mathcal{G}\_{t}\right]+\\ &\quad\mathbb{E}\left[(C^{2}\xi-1)\int\_{t}^{T}e^{\beta s}\left(\bar{Z}\_{s}^{2}+\sum\_{i=1}^{p}(\bar{K}\_{s}^{i})^{2}\lambda\_{s}^{i}\right)ds\middle|\mathcal{G}\_{t}\right]+\mathbb{E}\left[\xi\int\_{t}^{T}e^{\beta s}\bar{g}\_{s}^{2}ds\middle|\mathcal{G}\_{t}\right].\end{aligned} |  | (2.17) |

Then for each ξ,β>0\xi,\beta>0 such that β≥2​C+p+2ξ\beta\geq 2C+\frac{p+2}{\xi} and ξ≤1C2\xi\leq\frac{1}{C^{2}} we obtain the desired inequality ([2.7](https://arxiv.org/html/2601.01250v1#S2.E7 "In Proposition 2.7: ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")).

Using inequality ([2.17](https://arxiv.org/html/2601.01250v1#S2.E17 "In Proof. ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), integrating from 0 to TT, and taking the expectation, we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Y¯‖β2\displaystyle\|\bar{Y}\|\_{\beta}^{2} | ≤T[eβ​T𝔼[η¯2]+ξ∥g¯∥β2]+𝔼[∫0T𝔼[(C2ξ−1)∫tTeβ​s(Z¯s2+∑i=1p(K¯si)2)ds|𝒢t]dt]\displaystyle\leq T\left[e^{\beta T}\mathbb{E}[\bar{\eta}^{2}]+\xi\|\bar{g}\|\_{\beta}^{2}\right]+\mathbb{E}\left[\int\_{0}^{T}\mathbb{E}\left[(C^{2}\xi-1)\int\_{t}^{T}e^{\beta s}(\bar{Z}\_{s}^{2}+\sum\_{i=1}^{p}(\bar{K}\_{s}^{i})^{2})ds\middle|\mathcal{G}\_{t}\right]dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤T[eβ​T𝔼[η¯2]+ξ∥g¯∥β2]+(C2ξ−1)∫0T𝔼[∫0Teβ​s(Z¯s2+∑i=1p(K¯si)2ds]dt\displaystyle\leq T\left[e^{\beta T}\mathbb{E}[\bar{\eta}^{2}]+\xi\|\bar{g}\|\_{\beta}^{2}\right]+(C^{2}\xi-1)\int\_{0}^{T}\mathbb{E}\left[\int\_{0}^{T}e^{\beta s}(\bar{Z}\_{s}^{2}+\sum\_{i=1}^{p}(\bar{K}\_{s}^{i})^{2}ds\right]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =T​[eβ​T​𝔼​[η¯2]+ξ​‖g¯‖β2]+T​(C2​ξ−1)​(‖Z¯‖β2+‖K¯(p)‖λ(p),β2).\displaystyle=T\left[e^{\beta T}\mathbb{E}[\bar{\eta}^{2}]+\xi\|\bar{g}\|\_{\beta}^{2}\right]+T(C^{2}\xi-1)(\|\bar{Z}\|\_{\beta}^{2}+\|\bar{K}^{(p)}\|\_{\lambda^{(p)},\beta}^{2}). |  |

By rearranging, we get

|  |  |  |
| --- | --- | --- |
|  | ‖Y¯‖β2+T​(1−C2​ξ)​(‖Z¯‖β2+‖K¯(p)‖λ(p),β2)≤T​[eβ​T​𝔼​[η¯2]+ξ​‖g¯‖β2]\displaystyle\|\bar{Y}\|\_{\beta}^{2}+T(1-C^{2}\xi)(\|\bar{Z}\|\_{\beta}^{2}+\|\bar{K}^{(p)}\|\_{\lambda^{(p)},\beta}^{2})\leq T\left[e^{\beta T}\mathbb{E}[\bar{\eta}^{2}]+\xi\|\bar{g}\|\_{\beta}^{2}\right] |  |

Since ξ≤1C2\xi\leq\frac{1}{C^{2}}, we get the inequality from ([2.8](https://arxiv.org/html/2601.01250v1#S2.E8 "In Proposition 2.7: ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")).
  
Since ‖Y¯‖β2≥0\|\bar{Y}\|\_{\beta}^{2}\geq 0, we get,

|  |  |  |
| --- | --- | --- |
|  | ‖Z¯‖β2+‖K¯(p)‖λ(p),β2≤11−C2​ξ​[eβ​T​𝔼​[η¯2]+ξ​‖g¯‖β2],\displaystyle\|\bar{Z}\|\_{\beta}^{2}+\|\bar{K}^{(p)}\|\_{\lambda^{(p)},\beta}^{2}\leq\frac{1}{1-C^{2}\xi}\left[e^{\beta T}\mathbb{E}[\bar{\eta}^{2}]+\xi\|\bar{g}\|\_{\beta}^{2}\right], |  |

which leads to the inequality ([2.9](https://arxiv.org/html/2601.01250v1#S2.E9 "In Proposition 2.7: ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) for ξ<1C2\xi<\frac{1}{C^{2}}

∎

###### Remark 2.8:

In the case of a λ(p)\lambda^{(p)}-constant C=0C=0, ([2.7](https://arxiv.org/html/2601.01250v1#S2.E7 "In Proposition 2.7: ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) and ([2.8](https://arxiv.org/html/2601.01250v1#S2.E8 "In Proposition 2.7: ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) hold for all ξ,β>0\xi,\beta>0 such that β≥p+2ξ\beta\geq\frac{p+2}{\xi}. Inequality ([2.9](https://arxiv.org/html/2601.01250v1#S2.E9 "In Proposition 2.7: ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) holds for all ξ>0\xi>0 when C=0C=0.

#### 2.2.2 Existence and Uniqueness for BSDEs with Multiple Default Jumps

With the *a priori* estimates established for BSDEs with pp default jumps, we can now prove the existence and uniqueness of the solution. To do so, we make use of the representation property of square-integrable 𝔾\mathbb{G}-martingales (Theorem [2.1](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem1 "Theorem 2.1 (Martingale Representation Property): ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) and the *a priori* estimates established in Proposition [2.7](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem7 "Proposition 2.7: ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach").
  
For β>0\beta>0, we denote by ℋβ2,(p)\mathcal{H}\_{\beta}^{2,(p)} the space 𝒮2×ℋβ2×ℋλ1,β2×⋯×ℋλp,β2\mathcal{S}^{2}\times\mathcal{H}\_{\beta}^{2}\times\mathcal{H}\_{\lambda^{1},\beta}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p},\beta}^{2} equipped with the norm ‖(Y,Z,K1,…,Kp)‖β2,(p)≔‖Y‖β2+‖Z‖β2+‖K1‖λ1,β2+⋯+‖Kp‖λp,β2\|\left(Y,Z,K^{1},\ldots,K^{p}\right)\|\_{\beta}^{2,(p)}\coloneqq\|Y\|\_{\beta}^{2}+\|Z\|\_{\beta}^{2}+\|K^{1}\|\_{\lambda^{1},\beta}^{2}+\cdots+\|K^{p}\|\_{\lambda^{p},\beta}^{2}.

###### Proposition 2.9 (Exsitence and Uniqueness):

Let gg be a λ(p)\lambda^{(p)}-admissible driver, η∈L2​(𝒢T)\eta\in L^{2}(\mathcal{G}\_{T}) and DD be an optional process in 𝒜T2\mathcal{A}\_{T}^{2}. There exists a unique solution (Y,Z,K1,…,Kp)(Y,Z,K^{1},\ldots,K^{p}) in 𝒮T2×ℋT2×ℋλ1,T2×⋯×ℋλp,T2\mathcal{S}\_{T}^{2}\times\mathcal{H}\_{T}^{2}\times\mathcal{H}\_{\lambda^{1},T}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p},T}^{2} of the BSDE with multiple default jumps from Definition [2.5](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem5 "Definition 2.5 (BSDE with a Generalized 𝜆^(𝑝)-Admissible Driver): ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach").

###### Proof.

The proof follows a standard two-step argument, where the second step relies on the *a priori* estimates from Proposition [2.7](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem7 "Proposition 2.7: ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach").

We first consider the case where the driver is a driver process g​(t)g(t) which does not depend on (y,z,k1,…,kp)(y,z,k^{1},\ldots,k^{p}). In this case, the first component of the solution is, Yt=𝔼​[η+∫tTg​(s)​𝑑s+DT−Dt|𝒢t]Y\_{t}=\mathbb{E}[\eta+\int\_{t}^{T}g(s)ds+D\_{T}-D\_{t}|\mathcal{G}\_{t}]. Applying the 𝔾\mathbb{G}-martingale representation property to the square-integrable martingale 𝔼​[η+∫0Tg​(s)​𝑑s+DT|𝒢t]\mathbb{E}[\eta+\int\_{0}^{T}g(s)ds+D\_{T}|\mathcal{G}\_{t}] we get the processes Z∈ℋT2Z\in\mathcal{H}\_{T}^{2} and Ki∈ℋλi,T2K^{i}\in\mathcal{H}\_{\lambda^{i},T}^{2} for i∈{1,…,p}i\in\{1,\ldots,p\}. These processes are unique due to the uniqueness in the 𝔾\mathbb{G}-martingale representation result from Theorem [2.1](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem1 "Theorem 2.1 (Martingale Representation Property): ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"). Hence there exists a unique solution to the BSDE with driver g​(s)​d​s+d​Dsg(s)ds+dD\_{s}, terminal time TT and terminal condition η∈L2​(𝒢T)\eta\in L^{2}(\mathcal{G}\_{T}).

We now focus on the case of a λ(p)\lambda^{(p)}-admissible driver g​(t,y,z,k1,…,kp)g(t,y,z,k^{1},\ldots,k^{p}). We define a mapping 𝚽\mathbf{\Phi} from ℋβ2,(p)\mathcal{H}\_{\beta}^{2,(p)} to ℋβ2,(p)\mathcal{H}\_{\beta}^{2,(p)} as follows: for (U,V,J1,…,Jp)∈ℋβ2,(p)(U,V,J^{1},\ldots,J^{p})\in\mathcal{H}\_{\beta}^{2,(p)}, (Y,Z,K1,…,Kp)=𝚽​(U,V,J1,…,Jp)(Y,Z,K^{1},\ldots,K^{p})=\mathbf{\Phi}(U,V,J^{1},\ldots,J^{p}) is the solution of the BSDE with driver g​(t,Ut,Vt,Jt1,…,Jtp)​d​t+d​Dtg(t,U\_{t},V\_{t},J\_{t}^{1},\ldots,J\_{t}^{p})dt+dD\_{t}, terminal time TT and terminal condition η∈L2​(𝒢T)\eta\in L^{2}(\mathcal{G}\_{T}).
The mapping is well-defined due to the first step of the proof.
We show that the mapping 𝚽\mathbf{\Phi} is a strict contraction. Let (U^,V^,J^1,…,J^p)∈ℋβ2,p(\hat{U},\hat{V},\hat{J}^{1},\ldots,\hat{J}^{p})\in\mathcal{H}\_{\beta}^{2,p} and let (Y^,Z^,K^1,…,K^p)≔𝚽​(U^,V^,J^1,…,J^p)(\hat{Y},\hat{Z},\hat{K}^{1},\ldots,\hat{K}^{p})\coloneqq\mathbf{\Phi}(\hat{U},\hat{V},\hat{J}^{1},\ldots,\hat{J}^{p}) be the solution of the BSDE with the driver g​(t,U^t,V^t,J^t1,…,J^tp)​d​t+d​Dtg(t,\hat{U}\_{t},\hat{V}\_{t},\hat{J}\_{t}^{1},\ldots,\hat{J}\_{t}^{p})dt+dD\_{t}, terminal time TT and terminal condition η∈L2​(𝒢T)\eta\in L^{2}(\mathcal{G}\_{T}).

We set U¯t≔Ut−U^t\bar{U}\_{t}\coloneqq U\_{t}-\hat{U}\_{t}, V¯t≔Vt−V^t\bar{V}\_{t}\coloneqq V\_{t}-\hat{V}\_{t}, Y¯t≔Yt−Y^t\bar{Y}\_{t}\coloneqq Y\_{t}-\hat{Y}\_{t}, Z¯t≔Zt−Z^t\bar{Z}\_{t}\coloneqq Z\_{t}-\hat{Z}\_{t}, and for each i∈{1,…,p}i\in\{1,\ldots,p\} J¯ti≔Jti−J^ti\bar{J}\_{t}^{i}\coloneqq J\_{t}^{i}-\hat{J}\_{t}^{i} and K¯ti≔Kti−K^ti\bar{K}\_{t}^{i}\coloneqq K\_{t}^{i}-\hat{K}\_{t}^{i}. We set Δ​gt≔g​(t,Ut,Vt,Jt1,…,Jtp)−g​(t,U^t,V^t,J^t1,…,J^tp)\Delta g\_{t}\coloneqq g(t,U\_{t},V\_{t},J\_{t}^{1},\ldots,J\_{t}^{p})-g(t,\hat{U}\_{t},\hat{V}\_{t},\hat{J}\_{t}^{1},\ldots,\hat{J}\_{t}^{p}).
Then by the *a priori* estimates from Proposition [2.7](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem7 "Proposition 2.7: ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") and Remark [2.8](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem8 "Remark 2.8: ‣ 2.2.1 A Priori Estimates for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), applied to the driver processes g1​(t)≔g​(t,Ut,Vt,Jt1,…,Jtp)g\_{1}(t)\coloneqq g(t,U\_{t},V\_{t},J\_{t}^{1},\ldots,J\_{t}^{p}) and g2​(t)≔g​(t,U^t,V^t,J^t1,…,J^tp)g\_{2}(t)\coloneqq g(t,\hat{U}\_{t},\hat{V}\_{t},\hat{J}\_{t}^{1},\ldots,\hat{J}\_{t}^{p}) (where the driver g1​(t)g\_{1}(t) admits C1=0C\_{1}=0 as a λ(p)\lambda^{(p)}-constant since g1g\_{1} only depends on (t,ω)(t,\omega)), we have that, for all ξ,β>0\xi,\beta>0 such that β≥p+2ξ\beta\geq\frac{p+2}{\xi},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Y¯‖β2+‖Z¯‖β2+∑i=1p‖K¯i‖λi,β2≤ξ​T​‖Δ​g‖β2+ξ​‖Δ​g‖β2=ξ​(T+1)​‖Δ​g‖β2.\displaystyle\begin{aligned} \|\bar{Y}\|\_{\beta}^{2}+\|\bar{Z}\|\_{\beta}^{2}+\sum\_{i=1}^{p}\|\bar{K}^{i}\|\_{\lambda^{i},\beta}^{2}&\leq\xi T\|\Delta g\|\_{\beta}^{2}+\xi\|\Delta g\|\_{\beta}^{2}\\ &=\xi(T+1)\|\Delta g\|\_{\beta}^{2}.\end{aligned} |  | (2.18) |

As by definition gg is a λ(p)\lambda^{(p)}-admissible driver with λ(p)\lambda^{(p)} constant C>0C>0 we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | eβ​s​(Δ​gs)2\displaystyle e^{\beta s}(\Delta g\_{s})^{2} | ≤eβ​s​C2​(|U¯s|+|V¯s|+∑i=1p|J¯si|​λsi)2\displaystyle\leq e^{\beta s}C^{2}(|\bar{U}\_{s}|+|\bar{V}\_{s}|+\sum\_{i=1}^{p}|\bar{J}\_{s}^{i}|\sqrt{\lambda\_{s}^{i}})^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C2​(p+2)​eβ​s​[U¯s2+V¯s2+∑i=1p(J¯si)2​λsi].\displaystyle\leq C^{2}(p+2)e^{\beta s}[\bar{U}\_{s}^{2}+\bar{V}\_{s}^{2}+\sum\_{i=1}^{p}(\bar{J}\_{s}^{i})^{2}\lambda\_{s}^{i}]. |  |

Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Δ​g‖β2≤C2​(p+2)​𝔼​[∫0Teβ​s​(U¯s2+V¯s2+∑i=1p(J¯si)2​λsi)​𝑑s]=C2​(p+2)​(‖U¯‖β2+‖V¯‖β2+∑i=1p‖J¯i‖λi,β2).\displaystyle\begin{aligned} \|\Delta g\|\_{\beta}^{2}&\leq C^{2}(p+2)\mathbb{E}\left[\int\_{0}^{T}e^{\beta s}(\bar{U}\_{s}^{2}+\bar{V}\_{s}^{2}+\sum\_{i=1}^{p}(\bar{J}\_{s}^{i})^{2}\lambda\_{s}^{i})ds\right]\\ &=C^{2}(p+2)(\|\bar{U}\|\_{\beta}^{2}+\|\bar{V}\|\_{\beta}^{2}+\sum\_{i=1}^{p}\|\bar{J}^{i}\|\_{\lambda^{i},\beta}^{2}).\end{aligned} |  | (2.19) |

Using inequalities ([2.19](https://arxiv.org/html/2601.01250v1#S2.E19 "In Proof. ‣ 2.2.2 Existence and Uniqueness for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) and ([2.18](https://arxiv.org/html/2601.01250v1#S2.E18 "In Proof. ‣ 2.2.2 Existence and Uniqueness for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Y¯‖β2+‖Z¯‖β2+∑i=1p‖K¯i‖λi,β2≤C2​(p+2)​ξ​(T+1)​(‖U¯‖β2+‖V¯‖β2+∑i=1p‖J¯i‖λi,β2),\|\bar{Y}\|\_{\beta}^{2}+\|\bar{Z}\|\_{\beta}^{2}+\sum\_{i=1}^{p}\|\bar{K}^{i}\|\_{\lambda^{i},\beta}^{2}\leq C^{2}(p+2)\xi(T+1)(\|\bar{U}\|\_{\beta}^{2}+\|\bar{V}\|\_{\beta}^{2}+\sum\_{i=1}^{p}\|\bar{J}^{i}\|\_{\lambda^{i},\beta}^{2}), |  | (2.20) |

for all ξ,β>0\xi,\beta>0 such that β≥p+2ξ\beta\geq\frac{p+2}{\xi}. Choosing ξ=12​(T+1)​(p+2)​C2\xi=\frac{1}{2(T+1)(p+2)C^{2}} and β≥2​(p+2)2​(T+1)​C2\beta\geq 2(p+2)^{2}(T+1)C^{2}, we derive ∥Y¯,Z¯,K¯1,…,K¯p∥β2,(p)≤12∥U¯,V¯,J¯1,…,J¯p∥β2,(p)\|\bar{Y},\bar{Z},\bar{K}^{1},\ldots,\bar{K}^{p}\|\_{\beta}^{2,(p)}\leq\frac{1}{2}\|\bar{U},\bar{V},\bar{J}^{1},\ldots,\bar{J}^{p}\|\_{\beta}^{2,(p)}.

Hence for β≥2​(p+2)2​(T+1)​C2\beta\geq 2(p+2)^{2}(T+1)C^{2} we have that 𝚽\mathbf{\Phi} is a (strict) contraction from ℋβ2,(p)\mathcal{H}\_{\beta}^{2,(p)} to ℋβ2,(p)\mathcal{H}\_{\beta}^{2,(p)} and thus admits a unique fixed point (Y,Z,K1,…,Kp)(Y,Z,K^{1},\ldots,K^{p}) in the Banach space ℋβ2,(p)\mathcal{H}\_{\beta}^{2,(p)}, which is the unique solution to the BSDE with driver g​(t,Yt,Zt,Kt1,…,Ktp)​d​t+d​Dtg(t,Y\_{t},Z\_{t},K\_{t}^{1},\ldots,K\_{t}^{p})dt+dD\_{t}, terminal time TT and terminal condition η∈L2​(𝒢T)\eta\in L^{2}(\mathcal{G}\_{T}).
∎

#### 2.2.3 Generalized λ(p)\lambda^{(p)}-Linear BSDEs with Multiple Default Jumps

We study the particular case of λ(p)\lambda^{(p)}-linear BSDEs with multiple default jumps.

###### Definition 2.10 (λ(p)\lambda^{(p)}-Linear Driver and Generalized λ(p)\lambda^{(p)}-Linear Driver):

A driver gg is λ(p)\lambda^{(p)}-linear if it is of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(t,y,z,k1,…,kp)=αt​y+βt​z+∑i=1pγti​ki​λti+δt,g(t,y,z,k^{1},\ldots,k^{p})=\alpha\_{t}y+\beta\_{t}z+\sum\_{i=1}^{p}\gamma\_{t}^{i}k^{i}\lambda\_{t}^{i}+\delta\_{t}, |  | (2.21) |

where δ≔(δt)t∈[0,T]∈ℋT2\delta\coloneqq(\delta\_{t})\_{t\in[0,T]}\in\mathcal{H}\_{T}^{2} and (αt)(\alpha\_{t}),(βt)(\beta\_{t}) and (γti)(\gamma\_{t}^{i}) for i∈{1,…,p}i\in\{1,\ldots,p\}, are ℝ\mathbb{R}-valued predictable processes such that (αt)(\alpha\_{t}),(βt)(\beta\_{t}) and (γti​λti)(\gamma\_{t}^{i}\sqrt{\lambda\_{t}^{i}}) for i∈{1,…,p}i\in\{1,\ldots,p\}, are bounded.
For D∈𝒜T2D\in\mathcal{A}\_{T}^{2} given, we define the generalized λ(p)\lambda^{(p)}-linear driver as,

|  |  |  |  |
| --- | --- | --- | --- |
|  | (αt​y+βt​z+∑i=1pγti​ki​λti)​d​t+d​Dt.(\alpha\_{t}y+\beta\_{t}z+\sum\_{i=1}^{p}\gamma\_{t}^{i}k^{i}\lambda\_{t}^{i})dt+dD\_{t}. |  | (2.22) |

###### Remark 2.11:

If gg is given by ([2.21](https://arxiv.org/html/2601.01250v1#S2.E21 "In Definition 2.10 (𝜆^(𝑝)-Linear Driver and Generalized 𝜆^(𝑝)-Linear Driver): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), then using the transformation νti≔γti​λti\nu\_{t}^{i}\coloneqq\gamma\_{t}^{i}\sqrt{\lambda\_{t}^{i}} for each i∈{1,…,p}i\in\{1,\ldots,p\}, we have that each (νi)(\nu^{i}) is a bounded predictable process and,

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(t,y,z,k1,…,kp)=αt​y+βt​z+∑i=1pνti​ki​λti+δt.g(t,y,z,k^{1},\ldots,k^{p})=\alpha\_{t}y+\beta\_{t}z+\sum\_{i=1}^{p}\nu\_{t}^{i}k^{i}\sqrt{\lambda\_{t}^{i}}+\delta\_{t}. |  | (2.23) |

Hence, a λ(p)\lambda^{(p)}-linear driver is also a λ(p)\lambda^{(p)}-admissible driver.

We are interested in finding explicitly the solution of a generalized λ(p)\lambda^{(p)}-linear BSDE. To do so, we first need a preliminary result on exponential local martingales in our framework.

###### Remark 2.12:

Let Γ≔(Γt)t∈[0,T]\Gamma\coloneqq(\Gamma\_{t})\_{t\in[0,T]} be the process satisfying the SDE,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Γs=Γs−​(βs​d​Ws+∑i=1pγsi​d​Msi),Γ0=1.d\Gamma\_{s}=\Gamma\_{s-}(\beta\_{s}dW\_{s}+\sum\_{i=1}^{p}\gamma\_{s}^{i}dM\_{s}^{i}),\quad\Gamma\_{0}=1. |  | (2.24) |

From Lemma [A.3](https://arxiv.org/html/2601.01250v1#A1.Thmtheorem3 "Lemma A.3: ‣ Appendix A Some Technical Lemmas ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), we have: for all s≥0s\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γs=exp⁡(∫0sβr​𝑑Wr−12​∫0sβr2​𝑑r)​exp⁡(−∫0s∑i=1pγri​λri​d​r)​∏i=1p(1+γτii​𝟙{s≥τi}), a.s.\Gamma\_{s}=\exp\left(\int\_{0}^{s}\beta\_{r}dW\_{r}-\frac{1}{2}\int\_{0}^{s}\beta\_{r}^{2}dr\right)\exp\left(-\int\_{0}^{s}\sum\_{i=1}^{p}\gamma\_{r}^{i}\lambda\_{r}^{i}dr\right)\prod\_{i=1}^{p}(1+\gamma\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{s\geq\tau\_{i}\}}),\text{ a.s.} |  | (2.25) |

If for all i∈{1,…,p}i\in\{1,\ldots,p\} γτii≥−1\gamma\_{\tau\_{i}}^{i}\geq-1 (respectively γτii>−1\gamma\_{\tau\_{i}}^{i}>-1) a.s., then Γs≥0\Gamma\_{s}\geq 0 (respectively Γs>0\Gamma\_{s}>0) for all s≥0s\geq 0 a.s.

###### Proposition 2.13:

Let T>0T>0. If the random variable ∫0T(βs2+∑i=1p(γsi)2​λsi)​𝑑s\int\_{0}^{T}(\beta\_{s}^{2}+\sum\_{i=1}^{p}(\gamma\_{s}^{i})^{2}\lambda\_{s}^{i})ds is bounded, then the exponential local martingale (Γt)t∈[0,T](\Gamma\_{t})\_{t\in[0,T]}, defined by ([2.24](https://arxiv.org/html/2601.01250v1#S2.E24 "In Remark 2.12: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), is a martingale and satisfies 𝔼​[sup0≤t≤TΓt2]<+∞\mathbb{E}[\sup\_{0\leq t\leq T}\Gamma\_{t}^{2}]<+\infty.

###### Proof.

From ([2.24](https://arxiv.org/html/2601.01250v1#S2.E24 "In Remark 2.12: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) the process Γ\Gamma is a local martingale. We show that 𝔼​[sup0≤t≤TΓt2]<∞\mathbb{E}[\sup\_{0\leq t\leq T}\Gamma\_{t}^{2}]<\infty. Let d​Xt=βt​d​Wt+∑i=1pγti​d​MtidX\_{t}=\beta\_{t}dW\_{t}+\sum\_{i=1}^{p}\gamma\_{t}^{i}dM\_{t}^{i}. We have 111For this, we use Δ​Γt=Γt−Γt−\Delta\Gamma\_{t}=\Gamma\_{t}-\Gamma\_{t-} and Γt=Γt−+Γt−​Δ​Xt\Gamma\_{t}=\Gamma\_{t-}+\Gamma\_{t-}\Delta X\_{t} ((by ([2.25](https://arxiv.org/html/2601.01250v1#S2.E25 "In Remark 2.12: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"))); we get Δ​Γt=Γt−​Δ​Xt\Delta\Gamma\_{t}=\Gamma\_{t-}\Delta X\_{t}. d​Γt=Γt−​d​Xtd\Gamma\_{t}=\Gamma\_{t-}dX\_{t} and Δ​Γt=Γt−​Δ​Xt\Delta\Gamma\_{t}=\Gamma\_{t-}\Delta X\_{t}. Using this, we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​[Γ]t\displaystyle d[\Gamma]\_{t} | =d​⟨Γc⟩t+d​(∑0<s≤t(Δ​Γs)2)=Γt−2​d​⟨Xc⟩t+d​(∑0<s≤tΓs−2​(Δ​Xs)2)\displaystyle=d\langle\Gamma^{c}\rangle\_{t}+d\left(\sum\_{0<s\leq t}(\Delta\Gamma\_{s})^{2}\right)=\Gamma\_{t-}^{2}d\langle X^{c}\rangle\_{t}+d\left(\sum\_{0<s\leq t}\Gamma\_{s-}^{2}(\Delta X\_{s})^{2}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Γt−2​βt2​d​t+d​(∑i=1p∫0tΓs−2​(γsi)2​𝑑Nsi)=Γt−2​βt2​d​t+Γt−2​∑i=1p(γti)2​d​Nti.\displaystyle=\Gamma\_{t-}^{2}\beta\_{t}^{2}dt+d\left(\sum\_{i=1}^{p}\int\_{0}^{t}\Gamma\_{s-}^{2}(\gamma\_{s}^{i})^{2}dN\_{s}^{i}\right)=\Gamma\_{t-}^{2}\beta\_{t}^{2}dt+\Gamma\_{t-}^{2}\sum\_{i=1}^{p}(\gamma\_{t}^{i})^{2}dN\_{t}^{i}. |  |

Using Itô’s formula applied to (Γt2)(\Gamma\_{t}^{2}) and the fact that d​Nti=d​Mti+λti​d​tdN\_{t}^{i}=dM\_{t}^{i}+\lambda\_{t}^{i}dt, we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Γt2=2​Γt−​d​Γt+d​[Γ]t=Γt−2​(2​βt​d​Wt+2​∑i=1pγti​d​Mti+βt2​d​t+∑i=1p(γti)2​d​Nti)=Γt−2​[2​βt​d​Wt+∑i=1p(2​γti+(γti)2)​d​Mti+(βt2+∑i=1p(γti)2​λti)​d​t].\displaystyle\begin{aligned} &d\Gamma\_{t}^{2}=2\Gamma\_{t-}d\Gamma\_{t}+d[\Gamma]\_{t}=\Gamma\_{t-}^{2}(2\beta\_{t}dW\_{t}+2\sum\_{i=1}^{p}\gamma\_{t}^{i}dM\_{t}^{i}+\beta\_{t}^{2}dt+\sum\_{i=1}^{p}(\gamma\_{t}^{i})^{2}dN\_{t}^{i})\\ &=\Gamma\_{t-}^{2}\left[2\beta\_{t}dW\_{t}+\sum\_{i=1}^{p}(2\gamma\_{t}^{i}+(\gamma\_{t}^{i})^{2})dM\_{t}^{i}+\left(\beta\_{t}^{2}+\sum\_{i=1}^{p}(\gamma\_{t}^{i})^{2}\lambda\_{t}^{i}\right)dt\right].\end{aligned} |  | (2.26) |

This can be written in the form d​Γt2=Γt−2​d​Ytd\Gamma\_{t}^{2}=\Gamma\_{t-}^{2}dY\_{t}, where,

|  |  |  |
| --- | --- | --- |
|  | d​Yt≔(βt2+∑i=1p(γti)2​λti)​d​t+2​βt​d​Wt+∑i=1p(2​γti+(γti)2)​d​Mti.dY\_{t}\coloneqq\left(\beta\_{t}^{2}+\sum\_{i=1}^{p}(\gamma\_{t}^{i})^{2}\lambda\_{t}^{i}\right)dt+2\beta\_{t}dW\_{t}+\sum\_{i=1}^{p}(2\gamma\_{t}^{i}+(\gamma\_{t}^{i})^{2})dM\_{t}^{i}. |  |

We have d​Yt≔d​Yt(1)+d​Yt(2)dY\_{t}\coloneqq dY\_{t}^{(1)}+dY\_{t}^{(2)}, where Yt(1)≔∫0t(βs2+∑i=1p(γsi)2​λsi)​𝑑sY\_{t}^{(1)}\coloneqq\int\_{0}^{t}\left(\beta\_{s}^{2}+\sum\_{i=1}^{p}(\gamma\_{s}^{i})^{2}\lambda\_{s}^{i}\right)ds and Yt(2)≔∫0t2​βs​𝑑Ws+∫0t∑i=1p(2​γsi+(γsi)2)​d​MsiY\_{t}^{(2)}\coloneqq\int\_{0}^{t}2\beta\_{s}dW\_{s}+\int\_{0}^{t}\sum\_{i=1}^{p}(2\gamma\_{s}^{i}+(\gamma\_{s}^{i})^{2})dM\_{s}^{i}. We have,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ​(Y(1))t=exp⁡(∫0t(βs2+∑i=1p(γsi)2​λsi)​𝑑s).\mathcal{E}(Y^{(1)})\_{t}=\exp\left(\int\_{0}^{t}\left(\beta\_{s}^{2}+\sum\_{i=1}^{p}(\gamma\_{s}^{i})^{2}\lambda\_{s}^{i}\right)ds\right). |  | (2.27) |

Using Lemma [A.3](https://arxiv.org/html/2601.01250v1#A1.Thmtheorem3 "Lemma A.3: ‣ Appendix A Some Technical Lemmas ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), applied to Y(2)Y^{(2)}, we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰ​(Y(2))t=exp⁡(∫0t2​βs​𝑑Ws−∫0t∑i=1p(2​γsi+(γsi)2)​λsi​d​s−∫0t2​βs2​𝑑s)×∏i=1p(1+(2γτii+(γτii)2)𝟙{τi≤t}).\mathcal{E}(Y^{(2)})\_{t}=\exp\left(\int\_{0}^{t}2\beta\_{s}dW\_{s}-\int\_{0}^{t}\sum\_{i=1}^{p}(2\gamma\_{s}^{i}+(\gamma\_{s}^{i})^{2})\lambda\_{s}^{i}ds-\int\_{0}^{t}2\beta\_{s}^{2}ds\right)\\ \times\prod\_{i=1}^{p}\left(1+(2\gamma\_{\tau\_{i}}^{i}+(\gamma\_{\tau\_{i}}^{i})^{2})\mathbbm{1}\_{\{\tau\_{i}\leq t\}}\right). |  | (2.28) |

Using the identity ℰ​(Y(1)+Y(2)+[Y(1),Y(2)])t=ℰ​(Y(1))t​ℰ​(Y(2))t\mathcal{E}(Y^{(1)}+Y^{(2)}+[Y^{(1)},Y^{(2)}])\_{t}=\mathcal{E}(Y^{(1)})\_{t}\mathcal{E}(Y^{(2)})\_{t} and the fact that [Y(1),Y(2)]t=0[Y^{(1)},Y^{(2)}]\_{t}=0 for all tt a.s. we get,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℰ​(Y(1))t​ℰ​(Y(2))t=Γt2\displaystyle\mathcal{E}(Y^{(1)})\_{t}\mathcal{E}(Y^{(2)})\_{t}=\Gamma\_{t}^{2} | =exp⁡(∫0t(βs2+∑i=1p(γsi)2​λsi)​𝑑s)\displaystyle=\exp\left(\int\_{0}^{t}\left(\beta\_{s}^{2}+\sum\_{i=1}^{p}(\gamma\_{s}^{i})^{2}\lambda\_{s}^{i}\right)ds\right) |  | (2.29) |
|  |  | ×exp⁡(∫0t2​βs​𝑑Ws−∫0t∑i=1p(2​γsi+(γsi)2)​λsi​d​s−∫0t2​βs2​𝑑s)\displaystyle\times\exp\left(\int\_{0}^{t}2\beta\_{s}dW\_{s}-\int\_{0}^{t}\sum\_{i=1}^{p}(2\gamma\_{s}^{i}+(\gamma\_{s}^{i})^{2})\lambda\_{s}^{i}ds-\int\_{0}^{t}2\beta\_{s}^{2}ds\right) |  |
|  |  | ×∏i=1p(1+(2γτii+(γτii)2)𝟙{τi≤t}).\displaystyle\times\prod\_{i=1}^{p}\left(1+(2\gamma\_{\tau\_{i}}^{i}+(\gamma\_{\tau\_{i}}^{i})^{2})\mathbbm{1}\_{\{\tau\_{i}\leq t\}}\right). |  |

Setting ζt≔ℰ​(Y(2))t\zeta\_{t}\coloneqq\mathcal{E}(Y^{(2)})\_{t}, we have that ζ\zeta is an exponential local martingale with dynamics, d​ζt=ζt−​d​Yt(2)d\zeta\_{t}=\zeta\_{t-}dY\_{t}^{(2)}; more specifically,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ζt=ζt−​[2​βt​d​Wt+∑i=1p(2​γti+(γti)2)​d​Mti],ζ0=1.d\zeta\_{t}=\zeta\_{t-}\left[2\beta\_{t}dW\_{t}+\sum\_{i=1}^{p}(2\gamma\_{t}^{i}+(\gamma\_{t}^{i})^{2})dM\_{t}^{i}\right],\quad\zeta\_{0}=1. |  | (2.30) |

Thus, the exponential local martingale Γ2\Gamma^{2} from ([2.29](https://arxiv.org/html/2601.01250v1#S2.E29 "In Proof. ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) becomes,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γt2=ζt​exp⁡(∫0t(βs2+∑i=1p(γsi)2​λsi)​𝑑s).\Gamma\_{t}^{2}=\zeta\_{t}\exp\left(\int\_{0}^{t}\left(\beta\_{s}^{2}+\sum\_{i=1}^{p}(\gamma\_{s}^{i})^{2}\lambda\_{s}^{i}\right)ds\right). |  | (2.31) |

By ([2.30](https://arxiv.org/html/2601.01250v1#S2.E30 "In Proof. ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), the local martingale ζ\zeta is non-negative. This implies that ζ\zeta is a supermartingale and hence 𝔼​[ζT]≤1\mathbb{E}[\zeta\_{T}]\leq 1. Now by the assumption that ∫0T(βt2+∑i=1p(γti)2​λti)​𝑑t\int\_{0}^{T}(\beta\_{t}^{2}+\sum\_{i=1}^{p}(\gamma\_{t}^{i})^{2}\lambda\_{t}^{i})dt is bounded, we get,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ΓT2]≤𝔼​[ζT]​K≤K,\mathbb{E}[\Gamma\_{T}^{2}]\leq\mathbb{E}[\zeta\_{T}]K\leq K, |  |

where K>0K>0 is a constant depending on ∫0T(βt2+∑i=1p(γti)2​λti)​𝑑t\int\_{0}^{T}(\beta\_{t}^{2}+\sum\_{i=1}^{p}(\gamma\_{t}^{i})^{2}\lambda\_{t}^{i})dt.
By martingale inequalities, we get 𝔼​[sup0≤t≤TΓt2]<∞\mathbb{E}[\sup\_{0\leq t\leq T}\Gamma\_{t}^{2}]<\infty. We conclude that Γ\Gamma is a martingale.
∎

We now establish the explicit form of the (first component of the solution) solution of the BSDE with a generalized λ(p)\lambda^{(p)}-linear driver. We begin with the case where the finite variational process DD is predictable.

###### Theorem 2.14 (Explicit Solution of the Generalized λ(p)\lambda^{(p)}-Linear BSDE with DD Predictable):

Let (αt)(\alpha\_{t}), (βt)(\beta\_{t}) and (γti)(\gamma\_{t}^{i}), for i∈{1,…,p}i\in\{1,\ldots,p\}, be ℝ\mathbb{R}-valued predictable processes such that (αt)(\alpha\_{t}), (βt)(\beta\_{t}) and (γti​λti)(\gamma\_{t}^{i}\sqrt{\lambda\_{t}^{i}}), for i∈{1,…,p}i\in\{1,\ldots,p\}, are bounded.
Let η∈L2​(𝒢T)\eta\in L^{2}(\mathcal{G}\_{T}) and let DD be a (predictable) process in 𝒜p,T2\mathcal{A}\_{p,T}^{2}.
Let (Y,Z,K1,…,Kp)(Y,Z,K^{1},\ldots,K^{p}) be the solution in 𝒮2×ℋ2×ℋλ12×⋯×ℋλp2\mathcal{S}^{2}\times\mathcal{H}^{2}\times\mathcal{H}\_{\lambda^{1}}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p}}^{2} of the following BSDE with the generalized λ(p)\lambda^{(p)}-linear driver (αt​y+βt​z+∑i=1pγti​ki​λti)​d​t+d​Dt(\alpha\_{t}y+\beta\_{t}z+\sum\_{i=1}^{p}\gamma\_{t}^{i}k^{i}\lambda\_{t}^{i})dt+dD\_{t}, terminal time TT and terminal condition η\eta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​Yt=(αt​Yt+βt​Zt+∑i=1pγti​Kti​λti)​d​t+d​Dt−Zt​d​Wt−∑i=1pKti​d​Mti,YT=η.-dY\_{t}=\left(\alpha\_{t}Y\_{t}+\beta\_{t}Z\_{t}+\sum\_{i=1}^{p}\gamma\_{t}^{i}K\_{t}^{i}\lambda\_{t}^{i}\right)dt+dD\_{t}-Z\_{t}dW\_{t}-\sum\_{i=1}^{p}K\_{t}^{i}dM\_{t}^{i},\quad Y\_{T}=\eta. |  | (2.32) |

For each t∈[0,T]t\in[0,T], let (Γt,s)s≥t(\Gamma\_{t,s})\_{s\geq t} be the unique solution of the following adjoint forward SDE,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Γt,s=Γt,s−​(αs​d​s+βs​d​Ws+∑i=1pγsi​d​Msi),Γt,t=1.d\Gamma\_{t,s}=\Gamma\_{t,s-}\left(\alpha\_{s}ds+\beta\_{s}dW\_{s}+\sum\_{i=1}^{p}\gamma\_{s}^{i}dM\_{s}^{i}\right),\quad\Gamma\_{t,t}=1. |  | (2.33) |

Then, the process (Yt)(Y\_{t}) has the explicit form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt=𝔼[Γt,Tη+∫tTΓt,s−dDs|𝒢t],0≤t≤T,a.s.Y\_{t}=\mathbb{E}\left[\Gamma\_{t,T}\eta+\int\_{t}^{T}\Gamma\_{t,s-}dD\_{s}\middle|\mathcal{G}\_{t}\right],\quad 0\leq t\leq T,\quad\text{a.s.} |  | (2.34) |

###### Remark 2.15:

Applying Lemma [A.3](https://arxiv.org/html/2601.01250v1#A1.Thmtheorem3 "Lemma A.3: ‣ Appendix A Some Technical Lemmas ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") to the process (Γt,s)s≥t(\Gamma\_{t,s})\_{s\geq t} gives that (Γt,s)s≥t(\Gamma\_{t,s})\_{s\geq t} satisfies,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γt,s=exp⁡(∫tsαr​𝑑r)​ℰ​(∫t.βr​𝑑Wr+∫t.∑i=1pγri​d​Mr)s=exp⁡(∫tsαr​𝑑r+∫tsβr​𝑑Wr−12​∫tsβr2​𝑑r−∑i=1pγri​λri​d​r)​∏i=1p(1+γτii​𝟙{t<τi≤s}),\displaystyle\begin{aligned} \Gamma\_{t,s}&=\exp\left(\int\_{t}^{s}\alpha\_{r}dr\right)\mathcal{E}\left(\int\_{t}^{.}\beta\_{r}dW\_{r}+\int\_{t}^{.}\sum\_{i=1}^{p}\gamma\_{r}^{i}dM\_{r}\right)\_{s}\\ &=\exp\left(\int\_{t}^{s}\alpha\_{r}dr+\int\_{t}^{s}\beta\_{r}dW\_{r}-\frac{1}{2}\int\_{t}^{s}\beta\_{r}^{2}dr-\sum\_{i=1}^{p}\gamma\_{r}^{i}\lambda\_{r}^{i}dr\right)\prod\_{i=1}^{p}(1+\gamma\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{t<\tau\_{i}\leq s\}}),\end{aligned} |  | (2.35) |

for all t≤s≤Tt\leq s\leq T a.s. The process (e∫tsαr​𝑑r)t≤s≤T(e^{\int\_{t}^{s}\alpha\_{r}dr})\_{t\leq s\leq T} is positive and bounded (as α\alpha is bounded), and using Proposition [2.13](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem13 "Proposition 2.13: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") (since β\beta and γi​λi\gamma^{i}\sqrt{\lambda^{i}} for each i∈{1,…,p}i\in\{1,\ldots,p\} are bounded), we have that (Γt,s)t≤s≤T(\Gamma\_{t,s})\_{t\leq s\leq T} is a martingale and satisfies 𝔼​[supt≤s≤TΓt,s2]<+∞\mathbb{E}[\sup\_{t\leq s\leq T}\Gamma\_{t,s}^{2}]<+\infty.

###### Proof.

Fix t∈[0,T]t\in[0,T]. Since D∈𝒜p,T2D\in\mathcal{A}\_{p,T}^{2} is *predictable* and the process Γt,.\Gamma\_{t,.} admits at most pp jumps and only at the *totally inaccessible* times τ1,…,τp\tau\_{1},\ldots,\tau\_{p}, we have that [Γt,.,D]s=0[\Gamma\_{t,.},D]\_{s}=0 for s≥ts\geq t a.s. By applying Itô’s product rule to (Ys​Γt,s)(Y\_{s}\Gamma\_{t,s}), we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​(Ys​Γt,s)=−Ys−​d​Γt,s−Γt,s−​d​Ys−d​[Y,Γt,.]s.-d(Y\_{s}\Gamma\_{t,s})=-Y\_{s-}d\Gamma\_{t,s}-\Gamma\_{t,s-}dY\_{s}-d[Y,\Gamma\_{t,.}]\_{s}. |  | (2.36) |

Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​[Y,Γt,.]s=d​[∫t⋅(αr​Yr+βr​Zr+∑i=1pγri​Kri​λri)​𝑑r,Γt,⋅]s+d​[D,Γt,⋅]s+d​[Z∙W,Γt,⋅]s+d​(∑i=1p[Ki∙Mi,Γt,⋅]s)=d​[D,Γt,⋅]s+d​[∫t⋅Zr​𝑑Wr,∫t⋅Γt,r−​βr​𝑑Wr]s+d​(∑i=1p∑j=1p[∫t⋅Kri​𝑑Mri,∫t⋅Γt,r−​γrj​𝑑Mrj]s)=d​(∫tsΓt,r−​βr​Zr​𝑑r)+d​(∫ts∑i=1p∑j=1pKri​Γt,r−​γrj​d​[Mi,Mj]r)=Γt,s−​βs​Zs​d​s+d​(∫ts∑i=1pΓt,r−​Kri​γri​d​Nri)=Γt,s−​βs​Zs​d​s+Γt,s−​∑i=1pKsi​γsi​d​Nsi,\displaystyle\begin{aligned} d[Y,\Gamma\_{t,.}]\_{s}&=d\left[\int\_{t}^{\cdot}\left(\alpha\_{r}Y\_{r}+\beta\_{r}Z\_{r}+\sum\_{i=1}^{p}\gamma\_{r}^{i}K\_{r}^{i}\lambda\_{r}^{i}\right)dr,\Gamma\_{t,\cdot}\right]\_{s}+d[D,\Gamma\_{t,\cdot}]\_{s}\\ &\quad\quad+d[Z\bullet W,\Gamma\_{t,\cdot}]\_{s}+d\left(\sum\_{i=1}^{p}[K^{i}\bullet M^{i},\Gamma\_{t,\cdot}]\_{s}\right)\\ &=d[D,\Gamma\_{t,\cdot}]\_{s}+d\left[\int\_{t}^{\cdot}Z\_{r}dW\_{r},\int\_{t}^{\cdot}\Gamma\_{t,r-}\beta\_{r}dW\_{r}\right]\_{s}\\ &\quad\quad+d\left(\sum\_{i=1}^{p}\sum\_{j=1}^{p}\left[\int\_{t}^{\cdot}K\_{r}^{i}dM\_{r}^{i},\int\_{t}^{\cdot}\Gamma\_{t,r-}\gamma\_{r}^{j}dM\_{r}^{j}\right]\_{s}\right)\\ &=d\left(\int\_{t}^{s}\Gamma\_{t,r-}\beta\_{r}Z\_{r}dr\right)+d\left(\int\_{t}^{s}\sum\_{i=1}^{p}\sum\_{j=1}^{p}K\_{r}^{i}\Gamma\_{t,r-}\gamma\_{r}^{j}d[M^{i},M^{j}]\_{r}\right)\\ &=\Gamma\_{t,s-}\beta\_{s}Z\_{s}ds+d\left(\int\_{t}^{s}\sum\_{i=1}^{p}\Gamma\_{t,r-}K\_{r}^{i}\gamma\_{r}^{i}dN\_{r}^{i}\right)\\ &=\Gamma\_{t,s-}\beta\_{s}Z\_{s}ds+\Gamma\_{t,s-}\sum\_{i=1}^{p}K\_{s}^{i}\gamma\_{s}^{i}dN\_{s}^{i},\end{aligned} |  | (2.37) |

where we have used that d​[Mi,Mj]s=0d[M^{i},M^{j}]\_{s}=0, for i≠ji\neq j, since P​(τi=τj)=0P(\tau\_{i}=\tau\_{j})=0, i≠ji\neq j, and, for the case i=ji=j, d​[Mi]s=d​Nsid[M^{i}]\_{s}=dN\_{s}^{i}.

Plugging ([2.37](https://arxiv.org/html/2601.01250v1#S2.E37 "In Proof. ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) into ([2.36](https://arxiv.org/html/2601.01250v1#S2.E36 "In Proof. ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) and using d​Nsi=d​Msi+λsi​d​sdN\_{s}^{i}=dM\_{s}^{i}+\lambda\_{s}^{i}ds, we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​(Ys​Γt,s)=−Γt,s−​(Ys​βs+Zs)​d​Ws−Γt,s−​(∑i=1p(Ys−​γsi+Ksi​(1+γsi))​d​Msi)+Γt,s−​d​Ds.-d(Y\_{s}\Gamma\_{t,s})=-\Gamma\_{t,s-}(Y\_{s}\beta\_{s}+Z\_{s})dW\_{s}-\Gamma\_{t,s-}\left(\sum\_{i=1}^{p}(Y\_{s-}\gamma\_{s}^{i}+K\_{s}^{i}(1+\gamma\_{s}^{i}))dM\_{s}^{i}\right)\\ +\Gamma\_{t,s-}dD\_{s}. |  | (2.38) |

Setting d​ms=Γt,s−​(Ys​βs+Zs)​d​Ws+Γt,s−​(∑i=1p(Ys−​γsi+Ksi​(1+γsi))​d​Msi)dm\_{s}=\Gamma\_{t,s-}(Y\_{s}\beta\_{s}+Z\_{s})dW\_{s}+\Gamma\_{t,s-}\left(\sum\_{i=1}^{p}(Y\_{s-}\gamma\_{s}^{i}+K\_{s}^{i}(1+\gamma\_{s}^{i}))dM\_{s}^{i}\right), we get −d​(Ys​Γt,s)=−d​ms+Γt,s−​d​Ds-d(Y\_{s}\Gamma\_{t,s})=-dm\_{s}+\Gamma\_{t,s-}dD\_{s}. Integrating between tt and TT, we derive,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt=η​Γt,T+∫tTΓt,s−​𝑑Ds−(mT−mt),a.s.Y\_{t}=\eta\Gamma\_{t,T}+\int\_{t}^{T}\Gamma\_{t,s-}dD\_{s}-(m\_{T}-m\_{t}),\quad\text{a.s.} |  | (2.39) |

By Remark [2.15](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem15 "Remark 2.15: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") we have (Γt,s)t≤s≤T∈𝒮2(\Gamma\_{t,s})\_{t\leq s\leq T}\in\mathcal{S}^{2}. Furthermore, Y∈𝒮2Y\in\mathcal{S}^{2}, Z∈ℋ2Z\in\mathcal{H}^{2} and Ki∈ℋλi2K^{i}\in\mathcal{H}\_{\lambda^{i}}^{2} for each i∈{1,…,p}i\in\{1,\ldots,p\}, and β\beta and γi​λi\gamma^{i}\sqrt{\lambda^{i}} for each i∈{1,…,p}i\in\{1,\ldots,p\} are bounded. It follows that the local martingale m=(ms)t≤s≤Tm=(m\_{s})\_{t\leq s\leq T} is a martingale. Taking the conditional expectation in ([2.39](https://arxiv.org/html/2601.01250v1#S2.E39 "In Proof. ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), we get the desired equality ([2.34](https://arxiv.org/html/2601.01250v1#S2.E34 "In Theorem 2.14 (Explicit Solution of the Generalized 𝜆^(𝑝)-Linear BSDE with 𝐷 Predictable): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")).
∎

We now consider the case where the process DD just an optional process (not necessarily predictable). More precisely, DD is in 𝒜T2\mathcal{A}\_{T}^{2}; hence, by Proposition [2.6](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem6 "Proposition 2.6: ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), it is of the form ([2.6](https://arxiv.org/html/2601.01250v1#S2.E6 "In Proposition 2.6: ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")).

###### Theorem 2.16 (Explicit Solution of the Generalized λ(p)\lambda^{(p)}-Linear BSDE with DD Optional):

Let the assumptions made in Theorem [2.14](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem14 "Theorem 2.14 (Explicit Solution of the Generalized 𝜆^(𝑝)-Linear BSDE with 𝐷 Predictable): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") all hold, except that DD is now in 𝒜T2\mathcal{A}\_{T}^{2} (and not necessarily in 𝒜p,T2\mathcal{A}\_{p,T}^{2}). Let D′∈𝒜p,T2D^{\prime}\in\mathcal{A}\_{p,T}^{2} and θi∈ℋλi,T2\theta^{i}\in\mathcal{H}\_{\lambda^{i},T}^{2}, for i∈{1,…,p}i\in\{1,\ldots,p\}, be the unique predictable processes from Proposition [2.6](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem6 "Proposition 2.6: ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), such that for all t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt=Dt′+∫0t∑i=1pθsi​d​Nsi, a.s.D\_{t}=D\_{t}^{\prime}+\int\_{0}^{t}\sum\_{i=1}^{p}\theta\_{s}^{i}dN\_{s}^{i},\text{ a.s.} |  | (2.40) |

Let (Y,Z,K1,…,Kp)(Y,Z,K^{1},\ldots,K^{p}) be the solution in 𝒮2×ℋ2×ℋλ12×⋯×ℋλp2\mathcal{S}^{2}\times\mathcal{H}^{2}\times\mathcal{H}\_{\lambda^{1}}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p}}^{2} of the BSDE with generalized λ(p)\lambda^{(p)}-linear driver (αt​y+βt​z+∑i=1pγti​ki​λti)​d​t+d​Dt(\alpha\_{t}y+\beta\_{t}z+\sum\_{i=1}^{p}\gamma\_{t}^{i}k^{i}\lambda\_{t}^{i})dt+dD\_{t}, terminal time TT, and terminal condition η∈L2​(𝒢T)\eta\in L^{2}({\mathcal{G}\_{T}}).

Then, a.s. for all t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt=𝔼[Γt,Tη+∫tTΓt,s−(dDs′+∑i=1pθsi(1+γsi)dNsi)|𝒢t]=𝔼[Γt,Tη+∫tTΓt,s−dDs′+∑i=1pΓt,τiθτii𝟙{t<τi≤T}|𝒢t],\displaystyle\begin{aligned} Y\_{t}&=\mathbb{E}\left[\Gamma\_{t,T}\eta+\int\_{t}^{T}\Gamma\_{t,s-}\left(dD\_{s}^{\prime}+\sum\_{i=1}^{p}\theta\_{s}^{i}(1+\gamma\_{s}^{i})dN\_{s}^{i}\right)\middle|\mathcal{G}\_{t}\right]\\ &=\mathbb{E}\left[\Gamma\_{t,T}\eta+\int\_{t}^{T}\Gamma\_{t,s-}dD\_{s}^{\prime}+\sum\_{i=1}^{p}\Gamma\_{t,\tau\_{i}}\theta\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{t<\tau\_{i}\leq T\}}\middle|\mathcal{G}\_{t}\right],\end{aligned} |  | (2.41) |

where the process (Γt,s)t≤s≤T(\Gamma\_{t,s})\_{t\leq s\leq T} is the solution of the adjoint forward SDE ([2.35](https://arxiv.org/html/2601.01250v1#S2.E35 "In Remark 2.15: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")).

###### Proof.

Since DD satisfies ([2.40](https://arxiv.org/html/2601.01250v1#S2.E40 "In Theorem 2.16 (Explicit Solution of the Generalized 𝜆^(𝑝)-Linear BSDE with 𝐷 Optional): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), we have,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​[D,Γt,⋅]s=d​[D′,Γt,⋅]s+d​(∑i=1p∑j=1p[∫t⋅θri​𝑑Nri,∫t⋅Γt,r−​γrj​𝑑Nrj]s)=d​(∫tsΓt,r−​∑i=1pθri​γri​d​Nri)=Γt,s−​∑i=1pθsi​γsi​d​Nsia.s.,\displaystyle\begin{aligned} d[D,\Gamma\_{t,\cdot}]\_{s}&=d[D^{\prime},\Gamma\_{t,\cdot}]\_{s}+d\left(\sum\_{i=1}^{p}\sum\_{j=1}^{p}\left[\int\_{t}^{\cdot}\theta\_{r}^{i}dN\_{r}^{i},\int\_{t}^{\cdot}\Gamma\_{t,r-}\gamma\_{r}^{j}dN\_{r}^{j}\right]\_{s}\right)\\ &=d\left(\int\_{t}^{s}\Gamma\_{t,r-}\sum\_{i=1}^{p}\theta\_{r}^{i}\gamma\_{r}^{i}dN\_{r}^{i}\right)=\Gamma\_{t,s-}\sum\_{i=1}^{p}\theta\_{s}^{i}\gamma\_{s}^{i}dN\_{s}^{i}\quad\text{a.s.},\end{aligned} |  | (2.42) |

where we have used that τi≠τj\tau\_{i}\neq\tau\_{j} a.s. for i≠j.i\neq j.
By applying Itô’s product rule to (Ys​Γt,s)(Y\_{s}\Gamma\_{t,s}), using similar computations to those from the proof of Theorem [2.14](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem14 "Theorem 2.14 (Explicit Solution of the Generalized 𝜆^(𝑝)-Linear BSDE with 𝐷 Predictable): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), and using ([2.42](https://arxiv.org/html/2601.01250v1#S2.E42 "In Proof. ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​(Ys​Γt,s)=−Γt,s−​(Ys​βs+Zs)​d​Ws−Γt,s−​(∑i=1p(Ys−​γsi+Ksi​(1+γsi))​d​Msi)−Γt,s−​(d​Ds+∑i=1pθsi​γsi​d​Nsi).-d(Y\_{s}\Gamma\_{t,s})=-\Gamma\_{t,s-}(Y\_{s}\beta\_{s}+Z\_{s})dW\_{s}-\Gamma\_{t,s-}\left(\sum\_{i=1}^{p}(Y\_{s-}\gamma\_{s}^{i}+K\_{s}^{i}(1+\gamma\_{s}^{i}))dM\_{s}^{i}\right)\\ -\Gamma\_{t,s-}\left(dD\_{s}+\sum\_{i=1}^{p}\theta\_{s}^{i}\gamma\_{s}^{i}dN\_{s}^{i}\right). |  | (2.43) |

Using Γt,s−​(d​Ds+∑i=1pθsi​γsi​d​Nsi)=Γt,s−​(d​Ds′+∑i=1pθsi​(1+γsi)​d​Nsi)\Gamma\_{t,s-}(dD\_{s}+\sum\_{i=1}^{p}\theta\_{s}^{i}\gamma\_{s}^{i}dN\_{s}^{i})=\Gamma\_{t,s-}(dD\_{s}^{\prime}+\sum\_{i=1}^{p}\theta\_{s}^{i}(1+\gamma\_{s}^{i})dN\_{s}^{i}) in ([2.43](https://arxiv.org/html/2601.01250v1#S2.E43 "In Proof. ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), integrating from tt to TT and taking the conditional expectation, we derive that,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt=𝔼[Γt,Tη+∫tTΓt,s−(dDs′+∑i=1pθsi(1+γsi)dNsi)|𝒢t],Y\_{t}=\mathbb{E}\left[\Gamma\_{t,T}\eta+\int\_{t}^{T}\Gamma\_{t,s-}\left(dD\_{s}^{\prime}+\sum\_{i=1}^{p}\theta\_{s}^{i}(1+\gamma\_{s}^{i})dN\_{s}^{i}\right)\middle|\mathcal{G}\_{t}\right], |  | (2.44) |

which is the first equality from ([2.41](https://arxiv.org/html/2601.01250v1#S2.E41 "In Theorem 2.16 (Explicit Solution of the Generalized 𝜆^(𝑝)-Linear BSDE with 𝐷 Optional): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")).

Now, we have,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[∫tTΓt,s−∑i=1pθsi(1+γsi)dNsi|𝒢t]=𝔼[∑i=1pΓt,τi−θτii(1+γτii)𝟙{t<τi≤T}|𝒢t]=𝔼[∑i=1pΓt,τiθτii𝟙{t<τi≤T}|𝒢t].\displaystyle\begin{aligned} \mathbb{E}\left[\int\_{t}^{T}\Gamma\_{t,s-}\sum\_{i=1}^{p}\theta\_{s}^{i}(1+\gamma\_{s}^{i})dN\_{s}^{i}\middle|\mathcal{G}\_{t}\right]&=\mathbb{E}\left[\sum\_{i=1}^{p}\Gamma\_{t,\tau\_{i}-}\theta\_{\tau\_{i}}^{i}(1+\gamma\_{\tau\_{i}}^{i})\mathbbm{1}\_{\{t<\tau\_{i}\leq T\}}\middle|\mathcal{G}\_{t}\right]\\ &=\mathbb{E}\left[\sum\_{i=1}^{p}\Gamma\_{t,\tau\_{i}}\theta\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{t<\tau\_{i}\leq T\}}\middle|\mathcal{G}\_{t}\right].\end{aligned} |  | (2.45) |

The second equality in ([2.45](https://arxiv.org/html/2601.01250v1#S2.E45 "In Proof. ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) is due to Γt,s\Gamma\_{t,s} having the following representation,

|  |  |  |
| --- | --- | --- |
|  | Γt,s=exp⁡(∫ts(αr−12​βr2−∑i=1pγri​λri)​𝑑r+∫tsβr​𝑑Wr)​∏i=1p(1+γτii​𝟙{t<τi≤s}),\displaystyle\Gamma\_{t,s}=\exp\left(\int\_{t}^{s}\left(\alpha\_{r}-\frac{1}{2}\beta\_{r}^{2}-\sum\_{i=1}^{p}\gamma\_{r}^{i}\lambda\_{r}^{i}\right)dr+\int\_{t}^{s}\beta\_{r}dW\_{r}\right)\prod\_{i=1}^{p}(1+\gamma\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{t<\tau\_{i}\leq s\}}), |  |

for all t≤s≤Tt\leq s\leq T a.s.; it follows that, for each i∈{1,…,p},i\in\{1,\ldots,p\}, Γt,τi−​(1+γτii)​𝟙{t<τi≤T}=Γt,τi​𝟙{t<τi≤T}\Gamma\_{t,\tau\_{i}-}(1+\gamma\_{\tau\_{i}}^{i})\mathbbm{1}\_{\{t<\tau\_{i}\leq T\}}=\Gamma\_{t,\tau\_{i}}\mathbbm{1}\_{\{t<\tau\_{i}\leq T\}} (where we have used that τ1<τ2<…<τp\tau\_{1}<\tau\_{2}<...<\tau\_{p}).

By replacing ([2.45](https://arxiv.org/html/2601.01250v1#S2.E45 "In Proof. ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) in ([2.44](https://arxiv.org/html/2601.01250v1#S2.E44 "In Proof. ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), we get the following representation,

|  |  |  |
| --- | --- | --- |
|  | Yt=𝔼[Γt,Tη+∫tTΓt,s−dDs′+∑i=1pΓt,τiθτii𝟙{t<τi≤T}|𝒢t],Y\_{t}=\mathbb{E}\left[\Gamma\_{t,T}\eta+\int\_{t}^{T}\Gamma\_{t,s-}dD\_{s}^{\prime}+\sum\_{i=1}^{p}\Gamma\_{t,\tau\_{i}}\theta\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{t<\tau\_{i}\leq T\}}\middle|\mathcal{G}\_{t}\right], |  |

which is the second equality in ([2.41](https://arxiv.org/html/2601.01250v1#S2.E41 "In Theorem 2.16 (Explicit Solution of the Generalized 𝜆^(𝑝)-Linear BSDE with 𝐷 Optional): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")).
∎

### 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps

We now provide a comparison and a strict comparison results for BSDEs with generalized λ(p)\lambda^{(p)}-admissible drivers associated with finite variational rcll adapted processes in 𝒜T2\mathcal{A}\_{T}^{2}.
  
For convenience, we define the following sets:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | A0:={τ1>T},A1:={τ1≤T,τ2>T},…,Ak:={τk≤T,τk+1>T},…,\displaystyle A\_{0}=\{\tau\_{1}>T\},A\_{1}=\{\tau\_{1}\leq T,\tau\_{2}>T\},.,A\_{k}=\{\tau\_{k}\leq T,\tau\_{k+1}>T\},., |  | (2.46) |
|  |  | Ap−1:={τp−1≤T,τp>T}, and ​Ap:={τp≤T}.\displaystyle A\_{p-1}=\{\tau\_{p-1}\leq T,\tau\_{p}>T\},\text{ and }A\_{p}=\{\tau\_{p}\leq T\}. |  |

As τ1<τ2<…<τp\tau\_{1}<\tau\_{2}<...<\tau\_{p}, the above sets form a partition of Ω\Omega.

###### Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps):

Let η\eta and η^\hat{\eta} be in L2​(𝒢T)L^{2}(\mathcal{G}\_{T}). Let gg and g^\hat{g} be λ(p)\lambda^{(p)}-admissible drivers. Let DD and D^\hat{D} be processes in 𝒜T2\mathcal{A}\_{T}^{2}. Let (Y,Z,K1,…,Kp)(Y,Z,K^{1},\ldots,K^{p}) be the solution in 𝒮2×ℋT2×ℋλ1,T2×⋯×ℋλp,T2\mathcal{S}^{2}\times\mathcal{H}\_{T}^{2}\times\mathcal{H}\_{\lambda^{1},T}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p},T}^{2} to the BSDE,

|  |  |  |
| --- | --- | --- |
|  | −d​Yt=g​(t,Yt,Zt,Kt1,…,Ktp)​d​t+d​Dt−Zt​d​Wt−∑i=1pKti​d​Mti,YT=η.-dY\_{t}=g(t,Y\_{t},Z\_{t},K\_{t}^{1},\ldots,K\_{t}^{p})dt+dD\_{t}-Z\_{t}dW\_{t}-\sum\_{i=1}^{p}K\_{t}^{i}dM\_{t}^{i},\quad Y\_{T}=\eta. |  |

Let (Y^,Z^,K^1,…,K^p)(\hat{Y},\hat{Z},\hat{K}^{1},\ldots,\hat{K}^{p}) be the solution in 𝒮2×ℋT2×ℋλ1,T2×⋯×ℋλp,T2\mathcal{S}^{2}\times\mathcal{H}\_{T}^{2}\times\mathcal{H}\_{\lambda^{1},T}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p},T}^{2} to the BSDE,

|  |  |  |
| --- | --- | --- |
|  | −d​Y^t=g^​(t,Y^t,Z^t,K^t1,…,K^tp)​d​t+d​D^t−Z^t​d​Wt−∑i=1pK^ti​d​Mti,Y^T=η^.-d\hat{Y}\_{t}=\hat{g}(t,\hat{Y}\_{t},\hat{Z}\_{t},\hat{K}\_{t}^{1},\ldots,\hat{K}\_{t}^{p})dt+d\hat{D}\_{t}-\hat{Z}\_{t}dW\_{t}-\sum\_{i=1}^{p}\hat{K}\_{t}^{i}dM\_{t}^{i},\quad\hat{Y}\_{T}=\hat{\eta}. |  |

Then, the following two statements hold true:

1. (i)

   Comparison: Assume that there exist pp predictable processes (γti)(\gamma\_{t}^{i}) (where i∈{1,…,p}i\in\{1,\ldots,p\}) with (γti​λti)​ bounded ​d​P⊗d​t(\gamma\_{t}^{i}\sqrt{\lambda\_{t}^{i}})\text{ bounded }dP\otimes dt -a.e. (for i∈{1,…,p}i\in\{1,\ldots,p\}) such that,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | for each ​k∈{1,…,p}, on ​Ak,1+γτii≥0​ a.s. for all ​i∈{1,…,k},\text{ for each }k\in\{1,...,p\},\text{ on }A\_{k},1+\gamma\_{\tau\_{i}}^{i}\geq 0\text{ a.s. for all }i\in\{1,...,k\}, |  | (2.47) |

   and such that,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | g​(t,Y^t,Z^t,Kt1,…,Ktp)−g​(t,Y^t,Z^t,K^t1,…,K^tp)≥∑i=1pγti​(Kti−K^ti)​λtig(t,\hat{Y}\_{t},\hat{Z}\_{t},K\_{t}^{1},\ldots,K\_{t}^{p})-g(t,\hat{Y}\_{t},\hat{Z}\_{t},\hat{K}\_{t}^{1},\ldots,\hat{K}\_{t}^{p})\geq\sum\_{i=1}^{p}\gamma\_{t}^{i}(K\_{t}^{i}-\hat{K}\_{t}^{i})\lambda\_{t}^{i} |  | (2.48) |

   for t∈[0,T]t\in[0,T], d​P⊗d​tdP\otimes dt-a.e. Suppose that η≥η^\eta\geq\hat{\eta} a.s. that D¯≔D−D^\bar{D}\coloneqq D-\hat{D} is non-decreasing, and that

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | g​(t,Y^t,Z^t,K^t1,…,K^tp)≥g^​(t,Y^t,Z^t,K^t1,…,K^tp)g(t,\hat{Y}\_{t},\hat{Z}\_{t},\hat{K}\_{t}^{1},\ldots,\hat{K}\_{t}^{p})\geq\hat{g}(t,\hat{Y}\_{t},\hat{Z}\_{t},\hat{K}\_{t}^{1},\ldots,\hat{K}\_{t}^{p}) |  | (2.49) |

   for t∈[0,T]t\in[0,T], d​P⊗d​tdP\otimes dt-a.e.
   We then have Yt≥Y^tY\_{t}\geq\hat{Y}\_{t} for all t∈[0,T]t\in[0,T] a.s.
2. (ii)

   Strict Comparison: Assume moreover that γτii>−1\gamma\_{\tau\_{i}}^{i}>-1 a.s. for each i∈{1,…,p}i\in\{1,\ldots,p\} and that there exists t0∈[0,T]t\_{0}\in[0,T] such that Yt0=Y^t0Y\_{t\_{0}}=\hat{Y}\_{t\_{0}} a.s. Then, η=η^\eta=\hat{\eta} a.s. and the inequality in ([2.49](https://arxiv.org/html/2601.01250v1#S2.E49 "In item (i) ‣ Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) is an equality on [t0,T][t\_{0},T]. Furthermore, D¯≔D−D^\bar{D}\coloneqq D-\hat{D} is constant on [t0,T][t\_{0},T] and Y=Y^Y=\hat{Y} on [t0,T][t\_{0},T].

###### Remark 2.18:

Due to the assumption τ1<τ2<…<τp\tau\_{1}<\tau\_{2}<...<\tau\_{p}, the condition from Eq. ([2.47](https://arxiv.org/html/2601.01250v1#S2.E47 "In item (i) ‣ Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), namely, for each k∈{1,…,p}k\in\{1,...,p\}, on Ak,1+γτii≥0A\_{k},1+\gamma\_{\tau\_{i}}^{i}\geq 0 a.s. for all i∈{1,…,k}i\in\{1,...,k\}, is equivalent, in our framework, to the condition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | for all ​t∈[0,T],∏i=1p(1+γτii​𝟙{t<τi≤s})≥0, for all ​s∈[t,T], a.s.,\text{ for all }t\in[0,T],\prod\_{i=1}^{p}(1+\gamma\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{t<\tau\_{i}\leq s\}})\geq 0,\text{ for all }s\in[t,T],\text{ a.s.}, |  | (2.50) |

which ensures the non-negativity of the adjoint process (Γt,⋅)(\Gamma\_{t,\cdot}) in the proof of the comparison theorem. To show the equivalence between the two conditions, we proceed as follows: Let the condition from Eq.([2.50](https://arxiv.org/html/2601.01250v1#S2.E50 "In Remark 2.18: ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) hold. Let us take t=0 in this condition, and let k∈{1,…,p}k\in\{1,...,p\}. Let us place ourselves on the set AkA\_{k}: taking successively s=τ1​(ω)s=\tau\_{1}(\omega), s=τ2​(ω)s=\tau\_{2}(\omega),…, s=τk​(ω)s=\tau\_{k}(\omega) in Eq.([2.50](https://arxiv.org/html/2601.01250v1#S2.E50 "In Remark 2.18: ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) (and using that τ1<τ2<…<τp\tau\_{1}<\tau\_{2}<...<\tau\_{p}), we get, 1+γτ1​(ω)1​(ω)≥01+\gamma^{1}\_{\tau\_{1}(\omega)}(\omega)\geq 0, …, 1+γτk​(ω)k​(ω)≥01+\gamma^{k}\_{\tau\_{k}(\omega)}(\omega)\geq 0 on AkA\_{k}. Conversely, let the condition from Eq. ([2.47](https://arxiv.org/html/2601.01250v1#S2.E47 "In item (i) ‣ Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) hold true. For t∈[0,T]t\in[0,T], for s∈[t,T]s\in[t,T], we have ∏i=1p(1+γτii​𝟙{t<τi≤s})=∑k=0p𝟙Ak​(∏i=1p(1+γτii​𝟙{t<τi≤s})).\prod\_{i=1}^{p}(1+\gamma\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{t<\tau\_{i}\leq s\}})=\sum\_{k=0}^{p}\mathbbm{1}\_{A\_{k}}(\prod\_{i=1}^{p}(1+\gamma\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{t<\tau\_{i}\leq s\}})). Let k∈{1,…,p−1}.k\in\{1,...,p-1\}. We consider the set Ak∩{t<τi≤s}={τk≤T,τk+1>T}∩{t<τi≤s}A\_{k}\cap\{t<\tau\_{i}\leq s\}=\{\tau\_{k}\leq T,\tau\_{k+1}>T\}\cap\{t<\tau\_{i}\leq s\}: for each ii such that 1≤i≤k1\leq i\leq k, it holds γτii≥−1\gamma\_{\tau\_{i}}^{i}\geq-1 on Ak∩{t<τi≤s}A\_{k}\cap\{t<\tau\_{i}\leq s\} (by condition ([2.47](https://arxiv.org/html/2601.01250v1#S2.E47 "In item (i) ‣ Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"))); for i≥k+1i\geq k+1, Ak∩{t<τi≤s}=∅A\_{k}\cap\{t<\tau\_{i}\leq s\}=\varnothing (as τk+1>T\tau\_{k+1}>T on AkA\_{k} and as the τi\tau\_{i}’s are strictly ordered). On ApA\_{p}, γτii≥−1,\gamma\_{\tau\_{i}}^{i}\geq-1, for each i∈{1,…,p}.i\in\{1,...,p\}. Finally, we note that A0∩{t<τi≤s}=∅A\_{0}\cap\{t<\tau\_{i}\leq s\}=\varnothing, for each i∈{1,…,p}i\in\{1,...,p\} (as τ1>T\tau\_{1}>T on A0A\_{0}). We conclude that, for t∈[0,T]t\in[0,T], for s∈[t,T]s\in[t,T], ∏i=1p(1+γτii​𝟙{t<τi≤s})≥0.\prod\_{i=1}^{p}(1+\gamma\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{t<\tau\_{i}\leq s\}})\geq 0.

###### Remark 2.19:

Assume that γτii≥−1\gamma\_{\tau\_{i}}^{i}\geq-1 a.s. for each i∈{1,…,p}i\in\{1,\ldots,p\}. This implies that the condition: for each k∈{1,…,p}k\in\{1,...,p\}, on AkA\_{k}, 1+γτii≥01+\gamma\_{\tau\_{i}}^{i}\geq 0 a.s. for all i∈{1,…,k}i\in\{1,...,k\}, from Eq. ([2.47](https://arxiv.org/html/2601.01250v1#S2.E47 "In item (i) ‣ Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) is satisfied. If, moreover, γτii>−1\gamma\_{\tau\_{i}}^{i}>-1 a.s. for each i∈{1,…,p}i\in\{1,\ldots,p\}, then the condition from the strict comparison (ii) is also satisfied.

###### Proof.

Setting Y¯s≔Ys−Y^s\bar{Y}\_{s}\coloneqq Y\_{s}-\hat{Y}\_{s}, Z¯s≔Zs−Z^s\bar{Z}\_{s}\coloneqq Z\_{s}-\hat{Z}\_{s} and K¯si≔Ksi−K^si\bar{K}\_{s}^{i}\coloneqq K\_{s}^{i}-\hat{K}\_{s}^{i}, for each i∈{1,…,p}i\in\{1,\ldots,p\}, we have,

|  |  |  |
| --- | --- | --- |
|  | −d​Y¯s=hs​d​s+d​D¯s−Z¯s​d​Ws−∑i=1pK¯si​d​Msi,Y¯T=η−η^,-d\bar{Y}\_{s}=h\_{s}ds+d\bar{D}\_{s}-\bar{Z}\_{s}dW\_{s}-\sum\_{i=1}^{p}\bar{K}\_{s}^{i}dM\_{s}^{i},\quad\bar{Y}\_{T}=\eta-\hat{\eta}, |  |

where,

|  |  |  |  |
| --- | --- | --- | --- |
|  | hs≔g​(s,Ys−,Zs,Ks1,…,Ksp)−g^​(s,Y^s−,Z^s,K^s1,…,K^sp).h\_{s}\coloneqq g(s,Y\_{s-},Z\_{s},K\_{s}^{1},\ldots,K\_{s}^{p})-\hat{g}(s,\hat{Y}\_{s-},\hat{Z}\_{s},\hat{K}\_{s}^{1},\ldots,\hat{K}\_{s}^{p}). |  | (2.51) |

We set,

|  |  |  |  |
| --- | --- | --- | --- |
|  | δs≔g​(s,Ys−,Zs,Ks1,…,Ksp)−g​(s,Y^s−,Zs,Ks1,…,Ksp)Y¯s−​𝟙{Y¯s−≠0},βs≔g​(s,Y^s−,Zs,Ks1,…,Ksp)−g​(s,Y^s−,Z^s,Ks1,…,Ksp)Z¯s​𝟙{Z¯s≠0}.\displaystyle\begin{aligned} \delta\_{s}&\coloneqq\frac{g(s,Y\_{s-},Z\_{s},K\_{s}^{1},\ldots,K\_{s}^{p})-g(s,\hat{Y}\_{s-},Z\_{s},K\_{s}^{1},\ldots,K\_{s}^{p})}{\bar{Y}\_{s-}}\mathbbm{1}\_{\{\bar{Y}\_{s-}\neq 0\}},\\ \beta\_{s}&\coloneqq\frac{g(s,\hat{Y}\_{s-},Z\_{s},K\_{s}^{1},\ldots,K\_{s}^{p})-g(s,\hat{Y}\_{s-},\hat{Z}\_{s},K\_{s}^{1},\ldots,K\_{s}^{p})}{\bar{Z}\_{s}}\mathbbm{1}\_{\{\bar{Z}\_{s}\neq 0\}}.\end{aligned} |  | (2.52) |

By definition both δ\delta and β\beta are predictable. Furthermore, since gg is a λ(p)\lambda^{(p)}-admissible driver, it satisfies,

|  |  |  |
| --- | --- | --- |
|  | |g​(ω,t,y,z,k1,…,kp)−g​(ω,t,y^,z^,k^1,…,k^p)|≤C​(|y−y^|+|z−z^|+∑i=1pλti​(ω)​|ki−k^i|);|g(\omega,t,y,z,k^{1},\ldots,k^{p})-g(\omega,t,\hat{y},\hat{z},\hat{k}^{1},\ldots,\hat{k}^{p})|\\ \leq C\left(|y-\hat{y}|+|z-\hat{z}|+\sum\_{i=1}^{p}\sqrt{\lambda\_{t}^{i}(\omega)}|k^{i}-\hat{k}^{i}|\right); |  |

hence, the processes δ\delta and β\beta are bounded. With the above notation,

|  |  |  |
| --- | --- | --- |
|  | hs=δs​Y¯s−+βs​Z¯s+g​(s,Y^s−,Z^s,Ks1,…,Ksp)−g​(s,Y^s−,Z^s,K^s1,…,K^sp)+φs,h\_{s}=\delta\_{s}\bar{Y}\_{s-}+\beta\_{s}\bar{Z}\_{s}+g(s,\hat{Y}\_{s-},\hat{Z}\_{s},K\_{s}^{1},\ldots,K\_{s}^{p})-g(s,\hat{Y}\_{s-},\hat{Z}\_{s},\hat{K}\_{s}^{1},\ldots,\hat{K}\_{s}^{p})+\varphi\_{s}, |  |

where,

|  |  |  |  |
| --- | --- | --- | --- |
|  | φs≔g​(s,Y^s−,Z^s,K^s1,…,K^sp)−g^​(s,Y^s−,Z^s,K^s1,…,K^sp).\varphi\_{s}\coloneqq g(s,\hat{Y}\_{s-},\hat{Z}\_{s},\hat{K}\_{s}^{1},\ldots,\hat{K}\_{s}^{p})-\hat{g}(s,\hat{Y}\_{s-},\hat{Z}\_{s},\hat{K}\_{s}^{1},\ldots,\hat{K}\_{s}^{p}). |  | (2.53) |

Due to assumption ([2.48](https://arxiv.org/html/2601.01250v1#S2.E48 "In item (i) ‣ Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) and due to the fact that Yt=Yt−Y\_{t}=Y\_{t-} d​P⊗d​tdP\otimes dt-a.e.222This is true as Yt​(ω)Y\_{t}(\omega) has at most a countable number of jumps., we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | hs≥δs​Y¯s+βs​Z¯s+∑i=1pγsi​K¯si​λsi+φs,d​P⊗d​s​-a.e.h\_{s}\geq\delta\_{s}\bar{Y}\_{s}+\beta\_{s}\bar{Z}\_{s}+\sum\_{i=1}^{p}\gamma\_{s}^{i}\bar{K}\_{s}^{i}\lambda\_{s}^{i}+\varphi\_{s},\quad dP\otimes ds\text{-a.e.} |  | (2.54) |

We fix t∈[0,T]t\in[0,T]. Let Γt,.\Gamma\_{t,.} be the adjoint process, defined by,

|  |  |  |
| --- | --- | --- |
|  | d​Γt,s=Γt,s−​(δs​d​s+βs​d​Ws+∑i=1pγsi​d​Msi),Γt,t=1.d\Gamma\_{t,s}=\Gamma\_{t,s-}\left(\delta\_{s}ds+\beta\_{s}dW\_{s}+\sum\_{i=1}^{p}\gamma\_{s}^{i}dM\_{s}^{i}\right),\quad\Gamma\_{t,t}=1. |  |

As δ\delta, β\beta and γi​λi\gamma^{i}\sqrt{\lambda^{i}} for each i∈{1,…,p}i\in\{1,\ldots,p\} are bounded, we have that Γt,⋅∈𝒮2\Gamma\_{t,\cdot}\in\mathcal{S}^{2} by Remark [2.15](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem15 "Remark 2.15: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"). Due to the condition from Eq. ([2.47](https://arxiv.org/html/2601.01250v1#S2.E47 "In item (i) ‣ Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), to Equation ([2.35](https://arxiv.org/html/2601.01250v1#S2.E35 "In Remark 2.15: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) and to Remark [2.18](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem18 "Remark 2.18: ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), we have Γt,s≥0\Gamma\_{t,s}\geq 0 for all t≤s≤Tt\leq s\leq T a.s.

Step 1.  We consider first the case where DD and D^\hat{D} are (predictable) processes in 𝒜p,T2\mathcal{A}\_{p,T}^{2}, and prove the comparison and the strict comparison results in this case.
  
By applying Itô’s product rule to (Y¯s​Γt,s)(\bar{Y}\_{s}\Gamma\_{t,s}), we get, −d​(Y¯s​Γt,s)=−Y¯s−​d​Γt,s−Γt,s−​d​Y¯s−d​[Y¯,Γt,⋅]s-d(\bar{Y}\_{s}\Gamma\_{t,s})=-\bar{Y}\_{s-}d\Gamma\_{t,s}-\Gamma\_{t,s-}d\bar{Y}\_{s}-d[\bar{Y},\Gamma\_{t,\cdot}]\_{s}. We have,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​[Y¯,Γt,⋅]s=d​[∫t⋅Z¯r​𝑑Wr,∫t⋅Γt,r−​βr​𝑑Wr]s+d​(∑i=1p∑j=1p[∫t⋅K¯ri​𝑑Mri,∫t⋅Γt,r−​γrj​𝑑Mrj]s)=Γt,s−​βs​Z¯s​d​s+(∫ts∑i=1p∑j=1pK¯ri​Γt,r−​γrj​d​[Mi,Mj]r)=Γt,s−​βs​Z¯s​d​s+d​(∫tsΓt,r−​∑i=1pK¯ri​γri​d​Nri)=Γt,s−​βs​Z¯s​d​s+Γt,s−​∑i=1pK¯si​γsi​λsi​d​s+Γt,s−​∑i=1pK¯si​γsi​d​Msi,\displaystyle\begin{aligned} d[\bar{Y},\Gamma\_{t,\cdot}]\_{s}&=d\left[\int\_{t}^{\cdot}\bar{Z}\_{r}dW\_{r},\int\_{t}^{\cdot}\Gamma\_{t,r-}\beta\_{r}dW\_{r}\right]\_{s}+d\left(\sum\_{i=1}^{p}\sum\_{j=1}^{p}\left[\int\_{t}^{\cdot}\bar{K}\_{r}^{i}dM\_{r}^{i},\int\_{t}^{\cdot}\Gamma\_{t,r-}\gamma\_{r}^{j}dM\_{r}^{j}\right]\_{s}\right)\\ &=\Gamma\_{t,s-}\beta\_{s}\bar{Z}\_{s}ds+\left(\int\_{t}^{s}\sum\_{i=1}^{p}\sum\_{j=1}^{p}\bar{K}\_{r}^{i}\Gamma\_{t,r-}\gamma\_{r}^{j}d[M^{i},M^{j}]\_{r}\right)\\ &=\Gamma\_{t,s-}\beta\_{s}\bar{Z}\_{s}ds+d\left(\int\_{t}^{s}\Gamma\_{t,r-}\sum\_{i=1}^{p}\bar{K}\_{r}^{i}\gamma\_{r}^{i}dN\_{r}^{i}\right)\\ &=\Gamma\_{t,s-}\beta\_{s}\bar{Z}\_{s}ds+\Gamma\_{t,s-}\sum\_{i=1}^{p}\bar{K}\_{s}^{i}\gamma\_{s}^{i}\lambda\_{s}^{i}ds+\Gamma\_{t,s-}\sum\_{i=1}^{p}\bar{K}\_{s}^{i}\gamma\_{s}^{i}dM\_{s}^{i},\end{aligned} |  | (2.55) |

where we have used that d​[Mi,Mj]s=0d[M^{i},M^{j}]\_{s}=0, for i≠ji\neq j, since P​(τi=τj)=0P(\tau\_{i}=\tau\_{j})=0, for i≠ji\neq j, and for the case i=ji=j, d​[Mi]s=d​Nsid[M^{i}]\_{s}=dN\_{s}^{i}. This yields,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​(Y¯s​Γt,s)=−Γt,s−​(Y¯s−​δs​d​s+Y¯s−​βs​d​Ws+Y¯s−​∑i=1pγsi​d​Msi)+Γt,s−​(hs​d​s+d​D¯s−Z¯s​d​Ws−∑i=1pK¯si​d​Msi)−Γt,s−​βs​Z¯s​d​s−Γt,s−​∑i=1pK¯si​γsi​λsi​d​s−Γt,s−​∑i=1pK¯si​γsi​d​Msi=Γt,s−​(hs−δs​Y¯s−−βs​Z¯s−∑i=1pK¯si​γsi​λsi)​d​s+Γt,s−​d​D¯s−(Γt,s−​(Y¯s−​βs+Z¯s)​d​Ws+Γt,s−​(∑i=1p(K¯si​(1+γsi)+Y¯s−​γsi)​d​Msi))=Γt,s−​(hs−δs​Y¯s−−βs​Z¯s−∑i=1pK¯si​γsi​λsi)​d​s+Γt,s−​d​D¯s−d​ms,\displaystyle\begin{aligned} -d(\bar{Y}\_{s}\Gamma\_{t,s})&=-\Gamma\_{t,s-}\left(\bar{Y}\_{s-}\delta\_{s}ds+\bar{Y}\_{s-}\beta\_{s}dW\_{s}+\bar{Y}\_{s-}\sum\_{i=1}^{p}\gamma\_{s}^{i}dM\_{s}^{i}\right)\\ &\quad+\Gamma\_{t,s-}\left(h\_{s}ds+d\bar{D}\_{s}-\bar{Z}\_{s}dW\_{s}-\sum\_{i=1}^{p}\bar{K}\_{s}^{i}dM\_{s}^{i}\right)\\ &\quad-\Gamma\_{t,s-}\beta\_{s}\bar{Z}\_{s}ds-\Gamma\_{t,s-}\sum\_{i=1}^{p}\bar{K}\_{s}^{i}\gamma\_{s}^{i}\lambda\_{s}^{i}ds-\Gamma\_{t,s-}\sum\_{i=1}^{p}\bar{K}\_{s}^{i}\gamma\_{s}^{i}dM\_{s}^{i}\\ &=\Gamma\_{t,s-}\left(h\_{s}-\delta\_{s}\bar{Y}\_{s-}-\beta\_{s}\bar{Z}\_{s}-\sum\_{i=1}^{p}\bar{K}\_{s}^{i}\gamma\_{s}^{i}\lambda\_{s}^{i}\right)ds+\Gamma\_{t,s-}d\bar{D}\_{s}\\ &\quad-\left(\Gamma\_{t,s-}(\bar{Y}\_{s-}\beta\_{s}+\bar{Z}\_{s})dW\_{s}+\Gamma\_{t,s-}\left(\sum\_{i=1}^{p}(\bar{K}\_{s}^{i}(1+\gamma\_{s}^{i})+\bar{Y}\_{s-}\gamma\_{s}^{i})dM\_{s}^{i}\right)\right)\\ &=\Gamma\_{t,s-}\left(h\_{s}-\delta\_{s}\bar{Y}\_{s-}-\beta\_{s}\bar{Z}\_{s}-\sum\_{i=1}^{p}\bar{K}\_{s}^{i}\gamma\_{s}^{i}\lambda\_{s}^{i}\right)ds+\Gamma\_{t,s-}d\bar{D}\_{s}-dm\_{s},\end{aligned} |  | (2.56) |

where the process (ms)s∈[0,T](m\_{s})\_{s\in[0,T]} is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ms=Γt,s−​(Y¯s​βs+Z¯s)​d​Ws+Γt,s−​(∑i=1p(K¯si​(1+γsi)+Y¯s−​γsi)​d​Msi).dm\_{s}=\Gamma\_{t,s-}(\bar{Y}\_{s}\beta\_{s}+\bar{Z}\_{s})dW\_{s}+\Gamma\_{t,s-}(\sum\_{i=1}^{p}(\bar{K}\_{s}^{i}(1+\gamma\_{s}^{i})+\bar{Y}\_{s-}\gamma\_{s}^{i})dM\_{s}^{i}). |  | (2.57) |

The process (ms)(m\_{s}) is a martingale, since Γt,⋅∈𝒮2\Gamma\_{t,\cdot}\in\mathcal{S}^{2}, Y¯∈𝒮2\bar{Y}\in\mathcal{S}^{2}, Z¯∈ℋ2\bar{Z}\in\mathcal{H}^{2}, K¯i∈ℋλi2\bar{K}^{i}\in\mathcal{H}\_{\lambda^{i}}^{2} for each i∈{1,…,p}i\in\{1,\ldots,p\}, and since β\beta and γi​λi\gamma^{i}\sqrt{\lambda^{i}}, for each i∈{1,…,p}i\in\{1,\ldots,p\}, are bounded.
Using Equations ([2.54](https://arxiv.org/html/2601.01250v1#S2.E54 "In Proof. ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) and ([2.56](https://arxiv.org/html/2601.01250v1#S2.E56 "In Proof. ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), and the fact that Γ\Gamma is non-negative, we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​(Y¯s​Γt,s)≥Γt,s−​φs​d​s+Γt,s−​d​D¯s−d​ms.-d(\bar{Y}\_{s}\Gamma\_{t,s})\geq\Gamma\_{t,s-}\varphi\_{s}ds+\Gamma\_{t,s-}d\bar{D}\_{s}-dm\_{s}. |  | (2.58) |

Integrating ([2.58](https://arxiv.org/html/2601.01250v1#S2.E58 "In Proof. ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) between tt and TT, and taking the conditional expectation, results in,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y¯t≥𝔼[Γt,T(η−η^)+∫tTΓt,s−φsds+∫tTΓt,s−dD¯s|𝒢t],0≤t≤T a.s.\bar{Y}\_{t}\geq\mathbb{E}\left[\Gamma\_{t,T}(\eta-\hat{\eta})+\int\_{t}^{T}\Gamma\_{t,s-}\varphi\_{s}ds+\int\_{t}^{T}\Gamma\_{t,s-}d\bar{D}\_{s}\middle|\mathcal{G}\_{t}\right],\quad 0\leq t\leq T\text{ a.s.} |  | (2.59) |

From ([2.49](https://arxiv.org/html/2601.01250v1#S2.E49 "In item (i) ‣ Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) we have that φt≥0\varphi\_{t}\geq 0 d​P⊗d​tdP\otimes dt-a.e. Furthermore, since η−η^≥0\eta-\hat{\eta}\geq 0, since D¯\bar{D} is non-decreasing and the adjoint process (Γt,s)s∈[t,T](\Gamma\_{t,s})\_{s\in[t,T]} is non-negative, we have that all terms inside the conditional expectation are non-negative; hence, Y¯t=Yt−Y^t≥0\bar{Y}\_{t}=Y\_{t}-\hat{Y}\_{t}\geq 0 a.s. Since this holds for all t∈[0,T]t\in[0,T] and since both YY and Y^\hat{Y} are rcll, the *comparison* result (i) for D,D^∈𝒜p,T2D,\hat{D}\in\mathcal{A}\_{p,T}^{2} is proven.
  
Let us prove (ii) for D,D^∈𝒜p,T2D,\hat{D}\in\mathcal{A}\_{p,T}^{2}.
Assume that there exists t0∈[0,T]t\_{0}\in[0,T] such that Yt0=Y^t0Y\_{t\_{0}}=\hat{Y}\_{t\_{0}} a.s. and such that ∏i=1p(1+γτii​𝟙t0<τi≤s)>0\prod\_{i=1}^{p}(1+\gamma\_{\tau\_{i}}^{i}\mathbbm{1}\_{t\_{0}<\tau\_{i}\leq s})>0 for all s∈[t0,T]s\in[t\_{0},T] a.s. (cf. Eq. ([2.35](https://arxiv.org/html/2601.01250v1#S2.E35 "In Remark 2.15: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"))). This implies that Γt0,s>0\Gamma\_{t\_{0},s}>0 for all s∈[t0,T]s\in[t\_{0},T] a.s. On the other hand, Equation ([2.59](https://arxiv.org/html/2601.01250v1#S2.E59 "In Proof. ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) (for t=t0t=t\_{0}) leads to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=Y¯t0≥𝔼[Γt0,T(η−η^)+∫t0TΓt0,s−φsds+∫t0TΓt0,s−dD¯s|𝒢t0].0=\bar{Y}\_{t\_{0}}\geq\mathbb{E}\left[\Gamma\_{t\_{0},T}(\eta-\hat{\eta})+\int\_{t\_{0}}^{T}\Gamma\_{t\_{0},s-}\varphi\_{s}ds+\int\_{t\_{0}}^{T}\Gamma\_{t\_{0},s-}d\bar{D}\_{s}\middle|\mathcal{G}\_{t\_{0}}\right]. |  | (2.60) |

This, together with the non-negativity of the terms inside the conditional expectation and the positivity of (Γt,s)(\Gamma\_{t,s}), implies that η=η^\eta=\hat{\eta} a.s. and φt=0\varphi\_{t}=0, for all t∈[t0,T]t\in[t\_{0},T] d​P⊗d​tdP\otimes dt-a.e. Let us now set D~t≔∫t0tΓt0,s−​𝑑D¯s\tilde{D}\_{t}\coloneqq\int\_{t\_{0}}^{t}\Gamma\_{t\_{0},s-}d\bar{D}\_{s} for each t∈[t0,T]t\in[t\_{0},T]. We have D~T≥0\tilde{D}\_{T}\geq 0 a.s. as Γt0,s>0\Gamma\_{t\_{0},s}>0 and as D¯\bar{D} is non-decreasing (by assumption). Using this and ([2.60](https://arxiv.org/html/2601.01250v1#S2.E60 "In Proof. ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), we get 0=𝔼​[D~T|𝒢t0]0=\mathbb{E}[\tilde{D}\_{T}|\mathcal{G}\_{t\_{0}}] a.s., hence D~T=0\tilde{D}\_{T}=0 a.s. Since Γt0,s>0\Gamma\_{t\_{0},s}>0 for all T≥s≥t0T\geq s\geq t\_{0} a.s., we have D¯T−D¯t0=∫t0T(Γt0,s−)−1​𝑑D~s\bar{D}\_{T}-\bar{D}\_{t\_{0}}=\int\_{t\_{0}}^{T}(\Gamma\_{t\_{0},s-})^{-1}d\tilde{D}\_{s}, which implies that D¯t0=D¯T\bar{D}\_{t\_{0}}=\bar{D}\_{T} a.s. Hence, the *strict comparison* result (ii) is proven fro D,D^∈𝒜p,T2D,\hat{D}\in\mathcal{A}\_{p,T}^{2}.
  
Step 2. We now consider the case where the optional processes D,D^D,\hat{D} are not necessarily predictable; more precisely, D,D^∈𝒜T2D,\hat{D}\in\mathcal{A}\_{T}^{2}. By Proposition [2.6](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem6 "Proposition 2.6: ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") (applied to DD and to D^\hat{D}) there exist D′∈𝒜p,T2D^{\prime}\in\mathcal{A}\_{p,T}^{2}, D^′∈𝒜p,T2\hat{D}^{\prime}\in\mathcal{A}\_{p,T}^{2} and θi,θ^i∈ℋλi,T2\theta^{i},\hat{\theta}^{i}\in\mathcal{H}\_{\lambda^{i},T}^{2} (where i∈{1,…,p}i\in\{1,\ldots,p\}), such that DD and D^\hat{D} can be uniquely written as follows,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt=Dt′+∫0t∑i=1pθsi​d​Nsi,a.s. and ​D^t=D^t′+∫0t∑i=1pθ^si​d​Nsi,a.s.\displaystyle\begin{aligned} D\_{t}&=D\_{t}^{\prime}+\int\_{0}^{t}\sum\_{i=1}^{p}\theta\_{s}^{i}dN\_{s}^{i},\quad\text{a.s. and }\hat{D}\_{t}=\hat{D}\_{t}^{\prime}+\int\_{0}^{t}\sum\_{i=1}^{p}\hat{\theta}\_{s}^{i}dN\_{s}^{i},\quad\text{a.s.}\end{aligned} |  | (2.61) |

Since D¯≔D−D^\bar{D}\coloneqq D-\hat{D} is non-decreasing, and since τ1<⋯<τp\tau\_{1}<\cdots<\tau\_{p}, by Lemma [A.2](https://arxiv.org/html/2601.01250v1#A1.Thmtheorem2 "Lemma A.2: ‣ Appendix A Some Technical Lemmas ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") we get that D¯′≔D′−D^′\bar{D}^{\prime}\coloneqq D^{\prime}-\hat{D}^{\prime} is non-decreasing and for each i∈{1,…,p}i\in\{1,\ldots,p\} θτii≥θ^τii\theta\_{\tau\_{i}}^{i}\geq\hat{\theta}\_{\tau\_{i}}^{i} a.s. on {τi≤T}\{\tau\_{i}\leq T\}. By applying Itô’s product rule to (Y¯s​Γt,s)(\bar{Y}\_{s}\Gamma\_{t,s}), we get −d​(Y¯s​Γt,s)=−Y¯s−​d​Γt,s−Γt,s−​d​Y¯s−d​[Y¯,Γt,⋅]s-d(\bar{Y}\_{s}\Gamma\_{t,s})=-\bar{Y}\_{s-}d\Gamma\_{t,s}-\Gamma\_{t,s-}d\bar{Y}\_{s}-d[\bar{Y},\Gamma\_{t,\cdot}]\_{s}. Here, d​[Y¯,Γt,⋅]sd[\bar{Y},\Gamma\_{t,\cdot}]\_{s} is equal to the right-hand side of ([2.55](https://arxiv.org/html/2601.01250v1#S2.E55 "In Proof. ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) plus the additional term d​[D¯,Γt,⋅]sd[\bar{D},\Gamma\_{t,\cdot}]\_{s}. The term d​[D¯,Γt,⋅]sd[\bar{D},\Gamma\_{t,\cdot}]\_{s} can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​[D¯,Γt,⋅]s=d​[D¯′,Γt,⋅]s+d​(∑i=1p∑j=1p[∫t⋅(θri−θ^ri)​𝑑Nri,∫t⋅Γt,r−​γrj​𝑑Nrj]s)=d​(∫tsΓt,r−​∑i=1p∑j=1p(θri−θ^ri)​γrj​d​[Ni,Nj]r)=d​(∫tsΓt,r−​∑i=1p(θri−θ^ri)​γri​d​Nri)=Γt,s−​∑i=1p(θsi−θ^si)​γsi​d​Nsi,\displaystyle\begin{aligned} d[\bar{D},\Gamma\_{t,\cdot}]\_{s}&=d[\bar{D}^{\prime},\Gamma\_{t,\cdot}]\_{s}+d\left(\sum\_{i=1}^{p}\sum\_{j=1}^{p}\left[\int\_{t}^{\cdot}(\theta\_{r}^{i}-\hat{\theta}\_{r}^{i})dN\_{r}^{i},\int\_{t}^{\cdot}\Gamma\_{t,r-}\gamma\_{r}^{j}dN\_{r}^{j}\right]\_{s}\right)\\ &=d\left(\int\_{t}^{s}\Gamma\_{t,r-}\sum\_{i=1}^{p}\sum\_{j=1}^{p}(\theta\_{r}^{i}-\hat{\theta}\_{r}^{i})\gamma\_{r}^{j}d[N^{i},N^{j}]\_{r}\right)\\ &=d\left(\int\_{t}^{s}\Gamma\_{t,r-}\sum\_{i=1}^{p}(\theta\_{r}^{i}-\hat{\theta}\_{r}^{i})\gamma\_{r}^{i}dN\_{r}^{i}\right)=\Gamma\_{t,s-}\sum\_{i=1}^{p}(\theta\_{s}^{i}-\hat{\theta}\_{s}^{i})\gamma\_{s}^{i}dN\_{s}^{i},\end{aligned} |  | (2.62) |

where we have used that d​[Ni,Nj]s=0d[N^{i},N^{j}]\_{s}=0, for i≠ji\neq j, since P​(τi=τj)=0P(\tau\_{i}=\tau\_{j})=0, , for i≠ji\neq j, and d​[Ni]s=d​Nsid[N^{i}]\_{s}=dN\_{s}^{i} (when i=ji=j). Hence, we have,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​(Y¯s​Γt,s)=Γt,s−​(hs−δs​Y¯s−βs​Z¯s−∑i=1pK¯si​γsi​λsi)​d​s+Γt,s−​d​D¯s−d​ms+Γt,s−​∑i=1p(θsi−θ^si)​γsi​d​Nsi,-d(\bar{Y}\_{s}\Gamma\_{t,s})=\Gamma\_{t,s-}\left(h\_{s}-\delta\_{s}\bar{Y}\_{s}-\beta\_{s}\bar{Z}\_{s}-\sum\_{i=1}^{p}\bar{K}\_{s}^{i}\gamma\_{s}^{i}\lambda\_{s}^{i}\right)ds+\Gamma\_{t,s-}d\bar{D}\_{s}-dm\_{s}\\ +\Gamma\_{t,s-}\sum\_{i=1}^{p}(\theta\_{s}^{i}-\hat{\theta}\_{s}^{i})\gamma\_{s}^{i}dN\_{s}^{i}, |  | (2.63) |

where (mt)(m\_{t}) is the same martingale as the one from Eq. ([2.57](https://arxiv.org/html/2601.01250v1#S2.E57 "In Proof. ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), (ht)(h\_{t}) is the process from Eq. ([2.51](https://arxiv.org/html/2601.01250v1#S2.E51 "In Proof. ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), and (δt)(\delta\_{t}) and (βt)(\beta\_{t}) are the processes from Eq. ([2.52](https://arxiv.org/html/2601.01250v1#S2.E52 "In Proof. ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")). Using inequality ([2.54](https://arxiv.org/html/2601.01250v1#S2.E54 "In Proof. ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) and the fact that d​D¯t=d​D¯t′+∑i=1p(θti−θ^ti)​d​Ntid\bar{D}\_{t}=d\bar{D}\_{t}^{\prime}+\sum\_{i=1}^{p}(\theta\_{t}^{i}-\hat{\theta}\_{t}^{i})dN\_{t}^{i}, integrating between tt and TT (where t∈[0,T]t\in[0,T]), and taking the conditional expectation, we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y¯t≥𝔼[Γt,T(η−η^)+∫tTΓt,s−(dD¯s′+∑i=1p(θsi−θ^si)(1+γsi)dNsi+φsds)|𝒢t], a.s.\bar{Y}\_{t}\geq\mathbb{E}\left[\Gamma\_{t,T}(\eta-\hat{\eta})+\int\_{t}^{T}\Gamma\_{t,s-}\left(d\bar{D}\_{s}^{\prime}+\sum\_{i=1}^{p}(\theta\_{s}^{i}-\hat{\theta}\_{s}^{i})(1+\gamma\_{s}^{i})dN\_{s}^{i}+\varphi\_{s}ds\right)\middle|\mathcal{G}\_{t}\right]\text{, a.s.} |  | (2.64) |

where the process (φt)(\varphi\_{t}) is the same as the one from Eq. ([2.53](https://arxiv.org/html/2601.01250v1#S2.E53 "In Proof. ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")). Let us note that, for i∈{1,…,p}i\in\{1,\ldots,p\},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫tTΓt,s−​(θsi−θ^si)​(1+γsi)​𝑑Nsi=Γt,τi−​(θτii−θ^τii)​(1+γτii)​𝟙{T≥τi≥t}.\displaystyle\int\_{t}^{T}\Gamma\_{t,s-}(\theta\_{s}^{i}-\hat{\theta}\_{s}^{i})(1+\gamma\_{s}^{i})dN\_{s}^{i}=\Gamma\_{t,\tau\_{i}-}(\theta\_{\tau\_{i}}^{i}-\hat{\theta}\_{\tau\_{i}}^{i})(1+\gamma\_{\tau\_{i}}^{i})\mathbbm{1}\_{\{T\geq\tau\_{i}\geq t\}}. |  | (2.65) |

Let ii be fixed. We now check that this term is non-negative on each AkA\_{k}, where k∈{1,…,p}k\in\{1,...,p\}, and where the AkA\_{k}’s are the ones appearing in assumption ([2.47](https://arxiv.org/html/2601.01250v1#S2.E47 "In item (i) ‣ Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")). As noted above, θτii≥θ^τii\theta\_{\tau\_{i}}^{i}\geq\hat{\theta}\_{\tau\_{i}}^{i} a.s. on {τi≤T}\{\tau\_{i}\leq T\}. Furthermore, the adjoint process (Γt,s)s∈[0,T](\Gamma\_{t,s})\_{s\in[0,T]} is non-negative. Moreover, by definition of AkA\_{k}, we have 𝟙{T≥τi≥t}​𝟙Ak=0,\mathbbm{1}\_{\{T\geq\tau\_{i}\geq t\}}\mathbbm{1}\_{A\_{k}}=0, for 0≤k≤i−10\leq k\leq i-1, and, by assumption ([2.47](https://arxiv.org/html/2601.01250v1#S2.E47 "In item (i) ‣ Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), we have (1+γτii)​𝟙{T≥τi≥t}​𝟙Ak≥0(1+\gamma^{i}\_{\tau\_{i}})\mathbbm{1}\_{\{T\geq\tau\_{i}\geq t\}}\mathbbm{1}\_{A\_{k}}\geq 0 (for each k∈{i,…,p}k\in\{i,...,p\}). Hence, the term in Eq. ([2.65](https://arxiv.org/html/2601.01250v1#S2.E65 "In Proof. ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) is non-negative.
From the assumption ([2.49](https://arxiv.org/html/2601.01250v1#S2.E49 "In item (i) ‣ Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) and from ([2.53](https://arxiv.org/html/2601.01250v1#S2.E53 "In Proof. ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) we have that φt≥0\varphi\_{t}\geq 0 d​P⊗d​tdP\otimes dt-a.e. Furthermore, since η−η^≥0\eta-\hat{\eta}\geq 0, since (D¯t′)(\bar{D}\_{t}^{\prime}) is non-decreasing and the adjoint process (Γt,s)s∈[0,T](\Gamma\_{t,s})\_{s\in[0,T]} is non-negative, we have that all the terms inside the conditional expectation are non-negative; hence, Y¯t=Yt−Y^t≥0\bar{Y}\_{t}=Y\_{t}-\hat{Y}\_{t}\geq 0 a.s. Since this holds for all t∈[0,T]t\in[0,T], and since (Yt)(Y\_{t}) and (Y^t)(\hat{Y}\_{t}) are rcll, the *comparison result* (i) for D,D^∈𝒜T2D,\hat{D}\in\mathcal{A}\_{T}^{2} is proven.

Assume now that there exists t0∈[0,T]t\_{0}\in[0,T] such that Yt0=Y^t0Y\_{t\_{0}}=\hat{Y}\_{t\_{0}} a.s. and that for each i∈{1,…,p}i\in\{1,\ldots,p\} γτii>−1\gamma^{i}\_{\tau\_{i}}>-1 a.s. Thus, Γt,s>0\Gamma\_{t,s}>0 for all s∈[t,T]s\in[t,T] a.s. For t=t0t=t\_{0}, Eq. ([2.64](https://arxiv.org/html/2601.01250v1#S2.E64 "In Proof. ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) leads to,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=Y¯t0≥𝔼[Γt0,T(η−η^)+∫t0TΓt,s−(dD¯s′+∑i=1p(θsi−θ^si)(1+γsi)dNsi+φsds)|𝒢t0].0=\bar{Y}\_{t\_{0}}\geq\mathbb{E}\left[\Gamma\_{t\_{0},T}(\eta-\hat{\eta})+\int\_{t\_{0}}^{T}\Gamma\_{t,s-}\left(d\bar{D}\_{s}^{\prime}+\sum\_{i=1}^{p}(\theta\_{s}^{i}-\hat{\theta}\_{s}^{i})(1+\gamma\_{s}^{i})dN\_{s}^{i}+\varphi\_{s}ds\right)\middle|\mathcal{G}\_{t\_{0}}\right]. |  | (2.66) |

This, together with the non-negativity of the terms inside the conditional expectation and the positivity of (Γt,s)(\Gamma\_{t,s}), implies that η=η^\eta=\hat{\eta} a.s., φt=0\varphi\_{t}=0 for all t∈[t0,T]t\in[t\_{0},T] d​P⊗d​tdP\otimes dt-a.e., and, for each i∈{1,…,p}i\in\{1,\ldots,p\}, θτii=θ^τii\theta\_{\tau\_{i}}^{i}=\hat{\theta}\_{\tau\_{i}}^{i} on {t0<τi≤T}\{t\_{0}<\tau\_{i}\leq T\} a.s. We set D~t′≔∫t0tΓt0,s−​𝑑D¯s′\tilde{D}\_{t}^{\prime}\coloneqq\int\_{t\_{0}}^{t}\Gamma\_{t\_{0},s-}d\bar{D}\_{s}^{\prime} for each t∈[t0,T]t\in[t\_{0},T]. We have D~T′≥0\tilde{D}\_{T}^{\prime}\geq 0 a.s. as Γt0,s>0\Gamma\_{t\_{0},s}>0 and as D¯′\bar{D}^{\prime} is non-decreasing. Using this and ([2.66](https://arxiv.org/html/2601.01250v1#S2.E66 "In Proof. ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), we get 𝔼​[D~T′|𝒢t0]=0\mathbb{E}[\tilde{D}\_{T}^{\prime}|\mathcal{G}\_{t\_{0}}]=0 a.s.; hence, D~T′=0\tilde{D}\_{T}^{\prime}=0 a.s. Since Γt0,s>0\Gamma\_{t\_{0},s}>0 for all T≥s≥t0T\geq s\geq t\_{0} a.s. we have D¯T′−D¯t0′=∫t0T(Γt0,s−)−1​𝑑D~s′\bar{D}\_{T}^{\prime}-\bar{D}\_{t\_{0}}^{\prime}=\int\_{t\_{0}}^{T}(\Gamma\_{t\_{0},s-})^{-1}d\tilde{D}\_{s}^{\prime}, which implies that D¯t0′=D¯T′\bar{D}\_{t\_{0}}^{\prime}=\bar{D}\_{T}^{\prime} a.s. The *strict comparison* result (ii) for D,D^∈𝒜T2D,\hat{D}\in\mathcal{A}\_{T}^{2} is thus proven.

∎

We now provide an example where the conclusion of the comparison (and strict comparison) result from Theorem [2.17](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem17 "Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") does not necessarily hold, if the assumptions of the theorem are not satisfied.

###### Example 2.20:

Assume that for each i∈{1,…,p}i\in\{1,\ldots,p\} the process λi\lambda^{i} is bounded. Let gg be a λ(p)\lambda^{(p)}-linear driver (cf. Definition [2.21](https://arxiv.org/html/2601.01250v1#S2.E21 "In Definition 2.10 (𝜆^(𝑝)-Linear Driver and Generalized 𝜆^(𝑝)-Linear Driver): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) of the form,

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(ω,t,y,z,k1,…,kp)=αt​(ω)​y+βt​(ω)​z+∑i=1pγi​ki​λti​(ω),g(\omega,t,y,z,k^{1},\ldots,k^{p})=\alpha\_{t}(\omega)y+\beta\_{t}(\omega)z+\sum\_{i=1}^{p}\gamma^{i}k^{i}\lambda\_{t}^{i}(\omega), |  | (2.67) |

where each γi\gamma^{i} is a real constant. The dynamics of the adjoint process Γ0,⋅\Gamma\_{0,\cdot} are (cf. ([2.33](https://arxiv.org/html/2601.01250v1#S2.E33 "In Theorem 2.14 (Explicit Solution of the Generalized 𝜆^(𝑝)-Linear BSDE with 𝐷 Predictable): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"))),

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Γ0,s=Γ0,s−​(αs​d​s+βs​d​Ws+∑i=1pγi​d​Msi),Γ0,0=1.d\Gamma\_{0,s}=\Gamma\_{0,s-}\left(\alpha\_{s}ds+\beta\_{s}dW\_{s}+\sum\_{i=1}^{p}\gamma^{i}dM\_{s}^{i}\right),\quad\Gamma\_{0,0}=1. |  | (2.68) |

By Remark [2.15](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem15 "Remark 2.15: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), Γ0,T\Gamma\_{0,T} satisfies,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ0,T=HT​exp⁡(−∫0T∑i=1pγi​λsi​d​s)​∏i=1p(1+γi​𝟙{0<τi≤T}),\Gamma\_{0,T}=H\_{T}\exp\left(-\int\_{0}^{T}\sum\_{i=1}^{p}\gamma^{i}\lambda\_{s}^{i}ds\right)\prod\_{i=1}^{p}(1+\gamma^{i}\mathbbm{1}\_{\{0<\tau\_{i}\leq T\}}), |  | (2.69) |

where HH has the dynamics d​Ht=Ht​(αt​d​t+βt​d​Wt)dH\_{t}=H\_{t}(\alpha\_{t}dt+\beta\_{t}dW\_{t}) with H0=1H\_{0}=1.
  
We specify p=2p=2. We define the terminal condition as,

|  |  |  |  |
| --- | --- | --- | --- |
|  | η(1)≔𝟙{τ1≤T,τ2>T}.\eta^{(1)}\coloneqq\mathbbm{1}\_{\{\tau\_{1}\leq T,\tau\_{2}>T\}}. |  | (2.70) |

Let (Y(1))(Y^{(1)}) be the first component of the solution of the BSDE associated with driver gg, terminal time TT and terminal condition η(1)\eta^{(1)}. By the explicit formula from Theorem [2.14](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem14 "Theorem 2.14 (Explicit Solution of the Generalized 𝜆^(𝑝)-Linear BSDE with 𝐷 Predictable): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), we get,

|  |  |  |
| --- | --- | --- |
|  | Y0(1)=(1+γ1)​𝔼​[HT​e−∑j=12γj​∫0Tλsj​𝑑s​𝟙{τ1≤T,τ2>T}].Y\_{0}^{(1)}=(1+\gamma^{1})\mathbb{E}\left[H\_{T}e^{-\sum\_{j=1}^{2}\gamma^{j}\int\_{0}^{T}\lambda\_{s}^{j}ds}\mathbbm{1}\_{\{\tau\_{1}\leq T,\tau\_{2}>T\}}\right]. |  |

Under the assumption P​(τ1≤T,τ2>T)>0P(\tau\_{1}\leq T,\tau\_{2}>T)>0, if 1+γ1<01+\gamma^{1}<0, then Y0(1)<0Y\_{0}^{(1)}<0. However, η(1)≥0\eta^{(1)}\geq 0 a.s. Hence, the comparison result does not hold.
  
We now define the terminal condition as,

|  |  |  |  |
| --- | --- | --- | --- |
|  | η(2)≔𝟙{τ2≤T}.\eta^{(2)}\coloneqq\mathbbm{1}\_{\{\tau\_{2}\leq T\}}. |  | (2.71) |

Let (Y(2))(Y^{(2)}) be the solution of the BSDE associated with driver gg, terminal time TT and terminal condition η(2)\eta^{(2)}.

By the explicit formula from Theorem [2.14](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem14 "Theorem 2.14 (Explicit Solution of the Generalized 𝜆^(𝑝)-Linear BSDE with 𝐷 Predictable): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y0=(1+γ1)​(1+γ2)​𝔼​[HT​e−∑j=12γj​∫0Tλsj​𝑑s​𝟙{T≥τ2}],Y\_{0}=(1+\gamma^{1})(1+\gamma^{2})\mathbb{E}\left[H\_{T}e^{-\sum\_{j=1}^{2}\gamma^{j}\int\_{0}^{T}\lambda\_{s}^{j}ds}\mathbbm{1}\_{\{T\geq\tau\_{2}\}}\right], |  | (2.72) |

where we have used that τ1<τ2\tau\_{1}<\tau\_{2}.
Under the assumption P​(τ2≤T)>0P(\tau\_{2}\leq T)>0, if (1+γ1)​(1+γ2)<0(1+\gamma^{1})(1+\gamma^{2})<0, then ([2.72](https://arxiv.org/html/2601.01250v1#S2.E72 "In Example 2.20: ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) leads to Y0<0Y\_{0}<0. However, η(2)≥0\eta^{(2)}\geq 0 a.s. Hence, the comparison result does not hold.
  
The reader can generalize this reasoning to the case where p>2p>2, by using terminal conditions based on the sets from Eq.([2.46](https://arxiv.org/html/2601.01250v1#S2.E46 "In 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")).

If either (or both) γ1\gamma^{1} and γ2\gamma^{2} are equal to −1-1, then ([2.72](https://arxiv.org/html/2601.01250v1#S2.E72 "In Example 2.20: ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) gives Y0=0Y\_{0}=0. Under the assumption that P​(τ2≤T)>0P(\tau\_{2}\leq T)>0, we have P​(η(2)>0)>0P(\eta^{(2)}>0)>0, while Y0=0Y\_{0}=0, hence the strict comparison result does not hold.

## 3 Pricing of European Options in Markets with Multiple Defaults

### 3.1 Pricing in a Linear Financial Market with two Defaultable Risky Assets

We consider a market model where the primary assets are a risk-free savings account with price process BB, a default-free asset with price process S0S^{0}, and two assets with price processes S1S^{1} and S2S^{2}, which are subject to default or to some other credit event at times τ1\tau^{1} and τ2\tau^{2}, respectively.

More precisely, we place ourselves in the probabilistic setting of Section [2](https://arxiv.org/html/2601.01250v1#S2 "2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), where we set p=2p=2. The times τ1\tau\_{1} and τ2\tau\_{2} model here the times of default (or the times of some other extraneous credit events, provided they are ordered) of the risky assets S1S^{1} and S2S^{2}, respectively. As before Mt1=Nt1−∫0tλs1​𝑑sM\_{t}^{1}=N\_{t}^{1}-\int\_{0}^{t}\lambda\_{s}^{1}ds and Mt2=Nt2−∫0tλs2​𝑑sM\_{t}^{2}=N\_{t}^{2}-\int\_{0}^{t}\lambda\_{s}^{2}ds.
  
We consider the following dynamics for the asset prices,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Bt=Bt​rt​d​t,B0=1;d​St0=St0​[μt0​d​t+σt0​d​Wt],S00>0;d​St1=St−1​[μt1​d​t+σt1​d​Wt+βt1​d​Mt1],S01>0;d​St2=St−2​[μt2​d​t+σt2​d​Wt+βt2​d​Mt2],S02>0.\displaystyle\begin{aligned} dB\_{t}&=B\_{t}r\_{t}dt,\quad B\_{0}=1;\\ dS\_{t}^{0}&=S\_{t}^{0}[\mu\_{t}^{0}dt+\sigma\_{t}^{0}dW\_{t}],\quad S\_{0}^{0}>0;\\ dS\_{t}^{1}&=S\_{t-}^{1}[\mu\_{t}^{1}dt+\sigma\_{t}^{1}dW\_{t}+\beta\_{t}^{1}dM\_{t}^{1}],\quad S\_{0}^{1}>0;\\ dS\_{t}^{2}&=S\_{t-}^{2}[\mu\_{t}^{2}dt+\sigma\_{t}^{2}dW\_{t}+\beta\_{t}^{2}dM\_{t}^{2}],\quad S\_{0}^{2}>0.\end{aligned} |  | (3.1) |

The process rr, and the processes μi\mu^{i} and σi\sigma^{i} (for i∈{0,1,2}i\in\{0,1,2\}) are predictable, such that, σi>0\sigma^{i}>0 for i∈{0,1,2}i\in\{0,1,2\}, and r,μi,σir,\mu^{i},\sigma^{i} and (σi)−1(\sigma^{i})^{-1} are bounded (for i∈{0,1,2}i\in\{0,1,2\}). We note that there is no requirement for the intensity process λi\lambda^{i} to be bounded. We assume that βt1≠0\beta\_{t}^{1}\neq 0, βt2≠0\beta\_{t}^{2}\neq 0, and μt0≠rt\mu\_{t}^{0}\neq r\_{t}. We assume moreover that βti≥−1\beta\_{t}^{i}\geq-1 for i∈{1,2}i\in\{1,2\}.

###### Remark 3.1:

By Remark [2.12](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem12 "Remark 2.12: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), the explicit formula for SiS^{i}, where i∈{1,2}i\in\{1,2\}, is: for t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sti=exp⁡(∫0t(μsi−12​(σsi)2−βsi​λsi)​𝑑s+∫0tσsi​𝑑Ws)​(1+βτii​𝟙{t≥τi}), a.s.S\_{t}^{i}=\exp\left(\int\_{0}^{t}\left(\mu\_{s}^{i}-\frac{1}{2}(\sigma\_{s}^{i})^{2}-\beta\_{s}^{i}\lambda\_{s}^{i}\right)ds+\int\_{0}^{t}\sigma\_{s}^{i}dW\_{s}\right)(1+\beta\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{t\geq\tau\_{i}\}}),\text{ a.s.} |  | (3.2) |

If βτii=−1\beta^{i}\_{\tau\_{i}}=-1, then the ii-th asset’s price jumps to zero at τi\tau\_{i}.

We consider an investor who at time 0 invests an amount x∈ℝx\in\mathbb{R} in the market. For i∈{0,1,2}i\in\{0,1,2\} we use ϕti\phi\_{t}^{i} to denote the amount of money in asset StiS\_{t}^{i} at time t∈[0,T]t\in[0,T].
  
If βτii=−1\beta\_{\tau\_{i}}^{i}=-1 a.s., then, on the set {T≥t≥τi}\{T\geq t\geq\tau\_{i}\}, Sti=0S\_{t}^{i}=0 and the investor will no longer invest in this asset; thus, ϕti=0\phi\_{t}^{i}=0 on the set {T≥t>τi}\{T\geq t>\tau\_{i}\}.
  
In the case where p=1p=1 and β1=−1\beta^{1}=-1, this model has been considered in [[3](https://arxiv.org/html/2601.01250v1#bib.bib3)] and [[7](https://arxiv.org/html/2601.01250v1#bib.bib7)].

The process ϕ=(ϕ0,ϕ1,ϕ2)∈(ℋT2,ℋλ1,T2,ℋλ2,T)\phi=(\phi^{0},\phi^{1},\phi^{2})\in(\mathcal{H}\_{T}^{2},\mathcal{H}\_{\lambda^{1},T}^{2},\mathcal{H}\_{\lambda^{2},T}) is called the risky-asset strategy (or the strategy). Let now (Ct)t∈[0,T](C\_{t})\_{t\in[0,T]} be a finite variational optional process in 𝒜T2\mathcal{A}\_{T}^{2} which represents the cumulative cash ‘withdrawals’ from the portfolio. The value of the portfolio at time tt associated with the initial value xx, trading strategy ϕ\phi and ‘withdrawal’ process CC is denoted by Vtx,ϕ,CV\_{t}^{x,\phi,C}. If ϕ\phi is the strategy in the risky assets S0,S1,S2S^{0},S^{1},S^{2}, then the amount invested in the risk-free bank account is: Vtx,ϕ,C−∑i=02ϕtiV\_{t}^{x,\phi,C}-\sum\_{i=0}^{2}\phi^{i}\_{t}.

The self-financing condition for the wealth process Vx,ϕ,C=VV^{x,\phi,C}=V leads to the following dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vt=(Vt−∑i=02ϕtiBt0)​d​Bt0+∑i=02ϕti​d​StiSt−i−d​Ct=(Vt−ϕt0−ϕt1−ϕt2)​rt​d​t+ϕt0​(μt0​d​t+σt0​d​Wt)+ϕt1​(μt1​d​t+σt1​d​Wt+βt1​d​Mt)+ϕt2​(μt2​d​t+σt2​d​Wt+βt2​d​Mt2)−d​Ct=(Vt​rt+ϕt0​(μt0−rt)+ϕt1​(μt1−rt)+ϕt2​(μt2−rt))​d​t+(ϕt0​σt0+ϕt1​σt1+ϕt2​σt2)​d​Wt+ϕt1​βt1​d​Mt1+ϕt2​βt2​d​Mt2−d​Ct=(Vt​rt+ϕt′​σt​Θt0+ϕt1​Θt1​βt1​λt1+ϕt2​Θt2​βt2​λt2)​d​t−d​Ct+ϕt′​σt​d​Wt+ϕt1​βt1​d​Mt1+ϕt2​βt2​d​Mt2,\displaystyle\begin{aligned} dV\_{t}&=\left(\frac{V\_{t}-\sum\_{i=0}^{2}\phi\_{t}^{i}}{B\_{t}^{0}}\right)dB\_{t}^{0}+\sum\_{i=0}^{2}\frac{\phi\_{t}^{i}dS\_{t}^{i}}{S\_{t-}^{i}}-dC\_{t}\\ &=(V\_{t}-\phi\_{t}^{0}-\phi\_{t}^{1}-\phi\_{t}^{2})r\_{t}dt+\phi\_{t}^{0}(\mu\_{t}^{0}dt+\sigma\_{t}^{0}dW\_{t})\\ &\quad\quad+\phi\_{t}^{1}(\mu\_{t}^{1}dt+\sigma\_{t}^{1}dW\_{t}+\beta\_{t}^{1}dM\_{t})+\phi\_{t}^{2}(\mu\_{t}^{2}dt+\sigma\_{t}^{2}dW\_{t}+\beta\_{t}^{2}dM\_{t}^{2})-dC\_{t}\\ &=(V\_{t}r\_{t}+\phi\_{t}^{0}(\mu\_{t}^{0}-r\_{t})+\phi\_{t}^{1}(\mu\_{t}^{1}-r\_{t})+\phi\_{t}^{2}(\mu\_{t}^{2}-r\_{t}))dt\\ &\quad\quad+(\phi\_{t}^{0}\sigma\_{t}^{0}+\phi\_{t}^{1}\sigma\_{t}^{1}+\phi\_{t}^{2}\sigma\_{t}^{2})dW\_{t}+\phi\_{t}^{1}\beta\_{t}^{1}dM\_{t}^{1}+\phi\_{t}^{2}\beta\_{t}^{2}dM\_{t}^{2}-dC\_{t}\\ &=(V\_{t}r\_{t}+\phi\_{t}^{\prime}\sigma\_{t}\Theta\_{t}^{0}+\phi\_{t}^{1}\Theta\_{t}^{1}\beta\_{t}^{1}\lambda\_{t}^{1}+\phi\_{t}^{2}\Theta\_{t}^{2}\beta\_{t}^{2}\lambda\_{t}^{2})dt-dC\_{t}+\phi\_{t}^{\prime}\sigma\_{t}dW\_{t}\\ &\quad\quad+\phi\_{t}^{1}\beta\_{t}^{1}dM\_{t}^{1}+\phi\_{t}^{2}\beta\_{t}^{2}dM\_{t}^{2},\end{aligned} |  | (3.3) |

where ϕt′​σt=∑i=02ϕti​σti\phi\_{t}^{\prime}\sigma\_{t}=\sum\_{i=0}^{2}\phi\_{t}^{i}\sigma\_{t}^{i}, and

|  |  |  |
| --- | --- | --- |
|  | Θt0=μt0−rtσt0,Θt1=μt1−rt−σt1​Θt0βt1​λt1​𝟙{βt1​λt1≠0},Θt2=μt2−rt−σt2​Θt0βt2​λt2​𝟙{βt2​λt2≠0}.\Theta\_{t}^{0}=\frac{\mu\_{t}^{0}-r\_{t}}{\sigma\_{t}^{0}},\quad\Theta\_{t}^{1}=\frac{\mu\_{t}^{1}-r\_{t}-\sigma\_{t}^{1}\Theta\_{t}^{0}}{\beta\_{t}^{1}\lambda\_{t}^{1}}\mathbbm{1}\_{\{\beta\_{t}^{1}\lambda\_{t}^{1}\neq 0\}},\quad\Theta\_{t}^{2}=\frac{\mu\_{t}^{2}-r\_{t}-\sigma\_{t}^{2}\Theta\_{t}^{0}}{\beta\_{t}^{2}\lambda\_{t}^{2}}\mathbbm{1}\_{\{\beta\_{t}^{2}\lambda\_{t}^{2}\neq 0\}}. |  |

###### Assumption 3.1.1:

We assume that the processes Θ0\Theta^{0}, Θ1​λ1\Theta^{1}\sqrt{\lambda^{1}} and Θ2​λ2\Theta^{2}\sqrt{\lambda^{2}} are bounded.

Let T>0T>0. Let η∈L2​(𝒢T)\eta\in L^{2}(\mathcal{G}\_{T}) and let DD be a finite variational optional process in 𝒜T2\mathcal{A}\_{T}^{2}. We consider a European option with terminal time TT which generates a terminal payoff η\eta and intermediate cashflows, commonly referred to as ‘dividends’ (which need not be strictly positive, c.f., e.g., [[5](https://arxiv.org/html/2601.01250v1#bib.bib5)]). For each t∈[0,T]t\in[0,T], DtD\_{t} represents the cumulative intermediate cashflows generated by the option between [0,t][0,t]. As the ‘dividends’ are not necessarily positive, the process DD is not necessarily non-decreasing.

We place ourselves from the point of view of an agent who wants to sell this option at time t=0t=0. With the proceeds from the sale, they wish to construct a (self-financing) portfolio which allows them to pay the buyer of the contract the amount η\eta at time TT as well as the intermediate ‘dividends’ DD.

Setting Zt≔ϕt′​σtZ\_{t}\coloneqq\phi\_{t}^{\prime}\sigma\_{t} and Kti=ϕti​βtiK\_{t}^{i}=\phi\_{t}^{i}\beta\_{t}^{i}, for i∈{1,2}i\in\{1,2\}, and using ([3.3](https://arxiv.org/html/2601.01250v1#S3.E3 "In 3.1 Pricing in a Linear Financial Market with two Defaultable Risky Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) (with C=DC=D), we get that the process (V,Z,K1,K2)(V,Z,K^{1},K^{2}) satisfies the following dynamics,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​Vt=−(rt​Vt+Θt0​Zt+Θt1​Kt1​λt1+Θt2​Kt2​λt2)​d​t+d​Dt−Zt​d​Wt−Kt1​d​Mt1−Kt2​d​Mt2.-dV\_{t}=-(r\_{t}V\_{t}+\Theta\_{t}^{0}Z\_{t}+\Theta\_{t}^{1}K\_{t}^{1}\lambda\_{t}^{1}+\Theta\_{t}^{2}K\_{t}^{2}\lambda\_{t}^{2})dt+dD\_{t}-Z\_{t}dW\_{t}-K\_{t}^{1}dM\_{t}^{1}-K\_{t}^{2}dM\_{t}^{2}. |  | (3.4) |

For each (ω,t,y,z,k1,k2)(\omega,t,y,z,k^{1},k^{2}) we define,

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(ω,t,y,z,k1,k2)≔−rt​(ω)​y−Θt0​(ω)​z−Θt1​(ω)​k1​λt1​(ω)−Θt2​(ω)​k2​λt2​(ω).g(\omega,t,y,z,k^{1},k^{2})\coloneqq-r\_{t}(\omega)y-\Theta\_{t}^{0}(\omega)z-\Theta\_{t}^{1}(\omega)k^{1}\lambda\_{t}^{1}(\omega)-\Theta\_{t}^{2}(\omega)k^{2}\lambda\_{t}^{2}(\omega). |  | (3.5) |

By our previous assumptions and Assumption [3.1.1](https://arxiv.org/html/2601.01250v1#S3.Thmtheorem1.Thmassumption1 "Assumption 3.1.1: ‣ 3.1 Pricing in a Linear Financial Market with two Defaultable Risky Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), we have that r,Θ0r,\Theta^{0} and Θi​λi\Theta^{i}\sqrt{\lambda^{i}} (for i∈{1,2}i\in\{1,2\}) are predictable and bounded. It follows that the driver gg is a λ(p)\lambda^{(p)}-linear driver (cf. Eq. ([2.21](https://arxiv.org/html/2601.01250v1#S2.E21 "In Definition 2.10 (𝜆^(𝑝)-Linear Driver and Generalized 𝜆^(𝑝)-Linear Driver): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"))). By Proposition [2.9](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem9 "Proposition 2.9 (Exsitence and Uniqueness): ‣ 2.2.2 Existence and Uniqueness for BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), there exists a unique solution (X,Z,K1,K2)∈𝒮2×ℋ2×ℋλ12×ℋλ22(X,Z,K^{1},K^{2})\in\mathcal{S}^{2}\times\mathcal{H}^{2}\times\mathcal{H}\_{\lambda^{1}}^{2}\times\mathcal{H}\_{\lambda^{2}}^{2} of the BSDE associated with terminal time TT, generalized λ(p)\lambda^{(p)}-linear driver g​(t,y,z,k1,k2)​d​t+d​Dtg(t,y,z,k^{1},k^{2})dt+dD\_{t} and terminal condition η∈L2​(𝒢T)\eta\in L^{2}(\mathcal{G}\_{T}).

The solution of the BSDE (X,Z,K1,K2)(X,Z,K^{1},K^{2}) provides a replicating portfolio, where the seller chooses a risky-asset strategy ϕ\phi according to the following change of variables:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚽:ℋT2×ℋλ1,T2×ℋλ2,T2→ℋT2×ℋλ1,T2×ℋλ2,T2;(Z,K1,K2)↦𝚽​(Z,K1,K2)≔ϕ,\mathbf{\Phi}:\mathcal{H}\_{T}^{2}\times\mathcal{H}\_{\lambda^{1},T}^{2}\times\mathcal{H}\_{\lambda^{2},T}^{2}\rightarrow\mathcal{H}\_{T}^{2}\times\mathcal{H}\_{\lambda^{1},T}^{2}\times\mathcal{H}\_{\lambda^{2},T}^{2};(Z,K^{1},K^{2})\mapsto\mathbf{\Phi}(Z,K^{1},K^{2})\coloneqq\phi, |  | (3.6) |

where ϕ≔(ϕ0,ϕ1,ϕ2)\phi\coloneqq(\phi^{0},\phi^{1},\phi^{2}), and the amount ϕi\phi^{i} invested in the ii-th asset (where i∈{0,1,2}i\in\{0,1,2\}) is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕt0=Zt−Kt1​σt1βt1−Kt2​σt2βt2σt0,ϕt1=Kt1βt1,ϕt2=Kt2βt2.\phi\_{t}^{0}=\frac{Z\_{t}-\frac{K\_{t}^{1}\sigma\_{t}^{1}}{\beta\_{t}^{1}}-\frac{K\_{t}^{2}\sigma\_{t}^{2}}{\beta\_{t}^{2}}}{\sigma\_{t}^{0}},\quad\phi\_{t}^{1}=\frac{K\_{t}^{1}}{\beta\_{t}^{1}},\quad\phi\_{t}^{2}=\frac{K\_{t}^{2}}{\beta\_{t}^{2}}. |  | (3.7) |

Here, the process DD corresponds to the cumulative cash ‘withdrawn’ by the seller from their hedging (replicating) portfolio. The above portfolio is a replicating portfolio for the seller of the European contingent claim, since the seller is able to reinvest all proceeds from the sale into the market and pay η\eta at the option expiration date of TT, as well as the intermediate ‘dividends’ of the option.

The amount X0X\_{0} (the first component of the BSDE at time zero) is the hedging price (or price by replication) of the option at time t=0t=0 and we denote it with X0,T​(η,D)X\_{0,T}(\eta,D). For t∈[0,T]t\in[0,T], the hedging price (or price by replication) XtX\_{t} is denoted by Xt,T​(η,D)X\_{t,T}(\eta,D).

#### 3.1.1 The Case Where DD is Predictable

Let the cumulative ‘dividend’ process DD be a (predictable) process in 𝒜p2\mathcal{A}\_{p}^{2}. Since the driver from ([3.5](https://arxiv.org/html/2601.01250v1#S3.E5 "In 3.1 Pricing in a Linear Financial Market with two Defaultable Risky Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) is λ(p)\lambda^{(p)}-linear, we have, by Theorem [2.14](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem14 "Theorem 2.14 (Explicit Solution of the Generalized 𝜆^(𝑝)-Linear BSDE with 𝐷 Predictable): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), an explicit formula for Xt,T​(η,D)X\_{t,T}(\eta,D). For each t∈[0,T]t\in[0,T] the adjoint process (Γt,s)s∈[t,T](\Gamma\_{t,s})\_{s\in[t,T]} is the unique solution of the following SDE,

|  |  |  |
| --- | --- | --- |
|  | d​Γt,s=Γt,s−​(−rs​d​s−Θs0​d​Ws−Θs1​d​Ms1−Θs2​d​Ms2),Γt,t=1.d\Gamma\_{t,s}=\Gamma\_{t,s-}(-r\_{s}ds-\Theta\_{s}^{0}dW\_{s}-\Theta\_{s}^{1}dM\_{s}^{1}-\Theta\_{s}^{2}dM\_{s}^{2}),\quad\Gamma\_{t,t}=1. |  |

By Remark [2.14](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem14 "Theorem 2.14 (Explicit Solution of the Generalized 𝜆^(𝑝)-Linear BSDE with 𝐷 Predictable): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), (Γt,s)s∈[t,T](\Gamma\_{t,s})\_{s\in[t,T]} is written,

|  |  |  |
| --- | --- | --- |
|  | Γt,s=exp⁡(−∫tsru​𝑑u)​exp⁡(−∫tsΘu0​𝑑Ws−12​∫ts(Θu0)2−Θu1​λu1−Θu2​λu2​d​u)×(1−Θτ11​𝟙{t<τ1≤s})​(1−Θτ22​𝟙{t<τ2≤s})=e−∫tsru​𝑑u​ζt,s,\displaystyle\begin{aligned} \Gamma\_{t,s}&=\exp\left(-\int\_{t}^{s}r\_{u}du\right)\exp\left(-\int\_{t}^{s}\Theta\_{u}^{0}dW\_{s}-\frac{1}{2}\int\_{t}^{s}(\Theta\_{u}^{0})^{2}-\Theta\_{u}^{1}\lambda\_{u}^{1}-\Theta\_{u}^{2}\lambda\_{u}^{2}du\right)\\ &\quad\times(1-\Theta\_{\tau\_{1}}^{1}\mathbbm{1}\_{\{t<\tau\_{1}\leq s\}})(1-\Theta\_{\tau\_{2}}^{2}\mathbbm{1}\_{\{t<\tau\_{2}\leq s\}})\\ &=e^{-\int\_{t}^{s}r\_{u}du}\zeta\_{t,s},\end{aligned} |  |

where the process (ζt,s)s∈[t,T](\zeta\_{t,s})\_{s\in[t,T]} satisfies the dynamics,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ζt,s=ζt,s−​(−Θs0​d​Ws−Θs1​d​Ms1−Θs2​d​Ms2),ζt,t=1.d\zeta\_{t,s}=\zeta\_{t,s-}(-\Theta\_{s}^{0}dW\_{s}-\Theta\_{s}^{1}dM\_{s}^{1}-\Theta\_{s}^{2}dM\_{s}^{2}),\quad\zeta\_{t,t}=1. |  | (3.8) |

Hence, by the explicit formula (cf. Theorem [2.14](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem14 "Theorem 2.14 (Explicit Solution of the Generalized 𝜆^(𝑝)-Linear BSDE with 𝐷 Predictable): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") where DD is predictable),

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt,T(η,D)=Xt=𝔼[e−∫tTrs​𝑑sζt,Tη+∫tTe−∫tsru​𝑑uζt,s−dDs|𝒢t].X\_{t,T}(\eta,D)=X\_{t}=\mathbb{E}\left[e^{-\int\_{t}^{T}r\_{s}ds}\zeta\_{t,T}\eta+\int\_{t}^{T}e^{-\int\_{t}^{s}r\_{u}du}\zeta\_{t,s-}dD\_{s}\middle|\mathcal{G}\_{t}\right]. |  | (3.9) |

#### 3.1.2 The Case Where DD is Optional

Let us now consider the case where DD is not necessarily predictable, but only optional; more precisely, D∈𝒜2D\in\mathcal{A}^{2}. By Proposition [2.6](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem6 "Proposition 2.6: ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), there exist a unique process D′∈𝒜p2D^{\prime}\in\mathcal{A}\_{p}^{2} and unique processes ψ1∈ℋλ12,ψ2∈ℋλ22\psi^{1}\in\mathcal{H}\_{\lambda^{1}}^{2},\psi^{2}\in\mathcal{H}\_{\lambda^{2}}^{2}, such that for all t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt=Dt′+∫0t∑i=12ψsi​d​Nsi,a.s.D\_{t}=D\_{t}^{\prime}+\int\_{0}^{t}\sum\_{i=1}^{2}\psi\_{s}^{i}dN\_{s}^{i},\quad\text{a.s.} |  | (3.10) |

From a financial point of view, the random variable ψτii\psi\_{\tau\_{i}}^{i} represents the cash flow generated by the contingent claim (the option) at the ii-th default time τi\tau\_{i} (see also [[2](https://arxiv.org/html/2601.01250v1#bib.bib2)] Part I for contingent claims where the cash flow depends on the default times). By Theorem [2.16](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem16 "Theorem 2.16 (Explicit Solution of the Generalized 𝜆^(𝑝)-Linear BSDE with 𝐷 Optional): ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), the hedging price at time tt, Xt,T​(η,D)X\_{t,T}(\eta,D), is equal to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt,T(η,D)=𝔼[e−∫tTrs​𝑑sζt,Tη+∫tTe−∫tsru​𝑑uζt,s−dDs′+e−∫tτ1rs​𝑑sζt,τ1ψτ11𝟙{t<τ1≤T}+e−∫tτ2rs​𝑑sζt,τ2ψτ22𝟙{t<τ2≤T}|𝒢t].X\_{t,T}(\eta,D)=\mathbb{E}\left[e^{-\int\_{t}^{T}r\_{s}ds}\zeta\_{t,T}\eta\right.+\int\_{t}^{T}e^{-\int\_{t}^{s}r\_{u}du}\zeta\_{t,s-}dD\_{s}^{\prime}\\ \left.+e^{-\int\_{t}^{\tau\_{1}}r\_{s}ds}\zeta\_{t,\tau\_{1}}\psi\_{\tau\_{1}}^{1}\mathbbm{1}\_{\{t<\tau\_{1}\leq T\}}+e^{-\int\_{t}^{\tau\_{2}}r\_{s}ds}\zeta\_{t,\tau\_{2}}\psi\_{\tau\_{2}}^{2}\mathbbm{1}\_{\{t<\tau\_{2}\leq T\}}\middle|\mathcal{G}\_{t}\right]. |  | (3.11) |

#### 3.1.3 Change of measure

The change of measure technique is often used in linear market models in financial mathematics. In this sub-subsection, we will make the following assumption on the ‘Sharpe ratios’ Θ0\Theta^{0}, Θ1\Theta^{1} and Θ2\Theta^{2}.

###### Assumption 3.1.2:

We assume that ∏i=12(1−Θτii​𝟙{t<τi≤s})>0\prod\_{i=1}^{2}(1-\Theta\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{t<\tau\_{i}\leq s\}})>0 for all 0≤t≤s≤T0\leq t\leq s\leq T a.s.

By Remark [2.12](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem12 "Remark 2.12: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") and Assumption [3.1.2](https://arxiv.org/html/2601.01250v1#S3.Thmtheorem1.Thmassumption2 "Assumption 3.1.2: ‣ 3.1.3 Change of measure ‣ 3.1 Pricing in a Linear Financial Market with two Defaultable Risky Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") we have that ζt,s>0\zeta\_{t,s}>0 for all s∈[t,T]s\in[t,T]. By Assumption [3.1.1](https://arxiv.org/html/2601.01250v1#S3.Thmtheorem1.Thmassumption1 "Assumption 3.1.1: ‣ 3.1 Pricing in a Linear Financial Market with two Defaultable Risky Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") we have that ∫0T((Θs0)2+(Θs1)2​λs1+(Θs2)2​λs2)​𝑑s\int\_{0}^{T}((\Theta\_{s}^{0})^{2}+(\Theta\_{s}^{1})^{2}\lambda\_{s}^{1}+(\Theta\_{s}^{2})^{2}\lambda\_{s}^{2})ds is bounded; hence, by Proposition [2.13](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem13 "Proposition 2.13: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") (ζt,s)s∈[t,T](\zeta\_{t,s})\_{s\in[t,T]} is a square-integrable martingale. Let QQ be a new probability measure, defined by the Radon-Nikodym derivative with respect to PP on 𝒢T\mathcal{G}\_{T}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Qd​P|𝒢T=ζ0,T=ℰ​(−∫0⋅Θs0​𝑑Ws−∫0⋅Θs1​𝑑Ms1−∫0⋅Θs2​𝑑Ms2)T.\left.\frac{dQ}{dP}\right|\_{\mathcal{G}\_{T}}=\zeta\_{0,T}=\mathcal{E}\left(-\int\_{0}^{\cdot}\Theta\_{s}^{0}dW\_{s}-\int\_{0}^{\cdot}\Theta\_{s}^{1}dM\_{s}^{1}-\int\_{0}^{\cdot}\Theta\_{s}^{2}dM\_{s}^{2}\right)\_{T}. |  | (3.12) |

##### The Case Where DD is Predictable

In the case where the ‘dividend’ process DD is predictable, we use Bayes formula to perform a change of measure in the conditional expectation of ([3.9](https://arxiv.org/html/2601.01250v1#S3.E9 "In 3.1.1 The Case Where 𝐷 is Predictable ‣ 3.1 Pricing in a Linear Financial Market with two Defaultable Risky Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) (cf., e.g., Proposition 1.7.1.5 from [[16](https://arxiv.org/html/2601.01250v1#bib.bib16)]) to get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt,T(η,D)=Xt=𝔼Q[e−∫tTrs​𝑑sη+∫tTe−∫tsru​𝑑udDs|𝒢t]a.s.X\_{t,T}(\eta,D)=X\_{t}=\mathbb{E}^{Q}\left[e^{-\int\_{t}^{T}r\_{s}ds}\eta+\int\_{t}^{T}e^{-\int\_{t}^{s}r\_{u}du}dD\_{s}\middle|\mathcal{G}\_{t}\right]\quad\text{a.s.} |  | (3.13) |

##### The Case Where DD is Optional

If the ‘dividend’ process DD is optional, the price of the European option at time tt under the probability measure QQ can be written:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt,T(η,D)=𝔼Q[e−∫tTrs​𝑑sη+∫tTe−∫tsru​𝑑udDs′+e−∫tτ1rs​𝑑sψτ11𝟙{t<τ1≤T}+e−∫tτ2rs​𝑑sψτ22𝟙{t<τ2≤T}|𝒢t]X\_{t,T}(\eta,D)=\mathbb{E}^{Q}\left[e^{-\int\_{t}^{T}r\_{s}ds}\eta\right.+\int\_{t}^{T}e^{-\int\_{t}^{s}r\_{u}du}dD\_{s}^{\prime}\\ \left.+e^{-\int\_{t}^{\tau\_{1}}r\_{s}ds}\psi\_{\tau\_{1}}^{1}\mathbbm{1}\_{\{t<\tau\_{1}\leq T\}}+e^{-\int\_{t}^{\tau\_{2}}r\_{s}ds}\psi\_{\tau\_{2}}^{2}\mathbbm{1}\_{\{t<\tau\_{2}\leq T\}}\middle|\mathcal{G}\_{t}\right] |  | (3.14) |

We note that the pricing system for this market is linear.

### 3.2 Pricing in a Non-linear Complete Market with pp Defaultable Assets

We now assume that there are imperfections in the market, which are incorporated via the non-linearity of the driver in the dynamics of the wealth process. We consider the case where there are pp defaultable assets.

We introduce the following notation for the price processes of the primary assets: B,S0,S1,…,SpB,S^{0},S^{1},\ldots,S^{p}, where BB and S0S^{0} represent the price process of a risk-free savings account and a default-free risky asset, respectively, while for each i∈{1,…,p}i\in\{1,\ldots,p\}, SiS^{i} is the price process of the ii-th defaultable asset (or ii-th credit risk bearing asset). The underlying probabilistic framework is the same as that introduced at the beginning of Section [2](https://arxiv.org/html/2601.01250v1#S2 "2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), and we continue to work under the same assumptions. The price processes of BB and S0S^{0} remain unchanged from ([3.1](https://arxiv.org/html/2601.01250v1#S3.E1 "In 3.1 Pricing in a Linear Financial Market with two Defaultable Risky Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")). For each i∈{1,…,p}i\in\{1,\ldots,p\}, the price process of the ii-th defaultable asset is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sti=St−i​[μti​d​t+σti​d​Wt+βti​d​Mti],S0i>0.dS\_{t}^{i}=S\_{t-}^{i}\left[\mu\_{t}^{i}\,dt+\sigma\_{t}^{i}\,dW\_{t}+\beta\_{t}^{i}\,dM\_{t}^{i}\right],\quad S\_{0}^{i}>0. |  | (3.15) |

For each i∈{1,…,p}i\in\{1,\ldots,p\}, the processes μi\mu^{i} and σi\sigma^{i} are assumed to be predictable, with σi>0\sigma^{i}>0, and such that μi\mu^{i}, σi\sigma^{i}, and (σi)−1(\sigma^{i})^{-1} are bounded. The interest rate process rr is assumed to be predictable and bounded. We assume that, for each i∈{1,…,p}i\in\{1,\ldots,p\}, βti≠0\beta\_{t}^{i}\neq 0. We recall that, for each i∈{1,…,p}i\in\{1,\ldots,p\}, the process Mi=Ni−∫0⋅λsi​𝑑sM^{i}=N^{i}-\int\_{0}^{\cdot}\lambda\_{s}^{i}\,ds is the 𝔾\mathbb{G}-compensated default martingale.

We again consider an investor who, at time 0, invests an initial amount x∈ℝx\in\mathbb{R} in this market. For i∈{1,…,p}i\in\{1,\ldots,p\}, we let ϕti\phi\_{t}^{i} denote the amount of money invested in StiS\_{t}^{i} at time t∈[0,T]t\in[0,T]. If, for a given i∈{1,…,p}i\in\{1,\ldots,p\}, we have βτii=−1\beta\_{\tau\_{i}}^{i}=-1 a.s., then on the set {t≥τi}\{t\geq\tau\_{i}\}, the price of the ii-th asset becomes 0, and hence the investor will no longer invest in this asset. If βτi=−1\beta\_{\tau\_{i}}=-1, we set ϕti=0\phi\_{t}^{i}=0 on {t≥τi}\{t\geq\tau\_{i}\}.

Similarly to the linear framework, for a given risky-asset strategy denoted ϕ=(ϕ0,ϕ1,…,ϕp)∈ℋ2×ℋλ12×⋯×ℋλp2\phi=(\phi^{0},\phi^{1},\ldots,\phi^{p})\in\mathcal{H}^{2}\times\mathcal{H}\_{\lambda^{1}}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p}}^{2}, a given cash withdrawal finite variation optional process C∈𝒜T2C\in\mathcal{A}\_{T}^{2}, and a given initial wealth (capital) x∈ℝx\in\mathbb{R}, the wealth process at time t∈[0,T]t\in[0,T], denoted by Vtx,ϕ,CV\_{t}^{x,\phi,C} (or simply VtV\_{t} if there is no ambiguity), satisfies the self-financing condition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​Vt=g​(t,Vt,ϕt′​σt,ϕt1​βt1,…,ϕtp​βtp)​d​t−ϕt′​σt​d​Wt−∑i=1pϕti​βti​d​Mti+d​Ct;V0=x,-dV\_{t}=g(t,V\_{t},\phi\_{t}^{\prime}\sigma\_{t},\phi\_{t}^{1}\beta\_{t}^{1},\ldots,\phi\_{t}^{p}\beta\_{t}^{p})dt-\phi\_{t}^{\prime}\sigma\_{t}\,dW\_{t}-\sum\_{i=1}^{p}\phi\_{t}^{i}\beta\_{t}^{i}\,dM\_{t}^{i}+dC\_{t};\quad V\_{0}=x, |  | (3.16) |

where gg is a possibly non-linear λ(p)\lambda^{(p)}-admissible driver. Equivalently, setting Zt=ϕt′​σtZ\_{t}=\phi\_{t}^{\prime}\sigma\_{t} and, for each i∈{1,…,p}i\in\{1,\ldots,p\}, Kti=ϕti​βtiK\_{t}^{i}=\phi\_{t}^{i}\beta\_{t}^{i}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​Vt=g​(t,Vt,Zt,Kt1,…,Ktp)​d​t−Zt​d​Wt−∑i=1pKti​d​Mti+d​Ct;V0=x.-dV\_{t}=g(t,V\_{t},Z\_{t},K\_{t}^{1},\ldots,K\_{t}^{p})dt-Z\_{t}\,dW\_{t}-\sum\_{i=1}^{p}K\_{t}^{i}\,dM\_{t}^{i}+dC\_{t};\quad V\_{0}=x. |  | (3.17) |

We consider a European contingent claim with maturity TT, terminal payoff η∈L2​(𝒢T)\eta\in L^{2}(\mathcal{G}\_{T}), and optional ’dividend’ process D∈𝒜T2D\in\mathcal{A}\_{T}^{2}.
  
Let (X⋅,Tg​(η,D),Z⋅,Tg​(η,D),K⋅,Tg,1​(η,D),…,K⋅,Tg,p​(η,D))(X\_{\cdot,T}^{g}(\eta,D),Z\_{\cdot,T}^{g}(\eta,D),K\_{\cdot,T}^{g,1}(\eta,D),\ldots,K\_{\cdot,T}^{g,p}(\eta,D)), or simply (X,Z,K1,…,Kp)(X,Z,K^{1},\ldots,K^{p}), denote the solution of the BSDE with terminal time TT, terminal condition η\eta, and generalized driver g​(t,y,z,k1,…,kp)​d​t+d​Dtg(t,y,z,k^{1},\ldots,k^{p})\,dt+dD\_{t}, that is, the BSDE satisfying the following dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​Xt=g​(t,Xt,Zt,Kt1,…,Ktp)​d​t+d​Dt−Zt​d​Wt−∑i=1pKti​d​Mti,XT=η.-dX\_{t}=g(t,X\_{t},Z\_{t},K\_{t}^{1},\ldots,K\_{t}^{p})dt+dD\_{t}-Z\_{t}\,dW\_{t}-\sum\_{i=1}^{p}K\_{t}^{i}\,dM\_{t}^{i},\quad X\_{T}=\eta. |  | (3.18) |

Hence, the process X=X⋅,Tg​(η,D)X=X\_{\cdot,T}^{g}(\eta,D) coincides with the wealth process corresponding to initial wealth x=X0x=X\_{0}, cumulative cash withdrawal process DD, and risky-asset strategy ϕ=𝚽​(Z,K1,…,Kp)\phi=\mathbf{\Phi}(Z,K^{1},\ldots,K^{p}), where 𝚽\mathbf{\Phi} is the following generalization of ([3.6](https://arxiv.org/html/2601.01250v1#S3.E6 "In 3.1 Pricing in a Linear Financial Market with two Defaultable Risky Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚽:ℋ2×ℋλ12×⋯×ℋλp2\displaystyle\mathbf{\Phi}:\mathcal{H}^{2}\times\mathcal{H}\_{\lambda^{1}}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p}}^{2} | →ℋ2×ℋλ12×⋯×ℋλp2,\displaystyle\rightarrow\mathcal{H}^{2}\times\mathcal{H}\_{\lambda^{1}}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p}}^{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (Z,K1,…,Kp)\displaystyle(Z,K^{1},\ldots,K^{p}) | ↦𝚽​(Z,K1,…,Kp)≔ϕ,\displaystyle\mapsto\mathbf{\Phi}(Z,K^{1},\ldots,K^{p})\coloneqq\phi, |  |

where ϕ≔(ϕ0,ϕ1,…,ϕp)\phi\coloneqq(\phi^{0},\phi^{1},\ldots,\phi^{p}) and the amount ϕi\phi^{i} invested in the ii-th asset (where i∈{0,1,…,p}i\in\{0,1,\ldots,p\}) is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕt0=Zt−Kt1​σt1βt1−Kt2​σt2βt2σt0,ϕti=Ktiβti,for ​i∈{1,…,p}.\phi\_{t}^{0}=\frac{Z\_{t}-\frac{K\_{t}^{1}\sigma\_{t}^{1}}{\beta\_{t}^{1}}-\frac{K\_{t}^{2}\sigma\_{t}^{2}}{\beta\_{t}^{2}}}{\sigma\_{t}^{0}},\quad\phi\_{t}^{i}=\frac{K\_{t}^{i}}{\beta\_{t}^{i}},\quad\text{for }i\in\{1,\ldots,p\}. |  | (3.19) |

Thus, X=VX0,ϕ,DX=V^{X\_{0},\phi,D}.

Starting from the initial wealth X0=X0,Tg​(η,D)X\_{0}=X\_{0,T}^{g}(\eta,D), the seller can construct a risky-asset strategy ϕ\phi that allows them to pay the intermediate ’dividends’ DD and the final payoff η\eta. We therefore call the initial wealth X0X\_{0} the hedging price (or replicating price) at time t=0t=0 of the option, and the process ϕ\phi the hedging strategy (or replicating strategy).

More generally, let us consider a maturity time S∈[0,T]S\in[0,T]. For each S∈[0,T]S\in[0,T] and for each payoff-dividend pair (η,D)∈L2​(𝒢S)×𝒜S2(\eta,D)\in L^{2}(\mathcal{G}\_{S})\times\mathcal{A}\_{S}^{2}, the process X⋅,Sg​(η,D)X\_{\cdot,S}^{g}(\eta,D) is called the hedging price of the option with maturity SS and payoff-dividend pair (η,D)(\eta,D). This yields the following pricing system for the pp-defaultable non-linear market model:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐗g:(S,η,D)↦X⋅,Sg​(η,D),\mathbf{X}^{g}:(S,\eta,D)\mapsto X\_{\cdot,S}^{g}(\eta,D), |  | (3.20) |

which is generally non-linear with respect to the pair (η,D)(\eta,D) (as the driver gg is in general non-linear).

We now state some properties of this pricing system (cf. [[7](https://arxiv.org/html/2601.01250v1#bib.bib7)] for the case of single default, and [[10](https://arxiv.org/html/2601.01250v1#bib.bib10)] for the case without jumps).

#### 3.2.1 Properties of the Non-linear Pricing System 𝐗g\mathbf{X}^{g} in the Case of pp Defaultable Assets

* •

  Consistency: By the flow property of the BSDEs with default jumps, the pricing system 𝐗g\mathbf{X}^{g} is consistent. More precisely, let S′∈[0,T]S^{\prime}\in[0,T], η∈L2​(𝒢S′)\eta\in L^{2}(\mathcal{G}\_{S^{\prime}}), D∈𝒜S′2D\in\mathcal{A}\_{S^{\prime}}^{2} and S∈[0,S′]S\in[0,S^{\prime}]. Then the hedging price of the European contingent claim associated with terminal payoff η\eta, cumulative dividend process DD and maturity S′S^{\prime} coincides with the hedging price of the European option with terminal time SS, payoff XS,S′g​(η,D)X\_{S,S^{\prime}}^{g}(\eta,D) and dividend process (Dt)t≤S(D\_{t})\_{t\leq S}, that is,

  |  |  |  |
  | --- | --- | --- |
  |  | X⋅,S′g​(η,D)=X⋅,Sg​(XS,S′g​(η,D),D).X\_{\cdot,S^{\prime}}^{g}(\eta,D)=X\_{\cdot,S}^{g}\left(X\_{S,S^{\prime}}^{g}(\eta,D),D\right). |  |

  ###### Remark 3.2:

  Note that when g​(t,0,0,…,0)=0g(t,0,0,\ldots,0)=0, we get that the price of a European option with null payoff and no dividends is equal to 0 for all maturity times S∈[0,T]S\in[0,T], hence X⋅,Sg​(0,0)=0X\_{\cdot,S}^{g}(0,0)=0.

Due to the (possible) presence of default jumps the non-linear pricing system is not necessarily monotone with respect to the payoff and dividend process. We introduce the following assumption (cf. the comparison Theorem [2.17](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem17 "Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")).

###### Assumption 3.2.1:

We assume that for each i∈{1,…,p}i\in\{1,\ldots,p\} there exists a map,

|  |  |  |
| --- | --- | --- |
|  | γi:Ω×[0,T]×ℝ4→ℝ; ​(ω,t,y,z,ki,k^i)↦γty,z,ki,k^i​(ω)\gamma^{i}:\Omega\times[0,T]\times\mathbb{R}^{4}\rightarrow\mathbb{R};\text{ }(\omega,t,y,z,k^{i},\hat{k}^{i})\mapsto\gamma\_{t}^{y,z,k^{i},\hat{k}^{i}}(\omega) |  |

which is 𝒫⊗ℬ​(ℝ4)\mathcal{P}\otimes\mathcal{B}(\mathbb{R}^{4})-measurable, satisfying d​P⊗d​tdP\otimes dt-a.e. for each (y,z,ki,k^i)∈ℝ4(y,z,k^{i},\hat{k}^{i})\in\mathbb{R}^{4},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |γty,z,ki,k^i​λti|≤Candγty,z,ki,k^i≥−1,\left|\gamma\_{t}^{y,z,k^{i},\hat{k}^{i}}\sqrt{\lambda\_{t}^{i}}\right|\leq C\quad\text{and}\quad\gamma\_{t}^{y,z,k^{i},\hat{k}^{i}}\geq-1, |  | (3.21) |

and such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(t,y,z,k1,…,kp)−g​(t,y,z,k^1,…,k^p)≥∑i=1pγty,z,ki,k^i​(ki−k^i)​λti.g(t,y,z,k^{1},\ldots,k^{p})-g(t,y,z,\hat{k}^{1},\ldots,\hat{k}^{p})\geq\sum\_{i=1}^{p}\gamma\_{t}^{y,z,k^{i},\hat{k}^{i}}(k^{i}-\hat{k}^{i})\lambda\_{t}^{i}. |  | (3.22) |

We now introduce the following partial order relation (cf. also [[7](https://arxiv.org/html/2601.01250v1#bib.bib7)]). Let S∈[0,T]S\in[0,T] be given. For (η,D),(η^,D^)∈L2​(𝒢S)×𝒜S2(\eta,D),(\hat{\eta},\hat{D})\in L^{2}(\mathcal{G}\_{S})\times\mathcal{A}\_{S}^{2}, we say that (η,D)(\eta,D) dominates (η^,D^)(\hat{\eta},\hat{D}) and we write the following relation,

|  |  |  |
| --- | --- | --- |
|  | (η,D)≻(η^,D^)ifη≥η^​ a.s. and ​D−D^​ is non-decreasing.(\eta,D)\succ(\hat{\eta},\hat{D})\quad\text{if}\quad\eta\geq\hat{\eta}\text{ a.s. and }D-\hat{D}\text{ is non-decreasing}. |  |

###### Proposition 3.3:

Under Assumption [3.2.1](https://arxiv.org/html/2601.01250v1#S3.Thmtheorem2.Thmassumption1 "Assumption 3.2.1: ‣ 3.2.1 Properties of the Non-linear Pricing System 𝐗^𝑔 in the Case of 𝑝 Defaultable Assets ‣ 3.2 Pricing in a Non-linear Complete Market with 𝑝 Defaultable Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), the non-linear pricing system 𝐗g\mathbf{X}^{g} has the following properties:

1. (a)

   Monotonicity: The non-linear pricing system 𝐗g\mathbf{X}^{g} is non-decreasing with respect to the payoff-dividend pair. More precisely, for all maturity times S∈[0,T]S\in[0,T], for all payoffs η,η^∈L2​(𝒢S)\eta,\hat{\eta}\in L^{2}(\mathcal{G}\_{S}) and all cumulative dividend processes D,D^∈𝒜S2D,\hat{D}\in\mathcal{A}\_{S}^{2}, the following implication holds:

   |  |  |  |
   | --- | --- | --- |
   |  | If ​(η,D)≻(η^,D^), then we have ​Xt,Sg​(η,D)≥Xt,Sg​(η^,D^),t∈[0,S]​ a.s.\text{If }(\eta,D)\succ(\hat{\eta},\hat{D}),\text{ then we have }X\_{t,S}^{g}(\eta,D)\geq X\_{t,S}^{g}(\hat{\eta},\hat{D}),\quad t\in[0,S]\text{ a.s.} |  |
2. (b)

   Convexity: If gg is convex with respect to the vector (y,z,k1,…,kp)(y,z,k^{1},\ldots,k^{p}), then the non-linear pricing system 𝐗g\mathbf{X}^{g} is convex with respect to the payoff-dividend pair (η,D)(\eta,D), that is, for any α∈[0,1]\alpha\in[0,1], S∈[0,T]S\in[0,T], η,η^∈L2​(𝒢S)\eta,\hat{\eta}\in L^{2}(\mathcal{G}\_{S}) and D,D^∈𝒜S2D,\hat{D}\in\mathcal{A}\_{S}^{2}, we have: for all t∈[0,S]t\in[0,S],

   |  |  |  |
   | --- | --- | --- |
   |  | Xt,Sg​(α​η+(1−α)​η^,α​D+(1−α)​D^)≤α​Xt,Sg​(η,D)+(1−α)​Xt,Sg​(η^,D^)a.s.X\_{t,S}^{g}(\alpha\eta+(1-\alpha)\hat{\eta},\alpha D+(1-\alpha)\hat{D})\leq\alpha X\_{t,S}^{g}(\eta,D)+(1-\alpha)X\_{t,S}^{g}(\hat{\eta},\hat{D})\quad\text{a.s.} |  |
3. (c)

   Non-Negativity: When g​(t,0,0,0,…,0)=0g(t,0,0,0,\ldots,0)=0, the non-linear pricing system 𝐗g\mathbf{X}^{g} is non-negative, that is, for all S∈[0,T]S\in[0,T], for all non-negative terminal payoffs η∈L2​(𝒢S)\eta\in L^{2}(\mathcal{G}\_{S}) and for all non-decreasing optional dividend processes D∈𝒜S2D\in\mathcal{A}\_{S}^{2}, we have that Xt,Sg​(η,D)≥0X\_{t,S}^{g}(\eta,D)\geq 0 for all t∈[0,S]t\in[0,S] a.s.
4. (d)

   No Arbitrage: We assume the additional condition that, for each i∈{1,…,p}i\in\{1,\ldots,p\}, γty,z,ki,k^i>−1,\gamma\_{t}^{y,z,k^{i},\hat{k}^{i}}>-1, d​P⊗d​tdP\otimes dt-a.e. Then, the non-linear pricing system 𝐗g\mathbf{X}^{g} satisfies the no arbitrage property. That is, for all maturities S∈[0,T]S\in[0,T], for all terminal payoffs η,η^∈L2​(𝒢S)\eta,\hat{\eta}\in L^{2}(\mathcal{G}\_{S}) and for all optional cumulative dividend processes D,D^∈𝒜S2D,\hat{D}\in\mathcal{A}\_{S}^{2}, the following holds:
   If (η,D)≻(η^,D^)(\eta,D)\succ(\hat{\eta},\hat{D}) and if at time t0∈[0,S]t\_{0}\in[0,S] we have Xt0,Sg​(η,D)=Xt0,Sg​(η^,D^)X\_{t\_{0},S}^{g}(\eta,D)=X\_{t\_{0},S}^{g}(\hat{\eta},\hat{D}) a.s., then η=η^\eta=\hat{\eta} a.s. and (Dt−D^t)t0≤t≤S(D\_{t}-\hat{D}\_{t})\_{t\_{0}\leq t\leq S} is constant.

###### Proof.

For the monotonicity of the non-linear pricing system 𝐗g\mathbf{X}^{g} we use the comparison result from Theorem [2.17](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem17 "Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") (which is applicable under Assumption [3.2.1](https://arxiv.org/html/2601.01250v1#S3.Thmtheorem2.Thmassumption1 "Assumption 3.2.1: ‣ 3.2.1 Properties of the Non-linear Pricing System 𝐗^𝑔 in the Case of 𝑝 Defaultable Assets ‣ 3.2 Pricing in a Non-linear Complete Market with 𝑝 Defaultable Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) and set g=g^g=\hat{g} in this theorem.
  
For the  convexity of the non-linear pricing system 𝐗g\mathbf{X}^{g}, we use again the comparison result from Theorem [2.17](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem17 "Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"). The proof follows standard arguments.
  
The non-negativity is a direct consequence of the monotonicity property. If η^=0\hat{\eta}=0, D^=0\hat{D}=0, η≥0\eta\geq 0 a.s., and DD non-decreasing, then by the definition of the partial order relation ≻\succ we have, (η,D)≻(η^,D^)(\eta,D)\succ(\hat{\eta},\hat{D}). By the comparison result from Theorem [2.17](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem17 "Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") and Remark [3.2](https://arxiv.org/html/2601.01250v1#S3.Thmtheorem2 "Remark 3.2: ‣ 1st item ‣ 3.2.1 Properties of the Non-linear Pricing System 𝐗^𝑔 in the Case of 𝑝 Defaultable Assets ‣ 3.2 Pricing in a Non-linear Complete Market with 𝑝 Defaultable Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") we have that Xt,Sg​(η,D)≥Xt,Sg​(η^,D^)=Xt,Sg​(0,0)=0X\_{t,S}^{g}(\eta,D)\geq X\_{t,S}^{g}(\hat{\eta},\hat{D})=X\_{t,S}^{g}(0,0)=0.
  
The proof of the no arbitrage property is a direct consequence of the strict comparison result from Theorem [2.17](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem17 "Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), where we set g^=g\hat{g}=g.
∎

#### 3.2.2 The (g,D)(g,D)-Conditional Evaluation ℰg,D\mathscr{E}^{g,D} for a λ(p)\lambda^{(p)}-Admissible Driver

Let gg be a λ(p)\lambda^{(p)}-admissible driver and let DD be a given optional dividend process belonging to 𝒜T2\mathcal{A}\_{T}^{2}. For each S∈[0,T]S\in[0,T] and each η∈L2​(𝒢S)\eta\in L^{2}(\mathcal{G}\_{S}), we define the (g,D)(g,D)-conditional evaluation of η\eta by,

|  |  |  |
| --- | --- | --- |
|  | ℰt,Sg,D​(η)≔Xt,Sg​(η,D),0≤t≤S.\mathscr{E}\_{t,S}^{g,D}(\eta)\coloneqq X\_{t,S}^{g}(\eta,D),\quad 0\leq t\leq S. |  |

The (g,D)(g,D)-conditional evaluation ℰ⋅,Sg,D​(η)\mathscr{E}\_{\cdot,S}^{g,D}(\eta) is the first component of the solution of the BSDE associated with terminal time SS, generalized driver g​(t,y,z,k1,…,kp)​d​t+d​Dtg(t,y,z,k^{1},\ldots,k^{p})dt+dD\_{t} and terminal condition η\eta, where we have fixed DD in the space 𝒜T2\mathcal{A}\_{T}^{2}.

###### Remark 3.4:

In the case where D=0D=0, our (g,D)(g,D)-conditional evaluation reduces to the gg-conditional evaluation for the case of pp default times (which we denote by ℰg\mathscr{E}^{g}).
If, furthermore, g=0g=0, then the (g,D)(g,D)-conditional evaluation reduces to the standard conditional expectation under PP, that is ℰt,S0,0=𝔼P​[η|𝒢t]\mathscr{E}\_{t,S}^{0,0}=\mathbb{E}^{P}[\eta|\mathcal{G}\_{t}], for t∈[0,S]t\in[0,S].

###### Remark 3.5:

Note that we can in fact define the (g,D)(g,D)-conditional evaluation ℰ⋅,Sg,D​(η)\mathscr{E}\_{\cdot,S}^{g,D}(\eta) on the entire interval [0,T][0,T] by setting,

|  |  |  |
| --- | --- | --- |
|  | ℰt,Sg,D​(η)≔ℰt,TgS,DS​(η)​ for ​t≥S,\mathscr{E}\_{t,S}^{g,D}(\eta)\coloneqq\mathscr{E}\_{t,T}^{g^{S},D^{S}}(\eta)\text{ for }t\geq S, |  |

where we have set gS​(t,⋅)≔g​(t,⋅)​𝟙t≤Sg^{S}(t,\cdot)\coloneqq g(t,\cdot)\mathbbm{1}\_{t\leq S} and DtS≔Dt∧SD\_{t}^{S}\coloneqq D\_{t\wedge S}.

Let now 𝒯0\mathcal{T}\_{0} be the set of all stopping times. We extend the definition of the (g,D)(g,D)-conditional evaluation for each terminal stopping time τ∈𝒯0\tau\in\mathcal{T}\_{0} and each η∈L2​(𝒢τ)\eta\in L^{2}(\mathcal{G}\_{\tau}) as the first component of the solution of the BSDE associated with terminal time TT, λ(p)\lambda^{(p)}-admissible driver gτ​(t,⋅)≔g​(t,⋅)​𝟙t≤τg^{\tau}(t,\cdot)\coloneqq g(t,\cdot)\mathbbm{1}\_{t\leq\tau} and optional process Dtτ≔Dt∧τD\_{t}^{\tau}\coloneqq D\_{t\wedge\tau}.

Some properties of the non-linear (g,D)(g,D)-evaluations are as follows (cf. [[7](https://arxiv.org/html/2601.01250v1#bib.bib7)] for the single default jump case):

* •

  Consistency: Let τ,τ′∈𝒯0\tau,\tau^{\prime}\in\mathcal{T}\_{0} be such that τ≤τ′\tau\leq\tau^{\prime} a.s. and let η∈L2​(𝒢τ′)\eta\in L^{2}(\mathcal{G}\_{\tau^{\prime}}). Then, ℰt,τ′g,D​(η)=ℰt,τg,D​(ℰτ,τ′g,D​(η))\mathscr{E}\_{t,\tau^{\prime}}^{g,D}(\eta)=\mathscr{E}\_{t,\tau}^{g,D}(\mathscr{E}\_{\tau,\tau^{\prime}}^{g,D}(\eta)) a.s.
* •

  Generalized Zero-One Law: Let τ∈𝒯0\tau\in\mathcal{T}\_{0}, let η∈L2​(𝒢τ)\eta\in L^{2}(\mathcal{G}\_{\tau}). For t∈[0,T]t\in[0,T] and for A∈ℱt,A\in\mathcal{F}\_{t}, we have,

  |  |  |  |
  | --- | --- | --- |
  |  | ℰt,τgA,DA​(𝟙A​η)=𝟙A​ℰt,τg,D​(η)​ a.s.,\mathscr{E}\_{t,\tau}^{g^{A},D^{A}}(\mathbbm{1}\_{A}\eta)=\mathbbm{1}\_{A}\mathscr{E}\_{t,\tau}^{g,D}(\eta)\text{ a.s.,} |  |

  where gA​(s,⋅)≔g​(s,⋅)​𝟙A​𝟙(t,T]​(s)g^{A}(s,\cdot)\coloneqq g(s,\cdot)\mathbbm{1}\_{A}\mathbbm{1}\_{(t,T]}(s) and DsA≔(Ds−Dt)​𝟙A​𝟙s≥t.D\_{s}^{A}\coloneqq(D\_{s}-D\_{t})\mathbbm{1}\_{A}\mathbbm{1}\_{s\geq t}. In the case where D=0D=0, this property has been established in [[13](https://arxiv.org/html/2601.01250v1#bib.bib13)] (in the case of a Brownian-Poisson filtration).
* •

  Monotonicity: Using the comparison theorem (Theorem [2.17](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem17 "Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), under Assumption [3.2.1](https://arxiv.org/html/2601.01250v1#S3.Thmtheorem2.Thmassumption1 "Assumption 3.2.1: ‣ 3.2.1 Properties of the Non-linear Pricing System 𝐗^𝑔 in the Case of 𝑝 Defaultable Assets ‣ 3.2 Pricing in a Non-linear Complete Market with 𝑝 Defaultable Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), the (g,D)(g,D)-conditional evaluation ℰg,D​(⋅)\mathscr{E}^{g,D}(\cdot) is monotone with respect to the terminal payoff.
* •

  Convexity: Under Assumption [3.2.1](https://arxiv.org/html/2601.01250v1#S3.Thmtheorem2.Thmassumption1 "Assumption 3.2.1: ‣ 3.2.1 Properties of the Non-linear Pricing System 𝐗^𝑔 in the Case of 𝑝 Defaultable Assets ‣ 3.2 Pricing in a Non-linear Complete Market with 𝑝 Defaultable Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), if we further assume that gg is convex with respect to the vector (y,z,k1,…,kp)(y,z,k^{1},\ldots,k^{p}), then ℰg,D​(⋅)\mathscr{E}^{g,D}(\cdot) is convex with respect to the terminal payoff.
* •

  No Arbitrage Property: Under Assumption [3.2.1](https://arxiv.org/html/2601.01250v1#S3.Thmtheorem2.Thmassumption1 "Assumption 3.2.1: ‣ 3.2.1 Properties of the Non-linear Pricing System 𝐗^𝑔 in the Case of 𝑝 Defaultable Assets ‣ 3.2 Pricing in a Non-linear Complete Market with 𝑝 Defaultable Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), if we further assume that for each i∈{1,…,p}i\in\{1,\ldots,p\}, γty,z,ki,k^i>−1,\gamma\_{t}^{y,z,k^{i},\hat{k}^{i}}>-1, d​P⊗d​tdP\otimes dt-a.e., then by the strict comparison Theorem (Theorem [2.17](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem17 "Theorem 2.17 (Comparison and Strict Comparison for BSDEs with Multiple Default Jumps): ‣ 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") (ii)), ℰg,D\mathscr{E}^{g,D} has the no arbitrage property.

We now present two examples.

### 3.3 Example: Large Seller who Affects the ii-th Default Probability

We place ourselves in the same probabilistic framework as in Subsection [3.2](https://arxiv.org/html/2601.01250v1#S3.SS2 "3.2 Pricing in a Non-linear Complete Market with 𝑝 Defaultable Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"). We consider a European option with maturity T>0T>0, terminal payoff η∈L2​(𝒢T)\eta\in L^{2}(\mathcal{G}\_{T}) and an optional dividend process D∈𝒜T2D\in\mathcal{A}\_{T}^{2}. We consider the situation where the seller of this European option is a large trader. The hedging strategy of the trader (and its associated wealth process) may affect the default probabilities of the assets. For this example we assume that the large seller only affects the ii-th default probability (where ii is a fixed index). We also assume that the ii-th default intensity is bounded. The large seller takes this feedback effect into consideration for their market model.

Let ii be a fixed index in {1,…,p}\{1,\ldots,p\} (in the whole sub-section). We are given a family of probability measures parametrized by the risky-asset strategy ϕ\phi and the (self-financing) wealth process VV. More precisely, let ϕ∈ℋ2×ℋλ12×⋯×ℋλp2\phi\in\mathcal{H}^{2}\times\mathcal{H}\_{\lambda^{1}}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p}}^{2} and let V∈𝒮2V\in\mathcal{S}^{2}. Let QV,ϕ,iQ^{V,\phi,i} be the probability measure defined by the Radon-Nikodym density process (with respect to PP):

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​QV,ϕ,id​P|𝒢t=LtV,ϕ,i,\left.\frac{dQ^{V,\phi,i}}{dP}\right|\_{\mathcal{G}\_{t}}=L\_{t}^{V,\phi,i}, |  | (3.23) |

where LV,ϕ,iL^{V,\phi,i} is the solution of the SDE,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​LtV,ϕ,i=Lt−V,ϕ,i​γi​(t,Vt−,ϕt)​d​Mti;L0V,ϕ,i=1.dL\_{t}^{V,\phi,i}=L\_{t-}^{V,\phi,i}\gamma^{i}(t,V\_{t-},\phi\_{t})dM\_{t}^{i};\quad L\_{0}^{V,\phi,i}=1. |  | (3.24) |

We introduce the following assumption on the function γi\gamma^{i}.

###### Assumption 3.5.1:

The function γi:(ω,t,y,ϕ0,ϕ1,…,ϕp)↦γi​(ω,t,y,ϕ0,ϕ1,…,ϕp)\gamma^{i}:(\omega,t,y,\phi^{0},\phi^{1},\ldots,\phi^{p})\mapsto\gamma^{i}(\omega,t,y,\phi^{0},\phi^{1},\ldots,\phi^{p}) is a 𝒫⊗ℬ​(ℝp+2)\mathcal{P}\otimes\mathcal{B}(\mathbb{R}^{p+2})-measurable function defined on Ω×[0,T]×ℝp+2\Omega\times[0,T]\times\mathbb{R}^{p+2}, bounded, and such that the map y↦γi​(ω,t,y,ϕ0,ϕ1,…,ϕp)/ϕiy\mapsto\gamma^{i}(\omega,t,y,\phi^{0},\phi^{1},\ldots,\phi^{p})/\phi^{i} is uniformly Lipschitz. In addition we assume that γi​(t,⋅)>−1\gamma^{i}(t,\cdot)>-1, d​t⊗d​Pdt\otimes dP-a.e.

In the financial context, we use the function γi\gamma^{i} to represent the influence of the seller’s strategy on the default intensity of the ii-th asset, where ϕ\phi is the seller’s risky-asset strategy and VV is the value of their portfolio.

By Assumption [3.5.1](https://arxiv.org/html/2601.01250v1#S3.Thmtheorem5.Thmassumption1 "Assumption 3.5.1: ‣ 3.3 Example: Large Seller who Affects the 𝑖-th Default Probability ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), Remark [2.12](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem12 "Remark 2.12: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") and Proposition [2.13](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem13 "Proposition 2.13: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), the process LV,ϕ,iL^{V,\phi,i} is positive and belongs to 𝒮2\mathcal{S}^{2}.

Using Girsanov’s theorem (and our assumptions on λi\lambda\_{i} and γi\gamma^{i}) the process (WtV,ϕ,i)(W\_{t}^{V,\phi,i}) hereafter is a QV,ϕ,iQ^{V,\phi,i}-Brownian motion and the process (MtV,ϕ,i)(M\_{t}^{V,\phi,i}) is a QV,ϕ,iQ^{V,\phi,i}- martingale, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | WtV,ϕ,i≔Wt−∫0td​⟨W,LV,ϕ,i⟩sLs−V,ϕ,i=Wt;\displaystyle\begin{aligned} W\_{t}^{V,\phi,i}&\coloneqq W\_{t}-\int\_{0}^{t}\frac{d\langle W,L^{V,\phi,i}\rangle\_{s}}{L\_{s-}^{V,\phi,i}}=W\_{t};\end{aligned} |  | (3.25) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | MtV,ϕ,i≔Mti−∫0td​⟨Mi,LV,ϕ,i⟩sLs−V,ϕ,i=Mti−∫0tγi​(s,Vs−,ϕs)​λsi​𝑑s\displaystyle\begin{aligned} M\_{t}^{V,\phi,i}&\coloneqq M\_{t}^{i}-\int\_{0}^{t}\frac{d\langle M^{i},L^{V,\phi,i}\rangle\_{s}}{L\_{s-}^{V,\phi,i}}=M\_{t}^{i}-\int\_{0}^{t}\gamma^{i}(s,V\_{s-},\phi\_{s})\lambda\_{s}^{i}ds\end{aligned} |  | (3.26) |

Hence under QV,ϕ,iQ^{V,\phi,i}, the ii-th 𝔾\mathbb{G}-default intensity process is equal to λti​(1+γi​(t,Vt−,ϕt))\lambda\_{t}^{i}(1+\gamma^{i}(t,V\_{t-},\phi\_{t})) since we can rewrite ([3.26](https://arxiv.org/html/2601.01250v1#S3.E26 "In 3.3 Example: Large Seller who Affects the 𝑖-th Default Probability ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) as,

|  |  |  |
| --- | --- | --- |
|  | MtV,ϕ,i≔Mti−∫0tγi​(s,V−,ϕs)​λsi​𝑑s=Nti−∫0tλsi​(1+γi​(s,Vs−,ϕs))​𝑑s.M\_{t}^{V,\phi,i}\coloneqq M\_{t}^{i}-\int\_{0}^{t}\gamma^{i}(s,V\_{-},\phi\_{s})\lambda\_{s}^{i}ds=N\_{t}^{i}-\int\_{0}^{t}\lambda\_{s}^{i}(1+\gamma^{i}(s,V\_{s-},\phi\_{s}))ds. |  |

###### Remark 3.6:

For the case j≠ij\neq i (where j∈{1,…,p}j\in\{1,\ldots,p\}), we have MtV,ϕ,j:=MtjM\_{t}^{V,\phi,j}:=M\_{t}^{j} is a QV,ϕ,iQ^{V,\phi,i}-martingale, by Girsanov’s theorem. This is true as P​(τj=τi)=0P(\tau\_{j}=\tau\_{i})=0 for all j∈{1,…,p}j\in\{1,\ldots,p\} such that j≠ij\neq i (hence, ⟨Mj,Mi⟩s=0\langle M^{j},M^{i}\rangle\_{s}=0 for j≠ij\neq i).

The large seller then considers the following pricing model, which takes into account their impact on the market. For a fixed pair (V,ϕ)∈𝒮2×ℋ2×ℋλ12×⋯×ℋλp2(V,\phi)\in\mathcal{S}^{2}\times\mathcal{H}^{2}\times\mathcal{H}\_{\lambda^{1}}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p}}^{2}, which we call the wealth/risky-asset strategy pair, we have the following dynamics of the p+1p+1 risky assets under the probability QV,ϕ,iQ^{V,\phi,i},

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St0\displaystyle dS\_{t}^{0} | =St0​[μt0​d​t+σt0​d​Wt],\displaystyle=S\_{t}^{0}[\mu\_{t}^{0}dt+\sigma\_{t}^{0}dW\_{t}], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Stj\displaystyle dS\_{t}^{j} | =St−j​[μtj​d​t+σtj​d​Wt+βtj​d​Mtj],j≠i, ​j∈{1,…,p}\displaystyle=S\_{t-}^{j}[\mu\_{t}^{j}dt+\sigma\_{t}^{j}dW\_{t}+\beta\_{t}^{j}dM\_{t}^{j}],\quad j\neq i,\text{ }j\in\{1,\ldots,p\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sti\displaystyle dS\_{t}^{i} | =St−i​[μti​d​t+σti​d​Wt+βti​d​MtV,ϕ,i].\displaystyle=S\_{t-}^{i}[\mu\_{t}^{i}dt+\sigma\_{t}^{i}dW\_{t}+\beta\_{t}^{i}dM\_{t}^{V,\phi,i}]. |  |

The value process (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]} of the seller’s portfolio associated with an initial wealth x∈ℝx\in\mathbb{R}, a risky-asset strategy ϕ\phi, and an optional cumulative withdrawal process (which the seller will choose to be equal to the optional dividend process DD of the option), satisfies the following dynamics,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​Vt=−(rt​Vt+ϕt′​σt​Θt0+∑j=1pϕtj​βtj​Θtj​λtj)​d​t+d​Dt−ϕt′​σt​d​Wt−∑j=1j≠ipϕtj​βtj​d​Mtj−ϕti​βti​d​MtV,ϕ,i,V0=x,-dV\_{t}=-\left(r\_{t}V\_{t}+\phi\_{t}^{\prime}\sigma\_{t}\Theta\_{t}^{0}+\sum\_{j=1}^{p}\phi\_{t}^{j}\beta\_{t}^{j}\Theta\_{t}^{j}\lambda\_{t}^{j}\right)dt+dD\_{t}-\phi\_{t}^{\prime}\sigma\_{t}dW\_{t}\\ -\sum\_{\begin{subarray}{c}j=1\\ j\neq i\end{subarray}}^{p}\phi\_{t}^{j}\beta\_{t}^{j}dM\_{t}^{j}-\phi\_{t}^{i}\beta\_{t}^{i}dM\_{t}^{V,\phi,i},\quad V\_{0}=x, |  | (3.27) |

where ϕt′​σt=∑j=0pϕtj​σtj\phi\_{t}^{\prime}\sigma\_{t}=\sum\_{j=0}^{p}\phi\_{t}^{j}\sigma\_{t}^{j} and,

|  |  |  |
| --- | --- | --- |
|  | Θt0=μt0−rtσt0,Θtj=μtj−rt−σtj​Θt0βtj​λtj​𝟙{βtj​λtj≠0}, for ​j∈{1,…,p}.\Theta\_{t}^{0}=\frac{\mu\_{t}^{0}-r\_{t}}{\sigma\_{t}^{0}},\quad\Theta\_{t}^{j}=\frac{\mu\_{t}^{j}-r\_{t}-\sigma\_{t}^{j}\Theta\_{t}^{0}}{\beta\_{t}^{j}\lambda\_{t}^{j}}\mathbbm{1}\_{\{\beta\_{t}^{j}\lambda\_{t}^{j}\neq 0\}},\text{ for }j\in\{1,\ldots,p\}. |  |

Using the expression for MtV,ϕ,iM\_{t}^{V,\phi,i} from ([3.26](https://arxiv.org/html/2601.01250v1#S3.E26 "In 3.3 Example: Large Seller who Affects the 𝑖-th Default Probability ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), we obtain,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​Vt=−(rt​Vt+ϕt′​σt​Θt0+∑j=1pϕtj​βtj​Θtj​λtj+γi​(t,Vt−,ϕt)​λti​ϕti​βti)​d​t+d​Dt−ϕt′​σt​d​Wt−∑j=1pϕtj​βtj​d​Mtj,V0=x.-dV\_{t}=-\left(r\_{t}V\_{t}+\phi\_{t}^{\prime}\sigma\_{t}\Theta\_{t}^{0}+\sum\_{j=1}^{p}\phi\_{t}^{j}\beta\_{t}^{j}\Theta\_{t}^{j}\lambda\_{t}^{j}+\gamma^{i}(t,V\_{t-},\phi\_{t})\lambda\_{t}^{i}\phi\_{t}^{i}\beta\_{t}^{i}\right)dt+dD\_{t}\\ -\phi\_{t}^{\prime}\sigma\_{t}dW\_{t}-\sum\_{j=1}^{p}\phi\_{t}^{j}\beta\_{t}^{j}dM\_{t}^{j},\quad V\_{0}=x. |  | (3.28) |

By Assumption [3.5.1](https://arxiv.org/html/2601.01250v1#S3.Thmtheorem5.Thmassumption1 "Assumption 3.5.1: ‣ 3.3 Example: Large Seller who Affects the 𝑖-th Default Probability ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") on γi\gamma^{i}, for a given risky-asset strategy ϕ\phi, there exists a unique process Vx,ϕV^{x,\phi} satisfying the forward SDE ([3.28](https://arxiv.org/html/2601.01250v1#S3.E28 "In 3.3 Example: Large Seller who Affects the 𝑖-th Default Probability ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) with initial condition V0x,ϕ=xV\_{0}^{x,\phi}=x, where xx is the initial wealth of the investor.

We set Zt≔ϕt′​σtZ\_{t}\coloneq\phi\_{t}^{\prime}\sigma\_{t} and, for each j∈{1,…,p}j\in\{1,\ldots,p\}, Ktj≔βtj​ϕtjK\_{t}^{j}\coloneq\beta\_{t}^{j}\phi\_{t}^{j}. The dynamics of ([3.28](https://arxiv.org/html/2601.01250v1#S3.E28 "In 3.3 Example: Large Seller who Affects the 𝑖-th Default Probability ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) can be rewritten as,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​Vt=g​(t,Vt,Zt,Kt1,…,Ktp)​d​t+d​Dt−Zt​d​Wt−∑j=1pKtj​d​Mtj,V0=x,-dV\_{t}=g(t,V\_{t},Z\_{t},K\_{t}^{1},\ldots,K\_{t}^{p})dt+dD\_{t}-Z\_{t}dW\_{t}-\sum\_{j=1}^{p}K\_{t}^{j}dM\_{t}^{j},\quad V\_{0}=x, |  | (3.29) |

where the function gg is defined by,

|  |  |  |
| --- | --- | --- |
|  | g​(t,y,z,k1,…,kp)≔−rt​y−Θt0​z−∑j=1pΘtj​λtj​kj−γi​(t,y,z−∑j=1pkj​σtjβtjσt0,k1βt1,…,kpβtp)​λti​ki.g(t,y,z,k^{1},\ldots,k^{p})\coloneqq-r\_{t}y-\Theta\_{t}^{0}z-\sum\_{j=1}^{p}\Theta\_{t}^{j}\lambda\_{t}^{j}k^{j}\\ -\gamma^{i}\Big(t,y,\frac{z-\sum\_{j=1}^{p}\frac{k^{j}\sigma\_{t}^{j}}{\beta\_{t}^{j}}}{\sigma\_{t}^{0}},\frac{k^{1}}{\beta\_{t}^{1}},\ldots,\frac{k^{p}}{\beta\_{t}^{p}}\Big)\lambda\_{t}^{i}k^{i}. |  |

If we assume that that there exists C>0C>0 such that gg satisfies ([2.3](https://arxiv.org/html/2601.01250v1#S2.E3 "In Definition 2.2 (𝜆^(𝑝)-Admissible Driver): ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), then gg is a λ(p)\lambda^{(p)}-admissible driver (Definition [2.2](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem2 "Definition 2.2 (𝜆^(𝑝)-Admissible Driver): ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")).

Hence, for an option with pay-off η\eta at time TT and intermediate optional process DD, we have a particular case of the pricing system 𝐗g​(η,D)\mathbf{X}^{g}(\eta,D) from Subsection [3.2.1](https://arxiv.org/html/2601.01250v1#S3.SS2.SSS1 "3.2.1 Properties of the Non-linear Pricing System 𝐗^𝑔 in the Case of 𝑝 Defaultable Assets ‣ 3.2 Pricing in a Non-linear Complete Market with 𝑝 Defaultable Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), where gg is the above non-linear driver. From Subsection [3.2](https://arxiv.org/html/2601.01250v1#S3.SS2 "3.2 Pricing in a Non-linear Complete Market with 𝑝 Defaultable Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), the seller’s price process is equal to XX, where XX is the first component of the solution (X,Z,K1,…,Kp)(X,Z,K^{1},\ldots,K^{p}) to the BSDE,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​Xt=g​(t,Xt,Zt,Kt1,…,Ktp)​d​t+d​Dt−Zt​d​Wt−∑j=1pKtj​d​Mtj,XT=η.-dX\_{t}=g(t,X\_{t},Z\_{t},K\_{t}^{1},\ldots,K\_{t}^{p})dt+dD\_{t}-Z\_{t}dW\_{t}-\sum\_{j=1}^{p}K\_{t}^{j}dM\_{t}^{j},\quad X\_{T}=\eta. |  | (3.30) |

Furthermore the seller’s hedging strategy ϕ\phi is obtained by the change of variables formula,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚽:ℋT2×ℋλ1,T2×⋯×ℋλp,T2→ℋT2×ℋλ1,T2×⋯×ℋλp,T2,(Z,K1,…,Kp)↦𝚽​(Z,K1,…,Kp)≔ϕ=(ϕ0,ϕ1,…,ϕp),\displaystyle\begin{aligned} \mathbf{\Phi}:\mathcal{H}\_{T}^{2}\times\mathcal{H}\_{\lambda^{1},T}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p},T}^{2}&\rightarrow\mathcal{H}\_{T}^{2}\times\mathcal{H}\_{\lambda^{1},T}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p},T}^{2},\\ (Z,K^{1},\ldots,K^{p})&\mapsto\mathbf{\Phi}(Z,K^{1},\ldots,K^{p})\coloneqq\phi=(\phi^{0},\phi^{1},\ldots,\phi^{p}),\end{aligned} |  | (3.31) |

where

|  |  |  |
| --- | --- | --- |
|  | ϕt0=Zt0−∑j=1pKtj​σtjβtjσt0;ϕtj=Ktjβtj​ for all ​j∈{1,…,p}.\phi\_{t}^{0}=\frac{Z\_{t}^{0}-\sum\_{j=1}^{p}\frac{K\_{t}^{j}\sigma\_{t}^{j}}{\beta\_{t}^{j}}}{\sigma\_{t}^{0}};\quad\phi\_{t}^{j}=\frac{K\_{t}^{j}}{\beta\_{t}^{j}}\text{ for all }j\in\{1,\ldots,p\}. |  |

### 3.4 Example: Large Seller who Affects all pp Default Probabilities

In this example, we assume that the large seller affects all pp default probabilities. We also assume in this example that, for each i∈{1,…,p}i\in\{1,...,p\}, the ii-th default intensity is bounded.

Let 𝒬V,ϕ\mathcal{Q}^{V,\phi} be the probability measure, defined by the Radon-Nikodym density process (with respect to PP):

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​𝒬V,ϕd​P|𝒢t=ℒtV,ϕ,\left.\frac{d\mathcal{Q}^{V,\phi}}{dP}\right|\_{\mathcal{G}\_{t}}=\mathscr{L}\_{t}^{V,\phi}, |  | (3.32) |

where ℒV,ϕ\mathscr{L}^{V,\phi} is the solution to the SDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℒtV,ϕ=ℒt−V,ϕ​(∑i=1pγi​(t,Vt−,ϕt)​d​Mti);ℒ0V,ϕ=1.d\mathscr{L}\_{t}^{V,\phi}=\mathscr{L}\_{t-}^{V,\phi}\left(\sum\_{i=1}^{p}\gamma^{i}(t,V\_{t-},\phi\_{t})dM\_{t}^{i}\right);\quad\mathscr{L}\_{0}^{V,\phi}=1. |  | (3.33) |

###### Assumption 3.6.1:

For each i∈{1,…,p}i\in\{1,\ldots,p\}, the function γi\gamma^{i} satisfies Assumption [3.5.1](https://arxiv.org/html/2601.01250v1#S3.Thmtheorem5.Thmassumption1 "Assumption 3.5.1: ‣ 3.3 Example: Large Seller who Affects the 𝑖-th Default Probability ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach").

By Assumption [3.6.1](https://arxiv.org/html/2601.01250v1#S3.Thmtheorem6.Thmassumption1 "Assumption 3.6.1: ‣ 3.4 Example: Large Seller who Affects all 𝑝 Default Probabilities ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), Remark [2.12](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem12 "Remark 2.12: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") and Proposition [2.13](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem13 "Proposition 2.13: ‣ 2.2.3 Generalized 𝜆^(𝑝)-Linear BSDEs with Multiple Default Jumps ‣ 2.2 BSDE with Multiple Default Jumps: Properties ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), the process ℒV,ϕ\mathscr{L}^{V,\phi} is positive and belongs to the space 𝒮2\mathcal{S}^{2}.

By Girsanov’s theorem (and our assumptions), the process (𝒲tV,ϕ)(\mathscr{W}\_{t}^{V,\phi}) hereafter is a 𝒬V,ϕ\mathcal{Q}^{V,\phi}-Brownian motion and, for each i∈{1,…,p}i\in\{1,\ldots,p\}, the process (ℳtV,ϕ,i)(\mathscr{M}\_{t}^{V,\phi,i}) is a 𝒬V,ϕ\mathcal{Q}^{V,\phi}- martingale, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒲tV,ϕ≔Wt−∫0td​⟨W,ℒV,ϕ⟩sℒs−V,ϕ=Wt, and,\displaystyle\begin{aligned} \mathscr{W}\_{t}^{V,\phi}&\coloneqq W\_{t}-\int\_{0}^{t}\frac{d\langle W,\mathscr{L}^{V,\phi}\rangle\_{s}}{\mathscr{L}\_{s-}^{V,\phi}}=W\_{t},\text{ and,}\end{aligned} |  | (3.34) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳtV,ϕ,i≔Mti−∫0t∑j=1pγj​(s,Vs−,ϕs)​d​⟨Mj,Mi⟩s=Mti−∫0tγi​(s,Vs−,ϕs)​λsi​𝑑s.\displaystyle\begin{aligned} \mathscr{M}\_{t}^{V,\phi,i}&\coloneqq M\_{t}^{i}-\int\_{0}^{t}\sum\_{j=1}^{p}\gamma^{j}(s,V\_{s-},\phi\_{s})d\langle M^{j},M^{i}\rangle\_{s}=M\_{t}^{i}-\int\_{0}^{t}\gamma^{i}(s,V\_{s-},\phi\_{s})\lambda\_{s}^{i}ds.\end{aligned} |  | (3.35) |

For the final equality in ([3.35](https://arxiv.org/html/2601.01250v1#S3.E35 "In 3.4 Example: Large Seller who Affects all 𝑝 Default Probabilities ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), we have used that P​(τi=τj)=0P(\tau\_{i}=\tau\_{j})=0 for all i,j∈{1,…,p}i,j\in\{1,\ldots,p\}, such that i≠ji\neq j.

Hence, under the measure 𝒬V,ϕ\mathcal{Q}^{V,\phi}, for each i∈{1,…,p}i\in\{1,\ldots,p\}; the ii-th 𝔾\mathbb{G}-default intensity process is equal to λti​(1+γi​(t,Vt−,ϕt))\lambda\_{t}^{i}(1+\gamma^{i}(t,V\_{t-},\phi\_{t})) since we can rewrite ([3.35](https://arxiv.org/html/2601.01250v1#S3.E35 "In 3.4 Example: Large Seller who Affects all 𝑝 Default Probabilities ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) as,

|  |  |  |
| --- | --- | --- |
|  | ℳtV,ϕ,i≔Mti−∫0tγi​(s,Vs−,ϕs)​λsi​𝑑s=Nti−∫0tλsi​(1+γi​(s,Vs−,ϕs))​𝑑s.\mathscr{M}\_{t}^{V,\phi,i}\coloneqq M\_{t}^{i}-\int\_{0}^{t}\gamma^{i}(s,V\_{s-},\phi\_{s})\lambda\_{s}^{i}ds=N\_{t}^{i}-\int\_{0}^{t}\lambda\_{s}^{i}(1+\gamma^{i}(s,V\_{s-},\phi\_{s}))ds. |  |

For a given wealth/risky-asset strategy pair (V,ϕ)∈𝒮2×ℋ2×ℋλ12×⋯×ℋλp2(V,\phi)\in\mathcal{S}^{2}\times\mathcal{H}^{2}\times\mathcal{H}\_{\lambda^{1}}^{2}\times\cdots\times\mathcal{H}\_{\lambda^{p}}^{2}, the p+1p+1 risky assets have the following dynamics under 𝒬V,ϕ\mathcal{Q}^{V,\phi}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St0\displaystyle dS\_{t}^{0} | =St0​[μt0​d​t+σt0​d​Wt],\displaystyle=S\_{t}^{0}[\mu\_{t}^{0}dt+\sigma\_{t}^{0}dW\_{t}], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Sti\displaystyle dS\_{t}^{i} | =St−i​[μti​d​t+σti​d​Wt+βti​d​ℳtV,ϕ,i],i∈{1,…,p}.\displaystyle=S\_{t-}^{i}[\mu\_{t}^{i}dt+\sigma\_{t}^{i}dW\_{t}+\beta\_{t}^{i}d\mathscr{M}\_{t}^{V,\phi,i}],\quad i\in\{1,\ldots,p\}. |  |

The value process (Vt)t∈[0,T](V\_{t})\_{t\in[0,T]} of the seller’s portfolio associated with an initial wealth x∈ℝx\in\mathbb{R}, a risky-asset strategy ϕ\phi, and a cumulative withdrawal optional process (which the seller chooses in such a way as to be equal to the optional dividend process DD of the option,) satisfies the following,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​Vt=−(rt​Vt+ϕt′​σt​Θt0+∑i=1pϕti​βti​Θti​λti)​d​t+d​Dt−ϕt′​σt​d​Wt−∑i=1pϕti​βti​d​ℳtV,ϕ,i,V0=x,-dV\_{t}=-\left(r\_{t}V\_{t}+\phi\_{t}^{\prime}\sigma\_{t}\Theta\_{t}^{0}+\sum\_{i=1}^{p}\phi\_{t}^{i}\beta\_{t}^{i}\Theta\_{t}^{i}\lambda\_{t}^{i}\right)dt+dD\_{t}\\ -\phi\_{t}^{\prime}\sigma\_{t}dW\_{t}-\sum\_{i=1}^{p}\phi\_{t}^{i}\beta\_{t}^{i}d\mathscr{M}\_{t}^{V,\phi,i},\quad V\_{0}=x, |  | (3.36) |

where we have ϕt′​σt≔∑i=0pϕti​σti\phi\_{t}^{\prime}\sigma\_{t}\coloneqq\sum\_{i=0}^{p}\phi\_{t}^{i}\sigma\_{t}^{i} and,

|  |  |  |
| --- | --- | --- |
|  | Θt0=μt0−rtσt0,Θti=μti−rt−σti​Θt0βti​λti​𝟙{βti​λti≠0}, for ​i∈{1,…,p}.\Theta\_{t}^{0}=\frac{\mu\_{t}^{0}-r\_{t}}{\sigma\_{t}^{0}},\quad\Theta\_{t}^{i}=\frac{\mu\_{t}^{i}-r\_{t}-\sigma\_{t}^{i}\Theta\_{t}^{0}}{\beta\_{t}^{i}\lambda\_{t}^{i}}\mathbbm{1}\_{\{\beta\_{t}^{i}\lambda\_{t}^{i}\neq 0\}},\text{ for }i\in\{1,\ldots,p\}. |  |

We use the expression for ℳtV,ϕ,i\mathscr{M}\_{t}^{V,\phi,i} from ([3.35](https://arxiv.org/html/2601.01250v1#S3.E35 "In 3.4 Example: Large Seller who Affects all 𝑝 Default Probabilities ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) to obtain,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​Vt=−(rt​Vt+ϕt′​σt​Θt0+∑i=1pϕti​βti​Θti​λti+∑i=1pγi​(t,Vt−,ϕt)​λti​ϕti​βti)​d​t+d​Dt−ϕt′​σt​d​Wt−∑i=1pϕti​βti​d​Mti,V0=x.-dV\_{t}=-\left(r\_{t}V\_{t}+\phi\_{t}^{\prime}\sigma\_{t}\Theta\_{t}^{0}+\sum\_{i=1}^{p}\phi\_{t}^{i}\beta\_{t}^{i}\Theta\_{t}^{i}\lambda\_{t}^{i}+\sum\_{i=1}^{p}\gamma^{i}(t,V\_{t-},\phi\_{t})\lambda\_{t}^{i}\phi\_{t}^{i}\beta\_{t}^{i}\right)dt+dD\_{t}\\ -\phi\_{t}^{\prime}\sigma\_{t}dW\_{t}-\sum\_{i=1}^{p}\phi\_{t}^{i}\beta\_{t}^{i}dM\_{t}^{i},\quad V\_{0}=x. |  | (3.37) |

By Assumption [3.6.1](https://arxiv.org/html/2601.01250v1#S3.Thmtheorem6.Thmassumption1 "Assumption 3.6.1: ‣ 3.4 Example: Large Seller who Affects all 𝑝 Default Probabilities ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), for a given strategy ϕ\phi, there exists a unique process Vx,ϕV^{x,\phi} satisfying ([3.37](https://arxiv.org/html/2601.01250v1#S3.E37 "In 3.4 Example: Large Seller who Affects all 𝑝 Default Probabilities ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) with initial condition V0x,ϕ=xV\_{0}^{x,\phi}=x, where xx is the initial wealth of the trader.
Using ([3.37](https://arxiv.org/html/2601.01250v1#S3.E37 "In 3.4 Example: Large Seller who Affects all 𝑝 Default Probabilities ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) and setting Zt≔ϕt′​σtZ\_{t}\coloneq\phi\_{t}^{\prime}\sigma\_{t} and Kti≔βti​ϕtiK\_{t}^{i}\coloneq\beta\_{t}^{i}\phi\_{t}^{i}, for each i∈{1,…,p}i\in\{1,\ldots,p\}, we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | −d​Vt=g​(t,Vt,Zt,Kt1,…,Ktp)​d​t+d​Dt−Zt​d​Wt−∑i=1pKti​d​Mti,V0=x,-dV\_{t}=g(t,V\_{t},Z\_{t},K\_{t}^{1},\ldots,K\_{t}^{p})dt+dD\_{t}-Z\_{t}dW\_{t}-\sum\_{i=1}^{p}K\_{t}^{i}dM\_{t}^{i},\quad V\_{0}=x, |  | (3.38) |

where the function gg is defined by,

|  |  |  |
| --- | --- | --- |
|  | g​(t,y,z,k1,…,kp)≔−rt​y−Θt0​z−∑i=1pΘti​λti​ki−∑i=1pγi​(t,y,z−∑j=1pkj​σtjβtjσt0,k1βt1,…,kpβtp)​λti​ki.g(t,y,z,k^{1},\ldots,k^{p})\coloneqq-r\_{t}y-\Theta\_{t}^{0}z-\sum\_{i=1}^{p}\Theta\_{t}^{i}\lambda\_{t}^{i}k^{i}\\ -\sum\_{i=1}^{p}\gamma^{i}\Big(t,y,\frac{z-\sum\_{j=1}^{p}\frac{k^{j}\sigma\_{t}^{j}}{\beta\_{t}^{j}}}{\sigma\_{t}^{0}},\frac{k^{1}}{\beta\_{t}^{1}},\ldots,\frac{k^{p}}{\beta\_{t}^{p}}\Big)\lambda\_{t}^{i}k^{i}. |  |

If there exists C>0C>0 such that the function gg satisfies condition ([2.3](https://arxiv.org/html/2601.01250v1#S2.E3 "In Definition 2.2 (𝜆^(𝑝)-Admissible Driver): ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), then we have another example of the pricing system 𝐗g\mathbf{X}^{g} from Subsection [3.2.1](https://arxiv.org/html/2601.01250v1#S3.SS2.SSS1 "3.2.1 Properties of the Non-linear Pricing System 𝐗^𝑔 in the Case of 𝑝 Defaultable Assets ‣ 3.2 Pricing in a Non-linear Complete Market with 𝑝 Defaultable Assets ‣ 3 Pricing of European Options in Markets with Multiple Defaults ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"), where the non-linear driver gg is the one from above.

## Appendix A Some Technical Lemmas

###### Lemma A.1:

Let hh be a non-decreasing optional rcll process, with h0=0h\_{0}=0 and 𝔼​[hT2]<∞\mathbb{E}[h\_{T}^{2}]<\infty, that is, hh is a non-decreasing process in 𝒜T2\mathcal{A}\_{T}^{2}. Then hh has at most pp inaccessible jumps and these jumps occur at τ1,…,τp\tau\_{1},\ldots,\tau\_{p}. Moreover hh can be uniquely decomposed as follows ht=Bt+Δ​hτ1​𝟙{τ1≤t}+⋯+Δ​hτp​𝟙{τp≤t}=Bt+∑i=1p∫0tψti​𝑑Ntih\_{t}=B\_{t}+\Delta h\_{\tau\_{1}}\mathbbm{1}\_{\{\tau\_{1}\leq t\}}+\cdots+\Delta h\_{\tau\_{p}}\mathbbm{1}\_{\{\tau\_{p}\leq t\}}=B\_{t}+\sum\_{i=1}^{p}\int\_{0}^{t}\psi\_{t}^{i}dN\_{t}^{i}, where (Bt)t∈[0,T](B\_{t})\_{t\in[0,T]} is a (predictable) process in 𝒜p,T2\mathcal{A}\_{p,T}^{2} and for each i∈{1,…,p}i\in\{1,\ldots,p\}, ψi∈ℋλi,T2\psi^{i}\in\mathcal{H}\_{\lambda^{i},T}^{2}.

###### Proof.

Since hh is a square-integrable non-decreasing optional rcll process, hh is a square-integrable (rcll) submartingale. Thus, by the Doob-Meyer decomposition applied to hh, there exists a unique predictable process a∈𝒜p,T2a\in\mathcal{A}\_{p,T}^{2} and a unique square-integrable martingale mm with m0=0m\_{0}=0 such that ht=at+mth\_{t}=a\_{t}+m\_{t}. Using the martingale representation property from Theorem [2.1](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem1 "Theorem 2.1 (Martingale Representation Property): ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach") Eq. ([2.2](https://arxiv.org/html/2601.01250v1#S2.E2 "In Theorem 2.1 (Martingale Representation Property): ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), the 𝔾\mathbb{G}-martingale (mt)t∈[0,T](m\_{t})\_{t\in[0,T]} can be uniquely represented as mt=∫0tzs​𝑑Ws+∑i=1p∫0tψsi​𝑑Msim\_{t}=\int\_{0}^{t}z\_{s}dW\_{s}+\sum\_{i=1}^{p}\int\_{0}^{t}\psi\_{s}^{i}dM\_{s}^{i}, where z∈ℋT2z\in\mathcal{H}\_{T}^{2} and ψ1∈ℋλ1,T2,…,ψp∈ℋλp,T2\psi^{1}\in\mathcal{H}\_{\lambda^{1},T}^{2},\ldots,\psi^{p}\in\mathcal{H}\_{\lambda^{p},T}^{2}. Using d​Msi=d​Nsi−λsi​d​sdM\_{s}^{i}=dN\_{s}^{i}-\lambda\_{s}^{i}ds (from ([2.1](https://arxiv.org/html/2601.01250v1#S2.E1 "In 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"))), we get,

|  |  |  |
| --- | --- | --- |
|  | mt=∫0tzs​𝑑Ws−∑i=1p∫0tψsi​λsi​𝑑s+∑i=1p∫0tψsi​𝑑Nsi.m\_{t}=\int\_{0}^{t}z\_{s}dW\_{s}-\sum\_{i=1}^{p}\int\_{0}^{t}\psi\_{s}^{i}\lambda\_{s}^{i}ds+\sum\_{i=1}^{p}\int\_{0}^{t}\psi\_{s}^{i}dN\_{s}^{i}. |  |

Thus the process hh is uniquely written ht=at+∫0tzs​𝑑Ws−∑i=1p∫0tψsi​λsi​𝑑s+∑i=1p∫0tψsi​𝑑Nsih\_{t}=a\_{t}+\int\_{0}^{t}z\_{s}dW\_{s}-\sum\_{i=1}^{p}\int\_{0}^{t}\psi\_{s}^{i}\lambda\_{s}^{i}ds+\sum\_{i=1}^{p}\int\_{0}^{t}\psi\_{s}^{i}dN\_{s}^{i}. Setting Bt≔at+∫0tzs​𝑑Ws−∑i=1p∫0tψsi​λsi​𝑑sB\_{t}\coloneqq a\_{t}+\int\_{0}^{t}z\_{s}dW\_{s}-\sum\_{i=1}^{p}\int\_{0}^{t}\psi\_{s}^{i}\lambda\_{s}^{i}ds, we get,

|  |  |  |
| --- | --- | --- |
|  | ht=Bt+∑i=1p∫0tψsi​𝑑Nsi=Bt+∑i=1pψτii​𝟙{t≥τi}.h\_{t}=B\_{t}+\sum\_{i=1}^{p}\int\_{0}^{t}\psi\_{s}^{i}dN\_{s}^{i}=B\_{t}+\sum\_{i=1}^{p}\psi\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{t\geq\tau\_{i}\}}. |  |

The process BB is predictable since it is the sum of predictable terms. Moreover, BB is square-integrable.

The equality ht=Bt+∑i=1pψti​𝟙{t≥τi}h\_{t}=B\_{t}+\sum\_{i=1}^{p}\psi\_{t}^{i}\mathbbm{1}\_{\{t\geq\tau\_{i}\}}, together with the predictability of (Bt)(B\_{t}), the non-decreasingness of hh and the assumption that 0≤τ1<τ2<⋯<τp0\leq\tau\_{1}<\tau\_{2}<\cdots<\tau\_{p} a.s. implies that Δ​hτ1=ψτ11≥0\Delta h\_{\tau\_{1}}=\psi\_{\tau\_{1}}^{1}\geq 0 a.s. on {τ1≤T}\{\tau\_{1}\leq T\}, Δ​hτ2=ψτ22≥0\Delta h\_{\tau\_{2}}=\psi\_{\tau\_{2}}^{2}\geq 0 a.s. on {τ2≤T}\{\tau\_{2}\leq T\} and Δ​hτp=ψτpp≥0\Delta h\_{\tau\_{p}}=\psi\_{\tau\_{p}}^{p}\geq 0 a.s. on {τp≤T}\{\tau\_{p}\leq T\}, hence (Bt)(B\_{t}) is non-decreasing.
∎

###### Lemma A.2:

Let DD and D^\hat{D} be optional processes in 𝒜T2\mathcal{A}\_{T}^{2}. Let D′,D^′D^{\prime},\hat{D}^{\prime} in 𝒜p,T2\mathcal{A}\_{p,T}^{2} and θi,θ^i∈ℋλi,T2\theta^{i},\hat{\theta}^{i}\in\mathcal{H}\_{\lambda^{i},T}^{2} for i∈{1,…,p}i\in\{1,\ldots,p\}, be the unique processes such that,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt=Dt′+∫0t∑i=1pθsi​d​Nsi=Dt′+∑i=1pθτii​𝟙{τi≤t},a.s.D^t=D^t′+∫0t∑i=1pθ^si​d​Nsi=D^t′+∑i=1pθ^τii​𝟙{τi≤t},a.s.\displaystyle\begin{aligned} D\_{t}=D\_{t}^{\prime}+\int\_{0}^{t}\sum\_{i=1}^{p}\theta\_{s}^{i}dN\_{s}^{i}=D\_{t}^{\prime}+\sum\_{i=1}^{p}\theta\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{\tau\_{i}\leq t\}},\quad\text{a.s.}\\ \hat{D}\_{t}=\hat{D}\_{t}^{\prime}+\int\_{0}^{t}\sum\_{i=1}^{p}\hat{\theta}\_{s}^{i}dN\_{s}^{i}=\hat{D}\_{t}^{\prime}+\sum\_{i=1}^{p}\hat{\theta}\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{\tau\_{i}\leq t\}},\quad\text{a.s.}\end{aligned} |  | (A.1) |

If D¯≔D−D^\bar{D}\coloneqq D-\hat{D} is non-decreasing, then D¯′≔D′−D^′\bar{D}^{\prime}\coloneqq D^{\prime}-\hat{D}^{\prime} is non-decreasing and for each i∈{1,…,p}i\in\{1,\ldots,p\}, θτii≥θ^τii\theta\_{\tau\_{i}}^{i}\geq\hat{\theta}\_{\tau\_{i}}^{i} a.s. on {τi≤T}\{\tau\_{i}\leq T\}.

###### Proof.

We note that ([A.1](https://arxiv.org/html/2601.01250v1#A1.E1 "In Lemma A.2: ‣ Appendix A Some Technical Lemmas ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) holds by Proposition [2.6](https://arxiv.org/html/2601.01250v1#S2.Thmtheorem6 "Proposition 2.6: ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach"). Using ([A.1](https://arxiv.org/html/2601.01250v1#A1.E1 "In Lemma A.2: ‣ Appendix A Some Technical Lemmas ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) we have,

|  |  |  |  |
| --- | --- | --- | --- |
|  | D¯t≔D¯t′+(∑i=1p(θτii−θ^τii)​𝟙{τi≤t})=(Dt′−D^t′)+(∑i=1p(θτii−θ^τii)​𝟙{τi≤t}).\displaystyle\begin{aligned} \bar{D}\_{t}&\coloneqq\bar{D}\_{t}^{\prime}+\left(\sum\_{i=1}^{p}\left(\theta\_{\tau\_{i}}^{i}-\hat{\theta}\_{\tau\_{i}}^{i}\right)\mathbbm{1}\_{\{\tau\_{i}\leq t\}}\right)\\ &=\left(D\_{t}^{\prime}-\hat{D}\_{t}^{\prime}\right)+\left(\sum\_{i=1}^{p}\left(\theta\_{\tau\_{i}}^{i}-\hat{\theta}\_{\tau\_{i}}^{i}\right)\mathbbm{1}\_{\{\tau\_{i}\leq t\}}\right).\end{aligned} |  | (A.2) |

As an rcll predictable process does not jump at totally inaccessible stopping times (cf. [[17](https://arxiv.org/html/2601.01250v1#bib.bib17)], Proposition 2.24), we have Δ​D¯τi′=0\Delta\bar{D}^{\prime}\_{\tau\_{i}}=0 for all i∈{1,…,p}i\in\{1,\ldots,p\} a.s. Since, D¯\bar{D} is non-decreasing, we have, for i∈{1,…,p}i\in\{1,\ldots,p\}, Δ​D¯τi=θτii−θ^τii≥0\Delta\bar{D}\_{\tau\_{i}}=\theta\_{\tau\_{i}}^{i}-\hat{\theta}\_{\tau\_{i}}^{i}\geq 0 a.s.
  
Let us consider each of the sets AkA\_{k} from the partition from ([2.46](https://arxiv.org/html/2601.01250v1#S2.E46 "In 2.3 Comparison Theorems for BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")). On A0={τ1>T}A\_{0}=\{\tau\_{1}>T\},
we have D¯t​(ω)=Dt′​(ω)−D^t′​(ω)=D¯t′​(ω);\bar{D}\_{t}(\omega)=D\_{t}^{\prime}(\omega)-\hat{D}\_{t}^{\prime}(\omega)=\bar{D}^{\prime}\_{t}(\omega); hence, t↦D¯t′​(ω)t\mapsto\bar{D}^{\prime}\_{t}(\omega) is non-decreasing on A0A\_{0} (as t↦D¯t​(ω)t\mapsto\bar{D}\_{t}(\omega) is non-decreasing).
Let k∈{1,…,p−1}k\in\{1,\ldots,p-1\}. On AkA\_{k}, by reasoning successively for t∈[0,τ1​(ω))t\in[0,\tau\_{1}(\omega)) , …, for t∈[τk−1,τk​(ω))t\in[\tau\_{k-1},\tau\_{k}(\omega)), and for t∈[τk​(ω),T]t\in[\tau\_{k}(\omega),T], by using Eq. ([A.2](https://arxiv.org/html/2601.01250v1#A1.E2 "In Proof. ‣ Appendix A Some Technical Lemmas ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) and the assumption that D¯\bar{D} is non-decreasing, and by the fact that D¯′\bar{D}^{\prime} is predictable (and hence, does not jump at any of the τk\tau\_{k}’s), we get that t↦D¯t′​(ω)t\mapsto\bar{D}\_{t}^{\prime}(\omega) is non-decreasing on AkA\_{k}. Since, AkA\_{k} form a partition, we conclude.
∎

###### Lemma A.3:

The solution of the following forward SDE,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ζt=ζt−​(βt​d​Wt+∑i=1pγti​d​Mti);ζ0=0,d\zeta\_{t}=\zeta\_{t-}(\beta\_{t}dW\_{t}+\sum\_{i=1}^{p}\gamma\_{t}^{i}dM\_{t}^{i});\quad\zeta\_{0}=0, |  | (A.3) |

where the processes MiM^{i} are given by ([2.2](https://arxiv.org/html/2601.01250v1#S2.E2 "In Theorem 2.1 (Martingale Representation Property): ‣ 2.1 BSDEs with Multiple Default Jumps ‣ 2 The Underlying Probability Setup ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), is: for t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζt=exp⁡(∫0tβs​𝑑Ws−12​∫0tβs2​𝑑s)​exp⁡(−∫0t∑i=1pγsi​λsi​d​s)​∏i=1p(1+γτii​𝟙{τi≤t}), a.s.\zeta\_{t}=\exp\left(\int\_{0}^{t}\beta\_{s}dW\_{s}-\frac{1}{2}\int\_{0}^{t}\beta\_{s}^{2}ds\right)\exp\left(-\int\_{0}^{t}\sum\_{i=1}^{p}\gamma\_{s}^{i}\lambda\_{s}^{i}ds\right)\prod\_{i=1}^{p}(1+\gamma\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{\tau\_{i}\leq t\}}),\text{ a.s.} |  | (A.4) |

###### Proof.

The SDE from ([A.3](https://arxiv.org/html/2601.01250v1#A1.E3 "In Lemma A.3: ‣ Appendix A Some Technical Lemmas ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) can be solved by applying the Doléans-Dade formula (cf., for instance, [[17](https://arxiv.org/html/2601.01250v1#bib.bib17)]) to the semimartingale (Xt)t∈[0,T],(X\_{t})\_{t\in[0,T]}, where Xt≔∫0tβs​𝑑Ws+∫0t∑i=1pγsi​d​MsiX\_{t}\coloneqq\int\_{0}^{t}\beta\_{s}dW\_{s}+\int\_{0}^{t}\sum\_{i=1}^{p}\gamma\_{s}^{i}dM\_{s}^{i}, (with X0=0X\_{0}=0).
We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζt=ℰ​(X)t=exp⁡(Xt−X0−12​[Xc]t)​∏0<s≤t(1+Δ​Xs)​e−Δ​Xs,\zeta\_{t}=\mathcal{E}(X)\_{t}=\exp\left(X\_{t}-X\_{0}-\frac{1}{2}[X^{c}]\_{t}\right)\prod\_{0<s\leq t}(1+\Delta X\_{s})e^{-\Delta X\_{s}}, |  | (A.5) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | [Xc]t=∫0tβs2​𝑑s.[X^{c}]\_{t}=\int\_{0}^{t}\beta\_{s}^{2}ds. |  | (A.6) |

Since P​(τi=τj)=0P(\tau\_{i}=\tau\_{j})=0 for i,j∈{1,…,p}i,j\in\{1,\ldots,p\} such that i≠ji\neq j, we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∏0<s≤t(1+Δ​Xs)​e−Δ​Xs=exp⁡(−∫0t∑i=1pγsi​d​Msi−∫0t∑i=1pγsi​λsi​d​s)​∏i=1p(1+γτii​𝟙{τi≤t}).\displaystyle\begin{aligned} \prod\_{0<s\leq t}(1+\Delta X\_{s})e^{-\Delta X\_{s}}=\exp\left(-\int\_{0}^{t}\sum\_{i=1}^{p}\gamma\_{s}^{i}dM\_{s}^{i}-\int\_{0}^{t}\sum\_{i=1}^{p}\gamma\_{s}^{i}\lambda\_{s}^{i}ds\right)\prod\_{i=1}^{p}\left(1+\gamma\_{\tau\_{i}}^{i}\mathbbm{1}\_{\{\tau\_{i}\leq t\}}\right).\end{aligned} |  | (A.7) |

Substituting ([A.6](https://arxiv.org/html/2601.01250v1#A1.E6 "In Proof. ‣ Appendix A Some Technical Lemmas ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) and ([A.7](https://arxiv.org/html/2601.01250v1#A1.E7 "In Proof. ‣ Appendix A Some Technical Lemmas ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")) into ([A.5](https://arxiv.org/html/2601.01250v1#A1.E5 "In Proof. ‣ Appendix A Some Technical Lemmas ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")), we get the desired result ([A.4](https://arxiv.org/html/2601.01250v1#A1.E4 "In Lemma A.3: ‣ Appendix A Some Technical Lemmas ‣ European Options in Market Models with Multiple Defaults: the BSDE approach")).
∎

## References

* [1]
  Becherer, D., Büttner, M. & Kentia, K. On the monotone stability approach to BSDEs with jumps: Extensions, concrete criteria and examples. International Symposium On BSDEs. 1–41 (2017)
* [2]
  Bielecki, T., Björk, T., Jeanblanc, M., Rutkowski, M., Scheinkman, J., Xiong, W. Hedging of defaultable claims. Paris-Princeton Lectures On Mathematical Finance 2003. 1–132 (2004)
* [3]
   Bielecki, T., Jeanblanc, M., Rutkowski, M., PDE approach to valuation and hedging of credit derivatives,
  Quantitative finance 5, 257–270, (2005).
* [4]
  Bismut, J. Conjugate convex functions in optimal stochastic control. Journal Of Mathematical Analysis And Applications. 44, 384-404 (1973)
* [5]
  Crépey, S. Bilateral counterparty risk under funding constraints—Part I: Pricing. Mathematical Finance. 25, 1–22 (2015)
* [6]
  Delong, Ł. Backward stochastic differential equations with jumps and their actuarial and financial applications. (Springer, 2013)
* [7]
  Dumitrescu, R., Grigorova, M., Quenez, M. & Sulem, A. BSDEs with default jump. Computation And Combinatorics In Dynamics, Stochastics And Control: The Abel Symposium, Rosendal, Norway, August 2016. 233–263 (2018)
* [8]
  Dumitrescu, R., Quenez, M. & Sulem, A. Generalized Dynkin games and doubly reflected BSDEs with jumps. Electron. J. Probab. 21, 1–32 (2016)
* [9]
  El Karoui, N., Peng, S. & Quenez, M. Backward stochastic differential equations in finance. Mathematical Finance. 7, 1-71 (1997)
* [10]
  El Karoui, N. & Quenez, M. Non-linear pricing theory and backward stochastic differential equations. Financial Mathematics. pp. 191-246 (1997)
* [11]
  Kusuoka, S. A remark on default risk models. Advances In Mathematical Economics. 69–82 (1999)
* [12]
  Grigorian, K. & Jarrow, R. Enlargement of Filtrations: An Exposition of Core Ideas with Financial Examples. arXiv preprint arXiv:2303.03573. (2023)
* [13]
  Grigorova, M. & Quenez, M. Optimal stopping and a non-zero-sum Dynkin game in discrete time with risk measures induced by BSDEs. Stochastics. 89, 259–279 (2017)
* [14]
  Grigorova, M., Quenez, M. & Sulem, A. European options in a nonlinear incomplete market model with default. SIAM Journal On Financial Mathematics. 11, 849–880 (2020)
* [15]
  Grigorova, M., Quenez, M. & Sulem, A. American options in a non-linear incomplete market model with default. Stochastic Processes And Their Applications. 142, 479–512 (2021)
* [16]
  Jeanblanc, M., Yor, M. & Chesney, M. Mathematical methods for financial markets. (Springer Science & Business Media, 2009)
* [17]
  Jacod, J. & Shiryaev, A. Limit theorems for stochastic processes. (Springer Science & Business Media, 2013)
* [18]
  Papapantoleon, A., Possamaï, D. & Saplaouras, A. Existence and uniqueness results for BSDEs with jumps: the whole nine yards. Electronic Journal of Probability 23, 121, 1–68 (2018)
* [19]
  Pardoux, E. & Peng, S. Adapted solution of a backward stochastic differential equation. Systems & Control Letters. 14, 55-61 (1990)
* [20]

  Quenez, M.-C. & Sulem, A.
  BSDEs with jumps, optimization and applications to dynamic risk measures.
  Stochastic Processes and their Applications
  123, 8, 3328-3357 (2013)
* [21]

  Royer, M.
  Backward stochastic differential equations with jumps and related non-linear expectations.
  Stochastic Processes and their Applications
  116, 10, 1358–1376 (2006).
* [22]
  Zhang, J. Backward Stochastic Differential Equations. Probability Theory And Stochastic Modelling. (2017)