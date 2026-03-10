---
authors:
- Abdulrahman Alswaidan
- Jeffrey D. Varner
doc_id: arxiv:2603.06875v1
family_id: arxiv:2603.06875
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository:
  https://github.com/varnerlab/stochastic-attention-study-paper.git.'
url_abs: http://arxiv.org/abs/2603.06875v1
url_html: https://arxiv.org/html/2603.06875v1
venue: arXiv q-fin
version: 1
year: 2026
---


Abdulrahman Alswaidan and Jeffrey D. Varner
  
R.F. Smith School of Chemical and Biomolecular Engineering
  
Cornell University, Ithaca, NY 14850
  
{aa2725, jdv27}@cornell.edu

###### Abstract

Attention heads retrieve: given a query, they return a softmax-weighted average of stored values. We show that this computation is one step of gradient descent on a classical energy function, and that Langevin sampling from the corresponding distribution yields *stochastic attention*: a training-free sampler controlled by a single temperature. Lowering the temperature gives exact retrieval; raising it gives open-ended generation. Because the energy gradient equals the attention map, no score network, training loop, or learned model is required. We validate on four domains (64 to 4,096 dimensions). At generation temperature, stochastic attention is 2.6 times more novel and 2.0 times more diverse than the best learned baseline (a variational autoencoder trained on the same patterns), while matching a Metropolis-corrected gold standard. A simple signal-to-noise rule selects the operating temperature for any dimension. The approach requires no architectural changes and extends naturally to retrieval-augmented generation and in-context learning.

## 1 Introduction

