---
authors:
- Yimeng Qiu
doc_id: arxiv:2601.06271v1
family_id: arxiv:2601.06271
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A Three–Dimensional Efficient Surface for Portfolio Optimization
url_abs: http://arxiv.org/abs/2601.06271v1
url_html: https://arxiv.org/html/2601.06271v1
venue: arXiv q-fin
version: 1
year: 2026
---


Yimeng Qiu

(January 9, 2026)

## 1 Introduction

The classical mean–variance portfolio framework pioneered by
Markowitz (Markowitz, [1952](https://arxiv.org/html/2601.06271v1#bib.bib1 "Portfolio selection"))
quantifies the trade-off between expected return and variance of
portfolio returns, producing the familiar two-dimensional efficient
frontier in the (𝔼​[r],σ)(\mathbb{E}[r],\sigma) plane.
Although elegant and widely adopted, this approach implicitly assumes that
the relevant risk *all* can be summarized by variance and the
covariance matrix.
However, in highly interconnected financial markets, shocks often
propagate through complex networks of exposures, creating systemic
vulnerabilities that variance alone does not capture.

A natural extension is to measure *connectedness risk*—the degree
to which a shock to one asset spills over to others.
Diebold and Yilmaz (Diebold and Yilmaz, [2014](https://arxiv.org/html/2601.06271v1#bib.bib9 "On the network topology of variance decompositions: measuring the connectedness of financial firms")) formalize this concept using generalized forecast error variance decompositions (FEVD) from a vector
autoregression (VAR), producing a spillover matrix that quantifies the
risk transmission network of the system.
Other studies, such as Billio et al. (Billio et al., [2012](https://arxiv.org/html/2601.06271v1#bib.bib10 "Econometric measures of connectedness and systemic risk in the finance and insurance sectors")), confirm that
network-based measures convey information on systemic risk beyond what
is contained in pairwise covariances.

Recent work has begun to exploit the network structure for portfolio
construction.
Pozzi et al. (Pozzi et al., [2013](https://arxiv.org/html/2601.06271v1#bib.bib12 "Spread of risk across financial markets: better to invest in the peripheries")) show that tilting toward peripheral
stocks in a correlation network improves risk-adjusted performance, and
Peralta and Zareei (Peralta and Zareei, [2016](https://arxiv.org/html/2601.06271v1#bib.bib13 "A network approach to portfolio selection")) provide a theoretical link
between asset centrality and optimal mean–variance weights.
Although these articles highlight the importance of network effects, they
treat connectedness implicitly or focus on a single objective, such as
minimum-connectedness portfolios
(Broadstock et al. (Broadstock et al., [2022b](https://arxiv.org/html/2601.06271v1#bib.bib16 "Minimum connectedness portfolios: diversifying through network risk"))).

#### This paper.

We develop a unified framework that integrates *expected return*,
*variance risk*, and *connectedness risk* into a single
three-dimensional optimization paradigm.
Let κ≡𝐰𝖳​C​𝐰\kappa\equiv\mathbf{w}^{\mathsf{T}}C\mathbf{w} denote the portfolio
connectedness risk, where CC is a symmetric spillover matrix.
For a given return target μ0\mu\_{0} and a weighting parameter
λ∈[0,1]\lambda\in[0,1], we solve the following problem.

|  |  |  |
| --- | --- | --- |
|  | min𝐰⁡(1−λ)​𝐰𝖳​Σ​𝐰+λ​𝐰𝖳​C​𝐰,s.t.​𝐰𝖳​𝝁≥μ0, 1𝖳​𝐰=1,𝐰≥0.\min\_{\mathbf{w}}\;(1-\lambda)\,\mathbf{w}^{\mathsf{T}}\Sigma\mathbf{w}+\lambda\,\mathbf{w}^{\mathsf{T}}C\mathbf{w},\quad\text{s.t.}\;\mathbf{w}^{\mathsf{T}}\boldsymbol{\mu}\geq\mu\_{0},\;\mathbf{1}^{\mathsf{T}}\mathbf{w}=1,\;\mathbf{w}\geq 0. |  |

Varying (μ0,λ)(\mu\_{0},\lambda) trace a *three-dimensional efficient
surface* in the (𝔼​[r],σ,κ)(\mathbb{E}[r],\sigma,\kappa) space, allowing investors to
visualize and select portfolios according to their tolerance for both
volatility and network contagion.

#### Contributions.

Our study makes four contributions:

1. (1)

   Three-dimensional efficient surface.
   We extend the Markowitz frontier to a 3-D surface that jointly optimizes expected return, variance, and connectedness risk.
2. (2)

   Analytical characterization.
   Under a common-diagonalization assumption we obtain closed-form
   optimal weights, show that variance and connectedness trade off monotonically, and derive a linear approximation of the surface.
3. (3)

   Connectedness beta.
   We introduce a *connectedness β\beta* that measures an
   asset’s marginal contribution to portfolio connectedness,
   paralleling CAPM beta.
4. (4)

   Empirical validation.
   Using S&P 500 stocks (2010–2024) we construct dynamic 3D surfaces and show that portfolios with explicit connectedness constraints exhibit superior downside protection during stress episodes relative to mean variance benchmarks.

#### Road-map.

Section [2](https://arxiv.org/html/2601.06271v1#S2 "2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization") reviews the related literature.
Section [3](https://arxiv.org/html/2601.06271v1#S3 "3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization") presents the model and the main theoretical
results.

## 2 Literature Review

Our study is based on four strands of research:
(i) classical and extended mean variance theory,
(ii) econometric measures of connectedness, (iii) portfolio selection based on networks, and (iv) multiobjective risk optimization.

### 2.1 Mean–Variance Theory and Its Extensions

Markowitz’s *portfolio selection* paradigm
(Markowitz, [1952](https://arxiv.org/html/2601.06271v1#bib.bib1 "Portfolio selection"))
and its continuous–time extension by
Merton ([1972](https://arxiv.org/html/2601.06271v1#bib.bib2 "An analytic derivation of the efficient portfolio frontier"))
formalize diversification through the risk of the second moment.
Later refinements incorporate Bayesian priors
(Black and Litterman ([1992](https://arxiv.org/html/2601.06271v1#bib.bib3 "Global portfolio optimization"))),
shrinkage estimators
(Ledoit and Wolf, [2004](https://arxiv.org/html/2601.06271v1#bib.bib4 "A well–conditioned estimator for large–dimensional covariance matrices")),
and alternative risk measures such as CVaR
(Rockafellar and Uryasev, [2000](https://arxiv.org/html/2601.06271v1#bib.bib5 "Optimization of conditional value–at–risk")).
Recent work explores multi-factor or multi-risk frontiers, eg, g, adding tail risk or skewness
(Deguest and Martellini, [2015](https://arxiv.org/html/2601.06271v1#bib.bib6 "Improving mean–variance optimization when drawdown matters")),
but these remain *variance‐centric* and do not capture
shock propagation in financial networks.

### 2.2 Econometric Measures of Connectedness

The network perspective on systemic risk originates with
Mantegna ([1999](https://arxiv.org/html/2601.06271v1#bib.bib11 "Hierarchical structure in financial markets")),
who visualize equity markets through a correlation-based
minimum spanning tree.
Diebold and Yilmaz
([2009](https://arxiv.org/html/2601.06271v1#bib.bib7 "Measuring financial asset return and volatility spillovers, with application to global equity markets"), [2012](https://arxiv.org/html/2601.06271v1#bib.bib8 "Better to give than to receive: predictive directional measurement of volatility spillovers"),
[2014](https://arxiv.org/html/2601.06271v1#bib.bib9 "On the network topology of variance decompositions: measuring the connectedness of financial firms"))
pioneer the VAR–FEVD spillover index,
quantifying how much of the forecast variance of asset ii is
explained by shocks to asset jj.
Extensions include frequency domain connectivity (Baruník and Křehlík, [2018](https://arxiv.org/html/2601.06271v1#bib.bib15 "Measuring the frequency dynamics of financial connectedness and systemic risk")) and systemic risk networks in the finance-insurance nexus
(Billio et al., [2012](https://arxiv.org/html/2601.06271v1#bib.bib10 "Econometric measures of connectedness and systemic risk in the finance and insurance sectors")).
These studies consistently find that connectedness increases
during crises, underscoring its importance beyond variance.

### 2.3 Network–Based Portfolio Selection

A growing body of literature exploits network metrics for
asset allocation.
Pozzi et al. ([2013](https://arxiv.org/html/2601.06271v1#bib.bib12 "Spread of risk across financial markets: better to invest in the peripheries")) show empirically that tilting towards
*peripheral* equities in a correlation network yields
superior Sharpe ratios.
Peralta and Zareei ([2016](https://arxiv.org/html/2601.06271v1#bib.bib13 "A network approach to portfolio selection")) provide a theoretical link between
eigenvector centrality and optimal mean variance weights,
while Tumminello et al. ([2010](https://arxiv.org/html/2601.06271v1#bib.bib14 "Correlation, hierarchies, and networks in financial markets")) advocate filtering noisy
correlation matrices through planarity-constrained graphs
for risk reduction.
More recently, Broadstock et al. ([2022b](https://arxiv.org/html/2601.06271v1#bib.bib16 "Minimum connectedness portfolios: diversifying through network risk")) introduced
*Minimum Connectedness Portfolio* (MCoP),
minimizing w⊤​C​ww^{\top}Cw alone.
These contributions confirm the economic value of network
information but remain single–objective or heuristic,
leaving unanswered how to
optimize expected return, variance,
and connectedness *jointly*.

### 2.4 Multi–Objective Risk Optimization

Beyond variance, multi–objective frameworks account for
CVaR, drawdown, or higher moments
(Rockafellar and Uryasev, [2000](https://arxiv.org/html/2601.06271v1#bib.bib5 "Optimization of conditional value–at–risk"); Deguest and Martellini, [2015](https://arxiv.org/html/2601.06271v1#bib.bib6 "Improving mean–variance optimization when drawdown matters")),
typically through scalarisation or ε\varepsilon-contraint methods.
Our work differs in that the risk of connectedness is
*economically orthogonal* to variance and correlation,
arising from the dynamic spillover topology, not from
contemporaneous co-movement.
We therefore extend the efficient frontier to a three-dimensional surface
(𝔼​[r],σ,κ)(\mathbb{E}[r],\sigma,\kappa), in which variance and
connectedness appear as coequal quadratic forms.
To our knowledge, this is the first attempt to provide
closed‐form characterization, marginal beta interpretation,
and empirical visualization of such a surface.
f

## 3 Model and Optimization Framework

### 3.1 Setting and Notation

Let NN\! risky assets have random gross returns
𝐫=(r1,…,rN)𝖳\mathbf{r}=(r\_{1},\dots,r\_{N})^{\mathsf{T}}. Denote by

|  |  |  |
| --- | --- | --- |
|  | 𝝁=𝔼​[𝐫],Σ=Cov⁡(𝐫)\boldsymbol{\mu}=\mathbb{E}[\mathbf{r}],\qquad\Sigma=\operatorname{Cov}(\mathbf{r}) |  |

the expected return vector and the covariance matrix N×NN\times N.
A portfolio is a weight vector
w=(w1,…,wN)𝖳w=(w\_{1},\dots,w\_{N})^{\mathsf{T}} satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏𝖳​w=1,wi≥0​(i=1,…,N).\mathbf{1}^{\mathsf{T}}w=1,\qquad w\_{i}\geq 0\;\;(i=1,\dots,N). |  | (1) |

The expected return and variance of the portfolio are
𝔼​[rp]=w𝖳​𝝁,σp2=w𝖳​Σ​w.\mathbb{E}[r\_{p}]=w^{\mathsf{T}}\boldsymbol{\mu},\;\sigma\_{p}^{2}=w^{\mathsf{T}}\Sigma w.

Connectedness matrix.
To capture the risk of network spillover, we introduce a symmetric,
positive semidefinite matrix CC (e.g., the Diebold-Yilmaz FEVD
matrix; Diebold and Yilmaz, [2014](https://arxiv.org/html/2601.06271v1#bib.bib9 "On the network topology of variance decompositions: measuring the connectedness of financial firms"); Billio et al., [2012](https://arxiv.org/html/2601.06271v1#bib.bib10 "Econometric measures of connectedness and systemic risk in the finance and insurance sectors")).
Define the portfolio’s *connectedness risk*

|  |  |  |  |
| --- | --- | --- | --- |
|  | κp=w𝖳​C​w.\kappa\_{p}\;=\;w^{\mathsf{T}}C\,w. |  | (2) |

### 3.2 Joint Risk Objective

For a trade-off parameter λ∈[0,1]\lambda\in[0,1] we minimize

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lλ​(w)=λ​w𝖳​Σ​w+(1−λ)​w𝖳​C​w,L\_{\lambda}(w)\;=\;\lambda\,w^{\mathsf{T}}\Sigma w\;+\;(1-\lambda)\,w^{\mathsf{T}}Cw, |  | (3) |

subject to ([1](https://arxiv.org/html/2601.06271v1#S3.E1 "In 3.1 Setting and Notation ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization")).
Setting λ=1\lambda=1 recovers the global minimum-variance portfolio,
while λ=0\lambda=0 produces the minimum-connectedness portfolio
(Broadstock et al., [2022a](https://arxiv.org/html/2601.06271v1#bib.bib18 "Minimum connectedness portfolios and the market for green bonds")).
Varying λ\lambda traces a risk–risk frontier
(σp​(λ),κp​(λ))\bigl(\sigma\_{p}(\lambda),\kappa\_{p}(\lambda)\bigr);
adding a return target sweeps the entire
three-dimensional efficient surface
(𝔼​[rp],σp,κp)\bigl(\mathbb{E}[r\_{p}],\sigma\_{p},\kappa\_{p}\bigr).

### 3.3 Main Propositions

###### Proposition 1 (Existence and (Conditional) Uniqueness).

Fix a trade‑off parameter λ∈[0,1]\lambda\in[0,1] and consider the quadratic
program

|  |  |  |
| --- | --- | --- |
|  | minw∈ℝN⁡Lλ​(w)=λ​w𝖳​Σ​w+(1−λ)​w𝖳​C​ws.t.​ 1𝖳​w=1,wi≥0.\min\_{w\in\mathbb{R}^{N}}L\_{\lambda}(w)=\lambda\,w^{\mathsf{T}}\Sigma w+(1-\lambda)\,w^{\mathsf{T}}Cw\quad\text{s.t.}\;\mathbf{1}^{\mathsf{T}}w=1,\;\;w\_{i}\geq 0. |  |

Assume Σ≻0\Sigma\succ 0 and C⪰0C\succeq 0. Then

1. (i)

   Existence (all λ\lambda). 
   A minimizer w∗​(λ)w^{\ast}(\lambda) exists for every
   λ∈[0,1]\lambda\in[0,1].
2. (ii)

   Uniqueness (strictly positive‑definite case). 
   If either λ>0\lambda>0 or C≻0C\succ 0
   —so that
   Mλ:=λ​Σ+(1−λ)​C≻0M\_{\lambda}:=\lambda\Sigma+(1-\lambda)C\succ 0—
   the minimizer is unique.
3. (iii)

   Continuity of the solution map. 
   On any closed subinterval of [0,1][0,1] where the minimizer is unique, the mapping λ↦w∗​(λ)\lambda\mapsto w^{\ast}(\lambda) is continuous.
   In particular, it is continuous on (0,1](0,1] and on all of [0,1][0,1]
   whenever C≻0C\succ 0.

###### Proof.

Step 1 (compact feasible set).
The constraints
𝟏𝖳​w=1,wi≥0\mathbf{1}^{\mathsf{T}}w=1,\;w\_{i}\geq 0
confine ww to the closed simplex

|  |  |  |
| --- | --- | --- |
|  | 𝒲={w∈ℝN: 1𝖳​w=1,w≥0},\mathcal{W}\;=\;\bigl\{w\in\mathbb{R}^{N}:\,\mathbf{1}^{\mathsf{T}}w=1,\;w\geq 0\bigr\}, |  |

which is closed and bounded, and hence compact.

Step 2 (existence).
For fixed λ\lambda the loss
Lλ​(w)L\_{\lambda}(w) is continuous in ww.
By the extreme value theorem, a continuous function attains its infimum
in a compact set, so there is at least one minimizer
w∗​(λ)∈𝒲w^{\ast}(\lambda)\in\mathcal{W} exists—establishing (i).

Step 3 (strict convexity and uniqueness).
Set
Mλ:=λ​Σ+(1−λ)​CM\_{\lambda}:=\lambda\Sigma+(1-\lambda)C.
If λ>0\lambda>0 or C≻0C\succ 0 then
Mλ≻0M\_{\lambda}\succ 0; the quadratic form
w↦w𝖳​Mλ​ww\mapsto w^{\mathsf{T}}M\_{\lambda}w is *strictly* convex, hence it
admits at most one minimizer in the convex set 𝒲\mathcal{W}.
This proves (ii).
When λ=0\lambda=0 and CC is singular, M0=CM\_{0}=C is only
positive‑semidefinite; the objective is merely convex, so multiple
minimizer can arise (e.g. C=0C=0 makes every w∈𝒲w\in\mathcal{W}
optimal). We therefore refrain from a blanket uniqueness claim in that
degenerate case.

Step 4 (continuity of the minimizer).
Restrict attention to any closed interval on which
Mλ≻0M\_{\lambda}\succ 0 so that the minimizer is unique.
The map

|  |  |  |
| --- | --- | --- |
|  | λ⟼Mλ\lambda\;\longmapsto\;M\_{\lambda} |  |

is continuous in the operator norm.
Because matrix inversion is continuous on the cone of positive definite matrices, the closed-form expression
w∗​(λ)=Mλ−1​𝟏/[𝟏𝖳​Mλ−1​𝟏]w^{\ast}(\lambda)=M\_{\lambda}^{-1}\mathbf{1}\big/\bigl[\mathbf{1}^{\mathsf{T}}M\_{\lambda}^{-1}\mathbf{1}\bigr]
is continuous in λ\lambda.
Hence, the single-valued selection
λ↦w∗​(λ)\lambda\mapsto w^{\ast}(\lambda) is continuous wherever
Mλ≻0M\_{\lambda}\succ 0, proving (iii). ∎

###### Proposition 2 (Closed‑Form Optimal Weights (short‑selling allowed; see Appendix A for the long‑only case)).

Assume that the two risk matrices are simultaneously diagonalizable, i.e.
there exists an orthogonal matrix UU such that

|  |  |  |
| --- | --- | --- |
|  | Σ=U​ΛΣ​U𝖳,C=U​ΛC​U𝖳,\Sigma\;=\;U\Lambda\_{\Sigma}U^{\mathsf{T}},\qquad C\;=\;U\Lambda\_{C}U^{\mathsf{T}}, |  |

with diagonal entries σi2>0\sigma\_{i}^{2}>0 and ci>0c\_{i}>0.
Fix a trade‑off parameter λ∈[0,1]\lambda\in[0,1] and define

|  |  |  |
| --- | --- | --- |
|  | Mλ:=λ​Σ+(1−λ)​C.M\_{\lambda}\;:=\;\lambda\Sigma\;+\;(1-\lambda)C. |  |

Under the *sole* budget constraint

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏𝖳​w= 1,\mathbf{1}^{\mathsf{T}}w\;=\;1, |  | (4) |

and allowing individual asset positions to take any real value
(short‑selling permitted), the quadratic programme

|  |  |  |
| --- | --- | --- |
|  | minw∈ℝN⁡Lλ​(w)=w𝖳​Mλ​w\min\_{w\in\mathbb{R}^{N}}L\_{\lambda}(w)=w^{\mathsf{T}}M\_{\lambda}w |  |

admits the unique optimum

|  |  |  |  |
| --- | --- | --- | --- |
|  | w∗​(λ)=Mλ−1​𝟏𝟏𝖳​Mλ−1​𝟏.w^{\ast}(\lambda)\;=\;\frac{M\_{\lambda}^{-1}\mathbf{1}}{\mathbf{1}^{\mathsf{T}}M\_{\lambda}^{-1}\mathbf{1}}. |  | (5) |

###### Proof.

Step 1 (Lagrangian).
Introduce a multiplier ν\nu for ([4](https://arxiv.org/html/2601.06271v1#S3.E4 "In Proposition 2 (Closed‑Form Optimal Weights (short‑selling allowed; see Appendix A for the long‑only case)). ‣ 3.3 Main Propositions ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization")) and set

|  |  |  |
| --- | --- | --- |
|  | ℒ​(w,ν)=w𝖳​Mλ​w−ν​(𝟏𝖳​w−1).\mathcal{L}(w,\nu)\;=\;w^{\mathsf{T}}M\_{\lambda}w\;-\;\nu\bigl(\mathbf{1}^{\mathsf{T}}w-1\bigr). |  |

Step 2 (first‑order condition).
Differentiating with respect to ww gives
2​Mλ​w−ν​𝟏=0⟹w=ν2​Mλ−1​𝟏.2M\_{\lambda}w-\nu\mathbf{1}=0\;\Longrightarrow\;w=\tfrac{\nu}{2}\,M\_{\lambda}^{-1}\mathbf{1}.

Step 3 (enforce the budget).
Imposing 𝟏𝖳​w=1\mathbf{1}^{\mathsf{T}}w=1 yields

|  |  |  |
| --- | --- | --- |
|  | ν2=[𝟏𝖳​Mλ−1​𝟏]−1.\frac{\nu}{2}\;=\;\bigl[\mathbf{1}^{\mathsf{T}}M\_{\lambda}^{-1}\mathbf{1}\bigr]^{-1}. |  |

Substituting back gives the closed form
([5](https://arxiv.org/html/2601.06271v1#S3.E5 "In Proposition 2 (Closed‑Form Optimal Weights (short‑selling allowed; see Appendix A for the long‑only case)). ‣ 3.3 Main Propositions ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization")).

Step 4 (optimality and uniqueness).
Because Σ≻0\Sigma\succ 0 and C⪰0C\succeq 0, we have Mλ≻0M\_{\lambda}\succ 0
for all λ∈[0,1]\lambda\in[0,1].
The objective w𝖳​Mλ​ww^{\mathsf{T}}M\_{\lambda}w is therefore
*strictly* convex, so the stationary point found above is the
*unique* global minimizer subject to ([4](https://arxiv.org/html/2601.06271v1#S3.E4 "In Proposition 2 (Closed‑Form Optimal Weights (short‑selling allowed; see Appendix A for the long‑only case)). ‣ 3.3 Main Propositions ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization")).
∎

#### Remark (long‑only portfolios).

If one additionally imposes wi≥0w\_{i}\geq 0, the vector
([5](https://arxiv.org/html/2601.06271v1#S3.E5 "In Proposition 2 (Closed‑Form Optimal Weights (short‑selling allowed; see Appendix A for the long‑only case)). ‣ 3.3 Main Propositions ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization")) is still optimal *iff* every
component is nonnegative. Otherwise, the problem becomes a bounded
quadratic program whose solution no longer admits a one‑line closed
form; it must be obtained via KKT complementarity or numerical solvers
(e.g. activeset or interiorpoint methods). Appendix B contains a
full KKT derivation together with an efficient active set algorithm and
a numerical illustration.

###### Proposition 3 (Strict Trade–off: Negative Slope).

Let
σ2​(λ)=w∗​(λ)𝖳​Σ​w∗​(λ)\sigma^{2}(\lambda)=w^{\ast}(\lambda)^{\mathsf{T}}\Sigma w^{\ast}(\lambda)
and
κ​(λ)=w∗​(λ)𝖳​C​w∗​(λ),\kappa(\lambda)=w^{\ast}(\lambda)^{\mathsf{T}}Cw^{\ast}(\lambda),
where w∗​(λ)w^{\ast}(\lambda) is the unique minimizer of
([3](https://arxiv.org/html/2601.06271v1#S3.E3 "In 3.2 Joint Risk Objective ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization")) for a given λ∈(0,1)\lambda\in(0,1).
If Σ\Sigma and CC are not proportional, then

|  |  |  |
| --- | --- | --- |
|  | σ2⁣′​(λ)<0,κ′​(λ)>0,d​σ2d​κ=−1−λλ< 0.\sigma^{2\,\prime}(\lambda)<0,\qquad\kappa^{\prime}(\lambda)>0,\qquad\frac{\mathrm{d}\sigma^{2}}{\mathrm{d}\kappa}=-\frac{1-\lambda}{\lambda}\;<\;0. |  |

Therefore, the efficient frontier in the (σ,κ)(\sigma,\kappa) plane is strictly
downward-sloping: One cannot decrease the risk of connectedness without
increasing variance.

###### Proof (concise convex–analytic argument).

For each λ\lambda define
Mλ=λ​Σ+(1−λ)​CM\_{\lambda}=\lambda\Sigma+(1-\lambda)C
and let
F​(λ)=minw∈𝒲⁡w𝖳​Mλ​wF(\lambda)=\min\_{w\in\mathcal{W}}w^{\mathsf{T}}M\_{\lambda}w.
Because Lλ​(w)=w𝖳​Mλ​wL\_{\lambda}(w)=w^{\mathsf{T}}M\_{\lambda}w is strictly convex in
ww and linear in λ\lambda, the map FF is (i) differentiable and
(ii) *concave* on (0,1)(0,1).

Step 1 (Envelope theorem).
At the optimum
w∗​(λ)w^{\ast}(\lambda) we have

|  |  |  |
| --- | --- | --- |
|  | F′​(λ)=∂λ[w𝖳​Mλ​w]w=w∗=w∗𝖳​(Σ−C)​w∗=σ2​(λ)−κ​(λ).F^{\prime}(\lambda)=\partial\_{\lambda}\bigl[w^{\mathsf{T}}M\_{\lambda}w\bigr]\_{w=w^{\ast}}=w^{\ast\mathsf{T}}(\Sigma-C)w^{\ast}=\sigma^{2}(\lambda)-\kappa(\lambda). |  |

Step 2 (Total derivative).
Since
F​(λ)=λ​σ2+(1−λ)​κF(\lambda)=\lambda\sigma^{2}+(1-\lambda)\kappa,

|  |  |  |
| --- | --- | --- |
|  | F′​(λ)=σ2−κ+λ​σ2⁣′−(1−λ)​κ′.F^{\prime}(\lambda)=\sigma^{2}-\kappa+\lambda\sigma^{2\,\prime}-(1-\lambda)\kappa^{\prime}. |  |

Step 3 (Linear relation).
Equating (A) and (B) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​σ2⁣′+(1−λ)​κ′=0.\lambda\,\sigma^{2\,\prime}+(1-\lambda)\,\kappa^{\prime}=0. |  | (5) |

Step 4 (Concavity sign).
Concavity of FF implies
F′′​(λ)=σ2⁣′−κ′≤0F^{\prime\prime}(\lambda)=\sigma^{2\,\prime}-\kappa^{\prime}\leq 0.

Step 5 (Sign of derivatives).
The system ([5](https://arxiv.org/html/2601.06271v1#S3.E5a "In Proof (concise convex–analytic argument). ‣ Remark (long‑only portfolios). ‣ 3.3 Main Propositions ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization")) and F′′≤0F^{\prime\prime}\leq 0 forces
σ2⁣′<0\sigma^{2\,\prime}<0 and κ′>0\kappa^{\prime}>0
whenever Σ∝̸C\Sigma\not\propto C (otherwise both derivatives would be
zero). Dividing the two derivatives yields
d​σ2/d​κ=−(1−λ)/λ<0,\mathrm{d}\sigma^{2}/\mathrm{d}\kappa=-(1-\lambda)/\lambda<0,
establishing the strictly negative slope.

An explicit eigen-component derivation, applicable when Σ\Sigma and CC share a common orthonormal eigenbasis, is provided in Appendix B. This supplement facilitates numerical sensitivity analysis and isolates the contribution of individual spectral factors. ∎

###### Proposition 4 (Degenerate Case: C=c​ΣC=c\,\Sigma).

Let Σ≻0\Sigma\succ 0 and suppose the connectedness matrix is a positive
scalar multiple of the covariance matrix,

|  |  |  |  |
| --- | --- | --- | --- |
|  | C=c​Σ,c>0.C=c\,\Sigma,\qquad c>0. |  | (6) |

Under the sole budget constraint
𝟏𝖳​w=1\mathbf{1}^{\mathsf{T}}w=1
and allowing short sales, every feasible portfolio satisfies the
linear relation

|  |  |  |
| --- | --- | --- |
|  | κp​(w)=c​σp2​(w),\kappa\_{p}(w)\;=\;c\,\sigma\_{p}^{2}(w), |  |

so all attainable risk pairs lie on the single ray
κ=c​σ2\kappa=c\,\sigma^{2}.

Moreover, the quadratic objective

|  |  |  |
| --- | --- | --- |
|  | Lλ​(w)=λ​w𝖳​Σ​w+(1−λ)​w𝖳​C​wL\_{\lambda}(w)=\lambda\,w^{\mathsf{T}}\Sigma w+(1-\lambda)\,w^{\mathsf{T}}Cw |  |

reduces to a positive scalar multiple of variance,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lλ​(w)=[λ+(1−λ)​c]​w𝖳​Σ​w,L\_{\lambda}(w)=\bigl[\lambda+(1-\lambda)c\bigr]\,w^{\mathsf{T}}\Sigma w, |  | (7) |

so for *every* λ∈[0,1]\lambda\in[0,1] the unique minimizer is the
global minimum‑variance portfolio

|  |  |  |  |
| --- | --- | --- | --- |
|  | wMV=Σ−1​𝟏𝟏𝖳​Σ−1​𝟏.w^{\mathrm{MV}}\;=\;\frac{\Sigma^{-1}\mathbf{1}}{\mathbf{1}^{\mathsf{T}}\Sigma^{-1}\mathbf{1}}. |  | (8) |

Hence, the trade-off parameter λ\lambda is redundant and the entire
risk–risk frontier collapses to the straight line
κ=c​σ2\kappa=c\,\sigma^{2} through the origin.

###### Proof.

Step 1 (linear dependence of the two risks).
From ([6](https://arxiv.org/html/2601.06271v1#S3.E6 "In Proposition 4 (Degenerate Case: 𝐶=𝑐⁢Σ). ‣ Remark (long‑only portfolios). ‣ 3.3 Main Propositions ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization"))

|  |  |  |
| --- | --- | --- |
|  | κp​(w)=w𝖳​C​w=c​w𝖳​Σ​w=c​σp2​(w)\kappa\_{p}(w)=w^{\mathsf{T}}Cw=c\,w^{\mathsf{T}}\Sigma w=c\,\sigma\_{p}^{2}(w) |  |

holds for every feasible ww, proving the frontier degenerates to the
ray κ=c​σ2\kappa=c\,\sigma^{2}.

Step 2 (objective collapses to scaled variance).
Substituting ([6](https://arxiv.org/html/2601.06271v1#S3.E6 "In Proposition 4 (Degenerate Case: 𝐶=𝑐⁢Σ). ‣ Remark (long‑only portfolios). ‣ 3.3 Main Propositions ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization")) into the joint loss
gives ([7](https://arxiv.org/html/2601.06271v1#S3.E7 "In Proposition 4 (Degenerate Case: 𝐶=𝑐⁢Σ). ‣ Remark (long‑only portfolios). ‣ 3.3 Main Propositions ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization")). The scalar factor in
brackets is strictly positive because λ,c∈(0,1]\lambda,c\in(0,1].

Step 3 (unique optimizer).
Minimizing ([7](https://arxiv.org/html/2601.06271v1#S3.E7 "In Proposition 4 (Degenerate Case: 𝐶=𝑐⁢Σ). ‣ Remark (long‑only portfolios). ‣ 3.3 Main Propositions ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization")) is therefore
equivalent to the classical minimum‑variance problem

|  |  |  |
| --- | --- | --- |
|  | minw⁡w𝖳​Σ​ws.t. ​𝟏𝖳​w=1,\min\_{w}\;w^{\mathsf{T}}\Sigma w\quad\text{s.t. }\mathbf{1}^{\mathsf{T}}w=1, |  |

whose unique solution under short selling is exactly
([8](https://arxiv.org/html/2601.06271v1#S3.E8 "In Proposition 4 (Degenerate Case: 𝐶=𝑐⁢Σ). ‣ Remark (long‑only portfolios). ‣ 3.3 Main Propositions ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization")). Since the objective differs only by a
positive constant factor, the same wMVw^{\mathrm{MV}} minimizes
LλL\_{\lambda} for *all* λ\lambda.

Step 4 (economic interpretation).
Because connectedness does not add information beyond variance when
C∝ΣC\propto\Sigma, investors do not obtain a diversification benefit from
treating κp\kappa\_{p} separately; the optimization problem reduces to
the mean-variance analysis and the third dimension of risk is redundant.
∎

#### Remark (long‑only portfolios).

If non‑negativity constraints wi≥0w\_{i}\geq 0 are imposed, the relation
κ=c​σ2\kappa=c\,\sigma^{2} still holds, but the minimum variance weights
can no longer be written in closed form; the problem becomes a bounded
quadratic program solved by active set or interior point methods.
Appendix A outlines the required KKT conditions and provides an
efficient algorithmic routine.

### 3.4 Connectedness β\beta and Three–Fund Separation

#### Definition.

For a portfolio with weight vector ww and connectedness matrix
CC, we define *connectedness beta* of the asset ii by

|  |  |  |
| --- | --- | --- |
|  | βi(C):=2​[C​w]i,i=1,…,n.\beta^{(C)}\_{i}:=2\,[Cw]\_{i},\qquad i=1,\dots,n. |  |

Because w𝖳​C​w=κpw^{\mathsf{T}}Cw=\kappa\_{p}, the betas satisfy

|  |  |  |
| --- | --- | --- |
|  | ∑i=1nwi​βi(C)= 2​κp.\sum\_{i=1}^{n}w\_{i}\,\beta^{(C)}\_{i}\;=\;2\,\kappa\_{p}. |  |

Assets with large β(C)\beta^{(C)} behave as systemic *hubs*111In network terminology, a *hub* is a node with unusually high
degree, eigenvector centrality, or forecast‐error variance share; shocks
to such nodes propagate disproportionately through the system
(Kleinberg 2012, *Journal of the ACM*)..
That is, they occupy highly connected positions in the spillover
network, so tilting a portfolio toward these names increases its overall
risk of connectedness κp\kappa\_{p}.

###### Theorem 1 (Conditional Three–Fund Separation).

Let

|  |  |  |
| --- | --- | --- |
|  | wMV:=argmin𝟏𝖳​w=1w𝖳Σw,wMC:=argmin𝟏𝖳​w=1w𝖳Cw,\displaystyle w^{\mathrm{MV}}:=\arg\min\_{\mathbf{1}^{\mathsf{T}}w=1}\,w^{\mathsf{T}}\Sigma w,\qquad w^{\mathrm{MC}}:=\arg\min\_{\mathbf{1}^{\mathsf{T}}w=1}\,w^{\mathsf{T}}Cw, |  |

and let
wmax⁡μw^{\max\mu} denote the maximum–return portfolio
arg⁡max𝟏𝖳​w=1⁡w𝖳​𝛍\arg\max\_{\mathbf{1}^{\mathsf{T}}w=1}w^{\mathsf{T}}\boldsymbol{\mu}.
Moreover, assume that individual *asset* positions are not restricted (short selling allowed). The convex coefficients
αk≥0\alpha\_{k}\geq 0 introduced in the following apply only at the level *fund*.

Suppose that

1. (a)

   the three portfolios are distinct and the matrix
   W0:=[wMV,wMC,wmax⁡μ]W\_{0}:=[\,w^{\mathrm{MV}},\;w^{\mathrm{MC}},\;w^{\max\mu}\,]
   has full rank N−1N\!\!-\!1 in the subspace
   {w∈ℝN:𝟏𝖳​w=1}\{w\in\mathbb{R}^{N}:\mathbf{1}^{\mathsf{T}}w=1\};
2. (b)

   for every λ∈[0,1]\lambda\in[0,1] the unique minimizer
   w∗​(λ)w^{\ast}(\lambda) of
   Lλ​(w)=λ​w𝖳​Σ​w+(1−λ)​w𝖳​C​wL\_{\lambda}(w)=\lambda w^{\mathsf{T}}\Sigma w+(1-\lambda)w^{\mathsf{T}}Cw
   satisfies
   w∗​(λ)∈conv⁡{wMV,wMC,wmax⁡μ}w^{\ast}(\lambda)\in\operatorname{conv}\{w^{\mathrm{MV}},w^{\mathrm{MC}},w^{\max\mu}\},
   i.e. lies in the closed convex hull of the three corner funds.
   This containment obtains, for example, when
   Σ\Sigma and CC are simultaneously diagonalisable,
   all diagonal entries are positive, and
   𝝁\boldsymbol{\mu} as well as 𝟏\mathbf{1} lie in the positive
   cone spanned by the common eigenvectors.222Under the simultaneous–diagonalization condition the efficient
   surface parameterized by λ\lambda is itself convex; if,
   additionally, the three corner portfolios occupy the extreme
   points of that convex set, assumption (b) is automatically met.

Then every efficient portfolio w∗​(λ)w^{\ast}(\lambda) admits a
*three–fund representation*

|  |  |  |
| --- | --- | --- |
|  | w∗​(λ)=α1​(λ)​wMV+α2​(λ)​wMC+α3​(λ)​wmax⁡μ,αk​(λ)≥0,∑k=13αk​(λ)=1,w^{\ast}(\lambda)\;=\;\alpha\_{1}(\lambda)\,w^{\mathrm{MV}}\;+\;\alpha\_{2}(\lambda)\,w^{\mathrm{MC}}\;+\;\alpha\_{3}(\lambda)\,w^{\max\mu},\qquad\alpha\_{k}(\lambda)\geq 0,\;\sum\_{k=1}^{3}\alpha\_{k}(\lambda)=1, |  |

and the coefficients αk​(λ)\alpha\_{k}(\lambda) are unique.

###### Proof.

Step 1 (linear independence).
Condition (a) implies that the three fund vectors, augmented by
𝟏\mathbf{1}, form a matrix N×NN\times N of full rank:
W^:=[ 1,wMV,wMC,wmax⁡μ]\widehat{W}:=[\,\mathbf{1},\;w^{\mathrm{MV}},\;w^{\mathrm{MC}},\;w^{\max\mu}\,]
is invertible on ℝN\mathbb{R}^{N}. Hence, they affinely span the entire
budget hyperplane {w:𝟏𝖳​w=1}\{w:\mathbf{1}^{\mathsf{T}}w=1\}.

Step 2 (containment of the efficient set).
Assumption (b) specifies precisely that each
w∗​(λ)w^{\ast}(\lambda) belongs to *convex hull*
𝒮:=conv⁡{wMV,wMC,wmax⁡μ}\mathcal{S}:=\operatorname{conv}\{w^{\mathrm{MV}},w^{\mathrm{MC}},w^{\max\mu}\}.
Because 𝒮\mathcal{S} is a simplex in the
(N−1)(N\!-\!1)-dimensional budget hyperplane, every point in 𝒮\mathcal{S}
has a *unique* barycentric coordinate
(α1,α2,α3)(\alpha\_{1},\alpha\_{2},\alpha\_{3}) with
αk≥0,∑αk=1\alpha\_{k}\geq 0,\,\sum\alpha\_{k}=1.

Step 3 (representation of the efficient portfolio).
Thus, for the given λ\lambda there exist unique numbers
αk​(λ)\alpha\_{k}(\lambda) satisfying the stated constraints such that
w∗​(λ)=∑kαk​(λ)​wk(⋅)w^{\ast}(\lambda)=\sum\_{k}\alpha\_{k}(\lambda)\,w^{(\cdot)}\_{k}.
The proof is complete. ∎

#### Remarks.

1. (i)

   If assumption (b) is violated, for example, when the risk matrices are highly misaligned and w∗​(λ)w^{\ast}(\lambda) leaves the convex hull 𝒮\mathcal{S} for some λ\lambda-the barycentric coefficients may still exist but can become negative, in which case the representation remains *affine* rather than *convex*. Numerical examples of this failure mode are given
   in Appendix C.
2. (ii)

   When individual long‑only constraints wi≥0w\_{i}\!\geq 0 are imposed,
   condition (a) can be preserved but (b) almost never holds; the
   efficient set typically bends outside the simplex
   𝒮\mathcal{S}. Therefore, three-fund separation requires unrestricted short-selling at the *asset* level, whereas αk\alpha\_{k} only needs to be non-negative at the *fund* level.

#### Economic Interpretation.

A connectedness beta, βi(C)\beta\_{i}^{(C)}, plays exactly the same
diagnostic role for κp\kappa\_{p} as a CAPM beta for variance: it
measures the marginal increase in network spill-over risk generated by
an additional unit of wealth in the asset ii. Stocks with exceptionally
large stocks β(C)\beta^{(C)} are systemic *hubs*; a shock to any of them
quickly feeds into many others and inflates the quadratic form
w𝖳​C​ww^{\mathsf{T}}Cw. Moving portfolio weight away from those hubs and
towards the minimum-connectedness corner fund wMCw^{\mathrm{MC}}
mechanically lowers the weighted average
∑iwi​βi(C)=2​κp\sum\_{i}w\_{i}\beta\_{i}^{(C)}=2\kappa\_{p} without necessarily sacrificing
expected return. In practice, an investor can hedge crisis exposure by
tilting along the *MC–MV* edge of the three-fund simplex: a small
increase in ex ante volatility buys a large reduction in systemic
fragility, as evidenced by our empirical surface in Section LABEL:sec:empirical.

#### Illustrative Figures.

![Refer to caption](x1.png)


Figure 1: Illustrative distribution of the top-15 connectedness betas
βi(C)\beta^{(C)}\_{i} on a single trading day
(31 Dec 2024) using a randomly selected
100-stock subset of NYSE-listed stocks.
The figure is intended solely as a didactic
example to visualize the heavy-tailed nature of
β(C)\beta^{(C)}; all formal empirical tests in
Section LABEL:sec:empirical employ the full universe and
rolling estimates.

![Refer to caption](x2.png)


Figure 2: Barycentric representation of efficient portfolios spanned by the
three corner funds—minimum variance (MV), minimum connectedness
(MC), and tangency (Tan). Moving toward MC (resp. MV)
lowers connectedness risk κ\kappa (resp. variance σ2\sigma^{2}).
*Dots represent the optimal portfolio for
λ∈{0,0.05,…,1}\lambda\in\{0,0.05,\dots,1\} in the hybrid risk matrix
M​(λ)=λ​Σ+(1−λ)​CM(\lambda)=\lambda\Sigma+(1-\lambda)C.*

### 3.5 Preview of Empirical Analysis

The theoretical machinery of Sections 3.1–3.4 motivates three sets of
empirical tests, all implemented with *daily* S&P 500 data from
January 2010 to May 2025.333Market returns are obtained from CRSP;
the one–month Treasury bill is the risk–free rate. Sector deletions,
splits, and ticker substitutions are handled as in Hou, Xue and Zhang
(2020). For each trading day tt we estimate

1. (i)

   a shrinkage covariance matrix
   Σ^t\hat{\Sigma}\_{t} using a 252252-day rolling window;
2. (ii)

   a one-lag VAR on the same window and its 10-day FEVD to obtain the
   connectedness matrix C^t\hat{C}\_{t};
3. (iii)

   the trade-off price λ^t\hat{\lambda}\_{t} by minimizing the realized
   loss function ([3](https://arxiv.org/html/2601.06271v1#S3.E3 "In 3.2 Joint Risk Objective ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization")) across a coarse grid.

These objects directly feed into the hypotheses to be examined in
Section 5:

H1:
:   Portfolios that tilt towards the
    minimal‐connectedness fund wMCw^{\mathrm{MC}} achieve significantly lower
    tail risk and drawdown relative to the global minimum variation portfolio
    without sacrificing average return.

H2:
:   Stocks in the highest decile of the beta of connectedness
    β(C)\beta^{(C)} underperform low-β(C)\beta^{(C)} stocks when
    λ^t\hat{\lambda}\_{t} - the market price of connectedness risk—spikes; the
    spread is amplified during VIX surges.

H3:
:   A dynamic three-fund strategy
    {wMV,wMC,wTan}\{w^{\mathrm{MV}},w^{\mathrm{MC}},w^{\mathrm{Tan}}\} tracks the fully
    re-optimized efficient portfolio with monthly
    rebalancing *ex ante* tracking error below 5050 bp and
    transaction cost drag below 2020 bp p.a.

The next section details the construction of test portfolios, regression
specifications, and robustness diagnostics corresponding to
H1–H3.

### 3.6 Connectedness vs. Conventional Volatility

Table LABEL:tables:tc\_vix\_lit situates our null finding within the
literature. Consistent with Diebold and Yilmaz ([2009](https://arxiv.org/html/2601.06271v1#bib.bib7 "Measuring financial asset return and volatility spillovers, with application to global equity markets"), [2012](https://arxiv.org/html/2601.06271v1#bib.bib8 "Better to give than to receive: predictive directional measurement of volatility spillovers"))
and a dozen subsequent studies, we observe no economically or
statistically significant *linear* relation between the Total
Connectedness Index (TCI) and contemporaneous market volatility
(VIX or realised σ\sigma) during tranquil periods. Connectedness
appears to spike only in crisis windows—an episodic, regime-dependent
behaviour that a single unconditional β\beta cannot capture.

## Appendix A Robustness to Extreme TCI Spikes

### A.1 Outlier Treatment and Additional Specifications

To rule out that our baseline “flat” βVIX\beta\_{\text{VIX}} is driven by a handful
of extreme TCI spikes, we implement three cleansing strategies:

1. (a)

   1–99% Winsorisation (WIN),
2. (b)

   Median ± 6×\pm\,6\timesMAD trimming (MAD),
3. (c)

   Dropping the 33 windows with TCI >> 150%.

Table LABEL:tables:tc\_vix\_robust reports the OLS estimates; none of the
coefficients are statistically different from zero, corroborating the
findings in Table LABEL:tables:tc\_vix\_lit.

## Appendix A Long‑Only Hybrid‑Risk Optimization

Throughout this appendix, we impose the additional *long‑only*
constraint

|  |  |  |
| --- | --- | --- |
|  | wi≥0(i=1,…,N),𝟏𝖳​w=1.w\_{i}\geq 0\quad(i=1,\dots,N),\qquad\mathbf{1}^{\mathsf{T}}w=1. |  |

For a fixed trade‑off parameter λ∈[0,1]\lambda\in[0,1] write

|  |  |  |
| --- | --- | --- |
|  | Mλ=λ​Σ+(1−λ)​C⪰0.M\_{\lambda}=\lambda\Sigma+(1-\lambda)C\succeq 0. |  |

### A.1   Existence and (Possible) Non‑Uniqueness

###### Proposition A.​ A.1 (Long‑only optimization).

For every λ∈[0,1]\lambda\in[0,1] consider the quadratic programme

|  |  |  |
| --- | --- | --- |
|  | minw∈ℝN⁡w𝖳​Mλ​ws.t.​ 1𝖳​w=1,w≥0.\min\_{w\in\mathbb{R}^{N}}w^{\mathsf{T}}M\_{\lambda}w\quad\text{\emph{s.t.}}\;\mathbf{1}^{\mathsf{T}}w=1,\;w\geq 0. |  |

Then

1. (i)

   Existence. 
   A minimizer wLO​(λ)w^{\mathrm{LO}}(\lambda) exists.
2. (ii)

   Uniqueness. 
   If Mλ≻0M\_{\lambda}\succ 0 and the active index set
   𝒥={i:wiLO​(λ)>0}\mathcal{J}=\{i:w^{\mathrm{LO}}\_{i}(\lambda)>0\}
   satisfies Mλ,𝒥​𝒥≻0M\_{\lambda,\mathcal{J}\mathcal{J}}\succ 0, the minimizer is unique; otherwise multiple optima may occur along the boundary faces of the simplex.

Moreover, the Karush–Kuhn–Tucker system

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​Mλ​w−ν​𝟏−γ\displaystyle 2M\_{\lambda}w-\nu\mathbf{1}-\gamma | =0,\displaystyle=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏𝖳​w\displaystyle\mathbf{1}^{\mathsf{T}}w | =1,\displaystyle=1, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | wi≥0,γi\displaystyle w\_{i}\geq 0,\;\gamma\_{i} | ≥0,γi​wi=0(i=1,…,N)\displaystyle\geq 0,\;\gamma\_{i}w\_{i}=0\quad(i=1,\dots,N) |  |

is necessary and sufficient for optimality, where γ\gamma denotes the
vector of non‑negative inequality multipliers.

###### Proof.

Existence.
The feasible set is a closed, bounded simplex, hence compact; the
objective w𝖳​Mλ​ww^{\mathsf{T}}M\_{\lambda}w is continuous. Therefore, a
minimizer exists by the extreme value theorem.

Uniqueness.
If Mλ≻0M\_{\lambda}\succ 0 the quadratic form is strictly convex on the whole
budget hyperplane. Restricting it to the face
{w:wi=0​ for ​i∉𝒥}\{w:w\_{i}=0\text{ for }i\notin\mathcal{J}\}
yields a quadratic form with Hessian Mλ,𝒥​𝒥M\_{\lambda,\mathcal{J}\mathcal{J}}. When this sub-matrix is positive definite, the restriction is
strictly convex on the face, hence admits a unique minimizer there.
When Mλ,𝒥​𝒥M\_{\lambda,\mathcal{J}\mathcal{J}} loses rank, the form can be
flat in feasible directions, allowing multiple optima.

KKT.
The problem is convex with constraints of affine equality and polyhedral inequality. The Slater condition holds because
(1/N)​𝟏(1/N)\mathbf{1} is strictly feasible; hence, the KKT conditions are necessary
and sufficient.
∎

### A.2   Active‑Set Solver (Pseudo‑code)

Algorithm 1  Active‑set algorithm for long‑only hybrid‑risk portfolio

1:Mλ≽0M\_{\lambda}\succcurlyeq 0, tolerance ε>0\varepsilon>0

2:w←1N​𝟏w\leftarrow\frac{1}{N}\mathbf{1}⊳\triangleright initial strictly feasible point

3:A←{i:wi=0}A\leftarrow\{\,i:w\_{i}=0\,\}, 
F←{1,…,N}∖AF\leftarrow\{1,\dots,N\}\setminus A⊳\triangleright active / free sets

4:repeat

5:  Solve the equality‑constrained QP on FF:

|  |  |  |
| --- | --- | --- |
|  | minpF⁡12​pF𝖳​MF​F​pF​s.t.​ 1F𝖳​pF=0\min\_{p\_{F}}\;\frac{1}{2}p\_{F}^{\mathsf{T}}M\_{FF}p\_{F}\;\;\text{s.t.}\;\mathbf{1}\_{F}^{\mathsf{T}}p\_{F}=0 |  |

Set pi=0p\_{i}=0 for i∈Ai\in A.

6:  Compute ν\nu associated with the equality constraint
(e.g. via the normal equations) and set
γi=(2​Mλ​w−ν​𝟏)i\gamma\_{i}=(2M\_{\lambda}w-\nu\mathbf{1})\_{i} for i∈Ai\in A.

7:  if ‖p‖≤ε\|p\|\leq\varepsilon then

8:   if all γi≥−ε\gamma\_{i}\geq-\varepsilon for i∈Ai\in A then

9:     return ww ⊳\triangleright KKT satisfied → optimal

10:   else

11:     j←arg⁡mini∈A⁡γij\leftarrow\arg\min\_{i\in A}\gamma\_{i}

12:     A←A∖{j}A\leftarrow A\setminus\{j\}; F←F∪{j}F\leftarrow F\cup\{j\}

13:   end if

14:  else

15:   α←max⁡{β∈(0,1]:wi+β​pi≥0​ for all ​i}\alpha\leftarrow\max\{\beta\in(0,1]:w\_{i}+\beta p\_{i}\geq 0\text{ for all }i\}

16:   w←w+α​pw\leftarrow w+\alpha p

17:   Update AA and FF

18:  end if

19:until converged

Under nondegeneracy, the routine performs at most NN releases from the
active set and terminates in finitely many iterations at a KKT point
which, by Proposition[A.1](https://arxiv.org/html/2601.06271v1#ThmAppProposition1 "Proposition A.​ A.1 (Long‑only optimization). ‣ A.1 Existence and (Possible) Non‑Uniqueness ‣ Appendix A Long‑Only Hybrid‑Risk Optimization ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization"), is globally optimal.

### A.3   Numerical Illustration

Consider N=3N=3 assets with

|  |  |  |
| --- | --- | --- |
|  | Σ=0.05​[4.8435−1.9906−0.9228−1.99062.57432.7723−0.92282.77236.9938],C=Σ,λ=1.\Sigma=0.05\begin{bmatrix}4.8435&-1.9906&-0.9228\\ -1.9906&2.5743&2.7723\\ -0.9228&2.7723&6.9938\end{bmatrix},\qquad C=\Sigma,\quad\lambda=1. |  |

#### Closed‑form (unrestricted) solution.

Using ([5](https://arxiv.org/html/2601.06271v1#S3.E5 "In Proposition 2 (Closed‑Form Optimal Weights (short‑selling allowed; see Appendix A for the long‑only case)). ‣ 3.3 Main Propositions ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization")) one obtains

|  |  |  |
| --- | --- | --- |
|  | w∗=(0.4110, 0.7271,−0.1381)𝖳,σ2​(w∗)=0.03354.w^{\ast}=(0.4110,\;0.7271,\;-0.1381)^{\mathsf{T}},\qquad\sigma^{2}(w^{\ast})=0.03354. |  |

#### Long‑only solution.

The Algorithm[1](https://arxiv.org/html/2601.06271v1#alg1 "Algorithm 1 ‣ A.2 Active‑Set Solver (Pseudo‑code) ‣ Appendix A Long‑Only Hybrid‑Risk Optimization ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization") sets the third weight to zero and returns

|  |  |  |
| --- | --- | --- |
|  | w^=(0.4005, 0.5995, 0)𝖳,σ2​(w^)=0.03731.\widehat{w}=(0.4005,\;0.5995,\;0)^{\mathsf{T}},\qquad\sigma^{2}(\widehat{w})=0.03731. |  |

| Portfolio | Asset 1 | Asset 2 | Asset 3 |
| --- | --- | --- | --- |
| Closed‑form w∗w^{\ast} | 0.4110 | 0.7271 | −0.1381-0.1381 |
| Long‑only w^\widehat{w} | 0.4005 | 0.5995 | −-0.0000 |

Table 1: Unrestricted vs. long‑only weights (λ=1\lambda=1).
The long‑only constraint removes the short position in Asset 3, raising
portfolio variance by
Δ​σ2=0.0038(≈ 11.3%)\Delta\sigma^{2}=0.0038\ (\approx\ 11.3\ \%).

This toy example shows:

\* The analytic formula can produce negative positions even when Mλ≻0M\_{\lambda}\succ 0;
\* The long-only optimum differs, but an active set method converges rapidly and preserves the hybrid risk objective structure.

## Appendix B Analytic Derivatives under Simultaneous Diagonalization

This appendix provides an explicit coordinate-wise proof of
*strict variance–connectedness trade‑off*. Recovers the result
of Proposition[3](https://arxiv.org/html/2601.06271v1#Thmproposition3 "Proposition 3 (Strict Trade–off: Negative Slope). ‣ Remark (long‑only portfolios). ‣ 3.3 Main Propositions ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization") under the stronger assumption that
Σ\Sigma and CC share an eigenbasis.

###### Theorem ​ B.1 (Trade‑off under joint diagonalization).

Assume Σ=U​ΛΣ​U𝖳\Sigma=U\Lambda\_{\Sigma}U^{\mathsf{T}} and
C=U​ΛC​U𝖳C=U\Lambda\_{C}U^{\mathsf{T}} with
ΛΣ=diag⁡(σ12,…,σN2)\Lambda\_{\Sigma}=\operatorname{diag}(\sigma\_{1}^{2},\dots,\sigma\_{N}^{2}),
ΛC=diag⁡(c1,…,cN)\Lambda\_{C}=\operatorname{diag}(c\_{1},\dots,c\_{N}) and σi2,ci>0\sigma\_{i}^{2},c\_{i}>0.
For λ∈(0,1)\lambda\in(0,1), let

|  |  |  |
| --- | --- | --- |
|  | Mλ=λ​Σ+(1−λ)​C,wλ=arg⁡min𝟏𝖳​w=1⁡w𝖳​Mλ​wM\_{\lambda}=\lambda\Sigma+(1-\lambda)C,\quad w\_{\lambda}=\arg\min\_{\mathbf{1}^{\mathsf{T}}w=1}w^{\mathsf{T}}M\_{\lambda}w |  |

and set
σ2​(λ)=wλ𝖳​Σ​wλ\sigma^{2}(\lambda)=w\_{\lambda}^{\mathsf{T}}\Sigma w\_{\lambda},
κ​(λ)=wλ𝖳​C​wλ\kappa(\lambda)=w\_{\lambda}^{\mathsf{T}}Cw\_{\lambda}.
If the eigenratio vector (σi2/ci)(\sigma\_{i}^{2}/c\_{i}) is non‑constant, then

|  |  |  |
| --- | --- | --- |
|  | σ2⁣′​(λ)<0,κ′​(λ)>0,d​σ2d​κ=−1−λλ<0.\sigma^{2\,\prime}(\lambda)<0,\qquad\kappa^{\prime}(\lambda)>0,\qquad\frac{d\sigma^{2}}{d\kappa}=-\frac{1-\lambda}{\lambda}<0. |  |

###### Proof.

Step 1 (weights in the eigenbasis).
Write x=U𝖳​wx=U^{\mathsf{T}}w and
ηi=(U𝖳​𝟏)i>0\eta\_{i}=(U^{\mathsf{T}}\mathbf{1})\_{i}>0.
Minimizing x𝖳​Λλ​xx^{\mathsf{T}}\Lambda\_{\lambda}x s.t. ∑iηi​xi=1\sum\_{i}\eta\_{i}x\_{i}=1 gives

|  |  |  |
| --- | --- | --- |
|  | xi,λ=ηiZ​(λ)​Di​(λ),Di​(λ)=λ​σi2+(1−λ)​ci,Z​(λ)=∑kηk2Dk​(λ).x\_{i,\lambda}=\frac{\eta\_{i}}{Z(\lambda)D\_{i}(\lambda)},\quad D\_{i}(\lambda)=\lambda\sigma\_{i}^{2}+(1-\lambda)c\_{i},\quad Z(\lambda)=\sum\_{k}\frac{\eta\_{k}^{2}}{D\_{k}(\lambda)}. |  |

Step 2 (risk expressions).
Hence

|  |  |  |
| --- | --- | --- |
|  | σ2​(λ)=1Z​(λ)2​∑iηi2​σi2Di​(λ)2,κ​(λ)=1Z​(λ)2​∑iηi2​ciDi​(λ)2.\sigma^{2}(\lambda)=\frac{1}{Z(\lambda)^{2}}\sum\_{i}\frac{\eta\_{i}^{2}\sigma\_{i}^{2}}{D\_{i}(\lambda)^{2}},\quad\kappa(\lambda)=\frac{1}{Z(\lambda)^{2}}\sum\_{i}\frac{\eta\_{i}^{2}c\_{i}}{D\_{i}(\lambda)^{2}}. |  |

Step 3 (linear identity of derivatives).
Define
F​(λ)=min𝟏𝖳​w=1⁡w𝖳​Mλ​w=λ​σ2+(1−λ)​κ.F(\lambda)=\min\_{\mathbf{1}^{\mathsf{T}}w=1}w^{\mathsf{T}}M\_{\lambda}w=\lambda\sigma^{2}+(1-\lambda)\kappa.
Envelope theorem ⇒\Rightarrow
F′​(λ)=σ2−κF^{\prime}(\lambda)=\sigma^{2}-\kappa.
Direct differentiation yields

|  |  |  |
| --- | --- | --- |
|  | F′​(λ)=σ2−κ+λ​σ2⁣′−(1−λ)​κ′,F^{\prime}(\lambda)=\sigma^{2}-\kappa+\lambda\sigma^{2\,\prime}-(1-\lambda)\kappa^{\prime}, |  |

so that

|  |  |  |
| --- | --- | --- |
|  | λ​σ2⁣′+(1−λ)​κ′=0.\lambda\sigma^{2\,\prime}+(1-\lambda)\kappa^{\prime}=0. |  |

Step 4 (signs).
FF is concave ⇒\Rightarrow F′′​(λ)=σ2⁣′−κ′≤0F^{\prime\prime}(\lambda)=\sigma^{2\,\prime}-\kappa^{\prime}\leq 0.
If all eigenratios were equal, F′′≡0F^{\prime\prime}\equiv 0, contradicting the
non‑proportionality assumption; hence F′′<0F^{\prime\prime}<0 and
σ2⁣′<κ′\sigma^{2\,\prime}<\kappa^{\prime}.
Together with (⋆)(\star), this implies
σ2⁣′<0\sigma^{2\,\prime}<0 and κ′>0\kappa^{\prime}>0.

Step 5 (frontier slope).
Dividing (⋆)(\star) by κ′\kappa^{\prime} gives
d​σ2/d​κ=−(1−λ)/λ<0d\sigma^{2}/d\kappa=-(1-\lambda)/\lambda<0.
∎

## Appendix C When Three–Fund Coefficients Turn Negative

###### Example C.​ C.1 (Negative barycentric coefficients).

Consider N=3N=3 assets with

|  |  |  |
| --- | --- | --- |
|  | Σ=[0.0400.0300.0200.0300.0900.0100.0200.0100.160],C=[0.100−0.0200−0.0200.0500.01000.0100.020],𝝁=(0.08,0.06,0.10)𝖳.\Sigma=\begin{bmatrix}0.040&0.030&0.020\\ 0.030&0.090&0.010\\ 0.020&0.010&0.160\end{bmatrix},\quad C=\begin{bmatrix}0.100&-0.020&0\\ -0.020&0.050&0.010\\ 0&0.010&0.020\end{bmatrix},\quad\boldsymbol{\mu}=(0.08,0.06,0.10)^{\mathsf{T}}. |  |

Corner portfolios. 
With only the budget constraint (short selling allowed)

|  |  |  |
| --- | --- | --- |
|  | wMV=(0.7321,0.1429,0.1250),wMC=(0.1864,0.2373,0.5763),wmax⁡μ=(0,0,1).w^{\mathrm{MV}}=(0.7321,0.1429,0.1250),\;w^{\mathrm{MC}}=(0.1864,0.2373,0.5763),\;w^{\max\mu}=(0,0,1). |  |

Hybrid‑risk optimum. 
For λ=0.4\lambda=0.4 one obtains
w∗​(0.4)=(0.3378,0.3804,0.2818)w^{\ast}(0.4)=(0.3378,0.3804,0.2818).

Barycentric weights. 
Solving w∗=∑k=13αk​w(k)w^{\ast}=\sum\_{k=1}^{3}\alpha\_{k}w^{(k)} with
∑αk=1\sum\alpha\_{k}=1 yields
(α1,α2,α3)=(0.063,1.565,−0.628)(\alpha\_{1},\alpha\_{2},\alpha\_{3})=(0.063,1.565,-0.628).

Because α3<0\alpha\_{3}<0 and α2>1\alpha\_{2}>1, the representation is affine but
not convex: w∗w^{\ast} lies outside
𝒮=conv⁡{wMV,wMC,wmax⁡μ}\mathcal{S}=\operatorname{conv}\!\{w^{\mathrm{MV}},w^{\mathrm{MC}},w^{\max\mu}\}.
Figure [3](https://arxiv.org/html/2601.06271v1#Ax3.F3 "Figure 3 ‣ Appendix C When Three–Fund Coefficients Turn Negative ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization") illustrates the geometry.

![Refer to caption](x3.png)


Figure 3: Position of w∗​(0.4)w^{\ast}(0.4) relative to the simplex defined by
the three corner funds. The point lies outside the shaded
triangle, forcing at least one barycentric weight to be negative.

#### Take‑aways.

1. (1)

   Misalignment between Σ\Sigma and CC can bend the
   λ\lambda‑efficient curve outside the set

   |  |  |  |
   | --- | --- | --- |
   |  | conv⁡{wMV,wMC,wmax⁡μ},\operatorname{conv}\!\{w^{\mathrm{MV}},\;w^{\mathrm{MC}},\;w^{\max\mu}\}, |  |

   thereby invalidating a *convex* three‑fund representation.
2. (2)

   Theorem [1](https://arxiv.org/html/2601.06271v1#Thmtheorem1 "Theorem 1 (Conditional Three–Fund Separation). ‣ Definition. ‣ 3.4 Connectedness 𝛽 and Three–Fund Separation ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization") therefore *requires*
   Assumption (b): the efficient set must lie inside that convex hull.
3. (3)

   Even when convexity fails, an *affine* three‑fund expansion
   still exists; negative αk\alpha\_{k} may be interpreted as borrowing / lending at the *fund* level rather than as a
   breach of the limits of the position at the asset level.

## References

* J. Baruník and T. Křehlík (2018)
  Measuring the frequency dynamics of financial connectedness and systemic risk.
  Journal of Financial Econometrics 16 (2),  pp. 271–296.
  External Links: [Document](https://dx.doi.org/10.1093/jjfinec/nby001)
  Cited by: [§2.2](https://arxiv.org/html/2601.06271v1#S2.SS2.p1.2 "2.2 Econometric Measures of Connectedness ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* M. Billio, M. Getmansky, A. W. Lo, and L. Pelizzon (2012)
  Econometric measures of connectedness and systemic risk in the finance and insurance sectors.
  Journal of Financial Economics 104 (3),  pp. 535–559.
  External Links: [Document](https://dx.doi.org/10.1016/j.jfineco.2011.12.010)
  Cited by: [§1](https://arxiv.org/html/2601.06271v1#S1.p2.1 "1 Introduction ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization"),
  [§2.2](https://arxiv.org/html/2601.06271v1#S2.SS2.p1.2 "2.2 Econometric Measures of Connectedness ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization"),
  [§3.1](https://arxiv.org/html/2601.06271v1#S3.SS1.p2.1 "3.1 Setting and Notation ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* F. Black and R. Litterman (1992)
  Global portfolio optimization.
  Financial Analysts Journal 48 (5),  pp. 28–43.
  External Links: [Document](https://dx.doi.org/10.2469/faj.v48.n5.28)
  Cited by: [§2.1](https://arxiv.org/html/2601.06271v1#S2.SS1.p1.1 "2.1 Mean–Variance Theory and Its Extensions ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* D. C. Broadstock, I. Chatziantoniou, and D. Gabauer (2022a)
  Minimum connectedness portfolios and the market for green bonds.
  In Applications in Energy Finance,
   pp. 217–253.
  Cited by: [§3.2](https://arxiv.org/html/2601.06271v1#S3.SS2.p1.6 "3.2 Joint Risk Objective ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* D. C. Broadstock, I. Chatziantoniou, and D. Gabauer (2022b)
  Minimum connectedness portfolios: diversifying through network risk.
  Energy Economics 109,  pp. 105908.
  External Links: [Document](https://dx.doi.org/10.1016/j.eneco.2022.105908)
  Cited by: [§1](https://arxiv.org/html/2601.06271v1#S1.p3.1 "1 Introduction ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization"),
  [§2.3](https://arxiv.org/html/2601.06271v1#S2.SS3.p1.1 "2.3 Network–Based Portfolio Selection ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* R. Deguest and L. Martellini (2015)
  Improving mean–variance optimization when drawdown matters.
  Financial Analysts Journal 71 (4),  pp. 13–29.
  External Links: [Document](https://dx.doi.org/10.2469/faj.v71.n4.1)
  Cited by: [§2.1](https://arxiv.org/html/2601.06271v1#S2.SS1.p1.1 "2.1 Mean–Variance Theory and Its Extensions ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization"),
  [§2.4](https://arxiv.org/html/2601.06271v1#S2.SS4.p1.2 "2.4 Multi–Objective Risk Optimization ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* F. X. Diebold and K. Yilmaz (2009)
  Measuring financial asset return and volatility spillovers, with application to global equity markets.
  Economic Journal 119 (534),  pp. 158–171.
  External Links: [Document](https://dx.doi.org/10.1111/j.1468-0297.2008.02208.x)
  Cited by: [§2.2](https://arxiv.org/html/2601.06271v1#S2.SS2.p1.2 "2.2 Econometric Measures of Connectedness ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization"),
  [§3.6](https://arxiv.org/html/2601.06271v1#S3.SS6.p1.2 "3.6 Connectedness vs. Conventional Volatility ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* F. X. Diebold and K. Yilmaz (2012)
  Better to give than to receive: predictive directional measurement of volatility spillovers.
  International Journal of Forecasting 28 (1),  pp. 57–66.
  External Links: [Document](https://dx.doi.org/10.1016/j.ijforecast.2011.02.006)
  Cited by: [§2.2](https://arxiv.org/html/2601.06271v1#S2.SS2.p1.2 "2.2 Econometric Measures of Connectedness ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization"),
  [§3.6](https://arxiv.org/html/2601.06271v1#S3.SS6.p1.2 "3.6 Connectedness vs. Conventional Volatility ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* F. X. Diebold and K. Yilmaz (2014)
  On the network topology of variance decompositions: measuring the connectedness of financial firms.
  Journal of Econometrics 182 (1),  pp. 119–134.
  External Links: [Document](https://dx.doi.org/10.1016/j.jeconom.2014.05.012)
  Cited by: [§1](https://arxiv.org/html/2601.06271v1#S1.p2.1 "1 Introduction ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization"),
  [§2.2](https://arxiv.org/html/2601.06271v1#S2.SS2.p1.2 "2.2 Econometric Measures of Connectedness ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization"),
  [§3.1](https://arxiv.org/html/2601.06271v1#S3.SS1.p2.1 "3.1 Setting and Notation ‣ 3 Model and Optimization Framework ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* O. Ledoit and M. Wolf (2004)
  A well–conditioned estimator for large–dimensional covariance matrices.
  Journal of Multivariate Analysis 88 (2),  pp. 365–411.
  External Links: [Document](https://dx.doi.org/10.1016/S0047-259X%2803%2900096-4)
  Cited by: [§2.1](https://arxiv.org/html/2601.06271v1#S2.SS1.p1.1 "2.1 Mean–Variance Theory and Its Extensions ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* R. N. Mantegna (1999)
  Hierarchical structure in financial markets.
  European Physical Journal B 11 (1),  pp. 193–197.
  External Links: [Document](https://dx.doi.org/10.1007/s100510050929)
  Cited by: [§2.2](https://arxiv.org/html/2601.06271v1#S2.SS2.p1.2 "2.2 Econometric Measures of Connectedness ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* H. Markowitz (1952)
  Portfolio selection.
  The Journal of Finance 7 (1),  pp. 77–91.
  External Links: [Document](https://dx.doi.org/10.2307/2975974)
  Cited by: [§1](https://arxiv.org/html/2601.06271v1#S1.p1.1 "1 Introduction ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization"),
  [§2.1](https://arxiv.org/html/2601.06271v1#S2.SS1.p1.1 "2.1 Mean–Variance Theory and Its Extensions ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* R. C. Merton (1972)
  An analytic derivation of the efficient portfolio frontier.
  Journal of Financial and Quantitative Analysis 7 (4),  pp. 1851–1872.
  External Links: [Document](https://dx.doi.org/10.2307/2329621)
  Cited by: [§2.1](https://arxiv.org/html/2601.06271v1#S2.SS1.p1.1 "2.1 Mean–Variance Theory and Its Extensions ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* G. Peralta and A. Zareei (2016)
  A network approach to portfolio selection.
  Journal of Empirical Finance 38,  pp. 157–180.
  External Links: [Document](https://dx.doi.org/10.1016/j.jempfin.2016.01.004)
  Cited by: [§1](https://arxiv.org/html/2601.06271v1#S1.p3.1 "1 Introduction ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization"),
  [§2.3](https://arxiv.org/html/2601.06271v1#S2.SS3.p1.1 "2.3 Network–Based Portfolio Selection ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* F. Pozzi, T. Di Matteo, and T. Aste (2013)
  Spread of risk across financial markets: better to invest in the peripheries.
  Scientific Reports 3,  pp. 1665.
  External Links: [Document](https://dx.doi.org/10.1038/srep01665)
  Cited by: [§1](https://arxiv.org/html/2601.06271v1#S1.p3.1 "1 Introduction ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization"),
  [§2.3](https://arxiv.org/html/2601.06271v1#S2.SS3.p1.1 "2.3 Network–Based Portfolio Selection ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* R. T. Rockafellar and S. Uryasev (2000)
  Optimization of conditional value–at–risk.
  Journal of Risk 2 (3),  pp. 21–42.
  Cited by: [§2.1](https://arxiv.org/html/2601.06271v1#S2.SS1.p1.1 "2.1 Mean–Variance Theory and Its Extensions ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization"),
  [§2.4](https://arxiv.org/html/2601.06271v1#S2.SS4.p1.2 "2.4 Multi–Objective Risk Optimization ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").
* M. Tumminello, F. Lillo, and R. N. Mantegna (2010)
  Correlation, hierarchies, and networks in financial markets.
  Journal of Economic Behavior & Organization 75 (1),  pp. 40–58.
  External Links: [Document](https://dx.doi.org/10.1016/j.jebo.2010.04.008)
  Cited by: [§2.3](https://arxiv.org/html/2601.06271v1#S2.SS3.p1.1 "2.3 Network–Based Portfolio Selection ‣ 2 Literature Review ‣ A Three–Dimensional Efficient Surface for Portfolio Optimization").