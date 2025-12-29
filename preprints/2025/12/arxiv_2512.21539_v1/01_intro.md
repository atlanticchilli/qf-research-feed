---
authors:
- Igor V. Ovchinnikov
doc_id: arxiv:2512.21539v1
family_id: arxiv:2512.21539
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Chaos, Ito-Stratonovich dilemma, and topological supersymmetry
url_abs: http://arxiv.org/abs/2512.21539v1
url_html: https://arxiv.org/html/2512.21539v1
venue: arXiv q-fin
version: 1
year: 2025
---


Igor V. Ovchinnikov
R&D, CSD, ThermoFisher Scientific Inc, 200 Oyster Point, South San Francisco, 94080, CA, USA
[igor.vlad.ovchinnikov@gmail.com](mailto:igor.vlad.ovchinnikov@gmail.com)

###### Abstract.

It was recently established that the formalism of the generalized transfer operator (GTO) of dynamical systems (DS) theory, applied to stochastic differential equations (SDEs) of arbitrary form, belongs to the family of cohomological topological field theories (TFT) – a class of models at the intersection of algebraic topology and high-energy physics. This interdisciplinary approach, which can be called the supersymmetric theory of stochastic dynamics (STS), can be seen as an algebraic dual to the traditional set-theoretic framework of the DS theory, with its algebraic structure enabling the extension of some DS theory concepts to stochastic dynamics. Moreover, it reveals the presence of a topological supersymmetry (TS) in the GTOs of all SDEs. It also shows that among the various definitions of chaos, positive ”pressure”, defined as the logarithm of the GTO spectral radius, stands out as particularly meaningful from a physical perspective, as it corresponds to the spontaneous breakdown of TS on the TFT side. Via the Goldstone theorem, this definition has a potential to provide the long-sought explanation for the experimental signature of chaotic dynamics known as 1/f noise. Additionally, STS clarifies that among the various existing interpretations of SDEs, only the Stratonovich interpretation yields evolution operators that match the corresponding GTOs and, consequently, have a clear-cut mathematical meaning. Here, we discuss these and other aspects of STS from both the DS theory and TFT perspectives, focusing on links between these two fields and providing mathematical concepts with physical interpretations that may be useful in some contexts.

###### Key words and phrases:

Dynamical Systems, Stochastic Differential Equations, Chaos, Topological Field Theory, Supersymmetry

This work was partly conducted at the Device Research Laboratory, Department of Electrical Engineering, University of California at Los Angeles, Los Angeles, CA 90095, USA

## 1. Introduction

Originally introduced as an extension of the theory of elementary particles, [KaneShifman2000] supersymmetry has since evolved into a mathematical concept [Wit82] that underlies cohomological topological field theories (TFTs), [Baulieu\_1988, Witten88, Witten881, Baulieu\_1989, TFT\_BOOK, labastida1989] a family of models that bridge algebraic topology and high-energy physics. One interesting member of this family [Baulieu\_1988, Gozzi3] is the Parisi-Sourlas approach to Langevin stochastic differential equations (SDEs) [ParSour1, ParSour, Lyapunov\_SUSY] and its extensions to other classes of SDEs, [Gozzi3, Niemi2, Kurchan, KS] including general-form SDEs [OVCHINNIKOV2024114611] capable of exhibiting chaos – a ubiquitous phenomenon with a long history in science [Shep14, Rue14, Mot14, Chaos\_orig] and a central topic in dynamical systems (DS) theory. [Handbook\_of\_DS, Review\_Top\_Entropy] In this way, this framework, that can be called supersymmetric theory of stochastic dynamics (STS), connects TFTs with DS theory, offering interdisciplinary insights that may enrich both fields.

From a DS theory perspective, an interesting insight from STS is that one of the definitions of chaos – the emergence of positive ”pressure” [Rue02, Rue1990] – is equivalent to the spontaneous breakdown of topological supersymmetry (TS), an inherent property of all stochastic DSs. This presents two reasons why this definition stands out among other possible ways to define chaos. First, it makes very good physical sense – Richard Feynman might not have called turbulence ”the most important unsolved problem of classical physics” had he been aware that (hydrodynamic) chaos belongs to the most numerous family of qualitative physical phenomena that arise from spontaneous breakdown of various symmetries of nature. Second, through the Goldstone theorem, spontaneous TS breaking picture of chaos may provide a long-sought explanation for the experimental signature of chaos, known as 1/f noise. [Keshner\_1\_f\_noise\_1982, RevModPhys.53.497, Asc11, PhysRevLett.97.118102]

From the perspective of the TFT approach to SDEs, STS sheds new light on the operator ordering conventions in stochastic evolution operators which, in traditional theory of SDEs, [Kunita2019, Stochastic\_differential\_geometry\_at] correspond to different coexisting interpretations of stochastic dynamics. It shows that only the Stratonovich interpretation yields stochastic evolution operators that match the generalized transfer operators of the DS theory, which are unique and have a very natural mathematical meaning.

