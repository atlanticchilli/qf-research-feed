---
authors:
- Alexis Anagnostakis
- David Criens
- Mikhail Urusov
doc_id: arxiv:2512.07555v1
family_id: arxiv:2512.07555
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: On the structure of increasing profits in a 1D general diffusion market with
  interest rates
url_abs: http://arxiv.org/abs/2512.07555v1
url_html: https://arxiv.org/html/2512.07555v1
venue: arXiv q-fin
version: 1
year: 2025
---


Alexis Anagnostakis

A. Anagnostakis – Université de Lorraine, CNRS, IECL
F-57000, Metz, France.
[[alexis.anagnostakis@univ-grenoble-alpes.fr](mailto:alexis.anagnostakis@univ-grenoble-alpes.fr)](mailto:)
, 
David Criens
D. Criens – University of Freiburg, Ernst-Zermelo-Str. 1, 79104 Freiburg, Germany.
[[david.criens@stochastik.uni-freiburg.de](mailto:david.criens@stochastik.uni-freiburg.de)](mailto:)
 and 
Mikhail Urusov
M. Urusov – University of Duisburg-Essen, Thea-Leymann-Str. 9, 45127 Essen, Germany.
[[mikhail.urusov@uni-due.de](mailto:mikhail.urusov@uni-due.de)](mailto:)

(Date: December 8, 2025)

###### Abstract.

In this paper, we investigate a financial market model consisting of a risky asset, modeled as a general diffusion parameterized by a scale function and a speed measure, and a bank account process with a constant interest rate. This flexible class of financial market models allows for features such as reflecting boundaries, skewness effects, sticky points, and slowdowns on fractal sets. For this market model, we study the structure of a strong form of arbitrage opportunity called increasing profits. Our main contributions are threefold. First, we characterize the existence of increasing profits in terms of an auxiliary deterministic signed measure ν\nu and a canonical trading strategy θ\theta, both of which depend only on the deterministic parametric characteristics of our model, namely the scale function, the speed measure, and the interest rate. More precisely, we show that an increasing profit exists if and only if ν\nu is nontrivial, and that this is equivalent to θ\theta itself generating an increasing profit. Second, we provide a precise characterization of the entire set of increasing profits in terms of ν\nu and θ\theta, and moreover characterize the value processes associated with increasing profits. Finally, we establish novel connections between no-arbitrage theory and the general theory of stochastic processes. Specifically, we relate the failure of the representation property for general diffusions to the existence of certain types of increasing profits whose value processes are dominated by the quadratic variation measure of a space-transformed version of the asset price process.

###### Key words and phrases:

Increasing profit; value process; general diffusion; scale function; speed measure; interest rate

###### 2020 Mathematics Subject Classification:

60J60; 91B70; 91G15; 91G30.

## 1. Introduction

