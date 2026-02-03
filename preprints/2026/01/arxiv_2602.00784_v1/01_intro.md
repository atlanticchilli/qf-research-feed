---
authors:
- Tomasz Kania
doc_id: arxiv:2602.00784v1
family_id: arxiv:2602.00784
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Non-standard analysis for coherent risk estimation: hyperfinite representations,
  discrete Kusuoka formulae, and plug-in asymptotics'
url_abs: http://arxiv.org/abs/2602.00784v1
url_html: https://arxiv.org/html/2602.00784v1
venue: arXiv q-fin
version: 1
year: 2026
---


Tomasz Kania
Mathematical Institute
  
Czech Academy of Sciences
  
Žitná 25
  
115 67 Praha 1
  
Czech Republic and Institute of Mathematics and Computer Science
  
Jagiellonian University
  
Łojasiewicza 6, 30-348 Kraków, Poland
[kania@math.cas.cz, tomasz.marcin.kania@gmail.com](mailto:kania@math.cas.cz,%20tomasz.marcin.kania@gmail.com)

###### Abstract.

We develop a non-standard analysis framework for coherent risk measures and their finite-sample
analogues, coherent risk estimators, building on recent work of Aichele, Cialenco, Jelito, and Pitera.
Coherent risk measures on L∞L^{\infty} are realised as standard parts of internal support functionals on
Loeb probability spaces, and coherent risk estimators arise as finite-grid restrictions.

Our main results are: (i) a hyperfinite robust representation theorem that yields, as finite shadows,
the robust representation results for coherent risk estimators; (ii) a discrete Kusuoka representation
for law-invariant coherent risk estimators as suprema of mixtures of discrete expected shortfalls on
{k/n:k=1,…,n}\{k/n:k=1,\ldots,n\}; (iii) uniform almost sure consistency (with an explicit rate) for canonical
spectral plug-in estimators over Lipschitz spectral classes; (iv) a Kusuoka-type plug-in consistency
theorem under tightness and uniform estimation assumptions; (v) bootstrap validity for spectral
plug-in estimators via an NSA reformulation of the functional delta method (under standard smoothness
assumptions on FXF\_{X}); and (vi) asymptotic normality obtained through a hyperfinite central limit theorem.

The hyperfinite viewpoint provides a transparent probability-to-statistics dictionary: applying a risk
measure to a law corresponds to evaluating an internal functional on a hyperfinite empirical measure and
taking the standard part. We include a standard self-contained introduction to the required non-standard tools.

###### Key words and phrases:

coherent risk measure, coherent risk estimator, spectral risk, Kusuoka representation,
non-standard analysis, Loeb measure, order statistics, L-statistics, hyperfinite probability

###### 2020 Mathematics Subject Classification:

60B10, 60F15, 62G30, 91G70, 03H05

IM CAS (RVO 67985840).

## 1. Introduction

### 1.1. Background and motivation

