---
authors:
- Matthew Willetts
doc_id: arxiv:2603.05326v1
family_id: arxiv:2603.05326
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market
  Makers
url_abs: http://arxiv.org/abs/2603.05326v1
url_html: https://arxiv.org/html/2603.05326v1
venue: arXiv q-fin
version: 1
year: 2026
---


Matthew Willetts

###### Abstract

In Temporal Function Market Making (TFMM), a dynamic weight AMM pool rebalances from initial to final holdings by creating a series of arbitrage opportunities whose total cost depends on the weight trajectory taken.
We show that the per-step arbitrage loss is the KL divergence between new and old weight vectors, meaning the Fisher–Rao metric is the natural Riemannian metric on the weight simplex.
The loss-minimising interpolation under the leading-order expansion of this KL cost is SLERP (Spherical Linear Interpolation) in the Hellinger coordinates ηi=wi\eta\_{i}=\sqrt{w\_{i}}, i.e. a geodesic on the positive orthant of the unit sphere traversed at constant speed.
The SLERP midpoint equals the (AM+GM)/normalise heuristic of prior work [[1](#bib.bib1)], so the heuristic lies on the geodesic.
This identity holds for any number of tokens and any magnitude of weight change; using this link, all dyadic points on the geodesic can be reached by recursive AM-GM bisection without trigonometric functions.
SLERP’s relative sub-optimality on the full KL cost is proportional to the squared magnitude of the overall weight change and to 1/f21/f^{2}, where ff is the number of interpolation steps.

## 1 Introduction

Dynamic AMM pools rebalance their holdings by introducing arbitrage opportunities that disappear once reserves match the desired target.
In Temporal Function Market Making (TFMM) [[2](#bib.bib2)], this rebalancing is driven by changing the weights of a geometric mean market maker (G3M) pool from block to block.

The pool’s asset management strategy produces new target weights at a given cadence.111This can be any long-only zero-leverage strategy, for example: track a market-cap weighted index, or a trend-following strategy.
Spreading a weight update over multiple intermediate steps reduces the total arbitrage cost [[2](#bib.bib2)], so the pool interpolates towards the target.

Prior work [[1](#bib.bib1)] derived the optimal weight midpoint for a weight change in the limit of small steps, and from this obtained approximately-optimal trajectories using arithmetic and geometric mean interpolation: the (AM+GM)/normalise heuristic.
This heuristic captures ∼95%{\sim}95\% of the improvement available from full numerical optimisation, but the geometric reason for its effectiveness was left unexplained.

This paper provides that explanation.
We show that:

* •

  The per-step arbitrage loss is a KL divergence between weight vectors (Theorem [1](#Thmtheorem1 "Theorem 1 (Arbitrage loss as KL divergence). ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")), making the Fisher–Rao metric the natural Riemannian structure on the weight
  simplex.
* •

  The loss-minimising interpolation under the leading-order expansion is SLERP (Spherical Linear Interpolation) [[3](#bib.bib3)] in Hellinger coordinates (Corollary [2](#Thmcorollary2 "Corollary 2 (SLERP optimality). ‣ 4 SLERP on the sphere under Hellinger embedding ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).
* •

  The SLERP midpoint equals the (AM+GM)/normalise midpoint exactly, for any number of tokens (Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")), explaining why the heuristic works.
* •

  A trig-free recursive bisection algorithm computes exact SLERP trajectories at power-of-two step counts (Corollary [3](#Thmcorollary3 "Corollary 3 (Trig-free SLERP via recursive bisection). ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).
* •

  SLERP’s sub-optimality on the exact KL cost is bounded at O​(Ω4/f3)O(\Omega^{4}/f^{3}) (Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 6 Bounding SLERP’s sub-optimality on the exact KL cost ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).

We validate these results numerically in §[7](#S7 "7 Experiments ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers").

## 2 Background

### 2.1 Dynamic Weight Automated Market Makers

#### Arbitrage in Geometric Mean Market Makers when weights change

Consider an NN-token G3M pool with weights 𝐰=(w1,…,wN)\boldsymbol{\mathbf{w}}=(w\_{1},\ldots,w\_{N}) on the simplex (∑iwi=1\sum\_{i}w\_{i}=1, wi>0w\_{i}>0) and reserves 𝐑∈ℝ+N\boldsymbol{\mathbf{R}}\in\mathbb{R}^{N}\_{+}.
The pool invariant is ∏iRiwi=k\prod\_{i}R\_{i}^{w\_{i}}=k [[4](#bib.bib4), [5](#bib.bib5)].
When the pool is in equilibrium, its quoted prices match market prices.

When weights change directly from 𝐰start\boldsymbol{\mathbf{w}}^{\mathrm{start}} to 𝐰end\boldsymbol{\mathbf{w}}^{\mathrm{end}} at constant market prices, an arbitrage opportunity is created.
After arbitrage, the reserves satisfy [[1](#bib.bib1)]

|  |  |  |  |
| --- | --- | --- | --- |
|  | Riend=Ristart​wiendwistart​∏j=1N(wjstartwjend)wjend.R\_{i}^{\mathrm{end}}=R\_{i}^{\mathrm{start}}\frac{w\_{i}^{\mathrm{end}}}{w\_{i}^{\mathrm{start}}}\prod\_{j=1}^{N}\left(\frac{w\_{j}^{\mathrm{start}}}{w\_{j}^{\mathrm{end}}}\right)^{w\_{j}^{\mathrm{end}}}. |  | (1) |

#### Approximately Optimal Weight Interpolations

Within each block-to-block step, market prices are modelled as constant.
If, instead of updating weights directly from 𝐰start\boldsymbol{\mathbf{w}}^{\mathrm{start}} to 𝐰end\boldsymbol{\mathbf{w}}^{\mathrm{end}} in one step (i.e. across two blocks), the pool goes via an intermediate value 𝐰~\tilde{\boldsymbol{\mathbf{w}}} (i.e. across three blocks), so that it is arbitraged twice, 𝐰start→𝐰~→𝐰end\boldsymbol{\mathbf{w}}^{\mathrm{start}}\rightarrow\tilde{\boldsymbol{\mathbf{w}}}\rightarrow\boldsymbol{\mathbf{w}}^{\mathrm{end}}, the total cost paid to arbitrageurs is reduced [[2](#bib.bib2)].
𝐰~\tilde{\boldsymbol{\mathbf{w}}} can take a broad range of possible values and still improve the pool’s performance.
Dividing up a weight change in this way is beneficial for the same reason that splitting a large order reduces market impact: each sub-step faces a smaller price displacement (Figure [1](#S2.F1 "Figure 1 ‣ Approximately Optimal Weight Interpolations ‣ 2.1 Dynamic Weight Automated Market Makers ‣ 2 Background ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).

![Refer to caption](2603.05326v1/x1.png)


Figure 1: Why weight interpolation reduces rebalancing cost.
(a) For a G3M pool, rebalancing cost is quadratic in the weight change Δ​w\Delta w, so splitting into ff equal sub-steps of Δ​w/f\Delta w/f reduces total cost by a factor of ff.
(b) The quadratic cost curve is flat near the origin: small weight changes cost almost nothing, while a single large change incurs a disproportionately high arb loss.

If we assume that the weight change from 𝐰start→𝐰end\boldsymbol{\mathbf{w}}^{\mathrm{start}}\rightarrow\boldsymbol{\mathbf{w}}^{\mathrm{end}} is small, one can obtain that the optimal intermediate weights for the two-step process are

|  |  |  |  |
| --- | --- | --- | --- |
|  | w~i∗=wi​(tf)W0​(e​wi​(tf)wi​(t0))\tilde{w}\_{i}^{\*}=\frac{w\_{i}(t\_{f})}{W\_{0}\left(\frac{ew\_{i}(t\_{f})}{w\_{i}(t\_{0})}\right)} |  | (2) |

where W0​(⋅)W\_{0}(\cdot) is the principal branch of the Lambert W function and ee is Euler’s constant [[1](#bib.bib1)].

From bounding this result from above and below by the arithmetic and geometric means respectively, one can obtain an approximately-optimal ff-step weight trajectory {𝐰˘​(tk)}k=1,…,f−1\{\breve{\boldsymbol{\mathbf{w}}}(t\_{k})\}\_{k=1,...,f-1} from 𝐰​(t0)=𝐰start\boldsymbol{\mathbf{w}}(t\_{0})=\boldsymbol{\mathbf{w}}^{\mathrm{start}} to 𝐰​(tf)=𝐰end\boldsymbol{\mathbf{w}}(t\_{f})=\boldsymbol{\mathbf{w}}^{\mathrm{end}} as the average of the linear interpolation between these values and the geometric interpolation between these values [[1](#bib.bib1)]:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | wiAM​(tk)\displaystyle w\_{i}^{\mathrm{AM}}(t\_{k}) | =(1−kf)​wi​(t0)+kf​wi​(tf),\displaystyle=(1-\frac{k}{f})w\_{i}(t\_{0})+\frac{k}{f}w\_{i}(t\_{f}), |  | (3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | wiGM​(tk)\displaystyle w\_{i}^{\mathrm{GM}}(t\_{k}) | =(wi​(t0))(1−kf)​(wi​(tf))kf,\displaystyle={(w\_{i}(t\_{0}))^{(1-\frac{k}{f})}(w\_{i}(t\_{f}))^{\frac{k}{f}}}, |  | (4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | w˘i​(tk)\displaystyle\breve{w}\_{i}(t\_{k}) | =wiAM​(tk)+wiGM​(tk)∑j=1N(wjAM​(tk)+wjGM​(tk)).\displaystyle=\frac{w\_{i}^{\mathrm{AM}}(t\_{k})+w\_{i}^{\mathrm{GM}}(t\_{k})}{\sum\_{j=1}^{N}\left({w\_{j}^{\mathrm{AM}}(t\_{k})+w\_{j}^{\mathrm{GM}}(t\_{k})}\right)}. |  | (5) |

### 2.2 Information Geometry and the Fisher–Rao metric

The probability simplex ΔN−1={𝐩∈ℝ+N:∑ipi=1}\Delta^{N-1}=\{\mathbf{p}\in\mathbb{R}^{N}\_{+}:\sum\_{i}p\_{i}=1\} carries a natural Riemannian structure induced by the Kullback–Leibler (KL) divergence.
For two distributions p,q∈ΔN−1p,q\in\Delta^{N-1}, the KL divergence

|  |  |  |
| --- | --- | --- |
|  | DKL​(p∥q)=∑ipi​log⁡(pi/qi)D\_{\mathrm{KL}}(p\,\|\,q)=\sum\_{i}p\_{i}\log(p\_{i}/q\_{i}) |  |

is asymmetric and does not satisfy the triangle inequality, so it
is not itself a metric.
Its local second-order expansion, however, around q=pq=p yields a positive-definite quadratic form,

|  |  |  |  |
| --- | --- | --- | --- |
|  | DKL​(p∥p+d​p)=12​∑i=1N(d​pi)2pi+O​(‖d​p‖3).D\_{\mathrm{KL}}(p\,\|\,p+\mathrm{d}p)\;=\;\tfrac{1}{2}\sum\_{i=1}^{N}\frac{(\mathrm{d}p\_{i})^{2}}{p\_{i}}\;+\;O(\|\mathrm{d}p\|^{3}). |  | (6) |

This expansion defines the *Fisher–Rao metric* gg. On the ambient space ℝ+N\mathbb{R}^{N}\_{+}, the metric is diagonal, gi​j​(p)=δi​j/pig\_{ij}(p)=\delta\_{ij}/p\_{i}, with the corresponding squared infinitesimal line element,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​s2=∑i=1N(d​pi)2pi.\mathrm{d}s^{2}=\sum\_{i=1}^{N}\frac{(\mathrm{d}p\_{i})^{2}}{p\_{i}}. |  | (7) |

The geometry of the simplex (ΔN−1,g)(\Delta^{N-1},g) is that of the positive orthant of an (N−1N-1)-sphere.
By the theorem of Chentsov [[6](#bib.bib6)], this is the unique Riemannian metric (up to a scale factor) invariant under sufficient statistics, establishing it as the natural information geometry of the simplex.

## 3 Arbitrage loss is a KL divergence

###### Proposition 1.

[Retention Ratio]
For an NN-asset G3M pool with weights changing from 𝐰start\boldsymbol{\mathbf{w}}^{\mathrm{start}} one block to 𝐰end\boldsymbol{\mathbf{w}}^{\mathrm{end}} the next block, with zero fees, perfect arbitrage and, constant prices, the ratio of initial value to final value of the pool is the retention ratio

|  |  |  |  |
| --- | --- | --- | --- |
|  | r:=∏j=1N(wjstartwjend)wjend.r:=\prod\_{j=1}^{N}\left(\frac{w\_{j}^{\mathrm{start}}}{w\_{j}^{\mathrm{end}}}\right)^{w\_{j}^{\mathrm{end}}}. |  | (8) |

###### Proof.

See Appendix [A.1](#A1.SS1 "A.1 Deferred Proof: Proposition 1 [Retention ratio] ‣ Appendix A Retention Ratio ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers").
∎

###### Theorem 1 (Arbitrage loss as KL divergence).

The log-loss from a weight update is the KL divergence between new and old weights:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −log⁡r=∑i=1Nwiend​log⁡wiendwistart=DKL​(𝐰end∥𝐰start).-\log r=\sum\_{i=1}^{N}w\_{i}^{\mathrm{end}}\log\!\frac{w\_{i}^{\mathrm{end}}}{w\_{i}^{\mathrm{start}}}=D\_{\mathrm{KL}}\!\left(\boldsymbol{\mathbf{w}}^{\mathrm{end}}\,\|\,\boldsymbol{\mathbf{w}}^{\mathrm{start}}\right). |  | (9) |

In particular, r≤1r\leq 1 with equality if and only if 𝐰end=𝐰start\boldsymbol{\mathbf{w}}^{\mathrm{end}}=\boldsymbol{\mathbf{w}}^{\mathrm{start}}, since DKL≥0D\_{\mathrm{KL}}\geq 0.

###### Proof.

Taking −log-\log of Eq ([8](#S3.E8 "In Proposition 1. ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) and recognising the definition of DKLD\_{\mathrm{KL}}. Non-negativity follows from Gibbs’ inequality.
∎

The weight vectors have the properties of distributions on the token set, and this identification holds for weight changes of any magnitude.
The Fisher–Rao metric is the Hessian of the KL divergence at the diagonal [[7](#bib.bib7)]; its quadratic form gives the loss kernel (Eq ([10](#S3.E10 "In Corollary 1. ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) below).

###### Corollary 1.

[Quadratic loss kernel]
For small weight changes Δ​wi=wiend−wistart\Delta w\_{i}=w\_{i}^{\mathrm{end}}-w\_{i}^{\mathrm{start}}, the leading-order loss is

|  |  |  |  |
| --- | --- | --- | --- |
|  | −log⁡r≈∑i=1N(Δ​wi)22​wi.-\log r\;\approx\;\sum\_{i=1}^{N}\frac{(\Delta w\_{i})^{2}}{2\,w\_{i}}. |  | (10) |

###### Proof.

Taylor-expand Theorem [1](#Thmtheorem1 "Theorem 1 (Arbitrage loss as KL divergence). ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") to second order; the linear term vanishes by the simplex constraint (Appendix [A.2](#A1.SS2 "A.2 Deferred Proof: Corollary 1 [Quadratic loss kernel] ‣ Appendix A Retention Ratio ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).
∎

This is half the Fisher–Rao quadratic form, and it defines the infinitesimal line element on the weight simplex.

#### The Hellinger embedding and geodesics

The coordinate transformation ηi=wi\eta\_{i}=\sqrt{w\_{i}} maps ΔN−1\Delta^{N-1} isometrically (up to a factor) onto the positive orthant of the unit sphere S+N−1S^{N-1}\_{+}, under which the Fisher–Rao metric reduces to a multiple of the round metric.222This map wi↦wiw\_{i}\mapsto\sqrt{w\_{i}} is the *Hellinger embedding* [[7](#bib.bib7)].
Geodesics on the sphere are great circles, computable in closed form via spherical linear interpolation (SLERP) [[3](#bib.bib3)].
We exploit this correspondence throughout: interpolation is performed on S+N−1S^{N-1}\_{+} and mapped back to weights by squaring.

The metric, Eq ([7](#S2.E7 "In 2.2 Information Geometry and the Fisher–Rao metric ‣ 2 Background ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")), simplifies under the coordinate change

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηi=wi,so thatwi=ηi2,d​wi=2​ηi​d​ηi,\eta\_{i}=\sqrt{w\_{i}},\qquad\text{so that}\qquad w\_{i}=\eta\_{i}^{2},\quad\mathrm{d}w\_{i}=2\eta\_{i}\,\mathrm{d}\eta\_{i}, |  | (11) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇒d​s2=∑i=1N4​ηi2​(d​ηi)2ηi2=4​∑i=1N(d​ηi)2.\Rightarrow\mathrm{d}s^{2}=\sum\_{i=1}^{N}\frac{4\eta\_{i}^{2}\,(\mathrm{d}\eta\_{i})^{2}}{\eta\_{i}^{2}}=4\sum\_{i=1}^{N}(\mathrm{d}\eta\_{i})^{2}. |  | (12) |

The per-step loss, Eq ([10](#S3.E10 "In Corollary 1. ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")), is therefore 12​d​s2=2​∑i(d​ηi)2\tfrac{1}{2}\,\mathrm{d}s^{2}=2\sum\_{i}(\mathrm{d}\eta\_{i})^{2}: half the Fisher–Rao quadratic form evaluated on the unit sphere.
The constraint ∑iwi=1\sum\_{i}w\_{i}=1 becomes ∑iηi2=1\sum\_{i}\eta\_{i}^{2}=1: the point 𝜼=(η1,…,ηN)\boldsymbol{\mathbf{\eta}}=(\eta\_{1},\ldots,\eta\_{N}) lies on the positive orthant of the unit sphere SN−1S^{N-1}.
The metric is 4×4\times the round metric inherited from the ambient Euclidean space ℝN\mathbb{R}^{N}.
Figure [2](#S3.F2 "Figure 2 ‣ The Hellinger embedding and geodesics ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") illustrates this correspondence.

![Refer to caption](2603.05326v1/x2.png)


Figure 2: The Hellinger embedding maps the weight simplex ΔN−1\Delta^{N-1} to the positive orthant of the unit sphere S+N−1S^{N-1}\_{+} via ηi=wi\eta\_{i}=\sqrt{w\_{i}}.
Under this isometry, the Fisher–Rao metric becomes a scaling of the standard round metric, and geodesics (shortest paths under the arbitrage cost) become great circles, computable in closed form via SLERP.

## 4 SLERP on the sphere under Hellinger embedding

We derive the weight interpolation that minimises the quadratic loss (Eq ([10](#S3.E10 "In Corollary 1. ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers"))).

###### Corollary 2 (SLERP optimality).

Among all ff-step paths 𝐰​(t0),𝐰​(t1),…,𝐰​(tf)\boldsymbol{\mathbf{w}}(t\_{0}),\boldsymbol{\mathbf{w}}(t\_{1}),\ldots,\boldsymbol{\mathbf{w}}(t\_{f}) on the simplex from 𝐰start\boldsymbol{\mathbf{w}}^{\mathrm{start}} to 𝐰end\boldsymbol{\mathbf{w}}^{\mathrm{end}}, the one that minimises the total quadratic loss ∑k=1f∑i(Δ​wi(k))2/(2​wi(k−1))\sum\_{k=1}^{f}\sum\_{i}(\Delta w\_{i}^{(k)})^{2}/(2\,w\_{i}^{(k-1)}) is the constant-speed geodesic of the Fisher–Rao metric: SLERP in Hellinger coordinates.
Each step incurs equal loss 2​Ω2/f22\Omega^{2}/f^{2}, where Ω=arccos⁡(∑i=1Nwistart​wiend)\Omega=\arccos\!\left(\sum\_{i=1}^{N}\sqrt{w\_{i}^{\mathrm{start}}\,w\_{i}^{\mathrm{end}}}\right), giving total loss 2​Ω2/f2\Omega^{2}/f.

###### Proof.

The quadratic loss per step is the squared arc-length under 12​g\tfrac{1}{2}g.
By convexity of x↦x2x\mapsto x^{2}, the total loss ∑k=1f(d​sk)2≥S2/f\sum\_{k=1}^{f}(\mathrm{d}s\_{k})^{2}\geq S^{2}/f for any path of total arc-length SS, with equality if and only if all steps are equal (Appendix [B](#A2 "Appendix B Deferred proof: Constant metric speed minimises total loss (used in Corollary 2) ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).
The minimum over paths is attained by the geodesic (shortest SS). Under the Hellinger embedding (§[3](#S3.SS0.SSS0.Px1 "The Hellinger embedding and geodesics ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")), the metric is the scaled round metric on S+N−1S^{N-1}\_{+}, whose geodesics are great circles parameterised at constant angular velocity, that is: SLERP [[3](#bib.bib3)].
∎

### 4.1 The SLERP formula

Given start weights 𝐰start\boldsymbol{\mathbf{w}}^{\mathrm{start}} and end weights 𝐰end\boldsymbol{\mathbf{w}}^{\mathrm{end}}, the loss-minimising multi-step interpolation proceeds as in Algorithm [1](#alg1 "Algorithm 1 ‣ 4.1 The SLERP formula ‣ 4 SLERP on the sphere under Hellinger embedding ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers").

Algorithm 1  SLERP weight interpolation on the positive sphere

0: Start weights 𝐰start∈ΔN−1\mathbf{w}^{\mathrm{start}}\in\Delta^{N-1}, end weights 𝐰end∈ΔN−1\mathbf{w}^{\mathrm{end}}\in\Delta^{N-1}, number of steps ff

0: Interpolated weight sequence 𝐰​(0),𝐰​(1),…,𝐰​(f)\mathbf{w}(0),\mathbf{w}(1),\ldots,\mathbf{w}(f)

1: Map to the sphere:

2: 𝜼start←(w1start,…,wNstart)\boldsymbol{\eta}^{\mathrm{start}}\leftarrow\left(\sqrt{w\_{1}^{\mathrm{start}}},\,\ldots,\,\sqrt{w\_{N}^{\mathrm{start}}}\right)

3: 𝜼end←(w1end,…,wNend)\boldsymbol{\eta}^{\mathrm{end}}\leftarrow\left(\sqrt{w\_{1}^{\mathrm{end}}},\,\ldots,\,\sqrt{w\_{N}^{\mathrm{end}}}\right)

4: Compute geodesic angle:

5: Ω←arccos⁡(∑i=1Nwistart​wiend)\Omega\leftarrow\arccos\!\left(\sum\_{i=1}^{N}\sqrt{w\_{i}^{\mathrm{start}}\,w\_{i}^{\mathrm{end}}}\right) {Bhattacharyya coefficient}

6: SLERP interpolation:

7: for k=0,1,…,fk=0,1,\ldots,f do

8:  t←k/ft\leftarrow k/f

9:  𝜼​(t)←sin⁡((1−t)​Ω)sin⁡Ω​𝜼start+sin⁡(t​Ω)sin⁡Ω​𝜼end\boldsymbol{\eta}(t)\leftarrow\dfrac{\sin\!\left((1-t)\,\Omega\right)}{\sin\Omega}\,\boldsymbol{\eta}^{\mathrm{start}}+\dfrac{\sin\!\left(t\,\Omega\right)}{\sin\Omega}\,\boldsymbol{\eta}^{\mathrm{end}}

10:  Map back to weights: wi​(k)←[ηi​(t)]2w\_{i}(k)\leftarrow\left[\eta\_{i}(t)\right]^{2} for i=1,…,Ni=1,\ldots,N

11: end for

As established in Corollary [2](#Thmcorollary2 "Corollary 2 (SLERP optimality). ‣ 4 SLERP on the sphere under Hellinger embedding ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers"), consecutive points on the SLERP path are separated by a constant angular increment of Ω/f\Omega/f, giving per-step loss

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒk=(d​sk)2=2​Ω2f2\mathcal{L}\_{k}=(\mathrm{d}s\_{k})^{2}=\frac{2\Omega^{2}}{f^{2}} |  | (13) |

for all kk, and total loss ℒtotal=2​Ω2/f\mathcal{L}\_{\mathrm{total}}=2\Omega^{2}/f, which decreases as 1/f1/f with the number of steps.

### 4.2 Two-token case

For N=2N=2 tokens with weights (w, 1−w)(w,\,1-w), the sphere S1S^{1} is a quarter-circle in the positive quadrant.
The Hellinger embedding maps w↦(w,1−w)w\mapsto(\sqrt{w},\,\sqrt{1-w}), parameterised by a single angle θ=arcsin⁡(w)\theta=\arcsin(\sqrt{w}).
SLERP reduces to linear interpolation in θ\theta:

|  |  |  |  |
| --- | --- | --- | --- |
|  | w​(k)=sin2⁡(θstart+kf​(θend−θstart)),w(k)=\sin^{2}\!\left(\theta^{\mathrm{start}}+\frac{k}{f}\left(\theta^{\mathrm{end}}-\theta^{\mathrm{start}}\right)\right), |  | (14) |

where θstart=arcsin⁡(wstart)\theta^{\mathrm{start}}=\arcsin(\sqrt{w^{\mathrm{start}}}) and θend=arcsin⁡(wend)\theta^{\mathrm{end}}=\arcsin(\sqrt{w^{\mathrm{end}}}).

## 5 SLERP midpoint equals (AM+GM)/normalise midpoint

Does the prior (AM+GM)/normalise heuristic [[1](#bib.bib1)], Eq ([5](#S2.E5 "In Approximately Optimal Weight Interpolations ‣ 2.1 Dynamic Weight Automated Market Makers ‣ 2 Background ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")), connect to the SLERP geodesics?
The midpoints of the two trajectories are identical.

###### Theorem 2.

For any NN-token pool with start weights 𝐰start\boldsymbol{\mathbf{w}}^{\mathrm{start}} and end weights 𝐰end\boldsymbol{\mathbf{w}}^{\mathrm{end}}, the SLERP midpoint (𝛈​(t)←sin⁡((1−t)​Ω)sin⁡Ω​𝛈start+sin⁡(t​Ω)sin⁡Ω​𝛈end\boldsymbol{\eta}(t)\leftarrow\dfrac{\sin\!\left((1-t)\,\Omega\right)}{\sin\Omega}\,\boldsymbol{\eta}^{\mathrm{start}}+\dfrac{\sin\!\left(t\,\Omega\right)}{\sin\Omega}\,\boldsymbol{\eta}^{\mathrm{end}} at t=k/f=1/2t=k/f=1/2) is exactly equal to the (AM+GM)/normalise midpoint of [[1](#bib.bib1)].

###### Proof.

The SLERP midpoint on the sphere is

|  |  |  |
| --- | --- | --- |
|  | 𝜼mid=𝜼start+𝜼end2​cos⁡(Ω/2),\boldsymbol{\mathbf{\eta}}\_{\mathrm{mid}}=\frac{\boldsymbol{\mathbf{\eta}}^{\mathrm{start}}+\boldsymbol{\mathbf{\eta}}^{\mathrm{end}}}{2\cos(\Omega/2)}, |  |

giving weights

|  |  |  |  |
| --- | --- | --- | --- |
|  | wiSLERP=(wistart+wiend)2∑j(wjstart+wjend)2,w\_{i}^{\mathrm{SLERP}}=\frac{\left(\sqrt{w\_{i}^{\mathrm{start}}}+\sqrt{w\_{i}^{\mathrm{end}}}\right)^{2}}{\sum\_{j}\left(\sqrt{w\_{j}^{\mathrm{start}}}+\sqrt{w\_{j}^{\mathrm{end}}}\right)^{2}}, |  | (15) |

where we have used 4​cos2⁡(Ω/2)=2​(1+cos⁡Ω)=‖𝜼start+𝜼end‖24\cos^{2}(\Omega/2)=2(1+\cos\Omega)=\|\boldsymbol{\mathbf{\eta}}^{\mathrm{start}}+\boldsymbol{\mathbf{\eta}}^{\mathrm{end}}\|^{2}.
Expanding the numerator via (a+b)2=a+b+2​a​b(\sqrt{a}+\sqrt{b})^{2}=a+b+2\sqrt{ab}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (wistart+wiend)2=2​(wistart+wiend2⏟AMi+wistart​wiend⏟GMi).\left(\sqrt{w\_{i}^{\mathrm{start}}}+\sqrt{w\_{i}^{\mathrm{end}}}\right)^{2}=2\!\left(\underbrace{\frac{w\_{i}^{\mathrm{start}}+w\_{i}^{\mathrm{end}}}{2}}\_{\mathrm{AM}\_{i}}+\underbrace{\sqrt{w\_{i}^{\mathrm{start}}\,w\_{i}^{\mathrm{end}}}}\_{\mathrm{GM}\_{i}}\right). |  | (16) |

The factor of 2 cancels upon normalisation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wiSLERP=AMi+GMi∑j(AMj+GMj)=w˘i,w\_{i}^{\mathrm{SLERP}}=\frac{\mathrm{AM}\_{i}+\mathrm{GM}\_{i}}{\sum\_{j}\left(\mathrm{AM}\_{j}+\mathrm{GM}\_{j}\right)}=\breve{w}\_{i}, |  | (17) |

which is precisely the (AM+GM)/normalise formula (Eq ([5](#S2.E5 "In Approximately Optimal Weight Interpolations ‣ 2.1 Dynamic Weight Automated Market Makers ‣ 2 Background ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")), from [[1](#bib.bib1)] at t=1/2t=1/2).
∎

This identity holds for any number of tokens and any magnitude of weight change.
The heuristic midpoint is the geodesic midpoint.
See Figure [3](#S5.F3 "Figure 3 ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") for an informal visual proof.

![Refer to caption](2603.05326v1/x3.png)


Figure 3: Visual proof that the SLERP midpoint equals (AM+GM)/normalise (in the N=3 case).
To return to weight space we undo the Hellinger embedding ηi=wi\eta\_{i}=\sqrt{w\_{i}}, i.e. *square*.
Each square decomposes
(wis+wie)2=(wis+wie)+2​wis​wie=2​(AMi+GMi)(\sqrt{w\_{i}^{\mathrm{s}}}+\sqrt{w\_{i}^{\mathrm{e}}})^{2}=(w\_{i}^{\mathrm{s}}+w\_{i}^{\mathrm{e}})+2\sqrt{w\_{i}^{\mathrm{s}}\,w\_{i}^{\mathrm{e}}}=2(\mathrm{AM}\_{i}+\mathrm{GM}\_{i}).
Red diagonal blocks contribute 2​AMi2\,\mathrm{AM}\_{i}; blue off-diagonal blocks contribute 2​GMi2\,\mathrm{GM}\_{i}.
The factor of 2 cancels with normalisation, giving us the (AM+GM)/normalise heuristic exactly.

###### Corollary 3 (Trig-free SLERP via recursive bisection).

Let f=2df=2^{d} for some integer d≥1d\geq 1.
The full ff-step SLERP trajectory 𝐰​(k/f)\boldsymbol{\mathbf{w}}(k/f) for k=0,1,…,fk=0,1,\ldots,f can be computed by recursive midpoint bisection: at each level, insert the (AM+GM)/normalise midpoint between each consecutive pair of weights.
After dd levels, the resulting 2d+12^{d}+1 points lie exactly on the SLERP geodesic.

###### Proof.

SLERP restricted to any sub-arc of a great circle is itself a SLERP between the sub-arc’s endpoints.
By Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers"), the (AM+GM)/normalise midpoint equals the SLERP midpoint of that sub-arc.
The result follows by induction on the bisection depth dd.
∎

This means an on-chain implementation needs only addition, multiplication, square root, and normalisation, so no arccos\arccos or sin\sin evaluations, to produce the optimal interpolation at power-of-two step counts.

Algorithm 2  Trig-free SLERP via recursive bisection

0: Start weights 𝐰start∈ΔN−1\mathbf{w}^{\mathrm{start}}\in\Delta^{N-1}, end weights 𝐰end∈ΔN−1\mathbf{w}^{\mathrm{end}}\in\Delta^{N-1}, depth dd (gives f=2df=2^{d} steps)

0: 2d+12^{d}+1 points on the SLERP geodesic: 𝐰(0),𝐰(1),…,𝐰(2d)\mathbf{w}^{(0)},\mathbf{w}^{(1)},\ldots,\mathbf{w}^{(2^{d})}

1: Initialise list 𝒲←[𝐰start,𝐰end]\mathcal{W}\leftarrow[\mathbf{w}^{\mathrm{start}},\;\mathbf{w}^{\mathrm{end}}]

2: for level ℓ=1\ell=1 to dd do

3:  𝒲′←[]\mathcal{W}^{\prime}\leftarrow[\,]

4:  for each consecutive pair (𝐰(a),𝐰(b))(\mathbf{w}^{(a)},\mathbf{w}^{(b)}) in 𝒲\mathcal{W} do

5:   Compute midpoint: mi←wi(a)+wi(b)2+wi(a)​wi(b)m\_{i}\leftarrow\frac{w\_{i}^{(a)}+w\_{i}^{(b)}}{2}+\sqrt{w\_{i}^{(a)}\,w\_{i}^{(b)}} for each ii

6:   Normalise: m^i←mi/∑jmj\hat{m}\_{i}\leftarrow m\_{i}\,/\,\sum\_{j}m\_{j}

7:   Append 𝐰(a),𝐦^\mathbf{w}^{(a)},\;\hat{\mathbf{m}} to 𝒲′\mathcal{W}^{\prime}

8:  end for

9:  Append 𝐰end\mathbf{w}^{\mathrm{end}} to 𝒲′\mathcal{W}^{\prime}

10:  𝒲←𝒲′\mathcal{W}\leftarrow\mathcal{W}^{\prime}

11: end for

12: return 𝒲\mathcal{W}

Algorithm [2](#alg2 "Algorithm 2 ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") makes Corollary [3](#Thmcorollary3 "Corollary 3 (Trig-free SLERP via recursive bisection). ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") practical.
Each level requires only O​(N)O(N) arithmetic operations per midpoint insertion and no trigonometric functions.
Figure [4](#S5.F4 "Figure 4 ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") illustrates the construction on the Hellinger sphere.

![Refer to caption](2603.05326v1/x4.png)


Figure 4: Recursive bisection on the positive orthant of S+N−1S^{N-1}\_{+}.
At each depth dd, the (AM+GM)/normalise midpoint is inserted between every pair of adjacent points (bright green: newly inserted; dark green: inherited from previous depth).
By depth 3, the 2d+1=92^{d}+1=9 points densely trace the geodesic arc, all computed without trigonometric functions.

### 5.1 Comparison at general tt and with Lambert W

For t≠1/2t\neq 1/2, the SLERP and (AM+GM)/normalise trajectories differ.
SLERP weights at general tt are

|  |  |  |  |
| --- | --- | --- | --- |
|  | wiSLERP​(t)=[sin⁡((1−t)​Ω)sin⁡Ω​wistart+sin⁡(t​Ω)sin⁡Ω​wiend]2,w\_{i}^{\mathrm{SLERP}}(t)=\left[\frac{\sin\!\left((1-t)\,\Omega\right)}{\sin\Omega}\sqrt{w\_{i}^{\mathrm{start}}}+\frac{\sin\!\left(t\,\Omega\right)}{\sin\Omega}\sqrt{w\_{i}^{\mathrm{end}}}\right]^{\!2}, |  | (18) |

while (AM+GM)/normalise uses

|  |  |  |
| --- | --- | --- |
|  | w˘i​(t)∝(1−t)​wistart+t​wiend+(wistart)1−t​(wiend)t.\breve{w}\_{i}(t)\propto(1-t)\,w\_{i}^{\mathrm{start}}+t\,w\_{i}^{\mathrm{end}}+\left(w\_{i}^{\mathrm{start}}\right)^{1-t}\!\left(w\_{i}^{\mathrm{end}}\right)^{t}. |  |

###### Lemma 1 (Agreement at general tt).

Let ui=Δ​wi/wistartu\_{i}=\Delta w\_{i}/w\_{i}^{\mathrm{start}} where Δ​wi=wiend−wistart\Delta w\_{i}=w\_{i}^{\mathrm{end}}-w\_{i}^{\mathrm{start}}.
For any t∈[0,1]t\in[0,1], the SLERP, (AM+GM)/normalise, and Lambert W (normalised) trajectories agree through O​(u2)O(u^{2}) and first differ at O​(u3)O(u^{3}).
At the midpoint t=1/2t=1/2, SLERP and (AM+GM)/normalise agree exactly (Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).

###### Proof.

See Appendix [D](#A4 "Appendix D Taylor agreement of interpolation methods ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers").
∎

Table [1](#S5.T1 "Table 1 ‣ 5.1 Comparison at general 𝑡 and with Lambert W ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") summarises these results.
The discrepancy between SLERP / (AM+GM)/normalise and the Lambert W value arises because they optimise different objectives: Lambert W maximises the finite-step retention ratio rr, while SLERP minimises the quadratic approximation to −log⁡r-\log r.
For multi-step interpolation (large ff), the sub-optimality bound (Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 6 Bounding SLERP’s sub-optimality on the exact KL cost ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) guarantees that all three converge; the choice is practical (on-chain cost and implementation simplicity) rather than a matter of loss optimality.

Table 1: Agreement between midpoint formulae in powers of ui=Δ​wi/wiu\_{i}=\Delta w\_{i}/w\_{i}.

| Pair of methods | Midpoint | General tt |
| --- | --- | --- |
| SLERP vs (AM+GM)/normalise | Exact | Differ at O​(u3)O(u^{3}) |
| SLERP vs Lambert W (normalised) | Differ at O​(u3)O(u^{3}) | Differ at O​(u3)O(u^{3}) |
| (AM+GM)/normalise vs Lambert W (normalised) | Differ at O​(u3)O(u^{3}) | Differ at O​(u3)O(u^{3}) |

## 6 Bounding SLERP’s sub-optimality on the exact KL cost

SLERP minimises the quadratic approximation to the per-step KL cost (Corollary [2](#Thmcorollary2 "Corollary 2 (SLERP optimality). ‣ 4 SLERP on the sphere under Hellinger embedding ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).
The following theorem bounds the gap to the global optimum on the exact cost.

###### Theorem 3.

[Sub-optimality bound]
Let CSLERP​(f)C\_{\mathrm{SLERP}}(f) and C∗​(f)C\_{\*}(f) denote the total exact KL cost

|  |  |  |
| --- | --- | --- |
|  | ∑k=1fDKL​(𝐰(k)∥𝐰(k−1))\textstyle\sum\_{k=1}^{f}D\_{\mathrm{KL}}\!\left(\boldsymbol{\mathbf{w}}^{(k)}\,\|\,\boldsymbol{\mathbf{w}}^{(k-1)}\right) |  |

along the ff-step SLERP path and the globally optimal ff-step path, respectively.
For weights bounded away from zero (mini⁡wi≥ϵ>0\min\_{i}w\_{i}\geq\epsilon>0) and f≥4​Ω/ϵf\geq 4\Omega/\epsilon:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤CSLERP​(f)−C∗​(f)≤A​Ω4f3,0\;\leq\;C\_{\mathrm{SLERP}}(f)-C\_{\*}(f)\;\leq\;\frac{A\,\Omega^{4}}{f^{3}}, |  | (19) |

where AA depends on the weight configuration and ϵ\epsilon but not on ff.
The relative sub-optimality is O​(Ω2/f2)O(\Omega^{2}/f^{2}).

###### Proof.

Deferred to Appendix [C](#A3 "Appendix C Deferred proof: Theorem 3 [sub-optimality bound] ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers"). The explicit constant is A=128​N/ϵ4A=128\,N/\epsilon^{4}.
∎

Expanding the per-step KL cost beyond the quadratic approximation that SLERP minimises (Appendix [C](#A3 "Appendix C Deferred proof: Theorem 3 [sub-optimality bound] ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")), the leading remainder is Rk=−16​∑iwi​(ui(k))3+O​(u4)R\_{k}=-\frac{1}{6}\sum\_{i}w\_{i}(u\_{i}^{(k)})^{3}+O(u^{4}), which encodes the asymmetry of the KL divergence: it is negative when weights increase (ui>0u\_{i}>0, so the true KL cost is *less* than the quadratic) and positive when weights decrease.
SLERP, as the geodesic of the symmetric Fisher–Rao metric (α=0\alpha=0), treats both directions equally and does not exploit this asymmetry.
The exact KL-optimal path would take slightly larger steps where weights increase and slightly smaller steps where they decrease, but the available improvement is only O​(u2)O(u^{2}) per step, hence the bound.

For the N=3N=3 experimental setup of §[7](#S7 "7 Experiments ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") (Ω≈0.28\Omega\approx 0.28), at f=50f=50 the bound gives relative sub-optimality of O​(10−4)O(10^{-4}), consistent with the brute-force numerical results reported there.

###### Remark 1 (Lambert W midpoint as KL stationary point).

For f=2f=2, setting

|  |  |  |
| --- | --- | --- |
|  | ∂∂mi​[DKL​(𝐦∥𝐰start)+DKL​(𝐰end∥𝐦)]=0\frac{\partial}{\partial m\_{i}}\left[D\_{\mathrm{KL}}(\boldsymbol{\mathbf{m}}\,\|\,\boldsymbol{\mathbf{w}}^{\mathrm{start}})+D\_{\mathrm{KL}}(\boldsymbol{\mathbf{w}}^{\mathrm{end}}\,\|\,\boldsymbol{\mathbf{m}})\right]=0 |  |

for each component independently (ignoring the simplex constraint) yields exactly the Lambert W formula of Eq ([2](#S2.E2 "In Approximately Optimal Weight Interpolations ‣ 2.1 Dynamic Weight Automated Market Makers ‣ 2 Background ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).
The simplex constraint is then imposed by renormalisation, which is why the formula is exact only for small weight changes: the full constrained problem couples the components through a Lagrange multiplier that has no closed-form solution [[1](#bib.bib1)].
The Lambert W midpoint optimises the unconstrained component-wise KL cost, SLERP optimises the leading-order expansion of the constrained cost, and the two agree through O​(u2)O(u^{2}) (Table [1](#S5.T1 "Table 1 ‣ 5.1 Comparison at general 𝑡 and with Lambert W ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).

## 7 Experiments

We compare interpolation methods numerically using the same N=3N=3 token setup as [[1](#bib.bib1)]: 𝐰​(t0)={0.05,0.55,0.4}\boldsymbol{\mathbf{w}}(t\_{0})=\{0.05,0.55,0.4\}, 𝐰​(tf)={0.4,0.5,0.1}\boldsymbol{\mathbf{w}}(t\_{f})=\{0.4,0.5,0.1\}, f=1000f=1000 steps.

#### Weight trajectories and block-to-block changes

Weight trajectories and block-to-block changes are plotted in Appendix [G](#A7 "Appendix G Weight trajectories and block-to-block changes ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") (Figures [G.2](#A7.F2 "Figure G.2 ‣ Appendix G Weight trajectories and block-to-block changes ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") and [G.2](#A7.F2 "Figure G.2 ‣ Appendix G Weight trajectories and block-to-block changes ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).
At this scale, (AM+GM)/normalise and SLERP are visually indistinguishable, consistent with the exact midpoint equivalence (Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) and third-order agreement at general tt (§[5.1](#S5.SS1 "5.1 Comparison at general 𝑡 and with Lambert W ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).
For SLERP, block-to-block changes vary smoothly; constant metric speed in the Fisher–Rao metric does not correspond to constant weight increments in Cartesian coordinates, but the variation is small (∼10−4\sim 10^{-4}).

#### Per-step loss uniformity

![Refer to caption](2603.05326v1/slerp_perstep_loss_n3.png)


Figure 5: Per-step arbitrage loss −log⁡rk-\log r\_{k} across 1000 steps, N=3N=3 setup. Left to right: linear (std/mean =0.32=0.32), (AM+GM)/normalise (0.0860.086), SLERP (0.00020.0002). SLERP achieves near-perfect uniformity, orders of magnitude better than other methods.

Figure [5](#S7.F5 "Figure 5 ‣ Per-step loss uniformity ‣ 7 Experiments ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") shows the per-step arbitrage loss, −log⁡rk-\log r\_{k} across all 1000 steps, to directly test how different interpolation methods give different variation in loss per step.

Table 2: Per-step loss uniformity: ratio of standard deviation to mean of −log⁡rk-\log r\_{k}.

| Method | std/mean |
| --- | --- |
| Linear | 0.3236 |
| Geometric | 0.2155 |
| (AM+GM)/normalise | 0.0860 |
| SLERP | 0.0002 |

SLERP achieves near-perfect loss uniformity, Table [2](#S7.T2 "Table 2 ‣ Per-step loss uniformity ‣ 7 Experiments ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers"), consistent with it traversing the Fisher–Rao metric geodesic at constant speed.
The residual variation of 0.02%0.02\% arises from higher-order terms beyond the quadratic approximation of Eq ([10](#S3.E10 "In Corollary 1. ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).

#### Brute-force numerical verification

To verify that SLERP is near-optimal on the exact KL cost, we ran L-BFGS-B optimisation over all f−1f-1 intermediate weight vectors, initialised from the SLERP solution, for the N=3N=3 setup.
At f=1000f=1000, the optimiser converged in 29 iterations without improving the objective beyond SLERP’s value.
At f=50f=50, the optimiser achieved a retained fraction of 0.989 048 060.989\,048\,06 versus SLERP’s 0.989 047 930.989\,047\,93, a relative cost improvement of ∼1.2×10−5{\sim}1.2\times 10^{-5}, consistent with the O​(Ω2/f2)O(\Omega^{2}/f^{2}) bound of Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 6 Bounding SLERP’s sub-optimality on the exact KL cost ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers").

#### Difference between SLERP and other methods

![Refer to caption](2603.05326v1/interpolation_example_slerp/slerp_differences_combined.png)


Figure 6: Weight differences between interpolation methods. Left: SLERP minus linear (∼0.03\sim 0.03), reflecting the non-linearity of the geodesic. Centre: SLERP minus (AM+GM)/normalise (∼0.003\sim 0.003), an order of magnitude smaller, with an S-curve vanishing at both endpoints and the midpoint, consistent with Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers"). Right: brute-force optimal minus SLERP (∼10−7\sim 10^{-7}), confirming SLERP is near-optimal.

Figure [6](#S7.F6 "Figure 6 ‣ Difference between SLERP and other methods ‣ 7 Experiments ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") confirms that the SLERP-minus-linear differences are large (∼0.03\sim 0.03) with the same arch shape as the optimal-minus-linear plot in [[1](#bib.bib1)].
The SLERP-minus-(AM+GM)/normalise differences are an order of magnitude smaller (∼0.003\sim 0.003), and the differences in weights between SLERP and the brute force optimal trajectory are of order 10−710^{-7}.

#### Convergence across step counts

![Refer to caption](2603.05326v1/near_boundary_convergence_N=3_near-boundary.png)


Figure 7: N=3N=3 near-boundary configuration 𝐰:(0.01,0.01,0.98)→(0.49,0.49,0.02)\boldsymbol{\mathbf{w}}:(0.01,0.01,0.98)\to(0.49,0.49,0.02). Left: total arbitrage loss vs. step count ff for each interpolation method and the brute-force L-BFGS-B optimum. Right: relative sub-optimality (ratio of method loss to brute-force optimal loss minus one). SLERP closely tracks the brute-force optimum across all ff; linear interpolation diverges by up to ∼20%{\sim}20\% near the boundary.

Figure [7](#S7.F7 "Figure 7 ‣ Convergence across step counts ‣ 7 Experiments ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") shows total loss and relative sub-optimality as a function of the step count ff for the N=3N=3 near-boundary configuration.
SLERP closely tracks the brute-force optimal across steps, validating the O​(Ω2/f2)O(\Omega^{2}/f^{2}) sub-optimality bound of Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 6 Bounding SLERP’s sub-optimality on the exact KL cost ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers").
Linear interpolation diverges from the optimum as ff grows, incurring up to ∼20%{\sim}20\% excess loss at this near-boundary configuration.
(AM+GM)/normalise performs slightly worse than SLERP but substantially better than linear, consistent with the third-order agreement established in §[5.1](#S5.SS1 "5.1 Comparison at general 𝑡 and with Lambert W ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers").

#### Near-boundary behaviour

Current G3M implementations enforce a minimum weight of 1%1\%, so the practical boundary is wmin=0.01w\_{\min}=0.01.
At this floor the Fisher–Rao metric diverges and the quadratic approximation underlying SLERP is least accurate, making near-boundary performance an important stress test.

![Refer to caption](2603.05326v1/near_boundary_multistep.png)


Figure 8: Left: total loss at f=1000f=1000 as a function of the smallest weight wminw\_{\min}, for N=2N=2 symmetric weight changes (wmin, 1−wmin)→(1−wmin,wmin)(w\_{\min},\,1{-}w\_{\min})\to(1{-}w\_{\min},\,w\_{\min}). Right: loss ratio relative to SLERP. SLERP’s advantage over both linear and (AM+GM)/normalise grows as weights approach the boundary.

Figure [8](#S7.F8 "Figure 8 ‣ Near-boundary behaviour ‣ 7 Experiments ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") shows that SLERP’s advantage over both linear and (AM+GM)/normalise *widens* as weights approach the boundary: at wmin=0.01w\_{\min}=0.01, linear interpolation incurs ∼20%{\sim}20\% more loss than SLERP, and (AM+GM)/normalise incurs ∼3.5%{\sim}3.5\% more.
For interior weights (wmin≥0.2w\_{\min}\geq 0.2), all three methods are within 1%1\% of each other.

![Refer to caption](2603.05326v1/near_boundary_perstep_n3.png)


Figure 9: Per-step loss −log⁡rk-\log r\_{k} near the simplex boundary (N=3N=3, f=1000f=1000, 𝐰:(0.01,0.01,0.98)→(0.49,0.49,0.02)\boldsymbol{\mathbf{w}}:(0.01,0.01,0.98)\to(0.49,0.49,0.02)). SLERP achieves near-constant loss per step (std/mean =0.0011=0.0011); other methods show large variation, especially at steps where weights pass through their smallest values.

Figure [9](#S7.F9 "Figure 9 ‣ Near-boundary behaviour ‣ 7 Experiments ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") shows per-step losses for the N=3N=3 near-boundary configuration at f=1000f=1000.
SLERP maintains near-perfect uniformity (std/mean =0.0011=0.0011) even with weights at the 1%1\% floor: compare with std/mean =0.0002=0.0002 for the interior configuration of Figure [5](#S7.F5 "Figure 5 ‣ Per-step loss uniformity ‣ 7 Experiments ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers").
Linear interpolation shows extreme non-uniformity (std/mean =0.89=0.89) with a loss spike at the boundary-crossing steps.
Appendix [H](#A8 "Appendix H Near-boundary experiments ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") provides further near-boundary analysis, including a comparison of single-midpoint (f=2f=2) methods where the exact Lambert W formula of [[1](#bib.bib1)] outperforms SLERP by up to 10%10\%.

## 8 Discussion

#### A unifying geometric perspective

In the language of information geometry, the arbitrage cost is the canonical divergence of the dually-flat simplex (Appendix [E](#A5 "Appendix E Why (AM+GM)/normalise works: the 𝛼-family of geodesics ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).
The Fisher–Rao metric provides a single framework that explains why the various candidate interpolation methods (linear, geometric, (AM+GM)/normalise, Lambert W) all perform similarly.
Each corresponds to a different geodesic or approximate geodesic on the weight simplex (Appendix [E](#A5 "Appendix E Why (AM+GM)/normalise works: the 𝛼-family of geodesics ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")), and their near-agreement reflects the fact that the simplex geometry is nearly flat at the scale of typical per-step weight changes.
The sub-optimality bound (Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 6 Bounding SLERP’s sub-optimality on the exact KL cost ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) makes this precise: SLERP’s gap to the exact KL optimum is O​(Ω4/f3)O(\Omega^{4}/f^{3}), so for any reasonable step count the choice between methods is practical, not a matter of loss optimality.

#### Constant-price assumption

The analysis assumes market prices are constant within each interpolation (§[2](#S2 "2 Background ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).
In reality prices change over time, and arbitrage may be partial or
delayed, introducing additional effects outside the KL framework.
The optimal interpolation under time-varying prices remains an open question.

#### Multi-token generalisation

The Lambert W approach of [[1](#bib.bib1)] optimises each weight component independently and renormalises, which is only exact for small weight changes.
SLERP operates intrinsically on the sphere and automatically preserves the constraint ∑iwi=1\sum\_{i}w\_{i}=1 (since ∑iηi2=1\sum\_{i}\eta\_{i}^{2}=1 along any great circle in the positive orthant), making it a natural NN-token generalisation with no renormalisation required.

#### Fees and transaction costs

The analysis assumes zero fees and perfect arbitrage at every block.
In practice, fees and gas costs impose a profitability threshold: arbitrage occurs only when the accumulated opportunity exceeds transaction costs, reducing the effective rebalancing frequency from once per block to once every several minutes or hours [[8](#bib.bib8)].
At this coarser cadence the number of effective steps ff is small, so the absolute cost of rebalancing is dominated by the unavoidable 2​Ω2/f2\Omega^{2}/f term (Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 6 Bounding SLERP’s sub-optimality on the exact KL cost ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) rather than by the choice of interpolation method.

#### Implementation considerations

Computing SLERP requires one arccos\arccos evaluation, NN square roots, and per-step sin\sin calls, comparable in cost to geometric mean interpolation.
For on-chain implementations where transcendental functions are expensive, the (AM+GM)/normalise heuristic of [[1](#bib.bib1)] remains the most practical choice.
The recursive bisection algorithm (Corollary [3](#Thmcorollary3 "Corollary 3 (Trig-free SLERP via recursive bisection). ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) shows that this heuristic computes exact geodesic points at power-of-two step counts using only elementary arithmetic.
No trigonometric functions are needed.

#### Accuracy of the quadratic approximation

The quadratic loss kernel, Eq ([10](#S3.E10 "In Corollary 1. ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")), has cubic remainder in the per-step weight changes: for ff-step interpolation the cumulative error is O​(1/f2)O(1/f^{2}).
For large single-step updates or weights near zero, the Lambert W approach of [[1](#bib.bib1)] (which maximises the exact finite-step retention ratio) may be preferred.

## 9 Concluding remarks

The per-step arbitrage loss from rebalancing a TFMM pool is a KL divergence; the Fisher–Rao metric therefore governs rebalancing costs on the weight simplex.
The loss-minimising interpolation under the leading-order expansion of this cost is a geodesic traversed at constant speed (SLERP in Hellinger coordinates), and the (AM+GM)/normalise heuristic of [[1](#bib.bib1)] computes exact geodesic midpoints via a binomial identity.
The recursive bisection algorithm (Corollary [3](#Thmcorollary3 "Corollary 3 (Trig-free SLERP via recursive bisection). ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) produces the full SLERP trajectory at power-of-two step counts using only elementary arithmetic.
The sub-optimality bound (Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 6 Bounding SLERP’s sub-optimality on the exact KL cost ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) guarantees near-optimality on the exact KL cost.
The (AM+GM)/normalise heuristic remains the practical on-chain recommendation.

The geometric structure here is not specific to G3M/TFMM pools.
Any AMM whose trading function is parameterised by a vector on the probability simplex will have its arbitrage cost naturally expressible as a divergence in the information-geometric sense, making the Fisher–Rao metric the natural Riemannian structure.
Different AMM mechanisms (e.g. virtual balance interpolation in concentrated liquidity designs) would induce different, potentially state-dependent, metrics on their parameter spaces.
Identifying these metrics and their geodesics could yield analogous rebalancing strategies for other designs.

## References

* Willetts and Harrington [2024]

  Matthew Willetts and Christian Harrington.
  Optimal rebalancing in dynamic amms, 2024.
  URL <https://arxiv.org/abs/2403.18737>.
* team [2023]

  QuantAMM team.
  Temporal-function market making litepaper, 2023.
  URL <https://www.quantamm.fi/litepapers>.
* Shoemake [1985]

  Ken Shoemake.
  Animating rotation with quaternion curves.
  In *Proceedings of the 12th Annual Conference on Computer Graphics and Interactive Techniques (SIGGRAPH ’85)*, pages 245–254. ACM, 1985.
* Martinelli and Mushegian [2019]

  Fernando Martinelli and Nikolai Mushegian.
  Balancer: A non-custodial portfolio manager, liquidity provider, and price sensor., 2019.
* Evans [2019]

  Alex Evans.
  Liquidity provider returns in geometric mean markets, 2019.
* Chentsov [1982]

  Nikolai Nikolaevich Chentsov.
  Statistical decision rules and optimal inference.
  *Translations of Mathematical Monographs*, 53, 1982.
* Amari [1985]

  Shun-ichi Amari.
  *Differential-Geometrical Methods in Statistics*, volume 28 of *Lecture Notes in Statistics*.
  Springer, 1985.
* Willetts and Harrington [2026]

  Matthew Willetts and Christian Harrington.
  Pools as portfolios: Observed arbitrage efficiency & lvr analysis of dynamic weight amms, 2026.
  URL <https://arxiv.org/abs/2602.22069>.

## Appendix A Retention Ratio

### A.1 Deferred Proof: Proposition [1](#Thmproposition1 "Proposition 1. ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") [Retention ratio]

See [1](#Thmproposition1 "Proposition 1. ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")

###### Proof.

Start with Eq ([1](#S2.E1 "In Arbitrage in Geometric Mean Market Makers when weights change ‣ 2.1 Dynamic Weight Automated Market Makers ‣ 2 Background ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | Riend=Ristart​wiendwistart​∏j=1N(wjstartwjend)wjend,R\_{i}^{\mathrm{end}}=R\_{i}^{\mathrm{start}}\frac{w\_{i}^{\mathrm{end}}}{w\_{i}^{\mathrm{start}}}\prod\_{j=1}^{N}\left(\frac{w\_{j}^{\mathrm{start}}}{w\_{j}^{\mathrm{end}}}\right)^{w\_{j}^{\mathrm{end}}}, |  | (A.1) |

which we can rearrange to get

|  |  |  |  |
| --- | --- | --- | --- |
|  | RiendRistart​wistartwiend=∏j=1N(wjstartwjend)wjend,\frac{R\_{i}^{\mathrm{end}}}{R\_{i}^{\mathrm{start}}}\frac{w\_{i}^{\mathrm{start}}}{w\_{i}^{\mathrm{end}}}=\prod\_{j=1}^{N}\left(\frac{w\_{j}^{\mathrm{start}}}{w\_{j}^{\mathrm{end}}}\right)^{w\_{j}^{\mathrm{end}}}, |  | (A.2) |

and we thus define r:=∏j=1N(wjstartwjend)wjendr:=\prod\_{j=1}^{N}\left(\frac{w\_{j}^{\mathrm{start}}}{w\_{j}^{\mathrm{end}}}\right)^{w\_{j}^{\mathrm{end}}}.
For given reserves and market prices 𝐦p\boldsymbol{\mathbf{m}}\_{p}, pool value is V=∑i=1NRi​mp,iV=\sum\_{i=1}^{N}R\_{i}m\_{p,i}.
By the action of arbitrageurs, the pool holds the minimum value possible under its trading function. The weight vector then gives the division of value between assets [[2](#bib.bib2)], so we have for all ii

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vstart​wistart\displaystyle V^{\mathrm{start}}w^{\mathrm{start}}\_{i} | =Ristart​mp,i\displaystyle=R^{\mathrm{start}}\_{i}m\_{p,i} |  | (A.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vend​wiend\displaystyle V^{\mathrm{end}}w^{\mathrm{end}}\_{i} | =Riend​mp,i\displaystyle=R^{\mathrm{end}}\_{i}m\_{p,i} |  | (A.4) |

Dividing these componentwise, rearranging, and substituting Eq ([A.2](#A1.E2 "In Proof. ‣ A.1 Deferred Proof: Proposition 1 [Retention ratio] ‣ Appendix A Retention Ratio ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | VendVstart​wiendwistart\displaystyle\frac{V^{\mathrm{end}}}{V^{\mathrm{start}}}\frac{w^{\mathrm{end}}\_{i}}{w^{\mathrm{start}}\_{i}} | =RiendRistart\displaystyle=\frac{R^{\mathrm{end}}\_{i}}{R^{\mathrm{start}}\_{i}} |  | (A.5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⇒VendVstart\displaystyle\Rightarrow\frac{V^{\mathrm{end}}}{V^{\mathrm{start}}} | =RiendRistart​wistartwiend\displaystyle=\frac{R\_{i}^{\mathrm{end}}}{R\_{i}^{\mathrm{start}}}\frac{w\_{i}^{\mathrm{start}}}{w\_{i}^{\mathrm{end}}} |  | (A.6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⇒VendVstart\displaystyle\Rightarrow\frac{V^{\mathrm{end}}}{V^{\mathrm{start}}} | =∏j=1N(wjstartwjend)wjend\displaystyle=\prod\_{j=1}^{N}\left(\frac{w\_{j}^{\mathrm{start}}}{w\_{j}^{\mathrm{end}}}\right)^{w\_{j}^{\mathrm{end}}} |  | (A.7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⇒VendVstart\displaystyle\Rightarrow\frac{V^{\mathrm{end}}}{V^{\mathrm{start}}} | =r\displaystyle=r |  | (A.8) |

as required.
∎

### A.2 Deferred Proof: Corollary [1](#Thmcorollary1 "Corollary 1. ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") [Quadratic loss kernel]

See [1](#Thmcorollary1 "Corollary 1. ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")

###### Proof.

We derive Eq ([10](#S3.E10 "In Corollary 1. ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) in detail.
Starting from the retention ratio, Eq ([8](#S3.E8 "In Proposition 1. ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡r=∑i=1Nwiend​log⁡(wistartwiend).\log r=\sum\_{i=1}^{N}w\_{i}^{\mathrm{end}}\log\!\left(\frac{w\_{i}^{\mathrm{start}}}{w\_{i}^{\mathrm{end}}}\right). |  | (A.9) |

Writing wiend=wi+Δ​wiw\_{i}^{\mathrm{end}}=w\_{i}+\Delta w\_{i} (where wi≡wistartw\_{i}\equiv w\_{i}^{\mathrm{start}} for brevity):

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡r\displaystyle\log r | =∑i=1N(wi+Δ​wi)​log⁡(wiwi+Δ​wi)\displaystyle=\sum\_{i=1}^{N}(w\_{i}+\Delta w\_{i})\log\!\left(\frac{w\_{i}}{w\_{i}+\Delta w\_{i}}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∑i=1N(wi+Δ​wi)​log⁡(1+Δ​wiwi).\displaystyle=-\sum\_{i=1}^{N}(w\_{i}+\Delta w\_{i})\log\!\left(1+\frac{\Delta w\_{i}}{w\_{i}}\right). |  | (A.10) |

Expanding log⁡(1+x)=x−x2/2+O​(x3)\log(1+x)=x-x^{2}/2+O(x^{3}) with x=Δ​wi/wix=\Delta w\_{i}/w\_{i}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡r\displaystyle\log r | =−∑i=1N(wi+Δ​wi)​(Δ​wiwi−(Δ​wi)22​wi2+O​((Δ​wi)3wi3))\displaystyle=-\sum\_{i=1}^{N}(w\_{i}+\Delta w\_{i})\left(\frac{\Delta w\_{i}}{w\_{i}}-\frac{(\Delta w\_{i})^{2}}{2w\_{i}^{2}}+O\!\left(\frac{(\Delta w\_{i})^{3}}{w\_{i}^{3}}\right)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∑i=1N(Δ​wi+(Δ​wi)2wi−(Δ​wi)22​wi−(Δ​wi)32​wi2+⋯)\displaystyle=-\sum\_{i=1}^{N}\left(\Delta w\_{i}+\frac{(\Delta w\_{i})^{2}}{w\_{i}}-\frac{(\Delta w\_{i})^{2}}{2w\_{i}}-\frac{(\Delta w\_{i})^{3}}{2w\_{i}^{2}}+\cdots\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∑i=1NΔ​wi⏟= 0−∑i=1N(Δ​wi)22​wi+O​(Δ​w3).\displaystyle=-\underbrace{\sum\_{i=1}^{N}\Delta w\_{i}}\_{=\,0}-\sum\_{i=1}^{N}\frac{(\Delta w\_{i})^{2}}{2w\_{i}}+O(\Delta w^{3}). |  | (A.11) |

The linear term vanishes because ∑iΔ​wi=0\sum\_{i}\Delta w\_{i}=0 (weights sum to 1 at both endpoints), leaving

|  |  |  |  |
| --- | --- | --- | --- |
|  | −log⁡r≈∑i=1N(Δ​wi)22​wi,-\log r\;\approx\;\sum\_{i=1}^{N}\frac{(\Delta w\_{i})^{2}}{2w\_{i}}, |  | (A.12) |

as required.
∎

## Appendix B Deferred proof: Constant metric speed minimises total loss (used in Corollary [2](#Thmcorollary2 "Corollary 2 (SLERP optimality). ‣ 4 SLERP on the sphere under Hellinger embedding ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers"))

> Claim. Let s0<s1<⋯<sfs\_{0}<s\_{1}<\cdots<s\_{f} be a partition of a path of total arc-length S=sf−s0S=s\_{f}-s\_{0}.
> The sum ∑k=1f(Δ​sk)2\sum\_{k=1}^{f}(\Delta s\_{k})^{2}, where Δ​sk=sk−sk−1\Delta s\_{k}=s\_{k}-s\_{k-1}, is minimised when all increments are equal: Δ​sk=S/f\Delta s\_{k}=S/f for all kk.

###### Proof.

By the QM–AM inequality:

|  |  |  |
| --- | --- | --- |
|  | 1f​∑k=1f(Δ​sk)2≥(1f​∑k=1fΔ​sk)2=S2f2.\frac{1}{f}\sum\_{k=1}^{f}(\Delta s\_{k})^{2}\geq\left(\frac{1}{f}\sum\_{k=1}^{f}\Delta s\_{k}\right)^{\!2}=\frac{S^{2}}{f^{2}}. |  |

Hence ∑k(Δ​sk)2≥S2/f\sum\_{k}(\Delta s\_{k})^{2}\geq S^{2}/f, with equality iff all Δ​sk\Delta s\_{k} are equal.
∎

This result, combined with the identification of per-step loss as (d​sk)2(\mathrm{d}s\_{k})^{2}, establishes that the loss-minimising parameterisation of any path is constant metric speed.
The further optimisation over the choice of path then selects the geodesic, since among all paths with a given total arc-length SS, the one with smallest SS gives the smallest S2/fS^{2}/f.

## Appendix C Deferred proof: Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 6 Bounding SLERP’s sub-optimality on the exact KL cost ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") [sub-optimality bound]

See [3](#Thmtheorem3 "Theorem 3. ‣ 6 Bounding SLERP’s sub-optimality on the exact KL cost ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")

###### Proof.

Write the total exact cost as C=Q+RC=Q+R, where

|  |  |  |
| --- | --- | --- |
|  | Q=∑k=1f∑i(Δ​wi(k))22​wi(k−1),R=∑k=1fRk,Q=\sum\_{k=1}^{f}\sum\_{i}\frac{(\Delta w\_{i}^{(k)})^{2}}{2\,w\_{i}^{(k-1)}},\qquad R=\sum\_{k=1}^{f}R\_{k}, |  |

and Rk=∑iwi(k−1)​h​(ui(k))R\_{k}=\sum\_{i}w\_{i}^{(k-1)}\,h(u\_{i}^{(k)}) with ui(k)=Δ​wi(k)/wi(k−1)u\_{i}^{(k)}=\Delta w\_{i}^{(k)}/w\_{i}^{(k-1)} and h​(u)=(1+u)​log⁡(1+u)−u−u2/2h(u)=(1{+}u)\log(1{+}u)-u-u^{2}/2.
SLERP minimises QQ, so ∇Q|SLERP=0\nabla Q\big|\_{\mathrm{SLERP}}=0 and ∇C|SLERP=∇R|SLERP\nabla C\big|\_{\mathrm{SLERP}}=\nabla R\big|\_{\mathrm{SLERP}}.

#### Step 1: per-step change bound

Along the SLERP path the per-step angular displacement on the Hellinger sphere is Ω/f\Omega/f.
The weight change satisfies Δ​wi=(ηi(k)+ηi(k−1))​(ηi(k)−ηi(k−1))\Delta w\_{i}=(\eta\_{i}^{(k)}+\eta\_{i}^{(k-1)})(\eta\_{i}^{(k)}-\eta\_{i}^{(k-1)}), so |Δ​wi|≤2​|Δ​ηi||\Delta w\_{i}|\leq 2|\Delta\eta\_{i}| (since |ηi|≤1|\eta\_{i}|\leq 1) and

|  |  |  |
| --- | --- | --- |
|  | |ui(k)|=|Δ​wi(k)|wi(k−1)≤2​|Δ​ηi(k)|ϵ≤2​Ωf​ϵ,|u\_{i}^{(k)}|=\frac{|\Delta w\_{i}^{(k)}|}{w\_{i}^{(k-1)}}\leq\frac{2|\Delta\eta\_{i}^{(k)}|}{\epsilon}\leq\frac{2\Omega}{f\epsilon}, |  |

where the last inequality uses |Δ​ηi|≤|𝚫​𝜼|≤Ω/f|\Delta\eta\_{i}|\leq|\boldsymbol{\Delta\eta}|\leq\Omega/f and wi≥ϵw\_{i}\geq\epsilon.

#### Step 2: gradient of the remainder

Each component of ∇R\nabla R with respect to wi(k)w\_{i}^{(k)} receives contributions from steps kk and k+1k{+}1.
Since h′​(u)=log⁡(1+u)−uh^{\prime}(u)=\log(1{+}u)-u satisfies |h′​(u)|≤u2/(1−|u|)|h^{\prime}(u)|\leq u^{2}/(1-|u|) for |u|<1|u|<1, and |ui(k)|≤2​Ω/(f​ϵ)≤1/2|u\_{i}^{(k)}|\leq 2\Omega/(f\epsilon)\leq 1/2 for f≥4​Ω/ϵf\geq 4\Omega/\epsilon, each gradient component has magnitude

|  |  |  |
| --- | --- | --- |
|  | |∂R∂wi(k)|≤2⋅(2​Ω/(f​ϵ))21/2=16​Ω2f2​ϵ2.\left|\frac{\partial R}{\partial w\_{i}^{(k)}}\right|\leq 2\cdot\frac{(2\Omega/(f\epsilon))^{2}}{1/2}=\frac{16\,\Omega^{2}}{f^{2}\epsilon^{2}}. |  |

There are (f−1)(f{-}1) intermediate weight vectors, each with N−1N{-}1 degrees of freedom on the simplex, giving

|  |  |  |
| --- | --- | --- |
|  | ‖∇R‖2≤(f−1)​(N−1)​(16​Ω2f2​ϵ2)2≤256​N​Ω4f3​ϵ4.\|\nabla R\|^{2}\leq(f{-}1)(N{-}1)\left(\frac{16\,\Omega^{2}}{f^{2}\epsilon^{2}}\right)^{\!2}\leq\frac{256\,N\,\Omega^{4}}{f^{3}\,\epsilon^{4}}. |  |

#### Step 3: Hessian lower bound

The Hessian of QQ restricted to the simplex constraints is block-diagonal in the intermediate weight vectors.
Each diagonal block receives contributions from two consecutive Fisher–Rao metrics diag​(1/wi(k−1))\mathrm{diag}(1/w\_{i}^{(k-1)}) and diag​(1/wi(k))\mathrm{diag}(1/w\_{i}^{(k)}) (the latter from step k+1k{+}1, where w(k)w^{(k)} is the base point).
On the simplex hyperplane {∑ivi=0}\{\sum\_{i}v\_{i}=0\}, each Fisher–Rao metric has minimum eigenvalue ≥1/maxi⁡wi≥1\geq 1/\max\_{i}w\_{i}\geq 1, so each block satisfies λmin≥2\lambda\_{\min}\geq 2.
The per-step KL cost is proportional to (1+u)​log⁡(1+u)(1{+}u)\log(1{+}u), whose second derivative is 1/(1+u)1/(1{+}u), while the quadratic model has second derivative 11.
The Hessian perturbation per block is therefore proportional to 1/(1+u)−1=−u/(1+u)1/(1{+}u)-1=-u/(1{+}u), which satisfies |u/(1+u)|≤|u|/(1−|u|)≤2​|u||u/(1{+}u)|\leq|u|/(1-|u|)\leq 2|u| for |u|≤1/2|u|\leq 1/2.
By the Step 1 bound |u|≤2​Ω/(f​ϵ)|u|\leq 2\Omega/(f\epsilon), the perturbation magnitude is at most 4​Ω/(f​ϵ)4\Omega/(f\epsilon) per block.
For f≥4​Ω/ϵf\geq 4\Omega/\epsilon (already required in Step 2) this is at most 11, so the Hessian of CC satisfies λmin​(∇2C)≥2−1=1\lambda\_{\min}(\nabla^{2}C)\geq 2-1=1 per block.

#### Step 4: quadratic bound

Since SLERP is a critical point of QQ and the Hessian of CC at SLERP is positive definite, the standard bound on the cost improvement available from a gradient step gives

|  |  |  |
| --- | --- | --- |
|  | CSLERP−C∗≤‖∇C‖22​λmin​(∇2C)≤256​N​Ω42⋅f3​ϵ4=128​Nf3​ϵ4​Ω4,C\_{\mathrm{SLERP}}-C\_{\*}\leq\frac{\|\nabla C\|^{2}}{2\,\lambda\_{\min}(\nabla^{2}C)}\leq\frac{256\,N\,\Omega^{4}}{2\cdot f^{3}\,\epsilon^{4}}=\frac{128\,N}{f^{3}\,\epsilon^{4}}\,\Omega^{4}, |  |

so A=128​N/ϵ4A=128\,N/\epsilon^{4} suffices.
The relative sub-optimality is A​Ω4/f3A\,\Omega^{4}/f^{3} divided by the total SLERP cost 2​Ω2/f2\Omega^{2}/f, giving O​(Ω2/f2)O(\Omega^{2}/f^{2}).
∎

## Appendix D Taylor agreement of interpolation methods

Write wi≡wistartw\_{i}\equiv w\_{i}^{\mathrm{start}} and ui=Δ​wi/wiu\_{i}=\Delta w\_{i}/w\_{i} where Δ​wi=wiend−wistart\Delta w\_{i}=w\_{i}^{\mathrm{end}}-w\_{i}^{\mathrm{start}}.
The simplex constraint gives ∑iwi​ui=0\sum\_{i}w\_{i}u\_{i}=0.
Define σ2=∑jwj​uj2\sigma^{2}=\sum\_{j}w\_{j}u\_{j}^{2}.
We expand all three methods to second order in uu.

#### SLERP

Under the Hellinger embedding, wiend=wi​1+ui=wi​(1+ui/2−ui2/8+O​(u3))\sqrt{w\_{i}^{\mathrm{end}}}=\sqrt{w\_{i}}\sqrt{1+u\_{i}}=\sqrt{w\_{i}}(1+u\_{i}/2-u\_{i}^{2}/8+O(u^{3})).
The Bhattacharyya coefficient is

|  |  |  |
| --- | --- | --- |
|  | cos⁡Ω=∑jwj​1+uj=1+12​∑jwj​uj⏟= 0−18​σ2+O​(u3),\cos\Omega=\sum\_{j}w\_{j}\sqrt{1+u\_{j}}=1+\tfrac{1}{2}\underbrace{\sum\_{j}w\_{j}u\_{j}}\_{=\,0}-\tfrac{1}{8}\sigma^{2}+O(u^{3}), |  |

so Ω2=2​(1−cos⁡Ω)+O​(u4)=σ2/4+O​(u3)\Omega^{2}=2(1-\cos\Omega)+O(u^{4})=\sigma^{2}/4+O(u^{3}).
The SLERP coefficients satisfy, for small Ω\Omega,

|  |  |  |
| --- | --- | --- |
|  | sin⁡(x​Ω)sin⁡Ω=x+x​(1−x2)6​Ω2+O​(Ω4).\frac{\sin(x\Omega)}{\sin\Omega}=x+\frac{x(1-x^{2})}{6}\Omega^{2}+O(\Omega^{4}). |  |

Since Ω2=O​(u2)\Omega^{2}=O(u^{2}), any product of an Ω2\Omega^{2} correction with a term already O​(u)O(u) is O​(u3)O(u^{3}), so

|  |  |  |
| --- | --- | --- |
|  | ηi​(t)=wi​[(α+β)+t​ui2−t​ui28]+O​(u3),\eta\_{i}(t)=\sqrt{w\_{i}}\!\left[(\alpha+\beta)+\frac{tu\_{i}}{2}-\frac{tu\_{i}^{2}}{8}\right]+O(u^{3}), |  |

where α=sin⁡((1−t)​Ω)/sin⁡Ω\alpha=\sin((1\!-\!t)\Omega)/\sin\Omega, β=sin⁡(t​Ω)/sin⁡Ω\beta=\sin(t\Omega)/\sin\Omega.
Using (1−t)3+t3=1−3​t​(1−t)(1\!-\!t)^{3}+t^{3}=1-3t(1\!-\!t), the sum evaluates to α+β=1+t​(1−t)2​Ω2+O​(u4)\alpha+\beta=1+\frac{t(1-t)}{2}\Omega^{2}+O(u^{4}).
Squaring and substituting Ω2=σ2/4\Omega^{2}=\sigma^{2}/4:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wiSLERP​(t)=wi+t​Δ​wi+t​(1−t)4​wi​(σ2−ui2)+O​(u3).w\_{i}^{\mathrm{SLERP}}(t)=w\_{i}+t\,\Delta w\_{i}+\frac{t(1-t)}{4}\,w\_{i}\!\left(\sigma^{2}-u\_{i}^{2}\right)+O(u^{3}). |  | (D.13) |

#### (AM+GM)/normalise

The arithmetic component is wiAM​(t)=wi​(1+t​ui)w\_{i}^{\mathrm{AM}}(t)=w\_{i}(1+tu\_{i}).
The geometric component is wiGM​(t)=wi​(1+ui)t=wi​(1+t​ui+t​(t−1)2​ui2+O​(u3))w\_{i}^{\mathrm{GM}}(t)=w\_{i}(1+u\_{i})^{t}=w\_{i}(1+tu\_{i}+\frac{t(t-1)}{2}u\_{i}^{2}+O(u^{3})).
Their unnormalised sum is

|  |  |  |
| --- | --- | --- |
|  | wiAM+wiGM=wi​[2+2​t​ui+t​(t−1)2​ui2]+O​(u3).w\_{i}^{\mathrm{AM}}+w\_{i}^{\mathrm{GM}}=w\_{i}\!\left[2+2tu\_{i}+\tfrac{t(t-1)}{2}u\_{i}^{2}\right]+O(u^{3}). |  |

The normalisation factor, using ∑jwj​uj=0\sum\_{j}w\_{j}u\_{j}=0, is

|  |  |  |
| --- | --- | --- |
|  | Z=∑j(wjAM+wjGM)=2+t​(t−1)2​σ2+O​(u3).Z=\sum\_{j}(w\_{j}^{\mathrm{AM}}+w\_{j}^{\mathrm{GM}})=2+\tfrac{t(t-1)}{2}\sigma^{2}+O(u^{3}). |  |

Dividing and expanding 1/Z1/Z:

|  |  |  |  |
| --- | --- | --- | --- |
|  | w˘i​(t)=wi+t​Δ​wi+t​(1−t)4​wi​(σ2−ui2)+O​(u3),\breve{w}\_{i}(t)=w\_{i}+t\,\Delta w\_{i}+\frac{t(1-t)}{4}\,w\_{i}\!\left(\sigma^{2}-u\_{i}^{2}\right)+O(u^{3}), |  | (D.14) |

which matches Eq ([D.13](#A4.E13 "In SLERP ‣ Appendix D Taylor agreement of interpolation methods ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) exactly through O​(u2)O(u^{2}).

#### Lambert W at the midpoint

The optimal 2-step midpoint of [[1](#bib.bib1)] is w~i∗=wi​(1+ui)/W0​(e​(1+ui))\tilde{w}\_{i}^{\*}=w\_{i}(1+u\_{i})/W\_{0}(e(1+u\_{i})).
Expanding W0​(e​(1+u))W\_{0}(e(1+u)) around u=0u=0 (where W0​(e)=1W\_{0}(e)=1) by implicit differentiation of W​eW=e​(1+u)We^{W}=e(1+u):

|  |  |  |
| --- | --- | --- |
|  | W0​(e​(1+u))=1+u2−3​u216+O​(u3).W\_{0}(e(1+u))=1+\tfrac{u}{2}-\tfrac{3u^{2}}{16}+O(u^{3}). |  |

Then w~i∗=wi​(1+ui)​(1+ui/2−3​ui2/16)−1=wi​(1+ui/2−ui2/16+O​(u3))\tilde{w}\_{i}^{\*}=w\_{i}(1+u\_{i})(1+u\_{i}/2-3u\_{i}^{2}/16)^{-1}=w\_{i}(1+u\_{i}/2-u\_{i}^{2}/16+O(u^{3})).
This requires renormalisation; the normalisation factor is ∑jw~j∗=1−σ2/16+O​(u3)\sum\_{j}\tilde{w}\_{j}^{\*}=1-\sigma^{2}/16+O(u^{3}), giving

|  |  |  |  |
| --- | --- | --- | --- |
|  | w^iLW=wi+12​Δ​wi+116​wi​(σ2−ui2)+O​(u3).\hat{w}\_{i}^{\mathrm{LW}}=w\_{i}+\tfrac{1}{2}\Delta w\_{i}+\tfrac{1}{16}\,w\_{i}(\sigma^{2}-u\_{i}^{2})+O(u^{3}). |  | (D.15) |

Setting t=1/2t=1/2 in Eq ([D.13](#A4.E13 "In SLERP ‣ Appendix D Taylor agreement of interpolation methods ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) gives the same second-order term (1/2)​(1/2)4=116\frac{(1/2)(1/2)}{4}=\frac{1}{16}, confirming agreement through O​(u2)O(u^{2}).

#### The O​(u3)O(u^{3}) difference

At general t≠1/2t\neq 1/2, the third-order terms of SLERP and (AM+GM)/normalise differ (the former involves Ω4\Omega^{4} corrections from the SLERP coefficients, the latter involves cubic terms from (1+u)t(1+u)^{t}).
At t=1/2t=1/2, these methods agree exactly to all orders by Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers").
The Lambert W midpoint first differs from both at O​(u3)O(u^{3}), reflecting the fact that it optimises the exact retention ratio while the other two optimise the quadratic surrogate.

## Appendix E Why (AM+GM)/normalise works: the α\alpha-family of geodesics

The midpoint equivalence (Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) follows from the binomial identity, but it has a geometric interpretation in terms of a family of “straight lines” on the probability simplex [[7](#bib.bib7)].

Information geometry parameterises a family of connections on the simplex by α∈[−1,1]\alpha\in[-1,1].
Each value of α\alpha gives a different notion of geodesic:

* •

  α=−1\alpha=-1 (arithmetic/linear interpolation).
  Geodesics are straight lines in the ordinary simplex coordinates wiw\_{i}.
  The midpoint is wimid=(wistart+wiend)/2w\_{i}^{\mathrm{mid}}=(w\_{i}^{\mathrm{start}}+w\_{i}^{\mathrm{end}})/2.
  This is the interpolation used by liquidity bootstrapping pools and by TFMM when weights change linearly [[2](#bib.bib2)].
* •

  α=+1\alpha=+1 (geometric interpolation).
  Geodesics are straight lines in the log-coordinates θi=log⁡wi\theta\_{i}=\log w\_{i}.
  The midpoint is wimid∝wistart​wiendw\_{i}^{\mathrm{mid}}\propto\sqrt{w\_{i}^{\mathrm{start}}\,w\_{i}^{\mathrm{end}}} (after renormalisation).
* •

  α=0\alpha=0 (Fisher–Rao metric geodesic).
  Geodesics are great circles on the sphere under the Hellinger embedding.
  The midpoint is the SLERP midpoint.

AM and GM are the midpoints of the two extreme geodesics in this family.
Why does their *sum* land on the middle geodesic?

The Hellinger embedding forces this, and it is not a general principle about geodesic families.
The α=0\alpha=0 midpoint is computed by averaging the Hellinger coordinates wi\sqrt{w\_{i}} and squaring back.
Squaring a sum of square roots produces the binomial identity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (a+b)2=(a+b)⏟AM term+2​a​b⏟GM term\left(\sqrt{a}+\sqrt{b}\right)^{2}=\underbrace{(a+b)}\_{\text{AM term}}+\underbrace{2\sqrt{ab}}\_{\text{GM term}} |  | (E.16) |

The sum appears because squaring distributes as addition.
Had the embedding involved a different power (say, cube roots), the decomposition would be different and AM + GM would not appear.
The square root is forced by the Fisher–Rao metric: wi↦wi1/2w\_{i}\mapsto w\_{i}^{1/2} is the unique power that makes the metric Euclidean (up to scale), and the binomial identity is a consequence of that specific power.

The α=−1\alpha=-1 (arithmetic) midpoint automatically satisfies ∑iwimid=1\sum\_{i}w\_{i}^{\mathrm{mid}}=1, while the α=+1\alpha=+1 (geometric) midpoint does not and requires renormalisation.
The (AM+GM)/normalise formula inherits this need for renormalisation from its geometric-mean component.

For general t≠1/2t\neq 1/2, the three α\alpha-geodesics diverge, and the (AM+GM)/normalise trajectory, which averages the α=±1\alpha=\pm 1 trajectories pointwise, no longer lies exactly on the α=0\alpha=0 geodesic.
The third-order agreement reported in Table [1](#S5.T1 "Table 1 ‣ 5.1 Comparison at general 𝑡 and with Lambert W ‣ 5 SLERP midpoint equals (AM+GM)/normalise midpoint ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") reflects the smooth dependence of geodesics on α\alpha: near any base point, geodesics of the different connections share the same tangent vector and second-order curvature, differing only at third order.

### E.1 Differential-geometric context

For readers familiar with differential geometry, the three α\alpha-values above correspond to specific affine connections on the simplex manifold.

The α=0\alpha=0 connection is the *Levi-Civita connection* of the Fisher–Rao metric: the unique torsion-free, metric-compatible connection.
Its geodesics solve the standard Euler–Lagrange equation for arc-length minimisation, which is how the SLERP optimality result (Corollary [2](#Thmcorollary2 "Corollary 2 (SLERP optimality). ‣ 4 SLERP on the sphere under Hellinger embedding ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) is derived, without ever computing Christoffel symbols.
The Hellinger embedding sidesteps the Christoffel computation entirely: it maps the simplex isometrically onto a sphere, where the geodesics are known to be great circles.
(This is analogous to solving geodesic problems by calculus of variations in a convenient coordinate system, rather than by the geodesic equation x¨μ+Γν​ρμ​x˙ν​x˙ρ=0\ddot{x}^{\mu}+\Gamma^{\mu}\_{\nu\rho}\dot{x}^{\nu}\dot{x}^{\rho}=0 directly.)

The α=±1\alpha=\pm 1 connections are the *mixture* (mm) and *exponential* (ee) connections.
These are torsion-free but not metric-compatible, and they are *dually flat*: the simplex has zero curvature in the α=−1\alpha=-1 coordinates (wiw\_{i}) and separately in the α=+1\alpha=+1 coordinates (log⁡wi\log w\_{i}), but with respect to different connections.

This dual flatness gives rise to a *canonical divergence*: the unique divergence function compatible with the dually-flat structure.
On the probability simplex, the canonical divergence is the KL divergence [[7](#bib.bib7)].
The fact that arbitrage cost equals the KL divergence (Theorem [1](#Thmtheorem1 "Theorem 1 (Arbitrage loss as KL divergence). ‣ 3 Arbitrage loss is a KL divergence ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) means rebalancing cost is the canonical divergence of the simplex.

The three interpolation methods in the main text correspond to the three canonical geodesics: linear (α=−1\alpha=-1, flat in wiw\_{i}), geometric (α=+1\alpha=+1, flat in log⁡wi\log w\_{i}), and SLERP (α=0\alpha=0, the metric geodesic that sits between them).

## Appendix F Explicit computation: SLERP vs Lambert W for N=2N=2

For N=2N=2 with weights (w,1−w)(w,1-w), the SLERP midpoint (f=2f=2) is computed as follows.

Map to the sphere: 𝜼start=(wstart,1−wstart)\boldsymbol{\mathbf{\eta}}^{\mathrm{start}}=(\sqrt{w^{\mathrm{start}}},\,\sqrt{1-w^{\mathrm{start}}}), 𝜼end=(wend,1−wend)\boldsymbol{\mathbf{\eta}}^{\mathrm{end}}=(\sqrt{w^{\mathrm{end}}},\,\sqrt{1-w^{\mathrm{end}}}).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ω\displaystyle\Omega | =arccos⁡(wstart​wend+(1−wstart)​(1−wend)).\displaystyle=\arccos\!\left(\sqrt{w^{\mathrm{start}}w^{\mathrm{end}}}+\sqrt{(1-w^{\mathrm{start}})(1-w^{\mathrm{end}})}\right). |  | (F.17) |

The midpoint on the sphere is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜼mid=12​cos⁡(Ω/2)​(𝜼start+𝜼end).\boldsymbol{\mathbf{\eta}}\_{\mathrm{mid}}=\frac{1}{2\cos(\Omega/2)}\left(\boldsymbol{\mathbf{\eta}}^{\mathrm{start}}+\boldsymbol{\mathbf{\eta}}^{\mathrm{end}}\right). |  | (F.18) |

The midpoint weight is wmid=ηmid,12w\_{\mathrm{mid}}=\eta\_{\mathrm{mid},1}^{2}.

For wstart=0.5w^{\mathrm{start}}=0.5, wend=0.9w^{\mathrm{end}}=0.9:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ω\displaystyle\Omega | =arccos⁡(0.45+0.05)≈0.4636​rad,\displaystyle=\arccos\!\left(\sqrt{0.45}+\sqrt{0.05}\right)\approx 0.4636\,\text{rad}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | wmidSLERP\displaystyle w\_{\mathrm{mid}}^{\mathrm{SLERP}} | ≈0.729.\displaystyle\approx 0.729. |  | (F.19) |

Compare with wmidLambert≈0.717w\_{\mathrm{mid}}^{\mathrm{Lambert}}\approx 0.717 from [[1](#bib.bib1)].
The ∼1.7%{\sim}1.7\% difference reflects higher-order terms that matter at this (large) step size.
For f≥10f\geq 10, per-step changes are ≤0.04\leq 0.04 and the two methods agree to <0.1%<0.1\%.

## Appendix G Weight trajectories and block-to-block changes

The figures below reproduce the N=3N{=}3 setup of Figures 1–2 of [[1](#bib.bib1)], with the addition of SLERP, to allow direct visual comparison.

Figure G.1: Weight interpolations, N=3N=3. At this scale, (b) and (c) are visually indistinguishable.

![Refer to caption](2603.05326v1/interpolation_example_slerp/token_linear.png)


(a) Linear

![Refer to caption](2603.05326v1/interpolation_example_slerp/token_linear_geometric_mean.png)


(b) (AM+GM)/normalise

![Refer to caption](2603.05326v1/interpolation_example_slerp/token_slerp.png)


(c) SLERP

Figure G.2: Block-to-block weight changes (𝐰​(t+1)−𝐰​(t)\boldsymbol{\mathbf{w}}(t+1)-\boldsymbol{\mathbf{w}}(t)). Constant metric speed produces smoothly varying (not constant) weight changes in Cartesian coordinates.

![Refer to caption](2603.05326v1/interpolation_example_slerp/token_linear_change.png)


(a) Linear

![Refer to caption](2603.05326v1/interpolation_example_slerp/token_linear_geometric_mean_alt_change.png)


(b) (AM+GM)/normalise

![Refer to caption](2603.05326v1/interpolation_example_slerp/token_slerp_change.png)


(c) SLERP

At this scale, (AM+GM)/normalise and SLERP trajectories are visually indistinguishable; block-to-block changes for SLERP vary smoothly with amplitude ∼10−4{\sim}10^{-4}.

## Appendix H Near-boundary experiments

The sub-optimality bound (Theorem [3](#Thmtheorem3 "Theorem 3. ‣ 6 Bounding SLERP’s sub-optimality on the exact KL cost ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")) assumes weights bounded away from zero.
Near the simplex boundary the Fisher–Rao metric diverges and the quadratic approximation underlying SLERP is least accurate.
Current G3M implementations enforce a minimum weight of 1%1\%, so wmin=0.01w\_{\min}=0.01 is the practical boundary.

#### Single midpoint (f=2f=2)

For N=2N=2 with 𝐰:(wmin, 1−wmin)→(1−wmin,wmin)\boldsymbol{\mathbf{w}}:(w\_{\min},\,1{-}w\_{\min})\to(1{-}w\_{\min},\,w\_{\min}), we compare the direct Lambert W midpoint formula of [[1](#bib.bib1)],
mi=wiend/W​(wiend⋅e/wistart)m\_{i}=w\_{i}^{\mathrm{end}}/W\!\bigl(w\_{i}^{\mathrm{end}}\cdot e\,/\,w\_{i}^{\mathrm{start}}\bigr)
(normalised), against SLERP and the brute-force L-BFGS-B optimum.

Table H.1: Single-midpoint (f=2f=2) loss ratios for symmetric N=2N=2 weight changes at varying boundary distance. Lambert W, which maximises the exact retention ratio, beats SLERP near the boundary; both converge for small weight changes.

| wminw\_{\min} | SLERP / Optimal | Lambert W / Optimal | Lambert W / SLERP |
| --- | --- | --- | --- |
| 0.01 | 1.178 | 1.053 | 0.894 |
| 0.02 | 1.122 | 1.041 | 0.928 |
| 0.05 | 1.059 | 1.024 | 0.967 |
| 0.10 | 1.025 | 1.012 | 0.987 |
| 0.20 | 1.005 | 1.003 | 0.998 |
| 0.30 | 1.001 | 1.001 | 1.000 |
| 0.40 | 1.000 | 1.000 | 1.000 |

Table [H.1](#A8.T1 "Table H.1 ‣ Single midpoint (𝑓=2) ‣ Appendix H Near-boundary experiments ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers") confirms that for large single-step updates near the boundary, Lambert W, which optimises the exact finite-step retention, outperforms SLERP by up to 10%10\% at wmin=0.01w\_{\min}=0.01.
Both converge to the true optimum as the weight change shrinks (i.e. as wmin→0.5w\_{\min}\to 0.5), consistent with the quadratic approximation becoming exact in the small-step limit.
The multi-step near-boundary results, including the convergence across step counts, the widening advantage of SLERP, and per-step uniformity analysis, are presented in the main text (Figures [7](#S7.F7 "Figure 7 ‣ Convergence across step counts ‣ 7 Experiments ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")–[9](#S7.F9 "Figure 9 ‣ Near-boundary behaviour ‣ 7 Experiments ‣ Riemannian Geometry of Optimal Rebalancing in Dynamic Weight Automated Market Makers")).

DISCLAIMER.
This paper is for general information purposes only.
It does not constitute investment advice or a recommendation or solicitation to buy or sell any investment or asset, or to participate in systems that use TFMM.
It should not be used to evaluate the merits of any investment decision, nor relied upon for accounting, legal, tax, or investment advice.
The opinions expressed reflect the author’s current views on the development and functionality of TFMM and are subject to change without notice.

BETA