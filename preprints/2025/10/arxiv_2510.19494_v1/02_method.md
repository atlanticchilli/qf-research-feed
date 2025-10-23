---
authors:
- Fernando Alonso
- Álvaro Leitao
- Carlos Vázquez
doc_id: arxiv:2510.19494v1
family_id: arxiv:2510.19494
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Quantum Machine Learning methods for Fourier-based distribution estimation
  with application in option pricing
url_abs: http://arxiv.org/abs/2510.19494v1
url_html: https://arxiv.org/html/2510.19494v1
venue: arXiv q-fin
version: 1
year: 2025
---


Fernando Alonso
CITIC Research center, Spain
Galician Supercomputing Center (CESGA), Spain

Álvaro Leitao
CITIC Research center, Spain
Department of Mathematics, University of A Coruña, Spain
Corresponding author: alvaro.leitao@udc.gal

Carlos Vázquez
CITIC Research center, Spain
Department of Mathematics, University of A Coruña, Spain

(October 22, 2025)

###### Abstract

The ongoing progress in quantum technologies has fueled a sustained exploration of their potential applications across various domains. One particularly promising field is quantitative finance, where a central challenge is the pricing of financial derivatives—traditionally addressed through Monte Carlo integration techniques. In this work, we introduce two hybrid classical–quantum methods to address the option pricing problem. These approaches rely on reconstructing Fourier series representations of statistical distributions from the outputs of Quantum Machine Learning (QML) models based on Parametrized Quantum Circuits (PQCs). We analyze the impact of data size and PQC dimensionality on performance. Quantum Accelerated Monte Carlo (QAMC) is employed as a benchmark to quantitatively assess the proposed models in terms of computational cost and accuracy in the extraction of Fourier coefficients. Through the numerical experiments, we show that the proposed methods achieve remarkable accuracy, becoming a competitive quantum alternative for derivatives valuation.

## 1 Introduction