Over time, DS theory and TFTs have developed distinct perspectives on concepts that overlap within STS. Relating these perspectives may help facilitate interdisciplinary exchange. To this end, we present two complementary discussions of STS, each drawing connections to the other, and provide physical interpretations of mathematical concepts that may help strengthening the links between the two fields. In Sec.[2](https://arxiv.org/html/2512.21539v1#S2 "2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry"), we discuss continuous-time stochastic DSs. In Sec.[3](https://arxiv.org/html/2512.21539v1#S3 "3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry"), we examine the conventional approach to SDEs and their TFT representation. In Sec.[4](https://arxiv.org/html/2512.21539v1#S4 "4. Topological field theory and stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry"), we focus on the topological aspects of STS such as a close relation between instantons and Morse-Smale DSs. Sec.[5](https://arxiv.org/html/2512.21539v1#S5 "5. Self-sustained dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") offers a qualitative discussion of the STS perspective on 1/f noise and the ”edge of chaos.” We conclude in Sec. [6](https://arxiv.org/html/2512.21539v1#S6 "6. Conclusion ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry").

## 2. Continuous-time stochastic dynamical systems

One of the primary objects of interest in DS theory is a continuous-time deterministic DS, *i.e.*, an ordinary differential equation (ODE), x˙​(t)=F​(x​(t))\dot{x}(t)=F(x(t)), where x∈Xx\in X is a point in the phase (or state) space, XX, which, for concreteness, can be assumed to be a closed smooth manifold, and the law of evolution is represented by a sufficiently smooth flow vector field, F∈T​XF\in TX, from the tangent space of XX.

Deterministic dynamics is a mathematical idealization, as real-world DSs are inevitably subject to unpredictable environmental influence called noise. A more general formulation that incorporates the influence from the noise is given by the following non-autonomous extension of the continuous-time dynamics,111Here and in the following, the summation over repeated indices is assumed. Moreover, to prevent excessive notation, the vector indices are suppressed so that formulas appear as if the phase space was 1D. To avoid confusion, the vector indices are given explicitly in some formulas.

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | x˙​(t)=F​(x​(t))+(2​Θ)1/2​Ga​(x​(t))​ξa​(t)≡ℱ​(x​(t),ξ​(t)),\displaystyle\dot{x}(t)=F(x(t))+(2\Theta)^{1/2}G\_{a}(x(t))\xi^{a}(t)\equiv{\mathscr{F}}(x(t),\xi(t)), |  |

where Ga∈T​X,a=1,…,D,D=dimXG\_{a}\in TX,a=1,\ldots,D,D=\dim X is a set of sufficiently smooth vector fields that specify how the DS is coupled to the time-dependent noise, ξ​(t)∈ℝD\xi(t)\in\mathbb{R}^{D}.222In the literature, the noise is called additive/multiplicative depending on whether GaG\_{a}’s are independent/dependent on xx

An external observer does not know which noise configuration is realized in a given experiment. Consequently, a probabilistic framework is necessary – one that incorporates the observer’s uncertainty about the noise and, consequently, the DS. However, the noise itself is not uncertain: in any given experiment, the noise is just a deterministic function of time. Therefore, before introducing the observer’s uncertainty into the model – a step we will take later – Eq.([2.1](https://arxiv.org/html/2512.21539v1#S2.E1 "In 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) is an ODE governed by a time-dependent flow vector field, ℱ\mathscr{F} (see Fig.[1](https://arxiv.org/html/2512.21539v1#S2.F1 "Figure 1 ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")). 333This picture differs from the traditional understanding of SDEs, which is examined in Sec. [3](https://arxiv.org/html/2512.21539v1#S3 "3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") and whose relation to Eq. ([2.1](https://arxiv.org/html/2512.21539v1#S2.E1 "In 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) is discussed in Sec. [3.4](https://arxiv.org/html/2512.21539v1#S3.SS4 "3.4. Ito-Stratonovich dilemma ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry").

![Refer to caption](Basics_0.png)

![Refer to caption](Basics.png)

Figure 1.  (left) A continuous-time stochastic DS is defined by a flow vector field, ℱ\mathscr{F}, from the tangent space, T​XTX, of the phase space, XX. ℱ​(ξ​(t)){\mathscr{F}}(\xi(t)) is time-dependent due to the presence of the time-dependent noise, ξ​(t)\xi(t). The DS is equivalent to two-parameter family of noise-configuration-dependent diffeomorphisms, M​(ξ)t​t′M(\xi)\_{tt^{\prime}}, such that the trajectories are given by x​(t)=M​(ξ)t​t′​(x​(t′))x(t)=M(\xi)\_{tt^{\prime}}(x(t^{\prime})). (right) In the spirit of the pathintegral representation of temporal evolution, there is a copy of XX at every time moment and evolution is defined by pullbacks, M^​(ξ)t′​t∗\hat{M}(\xi)\_{t^{\prime}t}^{\*}, induced by inverse maps, M​(ξ)t′​tM(\xi)\_{t^{\prime}t}. The pullbacks act on a time-dependent differential form, |ψ​(t)⟩|\psi(t)\rangle, understood as a ”wavefunction” - a time-dependent object encoding information of the system’s past. When averaged over noise configurations, a pullback yields the generalized transfer operator, which is unique and corresponds to the Stratonovich interpretation of stochastic dynamics.

For any given initial condition and noise configuration, Eq.([2.1](https://arxiv.org/html/2512.21539v1#S2.E1 "In 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) yields a unique solution. Moreover, even if the noise configuration is not differentiable with respect to time, the solution is differentiable with respect to the initial condition. [Slavik] Therefore, there is a two-parameter family of ξ\xi-dependent diffeomorphisms,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.2) |  | M​(ξ)t​t′:X→X,M​(ξ)t​t′∘M​(ξ)t′​t′′=M​(ξ)t​t′′,M​(ξ)t​t′|t=t′=IdX,\displaystyle M(\xi)\_{tt^{\prime}}:X\to X,M(\xi)\_{tt^{\prime}}\circ M(\xi)\_{t^{\prime}t^{\prime\prime}}=M(\xi)\_{tt^{\prime\prime}},\left.M(\xi)\_{tt^{\prime}}\right|\_{t=t^{\prime}}=\text{Id}\_{X}, |  |

such that x​(t)=M​(ξ)t​t′​(x′)x(t)=M(\xi)\_{tt^{\prime}}(x^{\prime}) is the solution with the initial condition x​(t′)=x′x(t^{\prime})=x^{\prime}.

### 2.1. Generalized probability distributions

The dynamics can now be defined as follows: if at time t′t^{\prime}, the system is described by the probability distribution P​(x)P(x), then the average value of some function f:X→ℝf:X\to\mathbb{R} at a later time tt is

|  |  |  |  |
| --- | --- | --- | --- |
| (2.3) |  | f¯​(t)=∫Xf​(M​(ξ)t​t′​(x))​P​(x)​dD​x=∫Xf​(x)​M^​(ξ)t′​t∗​(P​(x)​dD​x).\displaystyle\bar{f}(t)=\int\_{X}f\left(M(\xi)\_{tt^{\prime}}(x)\right)P(x)\mathrm{d}^{D}x=\int\_{X}f(x)\hat{M}(\xi)\_{t^{\prime}t}^{\*}\left(P(x)\mathrm{d}^{D}x\right). |  |

Here M^​(ξ)t′​t∗\hat{M}(\xi)^{\*}\_{t^{\prime}t} is action or pullback induced by the ”inverse” map, M​(ξ)t​t′−1=M​(ξ)t′​tM(\xi)\_{tt^{\prime}}^{-1}=M(\xi)\_{t^{\prime}t}, on the probability distribution understood in the coordinate-free setting as a top-degree differential form, P​(x)​dD​x≡P​(x)​d​x1∧…∧d​xDP(x)\mathrm{d}^{D}x\equiv P(x)\mathrm{d}x^{1}\wedge...\wedge\mathrm{d}x^{D}. In other words, instead of propagating the dynamical variables forward, one can equivalently propagate the probability distribution backward,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.4) |  | P​(t)=M^​(ξ)t′​t∗​P​(t′).\displaystyle P(t)=\hat{M}(\xi)\_{t^{\prime}t}^{\*}P(t^{\prime}). |  |

If the observer is interested only in the original dynamical variables, the description of the DS in terms of P​(x)P(x) may suffice. However, to explore properties such as Lyapunov exponents, this description of the DS must be extended. Namely, one must introduce dynamical fields that represent ”differentials” – objects that belong to the tangent space of XX – evolving in the same way as the differentials of the original dynamical variables. Moreover, there is also a requirement that the properties of the new fields must reflect the fact that propagating two parallel differentials is pointless as it does not yield any additional information about Lyapunov exponents, as compared to propagating just one differential.

The fields that satisfy these requirements are anticommuting differentials or differential volume elements in the definition of the differential forms or kk-forms:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.5) |  | ψ(k)​(x)=(1/k!)​ψi1​….ik(k)​(x)​d​xi1∧…∧d​xik∈Ω(k)​(x), 0≤k≤D,\displaystyle\psi^{(k)}(x)=(1/k!)\psi^{(k)}\_{i\_{1}....i\_{k}}(x)\mathrm{d}x^{i\_{1}}\wedge...\wedge\mathrm{d}x^{i\_{k}}\in\Omega^{(k)}(x),\;0\leq k\leq D, |  |

where Ω(k)​(x)\Omega^{(k)}(x) is the space of kk-forms at point xx. Now, the above-mentioned generalization of the dynamical probability distributions is,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.6) |  | ψ=∑k=0Dψ(k)∈Ω=⨁k=0DΩ(k).\displaystyle\psi=\sum\nolimits\_{k=0}^{D}\psi^{(k)}\in\Omega=\bigoplus\nolimits\_{k=0}^{D}\Omega^{(k)}. |  |

Its temporal evolution follows from the above example and is given by the pullback of inverse maps,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.7) |  | ψ​(t)=M^​(ξ)t′​t∗​ψ​(t′).\displaystyle\psi(t)=\hat{M}(\xi)\_{t^{\prime}t}^{\*}\psi(t^{\prime}). |  |

Only top differential forms from Ω(D)\Omega^{(D)} represent probability distributions. 444In some cases, it may be possible to interpret the wavefunctions as the conditional probability distributions. [OvcEntropy] If at some moment of time they are positive everywhere on XX, they will remain this property at all later times (see Sec.[2.4.5](https://arxiv.org/html/2512.21539v1#S2.SS4.SSS5 "2.4.5. Ergodic zero ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") below). Other generalized distributions can be negative and the term ”distribution” may be misleading. Therefore, we adopt the terminology of quantum theory and refer to them instead as ”wavefunctions”. As compared to the conventional probability distributions, the wavefunctions contain additional memory that encodes information about Lyapunov exponents. [Lyapunov\_SUSY]

### 2.2. Generalized transfer operator

Unlike trajectories, points in XX, or maps, pullbacks are linear objects even when XX is nonlinear. As a linear object, M^​(ξ)t′​t∗\hat{M}(\xi)^{\*}\_{t^{\prime}t} can be averaged over noise configurations, yielding an evolution operator that incorporates the uncertainty of the external observer about the DS, 555The order of time arguments is purposely reversed here so that (for a white noise): ℳ^t​t′′=ℳ^t​t′​ℳ^t′​t′′\hat{\mathcal{M}}\_{tt^{\prime\prime}}=\hat{\mathcal{M}}\_{tt^{\prime}}\hat{\mathcal{M}}\_{t^{\prime}t^{\prime\prime}}.

|  |  |  |  |
| --- | --- | --- | --- |
| (2.8) |  | ℳ^t​t′=∬M^​(ξ)t′​t∗​𝒫​(ξ)​𝒟​ξ​=def​⟨M^​(ξ)t′​t∗⟩noise.\displaystyle\hat{\mathcal{M}}\_{tt^{\prime}}=\iint\hat{M}(\xi)^{\*}\_{t^{\prime}t}{\mathcal{P}}(\xi)\mathcal{D}\xi\overset{\text{def}}{=}\langle\hat{M}(\xi)^{\*}\_{t^{\prime}t}\rangle\_{\text{noise}}. |  |

Here, 𝒟​ξ{\mathcal{D}}\xi and 𝒫​(ξ){\mathcal{P}}(\xi) are, respectively, the differential of the functional integration (see, *e.g.*, Ref.[FunctionalIntegral] and Refs. therein) over the noise configurations and the corresponding normalized probability functional, so that ⟨1⟩noise=1\langle 1\rangle\_{\text{noise}}=1. The properties of the noise can be defined either by specifying 𝒫\mathcal{P}, as will be done in Sec.[3](https://arxiv.org/html/2512.21539v1#S3 "3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry"), or by specifying all the noise averages, for example, via the introduction of the generating functional, G​(η)=⟨e∫ηa​(τ)​ξa​(τ)​dτ⟩noiseG(\eta)=\langle e^{\int\eta\_{a}(\tau)\xi^{a}(\tau)\mathrm{d}\tau}\rangle\_{\text{noise}}, so that,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.9) |  | ⟨ξa1​(t1)​…​ξak​(tk)⟩noise=δδ​ηa1​(t1)​…​δδ​ηak​(tk)​G​(η)|η=0,\displaystyle\langle\xi^{a\_{1}}(t\_{1})...\xi^{a\_{k}}(t\_{k})\rangle\_{\text{noise}}=\frac{\delta}{\delta\eta\_{a\_{1}}(t\_{1})}...\frac{\delta}{\delta\eta\_{a\_{k}}(t\_{k})}G(\eta)\big|\_{\eta=0}, |  |

where δ/δ​ηa​(t)\delta/\delta\eta\_{a}(t) denotes functional differentiation. Below, we use the Gaussian white noise with G​(η)=e∫(η2​(τ)/2)​dτG(\eta)=e^{\int(\eta^{2}(\tau)/2)\mathrm{d}\tau} and,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.10) |  | ⟨ξa​(t)⟩noise=0,⟨ξa​(t)​ξb​(t′)⟩noise=δa​b​δ​(t−t′),…\displaystyle\langle\xi^{a}(t)\rangle\_{\text{noise}}=0,\;\langle\xi^{a}(t)\xi^{b}(t^{\prime})\rangle\_{\text{noise}}=\delta^{ab}\delta(t-t^{\prime}),... |  |

where δ​(t−t′)\delta(t-t^{\prime}) is the Dirac delta function.

In DS theory, the pullback averaged over noise is known as the generalized transfer operator (GTO). [Rue02, Rue1990] We use the same identifier for operator ([2.8](https://arxiv.org/html/2512.21539v1#S2.E8 "In 2.2. Generalized transfer operator ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), which is a variant of this concept with the difference that the noise is infinite dimensional and the pullbacks correspond to inverse diffeomorphisms.

The explicit form of the GTO can be derived by utilizing the concept of the chronological ordering of operators,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.11) |  | M^​(ξ)t′​t∗≡𝒯​e−∫t′tL^ℱ​(ξ​(τ))​dτ\displaystyle\hat{M}(\xi)^{\*}\_{t^{\prime}t}\equiv{\mathcal{T}}e^{-\int\_{t^{\prime}}^{t}\hat{L}\_{{\mathscr{F}}(\xi(\tau))}\mathrm{d}\tau} |  |
|  |  |  |
| --- | --- | --- |
|  | =1^Ω−∫t′tL^ℱ​(ξ​(τ))​dτ+∫t′tL^ℱ​(ξ​(τ1))​dτ1​∫t′τ1L^ℱ​(ξ​(τ2))​dτ2​…,\displaystyle=\hat{1}\_{\Omega}-\int\_{t^{\prime}}^{t}\hat{L}\_{{\mathscr{F}}(\xi(\tau))}\mathrm{d}\tau+\int\_{t^{\prime}}^{t}\hat{L}\_{{\mathscr{F}}(\xi(\tau\_{1}))}\mathrm{d}\tau\_{1}\int\_{t^{\prime}}^{\tau\_{1}}\hat{L}\_{{\mathscr{F}}(\xi(\tau\_{2}))}\mathrm{d}\tau\_{2}\dots, |  |

which is the solution of the following differential equation,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.12) |  | ∂tM^​(ξ)t′​t∗=−L^ℱ​(ξ​(t))​M^​(ξ)t′​t∗,M^​(ξ)t′​t∗|t=t′=1^Ω,\displaystyle\partial\_{t}\hat{M}(\xi)^{\*}\_{t^{\prime}t}=-\hat{L}\_{{\mathscr{F}}(\xi(t))}\hat{M}(\xi)^{\*}\_{t^{\prime}t},\;\hat{M}(\xi)^{\*}\_{t^{\prime}t}\big|\_{t=t^{\prime}}=\hat{1}\_{\Omega}, |  |

where L^ℱ​(ξ​(t))=d​M^​(ξ)t​t′∗/d​t|t=t′\hat{L}\_{{\mathscr{F}}(\xi(t))}=\mathrm{d}\hat{M}(\xi)^{\*}\_{tt^{\prime}}/\mathrm{d}t|\_{t=t^{\prime}} is the infinitesimal pullback or Lie derivative. Eq.([2.12](https://arxiv.org/html/2512.21539v1#S2.E12 "In 2.2. Generalized transfer operator ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) can be obtained by Taylor expanding the following equation in Δ​τ\Delta\tau

|  |  |  |  |
| --- | --- | --- | --- |
| (2.13) |  | M^​(ξ)t′​t+Δ​τ∗=(M​(ξ)t′​t∘M​(ξ)t​t+Δ​τ)∗^=M^​(ξ)t​t+Δ​τ∗​M^​(ξ)t′​t∗,\displaystyle\hat{M}(\xi)^{\*}\_{t^{\prime}t+\Delta\tau}=\widehat{(M(\xi)\_{t^{\prime}t}\circ M(\xi)\_{tt+\Delta\tau})^{\*}}=\hat{M}(\xi)\_{tt+\Delta\tau}^{\*}\hat{M}(\xi)\_{t^{\prime}t}^{\*}, |  |

and taking the limit Δ​τ→0\Delta\tau\to 0 using M^​(ξ)t​t+Δ​τ∗=1^Ω−Δ​τ​L^ℱ​(ξ​(t))+…\hat{M}(\xi)\_{tt+\Delta\tau}^{\*}=\hat{1}\_{\Omega}-\Delta\tau\hat{L}\_{{\mathscr{F}}(\xi(t))}+.... The minus sign here reminds once again that we are dealing with the inverse diffeomorphisms.

Assuming Gaussian white noise ([2.10](https://arxiv.org/html/2512.21539v1#S2.E10 "In 2.2. Generalized transfer operator ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), utilizing the linearity of the Lie derivative in its argument, L^ℱ​(ξ​(t))=L^F+ξa​(t)​(2​Θ)1/2​L^Ga\hat{L}\_{{\mathscr{F}}(\xi(t))}=\hat{L}\_{F}+\xi^{a}(t)(2\Theta)^{1/2}\hat{L}\_{G\_{a}}, noting that ℳ^t​t′′=ℳ^t​t′​ℳ^t′​t′′\hat{\mathcal{M}}\_{tt^{\prime\prime}}=\hat{\mathcal{M}}\_{tt^{\prime}}\hat{\mathcal{M}}\_{t^{\prime}t^{\prime\prime}} because the variables of white noise at different time moments do not correlate, and using Eq.([2.11](https://arxiv.org/html/2512.21539v1#S2.E11 "In 2.2. Generalized transfer operator ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) and identities ∫tt+Δ​τdτ1​∫tτ1dτ2=Δ​τ2/2\int\_{t}^{t+\Delta\tau}\mathrm{d}\tau\_{1}\int\_{t}^{\tau\_{1}}\mathrm{d}\tau\_{2}=\Delta\tau^{2}/2 and ∫tt+Δ​τdτ1​∫tτ1δ​(τ1−τ2)​dτ2=Δ​τ/2\int\_{t}^{t+\Delta\tau}\mathrm{d}\tau\_{1}\int\_{t}^{\tau\_{1}}\delta(\tau\_{1}-\tau\_{2})\mathrm{d}\tau\_{2}=\Delta\tau/2, one has,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.14) |  | ℳ^t+Δ​τ,t′=ℳ^t+Δ​τ,t​ℳ^t​t′=⟨𝒯​e−∫tt+Δ​τL^ℱ​(ξ​(τ))​dτ⟩noise​ℳ^t​t′\displaystyle\hat{\mathcal{M}}\_{t+\Delta\tau,t^{\prime}}=\hat{\mathcal{M}}\_{t+\Delta\tau,t}\hat{\mathcal{M}}\_{tt^{\prime}}=\langle{\mathcal{T}}e^{-\int\_{t}^{t+\Delta\tau}\hat{L}\_{{\mathscr{F}}(\xi(\tau))}\mathrm{d}\tau}\rangle\_{\text{noise}}\hat{\mathcal{M}}\_{tt^{\prime}} |  |
|  |  |  |
| --- | --- | --- |
|  | =(1^Ω−Δ​τ​L^F+Δ​τ2​L^F2/2+Δ​τ​Θ​L^Ga​L^Ga+…)​ℳ^t​t′.\displaystyle=\big(\hat{1}\_{\Omega}-\Delta\tau\hat{L}\_{F}+\Delta\tau^{2}\hat{L}\_{F}^{2}/2+\Delta\tau\Theta\hat{L}\_{G\_{a}}\hat{L}\_{G\_{a}}+...\big)\hat{\mathcal{M}}\_{tt^{\prime}}. |  |

In the limit Δ​τ→0\Delta\tau\to 0, the above equation gives,

|  |  |  |
| --- | --- | --- |
|  | ∂tℳ^t​t′=−H^​ℳ^t​t′,\displaystyle\partial\_{t}\hat{\mathcal{M}}\_{tt^{\prime}}=-\hat{H}\hat{\mathcal{M}}\_{tt^{\prime}}, |  |

which integrates into the following expression for the *finite-time* GTO,

|  |  |  |
| --- | --- | --- |
|  | ℳ^t​t′=e−(t−t′)​H^.\displaystyle\hat{\mathcal{M}}\_{tt^{\prime}}=e^{-(t-t^{\prime})\hat{H}}. |  |

Here, the *infinitesimal* GTO,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.15) |  | H^=L^F−Θ​L^Ga​L^Ga,\displaystyle\hat{H}=\hat{L}\_{F}-\Theta\hat{L}\_{G\_{a}}\hat{L}\_{G\_{a}}, |  |

has a very clear meaning: the first and the second terms are, respectively, the Lie derivative representing the drift along the deterministic part of the flow, FF, and the Laplacian666To be more accurate, this is a member of the family of Laplacians. representing the diffusion associated with the accumulation of uncertainty due to the influence from the noise.

From the point of view of the theory of SDEs, the GTO ([2.15](https://arxiv.org/html/2512.21539v1#S2.E15 "In 2.2. Generalized transfer operator ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) is a stochastic evolution operator in the Stratonovich interpretation of stochastic dynamics.[elworthy1999geometry] However, unlike the stochastic evolution operators in the theory of SDEs and/or the Parisi-Sourlas approach, the GTO has a clear-cut mathematical meaning, making it unique and eliminating the need for additional interpretations beyond its definition.

### 2.3. Topological supersymmetry

Central to our discussion is the Cartan formula for a Lie derivative, *e.g.*,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.16) |  | L^F=[d^,ı^F],\displaystyle\hat{L}\_{F}=[\hat{d},\hat{\imath}\_{F}], |  |

where d^:Ω(k)→Ω(k+1),k=0,D−1\hat{d}:\Omega^{(k)}\to\Omega^{(k+1)},k=0,D-1 and ı^F:Ω(k)→Ω(k−1),k=1​…​D\hat{\imath}\_{F}:\Omega^{(k)}\to\Omega^{(k-1)},k=1...D are, respectively, the exterior derivative and interior multiplication along its argument (see, e.g., Ref.[Nakahara]), and we introduced the concept of bi-graded commutator:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.17) |  | [a^,b^]=a^​b^−(−1)deg ​a^​ deg ​b^​b^​a^,\displaystyle[\hat{a},\hat{b}]=\hat{a}\hat{b}-(-1)^{\text{deg }{\hat{a}}\text{ deg }{\hat{b}}}\hat{b}\hat{a}, |  |

where the degree of an operator is defined as deg ​a^=l−k\text{deg }\hat{a}=l-k for a^:Ω(k)→Ω(l)\hat{a}:\Omega^{(k)}\to\Omega^{(l)}. Both, d^\hat{d} and ı^ℱ\hat{\imath}\_{\mathscr{F}} have odd degrees so that the r.h.s. of Eq.([2.16](https://arxiv.org/html/2512.21539v1#S2.E16 "In 2.3. Topological supersymmetry ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) is an anti-commutator.

The fundamental property of d^\hat{d} is nilpotency, d^2=0\hat{d}^{2}=0. It implies, particularly, that d^\hat{d} commutes with any d^\hat{d}-exact operator, i.e., operator of the form [d^,a^][\hat{d},\hat{a}]: [d^,[d^,a^]]=0,∀a^[\hat{d},[\hat{d},\hat{a}]]=0,\forall\hat{a}. This property and the fact that a commutator with d^\hat{d} is a bi-graded ”differentiation”, [d^,a^​b^]=[d^,a^]​b^+(−1)ind​a^​a^​[d^,b^][\hat{d},\hat{a}\hat{b}]=[\hat{d},\hat{a}]\hat{b}+(-1)^{\text{ind}\hat{a}}\hat{a}[\hat{d},\hat{b}], can be used to reveal that the GTO in Eq.([2.15](https://arxiv.org/html/2512.21539v1#S2.E15 "In 2.2. Generalized transfer operator ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) is d^\hat{d}-exact,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.18) |  | H^=[d^,d¯^],\displaystyle\hat{H}=[\hat{d},\hat{\bar{d}}], |  |

with d¯^=ı^F−Θ​ı^Ga​L^Ga\hat{\bar{d}}=\hat{\imath}\_{F}-\Theta\hat{\imath}\_{G\_{a}}\hat{L}\_{G\_{a}}. As a d^\hat{d}-exact operator, the GTO ([2.18](https://arxiv.org/html/2512.21539v1#S2.E18 "In 2.3. Topological supersymmetry ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) is also d^\hat{d}-closed, i.e., it is commutative with d^\hat{d}, 777Getting a bit head, the d^\hat{d}-exactness of the GTO ([2.18](https://arxiv.org/html/2512.21539v1#S2.E18 "In 2.3. Topological supersymmetry ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) is a stronger property than its d^\hat{d}-closeness ([2.19](https://arxiv.org/html/2512.21539v1#S2.E19 "In 2.3. Topological supersymmetry ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")). While d^\hat{d}-closeness ensures the pairing of the eigenstates into non-supersymmetric doublets (see Sec. [2.4.3](https://arxiv.org/html/2512.21539v1#S2.SS4.SSS3 "2.4.3. Non-supersymmetric doublets ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") below), d^\hat{d}-exactness further implies that supersymmetric singlets have exactly zero eigenvalues (see Sec.[2.4.4](https://arxiv.org/html/2512.21539v1#S2.SS4.SSS4 "2.4.4. Supersymmetric singlets ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") below).

|  |  |  |  |
| --- | --- | --- | --- |
| (2.19) |  | [d^,H^]=0.\displaystyle[\hat{d},\hat{H}]=0. |  |

In physics, it is said that a model has an internal continuous symmetry if there is a continuous group of operators such that G^​H^​G^−1=H^\hat{G}\hat{H}\hat{G}^{-1}=\hat{H}, where G^\hat{G} represents an element of the group. The generators of this group commute with H^\hat{H} whose eigenstates form irreducible representations of the group: one-dimensional fully symmetric representations corresponding to non-degenerate eigenstates are called singlets, while more-than-one dimensional representations corresponding to degenerate eigenstates are called multiplets. The symmetry is said to be broken spontaneously if the ground state is degenerate, i.e., it is a multiplet.

This scenario applies to our case: the continuous group of internal symmetry is G^s=es​d^=1+s​d^\hat{G}\_{s}=e^{s\hat{d}}=1+s\hat{d}, where s∈ℝs\in\mathbb{R}, G^s​G^t=G^t+s\hat{G}\_{s}\hat{G}\_{t}=\hat{G}\_{t+s}, and G^−s​H^​G^s=H^\hat{G}\_{-s}\hat{H}\hat{G}\_{s}=\hat{H}; the sole generator of this group is d^\hat{d}; the supersymmetric singlets in Sec.[2.4.4](https://arxiv.org/html/2512.21539v1#S2.SS4.SSS4 "2.4.4. Supersymmetric singlets ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") are the fully symmetric one-dimensional representations, while the non-supersymmetric doublets in Sec.[2.4.3](https://arxiv.org/html/2512.21539v1#S2.SS4.SSS3 "2.4.3. Non-supersymmetric doublets ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") are irreducible 2-dimensional representations. Consequently, d^\hat{d} can be recognized as the (generator of the) symmetry of the model.

This symmetry can be further identified as a supersymmetry – the term used for symmetries that mix bosons and fermions. This becomes evident when the differentials of wavefunctions are represented by Grassmann numbers or fermions, [Wit82] ∧d​xi∼χi\wedge\mathrm{d}x^{i}\sim\chi^{i}, so that the basic property of the differentials, d​xi1∧d​xi2=−d​xi2∧d​xi1\mathrm{d}x^{i\_{1}}\wedge\mathrm{d}x^{i\_{2}}=-\mathrm{d}x^{i\_{2}}\wedge\mathrm{d}x^{i\_{1}}, is consistent with that of Grassmann numbers, χi1​χi2=−χi2​χi1\chi^{i\_{1}}\chi^{i\_{2}}=-\chi^{i\_{2}}\chi^{i\_{1}}. In these terms, the exterior derivative has the form,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.20) |  | d^=χi​∂/∂xi,\displaystyle\hat{d}=\chi^{i}\partial/\partial x^{i}, |  |

and it acts on a wavefunction by destroying a boson, xx, and creating a fermion, χ\chi.

Furthermore, being a fundamental object in algebraic topology – where it serves as an algebraic dual of the boundary operation – d^\hat{d} can be identified as the topological supersymmetry (TS). Another justification for this terminology is that a d^\hat{d}-exact evolution operator, as in Eq.([2.18](https://arxiv.org/html/2512.21539v1#S2.E18 "In 2.3. Topological supersymmetry ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), is a defining characteristic of TFTs, [TFT\_BOOK] where the pathintegral counterpart of d^\hat{d} – typically denoted as QQ (see Eq.([3.16](https://arxiv.org/html/2512.21539v1#S3.E16 "In 3.2. Parisi-Sourlas approach as a BRST gauge-fixing ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) below) – is referred to as TS.

From the mathematical point of view, the presence of TS follows from the fact that d^\hat{d} commutes with pullbacks of all diffeomorphisms. In other words, the TS is an algebraic representation of the property of diffeomorphisms to preserve the topology of the phase space: infinitely close initial conditions result in close trajectories for any noise configuration. This further suggests that if TS is broken (see below), this property may no longer hold, allowing initially close points to evolve into trajectories that diverge over infinitely long evolution – a hallmark of chaos known as the butterfly effect. [Lorenz] Through its algebraic structure, STS extends this traditional understanding of the butterfly effect based on the concept of a deterministic trajectory to stochastic dynamics, where all trajectories are possible.

### 2.4. Eigensystem

The eigensystem of the GTO has a set of properties that constrains the spectra of the physically meaningful models – those with discrete spectra and finite spectral radius of the GTO – to the three major types presented in Fig.[2](https://arxiv.org/html/2512.21539v1#S2.F2 "Figure 2 ‣ 2.4.3. Non-supersymmetric doublets ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry"). [OvcEntropy] These properties are discussed in this section.

#### 2.4.1. Pseudo-Hermiticity and completeness

The GTO is a real operator and its eigenvalues are either real or come in complex conjugate pairs. This makes it a pseudo-Hermitian operator. [Mos02] Complex conjugate pairs of eigenvalues can be identified as Reulle-Pollicott resonances and they can be thought of as a nontrivial representation of the pseudo-time reversal (η​T\eta T-) symmetry. [Mos03] This symmetry and its breaking will be recalled in Sec.[5.1.2](https://arxiv.org/html/2512.21539v1#S5.SS1.SSS2 "5.1.2. Spontaneously pseudo-time-reversal symmetry breaking ‣ 5.1. Global ground state ‣ 5. Self-sustained dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") below. For now, the only property of pseudo-Hermiticity of H^\hat{H} we need is the existence of a complete bi-orthogonal eigensystem:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.21) |  | H^​ψα=Hα​ψα,ψ¯α​H^=ψ¯α​Hα,∫Xψ¯α∧ψβ=δα​β,\displaystyle\hat{H}\psi\_{\alpha}=H\_{\alpha}\psi\_{\alpha},\bar{\psi}\_{\alpha}\hat{H}=\bar{\psi}\_{\alpha}H\_{\alpha},\;\int\_{X}\bar{\psi}\_{\alpha}\wedge\psi\_{\beta}=\delta\_{\alpha\beta}, |  |

with HαH\_{\alpha} being the corresponding eigenvalues. For simplicity, the spectrum is assumed discrete, which is the case for compact XX and non-degenerate noise, that is, such that the noise-induced metric gi​j​(x)=Gai​(x)​Gaj​(x)g^{ij}(x)=G^{i}\_{a}(x)G\_{a}^{j}(x) is non-degenerate min spec ​g​(x)>0,∀x\text{min}\text{ spec }g(x)>0,\forall x so that H^\hat{H} is elliptic.

Any (right) wavefunction, ψ\psi, can be resolved as

|  |  |  |  |
| --- | --- | --- | --- |
| (2.22) |  | ψ=∑αcα​ψα,cα=∫Xψ¯α∧ψ.\displaystyle\psi=\sum\_{\alpha}c\_{\alpha}\psi\_{\alpha},c\_{\alpha}=\int\_{X}\bar{\psi}\_{\alpha}\wedge\psi. |  |

To make the distinction between the left and right wavefunctions manifest, let us adopt the terminology of quantum theory and refer to the left and right vectors as bras and kets, ψα→|α⟩\psi\_{\alpha}\to|\alpha\rangle, ψ¯α→⟨α|\bar{\psi}\_{\alpha}\to\langle\alpha|. In these notations, Eqs.([2.21](https://arxiv.org/html/2512.21539v1#S2.E21 "In 2.4.1. Pseudo-Hermiticity and completeness ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) read

|  |  |  |  |
| --- | --- | --- | --- |
| (2.23) |  | H^​|α⟩=Hα​|α⟩,⟨α|​H^=⟨α|​Hα,⟨α|β⟩​=def​∫Xψ¯α∧ψβ=δα​β,\displaystyle\hat{H}|\alpha\rangle=H\_{\alpha}|\alpha\rangle,\langle\alpha|\hat{H}=\langle\alpha|H\_{\alpha},\;\langle\alpha|\beta\rangle\overset{\text{def}}{=}\int\_{X}\bar{\psi}\_{\alpha}\wedge\psi\_{\beta}=\delta\_{\alpha\beta}, |  |

and the completeness property ([2.22](https://arxiv.org/html/2512.21539v1#S2.E22 "In 2.4.1. Pseudo-Hermiticity and completeness ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) can be expressed as a resolution of unity,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.24) |  | 1^Ω=∑α|α⟩​⟨α|,|ψ⟩=1^Ω​|ψ⟩=∑αcα​|α⟩,cα=⟨α|ψ⟩.\displaystyle\hat{1}\_{\Omega}=\sum\nolimits\_{\alpha}|\alpha\rangle\langle\alpha|,\;|\psi\rangle=\hat{1}\_{\Omega}|\psi\rangle=\sum\_{\alpha}c\_{\alpha}|\alpha\rangle,c\_{\alpha}=\langle\alpha|\psi\rangle. |  |

#### 2.4.2. Conservation of fermions

The GTO is block diagonal, H^=diag​(H^(0)​…​H^(D))\hat{H}=\text{diag}(\hat{H}^{(0)}...\hat{H}^{(D)}), because it commutes with the operator of the degree of a differential form, k^​|ψ⟩=k​|ψ⟩,∀|ψ⟩∈Ω(k)\hat{k}|\psi\rangle=k|\psi\rangle,\forall|\psi\rangle\in\Omega^{(k)}. Each eigenstate has a well-defined degree,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.25) |  | k^​|α⟩=kα​|α⟩, 0≤kα≤D.\displaystyle\hat{k}|\alpha\rangle=k\_{\alpha}|\alpha\rangle,\;0\leq k\_{\alpha}\leq D. |  |

In physics terms, k^\hat{k} is the operator of the number of fermions, which is a conserved quantity due to its commutativity with the GTO.

#### 2.4.3. Non-supersymmetric doublets

Except for a few supersymmetric singlets (see below), all the eigenstates are non-supersymmetric ”doublets”. This can be seen as follows. [Torsten] Let first note that if |α⟩|\alpha\rangle is an eigenstate and |α′⟩=d^​|α⟩≠0|\alpha^{\prime}\rangle=\hat{d}|\alpha\rangle\neq 0 than |α′⟩|\alpha^{\prime}\rangle is also an eigenstate with the same eigenvalue because [d^,H^]=0[\hat{d},\hat{H}]=0 and,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.26) |  | H^​|α⟩=Hα​|α⟩→d^​H^​|α⟩=Hα​d^​|α⟩→H^​|α′⟩=Hα​|α′⟩.\displaystyle\hat{H}|\alpha\rangle=H\_{\alpha}|\alpha\rangle\to\hat{d}\hat{H}|\alpha\rangle=H\_{\alpha}\hat{d}|\alpha\rangle\to\hat{H}|\alpha^{\prime}\rangle=H\_{\alpha}|\alpha^{\prime}\rangle. |  |

We also note that d^\hat{d} raises the degree of a wavefunction: kα′=kα+1k\_{\alpha^{\prime}}=k\_{\alpha}+1.

Let us now act by d^\hat{d} on each eigenstate of H^(0)\hat{H}^{(0)}, as visualized by the lowest row of curved arrows in Fig.[2](https://arxiv.org/html/2512.21539v1#S2.F2 "Figure 2 ‣ 2.4.3. Non-supersymmetric doublets ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry"). The result is a set of all the d^\hat{d}-exact eigenstates of H^(1)\hat{H}^{(1)}. 888A d^\hat{d}-exact state is a state from the image of d^\hat{d}, i.e., a state of the form d^​|a⟩\hat{d}|a\rangle. We can now further act by d^\hat{d} on all the eigenstates of H^(1)\hat{H}^{(1)}, as visualized by the second row of curved arrows in Fig.[2](https://arxiv.org/html/2512.21539v1#S2.F2 "Figure 2 ‣ 2.4.3. Non-supersymmetric doublets ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry"). All the d^\hat{d}-exact eigenstates which came from H^(0)\hat{H}^{(0)} vanish due to the nilpotency of TS: d^2=0\hat{d}^{2}=0. Other eigenstates turn into d^\hat{d}-exact eigenstates of H(2)H^{(2)}. Continuing this recursive procedure, we traverse and pair up all the eigenstates except those which are d^\hat{d}-closed 999A d^\hat{d}-closed state is a state in the kernel of d^\hat{d}, i.e., a state, |a⟩|a\rangle, such that d^​|a⟩=0\hat{d}|a\rangle=0. but not d^\hat{d}-exact, i.e., the ones that are nontrivial in the cohomology of d^\hat{d}, or, in de Rham cohomology. These are the supersymmetric singlets which we will speak about shortly.

This procedure can be repeated for bras. It goes in reverse direction, however, and one starts with the bras of the eigenstates for H^(D)\hat{H}^{(D)}, which are degree zero differential forms. 101010Dropping the bra-ket notations, if the ket of an eigenstate ψα∈Ω(k)\psi\_{\alpha}\in\Omega^{(k)}, then its bra ψ¯α∈Ω(D−k)\bar{\psi}\_{\alpha}\in\Omega^{(D-k)}. Subsequently acting by d^\hat{d} from the right, we obtain the pairs of bras such as ⟨α′|,⟨α|=⟨α′|​d^\langle\alpha^{\prime}|,\langle\alpha|=\langle\alpha^{\prime}|\hat{d}. They are the bras of the corresponding kets, and their normalization takes the form ⟨α′|α′⟩=⟨α|α⟩=⟨α′|d^|α⟩=1\langle\alpha^{\prime}|\alpha^{\prime}\rangle=\langle\alpha|\alpha\rangle=\langle\alpha^{\prime}|\hat{d}|\alpha\rangle=1. In this manner, each doublet can be defined via a single bra-ket pair, ⟨α~|\langle\tilde{\alpha}| and |α~⟩|\tilde{\alpha}\rangle, such that

|  |  |  |  |
| --- | --- | --- | --- |
| (2.27) |  | |α⟩=|α~⟩,⟨α|=⟨α~|d^, and |α′⟩=d^​|α~⟩,⟨α′|=⟨α~|,\displaystyle|\alpha\rangle=|\tilde{\alpha}\rangle,\langle\alpha|=\langle\tilde{\alpha}|\hat{d},\text{ and }\;|\alpha^{\prime}\rangle=\hat{d}|\tilde{\alpha}\rangle,\langle\alpha^{\prime}|=\langle\tilde{\alpha}|, |  |

and the orthogonality property reads,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.28) |  | ⟨α~|β~⟩=0,⟨α~|d^|β~⟩=δα~​β~.\displaystyle\langle\tilde{\alpha}|\tilde{\beta}\rangle=0,\langle\tilde{\alpha}|\hat{d}|\tilde{\beta}\rangle=\delta\_{\tilde{\alpha}\tilde{\beta}}. |  |

![Refer to caption](Spectra.png)


Figure 2.  The three possible types of GTO spectra (a,b,c) for a stochastic DS with X=𝕊3X=\mathbb{S}^{3}. Each row (k=0,…​3k=0,...3) contains three graphs representing spec​H(k)\text{spec}H^{(k)} for the three different types of spectra. Dots at the origin for k=0k=0 and k=3k=3 indicate the supersymmetric eigenstates from the zeroth and the third de Rham cohomologies of XX. In cases b and c, the ground states (crosses) are non-supersymmetric doublets, as they possess non-zero eigenvalues, signifying spontaneous breakdown of TS. Additionally, in case c, the pseudo-time reversal symmetry is also broken. The vertical arrowed curves illustrate the action of the TS operator.

#### 2.4.4. Supersymmetric singlets

As we already mentioned, the only eigenstates that are not paired up into non-supersymmetric doublets by the above procedure are those from de Rham cohomology. Due to the completeness of the eigensystem, each de Rham cohomology class contributes one supersymmetric ”singlet.” The bra and ket of each such eigenstate satisfy d^​|θ⟩=0,⟨θ|​d^=0\hat{d}|\theta\rangle=0,\langle\theta|\hat{d}=0. This means, particularly, that the expectation value of any d^\hat{d}-exact operator vanishes, ⟨θ|[d^,a^]|θ⟩=0,∀a^\langle\theta|[\hat{d},\hat{a}]|\theta\rangle=0,\forall\hat{a}. Since H^\hat{H} is d^\hat{d}-exact (see Eq.[2.18](https://arxiv.org/html/2512.21539v1#S2.E18 "In 2.3. Topological supersymmetry ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), all supersymmetric singlets have zero eigenvalue.

Summing up the properties of the eigensystem discussed so far, the resolution of unity on Ω\Omega can now be expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.29) |  | 1^Ω=∑θ|θ⟩​⟨θ|+∑β~(d^​|β~⟩​⟨β~|+|β~⟩​⟨β~|​d^)\displaystyle\hat{1}\_{\Omega}=\sum\nolimits\_{\theta}|\theta\rangle\langle\theta|+\sum\nolimits\_{\tilde{\beta}}\left(\hat{d}|\tilde{\beta}\rangle\langle\tilde{\beta}|+|\tilde{\beta}\rangle\langle\tilde{\beta}|\hat{d}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | +∑γ~,±(d^|γ~,±⟩⟨γ~,±|+|γ~,±⟩⟨γ~,±|d^),\displaystyle+\sum\nolimits\_{\tilde{\gamma},\pm}\left(\hat{d}|\tilde{\gamma},\pm\rangle\langle\tilde{\gamma},\pm|+|\tilde{\gamma},\pm\rangle\langle\tilde{\gamma},\pm|\hat{d}\right), |  |

where θ\theta, β~\tilde{\beta}, and γ~,±\tilde{\gamma},\pm run over the supersymmetric singlets and non-supersymmetric doublets with the real and complex-conjugate eigenvalues, respectively. The operator d¯^\hat{\bar{d}} from Eq.([2.18](https://arxiv.org/html/2512.21539v1#S2.E18 "In 2.3. Topological supersymmetry ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) can be expressed, up to a d^\hat{d}-exact piece which does not change the GTO, H^=[d^,d¯^+[d^,a^]]=[d^,d¯^]\hat{H}=[\hat{d},\hat{\bar{d}}+[\hat{d},\hat{a}]]=[\hat{d},\hat{\bar{d}}], as,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.30) |  | d¯^=∑β~|β~⟩Hβ~⟨β~|+∑γ~,±|γ~,±⟩Hγ~,±⟨γ~,±|,\displaystyle\hat{\bar{d}}=\sum\nolimits\_{\tilde{\beta}}|\tilde{\beta}\rangle H\_{\tilde{\beta}}\langle\tilde{\beta}|+\sum\nolimits\_{\tilde{\gamma},\pm}|\tilde{\gamma},\pm\rangle H\_{\tilde{\gamma},\pm}\langle\tilde{\gamma},\pm|, |  |

where Hβ~=Hβ~∗,Hγ~,±=Hγ~,∓∗H\_{\tilde{\beta}}=H\_{\tilde{\beta}}^{\*},H\_{\tilde{\gamma},\pm}=H\_{\tilde{\gamma},\mp}^{\*}.

#### 2.4.5. Ergodic zero

The zero eigenvalue supersymmetric eigenstate of H^(D)\hat{H}^{(D)}, the existence of which is topologically protected by the requirement of the completeness of the eigensystem of GTO, is always the ”ground state” of H^(D)\hat{H}^{(D)},

|  |  |  |  |
| --- | --- | --- | --- |
| (2.31) |  | min Re​(spec⁡H^(D))=0.\displaystyle\text{min Re}(\operatorname{spec}\hat{H}^{(D)})=0. |  |

Therefore, any probability distribution evolves into this steady-state probability distribution, known also as ”erdogic zero” or invariant measure. [CarrascoRodriguezHertz2021]

To prove this statement, we first observe that a probability distribution, with the property of being positive everywhere on XX, will retain this property throughout its evolution. Indeed, this property is preserved by the pullback induced by any diffeomorphism: the pullback involves the transformation of variables within a positive function, followed by multiplication by the Jacobian of the variable transformation, which is also positive as all diffeomorphism preserve orientation. Consequently, this property is also preserved by a pullback averaged over noise, i.e., by the GTO.

Lets assume that, in contradiction with Eq.([2.31](https://arxiv.org/html/2512.21539v1#S2.E31 "In 2.4.5. Ergodic zero ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")),

|  |  |  |  |
| --- | --- | --- | --- |
| (2.32) |  | Δ(D)=−min Re​(spec⁡H^(D))>0.\displaystyle\Delta^{(D)}=-\text{min Re}(\operatorname{spec}\hat{H}^{(D)})>0. |  |

Then, there is either a pair of eigenstates with complex conjugate eigenvalues such that Re ​Hα=−Δ(D)\text{Re }H\_{\alpha}=-\Delta^{(D)} or a single eigenstate with a real eigenvalue, Hα=−Δ(D)H\_{\alpha}=-\Delta^{(D)}.

In the first case, an everywhere-positive probability distribution, P∈Ω(D)P\in\Omega^{(D)}, will eventually begin to oscillate at sufficiently large times when its temporal evolution,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.33) |  | P​(t)=∑α,kα=De−t​Hα​cα​ψα,cα=∫Xψ¯α∧P​(0),\displaystyle P(t)=\sum\_{\alpha,k\_{\alpha}=D}e^{-tH\_{\alpha}}c\_{\alpha}\psi\_{\alpha},\;c\_{\alpha}=\int\_{X}\bar{\psi}\_{\alpha}\wedge P(0), |  |

is dominated by the fastest growing pair of eigenstates with complex conjugate eigenvalues. This contradicts that P​(t)P(t) must be everywhere positive on XX.

In the second case, lets note that all non-supersymmetric eigenstates with non-zero eigenvalue from Ω(D)\Omega^{(D)} are d^\hat{d}-exact. Indeed, H^​ψα=[d^,d¯^]​ψα=d^​d¯^​ψα=Hα​ψα\hat{H}\psi\_{\alpha}=[\hat{d},\hat{\bar{d}}]\psi\_{\alpha}=\hat{d}\hat{\bar{d}}\psi\_{\alpha}=H\_{\alpha}\psi\_{\alpha}, where we used that d^​ψα=0\hat{d}\psi\_{\alpha}=0 because ψα∈Ω(D)\psi\_{\alpha}\in\Omega^{(D)}. Therefore, ψα=d^​ψ~α\psi\_{\alpha}=\hat{d}\tilde{\psi}\_{\alpha} with ψ~=d¯^​ψα/Hα\tilde{\psi}=\hat{\bar{d}}\psi\_{\alpha}/H\_{\alpha}. This further implies that ∫Xψα=∫Xd^​ψ~α=0\int\_{X}\psi\_{\alpha}=\int\_{X}\hat{d}\tilde{\psi}\_{\alpha}=0. Consequently, all non-supersymmetric eigenstates are negative somewhere on XX. In result, Eq.([2.33](https://arxiv.org/html/2512.21539v1#S2.E33 "In 2.4.5. Ergodic zero ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) will take on negative values somewhere on XX at sufficiently large times when the contribution from the fastest growing non-supersymmetric eigenstate dominates P​(t)P(t). Therefore, Eq.([2.32](https://arxiv.org/html/2512.21539v1#S2.E32 "In 2.4.5. Ergodic zero ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) is not realizable, which proves Eq.([2.31](https://arxiv.org/html/2512.21539v1#S2.E31 "In 2.4.5. Ergodic zero ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")).

#### 2.4.6. Stochastic Poincare-Bendixson theorem

The property ([2.31](https://arxiv.org/html/2512.21539v1#S2.E31 "In 2.4.5. Ergodic zero ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) also holds for H^(0)\hat{H}^{(0)} which is isospectral with H^(D)\hat{H}^{(D)} (see Ref.[OvcEntropy]). This leads to conclusion that the spontaneous TS breaking is not possible for models with dimX<3\dim X<3: there is simply no room for a non-supersymmetric pair of eigenstates with degrees differing by unity and with a real part of their eigenvalue being negative unless the dimensionality of the phase space is 3 or higher. This statement can be looked upon as a STS proof of the stochastic Poincare-Bendixson theorem. [Stochastic\_PB\_theorem]

This may be a good moment to comment on the applicability of STS to random discrete-time dynamical systems. For such systems defined by maps that are diffeomorphisms, most conclusions drawn for SDEs remain directly applicable. If, however, the maps are not diffeomorphisms, a qualitatively new situation may arise.[Max\_2019] In particular, the TS symmetry operator may fail to commute with the evolution operator from the outset. This corresponds to what is known in theoretical physics as explicit symmetry breaking. All textbook examples of chaos with dimensionality lower than that allowed by the Poincaré–Bendixson theorem (dimX<3\dim X<3) fall into this category. Explicit symmetry breaking is qualitatively different from spontaneous symmetry breaking: in particular, the Goldstone theorem does not apply to explicit symmetry breaking. To the best of the present author’s knowledge, STS is the only theoretical framework that provides such a qualitative distinction between discrete-time and continuous-time chaos. Perhaps, this distinction merits further investigation which, however, goes beyond the scope of this paper.

### 2.5. Stochastic chaos

From the DS theory viewpoint, dynamics can be characterized as chaotic if the spectral radius of the finite-time GTO is larger than unity. Under this condition, the partition function,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.34) |  | Zt​t′=Tr ​ℳ^t​t′=∑αe−(t−t′)​Hα,\displaystyle Z\_{tt^{\prime}}=\text{Tr }\hat{\mathcal{M}}\_{tt^{\prime}}=\sum\nolimits\_{\alpha}e^{-(t-t^{\prime})H\_{\alpha}}, |  |

grows exponentially in the limit of infinitely long evolution signaling the exponential growth of the number of closed solutions – the hallmark of chaotic dynamics. This condition can be expressed as,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.35) |  | Δ=−minα⁡Re ​Hα>0,\displaystyle\Delta=-\min\nolimits\_{\alpha}\text{Re }H\_{\alpha}>0, |  |

where Δ\Delta is the rate of the exponential growth called ”pressure”. [Rue02] It can be viewed as a random DS theory version of the family of dynamical entropies including topological entropy [Handbook\_of\_DS, book\_hyperbolic\_flows] related, via Pesin formula, [Pesin] to (stochastic) Lyapunov exponents. [Arn03]

Spectra b and c in the Fig.[2](https://arxiv.org/html/2512.21539v1#S2.F2 "Figure 2 ‣ 2.4.3. Non-supersymmetric doublets ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") satisfy condition ([2.35](https://arxiv.org/html/2512.21539v1#S2.E35 "In 2.5. Stochastic chaos ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")). A practical example of spectrum of type b is the geodesic flow on a compact manifold of variable negative curvature. [Rue02, Anosov\_geodesic\_flows] An example of type c spectrum is the kinematic dynamo, where the galactic magnetic field not only grows but also rotates. [Torsten]

When condition ([2.35](https://arxiv.org/html/2512.21539v1#S2.E35 "In 2.5. Stochastic chaos ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) is satisfied, the contribution into the partition function from the ”erdogic zero” in Sec.([2.4.5](https://arxiv.org/html/2512.21539v1#S2.SS4.SSS5 "2.4.5. Ergodic zero ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) is negligible in the long-time limit because it has a zero eigenvalue. This means that this state cannot represent the DS in the long-time limit, implying that investigating ”ergodic zero” may not be the best way to explore chaos. The main contribution actually comes from the eigenstates with nontrivial degrees, k≠0,Dk\neq 0,D, because of Eq.([2.31](https://arxiv.org/html/2512.21539v1#S2.E31 "In 2.4.5. Ergodic zero ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")). Getting a bit ahead, this foreshadows the high-energy physics picture that the spontaneous TS breaking leads to the emergence of a Dirac/Fermi sea of fermions.

It should also be noted that for compact XX, the existence of zero-eigenvalue supersymmetric states is topologically protected—the Hilbert space would simply be incomplete in their absence. Consequently, situations in which the ‘pressure’ becomes negative cannot occur. For non-compact XX, however, the situation may differ: the absence of zero-eigenvalue supersymmetric states could be associated with issues of normalizability. This question merits further investigation, which lies beyond the scope of the present work.

While alternative definitions of stochastic chaos may exist, positive pressure offers a significant advantage. Within this definition, the ground state of the model, which is (one of) the fastest growing eigenstates of the GTO, has a nonzero eigenvalue and is therefore non-supersymmetric. By definition, this implies the spontaneous breakdown of TS. As a result, positive pressure makes a good physical sense and it has a potential, via the Goldstone theorem, to explain the experimental signature of chaotic behavior known as 1/f noise as discussed in Sec.[5](https://arxiv.org/html/2512.21539v1#S5 "5. Self-sustained dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") below.

### 2.6. Sharp trace

Another key quantity is the *sharp* trace of the GTO,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.36) |  | W=T​r​(−1)k^​ℳ^t​t′=∑α(−1)kα​e−(t−t′)​Hα,\displaystyle W=Tr(-1)^{\hat{k}}\hat{\mathcal{M}}\_{tt^{\prime}}=\sum\nolimits\_{\alpha}(-1)^{k\_{\alpha}}e^{-(t-t^{\prime})H\_{\alpha}}, |  |

where k^\hat{k} and kαk\_{\alpha} are defined in Eq.([2.25](https://arxiv.org/html/2512.21539v1#S2.E25 "In 2.4.2. Conservation of fermions ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")). This quantity is a fundamental object of topological nature known in physics as the Witten index.

For a non-supersymmetric doublet, the degrees of the paired eigenstates differ by unity. As a result, their contributions cancel out, leaving only supersymmetric singlets to contribute to the sharp trace. This leads to the expression:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.37) |  | W=∑k=0D(−1)k​Bk=E​u.C​h​(X),\displaystyle W=\sum\nolimits\_{k=0}^{D}(-1)^{k}B\_{k}=Eu.Ch(X), |  |

where E​u.C​h.Eu.Ch. denotes the Euler characteristic of XX and BkB\_{k} is the Betti number, which counts the number of supersymmetric singlets of degree kk.

![Refer to caption](Pathintegral.png)


Figure 3.  Pathintegral is a continuous-time limit, N→∞,Δ​τ=(t−t′)/N→0N\to\infty,\Delta\tau=(t-t^{\prime})/N\to 0, of the discrete time evolution picture: the domain of temporal evolution, (t,t′)(t,t^{\prime}), is split into NN time steps and the time takes on discrete values τN,τN−1,…​τ1,τ0\tau\_{N},\tau\_{N-1},...\tau\_{1},\tau\_{0}, t=τN,t′=τ0t=\tau\_{N},t^{\prime}=\tau\_{0}. Each time slice hosts a supersymmetric pair of fields xk,χkx\_{k},\chi\_{k}, and each dual slice hosts the corresponding supersymmetric pair of momenta fields, Bk,χ¯kB\_{k},\bar{\chi}\_{k}, along with the noise variable, ξk\xi\_{k}. The finite-time stochastic evolution operator is derived by integrating out all the fields except those at the first and last slices. Its exact expression depends on parameter α∈(0,1)\alpha\in(0,1), which dictates how xx and χ\chi are interpreted at the dual slice, τk\tau\_{k}: α​xk+(1−α)​xk−1\alpha x\_{k}+(1-\alpha)x\_{k-1}. Only for α=1/2\alpha=1/2, corresponding to the Stratonovich interpretation of SDEs, does the stochastic evolution operator matches the generalized transfer operator of the DS theory, thereby having a clear-cut mathematical meaning of the pullback averaged over noise.

## 3. Pathintegral representation of stochastic dynamics

### 3.1. Stochastic differential equations

In terms of the traditional theory of SDEs, Eq.([2.1](https://arxiv.org/html/2512.21539v1#S2.E1 "In 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) with the Gaussian white noise can be expressed as,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.1) |  | d​x​(t)=F​(x​(t))​d​t+(2​Θ)​Ga​(x​(t))∘d​Wa​(t),\displaystyle\mathrm{d}x(t)=F(x(t))\mathrm{d}t+(2\Theta)G\_{a}(x(t))\circ\mathrm{d}W^{a}(t), |  |

where Wa​(t)W^{a}(t) is the Wiener process, a function whose derivative over time is the Gaussian white noise, and symbol ∘\circ indicates that this is a Stratonovich SDE. (see, e.g., Ref.[Oks10] and Refs. therein) While notations in Eq. ([3.1](https://arxiv.org/html/2512.21539v1#S3.E1 "In 3.1. Stochastic differential equations ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) may seem like time is continuous, there is an important subtlety: in the traditional theory of SDEs, stochastic dynamics is understood as a continuous-time limit of a discrete-time evolution, and this limit is taken only after averaging over the noise configurations (see Sec.[3.4](https://arxiv.org/html/2512.21539v1#S3.SS4 "3.4. Ito-Stratonovich dilemma ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") below).

The discrete-time evolution picture of stochastic dynamics, assumed in Eq.([3.1](https://arxiv.org/html/2512.21539v1#S3.E1 "In 3.1. Stochastic differential equations ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), naturally aligns with numerical implementations of SDEs, as it formalizes a Runge-Kutta propagation scheme (augmented by stochastic noise). Furthermore, it is the basis for the pathintegral representation of stochastic dynamics, obtained through functional integration over trajectories. This formulation is the central focus of this section.

The discrete-time picture of evolution (see Fig. [3](https://arxiv.org/html/2512.21539v1#S2.F3 "Figure 3 ‣ 2.6. Sharp trace ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) is constructed by dividing the temporal domain into a large number, NN, of time steps, forming a discrete lattice of time points, τk=τ0+k​Δ​τ\tau\_{k}=\tau\_{0}+k\Delta\tau, where Δ​τ=(t−t′)/N\Delta\tau=(t-t^{\prime})/N is assumed to be vanishingly small but still finite. The discrete-time counterpart of Eq.([2.1](https://arxiv.org/html/2512.21539v1#S2.E1 "In 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) is, 111111Unlike Eq.([2.1](https://arxiv.org/html/2512.21539v1#S2.E1 "In 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), Eq.([3.2](https://arxiv.org/html/2512.21539v1#S3.E2 "In 3.1. Stochastic differential equations ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) may look suspicious for nonlinear XX’s because one cannot subtract points in a nonlinear space. The way around this subtlety is to believe that xx’s are not the points themselves but are their coordinates within some coordinate neighborhood. This may raise concerns about potential loss of coordinate independence of the so-obtained description. In the continuous-time limit, however, the coordinate independence is restored (see Eq.([3.24](https://arxiv.org/html/2512.21539v1#S3.E24 "In 3.3. Stochastic evolution operator ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) below).

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | xk−xk−1=ℱ​(x~k,ξk)​Δ​τ,\displaystyle x\_{k}-x\_{k-1}={\mathscr{F}}(\tilde{x}\_{k},\xi\_{k})\Delta\tau, |  |

where the discrete-time version of the Gaussian white noise can be defined by the following probability distribution,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.3) |  | P​(ξ)=(c​(Δ​τ))N​e−∑k=1NΔ​τ​(ξk)2/2,\displaystyle P(\xi)=(c(\Delta\tau))^{N}e^{-\sum\_{k=1}^{N}\Delta\tau(\xi\_{k})^{2}/2}, |  |

with c​(Δ​τ)=(Δ​τ/2​π)D/2c(\Delta\tau)=(\Delta\tau/2\pi)^{D/2} being the normalization constant, such that,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.4) |  | ∫∏k=1NP​(ξ)​dD​ξk=1,\displaystyle\int\prod\_{k=1}^{N}P(\xi)\mathrm{d}^{D}\xi\_{k}=1, |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (3.5) |  | ∫∏k=1Nξla​ξmb​P​(ξ)​dD​ξk=δl​m​δa​b/Δ​τ.\displaystyle\int\prod\_{k=1}^{N}\xi^{a}\_{l}\xi^{b}\_{m}P(\xi)\mathrm{d}^{D}\xi\_{k}=\delta\_{lm}\delta^{ab}/\Delta\tau. |  |

In Eq.([3.2](https://arxiv.org/html/2512.21539v1#S3.E2 "In 3.1. Stochastic differential equations ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), x~k=α​xk+(1−α)​xk−1\tilde{x}\_{k}=\alpha x\_{k}+(1-\alpha)x\_{k-1} is an α\alpha-family of approximations for xx during the kt​hk^{th} time step. Different choices of α\alpha correspond to different ”interpretations” of SDEs, with α=0,1/2,1\alpha=0,1/2,1 representing the Ito, Stratonovich, and Kolmogorov interpretations, respectively. [Oks10]

The functional integration over noise variables can be defined as,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.6) |  | ⟨1⟩noise=∬𝒫​(ξ)​𝒟​ξ​=def​limN→∞∏k=1N∫P​(ξ)​dD​ξk=1,\displaystyle\langle 1\rangle\_{\text{noise}}=\iint{\mathcal{P}}(\xi){\mathcal{D}}\xi\overset{\text{def}}{=}\lim\_{N\to\infty}\prod\_{k=1}^{N}\int P(\xi)\mathrm{d}^{D}\xi\_{k}=1, |  |

where the probability functional 𝒫​(ξ)=e−∫t′tdτ​ξ2​(τ)/2{\mathcal{P}}(\xi)=e^{-\int\_{t^{\prime}}^{t}\mathrm{d}\tau\xi^{2}(\tau)/2} and the normalization factors c​(Δ​τ)c(\Delta\tau) are absorbed into the functional differential, 𝒟​ξ{\mathcal{D}}\xi, for convenience.

### 3.2. Parisi-Sourlas approach as a BRST gauge-fixing

One interpretation of the Parisi–Sourlas approach to SDEs is that it rewrites the partition function of the noise in terms of the model’s dynamical variables using the BRST gauge-fixing procedure. [TFT\_BOOK] This approach begins with the formal introduction of the dynamical variables into the partition function of the noise as,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.7) |  | ∬𝒫​(ξ)​𝒟​ξ→∬p.b.c𝒫​(ξ)​𝒟​ξ​𝒟​x,\displaystyle\iint{\mathcal{P}}(\xi){\mathcal{D}}\xi\to\iint\_{p.b.c}{\mathcal{P}}(\xi){\mathcal{D}}\xi{\mathcal{D}}x, |  |

where the functional integration goes over closed paths or paths with periodic boundary conditions (p.b.c),

|  |  |  |  |
| --- | --- | --- | --- |
| (3.8) |  | ∬p.b.c𝒟​x​=def​limN→∞∏k=1N∫XdD​xk.\displaystyle\iint\_{p.b.c}{\mathcal{D}}x\overset{\text{def}}{=}\lim\nolimits\_{N\to\infty}\prod\nolimits\_{k=1}^{N}\int\_{X}\mathrm{d}^{D}x\_{k}. |  |

and there is no need to integrate over x0x\_{0} because the p.b.c. assume x0=xNx\_{0}=x\_{N}. 121212Rewriting the noise partition function in terms of dynamical variables can be viewed as a change of integration variables within the noise partition function. If this transformation is expected to yield a scalar quantity – rather than an operator, as in Sec.[3.3](https://arxiv.org/html/2512.21539v1#S3.SS3 "3.3. Stochastic evolution operator ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") below – then the numbers of ξ\xi’s and xx’s must be the same. This is the reason for using the p.b.c.

At this stage, the right-hand side of Eq.([3.7](https://arxiv.org/html/2512.21539v1#S3.E7 "In 3.2. Parisi-Sourlas approach as a BRST gauge-fixing ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), though not well-defined and technically infinite, can be interpreted as a redundant theory of the noise. Its ”action” is independent of xx. This independence can be viewed as a local symmetry with respect to continuous deformations of the paths. This symmetry can be gauge-fixed using the SDE as a gauge condition, [Henneaux1992] leading to the following pathintegral representation of the Witten index:

|  |  |  |  |
| --- | --- | --- | --- |
| (3.9) |  | W=∬p.b.cJ(ξ)(∏τδD((x˙(τ)−ℱ(x(τ),ξ(τ))dτ))𝒫(ξ)𝒟ξ𝒟x.\displaystyle W=\iint\_{p.b.c}J(\xi)\bigg(\prod\nolimits\_{\tau}\delta^{D}\bigg(\Big(\dot{x}(\tau)-{\mathscr{F}}(x(\tau),\xi(\tau)\Big)\mathrm{d}\tau\bigg)\bigg){\mathcal{P}}(\xi){\mathcal{D}}\xi{\mathcal{D}}x. |  |

Here, the δ\delta-functional is introduced to limit the functional integration only to solutions of the SDE:131313In this section, one may assume x~k=xk\tilde{x}\_{k}=x\_{k} since the dependence on α\alpha disappears in the pathintegral representation of stochastic dynamics. It will reemerge later, when we transition further into the operator representation in Sec.[3.3](https://arxiv.org/html/2512.21539v1#S3.SS3 "3.3. Stochastic evolution operator ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry").

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | limN→∞∏k=1NδD​(M​(ξk)tk−1​tk​(xk)−xk−1)\displaystyle\lim\_{N\to\infty}\prod\nolimits\_{k=1}^{N}\delta^{D}(M(\xi\_{k})\_{t\_{k-1}t\_{k}}(x\_{k})-x\_{k-1}) |  |
|  |  | =\displaystyle= | limN→∞∏k=1NδD​(((xk−xk−1)/Δ​τ−ℱ​(xk,ξk))​Δ​τ)\displaystyle\lim\_{N\to\infty}\prod\nolimits\_{k=1}^{N}\delta^{D}\bigg(\Big((x\_{k}-x\_{k-1})/\Delta\tau-{\mathscr{F}}(x\_{k},\xi\_{k})\Big)\Delta\tau\bigg) |  |
|  |  | =def\displaystyle\overset{\text{def}}{=} | ∏τδD​((x˙​(τ)−ℱ​(x​(τ),ξ​(τ)))​d​τ),\displaystyle\prod\nolimits\_{\tau}\delta^{D}\bigg(\Big(\dot{x}(\tau)-{\mathscr{F}}(x(\tau),\xi(\tau))\Big)\mathrm{d}\tau\bigg), |  |

where the single time-step map M​(ξk)tk−1​tk​(xk)=xk−Δ​τ​ℱ​(xk,ξk)+…M(\xi\_{k})\_{t\_{k-1}t\_{k}}(x\_{k})=x\_{k}-\Delta\tau{\mathscr{F}}(x\_{k},\xi\_{k})+.... Notation J​(ξ)J(\xi) in Eq.([3.9](https://arxiv.org/html/2512.21539v1#S3.E9 "In 3.2. Parisi-Sourlas approach as a BRST gauge-fixing ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) stands for the functional Jacobian, introduced to compensate, up to a sign, for the functional determinant that emerges when integrating out bosonic delta-functionals in ([3.2](https://arxiv.org/html/2512.21539v1#S3.Ex2 "3.2. Parisi-Sourlas approach as a BRST gauge-fixing ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) in a way which is a functional generalization of, ∫g​(y)​δl​(m​(y))​dl​y=∑yi,m​(yi)=0g​(yi)/|J​(yi)|\int g(y)\delta^{l}(m(y))\mathrm{d}^{l}y=\sum\_{y\_{i},m(y\_{i})=0}g(y\_{i})/|J(y\_{i})|, where y∈ℝly\in\mathbb{R}^{l}, m:ℝl→ℝlm:\mathbb{R}^{l}\to\mathbb{R}^{l}, and J​(y)=det(i​j)∂mi​(y)/∂yjJ(y)=\det\_{(ij)}\partial m^{i}(y)/\partial y^{j} is the Jacobian of mm. This functional Jacobian can be defined as,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J​(ξ)\displaystyle J(\xi) | =\displaystyle= | limN→∞det(k​k′)(∂(M​(ξk)tk−1​tk​(xk)−xk−1)/∂xk′)\displaystyle\lim\_{N\to\infty}\det\_{(kk^{\prime})}\Big(\partial(M(\xi\_{k})\_{t\_{k-1}t\_{k}}(x\_{k})-x\_{k-1})/\partial x\_{k^{\prime}}\Big) |  |
|  |  | =\displaystyle= | limN→∞∏k=1NδD​((∂(M​(ξk)tk−1​tk​(xk)−xk−1)/∂xk′)​χk′)​dD​χk\displaystyle\lim\_{N\to\infty}\prod\_{k=1}^{N}\delta^{D}\bigg(\Big(\partial\big(M(\xi\_{k})\_{t\_{k-1}t\_{k}}(x\_{k})-x\_{k-1}\big)/\partial x\_{k^{\prime}}\Big)\chi\_{k^{\prime}}\bigg)\mathrm{d}^{D}\chi\_{k} |  |
|  |  | =\displaystyle= | limN→∞∏k=1NδD​(T​M​(ξk)tk−1​tk​(xk)​χk−χk−1)​dD​χk\displaystyle\lim\_{N\to\infty}\prod\_{k=1}^{N}\delta^{D}(TM(\xi\_{k})\_{t\_{k-1}t\_{k}}(x\_{k})\chi\_{k}-\chi\_{k-1})\mathrm{d}^{D}\chi\_{k} |  |
|  |  | =\displaystyle= | limN→∞∏k=1NδD​(((χk−χk−1)/Δ​τ−T​ℱ​(xk,ξk)​χk)​Δ​τ)​dD​χk\displaystyle\lim\_{N\to\infty}\prod\_{k=1}^{N}\delta^{D}\Big(\Big((\chi\_{k}-\chi\_{k-1})/\Delta\tau-T{\mathscr{F}}(x\_{k},\xi\_{k})\chi\_{k}\Big)\Delta\tau\Big)\mathrm{d}^{D}\chi\_{k} |  |
|  |  | =def\displaystyle\overset{\text{def}}{=} | ∏τδD​((χ˙​(τ)−T​ℱ​(x​(τ),ξ​(τ))​χ​(τ))​d​τ)​𝒟​χ,\displaystyle\prod\_{\tau}\delta^{D}\bigg(\Big(\dot{\chi}(\tau)-T{\mathscr{F}}(x(\tau),\xi(\tau))\chi(\tau)\Big)\mathrm{d}\tau\bigg){\mathcal{D}}\chi, |  |

where T​M​(x)=∂M​(x)/∂xTM(x)=\partial M(x)/\partial x is the tangent map and T​ℱ​(x)=∂ℱ​(x)/∂xT{\mathscr{F}}(x)=\partial{\mathscr{F}}(x)/\partial x. The additional field χ∈T​X\chi\in TX is a Grassmann variable known as the Faddeev-Popov ghost. [Faddeev1967] It has been introduced to make use of one of the key properties of Grassmann numbers: ∫δ​(A^i11​χi1)​…​δ​(A^ill​χil)​dl​χ​=def​∫δl​(A^​χ)​dl​χ=det(i​j)Aji\int\delta(\hat{A}^{1}\_{i\_{1}}\chi^{i\_{1}})...\delta(\hat{A}^{l}\_{i\_{l}}\chi^{i\_{l}})\mathrm{d}^{l}\chi\overset{\text{def}}{=}\int\delta^{l}(\hat{A}\chi)\mathrm{d}^{l}\chi=\det\_{(ij)}A^{i}\_{j}, where AA is a square l×ll\times l matrix (see, e.g., Ref.[DeWitt\_1992]). Its functional differential is defined as 𝒟​χ=limN→∞∏k=1NdD​χk{\mathcal{D}}\chi=\lim\_{N\to\infty}\prod\_{k=1}^{N}\mathrm{d}^{D}\chi\_{k}.

The next step is to introduce momenta fields: the bosonic, BB, and fermionic, χ¯\bar{\chi}, both defined on the dual time slices (see Fig.[3](https://arxiv.org/html/2512.21539v1#S2.F3 "Figure 3 ‣ 2.6. Sharp trace ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) and belonging to the cotangent space of XX. These additional fields are needed to exponentiate the δ\delta-functionals in the way, which is a functional generalization of δ​(f​(x))=∫ei​B​f​(x)​dB/2​π\delta(f(x))=\int e^{iBf(x)}\mathrm{d}B/2\pi and its fermionic counterpart, δl​(A^​χ)=∫eχ¯i​Aji​χj​dl​χ¯\delta^{l}(\hat{A}\chi)=\int e^{\bar{\chi}\_{i}A^{i}\_{j}\chi^{j}}\mathrm{d}^{l}\bar{\chi}. With their help,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.12) |  | ∏τδD​((x˙​(τ)−ℱ​(x​(τ),ξ​(τ)))​d​τ)=∬ei​∫t′tB​(x˙−ℱ​(x,ξ))​dτ​𝒟​B,\displaystyle\prod\nolimits\_{\tau}\delta^{D}\bigg(\Big(\dot{x}(\tau)-{\mathscr{F}}(x(\tau),\xi(\tau))\Big)\mathrm{d}\tau\bigg)=\iint e^{i\int\_{t^{\prime}}^{t}B(\dot{x}-{\mathscr{F}}(x,\xi))\mathrm{d}\tau}{\mathcal{D}}B, |  |

where the integration measure is defined as 𝒟​B​=def​limN→∞∏k=1NdD​Bk/(2​π)D{\mathcal{D}}B\overset{\text{def}}{=}\lim\_{N\to\infty}\prod\_{k=1}^{N}\mathrm{d}^{D}B\_{k}/(2\pi)^{D}, and similarly,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J​(ξ)\displaystyle J(\xi) | =\displaystyle= | ∏τδD​((χ˙​(τ)−T​ℱ​(x​(τ),ξ​(τ))​χ​(τ))​d​τ)​𝒟​χ\displaystyle\prod\_{\tau}\delta^{D}\bigg(\Big(\dot{\chi}(\tau)-T{\mathscr{F}}(x(\tau),\xi(\tau))\chi(\tau)\Big)\mathrm{d}\tau\bigg){\mathcal{D}}\chi |  |
|  |  | =\displaystyle= | ∬e−i​∫t′tχ¯​(χ˙−T​ℱ​(x,ξ)​χ)​dτ​𝒟​χ¯​𝒟​χ,\displaystyle\iint e^{-i\int\_{t^{\prime}}^{t}\bar{\chi}(\dot{\chi}-T{\mathscr{F}}(x,\xi)\chi)\mathrm{d}\tau}{\mathcal{D}}\bar{\chi}{\mathcal{D}}\chi, |  |

with 𝒟​χ¯​=def​limN→∞∏k=1NdD​χ¯k{\mathcal{D}}\bar{\chi}\overset{\text{def}}{=}\lim\_{N\to\infty}\prod\_{k=1}^{N}\mathrm{d}^{D}\bar{\chi}\_{k}.141414Strictly speaking, the differential also has the factor (−i)D​N(-i)^{DN}, but one can always think that N=4​k,k∈NN=4k,k\in N.

An important observation is that the product of the bosonic δ\delta-functional ([3.12](https://arxiv.org/html/2512.21539v1#S3.E12 "In 3.2. Parisi-Sourlas approach as a BRST gauge-fixing ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) and the functional Jacobian ([3.2](https://arxiv.org/html/2512.21539v1#S3.Ex7 "3.2. Parisi-Sourlas approach as a BRST gauge-fixing ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) can be given as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | J​(ξ)​∏τδD​((x˙​(τ)−ℱ​(x​(τ),ξ​(τ)))​d​τ)\displaystyle J(\xi)\prod\nolimits\_{\tau}\delta^{D}\bigg(\Big(\dot{x}(\tau)-{\mathscr{F}}(x(\tau),\xi(\tau))\Big)\mathrm{d}\tau\bigg) |  |
|  |  | =\displaystyle= | ∬ei​∫t′t(B​(x˙−ℱ​(x,ξ))−χ¯​(χ˙−T​ℱ​(x,ξ)​χ))​dτ​𝒟​B​𝒟​χ¯​𝒟​χ\displaystyle\iint e^{i\int\_{t^{\prime}}^{t}\big(B(\dot{x}-{\mathscr{F}}(x,\xi))-\bar{\chi}(\dot{\chi}-T{\mathscr{F}}(x,\xi)\chi)\big)\mathrm{d}\tau}{\mathcal{D}}B{\mathcal{D}}\bar{\chi}{\mathcal{D}}\chi |  |
|  |  | =\displaystyle= | ∬e(Q,Ψ​(Φ,ξ))​𝒟​B​𝒟​χ¯​𝒟​χ,\displaystyle\iint e^{(Q,\Psi(\Phi,\xi))}{\mathcal{D}}B{\mathcal{D}}\bar{\chi}{\mathcal{D}}\chi, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
| (3.15) |  | Ψ​(ξ,Φ)=∫t′ti​χ¯​(x˙​(τ)−ℱ​(x​(τ),ξ​(τ)))​dτ,\displaystyle\Psi(\xi,\Phi)=\int\_{t^{\prime}}^{t}i\bar{\chi}(\dot{x}(\tau)-\mathcal{F}(x(\tau),\xi(\tau)))\mathrm{d}\tau, |  |

is the so-called gauge-fermion, the notation Φ=x​B​χ​χ¯\Phi=xB\chi\bar{\chi} represents the collection of all fields, and

|  |  |  |  |
| --- | --- | --- | --- |
| (3.16) |  | Q=∫t′t(χ​(τ)​δ/δ​x​(τ)+B​(τ)​δ/δ​χ¯​(τ))​dτ,\displaystyle Q=\int\_{t^{\prime}}^{t}\Big(\chi(\tau)\delta/\delta x(\tau)+B(\tau)\delta/\delta\bar{\chi}(\tau)\Big)\mathrm{d}\tau, |  |

is the operator of the BRST symmetry and/or the pathintegral version of TS. [TFT\_BOOK] Eq.([3.2](https://arxiv.org/html/2512.21539v1#S3.Ex9 "3.2. Parisi-Sourlas approach as a BRST gauge-fixing ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) is the core of the BRST gauge fixing procedure, where the gauge-fixing factors – the bosonic delta-functional and the corresponding Jacobian – are represented by an additional QQ-exact piece in the action.

The final step in obtaining the pathintegral representation of the Witten index is to integrate out the noise using the identity, ∬𝒟​ξ​e∫(−ξ2/2+a​ξ)​dτ=e∫𝑑τ​a2/2\iint{\mathcal{D}}\xi e^{\int(-\xi^{2}/2+a\xi)\mathrm{d}\tau}=e^{\int d\tau a^{2}/2}, which leads from Eqs.([3.9](https://arxiv.org/html/2512.21539v1#S3.E9 "In 3.2. Parisi-Sourlas approach as a BRST gauge-fixing ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) and ([3.2](https://arxiv.org/html/2512.21539v1#S3.Ex9 "3.2. Parisi-Sourlas approach as a BRST gauge-fixing ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) to,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.17) |  | W=∬p.b.c.e(Q,Ψ​(ξ,Φ))​𝒫​(ξ)​𝒟​ξ​𝒟​Φ=∬p.b.c.e(Q,Ψ​(Φ))​𝒟​Φ,\displaystyle W=\iint\_{p.b.c.}e^{(Q,\Psi(\xi,\Phi))}{\mathcal{P}}(\xi){\mathcal{D}}\xi{\mathcal{D}}\Phi=\iint\_{p.b.c.}e^{(Q,\Psi(\Phi))}{\mathcal{D}}\Phi, |  |

where the new gauge fermion Ψ=∫t′t(i​χ¯​x˙−d¯)​dτ\Psi=\int\_{t^{\prime}}^{t}(i\bar{\chi}\dot{x}-\bar{d})\mathrm{d}\tau, with d¯=i​χ¯​(F−Θ​Ga​LGa)\bar{d}=i\bar{\chi}(F-\Theta G\_{a}L\_{G\_{a}}) and LGa=(Q,i​χ¯​Ga)L\_{G\_{a}}=(Q,i\bar{\chi}G\_{a}) being the pathintegral versions of operator d¯^\hat{\bar{d}} in Eq.([2.18](https://arxiv.org/html/2512.21539v1#S2.E18 "In 2.3. Topological supersymmetry ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) and the Cartan formula for the Lie derivative ([2.16](https://arxiv.org/html/2512.21539v1#S2.E16 "In 2.3. Topological supersymmetry ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), which follows from the recognition of i​χ¯​Gai\bar{\chi}G\_{a} and QQ as the pathintegral versions of the interior multiplication by GaG\_{a} and the exterior derivative, respectively.

### 3.3. Stochastic evolution operator

The temporal evolution in the model is defined via the stochastic evolution operator (SEO) – the Parisi-Sourlas pathintegral with open boundary conditions:

|  |  |  |  |
| --- | --- | --- | --- |
| (3.18) |  | ∬x​χ​(t′)=x′​χ′x​χ​(t)=x​χe∫t′t(i​B​x˙+i​χ˙​χ¯−H​(Φ))​dτ​𝒟​Φ=⟨x​χ|e−(t−t′)​H^|x′​χ′⟩.\displaystyle\iint\_{{x\chi(t^{\prime})=x^{\prime}\chi^{\prime}}\atop{x\chi(t)=x\chi}}e^{\int\_{t^{\prime}}^{t}(iB\dot{x}+i\dot{\chi}{\bar{\chi}}-H(\Phi))\mathrm{d}\tau}{\mathcal{D}}\Phi=\langle x\chi|e^{-(t-t^{\prime})\hat{H}}|x^{\prime}\chi^{\prime}\rangle. |  |

Here, we used (Q,Ψ​(Φ))=∫t′t(i​B​x˙+i​χ˙​χ¯−H​(Φ))​dτ(Q,\Psi(\Phi))=\int\_{t^{\prime}}^{t}(iB\dot{x}+i\dot{\chi}{\bar{\chi}}-H(\Phi))\mathrm{d}\tau, with H=(Q,d¯​(Φ))H=(Q,\bar{d}(\Phi)), no integration is assumed over the variables on the first and the last time slices (see Fig.[3](https://arxiv.org/html/2512.21539v1#S2.F3 "Figure 3 ‣ 2.6. Sharp trace ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), H^\hat{H} is the SEO in the operator representation, and the basis of the operator representation, where xx and χ\chi are diagonal, is defined as: x^​|x​χ⟩=x​|x​χ⟩,χ^​|x​χ⟩=χ​|x​χ⟩\hat{x}|x\chi\rangle=x|x\chi\rangle,\hat{\chi}|x\chi\rangle=\chi|x\chi\rangle,
⟨x​χ|​x^=⟨x​χ|​x,⟨x​χ|​χ^=⟨x​χ|​χ\langle x\chi|\hat{x}=\langle x\chi|x,\langle x\chi|\hat{\chi}=\langle x\chi|\chi. This basis is complete,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.19) |  | ⟨x​χ|x′​χ′⟩=δD​(x−x′)​δD​(χ−χ′),∫|x​χ⟩​⟨x​χ|​dD​x​dD​χ=1^Ω,\displaystyle\langle x\chi|x^{\prime}\chi^{\prime}\rangle=\delta^{D}(x-x^{\prime})\delta^{D}(\chi-\chi^{\prime}),\;\int|x\chi\rangle\langle x\chi|\mathrm{d}^{D}x\mathrm{d}^{D}\chi=\hat{1}\_{\Omega}, |  |

and any wavefunction can be resolved as,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.20) |  | |ψ⟩=∫ψ​(x​χ)​|x​χ⟩​dD​x​dD​χ​, ​ψ​(x​χ)=⟨x​χ|ψ⟩.\displaystyle|\psi\rangle=\int\psi(x\chi)|x\chi\rangle\mathrm{d}^{D}x\mathrm{d}^{D}\chi\text{, }\psi(x\chi)=\langle x\chi|\psi\rangle. |  |

The explicit form of H^\hat{H} can be derived by considering a single step evolution of a wavefunction in the discrete time picture,

|  |  |  |  |
| --- | --- | --- | --- |
| (3.21) |  | ⟨x​χ|e−Δ​τ​H^|ψ⟩=∫⟨x​χ|e−Δ​τ​H^|y​η⟩​⟨y​η|ψ⟩​dD​y​dD​η\displaystyle\langle x\chi|e^{-\Delta\tau\hat{H}}|\psi\rangle=\int\langle x\chi|e^{-\Delta\tau\hat{H}}|y\eta\rangle\langle y\eta|\psi\rangle\mathrm{d}^{D}y\mathrm{d}^{D}\eta |  |
|  |  |  |
| --- | --- | --- |
|  | =∫(ei​B​(x−y)+i​χ¯​(χ−η)−Δ​τ​H​(B​χ¯​x~​χ~)​dD​B(2​π)D​dD​(i​χ¯))​⟨y​η|ψ⟩​dD​y​dD​η\displaystyle=\int\left(e^{iB(x-y)+i\bar{\chi}(\chi-\eta)-\Delta\tau H(B\bar{\chi}\tilde{x}\tilde{\chi})}\frac{\mathrm{d}^{D}B}{(2\pi)^{D}}\mathrm{d}^{D}(i\bar{\chi})\right)\langle y\eta|\psi\rangle\mathrm{d}^{D}y\mathrm{d}^{D}\eta |  |
|  |  |  |
| --- | --- | --- |
|  | =∫ei​B​(x−y)+i​χ¯​(χ−η)​(1−Δ​τ​H​(B​χ¯​x~​χ~)+…)​⟨y​η|ψ⟩​dD​B(2​π)D​dD​(i​χ¯)​dD​y​dD​η\displaystyle=\int e^{iB(x-y)+i\bar{\chi}(\chi-\eta)}\Big(1-\Delta\tau H(B\bar{\chi}\tilde{x}\tilde{\chi})+...\Big)\langle y\eta|\psi\rangle\frac{\mathrm{d}^{D}B}{(2\pi)^{D}}\mathrm{d}^{D}(i\bar{\chi})\mathrm{d}^{D}y\mathrm{d}^{D}\eta |  |
|  |  |  |
| --- | --- | --- |
|  | =(1−Δ​τ​H^+…)​⟨x​χ|ψ⟩,\displaystyle=(1-\Delta\tau\hat{H}+...)\langle x\chi|\psi\rangle, |  |

where x~=α​x+(1−α)​y\tilde{x}=\alpha x+(1-\alpha)y, χ~=α​χ+(1−α)​η\tilde{\chi}=\alpha\chi+(1-\alpha)\eta, and H^=H​(x~​χ~​B​χ¯)|B,χ¯→B^,χ¯^\hat{H}=\left.H(\tilde{x}\tilde{\chi}B\bar{\chi})\right|\_{B,\bar{\chi}\to\hat{B},{\hat{\bar{\chi}}}}, with

|  |  |  |  |
| --- | --- | --- | --- |
| (3.22) |  | i​B^=∂/∂x,i​χ¯^=∂/∂χ,\displaystyle i\hat{B}=\partial/\partial x,i\hat{\bar{\chi}}=\partial/\partial\chi, |  |

being the momenta operators whose form follows from expressions like this one, 151515Here, we explicitly show the vector indices.

|  |  |  |  |
| --- | --- | --- | --- |
| (3.23) |  | ∫ei​B​(x−y)​i​Bj1​…​i​Bjp​xk1​…​xkq​yl1​…​ylp​⟨y​η|ψ⟩​dD​B(2​π)D​dD​y\displaystyle\int e^{iB(x-y)}iB\_{j\_{1}}...iB\_{j\_{p}}x^{k\_{1}}...x^{k\_{q}}y^{l\_{1}}...y^{l\_{p}}\langle y\eta|\psi\rangle\frac{\mathrm{d}^{D}B}{(2\pi)^{D}}\mathrm{d}^{D}y |  |
|  |  |  |
| --- | --- | --- |
|  | =xk1​…​xkq​∂∂xj1​…​∂∂xjp​xl1​…​xlp​⟨x​η|ψ⟩,\displaystyle=x^{k\_{1}}...x^{k\_{q}}\frac{\partial}{\partial x^{j\_{1}}}...\frac{\partial}{\partial x^{j\_{p}}}x^{l\_{1}}...x^{l\_{p}}\langle x\eta|\psi\rangle, |  |

and similar expression can be derived for fermionic fields.

Besides proving Eq.([3.22](https://arxiv.org/html/2512.21539v1#S3.E22 "In 3.3. Stochastic evolution operator ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), Eq.([3.23](https://arxiv.org/html/2512.21539v1#S3.E23 "In 3.3. Stochastic evolution operator ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) also shows how to order operators: in the operator representation the position and momentum operators do not commute and the order of operators matters. As can be seen from the second line of Eq.([3.23](https://arxiv.org/html/2512.21539v1#S3.E23 "In 3.3. Stochastic evolution operator ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), the correct order is chronological: B,yB,y and xx represent, respectively, BkB\_{k}, xk−1x\_{k-1}, and xkx\_{k} at any given time slice, kk, of Fig.[3](https://arxiv.org/html/2512.21539v1#S2.F3 "Figure 3 ‣ 2.6. Sharp trace ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry"), so that BB acts after yy but before xx.

The exact form of SEO depends on α\alpha because, say, B​x~→α​x^​B^+(1−α)​B^​x^B\tilde{x}\to\alpha\hat{x}\hat{B}+(1-\alpha)\hat{B}\hat{x} (and similarly for fermions). Dropping the details, which can be found in Ref.[OvcEntropy], the SEO has the same form as the GTO ([2.15](https://arxiv.org/html/2512.21539v1#S2.E15 "In 2.2. Generalized transfer operator ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")),

|  |  |  |  |
| --- | --- | --- | --- |
| (3.24) |  | H^=L^Fα−Θ​L^Ga​L^Ga,\displaystyle\hat{H}=\hat{L}\_{F\_{\alpha}}-\Theta\hat{L}\_{G\_{a}}\hat{L}\_{G\_{a}}, |  |

but with a shifted flow vector field, Fα=F−Θ​(2​α−1)​(Ga⋅∂)​GaF\_{\alpha}=F-\Theta(2\alpha-1)(G\_{a}\cdot\partial)G\_{a}.

### 3.4. Ito-Stratonovich dilemma

The dependence of SEO ([3.24](https://arxiv.org/html/2512.21539v1#S3.E24 "In 3.3. Stochastic evolution operator ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) on α\alpha is the essence of Ito-Stratonovich dilemma. The meaning of this ambiguity in the definition of stochastic dynamics can be qualitatively understood as follows.

The entire family of Runge-Kutta methods (see, e.g., Ref.[Thijssen\_2007]) is based on the understanding that, under general assumptions, for any given initial condition and a sufficiently smooth configuration of the noise, ξ​(t)→ξ​(τk)≡ξk,k=1​…​N\xi(t)\to\xi(\tau\_{k})\equiv\xi\_{k},k=1...N, the contituous-time limit of Eq.([3.2](https://arxiv.org/html/2512.21539v1#S3.E2 "In 3.1. Stochastic differential equations ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) exists and the solution converges to that of Eq.([2.1](https://arxiv.org/html/2512.21539v1#S2.E1 "In 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")). The parameter α\alpha controls how the error approaches zero: *e.g.*, for the direct Euler method, where α=0\alpha=0, and the midpoint method, with α=1/2\alpha=1/2, the error ∼Δ​τ\sim\Delta\tau and Δ​τ2\Delta\tau^{2}, respectively. Importantly, the solution itself is unique and independent of α\alpha. Therefore, if we choose to take the continuous-time limit before averaging over the noise, Eq.([3.2](https://arxiv.org/html/2512.21539v1#S3.E2 "In 3.1. Stochastic differential equations ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) transforms into Eq.([2.1](https://arxiv.org/html/2512.21539v1#S2.E1 "In 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), eliminating any dependence on α\alpha. Now, the analysis of Sec.[2](https://arxiv.org/html/2512.21539v1#S2 "2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") applies, so that the temporal evolution of differential forms is governed by the GTO ([2.15](https://arxiv.org/html/2512.21539v1#S2.E15 "In 2.2. Generalized transfer operator ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), which has a very clear mathematical meaning and is independent of the parameter α\alpha.

This point of view on stochastic dynamics – the one employed in Sec.[2](https://arxiv.org/html/2512.21539v1#S2 "2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") – can be described as first taking the continuous-time limit and then averaging over the noise. The pathintegral representation, however, reverses the order of these operations as can be seen, particularly, from Eq.([3.21](https://arxiv.org/html/2512.21539v1#S3.E21 "In 3.3. Stochastic evolution operator ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), where the noise variable is already integrated out while the time step Δ​τ\Delta\tau is still finite. In result, the SEO looses its mathematical meaning – it is no longer a pullback averaged over the noise, but, rather, a result of formal manipulations with formulas.
Moreover, the error in the convergence of Eq.([3.2](https://arxiv.org/html/2512.21539v1#S3.E2 "In 3.1. Stochastic differential equations ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) to Eq.([2.1](https://arxiv.org/html/2512.21539v1#S2.E1 "In 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) mentioned in the previous paragraph, begins to interact with the noise yielding the α\alpha-dependence of the SEO.

The so emerging ambiguity in the evolution operator is a general property of pathintegrals, not limited to stochastic dynamics, and also appears in quantum theory. It can only be removed by imposing additional conditions or principles. In quantum theory, the condition is the requirement for a Hermitian Hamiltonian, which is satisfied by the Weyl symmetrization rule corresponding to α=1/2\alpha=1/2. In STS, the condition can be that the SEO matches the GTO ([2.18](https://arxiv.org/html/2512.21539v1#S2.E18 "In 2.3. Topological supersymmetry ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), which is also achieved at α=1/2\alpha=1/2. In other words, only the Stratonovich interpretation provides SEO that matches GTO and, consequently, has a clear-cut mathematical meaning – the pullback averaged over noise.

Other interpretations differ only by the shifted flow vector field in Eq.([3.24](https://arxiv.org/html/2512.21539v1#S3.E24 "In 3.3. Stochastic evolution operator ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), which, however, does not carry any new mathematics.
161616It is worth noting here that it is commonly asserted in the literature that the Ito interpretation is distinguished from a mathematical standpoint because of its connection to the concept of martingale.
[Oks10]
This view originates from the observation that, at α=0\alpha=0, the right hand side of Eq.([3.2](https://arxiv.org/html/2512.21539v1#S3.E2 "In 3.1. Stochastic differential equations ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry"))
depends only on xk−1x\_{k-1} (and ξk\xi\_{k}) but not on xkx\_{k}. This is typically interpreted to mean that the Ito scheme “does not look into the future,” since xkx\_{k} depends solely on the previous value xk−1x\_{k-1} (and on ξk\xi\_{k}). As pointed out in Appendix A.1 of Ref.
[OvcEntropy],
however, the same property holds for all the other interpretations of stochastic dynamics as well. The variable xkx\_{k} is a unique function of xk−1x\_{k-1} and ξk\xi\_{k} for any α\alpha. For α≠0\alpha\neq 0, however, the unique function is given by Eq.
([3.2](https://arxiv.org/html/2512.21539v1#S3.E2 "In 3.1. Stochastic differential equations ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry"))
only implicitly and one must solve for xkx\_{k} to express it explicitly in terms of xk−1x\_{k-1} and ξk\xi\_{k}. In other words, the fact that the right hand side of Eq
.([3.2](https://arxiv.org/html/2512.21539v1#S3.E2 "In 3.1. Stochastic differential equations ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) at α=0\alpha=0 does not depend on xkx\_{k} may facilitate the numerical implementation of temporal propagation, but carries no deeper mathematical significance. Particularly, stochastic evolution does not ”look into the future” at any α\alpha and the following is always true for top differential forms (probability distributions): P​(x,t)=∫dD​x′​ℳt​t′(D)​(x|x′)​P​(x′,t′),t′<tP(x,t)=\int d^{D}x^{\prime}{\mathcal{M}}^{(D)}\_{tt^{\prime}}(x|x^{\prime})P(x^{\prime},t^{\prime}),t^{\prime}<t, where ℳ(D){\mathcal{M}}^{(D)} is the corresponding part of the GTO.
 Having multiple interpretations of SDEs is redundant. That said, alternative interpretations are relevant in the context of numerical implementations of SDEs, where different schemes may be preferred depending on computational context.

## 4. Topological field theory and stochastic dynamics

The Parisi-Sourlas method is peculiar in that sense that its entire action is QQ-exact as if it is a gauge-fixing of an empty theory. This is a definitive feature of cohomological TFTs. [TFT\_BOOK] As a TFT, STS has objects of topological nature.

### 4.1. Witten and Lefschetz indices

The Witten index is one of such objects. Its topological character can be qualitatively understood as follows. As mentioned at the beginning of Sec.[3.2](https://arxiv.org/html/2512.21539v1#S3.SS2 "3.2. Parisi-Sourlas approach as a BRST gauge-fixing ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry"), the Witten index is obtained by rewriting the noise partition function in terms of the dynamical variables of the DS. When done correctly, this procedure should yield an object which represents the noise partition function. However, since the noise carries no information about the DS dynamics, this object must be insensitive to perturbations or continuous deformations of the model. In other words, the object must be a topological invariant.

On a more rigorous level, the topological nature of the Witten index can be seen by noting, once again, that the gauge-fixing character of the action ensures that only solutions of the SDE contribute into pathintegral representation of WW in, say, Eq.([3.9](https://arxiv.org/html/2512.21539v1#S3.E9 "In 3.2. Parisi-Sourlas approach as a BRST gauge-fixing ‣ 3. Pathintegral representation of stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")). Each solution provides either positive or negative unity,

|  |  |  |  |
| --- | --- | --- | --- |
| (4.1) |  | W=⟨∬p.b.cJ​(ξ)​(∏τδD​((x˙​(τ)−ℱ​(x​(τ),ξ​(τ)))​d​τ))​𝒟​x⟩noise\displaystyle W=\Big\langle\iint\_{p.b.c}J(\xi)\bigg(\prod\nolimits\_{\tau}\delta^{D}\bigg(\Big(\dot{x}(\tau)-{\mathscr{F}}(x(\tau),\xi(\tau))\Big)\mathrm{d}\tau\bigg)\bigg){\mathcal{D}}x\Big\rangle\_{\text{noise}} |  |
|  |  |  |
| --- | --- | --- |
|  | =⟨∑x˙=ℱ​(x,ξ)J​(ξ)/|J​(ξ)|⟩noise=⟨IN​(ξ)⟩noise,\displaystyle=\left\langle\sum\_{\dot{x}={\mathscr{F}}(x,\xi)}J(\xi)/|J(\xi)|\right\rangle\_{\text{noise}}=\langle I\_{N}(\xi)\rangle\_{\text{noise}}, |  |

where the absolute value of the Jacobian in the denominator is the result of the functional integration of the bosonic delta-functionals, and IN​(ξ)=∑x˙=ℱ​(x,ξ)sign⁡J​(ξ)I\_{N}(\xi)=\sum\_{\dot{x}={\mathscr{F}}(x,\xi)}\operatorname{sign}J(\xi), is the index of the so-called Nicolai map. [Nicolai1, Nicolai2] In our case, this is the map from the space of closed paths to the space of configurations of the noise making these paths solutions of the SDE, ξa​(x)=Gia​(x˙i−Fi)/(2​Θ)1/2\xi^{a}(x)=G^{a}\_{i}(\dot{x}^{i}-F^{i})/(2\Theta)^{1/2}. The index of the map can be viewed as a realization of the Poincaré–Hopf theorem on the infinite-dimensional space of close paths with the SDE playing the role of the vector field and with the solutions of the SDE playing the role of the critical points with index sign​J​(ξ)=sign​detδ​ξ/δ​x\text{sign}J(\xi)=\operatorname{sign}\det\delta\xi/\delta x. IN​(ξ)I\_{N}(\xi) is a topological object independent of ξ\xi. It equals its own stochastic average which, in turn, equals the Witten index.

There are other ways to see the topological character of WW, with the most general mathematical framework related to this issue being the Mathai-Quillen formalism. [BLAU199395] From the point of view of DS theory, the most interesting way to see its topological character is to integrate out all the fields but those on the first and last time slices (see Fig.[3](https://arxiv.org/html/2512.21539v1#S2.F3 "Figure 3 ‣ 2.6. Sharp trace ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")). This leads to,

|  |  |  |  |
| --- | --- | --- | --- |
| (4.2) |  | W=⟨∫δD​(M​(ξ)t′​t​(x)−x)​δD​(T​M​(ξ)t′​t​χ−χ)​dD​x​dD​χ⟩noise\displaystyle W=\Big\langle\int\delta^{D}(M(\xi)\_{t^{\prime}t}(x)-x)\delta^{D}(TM(\xi)\_{t^{\prime}t}\chi-\chi)\mathrm{d}^{D}x\mathrm{d}^{D}\chi\Big\rangle\_{\text{noise}} |  |
|  |  |  |
| --- | --- | --- |
|  | =⟨IL​(ξ)⟩noise, where ​IL​(ξ)=∑x=M​(ξ)t′​t​(x)sign det​(T​M​(ξ)t′​t​(x)−1^T​Xx),\displaystyle=\langle I\_{L}(\xi)\rangle\_{\text{noise}},\;\text{ where }I\_{L}(\xi)=\sum\_{x=M(\xi)\_{t^{\prime}t}(x)}\text{sign }\text{det}\big(TM(\xi)\_{t^{\prime}t}(x)-\hat{1}\_{TX\_{x}}\big), |  |

is the Lefschetz index of M​(ξ)t​t′M(\xi)\_{tt^{\prime}}, which is independent of the noise configuration and equals the Euler characteristic of XX.

### 4.2. Instantons and Morse-Smale dynamical systems

Another class of objects of topological character are instantons or, more accurately, certain matrix elements on instantons. These objects are the reason why cohomological TFTs are identified sometimes as intersection theories on instantons. Instanton matrix elements is our next subject of interest.

Let us begin, however, by pointing out that from the physical point of view, instantons are the fundamental building blocks of transient dynamics in strongly nonlinear DSs. Earthquakes, solar flares, neuronal avalanches, and balloon popping are examples of instantons. Any given instance of transient dynamics, however, can be viewed as a composite instanton, i.e., a sequence of *elementary* instantons. Examples of composite instantons include protein folding, the collapse of a building, or even the life circle of an organism, which can also be looked upon as a very complex composite instanton. Composite instantons may appear in response to quenches, i.e., sudden changes of conditions, where a DS is abruptly placed in an unstable position of its phase space and begins its evolution toward a stable attractor, as seen, for instance, in impact defragmentation. Another type of composite instantons is nonlinear dynamics induced by a slow change of external parameters, as in the crumpling paper or the Barkhausen effect.

From the mathematical point of view, instantons are transition processes between critical points or other invariant sets. As will be clear below, in this section we are talking about Morse-Smale DSs, the ones whose invariant sets are hyperbolic and have topologically well defined local stable or unstable manifolds. [Morse\_Smale\_DS, book\_hyperbolic\_flows] Moreover, unlike antiinstantons (see Sec.[4.2.3](https://arxiv.org/html/2512.21539v1#S4.SS2.SSS3 "4.2.3. Antiinstantons ‣ 4.2. Instantons and Morse-Smale dynamical systems ‣ 4. Topological field theory and stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") below), instantons are not directly related to noise. Therefore, they can be considered in the deterministic limit, which we adopt here.

A pathintegral representation of a matrix element on an instanton from a critical point aa to bb can be expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
| (4.3) |  | ⟨b|O^|a⟩=∬x​(±∞)=xb,aO​(x​(0)​χ​(0))​e(Q,∫−∞∞i​χ¯​(x˙−F)​dτ)​𝒟​Φ,\displaystyle\langle b|\hat{O}|a\rangle=\iint\_{x(\pm\infty)=x\_{b,a}}O(x(0)\chi(0))e^{(Q,\int\_{-\infty}^{\infty}i\bar{\chi}(\dot{x}-F)\mathrm{d}\tau)}{\mathcal{D}}\Phi, |  |

where xa,bx\_{a,b} are positions of the critical points such that F​(xa,b)=0F(x\_{a,b})=0, and OO is an operator assumed, for simplicity, to depend only on x​χx\chi at t=0t=0. In Eq.([4.3](https://arxiv.org/html/2512.21539v1#S4.E3 "In 4.2. Instantons and Morse-Smale dynamical systems ‣ 4. Topological field theory and stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), ⟨b|\langle b| and |a⟩|a\rangle are the bra and the ket of the so-called local supersymmetric states of the corresponding critical points. These objects will be defined in the next section. In a meantime, let us use ⟨b|\langle b| and |a⟩|a\rangle to avoid the necessity to introduce redundant notations.

The gauge-fixing character of the action of STS restricts the pathintegration only to the deterministic solutions that start at aa and end at bb. There are infinitely many such solutions and their union forms an instanton manifold, Ib​aI\_{ba}, and dim ​Ib​a=ind ​a−ind ​b\text{dim }I\_{ba}=\text{ind }a-\text{ind }b, where the index of a critical point is the number of the unstable directions of the flow at this critical point. The points from the instanton manifold parametrise these solutions, x˙c​l​(t,σ)=F​(xc​l​(t,σ))\dot{x}\_{cl}(t,\sigma)=F(x\_{cl}(t,\sigma)), xc​l​(±∞)=b,a;x\_{cl}(\pm\infty)=b,a; σ∈Ia​b\sigma\in I\_{ab}, where σ\sigma are coordinates on Ia​bI\_{ab} called instanton modulii. The differentiation of solutions with respect to the moduli yields zero modes of operator,

|  |  |  |  |
| --- | --- | --- | --- |
| (4.4) |  | D^​(σ)=d/d​t−T​F​(xc​l​(t,σ));D^​(σ)​∂xc​l​(t,σ)/∂σ=0.\displaystyle\hat{D}(\sigma)=\mathrm{d}/\mathrm{d}t-TF(x\_{cl}(t,\sigma));\;\hat{D}(\sigma)\partial x\_{cl}(t,\sigma)/\partial\sigma=0. |  |

These are the only zero-modes of D^\hat{D} and D^†\hat{D}^{\dagger} (see, e.g., Ref.[TFT\_BOOK]).

One can now introduce fluctuations around deterministic solutions as

|  |  |  |  |
| --- | --- | --- | --- |
| (4.5) |  | x​(t)=xc​l​(t,σ)+δ​x′​(t),\displaystyle x(t)=x\_{cl}(t,\sigma)+\delta x^{\prime}(t), |  |

where the prime indicates that the fluctuations are restricted to directions transverse to the modulii. The corresponding decomposition for the superpartner χ​(t)=(∂xc​l​(t,σ)/∂σ)​χσ+χ′​(t)\chi(t)=(\partial x\_{cl}(t,\sigma)/\partial\sigma)\chi\_{\sigma}+\chi^{\prime}(t), where χσ=(Q,σ)\chi\_{\sigma}=(Q,\sigma), χ′​(t)=(Q,δ​x′​(t))\chi^{\prime}(t)=(Q,\delta x^{\prime}(t)).

The instanton matrix element ([4.3](https://arxiv.org/html/2512.21539v1#S4.E3 "In 4.2. Instantons and Morse-Smale dynamical systems ‣ 4. Topological field theory and stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) can now be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
| (4.6) |  | ⟨b|O^|a⟩=∬(O​(σ​χσ)+…)​e(Q,∫−∞∞i​χ¯​D^​(σ)​δ​x′​dτ)​𝒟​Φ′​dDI​σ​dDI​χσ,\displaystyle\langle b|\hat{O}|a\rangle=\iint(O(\sigma\chi\_{\sigma})+...)e^{(Q,\int\_{-\infty}^{\infty}i\bar{\chi}\hat{D}(\sigma)\delta x^{\prime}\mathrm{d}\tau)}{\mathcal{D}}\Phi^{\prime}\mathrm{d}^{D\_{I}}\sigma\mathrm{d}^{D\_{I}}\chi\_{\sigma}, |  |

where DI=dim​Ib​aD\_{I}=\text{dim}I\_{ba}, O​(σ​χσ)=O​(xc​l​(0,σ),(∂xc​l​(0,σ)/∂σ)​χσ)O(\sigma\chi\_{\sigma})=O(x\_{cl}(0,\sigma),(\partial x\_{cl}(0,\sigma)/\partial\sigma)\chi\_{\sigma}), Φ′\Phi^{\prime} denotes integration of all the fields except the instanton modulii and their superpartners, and the dots denote other terms that do not contribute, as will be pointed out shortly.

Integrating out the fluctuations in Eq.([4.6](https://arxiv.org/html/2512.21539v1#S4.E6 "In 4.2. Instantons and Morse-Smale dynamical systems ‣ 4. Topological field theory and stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) yields a factor that equals unity (up to a sign), due to the cancellation of the bosonic and fermionic contributions, which is a very general principle in supersymemtric field theories, [MirrorSymmetry]

|  |  |  |  |
| --- | --- | --- | --- |
| (4.7) |  | ∬e(Q,∫−∞∞i​χ¯​D^​(σ)​δ​x′​dτ)𝒟Φ′=∬e∫−∞∞i​B​D^​(σ)​δ​x′​dτ𝒟B𝒟δx′×\displaystyle\iint e^{(Q,\int\_{-\infty}^{\infty}i\bar{\chi}\hat{D}(\sigma)\delta x^{\prime}\mathrm{d}\tau)}{\mathcal{D}}\Phi^{\prime}=\iint e^{\int\_{-\infty}^{\infty}iB\hat{D}(\sigma)\delta x^{\prime}\mathrm{d}\tau}{\mathcal{D}}B{\mathcal{D}}\delta x^{\prime}\times |  |
|  |  |  |
| --- | --- | --- |
|  | ×∬e−∫−∞∞i​χ¯​D^​(σ)​χ′​dτ𝒟χ¯𝒟χ′=det​D^′​(σ)(det​(D^′​(σ)​D′^†​(σ)))1/2=sign detD^′(σ),\displaystyle\times\iint e^{-\int\_{-\infty}^{\infty}i\bar{\chi}\hat{D}(\sigma)\chi^{\prime}\mathrm{d}\tau}{\mathcal{D}}\bar{\chi}{\mathcal{D}}\chi^{\prime}=\frac{\text{det}\hat{D}^{\prime}(\sigma)}{\big(\text{det}\big(\hat{D}^{\prime}(\sigma)\hat{D^{\prime}}^{\dagger}(\sigma)\big)\big)^{1/2}}=\text{sign det}\hat{D}^{\prime}(\sigma), |  |

where D^′​(σ)\hat{D}^{\prime}(\sigma) is a restriction of D^​(σ)\hat{D}(\sigma) on all but zero modes.

One of the basic rules of integration over fermionic fields is the requirement that every fermionic differential must be matched by the corresponding fermion according to ∫dχ=0,∫χ​dχ=1\int\mathrm{d}\chi=0,\int\chi\mathrm{d}\chi=1. In application to Eq.([4.6](https://arxiv.org/html/2512.21539v1#S4.E6 "In 4.2. Instantons and Morse-Smale dynamical systems ‣ 4. Topological field theory and stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), this means that OO must provide all the χσ\chi\_{\sigma}’s to match, dDI​χσ\mathrm{d}^{D\_{I}}\chi\_{\sigma}. This provision is accomplished by the first term in the resolution of OO in the parentheses in the r.h.s. of Eq.([4.6](https://arxiv.org/html/2512.21539v1#S4.E6 "In 4.2. Instantons and Morse-Smale dynamical systems ‣ 4. Topological field theory and stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), while the other terms do not contribute to the matrix element, assuming that the degree of OO equals the dimensionality of the instanton manifold. Thus, we arrive at

|  |  |  |  |
| --- | --- | --- | --- |
| (4.8) |  | ⟨b|O^|a⟩=∫O​(σ​χσ)​dσ​dχσ=∫Ia​bO,\displaystyle\langle b|\hat{O}|a\rangle=\int O(\sigma\chi\_{\sigma})\mathrm{d}\sigma\mathrm{d}\chi\_{\sigma}=\int\_{I\_{ab}}O, |  |

where OO in the r.h.s. is understood as a differential form on Ib​aI\_{ba}, which can be interpreted as a pullback of OO from the space of paths to Ib​aI\_{ba} provided by xc​lx\_{cl}.

![Refer to caption](Smale_Complex.png)

Figure 4.  An example of a Morse-Smale flow (thin green arrowed curves). The filled green circles (b, e) represent minima (index 0), hollow circles (a,f,g,h) correspond to saddles (index-1), and filled-black circles (c,b) denote index-2 critical points. The bras/kets of the local supersymmetric states of the Morse-Smale-Bott-Witten complex are Poincare duals of the local stable/unstable manifolds. For example, ⟨a|=p​(Sa)\langle a|=p(S\_{a}) and |a⟩=p​(Ua)|a\rangle=p(U\_{a}) are narrow distributions on Sa=(c​a​d)S\_{a}=(cad) and Ua=(e​a​b)U\_{a}=(eab), respectively, with fermions in transverse directions, whereas ⟨b|\langle b| and |d⟩|d\rangle are constant functions over the green and gray regions, respectively. The dashed curves represent the one-parameter families of 1-dimensional manifolds, γ1​(t),γ2​(t)\gamma\_{1}(t),\gamma\_{2}(t), obtained by the flow-defined diffeomorphisms, γ1​(t)=Mt​0​(γ1)\gamma\_{1}(t)=M\_{t0}(\gamma\_{1}). Their Poincare duals can be used to construct, e.g, the matrix element, ⟨b|p^​(γ1​(t))​p^​(γ2​(0))|d⟩=1\langle b|\hat{p}(\gamma\_{1}(t))\hat{p}(\gamma\_{2}(0))|d\rangle=1, which represents the intersection number of γ\gamma’s on the instanton manifold, Ib​d=Sb∩Ud=(b​h​d​a)I\_{bd}=S\_{b}\cap U\_{d}=(bhda). The matrix element is independent of tt’s because the intersection points (dis)appear in pairs with opposite orientations (white and black filled circles).

#### 4.2.1. Morse-Smale-Bott-Witten complex

To examine the instanton matrix element in the operator representation, let us define the local supersymmetric states (LSS), whose notation we already introduced in the previous section:

|  |  |  |  |
| --- | --- | --- | --- |
| (4.9) |  | ⟨x​χ|a⟩=∬x​(−∞)=xax​χ​(0)=x​χe(Q,∫−∞0i​χ¯​(x˙−F)​dτ)​𝒟​Φ,\displaystyle\langle x\chi|a\rangle=\iint\_{{x(-\infty)=x\_{a}}\atop{x\chi(0)=x\chi}}e^{(Q,\int\_{-\infty}^{0}i\bar{\chi}(\dot{x}-F)\mathrm{d}\tau)}{\mathcal{D}}\Phi, |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (4.10) |  | ⟨b|x​χ⟩=∬x​(+∞)=xbx​χ​(0)=x​χe(Q,∫0+∞i​χ¯​(x˙−F)​dτ)​𝒟​Φ.\displaystyle\langle b|x\chi\rangle=\iint\_{{x(+\infty)=x\_{b}}\atop{x\chi(0)=x\chi}}e^{(Q,\int\_{0}^{+\infty}i\bar{\chi}(\dot{x}-F)\mathrm{d}\tau)}{\mathcal{D}}\Phi. |  |

Given the gauge-fixing nature of the action limiting the pathintegration to deterministic solution of the flow, it follows that |a⟩|a\rangle is non-zero only for points that flow to aa in the t=−∞t=-\infty limit, that is, for points on the local unstable manifold of aa: UaU\_{a}.171717The local stable and unstable manifold of a critical point are defined as the set of points that asymptotically flow toward the critical point in the infinite future and past, respectively. Similarly, ⟨b|\langle b| is non-zero only on the local stable manifold of bb: SbS\_{b}. That the intersection of the local stable and unstable manifolds is the instanton manifold, Ib​a=Ua∩SbI\_{ba}=U\_{a}\cap S\_{b}, is a well known set-theoretic result of DS theory. From the algebraic point of view, however, the fermionic structure of the LSSs is also important.

To determine the fermionic content of a LSS, let us consider the simple case of a Langevin SDE on X=ℝX=\mathbb{R} with F=−U′,U=ω​x2/2F=-U^{\prime},U=\omega x^{2}/2 and an additive noise. Its SEO can be expressed as,

|  |  |  |  |
| --- | --- | --- | --- |
| (4.11) |  | H^=e−U/2​Θ​H^W​eU/2​Θ,H^W=H^W†=Θ​[d^W,d^W†],\displaystyle\hat{H}=e^{-U/2\Theta}\hat{H}\_{W}e^{U/2\Theta},\;\hat{H}\_{W}=\hat{H}\_{W}^{\dagger}=\Theta[\hat{d}\_{W},\hat{d}\_{W}^{\dagger}], |  |

where d^W=χ​(−U′/2​Θ+∂/∂x)\hat{d}\_{W}=\chi(-U^{\prime}/2\Theta+\partial/\partial x), d^W†=(∂/∂χ)​(−U′/2​Θ−∂/∂x)\hat{d}\_{W}^{\dagger}=(\partial/\partial\chi)(-U^{\prime}/2\Theta-\partial/\partial x), and H^W\hat{H}\_{W} can be identified as the Hermitian Hamiltonian of a 1D supersymmetric harmonic oscillator. [Junker1996] H^\hat{H} and H^W\hat{H}\_{W} are related via a similarity transformation so that their eigensystems are identical up to this transformation. In terms of H^W\hat{H}\_{W}, the ket and the bra of the zero-eigenvalue supersymmetric ground state are, respectively, ψW=χ​e−|ω|​x2/2​Θ\psi\_{W}=\chi e^{-|\omega|x^{2}/2\Theta} and ψ¯W=e−|ω|​x2/2​θ\bar{\psi}\_{W}=e^{-|\omega|x^{2}/2\theta} for ω>0\omega>0, and ψ¯W↔ψW\bar{\psi}\_{W}\leftrightarrow\psi\_{W} for ω<0\omega<0. In terms of H^\hat{H}, for ω>0\omega>0, the ket of the ground state is χ​e−|ω|​x2/Θ\chi e^{-|\omega|x^{2}/\Theta}, while the bra is a constant function. For ω<0\omega<0, the roles of bra and ket are reversed.

This example can be easily generalized to the multiple-variable non-degenerate critical point of a gradient flow. In appropriate coordinates, U=∑iωi​(xi)2/2,ωi≠0,i=1​…​DU=\sum\_{i}\omega\_{i}(x^{i})^{2}/2,\omega\_{i}\neq 0,i=1...D. Both the bra and the ket of the LSS factorize, with each coordinate contributing a factor from the 1D Langevin case above. In the deterministic limit (Θ→0\Theta\to 0), the ket of the LSS is a narrow distribution with fermions in the stable directions (ωi>0\omega\_{i}>0) and a constant function without fermions in the unstable directions (ωi<0\omega\_{i}<0). The situation is reversed for the bra, which is a narrow distribution in the unstable directions and a constant function in the stable directions.

A natural generalization of the previous example is that the ket and the bra of the LSS associated with an isolated critical point, aa, are the Poincare duals, p​(Ua)p(U\_{a}) and p​(Sa)p(S\_{a}), of the local unstable and stable manifolds, respectively. 181818By definition, the Poincare dual, p​(Z)p(Z), of a submanifold ZZ is a δ\delta-distribution on ZZ with differentials in transverse directions. Its key property is ∫Zψ=∫Xp​(Z)∧ψ,∀ψ\int\_{Z}\psi=\int\_{X}p(Z)\wedge\psi,\forall\psi. For example, for a co-dimension 11 hyperplane, γ0={x∈RD|xi=x0}\gamma\_{0}=\{x\in\mathrm{R}^{D}|x^{i}=x\_{0}\}, the Poincare dual p​(γ0)=δ​(xi−x0)​d​xip(\gamma\_{0})=\delta(x^{i}-x\_{0})\mathrm{d}x^{i}.  To see that this is indeed so, recall that in the deterministic limit, the SEO consists only of the Lie derivative along FF and the Poincare duals of (un)stable manifolds of the flow lie in its kernel, that is, they are zero-eigenvalue LSSs of the evolution operator.

In terms of Poincare duals, the matrix element ([4.8](https://arxiv.org/html/2512.21539v1#S4.E8 "In 4.2. Instantons and Morse-Smale dynamical systems ‣ 4. Topological field theory and stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
| (4.12) |  | ⟨b|O^|a⟩=∫Xp​(Sb)∧O∧p​(Ua).\displaystyle\langle b|\hat{O}|a\rangle=\int\_{X}p(S\_{b})\wedge O\wedge p(U\_{a}). |  |

Being supersymmetric states, the LSSs are d^\hat{d}-closed, d^​p​(Ua)=0\hat{d}p(U\_{a})=0. This property, however, holds only locally in the vicinity of the critical point, justifying the term ”local supersymmetric states”. From the global perspective, LSSs provide an algebraic representation of the Morse-Smale-Witten complex, with d^\hat{d} serving as the algebraic counterpart of the boundary operator. For instance, the action of d^\hat{d} on some of the LSSs in Fig.[4](https://arxiv.org/html/2512.21539v1#S4.F4 "Figure 4 ‣ 4.2. Instantons and Morse-Smale dynamical systems ‣ 4. Topological field theory and stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") is,

|  |  |  |  |
| --- | --- | --- | --- |
| (4.13) |  | d^​|a⟩=|b⟩−|e⟩,d^​|d⟩=|a⟩+|h⟩−|g⟩−|f⟩,…\displaystyle\hat{d}|a\rangle=|b\rangle-|e\rangle,\;\hat{d}|d\rangle=|a\rangle+|h\rangle-|g\rangle-|f\rangle,... |  |

This framework should extend naturally to nontrivial invariant sets via the Morse-Bott approach (see, *e.g.*, Ch.10 of Ref.[MirrorSymmetry]). Each de Rham cohomology class of an invariant set must provide one (global in terms of the invariant set) supersymmetric state (see Sec.[2.4.4](https://arxiv.org/html/2512.21539v1#S2.SS4.SSS4 "2.4.4. Supersymmetric singlets ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")). These may serve as additional factors for the Morse-Smale-Witten LSSs leading to a generalized structure that could be termed the Morse-Smale-Bott-Witten complex. While the present author is unaware of a rigorous establishment of this extension, he finds it natural to expect its validity for Morse-Smale DSs, whose Morse-Smale complex is topologically well-defined and structurally stable. [Morse\_Smale\_DS, book\_hyperbolic\_flows]

#### 4.2.2. Intersections on instantons

As mentioned earlier, certain matrix elements on instantons in TFTs are topological invariants. [Frenkel2007215] These are matrix elements of QQ-closed operators on LSSs. In the class of models considered here, the simplest topological invariants of this type can be defined as follows.

Consider a set of submanifolds in XX, {γα|α=0,1,…}\{\gamma\_{\alpha}|\alpha=0,1,...\}. Their Poincare duals, p​(γα)p(\gamma\_{\alpha}), satisfy the relation,

|  |  |  |  |
| --- | --- | --- | --- |
| (4.14) |  | (Q,p​(γi))=[d^,p​(γi)]=p​(∂γi),\displaystyle(Q,p(\gamma\_{i}))=[\hat{d},p(\gamma\_{i})]=p(\partial\gamma\_{i}), |  |

where ∂γi\partial\gamma\_{i} is the boundary of γi\gamma\_{i}. The duals p​(γ)p(\gamma)’s are QQ-closed if γ\gamma’s are either boundaryless or if their boundaries lie outside the domain of XX under consideration.

Consider also the following matrix elements,

|  |  |  |  |
| --- | --- | --- | --- |
| (4.15) |  | ∬x±∞=xb,ap​(γk)​(tk)​…​p​(γ1)​(0)​e(Q,∫−∞∞i​χ¯​(x˙−F)​dτ)​𝒟​Φ\displaystyle\iint\_{x\_{\pm\infty}=x\_{b,a}}p(\gamma\_{k})(t\_{k})...p(\gamma\_{1})(0)e^{(Q,\int\_{-\infty}^{\infty}i\bar{\chi}(\dot{x}-F)\mathrm{d}\tau)}{\mathcal{D}}\Phi |  |
|  |  |  |
| --- | --- | --- |
|  | =⟨b|p^​(γk)​(tk)​…​p^​(γ1)​(t1)|a⟩,\displaystyle=\langle b|\hat{p}(\gamma\_{k})(t\_{k})...\hat{p}(\gamma\_{1})(t\_{1})|a\rangle, |  |

where without loss of generality we assume tk>…>t1t\_{k}>...>t\_{1}, and

|  |  |  |  |
| --- | --- | --- | --- |
| (4.16) |  | p^​(γi)​(tk)=eti​H^​p^​(γi)​e−ti​H^=M^ti​0∗​(p​(γi))=p​(γi​(ti)),\displaystyle\hat{p}(\gamma\_{i})(t\_{k})=e^{t\_{i}\hat{H}}\hat{p}(\gamma\_{i})e^{-t\_{i}\hat{H}}=\hat{M}^{\*}\_{t\_{i}0}(p(\gamma\_{i}))=p(\gamma\_{i}(t\_{i})), |  |

are the corresponding operators in the so-called Heisenberg representation, M^ti​0∗\hat{M}^{\*}\_{t\_{i}0} is the pullback induced by Mti​0M\_{t\_{i}0}, and γi​(ti)=Mti​0​(γi)\gamma\_{i}(t\_{i})=M\_{t\_{i}0}(\gamma\_{i}) is the manifold obtained from γi\gamma\_{i} through the diffeomorphism, Mti​0M\_{t\_{i}0}. The validity of Eq.([4.16](https://arxiv.org/html/2512.21539v1#S4.E16 "In 4.2.2. Intersections on instantons ‣ 4.2. Instantons and Morse-Smale dynamical systems ‣ 4. Topological field theory and stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) follows from the observation that in the deterministic limit the SEO is just the flow along FF.

It is now clear that the above matrix element represents the intersection number,

|  |  |  |  |
| --- | --- | --- | --- |
| (4.17) |  | ∫Ib​ap​(γk​(tk))∧…∧p​(γ1​(t1))=∑x∈Ib​a∩γk​(tk)∩…∩γ1​(t1)(±),\displaystyle\int\_{I\_{ba}}p(\gamma\_{k}(t\_{k}))\wedge...\wedge p(\gamma\_{1}(t\_{1}))=\sum\_{x\in I\_{ba}\cap\gamma\_{k}(t\_{k})\cap...\cap\gamma\_{1}(t\_{1})}(\pm), |  |

where the signs account for the mutual orientation of γ\gamma’s at the intersection points, and it is assumed that the sum of codimensions of γ\gamma’s equals the dimensionality of Ib​aI\_{ba}. The topological invariance of Eq.([4.17](https://arxiv.org/html/2512.21539v1#S4.E17 "In 4.2.2. Intersections on instantons ‣ 4.2. Instantons and Morse-Smale dynamical systems ‣ 4. Topological field theory and stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) is its independence of t′​st^{\prime}s: the flow-induced diffeomorphism acting on any γ\gamma does not alter the intersection number because the intersection points (dis)appear in pairs with opposite orientations (see Fig.[3](https://arxiv.org/html/2512.21539v1#S2.F3 "Figure 3 ‣ 2.6. Sharp trace ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")).

#### 4.2.3. Antiinstantons

The qualitative discussion in Sec.[5](https://arxiv.org/html/2512.21539v1#S5 "5. Self-sustained dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry") below relies partly on the concept of antiinstantons. These are the time-reversed instantons of motion against the flow. Unlike instantons, antiinstantons are only possible with the assistance from the noise. As a result, their matrix elements contain exponentially weak Gibbs factors vanishing in the deterministic limit. This can be seen, for example, in the Langevin SDEs where antiinstantonic matrix elements are related to their instantonic counterparts as:

|  |  |  |  |
| --- | --- | --- | --- |
| (4.18) |  | ⟨a|O^†|b⟩=e−2​(U​(xb)−U​(xa))/Θ​⟨b|O^|a⟩,\displaystyle\langle a|\hat{O}^{\dagger}|b\rangle=e^{-2(U(x\_{b})-U(x\_{a}))/\Theta}\langle b|\hat{O}|a\rangle, |  |

where UU is the Langevin potential defining the flow F=−∂UF=-\partial U, and O^†\hat{O}^{\dagger} is the conjugate of O^\hat{O}, obtained by the substitutions χ↔χ¯\chi\leftrightarrow\bar{\chi} and B→B+2​F/ΘB\to B+2F/\Theta. [TFT\_BOOK]

![Refer to caption](Phase_Diagram.png)

  


Figure 5.  Stochastic DSs can be classified based on two key factors: *(i)* whether the topological supersymmetry (TS) is spontaneously broken (ordered phase) or unbroken (symmetric phase) and *(ii)* whether the flow vector field is integrable or non-integrable and/or chaotic. The symmetric phase with unbroken TS is labeled as T. The ordered phase with non-integrable flow (C-phase) is a stochastic generalization of the deterministic chaos, where the TS breaking is caused by the nonintegrability of the flow. The ordered phase with integrable flow (N-phase) can be identified as the noise-induced chaos, where the dynamics is dominated by noise-induced instantons. The instantons vanish in the deterministic limit, causing the N-phase to collapse onto the boundary of the C-phase. As noise intensity increases, the TS must eventually be restored disregard of the properties of the flow, as the GTO/SEO becomes dominated by the Laplacian, which alone does not break TS.

## 5. Self-sustained dynamics

As discussed at the beginning of Sec.[4](https://arxiv.org/html/2512.21539v1#S4 "4. Topological field theory and stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry"), transient dynamics is the concept representing a strongly nonlinear dissipative DS on its way to a stable attractor. In contrast, sustained dynamics refers to the state of the DS after infinitely long evolution unperturbed by external influence other than the stochastic noise. While transient dynamics is associated with instantons and local supersymmetric states, sustained dynamics is described by the global ground state. The very concept of the spontaneous symmetry breaking pertains to the global ground state.

### 5.1. Global ground state

The global ground state is a part of the definition of the generating functional, G​(η)G(\eta), – a functional of external probing fields, η\eta, introduced into the SDE, F→F​(η)F\to F(\eta), to explore the system’s response to external influence. It is understood that G​(η)G(\eta) must be constructed from the SEO, which is the most important object in the theory and which is also a functional of η\eta in the presence of the probing fields, M^T/2,−T/2​(η)\hat{M}\_{T/2,-T/2}(\eta).

The sharp trace of the SEO is unsuitable as a generating functional because, as a topological invariant, it is insensitive to the external perturbations. The ordinary trace of the GTO is a better alternative. However, it is still not good enough: in DSs with the broken pseudo-time-reversal symmetry (type-c spectra in Fig.[2](https://arxiv.org/html/2512.21539v1#S2.F2 "Figure 2 ‣ 2.4.3. Non-supersymmetric doublets ‣ 2.4. Eigensystem ‣ 2. Continuous-time stochastic dynamical systems ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), such a generating functional would exhibit undesirable oscillatory behavior in the long-time limit. The optimal choice for the generating functional is,

|  |  |  |  |
| --- | --- | --- | --- |
| (5.1) |  | G​(η)=−log​limT→∞eHg​T​⟨g|M^T/2,−T/2​(η)|g⟩,\displaystyle G(\eta)=-\log\lim\_{T\to\infty}e^{H\_{g}T}\langle g|\hat{M}\_{T/2,-T/2}(\eta)|g\rangle, |  |

where the factor eHg​T=1/⟨g|M^T/2,−T/2​(0)|g⟩e^{H\_{g}T}=1/\langle g|\hat{M}\_{T/2,-T/2}(0)|g\rangle is introduced to remove the unimportant infinite constant and |g⟩|g\rangle is the global ground state, i.e., one of the eigenstates with the smallest real part of the eigenvalue, Re ​Hg=minα⁡Re ​Hα\text{Re }H\_{g}=\min\nolimits\_{\alpha}\text{Re }H\_{\alpha}. This criterion for the eigenvalue of the ground state ensures the stability of the response.

The functional dependence of G​(η)G(\eta) on the probing fields characterizes the ground state’s response to external perturbations. Since this response involves transitions to all other eigenstates, the choice of a particular eigenstate as the ground state among a few fastest growing eigenstates does not impose any limitations onto the so-obtained description of the system’s dynamics.

#### 5.1.1. Spontaneous topological supersymmetry breaking

When the TS is broken spontaneously, an eigenstate with the same eigenvalue as the ground state exists, making the ground state easily ”excitable”. This effortless excitability is a predecessor of the Goldstone theorem, which states that in higher-dimensional models, where basespaces have dimensions other than time, a gapless excitation must exist. These excitations, known as goldstinos, mediate long-range responses and may provide a qualitative explanation for the ubiquity of power-law correlations in chaotic dynamics, commonly referred to as 1/f noise.

A rigorous theoretical explanation of 1/f noise remains an open question. However, there is a quantitative argument supporting this claim. This argument applies to higher-dimensional models with a long-range dynamics of Lorenzian type such as the one discussed in Ref.[OVCHINNIKOV2024114611]. In such models, the large-scale dynamics must be scale invariant and the corresponding effective field theory (EFT) [RFT\_SSB\_book] must be a conformal field theory (CFT). [ginsparg1988appliedconformalfieldtheory] 191919There are also reasons to believe that the EFT is not only a CFT but also a TFT.[ovchinnikov2025topologicalnaturebutterflyeffect] As a CFT, the EFT must possess a set of primary local fields, O^i(r),i=1,..,N\hat{O}\_{i}(r),i=1,..,N, where rr is a basespace point, such that, ⟨g|O^i​(r)|g⟩=0\langle g|\hat{O}\_{i}(r)|g\rangle=0, and

|  |  |  |  |
| --- | --- | --- | --- |
| (5.2) |  | ⟨g|O^i​(0)​O^i​(r)|g⟩=1/|r|2​Δi.\displaystyle\langle g|\hat{O}\_{i}(0)\hat{O}\_{i}(r)|g\rangle=1/|r|^{2\Delta\_{i}}. |  |

where Δ\Delta’s are the conformal weights of the primary fields. Furthermore, by the so-called operator-state correspondence in CFTs, any local operator, O^​(r)\hat{O}(r), can be resolved as

|  |  |  |  |
| --- | --- | --- | --- |
| (5.3) |  | O^​(r)=∑ici​O^i​(r)+…,\displaystyle\hat{O}(r)=\sum\nolimits\_{i}c\_{i}\hat{O}\_{i}(r)+..., |  |

where the omitted terms represent descendant fields, which are subdominant in the long-wavelength limit as they have higher conformal weights. Eqs.([5.2](https://arxiv.org/html/2512.21539v1#S5.E2 "In 5.1.1. Spontaneous topological supersymmetry breaking ‣ 5.1. Global ground state ‣ 5. Self-sustained dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) and ([5.3](https://arxiv.org/html/2512.21539v1#S5.E3 "In 5.1.1. Spontaneous topological supersymmetry breaking ‣ 5.1. Global ground state ‣ 5. Self-sustained dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")) lead to the conclusion that in the long-wavelength limit, correlators of a wide class of observables must be a power law

|  |  |  |  |
| --- | --- | --- | --- |
| (5.4) |  | ⟨g|O^​(0)​O^​(r)|g⟩||r|→∞=cis2/|r|2​Δim+…,\displaystyle\langle g|\hat{O}(0)\hat{O}(r)|g\rangle\big|\_{|r|\to\infty}=c\_{i\_{s}}^{2}/|r|^{2\Delta\_{i\_{m}}}+..., |  |

where isi\_{s} is the index of the primary field with the smallest conformal weight.

#### 5.1.2. Spontaneously pseudo-time-reversal symmetry breaking

Another interesting situation arises when HgH\_{g} is complex. In this case, the ”relative” eigenvalues, Δ​Hα=Hα−Hg\Delta H\_{\alpha}=H\_{\alpha}-H\_{g}, of the low-lying eigenstates – which govern the long-range behavior – are no longer real or complex conjugate pairs, signaling the breakdown of pseudo-time-reversal symmetry. In the context of kinematic dynamo theory, a complex HgH\_{g} corresponds to the rotation of a growing galactic magnetic field. [Torsten] The broader implications of a complex HgH\_{g} is an open question.

### 5.2. Phase Diagram

Our final topic of interest is the internal structure of the global ground state. A thorough analysis of this problem may take time to fully resolve. At present, only a qualitative understanding is available, which is expected to evolve with future research, leading to refinements and deeper insights. Despite its preliminary nature, this understanding provides valuable insights, making it a topic worthy of a brief discussion.

#### 5.2.1. Integrable flows and unbroken TS

In deterministic Morse-Smale DSs (see Sec.([4.2](https://arxiv.org/html/2512.21539v1#S4.SS2 "4.2. Instantons and Morse-Smale dynamical systems ‣ 4. Topological field theory and stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry"))), the local (un)stable manifolds with boundaries can be glued together into topologically well-defined global (un)stable manifolds that form foliations of XX. The existence of the topologically well-defined global unstable manifolds is actually a criterion for a flow to be identified as integrable in the sense of DS, *i.e.*, the ones satisfying Frobenius’ theorem. [Intro\_Smooth\_Manifolds] In such situations, and according to the discussion in the previous section, the Poincare duals of the global (un)stable manifolds are the global ground states. These ground states are supersymmetric because they are d^\hat{d}-closed, which is the algebraic version of the statement that the global (un)stable manifolds have no boundaries.

#### 5.2.2. Non-integrable flows and TS breaking

For chaotic or non-integrable deterministic DSs, the topologically well-defined global (un)stable manifolds do not exist. For example, in topological theory of chaos, [Gilmore\_book] the global unstable manifolds are approximated by branched unstable manifolds. The branched manifolds have self-intersections so that they are not topological manifolds. As a result, the Poincare dual of such a branched (un)stable manifold, which is supposed to be the ground state of the model, cannot be d^\hat{d}-closed. In other words, the ground state is not supersymmetric for chaotic deterministic flows and TS is broken spontaneously.

#### 5.2.3. Noise-induced chaos and instanton condensation

For an integrable flow, whose Morse-Smale complex is stable with respect to weak perturbations, introduction of a sufficiently weak noise must not break TS. the noise will only broaden the ground state in transverse directions of the global (un)stable manifold, making it – in the first approximation – a narrow supersymmetric Gaussian distribution. In high-energy theory terminology, this implies that the TS is unbroken at the Gaussian level. Higher-order perturbative corrections must not qualitatively change this picture because supersymmetries are robust symmetries: if they are not broken on the Guassian level, then higher-order perturbative corrections cannot break them either – the well-known absence of the supersymmetry breaking anomaly. [Bertlmann1996, AlvarezGaume1984]

However, sufficiently strong noise can break the TS of the integrable flows through a mechanism distinct from perturbative corrections – the condensation of the noise-induced antiinstantons and instantons matching them, or, simpler, the condensation of the noise-induced instantons. 202020Instantons is a reliable mechanism of the spontaneous supersymmetry breaking in high-energy physics. [DynSusyBrWitten] When this happens, the resulting dynamics should look as an endless sequence of the noise-induced instantons interacting with each other. Moreover, certain characteristics of instantons, such as their statistical properties – exemplified by the power-law distribution of earthquakes, solar flares, neuroavalanches, etc. – should reflect the long-range nature of chaos, in accordance with the Goldstone theorem. Importantly, the mere existence of instantons in a nonlinear model does not necessarily break TS. 212121For example, in Langevin SDEs with multiple minima of the Langevin potential, instantons exist, yet TS is never broken because the eigenvalues of the SEO are real and non-negative. Noise-induced instantons can only facilitate TS breaking in flows that are already close to being chaotic (see Fig.[5](https://arxiv.org/html/2512.21539v1#S4.F5 "Figure 5 ‣ 4.2.3. Antiinstantons ‣ 4.2. Instantons and Morse-Smale dynamical systems ‣ 4. Topological field theory and stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")).

It now follows that this type of dynamics, which can be called the noise-induced chaos, must collapse onto the boundary of deterministic chaos in the deterministic limit. This conclusion follows from two observations: *(i)* noise-induced chaos disappears in the deterministic limit, just like the anti-instantons that underlie it, and *(ii)* the TS-breaking phase transition must form a continuous curve that terminates precisely at the edge of deterministic chaos as the deterministic limit is approached. In this way (see Fig.[5](https://arxiv.org/html/2512.21539v1#S4.F5 "Figure 5 ‣ 4.2.3. Antiinstantons ‣ 4.2. Instantons and Morse-Smale dynamical systems ‣ 4. Topological field theory and stochastic dynamics ‣ Chaos, Ito-Stratonovich dilemma, and topological supersymmetry")), STS provides a theoretical framework for understanding the phenomenon known as the ”border of chaos.” [DynamicalComplexity, Crutchfield]

## 6. Conclusion

In this paper, we discussed key aspects of the recently established connection between dynamical systems theory and cohomological topological field theories, a framework that can be referred to as the supersymmetric theory of stochastic dynamics. We demonstrated that this approach is an algebraic dual to the set-theoretic framework of dynamical systems theory. The added algebraic structure reveals the presence of the topological supersymmetry in all stochastic models and enables the stochastic generalization of concepts traditionally associated with deterministic dynamics. Namely, the Morse-Smale complex of local unstable manifolds, strange attractors, and chaoticity of a deterministic flow correspond, on the side of stochastic dynamics, to the Morse-Smale-Bott-Witten complex of local supersymmetric states, global non-supersymmetric ground states, and the spontaneous breakdown of topological supersymmetry, respectively.

From a practical standpoint, STS is particularly interesting because it provides an explanation for the experimental signature of chaotic dynamics known as 1/f noise. Numerous attempts have been made to account for this phenomenon; the most prominent among them is perhaps the concept of self-organized criticality — the idea that some mysterious force fine-tunes stochastic dynamical systems to the transition into chaos.[Bak87] To the best of the present author’s knowledge, however, STS is the only framework that offers a theoretically rigorous explanation of 1/f noise.

Beyond that, STS has yielded fresh insights into the competing definitions of chaos and the various interpretations of stochastic dynamics, offering a theoretical understanding of behavior at the so-called “edge of chaos.” Its potential implications, however, extend even further. More broadly, mathematical physics today is divided into two major camps: quantum and classical. The gap between them is substantial, making collaboration between, for example, dynamical systems theorists and string theorists challenging. The supersymmetric theory of stochastic dynamics has the potential to bridge this divide by unifying concepts and providing a shared mathematical framework, fostering collaboration and accelerating progress in both areas.

## Acknowledgments

The author acknowledges the initial support from DARPA BAA ”Physical Intelligence” and extends special gratitude to Kang L. Wang for his pivotal role in enabling this work. Sincere thanks are also extended to Massimiliano Di Ventra, Torsten A. Ensslin, Robert N. Schwartz, Savdeep S. Sethi, Gabriel A. Weiderpass, Ben Israelii, Daniel Toker, Skirmantas Janusonis, Dmitri A. Riabtsev, Cheng-Zong Bai, and Eugene Ingerman, all of whom positively influenced this work.

## Declaration of conflict of interest

The author declares no conflicts of interest.

## Data availability statement

No datasets were generated or analyzed in this work.