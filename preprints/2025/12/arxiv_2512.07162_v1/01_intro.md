---
authors:
- Kieran A. Malandain
- Selim Kalici
- Hakob Chakhoyan
doc_id: arxiv:2512.07162v1
family_id: arxiv:2512.07162
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep
  Operator Networks'
url_abs: http://arxiv.org/abs/2512.07162v1
url_html: https://arxiv.org/html/2512.07162v1
venue: arXiv q-fin
version: 1
year: 2025
---


Hakob Chakhoyan
  
Selim Kalici
  
Kieran A. Malandain

###### Abstract

Real-time calibration of stochastic volatility models (SVMs) is computationally bottlenecked by the need to repeatedly solve coupled partial differential equations (PDEs). In this work, we propose DeepSVM, a physics-informed Deep Operator Network (PI-DeepONet) designed to learn the solution operator of the Heston model across its entire parameter space. Unlike standard data-driven deep learning (DL) approaches, DeepSVM requires no labelled training data. Rather, we employ a hard-constrained ansatz that enforces terminal payoffs and static no-arbitrage conditions by design. Furthermore, we use Residual-based Adaptive Refinement (RAR) to stabilize training in difficult regions subject to high gradients. Overall, DeepSVM achieves a final training loss of 𝟏𝟎−𝟓\mathbf{10^{-5}} and predicts highly accurate option prices across a range of typical market dynamics. While pricing accuracy is high, we find that the model’s derivatives (Greeks) exhibit noise in the at-the-money (ATM) regime, highlighting the specific need for higher-order regularization in physics-informed operator learning.

## I Introduction

Pricing European options under stochastic volatility models (SVMs) requires solving a two-dimensional parabolic partial differential equation (PDE) for each candidate set of market parameters. This becomes computationally expensive when calibrating the six free parameters of the Heston model [heston1993closed] to real-time, noisy market data, because the PDE solve must be repeated many times [srinivasanFastOptionPricing2025].

Recent advances in machine learning (ML) have begun to reshape the field of quantitative finance [kellyFinancialMachineLearning, fanDeepLearningSolving2025]. Specifically, Physics-Informed Neural Networks (PINNs) [raissi2019physics] have emerged as a powerful tool for solving financial PDEs without the need for large-scale, labeled datasets [noguerialonsoPhysicsInformedNeuralNetworks2023, hainautOptionPricingHeston2024]. However, standard PINNs typically learn a solution for a fixed set of parameters 𝝁\bm{\mu} that is determined at model initiation. Our goal is to replace numerical pricing with a neural operator [Lu\_2021\_DeepONet] that generalizes across parameter regimes, enabling near real-time pricing and calibration.

Crucially, this operator-learning paradigm fundamentally alters the computational economics of model calibration. In a typical volatility calibration routine, an optimizer must solve the pricing PDE thousands of times to fit the model to market quotes. While Finite Difference solvers and standard PINNs incur a high computational cost for every new parameter set queried, DeepSVM amortizes this cost entirely during the training phase. Once trained, the network provides near-instantaneous inference (𝒪​(1)\mathcal{O}(1) cost) across the global parameter space, effectively removing the bottleneck for real-time risk management and high-frequency trading applications.

