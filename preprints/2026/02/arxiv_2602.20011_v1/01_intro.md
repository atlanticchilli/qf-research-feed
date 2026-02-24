---
authors:
- Stefano De Marco
- Huyên Pham
- Davide Zanni
doc_id: arxiv:2602.20011v1
family_id: arxiv:2602.20011
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Schrödinger bridges with jumps for time series generation This work is supported
  by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of
  Quantitative Finance", the Chair “Risques Financiers", by FiME, Laboratoire de Finance
  des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB
  Chair.
url_abs: http://arxiv.org/abs/2602.20011v1
url_html: https://arxiv.org/html/2602.20011v1
venue: arXiv q-fin
version: 1
year: 2026
---


Stefano De Marco
 Huyên Pham
 Davide Zanni
CMAP, École Polytechnique, Institut Polytechnique de Paris, Email: stefano.de-marco@polytechnique.eduCMAP, École Polytechnique, Institut Polytechnique de Paris, Email: huyen.pham@polytechnique.eduCMAP, École Polytechnique, Institut Polytechnique de Paris, Email: davide.zanni@polytechnique.edu

(February 23, 2026)

###### Abstract

We study generative modeling for time series using entropic optimal transport and the Schrödinger bridge (SB) framework, with a focus on applications in finance and energy modeling.
Extending the diffusion-based approach of Hamdouche, Henry-Labordère, Pham, [[17](https://arxiv.org/html/2602.20011v1#bib.bib5 "Generative modeling for time series via Schrödinger bridge")], we introduce a jump–diffusion Schrödinger bridge model that allows for discontinuities in the generative dynamics.
Starting from a Schrödinger bridge entropy minimization problem, we reformulate the task as a stochastic control problem whose solution characterizes the optimal controlled jump–diffusion process. When sampled on a fixed time grid, this process generates synthetic time series matching the joint distributions of the observed data.

The model is fully data-driven, as both the drift and the jump intensity are learned directly from the data. We propose practical algorithms for training, sampling, and hyperparameter calibration. Numerical experiments on simulated and real datasets, including financial and energy time series, show that incorporating jumps substantially improves the realism of the generated data, in particular by capturing abrupt movements, heavy tails, and regime changes that diffusion-only models fail to reproduce. Comparisons with state-of-the-art generative models highlight the benefits and limitations of the proposed approach.

Keywords:
Schrödinger bridge; entropic optimal transport; jump processes; stochastic control; Lévy-driven dynamics; time series generation.
  
Mathematics Subject Classification: 91G80, 49Q22.

## 1 Introduction

##### Generative modeling task.

Generative models have gained increasing attention in machine learning and applied probability. The task of learning the underlying data distribution to synthesize realistic and novel samples has become crucial across diverse domains, such as the generation of high-fidelity images, coherent text, complex videos or molecular structures. Contemporary architectures generally fall into three categories: flow-matching models [[25](https://arxiv.org/html/2602.20011v1#bib.bib36 "Flow matching for generative modeling")], based on learning a velocity field to find a deterministic flow which moves a source distribution (usually Gaussian) to the target distribution; denoising diffusion models [[19](https://arxiv.org/html/2602.20011v1#bib.bib33 "Denoising diffusion probabilistic models"), [32](https://arxiv.org/html/2602.20011v1#bib.bib35 "Score-based generative modeling through stochastic differential equations")], built through the reversion of a Markov chain or a diffusion SDE, often relying on learning the score function of the data distribution; Generative Adversarial Networks (GANs) [[15](https://arxiv.org/html/2602.20011v1#bib.bib34 "Generative adversarial nets")], written as a zero-sum game between a generator and a discriminator. In quantitative finance the realistic simulation of financial time series has attracted increasing interest in risk management, portfolio construction, stress testing, and scenario generation. Traditional parametric models frequently fail to capture the complex and empirical stylized facts of financial data, thereby motivating the shift toward data-driven generative approaches. However, faithfully reproducing these temporal dependencies remains a significant challenge, and universally accepted evaluation metrics for synthetic financial data are still missing. See [[7](https://arxiv.org/html/2602.20011v1#bib.bib32 "Synthetic data for portfolios: A throw of the dice will never abolish chance")] for a complete overview.

In this work, we focus on generative modeling for time series based on optimal transport (OT) techniques. OT-based approaches seek to identify a transport mechanism that optimally moves a reference distribution into the empirical data distribution, minimizing a transport cost while preserving the structure of the data. This framework enables generative modeling by directly learning an optimal transport map or coupling, bypassing the need for adversarial training or the inversion of complex stochastic dynamics. Early explorations of this idea include training generative models by minimizing OT-based metrics like Sinkhorn divergences [[13](https://arxiv.org/html/2602.20011v1#bib.bib39 "Learning generative models with Sinkhorn divergences")]. Subsequent works have aimed to directly learn the optimal transport maps, such as through continuous-time Neural ODE flows [[29](https://arxiv.org/html/2602.20011v1#bib.bib38 "Ot-flow: Fast and accurate continuous normalizing flows via optimal transport")] or neural approximations of the Monge map [[22](https://arxiv.org/html/2602.20011v1#bib.bib40 "Neural optimal transport")]. Specifically for time series, causal optimal transport has been introduced to specifically reproduce temporal dependencies and causal structures rather than merely matching static marginal distributions [[33](https://arxiv.org/html/2602.20011v1#bib.bib12 "Cot-gan: Generating sequential data via causal optimal transport")]. Our work extends this domain by proposing a novel generative model built upon a specific, powerful optimal transport technique: the Schrödinger bridge (SB) problem.

##### The Schrödinger bridge problem.

The Schrödinger bridge problem, first introduced by E. Schrödinger in the 1930s, is an entropy minimization problem that seeks to find the probability measure that is "as close as possible" to another reference probability, while satisfying prescribed marginal distributions. Formally, consider a reference path measure ℚ\mathbb{Q} on the space Ω=C​([0,1],ℝd)\Omega=C([0,1],\mathbb{R}^{d}), typically fixed as the Wiener measure, under which the canonical process X=(Xt)t≥0X=(X\_{t})\_{t\geq 0} is a Brownian motion. The dynamic Schrödinger bridge problem is then formulated as

|  |  |  |
| --- | --- | --- |
|  | infℙ∈𝒫​(Ω):P0=μ0,P1=μ1H​(ℙ|ℚ),\inf\_{\mathbb{P}\in\mathcal{P}(\Omega):\,P\_{0}=\mu\_{0},\,P\_{1}=\mu\_{1}}H(\mathbb{P}|\mathbb{Q}), |  |

where H​(ℙ|ℚ)H(\mathbb{P}|\mathbb{Q}) is the relative entropy (Kullback-Leibler divergence) between the two path measures, P0=ℙ∘X0−1P\_{0}=\mathbb{P}\circ X\_{0}^{-1}, P1=ℙ∘X1−1P\_{1}=\mathbb{P}\circ X\_{1}^{-1}, and μ0\mu\_{0} and μ1\mu\_{1} are the prescribed initial and terminal marginal distributions belonging to 𝒫​(ℝd)\mathcal{P}(\mathbb{R}^{d}). The solution ℙ∗\mathbb{P}^{\*} is the probability law of a unique, constrained stochastic process that transports the initial distribution μ0\mu\_{0} to the target distribution μ1\mu\_{1} in an entropy-optimal way relative to the reference measure ℚ\mathbb{Q}. The static counterpart of the problem is defined on the space of probabilities 𝒫​(ℝd)\mathcal{P}(\mathbb{R}^{d}) as

|  |  |  |
| --- | --- | --- |
|  | infπ∈Π​(μ0,μ1)H​(π|Q01)\inf\_{\pi\in\Pi(\mu\_{0},\mu\_{1})}H(\pi|Q\_{01}) |  |

where Q01​(d​x​d​y)=ℚ​((X0,X1)∈d​x​d​y)Q\_{01}(\mathrm{d}x\,\mathrm{d}y)=\mathbb{Q}((X\_{0},X\_{1})\in\mathrm{d}x\,\mathrm{d}y) is the joint law of the initial and final position of the reference process, and Π​(μ0,μ1)\Pi(\mu\_{0},\mu\_{1}) denotes the set of couplings with marginals μ0\mu\_{0} and μ1\mu\_{1}. The classical Schrödinger bridge problem has been extensively studied: we refer to Léonard [[23](https://arxiv.org/html/2602.20011v1#bib.bib4 "A survey of the Schrödinger problem and some of its connections with optimal transport")] for a comprehensive overview of the Schrödinger bridge problem, including classical solution methods, dual formulation, and the characterization of the solution in terms of Schrödinger potentials. In this paper, we are interested in the application of the Schrödinger bridge problem to financial modeling and its extension to processes with discontinuities. This extension has been recently explored in depth in [[36](https://arxiv.org/html/2602.20011v1#bib.bib16 "Schrödinger Bridge Problem for Jump Diffusions"), [37](https://arxiv.org/html/2602.20011v1#bib.bib17 "The Schrödinger Bridge Problem for Jump Diffusions with Regime Switching")], where the authors define the minimization problem over the space of path measures on càdlàg trajectories, choosing as reference measure the law of a Lévy-Itô process. They provide the explicit characterization of the solution via the associated Schrödinger system and its potentials.

An important connection is given by the interpretation of the Schrödinger bridge problem as entropic optimal transport (EOT) problem, which can be viewed as a computationally tractable relaxation of classical optimal transport. Indeed, consider the static Schrödinger bridge problem with a reference measure R∈𝒫​(ℝd×ℝd)R\in\mathcal{P}(\mathbb{R}^{d}\times\mathbb{R}^{d}) of the form

|  |  |  |
| --- | --- | --- |
|  | d​R​(x,y)∝exp⁡(−1ε​c​(x,y))​d​(μ0⊗μ1)​(x,y)\mathrm{d}R(x,y)\propto\exp\left(-\frac{1}{\varepsilon}c(x,y)\right)\mathrm{d}(\mu\_{0}\otimes\mu\_{1})(x,y) |  |

Then minimizing the relative entropy with respect to RR over couplings Π​(μ0,μ1)\Pi(\mu\_{0},\mu\_{1}) is equivalent, up to an additive constant, to the problem

|  |  |  |
| --- | --- | --- |
|  | infπ∈Π​(μ0,μ1)∫c​(x,y)​π​(d​x,d​y)+ε​H​(π|μ0⊗μ1)\inf\_{\pi\in\Pi(\mu\_{0},\mu\_{1})}\int c(x,y)\pi(\mathrm{d}x,\mathrm{d}y)+\varepsilon H(\pi|\mu\_{0}\otimes\mu\_{1}) |  |

where cc is a given cost function and HH the Kullback-Leibler divergence. This formulation, combining a transport cost with an entropic regularization term, is precisely the EOT problem. This formulation, popularized by the work of Cuturi [[9](https://arxiv.org/html/2602.20011v1#bib.bib31 "Sinkhorn distances: Lightspeed computation of optimal transport")], provides the foundation for the well-known Sinkhorn algorithm, which allows to numerically compute the entropy-regularized optimal coupling. By leveraging this connection, various numerical methods for approximating the SB solution have been developed: the Iterative Proportional Fitting (IPF) [[27](https://arxiv.org/html/2602.20011v1#bib.bib28 "Introduction to entropic optimal transport")], that it is based on the Sinkhorn algorithm, the Iterative Markovian Fitting (IMF) [[31](https://arxiv.org/html/2602.20011v1#bib.bib25 "Diffusion Schrödinger bridge matching")], and faster techniques like the Light SB algorithm [[16](https://arxiv.org/html/2602.20011v1#bib.bib37 "Light and optimal schrödinger bridge matching")]. These numerical algorithms are essential for turning the Schrödinger bridge problem theory into a practical tool for generative modeling.

##### Generative models based on Schrödinger bridges.

The Schrödinger bridge technology provides a powerful foundation for the design of generative models. De Bortoli et al. [[12](https://arxiv.org/html/2602.20011v1#bib.bib26 "Diffusion Schrödinger bridge with applications to score-based generative modeling")] was among the first to establish a rigorous connection between the SB problem and score-based generative models, introducing the Diffusion SB as a novel implementation of the IPF algorithm using score-based diffusion techniques. This approach enables the construction of bridges between arbitrary distributions over a finite time horizon, and leads to improved sampling efficiency compared with classical score-based methods. Shi et al. [[31](https://arxiv.org/html/2602.20011v1#bib.bib25 "Diffusion Schrödinger bridge matching")] further developed this line of work by proposing Diffusion Schrödinger Bridge Matching, an algorithm which refines the practical approximation of Schrödinger bridges and offers a more scalable and robust alternative to IPF in high-dimensional settings.

In the context of time series, the Schrödinger bridge problem naturally induces a generative model on the path space. The resulting optimal stochastic process interpolates the joint distribution at fixed dates and, when sampled, produces synthetic time series whose joint finite-dimensional distribution matches those of the observed data. This dynamic optimal transport perspective combines the interpretability of OT with the flexibility of stochastic modeling, making it particularly well suited for generating realistic time series while preserving both distributional and temporal consistency. In financial applications, Labordère [[18](https://arxiv.org/html/2602.20011v1#bib.bib27 "From (Martingale) Schrödinger bridges to a new class of Stochastic Volatility Models")] introduced a martingale formulation of the Schrödinger bridge problem within an entropic optimal transport framework, incorporating martingale constraints that are essential for asset price modeling. Building on this idea, Hamdouche et al. [[17](https://arxiv.org/html/2602.20011v1#bib.bib5 "Generative modeling for time series via Schrödinger bridge")] rigorously defined and implemented a numerical algorithm to reproduce the joint distribution of financial time series using Schrödinger bridges.

In this paper, we extend the work of Hamdouche et al. [[17](https://arxiv.org/html/2602.20011v1#bib.bib5 "Generative modeling for time series via Schrödinger bridge")] to the setting of jump-diffusion processes. Extensions of generative models to dynamics with jumps have been explored, notably by generalizing diffusion-based stochastic differential equations to Lévy-driven dynamics [[34](https://arxiv.org/html/2602.20011v1#bib.bib29 "Score-based generative models with Lévy processes"), [3](https://arxiv.org/html/2602.20011v1#bib.bib30 "Generative modelling with jump-diffusions")]. Such extensions are crucial for capturing heavy-tailed distributions and abrupt movements commonly observed in financial and energy time series. We adopt a similar strategy within the Schrödinger bridge framework by moving beyond the standard Wiener reference and instead considering the law of a process composed of a Brownian motion and a compound Poisson process. This leads to a Schrödinger bridge problem defined on the space of càdlàg paths, and requires new theoretical results for the SB problem to discontinuous dynamics. Beyond its theoretical interest, this extension is strongly motivated by practical considerations: our numerical experiments demonstrate that incorporating jumps substantially improves the realism of the generated time series compared with diffusion-only Schrödinger bridge models, particularly in terms of tail behavior, abrupt variations, and regime changes.

##### Our contributions and organization of the paper.

This paper makes three main contributions:

* •

  First, we introduce a new Schrödinger bridge–based generative model for time series driven by jump–diffusion dynamics. Extending the framework of Hamdouche et al. [[17](https://arxiv.org/html/2602.20011v1#bib.bib5 "Generative modeling for time series via Schrödinger bridge")], we formulate the Schrödinger bridge problem on the space of probability laws of càdlàg processes, allowing the reference measure to be the law of a jump–diffusion process rather than a purely diffusive one.
* •

  Second, we propose a systematic calibration procedure for identifying the key hyperparameters of the Schrödinger bridge generative model, which is essential to ensure numerical stability and robustness across different financial datasets.
* •

  Third, through extensive numerical experiments on both financial and energy time series, we show that incorporating jumps leads to a substantial improvement in generative performance compared with diffusion-only Schrödinger bridge models, notably by better capturing heavy-tailed behavior, abrupt variations, and regime changes observed in real data.

The paper is organized as follows: in Section [2](https://arxiv.org/html/2602.20011v1#S2 "2 Setting and problem formulation ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."), we formulate the Schrödinger bridge problem for time series, and extend it to the setting of jump-diffusion processes. Section [3](https://arxiv.org/html/2602.20011v1#S3 "3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") presents the main theoretical result: Theorem [3.1](https://arxiv.org/html/2602.20011v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") characterizes the solution of the problem and explicitly identify the optimal controlled dynamics of the generative process used to simulate synthetic time series on a fixed time grid. In Section [4](https://arxiv.org/html/2602.20011v1#S4 "4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."), we develop the methodology for estimating the drift and jump intensity of the optimal dynamics, with particular attention to the case where the reference jump component is Gaussian. Section [5](https://arxiv.org/html/2602.20011v1#S5 "5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") introduces two simulation schemes designed for sampling trajectories of the optimal jump-diffusion process, and Section [6](https://arxiv.org/html/2602.20011v1#S6 "6 Hyperparameter tuning ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") describes the calibration procedure used to select the model hyperparameters. In Section [7](https://arxiv.org/html/2602.20011v1#S7 "7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."), we report numerical experiments on both simulated and real-world datasets, including financial and energy time series, presenting qualitative simulations, quantitative performance metrics, and comparisons with state-of-the-art generative models. Finally, Appendix [A](https://arxiv.org/html/2602.20011v1#A1 "Appendix A Predictability and Poisson measures ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") recalls some notions on the predictability of stochastic processes, and Appendix [B](https://arxiv.org/html/2602.20011v1#A2 "Appendix B Additional numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") reports some additional numerical tests.

## 2 Setting and problem formulation

Let d,N∈ℕd,N\in\mathbb{N}, and let μ\mu denote a probability distribution on the space (ℝd)N(\mathbb{R}^{d})^{N}. Assume that the distribution μ\mu is only accessible through a finite set of samples x(1),…,x(M)x^{\mathrm{(1)}},\ldots,x^{\mathrm{(M)}}, each observed on a discrete time grid 𝒯:={ti}i=1,…,N\mathcal{T}:=\{t\_{i}\}\_{i=1,\ldots,N}, where we set T:=tNT:=t\_{N} as the terminal observation horizon. Our aim is to develop a method that enables the generation of new samples from this unknown target distribution μ\mu.

Consider the space Ω=D​([0,T];ℝd)\Omega=D([0,T];\mathbb{R}^{d}) of the càdlàg functions ω:[0,T]→ℝd\omega:[0,T]\to\mathbb{R}^{d}, endowed with the Skorokhod topology, and denote by ℱ\mathcal{F} the associated Borel σ\sigma-algebra. Define the canonical process Xt​(ω)=ω​(t)X\_{t}(\omega)=\omega(t), for t∈[0,T]t\in[0,T], ω∈Ω\omega\in\Omega, with càdlàg paths and X0=0X\_{0}=0. Then the canonical filtration 𝔽=(ℱt)t\mathbb{F}=(\mathcal{F}\_{t})\_{t} is defined by ℱt=σ​(Xs,0≤s≤t)\mathcal{F}\_{t}=\sigma(X\_{s},0\leq s\leq t), that is, the smallest σ\sigma-algebra making the coordinate maps up to time tt measurable. Denoting by 𝒫​(Ω)\mathcal{P}(\Omega) the space of probability measures on Ω\Omega, consider the reference probability ℙ0∈𝒫​(Ω)\mathbb{P}^{0}\in\mathcal{P}(\Omega) being the law of the process defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=X0+σ​Wt0+∫(0,t]×ℝdz​N​(d​t,d​z),t∈[0,T],X\_{t}=X\_{0}+\sigma\,W^{0}\_{t}+\int\_{(0,t]\times\mathbb{R}^{d}}z\,N(\mathrm{d}t,\mathrm{d}z),\quad t\in[0,T], |  | (2.1) |

with X0=0X\_{0}=0, where W0W^{0} is a dd-dimensional Brownian motion, σ∈ℝd×d\sigma\in\mathbb{R}^{d\times d} is an invertible matrix, and N​(d​t,d​z)N(\mathrm{d}t,\mathrm{d}z) is a Poisson random measure on [0,T]×ℝd[0,T]\times\mathbb{R}^{d}, independent of W0W^{0}, with intensity measure

|  |  |  |
| --- | --- | --- |
|  | λ0​ν0​(d​z)​d​t\lambda^{0}\nu^{0}(\mathrm{d}z)\mathrm{d}t |  |

where λ0>0\lambda^{0}>0 is a constant jump intensity and ν0∈𝒫​(ℝd)\nu^{0}\in\mathcal{P}(\mathbb{R}^{d}) is the jump size distribution satisfying ν0​({0})=0\nu^{0}(\{0\})=0; in particular, the jump component has finite activity. Throughout the paper we work under the standing assumption that σ\sigma is non-degenerate and λ0≠0\lambda^{0}\neq 0, unless explicitly stated otherwise. Our goal is to solve the following Schrödinger bridge problem with jumps for time series, which will be denoted by SBJTS.

###### SBJTS problem.

Find ℙ∗∈𝒫​(Ω)\mathbb{P}^{\*}\in\mathcal{P}(\Omega) solution to

|  |  |  |
| --- | --- | --- |
|  | ℙ∗∈arg​minℙ∈𝒫𝒯μ​(Ω)⁡H​(ℙ|ℙ0)\mathbb{P}^{\*}\in\text{arg}\min\_{\mathbb{P}\in\mathcal{P}^{\mu}\_{\mathcal{T}}(\Omega)}H(\mathbb{P}|\mathbb{P}^{0}) |  |

where 𝒫𝒯μ​(Ω)={ℙ∈𝒫​(Ω):ℙ∘(Xt1,…,XtN)−1=μ}\mathcal{P}^{\mu}\_{\mathcal{T}}(\Omega)=\{\mathbb{P}\in\mathcal{P}(\Omega):\mathbb{P}\circ(X\_{t\_{1}},\ldots,X\_{t\_{N}})^{-1}=\mu\}, and H(⋅|⋅)H(\cdot|\cdot) is the Kullback-Leibler divergence between two probability measures defined by

|  |  |  |
| --- | --- | --- |
|  | H​(ℙ|ℙ0)={𝔼ℙ​[ln⁡d​ℙd​ℙ0]if ​ℙ≪ℙ0,+∞otherwise.H(\mathbb{P}|\mathbb{P}^{0})=\begin{cases}\mathbb{E}^{\mathbb{P}}\left[\ln\frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\mathbb{P}^{0}}\right]&\text{if }\mathbb{P}\ll\mathbb{P}^{0},\\ +\infty&\text{otherwise.}\end{cases} |  |

We remark that the structure of our problem coincides with the one introduced in [[17](https://arxiv.org/html/2602.20011v1#bib.bib5 "Generative modeling for time series via Schrödinger bridge")], except that we include an additional compound Poisson term in the dynamics of the process XX under the reference measure ℙ0\mathbb{P}^{0}. This modification provides a natural extension of the original framework, allowing for the presence of jumps.

To solve the SBJTS problem, we consider a stochastic control formulation, following the classical approach of [[10](https://arxiv.org/html/2602.20011v1#bib.bib15 "A stochastic control approach to reciprocal diffusion processes")]. Indeed, given ℙ∈𝒫​(Ω)\mathbb{P}\in\mathcal{P}(\Omega) with finite relative entropy H​(ℙ|ℙ0)<∞H(\mathbb{P}|\mathbb{P}^{0})<\infty, by Girsanov’s theorem (see [léonard, [21](https://arxiv.org/html/2602.20011v1#bib.bib24 "Limit theorems for stochastic processes")]) we can associate to ℙ\mathbb{P} an ℝd\mathbb{R}^{d} valued adapted process α=(αt)t∈[0,T]\alpha=(\alpha\_{t})\_{t\in[0,T]} and an ℝ+\mathbb{R}\_{+} valued predictable process λ=(λt)t∈[0,T]\lambda=(\lambda\_{t})\_{t\in[0,T]} with finite energy

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[12​∫0T‖σ−1​αt‖2​dt+∫(0,T]×ℝd(λt​(z)​ln⁡(λt​(z)λ0)+λ0−λt​(z))​ν0​(d​z)​dt]<∞,\mathbb{E}^{\mathbb{P}}\left[\frac{1}{2}\int\_{0}^{T}\|\sigma^{-1}\alpha\_{t}\|^{2}\mathrm{d}t+\int\_{(0,T]\times\mathbb{R}^{d}}\left(\lambda\_{t}(z)\ln\left(\frac{\lambda\_{t}(z)}{\lambda^{0}}\right)+\lambda^{0}-\lambda\_{t}(z)\right)\nu^{0}(\mathrm{d}z)\mathrm{d}t\right]<\infty, |  | (2.2) |

such that the Radon–Nikodym derivative corresponding to this change of measure is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℙd​ℙ0=exp(∫0T(σ−1αt)⊺dWt0−12∫0T∥σ−1αt∥2dt+∫(0,T]×ℝdln(λt​(z)λ0)N(dt,dz)−∫(0,T]×ℝd(λt(z)−λ0)ν0(dz)dt).\frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\mathbb{P}^{0}}=\exp\Bigg(\int\_{0}^{T}(\sigma^{-1}\alpha\_{t})^{\scriptscriptstyle{\intercal}}\,\mathrm{d}W^{0}\_{t}-\frac{1}{2}\int\_{0}^{T}\|\sigma^{-1}\alpha\_{t}\|^{2}\mathrm{d}t\\ +\int\_{(0,T]\times\mathbb{R}^{d}}\ln\left(\frac{\lambda\_{t}(z)}{\lambda^{0}}\right)N(\mathrm{d}t,\mathrm{d}z)-\int\_{(0,T]\times\mathbb{R}^{d}}(\lambda\_{t}(z)-\lambda^{0})\nu^{0}(\mathrm{d}z)\mathrm{d}t\Bigg). |  | (2.3) |

Moreover, the process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wt0−∫0tσ−1​αs​ds,t∈[0,T]W^{0}\_{t}-\int\_{0}^{t}\sigma^{-1}\alpha\_{s}\mathrm{d}s,\quad t\in[0,T] |  | (2.4) |

is a ℙ\mathbb{P}-Brownian motion, that we will denote by WtW\_{t}, and the process

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫(0,t]×ℝdln⁡(λs​(z)λ0)​N​(d​s,d​z)−∫(0,t]×ℝdλs​(z)​ln⁡(λs​(z)λ0)​ν0​(d​z)​ds,t∈[0,T]\int\_{(0,t]\times\mathbb{R}^{d}}\ln\left(\frac{\lambda\_{s}(z)}{\lambda^{0}}\right)N(\mathrm{d}s,\mathrm{d}z)-\int\_{(0,t]\times\mathbb{R}^{d}}\lambda\_{s}(z)\ln\left(\frac{\lambda\_{s}(z)}{\lambda^{0}}\right)\nu^{0}(\mathrm{d}z)\mathrm{d}s,\quad t\in[0,T] |  | (2.5) |

is a ℙ\mathbb{P}-martingale. Let J​(α,λ)J(\alpha,\lambda) be the functional

|  |  |  |
| --- | --- | --- |
|  | J​(α,λ)=𝔼ℙ​[12​∫0T‖σ−1​αt‖2​dt+∫(0,T]×ℝd(λt​(z)​ln⁡(λt​(z)λ0)−λt​(z)+λ0)​ν0​(d​z)​dt].J(\alpha,\lambda)=\mathbb{E}^{\mathbb{P}}\left[\frac{1}{2}\int\_{0}^{T}\|\sigma^{-1}\alpha\_{t}\|^{2}\mathrm{d}t+\int\_{(0,T]\times\mathbb{R}^{d}}\left(\lambda\_{t}(z)\ln\left(\frac{\lambda\_{t}(z)}{\lambda^{0}}\right)-\lambda\_{t}(z)+\lambda^{0}\right)\nu^{0}(\mathrm{d}z)\mathrm{d}t\right]. |  |

Then substituting ([2.3](https://arxiv.org/html/2602.20011v1#S2.E3 "In 2 Setting and problem formulation ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) into the expression of the Kullback-Leibler divergence of ℙ\mathbb{P} with respect to ℙ0\mathbb{P}^{0}, and using that ([3.10](https://arxiv.org/html/2602.20011v1#S3.E10 "In Proof. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) and ([2.5](https://arxiv.org/html/2602.20011v1#S2.E5 "In 2 Setting and problem formulation ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) are ℙ\mathbb{P}-martingales, we get

|  |  |  |
| --- | --- | --- |
|  | H​(ℙ|ℙ0)=J​(α,λ).H(\mathbb{P}|\mathbb{P}^{0})=J(\alpha,\lambda). |  |

Hence the SBJTS problem is equivalent to the following formulation

|  |  |  |
| --- | --- | --- |
|  | (P)​{minimize over (α,λ)∈𝒜 the functional J​(α,λ)subject to: ​Xt=X0+∫0tαs​ds+σ​Wt+∫(0,t]×ℝdz​N​(d​s,d​z),X0=0ℙ∘(Xt1,…,XtN)−1=μ(\textbf{P})\,\begin{cases}\text{minimize over $(\alpha,\lambda)\in\mathcal{A}$ the functional $J(\alpha,\lambda)$}\\ \text{subject to: }X\_{t}=X\_{0}+\int\_{0}^{t}\alpha\_{s}\,\mathrm{d}s+\sigma\,W\_{t}+\int\_{(0,t]\times\mathbb{R}^{d}}zN(\mathrm{d}s,\mathrm{d}z),\,X\_{0}=0\\ \quad\quad\quad\quad\quad\mathbb{P}\circ(X\_{t\_{1}},\ldots,X\_{t\_{N}})^{-1}=\mu\\ \end{cases} |  |

where

|  |  |  |
| --- | --- | --- |
|  | 𝒜={(α,λ):α:Ω×[0,T]→ℝd​ adapted, ​λ:Ω×[0,T]×ℝd→ℝ+​ predictable, ​J​(α,λ)<∞},\mathcal{A}=\left\{(\alpha,\lambda):\alpha:\Omega\times[0,T]\to\mathbb{R}^{d}\,\text{ adapted, }\lambda:\Omega\times[0,T]\times\mathbb{R}^{d}\to\mathbb{R}^{+}\,\text{ predictable, }J(\alpha,\lambda)<\infty\right\}, |  |

WW is ℙ\mathbb{P}-Brownian motion and the Poisson measure NN has intensity λt​(z)​ν0​(d​z)​d​t\lambda\_{t}(z)\nu^{0}(\mathrm{d}z)\mathrm{d}t under ℙ\mathbb{P}. We denote by VS​B​J​T​SV\_{SBJTS} the infimum of this stochastic control problem:

|  |  |  |
| --- | --- | --- |
|  | VS​B​J​T​S=infα,λ∈𝒜𝒯μJ​(α,λ)V\_{SBJTS}=\inf\_{\alpha,\lambda\in\mathcal{A}^{\mu}\_{\mathcal{T}}}J(\alpha,\lambda) |  |

where 𝒜𝒯μ\mathcal{A}^{\mu}\_{\mathcal{T}} is the set of controls (α,λ)∈𝒜(\alpha,\lambda)\in\mathcal{A} such that ℙ∘(Xt1,…,XtN)−1=μ\mathbb{P}\circ(X\_{t\_{1}},\ldots,X\_{t\_{N}})^{-1}=\mu and d​Xt=αt​d​t+σ​d​Wt+∫ℝdz​N​(d​t,d​z),\mathrm{d}X\_{t}=\alpha\_{t}\,\mathrm{d}t+\sigma\,\mathrm{d}W\_{t}+\int\_{\mathbb{R}^{d}}zN(\mathrm{d}t,\mathrm{d}z), for t≤Tt\leq T, X0=0X\_{0}=0.

Our goal is to prove the existence of an optimal pair (α∗,λ∗)∈𝒜𝒯μ(\alpha^{\*},\lambda^{\*})\in\mathcal{A}^{\mu}\_{\mathcal{T}} that can be explicitly derived. Once identified, these optimal drift and intensity can be used to simulate the corresponding controlled jump-diffusion process XX, thereby generating samples from the time series distribution μ\mu under the probability measure ℙ∗\mathbb{P}^{\*} on Ω\Omega.

## 3 Solution of the Schrödinger bridge problem with jumps for time series

Let μ𝒯0=ℙ0∘(Xt1,…,XtN)−1\mu^{0}\_{\mathcal{T}}=\mathbb{P}^{0}\circ(X\_{t\_{1}},\ldots,X\_{t\_{N}})^{-1} be the distribution of the time series under the reference measure ℙ0\mathbb{P}^{0}. We introduce the following assumptions on the target distribution μ\mu and μ𝒯0\mu^{0}\_{\mathcal{T}}.

###### Assumption 1.

Assume that H​(μ|μ𝒯0)<∞H(\mathbb{\mu}|\mathbb{\mu}^{0}\_{\mathcal{T}})<\infty.

Observe that Assumption [1](https://arxiv.org/html/2602.20011v1#Thmassumption1 "Assumption 1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") implies that μ≪μ𝒯0\mu\ll\mu^{0}\_{\mathcal{T}}. This condition is sufficient to guarantee that the SBJTS problem is well posed and that a minimizer exists. However, our objective is not only to establish the existence, but also to characterize the induced dynamics of the process XX under the optimal solution. For this purpose, we introduce an additional assumption, which plays a crucial role in the proof of Theorem [3.1](https://arxiv.org/html/2602.20011v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").

###### Assumption 2.

Assume that μ∼μ𝒯0\mu\sim\mu^{0}\_{\mathcal{T}}.

We denote by d​μd​μ𝒯0\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}} the density of μ\mu with respect to μ𝒯0\mu^{0}\_{\mathcal{T}}. Moreover, we set 𝐗ti:=(Xt1,…,Xti)\mathbf{X}\_{t\_{i}}:=(X\_{t\_{1}},\ldots,X\_{t\_{i}}), 𝐱i:=(x1,…,xi)\mathbf{x}\_{i}:=(x\_{1},\ldots,x\_{i}) for all (x1,…,xN)∈(ℝd)N(x\_{1},\ldots,x\_{N})\in(\mathbb{R}^{d})^{N}, t0=0t\_{0}=0, and we denote by Xt−X\_{t^{-}} the left limit of the process XX in tt. For i=0,…,N−1i=0,\ldots,N-1, t∈[ti,ti+1]t\in[t\_{i},t\_{i+1}], x1,…,xi,x∈ℝdx\_{1},\ldots,x\_{i},x\in\mathbb{R}^{d} consider the function

|  |  |  |  |
| --- | --- | --- | --- |
|  | hi​(t,x;𝐱i)=𝔼ℙ0​[d​μd​μ𝒯0​(Xt1,…,XtN)|𝐗ti=𝐱i,Xt=x].h\_{i}(t,x;\mathbf{x}\_{i})=\mathbb{E}^{\mathbb{P}^{0}}\left[\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}\left(X\_{t\_{1}},\ldots,X\_{t\_{N}}\right)\;\big|\;\mathbf{X}\_{t\_{i}}=\mathbf{x}\_{i},\ X\_{t}=x\right]. |  | (3.1) |

The solution of the SBJTS problem is provided in the following theorem.

###### Theorem 3.1.

The probability measure ℙ∗∈𝒫​(Ω)\mathbb{P}^{\*}\in\mathcal{P}(\Omega) defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℙ∗d​ℙ0=d​μd​μ𝒯0​(Xt1,…,XtN),\frac{\mathrm{d}\mathbb{P}^{\*}}{\mathrm{d}\mathbb{P}^{0}}=\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}(X\_{t\_{1}},\ldots,X\_{t\_{N}}), |  | (3.2) |

solves the SBJTS problem and it is the law of the optimal process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=X0+∫0tαs∗​ds+σ​Wt+∫(0,t]×ℝdz​N​(d​t,d​z),t∈[0,T],X\_{t}=X\_{0}+\int\_{0}^{t}\alpha^{\*}\_{s}\mathrm{d}s+\sigma\,W\_{t}+\int\_{(0,t]\times\mathbb{R}^{d}}zN(\mathrm{d}t,\mathrm{d}z),\quad t\in[0,T], |  | (3.3) |

with X0=0X\_{0}=0, where (Wt)t∈[0,T](W\_{t})\_{t\in[0,T]} is a ℙ∗\mathbb{P}^{\*}-Brownian motion, and NN is a Poisson random measure with intensity measure λt∗​(z)​ν0​(d​z)​d​t\lambda^{\*}\_{t}(z)\nu^{0}(dz)dt under ℙ∗\mathbb{P}^{\*}.
For i=0,…,N−1i=0,\ldots,N-1, t∈(ti,ti+1]t\in(t\_{i},t\_{i+1}], the drift αt∗\alpha^{\*}\_{t} and the intensity λt∗​(z)\lambda^{\*}\_{t}(z) are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | αt∗\displaystyle\alpha^{\*}\_{t} | =a​(t,Xt;𝐗ti),\displaystyle=a(t,X\_{t};\mathbf{X}\_{t\_{i}}), |  | (3.4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λt∗​(z)\displaystyle\lambda^{\*}\_{t}(z) | =Λ​(t,Xt−,z;𝐗ti),\displaystyle=\Lambda(t,X\_{t^{-}},z;\mathbf{X}\_{t\_{i}}), |  | (3.5) |

where, for x1,…,xi,x∈ℝdx\_{1},\ldots,x\_{i},x\in\mathbb{R}^{d}, and z∈ℝdz\in\mathbb{R}^{d}, we set

|  |  |  |  |
| --- | --- | --- | --- |
|  | a​(t,x;𝐱i)\displaystyle a(t,x;\mathbf{x}\_{i}) | =σ​σ⊺​∇xln⁡hi​(t,x;𝐱i),\displaystyle=\sigma\sigma^{\scriptscriptstyle{\intercal}}\nabla\_{x}\ln h\_{i}(t,x;\mathbf{x}\_{i}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ​(t,x,z;𝐱i)\displaystyle\Lambda(t,x,z;\mathbf{x}\_{i}) | =λ0​hi​(t,x+z;𝐱i)hi​(t,x;𝐱i).\displaystyle=\lambda^{0}\frac{h\_{i}(t,x+z;\mathbf{x}\_{i})}{h\_{i}(t,x;\mathbf{x}\_{i})}. |  |

The pair (α∗,λ∗)∈𝒜(\alpha^{\*},\lambda^{\*})\in\mathcal{A} achieves the minimum of the problem (P), which satisfies

|  |  |  |
| --- | --- | --- |
|  | VS​B​J​T​S=H​(ℙ∗|ℙ0)=H​(μ|μ𝒯0).V\_{SBJTS}=H(\mathbb{P}^{\*}|\mathbb{P}^{0})=H(\mu|\mu^{0}\_{\mathcal{T}}). |  |

###### Proof.

Step 1: definition of the candidate optimal measure ℙ∗\mathbb{P}^{\*}. Following the approach of [[17](https://arxiv.org/html/2602.20011v1#bib.bib5 "Generative modeling for time series via Schrödinger bridge")], we begin by introducing the definition of the probability measure ℙ∗\mathbb{P}^{\*} such that ℙ∗≪ℙ0\mathbb{P}^{\*}\ll\mathbb{P}^{0}. Observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ0​[d​μd​μ𝒯0​(Xt1,…,XtN)]\displaystyle\mathbb{E}^{\mathbb{P}^{0}}\left[\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}(X\_{t\_{1}},\ldots,X\_{t\_{N}})\right] | =∫(ℝd)Nd​μd​μ𝒯0​(x1,…,xN)​μ𝒯0​(d​x1,…,d​xN)=1.\displaystyle=\int\_{(\mathbb{R}^{d})^{N}}\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}(x\_{1},\ldots,x\_{N})\mu^{0}\_{\mathcal{T}}(\mathrm{d}x\_{1},\ldots,\mathrm{d}x\_{N})=1. |  |

This suggests the existence of a probability ℙ∗≪ℙ0\mathbb{P}^{\*}\ll\mathbb{P}^{0} defined by

|  |  |  |
| --- | --- | --- |
|  | d​ℙ∗d​ℙ0=d​μd​μ𝒯0​(Xt1,…,XtN)\frac{\mathrm{d}\mathbb{P}^{\*}}{\mathrm{d}\mathbb{P}^{0}}=\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}(X\_{t\_{1}},\ldots,X\_{t\_{N}}) |  |

on ℱT\mathcal{F}\_{T}, and we can define the martingale given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt=𝔼ℙ0​[d​ℙ∗d​ℙ0|ℱt],  0≤t≤T,Z\_{t}=\mathbb{E}^{\mathbb{P}^{0}}\left[\frac{\mathrm{d}\mathbb{P}^{\*}}{\mathrm{d}\mathbb{P}^{0}}\;\big|\;\mathcal{F}\_{t}\right],\;\;0\leq t\leq T, |  | (3.6) |

with Z0=1Z\_{0}=1.

Step 2: expression of the martingale ZZ as a Doléans-Dade exponential martingale.
For any fixed index i∈{0,…,N−1}i\in\{0,\ldots,N-1\}, and t∈[ti,ti+1]t\in[t\_{i},t\_{i+1}], using the definition ([3.1](https://arxiv.org/html/2602.20011v1#S3.E1 "In 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) of the function hi​(t,x;𝐱i)h\_{i}(t,x;\mathbf{x}\_{i}) and the tower property of the conditional expectation, we can write

|  |  |  |
| --- | --- | --- |
|  | hi​(t,x;𝐱i)=𝔼ℙ0​[hi+1​(ti+1,Xti+1;𝐱i,Xti+1)|Xt=x],h\_{i}(t,x;\,\mathbf{x}\_{i})=\mathbb{E}^{\mathbb{P}^{0}}\left[h\_{i+1}(t\_{i+1},X\_{t\_{i+1}};\,\mathbf{x}\_{i},X\_{t\_{i+1}})\,\big|\,X\_{t}=x\right], |  |

for x1,…,xi,x∈ℝdx\_{1},\ldots,x\_{i},x\in\mathbb{R}^{d}, and so, in particular,

|  |  |  |  |
| --- | --- | --- | --- |
|  | hi​(ti+1,x;𝐱i)=hi+1​(ti+1,x;𝐱i,x),h\_{i}(t\_{i+1},x;\mathbf{x}\_{i})=h\_{i+1}(t\_{i+1},x;\mathbf{x}\_{i},x), |  | (3.7) |

with the convention that hN​(tN,x;𝐱N−1,x)=d​μd​μ𝒯0​(x1,…,xN−1,x)h\_{N}(t\_{N},x;\,\mathbf{x}\_{N-1},x)=\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}(x\_{1},\ldots,x\_{N-1},x). By Markov property, we get that

|  |  |  |
| --- | --- | --- |
|  | Zt=hi​(t,Xt;𝐗ti),Z\_{t}=h\_{i}(t,X\_{t};\mathbf{X}\_{t\_{i}}), |  |

and, by the independence and stationarity of the increments of the Lévy process under ℙ0\mathbb{P}^{0}, it holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | hi​(t,x;𝐱i)=𝔼ξi+1,…,ξN​[d​μd​μ𝒯0​(x1,…,xi,x+ξi+1,…,x+∑j=i+1Nξj)],h\_{i}(t,x;\mathbf{x}\_{i})=\mathbb{E}\_{\xi\_{i+1},\ldots,\xi\_{N}}\left[\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}(x\_{1},\ldots,x\_{i},x+\xi\_{i+1},\ldots,\;x+\sum\_{j=i+1}^{N}\xi\_{j})\right], |  | (3.8) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξi+1\displaystyle\xi\_{i+1} | =σ​ti+1−t​Yi+1+∑n=1N¯ti+1−tJn(i+1),\displaystyle=\sigma\sqrt{t\_{i+1}-t}\,Y\_{i+1}+\sum\_{n=1}^{\bar{N}\_{t\_{i+1}-t}}J^{(i+1)}\_{n}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ξj\displaystyle\xi\_{j} | =σ​tj−tj−1​Yj+∑n=1N¯tj−tj−1Jn(j),for all ​j=i+2,…,N,\displaystyle=\sigma\sqrt{t\_{j}-t\_{j-1}}\,Y\_{j}+\sum\_{n=1}^{\bar{N}\_{t\_{j}-t\_{j-1}}}J^{(j)}\_{n},\quad\text{for all }j=i+2,\ldots,N, |  |

where Yj,j=i+2,…,NY\_{j},\,j=i+2,\ldots,N, are i.i.d. 𝒩​(0,Id)\mathcal{N}(0,I\_{d}), N¯\bar{N} is a Poisson process with intensity λ0\lambda^{0}, (Jn(j))n≥1,j=i+1,…,N(J^{(j)}\_{n})\_{n\geq 1,j=i+1,\ldots,N} are i.i.d. random variables distributed according to ν0\nu^{0}, independent of YjY\_{j} and N¯\bar{N}. Thanks to ([3.8](https://arxiv.org/html/2602.20011v1#S3.E8 "In Proof. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), we get that the function hi​(t,x;𝐱i)h\_{i}(t,x;\mathbf{x}\_{i}) writes as an integral with respect to a smooth density, given by the convolution of the Gaussian density with the jump distribution ν0\nu^{0}. Therefore, the function (t,x)↦hi​(t,x;𝐱i)(t,x)\mapsto h\_{i}(t,x;\mathbf{x}\_{i}) belongs to C1,2​([ti,ti+1]×ℝd)C^{1,2}([t\_{i},t\_{i+1}]\times\mathbb{R}^{d}), and we can apply Itô’s formula under the measure ℙ0\mathbb{P}^{0} to Zt=hi​(t,Xt;𝐗ti)Z\_{t}=h\_{i}(t,X\_{t};\mathbf{X}\_{t\_{i}}). Since ZZ is a ℙ0\mathbb{P}^{0}-martingale, its finite-variation part must vanish, therefore we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Zt=∇xhi​(t,Xt−;𝐗ti)⊺​σ​d​Wt0+∫ℝd(hi​(t,Xt−+z;𝐗ti)−hi​(t,Xt−;𝐗ti))​(N​(d​t,d​z)−λ0​ν0​(d​z)​d​t)=Zt−​(∇xln⁡hi​(t,Xt−;𝐗ti)⊺​σ​d​Wt0+∫ℝd(λ0​hi​(t,Xt−+z;𝐗ti)hi​(t,Xt−;𝐗ti)−λ0)​(N​(d​t,d​z)λ0−ν0​(d​z)​d​t))\begin{split}\mathrm{d}Z\_{t}&=\nabla\_{x}h\_{i}(t,X\_{t^{-}};\mathbf{X}\_{t\_{i}})^{\scriptscriptstyle{\intercal}}\,\sigma\mathrm{d}W^{0}\_{t}+\int\_{\mathbb{R}^{d}}(h\_{i}(t,X\_{t^{-}}+z;\mathbf{X}\_{t\_{i}})-h\_{i}(t,X\_{t^{-}};\mathbf{X}\_{t\_{i}}))(N(\mathrm{d}t,\mathrm{d}z)-\lambda^{0}\nu^{0}(\mathrm{d}z)\mathrm{d}t)\\ &=Z\_{t^{-}}\Bigg(\nabla\_{x}\ln h\_{i}(t,X\_{t^{-}};\mathbf{X}\_{t\_{i}})^{\scriptscriptstyle{\intercal}}\sigma\mathrm{d}W^{0}\_{t}+\int\_{\mathbb{R}^{d}}\Bigg(\lambda^{0}\frac{h\_{i}(t,X\_{t^{-}}+z;\mathbf{X}\_{t\_{i}})}{h\_{i}(t,X\_{t^{-}};\mathbf{X}\_{t\_{i}})}-\lambda^{0}\Bigg)\left(\frac{N(\mathrm{d}t,\mathrm{d}z)}{\lambda^{0}}-\nu^{0}(\mathrm{d}z)\mathrm{d}t\right)\Bigg)\end{split} |  | (3.9) |

in (ti,ti+1],i=0,…,N−1(t\_{i},t\_{i+1}],\,i=0,\ldots,N-1, where we use that hi​(t,x;𝐱i)h\_{i}(t,x;\mathbf{x}\_{i}) is strictly positive thanks to Assumption [2](https://arxiv.org/html/2602.20011v1#Thmassumption2 "Assumption 2. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."). By defining the processes αt∗\alpha^{\*}\_{t} as in ([3.4](https://arxiv.org/html/2602.20011v1#S3.E4 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), and λt∗​(z)\lambda^{\*}\_{t}(z) as in ([3.5](https://arxiv.org/html/2602.20011v1#S3.E5 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), we get

|  |  |  |
| --- | --- | --- |
|  | d​Zt=Zt−​((σ−1​αt∗)⊺​d​Wt0+∫ℝd(λt∗​(z)−λ0)​(N​(d​t,d​z)λ0−ν0​(d​z)​d​t)),\mathrm{d}Z\_{t}=Z\_{t^{-}}\Bigg((\sigma^{-1}\alpha^{\*}\_{t})^{\scriptscriptstyle{\intercal}}\mathrm{d}W^{0}\_{t}+\int\_{\mathbb{R}^{d}}(\lambda\_{t}^{\*}(z)-\lambda^{0})\left(\frac{N(\mathrm{d}t,\mathrm{d}z)}{\lambda^{0}}-\nu^{0}(\mathrm{d}z)\mathrm{d}t\right)\Bigg), |  |

whose solution is

|  |  |  |
| --- | --- | --- |
|  | Zt=exp(∫tit(σ−1αs∗)⊺dWs0−12∫tit∥σ−1αs∗∥2ds+∫(ti,t]×ℝdln(λs∗​(z)λ0)N(ds,dz)−∫(ti,t]×ℝd(λs∗(z)−λ0)ν0(dz)ds),Z\_{t}=\exp\Bigg(\int\_{t\_{i}}^{t}(\sigma^{-1}\alpha^{\*}\_{s})^{\scriptscriptstyle{\intercal}}\mathrm{d}W^{0}\_{s}-\frac{1}{2}\int\_{t\_{i}}^{t}\|\sigma^{-1}\alpha^{\*}\_{s}\|^{2}\mathrm{d}s\\ +\int\_{({t\_{i}},t]\times\mathbb{R}^{d}}\ln\left(\frac{\lambda^{\*}\_{s}(z)}{\lambda^{0}}\right)N(\mathrm{d}s,\mathrm{d}z)-\int\_{({t\_{i}},t]\times\mathbb{R}^{d}}(\lambda^{\*}\_{s}(z)-\lambda^{0})\nu^{0}(\mathrm{d}z)\mathrm{d}s\Bigg), |  |

for t∈(ti,ti+1],i=0,…,N−1t\in(t\_{i},t\_{i+1}],\,i=0,\ldots,N-1. From this last expression, we identify the Doléans–Dade exponential martingale, which we want to use in Girsanov’s theorem.

Step 3: application of Girsanov’s theorem.
Under the assumption that H​(ℙ∗|ℙ0)<∞H(\mathbb{P}^{\*}\,|\,\mathbb{P}^{0})<\infty, by Girsanov’s theorem there exist an ℝd\mathbb{R}^{d}-valued adapted process α∗=(αt∗)t∈[0,T]\alpha^{\*}=(\alpha^{\*}\_{t})\_{t\in[0,T]} and an ℝ+\mathbb{R}^{+}-valued predictable process λ∗​(z)=(λt∗​(z))t∈[0,T]\lambda^{\*}(z)=(\lambda^{\*}\_{t}(z))\_{t\in[0,T]}, for z∈ℝdz\in\mathbb{R}^{d}, defined in ([3.4](https://arxiv.org/html/2602.20011v1#S3.E4 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) and ([3.5](https://arxiv.org/html/2602.20011v1#S3.E5 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), such that it holds

|  |  |  |
| --- | --- | --- |
|  | d​ℙ∗d​ℙ0=ZT=exp(∫0T(σ−1αs∗)⊺dWs0−12∫0T∥σ−1αs∗∥2ds+∫(0,T]×ℝdln(λs∗​(z)λ0)N(ds,dz)−∫(0,T]×ℝd(λs∗(z)−λ0)ν0(dz)ds).\frac{\mathrm{d}\mathbb{P}^{\*}}{\mathrm{d}\mathbb{P}^{0}}=Z\_{T}=\exp\Bigg(\int\_{0}^{T}(\sigma^{-1}\alpha^{\*}\_{s})^{\scriptscriptstyle{\intercal}}\mathrm{d}W^{0}\_{s}-\frac{1}{2}\int\_{0}^{T}\|\sigma^{-1}\alpha^{\*}\_{s}\|^{2}\mathrm{d}s\\ +\int\_{(0,T]\times\mathbb{R}^{d}}\ln\left(\frac{\lambda^{\*}\_{s}(z)}{\lambda^{0}}\right)N(\mathrm{d}s,\mathrm{d}z)-\int\_{(0,T]\times\mathbb{R}^{d}}(\lambda^{\*}\_{s}(z)-\lambda^{0})\nu^{0}(\mathrm{d}z)\mathrm{d}s\Bigg). |  |

Moreover, it follows that the processes

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wt0−∫0tσ−1​αs∗​ds,\displaystyle W^{0}\_{t}-\int\_{0}^{t}\sigma^{-1}\alpha^{\*}\_{s}\mathrm{d}s, |  | (3.10) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫(0,t]×ℝdln⁡(λs∗​(z)λ0)​N​(d​s,d​z)−∫(0,t]×ℝdλs∗​(z)​ln⁡(λs∗​(z)λ0)​ν0​(d​z)​ds,\displaystyle\int\_{(0,t]\times\mathbb{R}^{d}}\ln\left(\frac{\lambda^{\*}\_{s}(z)}{\lambda^{0}}\right)N(\mathrm{d}s,\mathrm{d}z)-\int\_{(0,t]\times\mathbb{R}^{d}}\lambda^{\*}\_{s}(z)\ln\left(\frac{\lambda^{\*}\_{s}(z)}{\lambda^{0}}\right)\nu^{0}(\mathrm{d}z)\mathrm{d}s, |  | (3.11) |

for t∈[0,T]t\in[0,T], are ℙ∗\mathbb{P}^{\*}-martingales: ([3.10](https://arxiv.org/html/2602.20011v1#S3.E10 "In Proof. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) defines a new ℙ∗\mathbb{P}^{\*}-Brownian motion that we denote by WW, while from ([3.11](https://arxiv.org/html/2602.20011v1#S3.E11 "In Proof. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) we get that λt∗​(z)​ν0​(d​z)​d​t\lambda^{\*}\_{t}(z)\nu^{0}(\mathrm{d}z)\mathrm{d}t is the new intensity measure of the random Poisson measure N​(d​t,d​z)N(\mathrm{d}t,\mathrm{d}z) under ℙ∗\mathbb{P}^{\*}. Hence, we can conclude that the new dynamics of the process X=(Xt)t∈[0,T]X=(X\_{t})\_{t\in[0,T]} under the probability ℙ∗\mathbb{P}^{\*} is

|  |  |  |
| --- | --- | --- |
|  | Xt=X0+∫0tαs∗​ds+σ​Wt+∫(0,t]×ℝdz​N​(d​s,d​z),t∈[0,T],X\_{t}=X\_{0}+\int\_{0}^{t}\alpha^{\*}\_{s}\,\mathrm{d}s+\sigma\,W\_{t}+\int\_{(0,t]\times\mathbb{R}^{d}}zN(\mathrm{d}s,\mathrm{d}z),\quad t\in[0,T], |  |

where N​(d​t,d​z)N(\mathrm{d}t,\mathrm{d}z) has intensity measure λt∗​(z)​ν0​(d​z)​d​t\lambda^{\*}\_{t}(z)\nu^{0}(\mathrm{d}z)\mathrm{d}t.

Step 4: optimality of ℙ∗\mathbb{P}^{\*}.
We show now that the processes α∗\alpha^{\*} and λ∗​(z)\lambda^{\*}(z) are optimal for the minimization of J​(α,λ)J(\alpha,\lambda). By definition we have that J​(α∗,λ∗)=H​(ℙ∗|ℙ0)=H​(μ|μ𝒯0)J(\alpha^{\*},\lambda^{\*})=H(\mathbb{P}^{\*}|\mathbb{P}^{0})=H(\mu|\mu^{0}\_{\mathcal{T}}). Let α,λ\alpha,\lambda be the control and the intensity associated to another probability ℙ\mathbb{P}, then using Jensen inequality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1\displaystyle 1 | =𝔼ℙ0​[d​μd​μ𝒯0​(Xt1,…,XtN)]\displaystyle=\mathbb{E}^{\mathbb{P}^{0}}\left[\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}(X\_{t\_{1}},\ldots,X\_{t\_{N}})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℙ[exp(lnd​μd​μ𝒯0(Xt1,…,XtN)−∫0T(σ−1αt)⊺dWt0+12∫0T∥σ−1αt∥2dt−∫(0,T]×ℝdlnλt​(z)λ0N(dt,dz)\displaystyle=\mathbb{E}^{\mathbb{P}}\Bigg[\exp\Bigg(\ln\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}\left(X\_{t\_{1}},\ldots,X\_{t\_{N}}\right)-\int\_{0}^{T}(\sigma^{-1}\alpha\_{t})^{\scriptscriptstyle{\intercal}}\mathrm{d}W^{0}\_{t}+\frac{1}{2}\int\_{0}^{T}\|\sigma^{-1}\alpha\_{t}\|^{2}\mathrm{d}t-\int\_{(0,T]\times\mathbb{R}^{d}}\ln\frac{\lambda\_{t}(z)}{\lambda^{0}}N(\mathrm{d}t,\mathrm{d}z) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫(0,T]×ℝd(λt(z)−λ0)ν0(dz)dt)]\displaystyle\quad\quad+\int\_{(0,T]\times\mathbb{R}^{d}}(\lambda\_{t}(z)-\lambda^{0})\nu^{0}(\mathrm{d}z)\mathrm{d}t\Bigg)\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥exp(𝔼ℙ[lnd​μd​μ𝒯0(Xt1,…,XtN)−∫0T(σ−1αt)⊺dWtℙ−12∫0T∥σ−1αt∥2dt+∫(0,T]×ℝd(λt(z)−λ0)ν0(dz)dt\displaystyle\geq\exp\Bigg(\mathbb{E}^{\mathbb{P}}\Bigg[\ln\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}\left(X\_{t\_{1}},\ldots,X\_{t\_{N}}\right)-\int\_{0}^{T}(\sigma^{-1}\alpha\_{t})^{\scriptscriptstyle{\intercal}}\mathrm{d}W^{\mathbb{P}}\_{t}-\frac{1}{2}\int\_{0}^{T}\|\sigma^{-1}\alpha\_{t}\|^{2}\mathrm{d}t+\int\_{(0,T]\times\mathbb{R}^{d}}(\lambda\_{t}(z)-\lambda^{0})\nu^{0}(\mathrm{d}z)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫(0,T]×ℝdlnλt​(z)λ0λt(z)ν0(dz)dt−∫(0,T]×ℝdlnλt​(z)λ0(N(dt,dz)−λt(z)ν0(dz)dt)])\displaystyle\quad\quad-\int\_{(0,T]\times\mathbb{R}^{d}}\ln\frac{\lambda\_{t}(z)}{\lambda^{0}}\lambda\_{t}(z)\nu^{0}(\mathrm{d}z)\mathrm{d}t-\int\_{(0,T]\times\mathbb{R}^{d}}\ln\frac{\lambda\_{t}(z)}{\lambda^{0}}(N(\mathrm{d}t,\mathrm{d}z)-\lambda\_{t}(z)\nu^{0}(\mathrm{d}z)\mathrm{d}t)\Bigg]\Bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(H​(μ|μ𝒯0)−𝔼ℙ​[∫(0,T]×ℝd(λt​(z)​ln⁡λt​(z)λ0−λt​(z)+λ0)​ν0​(d​z)​dt+12​∫0T‖σ−1​αt‖2​dt])\displaystyle=\exp\Bigg(H(\mu|\mu^{0}\_{\mathcal{T}})-\mathbb{E}^{\mathbb{P}}\Bigg[\int\_{(0,T]\times\mathbb{R}^{d}}\Bigg(\lambda\_{t}(z)\ln\frac{\lambda\_{t}(z)}{\lambda^{0}}-\lambda\_{t}(z)+\lambda^{0}\Bigg)\nu^{0}(\mathrm{d}z)\mathrm{d}t+\frac{1}{2}\int\_{0}^{T}\|\sigma^{-1}\alpha\_{t}\|^{2}\mathrm{d}t\Bigg]\Bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(H​(μ|μ𝒯0)−J​(α,λ)).\displaystyle=\exp\Bigg(H(\mu|\mu^{0}\_{\mathcal{T}})-J(\alpha,\lambda)\Bigg). |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | J​(α∗,λ∗)=H​(μ|μ𝒯0)≤J​(α,λ),J(\alpha^{\*},\lambda^{\*})=H(\mu|\mu^{0}\_{\mathcal{T}})\leq J(\alpha,\lambda), |  |

and therefore also

|  |  |  |
| --- | --- | --- |
|  | H​(ℙ∗|ℙ0)≤H​(ℙ|ℙ0),∀ℙ∈𝒫𝒯μ​(Ω).H(\mathbb{P}^{\*}|\mathbb{P}^{0})\leq H(\mathbb{P}|\mathbb{P}^{0}),\quad\forall\mathbb{P}\in\mathcal{P}^{\mu}\_{\mathcal{T}}(\Omega). |  |

This shows that ℙ∗\mathbb{P}^{\*} realizes the minimum in the SBJTS problem.

Step 5: check the constraint on the joint law.
Finally we check that the constraint on the joint distribution is satisfied. For any function ϕ\phi bounded measurable on (ℝd)N(\mathbb{R}^{d})^{N}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ∗​[ϕ​(Xt1,…,XtN)]\displaystyle\mathbb{E}^{\mathbb{P}^{\*}}[\phi(X\_{t\_{1}},\ldots,X\_{t\_{N}})] | =𝔼ℙ0​[d​μd​μ𝒯0​(Xt1,…,XtN)​ϕ​(Xt1,…,XtN)]\displaystyle=\mathbb{E}^{\mathbb{P}^{0}}\left[\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}\left(X\_{t\_{1}},\ldots,X\_{t\_{N}}\right)\phi(X\_{t\_{1}},\ldots,X\_{t\_{N}})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫(ℝd)Nd​μd​μ𝒯0​(x1,…,xN)​ϕ​(x1,…,xN)​μ𝒯0​(d​x1,…,d​xN)\displaystyle=\int\_{(\mathbb{R}^{d})^{N}}\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}\left(x\_{1},\ldots,x\_{N}\right)\phi(x\_{1},\ldots,x\_{N})\mu^{0}\_{\mathcal{T}}(\mathrm{d}x\_{1},\ldots,\mathrm{d}x\_{N}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫(ℝd)Nϕ​(x1,…,xN)​μ​(d​x1,…,d​xN).\displaystyle=\int\_{(\mathbb{R}^{d})^{N}}\phi(x\_{1},\ldots,x\_{N})\mu\left(\mathrm{d}x\_{1},\ldots,\mathrm{d}x\_{N}\right). |  |

This proves that ℙ∗∘(Xt1,…,XtN)−1=μ\mathbb{P}^{\*}\circ(X\_{t\_{1}},\ldots,X\_{t\_{N}})^{-1}=\mu and completes the proof.
∎

Pure jump case.
Theorem [3.1](https://arxiv.org/html/2602.20011v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") holds also in the pure jump case. Indeed, if we assume that σ\sigma is null, i.e. that ℙ0\mathbb{P}^{0} is the law of a compound Poisson process with jumps distributed according to ν0\nu^{0}, then we can still write the SBJTS problem, define the solution as in ([3.2](https://arxiv.org/html/2602.20011v1#S3.E2 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) and the martingale

|  |  |  |
| --- | --- | --- |
|  | Zt=𝔼ℙ0​[d​μd​μ𝒯0​(Xt1,…,XtN)|ℱt],t≤T.Z\_{t}=\mathbb{E}^{\mathbb{P}^{0}}\left[\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}\left(X\_{t\_{1}},\ldots,X\_{t\_{N}}\right)\;\big|\;\mathcal{F}\_{t}\right],\quad t\leq T. |  |

By Markov property we have Zt=hi​(t,Xt;𝐗ti)Z\_{t}=h\_{i}(t,X\_{t};\mathbf{X}\_{t\_{i}}), for t∈(ti,ti+1],i=0,…,N−1t\in(t\_{i},t\_{i+1}],\,i=0,\ldots,N-1, and since X=(Xt)t≥0X=(X\_{t})\_{t\geq 0} is a pure jump process, it holds

|  |  |  |
| --- | --- | --- |
|  | hi​(t,Xt;𝐗ti)=hi​(ti,Xti;𝐗ti)+∑ti<s≤thi​(s,Xs;𝐗ti)−hi​(s,Xs−;𝐗ti)h\_{i}(t,X\_{t};\mathbf{X}\_{t\_{i}})=h\_{i}(t\_{i},X\_{t\_{i}};\mathbf{X}\_{t\_{i}})+\sum\_{t\_{i}<s\leq t}h\_{i}(s,X\_{s};\mathbf{X}\_{t\_{i}})-h\_{i}(s,X\_{s^{-}};\mathbf{X}\_{t\_{i}}) |  |

which gives

|  |  |  |
| --- | --- | --- |
|  | d​Zt=∫ℝd(hi​(t,Xt−+z;𝐗ti)−hi​(t,Xt−;𝐗ti))​(N​(d​t,d​z)−λ0​ν0​(d​z)​d​t)\mathrm{d}Z\_{t}=\int\_{\mathbb{R}^{d}}(h\_{i}(t,X\_{t^{-}}+z;\mathbf{X}\_{t\_{i}})-h\_{i}(t,X\_{t^{-}};\mathbf{X}\_{t\_{i}}))(N(\mathrm{d}t,\mathrm{d}z)-\lambda^{0}\nu^{0}(\mathrm{d}z)\mathrm{d}t) |  |

as ZZ is martingale. Hence we get that the new compensator of the Poisson measure N​(d​t,d​z)N(\mathrm{d}t,\mathrm{d}z) under the new measure ℙ∗\mathbb{P}^{\*} is λt∗​(z)​ν0​(d​z)​d​t\lambda^{\*}\_{t}(z)\nu^{0}(\mathrm{d}z)\mathrm{d}t, where

|  |  |  |
| --- | --- | --- |
|  | λt∗​(z)=λ0​hi​(t,Xt−+z;𝐗ti)hi​(t,Xt−;𝐗ti),\lambda^{\*}\_{t}(z)=\lambda^{0}\frac{h\_{i}(t,X\_{t^{-}}+z;\mathbf{X}\_{t\_{i}})}{h\_{i}(t,X\_{t^{-}};\mathbf{X}\_{t\_{i}})}, |  |

and the dynamics of the optimal process under ℙ∗\mathbb{P}^{\*} is

|  |  |  |
| --- | --- | --- |
|  | Xt=X0+∫(0,t]×ℝdz​N​(d​s,d​z),t∈[0,T].X\_{t}=X\_{0}+\int\_{(0,t]\times\mathbb{R}^{d}}zN(\mathrm{d}s,\mathrm{d}z),\quad t\in[0,T]. |  |

Notice that we only use that hi​(t,x;𝐱i)h\_{i}(t,x;\mathbf{x}\_{i}) is strictly positive and measurable, but no other smoothness assumptions are required.

Thanks to Theorem [3.1](https://arxiv.org/html/2602.20011v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."), we obtain the dynamics ([3.3](https://arxiv.org/html/2602.20011v1#S3.E3 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) of the optimal process XX under the probability measure ℙ∗\mathbb{P}^{\*} which solves the SBJTS problem. Our objective is to simulate this optimal dynamics. As follows from ([3.4](https://arxiv.org/html/2602.20011v1#S3.E4 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) and ([3.5](https://arxiv.org/html/2602.20011v1#S3.E5 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), both the drift and the jump intensity are time, state and path dependent, through their dependence on the vector 𝐱i\mathbf{x}\_{i}. This path dependence is essential, as it requires the construction of estimators to approximate the optimal drift and jump intensity that have to be evaluated along each simulated trajectory.

## 4 Approximation of the optimal drift and intensity

In this section, we focus on the expressions of the optimal drift and intensity of jumps to highlight how we can get fully data driven estimators that allow the simulation of the generative process ([3.3](https://arxiv.org/html/2602.20011v1#S3.E3 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")). We first derive an explicit expression for the function hi​(t,x;𝐱i)h\_{i}(t,x;\mathbf{x}\_{i}), and then we present the estimators that are used in practice.

### 4.1 Explicit formula for the drift and intensity of jumps

We state the following proposition using that μ𝒯0\mu^{0}\_{\mathcal{T}} admits a density with respect to the Lebesgue measure, as by definition μ𝒯0=ℙ0∘(Xt1,…,XtN)−1\mu^{0}\_{\mathcal{T}}=\mathbb{P}^{0}\circ(X\_{t\_{1}},\ldots,X\_{t\_{N}})^{-1}, where XX follows the dynamics ([2.1](https://arxiv.org/html/2602.20011v1#S2.E1 "In 2 Setting and problem formulation ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")). Moreover, as μ≪μ𝒯0\mu\ll\mu^{0}\_{\mathcal{T}} by hypothesis, μ\mu admits also a density with respect to the Lebesgue measure. By a slight abuse of notation, we denote these densities respectively by (x1,…,xN)↦μ𝒯0​(x1,…,xN)(x\_{1},\ldots,x\_{N})\mapsto\mu^{0}\_{\mathcal{T}}(x\_{1},\ldots,x\_{N}) and (x1,…,xN)↦μ​(x1,…,xN)(x\_{1},\ldots,x\_{N})\mapsto\mu(x\_{1},\ldots,x\_{N}).

###### Proposition 4.1.

For i=0,…,N−1i=0,\ldots,N-1, 𝐱i∈(ℝd)i\mathbf{x}\_{i}\in(\mathbb{R}^{d})^{i}, x∈ℝdx\in\mathbb{R}^{d} and z∈ℝdz\in\mathbb{R}^{d}, the functions a​(t,x;𝐱i)a(t,x;\mathbf{x}\_{i}) and Λ​(t,x,z;𝐱i)\Lambda(t,x,z;\mathbf{x}\_{i}) defined in Theorem [3.1](https://arxiv.org/html/2602.20011v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | a​(t,x;𝐱i)\displaystyle a(t,x;\mathbf{x}\_{i}) | =σ​σ⊺​𝔼μ​[∇xFi​(t,xi,x,Xti+1)|𝐗ti=𝐱i]𝔼μ​[Fi​(t,xi,x,Xti+1)|𝐗ti=𝐱i],t∈[ti,ti+1),\displaystyle=\sigma\sigma^{\scriptscriptstyle{\intercal}}\frac{\mathbb{E}\_{\mu}[\nabla\_{x}F\_{i}(t,x\_{i},x,X\_{t\_{i+1}})|\mathbf{X}\_{t\_{i}}=\mathbf{x}\_{i}]}{\mathbb{E}\_{\mu}[F\_{i}(t,x\_{i},x,X\_{t\_{i+1}})|\mathbf{X}\_{t\_{i}}=\mathbf{x}\_{i}]},\quad t\in[t\_{i},t\_{i+1}), |  | (4.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Λ​(t,x,z;𝐱i)\displaystyle\Lambda(t,x,z;\mathbf{x}\_{i}) | =λ0​𝔼μ​[Fi​(t,xi,x+z,Xti+1)|𝐗ti=𝐱i]𝔼μ​[Fi​(t,xi,x,Xti+1)|𝐗ti=𝐱i],t∈(ti,ti+1),\displaystyle=\lambda^{0}\frac{\mathbb{E}\_{\mu}[F\_{i}(t,x\_{i},x+z,X\_{t\_{i+1}})|\mathbf{X}\_{t\_{i}}=\mathbf{x}\_{i}]}{\mathbb{E}\_{\mu}[F\_{i}(t,x\_{i},x,X\_{t\_{i+1}})|\mathbf{X}\_{t\_{i}}=\mathbf{x}\_{i}]},\quad t\in(t\_{i},t\_{i+1}), |  | (4.2) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fi​(t,xi,x,xi+1)=fti+1−t0​(xi+1−x)fti+1−ti0​(xi+1−xi),F\_{i}(t,x\_{i},x,x\_{i+1})=\frac{f^{0}\_{t\_{i+1}-t}(x\_{i+1}-x)}{f^{0}\_{t\_{i+1}-t\_{i}}(x\_{i+1}-x\_{i})}, |  | (4.3) |

the function fti+1−t0f^{0}\_{t\_{i+1}-t} is the density of the increment Xti+1−XtX\_{t\_{i+1}}-X\_{t}, for t∈[ti,ti+1)t\in[t\_{i},t\_{i+1}), under the reference measure ℙ0\mathbb{P}^{0}, and 𝔼μ\mathbb{E}\_{\mu} denotes the expectation under μ\mu.

###### Proof.

Consider μ𝒯0​(x1,…,xN)\mu^{0}\_{\mathcal{T}}(x\_{1},\ldots,x\_{N}) the density with respect to the Lebesgue measure of the vector (Xt1,…,XtN)(X\_{t\_{1}},\ldots,X\_{t\_{N}}) under ℙ0\mathbb{P}^{0}. By independence of the increments, we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ𝒯0​(x1,…,xN)=∏j=0N−1ftj+1−tj0​(xj+1−xj),\mu^{0}\_{\mathcal{T}}(x\_{1},\ldots,x\_{N})=\prod\_{j=0}^{N-1}f^{0}\_{t\_{j+1}-t\_{j}}(x\_{j+1}-x\_{j}), |  | (4.4) |

where we set x0=0x\_{0}=0 and t0=0t\_{0}=0. For fixed i=0,…,N−1i=0,\ldots,N-1, t∈(ti,ti+1)t\in(t\_{i},t\_{i+1}), 𝐱i∈(ℝd)i\mathbf{x}\_{i}\in(\mathbb{R}^{d})^{i}, and x∈ℝdx\in\mathbb{R}^{d}, we can rewrite the function hi​(t,x;𝐱i)h\_{i}(t,x;\mathbf{x}\_{i}) using ([4.4](https://arxiv.org/html/2602.20011v1#S4.E4 "In Proof. ‣ 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | hi​(t,x;𝐱i)\displaystyle h\_{i}(t,x;\mathbf{x}\_{i}) | =𝔼ℙ0​[d​μd​μ𝒯0​(x1,…,xi,Xti+1,…,XtN)|Xt=x]\displaystyle=\mathbb{E}^{\mathbb{P}^{0}}\left[\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}(x\_{1},\ldots,x\_{i},X\_{t\_{i+1}},\ldots,X\_{t\_{N}})\;\big|\;X\_{t}=x\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫(ℝd)N−iμ​(x1,…,xN)μi0​(x1,…,xi)​fti+1−t0​(xi+1−x)fti+1−ti0​(xi+1−xi)​dxi+1​⋯​dxN\displaystyle=\int\_{(\mathbb{R}^{d})^{N-i}}\frac{\mu(x\_{1},\ldots,x\_{N})}{\mu^{0}\_{i}(x\_{1},\ldots,x\_{i})}\frac{f^{0}\_{t\_{i+1}-t}(x\_{i+1}-x)}{f^{0}\_{t\_{i+1}-t\_{i}}(x\_{i+1}-x\_{i})}\,\mathrm{d}x\_{i+1}\cdots\mathrm{d}x\_{N} |  |

where we call μi0​(x1,…,xi)\mu^{0}\_{i}(x\_{1},\ldots,x\_{i}) the density of (Xt1,…,Xti)(X\_{t\_{1}},\ldots,X\_{t\_{i}}) under μ𝒯0\mu^{0}\_{\mathcal{T}}. Hence, if we introduce the function

|  |  |  |
| --- | --- | --- |
|  | Fi​(t,xi,x,xi+1)=fti+1−t0​(xi+1−x)fti+1−ti0​(xi+1−xi),F\_{i}(t,x\_{i},x,x\_{i+1})=\frac{f^{0}\_{t\_{i+1}-t}(x\_{i+1}-x)}{f^{0}\_{t\_{i+1}-t\_{i}}(x\_{i+1}-x\_{i})}, |  |

and we denote by μi​(x1,…,xi)\mu\_{i}(x\_{1},\ldots,x\_{i}) the density of (Xt1,…,Xti)(X\_{t\_{1}},\ldots,X\_{t\_{i}}) under μ\mu with respect to the Lebesgue measure, i.e.

|  |  |  |
| --- | --- | --- |
|  | μi​(x1,…,xi)=∫(ℝd)N−iμ​(x1,…,xN)​dxi+1​⋯​dxN,\mu\_{i}(x\_{1},\ldots,x\_{i})=\int\_{(\mathbb{R}^{d})^{N-i}}\mu(x\_{1},\ldots,x\_{N})\,\mathrm{d}x\_{i+1}\cdots\mathrm{d}x\_{N}, |  |

we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | hi​(t,x;𝐱i)\displaystyle h\_{i}(t,x;\mathbf{x}\_{i}) | =∫(ℝd)N−iFi​(t,xi,x,xi+1)​μi​(x1,…,xi)μi0​(x1,…,xi)​μ​(x1,…,xN)μi​(x1,…,xi)​dxi+1​⋯​dxN\displaystyle=\int\_{(\mathbb{R}^{d})^{N-i}}F\_{i}(t,x\_{i},x,x\_{i+1})\frac{\mu\_{i}(x\_{1},\ldots,x\_{i})}{\mu^{0}\_{i}(x\_{1},\ldots,x\_{i})}\frac{\mu(x\_{1},\ldots,x\_{N})}{\mu\_{i}(x\_{1},\ldots,x\_{i})}\,\mathrm{d}x\_{i+1}\cdots\mathrm{d}x\_{N} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =C​∫(ℝd)N−iFi​(t,xi,x,xi+1)​μ​(x1,…,xN)μi​(x1,…,xi)​dxi+1​⋯​dxN,\displaystyle=C\int\_{(\mathbb{R}^{d})^{N-i}}F\_{i}(t,x\_{i},x,x\_{i+1})\frac{\mu(x\_{1},\ldots,x\_{N})}{\mu\_{i}(x\_{1},\ldots,x\_{i})}\,\mathrm{d}x\_{i+1}\cdots\mathrm{d}x\_{N}, |  |

with CC a constant depending only on (x1,…,xi)(x\_{1},\ldots,x\_{i}). Therefore,

|  |  |  |
| --- | --- | --- |
|  | hi​(t,x;𝐱i)=C​𝔼μ​[Fi​(t,xi,x,Xti+1)|𝐗ti=𝐱i].h\_{i}(t,x;\mathbf{x}\_{i})=C\,\mathbb{E}\_{\mu}[F\_{i}(t,x\_{i},x,X\_{t\_{i+1}})|\mathbf{X}\_{t\_{i}}=\mathbf{x}\_{i}]. |  |

This allows to get the expression

|  |  |  |
| --- | --- | --- |
|  | a​(t,x;𝐱i)=σ​σ⊺​∇xhi​(t,x;𝐱i)hi​(t,x;𝐱i)=σ​σ⊺​𝔼μ​[∇xFi​(t,xi,x,Xti+1)|𝐗ti=𝐱i]𝔼μ​[Fi​(t,xi,x,Xti+1)|𝐗ti=𝐱i],a(t,x;\mathbf{x}\_{i})=\sigma\sigma^{\scriptscriptstyle{\intercal}}\frac{\nabla\_{x}h\_{i}(t,x;\mathbf{x}\_{i})}{h\_{i}(t,x;\mathbf{x}\_{i})}=\sigma\sigma^{\scriptscriptstyle{\intercal}}\frac{\mathbb{E}\_{\mu}[\nabla\_{x}F\_{i}(t,x\_{i},x,X\_{t\_{i+1}})|\mathbf{X}\_{t\_{i}}=\mathbf{x}\_{i}]}{\mathbb{E}\_{\mu}[F\_{i}(t,x\_{i},x,X\_{t\_{i+1}})|\mathbf{X}\_{t\_{i}}=\mathbf{x}\_{i}]}, |  |

which is also well defined at t=tit=t\_{i} thanks to ([3.7](https://arxiv.org/html/2602.20011v1#S3.E7 "In Proof. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ​(t,x,z;𝐱i)=λ0​hi​(t,x+z;𝐱i)hi​(t,x;𝐱i)=λ0​𝔼μ​[Fi​(t,xi,x+z,Xti+1)|𝐗ti=𝐱i]𝔼μ​[Fi​(t,xi,x,Xti+1)|𝐗ti=𝐱i].\displaystyle\Lambda(t,x,z;\mathbf{x}\_{i})=\lambda^{0}\frac{h\_{i}(t,x+z;\mathbf{x}\_{i})}{h\_{i}(t,x;\mathbf{x}\_{i})}=\lambda^{0}\frac{\mathbb{E}\_{\mu}[F\_{i}(t,x\_{i},x+z,X\_{t\_{i+1}})|\mathbf{X}\_{t\_{i}}=\mathbf{x}\_{i}]}{\mathbb{E}\_{\mu}[F\_{i}(t,x\_{i},x,X\_{t\_{i+1}})|\mathbf{X}\_{t\_{i}}=\mathbf{x}\_{i}]}. |  | (4.5) |

∎

###### Remark 4.1.

At the time values {ti}i=1,…,N−1\{t\_{i}\}\_{i=1,\ldots,N-1} the value of the intensity function λti+1∗​(z)=Λ​(ti+1,Xti+1−,z;𝐗ti)\lambda^{\*}\_{t\_{i+1}}(z)=\Lambda(t\_{i+1},X\_{t\_{i+1}^{-}},z;\mathbf{X}\_{t\_{i}}) is given by following expression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ​(ti+1,x,z;𝐱i)\displaystyle\Lambda(t\_{i+1},x,z;\mathbf{x}\_{i}) | =λ0​𝔼ℙ0​[d​μd​μ𝒯0​(x1,…,xi,Xti+1,…,XtN)|Xti+1=x+z]𝔼ℙ0​[d​μd​μ𝒯0​(x1,…,xi,Xti+1,…,XtN)|Xti+1=x]\displaystyle=\lambda^{0}\frac{\mathbb{E}^{\mathbb{P}^{0}}\left[\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}(x\_{1},\ldots,x\_{i},X\_{t\_{i+1}},\ldots,X\_{t\_{N}})\;\big|\;X\_{t\_{i+1}}=x+z\right]}{\mathbb{E}^{\mathbb{P}^{0}}\left[\frac{\mathrm{d}\mu}{\mathrm{d}\mu^{0}\_{\mathcal{T}}}(x\_{1},\ldots,x\_{i},X\_{t\_{i+1}},\ldots,X\_{t\_{N}})\;\big|\;X\_{t\_{i+1}}=x\right]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =λ0​μi+1​(x1,…,xi,x+z)μi+10​(x1,…,xi,x+z)​μi+10​(x1,…,xi,x)μi+1​(x1,…,xi,x)\displaystyle=\lambda^{0}\frac{\mu\_{i+1}(x\_{1},\ldots,x\_{i},x+z)}{\mu^{0}\_{i+1}(x\_{1},\ldots,x\_{i},x+z)}\frac{\mu^{0}\_{i+1}(x\_{1},\ldots,x\_{i},x)}{\mu\_{i+1}(x\_{1},\ldots,x\_{i},x)} |  |

hence we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ​(ti+1,x,z;𝐱i)=λ0​fti+1−ti0​(x−xi)fti+1−ti0​(x+z−xi)​μi+1​(x1,…,xi,x+z)μi+1​(x1,…,xi,x).\displaystyle\Lambda(t\_{i+1},x,z;\mathbf{x}\_{i})=\lambda^{0}\frac{f^{0}\_{t\_{i+1}-t\_{i}}(x-x\_{i})}{f^{0}\_{t\_{i+1}-t\_{i}}(x+z-x\_{i})}\frac{\mu\_{i+1}(x\_{1},\ldots,x\_{i},x+z)}{\mu\_{i+1}(x\_{1},\ldots,x\_{i},x)}. |  | (4.6) |

Notice that by Theorem [3.1](https://arxiv.org/html/2602.20011v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") we get that λt∗​(z)=Λ​(t,Xt−,z;𝐗ti)\lambda^{\*}\_{t}(z)=\Lambda(t,X\_{t^{-}},z;\mathbf{X}\_{t\_{i}}) is well-defined and predictable with respect to the natural filtration of the process, as required for the construction of the controlled jump–diffusion. This predictability property is explicit in ([4.2](https://arxiv.org/html/2602.20011v1#S4.E2 "In Proposition 4.1. ‣ 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) and ([4.6](https://arxiv.org/html/2602.20011v1#S4.E6 "In Remark 4.1. ‣ 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), where the dependence on the past is expressed exclusively through values of the time series observed at strictly earlier times.

Thanks to Proposition [4.1](https://arxiv.org/html/2602.20011v1#S4.Thmtheorem1 "Proposition 4.1. ‣ 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."), we get expressions of the drift and intensity of jumps involving the expectation with respect to μ\mu. This is particularly convenient as this formulation allows to construct estimators in which the expectation under μ\mu is approximated using the initial time series sampled from the target distribution.

Analytical expressions: using the notation introduced in the proof of Theorem [3.1](https://arxiv.org/html/2602.20011v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."), we have that the increments of the process XX under ℙ0\mathbb{P}^{0} satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xti+1−Xt=l​a​wσ​ti+1−t​Y+∑n=1N¯ti+1−tJnX\_{t\_{i+1}}-X\_{t}\stackrel{{\scriptstyle law}}{{=}}\sigma\sqrt{t\_{i+1}-t}\,Y+\sum\_{n=1}^{\bar{N}\_{t\_{i+1}-t}}J\_{n} |  | (4.7) |

for t∈[ti,ti+1)t\in[t\_{i},t\_{i+1}), i=0,…,N−1i=0,\ldots,N-1, where YY is a standard Gaussian random variable 𝒩​(0,Id)\mathcal{N}(0,I\_{d}), N¯\bar{N} is a Poisson process with intensity λ0\lambda^{0}, (Jn)n≥1(J\_{n})\_{n\geq 1} are i.i.d. random variables distributed according to ν0\nu^{0}, independent of YY and N¯\bar{N}. Conditioning on the values of N¯\bar{N}, we can explicitly specify the density function of increments as

|  |  |  |  |
| --- | --- | --- | --- |
|  | fti+1−t0​(z)=e−λ0​(ti+1−t)(2​π​(ti+1−t))d2​|detσ|​∑k≥0(λ0​(ti+1−t))kk!​∫ℝdexp⁡(−‖σ−1​(z−y)‖22​(ti+1−t))​(ν0)∗k​(d​y),f^{0}\_{t\_{i+1}-t}(z)=\frac{e^{-\lambda^{0}(t\_{i+1}-t)}}{\left(2\pi(t\_{i+1}-t)\right)^{\frac{d}{2}}|\det\sigma|}\sum\_{k\geq 0}\frac{(\lambda^{0}(t\_{i+1}-t))^{k}}{k!}\int\_{\mathbb{R}^{d}}\exp{\left(-\frac{\|\sigma^{-1}(z-y)\|^{2}}{2(t\_{i+1}-t)}\right)}(\nu^{0})^{\*k}(dy), |  | (4.8) |

for z∈ℝdz\in\mathbb{R}^{d}, where we denote by (ν0)∗k(\nu^{0})^{\*k} the kk-times convolution product of the measure ν0\nu^{0}. Plugging the density ([4.8](https://arxiv.org/html/2602.20011v1#S4.E8 "In 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) into the function Fi​(t,xi,x,xti+1)F\_{i}(t,x\_{i},x,x\_{t\_{i+1}}), we achieve the expressions for the drift and intensity of jumps. In the numerical simulations we will fix a particular choice for the distribution ν0\nu^{0} in order to have tractable estimators.

### 4.2 Kernel regression estimators

We derive the approximation through classical kernel methods of the conditional expectation under the target distribution μ\mu that appears in the expressions of the optimal drift and intensity. Consider data samples 𝐗(m)=(Xt1(m),…,XtN(m)),m=1,…,M\mathbf{X}^{(m)}=(X^{(m)}\_{t\_{1}},\ldots,X^{(m)}\_{t\_{N}}),\,m=1,\ldots,M from μ\mu. Starting from the expressions ([4.1](https://arxiv.org/html/2602.20011v1#S4.E1 "In Proposition 4.1. ‣ 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) and ([4.2](https://arxiv.org/html/2602.20011v1#S4.E2 "In Proposition 4.1. ‣ 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), we can estimate the conditional expectation under μ\mu using the Nadaraya-Watson kernel estimator. For i=0,…,N−1i=0,\ldots,N-1 fixed, 𝐱i∈(ℝd)i\mathbf{x}\_{i}\in(\mathbb{R}^{d})^{i}, x,z∈ℝdx,z\in\mathbb{R}^{d} we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | a^​(t,x;𝐱i)=σ​σ⊺​∑m=1M∇xFi​(t,xi,x,Xti+1(m))​𝐊𝐡ii​(𝐱i−𝐗ti(m))∑m=1MFi​(t,xi,x,Xti+1(m))​𝐊𝐡ii​(𝐱i−𝐗ti(m)),t∈[ti,ti+1),\hat{a}(t,x;\mathbf{x}\_{i})=\sigma\sigma^{\scriptscriptstyle{\intercal}}\frac{\displaystyle\sum\_{m=1}^{M}\nabla\_{x}F\_{i}(t,x\_{i},x,X^{(m)}\_{t\_{i+1}})\,\mathbf{K}^{i}\_{\mathbf{h}\_{i}}(\mathbf{x}\_{i}-\mathbf{X}^{(m)}\_{t\_{i}})}{\displaystyle\sum\_{m=1}^{M}F\_{i}(t,x\_{i},x,X^{(m)}\_{t\_{i+1}})\,\mathbf{K}^{i}\_{\mathbf{h}\_{i}}(\mathbf{x}\_{i}-\mathbf{X}^{(m)}\_{t\_{i}})},\quad t\in[t\_{i},t\_{i+1}), |  | (4.9) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ^​(t,x,z;𝐱i)=λ0​∑m=1MFi​(t,xi,x+z,Xti+1(m))​𝐊𝐡ii​(𝐱i−𝐗ti(m))∑m=1MFi​(t,xi,x,Xti+1(m))​𝐊𝐡ii​(𝐱i−𝐗ti(m)),t∈(ti,ti+1).\displaystyle\hat{\Lambda}(t,x,z;\mathbf{x}\_{i})=\lambda^{0}\frac{\displaystyle\sum\_{m=1}^{M}F\_{i}(t,x\_{i},x+z,X^{(m)}\_{t\_{i+1}})\,\mathbf{K}^{i}\_{\mathbf{h}\_{i}}(\mathbf{x}\_{i}-\mathbf{X}^{(m)}\_{t\_{i}})}{\displaystyle\sum\_{m=1}^{M}F\_{i}(t,x\_{i},x,X^{(m)}\_{t\_{i+1}})\,\mathbf{K}^{i}\_{\mathbf{h}\_{i}}(\mathbf{x}\_{i}-\mathbf{X}^{(m)}\_{t\_{i}})},\quad t\in(t\_{i},t\_{i+1}). |  | (4.10) |

Here 𝐊i\mathbf{K}^{i} is a multivariate kernel function operating on ii arguments of dimension dd. Given a bandwidth vector 𝐡i=(h1,…,hi)∈(0,∞)i\mathbf{h}\_{i}=(h\_{1},\ldots,h\_{i})\in(0,\infty)^{i}, we define the rescaled kernel by 𝐊𝐡ii​(𝐱i)=1h1d​⋯​hid​𝐊i​(x1h1,…,xihi)\mathbf{K}^{i}\_{\mathbf{h}\_{i}}(\mathbf{x}\_{i})=\frac{1}{h\_{1}^{d}\cdots h\_{i}^{d}}\mathbf{K}^{i}(\frac{x\_{1}}{h\_{1}},\ldots,\frac{x\_{i}}{h\_{i}}). In our simulations, we take hj=hh\_{j}=h for all j=1,…,ij=1,\ldots,i and the standard multiplicative kernel

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐊i​(x1,…,xi)=∏j=1iK​(xj)\mathbf{K}^{i}(x\_{1},\ldots,x\_{i})=\prod\_{j=1}^{i}K(x\_{j}) |  | (4.11) |

where K:ℝd→ℝK:\mathbb{R}^{d}\to\mathbb{R} is the kernel function K​(x)=(1−‖x‖2)2​𝟙‖x‖≤1K(x)=(1-\|x\|^{2})^{2}\mathbbm{1}\_{\|x\|\leq 1} on ℝd\mathbb{R}^{d}. At the same way, we can derive the estimator for the intensity at times tit\_{i}, for i=1,…,Ni=1,\ldots,N, starting from ([4.6](https://arxiv.org/html/2602.20011v1#S4.E6 "In Remark 4.1. ‣ 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) and deriving the corresponding kernel estimator. This gives fully data-driven estimators that we can compute to simulate the generative process.

## 5 Simulation techniques

In this section, we develop the main tools to perform the simulation of the optimal generative process ([3.3](https://arxiv.org/html/2602.20011v1#S3.E3 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")). We first focus on the jump term: indeed, as we get a Poisson random measure with state-dependent intensity under ℙ∗\mathbb{P}^{\*}, the jump term is no longer independent of the Brownian term, and this implies that we need to update the value of the intensity along each trajectory. We present a methodology to compute the instantaneous intensity, then we propose two algorithms for the SBJTS generative model, based on different simulation schemes for the jump-diffusion optimal process ([3.3](https://arxiv.org/html/2602.20011v1#S3.E3 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")). We refer to [[4](https://arxiv.org/html/2602.20011v1#bib.bib14 "Probability theory and stochastic processes"), [8](https://arxiv.org/html/2602.20011v1#bib.bib6 "Financial modelling with jump processes")] for the theory of the simulation of non-homogeneous jump processes.

### 5.1 Gaussian jump distribution

In order to derive tractable estimators of the drift and intensity of jumps for the numerical simulations, we want an easy expression for the function ([4.3](https://arxiv.org/html/2602.20011v1#S4.E3 "In Proposition 4.1. ‣ 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), and so in particular for the density of the increments ([4.8](https://arxiv.org/html/2602.20011v1#S4.E8 "In 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")). This means that we need a distribution ν0\nu^{0} whose convolutions admit explicit expressions. We could take for example a Dirac distribution, allowing for jumps with constant amplitude, but this choice is not very flexible. For this reason, in our simulations we work with Gaussian distributions.

Let ν0\nu^{0} be a multivariate Gaussian measure with mean c∈ℝdc\in\mathbb{R}^{d} and covariance matrix Γ∈ℝd×d\Gamma\in\mathbb{R}^{d\times d}, i.e.

|  |  |  |
| --- | --- | --- |
|  | ν0​(A)=∫A1(2​π)d2​det(Γ)12​exp⁡(−12​(z−c)⊺​Γ−1​(z−c))​dz,A∈ℬ​(ℝ).\nu^{0}(A)=\int\_{A}\frac{1}{(2\pi)^{\frac{d}{2}}\det(\Gamma)^{\frac{1}{2}}}\exp{\left(-\frac{1}{2}(z-c)^{\scriptscriptstyle{\intercal}}\Gamma^{-1}(z-c)\right)}\mathrm{d}z,\quad A\in\mathcal{B}(\mathbb{R}). |  |

Then, in ([4.7](https://arxiv.org/html/2602.20011v1#S4.E7 "In 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) there are all independent Gaussian random variables, so using the properties of convolution we get an explicit formula for the density function ([4.8](https://arxiv.org/html/2602.20011v1#S4.E8 "In 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) of the increments of the process XX under the reference probability measure ℙ0\mathbb{P}^{0}. Moreover, we make the following assumption:

* •

  σ=d​i​a​g​(σ1,…,σd)\sigma=diag(\sigma\_{1},\ldots,\sigma\_{d}), with σp>0\sigma\_{p}>0, p=1,…,dp=1,\ldots,d;
* •

  Γ=d​i​a​g​(γ12,…,γd2)\Gamma=diag(\gamma\_{1}^{2},\ldots,\gamma\_{d}^{2}), with γp>0\gamma\_{p}>0, p=1,…,dp=1,\ldots,d.

Hence, for t∈[ti,ti+1)t\in[t\_{i},t\_{i+1}), i=0​…,N−1i=0\ldots,N-1, the expression of the density fti+1−t0f^{0}\_{t\_{i+1}-t} of the increment Xti+1−XtX\_{t\_{i+1}}-X\_{t} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | fti+1−t0​(z)=∑k≥0(λ0​(ti+1−t))kk!​e−λ0​(ti+1−t)(2​π)d2​∏p=1dσp2​(ti+1−t)+k​γp2​exp⁡(−12​∑p=1d(zp−k​cp)2σp2​(ti+1−t)+k​γp2)f^{0}\_{t\_{i+1}-t}(z)=\sum\_{k\geq 0}\frac{(\lambda^{0}(t\_{i+1}-t))^{k}}{k!}\frac{e^{-\lambda^{0}(t\_{i+1}-t)}}{(2\pi)^{\frac{d}{2}}\prod\_{p=1}^{d}\sqrt{\sigma\_{p}^{2}(t\_{i+1}-t)+k\gamma\_{p}^{2}}}\exp{\left(-\frac{1}{2}\sum\_{p=1}^{d}\frac{(z\_{p}-kc\_{p})^{2}}{\sigma\_{p}^{2}(t\_{i+1}-t)+k\gamma\_{p}^{2}}\right)} |  | (5.1) |

for z∈ℝdz\in\mathbb{R}^{d}. For fixed i=0,…,N−1i=0,\ldots,N-1, t∈[ti,ti+1)t\in[t\_{i},t\_{i+1}), 𝐱i∈(ℝd)i\mathbf{x}\_{i}\in(\mathbb{R}^{d})^{i}, x∈ℝdx\in\mathbb{R}^{d}, we get an explicit expression for the function Fi​(t,xi,x,xi+1)F\_{i}(t,x\_{i},x,x\_{i+1}) defined in ([4.3](https://arxiv.org/html/2602.20011v1#S4.E3 "In Proposition 4.1. ‣ 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), which allows to compute

|  |  |  |
| --- | --- | --- |
|  | a​(t,x;𝐱i)=σ​σ⊺​𝔼μ​[∇xFi​(t,xi,x,Xti+1)|𝐗ti=𝐱i]𝔼μ​[Fi​(t,xi,x,Xti+1)|𝐗ti=𝐱i],a(t,x;\mathbf{x}\_{i})=\sigma\sigma^{\scriptscriptstyle{\intercal}}\frac{\mathbb{E}\_{\mu}\left[\nabla\_{x}F\_{i}(t,x\_{i},x,X\_{t\_{i+1}})|\mathbf{X}\_{t\_{i}}=\mathbf{x}\_{i}\right]}{\mathbb{E}\_{\mu}[F\_{i}(t,x\_{i},x,X\_{t\_{i+1}})|\mathbf{X}\_{t\_{i}}=\mathbf{x}\_{i}]}, |  |

where the computation of ∇xFi​(t,xi,x,xi+1)\nabla\_{x}F\_{i}(t,x\_{i},x,x\_{i+1}) is immediate as the only term to differentiate in the function Fi​(t,xi,x,xi+1)F\_{i}(t,x\_{i},x,x\_{i+1}) is the exponential term at numerator, and for

|  |  |  |
| --- | --- | --- |
|  | Λ​(t,x,z;𝐱i)=λ0​𝔼μ​[Fi​(t,xi,x+z,Xti+1)|𝐗ti=𝐱i]𝔼μ​[Fi​(t,xi,x,Xti+1)|𝐗ti=𝐱i].\Lambda(t,x,z;\mathbf{x}\_{i})=\lambda^{0}\,\frac{\mathbb{E}\_{\mu}[F\_{i}(t,x\_{i},x+z,X\_{t\_{i+1}})|\mathbf{X}\_{t\_{i}}=\mathbf{x}\_{i}]}{\mathbb{E}\_{\mu}[F\_{i}(t,x\_{i},x,X\_{t\_{i+1}})|\mathbf{X}\_{t\_{i}}=\mathbf{x}\_{i}]}. |  |

Then using estimators ([4.9](https://arxiv.org/html/2602.20011v1#S4.E9 "In 4.2 Kernel regression estimators ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) and ([4.10](https://arxiv.org/html/2602.20011v1#S4.E10 "In 4.2 Kernel regression estimators ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), we approximate the optimal drift αt∗=a​(t,Xt;𝐗ti)\alpha^{\*}\_{t}=a(t,X\_{t};\mathbf{X}\_{t\_{i}}) and the optimal intensity λt∗​(z)=Λ​(t,Xt−,z;𝐗ti)\lambda^{\*}\_{t}(z)=\Lambda(t,X\_{t^{-}},z;\mathbf{X}\_{t\_{i}}).

###### Remark 5.1.

This framework implies that the components of the Brownian motion and of the jump term of the process XX under ℙ0\mathbb{P}^{0} are assumed to be independent from each other, as we take diagonal matrices for σ\sigma and Γ\Gamma to remove the correlation terms and have more tractable expressions. Nevertheless, we will show in the numerical simulations that this simplification is not restrictive, as the proposed generative model is still able to effectively capture the correlations among the different components of the datasets that we consider in Section [7](https://arxiv.org/html/2602.20011v1#S7 "7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").

### 5.2 Simulation of the jump term

Once that we have fixed the distribution ν0\nu^{0}, we focus on the non-homogeneous Poisson process, whose instantaneous rate at any time tt is given by

|  |  |  |
| --- | --- | --- |
|  | Lt:=∫ℝdλt∗​(z)​ν0​(d​z),L\_{t}:=\int\_{\mathbb{R}^{d}}\lambda^{\*}\_{t}(z)\nu^{0}(\mathrm{d}z), |  |

and the size of the jumps follows the distribution

|  |  |  |
| --- | --- | --- |
|  | λt∗​(z)​ν0Lt.\frac{\lambda^{\*}\_{t}(z)\nu^{0}}{L\_{t}}. |  |

In order to simulate this jump term, for t∈(ti,ti+1)t\in(t\_{i},t\_{i+1}), i=0,…,N−1i=0,\ldots,N-1, and given the value Xt−=xX\_{t}^{-}=x, we approximate λt∗​(z)\lambda^{\*}\_{t}(z) using the kernel estimator ([4.10](https://arxiv.org/html/2602.20011v1#S4.E10 "In 4.2 Kernel regression estimators ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) and LtL\_{t} with

|  |  |  |  |
| --- | --- | --- | --- |
|  | L^​(t,x;𝐱i):=∫ℝdΛ^​(t,x,z;𝐱i)​ν0​(d​z),\hat{L}(t,x;\mathbf{x}\_{i}):=\int\_{\mathbb{R}^{d}}\hat{\Lambda}(t,x,z;\mathbf{x}\_{i})\nu^{0}(\mathrm{d}z), |  | (5.2) |

which for example can be computed using the Gauss-Hermite quadrature formula. Then we can sample the jump amplitude according to the distribution Λ^​(t,x,z;𝐱i)​ν0L^​(t,x;𝐱i)\frac{\hat{\Lambda}(t,x,z;\mathbf{x}\_{i})\nu^{0}}{\hat{L}(t,x;\mathbf{x}\_{i})} with different numerical methods.

However, in our simulations we consider the following strategy to rewrite the term λt∗​(z)​ν0\lambda^{\*}\_{t}(z)\nu^{0}, which enables both a more efficient computation of L^​(t,x;𝐱i)\hat{L}(t,x;\mathbf{x}\_{i}) and an easy way to sample the jump amplitude. Denoting by g​(z)g(z) the density of the Gaussian measure ν0\nu^{0} with respect to the Lebesgue measure, and using the estimator ([4.10](https://arxiv.org/html/2602.20011v1#S4.E10 "In 4.2 Kernel regression estimators ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ^​(t,x,z;𝐱i)​g​(z)=λ0D​∑m=1M∑j≥0wj,m(2​π)d2​∏p=1dσp2​(ti+1−t)+j​γp2​exp⁡(−12​∑p=1d(zp−(Xti+1,p(m)−xp−j​cp))2σp2​(ti+1−t)+j​γp2)×1(2​π)d2​∏p=1dγp​exp⁡(−12​∑p=1d(zp−cp)2γp2)\hat{\Lambda}(t,x,z;\mathbf{x}\_{i})g(z)=\frac{\lambda^{0}}{D}\sum\_{m=1}^{M}\sum\_{j\geq 0}\frac{w\_{j,m}}{(2\pi)^{\frac{d}{2}}\prod\_{p=1}^{d}\sqrt{\sigma\_{p}^{2}(t\_{i+1}-t)+j\gamma\_{p}^{2}}}\exp{\left(-\frac{1}{2}\sum\_{p=1}^{d}\frac{(z\_{p}-(X^{(m)}\_{t\_{i+1},p}-x\_{p}-jc\_{p}))^{2}}{\sigma\_{p}^{2}(t\_{i+1}-t)+j\gamma\_{p}^{2}}\right)}\\ \times\frac{1}{(2\pi)^{\frac{d}{2}}\prod\_{p=1}^{d}\gamma\_{p}}\exp{\left(-\frac{1}{2}\sum\_{p=1}^{d}\frac{(z\_{p}-c\_{p})^{2}}{\gamma\_{p}^{2}}\right)} |  | (5.3) |

where DD is the denominator in the formula ([4.10](https://arxiv.org/html/2602.20011v1#S4.E10 "In 4.2 Kernel regression estimators ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), and

|  |  |  |  |
| --- | --- | --- | --- |
|  | wj,m=(λ0​(ti+1−t))jj!​e−λ0​(ti+1−t)​𝐊𝐡ii​(𝐱i−𝐗ti(m))∑k≥0(λ0​(ti+1−ti))kk!​e−λ0​(ti+1−ti)(2​π)d2​∏p=1dσp2​(ti+1−ti)+k​γp2​exp⁡(−12​∑p=1d(Xti+1,p(m)−xi,p−k​cp)2σp2​(ti+1−ti)+k​γp2)w\_{j,m}=\frac{\frac{(\lambda^{0}(t\_{i+1}-t))^{j}}{j!}e^{-\lambda^{0}(t\_{i+1}-t)}\,\mathbf{K}^{i}\_{\mathbf{h}\_{i}}(\mathbf{x}\_{i}-\mathbf{X}^{(m)}\_{t\_{i}})}{\displaystyle\sum\_{k\geq 0}\frac{(\lambda^{0}(t\_{i+1}-t\_{i}))^{k}}{k!}\frac{e^{-\lambda^{0}(t\_{i+1}-t\_{i})}}{(2\pi)^{\frac{d}{2}}\prod\_{p=1}^{d}\sqrt{\sigma\_{p}^{2}(t\_{i+1}-t\_{i})+k\gamma\_{p}^{2}}}\exp{\left(-\frac{1}{2}\sum\_{p=1}^{d}\frac{(X^{(m)}\_{t\_{i+1},p}-x\_{i,p}-kc\_{p})^{2}}{\sigma\_{p}^{2}(t\_{i+1}-t\_{i})+k\gamma\_{p}^{2}}\right)}} |  | (5.4) |

Using the property of convolution between Gaussian densities, we can rewrite each product of the sum in ([5.3](https://arxiv.org/html/2602.20011v1#S5.E3 "In 5.2 Simulation of the jump term ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) to get

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ^​(t,x,z;𝐱i)​g​(z)=λ0D​∑m=1M∑j≥0wj,m​Cj,m​gj,m​(z),\hat{\Lambda}(t,x,z;\mathbf{x}\_{i})g(z)=\frac{\lambda^{0}}{D}\sum\_{m=1}^{M}\sum\_{j\geq 0}w\_{j,m}\,C\_{j,m}\,g\_{j,m}(z), |  | (5.5) |

where we denote by gj,mg\_{j,m} the density of the multivariate Gaussian

|  |  |  |
| --- | --- | --- |
|  | 𝒩j,m:=𝒩​(ξj,m,Σj),\mathcal{N}\_{j,m}:=\mathcal{N}\left(\xi\_{j,m},\Sigma\_{j}\right), |  |

where ξj,m∈ℝd\xi\_{j,m}\in\mathbb{R}^{d}, Σj∈ℝd×ℝd\Sigma\_{j}\in\mathbb{R}^{d}\times\mathbb{R}^{d} are defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξj,m\displaystyle\xi\_{j,m} | =((Xti+1,p(m)−xp−j​cp)​γp2+cp​(σp2​(ti+1−t)+j​γp2)σp2​(ti+1−t)+(j+1)​γp2)p=1,…,d\displaystyle=\left(\frac{(X^{(m)}\_{t\_{i+1},p}-x\_{p}-jc\_{p})\gamma^{2}\_{p}+c\_{p}(\sigma\_{p}^{2}(t\_{i+1}-t)+j\gamma^{2}\_{p})}{\sigma\_{p}^{2}(t\_{i+1}-t)+(j+1)\gamma^{2}\_{p}}\right)\_{p=1,\ldots,d} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Σj\displaystyle\Sigma\_{j} | =d​i​a​g​(γp2​(σp2​(ti+1−t)+j​γp2)σp2​(ti+1−t)+(j+1)​γp2)p=1,…,d\displaystyle=diag\left(\frac{\gamma^{2}\_{p}(\sigma\_{p}^{2}(t\_{i+1}-t)+j\gamma^{2}\_{p})}{\sigma\_{p}^{2}(t\_{i+1}-t)+(j+1)\gamma^{2}\_{p}}\right)\_{p=1,\ldots,d} |  |

and by Cj,mC\_{j,m} the normalizing constant

|  |  |  |
| --- | --- | --- |
|  | Cj,m=∏p=1d12​π​(σp2​(ti+1−t)+(j+1)​γp2)​exp⁡(−(Xti+1,p(m)−xp−(j+1)​cp)22​(σp2​(ti+1−t)+(j+1)​γp2)),C\_{j,m}=\prod\_{p=1}^{d}\frac{1}{\sqrt{2\pi(\sigma\_{p}^{2}(t\_{i+1}-t)+(j+1)\gamma\_{p}^{2})}}\exp{\left(-\frac{(X^{(m)}\_{t\_{i+1},p}-x\_{p}-(j+1)c\_{p})^{2}}{2(\sigma\_{p}^{2}(t\_{i+1}-t)+(j+1)\gamma\_{p}^{2})}\right)}, |  |

for m=1,…,Mm=1,\ldots,M, j≥0j\geq 0. Therefore we get the Gaussian mixture ([5.5](https://arxiv.org/html/2602.20011v1#S5.E5 "In 5.2 Simulation of the jump term ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")). Substituting this mixture into ([5.2](https://arxiv.org/html/2602.20011v1#S5.E2 "In 5.2 Simulation of the jump term ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), the evaluation of the integral

|  |  |  |
| --- | --- | --- |
|  | L^​(t,x;𝐱i)=∫ℝdλ0D​∑m=1M∑j≥0wj,m​Cj,m​gj,m​(z)​d​z\hat{L}(t,x;\mathbf{x}\_{i})=\int\_{\mathbb{R}^{d}}\frac{\lambda^{0}}{D}\sum\_{m=1}^{M}\sum\_{j\geq 0}w\_{j,m}\,C\_{j,m}\,g\_{j,m}(z)\mathrm{d}z |  |

leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | L^​(t,x;𝐱i)=λ0D​∑m=1M∑j≥0wj,m​Cj,m.\hat{L}(t,x;\mathbf{x}\_{i})=\frac{\lambda^{0}}{D}\sum\_{m=1}^{M}\sum\_{j\geq 0}w\_{j,m}\,C\_{j,m}. |  | (5.6) |

Also the simulation of the jump size J∼Λ^​(t,x,z;𝐱i)​ν0L^​(t,x;𝐱i)J\sim\frac{\hat{\Lambda}(t,x,z;\mathbf{x}\_{i})\nu^{0}}{\hat{L}(t,x;\mathbf{x}\_{i})} is now straightforward, as we choose a pair of indices (j,m)(j,m) according to the probabilities wj,m​Cj,m∑j,mwj,m​Cj,m\frac{w\_{j,m}C\_{j,m}}{\sum\_{j,m}w\_{j,m}C\_{j,m}}, and generate the random variable JJ from the corresponding multivariate Gaussian distribution 𝒩j,m\mathcal{N}\_{j,m}. Notice that this methodology yields a reduction in computational complexity while maintaining the accuracy, as it allows to avoid numerical quadrature in ([5.2](https://arxiv.org/html/2602.20011v1#S5.E2 "In 5.2 Simulation of the jump term ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) to sample efficiently the jump sizes, hence we use it in all the numerical simulations.

###### Remark 5.2.

Whenever numerical evaluation of the estimators is required in the simulations, the density of the increments ([5.1](https://arxiv.org/html/2602.20011v1#S5.E1 "In 5.1 Gaussian jump distribution ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) is approximated by truncating the infinite sum to a finite number of jumps nJ∈ℕn\_{J}\in\mathbb{N}, i.e. we consider

|  |  |  |
| --- | --- | --- |
|  | f0^ti+1−t​(z)=∑k≥0nJ(λ0​(ti+1−t))kk!​e−λ0​(ti+1−t)(2​π)d2​∏p=1dσp2​(ti+1−t)+k​γp2​exp⁡(−12​∑p=1d(zp−k​cp)2σp2​(ti+1−t)+k​γp2).\hat{f^{0}}\_{t\_{i+1}-t}(z)=\sum\_{k\geq 0}^{n\_{J}}\frac{(\lambda^{0}(t\_{i+1}-t))^{k}}{k!}\frac{e^{-\lambda^{0}(t\_{i+1}-t)}}{(2\pi)^{\frac{d}{2}}\prod\_{p=1}^{d}\sqrt{\sigma\_{p}^{2}(t\_{i+1}-t)+k\gamma\_{p}^{2}}}\exp{\left(-\frac{1}{2}\sum\_{p=1}^{d}\frac{(z\_{p}-kc\_{p})^{2}}{\sigma\_{p}^{2}(t\_{i+1}-t)+k\gamma\_{p}^{2}}\right)}. |  |

Then we can derive the truncated versions of ([4.9](https://arxiv.org/html/2602.20011v1#S4.E9 "In 4.2 Kernel regression estimators ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) and ([5.6](https://arxiv.org/html/2602.20011v1#S5.E6 "In 5.2 Simulation of the jump term ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), which are the final expressions used in our numerical simulations.

### 5.3 Euler scheme with Gaussian jumps

The first simulation scheme that we propose is a classical Euler scheme for the simulation of the optimal process ([3.3](https://arxiv.org/html/2602.20011v1#S3.E3 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")): more details for the Euler scheme for jump-diffusion processes can be found for example in [[14](https://arxiv.org/html/2602.20011v1#bib.bib20 "Convergence of a discretization scheme for jump-diffusion processes with state–dependent intensities"), [30](https://arxiv.org/html/2602.20011v1#bib.bib22 "The Euler scheme for Lévy driven stochastic differential equations")]. Given the set of observation times {t0=0,t1,…,tN}\{t\_{0}=0,t\_{1},\ldots,t\_{N}\}, we fix a discretization π\pi inside each interval [ti,ti+1][t\_{i},t\_{i+1}], i=0,…,N−1i=0,\ldots,N-1, given by ti,k=ti+kNπ​Δ​tit\_{i,k}=t\_{i}+\frac{k}{N\_{\pi}}\Delta t\_{i}, for k=0,…,Nπ−1k=0,\ldots,N\_{\pi}-1, where Δ​ti=ti+1−ti\Delta t\_{i}=t\_{i+1}-t\_{i} and NπN\_{\pi} is the number of uniform time steps. From equation ([3.3](https://arxiv.org/html/2602.20011v1#S3.E3 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) we have

|  |  |  |
| --- | --- | --- |
|  | Xti,k+1−Xti,k=∫ti,kti,k+1αt∗​dt+∫ti,kti,k+1σ​dWt+∫ti,kti,k+1∫ℝz​N​(d​t,d​z)X\_{t\_{i,k+1}}-X\_{t\_{i,k}}=\int\_{t\_{i,k}}^{t\_{i,k+1}}\alpha^{\*}\_{t}\mathrm{d}t+\int\_{t\_{i,k}}^{t\_{i,k+1}}\sigma\mathrm{d}W\_{t}+\int\_{t\_{i,k}}^{t\_{i,k+1}}\int\_{\mathbb{R}}zN(\mathrm{d}t,\mathrm{d}z) |  |

for i=0,…,N−1i=0,\ldots,N-1 and k=0,…,Nπ−1k=0,\ldots,N\_{\pi}-1. We denote by xi,kx\_{i,k} the Euler approximation of Xti,kX\_{t\_{i,k}}, and by 𝐱i=(x1,…,xi)\mathbf{x}\_{i}=(x\_{1},\ldots,x\_{i}) the values attained at the grid times (t1,…,ti)(t\_{1},\ldots,t\_{i}). Notice that the approximation of Xti,k+1X\_{t\_{i,k+1}} is performed using the information available at ti,kt\_{i,k}, in particular the value xi,kx\_{i,k} of Xti,kX\_{t\_{i,k}}. In our setting this means that both the drift and the jump intensity are evaluated at (ti,k,xi,k)(t\_{i,k},x\_{i,k}) and assumed to be constant in the whole time interval (ti,k,ti,k+1)(t\_{i,k},t\_{i,k+1}). In particular, the drift αt∗\alpha^{\*}\_{t} is approximated by a^​(ti,k,xi,k;𝐱i)\hat{a}(t\_{i,k},x\_{i,k};\mathbf{x}\_{i}) given by the kernel estimator ([4.9](https://arxiv.org/html/2602.20011v1#S4.E9 "In 4.2 Kernel regression estimators ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), while for the jump component the instantaneous rate L^​(t,x;𝐱i)\hat{L}(t,x;\mathbf{x}\_{i}) is approximated by L^​(ti,k,xi,k;𝐱i)\hat{L}(t\_{i,k},x\_{i,k};\mathbf{x}\_{i}) via ([5.6](https://arxiv.org/html/2602.20011v1#S5.E6 "In 5.2 Simulation of the jump term ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")). This results in a constant intensity over each Euler time step, allowing to simulate the number of jumps in (ti,k,ti,k+1)(t\_{i,k},t\_{i,k+1}) as

|  |  |  |
| --- | --- | --- |
|  | N¯i,k∼Poi​((ti,k+1−ti,k)​L^​(ti,k,xi,k;𝐱i)).\bar{N}\_{i,k}\sim\text{Poi}((t\_{i,k+1}-t\_{i,k})\hat{L}(t\_{i,k},x\_{i,k};\mathbf{x}\_{i})). |  |

Finally, for the size of the jumps, we simulate i.i.d. random variables (Jn)n=1,…,N¯i,k(J\_{n})\_{n=1,\ldots,\bar{N}\_{i,k}} with distribution

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jn∼Λ^​(ti,k,xi,k,z;𝐱i)​ν0L^​(ti,k,xi,k;𝐱i),J\_{n}\sim\frac{\hat{\Lambda}(t\_{i,k},x\_{i,k},z;\mathbf{x}\_{i})\nu^{0}}{\hat{L}(t\_{i,k},x\_{i,k};\mathbf{x}\_{i})}, |  | (5.7) |

using the model ([5.5](https://arxiv.org/html/2602.20011v1#S5.E5 "In 5.2 Simulation of the jump term ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) with Gaussian densities 𝒩j,m=𝒩​(ξj,m,Σj)\mathcal{N}\_{j,m}=\mathcal{N}\left(\xi\_{j,m},\Sigma\_{j}\right) defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξj,m\displaystyle\xi\_{j,m} | =((Xti+1,p(m)−xi,k,p−j​cp)​γp2+cp​(σp2​(ti+1−ti,k)+j​γp2)σp2​(ti+1−ti,k)+(j+1)​γp2)p=1,…,d\displaystyle=\left(\frac{(X^{(m)}\_{t\_{i+1},p}-x\_{i,k,p}-jc\_{p})\gamma^{2}\_{p}+c\_{p}(\sigma\_{p}^{2}(t\_{i+1}-t\_{i,k})+j\gamma^{2}\_{p})}{\sigma\_{p}^{2}(t\_{i+1}-t\_{i,k})+(j+1)\gamma^{2}\_{p}}\right)\_{p=1,\ldots,d} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Σj\displaystyle\Sigma\_{j} | =d​i​a​g​(γp2​(σp2​(ti+1−ti,k)+j​γp2)σp2​(ti+1−ti,k)+(j+1)​γp2)p=1,…,d\displaystyle=diag\left(\frac{\gamma^{2}\_{p}(\sigma\_{p}^{2}(t\_{i+1}-t\_{i,k})+j\gamma^{2}\_{p})}{\sigma\_{p}^{2}(t\_{i+1}-t\_{i,k})+(j+1)\gamma^{2}\_{p}}\right)\_{p=1,\ldots,d} |  |

where xi,k,px\_{i,k,p} denotes the pp-th component of xi,k∈ℝdx\_{i,k}\in\mathbb{R}^{d}. The complete Euler scheme of the process XX is then given by

|  |  |  |
| --- | --- | --- |
|  | xi,k+1=xi,k+(ti,k+1−ti,k)​a^​(ti,k,xi,k;𝐱i)+σ​(Wti,k+1−Wti,k)+∑n=1N¯i,kJnx\_{i,k+1}=x\_{i,k}+(t\_{i,k+1}-t\_{i,k})\,\hat{a}(t\_{i,k},x\_{i,k};\mathbf{x}\_{i})+\sigma(W\_{t\_{i,k+1}}-W\_{t\_{i,k}})+\sum\_{n=1}^{\bar{N}\_{i,k}}J\_{n} |  |

The pseudo-code of the complete generative model is presented in Algorithm [1](https://arxiv.org/html/2602.20011v1#alg1 "Algorithm 1 ‣ 5.3 Euler scheme with Gaussian jumps ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").

Algorithm 1  SBJTS simulation with Euler scheme

1:Input: data samples of time series (Xt1(m),…,XtN(m))(X^{(m)}\_{t\_{1}},\ldots,X^{(m)}\_{t\_{N}}), m=1,…,Mm=1,\ldots,M

2:Initialization: initial state x0=0x\_{0}=0

3:for i=0,…,N−1i=0,\ldots,N-1 do

4:  Initialize state xi,0=xix\_{i,0}=x\_{i}

5:  for k=0,…,Nπ−1k=0,\ldots,N\_{\pi}-1 do

6:   Compute a^​(ti,k,xi,k;𝐱i)\hat{a}(t\_{i,k},x\_{i,k};\mathbf{x}\_{i}) by kernel estimator ([4.9](https://arxiv.org/html/2602.20011v1#S4.E9 "In 4.2 Kernel regression estimators ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."))

7:   Sample εk∼𝒩​(0,1)\varepsilon\_{k}\sim\mathcal{N}(0,1)

8:   Compute L^​(ti,k,xi,k;𝐱i)\hat{L}(t\_{i,k},x\_{i,k};\mathbf{x}\_{i}) by kernel estimator ([5.6](https://arxiv.org/html/2602.20011v1#S5.E6 "In 5.2 Simulation of the jump term ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."))

9:   Generate N¯i,k∼Poi​((ti,k+1−ti,k)​L^​(ti,k,xi,k;𝐱i))\bar{N}\_{i,k}\sim\text{Poi}((t\_{i,k+1}-t\_{i,k})\hat{L}(t\_{i,k},x\_{i,k};\mathbf{x}\_{i}))

10:   Generate Jn∼Λ^​(ti,k,xi,k,z;𝐱i)​ν0​(d​z)L^​(ti,k,xi,k;𝐱i)J\_{n}\sim\frac{\hat{\Lambda}(t\_{i,k},x\_{i,k},z;\mathbf{x}\_{i})\nu^{0}(\mathrm{d}z)}{\hat{L}(t\_{i,k},x\_{i,k};\mathbf{x}\_{i})}, n=1,…,N¯i,kn=1,\ldots,\bar{N}\_{i,k}

11:   Compute

|  |  |  |
| --- | --- | --- |
|  | xi,k+1=xi,k+Δ​tiNπ​a^​(ti,k,xi,k;𝐱i)+σ​Δ​tiNπ​εk+∑n=1N¯i,kJnx\_{i,k+1}=x\_{i,k}+\frac{\Delta t\_{i}}{N\_{\pi}}\hat{a}(t\_{i,k},x\_{i,k};\mathbf{x}\_{i})+\sigma\sqrt{\frac{\Delta t\_{i}}{N\_{\pi}}}\varepsilon\_{k}+\sum\_{n=1}^{\bar{N}\_{i,k}}J\_{n} |  |

12:  end for

13:  Set xi+1=xi,Nπx\_{i+1}=x\_{i,N\_{\pi}}

14:end for

15:Return: (x1,…,xNx\_{1},\ldots,x\_{N})

### 5.4 Jump-adapted version of the Euler scheme

We propose an alternative simulation method of the process ([3.3](https://arxiv.org/html/2602.20011v1#S3.E3 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) based on the so called jump-adapted Euler scheme for jump-diffusion SDEs (for details see [[5](https://arxiv.org/html/2602.20011v1#bib.bib19 "Strong approximations of stochastic differential equations with jumps")]). We consider the jump-adapted time discretization {τ0=0,τ1,…,τn=T}\{\tau\_{0}=0,\,\tau\_{1},\ldots,\tau\_{n}=T\}, which is constructed taking the equidistant time discretization π\pi given by {ti,k}i=0,…,N−1,k=0​…,Nπ−1\{t\_{i,k}\}\_{i=0,\ldots,N-1,\,k=0\ldots,N\_{\pi}-1} and adding the jump times given by the Poisson term of the SDE. In this way, we can simulate only the diffusion part of the process XX when there are no jumps, and add the jump increment only at the jump times. In particular, we use the following scheme:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Xτn+1−=Xτn+ατn∗​(τn+1−τn)+σ​(Wτn+1−Wτn)Xτn+1=Xτn+1−+J if ​τn+1​ is a jump timeXτn+1=Xτn+1− if ​τn+1​ is not a jump time\displaystyle\begin{cases}X\_{\tau\_{n+1}^{-}}=X\_{\tau\_{n}}+\alpha^{\*}\_{\tau\_{n}}(\tau\_{n+1}-\tau\_{n})+\sigma(W\_{\tau\_{n+1}}-W\_{\tau\_{n}})\\ X\_{\tau\_{n+1}}=X\_{\tau\_{n+1}^{-}}+J&\text{ if }\tau\_{n+1}\text{ is a jump time}\\ X\_{\tau\_{n+1}}=X\_{\tau\_{n+1}^{-}}&\text{ if }\tau\_{n+1}\text{ is not a jump time}\end{cases} |  | (5.8) |

where JJ denotes the jump size at each jump time. Once again, the simulation of the jump times is performed during the simulation of the process as we work with time, state and path dependent intensity. Classical methods for simulating this type of jump-diffusion processes are based on the thinning algorithm (by Ogata [[28](https://arxiv.org/html/2602.20011v1#bib.bib21 "On Lewis’ simulation method for point processes"), [14](https://arxiv.org/html/2602.20011v1#bib.bib20 "Convergence of a discretization scheme for jump-diffusion processes with state–dependent intensities")]), which consists in taking an upper bound MM of the intensity function, simulating the jump times of a Poisson process with constant rate MM, and then perform an acceptance-rejection step to select only the jump times of the time inhomogeneous Poisson process. Improvements of the Ogata’s formulation in the case of a time and state dependent intensity allow to take a local bound which is an upper bound in space, but still a function of time (see [[11](https://arxiv.org/html/2602.20011v1#bib.bib23 "An introduction to the theory of point processes: volume i: elementary theory and methods")]).

Algorithm 2  SBJTS simulation with jump-adapted Euler scheme

1:Input: data samples of time series (X1(m),…,XN(m))(X^{(m)}\_{1},\ldots,X^{(m)}\_{N}), m=1,…,Mm=1,\ldots,M

2:Initialization: initial x0=0x\_{0}=0, tcurrent=0t\_{\text{current}}=0

3:Generate the first jump time tjump∼Exp​(L^​(tcurrent,x0;𝐱0))t\_{\text{jump}}\sim\text{Exp}(\hat{L}(t\_{\text{current}},x\_{0};\mathbf{x}\_{0}))

4:for i=0,…,N−1i=0,\ldots,N-1 do

5:  Initialize state x=xix=x\_{i}

6:  if tjump=tit\_{\text{jump}}=t\_{i} then

7:   tjump∼ti+Exp​(L^​(ti,xi;𝐱i))t\_{\text{jump}}\sim t\_{i}+\text{Exp}(\hat{L}(t\_{i},x\_{i};\mathbf{x}\_{i}))

8:  end if

9:  for k=0,…,Nπ−1k=0,\ldots,N\_{\pi}-1 do

10:   while tjump≤ti,k+1t\_{\text{jump}}\leq t\_{i,k+1} and ti<tjump<ti+1t\_{i}<t\_{\text{jump}}<t\_{i+1} do

11:     Δ​t=tjump−tcurrent\Delta t=t\_{\text{jump}}-t\_{\text{current}}

12:     Compute a^​(tcurrent,x;𝐱i)\hat{a}(t\_{\text{current}},x;\mathbf{x}\_{i}) by kernel estimator ([4.9](https://arxiv.org/html/2602.20011v1#S4.E9 "In 4.2 Kernel regression estimators ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) and sample ε∼𝒩​(0,1)\varepsilon\sim\mathcal{N}(0,1)

13:     x←x+Δ​t​a^​(tcurrent,x;𝐱i)+σ​Δ​t​εx\leftarrow x+\Delta t\,\hat{a}(t\_{\text{current}},x;\mathbf{x}\_{i})+\sigma\sqrt{\Delta t}\,\varepsilon

14:     tcurrent=tjumpt\_{\text{current}}=t\_{\text{jump}}

15:     Generate J∼Λ^​(tcurrent,x,z;𝐱i)​ν0​(d​z)J\sim\hat{\Lambda}(t\_{\text{current}},x,z;\mathbf{x}\_{i})\nu^{0}(\mathrm{d}z)

16:     Compute L^​(tcurrent,x;𝐱i)\hat{L}(t\_{\text{current}},x;\mathbf{x}\_{i}) by kernel estimator ([5.6](https://arxiv.org/html/2602.20011v1#S5.E6 "In 5.2 Simulation of the jump term ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."))

17:     Generate tjump∼tcurrent+Exp​(L^​(tcurrent,x;𝐱i))t\_{\text{jump}}\sim t\_{\text{current}}+\text{Exp}(\hat{L}(t\_{\text{current}},x;\mathbf{x}\_{i}))

18:     x←x+Jx\leftarrow x+J

19:   end while

20:   Δ​t=ti,k+1−tcurrent\Delta t=t\_{i,k+1}-t\_{\text{current}}

21:   Compute a^​(tcurrent,x;𝐱i)\hat{a}(t\_{\text{current}},x;\mathbf{x}\_{i}) by kernel estimator ([4.9](https://arxiv.org/html/2602.20011v1#S4.E9 "In 4.2 Kernel regression estimators ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) and sample ε∼𝒩​(0,1)\varepsilon\sim\mathcal{N}(0,1)

22:   x←x+Δ​t​a^​(tcurrent,x;𝐱i)+σ​Δ​t​εx\leftarrow x+\Delta t\,\hat{a}(t\_{\text{current}},x;\mathbf{x}\_{i})+\sigma\sqrt{\Delta t}\,\varepsilon

23:   tcurrent=ti,k+1t\_{\text{current}}=t\_{i,k+1}

24:  end for

25:  Set xi+1=xi,Nπx\_{i+1}=x\_{i,N\_{\pi}}

26:end for

27:Return: (x1,…,xN)(x\_{1},\ldots,x\_{N})

However, the main difficulty in our case lies in the fact that it is not straightforward to determine a uniform upper bound in both time and space for the function ([5.6](https://arxiv.org/html/2602.20011v1#S5.E6 "In 5.2 Simulation of the jump term ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")). Moreover, working with state-dependent intensity, before performing the acceptance-rejection step we should simulate the continuous part of the process (which in particular involves the drift estimation) until each candidate jump time: to reduce at most the rejections, which generates additional computational time, we should find a strict upper bound of the intensity, which makes the problem still more complicate. For these reasons, we choose an approach that differs from the thinning method, and it is based on an approximation of the intensity function. Indeed, at each jump time τn\tau\_{n} we simulate the following jump time τn+1\tau\_{n+1} taking as time interval an exponential random variable with rate L^\hat{L} evaluated at τn\tau\_{n}. This means that we approximate the intensity function by a piecewise constant function, evaluating it only at the jump times. Consequently, the simulation of the jump component in the continuous-time generative process XX inevitably introduces a simulation error. However, rather than analyzing the error at the level of the SDE, we evaluate the performance of the generative model directly in terms of its ability to produce realistic synthetic time series, looking at specific metrics. In addition, this simulation strategy substantially reduces the computational cost of the generative model compared with the classical Euler scheme employed in Algorithm [1](https://arxiv.org/html/2602.20011v1#alg1 "Algorithm 1 ‣ 5.3 Euler scheme with Gaussian jumps ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."), making it particularly suitable for repeated generation tasks. We present the complete jump-adapted scheme in Algorithm [2](https://arxiv.org/html/2602.20011v1#alg2 "Algorithm 2 ‣ 5.4 Jump-adapted version of the Euler scheme ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").

This jump-adapted method has an average number of operations depending on the intensity of jumps as the number of points in the time discretization increases with the intensity. This means that it is not efficient in the case of a large intensity, whereas the standard Euler scheme is not affected. But in the simulations that we consider in the following sections, we work with an average small number of jumps, making Algorithm [2](https://arxiv.org/html/2602.20011v1#alg2 "Algorithm 2 ‣ 5.4 Jump-adapted version of the Euler scheme ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") much faster than Algorithm [1](https://arxiv.org/html/2602.20011v1#alg1 "Algorithm 1 ‣ 5.3 Euler scheme with Gaussian jumps ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."). Moreover, in this case we manage to always guarantee the predictability of the intensity function (t,z)↦λt∗​(z)(t,z)\mapsto\lambda^{\*}\_{t}(z), as the estimator L^​(t,x;𝐱i)\hat{L}(t,x;\mathbf{x}\_{i}) is computed before updating the Euler scheme with the jump occurring at time tt. Finally, we assume that no jumps occur exactly at the observation times {ti}i=1,…,N\{t\_{i}\}\_{i=1,\ldots,N} as jumps are generated only within each interval (ti,ti+1)(t\_{i},t\_{i+1}). This is consistent with the classical Euler scheme, where it is natural to treat jumps as occurring strictly between discretization points.

## 6 Hyperparameter tuning

We outline the methodology for selecting appropriate values for the hyperparameters of our generative model. We describe a systematic approach that balances model performance and computational efficiency, ensuring that the chosen hyperparameters lead to accurate generative behavior. We present our calibration procedure in the one-dimensional setting. Specifically, we consider the optimal process ([3.3](https://arxiv.org/html/2602.20011v1#S3.E3 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) taking values in ℝ\mathbb{R}, with hyperparameters σ>0\sigma>0, ν0=𝒩​(c,γ2)\nu^{0}=\mathcal{N}(c,\gamma^{2}), where c∈ℝc\in\mathbb{R}, γ>0\gamma>0, and λ0>0\lambda^{0}>0. Although our analysis is carried out in dimension one, the same procedure will be applied componentwise in the multidimensional case (see Section [7.3](https://arxiv.org/html/2602.20011v1#S7.SS3 "7.3 Test on real data: Stock and Energy dataset ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")).

### 6.1 Selection of the kernel bandwidth and Markovianity order

At each time, the kernel estimators presented above require to take into account the whole past values of the time series in order to compute the drift and intensity. In the presence of long time series, this results in an increasing number of factors 𝐊𝐡ii​(𝐱i−𝐗ti(m))\mathbf{K}^{i}\_{\mathbf{h}\_{i}}(\mathbf{x}\_{i}-\mathbf{X}^{(m)}\_{t\_{i}}) equal to zero as we look at further dates. In order to solve this problem, we can force a shorter memory in the estimators, asking that the drift and intensity depend on k<Nk<N past values. We follow the approach of [[1](https://arxiv.org/html/2602.20011v1#bib.bib1 "Robust time series generation via Schrödinger Bridge: a comprehensive evaluation")], where the authors propose a test to fix the window of past values dependence, also called Markovianity order. In addiction, this test allows to calibrate also the bandwidth hh of the kernel ([4.11](https://arxiv.org/html/2602.20011v1#S4.E11 "In 4.2 Kernel regression estimators ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")): this parameter has a direct impact on the amount of data that are involved in the kernel estimation, hence it is important to perform a bias-variance tradeoff to achieve a good performance in the generation of time series.

Following the cross-validation test proposed in [[1](https://arxiv.org/html/2602.20011v1#bib.bib1 "Robust time series generation via Schrödinger Bridge: a comprehensive evaluation")], fix a train set X=(Xt1(m),…,XtN(m))m=1,…,MX=(X^{(m)}\_{t\_{1}},\ldots,X^{(m)}\_{t\_{N}})\_{m=1,\ldots,M} and a test set Y=(Yt1(q),…,YtN(q))q=1,…,QY=(Y^{(q)}\_{t\_{1}},\ldots,Y^{(q)}\_{t\_{N}})\_{q=1,\ldots,Q} of real data. For each qq, we take the time series Y(q)Y^{(q)} of the test set at the first N−1N-1 dates (Yt1(q),…,YtN−1(q))(Y^{(q)}\_{t\_{1}},\ldots,Y^{(q)}\_{t\_{N-1}}) and we generate LL realizations of the last value Y^tN(q),l\hat{Y}^{(q),l}\_{t\_{N}} using the Schrödinger bridge generative model and the train set XX. We do this for each couple (h,k)(h,k) varying in a grid of values, and we compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | M​S​Eh,k=1Q​∑q=1Q|1L​∑l=1LY^tN(q),l−YtN(q)|2MSE\_{h,k}=\frac{1}{Q}\sum\_{q=1}^{Q}\left|\frac{1}{L}\sum\_{l=1}^{L}\hat{Y}^{(q),l}\_{t\_{N}}-Y^{(q)}\_{t\_{N}}\right|^{2} |  | (6.1) |

In this way we can select the optimal (h∗,k∗)(h^{\*},k^{\*}) which gives the minimum value of the previous mean square error function. In practice, at time tit\_{i}, with i>k∗i>k^{\*}, we will work with the kernel product K¯i(m)=∏j=i−k∗+1iKh∗​(xj−Xtj(m))\bar{K}^{(m)}\_{i}=\prod\_{j=i-k^{\*}+1}^{i}K\_{h^{\*}}(x\_{j}-X^{(m)}\_{t\_{j}}). In the following numerical simulations, we use this test when we generate synthetic time series with both the SBTS algorithm [[17](https://arxiv.org/html/2602.20011v1#bib.bib5 "Generative modeling for time series via Schrödinger bridge")] and our SBJTS algorithm.

### 6.2 Selection of the parameters σ\sigma, λ0\lambda^{0}, cc and γ\gamma

We propose two possible tests that we can use to determine appropriate values of σ\sigma, λ0\lambda^{0}, cc and γ\gamma. Each method is implemented after generating synthetic time series: for a given set of parameters, synthetic series are produced, a suitable loss function or metric is computed, and the results are compared with the corresponding statistics of the original data to identify the parameters that achieve the best performance. This procedure implies that we need to fix a grid of pre-specified parameter values over which the test is conducted. We proceed with the following two tests:

* •

  Test on the distribution of the quadratic variation: we consider the empirical distribution of the quadratic variation of the time series, computed summing the squared increments for each path, both for the initial time series (giving the distribution porigp\_{\text{orig}}) and for the synthetic time series (psyntp\_{\text{synt}}). We aim to minimize the Wasserstein-2 distance of these two distributions numerically estimated:

  |  |  |  |
  | --- | --- | --- |
  |  | 𝒲2​(porig,psynt)=(infπ∈Π​(porig,psynt)∫|x−y|2​𝑑π​(x,y))12\mathcal{W}\_{2}(p\_{\text{orig}},p\_{\text{synt}})=\left(\inf\_{\pi\in\Pi(p\_{\text{orig}},p\_{\text{synt}})}\int|x-y|^{2}d\pi(x,y)\right)^{\frac{1}{2}} |  |

  For each set of parameter values, we select the one that minimizes this loss function.
* •

  Test on the discriminative score: we consider the metric of the discriminative score to assess how distinguishable generated time series are from real ones. It works by training a recurrent neural network discriminator that learns to classify sequences as real or synthetic. Then the final score is defined as the absolute difference between 0.5 and the accuracy of classification. If the discriminator can easily separate the two classes, its accuracy is close to 1, and the discriminative score is close to 0.5. Conversely, if the generated data closely mimics the real distribution, the discriminator performs no better than random guessing (≈50%\approx 50\% accuracy), yielding a score near zero. Thus, the test provides a quantitative way to evaluate the realism of generated time series. For each set of parameter values, we select the one that minimizes the score.

In the following section we explain how we can combine these two tests to choose the parameters.

### 6.3 Calibration procedure

Our first step concerns the choice of the parameter cc, the mean of the Gaussian distribution ν0\nu^{0}. In all our numerical experiments, we set c=0c=0, a choice motivated by the stationarity of the time series under consideration. Since we work exclusively with stationary data, alternative values of cc do not lead to any improvement in the performance of the generative model.

To determine suitable values for the other parameters, a key role is played by the quadratic variation of the optimal process ([3.3](https://arxiv.org/html/2602.20011v1#S3.E3 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) which we aim to simulate under the measure ℙ∗\mathbb{P}^{\*}. Indeed, reproducing accurately the quadratic variation is essential in order to obtain time series that exhibit statistical behavior comparable to the original data. To this end, we look at the empirical variance of the increments of the initial data, and we try to generate time series with the same variance. Since under ℙ∗\mathbb{P}^{\*} we do not have an explicit expression for the variance of increments depending only on the hyperparameters, it is more practical to consider first the optimal process under ℙ0\mathbb{P}^{0} to obtain a preliminary selection of appropriate parameter values for σ\sigma, λ0\lambda^{0}, and γ\gamma. In particular, we look at the following expression, for i=0,…,N−1i=0,\dots,N-1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Varμ​(Xti+1−Xti)=Δ​ti​(σ2+λ0​γ2)\text{Var}\_{\mu}(X\_{t\_{i+1}}-X\_{t\_{i}})=\Delta t\_{i}(\sigma^{2}+\lambda^{0}\gamma^{2}) |  | (6.2) |

where on the left hand side we have the empirical variance under the measure μ\mu of the increments of the time series data, and on the right hand side the theoretical variance of the increment of the optimal process under the reference probability ℙ0\mathbb{P}^{0} in the time interval [ti,ti+1)[t\_{i},t\_{i+1}) of length Δ​ti=ti+1−ti\Delta t\_{i}=t\_{i+1}-t\_{i}. In practice, in our setting all time increments have a fixed length Δ​t\Delta t, and on the left hand side we consider the average of the empirical variances computed over these intervals. In this way, we can select a reference measure ℙ0\mathbb{P}^{0} under which the increments of the optimal process have already a variance close to the one of the initial data. Moreover, we can easily find some upper bounds for σ\sigma and γ\gamma, using ([6.2](https://arxiv.org/html/2602.20011v1#S6.E2 "In 6.3 Calibration procedure ‣ 6 Hyperparameter tuning ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), and excluding values which cause instability of the algorithm. For each set of parameters satisfying condition ([6.2](https://arxiv.org/html/2602.20011v1#S6.E2 "In 6.3 Calibration procedure ‣ 6 Hyperparameter tuning ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), we then generate synthetic time series using the SBJTS generative model.

However, considering only the variance under ℙ0\mathbb{P}^{0} does not ensure that the variance of the increments of the time series generated under ℙ∗\mathbb{P}^{\*} is close to the one of the data. To address this limitation, we can calibrate better the parameters directly under the measure ℙ∗\mathbb{P}^{\*}. For each couple (σ,γ)(\sigma,\gamma) fixed, we tune the parameter λ0\lambda^{0} to minimize the Wasserstein-2 distance between the empirical distribution of the quadratic variation of the simulated time series under ℙ∗\mathbb{P}^{\*} and the one of the initial data. This refinement results in a more effective calibration procedure for the generative model. Finally, among the candidate sets of parameters, we choose the set minimizing the discriminative score computed between the real and the synthetic time series. We describe the calibration procedure in detail below.

Calibration procedure for the parameters hh, kk, σ\sigma, λ0\lambda^{0} and γ\gamma:

* •

  Fix initial kernel bandwidth hh and Markovianity order kk: choose initial values for hh and kk, allowing for a reasonable bias-variance tradeoff in the kernel estimators.
* •

  Preliminary parameter selection under ℙ0\mathbb{P}^{0}: using relation ([6.2](https://arxiv.org/html/2602.20011v1#S6.E2 "In 6.3 Calibration procedure ‣ 6 Hyperparameter tuning ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), determine suitable values of (σ,γ)(\sigma,\gamma) which do not cause instability of the algorithm.
* •

  Parameter selection under ℙ∗\mathbb{P}^{\*}: for each couple (σ\sigma, γ\gamma) determined at the previous point, tune the value of λ0\lambda^{0} to minimize the Wasserstein-2 distance of the empirical distribution of the time series quadratic variation.
* •

  Minimization of the discriminative score: for each candidate (σ,γ,λ0)(\sigma,\gamma,\lambda^{0}), generate synthetic time series and select the triplet that minimizes the discriminative score.
* •

  Validate the initial parameters: run again the Markovianity-bandwidth test with the selected (σ,γ,λ0)(\sigma,\gamma,\lambda^{0}) to confirm that the initial choice of hh and kk remains appropriate.
* •

  Final generation: use the finalized parameter set to perform the generation of synthetic time series.

###### Remark 6.1.

We emphasize that, in theory, the SBJTS generative model can operate for any choice of parameters, as no specific restrictions are imposed on their values. However, in practice, the model’s performance varies significantly across different parameter configurations. It is therefore important to devote attention to the preliminary calibration phase in order to identify suitable parameters. This aspect becomes particularly crucial when dealing with time series derived from real datasets rather than those simulated from parametric models. Nevertheless, this calibration step is not intended to determine the optimal set of parameters, as it is always performed as a grid search on some fixed candidates, but rather to identify reasonable configurations that ensure good performance.

## 7 Numerical tests

### 7.1 Test on simulated data: Merton model

![Refer to caption](images/Merton_paths.png)


Figure 7.1: Simulated trajectories of Merton process ([7.1](https://arxiv.org/html/2602.20011v1#S7.E1 "In 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) with parameters a=0a=0, b=2b=2, λη=10\lambda\_{\eta}=10, mJ=0m\_{J}=0 and vJ=0.8v\_{J}=0.8.

As a preliminary illustrative example, we propose to test our generative model starting from time series obtained by the simulation of trajectories of a Merton jump–diffusion process in dimension 1 defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt=Y0+a​t+b​Wt+∑i=0ηtJi,t∈[0,T],Y\_{t}=Y\_{0}+a\,t+b\,W\_{t}+\sum\_{i=0}^{\eta\_{t}}J\_{i},\quad t\in[0,T], |  | (7.1) |

with Y0=1Y\_{0}=1, where aa and bb are fixed parameters, W=(Wt)t≥0W=(W\_{t})\_{t\geq 0} is a standard Brownian motion, η=(ηt)t≥0\eta=(\eta\_{t})\_{t\geq 0} a Poisson process with constant intensity λη\lambda\_{\eta}. The jumps (Ji)i≥0(J\_{i})\_{i\geq 0} are assumed to be i.i.d. and driven by a Gaussian distribution 𝒩​(mJ,vJ2)\mathcal{N}(m\_{J},v\_{J}^{2}). Moreover, we impose the following condition: when the trajectory lies above Y0Y\_{0} negative jumps are sampled, and when it lies below Y0Y\_{0} positive jumps are sampled. This mechanism ensures that the resulting time series are inherently stationary, eliminating the need for subsequent transformations. We present the case where the volatility bb is moderate and the variance of the jump term permits the occurrence of relatively large jumps. Specifically, we consider a Merton model driven by ([7.1](https://arxiv.org/html/2602.20011v1#S7.E1 "In 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), fixing the parameters a=0a=0, b=2b=2, λη=10\lambda\_{\eta}=10, mJ=0m\_{J}=0 and vJ=0.8v\_{J}=0.8. Figure [7.1](https://arxiv.org/html/2602.20011v1#S7.F1 "Figure 7.1 ‣ 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") displays the sample paths obtained from five simulated realizations of the process. This configuration is intended to represent a realistic scenario in which the average jump frequency remains relatively low. We simulate M=1000M=1000 sample paths and then discretize the trajectories on the uniform grid t1,…,tNt\_{1},\ldots,t\_{N} with ti+1−ti=1252t\_{i+1}-t\_{i}=\frac{1}{252}, for i=0,…,N−1i=0,\ldots,N-1, T=tNT=t\_{N} and N=100N=100; to run the simulation scheme, we discretize again each interval [ti,ti+1][t\_{i},t\_{i+1}] with Nπ=100N\_{\pi}=100 steps. We test both the SBTS model (taken from [[17](https://arxiv.org/html/2602.20011v1#bib.bib5 "Generative modeling for time series via Schrödinger bridge")]) and our SBJTS model to compare the resulting metrics on 500 synthetic time series.

#### 7.1.1 For comparison: SBTS generation using the algorithm from [Hamdouche, Henry-Labordère and Pham, 2023]

![Refer to caption](images/cont_paths_3.png)


Figure 7.2: Generation of synthetic time series by SBTS model: sample paths of real time series (left) and sample paths of synthetic time series with h=0.1h=0.1 and k=1k=1 (right).

![Refer to caption](images/QQ_time_series_cont.png)


Figure 7.3: Generation of synthetic time series by SBTS model: QQ-plot between the quantiles of the empirical distributions of Xt50X\_{t\_{50}} on real and synthetic time series.

To evaluate the performance of the SBTS algorithm on Merton-generated time series, we adopt the procedure described in [[1](https://arxiv.org/html/2602.20011v1#bib.bib1 "Robust time series generation via Schrödinger Bridge: a comprehensive evaluation"), [17](https://arxiv.org/html/2602.20011v1#bib.bib5 "Generative modeling for time series via Schrödinger bridge")]. Starting from the original time series (Xti)i=0,…,N(X\_{t\_{i}})\_{i=0,\ldots,N}, we compute the increments Rti=Xti−Xti−1R\_{t\_{i}}=X\_{t\_{i}}-X\_{t\_{i-1}} for i=1,…,Ni=1,\ldots,N, and apply the rescaling

|  |  |  |  |
| --- | --- | --- | --- |
|  | R~t1:tN=Rt1:tN×Δ​tσ​(Rt1:tN)\tilde{R}\_{t\_{1}:t\_{N}}=R\_{t\_{1}:t\_{N}}\times\frac{\sqrt{\Delta t}}{\sigma(R\_{t\_{1}:t\_{N}})} |  | (7.2) |

where Δ​t=1252\Delta t=\frac{1}{252} is the interval between two consecutive dates, Rt1:tN=(Rt1,…,RtN)R\_{t\_{1}:t\_{N}}=(R\_{t\_{1}},\ldots,R\_{t\_{N}}) denotes the entire series of increments, and σ​(Rt1:tN)\sigma(R\_{t\_{1}:t\_{N}}) their empirical standard deviation. This normalization ensures that the rescaled time series have increments with empirical variance approximately equal to Δ​t\Delta t. We consider the diffusion process defined by

|  |  |  |
| --- | --- | --- |
|  | d​Xt=αt∗​d​t+d​Wt,t∈[0,T],\mathrm{d}X\_{t}=\alpha^{\*}\_{t}\mathrm{d}t+\mathrm{d}W\_{t},\quad t\in[0,T], |  |

where the drift αt∗\alpha^{\*}\_{t} is defined as in ([3.4](https://arxiv.org/html/2602.20011v1#S3.E4 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) and ([4.1](https://arxiv.org/html/2602.20011v1#S4.E1 "In Proposition 4.1. ‣ 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), but in this case the expression of ([4.3](https://arxiv.org/html/2602.20011v1#S4.E3 "In Proposition 4.1. ‣ 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) involves only the Gaussian densities given by the increments of the Brownian motion, without Poisson terms. To generate synthetic time series we use the Algorithm 1 of [[17](https://arxiv.org/html/2602.20011v1#bib.bib5 "Generative modeling for time series via Schrödinger bridge")], then it is sufficient to multiply by σ​(Rt1:tN)Δ​t\frac{\sigma(R\_{t\_{1}:t\_{N}})}{\sqrt{\Delta t}} to get to the initial scale. We remark that in the aforementioned works, the generative model is performed using the log-return series (Rti)i=1,…,N(R\_{t\_{i}})\_{i=1,\ldots,N}, in order to enhance stationarity: in our case we take only the increments as we already assume the stationarity in the model that generates the initial time series.

The only hyperparameters required are the kernel bandwidth hh and the Markovianity order kk of the time series. Using the test described in Section [6.1](https://arxiv.org/html/2602.20011v1#S6.SS1 "6.1 Selection of the kernel bandwidth and Markovianity order ‣ 6 Hyperparameter tuning ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") combined with the SBTS model, we get k=1k=1, consistent with the assumption of a Markovian model, and h=0.1h=0.1. We stress that when the time series have relatively low variance, very small values of hh may lead to the generation of trajectories that nearly replicate the original data. To prevent this issue, we select a range of hh values for the bandwidth test that ensures an adequate number of observations within the kernel estimators.

However, this generative model does not succeed in reproducing time series comparable to the original dataset. In Figure [7.2](https://arxiv.org/html/2602.20011v1#S7.F2 "Figure 7.2 ‣ 7.1.1 For comparison: SBTS generation using the algorithm from [Hamdouche, Henry-Labordère and Pham, 2023] ‣ 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") we display the first five simulated trajectories to have a qualitative representation of the behaviour of the synthetic time series: it is evident that working with a diffusion process, the generative model struggles to reproduce the large increments of the initial data attributed to the jump term. To illustrate this more clearly, we look at the distribution of XtiX\_{t\_{i}}, for some tit\_{i} fixed. Indeed, even if the constraint of the Schrödinger bridge problem is on the joint distribution of the time series, we can check whether the generative model captures also the marginal distributions. We compare the real and synthetic time series by examining the empirical quantiles of Xt50X\_{t\_{50}} and representing them in a QQ-plot in Figure [7.3](https://arxiv.org/html/2602.20011v1#S7.F3 "Figure 7.3 ‣ 7.1.1 For comparison: SBTS generation using the algorithm from [Hamdouche, Henry-Labordère and Pham, 2023] ‣ 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."). The deviation of the points from the reference diagonal clearly indicates that the SBTS model fails to reproduce the distribution at this time: the empirical quantiles of the synthetic data are systematically different from those of the real data, revealing a significant mismatch between the two distributions.

#### 7.1.2 SBJTS generation

![Refer to caption](images/disc_scores_Merton.png)


Figure 7.4: Discriminative scores tested on real time series and synthetic time series generated with different values of the hyperparameters (σ,γ,λ0)(\sigma,\gamma,\lambda^{0}).

To assess the performance of the SBJTS model, we directly use the time series sampled from the Merton process without any rescaling. Instead, we calibrate the hyperparameters of the generative model to reproduce the key statistical characteristics of the original data. In this case, we consider the optimal process ([3.3](https://arxiv.org/html/2602.20011v1#S3.E3 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) in dimension 1, hence σ∈ℝ+\sigma\in\mathbb{R}^{+}, and ν0=𝒩​(c,γ2)\nu^{0}=\mathcal{N}(c,\gamma^{2}) is a Gaussian distribution with c∈ℝc\in\mathbb{R}, γ∈ℝ+\gamma\in\mathbb{R}^{+}. We generate synthetic time series and present numerical experiments evaluating the algorithm’s performance.

![Refer to caption](images/paths_time_series_data.png)

![Refer to caption](images/paths_synth_case1.png)

![Refer to caption](images/paths_synth_case2.png)

Figure 7.5: Generation of synthetic time series by SBJTS model: sample paths of real time series (left), sample paths of synthetic time series with the choice h=0.3h=0.3, k=1k=1, σ=2\sigma=2, λ0=5\lambda^{0}=5, c=0c=0, and γ=0.8\gamma=0.8 (case (i) - middle), sample paths of synthetic time series with the choice h=0.3h=0.3, k=1k=1, σ=1\sigma=1, λ0=70\lambda^{0}=70, c=0c=0, and γ=1\gamma=1 (case (ii) - right).



![Refer to caption](images/QQ_ex1_a.png)

![Refer to caption](images/QQ_ex1_b.png)

Figure 7.6: Generation of synthetic time series by SBJTS model: QQ-plot between the quantiles of the increments of initial time series and synthetic time series generated by SBTS and SBJTS in case (i) (left) and in case (ii) (right).

Calibration of the hyperparameters.
Following the calibration procedure outlined in Section [6.3](https://arxiv.org/html/2602.20011v1#S6.SS3 "6.3 Calibration procedure ‣ 6 Hyperparameter tuning ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."), we aim to determine suitable values for the parameters hh, kk, σ\sigma, λ0\lambda^{0}, cc and γ\gamma. In this example using Merton time series, we begin by setting k=1k=1, consistent with the Markovian nature of the Merton model, and choose h∈[0.1,0.3]h\in[0.1,0.3]. We fix c=0c=0. Empirically, values of σ<0.5\sigma<0.5 or σ>3\sigma>3 fail to reproduce the empirical quadratic variation of the increments and result in synthetic time series with high discriminative scores. Accordingly, we test σ∈{0.5,1,2,3}\sigma\in\{0.5,1,2,3\}. For each value of σ\sigma, using relation ([6.2](https://arxiv.org/html/2602.20011v1#S6.E2 "In 6.3 Calibration procedure ‣ 6 Hyperparameter tuning ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), we identify suitable values of γ\gamma (and a corresponding λ0\lambda^{0}); moreover, we find that γ<1\gamma<1 leads to numerical instability, while γ>1.5\gamma>1.5 produces synthetic series with excessively large jumps, causing the kernel estimators to vanish. Therefore, we test γ∈{0.5,0.8,1,1.5,2,3}\gamma\in\{0.5,0.8,1,1.5,2,3\}. For each pair (σ,γ)(\sigma,\gamma), we tune the value λ0\lambda^{0} via the test on the distribution of the quadratic variation (see Section [6.2](https://arxiv.org/html/2602.20011v1#S6.SS2 "6.2 Selection of the parameters 𝜎, 𝜆⁰, 𝑐 and 𝛾 ‣ 6 Hyperparameter tuning ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")): in this way, we identify parameter triples (σ,γ,λ0)(\sigma,\gamma,\lambda^{0}) for which the synthetic time series have quadratic variation distribution close to the same distribution on real time series. Finally, for each choice of (σ,γ,λ0)(\sigma,\gamma,\lambda^{0}) among these candidates, we run the generative model and compute the discriminative score comparing the synthetic data to the real data. Figure [7.4](https://arxiv.org/html/2602.20011v1#S7.F4 "Figure 7.4 ‣ 7.1.2 SBJTS generation ‣ 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") reports the scores obtained for the different tested parameters in a calibration test: we observe that the parameter combinations (σ,γ,λ0)(\sigma,\gamma,\lambda^{0}) yielding the lowest scores are those close to the true Merton parameters a,b,λη,mJ,vJa,b,\lambda\_{\eta},m\_{J},v\_{J} used to generate the initial time series. This behaviour is expected, and we indeed use this toy example to validate the calibration procedure. However, the dynamics ([3.3](https://arxiv.org/html/2602.20011v1#S3.E3 "In Theorem 3.1. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) induced by our generative model differ from the original Merton process: in particular, the Schrödinger-bridge construction introduces a generally non-zero drift, typically adding extra variability, and a data-dependent jump term that does not coincide with the one in ([7.1](https://arxiv.org/html/2602.20011v1#S7.E1 "In 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")). Consequently, the fact that we can find a slight discrepancy between the score minimizers and the true parameter values is not contradictory. In this simulation, the lowest discriminative score is obtained testing the generative model with the following choice of hyperparameters: h=0.3h=0.3, k=1k=1, σ=1\sigma=1, λ0=70\lambda^{0}=70, c=0c=0, γ=1\gamma=1.

Numerical results. We present now the results of the SBJTS generative model. We fix h=0.3h=0.3, k=1k=1 and the two following set of hyperparameters:

1. (i)

   σ=2\sigma=2, λ0=5\lambda^{0}=5, c=0c=0, and γ=0.8\gamma=0.8: this choice corresponds exactly to the same volatility, mean and variance of jump sizes of the initial Merton process defined in ([7.1](https://arxiv.org/html/2602.20011v1#S7.E1 "In 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), with the intensity λ0\lambda^{0} fixed to match the quadratic variation distribution;
2. (ii)

   σ=1\sigma=1, λ0=70\lambda^{0}=70, c=0c=0, and γ=1\gamma=1: this choice is set to match the distribution of the quadratic variation of the initial time series, and it corresponds to the lowest value of discriminative score in Figure [7.4](https://arxiv.org/html/2602.20011v1#S7.F4 "Figure 7.4 ‣ 7.1.2 SBJTS generation ‣ 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") (≈0.023\approx 0.023).

As a first visual check of the trajectories, in Figure [7.5](https://arxiv.org/html/2602.20011v1#S7.F5 "Figure 7.5 ‣ 7.1.2 SBJTS generation ‣ 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") we can see that the generated time series by SBJTS model have a general behaviour that is closed to the initial dataset and, in contrast with the simulation presented in Figure [7.2](https://arxiv.org/html/2602.20011v1#S7.F2 "Figure 7.2 ‣ 7.1.1 For comparison: SBTS generation using the algorithm from [Hamdouche, Henry-Labordère and Pham, 2023] ‣ 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") for the SBTS case, now it is evident the presence of jumps. The QQ-plots in Figure [7.6](https://arxiv.org/html/2602.20011v1#S7.F6 "Figure 7.6 ‣ 7.1.2 SBJTS generation ‣ 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") is built starting from the computation of the quantiles on all the increments of the time series: we can see that the distribution of the increments generated by SBJTS model has quantiles that closely match those of the original data, while the same quantiles on synthetic series produced by SBTS model exhibit significant discrepancy.

![Refer to caption](images/increments_dist.png)


Figure 7.7: Comparison between the empirical distribution of the increments of real data and synthetic data generated via SBJTS model in case (ii): distribution of increments larger than 0.7 (left) and smaller than 0.7 (right).

![Refer to caption](images/QQ-plot_timeseries.png)


Figure 7.8: QQ-plot between the quantiles of the empirical distributions of Xt50X\_{t\_{50}} on real and synthetic time series generated via SBJTS model in case (ii).

To provide additional metrics in case (ii), we plot in Figure [7.7](https://arxiv.org/html/2602.20011v1#S7.F7 "Figure 7.7 ‣ 7.1.2 SBJTS generation ‣ 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") the overall distribution of increments, where we fix a threshold of 0.7 to distinguish between small and large increments in both the original and generated time series. In this way, we can see that our generative model not only accurately captures the distribution of the small increments, but also the tails of the distribution, i.e. the large increments. This is particularly important as the jump term primarily affect this part of the distribution: at discrete sampling times, small jumps are essentially indistinguishable from diffusion-driven increments, whereas large jumps are much easier to identify. Examining the tail behaviour shows that the jump component is indeed well reproduced by our generative model. In Figure [7.8](https://arxiv.org/html/2602.20011v1#S7.F8 "Figure 7.8 ‣ 7.1.2 SBJTS generation ‣ 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."), we focus on the marginal distribution of Xt50X\_{t\_{50}}, exactly as in Figure [7.3](https://arxiv.org/html/2602.20011v1#S7.F3 "Figure 7.3 ‣ 7.1.1 For comparison: SBTS generation using the algorithm from [Hamdouche, Henry-Labordère and Pham, 2023] ‣ 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."): once again we can notice the improvement in the QQ-plot with respect to the SBTS model. In Appendix [B.1](https://arxiv.org/html/2602.20011v1#A2.SS1 "B.1 Merton time series: distribution of jumps and simulated trajectories ‣ Appendix B Additional numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") we present additional tests on the Merton time series.

### 7.2 Pure jump case

In this section, we provide an example in dimension one dropping the assumption on σ\sigma to be non-degenerate, as we consider σ=0\sigma=0. In this way we recover the pure jump case, as we consider the solution ℙ∗\mathbb{P}^{\*} of the SBJTS problem to be the law of the process XX with dynamics

|  |  |  |
| --- | --- | --- |
|  | {d​Xt=∫ℝz​N​(d​t,d​z),t∈[0,T],X0=1\begin{cases}\mathrm{d}X\_{t}=\int\_{\mathbb{R}}zN(\mathrm{d}t,\mathrm{d}z),\quad t\in[0,T],\\ X\_{0}=1\end{cases} |  |

where NN has intensity measure λt∗​(z)​ν0​(d​z)​d​t\lambda^{\*}\_{t}(z)\nu^{0}(\mathrm{d}z)\mathrm{d}t. In this case, the expressions ([4.1](https://arxiv.org/html/2602.20011v1#S4.E1 "In Proposition 4.1. ‣ 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) and ([4.2](https://arxiv.org/html/2602.20011v1#S4.E2 "In Proposition 4.1. ‣ 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) can be derived working directly with the measures μ𝒯0​(d​x1,…,d​xN)\mu^{0}\_{\mathcal{T}}(\mathrm{d}x\_{1},\ldots,\mathrm{d}x\_{N}) and μ​(d​x1,…,d​xN)\mu(\mathrm{d}x\_{1},\ldots,\mathrm{d}x\_{N}), using the decomposition

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ𝒯0​(d​x1,…,d​xN)=∏i=0N−1μi+1|i0​(d​xi+1),\mu^{0}\_{\mathcal{T}}(\mathrm{d}x\_{1},\ldots,\mathrm{d}x\_{N})=\prod\_{i=0}^{N-1}\mu^{0}\_{i+1|i}(\mathrm{d}x\_{i+1}), |  | (7.3) |

where μi+1|i0​(d​xi+1)\mu^{0}\_{i+1|i}(\mathrm{d}x\_{i+1}) denotes the conditional law of Xti+1X\_{t\_{i+1}} under ℙ0\mathbb{P}^{0}, given the value of XtiX\_{t\_{i}}. Making the choice ν0=𝒩​(c,γ)\nu^{0}=\mathcal{N}(c,\gamma) with c∈ℝc\in\mathbb{R} and γ∈ℝ+\gamma\in\mathbb{R}^{+}, we have

|  |  |  |
| --- | --- | --- |
|  | μi+1|i0​(d​z)=e−λ0​(ti+1−ti)​δ0​(d​z)+∑k≥1e−λ0​(ti+1−ti)​(λ0​(ti+1−ti))kk!​2​π​k​γ2​exp⁡(−|z−k​c|22​k​γ2)​d​z.\displaystyle\mu^{0}\_{i+1|i}(\mathrm{d}z)=e^{-\lambda^{0}(t\_{i+1}-t\_{i})}\delta\_{0}(\mathrm{d}z)+\sum\_{k\geq 1}\frac{e^{-\lambda^{0}(t\_{i+1}-t\_{i})}(\lambda^{0}(t\_{i+1}-t\_{i}))^{k}}{k!\sqrt{2\pi k\gamma^{2}}}\exp{\left(-\frac{|z-kc|^{2}}{2k\gamma^{2}}\right)}\mathrm{d}z. |  |

Hence, if we consider

|  |  |  |
| --- | --- | --- |
|  | fti+1−t0​(xi+1−x)={e−λ0​(ti+1−t),if ​xi+1−x=0,∑k≥1(λ0​(ti+1−t))kk!​e−λ0​(ti+1−t)2​π​k​γ2​exp⁡(−|xi+1−x−k​c|22​k​γ2),otherwise,f^{0}\_{t\_{i+1}-t}(x\_{i+1}-x)=\begin{cases}e^{-\lambda^{0}(t\_{i+1}-t)},&\text{if }x\_{i+1}-x=0,\\ \sum\_{k\geq 1}\frac{(\lambda^{0}(t\_{i+1}-t))^{k}}{k!}\frac{e^{-\lambda^{0}(t\_{i+1}-t)}}{\sqrt{2\pi k\gamma^{2}}}\exp{\left(-\frac{|x\_{i+1}-x-kc|^{2}}{2k\gamma^{2}}\right)},&\text{otherwise},\end{cases} |  |

for t∈[ti,ti+1)t\in[t\_{i},t\_{i+1}), i=0,…,N1i=0,\ldots,N\_{1}, then we get the expressions of the function Fi​(t,xi,x,xi+1)F\_{i}(t,x\_{i},x,x\_{i+1}) defined in ([4.3](https://arxiv.org/html/2602.20011v1#S4.E3 "In Proposition 4.1. ‣ 4.1 Explicit formula for the drift and intensity of jumps ‣ 4 Approximation of the optimal drift and intensity ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) and the estimators of the drift and jump intensity. Moreover, also in this case we can use at the Gaussian mixture model to simulate jump sizes: when we have a jump JJ at time t∈(ti,ti+1)t\in(t\_{i},t\_{i+1}) and Xt−=xX\_{t^{-}}=x, we sample the amplitude of jump from the following distribution

|  |  |  |
| --- | --- | --- |
|  | J∼∑m=1M∑j≥0wj,m​𝒩j,mJ\sim\sum\_{m=1}^{M}\sum\_{j\geq 0}w\_{j,m}\,\mathcal{N}\_{j,m} |  |

where

|  |  |  |
| --- | --- | --- |
|  | wj,m=(λ0​(ti+1−t))jj!​e−λ0​(ti+1−t)2​π​(j+1)​γ2​exp⁡(−|Xti+1(m)−x−(j+1)​c|22​(j+1)​γ2)e−λ0​(ti+1−ti)​𝟙{xi=Xti+1(m)}+∑k≥1(λ0​(ti+1−ti))kk!​e−λ0​(ti+1−ti)2​π​k​γ2​exp⁡(−|Xti+1(m)−xi−k​c|22​k​γ2)​K​(𝐱i−𝐗ti(m))\displaystyle w\_{j,m}=\frac{\frac{(\lambda^{0}(t\_{i+1}-t))^{j}}{j!}\frac{e^{-\lambda^{0}(t\_{i+1}-t)}}{\sqrt{2\pi(j+1)\gamma^{2}}}\exp{\left(-\frac{|X^{(m)}\_{t\_{i+1}}-x-(j+1)c|^{2}}{2(j+1)\gamma^{2}}\right)}}{e^{-\lambda^{0}(t\_{i+1}-t\_{i})}\mathbbm{1}\_{\{x\_{i}=X^{(m)}\_{t\_{i+1}}\}}+\sum\_{k\geq 1}\frac{(\lambda^{0}(t\_{i+1}-t\_{i}))^{k}}{k!}\frac{e^{-\lambda^{0}(t\_{i+1}-t\_{i})}}{\sqrt{2\pi k\gamma^{2}}}\exp{\left(-\frac{|X^{(m)}\_{t\_{i+1}}-x\_{i}-kc|^{2}}{2k\gamma^{2}}\right)}}K(\mathbf{x}\_{i}-\mathbf{X}^{(m)}\_{t\_{i}}) |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒩0,m\displaystyle\mathcal{N}\_{0,m} | =δ{0}​(Xti+1(m)−x),\displaystyle=\delta\_{\{0\}}(X^{(m)}\_{t\_{i+1}}-x),\quad |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒩j,m\displaystyle\mathcal{N}\_{j,m} | =𝒩​(Xti+1(m)−xj+1,j​γ2j+1),if ​j≥1.\displaystyle=\mathcal{N}\left(\frac{X^{(m)}\_{t\_{i+1}}-x}{j+1},\frac{j\gamma^{2}}{j+1}\right),\quad\text{if }j\geq 1. |  |

In this pure jump case, we test the SBJTS model starting from simulated time series built as discretization of the sample paths of Ornstein–Uhlenbeck process. We consider the process in dimension d=1d=1 defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Yt=θ​(a−Yt)​d​t+b​d​Wt,t∈[0,T],Y0=1\begin{cases}\mathrm{d}Y\_{t}=\theta(a-Y\_{t})\,\mathrm{d}t+b\,\mathrm{d}W\_{t},\quad t\in[0,T],\quad\\ Y\_{0}=1\end{cases} |  | (7.4) |

and we fix θ=100\theta=100, a=1a=1, b=10b=10, T=100252T=\frac{100}{252} in order to have strongly mean reverting trajectories also when we look at time series sampled at low frequency. We want to show that working with our state-dependent jump process properly calibrated we can generate synthetic time series sampled from the trajectories of the pure jump process XX with metrics close to the ones of the initial time series. With respect to the previous example where there was also the diffusion term (and in particular the drift) which contributes to replicate the correct behaviour of the time series, here we focus on the jump term.

![Refer to caption](images/path_purely_jump1.png)


Figure 7.9: Paths of initial time series sampled by the trajectories of the OU process (left), and generated time series by SBJTS model in the case of pure jump generative process XX (right).



![Refer to caption](images/purely_jump_QV1.png)

![Refer to caption](images/purely_jump_CDF1.png)

Figure 7.10: Comparison between the quadratic variation distribution of the initial time series and the generated time series by SBJTS model in the pure jump case (left). Comparison between the empirical CDF computed on real increments and on generated increments by SBJTS model in the pure jump case (right).

Numerical results.
Starting from the trajectories of the process ([7.4](https://arxiv.org/html/2602.20011v1#S7.E4 "In 7.2 Pure jump case ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")), we fix Δ​ti=1252\Delta t\_{i}=\frac{1}{252} to get initial time series of length N=100N=100. We then generate 500 synthetic time series, choosing as hyperparameters of the generative model K=1K=1, h=0.3h=0.3, λ0=1000\lambda^{0}=1000, c=0c=0 and γ=0.1\gamma=0.1: on average, the purely jump process has trajectories with 400 jumps. See Figure [7.9](https://arxiv.org/html/2602.20011v1#S7.F9 "Figure 7.9 ‣ 7.2 Pure jump case ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") to compare the trajectories of 5 realizations of real and synthetic time series. In Figure [7.10](https://arxiv.org/html/2602.20011v1#S7.F10 "Figure 7.10 ‣ 7.2 Pure jump case ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") we first plot the empirical distribution of the quadratic variation computed along the real and synthetic time series to show that the chosen hyperparameters yield closely matching distributions. To evaluate the quality of the generation, we look at the empirical cumulative distribution function of the increments for both the real and synthetic time series: we can notice a good performance of our generative model, as the two functions perfectly overlap. In Appendix [B.2](https://arxiv.org/html/2602.20011v1#A2.SS2 "B.2 Pure jump generative model: high-frequency case ‣ Appendix B Additional numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."), we present the same test taking a finer time discretization: in this way we look at the time series obtained from the same trajectories but working at high frequency.

### 7.3 Test on real data: Stock and Energy dataset

In this section, we apply the SBJTS generative model to the case of real datasets which store historical observations of multiple variables related to specific domains, hence we adopt the multidimensional formulation of the problem. From the historical observations we construct time series samples by applying a sliding-window procedure with overlapping windows. In this way we construct time series Xt0:tN=(Xt0,…,XtN)X\_{t\_{0}:t\_{N}}=(X\_{t\_{0}},\ldots,X\_{t\_{N}}), and then we use the following two normalizations:

* •

  Base one normalization: (Xt0:tN,pXt0,p)\left(\frac{X\_{t\_{0}:t\_{N},p}}{X\_{t\_{0},p}}\right), for p=1,…,d{p=1,\ldots,d};
* •

  Standard normalization: (Xt1:tN,p−m​(Xt1:tN,p)v​(Xt1:tN,p))\left(\frac{X\_{t\_{1}:t\_{N},p}-m(X\_{t\_{1}:t\_{N},p})}{v(X\_{t\_{1}:t\_{N},p})}\right), for p=1,…,d{p=1,\ldots,d}, where m​(Xt1:tN,p)m(X\_{t\_{1}:t\_{N},p}) denotes the empirical mean of the pp-th component of the entire time series and v​(Xt1:tN,p)v(X\_{t\_{1}:t\_{N},p}) the empirical standard deviation.

Hence we proceed with the calibration of the hyperparameters again through a grid–search procedure. To reduce the computational complexity, we first tune the parameters component-wise in dimension 1, following the methodology described in Section [6](https://arxiv.org/html/2602.20011v1#S6 "6 Hyperparameter tuning ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."). Once suitable parameter candidates have been identified, we can perform a full dd-dimensional calibration, where synthetic multivariate time series are generated for each candidate combination, and the set achieving the lowest discriminative score is selected. The parameters hh, kk and λ0\lambda^{0} are finally fixed globally through dd-dimensional generation. After obtaining new time series, we invert the standard normalization to return to the base-one scale, in order to compare them to the original data.

We test our generative model on two distinct datasets, and we compare our results with several state-of-the-art generative models for time series that are evaluated in the literature in terms of both generation quality and predictive performance. In particular, we consider models based on GAN architectures [[35](https://arxiv.org/html/2602.20011v1#bib.bib8 "Time-series generative adversarial networks")], flow-matching approaches [[20](https://arxiv.org/html/2602.20011v1#bib.bib13 "Fm-ts: Flow matching for time series generation")], optimal transport methods [[33](https://arxiv.org/html/2602.20011v1#bib.bib12 "Cot-gan: Generating sequential data via causal optimal transport")], and diffusion-based generative models employing score-matching techniques [[24](https://arxiv.org/html/2602.20011v1#bib.bib10 "TSGM: Regular and irregular time-series generation using score-based generative models"), [26](https://arxiv.org/html/2602.20011v1#bib.bib11 "Utilizing image transforms and diffusion models for generative modeling of short and long time series")]. For consistency with the existing benchmark, we compare real and synthetic time series of fixed length N=24N=24.

* •

  Stock dataset: daily historical Google stocks data from 2004 to 2019, including six features: high, low, opening, closing, adjusted closing prices, and volume, hence d=6d=6. We choose the following parameters: σp=0.7\sigma\_{p}=0.7 for p=1,…,d−1p=1,\ldots,d-1, σd=1\sigma\_{d}=1, λ0=0.2\lambda^{0}=0.2, cp=0c\_{p}=0 for p=1,…,dp=1,\ldots,d, γp=0.1\gamma\_{p}=0.1 for p=1,…,d−1p=1,\ldots,d-1, γd=0.6\gamma\_{d}=0.6. We generate 2000 synthetic time series.
* •

  Energy dataset: electricity consumption and environmental conditions of a low-energy residential building over time, taken from [[6](https://arxiv.org/html/2602.20011v1#bib.bib9 "Data driven prediction models of energy use of appliances in a low-energy house")]. Its main target variable is the total energy consumed by household appliances. The dataset includes a variety of environmental and indoor features like the temperature readings from multiple rooms, relative humidity levels in the same areas, and outdoor measurements such as temperature, relative humidity, wind speed, atmospheric pressure. The data were collected every 10 minutes for 137 days. This dataset has 28 features, hence d=28d=28, and we select the parameters σ1=σ2=1.2\sigma\_{1}=\sigma\_{2}=1.2, σp=1\sigma\_{p}=1 for p=3,…,dp=3,\ldots,d, λ0=0.5\lambda^{0}=0.5, cp=0c\_{p}=0 for p=1,…,dp=1,\ldots,d, γ1=γ2=0.3\gamma\_{1}=\gamma\_{2}=0.3 and γp=0.1\gamma\_{p}=0.1, p=3,…,dp=3,\ldots,d. We generate 1000 synthetic time series.

Once that we perform the generation of synthetic time series, we measure the quality of the synthetic data using the following two metrics:

* •

  Discriminative score: see Section [6.2](https://arxiv.org/html/2602.20011v1#S6.SS2 "6.2 Selection of the parameters 𝜎, 𝜆⁰, 𝑐 and 𝛾 ‣ 6 Hyperparameter tuning ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* •

  Predictive score: we aim to determine whether the synthetic data preserve the predictive structure of the real sequences. The idea is that, if the generative model is well trained, the synthetic samples should capture the temporal dependencies and conditional distributions present in the original data. Concretely, we train on the synthetic dataset a recurrent neural network, which learns to predict the dd-th component from time steps t2t\_{2} to tNt\_{N}, given the first d−1d-1 components from t1t\_{1} to tN−1t\_{N-1}, minimizing the mean absolute error. Then the trained predictor is tested on the real dataset, and the global mean absolute error gives the final score.

Following the benchmark literature, we compute the scores using post-hoc recurrent neural networks (GRU type) with batch size 128 and hidden dimension max⁡(d2,1)\max(\frac{d}{2},1), using a single layer for the predictive score and two layers for the discriminative score. To determine a value of the scores, we compare the same number of synthetic time series and randomly selected real samples; for each dataset, the final score is the mean of the results of 10 runs of the test, the error is the standard deviation. In Table [7.1](https://arxiv.org/html/2602.20011v1#S7.T1 "Table 7.1 ‣ 7.3 Test on real data: Stock and Energy dataset ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") we report the discriminative and predictive scores obtained using the SBJTS generative model on the Stock dataset compared to the scores of the other generative models taken from the aforementioned papers, while in Table [7.2](https://arxiv.org/html/2602.20011v1#S7.T2 "Table 7.2 ‣ 7.3 Test on real data: Stock and Energy dataset ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") we report the same metrics on the Energy dataset. In both cases, we underline in bold the scores obtained with our generative model and the lowest scores among the state-of-the-art benchmark. We can conclude that the SBJTS has a very competitive performance on the two datasets. Indeed, in the case of the Stock dataset, the scores are really close to the ones obtained for the SBTS model, which has already a very good performance compared to the other generative models. On the other hand, in the case of the Energy dataset we manage to definitely improve the discriminative score obtained with the SBTS generative model, without deteriorating the predictive score. This is motivated by the fact that the dataset presents some components whose behaviour can be better reproduced adding the jump term in the generative process, leading to higher accuracy on the generation of synthetic time series using our generative model, and therefore a low discriminative score.

| Model | Disc. score | Pred. score |
| --- | --- | --- |
| TSGM-VP | 0.022 ±\pm 0.005 | 0.037 ±\pm 0.000 |
| TSGM-subVP | 0.021 ±\pm 0.008 | 0.037 ±\pm 0.000 |
| ImagenTime | 0.037 ±\pm 0.006 | 0.036 ±\pm 0.000 |
| T-Forcing | 0.226 ±\pm 0.035 | 0.038 ±\pm 0.001 |
| P-Forcing | 0.257 ±\pm 0.026 | 0.043 ±\pm 0.001 |
| TimeGAN | 0.102 ±\pm 0.031 | 0.038 ±\pm 0.001 |
| RCGAN | 0.196 ±\pm 0.027 | 0.040 ±\pm 0.001 |
| C-RNN-GAN | 0.399 ±\pm 0.028 | 0.038 ±\pm 0.000 |
| TimeVAE | 0.175 ±\pm 0.031 | 0.042 ±\pm 0.002 |
| WaveGAN | 0.217 ±\pm 0.022 | 0.041 ±\pm 0.001 |
| COT-GAN | 0.285 ±\pm 0.030 | 0.044 ±\pm 0.000 |
| FM-TS | 0.019 ±\pm 0.013 | 0.036 ±\pm 0.000 |
| SBTS | 0.010 ±\pm 0.008 | 0.017 ±\pm 0.000 |
| SBJTS | 0.036 ±\pm 0.031 | 0.018 ±\pm 0.005 |

Table 7.1: Discriminative score and predictive score for the Stock dataset: comparison of the performance of the SBJTS model with other generative models. In bold: the lowest discriminative and predictive score among the benchmark and the scores for the SBJTS model.



| Model | Disc. score | Pred. score |
| --- | --- | --- |
| TSGM-VP | 0.221 ±\pm 0.025 | 0.257 ±\pm 0.000 |
| TSGM-subVP | 0.198 ±\pm 0.025 | 0.252 ±\pm 0.000 |
| ImagenTime | 0.040 ±\pm 0.004 | 0.250 ±\pm 0.000 |
| T-Forcing | 0.483 ±\pm 0.004 | 0.315 ±\pm 0.005 |
| P-Forcing | 0.412 ±\pm 0.006 | 0.303 ±\pm 0.006 |
| TimeGAN | 0.236 ±\pm 0.012 | 0.273 ±\pm 0.004 |
| RCGAN | 0.336 ±\pm 0.017 | 0.292 ±\pm 0.005 |
| C-RNN-GAN | 0.499 ±\pm 0.001 | 0.483 ±\pm 0.005 |
| TimeVAE | 0.498 ±\pm 0.006 | 0.268 ±\pm 0.004 |
| WaveGAN | 0.363 ±\pm 0.012 | 0.307 ±\pm 0.007 |
| COT-GAN | 0.498 ±\pm 0.000 | 0.260 ±\pm 0.000 |
| FM-TS | 0.053 ±\pm 0.010 | 0.250 ±\pm 0.000 |
| SBTS | 0.356 ±\pm 0.020 | 0.072 ±\pm 0.001 |
| SBJTS | 0.065 ±\pm 0.031 | 0.080 ±\pm 0.011 |

Table 7.2: Discriminative score and predictive score for the Energy dataset: comparison of the performance of the SBJTS model with other generative models. In bold: the lowest discriminative and predictive score among the benchmark and the scores for the SBJTS model.

## 8 Conclusion

In this work, we addressed the problem of generating realistic time series by extending Schrödinger bridge–based generative models to stochastic dynamics with jumps. Our main contribution is the generalization of the continuous-time framework of Hamdouche et al. [[17](https://arxiv.org/html/2602.20011v1#bib.bib5 "Generative modeling for time series via Schrödinger bridge")] to probability measures defined on the space of càdlàg paths, allowing the reference process to be a jump–diffusion. Under a finite Kullback-Leibler divergence assumption, we characterized the solution of the resulting Schrödinger bridge problem, and explicitly identified the dynamics of the optimal controlled process which, sampled at the observation dates, generates synthetic time series with joint distribution matching a prescribed target distribution. We further proposed a systematic hyperparameter calibration strategy that improves the numerical efficiency and robustness of the generative model.

The proposed framework nevertheless presents some limitations. In particular, the choice of the reference measure remains restrictive, and while the model learns jump sizes from the data, it does not explicitly aim to reproduce the empirical distribution of jump times. Addressing these aspects — by allowing for more flexible reference dynamics or by directly modeling jump-time distributions — constitutes a natural direction for future research. Despite these limitations, the extension of Schrödinger bridge generative models to jump–diffusion dynamics leads to consistent improvements in numerical experiments on both simulated and real-world datasets. In particular, the proposed approach shows competitive performance compared with state-of-the-art generative models, notably in capturing heavy-tailed behavior, abrupt variations, and regime changes in realistic time series.

## Appendix A Predictability and Poisson measures

We recall some notions on predictability and Poisson random measures that are used throughout the analysis of Schrödinger bridges for jump–diffusions: for additional details, see [[2](https://arxiv.org/html/2602.20011v1#bib.bib7 "Lévy processes and stochastic calculus"), [21](https://arxiv.org/html/2602.20011v1#bib.bib24 "Limit theorems for stochastic processes")]. Let (Ω,ℱ,(ℱt)t≥0,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\geq 0},\mathbb{P}) be a filtered probability space. The predictable σ\sigma-algebra 𝒫pred\mathcal{P}\_{\mathrm{pred}} is defined as the smallest σ\sigma-algebra on Ω×[0,∞)\Omega\times[0,\infty) that makes measurable all the left-continuous, (ℱt)(\mathcal{F}\_{t})-adapted processes; equivalently, it is generated by sets of the form (s,t]×A(s,t]\times A with 0≤s<t0\leq s<t and A∈ℱsA\in\mathcal{F}\_{s}. A Poisson random measure on a measurable space (E,ℰ)(E,\mathcal{E}) with intensity measure mm is a mapping N:Ω×ℬ​([0,∞))×ℰ→ℕ∪{0}N:\Omega\times\mathcal{B}([0,\infty))\times\mathcal{E}\to\mathbb{N}\cup\{0\}, denoted by N​(d​t,d​z)N(\mathrm{d}t,\mathrm{d}z), such that for each A∈ℰA\in\mathcal{E} the process t↦N​([0,t]×A)t\mapsto N([0,t]\times A) is a Poisson process with mean m​([0,t]×A)m([0,t]\times A) and with independent increments across disjoint sets. In the stochastic-intensity setting, the intensity measure is assumed to take the form λt​(z)​ν​(d​z)​d​t\lambda\_{t}(z)\nu(\mathrm{d}z)\mathrm{d}t, where λt​(z)\lambda\_{t}(z) is a non-negative, 𝒫pred\mathcal{P}\_{\mathrm{pred}}-measurable process. Hence

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[N​((s,t]×A)|ℱs]=𝔼​[∫(s,t]×Aλu​(z)​ν​(d​z)​du|ℱs].\mathbb{E}[N((s,t]\times A)|\mathcal{F}\_{s}]=\mathbb{E}\left[\int\_{(s,t]\times A}\lambda\_{u}(z)\nu(\mathrm{d}z)\mathrm{d}u\Bigg|\mathcal{F}\_{s}\right]. |  |

We can introduce the compensated measure of NN, denoted by N~​(d​t,d​z)\tilde{N}(\mathrm{d}t,\mathrm{d}z), as

|  |  |  |
| --- | --- | --- |
|  | N~​(d​t,d​z)=N​(d​t,d​z)−λt​(z)​ν​(d​z)​d​t,\tilde{N}(\mathrm{d}t,\mathrm{d}z)=N(\mathrm{d}t,\mathrm{d}z)-\lambda\_{t}(z)\nu(\mathrm{d}z)\mathrm{d}t, |  |

which defines a local martingale on each measurable set. Finally, for any predictable function F:[0,T]×E×Ω→ℝF:[0,T]\times E\times\Omega\to\mathbb{R} satisfying

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫[0,T]×E|F​(t,z)|2​λs​(z)​ν​(d​z)​ds]<∞,\mathbb{E}\left[\int\_{[0,T]\times E}|F(t,z)|^{2}\lambda\_{s}(z)\nu(\mathrm{d}z)\mathrm{d}s\right]<\infty, |  |

the stochastic integral

|  |  |  |
| --- | --- | --- |
|  | Mt=∫(0,t]×EF​(s,z)​N~​(d​s,d​z)M\_{t}=\int\_{(0,t]\times E}F(s,z)\tilde{N}(\mathrm{d}s,\mathrm{d}z) |  |

is well defined and yields a square-integrable martingale.

## Appendix B Additional numerical tests

### B.1 Merton time series: distribution of jumps and simulated trajectories

![Refer to caption](images/QV_dist_jump_1a.png)

![Refer to caption](images/QV_dist_jump_1b.png)

Figure B.1: Comparison between the quadratic variation distribution of the initial time series and the generated time series in case (i) (left) and in case (ii) (right).



![Refer to caption](images/jump_sizes_1a.png)

![Refer to caption](images/jump_sizes_1b.png)

Figure B.2: Empirical distribution of the generated jump sizes in the case (i) (left) and in the case (ii) (right) estimated over 500 synthetic time series.

We report here additional plots obtained in the generation of time series starting from the Merton model. In Figure [B.1](https://arxiv.org/html/2602.20011v1#A2.F1 "Figure B.1 ‣ B.1 Merton time series: distribution of jumps and simulated trajectories ‣ Appendix B Additional numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") we can see that the two choices of parameters presented in Section [7.1](https://arxiv.org/html/2602.20011v1#S7.SS1 "7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") (denoted always with case (i) and (ii)) allow to generate time series whose quadratic variation distribution matches the quadratic variation distribution of the initial data. Figure [B.2](https://arxiv.org/html/2602.20011v1#A2.F2 "Figure B.2 ‣ B.1 Merton time series: distribution of jumps and simulated trajectories ‣ Appendix B Additional numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") displays the empirical distribution of the generated jump sizes in case (i) and (ii). In both cases the distribution of jump sizes is bimodal. This suggests that the generative model captures small increments of the original data primarily with the diffusion component, while the larger jumps are captured by the jump mechanism.

### B.2 Pure jump generative model: high-frequency case

Starting from the same trajectories of the Ornstein-Uhlenbeck process ([7.4](https://arxiv.org/html/2602.20011v1#S7.E4 "In 7.2 Pure jump case ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")) sampled for the numerical test in Section [7.2](https://arxiv.org/html/2602.20011v1#S7.SS2 "7.2 Pure jump case ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."), we change the time discretization of the interval [0,T][0,T] decreasing the time step Δ​ti=ti+1−ti\Delta t\_{i}=t\_{i+1}-t\_{i} to look at the time series at different frequencies, taking Δ​ti=1252⋅110\Delta t\_{i}=\frac{1}{252}\cdot\frac{1}{10}, and so we work with time series with length N=1000N=1000. Moreover, we fix K=1K=1, h=0.3h=0.3 and, for the jump term, we fix the following three sets of hyperparameters:

1. (a)

   λ0=1Δ​ti=25200\lambda^{0}=\frac{1}{\Delta t\_{i}}=25200, c=0c=0 and γ=0.1\gamma=0.1;
2. (b)

   λ0=12​Δ​ti=12600\lambda^{0}=\frac{1}{2\Delta t\_{i}}=12600, c=0c=0 and γ=0.06\gamma=0.06;
3. (c)

   λ0=2000\lambda^{0}=2000, c=0c=0 and γ=0.03\gamma=0.03.

In all these three cases, the hyperparameters are fixed to generate time series that have an empirical distribution of the quadratic variation close to the one of the initial data. The fact that we decrease both the intensity λ0\lambda^{0} and the standard deviation γ\gamma is given by the fact that under the measure ℙ∗\mathbb{P}^{\*} the expression of the intensity of jumps depends on both the parameters. Taking a smaller value of γ\gamma produce an increase of the intensity of jump, so we calibrate the value λ0\lambda^{0} to compensate this relation. Moving from (a) to (c) the average number of jumps in each simulated trajectory increases: around 1400-1500 in case (a), 1500-1600 in case (b), 1800-2000 in case (c). In Figure [B.3](https://arxiv.org/html/2602.20011v1#A2.F3 "Figure B.3 ‣ B.2 Pure jump generative model: high-frequency case ‣ Appendix B Additional numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") we plot 5 time series from the real dataset and from the synthetic one.

![Refer to caption](images/paths_purely_jump_2.png)


Figure B.3: Sample paths of initial time series (left) and generated time series by SBJTS (right) using the pure jump optimal process with the choice λ0=12600\lambda^{0}=12600, c=0c=0 and σ=0.06\sigma=0.06.



![Refer to caption](images/purely_jump_dist2a.png)

![Refer to caption](images/purely_jump_dist2b.png)

![Refer to caption](images/purely_jump_dist2c.png)

Figure B.4: Distribution of the amplitude of the jumps generated in the trajectories of the pure jump optimal process and comparison with the Gaussian distribution with the empirical mean and empirical standard deviation of the jump distribution in case (a) (left), (b) (middle) and (c) (right).



![Refer to caption](images/purely_jump_CDF2a.png)

![Refer to caption](images/purely_jump_CDF2b.png)

![Refer to caption](images/purely_jump_CDF2c.png)

Figure B.5: Empirical CDF of the increments in case (a) (left), (b) (middle) and (c) (right).

![Refer to caption](images/purely_jump_QQ2.png)


Figure B.6: QQ-plot between the quantiles of the empirical distributions of the real and synthetic increments in case (c).

In all the cases (a), (b) and (c) we have similar results in terms of QQ-plot and discriminative score. However, as we decrease the value of γ\gamma, some differences emerge in the empirical distribution of the generated jump amplitudes along the trajectories. In particular, the distribution shifts from being approximately centered and Gaussian-shaped to becoming bimodal (see Figure [B.4](https://arxiv.org/html/2602.20011v1#A2.F4 "Figure B.4 ‣ B.2 Pure jump generative model: high-frequency case ‣ Appendix B Additional numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.")). This behaviour can be interpreted as follows: when the number of jumps increases, the model tends to generate many small jumps, which cluster around either the positive or the negative mode depending on the current state of the process, in order to replicate the mean-reverting structure of the original data. Conversely, when fewer jumps are present, the model compensates by generating jump amplitudes that are more concentrated around zero, to balance the effect of the larger jumps. In Figure [B.5](https://arxiv.org/html/2602.20011v1#A2.F5 "Figure B.5 ‣ B.2 Pure jump generative model: high-frequency case ‣ Appendix B Additional numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."), we plot the empirical CDF of the increments. In all three cases, the CDF obtained from the synthetic data exhibits a discontinuity at zero, reflecting the positive probability of increments being exactly zero due to time intervals in which no jumps are sampled. This is motivated by the limitations of reproducing the arbitrarily small and frequent fluctuations of a diffusion by a pure finite-activity jump process, unless taking very small amplitude of jumps, which creates instability on our generative model. The same behaviour is represented in Figure [B.6](https://arxiv.org/html/2602.20011v1#A2.F6 "Figure B.6 ‣ B.2 Pure jump generative model: high-frequency case ‣ Appendix B Additional numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") via the QQ-plot.

### B.3 Real datasets: qualitative and quantitative results

In addition to the discriminative and predictive score reported in Section [7.3](https://arxiv.org/html/2602.20011v1#S7.SS3 "7.3 Test on real data: Stock and Energy dataset ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."), in Table [B.1](https://arxiv.org/html/2602.20011v1#A2.T1 "Table B.1 ‣ B.3 Real datasets: qualitative and quantitative results ‣ Appendix B Additional numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") we report the 5% and 95% empirical quantiles of the empirical distribution of Xt12X\_{t\_{12}} computed on real values and on synthetic values generated by the SBJTS model. Overall, the synthetic data closely match the empirical quantiles across all components, indicating that the model accurately captures the marginal distribution. In particular, also in the case of the sixth component, which presents large fluctuations, the model still reproduces the extreme quantiles with high accuracy.

Figure [B.7](https://arxiv.org/html/2602.20011v1#A2.F7 "Figure B.7 ‣ B.3 Real datasets: qualitative and quantitative results ‣ Appendix B Additional numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") represents the empirical correlation matrix between the first 5 components of the Energy dataset. As discussed in Section [7.3](https://arxiv.org/html/2602.20011v1#S7.SS3 "7.3 Test on real data: Stock and Energy dataset ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."), the generative process XX under the reference measure ℙ0\mathbb{P}^{0} assumes independent Brownian and jump components across dimensions. Nevertheless, through the learned drift and jump intensity under the optimal measure ℙ∗\mathbb{P}^{\*}, the generated time series successfully reproduce the cross-component correlations observed in the original dd-dimensional dataset.

Finally, for illustrative purposes, in Figure [B.8](https://arxiv.org/html/2602.20011v1#A2.F8 "Figure B.8 ‣ B.3 Real datasets: qualitative and quantitative results ‣ Appendix B Additional numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") we present the trajectories of 20 real and synthetic time series from the Energy dataset for variables with indices 1, 7, and 27, to provide an intuitive check of the generation accuracy more than a rigorous validation test. These plots highlight how the SBJTS generative model is able to reproduce the qualitative behavior of the different variables: it adapts to time series with stronger mean reversion, it captures varying levels of volatility or the presence of peaks, that can be attributed to a jump dynamics.

| Component | 5% Data | 5% SBJTS | 95% Data | 95% SBJTS |
| --- | --- | --- | --- | --- |
| 1 | 0.923 | 0.923 | 1.097 | 1.087 |
| 2 | 0.926 | 0.928 | 1.096 | 1.086 |
| 3 | 0.921 | 0.922 | 1.098 | 1.087 |
| 4 | 0.922 | 0.924 | 1.095 | 1.089 |
| 5 | 0.922 | 0.924 | 1.095 | 1.088 |
| 6 | 0.413 | 0.402 | 2.474 | 2.484 |

Table B.1: Quantiles of Stock dataset: comparison of the empirical quantiles of Xt12X\_{t\_{12}} computed on real data and synthetic data.

![Refer to caption](images/correl_matrix.png)


Figure B.7: Correlation matrix among 5 components of the real dataset (left) and synthetic dataset (right) in the case of the Energy dataset.



![Refer to caption](images/Energy_comp_1.png)


(a) Trajectories of 20 real time series (left) and synthetic time series (right) for the variable 1 (appliances energy consumption) of the dataset Energy.

![Refer to caption](images/Energy_comp_7.png)


(b) Trajectories of 20 real time series (left) and synthetic time series (right) for the variable 7 (temperature in laundry room area) of the dataset Energy.

![Refer to caption](images/Energy_comp_27.png)


(c) Trajectories of 20 real time series (left) and synthetic time series (right) for the variable 27 (random variable 1) of the dataset Energy.

Figure B.8: Trajectories of time series from the Energy dataset.

## References

* [1]
  A. Alouadi, B. Barreau, L. Carlier, and H. Pham (2025)
  Robust time series generation via Schrödinger Bridge: a comprehensive evaluation.
  In Proceedings of the 6th ACM International Conference on AI in Finance,
   pp. 906–914.
  Cited by: [§6.1](https://arxiv.org/html/2602.20011v1#S6.SS1.p1.3 "6.1 Selection of the kernel bandwidth and Markovianity order ‣ 6 Hyperparameter tuning ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [§6.1](https://arxiv.org/html/2602.20011v1#S6.SS1.p2.10 "6.1 Selection of the kernel bandwidth and Markovianity order ‣ 6 Hyperparameter tuning ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [§7.1.1](https://arxiv.org/html/2602.20011v1#S7.SS1.SSS1.p1.3 "7.1.1 For comparison: SBTS generation using the algorithm from [Hamdouche, Henry-Labordère and Pham, 2023] ‣ 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [2]
  D. Applebaum (2009)
  Lévy processes and stochastic calculus.
   Cambridge university press.
  Cited by: [Appendix A](https://arxiv.org/html/2602.20011v1#A1.p1.19 "Appendix A Predictability and Poisson measures ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [3]
  A. Baule (2025)
  Generative modelling with jump-diffusions.
  arXiv preprint arXiv:2503.06558.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px3.p3.1 "Generative models based on Schrödinger bridges. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [4]
  P. Brémaud (2020)
  Probability theory and stochastic processes.
   Springer.
  Cited by: [§5](https://arxiv.org/html/2602.20011v1#S5.p1.1 "5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [5]
  N. Bruti-Liberati and E. Platen (2007)
  Strong approximations of stochastic differential equations with jumps.
  Journal of Computational and Applied Mathematics 205 (2),  pp. 982–1001.
  Cited by: [§5.4](https://arxiv.org/html/2602.20011v1#S5.SS4.p1.4 "5.4 Jump-adapted version of the Euler scheme ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [6]
  L. M. Candanedo, V. Feldheim, and D. Deramaix (2017)
  Data driven prediction models of energy use of appliances in a low-energy house.
  Energy and buildings 140,  pp. 81–97.
  Cited by: [2nd item](https://arxiv.org/html/2602.20011v1#S7.I3.i2.p1.10 "In 7.3 Test on real data: Stock and Energy dataset ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [7]
  A. R. Cetingoz and C. Lehalle (2025)
  Synthetic data for portfolios: A throw of the dice will never abolish chance.
  arXiv preprint arXiv:2501.03993.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px1.p1.1 "Generative modeling task. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [8]
  R. Cont and P. Tankov (2003)
  Financial modelling with jump processes.
   Chapman and Hall/CRC.
  Cited by: [§5](https://arxiv.org/html/2602.20011v1#S5.p1.1 "5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [9]
  M. Cuturi (2013)
  Sinkhorn distances: Lightspeed computation of optimal transport.
  Advances in neural information processing systems 26.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px2.p2.5 "The Schrödinger bridge problem. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [10]
  P. Dai Pra (1991)
  A stochastic control approach to reciprocal diffusion processes.
  Applied mathematics and Optimization 23 (1),  pp. 313–329.
  Cited by: [§2](https://arxiv.org/html/2602.20011v1#S2.p4.7 "2 Setting and problem formulation ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [11]
  D. J. Daley and D. Vere-Jones (2003)
  An introduction to the theory of point processes: volume i: elementary theory and methods.
   Springer.
  Cited by: [§5.4](https://arxiv.org/html/2602.20011v1#S5.SS4.p1.7 "5.4 Jump-adapted version of the Euler scheme ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [12]
  V. De Bortoli, J. Thornton, J. Heng, and A. Doucet (2021)
  Diffusion Schrödinger bridge with applications to score-based generative modeling.
  Advances in Neural Information Processing Systems 34,  pp. 17695–17709.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px3.p1.1 "Generative models based on Schrödinger bridges. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [13]
  A. Genevay, G. Peyré, and M. Cuturi (2018)
  Learning generative models with Sinkhorn divergences.
  In International Conference on Artificial Intelligence and Statistics,
   pp. 1608–1617.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px1.p2.1 "Generative modeling task. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [14]
  P. Glasserman and N. Merener (2004)
  Convergence of a discretization scheme for jump-diffusion processes with state–dependent intensities.
  Proceedings of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences 460 (2041),  pp. 111–127.
  Cited by: [§5.3](https://arxiv.org/html/2602.20011v1#S5.SS3.p1.8 "5.3 Euler scheme with Gaussian jumps ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [§5.4](https://arxiv.org/html/2602.20011v1#S5.SS4.p1.7 "5.4 Jump-adapted version of the Euler scheme ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [15]
  I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio (2014)
  Generative adversarial nets.
  Advances in neural information processing systems 27.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px1.p1.1 "Generative modeling task. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [16]
  N. Gushchin, S. Kholkin, E. Burnaev, and A. Korotin (2024)
  Light and optimal schrödinger bridge matching.
  In Forty-first International Conference on Machine Learning,
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px2.p2.5 "The Schrödinger bridge problem. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [17]
  M. Hamdouche, P. Henry-Labordere, and H. Pham (2023)
  Generative modeling for time series via Schrödinger bridge.
  arXiv preprint arXiv:2304.05093, in revision for Journal of Machine Learning Research.
  Cited by: [1st item](https://arxiv.org/html/2602.20011v1#S1.I1.i1.p1.1 "In Our contributions and organization of the paper. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px3.p2.1 "Generative models based on Schrödinger bridges. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px3.p3.1 "Generative models based on Schrödinger bridges. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [§2](https://arxiv.org/html/2602.20011v1#S2.p3.2 "2 Setting and problem formulation ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [§3](https://arxiv.org/html/2602.20011v1#S3.1.p1.3 "Proof. ‣ 3 Solution of the Schrödinger bridge problem with jumps for time series ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [§6.1](https://arxiv.org/html/2602.20011v1#S6.SS1.p2.14 "6.1 Selection of the kernel bandwidth and Markovianity order ‣ 6 Hyperparameter tuning ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [§7.1.1](https://arxiv.org/html/2602.20011v1#S7.SS1.SSS1.p1.10 "7.1.1 For comparison: SBTS generation using the algorithm from [Hamdouche, Henry-Labordère and Pham, 2023] ‣ 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [§7.1.1](https://arxiv.org/html/2602.20011v1#S7.SS1.SSS1.p1.3 "7.1.1 For comparison: SBTS generation using the algorithm from [Hamdouche, Henry-Labordère and Pham, 2023] ‣ 7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [§7.1](https://arxiv.org/html/2602.20011v1#S7.SS1.p1.24 "7.1 Test on simulated data: Merton model ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [§8](https://arxiv.org/html/2602.20011v1#S8.p1.1 "8 Conclusion ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [Schrödinger bridges with jumps for time series generation
  ††thanks: This work is supported by the Chair Deep Learning and Statistics Qube RT,
  the BNP-PAR Chair “Futures of Quantitative Finance", the Chair “Risques Financiers", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.](https://arxiv.org/html/2602.20011v1#id3.id1.1 "Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.") .
* [18]
  P. Henry-Labordere (2019)
  From (Martingale) Schrödinger bridges to a new class of Stochastic Volatility Models.
  arXiv preprint arXiv:1904.04554.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px3.p2.1 "Generative models based on Schrödinger bridges. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [19]
  J. Ho, A. Jain, and P. Abbeel (2020)
  Denoising diffusion probabilistic models.
  Advances in neural information processing systems 33,  pp. 6840–6851.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px1.p1.1 "Generative modeling task. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [20]
  Y. Hu, X. Wang, L. Wu, H. Zhang, S. Z. Li, S. Wang, and T. Chen (2024)
  Fm-ts: Flow matching for time series generation.
  Cited by: [§7.3](https://arxiv.org/html/2602.20011v1#S7.SS3.p2.1 "7.3 Test on real data: Stock and Energy dataset ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [21]
  J. Jacod and A. Shiryaev (2013)
  Limit theorems for stochastic processes.
  Vol. 288, Springer Science & Business Media.
  Cited by: [Appendix A](https://arxiv.org/html/2602.20011v1#A1.p1.19 "Appendix A Predictability and Poisson measures ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [§2](https://arxiv.org/html/2602.20011v1#S2.p4.7 "2 Setting and problem formulation ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [22]
  A. Korotin, D. Selikhanovych, and E. Burnaev (2022)
  Neural optimal transport.
  arXiv preprint arXiv:2201.12220.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px1.p2.1 "Generative modeling task. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [23]
  C. Léonard (2014)
  A survey of the Schrödinger problem and some of its connections with optimal transport.
  Discrete and Continuous Dynamical Systems 34 (4),  pp. 1533–1574.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px2.p1.18 "The Schrödinger bridge problem. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [24]
  H. Lim, J. Lee, S. Park, M. Kim, and N. Park (2025)
  TSGM: Regular and irregular time-series generation using score-based generative models.
  arXiv preprint arXiv:2511.21335.
  Cited by: [§7.3](https://arxiv.org/html/2602.20011v1#S7.SS3.p2.1 "7.3 Test on real data: Stock and Energy dataset ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [25]
  Y. Lipman, R. T. Chen, H. Ben-Hamu, M. Nickel, and M. Le (2022)
  Flow matching for generative modeling.
  arXiv preprint arXiv:2210.02747.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px1.p1.1 "Generative modeling task. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [26]
  I. Naiman, N. Berman, I. Pemper, I. Arbiv, G. Fadlon, and O. Azencot (2024)
  Utilizing image transforms and diffusion models for generative modeling of short and long time series.
  Advances in Neural Information Processing Systems 37,  pp. 121699–121730.
  Cited by: [§7.3](https://arxiv.org/html/2602.20011v1#S7.SS3.p2.1 "7.3 Test on real data: Stock and Energy dataset ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [27]
  M. Nutz (2021)
  Introduction to entropic optimal transport.
  Lecture notes, Columbia University.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px2.p2.5 "The Schrödinger bridge problem. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [28]
  Y. Ogata (1981)
  On Lewis’ simulation method for point processes.
  IEEE transactions on information theory 27 (1),  pp. 23–31.
  Cited by: [§5.4](https://arxiv.org/html/2602.20011v1#S5.SS4.p1.7 "5.4 Jump-adapted version of the Euler scheme ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [29]
  D. Onken, S. W. Fung, X. Li, and L. Ruthotto (2021)
  Ot-flow: Fast and accurate continuous normalizing flows via optimal transport.
  Proceedings of the AAAI Conference on Artificial Intelligence 35 (10),  pp. 9223–9232.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px1.p2.1 "Generative modeling task. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [30]
  P. Protter and D. Talay (1997)
  The Euler scheme for Lévy driven stochastic differential equations.
  The Annals of Probability 25 (1),  pp. 393–423.
  Cited by: [§5.3](https://arxiv.org/html/2602.20011v1#S5.SS3.p1.8 "5.3 Euler scheme with Gaussian jumps ‣ 5 Simulation techniques ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [31]
  Y. Shi, V. De Bortoli, A. Campbell, and A. Doucet (2023)
  Diffusion Schrödinger bridge matching.
  Advances in Neural Information Processing Systems 36,  pp. 62183–62223.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px2.p2.5 "The Schrödinger bridge problem. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px3.p1.1 "Generative models based on Schrödinger bridges. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [32]
  Y. Song, S. Ermon, D. P. Kingma, and B. Poole (2021)
  Score-based generative modeling through stochastic differential equations.
  In International Conference on Learning Representations,
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px1.p1.1 "Generative modeling task. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [33]
  T. Xu, L. K. Wenliang, M. Munn, and B. Acciaio (2020)
  Cot-gan: Generating sequential data via causal optimal transport.
  Advances in neural information processing systems 33,  pp. 8798–8809.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px1.p2.1 "Generative modeling task. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair."),
  [§7.3](https://arxiv.org/html/2602.20011v1#S7.SS3.p2.1 "7.3 Test on real data: Stock and Energy dataset ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [34]
  E. B. Yoon, K. Park, S. Kim, and S. Lim (2023)
  Score-based generative models with Lévy processes.
  Advances in Neural Information Processing Systems 36,  pp. 40694–40707.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px3.p3.1 "Generative models based on Schrödinger bridges. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [35]
  J. Yoon, D. Jarrett, and M. Van der Schaar (2019)
  Time-series generative adversarial networks.
  Advances in Neural Information Processing Systems 32.
  Cited by: [§7.3](https://arxiv.org/html/2602.20011v1#S7.SS3.p2.1 "7.3 Test on real data: Stock and Energy dataset ‣ 7 Numerical tests ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [36]
  A. Zlotchevski and L. Chen (2024)
  Schrödinger Bridge Problem for Jump Diffusions.
  arXiv preprint arXiv:2411.13765.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px2.p1.18 "The Schrödinger bridge problem. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").
* [37]
  A. Zlotchevski and L. Chen (2025)
  The Schrödinger Bridge Problem for Jump Diffusions with Regime Switching.
  arXiv preprint arXiv:2511.06079.
  Cited by: [§1](https://arxiv.org/html/2602.20011v1#S1.SS0.SSS0.Px2.p1.18 "The Schrödinger bridge problem. ‣ 1 Introduction ‣ Schrödinger bridges with jumps for time series generation This work is supported by the Chair Deep Learning and Statistics Qube RT, the BNP-PAR Chair “Futures of Quantitative Finance\", the Chair “Risques Financiers\", by FiME, Laboratoire de Finance des Marchés de l’Energie, and the “Finance and Sustainable Development” EDF - CACIB Chair.").