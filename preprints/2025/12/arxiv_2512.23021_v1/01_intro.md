---
authors:
- Layla Abu Khalaf
- William Smyth
doc_id: arxiv:2512.23021v1
family_id: arxiv:2512.23021
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control'
url_abs: http://arxiv.org/abs/2512.23021v1
url_html: https://arxiv.org/html/2512.23021v1
venue: arXiv q-fin
version: 1
year: 2025
---


Layla Abu Khalaf


William S. Smyth
Email: w.smyth@ulster.ac.uk

(December 28, 2025)

###### Abstract

We revisit Gerber’s Informational Quality (IQ) framework, a data-driven approach for constructing correlation matrices from co-movement evidence, and address two obstacles that limit its use in portfolio optimization: guaranteeing positive semidefiniteness (PSD) and controlling spectral conditioning. We introduce a squeezing identity that represents IQ estimators as a convex-like combination of structured channel matrices, and propose an atomic-IQ parameterization in which each channel-class matrix is built from PSD atoms with a single class-level normalization. This yields constructive PSD guarantees over an explicit feasibility region, avoiding reliance on ex-post projection. To regulate conditioning, we develop an analytic eigenfloor that targets either a minimum eigenvalue or a desired condition number and, when necessary, repairs PSD violations in closed form while remaining compatible with the squeezing identity. In long-only tangency backtests with transaction costs, atomic-IQ improves out-of-sample Sharpe ratios and delivers a more stable risk profile relative to a broad set of standard covariance estimators.

## I Introduction

Covariance and correlation matrices are central to portfolio construction, risk measurement, and pricing, yet high-dimensional estimates are noisy and often ill-conditioned. Classical responses such as linear and nonlinear shrinkage (ledoit2004honey; ledoit2004well; ledoit2017; ledoit2022quadratic), random-matrix cleaning (laloux1999; bun2017cleaning), factor models (chamberlain1983factor; fan2013factor), and ex-post PSD projection (higham2002computing) stabilize the sample estimator or its spectrum. These approaches improve behavior in practice, but none provide analytic control of eigenvalues: shrinkage intensities are estimated asymptotically, RMT rules are approximate, and Higham’s projection enforces PSD iteratively. No existing method offers closed-form eigenvalue targets for a given estimator.

Gerber Informational Quality (IQ) took a different route: it builds correlation matrices directly from structured co-movement statistics, producing interpretable estimates tailored to task objectives. While IQ often improved conditioning relative to the sample covariance, it did not guarantee PSD and, like other methods, offered no explicit means of controlling eigenvalues.

We develop *atomic–IQ*, a constructive refinement of IQ that addresses both limitations. It introduces the canonical squeezing identity, which can be viewed as balancing a baseline prior of mutual independence (a neutral benchmark) with structured dependence extracted from co-movement evidence. Each class matrix is built from positive semi-definite atoms and normalized once at class level, yielding correlation-PSD channels; under controllable conditions the full estimator is PSD without ex-post repair. We characterize feasibility through an exact spectral condition and give closed-form bounds in the basic–IQ case (squeezing channel weights {η2,η,1}\{\eta^{2},\eta,1\} with η∈[0,1]\eta\in[0,1]). Finally, we introduce an eigenfloor which not only raises λmin\lambda\_{\min}, contracts λmax\lambda\_{\max}, and provides closed-form rules for targeting a floor or condition number, but also acts as an analytic PSD repair that remains inside the squeezing representation. This yields the first covariance estimation framework with closed-form eigenvalue control. Implementation details and practical guardrails for using atomic–IQ in risk systems, together with additional spectral results and the full set of Sharpe ratio tests relative to atomic squeezing, are presented in the appendix.

The broader literature on covariance estimation can be divided into two families. The first consists of sample-anchored regularizers. Linear and quadratic shrinkage blend the sample covariance with a structured target, while nonlinear shrinkage modifies eigenvalues to reduce sampling error (ledoit2004well; ledoit2017; ledoit2022quadratic). Random-matrix theory (RMT) methods remove or adjust modes in the Marčenko–Pastur bulk (laloux1999; bun2017cleaning). Factor models (chamberlain1983factor; fan2013factor) replace the full system with a low-rank latent representation. Higham’s algorithm repairs indefiniteness ex post (higham2002computing). Despite their differences, all of these methods begin with the empirical covariance (or correlation) matrix and then regularize it after the fact.

The second family consists of concordance-based constructive estimators. These build correlation estimates directly from co-movement or concordance statistics rather than from the sample covariance. Kendall’s τ\tau, Spearman’s ρ\rho, and the Gerber statistic exemplify this approach, as does IQ. Such methods are constructive in that they assemble correlation matrices from structured evidence, including ranks, signs, or thresholded events, thereby bypassing the sample covariance altogether.

IQ belongs to this constructive family but also extends it. Whereas earlier concordance methods provide pairwise measures, IQ generalizes the approach to a system-wide framework. Its δ\delta–η\eta template aggregates concordant and discordant events into interpretable class matrices in a way that is compatible with modern optimization and machine learning. Atomic–IQ strengthens this framework by ensuring PSD through atomic construction and by introducing explicit eigenvalue controls via the eigenfloor. In this way IQ not only broadens the constructive family but also provides the first interpretable covariance estimator with analytic eigenvalue control. With atomic–IQ, the earlier concern that IQ matrices might fail to be PSD is resolved, and the approach can be regarded on the same footing as conventional methods while retaining its distinctive constructive character.

In financial applications this matters directly: portfolio optimization, risk-parity, and risk-management objectives are highly sensitive to the spectrum of the covariance matrix. Analytic eigenvalue control within the squeezing framework therefore provides not only structural validity but also transparent and tunable stability, allowing covariance estimates to be aligned explicitly with optimization requirements.

## II The Gerber Informational Quality Framework

The Gerber-IQ framework was designed to construct correlation matrices directly from structured co-movement statistics, bypassing the sample covariance and its associated noise. At its core lies a squeezing template, which maps pairs of asset returns into an alignment space and applies structured thresholds to separate informative co-movements from noise. The framework is parameterized by a collection of functional parameters that govern how evidence is aggregated:

* •

  𝐜=𝐜​(r0,c)\mathbf{c}=\mathbf{c}(r\_{0},c), which aligns marginal distributions on r0r\_{0} and defines the exclusion region for noise through cc,
* •

  𝜹\boldsymbol{\delta}, which sets the boundaries of the squeezing channels,
* •

  𝜼\boldsymbol{\eta}, which assigns squeezing weights to the various channels or channel classes,
* •

  γ\gamma, which governs temporal squeezing by reflecting the predictive value of signal based on recency,
* •

  ϵ\epsilon, which acts as a delay parameter for γ\gamma-activation, and
* •

  τ\tau, which specifies the lookback duration for the estimation sample.

We sometimes represent the collection of spatial parameters as 𝐬=𝐬​(𝐜,𝜹,𝜼)\mathbf{s}=\mathbf{s}(\mathbf{c},\boldsymbol{\delta},\boldsymbol{\eta}) and the temporal parameters as 𝐭=𝐭​(τ,ϵ,γ)\mathbf{t}=\mathbf{t}(\tau,\epsilon,\gamma).
These parameters can be set by an experienced analyst or, in part or in whole, learned within an optimization framework, for example by deep learning architectures such as Markowitz-Informed Neural Networks (minns2025ssrn).