The Heston model provides a realistic framework for option pricing by incorporating stochastic volatility, a key feature of financial markets. It assumes that an asset’s price SS follows a stochastic diffusion, while its variance ν\nu follows a correlated mean-reverting square-root process:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dSt\displaystyle\differential{S\_{t}} | =r​St​dt+νt​St​dWtS\displaystyle=rS\_{t}\differential{t}+\sqrt{\nu\_{t}}S\_{t}\,\differential{W^{S}\_{t}} |  | (1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dνt\displaystyle\differential{\nu\_{t}} | =κ​(θ−νt)​dt+σ​νt​dWtν,\displaystyle=\kappa(\theta-\nu\_{t})\differential{t}+\sigma\sqrt{\nu\_{t}}\differential{W^{\nu}\_{t}}, |  | (2) |

where the variables are labelled in Table [I](https://arxiv.org/html/2512.07162v1#S2.T1 "Table I ‣ II-C Parameter Space and Domain ‣ II Problem Formulation ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks"), and WS,WνW^{S},W^{\nu} are correlated Brownian motions with ⟨dWS,dWν⟩=ρ​dt\langle\differential{W^{S}},\differential{W^{\nu}}\rangle=\rho\differential{t}. We assume a zero dividend yield (q=0q=0) for this study, though the framework generalizes trivially.

In this work, we address the computational challenges of solving the Heston model by introducing DeepSVM. Our three primary contributions are identified as follows:

1. 1.

   We formulate the Heston pricing problem as an operator learning task, allowing for global generalization across market parameters 𝝁\bm{\mu} rather than a single instance solve.
2. 2.

   We introduce a hard-constrained ansatz architecture [lagaris1998artificial] to automatically satisfy the transformed terminal & boundary conditions, reducing the optimization search space.
3. 3.

   We demonstrate that a physics-informed approach, augmented via Residual-based Adaptive Refinement (RAR) [lu2021deepxde], can achieve high-fidelity pricing (comparable to an FD solver) without the need for expensive ground-truth data generation.

The remainder of this paper is organised thus: §[II](https://arxiv.org/html/2512.07162v1#S2 "II Problem Formulation ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks") details the mathematical formulation; §[III](https://arxiv.org/html/2512.07162v1#S3 "III Methodology: DeepSVM ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks") describes the DeepSVM architecture; and §[IV](https://arxiv.org/html/2512.07162v1#S4 "IV Results & Discussion ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks") presents numerical validation of our model.

## II Problem Formulation

The arbitrage-free price of a European option, V​(S,ν,t)V(S,\nu,t), is governed by the Feynman-Kac (FK) PDE derived from the Heston stochastic processes in Eqs. ([1](https://arxiv.org/html/2512.07162v1#S1.E1 "Equation 1 ‣ I Introduction ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks"))–([2](https://arxiv.org/html/2512.07162v1#S1.E2 "Equation 2 ‣ I Introduction ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks")). In order to facilitate efficient learning via neural networks, which perform better when key regions are centred around the origin [lecun2012efficient], we transform the coordinates to dimensionless quantities.

### II-A Log-Moneyness Transformation

Standard spot-price coordinates suffer from scaling issues, as the relevant domain for the asset price SS shifts with the strike price KK. Therefore, we introduce the log-moneyness coordinate xx:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x=ln⁡(SK),x=\ln(\frac{S}{K}), |  | (3) |

along with defining the time-to-maturity τ\tau:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ=T−t.\tau=T-t. |  | (4) |

where TT is the expiration time. We define the normalized option price u​(x,ν,τ)=V​(S,ν,t)/Ku(x,\nu,\tau)=V(S,\nu,t)/K. Thus, the Heston PDE transforms into the following parabolic equation for uu:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂u∂τ−𝒩​[u]=0,\partialderivative{u}{\tau}-\mathcal{N}[u]=0, |  | (5) |

where the differential operator 𝒩\mathcal{N} is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒩​[u]\displaystyle\mathcal{N}[u] | =(r−12​ν)​∂u∂x+ρ​σ​ν​∂2u∂x​∂ν\displaystyle=\left(r-\frac{1}{2}\nu\right)\partialderivative{u}{x}+\rho\sigma\nu\partialderivative{u}{x}{\nu} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​σ2​ν​∂2u∂ν2+12​ν​∂2u∂x2+κ​(θ−ν)​∂u∂ν−r​u.\displaystyle+\frac{1}{2}\sigma^{2}\nu\partialderivative[2]{u}{\nu}+\frac{1}{2}\nu\partialderivative[2]{u}{x}+\kappa(\theta-\nu)\partialderivative{u}{\nu}-ru. |  |

This transformation centers the ATM region at x=0x=0, creating a scale-invariant domain that simplifies the task for the neural operator we train.

### II-B Boundary and Terminal Conditions

The PDE ([5](https://arxiv.org/html/2512.07162v1#S2.E5 "Equation 5 ‣ II-A Log-Moneyness Transformation ‣ II Problem Formulation ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks")) must be solved subject to the terminal payoff condition at τ=0\tau=0 (i.e., t=Tt=T) and asymptotic boundary behaviours:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | u​(x,ν,τ=0)\displaystyle u(x,\nu,\tau=0) | =max⁡(ex−1,0)≡ϕ​(x),\displaystyle=\max(e^{x}-1,0)\equiv\phi(x), |  | (6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limx→∞u​(x,ν,τ)\displaystyle\lim\_{x\to\infty}u(x,\nu,\tau) | =ex−e−r​τ,\displaystyle=e^{x}-e^{-r\tau}, |  | (7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limx→−∞u​(x,ν,τ)\displaystyle\lim\_{x\to-\infty}u(x,\nu,\tau) | =0.\displaystyle=0. |  | (8) |

Further, as ν→0\nu\to 0, the second-order diffusion terms vanish, and ([5](https://arxiv.org/html/2512.07162v1#S2.E5 "Equation 5 ‣ II-A Log-Moneyness Transformation ‣ II Problem Formulation ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks")) simplifies to a hyperbolic transport equation, requiring no boundary condition at ν=0\nu=0 provided the Feller condition is satisfied.

### II-C Parameter Space and Domain

We formulate the pricing task as an operator learning problem for near-instantaneous pricing We seek to learn the mapping 𝒢:𝒫→𝒰\mathcal{G}:\mathcal{P}\to\mathcal{U}, where 𝒫⊂ℝ5\mathcal{P}\subset\mathbb{R}^{5} is the space of Heston parameters and 𝒰≡{u:Ω→ℝ}\mathcal{U}\equiv\{u:\Omega\to\mathbb{R}\} is the solution space over the domain Ω=(x,ν,τ)\Omega=(x,\nu,\tau). The specific ranges for the input parameters 𝝁∈𝒫\bm{\mu}\in\mathcal{P} are detailed in Table [I](https://arxiv.org/html/2512.07162v1#S2.T1 "Table I ‣ II-C Parameter Space and Domain ‣ II Problem Formulation ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks").

TABLE I: Parameter ranges and domain definitions. The Model Parameters form the input to the DeepONet Branch net, while the Domain Coordinates form the input to the Trunk net. The Feller condition 2​κ​θ>σ22\kappa\theta>\sigma^{2} is enforced during sampling.

|  |  |  |
| --- | --- | --- |
| Symbol | Description | Range |
| Model Parameters (𝝁\bm{\mu}) | | |
| κ\kappa | Mean reversion speed | [0.5, 3.0][0.5,\;3.0] |
| θ\theta | Long-run variance | [0.01, 0.20][0.01,\;0.20] |
| σ\sigma | Volatility of variance | [0.1, 1.0][0.1,\;1.0] |
| ρ\rho | Spot/variance corr. | [−0.95,−0.05][-0.95,\;-0.05] |
| rr | Risk-free rate | [0.00, 0.08][0.00,\;0.08] |
| Domain Coordinates (Ω\Omega) | | |
| xx | Log-moneyness ln⁡(S/K)\ln(S/K) | [−2.0, 2.0][-2.0,\;2.0] |
| ν\nu | Instantaneous Variance | [0.01, 0.40][0.01,\;0.40] |
| τ\tau | Time-to-maturity | [0.0, 1.0][0.0,\;1.0] |

## III Methodology: DeepSVM

To solve the operator learning problem defined in §[II](https://arxiv.org/html/2512.07162v1#S2 "II Problem Formulation ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks"), we
propose DeepSVM, a physics-informed DeepONet [wang2021learning]
augmented with a hard-constrained ansatz and adaptive sampling.

### III-A DeepONet architecture

We employ a DeepONet [Lu\_2021\_DeepONet] to approximate the solution
operator 𝒢\mathcal{G}. As illustrated in Fig. [1](https://arxiv.org/html/2512.07162v1#S3.F1 "Figure 1 ‣ III-A DeepONet architecture ‣ III Methodology: DeepSVM ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks"),
the architecture consists of two sub-networks:

1. 1.

   Branch net: a multi-layer perceptron (MLP) that encodes
   the input parameters 𝝁=(κ,θ,σ,ρ,r)\bm{\mu}=(\kappa,\theta,\sigma,\rho,r)
   into a latent embedding vector 𝐛​(𝝁)∈ℝp\mathbf{b}(\bm{\mu})\in\mathbb{R}^{p}.
2. 2.

   Trunk net: an MLP that encodes the spatiotemporal query
   coordinates (x,ν,τ)(x,\nu,\tau) into a basis vector
   𝐭​(x,ν,τ)∈ℝp\mathbf{t}(x,\nu,\tau)\in\mathbb{R}^{p}, where
   x=ln⁡(S/K)x=\ln(S/K) denotes log-moneyness.

The unconstrained output of the network is the inner product of these two
embeddings:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔑θ​(𝝁,x,ν,τ)=⟨𝐛​(𝝁),𝐭​(x,ν,τ)⟩,\mathfrak{N}\_{\theta}(\bm{\mu},x,\nu,\tau)=\big\langle\mathbf{b}(\bm{\mu}),\mathbf{t}(x,\nu,\tau)\big\rangle, |  | (9) |

where θ\theta denotes all trainable parameters of the branch and trunk nets.
Each scalar input component of (𝝀,x,ν,τ)(\boldsymbol{\lambda},x,\nu,\tau) is
linearly rescaled to lie in the interval [−1,1][-1,1] before being passed
to the network.
Both branch and trunk MLPs use 4 hidden layers with GELU activations and residual connections between layers, and the correction term σ​(⋅)\sigma(\cdot) is implemented as a Softplus.

![Refer to caption](x1.png)


Figure 1: The DeepSVM architecture. The model combines a DeepONet
core with a hard-constrained ansatz to enforce the terminal payoff
condition exactly. Training is stabilized via residual-based adaptive
refinement (RAR).

### III-B Hard-constrained ansatz

In general, vanilla PINNs struggle to exactly satisfy initial or terminal
conditions, leading to error propagation into the interior of the domain
[wang2021learning]. This issue is particularly pronounced in the
Heston stochastic volatility model, where the terminal payoff is not a
stationary solution of the PDE operator. We strictly enforce the terminal
payoff condition at τ=0\tau=0 by decomposing the solution into a fixed term
and a learned correction, following the classical ansatz of
[lagaris1998artificial]. Specifically, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | upred​(x,ν,τ;𝝁)=ϕ​(x)+τ​σ​(𝔑θ​(𝝁,x,ν,τ)),u\_{\text{pred}}(x,\nu,\tau;\bm{\mu})=\phi(x)+\tau\,\sigma\bigl(\mathfrak{N}\_{\theta}(\bm{\mu},x,\nu,\tau)\bigr), |  | (10) |

where ϕ​(x)=max⁡(ex−1,0)\phi(x)=\max(e^{x}-1,0) is the known terminal payoff defined in
§[II-B](https://arxiv.org/html/2512.07162v1#S2.SS2 "II-B Boundary and Terminal Conditions ‣ II Problem Formulation ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks"), and σ​(⋅)\sigma(\cdot) is
a smooth activation function (we use the Softplus nonlinearity).
The multiplicative factor τ\tau ensures that as τ→0\tau\to 0, the correction term vanishes and upred→ϕ​(x)u\_{\text{pred}}\to\phi(x) exactly. Furthermore, the use of the positive Softplus function for the correction term enforces the static no-arbitrage condition u​(x,ν,τ)≥ϕ​(x)u(x,\nu,\tau)\geq\phi(x), ensuring the option price never falls below its intrinsic value.

### III-C Loss function and training

Let 𝒩​[u]\mathcal{N}[u] denote the Heston differential operator defined in Eq. ([5](https://arxiv.org/html/2512.07162v1#S2.E5 "Equation 5 ‣ II-A Log-Moneyness Transformation ‣ II Problem Formulation ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks")). We train the network by minimizing the PDE residual over the domain, with the total loss:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ=ℒphys+λb​ℒbound+λa​ℒatm,\displaystyle\mathcal{L}=\mathcal{L}\_{\textrm{phys}}+\lambda\_{b}\mathcal{L}\_{\textrm{bound}}+\lambda\_{a}\mathcal{L}\_{\textrm{atm}}, |  | (11) |

The PDE residual is a modified penalty formulated to prioritize the highest residuals in the collocation set:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒphys=𝔼​[R2]+λmax​𝔼​[R4],\mathcal{L}\_{\textrm{phys}}=\mathbb{E}[R^{2}]+\lambda\_{\textrm{max}}\mathbb{E}[R^{4}], |  | (12) |

with λmax=0.1\lambda\_{\textrm{max}}=0.1 and the squared residual R2R^{2} defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R2=1N​∑i=1N|∂upred,i∂τ−𝒩​[upred,i]|2.R^{2}=\frac{1}{N}\sum\_{i=1}^{N}\left|\partialderivative{u\_{\textrm{pred},i}}{\tau}-\mathcal{N}[u\_{\textrm{pred},i}]\right|^{2}. |  | (13) |

The term ℒbound\mathcal{L}\_{\text{bound}} aggregates the boundary-condition errors at the spatial boundaries x=xminx=x\_{\min} and x=xmaxx=x\_{\max}, while ℒatm\mathcal{L}\_{\text{atm}} is the same residual loss restricted to a dedicated set of collocation points concentrated in the at-the-money (ATM) region x∈[−0.05,0.05]x\in[-0.05,0.05]. We set λb=1.0\lambda\_{b}=1.0 and λa=1.0\lambda\_{a}=1.0 in our experiments.

To combat the high gradients present near the ATM region, we employ Residual-based Adaptive Refinement (RAR) [lu2021deepxde, Wu\_2023]. During training, we periodically evaluate the PDE residual on a dense set of candidate points, identify those with the largest residuals, and add them to the active collocation set. This creates a feedback loop in which the model explicitly targets the most difficult regions of the state space.

We generate log-moneyness collocation points by warping a low-discrepancy Sobol sequence ux∈[0,1]u\_{x}\in[0,1] into the interval [xmin,xmax][x\_{\min},x\_{\max}] using a smooth tanh\tanh-based mapping that concentrates samples near the center of the domain. Define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xmid\displaystyle x\_{\mathrm{mid}} | =12​(xmin+xmax),\displaystyle=\frac{1}{2}\bigl(x\_{\min}+x\_{\max}\bigr), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | xhalf\displaystyle x\_{\mathrm{half}} | =12​(xmax−xmin),\displaystyle=\frac{1}{2}\bigl(x\_{\max}-x\_{\min}\bigr), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | zx\displaystyle z\_{x} | =2​ux−1∈[−1,1].\displaystyle=2u\_{x}-1\in[-1,1]. |  |

The transformed log-moneyness coordinate is then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x​(ux)=xmid+xhalf​tanh(αx​zx),x(u\_{x})=x\_{\mathrm{mid}}+x\_{\mathrm{half}}\,\tanh\bigl(\alpha\_{x}z\_{x}\bigr.), |  | (14) |

where αx>0\alpha\_{x}>0 controls the degree of clustering around xmidx\_{\mathrm{mid}}; we use αx=2\alpha\_{x}=2 in all experiments.

Training proceeds in two stages. First, we run 10,00010{,}000 iterations of the Adam optimizer with an initial learning rate of 10−410^{-4}, exponentially decaying the learning rate by a factor of 1/21/2 every 2,0002{,}000 steps. We perform a RAR update every 500500 optimizer steps. The total size of the collocation set is 200,000200{,}000 points to account for the high dimensionality of the problem. At each RAR step we draw 50,00050{,}000 candidate collocation points, evaluate their residuals, select the 20,00020{,}000 points with largest loss, and use them to replace randomly selected points in the active set. In addition, we maintain 4,0964{,}096 ATM collocation points and 2,0482{,}048 boundary-condition points, which remain fixed throughout the first training stage. In the second stage, we augment the boundary set with an additional 2,0482{,}048 points and refine the solution with L-BFGS (memory size 2020) for 5,0005{,}000 iterations, starting from the Adam solution and reusing the collocation sets from the initial phase.

## IV Results & Discussion

![Refer to caption](x2.png)


Figure 2: Convergence of the total loss during training. The shaded regions indicate the Adam and L–BFGS phases, respectively.

![Refer to caption](x3.png)


Figure 3: Top two rows: Comparison between DeepSVM and the semi-analytic Heston solution for three randomly selected parameter vectors 𝝁\boldsymbol{\mu}. For each column we show the option price (DeepSVM vs. semi-analytic) and the corresponding absolute pricing error as a function of log-moneyness x=ln⁡(S/K)x=\ln(S/K). Bottom row: For each parameter set, we show the corresponding Greeks (Delta and Gamma) computed via Autodiff from DeepSVM and from the semi-analytic model.

![Refer to caption](x4.png)


Figure 4: Spatial maps of the PDE residual mean-squared error (MSE) in (x,ν)(x,\nu) space. Top row: Residual MSE averaged over the parameter space 𝝁\boldsymbol{\mu} for different time-to-maturity slices τ\tau. Bottom row: Residual MSE averaged over τ\tau for three representative parameter vectors 𝝁\boldsymbol{\mu}. All panels share a common logarithmic color scale.

In Figure [2](https://arxiv.org/html/2512.07162v1#S4.F2 "Figure 2 ‣ IV Results & Discussion ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks") we show the training dynamics of DeepSVM. The Adam phase rapidly decreases the loss before plateauing, where we can observe the impact of the RAR steps every 500500 optimizer steps. Subsequently, the L-BFGS phase refines the solution and reduces the total loss to 𝒪​(10−5)\mathcal{O}(10^{-5}) within 5,0005{,}000 iterations. Empirically, we found that increasing the number of L-BFGS iterations beyond this point produces only marginal improvements in the objective function, indicating convergence for our current model, sampling scheme, and training routine.

Figure [3](https://arxiv.org/html/2512.07162v1#S4.F3 "Figure 3 ‣ IV Results & Discussion ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks") assesses the accuracy of DeepSVM against the numerical semi-analytic Heston solution. The top two rows display, for three randomly sampled parameter combinations 𝝁\boldsymbol{\mu}, the predicted call price as a function of log-moneyness xx together with the corresponding absolute price error on a logarithmic scale. Across all three chosen parameter sets, DeepSVM reproduces the price surface with high fidelity across the majority of the domain; the largest discrepancies occur in the narrow region near the ATM regime (x≈0x\approx 0). This confirms that the hard-constrained terminal ansatz employed in DeepSVM, combined with our modified loss and RAR scheme, can drive the pricing error down to a level that is essentially indistinguishable from market noise.

The bottom row of Figure [3](https://arxiv.org/html/2512.07162v1#S4.F3 "Figure 3 ‣ IV Results & Discussion ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks") highlights a critical observation regarding the derivatives of the learned operator. The Greeks, or sensitivities of the price with respect to state variables, exhibit noise that is not present in the semi-analytic benchmark. The two Greeks used for comparison are Delta (Δ\Delta) and Gamma (Γ\Gamma). Delta represents the sensitivity of the option price to the underlying asset spot price:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ≡∂V∂S=e−x​∂u∂x,\Delta\equiv\frac{\partial V}{\partial S}=e^{-x}\frac{\partial u}{\partial x}, |  | (15) |

and Gamma represents the curvature of the option value:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ≡∂2V∂S2=e−2​xK​[∂2u∂x2−∂u∂x].\Gamma\equiv\frac{\partial^{2}V}{\partial S^{2}}=\frac{e^{-2x}}{K}\left[\frac{\partial^{2}u}{\partial x^{2}}-\frac{\partial u}{\partial x}\right]. |  | (16) |

While the prices match the semi-analytic benchmark extremely well, the corresponding Greeks computed via automatic differentiation show deviations. Delta exhibits oscillations near the ATM region (x=0x=0), deviating from the smooth sigmoid-like profile of the semi-analytic solution. Consequently, Gamma—which involves a second derivative—amplifies these oscillations, leading to locally negative values in regions where convexity should be strictly positive.

Fundamentally, these artifacts arise because the neural network is constrained only by the PDE residual (which couples the value and derivatives) rather than by the derivatives directly. The optimizer finds a solution manifold that minimizes the PDE error but is not necessarily smooth in higher-order derivatives. We experimented with adding a soft constraint penalty to encourage positive values of Γ\Gamma at ATM collocation points, but this did not significantly improve the stability of the learned Greeks and degraded the overall pricing accuracy. This suggests that explicit Sobolev regularization (training on derivative norms) is a necessary direction for future research in financial operator learning.

To understand the structure of the PDE losses, Figure [4](https://arxiv.org/html/2512.07162v1#S4.F4 "Figure 4 ‣ IV Results & Discussion ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks") shows spatial maps of the residual mean squared error across (x,ν)(x,\nu) space. The top row shows residual maps averaged over uniformly sampled parameter draws 𝝁\boldsymbol{\mu}. We observe that the residual is negligible over the bulk of the domain, with the highest values persisting in localized pockets near the ATM region. The most problematic domain occurs at extremely small variances ATM, which corresponds to the region of maximum non-linearity in the payoff function. The bottom row of Figure [4](https://arxiv.org/html/2512.07162v1#S4.F4 "Figure 4 ‣ IV Results & Discussion ‣ DeepSVM: Learning Stochastic Volatility Models with Physics-Informed Deep Operator Networks") shows losses averaged over time for a single parameter set for three randomly selected choices of 𝝁\boldsymbol{\mu}. Here we again observe that while the residual is well-behaved globally, ridges of instability persist in the near-ATM regime where the Greeks are also distorted.

The loss analysis demonstrates that DeepSVM functions as an accurate surrogate model for the Heston PDE, achieving highly accurate residuals across large swathes of parameter space. However, standard physics-informed training, even with heavy sampling focused on the ATM regime, does not automatically guarantee smooth higher-order derivatives. This result highlights that while operator learning can solve the pricing problem (𝒪​(1)\mathcal{O}(1) inference), industrial applications requiring precise hedging parameters (Greeks) will likely require Sobolev-enhanced loss functions.

## V Conclusion

For European options in the classical Heston stochastic volatility model, semi-analytic Fourier-based pricing formulas are available and widely used in practice. From a pure pricing standpoint, these methods are typically more efficient than solving the associated pricing PDE.

However, our goal is not to improve on the classical Heston pricer itself, but to develop a general physics-informed operator learning framework (DeepSVM) that can be applied to stochastic volatility models and payoffs without closed-form or semi-analytic solutions. We therefore use the Heston model primarily as a benchmark setting with a trusted reference solution against which we can quantify the accuracy of our learned operator.

In this work, we have:

1. 1.

   Introduced the DeepSVM model, which accurately learns the pricing operator across the entirety of the parameter space corresponding to the Heston stochastic volatility model.
2. 2.

   Demonstrated that while pricing accuracy is high, the Greeks computed via automatic differentiation exhibit high-frequency noise when benchmarked against semi-analytic solutions, highlighting a specific regularization challenge in the at-the-money regime.

To address the discrepancies in the Greeks, future work should employ Sobolev training techniques [czarnecki2017sobolevtrainingneuralnetworks]. By differentiating the Heston PDE with respect to the state variables, we can obtain a system of coupled PDEs governing the sensitivities directly. Augmenting the loss function to minimize the residuals of these sensitivity equations would force the network to learn a solution manifold that is smooth in both value and derivative. Practically, these would be equations of the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂(∂xu)∂τ\displaystyle\partialderivative{(\partial\_{x}u)}{\tau} | =∂∂x⁡𝒩​[u],\displaystyle=\partialderivative{x}\mathcal{N}[u], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂(∂x​xu)∂τ\displaystyle\partialderivative{(\partial\_{xx}u)}{\tau} | =∂2∂x2⁡𝒩​[u].\displaystyle=\partialderivative[2]{x}\mathcal{N}[u]. |  |

While this technique would increase the size of the computational graph for each forward pass—since the ∂x𝒩​[u]\partial\_{x}\mathcal{N}[u] term contains third-order mixed derivatives—it represents the most theoretically sound path toward industrial-grade operator learning for finance.

Finally, while this work validates DeepSVM against the semi-analytic Heston benchmark, the true potential of this framework lies in generalized volatility regimes—such as Rough Volatility or high-dimensional Local Stochastic Volatility (LSV) models—where no closed-form solutions exist. In these computationally demanding environments, a pre-trained DeepSVM operator could replace expensive Monte Carlo simulations, offering a viable pathway for real-time exotic option pricing.