The measurement of financial risk occupies a central position in modern quantitative
finance, insurance, and regulatory frameworks. Since the seminal work of Artzner, Delbaen,
Eber, and Heath [[2](https://arxiv.org/html/2602.00784v1#bib.bib2)], the axiomatic approach to risk measures has provided both
theoretical foundations and practical guidance for risk management. A *coherent risk
measure* (CRM) is a functional ρ\rho acting on random variables (representing profit and
loss distributions) that satisfies four economically motivated axioms: monotonicity, cash
additivity, positive homogeneity, and subadditivity. (Throughout, we adopt the P&L sign
convention: XX represents profit, so losses are negative and ρ​(X)\rho(X) evaluates required
capital; hence the (−X)(-X) in dual representations.)

The fundamental structural result for CRMs is the *robust representation theorem*,
which asserts that under mild regularity conditions, any coherent risk measure can be
written as a supremum of expectations under a family of probability measures:

|  |  |  |
| --- | --- | --- |
|  | ρ​(X)=supQ∈𝒬𝖤Q​[−X].\rho(X)=\sup\_{Q\in\mathcal{Q}}\mathsf{E}\_{Q}[-X]. |  |

This representation reveals the dual nature of coherent risk: the set 𝒬\mathcal{Q}
encodes model uncertainty or stress scenarios, whilst the supremum captures a worst-case
perspective essential to prudent risk management.

Whilst the theory of CRMs is well-developed at the population level—where one has access
to the full distribution of XX—practical applications invariably require estimation from
finite samples. This raises the statistical question: what is the appropriate analogue of
coherent risk when one observes only a sample (x1,…,xn)∈ℝn(x\_{1},\ldots,x\_{n})\in\mathbb{R}^{n}?

This question was recently addressed by Aichele, Cialenco, Jelito, and Pitera [[1](https://arxiv.org/html/2602.00784v1#bib.bib1)],
who introduced the concept of a *coherent risk estimator* (CRE): a functional
ρ^n:ℝn→ℝ\hat{\rho}\_{n}:\mathbb{R}^{n}\to\mathbb{R} satisfying the same four coherence axioms, now interpreted
coordinatewise on the sample space. Their work establishes that CREs admit finite-dimensional
robust representations as suprema of linear functionals, with law-invariant and comonotonic
variants corresponding to L-estimators based on order statistics.

### 1.2. The non-standard analysis perspective

The purpose of this paper is to develop a unified framework for CRMs and CREs using
*non-standard analysis* (NSA). This approach, originating in the work of Abraham
Robinson [[16](https://arxiv.org/html/2602.00784v1#bib.bib16)], extends the real numbers to the *hyperreals* ℝ∗{}^{\*}\mathbb{R},
which include infinitesimal and infinite elements. Whilst initially developed for logical
and foundational purposes, NSA has proven to be a powerful tool in probability theory,
particularly through the *Loeb measure construction* [[15](https://arxiv.org/html/2602.00784v1#bib.bib15)], which produces
genuine σ\sigma-additive probability spaces from internal hyperfinite structures.

From the NSA perspective, the objects of interest have particularly transparent
interpretations:

* •

  Hyperfinite probability spaces. An internal hyperfinite set
  IN={1,2,…,N}I\_{N}=\{1,2,\ldots,N\} with N∈ℕ∗N\in{}^{\*}\mathbb{N} infinite, equipped with the counting
  probability measure μN​(A)=|A|/N\mu\_{N}(A)=|A|/N, becomes a genuine probability space via the Loeb
  construction. This provides a “bridge” between discrete and continuous probability.
* •

  Coherent risk measures as standard parts. A CRM ρ\rho on L∞L^{\infty} can be
  expressed as the standard part of a hyperfinite support functional: dual measures QQ
  correspond to hyperfinite weight vectors a=(a1,…,aN)a=(a\_{1},\ldots,a\_{N}) with ∑k=1Nak=1\sum\_{k=1}^{N}a\_{k}=1,
  and expectations under QQ become hyperfinite sums.
* •

  CREs as finite shadows. By taking N=nN=n finite, the hyperfinite
  representation specialises to the finite-dimensional robust representation of CREs. The
  passage from CRMs to CREs is simply the restriction of the hyperfinite picture to a finite
  grid.
* •

  Plug-in estimators as hyperfinite L-statistics. On an infinite hyperfinite
  i.i.d. sample (X1,…,XN)(X\_{1},\ldots,X\_{N}), spectral risk measures become standard parts of
  hyperfinite L-statistics. Consistency results emerge from the hyperfinite law of large
  numbers and quantile convergence.

This unified viewpoint offers several advantages. First, it provides a single conceptual
framework encompassing both the population-level theory of CRMs and the finite-sample
theory of CREs. Second, it simplifies certain asymptotic arguments by allowing one to work
internally with the entire probability space at once, taking standard parts only at the
end. Third, it suggests natural generalisations and new results, including uniform
consistency over families of risk measures and bootstrap validity.

### 1.3. Main contributions

The principal contributions of this paper are as follows.

1. (1)

   Hyperfinite robust representation (Section [4](https://arxiv.org/html/2602.00784v1#S4 "4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")). We establish
   that coherent risk measures on L∞L^{\infty} are standard parts of hyperfinite support functionals,
   providing a unified proof of the finite-sample robust representation theorems for CREs
   (Theorems [2.9](https://arxiv.org/html/2602.00784v1#S2.Thmtheorem9 "Theorem 2.9 (Robust representation of CREs [1, Theorem 4.1]). ‣ 2.3. Coherent risk estimators ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), [2.10](https://arxiv.org/html/2602.00784v1#S2.Thmtheorem10 "Theorem 2.10 (Law-invariant CREs [1, Theorem 4.2]). ‣ 2.3. Coherent risk estimators ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), and [2.11](https://arxiv.org/html/2602.00784v1#S2.Thmtheorem11 "Theorem 2.11 (Comonotonic law-invariant CREs [1, Theorem 4.10]). ‣ 2.3. Coherent risk estimators ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")).
2. (2)

   Discrete Kusuoka representation (Section [5](https://arxiv.org/html/2602.00784v1#S5 "5. Discrete Kusuoka representation for law-invariant CREs ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")). We prove
   that every law-invariant CRE admits a representation as a supremum over mixtures of
   discrete expected shortfalls at grid points (Theorem [5.5](https://arxiv.org/html/2602.00784v1#S5.Thmtheorem5 "Theorem 5.5 (Discrete Kusuoka representation). ‣ 5.3. The discrete Kusuoka representation theorem ‣ 5. Discrete Kusuoka representation for law-invariant CREs ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")). This is the
   finite-sample analogue of Kusuoka’s celebrated representation theorem for law-invariant
   CRMs on atomless spaces.
3. (3)

   Uniform spectral consistency (Section [7](https://arxiv.org/html/2602.00784v1#S7 "7. Spectral plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")). We establish
   uniform almost sure consistency for spectral plug-in CREs over Lipschitz families of
   spectra, with an explicit rate of convergence (Theorem [7.6](https://arxiv.org/html/2602.00784v1#S7.Thmtheorem6 "Theorem 7.6 (Uniform spectral plug-in consistency). ‣ 7.3. Uniform consistency over Lipschitz spectral classes ‣ 7. Spectral plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") and
   Corollary [7.8](https://arxiv.org/html/2602.00784v1#S7.Thmtheorem8 "Corollary 7.8. ‣ 7.3. Uniform consistency over Lipschitz spectral classes ‣ 7. Spectral plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")).
4. (4)

   Kusuoka plug-in consistency (Section [8](https://arxiv.org/html/2602.00784v1#S8 "8. Kusuoka-type plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")). We prove a
   general consistency theorem for Kusuoka-type plug-in estimators under tightness and
   uniform estimation conditions (Theorem [8.1](https://arxiv.org/html/2602.00784v1#S8.Thmtheorem1 "Theorem 8.1 (Kusuoka plug-in consistency). ‣ 8.2. Consistency theorem ‣ 8. Kusuoka-type plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")).
5. (5)

   Hyperfinite bootstrap validity (Section [9](https://arxiv.org/html/2602.00784v1#S9 "9. Hyperfinite bootstrap validity ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")). We show that
   the internal resampling scheme yields the correct Gaussian limit, via an NSA reformulation
   of the bootstrap delta method (Theorem [9.4](https://arxiv.org/html/2602.00784v1#S9.Thmtheorem4 "Theorem 9.4 (Hyperfinite Bootstrap Consistency). ‣ 9.2. Near-standardness of conditional laws ‣ 9. Hyperfinite bootstrap validity ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")).
6. (6)

   Asymptotic normality (Section [10](https://arxiv.org/html/2602.00784v1#S10 "10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")). We derive the asymptotic
   distribution of spectral plug-in estimators via the hyperfinite central limit theorem
   (Theorem [10.5](https://arxiv.org/html/2602.00784v1#S10.Thmtheorem5 "Theorem 10.5 (Asymptotic normality of spectral plug-in CREs). ‣ 10.2. Asymptotic normality of spectral estimators ‣ 10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")).

### 1.4. Organisation of the paper

Section [2](https://arxiv.org/html/2602.00784v1#S2 "2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") recalls the definitions of coherent risk measures and estimators,
following [[1](https://arxiv.org/html/2602.00784v1#bib.bib1)] and [[11](https://arxiv.org/html/2602.00784v1#bib.bib11)]. Section [3](https://arxiv.org/html/2602.00784v1#S3 "3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") provides a self-contained
introduction to non-standard analysis, covering hyperreals, hyperfinite sets, and Loeb
measures at the level required for our applications. Section [4](https://arxiv.org/html/2602.00784v1#S4 "4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") develops
the hyperfinite representation of CRMs and uses it to derive the finite-sample
representation theorems for CREs. Section [5](https://arxiv.org/html/2602.00784v1#S5 "5. Discrete Kusuoka representation for law-invariant CREs ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") establishes the discrete
Kusuoka representation. Section [6](https://arxiv.org/html/2602.00784v1#S6 "6. Spectral risk measures and hyperfinite L-statistics ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") treats spectral risk measures and their
hyperfinite L-statistic representations. Section [7](https://arxiv.org/html/2602.00784v1#S7 "7. Spectral plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") proves the uniform
spectral consistency theorem. Section [8](https://arxiv.org/html/2602.00784v1#S8 "8. Kusuoka-type plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") extends to general
Kusuoka-type plug-in estimators. Section [9](https://arxiv.org/html/2602.00784v1#S9 "9. Hyperfinite bootstrap validity ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") establishes bootstrap
validity. Section [10](https://arxiv.org/html/2602.00784v1#S10 "10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") derives asymptotic normality. Section [11](https://arxiv.org/html/2602.00784v1#S11 "11. Extensions to Orlicz hearts ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")
briefly discusses the extension to Orlicz hearts.

The role of NSA varies across sections: in Sections [4](https://arxiv.org/html/2602.00784v1#S4 "4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")–[5](https://arxiv.org/html/2602.00784v1#S5 "5. Discrete Kusuoka representation for law-invariant CREs ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"),
NSA provides a unifying language for dual representations, showing that CREs are finite shadows
of CRMs; in Sections [7](https://arxiv.org/html/2602.00784v1#S7 "7. Spectral plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")–[10](https://arxiv.org/html/2602.00784v1#S10 "10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), NSA serves as a probability-to-statistics
transfer device, converting population-level results (Glivenko–Cantelli, CLT, bootstrap validity)
to sample-level statements via the standard-part map.

### 1.5. Notation

Throughout, (Ω,𝒢,𝖯)(\Omega,\mathscr{G},\mathsf{P}) denotes a probability space. For brevity, we write L0L^{0} for
L0​(Ω,𝒢,𝖯)L^{0}(\Omega,\mathscr{G},\mathsf{P}), the space of (equivalence classes of) measurable
functions, and L∞L^{\infty} for L∞​(Ω,𝒢,𝖯)L^{\infty}(\Omega,\mathscr{G},\mathsf{P}), the space of essentially
bounded functions. Equalities and inequalities between random variables are understood in
the 𝖯\mathsf{P}-almost sure sense.

For x=(x1,…,xn)∈ℝnx=(x\_{1},\ldots,x\_{n})\in\mathbb{R}^{n}, we write x1:n⩽x2:n⩽⋯⩽xn:nx\_{1:n}\leqslant x\_{2:n}\leqslant\cdots\leqslant x\_{n:n}
for the order statistics and s​(x)=(x1:n,…,xn:n)s(x)=(x\_{1:n},\ldots,x\_{n:n}) for the sorted sample.
The standard simplex is

|  |  |  |
| --- | --- | --- |
|  | Δn:={a∈[0,∞)n:∑i=1nai=1},\Delta\_{n}:=\Big\{a\in[0,\infty)^{n}:\sum\_{i=1}^{n}a\_{i}=1\Big\}, |  |

and its monotone subset is

|  |  |  |
| --- | --- | --- |
|  | Δn↓:={a∈Δn:a1⩾a2⩾⋯⩾an}.\Delta\_{n}^{\downarrow}:=\{a\in\Delta\_{n}:a\_{1}\geqslant a\_{2}\geqslant\cdots\geqslant a\_{n}\}. |  |

## 2. Coherent risk measures and coherent risk estimators

This section recalls the basic definitions and fundamental representation theorems,
following the exposition in [[1](https://arxiv.org/html/2602.00784v1#bib.bib1)] and the standard reference [[11](https://arxiv.org/html/2602.00784v1#bib.bib11)].

### 2.1. Coherent risk measures on L∞L^{\infty}

The axiomatic approach to risk measurement begins with economically motivated desiderata
for a ‘good’ risk functional. We interpret X∈L∞X\in L^{\infty} as a random profit and loss
(P&L), with positive values representing gains and negative values representing losses.
The quantity ρ​(X)\rho(X) represents the capital required to make the position XX acceptable.

###### Definition 2.1 (Coherent risk measure).

A functional ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R} is a *coherent risk measure* (CRM) if for all
X,Y∈L∞X,Y\in L^{\infty}, m∈ℝm\in\mathbb{R}, and λ⩾0\lambda\geqslant 0:

1. (R1)

   *Monotonicity:* X⩽YX\leqslant Y implies ρ​(X)⩾ρ​(Y)\rho(X)\geqslant\rho(Y).
2. (R2)

   *Cash additivity:* ρ​(X+m)=ρ​(X)−m\rho(X+m)=\rho(X)-m.
3. (R3)

   *Positive homogeneity:* ρ​(λ​X)=λ​ρ​(X)\rho(\lambda X)=\lambda\rho(X).
4. (R4)

   *Subadditivity:* ρ​(X+Y)⩽ρ​(X)+ρ​(Y)\rho(X+Y)\leqslant\rho(X)+\rho(Y).

The axioms have clear economic interpretations. Monotonicity states that a position with
uniformly better outcomes requires less capital. Cash additivity asserts that adding a
deterministic amount mm to the position reduces the required capital by the same amount.
Positive homogeneity implies that scaling a position scales the risk proportionally.
Subadditivity captures the principle of diversification: the risk of a combined portfolio
does not exceed the sum of individual risks.

The fundamental structural result for CRMs is the robust representation theorem, which
characterises coherent risk measures in terms of their dual sets of probability measures.
We recall one version; see [[8](https://arxiv.org/html/2602.00784v1#bib.bib8), [11](https://arxiv.org/html/2602.00784v1#bib.bib11)] for a comprehensive treatment.

###### Theorem 2.2 (Robust representation on L∞L^{\infty}).

Let ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R} be a coherent risk measure satisfying the *Fatou property*:
if (Xn)(X\_{n}) is a bounded sequence converging 𝖯\mathsf{P}-almost surely to XX, then
ρ​(X)⩽lim infn→∞ρ​(Xn)\rho(X)\leqslant\liminf\_{n\to\infty}\rho(X\_{n}). Then there exists a non-empty convex set
𝒬\mathcal{Q} of probability measures on (Ω,𝒢)(\Omega,\mathscr{G}), each absolutely
continuous with respect to 𝖯\mathsf{P}, such that

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | ρ​(X)=supQ∈𝒬𝖤Q​[−X],X∈L∞.\rho(X)=\sup\_{Q\in\mathcal{Q}}\mathsf{E}\_{Q}[-X],\qquad X\in L^{\infty}. |  |

If, in addition, the set of Radon–Nikodym derivatives
{d​Q/d​𝖯:Q∈𝒬}⊂L1\{dQ/d\mathsf{P}:Q\in\mathcal{Q}\}\subset L^{1} can be chosen σ​(L1,L∞)\sigma(L^{1},L^{\infty})-compact
(equivalently, uniformly integrable and σ​(L1,L∞)\sigma(L^{1},L^{\infty})-closed),
then the supremum is attained for each XX.

The set 𝒬\mathcal{Q} is often interpreted as a family of “stress scenarios” or
“generalised probability assessments”, and the representation ([1](https://arxiv.org/html/2602.00784v1#S2.E1 "In Theorem 2.2 (Robust representation on 𝐿^∞). ‣ 2.1. Coherent risk measures on 𝐿^∞ ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"))
expresses the risk as a worst-case expected loss over these scenarios.

### 2.2. Law invariance and spectral representation

A particularly important class of CRMs are those depending only on the distribution of
the random variable.

###### Definition 2.3 (Law invariance).

A CRM ρ\rho is *law-invariant* if ρ​(X)=ρ​(Y)\rho(X)=\rho(Y) whenever XX and YY have the
same distribution under 𝖯\mathsf{P}.

For law-invariant CRMs on atomless probability spaces, Kusuoka [[14](https://arxiv.org/html/2602.00784v1#bib.bib14)] established
a remarkable representation in terms of expected shortfall:

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | ESα⁡(X):=−1α​∫0αqX​(u)​𝑑u,α∈(0,1],\operatorname{ES}\_{\alpha}(X):=-\frac{1}{\alpha}\int\_{0}^{\alpha}q\_{X}(u)\,du,\qquad\alpha\in(0,1], |  |

where qX:(0,1)→ℝq\_{X}:(0,1)\to\mathbb{R} is the lower quantile function of XX,
qX​(α):=inf{x∈ℝ:FX​(x)⩾α}q\_{X}(\alpha):=\inf\{x\in\mathbb{R}:F\_{X}(x)\geqslant\alpha\}.

###### Remark 2.4 (Parameterisation convention).

In our convention, the parameter α∈(0,1]\alpha\in(0,1] is a *tail probability*: small α\alpha
corresponds to the worst tail of the profit distribution (largest losses). This differs from
the regulatory convention for *loss* distributions, where ES is often quoted at a
“confidence level” close to 11 (e.g., ES0.975\operatorname{ES}\_{0.975} for the 2.5%2.5\% tail of losses).
The two are related by ESαprofit⁡(X)=ES1−αloss⁡(−X)\operatorname{ES}\_{\alpha}^{\text{profit}}(X)=\operatorname{ES}\_{1-\alpha}^{\text{loss}}(-X).

###### Theorem 2.5 (Kusuoka representation [[14](https://arxiv.org/html/2602.00784v1#bib.bib14)]).

Let (Ω,𝒢,𝖯)(\Omega,\mathscr{G},\mathsf{P}) be atomless and ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R} a law-invariant
CRM satisfying the Fatou property. Then there exists a non-empty convex set ℳ\mathcal{M}
of probability measures on (0,1](0,1] such that

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | ρ​(X)=supν∈ℳ∫(0,1]ESα⁡(X)​ν​(d​α),X∈L∞.\rho(X)=\sup\_{\nu\in\mathcal{M}}\int\_{(0,1]}\operatorname{ES}\_{\alpha}(X)\,\nu(d\alpha),\qquad X\in L^{\infty}. |  |

A special case arises when the supremum in ([3](https://arxiv.org/html/2602.00784v1#S2.E3 "In Theorem 2.5 (Kusuoka representation [14]). ‣ 2.2. Law invariance and spectral representation ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")) is achieved by a single
measure, leading to spectral risk measures.

###### Definition 2.6 (Spectral risk measure).

Let φ:[0,1]→[0,∞)\varphi:[0,1]\to[0,\infty) be a function satisfying:

1. (S1)

   φ\varphi is non-increasing;
2. (S2)

   φ\varphi is bounded;
3. (S3)

   ∫01φ​(α)​𝑑α=1\int\_{0}^{1}\varphi(\alpha)\,d\alpha=1.

The *spectral risk measure* with spectrum φ\varphi is

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | ρφ​(X):=−∫01qX​(α)​φ​(α)​𝑑α.\rho\_{\varphi}(X):=-\int\_{0}^{1}q\_{X}(\alpha)\,\varphi(\alpha)\,d\alpha. |  |

Spectral risk measures are coherent and law-invariant. The expected shortfall ESα\operatorname{ES}\_{\alpha}
corresponds to the spectrum φ​(u)=α−1​𝟏(0,α]​(u)\varphi(u)=\alpha^{-1}\mathbf{1}\_{(0,\alpha]}(u).

### 2.3. Coherent risk estimators

We now turn to the finite-sample setting. Fix n∈ℕn\in\mathbb{N} and interpret
x=(x1,…,xn)∈ℝnx=(x\_{1},\ldots,x\_{n})\in\mathbb{R}^{n} as a realised sample of P&L values.

###### Definition 2.7 (Coherent risk estimator [[1](https://arxiv.org/html/2602.00784v1#bib.bib1), Definition 3.1]).

A mapping ρ^n:ℝn→ℝ\hat{\rho}\_{n}:\mathbb{R}^{n}\to\mathbb{R} is a *coherent risk estimator* (CRE) if for all
x,y∈ℝnx,y\in\mathbb{R}^{n}, m∈ℝm\in\mathbb{R}, and λ⩾0\lambda\geqslant 0:

1. (E1)

   *Monotonicity:* xi⩽yix\_{i}\leqslant y\_{i} for all ii implies
   ρ^n​(x)⩾ρ^n​(y)\hat{\rho}\_{n}(x)\geqslant\hat{\rho}\_{n}(y).
2. (E2)

   *Cash additivity:* ρ^n​(x+m​𝟏)=ρ^n​(x)−m\hat{\rho}\_{n}(x+m\mathbf{1})=\hat{\rho}\_{n}(x)-m, where
   𝟏=(1,…,1)\mathbf{1}=(1,\ldots,1).
3. (E3)

   *Positive homogeneity:* ρ^n​(λ​x)=λ​ρ^n​(x)\hat{\rho}\_{n}(\lambda x)=\lambda\hat{\rho}\_{n}(x).
4. (E4)

   *Subadditivity:* ρ^n​(x+y)⩽ρ^n​(x)+ρ^n​(y)\hat{\rho}\_{n}(x+y)\leqslant\hat{\rho}\_{n}(x)+\hat{\rho}\_{n}(y).

The axioms (E1)–(E4) are the direct translations of (R1)–(R4) to the finite-sample
setting. Note that we follow the sign convention of [[1](https://arxiv.org/html/2602.00784v1#bib.bib1)]: larger losses (smaller
xix\_{i}) increase the required capital.

###### Definition 2.8 (Law invariance and comonotonicity for CREs).

A CRE ρ^n\hat{\rho}\_{n} is *law-invariant* if ρ^n​(x)=ρ^n​(σ​(x))\hat{\rho}\_{n}(x)=\hat{\rho}\_{n}(\sigma(x)) for
every permutation σ\sigma of {1,…,n}\{1,\ldots,n\}. It is called *comonotonic* whenever
ρ^n​(x+y)=ρ^n​(x)+ρ^n​(y)\hat{\rho}\_{n}(x+y)=\hat{\rho}\_{n}(x)+\hat{\rho}\_{n}(y) whenever xx and yy are comonotonic,
meaning (xi−xj)​(yi−yj)⩾0(x\_{i}-x\_{j})(y\_{i}-y\_{j})\geqslant 0 for all i,ji,j.

The main representation results for CREs, established in [[1](https://arxiv.org/html/2602.00784v1#bib.bib1)], are:

###### Theorem 2.9 (Robust representation of CREs [[1](https://arxiv.org/html/2602.00784v1#bib.bib1), Theorem 4.1]).

A function ρ^n:ℝn→ℝ\hat{\rho}\_{n}:\mathbb{R}^{n}\to\mathbb{R} is a CRE if and only if there exists a non-empty
convex set Mρ^n∗⊆ΔnM^{\*}\_{\hat{\rho}\_{n}}\subseteq\Delta\_{n} such that

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | ρ^n​(x)=supa∈Mρ^n∗∑i=1nai​(−xi),x∈ℝn,\hat{\rho}\_{n}(x)=\sup\_{a\in M^{\*}\_{\hat{\rho}\_{n}}}\sum\_{i=1}^{n}a\_{i}(-x\_{i}),\qquad x\in\mathbb{R}^{n}, |  |

and the supremum is attained for each xx.

###### Theorem 2.10 (Law-invariant CREs [[1](https://arxiv.org/html/2602.00784v1#bib.bib1), Theorem 4.2]).

A function ρ^n:ℝn→ℝ\hat{\rho}\_{n}:\mathbb{R}^{n}\to\mathbb{R} is a law-invariant CRE if and only if there exists
a non-empty convex set Mρ^ns⊆Δn↓M^{s}\_{\hat{\rho}\_{n}}\subseteq\Delta\_{n}^{\downarrow} such that

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | ρ^n​(x)=supa∈Mρ^ns∑i=1nai​(−xi:n),x∈ℝn,\hat{\rho}\_{n}(x)=\sup\_{a\in M^{s}\_{\hat{\rho}\_{n}}}\sum\_{i=1}^{n}a\_{i}(-x\_{i:n}),\qquad x\in\mathbb{R}^{n}, |  |

with the supremum attained for each xx.

###### Theorem 2.11 (Comonotonic law-invariant CREs [[1](https://arxiv.org/html/2602.00784v1#bib.bib1), Theorem 4.10]).

A function ρ^n:ℝn→ℝ\hat{\rho}\_{n}:\mathbb{R}^{n}\to\mathbb{R} is a comonotonic, law-invariant CRE if and only if
there exists a unique a∈Δn↓a\in\Delta\_{n}^{\downarrow} such that

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | ρ^n​(x)=∑i=1nai​(−xi:n),x∈ℝn.\hat{\rho}\_{n}(x)=\sum\_{i=1}^{n}a\_{i}(-x\_{i:n}),\qquad x\in\mathbb{R}^{n}. |  |

Our goal in the following sections is to provide a unified hyperfinite perspective on
these results and to establish new consistency and asymptotic theorems.

## 3. Non-standard analysis: a self-contained introduction

This section provides the essential non-standard machinery required for our applications.
We aim for a self-contained exposition accessible to readers without prior exposure to
NSA, whilst maintaining sufficient rigour for our proofs. For comprehensive treatments,
see Keisler [[13](https://arxiv.org/html/2602.00784v1#bib.bib13)], Albeverio et al. [[3](https://arxiv.org/html/2602.00784v1#bib.bib3)], and Fajardo–Keisler
[[10](https://arxiv.org/html/2602.00784v1#bib.bib10)].

### 3.1. Standing conventions and the Loeb model

###### Convention 3.1 (Saturation assumption).

Throughout this paper, we work in a *countably saturated* non-standard enlargement:
every countable collection of internal sets with the finite intersection property has
non-empty intersection. This level of saturation suffices for all constructions in this paper,
including overspill/underspill arguments and the existence of Loeb measures. Countable saturation
can be arranged in standard constructions, e.g., via an ultrapower by a non-principal ultrafilter
on ℕ\mathbb{N} in a countable superstructure setting; see [[3](https://arxiv.org/html/2602.00784v1#bib.bib3), Ch. 4].

###### Notation 3.2 (Standing Loeb model).

Throughout Sections [3](https://arxiv.org/html/2602.00784v1#S3 "3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")–[10](https://arxiv.org/html/2602.00784v1#S10 "10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") we work inside a fixed countably
saturated non-standard universe. When we invoke hyperfinite probability, we use the
following canonical model.

We fix an infinite N∈ℕ∗N\in{}^{\*}\mathbb{N}, chosen once and for all by the mechanism described in
Lemma [3.3](https://arxiv.org/html/2602.00784v1#S3.Thmtheorem3 "Lemma 3.3 (Simultaneous validity of hyperfinite properties). ‣ 3.1. Standing conventions and the Loeb model ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") below. The hyperfinite set IN={1,…,N}I\_{N}=\{1,\dots,N\} carries the internal
counting measure μN​(A)=|A|/N\mu\_{N}(A)=|A|/N on the algebra ℐN\mathscr{I}\_{N} of internal subsets.
Let (IN,ℐNL,L​(μN))(I\_{N},\mathscr{I}\_{N}^{L},L(\mu\_{N})) denote the associated Loeb probability space.

When we state results about i.i.d. samples (Xi)(X\_{i}) from a random variable XX on an
ambient probability space (Ω,𝒢,𝖯)(\Omega,\mathscr{G},\mathsf{P}), we implicitly pass to the
non-standard extension (Ω∗,𝒢∗,𝖯∗)({}^{\*}\Omega,{}^{\*}\mathscr{G},{}^{\*}\mathsf{P}) and its Loeb
completion (Ω∗,L​(𝒢∗),L​(𝖯∗))({}^{\*}\Omega,L({}^{\*}\mathscr{G}),L({}^{\*}\mathsf{P})); all “almost sure”
statements in NSA arguments are understood with respect to L​(𝖯∗)L({}^{\*}\mathsf{P}) unless
explicitly stated otherwise.

Star-suppression convention.
When a standard function ff is evaluated at a hyperreal argument, we mean, by convention, its
non-standard extension f∗{}^{\*}f; e.g. q​(αk)q(\alpha\_{k}) abbreviates q∗​(αk){}^{\*}q(\alpha\_{k}).

###### Lemma 3.3 (Simultaneous validity of hyperfinite properties).

Let (Pj)j∈ℕ(P\_{j})\_{j\in\mathbb{N}} be a countable family of properties, where each Pj​(n)P\_{j}(n) is a
*first-order* statement about sample size nn expressible with rational parameters
(e.g., “𝖯∗​(|⋯|>ε)<δ{}^{\*}\mathsf{P}(|\cdots|>\varepsilon)<\delta” for rational ε,δ>0\varepsilon,\delta>0).
By the internal definition principle, each set

|  |  |  |
| --- | --- | --- |
|  | Sj:={n∈ℕ∗:Pj​(n)​ holds}S\_{j}:=\{n\in{}^{\*}\mathbb{N}:P\_{j}(n)\text{ holds}\} |  |

is internal. Assume each PjP\_{j} holds eventually for standard nn, i.e., SjS\_{j} contains
all sufficiently large standard naturals.

Then there exists an *infinite* N∈ℕ∗N\in{}^{\*}\mathbb{N} such that Pj​(N)P\_{j}(N) holds for all j∈ℕj\in\mathbb{N}.

###### Proof.

For each standard m∈ℕm\in\mathbb{N}, define the internal set Bm:={n∈ℕ∗:n>m}B\_{m}:=\{n\in{}^{\*}\mathbb{N}:n>m\}.
Consider the countable family of internal sets {Sj}j∈ℕ∪{Bm}m∈ℕ\{S\_{j}\}\_{j\in\mathbb{N}}\cup\{B\_{m}\}\_{m\in\mathbb{N}}.

This family has the finite intersection property: for any finite J⊂ℕJ\subset\mathbb{N} and
finite M⊂ℕM\subset\mathbb{N}, the intersection ⋂j∈JSj∩⋂m∈MBm\bigcap\_{j\in J}S\_{j}\cap\bigcap\_{m\in M}B\_{m}
contains all standard n>max⁡(maxj∈J⁡n0(j),max⁡M)n>\max(\max\_{j\in J}n\_{0}^{(j)},\max M), hence is non-empty.

By countable saturation, ⋂j∈ℕSj∩⋂m∈ℕBm≠∅\bigcap\_{j\in\mathbb{N}}S\_{j}\cap\bigcap\_{m\in\mathbb{N}}B\_{m}\neq\emptyset.
Any element NN of this intersection satisfies Pj​(N)P\_{j}(N) for all jj (since N∈SjN\in S\_{j})
and N>mN>m for all standard mm (since N∈BmN\in B\_{m}), hence NN is infinite.
∎

###### Remark 3.4 (Properties used in this paper).

The properties PjP\_{j} we invoke include: the hyperfinite strong law of large numbers
(Theorem [3.18](https://arxiv.org/html/2602.00784v1#S3.Thmtheorem18 "Theorem 3.18 (Hyperfinite strong law of large numbers). ‣ 3.7. The hyperfinite strong law and Glivenko–Cantelli theorem ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")) for countably many integrands arising from truncations,
the hyperfinite Glivenko–Cantelli theorem (Theorem [3.20](https://arxiv.org/html/2602.00784v1#S3.Thmtheorem20 "Theorem 3.20 (Hyperfinite Glivenko–Cantelli / quantile shadow). ‣ 3.7. The hyperfinite strong law and Glivenko–Cantelli theorem ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")), and the hyperfinite
CLT (Theorem [10.1](https://arxiv.org/html/2602.00784v1#S10.Thmtheorem1 "Theorem 10.1 (Hyperfinite CLT). ‣ 10.1. Hyperfinite central limit theorem ‣ 10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")). Each is expressed in the first-order form
“∀ε∈ℚ>0​∃n0​∀n⩾n0\forall\varepsilon\in\mathbb{Q}\_{>0}\,\exists n\_{0}\,\forall n\geqslant n\_{0}: [bound holds]”,
which transfers to give internal sets SjS\_{j}. Lemma [3.3](https://arxiv.org/html/2602.00784v1#S3.Thmtheorem3 "Lemma 3.3 (Simultaneous validity of hyperfinite properties). ‣ 3.1. Standing conventions and the Loeb model ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") then
guarantees a single infinite NN for which all hold simultaneously.

###### Proposition 3.5 (Atomless separable spaces and Loeb spaces).

Every atomless *separable* (i.e., countably generated mod null sets) standard probability
space (Ω,𝒢,𝖯)(\Omega,\mathscr{G},\mathsf{P}) is measure-algebra isomorphic to a hyperfinite Loeb space
(IN,ℐNL,L​(μN))(I\_{N},\mathscr{I}\_{N}^{L},L(\mu\_{N})) for some infinite N∈ℕ∗N\in{}^{\*}\mathbb{N}.
Precisely, there is a Boolean algebra isomorphism

|  |  |  |
| --- | --- | --- |
|  | Φ:𝒢/𝒩𝖯→≅ℐNL/𝒩L​(μN)\Phi:\mathscr{G}/\mathcal{N}\_{\mathsf{P}}\xrightarrow{\;\cong\;}\mathscr{I}\_{N}^{L}/\mathcal{N}\_{L(\mu\_{N})} |  |

between the measure algebras (quotients by null sets) such that 𝖯​(A)=L​(μN)​(Φ​([A]))\mathsf{P}(A)=L(\mu\_{N})(\Phi([A]))
for all A∈𝒢A\in\mathscr{G}. This isomorphism induces isometric lattice isomorphisms
Lp​(Ω,𝖯)≅Lp​(IN,L​(μN))L^{p}(\Omega,\mathsf{P})\cong L^{p}(I\_{N},L(\mu\_{N})) for all p∈[1,∞]p\in[1,\infty].

###### Proof (reference).

This is Keisler’s representation theorem; see [[10](https://arxiv.org/html/2602.00784v1#bib.bib10), Thm. 10.3.1] or [[3](https://arxiv.org/html/2602.00784v1#bib.bib3), Ch. 5].
The key fact is that the hyperfinite Loeb space (IN,ℐNL,L​(μN))(I\_{N},\mathscr{I}\_{N}^{L},L(\mu\_{N})) with infinite NN is
atomless and has the same measure algebra (mod null sets) as the Lebesgue unit interval.
Every atomless separable probability space shares this property by Maharam’s theorem.
∎

For distributional/statistical arguments, when the underlying standard probability space
is atomless and separable (which includes all standard Borel probability spaces), we may
replace it by an isomorphic Loeb space via Proposition [3.5](https://arxiv.org/html/2602.00784v1#S3.Thmtheorem5 "Proposition 3.5 (Atomless separable spaces and Loeb spaces). ‣ 3.1. Standing conventions and the Loeb model ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"). This convention
avoids repeated measure-theoretic bookkeeping and allows us to treat hyperfinite sums as
Loeb integrals via standard part.

### 3.2. The hyperreal numbers

The starting point of non-standard analysis is the construction of an ordered field
extension ℝ∗{}^{\*}\mathbb{R} of ℝ\mathbb{R}, called the *hyperreals*. There are several approaches
to this construction (ultraproducts, superstructures, axiomatic); we adopt the axiomatic
viewpoint, which suffices for applications.

###### Definition 3.6 (Hyperreal numbers).

The *hyperreal numbers* ℝ∗{}^{\*}\mathbb{R} form an ordered field extension of ℝ\mathbb{R} satisfying
the following properties:

1. (H1)

   ℝ⊂ℝ∗\mathbb{R}\subset{}^{\*}\mathbb{R} is a proper ordered subfield.
2. (H2)

   (*Transfer principle*) Every first-order statement about ℝ\mathbb{R} that is true
   remains true when interpreted in ℝ∗{}^{\*}\mathbb{R}.
3. (H3)

   There exist *infinitesimals* ε∈ℝ∗\varepsilon\in{}^{\*}\mathbb{R} with
   |ε|<1/n|\varepsilon|<1/n for all n∈ℕn\in\mathbb{N}.
4. (H4)

   There exist *infinite* hyperreals H∈ℝ∗H\in{}^{\*}\mathbb{R} with |H|>n|H|>n for all
   n∈ℕn\in\mathbb{N}.

(In standard constructions, (H3) and (H4) follow from (H1) and (H2) together with properness.)

The transfer principle is the key tool for moving between standard and non-standard
contexts. It asserts that the hyperreals satisfy the same first-order properties as the
reals. For instance, the statement “for all x,y∈ℝx,y\in\mathbb{R} with x<yx<y, there exists
z∈ℝz\in\mathbb{R} with x<z<yx<z<y” transfers to “for all x,y∈ℝ∗x,y\in{}^{\*}\mathbb{R} with x<yx<y,
there exists z∈ℝ∗z\in{}^{\*}\mathbb{R} with x<z<yx<z<y.”

###### Definition 3.7 (Finite, infinitesimal, infinite).

A hyperreal x∈ℝ∗x\in{}^{\*}\mathbb{R} is:

* •

  *finite* if |x|⩽n|x|\leqslant n for some n∈ℕn\in\mathbb{N};
* •

  *infinitesimal* if |x|<1/n|x|<1/n for all n∈ℕn\in\mathbb{N};
* •

  *infinite* if |x|>n|x|>n for all n∈ℕn\in\mathbb{N}.

Two hyperreals x,yx,y are *infinitely close*, written x≈yx\approx y, if x−yx-y is
infinitesimal.

The following proposition provides the crucial connection between finite hyperreals and
real numbers.

###### Proposition 3.8 (Standard part).

Every finite hyperreal x∈ℝ∗x\in{}^{\*}\mathbb{R} is infinitely close to a unique real number,
denoted st⁡(x)∈ℝ\operatorname{st}(x)\in\mathbb{R} and called its *standard part*. The map
st:{x∈ℝ∗:x​ is finite}→ℝ\operatorname{st}:\{x\in{}^{\*}\mathbb{R}:x\text{ is finite}\}\to\mathbb{R} satisfies:

1. (i)

   st⁡(x+y)=st⁡(x)+st⁡(y)\operatorname{st}(x+y)=\operatorname{st}(x)+\operatorname{st}(y) for finite x,yx,y;
2. (ii)

   st⁡(x​y)=st⁡(x)​st⁡(y)\operatorname{st}(xy)=\operatorname{st}(x)\operatorname{st}(y) for finite x,yx,y;
3. (iii)

   st⁡(x)⩽st⁡(y)\operatorname{st}(x)\leqslant\operatorname{st}(y) if x⩽yx\leqslant y for finite x,yx,y;
4. (iv)

   st⁡(r)=r\operatorname{st}(r)=r for all r∈ℝr\in\mathbb{R}.

###### Proof.

For any finite xx, the set {r∈ℝ:r⩽x}\{r\in\mathbb{R}:r\leqslant x\} is non-empty and bounded above,
hence has a supremum s:=sup{r∈ℝ:r⩽x}s:=\sup\{r\in\mathbb{R}:r\leqslant x\}. We claim x≈sx\approx s. If
x−s>1/nx-s>1/n for some n∈ℕn\in\mathbb{N}, then s+1/(2​n)<xs+1/(2n)<x and s+1/(2​n)∈ℝs+1/(2n)\in\mathbb{R},
contradicting the definition of ss. Similarly, if s−x>1/ns-x>1/n, then s−1/(2​n)>xs-1/(2n)>x
implies s−1/(2​n)s-1/(2n) is an upper bound for {r∈ℝ:r⩽x}\{r\in\mathbb{R}:r\leqslant x\}, contradicting the
supremum. Thus |x−s|<1/n|x-s|<1/n for all nn, i.e., x≈sx\approx s.

Uniqueness: if x≈sx\approx s and x≈s′x\approx s^{\prime} with s,s′∈ℝs,s^{\prime}\in\mathbb{R}, then s−s′s-s^{\prime} is
infinitesimal and real, hence zero.

The algebraic properties follow from the corresponding properties of ≈\approx and the
field operations.
∎

### 3.3. The hypernaturals and hyperfinite sets

The natural numbers ℕ\mathbb{N} extend to the *hypernaturals* ℕ∗⊂ℝ∗{}^{\*}\mathbb{N}\subset{}^{\*}\mathbb{R}. By
the transfer principle, ℕ∗{}^{\*}\mathbb{N} satisfies all first-order properties of ℕ\mathbb{N}. However,
ℕ∗{}^{\*}\mathbb{N} properly contains ℕ\mathbb{N}: there exist *infinite hypernaturals*
N∈ℕ∗∖ℕN\in{}^{\*}\mathbb{N}\setminus\mathbb{N} satisfying N>nN>n for all n∈ℕn\in\mathbb{N}.

###### Definition 3.9 (Hyperfinite set).

For N∈ℕ∗N\in{}^{\*}\mathbb{N}, the set

|  |  |  |
| --- | --- | --- |
|  | IN:={1,2,…,N}={k∈ℕ∗:1⩽k⩽N}I\_{N}:=\{1,2,\ldots,N\}=\{k\in{}^{\*}\mathbb{N}:1\leqslant k\leqslant N\} |  |

is called a *hyperfinite set*. It is *internal* in the sense that it arises
from the non-standard extension.

The crucial property of hyperfinite sets is that they behave like finite sets from the
internal perspective. In particular:

###### Proposition 3.10 (Internal finite operations).

Let N∈ℕ∗N\in{}^{\*}\mathbb{N} (possibly infinite) and let f:IN→ℝ∗f:I\_{N}\to{}^{\*}\mathbb{R} be an internal function.
Then:

1. (i)

   The hyperfinite sum ∑k=1Nf​(k)∈ℝ∗\sum\_{k=1}^{N}f(k)\in{}^{\*}\mathbb{R} is well-defined.
2. (ii)

   The hyperfinite product ∏k=1Nf​(k)∈ℝ∗\prod\_{k=1}^{N}f(k)\in{}^{\*}\mathbb{R} is well-defined.
3. (iii)

   The maximum maxk∈IN⁡f​(k)\max\_{k\in I\_{N}}f(k) and minimum mink∈IN⁡f​(k)\min\_{k\in I\_{N}}f(k) are
   well-defined.
4. (iv)

   Sorting: if ff takes values in ℝ∗{}^{\*}\mathbb{R}, then there exists an *internal* permutation
   σ:IN→IN\sigma:I\_{N}\to I\_{N} such that f​(σ​(1))⩽f​(σ​(2))⩽⋯⩽f​(σ​(N))f(\sigma(1))\leqslant f(\sigma(2))\leqslant\cdots\leqslant f(\sigma(N)).

These properties follow from the transfer principle applied to the corresponding statements
about finite sets. In particular, for (iv) we transfer the statement “for every finite set
SS and function g:S→ℝg:S\to\mathbb{R} there exists a permutation σ\sigma sorting gg”; this yields
an *internal* permutation σ\sigma, which is essential for later applications to
order statistics.

### 3.4. Internal and external sets

A fundamental distinction in NSA is between *internal* and *external* sets.
Internal sets arise from the non-standard extension and satisfy the transfer principle;
external sets do not.

###### Example 3.11.

The set IN={1,2,…,N}I\_{N}=\{1,2,\dots,N\} for N∈ℕ∗N\in{}^{\*}\mathbb{N} is internal. The set ℕ\mathbb{N} itself,
viewed as a subset of ℕ∗{}^{\*}\mathbb{N}, is external when ℕ∗≠ℕ{}^{\*}\mathbb{N}\neq\mathbb{N}.

A convenient way to see this without appealing to second-order quantification is the
following. In the standard universe, for every m∈ℕm\in\mathbb{N} every non-empty subset of
{1,…,m}\{1,\dots,m\} has a maximum. This *is* a first-order statement in the superstructure.
By transfer, for every M∈ℕ∗M\in{}^{\*}\mathbb{N} every non-empty *internal* subset of IMI\_{M} has a
maximum.

Now pick an infinite H∈ℕ∗H\in{}^{\*}\mathbb{N}. Then ℕ⊆IH\mathbb{N}\subseteq I\_{H}. If ℕ\mathbb{N} were internal, it would be
an internal non-empty subset of IHI\_{H} and hence would have a maximum, contradicting the
fact that ℕ\mathbb{N} has no largest element. Therefore ℕ\mathbb{N} is external.

###### Proposition 3.12 (Internal definition principle).

If P​(x)P(x) is a first-order property and AA is an internal set, then
{x∈A:P​(x)}\{x\in A:P(x)\} is internal.

### 3.5. Loeb measure: from hyperfinite to standard probability

The Loeb construction [[15](https://arxiv.org/html/2602.00784v1#bib.bib15)] is the key tool for producing genuine probability spaces
from internal hyperfinite structures. We describe it in the context most relevant to our
applications.

Fix an infinite N∈ℕ∗N\in{}^{\*}\mathbb{N} and consider the hyperfinite set IN={1,…,N}I\_{N}=\{1,\ldots,N\}.
Let ℐN\mathscr{I}\_{N} denote the algebra of all internal subsets of INI\_{N}. Define the
*internal counting probability measure* μN:ℐN→[0,1]∗\mu\_{N}:\mathscr{I}\_{N}\to{}^{\*}[0,1] by

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | μN​(A):=|A|N,A∈ℐN,\mu\_{N}(A):=\frac{|A|}{N},\qquad A\in\mathscr{I}\_{N}, |  |

where |A|∈ℕ∗|A|\in{}^{\*}\mathbb{N} is the internal cardinality of AA.

The triple (IN,ℐN,μN)(I\_{N},\mathscr{I}\_{N},\mu\_{N}) is an internal finitely additive probability
space. The Loeb construction promotes this to a genuine σ\sigma-additive probability
space.

###### Theorem 3.13 (Loeb measure construction).

Define the *Loeb premeasure* μN0:ℐN→[0,1]\mu\_{N}^{0}:\mathscr{I}\_{N}\to[0,1] by
μN0​(A):=st⁡(μN​(A))\mu\_{N}^{0}(A):=\operatorname{st}(\mu\_{N}(A)) for A∈ℐNA\in\mathscr{I}\_{N}.
Define an outer measure L∗​(μN)L^{\*}(\mu\_{N}) on *all* subsets B⊆INB\subseteq I\_{N} by

|  |  |  |
| --- | --- | --- |
|  | L∗​(μN)​(B):=inf{μN0​(A):A∈ℐN,B⊆A}.L^{\*}(\mu\_{N})(B):=\inf\{\mu\_{N}^{0}(A):\ A\in\mathscr{I}\_{N},\ B\subseteq A\}. |  |

Let ℐNL\mathscr{I}\_{N}^{L} be the σ\sigma-algebra of L∗​(μN)L^{\*}(\mu\_{N})-measurable sets in the
sense of Carathéodory, and define L​(μN):=L∗​(μN)↾ℐNLL(\mu\_{N}):=L^{\*}(\mu\_{N})\!\upharpoonright\_{\mathscr{I}\_{N}^{L}}.
Then:

1. (i)

   μN0\mu\_{N}^{0} is a finitely additive probability measure on the internal algebra
   ℐN\mathscr{I}\_{N}.
2. (ii)

   ℐN⊆ℐNL\mathscr{I}\_{N}\subseteq\mathscr{I}\_{N}^{L}, and L​(μN)L(\mu\_{N}) is a complete σ\sigma-additive
   probability measure on ℐNL\mathscr{I}\_{N}^{L} extending μN0\mu\_{N}^{0}.
3. (iii)

   In particular, σ​(ℐN)⊆ℐNL\sigma(\mathscr{I}\_{N})\subseteq\mathscr{I}\_{N}^{L}, and the restriction
   of L​(μN)L(\mu\_{N}) to σ​(ℐN)\sigma(\mathscr{I}\_{N}) is a σ\sigma-additive extension of μN0\mu\_{N}^{0}.

###### Proof (reference).

The key step is verifying that the Carathéodory construction yields a complete
σ\sigma-additive measure. The countable subadditivity of μN0\mu\_{N}^{0} on
ℐN\mathscr{I}\_{N} (which follows from the internal finite additivity and saturation)
is the crucial ingredient. For the full argument, see Loeb [[15](https://arxiv.org/html/2602.00784v1#bib.bib15)] or
[[3](https://arxiv.org/html/2602.00784v1#bib.bib3), Ch. 5] and [[10](https://arxiv.org/html/2602.00784v1#bib.bib10), Chs. 4–5].
∎

###### Remark 3.14.

The Loeb space is rich enough to support continuous distributions, despite being built
from a discrete internal structure. For instance, if NN is infinite, the Loeb space
(IN,ℐNL,L​(μN))(I\_{N},\mathscr{I}\_{N}^{L},L(\mu\_{N})) is atomless.

### 3.6. Hyperfinite integration and the Riemann sum approximation

The Loeb measure allows us to integrate functions on hyperfinite spaces. For our purposes,
the following connection between hyperfinite sums and standard integrals is fundamental.

###### Proposition 3.15 (Hyperfinite Riemann approximation).

Let f:[0,1]→ℝf:[0,1]\to\mathbb{R} be bounded and Riemann integrable, and let f∗:[0,1]∗→ℝ∗{}^{\*}f:{}^{\*}[0,1]\to{}^{\*}\mathbb{R}
be its non-standard extension. For any infinite N∈ℕ∗N\in{}^{\*}\mathbb{N},

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | ∫01f​(t)​𝑑t=st⁡(1N​∑k=1Nf∗​(kN)).\int\_{0}^{1}f(t)\,dt=\operatorname{st}\left(\frac{1}{N}\sum\_{k=1}^{N}{}^{\*}f\left(\frac{k}{N}\right)\right). |  |

###### Proof.

By Riemann integrability, for each ε>0\varepsilon>0 there exists n0∈ℕn\_{0}\in\mathbb{N} such that
for all n⩾n0n\geqslant n\_{0},

|  |  |  |
| --- | --- | --- |
|  | |∫01f​(t)​𝑑t−1n​∑k=1nf​(kn)|<ε.\left|\int\_{0}^{1}f(t)\,dt-\frac{1}{n}\sum\_{k=1}^{n}f\left(\frac{k}{n}\right)\right|<\varepsilon. |  |

By transfer, this statement holds for all n∈ℕ∗n\in{}^{\*}\mathbb{N} with n⩾n0n\geqslant n\_{0}. In particular,
it holds for the infinite NN, giving

|  |  |  |
| --- | --- | --- |
|  | |∫01f​(t)​𝑑t−1N​∑k=1Nf∗​(kN)|<ε.\left|\int\_{0}^{1}f(t)\,dt-\frac{1}{N}\sum\_{k=1}^{N}{}^{\*}f\left(\frac{k}{N}\right)\right|<\varepsilon. |  |

Since ε>0\varepsilon>0 was arbitrary, the hyperfinite sum differs from the integral by
an infinitesimal, and taking standard parts yields ([9](https://arxiv.org/html/2602.00784v1#S3.E9 "In Proposition 3.15 (Hyperfinite Riemann approximation). ‣ 3.6. Hyperfinite integration and the Riemann sum approximation ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")).
∎

###### Proposition 3.16 (Loeb lifting for L1L^{1}-functions on the hyperfinite grid).

Let f∈L1​([0,1],λ)f\in L^{1}([0,1],\lambda), where λ\lambda is Lebesgue measure. Fix an infinite
N∈ℕ∗N\in{}^{\*}\mathbb{N} and write IN={1,…,N}I\_{N}=\{1,\dots,N\}. Then there exists an internal function
F:IN→ℝ∗F:I\_{N}\to{}^{\*}\mathbb{R} such that:

1. (i)

   f​(st⁡(k/N))=st⁡(F​(k))f(\operatorname{st}(k/N))=\operatorname{st}(F(k)) for L​(μN)L(\mu\_{N})-almost all k∈INk\in I\_{N};
2. (ii)

   FF is SS-integrable (equivalently, Loeb integrable) and

   |  |  |  |
   | --- | --- | --- |
   |  | ∫01f​(t)​𝑑t=st⁡(1N​∑k=1NF​(k)).\int\_{0}^{1}f(t)\,dt=\operatorname{st}\Big(\frac{1}{N}\sum\_{k=1}^{N}F(k)\Big). |  |

If, in addition, ff is bounded and Riemann integrable, one may choose F​(k)=f∗​(k/N)F(k)={}^{\*}f(k/N).

###### Proof (reference).

This is a standard lifting result in Loeb integration theory: every L1L^{1} function admits
an internal SS-integrable lifting on the hyperfinite grid, and the Loeb integral equals
the standard part of the internal counting integral. See, for example,
[[10](https://arxiv.org/html/2602.00784v1#bib.bib10), Chs. 4–5] (Loeb liftings and SS-integrability) or [[3](https://arxiv.org/html/2602.00784v1#bib.bib3), Ch. 5].
The last sentence follows from Proposition [3.15](https://arxiv.org/html/2602.00784v1#S3.Thmtheorem15 "Proposition 3.15 (Hyperfinite Riemann approximation). ‣ 3.6. Hyperfinite integration and the Riemann sum approximation ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics").
∎

###### Remark 3.17 (A concrete SS-integrability criterion).

An internal function F:IN→ℝ∗F:I\_{N}\to{}^{\*}\mathbb{R} is called *SS-integrable* if
1N​∑k=1N|F​(k)|\frac{1}{N}\sum\_{k=1}^{N}|F(k)| is finite and, for every internal A⊆INA\subseteq I\_{N} with
μN​(A)≈0\mu\_{N}(A)\approx 0, one has 1N​∑k∈A|F​(k)|≈0\frac{1}{N}\sum\_{k\in A}|F(k)|\approx 0.
In that case st⁡(F)\operatorname{st}(F) is Loeb integrable and its Loeb integral equals the standard part
of the internal counting integral.

### 3.7. The hyperfinite strong law and Glivenko–Cantelli theorem

For statistical applications, we need the non-standard versions of classical limit theorems.

###### Theorem 3.18 (Hyperfinite strong law of large numbers).

Let (Xi)i∈ℕ(X\_{i})\_{i\in\mathbb{N}} be i.i.d. with 𝖤​[|X1|]<∞\mathsf{E}[|X\_{1}|]<\infty on (Ω,𝒢,𝖯)(\Omega,\mathscr{G},\mathsf{P}).
Let N∈ℕ∗N\in{}^{\*}\mathbb{N} be infinite and consider the hyperfinite extension
(X1,…,XN)(X\_{1},\dots,X\_{N}) as random variables on (Ω∗,L​(𝒢∗),L​(𝖯∗))({}^{\*}\Omega,L({}^{\*}\mathscr{G}),L({}^{\*}\mathsf{P})).
Then

|  |  |  |
| --- | --- | --- |
|  | 1N​∑k=1NXk≈𝖤​[X1]holds L​(𝖯∗)-almost surely.\frac{1}{N}\sum\_{k=1}^{N}X\_{k}\approx\mathsf{E}[X\_{1}]\qquad\text{holds $L({}^{\*}\mathsf{P})$-almost surely.} |  |

###### Proof.

By the classical strong law, 1n​∑k=1nXk→𝖤​[X1]\frac{1}{n}\sum\_{k=1}^{n}X\_{k}\to\mathsf{E}[X\_{1}] almost surely as
n→∞n\to\infty. For each rational ε>0\varepsilon>0, define

|  |  |  |
| --- | --- | --- |
|  | Aε:={ω∈Ω:∃n0∈ℕ​ such that ​∀n⩾n0,|1n​∑k=1nXk​(ω)−𝖤​[X1]|<ε}.A\_{\varepsilon}:=\left\{\omega\in\Omega:\exists n\_{0}\in\mathbb{N}\text{ such that }\forall n\geqslant n\_{0},\left|\frac{1}{n}\sum\_{k=1}^{n}X\_{k}(\omega)-\mathsf{E}[X\_{1}]\right|<\varepsilon\right\}. |  |

This set is 𝒢\mathscr{G}-measurable (it is a countable union/intersection of measurable events),
and the strong law gives 𝖯​(Aε)=1\mathsf{P}(A\_{\varepsilon})=1.

The non-standard extension Aε∗⊆Ω∗{}^{\*}A\_{\varepsilon}\subseteq{}^{\*}\Omega is internal (it is the star-extension
of a standard set), hence Aε∗∈𝒢∗⊆L​(𝒢∗){}^{\*}A\_{\varepsilon}\in{}^{\*}\mathscr{G}\subseteq L({}^{\*}\mathscr{G}).
Moreover,

|  |  |  |
| --- | --- | --- |
|  | L​(𝖯∗)​(Aε∗)=st⁡(𝖯∗​(Aε∗))=st⁡(𝖯​(Aε))=1,L({}^{\*}\mathsf{P})({}^{\*}A\_{\varepsilon})=\operatorname{st}({}^{\*}\mathsf{P}({}^{\*}A\_{\varepsilon}))=\operatorname{st}(\mathsf{P}(A\_{\varepsilon}))=1, |  |

using the fact that 𝖯∗​(Aε∗)=𝖯​(Aε){}^{\*}\mathsf{P}({}^{\*}A\_{\varepsilon})=\mathsf{P}(A\_{\varepsilon}) by transfer of the probability.

For ω∈Aε∗\omega\in{}^{\*}A\_{\varepsilon}, the internal statement
“∃n0∈ℕ∗\exists n\_{0}\in{}^{\*}\mathbb{N} such that ∀n∈ℕ∗\forall n\in{}^{\*}\mathbb{N} with n⩾n0n\geqslant n\_{0},
|1n​∑k=1nXk​(ω)−𝖤​[X1]|<ε|\frac{1}{n}\sum\_{k=1}^{n}X\_{k}(\omega)-\mathsf{E}[X\_{1}]|<\varepsilon”
holds (by transfer of the defining property of AεA\_{\varepsilon}).
In particular, it holds for the infinite NN, giving
|1N​∑k=1NXk​(ω)−𝖤​[X1]|<ε|\frac{1}{N}\sum\_{k=1}^{N}X\_{k}(\omega)-\mathsf{E}[X\_{1}]|<\varepsilon.

Since L​(𝖯∗)​(Aε∗)=1L({}^{\*}\mathsf{P})({}^{\*}A\_{\varepsilon})=1 for each rational ε>0\varepsilon>0, intersecting over
ε∈ℚ>0\varepsilon\in\mathbb{Q}\_{>0} (a countable intersection of Loeb-measure-one sets) yields the claim
L​(𝖯∗)L({}^{\*}\mathsf{P})-almost surely.
∎

###### Remark 3.19 (Two-level almost sure statements).

In hyperfinite sampling statements we use two measures simultaneously:
L​(𝖯∗)L({}^{\*}\mathsf{P}) governs the randomness of the sample path ω∈Ω∗\omega\in{}^{\*}\Omega,
while L​(μN)L(\mu\_{N}) governs the fraction of indices k∈INk\in I\_{N} for a fixed sample path.
Thus “for L​(μN)L(\mu\_{N})-almost all kk” should be read as: for L​(𝖯∗)L({}^{\*}\mathsf{P})-almost all
sample outcomes, the exceptional set of indices has Loeb counting measure zero.

###### Theorem 3.20 (Hyperfinite Glivenko–Cantelli / quantile shadow).

Let (Xi)i∈ℕ(X\_{i})\_{i\in\mathbb{N}} be i.i.d. with distribution function FF and lower quantile function
q​(α)=inf{x:F​(x)⩾α}q(\alpha)=\inf\{x:\,F(x)\geqslant\alpha\}. Assume 𝖤​[|X1|]<∞\mathsf{E}[|X\_{1}|]<\infty, equivalently
∫01|q​(α)|​𝑑α<∞\int\_{0}^{1}|q(\alpha)|\,d\alpha<\infty.

Fix an infinite N∈ℕ∗N\in{}^{\*}\mathbb{N} and consider the hyperfinite sample (X1,…,XN)(X\_{1},\dots,X\_{N}) with order
statistics X1:N⩽⋯⩽XN:NX\_{1:N}\leqslant\cdots\leqslant X\_{N:N}. Let αk:=k/N\alpha\_{k}:=k/N.

Then L​(𝖯∗)L({}^{\*}\mathsf{P})-almost surely, the set of indices

|  |  |  |
| --- | --- | --- |
|  | G:={k∈IN:Xk:N≈q​(αk)}G:=\{k\in I\_{N}:\ X\_{k:N}\approx q(\alpha\_{k})\} |  |

has Loeb counting measure L​(μN)​(G)=1L(\mu\_{N})(G)=1.

Moreover, for every bounded *Riemann integrable* g:[0,1]→ℝg:[0,1]\to\mathbb{R} with
∫01|g​(α)​q​(α)|​𝑑α<∞\int\_{0}^{1}|g(\alpha)q(\alpha)|\,d\alpha<\infty, we have

|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | st⁡(1N​∑k=1Ng​(αk)​Xk:N)=∫01g​(α)​q​(α)​𝑑α.\operatorname{st}\Big(\frac{1}{N}\sum\_{k=1}^{N}g(\alpha\_{k})X\_{k:N}\Big)=\int\_{0}^{1}g(\alpha)q(\alpha)\,d\alpha. |  |

###### Proof.

*Internal infinitesimal bound via convergence in probability.*
The classical Glivenko–Cantelli theorem states that supx|Fn​(x)−F​(x)|→0\sup\_{x}|F\_{n}(x)-F(x)|\to 0 almost surely.
The following weaker consequence suffices: for every η>0\eta>0,

|  |  |  |
| --- | --- | --- |
|  | 𝖯​(supx|Fn​(x)−F​(x)|>η)→0as ​n→∞.\mathsf{P}\Big(\sup\_{x}|F\_{n}(x)-F(x)|>\eta\Big)\to 0\quad\text{as }n\to\infty. |  |

This is a first-order statement: for every standard η>0\eta>0 and δ>0\delta>0, there exists
n0∈ℕn\_{0}\in\mathbb{N} such that for all n⩾n0n\geqslant n\_{0}, 𝖯​(supx|Fn−F|>η)<δ\mathsf{P}(\sup\_{x}|F\_{n}-F|>\eta)<\delta.

By transfer, for our fixed infinite NN and any standard η,δ>0\eta,\delta>0,

|  |  |  |
| --- | --- | --- |
|  | 𝖯∗​(supx|FN​(x)−F​(x)|>η)<δ.{}^{\*}\mathsf{P}\Big(\sup\_{x}|F\_{N}(x)-F(x)|>\eta\Big)<\delta. |  |

Taking Loeb measures (standard parts), L​(𝖯∗)​(supx|FN−F|>η)⩽δL({}^{\*}\mathsf{P})(\sup\_{x}|F\_{N}-F|>\eta)\leqslant\delta. Since
δ>0\delta>0 was arbitrary, L​(𝖯∗)​(supx|FN−F|>η)=0L({}^{\*}\mathsf{P})(\sup\_{x}|F\_{N}-F|>\eta)=0.

Intersecting over a countable sequence η=1/m\eta=1/m for m∈ℕm\in\mathbb{N}, we obtain

|  |  |  |
| --- | --- | --- |
|  | L​(𝖯∗)​(supx|FN​(x)−F​(x)|​ is infinitesimal)=1.L({}^{\*}\mathsf{P})\Big(\sup\_{x}|F\_{N}(x)-F(x)|\text{ is infinitesimal}\Big)=1. |  |

Fix a sample path in this Loeb-probability-one event, and let ε0:=supx|FN​(x)−F​(x)|\varepsilon\_{0}:=\sup\_{x}|F\_{N}(x)-F(x)|.
Then ε0≈0\varepsilon\_{0}\approx 0 is a positive infinitesimal. Moreover, ε0\varepsilon\_{0} is *internal*
(it is the internal supremum of an internal function), so we may use it in transferred statements.

The standard quantile bracketing implication: for any α∈(0,1)\alpha\in(0,1) and ε∈(0,α∧(1−α))\varepsilon\in(0,\alpha\wedge(1-\alpha)),

|  |  |  |  |
| --- | --- | --- | --- |
| (11) |  | supx|Fn​(x)−F​(x)|⩽ε⟹q​(α−ε)⩽qn​(α)⩽q​(α+ε).\sup\_{x}|F\_{n}(x)-F(x)|\leqslant\varepsilon\quad\Longrightarrow\quad q(\alpha-\varepsilon)\leqslant q\_{n}(\alpha)\leqslant q(\alpha+\varepsilon). |  |

This can be expressed using only bounded quantification over ℝ\mathbb{R} and the defining formula for
the lower quantile, so it is a first-order statement in α\alpha, ε\varepsilon, and FnF\_{n}.
By transfer, ([11](https://arxiv.org/html/2602.00784v1#S3.E11 "In Proof. ‣ 3.7. The hyperfinite strong law and Glivenko–Cantelli theorem ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")) holds for all hyperreal α∈(0,1)∗\alpha\in{}^{\*}(0,1) and hyperreal
ε∈(0,α∧(1−α))∗\varepsilon\in{}^{\*}(0,\alpha\wedge(1-\alpha)) with ‖FN−F‖∞⩽ε\|F\_{N}-F\|\_{\infty}\leqslant\varepsilon.

Since ‖FN−F‖∞⩽ε0\|F\_{N}-F\|\_{\infty}\leqslant\varepsilon\_{0} and ε0\varepsilon\_{0} is infinitesimal,
for any hyperreal α∈(0,1)∗\alpha\in{}^{\*}(0,1) with α>ε0\alpha>\varepsilon\_{0} and α<1−ε0\alpha<1-\varepsilon\_{0},

|  |  |  |
| --- | --- | --- |
|  | q​(α−ε0)⩽qN​(α)⩽q​(α+ε0).q(\alpha-\varepsilon\_{0})\leqslant q\_{N}(\alpha)\leqslant q(\alpha+\varepsilon\_{0}). |  |

In particular, qN​(αk)⩽q​(αk+ε0)q\_{N}(\alpha\_{k})\leqslant q(\alpha\_{k}+\varepsilon\_{0}) and qN​(αk)⩾q​(αk−ε0)q\_{N}(\alpha\_{k})\geqslant q(\alpha\_{k}-\varepsilon\_{0}).

*Halos of discontinuities and boundary have Loeb measure zero.*
Since qq is monotone, its set of discontinuity points Disc​(q)⊆(0,1)\mathrm{Disc}(q)\subseteq(0,1) is at most countable.
For each standard α0∈Disc​(q)∪{0,1}\alpha\_{0}\in\mathrm{Disc}(q)\cup\{0,1\}, define the *halo*

|  |  |  |
| --- | --- | --- |
|  | Hα0:={k∈IN:αk≈α0}={k∈IN:|αk−α0|​is infinitesimal}.H\_{\alpha\_{0}}:=\{k\in I\_{N}:\ \alpha\_{k}\approx\alpha\_{0}\}=\{k\in I\_{N}:\ |\alpha\_{k}-\alpha\_{0}|\ \text{is infinitesimal}\}. |  |

We claim L​(μN)​(Hα0)=0L(\mu\_{N})(H\_{\alpha\_{0}})=0. For any standard δ>0\delta>0,

|  |  |  |
| --- | --- | --- |
|  | Hα0⊆{k∈IN:|αk−α0|<δ},H\_{\alpha\_{0}}\subseteq\{k\in I\_{N}:\ |\alpha\_{k}-\alpha\_{0}|<\delta\}, |  |

and the right-hand side is internal with

|  |  |  |
| --- | --- | --- |
|  | μN​({k:|αk−α0|<δ})⩽2​δ.\mu\_{N}(\{k:|\alpha\_{k}-\alpha\_{0}|<\delta\})\leqslant 2\delta. |  |

Taking standard parts, L​(μN)​(Hα0)⩽2​δL(\mu\_{N})(H\_{\alpha\_{0}})\leqslant 2\delta. Since δ>0\delta>0 was arbitrary,
L​(μN)​(Hα0)=0L(\mu\_{N})(H\_{\alpha\_{0}})=0. (Note: Hα0H\_{\alpha\_{0}} has outer Loeb measure zero, hence is Loeb measurable.)

Define

|  |  |  |
| --- | --- | --- |
|  | D:=⋃α0∈Disc​(q)∪{0,1}Hα0.D:=\bigcup\_{\alpha\_{0}\in\mathrm{Disc}(q)\cup\{0,1\}}H\_{\alpha\_{0}}. |  |

Since Disc​(q)∪{0,1}\mathrm{Disc}(q)\cup\{0,1\} is countable and each Hα0H\_{\alpha\_{0}} has Loeb measure 0,
and L​(μN)L(\mu\_{N}) is countably additive, L​(μN)​(D)=0L(\mu\_{N})(D)=0.

*The quantile shadow on G=IN∖DG=I\_{N}\setminus D.*
Take k∉Dk\notin D, so αk\alpha\_{k} is not in the halo of any discontinuity of qq nor in the halo of
{0,1}\{0,1\}. This means t:=st⁡(αk)∈(0,1)∖Disc​(q)t:=\operatorname{st}(\alpha\_{k})\in(0,1)\setminus\mathrm{Disc}(q), hence qq is continuous at tt.

Since qq is continuous at tt and αk≈t\alpha\_{k}\approx t, both αk−ε0≈t\alpha\_{k}-\varepsilon\_{0}\approx t
and αk+ε0≈t\alpha\_{k}+\varepsilon\_{0}\approx t (because ε0\varepsilon\_{0} is infinitesimal). Therefore

|  |  |  |
| --- | --- | --- |
|  | q​(αk−ε0)≈q​(t)≈q​(αk+ε0).q(\alpha\_{k}-\varepsilon\_{0})\approx q(t)\approx q(\alpha\_{k}+\varepsilon\_{0}). |  |

The transferred bracketing gives

|  |  |  |
| --- | --- | --- |
|  | q​(αk−ε0)⩽qN​(αk)=Xk:N⩽q​(αk+ε0),q(\alpha\_{k}-\varepsilon\_{0})\leqslant q\_{N}(\alpha\_{k})=X\_{k:N}\leqslant q(\alpha\_{k}+\varepsilon\_{0}), |  |

hence Xk:N≈q​(t)=q​(st⁡(αk))≈q​(αk)X\_{k:N}\approx q(t)=q(\operatorname{st}(\alpha\_{k}))\approx q(\alpha\_{k}) (using continuity again).
Thus k∈Gk\in G, and we conclude G⊇IN∖DG\supseteq I\_{N}\setminus D, hence L​(μN)​(G)=1L(\mu\_{N})(G)=1.

*Convention for the integral identity.*
We interpret integrals involving internal functions (such as qNq\_{N} and gNg\_{N}) as Loeb integrals
on the hyperfinite grid {αk:k∈IN}\{\alpha\_{k}:k\in I\_{N}\}, so that

|  |  |  |
| --- | --- | --- |
|  | ∫01H​(α)​𝑑α=st⁡(1N​∑k=1NH​(αk))\int\_{0}^{1}H(\alpha)\,d\alpha=\operatorname{st}\Big(\frac{1}{N}\sum\_{k=1}^{N}H(\alpha\_{k})\Big) |  |

whenever HH is SS-integrable on the grid (cf. Remark [3.17](https://arxiv.org/html/2602.00784v1#S3.Thmtheorem17 "Remark 3.17 (A concrete 𝑆-integrability criterion). ‣ 3.6. Hyperfinite integration and the Riemann sum approximation ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")
and Lemma [4.1](https://arxiv.org/html/2602.00784v1#S4.Thmtheorem1 "Lemma 4.1 (Internal liftings and Loeb expectation). ‣ 4.1. The hyperfinite dictionary ‣ 4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")).

*The integral identity via truncation.*
Define the step function gN​(α):=g​(αk)g\_{N}(\alpha):=g(\alpha\_{k}) on ((k−1)/N,k/N]((k-1)/N,k/N]. Then

|  |  |  |
| --- | --- | --- |
|  | 1N​∑k=1Ng​(αk)​Xk:N=∫01gN​(α)​qN​(α)​𝑑α\frac{1}{N}\sum\_{k=1}^{N}g(\alpha\_{k})X\_{k:N}=\int\_{0}^{1}g\_{N}(\alpha)\,q\_{N}(\alpha)\,d\alpha |  |

because qN​(α)=Xk:Nq\_{N}(\alpha)=X\_{k:N} on ((k−1)/N,k/N]((k-1)/N,k/N].

We prove ∫01|qN−q|​𝑑α≈0\int\_{0}^{1}|q\_{N}-q|\,d\alpha\approx 0 directly by truncation (not as a consequence of
the quantile shadow, which only gives pointwise information on a full-Loeb set).
For M>0M>0, define q(M):=max⁡(min⁡(q,M),−M)q^{(M)}:=\max(\min(q,M),-M) and qN(M):=max⁡(min⁡(qN,M),−M)q\_{N}^{(M)}:=\max(\min(q\_{N},M),-M).
Then

|  |  |  |
| --- | --- | --- |
|  | ∫01|qN−q|⩽∫01|qN(M)−q(M)|+∫01|qN−qN(M)|+∫01|q−q(M)|.\int\_{0}^{1}|q\_{N}-q|\leqslant\int\_{0}^{1}|q\_{N}^{(M)}-q^{(M)}|+\int\_{0}^{1}|q\_{N}-q\_{N}^{(M)}|+\int\_{0}^{1}|q-q^{(M)}|. |  |

For the first term: |qN(M)−q(M)|⩽2​M|q\_{N}^{(M)}-q^{(M)}|\leqslant 2M pointwise, and on the full-Loeb set GG,
qN(M)​(αk)≈q(M)​(αk)q\_{N}^{(M)}(\alpha\_{k})\approx q^{(M)}(\alpha\_{k}). By the Loeb dominated convergence theorem
(see [[3](https://arxiv.org/html/2602.00784v1#bib.bib3), Thm. 4.3.6]: for internal functions dominated by an SS-integrable bound,
pointwise near-equality on a Loeb-measure-one set implies the integrals are infinitely close),
∫01|qN(M)−q(M)|≈0\int\_{0}^{1}|q\_{N}^{(M)}-q^{(M)}|\approx 0 for each fixed standard MM.

For the second term: |qN−qN(M)|=|qN|​𝟏|qN|>M|q\_{N}-q\_{N}^{(M)}|=|q\_{N}|\mathbf{1}\_{|q\_{N}|>M}. Since 𝖤​|X1|<∞\mathsf{E}|X\_{1}|<\infty, the
hyperfinite SLLN gives 1N​∑k=1N|Xk|≈𝖤​|X1|<∞\frac{1}{N}\sum\_{k=1}^{N}|X\_{k}|\approx\mathsf{E}|X\_{1}|<\infty. By the standard
integration identity for order statistics, ∫01|qN|​𝑑α=1N​∑k=1N|Xk:N|\int\_{0}^{1}|q\_{N}|\,d\alpha=\frac{1}{N}\sum\_{k=1}^{N}|X\_{k:N}|,
which has finite standard part. Thus ∫01|qN−qN(M)|→0\int\_{0}^{1}|q\_{N}-q\_{N}^{(M)}|\to 0 as M→∞M\to\infty (in the
sense that for any standard δ>0\delta>0, there exists standard MM such that this integral <δ<\delta).

For the third term: ∫01|q−q(M)|→0\int\_{0}^{1}|q-q^{(M)}|\to 0 as M→∞M\to\infty by 𝖤​|X1|<∞\mathsf{E}|X\_{1}|<\infty.

Given δ>0\delta>0, choose MM large enough that the second and third terms are each <δ/3<\delta/3.
Then choose the infinitesimal such that the first term is infinitesimal. Taking standard parts,
st⁡(∫01|qN−q|)⩽2​δ/3<δ\operatorname{st}(\int\_{0}^{1}|q\_{N}-q|)\leqslant 2\delta/3<\delta. Since δ\delta was arbitrary, ∫01|qN−q|≈0\int\_{0}^{1}|q\_{N}-q|\approx 0.

Now we can complete the proof of ([10](https://arxiv.org/html/2602.00784v1#S3.E10 "In Theorem 3.20 (Hyperfinite Glivenko–Cantelli / quantile shadow). ‣ 3.7. The hyperfinite strong law and Glivenko–Cantelli theorem ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")):

|  |  |  |
| --- | --- | --- |
|  | ∫01gN​qN−∫01g​q=∫01gN​(qN−q)+∫01(gN−g)​q.\int\_{0}^{1}g\_{N}q\_{N}-\int\_{0}^{1}gq=\int\_{0}^{1}g\_{N}(q\_{N}-q)+\int\_{0}^{1}(g\_{N}-g)q. |  |

The first term is bounded by ‖g‖∞​∫01|qN−q|≈0\|g\|\_{\infty}\int\_{0}^{1}|q\_{N}-q|\approx 0.
For the second term, fix MM and split q=q(M)+(q−q(M))q=q^{(M)}+(q-q^{(M)}):

|  |  |  |
| --- | --- | --- |
|  | |∫01(gN−g)​q|⩽‖q(M)‖∞​∫01|gN−g|+2​‖g‖∞​∫01|q−q(M)|.\Big|\int\_{0}^{1}(g\_{N}-g)q\Big|\leqslant\|q^{(M)}\|\_{\infty}\int\_{0}^{1}|g\_{N}-g|+2\|g\|\_{\infty}\int\_{0}^{1}|q-q^{(M)}|. |  |

Since gg is Riemann integrable, ∫01|gN−g|≈0\int\_{0}^{1}|g\_{N}-g|\approx 0 (by the hyperfinite Riemann sum
approximation). Let M→∞M\to\infty and use ∫01|q−q(M)|→0\int\_{0}^{1}|q-q^{(M)}|\to 0. Taking standard parts
yields ([10](https://arxiv.org/html/2602.00784v1#S3.E10 "In Theorem 3.20 (Hyperfinite Glivenko–Cantelli / quantile shadow). ‣ 3.7. The hyperfinite strong law and Glivenko–Cantelli theorem ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")).
∎

### 3.8. Overspill and underspill

Two technical principles are frequently used in NSA arguments. We assume throughout that
our non-standard universe is *countably saturated*: every countable collection of
internal sets with the finite intersection property has non-empty intersection.

###### Proposition 3.21 (Overspill).

Let A⊆ℕ∗A\subseteq{}^{\*}\mathbb{N} be internal. If AA contains all standard natural numbers, then
AA contains some infinite hypernatural.

###### Proof.

For each standard m∈ℕm\in\mathbb{N}, define the internal set

|  |  |  |
| --- | --- | --- |
|  | Am:={n∈ℕ∗:n∈A∧n>m}.A\_{m}:=\{n\in{}^{\*}\mathbb{N}:\ n\in A\ \wedge\ n>m\}. |  |

Each AmA\_{m} is internal by the internal definition principle (intersection of AA with
the internal set {n∈ℕ∗:n>m}\{n\in{}^{\*}\mathbb{N}:n>m\}). Each AmA\_{m} is non-empty since m+1∈Am+1\in A
(as AA contains all standard naturals) and m+1>mm+1>m.

The collection {Am:m∈ℕ}\{A\_{m}:m\in\mathbb{N}\} is countable and has the finite intersection property:
for any m1,…,mk∈ℕm\_{1},\dots,m\_{k}\in\mathbb{N}, we have Am1∩⋯∩Amk⊇Amax⁡(m1,…,mk)≠∅A\_{m\_{1}}\cap\cdots\cap A\_{m\_{k}}\supseteq A\_{\max(m\_{1},\dots,m\_{k})}\neq\emptyset.

By countable saturation, ⋂m∈ℕAm≠∅\bigcap\_{m\in\mathbb{N}}A\_{m}\neq\emptyset. Pick HH in this intersection.
Then H∈AH\in A and H>mH>m for every standard m∈ℕm\in\mathbb{N}, hence HH is infinite.
∎

###### Proposition 3.22 (Underspill / underflow).

Let A⊆ℕ∗A\subseteq{}^{\*}\mathbb{N} be internal. If AA contains every infinite hypernatural, then
AA contains some standard natural number.

Equivalently: if A∩ℕ=∅A\cap\mathbb{N}=\emptyset, then there exists an infinite H∈ℕ∗H\in{}^{\*}\mathbb{N} such that
A⊆{H+1,H+2,…}A\subseteq\{H+1,H+2,\dots\}.

###### Proof.

Assume first that AA contains every infinite hypernatural and set B:=ℕ∗∖AB:={}^{\*}\mathbb{N}\setminus A.
Then BB is internal. If B=∅B=\emptyset, then A=ℕ∗A={}^{\*}\mathbb{N} and in particular AA contains every standard natural,
so the conclusion holds. Hence we may assume B≠∅B\neq\emptyset.

By assumption, BB contains no infinite hypernaturals, hence every
element of BB is finite and therefore standard; thus B⊆ℕB\subseteq\mathbb{N}.

Fix an infinite H∈ℕ∗H\in{}^{\*}\mathbb{N}. Then B⊆IH={1,…,H}B\subseteq I\_{H}=\{1,\dots,H\}. Since BB is a non-empty
internal subset of the hyperfinite set IHI\_{H}, transfer of the finite-maximum principle
implies that BB has a maximum element m=max⁡Bm=\max B. This mm cannot be infinite (because BB
contains no infinite hypernaturals), hence m∈ℕm\in\mathbb{N}. Therefore B⊆{1,…,m}B\subseteq\{1,\dots,m\},
so BB is finite. Consequently AA contains all standard naturals >m>m, and in particular
AA contains some standard natural number.

For the equivalent formulation, assume A∩ℕ=∅A\cap\mathbb{N}=\emptyset, so ℕ⊆ℕ∗∖A\mathbb{N}\subseteq{}^{\*}\mathbb{N}\setminus A.
Consider the internal set

|  |  |  |
| --- | --- | --- |
|  | C:={m∈ℕ∗:{1,…,m}⊆ℕ∗∖A}.C:=\{m\in{}^{\*}\mathbb{N}:\ \{1,\dots,m\}\subseteq{}^{\*}\mathbb{N}\setminus A\}. |  |

Then CC contains every standard m∈ℕm\in\mathbb{N}, hence by overspill CC contains an infinite HH.
Thus {1,…,H}⊆ℕ∗∖A\{1,\dots,H\}\subseteq{}^{\*}\mathbb{N}\setminus A, which is equivalent to
A⊆{H+1,H+2,…}A\subseteq\{H+1,H+2,\dots\}.
∎

## 4. Hyperfinite representation of coherent risk measures

We now develop the hyperfinite representation of coherent risk measures, which forms the
foundation for our unified treatment of CRMs and CREs.

### 4.1. The hyperfinite dictionary

Working on the standing Loeb model (IN,ℐNL,L​(μN))(I\_{N},\mathscr{I}\_{N}^{L},L(\mu\_{N})) from
Notation [3.2](https://arxiv.org/html/2602.00784v1#S3.Thmtheorem2 "Notation 3.2 (Standing Loeb model). ‣ 3.1. Standing conventions and the Loeb model ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), we may regard elements of L∞L^{\infty} as essentially bounded
Loeb-measurable functions on INI\_{N}. The Loeb integration theory provides a canonical
internal representation of such functions.

###### Lemma 4.1 (Internal liftings and Loeb expectation).

Let X:IN→ℝX:I\_{N}\to\mathbb{R} be Loeb measurable and essentially bounded. Then there exists a bounded
internal function X~:IN→ℝ∗\tilde{X}:I\_{N}\to{}^{\*}\mathbb{R} such that X=st⁡(X~)X=\operatorname{st}(\tilde{X}) L​(μN)L(\mu\_{N})-almost surely, and

|  |  |  |
| --- | --- | --- |
|  | ∫INX​𝑑L​(μN)=st⁡(1N​∑k=1NX~​(k)).\int\_{I\_{N}}X\,dL(\mu\_{N})=\operatorname{st}\Big(\frac{1}{N}\sum\_{k=1}^{N}\tilde{X}(k)\Big). |  |

If YY is Loeb integrable and Y~\tilde{Y} is an SS-integrable internal lifting, then

|  |  |  |
| --- | --- | --- |
|  | ∫INY​𝑑L​(μN)=st⁡(1N​∑k=1NY~​(k))\int\_{I\_{N}}Y\,dL(\mu\_{N})=\operatorname{st}\Big(\frac{1}{N}\sum\_{k=1}^{N}\tilde{Y}(k)\Big) |  |

as well.

###### Proof (reference).

See [[10](https://arxiv.org/html/2602.00784v1#bib.bib10), Chs. 4–5] for liftings of Loeb-measurable functions and the identification
of Loeb integrals with standard parts of internal counting integrals.
∎

The following lemma ensures that uniform integrability passes to the non-standard extension,
which is crucial for making our hyperfinite representation *internal*.

###### Lemma 4.2 (Uniform integrability implies SS-integrability of 𝒵∗{}^{\*}\mathcal{Z}).

Let 𝒵⊂L+1\mathcal{Z}\subset L^{1}\_{+} be uniformly integrable with supZ∈𝒵𝖤​[Z]⩽C<∞\sup\_{Z\in\mathcal{Z}}\mathsf{E}[Z]\leqslant C<\infty.
Then for every Z∈𝒵∗Z\in{}^{\*}\mathcal{Z}, the internal function Z:IN→[0,∞)∗Z:I\_{N}\to{}^{\*}[0,\infty) is SS-integrable
on the Loeb space (IN,ℐNL,L​(μN))(I\_{N},\mathscr{I}\_{N}^{L},L(\mu\_{N})), with

|  |  |  |
| --- | --- | --- |
|  | ∫Z​𝑑L​(μN)=st⁡(1N​∑k=1NZ​(k)).\int Z\,dL(\mu\_{N})=\operatorname{st}\Big(\frac{1}{N}\sum\_{k=1}^{N}Z(k)\Big). |  |

In particular, if 𝖤​[Z]=1\mathsf{E}[Z]=1 for all Z∈𝒵Z\in\mathcal{Z}, then 1N​∑k=1NZ​(k)≈1\frac{1}{N}\sum\_{k=1}^{N}Z(k)\approx 1
for all Z∈𝒵∗Z\in{}^{\*}\mathcal{Z}.

Moreover, if X∈L∞X\in L^{\infty} has a bounded internal lifting X~\tilde{X} with |X~|⩽M|\tilde{X}|\leqslant M,
then for any Z∈𝒵∗Z\in{}^{\*}\mathcal{Z} the product X~⋅Z\tilde{X}\cdot Z is SS-integrable and

|  |  |  |
| --- | --- | --- |
|  | 𝖤​[−X​Z]=st⁡(1N​∑k=1N(−X~​(k))​Z​(k)).\mathsf{E}[-XZ]=\operatorname{st}\Big(\frac{1}{N}\sum\_{k=1}^{N}(-\tilde{X}(k))\,Z(k)\Big). |  |

###### Proof.

Uniform integrability of 𝒵\mathcal{Z} means: for every ε>0\varepsilon>0 there exists K>0K>0 such that
supZ∈𝒵𝖤​[Z​𝟏{Z>K}]<ε\sup\_{Z\in\mathcal{Z}}\mathsf{E}[Z\mathbf{1}\_{\{Z>K\}}]<\varepsilon. This is a first-order statement:

|  |  |  |
| --- | --- | --- |
|  | ∀ε∈ℚ>0∃K∈ℚ>0∀Z∈𝒵:𝖤[Z𝟏{Z>K}]<ε.\forall\varepsilon\in\mathbb{Q}\_{>0}\ \exists K\in\mathbb{Q}\_{>0}\ \forall Z\in\mathcal{Z}:\quad\mathsf{E}[Z\mathbf{1}\_{\{Z>K\}}]<\varepsilon. |  |

By transfer, for every standard ε>0\varepsilon>0 there exists standard K>0K>0 such that
𝖤∗​[Z​𝟏{Z>K}]<ε{}^{\*}\mathsf{E}[Z\mathbf{1}\_{\{Z>K\}}]<\varepsilon for all Z∈𝒵∗Z\in{}^{\*}\mathcal{Z}.

In terms of the hyperfinite counting measure, this says

|  |  |  |
| --- | --- | --- |
|  | 1N​∑k:Z​(k)>KZ​(k)<ε\frac{1}{N}\sum\_{k:Z(k)>K}Z(k)<\varepsilon |  |

for all Z∈𝒵∗Z\in{}^{\*}\mathcal{Z}. This is exactly the criterion for SS-integrability: the “tail”
of the internal sum is uniformly small for large standard KK. By the standard characterisation
of SS-integrability (see [[3](https://arxiv.org/html/2602.00784v1#bib.bib3), Prop. 4.3.5]), each Z∈𝒵∗Z\in{}^{\*}\mathcal{Z} is SS-integrable.

The Loeb integral identity follows from the definition of SS-integrability: if ZZ is SS-integrable,
then ∫Z​𝑑L​(μN)=st⁡(1N​∑k=1NZ​(k))\int Z\,dL(\mu\_{N})=\operatorname{st}(\frac{1}{N}\sum\_{k=1}^{N}Z(k)).

For the constraint 𝖤​[Z]=1\mathsf{E}[Z]=1, transfer gives ∫Z​𝑑L​(μN)=1\int Z\,dL(\mu\_{N})=1 for all Z∈𝒵∗Z\in{}^{\*}\mathcal{Z}.
By the Loeb integral identity, st⁡(1N​∑k=1NZ​(k))=1\operatorname{st}(\frac{1}{N}\sum\_{k=1}^{N}Z(k))=1, hence
1N​∑k=1NZ​(k)≈1\frac{1}{N}\sum\_{k=1}^{N}Z(k)\approx 1 for all Z∈𝒵∗Z\in{}^{\*}\mathcal{Z}.

For the product: since |X~|⩽M|\tilde{X}|\leqslant M and Z⩾0Z\geqslant 0 is SS-integrable, |X~⋅Z|⩽M⋅Z|\tilde{X}\cdot Z|\leqslant M\cdot Z
is dominated by an SS-integrable function, hence X~⋅Z\tilde{X}\cdot Z is SS-integrable.
∎

### 4.2. Hyperfinite robust representation

We can now state and prove the hyperfinite version of the robust representation theorem.
The key observation is that standard attainment on a compact set immediately gives us an
internal maximiser via the non-standard extension of the standard maximiser. By
Lemma [4.2](https://arxiv.org/html/2602.00784v1#S4.Thmtheorem2 "Lemma 4.2 (Uniform integrability implies 𝑆-integrability of {^∗}𝒵). ‣ 4.1. The hyperfinite dictionary ‣ 4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), elements of 𝒵∗{}^{\*}\mathcal{Z} are automatically SS-integrable,
so we can work directly with 𝒵∗{}^{\*}\mathcal{Z} as an *internal* set.

###### Theorem 4.3 (Hyperfinite robust representation on L∞L^{\infty}).

Let (Ω,𝒢,𝖯)(\Omega,\mathscr{G},\mathsf{P}) be atomless and separable, and let ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R} be a
coherent risk measure with the Fatou property. Assume it admits a robust representation of the form

|  |  |  |
| --- | --- | --- |
|  | ρ​(X)=supZ∈𝒵𝖤​[−X​Z],𝒵⊂L+1,𝖤​[Z]=1,\rho(X)=\sup\_{Z\in\mathcal{Z}}\mathsf{E}[-XZ],\qquad\mathcal{Z}\subset L^{1}\_{+},\ \mathsf{E}[Z]=1, |  |

where 𝒵\mathcal{Z} is compact in σ​(L1,L∞)\sigma(L^{1},L^{\infty}) (equivalently, uniformly integrable and
σ​(L1,L∞)\sigma(L^{1},L^{\infty})-closed).

We may (and do) identify the underlying atomless probability space with the standing Loeb model
(IN,ℐNL,L​(μN))(I\_{N},\mathscr{I}\_{N}^{L},L(\mu\_{N})) (Notation [3.2](https://arxiv.org/html/2602.00784v1#S3.Thmtheorem2 "Notation 3.2 (Standing Loeb model). ‣ 3.1. Standing conventions and the Loeb model ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")), and let X~\tilde{X} be a bounded
internal lifting of XX as in Lemma [4.1](https://arxiv.org/html/2602.00784v1#S4.Thmtheorem1 "Lemma 4.1 (Internal liftings and Loeb expectation). ‣ 4.1. The hyperfinite dictionary ‣ 4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"). Then

|  |  |  |
| --- | --- | --- |
|  | ρ​(X)=st⁡(supZ∈𝒵∗1N​∑k=1N(−X~​(k))​Z​(k)),X∈L∞,\rho(X)=\operatorname{st}\Big(\sup\_{Z\in{}^{\*}\mathcal{Z}}\frac{1}{N}\sum\_{k=1}^{N}(-\tilde{X}(k))\,Z(k)\Big),\qquad X\in L^{\infty}, |  |

where 𝒵∗{}^{\*}\mathcal{Z} is the internal non-standard extension of 𝒵\mathcal{Z}, and elements
Z∈𝒵∗Z\in{}^{\*}\mathcal{Z} are SS-integrable by Lemma [4.2](https://arxiv.org/html/2602.00784v1#S4.Thmtheorem2 "Lemma 4.2 (Uniform integrability implies 𝑆-integrability of {^∗}𝒵). ‣ 4.1. The hyperfinite dictionary ‣ 4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics").
The supremum over 𝒵∗{}^{\*}\mathcal{Z} is *internal*, and is attained by some Z♯∈𝒵∗Z^{\sharp}\in{}^{\*}\mathcal{Z}.

Equivalently, defining weight vectors a=Ψ​(Z)a=\Psi(Z) via the normalisation

|  |  |  |
| --- | --- | --- |
|  | Ψ​(Z)k:=Z​(k)/∑j=1NZ​(j),\Psi(Z)\_{k}:=Z(k)/\sum\_{j=1}^{N}Z(j), |  |

we have ∑kak=1\sum\_{k}a\_{k}=1 exactly and

|  |  |  |
| --- | --- | --- |
|  | ρ​(X)=st⁡(supa∈𝒜N∑k=1Nak​(−X~​(k))),\rho(X)=\operatorname{st}\Big(\sup\_{a\in\mathcal{A}\_{N}}\sum\_{k=1}^{N}a\_{k}\,(-\tilde{X}(k))\Big), |  |

where 𝒜N:={Ψ​(Z):Z∈𝒵∗}\mathcal{A}\_{N}:=\{\Psi(Z):Z\in{}^{\*}\mathcal{Z}\} is *internal* (as the image of
an internal set under an internal map). For the maximiser Z♯∈𝒵∗Z^{\sharp}\in{}^{\*}\mathcal{Z},
Ψ​(Z♯)\Psi(Z^{\sharp}) achieves a value infinitely close to the supremum over 𝒜N\mathcal{A}\_{N}.

###### Proof.

Internality of 𝒵∗{}^{\*}\mathcal{Z}.
Fix once and for all a measurable representative for each element of 𝒵⊂L+1\mathcal{Z}\subset L^{1}\_{+}
(possible since 𝒵\mathcal{Z} is a set, not a quotient).
With this choice, 𝒵∗{}^{\*}\mathcal{Z} may be viewed as an internal family of internal functions IN→[0,∞)∗I\_{N}\to{}^{\*}[0,\infty).

By Lemma [4.2](https://arxiv.org/html/2602.00784v1#S4.Thmtheorem2 "Lemma 4.2 (Uniform integrability implies 𝑆-integrability of {^∗}𝒵). ‣ 4.1. The hyperfinite dictionary ‣ 4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"),
since 𝒵\mathcal{Z} is uniformly integrable, every Z∈𝒵∗Z\in{}^{\*}\mathcal{Z} is automatically SS-integrable.
Crucially, 𝒵∗{}^{\*}\mathcal{Z} is an *internal* set (as the non-standard extension of a standard set),
so the supremum supZ∈𝒵∗(⋯)\sup\_{Z\in{}^{\*}\mathcal{Z}}(\cdots) is internal.

Fix X∈L∞X\in L^{\infty} and define the functional
fX:𝒵→ℝf\_{X}:\mathcal{Z}\to\mathbb{R} by fX​(Z):=𝖤​[−X​Z]f\_{X}(Z):=\mathsf{E}[-XZ]. This is continuous in the σ​(L1,L∞)\sigma(L^{1},L^{\infty}) topology
on 𝒵\mathcal{Z} (by definition of that topology). Since 𝒵\mathcal{Z} is
σ​(L1,L∞)\sigma(L^{1},L^{\infty})-compact, there exists a standard maximiser Z∗∈𝒵Z^{\*}\in\mathcal{Z} such that
fX​(Z∗)=ρ​(X)f\_{X}(Z^{\*})=\rho(X).

The non-standard extension Z∗∗∈𝒵∗{}^{\*}Z^{\*}\in{}^{\*}\mathcal{Z} (viewing Z∗Z^{\*} as an element of the
standard universe) satisfies fX∗​(Z∗∗)=ρ∗​(X)=ρ​(X){}^{\*}f\_{X}({}^{\*}Z^{\*})={}^{\*}\rho(X)=\rho(X) by transfer. Set Z♯:=Z∗∗Z^{\sharp}:={}^{\*}Z^{\*}.
Alternatively, one may transfer the existence statement directly: the first-order statement
“∃Z∈𝒵​(fX​(Z)=ρ​(X))\exists Z\in\mathcal{Z}\ (f\_{X}(Z)=\rho(X))” holds, hence by transfer there exists
Z♯∈𝒵∗Z^{\sharp}\in{}^{\*}\mathcal{Z} such that fX∗​(Z♯)=ρ​(X){}^{\*}f\_{X}(Z^{\sharp})=\rho(X).

We may (and do) identify the underlying atomless probability space with the standing Loeb model
(IN,ℐNL,L​(μN))(I\_{N},\mathscr{I}\_{N}^{L},L(\mu\_{N})), and let X~:IN→ℝ∗\tilde{X}:I\_{N}\to{}^{\*}\mathbb{R} be a bounded internal
lifting of XX as in Lemma [4.1](https://arxiv.org/html/2602.00784v1#S4.Thmtheorem1 "Lemma 4.1 (Internal liftings and Loeb expectation). ‣ 4.1. The hyperfinite dictionary ‣ 4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"). By Lemma [4.2](https://arxiv.org/html/2602.00784v1#S4.Thmtheorem2 "Lemma 4.2 (Uniform integrability implies 𝑆-integrability of {^∗}𝒵). ‣ 4.1. The hyperfinite dictionary ‣ 4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), since Z♯∈𝒵∗Z^{\sharp}\in{}^{\*}\mathcal{Z}
is SS-integrable and X~\tilde{X} is bounded, the product (−X~)⋅Z♯(-\tilde{X})\cdot Z^{\sharp} is SS-integrable.
Applying Lemma [4.2](https://arxiv.org/html/2602.00784v1#S4.Thmtheorem2 "Lemma 4.2 (Uniform integrability implies 𝑆-integrability of {^∗}𝒵). ‣ 4.1. The hyperfinite dictionary ‣ 4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") yields

|  |  |  |  |
| --- | --- | --- | --- |
| (12) |  | ρ​(X)=fX∗​(Z♯)=st⁡(1N​∑k=1N(−X~​(k))​Z♯​(k)).\rho(X)={}^{\*}f\_{X}(Z^{\sharp})=\operatorname{st}\Big(\frac{1}{N}\sum\_{k=1}^{N}(-\tilde{X}(k))\,Z^{\sharp}(k)\Big). |  |

Moreover, by transfer of “fX​(Z)⩽ρ​(X)f\_{X}(Z)\leqslant\rho(X) for all Z∈𝒵Z\in\mathcal{Z}”, we have
fX∗​(Z)⩽ρ​(X){}^{\*}f\_{X}(Z)\leqslant\rho(X) for all Z∈𝒵∗Z\in{}^{\*}\mathcal{Z}. Since the supremum over the internal
set 𝒵∗{}^{\*}\mathcal{Z} is internal, we obtain

|  |  |  |
| --- | --- | --- |
|  | ρ​(X)=st⁡(supZ∈𝒵∗1N​∑k=1N(−X~​(k))​Z​(k)).\rho(X)=\operatorname{st}\Big(\sup\_{Z\in{}^{\*}\mathcal{Z}}\frac{1}{N}\sum\_{k=1}^{N}(-\tilde{X}(k))\,Z(k)\Big). |  |

For the normalised weight formulation, define

|  |  |  |
| --- | --- | --- |
|  | H​(Z):=1N​∑j=1NZ​(j),Ψ​(Z)k:=Z​(k)∑j=1NZ​(j),k=1,…,N.H(Z):=\frac{1}{N}\sum\_{j=1}^{N}Z(j),\qquad\Psi(Z)\_{k}:=\frac{Z(k)}{\sum\_{j=1}^{N}Z(j)},\quad k=1,\dots,N. |  |

Then ∑k=1NΨ​(Z)k=1\sum\_{k=1}^{N}\Psi(Z)\_{k}=1 exactly (this is an algebraic identity).

For Z∈𝒵∗Z\in{}^{\*}\mathcal{Z}, by Lemma [4.2](https://arxiv.org/html/2602.00784v1#S4.Thmtheorem2 "Lemma 4.2 (Uniform integrability implies 𝑆-integrability of {^∗}𝒵). ‣ 4.1. The hyperfinite dictionary ‣ 4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") we have
1N​∑k=1NZ​(k)≈1\frac{1}{N}\sum\_{k=1}^{N}Z(k)\approx 1, i.e., H​(Z)≈1H(Z)\approx 1.
Since Z⩾0Z\geqslant 0 and H​(Z)≈1>0H(Z)\approx 1>0, Ψ​(Z)\Psi(Z) is well-defined and internal.
The set 𝒜N:={Ψ​(Z):Z∈𝒵∗}\mathcal{A}\_{N}:=\{\Psi(Z):Z\in{}^{\*}\mathcal{Z}\} is internal (as the image of
an internal set under an internal map).

The connection between the two formulations is:

|  |  |  |
| --- | --- | --- |
|  | 1N​∑k=1N(−X~​(k))​Z​(k)=H​(Z)​∑k=1NΨ​(Z)k​(−X~​(k)).\frac{1}{N}\sum\_{k=1}^{N}(-\tilde{X}(k))\,Z(k)=H(Z)\sum\_{k=1}^{N}\Psi(Z)\_{k}\,(-\tilde{X}(k)). |  |

Since |X~|⩽M|\tilde{X}|\leqslant M for some standard MM, the sum ∑k=1NΨ​(Z)k​(−X~​(k))\sum\_{k=1}^{N}\Psi(Z)\_{k}(-\tilde{X}(k))
is bounded (in absolute value by MM, since ∑kΨ​(Z)k=1\sum\_{k}\Psi(Z)\_{k}=1). Since H​(Z)≈1H(Z)\approx 1,

|  |  |  |
| --- | --- | --- |
|  | st⁡(1N​∑k=1N(−X~​(k))​Z​(k))=st⁡(∑k=1NΨ​(Z)k​(−X~​(k))).\operatorname{st}\Big(\frac{1}{N}\sum\_{k=1}^{N}(-\tilde{X}(k))\,Z(k)\Big)=\operatorname{st}\Big(\sum\_{k=1}^{N}\Psi(Z)\_{k}\,(-\tilde{X}(k))\Big). |  |

The weight-vector supremum satisfies

|  |  |  |
| --- | --- | --- |
|  | st⁡(supa∈𝒜N∑k=1Nak​(−X~​(k)))=st⁡(supZ∈𝒵∗1N​∑k=1N(−X~​(k))​Z​(k)).\operatorname{st}\Big(\sup\_{a\in\mathcal{A}\_{N}}\sum\_{k=1}^{N}a\_{k}\,(-\tilde{X}(k))\Big)=\operatorname{st}\Big(\sup\_{Z\in{}^{\*}\mathcal{Z}}\frac{1}{N}\sum\_{k=1}^{N}(-\tilde{X}(k))\,Z(k)\Big). |  |

Indeed, for Z∈𝒵∗Z\in{}^{\*}\mathcal{Z} we have

|  |  |  |
| --- | --- | --- |
|  | ∑k=1NΨ​(Z)​(k)​(−X~​(k))=1∑j=1NZ​(j)​∑k=1N(−X~​(k))​Z​(k)=1H​(Z)⋅1N​∑k=1N(−X~​(k))​Z​(k).\sum\_{k=1}^{N}\Psi(Z)(k)(-\tilde{X}(k))=\frac{1}{\sum\_{j=1}^{N}Z(j)}\sum\_{k=1}^{N}(-\tilde{X}(k))Z(k)=\frac{1}{H(Z)}\cdot\frac{1}{N}\sum\_{k=1}^{N}(-\tilde{X}(k))Z(k). |  |

Since 𝒵∗{}^{\*}\mathcal{Z} is internal and H​(Z)≈1H(Z)\approx 1 for every Z∈𝒵∗Z\in{}^{\*}\mathcal{Z}, the internal set
{|1/H​(Z)−1|:Z∈𝒵∗}\{|1/H(Z)-1|:Z\in{}^{\*}\mathcal{Z}\} consists only of infinitesimals, hence its supremum is infinitesimal.
Moreover,

|  |  |  |
| --- | --- | --- |
|  | |1N​∑k=1N(−X~​(k))​Z​(k)|⩽‖X~‖∞​H​(Z),\left|\frac{1}{N}\sum\_{k=1}^{N}(-\tilde{X}(k))Z(k)\right|\leqslant\|\tilde{X}\|\_{\infty}\,H(Z), |  |

so taking internal suprema preserves the standard part. Therefore the two internal suprema have the same standard part.

The attainment statement follows from transfer: the standard maximiser Z∗∈𝒵Z^{\*}\in\mathcal{Z}
extends to Z♯=Z∗∗∈𝒵∗Z^{\sharp}={}^{\*}Z^{\*}\in{}^{\*}\mathcal{Z}, and a♯:=Ψ​(Z♯)a^{\sharp}:=\Psi(Z^{\sharp}) achieves
a value infinitely close to the supremum over 𝒜N\mathcal{A}\_{N}.
∎

###### Remark 4.4 (Why compactness appears).

The passage from a standard supremum supQ∈𝒬𝖤Q​[−X]\sup\_{Q\in\mathcal{Q}}\mathsf{E}\_{Q}[-X] to an internal
maximum over 𝒬∗{}^{\*}\mathcal{Q} uses the NSA characterisation of compactness. In the
absence of compactness one still obtains ε\varepsilon-maximisers in 𝒬∗{}^{\*}\mathcal{Q}
and hence a hyperfinite representation *up to infinitesimals*, uniformly over
XX with ‖X‖∞⩽1\|X\|\_{\infty}\leqslant 1; compactness is the natural condition ensuring exact
shadowing by standard parts.

###### Remark 4.5 (The hyperfinite dictionary).

Theorem [4.3](https://arxiv.org/html/2602.00784v1#S4.Thmtheorem3 "Theorem 4.3 (Hyperfinite robust representation on 𝐿^∞). ‣ 4.2. Hyperfinite robust representation ‣ 4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") establishes the central dictionary of our approach:

| CRM (population) | Hyperfinite representation |
| --- | --- |
| Probability measure QQ | Weight vector a∈([0,1]∗)Na\in({}^{\*}[0,1])^{N}, ∑ak=1\sum a\_{k}=1 |
| Expectation 𝖤Q​[−X]\mathsf{E}\_{Q}[-X] | Hyperfinite sum ∑k=1Nak​(−xk)\sum\_{k=1}^{N}a\_{k}(-x\_{k}) |
| Supremum over 𝒬\mathcal{Q} | Internal supremum over 𝒜N\mathcal{A}\_{N} |
| Risk measure ρ​(X)\rho(X) | Standard part of hyperfinite support function |

### 4.3. From hyperfinite representation to CRE representation

The finite-sample representation theorems for CREs now emerge as special cases.

###### Hyperfinite proof of Theorem [2.9](https://arxiv.org/html/2602.00784v1#S2.Thmtheorem9 "Theorem 2.9 (Robust representation of CREs [1, Theorem 4.1]). ‣ 2.3. Coherent risk estimators ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics").

Fix n∈ℕn\in\mathbb{N} and consider the finite probability space
(Ω^,𝒢^,𝖯^)(\hat{\Omega},\hat{\mathscr{G}},\hat{\mathsf{P}}) with Ω^={ω1,…,ωn}\hat{\Omega}=\{\omega\_{1},\ldots,\omega\_{n}\},
𝒢^=2Ω^\hat{\mathscr{G}}=2^{\hat{\Omega}}, and 𝖯^​({ωi})=1/n\hat{\mathsf{P}}(\{\omega\_{i}\})=1/n.

A CRE ρ^n:ℝn→ℝ\hat{\rho}\_{n}:\mathbb{R}^{n}\to\mathbb{R} induces a CRM ρ\rho on this finite space by
ρ​(X):=ρ^n​(x)\rho(X):=\hat{\rho}\_{n}(x) where xi=X​(ωi)x\_{i}=X(\omega\_{i}). The axioms (E1)–(E4) translate
directly to (R1)–(R4).

By finite-dimensional convex duality (the finite space version of the robust representation,
which does not require atomlessness), there exists a convex set 𝒬\mathcal{Q} of probability measures
on Ω^\hat{\Omega} such that

|  |  |  |
| --- | --- | --- |
|  | ρ​(X)=supQ∈𝒬𝖤Q​[−X].\rho(X)=\sup\_{Q\in\mathcal{Q}}\mathsf{E}\_{Q}[-X]. |  |

Each QQ on Ω^\hat{\Omega} corresponds to a weight vector a∈Δna\in\Delta\_{n} via
ai=Q​({ωi})a\_{i}=Q(\{\omega\_{i}\}), in which case 𝖤Q​[−X]=∑i=1nai​(−xi)=⟨a,−x⟩\mathsf{E}\_{Q}[-X]=\sum\_{i=1}^{n}a\_{i}(-x\_{i})=\langle a,-x\rangle. Setting Mρ^n∗:={a​(Q):Q∈𝒬}M^{\*}\_{\hat{\rho}\_{n}}:=\{a(Q):Q\in\mathcal{Q}\}, we obtain

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(x)=supa∈Mρ^n∗⟨a,−x⟩.\hat{\rho}\_{n}(x)=\sup\_{a\in M^{\*}\_{\hat{\rho}\_{n}}}\langle a,-x\rangle. |  |

Convexity of Mρ^n∗M^{\*}\_{\hat{\rho}\_{n}} follows from convexity of 𝒬\mathcal{Q}, and attainment
follows from compactness of the simplex Δn\Delta\_{n}.
∎

For the law-invariant representation, we need the rearrangement inequality.

###### Lemma 4.6 (Rearrangement inequality [[12](https://arxiv.org/html/2602.00784v1#bib.bib12), Theorem 368]).

Let u,v∈ℝnu,v\in\mathbb{R}^{n} with decreasing rearrangements u↓u^{\downarrow} and v↓v^{\downarrow}. Then
for any permutation σ\sigma,

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nui​vσ​(i)⩽∑i=1nui↓​vi↓,\sum\_{i=1}^{n}u\_{i}v\_{\sigma(i)}\leqslant\sum\_{i=1}^{n}u^{\downarrow}\_{i}v^{\downarrow}\_{i}, |  |

with equality when uu and vv are both sorted in the same order (both increasing or both decreasing).

We may now prove Theorem [2.10](https://arxiv.org/html/2602.00784v1#S2.Thmtheorem10 "Theorem 2.10 (Law-invariant CREs [1, Theorem 4.2]). ‣ 2.3. Coherent risk estimators ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics").

###### Proof of Theorem [2.10](https://arxiv.org/html/2602.00784v1#S2.Thmtheorem10 "Theorem 2.10 (Law-invariant CREs [1, Theorem 4.2]). ‣ 2.3. Coherent risk estimators ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics").

By Theorem [2.9](https://arxiv.org/html/2602.00784v1#S2.Thmtheorem9 "Theorem 2.9 (Robust representation of CREs [1, Theorem 4.1]). ‣ 2.3. Coherent risk estimators ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") there exists a non-empty convex Mρ^n∗⊆ΔnM^{\*}\_{\hat{\rho}\_{n}}\subseteq\Delta\_{n}
such that ρ^n​(x)=supa∈Mρ^n∗⟨a,−x⟩\hat{\rho}\_{n}(x)=\sup\_{a\in M^{\*}\_{\hat{\rho}\_{n}}}\langle a,-x\rangle.

Define the *symmetrised* set

|  |  |  |
| --- | --- | --- |
|  | M~:=conv⁡{π​(a):a∈Mρ^n∗,π​a permutation of ​{1,…,n}}⊆Δn,\widetilde{M}:=\operatorname{conv}\bigl\{\pi(a):\ a\in M^{\*}\_{\hat{\rho}\_{n}},\ \pi\ \text{a permutation of }\{1,\dots,n\}\bigr\}\subseteq\Delta\_{n}, |  |

where π​(a)\pi(a) denotes the permuted vector (aπ​(1),…,aπ​(n))(a\_{\pi(1)},\dots,a\_{\pi(n)}).
Then M~\widetilde{M} is convex and non-empty. Moreover, law invariance implies that for every xx,

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(x)=ρ^n​(π​(x))=supa∈Mρ^n∗⟨a,−π​(x)⟩=supa∈Mρ^n∗⟨π−1​(a),−x⟩,\hat{\rho}\_{n}(x)=\hat{\rho}\_{n}(\pi(x))=\sup\_{a\in M^{\*}\_{\hat{\rho}\_{n}}}\langle a,-\pi(x)\rangle=\sup\_{a\in M^{\*}\_{\hat{\rho}\_{n}}}\langle\pi^{-1}(a),-x\rangle, |  |

and taking the supremum over all permutations shows

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(x)=supb∈M~⟨b,−x⟩.\hat{\rho}\_{n}(x)=\sup\_{b\in\widetilde{M}}\langle b,-x\rangle. |  |

Now for each b∈Δnb\in\Delta\_{n} let b↓∈Δn↓b^{\downarrow}\in\Delta\_{n}^{\downarrow} be its decreasing rearrangement.
Note that −s​(x)-s(x) is the *decreasing* rearrangement of −x-x (since s​(x)=(x1:n,…,xn:n)s(x)=(x\_{1:n},\ldots,x\_{n:n})
is increasing). By the rearrangement inequality (Lemma [4.6](https://arxiv.org/html/2602.00784v1#S4.Thmtheorem6 "Lemma 4.6 (Rearrangement inequality [12, Theorem 368]). ‣ 4.3. From hyperfinite representation to CRE representation ‣ 4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")) applied to u=bu=b and v=−xv=-x,

|  |  |  |
| --- | --- | --- |
|  | ⟨b,−x⟩=∑i=1nbi​(−xi)⩽∑i=1nbi↓​(−x)i↓=∑i=1nbi↓​(−xi:n)=⟨b↓,−s​(x)⟩.\langle b,-x\rangle=\sum\_{i=1}^{n}b\_{i}(-x\_{i})\leqslant\sum\_{i=1}^{n}b^{\downarrow}\_{i}(-x)^{\downarrow}\_{i}=\sum\_{i=1}^{n}b^{\downarrow}\_{i}(-x\_{i:n})=\langle b^{\downarrow},-s(x)\rangle. |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(x)=supb∈M~⟨b,−x⟩⩽supb∈M~⟨b↓,−s​(x)⟩.\hat{\rho}\_{n}(x)=\sup\_{b\in\widetilde{M}}\langle b,-x\rangle\leqslant\sup\_{b\in\widetilde{M}}\langle b^{\downarrow},-s(x)\rangle. |  |

Conversely, for any b∈M~b\in\widetilde{M}, since M~\widetilde{M} is permutation invariant, we have
b↓∈M~b^{\downarrow}\in\widetilde{M}. Moreover, s​(x)s(x) is a permutation of xx, so there exists a
permutation σ\sigma with s​(x)=σ​(x)s(x)=\sigma(x). Then

|  |  |  |
| --- | --- | --- |
|  | ⟨b↓,−s​(x)⟩=⟨σ−1​(b↓),−x⟩⩽supb′∈M~⟨b′,−x⟩=ρ^n​(x),\langle b^{\downarrow},-s(x)\rangle=\langle\sigma^{-1}(b^{\downarrow}),-x\rangle\leqslant\sup\_{b^{\prime}\in\widetilde{M}}\langle b^{\prime},-x\rangle=\hat{\rho}\_{n}(x), |  |

where we used σ−1​(b↓)∈M~\sigma^{-1}(b^{\downarrow})\in\widetilde{M} by permutation invariance.
Hence supb∈M~⟨b↓,−s​(x)⟩⩽ρ^n​(x)\sup\_{b\in\widetilde{M}}\langle b^{\downarrow},-s(x)\rangle\leqslant\hat{\rho}\_{n}(x), establishing equality.

Therefore, with

|  |  |  |
| --- | --- | --- |
|  | Mρ^ns:=cl⁡conv⁡{b↓:b∈M~}⊆Δn↓,M^{s}\_{\hat{\rho}\_{n}}:=\operatorname{cl}\operatorname{conv}\{b^{\downarrow}:\ b\in\widetilde{M}\}\subseteq\Delta\_{n}^{\downarrow}, |  |

we obtain

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(x)=supa∈Mρ^ns∑i=1nai​(−xi:n).\hat{\rho}\_{n}(x)=\sup\_{a\in M^{s}\_{\hat{\rho}\_{n}}}\sum\_{i=1}^{n}a\_{i}(-x\_{i:n}). |  |

Attainment follows because Mρ^nsM^{s}\_{\hat{\rho}\_{n}} is a closed subset of the compact simplex Δn↓\Delta\_{n}^{\downarrow},
and the objective is continuous and linear in aa.
∎

###### Proof of Theorem [2.11](https://arxiv.org/html/2602.00784v1#S2.Thmtheorem11 "Theorem 2.11 (Comonotonic law-invariant CREs [1, Theorem 4.10]). ‣ 2.3. Coherent risk estimators ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") (finite Choquet / distortion representation).

Let ρ^n\hat{\rho}\_{n} be coherent, law-invariant, and comonotonic additive. By Theorem [2.10](https://arxiv.org/html/2602.00784v1#S2.Thmtheorem10 "Theorem 2.10 (Law-invariant CREs [1, Theorem 4.2]). ‣ 2.3. Coherent risk estimators ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")
there exists a non-empty convex set Mρ^ns⊆Δn↓M^{s}\_{\hat{\rho}\_{n}}\subseteq\Delta\_{n}^{\downarrow} such that

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(x)=supa∈Mρ^ns∑i=1nai​(−xi:n).\hat{\rho}\_{n}(x)=\sup\_{a\in M^{s}\_{\hat{\rho}\_{n}}}\sum\_{i=1}^{n}a\_{i}(-x\_{i:n}). |  |

A standard representation theorem for comonotonic additive, monotone functionals on a finite
lattice states that such a functional is a Choquet integral with respect to a unique capacity
(called the *core* of the functional); see, e.g., [[9](https://arxiv.org/html/2602.00784v1#bib.bib9), Ch. 5]. In the present finite-dimensional setting, one may
take the capacity c:2{1,…,n}→[0,1]c:2^{\{1,\dots,n\}}\to[0,1] defined by

|  |  |  |
| --- | --- | --- |
|  | c​(A):=ρ^n​(−𝟏A),A⊆{1,…,n},c(A):=\hat{\rho}\_{n}(-\mathbf{1}\_{A}),\qquad A\subseteq\{1,\dots,n\}, |  |

where 𝟏A∈ℝn\mathbf{1}\_{A}\in\mathbb{R}^{n} is the indicator vector of AA.

Law invariance implies that c​(A)c(A) depends only on |A||A|, hence cc is determined by a unique
distortion function on the grid {0,1,…,n}\{0,1,\dots,n\}:

|  |  |  |
| --- | --- | --- |
|  | g​(k):=c​({1,2,…,k})=ρ^n​(−𝟏{1,…,k}),k=0,…,n,g(k):=c(\{1,2,\dots,k\})=\hat{\rho}\_{n}(-\mathbf{1}\_{\{1,\dots,k\}}),\qquad k=0,\dots,n, |  |

with g​(0)=0g(0)=0 and g​(n)=1g(n)=1. Coherence (in particular subadditivity) is equivalent in this finite
setting to discrete concavity of gg (equivalently, to Δn↓\Delta\_{n}^{\downarrow}-monotonicity of the
resulting weights).

By the finite Choquet integral formula (see, e.g., [[9](https://arxiv.org/html/2602.00784v1#bib.bib9), Ch. 5] or the risk-measure
presentation in [[11](https://arxiv.org/html/2602.00784v1#bib.bib11)]), for every x∈ℝnx\in\mathbb{R}^{n},

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(x)=∑i=1n(g​(i)−g​(i−1))​(−xi:n).\hat{\rho}\_{n}(x)=\sum\_{i=1}^{n}\bigl(g(i)-g(i-1)\bigr)\,(-x\_{i:n}). |  |

Setting ai:=g​(i)−g​(i−1)a\_{i}:=g(i)-g(i-1) yields a∈Δn↓a\in\Delta\_{n}^{\downarrow}. Uniqueness follows because the values
ρ^n​(−𝟏{1,…,k})=g​(k)\hat{\rho}\_{n}(-\mathbf{1}\_{\{1,\dots,k\}})=g(k) recover the increments ai=g​(i)−g​(i−1)a\_{i}=g(i)-g(i-1), hence the weight
vector is uniquely determined.

Consequently Mρ^nsM^{s}\_{\hat{\rho}\_{n}} must be the singleton {a}\{a\}, proving the theorem.
∎

## 5. Discrete Kusuoka representation for law-invariant CREs

The Kusuoka representation (Theorem [2.5](https://arxiv.org/html/2602.00784v1#S2.Thmtheorem5 "Theorem 2.5 (Kusuoka representation [14]). ‣ 2.2. Law invariance and spectral representation ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")) expresses law-invariant CRMs as
suprema over mixtures of expected shortfall. In this section, we establish the
finite-sample analogue for CREs.

### 5.1. Discrete expected shortfall

We begin by defining the natural finite-sample version of expected shortfall.

###### Definition 5.1 (Discrete expected shortfall).

For x∈ℝnx\in\mathbb{R}^{n} and k∈{1,…,n}k\in\{1,\ldots,n\}, the *discrete expected shortfall* at
level k/nk/n is

|  |  |  |  |
| --- | --- | --- | --- |
| (13) |  | dESk/n⁡(x):=−1k​∑i=1kxi:n.\operatorname{dES}\_{k/n}(x):=-\frac{1}{k}\sum\_{i=1}^{k}x\_{i:n}. |  |

This is the average of the kk smallest (most negative) outcomes, negated to give a
positive quantity for losses. When k=1k=1, we recover the minimum:
dES1/n⁡(x)=−x1:n\operatorname{dES}\_{1/n}(x)=-x\_{1:n}. When k=nk=n, we get the negative mean:
dES1⁡(x)=−1n​∑i=1nxi\operatorname{dES}\_{1}(x)=-\frac{1}{n}\sum\_{i=1}^{n}x\_{i}.

###### Remark 5.2.

The discrete expected shortfall dESk/n\operatorname{dES}\_{k/n} is a coherent, law-invariant, comonotonic
risk estimator. Its weight vector is a=(1k,…,1k,0,…,0)a=(\frac{1}{k},\ldots,\frac{1}{k},0,\ldots,0)
with kk entries equal to 1/k1/k, which lies in Δn↓\Delta\_{n}^{\downarrow}.

### 5.2. Decomposition of L-estimators into discrete expected shortfall

The key technical result is that any L-estimator with non-increasing weights can be
written as a mixture of discrete expected shortfalls.

###### Lemma 5.3 (ES-decomposition lemma).

Let a=(a1,…,an)∈Δn↓a=(a\_{1},\ldots,a\_{n})\in\Delta\_{n}^{\downarrow} and set an+1:=0a\_{n+1}:=0. Define

|  |  |  |  |
| --- | --- | --- | --- |
| (14) |  | μk:=k​(ak−ak+1),k=1,…,n.\mu\_{k}:=k(a\_{k}-a\_{k+1}),\qquad k=1,\ldots,n. |  |

Then:

1. (i)

   μk⩾0\mu\_{k}\geqslant 0 for all kk;
2. (ii)

   ∑k=1nμk=1\sum\_{k=1}^{n}\mu\_{k}=1;
3. (iii)

   for every x∈ℝnx\in\mathbb{R}^{n},

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (15) |  | ∑i=1nai​(−xi:n)=∑k=1nμk​dESk/n⁡(x).\sum\_{i=1}^{n}a\_{i}(-x\_{i:n})=\sum\_{k=1}^{n}\mu\_{k}\,\operatorname{dES}\_{k/n}(x). |  |

###### Proof.

(i) Since aa is non-increasing, ak⩾ak+1a\_{k}\geqslant a\_{k+1}, hence μk=k​(ak−ak+1)⩾0\mu\_{k}=k(a\_{k}-a\_{k+1})\geqslant 0.

(ii) We compute:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=1nμk\displaystyle\sum\_{k=1}^{n}\mu\_{k} | =∑k=1nk​(ak−ak+1)\displaystyle=\sum\_{k=1}^{n}k(a\_{k}-a\_{k+1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑k=1nk​ak−∑k=1nk​ak+1\displaystyle=\sum\_{k=1}^{n}ka\_{k}-\sum\_{k=1}^{n}ka\_{k+1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑k=1nk​ak−∑j=2n+1(j−1)​aj\displaystyle=\sum\_{k=1}^{n}ka\_{k}-\sum\_{j=2}^{n+1}(j-1)a\_{j} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =a1+∑k=2nk​ak−∑j=2n(j−1)​aj−n​an+1\displaystyle=a\_{1}+\sum\_{k=2}^{n}ka\_{k}-\sum\_{j=2}^{n}(j-1)a\_{j}-na\_{n+1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =a1+∑k=2n(k−(k−1))​ak−0\displaystyle=a\_{1}+\sum\_{k=2}^{n}(k-(k-1))a\_{k}-0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =a1+∑k=2nak=∑k=1nak=1.\displaystyle=a\_{1}+\sum\_{k=2}^{n}a\_{k}=\sum\_{k=1}^{n}a\_{k}=1. |  |

(iii) We expand the right-hand side:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=1nμk​dESk/n⁡(x)\displaystyle\sum\_{k=1}^{n}\mu\_{k}\,\operatorname{dES}\_{k/n}(x) | =∑k=1nμk⋅(−1k​∑i=1kxi:n)\displaystyle=\sum\_{k=1}^{n}\mu\_{k}\cdot\left(-\frac{1}{k}\sum\_{i=1}^{k}x\_{i:n}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∑k=1n(ak−ak+1)​∑i=1kxi:n.\displaystyle=-\sum\_{k=1}^{n}(a\_{k}-a\_{k+1})\sum\_{i=1}^{k}x\_{i:n}. |  |

We exchange the order of summation. For each i∈{1,…,n}i\in\{1,\ldots,n\}, the term xi:nx\_{i:n}
appears in the inner sum for all k⩾ik\geqslant i. Thus:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −∑k=1n(ak−ak+1)​∑i=1kxi:n\displaystyle-\sum\_{k=1}^{n}(a\_{k}-a\_{k+1})\sum\_{i=1}^{k}x\_{i:n} | =−∑i=1nxi:n​∑k=in(ak−ak+1)\displaystyle=-\sum\_{i=1}^{n}x\_{i:n}\sum\_{k=i}^{n}(a\_{k}-a\_{k+1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∑i=1nxi:n​(ai−an+1)\displaystyle=-\sum\_{i=1}^{n}x\_{i:n}(a\_{i}-a\_{n+1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∑i=1nxi:n⋅ai\displaystyle=-\sum\_{i=1}^{n}x\_{i:n}\cdot a\_{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1nai​(−xi:n).∎\displaystyle=\sum\_{i=1}^{n}a\_{i}(-x\_{i:n}).\qed |  |

### 5.3. The discrete Kusuoka representation theorem

Let 𝒯:Δn↓→Δn\mathcal{T}:\Delta\_{n}^{\downarrow}\to\Delta\_{n} denote the linear map a↦μa\mapsto\mu defined by
([14](https://arxiv.org/html/2602.00784v1#S5.E14 "In Lemma 5.3 (ES-decomposition lemma). ‣ 5.2. Decomposition of L-estimators into discrete expected shortfall ‣ 5. Discrete Kusuoka representation for law-invariant CREs ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")). The lemma shows that 𝒯\mathcal{T} is well-defined and maps
non-increasing probability vectors to probability vectors.

###### Remark 5.4 (Inverse of 𝒯\mathcal{T}).

Given μ∈Δn\mu\in\Delta\_{n} with μk=k​(ak−ak+1)\mu\_{k}=k(a\_{k}-a\_{k+1}) and an+1=0a\_{n+1}=0, one recovers

|  |  |  |
| --- | --- | --- |
|  | ai=∑k=inμkk,i=1,…,n.a\_{i}=\sum\_{k=i}^{n}\frac{\mu\_{k}}{k},\qquad i=1,\ldots,n. |  |

Thus mixtures of dESk/n\operatorname{dES}\_{k/n} are in one-to-one correspondence with weight vectors in Δn↓\Delta\_{n}^{\downarrow}.

###### Theorem 5.5 (Discrete Kusuoka representation).

Let ρ^n:ℝn→ℝ\hat{\rho}\_{n}:\mathbb{R}^{n}\to\mathbb{R} be a law-invariant CRE. Then there exists a non-empty convex
set ℳn⊆Δn\mathcal{M}\_{n}\subseteq\Delta\_{n} such that for all x∈ℝnx\in\mathbb{R}^{n},

|  |  |  |  |
| --- | --- | --- | --- |
| (16) |  | ρ^n​(x)=supμ∈ℳn∑k=1nμk​dESk/n⁡(x),\hat{\rho}\_{n}(x)=\sup\_{\mu\in\mathcal{M}\_{n}}\sum\_{k=1}^{n}\mu\_{k}\,\operatorname{dES}\_{k/n}(x), |  |

with the supremum attained. Moreover, one may take ℳn=𝒯​(Mρ^ns)\mathcal{M}\_{n}=\mathcal{T}(M^{s}\_{\hat{\rho}\_{n}}),
where Mρ^nsM^{s}\_{\hat{\rho}\_{n}} is the representing set from Theorem [2.10](https://arxiv.org/html/2602.00784v1#S2.Thmtheorem10 "Theorem 2.10 (Law-invariant CREs [1, Theorem 4.2]). ‣ 2.3. Coherent risk estimators ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics").

###### Proof.

By Theorem [2.10](https://arxiv.org/html/2602.00784v1#S2.Thmtheorem10 "Theorem 2.10 (Law-invariant CREs [1, Theorem 4.2]). ‣ 2.3. Coherent risk estimators ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), there exists a convex set Mρ^ns⊆Δn↓M^{s}\_{\hat{\rho}\_{n}}\subseteq\Delta\_{n}^{\downarrow}
such that

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(x)=supa∈Mρ^ns∑i=1nai​(−xi:n).\hat{\rho}\_{n}(x)=\sup\_{a\in M^{s}\_{\hat{\rho}\_{n}}}\sum\_{i=1}^{n}a\_{i}(-x\_{i:n}). |  |

By Lemma [5.3](https://arxiv.org/html/2602.00784v1#S5.Thmtheorem3 "Lemma 5.3 (ES-decomposition lemma). ‣ 5.2. Decomposition of L-estimators into discrete expected shortfall ‣ 5. Discrete Kusuoka representation for law-invariant CREs ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), for each a∈Mρ^nsa\in M^{s}\_{\hat{\rho}\_{n}},

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nai​(−xi:n)=∑k=1nμk​dESk/n⁡(x),\sum\_{i=1}^{n}a\_{i}(-x\_{i:n})=\sum\_{k=1}^{n}\mu\_{k}\,\operatorname{dES}\_{k/n}(x), |  |

where μ=𝒯​(a)\mu=\mathcal{T}(a). Thus

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(x)=supa∈Mρ^ns∑k=1n𝒯​(a)k​dESk/n⁡(x)=supμ∈𝒯​(Mρ^ns)∑k=1nμk​dESk/n⁡(x).\hat{\rho}\_{n}(x)=\sup\_{a\in M^{s}\_{\hat{\rho}\_{n}}}\sum\_{k=1}^{n}\mathcal{T}(a)\_{k}\,\operatorname{dES}\_{k/n}(x)=\sup\_{\mu\in\mathcal{T}(M^{s}\_{\hat{\rho}\_{n}})}\sum\_{k=1}^{n}\mu\_{k}\,\operatorname{dES}\_{k/n}(x). |  |

Setting ℳn:=𝒯​(Mρ^ns)\mathcal{M}\_{n}:=\mathcal{T}(M^{s}\_{\hat{\rho}\_{n}}), we obtain ([16](https://arxiv.org/html/2602.00784v1#S5.E16 "In Theorem 5.5 (Discrete Kusuoka representation). ‣ 5.3. The discrete Kusuoka representation theorem ‣ 5. Discrete Kusuoka representation for law-invariant CREs ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")).

Convexity: since 𝒯\mathcal{T} is linear, 𝒯​(Mρ^ns)\mathcal{T}(M^{s}\_{\hat{\rho}\_{n}}) is convex
whenever Mρ^nsM^{s}\_{\hat{\rho}\_{n}} is.

Attainment: the supremum in ([6](https://arxiv.org/html/2602.00784v1#S2.E6 "In Theorem 2.10 (Law-invariant CREs [1, Theorem 4.2]). ‣ 2.3. Coherent risk estimators ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")) is attained for each xx at some
a∗∈Mρ^nsa^{\*}\in M^{s}\_{\hat{\rho}\_{n}}. Then μ∗=𝒯​(a∗)\mu^{\*}=\mathcal{T}(a^{\*}) achieves the supremum in
([16](https://arxiv.org/html/2602.00784v1#S5.E16 "In Theorem 5.5 (Discrete Kusuoka representation). ‣ 5.3. The discrete Kusuoka representation theorem ‣ 5. Discrete Kusuoka representation for law-invariant CREs ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")).
∎

###### Corollary 5.6 (Comonotonic case).

A CRE ρ^n\hat{\rho}\_{n} is comonotonic and law-invariant if and only if there exists a unique
μ∈Δn\mu\in\Delta\_{n} such that

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(x)=∑k=1nμk​dESk/n⁡(x),x∈ℝn.\hat{\rho}\_{n}(x)=\sum\_{k=1}^{n}\mu\_{k}\,\operatorname{dES}\_{k/n}(x),\qquad x\in\mathbb{R}^{n}. |  |

###### Proof.

By Theorem [2.11](https://arxiv.org/html/2602.00784v1#S2.Thmtheorem11 "Theorem 2.11 (Comonotonic law-invariant CREs [1, Theorem 4.10]). ‣ 2.3. Coherent risk estimators ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), Mρ^ns={a}M^{s}\_{\hat{\rho}\_{n}}=\{a\} is a singleton, hence
ℳn={𝒯​(a)}\mathcal{M}\_{n}=\{\mathcal{T}(a)\} is a singleton.
∎

###### Remark 5.7.

The discrete Kusuoka representation ([16](https://arxiv.org/html/2602.00784v1#S5.E16 "In Theorem 5.5 (Discrete Kusuoka representation). ‣ 5.3. The discrete Kusuoka representation theorem ‣ 5. Discrete Kusuoka representation for law-invariant CREs ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")) is the finite-sample analogue
of the population-level Kusuoka representation ([3](https://arxiv.org/html/2602.00784v1#S2.E3 "In Theorem 2.5 (Kusuoka representation [14]). ‣ 2.2. Law invariance and spectral representation ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")). The probability
measure ν\nu on (0,1](0,1] is replaced by a probability vector μ∈Δn\mu\in\Delta\_{n}, and the
continuous expected shortfall ESα\operatorname{ES}\_{\alpha} is replaced by its discrete counterpart
dESk/n\operatorname{dES}\_{k/n}. This representation makes explicit the sense in which CREs are
“statistical shadows” of CRMs.

## 6. Spectral risk measures and hyperfinite L-statistics

We now turn to spectral risk measures and their finite-sample estimators, developing the
hyperfinite perspective that will underpin our consistency results.

### 6.1. Spectral risk as a hyperfinite L-statistic

Let φ\varphi be a spectrum (Definition [2.6](https://arxiv.org/html/2602.00784v1#S2.Thmtheorem6 "Definition 2.6 (Spectral risk measure). ‣ 2.2. Law invariance and spectral representation ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")) and X∈L1X\in L^{1} a random
variable with lower quantile function qXq\_{X}. The spectral risk measure is

|  |  |  |
| --- | --- | --- |
|  | ρφ​(X)=−∫01qX​(α)​φ​(α)​𝑑α.\rho\_{\varphi}(X)=-\int\_{0}^{1}q\_{X}(\alpha)\,\varphi(\alpha)\,d\alpha. |  |

Now consider a hyperfinite i.i.d. sample (X1,…,XN)(X\_{1},\ldots,X\_{N}) with N∈ℕ∗N\in{}^{\*}\mathbb{N} infinite.
Let X1:N⩽⋯⩽XN:NX\_{1:N}\leqslant\cdots\leqslant X\_{N:N} be the order statistics and αk:=k/N\alpha\_{k}:=k/N.
Define the *hyperfinite L-statistic*

|  |  |  |  |
| --- | --- | --- | --- |
| (17) |  | LNφ:=−1N​∑k=1Nφ​(αk)​Xk:N.L\_{N}^{\varphi}:=-\frac{1}{N}\sum\_{k=1}^{N}\varphi(\alpha\_{k})\,X\_{k:N}. |  |

###### Proposition 6.1 (Hyperfinite spectral representation).

Let X∈L1X\in L^{1} with quantile function qXq\_{X}, and let φ\varphi be a bounded spectrum.
Then, for Loeb-almost all sample paths,

|  |  |  |  |
| --- | --- | --- | --- |
| (18) |  | ρφ​(X)=st⁡(LNφ).\rho\_{\varphi}(X)=\operatorname{st}(L\_{N}^{\varphi}). |  |

###### Proof.

Apply Theorem [3.20](https://arxiv.org/html/2602.00784v1#S3.Thmtheorem20 "Theorem 3.20 (Hyperfinite Glivenko–Cantelli / quantile shadow). ‣ 3.7. The hyperfinite strong law and Glivenko–Cantelli theorem ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") with g=φg=\varphi. Since φ\varphi is bounded and (being
monotone) Riemann integrable, and X∈L1X\in L^{1} implies ∫01|φ​(α)​qX​(α)|​𝑑α<∞\int\_{0}^{1}|\varphi(\alpha)q\_{X}(\alpha)|\,d\alpha<\infty,
we obtain

|  |  |  |
| --- | --- | --- |
|  | st⁡(1N​∑k=1Nφ​(αk)​Xk:N)=∫01φ​(α)​qX​(α)​𝑑α.\operatorname{st}\Big(\frac{1}{N}\sum\_{k=1}^{N}\varphi(\alpha\_{k})X\_{k:N}\Big)=\int\_{0}^{1}\varphi(\alpha)q\_{X}(\alpha)\,d\alpha. |  |

Multiplying by −1-1 gives st⁡(LNφ)=ρφ​(X)\operatorname{st}(L\_{N}^{\varphi})=\rho\_{\varphi}(X).
∎

### 6.2. Canonical spectral plug-in estimators

Given a spectrum φ\varphi and sample size n∈ℕn\in\mathbb{N}, the canonical finite-sample
estimator is constructed as follows.

###### Definition 6.2 (Canonical spectral plug-in estimator).

For x∈ℝnx\in\mathbb{R}^{n}, define

|  |  |  |  |
| --- | --- | --- | --- |
| (19) |  | ρ^n,φ​(x):=−∑i=1nai,n​(φ)​xi:n,\hat{\rho}\_{n,\varphi}(x):=-\sum\_{i=1}^{n}a\_{i,n}(\varphi)\,x\_{i:n}, |  |

where the weights are

|  |  |  |  |
| --- | --- | --- | --- |
| (20) |  | ai,n​(φ):=∫(i−1)/ni/nφ​(s)​𝑑s,i=1,…,n.a\_{i,n}(\varphi):=\int\_{(i-1)/n}^{i/n}\varphi(s)\,ds,\qquad i=1,\ldots,n. |  |

###### Proposition 6.3.

The canonical spectral plug-in estimator ρ^n,φ\hat{\rho}\_{n,\varphi} is a comonotonic,
law-invariant CRE. Moreover, its Kusuoka representation (Theorem [5.5](https://arxiv.org/html/2602.00784v1#S5.Thmtheorem5 "Theorem 5.5 (Discrete Kusuoka representation). ‣ 5.3. The discrete Kusuoka representation theorem ‣ 5. Discrete Kusuoka representation for law-invariant CREs ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"))
has ℳn={μ}\mathcal{M}\_{n}=\{\mu\} a singleton with μ=𝒯​(an​(φ))\mu=\mathcal{T}(a\_{n}(\varphi)).

###### Proof.

Since φ\varphi is non-increasing, the weights ai,n​(φ)a\_{i,n}(\varphi) are non-increasing in
ii (as integrals of a non-increasing function over consecutive intervals). Also,
∑i=1nai,n​(φ)=∫01φ=1\sum\_{i=1}^{n}a\_{i,n}(\varphi)=\int\_{0}^{1}\varphi=1, so an​(φ)∈Δn↓a\_{n}(\varphi)\in\Delta\_{n}^{\downarrow}.

By Theorem [2.11](https://arxiv.org/html/2602.00784v1#S2.Thmtheorem11 "Theorem 2.11 (Comonotonic law-invariant CREs [1, Theorem 4.10]). ‣ 2.3. Coherent risk estimators ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), ρ^n,φ\hat{\rho}\_{n,\varphi} is a comonotonic, law-invariant CRE.
The Kusuoka representation follows from Corollary [5.6](https://arxiv.org/html/2602.00784v1#S5.Thmtheorem6 "Corollary 5.6 (Comonotonic case). ‣ 5.3. The discrete Kusuoka representation theorem ‣ 5. Discrete Kusuoka representation for law-invariant CREs ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics").
∎

### 6.3. Step approximations and the spectral-estimator correspondence

For theoretical analysis, it is useful to associate with each weight vector
an∈Δn↓a\_{n}\in\Delta\_{n}^{\downarrow} a step function φn\varphi\_{n} on [0,1][0,1].

###### Definition 6.4 (Associated step function).

For an=(a1,n,…,an,n)∈Δn↓a\_{n}=(a\_{1,n},\ldots,a\_{n,n})\in\Delta\_{n}^{\downarrow}, define

|  |  |  |  |
| --- | --- | --- | --- |
| (21) |  | φn​(t):=∑i=1nn​ai,n​ 1((i−1)/n,i/n]​(t),t∈(0,1].\varphi\_{n}(t):=\sum\_{i=1}^{n}na\_{i,n}\,\mathbf{1}\_{((i-1)/n,i/n]}(t),\qquad t\in(0,1]. |  |

When ana\_{n} arises from a spectrum φ\varphi via ([20](https://arxiv.org/html/2602.00784v1#S6.E20 "In Definition 6.2 (Canonical spectral plug-in estimator). ‣ 6.2. Canonical spectral plug-in estimators ‣ 6. Spectral risk measures and hyperfinite L-statistics ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")), we have

|  |  |  |
| --- | --- | --- |
|  | φn​(t)=n​∫(i−1)/ni/nφ​(s)​𝑑s​ for ​t∈((i−1)/n,i/n],\varphi\_{n}(t)=n\int\_{(i-1)/n}^{i/n}\varphi(s)ds\text{ for }t\in((i-1)/n,i/n], |  |

which is the average of φ\varphi on that interval.

###### Lemma 6.5 (Integral correspondence).

For an∈Δn↓a\_{n}\in\Delta\_{n}^{\downarrow} and its associated step function φn\varphi\_{n},

|  |  |  |  |
| --- | --- | --- | --- |
| (22) |  | ∑i=1nai,n​xi:n=∫01φn​(α)​qn​(α)​𝑑α,\sum\_{i=1}^{n}a\_{i,n}\,x\_{i:n}=\int\_{0}^{1}\varphi\_{n}(\alpha)\,q\_{n}(\alpha)\,d\alpha, |  |

where qn​(α):=x⌈n​α⌉:nq\_{n}(\alpha):=x\_{\lceil n\alpha\rceil:n} is the empirical quantile function.

###### Proof.

For α∈((i−1)/n,i/n]\alpha\in((i-1)/n,i/n], we have ⌈n​α⌉=i\lceil n\alpha\rceil=i, so
qn​(α)=xi:nq\_{n}(\alpha)=x\_{i:n}. Thus

|  |  |  |
| --- | --- | --- |
|  | ∫01φn​(α)​qn​(α)​𝑑α=∑i=1n∫(i−1)/ni/nn​ai,n⋅xi:n​𝑑α=∑i=1nn​ai,n⋅1n⋅xi:n=∑i=1nai,n​xi:n.∎\int\_{0}^{1}\varphi\_{n}(\alpha)q\_{n}(\alpha)d\alpha=\sum\_{i=1}^{n}\int\_{(i-1)/n}^{i/n}na\_{i,n}\cdot x\_{i:n}\,d\alpha=\sum\_{i=1}^{n}na\_{i,n}\cdot\frac{1}{n}\cdot x\_{i:n}=\sum\_{i=1}^{n}a\_{i,n}x\_{i:n}.\qed |  |

## 7. Spectral plug-in consistency

We now establish the consistency of spectral plug-in estimators, culminating in a
uniform consistency theorem over Lipschitz families of spectra.

### 7.1. Pointwise consistency: analytic core

The following lemma isolates the key analytic condition for consistency.

###### Lemma 7.1 (Primitive convergence implies density convergence).

Let (φn)n∈ℕ(\varphi\_{n})\_{n\in\mathbb{N}} be a sequence of step functions on [0,1][0,1], each non-increasing,
non-negative, and satisfying ∫01φn=1\int\_{0}^{1}\varphi\_{n}=1. Assume supn‖φn‖∞<∞\sup\_{n}\|\varphi\_{n}\|\_{\infty}<\infty.
Let φ\varphi be a bounded spectrum. Define the primitives

|  |  |  |
| --- | --- | --- |
|  | Φn​(t):=∫0tφn​(s)​𝑑s,Φ​(t):=∫0tφ​(s)​𝑑s.\Phi\_{n}(t):=\int\_{0}^{t}\varphi\_{n}(s)\,ds,\qquad\Phi(t):=\int\_{0}^{t}\varphi(s)\,ds. |  |

If Φn​(t)→Φ​(t)\Phi\_{n}(t)\to\Phi(t) for all t∈(0,1)t\in(0,1), then:

1. (i)

   φn​(t)→φ​(t)\varphi\_{n}(t)\to\varphi(t) for almost every t∈(0,1)t\in(0,1);
2. (ii)

   φn→φ\varphi\_{n}\to\varphi in L1​([0,1])L^{1}([0,1]).

###### Proof.

(i) Fix t∈(0,1)t\in(0,1) and h>0h>0 sufficiently small. Since φn\varphi\_{n} is non-increasing,
for any s∈[t,t+h]s\in[t,t+h] we have φn​(s)⩽φn​(t)\varphi\_{n}(s)\leqslant\varphi\_{n}(t), hence

|  |  |  |
| --- | --- | --- |
|  | Φn​(t+h)−Φn​(t)h=1h​∫tt+hφn​(s)​𝑑s⩽φn​(t).\frac{\Phi\_{n}(t+h)-\Phi\_{n}(t)}{h}=\frac{1}{h}\int\_{t}^{t+h}\varphi\_{n}(s)ds\leqslant\varphi\_{n}(t). |  |

Similarly, for s∈[t−h,t]s\in[t-h,t], φn​(s)⩾φn​(t)\varphi\_{n}(s)\geqslant\varphi\_{n}(t), so

|  |  |  |
| --- | --- | --- |
|  | φn​(t)⩽Φn​(t)−Φn​(t−h)h.\varphi\_{n}(t)\leqslant\frac{\Phi\_{n}(t)-\Phi\_{n}(t-h)}{h}. |  |

Taking lim inf\liminf and lim sup\limsup as n→∞n\to\infty, and using Φn→Φ\Phi\_{n}\to\Phi pointwise:

|  |  |  |
| --- | --- | --- |
|  | Φ​(t+h)−Φ​(t)h⩽lim infn→∞φn​(t)⩽lim supn→∞φn​(t)⩽Φ​(t)−Φ​(t−h)h.\frac{\Phi(t+h)-\Phi(t)}{h}\leqslant\liminf\_{n\to\infty}\varphi\_{n}(t)\leqslant\limsup\_{n\to\infty}\varphi\_{n}(t)\leqslant\frac{\Phi(t)-\Phi(t-h)}{h}. |  |

Now let h↓0h\downarrow 0. Since φ\varphi is non-increasing, Φ\Phi is concave, hence
differentiable almost everywhere. At differentiability points of Φ\Phi, both bounds
converge to Φ′​(t)=φ​(t)\Phi^{\prime}(t)=\varphi(t), giving φn​(t)→φ​(t)\varphi\_{n}(t)\to\varphi(t).

(ii) By (i), φn→φ\varphi\_{n}\to\varphi pointwise almost everywhere. The uniform bound
supn‖φn‖∞<∞\sup\_{n}\|\varphi\_{n}\|\_{\infty}<\infty allows dominated convergence:
∫01|φn−φ|→0\int\_{0}^{1}|\varphi\_{n}-\varphi|\to 0.
∎

### 7.2. Spectral L-estimator consistency theorem

###### Theorem 7.2 (Spectral L-estimator consistency: a distribution-free criterion).

Let φ\varphi be a bounded spectrum. Let ρ^n​(x)=−∑i=1nai,n​xi:n\hat{\rho}\_{n}(x)=-\sum\_{i=1}^{n}a\_{i,n}x\_{i:n} with
an∈Δn↓a\_{n}\in\Delta\_{n}^{\downarrow}, and let φn\varphi\_{n} be the associated step function ([21](https://arxiv.org/html/2602.00784v1#S6.E21 "In Definition 6.4 (Associated step function). ‣ 6.3. Step approximations and the spectral-estimator correspondence ‣ 6. Spectral risk measures and hyperfinite L-statistics ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")).
Assume supn‖φn‖∞<∞\sup\_{n}\|\varphi\_{n}\|\_{\infty}<\infty.

Then the following are equivalent:

1. (i)

   For every t∈(0,1)t\in(0,1), ∫0tφn​(s)​𝑑s→∫0tφ​(s)​𝑑s\int\_{0}^{t}\varphi\_{n}(s)\,ds\to\int\_{0}^{t}\varphi(s)\,ds.
2. (ii)

   For every X∈L1X\in L^{1} and every i.i.d. sample (Xi)(X\_{i}) with law XX,

   |  |  |  |
   | --- | --- | --- |
   |  | ρ^n​(X1,…,Xn)→n→∞a.s.ρφ​(X).\hat{\rho}\_{n}(X\_{1},\ldots,X\_{n})\xrightarrow[n\to\infty]{\mathrm{a.s.}}\rho\_{\varphi}(X). |  |

###### Remark 7.3.

The condition supn‖φn‖∞<∞\sup\_{n}\|\varphi\_{n}\|\_{\infty}<\infty is automatic for the canonical discretisation
ai,n=∫(i−1)/ni/nφa\_{i,n}=\int\_{(i-1)/n}^{i/n}\varphi of a bounded spectrum φ\varphi: in this case
‖φn‖∞⩽‖φ‖∞\|\varphi\_{n}\|\_{\infty}\leqslant\|\varphi\|\_{\infty} since φn\varphi\_{n} is a step-function approximation.
For general L-estimator weights (ai,n)(a\_{i,n}) not arising from a fixed spectrum, the uniform
bound is a genuine assumption that must be verified.

###### Proof.

Assume *(i)*. By Lemma [7.1](https://arxiv.org/html/2602.00784v1#S7.Thmtheorem1 "Lemma 7.1 (Primitive convergence implies density convergence). ‣ 7.1. Pointwise consistency: analytic core ‣ 7. Spectral plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), the primitive convergence implies
φn→φ\varphi\_{n}\to\varphi in L1​([0,1])L^{1}([0,1]). Let qn​(α):=X⌈n​α⌉:nq\_{n}(\alpha):=X\_{\lceil n\alpha\rceil:n} be the
empirical quantile function and let qXq\_{X} be the population lower quantile. By the
Glivenko–Cantelli theorem, qn​(α)→qX​(α)q\_{n}(\alpha)\to q\_{X}(\alpha) almost surely at every continuity
point of qXq\_{X}, hence for almost every α∈(0,1)\alpha\in(0,1).

Using Lemma [6.5](https://arxiv.org/html/2602.00784v1#S6.Thmtheorem5 "Lemma 6.5 (Integral correspondence). ‣ 6.3. Step approximations and the spectral-estimator correspondence ‣ 6. Spectral risk measures and hyperfinite L-statistics ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"),

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(X1,…,Xn)=−∫01φn​(α)​qn​(α)​𝑑α,ρφ​(X)=−∫01φ​(α)​qX​(α)​𝑑α.\hat{\rho}\_{n}(X\_{1},\ldots,X\_{n})=-\int\_{0}^{1}\varphi\_{n}(\alpha)\,q\_{n}(\alpha)\,d\alpha,\qquad\rho\_{\varphi}(X)=-\int\_{0}^{1}\varphi(\alpha)\,q\_{X}(\alpha)\,d\alpha. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | |ρ^n​(X1,…,Xn)−ρφ​(X)|⩽∫01|φn−φ|​|qn|​𝑑α+∫01|φ|​|qn−qX|​𝑑α.\left|\hat{\rho}\_{n}(X\_{1},\ldots,X\_{n})-\rho\_{\varphi}(X)\right|\leqslant\int\_{0}^{1}|\varphi\_{n}-\varphi|\,|q\_{n}|\,d\alpha+\int\_{0}^{1}|\varphi|\,|q\_{n}-q\_{X}|\,d\alpha. |  |

We handle these two integrals separately.

Fix M>0M>0. Since |qn|=|qn|​𝟏{|qn|⩽M}+|qn|​𝟏{|qn|>M}|q\_{n}|=|q\_{n}|\mathbf{1}\_{\{|q\_{n}|\leqslant M\}}+|q\_{n}|\mathbf{1}\_{\{|q\_{n}|>M\}}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫01|φn−φ|​|qn|​𝑑α\displaystyle\int\_{0}^{1}|\varphi\_{n}-\varphi|\,|q\_{n}|\,d\alpha | ⩽M​∫01|φn−φ|​𝑑α+(supm‖φm‖∞+‖φ‖∞)​∫01|qn|​ 1{|qn|>M}​𝑑α.\displaystyle\leqslant M\int\_{0}^{1}|\varphi\_{n}-\varphi|\,d\alpha+\bigl(\sup\_{m}\|\varphi\_{m}\|\_{\infty}+\|\varphi\|\_{\infty}\bigr)\int\_{0}^{1}|q\_{n}|\,\mathbf{1}\_{\{|q\_{n}|>M\}}\,d\alpha. |  |

The first term converges to 0 because φn→φ\varphi\_{n}\to\varphi in L1L^{1}. Moreover,

|  |  |  |
| --- | --- | --- |
|  | ∫01|qn​(α)|​ 1{|qn​(α)|>M}​𝑑α=1n​∑i=1n|Xi|​ 1{|Xi|>M},\int\_{0}^{1}|q\_{n}(\alpha)|\,\mathbf{1}\_{\{|q\_{n}(\alpha)|>M\}}\,d\alpha=\frac{1}{n}\sum\_{i=1}^{n}|X\_{i}|\,\mathbf{1}\_{\{|X\_{i}|>M\}}, |  |

since qnq\_{n} is a step function taking the values Xi:nX\_{i:n}. By the strong law of large
numbers, the right-hand side converges almost surely to 𝖤​[|X|​ 1{|X|>M}]\mathsf{E}[|X|\,\mathbf{1}\_{\{|X|>M\}}].
Letting n→∞n\to\infty and then M→∞M\to\infty (using 𝖤​|X|<∞\mathsf{E}|X|<\infty) shows

|  |  |  |
| --- | --- | --- |
|  | ∫01|φn−φ|​|qn|​𝑑α⟶0almost surely.\int\_{0}^{1}|\varphi\_{n}-\varphi|\,|q\_{n}|\,d\alpha\longrightarrow 0\qquad\text{almost surely.} |  |

For the second term, note first that qn​(α)→qX​(α)q\_{n}(\alpha)\to q\_{X}(\alpha) almost everywhere.
Define truncations qn(M):=max⁡(min⁡(qn,M),−M)q\_{n}^{(M)}:=\max(\min(q\_{n},M),-M) and qX(M):=max⁡(min⁡(qX,M),−M)q\_{X}^{(M)}:=\max(\min(q\_{X},M),-M).
Then |qn(M)−qX(M)|⩽2​M|q\_{n}^{(M)}-q\_{X}^{(M)}|\leqslant 2M and qn(M)→qX(M)q\_{n}^{(M)}\to q\_{X}^{(M)} almost everywhere, so dominated
convergence yields ∫01|qn(M)−qX(M)|​𝑑α→0\int\_{0}^{1}|q\_{n}^{(M)}-q\_{X}^{(M)}|\,d\alpha\to 0 almost surely for each fixed MM.
Moreover,

|  |  |  |
| --- | --- | --- |
|  | ∫01|qn−qX|⩽∫01|qn−qn(M)|+∫01|qn(M)−qX(M)|+∫01|qX(M)−qX|.\int\_{0}^{1}|q\_{n}-q\_{X}|\leqslant\int\_{0}^{1}|q\_{n}-q\_{n}^{(M)}|+\int\_{0}^{1}|q\_{n}^{(M)}-q\_{X}^{(M)}|+\int\_{0}^{1}|q\_{X}^{(M)}-q\_{X}|. |  |

The middle term tends to 0 almost surely for fixed MM. The last term tends to 0 as
M→∞M\to\infty because qX∈L1​(0,1)q\_{X}\in L^{1}(0,1) when X∈L1X\in L^{1}. Finally,

|  |  |  |
| --- | --- | --- |
|  | ∫01|qn​(α)|​ 1{|qn​(α)|>M}​𝑑α=1n​∑i=1n|Xi|​ 1{|Xi|>M}⟶𝖤​[|X|​ 1{|X|>M}]\int\_{0}^{1}|q\_{n}(\alpha)|\,\mathbf{1}\_{\{|q\_{n}(\alpha)|>M\}}\,d\alpha=\frac{1}{n}\sum\_{i=1}^{n}|X\_{i}|\,\mathbf{1}\_{\{|X\_{i}|>M\}}\longrightarrow\mathsf{E}[|X|\,\mathbf{1}\_{\{|X|>M\}}] |  |

almost surely, and the right-hand side vanishes as M→∞M\to\infty. Hence
∫01|qn−qX|​𝑑α→0\int\_{0}^{1}|q\_{n}-q\_{X}|\,d\alpha\to 0 almost surely, and therefore

|  |  |  |
| --- | --- | --- |
|  | ∫01|φ​(α)|​|qn​(α)−qX​(α)|​𝑑α⩽‖φ‖∞​∫01|qn−qX|⟶0almost surely.\int\_{0}^{1}|\varphi(\alpha)|\,|q\_{n}(\alpha)-q\_{X}(\alpha)|\,d\alpha\leqslant\|\varphi\|\_{\infty}\int\_{0}^{1}|q\_{n}-q\_{X}|\longrightarrow 0\qquad\text{almost surely.} |  |

Combining the two parts proves *(ii)*.

Conversely, assume *(ii)*. Fix t∈(0,1)t\in(0,1) and let U∼Unif​(0,1)U\sim\mathrm{Unif}(0,1).
Set X:=−𝟏{U⩽t}X:=-\mathbf{1}\_{\{U\leqslant t\}}. Then XX is bounded and

|  |  |  |
| --- | --- | --- |
|  | qX​(α)={−1,α∈(0,t],0,α∈(t,1),soρφ​(X)=∫0tφ​(α)​𝑑α.q\_{X}(\alpha)=\begin{cases}-1,&\alpha\in(0,t],\\ 0,&\alpha\in(t,1),\end{cases}\qquad\text{so}\qquad\rho\_{\varphi}(X)=\int\_{0}^{t}\varphi(\alpha)\,d\alpha. |  |

For an i.i.d. sample Xi:=−𝟏{Ui⩽t}X\_{i}:=-\mathbf{1}\_{\{U\_{i}\leqslant t\}}, let mn:=∑i=1n𝟏{Ui⩽t}m\_{n}:=\sum\_{i=1}^{n}\mathbf{1}\_{\{U\_{i}\leqslant t\}} and
tn:=mn/nt\_{n}:=m\_{n}/n. The order statistics satisfy X1:n=⋯=Xmn:n=−1X\_{1:n}=\cdots=X\_{m\_{n}:n}=-1 and
Xmn+1:n=⋯=Xn:n=0X\_{m\_{n}+1:n}=\cdots=X\_{n:n}=0, hence

|  |  |  |
| --- | --- | --- |
|  | ρ^n​(X1,…,Xn)=−∑i=1nai,n​Xi:n=∑i=1mnai,n=∫0tnφn​(α)​𝑑α.\hat{\rho}\_{n}(X\_{1},\ldots,X\_{n})=-\sum\_{i=1}^{n}a\_{i,n}X\_{i:n}=\sum\_{i=1}^{m\_{n}}a\_{i,n}=\int\_{0}^{t\_{n}}\varphi\_{n}(\alpha)\,d\alpha. |  |

By the strong law, tn→tt\_{n}\to t almost surely, and the uniform bound supn‖φn‖∞<∞\sup\_{n}\|\varphi\_{n}\|\_{\infty}<\infty
implies

|  |  |  |
| --- | --- | --- |
|  | |∫0tnφn−∫0tφn|⩽supn‖φn‖∞​|tn−t|⟶0almost surely.\left|\int\_{0}^{t\_{n}}\varphi\_{n}-\int\_{0}^{t}\varphi\_{n}\right|\leqslant\sup\_{n}\|\varphi\_{n}\|\_{\infty}\,|t\_{n}-t|\longrightarrow 0\qquad\text{almost surely.} |  |

Using *(ii)* for this bounded XX gives ∫0tnφn→∫0tφ\int\_{0}^{t\_{n}}\varphi\_{n}\to\int\_{0}^{t}\varphi almost surely,
and the previous estimate therefore yields ∫0tφn→∫0tφ\int\_{0}^{t}\varphi\_{n}\to\int\_{0}^{t}\varphi, i.e. *(i)*.
∎

### 7.3. Uniform consistency over Lipschitz spectral classes

We now establish uniform consistency over families of spectra satisfying Lipschitz and
boundedness conditions.

###### Definition 7.4 (Lipschitz spectral class).

A family 𝒱\mathcal{V} of spectra is a *Lipschitz spectral class* with constants
(C,L)(C,L) if:

1. (V1)

   Each φ∈𝒱\varphi\in\mathcal{V} is non-increasing, bounded, and ∫01φ=1\int\_{0}^{1}\varphi=1.
2. (V2)

   supφ∈𝒱‖φ‖∞⩽C\sup\_{\varphi\in\mathcal{V}}\|\varphi\|\_{\infty}\leqslant C.
3. (V3)

   Each φ∈𝒱\varphi\in\mathcal{V} is LL-Lipschitz: |φ​(s)−φ​(t)|⩽L​|s−t||\varphi(s)-\varphi(t)|\leqslant L|s-t|.

###### Lemma 7.5 (Uniform discretisation bound).

Let 𝒱\mathcal{V} be a Lipschitz spectral class with constants (C,L)(C,L). For each
φ∈𝒱\varphi\in\mathcal{V} and n∈ℕn\in\mathbb{N}, let an​(φ)a\_{n}(\varphi) be the canonical weights
([20](https://arxiv.org/html/2602.00784v1#S6.E20 "In Definition 6.2 (Canonical spectral plug-in estimator). ‣ 6.2. Canonical spectral plug-in estimators ‣ 6. Spectral risk measures and hyperfinite L-statistics ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")) and φn\varphi\_{n} the associated step function. Then:

1. (i)

   supφ∈𝒱supt∈(0,1]|φn​(t)−φ​(t)|⩽L/n\sup\_{\varphi\in\mathcal{V}}\sup\_{t\in(0,1]}|\varphi\_{n}(t)-\varphi(t)|\leqslant L/n.
2. (ii)

   For any x∈ℝnx\in\mathbb{R}^{n},

   |  |  |  |
   | --- | --- | --- |
   |  | supφ∈𝒱|∑i=1nai,n​(φ)​xi:n−∫01φ​(α)​qn​(α)​𝑑α|⩽Ln​∫01|qn​(α)|​𝑑α.\sup\_{\varphi\in\mathcal{V}}\left|\sum\_{i=1}^{n}a\_{i,n}(\varphi)x\_{i:n}-\int\_{0}^{1}\varphi(\alpha)q\_{n}(\alpha)d\alpha\right|\leqslant\frac{L}{n}\int\_{0}^{1}|q\_{n}(\alpha)|d\alpha. |  |

###### Proof.

(i) For t∈((i−1)/n,i/n]t\in((i-1)/n,i/n], we have
φn​(t)=n​∫(i−1)/ni/nφ​(s)​𝑑s\varphi\_{n}(t)=n\int\_{(i-1)/n}^{i/n}\varphi(s)ds, the average of φ\varphi on that
interval. For any s∈((i−1)/n,i/n]s\in((i-1)/n,i/n] and Lipschitz φ\varphi,

|  |  |  |
| --- | --- | --- |
|  | |φ​(s)−φ​(t)|⩽L​|s−t|⩽L/n.|\varphi(s)-\varphi(t)|\leqslant L|s-t|\leqslant L/n. |  |

Thus |φn​(t)−φ​(t)|⩽L/n|\varphi\_{n}(t)-\varphi(t)|\leqslant L/n, uniformly in tt and φ∈𝒱\varphi\in\mathcal{V}.

(ii) By Lemma [6.5](https://arxiv.org/html/2602.00784v1#S6.Thmtheorem5 "Lemma 6.5 (Integral correspondence). ‣ 6.3. Step approximations and the spectral-estimator correspondence ‣ 6. Spectral risk measures and hyperfinite L-statistics ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"),
∑i=1nai,n​(φ)​xi:n=∫01φn​(α)​qn​(α)​𝑑α\sum\_{i=1}^{n}a\_{i,n}(\varphi)x\_{i:n}=\int\_{0}^{1}\varphi\_{n}(\alpha)q\_{n}(\alpha)d\alpha.
Thus

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∑i=1nai,n​(φ)​xi:n−∫01φ​(α)​qn​(α)​𝑑α|\displaystyle\left|\sum\_{i=1}^{n}a\_{i,n}(\varphi)x\_{i:n}-\int\_{0}^{1}\varphi(\alpha)q\_{n}(\alpha)d\alpha\right| | =|∫01(φn−φ)​qn​𝑑α|\displaystyle=\left|\int\_{0}^{1}(\varphi\_{n}-\varphi)q\_{n}\,d\alpha\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽‖φn−φ‖∞​∫01|qn|\displaystyle\leqslant\|\varphi\_{n}-\varphi\|\_{\infty}\int\_{0}^{1}|q\_{n}| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽Ln​∫01|qn|.∎\displaystyle\leqslant\frac{L}{n}\int\_{0}^{1}|q\_{n}|.\qed |  |

###### Theorem 7.6 (Uniform spectral plug-in consistency).

Let 𝒱\mathcal{V} be a Lipschitz spectral class with constants (C,L)(C,L). Let X∈L1X\in L^{1}
and (Xi)(X\_{i}) be i.i.d. with law XX. Then

|  |  |  |  |
| --- | --- | --- | --- |
| (23) |  | supφ∈𝒱|ρ^n,φ​(X1,…,Xn)−ρφ​(X)|→n→∞a.s.0.\sup\_{\varphi\in\mathcal{V}}\left|\hat{\rho}\_{n,\varphi}(X\_{1},\ldots,X\_{n})-\rho\_{\varphi}(X)\right|\xrightarrow[n\to\infty]{\mathrm{a.s.}}0. |  |

(The uniformity is over spectra φ∈𝒱\varphi\in\mathcal{V} for a fixed underlying law of XX.)

###### Proof.

Let qn​(α):=X⌈n​α⌉:nq\_{n}(\alpha):=X\_{\lceil n\alpha\rceil:n} be the empirical quantile function and let qXq\_{X} be the
population lower quantile. For each φ∈𝒱\varphi\in\mathcal{V}, write φn\varphi\_{n} for the step function
associated with the canonical weights (Definitions [6.2](https://arxiv.org/html/2602.00784v1#S6.Thmtheorem2 "Definition 6.2 (Canonical spectral plug-in estimator). ‣ 6.2. Canonical spectral plug-in estimators ‣ 6. Spectral risk measures and hyperfinite L-statistics ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") and [6.4](https://arxiv.org/html/2602.00784v1#S6.Thmtheorem4 "Definition 6.4 (Associated step function). ‣ 6.3. Step approximations and the spectral-estimator correspondence ‣ 6. Spectral risk measures and hyperfinite L-statistics ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")).
By Lemma [6.5](https://arxiv.org/html/2602.00784v1#S6.Thmtheorem5 "Lemma 6.5 (Integral correspondence). ‣ 6.3. Step approximations and the spectral-estimator correspondence ‣ 6. Spectral risk measures and hyperfinite L-statistics ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"),

|  |  |  |
| --- | --- | --- |
|  | ρ^n,φ​(X1,…,Xn)=−∫01φn​(α)​qn​(α)​𝑑α,ρφ​(X)=−∫01φ​(α)​qX​(α)​𝑑α.\hat{\rho}\_{n,\varphi}(X\_{1},\ldots,X\_{n})=-\int\_{0}^{1}\varphi\_{n}(\alpha)\,q\_{n}(\alpha)\,d\alpha,\qquad\rho\_{\varphi}(X)=-\int\_{0}^{1}\varphi(\alpha)\,q\_{X}(\alpha)\,d\alpha. |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | supφ∈𝒱|ρ^n,φ​(X1,…,Xn)−ρφ​(X)|\displaystyle\sup\_{\varphi\in\mathcal{V}}\left|\hat{\rho}\_{n,\varphi}(X\_{1},\ldots,X\_{n})-\rho\_{\varphi}(X)\right| | ⩽supφ∈𝒱|∫01(φn−φ)​qn​𝑑α|+supφ∈𝒱|∫01φ​(qn−qX)​𝑑α|.\displaystyle\leqslant\sup\_{\varphi\in\mathcal{V}}\left|\int\_{0}^{1}(\varphi\_{n}-\varphi)\,q\_{n}\,d\alpha\right|+\sup\_{\varphi\in\mathcal{V}}\left|\int\_{0}^{1}\varphi\,(q\_{n}-q\_{X})\,d\alpha\right|. |  |

For the first term, Lemma [7.5](https://arxiv.org/html/2602.00784v1#S7.Thmtheorem5 "Lemma 7.5 (Uniform discretisation bound). ‣ 7.3. Uniform consistency over Lipschitz spectral classes ‣ 7. Spectral plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")(i) yields

|  |  |  |
| --- | --- | --- |
|  | supφ∈𝒱|∫01(φn−φ)​qn​𝑑α|⩽Ln​∫01|qn​(α)|​𝑑α=Ln⋅1n​∑i=1n|Xi|.\sup\_{\varphi\in\mathcal{V}}\left|\int\_{0}^{1}(\varphi\_{n}-\varphi)\,q\_{n}\,d\alpha\right|\leqslant\frac{L}{n}\int\_{0}^{1}|q\_{n}(\alpha)|\,d\alpha=\frac{L}{n}\cdot\frac{1}{n}\sum\_{i=1}^{n}|X\_{i}|. |  |

By the strong law, 1n​∑i=1n|Xi|→𝖤​|X|\frac{1}{n}\sum\_{i=1}^{n}|X\_{i}|\to\mathsf{E}|X| almost surely, so this term tends to 0
almost surely.

For the second term, boundedness of the class gives

|  |  |  |
| --- | --- | --- |
|  | supφ∈𝒱|∫01φ​(qn−qX)​𝑑α|⩽supφ∈𝒱‖φ‖∞​∫01|qn−qX|⩽C​∫01|qn−qX|.\sup\_{\varphi\in\mathcal{V}}\left|\int\_{0}^{1}\varphi\,(q\_{n}-q\_{X})\,d\alpha\right|\leqslant\sup\_{\varphi\in\mathcal{V}}\|\varphi\|\_{\infty}\int\_{0}^{1}|q\_{n}-q\_{X}|\leqslant C\int\_{0}^{1}|q\_{n}-q\_{X}|. |  |

It remains to show ∫01|qn−qX|​𝑑α→0\int\_{0}^{1}|q\_{n}-q\_{X}|\,d\alpha\to 0 almost surely when X∈L1X\in L^{1}.
By Glivenko–Cantelli, qn​(α)→qX​(α)q\_{n}(\alpha)\to q\_{X}(\alpha) at continuity points of qXq\_{X}, hence almost everywhere.
Fix M>0M>0 and define truncations qn(M)q\_{n}^{(M)} and qX(M)q\_{X}^{(M)} by clamping to [−M,M][-M,M].
Then qn(M)→qX(M)q\_{n}^{(M)}\to q\_{X}^{(M)} almost everywhere and |qn(M)−qX(M)|⩽2​M|q\_{n}^{(M)}-q\_{X}^{(M)}|\leqslant 2M, so dominated
convergence gives ∫01|qn(M)−qX(M)|​𝑑α→0\int\_{0}^{1}|q\_{n}^{(M)}-q\_{X}^{(M)}|\,d\alpha\to 0 almost surely for fixed MM.
Moreover,

|  |  |  |
| --- | --- | --- |
|  | ∫01|qn−qX|⩽∫01|qn−qn(M)|+∫01|qn(M)−qX(M)|+∫01|qX(M)−qX|.\int\_{0}^{1}|q\_{n}-q\_{X}|\leqslant\int\_{0}^{1}|q\_{n}-q\_{n}^{(M)}|+\int\_{0}^{1}|q\_{n}^{(M)}-q\_{X}^{(M)}|+\int\_{0}^{1}|q\_{X}^{(M)}-q\_{X}|. |  |

The middle term vanishes as n→∞n\to\infty. Since X∈L1X\in L^{1}, we have qX∈L1​(0,1)q\_{X}\in L^{1}(0,1), so
∫01|qX(M)−qX|→0\int\_{0}^{1}|q\_{X}^{(M)}-q\_{X}|\to 0 as M→∞M\to\infty. Finally,

|  |  |  |
| --- | --- | --- |
|  | ∫01|qn​(α)|​ 1{|qn​(α)|>M}​𝑑α=1n​∑i=1n|Xi|​ 1{|Xi|>M}⟶𝖤​[|X|​ 1{|X|>M}]\int\_{0}^{1}|q\_{n}(\alpha)|\,\mathbf{1}\_{\{|q\_{n}(\alpha)|>M\}}\,d\alpha=\frac{1}{n}\sum\_{i=1}^{n}|X\_{i}|\,\mathbf{1}\_{\{|X\_{i}|>M\}}\longrightarrow\mathsf{E}[|X|\,\mathbf{1}\_{\{|X|>M\}}] |  |

almost surely by the strong law, and the limit tends to 0 as M→∞M\to\infty.
Thus ∫01|qn−qX|→0\int\_{0}^{1}|q\_{n}-q\_{X}|\to 0 almost surely, and the second term tends to 0 almost surely as well.

Combining the two bounds proves ([23](https://arxiv.org/html/2602.00784v1#S7.E23 "In Theorem 7.6 (Uniform spectral plug-in consistency). ‣ 7.3. Uniform consistency over Lipschitz spectral classes ‣ 7. Spectral plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")).
∎

###### Remark 7.7.

Theorem [7.6](https://arxiv.org/html/2602.00784v1#S7.Thmtheorem6 "Theorem 7.6 (Uniform spectral plug-in consistency). ‣ 7.3. Uniform consistency over Lipschitz spectral classes ‣ 7. Spectral plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") requires spectra in the *Lipschitz* class 𝒱\mathcal{V}.
This covers distortion risk measures and spectral measures with smooth weights, but does
not cover the Expected Shortfall spectrum φα​(u)=α−1​𝟏(0,α]​(u)\varphi\_{\alpha}(u)=\alpha^{-1}\mathbf{1}\_{(0,\alpha]}(u),
which is bounded but not Lipschitz (it has a jump discontinuity at u=αu=\alpha).

For ES specifically, one can prove consistency by a direct argument exploiting the explicit
formula ESα=−1α​∫0αq​(u)​𝑑u\operatorname{ES}\_{\alpha}=-\frac{1}{\alpha}\int\_{0}^{\alpha}q(u)\,du and Glivenko–Cantelli, but the
*uniform* rate over α∈[δ,1]\alpha\in[\delta,1] requires additional care; see [[7](https://arxiv.org/html/2602.00784v1#bib.bib7)]
for sharp uniform results on ES estimation.

###### Corollary 7.8.

Under the conditions of Theorem [7.6](https://arxiv.org/html/2602.00784v1#S7.Thmtheorem6 "Theorem 7.6 (Uniform spectral plug-in consistency). ‣ 7.3. Uniform consistency over Lipschitz spectral classes ‣ 7. Spectral plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), assume additionally that
𝖤​[|X|2+η]<∞\mathsf{E}[|X|^{2+\eta}]<\infty for some η>0\eta>0. Then

|  |  |  |
| --- | --- | --- |
|  | supφ∈𝒱|ρ^n,φ​(X1,…,Xn)−ρφ​(X)|=O𝖯​(1n).\sup\_{\varphi\in\mathcal{V}}\left|\hat{\rho}\_{n,\varphi}(X\_{1},\ldots,X\_{n})-\rho\_{\varphi}(X)\right|=O\_{\mathsf{P}}\!\left(\frac{1}{\sqrt{n}}\right). |  |

If, in addition, XX is almost surely bounded and the distribution function FF is continuous, then

|  |  |  |
| --- | --- | --- |
|  | supφ∈𝒱|ρ^n,φ​(X1,…,Xn)−ρφ​(X)|=O​(log⁡log⁡nn)almost surely.\sup\_{\varphi\in\mathcal{V}}\left|\hat{\rho}\_{n,\varphi}(X\_{1},\ldots,X\_{n})-\rho\_{\varphi}(X)\right|=O\!\left(\sqrt{\frac{\log\log n}{n}}\right)\quad\text{almost surely.} |  |

###### Proof.

From the proof of Theorem [7.6](https://arxiv.org/html/2602.00784v1#S7.Thmtheorem6 "Theorem 7.6 (Uniform spectral plug-in consistency). ‣ 7.3. Uniform consistency over Lipschitz spectral classes ‣ 7. Spectral plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") we have
supφ∈𝒱|ρ^n,φ−ρφ​(X)|⩽An+Bn\sup\_{\varphi\in\mathcal{V}}|\hat{\rho}\_{n,\varphi}-\rho\_{\varphi}(X)|\leqslant A\_{n}+B\_{n} with

|  |  |  |
| --- | --- | --- |
|  | An⩽Ln​∫01|qn​(α)|​𝑑α=Ln⋅1n​∑i=1n|Xi|andBn⩽C​∫01|qn​(α)−qX​(α)|​𝑑α=C​W1​(μ^n,μ).A\_{n}\leqslant\frac{L}{n}\int\_{0}^{1}|q\_{n}(\alpha)|\,d\alpha=\frac{L}{n}\cdot\frac{1}{n}\sum\_{i=1}^{n}|X\_{i}|\quad\text{and}\quad B\_{n}\leqslant C\int\_{0}^{1}|q\_{n}(\alpha)-q\_{X}(\alpha)|\,d\alpha=C\,W\_{1}(\hat{\mu}\_{n},\mu). |  |

(The quantile formula W1​(μ^n,μ)=∫01|qn−qX|W\_{1}(\hat{\mu}\_{n},\mu)=\int\_{0}^{1}|q\_{n}-q\_{X}| holds whenever both measures have
finite first moments—guaranteed here by X∈L1X\in L^{1} from Theorem [7.6](https://arxiv.org/html/2602.00784v1#S7.Thmtheorem6 "Theorem 7.6 (Uniform spectral plug-in consistency). ‣ 7.3. Uniform consistency over Lipschitz spectral classes ‣ 7. Spectral plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics");
see, e.g., [[20](https://arxiv.org/html/2602.00784v1#bib.bib20), Theorem 2.18].)
Thus An=O​(n−1)A\_{n}=O(n^{-1}) almost surely by the strong law.

For the stochastic term, the one-dimensional identity
W1​(μ^n,μ)=∫ℝ|Fn​(x)−F​(x)|​𝑑xW\_{1}(\hat{\mu}\_{n},\mu)=\int\_{\mathbb{R}}|F\_{n}(x)-F(x)|\,dx (again [[20](https://arxiv.org/html/2602.00784v1#bib.bib20)]) converts
the quantile integral to a CDF integral.
For each fixed xx, conditional on F​(x)F(x) we have Fn​(x)=1n​Bin​(n,F​(x))F\_{n}(x)=\frac{1}{n}\mathrm{Bin}(n,F(x)), hence
𝖤​|Fn​(x)−F​(x)|⩽𝖵𝖺𝗋⁡(Fn​(x))=F​(x)​(1−F​(x))/n\mathsf{E}|F\_{n}(x)-F(x)|\leqslant\sqrt{\operatorname{\mathsf{Var}}(F\_{n}(x))}=\sqrt{F(x)(1-F(x))/n}.
By the Fubini theorem and Jensen’s inequality,

|  |  |  |
| --- | --- | --- |
|  | 𝖤​W1​(μ^n,μ)⩽1n​∫ℝF​(x)​(1−F​(x))​𝑑x.\mathsf{E}\,W\_{1}(\hat{\mu}\_{n},\mu)\leqslant\frac{1}{\sqrt{n}}\int\_{\mathbb{R}}\sqrt{F(x)(1-F(x))}\,dx. |  |

The integral is finite under 𝖤​|X|2+η<∞\mathsf{E}|X|^{2+\eta}<\infty. Indeed, for x⩾1x\geqslant 1,

|  |  |  |
| --- | --- | --- |
|  | 1−F​(x)=𝖯​(X>x)⩽𝖤​|X|2+ηx2+η1-F(x)=\mathsf{P}(X>x)\leqslant\frac{\mathsf{E}|X|^{2+\eta}}{x^{2+\eta}} |  |

by Markov’s inequality, and hence

|  |  |  |
| --- | --- | --- |
|  | F​(x)​(1−F​(x))⩽1−F​(x)⩽𝖤​|X|2+η​x−(1+η/2).\sqrt{F(x)(1-F(x))}\leqslant\sqrt{1-F(x)}\leqslant\sqrt{\mathsf{E}|X|^{2+\eta}}\,x^{-(1+\eta/2)}. |  |

Since η>0\eta>0, the function x↦x−(1+η/2)x\mapsto x^{-(1+\eta/2)} is integrable on [1,∞)[1,\infty).
A symmetric argument for x⩽−1x\leqslant-1 (using 𝖯​(X⩽x)=𝖯​(−X⩾−x)\mathsf{P}(X\leqslant x)=\mathsf{P}(-X\geqslant-x)) yields integrability
on (−∞,−1](-\infty,-1], and integrability on [−1,1][-1,1] is trivial because F​(1−F)⩽1/2\sqrt{F(1-F)}\leqslant 1/2.
Therefore ∫ℝF​(x)​(1−F​(x))​𝑑x<∞\int\_{\mathbb{R}}\sqrt{F(x)(1-F(x))}\,dx<\infty.

Hence 𝖤​W1​(μ^n,μ)=O​(n−1/2)\mathsf{E}W\_{1}(\hat{\mu}\_{n},\mu)=O(n^{-1/2}), and Markov’s inequality yields
W1​(μ^n,μ)=O𝖯​(n−1/2)W\_{1}(\hat{\mu}\_{n},\mu)=O\_{\mathsf{P}}(n^{-1/2}). (This rate is standard in the 1D empirical Wasserstein
literature; see, e.g., [[5](https://arxiv.org/html/2602.00784v1#bib.bib5)] for optimal moment conditions.)
Hence Bn=O𝖯​(n−1/2)B\_{n}=O\_{\mathsf{P}}(n^{-1/2}), and the first claim follows.

If XX is bounded and FF is continuous, then the probability integral transform and the law of the
iterated logarithm for the uniform empirical process give
supx|Fn​(x)−F​(x)|=O​(log⁡log⁡n/n)\sup\_{x}|F\_{n}(x)-F(x)|=O(\sqrt{\log\log n/n}) almost surely; see, e.g., [[19](https://arxiv.org/html/2602.00784v1#bib.bib19)].
Since XX is bounded, W1​(μ^n,μ)=∫ℝ|Fn−F|​𝑑xW\_{1}(\hat{\mu}\_{n},\mu)=\int\_{\mathbb{R}}|F\_{n}-F|\,dx is bounded by
diam​(supp​(X))​supx|Fn​(x)−F​(x)|\mathrm{diam}(\mathrm{supp}(X))\sup\_{x}|F\_{n}(x)-F(x)|, giving the stated almost sure rate.
∎

###### Remark 7.9.

From the hyperfinite viewpoint, Theorem [7.6](https://arxiv.org/html/2602.00784v1#S7.Thmtheorem6 "Theorem 7.6 (Uniform spectral plug-in consistency). ‣ 7.3. Uniform consistency over Lipschitz spectral classes ‣ 7. Spectral plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") reflects the fact that
one can work *internally* with the entire class 𝒱\mathcal{V} at once. The Lipschitz
condition provides a deterministic envelope bounding the discretisation error uniformly,
whilst the Loeb-measure quantile convergence handles the stochastic approximation
uniformly over all bounded φ\varphi.

## 8. Kusuoka-type plug-in consistency

We now extend the consistency theory to general law-invariant coherent risk measures via
the Kusuoka representation.

### 8.1. Setup and assumptions

Let ρ:L∞→ℝ\rho:L^{\infty}\to\mathbb{R} be a law-invariant CRM on an atomless space with Kusuoka
representation ([3](https://arxiv.org/html/2602.00784v1#S2.E3 "In Theorem 2.5 (Kusuoka representation [14]). ‣ 2.2. Law invariance and spectral representation ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")):

|  |  |  |
| --- | --- | --- |
|  | ρ​(X)=supν∈ℳ∫(0,1]ESα⁡(X)​ν​(d​α).\rho(X)=\sup\_{\nu\in\mathcal{M}}\int\_{(0,1]}\operatorname{ES}\_{\alpha}(X)\,\nu(d\alpha). |  |

We construct finite-sample estimators by discretising the Kusuoka integral. Let
(αi,n)i=0n(\alpha\_{i,n})\_{i=0}^{n} be a grid with 0=α0,n<α1,n<⋯<αn,n=10=\alpha\_{0,n}<\alpha\_{1,n}<\cdots<\alpha\_{n,n}=1.
For simplicity, take the uniform grid αi,n=i/n\alpha\_{i,n}=i/n.

Suppose we have, for each α∈(0,1]\alpha\in(0,1], an estimator
ES^α,n:ℝn→ℝ\widehat{\operatorname{ES}}\_{\alpha,n}:\mathbb{R}^{n}\to\mathbb{R} for ESα\operatorname{ES}\_{\alpha}. The *Kusuoka-type plug-in
estimator* is

|  |  |  |  |
| --- | --- | --- | --- |
| (24) |  | ρ^n​(x):=supν∈ℳ∑i=1nES^αi,n,n​(x)​ν​((αi−1,n,αi,n]).\hat{\rho}\_{n}(x):=\sup\_{\nu\in\mathcal{M}}\sum\_{i=1}^{n}\widehat{\operatorname{ES}}\_{\alpha\_{i,n},n}(x)\,\nu((\alpha\_{i-1,n},\alpha\_{i,n}]). |  |

### 8.2. Consistency theorem

###### Theorem 8.1 (Kusuoka plug-in consistency).

Let ρ\rho be a law-invariant CRM with Kusuoka representation ([3](https://arxiv.org/html/2602.00784v1#S2.E3 "In Theorem 2.5 (Kusuoka representation [14]). ‣ 2.2. Law invariance and spectral representation ‣ 2. Coherent risk measures and coherent risk estimators ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")). Assume:

1. (K1)

   (Tightness) For every ε>0\varepsilon>0, there exists δ∈(0,1)\delta\in(0,1)
   such that supν∈ℳν​((0,δ])⩽ε\sup\_{\nu\in\mathcal{M}}\nu((0,\delta])\leqslant\varepsilon.
2. (K2)

   (Uniform ES estimation) For every δ∈(0,1)\delta\in(0,1),

   |  |  |  |
   | --- | --- | --- |
   |  | supα∈[δ,1]|ES^α,n​(X1,…,Xn)−ESα⁡(X)|→n→∞a.s.0\sup\_{\alpha\in[\delta,1]}\left|\widehat{\operatorname{ES}}\_{\alpha,n}(X\_{1},\ldots,X\_{n})-\operatorname{ES}\_{\alpha}(X)\right|\xrightarrow[n\to\infty]{\mathrm{a.s.}}0 |  |

   for any bounded XX and i.i.d. sample (Xi)(X\_{i}) with law XX.
3. (K3)

   (Uniform envelope) There exists C<∞C<\infty such that
   |ES^α,n​(x)|⩽C​‖x‖∞|\widehat{\operatorname{ES}}\_{\alpha,n}(x)|\leqslant C\|x\|\_{\infty} for all α,n,x\alpha,n,x.
4. (K4)

   (Grid refinement) The mesh maxi⁡(αi,n−αi−1,n)→0\max\_{i}(\alpha\_{i,n}-\alpha\_{i-1,n})\to 0
   as n→∞n\to\infty.

Then for any bounded XX and i.i.d. sample (Xi)(X\_{i}),

|  |  |  |  |
| --- | --- | --- | --- |
| (25) |  | ρ^n​(X1,…,Xn)→n→∞a.s.ρ​(X).\hat{\rho}\_{n}(X\_{1},\ldots,X\_{n})\xrightarrow[n\to\infty]{\mathrm{a.s.}}\rho(X). |  |

Assumption (K1) excludes risk measures that put mass arbitrarily close to α=0\alpha=0, which is
necessary because ESα⁡(X)→−∞\operatorname{ES}\_{\alpha}(X)\to-\infty as α↓0\alpha\downarrow 0 for unbounded-below XX,
and discretisation near 0 is unstable. A typical choice for ES^α,n\widehat{\operatorname{ES}}\_{\alpha,n} is
the discrete ES dES⌈n​α⌉/n\mathrm{dES}\_{\lceil n\alpha\rceil/n} from ([13](https://arxiv.org/html/2602.00784v1#S5.E13 "In Definition 5.1 (Discrete expected shortfall). ‣ 5.1. Discrete expected shortfall ‣ 5. Discrete Kusuoka representation for law-invariant CREs ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")), for which (K2)–(K3)
hold; see Theorem [7.2](https://arxiv.org/html/2602.00784v1#S7.Thmtheorem2 "Theorem 7.2 (Spectral L-estimator consistency: a distribution-free criterion). ‣ 7.2. Spectral L-estimator consistency theorem ‣ 7. Spectral plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics").

###### Proof.

Fix a bounded random variable XX and an i.i.d. sample (Xi)i⩾1(X\_{i})\_{i\geqslant 1} with law XX.
For ν∈ℳ\nu\in\mathcal{M} set

|  |  |  |
| --- | --- | --- |
|  | I​(ν):=∫(0,1]ESα⁡(X)​ν​(d​α),I^n​(ν):=∑i=1nES^αi,n,n​(X1,…,Xn)​ν​((αi−1,n,αi,n]).I(\nu):=\int\_{(0,1]}\operatorname{ES}\_{\alpha}(X)\,\nu(d\alpha),\qquad\hat{I}\_{n}(\nu):=\sum\_{i=1}^{n}\widehat{\operatorname{ES}}\_{\alpha\_{i,n},n}(X\_{1},\ldots,X\_{n})\,\nu((\alpha\_{i-1,n},\alpha\_{i,n}]). |  |

Then ρ​(X)=supν∈ℳI​(ν)\rho(X)=\sup\_{\nu\in\mathcal{M}}I(\nu) and ρ^n​(X1,…,Xn)=supν∈ℳI^n​(ν)\hat{\rho}\_{n}(X\_{1},\ldots,X\_{n})=\sup\_{\nu\in\mathcal{M}}\hat{I}\_{n}(\nu).
Since |supνa​(ν)−supνb​(ν)|⩽supν|a​(ν)−b​(ν)||\sup\_{\nu}a(\nu)-\sup\_{\nu}b(\nu)|\leqslant\sup\_{\nu}|a(\nu)-b(\nu)|, it suffices to prove that

|  |  |  |
| --- | --- | --- |
|  | supν∈ℳ|I^n​(ν)−I​(ν)|⟶0almost surely.\sup\_{\nu\in\mathcal{M}}|\hat{I}\_{n}(\nu)-I(\nu)|\longrightarrow 0\qquad\text{almost surely.} |  |

Fix ε>0\varepsilon>0 and choose δ∈(0,1)\delta\in(0,1) such that
supν∈ℳν​((0,δ])⩽ε\sup\_{\nu\in\mathcal{M}}\nu((0,\delta])\leqslant\varepsilon (assumption (K1)).
For each ν∈ℳ\nu\in\mathcal{M}, split

|  |  |  |
| --- | --- | --- |
|  | I(ν)=∫(0,δ]ESα(X)ν(dα)+∫(δ,1]ESα(X)ν(dα)=:I0,δ(ν)+Iδ,1(ν),I(\nu)=\int\_{(0,\delta]}\operatorname{ES}\_{\alpha}(X)\,\nu(d\alpha)+\int\_{(\delta,1]}\operatorname{ES}\_{\alpha}(X)\,\nu(d\alpha)=:I\_{0,\delta}(\nu)+I\_{\delta,1}(\nu), |  |

and split I^n​(ν)\hat{I}\_{n}(\nu) analogously into the terms with αi,n⩽δ\alpha\_{i,n}\leqslant\delta and αi,n>δ\alpha\_{i,n}>\delta:

|  |  |  |
| --- | --- | --- |
|  | I^n​(ν)=∑αi,n⩽δES^αi,n,n​(X1,…,Xn)​ν​((αi−1,n,αi,n])+∑αi,n>δES^αi,n,n(X1,…,Xn)ν((αi−1,n,αi,n])=:I^0,δ,n(ν)+I^δ,1,n(ν).\hat{I}\_{n}(\nu)=\sum\_{\alpha\_{i,n}\leqslant\delta}\widehat{\operatorname{ES}}\_{\alpha\_{i,n},n}(X\_{1},\ldots,X\_{n})\,\nu((\alpha\_{i-1,n},\alpha\_{i,n}])\\ +\sum\_{\alpha\_{i,n}>\delta}\widehat{\operatorname{ES}}\_{\alpha\_{i,n},n}(X\_{1},\ldots,X\_{n})\,\nu((\alpha\_{i-1,n},\alpha\_{i,n}])=:\hat{I}\_{0,\delta,n}(\nu)+\hat{I}\_{\delta,1,n}(\nu). |  |

Because XX is bounded we have |ESα⁡(X)|⩽‖X‖∞|\operatorname{ES}\_{\alpha}(X)|\leqslant\|X\|\_{\infty} for all α∈(0,1]\alpha\in(0,1].
Therefore,

|  |  |  |
| --- | --- | --- |
|  | supν∈ℳ|I0,δ​(ν)|⩽‖X‖∞​supν∈ℳν​((0,δ])⩽‖X‖∞​ε.\sup\_{\nu\in\mathcal{M}}|I\_{0,\delta}(\nu)|\leqslant\|X\|\_{\infty}\sup\_{\nu\in\mathcal{M}}\nu((0,\delta])\leqslant\|X\|\_{\infty}\,\varepsilon. |  |

Moreover, since XX is bounded, ‖(X1,…,Xn)‖∞⩽‖X‖∞\|(X\_{1},\ldots,X\_{n})\|\_{\infty}\leqslant\|X\|\_{\infty} almost surely, and
assumption (K3) yields |ES^α,n​(X1,…,Xn)|⩽C​‖X‖∞|\widehat{\operatorname{ES}}\_{\alpha,n}(X\_{1},\ldots,X\_{n})|\leqslant C\|X\|\_{\infty} for all α,n\alpha,n
on an almost sure event. Hence,

|  |  |  |
| --- | --- | --- |
|  | supν∈ℳ|I^0,δ,n​(ν)|⩽C​‖X‖∞​supν∈ℳν​((0,δ])⩽C​‖X‖∞​εalmost surely.\sup\_{\nu\in\mathcal{M}}|\hat{I}\_{0,\delta,n}(\nu)|\leqslant C\|X\|\_{\infty}\sup\_{\nu\in\mathcal{M}}\nu((0,\delta])\leqslant C\|X\|\_{\infty}\,\varepsilon\qquad\text{almost surely.} |  |

Combining these two bounds gives

|  |  |  |
| --- | --- | --- |
|  | supν∈ℳ|I^0,δ,n​(ν)−I0,δ​(ν)|⩽(1+C)​‖X‖∞​εalmost surely.\sup\_{\nu\in\mathcal{M}}\bigl|\hat{I}\_{0,\delta,n}(\nu)-I\_{0,\delta}(\nu)\bigr|\leqslant(1+C)\|X\|\_{\infty}\,\varepsilon\qquad\text{almost surely.} |  |

It remains to control the contribution from (δ,1](\delta,1]. Write

|  |  |  |  |
| --- | --- | --- | --- |
|  | I^δ,1,n​(ν)−Iδ,1​(ν)\displaystyle\hat{I}\_{\delta,1,n}(\nu)-I\_{\delta,1}(\nu) | =∑αi,n>δ(ES^αi,n,n​(X1,…,Xn)−ESαi,n⁡(X))​ν​((αi−1,n,αi,n])\displaystyle=\sum\_{\alpha\_{i,n}>\delta}\Big(\widehat{\operatorname{ES}}\_{\alpha\_{i,n},n}(X\_{1},\ldots,X\_{n})-\operatorname{ES}\_{\alpha\_{i,n}}(X)\Big)\,\nu((\alpha\_{i-1,n},\alpha\_{i,n}]) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑αi,n>δESαi,n⁡(X)​ν​((αi−1,n,αi,n])−∫(δ,1]ESα⁡(X)​ν​(d​α).\displaystyle\quad+\sum\_{\alpha\_{i,n}>\delta}\operatorname{ES}\_{\alpha\_{i,n}}(X)\,\nu((\alpha\_{i-1,n},\alpha\_{i,n}])-\int\_{(\delta,1]}\operatorname{ES}\_{\alpha}(X)\,\nu(d\alpha). |  |

For the first term we simply use ν​((δ,1])⩽1\nu((\delta,1])\leqslant 1 and assumption (K2):

|  |  |  |
| --- | --- | --- |
|  | supν∈ℳ|∑αi,n>δ(ES^αi,n,n​(X1,…,Xn)−ESαi,n⁡(X))​ν​((αi−1,n,αi,n])|⩽supα∈[δ,1]|ES^α,n​(X1,…,Xn)−ESα⁡(X)|⟶0\sup\_{\nu\in\mathcal{M}}\left|\sum\_{\alpha\_{i,n}>\delta}\Big(\widehat{\operatorname{ES}}\_{\alpha\_{i,n},n}(X\_{1},\ldots,X\_{n})-\operatorname{ES}\_{\alpha\_{i,n}}(X)\Big)\,\nu((\alpha\_{i-1,n},\alpha\_{i,n}])\right|\\ \leqslant\sup\_{\alpha\in[\delta,1]}\left|\widehat{\operatorname{ES}}\_{\alpha,n}(X\_{1},\ldots,X\_{n})-\operatorname{ES}\_{\alpha}(X)\right|\longrightarrow 0 |  |

almost surely.

For the second term, define g​(α):=ESα⁡(X)g(\alpha):=\operatorname{ES}\_{\alpha}(X) on [δ,1][\delta,1].
Since XX is bounded, qXq\_{X} is bounded, so α↦∫0αqX​(u)​𝑑u\alpha\mapsto\int\_{0}^{\alpha}q\_{X}(u)\,du is continuous
and therefore g​(α)=−(1/α)​∫0αqX​(u)​𝑑ug(\alpha)=-(1/\alpha)\int\_{0}^{\alpha}q\_{X}(u)\,du is continuous on [δ,1][\delta,1].
By compactness, gg is uniformly continuous on [δ,1][\delta,1]. Let ωg​(h)\omega\_{g}(h) denote its modulus
of continuity:

|  |  |  |
| --- | --- | --- |
|  | ωg(h):=sup{|g(α)−g(β)|:α,β∈[δ,1],|α−β|⩽h}.\omega\_{g}(h):=\sup\{|g(\alpha)-g(\beta)|:\ \alpha,\beta\in[\delta,1],\ |\alpha-\beta|\leqslant h\}. |  |

Let Δn:=maxi⁡(αi,n−αi−1,n)\Delta\_{n}:=\max\_{i}(\alpha\_{i,n}-\alpha\_{i-1,n}), which tends to 0 by (K4).
Then, for every ν∈ℳ\nu\in\mathcal{M},

|  |  |  |
| --- | --- | --- |
|  | |∑αi,n>δESαi,n⁡(X)​ν​((αi−1,n,αi,n])−∫(δ,1]ESα⁡(X)​ν​(d​α)|\displaystyle\left|\sum\_{\alpha\_{i,n}>\delta}\operatorname{ES}\_{\alpha\_{i,n}}(X)\,\nu((\alpha\_{i-1,n},\alpha\_{i,n}])-\int\_{(\delta,1]}\operatorname{ES}\_{\alpha}(X)\,\nu(d\alpha)\right| |  |
|  |  |  |
| --- | --- | --- |
|  | =|∑αi,n>δ∫(αi−1,n,αi,n](g​(αi,n)−g​(α))​ν​(d​α)|\displaystyle\qquad=\left|\sum\_{\alpha\_{i,n}>\delta}\int\_{(\alpha\_{i-1,n},\alpha\_{i,n}]}\bigl(g(\alpha\_{i,n})-g(\alpha)\bigr)\,\nu(d\alpha)\right| |  |
|  |  |  |
| --- | --- | --- |
|  | ⩽∑αi,n>δ∫(αi−1,n,αi,n]ωg​(Δn)​ν​(d​α)⩽ωg​(Δn).\displaystyle\qquad\leqslant\sum\_{\alpha\_{i,n}>\delta}\int\_{(\alpha\_{i-1,n},\alpha\_{i,n}]}\omega\_{g}(\Delta\_{n})\,\nu(d\alpha)\leqslant\omega\_{g}(\Delta\_{n}). |  |

This bound is uniform in ν\nu, and ωg​(Δn)→0\omega\_{g}(\Delta\_{n})\to 0 as n→∞n\to\infty.

Putting everything together, we obtain on an almost sure event:

|  |  |  |
| --- | --- | --- |
|  | lim supn→∞supν∈ℳ|I^n​(ν)−I​(ν)|⩽(1+C)​‖X‖∞​ε.\limsup\_{n\to\infty}\sup\_{\nu\in\mathcal{M}}|\hat{I}\_{n}(\nu)-I(\nu)|\leqslant(1+C)\|X\|\_{\infty}\,\varepsilon. |  |

Since ε>0\varepsilon>0 is arbitrary,
supν∈ℳ|I^n​(ν)−I​(ν)|→0\sup\_{\nu\in\mathcal{M}}|\hat{I}\_{n}(\nu)-I(\nu)|\to 0 almost surely, we conclude convergence
ρ^n​(X1,…,Xn)→ρ​(X)\hat{\rho}\_{n}(X\_{1},\ldots,X\_{n})\to\rho(X) a.s.
∎

## 9. Hyperfinite bootstrap validity

We establish bootstrap validity by exploiting the internal nature of the resampling procedure.
In the hyperfinite framework, the bootstrap distribution is simply the internal distribution
of the statistic conditional on the hyperfinite sample.

### 9.1. Internal bootstrap construction

Let (X1,…,XN)(X\_{1},\dots,X\_{N}) be a hyperfinite sample with infinite N∈ℕ∗N\in{}^{\*}\mathbb{N}.
The empirical measure is 𝖯^N=1N​∑k=1NδXk\hat{\mathsf{P}}\_{N}=\frac{1}{N}\sum\_{k=1}^{N}\delta\_{X\_{k}}.

Introduce an internal i.i.d. sequence (U1,…,UN)(U\_{1},\dots,U\_{N}), independent of (X1,…,XN)(X\_{1},\dots,X\_{N}),
with each UiU\_{i} uniformly distributed on IN={1,…,N}I\_{N}=\{1,\dots,N\} (counting law μN\mu\_{N}). Define the
*hyperfinite bootstrap sample* by

|  |  |  |
| --- | --- | --- |
|  | Xi∗:=XUi,i=1,…,N.X\_{i}^{\*}:=X\_{U\_{i}},\qquad i=1,\dots,N. |  |

Then (X1∗,…,XN∗)(X\_{1}^{\*},\dots,X\_{N}^{\*}) is internal and i.i.d. with law 𝖯^N\hat{\mathsf{P}}\_{N}, and
conditional-on-sample statements are interpreted as statements under the bootstrap-index
randomness (Ui)(U\_{i}) with (Xi)(X\_{i}) held fixed. This construction makes the internal conditional
law explicit: it is simply the pushforward of the internal product counting law of (Ui)(U\_{i}).

By the star-suppression convention (Notation [3.2](https://arxiv.org/html/2602.00784v1#S3.Thmtheorem2 "Notation 3.2 (Standing Loeb model). ‣ 3.1. Standing conventions and the Loeb model ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")), the mapping
(n,x)↦ρ^n,φ​(x)(n,x)\mapsto\hat{\rho}\_{n,\varphi}(x) extends internally to hypernatural NN, giving
the internal statistic ρ^N,φ\hat{\rho}\_{N,\varphi}.
Let ρ^N:=ρ^N,φ​(X1,…,XN)\hat{\rho}\_{N}:=\hat{\rho}\_{N,\varphi}(X\_{1},\dots,X\_{N}) be the estimator on the original sample,
and ρ^N∗:=ρ^N,φ​(X1∗,…,XN∗)\hat{\rho}\_{N}^{\*}:=\hat{\rho}\_{N,\varphi}(X\_{1}^{\*},\dots,X\_{N}^{\*}) be the estimator on the bootstrap sample.

We measure closeness of laws using the Kolmogorov distance. For standard probability measures,

|  |  |  |
| --- | --- | --- |
|  | dK​(ℒ​(Y),ℒ​(Z)):=supt∈ℝ|𝖯​(Y⩽t)−𝖯​(Z⩽t)|.d\_{K}(\mathcal{L}(Y),\mathcal{L}(Z)):=\sup\_{t\in\mathbb{R}}\big|\mathsf{P}(Y\leqslant t)-\mathsf{P}(Z\leqslant t)\big|. |  |

In the hyperfinite setting, we must be careful about internality. For m∈ℕ∗m\in{}^{\*}\mathbb{N}, define the
*internal truncated Kolmogorov distance*

|  |  |  |
| --- | --- | --- |
|  | dK,m​(ℒ​(Y),ℒ​(Z)):=maxt∈{−m,−m+1/m,…,m}⁡|𝖯∗​(Y⩽t)−𝖯∗​(Z⩽t)|.d\_{K,m}(\mathcal{L}(Y),\mathcal{L}(Z)):=\max\_{t\in\{-m,-m+1/m,\dots,m\}}\big|{}^{\*}\mathsf{P}(Y\leqslant t)-{}^{\*}\mathsf{P}(Z\leqslant t)\big|. |  |

This is internal (a maximum over an internal hyperfinite grid).

###### Lemma 9.1 (Internal Kolmogorov distance approximation).

Let YY be a finite ℝ∗{}^{\*}\mathbb{R}-valued random variable on (Ω∗,L​(𝖯∗))({}^{\*}\Omega,L({}^{\*}\mathsf{P})), and let μ\mu be a standard probability measure on ℝ\mathbb{R} with continuous CDF GG.
For m∈ℕ∗m\in{}^{\*}\mathbb{N} define

|  |  |  |
| --- | --- | --- |
|  | dK,m​(ℒ∗​(Y),μ):=maxt∈{−m,−m+1/m,…,m}⁡|ℒ∗​(Y)​((−∞,t])−G​(t)|.d\_{K,m}(\mathcal{L}^{\*}(Y),\mu):=\max\_{t\in\{-m,-m+1/m,\dots,m\}}\left|\mathcal{L}^{\*}(Y)((-\infty,t])-G(t)\right|. |  |

1. (i)

   If there exists an infinite m∈ℕ∗m\in{}^{\*}\mathbb{N} such that dK,m​(ℒ∗​(Y),μ)≈0d\_{K,m}(\mathcal{L}^{\*}(Y),\mu)\approx 0, then

   |  |  |  |
   | --- | --- | --- |
   |  | dK​(ℒ​(st⁡(Y)),μ)=0.d\_{K}(\mathcal{L}(\operatorname{st}(Y)),\mu)=0. |  |
2. (ii)

   The event {dK,m​(ℒ∗​(Y∣X),μ)>ε}\{d\_{K,m}(\mathcal{L}^{\*}(Y\mid X),\mu)>\varepsilon\} is internal for each internal m∈ℕ∗m\in{}^{\*}\mathbb{N} and each standard ε>0\varepsilon>0, hence Loeb measurable.

###### Proof.

(i) Fix an infinite m∈ℕ∗m\in{}^{\*}\mathbb{N} with dK,m​(ℒ∗​(Y),μ)≈0d\_{K,m}(\mathcal{L}^{\*}(Y),\mu)\approx 0 and write Δ:=1/m\Delta:=1/m.
Let t∈ℝt\in\mathbb{R} be standard and let η>0\eta>0 be standard.
Since mm is infinite, we have t,t+η∈(−m,m)t,t+\eta\in(-m,m).
Choose gridpoints s,s′∈{−m,−m+1/m,…,m}s,s^{\prime}\in\{-m,-m+1/m,\dots,m\} such that

|  |  |  |
| --- | --- | --- |
|  | s⩽t<s+Δ,s′⩽t+η<s′+Δ.s\leqslant t<s+\Delta,\qquad s^{\prime}\leqslant t+\eta<s^{\prime}+\Delta. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | {Y⩽s}⊆{st⁡(Y)⩽t}⊆{Y⩽t+η}⊆{Y⩽s′+Δ}.\{Y\leqslant s\}\subseteq\{\operatorname{st}(Y)\leqslant t\}\subseteq\{Y\leqslant t+\eta\}\subseteq\{Y\leqslant s^{\prime}+\Delta\}. |  |

Taking Loeb probabilities and using L​(𝖯∗)​(A)=st⁡(𝖯∗​(A))L({}^{\*}\mathsf{P})(A)=\operatorname{st}({}^{\*}\mathsf{P}(A)) for internal AA gives

|  |  |  |
| --- | --- | --- |
|  | st⁡(𝖯∗​(Y⩽s))⩽L​(𝖯∗)​(st⁡(Y)⩽t)⩽st⁡(𝖯∗​(Y⩽s′+Δ)).\operatorname{st}({}^{\*}\mathsf{P}(Y\leqslant s))\leqslant L({}^{\*}\mathsf{P})(\operatorname{st}(Y)\leqslant t)\leqslant\operatorname{st}({}^{\*}\mathsf{P}(Y\leqslant s^{\prime}+\Delta)). |  |

By the definition of dK,md\_{K,m},

|  |  |  |
| --- | --- | --- |
|  | |𝖯∗​(Y⩽s)−G​(s)|⩽dK,m​(ℒ∗​(Y),μ)≈0,\big|{}^{\*}\mathsf{P}(Y\leqslant s)-G(s)\big|\leqslant d\_{K,m}(\mathcal{L}^{\*}(Y),\mu)\approx 0, |  |

and

|  |  |  |
| --- | --- | --- |
|  | |𝖯∗​(Y⩽s′+Δ)−G​(s′+Δ)|⩽dK,m​(ℒ∗​(Y),μ)≈0.\big|{}^{\*}\mathsf{P}(Y\leqslant s^{\prime}+\Delta)-G(s^{\prime}+\Delta)\big|\leqslant d\_{K,m}(\mathcal{L}^{\*}(Y),\mu)\approx 0. |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | st⁡(G​(s))⩽L​(𝖯∗)​(st⁡(Y)⩽t)⩽st⁡(G​(s′+Δ)).\operatorname{st}(G(s))\leqslant L({}^{\*}\mathsf{P})(\operatorname{st}(Y)\leqslant t)\leqslant\operatorname{st}(G(s^{\prime}+\Delta)). |  |

Since s≈ts\approx t and s′+Δ≈t+ηs^{\prime}+\Delta\approx t+\eta and GG is continuous, we have
st⁡(G​(s))=G​(t)\operatorname{st}(G(s))=G(t) and st⁡(G​(s′+Δ))=G​(t+η)\operatorname{st}(G(s^{\prime}+\Delta))=G(t+\eta).
Therefore

|  |  |  |
| --- | --- | --- |
|  | G​(t)⩽L​(𝖯∗)​(st⁡(Y)⩽t)⩽G​(t+η).G(t)\leqslant L({}^{\*}\mathsf{P})(\operatorname{st}(Y)\leqslant t)\leqslant G(t+\eta). |  |

Letting η↓0\eta\downarrow 0 and using continuity of GG yields
L​(𝖯∗)​(st⁡(Y)⩽t)=G​(t)L({}^{\*}\mathsf{P})(\operatorname{st}(Y)\leqslant t)=G(t) for all t∈ℝt\in\mathbb{R}, *i.e.* st⁡(Y)∼μ\operatorname{st}(Y)\sim\mu.

(ii) For fixed internal mm, the grid {−m,−m+1/m,…,m}\{-m,-m+1/m,\dots,m\} is hyperfinite and
dK,md\_{K,m} is a hyperfinite maximum of internal conditional probabilities and standard constants.
Thus {dK,m​(ℒ∗​(Y∣X),μ)>ε}\{d\_{K,m}(\mathcal{L}^{\*}(Y\mid X),\mu)>\varepsilon\} is internal for standard ε>0\varepsilon>0.
∎

### 9.2. Near-standardness of conditional laws

Bootstrap validity requires that the conditional law of N​(ρ^N∗−ρ^N)\sqrt{N}(\hat{\rho}\_{N}^{\*}-\hat{\rho}\_{N})
is infinitely close to the limiting law of N​(ρ^N−ρ​(X))\sqrt{N}(\hat{\rho}\_{N}-\rho(X)).

###### Assumption 9.2 (Bootstrap regularity).

The random variable XX satisfies:

1. (B1)

   FXF\_{X} is continuous;
2. (B2)

   XX has a density fXf\_{X} that is bounded and bounded away from 0 on the interior
   quantile range {qX​(α):α∈[δ,1−δ]}\{q\_{X}(\alpha):\alpha\in[\delta,1-\delta]\} for each fixed δ∈(0,1/2)\delta\in(0,1/2).

Equivalently, (B2) says fXf\_{X} is continuous and strictly positive on every compact subinterval
of the interior of the support of XX.
Under (B1)–(B2), the quantile map F↦qFF\mapsto q\_{F} is Hadamard differentiable at FXF\_{X},
and the spectral functional T​(F)=−∫01qF​(α)​φ​(α)​𝑑αT(F)=-\int\_{0}^{1}q\_{F}(\alpha)\varphi(\alpha)\,d\alpha inherits
Hadamard differentiability; see [[18](https://arxiv.org/html/2602.00784v1#bib.bib18), Lemma 21.3, Thm. 21.5].

###### Lemma 9.3 (Hadamard derivative of the spectral functional).

Under Assumption [9.2](https://arxiv.org/html/2602.00784v1#S9.Thmtheorem2 "Assumption 9.2 (Bootstrap regularity). ‣ 9.2. Near-standardness of conditional laws ‣ 9. Hyperfinite bootstrap validity ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), the spectral functional T​(F)=−∫01qF​(α)​φ​(α)​𝑑αT(F)=-\int\_{0}^{1}q\_{F}(\alpha)\varphi(\alpha)\,d\alpha
is Hadamard differentiable at FXF\_{X} tangentially to C​(ℝ)C(\mathbb{R}), with derivative

|  |  |  |
| --- | --- | --- |
|  | TFX′​(h)=∫01h​(qX​(α))fX​(qX​(α))​φ​(α)​𝑑α.T^{\prime}\_{F\_{X}}(h)=\int\_{0}^{1}\frac{h(q\_{X}(\alpha))}{f\_{X}(q\_{X}(\alpha))}\,\varphi(\alpha)\,d\alpha. |  |

###### Proof.

The quantile functional Q:F↦qF​(α)Q:F\mapsto q\_{F}(\alpha) has Hadamard derivative
QFX′​(h)​(α)=−h​(qX​(α))/fX​(qX​(α))Q^{\prime}\_{F\_{X}}(h)(\alpha)=-h(q\_{X}(\alpha))/f\_{X}(q\_{X}(\alpha)) at continuity points α\alpha of qXq\_{X};
see [[18](https://arxiv.org/html/2602.00784v1#bib.bib18), Lemma 21.1]. Since

|  |  |  |
| --- | --- | --- |
|  | T​(F)=−∫01Q​(F)​(α)​φ​(α)​𝑑α,T(F)=-\int\_{0}^{1}Q(F)(\alpha)\varphi(\alpha)\,d\alpha, |  |

the chain rule gives

|  |  |  |
| --- | --- | --- |
|  | TFX′​(h)=−∫01QFX′​(h)​(α)​φ​(α)​𝑑α=∫01h​(qX​(α))fX​(qX​(α))​φ​(α)​𝑑α.∎T^{\prime}\_{F\_{X}}(h)=-\int\_{0}^{1}Q^{\prime}\_{F\_{X}}(h)(\alpha)\,\varphi(\alpha)\,d\alpha=\int\_{0}^{1}\frac{h(q\_{X}(\alpha))}{f\_{X}(q\_{X}(\alpha))}\,\varphi(\alpha)\,d\alpha.\qed |  |

###### Theorem 9.4 (Hyperfinite Bootstrap Consistency).

Let X∈L2X\in L^{2} satisfy Assumption [9.2](https://arxiv.org/html/2602.00784v1#S9.Thmtheorem2 "Assumption 9.2 (Bootstrap regularity). ‣ 9.2. Near-standardness of conditional laws ‣ 9. Hyperfinite bootstrap validity ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), and let φ\varphi be Lipschitz.
Assume moreover that the hypotheses of Theorem [10.5](https://arxiv.org/html/2602.00784v1#S10.Thmtheorem5 "Theorem 10.5 (Asymptotic normality of spectral plug-in CREs). ‣ 10.2. Asymptotic normality of spectral estimators ‣ 10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") hold, so that the asymptotic
variance σφ2\sigma\_{\varphi}^{2} in ([28](https://arxiv.org/html/2602.00784v1#S10.E28 "In Theorem 10.5 (Asymptotic normality of spectral plug-in CREs). ‣ 10.2. Asymptotic normality of spectral estimators ‣ 10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")) is finite.
Let ℒ∗(⋅|X)\mathcal{L}^{\*}(\cdot|X) denote the internal conditional law given the sample
(i.e., the law under the bootstrap-index randomness (Ui)(U\_{i}) with (Xi)(X\_{i}) fixed).
Then, for L​(𝖯∗)L({}^{\*}\mathsf{P})-almost all sample paths ω\omega,

|  |  |  |
| --- | --- | --- |
|  | dK​(ℒ∗​(N​(ρ^N∗−ρ^N)|X​(ω)),N​(0,σφ2))≈0,d\_{K}\left(\mathcal{L}^{\*}\left(\sqrt{N}(\hat{\rho}\_{N}^{\*}-\hat{\rho}\_{N})\;\Big|\;X(\omega)\right),\ N(0,\sigma\_{\varphi}^{2})\right)\approx 0, |  |

where σφ2\sigma\_{\varphi}^{2} is the asymptotic variance in Theorem [10.5](https://arxiv.org/html/2602.00784v1#S10.Thmtheorem5 "Theorem 10.5 (Asymptotic normality of spectral plug-in CREs). ‣ 10.2. Asymptotic normality of spectral estimators ‣ 10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics").

###### Proof.

The proof combines the standard functional delta method for the bootstrap as explained by
[[18](https://arxiv.org/html/2602.00784v1#bib.bib18), Thm. 23.9] with NSA reasoning, using the internal Kolmogorov distance
dK,md\_{K,m} from Lemma [9.1](https://arxiv.org/html/2602.00784v1#S9.Thmtheorem1 "Lemma 9.1 (Internal Kolmogorov distance approximation). ‣ 9.1. Internal bootstrap construction ‣ 9. Hyperfinite bootstrap validity ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") to ensure measurability.

*Near-standardness of the empirical measure.*
Fix a sample path ω\omega such that the empirical CDF F^N\hat{F}\_{N} satisfies
‖F^N−FX‖∞≈0\|\hat{F}\_{N}-F\_{X}\|\_{\infty}\approx 0. By the hyperfinite Glivenko–Cantelli theorem
(Theorem [3.20](https://arxiv.org/html/2602.00784v1#S3.Thmtheorem20 "Theorem 3.20 (Hyperfinite Glivenko–Cantelli / quantile shadow). ‣ 3.7. The hyperfinite strong law and Glivenko–Cantelli theorem ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")), this holds for L​(𝖯∗)L({}^{\*}\mathsf{P})-almost all ω\omega.

*Standard bootstrap delta method.*
The standard bootstrap delta method [[18](https://arxiv.org/html/2602.00784v1#bib.bib18), Thm. 23.9] asserts:
under Assumption [9.2](https://arxiv.org/html/2602.00784v1#S9.Thmtheorem2 "Assumption 9.2 (Bootstrap regularity). ‣ 9.2. Near-standardness of conditional laws ‣ 9. Hyperfinite bootstrap validity ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), the conditional distribution of
n​(T​(F^n∗)−T​(F^n))\sqrt{n}(T(\hat{F}\_{n}^{\*})-T(\hat{F}\_{n})) given the sample converges to
ℒ​(TFX′​(𝔾))\mathcal{L}(T^{\prime}\_{F\_{X}}(\mathbb{G})) *in probability* in the bounded-Lipschitz metric,
where 𝔾\mathbb{G} is an FXF\_{X}-Brownian bridge. Since the limit distribution N​(0,σφ2)N(0,\sigma\_{\varphi}^{2})
has a continuous CDF, this implies convergence in Kolmogorov distance
[[18](https://arxiv.org/html/2602.00784v1#bib.bib18), Lemma 21.2]: for every ε,δ>0\varepsilon,\delta>0 and m∈ℕm\in\mathbb{N},
there exists n0∈ℕn\_{0}\in\mathbb{N} such that for all n⩾n0n\geqslant n\_{0},

|  |  |  |
| --- | --- | --- |
|  | 𝖯​(dK,m​(ℒ​(n​(T​(F^n∗)−T​(F^n))∣X),N​(0,σφ2))>ε)<δ.\mathsf{P}\Big(d\_{K,m}\big(\mathcal{L}(\sqrt{n}(T(\hat{F}\_{n}^{\*})-T(\hat{F}\_{n}))\mid X),\,N(0,\sigma\_{\varphi}^{2})\big)>\varepsilon\Big)<\delta. |  |

*NSA repackaging via internal distance.*
Fix standard ε,δ>0\varepsilon,\delta>0 and standard m∈ℕm\in\mathbb{N}. The event
Em,ε:={dK,m​(ℒ∗​(N​(ρ^N∗−ρ^N)∣X),N​(0,σφ2))>ε}E\_{m,\varepsilon}:=\{d\_{K,m}(\mathcal{L}^{\*}(\sqrt{N}(\hat{\rho}\_{N}^{\*}-\hat{\rho}\_{N})\mid X),N(0,\sigma\_{\varphi}^{2}))>\varepsilon\}
is *internal* by Lemma [9.1](https://arxiv.org/html/2602.00784v1#S9.Thmtheorem1 "Lemma 9.1 (Internal Kolmogorov distance approximation). ‣ 9.1. Internal bootstrap construction ‣ 9. Hyperfinite bootstrap validity ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")(ii), hence Loeb measurable.

The sample size NN exceeds any standard threshold n0n\_{0} (since NN is infinite), so
𝖯∗​(Em,ε)<δ{}^{\*}\mathsf{P}(E\_{m,\varepsilon})<\delta. Taking Loeb measures and using that δ>0\delta>0 is arbitrary,
L​(𝖯∗)​(Em,ε)=0L({}^{\*}\mathsf{P})(E\_{m,\varepsilon})=0 for each standard ε>0\varepsilon>0 and m∈ℕm\in\mathbb{N}.

Intersecting over countably many ε=1/k\varepsilon=1/k and m∈ℕm\in\mathbb{N}, we obtain a Loeb-probability-one
set GG on which dK,m​(ℒ∗​(N​(ρ^N∗−ρ^N)∣X),N​(0,σφ2))<1/rd\_{K,m}(\mathcal{L}^{\*}(\sqrt{N}(\hat{\rho}\_{N}^{\*}-\hat{\rho}\_{N})\mid X),N(0,\sigma\_{\varphi}^{2}))<1/r
for all standard m,r∈ℕm,r\in\mathbb{N}. To obtain an infinite MM with dK,M≈0d\_{K,M}\approx 0, we use saturation:
for each standard r∈ℕr\in\mathbb{N}, define the internal set

|  |  |  |
| --- | --- | --- |
|  | Ar:={m∈ℕ∗:dK,m​(ℒ∗​(N​(ρ^N∗−ρ^N)∣X),N​(0,σφ2))<1/r}.A\_{r}:=\{m\in{}^{\*}\mathbb{N}:d\_{K,m}(\mathcal{L}^{\*}(\sqrt{N}(\hat{\rho}\_{N}^{\*}-\hat{\rho}\_{N})\mid X),N(0,\sigma\_{\varphi}^{2}))<1/r\}. |  |

On the set GG, each ArA\_{r} contains all standard mm. The family {Ar}r∈ℕ∪{Bs}s∈ℕ\{A\_{r}\}\_{r\in\mathbb{N}}\cup\{B\_{s}\}\_{s\in\mathbb{N}}
(where Bs:={m∈ℕ∗:m>s}B\_{s}:=\{m\in{}^{\*}\mathbb{N}:m>s\}) has the finite intersection property. By countable saturation,
there exists M∈⋂r∈ℕAr∩⋂s∈ℕBsM\in\bigcap\_{r\in\mathbb{N}}A\_{r}\cap\bigcap\_{s\in\mathbb{N}}B\_{s}, which is infinite (since M>sM>s for
all standard ss) and satisfies dK,M<1/rd\_{K,M}<1/r for all standard rr, hence dK,M≈0d\_{K,M}\approx 0.
By Lemma [9.1](https://arxiv.org/html/2602.00784v1#S9.Thmtheorem1 "Lemma 9.1 (Internal Kolmogorov distance approximation). ‣ 9.1. Internal bootstrap construction ‣ 9. Hyperfinite bootstrap validity ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")(i), the standard-part distribution equals N​(0,σφ2)N(0,\sigma\_{\varphi}^{2}).

*Identification of the asymptotic variance.*
The random variable TFX′​(𝔾)T^{\prime}\_{F\_{X}}(\mathbb{G}) equals

|  |  |  |
| --- | --- | --- |
|  | ∫01𝔾​(qX​(α))fX​(qX​(α))​φ​(α)​𝑑α=∫01B​(α)fX​(qX​(α))​φ​(α)​𝑑α,\int\_{0}^{1}\frac{\mathbb{G}(q\_{X}(\alpha))}{f\_{X}(q\_{X}(\alpha))}\,\varphi(\alpha)\,d\alpha=\int\_{0}^{1}\frac{B(\alpha)}{f\_{X}(q\_{X}(\alpha))}\,\varphi(\alpha)\,d\alpha, |  |

where B​(α):=𝔾​(qX​(α))B(\alpha):=\mathbb{G}(q\_{X}(\alpha)) is a standard Brownian bridge on [0,1][0,1]
(since 𝔾​(x)\mathbb{G}(x) at x=qX​(α)x=q\_{X}(\alpha) with FX​(qX​(α))=αF\_{X}(q\_{X}(\alpha))=\alpha gives
Cov​(B​(α),B​(β))=min⁡(α,β)−α​β\mathrm{Cov}(B(\alpha),B(\beta))=\min(\alpha,\beta)-\alpha\beta).

This integral is Gaussian with mean zero. Under the stronger smoothness hypotheses of
Theorem [10.5](https://arxiv.org/html/2602.00784v1#S10.Thmtheorem5 "Theorem 10.5 (Asymptotic normality of spectral plug-in CREs). ‣ 10.2. Asymptotic normality of spectral estimators ‣ 10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") (in particular, qX∈C1q\_{X}\in C^{1} with qX′=1/fX​(qX)q\_{X}^{\prime}=1/f\_{X}(q\_{X})), the variance equals

|  |  |  |
| --- | --- | --- |
|  | σφ2=∫01∫01(min⁡(α,β)−α​β)​φ​(α)​φ​(β)fX​(qX​(α))​fX​(qX​(β))​𝑑α​𝑑β.\sigma\_{\varphi}^{2}=\int\_{0}^{1}\int\_{0}^{1}(\min(\alpha,\beta)-\alpha\beta)\,\frac{\varphi(\alpha)\varphi(\beta)}{f\_{X}(q\_{X}(\alpha))f\_{X}(q\_{X}(\beta))}\,d\alpha\,d\beta. |  |

Since the limit N​(0,σφ2)N(0,\sigma\_{\varphi}^{2}) has a continuous CDF, weak convergence to it implies
Kolmogorov distance convergence (see, e.g., [[18](https://arxiv.org/html/2602.00784v1#bib.bib18), Lemma 21.2]).
Thus dK​(ℒ∗​(N​(ρ^N∗−ρ^N)∣X),N​(0,σφ2))≈0d\_{K}(\mathcal{L}^{\*}(\sqrt{N}(\hat{\rho}\_{N}^{\*}-\hat{\rho}\_{N})\mid X),N(0,\sigma\_{\varphi}^{2}))\approx 0.
∎

###### Remark 9.5 (The power of the hyperfinite viewpoint).

The advantage of this approach is that we do not need to check “sequences” of conditional
measures converging in a double-limit sense. We fix a single infinite NN and a typical path;
the bootstrap distribution is then a fixed internal distribution, which we show is near-standard
to the Gaussian. The transfer principle converts the standard Hadamard differentiability
into an internal statement, and near-standardness of the empirical measure (from Theorem
[3.20](https://arxiv.org/html/2602.00784v1#S3.Thmtheorem20 "Theorem 3.20 (Hyperfinite Glivenko–Cantelli / quantile shadow). ‣ 3.7. The hyperfinite strong law and Glivenko–Cantelli theorem ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")) provides the bridge between the internal and standard worlds.

## 10. Asymptotic normality via the hyperfinite CLT

We derive the asymptotic distribution of spectral plug-in estimators using the hyperfinite
central limit theorem.

### 10.1. Hyperfinite central limit theorem

###### Theorem 10.1 (Hyperfinite CLT).

Let (Xi)i∈ℕ(X\_{i})\_{i\in\mathbb{N}} be i.i.d. on
(Ω,𝒢,𝖯)(\Omega,\mathscr{G},\mathsf{P}) with 𝖤​[X1]=0\mathsf{E}[X\_{1}]=0 and 𝖵𝖺𝗋⁡(X1)=σ2<∞\operatorname{\mathsf{Var}}(X\_{1})=\sigma^{2}<\infty. Let N∈ℕ∗N\in{}^{\*}\mathbb{N} be infinite and consider the hyperfinite
sum SN:=1N​∑k=1NXkS\_{N}:=\frac{1}{\sqrt{N}}\sum\_{k=1}^{N}X\_{k} on (Ω∗,L​(𝒢∗),L​(𝖯∗))({}^{\*}\Omega,L({}^{\*}\mathscr{G}),L({}^{\*}\mathsf{P})).
Under the finite variance assumption, SNS\_{N} is finite L​(𝖯∗)L({}^{\*}\mathsf{P})-almost surely.
Indeed, by Chebyshev’s inequality (which transfers), for any standard M>0M>0,

|  |  |  |
| --- | --- | --- |
|  | 𝖯∗​(|SN|>M)⩽𝖤∗​[SN2]M2=σ2M2.{}^{\*}\mathsf{P}(|S\_{N}|>M)\leqslant\frac{{}^{\*}\mathsf{E}[S\_{N}^{2}]}{M^{2}}=\frac{\sigma^{2}}{M^{2}}. |  |

Taking standard parts, L​(𝖯∗)​(|SN|>M)⩽σ2/M2L({}^{\*}\mathsf{P})(|S\_{N}|>M)\leqslant\sigma^{2}/M^{2}. Letting M→∞M\to\infty,

|  |  |  |
| --- | --- | --- |
|  | L​(𝖯∗)​(|SN|​ is infinite)=0.L({}^{\*}\mathsf{P})(|S\_{N}|\text{ is infinite})=0. |  |

Thus st⁡(SN)\operatorname{st}(S\_{N}) is well-defined L​(𝖯∗)L({}^{\*}\mathsf{P})-almost surely.

Then for every t∈ℝt\in\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | L​(𝖯∗)​(st⁡(SN)⩽t)=Φ​(t/σ),L({}^{\*}\mathsf{P})\bigl(\operatorname{st}(S\_{N})\leqslant t\bigr)=\Phi(t/\sigma), |  |

where Φ\Phi is the standard normal distribution function.

###### Remark 10.2.

The hyperfinite CLT is a *standard* result in non-standard probability; see, e.g.,
[[3](https://arxiv.org/html/2602.00784v1#bib.bib3), Ch. 5] or [[4](https://arxiv.org/html/2602.00784v1#bib.bib4)] for systematic treatments.

###### Proof.

By the classical CLT, Sn:=1n​∑k=1nXk→𝑑N​(0,σ2)S\_{n}:=\frac{1}{\sqrt{n}}\sum\_{k=1}^{n}X\_{k}\xrightarrow{d}N(0,\sigma^{2}).
For any t∈ℝt\in\mathbb{R} and ε>0\varepsilon>0, there exists n0n\_{0} such that for all n⩾n0n\geqslant n\_{0},

|  |  |  |
| --- | --- | --- |
|  | |𝖯​(Sn⩽t)−Φ​(t/σ)|<ε.|\mathsf{P}(S\_{n}\leqslant t)-\Phi(t/\sigma)|<\varepsilon. |  |

By transfer, this holds for NN, hence
|𝖯∗​(SN⩽t)−Φ​(t/σ)|<ε|{}^{\*}\mathsf{P}(S\_{N}\leqslant t)-\Phi(t/\sigma)|<\varepsilon.
Since ε\varepsilon is arbitrary, 𝖯∗​(SN⩽t)≈Φ​(t/σ){}^{\*}\mathsf{P}(S\_{N}\leqslant t)\approx\Phi(t/\sigma).

To pass from 𝖯∗​(SN⩽t){}^{\*}\mathsf{P}(S\_{N}\leqslant t) to the Loeb event {st⁡(SN)⩽t}\{\operatorname{st}(S\_{N})\leqslant t\}, note that

|  |  |  |
| --- | --- | --- |
|  | {st⁡(SN)⩽t}=⋂m∈ℕ{SN⩽t+1/m},\{\operatorname{st}(S\_{N})\leqslant t\}=\bigcap\_{m\in\mathbb{N}}\{S\_{N}\leqslant t+1/m\}, |  |

hence by continuity from above of L​(𝖯∗)L({}^{\*}\mathsf{P}),

|  |  |  |
| --- | --- | --- |
|  | L​(𝖯∗)​(st⁡(SN)⩽t)=limm→∞st⁡(𝖯∗​(SN⩽t+1/m)).L({}^{\*}\mathsf{P})(\operatorname{st}(S\_{N})\leqslant t)=\lim\_{m\to\infty}\operatorname{st}\bigl({}^{\*}\mathsf{P}(S\_{N}\leqslant t+1/m)\bigr). |  |

Since 𝖯∗​(SN⩽t+1/m)≈Φ​((t+1/m)/σ){}^{\*}\mathsf{P}(S\_{N}\leqslant t+1/m)\approx\Phi((t+1/m)/\sigma) for each fixed mm and Φ\Phi is continuous,
the limit equals Φ​(t/σ)\Phi(t/\sigma).
∎

### 10.2. Asymptotic normality of spectral estimators

Before stating the main CLT, we establish two technical lemmas that make the NSA proof rigorous.

###### Lemma 10.3 (Infinitesimal perturbation preserves standard-part distribution).

Let Y,ZY,Z be finite hyperreal random variables on (Ω∗,L​(𝖯∗))({}^{\*}\Omega,L({}^{\*}\mathsf{P})) such that
Y≈ZY\approx Z holds L​(𝖯∗)L({}^{\*}\mathsf{P})-almost surely. Then st⁡(Y)\operatorname{st}(Y) and st⁡(Z)\operatorname{st}(Z) have the same
distribution under L​(𝖯∗)L({}^{\*}\mathsf{P}).

###### Proof.

Let A:={ω:Y​(ω)≈Z​(ω)}A:=\{\omega:Y(\omega)\approx Z(\omega)\}. By hypothesis, L​(𝖯∗)​(A)=1L({}^{\*}\mathsf{P})(A)=1.
For any t∈ℝt\in\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | {st⁡(Y)⩽t}∩A={st⁡(Z)⩽t}∩A\{\operatorname{st}(Y)\leqslant t\}\cap A=\{\operatorname{st}(Z)\leqslant t\}\cap A |  |

because if Y≈ZY\approx Z and st⁡(Y)⩽t\operatorname{st}(Y)\leqslant t, then st⁡(Z)=st⁡(Y)⩽t\operatorname{st}(Z)=\operatorname{st}(Y)\leqslant t, and vice versa.
Since L​(𝖯∗)​(Ac)=0L({}^{\*}\mathsf{P})(A^{c})=0, we have

|  |  |  |
| --- | --- | --- |
|  | L​(𝖯∗)​(st⁡(Y)⩽t)=L​(𝖯∗)​(st⁡(Y)⩽t,A)=L​(𝖯∗)​(st⁡(Z)⩽t,A)=L​(𝖯∗)​(st⁡(Z)⩽t).∎L({}^{\*}\mathsf{P})(\operatorname{st}(Y)\leqslant t)=L({}^{\*}\mathsf{P})(\operatorname{st}(Y)\leqslant t,A)=L({}^{\*}\mathsf{P})(\operatorname{st}(Z)\leqslant t,A)=L({}^{\*}\mathsf{P})(\operatorname{st}(Z)\leqslant t).\qed |  |

###### Lemma 10.4 (Asymptotic linearity in first-order form).

Under the hypotheses of Theorem [10.5](https://arxiv.org/html/2602.00784v1#S10.Thmtheorem5 "Theorem 10.5 (Asymptotic normality of spectral plug-in CREs). ‣ 10.2. Asymptotic normality of spectral estimators ‣ 10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), the asymptotic linearity of the spectral
L-statistic can be expressed as follows: for every ε∈ℚ>0\varepsilon\in\mathbb{Q}\_{>0},
there exists n0∈ℕn\_{0}\in\mathbb{N} such that for all n⩾n0n\geqslant n\_{0},

|  |  |  |  |
| --- | --- | --- | --- |
| (26) |  | 𝖯​(|n​(ρ^n,φ−ρφ​(X))−1n​∑i=1nIFφ​(Xi)|>ε)<ε,\mathsf{P}\Big(\Big|\sqrt{n}(\hat{\rho}\_{n,\varphi}-\rho\_{\varphi}(X))-\frac{1}{\sqrt{n}}\sum\_{i=1}^{n}\mathrm{IF}\_{\varphi}(X\_{i})\Big|>\varepsilon\Big)<\varepsilon, |  |

where IFφ​(x):=∫01φ​(α)​qX′​(α)​(𝟏x⩽qX​(α)−α)​𝑑α\mathrm{IF}\_{\varphi}(x):=\int\_{0}^{1}\varphi(\alpha)\,q\_{X}^{\prime}(\alpha)\,(\mathbf{1}\_{x\leqslant q\_{X}(\alpha)}-\alpha)\,d\alpha.
This statement is first-order in the sense that it can be formalised using only bounded
quantification over rationals, hence is amenable to transfer and underspill.

###### Proof.

This is the content of [[17](https://arxiv.org/html/2602.00784v1#bib.bib17), Thm. 8.5]: under the smoothness hypotheses (bounded
φ\varphi, qX∈C1q\_{X}\in C^{1} with finite ∫φ2​(qX′)2\int\varphi^{2}(q\_{X}^{\prime})^{2}), the L-statistic
ρ^n,φ\hat{\rho}\_{n,\varphi} is asymptotically linear with influence function IFφ\mathrm{IF}\_{\varphi}.
The “o𝖯​(1)o\_{\mathsf{P}}(1)” remainder term means precisely that for every ε>0\varepsilon>0,
𝖯​(|remainder|>ε)→0\mathsf{P}(|\text{remainder}|>\varepsilon)\to 0, which can be restated in the
“∀ε​∃n0​∀n⩾n0\forall\varepsilon\exists n\_{0}\forall n\geqslant n\_{0}” form above.
∎

###### Theorem 10.5 (Asymptotic normality of spectral plug-in CREs).

Let X∈L2X\in L^{2} and φ\varphi a bounded spectrum. Assume the quantile function qXq\_{X} is
continuously differentiable on (0,1)(0,1) with derivative qX′=1/fX​(qX)q\_{X}^{\prime}=1/f\_{X}(q\_{X}), where fXf\_{X}
is the density of XX. Assume moreover that ∫01φ​(α)2​qX′​(α)2​𝑑α<∞\int\_{0}^{1}\varphi(\alpha)^{2}q\_{X}^{\prime}(\alpha)^{2}\,d\alpha<\infty,
so that σφ2\sigma\_{\varphi}^{2} in ([28](https://arxiv.org/html/2602.00784v1#S10.E28 "In Theorem 10.5 (Asymptotic normality of spectral plug-in CREs). ‣ 10.2. Asymptotic normality of spectral estimators ‣ 10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")) is finite. Then

|  |  |  |  |
| --- | --- | --- | --- |
| (27) |  | n​(ρ^n,φ​(X1,…,Xn)−ρφ​(X))→𝑑N​(0,σφ2),\sqrt{n}\left(\hat{\rho}\_{n,\varphi}(X\_{1},\ldots,X\_{n})-\rho\_{\varphi}(X)\right)\xrightarrow{d}N(0,\sigma\_{\varphi}^{2}), |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
| (28) |  | σφ2=∫01∫01(min⁡(α,β)−α​β)​φ​(α)​φ​(β)​qX′​(α)​qX′​(β)​𝑑α​𝑑β.\sigma\_{\varphi}^{2}=\int\_{0}^{1}\int\_{0}^{1}(\min(\alpha,\beta)-\alpha\beta)\varphi(\alpha)\varphi(\beta)q\_{X}^{\prime}(\alpha)q\_{X}^{\prime}(\beta)\,d\alpha\,d\beta. |  |

###### Proof.

The result is a classical asymptotic normality theorem for L-statistics; see
[[17](https://arxiv.org/html/2602.00784v1#bib.bib17), Ch. 8] or [[18](https://arxiv.org/html/2602.00784v1#bib.bib18), Ch. 21] for the functional delta method approach.
For the reader’s convenience, we provide a complete NSA proof using the hyperfinite CLT and the lemmata above.

*The influence function representation.*
For L-statistics of the form ρ^n,φ=−∫01qn​(α)​φ​(α)​𝑑α\hat{\rho}\_{n,\varphi}=-\int\_{0}^{1}q\_{n}(\alpha)\varphi(\alpha)\,d\alpha,
the classical theory provides the asymptotic linearity result stated in Lemma [10.4](https://arxiv.org/html/2602.00784v1#S10.Thmtheorem4 "Lemma 10.4 (Asymptotic linearity in first-order form). ‣ 10.2. Asymptotic normality of spectral estimators ‣ 10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics").
The influence function is

|  |  |  |
| --- | --- | --- |
|  | IFφ​(x):=∫01φ​(α)​qX′​(α)​(𝟏x⩽qX​(α)−α)​𝑑α.\mathrm{IF}\_{\varphi}(x):=\int\_{0}^{1}\varphi(\alpha)\,q\_{X}^{\prime}(\alpha)\,\bigl(\mathbf{1}\_{x\leqslant q\_{X}(\alpha)}-\alpha\bigr)\,d\alpha. |  |

Under the smoothness assumptions, IFφ∈L2\mathrm{IF}\_{\varphi}\in L^{2} with 𝖤​[IFφ​(X)]=0\mathsf{E}[\mathrm{IF}\_{\varphi}(X)]=0
and 𝖵𝖺𝗋⁡(IFφ​(X))=σφ2\operatorname{\mathsf{Var}}(\mathrm{IF}\_{\varphi}(X))=\sigma\_{\varphi}^{2}.

*NSA formulation via hyperfinite CLT.*
For infinite N∈ℕ∗N\in{}^{\*}\mathbb{N}, consider the internal average

|  |  |  |
| --- | --- | --- |
|  | TN:=1N​∑i=1NIFφ​(Xi).T\_{N}:=\frac{1}{\sqrt{N}}\sum\_{i=1}^{N}\mathrm{IF}\_{\varphi}(X\_{i}). |  |

By the hyperfinite CLT (Theorem [10.1](https://arxiv.org/html/2602.00784v1#S10.Thmtheorem1 "Theorem 10.1 (Hyperfinite CLT). ‣ 10.1. Hyperfinite central limit theorem ‣ 10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")), st⁡(TN)∼N​(0,σφ2)\operatorname{st}(T\_{N})\sim N(0,\sigma\_{\varphi}^{2}).

By Lemma [10.4](https://arxiv.org/html/2602.00784v1#S10.Thmtheorem4 "Lemma 10.4 (Asymptotic linearity in first-order form). ‣ 10.2. Asymptotic normality of spectral estimators ‣ 10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), the asymptotic linearity statement
([26](https://arxiv.org/html/2602.00784v1#S10.E26 "In Lemma 10.4 (Asymptotic linearity in first-order form). ‣ 10.2. Asymptotic normality of spectral estimators ‣ 10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")) holds for all n⩾n0n\geqslant n\_{0} for some standard n0n\_{0}.
For the fixed infinite NN in our standing model, N>n0N>n\_{0}, so

|  |  |  |
| --- | --- | --- |
|  | 𝖯∗​(|N​(ρ^N,φ−ρφ​(X))−TN|>ε)<ε.{}^{\*}\mathsf{P}\Big(\Big|\sqrt{N}(\hat{\rho}\_{N,\varphi}-\rho\_{\varphi}(X))-T\_{N}\Big|>\varepsilon\Big)<\varepsilon. |  |

Intersecting over a sequence ε=1/m\varepsilon=1/m (m∈ℕm\in\mathbb{N}) and taking Loeb probabilities, we see that
N​(ρ^N,φ−ρφ​(X))≈TN\sqrt{N}(\hat{\rho}\_{N,\varphi}-\rho\_{\varphi}(X))\approx T\_{N} holds L​(𝖯∗)L({}^{\*}\mathsf{P})-almost surely.

*Conclusion via standard part.*
By Lemma [10.3](https://arxiv.org/html/2602.00784v1#S10.Thmtheorem3 "Lemma 10.3 (Infinitesimal perturbation preserves standard-part distribution). ‣ 10.2. Asymptotic normality of spectral estimators ‣ 10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics"), since
N​(ρ^N,φ−ρφ​(X))≈TN\sqrt{N}(\hat{\rho}\_{N,\varphi}-\rho\_{\varphi}(X))\approx T\_{N} L​(𝖯∗)L({}^{\*}\mathsf{P})-a.s., we have

|  |  |  |
| --- | --- | --- |
|  | st⁡(N​(ρ^N,φ−ρφ​(X)))∼st⁡(TN)∼N​(0,σφ2).\operatorname{st}\bigl(\sqrt{N}(\hat{\rho}\_{N,\varphi}-\rho\_{\varphi}(X))\bigr)\sim\operatorname{st}(T\_{N})\sim N(0,\sigma\_{\varphi}^{2}). |  |

*Transfer back to standard sequences.*
To obtain the standard convergence in distribution, we use overspill on a complement set.
Fix t∈ℚt\in\mathbb{Q} and rational ε>0\varepsilon>0. Define the internal set

|  |  |  |
| --- | --- | --- |
|  | St,ε:={n∈ℕ∗:|𝖯∗​(n​(ρ^n,φ−ρφ​(X))⩽t)−Φ​(t/σφ)|<ε}.S\_{t,\varepsilon}:=\{n\in{}^{\*}\mathbb{N}:|{}^{\*}\mathsf{P}(\sqrt{n}(\hat{\rho}\_{n,\varphi}-\rho\_{\varphi}(X))\leqslant t)-\Phi(t/\sigma\_{\varphi})|<\varepsilon\}. |  |

This set is internal because the defining predicate uses 𝖯∗{}^{\*}\mathsf{P} (the non-standard extension
of 𝖯\mathsf{P}) and involves only internal random variables, hypernatural nn, and standard constants
t,ε,σφ,Φt,\varepsilon,\sigma\_{\varphi},\Phi. Choose a standard m∈ℕm\in\mathbb{N} so large that 1/m<ε/31/m<\varepsilon/3 and

|  |  |  |
| --- | --- | --- |
|  | Φ​(t+1/mσφ)−Φ​(t−1/mσφ)<ε/3,\Phi\!\left(\frac{t+1/m}{\sigma\_{\varphi}}\right)-\Phi\!\left(\frac{t-1/m}{\sigma\_{\varphi}}\right)<\varepsilon/3, |  |

which is possible by continuity of Φ\Phi.

Let us define the *influence function* of the spectral functional by

|  |  |  |
| --- | --- | --- |
|  | IFφ​(x):=∫01φ​(α)​qX′​(α)​(𝟏{x⩽qX​(α)}−α)​𝑑α=∫01φ​(α)​𝟏{x⩽qX​(α)}−αfX​(qX​(α))​𝑑α.\mathrm{IF}\_{\varphi}(x):=\int\_{0}^{1}\varphi(\alpha)\,q\_{X}^{\prime}(\alpha)\bigl(\mathbf{1}\_{\{x\leqslant q\_{X}(\alpha)\}}-\alpha\bigr)\,d\alpha=\int\_{0}^{1}\varphi(\alpha)\,\frac{\mathbf{1}\_{\{x\leqslant q\_{X}(\alpha)\}}-\alpha}{f\_{X}(q\_{X}(\alpha))}\,d\alpha. |  |

For n∈ℕ∗n\in{}^{\*}\mathbb{N} we define the (internal) hyperfinite sum

|  |  |  |
| --- | --- | --- |
|  | Tn:=1n​∑i=1nIFφ​(Xi).T\_{n}:=\frac{1}{\sqrt{n}}\sum\_{i=1}^{n}\mathrm{IF}\_{\varphi}(X\_{i}). |  |

By transfer of ([26](https://arxiv.org/html/2602.00784v1#S10.E26 "In Lemma 10.4 (Asymptotic linearity in first-order form). ‣ 10.2. Asymptotic normality of spectral estimators ‣ 10. Asymptotic normality via the hyperfinite CLT ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")) with ε=1/m\varepsilon=1/m, every infinite nn satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝖯∗​(|n​(ρ^n,φ−ρφ​(X))−Tn|>1/m)<1/m.{}^{\*}\mathsf{P}\big(|\sqrt{n}(\hat{\rho}\_{n,\varphi}-\rho\_{\varphi}(X))-T\_{n}|>1/m\big)<1/m. |  |

Moreover, the classical CLT for the i.i.d. sequence IFφ​(Xi)\mathrm{IF}\_{\varphi}(X\_{i}) implies (by transfer) that for each standard u∈ℝu\in\mathbb{R} and each infinite nn,

|  |  |  |
| --- | --- | --- |
|  | 𝖯∗​(Tn⩽u)≈Φ​(u/σφ).{}^{\*}\mathsf{P}(T\_{n}\leqslant u)\approx\Phi(u/\sigma\_{\varphi}). |  |

For such nn we therefore have the sandwich bounds

|  |  |  |
| --- | --- | --- |
|  | 𝖯∗​(Tn⩽t−1/m)−1/m⩽𝖯∗​(n​(ρ^n,φ−ρφ​(X))⩽t)⩽𝖯∗​(Tn⩽t+1/m)+1/m.{}^{\*}\mathsf{P}(T\_{n}\leqslant t-1/m)-1/m\leqslant{}^{\*}\mathsf{P}(\sqrt{n}(\hat{\rho}\_{n,\varphi}-\rho\_{\varphi}(X))\leqslant t)\leqslant{}^{\*}\mathsf{P}(T\_{n}\leqslant t+1/m)+1/m. |  |

Consequently, for every infinite nn,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝖯∗​(n​(ρ^n,φ−ρφ​(X))⩽t)−Φ​(t/σφ)|\displaystyle\Big|{}^{\*}\mathsf{P}(\sqrt{n}(\hat{\rho}\_{n,\varphi}-\rho\_{\varphi}(X))\leqslant t)-\Phi(t/\sigma\_{\varphi})\Big| | ⩽max±⁡|𝖯∗​(Tn⩽t±1/m)−Φ​(t±1/mσφ)|\displaystyle\leqslant\max\_{\pm}\Big|{}^{\*}\mathsf{P}(T\_{n}\leqslant t\pm 1/m)-\Phi\!\Big(\frac{t\pm 1/m}{\sigma\_{\varphi}}\Big)\Big| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +|Φ​(t+1/mσφ)−Φ​(t−1/mσφ)|+1m<ε,\displaystyle\quad+\Big|\Phi\!\Big(\frac{t+1/m}{\sigma\_{\varphi}}\Big)-\Phi\!\Big(\frac{t-1/m}{\sigma\_{\varphi}}\Big)\Big|+\frac{1}{m}<\varepsilon, |  |

so all infinite nn lie in St,εS\_{t,\varepsilon}.

Let Bt,ε:=ℕ∗∖St,εB\_{t,\varepsilon}:={}^{\*}\mathbb{N}\setminus S\_{t,\varepsilon} be the internal complement.
Since N∈St,εN\in S\_{t,\varepsilon} for every infinite NN, the set Bt,εB\_{t,\varepsilon} contains
no infinite hypernaturals. If Bt,εB\_{t,\varepsilon} contained arbitrarily large standard integers,
then by overspill (Proposition [3.21](https://arxiv.org/html/2602.00784v1#S3.Thmtheorem21 "Proposition 3.21 (Overspill). ‣ 3.8. Overspill and underspill ‣ 3. Non-standard analysis: a self-contained introduction ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics")) it would contain an infinite hypernatural,
a contradiction. Hence there exists n0∈ℕn\_{0}\in\mathbb{N} such that Bt,ε⊆{1,…,n0−1}B\_{t,\varepsilon}\subseteq\{1,\dots,n\_{0}-1\},
and therefore every standard n⩾n0n\geqslant n\_{0} lies in St,εS\_{t,\varepsilon}.

Since ε\varepsilon and tt were arbitrary rationals, and CDFs are determined by their
values at rationals (by right-continuity), we obtain
n​(ρ^n,φ−ρφ​(X))→𝑑N​(0,σφ2)\sqrt{n}(\hat{\rho}\_{n,\varphi}-\rho\_{\varphi}(X))\xrightarrow{d}N(0,\sigma\_{\varphi}^{2}).
∎

## 11. Extensions to Orlicz hearts

We briefly discuss how the hyperfinite framework extends to coherent risk measures on
Orlicz hearts.

### 11.1. Orlicz spaces and duality

Let Φ:[0,∞)→[0,∞)\Phi:[0,\infty)\to[0,\infty) be a Young function (convex, increasing,
Φ​(0)=0\Phi(0)=0, Φ​(x)/x→∞\Phi(x)/x\to\infty). The *Orlicz space* LΦL^{\Phi} consists of
random variables XX with 𝖤​[Φ​(|X|/λ)]<∞\mathsf{E}[\Phi(|X|/\lambda)]<\infty for some λ>0\lambda>0. The
*Orlicz heart* HΦ⊆LΦH^{\Phi}\subseteq L^{\Phi} consists of XX with this condition holding
for all λ>0\lambda>0.

The dual Orlicz space LΨL^{\Psi}, where Ψ\Psi is the complementary Young function, provides
the dual pairs for robust representation.

### 11.2. Hyperfinite representation on Orlicz hearts

###### Remark 11.1 (Orlicz hearts: what changes).

A full Orlicz-heart analogue of Theorem [4.3](https://arxiv.org/html/2602.00784v1#S4.Thmtheorem3 "Theorem 4.3 (Hyperfinite robust representation on 𝐿^∞). ‣ 4.2. Hyperfinite robust representation ‣ 4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") requires replacing the L∞L^{\infty}–L1L^{1}
duality by the HΦH^{\Phi}–LΨL^{\Psi} duality (where Ψ\Psi is complementary to Φ\Phi) and imposing the usual
lower semicontinuity/Fatou-type condition in the HΦH^{\Phi} topology; see [[6](https://arxiv.org/html/2602.00784v1#bib.bib6)].

Specifically, the key modifications are:

1. (i)

   The representing set 𝒵\mathcal{Z} in Theorem [4.3](https://arxiv.org/html/2602.00784v1#S4.Thmtheorem3 "Theorem 4.3 (Hyperfinite robust representation on 𝐿^∞). ‣ 4.2. Hyperfinite robust representation ‣ 4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") must consist of
   densities Z∈L+ΨZ\in L^{\Psi}\_{+} with 𝖤​[Z]=1\mathsf{E}[Z]=1, and compactness is taken in σ​(LΨ,HΦ)\sigma(L^{\Psi},H^{\Phi}).
2. (ii)

   The internal lifting X~\tilde{X} of X∈HΦX\in H^{\Phi} must satisfy 1N​∑k=1NΦ​(|X~​(k)|/λ)\frac{1}{N}\sum\_{k=1}^{N}\Phi(|\tilde{X}(k)|/\lambda)
   finite for all standard λ>0\lambda>0, not merely boundedness.
3. (iii)

   For Z♯∈𝒵∗Z^{\sharp}\in{}^{\*}\mathcal{Z}, SS-integrability of the product X~⋅Z♯\tilde{X}\cdot Z^{\sharp}
   follows from the Orlicz–Hölder inequality |𝖤​[X​Z]|⩽2​‖X‖Φ​‖Z‖Ψ|\mathsf{E}[XZ]|\leqslant 2\|X\|\_{\Phi}\|Z\|\_{\Psi} (transferred internally).
4. (iv)

   The normalisation H​(Z)≈1H(Z)\approx 1 still holds since 𝖤​[Z]=1\mathsf{E}[Z]=1 transfers.

The remainder of the proof of Theorem [4.3](https://arxiv.org/html/2602.00784v1#S4.Thmtheorem3 "Theorem 4.3 (Hyperfinite robust representation on 𝐿^∞). ‣ 4.2. Hyperfinite robust representation ‣ 4. Hyperfinite representation of coherent risk measures ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") proceeds unchanged once these
modifications are in place.

### 11.3. Consistency on Orlicz domains

For plug-in consistency on HΦH^{\Phi}, the uniform boundedness assumption (K3) in Theorem
[8.1](https://arxiv.org/html/2602.00784v1#S8.Thmtheorem1 "Theorem 8.1 (Kusuoka plug-in consistency). ‣ 8.2. Consistency theorem ‣ 8. Kusuoka-type plug-in consistency ‣ Non-standard analysis for coherent risk estimation: hyperfinite representations, discrete Kusuoka formulae, and plug-in asymptotics") is replaced by:

1. (K3’)

   There exists C<∞C<\infty such that
   |ES^α,n​(x)|⩽C​‖x‖Φ|\widehat{\operatorname{ES}}\_{\alpha,n}(x)|\leqslant C\|x\|\_{\Phi} for all α,n,x\alpha,n,x.

Under this and the other assumptions (with L∞L^{\infty} replaced by HΦH^{\Phi}), the Kusuoka
plug-in consistency theorem extends to Orlicz hearts, though a complete treatment requires
careful attention to the Orlicz-space duality theory.

## 12. Concluding remarks

We have developed a systematic hyperfinite framework for coherent risk estimation,
demonstrating that non-standard analysis provides both conceptual clarity and technical
power for this class of problems.

The hyperfinite viewpoint suggests several directions for future work:

* •

  Sensitivity analysis. Internal Lipschitz properties of hyperfinite risk
  functionals could yield robustness bounds for CREs under model misspecification.
* •

  High-dimensional extensions. The hyperfinite framework may extend to
  systemic risk measures on high-dimensional portfolios, where the number of assets grows
  with the sample size.
* •

  Dynamic risk. Time-consistent dynamic risk measures might admit
  hyperfinite backward induction representations, simplifying certain asymptotic analyses.
* •

  Computational aspects. The hyperfinite picture suggests natural
  discretisation schemes for computing coherent risk measures, with explicit error bounds
  derived from the standard-part construction.

## Acknowledgements

The author thanks the Scientific Circle of Financial Mathematics at Jagiellonian University
(Koło Naukowe Matematyki Finansowej UJ) for the invitation to speak at the 26th edition
of the “Future Financier Academy” (Akademia Przyszłego Finansisty) seminar held in
Kacwin, 28–30 November 2025. It was at this conference that the author first learned of
the arXiv preprint [[1](https://arxiv.org/html/2602.00784v1#bib.bib1)] by Aichele, Cialenco, Jelito, and Pitera on coherent estimation
of risk measures, and where the idea of reformulating their results using non-standard analysis
was first conceived.

## References

* [1]

  M. Aichele, I. Cialenco, D. Jelito, and M. Pitera.
  Coherent estimation of risk measures.
  arXiv preprint, arXiv:2510.05809, 2025.
* [2]

  P. Artzner, F. Delbaen, J.-M. Eber, and D. Heath.
  Coherent measures of risk.
  Math. Finance, 9(3):203–228, 1999.
* [3]

  S. Albeverio, J. E. Fenstad, R. Høegh-Krohn, and T. Lindstrøm.
  Nonstandard Methods in Stochastic Analysis and Mathematical Physics.
  Academic Press, 1986.
* [4]

  R. M. Anderson.
  A non-standard representation for Brownian motion and Itô integration.
  Israel J. Math., 25(1–2):15–46, 1976.
* [5]

  S. G. Bobkov and M. Ledoux.
  One-dimensional empirical measures, order statistics, and Kantorovich transport distances.
  Mem. Amer. Math. Soc., 261(1259), 2019.
* [6]

  P. Cheridito and T. Li.
  Risk measures on Orlicz hearts.
  Math. Finance, 19(2):189–214, 2009.
* [7]

  S. X. Chen.
  Nonparametric estimation of expected shortfall.
  J. Financial Econometrics, 6(1):87–107, 2008.
* [8]

  F. Delbaen.
  Coherent risk measures on general probability spaces.
  In Advances in Finance and Stochastics, pp. 1–37, 2002.
* [9]

  D. Denneberg.
  Non-Additive Measure and Integral.
  Kluwer Academic Publishers, 1994.
* [10]

  S. Fajardo and H. J. Keisler.
  Model Theory of Stochastic Processes.
  Lecture Notes in Logic, Cambridge University Press, 2002.
* [11]

  H. Föllmer and A. Schied.
  Stochastic Finance: An Introduction in Discrete Time.
  4th ed., De Gruyter, 2016.
* [12]

  G. H. Hardy, J. E. Littlewood, and G. Pólya.
  Inequalities.
  Cambridge University Press, 2nd ed., 1952.
* [13]

  H. J. Keisler.
  Foundations of Infinitesimal Calculus.
  Online text, 2012.
* [14]

  S. Kusuoka.
  On law-invariant coherent risk measures.
  In Advances in Mathematical Economics, vol. 3, pp. 83–95.
  Springer, 2001.
* [15]

  P. A. Loeb.
  Conversion from non-standard to standard measure spaces and applications
  in probability theory.
  Trans. Amer. Math. Soc., 211:113–122, 1975.
* [16]

  A. Robinson.
  Non-standard Analysis.
  North-Holland, 1966.
* [17]

  R. J. Serfling.
  Approximation Theorems of Mathematical Statistics.
  Wiley, 1980.
* [18]

  A. W. van der Vaart.
  Asymptotic Statistics.
  Cambridge University Press, 1998.
* [19]

  A. W. van der Vaart and J. A. Wellner.
  Weak Convergence and Empirical Processes.
  Springer, 1996.
* [20]

  C. Villani.
  Optimal Transport: Old and New.
  Springer, 2009.