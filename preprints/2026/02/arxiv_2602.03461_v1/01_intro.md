---
authors:
- Philipp J. Schneider
- Daniel Kuhn
doc_id: arxiv:2602.03461v1
family_id: arxiv:2602.03461
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Soft-Radial Projection for Constrained End-to-End Learning
url_abs: http://arxiv.org/abs/2602.03461v1
url_html: https://arxiv.org/html/2602.03461v1
venue: arXiv q-fin
version: 1
year: 2026
---


Philipp J. Schneider  Daniel Kuhn
Risk Analytics and Optimization Chair


 EPFL
{philipp.schneider, daniel.kuhn}@epfl.ch

###### Abstract

Integrating hard constraints into deep learning is essential for safety-critical systems. Yet existing constructive layers that project predictions onto constraint boundaries face a fundamental bottleneck: *gradient saturation*. By collapsing exterior points onto lower-dimensional surfaces, standard orthogonal projections induce rank-deficient Jacobians, which nullify gradients orthogonal to active constraints and hinder optimization. We introduce Soft-Radial Projection, a differentiable reparameterization layer that circumvents this issue through a radial mapping from Euclidean space into the *interior* of the feasible set. This construction guarantees strict feasibility while preserving a full-rank Jacobian almost everywhere, thereby preventing the optimization stalls typical of boundary-based methods. We theoretically prove that the architecture retains the universal approximation property and empirically show improved convergence behavior and solution quality over state-of-the-art optimization- and projection-based baselines.

## 1 Introduction