Figure [1](https://arxiv.org/html/2512.23021v1#S2.F1 "Figure 1 ‣ II The Gerber Informational Quality Framework ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control") illustrates this alignment structure.
Panel (a) shows sample co-movement vectors; Panel (b) depicts the squeezing channels defined by 𝜹\boldsymbol{\delta} and 𝜼\boldsymbol{\eta}; Panel (c) overlays co-movement vectors
onto the template; and Panel (d) refines the structure into body, wing, and tail regions (or channel classes). This representation provides a clear and interpretable map from raw return pairs to a
structured statistical template.

![Refer to caption](fig_1.png)


Figure 1: 
Illustration of the 𝜹\boldsymbol{\delta}–𝜼\boldsymbol{\eta} alignment template:
co-movement vectors (a), squeezing channels (b), vectors on the template (c), and
refined body–tail–wing structure (d).

To compute IQ we refer to the squeezing template in Figure [1](https://arxiv.org/html/2512.23021v1#S2.F1 "Figure 1 ‣ II The Gerber Informational Quality Framework ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control"). This structure translates into statistical expressions that generate correlation matrix elements ρi​j​(t;𝐬,𝐭)\rho\_{ij}(t;\mathbf{s},\mathbf{t}), representing the IQ measure of co-movement between assets RiR\_{i} and RjR\_{j} at time tt. Let T:={0,1,…,τ−1}T:=\{0,1,\dots,\tau-1\} index the τ\tau observations in the lookback window, ordered from oldest to most recent, with times {tm}m∈T\{t\_{m}\}\_{m\in T}. For each asset RkR\_{k}, we define an exclusion region for transformed returns based on the noise threshold cc:

|  |  |  |
| --- | --- | --- |
|  | Mk:={m∈T:|r~k​(tm)|≤c}.M\_{k}:=\{m\in T:|\tilde{r}\_{k}(t\_{m})|\leq c\}. |  |

The threshold cc may be specified in asset-specific units, for example as a multiple of the sample standard deviation of asset kk, or in pairwise units based on an aggregate of the volatilities of assets ii and jj (such as min⁡{σ^i,σ^j}\min\{\hat{\sigma}\_{i},\hat{\sigma}\_{j}\}, max⁡{σ^i,σ^j}\max\{\hat{\sigma}\_{i},\hat{\sigma}\_{j}\}, or an average). From these, we form index sets over which the statistic is computed:

|  |  |  |
| --- | --- | --- |
|  | E∪:=T∖(Mi∪Mj),E∩:=T∖(Mi∩Mj).E\_{\cup}:=T\setminus(M\_{i}\cup M\_{j}),\qquad E\_{\cap}:=T\setminus(M\_{i}\cap M\_{j}). |  |

We then define indicator functions for concordant and discordant co-movement:

|  |  |  |
| --- | --- | --- |
|  | I+​(tm)={1if ​r~i​(tm)​r~j​(tm)>0,0otherwise,I−​(tm)={1if ​r~i​(tm)​r~j​(tm)<0,0otherwise.I^{+}(t\_{m})=\begin{cases}1&\text{if }\tilde{r}\_{i}(t\_{m})\,\tilde{r}\_{j}(t\_{m})>0,\\ 0&\text{otherwise},\end{cases}\qquad I^{-}(t\_{m})=\begin{cases}1&\text{if }\tilde{r}\_{i}(t\_{m})\,\tilde{r}\_{j}(t\_{m})<0,\\ 0&\text{otherwise}.\end{cases} |  |

Let η​(tm;ω​(𝐜,𝜹))\eta(t\_{m};\omega(\mathbf{c},\boldsymbol{\delta})) denote the squeezing weight assigned to the co-movement (r~i​(tm),r~j​(tm))(\tilde{r}\_{i}(t\_{m}),\tilde{r}\_{j}(t\_{m})), where the channel ω​(𝐜,𝜹)\omega(\mathbf{c},\boldsymbol{\delta}) is determined by the spatial parameters 𝐜\mathbf{c} and 𝜹\boldsymbol{\delta}. The IQ squeezing statistic is then defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρi​j​(t;𝐬,𝐭)=∑m∈E∪Δ​(tm)​η​(tm;ω​(𝐜,𝜹))​v​(tm;𝐭)∑m∈E∩η​(tm;ω​(𝐜,𝜹))​v​(tm;𝐭),\rho\_{ij}(t;\mathbf{s},\mathbf{t})\;=\;\frac{\sum\_{m\in E\_{\cup}}\Delta(t\_{m})\,\eta(t\_{m};\omega(\mathbf{c},\boldsymbol{\delta}))\,v(t\_{m};\mathbf{t})}{\sum\_{m\in E\_{\cap}}\eta(t\_{m};\omega(\mathbf{c},\boldsymbol{\delta}))\,v(t\_{m};\mathbf{t})}, |  | (1) |

where Δ​(tm)=I+​(tm)−I−​(tm)\Delta(t\_{m})=I^{+}(t\_{m})-I^{-}(t\_{m}). The numerator aggregates evidence of concordant and discordant co-movements when both transformed returns exceed the noise threshold cc, while the denominator aggregates evidence when at least one transformed return exceeds the threshold.

Temporal effects are incorporated through the discount factor

|  |  |  |
| --- | --- | --- |
|  | v​(tm;𝐭)=exp⁡(−γ​(τ−1−(m+ϵ))+),m∈{0,1,…,τ−1}.v(t\_{m};\mathbf{t})=\exp\!\Big(-\,\gamma\,(\tau-1-(m+\epsilon))\_{+}\Big),\qquad m\in\{0,1,\dots,\tau-1\}. |  |

where ϵ\epsilon is the delay parameter, γ>0\gamma>0 is the decay parameter, and τ\tau denotes the lookback window duration, which determines the index set over which v​(tm;𝐭)v(t\_{m};\mathbf{t}) is evaluated.

This element-level construction translates naturally to the system-wide representation. At the matrix level, IQ correlation matrices can be expressed through the canonical squeezing identity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S≡∑α∈𝒦ηα​C(α)+(1−∑α∈𝒦ηα)​I,S\;\equiv\;\sum\_{\alpha\in\mathcal{K}}\eta\_{\alpha}\,C^{(\alpha)}\;+\;\left(1-\sum\_{\alpha\in\mathcal{K}}\eta\_{\alpha}\right)I, |  | (2) |

where the coefficients {ηα}\{\eta\_{\alpha}\} are channel-class squeezing weights and each C(α)C^{(\alpha)} is a channel-class matrix. Channels are the non-overlapping regions of the bivariate support defined by the template parameters 𝜹\boldsymbol{\delta} and 𝐜\mathbf{c}. In practice, channels are grouped into broader channel classes, α∈𝒦\alpha\in\mathcal{K}, such as body, wing, and tail (Figure 1(d)), with all channels in a class allocated the same squeezing weight. The matrices C(α)C^{(\alpha)} should therefore be interpreted as correlation matrices constructed from data passing through particular channel classes. Operational details for implementing the body, wing, and tail channel classes, and the noise-exclusion band, are provided in the appendix.

In the next section we turn to how these channel-class matrices are constructed from atomic building blocks and why this guarantees positive semi-definiteness by design.

## III Atomic–IQ: PSD by Design

The canonical squeezing identity expresses the estimator as a balance between a zero‑correlation benchmark and a structured component assembled from co‑movement evidence. In this view, ([2](https://arxiv.org/html/2512.23021v1#S2.E2 "Equation 2 ‣ II The Gerber Informational Quality Framework ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) implements an endogenous zero‑correlation prior, while the class matrices {C(α)}\{C^{(\alpha)}\} provide data‑driven, objective-led adjustments. The coefficients {ηα}\{\eta\_{\alpha}\} tune the trade‑off, allowing the estimator to range from near‑neutral (close to zero correlation) to strongly structured dependence. The neutral share 1−∑αηα1-\sum\_{\alpha}\eta\_{\alpha} keeps a measurable portion of the estimate anchored at the benchmark, and the structured share ∑αηα​C(α)\sum\_{\alpha}\eta\_{\alpha}C^{(\alpha)} moves the estimate away from it in directions and magnitudes supported by the evidence. In short, neutrality is not discarded; it is modulated according to where the information lies across statistical and temporal channels.

An immediate qualitative feature follows. The collective squeeze ∑αηα\sum\_{\alpha}\eta\_{\alpha} determines the overall balance between the neutral benchmark and the structured component. When the collective squeeze is less than one, PSD is guaranteed. Once it exceeds one, PSD is no longer automatic and holds only under additional spectral conditions. The remainder of this section turns to how atomic–IQ constructs the structured component from positive semi‑definite building blocks, and why PSD is preserved when the collective squeeze does not exceed unity.

### A Building Blocks: Atoms, Aggregation and Scaling

At the event level each concordant/discordant co‑movement between assets RiR\_{i} and RjR\_{j} contributes a 2×22\times 2 atom

|  |  |  |  |
| --- | --- | --- | --- |
|  | A+=[1111],A−=[1−1−11],A^{+}=\begin{bmatrix}1&1\\[2.0pt] 1&1\end{bmatrix},\qquad A^{-}=\begin{bmatrix}1&-1\\[2.0pt] -1&1\end{bmatrix}, |  | (3) |

which is embedded into the (i,j)(i,j) block of the n×nn\times n correlation template via the selector

|  |  |  |
| --- | --- | --- |
|  | Ji​j:=[ei​ej]∈ℝn×2,X↦Ji​j​X​Ji​j⊤.J\_{ij}:=[\,e\_{i}\ e\_{j}\,]\in\mathbb{R}^{n\times 2},\qquad X\mapsto J\_{ij}XJ\_{ij}^{\top}. |  |

Let e=(i,j,t)e=(i,j,t) index an event involving RiR\_{i} and RjR\_{j} at time tt, with sign πe∈{+,−}\pi\_{e}\in\{+,-\}. We may represent a per‑event scaled atom as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ae:=𝒮e​[Aπe],{A}\_{e}:=\mathcal{S}\_{e}\!\left[A^{\,\pi\_{e}}\right], |  | (4) |

where 𝒮e\mathcal{S}\_{e} is a PSD‑preserving scaling operator. Two concrete choices (whole‑atom vs off‑diagonal‑only) are given later; for now ([4](https://arxiv.org/html/2512.23021v1#S3.E4 "Equation 4 ‣ A Building Blocks: Atoms, Aggregation and Scaling ‣ III Atomic–IQ: PSD by Design ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) covers both and implicitly carries any temporal or magnitude effects. Events are grouped into classes α∈𝒦\alpha\in\mathcal{K} by the squeezing template. The class accumulator matrix is the sum of embedded scaled atoms:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gα=∑e∈αJi​jAeJi​j.⊤G\_{\alpha}=\sum\_{e\in\alpha}J\_{ij}\,{A}\_{e}\,J^{\phantom{\top}}\_{ij}{}^{\top}. |  | (5) |

If 𝒮e\mathcal{S}\_{e} preserves positive semi‑definiteness, each addend in ([5](https://arxiv.org/html/2512.23021v1#S3.E5 "Equation 5 ‣ A Building Blocks: Atoms, Aggregation and Scaling ‣ III Atomic–IQ: PSD by Design ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) is PSD and hence Gα⪰0G\_{\alpha}\succeq 0. When all qualifying events in a lookback window have been accounted for, each class aggregator GαG\_{\alpha} is normalized to correlation scale,

|  |  |  |  |
| --- | --- | --- | --- |
|  | C(α)=Dα−12​Gα​Dα−12,Dα:=diag​(Gα),C^{(\alpha)}=D\_{\alpha}^{-\tfrac{1}{2}}\,G\_{\alpha}\,D\_{\alpha}^{-\tfrac{1}{2}},\qquad D\_{\alpha}:=\mathrm{diag}(G\_{\alpha}), |  | (6) |

which preserves PSD status. Thus, each class matrix C(α)C^{(\alpha)} is a PSD correlation matrix. A useful by‑product is refinement invariance: splitting a class into sub‑channels, summing first, and normalizing once yields the same C(α)C^{(\alpha)} as treating the class as a single block.

Eqs. ([5](https://arxiv.org/html/2512.23021v1#S3.E5 "Equation 5 ‣ A Building Blocks: Atoms, Aggregation and Scaling ‣ III Atomic–IQ: PSD by Design ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control"))–([6](https://arxiv.org/html/2512.23021v1#S3.E6 "Equation 6 ‣ A Building Blocks: Atoms, Aggregation and Scaling ‣ III Atomic–IQ: PSD by Design ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) complete the structured component; the squeezing identity then blends the class matrices with the neutral benchmark as in Section 4.

There are two scaling modes for 𝒮e\mathcal{S}\_{e}: whole‑atom scaling (atomic-IQ1) and off-diagonal scaling (atomic-IQ2). In whole-atom scaling the entire 2×22\times 2 atom receives the same positive weight ata\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮eIQ1​[Aπe]=vt​Aπe=(at​I2)​Aπe​(at​I2),\mathcal{S}\_{e}^{\mathrm{IQ1}}\!\left[A^{\,\pi\_{e}}\right]=v\_{t}\,A^{\,\pi\_{e}}=\big(\sqrt{a\_{t}}\,I\_{2}\big)\,A^{\,\pi\_{e}}\,\big(\sqrt{a\_{t}}\,I\_{2}\big), |  | (7) |

a PSD‑preserving congruence. This modulates qualifying movement and co‑movement together. In off‑diagonal scaling, qualifying movement (diagonal) and co‑movement (off‑diagonal) are decoupled by applying a PSD mask entrywise (Hadamard product). Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(v)=[1vv1],|v|≤1,H(v)=\begin{bmatrix}1&v\\[2.0pt] v&1\end{bmatrix},\qquad|v|\leq 1, |  | (8) |

so H​(v)⪰0H(v)\succeq 0. For event ee with sign πe\pi\_{e}, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮eIQ2​[Aπe]=H​(vt)∘Aπe=1+vt2​Aπe+1−vt2​A−πe.\mathcal{S}\_{e}^{\mathrm{IQ2}}\!\left[A^{\,\pi\_{e}}\right]=H(v\_{t})\circ A^{\,\pi\_{e}}=\tfrac{1+v\_{t}}{2}\,A^{\,\pi\_{e}}+\tfrac{1-v\_{t}}{2}\,A^{-\,\pi\_{e}}. |  | (9) |

Since both H​(vt)H(v\_{t}) and AπeA^{\,\pi\_{e}} are PSD, the Schur product theorem ensures 𝒮eIQ2​[Aπe]⪰0\mathcal{S}\_{e}^{\mathrm{IQ2}}\!\left[A^{\,\pi\_{e}}\right]\succeq 0. In effect, events retain their occurrence counts, while their co-movement is scaled by vtv\_{t}.

The profiling factor vtv\_{t} is determined through temporal scaling. Patterns of co-movement change over time: regimes shift, volatility clusters, and the strength of association between assets may vary within a given lookback window. Temporal scaling lets the estimator adapt by adjusting how much weight each instant contributes to the structured component. In particular, it allows the model to learn whether evidence nearer one end of the lookback window or the other carries greater informational value in the current window. This directional temporal decay is a departure from the original Gerber–IQ formalism, which discounts only into the past from the most recent observation. This flexibility is a modeling advantage, but it raises technical considerations for preserving PSD (especially under Hadamard/entrywise masking in atomic-IQ2), maintaining interpretational symmetry between opposite time–directions, and ensuring numerical stability.

To illustrate this we write t=0,…,τ−1t=0,\dots,\tau\!-\!1 to index the window from oldest to most recent, and define

|  |  |  |  |
| --- | --- | --- | --- |
|  | at=exp⁡(−γ​(τ−1−(t+ϵ))+),(x)+:=max⁡{x,0},a\_{t}\;=\;\exp\!\Big(-\,\gamma\,(\tau-1-(t+\epsilon))\_{+}\Big),\qquad(x)\_{+}:=\max\{x,0\}, |  | (10) |

with delay ϵ≥0\epsilon\geq 0. Interpreting γ\gamma as the temporal-scaling parameter, γ>0\gamma>0 downweights older evidence, while γ<0\gamma<0 upweights it. For whole-atom scaling (atomic-IQ1), PSD is unaffected because at>0a\_{t}>0 simply rescales PSD atoms. However, more generally, two issues emerge: (i) we have interpretational asymmetry because transformations induced by +γ+\gamma and −γ-\gamma are not mirror images; and (ii) in off-diagonal scaling (atomic-IQ2), taking vt=atv\_{t}=a\_{t} can yield vt>1v\_{t}>1 when γ<0\gamma<0, violating the Schur bound |vt|≤1|v\_{t}|\leq 1 thereby breaking the PSD guarantee under Hadamard masking.

To resolve both points, we separate magnitude and direction via a signed profile. Let the sign of γ\gamma direct which edge of the window defines *distance*, and let |γ||\gamma| control the decay rate in that direction. This gives,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ageγ⁡(t)={τ−1−t,γ≥0,t,γ<0,at=exp⁡(−|γ|​(ageγ⁡(t)−ϵ)+)∈(0,1].\operatorname{age}\_{\gamma}(t)\;=\;\begin{cases}\tau-1-t,&\gamma\geq 0,\\[3.0pt] t,&\gamma<0,\end{cases}\qquad a\_{t}\;=\;\exp\!\Big(-\,|\gamma|\,(\operatorname{age}\_{\gamma}(t)-\epsilon)\_{+}\Big)\in(0,1]. |  | (11) |

With ([11](https://arxiv.org/html/2512.23021v1#S3.E11 "Equation 11 ‣ A Building Blocks: Atoms, Aggregation and Scaling ‣ III Atomic–IQ: PSD by Design ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")), atomic-IQ1 continues to scale entire atoms by ata\_{t}, preserving PSD. Atomic-IQ2 sets vt=atv\_{t}=a\_{t}, which automatically respects |vt|≤1|v\_{t}|\leq 1. Additionally, positive/negative γ\gamma now enjoy interpretational symmetry. The informative edge (recent vs. oldest) is now determined by sign⁡(γ)\operatorname{sign}(\gamma) while |γ||\gamma| sets the decay rate. The delay parameter ϵ\epsilon creates a flat shelf at the chosen edge before decay begins.

For gradient-based estimation, one may smooth the kink at γ=0\gamma=0 without changing semantics, e.g.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | w​(γ)\displaystyle w(\gamma) | =12​(1+tanh⁡(κ​γ))\displaystyle=\tfrac{1}{2}\bigl(1+\tanh(\kappa\gamma)\bigr) |  | (12) |
|  | at\displaystyle a\_{t} | =exp⁡(−|γ|~​(ageγ⁡(t)−ϵ)+)\displaystyle=\exp\!\Big(-\,\widetilde{|\gamma|}\,(\operatorname{age}\_{\gamma}(t)-\epsilon)\_{+}\Big) |  |
|  | ageγ⁡(t)\displaystyle\operatorname{age}\_{\gamma}(t) | =w​(γ)​(τ−1−t)+(1−w​(γ))​t\displaystyle=w(\gamma)(\tau-1-t)+\bigl(1-w(\gamma)\bigr)t |  |
|  | |γ|~\displaystyle\widetilde{|\gamma|} | =γ2+εγ2\displaystyle=\sqrt{\gamma^{2}+\varepsilon\_{\gamma}^{2}} |  |

with small εγ>0\varepsilon\_{\gamma}>0 and moderate κ>0\kappa>0, providing C∞C^{\infty} continuity at γ=0\gamma=0 and avoiding numerical artefacts. Modern gradient-based methods typically handle the unsmoothed kink without difficulty; the smoothed form is included out of caution rather than necessity.

In practice, atomic-IQ1 and atomic-IQ2 behave differently but coherently under this scheme. In the former, each event contributes at​Aπea\_{t}A^{\pi\_{e}}, so diagonals (qualifying event) and off-diagonals (associated co-movement) are modulated together; uniform rescaling of {at}\{a\_{t}\} cancels after normalization, only the shape of the temporal profile matters. In the latter, diagonals accumulate counts while off-diagonals are tempered by ata\_{t}. Increasing |γ||\gamma| downweights co-movement evidence, thereby moderating pairwise alignment relative to event occurrence, with the effect becoming stronger the further one moves from the chosen edge.

Two simple diagnostics make runs comparable across datasets and windows. The first is the effective mass,

|  |  |  |  |
| --- | --- | --- | --- |
|  | τeff=∑t=0τ−1at,\tau\_{\mathrm{eff}}\;=\;\sum\_{t=0}^{\tau-1}a\_{t}, |  | (13) |

which measures the total weight assigned across the window. In atomic-IQ1 this captures how much of the window contributes to the structured component, while in atomic-IQ2 it indicates the relative strength with which co-movement is being tempered against raw activity.

The second is the weighted mean age,

|  |  |  |  |
| --- | --- | --- | --- |
|  | age¯=∑t=0τ−1at​ageγ⁡(t)∑t=0τ−1at,\overline{\mathrm{age}}\;=\;\frac{\sum\_{t=0}^{\tau-1}a\_{t}\,\operatorname{age}\_{\gamma}(t)}{\sum\_{t=0}^{\tau-1}a\_{t}}, |  | (14) |

which locates the center of mass of the profile. In atomic-IQ1 it summarizes which portion of the window most influences C(α)C^{(\alpha)}, and in atomic-IQ2 it clarifies where correlations are most heavily adjusted relative to event occurrence. Reporting (τeff,age¯)(\tau\_{\mathrm{eff}},\overline{\mathrm{age}}) alongside (γ,ϵ)(\gamma,\epsilon) makes runs interpretable and comparable across datasets and window lengths.

## IV Spectral Regimes

The canonical squeezing identity

|  |  |  |
| --- | --- | --- |
|  | S≡∑α∈𝒦ηα​C(α)+(1−∑α∈𝒦ηα)​IS\;\equiv\;\sum\_{\alpha\in\mathcal{K}}\eta\_{\alpha}\,C^{(\alpha)}\;+\;\left(1-\sum\_{\alpha\in\mathcal{K}}\eta\_{\alpha}\right)I |  |

expresses the estimator as a balance between the neutral benchmark II and the contributions of the channel classes. It is convenient to rewrite this in a compact form. Let

|  |  |  |
| --- | --- | --- |
|  | ξ:=∑α∈𝒦ηα,P:=1ξ​∑α∈𝒦ηα​C(α)(ξ>0).\xi:=\sum\_{\alpha\in\mathcal{K}}\eta\_{\alpha},\qquad P:=\frac{1}{\xi}\sum\_{\alpha\in\mathcal{K}}\eta\_{\alpha}\,C^{(\alpha)}\quad(\xi>0). |  |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | S=(1−ξ)​I+ξ​P.S\;=\;(1-\xi)I\;+\;\xi P. |  | (15) |

This representation shows that the estimator lies on the line segment between the neutral benchmark II and the squeezing blend PP when ξ≤1\xi\leq 1, and continues beyond PP when ξ>1\xi>1. It is important to emphasize that neither II nor PP are exogenous features; both are endogenous constructs intrinsic to the IQ framework. In particular, PP is not an external target but an internally generated average of channel-class matrices defined within the model.

When the collective squeeze satisfies ξ≪1\xi\ll 1, the estimator

|  |  |  |
| --- | --- | --- |
|  | S=(1−ξ)​I+ξ​P≈I+ξ​(P−I)S\;=\;(1-\xi)I+\xi P\;\approx\;I+\xi(P-I) |  |

can be viewed as a perturbation of the identity benchmark by a small, structured deviation P−IP-I. In this regime, the IQ framework naturally enters a perturbative form, reminiscent of classical perturbation theory, where the response of a system is analyzed as a first-order correction to an unperturbed state. Here, P−IP-I plays the role of a data-driven perturbation operator, and ξ\xi controls its magnitude. The analogy highlights that the squeezing operation constitutes not merely an interpolation between two matrices, but a controlled perturbative deformation of II governed by interpretable, learned parameters.

This observation opens a potentially fruitful line of interpretation: the perturbative squeezing regime. In this view, SS may be regarded as the first term of a data-driven perturbation expansion, where higher-order corrections could, in principle, capture increasingly refined spectral interactions among the endogenous channel classes. Unlike conventional perturbation theory, the perturbation here is not exogenous but arises endogenously from the data itself, through the structured learning of the IQ parameters. Consequently, the matrix PP can be interpreted as a tunable, positive semidefinite perturbation that embodies information-driven adjustments to the neutral benchmark.

This framing suggests that the Atomic-IQ architecture could be extended into a broader theory of data-driven perturbation of PSD operators. In portfolio optimization this perspective connects naturally with ideas of robustness and controlled deviation, where II represents neutrality or independence, and PP encodes structured dependencies inferred from data. Although not developed further here, this conceptual link to perturbation theory may offer a promising analytical bridge between interpretable learning and spectral sensitivity analysis, and thus provides an avenue for future theoretical exploration.

Having introduced the conceptual interpretation of SS as a perturbative blend of II and PP, we now turn to its spectral implications, which can be derived directly from the compact form in ([15](https://arxiv.org/html/2512.23021v1#S4.E15 "Equation 15 ‣ IV Spectral Regimes ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control"))

The eigenvalues of SS follow directly from ([15](https://arxiv.org/html/2512.23021v1#S4.E15 "Equation 15 ‣ IV Spectral Regimes ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")). If λi​(P)\lambda\_{i}(P) denotes the spectrum of PP, then

|  |  |  |
| --- | --- | --- |
|  | λi​(S)=(1−ξ)+ξ​λi​(P).\lambda\_{i}(S)\;=\;(1-\xi)+\xi\,\lambda\_{i}(P). |  |

It follows that

|  |  |  |
| --- | --- | --- |
|  | S⪰0⟺(1−ξ)+ξ​λmin​(P)≥0.S\succeq 0\;\Longleftrightarrow\;(1-\xi)+\xi\,\lambda\_{\min}(P)\geq 0. |  |

Two regimes emerge. When ξ≤1\xi\leq 1, this inequality always holds provided the channel‑class matrices are positive semi‑definite, which they are in atomic-IQ, so positive semi‑definiteness is guaranteed. When ξ>1\xi>1, positive semi‑definiteness is no longer automatic and holds only if the smallest eigenvalue of PP exceeds the threshold 1−1/ξ1-1/\xi.

In general, the collective squeeze ξ\xi is a free parameter, and choosing ξ<1\xi<1 is always an available option that guarantees positive semi‑definiteness regardless of the detailed structure of PP. In the original IQ paper (gerberiqssrn), however, we collapsed three class weights into a single parameter by making a specific allocation judgment: the tail class received full weight, the body class weight η\eta, and the wing class weight η2\eta^{2}. This yields what we refer to as basic–IQ. A consequence of this parameterization is that the collective squeeze becomes

|  |  |  |
| --- | --- | --- |
|  | ξ​(η)=1+η+η2,\xi(\eta)=1+\eta+\eta^{2}, |  |

which exceeds unity for any η>0\eta>0. Thus basic–IQ operates in the regime where positive semi‑definiteness is conditional. In earlier work this was handled by applying Higham’s (higham2002computing) projection whenever the estimator was indefinite; with the spectral condition in hand we can now state explicitly when the basic–IQ estimator will be positive semi‑definite.

In the basic–IQ case the structured blend is

|  |  |  |
| --- | --- | --- |
|  | P​(η)=C(T)+η​C(B)+η2​C(W)1+η+η2,P(\eta)=\frac{C^{(T)}+\eta\,C^{(B)}+\eta^{2}\,C^{(W)}}{1+\eta+\eta^{2}}, |  |

so the condition becomes

|  |  |  |
| --- | --- | --- |
|  | λmin​(P​(η))≥η+η21+η+η2.\lambda\_{\min}\!\big(P(\eta)\big)\;\geq\;\frac{\eta+\eta^{2}}{1+\eta+\eta^{2}}. |  |

This criterion is necessary and sufficient. As η\eta approaches one, the weighting becomes uniform across classes and the template boundaries (which vanish at η=1\eta=1) cease to affect the construction; the squeezed blend must move increasingly close to the identity in spectral terms to return a PSD matrix. More generally, as η\eta increases from zero the requirement tightens smoothly.

In practice it can be useful to replace this exact test with bounds that depend only on the class eigenvalue minima. Let mB=λmin​(C(B))m\_{B}=\lambda\_{\min}(C^{(B)}), mW=λmin​(C(W))m\_{W}=\lambda\_{\min}(C^{(W)}), and mT=λmin​(C(T))m\_{T}=\lambda\_{\min}(C^{(T)}). A simple sufficient condition is

|  |  |  |
| --- | --- | --- |
|  | η2​(1−mT)+η​(1−mW)≤mB,\eta^{2}(1-m\_{T})\;+\;\eta(1-m\_{W})\;\leq\;m\_{B}, |  |

while a necessary condition is

|  |  |  |
| --- | --- | --- |
|  | η2+η≤mmax1−mmax,mmax=max⁡{mB,mW,mT}.\eta^{2}+\eta\;\leq\;\frac{m\_{\max}}{1-m\_{\max}},\qquad m\_{\max}=\max\{m\_{B},m\_{W},m\_{T}\}. |  |

These inequalities describe feasible ranges of η\eta given information about the extremal eigenvalues of the class matrices. Proofs (with some routine steps omitted for brevity) for these spectral mapping and feasibility results, together with formulas for choosing the eigenfloor parameter to target a minimum eigenvalue or condition number, are given in the appendix.

## V Eigenfloor and Conditioning

The spectral analysis in the previous section distinguishes a guaranteed regime, where the collective squeeze ξ≤1\xi\leq 1, from a conditional regime, where ξ>1\xi>1. In both settings it may be desirable to exercise explicit control over numerical conditioning. To this end we introduce an identity reserve, termed the *eigenfloor*, which contracts the spectrum toward unity while remaining entirely within the squeezing framework.

### A The Eigenfloor Mechanism

The eigenfloor is defined for ϕ∈[0,1]\phi\in[0,1] by

|  |  |  |  |
| --- | --- | --- | --- |
|  | S^​(ϕ)=(1−ϕ)​S+ϕ​I.\widehat{S}(\phi)\;=\;(1-\phi)\,S\;+\;\phi\,I. |  | (16) |

Substituting the canonical squeezing form S=∑αηα​C(α)+(1−ξ)​IS=\sum\_{\alpha}\eta\_{\alpha}C^{(\alpha)}+\bigl(1-\xi\bigr)I with ξ=∑αηα\xi=\sum\_{\alpha}\eta\_{\alpha} yields

|  |  |  |
| --- | --- | --- |
|  | S^​(ϕ)=(1−ϕ)​∑αηα​C(α)+((1−ϕ)​(1−ξ)+ϕ)​I,\widehat{S}(\phi)\;=\;(1-\phi)\sum\_{\alpha}\eta\_{\alpha}C^{(\alpha)}\;+\;\bigl((1-\phi)(1-\xi)+\phi\bigr)I, |  |

which can be rearranged into the canonical representation with rescaled weights:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S^​(ϕ)=∑α(1−ϕ)​ηα​C(α)+(1−(1−ϕ)​ξ)​I.\widehat{S}(\phi)\;=\;\sum\_{\alpha}(1-\phi)\,\eta\_{\alpha}\,C^{(\alpha)}\;+\;\Bigl(1-(1-\phi)\,\xi\Bigr)\,I. |  | (17) |

Equivalently, writing S=(1−ξ)​I+ξ​P=I+ξ​(P−I)S=(1-\xi)I+\xi P=I+\xi(P-I),

|  |  |  |  |
| --- | --- | --- | --- |
|  | S^​(ϕ)=I+(1−ϕ)​ξ⏟ξeff​(P−I),\widehat{S}(\phi)\;=\;I\;+\;\underbrace{(1-\phi)\,\xi}\_{\xi\_{\text{eff}}}\,(P-I), |  | (18) |

so the squeezing semantics are preserved: the class weights rescale to ηα′=(1−ϕ)​ηα\eta^{\prime}\_{\alpha}=(1-\phi)\eta\_{\alpha}, and the effective collective squeeze reduces from ξ\xi to ξeff=(1−ϕ)​ξ\xi\_{\text{eff}}=(1-\phi)\xi.

Since II commutes with SS, the eigenvalues transform affinely:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λi​(S^​(ϕ))=(1−ϕ)​λi​(S)+ϕ.\lambda\_{i}\bigl(\widehat{S}(\phi)\bigr)\;=\;(1-\phi)\,\lambda\_{i}(S)+\phi. |  | (19) |

Each eigenvalue therefore moves toward 11. The spectral spread contracts: λmin\lambda\_{\min} is nondecreasing, λmax\lambda\_{\max} is nonincreasing, and for correlation-type matrices (trace =N=N, where NN is the number of assets) the mean eigenvalue remains 11. Consequently, the floor simultaneously lowers the top of the spectrum and raises the bottom, improving numerical conditioning while leaving the total variance unchanged.

### B Targeted Conditioning and PSD Repair

Let α=λmax​(S)\alpha=\lambda\_{\max}(S) and β=λmin​(S)\beta=\lambda\_{\min}(S). Two closed-form rules allow one to choose tt to achieve a desired spectral property.

#### Target minimum eigenvalue.

For a specified λ¯∈[0,1]\underline{\lambda}\in[0,1], equation ([19](https://arxiv.org/html/2512.23021v1#S5.E19 "Equation 19 ‣ A The Eigenfloor Mechanism ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−ϕ)​β+ϕ≥λ¯⟺ϕ≥λ¯−β 1−β(β<1).(1-\phi)\,\beta+\phi\;\geq\;\underline{\lambda}\quad\Longleftrightarrow\quad\phi\;\geq\;\frac{\underline{\lambda}-\beta}{\,1-\beta\,}\qquad(\beta<1). |  | (20) |

Clamping to the admissible range yields

|  |  |  |
| --- | --- | --- |
|  | ϕmin​(λ¯)=[(λ¯−β)/(1−β)]0 1.\phi\_{\min}(\underline{\lambda})\;=\;\Bigl[\;(\underline{\lambda}-\beta)/(1-\beta)\;\Bigr]\_{0}^{\,1}. |  |

If λ¯=0\underline{\lambda}=0 and β≥0\beta\geq 0, no floor is required and one may set ϕ=0\phi=0; if β<0\beta<0, then ϕmin​(0)=−β/(1−β)∈(0,1)\phi\_{\min}(0)=-\beta/(1-\beta)\in(0,1) is the smallest floor that restores positive semidefiniteness.

#### Target condition number.

For a desired condition number K≥1K\geq 1 and β>0\beta>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ≥α−K​β(α−1)+K​(1−β).\phi\;\geq\;\frac{\alpha-K\beta}{\,(\alpha-1)+K(1-\beta)\,}. |  | (21) |

If β≤0\beta\leq 0, first apply ([20](https://arxiv.org/html/2512.23021v1#S5.E20 "Equation 20 ‣ Target minimum eigenvalue. ‣ B Targeted Conditioning and PSD Repair ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) to ensure λmin​(S^​(ϕ))>0\lambda\_{\min}(\widehat{S}(\phi))>0, then use ([21](https://arxiv.org/html/2512.23021v1#S5.E21 "Equation 21 ‣ Target condition number. ‣ B Targeted Conditioning and PSD Repair ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) on the updated spectrum. These expressions provide closed-form tuning rules for analytic PSD repair and explicit conditioning control without numerical optimization.

### C Application in Conditional Regimes

In atomic–IQ each C(α)C^{(\alpha)} is positive semidefinite, implying P⪰0P\succeq 0 and λmin​(P)∈[0,1]\lambda\_{\min}(P)\in[0,1]. When ξ>1\xi>1 and no information on λmin​(P)\lambda\_{\min}(P) is available, the bound λmin​(S)≥(1−ξ)+ξ⋅0=1−ξ\lambda\_{\min}(S)\geq(1-\xi)+\xi\cdot 0=1-\xi implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ≥ 1−1ξ\phi\;\geq\;1-\frac{1}{\xi} |  | (22) |

guarantees S^​(ϕ)⪰0\widehat{S}(\phi)\succeq 0 irrespective of PP. If a lower bound λmin​(P)≥μ∈[0,1]\lambda\_{\min}(P)\geq\mu\in[0,1] is known, then λmin​(S)≥(1−ξ)+ξ​μ\lambda\_{\min}(S)\geq(1-\xi)+\xi\mu and the required floor can be reduced to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ≥max⁡{ 0, 1−1ξ​(1−μ)}.\phi\;\geq\;\max\Bigl\{\,0,\ 1-\frac{1}{\xi(1-\mu)}\,\Bigr\}. |  | (23) |

For the basic–IQ parameterization ξ​(η)=1+η+η2\xi(\eta)=1+\eta+\eta^{2}, the conservative choice ([22](https://arxiv.org/html/2512.23021v1#S5.E22 "Equation 22 ‣ C Application in Conditional Regimes ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) becomes ϕ≥1−1/(1+η+η2)\phi\geq 1-1/\bigl(1+\eta+\eta^{2}\bigr).

Although ([16](https://arxiv.org/html/2512.23021v1#S5.E16 "Equation 16 ‣ A The Eigenfloor Mechanism ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) resembles shrinkage toward the identity, equations ([17](https://arxiv.org/html/2512.23021v1#S5.E17 "Equation 17 ‣ A The Eigenfloor Mechanism ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) and ([18](https://arxiv.org/html/2512.23021v1#S5.E18 "Equation 18 ‣ A The Eigenfloor Mechanism ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) show that the eigenfloor remains fully internal to the squeezing representation. It constitutes a re-parameterization that rescales the class weights and increases the endogenous identity share. Hence it performs two roles simultaneously: an analytic PSD-restoring mechanism when SS is indefinite, and an explicit conditioning control when SS is already PSD.

If SS already meets the desired conditioning, set ϕ=0\phi=0. Small floors such as t∈[0.02,0.05]t\in[0.02,0.05] often stabilize optimization without materially altering class semantics. When only ξ\xi is known, the conservative bound ([22](https://arxiv.org/html/2512.23021v1#S5.E22 "Equation 22 ‣ C Application in Conditional Regimes ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) ensures PSD; when partial spectral information on PP is available, the refined bound ([23](https://arxiv.org/html/2512.23021v1#S5.E23 "Equation 23 ‣ C Application in Conditional Regimes ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) is tighter and typically sufficient in practice.

The analytic framework developed in Sections III–V establishes atomic–IQ as a constructive and spectrally controlled covariance estimator. By combining atomic building blocks, the canonical squeezing identity, and the eigenfloor mechanism, the estimator achieves both interpretability and explicit eigenvalue regulation. Having derived these properties in closed form, it is natural to ask how atomic–IQ behaves in practice when used within an economically meaningful optimization task. The next section addresses this question empirically, situating the estimator alongside established covariance models in a realistic portfolio-optimization setting.

## VI Empirical Study: Tangency Portfolio on a Multi-Asset Universe

This section demonstrates the atomic–IQ framework in a practical portfolio optimization setting. The aim is not exhaustive benchmarking, but to illustrate how the analytic properties established earlier, positive semi-definiteness by design, closed-form eigenvalue control, and interpretability, translate into realized portfolio behavior. Using a diversified multi-asset universe and a tangency (maximum-Sharpe) objective, atomic–IQ is evaluated alongside representative estimators from shrinkage, random-matrix, and concordance-based families. The empirical design emphasizes transparency and replicability: all estimators share the same data, constraints, and turnover assumptions, isolating the contribution of covariance estimation itself.

### A Empirical Design

Purpose and scope.
The preceding sections developed atomic–IQ (AIQ) as a constructive, PSD-guaranteed estimator offering analytic control over eigenvalues through the canonical squeezing identity and the eigenfloor mechanism. This section positions AIQ relative to established estimators within a single, economically meaningful objective, the long-only tangency (maximum-Sharpe) portfolio. The empirical study is intentionally compact yet complete, providing a clear comparison of estimator behavior in a realistic multi-asset environment. It details the data universe, backtesting protocol, competing estimators, and evaluation metrics, establishing a direct link between analytic properties and portfolio-level outcomes.

Asset universe and data.
We reuse the 10‑asset universe from the IQ study (gerberiqssrn): five equity indices (U.S. large‑cap, U.S. small‑cap, developed ex‑U.S., emerging markets, and U.S. growth), two bond indices (aggregate and high‑yield), listed real estate, gold, and a broad commodities index. We work with monthly total returns from January 1988 to December 2024 and rebalance monthly.

Many covariance estimators in the literature are motivated by high dimensional asymptotics, and their optimality results are typically derived for regimes in which the cross sectional dimension is large relative to the sample length. Relatedly, the random matrix perspective we adopt is underpinned by Marchenko Pastur type limits, which are most informative when applied to larger universes. We nevertheless focus on a realistic N=10N=10 setting here, both for brevity and because ten asset universes remain common in strategic allocation and benchmark design. Readers interested in broader empirical evidence across alternative portfolio sizes and universes are referred to gerberiqssrn; all results reported there for the Gerber IQ estimator can be replicated with Atomic IQ.

Backtest protocol.
At each monthly decision date dd we estimate expected returns 𝝁^d\hat{\boldsymbol{\mu}}\_{d} and the covariance matrix 𝚺^d\hat{\boldsymbol{\Sigma}}\_{d} from a rolling lookback window of τ=20\tau{=}20 months, with 𝝁^d\hat{\boldsymbol{\mu}}\_{d} computed as the sample mean over the same window. We then solve the long-only tangency problem

|  |  |  |
| --- | --- | --- |
|  | max𝐰≥0, 1⊤​𝐰=1⁡𝐰⊤​𝝁^d𝐰⊤​𝚺^d​𝐰,\max\_{\mathbf{w}\geq 0,\ \mathbf{1}^{\top}\mathbf{w}=1}\ \frac{\mathbf{w}^{\top}\hat{\boldsymbol{\mu}}\_{d}}{\sqrt{\mathbf{w}^{\top}\hat{\boldsymbol{\Sigma}}\_{d}\,\mathbf{w}}}, |  |

apply the resulting weights for the subsequent month, and repeat. Transaction costs of 10 bps are charged on dollar turnover at each rebalance. The in-sample period (1988–1999) is used for hyperparameter selection, and out-of-sample performance is evaluated over January 2000–December 2024. When required, we enforce positive semi-definiteness using the analytic eigenfloor repair described above, preserving trace.

Hyperparameter selection. The atomic–IQ framework introduces a small number of design parameters that control how co-movement evidence is aggregated, including the alignment center r0r\_{0}, the volatility scaling scheme σrk\sigma\_{r\_{k}} used for standardization (which sets the implied units for the noise gate cc and the channel boundary δ\delta), the noise gate cc, the channel boundary δ\delta, the channel squeezing weights 𝜼\boldsymbol{\eta}, the temporal decay parameter γ\gamma, the temporal decay delay parameter ϵ\epsilon, the lookback duration parameter τ\tau, and, when used, the eigenfloor level ϕ\phi. Rather than tune these by hand, we treat them as hyperparameters and select them by data-driven search. To do so we employ Optuna, an open-source hyperparameter optimization library that implements adaptive sampling and early stopping strategies (akiba2019optuna), which allows us to explore the atomic–IQ parameter space efficiently without relying on a coarse grid search.

In the empirical study Optuna explores the ranges in Table [2](https://arxiv.org/html/2512.23021v1#S6.T2 "Table 2 ‣ A Empirical Design ‣ VI Empirical Study: Tangency Portfolio on a Multi-Asset Universe ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control"), with the noise gate fixed at c=0.5c=0.5 and the lookback duration fixed at τ=20\tau=20 months, which implies q=T/N=2q=T/N=2 in the N=10N=10 asset setting. The parameters r0r\_{0}, δ\delta, η\eta, γ\gamma, and ϵ\epsilon are treated as free variables and optimised over the corresponding ranges in Table [2](https://arxiv.org/html/2512.23021v1#S6.T2 "Table 2 ‣ A Empirical Design ‣ VI Empirical Study: Tangency Portfolio on a Multi-Asset Universe ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control"), with each candidate configuration evaluated by running the full tangency backtest on the in-sample period 1988–1999. Positive semi-definiteness is enforced using an eigenfloor ϕ\phi, but ϕ\phi is not treated as a single tuned scalar; instead we adopt the fixed repair policy of Section [V](https://arxiv.org/html/2512.23021v1#S5 "V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control").[C](https://arxiv.org/html/2512.23021v1#S5.SS3 "C Application in Conditional Regimes ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control") and compute the realised floor ϕd\phi\_{d} at each monthly covariance update. Specifically, with ξ\xi denoting the collective squeeze and PP the normalized structural component, we compute μ=λmin​(P)\mu=\lambda\_{\min}(P) and set ϕd=0\phi\_{d}=0 whenever the feasibility condition holds, otherwise we apply the tight analytic floor ϕd=max⁡{0, 1−[ξ​(1−μ)]−1}\phi\_{d}=\max\{0,\,1-[\xi(1-\mu)]^{-1}\} before forming the repaired estimator. For a given Optuna trial we then construct the corresponding AIQ1 or AIQ2 covariance estimator, solve the long-only tangency problem with 10 bp transaction costs at each monthly rebalance, and record the resulting after-cost Sharpe ratio. Optuna uses these scalar evaluations to concentrate the search in promising regions of the parameter space, delivering well-behaved parameter sets with a modest computational budget. The best-performing configuration for each member of the atomic–IQ family (AIQ1 and AIQ2) is then held fixed and carried forward into the out-of-sample evaluation from 2000 to 2024. To support reproducibility, we provide a reference implementation of the full pipeline in a public repository.111<https://doi.org/10.5281/zenodo.18069453>

Estimators compared.

We benchmark atomic–IQ against shrinkage, random‑matrix theory, and concordance‑based constructions, plus a historical sample covariance (HC) baseline. Table LABEL:tab:1 lists the families referred to in the results.

Table 1: Collection of candidate techniques for covariance matrix estimation against which atomic squeezing is tested. Testing is also performed against the untreated sample covariance matrix.

| Technique | Description |
| --- | --- |
| Shrinkage | |
| Linear (LS1) | Shrinkage toward a one-parameter matrix: all variances are equal, and all covariances are zero (ledoit2004well). |
| Linear (LS2) | Shrinkage toward a two-parameter matrix: all variances are equal, and all covariances are equal (ledoit1995essays). |
| Linear (LS3) | Shrinkage toward a constant-correlation matrix: the target matrix preserves the diagonal of the sample covariance matrix and sets all correlations equal (ledoit2004honey). |
| Linear (LS4) | Shrinkage toward a diagonal matrix: the target matrix preserves the sample variances and sets covariances to zero (ledoit1995essays). |
| Linear (LS5) | Shrinkage toward a one-factor market model where the factor is the cross-sectional average of the variables; variances are preserved (ledoit2003improved). |
| Non-linear (NLS1) | Geometric-inverse shrinkage under symmetrized Kullback-Leibler loss; averages linear-inverse and quadratic-inverse shrinkage (ledoit2022quadratic). |
| Non-linear (NLS2) | Linear-inverse shrinkage derived under Stein’s loss (ledoit2022quadratic). |
| Non-linear (NLS3) | Quadratic-inverse shrinkage derived under Frobenius loss, inverse Stein’s loss, and minimum variance loss (ledoit2022quadratic). |
| Random Matrix Theory | |
| Constant Residual Eigenvalue (CRE) | Applies the Marchenko-Pastur theorem to identify noise-associated eigenvalues, replacing them with their mean to preserve the trace (de2020machine). |
| Shrinkage of Residual Eigenvalues (SRE) | Similar to CRE, but shrinks noise eigenvalues toward a diagonalized form while preserving the trace (de2020machine). |
| Co-Movement | |
| Gerber Statistic (GS) | Inspired by Kendall’s Tau, uses a noise exclusion zone, scaled axes and non-translated origin (ri=0,rj=0r\_{i}=0,r\_{j}=0) (gerber2022gerber). |
| Atomic-IQ (AIQ) | Inspired by the Gerber IQ statistic, a PSD squeezing co-movement statistic with analytic control of eigenvalues and condition number |
|  |  |

Atomic–IQ parameterization and PSD control.
Atomic–IQ uses spatial and temporal controls that (i) align marginal distributions, (ii) identify body/tail/wing channels via thresholds, and (iii) assign information-weighted squeezing. Table [2](https://arxiv.org/html/2512.23021v1#S6.T2 "Table 2 ‣ A Empirical Design ‣ VI Empirical Study: Tangency Portfolio on a Multi-Asset Universe ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control") summarizes the parameters along with the typical ranges used in the in-sample optimization.

PSD is guaranteed either (i) by design when the collective squeeze respects the canonical identity (no eigenvalues cross zero), or (ii) by applying an analytic eigenfloor λk←max⁡{λk,ϕ}\lambda\_{k}\leftarrow\max\{\lambda\_{k},\phi\} to the spectrum of the squeezed matrix, for a small ϕ>0\phi\!>\!0 chosen within the squeezing framework; both routes are optimization-friendly and maintain trace consistency.

Atomic–IQ squeezing weights.
In *free* mode, which is what we use in this study, Atomic–IQ parameterizes the three channel weights via independent logits 𝐳=(zB,zW,zT)\mathbf{z}=(z\_{B},z\_{W},z\_{T}) mapped through the sigmoid, ηk=σ​(zk)\eta\_{k}=\sigma(z\_{k}) for k∈{B,W,T}k\in\{B,W,T\}, with σ​(x)=1/(1+e−x)\sigma(x)=1/(1+e^{-x}). The zero-correlation benchmark weight is then determined residually as

|  |  |  |
| --- | --- | --- |
|  | 1−ξ= 1−(ηB+ηW+ηT).1-\xi\;=\;1-(\eta\_{B}+\eta\_{W}+\eta\_{T}). |  |

In our calibrated solutions (see Table [3](https://arxiv.org/html/2512.23021v1#S6.T3 "Table 3 ‣ A Empirical Design ‣ VI Empirical Study: Tangency Portfolio on a Multi-Asset Universe ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) ξ>1\xi>1, placing the estimator in the conditional regime; the framework and analytic PSD controls are designed to accommodate this while maintaining PSD status of the overall covariance estimator S^\hat{S}.

Optuna budget and implications of the calibrated parameters.
The Atomic–IQ Optuna hyperparameter search is run for 5,000 trials (candidate parameter configurations). This is a deliberately modest search budget, chosen as a compromise between computational cost and accessibility, so that the calibration protocol can be replicated on limited hardware. At the same time, 5,000 trials remains a relatively limited exploration for multi-parameter estimators, particularly Atomic–IQ, where interactions across spatial and temporal controls can create a high-dimensional search landscape.

Inspecting the calibrated solutions, both Atomic–IQ1 and Atomic–IQ2 select ϵ≈19\epsilon\approx 19 (to the nearest integer), which corresponds to the upper bound τ−1=19\tau-1=19 under a τ=20\tau=20 month lookback. Since ϵ\epsilon governs temporal discounting, this indicates that, in this study, the optimal degree of temporal decay is effectively zero, with past co-movement contributions retained at full temporal weight. Consequently, the reported values of γ\gamma should be interpreted as artifacts of the constrained finite search rather than as evidence of a meaningful optimal temporal-discounting mechanism in the present setting. This temporal conclusion is independent of the spatial allocation, which is controlled by the channel weights.

Finally, the calibrated channel weights imply distinct spatial emphasis across the two variants. For Atomic–IQ1 the ordering is ηT>ηB>ηW\eta\_{T}>\eta\_{B}>\eta\_{W}, indicating strongest emphasis on tail co-movements, followed by body, with the wing channel receiving the smallest of the three channel weights. For Atomic–IQ2 the ordering is ηB≈ηT≫ηW\eta\_{B}\approx\eta\_{T}\gg\eta\_{W}, indicating an almost symmetric allocation between body and tail with a negligible wing component.

Parameterization of tunable benchmarks.
Among the alternative estimators, only the Gerber Statistic (GS) and the random-matrix shrinkage estimator (SRE) are directly tunable in our study. For GS, the tunable hyperparameter is the threshold θ\theta that defines the co-movement event regions. We report results for θ∈{0.5, 0.7, 0.9}\theta\in\{0.5,\,0.7,\,0.9\} to match the settings used in the original Gerber study, and we additionally consider an optimized setting θ∗=0.439\theta^{\ast}=0.439 obtained via the same Optuna in-sample optimization protocol used for Atomic–IQ. We denote this optimized variant as GS∗.

For SRE, the tunable hyperparameter is the shrinkage-mix weight α\alpha, which controls the weight assigned to the sample covariance matrix in the shrinkage combination. We report SRE with α=0.1\alpha=0.1, which is commonly used in related work, and an optimized variant SRE∗ where α∗\alpha^{\ast} is selected using the same Optuna protocol.

Strictly, both SRE and CRE also require a kernel density estimation bandwidth; throughout we fix this bandwidth at h=0.01h=0.01 for both methods, following common practice, and we do not tune hh. All Optuna-based hyperparameter selections are conducted using the in-sample calibration period (1988–1999) only.

|  |  |  |
| --- | --- | --- |
| Parameter | Interpretation | Typical Values |
| Spatial Parameters | | |
| r0r\_{0} (center) | Establishes a co-movement center for the delineation of concordant and discordant co-movement, a critical component of statistical distributional alignment. | r0∈{r¯,r~,0}r\_{0}\in\{\bar{r},\tilde{r},0\}† |
| cc (exclusion) | Reduces noise by filtering out observations with low co-movement informational value. Given in units of the scaling parameter σrk\sigma\_{r\_{k}}. | fixed at 0.5 in this study |
| δ\delta (boundary) | Establishes squeezing channel boundaries that separate moderate from extreme returns in scaled return space, enabling empirical tail detection. Given in units of the scaling parameter σrk\sigma\_{r\_{k}}. | 1 - 3 |
| σrk\sigma\_{r\_{k}}(scaling) | Implements volatility scaling used to map returns into scaled return space when applying cc and δ\delta. The choice affects interpretation of squeezing channels. | f​(σ^ri,σ^rj)∈f(\hat{\sigma}\_{r\_{i}},\hat{\sigma}\_{r\_{j}})\in  {(σ^ri,σ^rj),max(σ^ri,σ^rj),\Big\{(\hat{\sigma}\_{r\_{i}},\hat{\sigma}\_{r\_{j}}),\;\max(\hat{\sigma}\_{r\_{i}},\hat{\sigma}\_{r\_{j}}),\;\Big.  min(σ^ri,σ^rj),mean(σ^ri,σ^rj)}\Big.\min(\hat{\sigma}\_{r\_{i}},\hat{\sigma}\_{r\_{j}}),\;\operatorname{mean}(\hat{\sigma}\_{r\_{i}},\hat{\sigma}\_{r\_{j}})\Big\} |
| η\eta (squeeze) | Controls the squeezing intensity assigned to observations within defined channels. Noisier data are allocated lower values (closer to 0), indicating stronger squeezing, while more informative data receive values closer to 1, preserving their influence. | 0 – 1 |
| Temporal Parameters | | |
| τ\tau (duration) | Lookback window length for co-movement estimation. Balances responsiveness with statistical and computational stability. | fixed at 20 months to give q=τ/N=2q=\tau/N=2 |
| ε\varepsilon (delay) | Implements a flat-weighting window to allow data to retain full influence prior to the onset of temporal decay. | ε∈[0,τ−1]\varepsilon\in[0,\tau-1] |
| γ\gamma (decay) | Controls temporal weighting; |γ||\gamma| sets the discount strength and the sign of γ\gamma determines whether emphasis is placed toward the start or the end of the lookback window. The discount rate is parameterized via the half-life T1/2=ln⁡(2)/|γ|T\_{1/2}=\ln(2)/|\gamma|, with T1/2=∞T\_{1/2}=\infty corresponding to γ=0\gamma=0. | T1/2∈[6.93,∞)≡|γ|∈[0,0.1]T\_{1/2}\in[6.93,\infty)\;\equiv\;|\gamma|\in[0,0.1] |

Table 2: Parameter guidance: grouped by function with interpretation and typical values. †{r¯,r~,0}\{\bar{r},\tilde{r},0\} denotes, respectively, the sample mean return, the sample median return, and zero return.



| Parameter | Atomic–IQ1 | Atomic–IQ2 |
| --- | --- | --- |
| r0r\_{0} | 0 | 0 |
| σrk\sigma\_{r\_{k}} | max⁡(σ^ri,σ^rj)\max\!\left(\hat{\sigma}\_{r\_{i}},\,\hat{\sigma}\_{r\_{j}}\right) | max⁡(σ^ri,σ^rj)\max\!\left(\hat{\sigma}\_{r\_{i}},\,\hat{\sigma}\_{r\_{j}}\right) |
| δ\delta | 1.50 | 1.52 |
| ηB\eta\_{B} | 0.956 | 0.976 |
| ηW\eta\_{W} | 0.870 | 0.0190 |
| ηT\eta\_{T} | 0.979 | 0.976 |
| γ†\gamma^{\dagger} | 0.0541 | 0.0765 |
| ϵ\epsilon | 19.0 | 18.9 |

Table 3: In-sample calibrated Atomic–IQ settings used in the out-of-sample backtests. † Note that ε\varepsilon (delayed decay) takes close to its maximum permissible value, rendering the reported values of γ\gamma artefacts; in effect there is no temporal discounting.

Evaluation metrics.
We report the annualized Sharpe ratio, the Sortino ratio, the Calmar ratio, the annualized return, the cumulative return, the annualized volatility (σ\sigma), the maximum drawdown, the 95% monthly value-at-risk, and the average monthly turnover. The out-of-sample window for all tables is 2000–2024.

We also report statistical significance tests for out-of-sample performance differences, with particular emphasis on pairwise tests of out-of-sample Sharpe ratio differences between atomic–IQ and each competing estimator.

### B Empirical Results

Table 4 reports out-of-sample performance for all covariance estimators under the common long-only tangency protocol described in Section VI.A (monthly rebalancing, τ=20\tau=20 months for both 𝝁^\hat{\boldsymbol{\mu}} and 𝚺^\hat{\boldsymbol{\Sigma}}, and 10 bp transaction costs applied to dollar turnover). Results are ordered by decreasing after-cost Sharpe ratio.

Several patterns are immediate. First, the atomic–IQ variants sit at the top of the Sharpe distribution: AIQ1 delivers the highest out-of-sample Sharpe ratio (0.56), with AIQ2 close behind (0.54). This risk-adjusted performance is achieved with comparatively low volatility (7.70% for AIQ1 and 7.65% for AIQ2), and with moderate drawdowns (approximately −28%-28\%) relative to the higher-volatility shrinkage alternatives. In contrast, the best-performing linear shrinkage variant by Sharpe, LS1 (0.54), attains materially higher annualized return, but it does so with substantially higher volatility (11.40%), deeper drawdowns (−36.53%-36.53\%), and a more adverse 95% VaR (Table 4).

Second, methods that emphasize raw return, such as LS2, rank highly on annualized and cumulative return but are penalized by markedly higher risk. LS2 achieves the highest annualized and cumulative returns in the table, yet it exhibits the highest volatility and one of the worst drawdowns and VaR outcomes, which depresses its Sharpe ratio and makes its risk profile less attractive for a tangency objective.

Third, the concordance-based Gerber family is competitive but does not dominate: GS1 and the Optuna-tuned GS∗ deliver similar Sharpe ratios (both 0.51), with broadly comparable tail-risk statistics, while GS3 is slightly weaker (0.50) and GS2 is clearly the weakest among the Gerber variants (0.44). This ordering is consistent with the view that concordance-based construction is effective in this setting, but that atomic squeezing can improve risk-adjusted performance while also providing PSD guarantees and explicit spectral control.

Finally, the random-matrix cleaners (CRE and SRE) do not improve Sharpe in this particular N=10N=10 universe. SRE and SRE∗ cluster around the historical covariance baseline (HC), and CRE is slightly lower. Overall, the table suggests that AIQ1 achieves its Sharpe premium primarily through a more favorable risk profile (lower volatility and milder tail risk) rather than through unusually high raw returns, and it does so without incurring unusually high turnover relative to competing approaches.

### C Overall Rankings Across Estimators

To summarize performance beyond Sharpe alone, Table 5 reports per-metric ranks for every estimator across the full set of reported outcomes (Sharpe, Sortino, Calmar, annualized return, cumulative return, volatility, maximum drawdown, 95% VaR, and turnover). The aggregate score is the sum of these ranks (lower is better), providing a compact measure of broad risk–return quality under the common backtest protocol.

The aggregate rankings reinforce the central message of Table 4. AIQ1 attains the best overall score (34), reflecting a combination of first-ranked Sharpe performance and consistently strong risk metrics, particularly volatility and tail-risk measures, without sacrificing turnover. AIQ2 ranks second overall (52), driven by similarly low volatility and strong Sharpe and turnover ranks, though with weaker return ranks than some shrinkage competitors. The next cluster comprises the Gerber variants GS1 and GS∗ (aggregate scores in the low-to-mid 60s), which benefit from strong drawdown and Calmar ranks, but do not match atomic–IQ on Sharpe and volatility simultaneously.

Several trade-offs become clearer in the rank table. LS1 ranks near the top on Sharpe and performs strongly on return, but its high volatility and adverse tail metrics push it down in aggregate rank. LS2 illustrates an even starker version of this pattern: it is first-ranked on annualized and cumulative return, yet it ranks last (or near-last) on volatility, drawdown, and VaR, yielding a poor aggregate score despite headline return strength. Conversely, the sample covariance (HC) and the RMT cleaners (SRE, SRE∗, CRE) occupy the middle-to-lower portion of the aggregate ordering, indicating that in this low-dimensional setting their improvements in stability do not translate into superior out-of-sample tangency performance once costs and tail risk are accounted for.

Taken together, Tables 4–5 indicate that atomic–IQ, and AIQ1 in particular, offers a favorable combination of high risk-adjusted performance and broad risk control, rather than a narrow improvement in a single metric. This is consistent with the intended role of the squeezing framework, namely to produce covariance estimates that are optimization-ready and spectrally controlled while still improving realized portfolio behavior.

| Estimator | SR | AR | CR | σ\sigma | MDD | VaR95 | So | Cal | Turn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AIQ1 | 0.560.56 | 5.915.91 | 267.93267.93 | 7.707.70 | −28.06-28.06 | −3.16-3.16 | 0.680.68 | 0.210.21 | 2.812.81 |
| AIQ2 | 0.540.54 | 5.695.69 | 249.98249.98 | 7.657.65 | −28.29-28.29 | −3.28-3.28 | 0.650.65 | 0.200.20 | 2.762.76 |
| LS1 | 0.540.54 | 7.717.71 | 412.45412.45 | 11.4011.40 | −36.53-36.53 | −4.71-4.71 | 0.650.65 | 0.210.21 | 3.323.32 |
| LS2 | 0.520.52 | 8.518.51 | 484.81484.81 | 13.2213.22 | −41.75-41.75 | −5.90-5.90 | 0.640.64 | 0.200.20 | 3.963.96 |
| NLS6 | 0.520.52 | 6.536.53 | 308.82308.82 | 9.609.60 | −30.22-30.22 | −4.04-4.04 | 0.620.62 | 0.220.22 | 3.693.69 |
| NLS8 | 0.520.52 | 6.586.58 | 312.49312.49 | 9.669.66 | −30.21-30.21 | −4.04-4.04 | 0.620.62 | 0.220.22 | 3.703.70 |
| GS1 | 0.510.51 | 5.915.91 | 262.04262.04 | 8.528.52 | −27.22-27.22 | −3.35-3.35 | 0.600.60 | 0.220.22 | 3.473.47 |
| GS\* | 0.510.51 | 5.925.92 | 262.77262.77 | 8.568.56 | −27.22-27.22 | −3.35-3.35 | 0.600.60 | 0.220.22 | 3.473.47 |
| NLS7 | 0.510.51 | 6.486.48 | 304.65304.65 | 9.559.55 | −30.25-30.25 | −4.03-4.03 | 0.620.62 | 0.210.21 | 3.693.69 |
| GS3 | 0.500.50 | 5.595.59 | 239.90239.90 | 8.018.01 | −29.36-29.36 | −3.51-3.51 | 0.600.60 | 0.190.19 | 3.313.31 |
| HC | 0.490.49 | 5.945.94 | 261.90261.90 | 8.898.89 | −30.50-30.50 | −3.39-3.39 | 0.590.59 | 0.190.19 | 3.453.45 |
| LS3 | 0.490.49 | 6.146.14 | 275.83275.83 | 9.339.33 | −32.13-32.13 | −3.73-3.73 | 0.590.59 | 0.190.19 | 3.413.41 |
| SRE\* | 0.490.49 | 5.945.94 | 261.86261.86 | 8.898.89 | −30.50-30.50 | −3.39-3.39 | 0.590.59 | 0.190.19 | 3.453.45 |
| LS5 | 0.480.48 | 5.785.78 | 250.25250.25 | 8.658.65 | −31.45-31.45 | −3.06-3.06 | 0.580.58 | 0.180.18 | 3.343.34 |
| SRE | 0.480.48 | 5.825.82 | 252.96252.96 | 8.748.74 | −30.55-30.55 | −3.26-3.26 | 0.580.58 | 0.190.19 | 3.463.46 |
| CRE | 0.470.47 | 5.745.74 | 245.91245.91 | 8.848.84 | −32.10-32.10 | −3.07-3.07 | 0.560.56 | 0.180.18 | 3.453.45 |
| LS4 | 0.470.47 | 5.535.53 | 232.19232.19 | 8.508.50 | −30.01-30.01 | −3.32-3.32 | 0.560.56 | 0.180.18 | 3.233.23 |
| GS2 | 0.440.44 | 5.305.30 | 215.24215.24 | 8.378.37 | −29.32-29.32 | −3.65-3.65 | 0.520.52 | 0.180.18 | 3.443.44 |

Table 4: Out of sample performance across all estimators and metrics, ordered on decreasing Sharpe ratio; monthly rebalancing; 10 bp costs.



| Estimator | SR | AR | CR | σ\sigma | MDD | VaR95 | So | Cal | Turn | Agg |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AIQ1 | 11 | 1010 | 77 | 22 | 33 | 33 | 11 | 55 | 22 | 3434 |
| AIQ2 | 22 | 1515 | 1414 | 11 | 44 | 55 | 22 | 88 | 11 | 5252 |
| GS1 | 77 | 1010 | 99 | 66 | 11 | 77 | 99 | 11 | 1313 | 6363 |
| GS\* | 77 | 99 | 88 | 77 | 11 | 1010 | 88 | 11 | 1414 | 6565 |
| LS1 | 22 | 22 | 22 | 1717 | 1717 | 1717 | 22 | 55 | 55 | 6969 |
| NLS6 | 44 | 44 | 44 | 1515 | 1010 | 1515 | 55 | 11 | 1515 | 7272 |
| NLS8 | 44 | 33 | 33 | 1616 | 99 | 1515 | 55 | 11 | 1717 | 7272 |
| NLS7 | 77 | 55 | 55 | 1414 | 1111 | 1414 | 55 | 55 | 1515 | 8080 |
| GS3 | 1010 | 1616 | 1616 | 33 | 66 | 1111 | 99 | 1010 | 44 | 8484 |
| HC | 1111 | 77 | 1010 | 1111 | 1212 | 99 | 1111 | 1010 | 99 | 8888 |
| SRE\* | 1111 | 77 | 1111 | 1010 | 1212 | 99 | 1111 | 1010 | 99 | 8989 |
| LS2 | 44 | 11 | 11 | 1818 | 1818 | 1818 | 44 | 88 | 1818 | 9090 |
| LS3 | 1111 | 66 | 66 | 1313 | 1616 | 1313 | 1111 | 1010 | 77 | 9393 |
| LS5 | 1414 | 1313 | 1313 | 88 | 1414 | 11 | 1414 | 1515 | 66 | 9898 |
| SRE | 1414 | 1212 | 1212 | 99 | 1515 | 44 | 1414 | 1010 | 1212 | 100100 |
| LS4 | 1616 | 1717 | 1717 | 55 | 88 | 66 | 1616 | 1515 | 33 | 102102 |
| CRE | 1616 | 1414 | 1515 | 1212 | 1717 | 22 | 1616 | 1515 | 99 | 112112 |
| GS2 | 1818 | 1818 | 1818 | 44 | 55 | 1212 | 1818 | 1515 | 88 | 116116 |

Table 5: Aggregate ranking of out of sample performance across all estimators and metrics (lower is better.)

### D Sharpe Ratio Comparison and Statistical Inference

Table 4 reports the out-of-sample performance of all competing covariance estimators under the common long-only tangency protocol, and Table 5 aggregates ranks across the full set of reported metrics. AIQ1 attains the highest after-cost Sharpe ratio (0.56) among all methods (Table 4), but the key feature is that this Sharpe is delivered with a distinctly favourable overall risk profile. Relative to the main conventional competitors that are closest on Sharpe, such as LS1 (0.54), AIQ1 operates at materially lower volatility (7.70% versus 11.40%), with milder drawdowns and tighter tail-risk, while also exhibiting lower turnover (Table 4). This broad stability is reflected in the aggregate ranking, where AIQ1 achieves the best overall score (34), followed by AIQ2 (52), with the remaining estimators spanning larger totals (Table 5). In this sense, AIQ1 does not appear to obtain a Sharpe premium by accepting hidden risk elsewhere in the distribution.

Because differences in Sharpe ratios across the top of the table are modest, we also ask whether any alternative estimator can be shown to deliver a Sharpe ratio that is statistically higher than AIQ1’s. Treating AIQ1 as the benchmark, we test one-sided hypotheses of the form H0:S​R​(k)≥S​R​(AIQ1)H\_{0}:\,SR(k)\geq SR(\mathrm{AIQ1}) versus H1:S​R​(k)<S​R​(AIQ1)H\_{1}:\,SR(k)<SR(\mathrm{AIQ1}) for each competitor kk (Appendix C). In full-sample terms, using a moving-block bootstrap over monthly excess returns, the evidence supports rejection of H0H\_{0} for the weaker methods, with GS2 and LS4 in particular exhibiting Sharpe ratios that are significantly lower than AIQ1 at conventional levels. For the remaining estimators, the bootstrap confidence intervals for the full-sample Sharpe difference include zero, so there is no statistical evidence that any method improves on AIQ1’s Sharpe once estimation error and time dependence are accounted for.

To assess stability of relative Sharpe performance through time, we compute 36-month rolling Sharpe ratios and form the difference series

|  |  |  |
| --- | --- | --- |
|  | Dt(k)=S​Rt​(AIQ1)−S​Rt​(k),D^{(k)}\_{t}=SR\_{t}(\mathrm{AIQ1})-SR\_{t}(k), |  |

for each competitor kk, evaluated both on the monthly grid and on a thinned grid with a step of three months to reduce overlap across windows (Appendix C). On the monthly grid, the average rolling Sharpe difference is positive against every competing estimator, with typical mean differentials in the range 0.04 to 0.16 in annualised units. Accounting for strong serial dependence induced by overlapping windows, Newey–West HAC inference and a moving-block bootstrap for the mean difference again identify GS2 and LS4 as robustly inferior to AIQ1 across both grids. For several of the stronger competitors, including LS1 and the nonlinear shrinkage estimators, the HAC p-values on the monthly grid are small, suggesting that AIQ1’s rolling Sharpe advantage may be economically meaningful even when statistical separation is not uniformly sharp under bootstrap uncertainty. Overall, the inference results support the practical conclusion suggested by Tables 4–5: several estimators are Sharpe-comparable to AIQ1, none can be shown to outperform it on Sharpe, and the weakest alternatives are clearly dominated.

## VII Conclusion

This paper develops squeezed covariance estimation, a constructive framework that advances Informational Quality by resolving two core obstacles that routinely limit the practical use of concordance-based covariance estimators. First, it provides PSD guarantees by construction. Channel-class matrices are assembled from positive semi-definite atoms and normalized at the class level, so the estimator remains PSD whenever the collective squeeze lies in the feasible region. For the conditional regime, we derive an exact feasibility condition and illustrate it under the basic–IQ parameterization, making the PSD boundary explicit rather than relying on ex-post projection. Second, the framework delivers analytic eigenvalue control. We introduce an eigenfloor mechanism that enforces a positive spectral margin and supplies closed-form rules for targeting either a minimum-eigenvalue floor or a desired condition number. Importantly, the same mechanism functions as an analytic PSD repair in the conditional regime while remaining expressible within the canonical squeezing identity. The resulting estimator is interpretable, spectrally disciplined, and immediately optimization-ready, offering a principled alternative to ad hoc PSD fixes and placing concordance-based methods on equal footing with sample-anchored regularization.

Empirically, under a common long-only tangency backtest with transaction costs, atomic–IQ delivers the strongest risk-adjusted performance when compared against the full set of estimators in the study. The main economic message is not merely a higher Sharpe ratio, but a consistently improved risk profile: atomic–IQ achieves its Sharpe advantage with lower realized volatility and tighter tail-risk characteristics, rather than by accepting hidden fragility elsewhere in the return distribution. This is precisely the type of improvement that matters for implementable portfolio choice, where stability and robustness are as important as headline performance.

Finally, the squeezing construction is dimension-agnostic and naturally accommodates changes in the portfolio dimension NN and the sampling ratio Q=T/NQ=T/N. This makes the framework relevant across both data-rich and data-poor regimes, including settings where classical sample-based covariance estimation becomes unstable and where PSD feasibility and spectral control are most consequential.

## Appendix Appendix A Spectral mapping and feasibility

### A Correlation–PSD of class matrices C(α)C^{(\alpha)}

#### Proof sketch.

Each event atom A±A^{\pm} is positive semi-definite by construction: it is a rank-one
outer product with eigenvalues {0,2}\{0,2\}. For a given class α\alpha, the accumulator

|  |  |  |
| --- | --- | --- |
|  | Gα=∑(i,j),e∈αwe​A±​(e),we>0,G\_{\alpha}=\sum\_{(i,j),\,e\in\alpha}w\_{e}A^{\pm}(e),\qquad w\_{e}>0, |  |

is therefore a non-negative sum of PSD matrices and hence PSD itself.

To obtain C(α)C^{(\alpha)}, we apply a congruence transform with the diagonal scaling
matrix Dα=diag​(Gα)D\_{\alpha}=\mathrm{diag}(G\_{\alpha}):

|  |  |  |
| --- | --- | --- |
|  | C(α)=Dα−12​Gα​Dα−12.C^{(\alpha)}=D\_{\alpha}^{-\tfrac{1}{2}}G\_{\alpha}D\_{\alpha}^{-\tfrac{1}{2}}. |  |

Congruence transformations preserve positive semi-definiteness, so C(α)C^{(\alpha)} is PSD.
By construction C(α)C^{(\alpha)} is also symmetric with unit diagonal. Moreover, since Gα⪰0G\_{\alpha}\succeq 0,
its entries satisfy the standard PSD (Cauchy–Schwarz / principal-minor) bound
|(Gα)i​j|≤(Gα)i​i​(Gα)j​j|(G\_{\alpha})\_{ij}|\leq\sqrt{(G\_{\alpha})\_{ii}(G\_{\alpha})\_{jj}}. It follows that the off-diagonal
entries of C(α)C^{(\alpha)} are bounded in [−1,1][-1,1]. Thus each C(α)C^{(\alpha)} is correlation–PSD.

Finally, since the identity matrix II is PSD and convex combinations of PSD matrices are PSD,
the overall estimator SS in ([15](https://arxiv.org/html/2512.23021v1#S4.E15 "Equation 15 ‣ IV Spectral Regimes ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) is PSD whenever the collective squeeze does not exceed one.

### B Exact PSD condition

#### Spectral mapping under the neutral benchmark II.

Using the compact form in ([15](https://arxiv.org/html/2512.23021v1#S4.E15 "Equation 15 ‣ IV Spectral Regimes ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")), we may write,

|  |  |  |
| --- | --- | --- |
|  | S=(1−ξ)​I+ξ​P=I+ξ​(P−I),S=(1-\xi)I+\xi P\;=\;I+\xi(P-I), |  |

where ξ=∑α∈𝒦ηα\xi=\sum\_{\alpha\in\mathcal{K}}\eta\_{\alpha} is the collective squeeze and PP is the
corresponding normalized blend of class matrices.
Diagonalize P=U​Λ​U⊤P=U\Lambda U^{\top}. Then

|  |  |  |
| --- | --- | --- |
|  | S=(1−ξ)​I+ξ​U​Λ​U⊤=U​((1−ξ)​I+ξ​Λ)​U⊤,S\;=\;(1-\xi)I+\xi U\Lambda U^{\top}\;=\;U\bigl((1-\xi)I+\xi\Lambda\bigr)U^{\top}, |  |

so SS and PP share eigenvectors, with eigenvalues related by the affine map

|  |  |  |
| --- | --- | --- |
|  | λi​(S)=(1−ξ)⋅1+ξ​λi​(P)= 1+ξ​(λi​(P)−1).\lambda\_{i}(S)\;=\;(1-\xi)\cdot 1+\xi\,\lambda\_{i}(P)\;=\;1+\xi\bigl(\lambda\_{i}(P)-1\bigr). |  |

In particular,

|  |  |  |
| --- | --- | --- |
|  | S⪰0⇔λmin​(S)≥0⇔(1−ξ)+ξ​λmin​(P)≥0.S\succeq 0\iff\lambda\_{\min}(S)\geq 0\iff(1-\xi)+\xi\,\lambda\_{\min}(P)\geq 0. |  |

Equivalently, for ξ>1\xi>1 (extrapolation), feasibility is

|  |  |  |
| --- | --- | --- |
|  | λmin​(P)≥ 1−1ξ,\lambda\_{\min}(P)\ \geq\ 1-\tfrac{1}{\xi}, |  |

while for ξ≤1\xi\leq 1 (interpolation), PSD holds whenever the class matrices are PSD, since SS is then a
convex combination of PSD matrices. This is the interpolation/extrapolation interpretation used in the main text.

### C Basic IQ feasibility

#### Basic IQ weights ({η2,η,1}\{\eta^{2},\eta,1\}, η∈[0,1]\eta\in[0,1]).

Let ξ​(η)=1+η+η2\xi(\eta)=1+\eta+\eta^{2} and define

|  |  |  |
| --- | --- | --- |
|  | P​(η)=C(T)+η​C(B)+η2​C(W)1+η+η2.P(\eta)=\frac{C^{(T)}+\eta\,C^{(B)}+\eta^{2}\,C^{(W)}}{1+\eta+\eta^{2}}. |  |

Then ξ​(η)∈[1,3]\xi(\eta)\in[1,3], and for any η>0\eta>0 we are in extrapolation (ξ​(η)>1)\bigl(\xi(\eta)>1\bigr).
Applying the exact PSD condition above with ξ=ξ​(η)\xi=\xi(\eta) yields the feasibility threshold

|  |  |  |
| --- | --- | --- |
|  | S​(η)⪰0⇔(1−ξ​(η))+ξ​(η)​λmin​(P​(η))≥0⇔λmin​(P​(η))≥ 1−1ξ​(η)=η+η21+η+η2.S(\eta)\succeq 0\iff(1-\xi(\eta))+\xi(\eta)\,\lambda\_{\min}\!\bigl(P(\eta)\bigr)\geq 0\iff\lambda\_{\min}\!\bigl(P(\eta)\bigr)\ \geq\ 1-\tfrac{1}{\xi(\eta)}\ =\ \frac{\eta+\eta^{2}}{1+\eta+\eta^{2}}. |  |

#### Bounds in terms of class minima.

Write mk=λmin​(C(k))m\_{k}=\lambda\_{\min}\!\bigl(C^{(k)}\bigr) for k∈{T,B,W}k\in\{T,B,W\}.
Since λmin\lambda\_{\min} is concave on the PSD cone, for nonnegative weights summing to one,

|  |  |  |
| --- | --- | --- |
|  | λmin​(P​(η))≥mT+η​mB+η2​mW1+η+η2.\lambda\_{\min}\!\bigl(P(\eta)\bigr)\;\geq\;\frac{m\_{T}+\eta m\_{B}+\eta^{2}m\_{W}}{1+\eta+\eta^{2}}. |  |

A sufficient condition for feasibility is therefore

|  |  |  |
| --- | --- | --- |
|  | mT+η​mB+η2​mW1+η+η2≥η+η21+η+η2,\frac{m\_{T}+\eta m\_{B}+\eta^{2}m\_{W}}{1+\eta+\eta^{2}}\ \geq\ \frac{\eta+\eta^{2}}{1+\eta+\eta^{2}}, |  |

which rearranges to

|  |  |  |
| --- | --- | --- |
|  | η2​(1−mW)+η​(1−mB)≤mT.\eta^{2}(1-m\_{W})+\eta(1-m\_{B})\ \leq\ m\_{T}. |  |

For a necessary (coarse) bound, note that λmin​(P​(η))≤mmax\lambda\_{\min}\!\bigl(P(\eta)\bigr)\leq m\_{\max},
where mmax:=max⁡{mT,mB,mW}m\_{\max}:=\max\{m\_{T},m\_{B},m\_{W}\}. If S​(η)S(\eta) is PSD, then in particular
λmin​(P​(η))≥(η+η2)/(1+η+η2)\lambda\_{\min}\!\bigl(P(\eta)\bigr)\geq(\eta+\eta^{2})/(1+\eta+\eta^{2}), hence necessarily

|  |  |  |
| --- | --- | --- |
|  | η+η21+η+η2≤mmax⟹η2+η≤mmax1−mmax.\frac{\eta+\eta^{2}}{1+\eta+\eta^{2}}\ \leq\ m\_{\max}\quad\Longrightarrow\quad\eta^{2}+\eta\ \leq\ \frac{m\_{\max}}{1-m\_{\max}}. |  |

These bounds are the sufficient and necessary inequalities reported in the main text.

### D Choosing ϕ\phi for λmin\lambda\_{\min} and κ\kappa

For S^​(ϕ)=(1−ϕ)​S+ϕ​I\widehat{S}(\phi)=(1-\phi)S+\phi I, the extremal eigenvalues are affine in ϕ\phi. If α=λmax​(S)\alpha=\lambda\_{\max}(S)
and β=λmin​(S)\beta=\lambda\_{\min}(S), then

|  |  |  |
| --- | --- | --- |
|  | λmax​(S^​(ϕ))=(1−ϕ)​α+ϕ,λmin​(S^​(ϕ))=(1−ϕ)​β+ϕ.\lambda\_{\max}(\widehat{S}(\phi))=(1-\phi)\alpha+\phi,\qquad\lambda\_{\min}(\widehat{S}(\phi))=(1-\phi)\beta+\phi. |  |

Solving (1−ϕ)​β+ϕ≥λ¯(1-\phi)\beta+\phi\geq\underline{\lambda} yields the expression in ([20](https://arxiv.org/html/2512.23021v1#S5.E20 "Equation 20 ‣ Target minimum eigenvalue. ‣ B Targeted Conditioning and PSD Repair ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")); solving

|  |  |  |
| --- | --- | --- |
|  | (1−ϕ)​α+ϕ(1−ϕ)​β+ϕ≤K\frac{(1-\phi)\alpha+\phi}{(1-\phi)\beta+\phi}\leq K |  |

yields the expression in ([21](https://arxiv.org/html/2512.23021v1#S5.E21 "Equation 21 ‣ Target condition number. ‣ B Targeted Conditioning and PSD Repair ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")).

## Appendix Appendix B Compact illustration

This section provides a small worked example to visualize the regimes and the role of the eigenfloor. The aim is not to benchmark but to make the mechanics concrete.

#### Setup.

Take three assets (n=3)(n=3) and three channel classes B,W,TB,W,T.
In the full procedure the class matrices C(B),C(W),C(T)C^{(B)},C^{(W)},C^{(T)} are constructed from data by aggregating co-movement events through the squeezing template in Figure [1](https://arxiv.org/html/2512.23021v1#S2.F1 "Figure 1 ‣ II The Gerber Informational Quality Framework ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control") and then normalizing once per class.
For this compact illustration we use the following correlation–PSD matrices, chosen to be numerically plausible and to make the regimes and the role of the eigenfloor transparent:

|  |  |  |
| --- | --- | --- |
|  | C(B)=[10.300.200.3010.250.200.251],C(W)=[1−0.50−0.20−0.501−0.30−0.20−0.301],C(T)=[100.800100.8001].C^{(B)}=\begin{bmatrix}1&0.30&0.20\\ 0.30&1&0.25\\ 0.20&0.25&1\end{bmatrix},\quad C^{(W)}=\begin{bmatrix}1&-0.50&-0.20\\ -0.50&1&-0.30\\ -0.20&-0.30&1\end{bmatrix},\quad C^{(T)}=\begin{bmatrix}1&0&0.80\\ 0&1&0\\ 0.80&0&1\end{bmatrix}. |  |

In basic–IQ the class weights are {1,η,η2}\{1,\eta,\eta^{2}\} on {T,B,W}\{T,B,W\} with η∈[0,1]\eta\in[0,1].
Hence the collective squeeze is ξ​(η)=1+η+η2\xi(\eta)=1+\eta+\eta^{2} and the blend is

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(η)=C(T)+η​C(B)+η2​C(W) 1+η+η2,S​(η)=(1−ξ​(η))​I+ξ​(η)​P​(η).P(\eta)\;=\;\frac{C^{(T)}+\eta\,C^{(B)}+\eta^{2}C^{(W)}}{\,1+\eta+\eta^{2}\,},\qquad S(\eta)\;=\;(1-\xi(\eta))I+\xi(\eta)P(\eta). |  | (24) |

#### Guaranteed vs. conditional regimes.

Using the exact PSD condition from Appendix [Appendix A](https://arxiv.org/html/2512.23021v1#A1 "Appendix Appendix A Spectral mapping and feasibility ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control"), S​(η)⪰0S(\eta)\succeq 0 if and only if
(1−ξ​(η))+ξ​(η)​λmin​(P​(η))≥0(1-\xi(\eta))+\xi(\eta)\,\lambda\_{\min}\!\big(P(\eta)\big)\geq 0, that is,
λmin​(P​(η))≥1−1ξ​(η)=η+η21+η+η2\lambda\_{\min}\!\big(P(\eta)\big)\geq 1-\tfrac{1}{\xi(\eta)}=\tfrac{\eta+\eta^{2}}{1+\eta+\eta^{2}} when ξ​(η)>1\xi(\eta)>1.
For η∈(0,1]\eta\in(0,1], ξ​(η)>1\xi(\eta)>1 and we are in extrapolation.
For three representative values (computed from the matrices above):

| η\eta | ξ​(η)\xi(\eta) | λmin​(P​(η))\lambda\_{\min}\!\big(P(\eta)\big) | threshold 1−1ξ​(η)1-\tfrac{1}{\xi(\eta)} | PSD? |
| --- | --- | --- | --- | --- |
| 0.00.0 | 1.001.00 | 0.2000.200 | 0.0000.000 | yes |
| 0.50.5 | 1.751.75 | 0.5140.514 | 0.4290.429 | yes |
| 1.01.0 | 3.003.00 | 0.7290.729 | 0.6670.667 | yes |

For these matrices the blend is sufficiently close to the identity that the conditional regime still yields PSD.

#### Effect on S​(η)S(\eta) and the eigenfloor.

At η=1\eta=1 the spectrum of S​(η)S(\eta) is approximately

|  |  |  |
| --- | --- | --- |
|  | λ​(S​(1))≈{ 1.838, 0.977, 0.186},\lambda\big(S(1)\big)\approx\{\,1.838,\ 0.977,\ 0.186\,\}, |  |

so the matrix is PSD but moderately ill conditioned.
Two common stabilization goals can be met by a small identity reserve using ([16](https://arxiv.org/html/2512.23021v1#S5.E16 "Equation 16 ‣ A The Eigenfloor Mechanism ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control"))–([19](https://arxiv.org/html/2512.23021v1#S5.E19 "Equation 19 ‣ A The Eigenfloor Mechanism ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")):

* •

  *Target condition number.* For K=5K=5, ([21](https://arxiv.org/html/2512.23021v1#S5.E21 "Equation 21 ‣ Target condition number. ‣ B Targeted Conditioning and PSD Repair ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) gives t≈0.185t\approx 0.185, yielding

  |  |  |  |
  | --- | --- | --- |
  |  | λ​(S^​(0.185))≈{ 1.683, 0.981, 0.337}.\lambda\big(\widehat{S}(0.185)\big)\approx\{\,1.683,\ 0.981,\ 0.337\,\}. |  |
* •

  *Target minimum eigenvalue.* For λ¯=0.50\underline{\lambda}=0.50, ([20](https://arxiv.org/html/2512.23021v1#S5.E20 "Equation 20 ‣ Target minimum eigenvalue. ‣ B Targeted Conditioning and PSD Repair ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) gives t≈0.386t\approx 0.386, yielding

  |  |  |  |
  | --- | --- | --- |
  |  | λ​(S^​(0.386))≈{ 1.514, 0.986, 0.500}.\lambda\big(\widehat{S}(0.386)\big)\approx\{\,1.514,\ 0.986,\ 0.500\,\}. |  |

Both choices move the spectrum toward 11 as predicted by ([19](https://arxiv.org/html/2512.23021v1#S5.E19 "Equation 19 ‣ A The Eigenfloor Mechanism ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")), while preserving the squeezing representation via ([17](https://arxiv.org/html/2512.23021v1#S5.E17 "Equation 17 ‣ A The Eigenfloor Mechanism ‣ V Eigenfloor and Conditioning ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")) with rescaled class weights.

#### Remarks.

(i) The example is intentionally small and uses fixed class matrices for clarity. In practice C(α)C^{(\alpha)} are constructed atomically from data and normalized once per class.

(ii) When ξ≤1\xi\leq 1 (atomic–IQ) no floor is required; when ξ>1\xi>1 the eigenfloor provides a closed–form PSD repair and conditioning control while keeping the estimator inside the squeezing family.

(iii) Larger asset panels and temporal weighting variants are reported in the accompanying empirical results (see Sections [VI](https://arxiv.org/html/2512.23021v1#S6 "VI Empirical Study: Tangency Portfolio on a Multi-Asset Universe ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control").[A](https://arxiv.org/html/2512.23021v1#S6.SS1 "A Empirical Design ‣ VI Empirical Study: Tangency Portfolio on a Multi-Asset Universe ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control") & [VI](https://arxiv.org/html/2512.23021v1#S6 "VI Empirical Study: Tangency Portfolio on a Multi-Asset Universe ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control").[B](https://arxiv.org/html/2512.23021v1#S6.SS2 "B Empirical Results ‣ VI Empirical Study: Tangency Portfolio on a Multi-Asset Universe ‣ Squeezed Covariance Matrix Estimation: Analytic Eigenvalue Control")).

## Appendix Appendix C Sharpe ratio tests relative to atomic–IQ

This section describes the inference procedures used to compare the Sharpe ratios of all competing covariance estimators reported in the empirical results (Table 4) to AIQ1. Throughout, AIQ1 is treated as the benchmark. Our primary question is whether any alternative estimator delivers a higher Sharpe ratio than AIQ1. Accordingly, for each competitor kk we formulate one-sided hypotheses of the form

|  |  |  |
| --- | --- | --- |
|  | H0:SR(k)≥SR(AIQ1)vs.H1:SR(k)<SR(AIQ1).H\_{0}:\text{SR}^{(k)}\geq\text{SR}^{(\text{AIQ1})}\quad\text{vs.}\quad H\_{1}:\text{SR}^{(k)}<\text{SR}^{(\text{AIQ1})}. |  |

Rejection of H0H\_{0} is interpreted as evidence that estimator kk has a lower Sharpe ratio than AIQ1; failure to reject means that, based on Sharpe alone, kk is at best comparable to AIQ1.

Because we test multiple competitors, the reported pp-values should be interpreted as pairwise evidence relative to AIQ1. Unless stated otherwise, we do not apply a family-wise multiple-testing correction; the complete set of test statistics and confidence intervals is reported in the online supplement. To align with our study, in what follows assume T≡τ=20T\equiv\tau=20 and L=12L=12.

### Setup and notation

Let rt(k)r\_{t}^{(k)} denote the monthly excess return (net of the risk-free rate and after transaction costs) of the tangency portfolio constructed using estimator kk in month tt, for t=1,…,Tt=1,\dots,T. We work with two Sharpe ratio objects:

1. 1.

   The full-sample annualized Sharpe ratio,

   |  |  |  |
   | --- | --- | --- |
   |  | SR^(k)=12​r¯(k)σ^(k),r¯(k)=1T​∑t=1Trt(k),σ^(k)=(1T−1​∑t=1T(rt(k)−r¯(k))2)1/2.\widehat{\text{SR}}^{(k)}=\sqrt{12}\,\frac{\bar{r}^{(k)}}{\hat{\sigma}^{(k)}},\qquad\bar{r}^{(k)}=\frac{1}{T}\sum\_{t=1}^{T}r\_{t}^{(k)},\quad\hat{\sigma}^{(k)}=\left(\frac{1}{T-1}\sum\_{t=1}^{T}\bigl(r\_{t}^{(k)}-\bar{r}^{(k)}\bigr)^{2}\right)^{1/2}. |  |
2. 2.

   The rolling annualized Sharpe ratio computed over a window of WW months (in the empirical work W=36W=36). For each t≥Wt\geq W we set

   |  |  |  |
   | --- | --- | --- |
   |  | SR^t(k)=12​μ^t(k)σ^t(k),μ^t(k)=1W​∑j=t−W+1trj(k),σ^t(k)=(1W−1​∑j=t−W+1t(rj(k)−μ^t(k))2)1/2.\widehat{\text{SR}}\_{t}^{(k)}=\sqrt{12}\,\frac{\hat{\mu}\_{t}^{(k)}}{\hat{\sigma}\_{t}^{(k)}},\quad\hat{\mu}\_{t}^{(k)}=\frac{1}{W}\sum\_{j=t-W+1}^{t}r\_{j}^{(k)},\quad\hat{\sigma}\_{t}^{(k)}=\left(\frac{1}{W-1}\sum\_{j=t-W+1}^{t}\bigl(r\_{j}^{(k)}-\hat{\mu}\_{t}^{(k)}\bigr)^{2}\right)^{1/2}. |  |

   In addition to the standard monthly grid (t=W,W+1,…,T)(t=W,W+1,\dots,T), we also consider a thinned grid with a step of three months (t=W,W+3,W+6,…)(t=W,W+3,W+6,\dots) as a robustness check that reduces overlap across windows.

For each competitor kk we treat AIQ1 as the benchmark and define the Sharpe differences

|  |  |  |
| --- | --- | --- |
|  | Δ(k)=SR^(AIQ1)−SR^(k)(full sample),Dt(k)=SR^t(AIQ1)−SR^t(k)(rolling).\Delta^{(k)}=\widehat{\text{SR}}^{(\text{AIQ1})}-\widehat{\text{SR}}^{(k)}\quad\text{(full sample)},\qquad D\_{t}^{(k)}=\widehat{\text{SR}}\_{t}^{(\text{AIQ1})}-\widehat{\text{SR}}\_{t}^{(k)}\quad\text{(rolling)}. |  |

A positive value of Δ(k)\Delta^{(k)} or Dt(k)D\_{t}^{(k)} indicates that AIQ1 has the higher Sharpe ratio at the given horizon.

### Full-sample Sharpe ratio tests

We first test whether any estimator achieves a higher full-sample Sharpe ratio than AIQ1. For each competitor kk we compute the observed Sharpe difference

|  |  |  |
| --- | --- | --- |
|  | Δ^(k)=SR^(AIQ1)−SR^(k).\widehat{\Delta}^{(k)}=\widehat{\text{SR}}^{(\text{AIQ1})}-\widehat{\text{SR}}^{(k)}. |  |

To obtain its sampling distribution under the null, we use a moving-block bootstrap over monthly excess returns. Let

|  |  |  |
| --- | --- | --- |
|  | 𝐑t(k)=(rt(AIQ1),rt(k))⊤,t=1,…,T,\mathbf{R}\_{t}^{(k)}=\bigl(r\_{t}^{(\text{AIQ1})},\,r\_{t}^{(k)}\bigr)^{\top},\qquad t=1,\dots,T, |  |

and stack these in a T×2T\times 2 matrix R(k)R^{(k)}.

We form overlapping blocks of length LL months,

|  |  |  |
| --- | --- | --- |
|  | B1=(𝐑1(k),…,𝐑L(k)),B2=(𝐑2(k),…,𝐑L+1(k)),…,BT−L+1=(𝐑T−L+1(k),…,𝐑T(k)),B\_{1}=(\mathbf{R}\_{1}^{(k)},\dots,\mathbf{R}\_{L}^{(k)}),\;B\_{2}=(\mathbf{R}\_{2}^{(k)},\dots,\mathbf{R}\_{L+1}^{(k)}),\dots,\;B\_{T-L+1}=(\mathbf{R}\_{T-L+1}^{(k)},\dots,\mathbf{R}\_{T}^{(k)}), |  |

and then construct bootstrap samples by concatenating randomly selected blocks with replacement until at least TT observations have been accumulated, truncating to length TT. For each bootstrap replication b=1,…,Bb=1,\dots,B we denote the resampled series by {𝐑t∗(k,b)}t=1T\{\mathbf{R}\_{t}^{\*(k,b)}\}\_{t=1}^{T} and compute the corresponding Sharpe ratio difference

|  |  |  |
| --- | --- | --- |
|  | Δ∗(k,b)=SR^∗,(AIQ1)−SR^∗,(k),\Delta^{\*(k,b)}=\widehat{\text{SR}}^{\*,(\text{AIQ1})}-\widehat{\text{SR}}^{\*,(k)}, |  |

based on the bootstrap excess returns. This yields an empirical distribution {Δ∗(k,b)}b=1B\{\Delta^{\*(k,b)}\}\_{b=1}^{B}.

We report percentile 95%95\% confidence intervals for Δ(k)\Delta^{(k)} as the 2.52.5th and 97.597.5th percentiles of this bootstrap distribution. For the one-sided test

|  |  |  |
| --- | --- | --- |
|  | H0:SR(k)≥SR(AIQ1)vs.H1:SR(k)<SR(AIQ1),H\_{0}:\text{SR}^{(k)}\geq\text{SR}^{(\text{AIQ1})}\quad\text{vs.}\quad H\_{1}:\text{SR}^{(k)}<\text{SR}^{(\text{AIQ1})}, |  |

the bootstrap pp-value is approximated by

|  |  |  |
| --- | --- | --- |
|  | pfull(k)=Pr⁡(Δ∗(k)≤0)≈1B​∑b=1B𝕀​{Δ∗(k,b)≤0},p^{(k)}\_{\text{full}}=\Pr\!\bigl(\Delta^{\*(k)}\leq 0\bigr)\approx\frac{1}{B}\sum\_{b=1}^{B}\mathbb{I}\{\Delta^{\*(k,b)}\leq 0\}, |  |

that is, the fraction of bootstrap Sharpe differences that are less than or equal to zero. Small values of pfull(k)p^{(k)}\_{\text{full}} provide evidence that SR(AIQ1)\text{SR}^{(\text{AIQ1})} exceeds SR(k)\text{SR}^{(k)}. In the empirical results, GS2 and LS4 yield small one-sided pp-values and bootstrap confidence intervals for Δ(k)\Delta^{(k)} that are bounded away from zero, indicating that their full-sample Sharpe ratios are significantly lower than AIQ1’s. For the remaining estimators the confidence intervals include zero and the one-sided pp-values are relatively large, so there is no statistical evidence that any alternative delivers a higher Sharpe ratio than AIQ1.

### Rolling 36-month Sharpe ratio tests

We next examine the relative Sharpe performance over rolling 36-month windows. For each competitor kk and grid choice (monthly or every third month) we consider the sequence {Dt(k)}t=1T∗\{D\_{t}^{(k)}\}\_{t=1}^{T^{\*}} and its sample mean

|  |  |  |
| --- | --- | --- |
|  | D¯(k)=1T∗​∑t=1T∗Dt(k).\bar{D}^{(k)}=\frac{1}{T^{\*}}\sum\_{t=1}^{T^{\*}}D\_{t}^{(k)}. |  |

The parameter of interest is the unconditional mean

|  |  |  |
| --- | --- | --- |
|  | μD(k)=𝔼​[Dt(k)],\mu\_{D}^{(k)}=\mathbb{E}[D\_{t}^{(k)}], |  |

and we test the one-sided hypothesis

|  |  |  |
| --- | --- | --- |
|  | H0:μD(k)≤0vs.H1:μD(k)>0.H\_{0}:\mu\_{D}^{(k)}\leq 0\quad\text{vs.}\quad H\_{1}:\mu\_{D}^{(k)}>0. |  |

Under H0H\_{0} estimator kk is at least as good as AIQ1 in rolling Sharpe on average; rejection indicates that AIQ1 has the higher Sharpe ratio across 36-month windows.

Because the rolling windows overlap heavily, {Dt(k)}\{D\_{t}^{(k)}\} is serially correlated and potentially heteroskedastic. We therefore use both Newey–West heteroskedasticity- and autocorrelation-consistent (HAC) standard errors and a moving-block bootstrap for the mean.

#### Newey–West inference.

Let ut(k)=Dt(k)−D¯(k)u\_{t}^{(k)}=D\_{t}^{(k)}-\bar{D}^{(k)}, and define the sample autocovariances

|  |  |  |
| --- | --- | --- |
|  | γ^ℓ(k)=1T∗​∑t=ℓ+1T∗ut(k)​ut−ℓ(k),ℓ=0,1,…,q,\hat{\gamma}\_{\ell}^{(k)}=\frac{1}{T^{\*}}\sum\_{t=\ell+1}^{T^{\*}}u\_{t}^{(k)}u\_{t-\ell}^{(k)},\qquad\ell=0,1,\dots,q, |  |

for a truncation lag qq measured in months. The Newey–West estimator of the long-run variance of T∗1/2​D¯(k)T^{\*1/2}\bar{D}^{(k)} is

|  |  |  |
| --- | --- | --- |
|  | Ω^NW(k)=γ^0(k)+2​∑ℓ=1qwℓ​γ^ℓ(k),wℓ=1−ℓq+1(Bartlett weights).\widehat{\Omega}^{(k)}\_{\text{NW}}=\hat{\gamma}\_{0}^{(k)}+2\sum\_{\ell=1}^{q}w\_{\ell}\hat{\gamma}\_{\ell}^{(k)},\qquad w\_{\ell}=1-\frac{\ell}{q+1}\quad\text{(Bartlett weights)}. |  |

The HAC variance estimator for D¯(k)\bar{D}^{(k)} is then

|  |  |  |
| --- | --- | --- |
|  | Var^NW​(D¯(k))=Ω^NW(k)T∗,\widehat{\text{Var}}\_{\text{NW}}(\bar{D}^{(k)})=\frac{\widehat{\Omega}^{(k)}\_{\text{NW}}}{T^{\*}}, |  |

with corresponding standard error SENW​(D¯(k))=Var^NW​(D¯(k))\text{SE}\_{\text{NW}}(\bar{D}^{(k)})=\sqrt{\widehat{\text{Var}}\_{\text{NW}}(\bar{D}^{(k)})} and tt-statistic

|  |  |  |
| --- | --- | --- |
|  | tNW(k)=D¯(k)SENW​(D¯(k)).t^{(k)}\_{\text{NW}}=\frac{\bar{D}^{(k)}}{\text{SE}\_{\text{NW}}(\bar{D}^{(k)})}. |  |

For the one-sided test H0:μD(k)≤0H\_{0}:\mu\_{D}^{(k)}\leq 0 vs H1:μD(k)>0H\_{1}:\mu\_{D}^{(k)}>0, the pp-value is

|  |  |  |
| --- | --- | --- |
|  | pNW(k)=1−Φ​(tNW(k)),p^{(k)}\_{\text{NW}}=1-\Phi\bigl(t^{(k)}\_{\text{NW}}\bigr), |  |

where Φ​(⋅)\Phi(\cdot) is the standard normal distribution function. Small values of pNW(k)p^{(k)}\_{\text{NW}} indicate that the average 36-month Sharpe ratio of AIQ1 exceeds that of estimator kk.

#### Block bootstrap for the mean.

As a complementary robustness check, we also implement a moving-block bootstrap for the mean D¯(k)\bar{D}^{(k)}, using the same block length LL as in the full-sample analysis. We form overlapping blocks of {Dt(k)}\{D\_{t}^{(k)}\} and generate bootstrap samples by concatenating random blocks with replacement until T∗T^{\*} observations are obtained. For each replication bb we compute the bootstrap mean D¯∗(k,b)\bar{D}^{\*(k,b)}, yielding an empirical distribution {D¯∗(k,b)}b=1B\{\bar{D}^{\*(k,b)}\}\_{b=1}^{B}. Percentile confidence intervals for μD(k)\mu\_{D}^{(k)} are obtained from the empirical quantiles of this distribution. A one-sided bootstrap pp-value for H0:μD(k)≤0H\_{0}:\mu\_{D}^{(k)}\leq 0 is approximated by

|  |  |  |
| --- | --- | --- |
|  | pboot(k)=Pr⁡(D¯∗(k)≤0)≈1B​∑b=1B𝕀​{D¯∗(k,b)≤0}.p^{(k)}\_{\text{boot}}=\Pr\bigl(\bar{D}^{\*(k)}\leq 0\bigr)\approx\frac{1}{B}\sum\_{b=1}^{B}\mathbb{I}\{\bar{D}^{\*(k,b)}\leq 0\}. |  |

#### Interpretation.

In the empirical results, the point estimates D¯(k)\bar{D}^{(k)} are positive for all competitors, indicating that AIQ1’s 36-month Sharpe ratio is higher on average than that of every alternative estimator. For GS2 and LS4, both the HAC tt-statistics and the bootstrap confidence intervals support rejection of H0H\_{0} on both the monthly and thinned grids, implying that their rolling Sharpe ratios are significantly lower than AIQ1’s. For LS1 and the nonlinear shrinkage estimators NLS6–NLS8, the Newey–West pp-values on the monthly grid are also small, providing suggestive evidence of a Sharpe premium for AIQ1, although the bootstrap intervals are somewhat wider. For the remaining competitors we do not reject H0H\_{0} at conventional levels, so there is no statistical evidence that any of them achieves a higher Sharpe ratio than AIQ1 over 36-month windows. Taken together with the full-sample tests, these results show that while several estimators are comparable to AIQ1 in Sharpe, none can be shown to outperform it, and the weaker methods are clearly dominated.