Attention is the central computational primitive of modern deep learning [[29](#bib.bib1 "Attention is all you need")]. Given a query, it computes a softmax-weighted average of stored values, a powerful operation but a fundamentally *deterministic* one. The same query always produces the same output. Attention retrieves; it does not generate. Yet generation from a structured memory is precisely what many downstream tasks require: producing novel but plausible continuations, interpolating between stored prototypes, or exploring the space of patterns consistent with partial evidence. A natural question arises: *can the attention mechanism itself be made stochastic, in a principled way, so that it samples from the space of memories rather than merely returning their weighted average?*

The ingredients for an answer already exist, though they have not been assembled. On one side, a line of work on associative memory, from Hopfield networks [[13](#bib.bib2 "Neural networks and physical systems with emergent collective computational abilities")] through dense associative memories [[16](#bib.bib4 "Dense associative memory for pattern recognition"), [17](#bib.bib14 "Large associative memory problem in neurobiology and machine learning")] to the modern continuous formulation of Ramsauer et al. [[21](#bib.bib3 "Hopfield networks is all you need")], has revealed that each attention head implicitly performs gradient descent on a smooth, confining energy whose minima are stored patterns. On the other side, a mature theory of Langevin dynamics [[23](#bib.bib5 "Exponential convergence of Langevin distributions and their discrete approximations"), [30](#bib.bib7 "Bayesian learning via stochastic gradient Langevin dynamics"), [7](#bib.bib8 "Nonasymptotic convergence analysis for the unadjusted Langevin algorithm")] shows how to convert *any* such energy into a sampler for the corresponding Boltzmann distribution: one simply adds calibrated noise to the gradient update. Meanwhile, energy-based models [[19](#bib.bib24 "A tutorial on energy-based learning"), [27](#bib.bib18 "How to train your energy-based models")] and score-based diffusion methods [[26](#bib.bib16 "Generative modeling by estimating gradients of the data distribution"), [28](#bib.bib17 "Score-based generative modeling through stochastic differential equations")] have demonstrated the power of Langevin-type sampling for generation, but rely on black-box neural networks whose scores must be learned. The Energy Transformer [[12](#bib.bib15 "Energy transformer")] brings Hopfield energies into a deep architecture, yet remains a discriminative model that descends the energy rather than sampling from it. The classical retrieval-generation duality (Hopfield networks retrieve, Boltzmann machines sample, and both share the same energy [[1](#bib.bib21 "A learning algorithm for Boltzmann machines")]) has not been lifted to the modern continuous setting.

In this paper, we close that gap. We show that applying the unadjusted Langevin algorithm to the modern Hopfield energy yields a *stochastic attention* update: a single iteration comprising a contraction toward the origin, a softmax attention pull toward stored memories, and an isotropic Gaussian perturbation whose magnitude is governed by the temperature. The inverse temperature β\beta interpolates continuously between exact retrieval (β→∞\beta\to\infty) and open-ended exploration (β→0\beta\to 0), providing a principled generation mechanism that requires no learned score network, no training loop, and no contrastive objective. Because the gradient of the Hopfield energy is exactly the identity minus the attention map, every step of the sampler is computed by the same primitive operations as a standard attention head. In particular, 𝐗\mathbf{X} can be the key matrix of any pretrained attention layer, making stochastic attention a zero-shot stochastic decoding layer compatible with retrieval-augmented generation and in-context learning settings. The energy’s analytic structure (infinite differentiability, Lipschitz gradients, and a quadratic confining bound) delivers convergence guarantees that generic energy-based models cannot offer without additional assumptions. In practice, the same algorithm realizes two qualitatively distinct operating regimes: at high β\beta it performs *structured retrieval*, generating outputs that closely resemble stored patterns; once β\beta falls below a signal-to-noise threshold (SNR≈0.025\mathrm{SNR}\approx 0.025, derived in Section 4), it performs *genuine generation*, producing novel outputs that outperform learned baselines on both novelty and diversity. Section 2 surveys related work; Section 3 reviews the necessary background on attention, modern Hopfield networks, and Langevin dynamics; Section 4 derives the stochastic attention update, presents the algorithm, and characterizes its properties; Section 5 validates both regimes experimentally across four domains.

## 2 Related Work

Our work lies at the intersection of associative memory, energy-based modeling, and Langevin sampling. We review each strand and identify where existing approaches stop short of the connection we propose.

#### Hopfield networks and associative memory.

Hopfield [[13](#bib.bib2 "Neural networks and physical systems with emergent collective computational abilities")] introduced a recurrent network of NN binary neurons whose asynchronous dynamics minimize the quadratic energy E​(𝐬)=−12​𝐬⊤​𝐖𝐬E(\mathbf{s})=-\frac{1}{2}\mathbf{s}^{\top}\mathbf{W}\mathbf{s}, with 𝐖=1N​∑i𝐦i​𝐦i⊤\mathbf{W}=\frac{1}{N}\sum\_{i}\mathbf{m}\_{i}\mathbf{m}\_{i}^{\top} the Hebbian weight matrix. Stored patterns correspond to local minima of EE, so retrieval proceeds by gradient descent from an initial probe. When the KK patterns are uncorrelated random binary vectors, Amit et al. [[2](#bib.bib6 "Storing infinite numbers of patterns in a spin-glass model of neural networks")] showed via a replica-symmetric mean-field analysis that reliable retrieval is possible only when the load ratio K/N<αc≈0.138K/N<\alpha\_{c}\approx 0.138 (where αc\alpha\_{c} denotes the critical load ratio, not to be confused with the step size α\alpha used later); beyond this threshold the energy landscape becomes dominated by spurious mixtures. Folli et al. [[8](#bib.bib11 "On the maximum storage capacity of the Hopfield model")] later gave exact finite-NN expressions for the bit-error probability, confirming the αc\alpha\_{c} transition and showing that the number of retrieval errors grows with K/NK/N as cross-talk noise overwhelms the coherent signal.

The modern Hopfield network program, initiated by Krotov and Hopfield [[16](#bib.bib4 "Dense associative memory for pattern recognition")], addresses these shortcomings by replacing the quadratic interaction with higher-order (polynomial or exponential) interaction functions. Dense associative memories with degree-nn polynomial energy store on the order of Nn−1N^{n-1} patterns, breaking the linear capacity barrier by trading pairwise for higher-order synaptic interactions, and the resulting retrieval dynamics map onto deep networks with rectified polynomial activations. At the top of this hierarchy sits the log-sum-exp (lse) energy, which achieves storage capacity that grows *exponentially* in the pattern dimension NN [[21](#bib.bib3 "Hopfield networks is all you need")]. Ramsauer et al. [[21](#bib.bib3 "Hopfield networks is all you need")] proved that the continuous-state retrieval map associated with the lse energy is equivalent to transformer-style attention: each attention head performs one step of gradient descent on the energy, and the fixed points of the dynamics (global, metastable, or single-pattern) correspond to different retrieval regimes. All of these works, however, focus exclusively on *retrieval*, that is, the convergence of iterates to stored patterns or their convex combinations. Sampling from the Boltzmann distribution defined by the same energy, which would yield a generative mechanism, is not explored. Our work fills this gap by applying Langevin dynamics to the modern Hopfield energy, converting the deterministic retrieval map into a stochastic sampler.

The idea that a single energy function supports both retrieval and generation dates to the Boltzmann machine [[1](#bib.bib21 "A learning algorithm for Boltzmann machines")], which shares the quadratic energy of the Hopfield network but samples from it via Gibbs dynamics instead of minimizing it. Sejnowski [[24](#bib.bib22 "Higher-order Boltzmann machines")] extended this to higher-order interactions, corresponding to the polynomial energies later studied by Krotov and Hopfield [[16](#bib.bib4 "Dense associative memory for pattern recognition")]. However, these classical models operate on binary states with discrete Gibbs sampling; our formulation inherits the same duality in the continuous, modern Hopfield setting where Langevin dynamics scales naturally to high dimensions.

#### Energy-based, score-based and diffusion models.

Energy-based models (EBMs) define a probability distribution p​(𝐱)∝exp⁡(−E​(𝐱))p(\mathbf{x})\propto\exp(-E(\mathbf{x})) for an energy function EE parameterized by a neural network [[19](#bib.bib24 "A tutorial on energy-based learning")]. Training typically proceeds by contrastive divergence [[10](#bib.bib23 "Training products of experts by minimizing contrastive divergence")], score matching [[14](#bib.bib25 "Estimation of non-normalized statistical models by score matching")], or noise contrastive estimation [[27](#bib.bib18 "How to train your energy-based models")]. The energy in a generic EBM is a black-box neural network, so its gradient (the score function) must be estimated or approximated. By contrast, the modern Hopfield energy has a *closed-form* gradient (identity minus softmax attention) requiring no auxiliary score network. Moreover, 𝐗\mathbf{X} is given as data rather than learned, so no training loop is needed, and the log-sum-exp structure provides analytic guarantees (smoothness, Lipschitz gradients, quadratic confinement) that generic EBMs achieve only with careful architectural design. The Energy Transformer [[12](#bib.bib15 "Energy transformer")] shows that Hopfield-type energies improve discriminative tasks (graph anomaly detection, image completion) but does not sample from the Boltzmann distribution; our work uses the same energy class for generation.

Song and Ermon [[26](#bib.bib16 "Generative modeling by estimating gradients of the data distribution")] introduced score-based generative modeling, in which a neural network is trained to approximate ∇log⁡p​(𝐱)\nabla\log p(\mathbf{x}) at multiple noise levels, and samples are drawn by annealed Langevin dynamics. Song et al. [[28](#bib.bib17 "Score-based generative modeling through stochastic differential equations")] unified this framework with diffusion probabilistic models [[11](#bib.bib19 "Denoising diffusion probabilistic models"), [25](#bib.bib20 "Deep unsupervised learning using nonequilibrium thermodynamics")] by showing that both arise from forward and reverse-time stochastic differential equations. These methods achieve remarkable sample quality but rely on a learned score network trained on data; our score function is *exact* and *analytic*, ∇log⁡pβ​(𝝃)=β​(𝐓​(𝝃)−𝝃)\nabla\log p\_{\beta}(\boldsymbol{\xi})=\beta(\mathbf{T}(\boldsymbol{\xi})-\boldsymbol{\xi}), requiring no training, at the cost of being restricted to the Boltzmann distribution of a fixed memory 𝐗\mathbf{X}, a restriction that permits convergence guarantees unavailable in the learned-score setting.

Normalizing flows [[22](#bib.bib27 "Variational inference with normalizing flows")] construct flexible generative models via learned invertible transformations; like diffusion models, they require training data and a learned bijection, and do not expose a closed-form score function over a fixed memory. Several works have introduced stochasticity into the attention mechanism itself: Deng et al. [[6](#bib.bib28 "Latent alignment and variational attention")] replace the softmax with a latent categorical or Gaussian variable, trained via variational inference, to model alignment uncertainty in sequence-to-sequence tasks. These approaches treat attention weights as random variables to be inferred, whereas our stochasticity arises from Langevin dynamics on a fixed Hopfield energy: the temperature parameter 1/β1/\beta controls the noise level, no variational objective is optimized, and the goal is memory-based generation rather than alignment uncertainty.

## 3 Background

We build our approach on three ideas that, taken separately, are well understood but whose intersection has not been explored. We review them here in the order that motivates our construction: attention as a computational primitive, its reinterpretation as energy minimization via modern Hopfield networks, and Langevin dynamics as the tool that converts any energy landscape into a sampler.

#### Attention as deterministic retrieval.

The transformer architecture [[29](#bib.bib1 "Attention is all you need")] computes attention via queries 𝐐\mathbf{Q}, keys 𝐊\mathbf{K}, and values 𝐕\mathbf{V}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Attention​(𝐐,𝐊,𝐕)=softmax⁡(𝐐𝐊⊤d)​𝐕,\mathrm{Attention}(\mathbf{Q},\mathbf{K},\mathbf{V})=\operatorname{softmax}\!\left(\frac{\mathbf{Q}\mathbf{K}^{\top}}{\sqrt{d}}\right)\mathbf{V}, |  | (1) |

where dd is the key dimension and the softmax is applied row-wise. Each output row is a convex combination of value vectors, with weights determined by query-key similarity.
Crucially, this operation is *deterministic*: given the same query, it always returns the same weighted average. Attention retrieves information from a fixed store; it does not generate anything new. Our goal is to relax this limitation, but to do so we first need to understand what energy landscape attention is implicitly descending.

#### The energy landscape beneath attention.

The classical Hopfield network [[13](#bib.bib2 "Neural networks and physical systems with emergent collective computational abilities")] stores KK binary patterns 𝐦1,…,𝐦K∈{−1,+1}N\mathbf{m}\_{1},\dots,\mathbf{m}\_{K}\in\{-1,+1\}^{N} via the quadratic energy

|  |  |  |  |
| --- | --- | --- | --- |
|  | Eclassical​(𝐬)=−12​𝐬⊤​𝐖𝐬−𝐛⊤​𝐬,𝐖=1N​∑i=1K𝐦i​𝐦i⊤,E\_{\mathrm{classical}}(\mathbf{s})=-\tfrac{1}{2}\,\mathbf{s}^{\top}\mathbf{W}\mathbf{s}-\mathbf{b}^{\top}\mathbf{s},\qquad\mathbf{W}=\frac{1}{N}\sum\_{i=1}^{K}\mathbf{m}\_{i}\mathbf{m}\_{i}^{\top}, |  | (2) |

where 𝐛∈ℝN\mathbf{b}\in\mathbb{R}^{N} is an external bias (typically set to zero). Retrieval proceeds by coordinate-wise sign updates that descend EclassicalE\_{\mathrm{classical}}. The storage capacity of this network scales as 𝒪​(N)\mathcal{O}(N) [[2](#bib.bib6 "Storing infinite numbers of patterns in a spin-glass model of neural networks")], severely limiting the number of patterns.

Modern (continuous) Hopfield networks [[21](#bib.bib3 "Hopfield networks is all you need")] overcome this bottleneck by replacing the quadratic energy with a log-sum-exp (lse) form. Let 𝐗=[𝐦1,…,𝐦K]∈ℝN×K\mathbf{X}=[\mathbf{m}\_{1},\dots,\mathbf{m}\_{K}]\in\mathbb{R}^{N\times K} be the memory matrix, β>0\beta>0 an inverse temperature, and M:=maxi⁡‖𝐦i‖2M:=\max\_{i}\|\mathbf{m}\_{i}\|\_{2}. The energy is

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(𝝃)=−lseβ⁡(𝐗⊤​𝝃)+12​‖𝝃‖22+1β​log⁡K+12​M2,E(\boldsymbol{\xi})=-\operatorname{lse}\_{\beta}\!\bigl(\mathbf{X}^{\top}\boldsymbol{\xi}\bigr)+\tfrac{1}{2}\|\boldsymbol{\xi}\|\_{2}^{2}+\tfrac{1}{\beta}\log K+\tfrac{1}{2}M^{2}, |  | (3) |

where lseβ⁡(𝐳):=β−1​log⁡(∑i=1Keβ​zi)\operatorname{lse}\_{\beta}(\mathbf{z}):=\beta^{-1}\log\bigl(\sum\_{i=1}^{K}e^{\beta z\_{i}}\bigr) is the scaled log-sum-exp. The associated retrieval (update) map is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐓​(𝝃):=𝐗​softmax⁡(β​𝐗⊤​𝝃),\mathbf{T}(\boldsymbol{\xi}):=\mathbf{X}\,\operatorname{softmax}\!\bigl(\beta\,\mathbf{X}^{\top}\boldsymbol{\xi}\bigr), |  | (4) |

and one can show that ∇E​(𝝃)=𝝃−𝐓​(𝝃)\nabla E(\boldsymbol{\xi})=\boldsymbol{\xi}-\mathbf{T}(\boldsymbol{\xi}) [[21](#bib.bib3 "Hopfield networks is all you need")]. Hence the deterministic iteration 𝝃t+1=𝐓​(𝝃t)\boldsymbol{\xi}^{t+1}=\mathbf{T}(\boldsymbol{\xi}^{t}) is gradient descent on EE with unit step size, converging to a fixed point 𝝃⋆\boldsymbol{\xi}^{\star} satisfying 𝐓​(𝝃⋆)=𝝃⋆\mathbf{T}(\boldsymbol{\xi}^{\star})=\boldsymbol{\xi}^{\star}.

Two properties of this energy are essential for what follows. First, EE is C∞C^{\infty} (the lse is infinitely differentiable), so standard gradient-based convergence theory applies. Second, EE is *confining*: it admits the lower bound [[21](#bib.bib3 "Hopfield networks is all you need")]

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(𝝃)≥12​(‖𝝃‖2−M)2≥ 0,E(\boldsymbol{\xi})\;\geq\;\tfrac{1}{2}\bigl(\|\boldsymbol{\xi}\|\_{2}-M\bigr)^{2}\;\geq\;0, |  | (5) |

so EE grows at least quadratically as ‖𝝃‖→∞\|\boldsymbol{\xi}\|\to\infty. Iterates cannot escape to infinity.

#### The bridge.

Ramsauer et al. [[21](#bib.bib3 "Hopfield networks is all you need")] observed that single-head attention ([1](#S3.E1 "In Attention as deterministic retrieval. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) with 𝐐=𝝃⊤\mathbf{Q}=\boldsymbol{\xi}^{\top}, 𝐊=𝐗⊤\mathbf{K}=\mathbf{X}^{\top}, 𝐕=𝐗⊤\mathbf{V}=\mathbf{X}^{\top}, and inverse temperature β=1/d\beta=1/\sqrt{d} is *exactly one step* of the retrieval map ([4](#S3.E4 "In The energy landscape beneath attention. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")). In other words, every attention head is implicitly performing energy minimization on ([3](#S3.E3 "In The energy landscape beneath attention. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")), revealing a hidden energy landscape whose minima are the stored memories.

#### From minimization to sampling.

Given a smooth potential U:ℝN→ℝU:\mathbb{R}^{N}\to\mathbb{R} with target density p​(𝐱)∝exp⁡(−U​(𝐱))p(\mathbf{x})\propto\exp(-U(\mathbf{x})), the (overdamped) Langevin stochastic differential equation is

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​𝐱t=−∇U​(𝐱t)​d​t+2​d​𝐁t,d\mathbf{x}\_{t}=-\nabla U(\mathbf{x}\_{t})\,dt+\sqrt{2}\,d\mathbf{B}\_{t}, |  | (6) |

where 𝐁t\mathbf{B}\_{t} is standard NN-dimensional Brownian motion. The process ([6](#S3.E6 "In From minimization to sampling. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) has pp as its unique stationary distribution provided two regularity conditions hold [[23](#bib.bib5 "Exponential convergence of Langevin distributions and their discrete approximations")]: (R1) ∇U\nabla U is LL-Lipschitz, i.e. ‖∇U​(𝐱)−∇U​(𝐲)‖2≤L​‖𝐱−𝐲‖2\|\nabla U(\mathbf{x})-\nabla U(\mathbf{y})\|\_{2}\leq L\|\mathbf{x}-\mathbf{y}\|\_{2}; and (R2) UU is dissipative, i.e. ⟨∇U​(𝐱),𝐱⟩≥a​‖𝐱‖22−b\langle\nabla U(\mathbf{x}),\mathbf{x}\rangle\geq a\|\mathbf{x}\|\_{2}^{2}-b for constants a>0a>0, b≥0b\geq 0.
The modern Hopfield energy ([3](#S3.E3 "In The energy landscape beneath attention. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) satisfies both: it is C∞C^{\infty} with Lipschitz gradient (R1), and its quadratic lower bound ([5](#S3.E5 "In The energy landscape beneath attention. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) implies dissipativity (R2).

In practice, we discretize ([6](#S3.E6 "In From minimization to sampling. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) with step size α>0\alpha>0 to obtain the *unadjusted Langevin algorithm* (ULA) [[23](#bib.bib5 "Exponential convergence of Langevin distributions and their discrete approximations")]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱t+1=𝐱t−α​∇U​(𝐱t)+2​α​ϵt,ϵt∼𝒩​(𝟎,𝐈).\mathbf{x}\_{t+1}=\mathbf{x}\_{t}-\alpha\,\nabla U(\mathbf{x}\_{t})+\sqrt{2\alpha}\;\boldsymbol{\epsilon}\_{t},\quad\boldsymbol{\epsilon}\_{t}\sim\mathcal{N}(\mathbf{0},\mathbf{I}). |  | (7) |

The noise scale 2​α\sqrt{2\alpha} maintains the *fluctuation-dissipation relation* so that, in the limit α→0\alpha\to 0, iterates sample exactly from pp [[30](#bib.bib7 "Bayesian learning via stochastic gradient Langevin dynamics")]. For finite α\alpha the stationary distribution is biased, but the bias vanishes as α→0\alpha\to 0 and can be bounded when UU is smooth and strongly convex outside a ball [[7](#bib.bib8 "Nonasymptotic convergence analysis for the unadjusted Langevin algorithm")]. Introducing an inverse temperature β>0\beta>0 via U=β​EU=\beta E yields a Boltzmann target pβ∝exp⁡(−β​E)p\_{\beta}\propto\exp(-\beta E); the temperature 1/β1/\beta controls the trade-off between exploitation (retrieval) and exploration (generation). Section 4 makes this connection explicit.

## 4 Method

The background section established three facts: (i) attention is one step of gradient descent on the modern Hopfield energy EE, (ii) EE is smooth and confining, and (iii) Langevin dynamics converts any smooth, confining energy into a sampler for the corresponding Boltzmann distribution. We now combine these facts to derive *stochastic attention*, a single update rule that interpolates between deterministic memory retrieval and stochastic generation of novel states.

### 4.1 Stochastic Attention Update

Recall the setup from Section 3: the memory matrix 𝐗=[𝐦1,…,𝐦K]∈ℝN×K\mathbf{X}=[\mathbf{m}\_{1},\dots,\mathbf{m}\_{K}]\in\mathbb{R}^{N\times K} has KK stored memories as its columns, each of dimension NN. We wish to sample from the Boltzmann distribution induced by the modern Hopfield energy ([3](#S3.E3 "In The energy landscape beneath attention. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | pβ​(𝝃)∝exp⁡(−β​E​(𝝃)),p\_{\beta}(\boldsymbol{\xi})\;\propto\;\exp\!\bigl(-\beta\,E(\boldsymbol{\xi})\bigr), |  | (8) |

where β>0\beta>0 is the inverse temperature and EE is defined in ([3](#S3.E3 "In The energy landscape beneath attention. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")). To apply the ULA ([7](#S3.E7 "In From minimization to sampling. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) we need ∇E\nabla E. The background already established the identity ∇E​(𝝃)=𝝃−𝐓​(𝝃)\nabla E(\boldsymbol{\xi})=\boldsymbol{\xi}-\mathbf{T}(\boldsymbol{\xi}), where 𝐓\mathbf{T} is the softmax attention map ([4](#S3.E4 "In The energy landscape beneath attention. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")). Reparameterizing the ULA via U=β​EU=\beta E and rescaling time by β\beta (so the gradient of EE, rather than β​E\beta E, appears directly), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝃t+1=𝝃t−α​(𝝃t−𝐓​(𝝃t))+2​αβ​ϵt,ϵt∼𝒩​(𝟎,𝐈),\boldsymbol{\xi}\_{t+1}=\boldsymbol{\xi}\_{t}-\alpha\bigl(\boldsymbol{\xi}\_{t}-\mathbf{T}(\boldsymbol{\xi}\_{t})\bigr)+\sqrt{\tfrac{2\alpha}{\beta}}\;\boldsymbol{\epsilon}\_{t},\qquad\boldsymbol{\epsilon}\_{t}\sim\mathcal{N}(\mathbf{0},\mathbf{I}), |  | (9) |

which, after collecting terms, takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝃t+1=(1−α)​𝝃t+α​𝐗​softmax⁡(β​𝐗⊤​𝝃t)+2​αβ​ϵt\boxed{\;\boldsymbol{\xi}\_{t+1}=(1-\alpha)\,\boldsymbol{\xi}\_{t}+\alpha\,\mathbf{X}\,\operatorname{softmax}\!\bigl(\beta\,\mathbf{X}^{\top}\boldsymbol{\xi}\_{t}\bigr)+\sqrt{\tfrac{2\alpha}{\beta}}\;\boldsymbol{\epsilon}\_{t}\;} |  | (10) |

This is the *stochastic attention* update. Each iteration performs three operations: a contraction toward the origin (the (1−α)​𝝃t(1-\alpha)\boldsymbol{\xi}\_{t} term), a softmax-weighted pull toward stored memories (the attention term), and an isotropic Gaussian perturbation whose magnitude is governed by the temperature 1/β1/\beta. The complete procedure is given as pseudocode in Algorithm [1](#alg1 "Algorithm 1 ‣ 4.1 Stochastic Attention Update ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."). Because the memory matrix 𝐗\mathbf{X} is fixed and known, each step requires only the same primitive operations as a single attention head: two matrix-vector products, one softmax, and one Gaussian draw, for a per-step cost of 𝒪​(N​K)\mathcal{O}(NK).

Algorithm 1  Stochastic Attention Sampler

0: Memory matrix 𝐗∈ℝN×K\mathbf{X}\in\mathbb{R}^{N\times K}, inverse temperature β>0\beta>0, step size α∈(0,1)\alpha\in(0,1), number of iterations TT, initial state 𝝃0∈ℝN\boldsymbol{\xi}\_{0}\in\mathbb{R}^{N}

0: Sample trajectory 𝝃0,𝝃1,…,𝝃T\boldsymbol{\xi}\_{0},\boldsymbol{\xi}\_{1},\dots,\boldsymbol{\xi}\_{T}

1: for t=0,1,…,T−1t=0,1,\dots,T-1 do

2:  𝐚t←softmax⁡(β​𝐗⊤​𝝃t)\mathbf{a}\_{t}\leftarrow\operatorname{softmax}\!\bigl(\beta\,\mathbf{X}^{\top}\boldsymbol{\xi}\_{t}\bigr) ⊳\triangleright attention weights

3:  ϵt∼𝒩​(𝟎,𝐈N)\boldsymbol{\epsilon}\_{t}\sim\mathcal{N}(\mathbf{0},\mathbf{I}\_{N})

4:  𝝃t+1←(1−α)​𝝃t+α​𝐗​𝐚t+2​α/β​ϵt\boldsymbol{\xi}\_{t+1}\leftarrow(1-\alpha)\,\boldsymbol{\xi}\_{t}+\alpha\,\mathbf{X}\,\mathbf{a}\_{t}+\sqrt{2\alpha/\beta}\;\boldsymbol{\epsilon}\_{t}

5: end for

### 4.2 Properties and Limiting Behavior

The update ([10](#S4.E10 "In 4.1 Stochastic Attention Update ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) is controlled by two parameters, the inverse temperature β\beta and the step size α\alpha, that together determine where the sampler sits on a spectrum from exact retrieval to open-ended generation.

When β→∞\beta\to\infty and the noise vanishes, the softmax sharpens to a hard arg⁡max\arg\max and the update reduces to deterministic retrieval of the nearest stored memory (*hard attention*). At finite β\beta with zero noise, the update yields the standard softmax-weighted average familiar from transformers (*soft attention*). When β\beta is finite and noise is present, the sampler generates states that fluctuate around stored memories, producing novel patterns shaped by the memory geometry (*stochastic attention*). As β→0\beta\to 0, the Boltzmann distribution flattens and sampling becomes noise-dominated. The step size α∈(0,1)\alpha\in(0,1) controls discretization fidelity: smaller α\alpha reduces ULA bias [[7](#bib.bib8 "Nonasymptotic convergence analysis for the unadjusted Langevin algorithm")] at the cost of slower mixing, while larger α\alpha accelerates exploration but increases discretization error.

Beyond these limiting behaviors, the sampler inherits concrete guarantees from the analytic structure of the Hopfield energy. Because the gradient ∇E​(𝝃)=𝝃−𝐓​(𝝃)\nabla E(\boldsymbol{\xi})=\boldsymbol{\xi}-\mathbf{T}(\boldsymbol{\xi}) is computed exactly by a single attention operation, the score function ∇log⁡pβ=β​(𝐓−𝝃)\nabla\log p\_{\beta}=\beta(\mathbf{T}-\boldsymbol{\xi}) is known in closed form; no auxiliary score network is needed. The following proposition (proved in Appendix [B](#A2 "Appendix B Proof of Proposition 1 ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) makes the regularity conditions from Section 3 explicit.

###### Proposition 1.

Let σmax=‖𝐗‖op\sigma\_{\max}=\|\mathbf{X}\|\_{\mathrm{op}} denote the largest singular value of the memory matrix. The modern Hopfield energy ([3](#S3.E3 "In The energy landscape beneath attention. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) has Lipschitz-continuous gradient with constant L=1+β​σmax2/2L=1+\beta\sigma\_{\max}^{2}/2 and satisfies the dissipativity condition ⟨∇E​(𝛏),𝛏⟩≥‖𝛏‖22/2−M2/2\langle\nabla E(\boldsymbol{\xi}),\boldsymbol{\xi}\rangle\geq\|\boldsymbol{\xi}\|\_{2}^{2}/2-M^{2}/2 for all 𝛏∈ℝN\boldsymbol{\xi}\in\mathbb{R}^{N}.

The Lipschitz constant grows linearly in β\beta: the energy landscape sharpens at low temperature and step-size selection becomes more delicate. The Hessian satisfies ∇2E⪰(1−β​σmax2/2)​𝐈\nabla^{2}E\succeq(1-\beta\sigma\_{\max}^{2}/2)\mathbf{I}, so EE is strictly convex when β​σmax2<2\beta\sigma\_{\max}^{2}<2, yielding the following convergence guarantee.

###### Corollary 2.

When β​σmax2<2\beta\sigma\_{\max}^{2}<2, the potential U=β​EU=\beta E is mm-strongly convex with m=β​(1−β​σmax2/2)m=\beta(1-\beta\sigma\_{\max}^{2}/2) and has LUL\_{U}-Lipschitz gradient with LU=β​(1+β​σmax2/2)L\_{U}=\beta(1+\beta\sigma\_{\max}^{2}/2). The iterates of Algorithm [1](#alg1 "Algorithm 1 ‣ 4.1 Stochastic Attention Update ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") then converge to pβp\_{\beta} in W2W\_{2} at a geometric rate, with a discretization bias that vanishes as α→0\alpha\to 0 [[4](#bib.bib9 "Theoretical guarantees for approximate sampling from a smooth and log-concave density"), [7](#bib.bib8 "Nonasymptotic convergence analysis for the unadjusted Langevin algorithm")]. For arbitrary β>0\beta>0 the continuous-time Langevin diffusion is geometrically ergodic [[23](#bib.bib5 "Exponential convergence of Langevin distributions and their discrete approximations")]; the ULA discretization approximates pβp\_{\beta} with bias O​(α)O(\alpha).

#### Scope of the convergence guarantee.

Corollary [2](#Thmtheorem2 "Corollary 2. ‣ 4.2 Properties and Limiting Behavior ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")’s geometric-rate guarantee requires β​σmax2<2\beta\sigma\_{\max}^{2}<2, i.e., a log-concave energy. In our experiments σmax2≈2\sigma\_{\max}^{2}\approx 2–33, so this condition holds only for β≲1\beta\lesssim 1, far below the operating range. At β≥200\beta\geq 200 the energy is multimodal and the log-concave rate bound no longer applies; deriving explicit mixing-time bounds in this regime is an open problem. Two complementary guarantees nonetheless support the operating regime: the continuous-time Langevin SDE is geometrically ergodic for any β>0\beta>0 by Proposition [1](#Thmtheorem1 "Proposition 1. ‣ 4.2 Properties and Limiting Behavior ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") [[23](#bib.bib5 "Exponential convergence of Langevin distributions and their discrete approximations")], and the MALA acceptance rate of 99.2% at α=0.01\alpha{=}0.01 (Table [1](#S5.T1 "Table 1 ‣ Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) confirms negligible ULA discretization bias in practice.

Because 𝐗\mathbf{X} is given as data, there are no learned parameters: no training loop, no contrastive divergence, and no score-matching objective. The confining bound ([5](#S3.E5 "In The energy landscape beneath attention. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) keeps iterates concentrated near conv​{𝐦1,…,𝐦K}\mathrm{conv}\{\mathbf{m}\_{1},\dots,\mathbf{m}\_{K}\} with excursions controlled by 2​α/β\sqrt{2\alpha/\beta}; Section 5 derives a dimension-independent β\beta-selection rule from the per-step signal-to-noise ratio.

## 5 Experiments

![Refer to caption](2603.06875v1/x1.png)


Figure 1: Synthetic experiments.
(a) Phase behavior as a function of inverse temperature β\beta (d=64d=64, K=16K=16). Left axis (blue): mean cosine similarity to the nearest stored pattern; right axis (coral): scaled entropy H​(𝐚)/log⁡KH(\mathbf{a})/\log K. Both diagnostics reveal a smooth transition centered near β≈5​–​10\beta\approx 5\text{--}10 (gold band).
(b) Convergence validation (d=8d=8, K=4K=4, β=5\beta=5). Pooled energy density from eight independent chains (gray) overlaid on a long-run reference distribution (coral); inset reports the Kolmogorov–Smirnov statistic and moment differences.

#### Temperature spectrum, Convergence diagnostics and Load Ratio using synthetic data.

For the first three experiments we constructed memory matrices whose columns are independent draws from the uniform distribution on the unit sphere 𝕊d−1\mathbb{S}^{d-1}.
Concretely, each pattern was sampled as 𝐱k∼𝒩​(𝟎,𝐈d)\mathbf{x}\_{k}\sim\mathcal{N}(\mathbf{0},\mathbf{I}\_{d}) and normalized, 𝐱k←𝐱k/∥𝐱k∥\mathbf{x}\_{k}\leftarrow\mathbf{x}\_{k}/\lVert\mathbf{x}\_{k}\rVert.
This is the standard generative model in the Hopfield capacity literature [[2](#bib.bib6 "Storing infinite numbers of patterns in a spin-glass model of neural networks"), [8](#bib.bib11 "On the maximum storage capacity of the Hopfield model")] and ensures that, in expectation, the KK patterns are nearly orthogonal for moderate load ratios K/dK/d.
Unless otherwise noted we fixed d=64d=64; the convergence experiment used d=8d=8 so that the Boltzmann target density remained tractable for ground-truth comparison.
All datasets were generated with fixed random seeds.

We evaluated how the inverse temperature β\beta controlled the transition from noise-dominated diffusion to near-deterministic retrieval (Fig. [1](#S5.F1 "Figure 1 ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")a).
We stored K=16K=16 unit-norm patterns in 𝐗∈ℝ64×16\mathbf{X}\in\mathbb{R}^{64\times 16} and ran Algorithm 1 for T=10,000T=10{,}000 iterations at each of 25 values of β\beta spanning the range [10−2, 103][10^{-2},\,10^{3}] (approximately log-spaced), with step size α=0.01\alpha=0.01 and a burn-in of 2,0002{,}000 samples.
For every post-burn-in sample 𝝃t\boldsymbol{\xi}\_{t} we recorded two diagnostics: the cosine similarity to the nearest stored pattern, maxk⁡𝐦k⊤​𝝃t/(∥𝐦k∥​∥𝝃t∥)\max\_{k}\mathbf{m}\_{k}^{\top}\boldsymbol{\xi}\_{t}/(\lVert\mathbf{m}\_{k}\rVert\lVert\boldsymbol{\xi}\_{t}\rVert), and the Shannon entropy of the attention weights, H​(𝐩)=−∑kpk​log⁡pkH(\mathbf{p})=-\sum\_{k}p\_{k}\log p\_{k} where 𝐩=softmax⁡(β​𝐗⊤​𝝃t)\mathbf{p}=\operatorname{softmax}(\beta\mathbf{X}^{\top}\boldsymbol{\xi}\_{t}).

Both curves exhibited a smooth sigmoidal transition centered near β≈5​–​10\beta\approx 5\text{--}10.
At small β\beta the cosine similarity plateaued around 0.220.22, consistent with the expected inner product between a random unit vector and 16 stored patterns in 64 dimensions, while the entropy saturated at log⁡K≈2.77\log K\approx 2.77 nats, the uniform limit.
As β\beta increased through the transition region the attention weights concentrated on a single pattern: the entropy dropped sharply to zero by β≈25\beta\approx 25, and the cosine similarity rose to 0.9690.969 at β=1000\beta=1000.
The variance of both diagnostics peaked in the transition region, where the chain intermittently switched between pattern-aligned and exploratory states.
These results confirmed that β\beta acts as a continuous order parameter interpolating between disordered and ordered phases, in direct analogy to the paramagnetic-to-ferromagnetic transition in classical Hopfield networks [[1](#bib.bib21 "A learning algorithm for Boltzmann machines")]; the useful generation regime occupies intermediate β\beta values whose scale is problem-dependent and set by the SNR argument of Eq. ([11](#S5.E11 "In Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")).

We verified that Algorithm 1 converged to the correct Boltzmann target by running multiple independent chains on a small system where thorough mixing is feasible (Fig. [1](#S5.F1 "Figure 1 ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")b).
We stored K=4K=4 unit-norm patterns in 𝐗∈ℝ8×4\mathbf{X}\in\mathbb{R}^{8\times 4} and launched eight chains from different random initializations at β=5\beta=5 with step size α=0.01\alpha=0.01 and T=20,000T=20{,}000 iterations, discarding the first 5,0005{,}000 steps as burn-in.
All eight chains converged to the same stationary energy level; pooled post-burn-in energies closely matched a long-chain reference distribution (T=200,000T=200{,}000, burn-in 50,00050{,}000) with a small KS statistic, confirming convergence to the correct Boltzmann target rather than a single mode.

We mapped the joint effect of memory load and temperature on attention selectivity by constructing a phase diagram over the load ratio K/dK/d and inverse temperature β\beta (Fig. [3](#A4.F3 "Figure 3 ‣ Appendix D Load-Ratio Phase Diagram ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")).
We set d=64d=64 and swept K/dK/d across 10 values in [0.05, 2.0][0.05,\,2.0] and β\beta across 20 log-spaced values in [0.5, 100][0.5,\,100], running Algorithm 1 on five independent datasets per condition with T=10,000T=10{,}000 iterations, step size α=0.01\alpha=0.01, and a burn-in of 2,0002{,}000.
For each (β,K/d)(\beta,\,K/d) pair we reported the attention concentration C=1−H​(𝐚)/log⁡KC=1-H(\mathbf{a})/\log K, averaged over post-burn-in samples and datasets; C=1C=1 indicates perfect pattern-selective attention and C=0C=0 the uniform limit.
The resulting heatmap revealed a clear phase boundary (dashed C=0.5C=0.5 contour): a retrieval regime in the upper-left corner (high β\beta, low K/dK/d) where the sampler locked onto individual patterns, and a diffuse regime in the lower-right where attention spread uniformly across all memories.
The boundary shifted rightward as β\beta increased, indicating that higher inverse temperature extends reliable retrieval to larger memory loads, consistent with classical Hopfield capacity theory [[2](#bib.bib6 "Storing infinite numbers of patterns in a spin-glass model of neural networks")].

#### Image generation on MNIST.

The synthetic experiments above validated the sampler’s statistical properties on controlled data. We tested whether it could generate structured, recognizable outputs from real-world patterns and compared it against six baselines.
We selected K=100K=100 images of the digit “3” from the MNIST training set [[18](#bib.bib10 "Gradient-based learning applied to document recognition")], flattened each to a vector in ℝ784\mathbb{R}^{784}, and normalized to unit norm to form the memory matrix 𝐗∈ℝ784×100\mathbf{X}\in\mathbb{R}^{784\times 100} (load ratio K/d≈0.13K/d\approx 0.13).
Because the energy landscape at high β\beta is deeply multimodal, a single long chain can become trapped in one basin for the entire run.
We therefore launched 30 independent chains, each initialized near a different randomly chosen stored pattern with a small Gaussian perturbation (σinit=0.01\sigma\_{\mathrm{init}}=0.01).
Each chain ran Algorithm [1](#alg1 "Algorithm 1 ‣ 4.1 Stochastic Attention Update ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") at β=2000\beta=2000 with step size α=0.01\alpha=0.01 for T=5,000T=5{,}000 iterations; after discarding the first 2,0002{,}000 steps as burn-in, thinning every 100th iteration to obtain 30 post-burn-in snapshots, and sub-sampling 5 evenly spaced snapshots per chain, we retained 30×5=15030\times 5=150 generated images that collectively span 30 distinct energy basins.

The choice of β=2000\beta=2000 follows from the per-step signal-to-noise ratio,

|  |  |  |  |
| --- | --- | --- | --- |
|  | SNR=O​(α)2​α​d/β=α​β2​d,\mathrm{SNR}\;=\;\frac{O(\alpha)}{\sqrt{2\alpha d/\beta}}\;=\;\sqrt{\frac{\alpha\beta}{2d}}\,, |  | (11) |

where numerator and denominator are the gradient displacement and expected noise magnitude. The synthetic experiment placed the transition near SNR≈0.025\mathrm{SNR}\approx 0.025 (β≈5\beta\approx 5–1010, d=64d{=}64); inverting at d=784d{=}784 gives β≈100\beta\approx 100, and we set β=2000\beta=2000 (SNR=0.113\mathrm{SNR}=0.113, 4×4\times the transition) to operate well inside the structured regime.

To isolate the contribution of the energy-landscape structure, we compared against five baselines that used the same memory matrix: (i) *bootstrap resampling*, which draws a stored pattern uniformly at random; (ii) *Gaussian perturbation*, which selects a random stored pattern and adds isotropic noise 𝒩​(𝟎,σ2​𝐈)\mathcal{N}(\mathbf{0},\sigma^{2}\mathbf{I}) with σ\sigma matched to the sampler’s per-step noise scale 2​α/β\sqrt{2\alpha/\beta}; (iii) *random convex combination*, which outputs 𝐗𝐰\mathbf{X}\mathbf{w} for weights 𝐰∼Dirichlet​(1,…,1)\mathbf{w}\sim\mathrm{Dirichlet}(1,\dots,1); (iv) *GMM-PCA*, which projects the KK patterns onto the top-5050 PCA components, fits a 1010-component diagonal-covariance GMM via EM, and draws samples from the learned distribution (full specification in Appendix [I.1](#A9.SS1 "I.1 GMM-PCA ‣ Appendix I Baseline Method Specifications ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")); (v) *VAE* (latent dim 8, encoder 784→\to256→\to128→μ/log⁡σ2\to\mu/\log\sigma^{2}, decoder symmetric), trained for 4,000 epochs on the same K=100K{=}100 patterns with two-phase training to avoid posterior collapse, samples from 𝒩​(𝟎,𝐈)\mathcal{N}(\mathbf{0},\mathbf{I}) (full specification in Appendix [I.2](#A9.SS2 "I.2 Variational Autoencoder ‣ Appendix I Baseline Method Specifications ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")); and (vi) *MALA* (Metropolis-Adjusted Langevin Algorithm), which uses exactly the same Langevin proposal as Algorithm [1](#alg1 "Algorithm 1 ‣ 4.1 Stochastic Attention Update ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") but adds a Metropolis–Hastings accept/reject correction to eliminate discretization bias, run with the identical multi-chain protocol.
For each method we generated 150 samples and evaluated three metrics, novelty 𝒩\mathcal{N}, diversity 𝒟¯\bar{\mathcal{D}}, and mean energy E¯\bar{E}, defined as:

|  |  |  |
| --- | --- | --- |
|  | 𝒩​(𝝃^)=1−maxk⁡cos⁡(𝝃^,𝐦k),𝒟¯=2S​(S−1)​∑i<j(1−cos⁡(𝝃^i,𝝃^j)),E¯=1S​∑i=1SE​(𝝃^i),\displaystyle\mathcal{N}(\hat{\boldsymbol{\xi}})=1-\max\_{k}\cos\!\bigl(\hat{\boldsymbol{\xi}},\,\mathbf{m}\_{k}\bigr),\qquad\bar{\mathcal{D}}=\frac{2}{S(S{-}1)}\!\sum\_{i<j}\bigl(1-\cos(\hat{\boldsymbol{\xi}}\_{i},\hat{\boldsymbol{\xi}}\_{j})\bigr),\qquad\bar{E}=\frac{1}{S}\sum\_{i=1}^{S}E\!\bigl(\hat{\boldsymbol{\xi}}\_{i}\bigr), |  |

where cos⁡(𝐱,𝐲)=𝐱⊤​𝐲/(∥𝐱∥​∥𝐲∥)\cos(\mathbf{x},\mathbf{y})=\mathbf{x}^{\top}\mathbf{y}/(\lVert\mathbf{x}\rVert\,\lVert\mathbf{y}\rVert) denotes cosine similarity.
Novelty 𝒩\mathcal{N} measures departure from the nearest stored pattern (higher is more novel). Diversity 𝒟¯\bar{\mathcal{D}} is the mean pairwise cosine distance among generated samples (higher is more diverse). The mean Hopfield energy E¯\bar{E} measures proximity to the memory manifold (lower indicates more structured outputs).

Table 1: Quantitative comparison on MNIST digit “3” (K=100K=100, d=784d=784). 𝒩\mathcal{N} and 𝒟¯\bar{\mathcal{D}} are higher-is-better (↑\uparrow); E¯\bar{E} is lower-is-better (↓\downarrow). Values are mean ±\pm SE across 30 chains. Two SA rows demonstrate the temperature knob: β=2000\beta{=}2000 (SNR=0.113\mathrm{SNR}{=}0.113, structured retrieval) and β=200\beta{=}200 (SNR=0.036\mathrm{SNR}{=}0.036, generation). †Energy is positive at β=200\beta{=}200 because samples explore off the attractor manifold.

| Method | 𝒩\mathcal{N} ↑\uparrow | 𝒟¯\bar{\mathcal{D}} ↑\uparrow | E¯\bar{E} ↓\downarrow |
| --- | --- | --- | --- |
| Bootstrap (replay) | 0.000±0.0000.000\pm 0.000 | 0.459±0.0110.459\pm 0.011 | −0.500±0.000-0.500\pm 0.000 |
| Gaussian perturbation | 0.004±0.0000.004\pm 0.000 | 0.450±0.0130.450\pm 0.013 | −0.496±0.000-0.496\pm 0.000 |
| Random convex combination | 0.092±0.0000.092\pm 0.000 | 0.008±0.0000.008\pm 0.000 | −0.399±0.000-0.399\pm 0.000 |
| GMM-PCA (r=50r{=}50, C=10C{=}10) | 0.198±0.0040.198\pm 0.004 | 0.419±0.0110.419\pm 0.011 | −0.303±0.005-0.303\pm 0.005 |
| VAE (latent=8{=}8) | 0.214±0.0050.214\pm 0.005 | 0.441±0.0080.441\pm 0.008 | −0.286±0.005-0.286\pm 0.005 |
| MALA (β=2000\beta{=}2000) | 0.151±0.0010.151\pm 0.001 | 0.598±0.0010.598\pm 0.001 | −0.305±0.001-0.305\pm 0.001 |
| SA (β=2000\beta{=}2000, retrieval) | 0.152±0.0010.152\pm 0.001 | 0.600±0.0010.600\pm 0.001 | −0.303±0.001-0.303\pm 0.001 |
| SA (β=200\beta{=}200, generation) | 0.548±0.002\mathbf{0.548\pm 0.002} | 0.885±0.002\mathbf{0.885\pm 0.002} | 1.467±0.008†1.467\pm 0.008^{\dagger} |



![Refer to caption](2603.06875v1/figs/Fig_mnist_grid_bootstrap.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_grid_gaussian.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_grid_convex.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_grid_mala.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_grid_sa.png)

(a) Bootstrap (b) Gaussian (c) Convex (d) MALA (e) Ours

Figure 2: Generated MNIST digit “3” samples (4×44\times 4 grids) at β=2000\beta{=}2000 (SNR=0.113\mathrm{SNR}{=}0.113, structured-retrieval regime). Bootstrap outputs are exact copies of stored images. Gaussian perturbation adds unstructured noise. Random convex combinations produce blurry averages. MALA and our ULA-based stochastic attention sampler (β\beta controls the operating mode: β=2000\beta{=}2000 for structured retrieval, β=200\beta{=}200 for generation) produce visually indistinguishable diverse, structured digits, confirming that the Metropolis correction is unnecessary at step size α=0.01\alpha{=}0.01.

Table [1](#S5.T1 "Table 1 ‣ Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") and Figure [2](#S5.F2 "Figure 2 ‣ Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") summarized the results. Each non-Langevin baseline failed on at least one axis: bootstrap by construction (𝒩=0\mathcal{N}{=}0); Gaussian perturbation by negligible noise (σ≈0.003\sigma{\approx}0.003, indistinguishable from bootstrap); and random convex combination by mode collapse (𝒟¯=0.008\bar{\mathcal{D}}{=}0.008). Among static baselines, the VAE (latent dim 8, trained on the same K=100K{=}100 patterns) is the strongest: 𝒩=0.214±0.005\mathcal{N}{=}0.214\pm 0.005, 𝒟¯=0.441±0.008\bar{\mathcal{D}}{=}0.441\pm 0.008, surpassing GMM-PCA on both axes. At β=200\beta{=}200 (SNR==0.036, the generation regime), SA dominates every baseline, including the best learned model (VAE), on both generation metrics simultaneously: novelty 0.548±0.0020.548\pm 0.002 (2.6×2.6{\times} VAE, 2.8×2.8{\times} GMM-PCA), diversity 0.885±0.0020.885\pm 0.002 (2.0×2.0{\times} VAE, 2.1×2.1{\times} GMM-PCA); energy rises above zero as samples explore off the attractor manifold (see †). MALA’s 99.2% acceptance rate at both β\beta values confirms negligible ULA bias across regimes. The SNR transition band (0.020.02–0.030.03) thus delimits two qualitatively distinct regimes in the same algorithm: *structured retrieval* (β=2000\beta{=}2000, crisp digits near stored patterns) and *genuine generation* (β=200\beta{=}200, blurry-but-recognizable novel digits). To verify that the high diversity at β=200\beta{=}200 reflects genuine basin-crossing rather than multi-chain initialization, we ran a single long chain (T=50,000T{=}50{,}000) from a fixed seed; single-chain diversity reached 0.7960.796, exceeding the 30-chain β=2000\beta{=}2000 value of 0.6000.600 (Table [5](#A6.T5 "Table 5 ‣ Appendix F Single-Chain Diversity Analysis ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."), Appendix [F](#A6 "Appendix F Single-Chain Diversity Analysis ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")).

Appendix [E](#A5 "Appendix E Multi-Digit MNIST Generalization ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") confirmed the same ranking on digits “1” and “8” (SA: 𝒩≈0.152\mathcal{N}{\approx}0.152–0.1530.153, 𝒟¯≈0.557\bar{\mathcal{D}}{\approx}0.557–0.5910.591; VAE: 𝒩≈0.180\mathcal{N}{\approx}0.180–0.2090.209, 𝒟¯≈0.397\bar{\mathcal{D}}{\approx}0.397–0.4080.408; MALA acceptance 99.2%): the VAE remains the strongest non-Langevin baseline on novelty but is far below both Langevin methods on diversity across all digit classes. Appendix [G](#A7 "Appendix G Financial Log-Return Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") used S&P 500 log-returns (d=424d{=}424, K=2,766K{=}2{,}766) to characterize the novelty–fidelity trade-off on real data: SA achieved novelty 0.768±0.0010.768\pm 0.001 (bootstrap: 0.0000.000) while bootstrap led on marginal fidelity (99.3%99.3\% vs. 64.2%64.2\% KS pass); volatility clustering was not reproduced, a principled consequence of fixed-β\beta equilibrium sampling. Appendix [H](#A8 "Appendix H Simpsons Character Face Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") scales to face images at d=4,096d{=}4{,}096: the SNR rule prescribes β=10,000\beta{=}10{,}000; SA achieves novelty 0.159±0.0000.159\pm 0.000 and diversity 0.293±0.0010.293\pm 0.001, with ranking identical to MNIST across a 5.2×5.2{\times} dimension increase.

## 6 Discussion and Conclusion

The experiments validated the core claim: Langevin dynamics on the modern Hopfield energy converts deterministic attention into a principled stochastic sampler governed by a single temperature parameter.
The temperature spectrum (Fig. [1](#S5.F1 "Figure 1 ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")a) exhibited a smooth phase transition between retrieval and generation, the continuous analogue of the classical Hopfield/Boltzmann duality [[1](#bib.bib21 "A learning algorithm for Boltzmann machines")] lifted to continuous states and Langevin dynamics. The convergence experiment (Fig. [1](#S5.F1 "Figure 1 ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")b) confirmed that Algorithm 1 reached the correct Boltzmann target, consistent with ULA theory [[7](#bib.bib8 "Nonasymptotic convergence analysis for the unadjusted Langevin algorithm")]. The load-ratio sweep (Fig. [3](#A4.F3 "Figure 3 ‣ Appendix D Load-Ratio Phase Diagram ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) showed that generation quality degraded gracefully as K/dK/d increased, providing empirical evidence linking modern Hopfield capacity to generation quality. The MNIST experiment (Table [1](#S5.T1 "Table 1 ‣ Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."), Fig. [2](#S5.F2 "Figure 2 ‣ Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) demonstrated that these properties carried over to real images: the sampler generated novel, low-energy digit images that no static baseline could approach, including a VAE trained on the same K=100K{=}100 patterns (𝒩=0.214\mathcal{N}{=}0.214, 𝒟¯=0.441\bar{\mathcal{D}}{=}0.441, the strongest non-Langevin result): at β=200\beta{=}200, SA led the VAE by 2.6×2.6{\times} on novelty and 2.0×2.0{\times} on diversity. SA matched the Metropolis-corrected MALA baseline, confirming ULA’s discretization bias was negligible at α=0.01\alpha{=}0.01. Appendices [G](#A7 "Appendix G Financial Log-Return Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") and [H](#A8 "Appendix H Simpsons Character Face Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") extended these results to S&P 500 log-returns (d=424d{=}424) and face images (d=4,096d{=}4{,}096), confirming the SNR rule and the novelty–fidelity trade-off across a 5.2×5.2{\times} dimension range.

In summary, stochastic attention reuses the same primitive operations as a standard attention head and requires no learned score network, no training loop, and no contrastive objective. The analytic structure of the Hopfield energy (smoothness, dissipativity, and an exact closed-form gradient) provides convergence guarantees that generic energy-based samplers cannot offer without additional assumptions. Across all four experimental domains (d∈{64, 784, 424, 4,096}d\in\{64,\,784,\,424,\,4{,}096\}), the transition from structured retrieval to diffuse generation consistently occurs near SNR=α​β/2​d≈0.02\mathrm{SNR}=\sqrt{\alpha\beta/2d}\approx 0.02–0.030.03, giving a dimension-independent rule for targeting β\beta: set β=SNRtarget2⋅2​d/α\beta=\mathrm{SNR}\_{\mathrm{target}}^{2}\cdot 2d/\alpha.

#### Limitations.

The ULA discretization introduces bias scaling with α\alpha; our MALA comparison (Table [1](#S5.T1 "Table 1 ‣ Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) shows a 99.2% acceptance rate at α=0.01\alpha{=}0.01, confirming negligible bias at this step size. At larger α\alpha, MALA (Algorithm [2](#alg2 "Algorithm 2 ‣ Appendix C MALA Variant of Stochastic Attention ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."), Appendix [C](#A3 "Appendix C MALA Variant of Stochastic Attention ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) is the preferred variant. Mixing time grows with both β\beta and K/dK/d, and quantitative scaling laws remain to be established. Each step costs 𝒪​(N​K)\mathcal{O}(NK) (two matrix–vector products plus a softmax), identical to a single attention head; for N=784N{=}784, K=100K{=}100 the full 30-chain experiment completes in under 10 minutes on a laptop CPU. The method also requires 𝐗\mathbf{X} to be known and fixed at sampling time; streaming or latent memory settings would require extension. We consider only single-head attention over a flat memory; extension to multi-head attention, hierarchical memories, or full encoder-decoder transformers is future work.

## Acknowledgments

This work grew out of the CHEME-5820 Machine Learning and Artificial Intelligence Methods for Engineers course at Cornell University; the central idea arose while preparing a lecture on Boltzmann machines immediately after covering modern Hopfield networks. Financial market data used in Appendix [G](#A7 "Appendix G Financial Log-Return Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") were obtained from Polygon.io.

## References

* [1]
  D. H. Ackley, G. E. Hinton, and T. J. Sejnowski (1985)
  A learning algorithm for Boltzmann machines.
  Cognitive Science 9 (1),  pp. 147–169.
  External Links: [Document](https://dx.doi.org/10.1207/s15516709cog0901%5F7)
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§2](#S2.SS0.SSS0.Px1.p3.1 "Hopfield networks and associative memory. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§5](#S5.SS0.SSS0.Px1.p3.10 "Temperature spectrum, Convergence diagnostics and Load Ratio using synthetic data. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§6](#S6.p1.11 "6 Discussion and Conclusion ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [2]
  D. J. Amit, H. Gutfreund, and H. Sompolinsky (1985)
  Storing infinite numbers of patterns in a spin-glass model of neural networks.
  Physical Review Letters 55 (14),  pp. 1530–1533.
  External Links: [Document](https://dx.doi.org/10.1103/PhysRevLett.55.1530)
  Cited by: [§2](#S2.SS0.SSS0.Px1.p1.11 "Hopfield networks and associative memory. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§3](#S3.SS0.SSS0.Px2.p1.5 "The energy landscape beneath attention. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§5](#S5.SS0.SSS0.Px1.p1.7 "Temperature spectrum, Convergence diagnostics and Load Ratio using synthetic data. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§5](#S5.SS0.SSS0.Px1.p5.18 "Temperature spectrum, Convergence diagnostics and Load Ratio using synthetic data. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [3]
  R. Cont (2001)
  Empirical properties of asset returns: stylized facts and statistical issues.
  Quantitative Finance 1 (2),  pp. 223–236.
  Cited by: [§G.3](#A7.SS3.SSS0.Px3.p2.3 "Stylized Fact 3: Volatility clustering. ‣ G.3 Sequential Generation and Temporal Properties ‣ Appendix G Financial Log-Return Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§G.3](#A7.SS3.SSS0.Px4.p1.6 "Summary. ‣ G.3 Sequential Generation and Temporal Properties ‣ Appendix G Financial Log-Return Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§G.3](#A7.SS3.p1.1 "G.3 Sequential Generation and Temporal Properties ‣ Appendix G Financial Log-Return Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [4]
  A. S. Dalalyan (2017)
  Theoretical guarantees for approximate sampling from a smooth and log-concave density.
  Journal of the Royal Statistical Society: Series B (Statistical Methodology) 79 (3),  pp. 651–676.
  External Links: [Document](https://dx.doi.org/10.1111/rssb.12183)
  Cited by: [Corollary 2](#Thmtheorem2.p1.12.12 "Corollary 2. ‣ 4.2 Properties and Limiting Behavior ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [5]
  A. P. Dempster, N. M. Laird, and D. B. Rubin (1977)
  Maximum likelihood from incomplete data via the EM algorithm.
  Journal of the Royal Statistical Society: Series B 39 (1),  pp. 1–38.
  Cited by: [§I.1](#A9.SS1.SSS0.Px2.p1.2 "Gaussian mixture model. ‣ I.1 GMM-PCA ‣ Appendix I Baseline Method Specifications ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [6]
  Y. Deng, Y. Kim, J. Chiu, D. Guo, and A. M. Rush (2018)
  Latent alignment and variational attention.
  In Advances in Neural Information Processing Systems,
  Vol. 31.
  Cited by: [§2](#S2.SS0.SSS0.Px2.p3.1 "Energy-based, score-based and diffusion models. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [7]
  A. Durmus and É. Moulines (2017)
  Nonasymptotic convergence analysis for the unadjusted Langevin algorithm.
  The Annals of Applied Probability 27 (3),  pp. 1551–1587.
  External Links: [Document](https://dx.doi.org/10.1214/16-AAP1238)
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§3](#S3.SS0.SSS0.Px4.p2.11 "From minimization to sampling. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§4.2](#S4.SS2.p2.8 "4.2 Properties and Limiting Behavior ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§6](#S6.p1.11 "6 Discussion and Conclusion ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [Corollary 2](#Thmtheorem2.p1.12.12 "Corollary 2. ‣ 4.2 Properties and Limiting Behavior ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [8]
  V. Folli, M. Leonetti, and G. Ruocco (2017)
  On the maximum storage capacity of the Hopfield model.
  Frontiers in Computational Neuroscience 10,  pp. 144.
  External Links: [Document](https://dx.doi.org/10.3389/fncom.2016.00144)
  Cited by: [§2](#S2.SS0.SSS0.Px1.p1.11 "Hopfield networks and associative memory. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§5](#S5.SS0.SSS0.Px1.p1.7 "Temperature spectrum, Convergence diagnostics and Load Ratio using synthetic data. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [9]
  I. Higgins, L. Matthey, A. Pal, C. Burgess, X. Glorot, M. Botvinick, S. Mohamed, and A. Lerchner (2017)
  Beta-VAE: Learning basic visual concepts with a constrained variational framework.
  In International Conference on Learning Representations,
  Cited by: [§I.2](#A9.SS2.SSS0.Px2.p1.1 "Objective. ‣ I.2 Variational Autoencoder ‣ Appendix I Baseline Method Specifications ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [10]
  G. E. Hinton (2002)
  Training products of experts by minimizing contrastive divergence.
  Neural Computation 14 (8),  pp. 1771–1800.
  External Links: [Document](https://dx.doi.org/10.1162/089976602760128018)
  Cited by: [§2](#S2.SS0.SSS0.Px2.p1.3 "Energy-based, score-based and diffusion models. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [11]
  J. Ho, A. Jain, and P. Abbeel (2020)
  Denoising diffusion probabilistic models.
  In Advances in Neural Information Processing Systems,
  Vol. 33,  pp. 6840–6851.
  Cited by: [§2](#S2.SS0.SSS0.Px2.p2.3 "Energy-based, score-based and diffusion models. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [12]
  B. Hoover, Y. Liang, B. Pham, R. Panda, H. Strobelt, D. H. Chau, M. J. Zaki, and D. Krotov (2024)
  Energy transformer.
  In Advances in Neural Information Processing Systems,
  Vol. 36.
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§2](#S2.SS0.SSS0.Px2.p1.3 "Energy-based, score-based and diffusion models. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [13]
  J. J. Hopfield (1982)
  Neural networks and physical systems with emergent collective computational abilities.
  Proceedings of the National Academy of Sciences 79 (8),  pp. 2554–2558.
  External Links: [Document](https://dx.doi.org/10.1073/pnas.79.8.2554)
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§2](#S2.SS0.SSS0.Px1.p1.11 "Hopfield networks and associative memory. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§3](#S3.SS0.SSS0.Px2.p1.2 "The energy landscape beneath attention. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [14]
  A. Hyvärinen (2005)
  Estimation of non-normalized statistical models by score matching.
  Journal of Machine Learning Research 6,  pp. 695–709.
  Cited by: [§2](#S2.SS0.SSS0.Px2.p1.3 "Energy-based, score-based and diffusion models. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [15]
  D. P. Kingma and J. Ba (2014)
  Adam: A method for stochastic optimization.
  arXiv preprint arXiv:1412.6980.
  Cited by: [§I.2](#A9.SS2.SSS0.Px4.p1.7 "Optimization and sampling. ‣ I.2 Variational Autoencoder ‣ Appendix I Baseline Method Specifications ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [16]
  D. Krotov and J. J. Hopfield (2016)
  Dense associative memory for pattern recognition.
  In Advances in Neural Information Processing Systems,
  Vol. 29.
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§2](#S2.SS0.SSS0.Px1.p2.3 "Hopfield networks and associative memory. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§2](#S2.SS0.SSS0.Px1.p3.1 "Hopfield networks and associative memory. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [17]
  D. Krotov and J. Hopfield (2021)
  Large associative memory problem in neurobiology and machine learning.
  In International Conference on Learning Representations (ICLR),
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [18]
  Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner (1998)
  Gradient-based learning applied to document recognition.
  Proceedings of the IEEE 86 (11),  pp. 2278–2324.
  External Links: [Document](https://dx.doi.org/10.1109/5.726791)
  Cited by: [§5](#S5.SS0.SSS0.Px2.p1.11 "Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [19]
  Y. LeCun, S. Chopra, R. Hadsell, M. Ranzato, and F. J. Huang (2006)
  A tutorial on energy-based learning.
  In Predicting Structured Data, G. Bakir, T. Hofmann, B. Schölkopf, A. J. Smola, B. Taskar, and S.V.N. Vishwanathan (Eds.),
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§2](#S2.SS0.SSS0.Px2.p1.3 "Energy-based, score-based and diffusion models. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [20]
  J. Lucas, G. Tucker, R. Grosse, and M. Norouzi (2019)
  Don’t blame the ELBO! A linear VAE perspective on posterior collapse.
  In Advances in Neural Information Processing Systems,
  Vol. 32.
  Cited by: [§I.2](#A9.SS2.SSS0.Px3.p1.6 "Two-phase training protocol. ‣ I.2 Variational Autoencoder ‣ Appendix I Baseline Method Specifications ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [21]
  H. Ramsauer, B. Schäfl, J. Lehner, P. Seidl, M. Widrich, T. Adler, L. Gruber, M. Holzleitner, M. Pavlović, G. K. Sandve, V. Greiff, D. Kreil, M. Kopp, G. Klambauer, J. Brandstetter, and S. Hochreiter (2021)
  Hopfield networks is all you need.
  In International Conference on Learning Representations (ICLR),
  Cited by: [Appendix B](#A2.SS0.SSS0.Px1.p1.3 "Hessian computation. ‣ Appendix B Proof of Proposition 1 ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§G.1](#A7.SS1.p1.11 "G.1 Data and Memory Construction ‣ Appendix G Financial Log-Return Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§1](#S1.p2.1 "1 Introduction ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§2](#S2.SS0.SSS0.Px1.p2.3 "Hopfield networks and associative memory. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§3](#S3.SS0.SSS0.Px2.p2.3 "The energy landscape beneath attention. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§3](#S3.SS0.SSS0.Px2.p2.9 "The energy landscape beneath attention. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§3](#S3.SS0.SSS0.Px2.p3.3 "The energy landscape beneath attention. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§3](#S3.SS0.SSS0.Px3.p1.4 "The bridge. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [22]
  D. J. Rezende and S. Mohamed (2015)
  Variational inference with normalizing flows.
  In Proceedings of the 32nd International Conference on Machine Learning,
   pp. 1530–1538.
  Cited by: [§2](#S2.SS0.SSS0.Px2.p3.1 "Energy-based, score-based and diffusion models. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [23]
  G. O. Roberts and R. L. Tweedie (1996)
  Exponential convergence of Langevin distributions and their discrete approximations.
  Bernoulli 2 (4),  pp. 341–363.
  External Links: [Document](https://dx.doi.org/10.2307/3318418)
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§3](#S3.SS0.SSS0.Px4.p1.13 "From minimization to sampling. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§3](#S3.SS0.SSS0.Px4.p2.1 "From minimization to sampling. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§4.2](#S4.SS2.SSS0.Px1.p1.7 "Scope of the convergence guarantee. ‣ 4.2 Properties and Limiting Behavior ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [Corollary 2](#Thmtheorem2.p1.12.12 "Corollary 2. ‣ 4.2 Properties and Limiting Behavior ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [24]
  T. J. Sejnowski (1986)
  Higher-order Boltzmann machines.
  In AIP Conference Proceedings,
  Vol. 151,  pp. 398–403.
  Cited by: [§2](#S2.SS0.SSS0.Px1.p3.1 "Hopfield networks and associative memory. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [25]
  J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan, and S. Ganguli (2015)
  Deep unsupervised learning using nonequilibrium thermodynamics.
  In Proceedings of the 32nd International Conference on Machine Learning (ICML),
   pp. 2256–2265.
  Cited by: [§2](#S2.SS0.SSS0.Px2.p2.3 "Energy-based, score-based and diffusion models. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [26]
  Y. Song and S. Ermon (2019)
  Generative modeling by estimating gradients of the data distribution.
  In Advances in Neural Information Processing Systems,
  Vol. 32.
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§2](#S2.SS0.SSS0.Px2.p2.3 "Energy-based, score-based and diffusion models. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [27]
  Y. Song and D. P. Kingma (2021)
  How to train your energy-based models.
  arXiv preprint arXiv:2101.03288.
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§2](#S2.SS0.SSS0.Px2.p1.3 "Energy-based, score-based and diffusion models. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [28]
  Y. Song, J. Sohl-Dickstein, D. P. Kingma, A. Kumar, S. Ermon, and B. Poole (2021)
  Score-based generative modeling through stochastic differential equations.
  In International Conference on Learning Representations (ICLR),
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§2](#S2.SS0.SSS0.Px2.p2.3 "Energy-based, score-based and diffusion models. ‣ 2 Related Work ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [29]
  A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin (2017)
  Attention is all you need.
  In Advances in Neural Information Processing Systems,
  Vol. 30,  pp. 5998–6008.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§3](#S3.SS0.SSS0.Px1.p1.3 "Attention as deterministic retrieval. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").
* [30]
  M. Welling and Y. W. Teh (2011)
  Bayesian learning via stochastic gradient Langevin dynamics.
  In Proceedings of the 28th International Conference on Machine Learning (ICML),
   pp. 681–688.
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."),
  [§3](#S3.SS0.SSS0.Px4.p2.11 "From minimization to sampling. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").

## Appendix A Broader Impact Statement

This work is primarily methodological: it connects two well-studied mathematical frameworks (modern Hopfield networks and Langevin dynamics) to produce a stochastic attention mechanism. Because the method generates outputs that are structured combinations of stored memory patterns, it inherits the biases present in whatever memory matrix is supplied. Practitioners should therefore audit the stored patterns for representational harms before deploying the sampler in applications that affect individuals (e.g., image synthesis, recommendation). The training-free nature of the method lowers the barrier to misuse relative to large diffusion models, but also limits expressiveness to the convex hull of the memory, reducing the risk of generating entirely novel harmful content. We do not foresee direct negative societal consequences beyond those common to all generative modeling research, and we encourage responsible use.

## Appendix B Proof of Proposition [1](#Thmtheorem1 "Proposition 1. ‣ 4.2 Properties and Limiting Behavior ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")

We prove the two regularity properties of the modern Hopfield energy EE defined in ([3](#S3.E3 "In The energy landscape beneath attention. ‣ 3 Background ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")). Write 𝐩​(𝝃)=softmax⁡(β​𝐗⊤​𝝃)∈ℝK\mathbf{p}(\boldsymbol{\xi})=\operatorname{softmax}(\beta\mathbf{X}^{\top}\boldsymbol{\xi})\in\mathbb{R}^{K} for the attention weight vector at state 𝝃\boldsymbol{\xi}, and recall the retrieval map 𝐓​(𝝃)=𝐗𝐩​(𝝃)\mathbf{T}(\boldsymbol{\xi})=\mathbf{X}\mathbf{p}(\boldsymbol{\xi}).

#### Hessian computation.

The gradient is ∇E​(𝝃)=𝝃−𝐓​(𝝃)\nabla E(\boldsymbol{\xi})=\boldsymbol{\xi}-\mathbf{T}(\boldsymbol{\xi}) [[21](#bib.bib3 "Hopfield networks is all you need")]. To obtain the Hessian we differentiate the retrieval map. Let 𝐳=β​𝐗⊤​𝝃∈ℝK\mathbf{z}=\beta\mathbf{X}^{\top}\boldsymbol{\xi}\in\mathbb{R}^{K} denote the pre-softmax logits. The Jacobian of the softmax is the K×KK\times K matrix

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂𝐩∂𝐳=diag(𝐩)−𝐩𝐩⊤=:𝐒(𝐩),\frac{\partial\mathbf{p}}{\partial\mathbf{z}}=\operatorname{diag}(\mathbf{p})-\mathbf{p}\mathbf{p}^{\top}=:\mathbf{S}(\mathbf{p}), |  | (12) |

which is the covariance matrix of a categorical distribution with probabilities 𝐩\mathbf{p}. By the chain rule (∂𝐳/∂𝝃=β​𝐗⊤\partial\mathbf{z}/\partial\boldsymbol{\xi}=\beta\mathbf{X}^{\top}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇2E​(𝝃)=𝐈N−β​𝐗​𝐒​(𝐩​(𝝃))​𝐗⊤.\nabla^{2}E(\boldsymbol{\xi})=\mathbf{I}\_{N}-\beta\,\mathbf{X}\,\mathbf{S}\bigl(\mathbf{p}(\boldsymbol{\xi})\bigr)\,\mathbf{X}^{\top}. |  | (13) |

#### Part (i): Lipschitz gradient.

The Lipschitz constant of ∇E\nabla E equals sup𝝃‖∇2E​(𝝃)‖op\sup\_{\boldsymbol{\xi}}\|\nabla^{2}E(\boldsymbol{\xi})\|\_{\mathrm{op}}. Because 𝐒​(𝐩)\mathbf{S}(\mathbf{p}) is a covariance matrix it is positive semidefinite, so β​𝐗𝐒𝐗⊤⪰𝟎\beta\mathbf{X}\mathbf{S}\mathbf{X}^{\top}\succeq\mathbf{0}. By the triangle inequality for the spectral norm,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖∇2E​(𝝃)‖op≤‖𝐈N‖op+β​‖𝐗​𝐒​(𝐩)​𝐗⊤‖op≤ 1+β​σmax2​‖𝐒​(𝐩)‖op,\|\nabla^{2}E(\boldsymbol{\xi})\|\_{\mathrm{op}}\;\leq\;\|\mathbf{I}\_{N}\|\_{\mathrm{op}}+\beta\,\|\mathbf{X}\,\mathbf{S}(\mathbf{p})\,\mathbf{X}^{\top}\|\_{\mathrm{op}}\;\leq\;1+\beta\,\sigma\_{\max}^{2}\,\|\mathbf{S}(\mathbf{p})\|\_{\mathrm{op}}, |  | (14) |

where the second step uses submultiplicativity of the spectral norm: ‖𝐀𝐁𝐂‖op≤‖𝐀‖op​‖𝐁‖op​‖𝐂‖op\|\mathbf{A}\mathbf{B}\mathbf{C}\|\_{\mathrm{op}}\leq\|\mathbf{A}\|\_{\mathrm{op}}\|\mathbf{B}\|\_{\mathrm{op}}\|\mathbf{C}\|\_{\mathrm{op}}.

It remains to bound ‖𝐒​(𝐩)‖op\|\mathbf{S}(\mathbf{p})\|\_{\mathrm{op}}. For any unit vector 𝐯∈ℝK\mathbf{v}\in\mathbb{R}^{K},

|  |  |  |
| --- | --- | --- |
|  | 𝐯⊤​𝐒​(𝐩)​𝐯=∑ipi​vi2−(∑ipi​vi)2=Var𝐩⁡(V),\displaystyle\mathbf{v}^{\top}\mathbf{S}(\mathbf{p})\mathbf{v}=\sum\_{i}p\_{i}v\_{i}^{2}-\Bigl(\sum\_{i}p\_{i}v\_{i}\Bigr)^{\!2}=\operatorname{Var}\_{\mathbf{p}}(V), |  |

where VV is the random variable taking value viv\_{i} with probability pip\_{i}. By Popoviciu’s variance inequality, Var⁡(V)≤(vmax−vmin)2/4\operatorname{Var}(V)\leq(v\_{\max}-v\_{\min})^{2}/4. Under the constraint ‖𝐯‖2=1\|\mathbf{v}\|\_{2}=1, the difference vmax−vminv\_{\max}-v\_{\min} satisfies

|  |  |  |
| --- | --- | --- |
|  | (vmax−vmin)2≤(|vmax|+|vmin|)2≤ 2​(vmax2+vmin2)≤ 2​‖𝐯‖22=2,\displaystyle(v\_{\max}-v\_{\min})^{2}\;\leq\;(|v\_{\max}|+|v\_{\min}|)^{2}\;\leq\;2(v\_{\max}^{2}+v\_{\min}^{2})\;\leq\;2\|\mathbf{v}\|\_{2}^{2}=2, |  |

where the second step is the Cauchy–Schwarz (QM-AM) inequality (a+b)2≤2​(a2+b2)(a+b)^{2}\leq 2(a^{2}+b^{2}) for a,b≥0a,b\geq 0. Therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝐒​(𝐩)‖op=sup‖𝐯‖=1Var𝐩⁡(V)≤24=12,\|\mathbf{S}(\mathbf{p})\|\_{\mathrm{op}}=\sup\_{\|\mathbf{v}\|=1}\operatorname{Var}\_{\mathbf{p}}(V)\;\leq\;\frac{2}{4}=\frac{1}{2}, |  | (15) |

and this bound is tight: equality holds when K≥2K\geq 2 with 𝐩=(12,12,0,…,0)\mathbf{p}=(\tfrac{1}{2},\tfrac{1}{2},0,\dots,0) and 𝐯=(12,−12,0,…,0)\mathbf{v}=(\tfrac{1}{\sqrt{2}},-\tfrac{1}{\sqrt{2}},0,\dots,0).

Substituting ([15](#A2.E15 "In Part (i): Lipschitz gradient. ‣ Appendix B Proof of Proposition 1 ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) into ([14](#A2.E14 "In Part (i): Lipschitz gradient. ‣ Appendix B Proof of Proposition 1 ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) yields

|  |  |  |
| --- | --- | --- |
|  | sup𝝃∥∇2E(𝝃)∥op≤ 1+β​σmax22=:L.\displaystyle\sup\_{\boldsymbol{\xi}}\|\nabla^{2}E(\boldsymbol{\xi})\|\_{\mathrm{op}}\;\leq\;1+\frac{\beta\,\sigma\_{\max}^{2}}{2}=:L. |  |

#### Part (ii): Dissipativity.

Expanding the inner product,

|  |  |  |
| --- | --- | --- |
|  | ⟨∇E​(𝝃),𝝃⟩=‖𝝃‖22−⟨𝐓​(𝝃),𝝃⟩.\displaystyle\langle\nabla E(\boldsymbol{\xi}),\,\boldsymbol{\xi}\rangle=\|\boldsymbol{\xi}\|\_{2}^{2}-\langle\mathbf{T}(\boldsymbol{\xi}),\,\boldsymbol{\xi}\rangle. |  |

The retrieval map 𝐓​(𝝃)=𝐗𝐩=∑kpk​𝐦k\mathbf{T}(\boldsymbol{\xi})=\mathbf{X}\mathbf{p}=\sum\_{k}p\_{k}\mathbf{m}\_{k} is a convex combination of stored patterns, so by the triangle inequality

|  |  |  |
| --- | --- | --- |
|  | ‖𝐓​(𝝃)‖2=‖∑kpk​𝐦k‖2≤∑kpk​‖𝐦k‖2≤M,\displaystyle\|\mathbf{T}(\boldsymbol{\xi})\|\_{2}=\Bigl\|\sum\_{k}p\_{k}\mathbf{m}\_{k}\Bigr\|\_{2}\leq\sum\_{k}p\_{k}\|\mathbf{m}\_{k}\|\_{2}\leq M, |  |

where M=maxk⁡‖𝐦k‖2M=\max\_{k}\|\mathbf{m}\_{k}\|\_{2} and ∑kpk=1\sum\_{k}p\_{k}=1. By the Cauchy–Schwarz inequality,

|  |  |  |
| --- | --- | --- |
|  | |⟨𝐓​(𝝃),𝝃⟩|≤‖𝐓​(𝝃)‖2​‖𝝃‖2≤M​‖𝝃‖2.\displaystyle|\langle\mathbf{T}(\boldsymbol{\xi}),\,\boldsymbol{\xi}\rangle|\leq\|\mathbf{T}(\boldsymbol{\xi})\|\_{2}\,\|\boldsymbol{\xi}\|\_{2}\leq M\|\boldsymbol{\xi}\|\_{2}. |  |

Applying Young’s inequality a​b≤a22+b22ab\leq\tfrac{a^{2}}{2}+\tfrac{b^{2}}{2} with a=Ma=M and b=‖𝝃‖2b=\|\boldsymbol{\xi}\|\_{2},

|  |  |  |
| --- | --- | --- |
|  | M​‖𝝃‖2≤M22+‖𝝃‖222.\displaystyle M\|\boldsymbol{\xi}\|\_{2}\;\leq\;\frac{M^{2}}{2}+\frac{\|\boldsymbol{\xi}\|\_{2}^{2}}{2}. |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | ⟨∇E​(𝝃),𝝃⟩≥‖𝝃‖22−M22−‖𝝃‖222=12​‖𝝃‖22−M22,\displaystyle\langle\nabla E(\boldsymbol{\xi}),\,\boldsymbol{\xi}\rangle\;\geq\;\|\boldsymbol{\xi}\|\_{2}^{2}-\frac{M^{2}}{2}-\frac{\|\boldsymbol{\xi}\|\_{2}^{2}}{2}=\frac{1}{2}\|\boldsymbol{\xi}\|\_{2}^{2}-\frac{M^{2}}{2}, |  |

which is the dissipativity condition (R2) with constants a=12a=\tfrac{1}{2} and b=M22b=\tfrac{M^{2}}{2}. ∎

#### Convexity threshold (Corollary [2](#Thmtheorem2 "Corollary 2. ‣ 4.2 Properties and Limiting Behavior ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")).

Since 𝐒​(𝐩)⪰𝟎\mathbf{S}(\mathbf{p})\succeq\mathbf{0}, the Hessian ([13](#A2.E13 "In Hessian computation. ‣ Appendix B Proof of Proposition 1 ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) satisfies ∇2E⪯𝐈\nabla^{2}E\preceq\mathbf{I} (the identity provides an upper bound on the eigenvalues). For the lower bound, β​𝐗𝐒𝐗⊤⪯β​σmax22​𝐈\beta\mathbf{X}\mathbf{S}\mathbf{X}^{\top}\preceq\tfrac{\beta\sigma\_{\max}^{2}}{2}\mathbf{I} by ([15](#A2.E15 "In Part (i): Lipschitz gradient. ‣ Appendix B Proof of Proposition 1 ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) and submultiplicativity, so

|  |  |  |
| --- | --- | --- |
|  | ∇2E​(𝝃)⪰(1−β​σmax22)​𝐈.\displaystyle\nabla^{2}E(\boldsymbol{\xi})\;\succeq\;\Bigl(1-\frac{\beta\sigma\_{\max}^{2}}{2}\Bigr)\mathbf{I}. |  |

When β​σmax2<2\beta\sigma\_{\max}^{2}<2 the lower bound is strictly positive, so EE is strictly convex. The potential U=β​EU=\beta E is then mm-strongly convex with m=β​(1−β​σmax2/2)m=\beta(1-\beta\sigma\_{\max}^{2}/2) and has LUL\_{U}-Lipschitz gradient with LU=β​(1+β​σmax2/2)L\_{U}=\beta(1+\beta\sigma\_{\max}^{2}/2). The condition number is

|  |  |  |
| --- | --- | --- |
|  | κ=LUm=1+β​σmax2/21−β​σmax2/2,\displaystyle\kappa=\frac{L\_{U}}{m}=\frac{1+\beta\sigma\_{\max}^{2}/2}{1-\beta\sigma\_{\max}^{2}/2}, |  |

which diverges as β​σmax2→2\beta\sigma\_{\max}^{2}\to 2, reflecting the onset of non-convexity and the proliferation of local minima in the energy landscape.

## Appendix C MALA Variant of Stochastic Attention

Algorithm [1](#alg1 "Algorithm 1 ‣ 4.1 Stochastic Attention Update ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") uses the Unadjusted Langevin Algorithm (ULA), which is simple but introduces an O​(α)O(\alpha) discretization bias. The Metropolis-Adjusted Langevin Algorithm (MALA) eliminates this bias by appending an accept/reject step to each Langevin proposal. At the step size and temperature used in our experiments (α=0.01\alpha{=}0.01, β=2000\beta{=}2000), the two algorithms produced practically indistinguishable outputs (Table [1](#S5.T1 "Table 1 ‣ Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")); however, the correction becomes important when a larger step size is desired, e.g., to accelerate mixing in high-dimensional or low-temperature settings where α\alpha must be increased beyond the regime in which the ULA bias is negligible.

Algorithm 2  MALA Stochastic Attention Sampler

0: Memory matrix 𝐗∈ℝN×K\mathbf{X}\in\mathbb{R}^{N\times K}, inverse temperature β>0\beta>0, step size α∈(0,1)\alpha\in(0,1), iterations TT, initial state 𝝃0∈ℝN\boldsymbol{\xi}\_{0}\in\mathbb{R}^{N}

0: Sample trajectory 𝝃0,𝝃1,…,𝝃T\boldsymbol{\xi}\_{0},\boldsymbol{\xi}\_{1},\dots,\boldsymbol{\xi}\_{T}

1: for t=0,1,…,T−1t=0,1,\dots,T-1 do

2:  𝐚t←softmax⁡(β​𝐗⊤​𝝃t)\mathbf{a}\_{t}\leftarrow\operatorname{softmax}\!\bigl(\beta\,\mathbf{X}^{\top}\boldsymbol{\xi}\_{t}\bigr) ⊳\triangleright attention weights at current state

3:  𝝁t←(1−α)​𝝃t+α​𝐗​𝐚t\boldsymbol{\mu}\_{t}\leftarrow(1-\alpha)\,\boldsymbol{\xi}\_{t}+\alpha\,\mathbf{X}\,\mathbf{a}\_{t} ⊳\triangleright Langevin proposal mean

4:  ϵt∼𝒩​(𝟎,𝐈N)\boldsymbol{\epsilon}\_{t}\sim\mathcal{N}(\mathbf{0},\mathbf{I}\_{N})

5:  𝝃⋆←𝝁t+2​α/β​ϵt\boldsymbol{\xi}^{\star}\leftarrow\boldsymbol{\mu}\_{t}+\sqrt{2\alpha/\beta}\;\boldsymbol{\epsilon}\_{t} ⊳\triangleright candidate state

6:  𝐚⋆←softmax⁡(β​𝐗⊤​𝝃⋆)\mathbf{a}^{\star}\leftarrow\operatorname{softmax}\!\bigl(\beta\,\mathbf{X}^{\top}\boldsymbol{\xi}^{\star}\bigr) ⊳\triangleright attention weights at candidate

7:  𝝁⋆←(1−α)​𝝃⋆+α​𝐗​𝐚⋆\boldsymbol{\mu}^{\star}\leftarrow(1-\alpha)\,\boldsymbol{\xi}^{\star}+\alpha\,\mathbf{X}\,\mathbf{a}^{\star} ⊳\triangleright reverse proposal mean

8:  log⁡r←−β​[E​(𝝃⋆)−E​(𝝃t)]−β4​α​[∥𝝃t−𝝁⋆∥2−∥𝝃⋆−𝝁t∥2]\log r\leftarrow-\beta\bigl[E(\boldsymbol{\xi}^{\star})-E(\boldsymbol{\xi}\_{t})\bigr]-\frac{\beta}{4\alpha}\bigl[\lVert\boldsymbol{\xi}\_{t}-\boldsymbol{\mu}^{\star}\rVert^{2}-\lVert\boldsymbol{\xi}^{\star}-\boldsymbol{\mu}\_{t}\rVert^{2}\bigr]

9:  u∼Uniform​(0,1)u\sim\mathrm{Uniform}(0,1)

10:  if log⁡u<min⁡(0,log⁡r)\log u<\min(0,\,\log r) then

11:   𝝃t+1←𝝃⋆\boldsymbol{\xi}\_{t+1}\leftarrow\boldsymbol{\xi}^{\star} ⊳\triangleright accept

12:  else

13:   𝝃t+1←𝝃t\boldsymbol{\xi}\_{t+1}\leftarrow\boldsymbol{\xi}\_{t} ⊳\triangleright reject

14:  end if

15: end for

Compared with Algorithm [1](#alg1 "Algorithm 1 ‣ 4.1 Stochastic Attention Update ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."), MALA replaces the single-line state update (line 4) with a propose-then-correct cycle (lines 2–13). The additional cost per step is one extra attention evaluation (line 6) and one energy evaluation (line 8), doubling the per-iteration 𝒪​(N​K)\mathcal{O}(NK) cost. In the limit α→0\alpha\to 0 both algorithms coincide; at moderate α\alpha the accept/reject step removes O​(α)O(\alpha) discretization bias.

#### What line 8 computes and why.

The ULA update in Algorithm [1](#alg1 "Algorithm 1 ‣ 4.1 Stochastic Attention Update ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") draws each new state from a Gaussian proposal centered on the Langevin mean 𝝁t\boldsymbol{\mu}\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | q​(𝝃⋆∣𝝃t)=𝒩​(𝝃⋆;𝝁t,2​αβ​𝐈),q(\boldsymbol{\xi}^{\star}\mid\boldsymbol{\xi}\_{t})=\mathcal{N}\!\bigl(\boldsymbol{\xi}^{\star};\;\boldsymbol{\mu}\_{t},\;\tfrac{2\alpha}{\beta}\mathbf{I}\bigr), |  | (16) |

where 𝝁t=(1−α)​𝝃t+α​𝐗𝐚t\boldsymbol{\mu}\_{t}=(1{-}\alpha)\boldsymbol{\xi}\_{t}+\alpha\,\mathbf{X}\mathbf{a}\_{t} encodes one step of gradient descent on EE.
For the chain to sample from the correct Boltzmann target pβ∝exp⁡(−β​E)p\_{\beta}\propto\exp(-\beta E), the transition kernel must satisfy *detailed balance*: pβ​(𝝃)​q​(𝝃⋆∣𝝃)=pβ​(𝝃⋆)​q​(𝝃∣𝝃⋆)p\_{\beta}(\boldsymbol{\xi})\,q(\boldsymbol{\xi}^{\star}\mid\boldsymbol{\xi})=p\_{\beta}(\boldsymbol{\xi}^{\star})\,q(\boldsymbol{\xi}\mid\boldsymbol{\xi}^{\star}) for every pair of states.
When α>0\alpha>0 the proposal ([16](#A3.E16 "In What line 8 computes and why. ‣ Appendix C MALA Variant of Stochastic Attention ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) is *asymmetric*: the forward density q​(𝝃⋆∣𝝃t)q(\boldsymbol{\xi}^{\star}\mid\boldsymbol{\xi}\_{t}) is centered on 𝝁t\boldsymbol{\mu}\_{t}, but the reverse density q​(𝝃t∣𝝃⋆)q(\boldsymbol{\xi}\_{t}\mid\boldsymbol{\xi}^{\star}) is centered on a *different* point 𝝁⋆=(1−α)​𝝃⋆+α​𝐗𝐚⋆\boldsymbol{\mu}^{\star}=(1{-}\alpha)\boldsymbol{\xi}^{\star}+\alpha\mathbf{X}\mathbf{a}^{\star} (line 7). The gradient at the candidate 𝝃⋆\boldsymbol{\xi}^{\star} generally differs from the gradient at 𝝃t\boldsymbol{\xi}\_{t}, so the two Gaussians are not mirror images of each other. This asymmetry means the ULA chain does not satisfy detailed balance and therefore converges to a distribution that is O​(α)O(\alpha)-close to, but not exactly, pβp\_{\beta}.

MALA corrects this by computing the Metropolis–Hastings acceptance ratio on line 8, which is the logarithm of

|  |  |  |  |
| --- | --- | --- | --- |
|  | r=pβ​(𝝃⋆)​q​(𝝃t∣𝝃⋆)pβ​(𝝃t)​q​(𝝃⋆∣𝝃t).r=\frac{p\_{\beta}(\boldsymbol{\xi}^{\star})\;q(\boldsymbol{\xi}\_{t}\mid\boldsymbol{\xi}^{\star})}{p\_{\beta}(\boldsymbol{\xi}\_{t})\;q(\boldsymbol{\xi}^{\star}\mid\boldsymbol{\xi}\_{t})}. |  | (17) |

We now derive log⁡r\log r explicitly. The target ratio contributes

|  |  |  |
| --- | --- | --- |
|  | log⁡pβ​(𝝃⋆)pβ​(𝝃t)=−β​[E​(𝝃⋆)−E​(𝝃t)].\displaystyle\log\frac{p\_{\beta}(\boldsymbol{\xi}^{\star})}{p\_{\beta}(\boldsymbol{\xi}\_{t})}=-\beta\bigl[E(\boldsymbol{\xi}^{\star})-E(\boldsymbol{\xi}\_{t})\bigr]. |  |

For the proposal ratio, both the forward and reverse proposals are Gaussians with the same variance σ2=2​α/β\sigma^{2}=2\alpha/\beta but different means. Writing out the log-density of a 𝒩​(𝝁,σ2​𝐈)\mathcal{N}(\boldsymbol{\mu},\sigma^{2}\mathbf{I}) and noting that the normalization constants cancel:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡q​(𝝃t∣𝝃⋆)q​(𝝃⋆∣𝝃t)\displaystyle\log\frac{q(\boldsymbol{\xi}\_{t}\mid\boldsymbol{\xi}^{\star})}{q(\boldsymbol{\xi}^{\star}\mid\boldsymbol{\xi}\_{t})} | =−12​σ2​∥𝝃t−𝝁⋆∥2+12​σ2​∥𝝃⋆−𝝁t∥2\displaystyle=-\frac{1}{2\sigma^{2}}\lVert\boldsymbol{\xi}\_{t}-\boldsymbol{\mu}^{\star}\rVert^{2}+\frac{1}{2\sigma^{2}}\lVert\boldsymbol{\xi}^{\star}-\boldsymbol{\mu}\_{t}\rVert^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−12⋅(2​α/β)​[∥𝝃t−𝝁⋆∥2−∥𝝃⋆−𝝁t∥2]\displaystyle=-\frac{1}{2\cdot(2\alpha/\beta)}\bigl[\lVert\boldsymbol{\xi}\_{t}-\boldsymbol{\mu}^{\star}\rVert^{2}-\lVert\boldsymbol{\xi}^{\star}-\boldsymbol{\mu}\_{t}\rVert^{2}\bigr] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−β4​α​[∥𝝃t−𝝁⋆∥2−∥𝝃⋆−𝝁t∥2].\displaystyle=-\frac{\beta}{4\alpha}\bigl[\lVert\boldsymbol{\xi}\_{t}-\boldsymbol{\mu}^{\star}\rVert^{2}-\lVert\boldsymbol{\xi}^{\star}-\boldsymbol{\mu}\_{t}\rVert^{2}\bigr]. |  |

Summing the two contributions gives the expression on line 8:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡r=−β​[E​(𝝃⋆)−E​(𝝃t)]⏟(i) target ratio−β4​α​[∥𝝃t−𝝁⋆∥2−∥𝝃⋆−𝝁t∥2]⏟(ii) proposal asymmetry correction.\log r=\underbrace{-\beta\bigl[E(\boldsymbol{\xi}^{\star})-E(\boldsymbol{\xi}\_{t})\bigr]}\_{\text{(i) target ratio}}\;-\;\underbrace{\frac{\beta}{4\alpha}\bigl[\lVert\boldsymbol{\xi}\_{t}-\boldsymbol{\mu}^{\star}\rVert^{2}-\lVert\boldsymbol{\xi}^{\star}-\boldsymbol{\mu}\_{t}\rVert^{2}\bigr]}\_{\text{(ii) proposal asymmetry correction}}. |  | (18) |

Term (i) is the standard Boltzmann factor: it favors moves to lower energy (as in simulated annealing). Term (ii) corrects for the asymmetry of the Langevin proposal: ∥𝝃⋆−𝝁t∥2\lVert\boldsymbol{\xi}^{\star}-\boldsymbol{\mu}\_{t}\rVert^{2} measures how far the candidate is from the forward proposal mean, while ∥𝝃t−𝝁⋆∥2\lVert\boldsymbol{\xi}\_{t}-\boldsymbol{\mu}^{\star}\rVert^{2} measures how far the current state is from the reverse proposal mean. If the proposal were symmetric (as it would be for a random walk with no gradient), these two norms would cancel and only the energy term would remain. With the Langevin gradient drift they differ, and term (ii) accounts for the resulting bias.

#### The accept/reject decision (lines 9–13).

Given log⁡r\log r, the chain draws u∼Uniform​(0,1)u\sim\mathrm{Uniform}(0,1) and accepts the candidate 𝝃⋆\boldsymbol{\xi}^{\star} if log⁡u<min⁡(0,log⁡r)\log u<\min(0,\log r), i.e. if u<min⁡(1,r)u<\min(1,r). There are two cases:

* •

  *r≥1r\geq 1 (always accept):* The candidate is favored by both the target and the proposal correction. The move is accepted with probability 1.
* •

  *r<1r<1 (accept with probability rr):* The candidate is disfavored on net. It is accepted with probability rr and rejected with probability 1−r1{-}r, in which case the chain stays at 𝝃t\boldsymbol{\xi}\_{t}.

This stochastic accept/reject step restores detailed balance *exactly*, regardless of the step size α\alpha. The trade-off is efficiency: when α\alpha is too large the proposal overshoots, rr is frequently small, and most candidates are rejected, so the chain moves slowly. When α\alpha is small the proposal is accurate, r≈1r\approx 1 almost always, and MALA reduces to ULA. The acceptance rate therefore serves as a built-in diagnostic: high acceptance (≳\gtrsim90%) means the discretization bias is small and ULA suffices; low acceptance means the Metropolis correction is actively preventing the chain from drifting to the wrong distribution.

When is the correction useful? At the operating point of our MNIST experiment (α=0.01\alpha{=}0.01, d=784d{=}784, β=2000\beta{=}2000) the acceptance rate is 99.2%, so the correction is a near no-op. However, if the step size is increased to accelerate mixing (e.g., α=0.1\alpha{=}0.1 or larger), the ULA bias grows as O​(α)O(\alpha) and the stationary distribution shifts away from the true target. In this regime MALA remains unbiased (albeit with a lower acceptance rate), making it the preferred choice. Practitioners should therefore monitor the acceptance rate: values above ∼\sim90% indicate that ULA suffices, while lower rates signal that the Metropolis correction is earning its keep.

## Appendix D Load-Ratio Phase Diagram

Figure [3](#A4.F3 "Figure 3 ‣ Appendix D Load-Ratio Phase Diagram ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") showed the full phase diagram of attention concentration C=1−H​(𝐚)/log⁡KC=1-H(\mathbf{a})/\log K over load ratio K/dK/d and inverse temperature β\beta, as described in the main text.

![Refer to caption](2603.06875v1/x2.png)


Figure 3: Phase diagram of attention concentration C=1−H​(𝐚)/log⁡KC=1-H(\mathbf{a})/\log K over load ratio K/dK/d (horizontal) and inverse temperature β\beta (vertical, log scale), with d=64d=64. Each cell averages over five independent datasets. The dashed contour marks C=0.5C=0.5, separating a retrieval regime (upper-left, warm colors) from a diffuse regime (lower-right, dark colors).

## Appendix E Multi-Digit MNIST Generalization

To verify that the results reported for digit “3” in the main text are not specific to a single morphological class, we repeated the identical multi-chain protocol (30 chains, T=5,000T{=}5{,}000, burn-in 2,0002{,}000, thin every 100 then sub-sample 5, β=2000\beta{=}2000, α=0.01\alpha{=}0.01, K=100K{=}100 stored patterns per digit) on two additional MNIST digits chosen for their distinct morphological properties: digit “1” (simple stroke, near-degenerate orientation) and digit “8” (complex topology with two enclosed loops and high intra-class variance). All seven baselines (including the VAE) and the MALA variant were run with the identical protocol; results appear in Tables [2](#A5.T2 "Table 2 ‣ Appendix E Multi-Digit MNIST Generalization ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") and [3](#A5.T3 "Table 3 ‣ Appendix E Multi-Digit MNIST Generalization ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").

Table 2: Quantitative comparison on MNIST digit “1” (K=100K{=}100, d=784d{=}784, β=2000\beta{=}2000). Same protocol as Table [1](#S5.T1 "Table 1 ‣ Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."), including the VAE baseline (latent dim 8, same two-phase training). MALA acceptance rate: 99.2%. Values are mean ±\pm SE across 30 chains.

| Method | 𝒩\mathcal{N} ↑\uparrow | 𝒟¯\bar{\mathcal{D}} ↑\uparrow | E¯\bar{E} ↓\downarrow |
| --- | --- | --- | --- |
| Bootstrap (replay) | 0.000±0.0000.000\pm 0.000 | 0.416±0.0190.416\pm 0.019 | −0.500±0.000-0.500\pm 0.000 |
| Gaussian perturbation | 0.004±0.0000.004\pm 0.000 | 0.422±0.0170.422\pm 0.017 | −0.496±0.000-0.496\pm 0.000 |
| Random convex combination | 0.097±0.0010.097\pm 0.001 | 0.007±0.0000.007\pm 0.000 | −0.398±0.001-0.398\pm 0.001 |
| GMM-PCA (r=50r{=}50, C=10C{=}10) | 0.130±0.0050.130\pm 0.005 | 0.401±0.0170.401\pm 0.017 | −0.366±0.005-0.366\pm 0.005 |
| VAE (latent=8{=}8) | 0.180±0.0060.180\pm 0.006 | 0.408±0.0080.408\pm 0.008 | −0.320±0.006-0.320\pm 0.006 |
| MALA | 0.151±0.0010.151\pm 0.001 | 0.586±0.0010.586\pm 0.001 | −0.305±0.001-0.305\pm 0.001 |
| Stochastic attention | 0.153±0.001\mathbf{0.153\pm 0.001} | 0.591±0.001\mathbf{0.591\pm 0.001} | −0.303±0.001\mathbf{-0.303\pm 0.001} |




Table 3: Quantitative comparison on MNIST digit “8” (K=100K{=}100, d=784d{=}784, β=2000\beta{=}2000). Same protocol as Table [1](#S5.T1 "Table 1 ‣ Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."), including the VAE baseline (latent dim 8, same two-phase training). MALA acceptance rate: 99.2%. Values are mean ±\pm SE across 30 chains.

| Method | 𝒩\mathcal{N} ↑\uparrow | 𝒟¯\bar{\mathcal{D}} ↑\uparrow | E¯\bar{E} ↓\downarrow |
| --- | --- | --- | --- |
| Bootstrap (replay) | 0.000±0.0000.000\pm 0.000 | 0.421±0.0120.421\pm 0.012 | −0.500±0.000-0.500\pm 0.000 |
| Gaussian perturbation | 0.004±0.0000.004\pm 0.000 | 0.450±0.0110.450\pm 0.011 | −0.496±0.000-0.496\pm 0.000 |
| Random convex combination | 0.099±0.0000.099\pm 0.000 | 0.007±0.0000.007\pm 0.000 | −0.395±0.000-0.395\pm 0.000 |
| GMM-PCA (r=50r{=}50, C=10C{=}10) | 0.194±0.0050.194\pm 0.005 | 0.420±0.0110.420\pm 0.011 | −0.305±0.005-0.305\pm 0.005 |
| VAE (latent=8{=}8) | 0.209±0.0050.209\pm 0.005 | 0.397±0.0090.397\pm 0.009 | −0.291±0.005-0.291\pm 0.005 |
| MALA | 0.151±0.0010.151\pm 0.001 | 0.554±0.0020.554\pm 0.002 | −0.305±0.001-0.305\pm 0.001 |
| Stochastic attention | 0.152±0.001\mathbf{0.152\pm 0.001} | 0.557±0.001\mathbf{0.557\pm 0.001} | −0.303±0.001\mathbf{-0.303\pm 0.001} |

Across all three digit classes, the stochastic attention sampler and MALA produced practically indistinguishable metrics, both dominating every baseline on diversity simultaneously. The VAE (latent dim 8) was the strongest non-Langevin baseline on novelty (0.1800.180–0.2090.209 vs. 0.1300.130–0.1940.194 for GMM-PCA), but both learned models were far below the Langevin methods on diversity (0.3970.397–0.4080.408 for VAE vs. 0.5570.557–0.6000.600 for SA), confirming that a static learned density cannot match the ergodic coverage of Langevin dynamics. The MALA acceptance rate was 99.2% for all digits, confirming that ULA discretization bias remains negligible regardless of digit morphology.

Figure [4](#A5.F4 "Figure 4 ‣ Appendix E Multi-Digit MNIST Generalization ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") and Figure [5](#A5.F5 "Figure 5 ‣ Appendix E Multi-Digit MNIST Generalization ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") showed representative 4×44{\times}4 sample grids for each method. The qualitative pattern was the same as for digit “3”: bootstrap outputs were exact stored copies, Gaussian perturbation was visually indistinguishable from bootstrap, random convex combinations produced uniform blurry averages, and both Langevin methods generated diverse, structured digits.

![Refer to caption](2603.06875v1/figs/Fig_mnist_grid_bootstrap_digit1.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_grid_gaussian_digit1.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_grid_convex_digit1.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_grid_mala_digit1.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_grid_sa_digit1.png)

(a) Bootstrap (b) Gaussian (c) Convex (d) MALA (e) Ours

Figure 4: Generated MNIST digit “1” samples (4×44{\times}4 grids). The pattern matches digit “3”: only the Langevin-based methods (d, e) produce diverse, structured outputs.



![Refer to caption](2603.06875v1/figs/Fig_mnist_grid_bootstrap_digit8.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_grid_gaussian_digit8.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_grid_convex_digit8.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_grid_mala_digit8.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_grid_sa_digit8.png)

(a) Bootstrap (b) Gaussian (c) Convex (d) MALA (e) Ours

Figure 5: Generated MNIST digit “8” samples (4×44{\times}4 grids). Despite digit “8” having higher intra-class variance and more complex topology than digit “3”, the qualitative pattern is unchanged: Langevin methods dominate all baselines.

#### Temperature spectrum on digit “8.”

The baseline comparison above fixes β=2000\beta{=}2000, which places the sampler deep in the retrieval regime: each chain stays near its seed pattern and the “generation” is local variation within a single energy basin.
To show the full retrieval-generation trade-off on real images, Figure [6](#A5.F6 "Figure 6 ‣ Temperature spectrum on digit “8.” ‣ Appendix E Multi-Digit MNIST Generalization ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") displays 4×44{\times}4 SA grids at four inverse temperatures alongside 16 stored patterns for reference.
Table [4](#A5.T4 "Table 4 ‣ Temperature spectrum on digit “8.” ‣ Appendix E Multi-Digit MNIST Generalization ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") reported the corresponding metrics.

Table 4: Temperature spectrum for digit “8” (K=100K{=}100, d=784d{=}784, α=0.01\alpha{=}0.01, 30 chains). SNR=α​β/2​d\mathrm{SNR}=\sqrt{\alpha\beta/2d} is the per-step signal-to-noise ratio; the synthetic transition occurs near SNR≈0.02\mathrm{SNR}\approx 0.02–0.030.03. As SNR falls through this band the sampler crosses from structured retrieval into diffuse generation. Values are mean ±\pm SE across 30 chains.

| β\beta | SNR | 𝒩\mathcal{N} ↑\uparrow | 𝒟¯\bar{\mathcal{D}} ↑\uparrow | E¯\bar{E} ↓\downarrow | Mean max-cos\cos |
| --- | --- | --- | --- | --- | --- |
| 2000 | 0.113 | 0.152±0.0010.152\pm 0.001 | 0.557±0.0010.557\pm 0.001 | −0.3±0.00-0.3\pm 0.00 | 0.848±0.0010.848\pm 0.001 |
| 200 | 0.036 | 0.547±0.0020.547\pm 0.002 | 0.872±0.0020.872\pm 0.002 | 1.5±0.011.5\pm 0.01 | 0.453±0.0020.453\pm 0.002 |
| 50 | 0.018 | 0.753±0.0020.753\pm 0.002 | 0.965±0.0020.965\pm 0.002 | 7.4±0.037.4\pm 0.03 | 0.247±0.0020.247\pm 0.002 |
| 10 | 0.008 | 0.870±0.0030.870\pm 0.003 | 0.992±0.0020.992\pm 0.002 | 38.6±0.1638.6\pm 0.16 | 0.130±0.0030.130\pm 0.003 |

At β=2000\beta{=}2000 the outputs were recognizable eights that closely resembled individual stored patterns (mean max-cos 0.85); novelty was low and diversity came entirely from the multi-chain initialization, not from any single chain exploring between basins.
As β\beta decreased, the energy barriers shrank, chains escaped their initial basins, and novelty/diversity rose sharply.
At β=200\beta{=}200 the mean max-cosine dropped to 0.45, meaning outputs sat roughly halfway between stored patterns, a regime of genuine interpolation.
By β=50\beta{=}50 the samples were highly novel (0.75) but began to lose recognizable digit structure, and at β=10\beta{=}10 the outputs were essentially isotropic noise with no visual resemblance to eights.
This illustrates the fundamental retrieval-generation trade-off: no single β\beta simultaneously maximizes fidelity and novelty. The operating point must be chosen according to the application, and the temperature parameter gives the user explicit control over this trade-off.

![Refer to caption](2603.06875v1/figs/Fig_mnist_tempspectrum_digit8_stored.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_tempspectrum_digit8_beta2000.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_tempspectrum_digit8_beta200.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_tempspectrum_digit8_beta50.png)

![Refer to caption](2603.06875v1/figs/Fig_mnist_tempspectrum_digit8_beta10.png)

Stored β=2000\beta{=}2000 β=200\beta{=}200 β=50\beta{=}50 β=10\beta{=}10

Figure 6: Temperature spectrum for MNIST digit “8.” From left to right: 16 stored patterns; SA samples at β=2000\beta{=}2000 (retrieval, local variation around stored patterns); β=200\beta{=}200 (intermediate, genuine interpolation); β=50\beta{=}50 (high novelty, structure fading); β=10\beta{=}10 (diffuse noise). The trade-off between fidelity and novelty is governed entirely by β\beta.

## Appendix F Single-Chain Diversity Analysis

Table [1](#S5.T1 "Table 1 ‣ Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") uses 30 independent chains each initialized near a different stored pattern; the reported diversity of 0.6000.600 includes both *initialization diversity* (spread from 30 distinct seeds) and *within-chain mixing* (sampling from a fixed starting point). To quantify these contributions separately, we ran one chain from a fixed initialization (stored pattern 1 plus σinit=0.01\sigma\_{\mathrm{init}}{=}0.01 Gaussian noise, seed fixed) for T=50,000T{=}50{,}000 steps (burn-in 10,00010{,}000, thin every 100, yielding 400 samples) at β∈{2000, 200, 50}\beta\in\{2000,\,200,\,50\} (SNR∈{0.113, 0.036, 0.018}\mathrm{SNR}\in\{0.113,\,0.036,\,0.018\}) on digit “3”.

Table 5: Single-chain vs. multi-chain diversity on digit “3” (K=100K{=}100, d=784d{=}784, α=0.01\alpha{=}0.01). SNR=α​β/2​d\mathrm{SNR}=\sqrt{\alpha\beta/2d}. The multi-chain row reproduces the SA entry from Table [1](#S5.T1 "Table 1 ‣ Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."). The diversity gap of 0.3180.318 at SNR=0.113\mathrm{SNR}{=}0.113 is the initialization contribution; single-chain diversity exceeds the multi-chain value once SNR falls toward the transition band (0.020.02–0.030.03).

| Protocol | β\beta | SNR | 𝒩\mathcal{N} ↑\uparrow | 𝒟¯\bar{\mathcal{D}} ↑\uparrow | E¯\bar{E} ↓\downarrow | Max-cos\cos |
| --- | --- | --- | --- | --- | --- | --- |
| Multi-chain (30 chains) | 2000 | 0.113 | 0.152±0.0010.152\pm 0.001 | 0.600±0.0010.600\pm 0.001 | −0.303±0.001-0.303\pm 0.001 | 0.848±0.0010.848\pm 0.001 |
| Single-chain | 2000 | 0.113 | 0.153±0.0000.153\pm 0.000 | 0.282±0.0010.282\pm 0.001 | −0.300±0.000-0.300\pm 0.000 | 0.847±0.0000.847\pm 0.000 |
| Single-chain | 200 | 0.036 | 0.551±0.0010.551\pm 0.001 | 0.796±0.0020.796\pm 0.002 | 1.5±0.0\phantom{-}1.5\phantom{0}\pm 0.0\phantom{0} | 0.449±0.0010.449\pm 0.001 |
| Single-chain | 50 | 0.018 | 0.756±0.0020.756\pm 0.002 | 0.967±0.0020.967\pm 0.002 | 7.4±0.0\phantom{-}7.4\phantom{0}\pm 0.0\phantom{0} | 0.244±0.0020.244\pm 0.002 |



![Refer to caption](2603.06875v1/figs/Fig_single_chain_grid_beta2000.png)

(a) β=2000\beta{=}2000, SNR=0.113=0.113
  
structured retrieval (𝒟¯=0.282\bar{\mathcal{D}}{=}0.282)

![Refer to caption](2603.06875v1/figs/Fig_single_chain_grid_beta200.png)

(b) β=200\beta{=}200, SNR=0.036=0.036
  
genuine generation (𝒟¯=0.796\bar{\mathcal{D}}{=}0.796)

![Refer to caption](2603.06875v1/figs/Fig_single_chain_grid_beta50.png)

(c) β=50\beta{=}50, SNR=0.018=0.018
  
diffuse (𝒟¯=0.967\bar{\mathcal{D}}{=}0.967)

Figure 7: Single-chain samples (6×66{\times}6 grids, digit “3”) from a fixed seed at three operating points. (a) At SNR=0.113=0.113 the chain stays near one stored pattern; diversity is low (0.2820.282). (b) At SNR=0.036=0.036 the chain spontaneously crosses energy barriers; single-chain diversity (0.7960.796) *exceeds* the 30-chain β=2000\beta{=}2000 value (0.6000.600), confirming genuine generation. (c) At SNR=0.018=0.018 the chain is fully diffuse; samples lose recognizable digit structure.

At β=2000\beta{=}2000 the single-chain diversity of 0.2820.282 is not negligible: the chain samples a genuine distribution within its energy basin rather than collapsing to a point mass. As β\beta decreased the energy barriers shrank, chains escaped their initial basins, and single-chain diversity rose sharply, mirroring the temperature-spectrum results of Appendix [E](#A5 "Appendix E Multi-Digit MNIST Generalization ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."). At β=200\beta{=}200 single-chain diversity (0.7960.796) exceeds the multi-chain value at β=2000\beta{=}2000, and at β=50\beta{=}50 it approaches the isotropic limit (0.9670.967, mean max-cos 0.2440.244). The multi-chain protocol at β=2000\beta{=}2000 is therefore best understood as a *structured retrieval* strategy in which each chain contributes low-energy samples from a distinct basin, while single-chain operation at β=200\beta{=}200 provides genuine generative diversity without requiring multiple initializations.

## Appendix G Financial Log-Return Generation

The synthetic experiments validated the sampler on controlled geometry; this section used real financial data to *precisely characterize* what equilibrium Boltzmann sampling on the Hopfield energy captures and, equally importantly, what it cannot, and why each limitation is a principled theoretical consequence rather than a tuning failure.

### G.1 Data and Memory Construction

We collected daily adjusted closing prices for d=424d=424 S&P 500 constituents with complete histories over a K=2,766K=2{,}766-trading-day window. For each firm ii and day tt, the continuously compounded growth rate is gt(i)=log⁡(St(i)/St−1(i))g^{(i)}\_{t}=\log(S^{(i)}\_{t}/S^{(i)}\_{t-1}). Each trading day yielded a dd-dimensional return vector 𝐠t∈ℝ424\mathbf{g}\_{t}\in\mathbb{R}^{424}. We stored these as columns of a raw memory matrix 𝐌∈ℝd×K\mathbf{M}\in\mathbb{R}^{d\times K} and constructed the scaled memory matrix 𝐗∈ℝd×K\mathbf{X}\in\mathbb{R}^{d\times K} by centering each column to zero cross-sectional mean and normalizing to unit ℓ2\ell\_{2} norm, following the standard protocol for modern Hopfield networks [[21](#bib.bib3 "Hopfield networks is all you need")]. The load ratio was K/d≈6.5K/d\approx 6.5.

### G.2 I.I.D. Pool: Marginal and Cross-Sectional Fidelity

We compared SA to *historical bootstrap resampling* (drawing stored return vectors uniformly at random from 𝐌\mathbf{M}) on marginal and cross-sectional metrics. Because the projection 𝐠^=𝐌​softmax⁡(β​𝐗⊤​𝝃)\hat{\mathbf{g}}=\mathbf{M}\,\operatorname{softmax}(\beta\,\mathbf{X}^{\top}\boldsymbol{\xi}) is a convex combination of historical return vectors, bootstrap sets an upper bound on distributional fidelity; the key question is what SA contributes beyond verbatim replay. We launched nchains=30n\_{\text{chains}}=30 independent ULA chains, each initialized near a randomly chosen stored memory, and ran T=5,000T=5{,}000 steps with step size α=0.01\alpha=0.01 and fixed inverse temperature β=25\beta=25 (SNR=α​β/2​d≈0.017\mathrm{SNR}=\sqrt{\alpha\beta/2d}\approx 0.017). After discarding a burn-in of 2,0002{,}000 steps and thinning every 100100, we obtained 900900 approximately i.i.d. samples.

#### Marginal distributions and novelty.

For each of d=424d=424 tickers, we ran a two-sample KS test between generated and historical returns, and QQ plots for five representative tickers (Figure [8](#A7.F8 "Figure 8 ‣ Tail survival functions. ‣ G.2 I.I.D. Pool: Marginal and Cross-Sectional Fidelity ‣ Appendix G Financial Log-Return Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")). The convex-combination projection compresses per-ticker standard deviation by ≈1.14×\approx 1.14\times at β=25\beta{=}25 (SNR≈\approx0.017); we correct for this by applying a per-ticker affine standardization (aligning the mean and standard deviation of each ticker’s generated series to the historical moments, analogous to the marginal-calibration step in copula-based scenario generation), which leaves the chain dynamics and novelty metric unchanged. After correction, 272272 of 424424 tickers pass the two-sample KS test at the 5%5\% level (mean p=0.193p{=}0.193). Bootstrap achieves 99.3%99.3\% pass by drawing from the empirical distribution (mean p=0.622p{=}0.622); the residual 35.8%35.8\% SA failure reflects higher-order distributional differences (skewness, kurtosis) beyond what affine correction addresses. The key distinction remains novelty: SA chain states have 1−maxk⁡cos⁡(𝝃,𝐗:,k)=0.768±0.0011-\max\_{k}\cos(\boldsymbol{\xi},\mathbf{X}\_{:,k})=0.768\pm 0.001, while every bootstrap draw is a verbatim historical scenario (novelty 0.0000.000, Table [6](#A7.T6 "Table 6 ‣ Summary. ‣ G.3 Sequential Generation and Temporal Properties ‣ Appendix G Financial Log-Return Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")).

#### Cross-asset correlation.

Figure [9](#A7.F9 "Figure 9 ‣ Tail survival functions. ‣ G.2 I.I.D. Pool: Marginal and Cross-Sectional Fidelity ‣ Appendix G Financial Log-Return Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") plots each of the (4242)=89,676\binom{424}{2}=89{,}676 pairwise correlations of the generated returns against the corresponding historical correlations. The cloud lay along the y=xy=x diagonal: SA Frobenius correlation error is 26.3%26.3\% versus 15.6%15.6\% for bootstrap. The per-ticker affine correction does not alter this value: correlation is scale-invariant, so rescaling each ticker’s series preserves cor⁡(𝐆^)\operatorname{cor}(\hat{\mathbf{G}}) exactly. SA trades some correlation fidelity for novelty; the Hopfield energy concentrates sampling on energetically favorable regime interpolations rather than uniform historical replay.

#### Tail survival functions.

Figure [10](#A7.F10 "Figure 10 ‣ Tail survival functions. ‣ G.2 I.I.D. Pool: Marginal and Cross-Sectional Fidelity ‣ Appendix G Financial Log-Return Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") displays the empirical survival functions of portfolio-level (equal-weight) returns. Both right and left tails matched closely on a log scale, demonstrating that the sampler reproduced the heavy-tailed nature of equity returns without distributional assumptions.

![Refer to caption](2603.06875v1/x3.png)


Figure 8: QQ plots of generated (after per-ticker affine correction) vs. historical log returns for five representative S&P 500 constituents. Quantiles track closely for these tickers; 64.2%64.2\% of all 424424 tickers pass the two-sample KS test at the 5%5\% level. The dashed red line is y=xy=x.

![Refer to caption](2603.06875v1/x4.png)


Figure 9: Pairwise correlation: historical vs. generated. Each point represents one of 89,67689{,}676 asset pairs. The scatter around y=xy=x shows partial preservation of cross-asset dependence structure (Frobenius error 26.3%26.3\% vs. 15.6%15.6\% for bootstrap).

![Refer to caption](2603.06875v1/x5.png)


Figure 10: Empirical survival functions of equal-weighted portfolio returns. Both right tail P​(g>x)P(g>x) and left tail P​(g<x)P(g<x) match closely on a log scale.

### G.3 Sequential Generation and Temporal Properties

The i.i.d. pool above validates marginal fidelity but says nothing about temporal dynamics. Real equity returns exhibit two key temporal properties: (i) returns are essentially unpredictable (near-zero autocorrelation), and (ii) squared returns (a proxy for volatility) are highly autocorrelated and decay slowly, a phenomenon known as *volatility clustering* [[3](#bib.bib26 "Empirical properties of asset returns: stylized facts and statistical issues")]. We tested how far the stochastic attention sampler could go toward reproducing these properties.

#### Protocol.

We generated a sequential time series of daily return vectors using the MALA sampler (Algorithm [2](#alg2 "Algorithm 2 ‣ Appendix C MALA Variant of Stochastic Attention ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.")) with warm-starting: each day’s chain was initialized at the previous day’s endpoint, creating temporal continuity in the chain trajectory.
We set β=12\beta=12 (below the main operating point β=25\beta{=}25) to ensure adequate MALA mixing within Tinner=200T\_{\text{inner}}{=}200 inner steps per day.
Algorithm [3](#alg3 "Algorithm 3 ‣ Protocol. ‣ G.3 Sequential Generation and Temporal Properties ‣ Appendix G Financial Log-Return Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") gives the pseudocode.

Algorithm 3  MALA Warm-Start Sequential Return Generation

0: Scaled memory matrix 𝐗∈ℝd×K\mathbf{X}\in\mathbb{R}^{d\times K}, raw memory matrix 𝐌∈ℝd×K\mathbf{M}\in\mathbb{R}^{d\times K}, inverse temperature β\beta, step size α\alpha, inner steps TinnerT\_{\text{inner}}, number of days TdaysT\_{\text{days}}

0: Synthetic return matrix 𝐆^∈ℝTdays×d\hat{\mathbf{G}}\in\mathbb{R}^{T\_{\text{days}}\times d}

1: k∼Uniform​{1,…,K}k\sim\mathrm{Uniform}\{1,\dots,K\}

2: 𝝃←𝐗:,k+0.01​𝜼,𝜼∼𝒩​(𝟎,𝐈d)\boldsymbol{\xi}\leftarrow\mathbf{X}\_{:,k}+0.01\,\boldsymbol{\eta},\quad\boldsymbol{\eta}\sim\mathcal{N}(\mathbf{0},\mathbf{I}\_{d}) ⊳\triangleright initialize near random memory

3: for t=1,2,…,Tdayst=1,2,\dots,T\_{\text{days}} do

4:  Run TinnerT\_{\text{inner}} steps of Algorithm [2](#alg2 "Algorithm 2 ‣ Appendix C MALA Variant of Stochastic Attention ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") from 𝝃\boldsymbol{\xi}; set 𝝃←\boldsymbol{\xi}\leftarrow endpoint ⊳\triangleright warm-start

5:  𝐆^t,:←𝐌​softmax⁡(β​𝐗⊤​𝝃)\hat{\mathbf{G}}\_{t,:}\leftarrow\mathbf{M}\,\operatorname{softmax}(\beta\,\mathbf{X}^{\top}\boldsymbol{\xi}) ⊳\triangleright project to growth-rate space

6: end for

We generated Tdays=2,766T\_{\text{days}}=2{,}766 synthetic trading days (matching the historical sample size) with Tinner=200T\_{\text{inner}}=200, α=0.01\alpha=0.01, and β=12\beta=12. The mean MALA acceptance rate was 99.4%, confirming that the ULA discretization bias is negligible at this operating point.

#### Stylized Fact 2: Near-zero return autocorrelation.

Figure [11](#A7.F11 "Figure 11 ‣ Summary. ‣ G.3 Sequential Generation and Temporal Properties ‣ Appendix G Financial Log-Return Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") (top row) showed the autocorrelation function of raw returns for five representative tickers. The generated ACF (blue) lay within the 99% confidence interval for white noise at all lags ≥1\geq 1, matching the historical pattern (red).

#### Stylized Fact 3: Volatility clustering.

Figure [11](#A7.F11 "Figure 11 ‣ Summary. ‣ G.3 Sequential Generation and Temporal Properties ‣ Appendix G Financial Log-Return Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") (bottom row) showed the autocorrelation function of squared returns. The historical series (red) exhibits the characteristic slow-decaying positive autocorrelation of volatility clustering. The generated series (blue), however, showed ACF(g2g^{2}) ≈0\approx 0 at all lags; the sampler did not reproduce this effect. We verified that at the main operating point (β=25\beta{=}25, Tinner=2,000T\_{\text{inner}}{=}2{,}000), ACF(g2g^{2}) also collapses to ≈0{\approx}0 (mean over 424424 tickers: 0.00050.0005), confirming this is a property of equilibrium sampling and not an artifact of the choice of β\beta.

This is a fundamental limitation of equilibrium Boltzmann sampling, not a tuning failure. The stochastic attention sampler targets the stationary distribution pβ∝exp⁡(−β​E)p\_{\beta}\propto\exp(-\beta E) at fixed β\beta. At stationarity, the variance of each day’s output is governed by the static energy landscape and the fixed temperature; there is no mechanism for the return variance to change systematically over time. Volatility clustering in real markets arises from non-stationary dynamics: regime shifts driven by exogenous shocks, feedback loops between volatility and leverage, and time-varying risk premia [[3](#bib.bib26 "Empirical properties of asset returns: stylized facts and statistical issues")]. Reproducing these effects within the Langevin framework would require introducing explicit temporal structure, for instance a time-varying inverse temperature β​(t)\beta(t) that creates exogenous volatility regimes, or coupling the sampler to a latent regime-switching process. These extensions are natural directions for future work.

#### Summary.

Table [6](#A7.T6 "Table 6 ‣ Summary. ‣ G.3 Sequential Generation and Temporal Properties ‣ Appendix G Financial Log-Return Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") made three theoretical predictions concrete. *First*, the novelty–fidelity trade-off is real and quantified: SA generates regime interpolations absent from the historical record (𝒩=0.768±0.001\mathcal{N}=0.768\pm 0.001) while bootstrap, which replays history verbatim, achieves 𝒩=0.000\mathcal{N}=0.000; marginal fidelity runs in the opposite direction (64.2%64.2\% vs. 99.3%99.3\% KS pass). *Second*, the Hopfield energy captures cross-sectional dependence independently of marginals: Frobenius error 26.3%26.3\% is unchanged by per-ticker affine correction, confirming that the energy geometry encodes correlation structure, not scale. *Third*, volatility clustering, a non-stationary phenomenon driven by regime shifts and leverage feedback [[3](#bib.bib26 "Empirical properties of asset returns: stylized facts and statistical issues")], is exactly what a fixed-β\beta equilibrium sampler cannot reproduce; the absence is a theoretical prediction confirmed by experiment, not a tuning failure.

Table 6: Finance experiment: principled trade-offs of equilibrium Boltzmann sampling. SA and bootstrap occupy opposite ends of a novelty–fidelity spectrum: SA generates novel regime interpolations (𝒩=0.768±0.001\mathcal{N}=0.768\pm 0.001) that bootstrap cannot produce, while bootstrap preserves marginals by construction. The Frobenius correlation error is identical before and after affine correction, confirming the energy captures dependence independently of scale. Temporal metrics apply to the sequential MALA experiment only.

|  |  |  |
| --- | --- | --- |
| Property | SA (corrected) | Bootstrap |
| Distributional fidelity (i.i.d. pool, 900 samples) | | |
| KS pp-value (mean; 64.2% pass at 5%5\%) | 0.193 | 0.622 |
| Cross-asset Frobenius error | 26.3% | 15.6% |
| Novelty (1−maxk⁡cos1-\max\_{k}\cos) | 0.768±0.0010.768\pm 0.001 | 0.000 |
| Temporal properties (MALA warm-start, 2766 days) | | |
| SF2: Return unpredictability | Reproduced [ACF(gg) in 99% CI, β=12\beta{=}12] | N/A |
| SF3: Volatility clustering | Not reproduced (β=12\beta{=}12) | N/A |



![Refer to caption](2603.06875v1/x6.png)

![Refer to caption](2603.06875v1/x7.png)

Figure 11: Stylized Facts 2 and 3: Autocorrelation analysis for five S&P 500 tickers.
Top row: ACF(gg): the generated series (blue) stays within the 99% confidence band (dashed) at all lags, matching the near-zero autocorrelation of historical returns (red).
Bottom row: ACF(g2g^{2}): the historical series (red) shows persistent positive autocorrelation characteristic of volatility clustering, while the generated series (blue) shows ACF(g2g^{2}) ≈0\approx 0, reflecting the absence of non-stationary dynamics in the equilibrium sampler.

## Appendix H Simpsons Character Face Generation

To test whether the stochastic attention sampler generalizes from grayscale digit images to structured natural images at larger scale, we applied Algorithm [1](#alg1 "Algorithm 1 ‣ 4.1 Stochastic Attention Update ‣ 4 Method ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") to a corpus of 1,0001{,}000 Simpsons character face images, each downsampled to 64×6464\times 64 pixels and converted to grayscale, yielding pattern vectors in ℝd\mathbb{R}^{d} with d=4,096d=4{,}096, a 5.2×5.2\times scale-up over the MNIST experiment (d=784d=784).

#### Data and setup.

We selected K=100K=100 images uniformly at random (fixed seed), matching the MNIST memory bank size to enable direct metric comparison. Each image was flattened in row-major order and normalized to unit ℓ2\ell\_{2} norm to form the memory matrix 𝐗∈ℝ4096×100\mathbf{X}\in\mathbb{R}^{4096\times 100} (load ratio K/d≈0.024K/d\approx 0.024, well below capacity).

#### Choosing β\beta via the SNR rule.

At d=4,096d=4{,}096, the MNIST value β=2,000\beta=2{,}000 gives SNR=α​β/(2​d)≈0.049\mathrm{SNR}=\sqrt{\alpha\beta/(2d)}\approx 0.049, half the MNIST operating point (SNR≈0.113\mathrm{SNR}\approx 0.113). At this lower SNR the noise overwhelms the gradient, inflating the chain norm above unity and placing samples far from the memory manifold (empirically: energy ≈+0.53\approx+0.53). The SNR rule gives

|  |  |  |
| --- | --- | --- |
|  | β=SNRMNIST2⋅2​dα=0.01276×2×40960.01≈10,449.\beta=\mathrm{SNR}\_{\mathrm{MNIST}}^{2}\cdot\frac{2d}{\alpha}=0.01276\times\frac{2\times 4096}{0.01}\approx 10{,}449. |  |

We used β=10,000\beta=10{,}000 (SNR=0.110\mathrm{SNR}=0.110), recovering the MNIST operating point. All other hyperparameters were identical to the MNIST experiment: α=0.01\alpha=0.01, 30 independent chains initialized near distinct stored patterns (σinit=0.01\sigma\_{\mathrm{init}}=0.01), T=5,000T=5{,}000 iterations, burn-in 2,0002{,}000, thin every 100 then sub-sample 5 per chain, yielding 30×5=15030\times 5=150 samples per method. The MALA acceptance rate exceeded 99%, confirming that ULA discretization bias is negligible.

#### Temperature spectrum.

Figure [12](#A8.F12 "Figure 12 ‣ Temperature spectrum. ‣ Appendix H Simpsons Character Face Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") showed four samples at each of six inverse temperatures spanning β∈{500,1000,2000,5000,10000,20000}\beta\in\{500,1000,2000,5000,10000,20000\}, corresponding to SNR∈{0.025,0.035,0.049,0.078,0.110,0.156}\mathrm{SNR}\in\{0.025,0.035,0.049,0.078,0.110,0.156\}. The noise-to-retrieval transition tracked SNR, not the raw β\beta value: rows below SNR≈0.05\mathrm{SNR}\approx 0.05 show diffuse gray images, while rows at SNR≥0.110\mathrm{SNR}\geq 0.110 yield recognizable character faces.

![Refer to caption](2603.06875v1/figs/Fig_simpsons_beta_spectrum.png)


Figure 12: Temperature spectrum for Simpsons character images (K=100K{=}100, d=4,096d{=}4{,}096, α=0.01\alpha{=}0.01). Each row shows 4 SA samples at one inverse temperature; rows are ordered from high β\beta (top, β=20,000\beta{=}20{,}000, SNR=0.156\mathrm{SNR}{=}0.156) to low β\beta (bottom, β=500\beta{=}500, SNR=0.025\mathrm{SNR}{=}0.025). The operating point β=10,000\beta{=}10{,}000 (SNR=0.110\mathrm{SNR}{=}0.110, row 2 from top) reproduces the MNIST SNR and yields structured character faces.

#### Quantitative comparison.

Table [7](#A8.T7 "Table 7 ‣ Quantitative comparison. ‣ Appendix H Simpsons Character Face Generation ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") reported metrics for all five methods at β=10,000\beta=10{,}000. The relative ranking matched the MNIST experiment exactly: SA and MALA dominated all non-Langevin baselines on every axis simultaneously, and both Langevin methods were statistically indistinguishable. SA novelty (0.159±0.0000.159\pm 0.000) was comparable to the MNIST value (0.152±0.0010.152\pm 0.001); mean energy (−0.293±0.000-0.293\pm 0.000) confirmed that samples lay on the memory manifold. Diversity was lower than MNIST (0.2930.293 vs. 0.6000.600), but this reflected the higher inter-pattern correlation of face images rather than a failure of the sampler: bootstrap diversity (0.1170.117) was likewise far below the MNIST value (0.4590.459), indicating that the stored patterns themselves were more concentrated in the Simpsons corpus.

Table 7: Quantitative comparison on Simpsons character faces (K=100K{=}100, d=4,096d{=}4{,}096, β=10,000\beta{=}10{,}000, SNR=0.110\mathrm{SNR}=0.110). Same protocol as Table [1](#S5.T1 "Table 1 ‣ Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.") except GMM-PCA and VAE are omitted: at d=4,096d{=}4{,}096 with only K=100K{=}100 training patterns, both methods are degenerate (GMM covariance is rank-deficient; VAE encoder–decoder cannot generalize from 100 examples in 4,096 dimensions). MALA acceptance rate: >99%>99\%. Values are mean ±\pm SE across 30 chains. Lower diversity relative to MNIST reflects higher inter-pattern correlation of face images (bootstrap diversity 0.1170.117 vs. 0.4590.459 for digit “3”).

| Method | 𝒩\mathcal{N} ↑\uparrow | 𝒟¯\bar{\mathcal{D}} ↑\uparrow | E¯\bar{E} ↓\downarrow |
| --- | --- | --- | --- |
| Bootstrap (replay) | 0.000±0.0000.000\pm 0.000 | 0.117±0.0050.117\pm 0.005 | −0.500±0.000-0.500\pm 0.000 |
| Gaussian perturbation | 0.004±0.0000.004\pm 0.000 | 0.124±0.0040.124\pm 0.004 | −0.496±0.000-0.496\pm 0.000 |
| Random convex combination | 0.018±0.0000.018\pm 0.000 | 0.001±0.0000.001\pm 0.000 | −0.482±0.000-0.482\pm 0.000 |
| MALA | 0.157±0.0000.157\pm 0.000 | 0.289±0.0010.289\pm 0.001 | −0.296±0.000-0.296\pm 0.000 |
| Stochastic attention | 0.159±0.000\mathbf{0.159\pm 0.000} | 0.293±0.001\mathbf{0.293\pm 0.001} | −0.293±0.000\mathbf{-0.293\pm 0.000} |



![Refer to caption](2603.06875v1/figs/Fig_simpsons_grid_bootstrap.png)

![Refer to caption](2603.06875v1/figs/Fig_simpsons_grid_gaussian.png)

![Refer to caption](2603.06875v1/figs/Fig_simpsons_grid_convex.png)

![Refer to caption](2603.06875v1/figs/Fig_simpsons_grid_mala.png)

![Refer to caption](2603.06875v1/figs/Fig_simpsons_grid_sa.png)

(a) Bootstrap (b) Gaussian (c) Convex (d) MALA (e) Ours

Figure 13: Generated Simpsons character face samples (4×44{\times}4 grids, d=4,096d{=}4{,}096, β=10,000\beta{=}10{,}000). The qualitative pattern mirrors MNIST: only the Langevin-based methods (d, e) produce diverse, structured face images.

## Appendix I Baseline Method Specifications

This section gives complete mathematical specifications for the two learned generative
baselines in Table [1](#S5.T1 "Table 1 ‣ Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git."): GMM-PCA and the VAE.
All hyperparameters reported here were used without modification in the experiments;
the implementation is publicly available in code/mnist-experiment/ and
code/vae-experiment/ in the accompanying repository.

### I.1 GMM-PCA

#### Dimensionality reduction.

Let 𝐗∈ℝd×K\mathbf{X}\in\mathbb{R}^{d\times K} be the column-normalized memory matrix
(d=784d{=}784, K=100K{=}100). Compute the economy SVD
𝐗=𝐔​𝚺​𝐕⊤\mathbf{X}=\mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^{\!\top} and retain the top
r=50r{=}50 left singular vectors, forming 𝐔r∈ℝd×r\mathbf{U}\_{r}\in\mathbb{R}^{d\times r}.
Project each stored pattern to a low-dimensional code:
𝐳k=𝐔r⊤​𝐦k∈ℝr\mathbf{z}\_{k}=\mathbf{U}\_{r}^{\!\top}\mathbf{m}\_{k}\in\mathbb{R}^{r}, k=1,…,Kk=1,\dots,K.
For the digit “3” memory matrix, the top 50 components capture >>95% of total variance.

#### Gaussian mixture model.

Fit a C=10C{=}10 component GMM with *diagonal* covariance to the code matrix
𝐙=[𝐳1​|⋯|​𝐳K]∈ℝr×K\mathbf{Z}{=}[\mathbf{z}\_{1}|\cdots|\mathbf{z}\_{K}]\in\mathbb{R}^{r\times K} via
Expectation-Maximization [[5](#bib.bib32 "Maximum likelihood from incomplete data via the EM algorithm")]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(𝐳)=∑c=1Cπc​𝒩​(𝐳;𝝁c,diag​(𝝈c2)),∑c=1Cπc=1,πc≥0.p(\mathbf{z})=\sum\_{c=1}^{C}\pi\_{c}\,\mathcal{N}\!\bigl(\mathbf{z};\,\boldsymbol{\mu}\_{c},\,\mathrm{diag}(\boldsymbol{\sigma}\_{c}^{2})\bigr),\quad\sum\_{c=1}^{C}\pi\_{c}=1,\quad\pi\_{c}\geq 0. |  | (19) |

Parameters {πc,𝝁c,𝝈c2}c=1C\{\pi\_{c},\boldsymbol{\mu}\_{c},\boldsymbol{\sigma}\_{c}^{2}\}\_{c=1}^{C} are estimated
by EM with K-means++ initialization and convergence tolerance 10−810^{-8} on the
log-likelihood.
The diagonal-covariance constraint prevents singularity when K>rK>r and is equivalent to
assuming conditionally independent PCA coordinates within each component.

#### Sampling.

To draw one sample: (i) sample component c∼Categorical​(𝝅)c\sim\mathrm{Categorical}(\boldsymbol{\pi});
(ii) sample 𝐳~∼𝒩​(𝝁c,diag​(𝝈c2))\tilde{\mathbf{z}}\sim\mathcal{N}(\boldsymbol{\mu}\_{c},\mathrm{diag}(\boldsymbol{\sigma}\_{c}^{2}));
(iii) reconstruct 𝝃^=𝐔r​𝐳~\hat{\boldsymbol{\xi}}=\mathbf{U}\_{r}\tilde{\mathbf{z}} and
renormalize to unit ℓ2\ell\_{2} norm.
The 150 evaluation samples are drawn i.i.d. under this procedure with a fixed seed.

#### Hyperparameters.

r=50r{=}50 PCA components; C=10C{=}10 GMM components; K-means++ initialization;
EM convergence tolerance 10−810^{-8}; no regularization beyond the diagonal-covariance constraint.

### I.2 Variational Autoencoder

#### Architecture.

The encoder maps 𝐱∈ℝ784\mathbf{x}\in\mathbb{R}^{784} to the parameters of an approximate posterior:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐡1\displaystyle\mathbf{h}\_{1} | =ReLU​(𝐖1​𝐱+𝐛1),𝐖1∈ℝ256×784,\displaystyle=\mathrm{ReLU}(\mathbf{W}\_{1}\mathbf{x}+\mathbf{b}\_{1}),\quad\mathbf{W}\_{1}\in\mathbb{R}^{256\times 784}, |  | (20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐡2\displaystyle\mathbf{h}\_{2} | =ReLU​(𝐖2​𝐡1+𝐛2),𝐖2∈ℝ128×256,\displaystyle=\mathrm{ReLU}(\mathbf{W}\_{2}\mathbf{h}\_{1}+\mathbf{b}\_{2}),\quad\mathbf{W}\_{2}\in\mathbb{R}^{128\times 256}, |  | (21) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝝁ϕ​(𝐱)\displaystyle\boldsymbol{\mu}\_{\phi}(\mathbf{x}) | =𝐖μ​𝐡2+𝐛μ,𝐖μ∈ℝ8×128,\displaystyle=\mathbf{W}\_{\mu}\mathbf{h}\_{2}+\mathbf{b}\_{\mu},\quad\mathbf{W}\_{\mu}\in\mathbb{R}^{8\times 128}, |  | (22) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | log⁡𝝈ϕ2​(𝐱)\displaystyle\log\boldsymbol{\sigma}^{2}\_{\phi}(\mathbf{x}) | =𝐖σ​𝐡2+𝐛σ,𝐖σ∈ℝ8×128.\displaystyle=\mathbf{W}\_{\sigma}\mathbf{h}\_{2}+\mathbf{b}\_{\sigma},\quad\mathbf{W}\_{\sigma}\in\mathbb{R}^{8\times 128}. |  | (23) |

The decoder is architecturally symmetric: 8→128→256→7848\to 128\to 256\to 784, with ReLU activations on
hidden layers and a linear output.
All weight matrices are Glorot-uniform initialized; biases are zero-initialized.
The decoder output is renormalized to unit ℓ2\ell\_{2} norm before computing metrics, matching
the normalization convention of all other methods in Table [1](#S5.T1 "Table 1 ‣ Image generation on MNIST. ‣ 5 Experiments ‣ Stochastic Attention via Langevin Dynamics on the Modern Hopfield EnergyRepository: https://github.com/varnerlab/stochastic-attention-study-paper.git.").

#### Objective.

We minimize the β\beta-VAE objective [[9](#bib.bib30 "Beta-VAE: Learning basic visual concepts with a constrained variational framework")]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(ϕ,θ;𝐱)=‖𝐱−𝐱^θ​(𝐳)‖22⏟reconstruction+βKL​DKL​(qϕ​(𝐳|𝐱)∥𝒩​(𝟎,𝐈))⏟regularization,\mathcal{L}(\phi,\theta;\mathbf{x})=\underbrace{\bigl\lVert\mathbf{x}-\hat{\mathbf{x}}\_{\theta}(\mathbf{z})\bigr\rVert\_{2}^{2}}\_{\text{reconstruction}}+\;\beta\_{\mathrm{KL}}\underbrace{D\_{\mathrm{KL}}\!\bigl(q\_{\phi}(\mathbf{z}|\mathbf{x})\,\big\|\,\mathcal{N}(\mathbf{0},\mathbf{I})\bigr)}\_{\text{regularization}}, |  | (24) |

where qϕ​(𝐳|𝐱)=𝒩​(𝝁ϕ​(𝐱),diag​(𝝈ϕ2​(𝐱)))q\_{\phi}(\mathbf{z}|\mathbf{x})=\mathcal{N}(\boldsymbol{\mu}\_{\phi}(\mathbf{x}),\mathrm{diag}(\boldsymbol{\sigma}^{2}\_{\phi}(\mathbf{x}))) and the reparameterization trick
𝐳=𝝁ϕ​(𝐱)+𝝈ϕ​(𝐱)⊙ϵ\mathbf{z}=\boldsymbol{\mu}\_{\phi}(\mathbf{x})+\boldsymbol{\sigma}\_{\phi}(\mathbf{x})\odot\boldsymbol{\epsilon}, ϵ∼𝒩​(𝟎,𝐈)\boldsymbol{\epsilon}\sim\mathcal{N}(\mathbf{0},\mathbf{I}),
enables gradient flow through the sampling step.
The KL term has a closed form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | DKL=12​∑j=18[μϕ,j2+σϕ,j2−log⁡σϕ,j2−1].D\_{\mathrm{KL}}=\tfrac{1}{2}\sum\_{j=1}^{8}\bigl[\mu\_{\phi,j}^{2}+\sigma\_{\phi,j}^{2}-\log\sigma\_{\phi,j}^{2}-1\bigr]. |  | (25) |

#### Two-phase training protocol.

Training directly with the full β\beta-VAE objective on a small dataset (K=100K{=}100)
causes *posterior collapse*: the encoder ignores the input, the KL term drives every
latent dimension to 𝒩​(0,1)\mathcal{N}(0,1), and the decoder learns a constant map.
We prevent this with a two-phase schedule:

1. 1.

   Warm-up (epochs 1–2,000): Train with βKL=0\beta\_{\mathrm{KL}}{=}0
   (reconstruction-only autoencoder objective). This establishes a non-degenerate
   encoder (one that uses the latent code productively) before any regularization pressure
   is applied.
2. 2.

   Fine-tuning (epochs 2,001–4,000): Introduce the KL term with
   βKL=0.0001\beta\_{\mathrm{KL}}{=}0.0001 and a linear warmup schedule
   (βKL​(t)=0.0001⋅(t/2000)\beta\_{\mathrm{KL}}(t)=0.0001\cdot(t/2000) for t∈[1,2000]t\in[1,2000]).
   The small final weight provides light regularization toward the Gaussian prior without
   overriding the reconstruction signal.

The warm-up phase is equivalent to a hard β\beta-annealing schedule and is standard practice
for low-data VAE training [[20](#bib.bib31 "Don’t blame the ELBO! A linear VAE perspective on posterior collapse")].
On large datasets (K≫104K\gg 10^{4}), the reconstruction gradient swamps the KL term and posterior
collapse does not occur; the two-phase protocol is needed here specifically because
K=100K{=}100 makes the per-sample gradients noisy relative to the KL regularization pressure.

#### Optimization and sampling.

Optimizer: Adam [[15](#bib.bib29 "Adam: A method for stochastic optimization")] with learning rate 10−310^{-3},
β1=0.9\beta\_{1}{=}0.9, β2=0.999\beta\_{2}{=}0.999, ε=10−8\varepsilon{=}10^{-8}, batch size K=100K{=}100
(full-dataset batches throughout).
No weight decay, dropout, or data augmentation was applied.
At evaluation time, 150 samples are drawn by sampling
𝐳∼𝒩​(𝟎,𝐈8)\mathbf{z}\sim\mathcal{N}(\mathbf{0},\mathbf{I}\_{8}) and decoding
𝐱^=𝐱^θ​(𝐳)\hat{\mathbf{x}}=\hat{\mathbf{x}}\_{\theta}(\mathbf{z}), then renormalizing to unit norm.

#### Hyperparameter selection.

The final configuration (latent dim 8, βKL=0.0001\beta\_{\mathrm{KL}}{=}0.0001) was chosen by a
grid search over latent dimension ∈{4,8,16,32}\in\{4,8,16,32\} and βKL∈{0.1,0.01,0.001,0.0001}\beta\_{\mathrm{KL}}\in\{0.1,0.01,0.001,0.0001\},
evaluating novelty and diversity on the held-out generation protocol.
Latent dim 8 with βKL=0.0001\beta\_{\mathrm{KL}}{=}0.0001 achieved 𝒩=0.214±0.005\mathcal{N}{=}0.214\pm 0.005,
𝒟¯=0.441±0.008\bar{\mathcal{D}}{=}0.441\pm 0.008, outperforming all other static baselines including
GMM-PCA (𝒩=0.198\mathcal{N}{=}0.198, 𝒟¯=0.419\bar{\mathcal{D}}{=}0.419).
Smaller latent dimensions or larger βKL\beta\_{\mathrm{KL}} values degraded novelty and
diversity, while larger latent dimensions showed posterior collapse symptoms
(diversity collapsing to 𝒟¯<0.05\bar{\mathcal{D}}{<}0.05 at latent dim 32 with βKL=0.01\beta\_{\mathrm{KL}}{=}0.01).

BETA