Quantum computing is a field that studies how information processing can be optimized by leveraging the principles of quantum mechanics. Since its inception, significant advances have been made in the design of algorithms and the development of quantum hardware. This has led to a surge in quantum technologies and a continuous search for their applications across various areas. One of these areas is quantitative finance, and the main reason for exploring this field is that some of the internal procedures currently used by financial institutions require highly demanding computations. One of the most relevant applications in finance is the valuation of financial derivatives, which consists of determining the price of a derivative at any date prior to a known maturity date, given by a payoff established in the contract. A derivative is a financial contract, the price of which depends on the future evolution of one or several financial products or rates, which are referred to as underlying. Options represent a main class of derivatives (see [[1](https://arxiv.org/html/2510.19494v1#bib.bibx1)], for a general introduction to options and derivatives).

Several proposals of quantum computing developments for financial applications have been explored in recent years, including the pricing of financial derivatives, as described in some review articles (see [[2](https://arxiv.org/html/2510.19494v1#bib.bibx2)], [[3](https://arxiv.org/html/2510.19494v1#bib.bibx3)] or [[4](https://arxiv.org/html/2510.19494v1#bib.bibx4)], for example). Among the possible quantum computing techniques for options pricing, we can find the so-called Quantum Accelerated Monte Carlo (QAMC) algorithms (see [[5](https://arxiv.org/html/2510.19494v1#bib.bibx5)], [[6](https://arxiv.org/html/2510.19494v1#bib.bibx6)] or [[7](https://arxiv.org/html/2510.19494v1#bib.bibx7)], for example). For these algorithms, the pricing problem is posed in terms of an expectation, which leads to the computation of an integral. In the QAMC approach, this integral is mainly obtained by means of an amplitude estimation algorithm, where the solution of the integral is encapsulated into the amplitude of a quantum state. More precisely, three main steps are involved: a quantum circuit to sample the paths for a prescribed probability distribution, a quantum operator to encode the payoff of the derivative and the aforementioned amplitude estimation routine. This idea has been recently exploited in [[8](https://arxiv.org/html/2510.19494v1#bib.bibx8)], where a specific QAMC method proposed in [[9](https://arxiv.org/html/2510.19494v1#bib.bibx9)] is applied to price derivatives with potential negative price. We note that other recent methodologies to calculate integrals with quantum computers are based on the decomposition of the integrand into Fourier series using quantum machine learning models, such as in [[10](https://arxiv.org/html/2510.19494v1#bib.bibx10)] or [[11](https://arxiv.org/html/2510.19494v1#bib.bibx11)]. Alternative formulations for option pricing based on partial differential equations (PDEs) transform the classical PDE for the problem into the propagation governed by an appropriate Hamiltonian operator (see [[12](https://arxiv.org/html/2510.19494v1#bib.bibx12)], with additional ideas in [[13](https://arxiv.org/html/2510.19494v1#bib.bibx13)] and [[14](https://arxiv.org/html/2510.19494v1#bib.bibx14)]).

The core ingredient in the present work relies on the area of Quantum Machine Learning (QML), from which different proposals have already been made to address financial problems, such as in [[15](https://arxiv.org/html/2510.19494v1#bib.bibx15)], [[16](https://arxiv.org/html/2510.19494v1#bib.bibx16)] or [[17](https://arxiv.org/html/2510.19494v1#bib.bibx17)], for example. Among the QML models, one of the most well-known approaches is to construct quantum circuits containing sets of gates, some of which depend on certain parameters that are typically adjusted according to a criterion based on the output of the circuit, thus looking for the set of parameters that provides the optimal value that minimizes a cost function. This classical–quantum concept is known in the literature as Parametrized Quantum Circuits (PQCs). In the context of QML, the ability of PQCs to approximate functions belonging to certain functional spaces has been studied in works like [[18](https://arxiv.org/html/2510.19494v1#bib.bibx18)] and [[19](https://arxiv.org/html/2510.19494v1#bib.bibx19)], with positive results when PQCs configurations are expressed in terms generalized trigonometric series. More recently, in [[8](https://arxiv.org/html/2510.19494v1#bib.bibx8)] and [[20](https://arxiv.org/html/2510.19494v1#bib.bibx20)] a rigorous analysis has been carried out on the approximation of continuous functions and functions in different Sobolev spaces by means these PQCs configurations. In the present article, we recall some of the theorems from [[20](https://arxiv.org/html/2510.19494v1#bib.bibx20)] that constitute the theoretical basis of the here proposed QML methodology to approximate the involved probability distributions by means of PQCs. More recently, in [[11](https://arxiv.org/html/2510.19494v1#bib.bibx11)] the authors propose a methodology for computing Monte Carlo integrals by decomposing the integrand in trigonometric Fourier series, the coefficients of which are approximated by specific PQCs, namely the so called quantum neuronal networks (QNN). Next, the integration of the trigonometric terms is performed with iterated quantum amplitude estimation techniques (IQAE). Unlike the work in [[11](https://arxiv.org/html/2510.19494v1#bib.bibx11)], in this article we address the Fourier expansion of the payoff of the derivative with the exact coefficients while the probability distribution is obtained from PQCs, that learn the respective Fourier coefficients. Then, the integral estimate can be obtained as the sum of products of coefficients corresponding to the expansion of the two factors of the integral, namely the payoff and the probability distribution. Indeed, for the probability distribution we propose two characterization: the probability density function or the cumulative density function. Moreover, in our financial application, this approach provides the relevant flexibility with great practical interest of getting the information about the probability distribution from samples of the prices of the underlying taken from the market.

Thus, in the present article, a classical–quantum method for the pricing of financial derivatives is proposed and formulated, based on the outputs of QML models built with PQCs, that enables to address the valuation problem pricing from a novel perspective, combining QML tools with fundamental principles of quantitative finance. Within this framework, two different training approaches have been developed to calculate the price of the derivative with the goal of leveraging the expressive power and generalization capabilities that these models offer, in various practical scenarios. Moreover, in order to assess the performance of the designed circuits through numerical results, QAMC is used to obtain a meaningful comparison in terms of both cost and accuracy in the extraction of Fourier coefficients.

The manuscript is organized as follows. In Section [2](https://arxiv.org/html/2510.19494v1#S2 "2 Preliminaries ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"), we introduce the fundamental concepts that will serve as a foundation throughout the article. More precisely, in Section [2.1](https://arxiv.org/html/2510.19494v1#S2.SS1 "2.1 Basic concepts on options pricing ‣ 2 Preliminaries ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"), an overview of the pricing problem is given; in Section [2.2](https://arxiv.org/html/2510.19494v1#S2.SS2 "2.2 PQCs as universal approximators ‣ 2 Preliminaries ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"), we demonstrate how, with an appropriate choice of PQC, it is possible to construct Fourier series capable of approximating specific functions; and in Section [2.3](https://arxiv.org/html/2510.19494v1#S2.SS3 "2.3 Quantum accelerated Monte Carlo techniques ‣ 2 Preliminaries ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"), a brief overview is provided on how the QAMC tackles the problems written in terms of expectations. Section [3](https://arxiv.org/html/2510.19494v1#S3 "3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing") is devoted to the introduction of the newly proposed method based on the use of a QML model built on PQCs. In the first part, Section [3.1](https://arxiv.org/html/2510.19494v1#S3.SS1 "3.1 Fourier series approximation of PDF and CDF ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"), the mathematical formulation of the first two methods is presented. In the second part, Section [3.2](https://arxiv.org/html/2510.19494v1#S3.SS2 "3.2 Methodology ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"), the implementation of each method is carefully described. Then, in Section [4](https://arxiv.org/html/2510.19494v1#S4 "4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"), the numerical results obtained are presented, specifying the experimental settings in Section [4.1](https://arxiv.org/html/2510.19494v1#S4.SS1 "4.1 Experiment setting ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"), and discussing the impact of the data size and the PQC dimension schemes employed in Section [4.2.1](https://arxiv.org/html/2510.19494v1#S4.SS2.SSS1 "4.2.1 Impact of the data size ‣ 4.2 Results and discussion ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing") and Section [4.2.2](https://arxiv.org/html/2510.19494v1#S4.SS2.SSS2 "4.2.2 Impact of the number of coefficients ‣ 4.2 Results and discussion ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"), respectively. Finally, the main conclusions are summarized in Section [5](https://arxiv.org/html/2510.19494v1#S5 "5 Conclusions ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing").

## 2 Preliminaries

### 2.1 Basic concepts on options pricing

One of the fundamental areas in quantitative finance concerns the pricing of financial derivatives. A derivative is a financial product whose price depends on the price of another financial product or the value of another financial magnitude (interest rate, exchange rate, etc.) on future dates. This financial magnitude or product is referred to as an underlying factor or underlying asset. In the class of European derivatives, there is usually a unique future date to be considered that is termed the maturity date. Thus, the pricing of financial derivatives consists in determining the price of the derivative at any date prior to its maturity, as the value at maturity is known and given by a payoff established in the contract. Among financial derivatives, which also include forward contracts and futures among others, we will focus on options contracts. European options give the owner the right, but not the obligation, to buy/sell the underlying asset at maturity date or receive the payoff at that date (for example, see [[1](https://arxiv.org/html/2510.19494v1#bib.bibx1)] for a review of option types, practical use, and their pricing). Therefore, option pricing requires taking into account the future and uncertain dynamics of the underlying asset price, which is assumed to be a stochastic process (i.e., a random variable at each time). Such dynamics is typically modeled in terms of stochastic differential equations (SDEs). Therefore, the option price is also a stochastic process.

In this section, we introduce the main mathematical concepts and notation to address the option pricing techniques proposed in this article. Let StS\_{t} and vtv\_{t}, respectively, denote the prices of the underlying asset and the option at time t∈[0,T]t\in[0,T], where TT is the maturity date. In view of the previous arguments, we can assume that vt=V​(t,St)v\_{t}=V(t,S\_{t}), for some function V:[0,T]×ℝ→ℝV:[0,T]\times\mathbb{R}\rightarrow\mathbb{R} that relates the option price to time and the underlying asset price. A European option specifies the payoff hh received by its holder at maturity date, which depends on the underlying asset price at maturity date:

|  |  |  |
| --- | --- | --- |
|  | vT=h​(T,ST).v\_{T}=h(T,S\_{T}). |  |

Using option pricing theory (see [[1](https://arxiv.org/html/2510.19494v1#bib.bibx1)], for example), the price of a European option at time t<Tt<T can be obtained in terms of a conditional expectation in the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | vt=e−r​(T−t)​𝔼ℚ​[h​(T,ST)∣ℱt]=e−r​(T−t)​∫ℝh​(T,y)​f​(y∣ℱt)​𝑑y,v\_{t}=e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}\left[h(T,S\_{T})\mid\mathcal{F}\_{t}\right]=e^{-r(T-t)}\int\_{\mathbb{R}}h(T,y)~f(y\mid\mathcal{F}\_{t})\,dy, |  | (1) |

where 𝔼ℚ\mathbb{E}^{\mathbb{Q}} denotes the expectation under a probability measure ℚ\mathbb{Q}111In the literature, it is common to refer to it as the risk-neutral measure., rr is the constant risk-free interest rate and ℱt\mathcal{F}\_{t} denotes the σ\sigma-algebra containing the market information available up to time tt, which is assumed to be known. Moreover, f​(⋅)f(\cdot) is the probability density function (PDF) of the asset price process StS\_{t} under ℚ\mathbb{Q}.

Note that the expression ([1](https://arxiv.org/html/2510.19494v1#S2.E1 "In 2.1 Basic concepts on options pricing ‣ 2 Preliminaries ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")) indicates that the value of the derivative at time tt is the discounted price of the expected payoff, conditional on the market information available up to time tt. Moreover, in view of expression ([1](https://arxiv.org/html/2510.19494v1#S2.E1 "In 2.1 Basic concepts on options pricing ‣ 2 Preliminaries ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")), the computation of the expectation to obtain the option price requires appropriate integration methods for general payoff and PDF expressions. In the present research work we mainly aim to take advantage of QML techniques to estimate the PDF and approximate this integral.

### 2.2 PQCs as universal approximators

A very common approach within the quantum-classical framework of QML consists of using trainable quantum circuits as models, in a similar way to neural networks. In this approach, quantum gates are used both to encode the data inputs, x=(x1,…,xN)x=(x\_{1},\ldots,x\_{N}), and to implement trainable weights, 𝜽=(θ1,…,θM)\boldsymbol{\theta}=(\theta\_{1},\ldots,\theta\_{M}). The circuit is measured multiple times to estimate the expected value of an observable, and this result is understood as a prediction, leading to the implementation of a function fθ​(x)f\_{\theta}(x). This approach is referred by various authors in the literature as PQCs (see for example [[21](https://arxiv.org/html/2510.19494v1#bib.bibx21)], [[22](https://arxiv.org/html/2510.19494v1#bib.bibx22)] or [[23](https://arxiv.org/html/2510.19494v1#bib.bibx23)]). The information extracted from the circuit and the process of evaluating the cost function are both classical, which makes PQC-based algorithms hybrid.

Let a univariate quantum model be defined as the expectation value of an observable with respect to a state prepared by a PQC, that is:

|  |  |  |
| --- | --- | --- |
|  | fθ​(x)=⟨0|U†​(x,𝜽)​M​U​(x,𝜽)|0⟩,f\_{\theta}(x)=\langle 0|U^{\dagger}(x,\boldsymbol{\theta})MU(x,\boldsymbol{\theta})|0\rangle, |  |

where |0⟩|0\rangle is one of the computational basis states, U​(x,𝜽)U(x,\boldsymbol{\theta}) is a quantum circuit that depends on the input (xx) and on a set of parameters (𝜽\boldsymbol{\theta}), and MM is an observable. The quantum circuit representing our model will be constructed from LL layers, each one consisting of a data-encoding block SH​(x)S\_{H}(x) and a trainable block W​(𝜽)W(\boldsymbol{\theta}) controlled by the parameters 𝜽\boldsymbol{\theta}, as shown in Figure [1](https://arxiv.org/html/2510.19494v1#S2.F1 "Figure 1 ‣ 2.2 PQCs as universal approximators ‣ 2 Preliminaries ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"). For simplicity, in the subsequent developments, we will assume that the trainable blocks are arbitrary unitary operations, i.e., W​(𝜽)=WW(\boldsymbol{\theta})=W, and we will omit the subscript in f𝜽f\_{\boldsymbol{\theta}} hereafter. Thus, the total quantum circuit has the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(x)=W(L+1)​(𝜽)​SH​(x)​W(L)​(𝜽)​⋯​W(2)​(𝜽)​SH​(x)​W(1)​(𝜽),U(x)=W^{(L+1)}(\boldsymbol{\theta})S\_{H}(x)W^{(L)}(\boldsymbol{\theta})\cdots W^{(2)}(\boldsymbol{\theta})S\_{H}(x)W^{(1)}(\boldsymbol{\theta}), |  | (2) |

where the data-encoding block is identical in each layer and has the form
SH​(x)=e−x1​H⊗⋯⊗e−xN​HS\_{H}(x)=e^{-x\_{1}H}\otimes\cdots\otimes e^{-x\_{N}H},
for HH a Hamiltonian that generates the time evolution used to encode the data.

![Refer to caption](x1.png)


Figure 1: Scheme of a quantum circuit composed of LL layers, where each layer consists of a trainable circuit block W(i)​(𝜽)W^{(i)}(\boldsymbol{\theta}), with i∈{1,…,L}i\in\{1,\ldots,L\}, and a data-encoding block SH​(x)S\_{H}(x), from [[18](https://arxiv.org/html/2510.19494v1#bib.bibx18)].

In this context, the fundamental idea under the developments we will carry out is that, given an appropriate choice of circuits, the quantum function representing our model can be written as a Fourier series of the form

|  |  |  |
| --- | --- | --- |
|  | fθ​(x)=∑ω∈Ωcω​(θ)​ei​ω​x.f\_{\theta}(x)=\sum\_{\omega\in\Omega}c\_{\omega}(\theta)e^{i\omega x}. |  |

Several references in the literature prove that the frequency spectrum (Ω⊆ℝN\Omega\subseteq\mathbb{R}^{N}) is completely determined by the eigenvalues of the Hamiltonians forming the encoding block, while the complete circuit design controls the coefficients (cωc\_{\omega}) that a quantum model can adjust (for example, see [[18](https://arxiv.org/html/2510.19494v1#bib.bibx18)] and [[19](https://arxiv.org/html/2510.19494v1#bib.bibx19)]). Moreover, in many cases the frequencies are integers (Ω⊆ℤN\Omega\subseteq\mathbb{Z}^{N}), and the sum becomes a partial Fourier series222The term partial Fourier series indicates that only a subset of the Fourier coefficients are nonzero.

|  |  |  |
| --- | --- | --- |
|  | fθ​(x)=∑n∈Ωcn​(θ)​ei​n​x,f\_{\theta}(x)=\sum\_{n\in\Omega}c\_{n}(\theta)e^{inx}, |  |

where the functions ei​n​xe^{inx} form an orthogonal basis. This formalism allows quantum models to be studied using the tools of Fourier analysis.

From the aforementioned results, it arises the intuition that, employing a sufficiently large number of repetitions of encoding gates or Hamiltonians with sufficiently large dimension and suitably non-degenerate spectrum, quantum models can approximate a wide range of functions.

Thus two key aspects appear: the *universality* and the *expressivity* of PQCs, that is, the ability of PQCs to approximate any function belonging to a given function space defined over a prescribed domain, up to arbitrary precision with respect to a specific norm. This idea was first explored in [[18](https://arxiv.org/html/2510.19494v1#bib.bibx18)] and [[19](https://arxiv.org/html/2510.19494v1#bib.bibx19)], and following these developments it is shown that, if trainable circuit blocks are allowed with sufficient flexibility to implement arbitrary global unitary gates, then there exists a quantum model with L=1L=1 capable of realizing any possible set of Fourier coefficients.

Furthermore, in [[24](https://arxiv.org/html/2510.19494v1#bib.bibx24)] and Chapter 5 of [[20](https://arxiv.org/html/2510.19494v1#bib.bibx20)] it has been proven that PQCs can approximate arbitrarily well the space of continuous functions, the space of pp-integrable functions and the Sobolev space HkH^{k}, which is the set of functions whose derivatives up to order kk are L2L^{2}-integrable. Before recalling these results, it is necessary to introduce the following definition of universal Hamiltonian family proposed in [[18](https://arxiv.org/html/2510.19494v1#bib.bibx18)].

###### Definition 2.1.

Let {Hm∣m∈ℕ}\{H\_{m}\mid m\in\mathbb{N}\} be a Hamiltonian family where HmH\_{m} acts on mm subsystems
of dimension dd.
Such a Hamiltonian family gives rise to a family of models {fm}\{f\_{m}\} in the following way:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fm​(x)=⟨Γ|SHm†​(x)​M​SHm​(x)|Γ⟩.f\_{m}(x)=\langle\Gamma\,|\,S^{\dagger}\_{H\_{m}}(x)MS\_{H\_{m}}(x)\,|\,\Gamma\rangle. |  | (3) |

Furthermore, for each m∈ℕm\in\mathbb{N}, the set
ΩHm:={λjm−λkm|j,k∈{1,…,dm}}\Omega\_{H\_{m}}:=\bigl\{\lambda^{m}\_{j}-\lambda^{m}\_{k}\;\big|\;j,k\in\{1,\dots,d\_{m}\}\bigr\},
where {λ1m,…,λdmm}\{\lambda^{m}\_{1},\dots,\lambda^{m}\_{d\_{m}}\} are the eigenvalues of HmH\_{m},
is defined as the *frequency spectrum* of HmH\_{m}. A Hamiltonian family is a universal Hamiltonian family if for any Z∈ℕZ\in\mathbb{N} there exists m∈ℕm\in\mathbb{N} such that {−Z,…,0,…,Z}⊂Hm​(Ω)\{-Z,\dots,0,\dots,Z\}\subset H\_{m}(\Omega).

Based on the previous definition, in Chapter 5 of [[20](https://arxiv.org/html/2510.19494v1#bib.bibx20)], the following three theorems have been proved.

###### Theorem 2.1.

(Convergence in C0C^{0})

Let {Hm}\{H\_{m}\} be a universal Hamiltonian family,
and {fm}\{f\_{m}\} the associated quantum model family ([3](https://arxiv.org/html/2510.19494v1#S2.E3 "In Definition 2.1. ‣ 2.2 PQCs as universal approximators ‣ 2 Preliminaries ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")).
For all functions f∗∈C0​(U)f^{\ast}\in C\_{0}(U) where UU is compactly contained
in [0,2​π]N[0,2\pi]^{N}, and for all ϵ>0\epsilon>0,
there exists some m′∈ℕm^{\prime}\in\mathbb{N}, some state
|Γ⟩∈ℂdm′\lvert\Gamma\rangle\in\mathbb{C}^{d\_{m^{\prime}}}, and some observable MM such that
fm′f\_{m^{\prime}} converges uniformly to f∗f^{\ast}:

|  |  |  |
| --- | --- | --- |
|  | ‖fm′−f∗‖C0<ϵ.\|f\_{m^{\prime}}-f^{\ast}\|\_{C^{0}}<\epsilon. |  |

with

|  |  |  |
| --- | --- | --- |
|  | ‖fm′−f∗‖C0:=supx∈[0,2​π]N‖fm′​(x)−f∗​(x)‖.\|f\_{m^{\prime}}-f^{\ast}\|\_{C^{0}}:=\sup\_{x\in[0,2\pi]^{N}}\|f\_{m^{\prime}}(x)-f^{\ast}(x)\|. |  |

###### Theorem 2.2.

(Convergence in LpL^{p})

Let {Hm}\{H\_{m}\} be a universal Hamiltonian family,
and {fm}\{f\_{m}\} the associated quantum model family ([3](https://arxiv.org/html/2510.19494v1#S2.E3 "In Definition 2.1. ‣ 2.2 PQCs as universal approximators ‣ 2 Preliminaries ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")).
For all functions f∗∈Lp​([0,2​π]N)f^{\ast}\in L^{p}\!\bigl([0,2\pi]^{N}\bigr)
where 1≤p<∞1\leq p<\infty, and for all ϵ>0\epsilon>0,
there exists some m′∈ℕm^{\prime}\in\mathbb{N}, some state
|Γ⟩∈ℂdm′\lvert\Gamma\rangle\in\mathbb{C}^{d\_{m^{\prime}}}, and some observable MM such that:

|  |  |  |
| --- | --- | --- |
|  | ‖fm′−f∗‖Lp<ϵ,\|f\_{m^{\prime}}-f^{\ast}\|\_{L^{p}}<\epsilon, |  |

with

|  |  |  |
| --- | --- | --- |
|  | ‖fm′−f∗‖Lp:=(∫[0,2​π]N|fm′−f∗|p​𝑑P)1/p.\|f\_{m^{\prime}}-f^{\ast}\|\_{L^{p}}:=\left(\int\_{[0,2\pi]^{N}}|f\_{m^{\prime}}-f^{\ast}|^{p}\,dP\right)^{1/p}. |  |

###### Theorem 2.3.

(Convergence in HkH^{k})

Let {Hm}\{H\_{m}\} be a universal Hamiltonian family
and {fm}\{f\_{m}\} the associated quantum model family ([3](https://arxiv.org/html/2510.19494v1#S2.E3 "In Definition 2.1. ‣ 2.2 PQCs as universal approximators ‣ 2 Preliminaries ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")).
For all functions f∗∈Hk+1​(U)f^{\ast}\in H^{k+1}(U) where UU is compactly contained
in the closed cube [0,2​π]N[0,2\pi]^{N}, and for all ϵ>0\epsilon>0,
there exists some m′∈ℕm^{\prime}\in\mathbb{N}, some state
|Γ⟩∈ℂdm′\lvert\Gamma\rangle\in\mathbb{C}^{d\_{m^{\prime}}}, and some observable MM such
that fm′f\_{m^{\prime}} converges to f∗f^{\ast} with respect to the HkH^{k}–norm:

|  |  |  |
| --- | --- | --- |
|  | ‖fm′−f∗‖Hk<ϵ,\|f\_{m^{\prime}}-f^{\ast}\|\_{H^{k}}<\epsilon, |  |

with

|  |  |  |
| --- | --- | --- |
|  | ‖fm′−f∗‖Hk:=(∑|α|≤k∫U|∂|α|∂x1α1​⋯​∂xNαN​(fm′−f∗)​(x)|2​𝑑P​(x))1/2.\displaystyle\|f\_{m^{\prime}}-f^{\ast}\|\_{H^{k}}:=\left(\sum\_{|\alpha|\leq k}\int\_{U}\Bigg|\frac{\partial^{|\alpha|}}{\partial x\_{1}^{\alpha\_{1}}\cdots\partial x\_{N}^{\alpha\_{N}}}(f\_{m^{\prime}}-f^{\ast})(x)\Bigg|^{2}\,dP(x)\right)^{1/2}. |  |

As discussed in Chapter 6 of [[20](https://arxiv.org/html/2510.19494v1#bib.bibx20)], the relevance of these results is that the generalization bounds of the empirical risk defined in H1H^{1} imply the minimization of the empirical risk in C0C^{0}. This is really strong because the convergence in the sense of C0C^{0} is equivalent to a convergence of every point to the true solution.

### 2.3 Quantum accelerated Monte Carlo techniques

Monte Carlo method is one of the best-known integration techniques for solving option pricing problems, when formulated in terms of expectations. This method gives an approximation of the value of definite integrals by generating random samples within the integration region and computing the average value of the function evaluated in these samples [[25](https://arxiv.org/html/2510.19494v1#bib.bibx25)].

Let us consider the definite integral

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[g​(x)]=∫xminxmaxg​(x)​f​(x)​𝑑x,\mathbb{E}[g(x)]=\int\_{x\_{\text{min}}}^{x\_{\text{max}}}g(x)f(x)\,dx, |  |

where ff is a PDF with support contained in the interval [xmin,xmax][x\_{\text{min}},x\_{\text{max}}] and gg is a function of interest, namely, the payoff in the options pricing problem. The Monte Carlo method consists in generating II independent and identically distributed samples xix\_{i}, for i=0,…,I−1i=0,\dots,I-1, drawn from the PDF ff, such that the value of the integral is approximated by

|  |  |  |
| --- | --- | --- |
|  | ∫xminxmaxg​(x)​f​(x)​𝑑x≈∑i=0I−1g​(xi)​f​(xi).\int\_{x\_{\text{min}}}^{x\_{\text{max}}}g(x)f(x)\,dx\approx\sum\_{i=0}^{I-1}g(x\_{i})f(x\_{i}). |  |

Since this method can be computationally demanding for certain types of integrals, in recent years the advantages offered by quantum computing have been exploited to develop the QAMC method [[26](https://arxiv.org/html/2510.19494v1#bib.bibx26)], which achieves a quadratic improvement, in terms of the mean squared error, in the number of queries required compared to its classical counterpart.

The idea behind this method is to encapsulate the value of the expectation within the amplitudes of a quantum state, and then maximize the probability of obtaining
this value when performing a measurement. For this purpose, the following state is constructed

|  |  |  |
| --- | --- | --- |
|  | |ψ⟩=∑x=02n−1g​(x)​f​(x)​|x⟩n​|1⟩+∑x=02n−1(1−g​(x))​f​(x)​|x⟩n​|0⟩.|\psi\rangle=\sum\_{x=0}^{2^{n}-1}\sqrt{g(x)f(x)}\,|x\rangle^{n}|1\rangle+\sum\_{x=0}^{2^{n}-1}\sqrt{(1-g(x))f(x)}\,|x\rangle^{n}|0\rangle. |  |

If we now conveniently define the following quantities

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | q\displaystyle q | =\displaystyle= | ∑x=02n−1g​(x)​f​(x)≈𝔼​[g​(x)]\displaystyle\sum\_{x=0}^{2^{n}-1}g(x)f(x)\approx\mathbb{E}[g(x)] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |ψ~1⟩\displaystyle|\tilde{\psi}\_{1}\rangle | =\displaystyle= | 1q​∑x=02n−1g​(x)​f​(x)​|x⟩n,\displaystyle\frac{1}{\sqrt{q}}\sum\_{x=0}^{2^{n}-1}\sqrt{g(x)}\sqrt{f(x)}\,|x\rangle^{n}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |ψ~0⟩\displaystyle|\tilde{\psi}\_{0}\rangle | =\displaystyle= | 11−q​∑x=02n−11−g​(x)​f​(x)​|x⟩n,\displaystyle\frac{1}{\sqrt{1-q}}\sum\_{x=0}^{2^{n}-1}\sqrt{1-g(x)}\sqrt{f(x)}\,|x\rangle^{n}, |  |

and rewrite |ψ⟩|\psi\rangle as

|  |  |  |
| --- | --- | --- |
|  | |ψ⟩=q​|ψ~1⟩​|1⟩+1−q​|ψ~0⟩​|0⟩,|\psi\rangle=\sqrt{q}\,|\tilde{\psi}\_{1}\rangle|1\rangle+\sqrt{1-q}\,|\tilde{\psi}\_{0}\rangle|0\rangle, |  |

we can observe that the problem can be solved through Quantum Amplitude Estimation (QAE) [[27](https://arxiv.org/html/2510.19494v1#bib.bibx27)], since the probability
of the state aa corresponds to the integral to be computed, that estimates 𝔼​[g​(x)]\mathbb{E}[g(x)].

However, QAMC presents some drawbacks for which several modifications of its original formulation have been proposed. For instance, to address the problem that emerges from the Quantum Phase Estimation (QPE) [[28](https://arxiv.org/html/2510.19494v1#bib.bibx28)] subroutine, alternatives such as the Iterative Quantum Amplitude Estimation (IQAE) [[29](https://arxiv.org/html/2510.19494v1#bib.bibx29)] or the Real Quantum Amplitude Estimation (RQAE) [[9](https://arxiv.org/html/2510.19494v1#bib.bibx9)] have been developed. Furthermore, to adequately prepare the initial quantum state different ideas have been proposed, as discussed in [[30](https://arxiv.org/html/2510.19494v1#bib.bibx30)], [[31](https://arxiv.org/html/2510.19494v1#bib.bibx31)], and [[32](https://arxiv.org/html/2510.19494v1#bib.bibx32)]. Other approaches include methods based on decomposing the integrand into Fourier series, such as Fourier Quantum Monte Carlo Integration (FQMCI) [[10](https://arxiv.org/html/2510.19494v1#bib.bibx10)] or Quantum Fourier Iterative Amplitude Estimation (QFIAE) [[11](https://arxiv.org/html/2510.19494v1#bib.bibx11)], which propose ways to compute the Fourier series using QML.

## 3 Formulation and methodology

As previously mentioned, in quantitative finance, efficient numerical methods are required to value complex contracts and calibrate various financial models. Existing methods can be classified into three main groups: numerical methods for partial differential equations, Monte Carlo simulation techniques, and numerical integration methods, each presenting its own advantages and disadvantages depending on the specific financial application.

As mentioned before, the rise of quantum computing can lead to a new set of methods which can accelerate numerical simulations and potentially achieve more efficient valuation and calibration of complex financial models. In this work, we explore such potential through classical–quantum techniques built on PQC-based QML models. The following sections describe the formulation and implementation of these techniques, along with the methodology

### 3.1 Fourier series approximation of PDF and CDF

The here proposed approaches rely on the use of trigonometric Fourier series, that is, series based on sine and cosine functions. They rely on the same idea, although their main difference is that the first one uses the trigonometric series of the PDF, as in [[33](https://arxiv.org/html/2510.19494v1#bib.bibx33)], and the second one uses the trigonometric series of the cumulative distribution function (CDF), as in [[34](https://arxiv.org/html/2510.19494v1#bib.bibx34)].

#### 3.1.1 PDF approximation formulation

Returning to the formulation ([1](https://arxiv.org/html/2510.19494v1#S2.E1 "In 2.1 Basic concepts on options pricing ‣ 2 Preliminaries ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")) of the derivative pricing problem for European vanilla options, the starting point lies in the calculation of the pricing formula under the risk-neutral measure, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t0,x)=e−r​(T−t0)​𝔼ℚ​[h​(T,y)|x]=e−r​(T−t0)​∫ℝh​(T,y)​f​(y|x)​𝑑y,V(t\_{0},x)=e^{-r(T-t\_{0})}\,\mathbb{E}^{\mathbb{Q}}[h(T,y)|x]=e^{-r(T-t\_{0})}\int\_{\mathbb{R}}h(T,y)f(y|x)\,dy, |  | (4) |

where xx and yy are the state variables at times t0t\_{0} and TT, respectively, and f​(y|x)f(y|x) is the probability density of yy conditioned on xx.

In finance, it is common to work in practice with PDFs whose tails tend to vanish, so it can be assumed that there exists an interval [a,b]⊂ℝ[a,b]\subset\mathbb{R} such that the integral in ([4](https://arxiv.org/html/2510.19494v1#S3.E4 "In 3.1.1 PDF approximation formulation ‣ 3.1 Fourier series approximation of PDF and CDF ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")) can be approximated without significant loss of accuracy, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t0,x)≈e−r​(T−t0)​∫abh​(T,y)​f​(y|x)​𝑑y.V(t\_{0},x)\approx e^{-r(T-t\_{0})}\int\_{a}^{b}h(T,y)f(y|x)\,dy. |  | (5) |

Since f​(y|x)f(y|x) is usually not known explicitly, we can approximate the density by its 𝒦\mathcal{K}-truncated trigonometric Fourier series expansion in yy

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(y|x)≈A0f2+∑k=1𝒦(Akf​cos⁡(2​π​k​(y−a)b−a)+Bkf​sin⁡(2​π​k​(y−a)b−a)),f(y|x)\approx\frac{A\_{0}^{f}}{2}+\sum\_{k=1}^{\mathcal{K}}\left(A\_{k}^{f}\cos\left(2\pi k\frac{(y-a)}{b-a}\right)+B\_{k}^{f}\sin\left(2\pi k\frac{(y-a)}{b-a}\right)\right), |  | (6) |

where

|  |  |  |
| --- | --- | --- |
|  | Akf=2b−a​∫abf​(y|x)​cos⁡(2​π​k​(y−a)b−a)​𝑑y,A\_{k}^{f}=\frac{2}{b-a}\int\_{a}^{b}f(y|x)\cos\left(2\pi k\frac{(y-a)}{b-a}\right)\,dy, |  |

and

|  |  |  |
| --- | --- | --- |
|  | Bkf=2b−a​∫abf​(y|x)​sin⁡(2​π​k​(y−a)b−a)​𝑑y.B\_{k}^{f}=\frac{2}{b-a}\int\_{a}^{b}f(y|x)\sin\left(2\pi k\frac{(y-a)}{b-a}\right)\,dy. |  |

It should be remarked that regarding the underlying asset price process, we can use the same arguments as in [[33](https://arxiv.org/html/2510.19494v1#bib.bibx33)] to ensure that, due to the conditions required for the existence of the Fourier series, it is possible to truncate the number of terms in the series while controlling the accuracy.

By substituting equation ([6](https://arxiv.org/html/2510.19494v1#S3.E6 "In 3.1.1 PDF approximation formulation ‣ 3.1 Fourier series approximation of PDF and CDF ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")) into equation ([5](https://arxiv.org/html/2510.19494v1#S3.E5 "In 3.1.1 PDF approximation formulation ‣ 3.1 Fourier series approximation of PDF and CDF ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")), we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V​(t0,x)\displaystyle V(t\_{0},x) | ≈e−r​(T−t0)​∫abh​(T,y)​(A0f2+∑k=1𝒦Akf​cos⁡(2​π​k​(y−a)b−a))​𝑑y\displaystyle\approx e^{-r(T-t\_{0})}\int\_{a}^{b}h(T,y)\left(\frac{A\_{0}^{f}}{2}+\sum\_{k=1}^{\mathcal{K}}A\_{k}^{f}\cos\left(2\pi k\frac{(y-a)}{b-a}\right)\right)\,dy |  | (7) |
|  |  | +e−r​(T−t0)​∫abh​(T,y)​∑k=1𝒦Bkf​sin⁡(2​π​k​(y−a)b−a)​d​y.\displaystyle+e^{-r(T-t\_{0})}\int\_{a}^{b}h(T,y)\sum\_{k=1}^{\mathcal{K}}B\_{k}^{f}\sin\left(2\pi k\frac{(y-a)}{b-a}\right)\,dy. |  |

Next, if we now exchange the summation and the integral in ([7](https://arxiv.org/html/2510.19494v1#S3.E7 "In 3.1.1 PDF approximation formulation ‣ 3.1 Fourier series approximation of PDF and CDF ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")) and introduce the definitions

|  |  |  |
| --- | --- | --- |
|  | Ck:=2b−a​∫abh​(T,y)​cos⁡(2​π​k​(y−a)b−a)​𝑑y,C\_{k}:=\frac{2}{b-a}\int\_{a}^{b}h(T,y)\cos\left(2\pi k\frac{(y-a)}{b-a}\right)\,dy, |  |

and

|  |  |  |
| --- | --- | --- |
|  | Dk:=2b−a​∫abh​(T,y)​sin⁡(2​π​k​(y−a)b−a)​𝑑y,D\_{k}:=\frac{2}{b-a}\int\_{a}^{b}h(T,y)\sin\left(2\pi k\frac{(y-a)}{b-a}\right)\,dy, |  |

we obtain

|  |  |  |
| --- | --- | --- |
|  | V​(t0,x)≈12​(b−a)​e−r​Δ​t​(A0f⋅C02+∑k=1𝒦(Akf⋅Ck+Bkf⋅Dk)).V(t\_{0},x)\approx\frac{1}{2}(b-a)e^{-r\Delta t}\left(\frac{A\_{0}^{f}\cdot C\_{0}}{2}+\sum\_{k=1}^{\mathcal{K}}\left(A\_{k}^{f}\cdot C\_{k}+B\_{k}^{f}\cdot D\_{k}\right)\right). |  |

It should be noted that CkC\_{k} and DkD\_{k} are the coefficients of the trigonometric Fourier series of h​(T,y)h(T,y). Thus, the integral of the product of two real functions, f​(y|x)f(y|x) and h​(T,y)h(T,y) has been transformed into the sum of the product of the respective coefficients of their trigonometric Fourier series.

#### 3.1.2 CDF approximation formulation

In the original formulation of the valuation integral, the integrand may have either infinite or bounded support, and the payoff function may be only piecewise smooth and have discontinuities. Therefore, working directly with the PDF can be numerically unstable or ill-posed. Unlike the PDF, the CDF provides a smoother and continuous representation of the underlying variable’s behavior regardless its critical features, which allows to efficiently handle discontinuities and to come up with more stable numerical approximations.

Firstly, assuming that the derivative of the payoff function has a discontinuity at c∈[a,b]c\in[a,b], we split valuation integral as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t0,x)\displaystyle V(t\_{0},x) | =e−r​(T−t0)​∫abh​(T,y)​f​(y|x)​𝑑y\displaystyle=e^{-r(T-t\_{0})}\int\_{a}^{b}h(T,y)f(y|x)\,dy |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =e−r​(T−t0)​(∫ach​(T,y)​f​(y|x)​𝑑y+∫cbh​(T,y)​f​(y|x)​𝑑y).\displaystyle=e^{-r(T-t\_{0})}\left(\int\_{a}^{c}h(T,y)f(y|x)\,dy+\int\_{c}^{b}h(T,y)f(y|x)\,dy\right). |  |

Then, integrating by parts we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V​(t0,x)\displaystyle V(t\_{0},x) | =e−r​(T−t0)​(h​(T,b)​F​(b)−h​(T,a)​F​(a))\displaystyle=e^{-r(T-t\_{0})}\left(h(T,b)F(b)-h(T,a)F(a)\right) |  | (8) |
|  |  | −e−r​(T−t0)​(∫ach′​(T,y)​F​(y)​𝑑y+∫cbh′​(T,y)​F​(y)​𝑑y),\displaystyle-e^{-r(T-t\_{0})}\left(\int\_{a}^{c}h^{\prime}(T,y)F(y)\,dy+\int\_{c}^{b}h^{\prime}(T,y)F(y)\,dy\right), |  |

where the CDF is given by

|  |  |  |
| --- | --- | --- |
|  | F​(y)=∫−∞yf​(x)​𝑑x.F(y)=\int\_{-\infty}^{y}f(x)\,dx. |  |

Following the same reasoning as before, it is possible to define the Fourier series of period 2​(b−a)2(b-a) in an interval [a^,b^][\hat{a},\hat{b}], whose election will be later motivated. Thus, the Fourier series of the CDF is

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(y)≈A0F2+∑k=1𝒦(AkF​cos⁡(2​π​k​(y−a^)b^−a^)+BkF​sin⁡(2​π​k​(y−a^)b^−a^)).F(y)\approx\frac{A\_{0}^{F}}{2}+\sum\_{k=1}^{\mathcal{K}}\left(A\_{k}^{F}\cos\left(2\pi k\frac{(y-\hat{a})}{\hat{b}-\hat{a}}\right)+B\_{k}^{F}\sin\left(2\pi k\frac{(y-\hat{a})}{\hat{b}-\hat{a}}\right)\right). |  | (9) |

Substituting ([9](https://arxiv.org/html/2510.19494v1#S3.E9 "In 3.1.2 CDF approximation formulation ‣ 3.1 Fourier series approximation of PDF and CDF ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")) in ([8](https://arxiv.org/html/2510.19494v1#S3.E8 "In 3.1.2 CDF approximation formulation ‣ 3.1 Fourier series approximation of PDF and CDF ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")) and exchanging the summation with the integral we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t0,x)\displaystyle V(t\_{0},x) | ≈e−r​Δ​t​(h​(T,b)​F​(b)−h​(T,a)​F​(a))\displaystyle\approx e^{-r\Delta t}\left(h(T,b)F(b)-h(T,a)F(a)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −e−r​Δ​t​(A0F⋅C0a2+∑k=1𝒦(AkF⋅Cka+BkF⋅Dka))\displaystyle-e^{-r\Delta t}\left(\frac{A\_{0}^{F}\cdot C\_{0}^{a}}{2}+\sum\_{k=1}^{\mathcal{K}}\left(A\_{k}^{F}\cdot C\_{k}^{a}+B\_{k}^{F}\cdot D\_{k}^{a}\right)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −e−r​Δ​t​(A0F⋅C0b2+∑k=1𝒦(AkF⋅Ckb+BkF⋅Dkb))\displaystyle-e^{-r\Delta t}\left(\frac{A\_{0}^{F}\cdot C\_{0}^{b}}{2}+\sum\_{k=1}^{\mathcal{K}}\left(A\_{k}^{F}\cdot C\_{k}^{b}+B\_{k}^{F}\cdot D\_{k}^{b}\right)\right) |  |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Cka\displaystyle C\_{k}^{a} | :=∫ach′​(T,y)​cos⁡(2​π​k​(y−a^)b^−a^)​𝑑y,Dka:=∫ach′​(T,y)​sin⁡(2​π​k​(y−a^)b^−a^)​𝑑y,\displaystyle=\int\_{a}^{c}h^{\prime}(T,y)\cos\left(2\pi k\frac{(y-\hat{a})}{\hat{b}-\hat{a}}\right)dy,\,\,D\_{k}^{a}=\int\_{a}^{c}h^{\prime}(T,y)\sin\left(2\pi k\frac{(y-\hat{a})}{\hat{b}-\hat{a}}\right)dy, |  | (10) |
|  | Ckb\displaystyle C\_{k}^{b} | :=∫cbh′​(T,y)​cos⁡(2​π​k​(y−a^)b^−a^)​𝑑y,Dkb:=∫cbh′​(T,y)​sin⁡(2​π​k​(y−a^)b^−a^)​𝑑y.\displaystyle=\int\_{c}^{b}h^{\prime}(T,y)\cos\left(2\pi k\frac{(y-\hat{a})}{\hat{b}-\hat{a}}\right)dy,\,\,D\_{k}^{b}=\int\_{c}^{b}h^{\prime}(T,y)\sin\left(2\pi k\frac{(y-\hat{a})}{\hat{b}-\hat{a}}\right)dy. |  |

It should be remarked that, in contrast with the previous method, the quantities defined in ([10](https://arxiv.org/html/2510.19494v1#S3.E10 "In 3.1.2 CDF approximation formulation ‣ 3.1 Fourier series approximation of PDF and CDF ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")) do not correspond to the Fourier coefficients of the series that approximates h​(T,y)h(T,y), because the integration domain does not match with the one of the basis functions.

### 3.2 Methodology

As mentioned before, the proposed technique is based on the approximation of functions through Fourier series extracted from the QML models built on PQCs.
This approximation allows for a flexible capture of the functional structure of the distributions involved in the pricing models, taking advantage of the expressive and differentiable capabilities of these models. Moreover, the integration of classical and quantum computing provides an alternative framework for the valuation of derivatives and the approximation of complex financial functions. For this purpose, three approaches have been designed.

In the first one, supervised learning is employed, using datasets that contain both inputs and labeled outputs. In this case, a PQC is trained to approximate the PDF of the variable representing the underlying asset price and to extract its Fourier series. The coefficients corresponding to the payoff of the derivative are obtained analytically.

The second approach is more realistic from a practical point of view, since in derivatives pricing one rarely has access to the exact PDF of the underlying asset price, but to asset price’s evolution in time. Therefore, in this second case, self-supervised learning is employed, after providing the model with a sufficiently representative set of asset samples. From these samples, the model must infer the implicit distribution and estimate the coefficients needed to calculate the price of the derivative.

Note that, as argued in [[20](https://arxiv.org/html/2510.19494v1#bib.bibx20)], in both cases it is assumed that the probability distribution P​(x,y)P(x,y) yields a deterministic mapping for some function g∗:𝒳→𝒴g^{\*}:\mathcal{X}\rightarrow\mathcal{Y}. Therefore, to solve the classical problem

|  |  |  |
| --- | --- | --- |
|  | g=arg⁡ming^∈ℳ⁡R​(g^),g=\arg\min\_{\hat{g}\in\mathcal{M}}R(\hat{g}), |  |

for ℳ\mathcal{M} a subset of functions in some functional space. Instead of working with the joint probability distribution P​(x,y)P(x,y), so that

|  |  |  |
| --- | --- | --- |
|  | R​(g)=∫𝒳×𝒴ℓ​(g∗​(x),g​(x))​𝑑P​(x,y),R(g)=\int\_{\mathcal{X}\times\mathcal{Y}}\ell(g^{\*}(x),g(x))\,dP(x,y), |  |

it is possible to work with the marginal distribution P𝒳=P𝒳​(x)P\_{\mathcal{X}}=P\_{\mathcal{X}}(x), so that

|  |  |  |
| --- | --- | --- |
|  | R​(g)=∫𝒳ℓ​(g∗​(x),g​(x))​𝑑P𝒳​(x).R(g)=\int\_{\mathcal{X}}\ell(g^{\*}(x),g(x))\,dP\_{\mathcal{X}}(x). |  |

Since in both scenarios we will work in the Sobolev space H1​(𝒳)H^{1}(\mathcal{X}) where 𝒳⊂ℝ\mathcal{X}\subset\mathbb{R} and g∗∈𝒯⊆H1​(𝒳)g^{\*}\in\mathcal{T}\subseteq H^{1}(\mathcal{X}), the corresponding risk can be defined in terms of the usual norm in H1H^{1} as

|  |  |  |
| --- | --- | --- |
|  | RH1​(g)=‖g∗−g‖H12=∫𝒳(g∗​(x)−g​(x))2+(∂g∗​(x)∂x−∂g​(x)∂x)2​d​PX​(x),R\_{H^{1}}(g)=\|g^{\*}-g\|\_{H^{1}}^{2}=\int\_{\mathcal{X}}\left(g^{\*}(x)-g(x)\right)^{2}+\left(\frac{\partial g^{\*}(x)}{\partial x}-\frac{\partial g(x)}{\partial x}\right)^{2}\,dP\_{X}(x), |  |

and the empirical risk can be defined as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Rh1S​(g∗,g)\displaystyle R\_{h^{1}}^{S}(g^{\*},g) | =1I​∑i=0I−1(g∗​(xi)−g​(xi))2+1I​∑i=0I−1(∂g∗∂x​(xi)−∂g∂x​(xi))2,\displaystyle=\frac{1}{I}\sum\_{i=0}^{I-1}\left(g^{\*}(x\_{i})-g(x\_{i})\right)^{2}+\frac{1}{I}\sum\_{i=0}^{I-1}\left(\frac{\partial g^{\*}}{\partial x}(x\_{i})-\frac{\partial g}{\partial x}(x\_{i})\right)^{2}, |  | (11) |

where II is the number of samples considered in the corresponding dataset. The use of information about the derivatives of the outputs with respect to the inputs was first introduced in [[35](https://arxiv.org/html/2510.19494v1#bib.bibx35)], giving rise to a new subfield of machine learning known as Differential Machine Learning (DML). In accordance with the aforementioned theorems, several results show that incorporating this information can significantly improve a model’s training performance, as it forces the function estimates to converge point-wise rather than on average.

Another significant aspect that has to be taken into account is that the model to obtain the statistical functions is going to be trained in [−2​π,2​π][-2\pi,2\pi] with data rescaled to [−π,π][-\pi,\pi], rather than trained directly in [−π,π][-\pi,\pi]. This ensures that the resulting Fourier series is smoother and does not exhibit Gibbs phenomena, since outside [−π,π][-\pi,\pi] an approximation freedom is allowed due to the lack of data information outside that region. An example of the impact of this feature can be observed in Figure [2](https://arxiv.org/html/2510.19494v1#S3.F2 "Figure 2 ‣ 3.2 Methodology ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing") but, specially, in Figure [3](https://arxiv.org/html/2510.19494v1#S3.F3 "Figure 3 ‣ 3.2 Methodology ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"), because of the sharp jumps that the the CDF exhibits at its edges due to the periodic extension, causing the oscillations to become more pronounced and the approximation to be worse.

![Refer to caption](x2.png)


(a)

![Refer to caption](x3.png)


(b)

Figure 2: Approximation of the PDF with training in different intervals.



![Refer to caption](x4.png)


(a)

![Refer to caption](x5.png)


(b)

Figure 3: Approximation of the CDF with training in different intervals.

In addition, all experiments related to these first two methods are conducted using the same quantum ansatz, illustrated in Figure [4](https://arxiv.org/html/2510.19494v1#S3.F4 "Figure 4 ‣ 3.2 Methodology ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"), which is composed of a fixed number of qubits and layers. However, this design can be scaled in complexity to analyze how the results vary with respect to the capacity of the circuit. This strategy allows to study both the accuracy and generalization of the model in different scenarios.

![Refer to caption](x6.png)


Figure 4: Scheme of a single layer of the quantum ansatz used to construct the PQC for 2 qubits, extracted from [[20](https://arxiv.org/html/2510.19494v1#bib.bibx20)].

The last proposed method is based on the use of QAMC. As a QAE routine we select a modified version of the RQAE algorithm, termed mRQAE (see [[8](https://arxiv.org/html/2510.19494v1#bib.bibx8)] for details), which allows to estimate not only the magnitude but also the sign of the quantity of interest. This is crucial in this case, since the Fourier coefficients can be either positive or negative. Thus, by employing the mRQAE algorithm, we will be able to obtain the Fourier coefficients of the underlying distribution to a certain precision and eventually calculate the derivative’s price.

Although the structure of this third quantum method differs from the previously proposed ones, its primary purpose in this context is to serve as a benchmark for assessing the performance of the designed circuits. Specifically, it provides a set of reference numerical results that enable a meaningful comparison in terms of both cost and accuracy in the extraction of Fourier coefficients.

In order to establish this comparison, the QAMC method will be evaluated under various error tolerances achievable by Methods I and II. For each tolerance level, we will measure the number of circuits runs for each coefficient (interpreted as quantum samples in the context of QAMC). This number of executions will serve as a proxy for computational cost, thus providing an empirical cost metric against which the efficiency of the designed PQCs can be evaluated.

Next, we explain in more detail the relevant methodological aspects of the three mentioned approaches.

#### 3.2.1 Method I: Supervised Learning for PDF approximation

First, we consider a labeled dataset associated with the probability distribution
𝒯={(xi,yi)∈Z=𝒳×𝒴∼P​(x,y)|∀i∈{0,…,I−1}}\mathcal{T}=\{(x\_{i},y\_{i})\in Z=\mathcal{X}\times\mathcal{Y}\sim P(x,y)~|~\forall i\in\{0,\dots,I-1\}\},
defined over a truncation interval that ensures the Fourier series approximation is sufficiently accurate. This interval is obtained following the same reasoning described in [[33](https://arxiv.org/html/2510.19494v1#bib.bibx33)].

Next, we train the PQC using the empirical risk function defined in ([11](https://arxiv.org/html/2510.19494v1#S3.E11 "In 3.2 Methodology ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")) applied to the PDF, i.e.,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Rh1S​(f∗,f)\displaystyle R\_{h^{1}}^{S}(f^{\*},f) | =1I​∑i=0I−1(f∗​(xi)−f​(xi))2+1I​∑i=0I−1(d​f∗d​x​(xi)−d​fd​x​(xi))2,\displaystyle=\frac{1}{I}\sum\_{i=0}^{I-1}\left(f^{\*}(x\_{i})-f(x\_{i})\right)^{2}+\frac{1}{I}\sum\_{i=0}^{I-1}\left(\frac{df^{\*}}{dx}(x\_{i})-\frac{df}{dx}(x\_{i})\right)^{2}, |  | (12) |

to approximate the underlying PDF in [−2​π,2​π][-2\pi,2\pi] with data rescaled to [−π,π][-\pi,\pi], as mentioned before.

Subsequently, the Fourier series coefficients are extracted using a precise and efficient strategy based on the Discrete Fourier Transform (DFT), applied to direct evaluations of the trained circuit in [−π,π][-\pi,\pi].
For this purpose, we use the scalar function that returns the output of the trained quantum circuit for each input xx, corresponding to the Fourier series in exponential form, i.e.,

|  |  |  |
| --- | --- | --- |
|  | f​(y|x)≈∑k=−𝒦𝒦ck⋅ei​k​x,f(y|x)\approx\sum\_{k=-\mathcal{K}}^{\mathcal{K}}c\_{k}\cdot e^{ikx}, |  |

where 𝒦\mathcal{K} is the specified maximum degree and the coefficients ck∈ℂc\_{k}\in\mathbb{C}. To obtain the desired trigonometric form, the coefficients AkfA\_{k}^{f} and BkfB\_{k}^{f} of the trigonometric series are computed from the complex coefficients ckc\_{k} of the exponential form, using the identities

|  |  |  |
| --- | --- | --- |
|  | Akf=(ck+c−k),Bkf=−i​(ck−c−k).A\_{k}^{f}=(c\_{k}+c\_{-k}),\quad B\_{k}^{f}=-i(c\_{k}-c\_{-k}). |  |

Then, the Fourier series coefficients associated with the payoff function, CkC\_{k} and DkD\_{k}, are typically available in closed-form. Finally, the price is computed using the expression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t0,x)≈12​(b−a)​e−r​Δ​t​(A0f⋅C02+∑k=1𝒦(Akf⋅Ck+Bkf⋅Dk)).V(t\_{0},x)\approx\frac{1}{2}(b-a)e^{-r\Delta t}\left(\frac{A\_{0}^{f}\cdot C\_{0}}{2}+\sum\_{k=1}^{\mathcal{K}}\left(A\_{k}^{f}\cdot C\_{k}+B\_{k}^{f}\cdot D\_{k}\right)\right). |  | (13) |

#### 3.2.2 Method II: Self-supervised Learning for CDF approximation

As mentioned before, in derivative pricing, the exact probability distribution of the underlying asset is rarely available. Therefore, in this case, self-supervised learning will be employed, providing the model with only a representative set of asset samples, so that the labels required to construct the model’s cost function are generated internally from that set.

The formulation of the process is based on the results of Chapter 7 of [[20](https://arxiv.org/html/2510.19494v1#bib.bibx20)], where, from various convergence results, an adaptation of the classical optimization problem is proposed. This starts from a target function F∗∈𝒯⊆HkF^{\*}\in\mathcal{T}\subseteq H^{k} mapping inputs x∈𝒳x\in\mathcal{X} to target labels y∈𝒴y\in\mathcal{Y}, a model F∈ℳ⊆HkF\in\mathcal{M}\subseteq H^{k}, and a risk function RHk:ℳ⟶ℝ+∪{0}R\_{H^{k}}:\mathcal{M}\longrightarrow\mathbb{R}^{+}\cup\{0\}, where the goal is to find the best approximation FF of the target F∗F^{\*} such that

|  |  |  |
| --- | --- | --- |
|  | F=arg⁡minF^∈ℳ⁡RHk​(F^).F=\arg\min\_{\hat{F}\in\mathcal{M}}R\_{H^{k}}(\hat{F}). |  |

The main differences introduced in this method are that the training dataset is given solely by samples and that the function to be estimated will be the CDF. For this purpose, we start by defining the dataset
𝒯={xi∈𝒳|xi∼F∗,i∈{0,…,I−1}}\mathcal{T}=\{x\_{i}\in\mathcal{X}~|~x\_{i}\sim F^{\*},\ i\in\{0,\ldots,I-1\}\},
where neither labels nor their derivatives are available. Therefore, it is necessary to define a new risk function that uses only the inputs x∈𝒳x\in\mathcal{X} and somehow incorporates the derivatives to ensure convergence of the approximation.

To do this, we first consider the case where the empirical risk RR is defined as the squared norm in the discretized space l2​(𝒳)l^{2}(\mathcal{X}):

|  |  |  |
| --- | --- | --- |
|  | Rl2𝒯​(F)=1I​∑i=0I−1(F∗​(xi)−F​(xi))2.R^{\mathcal{T}}\_{l^{2}}(F)=\frac{1}{I}\sum\_{i=0}^{I-1}(F^{\*}(x\_{i})-F(x\_{i}))^{2}. |  |

Since in our case the true labels F∗​(xi)F^{\*}(x\_{i}) are not available, we approximate them by the empirical CDF:

|  |  |  |
| --- | --- | --- |
|  | F∗​(x)≈Femp∗​(x)=1I​∑i=0I−1𝟏xi≤x,F^{\*}(x)\approx F^{\*}\_{\text{emp}}(x)=\frac{1}{I}\sum\_{i=0}^{I-1}\mathbf{1}\_{x\_{i}\leq x}, |  |

so that we use the empirical risk

|  |  |  |
| --- | --- | --- |
|  | R𝒯,l2𝒳​(F)=1I​∑i=0I−1(Femp∗​(xi)−F​(xi))2.R^{\mathcal{X}}\_{\mathcal{T},l^{2}}(F)=\frac{1}{I}\sum\_{i=0}^{I-1}\left(F^{\*}\_{\text{emp}}(x\_{i})-F(x\_{i})\right)^{2}. |  |

Next, we want to apply a similar procedure to the derivative of FF, i.e., the probability density function ff. To this end, we consider the following risk:

|  |  |  |
| --- | --- | --- |
|  | RL2​(f)=∫𝒳(f∗​(x)−f​(x))2​𝑑x=∫𝒳f∗​(x)2​𝑑x−2​∫𝒳f​(x)​f∗​(x)​𝑑x+∫𝒳f​(x)2​𝑑x.R\_{L^{2}}(f)=\int\_{\mathcal{X}}(f^{\*}(x)-f(x))^{2}\,dx=\int\_{\mathcal{X}}f^{\*}(x)^{2}\,dx-2\int\_{\mathcal{X}}f(x)f^{\*}(x)\,dx+\int\_{\mathcal{X}}f(x)^{2}\,dx. |  |

Instead of working with the full expression of RL2​(f)R\_{L^{2}}(f), we consider each term separately. Firstly, the term

|  |  |  |
| --- | --- | --- |
|  | −2​∫𝒳f​(x)​f∗​(x)​𝑑x,-2\int\_{\mathcal{X}}f(x)f^{\*}(x)\,dx, |  |

can be easily approximated by a Monte Carlo method:

|  |  |  |
| --- | --- | --- |
|  | −2​∫𝒳f​(x)​f∗​(x)​𝑑x≈−2n​∑i=0I−1f​(xi).-2\int\_{\mathcal{X}}f(x)f^{\*}(x)\,dx\approx-\frac{2}{n}\sum\_{i=0}^{I-1}f(x\_{i}). |  |

Secondly, the term

|  |  |  |
| --- | --- | --- |
|  | ∫𝒳f​(x)2​𝑑x,\int\_{\mathcal{X}}f(x)^{2}\,dx, |  |

can be approximated by any numerical integration method QQ:

|  |  |  |
| --- | --- | --- |
|  | ∫𝒳f​(x)2​𝑑x≈Q​(f2).\int\_{\mathcal{X}}f(x)^{2}\,dx\approx Q(f^{2}). |  |

Finally, the term

|  |  |  |
| --- | --- | --- |
|  | ∫𝒳f∗​(x)2​𝑑x,\int\_{\mathcal{X}}f^{\*}(x)^{2}\,dx, |  |

is a constant. If, in a minimization problem, we remove a constant from the function to be minimized, the minimum value of the function changes but not the point where this minimum is achieved, which in our case is the function ff. That is, we have

|  |  |  |
| --- | --- | --- |
|  | f=arg⁡minf^∈ℳ⁡RL2​(f^)⟺f=arg⁡minf^∈ℳ⁡[RL2​(f^)−‖f∗‖L22].f=\arg\min\_{\hat{f}\in\mathcal{M}}R\_{L^{2}}(\hat{f})\Longleftrightarrow f=\arg\min\_{\hat{f}\in\mathcal{M}}\left[R\_{L^{2}}(\hat{f})-\|f^{\*}\|^{2}\_{L^{2}}\right]. |  |

Combining these ideas, the empirical risk we construct for the total risk based on the PDF takes the form

|  |  |  |
| --- | --- | --- |
|  | Rl2𝒯​(f)=−2I​∑i=0I−1f​(xi)+Q​(f2).R^{\mathcal{T}}\_{l^{2}}(f)=-\frac{2}{I}\sum\_{i=0}^{I-1}f(x\_{i})+Q(f^{2}). |  |

In order to build a new empirical risk function in a similar way to ([11](https://arxiv.org/html/2510.19494v1#S3.E11 "In 3.2 Methodology ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")), we can consider the combination of the empirical risks of FF and ff:

|  |  |  |
| --- | --- | --- |
|  | Rl2,l2𝒯​(F)=R𝒯,l2𝒳​(F)+Rl2𝒯​(f)=1I​∑i=0I−1(Femp∗​(xi)−F​(xi))2−2I​∑i=0I−1f​(xi)+Q​(f2),R^{\mathcal{T}}\_{l^{2},l^{2}}(F)=R^{\mathcal{X}}\_{\mathcal{T},l^{2}}(F)+R^{\mathcal{T}}\_{l^{2}}(f)=\frac{1}{I}\sum\_{i=0}^{I-1}\left(F^{\*}\_{\text{emp}}(x\_{i})-F(x\_{i})\right)^{2}-\frac{2}{I}\sum\_{i=0}^{I-1}f(x\_{i})+Q(f^{2}), |  |

which is related to the use of DML features for the CDF estimation.

Moreover, in order to guarantee that the CDF approximation is sufficiently accurate at the extremes of the function domain, we add an additional constraint term to the empirical risk function, resulting in

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Rl2,l2𝒯​(F)\displaystyle R^{\mathcal{T}}\_{l^{2},l^{2}}(F) | =\displaystyle= | 1I​∑i=1I−2(Femp∗​(xi)−F​(xi))2\displaystyle\frac{1}{I}\sum\_{i=1}^{I-2}\left(F^{\*}\_{\text{emp}}(x\_{i})-F(x\_{i})\right)^{2} |  |
|  |  |  | −2I​∑i=0I−1f​(xi)+Q​(f2)\displaystyle-\frac{2}{I}\sum\_{i=0}^{I-1}f(x\_{i})+Q(f^{2}) |  |
|  |  |  | +(Femp∗​(x0))2+(Femp∗​(xI−1)−1)2.\displaystyle+\left(F^{\*}\_{\text{emp}}(x\_{0})\right)^{2}+\left(F^{\*}\_{\text{emp}}(x\_{I-1})-1\right)^{2}. |  |

Since the sample sizes will be sufficiently representative, the constraints introduced here do not involve a forced approximation, but rather help to improve the fit at those points that may exhibit instabilities, particularly at the extremes. Thus, given an unlabeled dataset where the truncation interval is determined by the sample elements, the PQC will be trained in [−2​π,2​π][-2\pi,2\pi] but with data rescaled to [−π,π][-\pi,\pi]. Subsequently, the series coefficients will be extracted using the DFT, applied to the direct evaluations of the trained circuit in [−2​π,2​π][-2\pi,2\pi]. This allows us to recover the coefficients ckc\_{k} of the exponential series and turn them into in their trigonometric form.

Finally, as mentioned, the Fourier series coefficients associated with the payoff function are often obtained analytically, allowing to compute the final price using the expression

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V​(t0,x)\displaystyle V(t\_{0},x) | ≈\displaystyle\approx | e−r​Δ​t​(h​(T,b)​F​(b)−h​(T,a)​F​(a))\displaystyle e^{-r\Delta t}\left(h(T,b)F(b)-h(T,a)F(a)\right) |  |
|  |  |  | −e−r​Δ​t​(A0F⋅C0a2+∑k=1𝒦(AkF⋅Cka+BkF⋅Dka))\displaystyle-e^{-r\Delta t}\left(\frac{A\_{0}^{F}\cdot C\_{0}^{a}}{2}+\sum\_{k=1}^{\mathcal{K}}\left(A\_{k}^{F}\cdot C\_{k}^{a}+B\_{k}^{F}\cdot D\_{k}^{a}\right)\right) |  |
|  |  |  | −e−r​Δ​t​(A0F⋅C0b2+∑k=1𝒦(AkF⋅Ckb+BkF⋅Dkb))\displaystyle-e^{-r\Delta t}\left(\frac{A\_{0}^{F}\cdot C\_{0}^{b}}{2}+\sum\_{k=1}^{\mathcal{K}}\left(A\_{k}^{F}\cdot C\_{k}^{b}+B\_{k}^{F}\cdot D\_{k}^{b}\right)\right) |  |

Note that the reason for using a Fourier series of period 2​(b−a)2(b-a), as defined in ([9](https://arxiv.org/html/2510.19494v1#S3.E9 "In 3.1.2 CDF approximation formulation ‣ 3.1 Fourier series approximation of PDF and CDF ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")), in the interval

|  |  |  |
| --- | --- | --- |
|  | [a^,b^]=[3​a−b2,3​b−a2],[\hat{a},\hat{b}]=\left[\frac{3a-b}{2},\frac{3b-a}{2}\right], |  |

is that the the Gibbs phenomenon is completely eliminated, because we are only considering the part of the series corresponding to the CDF when defining the quantities in ([10](https://arxiv.org/html/2510.19494v1#S3.E10 "In 3.1.2 CDF approximation formulation ‣ 3.1 Fourier series approximation of PDF and CDF ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")) between [a,c][a,c] and [c,b][c,b], respectively. This is also why these are not the Fourier coefficients of the series that approximates h​(T,y)h(T,y).

#### 3.2.3 Method III: QAMC with mRQAE for PDF approximation

In this case, we propose an approach similar to the one employed in the first method, in the sense that we will compute the values of the coefficients of the trigonometric Fourier series of the underlying price PDF, although using QAMC.

We start from the same conditions as in Section [3.1](https://arxiv.org/html/2510.19494v1#S3.SS1 "3.1 Fourier series approximation of PDF and CDF ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"), assuming the existence of an interval [a,b]⊂ℝ[a,b]\subset\mathbb{R} and a number 𝒦\mathcal{K} of terms so that the Fourier series represents the PDF with sufficient accuracy, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(y|x)≈A02+∑k=1𝒦(Akf​cos⁡(2​π​k​(y−a)b−a)+Bkf​sin⁡(2​π​k​(y−a)b−a)),f(y|x)\approx\frac{A\_{0}}{2}+\sum\_{k=1}^{\mathcal{K}}\left(A\_{k}^{f}\cos\left(2\pi k\frac{(y-a)}{b-a}\right)+B\_{k}^{f}\sin\left(2\pi k\frac{(y-a)}{b-a}\right)\right), |  | (14) |

In order to compute the coefficients, we proceed as described in [[36](https://arxiv.org/html/2510.19494v1#bib.bibx36)], restricting ourselves to models where an exact simulation of the asset’s evolution can be performed, thereby avoiding errors arising from the use of numerical methods such as Euler-Maruyama. Therefore, when working for example with a Black-Scholes model, we can also assume the existence of a unitary operator that encodes the distribution of paths.

This results in the need for only a single register of n×nn\times n qubits to perform the entire simulation, so that we generate a set of II333Note that it is not necessarily true that I=2nI=2^{n} for nn the number of qubits. labeled data,
𝒯={(Si,f​(Si))∈𝒳×𝒴|∀i∈{0,…,I−1}}\mathcal{T}=\{(S\_{i},f(S\_{i}))\in\mathcal{X}\times\mathcal{Y}~|~~\forall i\in\{0,\dots,I-1\}\},
that allows us to estimate the coefficients as

|  |  |  |
| --- | --- | --- |
|  | Akf=2b−a​∫abf​(y|x)​cos⁡(2​π​k​(y−a)b−a)​𝑑y≈2b−a​∑i=0I−1f​(Si)​cos⁡(2​π​k​(Si−a)b−a),A\_{k}^{f}=\frac{2}{b-a}\int\_{a}^{b}f(y|x)\cos\left(2\pi k\frac{(y-a)}{b-a}\right)\,dy\approx\frac{2}{b-a}\sum\_{i=0}^{I-1}f(S\_{i})\,\cos\left(2\pi k\frac{(S\_{i}-a)}{b-a}\right), |  |

|  |  |  |
| --- | --- | --- |
|  | Bkf=2b−a​∫abf​(y|x)​sin⁡(2​π​k​(y−a)b−a)​𝑑y≈2b−a​∑i=0I−1f​(Si)​sin⁡(2​π​k​(Si−a)b−a).B\_{k}^{f}=\frac{2}{b-a}\int\_{a}^{b}f(y|x)\sin\left(2\pi k\frac{(y-a)}{b-a}\right)\,dy\approx\frac{2}{b-a}\sum\_{i=0}^{I-1}f(S\_{i})\,\sin\left(2\pi k\frac{(S\_{i}-a)}{b-a}\right). |  |

As mentioned, to achieve this we make use of the mRQAE, which is an asymptotically more efficient version of the RQAE. Their main difference is that parameters such as the confidence and the required precision in each iteration are chosen following different criteria. Note again that this QAE routine enables to recover the sign of the coefficients and compute the price accurately.

Again, we assume that the Fourier series coefficients associated with the payoff function, CkC\_{k} and DkD\_{k}, can be evaluated via analytical expressions, enabling to calculate the derivative’s price using ([13](https://arxiv.org/html/2510.19494v1#S3.E13 "In 3.2.1 Method I: Supervised Learning for PDF approximation ‣ 3.2 Methodology ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")).

## 4 Numerical results

In the following section, we present and discuss the results obtained from the different experiments, highlighting the main trends and insights derived from the comparative evaluation of the proposed methods.

### 4.1 Experiment setting

For our numerical experiments, we consider the pricing of a European vanilla put option at t0=0t\_{0}=0, so that the payoff takes the form (see [[1](https://arxiv.org/html/2510.19494v1#bib.bibx1)], for example):

|  |  |  |
| --- | --- | --- |
|  | h​(T,ST)=max⁡{K−ST,0}.h(T,S\_{T})=\max\{K-S\_{T},0\}. |  |

In order to price an option, the stochastic dynamics of the underlying asset price StS\_{t} has to be introduced, usually in terms of a stochastic differential equation (SDE). In the present work, we assume that the underlying asset follows a Black–Scholes-type dynamics, which is described by the following SDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=r​St​d​t+σ​St​d​Bt,dS\_{t}=rS\_{t}\,dt+\sigma S\_{t}\,dB\_{t}, |  | (15) |

where S0S\_{0} is the given price of the underlying at t=0t=0, rr is the risk-free interest rate, σ\sigma is the constant volatility of the assets, and BtB\_{t} represents a standard Brownian motion under the probability measure ℚ\mathbb{Q}.

In the case of more complex dynamics, such as stochastic volatility models, the simulation of the underlying asset prices to obtain STS\_{T} (and therefore h​(T,ST)h(T,S\_{T})) requires the use of numerical methods to solve SDEs. However, in the case of Black-Scholes dynamics, the exact solution of SDE ([15](https://arxiv.org/html/2510.19494v1#S4.E15 "In 4.1 Experiment setting ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")) can be obtained from Ito calculus and is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=S0​exp⁡((r−σ22)​t+Bt).S\_{t}=S\_{0}\exp\left(\left(r-\frac{\sigma^{2}}{2}\right)t+B\_{t}\right). |  | (16) |

It should be remarked that, in Black–Scholes models for asset prices, when valuing derivatives it is common to work with logarithmic normalized by the strike price, due to the transformation of the statistical behavior of the underlying asset. Note that expression ([16](https://arxiv.org/html/2510.19494v1#S4.E16 "In 4.1 Experiment setting ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")) implies that the model assumes the following lognormal distribution for the asset price at time tt:

|  |  |  |
| --- | --- | --- |
|  | St∼Lognormal​(r,σ2​t),S\_{t}\sim\text{Lognormal}(r,\sigma^{2}t), |  |

then it can be easily proven that the logarithmic normalized prices XtX\_{t} follow a normal distribution as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt:=log⁡(St/K)∼𝒩​(log⁡(S0K)+(r−12​σ2)​t,σ2​t).X\_{t}:=\log(S\_{t}/K)\sim\mathcal{N}\left(\log\left(\frac{S\_{0}}{K}\right)+\left(r-\frac{1}{2}\sigma^{2}\right)t,\ \sigma^{2}t\right). |  | (17) |

The goal of this transformation is to work with a symmetric and unbounded distribution, such as the normal distribution, which is particularly useful in contexts where techniques based on Fourier theory, machine learning, or quantum simulation are employed, since many of these tools operate more naturally and efficiently in symmetric domains centered around zero.

Note that when working with the process XtX\_{t}, the consideration of its probability distribution ([17](https://arxiv.org/html/2510.19494v1#S4.E17 "In 4.1 Experiment setting ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")) allows one to obtain the expression of the payoff hh and the PDF ff that appear in the integral expression ([4](https://arxiv.org/html/2510.19494v1#S3.E4 "In 3.1.1 PDF approximation formulation ‣ 3.1 Fourier series approximation of PDF and CDF ‣ 3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")).

The following model parameters have been chosen:

|  |  |  |
| --- | --- | --- |
|  | S0=100,r=0.1,T=1,σ=0.25.S\_{0}=100,\quad r=0.1,\quad T=1,\quad\sigma=0.25. |  |

These values allow the simulation of a realistic yet controlled market scenario, suitable for evaluating the generalization ability and accuracy of the proposed methods. Additionally, three different strike prices have been selected:

|  |  |  |
| --- | --- | --- |
|  | K=90,K=100​and​K=110,K=90,~~K=100~~\text{and}~~K=110, |  |

with the aim of analyzing the model’s behavior for different option contract configurations where the spot price S0S\_{0} is above, equal to, or below the strike price KK, respectively.

Regarding the PQC training setup, the hyperparameters used in the different experiments are summarized in Table [1](https://arxiv.org/html/2510.19494v1#S4.T1 "Table 1 ‣ 4.1 Experiment setting ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing").

Table 1: Training hyperparameters used in methods I and II.

| Hyperparameter | I | II |
| --- | --- | --- |
| Optimizer | Adam | Adam |
| Learning rate | 0.0050.005 | 0.10.1 |
| Epochs | 300300 | 300300 |
| Supervised weight | 0.90.9 | 0.20.2 |
| Differential weight | 0.10.1 | 0.80.8 |
| Training points | 250−2.5⋅103250-2.5\cdot 10^{3} | 103−10410^{3}-10^{4} |
| Test points | 100100 | 10310^{3} |
| Repetitions | 1010 | 1010 |

Additionally, experiments have been conducted with different regular (n×n)(n\times n) configurations (referring to the nn qubits and nn layers employed in the PQC), to assess whether another number of parameters improves the results. However, as it is common in QML problems, there is neither universal optimal configuration, nor a clear relationship between scalability and accuracy. In many cases, it is necessary to find an appropriate balance (a trade-off) between model the complexity and the specific characteristics of the problem under consideration. For the (QAMC-based) Method III, the number of coefficients used will be the same as in Method I, by construction, and we vary the number of executions of the circuit, often called *shots* in the quantum jargon, by prescribing an increasing tolerance for the mRQAE routine.

In general, the structures used to design the PQCs in the experiments are chosen such that they return accurate approximations of the distributions and the payoff and capture the complexity of the problem. For Method I, the minimum scheme is 6×66\times 6, while for Method II it is 4×44\times 4.

Finally, Table [2](https://arxiv.org/html/2510.19494v1#S4.T2 "Table 2 ‣ 4.1 Experiment setting ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing") shows the technical characteristics of the computational system for the experiments.

Table 2: Technical characteristics of the computational environment used.

| Parameter | Value |
| --- | --- |
| Processor | Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz |
| RAM Memory | 8.0 GB |
| Operating System | Windows 10 (64 bits) |
| Python Version | 3.12.7 |
| JAX Version | 0.4.35 |
| PennyLane Version | 0.40.0 |

### 4.2 Results and discussion

In this section, we firstly present the convergence results obtained by the three methods described in Section [3](https://arxiv.org/html/2510.19494v1#S3 "3 Formulation and methodology ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"). Several experiments have been carried out for each method with an increasing approximation power of the PQC and the results are shown in Figure [5](https://arxiv.org/html/2510.19494v1#S4.F5 "Figure 5 ‣ 4.2 Results and discussion ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing") (Method I and Method II) and Figure [8](https://arxiv.org/html/2510.19494v1#S4.F8 "Figure 8 ‣ 4.2.1 Impact of the data size ‣ 4.2 Results and discussion ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing") (Method III), respectively. Each of the pictures in these graphs show the accuracy convergence in terms of the size of each case’s employed dataset for the three considered strike prices. Next, in Sections [4.2.1](https://arxiv.org/html/2510.19494v1#S4.SS2.SSS1 "4.2.1 Impact of the data size ‣ 4.2 Results and discussion ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing") and [4.2.2](https://arxiv.org/html/2510.19494v1#S4.SS2.SSS2 "4.2.2 Impact of the number of coefficients ‣ 4.2 Results and discussion ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"), we discuss the presented results more in depth, analyzing the impact on the PQC estimations in terms of the dataset size and the PQC structures (number of coefficients in the approximation).

![Refer to caption](x7.png)


(a)

![Refer to caption](x8.png)


(b)

![Refer to caption](x9.png)


(c)

![Refer to caption](x10.png)


(d)

![Refer to caption](x11.png)


(e)

![Refer to caption](x12.png)


(f)

Figure 5: Convergence results for Method I (left column) and Method II (right column).

#### 4.2.1 Impact of the data size

One of the main objectives of increasing the sample size is to obtain a more complete and representative dataset, in order to capture the underlying distribution in a more faithful way. As the number of observations increases, the estimations obtained through approximation models should reflect more accurately the statistical patterns of the original data, thus resulting in a better generalization and a reduction of the error.

From Figure [5](https://arxiv.org/html/2510.19494v1#S4.F5 "Figure 5 ‣ 4.2 Results and discussion ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"), a clear convergence towards the exact value in both Method I and Method II can be observed as the sample size increases. However, some outliers appear, which can be attributed to the inherent error of the training process, particularly to the randomness in the initialization of the quantum model weights, which introduces fluctuations that are not always corrected during optimization. These aspects highlight the importance of carrying out a larger number of experimental repetitions, accompanied by a statistical analysis that isolates these sources of uncertainty.

Despite these limitations, the results obtained so far are clearly satisfactory and demonstrate the potential of the approach, as illustrated in Figures [6](https://arxiv.org/html/2510.19494v1#S4.F6 "Figure 6 ‣ 4.2.1 Impact of the data size ‣ 4.2 Results and discussion ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing") and [7](https://arxiv.org/html/2510.19494v1#S4.F7 "Figure 7 ‣ 4.2.1 Impact of the data size ‣ 4.2 Results and discussion ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing") for Method I and Method II, respectively.

![Refer to caption](x13.png)


(a)

![Refer to caption](x14.png)


(b)

![Refer to caption](x15.png)


(c)

Figure 6: Output of the PQC for Method I (a) and for Method II (b).



![Refer to caption](x16.png)


(a)

![Refer to caption](x17.png)


(b)

![Refer to caption](x18.png)


(c)

Figure 7: Output of the PQC for Method II.

The Method III (Figure [8](https://arxiv.org/html/2510.19494v1#S4.F8 "Figure 8 ‣ 4.2.1 Impact of the data size ‣ 4.2 Results and discussion ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing")) achieves remarkably accurate estimations, with reduced variability (specially when more shots are employed). Those effects are somehow expected since, while the precision and variability of the estimations provided by the PQCs (Methods I and II) are mainly affected by the quality of the optimization process (subject to the intrinsic variability of initial parameters, random jumps, etc.) and the data, the precision by QAMC is controlled by the QAE routine (mRQAE), prescribing that the discrete data points are enough to accurately represent the continuous density function.

![Refer to caption](x19.png)


(a)

![Refer to caption](x20.png)


(b)

![Refer to caption](x21.png)


(c)

Figure 8: Convergence results for Method III.

Note however that, in order to get highly accurate predictions, we need around 50005000 shots per coefficient in average, thus implying an order of hundreds of thousand shots to obtain the final price. In comparison, with Method II we obtain similar results with 1000010000 data samples (and, of course, after a training procedure), which highlights the potential of QML-based approaches in the derivatives valuation area, as a complementary methodology to the more popular QAMC. From a practical point of view, the performance of Method II is even more relevant, since it does not require the availability of the underlying PDF, but only the generation of random samples following the proper distribution.

#### 4.2.2 Impact of the number of coefficients

Since the functions to be approximated in each method are different, it is necessary to use distinct dimensions in the PQC schemes to ensure good results. This is because, in certain cases, adding an excessive number of terms in the approximation of a function can introduce additional contributions to oscillations and instabilities in the model. In the specific case of the CDF, which exhibits sharp jumps at its boundaries due to periodic extension, these oscillations may become more pronounced.

Moreover, the exponential nature of the payoff and the periodicity of the approximation give rise to abrupt jumps at the points of discontinuity. As a result, the outcomes may present larger errors and significant variability as the number of terms in the Fourier expansion increases.

Nevertheless, when using dimensions on the order of 6×66\times 6, 7×77\times 7, and 8×88\times 8 for Method I, and 4×44\times 4, 5×55\times 5, and 6×66\times 6 for Method II, both methods display stable behavior, showing a clear trend of convergence towards the true derivative value as the expressive capacity of the circuit increases. This can be clearly seen in Figure [5](https://arxiv.org/html/2510.19494v1#S4.F5 "Figure 5 ‣ 4.2 Results and discussion ‣ 4 Numerical results ‣ Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing"), reinforcing the idea that introducing flexibility in the Fourier series approximation is essential to achieve accurate and reliable estimates.

It is worth noting that, according to the results, the best performance is obtained with an intermediate scheme (7×77\times 7 for Method I and 5×55\times 5 for Method II), illustrating how in this type of problem there is often a trade-off between model complexity and the specific characteristics of the problem under study.
On the other hand, in the case of Method III, increasing the number of coefficients leads to a substantial improvement in the results, particularly when the number of shots is low. Beyond a certain threshold, the coefficients tend to take significantly small values and, combined with the accuracy provided by QAMC, it clearly shows how these small contributions help to refine the computed price, thus illustrating a clear convergence of the estimated prices.

## 5 Conclusions

In this work, we have presented two hybrid classical–quantum approaches for the option pricing problem. This framework connects quantum learning models with Fourier-based valuation techniques, enabling the extraction of relevant statistical information from quantum-generated data. The performance of the proposed models was benchmarked against QAMC, allowing for a quantitative comparison in terms of computational cost and accuracy in the recovery of Fourier coefficients. The number of circuit executions per coefficient, interpreted as quantum samples, served as an empirical cost metric to evaluate PQC efficiency.

Both methods exhibited stable convergence towards the true derivative value as the expressive capacity of the PQCs increased. Circuit dimensions on the order of 6×66\times 6 to 8×88\times 8 for Method I and 4×44\times 4 to 6×66\times 6 for Method II yielded consistent and reliable estimates, confirming the importance of model flexibility in Fourier-based approximations.

In addition, as the sample size is increased, a systematic convergence towards the exact solution has been observed across methods, though minor outliers appeared due to stochastic effects in the training phase, particularly from random initialization of quantum weights. These effects suggest the need for multiple experimental runs and statistical post-analysis to isolate uncertainty sources.

Finally, Method II obtains comparable precision using only ∼10000\sim 10000 data samples as the benchmarking Method III, which requires on the order of hundreds of thousands of shots to achieve high accuracy with low variability. This fact underscores the potential of QML-based strategies as efficient and complementary alternatives to traditional QAMC schemes. Moreover, Method II stands out for not requiring explicit knowledge of the underlying probability density function, instead relying on sampling from the appropriate distribution, as it is common practice in industry.

## Acknowledgements

All authors acknowledge the support of CITIC, as a center accredited for excellence within the Galician University System and a
member of the CIGUS Network, receiving subsidies from the Department of Education, Science, Universities, and Vocational Training of the Xunta de Galicia. Additionally, it is co-financed by the EU through the FEDER Galicia 2021-27 operational program (ref. ED451G 2023/01). Á. Leitao and C. Vázquez acknowledge the funding from the Ministry of Science and Innovation of Spain (ref. PID2022-141058OB-I00) and from the Department of Education, Science, Universities, and Vocational Training of the Xunta de Galicia (ref. ED451C 2022/047), both including FEDER financial support. Á. Leitao acknowledges the financial support from the Spanish Ministry of Science and Innovation through the Ramón y Cajal 2022 grant, and the Department of Education, Science, Universities, and Vocational Training of the Xunta de Galicia through the Excellence research program (ref. ED431F 2025/032).

## References

* [1]
  John C. Hull
  “Options, Futures and Other Derivatives”
  Pearson Prentice Hall, 2006
* [2]
  Andrés Gómez, Alvaro Leitao, Alberto P. Manzano, Maria R. Nogueiras, Gustavo Ordóñez and Carlos Vázquez
  “A Survey on Quantum Computational Finance for Derivatives Pricing and VaR”
  In *Archives of Computational Methods in Engineering* 9, 2022, pp. 4137–4163
* [3]
  Adam Bouland, Wim Dam, Hamed Joorati, Iordanis Kerenidis and Anupam Prakash
  “Prospects and Challenges of Quantum Finance”, 2020
  arXiv:[2011.06492](https://arxiv.org/abs/2011.06492)
* [4]
  Román Orús, Samuel Mugel and Enrique Lizaso
  “Quantum Computing for Finance: Overview and Prospects” 100028
  In *Reviews in Physics* 4
  Elsevier BV, 2019
* [5]
  Nikitas Stamatopoulos, Daniel J. Egger, Yue Sun, Christa Zoufal, Raban Iten, Ning Shen and Stefan Woerner
  “Option Pricing Using Quantum Computers” 291
  In *Quantum* 4
  Verein zur Forderung des Open Access Publizierens in den Quantenwissenschaften, 2020
* [6]
  Robert Scriba, Yuying Li and Jingbo B Wang
  “Monte Carlo Option Pricing in Quantum Parallel”, 2025
  arXiv:[2505.09459](https://arxiv.org/abs/2505.09459)
* [7]
  Zoltán Udvarnoki, Gábor Fáth and Norbert Fogarasi
  “Quantum Advantage of Monte Carlo Option Pricing” 055001
  In *Journal of Physics Communications* 7.5
  IOP Publishing, 2023
* [8]
  Alberto P. Manzano, Gonzalo Ferro, Álvaro Leitao, Carlos Vázquez and Andrés Gómez
  “Alternative Pipeline for Option Pricing Using Quantum Computers” 28
  In *EPJ Quantum Technology* 12, 2025
* [9]
  Alberto P. Manzano, Daniele Musso and Álvaro Leitao
  “Real Quantum Amplitude Estimation”
  In *EPJ Quantum Technology* 10.1
  SpringerOpen, 2023, pp. 1–24
* [10]
  Steven Herbert
  “Quantum Monte Carlo Integration: The Full Advantage in Minimal Circuit Depth” 823
  In *Quantum* 6
  Verein zur Forderung des Open Access Publizierens in den Quantenwissenschaften, 2022
* [11]
  Jorge J. Lejarza, Michele Grossi, Leandro Cieri and Germán Rodrigo
  “Quantum Fourier Iterative Amplitude Estimation”
  In *2023 IEEE International Conference on Quantum Computing and Engineering (QCE)*
  IEEE, 2023, pp. 571–579
* [12]
  Javier González-Conde, Angel Rodríguez-Rozas, Enrique Solano and Mikel Sanz
  “Pricing Financial Derivatives with Exponential Quantum Speedup”, 2021
  arXiv:[2101.04023](https://arxiv.org/abs/2101.04023)
* [13]
  Filipe Fontanela, Antoine Jacquier and Mugad Oumgari
  “Short Communication: A Quantum Algorithm for Linear PDEs Arising in Finance”
  In *SIAM Journal on Financial Mathematics* 12.4, 2021, pp. SC98–SC114
* [14]
  Swagat Kumar and Colin Michael Wilmott
  “Simulating the non-Hermitian dynamics of financial option pricing with quantum computers”
  In *Scientific Reports* 15.1
  Springer ScienceBusiness Media LLC, 2025
* [15]
  Lucas Leclerc, Luis Ortiz-Guitierrez, Sebastian Grijalva, Boris Albrecht, Julia R.. Cline, Vincent E. Elfving, Adrien Signoles, Loïc Henriet, Gianni Del Bimbo, Usman Ayub Sheikh, Maitree Shah, Luc Andrea, Faysal Ishtiaq, Andoni Duarte, Samuel Mugel, Irene Caceres, Michel Kurek, Roman Orus, Achraf Seddik, Oumaima Hammammi, Hacene Isselnane and Didier M’tamon
  “Financial Risk Management on a Neutral Atom Quantum Processor”, 2024
  arXiv:[2212.03223 [quant-ph]](https://arxiv.org/abs/2212.03223)
* [16]
  Sohum Thakkar, Skander Kazdaghli, Natansh Mathur, Iordanis Kerenidis, André J. Ferreira-Martins and Samurai Brito
  “Improved Financial Forecasting via Quantum Machine Learning”, 2024
  arXiv:[2306.12965 [q-fin.ST]](https://arxiv.org/abs/2306.12965)
* [17]
  Sascha Wilkens and Joe Moorhouse
  “Quantum computing for financial risk measurement”
  In *Quantum Information Processing* 22, 2023
  DOI: [10.1007/s11128-022-03777-2](https://dx.doi.org/10.1007/s11128-022-03777-2)
* [18]
  Maria Schuld, Ryan Sweke and Johannes Jakob Meyer
  “Effect of Data Encoding on the Expressive Power of Variational Quantum-Machine-learning Models”
  In *Physical Review A* 103.3
  American Physical Society (APS), 2021
* [19]
  Adrián Pérez-Salinas, David López-Núñez, Artur García-Sáez, P. Forn-Díaz and José I. Latorre
  “One Qubit as a Universal Approximant” 01245
  In *Physical Review A* 104
  American Physical Society (APS), 2021
* [20]
  Alberto P. Manzano
  “Contributions to the Pricing of Financial Derivatives Contracts in Commodity Markets and the Use of Quantum Computing in Finance”, 2024
* [21]
  Yu Liu, Kentaro Baba, Kazuya Kaneko, Naoyuki Takeda, Junpei Koyama and Koichi Kimura
  “Analysis of Parameterized Quantum Circuits: on The Connection Between Expressibility and Types of Quantum Gates”, 2024
  arXiv:[2408.01036](https://arxiv.org/abs/2408.01036)
* [22]
  Marcello Benedetti, Erika Lloyd, Stefan Sack and Mattia Fiorentini
  “Parameterized Quantum Circuits as Machine Learning Models” 043001
  In *Quantum Science and Technology* 4.4
  IOP Publishing, 2019
* [23]
  Mateusz Ostaszewski, Edward Grant and Marcello Benedetti
  “Structure Optimization for Parameterized Quantum Circuits” 391
  In *Quantum* 5
  Verein zur Förderung des Open Access Publizierens in den Quantenwissenschaften, 2021
* [24]
  Alberto P. Manzano, David Dechant, Jordi Tura and Vedran Dunjko
  “Approximation and Generalization Capacities of Parametrized Quantum Circuits for Functions in Sobolev Spaces” 1658
  In *Quantum* 9
  Verein zur Forderung des Open Access Publizierens in den Quantenwissenschaften, 2025
* [25]
  Paul Glassermann
  “Monte Carlo Methods in Financial Engineering”
  Springer, 2004
* [26]
  Ashley Montanaro
  “Quantum Speedup of Monte Carlo Methods” 2181
  In *Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences* 471
  The Royal Society, 2015
* [27]
  Gilles Brassard, Peter Høyer, Michele Mosca and Alain Tapp
  “Quantum Amplitud Amplification and Estimation”
  In *Quantum Computation and Information* 305, Contemporary Mathematics
  American Mathematical Society, 2002, pp. 53–74
* [28]
  Philip Intallura, Georgios Korpas, Sudeepto Chakraborty, Vyacheslav Kungurtsev and Jakub Marecek
  “A Survey of Quantum Alternatives to Randomized Algorithms: Monte Carlo Integration and Beyond”, 2023
  arXiv:[2303.04945](https://arxiv.org/abs/2303.04945)
* [29]
  Dmitry Grinko, Julien Gacon, Christa Zoufal and Stefan Woerner
  “Iterative Quantum Amplitude Estimation” 52
  In *npj Quantum Information* 7
  Springer ScienceBusiness Media LLC, 2021
* [30]
  Almudena Carrera Vázquez and Stefan Woerner
  “Efficient State Preparation for Quantum Amplitude Estimation” 034027
  In *Phys. Rev. Appl.* 15
  American Physical Society, 2021
* [31]
  Adam Holmes and A.. Matsuura
  “Efficient Quantum Circuits for Accurate State Preparation of Smooth, Differentiable Functions”, 2020
  arXiv:[2005.04351](https://arxiv.org/abs/2005.04351)
* [32]
  Lov Grover and Terry Rudolph
  “Creating Superpositions that Correspond to Efficiently Integrable Probability Distributions”, 2002
  arXiv:[quant-ph/0208112](https://arxiv.org/abs/quant-ph/0208112)
* [33]
  Fang Fang and Cornelis W. Oosterlee
  “A Novel Pricing Method for European Options Based on Fourier-Cosine Series Expansions”
  In *SIAM Journal on Scientific Computing* 31.2, 2009, pp. 826–848
* [34]
  Leif B.G. Andersen and Mark Lake
  “High-Performance Applications of the Non-Uniform Fast Fourier Transform to Option Pricing” SSRN, 2022
  URL: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4335916>
* [35]
  Brian Huge and Antoine Savine
  “Differential Machine Learning”, 2020
* [36]
  Dong An, Noah Linden, Jin-Peng Liu, Ashley Montanaro, Changpeng Shao and Jiasu Wang
  “Quantum-accelerated Multilevel Monte Carlo Methods for Stochastic Differential Equations in Mathematical Finance” 481
  In *Quantum* 5
  Verein zur Forderung des Open Access Publizierens in den Quantenwissenschaften, 2021