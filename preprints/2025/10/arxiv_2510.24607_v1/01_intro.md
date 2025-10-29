---
authors:
- Yimeng Qiu
doc_id: arxiv:2510.24607v1
family_id: arxiv:2510.24607
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target
  Exposures'
url_abs: http://arxiv.org/abs/2510.24607v1
url_html: https://arxiv.org/html/2510.24607v1
venue: arXiv q-fin
version: 1
year: 2025
---


Yimeng Qiu

(2025/06/18)

###### Abstract

We develop *Entropy-Guided Multiplicative Updates* (EGMU), a convex optimization framework for constructing multi-factor target-exposure portfolios by minimizing Kullback–Leibler (KL) divergence from a benchmark subject to linear factor constraints.
Our contributions are theoretical and algorithmic.
(*i*) We formalize feasibility and uniqueness: with strictly positive benchmark and feasible targets in the convex hull of exposures, the solution is unique and strictly positive.
(*ii*) We derive the dual concave program with gradient t−𝔼w​(θ)​[x]t-\mathbb{E}\_{w(\theta)}[x] and Hessian −Covw​(θ)​(x)-\mathrm{Cov}\_{w(\theta)}(x), and give a precise sensitivity formula ∂θ∗/∂t=Covw∗​(x)−1\partial\theta^{\*}/\partial t=\mathrm{Cov}\_{w^{\*}}(x)^{-1} and ∂w∗/∂t=diag​(w∗)​(X−𝟏​μ⊤)​Covw∗​(x)−1\partial w^{\*}/\partial t=\mathrm{diag}(w^{\*})(X-\mathbf{1}\mu^{\top})\mathrm{Cov}\_{w^{\*}}(x)^{-1}.
(*iii*) We present two provably convergent solvers: a damped *dual Newton* method with global convergence and local quadratic rate, and a *KL-projection* scheme based on IPF/Bregman–Dykstra for equalities and inequalities.
(*iv*) We further generalize EGMU with *elastic targets* (strongly concave dual) and *robust target sets* (support-function dual), and introduce a *path-following ODE* for solution trajectories, all reusing the same dual-moment structure and solved via Newton or proximal-gradient schemes.
(*v*) We detail numerically stable and scalable implementations (LogSumExp, covariance regularization, half-space KL-projections).
We emphasize theory and reproducible algorithms; empirical benchmarking is optional.

Keywords: KL divergence, information projection, entropy pooling, factor exposures, Bregman projections, convex optimization.

## 1 Introduction

Rules-based multi-factor portfolios seek specified exposures (Value, Momentum, Quality, Low Volatility, etc.).
Heuristic sequential “tilts” lack a single global objective and are order-dependent.
Quadratic exposure-matching solves a different closeness metric and often needs explicit regularization and a risk model.