Many decision-making systems operate under hard constraints during both training and deployment—for example, safety envelopes in autonomous driving, actuator limits in robotics (Brunke et al., [2022](https://arxiv.org/html/2602.03461v1#bib.bib47 "Safe learning in robotics: From learning-based control to safe reinforcement learning")), or budget and capacity constraints in operations. While neural networks are powerful function approximators, they are not inherently constraint-aware, and naive usage can lead to *infeasible* outputs precisely in scenarios where constraint violations have serious consequences. We formalize constrained learning objectives and propose architectural mechanisms that enforce feasibility *by construction*.

Setup. Let 𝒵⊆ℝd\mathcal{Z}\subseteq\mathbb{R}^{d} be the input space, 𝒴⊆ℝn\mathcal{Y}\subseteq\mathbb{R}^{n} the target space, and 𝒞⊆ℝn\mathcal{C}\subseteq\mathbb{R}^{n} the feasible set of decisions, assumed closed and convex with a nonempty interior. This assumption is without loss of generality, as we can always restrict the ambient space to the affine hull of the convex set. Data are drawn from a distribution ℙ\mathbb{P} on 𝒵×𝒴\mathcal{Z}\times\mathcal{Y} with marginal ℙZ\mathbb{P}\_{Z} on 𝒵\mathcal{Z}. We define the policy space Π\Pi as the set of all measurable mappings π:𝒵→ℝn\pi:\mathcal{Z}\to\mathbb{R}^{n} that map an input zz to a decision.

Supervised learning. Let (z,y)∼ℙ(z,y)\sim\mathbb{P}. We learn an optimal policy by solving

|  |  |  |  |
| --- | --- | --- | --- |
|  | minπ∈Π𝔼(z,y)∼ℙ​[ℓ​(π​(z),y)]s.t.π​(z)∈𝒞for ℙZ-a.e. ​z,\begin{array}[]{cl}\displaystyle\min\_{\pi\in\Pi}&\displaystyle\mathbb{E}\_{(z,y)\sim\mathbb{P}}\big[\ell\big(\pi(z),y\big)\big]\\ \text{s.t.}&\pi(z)\in\mathcal{C}\quad\text{for $\mathbb{P}\_{Z}$-a.e.\ }z,\end{array} |  | (1) |

where ℓ:𝒞×𝒴→ℝ\ell:\mathcal{C}\times\mathcal{Y}\to\mathbb{R} is a chosen loss. This formulation covers standard regression tasks as well as imitation learning, where the label yy represents a hindsight-optimal decision π⋆​(z)\pi^{\star}(z). In such cases, ℓ\ell quantifies the distance to the optimal decision or a regret surrogate.

Task-driven learning. Without labels, we measure performance directly via a task cost c:𝒵×𝒞→ℝc:\mathcal{Z}\times\mathcal{C}\to\mathbb{R} and optimize

|  |  |  |  |
| --- | --- | --- | --- |
|  | minπ∈Π𝔼z∼ℙZ​[c​(z,π​(z))]s.t.π​(z)∈𝒞for ℙZ-a.e. ​z.\begin{array}[]{cl}\displaystyle\min\_{\pi\in\Pi}&\displaystyle\mathbb{E}\_{z\sim\mathbb{P}\_{Z}}\big[c\big(z,\pi(z)\big)\big]\\ \text{s.t.}&\pi(z)\in\mathcal{C}\quad\text{for $\mathbb{P}\_{Z}$-a.e.\ }z.\end{array} |  | (2) |

This formulation aligns the training objective with the downstream operational cost, thereby circumventing the potential objective mismatch inherent in surrogate supervised targets (Donti et al., [2017](https://arxiv.org/html/2602.03461v1#bib.bib48 "Task-based end-to-end model learning in stochastic optimization"); Elmachtoub and Grigas, [2022](https://arxiv.org/html/2602.03461v1#bib.bib49 "Smart “predict, then optimize”"); Rychener et al., [2023](https://arxiv.org/html/2602.03461v1#bib.bib22 "End-to-end learning for stochastic optimization: A Bayesian perspective"); Chenreddy and Delage, [2024](https://arxiv.org/html/2602.03461v1#bib.bib56 "End-to-end conditional robust optimization")).

Feasibility by construction. Optimization over the space of constrained functions is generally intractable. However, we can simplify the problem by leveraging the *Interchangeability Principle* (Rockafellar and Wets, [2009](https://arxiv.org/html/2602.03461v1#bib.bib37 "Variational Analysis"), Theorem 14.60). Applied to the task-driven formulation ([2](https://arxiv.org/html/2602.03461v1#S1.E2 "Equation 2 ‣ 1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning")), this principle establishes that minimizing the expected cost is equivalent to minimizing the cost pointwise for almost every input zz, formally infπ∈Π,π​(z)∈𝒞𝔼z∼ℙZ​[c​(z,π​(z))]=𝔼z∼ℙZ​[infx∈𝒞c​(z,x)]\inf\_{\pi\in\Pi,\,\pi(z)\in\mathcal{C}}\mathbb{E}\_{z\sim\mathbb{P}\_{Z}}[c(z,\pi(z))]=\mathbb{E}\_{z\sim\mathbb{P}\_{Z}}\left[\inf\_{x\in\mathcal{C}}c(z,x)\right]. This equivalence allows us to solve the functional problem by finding a pointwise optimal decision for any given input zz. We enforce constraints constructively by reparameterizing the decision policy: we optimize an unconstrained candidate function g:𝒵→ℝng:\mathcal{Z}\to\mathbb{R}^{n} composed with a fixed projection operator, such that π​(z)=Proj​(g​(z))\pi(z)=\text{Proj}(g(z)).

The geometric properties of the projection are decisive for the optimization landscape. The standard approach is the *orthogonal projection* of a vector u∈ℝnu\in\mathbb{R}^{n}, denoted P​(u)=arg⁡minv∈𝒞⁡‖u−v‖2P(u)=\arg\min\_{v\in\mathcal{C}}\|u-v\|^{2}. While PP guarantees feasibility, it maps the entire exterior space onto the lower-dimensional boundary ∂𝒞\partial\mathcal{C}. In Figure [1(a)](https://arxiv.org/html/2602.03461v1#S1.F1.sf1 "Figure 1(a) ‣ Figure 1 ‣ 1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning"), we demonstrate the phenomenon of gradient saturation. This occurs when the unconstrained output u=g​(z)u=g(z) falls outside 𝒞\mathcal{C} and the level sets of the objective are orthogonal to the boundary. Because PP collapses the exterior space onto the surface ∂𝒞\partial\mathcal{C}, infinitesimal variations of uu orthogonal to the boundary result in zero change to the output π​(z)\pi(z). Consequently, gradient components in these directions are nullified, and the optimization dynamics stall or crawl along the boundary. While the projection is idempotent—preserving the landscape for points already in the interior—the optimization landscape for exterior points u∉𝒞u\notin\mathcal{C} becomes rank-deficient.

![Refer to caption](x1.png)


(a) Orthogonal projection P​(u)P(u).

![Refer to caption](x2.png)


(b) Soft-radial projection p​(u)p(u) into Int⁡(𝒞)\operatorname{Int}(\mathcal{C}).

Figure 1: Impact of projection geometry on optimization. Comparison of (a) Orthogonal and (b) Soft-Radial Projection on a 2D constrained task (target ×\times). Main plots visualize the trajectory of the unconstrained candidate (∘\circ) versus the feasible decision (++). Insets show the coordinate grid warping (A) and training loss (B). Note that soft-radial projection prevents gradient saturation by maintaining descent signals for infeasible inputs.

Soft-Radial Projection to the interior. We instantiate the projection layer as a *Soft-Radial Projection* p:ℝn→Int⁡(𝒞)p:\mathbb{R}^{n}\to\operatorname{Int}(\mathcal{C}) constructed as a radial homeomorphism. Unlike the orthogonal projection, this map keeps every output strictly inside the interior Int⁡(𝒞)\operatorname{Int}(\mathcal{C}), acting as a smooth reparameterization of the feasible set rather than a distance-minimizing operator. By enforcing a diffeomorphic correspondence almost everywhere, we ensure well-conditioned gradients that guide the optimizer efficiently through the feasible region—and asymptotically toward the boundary if necessary—without the saturation artifacts of the orthogonal projection (cf. Figure [1](https://arxiv.org/html/2602.03461v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning")).

Related work.
The challenge of obtaining feasibility guarantees for neural networks has attracted broad interest across research domains, ranging from safety-critical control (Garcıa and Fernández, [2015](https://arxiv.org/html/2602.03461v1#bib.bib51 "A comprehensive survey on safe reinforcement learning")) to decision-focused analytics (Kotary et al., [2021](https://arxiv.org/html/2602.03461v1#bib.bib52 "End-to-end constrained optimization learning: A survey")). For an extensive review, we refer to Appendix [A](https://arxiv.org/html/2602.03461v1#A1 "Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning"). Existing methodologies can be broadly categorized into optimization-based layers (e.g., Amos and Kolter, [2017](https://arxiv.org/html/2602.03461v1#bib.bib30 "Optnet: Differentiable optimization as a layer in neural networks"); Agrawal et al., [2019](https://arxiv.org/html/2602.03461v1#bib.bib18 "Differentiable convex optimization layers"); Donti et al., [2021](https://arxiv.org/html/2602.03461v1#bib.bib16 "DC3: A learning method for optimization with hard constraints")), which operate via implicit differentiation through iterative solvers, and constructive layers that enforce feasibility by design via specialized projections (e.g., Konstantinov and Utkin, [2023](https://arxiv.org/html/2602.03461v1#bib.bib3 "A new computationally simple approach for implementing neural networks with output hard constraints"); Liang et al., [2024](https://arxiv.org/html/2602.03461v1#bib.bib7 "Homeomorphic projection to ensure neural-network solution feasibility for constrained optimization")). Crucially, the current research frontier has shifted beyond merely guaranteeing constraint satisfaction (Dalal et al., [2018](https://arxiv.org/html/2602.03461v1#bib.bib21 "Safe exploration in continuous action spaces")) to ensuring smooth optimization landscapes that facilitate superior learning performance.

Contributions. Our main contributions are as follows:

* •

  We introduce Soft-Radial Projection, a closed-form layer for convex sets that ensures strict interior feasibility via a radial transformation (differentiable almost everywhere).
* •

  We provide a theoretical analysis of the gradient dynamics, showing that our construction avoids the rank-deficient Jacobian issues inherent to orthogonal projections.
* •

  We prove that the architecture preserves the Universal Approximation property (Theorem [4](https://arxiv.org/html/2602.03461v1#S4 "4 Constrained Universal Approximation ‣ Soft-Radial Projection for Constrained End-to-End Learning")) for continuous functions mapping into Int⁡(𝒞)\operatorname{Int}(\mathcal{C}).
* •

  Empirical results demonstrate the effectiveness of our method in end-to-end learning tasks, including portfolio optimization and resource allocation for demand sharing.

We proceed by formally introducing the soft-radial projection mechanism.

Notation.
We use ‖u‖\|u\| for the Euclidean norm of vectors and ‖A‖\|A\| for the spectral norm of matrices. For functions ψ:𝒵→ℝn\psi:\mathcal{Z}\to\mathbb{R}^{n}, we denote the uniform norm by ‖ψ‖∞≔supz∈𝒵‖ψ​(z)‖\|\psi\|\_{\infty}\coloneqq\sup\_{z\in\mathcal{Z}}\|\psi(z)\|. We write Int⁡(𝒞)\operatorname{Int}(\mathcal{C}) and ∂𝒞\partial\mathcal{C} for the interior and boundary of the feasible set. The Jacobian of a differentiable map ϕ\phi is denoted by JϕJ\_{\phi}. We reserve uu for unconstrained vectors (pre-projection) and use xx or π​(z)\pi(z) for feasible vectors in 𝒞\mathcal{C}.

## 2 Soft-Radial Projection Layer

Many models output a raw vector in ℝn\mathbb{R}^{n} that must satisfy hard constraints at inference time—e.g., neural networks and decoders, control policies, differentiable optimization layers, or amortized solvers. We place a *soft-radial projection layer* p:ℝn→Int⁡(𝒞)p:\mathbb{R}^{n}\to\operatorname{Int}(\mathcal{C}) downstream of such modules so that, regardless of how the raw output is produced (even if infeasible), the final decision lies in the feasible set.

Concretely, we instantiate the unconstrained candidate gg as a parameterized map gθ:𝒵→ℝng\_{\theta}:\mathcal{Z}\to\mathbb{R}^{n} (e.g., a neural network). Given the raw output u=gθ​(z)u=g\_{\theta}(z), we set the policy as πθ=p∘gθ\pi\_{\theta}=p\circ g\_{\theta}, which ensures πθ​(z)∈Int⁡(𝒞)\pi\_{\theta}(z)\in\operatorname{Int}(\mathcal{C}) during training and deployment without penalty tuning or post-hoc repair. The learning objectives ([1](https://arxiv.org/html/2602.03461v1#S1.E1 "Equation 1 ‣ 1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning")) and ([2](https://arxiv.org/html/2602.03461v1#S1.E2 "Equation 2 ‣ 1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning")) are then instantiated by composing with pp (e.g., ℓ​(πθ​(z),y)\ell(\pi\_{\theta}(z),y) or c​(z,πθ​(z))c(z,\pi\_{\theta}(z))). This composition turns any base predictor into a constraint-satisfying model while keeping gradients usable for end-to-end training. The remainder of this section develops the geometry and regularity of pp needed for gradient-based methods. We first formalize the soft-radial projection pp and its raywise components. The construction relies on a smooth contraction toward an anchor point, mapping the entire ambient space into the interior of 𝒞\mathcal{C} while retaining differentiability almost everywhere.

###### Definition 2.1 (Soft-Radial Projection).

Let 𝒞⊆ℝn\mathcal{C}\subseteq\mathbb{R}^{n} be a closed, convex set with nonempty interior, and fix an anchor point u0∈Int⁡(𝒞)u\_{0}\in\operatorname{Int}(\mathcal{C}). Let r:ℝ+→[0,1)r:\mathbb{R}\_{+}\to[0,1) be continuous and strictly increasing with r​(0)>0r(0)>0 and limρ→∞r​(ρ)=1\lim\_{\rho\to\infty}r(\rho)=1.

For any u∈ℝnu\in\mathbb{R}^{n}, the *soft-radial projection* of uu onto 𝒞\mathcal{C} is

|  |  |  |
| --- | --- | --- |
|  | p​(u)=u0+r​(‖u−u0‖2)​(q​(u)−u0),p(u)\;=\;u\_{0}\;+\;r\!\big(\|u-u\_{0}\|^{2}\big)\,\big(q(u)-u\_{0}\big), |  |

where q​(u)q(u) denotes the *hard radial projection* of uu onto 𝒞\mathcal{C},

|  |  |  |
| --- | --- | --- |
|  | q​(u)={u,if ​u∈𝒞,u0+α⋆​(u)​(u−u0),otherwise.q(u)\;=\;\begin{cases}u,&\text{if }u\in\mathcal{C},\\[4.0pt] u\_{0}+\alpha^{\star}(u)(u-u\_{0}),&\text{otherwise}.\end{cases} |  |

The scaling factor α⋆​(u)\alpha^{\star}(u) is defined as

|  |  |  |
| --- | --- | --- |
|  | α⋆​(u)=sup{α∈[0,1]:u0+α​(u−u0)∈𝒞}∈[0,1].\alpha^{\star}(u)\;=\;\sup\{\alpha\in[0,1]:\;u\_{0}+\alpha(u-u\_{0})\in\mathcal{C}\}\in[0,1]. |  |

###### Remark 2.2.

The mapping qq projects uu onto 𝒞\mathcal{C} along the ray emanating from the anchor u0u\_{0}, in contrast to the usual Euclidean (orthogonal) projection. The soft-radial projection pp then interpolates between u0u\_{0} and q​(u)q(u), with interpolation factor governed by r​(‖u−u0‖2)r(\|u-u\_{0}\|^{2}) (see Fig. [2](https://arxiv.org/html/2602.03461v1#S2.F2 "Figure 2 ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning")). If we drop the strict-interior requirement and allow r≡1r\equiv 1, then p​(u)=q​(u)p(u)=q(u) and the soft-radial projection takes the form of the hard radial projection.

![Refer to caption](x3.png)


Figure 2: Geometric intuition. A ray from anchor u0u\_{0} through input uu intersects the boundary ∂𝒞\partial\mathcal{C} at the hard radial projection q​(u)q(u). Our soft-radial mapping p​(u)p(u) strictly enforces feasibility by smoothly interpolating along the segment [u0,q​(u)][u\_{0},q(u)] via the radial weight rr.

Coordinate convention. The construction of pp is invariant under translations of both the input and the set: replacing uu by u−u0u-u\_{0} and 𝒞\mathcal{C} by 𝒞−{u0}\mathcal{C}-\{u\_{0}\} leaves all statements below unchanged. In the proofs, we therefore assume, without loss of generality, that the anchor is at the origin, 0∈Int⁡(𝒞)0\in\operatorname{Int}(\mathcal{C}), so that q​(u)=uq(u)=u for u∈𝒞u\in\mathcal{C}, q​(u)=α⋆​(u)​uq(u)=\alpha^{\star}(u)\,u otherwise, and the soft-radial projection simply reads p​(u)=r​(‖u‖2)​q​(u)p(u)=r(\|u\|^{2})\,q(u). For a general anchor u0u\_{0}, one recovers the global form by applying these statements to 𝒞−{u0}\mathcal{C}-\{u\_{0}\} and u−u0u-u\_{0}, and then translating back by u0u\_{0}.

Regularity of components.
We first record basic properties of the ray map qq and the scalar α⋆\alpha^{\star}. These facts will be used later to build a raywise parametrization of Int⁡(𝒞)\operatorname{Int}(\mathcal{C}) and to analyze ℓ∘p\ell\circ p with first-order methods. In particular, continuity and local Lipschitz continuity of qq ensure that composing losses with pp preserves standard first-order optimization guarantees on compact sublevel sets.

{restatable}

lemmaRayRegularity
(Ray intersection and continuity). Let 𝒞⊂ℝn\mathcal{C}\subset\mathbb{R}^{n} be nonempty, closed, and convex with nonempty interior, and assume 0∈Int⁡(𝒞)0\in\operatorname{Int}(\mathcal{C}). For any u∈ℝnu\in\mathbb{R}^{n}, the set

|  |  |  |
| --- | --- | --- |
|  | {α∈[0,1]:α​u∈𝒞}\{\alpha\in[0,1]:\alpha u\in\mathcal{C}\} |  |

is a nonempty closed interval [0,α⋆​(u)][0,\alpha^{\star}(u)] for a unique α⋆​(u)∈[0,1]\alpha^{\star}(u)\in[0,1], and q​(u)∈𝒞q(u)\in\mathcal{C}. Moreover, α⋆\alpha^{\star} is globally Lipschitz continuous and qq is locally Lipschitz (and therefore differentiable almost everywhere by Rademacher’s theorem; see, e.g., Federer ([1969](https://arxiv.org/html/2602.03461v1#bib.bib26 "Geometric measure theory")), Thm. 3.1.6).

Structural properties of pp. We now analyze the global geometry of pp. A critical requirement is that pp must preserve the *representational capacity* of the model gg. Unlike orthogonal projections, which suffer from dimensional collapse by mapping the exterior space onto the boundary surface (a many-to-one mapping), our construction guarantees that pp induces a *one-to-one parametrization* of Int⁡(𝒞)\operatorname{Int}(\mathcal{C}) by strictly rescaling radii along rays emanating from the origin.

###### Assumption 2.3 (Radial monotonicity).

The function r:ℝ+→[0,1)r:\mathbb{R}\_{+}\to[0,1) is C1C^{1}, strictly increasing with r′​(ρ)>0r^{\prime}(\rho)>0 for all ρ>0\rho>0, and satisfies r​(0)>0r(0)>0 and limρ→∞r​(ρ)=1\lim\_{\rho\to\infty}r(\rho)=1.

Assumption [2.3](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem3 "Assumption 2.3 (Radial monotonicity). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning") ensures that the soft-radial projection is strictly monotonic along rays, providing the topological foundation for the one-to-one mapping. This prevents distinct points on the same ray from collapsing to the same interior location. Specifically, the scalar map t↦r​(t2)​tt\mapsto r(t^{2})t has derivative dd​t​[r​(t2)​t]=r​(t2)+2​t2​r′​(t2)\frac{d}{dt}\bigl[r(t^{2})t\bigr]\;=\;r(t^{2})+2t^{2}r^{\prime}(t^{2}).
Since rr and r′r^{\prime} are positive, this derivative is strictly positive for all t≥0t\geq 0, confirming that pp is an injective transformation into Int⁡(𝒞)\operatorname{Int}(\mathcal{C}).

The mapping pp admits a radial decomposition into angular and radial components, simplifying the analysis. Since the projection preserves the direction of the ray ℝ+​v\mathbb{R}\_{+}v (the angular component), its behavior is fully characterized by its action on the scalar distance from the origin—the radial component.

###### Definition 2.4 (Boundary distance).

Fix a unit direction v∈ℝnv\in\mathbb{R}^{n} (‖v‖=1\|v\|=1). We define the *boundary distance* t¯​(v)∈(0,∞]\bar{t}(v)\in(0,\infty] as the distance from the origin to the boundary of 𝒞\mathcal{C} along vv, given by t¯​(v)≔sup{t≥0:t​v∈𝒞}\bar{t}(v)\coloneqq\sup\{t\geq 0:tv\in\mathcal{C}\}.

With the boundary established, the radial profile of the projection is defined by the function ψv\psi\_{v}. This map distinguishes between the interior regime, where the ray remains within 𝒞\mathcal{C}, and the exterior regime, where the input is scaled relative to the boundary.

###### Definition 2.5 (Scalar projection map).

For a fixed unit direction vv, define the map ψv:[0,∞)→[0,∞)\psi\_{v}:[0,\infty)\to[0,\infty) by ψv​(t)≔r​(t2)​min⁡{t,t¯​(v)}.\psi\_{v}(t)\coloneqq r(t^{2})\min\{t,\bar{t}(v)\}.

By construction, the soft-radial projection satisfies p​(t​v)=ψv​(t)​vp(tv)=\psi\_{v}(t)v. With this decomposition, we now establish the regularity of these components. The following lemma verifies that the boundary distance varies continuously with direction and that the scalar projection is strictly monotonic—properties that are essential for proving the soft-radial projection is a global bijection.

{restatable}

lemmaRegComponents
(Regularity of components). The boundary distance map t¯\bar{t} is continuous on the unit sphere {v:‖v‖=1}\{v:\|v\|=1\} (with values in (0,∞](0,\infty]). Moreover, under Assumption [2.3](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem3 "Assumption 2.3 (Radial monotonicity). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning"), for any unit direction vv, the scalar map ψv\psi\_{v} is continuous and strictly increasing, and its range is exactly [0,t¯​(v))[0,\bar{t}(v)).

The raywise analysis in Lemma [2.5](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem5 "Definition 2.5 (Scalar projection map). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning") provides the sufficient conditions to characterize the global topology of pp. We now formally state the main result: pp is a homeomorphism, acting as a reversible deformation of the entire ambient space ℝn\mathbb{R}^{n} onto the feasible interior Int⁡(𝒞)\operatorname{Int}(\mathcal{C}).

{restatable}

theoremHomeomorphism
(Homeomorphism). Under Assumption [2.3](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem3 "Assumption 2.3 (Radial monotonicity). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning"), the soft-radial projection p:ℝn→Int⁡(𝒞)p:\mathbb{R}^{n}\to\operatorname{Int}(\mathcal{C}) is a homeomorphism.

This theorem confirms that the soft-radial layer preserves the topological structure of the unconstrained function space. Avoiding the dimensional collapse of hard projections, pp maintains a full-dimensional, bijective correspondence between the parameter space and the feasible policy space.

Differential regularity. Finally, to enable gradient-based learning, we require the projection to be differentiable and the resulting optimization landscape to be free of projection-induced vanishing gradients.

{restatable}

theoremDiffInvert
(Differentiability and invertibility). Under Assumption [2.3](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem3 "Assumption 2.3 (Radial monotonicity). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning"), the soft-radial projection pp is differentiable almost everywhere on ℝn\mathbb{R}^{n}. The Jacobian Jp​(u)J\_{p}(u) is invertible at every point uu where it exists.

The global invertibility of JpJ\_{p} ensures that the mapping is *full-rank* almost everywhere. Consequently, the gradient signal is preserved even when the raw output is far outside 𝒞\mathcal{C}, strictly avoiding the rank-deficiency and optimization stalling characteristic of standard orthogonal projections.

## 3 Optimization Guarantees

After establishing the geometry of the projection layer, we now analyze its implications for *unconstrained optimization*. Consider a standard constrained task where we seek to minimize a loss ℓ​(x)\ell(x) over the feasible set 𝒞\mathcal{C}. By equipping the model with the soft-radial projection, we transform this into the unconstrained minimization of the *composite objective* f​(u)≔ℓ​(p​(u))f(u)\coloneqq\ell(p(u)), where u∈ℝnu\in\mathbb{R}^{n} denotes the unconstrained candidate vector (e.g., the model output u=g​(z)u=g(z)).

The following discussion translates the geometric properties of pp into concrete optimization guarantees for ff, proceeding from the consistency of optimal values to algorithmic convergence rates.

Optimal value equivalence.
Our primary requirement is that solving the unconstrained formulation f​(u)f(u) is equivalent to solving the original constrained objective ℓ​(x)\ell(x). The homeomorphism property of pp guarantees that the global minima align, meaning no valid solutions are lost and no spurious solutions are created.

{restatable}

theoremEquivOptVal
(Equivalence of optimal values). Let ℓ:𝒞→ℝ\ell:\mathcal{C}\to\mathbb{R} be continuous. With f≔ℓ∘pf\coloneqq\ell\circ p, we have

|  |  |  |
| --- | --- | --- |
|  | infu∈ℝnf​(u)=infx∈Int⁡(𝒞)ℓ​(x)=infx∈𝒞ℓ​(x).\inf\_{u\in\mathbb{R}^{n}}f(u)\;=\;\inf\_{x\in\operatorname{Int}(\mathcal{C})}\ell(x)\;=\;\inf\_{x\in\mathcal{C}}\ell(x). |  |

Moreover, arg⁡min⁡f≠∅\arg\min f\neq\emptyset if and only if arg⁡min𝒞⁡ℓ\arg\min\_{\mathcal{C}}\ell intersects Int⁡(𝒞)\operatorname{Int}(\mathcal{C}). In that case, u⋆∈arg⁡min⁡fu^{\star}\in\arg\min f if and only if p​(u⋆)∈arg⁡min𝒞⁡ℓp(u^{\star})\in\arg\min\_{\mathcal{C}}\ell.

First-order correspondence. Beyond agreement of optimal values, optimization algorithms require that first-order stationarity of the unconstrained objective f≔ℓ∘pf\coloneqq\ell\circ p be interpretable in terms of first-order conditions for the original constrained problem. Since p​(ℝn)⊂Int⁡(𝒞)p(\mathbb{R}^{n})\subset\operatorname{Int}(\mathcal{C}), the correspondence we establish is necessarily an *interior* one: it relates stationary points of ff to points x∈Int⁡(𝒞)x\in\operatorname{Int}(\mathcal{C}) satisfying ∇ℓ​(x)=0\nabla\ell(x)=0. Boundary minimizers of ℓ\ell over 𝒞\mathcal{C} do not necessarily satisfy ∇ℓ=0\nabla\ell=0 and therefore cannot, in general, be characterized by stationarity of ff. The next statement formalizes the interior correspondence via the chain rule and the fact that JpJ\_{p} is invertible almost everywhere.

{restatable}

propositionCorrStatPoints
(Correspondence of stationary points). Assume ℓ\ell is C1C^{1} on Int⁡(𝒞)\operatorname{Int}(\mathcal{C}). Wherever pp is differentiable, with f=ℓ∘pf=\ell\circ p we have

|  |  |  |
| --- | --- | --- |
|  | ∇f​(u)=Jp​(u)⊤​∇ℓ​(p​(u)).\nabla f(u)\;=\;J\_{p}(u)^{\top}\,\nabla\ell\big(p(u)\big). |  |

Consequently, at any point uu where the Jacobian Jp​(u)J\_{p}(u) is invertible—which holds almost everywhere by Theorem [2.5](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem5 "Definition 2.5 (Scalar projection map). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning")—the stationary conditions are equivalent:

|  |  |  |
| --- | --- | --- |
|  | ∇f​(u)=0⟺∇ℓ​(p​(u))=0.\nabla f(u)=0\quad\Longleftrightarrow\quad\nabla\ell\big(p(u)\big)=0. |  |

This implies that the unconstrained optimization landscape of ff introduces no spurious stationary points within the interior of 𝒞\mathcal{C}.

*Remark.* If a minimizer x⋆x^{\star} of ℓ\ell lies on the boundary ∂𝒞\partial\mathcal{C} and satisfies ∇ℓ​(x⋆)≠0\nabla\ell(x^{\star})\neq 0 (as is typical for constrained optima), Proposition [3](https://arxiv.org/html/2602.03461v1#S3 "3 Optimization Guarantees ‣ Soft-Radial Projection for Constrained End-to-End Learning") implies that there is no stationary point uu corresponding to x⋆x^{\star}. In this case, minimizing sequences for ff must diverge, ‖uk‖→∞\|u\_{k}\|\to\infty, pushing p​(uk)p(u\_{k}) toward the boundary.

Global optimality for convex losses. When ℓ\ell is convex, any *interior* stationary point is globally optimal. Since p​(ℝn)=Int⁡(𝒞)p(\mathbb{R}^{n})=\operatorname{Int}(\mathcal{C}) and Proposition [3](https://arxiv.org/html/2602.03461v1#S3 "3 Optimization Guarantees ‣ Soft-Radial Projection for Constrained End-to-End Learning") shows that, at points where JpJ\_{p} is invertible, stationarity of f=ℓ∘pf=\ell\circ p is equivalent to ∇ℓ=0\nabla\ell=0 at the corresponding interior point, it follows that pp does not introduce spurious interior local minima.

{restatable}

corollaryGlobOptInt
(Global optimality of interior stationary points for convex losses). Assume ℓ\ell is convex and C1C^{1} on Int⁡(𝒞)\operatorname{Int}(\mathcal{C}), and let f≔ℓ∘pf\coloneqq\ell\circ p. If uu is a local minimizer of ff at which pp is differentiable, then p​(u)p(u) is a global minimizer of ℓ\ell over 𝒞\mathcal{C}.

*Remark (Anchor).* At the anchor u0∈Int⁡(𝒞)u\_{0}\in\operatorname{Int}(\mathcal{C}) we have Jp​(u0)=r​(0)​IJ\_{p}(u\_{0})=r(0)I, hence

|  |  |  |
| --- | --- | --- |
|  | ∇(ℓ∘p)⁡(u0)=Jp​(u0)⊤​∇ℓ​(p​(u0))=r​(0)​∇ℓ​(u0).\nabla(\ell\circ p)(u\_{0})=J\_{p}(u\_{0})^{\top}\nabla\ell(p(u\_{0}))=r(0)\,\nabla\ell(u\_{0}). |  |

Thus, the condition r​(0)>0r(0)>0 (cf. Assumption [2.3](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem3 "Assumption 2.3 (Radial monotonicity). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning")) prevents the anchor from becoming an artificial stationary point.

On PL-type conditions. Since the non-linearity of the soft-radial projection pp induces non-convexity in the composite objective f=ℓ∘pf=\ell\circ p, standard global convergence guarantees do not apply directly. A natural question is whether ff satisfies the weaker Polyak–Łojasiewicz (PL) inequality, which would suffice to ensure linear convergence rates. However, even when ℓ\ell is well-conditioned on 𝒞\mathcal{C}, the saturation r​(ρ)→1r(\rho)\to 1 as ρ→∞\rho\to\infty can create regions where ‖∇f‖\|\nabla f\| becomes arbitrarily small while the suboptimality f−f⋆f-f^{\star} stays bounded away from 0, ruling out a global PL bound.
{restatable}lemmaAbsencePL
(Absence of a global PL inequality in general).
Even if 𝒞≔B1​(0)\mathcal{C}\coloneqq B\_{1}(0), ℓ​(x)≔‖x‖2\ell(x)\coloneqq\|x\|^{2} and u0≔0u\_{0}\coloneqq 0, there exists no function rr satisfying Assumption [2.3](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem3 "Assumption 2.3 (Radial monotonicity). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning") such that f=ℓ∘pf=\ell\circ p satisfies a global PL inequality on ℝn\mathbb{R}^{n}.

Gradient methods under bounded iterates. Although a global PL inequality fails in general (Lemma [3](https://arxiv.org/html/2602.03461v1#S3 "3 Optimization Guarantees ‣ Soft-Radial Projection for Constrained End-to-End Learning")), optimization in practice is typically confined to a bounded region, either *by design* (e.g., projected updates, trust regions, gradient clipping/weight decay) or *by stability* of the dynamics. Since the soft-radial projection pp depends on the constraint set 𝒞\mathcal{C} through the radial map qq, global smoothness of pp (and hence of f=ℓ∘pf=\ell\circ p) cannot be taken for granted for arbitrary convex 𝒞\mathcal{C}. We therefore record standard convergence guarantees under the common assumption that the iterates remain in a bounded region. We consider the minimization of the expected objective F​(θ)≔𝔼z​[f​(gθ​(z))]F(\theta)\coloneqq\mathbb{E}\_{z}[f(g\_{\theta}(z))], where f=ℓ∘pf=\ell\circ p, and gθg\_{\theta} is the neural network function parametrized by θ∈Θ\theta\in\Theta.

{restatable}

propositionConvergence(Convergence of stochastic gradient descent). Let F​(θ)≔𝔼z​[ℓ​(p​(gθ​(z)))]F(\theta)\coloneqq\mathbb{E}\_{z}[\ell(p(g\_{\theta}(z)))] with iterates confined to a compact set K⊂ℝpK\subset\mathbb{R}^{p}.

1. 1.

   Smooth Regime: If ℙ\mathbb{P} is absolutely continuous, FF is continuously differentiable and LL-smooth on KK. SGD with step size ηt∝T−1/2\eta\_{t}\propto T^{-1/2} satisfies:

   |  |  |  |
   | --- | --- | --- |
   |  | min0≤t<T⁡𝔼​[‖∇F​(θt)‖2]=𝒪​(T−1/2).\min\_{0\leq t<T}\mathbb{E}[\|\nabla F(\theta\_{t})\|^{2}]=\mathcal{O}(T^{-1/2}). |  |
2. 2.

   Nonsmooth Regime: For general distributions or non-smooth losses, FF is locally Lipschitz. Stochastic Subgradient Descent with diminishing steps ηt→0\eta\_{t}\to 0 converges asymptotically to the set of Clarke stationary points:

   |  |  |  |
   | --- | --- | --- |
   |  | limT→∞𝔼​[minv∈∂F​(θT)⁡‖v‖]=0.\lim\_{T\to\infty}\mathbb{E}\left[\min\_{v\in\partial F(\theta\_{T})}\|v\|\right]=0. |  |

Regularity and proof intuition. The regularity of the objective F​(θ)F(\theta) depends on the interplay between the data distribution and the composite function comprising the network gθg\_{\theta}, the projection pp, and the loss ℓ\ell. We identify the boundary of the feasible set ∂𝒞\partial\mathcal{C} (where pp exhibits kinks, see Thm. [2.5](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem5 "Definition 2.5 (Scalar projection map). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning")) and the activation functions within gθg\_{\theta} as the primary sources of non-differentiability. These points constitute lower-dimensional manifolds in the output space. In the *Smooth Regime*, the absolute continuity of ℙ\mathbb{P} implies that the pre-activations gθ​(z)g\_{\theta}(z) fall on these *kinks* with probability zero. Consequently, the gradient of the expected objective is well-defined almost everywhere, and standard LL-smoothness holds on compact sets. In the *Nonsmooth Regime*, we rely on the fact that pp is locally Lipschitz. Since the composition of locally Lipschitz functions (pp, gθg\_{\theta}, ℓ\ell) preserves this property, the objective admits bounded Clarke subgradients, ensuring the stability of stochastic subgradient updates.

Robustness to degeneracy. A potential concern is the *degenerate* scenario where the network gθg\_{\theta} collapses the data distribution onto the non-differentiable boundary ∂𝒞\partial\mathcal{C}. In this case, the optimization effectively switches to subgradient descent. Unlike orthogonal projections where gradients may vanish (due to rank deficiency), the soft-radial projection maintains strict feasibility and non-zero subgradients at the boundary, providing valid descent directions to recover from such collapse.

## 4 Constrained Universal Approximation

We next demonstrate that the soft-radial projection preserves the expressivity of the underlying model. To establish this, let 𝒵⊂ℝd\mathcal{Z}\subset\mathbb{R}^{d} be a compact input space and consider a class of continuous functions 𝒢≔{gθ:𝒵→ℝn∣θ∈Θ}\mathcal{G}\coloneqq\{g\_{\theta}:\mathcal{Z}\to\mathbb{R}^{n}\mid\theta\in\Theta\}, such as sufficiently deep and wide neural networks (Cybenko, [1989](https://arxiv.org/html/2602.03461v1#bib.bib4 "Approximation by superpositions of a sigmoidal function"); Hornik, [1991](https://arxiv.org/html/2602.03461v1#bib.bib5 "Approximation capabilities of multilayer feedforward networks")). We assume 𝒢\mathcal{G} is a *universal approximator* in the space of continuous functions C​(𝒵,ℝn)C(\mathcal{Z},\mathbb{R}^{n}); that is, for any continuous function ϕ∈C​(𝒵,ℝn)\phi\in C(\mathcal{Z},\mathbb{R}^{n}) and δ>0\delta>0, there exists a function g∈𝒢g\in\mathcal{G} such that

|  |  |  |
| --- | --- | --- |
|  | supz∈𝒵‖g​(z)−ϕ​(z)‖≤δ.\sup\_{z\in\mathcal{Z}}\|g(z)-\phi(z)\|\leq\delta. |  |

With 𝒢\mathcal{G} defined, we aim to show that the constrained model class {p∘g∣g∈𝒢}\{p\circ g\mid g\in\mathcal{G}\} is also a universal approximator for targets in 𝒞\mathcal{C}. A topological nuance here is that pp maps strictly into the *open* interior Int⁡(𝒞)\operatorname{Int}(\mathcal{C}). We must therefore prove that this class can approximate any continuous target h:𝒵→𝒞h:\mathcal{Z}\to\mathcal{C} arbitrarily well, even when the target’s image contains points on the boundary ∂𝒞\partial\mathcal{C}.

Recall from Theorem [2.5](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem5 "Definition 2.5 (Scalar projection map). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning") that the soft-radial projection p:ℝn→Int⁡(𝒞)p:\mathbb{R}^{n}\to\operatorname{Int}(\mathcal{C}) is a homeomorphism.

{restatable}

theoremConstUnvAppr
(Universal approximation on 𝒞\mathcal{C}). Let 𝒵⊂ℝd\mathcal{Z}\subset\mathbb{R}^{d} be compact and let 𝒢\mathcal{G} be a universal approximator on 𝒵\mathcal{Z}. For every continuous function h:𝒵→𝒞h:\mathcal{Z}\to\mathcal{C} and every ε>0\varepsilon>0, there exists a function g∈𝒢g\in\mathcal{G} such that the constrained predictor p∘gp\circ g satisfies

|  |  |  |
| --- | --- | --- |
|  | supz∈𝒵‖p​(g​(z))−h​(z)‖≤ε.\sup\_{z\in\mathcal{Z}}\|\,p(g(z))-h(z)\,\|\;\leq\;\varepsilon. |  |

Proof intuition. The argument proceeds by density and composition. First, the convexity of 𝒞\mathcal{C} ensures that continuous functions mapping to the interior Int⁡(𝒞)\operatorname{Int}(\mathcal{C}) are dense in the space of all feasible continuous functions C​(𝒵,𝒞)C(\mathcal{Z},\mathcal{C}); thus, any target hh admits a uniformly close approximation hεh\_{\varepsilon} that remains strictly interior. Second, because pp is a homeomorphism from ℝn\mathbb{R}^{n} onto Int⁡(𝒞)\operatorname{Int}(\mathcal{C}), there exists a continuous pre-image ϕ:𝒵→ℝn\phi:\mathcal{Z}\to\mathbb{R}^{n} such that p∘ϕ=hεp\circ\phi=h\_{\varepsilon}. The result then follows by applying the universal approximation property of 𝒢\mathcal{G} to approximate this unconstrained function ϕ\phi.

*Remark (Unbounded sets 𝒞\mathcal{C}).* The compactness of the input domain 𝒵\mathcal{Z} is crucial. It ensures that the image h​(𝒵)h(\mathcal{Z}) is bounded even if the feasible set 𝒞\mathcal{C} itself is unbounded. Consequently, the requisite pre-images in ℝn\mathbb{R}^{n} remain within a compact subset, where the uniform approximation bounds of 𝒢\mathcal{G} apply.

Approximation stability.
Finally, we ensure that the error bounds of the base estimator transfer to the constrained model. Let K⊂ℝnK\subset\mathbb{R}^{n} be compact and let LKL\_{K} be a Lipschitz constant of pp on KK. For any continuous function ϕ:𝒵→ℝn\phi:\mathcal{Z}\to\mathbb{R}^{n} and any approximator g∈𝒢g\in\mathcal{G} satisfying ϕ​(𝒵)⊂K\phi(\mathcal{Z})\subset K and g​(𝒵)⊂Kg(\mathcal{Z})\subset K, we have

|  |  |  |
| --- | --- | --- |
|  | supz∈𝒵‖p​(g​(z))−p​(ϕ​(z))‖≤LK​supz∈𝒵‖g​(z)−ϕ​(z)‖.\sup\_{z\in\mathcal{Z}}\|p(g(z))-p(\phi(z))\|\;\leq\;L\_{K}\sup\_{z\in\mathcal{Z}}\|g(z)-\phi(z)\|. |  |

This follows immediately by applying the Lipschitz bound for pp pointwise on KK and taking the supremum over z∈𝒵z\in\mathcal{Z}.

*Implication.* Composition with pp preserves expressivity and transfers uniform approximation guarantees up to a constant factor. Any uniform error bound for the base class 𝒢\mathcal{G} translates to the constrained class p∘𝒢p\circ\mathcal{G}, scaled by the Lipschitz constant LKL\_{K} of the projection.

## 5 Numerical Experiments

While Section [1](https://arxiv.org/html/2602.03461v1#S1 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning") emphasized safety, strict constraints are equally critical in operations where violations are prohibitive. We evaluate our framework on formulation ([2](https://arxiv.org/html/2602.03461v1#S1.E2 "Equation 2 ‣ 1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning")) via portfolio optimization and ride-sharing dispatch; see Appendix [C](https://arxiv.org/html/2602.03461v1#A3 "Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning") for extended experimental details. For our implementation, we treat the projection as a differentiable layer, allowing us to train the model end-to-end by backpropagating gradients directly through the projection operation to the base network gθg\_{\theta}.111Code: <https://anonymous.4open.science/r/soft-radial-projection-e2e-icml/>

### 5.1 Implementation Details

A critical computational advantage of the soft-radial projection is that the ray-boundary intersection scalar, α⋆​(u)\alpha^{\star}(u), often admits an efficient closed-form solution. This contrasts sharply with standard layers based on orthogonal projection (minv∈𝒞⁡‖u−v‖2\min\_{v\in\mathcal{C}}\|u-v\|^{2}). For feasible sets formed by intersecting constraints (such as the capped simplex), orthogonal projection requires solving a constrained quadratic program (QP) for every sample in the batch. These QPs typically lack closed-form solutions, necessitating iterative numerical solvers—such as Dykstra’s algorithm for intersections of convex sets (Dykstra, [1983](https://arxiv.org/html/2602.03461v1#bib.bib42 "An algorithm for restricted least squares regression"); Boyle and Dykstra, [1986](https://arxiv.org/html/2602.03461v1#bib.bib41 "A method for finding projections onto the intersection of convex sets in Hilbert spaces")) or ADMM for splitting complex composite constraints (Boyd et al., [2010](https://arxiv.org/html/2602.03461v1#bib.bib43 "Distributed optimization and statistical learning via the alternating direction method of multipliers"))—that significantly slow down the forward pass. Our method circumvents this bottleneck by replacing the iterative QP with a direct, vectorized calculation.

Choice of radial contraction rr.
Recall from Definition [2.1](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem1 "Definition 2.1 (Soft-Radial Projection). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning") that the radial contraction rr maps the squared distance ρ≔‖u−u0‖2\rho\coloneqq\|u-u\_{0}\|^{2} to a scaling factor in [0,1)[0,1). We parameterize this contraction using smooth sigmoidal mappings satisfying Assumption [2.3](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem3 "Assumption 2.3 (Radial monotonicity). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning"). Fixing parameters ε∈(0,1)\varepsilon\in(0,1) and λ>0\lambda>0, we consider three families:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | (Rational) | r​(ρ)\displaystyle r(\rho) | =ε+(1−ε)​ρρ+λ\displaystyle=\varepsilon+(1-\varepsilon)\frac{\rho}{\rho+\lambda} |  | (3) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | (Exponential) | r​(ρ)\displaystyle r(\rho) | =ε+(1−ε)​(1−e−ρ/λ)\displaystyle=\varepsilon+(1-\varepsilon)\big(1-e^{-\rho/\lambda}\big) |  | (4) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | (Hyperbolic) | r​(ρ)\displaystyle r(\rho) | =ε+(1−ε)​tanh⁡(ρ/λ)\displaystyle=\varepsilon+(1-\varepsilon)\tanh(\rho/\lambda) |  | (5) |

While all three forms guarantee strict interior feasibility, they differ in their asymptotic saturation rate (see Appendix [C.1](https://arxiv.org/html/2602.03461v1#A3.SS1 "C.1 Sensitivity Analysis: Radial Contraction and Scaling ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning")). Note that the term r​(ρ)+2​ρ​r′​(ρ)r(\rho)+2\rho\,r^{\prime}(\rho) remains strictly positive bounded away from zero, ensuring the Jacobian is well-conditioned even at the anchor u0u\_{0}.

Computing the radial map. The evaluation of p​(u)p(u) reduces to computing the scalar α⋆​(u)\alpha^{\star}(u), defined as the distance from the anchor u0u\_{0} to the boundary ∂𝒞\partial\mathcal{C} along the ray (u−u0)(u-u\_{0}).

Case 1: Polyhedra (Linear constraints). For sets defined by linear inequalities A​x≤bAx\leq b (e.g., the simplex or capped simplex), the intersection time is computable exactly without iteration. Since u0u\_{0} is strictly interior (b−A​u0>0b-Au\_{0}>0), the distance to the boundary is the minimum positive intersection time across all hyperplanes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | α⋆​(u)=mini:ai⊤​(u−u0)>0⁡bi−ai⊤​u0ai⊤​(u−u0).\alpha^{\star}(u)\;=\;\min\_{i:\,a\_{i}^{\top}(u-u\_{0})>0}\frac{b\_{i}-a\_{i}^{\top}u\_{0}}{a\_{i}^{\top}(u-u\_{0})}. |  | (6) |

This operation is 𝒪​(m)\mathcal{O}(m) per sample and is fully parallelizable.

Case 2: Euclidean balls. For spherical constraints ‖x−c‖2≤R\|x-c\|\_{2}\leq R, the scalar α⋆​(u)\alpha^{\star}(u) is the unique positive root of the quadratic equation ‖(u0+t​(u−u0))−c‖2=R2\|(u\_{0}+t(u-u\_{0}))-c\|^{2}=R^{2}, which admits a simple analytic solution.

Case 3: General convex sets. For general convex sets defined by level sets h​(x)≤0h(x)\leq 0, finding α⋆\alpha^{\star} is equivalent to finding the root of the scalar function ϕ​(t)=h​(u0+t​(u−u0))\phi(t)=h(u\_{0}+t(u-u\_{0})). Since 𝒞\mathcal{C} is convex, ϕ​(t)\phi(t) is convex and monotonic along the ray. The root can therefore be found to machine precision efficiently using Newton-Raphson or Bisection methods.

Baselines. To provide insights with different neural network architectures, we consider for gθ​(z)g\_{\theta}(z) a multi-layer perceptron (MLP) and a Long Short-Term Memory (LSTM) (Hochreiter and Schmidhuber, [1997](https://arxiv.org/html/2602.03461v1#bib.bib44 "Long short-term memory")) architecture. To benchmark the efficacy of the soft-radial projection, we compare against state-of-the-art constraint enforcement layers (Proj​(gθ​(z))\text{Proj}(g\_{\theta}(z))) across three categories:

* •

  Softmax (Simplex): For standard simplex constraints, we utilize the ubiquitous Softmax function with temperature scaling τ\tau. While computationally cheap, it does not generalize to arbitrary convex sets.
* •

  Orthogonal projection: We compare against the standard Euclidean projection. As discussed in Section [1](https://arxiv.org/html/2602.03461v1#S1 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning"), this method is idempotent—preserving the landscape for already-feasible points—but suffers from gradient saturation when inputs lie outside 𝒞\mathcal{C}.
* •

  Optimization-based layers: We evaluate against *Deep Constraint Completion and Correction* (DC3) (Donti et al., [2021](https://arxiv.org/html/2602.03461v1#bib.bib16 "DC3: A learning method for optimization with hard constraints")), which enforces feasibility via gradient-based corrections, and *HardNet* (Min and Azizan, [2024](https://arxiv.org/html/2602.03461v1#bib.bib9 "HardNet: Hard-constrained neural networks with universal approximation guarantees")), a recent architecture specialized for affine constraints.222App. [C.2](https://arxiv.org/html/2602.03461v1#A3.SS2 "C.2 Adaptation of Competitor Methods to Capped Simplex Constraints ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning") describes the implementation of the respective models for the capped simplex.

### 5.2 Portfolio Optimization

We consider a financial market with NN assets over a finite horizon TT. Let (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) be a probability space equipped with a filtration (ℱt)t≥0(\mathcal{F}\_{t})\_{t\geq 0}. At each time step tt, the agent observes signals ztz\_{t}–comprising raw returns augmented with rolling volatility and correlation to the market proxy computed over lookback HH—and selects a portfolio weight vector wt∈𝒞⊂ℝNw\_{t}\in\mathcal{C}\subset\mathbb{R}^{N}. Between steps t−1t-1 and tt, price relatives yt∈ℝ+Ny\_{t}\in\mathbb{R}^{N}\_{+} induce a passive drift, evolving weights to wt−1+=(diag⁡(yt)​wt−1)/(yt⊤​wt−1)w\_{t-1}^{+}=(\operatorname{diag}(y\_{t})\,w\_{t-1})/(y\_{t}^{\top}w\_{t-1}). The goal is to maximize the Sharpe ratio of the net returns RtnetR^{\text{net}}\_{t}

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝜃𝔼​[Rtnet]Var⁡(Rtnet)s.t.Rtnet=wt−1⊤​yt−γ2​‖wt−wt−1+‖1,∀t,wt=Proj𝒞​(gθ​(zt)),∀t.\begin{array}[]{cl}\displaystyle\underset{\theta}{\text{max}}&\displaystyle\frac{\mathbb{E}[R^{\text{net}}\_{t}]}{\sqrt{\operatorname{Var}(R^{\text{net}}\_{t})}}\\[10.00002pt] \text{s.t.}&\displaystyle R^{\text{net}}\_{t}=w\_{t-1}^{\top}y\_{t}-\frac{\gamma}{2}\|w\_{t}-w\_{t-1}^{+}\|\_{1},\quad\forall t,\\[10.00002pt] &\displaystyle w\_{t}=\text{Proj}\_{\mathcal{C}}(g\_{\theta}(z\_{t})),\quad\forall t.\end{array} |  | (7) |

Here, γ\gamma is the transaction cost parameter and the L1L\_{1} norm captures the turnover cost. As the L1L\_{1} norm is not differentiable at zero, we replace it in the implementation with the Pseudo-Huber loss. We employ the component-wise capped simplex, which generalizes the standard simplex by enforcing asset-specific capacities c∈(N−1,1]Nc\in(N^{-1},1]^{N} to control risk concentration
𝒞={w∈ℝ+N| 1⊤​w=1,w≤c}\mathcal{C}\;=\;\left\{w\in\mathbb{R}^{N}\_{+}\;\middle|\;\mathds{1}^{\top}w=1,\;w\leq c\right\}.

Results analysis. Table [1](https://arxiv.org/html/2602.03461v1#S5.T1 "Table 1 ‣ 5.2 Portfolio Optimization ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning") compares the net Sharpe ratio (SR) and turnover costs utilizing an LSTM architecture within an end-to-end learning framework across different constraint enforcement methods.
On the standard simplex (Δ\Delta), the soft-radial projection demonstrates superior stability, achieving a Sharpe ratio of 0.90​(±0.03)0.90\,(\pm 0.03) and significantly outperforming Softmax (0.630.63). Notably, the standard orthogonal Projection fails to converge to a profitable strategy (0.250.25), yielding high turnover (0.480.48). This suggests that the LSTM struggles to backpropagate effective gradients through the hard projection step, likely due to vanishing gradients at the constraint boundaries.
On the capped simplex (𝒞\mathcal{C}), baseline methods (O-Proj, DC3, HardNet) cluster around a Sharpe ratio of 0.620.62–0.640.64 with higher variance, while the soft-radial projection maintains its performance (0.900.90) with minimal turnover (0.050.05). The reduced standard deviation (±0.02\pm 0.02) indicates that our method is not only more performant but also significantly more robust to initialization than competitive differentiable optimization layers.

Table 1: Portfolio results for Liquid dataset, aggregated over five seeds (mean ±\pm std) with N=50N=50 assets, per-asset capacity c=0.05c=0.05, and transaction cost γ=0.1\gamma=0.1; see App. [C.4](https://arxiv.org/html/2602.03461v1#A3.SS4 "C.4 Extended Analysis: Portfolio Optimization ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning").

|  |  |  |  |
| --- | --- | --- | --- |
| Feasible Set | Method | SR (Net) | Turnover |
| Δ\Delta | Softmax | 0.63​(±0.19)0.63\,(\pm 0.19) | 0.22​(±0.05)0.22\,(\pm 0.05) |
| O-Proj | 0.25​(±0.18)0.25\,(\pm 0.18) | 0.48​(±0.02)0.48\,(\pm 0.02) |
| Soft-Radial | 0.90​(±0.03)0.90\,(\pm 0.03) | 0.06​(±0.00)0.06\,(\pm 0.00) |
| 𝒞\mathcal{C} | O-Proj | 0.64​(±0.09)0.64\,(\pm 0.09) | 0.22​(±0.01)0.22\,(\pm 0.01) |
| DC3 | 0.63​(±0.08)0.63\,(\pm 0.08) | 0.23​(±0.01)0.23\,(\pm 0.01) |
| HardNet | 0.62​(±0.11)0.62\,(\pm 0.11) | 0.19​(±0.01)0.19\,(\pm 0.01) |
| Soft-Radial | 0.90​(±0.02)0.90\,(\pm 0.02) | 0.05​(±0.00)0.05\,(\pm 0.00) |

### 5.3 Ride-Sharing Dispatch

To demonstrate generalizability, we apply our framework to ride-sharing dispatch with a *time-varying budget*. Unlike the fixed portfolio sum, the available fleet size St∈ℕ+S\_{t}\in\mathbb{N}\_{+} fluctuates over time, causing the feasible set 𝒞t\mathcal{C}\_{t} to expand and contract. In practice, such constraints enforce per-zone capacity limits (e.g., congestion or emissions control) Alonso-Mora et al. ([2017](https://arxiv.org/html/2602.03461v1#bib.bib39 "On-demand high-capacity ride-sharing via dynamic trip-vehicle assignment")); Zardini et al. ([2022](https://arxiv.org/html/2602.03461v1#bib.bib40 "Analysis and control of autonomous mobility-on-demand systems")). At each time step tt, the agent observes a demand history window ztz\_{t} (augmented with sine/cosine encodings for day and week) and a current supply proxy StS\_{t}. We seek an allocation at∈ℝ+Na\_{t}\in\mathbb{R}^{N}\_{+} over NN zones to maximize the served rate for the upcoming interval. We optimize the empirical average:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxθ1T​∑t=1T[∑i=1Nminτ⁡(ai,t,di,t)∑i=1Ndi,t]s.t.at=Proj𝒞t​(gθ​(zt)),∀t,\begin{array}[]{cl}\displaystyle\max\_{\theta}&\displaystyle\frac{1}{T}\sum\_{t=1}^{T}\left[\frac{\sum\_{i=1}^{N}\operatorname{min}\_{\tau}(a\_{i,t},d\_{i,t})}{\sum\_{i=1}^{N}d\_{i,t}}\right]\\[15.00002pt] \text{s.t.}&a\_{t}=\text{Proj}\_{\mathcal{C}\_{t}}(g\_{\theta}(z\_{t})),\quad\forall t,\end{array} |  | (8) |

where dtd\_{t} is the realized demand in the interval following the observation window. We replace the hard minimum with the smooth SoftMin, minτ⁡(x,y)=−τ​log⁡(e−x/τ+e−y/τ)\operatorname{min}\_{\tau}(x,y)=-\tau\log(e^{-x/\tau}+e^{-y/\tau}), to maintain non-zero gradients even when supply exceeds demand (ai,t>di,ta\_{i,t}>d\_{i,t}). The constraint set is a scaled capped simplex
𝒞t={a∈ℝ+N| 1⊤​a=St,a≤κ​St}\mathcal{C}\_{t}\!=\!\left\{a\in\mathbb{R}^{N}\_{+}\;\middle|\;\mathds{1}^{\top}a=S\_{t},\;a\leq\kappa S\_{t}\right\}. We implement Proj via a scaling transformation (homothety): the network output is normalized by StS\_{t}, projected onto the canonical unit capped simplex, and subsequently rescaled by StS\_{t}. This effectively maps the dynamic constraint geometry to a fixed reference polytope.

Table 2: Ride-sharing dispatch results, aggregated over five random seeds (mean ±\pm std), for the top N=150N=150 activity zones and zone capacity κ=0.1\kappa=0.1; see App. [C.5](https://arxiv.org/html/2602.03461v1#A3.SS5 "C.5 Extended Analysis: Ride-Sharing Dispatch ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning").

|  |  |  |
| --- | --- | --- |
| Feasible Set | Method | Served Rate |
| Δt\Delta\_{t} | Softmax | 0.84​(±0.00)0.84\,(\pm 0.00) |
| 𝒞t\mathcal{C}\_{t} | O-Proj | 0.70​(±0.01)0.70\,(\pm 0.01) |
| DC3 | 0.84​(±0.00)0.84\,(\pm 0.00) |
| HardNet | 0.84​(±0.00)0.84\,(\pm 0.00) |
| Soft-Radial | 0.84​(±0.00)0.84\,(\pm 0.00) |

Results analysis. Table [2](https://arxiv.org/html/2602.03461v1#S5.T2 "Table 2 ‣ 5.3 Ride-Sharing Dispatch ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning") summarizes the served rate (demand fulfillment) using an MLP policy. Unlike the stochastic portfolio domain, the ride-sharing environment exhibits stable gradient signals, allowing the unconstrained Softmax baseline to reach a high served rate of 0.840.84. In the constrained setting (𝒞t\mathcal{C}\_{t}), we observe a performance saturation: DC3, HardNet, and our proposed soft-radial projection converge to the same solution quality (0.84±0.000.84\pm 0.00). This confirms that the soft-radial projection effectively recovers the optimal feasible policy, matching the performance of specialized differentiable optimization layers. Conversely, the standard orthogonal projection significantly underperforms (0.700.70), again highlighting the detrimental effect of hard boundary constraints on gradient flow during training.

## 6 Conclusion

This paper introduced soft-radial projection to address the gradient saturation inherent in orthogonal projection layers. By constructing a radial homeomorphism to the interior of a convex set, we ensure strict feasibility and model expressivity (Theorem [4](https://arxiv.org/html/2602.03461v1#S4 "4 Constrained Universal Approximation ‣ Soft-Radial Projection for Constrained End-to-End Learning")) without the computational bottleneck of iterative solvers. Empirically, this approach yields superior solution quality compared to optimization-based baselines, effectively balancing theoretical rigor with practical efficiency. These results establish soft-radial projection as a robust, plug-and-play primitive for imposing hard constraints in end-to-end learning.

Limitations. Our framework relies on the convexity of the feasible set to ensure unique radial intersections, preventing immediate application to non-convex manifolds. Additionally, the method requires a known interior anchor point; while straightforward in our tested domains, automating anchor selection for arbitrary high-dimensional sets and analyzing the stability implications of dynamic anchors remain important directions for future work.

## References

* A. Agrawal, B. Amos, S. Barratt, S. Boyd, S. Diamond, and Z. Kolter (2019)
  [Differentiable convex optimization layers](https://papers.nips.cc/paper_files/paper/2019/hash/9ce3c52fc54362e22053399d3181c638-Abstract.html).
  In Advances in Neural Information Processing Systems,
   pp. 9562–9574.
  Cited by: [§A.1](https://arxiv.org/html/2602.03461v1#A1.SS1.p2.1 "A.1 Approximation and Optimization Approaches ‣ Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [§C.2](https://arxiv.org/html/2602.03461v1#A3.SS2.p2.11 "C.2 Adaptation of Competitor Methods to Capped Simplex Constraints ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [§1](https://arxiv.org/html/2602.03461v1#S1.p9.1 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* J. Alonso-Mora, S. Samaranayake, A. Wallar, E. Frazzoli, and D. Rus (2017)
  [On-demand high-capacity ride-sharing via dynamic trip-vehicle assignment](https://doi.org/10.1073/pnas.1611675114).
  Proceedings of the National Academy of Sciences 114 (3),  pp. 462–467.
  Cited by: [§5.3](https://arxiv.org/html/2602.03461v1#S5.SS3.p1.7 "5.3 Ride-Sharing Dispatch ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* B. Amos and J. Z. Kolter (2017)
  [Optnet: Differentiable optimization as a layer in neural networks](https://proceedings.mlr.press/v70/amos17a.html).
  In International Conference on Machine Learning,
   pp. 136–145.
  Cited by: [§A.1](https://arxiv.org/html/2602.03461v1#A1.SS1.p2.1 "A.1 Approximation and Optimization Approaches ‣ Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [§1](https://arxiv.org/html/2602.03461v1#S1.p9.1 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* S. Boyd, N. Parikh, E. Chu, B. Peleato, and J. Eckstein (2010)
  Distributed optimization and statistical learning via the alternating direction method of multipliers.
  Foundations and Trends® in Machine Learning 3 (1),  pp. 1–122.
  Cited by: [§5.1](https://arxiv.org/html/2602.03461v1#S5.SS1.p1.2 "5.1 Implementation Details ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* J. P. Boyle and R. L. Dykstra (1986)
  [A method for finding projections onto the intersection of convex sets in Hilbert spaces](https://doi.org/10.1007/978-1-4613-9940-7_3).
  In Advances in Order Restricted Statistical Inference, R. Dykstra, T. Robertson, and F. T. Wright (Eds.),
  New York, NY,  pp. 28–47.
  Cited by: [§5.1](https://arxiv.org/html/2602.03461v1#S5.SS1.p1.2 "5.1 Implementation Details ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* J. Brodie, I. Daubechies, C. De Mol, D. Giannone, and I. Loris (2009)
  [Sparse and stable Markowitz portfolios](https://doi.org/10.1073/pnas.0904287106).
  Proceedings of the National Academy of Sciences 106 (30),  pp. 12267–12272.
  Cited by: [§C.4.1](https://arxiv.org/html/2602.03461v1#A3.SS4.SSS1.p4.2 "C.4.1 Discussion: Deep Portfolio Optimization vs. Classical Approaches ‣ C.4 Extended Analysis: Portfolio Optimization ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* L.E.J. Brouwer (1912)
  Über Abbildung von Mannigfaltigkeiten.
  Mathematische Annalen 71,  pp. 97–115.
  Cited by: [§B.1](https://arxiv.org/html/2602.03461v1#A2.SS1.10.p4.7 "Proof. ‣ B.1 Proofs of Section 2 ‣ Appendix B Proofs ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* L. Brunke, M. Greeff, A. W. Hall, Z. Yuan, S. Zhou, J. Panerati, and A. P. Schoellig (2022)
  [Safe learning in robotics: From learning-based control to safe reinforcement learning](https://doi.org/10.1146/annurev-control-042920-020211).
  Annual Review of Control, Robotics, and Autonomous Systems 5 (1),  pp. 411–444.
  Cited by: [§1](https://arxiv.org/html/2602.03461v1#S1.p1.1 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* P. Charbonnier, L. Blanc-Feraud, G. Aubert, and M. Barlaud (1994)
  [Two deterministic half-quadratic regularization algorithms for computed imaging](https://doi.org/10.1109/ICIP.1994.413553).
  In International Conference on Image Processing,
  Vol. 2,  pp. 168–172.
  Cited by: [§C.4.3](https://arxiv.org/html/2602.03461v1#A3.SS4.SSS3.p2.2 "C.4.3 Implementation Details ‣ C.4 Extended Analysis: Portfolio Optimization ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* A. R. Chenreddy and E. Delage (2024)
  [End-to-end conditional robust optimization](https://openreview.net/forum?id=Oe9ngGi8Gh).
  In Uncertainty in Artificial Intelligence,
   pp. 736–748.
  Cited by: [§1](https://arxiv.org/html/2602.03461v1#S1.p5.2 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* G. E. Constante-Flores, H. Chen, and C. Li (2025)
  [Enforcing Hard Linear Constraints in Deep Learning Models with Decision Rules](https://openreview.net/forum?id=gjiCml2CNG).
  In Advances in Neural Information Processing Systems,
  Vol. 38.
  Cited by: [Appendix A](https://arxiv.org/html/2602.03461v1#A1.p2.2 "Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* G. Cybenko (1989)
  [Approximation by superpositions of a sigmoidal function](https://doi.org/10.1007/BF02551274).
  Mathematics of Control, Signals and Systems 2 (4),  pp. 303–314.
  Cited by: [§4](https://arxiv.org/html/2602.03461v1#S4.p1.7 "4 Constrained Universal Approximation ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* G. Dalal, K. Dvijotham, M. Vecerik, T. Hester, C. Paduraru, and Y. Tassa (2018)
  Safe exploration in continuous action spaces.
  arXiv preprint arXiv:1801.08757.
  Cited by: [§1](https://arxiv.org/html/2602.03461v1#S1.p9.1 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* D. Davis, D. Drusvyatskiy, S. Kakade, and J. D. Lee (2020)
  [Stochastic subgradient method converges on tame functions](https://doi.org/10.1007/s10208-018-09409-5).
  Foundations of Computational Mathematics 20 (1),  pp. 119–154.
  Cited by: [item 2](https://arxiv.org/html/2602.03461v1#A2.I1.i2.p1.1 "In Regime II: Nonsmooth Optimization. ‣ B.2 Proofs of Section 3 ‣ Appendix B Proofs ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [§B.2](https://arxiv.org/html/2602.03461v1#A2.SS2.SSS0.Px2.p1.1 "Regime II: Nonsmooth Optimization. ‣ B.2 Proofs of Section 3 ‣ Appendix B Proofs ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [§B.2](https://arxiv.org/html/2602.03461v1#A2.SS2.SSS0.Px2.p2.3 "Regime II: Nonsmooth Optimization. ‣ B.2 Proofs of Section 3 ‣ Appendix B Proofs ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* M. H. Davis and A. R. Norman (1990)
  [Portfolio selection with transaction costs](https://doi.org/10.1287/moor.15.4.676).
  Mathematics of Operations Research 15 (4),  pp. 676–713.
  Cited by: [§C.4.1](https://arxiv.org/html/2602.03461v1#A3.SS4.SSS1.p6.1 "C.4.1 Discussion: Deep Portfolio Optimization vs. Classical Approaches ‣ C.4 Extended Analysis: Portfolio Optimization ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* K. Deng, H. Zhang, J. Lu, and H. Sun (2025)
  [HoP: Homeomorphic polar learning for hard constrained optimization](https://arxiv.org/abs/2502.00304).
  arXiv preprint arXiv:2502.00304.
  Cited by: [§A.2](https://arxiv.org/html/2602.03461v1#A1.SS2.p3.1 "A.2 Constructive Geometric Layers ‣ Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [Table 3](https://arxiv.org/html/2602.03461v1#A1.T3.2.2.2.2 "In Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* P. Donti, B. Amos, and J. Z. Kolter (2017)
  [Task-based end-to-end model learning in stochastic optimization](https://papers.nips.cc/paper_files/paper/2017/hash/3fc2c60b5782f641f76bcefc39fb2392-Abstract.html).
  In Advances in Neural Information Processing Systems,
  Vol. 30,  pp. 5490–5500.
  Cited by: [§1](https://arxiv.org/html/2602.03461v1#S1.p5.2 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* P. L. Donti, D. Rolnick, and J. Z. Kolter (2021)
  [DC3: A learning method for optimization with hard constraints](https://openreview.net/forum?id=V1ZHVxJ6dSS).
  In International Conference on Learning Representations,
  Cited by: [§A.1](https://arxiv.org/html/2602.03461v1#A1.SS1.p2.1 "A.1 Approximation and Optimization Approaches ‣ Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [Table 3](https://arxiv.org/html/2602.03461v1#A1.T3.1.1.1.2 "In Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [§C.2](https://arxiv.org/html/2602.03461v1#A3.SS2.SSS0.Px1.p1.5 "Symmetric DC3 for the capped simplex. ‣ C.2 Adaptation of Competitor Methods to Capped Simplex Constraints ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [Appendix C](https://arxiv.org/html/2602.03461v1#A3.p1.2 "Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [§1](https://arxiv.org/html/2602.03461v1#S1.p9.1 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [3rd item](https://arxiv.org/html/2602.03461v1#S5.I1.i3.p1.1 "In 5.1 Implementation Details ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* R. L. Dykstra (1983)
  [An algorithm for restricted least squares regression](https://doi.org/10.2307/2288193).
  Journal of the American Statistical Association 78 (384),  pp. 837–842.
  Cited by: [§5.1](https://arxiv.org/html/2602.03461v1#S5.SS1.p1.2 "5.1 Implementation Details ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* A. N. Elmachtoub and P. Grigas (2022)
  [Smart “predict, then optimize”](https://doi.org/10.1287/mnsc.2020.3922).
  Management Science 68 (1),  pp. 9–26.
  Cited by: [§1](https://arxiv.org/html/2602.03461v1#S1.p5.2 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* H. Federer (1969)
  Geometric measure theory.
  Grundlehren der mathematischen Wissenschaften, Vol. 153, Springer-Verlag, Berlin, Germany.
  Cited by: [§2](https://arxiv.org/html/2602.03461v1#S2.p5.8 "2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* J. Garcıa and F. Fernández (2015)
  [A comprehensive survey on safe reinforcement learning](https://jmlr.org/papers/v16/garcia15a.html).
  Journal of Machine Learning Research 16 (42),  pp. 1437–1480.
  Cited by: [§1](https://arxiv.org/html/2602.03461v1#S1.p9.1 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* S. Ghadimi and G. Lan (2013)
  [Stochastic first-and zeroth-order methods for nonconvex stochastic programming](https://doi.org/10.1137/120880811).
  SIAM Journal on Optimization 23 (4),  pp. 2341–2368.
  Cited by: [§B.2](https://arxiv.org/html/2602.03461v1#A2.SS2.SSS0.Px1.p3.8 "Regime I: Smooth Optimization. ‣ B.2 Proofs of Section 3 ‣ Appendix B Proofs ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* P. D. Grontas, A. Terpin, E. C. Balta, R. D’Andrea, and J. Lygeros (2026)
  [Pinet: Optimizing hard-constrained neural networks with orthogonal projection layers](https://openreview.net/forum?id=EJ680UQeZG).
  In International Conference on Learning Representations,
  Cited by: [Appendix A](https://arxiv.org/html/2602.03461v1#A1.p2.2 "Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* S. Hochreiter and J. Schmidhuber (1997)
  [Long short-term memory](https://doi.org/10.1162/neco.1997.9.8.1735).
  Neural Computation 9 (8),  pp. 1735–1780.
  Cited by: [§5.1](https://arxiv.org/html/2602.03461v1#S5.SS1.p7.2 "5.1 Implementation Details ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* K. Hornik (1991)
  [Approximation capabilities of multilayer feedforward networks](https://doi.org/10.1016/0893-6080(91)90009-T).
  Neural Networks 4 (2),  pp. 251–257.
  Cited by: [§4](https://arxiv.org/html/2602.03461v1#S4.p1.7 "4 Constrained Universal Approximation ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* A. V. Konstantinov and L. V. Utkin (2023)
  [A new computationally simple approach for implementing neural networks with output hard constraints](https://doi.org/10.1134/S1064562423701077).
  In Doklady Mathematics,
  Vol. 108,  pp. S233–S241.
  Cited by: [§A.2](https://arxiv.org/html/2602.03461v1#A1.SS2.p4.4 "A.2 Constructive Geometric Layers ‣ Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [Table 3](https://arxiv.org/html/2602.03461v1#A1.T3.3.3.9.1 "In Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [§1](https://arxiv.org/html/2602.03461v1#S1.p9.1 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* J. Kotary, F. Fioretto, P. Van Hentenryck, and B. Wilder (2021)
  [End-to-end constrained optimization learning: A survey](https://doi.org/10.24963/ijcai.2021/610).
  In International Joint Conference on Artificial Intelligence,
   pp. 4475–4482.
  Note: Survey Track
  Cited by: [§1](https://arxiv.org/html/2602.03461v1#S1.p9.1 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* E. Liang, M. Chen, and S. H. Low (2024)
  [Homeomorphic projection to ensure neural-network solution feasibility for constrained optimization](http://jmlr.org/papers/v25/23-1577.html).
  Journal of Machine Learning Research 25 (329),  pp. 1–55.
  Cited by: [§A.2](https://arxiv.org/html/2602.03461v1#A1.SS2.p3.1 "A.2 Constructive Geometric Layers ‣ Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [Table 3](https://arxiv.org/html/2602.03461v1#A1.T3.3.3.8.1 "In Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [§1](https://arxiv.org/html/2602.03461v1#S1.p9.1 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* H. Markowitz (1952)
  [Portfolio selection](https://doi.org/10.2307/2975974).
  Journal of Finance 7 (1),  pp. 77–91.
  Cited by: [§C.4.1](https://arxiv.org/html/2602.03461v1#A3.SS4.SSS1.p1.1 "C.4.1 Discussion: Deep Portfolio Optimization vs. Classical Approaches ‣ C.4 Extended Analysis: Portfolio Optimization ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* P. Márquez-Neila, M. Salzmann, and P. Fua (2017)
  [Imposing hard constraints on deep networks: Promises and limitations](https://infoscience.epfl.ch/entities/publication/e9a398fa-e422-4472-a028-94c90e25e061).
  arXiv preprint arXiv:1706.02025.
  Note: CVPR 2017 Workshop on Negative Results in Computer Vision
  Cited by: [§A.1](https://arxiv.org/html/2602.03461v1#A1.SS1.p1.1 "A.1 Approximation and Optimization Approaches ‣ Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* R. O. Michaud (1989)
  [The Markowitz optimization enigma: Is ‘optimized’ optimal?](https://doi.org/10.2469/faj.v45.n1.31).
  Financial Analysts Journal 45 (1),  pp. 31–42.
  Cited by: [§C.4.1](https://arxiv.org/html/2602.03461v1#A3.SS4.SSS1.p2.5 "C.4.1 Discussion: Deep Portfolio Optimization vs. Classical Approaches ‣ C.4 Extended Analysis: Portfolio Optimization ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* Y. Min and N. Azizan (2024)
  [HardNet: Hard-constrained neural networks with universal approximation guarantees](https://arxiv.org/abs/2410.10807).
  arXiv preprint arXiv:2410.10807.
  Cited by: [§A.2](https://arxiv.org/html/2602.03461v1#A1.SS2.p2.1 "A.2 Constructive Geometric Layers ‣ Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [Table 3](https://arxiv.org/html/2602.03461v1#A1.T3.3.3.7.1 "In Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [§C.2](https://arxiv.org/html/2602.03461v1#A3.SS2.p2.12 "C.2 Adaptation of Competitor Methods to Capped Simplex Constraints ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [§C.2](https://arxiv.org/html/2602.03461v1#A3.SS2.p2.3 "C.2 Adaptation of Competitor Methods to Capped Simplex Constraints ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [§C.2](https://arxiv.org/html/2602.03461v1#A3.SS2.p2.7 "C.2 Adaptation of Competitor Methods to Capped Simplex Constraints ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [Appendix C](https://arxiv.org/html/2602.03461v1#A3.p1.2 "Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [3rd item](https://arxiv.org/html/2602.03461v1#S5.I1.i3.p1.1 "In 5.1 Implementation Details ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* R. T. Rockafellar and R. J.-B. Wets (2009)
  [Variational Analysis](https://doi.org/10.1007/978-3-642-02431-3).
   Springer.
  Cited by: [§1](https://arxiv.org/html/2602.03461v1#S1.p6.5 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* R. T. Rockafellar (1970)
  Convex Analysis.
   Princeton University Press, Princeton, NJ.
  Cited by: [§B.1](https://arxiv.org/html/2602.03461v1#A2.SS1.13.p3.13 "Proof. ‣ B.1 Proofs of Section 2 ‣ Appendix B Proofs ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [§B.1](https://arxiv.org/html/2602.03461v1#A2.SS1.2.p2.12 "Proof. ‣ B.1 Proofs of Section 2 ‣ Appendix B Proofs ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* Y. Rychener, D. Kuhn, and T. Sutter (2023)
  [End-to-end learning for stochastic optimization: A Bayesian perspective](https://proceedings.mlr.press/v202/rychener23a).
  In International Conference on Machine Learning,
   pp. 29455–29472.
  Cited by: [§1](https://arxiv.org/html/2602.03461v1#S1.p5.2 "1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* J. Tordesillas, J. P. How, and M. Hutter (2023)
  [Rayen: Imposition of hard convex constraints on neural networks](https://arxiv.org/abs/2307.08336).
  arXiv preprint arXiv:2307.08336.
  Cited by: [§A.2](https://arxiv.org/html/2602.03461v1#A1.SS2.p2.1 "A.2 Constructive Geometric Layers ‣ Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning"),
  [Table 3](https://arxiv.org/html/2602.03461v1#A1.T3.3.3.6.1 "In Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* G. Zardini, N. Lanzetti, M. Pavone, and E. Frazzoli (2022)
  [Analysis and control of autonomous mobility-on-demand systems](https://doi.org/10.1146/annurev-control-042920-012811).
  Annual Review of Control, Robotics, and Autonomous Systems 5 (1),  pp. 633–658.
  Cited by: [§5.3](https://arxiv.org/html/2602.03461v1#S5.SS3.p1.7 "5.3 Ride-Sharing Dispatch ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning").
* Z. Zhang, S. Zohren, and S. Roberts (2020)
  [Deep learning for portfolio optimization](https://doi.org/10.3905/jfds.2020.1.042).
  Journal of Financial Data Science 2 (4),  pp. 8–20.
  Cited by: [§C.4.1](https://arxiv.org/html/2602.03461v1#A3.SS4.SSS1.p1.1 "C.4.1 Discussion: Deep Portfolio Optimization vs. Classical Approaches ‣ C.4 Extended Analysis: Portfolio Optimization ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning").

## Appendix A Related Work

Enforcing hard constraints in neural networks is a fundamental challenge in safety-critical learning, requiring architectures that guarantee output feasibility without compromising optimization stability. The literature can be categorized by the mechanism of enforcement—ranging from soft relaxations and iterative solvers to rigorous geometric constructions. Table [3](https://arxiv.org/html/2602.03461v1#A1.T3 "Table 3 ‣ Appendix A Related Work ‣ Soft-Radial Projection for Constrained End-to-End Learning") summarizes the properties of representative state-of-the-art approaches.

Broadly, constraint layers are distinguished by their dependency on the input context. *Input-independent constraints* involve a feasible set 𝒞\mathcal{C} that is fixed across all samples (e.g., static actuator limits or portfolio weights), whereas *input-dependent constraints* involve a dynamic geometry 𝒞​(z)\mathcal{C}(z) conditioned on the input. Our work primarily targets the former, establishing a rigorous geometric framework for fixed convex sets. While strict constraint satisfaction is essential, the quality of the learning signal—specifically the ability of backpropagation to provide informative gradients in high-noise regimes—remains under-explored. Existing approaches prioritize inference speed and feasibility during training and execution. However, the convergence behavior toward the true solution and the ultimate optimality gap are less understood, particularly when the enforcement layer significantly alters the unconstrained network output. While this review is not exhaustive—with ongoing developments ranging from accelerated orthogonal projections Grontas et al. ([2026](https://arxiv.org/html/2602.03461v1#bib.bib54 "Pinet: Optimizing hard-constrained neural networks with orthogonal projection layers")) to the use of decision rules for constraint enforcement Constante-Flores et al. ([2025](https://arxiv.org/html/2602.03461v1#bib.bib53 "Enforcing Hard Linear Constraints in Deep Learning Models with Decision Rules"))—different applications and noise profiles often demand alternatives to standard orthogonal projection to maintain superior optimization properties.

Table 3: Comparison with State-of-the-Art Constraint Layers.
We position Soft-Radial Projection among constructive geometric layers that guarantee feasibility without high-dimensional iterative solvers.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Method | Constraint Scope | Input Dep. | Satisfaction | Computation | Gradient Landscape | Univ. Approx. |
| Soft-Penalty | Any | Yes | No (Penalty) | Closed-Form | Smooth (infeasible) | Yes |
| DC3 Donti et al. ([2021](https://arxiv.org/html/2602.03461v1#bib.bib16 "DC3: A learning method for optimization with hard constraints")) | General | Yes | Approx.⋆ | Iterative (GD) | Step-size sensitive | Unknown |
| RAYEN Tordesillas et al. ([2023](https://arxiv.org/html/2602.03461v1#bib.bib29 "Rayen: Imposition of hard convex constraints on neural networks")) | Convex (Lin/QC/SOC/LMI) | Limited | Strict | Closed-Form | Clipped / Flat | Unknown |
| HardNet-Aff Min and Azizan ([2024](https://arxiv.org/html/2602.03461v1#bib.bib9 "HardNet: Hard-constrained neural networks with universal approximation guarantees")) | Affine | Yes | Strict | Closed-Form | Saturated (Boundary) | Yes |
| HP Liang et al. ([2024](https://arxiv.org/html/2602.03461v1#bib.bib7 "Homeomorphic projection to ensure neural-network solution feasibility for constrained optimization")) | Ball-Homeomorphic | Yes | Strict | Bisection | Iterative search | Yes |
| HoP (Polar) Deng et al. ([2025](https://arxiv.org/html/2602.03461v1#bib.bib8 "HoP: Homeomorphic polar learning for hard constrained optimization")) | Star-Convex | Yes | Strict (Int.) | Closed-Form† | Polar stagnation | Unknown |
| RP Konstantinov and Utkin ([2023](https://arxiv.org/html/2602.03461v1#bib.bib3 "A new computationally simple approach for implementing neural networks with output hard constraints")) | Convex (Lin/Quad) | Limited | Strict (Int.) | Closed-Form | Smooth (Saturating) | Unknown |
| \rowcolorgray!10 Soft-Radial (Ours) | Convex | No‡ | Strict (Int.) | C.-F. / 1D Root | Full-rank Jacobian a.e. | Yes |

⋆Asymptotic (linear constraints); heuristic/approximate otherwise; truncated correction in practice.
  
†HoP requires a per-sample interior anchor and a ray–boundary intersection query.
  
‡Current focus is on fixed sets 𝒞\mathcal{C}, though formulation supports dynamic anchors.

### A.1 Approximation and Optimization Approaches

Soft Penalties and Activations.
The most straightforward approach, favored by many industry practitioners, relaxes strict constraints into the training objective. Penalty-based methods augment the loss function with a regularization term proportional to the magnitude of constraint violations Márquez-Neila et al. ([2017](https://arxiv.org/html/2602.03461v1#bib.bib50 "Imposing hard constraints on deep networks: Promises and limitations")). While this preserves the smoothness of the optimization landscape, it fundamentally fails to guarantee feasibility during inference, particularly in high-dimensional spaces where the volume of the feasible set relative to the ambient space can become negligible. Similarly, standard activation functions (e.g., Sigmoid, Softmax) offer computationally efficient bounds for elementary box or simplex constraints but lack the topological expressivity to model complex coupled constraints or polyhedral boundaries.

Differentiable Optimization and Iterative Correction. To ensure strict satisfaction, a second family of methods embeds optimization solvers directly into the network architecture. Differentiable optimization layers, such as OptNet Amos and Kolter ([2017](https://arxiv.org/html/2602.03461v1#bib.bib30 "Optnet: Differentiable optimization as a layer in neural networks")) and CVXPYLayers Agrawal et al. ([2019](https://arxiv.org/html/2602.03461v1#bib.bib18 "Differentiable convex optimization layers")), compute the orthogonal projection of a prediction onto 𝒞\mathcal{C} by solving a convex program during the forward pass. DC3 Donti et al. ([2021](https://arxiv.org/html/2602.03461v1#bib.bib16 "DC3: A learning method for optimization with hard constraints")) instead utilizes a *completion–correction* scheme, where equality constraints are satisfied via variable completion and inequality violations are reduced through iterative gradient-based correction. While mathematically general, these approaches introduce significant computational overhead. Furthermore, backpropagating through these layers typically relies on implicit differentiation, which assumes the inner solver has reached a stationary point. When truncated for real-time efficiency (e.g., fixed-iteration limits), this assumption is violated, leading to conflict-prone gradient updates where the descent direction of the task loss contradicts the incomplete constraint correction.

### A.2 Constructive Geometric Layers

To circumvent the computational cost of iterative solvers, recent research focuses on “Feasibility by Construction” via closed-form surjective mappings Proj:ℝn→𝒞\text{Proj}:\mathbb{R}^{n}\to\mathcal{C}. We classify these geometric approaches into three distinct families:

Gauge and Boundary Projections.
RAYEN Tordesillas et al. ([2023](https://arxiv.org/html/2602.03461v1#bib.bib29 "Rayen: Imposition of hard convex constraints on neural networks")) enforces convex constraints by selecting a fixed interior point and *rescaling* a predicted direction so that the endpoint remains feasible; the mapping is identity when the step stays inside the set, and otherwise returns the first ray–boundary intersection. HardNet-Aff Min and Azizan ([2024](https://arxiv.org/html/2602.03461v1#bib.bib9 "HardNet: Hard-constrained neural networks with universal approximation guarantees")) targets *input-dependent affine* inequalities via a closed-form pseudoinverse-based correction that clamps violated constraints to their bounds while moving in directions parallel to already-satisfied constraint boundaries. While both layers are computationally efficient, their piecewise ray/clamping structure can suppress learning signals when constraints are active (e.g., RAYEN becomes insensitive to step magnitude after rescaling, and HardNet-Aff can attenuate gradient components in constraint-normal directions). This suppression can bias training toward boundary-feasible outputs and reduce interior exploration.

Topological Diffeomorphisms.
To utilize the set’s interior, topological methods reshape the output space. Homeomorphic Projection (HP) Liang et al. ([2024](https://arxiv.org/html/2602.03461v1#bib.bib7 "Homeomorphic projection to ensure neural-network solution feasibility for constrained optimization")) learns a bi-Lipschitz *invertible neural network* (INN) that approximates a minimum-distortion homeomorphism between the constraint set and a unit ball. At inference, HP maps an infeasible prediction into the ball via the INN inverse and then performs a kk-step bisection along the ray to the ball center, requiring repeated INN forward evaluations and feasibility checks; the resulting boundary-feasible point trades computation for accuracy through the bisection depth and depends on the learned mapping distortion.
Polar coordinate methods like HoP Deng et al. ([2025](https://arxiv.org/html/2602.03461v1#bib.bib8 "HoP: Homeomorphic polar learning for hard constrained optimization")) attempt an analytic solution but introduce polar stagnation, singularities at the origin where angular components are undefined, resulting in numerical instability near the geometric center.

Radial Interior Mappings.
Closely related to our work, Konstantinov and Utkin ([2023](https://arxiv.org/html/2602.03461v1#bib.bib3 "A new computationally simple approach for implementing neural networks with output hard constraints")) propose a “ray-projection” layer that constructs feasible points by scaling a direction vector rr from an interior anchor. While effective, this requires a specialized architecture that learns separate polar coordinates (g​(r,s)g(r,s)) rather than a direct map of the ambient Euclidean space. Furthermore, these constructions typically do not furnish a global bijection between ℝn\mathbb{R}^{n} and Int⁡(𝒞)\operatorname{Int}(\mathcal{C}), potentially resulting in saturating radial behavior due to the choice of bounded scaling functions (e.g., sigmoids).

Our Contribution: Soft-Radial Projection. We propose a drop-in reparameterization layer for fixed closed convex sets with a non-empty interior. Our mapping acts directly on the unconstrained ambient prediction u∈ℝnu\in\mathbb{R}^{n} as a unified radial homeomorphism ℝn→Int⁡(𝒞)\mathbb{R}^{n}\to\operatorname{Int}(\mathcal{C}). For standard convex geometries—such as balls, ellipsoids, and boxes—the mapping admits a closed-form solution. For general convex sets, we utilize an efficient monotonic 1D root-finding procedure. Crucially, we ensure the mapping is differentiable with an invertible Jacobian almost everywhere, preventing the rank-collapse characteristic of boundary projections. This ensures the learning signal remains non-vanishing even for predictions far outside the feasible set, while preserving the Universal Approximation property of the base network (Theorem [4](https://arxiv.org/html/2602.03461v1#S4 "4 Constrained Universal Approximation ‣ Soft-Radial Projection for Constrained End-to-End Learning")).

## Appendix B Proofs

In the following sections, we provide complete proofs for the theoretical results. To facilitate readability, we restate each claim prior to its proof.

### B.1 Proofs of Section [2](https://arxiv.org/html/2602.03461v1#S2 "2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning")

We begin by establishing the regularity of the individual projection components.

\RayRegularity

\*

###### Proof.

*Ray feasibility and intersection.* Fix u∈ℝnu\in\mathbb{R}^{n} and consider scalars α∈[0,1]\alpha\in[0,1] such that α​u∈𝒞\alpha u\in\mathcal{C}. The map α↦α​u\alpha\mapsto\alpha u is continuous and 𝒞\mathcal{C} is closed, so the set of feasible α∈[0,1]\alpha\in[0,1] is closed in [0,1][0,1] and nonempty (since α=0\alpha=0 is always feasible). Convexity of 𝒞\mathcal{C} implies this set is convex in ℝ\mathbb{R}, and any nonempty closed convex subset of ℝ\mathbb{R} is an interval; hence it is of the form [0,α⋆​(u)][0,\alpha^{\star}(u)] for a unique α⋆​(u)∈[0,1]\alpha^{\star}(u)\in[0,1].

*Global Lipschitz continuity of α\alpha.* Let γ𝒞:ℝn→[0,∞)\gamma\_{\mathcal{C}}:\mathbb{R}^{n}\to[0,\infty) denote the Minkowski functional (gauge) of 𝒞\mathcal{C},

|  |  |  |
| --- | --- | --- |
|  | γ𝒞​(x)≔inf{t>0:x∈t​𝒞}.\gamma\_{\mathcal{C}}(x)\coloneqq\inf\{t>0:x\in t\mathcal{C}\}. |  |

Standard properties of the gauge (see, e.g., Rockafellar ([1970](https://arxiv.org/html/2602.03461v1#bib.bib25 "Convex Analysis")), Thm. 14.5 and Chap. 13) imply that γ𝒞\gamma\_{\mathcal{C}} is sublinear (convex and positively homogeneous) and finite on ℝn\mathbb{R}^{n} when 0∈Int⁡(𝒞)0\in\operatorname{Int}(\mathcal{C}). Because 0∈Int⁡(𝒞)0\in\operatorname{Int}(\mathcal{C}), there exists δ>0\delta>0 with B​(0,δ)⊂𝒞B(0,\delta)\subset\mathcal{C}, which yields γ𝒞​(x)≤‖x‖/δ\gamma\_{\mathcal{C}}(x)\leq\|x\|/\delta for all xx and, by subadditivity of γ𝒞\gamma\_{\mathcal{C}},

|  |  |  |
| --- | --- | --- |
|  | γ𝒞​(x)−γ𝒞​(y)≤γ𝒞​(x−y)≤‖x−y‖δ∀x,y∈ℝn,\gamma\_{\mathcal{C}}(x)-\gamma\_{\mathcal{C}}(y)\leq\gamma\_{\mathcal{C}}(x-y)\leq\frac{\|x-y\|}{\delta}\quad\forall\;x,y\in\mathbb{R}^{n}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | γ𝒞​(y)−γ𝒞​(x)≤γ𝒞​(y−x)≤‖y−x‖δ∀x,y∈ℝn.\gamma\_{\mathcal{C}}(y)-\gamma\_{\mathcal{C}}(x)\leq\gamma\_{\mathcal{C}}(y-x)\leq\frac{\|y-x\|}{\delta}\quad\forall\;x,y\in\mathbb{R}^{n}. |  |

Taking the maximum of the two inequalities shows

|  |  |  |
| --- | --- | --- |
|  | |γ𝒞​(x)−γ𝒞​(y)|≤‖x−y‖δ∀x,y∈ℝn,|\gamma\_{\mathcal{C}}(x)-\gamma\_{\mathcal{C}}(y)|\leq\frac{\|x-y\|}{\delta}\quad\forall\;x,y\in\mathbb{R}^{n}, |  |

so γ𝒞\gamma\_{\mathcal{C}} is Lipschitz with constant 1/δ1/\delta.

For u≠0u\neq 0, the feasibility of α​u∈𝒞\alpha u\in\mathcal{C} is equivalent to α≤1/γ𝒞​(u)\alpha\leq 1/\gamma\_{\mathcal{C}}(u). Therefore, the feasible α∈[0,1]\alpha\in[0,1] form the interval [0,min⁡{1,1/γ𝒞​(u)}][0,\min\{1,1/\gamma\_{\mathcal{C}}(u)\}], implying that α⋆​(u)=min⁡(1,1/γ𝒞​(u))\alpha^{\star}(u)=\min\bigl(1,1/\gamma\_{\mathcal{C}}(u)\bigr), for u≠0u\neq 0, while for u=0u=0 we clearly have α⋆​(u)=1\alpha^{\star}(u)=1. Define a helper function ψ:[0,∞)→(0,1]\psi:[0,\infty)\to(0,1] by ψ​(t)≔min⁡(1,1/t)\psi(t)\coloneqq\min(1,1/t) for t>0t>0 and ψ​(0)≔1\psi(0)\coloneqq 1. The function ψ\psi is 11–Lipschitz on [0,∞)[0,\infty), so for all u,v∈ℝnu,v\in\mathbb{R}^{n},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |α⋆​(u)−α⋆​(v)|\displaystyle|\alpha^{\star}(u)-\alpha^{\star}(v)| | =|ψ​(γ𝒞​(u))−ψ​(γ𝒞​(v))|\displaystyle=|\psi(\gamma\_{\mathcal{C}}(u))-\psi(\gamma\_{\mathcal{C}}(v))| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤|γ𝒞​(u)−γ𝒞​(v)|≤‖u−v‖δ.\displaystyle\leq|\gamma\_{\mathcal{C}}(u)-\gamma\_{\mathcal{C}}(v)|\leq\frac{\|u-v\|}{\delta}. |  |

Thus α⋆\alpha^{\star} is globally Lipschitz with constant 1/δ1/\delta.

*Local Lipschitz continuity of qq.* We now bound the variation of q​(u)=α⋆​(u)​uq(u)=\alpha^{\star}(u)u on bounded sets. Let R>0R>0 and assume ‖v‖≤R\|v\|\leq R and ‖u‖≤R\|u\|\leq R.
Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖q​(u)−q​(v)‖\displaystyle\|q(u)-q(v)\| | =‖α⋆​(u)​u−α⋆​(v)​v‖\displaystyle=\|\alpha^{\star}(u)u-\alpha^{\star}(v)v\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖α⋆​(u)​(u−v)‖+‖v​(α⋆​(u)−α⋆​(v))‖\displaystyle\leq\|\alpha^{\star}(u)(u-v)\|+\|v(\alpha^{\star}(u)-\alpha^{\star}(v))\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖u−v‖+‖v‖⋅|α⋆​(u)−α⋆​(v)|\displaystyle\leq\|u-v\|+\|v\|\cdot|\alpha^{\star}(u)-\alpha^{\star}(v)| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖u−v‖+‖v‖δ​‖u−v‖\displaystyle\leq\|u-v\|+\frac{\|v\|}{\delta}\,\|u-v\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(1+Rδ)​‖u−v‖.\displaystyle\leq\Bigl(1+\frac{R}{\delta}\Bigr)\|u-v\|. |  |

Hence qq is (1+R/δ)(1+R/\delta)–Lipschitz on the ball {u:‖u‖≤R}\{u:\|u\|\leq R\}, which implies that qq is locally Lipschitz on ℝn\mathbb{R}^{n}, completing the proof.
∎

Next, we analyze the structural properties of the constructed projection map.

\RegComponents

\*

###### Proof.

*Continuity of t¯\bar{t}.* We relate t¯​(v)\bar{t}(v) to the Minkowski functional (gauge) γ𝒞\gamma\_{\mathcal{C}}. By definition, t¯​(v)=1/γ𝒞​(v)\bar{t}(v)=1/\gamma\_{\mathcal{C}}(v) (with the convention 1/0=∞1/0=\infty). Since γ𝒞\gamma\_{\mathcal{C}} is continuous on ℝn\mathbb{R}^{n} (Lemma [2](https://arxiv.org/html/2602.03461v1#S2.F2 "Figure 2 ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning")) and the inversion map is continuous on [0,∞)[0,\infty) into (0,∞](0,\infty], the composition v↦t¯​(v)v\mapsto\bar{t}(v) is continuous on the unit sphere.

*Properties of ψv\psi\_{v}.* For t≤t¯​(v)t\leq\bar{t}(v), we have ψv​(t)=r​(t2)​t\psi\_{v}(t)=r(t^{2})t. Strict monotonicity on this interval was established immediately following Assumption [2.3](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem3 "Assumption 2.3 (Radial monotonicity). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning"). For t>t¯​(v)t>\bar{t}(v) (which implies t¯​(v)<∞\bar{t}(v)<\infty), we have ψv​(t)=r​(t2)​t¯​(v)\psi\_{v}(t)=r(t^{2})\bar{t}(v), which is strictly increasing simply because rr is increasing. Continuity holds at t=t¯​(v)t=\bar{t}(v) as both expressions coincide. Finally, since ψv​(0)=0\psi\_{v}(0)=0 and limt→∞ψv​(t)=t¯​(v)\lim\_{t\to\infty}\psi\_{v}(t)=\bar{t}(v), the range is exactly [0,t¯​(v))[0,\bar{t}(v)).
∎

Building on these established properties, we prove that pp is indeed a homeomorphism.

\Homeomorphism

\*

###### Proof.

We first establish that pp is a bijection.

*Injectivity.* Let u1,u2∈ℝnu\_{1},u\_{2}\in\mathbb{R}^{n} with p​(u1)=p​(u2)p(u\_{1})=p(u\_{2}). Since pp preserves directions (i.e., p​(u)∈ℝ+​up(u)\in\mathbb{R}\_{+}u), u1u\_{1} and u2u\_{2} must lie on the same ray, so ui=ti​vu\_{i}=t\_{i}v for some unit vector vv and ti≥0t\_{i}\geq 0.The scalar map ψv\psi\_{v} from Definition [2.5](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem5 "Definition 2.5 (Scalar projection map). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning") satisfies p​(ti​v)=ψv​(ti)​vp(t\_{i}v)=\psi\_{v}(t\_{i})v. By Lemma [2.5](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem5 "Definition 2.5 (Scalar projection map). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning"), ψv\psi\_{v} is strictly increasing, so ψv​(t1)=ψv​(t2)\psi\_{v}(t\_{1})=\psi\_{v}(t\_{2}) implies t1=t2t\_{1}=t\_{2}, and hence u1=u2u\_{1}=u\_{2}.

*Surjectivity.* Let x∈Int⁡(𝒞)x\in\operatorname{Int}(\mathcal{C}). If x=0x=0, x=p​(0)x=p(0). If x≠0x\neq 0, set v=x/‖x‖v=x/\|x\| and s=‖x‖s=\|x\|. Since x∈Int⁡(𝒞)x\in\operatorname{Int}(\mathcal{C}), we strictly have s<t¯​(v)s<\bar{t}(v). By Lemma [2.5](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem5 "Definition 2.5 (Scalar projection map). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning"), the continuous scalar map ψv\psi\_{v} has range [0,t¯​(v))[0,\bar{t}(v)). By the Intermediate Value Theorem, there exists a unique tt such that ψv​(t)=s\psi\_{v}(t)=s, yielding p​(t​v)=xp(tv)=x. Moreover, pp is continuous on ℝn\mathbb{R}^{n} as it is composed of the continuous scaling function rr (Assumption [2.3](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem3 "Assumption 2.3 (Radial monotonicity). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning")) and the continuous hard radial projection qq (Lemma [2](https://arxiv.org/html/2602.03461v1#S2.F2 "Figure 2 ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning")). Thus, pp is a continuous bijection from ℝn\mathbb{R}^{n} onto Int⁡(𝒞)\operatorname{Int}(\mathcal{C}).

*Continuity of Inverse.* Since pp is a continuous injection from ℝn\mathbb{R}^{n} into an open subset ℝn\mathbb{R}^{n}, the Invariance of Domain theorem Brouwer ([1912](https://arxiv.org/html/2602.03461v1#bib.bib33 "Über Abbildung von Mannigfaltigkeiten")) guarantees that pp is an open map. Because pp is a continuous bijection that maps open sets to open sets, it is a homeomorphism between ℝn\mathbb{R}^{n} and its image Int⁡(𝒞)\operatorname{Int}(\mathcal{C}).
∎

Finally, we analyze the differentiability of pp, establishing that it is a diffeomorphism almost everywhere.

\DiffInvert

\*

###### Proof.

By Lemma [2](https://arxiv.org/html/2602.03461v1#S2.F2 "Figure 2 ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning"), qq is locally Lipschitz and therefore differentiable almost everywhere by Rademacher’s theorem. Since rr is C1C^{1}, the product p​(u)=r​(‖u‖2)​q​(u)p(u)=r(\|u\|^{2})q(u) shares the same domain of differentiability. Whenever Jp​(u)J\_{p}(u) exists, the product rule gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jp​(u)=r​(‖u‖2)​Jq​(u)+ 2​r′​(‖u‖2)​q​(u)​u⊤.J\_{p}(u)\;=\;r(\|u\|^{2})\,J\_{q}(u)\;+\;2\,r^{\prime}(\|u\|^{2})\,q(u)\,u^{\top}. |  | (9) |

We analyze the invertibility of this Jacobian in two cases based on the position of uu relative to 𝒞\mathcal{C}. Note that pp is generally not differentiable for u∈∂𝒞u\in\partial\mathcal{C} because the map α⋆​(u)\alpha^{\star}(u) (and thus qq) typically exhibits a kink at the boundary where the active regime switches.

*Interior points.* For u∈Int⁡(𝒞)u\in\operatorname{Int}(\mathcal{C}) we have q​(u)=uq(u)=u and Jq​(u)=IJ\_{q}(u)=I, hence

|  |  |  |
| --- | --- | --- |
|  | Jp​(u)=r​(‖u‖2)​I+2​r′​(‖u‖2)​u​u⊤.J\_{p}(u)=r(\|u\|^{2})\,I+2\,r^{\prime}(\|u\|^{2})\,uu^{\top}. |  |

For u≠0u\neq 0, this matrix has eigenvector u/‖u‖u/\|u\|, with corresponding eigenvalue r​(‖u‖2)+2​‖u‖2​r′​(‖u‖2)r(\|u\|^{2})+2\,\|u\|^{2}\,r^{\prime}(\|u\|^{2}) and all vectors orthogonal to uu are eigenvectors with eigenvalue r​(‖u‖2)r(\|u\|^{2}). Assumption [2.3](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem3 "Assumption 2.3 (Radial monotonicity). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning") gives r​(ρ)>0r(\rho)>0 and r​(ρ)+2​ρ​r′​(ρ)>0r(\rho)+2\rho\,r^{\prime}(\rho)>0 for all ρ≥0\rho\geq 0, so Jp​(u)≻0J\_{p}(u)\succ 0 is invertible for all u∈Int⁡(𝒞)∖{0}u\in\operatorname{Int}(\mathcal{C})\setminus\{0\}. At the origin, qq coincides with the identity in a neighborhood of 0 (because 0∈Int⁡(𝒞)0\in\operatorname{Int}(\mathcal{C})), so Jq​(0)=IJ\_{q}(0)=I and the rank-one term vanishes, giving Jp​(0)=r​(0)​IJ\_{p}(0)=r(0)\,I, which is invertible since r​(0)>0r(0)>0.

*Exterior points.* For points outside the interior (u∉Int⁡(𝒞)u\notin\operatorname{Int}(\mathcal{C})), q​(u)q(u) lies on the boundary ∂𝒞\partial\mathcal{C}. Using the gauge γ𝒞\gamma\_{\mathcal{C}} of 𝒞\mathcal{C} (the Minkowski functional), the condition u∉Int⁡(𝒞)u\notin\operatorname{Int}(\mathcal{C}) implies γ𝒞​(u)≥1\gamma\_{\mathcal{C}}(u)\geq 1, and the hard radial projection is given by q​(u)=u/γ𝒞​(u)q(u)=u/\gamma\_{\mathcal{C}}(u). Now fix a point uu where γ𝒞\gamma\_{\mathcal{C}} is differentiable (which holds almost everywhere by standard results on convex functions, see, e.g., Rockafellar ([1970](https://arxiv.org/html/2602.03461v1#bib.bib25 "Convex Analysis")), §25). To simplify notation, let λ≔γ𝒞​(u)≥1\lambda\coloneqq\gamma\_{\mathcal{C}}(u)\geq 1. Differentiating q​(u)q(u) with respect to uu yields the Jacobian

|  |  |  |
| --- | --- | --- |
|  | Jq​(u)=1λ​I−1λ2​u​∇γ𝒞​(u)⊤.J\_{q}(u)\;=\;\frac{1}{\lambda}I-\frac{1}{\lambda^{2}}\,u\,\nabla\gamma\_{\mathcal{C}}(u)^{\top}. |  |

We establish that Jp​(u)J\_{p}(u) is invertible by showing its kernel is trivial. Let h∈ℝnh\in\mathbb{R}^{n} satisfy Jp​(u)​h=0J\_{p}(u)h=0. We decompose hh with respect to the subspace W={w∈ℝn∣u⊤​w=0}W=\{w\in\mathbb{R}^{n}\mid u^{\top}w=0\}. Any hh can be uniquely written as h=hW+β​uh=h\_{W}+\beta u, where hW∈Wh\_{W}\in W and β∈ℝ\beta\in\mathbb{R}.

First, we compute the product of Jq​(u)J\_{q}(u) with the radial component. Since γ𝒞\gamma\_{\mathcal{C}} is positively homogeneous of degree 1 by definition, Euler’s homogeneous function theorem implies ∇γ𝒞​(u)⊤​u=γ𝒞​(u)=λ\nabla\gamma\_{\mathcal{C}}(u)^{\top}u=\gamma\_{\mathcal{C}}(u)=\lambda. Using this relation, we find

|  |  |  |
| --- | --- | --- |
|  | Jq​(u)​u=1λ​u−1λ2​u​(∇γ𝒞​(u)⊤​u)⏟λ=1λ​u−1λ​u= 0.J\_{q}(u)u\;=\;\frac{1}{\lambda}u-\frac{1}{\lambda^{2}}u\underbrace{(\nabla\gamma\_{\mathcal{C}}(u)^{\top}u)}\_{\lambda}\;=\;\frac{1}{\lambda}u-\frac{1}{\lambda}u\;=\;0. |  |

For the orthogonal component hWh\_{W}, we have

|  |  |  |
| --- | --- | --- |
|  | Jq​(u)​hW=1λ​hW−∇γ𝒞​(u)⊤​hWλ2​u.J\_{q}(u)h\_{W}\;=\;\frac{1}{\lambda}h\_{W}-\frac{\nabla\gamma\_{\mathcal{C}}(u)^{\top}h\_{W}}{\lambda^{2}}u. |  |

Substituting h=hW+β​uh=h\_{W}+\beta u and the expression for Jp​(u)J\_{p}(u) ([9](https://arxiv.org/html/2602.03461v1#A2.E9 "Equation 9 ‣ Proof. ‣ B.1 Proofs of Section 2 ‣ Appendix B Proofs ‣ Soft-Radial Projection for Constrained End-to-End Learning")) into the condition Jp​(u)​h=0J\_{p}(u)h=0 yields

|  |  |  |
| --- | --- | --- |
|  | r​(‖u‖2)​Jq​(u)​hW+2​β​‖u‖2​r′​(‖u‖2)​q​(u)= 0.r(\|u\|^{2})J\_{q}(u)h\_{W}+2\beta\|u\|^{2}r^{\prime}(\|u\|^{2})q(u)\;=\;0. |  |

Substituting the expansion of Jq​(u)​hWJ\_{q}(u)h\_{W} allows us to group terms proportional to uu. The equation becomes

|  |  |  |
| --- | --- | --- |
|  | r​(‖u‖2)λ​hW+μ​u=0,\frac{r(\|u\|^{2})}{\lambda}h\_{W}\;+\;\mu u=0, |  |

where μ∈ℝ\mu\in\mathbb{R} captures all radial coefficients:

|  |  |  |
| --- | --- | --- |
|  | μ=2​β​‖u‖2​r′​(‖u‖2)​1λ−r​(‖u‖2)​∇γ𝒞​(u)⊤​hWλ2.\mu=2\beta\|u\|^{2}r^{\prime}(\|u\|^{2})\frac{1}{\lambda}-\frac{r(\|u\|^{2})\nabla\gamma\_{\mathcal{C}}(u)^{\top}h\_{W}}{\lambda^{2}}. |  |

Projecting the vector equation onto the subspace WW eliminates μ​u\mu u, yielding

|  |  |  |
| --- | --- | --- |
|  | r​(‖u‖2)λ​hW=0.\frac{r(\|u\|^{2})}{\lambda}h\_{W}=0. |  |

Since r>0r>0 and λ≥1\lambda\geq 1, we must have hW=0h\_{W}=0. Consequently, the radial term must also vanish, so μ​u=0\mu u=0, implying μ=0\mu=0. With hW=0h\_{W}=0, the expression for μ\mu simplifies to

|  |  |  |
| --- | --- | --- |
|  | 2​β​‖u‖2​r′​(‖u‖2)​1λ=0.2\beta\|u\|^{2}r^{\prime}(\|u\|^{2})\frac{1}{\lambda}=0. |  |

Assumption [2.3](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem3 "Assumption 2.3 (Radial monotonicity). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning") ensures r′​(ρ)>0r^{\prime}(\rho)>0 for ρ>0\rho>0, so we must have β=0\beta=0. Thus h=0h=0, proving that Jp​(u)J\_{p}(u) is invertible. Combining the results for interior and exterior points, we conclude that pp is differentiable almost everywhere and Jp​(u)J\_{p}(u) is invertible wherever it exists.
∎

### B.2 Proofs of Section [3](https://arxiv.org/html/2602.03461v1#S3 "3 Optimization Guarantees ‣ Soft-Radial Projection for Constrained End-to-End Learning")

We begin by establishing the equivalence of the optimal values between the unconstrained composite optimization f​(u)f(u) and the constrained optimization objective.

\EquivOptVal

\*

###### Proof.

By bijectivity of p:ℝn→Int⁡(𝒞)p:\mathbb{R}^{n}\to\operatorname{Int}(\mathcal{C}),

|  |  |  |
| --- | --- | --- |
|  | infu∈ℝnf​(u)=infx∈Int⁡(𝒞)ℓ​(x).\inf\_{u\in\mathbb{R}^{n}}f(u)=\inf\_{x\in\operatorname{Int}(\mathcal{C})}\ell(x). |  |

Since u0∈Int⁡(𝒞)u\_{0}\in\operatorname{Int}(\mathcal{C}) and 𝒞\mathcal{C} is convex, for any x∈𝒞x\in\mathcal{C} and ε∈(0,1]\varepsilon\in(0,1],
xε≔(1−ε)​x+ε​u0∈Int⁡(𝒞)x\_{\varepsilon}\coloneqq(1-\varepsilon)x+\varepsilon u\_{0}\in\operatorname{Int}(\mathcal{C}) and xε→xx\_{\varepsilon}\to x as ε↓0\varepsilon\downarrow 0.
By continuity, ℓ​(xε)→ℓ​(x)\ell(x\_{\varepsilon})\to\ell(x), hence infInt⁡(𝒞)ℓ≤ℓ​(x)\inf\_{\operatorname{Int}(\mathcal{C})}\ell\leq\ell(x) for all x∈𝒞x\in\mathcal{C},
implying infInt⁡(𝒞)ℓ≤inf𝒞ℓ\inf\_{\operatorname{Int}(\mathcal{C})}\ell\leq\inf\_{\mathcal{C}}\ell.
Since Int⁡(𝒞)⊆𝒞\operatorname{Int}(\mathcal{C})\subseteq\mathcal{C}, we also have inf𝒞ℓ≤infInt⁡(𝒞)ℓ\inf\_{\mathcal{C}}\ell\leq\inf\_{\operatorname{Int}(\mathcal{C})}\ell.
Thus the optimal values coincide.

Finally, arg⁡min⁡f≠∅\arg\min f\neq\emptyset holds iff there exists x⋆∈Int⁡(𝒞)x^{\star}\in\operatorname{Int}(\mathcal{C}) with
ℓ​(x⋆)=infx∈𝒞ℓ​(x)\ell(x^{\star})=\inf\_{x\in\mathcal{C}}\ell(x), in which case u⋆=p−1​(x⋆)u^{\star}=p^{-1}(x^{\star}) exists and satisfies u⋆∈arg⁡min⁡fu^{\star}\in\arg\min f.
Conversely, if u⋆∈arg⁡min⁡fu^{\star}\in\arg\min f, then p​(u⋆)∈Int⁡(𝒞)p(u^{\star})\in\operatorname{Int}(\mathcal{C}) satisfies
ℓ​(p​(u⋆))=infx∈𝒞ℓ​(x)\ell(p(u^{\star}))=\inf\_{x\in\mathcal{C}}\ell(x), i.e., p​(u⋆)∈arg⁡min𝒞⁡ℓ∩Int⁡(𝒞)p(u^{\star})\in\arg\min\_{\mathcal{C}}\ell\cap\operatorname{Int}(\mathcal{C}).
∎

Next, we establish the equivalence of stationary points between the two objectives.

\CorrStatPoints

\*

###### Proof.

The gradient identity follows from the chain rule, using that p​(u)∈Int⁡(𝒞)p(u)\in\operatorname{Int}(\mathcal{C}) for all uu. If Jp​(u)J\_{p}(u) is invertible and ∇f​(u)=Jp​(u)⊤​∇ℓ​(p​(u))=0\nabla f(u)=J\_{p}(u)^{\top}\nabla\ell(p(u))=0, then ∇ℓ​(p​(u))=0\nabla\ell(p(u))=0. The converse is immediate.
∎

We then extend this analysis to show that local minimizers of the composite objective correspond to global minimizers of the constrained problem.

\GlobOptInt

\*

###### Proof.

Let uu be a local minimizer of ff at which pp is differentiable. Then Jp​(u)J\_{p}(u) is invertible by Theorem [2.5](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem5 "Definition 2.5 (Scalar projection map). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning"), and ∇f​(u)=0\nabla f(u)=0. By Proposition [3](https://arxiv.org/html/2602.03461v1#S3 "3 Optimization Guarantees ‣ Soft-Radial Projection for Constrained End-to-End Learning"), ∇ℓ​(p​(u))=0\nabla\ell(p(u))=0. Since p​(u)∈Int⁡(𝒞)p(u)\in\operatorname{Int}(\mathcal{C}) and ℓ\ell is convex, ∇ℓ​(p​(u))=0\nabla\ell(p(u))=0 implies that p​(u)p(u) is a global minimizer of ℓ\ell (over ℝn\mathbb{R}^{n}, and therefore also over 𝒞\mathcal{C}).
∎

We now investigate the convergence rate and demonstrate the absence of a global Polyak-Łojasiewicz (PL) condition, which necessitates a more nuanced convergence analysis.

\AbsencePL

\*

###### Proof.

The unique minimizer of ℓ\ell over 𝒞\mathcal{C} is x⋆=0x^{\star}=0, and the corresponding optimal value ℓ⋆=0\ell^{\star}=0. Fix a unit vector vv and consider u​(t)≔t​vu(t)\coloneqq tv with t≥0t\geq 0. For 𝒞=B1​(0)\mathcal{C}=B\_{1}(0) the hard radial projection is q​(u)=uq(u)=u if ‖u‖≤1\|u\|\leq 1 and q​(u)=u/‖u‖q(u)=u/\|u\| otherwise; hence for t≥1t\geq 1 we have q​(u​(t))=vq(u(t))=v and therefore

|  |  |  |
| --- | --- | --- |
|  | p​(u​(t))=r​(t2)​v,f​(u​(t))=‖p​(u​(t))‖2=r​(t2)2.p(u(t))\;=\;r(t^{2})\,v,\qquad f(u(t))\;=\;\|p(u(t))\|^{2}\;=\;r(t^{2})^{2}. |  |

Since r​(t2)→1r(t^{2})\to 1 as t→∞t\to\infty, we obtain

|  |  |  |
| --- | --- | --- |
|  | f​(u​(t))−f⋆=r​(t2)2→ 1(t→∞),f(u(t))-f^{\star}\;=\;r(t^{2})^{2}\;\to\;1\quad(t\to\infty), |  |

so along this ray the suboptimality converges to a strictly positive constant. Next, compute the gradient for t>1t>1. On {‖u‖>1}\{\|u\|>1\}, the hard radial projection q​(u)=u/‖u‖q(u)=u/\|u\| has Jacobian

|  |  |  |
| --- | --- | --- |
|  | Jq​(u)=1‖u‖​(I−u​u⊤‖u‖2),J\_{q}(u)\;=\;\frac{1}{\|u\|}\Bigl(I-\frac{uu^{\top}}{\|u\|^{2}}\Bigr), |  |

so at u​(t)=t​vu(t)=tv

|  |  |  |
| --- | --- | --- |
|  | Jq​(u​(t))=1t​(I−v​v⊤).J\_{q}(u(t))\;=\;\frac{1}{t}\bigl(I-vv^{\top}\bigr). |  |

Substituting the expression for the Jacobian Jp​(u)J\_{p}(u) given in ([9](https://arxiv.org/html/2602.03461v1#A2.E9 "Equation 9 ‣ Proof. ‣ B.1 Proofs of Section 2 ‣ Appendix B Proofs ‣ Soft-Radial Projection for Constrained End-to-End Learning")), we obtain for t>1t>1

|  |  |  |
| --- | --- | --- |
|  | Jp​(u​(t))=r​(t2)t​(I−v​v⊤)+ 2​t​r′​(t2)​v​v⊤.J\_{p}(u(t))=\frac{r(t^{2})}{t}(I-vv^{\top})\;+\;2t\,r^{\prime}(t^{2})\,vv^{\top}. |  |

By Proposition [3](https://arxiv.org/html/2602.03461v1#S3 "3 Optimization Guarantees ‣ Soft-Radial Projection for Constrained End-to-End Learning"), the gradient is given by ∇f​(u)=Jp​(u)⊤​∇ℓ​(p​(u))\nabla f(u)=J\_{p}(u)^{\top}\nabla\ell(p(u)). Since ℓ​(x)=‖x‖2\ell(x)=\|x\|^{2} implies ∇ℓ​(x)=2​x\nabla\ell(x)=2x, and specifically p​(u​(t))=r​(t2)​vp(u(t))=r(t^{2})v, we obtain

|  |  |  |
| --- | --- | --- |
|  | ∇f​(u​(t))=Jp​(u​(t))⊤​(2​r​(t2)​v)= 2​r​(t2)​Jp​(u​(t))​v,\nabla f(u(t))\;=\;J\_{p}(u(t))^{\top}\bigl(2r(t^{2})v\bigr)\;=\;2r(t^{2})J\_{p}(u(t))v, |  |

where the last equality follows from the symmetry of Jp​(u​(t))J\_{p}(u(t)). When applying the Jacobian matrix to the vector vv, the tangential term vanishes because (I−v​v⊤)​v=0(I-vv^{\top})v=0. Only the radial term remains

|  |  |  |
| --- | --- | --- |
|  | Jp​(u​(t))​v=(2​t​r′​(t2)​v​v⊤)​v= 2​t​r′​(t2)​v.J\_{p}(u(t))v\;=\;\left(2tr^{\prime}(t^{2})vv^{\top}\right)v\;=\;2tr^{\prime}(t^{2})v. |  |

Substituting this back yields the final gradient norm

|  |  |  |
| --- | --- | --- |
|  | ‖∇f​(u​(t))‖=‖2​r​(t2)⋅2​t​r′​(t2)​v‖= 4​t​r​(t2)​r′​(t2).\|\nabla f(u(t))\|\;=\;\|2r(t^{2})\cdot 2tr^{\prime}(t^{2})v\|\;=\;4\,t\,r(t^{2})\,r^{\prime}(t^{2}). |  |

It remains to show the existence of a sequence tk→∞t\_{k}\to\infty such that tk​r′​(tk2)→0t\_{k}r^{\prime}(t\_{k}^{2})\to 0. Since limρ→∞r​(ρ)=1\lim\_{\rho\to\infty}r(\rho)=1, we have ∫0∞r′​(ρ)​𝑑ρ=1−r​(0)<∞\int\_{0}^{\infty}r^{\prime}(\rho)\,d\rho=1-r(0)<\infty. We claim there exists a sequence ρk→∞\rho\_{k}\to\infty such that ρk​r′​(ρk)→0\sqrt{\rho\_{k}}\,r^{\prime}(\rho\_{k})\to 0. Indeed, if not, then there exist ε>0\varepsilon>0 and ρ0≥0\rho\_{0}\geq 0 such that ρ​r′​(ρ)≥ε\sqrt{\rho}\,r^{\prime}(\rho)\geq\varepsilon for all ρ≥ρ0\rho\geq\rho\_{0}, which implies

|  |  |  |
| --- | --- | --- |
|  | ∫0∞r′​(ρ)​𝑑ρ≥ε​∫ρ0∞d​ρρ=∞,\int\_{0}^{\infty}r^{\prime}(\rho)\,d\rho\;\geq\;\varepsilon\int\_{\rho\_{0}}^{\infty}\frac{d\rho}{\sqrt{\rho}}\;=\;\infty, |  |

a contradiction. Setting tk≔ρkt\_{k}\coloneqq\sqrt{\rho\_{k}} yields tk→∞t\_{k}\to\infty and tk​r′​(tk2)→0t\_{k}r^{\prime}(t\_{k}^{2})\to 0. Along u​(tk)=tk​vu(t\_{k})=t\_{k}v we therefore have ‖∇f​(u​(tk))‖→0\|\nabla f(u(t\_{k}))\|\to 0 while f​(u​(tk))−f⋆→1f(u(t\_{k}))-f^{\star}\to 1. Consequently, no μ>0\mu>0 can satisfy a global PL inequality ‖∇f​(u)‖2≥2​μ​(f​(u)−f⋆)\|\nabla f(u)\|^{2}\geq 2\mu\,(f(u)-f^{\star}) for all u∈ℝnu\in\mathbb{R}^{n}.
∎

Given the absence of the global PL condition, we provide convergence guarantees for both smooth and nonsmooth regimes.

\Convergence

\*

###### Proof.

We differentiate between the smooth and non-smooth regimes based on the properties of the data distribution and the resulting regularity of the composite objective.

##### Regime I: Smooth Optimization.

Assume the data distribution ℙ\mathbb{P} is absolutely continuous. As established in Theorem [2.5](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem5 "Definition 2.5 (Scalar projection map). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning"), the soft-radial projection pp is differentiable almost everywhere. Consequently, the event that a pre-activation u=gθ​(z)u=g\_{\theta}(z) lands exactly on the non-differentiable boundary ∂𝒞\partial\mathcal{C} has measure zero.

While the pointwise function f​(u)=ℓ​(p​(u))f(u)=\ell(p(u)) is not globally LL-smooth (due to Jacobian discontinuities at ∂𝒞\partial\mathcal{C}), the *expected* objective F​(θ)F(\theta) becomes smooth due to the smoothing effect of the integration over an absolutely continuous distribution. However, to provide a tractable bound on the gradients, we analyze the smoothness of ff on the dense open set U=ℝn∖∂𝒞U=\mathbb{R}^{n}\setminus\partial\mathcal{C} where pp is twice differentiable. Assume ∇ℓ\nabla\ell is LℓL\_{\ell}-Lipschitz on p​(K)p(K), and on the smooth pieces U∩KU\cap K, JpJ\_{p} is LpL\_{p}-Lipschitz. Define the constants over these smooth regions:

|  |  |  |
| --- | --- | --- |
|  | Gℓ≔supx∈p​(K)‖∇ℓ​(x)‖,Bp≔supu∈K∖∂𝒞‖Jp​(u)‖.G\_{\ell}\coloneqq\sup\_{x\in p(K)}\|\nabla\ell(x)\|,\qquad B\_{p}\coloneqq\sup\_{u\in K\setminus\partial\mathcal{C}}\|J\_{p}(u)\|. |  |

For any u,u′u,u^{\prime} lying in the same connected component of U∩KU\cap K, we apply the chain rule ∇f​(u)=Jp​(u)⊤​∇ℓ​(p​(u))\nabla f(u)=J\_{p}(u)^{\top}\nabla\ell(p(u)). We decouple the variations in the Jacobian and the loss gradient by adding and subtracting the cross-term Jp​(u)⊤​∇ℓ​(p​(u′))J\_{p}(u)^{\top}\nabla\ell(p(u^{\prime})), and applying the triangle inequality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖∇f​(u)−∇f​(u′)‖\displaystyle\|\nabla f(u)-\nabla f(u^{\prime})\| | =‖Jp​(u)⊤​∇ℓ​(p​(u))−Jp​(u′)⊤​∇ℓ​(p​(u′))‖\displaystyle=\|J\_{p}(u)^{\top}\nabla\ell(p(u))-J\_{p}(u^{\prime})^{\top}\nabla\ell(p(u^{\prime}))\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =‖Jp​(u)⊤​∇ℓ​(p​(u))−Jp​(u)⊤​∇ℓ​(p​(u′))+Jp​(u)⊤​∇ℓ​(p​(u′))−Jp​(u′)⊤​∇ℓ​(p​(u′))‖\displaystyle=\|J\_{p}(u)^{\top}\nabla\ell(p(u))-J\_{p}(u)^{\top}\nabla\ell(p(u^{\prime}))+J\_{p}(u)^{\top}\nabla\ell(p(u^{\prime}))-J\_{p}(u^{\prime})^{\top}\nabla\ell(p(u^{\prime}))\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖Jp​(u)‖​‖∇ℓ​(p​(u))−∇ℓ​(p​(u′))‖+‖∇ℓ​(p​(u′))‖​‖Jp​(u)−Jp​(u′)‖\displaystyle\leq\|J\_{p}(u)\|\|\nabla\ell(p(u))-\nabla\ell(p(u^{\prime}))\|+\|\nabla\ell(p(u^{\prime}))\|\|J\_{p}(u)-J\_{p}(u^{\prime})\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Bp​Lℓ​‖p​(u)−p​(u′)‖+Gℓ​Lp​‖u−u′‖\displaystyle\leq B\_{p}L\_{\ell}\|p(u)-p(u^{\prime})\|+G\_{\ell}L\_{p}\|u-u^{\prime}\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(Bp2​Lℓ+Gℓ​Lp)​‖u−u′‖.\displaystyle\leq(B\_{p}^{2}L\_{\ell}+G\_{\ell}L\_{p})\|u-u^{\prime}\|. |  |

Thus, ff is LL-smooth *almost everywhere* with constant L≤Lℓ​Bp2+Gℓ​LpL\leq L\_{\ell}B\_{p}^{2}+G\_{\ell}L\_{p}. Under the assumption of absolute continuity of ℙ\mathbb{P}, the objective F​(θ)=𝔼​[f​(gθ​(z))]F(\theta)=\mathbb{E}[f(g\_{\theta}(z))] inherits differentiability, and the variance of the gradients is bounded by the Lipschitz continuity of ff. Applying standard Stochastic Gradient Descent (SGD) with step size ηt∝1/T\eta\_{t}\propto 1/\sqrt{T} guarantees convergence to a stationary point of FF Ghadimi and Lan ([2013](https://arxiv.org/html/2602.03461v1#bib.bib31 "Stochastic first-and zeroth-order methods for nonconvex stochastic programming")):

|  |  |  |
| --- | --- | --- |
|  | min0≤t<T⁡𝔼​[‖∇F​(θt)‖2]=𝒪​(1T).\min\_{0\leq t<T}\mathbb{E}[\|\nabla F(\theta\_{t})\|^{2}]=\mathcal{O}\left(\frac{1}{\sqrt{T}}\right). |  |

##### Regime II: Nonsmooth Optimization.

If the data distribution is discrete or arbitrary, the differentiability of F​(θ)F(\theta) cannot be guaranteed. However, we can establish convergence by relying on the theory of *tame functions* Davis et al. ([2020](https://arxiv.org/html/2602.03461v1#bib.bib38 "Stochastic subgradient method converges on tame functions")). This framework covers the vast majority of deep learning architectures and ensures that stochastic subgradient methods converge effectively, provided the objective satisfies two structural properties:

1. 1.

   Lipschitz Continuity: As a consequence of Lemma [2](https://arxiv.org/html/2602.03461v1#S2.F2 "Figure 2 ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning"), the soft-radial projection pp is locally Lipschitz. Since the loss ℓ\ell and the network gθg\_{\theta} (e.g., with ReLU activations) are also locally Lipschitz, their composition F​(θ)F(\theta) inherits this property. This guarantees that the Clarke subdifferential ∂F​(θ)\partial F(\theta) is non-empty and uniformly bounded on compact sets.
2. 2.

   Tame Objective: The convergence results of Davis et al. ([2020](https://arxiv.org/html/2602.03461v1#bib.bib38 "Stochastic subgradient method converges on tame functions")) apply to the class of *tame* functions. This class encompasses functions constructed from finite compositions of piecewise-polynomials and algebraic operations. Since standard activations (like ReLU) are piecewise-polynomial, and our soft-radial projection is constructed from norms and algebraic radial mappings (assuming a semi-algebraic constraint set 𝒞\mathcal{C}, such as a polytope or ball), the composite objective satisfies this property. This guarantees that the loss landscape is geometrically well-behaved, preventing pathological infinite oscillations.

Davis et al. ([2020](https://arxiv.org/html/2602.03461v1#bib.bib38 "Stochastic subgradient method converges on tame functions"), Thm. 3.2) proved that for any locally Lipschitz, tame function, the Stochastic Subgradient Method with diminishing step sizes ηt→0\eta\_{t}\to 0 (and ∑ηt=∞\sum\eta\_{t}=\infty, ∑ηt2<∞\sum\eta\_{t}^{2}<\infty) converges almost surely to the set of Clarke stationary points:

|  |  |  |
| --- | --- | --- |
|  | limT→∞𝔼​[minv∈∂F​(θT)⁡‖v‖]=0.\lim\_{T\to\infty}\mathbb{E}\left[\min\_{v\in\partial F(\theta\_{T})}\|v\|\right]=0. |  |

This result holds even if the iterates traverse the non-differentiable boundary ∂𝒞\partial\mathcal{C}, provided the standard bounded variance assumption on the subgradients is met. In our case, this is guaranteed by the local Lipschitz property of the objective on the compact set KK.
∎

### B.3 Proofs of Section [4](https://arxiv.org/html/2602.03461v1#S4 "4 Constrained Universal Approximation ‣ Soft-Radial Projection for Constrained End-to-End Learning")

Finally, we prove that the constrained model inherits the universal approximation capabilities of the underlying unconstrained architecture.

\ConstUnvAppr

\*

###### Proof.

Without loss of generality, we assume 0∈Int⁡(𝒞)0\in\operatorname{Int}(\mathcal{C}) serves as the anchor point (see Coordinate Convention in Section [2](https://arxiv.org/html/2602.03461v1#S2 "2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning")). Throughout this proof, we denote the uniform norm of a function ψ:𝒵→ℝn\psi:\mathcal{Z}\to\mathbb{R}^{n} by ‖ψ‖∞≔supz∈𝒵‖ψ​(z)‖\|\psi\|\_{\infty}\coloneqq\sup\_{z\in\mathcal{Z}}\|\psi(z)\|. We separate the interior and boundary cases.

*Interior case.* Assume the target image satisfies h​(𝒵)⊂Int⁡(𝒞)h(\mathcal{Z})\subset\operatorname{Int}(\mathcal{C}). Since p:ℝn→Int⁡(𝒞)p:\mathbb{R}^{n}\to\operatorname{Int}(\mathcal{C}) is a homeomorphism (Theorem [2.5](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem5 "Definition 2.5 (Scalar projection map). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning")), the function ϕ≔p−1∘h:𝒵→ℝn\phi\coloneqq p^{-1}\circ h:\mathcal{Z}\to\mathbb{R}^{n} is continuous. Since 𝒵\mathcal{Z} is compact, the image ϕ​(𝒵)\phi(\mathcal{Z}) is compact. Fix any δ0>0\delta\_{0}>0 (e.g., δ0=1\delta\_{0}=1) and define the compact δ0\delta\_{0}-thickening

|  |  |  |
| --- | --- | --- |
|  | K≔{ξ∈ℝn∣dist⁡(ξ,ϕ​(𝒵))≤δ0},K\coloneqq\bigl\{\xi\in\mathbb{R}^{n}\mid\operatorname{dist}\bigl(\xi,\phi(\mathcal{Z})\bigr)\leq\delta\_{0}\bigr\}, |  |

where dist⁡(ξ,A)≔infa∈A‖ξ−a‖\operatorname{dist}(\xi,A)\coloneqq\inf\_{a\in A}\|\xi-a\|. By the local Lipschitz continuity of pp on the compact set KK, there exists a constant LK<∞L\_{K}<\infty such that ‖p​(a)−p​(b)‖≤LK​‖a−b‖\|p(a)-p(b)\|\leq L\_{K}\|a-b\| for all a,b∈Ka,b\in K. By the universality of 𝒢\mathcal{G}, there exists a function g∈𝒢g\in\mathcal{G} such that

|  |  |  |
| --- | --- | --- |
|  | ‖g−ϕ‖∞≤δ,δ≔min⁡{δ0,εLK}.\|g-\phi\|\_{\infty}\;\leq\;\delta,\qquad\delta\coloneqq\min\Bigl\{\delta\_{0},\ \frac{\varepsilon}{L\_{K}}\Bigr\}. |  |

This implies g​(𝒵)⊂Kg(\mathcal{Z})\subset K. Consequently, for all z∈𝒵z\in\mathcal{Z}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖p​(g​(z))−h​(z)‖\displaystyle\|p(g(z))-h(z)\| | =‖p​(g​(z))−p​(ϕ​(z))‖\displaystyle=\|p(g(z))-p(\phi(z))\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤LK​‖g​(z)−ϕ​(z)‖\displaystyle\leq L\_{K}\,\|g(z)-\phi(z)\| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤LK​δ≤ε,\displaystyle\leq L\_{K}\,\delta\;\leq\;\varepsilon, |  |

which implies ‖p∘g−h‖∞≤ε\|p\circ g-h\|\_{\infty}\leq\varepsilon, proving the claim for the interior case.

*Boundary case.* For a general target h:𝒵→𝒞h:\mathcal{Z}\to\mathcal{C}, we define a strictly interior approximation hεh\_{\varepsilon} by shrinking hh towards the anchor. Define the shrink operator Sτ​(x)≔(1−τ)​xS\_{\tau}(x)\coloneqq(1-\tau)x. Since 𝒞\mathcal{C} is convex and 0∈Int⁡(𝒞)0\in\operatorname{Int}(\mathcal{C}), we have Sτ​(𝒞)⊂Int⁡(𝒞)S\_{\tau}(\mathcal{C})\subset\operatorname{Int}(\mathcal{C}) for any τ∈(0,1)\tau\in(0,1).Let D≔‖h‖∞<∞D\coloneqq\|h\|\_{\infty}<\infty. If D=0D=0, then h≡0h\equiv 0, and the interior case applies directly. Otherwise, we select a shrinkage factor τ\tau sufficiently small to ensure hεh\_{\varepsilon} remains within ε/2\varepsilon/2 of hh. Specifically, set:

|  |  |  |
| --- | --- | --- |
|  | τ≔min⁡{12,ε2​D}∈(0,1),hε≔Sτ∘h.\tau\coloneqq\min\Bigl\{\tfrac{1}{2},\ \frac{\varepsilon}{2D}\Bigr\}\in(0,1),\qquad h\_{\varepsilon}\coloneqq S\_{\tau}\circ h. |  |

The uniform distance between the original and shrunken target is bounded by

|  |  |  |
| --- | --- | --- |
|  | ‖hε−h‖∞=supz∈𝒵‖(1−τ)​h​(z)−h​(z)‖=τ​D≤ε2.\|h\_{\varepsilon}-h\|\_{\infty}\;=\;\sup\_{z\in\mathcal{Z}}\|(1-\tau)h(z)-h(z)\|\;=\;\tau D\;\leq\;\frac{\varepsilon}{2}. |  |

Since the new target satisfies hε​(𝒵)⊂Int⁡(𝒞)h\_{\varepsilon}(\mathcal{Z})\subset\operatorname{Int}(\mathcal{C}), we can invoke the *Interior case* result with precision ε/2\varepsilon/2. This guarantees the existence of a function g∈𝒢g\in\mathcal{G} such that

|  |  |  |
| --- | --- | --- |
|  | ‖p∘g−hε‖∞≤ε2.\|p\circ g-h\_{\varepsilon}\|\_{\infty}\;\leq\;\frac{\varepsilon}{2}. |  |

Finally, applying the triangle inequality yields the total error bound

|  |  |  |
| --- | --- | --- |
|  | ‖p∘g−h‖∞≤‖p∘g−hε‖∞⏟≤ε/2+‖hε−h‖∞⏟≤ε/2≤ε.\|p\circ g-h\|\_{\infty}\;\leq\;\underbrace{\|p\circ g-h\_{\varepsilon}\|\_{\infty}}\_{\leq\varepsilon/2}\;+\;\underbrace{\|h\_{\varepsilon}-h\|\_{\infty}}\_{\leq\varepsilon/2}\;\leq\;\varepsilon. |  |

∎

## Appendix C Extended Numerical Results

In this section, we first provide additional insights into the model parameters, specifically how the radial contraction function r​(⋅)r(\cdot) and the scale parameter λ\lambda influence the effective optimization landscape. Next, we provide implementation details for the competitor algorithms, DC3 (Donti et al., [2021](https://arxiv.org/html/2602.03461v1#bib.bib16 "DC3: A learning method for optimization with hard constraints")) and HardNet (Min and Azizan, [2024](https://arxiv.org/html/2602.03461v1#bib.bib9 "HardNet: Hard-constrained neural networks with universal approximation guarantees")), which were adjusted to accommodate the (capped) simplex constraints considered in our experiments. We then detail the architectures and hyperparameters utilized within our study. Finally, we conclude with a comprehensive description of our experimental setups.

### C.1 Sensitivity Analysis: Radial Contraction and Scaling

In Sec. [5.1](https://arxiv.org/html/2602.03461v1#S5.SS1 "5.1 Implementation Details ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning") we introduced radial contraction functions r​(⋅)r(\cdot) satisfying the properties of Assumption [2.3](https://arxiv.org/html/2602.03461v1#S2.Thmtheorem3 "Assumption 2.3 (Radial monotonicity). ‣ 2 Soft-Radial Projection Layer ‣ Soft-Radial Projection for Constrained End-to-End Learning"). The *rational* radial contraction decays polynomially (𝒪​(ρ−1)\mathcal{O}(\rho^{-1})), whereas the *exponential* and *hyperbolic* forms exhibit exponential decay. Consequently, the rational link preserves larger gradient magnitudes for predictions falling far outside the feasible set (ρ≫1\rho\gg 1), which helps mitigate the vanishing gradient problem for extreme outliers.

Similar to the problem illustrated in Fig. [1](https://arxiv.org/html/2602.03461v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Soft-Radial Projection for Constrained End-to-End Learning"), we evaluate the role of r​(⋅)r(\cdot) in terms of warping the effective loss landscape (A), influencing the training loss (B), and determining the convergence to the target x∗x^{\*}. Figures [3](https://arxiv.org/html/2602.03461v1#A3.F3 "Figure 3 ‣ C.1 Sensitivity Analysis: Radial Contraction and Scaling ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning"), [4](https://arxiv.org/html/2602.03461v1#A3.F4 "Figure 4 ‣ C.1 Sensitivity Analysis: Radial Contraction and Scaling ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning"), and [5](https://arxiv.org/html/2602.03461v1#A3.F5 "Figure 5 ‣ C.1 Sensitivity Analysis: Radial Contraction and Scaling ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning") visualize the effective loss landscape for the *rational* ([3](https://arxiv.org/html/2602.03461v1#S5.E3 "Equation 3 ‣ 5.1 Implementation Details ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning")), *exponential* ([4](https://arxiv.org/html/2602.03461v1#S5.E4 "Equation 4 ‣ 5.1 Implementation Details ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning")), and *hyperbolic* ([5](https://arxiv.org/html/2602.03461v1#S5.E5 "Equation 5 ‣ 5.1 Implementation Details ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning")) functions, respectively. Furthermore, we illustrate in Fig. [6](https://arxiv.org/html/2602.03461v1#A3.F6 "Figure 6 ‣ C.1 Sensitivity Analysis: Radial Contraction and Scaling ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning") how the minimum scaling threshold ε\varepsilon modifies the landscape geometry surrounding the chosen anchor u0u\_{0}.

![Refer to caption](x4.png)


(a) λ=0.5\lambda=0.5.

![Refer to caption](x5.png)


(b) λ=1.0\lambda=1.0.

![Refer to caption](x6.png)


(c) λ=2.0\lambda=2.0

Figure 3: Soft-radial projection p​(u)p(u) with *rational* radial contraction ([3](https://arxiv.org/html/2602.03461v1#S5.E3 "Equation 3 ‣ 5.1 Implementation Details ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning")).



![Refer to caption](x7.png)


(a) λ=0.5\lambda=0.5.

![Refer to caption](x8.png)


(b) λ=1.0\lambda=1.0.

![Refer to caption](x9.png)


(c) λ=2.0\lambda=2.0.

Figure 4: Soft-radial projection p​(u)p(u) with *exponential* radial contraction ([4](https://arxiv.org/html/2602.03461v1#S5.E4 "Equation 4 ‣ 5.1 Implementation Details ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning")).



![Refer to caption](x10.png)


(a) λ=0.5\lambda=0.5.

![Refer to caption](x11.png)


(b) λ=1.0\lambda=1.0.

![Refer to caption](x12.png)


(c) λ=2.0\lambda=2.0.

Figure 5: Soft-radial projection p​(u)p(u) with *hyperbolic* radial contraction ([5](https://arxiv.org/html/2602.03461v1#S5.E5 "Equation 5 ‣ 5.1 Implementation Details ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning")).



![Refer to caption](x13.png)


(a) ε=0.001\varepsilon=0.001.

![Refer to caption](x14.png)


(b) ε=0.01\varepsilon=0.01.

![Refer to caption](x15.png)


(c) ε=0.1\varepsilon=0.1.

Figure 6: Soft-radial projection p​(u)p(u) for varying minimum scaling threshold ε\varepsilon.

### C.2 Adaptation of Competitor Methods to Capped Simplex Constraints

We explain the adaptation of the competitor methods with respect to the capped simplex introduced in the portfolio setting and formally defined as

|  |  |  |
| --- | --- | --- |
|  | 𝒞={w∈ℝN| 0≤w, 1⊤​w=1,w≤c},\mathcal{C}\;=\;\Bigl\{w\in\mathbb{R}^{N}\ \big|\ 0\leq w,\ \mathds{1}^{\top}w=1,\ w\leq c\Bigr\}, |  |

where ww is the portfolio weight and cc is a cap on the weight.

HardNet. The HardNet framework Min and Azizan ([2024](https://arxiv.org/html/2602.03461v1#bib.bib9 "HardNet: Hard-constrained neural networks with universal approximation guarantees")) enforces feasibility by appending a differentiable projection layer to an unconstrained predictor gθ:𝒵→ℝNg\_{\theta}:\mathcal{Z}\to\mathbb{R}^{N}. Given an input z∈𝒵z\in\mathcal{Z} and raw output u≔gθ​(z)u\coloneqq g\_{\theta}(z), the method considers input-dependent affine constraints of the form

|  |  |  |
| --- | --- | --- |
|  | b¯​(z)≤A​(z)​w≤b¯​(z).\underline{b}(z)\leq A(z)w\leq\bar{b}(z). |  |

Min and Azizan ([2024](https://arxiv.org/html/2602.03461v1#bib.bib9 "HardNet: Hard-constrained neural networks with universal approximation guarantees")) derive a closed-form projection for this case, denoted HardNet-Aff:

|  |  |  |  |
| --- | --- | --- | --- |
|  | PHN​(u;z)=u+AR†​(z)​(ReLU⁡(b¯​(z)−A​(z)​u)−ReLU⁡(A​(z)​u−b¯​(z))),P\_{\text{HN}}(u;z)\;=\;u\;+\;A^{\dagger}\_{\mathrm{R}}(z)\Big(\operatorname{ReLU}\big(\underline{b}(z)-A(z)u\big)-\operatorname{ReLU}\big(A(z)u-\bar{b}(z)\big)\Big), |  | (10) |

where AR†​(z)≔A​(z)⊤​(A​(z)​A​(z)⊤)−1A^{\dagger}\_{\mathrm{R}}(z)\coloneqq A(z)^{\top}\!\big(A(z)A(z)^{\top}\big)^{-1} is the Moore–Penrose *right* pseudoinverse. This closed form assumes that A​(z)A(z) has full row rank (Assumption 5 in Min and Azizan ([2024](https://arxiv.org/html/2602.03461v1#bib.bib9 "HardNet: Hard-constrained neural networks with universal approximation guarantees"))), describing an underdetermined system.
In our portfolio setting, the feasible set is a capped simplex; stacking the equality constraint with the 2​N2N bound constraints yields an *overdetermined* affine system. Consequently, the matrix A​A⊤AA^{\top} is singular and the right-pseudoinverse expression in ([10](https://arxiv.org/html/2602.03461v1#A3.E10 "Equation 10 ‣ C.2 Adaptation of Competitor Methods to Capped Simplex Constraints ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning")) is not directly applicable. We therefore use a least-squares relaxation of the HardNet correction. This involves defining a (signed) violation vector

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(u;z)≔ReLU⁡(b¯​(z)−A​u)−ReLU⁡(A​u−b¯​(z)).v(u;z)\;\coloneqq\;\operatorname{ReLU}\big(\underline{b}(z)-Au\big)-\operatorname{ReLU}\big(Au-\bar{b}(z)\big). |  | (11) |

Since the resulting static constraint matrix AA has full column rank in our construction, we compute a least-squares correction direction via the *left* pseudoinverse

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​(u;z)≔arg⁡minΔ∈ℝN⁡‖A​Δ−v​(u;z)‖2=AL†​v​(u;z),AL†≔(A⊤​A)−1​A⊤.\Delta(u;z)\;\coloneqq\;\arg\min\_{\Delta\in\mathbb{R}^{N}}\ \|A\Delta-v(u;z)\|^{2}\;=\;A^{\dagger}\_{\mathrm{L}}\,v(u;z),\qquad A^{\dagger}\_{\mathrm{L}}\coloneqq(A^{\top}A)^{-1}A^{\top}. |  | (12) |

We then set w~≔u+Δ​(u;z)\tilde{w}\coloneqq u+\Delta(u;z). A conceptually broader but computationally slower alternative proposed by the authors for general convex constraints is to embed the projection as a differentiable convex optimization layer Agrawal et al. ([2019](https://arxiv.org/html/2602.03461v1#bib.bib18 "Differentiable convex optimization layers")), referred to as HardNet-Cvx. To remove any remaining numerical residuals during evaluation, we additionally apply an exact orthogonal projection onto the capped simplex, w=P​(w~)w=P(\tilde{w}), to guarantee w∈𝒞w\in\mathcal{C}.

##### Symmetric DC3 for the capped simplex.

We adapt the Deep Constraint Completion and Correction (DC3) framework (Donti et al., [2021](https://arxiv.org/html/2602.03461v1#bib.bib16 "DC3: A learning method for optimization with hard constraints")) to 𝒞\mathcal{C}. Standard DC3 selects N−1N-1 independent variables and defines the remaining coordinate as dependent via the equality constraint. Applied directly to the raw network output u=gθ​(z)u=g\_{\theta}(z), this introduces an asymmetry: the dependent coordinate absorbs the entire sum deviation, often producing unstable magnitudes and gradients. To mitigate this, we employ a *symmetric* initialization that first distributes the sum deviation evenly by orthogonally projecting uu onto the simplex hyperplane
ℋ≔{w∈ℝN:𝟏⊤​w=1}.\mathcal{H}\coloneqq\{w\in\mathbb{R}^{N}:\mathbf{1}^{\top}w=1\}.
Concretely, we set

|  |  |  |  |
| --- | --- | --- | --- |
|  | w(0)≔Pℋ​(u)=u−1N​(𝟙⊤​u−1)​𝟙∈ℋ.w^{(0)}\;\coloneqq\;P\_{\mathcal{H}}(u)\;=\;u-\frac{1}{N}\big(\mathds{1}^{\top}u-1\big)\mathds{1}\;\in\;\mathcal{H}. |  | (13) |

We then take the first N−1N-1 coordinates as free variables
ξ≔(w1(0),…,wN−1(0))⊤∈ℝN−1\xi\coloneqq(w^{(0)}\_{1},\ldots,w^{(0)}\_{N-1})^{\top}\in\mathbb{R}^{N-1}
and enforce the equality constraint through a completion map

|  |  |  |  |
| --- | --- | --- | --- |
|  | w​(ξ)≔[ξ1−𝟙⊤​ξ],w(\xi)\;\coloneqq\;\begin{bmatrix}\xi\\ 1-\mathds{1}^{\top}\xi\end{bmatrix}, |  | (14) |

which ensures 𝟙⊤​w​(ξ)=1\mathds{1}^{\top}w(\xi)=1 for all ξ\xi.
To correct violations of the bound constraints 0≤w≤c0\leq w\leq c, we minimize a squared hinge-residual energy

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱(ξ)≔∑i=1N(ReLU(−wi(ξ))2+ReLU(wi(ξ)−ci)2),\mathcal{V}(\xi)\;\coloneqq\;\sum\_{i=1}^{N}\Big(\operatorname{ReLU}\big(-w\_{i}(\xi)\big)^{2}+\operatorname{ReLU}\big(w\_{i}(\xi)-c\_{i}\big)^{2}\Big), |  | (15) |

via an unrolled gradient descent loop on the free variables

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξ(t+1)=ξ(t)−η​∇ξ𝒱​(ξ(t)),t=0,…,L−1.\xi^{(t+1)}\;=\;\xi^{(t)}-\eta\,\nabla\_{\xi}\mathcal{V}\big(\xi^{(t)}\big),\qquad t=0,\ldots,L-1. |  | (16) |

The final output is given by w(L)=w​(ξ(L))w^{(L)}=w(\xi^{(L)}). Gradients are backpropagated through the completion map ([14](https://arxiv.org/html/2602.03461v1#A3.E14 "Equation 14 ‣ Symmetric DC3 for the capped simplex. ‣ C.2 Adaptation of Competitor Methods to Capped Simplex Constraints ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning")), properly accounting for the dependence of the dependent coordinate on the free variables. Similar to the HardNet implementation, we apply an orthogonal projection during evaluation to ensure strict feasibility.

### C.3 Hyperparameter Tuning

Table [4](https://arxiv.org/html/2602.03461v1#A3.T4 "Table 4 ‣ C.3 Hyperparameter Tuning ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning") summarizes the hyperparameters used in our experiments, distinguishing between the portfolio optimization and ride-sharing dispatch task. For both domains, we perform a grid search to select the optimal configuration based on validation performance. As noted earlier, for HardNet and DC3, we apply a final orthogonal projection to the candidate solution during evaluation only. This ensures that the evaluation metrics are not penalized by minor infeasibilities caused by numerical rounding errors. Crucially, we omit this strict projection step during training to preserve gradient flow and prevent the deterioration of learning signals.

Table 4: Hyperparameter settings for portfolio optimization and ride-sharing dispatch experiments.

|  |  |  |
| --- | --- | --- |
| Parameter | Portfolio Optimization | Ride-Sharing Dispatch |
| Architecture & Training | | |
| Base Architecture | LSTM | MLP |
| Hidden Units | {32,64}\{32,64\} | |
| Dropout Rate | {0.1,0.2}\{0.1,0.2\} | |
| Optimizer | Adam | |
| Learning Rate | {1×10−4,5×10−4}\{1\times 10^{-4},5\times 10^{-4}\} | |
| Lookback Horizon (HH) | {10,30}\{10,30\} | 2424 |
| Batch Size | 6464 | 128128 |
| Training Epochs | 5050 | 100100 |
| Projection Layer Hyperparameters | | |
| Softmax Temperature (τ\tau) | {0.1,0.5,1.0,2.0}\{0.1,0.5,1.0,2.0\} | |
| Soft-radial λ\lambda | {0.5,1.0,2.0,5.0,10.0}\{0.5,1.0,2.0,5.0,10.0\} | |
| Soft-radial r​(⋅)r(\cdot) | {Fractional, Exponential, Hyperbolic} | |
| HardNet Steps | {1,3,5}\{1,3,5\} | |
| DC3 Steps | {1,3,5}\{1,3,5\} | |
| DC3 Learning Rate | {10−2,10−1}\{10^{-2},10^{-1}\} | |
| DC3 Momentum | {0.5,0.9}\{0.5,0.9\} | |

### C.4 Extended Analysis: Portfolio Optimization

#### C.4.1 Discussion: Deep Portfolio Optimization vs. Classical Approaches

The formulation presented in Section [5.2](https://arxiv.org/html/2602.03461v1#S5.SS2 "5.2 Portfolio Optimization ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning") represents a deep portfolio optimization problem Zhang et al. ([2020](https://arxiv.org/html/2602.03461v1#bib.bib45 "Deep learning for portfolio optimization")), which fundamentally differs from the classical mean-variance optimization framework Markowitz ([1952](https://arxiv.org/html/2602.03461v1#bib.bib35 "Portfolio selection")).

Predict-then-Optimize vs. End-to-End Learning.
Classical mean-variance optimization typically operates in a “predict-then-optimize” framework: one first estimates the expected return vector μ∈ℝN\mu\in\mathbb{R}^{N} and the covariance matrix Σ∈𝕊+N\Sigma\in\mathbb{S}^{N}\_{+}, and then solves a quadratic program to maximize w⊤​μ−ζ​w⊤​Σ​ww^{\top}\mu-\zeta w^{\top}\Sigma w. This two-step process suffers from two major limitations. First, it separates the prediction error from the optimization cost; a small error in estimating Σ\Sigma can lead to drastically suboptimal portfolios (a phenomenon formally known as the “error maximization” property of Markowitz Michaud ([1989](https://arxiv.org/html/2602.03461v1#bib.bib36 "The Markowitz optimization enigma: Is ‘optimized’ optimal?"))). Second, while standard sample estimators neglect temporal dependencies (implicitly assuming i.i.d. returns), more advanced dynamic estimators (e.g., generalized autoregressive conditional heteroskedasticity (GARCH) model) often impose rigid parametric structures that fail to capture the complex, non-linear interactions between assets that recurrent neural network architectures in the form of gθg\_{\theta} are designed to exploit.

Parameter Sensitivity and Convexity.
A significant hurdle in classical frameworks is the sensitivity to the risk-aversion parameter ζ\zeta, which requires frequent recalibration. Our formulation bypasses this by directly maximizing the Sharpe ratio—a scale-invariant metric that eliminates the need for a subjective risk-return trade-off coefficient. While the static Sharpe ratio maximization is a quasiconcave problem that can be reformulated as a Second-Order Cone Program (SOCP) for global convergence, parameterizing the weights via a neural network gθg\_{\theta} introduces non-convexity. We accept this trade-off to leverage the representational power of deep learning; the model can ingest complex state histories to generate non-linear weight mappings, far surpassing the constraints of the linear-quadratic assumptions in traditional finance.

Transaction Cost as Temporal Regularization. Finally, we address the cost of trading. Classical frameworks often use static L2L\_{2} regularization to prevent overfitting or L1L\_{1} regularization to enforce sparsity Brodie et al. ([2009](https://arxiv.org/html/2602.03461v1#bib.bib34 "Sparse and stable Markowitz portfolios")). However, these spatial constraints fail to penalize policy volatility: a network can satisfy strict sparsity constraints while still oscillating wildly between assets over time.

To enforce temporal consistency, we explicitly model transaction costs via the term γ2​‖wt−wt−1+‖1\frac{\gamma}{2}\|w\_{t}-w\_{t-1}^{+}\|\_{1}. Unlike static penalties, this targets the velocity of the portfolio turnover. Crucially, costs are computed relative to the drifted portfolio wt−1+w\_{t-1}^{+}, ensuring that passive price movements do not incur penalties. Let wt−1w\_{t-1} be the weights at t−1t-1. Over the interval (t−1,t](t-1,t], price movements yty\_{t} cause these weights to evolve naturally into the drifted weights wt−1+=(diag​(yt)​wt−1)/(yt⊤​wt−1)w\_{t-1}^{+}=(\text{diag}(y\_{t})\,w\_{t-1})/(y\_{t}^{\top}w\_{t-1}). The numerator captures asset-specific growth, while the denominator renormalizes the sum.

###### Remark C.1 (Cost normalization).

The factor 1/21/2 normalizes the L1L\_{1} distance to represent one-way turnover (the fraction of portfolio value actively replaced). Thus, γ\gamma represents the effective cost per unit of turnover.

This formulation has a profound effect on the learning dynamics. By including this cost directly in the objective, the gradient signal penalizes high-frequency control noise. The policy learns a valid economic trade-off: it naturally creates a *hysteresis effect*, where the portfolio weights exhibit inertia against small market fluctuations. This recovers the classical *no-trade zone* behavior predicted by Davis and Norman ([1990](https://arxiv.org/html/2602.03461v1#bib.bib55 "Portfolio selection with transaction costs")): rebalancing is only performed if the expected Sharpe ratio gain strictly outweighs the explicit cost of the action.

#### C.4.2 Descriptive Statistics

In Table [5](https://arxiv.org/html/2602.03461v1#A3.T5 "Table 5 ‣ C.4.2 Descriptive Statistics ‣ C.4 Extended Analysis: Portfolio Optimization ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning"), we provide descriptive statistics for the asset universes included in our analysis. We evaluate performance across three distinct portfolios, each representing a different difficulty level and correlation structure:

* •

  Global: The Global portfolio aggregates a diverse set of multi-asset class indices covering global equities, treasury bonds, and commodities. It represents a macro-allocation problem characterized by lower average correlation.
* •

  Sectors: The Sectors dataset comprises the 11 primary Global Industry Classification Standard (GICS) sectors. It serves as a standard industry benchmark with high inter-asset correlation, effectively representing the broader US economy.
* •

  Liquid: The Liquid collection contains a selection of 50 high-volume individual stocks. This universe captures the higher volatility and idiosyncratic risk associated with individual stock picking.

Returns are derived from Yahoo Finance adjusted closing prices to account for corporate actions, such as splits and dividends, and are partitioned chronologically to strictly prevent look-ahead bias.333We note that survivorship bias is not compensated for within our analysis, and assets with missing data are omitted from the study. The training set spans from 2010/01/01 to 2018/12/31, covering the post-financial-crisis recovery. The validation set, used for hyperparameter tuning, covers 2019/01/01 to 2020/12/31. The test set extends from 2021/01/01 to 2025/12/31.

Table [5](https://arxiv.org/html/2602.03461v1#A3.T5 "Table 5 ‣ C.4.2 Descriptive Statistics ‣ C.4 Extended Analysis: Portfolio Optimization ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning") reports the annualized mean and median returns alongside annualized volatility. To fully characterize the risk profile and market dynamics, we also include the Maximum Drawdown (Max DD), the average pairwise correlation between assets (ϱ¯\bar{\varrho}), the lag-1 autocorrelation (AC(1)), and the Kolmogorov-Smirnov pp-value (pKSp\_{\text{KS}}). As shown in the table, the test period exhibits significantly higher volatility and maximum drawdown compared to the training period, reflecting more turbulent market conditions. This distribution shift is quantified by pKSp\_{\text{KS}}: for the Global, Liquid, and Sectors universes, pKS<0.05p\_{\text{KS}}<0.05 in the test set, rejecting the null hypothesis that the test data follows the training distribution. This confirms that our evaluation effectively tests the model’s generalization to out-of-distribution market regimes.

Table 5: Summary statistics. Returns, Volatility, and Drawdown are in percentages. ϱ¯\bar{\varrho} is average correlation. pKSp\_{\text{KS}} tests for regime shift.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Universe | Split | μ(%)\mu\,(\%) | Median (%)(\%) | σ(%)\sigma\,(\%) | MaxDD (%)(\%) | ϱ¯\bar{\varrho} | AC(1) | pKSp\_{\text{KS}} |
| Global | Train | 7.307.30 | 11.8411.84 | 17.4717.47 | −19.37-19.37 | 0.350.35 | −0.037-0.037 |  |
| Global | Val | 7.467.46 | 14.2214.22 | 15.6815.68 | −13.87-13.87 | 0.320.32 | −0.020-0.020 | 0.6070.607 |
| Global | Test | 9.309.30 | 13.6013.60 | 22.3422.34 | −28.46-28.46 | 0.460.46 | −0.045-0.045 | 0.0110.011 |
| Liquid | Train | 19.1219.12 | 14.7214.72 | 24.9824.98 | −16.11-16.11 | 0.380.38 | −0.021-0.021 |  |
| Liquid | Val | 19.7119.71 | 30.7630.76 | 25.4025.40 | −18.11-18.11 | 0.390.39 | −0.029-0.029 | 0.3190.319 |
| Liquid | Test | 16.9516.95 | 16.9316.93 | 31.4431.44 | −30.56-30.56 | 0.400.40 | −0.088-0.088 | 0.0190.019 |
| Sectors | Train | 13.4613.46 | 20.1720.17 | 17.0517.05 | −18.61-18.61 | 0.700.70 | −0.037-0.037 |  |
| Sectors | Val | 9.759.75 | 26.7226.72 | 17.1517.15 | −18.47-18.47 | 0.580.58 | −0.003-0.003 | 0.8260.826 |
| Sectors | Test | 13.9913.99 | 22.0122.01 | 24.5724.57 | −36.91-36.91 | 0.650.65 | −0.107-0.107 | 0.0070.007 |

#### C.4.3 Implementation Details

In the portfolio optimization setting, we augment raw asset returns with rolling volatility and rolling correlation to a cross-sectional market proxy (defined as the mean return across the universe). These features are computed over the lookback horizon HH and normalized using training-set statistics to strictly prevent look-ahead bias. We acknowledge that achieving state-of-the-art financial performance typically requires a broader set of predictive signals (alphas). However, our primary objective is to evaluate the stability of the learning process under the high noise-to-signal ratio characteristic of financial time series, rather than to maximize the Sharpe ratio through signal engineering.

As discussed in Sec. [5.2](https://arxiv.org/html/2602.03461v1#S5.SS2 "5.2 Portfolio Optimization ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning"), the L1L\_{1} transaction cost term in ([7](https://arxiv.org/html/2602.03461v1#S5.E7 "Equation 7 ‣ 5.2 Portfolio Optimization ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning")) is non-differentiable at zero, posing a challenge for gradient-based optimization. To address this, we replace the exact L1L\_{1}-norm with the Pseudo-Huber loss, a reparameterization of the smooth penalty introduced by Charbonnier et al. ([1994](https://arxiv.org/html/2602.03461v1#bib.bib46 "Two deterministic half-quadratic regularization algorithms for computed imaging")), defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lδ​(wt,wt−1+)=∑i=1N(δ2+(wi,t−wi,t−1+)2−δ)L\_{\delta}(w\_{t},w\_{t-1}^{+})=\sum\_{i=1}^{N}\left(\sqrt{\delta^{2}+(w\_{i,t}-w\_{i,t-1}^{+})^{2}}-\delta\right) |  | (17) |

where δ>0\delta>0 controls the steepness. As δ→0\delta\to 0, this function converges to ‖wt−wt−1+‖1\|w\_{t}-w\_{t-1}^{+}\|\_{1}, preserving theoretical consistency while enabling stable gradient flow.

#### C.4.4 Additional Empirical Results

In Section [5](https://arxiv.org/html/2602.03461v1#S5 "5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning"), we presented results for the Sharpe ratio maximization formulation defined in ([7](https://arxiv.org/html/2602.03461v1#S5.E7 "Equation 7 ‣ 5.2 Portfolio Optimization ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning")). A common concern in practice is that the explicit inclusion of transaction costs may encourage trivial solutions where the network prioritizes weight stability over active performance optimization. To address this, we provide comparative results for portfolio optimization where training is performed without modeling transaction costs (i.e., omitting the γ2​‖wt−wt−1+‖1\frac{\gamma}{2}\|w\_{t}-w\_{t-1}^{+}\|\_{1} term). We refer to the formulation excluding these costs from the loss function as *training gross*, and the standard formulation including them as *training net*. Crucially, to ensure a fair comparison, we report the net Sharpe ratio and turnover for both configurations during evaluation. Table [6](https://arxiv.org/html/2602.03461v1#A3.T6 "Table 6 ‣ C.4.4 Additional Empirical Results ‣ C.4 Extended Analysis: Portfolio Optimization ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning") and Table [7](https://arxiv.org/html/2602.03461v1#A3.T7 "Table 7 ‣ C.4.4 Additional Empirical Results ‣ C.4 Extended Analysis: Portfolio Optimization ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning") present the aggregated results for the *training gross* and *training net* settings, respectively. Overall, we observe that explicitly considering transaction costs during training leads to a decrease in test-time turnover across methods. Consistent with our findings in Section [5](https://arxiv.org/html/2602.03461v1#S5 "5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning"), our *soft-radial projection* demonstrates superior financial performance and greater robustness to random seed initialization.

Table 6: Portfolio optimization results for the *training gross* objective (costs omitted from loss), aggregated over five random seeds (mean ±\pm std).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Universe | Feasible Set | Method | Sharpe Ratio (Net) | Turnover |
| Global | Δ\Delta | Softmax | 0.03​(±0.29)0.03\,(\pm 0.29) | 0.27​(±0.04)0.27\,(\pm 0.04) |
| O-Proj | 0.15​(±0.32)0.15\,(\pm 0.32) | 0.23​(±0.05)0.23\,(\pm 0.05) |
| Soft-Radial | 0.55​(±0.04)0.55\,(\pm 0.04) | 0.06​(±0.02)0.06\,(\pm 0.02) |
| Global | c=0.15c=0.15 | O-Proj | 0.33​(±0.13)0.33\,(\pm 0.13) | 0.15​(±0.01)0.15\,(\pm 0.01) |
| DC3 | 0.34​(±0.14)0.34\,(\pm 0.14) | 0.19​(±0.01)0.19\,(\pm 0.01) |
| HardNet | 0.43​(±0.13)0.43\,(\pm 0.13) | 0.17​(±0.02)0.17\,(\pm 0.02) |
| Soft-Radial | 0.60​(±0.09)0.60\,(\pm 0.09) | 0.06​(±0.02)0.06\,(\pm 0.02) |
| Liquid | Δ\Delta | Softmax | 0.61​(±0.32)0.61\,(\pm 0.32) | 0.22​(±0.05)0.22\,(\pm 0.05) |
| O-Proj | 0.44​(±0.25)0.44\,(\pm 0.25) | 0.44​(±0.02)0.44\,(\pm 0.02) |
| Soft-Radial | 0.87​(±0.03)0.87\,(\pm 0.03) | 0.09​(±0.01)0.09\,(\pm 0.01) |
| Liquid | c=0.05c=0.05 | O-Proj | 0.56​(±0.12)0.56\,(\pm 0.12) | 0.20​(±0.01)0.20\,(\pm 0.01) |
| DC3 | 0.49​(±0.18)0.49\,(\pm 0.18) | 0.23​(±0.02)0.23\,(\pm 0.02) |
| HardNet | 0.59​(±0.19)0.59\,(\pm 0.19) | 0.20​(±0.01)0.20\,(\pm 0.01) |
| Soft-Radial | 0.87​(±0.02)0.87\,(\pm 0.02) | 0.07​(±0.01)0.07\,(\pm 0.01) |
| Sectors | Δ\Delta | Softmax | 0.39​(±0.16)0.39\,(\pm 0.16) | 0.26​(±0.04)0.26\,(\pm 0.04) |
| O-Proj | 0.56​(±0.14)0.56\,(\pm 0.14) | 0.23​(±0.02)0.23\,(\pm 0.02) |
| Soft-Radial | 0.74​(±0.04)0.74\,(\pm 0.04) | 0.11​(±0.02)0.11\,(\pm 0.02) |
| Sectors | c=0.5c=0.5 | O-Proj | 0.58​(±0.08)0.58\,(\pm 0.08) | 0.21​(±0.03)0.21\,(\pm 0.03) |
| DC3 | 0.55​(±0.07)0.55\,(\pm 0.07) | 0.20​(±0.02)0.20\,(\pm 0.02) |
| HardNet | 0.63​(±0.07)0.63\,(\pm 0.07) | 0.20​(±0.03)0.20\,(\pm 0.03) |
| Soft-Radial | 0.75​(±0.05)0.75\,(\pm 0.05) | 0.13​(±0.02)0.13\,(\pm 0.02) |
| Sectors | c=0.15c=0.15 | O-Proj | 0.73​(±0.10)0.73\,(\pm 0.10) | 0.09​(±0.00)0.09\,(\pm 0.00) |
| DC3 | 0.72​(±0.02)0.72\,(\pm 0.02) | 0.07​(±0.00)0.07\,(\pm 0.00) |
| HardNet | 0.82​(±0.05)0.82\,(\pm 0.05) | 0.07​(±0.01)0.07\,(\pm 0.01) |
| Soft-Radial | 0.82​(±0.03)0.82\,(\pm 0.03) | 0.03​(±0.01)0.03\,(\pm 0.01) |




Table 7: Portfolio optimization results for the *training net* objective (costs included in loss), aggregated over five random seeds (mean ±\pm std).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Universe | Feasible Set | Method | Sharpe Ratio (Net) | Turnover |
| Global | Δ\Delta | Softmax | 0.21​(±0.29)0.21\,(\pm 0.29) | 0.31​(±0.04)0.31\,(\pm 0.04) |
| O-Proj | 0.27​(±0.20)0.27\,(\pm 0.20) | 0.20​(±0.03)0.20\,(\pm 0.03) |
| Soft-Radial | 0.68​(±0.09)0.68\,(\pm 0.09) | 0.05​(±0.03)0.05\,(\pm 0.03) |
| Global | c=0.15c=0.15 | O-Proj | 0.49​(±0.18)0.49\,(\pm 0.18) | 0.17​(±0.02)0.17\,(\pm 0.02) |
| DC3 | 0.38​(±0.15)0.38\,(\pm 0.15) | 0.18​(±0.02)0.18\,(\pm 0.02) |
| HardNet | 0.44​(±0.13)0.44\,(\pm 0.13) | 0.16​(±0.02)0.16\,(\pm 0.02) |
| Soft-Radial | 0.68​(±0.05)0.68\,(\pm 0.05) | 0.05​(±0.01)0.05\,(\pm 0.01) |
| Liquid | Δ\Delta | Softmax | 0.63​(±0.19)0.63\,(\pm 0.19) | 0.22​(±0.05)0.22\,(\pm 0.05) |
| O-Proj | 0.25​(±0.18)0.25\,(\pm 0.18) | 0.48​(±0.02)0.48\,(\pm 0.02) |
| Soft-Radial | 0.90​(±0.03)0.90\,(\pm 0.03) | 0.06​(±0.00)0.06\,(\pm 0.00) |
| Liquid | c=0.05c=0.05 | O-Proj | 0.64​(±0.09)0.64\,(\pm 0.09) | 0.22​(±0.01)0.22\,(\pm 0.01) |
| DC3 | 0.63​(±0.08)0.63\,(\pm 0.08) | 0.23​(±0.01)0.23\,(\pm 0.01) |
| HardNet | 0.62​(±0.11)0.62\,(\pm 0.11) | 0.19​(±0.01)0.19\,(\pm 0.01) |
| Soft-Radial | 0.90​(±0.02)0.90\,(\pm 0.02) | 0.05​(±0.00)0.05\,(\pm 0.00) |
| Sectors | Δ\Delta | Softmax | 0.43​(±0.24)0.43\,(\pm 0.24) | 0.25​(±0.04)0.25\,(\pm 0.04) |
| O-Proj | 0.68​(±0.21)0.68\,(\pm 0.21) | 0.21​(±0.03)0.21\,(\pm 0.03) |
| Soft-Radial | 0.76​(±0.04)0.76\,(\pm 0.04) | 0.09​(±0.03)0.09\,(\pm 0.03) |
| Sectors | c=0.5c=0.5 | O-Proj | 0.73​(±0.23)0.73\,(\pm 0.23) | 0.18​(±0.02)0.18\,(\pm 0.02) |
| DC3 | 0.72​(±0.08)0.72\,(\pm 0.08) | 0.17​(±0.02)0.17\,(\pm 0.02) |
| HardNet | 0.66​(±0.08)0.66\,(\pm 0.08) | 0.19​(±0.03)0.19\,(\pm 0.03) |
| Soft-Radial | 0.77​(±0.07)0.77\,(\pm 0.07) | 0.12​(±0.02)0.12\,(\pm 0.02) |
| Sectors | c=0.15c=0.15 | O-Proj | 0.80​(±0.06)0.80\,(\pm 0.06) | 0.09​(±0.01)0.09\,(\pm 0.01) |
| DC3 | 0.78​(±0.06)0.78\,(\pm 0.06) | 0.07​(±0.00)0.07\,(\pm 0.00) |
| HardNet | 0.84​(±0.02)0.84\,(\pm 0.02) | 0.06​(±0.01)0.06\,(\pm 0.01) |
| Soft-Radial | 0.87​(±0.04)0.87\,(\pm 0.04) | 0.02​(±0.00)0.02\,(\pm 0.00) |

### C.5 Extended Analysis: Ride-Sharing Dispatch

Our taxi dataset is derived from the publicly available records of the NYC Taxi and Limousine Commission (TLC) for the period of January to June 2024. To ensure a robust evaluation of temporal generalization, the data is split chronologically into 70% training, 15% validation, and 15% testing sets. To capture the multi-scale periodicity of urban mobility, we represent temporal states using cyclical sine-cosine encodings for both daily and weekly cycles. Unlike categorical indicators that create artificial boundaries at midnight, this continuous representation allows the policy network gθg\_{\theta} to learn smooth, time-dependent transition boundaries. This enables the model to proactively align fleet distribution with anticipated demand peaks, maximizing the global served rate within the constraints of the time-varying supply StS\_{t}.

In Section [5](https://arxiv.org/html/2602.03461v1#S5 "5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning") (Table [2](https://arxiv.org/html/2602.03461v1#S5.T2 "Table 2 ‣ 5.3 Ride-Sharing Dispatch ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning")), we presented results for an MLP model subject to the scaled capped simplex with κ=0.1\kappa=0.1. Here, we introduce a more challenging experimental setting with κ=0.02\kappa=0.02. This tighter constraint creates a significantly more difficult allocation problem, requiring the distribution of the fleet across all N=150N=150 zones with strictly limited per-zone capacity. For completeness, we also provide results for projection onto the standard simplex. While this baseline serves as a reference point consistent with Table [2](https://arxiv.org/html/2602.03461v1#S5.T2 "Table 2 ‣ 5.3 Ride-Sharing Dispatch ‣ 5 Numerical Experiments ‣ Soft-Radial Projection for Constrained End-to-End Learning"), we observe a clear deterioration in performance for the constrained models under this stricter regime, characterized by a lower volume of served customers (cf. Table [8](https://arxiv.org/html/2602.03461v1#A3.T8 "Table 8 ‣ C.5 Extended Analysis: Ride-Sharing Dispatch ‣ Appendix C Extended Numerical Results ‣ Soft-Radial Projection for Constrained End-to-End Learning")). Consistent with the less constrained objective, most methods perform equivalently, with the notable exception of the orthogonal projection. These findings suggest that across the set of projection methods, performance is heavily influenced by data noise and model complexity.

Table 8: Ride sharing dispatch results aggregated over five random seeds (mean ±\pm std).

|  |  |  |
| --- | --- | --- |
| Feasible Set | Method | Served Rate |
| Δ\Delta | Softmax | 0.83​(±0.00)0.83\,(\pm 0.00) |
| κ=0.02\kappa=0.02 | O-Proj | 0.64​(±0.00)0.64\,(\pm 0.00) |
| DC3 | 0.69​(±0.00)0.69\,(\pm 0.00) |
| HardNet | 0.69​(±0.00)0.69\,(\pm 0.00) |
| Soft-Radial | 0.69​(±0.00)0.69\,(\pm 0.00) |