Diffusion models with non-standard path properties, such as reflection, stickiness or skewness, have proven to be valuable tools for modeling a wide range of economic and financial scenarios. Prominent examples for applications of models with reflecting boundaries include portfolio protection mechanisms, where capital is added once the portfolio value reaches a prescribed threshold ([[15](https://arxiv.org/html/2512.07555v1#bib.bib15)]); withdrawal strategies designed to secure a minimal level of income prior to retirement ([[22](https://arxiv.org/html/2512.07555v1#bib.bib22)]); or situations in which central bank interventions aim to maintain exchange rates above a lower bound ([[24](https://arxiv.org/html/2512.07555v1#bib.bib24)]). Furthermore, diffusions with sticky points are able to capture possible takeover offers ([[7](https://arxiv.org/html/2512.07555v1#bib.bib7)]) and models with skewness naturally arise in the context of local volatility models and have been linked to the so-called “steep short end of the smile” phenomenon ([[14](https://arxiv.org/html/2512.07555v1#bib.bib14), [25](https://arxiv.org/html/2512.07555v1#bib.bib25)]).

The recent paper [[5](https://arxiv.org/html/2512.07555v1#bib.bib5)] has drawn attention to the fact that such models may admit particularly strong forms of arbitrage, so-called increasing profits, characterized by an increasing value process whose terminal value is positive with positive probability. In our previous article [[1](https://arxiv.org/html/2512.07555v1#bib.bib1)], we provided a comprehensive analysis of the existence and absence of increasing profits for general one-dimensional diffusion models with a single risky asset, modeled as a general diffusion in the sense of Itô and McKean [[16](https://arxiv.org/html/2512.07555v1#bib.bib16)], and a bank account with constant interest rate. Our results provide a characterization of the *no increasing profit (NIP)* condition in terms of the deterministic characteristics of the underlying general diffusion, the scale function and the speed measure.

In the present paper, we go a step further and study the structural foundations of increasing profits within such a general diffusion framework. Our goal is a precise description of the set of increasing profits and their corresponding value processes. In this regard, our results are particularly relevant in models where the no-arbitrage condition NIP fails, such as the diffusion models studied in [[14](https://arxiv.org/html/2512.07555v1#bib.bib14), [15](https://arxiv.org/html/2512.07555v1#bib.bib15), [22](https://arxiv.org/html/2512.07555v1#bib.bib22), [24](https://arxiv.org/html/2512.07555v1#bib.bib24), [25](https://arxiv.org/html/2512.07555v1#bib.bib25)], where increasing profits naturally occur.
Our analysis also provides an alternative approach to our previous deterministic characterization of NIP from [[1](https://arxiv.org/html/2512.07555v1#bib.bib1)] whose proofs relied on the fundamental weak structure conditions ([[12](https://arxiv.org/html/2512.07555v1#bib.bib12)]), which are not used in the present paper.

Let us explain the results from this paper in a more precise manner.
Our contributions are threefold. The main mathematical objects of interest are an auxiliary signed measure ν\nu and a related trading strategy θ\theta, both depending only on the interest rate, the scale function and speed measure of the risky asset.

Our first main result reveals their canonical importance showing that an increasing profit exists if and only if θ\theta itself constitutes an increasing profit. We further show that this is equivalent to the fact that ν\nu is a nontrivial signed measure.
The second part of this result recovers our characterization for NIP that we established in [[1](https://arxiv.org/html/2512.07555v1#bib.bib1)].
By means of several examples, including Black–Scholes and Bachelier models featuring absorbing or reflecting boundaries, sticky points and skewness effects, we relate each component of ν\nu to specific path properties of the underlying diffusion, thereby clarifying exactly which path properties lead to increasing profits and how they can be exploited. In this context, we make the interesting observation that although value processes of increasing profits cannot be dominated by the quadratic variation measure of the asset price process (as otherwise they would be zero identically; see Lemma [2.6](https://arxiv.org/html/2512.07555v1#S2.Thmtheorem6 "Lemma 2.6. ‣ 2.2. Increasing Profits ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") below), it is possible that such value processes are dominated by the quadratic variation measure of a space transformation of the asset process, a diffusion on natural scale. We call such strategies quadratic variation increasing profits. This appears to be a curiosity of our general diffusion framework, as this feature cannot be observed in classical SDE models, even under the very weak Engelbert–Schmidt conditions.

As a second main contribution, we characterize the entire class of increasing profits in relation to the canonical strategy θ\theta and the signed measure ν\nu. In particular, we show that increasing profits can only be generated during times when θ\theta does not vanish, which underlines its structural importance.
Moreover, we obtain an explicit representation for the value processes of any increasing profit, linking them to ν\nu and to the local time process of the underlying diffusion.

Lastly, we reveal an intrinsic relation between the failure of the representation property (RP)
for the risky asset and the existence of quadratic variation increasing profits.
The RP is known to be of fundamental importance in the context of market completeness and also from the viewpoint of the general theory of stochastic processes.
More specifically, we identify a broad framework in which the existence of quadratic variation increasing profits is equivalent to the failure of the RP. In general, however, the NIP condition and the RP are in a general position, meaning that neither of them implies the other.

*Outline.* The paper is structured as follows. In Section [2](https://arxiv.org/html/2512.07555v1#S2 "2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") we introduce our financial market model and recall the notion of increasing profits.
Our main results are presented in Section [3](https://arxiv.org/html/2512.07555v1#S3 "3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), the proofs are deferred to Section [4](https://arxiv.org/html/2512.07555v1#S4 "4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), and the examples are discussed in Section [5](https://arxiv.org/html/2512.07555v1#S5 "5. Examples ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates").
In the concluding Section [6](https://arxiv.org/html/2512.07555v1#S6 "6. On the Relation of Increasing Profits and the Representation Property ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") we discuss the relation between the existence of quadratic variation increasing profits and the failure of the representation property.

## 2. The Financial Market and the Concept of Increasing Profits

### 2.1. The Financial Market

In this paper, we consider a financial market driven by a regular
continuous strong Markov process, which is alternatively called a
*general diffusion*.
A quite complete overview on the theory of general diffusions can be found in the seminal monograph [[16](https://arxiv.org/html/2512.07555v1#bib.bib16)] by Itô and McKean.
Shorter textbook introductions are given in [[13](https://arxiv.org/html/2512.07555v1#bib.bib13), [19](https://arxiv.org/html/2512.07555v1#bib.bib19), [26](https://arxiv.org/html/2512.07555v1#bib.bib26), [27](https://arxiv.org/html/2512.07555v1#bib.bib27)].

As the concepts of scale and speed are crucial for our results, we recall some facts about them without going too much into detail.
We take a state space J⊂ℝJ\subset\mathbb{R} that is supposed to be a bounded or unbounded, closed, open or half-open interval. A scale function is a strictly increasing continuous function 𝔰:J→ℝ\mathfrak{s}\colon J\to\mathbb{R}
and a speed measure is a measure 𝔪\mathfrak{m} on (J,ℬ​(J))(J,\mathcal{B}(J)) that satisfies
𝔪​([a,b])∈(0,∞)\mathfrak{m}([a,b])\in(0,\infty) for all a<ba<b in J∘J^{\circ}, where J∘J^{\circ} denotes the interior of JJ. We define

|  |  |  |
| --- | --- | --- |
|  | α≜infJ∈[−∞,∞)andβ≜supJ∈(−∞,∞].\alpha\triangleq\inf J\in[-\infty,\infty)\quad\text{and}\quad\beta\triangleq\sup J\in(-\infty,\infty]. |  |

The values 𝔰​(α)\mathfrak{s}(\alpha) and 𝔰​(β)\mathfrak{s}(\beta) are defined by continuity (in particular, they can be infinite).
We also remark that the speed measure can be infinite near α\alpha and β\beta, and that the values 𝔪​({α})\mathfrak{m}(\{\alpha\}) and 𝔪​({β})\mathfrak{m}(\{\beta\}) can be anything in [0,∞][0,\infty] provided α∈J\alpha\in J and β∈J\beta\in J, respectively.

Before we proceed, let us mention that speed measures and semimartingale local times are not scaled consistently in the literature.
For the speed measure, we use the scaling from the books of Kallenberg [[19](https://arxiv.org/html/2512.07555v1#bib.bib19)] and Rogers and Williams [[27](https://arxiv.org/html/2512.07555v1#bib.bib27)], which is half the speed measure from the monographs of
Freedman [[13](https://arxiv.org/html/2512.07555v1#bib.bib13)],
Itô and McKean [[16](https://arxiv.org/html/2512.07555v1#bib.bib16)]
and Revuz and Yor [[26](https://arxiv.org/html/2512.07555v1#bib.bib26)]. To give an example, our speed measure of Brownian motion (on natural scale) is simply the Lebesgue measure, while it is twice the Lebesgue measure in [[13](https://arxiv.org/html/2512.07555v1#bib.bib13), [16](https://arxiv.org/html/2512.07555v1#bib.bib16), [26](https://arxiv.org/html/2512.07555v1#bib.bib26)]. Similarly, we use the semimartingale local time scaling of Freedman [[13](https://arxiv.org/html/2512.07555v1#bib.bib13)], Kallenberg [[19](https://arxiv.org/html/2512.07555v1#bib.bib19)], Revuz and Yor [[26](https://arxiv.org/html/2512.07555v1#bib.bib26)] and Rogers and Williams [[27](https://arxiv.org/html/2512.07555v1#bib.bib27)], which is twice the local time of Itô and McKean [[16](https://arxiv.org/html/2512.07555v1#bib.bib16)] and Karatzas and Shreve [[21](https://arxiv.org/html/2512.07555v1#bib.bib21)].
Furthermore, we emphasize that we always use the right-continuous version of the semimartingale local time
(in the space variable).

We are in a position to explain our financial framework.
Throughout this paper, we consider a finite time horizon T∈(0,∞)T\in(0,\infty).
Let 𝔹=(Ω,ℱ,𝐅=(ℱt)t∈[0,T],ℙ)\mathbb{B}=(\Omega,\mathcal{F},\mathbf{F}=(\mathcal{F}\_{t})\_{t\in[0,T]},\mathbb{P}) be a filtered probability space with a right-continuous filtration that supports a regular continuous strong Markov process (in the sense of [[27](https://arxiv.org/html/2512.07555v1#bib.bib27), Section V.45] except that the underlying setting needs not to be the canonical one) Y=(Yt)t∈[0,T]Y=(Y\_{t})\_{t\in[0,T]} with state space JJ, scale function 𝔰\mathfrak{s}, speed measure 𝔪\mathfrak{m} and deterministic starting value
x0x\_{0}. As for the starting value, we always assume that

|  |  |  |
| --- | --- | --- |
|  | either ​x0∈J∘​ or ​x0∈J∖J∘​ is a reflecting boundary for ​Y.\text{either }x\_{0}\in J^{\circ}\text{ or }x\_{0}\in J\setminus J^{\circ}\text{ is a reflecting boundary for }Y. |  |

We exclude the case of an absorbing starting value x0∈J∖J∘x\_{0}\in J\setminus J^{\circ}, since then the process YY is simply constant.
In the above context, the strong Markov property refers to the filtration 𝐅\mathbf{F}.

###### Standing Assumption 2.1.

YY is a semimartingale on the stochastic basis 𝔹\mathbb{B}.

The Standing Assumption [2.1](https://arxiv.org/html/2512.07555v1#S2.Thmtheorem1 "Standing Assumption 2.1. ‣ 2.1. The Financial Market ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") is not automatically true in our general diffusion setting. For example, if BB is a Brownian motion starting in zero, then |B|\sqrt{|B|} is a general diffusion but *not* a semimartingale ([[26](https://arxiv.org/html/2512.07555v1#bib.bib26), Exercise VI.1.14]).
The semimartingale property of YY is solely a property of the scale function 𝔰\mathfrak{s}, more precisely, but equivalently, its inverse.
The following lemma collects some properties that are proved in [[6](https://arxiv.org/html/2512.07555v1#bib.bib6), Section 5].

Recall that for an open interval I⊂ℝI\subset\mathbb{R} and a real-valued function 𝔣:I→ℝ\mathfrak{f}\colon I\to\mathbb{R} that is the difference of two convex functions on II, one can define the second derivative measure 𝔣′′​(d​x)\mathfrak{f}^{\prime\prime}(\mathrm{d}x) by

|  |  |  |
| --- | --- | --- |
|  | 𝔣′′​((x,y])≜𝔣+′​(y)−𝔣+′​(x),x<y​ in ​I,\mathfrak{f}^{\prime\prime}((x,y])\triangleq\mathfrak{f}^{\prime}\_{+}(y)-\mathfrak{f}^{\prime}\_{+}(x),\quad x<y\text{ in }I, |  |

where 𝔣+′\mathfrak{f}^{\prime}\_{+} denotes the right derivative of 𝔣\mathfrak{f}.

###### Lemma 2.2.

Assume that YY is a semimartingale. Then, the inverse scale function 𝔮≜𝔰−1\mathfrak{q}\triangleq\mathfrak{s}^{-1} is the difference of two convex functions on the interior 𝔰​(J∘)\mathfrak{s}(J^{\circ}). Furthermore, in case J=[α,∞)J=[\alpha,\infty) and α\alpha is absorbing for YY, it holds that

|  |  |  |
| --- | --- | --- |
|  | ∫𝔰​(α)+(x−𝔰​(α))​|𝔮′′|​(d​x)<∞.\int\_{\mathfrak{s}(\alpha)+}(x-\mathfrak{s}(\alpha))\,|\mathfrak{q}^{\prime\prime}|(\mathrm{d}x)<\infty. |  |

In case J=[α,∞)J=[\alpha,\infty) and α\alpha is reflecting for YY, the second derivative measure 𝔮′′​(d​x)\mathfrak{q}^{\prime\prime}(\mathrm{d}x) can be identified with a finite signed measure on every interval [𝔰​(α),𝔰​(z)][\mathfrak{s}(\alpha),\mathfrak{s}(z)] with z∈(α,∞)z\in(\alpha,\infty).

###### Proof.

These statements follow directly from the discussion in [[6](https://arxiv.org/html/2512.07555v1#bib.bib6), Section 5].
∎

Of course, suitable adjustments of the last two statements from Lemma [2.2](https://arxiv.org/html/2512.07555v1#S2.Thmtheorem2 "Lemma 2.2. ‣ 2.1. The Financial Market ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") hold also for more general state spaces JJ.

In the following, our financial market is supposed to contain one risky asset that is given by the general diffusion semimartingale YY.
Furthermore, we fix a deterministic interest rate r∈ℝr\in\mathbb{R}. The discounting will be done by the usual bank account process er​te^{rt} for t∈[0,T]t\in[0,T], leading to the discounted price process S=(St)t∈[0,T]S=(S\_{t})\_{t\in[0,T]} given by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | St≜e−r​t​Yt,t∈[0,T].\displaystyle S\_{t}\triangleq e^{-rt}\,Y\_{t},\quad t\in[0,T]. |  |

We now recall the concept of increasing profits, which is the central arbitrage concept studied in this paper.

### 2.2. Increasing Profits

Let us now recall the “no increasing profit” NIP condition, which is similar to the “no unbounded increasing profit” first introduced by Karatzas and Kardaras in [[20](https://arxiv.org/html/2512.07555v1#bib.bib20)].
Our presentation follows Fontana [[12](https://arxiv.org/html/2512.07555v1#bib.bib12)].
In the sequel we use the notation L​(S)L(S) for the set of all predictable processes that are integrable w.r.t. the continuous semimartingale SS.
The elements H∈L​(S)H\in L(S) are alternatively called *strategies*. The integral process

|  |  |  |
| --- | --- | --- |
|  | VtH≜∫0tHs​dSs,t∈[0,T],V^{H}\_{t}\triangleq\int\_{0}^{t}H\_{s}\,\mathrm{d}S\_{s},\quad t\in[0,T], |  |

is called the value process associated to the strategy H∈L​(S)H\in L(S).

###### Definition 2.3.

A strategy H∈L​(S)H\in L(S) is called an increasing profit if

|  |  |  |  |
| --- | --- | --- | --- |
| (2.2) |  | ℙ​-a.s.,[0,T]∋t↦VtH​ is increasing, and ​ℙ​(VTH>0)>0.\displaystyle\mathbb{P}\text{-a.s.},\;[0,T]\ni t\mapsto V^{H}\_{t}\text{ is increasing, and }\mathbb{P}\big(V^{H}\_{T}>0\big)>0. |  |

We denote the set of all such strategies by 𝖨𝖯\mathsf{IP}:

|  |  |  |
| --- | --- | --- |
|  | 𝖨𝖯≜{H∈L​(S):H​ is an increasing profit}.\mathsf{IP}\triangleq\big\{H\in L(S)\colon H\text{ is an increasing profit}\big\}. |  |

If 𝖨𝖯=∅\mathsf{IP}=\emptyset, we say that the *NIP* condition holds.

###### Remark 2.4.

If 𝖨𝖯≠∅\mathsf{IP}\neq\emptyset, the set {VTH:H∈𝖨𝖯}\{V^{H}\_{T}\colon H\in\mathsf{IP}\} is unbounded with positive probability, i.e.,

|  |  |  |
| --- | --- | --- |
|  | ℙ​(supH∈𝖨𝖯VTH=∞)>0.\mathbb{P}\Big(\sup\_{H\,\in\,\mathsf{IP}}V^{H}\_{T}=\infty\Big)>0. |  |

This follows directly from the fact that 𝖨𝖯\mathsf{IP} is a cone.

###### Remark 2.5.

While increasing profits have an obvious financial interpretation,
from the viewpoint of the general theory of stochastic processes
the following question seems to be more natural:
*When does a strategy H∈L​(S)H\in L(S) exist such that VHV^{H} is a non-constant finite variation process?*

We recall the answer to this question in the more general setting where the discounted price is a continuous semimartingale
(notice that, from the next section on, we again consider the discounted general diffusion setting ([2.1](https://arxiv.org/html/2512.07555v1#S2.E1 "In 2.1. The Financial Market ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) only):

Let S′=(St′)t∈[0,T]S^{\prime}=(S^{\prime}\_{t})\_{t\in[0,T]} be a continuous semimartingale.
Then there exists an increasing profit H∈L​(S′)H\in L(S^{\prime})
if and only if
there exists a trading strategy K∈L​(S′)K\in L(S^{\prime})
whose value process ∫0⋅Ks​dSs′\int\_{0}^{\cdot}K\_{s}\,\mathrm{d}S^{\prime}\_{s}
is of finite variation and non-constant with positive probability.
This is seen by inspecting the proof of [[12](https://arxiv.org/html/2512.07555v1#bib.bib12), Theorem 3.1]
(cf. [[12](https://arxiv.org/html/2512.07555v1#bib.bib12), Remark 3.1]).

It is worth noting that this equivalence is no longer true if the asset price process is allowed to have jumps.
Indeed, let N=(Nt)t∈[0,T]N=(N\_{t})\_{t\in[0,T]} be a Poisson process with intensity 11.
Consider the compensated Poisson process model

|  |  |  |  |
| --- | --- | --- | --- |
| (2.3) |  | St′=Nt−t,t∈[0,T].S^{\prime}\_{t}=N\_{t}-t,\quad t\in[0,T]. |  |

As S′S^{\prime} is a martingale, NIP holds, that is, increasing profits do not exist in this model.
On the other hand, the strategy H≡1H\equiv 1 produces a non-constant value process of finite variation: VH=S′V^{H}=S^{\prime}.111We also observe that this strategy is *admissible* in the sense that its value process is bounded from below by a deterministic constant (TT).
In other words, we cannot save that equivalence for càdlàg semimartingales by considering only admissibile strategies.

In the realm of the previous remark, the following lemma reveals some intrinsic structure underlying value processes of increasing or finite variation profits.

###### Lemma 2.6.

Let S′=(St′)t∈[0,T]S^{\prime}=(S^{\prime}\_{t})\_{t\in[0,T]} be a continuous semimartingale and take H∈L​(S′)H\in L(S^{\prime}) such that a.s. ∫0⋅Hs​dSs′\int\_{0}^{\cdot}H\_{s}\,\mathrm{d}S^{\prime}\_{s} is of finite variation and dominated by the quadratic variation measure d​⟨S′⟩\mathrm{d}\langle S^{\prime}\rangle. Then, a.s. ∫0⋅Hs​dSs′=0\int\_{0}^{\cdot}H\_{s}\,\mathrm{d}S^{\prime}\_{s}=0.

###### Proof.

As ∫0⋅Hs​dSs′\int\_{0}^{\cdot}H\_{s}\,\mathrm{d}S^{\prime}\_{s} is of finite variation, we get that a.s.

|  |  |  |
| --- | --- | --- |
|  | 0=⟨∫0⋅𝟙{Hs≠0}Hs​d​(∫0sHr​dSr′)⟩=∫0⋅𝟙{Hs≠0}​d​⟨S′⟩s.0=\Big\langle\int\_{0}^{\cdot}\frac{\mathbbm{1}\_{\{H\_{s}\neq 0\}}}{H\_{s}}\,\mathrm{d}\Big(\int\_{0}^{s}H\_{r}\,\mathrm{d}S^{\prime}\_{r}\Big)\Big\rangle=\int\_{0}^{\cdot}\mathbbm{1}\_{\{H\_{s}\neq 0\}}\,\mathrm{d}\langle S^{\prime}\rangle\_{s}. |  |

Hence, by the domination assumption, a.s.

|  |  |  |
| --- | --- | --- |
|  | 0=∫0⋅𝟙{Hs≠0}​d​(∫0sHr​dSr′)=∫0⋅Hs​dSs′,0=\int\_{0}^{\cdot}\mathbbm{1}\_{\{H\_{s}\neq 0\}}\,\mathrm{d}\Big(\int\_{0}^{s}H\_{r}\,\mathrm{d}S^{\prime}\_{r}\Big)=\int\_{0}^{\cdot}H\_{s}\,\mathrm{d}S^{\prime}\_{s}, |  |

which completes the proof.
∎

This lemma explains that value processes of increasing (or finite variation) profits are not dominated by the quadratic variation measure of the discounted asset price process. As we encounter below, however, it is possible that such value processes are dominated by the quadratic variation measure d​⟨U⟩\mathrm{d}\langle U\rangle of the space-transformed natural scale diffusion U=𝔰​(Y)U=\mathfrak{s}(Y).
This appears to be an interesting feature of our general diffusion setting,
and the existence of such increasing profits is related to failure of the representation property of SS (see Section [6](https://arxiv.org/html/2512.07555v1#S6 "6. On the Relation of Increasing Profits and the Representation Property ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")).

## 3. The Structure of Increasing Profits

In our previous paper [[1](https://arxiv.org/html/2512.07555v1#bib.bib1)] we established a deterministic characterization of NIP in terms of the scale function and the speed measure.
The proofs in [[1](https://arxiv.org/html/2512.07555v1#bib.bib1)] relied on the fundamental theorem of asset pricing for NIP, which states that NIP is equivalent to a weak structure condition; cf. [[12](https://arxiv.org/html/2512.07555v1#bib.bib12)].
In this paper we investigate the NIP condition from a quite different point of view. Namely, instead of studying the NIP condition directly, we focus on the structure of increasing profits. This path provides new economic insights and it also leads to a new proof for results from [[1](https://arxiv.org/html/2512.07555v1#bib.bib1)].

By Standing Assumption [2.1](https://arxiv.org/html/2512.07555v1#S2.Thmtheorem1 "Standing Assumption 2.1. ‣ 2.1. The Financial Market ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") and Lemma [2.2](https://arxiv.org/html/2512.07555v1#S2.Thmtheorem2 "Lemma 2.2. ‣ 2.1. The Financial Market ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), restricted to the open set 𝔰​(J∘)\mathfrak{s}(J^{\circ}), the inverse scale function 𝔮=𝔰−1\mathfrak{q}=\mathfrak{s}^{-1} is the difference of two convex functions. Consequently, the second derivative measure 𝔮′′​(d​x)\mathfrak{q}^{\prime\prime}(\mathrm{d}x) is well-defined on 𝔰​(J∘)\mathfrak{s}(J^{\circ}).
By Lebesgue’s decomposition and the Radon–Nikodym theorem ([[2](https://arxiv.org/html/2512.07555v1#bib.bib2), Theorems 5.2.6, 5.3.5]), there exists a unique decomposition

|  |  |  |
| --- | --- | --- |
|  | 𝔮′′​(d​x)=𝔮ac′′​(x)​d​x+𝔮si′′​(d​x)on ​ℬ​(𝔰​(J∘)),\mathfrak{q}^{\prime\prime}(\mathrm{d}x)=\mathfrak{q}^{\prime\prime}\_{\operatorname{ac}}(x)\,\mathrm{d}x+\mathfrak{q}^{\prime\prime}\_{\operatorname{si}}(\mathrm{d}x)\quad\text{on }\mathcal{B}(\mathfrak{s}(J^{\circ})), |  |

where 𝔮si′′\mathfrak{q}^{\prime\prime}\_{\operatorname{si}} is a signed measure that is singular w.r.t. the Lebesgue measure λ\{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}. For λ\{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}-a.a. x∈𝔰​(J∘)x\in\mathfrak{s}(J^{\circ}),
the second derivative 𝔮′′​(x)\mathfrak{q}^{\prime\prime}(x) of 𝔮\mathfrak{q} at the point xx exists in the usual sense,
is finite, and 𝔮′′​(x)=𝔮ac′′​(x)\mathfrak{q}^{\prime\prime}(x)=\mathfrak{q}^{\prime\prime}\_{\operatorname{ac}}(x).
Therefore, in what follows, we prefer to write 𝔮′′​(x)\mathfrak{q}^{\prime\prime}(x) instead of 𝔮ac′′​(x)\mathfrak{q}^{\prime\prime}\_{\operatorname{ac}}(x).

###### Remark 3.1.

As 𝔮\mathfrak{q} is a difference of two convex functions on 𝔰​(J∘)\mathfrak{s}(J^{\circ}),
its right and left derivatives 𝔮+′\mathfrak{q}^{\prime}\_{+} and 𝔮−′\mathfrak{q}^{\prime}\_{-} exist, are finite everywhere on 𝔰​(J∘)\mathfrak{s}(J^{\circ}) and can differ only on an at most countable set.
In what follows, we use the notation {𝔮+′=0}\{\mathfrak{q}^{\prime}\_{+}=0\}
as a shorthand for {x∈𝔰​(J∘):𝔮+′​(x)=0}\{x\in\mathfrak{s}(J^{\circ}):\mathfrak{q}^{\prime}\_{+}(x)=0\}.
Furthermore,
we write {𝔮′=0}\{\mathfrak{q}^{\prime}=0\} for an arbitrary Borel subset of 𝔰​(J∘)\mathfrak{s}(J^{\circ})
that differs from the set {𝔮+′=0}\{\mathfrak{q}^{\prime}\_{+}=0\} on a Lebesgue-null set
(i.e., λ\({𝔮′=0}​△​{𝔮+′=0})=0{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}(\{\mathfrak{q}^{\prime}=0\}\,\triangle\,\{\mathfrak{q}^{\prime}\_{+}=0\})=0).

Recalling [[26](https://arxiv.org/html/2512.07555v1#bib.bib26), Exercise VII.3.18], the process U≜𝔰​(Y)U\triangleq\mathfrak{s}(Y) is a general diffusion on natural scale (i.e., up to increasing affine transformations, the scale function is the identity) with speed measure 𝔪U≜𝔪∘𝔰−1\mathfrak{m}^{U}\triangleq\mathfrak{m}\circ\mathfrak{s}^{-1}.
We denote the Lebesgue decomposition (w.r.t. the Lebesgue measure) of the
restriction 𝔪U|𝔰​(J∘)\mathfrak{m}^{U}|\_{\mathfrak{s}(J^{\circ})} to (𝔰​(J∘),ℬ​(𝔰​(J∘)))(\mathfrak{s}(J^{\circ}),\mathcal{B}(\mathfrak{s}(J^{\circ}))) of the speed measure 𝔪U\mathfrak{m}^{U}
by

|  |  |  |
| --- | --- | --- |
|  | 𝔪U|𝔰​(J∘)​(d​x)=𝔪acU​(x)​d​x+𝔪siU​(d​x)on ​ℬ​(𝔰​(J∘)).\mathfrak{m}^{U}|\_{\mathfrak{s}(J^{\circ})}(\mathrm{d}x)=\mathfrak{m}^{U}\_{\operatorname{ac}}(x)\,\mathrm{d}x+\mathfrak{m}^{U}\_{\operatorname{si}}(\mathrm{d}x)\quad\text{on }\mathcal{B}(\mathfrak{s}(J^{\circ})). |  |

Furthermore, we introduce the auxiliary
signed measure ν\nu on (𝔰​(J),ℬ​(𝔰​(J)))(\mathfrak{s}(J),\mathcal{B}(\mathfrak{s}(J))) by the formula

|  |  |  |  |
| --- | --- | --- | --- |
| (3.1) |  | ν​(d​x)≜− 1{𝔮′=0}∩𝔰​(J∘)​(x)​r​𝔮​(x)​𝔪acU​(x)​d​x+𝟙𝔰​(J∘)​(x)​[12​𝔮si′′​(d​x)−r​𝔮​(x)​𝔪siU​(d​x)]−𝟙{α∈𝒜}​r​α​δ𝔰​(α)​(d​x)−𝟙{β∈𝒜}​r​β​δ𝔰​(β)​(d​x)+𝟙{α∈ℛ}​(12​𝔮+′​(𝔰​(α))−r​α​𝔪U​({𝔰​(α)}))​δ𝔰​(α)​(d​x)+𝟙{β∈ℛ}​(−12​𝔮−′​(𝔰​(β))−r​β​𝔪U​({𝔰​(β)}))​δ𝔰​(β)​(d​x),\begin{split}\nu(\mathrm{d}x)\triangleq-&\,\mathbbm{1}\_{\{\mathfrak{q}^{\prime}=0\}\,\cap\,\mathfrak{s}(J^{\circ})}(x)r\mathfrak{q}(x)\mathfrak{m}^{U}\_{\operatorname{ac}}(x)\,\mathrm{d}x\\ &+\mathbbm{1}\_{\mathfrak{s}(J^{\circ})}(x)\big[\tfrac{1}{2}\mathfrak{q}^{\prime\prime}\_{\operatorname{si}}(\mathrm{d}x)-r\mathfrak{q}(x)\mathfrak{m}^{U}\_{{\operatorname{si}}}(\mathrm{d}x)\big]\\ &-\mathbbm{1}\_{\{\alpha\,\in\,\mathcal{A}\}}r\alpha\,\delta\_{\mathfrak{s}(\alpha)}(\mathrm{d}x)-\mathbbm{1}\_{\{\beta\,\in\,\mathcal{A}\}}r\beta\,\delta\_{\mathfrak{s}(\beta)}(\mathrm{d}x)\\ &+\mathbbm{1}\_{\{\alpha\,\in\,\mathcal{R}\}}(\tfrac{1}{2}\mathfrak{q}^{\prime}\_{+}(\mathfrak{s}(\alpha))-r\alpha\mathfrak{m}^{U}(\{\mathfrak{s}(\alpha)\}))\,\delta\_{\mathfrak{s}(\alpha)}(\mathrm{d}x)\\ &+\mathbbm{1}\_{\{\beta\,\in\,\mathcal{R}\}}(-\tfrac{1}{2}\mathfrak{q}^{\prime}\_{-}(\mathfrak{s}(\beta))-r\beta\mathfrak{m}^{U}(\{\mathfrak{s}(\beta)\}))\,\delta\_{\mathfrak{s}(\beta)}(\mathrm{d}x),\end{split} |  |

where 𝒜\mathcal{A} (resp., ℛ\mathcal{R}) denotes the set of absorbing (resp., reflecting) boundaries for the diffusion YY. Notice that ν\nu is locally finite on (𝔰​(J∘),ℬ​(𝔰​(J∘)))(\mathfrak{s}(J^{\circ}),\mathcal{B}(\mathfrak{s}(J^{\circ}))).
Every term of ν\nu captures a specific effect which results in an increasing profit.
More specifically, we will prove that NIP holds if and only if the measure ν\nu vanishes (ν≡0)(\nu\equiv 0). In Section [5](https://arxiv.org/html/2512.07555v1#S5 "5. Examples ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") below, we will link each component of ν\nu to path properties of YY, and use examples to demonstrate how these lead to increasing profits.

Our first result provides a description for the value process VHV^{H}
associated to an increasing profit H∈L​(S)H\in L(S).
More generally, the result only requires a value process of finite variation. In this context, we recall that increasing profits have a natural relation to trading strategies whose value processes are of finite variation, see Remark [2.5](https://arxiv.org/html/2512.07555v1#S2.Thmtheorem5 "Remark 2.5. ‣ 2.2. Increasing Profits ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates").
We also define the hitting times

|  |  |  |
| --- | --- | --- |
|  | Tx​(U)≜inf{t∈[0,T]:Ut=x}∧T,inf∅≜∞,T\_{x}(U)\triangleq\inf\{t\in[0,T]\colon U\_{t}=x\}\wedge T,\quad\inf\emptyset\triangleq\infty, |  |

for x∈𝔰​(J)x\in\mathfrak{s}(J).

Finally, for the general diffusion UU on natural scale,
we introduce the *diffusion local time* as the random field
(L^tx​(U):(t,x)∈[0,T]×𝔰​(J))(\widehat{L}\_{t}^{x}(U):(t,x)\in[0,T]\times\mathfrak{s}(J)), defined by the formula

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | L^tx​(U)={Ltx​(U)if ​(t,x)∈[0,T]×𝔰​(J∖β),Ltx−​(U)if ​(t,x)∈[0,T]×{𝔰​(β)}​ (in case ​β∈J​),\widehat{L}\_{t}^{x}(U)=\begin{cases}L\_{t}^{x}(U)&\text{if }(t,x)\in[0,T]\times\mathfrak{s}(J\setminus\beta),\\ L\_{t}^{x-}(U)&\text{if }(t,x)\in[0,T]\times\{\mathfrak{s}(\beta)\}\text{ (in case }\beta\in J\text{)},\end{cases} |  |

where β≜supJ\beta\triangleq\sup J and (Ltx​(U):(t,x)∈[0,T]×ℝ)(L\_{t}^{x}(U)\colon(t,x)\in[0,T]\times\operatorname{\mathbb{R}}) is the
semimartingale local time.
In other words, in the diffusion local time for a general diffusion on natural scale we correct the value of the semimartingale local time only at the upper boundary of the state space
(notice that we have L𝔰​(β)​(U)=0L^{\mathfrak{s}(\beta)}(U)=0,
once β∈J\beta\in J,
for the semimartingale local time, as the latter is right-continuous in the space variable).

###### Proposition 3.2.

If the strategy H∈L​(S)H\in L(S) is such that its value process VHV^{H} is of finite variation, then a.s.

|  |  |  |  |
| --- | --- | --- | --- |
| (3.3) |  | VH=∫0⋅Hs​e−r​s​∫(𝟙𝔰​(J∖𝒜)​(x)​d​L^sx​(U)+𝟙𝔰​(𝒜)​(x)​𝟙(Tx​(U),T]​(s)​d​s)​ν​(d​x).V^{H}=\int\_{0}^{\cdot}H\_{s}e^{-rs}\int\Big(\mathbbm{1}\_{\mathfrak{s}(J\,\setminus\,\mathcal{A})}(x)\,\mathrm{d}\widehat{L}^{x}\_{s}(U)+\mathbbm{1}\_{\mathfrak{s}(\mathcal{A})}(x)\mathbbm{1}\_{(T\_{x}(U),T]}(s)\,\mathrm{d}s\Big)\,\nu(\mathrm{d}x). |  |

Next, we ask about the precise structure of increasing profits and, as a byproduct, a characterization of the NIP condition. This question is answered in the following theorem, which we consider as our main result.
We need some additional notation for its formulation.
Let

|  |  |  |
| --- | --- | --- |
|  | ν=ν+−ν−\nu=\nu\_{+}-\nu\_{-} |  |

be the Jordan decomposition ([[2](https://arxiv.org/html/2512.07555v1#bib.bib2), Theorem 5.1.8]) of ν\nu on ℬ​(𝔰​(J))\mathcal{B}(\mathfrak{s}(J)) and, as always, we denote the total variation measure by |ν|≜ν++ν−|\nu|\triangleq\nu\_{+}+\nu\_{-}. Further, let 𝔰​(J)=N+⊔N−\mathfrak{s}(J)=N\_{+}\sqcup N\_{-} be a Hahn decomposition ([[2](https://arxiv.org/html/2512.07555v1#bib.bib2), Theorem 5.1.9]) for (𝔰​(J),ℬ​(𝔰​(J)),ν)(\mathfrak{s}(J),\mathcal{B}(\mathfrak{s}(J)),\nu), i.e., for all A∈ℬ​(𝔰​(J))A\in\mathcal{B}(\mathfrak{s}(J)),

|  |  |  |  |
| --- | --- | --- | --- |
| (3.4) |  | ν​(A∩N+)=ν+​(A),ν​(A∩N−)=−ν−​(A).\displaystyle\nu(A\cap N\_{+})=\nu\_{+}(A),\quad\nu(A\cap N\_{-})=-\nu\_{-}(A). |  |

Let ν|𝔰​(J∘)=νac+νsi\nu|\_{\mathfrak{s}(J^{\circ})}=\nu\_{\textup{ac}}+\nu\_{\textup{si}} be the Lebesgue decomposition ([[2](https://arxiv.org/html/2512.07555v1#bib.bib2), Theorem 5.2.6]) of the locally finite signed measure ν|𝔰​(J∘)\nu|\_{\mathfrak{s}(J^{\circ})} w.r.t. the Lebesgue measure on (𝔰​(J∘),ℬ​(𝔰​(J∘)))(\mathfrak{s}(J^{\circ}),\mathcal{B}(\mathfrak{s}(J^{\circ}))), and let Nsi∈ℬ​(𝔰​(J∘))N\_{\operatorname{si}}\in\mathcal{B}(\mathfrak{s}(J^{\circ})) be a Lebesgue-null set such that ν​(A∩Nsi)=νsi​(A)\nu(A\cap N\_{\operatorname{si}})=\nu\_{\textup{si}}(A) for all A∈ℬ​(𝔰​(J∘))A\in\mathcal{B}(\mathfrak{s}(J^{\circ})), which exists by the definition of the singular part ([[2](https://arxiv.org/html/2512.07555v1#bib.bib2), Definition 5.2.1]).
We set

|  |  |  |
| --- | --- | --- |
|  | N𝔮′=0≜𝔰​(J∖J∘)∪Nsi∪{𝔮+′=0}∈ℬ​(𝔰​(J)),N\_{\mathfrak{q}^{\prime}=0}\triangleq\mathfrak{s}(J\setminus J^{\circ})\cup N\_{\operatorname{si}}\cup\{\mathfrak{q}^{\prime}\_{+}=0\}\in\mathcal{B}(\mathfrak{s}(J)), |  |

and notice that ν\nu is concentrated on N𝔮′=0N\_{\mathfrak{q}^{\prime}=0}, i.e., ν​(A∩N𝔮′=0)=ν​(A)\nu(A\cap N\_{\mathfrak{q}^{\prime}=0})=\nu(A) for all A∈ℬ​(𝔰​(J))A\in\mathcal{B}(\mathfrak{s}(J)).
Next, we define the strategy

|  |  |  |  |
| --- | --- | --- | --- |
| (3.5) |  | θt≜𝟙N+∩N𝔮′=0​(Ut)−𝟙N−∩N𝔮′=0​(Ut),t∈[0,T],\displaystyle\theta\_{t}\triangleq\mathbbm{1}\_{N\_{+}\,\cap\,N\_{\mathfrak{q}^{\prime}=0}}(U\_{t})-\mathbbm{1}\_{N\_{-}\,\cap\,N\_{\mathfrak{q}^{\prime}=0}}(U\_{t}),\quad t\in[0,T], |  |

and the kernel

|  |  |  |
| --- | --- | --- |
|  | μ​(d​t,ω)≜∫𝔰​(J∖𝒜)dL^tx​(U)​(ω)​|ν|​(d​x)+∑x∈𝔰​(𝒜)|ν​(x)|​𝟙(Tx​(U​(ω)),T]​(t)​d​t,\mu(\mathrm{d}t,\omega)\triangleq\int\_{\mathfrak{s}(J\,\setminus\,\mathcal{A})}\,\mathrm{d}\widehat{L}^{x}\_{t}(U)(\omega)\,|\nu|(\mathrm{d}x)+\sum\_{x\in\mathfrak{s}(\mathcal{A})}|\nu(x)|\mathbbm{1}\_{(T\_{x}(U(\omega)),T]}(t)\,\mathrm{d}t, |  |

where we again use the diffusion local time from ([3.2](https://arxiv.org/html/2512.07555v1#S3.E2 "In 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")).
We write μ⊗ℙ\mu\otimes\mathbb{P} for the measure μ​(d​t,ω)​ℙ​(d​ω)\mu(\mathrm{d}t,\omega)\,\mathbb{P}(\mathrm{d}\omega) and d​⟨U⟩⊗ℙ\mathrm{d}\langle U\rangle\otimes\mathbb{P} for the measure d​⟨U⟩t​(ω)​ℙ​(d​ω)\mathrm{d}\langle U\rangle\_{t}(\omega)\,\mathbb{P}(\mathrm{d}\omega), both defined on the measurable space ([0,T]×Ω,ℬ​([0,T])⊗ℱ)([0,T]\times\Omega,\mathcal{B}([0,T])\otimes\mathcal{F}).
Finally, write

|  |  |  |
| --- | --- | --- |
|  | T𝔰​(𝒜)​(U)≜inf{t∈[0,T]:Ut∈𝔰​(𝒜)}∧T,T\_{\mathfrak{s}(\mathcal{A})}(U)\triangleq\inf\{t\in[0,T]\colon U\_{t}\in\mathfrak{s}(\mathcal{A})\}\wedge T, |  |

for the first time UU hits an absorbing boundary point.

We now present the main results of this paper. The first theorem highlights the structural importance of the strategy θ\theta and the signed measure ν\nu, providing an equivalent characterization for the NIP condition.

###### Theorem 3.3.

The following are equivalent:

1. (i)

   There exists an increasing profit.
2. (ii)

   There exists a set G∈ℬ​(𝔰​(J))G\in\mathcal{B}(\mathfrak{s}(J)) such that |ν|​(G)>0|\nu|(G)>0.
3. (iii)

   The trading strategy θ\theta from ([3.5](https://arxiv.org/html/2512.07555v1#S3.E5 "In 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) is an increasing profit.

In particular, NIP is equivalent to |ν|≡0|\nu|\equiv 0.

It is worth noting that |ν|≡0|\nu|\equiv 0 is equivalent to ν≡0\nu\equiv 0.
Indeed, if |ν|=ν++ν−≡0|\nu|=\nu\_{+}+\nu\_{-}\equiv 0, then ν+≡0\nu\_{+}\equiv 0 and ν−≡0\nu\_{-}\equiv 0, hence ν=ν+−ν−≡0\nu=\nu\_{+}-\nu\_{-}\equiv 0.
Conversely, if ν≡0\nu\equiv 0, then, by ([3.4](https://arxiv.org/html/2512.07555v1#S3.E4 "In 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")), ν+=ν(⋅∩N+)≡0\nu\_{+}=\nu(\,\cdot\,\cap N\_{+})\equiv 0 and ν−=−ν(⋅∩N−)≡0\nu\_{-}=-\nu(\,\cdot\,\cap N\_{-})\equiv 0, hence |ν|=ν++ν−≡0|\nu|=\nu\_{+}+\nu\_{-}\equiv 0.

The next theorem provides a precise characterization for the set 𝖨𝖯\mathsf{IP} of increasing profits. At this point, we recall that the corresponding value processes are described in Proposition [3.2](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") above.

###### Theorem 3.4.

A strategy H∈L​(S)H\in L(S) is an increasing profit if and only if it satisfies the following three properties:

1. (i)

   d​⟨U⟩⊗ℙ\mathrm{d}\langle U\rangle\otimes\mathbb{P}-a.e. H​𝔮+′​(U)=0H\mathfrak{q}^{\prime}\_{+}(U)=0 on [0,T𝔰​(𝒜)​(U))[0,T\_{\mathfrak{s}(\mathcal{A})}(U)).
2. (ii)

   μ⊗ℙ\mu\otimes\mathbb{P}-a.e. θ​H≥0\theta H\geq 0.
3. (iii)

   ℙ​(μ​({t∈[0,T]:θt​Ht>0},⋅)>0)>0\mathbb{P}(\mu(\{t\in[0,T]\colon\theta\_{t}H\_{t}>0\},\cdot\,)>0)>0.

Providing some intuition, (i) deactivates the martingale part of the value process VHV^{H}, (ii) entails that it has increasing paths, and (ii) and (iii) together ensure that VHV^{H} has a positive terminal value with positive probability.
We remark that 𝔮+′\mathfrak{q}^{\prime}\_{+} can be replaced with 𝔮−′\mathfrak{q}^{\prime}\_{-} in (i). This follows from the semimartingale occupation times formula together with the fact that 𝔮+′\mathfrak{q}^{\prime}\_{+} and 𝔮−′\mathfrak{q}^{\prime}\_{-} differ on an at most Lebesgue-null set (in fact, even on an at most countable set).

In concrete model situations, (i) and (ii) from Theorem [3.4](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") are quite easy to understand, while
condition (iii) appears to require a case by case study.
Our final main result replaces this part with a pathwise condition, providing a sufficient condition for a strategy to be an increasing profit.

###### Proposition 3.5.

Let H∈L​(S)H\in L(S) satisfy the following:

1. (i)

   d​⟨U⟩⊗ℙ\mathrm{d}\langle U\rangle\otimes\mathbb{P}-a.e. H​𝔮+′​(U)=0H\mathfrak{q}^{\prime}\_{+}(U)=0 on [0,T𝔰​(𝒜)​(U))[0,T\_{\mathfrak{s}(\mathcal{A})}(U)).
2. (ii)

   μ⊗ℙ\mu\otimes\mathbb{P}-a.e. θ​H≥0\theta H\geq 0.
3. (iii)

   There exists a set G∈ℬ​(𝔰​(J))G\in\mathcal{B}(\mathfrak{s}(J)) such that |ν|​(G)>0|\nu|(G)>0 and a.s. it holds:
   for all t∈[0,T]t\in[0,T] with Ut∈GU\_{t}\in G, we have θt​Ht>0\theta\_{t}H\_{t}>0.

Then, HH is an increasing profit.

###### Discussion 3.6.

(a) In our previous result [[1](https://arxiv.org/html/2512.07555v1#bib.bib1), Theorem 3.1], we proved that NIP is equivalent to the following three conditions:

1. (i)

   Every accessible boundary point b∈J∖J∘b\in J\setminus J^{\circ} satisfies one of the following two conditions:

   1. (i.a)

      bb is absorbing and either r=0r=0 or b=0b=0;
   2. (i.b)

      bb is reflecting and

      |  |  |  |
      | --- | --- | --- |
      |  | r​b​𝔪U​({𝔰​(b)})={12​𝔮+′​(𝔰​(α)),b=α,−12​𝔮−′​(𝔰​(β)),b=β.rb\,\mathfrak{m}^{U}(\{\mathfrak{s}(b)\})=\begin{cases}\frac{1}{2}\mathfrak{q}^{\prime}\_{+}(\mathfrak{s}(\alpha)),&b=\alpha,\\[2.84526pt] -\frac{1}{2}\mathfrak{q}^{\prime}\_{-}(\mathfrak{s}(\beta)),&b=\beta.\end{cases} |  |
2. (ii)

   r​𝔮​(x)​𝔪siU​(d​x)=12​𝔮si′′​(d​x)r\mathfrak{q}(x)\mathfrak{m}^{U}\_{\operatorname{si}}(\mathrm{d}x)=\frac{1}{2}\mathfrak{q}^{\prime\prime}\_{\operatorname{si}}(\mathrm{d}x) on ℬ​(𝔰​(J∘))\mathcal{B}(\mathfrak{s}(J^{\circ})).
3. (iii)

   r​𝔪acU​(x)=0r\mathfrak{m}^{U}\_{\operatorname{ac}}(x)=0 for λ\{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}-a.a. x∈{z∈𝔰​(J∘):𝔮′​(z)=0}x\in\{z\in\mathfrak{s}(J^{\circ})\colon\mathfrak{q}^{\prime}(z)=0\}.

Taking ([3.1](https://arxiv.org/html/2512.07555v1#S3.E1 "In 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) into account, (i) holds if and only if the last three terms in ([3.1](https://arxiv.org/html/2512.07555v1#S3.E1 "In 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) are zero, (ii) holds if and only if the second term is zero, and finally, (iii) holds if and only if the first term vanishes.
Notice that the first term in ([3.1](https://arxiv.org/html/2512.07555v1#S3.E1 "In 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) contains the additional factor 𝔮​(x)\mathfrak{q}(x), but it vanishes in at most one point, as 𝔮\mathfrak{q} is strictly increasing, and is, therefore, excluded from (iii).
As a consequence, since |ν|≡0|\nu|\equiv 0 if and only if ν≡0\nu\equiv 0, the equivalence of (i) and (ii) from Theorem [3.3](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") recovers [[1](https://arxiv.org/html/2512.07555v1#bib.bib1), Theorem 3.1].

(b) Theorem [3.3](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") reveals the fundamental importance of the trading strategy θ\theta. First, there exists an increasing profit if and only if θ∈𝖨𝖯\theta\in\mathsf{IP} and second, any increasing profit is only made on the support of θ\theta, i.e., on the set {t∈[0,T]:θt≠0}\{t\in[0,T]\colon\theta\_{t}\neq 0\}. More specifically, if HH is an increasing profit, we must have ℙ⊗μ\mathbb{P}\otimes\mu-a.e. {H>0}⊂{θ≥0}\{H>0\}\subset\{\theta\geq 0\} and {H<0}⊂{θ≤0}\{H<0\}\subset\{\theta\leq 0\}. This provides a rather precise understanding of how an increasing profit can be achieved. Proposition [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") provides a useful recipe to design increasing profits using θ\theta and non-negligible sets under the measure |ν||\nu|.
Recalling Remark [2.4](https://arxiv.org/html/2512.07555v1#S2.Thmtheorem4 "Remark 2.4. ‣ 2.2. Increasing Profits ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), scaling the strategy θ\theta allows to gain an unbounded increasing profit.

(c) The structure of θ\theta and ν\nu connects the existence of increasing profits to certain path properties of our general diffusion YY and further explains how they can be converted into increasing profits. We discuss these interpretations
in Section [5](https://arxiv.org/html/2512.07555v1#S5 "5. Examples ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") by considering a variety of examples.

(d) The Hahn decomposition N+⊔N−N\_{+}\sqcup N\_{-} is not unique (it is only unique up to null sets; see the first remark on p. 224 in [[2](https://arxiv.org/html/2512.07555v1#bib.bib2)] for details). As a consequence, the trading strategy θ\theta depends on this decomposition. Nevertheless, by virtue of Proposition [3.2](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), the value function VθV^{\theta} is independent of the choice of the Hahn decomposition in the sense that all “versions” of θ\theta lead to the same value process.

Another natural question is whether the choice of the set N𝔮′=0N\_{\mathfrak{q}^{\prime}=0} is unique. In general, we only require the following two properties: first, N𝔮′=0∩{𝔮′≠0}N\_{\mathfrak{q}^{\prime}=0}\cap\{\mathfrak{q}^{\prime}\neq 0\} must be a Lebesgue-null set and second, the signed measure ν\nu must be concentrated on N𝔮′=0N\_{\mathfrak{q}^{\prime}=0}. The purpose of the
first property is to guarantee that the value process VθV^{\theta} is of finite variation, and the purpose of the second property is explained by the structure of VθV^{\theta} as in Proposition [3.2](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), activating the possibility of a positive terminal value. Our choice of N𝔮′=0N\_{\mathfrak{q}^{\prime}=0} clearly has these two properties. Again, the value process is not affected by taking a different set with such properties.

(e) Proposition [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") provides sufficient but not necessary conditions for an increasing profit.
The point for including it is its simplicity in comparison with part (iii) from Theorem [3.4](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates").
To see that the conditions in Proposition [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") are not necessary, consider the case 𝔰​(J)=[𝔰​(α),∞)\mathfrak{s}(J)=[\mathfrak{s}(\alpha),\infty) with α∈ℛ\alpha\in\mathcal{R}, and assume that G∈ℬ​(𝔰​(J))G\in\mathcal{B}(\mathfrak{s}(J)) is such that |ν|​(G)>0|\nu|(G)>0. Then, for
R∈(𝔰​(x0),∞)R\in(\mathfrak{s}(x\_{0}),\infty)
large enough, we also have |ν|​(G∩[𝔰​(α),R])>0|\nu|(G\cap[\mathfrak{s}(\alpha),R])>0 and, following arguments from the proof of Proposition [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), one can show that

|  |  |  |
| --- | --- | --- |
|  | Ht≜θt​𝟙G∩[𝔰​(α),R]​(Ut)​𝟙{t≤TR+1​(U)},t∈[0,T],H\_{t}\triangleq\theta\_{t}\mathbbm{1}\_{G\,\cap\,[\mathfrak{s}(\alpha),R]}(U\_{t})\mathbbm{1}\_{\{t\leq T\_{R+1}(U)\}},\quad t\in[0,T], |  |

is an increasing profit. However, Ht=0H\_{t}=0 on (TR+1​(U),T](T\_{R+1}(U),T], while, for any non-empty set A∈ℬ​(𝔰​(J))A\in\mathcal{B}(\mathfrak{s}(J)), with positive probability, (TR+1​(U),T]∩{t∈[0,T]:Ut∈A}≠∅(T\_{R+1}(U),T]\cap\{t\in[0,T]\colon U\_{t}\in A\}\neq\emptyset. Again, for details we refer to the proof of Proposition [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") below. Of course, it is possible to sharpen the sufficient conditions in Proposition [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") to cover such examples. However, it seems that a precise description is difficult to formulate without using the kernel μ\mu (cf. Theorem [3.4](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") (iii)).

Last, let us stress that if the NIP condition fails, there exists always an increasing profit H∈𝖨𝖯H\in\mathsf{IP} that satisfies the properties from Proposition [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), namely the canonical strategy θ\theta.

## 4. Proofs of Theorems [3.3](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") and [3.4](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), and Propositions [3.2](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") and [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")

This section is dedicated to the proofs of our main results.
We start with Proposition [3.2](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), followed by Theorem [3.4](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") and Proposition [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), and finally, we turn to Theorem [3.3](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"). Throughout this section, to ease our presentation, we only consider the situation 𝔰​(J)=[𝔰​(α),∞)\mathfrak{s}(J)=[\mathfrak{s}(\alpha),\infty).
In this case, diffusion
and semimartingale local times coincide,
and we therefore use only the latter in the formulas below.
All other cases for 𝔰​(J)\mathfrak{s}(J) can be treated similarly.

To provide fairly self-contained proofs, let us recall some results from the references [[1](https://arxiv.org/html/2512.07555v1#bib.bib1), [4](https://arxiv.org/html/2512.07555v1#bib.bib4), [19](https://arxiv.org/html/2512.07555v1#bib.bib19), [27](https://arxiv.org/html/2512.07555v1#bib.bib27)].

###### Lemma 4.1 ([[1](https://arxiv.org/html/2512.07555v1#bib.bib1), Lemma 3.2]).

Let S=S0+M+AS=S\_{0}+M+A be the Doob–Meyer decomposition of SS, where MM is the local martingale and AA the finite variation part.

(a)
In case α\alpha is absorbing for YY, then

|  |  |  |  |
| --- | --- | --- | --- |
| (4.1) |  | d​⟨M⟩t=e−2​r​t​[𝔮+′​(Ut)]2​𝟙{t<T𝔰​(α)​(U)}​d​⟨U⟩t,d​At=e−r​t​[−r​𝔮​(Ut)​d​t+12​∫𝔰​(J∘)dLtx​(U)​𝔮′′​(d​x)],\begin{split}\mathrm{d}\langle M\rangle\_{t}&=e^{-2rt}\big[\mathfrak{q}^{\prime}\_{+}(U\_{t})\big]^{2}\mathbbm{1}\_{\{t<T\_{\mathfrak{s}(\alpha)}(U)\}}\,\mathrm{d}\langle U\rangle\_{t},\\ \mathrm{d}A\_{t}&=e^{-rt}\Big[-r\mathfrak{q}(U\_{t})\,\mathrm{d}t+\frac{1}{2}\int\_{\mathfrak{s}(J^{\circ})}\mathrm{d}L^{x}\_{t}(U)\,\mathfrak{q}^{\prime\prime}(\mathrm{d}x)\Big],\end{split} |  |

where the indicator 𝟙{t<T𝔰​(α)​(U)}\mathbbm{1}\_{\{t<T\_{\mathfrak{s}(\alpha)}(U)\}} is included
to emphasize that we do not require 𝔮+′​(𝔰​(α))\mathfrak{q}^{\prime}\_{+}(\mathfrak{s}(\alpha)) to be well-defined (and, indeed, the limit of 𝔮+′​(u)\mathfrak{q}^{\prime}\_{+}(u), as u↘𝔰​(α)u\searrow\mathfrak{s}(\alpha), can fail to exist).

(b)
In case α\alpha is reflecting for YY, then

|  |  |  |  |
| --- | --- | --- | --- |
| (4.2) |  | d​⟨M⟩t=e−2​r​t​[𝔮+′​(Ut)]2​d​⟨U⟩t,d​At=e−r​t​[−r​𝔮​(Ut)​d​t+12​𝔮+′​(𝔰​(α))​d​Lt𝔰​(α)​(U)+12​∫𝔰​(J∘)dLtx​(U)​𝔮′′​(d​x)].\begin{split}\mathrm{d}\langle M\rangle\_{t}&=e^{-2rt}\big[\mathfrak{q}^{\prime}\_{+}(U\_{t})\big]^{2}\,\mathrm{d}\langle U\rangle\_{t},\\ \mathrm{d}A\_{t}&=e^{-rt}\Big[-r\mathfrak{q}(U\_{t})\,\mathrm{d}t+\frac{1}{2}\mathfrak{q}^{\prime}\_{+}(\mathfrak{s}(\alpha))\,\mathrm{d}L^{\mathfrak{s}(\alpha)}\_{t}(U)+\frac{1}{2}\int\_{\mathfrak{s}(J^{\circ})}\mathrm{d}L^{x}\_{t}(U)\,\mathfrak{q}^{\prime\prime}(\mathrm{d}x)\Big].\end{split} |  |

###### Lemma 4.2 ([[1](https://arxiv.org/html/2512.07555v1#bib.bib1), Lemma 3.5]).

Consider an open interval I⊂ℝI\subset\mathbb{R} and a function f:I→ℝf\colon I\to\mathbb{R} such that

1. (i)

   f′f^{\prime} exists and is finite λ\{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}-a.e. on II,
2. (ii)

   f′′f^{\prime\prime} exists and is finite λ\{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}-a.e. on II.

Then, f′′​𝟙{f′=0}=0f^{\prime\prime}\mathbbm{1}\_{\{f^{\prime}=0\}}=0 λ\{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}-a.e. on II.

###### Lemma 4.3 ([[4](https://arxiv.org/html/2512.07555v1#bib.bib4), Theorem 1.1]).

For every ε∈(0,T]\varepsilon\in(0,T], x0∈𝔰​(J∘∪ℛ)x\_{0}\in\mathfrak{s}(J^{\circ}\cup\mathcal{R}) and y0∈𝔰​(J)y\_{0}\in\mathfrak{s}(J),

|  |  |  |
| --- | --- | --- |
|  | ℙ​(Ty0​(U)​<ε∣​U0=x0)>0,\mathbb{P}(T\_{y\_{0}}(U)<\varepsilon\mid U\_{0}=x\_{0})>0, |  |

where we recall that ℛ\mathcal{R} are the reflecting boundaries of YY and Ty0​(U)=inf{t∈[0,T]:Ut=y0}∧TT\_{y\_{0}}(U)=\inf\{t\in[0,T]\colon U\_{t}=y\_{0}\}\wedge T.

###### Lemma 4.4 ([[19](https://arxiv.org/html/2512.07555v1#bib.bib19), Corollary 29.18]).

Let M=(Mt)t≥0M=(M\_{t})\_{t\geq 0} be a continuous local martingale with local time process (Ltx​(M):x∈ℝ,t≥0)(L\_{t}^{x}(M)\colon x\in\mathbb{R},\,t\geq 0). Then, a.s., it holds simultaneously for all x∈ℝx\in\mathbb{R} and t∈ℝ+t\in\mathbb{R}\_{+} that

|  |  |  |
| --- | --- | --- |
|  | {Ltx​(M)>0}={infs∈[0,t]Ms<x<sups∈[0,t]Ms}.\{L\_{t}^{x}(M)>0\}=\Big\{\inf\_{s\in[0,t]}M\_{s}<x<\sup\_{s\in[0,t]}M\_{s}\Big\}. |  |

The last lemma we recall is a mild extension of the diffusion occupation time formula from [[27](https://arxiv.org/html/2512.07555v1#bib.bib27), Theorem V.49.1] as provided by [[7](https://arxiv.org/html/2512.07555v1#bib.bib7), Lemma C.15].

###### Lemma 4.5 ([[7](https://arxiv.org/html/2512.07555v1#bib.bib7), Lemma C.15]).

a.s. we have

|  |  |  |  |
| --- | --- | --- | --- |
| (4.3) |  | ∫0tf​(Us)​ds=∫𝔰​(J)f​(y)​Lty​(U)​𝔪U​(d​y)\int\_{0}^{t}f(U\_{s})\,\mathrm{d}s=\int\_{\mathfrak{s}(J)}f(y)L^{y}\_{t}(U)\,\mathfrak{m}^{U}(\mathrm{d}y) |  |

simultaneously for all t∈[0,T]t\in[0,T] and all Borel functions
f:𝔰​(J)→[0,∞]f\colon\mathfrak{s}(J)\to[0,\infty]
with f​(𝔰​(α))=0f(\mathfrak{s}(\alpha))=0 if α∈𝒜\alpha\in\mathcal{A}.

We now present the proofs for our main results.

###### Proof of Proposition [3.2](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates").

Let us start with a general observation. Denote the Doob–Meyer decomposition of SS by S=S0+M+AS=S\_{0}+M+A, where MM is the local martingale and AA is the finite variation part. Then, as VHV^{H} is of finite variation,

|  |  |  |
| --- | --- | --- |
|  | VH−∫0⋅Hs​dAs=∫0⋅Hs​dMsV^{H}-\int\_{0}^{\cdot}H\_{s}\,\mathrm{d}A\_{s}=\int^{\cdot}\_{0}H\_{s}\,\mathrm{d}M\_{s} |  |

is a continuous local martingale of finite variation and hence, constant.
Consequently,

|  |  |  |
| --- | --- | --- |
|  | VH=∫0⋅Hs​dAs.V^{H}=\int\_{0}^{\cdot}H\_{s}\,\mathrm{d}A\_{s}. |  |

Now, we distinguish the cases where α\alpha is absorbing or reflecting for YY.

Case 1: α\alpha is absorbing. By Lemma [4.1](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem1 "Lemma 4.1 ([1, Lemma 3.2]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"),

|  |  |  |
| --- | --- | --- |
|  | d​At=e−r​t​[−r​𝔮​(Ut)​d​t+12​∫𝔰​(J∘)dLtx​(U)​𝔮′′​(d​x)].\displaystyle\mathrm{d}A\_{t}=e^{-rt}\Big[-r\mathfrak{q}(U\_{t})\,\mathrm{d}t+\frac{1}{2}\int\_{\mathfrak{s}(J^{\circ})}\mathrm{d}L^{x}\_{t}(U)\,\mathfrak{q}^{\prime\prime}(\mathrm{d}x)\Big]. |  |

Using the occupation time formula for diffusions as given by Lemma [4.5](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem5 "Lemma 4.5 ([7, Lemma C.15]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), we get that

|  |  |  |
| --- | --- | --- |
|  | 𝔮​(Ut)​𝟙𝔰​(J∘)​(Ut)​d​t=∫𝔰​(J∘)𝔮​(x)​dLtx​(U)​𝔪U​(d​x).\mathfrak{q}(U\_{t})\mathbbm{1}\_{\mathfrak{s}(J^{\circ})}(U\_{t})\,\mathrm{d}t=\int\_{\mathfrak{s}(J^{\circ})}\mathfrak{q}(x)\mathrm{d}L^{x}\_{t}(U)\,\mathfrak{m}^{U}(\mathrm{d}x). |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | VH\displaystyle V^{H} | =∫0⋅Ht​e−r​t​[𝟙{Ut=𝔰​(α)}​(−r​α)​d​t+∫𝔰​(J∘)dLtx​(U)​(−r​𝔮​(x)​𝔪U​(d​x)+12​𝔮′′​(d​x))]\displaystyle=\int\_{0}^{\cdot}H\_{t}e^{-rt}\Big[\mathbbm{1}\_{\{U\_{t}=\mathfrak{s}(\alpha)\}}(-r\alpha)\,\mathrm{d}t+\int\_{\mathfrak{s}(J^{\circ})}\,\mathrm{d}L^{x}\_{t}(U)\,\Big(-r\mathfrak{q}(x)\,\mathfrak{m}^{U}(\mathrm{d}x)+\tfrac{1}{2}\,\mathfrak{q}^{\prime\prime}(\mathrm{d}x)\Big)\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.4) |  |  | =∫0⋅Ht​e−r​t​[𝟙[T𝔰​(α)​(U),T]​(t)​(−r​α)​d​t+∫𝔰​(J∘)dLtx​(U)​(−r​𝔮​(x)​𝔪U​(d​x)+12​𝔮′′​(d​x))],\displaystyle=\int\_{0}^{\cdot}H\_{t}e^{-rt}\,\Big[\mathbbm{1}\_{[T\_{\mathfrak{s}(\alpha)}(U),T]}(t)(-r\alpha)\,\mathrm{d}t+\int\_{\mathfrak{s}(J^{\circ})}\,\mathrm{d}L^{x}\_{t}(U)\,\Big(-r\mathfrak{q}(x)\,\mathfrak{m}^{U}(\mathrm{d}x)+\tfrac{1}{2}\,\mathfrak{q}^{\prime\prime}(\mathrm{d}x)\Big)\Big], |  |

where we use that α∈𝒜\alpha\in\mathcal{A}. As explained above, ∫0⋅Hs​dMs=0\int\_{0}^{\cdot}H\_{s}\,\mathrm{d}M\_{s}=0 and, in particular, Ht2​d​⟨M⟩t=0H^{2}\_{t}\,\mathrm{d}\langle M\rangle\_{t}=0.
Using the formula for ⟨M⟩\langle M\rangle from Lemma [4.1](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem1 "Lemma 4.1 ([1, Lemma 3.2]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), and the occupation time formula for semimartingales, we get, for t<T𝔰​(α)​(U)t<T\_{\mathfrak{s}(\alpha)}(U),

|  |  |  |  |
| --- | --- | --- | --- |
| (4.5) |  | 0=∫0te2​r​t​𝟙{𝔮′​(Us)≠0}[𝔮′​(Us)]2​Hs2​d​⟨M⟩s=∫0tHs2​[𝔮+′​(Us)]2​𝟙{𝔮′​(Us)≠0}[𝔮′​(Us)]2​d​⟨U⟩s=∫0tHs2​∫𝔰​(J∘)[𝔮+′​(x)]2​𝟙{𝔮′​(x)≠0}[𝔮′​(x)]2​dLsx​(U)​dx=∫0tHs2​∫𝔰​(J∘)𝟙{𝔮′​(x)≠0}​dLsx​(U)​dx.\begin{split}0&=\int\_{0}^{t}\frac{e^{2rt}\mathbbm{1}\_{\{\mathfrak{q}^{\prime}(U\_{s})\neq 0\}}}{\big[\mathfrak{q}^{\prime}(U\_{s})\big]^{2}}H^{2}\_{s}\,\mathrm{d}\langle M\rangle\_{s}\\ &=\int\_{0}^{t}H^{2}\_{s}\frac{\big[\mathfrak{q}^{\prime}\_{+}(U\_{s})\big]^{2}\mathbbm{1}\_{\{\mathfrak{q}^{\prime}(U\_{s})\neq 0\}}}{\big[\mathfrak{q}^{\prime}(U\_{s})\big]^{2}}\,\mathrm{d}\langle U\rangle\_{s}\\ &=\int\_{0}^{t}H^{2}\_{s}\,\int\_{\mathfrak{s}(J^{\circ})}\frac{\big[\mathfrak{q}^{\prime}\_{+}(x)\big]^{2}\mathbbm{1}\_{\{\mathfrak{q}^{\prime}(x)\neq 0\}}}{\big[\mathfrak{q}^{\prime}(x)\big]^{2}}\,\mathrm{d}L^{x}\_{s}(U)\,\mathrm{d}x\\ &=\int\_{0}^{t}H^{2}\_{s}\,\int\_{\mathfrak{s}(J^{\circ})}\mathbbm{1}\_{\{\mathfrak{q}^{\prime}(x)\neq 0\}}\,\mathrm{d}L^{x}\_{s}(U)\,\mathrm{d}x.\end{split} |  |

Using this identity and the fact that λ\{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}-a.e. 𝟙{𝔮′=0}​𝔮′′=0\mathbbm{1}\_{\{\mathfrak{q}^{\prime}=0\}}\mathfrak{q}^{\prime\prime}=0 by Lemma [4.2](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem2 "Lemma 4.2 ([1, Lemma 3.5]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), ([4.4](https://arxiv.org/html/2512.07555v1#S4.E4 "In 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) reformulates to ([3.3](https://arxiv.org/html/2512.07555v1#S3.E3 "In Proposition 3.2. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) and the formula is proved.

Case 2: α\alpha is reflecting. Again by Lemma [4.1](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem1 "Lemma 4.1 ([1, Lemma 3.2]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​At\displaystyle\mathrm{d}A\_{t} | =e−r​t​[−r​𝔮​(Ut)​d​t+12​𝔮+′​(𝔰​(α))​d​Lt𝔰​(α)​(U)+12​∫𝔰​(J∘)dLtx​(U)​𝔮′′​(d​x)].\displaystyle=e^{-rt}\Big[-r\mathfrak{q}(U\_{t})\,\mathrm{d}t+\frac{1}{2}\mathfrak{q}^{\prime}\_{+}(\mathfrak{s}(\alpha))\,\mathrm{d}L^{\mathfrak{s}(\alpha)}\_{t}(U)+\frac{1}{2}\int\_{\mathfrak{s}(J^{\circ})}\mathrm{d}L^{x}\_{t}(U)\,\mathfrak{q}^{\prime\prime}(\mathrm{d}x)\Big]. |  |

As α∈ℛ\alpha\in\mathcal{R}, the occupation time formula for diffusions given by Lemma [4.5](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem5 "Lemma 4.5 ([7, Lemma C.15]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") yields that

|  |  |  |
| --- | --- | --- |
|  | 𝔮​(Ut)​d​t=∫𝔰​(J)𝔮​(x)​dLtx​(U)​𝔪U​(d​x),\mathfrak{q}(U\_{t})\,\mathrm{d}t=\int\_{\mathfrak{s}(J)}\mathfrak{q}(x)\,\mathrm{d}L^{x}\_{t}(U)\,\mathfrak{m}^{U}(\mathrm{d}x), |  |

and consequently,

|  |  |  |
| --- | --- | --- |
|  | d​At=e−r​t​[(12​𝔮+′​(𝔰​(α))−r​α​𝔪U​({𝔰​(α)}))​d​Lt𝔰​(α)​(U)+∫𝔰​(J∘)dLtx​(U)​(12​𝔮′′​(d​x)−r​𝔮​(x)​𝔪U​(d​x))].\mathrm{d}A\_{t}=e^{-rt}\Big[\big(\tfrac{1}{2}\mathfrak{q}^{\prime}\_{+}(\mathfrak{s}(\alpha))-r\alpha\mathfrak{m}^{U}(\{\mathfrak{s}(\alpha)\})\big)\,\mathrm{d}L^{\mathfrak{s}(\alpha)}\_{t}(U)+\int\_{\mathfrak{s}(J^{\circ})}\mathrm{d}L^{x}\_{t}(U)\,\big(\tfrac{1}{2}\mathfrak{q}^{\prime\prime}(\mathrm{d}x)-r\mathfrak{q}(x)\,\mathfrak{m}^{U}(\mathrm{d}x)\big)\Big]. |  |

Finally, as ([4.5](https://arxiv.org/html/2512.07555v1#S4.E5 "In 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) holds irrespective of the boundary classification of α\alpha, and λ\{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}-a.e. 𝟙{𝔮′=0}​𝔮′′=0\mathbbm{1}\_{\{\mathfrak{q}^{\prime}=0\}}\mathfrak{q}^{\prime\prime}=0, again by Lemma [4.2](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem2 "Lemma 4.2 ([1, Lemma 3.5]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), the formula ([3.3](https://arxiv.org/html/2512.07555v1#S3.E3 "In Proposition 3.2. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) follows.
∎

###### Proof of Theorem [3.4](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates").

First, we prove the necessity of the conditions (i)-(iii), assuming H∈𝖨𝖯H\in\mathsf{IP}. As the value process VHV^{H} of the increasing profit HH is of finite variation, Lemma [4.1](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem1 "Lemma 4.1 ([1, Lemma 3.2]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") yields that

|  |  |  |
| --- | --- | --- |
|  | 0=⟨VH⟩T=∫0THs2​d​⟨S⟩s=∫0Te−2​r​s​(Hs​𝔮+′​(Us))2​𝟙{s<T𝔰​(𝒜)​(U)}​d​⟨U⟩s.0=\langle V^{H}\rangle\_{T}=\int\_{0}^{T}H^{2}\_{s}\,\mathrm{d}\langle S\rangle\_{s}=\int\_{0}^{T}e^{-2rs}\big(H\_{s}\mathfrak{q}^{\prime}\_{+}(U\_{s})\big)^{2}\mathbbm{1}\_{\{s<T\_{\mathfrak{s}(\mathcal{A})}(U)\}}\,\mathrm{d}\langle U\rangle\_{s}. |  |

Notice the use of T𝔰​(𝒜)​(U)T\_{\mathfrak{s}(\mathcal{A})}(U) rather than T𝔰​(α)​(U)T\_{\mathfrak{s}(\alpha)}(U) in the above display. This comprises both cases of Lemma [4.1](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem1 "Lemma 4.1 ([1, Lemma 3.2]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") into one formula.
The latter display implies that d​⟨U⟩⊗ℙ\mathrm{d}\langle U\rangle\otimes\mathbb{P}-a.e. H​𝔮+′​(U)=0H\mathfrak{q}^{\prime}\_{+}(U)=0 on [0,T𝔰​(𝒜)​(U))[0,T\_{\mathfrak{s}(\mathcal{A})}(U)), i.e., part (i) holds.
We next establish part (ii).
As VHV^{H} is of finite variation, we can apply Proposition [3.2](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), which yields that

|  |  |  |
| --- | --- | --- |
|  | VtH=∫0tHs​e−r​s​∫(𝟙𝔰​(J∖𝒜)​(x)​d​Lsx​(U)+𝟙𝔰​(𝒜)​(x)​𝟙(Tx​(U),T]​(s)​d​s)​ν​(d​x).\displaystyle V^{H}\_{t}=\int\_{0}^{t}H\_{s}e^{-rs}\int\Big(\mathbbm{1}\_{\mathfrak{s}(J\,\setminus\,\mathcal{A})}(x)\,\mathrm{d}L^{x}\_{s}(U)+\mathbbm{1}\_{\mathfrak{s}(\mathcal{A})}(x)\mathbbm{1}\_{(T\_{x}(U),T]}(s)\,\mathrm{d}s\Big)\,\nu(\mathrm{d}x). |  |

Using that ν\nu is concentrated on N𝔮′=0N\_{\mathfrak{q}^{\prime}=0}, the identity θ2=𝟙N𝔮′=0​(U)\theta^{2}=\mathbbm{1}\_{N\_{\mathfrak{q}^{\prime}=0}}(U), the identities in ([3.4](https://arxiv.org/html/2512.07555v1#S3.E4 "In 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")), and the occupation time formula for semimartingales, we compute that, for t∈[0,T]t\in[0,T],

|  |  |  |  |
| --- | --- | --- | --- |
| (4.6) |  | VtH=∫0tθs​Hs​e−r​s​∫(𝟙𝔰​(J∖𝒜)​(x)​d​Lsx​(U)+𝟙𝔰​(𝒜)​(x)​𝟙(Tx​(U),T]​(s)​d​s)​|ν|​(d​x)=∫0tθs​Hs​e−r​s​μ​(d​s,⋅).\begin{split}V^{H}\_{t}&=\int\_{0}^{t}\theta\_{s}H\_{s}e^{-rs}\int\Big(\mathbbm{1}\_{\mathfrak{s}(J\,\setminus\,\mathcal{A})}(x)\,\mathrm{d}L^{x}\_{s}(U)+\mathbbm{1}\_{\mathfrak{s}(\mathcal{A})}(x)\mathbbm{1}\_{(T\_{x}(U),T]}(s)\,\mathrm{d}s\Big)\,|\nu|(\mathrm{d}x)\\ &=\int\_{0}^{t}\theta\_{s}H\_{s}e^{-rs}\,\mu(\mathrm{d}s,\cdot\,).\end{split} |  |

As VHV^{H} is an increasing process, the same holds for

|  |  |  |
| --- | --- | --- |
|  | ∫0⋅er​s​dVsH=∫0⋅θs​Hs​μ​(d​s,⋅).\int\_{0}^{\cdot}e^{rs}\,\mathrm{d}V^{H}\_{s}=\int\_{0}^{\cdot}\theta\_{s}H\_{s}\,\mu(\mathrm{d}s,\cdot\,). |  |

The standard measure theory yields that μ⊗ℙ\mu\otimes\mathbb{P}-a.e. θ​H≥0\theta H\geq 0, which means that (ii) holds.
Finally, as ℙ​(VTH>0)>0\mathbb{P}(V^{H}\_{T}>0)>0, we also have

|  |  |  |
| --- | --- | --- |
|  | ℙ​(∫0Tθs​Hs​e−r​s​μ​(d​s,⋅)>0)>0,\mathbb{P}\Big(\int\_{0}^{T}\theta\_{s}H\_{s}e^{-rs}\mu(\mathrm{d}s,\cdot\,)>0\Big)>0, |  |

which clearly implies

|  |  |  |
| --- | --- | --- |
|  | ℙ​(μ​({t∈[0,T]:θt​Ht>0},⋅)>0)>0.\mathbb{P}(\mu(\{t\in[0,T]\colon\theta\_{t}H\_{t}>0\},\cdot\,)>0)>0. |  |

In summary, (i)-(iii) hold, completing the proof of the necessity direction.

We turn to the proof of the converse direction, assuming that H∈L​(S)H\in L(S) satisfies (i)-(iii).
In the following we show ([4.6](https://arxiv.org/html/2512.07555v1#S4.E6 "In 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")),
which implies H∈𝖨𝖯H\in\mathsf{IP}. More precisely, then (ii) implies that VHV^{H} is increasing and (iii) implies that it has a positive terminal value with positive probability.

As explained in the first part of this proof, to get ([4.6](https://arxiv.org/html/2512.07555v1#S4.E6 "In 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) it suffices to prove that VHV^{H} is of finite variation. Using property (i) and Lemma [4.1](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem1 "Lemma 4.1 ([1, Lemma 3.2]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), we get that ⟨VH⟩=0\langle V^{H}\rangle=0, which implies that VHV^{H} is of finite variation.
∎

###### Proof of Proposition [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates").

By virtue of Theorem [3.4](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), it suffices to understand the implication

|  |  |  |  |
| --- | --- | --- | --- |
| (4.7) |  | ∃G∈ℬ​(𝔰​(J)):|ν|​(G)>0,a.s.θH>0 on {t∈[0,T]:Ut∈G}⟹ℙ​(μ​({t∈[0,T]:θt​Ht>0},⋅)>0)>0.\begin{split}\exists\,G\in\mathcal{B}(\mathfrak{s}(J))\colon|\nu|(G)>0&,\,\text{a.s.}\ \theta H>0\text{ on }\{t\in[0,T]\colon U\_{t}\in G\}\\ &\implies\mathbb{P}(\mu(\{t\in[0,T]\colon\theta\_{t}H\_{t}>0\},\cdot\,)>0)>0.\end{split} |  |

We assume that GG is as in ([4.7](https://arxiv.org/html/2512.07555v1#S4.E7 "In 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")).
By the monotone convergence theorem,

|  |  |  |
| --- | --- | --- |
|  | |ν|​(G∩[𝔰​(α),R])→|ν|​(G)>0,R↗∞.|\nu|(G\cap[\mathfrak{s}(\alpha),R])\to|\nu|(G)>0,\quad R\nearrow\infty. |  |

Hence, there exists an R∈(𝔰​(x0),∞)R\in(\mathfrak{s}(x\_{0}),\infty) such that |ν|​(G∩[𝔰​(α),R])>0|\nu|(G\cap[\mathfrak{s}(\alpha),R])>0.
We now prove that

|  |  |  |  |
| --- | --- | --- | --- |
| (4.8) |  | ℙ​(μ​({t∈[0,T]:Ut∈G∩[𝔰​(α),R]},⋅)>0)>0,\displaystyle\mathbb{P}(\mu(\{t\in[0,T]\colon U\_{t}\in G\cap[\mathfrak{s}(\alpha),R]\},\cdot\,)>0)>0, |  |

which implies the implication ([4.7](https://arxiv.org/html/2512.07555v1#S4.E7 "In 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) and hence, completes the proof.
Our argument is split into three steps. Before we start, recall that

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ({t∈[0,T]:\displaystyle\mu(\{t\in[0,T]\colon | Ut∈G∩[𝔰(α),R]},⋅)\displaystyle U\_{t}\in G\cap[\mathfrak{s}(\alpha),R]\},\cdot\,) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫G∩([𝔰​(α),R]∖𝔰​(𝒜))LTx​(U)​|ν|​(d​x)+|ν​(G∩𝔰​(𝒜))|​((T𝔰​(α)​(U)∨T)−T𝔰​(α)​(U)).\displaystyle=\int\_{G\,\cap\,([\mathfrak{s}(\alpha),R]\setminus\mathfrak{s}(\mathcal{A}))}L^{x}\_{T}(U)\,|\nu|(\mathrm{d}x)+|\nu(G\cap\mathfrak{s}(\mathcal{A}))|\big((T\_{\mathfrak{s}(\alpha)}(U)\vee T)-T\_{\mathfrak{s}(\alpha)}(U)\big). |  |

Step 1:
If |ν|​(G∩𝔰​(𝒜))>0|\nu|(G\cap\mathfrak{s}(\mathcal{A}))>0, then statement ([4.8](https://arxiv.org/html/2512.07555v1#S4.E8 "In 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) follows from Lemma [4.3](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem3 "Lemma 4.3 ([4, Theorem 1.1]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"),
as the latter implies ℙ​(T𝔰​(α)​(U)<T)>0\mathbb{P}(T\_{\mathfrak{s}(\alpha)}(U)<T)>0.

In the following two steps, we will show that

|  |  |  |  |
| --- | --- | --- | --- |
| (4.9) |  | ℙ​(LTx​(U)>0​ for all ​x∈[𝔰​(α),R]∖𝔰​(𝒜))>0,\displaystyle\mathbb{P}(L^{x}\_{T}(U)>0\text{ for all }x\in[\mathfrak{s}(\alpha),R]\setminus\mathfrak{s}(\mathcal{A}))>0, |  |

which entails ([4.8](https://arxiv.org/html/2512.07555v1#S4.E8 "In 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"))
whenever |ν|​(G∩𝔰​(𝒜))=0|\nu|(G\cap\mathfrak{s}(\mathcal{A}))=0, as then |ν|​(G∩([𝔰​(α),R]∖𝔰​(𝒜)))>0|\nu|\big(G\cap([\mathfrak{s}(\alpha),R]\setminus\mathfrak{s}(\mathcal{A}))\big)>0.

Step 2: We now show that a.s. on {T𝔰​(α)​(U)<T,TR​(U)<T}\{T\_{\mathfrak{s}(\alpha)}(U)<T,\,T\_{R}(U)<T\},

|  |  |  |
| --- | --- | --- |
|  | LTx​(U)>0​ for all x∈[𝔰​(α),R]∖𝔰​(𝒜).L^{x}\_{T}(U)>0\text{ for all $x\in[\mathfrak{s}(\alpha),R]\setminus\mathfrak{s}(\mathcal{A})$}. |  |

To see this, recall from [[19](https://arxiv.org/html/2512.07555v1#bib.bib19), Theorem 33.9] that there exists a Brownian motion B=(Bs)s≥0B=(B\_{s})\_{s\geq 0} (possibly on an extended probability space) such that a.s. Ut=BγtU\_{t}=B\_{\gamma\_{t}} for t∈[0,T]t\in[0,T], where

|  |  |  |
| --- | --- | --- |
|  | γt≜inf{s≥0:∫𝔰​(J)Lsx​(B)​𝔪U​(d​x)>t}.\gamma\_{t}\triangleq\inf\Big\{s\geq 0\colon\int\_{\mathfrak{s}(J)}L^{x}\_{s}(B)\,\mathfrak{m}^{U}(\mathrm{d}x)>t\Big\}. |  |

Moreover, it is easy to see that t↦γtt\mapsto\gamma\_{t} is a.s. strictly increasing on the set [0,T𝔰​(𝒜)​(U))[0,T\_{\mathfrak{s}(\mathcal{A})}(U)). We now distinguish the cases where α\alpha is reflecting or absorbing.

Case 1: α∈ℛ\alpha\in\mathcal{R}. On the set {T𝔰​(α)​(U)<T,TR​(U)<T}\{T\_{\mathfrak{s}(\alpha)}(U)<T,\,T\_{R}(U)<T\}, we have a.s. γT>T𝔰​(α)​(B)∨TR​(B)\gamma\_{T}>T\_{\mathfrak{s}(\alpha)}(B)\vee T\_{R}(B) and hence, by standard properties of Brownian paths, a.s.

|  |  |  |
| --- | --- | --- |
|  | mins∈[0,γT]⁡Bs<𝔰​(α),maxs∈[0,γT]⁡Bs>R.\min\_{s\in[0,\gamma\_{T}]}B\_{s}<\mathfrak{s}(\alpha),\quad\max\_{s\in[0,\gamma\_{T}]}B\_{s}>R. |  |

Consequently, Lemma [4.4](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem4 "Lemma 4.4 ([19, Corollary 29.18]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") yields that, a.s. on {T𝔰​(α)​(U)<T,TR​(U)<T}\{T\_{\mathfrak{s}(\alpha)}(U)<T,\,T\_{R}(U)<T\}, LTx​(U)=LγTx​(B)>0L\_{T}^{x}(U)=L\_{\gamma\_{T}}^{x}(B)>0 for all x∈[𝔰​(α),R]x\in[\mathfrak{s}(\alpha),R].

Case 2: α∈𝒜\alpha\in\mathcal{A}. While we still have a.s. γT>TR​(B)\gamma\_{T}>T\_{R}(B) on {T>TR​(U)}\{T>T\_{R}(U)\}, the difference to the previous case is that only a.s. γT=T𝔰​(α)​(B)\gamma\_{T}=T\_{\mathfrak{s}(\alpha)}(B) on {T>T𝔰​(α)​(U)}\{T>T\_{\mathfrak{s}(\alpha)}(U)\}. Thus, we can only conclude that, a.s. on {T𝔰​(α)​(U)<T,TR​(U)<T}\{T\_{\mathfrak{s}(\alpha)}(U)<T,\,T\_{R}(U)<T\},

|  |  |  |
| --- | --- | --- |
|  | mins∈[0,γT]⁡Bs=𝔰​(α),maxs∈[0,γT]⁡Bs>R.\min\_{s\in[0,\gamma\_{T}]}B\_{s}=\mathfrak{s}(\alpha),\quad\max\_{s\in[0,\gamma\_{T}]}B\_{s}>R. |  |

Using Lemma [4.4](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem4 "Lemma 4.4 ([19, Corollary 29.18]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), we still get, a.s. on {T𝔰​(α)​(U)<T,TR​(U)<T}\{T\_{\mathfrak{s}(\alpha)}(U)<T,\,T\_{R}(U)<T\}, LTx​(U)>0L\_{T}^{x}(U)>0 for all x∈(𝔰​(α),R]x\in(\mathfrak{s}(\alpha),R], which is precisely what we claimed.

Step 3: We now prove that ℙ​(T𝔰​(α)​(U)<T,TR​(U)<T)>0\mathbb{P}(T\_{\mathfrak{s}(\alpha)}(U)<T,\,T\_{R}(U)<T)>0.
Using the strong Markov property of UU and Lemma [4.3](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem3 "Lemma 4.3 ([4, Theorem 1.1]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), we get that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(T𝔰​(α)​(U)<T,TR​(U)<T)≥ℙ​(T𝔰​(α)​(U⋅+TR​(U))<T/2,TR​(U)<T/2)=ℙ​(T𝔰​(α)​(U)​<T/2∣​U0=R)​ℙ​(TR​(U)<T/2)>0.\begin{split}\mathbb{P}(T\_{\mathfrak{s}(\alpha)}(U)<T,\,T\_{R}(U)<T)&\geq\mathbb{P}(T\_{\mathfrak{s}(\alpha)}(U\_{\cdot+T\_{R}(U)})<T/2,\,T\_{R}(U)<T/2)\\ &=\mathbb{P}(T\_{\mathfrak{s}(\alpha)}(U)<T/2\mid U\_{0}=R)\mathbb{P}(T\_{R}(U)<T/2)>0.\end{split} |  |

In summary, ([4.9](https://arxiv.org/html/2512.07555v1#S4.E9 "In 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) follows and the proof complete.
∎

###### Proof of Theorem [3.3](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates").

The implication (iii) ⟹\implies (i) is trivial, and (i) ⟹\implies (ii) follows by contraposition: if |ν|≡0|\nu|\equiv 0, then ν≡0\nu\equiv 0 and Proposition [3.2](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") yields that 𝖨𝖯=∅\mathsf{IP}=\emptyset.

It remains to prove the implication (ii) ⟹\implies (iii).
We use Proposition [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), verifying [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")-(i)-(iii) for H=θH=\theta.
Using the occupation time formula for semimartingales, we obtain that

|  |  |  |
| --- | --- | --- |
|  | ∫0T|θs​𝔮+′​(Us)|​d​⟨U⟩s=∫𝟙N𝔮′=0​(x)​|𝔮+′​(x)|​LTx​(U)​dx=∫𝟙{𝔮+′​(x)=0}​|𝔮+′​(x)|​LTx​(U)​dx=0,\displaystyle\int\_{0}^{T}|\theta\_{s}\mathfrak{q}^{\prime}\_{+}(U\_{s})|\,\mathrm{d}\langle U\rangle\_{s}=\int\mathbbm{1}\_{N\_{\mathfrak{q}^{\prime}=0}}(x)|\mathfrak{q}^{\prime}\_{+}(x)|L^{x}\_{T}(U)\,\mathrm{d}x=\int\mathbbm{1}\_{\{\mathfrak{q}^{\prime}\_{+}(x)=0\}}|\mathfrak{q}^{\prime}\_{+}(x)|L^{x}\_{T}(U)\,\mathrm{d}x=0, |  |

which proves [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")-(i).
Next, [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")-(ii) holds trivially, since θ2≥0\theta^{2}\geq 0.
Finally, take G∈ℬ​(𝔰​(J))G\in\mathcal{B}(\mathfrak{s}(J)) with |ν|​(G)>0|\nu|(G)>0.
Then, |ν|​(G∩N𝔮′=0)>0|\nu|(G\cap N\_{\mathfrak{q}^{\prime}=0})>0, because |ν||\nu| is concentrated on N𝔮′=0N\_{\mathfrak{q}^{\prime}=0}, and since θ2=𝟙N𝔮′=0​(U)>0\theta^{2}=\mathbbm{1}\_{N\_{\mathfrak{q}^{\prime}=0}}(U)>0 on {t∈[0,T]:Ut∈G∩N𝔮′=0}\{t\in[0,T]\colon U\_{t}\in G\cap N\_{\mathfrak{q}^{\prime}=0}\}, [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")-(iii) holds. The proof is complete.
∎

## 5. Examples

The structure of θ\theta and ν\nu connects the existence of increasing profits to path properties of our general diffusion YY, explaining how they can generate strategies that are increasing profits.
In the following, we illustrate these connections through a variety of examples.
For reader’s convenience, we recall that ν\nu is the signed measure on (𝔰​(J),ℬ​(𝔰​(J)))(\mathfrak{s}(J),\mathcal{B}(\mathfrak{s}(J))) that is given by the formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν​(d​x)=−\displaystyle\nu(\mathrm{d}x)=- | 1{𝔮′=0}∩𝔰​(J∘)​(x)​r​𝔮​(x)​𝔪acU​(x)​d​x\displaystyle\,\mathbbm{1}\_{\{\mathfrak{q}^{\prime}=0\}\,\cap\,\mathfrak{s}(J^{\circ})}(x)r\mathfrak{q}(x)\mathfrak{m}^{U}\_{\operatorname{ac}}(x)\,\mathrm{d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟙𝔰​(J∘)​(x)​[12​𝔮si′′​(d​x)−r​𝔮​(x)​𝔪siU​(d​x)]\displaystyle+\mathbbm{1}\_{\mathfrak{s}(J^{\circ})}(x)\big[\tfrac{1}{2}\mathfrak{q}^{\prime\prime}\_{\operatorname{si}}(\mathrm{d}x)-r\mathfrak{q}(x)\mathfrak{m}^{U}\_{{\operatorname{si}}}(\mathrm{d}x)\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝟙{α∈𝒜}​r​α​δ𝔰​(α)​(d​x)−𝟙{β∈𝒜}​r​β​δ𝔰​(β)​(d​x)\displaystyle-\mathbbm{1}\_{\{\alpha\,\in\,\mathcal{A}\}}r\alpha\,\delta\_{\mathfrak{s}(\alpha)}(\mathrm{d}x)-\mathbbm{1}\_{\{\beta\,\in\,\mathcal{A}\}}r\beta\,\delta\_{\mathfrak{s}(\beta)}(\mathrm{d}x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟙{α∈ℛ}​(12​𝔮+′​(𝔰​(α))−r​α​𝔪U​({𝔰​(α)}))​δ𝔰​(α)​(d​x)\displaystyle+\mathbbm{1}\_{\{\alpha\,\in\,\mathcal{R}\}}(\tfrac{1}{2}\mathfrak{q}^{\prime}\_{+}(\mathfrak{s}(\alpha))-r\alpha\mathfrak{m}^{U}(\{\mathfrak{s}(\alpha)\}))\,\delta\_{\mathfrak{s}(\alpha)}(\mathrm{d}x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟙{β∈ℛ}​(−12​𝔮−′​(𝔰​(β))−r​β​𝔪U​({𝔰​(β)}))​δ𝔰​(β)​(d​x).\displaystyle+\mathbbm{1}\_{\{\beta\,\in\,\mathcal{R}\}}(-\tfrac{1}{2}\mathfrak{q}^{\prime}\_{-}(\mathfrak{s}(\beta))-r\beta\mathfrak{m}^{U}(\{\mathfrak{s}(\beta)\}))\,\delta\_{\mathfrak{s}(\beta)}(\mathrm{d}x). |  |

We start discussing the situation where YY attains boundary points, which possibly activates some of the last three lines in the definition of ν\nu. The first example discusses cases with absorbing boundaries,
which turns out to be the case with the easiest interpretation.

###### Example 5.1 (Engelbert–Schmidt diffusion market model).

Consider a classical SDE model

|  |  |  |
| --- | --- | --- |
|  | d​Yt=b​(Yt)​d​t+σ​(Yt)​d​Wt,Y0=y0∈J∘≜(α,β),\mathrm{d}Y\_{t}=b(Y\_{t})\,\mathrm{d}t+\sigma(Y\_{t})\,\mathrm{d}W\_{t},\quad Y\_{0}=y\_{0}\in J^{\circ}\triangleq(\alpha,\beta), |  |

where W=(Wt)t∈[0,T]W=(W\_{t})\_{t\in[0,T]} is a Brownian motion and the coefficients b:J∘→ℝb\colon J^{\circ}\to\mathbb{R} and σ:J∘→ℝ\sigma\colon J^{\circ}\to\mathbb{R} are Borel functions that satisfy the Engelbert–Schmidt conditions

|  |  |  |
| --- | --- | --- |
|  | ∀x∈J∘:σ​(x)≠0,1+|b|σ2∈Lloc1​(J∘).\forall\,x\in J^{\circ}:\;\sigma(x)\neq 0,\quad\frac{1+|b|}{\sigma^{2}}\in L^{1}\_{\textup{loc}}(J^{\circ}). |  |

We assume that (Y,W)(Y,W) is a weak solution to the above SDE and we stipulate that YY gets absorbed in {α,β}\{\alpha,\beta\} when it hits this set.
This convention is in conjunction with the classical Engelbert–Schmidt theory [[11](https://arxiv.org/html/2512.07555v1#bib.bib11)]; see Chapter 5.5 in [[21](https://arxiv.org/html/2512.07555v1#bib.bib21)] for a textbook presentation.
The sets 𝒜\mathcal{A} and J≜J∘∪𝒜J\triangleq J^{\circ}\cup\mathcal{A} are determined via bb and σ\sigma by Feller’s test for explosion; see [[21](https://arxiv.org/html/2512.07555v1#bib.bib21), Proposition 5.5.29].
Moreover, we need to choose bb and σ\sigma in such a way that we get J⊂ℝJ\subset\mathbb{R}
(notice that the latter is necessary for Standing Assumption [2.1](https://arxiv.org/html/2512.07555v1#S2.Thmtheorem1 "Standing Assumption 2.1. ‣ 2.1. The Financial Market ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")),
i.e.,
explosions at infinite boundary points are not allowed.
To be more specific, with

|  |  |  |
| --- | --- | --- |
|  | 𝔰​(x)≜∫xexp⁡{−∫y2​b​(z)σ2​(z)​dz}​dy​ for ​x∈(α,β), and ​𝔰​(α)≜limy↘α𝔰​(y),𝔰​(β)≜limy↗β𝔰​(y),\mathfrak{s}(x)\triangleq\int^{x}\exp\Big\{-\int^{y}\frac{2b(z)}{\sigma^{2}(z)}\,\mathrm{d}z\Big\}\,\mathrm{d}y\text{ for }x\in(\alpha,\beta),\text{ and }\mathfrak{s}(\alpha)\triangleq\lim\_{y\searrow\alpha}\mathfrak{s}(y),\ \,\mathfrak{s}(\beta)\triangleq\lim\_{y\nearrow\beta}\mathfrak{s}(y), |  |

for every b∈{α,β}∖ℝb\in\{\alpha,\beta\}\setminus\mathbb{R} one of the following two items must hold:

1. (a)

   |𝔰​(b)|=∞|\mathfrak{s}(b)|=\infty;
2. (b)

   |𝔰​(b)|<∞|\mathfrak{s}(b)|<\infty and, for every non-empty interval I⊂J∘I\subset J^{\circ} with bb as endpoint,

   |  |  |  |
   | --- | --- | --- |
   |  | ∫I|𝔰​(b)−𝔰​(y)|𝔰′​(y)​σ2​(y)​dy=∞.\int\_{I}\frac{|\mathfrak{s}(b)-\mathfrak{s}(y)|}{\mathfrak{s}^{\prime}(y)\sigma^{2}(y)}\,\mathrm{d}y=\infty. |  |

This guarantees that the solution process YY cannot reach the values ±∞\pm\infty. In the same spirit, we characterize

|  |  |  |
| --- | --- | --- |
|  | 𝒜={b∈{α,β}∩ℝ:both (a) and (b) above fail}.\mathcal{A}=\big\{b\in\{\alpha,\beta\}\cap\mathbb{R}\colon\text{both (a) and (b) above fail}\,\big\}. |  |

It is well-known ([[11](https://arxiv.org/html/2512.07555v1#bib.bib11)]) that YY is a general diffusion with scale function 𝔰\mathfrak{s} and speed measure

|  |  |  |
| --- | --- | --- |
|  | 𝔪​(d​x)≜d​x𝔰′​(x)​σ2​(x)​ on ​ℬ​(J∘),𝔪​({b})≜∞​∀b∈𝒜.\mathfrak{m}(\mathrm{d}x)\triangleq\frac{\mathrm{d}x}{\mathfrak{s}^{\prime}(x)\sigma^{2}(x)}\text{ on }\mathcal{B}(J^{\circ}),\qquad\mathfrak{m}(\{b\})\triangleq\infty\;\;\forall\,b\in\mathcal{A}. |  |

Lastly, let us comment on Standing Assumption [2.1](https://arxiv.org/html/2512.07555v1#S2.Thmtheorem1 "Standing Assumption 2.1. ‣ 2.1. The Financial Market ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), i.e., when YY is a semimartingale.
By definition of a weak solution up to explosion (see Definition 5.5.20 in [[21](https://arxiv.org/html/2512.07555v1#bib.bib21)]), the solution process YY is always a semimartingale on the stochastic interval [0,T𝒜​(Y))[0,T\_{\mathcal{A}}(Y)). However, it is a delicate point that the semimartingale property can get lost at the hitting time of a boundary point,
see the counterexamples in [[23](https://arxiv.org/html/2512.07555v1#bib.bib23), Section 4].
We give a flavor for conditions on bb and σ\sigma that entail Standing Assumption [2.1](https://arxiv.org/html/2512.07555v1#S2.Thmtheorem1 "Standing Assumption 2.1. ‣ 2.1. The Financial Market ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"): if α∈J\alpha\in J but β∉J\beta\not\in J, then it holds if and only if

|  |  |  |
| --- | --- | --- |
|  | ∫α+|𝔰​(y)−𝔰​(α)|𝔰′​(y)​|b​(y)|σ2​(y)​dy<∞\int\_{\alpha+}\frac{|\mathfrak{s}(y)-\mathfrak{s}(\alpha)|}{\mathfrak{s}^{\prime}(y)}\frac{|b(y)|}{\sigma^{2}(y)}\,\mathrm{d}y<\infty |  |

(cf. [[6](https://arxiv.org/html/2512.07555v1#bib.bib6)] or [[23](https://arxiv.org/html/2512.07555v1#bib.bib23), Corollary 3.6]).

Next, it is straightforward to prove that the function 𝔮=𝔰−1\mathfrak{q}=\mathfrak{s}^{-1} is continuously differentiable with absolutely continuous derivative.
In particular, the measures 𝔮′′​(d​x)\mathfrak{q}^{\prime\prime}(\mathrm{d}x) and 𝔪U=𝔪∘𝔰−1\mathfrak{m}^{U}=\mathfrak{m}\circ\mathfrak{s}^{-1} are absolutely continuous w.r.t. the Lebesgue measure.
Moreover, as, for all x∈𝔰​(J∘)x\in\mathfrak{s}(J^{\circ}),

|  |  |  |
| --- | --- | --- |
|  | 𝔮′​(x)=exp⁡{∫𝔮​(x)2​b​(z)σ2​(z)​dz}>0,\mathfrak{q}^{\prime}(x)=\exp\Big\{\int^{\mathfrak{q}(x)}\frac{2b(z)}{\sigma^{2}(z)}\,\mathrm{d}z\Big\}>0, |  |

we obtain that

|  |  |  |
| --- | --- | --- |
|  | ν​(d​x)=−∑b∈𝒜r​b​δ𝔰​(b)​(d​x).\nu(\mathrm{d}x)=-\sum\_{b\in\mathcal{A}}rb\,\delta\_{\mathfrak{s}(b)}(\mathrm{d}x). |  |

As
a consequence of Theorem [3.3](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), NIP holds if and only if r​b=0rb=0 for all
b∈𝒜=J∖J∘b\in\mathcal{A}=J\setminus J^{\circ}. This recovers the well-known fact that NIP holds in the zero interest rate regime, but we also observe that there are increasing profits in the non-zero interest rate regime when YY has non-zero (necessarily absorbing) boundary points.
For suitable choices of N+,N−N\_{+},N\_{-}, depending on the sign of r​b≠0rb\neq 0,
b∈𝒜b\in\mathcal{A},
and
N𝔮′=0=𝔰​(𝒜)N\_{\mathfrak{q}^{\prime}=0}=\mathfrak{s}(\mathcal{A}), we find that

|  |  |  |
| --- | --- | --- |
|  | θ=−∑b∈𝒜sgn⁡(r​b)​𝟙{U=𝔰​(b)}=−∑b∈𝒜sgn⁡(r​b)​𝟙[T𝔰​(b)​(U),T],\theta=-\sum\_{b\in\mathcal{A}}\,\operatorname{sgn}(rb)\mathbbm{1}\_{\{U\,=\,\mathfrak{s}(b)\}}=-\sum\_{b\in\mathcal{A}}\,\operatorname{sgn}(rb)\mathbbm{1}\_{[T\_{\mathfrak{s}(b)}(U),T]}, |  |

is an increasing profit with value process

|  |  |  |
| --- | --- | --- |
|  | Vtθ=∑b∈𝒜∫T𝔰​(b)​(U)T𝔰​(b)​(U)∨t|b​r|​e−r​s​ds=∑b∈𝒜|b​(e−r​T𝔰​(b)​(U)−e−r​(T𝔰​(b)​(U)∨t))|.V^{\theta}\_{t}=\sum\_{b\in\mathcal{A}}\int\_{T\_{\mathfrak{s}(b)}(U)}^{T\_{\mathfrak{s}(b)}(U)\vee\,t}|br|e^{-rs}\,\mathrm{d}s=\sum\_{b\in\mathcal{A}}\big|b(e^{-rT\_{\mathfrak{s}(b)}(U)}-e^{-r(T\_{\mathfrak{s}(b)}(U)\vee\,t)})\big|. |  |

To
get the idea behind these results, assume that r​b≠0rb\neq 0 for some b∈𝒜b\in\mathcal{A}.
In this case, on the time interval [T𝔰​(b)​(U),T][T\_{\mathfrak{s}(b)}(U),T], the discounted price process St=e−r​t​YtS\_{t}=e^{-rt}Y\_{t} is non-constant and either increasing or decreasing. Thus, we achieve an increasing profit either by buying or selling the risky asset at time T𝔰​(b)​(U)T\_{\mathfrak{s}(b)}(U). This is exactly what θ\theta suggests (and its sign accounts for buying or selling).

We now turn to the case with reflecting boundary points, which deals with the final two terms of the auxiliary signed measure ν\nu. We notice that these have two different ingredients, namely 𝔮±′​(𝔰​(b))\mathfrak{q}^{\prime}\_{\pm}(\mathfrak{s}(b)) and r​b​𝔪U​({𝔰​(b)})rb\mathfrak{m}^{U}(\{\mathfrak{s}(b)\}), where b∈ℛb\in\mathcal{R}. Both of these terms turn out to be related to local time effects, but with a quite different flavor. The first one represents local time terms in the drift that account for reflection from the boundary, while the second term measures stickiness in the reflecting boundary.

###### Example 5.2 (Black–Scholes model with reflection).

Consider a version of the Black–Scholes model with reflection from a positive boundary. This model has been studied in [[5](https://arxiv.org/html/2512.07555v1#bib.bib5)], where it was shown that NIP fails for this model in the zero interest rate regime.
We introduce the model through its scale function and speed measure, taking
J=[1,∞)J=[1,\infty), μ∈ℝ\mu\in\mathbb{R}, σ>0\sigma>0 and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔰​(x)\displaystyle\mathfrak{s}(x) | =∫xy−2​μ/σ2​dy,x∈[1,∞),\displaystyle=\int^{x}y^{-2\mu/\sigma^{2}}\,\mathrm{d}y,\ x\in[1,\infty), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔪​(d​x)\displaystyle\mathfrak{m}(\mathrm{d}x) | =x2​μ/σ2−2σ2​d​x​ on ​ℬ​((1,∞)),𝔪​({1})∈[0,∞).\displaystyle=\frac{x^{2\mu/\sigma^{2}-2}}{\sigma^{2}}\,\mathrm{d}x\text{ on }\mathcal{B}((1,\infty)),\quad\mathfrak{m}(\{1\})\in[0,\infty). |  |

The value 𝔪​({1})∈[0,∞)\mathfrak{m}(\{1\})\in[0,\infty) decides about the reflective behavior of the model. If 𝔪​({1})=0\mathfrak{m}(\{1\})=0 the reflection is instantaneous, as in the paper [[5](https://arxiv.org/html/2512.07555v1#bib.bib5)], and if 𝔪​({1})>0\mathfrak{m}(\{1\})>0, the boundary point 11 is sticky reflecting.
Again, the second derivative measure 𝔮′′​(d​x)\mathfrak{q}^{\prime\prime}(\mathrm{d}x) is absolutely continuous w.r.t. the Lebesgue measure, 𝔮′>0\mathfrak{q}^{\prime}>0 with
𝔮+′​(𝔰​(1))=1\mathfrak{q}^{\prime}\_{+}(\mathfrak{s}(1))=1,
and we get that

|  |  |  |
| --- | --- | --- |
|  | ν​(d​x)=(12−r​𝔪​({1}))​δ𝔰​(1)​(d​x),\displaystyle\nu(\mathrm{d}x)=\Big(\frac{1}{2}-r\mathfrak{m}(\{1\})\Big)\,\delta\_{\mathfrak{s}(1)}(\mathrm{d}x), |  |

as, clearly, 𝔪U​({𝔰​(1)})=𝔪​({1})\mathfrak{m}^{U}(\{\mathfrak{s}(1)\})=\mathfrak{m}(\{1\}).
Using Theorem [3.3](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), we obtain that

|  |  |  |
| --- | --- | --- |
|  | NIP holds⟺r​𝔪​({1})=12.\text{NIP holds}\quad\Longleftrightarrow\quad r\mathfrak{m}(\{1\})=\frac{1}{2}. |  |

In particular, if r=0r=0 or 𝔪​({1})=0\mathfrak{m}(\{1\})=0, there exists an increasing profit, covering the observation from [[5](https://arxiv.org/html/2512.07555v1#bib.bib5)].
If NIP fails,

|  |  |  |
| --- | --- | --- |
|  | θ=sgn⁡(12−r​𝔪​({1}))​𝟙{Y= 1}\theta=\operatorname{sgn}\Big(\frac{1}{2}-r\mathfrak{m}(\{1\})\Big)\mathbbm{1}\_{\{Y\,=\,1\}} |  |

is an increasing profit with value process

|  |  |  |
| --- | --- | --- |
|  | Vtθ=|12−r​𝔪​({1})|​∫0te−r​s​dLs𝔰​(1)​(U)=|12−r​𝔪​({1})|​∫0te−r​s​dLs1​(Y),t∈[0,T].V^{\theta}\_{t}=\Big|\frac{1}{2}-r\mathfrak{m}(\{1\})\Big|\,\int\_{0}^{t}e^{-rs}\,\mathrm{d}L^{\mathfrak{s}(1)}\_{s}(U)=\Big|\frac{1}{2}-r\mathfrak{m}(\{1\})\Big|\,\int\_{0}^{t}e^{-rs}\,\mathrm{d}L^{1}\_{s}(Y),\quad t\in[0,T]. |  |

Notice that L1​(Y)=L𝔮​(𝔰​(1))​(𝔮​(U))=L𝔰​(1)​(U)L^{1}(Y)=L^{\mathfrak{q}(\mathfrak{s}(1))}(\mathfrak{q}(U))=L^{\mathfrak{s}(1)}(U)
due to 𝔮+′​(𝔰​(1))=1\mathfrak{q}^{\prime}\_{+}(\mathfrak{s}(1))=1 and [[26](https://arxiv.org/html/2512.07555v1#bib.bib26), Exercise VI.1.23] together with Lemma [2.2](https://arxiv.org/html/2512.07555v1#S2.Thmtheorem2 "Lemma 2.2. ‣ 2.1. The Financial Market ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")
(the latter justifies the application of [[26](https://arxiv.org/html/2512.07555v1#bib.bib26), Exercise VI.1.23]). The structure of θ\theta explains that increasing profit can only be made on the set {t∈[0,T]:Yt=1}\{t\in[0,T]\colon Y\_{t}=1\}. Namely, depending on the sign of 12−r​𝔪​({1})\frac{1}{2}-r\mathfrak{m}(\{1\}), buying or selling while YY is in its reflecting state 11 yields an increasing profit. This observation is also reflected by the fact that, whenever HH is an arbitrary increasing profit, the value process of HH is given by

|  |  |  |
| --- | --- | --- |
|  | VtH=∫0tHs​e−r​s​(12−r​𝔪​({1}))​dLs1​(Y),t∈[0,T]V^{H}\_{t}=\int\_{0}^{t}H\_{s}e^{-rs}\Big(\frac{1}{2}-r\mathfrak{m}(\{1\})\Big)\,\mathrm{d}L^{1}\_{s}(Y),\quad t\in[0,T] |  |

(cf. Proposition [3.2](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")).
Let us discuss more intuitions behind this observation.
As will be shown in a forthcoming paper [[9](https://arxiv.org/html/2512.07555v1#bib.bib9)],
the dynamics of YY can be described via an SDE with constraints, namely

|  |  |  |  |
| --- | --- | --- | --- |
| (5.1) |  | d​Yt=Yt​𝟙{Yt≠1}​(μ​d​t+σ​d​Wt)+12​d​Lt1​(Y),𝟙{Yt=1}​d​t=𝔪​({1})​d​Lt1​(Y).\displaystyle\mathrm{d}Y\_{t}=Y\_{t}\mathbbm{1}\_{\{Y\_{t}\neq 1\}}\Big(\mu\,\mathrm{d}t+\sigma\,\mathrm{d}W\_{t}\Big)+\frac{1}{2}\,\mathrm{d}L^{1}\_{t}(Y),\quad\mathbbm{1}\_{\{Y\_{t}=1\}}\,\mathrm{d}t=\mathfrak{m}(\{1\})\,\mathrm{d}L^{1}\_{t}(Y). |  |

By the integration by parts formula and the side constraint,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St\displaystyle\mathrm{d}S\_{t} | =e−r​t​Yt​𝟙{Yt≠1}​(μ​d​t+σ​d​Wt)+12​e−r​t​d​Lt1​(Y)−r​e−r​t​Yt​d​t\displaystyle=e^{-rt}Y\_{t}\mathbbm{1}\_{\{Y\_{t}\neq 1\}}\Big(\mu\,\mathrm{d}t+\sigma\,\mathrm{d}W\_{t}\Big)+\frac{1}{2}\,e^{-rt}\,\mathrm{d}L^{1}\_{t}(Y)-re^{-rt}Y\_{t}\,\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =e−r​t​Yt​𝟙{Yt≠1}​((μ−r)​d​t+σ​d​Wt)+e−r​t​(12−r​𝔪​({1}))​d​Lt1​(Y).\displaystyle=e^{-rt}Y\_{t}\mathbbm{1}\_{\{Y\_{t}\neq 1\}}\Big((\mu-r)\,\mathrm{d}t+\sigma\,\mathrm{d}W\_{t}\Big)+e^{-rt}\,\Big(\frac{1}{2}-r\mathfrak{m}(\{1\})\Big)\,\mathrm{d}L^{1}\_{t}(Y). |  |

The first term provides another reasoning for our observation that any increasing profit must be supported on {t∈[0,T]:Yt=1}\{t\in[0,T]\colon Y\_{t}=1\}, as otherwise the martingale part gets activated, while the second term explains the condition r​𝔪​({1})≠1/2r\mathfrak{m}(\{1\})\neq 1/2, as otherwise SS is constant on the set {t∈[0,T]:Yt=1}\{t\in[0,T]\colon Y\_{t}=1\}.
Notice also that in case r​𝔪​({1})=1/2r\mathfrak{m}(\{1\})=1/2 the local time effects from skewness and stickiness cancel each other, and that then no increasing profit exists.

In the previous example, there was a boundary point bb with 𝔮±′​(𝔰​(b))≠0\mathfrak{q}^{\prime}\_{\pm}(\mathfrak{s}(b))\neq 0, leading to a local time term in the drift.
The following example illustrates that this term might also be inactive, initiating increasing profits solely through the stickiness at the reflecting boundary.

###### Example 5.3 (Shifted generalized square Bessel process of dimension δ∈(0,2)\delta\in(0,2)).

We consider a shifted generalization of the square Bessel process of low dimension δ∈(0,2)\delta\in(0,2) that features sticky reflection, while the classical square Bessel process only allows for instantaneous reflection.
We define YY with state space J=[1,∞)J=[1,\infty) through scale and speed given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔰​(x)\displaystyle\mathfrak{s}(x) | =(x−1)1−δ/2,x∈[1,∞),\displaystyle=(x-1)^{1-\delta/2},\ x\in[1,\infty), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔪​(d​x)\displaystyle\mathfrak{m}(\mathrm{d}x) | =(x−1)δ/2−14​(1−δ2)​d​x​ on ​ℬ​((1,∞)),𝔪​({1})∈[0,∞).\displaystyle=\frac{(x-1)^{\delta/2-1}}{4(1-\frac{\delta}{2})}\,\mathrm{d}x\text{ on }\mathcal{B}((1,\infty)),\quad\mathfrak{m}(\{1\})\in[0,\infty). |  |

In this case, the inverse scale function is given by

|  |  |  |
| --- | --- | --- |
|  | 𝔮​(x)=x1/(1−δ/2)+1,x∈𝔰​([1,∞))=ℝ+.\displaystyle\mathfrak{q}(x)=x^{1/(1-\delta/2)}+1,\quad x\in\mathfrak{s}([1,\infty))=\mathbb{R}\_{+}. |  |

Using 1/(1−δ/2)>11/(1-\delta/2)>1, it follows that 𝔮+′​(𝔰​(1))=𝔮+′​(0)=0\mathfrak{q}^{\prime}\_{+}(\mathfrak{s}(1))=\mathfrak{q}^{\prime}\_{+}(0)=0, and the auxiliary signed measure ν\nu is given by the formula

|  |  |  |
| --- | --- | --- |
|  | ν​(d​x)=−r​𝔪​({1})​δ0​(d​x).\nu(\mathrm{d}x)=-r\mathfrak{m}(\{1\})\,\delta\_{0}(\mathrm{d}x). |  |

As a consequence,

|  |  |  |
| --- | --- | --- |
|  | NIP holds⟺r​𝔪​({1})=0.\text{NIP holds}\quad\Longleftrightarrow\quad r\mathfrak{m}(\{1\})=0. |  |

In the case r​𝔪​({1})≠0r\mathfrak{m}(\{1\})\neq 0, we may take

|  |  |  |
| --- | --- | --- |
|  | θ=−sgn⁡(r​𝔪​({1}))​𝟙{Y= 1},\theta=-\operatorname{sgn}(r\mathfrak{m}(\{1\}))\mathbbm{1}\_{\{Y\,=\,1\}}, |  |

explaining that investing while YY is in the reflecting boundary leads to an increasing profit.
To provide some heuristic intuition, in contrast to the previous example, 𝔮+′​(0)=0\mathfrak{q}^{\prime}\_{+}(0)=0 deactivates the local time term in the dynamics that accounts for reflection (relating this to the previous example, this corresponds to the term d​Lt1​(Y)/2\mathrm{d}L^{1}\_{t}(Y)/2 in ([5.1](https://arxiv.org/html/2512.07555v1#S5.E1 "In Example 5.2 (Black–Scholes model with reflection). ‣ 5. Examples ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"))). Still, a local time term arises through stickiness (as in the previous example, this corresponds to the second equation in ([5.1](https://arxiv.org/html/2512.07555v1#S5.E1 "In Example 5.2 (Black–Scholes model with reflection). ‣ 5. Examples ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"))).222To stress even more the difference from the previous example, we notice that, in the present example, there is no increasing profit in the instantaneously reflecting case 𝔪​({1})=0\mathfrak{m}(\{1\})=0.
In the end, we have

|  |  |  |
| --- | --- | --- |
|  | 𝟙{Yt= 1}​d​St=e−r​t​(−r​𝔪​({1}))​d​Lt0​(U),\mathbbm{1}\_{\{Y\_{t}\,=\,1\}}\,\mathrm{d}S\_{t}=e^{-rt}(-r\mathfrak{m}(\{1\}))\,\mathrm{d}L^{0}\_{t}(U), |  |

which is either increasing or decreasing, and non-constant if r​𝔪​({1})≠0r\mathfrak{m}(\{1\})\neq 0.

Next, we discuss the influence of the second term from ν\nu.
Recall that Nsi∈ℬ​(𝔰​(J∘))N\_{\operatorname{si}}\in\mathcal{B}(\mathfrak{s}(J^{\circ})) denotes a Lebesgue-null set such that
ν​(A∩Nsi)=νsi​(A)\nu(A\cap N\_{\operatorname{si}})=\nu\_{\operatorname{si}}(A) for all A∈ℬ​(𝔰​(J∘))A\in\mathcal{B}(\mathfrak{s}(J^{\circ})).
First consider the case where NsiN\_{\operatorname{si}} consists of one point, say a∈𝔰​(J∘)a\in\mathfrak{s}(J^{\circ}).
Again, the singular parts 𝔮si′′​(d​x)\mathfrak{q}^{\prime\prime}\_{\operatorname{si}}(\mathrm{d}x) and 𝔪siU​(d​x)\mathfrak{m}^{U}\_{\operatorname{si}}(\mathrm{d}x) account for local time terms that occur in the drift of SS.
In the case of 𝔪siU​(d​x)\mathfrak{m}^{U}\_{\operatorname{si}}(\mathrm{d}x) these come from sticky behavior of YY at the point 𝔮​(a)\mathfrak{q}(a), precisely as this was the case with reflecting boundaries. For 𝔮si′′​(d​x)\mathfrak{q}^{\prime\prime}\_{\operatorname{si}}(\mathrm{d}x) the situation is different, and the local time terms arise from the desire of the process YY to leave the point 𝔮​(a)\mathfrak{q}(a) in a preferred direction.
The following two examples illustrate these phenomena.

###### Example 5.4 (Bachelier model with stickiness).

We consider an extension of the classical Bachelier model,
where the price of the risky asset is a Brownian motion with a sticky point ξ∈ℝ\xi\in\mathbb{R}, i.e., the general diffusion on ℝ\operatorname{\mathbb{R}} with scale and speed defined by

|  |  |  |  |
| --- | --- | --- | --- |
| (5.2) |  | 𝔰​(x)=x,𝔪​(d​x)=d​x+ρ​δξ​(d​x),\mathfrak{s}(x)=x,\quad\mathfrak{m}(\mathrm{d}x)=\,\mathrm{d}x+\rho\,\delta\_{\xi}(\mathrm{d}x), |  |

where ρ≥0\rho\geq 0 is the so-called stickiness parameter.
To give some intuition on this process, the amount of time the process spends at ξ\xi is governed by the relation

|  |  |  |  |
| --- | --- | --- | --- |
| (5.3) |  | ∫0t𝟙{Ys=ξ}​ds=ρ​Ltξ​(Y),for all ​t≥0,\int\_{0}^{t}{\mathbbm{1}}\_{\{Y\_{s}=\xi\}}\,\mathrm{d}s=\rho L^{\xi}\_{t}(Y),\quad\text{for all }t\geq 0, |  |

and, in the case ρ>0\rho>0, is of positive Lebesgue measure, as soon as the threshold ξ\xi is reached.

Then, the auxiliary measure is given by

|  |  |  |
| --- | --- | --- |
|  | ν​(d​x)=−r​ξ​ρ​δξ​(d​x),\nu(\mathrm{d}x)=-r\xi\rho\,\delta\_{\xi}(\mathrm{d}x), |  |

and Theorem [3.3](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") shows that

|  |  |  |
| --- | --- | --- |
|  | NIP holds⟺r​ξ​ρ=0.\text{NIP holds}\quad\Longleftrightarrow\quad r\xi\rho=0. |  |

In the case r​ξ​ρ≠0r\xi\rho\neq 0, the canonical increasing profit is given by
θ=−sgn⁡(r​ξ)​𝟙{Yt=ξ}\theta=-\operatorname{sgn}(r\xi)\mathbbm{1}\_{\{Y\_{t}\,=\,\xi\}},
and its value process reads

|  |  |  |
| --- | --- | --- |
|  | Vtθ=∫0t|r​ξ|​ρ​e−r​s​dLsξ​(Y),t∈[0,T].V^{\theta}\_{t}=\int\_{0}^{t}|r\xi|\rho e^{-rs}\,\mathrm{d}L^{\xi}\_{s}(Y),\quad t\in[0,T]. |  |

Similarly, by Proposition [3.2](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), whenever HH is an increasing profit, its value process is given by

|  |  |  |
| --- | --- | --- |
|  | VtH=−∫0tHs​r​ξ​ρ​e−r​s​dLsξ​(Y),t∈[0,T].V^{H}\_{t}=-\int\_{0}^{t}H\_{s}r\xi\rho e^{-rs}\,\mathrm{d}L^{\xi}\_{s}(Y),\quad t\in[0,T]. |  |

We notice that increasing profits can only be made in the sticky point.
To give some intuition on this example, we recall that YY solves the SDE system involving the local time (see [[10](https://arxiv.org/html/2512.07555v1#bib.bib10)]):

|  |  |  |  |
| --- | --- | --- | --- |
| (5.4) |  | d​Yt=𝟙{Yt≠ξ}​d​Bt,𝟙{Yt=ξ}​d​t=ρ​d​Ltξ​(Y),\,\mathrm{d}Y\_{t}={\mathbbm{1}}\_{\{Y\_{t}\not=\xi\}}\,\mathrm{d}B\_{t},\quad{\mathbbm{1}}\_{\{Y\_{t}=\xi\}}\,\mathrm{d}t=\rho\,\mathrm{d}L^{\xi}\_{t}(Y), |  |

where BB is a Brownian motion.
Integration by parts yields that the discounted price process SS follows the dynamic

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (5.5) |  | d​St\displaystyle\,\mathrm{d}S\_{t} | =d​(e−r​t​Yt)=𝟙{Yt≠ξ}​(−r​St​d​t+e−r​t​d​Bt)−r​ξ​ρ​e−r​t​d​Ltξ​(Y).\displaystyle=\,\mathrm{d}(e^{-rt}Y\_{t})={\mathbbm{1}}\_{\{Y\_{t}\not=\xi\}}\left(-rS\_{t}\,\mathrm{d}t+e^{-rt}\,\mathrm{d}B\_{t}\right)-r\xi\rho e^{-rt}\,\mathrm{d}L^{\xi}\_{t}(Y). |  |

Therefore, SS has a local time drift which, for the same reason as in Examples [5.2](https://arxiv.org/html/2512.07555v1#S5.Thmtheorem2 "Example 5.2 (Black–Scholes model with reflection). ‣ 5. Examples ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") and [5.3](https://arxiv.org/html/2512.07555v1#S5.Thmtheorem3 "Example 5.3 (Shifted generalized square Bessel process of dimension 𝛿∈(0,2)). ‣ 5. Examples ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"),
initiates an increasing profit.

###### Example 5.5 (Bachelier model with skewness).

We take a look at the Bachelier model with skewness, as considered in [[28](https://arxiv.org/html/2512.07555v1#bib.bib28)]. In other words, we suppose that YY is a Brownian motion with skewness at zero, i.e., the state space is given by J=ℝJ=\mathbb{R} and scale and speed are defined through

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔰​(x)\displaystyle\mathfrak{s}(x) | ={(1−κ)​x,x≥0,κ​x,x<0,\displaystyle=\begin{cases}(1-\kappa)x,&x\geq 0,\\ \kappa x,&x<0,\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔪​(d​x)\displaystyle\mathfrak{m}(\mathrm{d}x) | =(1−κ)−1​𝟙{x≥0}​d​x+κ−1​𝟙{x<0}​d​x,\displaystyle=(1-\kappa)^{-1}\mathbbm{1}\_{\{x\geq 0\}}\,\mathrm{d}x+\kappa^{-1}\mathbbm{1}\_{\{x<0\}}\,\mathrm{d}x, |  |

where κ∈(0,1)∖{1/2}\kappa\in(0,1)\setminus\{1/2\} is the so-called skewness parameter. To provide some intuition, if κ<1/2\kappa<1/2 (resp., κ>1/2\kappa>1/2), then the process YY has the tendency to leave the origin downwards (resp., upwards).
We notice that 𝔮′>0\mathfrak{q}^{\prime}>0 λ\{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}-a.e.
and 𝔮si′′​(d​x)=(2​κ−1)/(κ​(1−κ))​δ0​(d​x)\mathfrak{q}^{\prime\prime}\_{\operatorname{si}}(\mathrm{d}x)=(2\kappa-1)/(\kappa(1-\kappa))\,\delta\_{0}(\mathrm{d}x). Consequently,

|  |  |  |
| --- | --- | --- |
|  | ν​(d​x)=2​κ−12​κ​(1−κ)​δ0​(d​x),\nu(\mathrm{d}x)=\frac{2\kappa-1}{2\kappa(1-\kappa)}\,\delta\_{0}(\mathrm{d}x), |  |

and Theorem [3.3](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") shows that
θ=sgn⁡(2​κ−1)​𝟙{Y=0}\theta=\operatorname{sgn}(2\kappa-1)\mathbbm{1}\_{\{Y=0\}}
is an increasing profit, independently of the interest rate. The value process of θ\theta is given by

|  |  |  |
| --- | --- | --- |
|  | Vtθ=∫0t|2​κ−1|2​κ​(1−κ)​e−r​s​dLs0​(U)=∫0t|1−12​κ|​e−r​s​dLs0​(Y),t∈[0,T],V^{\theta}\_{t}=\int\_{0}^{t}\frac{|2\kappa-1|}{2\kappa(1-\kappa)}e^{-rs}\,\mathrm{d}L^{0}\_{s}(U)=\int\_{0}^{t}\Big|1-\frac{1}{2\kappa}\Big|e^{-rs}\,\mathrm{d}L^{0}\_{s}(Y),\quad t\in[0,T], |  |

where we use [[26](https://arxiv.org/html/2512.07555v1#bib.bib26), Exercise VI.1.23] for the last identity.
Similarly, whenever HH is an increasing profit, its value process reads

|  |  |  |
| --- | --- | --- |
|  | VtH=∫0t(1−12​κ)​Hs​e−r​s​dLs0​(Y),t∈[0,T].V^{H}\_{t}=\int\_{0}^{t}\Big(1-\frac{1}{2\kappa}\Big)H\_{s}e^{-rs}\,\mathrm{d}L^{0}\_{s}(Y),\quad t\in[0,T]. |  |

We notice that increasing profits can only be made in the skew point.
To provide some intuition for the origin of increasing profits, recall from [[26](https://arxiv.org/html/2512.07555v1#bib.bib26), Exercise X.2.30] that the process YY has an SDE representation of the form

|  |  |  |
| --- | --- | --- |
|  | d​Yt=d​Wt+(1−12​κ)​d​Lt0​(Y).\mathrm{d}Y\_{t}=\mathrm{d}W\_{t}+\Big(1-\frac{1}{2\kappa}\Big)\,\mathrm{d}L^{0}\_{t}(Y). |  |

This formula explains that YY has a local time drift, which stems from the fact that 𝔮si′′​({0})≠0\mathfrak{q}^{\prime\prime}\_{\operatorname{si}}(\{0\})\neq 0. For the same reason as in the Examples [5.2](https://arxiv.org/html/2512.07555v1#S5.Thmtheorem2 "Example 5.2 (Black–Scholes model with reflection). ‣ 5. Examples ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), [5.3](https://arxiv.org/html/2512.07555v1#S5.Thmtheorem3 "Example 5.3 (Shifted generalized square Bessel process of dimension 𝛿∈(0,2)). ‣ 5. Examples ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") and [5.4](https://arxiv.org/html/2512.07555v1#S5.Thmtheorem4 "Example 5.4 (Bachelier model with stickiness). ‣ 5. Examples ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), this drift initiates an increasing profit.

In general, the phenomena that stem from the second term from ν\nu are richer than the one described in the previous example.
But, in any case, the corresponding increasing profits are made on the set
{t∈[0,T]:Ut∈Nsi}\{t\in[0,T]\colon U\_{t}\in N\_{\operatorname{si}}\}
(cf. ([3.5](https://arxiv.org/html/2512.07555v1#S3.E5 "In 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"))),
where we also recall that Nsi⊂𝔰​(J∘)N\_{\operatorname{si}}\subset\mathfrak{s}(J^{\circ}) is
Lebesgue null.333To provide a specific example where the sets of the form {t∈[0,T]:Ut=a}\{t\in[0,T]\colon U\_{t}=a\} with a∈𝔰​(J∘)a\in\mathfrak{s}(J^{\circ}) do not suffice,
consider r≠0r\neq 0 and a general diffusion YY with J=ℝJ=\mathbb{R} on natural scale (in particular, Y=UY=U)
with the speed measure that does not have atoms but has a nonvanishing singular component 𝔪siU​(d​x)\mathfrak{m}^{U}\_{\operatorname{si}}(\mathrm{d}x) concentrated on the Cantor set.
This is different from the influence of the first term from ν\nu, which appears to be the most curious one and is discussed in the next example.

###### Example 5.6 (Increasing profits made on a set of positive Lebesgue measure).

We start by constructing a scale function on J=ℝJ=\mathbb{R}, following an idea from [[8](https://arxiv.org/html/2512.07555v1#bib.bib8), Lemma 2.1].
Take a closed set F⊂[0,1]F\subset[0,1] with empty interior such that λ\(F)>0{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}(F)>0.
This could be a *fat* Cantor set or, alternatively, one could construct such a set as follows (cf. [[3](https://arxiv.org/html/2512.07555v1#bib.bib3), Example 1.7.6]).
Let {qn:n∈ℕ}\{q\_{n}\colon n\in\mathbb{N}\} be an enumeration of all rational points in [0,1][0,1].
Take a∈(0,1)a\in(0,1) and a positive sequence {rn:n∈ℕ}\{r\_{n}\colon n\in\mathbb{N}\} such that
∑n=1∞2​rn≤a\sum\_{n=1}^{\infty}2r\_{n}\leq a.
It is easy to verify that
F≜[0,1]∖GF\triangleq[0,1]\setminus G,
where G≜⋃n∈ℕ(qn−rn,qn+rn)G\triangleq\bigcup\_{n\in\mathbb{N}}(q\_{n}-r\_{n},q\_{n}+r\_{n}),
satisfies the requirements.
Now, we set

|  |  |  |
| --- | --- | --- |
|  | 𝔮​(x)≜∫0xdF​(z)​dz,x∈ℝ,dF​(z)≜infy∈F|z−y|.\mathfrak{q}(x)\triangleq\int\_{0}^{x}d\_{F}(z)\,\mathrm{d}z,\quad x\in\mathbb{R},\quad d\_{F}(z)\triangleq\inf\_{y\in F}|z-y|. |  |

Notice that 𝔮\mathfrak{q} is a C1C^{1}-function on ℝ\mathbb{R} with

|  |  |  |  |
| --- | --- | --- | --- |
| (5.6) |  | {x∈ℝ:𝔮′​(x)=0}=F\{x\in\mathbb{R}\colon\mathfrak{q}^{\prime}(x)=0\}=F |  |

(because z↦dF​(z)z\mapsto d\_{F}(z) is continuous and FF is closed) and
𝔮\mathfrak{q} is strictly increasing (because FF is closed and does not contain any open interval).
Let UU be a Brownian motion and define Y≜𝔮​(U)Y\triangleq\mathfrak{q}(U),
which is a general diffusion
with state space 𝔮​(ℝ)=ℝ\mathfrak{q}(\mathbb{R})=\mathbb{R}, scale function 𝔰≜𝔮−1\mathfrak{s}\triangleq\mathfrak{q}^{-1} and speed measure λ\∘𝔮−1{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}\circ\mathfrak{q}^{-1}.
Furthermore, as 𝔮′=dF​(⋅)\mathfrak{q}^{\prime}=d\_{F}(\cdot) is Lipschitz continuous on ℝ\mathbb{R},
hence absolutely continuous (in particular, 𝔮si′′​(d​x)≡0\mathfrak{q}^{\prime\prime}\_{\operatorname{si}}(\mathrm{d}x)\equiv 0),
then 𝔮′\mathfrak{q}^{\prime} is of locally finite variation, showing that 𝔮\mathfrak{q} is a difference of two convex functions on ℝ\mathbb{R}.
This explains that Standing Assumption [2.1](https://arxiv.org/html/2512.07555v1#S2.Thmtheorem1 "Standing Assumption 2.1. ‣ 2.1. The Financial Market ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") is satisfied.
As 𝔪U=λ\\mathfrak{m}^{U}={\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}, we also have 𝔪siU​(d​x)≡0\mathfrak{m}^{U}\_{\operatorname{si}}(\mathrm{d}x)\equiv 0, hence

|  |  |  |
| --- | --- | --- |
|  | ν​(d​x)=−r​𝔮​(x)​𝟙F​(x)​d​x.\nu(\mathrm{d}x)=-r\mathfrak{q}(x)\mathbbm{1}\_{F}(x)\,\mathrm{d}x. |  |

By Theorem [3.3](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"),

|  |  |  |
| --- | --- | --- |
|  | NIP holds⟺r=0.\text{NIP holds}\quad\Longleftrightarrow\quad r=0. |  |

In the case r≠0r\neq 0, we may take
θ=−sgn⁡(r)​𝟙F​(U),\theta=-\operatorname{sgn}(r)\mathbbm{1}\_{F}(U),
which is an increasing profit with the value process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vtθ\displaystyle V^{\theta}\_{t} | =∫0t|r|​e−r​s​∫F𝔮​(x)​dLtx​(U)​dx\displaystyle=\int\_{0}^{t}|r|e^{-rs}\int\_{F}\mathfrak{q}(x)\,\mathrm{d}L^{x}\_{t}(U)\,\mathrm{d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0t|r|​e−r​s​𝔮​(Us)​𝟙F​(Us)​d​⟨U⟩s\displaystyle=\int\_{0}^{t}|r|e^{-rs}\mathfrak{q}(U\_{s})\mathbbm{1}\_{F}(U\_{s})\,\mathrm{d}\langle U\rangle\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0t|r|​e−r​s​Ys​𝟙F​(Us)​d​⟨U⟩s,t∈[0,T].\displaystyle=\int\_{0}^{t}|r|e^{-rs}Y\_{s}\mathbbm{1}\_{F}(U\_{s})\,\mathrm{d}\langle U\rangle\_{s},\quad t\in[0,T]. |  |

In contrast to the previous examples, increasing profits are not made while YY attains a discrete set of points, but while UU is in the uncountable set FF with positive Lebesgue measure. Another crucial difference is that in this setting the value processes of increasing profits are not integrals w.r.t. a local time process,
but w.r.t. the quadratic variation process ⟨U⟩\langle U\rangle.

## 6. On the Relation of Increasing Profits and the Representation Property

Example [5.6](https://arxiv.org/html/2512.07555v1#S5.Thmtheorem6 "Example 5.6 (Increasing profits made on a set of positive Lebesgue measure). ‣ 5. Examples ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") illustrated a very peculiar form of increasing profits whose value processes are integrals w.r.t. the quadratic variation measure d​⟨U⟩\mathrm{d}\langle U\rangle. As we will encounter in this section, for a variety of general diffusion models, the existence of such increasing profits is intrinsically connected to the failure of the so-called representation property (RP),
which is of fundamental importance both in the context of market completeness (see, e.g., [[29](https://arxiv.org/html/2512.07555v1#bib.bib29), Section VII.2.d]) and from the viewpoint of the general theory of stochastic processes (see, e.g., [[18](https://arxiv.org/html/2512.07555v1#bib.bib18), Sections III.4.c-d]).

To study this connection formally, we define (ℱtS)t∈[0,T](\mathcal{F}^{S}\_{t})\_{t\in[0,T]} to be the right-continuous natural filtration of SS, that is, ℱtS≜⋂s∈(t,T]σ​(Sr,r≤s)\mathcal{F}^{S}\_{t}\triangleq\bigcap\_{s\in(t,T]}\sigma(S\_{r},r\leq s), for all t∈[0,T)t\in[0,T), and ℱTS≜σ​(Sr,r≤T)\mathcal{F}^{S}\_{T}\triangleq\sigma(S\_{r},r\leq T).
Recall from Stricker’s lemma ([[17](https://arxiv.org/html/2512.07555v1#bib.bib17), Theorem 9.19]) that SS is not only an (ℱt)t∈[0,T](\mathcal{F}\_{t})\_{t\in[0,T]}-semimartingale, but also an (ℱtS)t∈[0,T](\mathcal{F}^{S}\_{t})\_{t\in[0,T]}-semimartingale.

###### Definition 6.1 (Representation property).

We say that the representation property (RP) holds for the semimartingale SS if every (ℱtS)t∈[0,T](\mathcal{F}^{S}\_{t})\_{t\in[0,T]}-local martingale M=(Mt)t∈[0,T]M=(M\_{t})\_{t\in[0,T]} has a representation

|  |  |  |
| --- | --- | --- |
|  | M=M0+∫0⋅Hs​dSsc,M=M\_{0}+\int\_{0}^{\cdot}H\_{s}\,\mathrm{d}S^{c}\_{s}, |  |

where HH is an (ℱtS)t∈[0,T](\mathcal{F}^{S}\_{t})\_{t\in[0,T]}-predictable process such that a.s. ∫0THs2​d​⟨S⟩s<∞\int\_{0}^{T}H^{2}\_{s}\,\mathrm{d}\langle S\rangle\_{s}<\infty and ScS^{c} is the continuous (ℱtS)t∈[0,T](\mathcal{F}^{S}\_{t})\_{t\in[0,T]}-local martingale part of SS.

Using the main result from [[8](https://arxiv.org/html/2512.07555v1#bib.bib8)], in our general diffusion framework, the RP can be described in terms of the inverse scale function 𝔮\mathfrak{q}.
We recall that {𝔮′=0}\{\mathfrak{q}^{\prime}=0\} denotes an arbitrary Borel subset of 𝔰​(J∘)\mathfrak{s}(J^{\circ})
that differs from the set
{x∈𝔰​(J∘):𝔮+′​(x)=0}\{x\in\mathfrak{s}(J^{\circ}):\mathfrak{q}^{\prime}\_{+}(x)=0\}
(abbreviated as {𝔮+′=0}\{\mathfrak{q}^{\prime}\_{+}=0\})
on a Lebesgue-null set;
cf. Remark [3.1](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem1 "Remark 3.1. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates").

###### Lemma 6.2.

The RP holds for the semimartingale SS if and only if λ\(𝔮′=0)=0{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}(\mathfrak{q}^{\prime}=0)=0.

###### Proof.

Clearly, the right-continuous natural filtration
(ℱtS)t∈[0,T](\mathcal{F}^{S}\_{t})\_{t\in[0,T]}
of SS coincides with
the right-continuous natural filtration
(ℱtY)t∈[0,T](\mathcal{F}^{Y}\_{t})\_{t\in[0,T]} of YY.
Using that

|  |  |  |
| --- | --- | --- |
|  | d​St=e−r​t​d​Yt−r​St​d​t,\mathrm{d}S\_{t}=e^{-rt}\,\mathrm{d}Y\_{t}-rS\_{t}\,\mathrm{d}t, |  |

we observe that the continuous (ℱtS)t∈[0,T](\mathcal{F}^{S}\_{t})\_{t\in[0,T]}-local martingale part of SS is given by d​Stc=e−r​t​d​Ytc\mathrm{d}S^{c}\_{t}=e^{-rt}\,\mathrm{d}Y^{c}\_{t}, where YcY^{c} is the continuous (ℱtY)t∈[0,T](\mathcal{F}^{Y}\_{t})\_{t\in[0,T]}-local martingale part of YY.

Consequently, the RP holds for SS if and only if it holds for YY. As the RP for YY is equivalent to λ\(𝔮′=0)=0{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}(\mathfrak{q}^{\prime}=0)=0 by [[8](https://arxiv.org/html/2512.07555v1#bib.bib8), Theorem 2.1], the claim follows.
∎

By virtue of formula ([3.1](https://arxiv.org/html/2512.07555v1#S3.E1 "In 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) for the signed measure ν\nu,
the condition λ\(𝔮′=0)>0{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}(\mathfrak{q}^{\prime}=0)>0, characterizing
the failure of the RP for SS,
is closely related to the existence of certain increasing profits, like the one illustrated by Example [5.6](https://arxiv.org/html/2512.07555v1#S5.Thmtheorem6 "Example 5.6 (Increasing profits made on a set of positive Lebesgue measure). ‣ 5. Examples ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates").
We now describe this relation precisely.

###### Definition 6.3.

We call an increasing profit H∈𝖨𝖯H\in\mathsf{IP} a quadratic variation increasing profit (QVIP) if a.s. d​VH≪d​⟨U⟩\mathrm{d}V^{H}\ll\mathrm{d}\langle U\rangle.
We denote

|  |  |  |
| --- | --- | --- |
|  | 𝖰𝖵𝖨𝖯≜{H∈L​(S):H​ is a QVIP}.\mathsf{QVIP}\triangleq\big\{H\in L(S)\colon H\text{ is a QVIP}\big\}. |  |

It is instructive to relate this definition to Lemma [2.6](https://arxiv.org/html/2512.07555v1#S2.Thmtheorem6 "Lemma 2.6. ‣ 2.2. Increasing Profits ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), which entails that the value processes of increasing profits cannot be dominated by the quadratic variation measure d​⟨S⟩\mathrm{d}\langle S\rangle. As we have seen in Example [5.6](https://arxiv.org/html/2512.07555v1#S5.Thmtheorem6 "Example 5.6 (Increasing profits made on a set of positive Lebesgue measure). ‣ 5. Examples ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), this is not the case for d​⟨U⟩\mathrm{d}\langle U\rangle and QVIPs may exist.

Recall that ν|𝔰​(J∘)=νac+νsi\nu|\_{\mathfrak{s}(J^{\circ})}=\nu\_{\textup{ac}}+\nu\_{\textup{si}} denotes the Lebesgue decomposition of ν|𝔰​(J∘)\nu|\_{\mathfrak{s}(J^{\circ})} w.r.t. the Lebesgue measure and that Nsi∈ℬ​(𝔰​(J∘))N\_{\operatorname{si}}\in\mathcal{B}(\mathfrak{s}(J^{\circ})) is a Lebesgue-null set such that ν​(A∩Nsi)=νsi​(A)\nu(A\cap N\_{\operatorname{si}})=\nu\_{\textup{si}}(A) for all A∈ℬ​(𝔰​(J∘))A\in\mathcal{B}(\mathfrak{s}(J^{\circ})).

The existence of a QVIP can be characterized in the spirit of Theorem [3.3](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates").
We define the strategy

|  |  |  |
| --- | --- | --- |
|  | θ¯≜𝟙(N+∩{𝔮+′=0})∖Nsi​(U)−𝟙(N−∩{𝔮+′=0})∖Nsi​(U),\bar{\theta}\triangleq\mathbbm{1}\_{(N\_{+}\,\cap\,\{\mathfrak{q}^{\prime}\_{+}=0\})\,\setminus\,N\_{\operatorname{si}}}(U)-\mathbbm{1}\_{(N\_{-}\,\cap\,\{\mathfrak{q}^{\prime}\_{+}=0\})\,\setminus\,N\_{\operatorname{si}}}(U), |  |

which takes over the role of θ\theta in Theorem [3.3](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates").

###### Lemma 6.4.

The following are equivalent:

1. (i)

   A QVIP exists.
2. (ii)

   There exists a G∈ℬ​(𝔰​(J∘))G\in\mathcal{B}(\mathfrak{s}(J^{\circ})) such that |νac|​(G)>0|\nu\_{\operatorname{ac}}|(G)>0.
3. (iii)

   θ¯∈𝖨𝖯\bar{\theta}\in\mathsf{IP}.
4. (iv)

   θ¯∈𝖰𝖵𝖨𝖯\bar{\theta}\in\mathsf{QVIP}.

In particular, 𝖰𝖵𝖨𝖯=∅\mathsf{QVIP}=\emptyset is equivalent to |νac|≡0|\nu\_{\operatorname{ac}}|\equiv 0.

It is worth recalling that |νac|≡0|\nu\_{\operatorname{ac}}|\equiv 0 is equivalent to νac≡0\nu\_{\operatorname{ac}}\equiv 0 (cf. the paragraph after Theorem [3.3](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")).

###### Proof.

In the proof we use the notation Nsic≜𝔰​(J∘)∖NsiN^{c}\_{\operatorname{si}}\triangleq\mathfrak{s}(J^{\circ})\setminus N\_{\operatorname{si}}.

The implication (iv) ⟹\implies (i) is trivial.
Let us show that (i) ⟹\implies (ii).
Assume that H∈𝖨𝖯H\in\mathsf{IP} satisfies d​VtH≪d​⟨U⟩t\mathrm{d}V^{H}\_{t}\ll\mathrm{d}\langle U\rangle\_{t}.
By the semimartingale occupation time formula, ⟨U⟩t=∫Ltx​(U)​dx\langle U\rangle\_{t}=\int L\_{t}^{x}(U)\,\mathrm{d}x, that is,
d​VtH≪∫dLtx​(U)​dx\mathrm{d}V^{H}\_{t}\ll\int\mathrm{d}L^{x}\_{t}(U)\,\mathrm{d}x.
As 𝔰​(J∖J∘)∪Nsi\mathfrak{s}(J\setminus J^{\circ})\cup N\_{\operatorname{si}} is a Lebesgue-null set,
then, by Proposition [3.2](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"),
we obtain that

|  |  |  |
| --- | --- | --- |
|  | VH=∫0⋅𝟙Nsic​(Us)​dVsH=∫0⋅Hs​e−r​s​∫NsicdLsx​(U)​ν​(d​x)=∫0⋅Hs​e−r​s​∫dLsx​(U)​(𝟙(N+∩{𝔮+′=0})∖Nsi−𝟙(N−∩{𝔮+′=0})∖Nsi)​|ν|​(d​x)=∫0⋅Hs​e−r​s​∫dLsx​(U)​(𝟙(N+∩{𝔮+′=0})∖Nsi−𝟙(N−∩{𝔮+′=0})∖Nsi)​|νac|​(d​x)=∫0⋅θ¯s​Hs​e−r​s​∫dLtx​(U)​|νac|​(d​x).\begin{split}V^{H}&=\int\_{0}^{\cdot}\mathbbm{1}\_{N^{c}\_{\operatorname{si}}}(U\_{s})\,\mathrm{d}V^{H}\_{s}\\ &=\int\_{0}^{\cdot}H\_{s}e^{-rs}\int\_{N^{c}\_{\operatorname{si}}}\,\mathrm{d}L^{x}\_{s}(U)\,\nu(\mathrm{d}x)\\ &=\int\_{0}^{\cdot}H\_{s}e^{-rs}\int\,\mathrm{d}L^{x}\_{s}(U)\,(\mathbbm{1}\_{(N\_{+}\,\cap\,\{\mathfrak{q}^{\prime}\_{+}=0\})\setminus N\_{\operatorname{si}}}-\mathbbm{1}\_{(N\_{-}\,\cap\,\{\mathfrak{q}^{\prime}\_{+}=0\})\setminus N\_{\operatorname{si}}})\,|\nu|(\mathrm{d}x)\\ &=\int\_{0}^{\cdot}H\_{s}e^{-rs}\int\,\mathrm{d}L^{x}\_{s}(U)\,(\mathbbm{1}\_{(N\_{+}\,\cap\,\{\mathfrak{q}^{\prime}\_{+}=0\})\setminus N\_{\operatorname{si}}}-\mathbbm{1}\_{(N\_{-}\,\cap\,\{\mathfrak{q}^{\prime}\_{+}=0\})\setminus N\_{\operatorname{si}}})\,|\nu\_{\operatorname{ac}}|(\mathrm{d}x)\\ &=\int\_{0}^{\cdot}\bar{\theta}\_{s}H\_{s}e^{-rs}\int\mathrm{d}L^{x}\_{t}(U)\,|\nu\_{\operatorname{ac}}|(\mathrm{d}x).\end{split} |  |

As H∈𝖨𝖯H\in\mathsf{IP} implies ℙ​(VTH>0)>0\mathbb{P}(V^{H}\_{T}>0)>0, arguing by contraposition, it follows that |νac||\nu\_{\operatorname{ac}}| cannot be the zero measure, which is equivalent to (ii).

Next, the implication (ii) ⟹\implies (iii) follows directly from Proposition [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"). To be more specific, notice that
θ¯​𝔮+′​(U)=0\bar{\theta}\mathfrak{q}^{\prime}\_{+}(U)=0, θ¯​θ=𝟙{𝔮+′=0}∖Nsi​(U)≥0\bar{\theta}\theta=\mathbbm{1}\_{\{\mathfrak{q}^{\prime}\_{+}=0\}\,\setminus\,N\_{\operatorname{si}}}(U)\geq 0 and >0>0 on {t∈[0,T]:Ut∈{q+′=0}∖Nsi}\{t\in[0,T]\colon U\_{t}\in\{q^{\prime}\_{+}=0\}\,\setminus\,N\_{\operatorname{si}}\}.
As

|  |  |  |
| --- | --- | --- |
|  | G∈ℬ​(𝔰​(J∘)),|νac|​(G)>0⟹|ν|​(G∩{𝔮+′=0}∩Nsic)=|νac|​(G)>0,G\in\mathcal{B}(\mathfrak{s}(J^{\circ})),\,|\nu\_{\operatorname{ac}}|(G)>0\quad\implies\quad|\nu|(G\cap\{\mathfrak{q}^{\prime}\_{+}=0\}\cap N^{c}\_{\operatorname{si}})=|\nu\_{{\operatorname{ac}}}|(G)>0, |  |

we conclude that (i)-(iii) from Proposition [3.5](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem5 "Proposition 3.5. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") hold.

Finally, we prove the implication (iii) ⟹\implies (iv).
If θ¯∈𝖨𝖯\bar{\theta}\in\mathsf{IP}, using Proposition [3.2](https://arxiv.org/html/2512.07555v1#S3.Thmtheorem2 "Proposition 3.2. ‣ 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") and the occupation time formula for semimartingales, we get that

|  |  |  |  |
| --- | --- | --- | --- |
| (6.1) |  | Vθ¯=∫0⋅e−r​s​∫{𝔮+′=0}∩NsicdLsx​(U)​(𝟙N+​(x)−𝟙N−​(x))​ν​(d​x)=∫0⋅e−r​s​∫{𝔮+′=0}∩NsicdLsx​(U)​|ν|​(d​x)=∫0⋅e−r​s​∫{𝔮+′=0}dLsx​(U)​|νac|​(d​x)=∫0⋅e−r​s​∫|r​𝔮​(x)|​𝔪acU​(x)​𝟙{𝔮′=0}​dLsx​(U)​dx=∫0⋅e−r​s​|r​𝔮​(Us)|​𝔪acU​(Us)​𝟙{𝔮′=0}​(Us)​d​⟨U⟩s,\begin{split}V^{\bar{\theta}}&=\int\_{0}^{\cdot}e^{-rs}\int\_{\{\mathfrak{q}^{\prime}\_{+}=0\}\,\cap\,N^{c}\_{\operatorname{si}}}\,\mathrm{d}L^{x}\_{s}(U)\,(\mathbbm{1}\_{N\_{+}}(x)-\mathbbm{1}\_{N\_{-}}(x))\,\nu(\mathrm{d}x)\\ &=\int\_{0}^{\cdot}e^{-rs}\int\_{\{\mathfrak{q}^{\prime}\_{+}=0\}\,\cap\,N^{c}\_{\operatorname{si}}}\,\mathrm{d}L^{x}\_{s}(U)\,|\nu|(\mathrm{d}x)\\ &=\int\_{0}^{\cdot}e^{-rs}\int\_{\{\mathfrak{q}^{\prime}\_{+}=0\}}\,\mathrm{d}L^{x}\_{s}(U)\,|\nu\_{\operatorname{ac}}|(\mathrm{d}x)\\ &=\int\_{0}^{\cdot}e^{-rs}\int|r\mathfrak{q}(x)|\mathfrak{m}^{U}\_{\operatorname{ac}}(x)\mathbbm{1}\_{\{\mathfrak{q}^{\prime}=0\}}\,\mathrm{d}L^{x}\_{s}(U)\,\mathrm{d}x\\ &=\int\_{0}^{\cdot}e^{-rs}|r\mathfrak{q}(U\_{s})|\mathfrak{m}^{U}\_{\operatorname{ac}}(U\_{s})\mathbbm{1}\_{\{\mathfrak{q}^{\prime}=0\}}(U\_{s})\,\mathrm{d}\langle U\rangle\_{s},\end{split} |  |

which is the value process of a QVIP. This means that θ¯\bar{\theta} is a QVIP, i.e., (iv) holds. This concludes the proof.
∎

###### Corollary 6.5.

A QVIP exists if and only if r≠0r\neq 0 and λ\(𝔪acU>0,𝔮′=0)>0{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}(\mathfrak{m}^{U}\_{{\operatorname{ac}}}>0,\mathfrak{q}^{\prime}=0)>0.

The result is a direct consequence of Lemma [6.4](https://arxiv.org/html/2512.07555v1#S6.Thmtheorem4 "Lemma 6.4. ‣ 6. On the Relation of Increasing Profits and the Representation Property ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") and the structure of νac\nu\_{\operatorname{ac}}
(recall ([3.1](https://arxiv.org/html/2512.07555v1#S3.E1 "In 3. The Structure of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) and notice that the factor 𝔮​(x)\mathfrak{q}(x) vanishes at most in one point, hence does not matter).

###### Discussion 6.6.

(a)
Corollary [6.5](https://arxiv.org/html/2512.07555v1#S6.Thmtheorem5 "Corollary 6.5. ‣ 6. On the Relation of Increasing Profits and the Representation Property ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") allows us to relate the failure of the RP for SS to the existence of a QVIP. Namely, if, for example, 𝔪acU>0\mathfrak{m}^{U}\_{\operatorname{ac}}>0 on {𝔮′=0}\{\mathfrak{q}^{\prime}=0\}, then it follows from Corollary [6.5](https://arxiv.org/html/2512.07555v1#S6.Thmtheorem5 "Corollary 6.5. ‣ 6. On the Relation of Increasing Profits and the Representation Property ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") and Lemma [6.2](https://arxiv.org/html/2512.07555v1#S6.Thmtheorem2 "Lemma 6.2. ‣ 6. On the Relation of Increasing Profits and the Representation Property ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") that a QVIP exists if and only if r≠0r\neq 0 and the RP fails.

More precisely, Corollary [6.5](https://arxiv.org/html/2512.07555v1#S6.Thmtheorem5 "Corollary 6.5. ‣ 6. On the Relation of Increasing Profits and the Representation Property ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") and Lemma [6.2](https://arxiv.org/html/2512.07555v1#S6.Thmtheorem2 "Lemma 6.2. ‣ 6. On the Relation of Increasing Profits and the Representation Property ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") show that, if r≠0r\neq 0, the failure of the RP for SS is a necessary condition for the existence of a QVIP. To give an example where it is not sufficient, assume that r≠0r\neq 0, 𝔰​(J)=ℝ\mathfrak{s}(J)=\mathbb{R} and that 𝔪U\mathfrak{m}^{U}
is a discrete measure concentrated
on the set of rational numbers ℚ\mathbb{Q}. Then, 𝔪acU=0\mathfrak{m}^{U}\_{\operatorname{ac}}=0 and no QVIP exists by Corollary [6.5](https://arxiv.org/html/2512.07555v1#S6.Thmtheorem5 "Corollary 6.5. ‣ 6. On the Relation of Increasing Profits and the Representation Property ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), irrespectively of the choice of 𝔮\mathfrak{q}.
However, taking 𝔮\mathfrak{q} as in Example [5.6](https://arxiv.org/html/2512.07555v1#S5.Thmtheorem6 "Example 5.6 (Increasing profits made on a set of positive Lebesgue measure). ‣ 5. Examples ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), the RP for SS fails by Lemma [6.2](https://arxiv.org/html/2512.07555v1#S6.Thmtheorem2 "Lemma 6.2. ‣ 6. On the Relation of Increasing Profits and the Representation Property ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates").

(b)
Corollary [6.5](https://arxiv.org/html/2512.07555v1#S6.Thmtheorem5 "Corollary 6.5. ‣ 6. On the Relation of Increasing Profits and the Representation Property ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates") can be related to Lemma [2.6](https://arxiv.org/html/2512.07555v1#S2.Thmtheorem6 "Lemma 2.6. ‣ 2.2. Increasing Profits ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"). Indeed, by Lemma [4.1](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem1 "Lemma 4.1 ([1, Lemma 3.2]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), a.s. d​⟨S⟩∼d​⟨U⟩\mathrm{d}\langle S\rangle\sim\mathrm{d}\langle U\rangle on {t∈[0,T]:𝔮′​(Ut)>0}\{t\in[0,T]\colon\mathfrak{q}^{\prime}(U\_{t})>0\}. In view of Lemma [2.6](https://arxiv.org/html/2512.07555v1#S2.Thmtheorem6 "Lemma 2.6. ‣ 2.2. Increasing Profits ‣ 2. The Financial Market and the Concept of Increasing Profits ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), this means that a QVIP can only be made on the set {t∈[0,T]:𝔮′​(Ut)=0}\{t\in[0,T]\colon\mathfrak{q}^{\prime}(U\_{t})=0\}, which implies that {𝔮′=0}\{\mathfrak{q}^{\prime}=0\} has to have positive Lebesgue measure by the semimartingale occupation time formula.

(c)
Finally, we provide some intuition behind the connection between the failure of the RP for SS and the existence of a QVIP.
To this end, we first observe that

|  |  |  |  |
| --- | --- | --- | --- |
| (6.2) |  | the RP for S fails⟺the local martingale ​∫0⋅𝟙{𝔮′=0}​(Us)​dUsc​ is non-constant.\text{the RP for $S$ fails}\quad\Longleftrightarrow\quad\text{the local martingale }\int\_{0}^{\cdot}\mathbbm{1}\_{\{\mathfrak{q}^{\prime}=0\}}(U\_{s})\,\mathrm{d}U\_{s}^{c}\text{ is non-constant.} |  |

Indeed, by the semimartingale occupation time formula together with Lemma [4.4](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem4 "Lemma 4.4 ([19, Corollary 29.18]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), the latter is seen to be equivalent to λ\(𝔮′=0)>0{\mathchoice{\lambda\mkern-4.5mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.83mu{\raisebox{1.72218pt}{\scriptsize$\backslash$}}}{\lambda\mkern-4.5mu{\raisebox{0.86108pt}{\footnotesize$\scriptscriptstyle\backslash$}}}{\lambda\mkern-5.0mu{\raisebox{0.86108pt}{\tiny$\scriptscriptstyle\backslash$}}}}(\mathfrak{q}^{\prime}=0)>0, which is, in turn, equivalent to the failure of the RP for SS by Lemma [6.2](https://arxiv.org/html/2512.07555v1#S6.Thmtheorem2 "Lemma 6.2. ‣ 6. On the Relation of Increasing Profits and the Representation Property ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates").444Alternatively,
it is instructive to deduce the implication
(⟸\Longleftarrow) in ([6.2](https://arxiv.org/html/2512.07555v1#S6.E2 "In Discussion 6.6. ‣ 6. On the Relation of Increasing Profits and the Representation Property ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")) from Lemma [4.1](https://arxiv.org/html/2512.07555v1#S4.Thmtheorem1 "Lemma 4.1 ([1, Lemma 3.2]). ‣ 4. Proofs of Theorems 3.3 and 3.4, and Propositions 3.2 and 3.5 ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"), which, in particular, explains that the local martingale
∫0⋅𝟙{𝔮′=0}​(Us)​dUsc\int\_{0}^{\cdot}\mathbbm{1}\_{\{\mathfrak{q}^{\prime}=0\}}(U\_{s})\,\mathrm{d}U\_{s}^{c}
cannot be represented as a d​Sc\mathrm{d}S^{c}-integral if it is non-constant.
The nontriviality of the local martingale in ([6.2](https://arxiv.org/html/2512.07555v1#S6.E2 "In Discussion 6.6. ‣ 6. On the Relation of Increasing Profits and the Representation Property ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates"))
is equivalent to the fact that ∫0T𝟙{𝔮′=0}​(Us)​d​⟨U⟩s>0\int\_{0}^{T}\mathbbm{1}\_{\{\mathfrak{q}^{\prime}=0\}}(U\_{s})\,\mathrm{d}\langle U\rangle\_{s}>0 with positive probability.
By virtue of ([6.1](https://arxiv.org/html/2512.07555v1#S6.E1 "In 6. On the Relation of Increasing Profits and the Representation Property ‣ On the structure of increasing profits in a 1D general diffusion market with interest rates")), this is necessary for the existence of a QVIP
(and even sufficient if r≠0r\neq 0 and 𝔪acU>0\mathfrak{m}^{U}\_{\operatorname{ac}}>0 on {𝔮′=0}\{\mathfrak{q}^{\prime}=0\}).

## References

* [1]

  A. Anagnostakis, D. Criens, and M. Urusov, On weak notions of
  no-arbitrage in a 1D general diffusion market with interest rates.
  Preprint, arXiv:2503.14078 [q-fin.MF], 2025.
* [2]

  J. J. Benedetto and W. Czaja, Integration and modern analysis,
  Birkhäuser Adv. Texts, Basler Lehrbüch., Basel: Birkhäuser, 2009.
* [3]

  V. I. Bogachev, Measure theory. Vol. I and II, Berlin:
  Springer, 2007.
* [4]

  C. Bruggeman and J. Ruf, A one-dimensional diffusion hits points
  fast, Electron. Commun. Probab., 21 (2016), p. 7.
  Id/No 22.
* [5]

  D. Buckner, K. Dowd, and H. Hulley, Arbitrage problems with
  reflected geometric Brownian motion, Finance Stoch., 28 (2024), pp. 1–26.
* [6]

  E. Cinlar, J. Jacod, P. Protter, and M. J. Sharpe, Semimartingales
  and Markov processes, Z. Wahrscheinlichkeitstheor. Verw. Geb., 54 (1980),
  pp. 161–219.
* [7]

  D. Criens and M. Urusov, Separating times for one-dimensional
  general diffusions.
  arXiv:2211.06042v3 [math.PR] (to appear in Ann. Appl.
  Probab.), 2022.
* [8]

   , On the
  representation property for 1D general diffusion semimartingales, Theory
  Probab. Appl., 69 (2025), pp. 579–591.
* [9]

  D. Criens, M. Urusov, and M. Zervos, in preparation.
* [10]

  H.-J. Engelbert and G. Peskir, Stochastic differential equations for
  sticky Brownian motion, Stochastics, 86 (2014), pp. 993–1021.
* [11]

  H. J. Engelbert and W. Schmidt, Strong Markov continuous local
  martingales and solutions of one-dimensional stochastic differential
  equations. III, Math. Nachr., 151 (1991), pp. 149–197.
* [12]

  C. Fontana, Weak and strong no-arbitrage conditions for continuous
  financial markets, Int. J. Theor. Appl. Finance, 18 (2015), p. 34.
  Id/No 1550005.
* [13]

  D. Freedman, Brownian Motion and Diffusion, Springer New York
  Heidelberg Berlin, 1983.
* [14]

  A. Gairat and V. Shcherbakov, Density of skew Brownian motion and
  its functionals with application in finance, Math. Finance, 27 (2017),
  pp. 1069–1088.
* [15]

  H. U. Gerber and G. Pafumi, Pricing dynamic investment fund
  protection (With discussion by Terence Chan, François-Serge
  Lhabitant and Svein-Arne Persson and a reply by the authors)., N.
  Am. Actuar. J., 4 (2000), pp. 28–41.
* [16]

  K. Itô and H. P. jun. McKean, Diffusion processes and their
  sample paths., Berlin: Springer-Verlag, 1996.
* [17]

  J. Jacod, Calcul stochastique et problèmes de martingales,
  vol. 714 of Lect. Notes Math., Springer, Cham, 1979.
* [18]

  J. Jacod and A. N. Shiryaev, Limit theorems for stochastic
  processes, vol. 288 of Grundlehren der mathematischen Wissenschaften,
  Springer-Verlag, Berlin, 2nd ed., 2003.
* [19]

  O. Kallenberg, Foundations of modern probability. In 2 volumes,
  vol. 99 of Probab. Theory Stoch. Model., Cham: Springer, 3rd revised and
  expanded ed., 2021.
* [20]

  I. Karatzas and C. Kardaras, The numéraire portfolio in
  semimartingale financial models, Finance Stoch., 11 (2007), pp. 447–493.
* [21]

  I. Karatzas and S. E. Shreve, Brownian motion and stochastic
  calculus, vol. 113 of Graduate Texts in Mathematics, Springer-Verlag, New
  York, 2nd ed., 1991.
* [22]

  B. Ko, E. S. W. Shiu, and L. Wei, Pricing maturity guarantee with
  dynamic withdrawal benefit, Insur. Math. Econ., 47 (2010), pp. 216–223.
* [23]

  A. Mijatović and M. Urusov, On the loss of the semimartingale
  property at the hitting time of a level, J. Theoret. Probab., 28 (2015),
  pp. 892–922.
* [24]

  E. Neuman and A. Schied, Optimal portfolio liquidation in target
  zone models and catalytic superprocesses, Finance Stoch., 20 (2016),
  pp. 495–509.
* [25]

  P. Pigato, Extreme at-the-money skew in a local volatility model,
  Finance Stoch., 23 (2019), pp. 827–859.
* [26]

  D. Revuz and M. Yor, Continuous martingales and Brownian motion,
  vol. 293 of Grundlehren der Mathematischen Wissenschaften, Springer-Verlag,
  Berlin, 3rd ed., 1999.
* [27]

  L. C. G. Rogers and D. Williams, Diffusions, Markov processes, and
  martingales. Vol. 2: Itô calculus., Cambridge: Cambridge University
  Press, 2nd ed., 2000.
* [28]

  D. Rossello, Arbitrage in skew Brownian motion models, Insur.
  Math. Econ., 50 (2012), pp. 50–56.
* [29]

  A. N. Shiryaev, Essentials of stochastic finance, vol. 3 of Adv.
  Ser. Stat. Sci. Appl. Probab., Singapore: World Scientific, 1999.