We pose *Entropy-Guided Multiplicative Updates* (EGMU): minimize DKL(𝐰∥𝐛)D\_{\mathrm{KL}}\!\left(\mathbf{w}\middle\|\mathbf{b}\right) over the simplex under linear exposure constraints. This information projection is classical and yields exponential-family solutions and convex duality structure [[6](https://arxiv.org/html/2510.24607v1#bib.bib6), [5](https://arxiv.org/html/2510.24607v1#bib.bib5)]. In portfolio engineering it parallels Entropy Pooling [[8](https://arxiv.org/html/2510.24607v1#bib.bib8)]. Our focus is to provide a rigorous, self-contained treatment tailored to target-exposure construction: feasibility/uniqueness, sensitivity, and provably convergent algorithms for equality and inequality constraints. We also give implementable pseudo-code with stability safeguards. Our generalized variants—elastic/robust targets and solution paths—remain within the same dual-moment framework.

#### Notation.

Let NN be the number of assets, KK factors. Benchmark 𝐛∈ΔN:={𝐰∈ℝ≥0N:𝟏⊤​𝐰=1}\mathbf{b}\in\Delta^{N}:=\{\mathbf{w}\!\in\!\mathbb{R}\_{\geq 0}^{N}:\mathbf{1}^{\top}\mathbf{w}=1\} has strictly positive entries (bi>0b\_{i}>0). Exposure matrix 𝐗∈ℝN×K\mathbf{X}\in\mathbb{R}^{N\times K} has rows 𝐱i⊤\mathbf{x}\_{i}^{\top}. Targets t∈ℝKt\in\mathbb{R}^{K}. Expectations 𝔼w​[⋅]\mathbb{E}\_{w}[\cdot] are under the discrete distribution ww on {1,…,N}\{1,\dots,N\}.

#### Operators and shorthand.

For a vector vv, normalize​(v):=v/(𝟏⊤​v)\mathrm{normalize}(v):=v/(\mathbf{1}^{\top}v) projects vv onto the simplex ray.
Elementwise product/division are denoted by ⊙\odot and ⊘\oslash.
We write Π𝒞KL​(u)\Pi^{\mathrm{KL}}\_{\mathcal{C}}(u) for the (unique) KL projection of uu onto a closed convex set 𝒞⊆ΔN\mathcal{C}\subseteq\Delta^{N}.
We use the LogSumExp trick log​∑ibi​esi=log​∑ibi​esi−m+m\log\!\sum\_{i}b\_{i}e^{s\_{i}}=\log\!\sum\_{i}b\_{i}e^{s\_{i}-m}+m with m=maxi⁡sim=\max\_{i}s\_{i}.
We adopt 𝔼w​[x]=∑iwi​xi\mathbb{E}\_{w}[x]=\sum\_{i}w\_{i}x\_{i} and Covw​(x)=∑iwi​(xi−μ)​(xi−μ)⊤\mathrm{Cov}\_{w}(x)=\sum\_{i}w\_{i}(x\_{i}-\mu)(x\_{i}-\mu)^{\top} with μ=𝔼w​[x]\mu=\mathbb{E}\_{w}[x].

#### Contributions at a glance.

* •

  KL-based target-exposure construction: existence/uniqueness and the exponential-family solution with covariance Hessian.
* •

  Algorithms with guarantees: a damped dual Newton method and Bregman projection schemes (IPF/Dykstra) for equalities and inequalities.
* •

  Generalizations with shared dual moments: elastic targets (strongly concave dual) and robust target sets (support-function dual) with a proximal-gradient solver.
* •

  Sensitivity and paths: closed-form sensitivities and a homotopy ODE to trace optimal solutions along target directions.

## 2 Problem, Feasibility, and Geometry

### 2.1 KL-Minimization with Linear Constraints

We study

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝐰∈ΔNDKL(𝐰∥𝐛)s.t.𝐗⊤𝐰=t,A𝐰≤c.\min\_{\mathbf{w}\in\Delta^{N}}\ D\_{\mathrm{KL}}\!\left(\mathbf{w}\middle\|\mathbf{b}\right)\quad\text{s.t.}\quad\mathbf{X}^{\top}\mathbf{w}=t,\qquad A\mathbf{w}\leq c. |  | (1) |

The objective is strictly convex on the relative interior of ΔN\Delta^{N}; the feasible set is convex.

### 2.2 Feasibility and Strict Positivity

###### Proposition 1 (Feasibility and strict positivity).

If only equality constraints 𝐗⊤​𝐰=t\mathbf{X}^{\top}\mathbf{w}=t are present, feasibility holds iff t∈conv​{𝐱i}i=1Nt\in\mathrm{conv}\{\mathbf{x}\_{i}\}\_{i=1}^{N}. If tt lies in the relative interior of conv​{𝐱i}\mathrm{conv}\{\mathbf{x}\_{i}\}, the unique optimizer satisfies wi⋆>0w\_{i}^{\star}>0 for all ii. With additional linear inequalities A​𝐰≤cA\mathbf{w}\leq c, feasibility remains a convex polytope; infeasibility admits a Farkas-type certificate.

###### Remark 1 (Intercept factor, linear dependence, and gauge fixing).

If 𝐗\mathbf{X} contains a constant (intercept) column 𝟏\mathbf{1}, then the budget constraint 𝟏⊤​𝐰=1\mathbf{1}^{\top}\mathbf{w}=1 is linearly redundant with that column, making the dual variable non-unique and the covariance Covw​(θ)​(x)\mathrm{Cov}\_{w(\theta)}(x) singular along the intercept direction.
In practice, *remove the intercept column and keep the budget*, or equivalently keep the intercept but *fix its dual component to zero* (gauge fixing).
Numerically, this avoids singular normal equations and yields a well-posed Newton step on the K−1K{-}1 dimensional exposure subspace.

###### Lemma 1 (Column-shift (translation) invariance).

For any d∈ℝKd\in\mathbb{R}^{K}, define X′:=X−𝟏​d⊤X^{\prime}:=X-\mathbf{1}d^{\top} and t′:=t−dt^{\prime}:=t-d. Then the equality-feasible sets coincide:

|  |  |  |
| --- | --- | --- |
|  | {w∈ΔN:X⊤​w=t}={w∈ΔN:X′⁣⊤​w=t′}.\{w\in\Delta^{N}:\ X^{\top}w=t\}\;=\;\{w\in\Delta^{N}:\ X^{\prime\top}w=t^{\prime}\}. |  |

*Proof.* One line: X′⁣⊤​w=(X−𝟏​d⊤)⊤​w=X⊤​w−d​(𝟏⊤​w)=t−dX^{\prime\top}w=(X-\mathbf{1}d^{\top})^{\top}w=X^{\top}w-d(\mathbf{1}^{\top}w)=t-d since 𝟏⊤​w=1\mathbf{1}^{\top}w=1.

## 3 Duality and Exponential-Family Form

### 3.1 Exponential Tilt (Equality Case)

With only 𝐗⊤​𝐰=t\mathbf{X}^{\top}\mathbf{w}=t, the KKT conditions give the exponential-family solution

|  |  |  |  |
| --- | --- | --- | --- |
|  | wi​(θ)=bi​exp⁡(θ⊤​𝐱i)∑jbj​exp⁡(θ⊤​𝐱j).w\_{i}(\theta)=\frac{b\_{i}\exp(\theta^{\top}\mathbf{x}\_{i})}{\sum\_{j}b\_{j}\exp(\theta^{\top}\mathbf{x}\_{j})}. |  | (2) |

The dual concave objective reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(θ)=θ⊤​t−log⁡(∑ibi​eθ⊤​𝐱i),L(\theta)=\theta^{\top}t-\log\!\Big(\sum\_{i}b\_{i}e^{\theta^{\top}\mathbf{x}\_{i}}\Big), |  | (3) |

with

|  |  |  |
| --- | --- | --- |
|  | ∇L​(θ)=t−𝔼w​(θ)​[𝐱],∇2L​(θ)=−Covw​(θ)​(𝐱).\nabla L(\theta)=t-\mathbb{E}\_{w(\theta)}[\mathbf{x}],\qquad\nabla^{2}L(\theta)=-\mathrm{Cov}\_{w(\theta)}(\mathbf{x}). |  |

Strict concavity holds on the span where Covw​(θ)​(𝐱)≻0\mathrm{Cov}\_{w(\theta)}(\mathbf{x})\succ 0 [[9](https://arxiv.org/html/2510.24607v1#bib.bib9)].

### 3.2 Sensitivity to Targets

Let θ⋆\theta^{\star} maximize LL, μ=𝔼w⋆​[𝐱]\mu=\mathbb{E}\_{w^{\star}}[\mathbf{x}], and Σ=Covw⋆​(𝐱)\Sigma=\mathrm{Cov}\_{w^{\star}}(\mathbf{x}). Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂θ⋆∂t=Σ−1,∂wi⋆∂t=wi⋆​(𝐱i−μ)⊤​Σ−1.\frac{\partial\theta^{\star}}{\partial t}=\Sigma^{-1},\qquad\frac{\partial w\_{i}^{\star}}{\partial t}=w\_{i}^{\star}(\mathbf{x}\_{i}-\mu)^{\top}\Sigma^{-1}. |  | (4) |

### 3.3 Elastic Targets (Soft Penalty): Dual, Uniqueness, and Sensitivity

Consider the elastic objective

|  |  |  |
| --- | --- | --- |
|  | minw∈ΔNDKL(w∥b)+λsoft2∥X⊤w−t∥22.\min\_{w\in\Delta^{N}}\ D\_{\mathrm{KL}}\!\left(w\middle\|b\right)+\frac{\lambda\_{\mathrm{soft}}}{2}\,\|X^{\top}w-t\|\_{2}^{2}. |  |

Its Fenchel dual is

|  |  |  |
| --- | --- | --- |
|  | maxθ∈ℝKLel​(θ):=θ⊤​t−log​∑ibi​eθ⊤​xi−12​λsoft​‖θ‖22,\max\_{\theta\in\mathbb{R}^{K}}\quad L\_{\mathrm{el}}(\theta):=\theta^{\top}t-\log\!\sum\_{i}b\_{i}e^{\theta^{\top}x\_{i}}-\frac{1}{2\lambda\_{\mathrm{soft}}}\|\theta\|\_{2}^{2}, |  |

so the optimizer is unique and the primal solution remains the exponential tilt wi∝bi​eθ⋆⊤​xiw\_{i}\propto b\_{i}e^{\theta^{\star\top}x\_{i}}. The gradient/Hessian of LelL\_{\mathrm{el}} are

|  |  |  |
| --- | --- | --- |
|  | ∇Lel​(θ)=t−𝔼w​(θ)​[x]−1λsoft​θ,∇2Lel​(θ)=−Covw​(θ)​(x)−1λsoft​I.\nabla L\_{\mathrm{el}}(\theta)=t-\mathbb{E}\_{w(\theta)}[x]-\tfrac{1}{\lambda\_{\mathrm{soft}}}\theta,\qquad\nabla^{2}L\_{\mathrm{el}}(\theta)=-\mathrm{Cov}\_{w(\theta)}(x)-\tfrac{1}{\lambda\_{\mathrm{soft}}}I. |  |

###### Theorem 1 (Elastic sensitivity).

At θel⋆\theta^{\star}\_{\mathrm{el}}, we have

|  |  |  |
| --- | --- | --- |
|  | ∂θel⋆∂t=(Σ+1λsoft​I)−1,∂w⋆∂t=diag​(w⋆)​(X−𝟏​μ⊤)​(Σ+1λsoft​I)−1.\frac{\partial\theta^{\star}\_{\mathrm{el}}}{\partial t}=\big(\Sigma+\tfrac{1}{\lambda\_{\mathrm{soft}}}I\big)^{-1},\qquad\frac{\partial w^{\star}}{\partial t}=\mathrm{diag}(w^{\star})\,(X-\mathbf{1}\mu^{\top})\,\big(\Sigma+\tfrac{1}{\lambda\_{\mathrm{soft}}}I\big)^{-1}. |  |

### 3.4 Robust Target Sets via Support Functions

Relax the equality to a convex set: X⊤​w∈t0+𝒰X^{\top}w\in t\_{0}+\mathcal{U} for a closed, convex, centrally-symmetric set 𝒰⊂ℝK\mathcal{U}\subset\mathbb{R}^{K}. Then

|  |  |  |
| --- | --- | --- |
|  | minw∈ΔNDKL(w∥b)+ιt0+𝒰(X⊤w)⟺maxθ∈ℝKLrob(θ):=σt0+𝒰(θ)−log∑ibieθ⊤​xi,\min\_{w\in\Delta^{N}}\ D\_{\mathrm{KL}}\!\left(w\middle\|b\right)+\iota\_{\,t\_{0}+\mathcal{U}}(X^{\top}w)\quad\Longleftrightarrow\quad\max\_{\theta\in\mathbb{R}^{K}}\ L\_{\mathrm{rob}}(\theta):=\sigma\_{t\_{0}+\mathcal{U}}(\theta)-\log\!\sum\_{i}b\_{i}e^{\theta^{\top}x\_{i}}, |  |

where σS​(θ)\sigma\_{S}(\theta) is the support function. In particular,

|  |  |  |
| --- | --- | --- |
|  | 𝒰={u:‖u‖2≤ρ}⇒σt0+𝒰​(θ)=θ⊤​t0+ρ​‖θ‖2;𝒰={u:‖u‖∞≤ρ}⇒σt0+𝒰​(θ)=θ⊤​t0+ρ​‖θ‖1.\mathcal{U}=\{u:\|u\|\_{2}\leq\rho\}\Rightarrow\sigma\_{t\_{0}+\mathcal{U}}(\theta)=\theta^{\top}t\_{0}+\rho\|\theta\|\_{2};\quad\mathcal{U}=\{u:\|u\|\_{\infty}\leq\rho\}\Rightarrow\sigma\_{t\_{0}+\mathcal{U}}(\theta)=\theta^{\top}t\_{0}+\rho\|\theta\|\_{1}. |  |

The primal optimizer keeps the exponential tilt wi∝bi​eθ⋆⊤​xiw\_{i}\propto b\_{i}e^{\theta^{\star\top}x\_{i}}.

## 4 Algorithms

### 4.1 EGMU-Newton: Damped Dual Newton Ascent (Equality Core)

We solve ([3](https://arxiv.org/html/2510.24607v1#S3.E3 "In 3.1 Exponential Tilt (Equality Case) ‣ 3 Duality and Exponential-Family Form ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures")) via Newton steps with backtracking. Each iteration forms μ=𝔼w​(θ)​[𝐱]\mu=\mathbb{E}\_{w(\theta)}[\mathbf{x}] and Σ=Covw​(θ)​(𝐱)\Sigma=\mathrm{Cov}\_{w(\theta)}(\mathbf{x}) in O​(N​K)O(NK) and O​(N​K2)O(NK^{2}), and solves Σ​Δ=g\Sigma\,\Delta=g with g=t−μg=t-\mu.

Algorithm 1  EGMU-Newton (Equality Case, LogSumExp-stable)

1:Input: b∈ΔNb\in\Delta^{N}, X∈ℝN×KX\in\mathbb{R}^{N\times K}, target tt, tol ε\varepsilon, ridge δ≥0\delta\geq 0

2:Initialize θ←0\theta\leftarrow 0

3:while ‖∇L​(θ)‖2>ε\|\nabla L(\theta)\|\_{2}>\varepsilon do

4:  Scores: si←θ⊤​xis\_{i}\leftarrow\theta^{\top}x\_{i}; m←maxi⁡sim\leftarrow\max\_{i}s\_{i}

5:  Log-sum-exp: log⁡Z←log​∑ibi​exp⁡(si−m)+m\log Z\leftarrow\log\!\sum\_{i}b\_{i}\exp(s\_{i}-m)+m

6:  Weights: wi←bi​exp⁡(si−log⁡Z)w\_{i}\leftarrow b\_{i}\exp(s\_{i}-\log Z)

7:  Moments: μ←X⊤​w\mu\leftarrow X^{\top}w; g←t−μg\leftarrow t-\mu

8:  Covariance: Σ←∑iwi​(xi−μ)​(xi−μ)⊤\Sigma\leftarrow\sum\_{i}w\_{i}(x\_{i}-\mu)(x\_{i}-\mu)^{\top}

9:  Solve: (Σ+δ​I)​Δ=g(\Sigma+\delta I)\Delta=g ⊳\triangleright Cholesky; δ\delta only if needed

10:  Line search: Armijo backtracking with parameters (c,β)(c,\beta)

11:  θ←θ+α​Δ\theta\leftarrow\theta+\alpha\Delta

12:end while

13:Return w​(θ)w(\theta) via ([2](https://arxiv.org/html/2510.24607v1#S3.E2 "In 3.1 Exponential Tilt (Equality Case) ‣ 3 Duality and Exponential-Family Form ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures"))

#### Line-search parameters.

Choose c∈(10−6,10−1)c\in(10^{-6},10^{-1}) and β∈(0,1)\beta\in(0,1) (e.g., β=0.5\beta=0.5); pick the largest α=βm\alpha=\beta^{m} such that
L​(θ+α​Δ)≥L​(θ)+c​α​g⊤​ΔL(\theta+\alpha\Delta)\geq L(\theta)+c\,\alpha\,g^{\top}\Delta.

#### Elastic variant (R1).

For Lel​(θ)L\_{\mathrm{el}}(\theta), reuse Algorithm [1](https://arxiv.org/html/2510.24607v1#alg1 "Algorithm 1 ‣ 4.1 EGMU-Newton: Damped Dual Newton Ascent (Equality Core) ‣ 4 Algorithms ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures") with

|  |  |  |
| --- | --- | --- |
|  | g←t−μ−1λsoft​θ,Σ←Σ+1λsoft​I.g\leftarrow t-\mu-\tfrac{1}{\lambda\_{\mathrm{soft}}}\theta,\qquad\Sigma\leftarrow\Sigma+\tfrac{1}{\lambda\_{\mathrm{soft}}}I. |  |

This preserves global convergence and improves conditioning via the I/λsoftI/\lambda\_{\mathrm{soft}} term.

### 4.2 KL-Projections for Equalities: IPF / One-Dimensional Solves

For a single equality a⊤​w=τa^{\top}w=\tau, the KL projection of uu onto that hyperplane has closed form

|  |  |  |
| --- | --- | --- |
|  | w​(α)∝u⊙exp⁡(α​a),with ​ϕ​(α):=a⊤​w​(α)−τ=0,w(\alpha)\ \propto\ u\odot\exp(\alpha a),\quad\text{with }\ \phi(\alpha):=a^{\top}w(\alpha)-\tau=0, |  |

where ϕ\phi is strictly monotone since ϕ′​(α)=Varw​(α)​(a)>0\phi^{\prime}(\alpha)=\mathrm{Var}\_{w(\alpha)}(a)>0 unless aa is degenerate. Root α\alpha is found by bisection/Brent in O​(N)O(N).
Cycling over k=1,…,Kk=1,\dots,K yields IPF/GIS; it converges to the KL minimizer under feasibility [[6](https://arxiv.org/html/2510.24607v1#bib.bib6), [7](https://arxiv.org/html/2510.24607v1#bib.bib7)].

Algorithm 2  EGMU-IPF (Equalities via KL One-Dimensional Projections)

1:Input: prior u∈ΔNu\in\Delta^{N}, constraints {(ak,τk)}k=1K\{(a\_{k},\tau\_{k})\}\_{k=1}^{K}, tol ε\varepsilon

2:w←uw\leftarrow u

3:repeat

4:  for k=1k=1 to KK do

5:   Find α\alpha s.t. ak⊤​(normalize​(w⊙eα​ak))=τka\_{k}^{\top}\big(\mathrm{normalize}(w\odot e^{\alpha a\_{k}})\big)=\tau\_{k} ⊳\triangleright bisection/Brent

6:   w←normalize​(w⊙eα​ak)w\leftarrow\mathrm{normalize}(w\odot e^{\alpha a\_{k}})

7:  end for

8:until maxk⁡|ak⊤​w−τk|≤ε\max\_{k}|a\_{k}^{\top}w-\tau\_{k}|\leq\varepsilon

9:Return ww

### 4.3 KL-Projections for Inequalities: Bregman–Dykstra

For a half-space ℋ={w:a⊤​w≤τ}\mathcal{H}=\{w:a^{\top}w\leq\tau\}, the KL projection of uu onto ℋ\mathcal{H} is either uu (if feasible) or w​(λ)∝u⊙e−λ​aw(\lambda)\propto u\odot e^{-\lambda a} with λ≥0\lambda\geq 0 chosen so that a⊤​w​(λ)=τa^{\top}w(\lambda)=\tau.
Bregman–Dykstra cycles projections onto {𝒞j}\{\mathcal{C}\_{j}\} with correction terms {qj}\{q\_{j}\} and converges to the KL-projection onto ∩j𝒞j\cap\_{j}\mathcal{C}\_{j} [[3](https://arxiv.org/html/2510.24607v1#bib.bib3)].
Moreover, since dd​λ​a⊤​w​(λ)=−Varw​(λ)​(a)≤0\tfrac{d}{d\lambda}\,a^{\top}w(\lambda)=-\mathrm{Var}\_{w(\lambda)}(a)\leq 0, the residual a⊤​w​(λ)−τa^{\top}w(\lambda)-\tau is strictly decreasing in λ\lambda (unless aa is degenerate), so the one-dimensional root-finding is robust and unimodal.

Algorithm 3  EGMU-Projection (Inequalities via KL Bregman–Dykstra)

1:Input: prior u∈ΔNu\in\Delta^{N}, sets {𝒞j}j=1J\{\mathcal{C}\_{j}\}\_{j=1}^{J} (equalities/half-spaces), tol ε\varepsilon

2:w←uw\leftarrow u; qj←𝟏q\_{j}\leftarrow\mathbf{1} for all jj

3:repeat

4:  for j=1j=1 to JJ do

5:   y←normalize​(w⊙qj)y\leftarrow\mathrm{normalize}(w\odot q\_{j})

6:   z←Π𝒞jKL​(y)z\leftarrow\Pi^{\mathrm{KL}}\_{\mathcal{C}\_{j}}(y) ⊳\triangleright closed-form or 1-D solve as above

7:   qj←(w⊙qj)⊘zq\_{j}\leftarrow(w\odot q\_{j})\oslash z ⊳\triangleright elementwise

8:   w←zw\leftarrow z

9:  end for

10:until constraint violations ≤ε\leq\varepsilon

11:Return ww

### 4.4 EGMU-ProxGrad (Robust Dual, R2)

For Lrob​(θ)=θ⊤​t0−log​∑ibi​eθ⊤​xi⏟smooth concave ​f​(θ)+σ𝒰​(θ)⏟convex,L\_{\mathrm{rob}}(\theta)=\underbrace{\theta^{\top}t\_{0}-\log\!\sum\_{i}b\_{i}e^{\theta^{\top}x\_{i}}}\_{\text{smooth concave }f(\theta)}\ +\ \underbrace{\sigma\_{\mathcal{U}}(\theta)}\_{\text{convex}}, apply proximal gradient ascent

|  |  |  |
| --- | --- | --- |
|  | θ+=proxη​σ𝒰​(θ+η​∇f​(θ)),with∇f​(θ)=t0−𝔼w​(θ)​[x].\theta^{+}\;=\;\mathrm{prox}\_{\eta\,\sigma\_{\mathcal{U}}}\big(\theta+\eta\,\nabla f(\theta)\big),\quad\text{with}\quad\nabla f(\theta)=t\_{0}-\mathbb{E}\_{w(\theta)}[x]. |  |

By Moreau’s identity, proxη​σ𝒰​(z)=z−η​Π𝒰​(z/η)\mathrm{prox}\_{\eta\,\sigma\_{\mathcal{U}}}(z)=z-\eta\,\Pi\_{\mathcal{U}}(z/\eta) (see, e.g., [2](https://arxiv.org/html/2510.24607v1#bib.bib2)), where Π𝒰\Pi\_{\mathcal{U}} is the Euclidean projection onto 𝒰\mathcal{U} (closed forms: ℓ2\ell\_{2} ball ⇒\Rightarrow radial shrink; ℓ∞\ell\_{\infty} box ⇒\Rightarrow coordinatewise clip).

Algorithm 4  EGMU-ProxGrad (Robust Dual with ℓ2/ℓ∞\ell\_{2}/\ell\_{\infty} target sets)

1:Input: b,X,t0b,X,t\_{0}, convex 𝒰\mathcal{U} (e.g., ℓ2\ell\_{2} ball radius ρ\rho or ℓ∞\ell\_{\infty} box), step η>0\eta>0, tol ε\varepsilon

2:Initialize θ←0\theta\leftarrow 0

3:repeat

4:  wi∝bi​eθ⊤​xiw\_{i}\propto b\_{i}e^{\theta^{\top}x\_{i}}; normalize ww

5:  g←t0−X⊤​wg\leftarrow t\_{0}-X^{\top}w ⊳\triangleright =∇f​(θ)=\nabla f(\theta)

6:  z←θ+η​gz\leftarrow\theta+\eta g

7:  Prox: θ←z−η​Π𝒰​(z/η)\theta\leftarrow z-\eta\,\Pi\_{\mathcal{U}}(z/\eta)

8:until ‖∇f​(θ)−u‖2≤ε\|\nabla f(\theta)-u\|\_{2}\leq\varepsilon for some u∈∂σ𝒰​(θ)u\in\partial\sigma\_{\mathcal{U}}(\theta)

9:Return w​(θ)w(\theta)

#### When to use which solver.

Use Algorithm [1](https://arxiv.org/html/2510.24607v1#alg1 "Algorithm 1 ‣ 4.1 EGMU-Newton: Damped Dual Newton Ascent (Equality Core) ‣ 4 Algorithms ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures") for fast equality matching (small KK, large NN). Use the elastic variant in §[3.3](https://arxiv.org/html/2510.24607v1#S3.SS3 "3.3 Elastic Targets (Soft Penalty): Dual, Uniqueness, and Sensitivity ‣ 3 Duality and Exponential-Family Form ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures") when exact feasibility is difficult or undesirable. Use Algorithm [4](https://arxiv.org/html/2510.24607v1#alg4 "Algorithm 4 ‣ 4.4 EGMU-ProxGrad (Robust Dual, R2) ‣ 4 Algorithms ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures") for robust target sets (ℓ2/ℓ∞\ell\_{2}/\ell\_{\infty}) or when you want feasibility-by-construction via projections.

### 4.5 Path-Following via Sensitivity ODE (Module C)

For a target path t​(λ)=t0+λ​Δt(\lambda)=t\_{0}+\lambda\Delta, the optimal dual parameter satisfies the ODE

|  |  |  |
| --- | --- | --- |
|  | d​θ​(λ)d​λ=(Σ​(θ​(λ))+1λsoft​I)−1​Δ,θ​(0)=θ⋆​(t0),λ∈[0,1],\frac{d\theta(\lambda)}{d\lambda}=\Big(\Sigma(\theta(\lambda))+\tfrac{1}{\lambda\_{\mathrm{soft}}}I\Big)^{-1}\Delta,\qquad\theta(0)=\theta^{\star}(t\_{0}),\ \lambda\in[0,1], |  |

with λsoft=∞\lambda\_{\mathrm{soft}}=\infty for the equality case. The path is unique under Σ⪰m​I\Sigma\succeq mI and locally Lipschitz Hessian; for robust sets it is piecewise smooth (kinks when the active face of 𝒰\mathcal{U} changes).

Algorithm 5  EGMU-Path (Homotopy Integrator)

1:Input: b,X,t0,Δb,X,t\_{0},\Delta, (optional) λsoft\lambda\_{\mathrm{soft}}, step h>0h>0

2:Initialize θ←θ⋆​(t0)\theta\leftarrow\theta^{\star}(t\_{0}) (or 0)

3:for λ=0\lambda=0 to 11 step hh do

4:  wi∝bi​eθ⊤​xiw\_{i}\propto b\_{i}e^{\theta^{\top}x\_{i}}; normalize ww

5:  μ←X⊤​w\mu\leftarrow X^{\top}w; Σ←∑iwi​(xi−μ)​(xi−μ)⊤\Sigma\leftarrow\sum\_{i}w\_{i}(x\_{i}-\mu)(x\_{i}-\mu)^{\top}

6:  M←Σ+1λsoft​IM\leftarrow\Sigma+\tfrac{1}{\lambda\_{\mathrm{soft}}}I (take 1/λsoft=01/\lambda\_{\mathrm{soft}}=0 if equality)

7:  Euler/RK2: θ←θ+h​M−1​Δ\theta\leftarrow\theta+h\,M^{-1}\Delta (or a second-order variant)

8:end for

9:Return the path {θ​(λ),w​(λ)}\{\theta(\lambda),w(\lambda)\}

## 5 Theoretical Guarantees

###### Theorem 2 (Existence and uniqueness).

Under feasibility (Slater) and strictly positive bb, problem ([1](https://arxiv.org/html/2510.24607v1#S2.E1 "In 2.1 KL-Minimization with Linear Constraints ‣ 2 Problem, Feasibility, and Geometry ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures")) admits a unique optimizer. If t∈relint​conv​{𝐱i}t\in\mathrm{relint}\,\mathrm{conv}\{\mathbf{x}\_{i}\} and no inequality is active at the boundary, the optimizer is strictly positive.

###### Theorem 3 (Dual structure and strict concavity).

L​(θ)L(\theta) in ([3](https://arxiv.org/html/2510.24607v1#S3.E3 "In 3.1 Exponential Tilt (Equality Case) ‣ 3 Duality and Exponential-Family Form ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures")) is concave with ∇L​(θ)=t−𝔼w​(θ)​[𝐱]\nabla L(\theta)=t-\mathbb{E}\_{w(\theta)}[\mathbf{x}] and ∇2L​(θ)=−Covw​(θ)​(𝐱)\nabla^{2}L(\theta)=-\mathrm{Cov}\_{w(\theta)}(\mathbf{x}). On the subspace where Covw​(θ)​(𝐱)≻0\mathrm{Cov}\_{w(\theta)}(\mathbf{x})\succ 0, LL is strictly concave, hence θ⋆\theta^{\star} is unique and ([2](https://arxiv.org/html/2510.24607v1#S3.E2 "In 3.1 Exponential Tilt (Equality Case) ‣ 3 Duality and Exponential-Family Form ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures")) yields the unique primal optimizer.

###### Theorem 4 (Sensitivity).

At the optimum, ∂θ⋆∂t=Covw⋆​(𝐱)−1\dfrac{\partial\theta^{\star}}{\partial t}=\mathrm{Cov}\_{w^{\star}}(\mathbf{x})^{-1} and ∂w⋆∂t=diag​(w⋆)​(X−𝟏​μ⊤)​Covw⋆​(𝐱)−1\dfrac{\partial w^{\star}}{\partial t}=\mathrm{diag}(w^{\star})\,(X-\mathbf{1}\mu^{\top})\,\mathrm{Cov}\_{w^{\star}}(\mathbf{x})^{-1} with μ=𝔼w⋆​[𝐱]\mu=\mathbb{E}\_{w^{\star}}[\mathbf{x}].

###### Theorem 5 (Elastic dual: strong concavity and sensitivity).

Lel​(θ)L\_{\mathrm{el}}(\theta) is strongly concave with parameter 1/λsoft1/\lambda\_{\mathrm{soft}}; the maximizer is unique and Theorem [1](https://arxiv.org/html/2510.24607v1#Thmtheorem1 "Theorem 1 (Elastic sensitivity). ‣ 3.3 Elastic Targets (Soft Penalty): Dual, Uniqueness, and Sensitivity ‣ 3 Duality and Exponential-Family Form ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures") holds.

###### Proposition 2 (Robust dual: concavity and optimality).

Lrob​(θ)=σt0+𝒰​(θ)−log​∑ibi​eθ⊤​xiL\_{\mathrm{rob}}(\theta)=\sigma\_{t\_{0}+\mathcal{U}}(\theta)-\log\sum\_{i}b\_{i}e^{\theta^{\top}x\_{i}} is concave. Any maximizer θ⋆\theta^{\star} yields the exponential tilt wi⋆∝bi​eθ⋆⊤​xiw\_{i}^{\star}\propto b\_{i}e^{\theta^{\star\top}x\_{i}}. For 𝒰\mathcal{U} an ℓ2\ell\_{2} ball or ℓ∞\ell\_{\infty} box, Algorithm [4](https://arxiv.org/html/2510.24607v1#alg4 "Algorithm 4 ‣ 4.4 EGMU-ProxGrad (Robust Dual, R2) ‣ 4 Algorithms ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures") converges to a maximizer under standard step-size/backtracking rules (Lipschitz gradient of ff).

###### Theorem 6 (Convergence of EGMU-Newton).

With standard backtracking/damping, Newton ascent on LL is globally convergent; if Covw​(θ)​(𝐱)⪰m​I\mathrm{Cov}\_{w(\theta)}(\mathbf{x})\succeq mI and ∇2L\nabla^{2}L is Lipschitz in a neighborhood of θ⋆\theta^{\star}, the rate is locally quadratic.

###### Theorem 7 (Convergence of projection schemes).

(*i*) IPF/one-dimensional KL projections cycling over equalities converge to the unique KL minimizer when feasible.
(*ii*) Bregman–Dykstra with KL distance over finitely many closed convex sets (equalities and half-spaces) converges to the KL projection onto their intersection.

###### Remark 2 (Complexity).

Per Newton step: O​(N​K)O(NK) + O​(N​K2)O(NK^{2}) to form moments and covariance, and O​(K3)O(K^{3}) to solve the K×KK\times K system.
Each 1-D projection is O​(N)O(N) per function/derivative evaluation (bisection/Brent). Memory footprint is O​(N​K)O(NK).

## 6 Implementation Notes (Stability and Scaling)

* •

  Stability: always use LogSumExp for partition functions; center exposures to reduce conditioning; add small ridge δ​I\delta I when Σ\Sigma is nearly singular.
* •

  Elastic targets (R1): the I/λsoftI/\lambda\_{\mathrm{soft}} term improves conditioning and ensures strong concavity in the dual; recommended defaults λsoft∈[10,103]\lambda\_{\mathrm{soft}}\in[10,10^{3}] when feasibility is uncertain.
* •

  Robust sets (R2): for ℓ2/ℓ∞\ell\_{2}/\ell\_{\infty} sets, use Algorithm [4](https://arxiv.org/html/2510.24607v1#alg4 "Algorithm 4 ‣ 4.4 EGMU-ProxGrad (Robust Dual, R2) ‣ 4 Algorithms ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures"); for general 𝒰\mathcal{U}, combine projection oracles (or Bregman–Dykstra in tt-space) with Moreau identity.
* •

  Cap/box constraints in ww: half-space KL projections have 1-D solves with monotone residuals (dd​λ​a⊤​w​(λ)=−Varw​(λ)​(a)≤0\frac{d}{d\lambda}a^{\top}w(\lambda)=-\mathrm{Var}\_{w(\lambda)}(a)\leq 0), hence root-finding is unimodal/robust.
* •

  Default solver parameters: ε=10−8\varepsilon=10^{-8}, c=10−4c=10^{-4}, β=0.5\beta=0.5, δ=max⁡(10−10,10−6​tr​(Σ)/K)\delta=\max(10^{-10},10^{-6}\,\mathrm{tr}(\Sigma)/K).

## 7 Extension: Multi-Period and Turnover Regularization (Brief)

At time tt, given previous weights pt−1p\_{t-1}, consider

|  |  |  |
| --- | --- | --- |
|  | minwt∈ΔNDKL(wt∥b)+γDKL(wt∥pt−1)s.t.X⊤wt=τt,Awt≤c.\min\_{w\_{t}\in\Delta^{N}}\ D\_{\mathrm{KL}}\!\left(w\_{t}\middle\|b\right)\;+\;\gamma\,D\_{\mathrm{KL}}\!\left(w\_{t}\middle\|p\_{t-1}\right)\quad\text{s.t.}\quad X^{\top}w\_{t}=\tau\_{t},\;Aw\_{t}\leq c. |  |

This is equivalent (up to an additive constant) to (1+γ)DKL(wt∥b~t)(1+\gamma)\,D\_{\mathrm{KL}}\!\left(w\_{t}\middle\|\tilde{b}\_{t}\right) with the *effective prior*

|  |  |  |
| --- | --- | --- |
|  | b~t,i∝bi11+γ​pt−1,iγ1+γ,\tilde{b}\_{t,i}\ \propto\ b\_{i}^{\frac{1}{1+\gamma}}\;p\_{t-1,i}^{\frac{\gamma}{1+\gamma}}, |  |

hence the solution remains an exponential tilt wt,i∝b~t,i​exp⁡(θt⊤​xi)w\_{t,i}\propto\tilde{b}\_{t,i}\exp(\theta\_{t}^{\top}x\_{i}) and all dual/algorithmic machinery is unchanged after b←b~tb\leftarrow\tilde{b}\_{t}.
If an explicit turnover budget is desired, one may add linearized constraints or standard split variables to encode ℓ1\ell\_{1}-type variation limits, which fit directly into the KL-projection (Bregman–Dykstra) framework.

## 8 Related Work

#### Information projection and exponential families.

Our formulation is a classical II-projection (minimization of KL under linear moment constraints),
which yields exponential-family solutions and a concave dual with covariance Hessian; see
Csiszár [[6](https://arxiv.org/html/2510.24607v1#bib.bib6)] for the geometry of II-divergence, Cover and Thomas [[5](https://arxiv.org/html/2510.24607v1#bib.bib5)] for an information-theoretic treatment,
and Wainwright and Jordan [[9](https://arxiv.org/html/2510.24607v1#bib.bib9)] for the exponential-family viewpoint connecting gradients/Hessians with moments/covariances.

#### Iterative proportional fitting and Bregman projections.

For equality constraints, iterative proportional fitting / generalized iterative scaling (IPF/GIS)
provides a coordinate-wise Bregman projection method with convergence guarantees [[7](https://arxiv.org/html/2510.24607v1#bib.bib7), [6](https://arxiv.org/html/2510.24607v1#bib.bib6)].
For intersections of convex sets (equalities and half-spaces), Bregman–Dykstra cycles converge to the unique Bregman projection
onto the intersection [[3](https://arxiv.org/html/2510.24607v1#bib.bib3)].

#### Entropy pooling and portfolio engineering.

In portfolio applications, our setup parallels Entropy Pooling (EP), which applies cross-entropy
updating to scenario probabilities under linear “views” [[8](https://arxiv.org/html/2510.24607v1#bib.bib8)]. EGMU adapts the same KL geometry to
*asset weights on the simplex* with *factor exposure* constraints, and makes the dual structure and sensitivity
explicitly operational for target-exposure construction.

#### Convex duality, support functions, and robustness.

The elastic and robust variants we study are standard Fenchel–Rockafellar constructs: adding a squared penalty in the primal corresponds to
a Tikhonov (strongly concave) term in the dual; relaxing equalities to a convex target set yields a dual support function. These follow from
textbook convex analysis and duality [[4](https://arxiv.org/html/2510.24607v1#bib.bib4), Ch. 3–5], and integrate seamlessly with the exponential-family moment
structure reviewed by Wainwright and Jordan [[9](https://arxiv.org/html/2510.24607v1#bib.bib9)].

#### Optimization and numerical stability.

Our damped Newton method with backtracking and ridge regularization follows standard convex-optimization practice [[4](https://arxiv.org/html/2510.24607v1#bib.bib4)].
Implementation details (LogSumExp stabilization, covariance centering/ridge, and moment reuse) are tailored to large-NN, small-KK regimes
typical in factor construction.

## 9 Conclusion

EGMU frames target-exposure construction as KL minimization on the simplex with rigorous feasibility, uniqueness, dual structure, and sensitivity. We provide provably convergent solvers—dual Newton and KL projection (IPF/Bregman–Dykstra)—and *extend* the framework to elastic/robust targets with a shared dual-moment core and furnish a path-following ODE. This yields a principled, reproducible baseline requiring minimal empirical work.

## A Proofs and Technical Details

### A.1 Proof of Proposition [1](https://arxiv.org/html/2510.24607v1#Thmproposition1 "Proposition 1 (Feasibility and strict positivity). ‣ 2.2 Feasibility and Strict Positivity ‣ 2 Problem, Feasibility, and Geometry ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures")

Let 𝒳={𝐱i}i=1N\mathcal{X}=\{\mathbf{x}\_{i}\}\_{i=1}^{N}. Since w∈ΔNw\in\Delta^{N} implies X⊤​w=∑iwi​𝐱iX^{\top}w=\sum\_{i}w\_{i}\mathbf{x}\_{i}, feasibility of X⊤​w=tX^{\top}w=t is equivalent to t∈conv​(𝒳)t\in\mathrm{conv}(\mathcal{X}). If t∈relint​conv​(𝒳)t\in\mathrm{relint}\,\mathrm{conv}(\mathcal{X}) and bi>0b\_{i}>0, the KL objective is essentially smooth and strictly convex on the relative interior of the simplex, so the unique minimizer satisfies wi⋆>0w\_{i}^{\star}>0 by standard Lagrange multiplier/KKT arguments. With inequalities A​w≤cAw\leq c, feasibility is a convex polytope; infeasibility admits a Farkas certificate (see, e.g., [4](https://arxiv.org/html/2510.24607v1#bib.bib4), Ch. 5). □\square

### A.2 Exponential Family and Dual Structure

Consider the Lagrangian (equalities only)

|  |  |  |
| --- | --- | --- |
|  | ℒ​(w,λ,ν)=∑iwi​log⁡wibi+λ⊤​(X⊤​w−t)+ν​(𝟏⊤​w−1).\mathcal{L}(w,\lambda,\nu)=\sum\_{i}w\_{i}\log\frac{w\_{i}}{b\_{i}}+\lambda^{\top}(X^{\top}w-t)+\nu(\mathbf{1}^{\top}w-1). |  |

Stationarity in wiw\_{i} gives log⁡wi−log⁡bi+λ⊤​xi+ν+1=0\log w\_{i}-\log b\_{i}+\lambda^{\top}x\_{i}+\nu+1=0, hence

|  |  |  |
| --- | --- | --- |
|  | wi​(θ)=bi​eθ⊤​xi∑jbj​eθ⊤​xj,θ:=−λ.w\_{i}(\theta)=\frac{b\_{i}e^{\theta^{\top}x\_{i}}}{\sum\_{j}b\_{j}e^{\theta^{\top}x\_{j}}},\quad\theta:=-\lambda. |  |

Substituting into the Lagrangian yields the dual L​(θ)=θ⊤​t−log​∑ibi​eθ⊤​xiL(\theta)=\theta^{\top}t-\log\sum\_{i}b\_{i}e^{\theta^{\top}x\_{i}}. Differentiating under the softmax,

|  |  |  |
| --- | --- | --- |
|  | ∇L​(θ)=t−∑iwi​(θ)​xi,∇2L​(θ)=−∑iwi​(θ)​(xi−μ)​(xi−μ)⊤=−Covw​(θ)​(x).\nabla L(\theta)=t-\sum\_{i}w\_{i}(\theta)x\_{i},\qquad\nabla^{2}L(\theta)=-\sum\_{i}w\_{i}(\theta)(x\_{i}-\mu)(x\_{i}-\mu)^{\top}=-\mathrm{Cov}\_{w(\theta)}(x). |  |

Strict concavity holds where Covw​(θ)​(x)≻0\mathrm{Cov}\_{w(\theta)}(x)\succ 0 (see [9](https://arxiv.org/html/2510.24607v1#bib.bib9)). □\square

### A.3 Proof of Theorem [2](https://arxiv.org/html/2510.24607v1#Thmtheorem2 "Theorem 2 (Existence and uniqueness). ‣ 5 Theoretical Guarantees ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures")

DKL(⋅∥b)D\_{\mathrm{KL}}\!\left(\cdot\middle\|b\right) is strictly convex and lower semi-continuous on the simplex; the feasible set is convex and, under Slater, nonempty with nonempty relative interior. Hence a unique minimizer exists. Strict positivity follows from the fact that bi>0b\_{i}>0 and t∈relintt\in\mathrm{relint} enforce finite Lagrange multipliers and thus wi⋆∝bi​eθ⋆⊤​xi>0w\_{i}^{\star}\propto b\_{i}e^{\theta^{\star\top}x\_{i}}>0. □\square

### A.4 Proof of Theorem [4](https://arxiv.org/html/2510.24607v1#Thmtheorem4 "Theorem 4 (Sensitivity). ‣ 5 Theoretical Guarantees ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures")

At optimum, ∇L​(θ⋆)=0⇔𝔼w​(θ⋆)​[x]=t\nabla L(\theta^{\star})=0\iff\mathbb{E}\_{w(\theta^{\star})}[x]=t. Differentiate both sides w.r.t. tt:
∂∂t​𝔼w​(θ⋆)​[x]=I.\frac{\partial}{\partial t}\mathbb{E}\_{w(\theta^{\star})}[x]=I.
Using the exponential-family identity
∂∂θ​𝔼w​(θ)​[x]=Covw​(θ)​(x),\frac{\partial}{\partial\theta}\mathbb{E}\_{w(\theta)}[x]=\mathrm{Cov}\_{w(\theta)}(x),
apply the chain rule to get
Covw⋆​(x)⋅∂θ⋆∂t=I⇒∂θ⋆∂t=Covw⋆​(x)−1.\mathrm{Cov}\_{w^{\star}}(x)\cdot\frac{\partial\theta^{\star}}{\partial t}=I\Rightarrow\frac{\partial\theta^{\star}}{\partial t}=\mathrm{Cov}\_{w^{\star}}(x)^{-1}.
For wi⋆=bi​exp⁡(θ⋆⊤​xi−log⁡Z)w\_{i}^{\star}=b\_{i}\exp(\theta^{\star\top}x\_{i}-\log Z),

|  |  |  |
| --- | --- | --- |
|  | ∂wi⋆∂θ=wi⋆​(xi−μ)⊤,μ=𝔼w⋆​[x].\frac{\partial w\_{i}^{\star}}{\partial\theta}=w\_{i}^{\star}(x\_{i}-\mu)^{\top},\quad\mu=\mathbb{E}\_{w^{\star}}[x]. |  |

Thus ∂wi⋆∂t=wi⋆​(xi−μ)⊤​Covw⋆​(x)−1\dfrac{\partial w\_{i}^{\star}}{\partial t}=w\_{i}^{\star}(x\_{i}-\mu)^{\top}\mathrm{Cov}\_{w^{\star}}(x)^{-1}, yielding the matrix form in the main text. □\square

### A.5 Elastic Dual and Sensitivity (Proof of Thm. [5](https://arxiv.org/html/2510.24607v1#Thmtheorem5 "Theorem 5 (Elastic dual: strong concavity and sensitivity). ‣ 5 Theoretical Guarantees ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures"))

The dual reads Lel​(θ)=L​(θ)−12​λsoft​‖θ‖2L\_{\mathrm{el}}(\theta)=L(\theta)-\tfrac{1}{2\lambda\_{\mathrm{soft}}}\|\theta\|^{2}. Hence ∇Lel=∇L−1λsoft​θ\nabla L\_{\mathrm{el}}=\nabla L-\tfrac{1}{\lambda\_{\mathrm{soft}}}\theta and ∇2Lel=∇2L−1λsoft​I\nabla^{2}L\_{\mathrm{el}}=\nabla^{2}L-\tfrac{1}{\lambda\_{\mathrm{soft}}}I, proving strong concavity. At the maximizer, t−𝔼w​(θ)​[x]−1λsoft​θ=0t-\mathbb{E}\_{w(\theta)}[x]-\tfrac{1}{\lambda\_{\mathrm{soft}}}\theta=0. Differentiating w.r.t. tt and using ∂𝔼w​(θ)​[x]/∂θ=Σ\partial\mathbb{E}\_{w(\theta)}[x]/\partial\theta=\Sigma gives (Σ+1λsoft​I)​∂θ/∂t=I(\Sigma+\tfrac{1}{\lambda\_{\mathrm{soft}}}I)\,\partial\theta/\partial t=I, establishing the stated sensitivities. □\square

### A.6 KL Projection onto a Single Equality (IPF step)

Fix u∈ΔNu\in\Delta^{N} and the set ℋ={w:a⊤​w=τ}\mathcal{H}=\{w:a^{\top}w=\tau\}. Minimize DKL​(w∥u)D\_{\mathrm{KL}}(w\|u) subject to a⊤​w=τa^{\top}w=\tau and 𝟏⊤​w=1\mathbf{1}^{\top}w=1. Stationarity: log⁡(wi/ui)+1+α​ai+ν=0\log(w\_{i}/u\_{i})+1+\alpha a\_{i}+\nu=0, so wi∝ui​eα​aiw\_{i}\propto u\_{i}e^{\alpha a\_{i}}. The normalization ensures w​(α)∈ΔNw(\alpha)\in\Delta^{N}. Define ϕ​(α)=a⊤​w​(α)−τ\phi(\alpha)=a^{\top}w(\alpha)-\tau. One computes ϕ′​(α)=Varw​(α)​(a)>0\phi^{\prime}(\alpha)=\mathrm{Var}\_{w(\alpha)}(a)>0 unless aa is degenerate, hence a unique root exists and can be found by bisection. □\square

### A.7 KL Projection onto a Half-space (Inequality step)

For ℋ={w:a⊤​w≤τ}\mathcal{H}=\{w:a^{\top}w\leq\tau\}, if uu is feasible, the projection is uu. Otherwise, the KKT conditions yield w​(λ)∝u⊙e−λ​aw(\lambda)\propto u\odot e^{-\lambda a} with λ≥0\lambda\geq 0 chosen so that a⊤​w​(λ)=τa^{\top}w(\lambda)=\tau. Monotonicity follows from dd​λ​a⊤​w​(λ)=−Varw​(λ)​(a)≤0\frac{d}{d\lambda}a^{\top}w(\lambda)=-\mathrm{Var}\_{w(\lambda)}(a)\leq 0. □\square

### A.8 Convergence of EGMU-Newton (Refinement of Thm. [6](https://arxiv.org/html/2510.24607v1#Thmtheorem6 "Theorem 6 (Convergence of EGMU-Newton). ‣ 5 Theoretical Guarantees ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures"))

The objective L​(θ)=θ⊤​t−log​∑ibi​eθ⊤​xiL(\theta)=\theta^{\top}t-\log\sum\_{i}b\_{i}e^{\theta^{\top}x\_{i}} is twice continuously differentiable and concave, with ∇L​(θ)=t−𝔼w​(θ)​[x]\nabla L(\theta)=t-\mathbb{E}\_{w(\theta)}[x] and ∇2L​(θ)=−Covw​(θ)​(x)\nabla^{2}L(\theta)=-\mathrm{Cov}\_{w(\theta)}(x). If ‖xi‖2≤R\|x\_{i}\|\_{2}\leq R for all ii, then ‖∇2L​(θ)‖≤R2\|\nabla^{2}L(\theta)\|\leq R^{2} for all θ\theta, and ∇2L\nabla^{2}L is locally Lipschitz (with constant depending on RR and the third centered moment). Under these mild smoothness conditions, damped Newton with Armijo backtracking is globally convergent and locally quadratically convergent in a neighborhood of θ⋆\theta^{\star} for strongly concave LL on the relevant subspace (see [4](https://arxiv.org/html/2510.24607v1#bib.bib4), Ch. 9). Ridge regularization (Σ+δ​I)(\Sigma+\delta I) stabilizes solves when Σ\Sigma is ill-conditioned; as δ↓0\delta\downarrow 0 the step approaches the exact Newton direction.

### A.9 Convergence of IPF and Bregman–Dykstra (Proof of Thm. [7](https://arxiv.org/html/2510.24607v1#Thmtheorem7 "Theorem 7 (Convergence of projection schemes). ‣ 5 Theoretical Guarantees ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures"))

Part (i) follows from Csiszár’s II-projection theory and the Darroch–Ratcliff analysis of generalized iterative scaling for log-linear models [[6](https://arxiv.org/html/2510.24607v1#bib.bib6), [7](https://arxiv.org/html/2510.24607v1#bib.bib7)]. Part (ii) is a special case of Dykstra’s algorithm with Bregman divergences: for finitely many closed convex sets and a Legendre-type Bregman generator (negative entropy here), the cyclic projections converge to the unique Bregman projection onto the intersection [[3](https://arxiv.org/html/2510.24607v1#bib.bib3)]. □\square

### A.10 Carathéodory support bound (remark)

Any t∈conv​{𝐱i}t\in\mathrm{conv}\{\mathbf{x}\_{i}\} admits a representation using at most K+1K+1 points. See, e.g., Barvinok [[1](https://arxiv.org/html/2510.24607v1#bib.bib1)]. This yields a sparsity upper bound for exact feasibility, though KL minimization under strictly positive prior typically produces dense solutions unless boundary constraints are active.

### A.11 Robust dual and proximal map (details)

Let g​(y)=ιt0+𝒰​(y)g(y)=\iota\_{\,t\_{0}+\mathcal{U}}(y). Its Fenchel conjugate is
g∗​(θ)=supy{θ⊤​y−g​(y)}=supu∈𝒰θ⊤​(t0+u)=θ⊤​t0+σ𝒰​(θ)g^{\*}(\theta)=\sup\_{y}\{\theta^{\top}y-g(y)\}=\sup\_{u\in\mathcal{U}}\theta^{\top}(t\_{0}+u)=\theta^{\top}t\_{0}+\sigma\_{\mathcal{U}}(\theta),
hence the robust dual in §[3.4](https://arxiv.org/html/2510.24607v1#S3.SS4 "3.4 Robust Target Sets via Support Functions ‣ 3 Duality and Exponential-Family Form ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures"). For the proximal step, use Moreau’s identity for conjugates:
proxη​g∗​(z)=z−η​proxg/η​(z/η)\mathrm{prox}\_{\eta g^{\*}}(z)=z-\eta\,\mathrm{prox}\_{g/\eta}(z/\eta).
Since g/ηg/\eta is the indicator of t0+𝒰t\_{0}+\mathcal{U}, proxg/η​(z/η)=Πt0+𝒰​(z/η)\mathrm{prox}\_{g/\eta}(z/\eta)=\Pi\_{\,t\_{0}+\mathcal{U}}(z/\eta).
With the translation y↦y−t0y\mapsto y-t\_{0}, this yields
proxη​σ𝒰​(z)=z−η​Π𝒰​(z/η)\mathrm{prox}\_{\eta\,\sigma\_{\mathcal{U}}}(z)=z-\eta\,\Pi\_{\mathcal{U}}(z/\eta) used in Algorithm [4](https://arxiv.org/html/2510.24607v1#alg4 "Algorithm 4 ‣ 4.4 EGMU-ProxGrad (Robust Dual, R2) ‣ 4 Algorithms ‣ Entropy-Guided Multiplicative Updates: KL Projections for Multi-Factor Target Exposures"). □\square

### A.12 Existence and uniqueness of the solution path ODE

For t​(λ)=t0+λ​Δt(\lambda)=t\_{0}+\lambda\Delta, the optimal θ​(λ)\theta(\lambda) satisfies
F​(θ,λ):=t​(λ)−𝔼w​(θ)​[x]−1λsoft​θ=0F(\theta,\lambda):=t(\lambda)-\mathbb{E}\_{w(\theta)}[x]-\tfrac{1}{\lambda\_{\mathrm{soft}}}\theta=0.
Then ∂θF​(θ,λ)=Σ​(θ)+1λsoft​I⪰m​I\partial\_{\theta}F(\theta,\lambda)=\Sigma(\theta)+\tfrac{1}{\lambda\_{\mathrm{soft}}}I\succeq mI on a neighborhood where
Σ\Sigma is bounded below. By the implicit function theorem, there exists a unique C1C^{1} path θ​(λ)\theta(\lambda) with
d​θd​λ=(Σ​(θ)+1λsoft​I)−1​Δ\dfrac{d\theta}{d\lambda}=\big(\Sigma(\theta)+\tfrac{1}{\lambda\_{\mathrm{soft}}}I\big)^{-1}\Delta.
Under locally Lipschitz ∇2L\nabla^{2}L, Euler and RK2 integrators achieve O​(h)O(h) and O​(h2)O(h^{2}) global errors respectively. □\square

## Classification and availability

JEL: G11, C61, C63, C58. MSC 2020: 90C25, 90C90, 62F10, 94A17. Reproducibility: Minimal synthetic scripts (Newton/IPF/ProxGrad/Path) to reproduce algorithms and figures are provided in the supplementary material; no proprietary data are used.

## References

* Barvinok [2002]

  A. Barvinok.
  *A Course in Convexity*, volume 54 of *Graduate Studies in Mathematics*.
  American Mathematical Society, Providence, RI, 2002.
* Bauschke and Combettes [2011]

  H. H. Bauschke and P. L. Combettes.
  *Convex Analysis and Monotone Operator Theory in Hilbert Spaces*.
  Springer, New York, 2011.
* Bauschke and Lewis [2000]

  H. H. Bauschke and A. S. Lewis.
  Dykstra’s algorithm with bregman projections: A convergence proof.
  *Optimization*, 48(4):409–427, 2000.
* Boyd and Vandenberghe [2004]

  S. Boyd and L. Vandenberghe.
  *Convex Optimization*.
  Cambridge University Press, Cambridge, 2004.
* Cover and Thomas [2006]

  T. M. Cover and J. A. Thomas.
  *Elements of Information Theory*.
  Wiley-Interscience, Hoboken, NJ, 2 edition, 2006.
* Csiszár [1975]

  I. Csiszár.
  I-divergence geometry of probability distributions and minimization problems.
  *The Annals of Probability*, 3(1):146–158, 1975.
* Darroch and Ratcliff [1972]

  J. N. Darroch and D. Ratcliff.
  Generalized iterative scaling for log-linear models.
  *The Annals of Mathematical Statistics*, 43(5):1470–1480, 1972.
* Meucci [2008]

  A. Meucci.
  Fully flexible views: Theory and practice.
  *Risk*, 21(10):97–102, 2008.
* Wainwright and Jordan [2008]

  M. J. Wainwright and M. I. Jordan.
  Graphical models, exponential families, and variational inference.
  *Foundations and Trends in Machine Learning*, 1(1-2):1–305, 2008.