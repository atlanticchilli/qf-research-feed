---
authors:
- Anders G Frøseth
doc_id: arxiv:2603.09006v1
family_id: arxiv:2603.09006
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics'
url_abs: http://arxiv.org/abs/2603.09006v1
url_html: https://arxiv.org/html/2603.09006v1
venue: arXiv q-fin
version: 1
year: 2026
---


Anders G Frøseth
Independent Researcher.
E-mail: [indrefjorden@pm.me](2603.09006v1/mailto:indrefjorden@pm.me).

(8 March 2026)

###### Abstract

We develop spectral portfolio theory by establishing a direct identification: neural network weight matrices trained on stochastic processes are portfolio allocation matrices, and their spectral structure encodes factor decompositions and wealth concentration patterns.
The three forces governing stochastic gradient descent (SGD)—gradient signal, dimensional regularisation, and eigenvalue repulsion—translate directly into portfolio dynamics: smart money, survival constraint, and endogenous diversification.
The spectral properties of SGD weight matrices transition from Marchenko–Pastur statistics (additive regime, short horizon) to inverse-Wishart via the free log-normal (multiplicative regime, long horizon), mirroring the transition from daily returns to long-run wealth compounding.
We unify the cross-sectional wealth dynamics of Bouchaud and Mézard ([2000](#bib.bib2)), the within-portfolio dynamics of Olsen et al. ([2025](#bib.bib26)), and the scalar Fokker–Planck framework via a common spectral foundation.
A central result is the Spectral Invariance Theorem: any isotropic perturbation to the portfolio objective preserves the singular-value distribution up to scale and shift, while anisotropic perturbations produce spectral distortion proportional to their cross-asset variance.
We develop applications to portfolio design, wealth inequality measurement, tax policy, and neural network diagnostics.
In the tax context, the invariance result recovers and generalises the neutrality conditions of Frøseth ([2026b](#bib.bib9)).

## 1 Introduction

Consider a feedforward neural network trained to learn a stochastic process—a drift function, a transition density, or a score function—from observed trajectories.
At each layer, the weight matrix W∈ℝm×nW\in\mathbb{R}^{m\times n} evolves under stochastic gradient descent.

This paper takes the following identification as its foundation: the weight matrix at a given layer is a portfolio allocation matrix.
Row ii specifies how capital is distributed across nn assets in state ii, and columns index assets.
Training the network on data from a stochastic process is equivalent to running an adaptive portfolio optimizer on that process.

The spectral theory of SGD dynamics developed by Olsen et al. ([2025](#bib.bib26)) reveals that this identification is not merely an analogy: the stationary portfolio structure, the factor decomposition, and the concentration–diversification tradeoff emerge as direct mathematical consequences.
This paper develops the framework systematically, proving a spectral invariance theorem for isotropic perturbations and applying the results to portfolio design, wealth inequality, tax policy, and neural network diagnostics.

The main contributions are as follows.
First, we establish that the three forces in the singular-value evolution equation have direct portfolio interpretations: gradient signal encodes smart money (return-seeking), dimensional regularisation captures an endogenous survival constraint, and eigenvalue repulsion implements endogenous diversification without explicit constraints.
Second, we characterize the stationary spectral distribution as having a gamma-type bulk with power-law tail, giving rise to the core–satellite portfolio structure observed empirically in institutional wealth and household portfolio data.
Third, we show that the spectral transition from additive (Marchenko–Pastur) to multiplicative (inverse-Wishart) regimes is governed by the free log-normal distribution and the matrix Kesten problem, establishing a precise mathematical duality between short-horizon and long-horizon portfolio dynamics.
Fourth, we unify the cross-sectional wealth model of Bouchaud and Mézard, the within-portfolio model of Olsen et al., and the scalar Fokker–Planck framework via spectral decomposition.
Fifth, we prove the Spectral Invariance Theorem: any isotropic perturbation to the portfolio objective preserves the spectral shape of the allocation matrix, while anisotropic perturbations produce distortion proportional to their cross-asset variance.
Sixth, we develop applications to portfolio design, wealth inequality measurement, tax policy, and neural network diagnostics, demonstrating the breadth of the framework.

The paper is organized in five parts.
Part I (Sections [2](#S2 "2 Setup: Weight Matrices as Allocation Matrices ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")–[5](#S5 "5 Network Learning: Factor Complexity and Data Structure ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) establishes the foundations: the learning setup (Figure [1](#S2.F1 "Figure 1 ‣ 2 Setup: Weight Matrices as Allocation Matrices ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")), the weight matrix–portfolio identification, the SVD decomposition into eigenportfolios, the three forces of SGD, the stationary spectral distribution, and factor complexity.
Part II (Sections [6](#S6 "6 Timescale Regimes and Spectral Transitions ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")–[9](#S9 "9 The Fokker–Planck Connection ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) develops the dynamics: timescale regimes governing the additive-to-multiplicative transition, the ergodicity gap as a spectral observable, the aggregation from matrix to scalar via Itô projection, and the Fokker–Planck connection.
Part III (Sections [10](#S10 "10 The Bouchaud–Mézard Unification ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")–[14](#S14 "14 The Loss Function and Utility Correspondence ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) presents general results: the Bouchaud–Mézard unification, the Spectral Invariance Theorem and its anisotropic counterpart, the Spectral Invariance Conjecture, and the loss–utility correspondence.
Part IV (Section [15](#S15 "15 Applications ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) develops applications to portfolio design, wealth inequality, tax policy, and neural network diagnostics.
Part V (Sections [16](#S16 "16 Testable Predictions ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")–[19](#S19 "19 Conclusion ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) collects testable predictions, open questions, literature context, and conclusions.

## 2 Setup: Weight Matrices as Allocation Matrices

The starting point is a stochastic process observed through discrete trajectories.
The process follows a stochastic differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​x=v​(x)​d​t+2​D​d​B,dx=v(x)\,dt+\sqrt{2D}\,dB, |  | (1) |

where v​(x)v(x) is the drift function and DD the diffusion constant.
A neural network is trained to learn either the drift v​(x)v(x), the transition density p​(xt+Δ​t∣xt)p(x\_{t+\Delta t}\mid x\_{t}), or the score function ∇xlog⁡p​(x)\nabla\_{x}\log p(x) from observed trajectory data {x0,xΔ​t,x2​Δ​t,…}\{x\_{0},x\_{\Delta t},x\_{2\Delta t},\ldots\}.
The weight matrix WW at each layer is updated by stochastic gradient descent on a loss function ℒ​(W)\mathcal{L}(W) that is quadratic in the prediction residual (see Section [14](#S14 "14 The Loss Function and Utility Correspondence ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics") for details).

Data: trajectoriesttx​(t)x(t)d​x=v​(x)​d​t+2​D​d​Bdx=v(x)\,dt+\sqrt{2D}\,dB{xt,xt+Δ​t}\{x\_{t},x\_{t+\Delta t}\}Neural networkxtx\_{t}WWv^​(xt;W)\hat{v}(x\_{t};W)predictionLoss function


MLE:
1T​∑t‖Δ​xtΔ​t−v^‖2\displaystyle\frac{1}{T}\sum\_{t}\Bigl\|\frac{\Delta x\_{t}}{\Delta t}-\hat{v}\Bigr\|^{2}
Score matching:
12​‖sθ−∇log⁡p‖2\frac{1}{2}\|s\_{\theta}-\nabla\!\log p\|^{2}

both quadratic in residual
SGD: W←W−η​∇Wℒ+noise\;W\leftarrow W-\eta\,\nabla\_{W}\mathcal{L}+\text{noise}


Figure 1: The learning setup.
A stochastic process ([1](#S2.E1 "Equation 1 ‣ 2 Setup: Weight Matrices as Allocation Matrices ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) generates trajectory data (left).
A neural network with weight matrix WW at each layer learns the drift function v^​(x;W)\hat{v}(x;W) or the score function sθ​(x)s\_{\theta}(x) (centre).
The loss function is quadratic in the prediction residual (right), whether using maximum likelihood or score matching.
SGD updates WW iteratively, and the stationary spectral distribution of WW encodes the structure of the learned process.

In Olsen et al. ([2025](#bib.bib26)), the weight matrix W∈ℝm×nW\in\mathbb{R}^{m\times n} evolves under the stochastic differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​W=−η​∂ℒ∂W​d​t+2​η​D​d​𝒲,dW=-\eta\frac{\partial\mathcal{L}}{\partial W}\,dt+\sqrt{2\eta D}\,d\mathcal{W}, |  | (2) |

where η\eta is the learning rate, DD an effective diffusion constant, and d​𝒲d\mathcal{W} is matrix-valued Wiener noise.

We relabel the dimensions: set m=Tm=T (time periods or states of the world) and n=Nn=N (number of assets).
Then Wt​iW\_{ti} represents the portfolio weight on asset ii in state tt.
The allocation matrix W∈ℝT×NW\in\mathbb{R}^{T\times N} evolves as investors rebalance in response to return signals, information noise, and constraints implicit in the learning dynamics.

The singular value decomposition W=U​Σ​V⊤W=U\Sigma V^{\top} decomposes this allocation into principal components.
The left singular vectors uk∈ℝTu\_{k}\in\mathbb{R}^{T} show when each factor is relevant (temporal patterns).
The right singular vectors vk∈ℝNv\_{k}\in\mathbb{R}^{N} show which assets compose each factor (eigenportfolios).
The singular values σk\sigma\_{k} measure the magnitude of allocation to each eigenportfolio.

This decomposition reveals the factor structure naturally: large singular values correspond to important factors (market-wide moves, systematic risks); small singular values correspond to idiosyncratic or second-order effects.
The right singular vectors vkv\_{k} define eigenportfolio compositions, and the left singular vectors uku\_{k} indicate when each factor dominates.
Figure [2](#S2.F2 "Figure 2 ‣ 2 Setup: Weight Matrices as Allocation Matrices ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics") illustrates this relabelling.

Neural Network Layerxt∈ℝmx\_{t}\in\mathbb{R}^{m}W∈ℝm×nW\in\mathbb{R}^{m\times n}weight matrixyt=W⊤​xty\_{t}=W^{\top}\!x\_{t}≡\equivPortfolio Allocationt=1t{=}1t=2t{=}2t=Tt{=}TstatesWt​iW\_{ti}allocation matrixi=1i{=}1i=2i{=}2i=3i{=}3i=Ni{=}NassetsSVD: W=U​Σ​V⊤W=U\Sigma V^{\top}UUΣ\SigmaV⊤V^{\top}


uk∈ℝTu\_{k}\in\mathbb{R}^{T}
temporal
patterns

σk\sigma\_{k}
factor
magnitudes

vk∈ℝNv\_{k}\in\mathbb{R}^{N}
eigenportfolio
compositions

SGD dynamics:
d​W=−η​∇ℒ​d​t+2​η​D​d​𝒲dW=-\eta\nabla\mathcal{L}\,dt+\sqrt{2\eta D}\,d\mathcal{W}
≡\equiv adaptive portfolio
rebalancing
spectra


Figure 2: The neural network–portfolio identification.
A single layer with weight matrix W∈ℝm×nW\in\mathbb{R}^{m\times n} maps input xtx\_{t} to output yt=W⊤​xty\_{t}=W^{\top}x\_{t} (top left).
Relabelling rows as states and columns as assets gives the allocation matrix Wt​iW\_{ti} (bottom left).
The SVD decomposes WW into temporal patterns uku\_{k}, factor magnitudes σk\sigma\_{k}, and eigenportfolio compositions vkv\_{k} (top right).
SGD dynamics on WW are equivalent to adaptive portfolio rebalancing (bottom right); the stationary spectral density of σk\sigma\_{k} is determined by the signal-to-noise ratio β1/η​D\beta\_{1}/\eta D.

## 3 Portfolio Dynamics: The Three Forces of SGD

By Olsen et al. ([2025](#bib.bib26)) (Theorem 3.1), the singular values evolve as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​σk=[−η​uk⊤​(∇Wℒ)​vk+η​D​(m−n+12​σk−∑j≠kσkσk2−σj2)]​d​t+2​η​D​d​βk.d\sigma\_{k}=\Bigl[-\eta\,u\_{k}^{\top}(\nabla\_{W}\mathcal{L})\,v\_{k}+\eta D\Bigl(\frac{m-n+1}{2\sigma\_{k}}-\sum\_{j\neq k}\frac{\sigma\_{k}}{\sigma\_{k}^{2}-\sigma\_{j}^{2}}\Bigr)\Bigr]dt+\sqrt{2\eta D}\,d\beta\_{k}. |  | (3) |

This equation contains three distinct forces, each with a clear portfolio interpretation.

### 3.1 Gradient Signal: Smart Money

The term

|  |  |  |  |
| --- | --- | --- | --- |
|  | −η​uk⊤​(∇Wℒ)​vk-\eta\,u\_{k}^{\top}(\nabla\_{W}\mathcal{L})\,v\_{k} |  | (4) |

is the projected return signal pushing capital toward high-performing eigenportfolios.
This is the optimizer’s best estimate of where marginal utility of wealth is highest.
In a mean–variance framework with loss ℒ=−W​r+γ2​W2\mathcal{L}=-Wr+\tfrac{\gamma}{2}W^{2}, this term becomes the excess return on factor kk adjusted for risk aversion.
The negative sign reflects gradient descent: the optimizer increases weights on factors with positive marginal returns.

This force implements smart money dynamics: capital flows toward factors with superior risk-adjusted returns.

### 3.2 Dimensional Regularization: Survival Constraint

The term

|  |  |  |  |
| --- | --- | --- | --- |
|  | η​D​m−n+12​σk\eta D\,\frac{m-n+1}{2\sigma\_{k}} |  | (5) |

is a 1/σk1/\sigma\_{k} restoring force that prevents any eigenportfolio loading from reaching zero.
Small positions get pushed up.
Economically, this is a minimum-position constraint arising *endogenously* from the noise structure.
An investor observing returns with noise cannot rationally set any factor exposure exactly to zero, because zero exposure means zero information—creating an explore–exploit tension.

The prefactor m−n+1m-n+1 is the aspect ratio of the allocation matrix, encoding how many degrees of freedom remain after fitting the primary factors.
More time periods (larger mm) strengthen the survival constraint; more assets (larger nn) weaken it.

This force implements endogenous survival: positions that would shrink to zero due to poor current performance are sustained by information and exploration incentives.

### 3.3 Eigenvalue Repulsion: Endogenous Diversification

The term

|  |  |  |  |
| --- | --- | --- | --- |
|  | η​D​∑j≠kσkσk2−σj2\eta D\sum\_{j\neq k}\frac{\sigma\_{k}}{\sigma\_{k}^{2}-\sigma\_{j}^{2}} |  | (6) |

prevents any two eigenportfolio loadings from becoming equal.
In portfolio language, this is endogenous diversification.
Even without an explicit diversification constraint, stochastic rebalancing naturally separates factor exposures.
When two factors carry similar weight (σk≈σj\sigma\_{k}\approx\sigma\_{j}), the denominator diverges, creating an unstable repulsion that forces differentiation.

This is a new micro-foundation for diversification: it arises not from risk aversion (which is in the gradient term), but from the *noise structure of learning under partial information*.
It holds regardless of the loss function or risk aversion parameter.

###### Remark (Connection to Merton).

In the continuous-time portfolio problem, the optimal allocation involves the inverse covariance matrix Σ−1\Sigma^{-1} (Merton, [1969](#bib.bib24), [1971](#bib.bib25)).
The eigenvalue repulsion ensures that the estimated covariance matrix remains well-conditioned—it is a regularisation of the Merton solution that emerges from the learning dynamics.

| This paper | Nearest existing concept | Key distinction |
| --- | --- | --- |
| Smart money (gradient signal) | Informed investor flows (Gruber, [1996](#bib.bib12)) | Optimisation on available data, not asymmetric information; compatible with market efficiency |
| Survival constraint (dim. regularisation) | Safety-first / Kelly criterion (Roy, [1952](#bib.bib31)) | Survival of information channels (factor exposures), not of the investor |
| Endogenous diversification (eigenvalue repulsion) | Mean–variance diversification (Markowitz, [1952](#bib.bib22)) | Emerges from noise structure of learning; independent of risk aversion |

Table 1: Terminology disambiguation. The portfolio labels proposed in this paper echo but differ from established usage. Each force in the singular-value SDE ([3](#S3.E3 "Equation 3 ‣ 3 Portfolio Dynamics: The Three Forces of SGD ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) has a nearest classical counterpart; the distinctions are summarised here.

###### Remark (Adaptive dynamics).

Taken together, the three forces describe an explore–exploit–diversify triad: the gradient signal exploits current information, the survival constraint maintains exploratory positions, and eigenvalue repulsion enforces differentiation.
This is reminiscent of the Adaptive Markets Hypothesis (Lo, [2004](#bib.bib20), [2017](#bib.bib21)), in which market behaviour is driven by evolutionary dynamics among strategies.
The spectral framework can be viewed as providing a mathematical instantiation of Lo’s qualitative programme.

## 4 The Stationary Portfolio: Bulk and Tail

By Olsen et al. ([2025](#bib.bib26)) (Theorem 3.2), the stationary distribution of singular values is

|  |  |  |  |
| --- | --- | --- | --- |
|  | pσ​(σ)∝σm−n+1​e−(β1/4​η​D)​σ2,p\_{\sigma}(\sigma)\propto\sigma^{m-n+1}\,e^{-(\beta\_{1}/4\eta D)\,\sigma^{2}}, |  | (7) |

where β1\beta\_{1} is a mean-field restoring-force constant.

This distribution exhibits a clear structure: a concentrated bulk followed by a power-law tail.

###### Definition 1 (Core–Satellite Portfolio).

At stationarity, we partition the eigenportfolios into two groups:

* •

  Bulk: most eigenportfolio loadings cluster in a concentrated region.
  This is the diversified core—broad market exposure spread across many factors.
* •

  Tail: a few large σk\sigma\_{k} values form a power-law tail (σm−n+1\sigma^{m-n+1} for large σ\sigma).
  These are concentrated satellite positions—large bets on specific factors.

This core–satellite structure is observed empirically in institutional portfolios and, crucially, in the Norwegian wealth register data of Frøseth ([2026b](#bib.bib9), [a](#bib.bib8), [c](#bib.bib10)).

The tail exponent m−n+1m-n+1 depends on the aspect ratio of the allocation matrix.
For a market with NN assets observed over TT periods, the exponent is T−N+1T-N+1.
More observation (larger TT) fattens the tail (allows more concentration); more assets (larger NN) thins it (forces diversification).
This is testable against Norwegian portfolio data.

###### Definition 2 (Effective Spectral Rank).

Define the *effective spectral rank* as

|  |  |  |  |
| --- | --- | --- | --- |
|  | reff=∑kσkmaxk⁡σk,r\_{\text{eff}}=\frac{\sum\_{k}\sigma\_{k}}{\max\_{k}\sigma\_{k}}, |  | (8) |

the ratio of total allocation to the largest single factor exposure.
This measures the complexity of the portfolio: reff=1r\_{\text{eff}}=1 means one factor dominates; reff=Nr\_{\text{eff}}=N means all factors have equal weight.
The stationary distribution predicts a specific value of reffr\_{\text{eff}} as a function of the aspect ratio and the signal-to-noise ratio.

## 5 Network Learning: Factor Complexity and Data Structure

When a weight matrix WW is trained on data from a stochastic process, it encodes a factor decomposition of that process.
The singular values tell us the relative importance of each factor.

Consider three cases:

Case 1: Simple underlying structure.
If the data is generated by a drift function with simple structure (mean-reverting, polynomial, Fourier basis), the trained weight matrix will have a small number of large singular values followed by a sharp drop.
The bulk is thin, the tail is fat—a concentrated factor model.

Case 2: Complex or noisy data.
If the data is noisy or has complex structure, the trained matrix will have a more gradual decay of singular values.
The bulk is thick, the tail is thinner—a more diversified representation.

Case 3: Pareto-distributed data.
The spectral complexity measure reffr\_{\text{eff}} directly reflects the intrinsic dimensionality of the process.
For Pareto-distributed data (as in wealth), the exponent of reffr\_{\text{eff}} should match the Pareto exponent of the data.

This means the weight spectrum is not an artifact of the learning process; it is a faithful encoding of the underlying data structure.
In deep networks with LL layers, each layer performs a hierarchical factor decomposition: early layers capture primary factors, intermediate layers combine them into secondary factors, and the final layer produces the output.
This is the fund-of-funds structure: not a single portfolio, but a hierarchy of portfolios.

## 6 Timescale Regimes and Spectral Transitions

The spectral portfolio framework must reconcile two well-established facts about asset dynamics that operate on different timescales.

### 6.1 The Additive Regime: Short Horizon

At timescales from minutes to days, asset returns are approximately additive: rt≈μ​δ​t+σ​δ​Btr\_{t}\approx\mu\,\delta t+\sigma\,\delta B\_{t}, with heavy tails but finite variance over short windows.
This is the regime of the classical stylized facts (Cont, [2001](#bib.bib5); Bouchaud and Potters, [2003](#bib.bib3)): fat-tailed return distributions, volatility clustering, and approximately uncorrelated returns.
The covariance matrix Σ=Cov​(rt)\Sigma=\mathrm{Cov}(r\_{t}) has a Marchenko–Pastur bulk with a few spikes (market factor, sector factors), and random matrix theory cleaning (Laloux et al., [1999](#bib.bib18); Ledoit and Wolf, [2004](#bib.bib19)) is effective precisely because the bulk is well described by random matrix universality.

This is also the regime where Olsen et al. ([2025](#bib.bib26))’s spectral theory of SGD applies most directly: weight updates are small additive perturbations, the matrix-valued SDE is well approximated by Dyson Brownian motion, and the stationary spectral density follows a gamma-type distribution with power-law tails.

### 6.2 The Multiplicative Regime: Long Horizon

At timescales from months to years, compounding dominates.
Wealth dynamics are inherently multiplicative: d​W/W=μ​d​t+σ​d​Bt\mathrm{d}W/W=\mu\,\mathrm{d}t+\sigma\,\mathrm{d}B\_{t}, and the natural coordinate is log-wealth x=ln⁡Wx=\ln W, which converts multiplicative dynamics into an additive SDE with drift v=μ−12​σ2v=\mu-\tfrac{1}{2}\sigma^{2} and diffusion D=σ2D=\sigma^{2}.
This is the regime of Frøseth ([2026c](#bib.bib10)), where the Fokker–Planck equation governs the wealth distribution and the Pareto tail emerges from drift–diffusion balance.

Tax effects and portfolio allocation decisions operate on this longer timescale.
The Heston model (Heston, [1993](#bib.bib15)) and other stochastic-volatility extensions capture both regimes: they remain multiplicative while capturing the volatility clustering persisting from the short-horizon regime.

### 6.3 The qq-Transformation: Quantifying the Crossover

Bouchaud and Potters ([2003](#bib.bib3)) introduce a continuous parametrisation of the additive-to-multiplicative crossover.
Define the price process

|  |  |  |  |
| --- | --- | --- | --- |
|  | x​(T)=x0​(1+q​(T)​ξ​(T))1/q​(T),q​(T)∈[0,1],x(T)=x\_{0}\bigl(1+q(T)\,\xi(T)\bigr)^{1/q(T)},\qquad q(T)\in[0,1], |  | (9) |

where ξ​(T)\xi(T) is the fundamental random variable (normalised return).
At q=1q=1 the process is fully additive: x=x0​(1+ξ)x=x\_{0}(1+\xi).
As q→0q\to 0, one recovers the multiplicative limit: (1+q​ξ)1/q→eξ(1+q\xi)^{1/q}\to e^{\xi}, so x=x0​eξx=x\_{0}\,e^{\xi}.

The index q​(T)q(T) is a quantitative measure of the additivity of the process at horizon TT.
Empirically, qq decreases monotonically from near 1 at intraday timescales to near 0 at horizons of months to years.
The crossover timescale TcT\_{c} at which q≈1/2q\approx 1/2 is on the order of *months* for liquid equity markets.

The qq-transformation also governs the skewness:

|  |  |  |  |
| --- | --- | --- | --- |
|  | s​(T)=−3​q​(T)​σ​(T),s(T)=-3\,q(T)\,\sigma(T), |  | (10) |

so that skewness vanishes in the multiplicative limit (q→0q\to 0) and is largest in the additive regime.
This provides a measurable diagnostic: the observed skewness at a given horizon identifies where the process sits in the crossover.

For the spectral portfolio framework, q​(T)q(T) determines which universality class governs the covariance spectrum at a given horizon.
When q≈1q\approx 1 (additive, short horizon), the spectrum is Marchenko–Pastur with isolated signal spikes.
When q≈0q\approx 0 (multiplicative, long horizon), the spectrum transitions toward the free log-normal/inverse-Wishart regime described next.

### 6.4 The Transition: Marchenko–Pastur to Inverse-Wishart

The passage from additive to multiplicative regime reflects not merely a change of resolution but a change in the dominant mechanism and, crucially, a change in the spectral universality class.

Potters and Bouchaud ([2021](#bib.bib30)) develop this transition explicitly in free probability language.
The additive central limit theorem for free random matrices gives the Wigner semicircle (Marchenko–Pastur for rectangular matrices).
The *multiplicative* central limit theorem gives the *free log-normal*, with S-transform

|  |  |  |  |
| --- | --- | --- | --- |
|  | SLN​(t)=e−a/2−b​t,S\_{\mathrm{LN}}(t)=\mathrm{e}^{-a/2-bt}, |  | (11) |

where aa controls the mean log-eigenvalue and bb the variance.
The free log-normal is stable under free products, as the semicircle is stable under free sums.
For small aa, the density is indistinguishable from a Wigner semicircle; as aa grows, it develops the characteristic asymmetric shape of multiplicative dynamics.

Multiplicative Dyson Brownian Motion.
The additive DBM governing eigenvalue dynamics in the short-horizon regime has a multiplicative counterpart (Potters and Bouchaud, [2021](#bib.bib30)):

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​λid​t=a2​λi+bN​∑j≠iλi​λjλi−λj+bN​λi​ξi,\frac{\mathrm{d}\lambda\_{i}}{\mathrm{d}t}=\frac{a}{2}\,\lambda\_{i}+\frac{b}{N}\sum\_{j\neq i}\frac{\lambda\_{i}\lambda\_{j}}{\lambda\_{i}-\lambda\_{j}}+\sqrt{\frac{b}{N}}\,\lambda\_{i}\,\xi\_{i}, |  | (12) |

where ξi\xi\_{i} are independent Langevin noise terms.
Every term is proportional to λi\lambda\_{i}: the drift, the repulsion, and the noise are all multiplicative.
At arbitrary time tt, the spectral density is the free log-normal with parameters t​ata and t​btb.

Matrix Kesten Problem.
The scalar Kesten recursion Zn+1=Zn​(1+ζn)Z\_{n+1}=Z\_{n}(1+\zeta\_{n}), which generates Pareto tails in Bouchaud and Mézard ([2000](#bib.bib2)); Frøseth ([2026c](#bib.bib10)), has a matrix generalization.
The corresponding Fokker–Planck equation is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂P∂t=−∂∂U​[(1+m​U)​P]+σ22​∂2∂U2​[U2​P],\frac{\partial P}{\partial t}=-\frac{\partial}{\partial U}\bigl[(1+mU)P\bigr]+\frac{\sigma^{2}}{2}\frac{\partial^{2}}{\partial U^{2}}\bigl[U^{2}P\bigr], |  | (13) |

with stationary distribution Peq​(U)∝U−1−μ​e−2/(σ2​U)P\_{\mathrm{eq}}(U)\propto U^{-1-\mu}\,\mathrm{e}^{-2/(\sigma^{2}U)}, an inverse-gamma with power-law tail exponent

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ=1+2​m^σ2.\mu=1+\frac{2\hat{m}}{\sigma^{2}}. |  | (14) |

The matrix Kesten variable is an inverse-Wishart matrix, whose eigenvalue spectrum maps to Marchenko–Pastur under λ→1/λ\lambda\to 1/\lambda.
This establishes a precise duality: the additive regime is Marchenko–Pastur; the multiplicative regime is inverse-Wishart; the two are related by spectral inversion.

###### Remark (Interpolating Family).

The free log-normal provides a one-parameter family interpolating continuously between additive and multiplicative regimes.
At small aa (short horizon), the density resembles the Marchenko–Pastur semicircle.
At large aa (long horizon), the density develops a power-law tail controlled by μ=1+2​m^/σ2\mu=1+2\hat{m}/\sigma^{2}.
The parameter aa plays the role of effective horizon, growing with the number of compounding periods.

For the spectral portfolio framework:

1. 1.

   The *within-layer* spectral structure of SGD weight matrices reflects the additive regime.
   The network is trained on short-horizon data increments; the relevant universality class is Marchenko–Pastur; the relevant dynamics are additive DBM.
2. 2.

   The *cross-sectional* spectral structure of the population allocation matrix reflects the multiplicative regime.
   Agents compound returns over long horizons; the relevant universality class is the free log-normal/inverse-Wishart; the dynamics are multiplicative DBM.
3. 3.

   The aggregation from matrix to scalar (Section [8](#S8 "8 Aggregation: From Matrix to Scalar via Itô’s Lemma ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) is the radial projection from matrix Fokker–Planck to scalar Fokker–Planck, mapping the spectral exponent μ\mu of inverse-Wishart to the Pareto exponent α=1+v/D\alpha=1+v/D of the wealth distribution.
4. 4.

   The scalar Kesten process of Frøseth ([2026c](#bib.bib10)) and the matrix Kesten problem are related by this same projection.
   The Pareto tail of the wealth distribution is the radial shadow of the inverse-Wishart tail of the allocation matrix.

Regime shifts manifest spectrally as changes in the effective parameter aa of the free log-normal, from small aa (Marchenko–Pastur bulk with isolated spikes) to large aa (inverse-Wishart density with power-law tails).
Market crashes or policy reforms can trigger cross-sectional regime shifts: assets in the additive regime may suddenly transition to multiplicative dynamics (fire sales, forced liquidation).

## 7 The Ergodicity Gap as Spectral Observable

A central insight from Peters ([2019](#bib.bib28)) and Frøseth ([2026c](#bib.bib10)) is the distinction between *ensemble average* and *time average*.
The wealth distribution π​(x)\pi(x) represents the ensemble (cross-section at a fixed time).
An individual trajectory x​(t)x(t) represents time evolution of a single agent.

In ergodic systems, the two averages coincide: an agent’s long-run average outcome equals the population average.
In non-ergodic systems, they differ: the population distribution can have fat tails while individual trajectories concentrate.

###### Definition 3 (Ergodicity Gap).

For a wealth process x​(t)x(t) with drift vv and diffusion DD, define the *ergodicity gap* as the difference between the ensemble and time-average growth rates:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​g=gens−gtime=(v+12​D)−(v−12​D)=D.\Delta g\;=\;g\_{\text{ens}}-g\_{\text{time}}\;=\;\bigl(v+\tfrac{1}{2}D\bigr)-\bigl(v-\tfrac{1}{2}D\bigr)\;=\;D. |  | (15) |

Here gens=dd​t​log⁡𝔼​[x]g\_{\text{ens}}=\frac{d}{dt}\log\mathbb{E}[x] is the growth rate of the ensemble mean and gtime=𝔼​[dd​t​log⁡x]g\_{\text{time}}=\mathbb{E}[\frac{d}{dt}\log x] is the expected time-average (geometric) growth rate.

In the scalar model of Frøseth ([2026c](#bib.bib10)), the ergodicity gap is simply the diffusion coefficient DD.
In the spectral framework, the Itô projection of Section [8](#S8 "8 Aggregation: From Matrix to Scalar via Itô’s Lemma ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics") yields an effective scalar diffusion

|  |  |  |  |
| --- | --- | --- | --- |
|  | Deff=2​η​D,D\_{\text{eff}}=2\eta D, |  | (16) |

where η\eta is the learning rate and DD the data covariance scale.
The radial projection collapses all m​nmn noise directions onto one: each matrix entry contributes independently to ‖W‖F2\|W\|\_{F}^{2}, but the quadratic variation of x=‖W‖Fx=\|W\|\_{F} is (1/x2)​∑Wa​i2⋅2​η​D=2​η​D(1/x^{2})\sum W\_{ai}^{2}\cdot 2\eta D=2\eta D.
The ergodicity gap thus has a spectral interpretation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​g=Deff=2​η​D.\Delta g=D\_{\text{eff}}=2\eta D. |  | (17) |

The gap depends on the noise level but not on matrix dimensions.
However, the *effect* of the gap on the wealth distribution depends on the spectral structure: when the spectral tail is fat (small tail exponent), fewer factors carry most of the variance, individual trajectories are more volatile relative to their mean, and the distributional consequences of non-ergodicity are more severe.
When the spectrum is flat (many comparable factors), the volatility is spread across dimensions and individual trajectories track the ensemble more closely.

An isotropic perturbation (Theorem [1](#Thmtheorem1 "Theorem 1 (Spectral Invariance). ‣ 11.2 Spectral Consequences ‣ 11 Isotropic Perturbations and Spectral Invariance ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) preserves the spectral shape, hence preserves DeffD\_{\text{eff}} and leaves the ergodicity gap unchanged.
An anisotropic perturbation that compresses the spectral tail (e.g. differential taxation favouring diversified portfolios) reduces the effective number of dominant factors, lowers DeffD\_{\text{eff}}, and narrows the gap.

## 8 Aggregation: From Matrix to Scalar via Itô’s Lemma

Define total portfolio value as x=‖W‖F=(∑a,iWa​i2)1/2x=\|W\|\_{F}=\bigl(\sum\_{a,i}W\_{ai}^{2}\bigr)^{1/2}.
By Itô’s lemma applied to f​(W)=‖W‖Ff(W)=\|W\|\_{F}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​x=1x​∑a,iWa​i​d​Wa​i+12​x​(m​n⋅2​η​D−1x2​∑a,iWa​i2⋅2​η​D)​d​t.dx=\frac{1}{x}\sum\_{a,i}W\_{ai}\,dW\_{ai}+\frac{1}{2x}\Bigl(mn\cdot 2\eta D-\frac{1}{x^{2}}\sum\_{a,i}W\_{ai}^{2}\cdot 2\eta D\Bigr)dt. |  | (18) |

The first term gives the drift contribution from the gradient signal projected onto the radial direction.
The second term simplifies using ∑Wa​i2=x2\sum W\_{ai}^{2}=x^{2}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​x=1x​tr⁡(W⊤​d​W)+η​D​(m​n−1)x​d​t.dx=\frac{1}{x}\operatorname{tr}(W^{\top}dW)+\frac{\eta D(mn-1)}{x}\,dt. |  | (19) |

In SVD coordinates, tr⁡(W⊤​d​W)=∑kσk​d​σk\operatorname{tr}(W^{\top}dW)=\sum\_{k}\sigma\_{k}\,d\sigma\_{k} plus rotational terms.
If the rotational terms average out (which they do under isotropic noise), the radial process becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​xx=μrad​d​t+σrad​d​B,\frac{dx}{x}=\mu\_{\text{rad}}\,dt+\sigma\_{\text{rad}}\,dB, |  | (20) |

a geometric Brownian motion.
This is exactly the scalar SDE of Frøseth ([2026c](#bib.bib10)).
The wealth Fokker–Planck is the radial projection of the matrix Fokker–Planck.

The radial drift and diffusion are computed by substituting the multiplicative Dyson BM ([12](#S6.E12 "Equation 12 ‣ 6.4 The Transition: Marchenko–Pastur to Inverse-Wishart ‣ 6 Timescale Regimes and Spectral Transitions ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) into ([19](#S8.E19 "Equation 19 ‣ 8 Aggregation: From Matrix to Scalar via Itô’s Lemma ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")).
Let p=min⁡(m,n)p=\min(m,n) be the number of singular values and write x2=∑k=1pσk2x^{2}=\sum\_{k=1}^{p}\sigma\_{k}^{2}.
The signal term contributes a radial drift from the restoring force in ([7](#S4.E7 "Equation 7 ‣ 4 The Stationary Portfolio: Bulk and Tail ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")), and the Itô correction from ([18](#S8.E18 "Equation 18 ‣ 8 Aggregation: From Matrix to Scalar via Itô’s Lemma ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) contributes η​D​(m​n−1)/x\eta D(mn-1)/x.
The noise has quadratic variation (1/x2)​∑a,i‖Wa​i‖2⋅2​η​D=2​η​D(1/x^{2})\sum\_{a,i}\|W\_{ai}\|^{2}\cdot 2\eta D=2\eta D, giving an effective scalar diffusion Deff=2​η​DD\_{\text{eff}}=2\eta D independent of matrix dimensions (the radial projection collapses all m​nmn noise directions onto one).
The Pareto exponent is

|  |  |  |  |
| --- | --- | --- | --- |
|  | α=1+vradialDeff,\alpha=1+\frac{v\_{\text{radial}}}{D\_{\text{eff}}}, |  | (21) |

where vradialv\_{\text{radial}} depends on mm, nn, and β1/η​D\beta\_{1}/\eta D.

The function ff can be evaluated explicitly in two regimes.

Single-factor limit (p=1p=1, i.e. n=1n=1).
The allocation matrix reduces to a vector, eigenvalue repulsion vanishes, and the spectral SDE collapses to a scalar Ornstein–Uhlenbeck process for σ2\sigma^{2}.
The radial SDE ([20](#S8.E20 "Equation 20 ‣ 8 Aggregation: From Matrix to Scalar via Itô’s Lemma ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) becomes

|  |  |  |
| --- | --- | --- |
|  | d​x=(−β12​x+η​D​(m−1)x)​d​t+2​η​D​d​B.dx=\Bigl(-\frac{\beta\_{1}}{2}x+\frac{\eta D(m-1)}{x}\Bigr)dt+\sqrt{2\eta D}\,dB. |  |

At stationarity, the process for y=x2y=x^{2} has drift vy=−β1​y+2​η​D⋅mv\_{y}=-\beta\_{1}y+2\eta D\cdot m and diffusion 4​η​D⋅y4\eta D\cdot y.
The stationary density is P​(y)∝y−1−μ​e−const/yP(y)\propto y^{-1-\mu}e^{-\text{const}/y} with

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ|p=1=1+(m−1)​β12​η​D,\mu\big|\_{p=1}=1+\frac{(m-1)\beta\_{1}}{2\eta D}, |  | (22) |

which is exactly the scalar Kesten exponent ([14](#S6.E14 "Equation 14 ‣ 6.4 The Transition: Marchenko–Pastur to Inverse-Wishart ‣ 6 Timescale Regimes and Spectral Transitions ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) with m^=(m−1)​β1/2\hat{m}=(m-1)\beta\_{1}/2 and σ2=2​η​D\sigma^{2}=2\eta D.
The corresponding wealth Pareto exponent is α=μ/2\alpha=\mu/2 (since wealth scales as xx, not x2x^{2}).

Large-NN regime (m,n≫1m,n\gg 1, m/n=γm/n=\gamma fixed).
The eigenvalue repulsion is of order p2p^{2} but the repulsion terms cancel in the radial projection (they redistribute variance among singular values without changing ∑σk2\sum\sigma\_{k}^{2}).
The radial drift at stationarity is vradial=−β1​x/2+η​D​(m​n−1)/xv\_{\text{radial}}=-\beta\_{1}x/2+\eta D(mn-1)/x.
Setting vradial=0v\_{\text{radial}}=0 at the stationary mean x¯2=2​η​D​(m​n−1)/β1\bar{x}^{2}=2\eta D(mn-1)/\beta\_{1} and linearising, the Pareto exponent becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | α≈ 1+(m​n−1)​β12​m​n​η​D≈ 1+β12​η​D,m,n≫1.\alpha\;\approx\;1+\frac{(mn-1)\beta\_{1}}{2mn\,\eta D}\;\approx\;1+\frac{\beta\_{1}}{2\eta D},\qquad m,n\gg 1. |  | (23) |

In the large-NN limit the Pareto exponent depends on the signal-to-noise ratio β1/(2​η​D)\beta\_{1}/(2\eta D) alone, independent of matrix dimensions.
This is the spectral counterpart of the Kesten result: strong signal (large β1\beta\_{1}) produces a thin tail (large α\alpha), while strong noise (large η​D\eta D) produces a fat tail (small α\alpha).

For general (m,n)(m,n), the function ff interpolates between the single-factor formula ([22](#S8.E22 "Equation 22 ‣ 8 Aggregation: From Matrix to Scalar via Itô’s Lemma ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) and the large-NN limit ([23](#S8.E23 "Equation 23 ‣ 8 Aggregation: From Matrix to Scalar via Itô’s Lemma ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")), and can be computed by numerical integration of the radial projection against the spectral density ([7](#S4.E7 "Equation 7 ‣ 4 The Stationary Portfolio: Bulk and Tail ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")).

## 9 The Fokker–Planck Connection

Both the wealth distribution and the spectral density satisfy Fokker–Planck equations, revealing a deep structural parallel.

Wealth distribution (Frøseth, [2026c](#bib.bib10)):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂π∂t=−∂∂x​[v​(x)​π]+D​∂2π∂x2.\frac{\partial\pi}{\partial t}=-\frac{\partial}{\partial x}\bigl[v(x)\,\pi\bigr]+D\,\frac{\partial^{2}\pi}{\partial x^{2}}. |  | (24) |

The stationary solution has Pareto tail with exponent α=1+v/D\alpha=1+v/D.

Spectral density:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂ρ∂λ=∂∂λ​[(c​(λ∗−λ)−PV​∫ρ​(λ′)λ−λ′​𝑑λ′)​ρ]+Deff​∂2ρ∂λ2.\frac{\partial\rho}{\partial\lambda}=\frac{\partial}{\partial\lambda}\Bigl[\bigl(c(\lambda^{\*}-\lambda)-\mathrm{PV}\!\int\frac{\rho(\lambda^{\prime})}{\lambda-\lambda^{\prime}}\,d\lambda^{\prime}\bigr)\rho\Bigr]+D\_{\text{eff}}\,\frac{\partial^{2}\rho}{\partial\lambda^{2}}. |  | (25) |

The stationary solution has gamma-type density with power-law tail exponent m−n+1m-n+1.

The spectral equation has an extra nonlocal interaction term (the principal-value integral—the mean-field version of eigenvalue repulsion).
Structurally, both are drift–diffusion PDEs with power-law stationary solutions.

If we consider a single-factor portfolio (N=1N=1, so the allocation matrix reduces to a vector), the repulsion term vanishes and the spectral FP reduces to the standard wealth FP.
In this limit, the spectral exponent should reduce to the Pareto exponent.
The scalar wealth model is the N=1N=1 projection of the matrix model.
Figure [3](#S9.F3 "Figure 3 ‣ 9 The Fokker–Planck Connection ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics") summarises the flow from the three forces through the spectral density to the wealth distribution.

Three forces on singular values σk\sigma\_{k}Gradient signal−η​uk⊤​(∇Wℒ)​vk-\eta\,u\_{k}^{\top}(\nabla\_{W}\mathcal{L})\,v\_{k}Survival constraintη​D​(m−n+1)/(2​σk)\eta D\,(m{-}n{+}1)/(2\sigma\_{k})Eigenvalue repulsion−η​D​∑j≠kσk/(σk2−σj2)-\eta D\sum\_{j\neq k}\sigma\_{k}/(\sigma\_{k}^{2}{-}\sigma\_{j}^{2})smart moneyminimum positiondiversificationStationary spectral density: p​(σ)∝σm−n+1​e−β1​σ2/4​η​Dp(\sigma)\propto\sigma^{m-n+1}\,e^{-\beta\_{1}\sigma^{2}/4\eta D}σ\sigmap​(σ)p(\sigma)bulk (core)tail ∼σm−n+1\sim\!\sigma^{m-n+1} (satellites)Itô projectionx=‖W‖Fx=\|W\|\_{F}Wealth distribution: π​(x)∝x−1−α\pi(x)\propto x^{-1-\alpha},  α=1+vradial/Deff\alpha=1+v\_{\mathrm{radial}}/D\_{\mathrm{eff}}xx (wealth)π​(x)\pi(x)Pareto tailα=1+β12​η​D\alpha=1+\frac{\beta\_{1}}{2\eta D}


spectral exponent
m−n+1m-n+1
↓\downarrow
Pareto exponent
α\alpha


Figure 3: From forces to wealth distributions.
The three forces in the singular-value SDE ([3](#S3.E3 "Equation 3 ‣ 3 Portfolio Dynamics: The Three Forces of SGD ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) — gradient signal, survival constraint, and eigenvalue repulsion — determine the stationary spectral density (middle).
The gamma-type density has a concentrated bulk (core portfolio) and a power-law tail (satellite positions).
The radial Itô projection (Section [8](#S8 "8 Aggregation: From Matrix to Scalar via Itô’s Lemma ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) maps the matrix-valued spectral density to a scalar wealth process x=‖W‖Fx=\|W\|\_{F}, whose stationary distribution exhibits a Pareto tail with exponent α\alpha determined by the signal-to-noise ratio β1/η​D\beta\_{1}/\eta D.

## 10 The Bouchaud–Mézard Unification

Bouchaud and Mézard ([2000](#bib.bib2)) model wealth dynamics across a population of agents:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​wi=ηi​wi​d​t+∑jJi​j​(wj−wi)​d​t,dw\_{i}=\eta\_{i}w\_{i}\,dt+\sum\_{j}J\_{ij}(w\_{j}-w\_{i})\,dt, |  | (26) |

where ηi\eta\_{i} is multiplicative noise (investment returns) and Ji​jJ\_{ij} describes wealth exchange (trade, lending, redistribution) between agents.

Stack NN agents’ wealths into a vector w=(w1,…,wN)w=(w\_{1},\ldots,w\_{N}).
The exchange term is J​w−diag⁡(J​𝟏)​wJw-\operatorname{diag}(J\mathbf{1})w, a matrix–vector product minus diagonal correction.
The full dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​w=[diag⁡(η)+J−diag⁡(J​𝟏)]​w​d​t.dw=\bigl[\operatorname{diag}(\eta)+J-\operatorname{diag}(J\mathbf{1})\bigr]\,w\,dt. |  | (27) |

The matrix M=diag⁡(η)+J−diag⁡(J​𝟏)M=\operatorname{diag}(\eta)+J-\operatorname{diag}(J\mathbf{1}) has eigenvalues whose distribution determines the steady-state wealth distribution.
Bouchaud and Mézard ([2000](#bib.bib2)) show that the Pareto exponent is determined by the balance between the noise spectrum (eigenvalues of diag⁡(η)\operatorname{diag}(\eta)) and the exchange coupling JJ.

The exchange matrix JJ introduces inter-agent coupling—analogous to the eigenvalue repulsion in Olsen et al. ([2025](#bib.bib26)).

* •

  Without coupling (J=0J=0 or no repulsion): wealth and singular values evolve independently, leading to condensation.
* •

  With coupling: repulsive interaction prevents condensation and produces power-law tails.

This establishes a unified framework in which three descriptions of wealth-related dynamics share common spectral structure:

1. 1.

   Bouchaud–Mézard describes the *cross-sectional* dynamics (wealth distribution across agents).
2. 2.

   Olsen et al. ([2025](#bib.bib26)) describes the *within-portfolio* dynamics (allocations across assets).
3. 3.

   The scalar Fokker–Planck framework of Frøseth ([2026c](#bib.bib10)) provides the *radial projection* linking spectral and Pareto exponents.

All three are instances of interacting particle systems with multiplicative noise, where the interaction term prevents condensation and produces power-law distributions.
Any uniform perturbation (e.g. a tax, a fee, a regulatory cost) modifies the multiplicative noise term in all three descriptions simultaneously.

## 11 Isotropic Perturbations and Spectral Invariance

We now establish the central invariance result.
Consider any perturbation to the portfolio objective that affects all assets uniformly—what we call an *isotropic perturbation*.
Examples include a proportional wealth tax with uniform assessment, a flat management fee, a uniform transaction cost, or any regulatory levy that does not distinguish between asset classes.

### 11.1 The Isotropic Condition

An isotropic perturbation modifies the loss function as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒpost​(W)=k⋅ℒpre​(W)+const,\mathcal{L}\_{\text{post}}(W)=k\cdot\mathcal{L}\_{\text{pre}}(W)+\text{const}, |  | (28) |

where k>0k>0 is a scalar that depends on the perturbation parameters but not on the direction in weight space.
This is a uniform rescaling of the loss across all directions.

### 11.2 Spectral Consequences

This uniform rescaling produces three immediate consequences:

1. 1.

   Gradient Scaling.
   The gradient rescales uniformly: ∇Wℒpost=k​∇Wℒpre\nabla\_{W}\mathcal{L}\_{\text{post}}=k\nabla\_{W}\mathcal{L}\_{\text{pre}}.
   All signal terms in the singular-value SDE scale by the same factor kk.
2. 2.

   Repulsion Structure Preserved.
   The eigenvalue repulsion term depends only on DD and the geometry of the singular value space, not on the loss function.
   It is unaffected by the perturbation.
3. 3.

   Spectral Density Transformation.
   The stationary singular-value density becomes

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | pσpost​(σ)=pσpre​(σ/k)/k,p\_{\sigma}^{\text{post}}(\sigma)=p\_{\sigma}^{\text{pre}}\bigl(\sigma/\sqrt{k}\bigr)/\sqrt{k}, |  | (29) |

   a scale-shifted version of the pre-perturbation distribution.
   The shape (the exponent m−n+1m-n+1 in the power-law tail) is preserved.

###### Theorem 1 (Spectral Invariance).

An isotropic perturbation to the portfolio objective preserves the singular-value distribution of the allocation matrix up to a scale-and-shift transformation.
The tail exponent, the eigenportfolio directions, and the effective spectral rank are all invariant.

###### Proof sketch.

Let W∈ℝT×NW\in\mathbb{R}^{T\times N} be the allocation matrix with singular-value decomposition W=U​Σ​V⊤W=U\Sigma V^{\top}, where Σ=diag⁡(σ1,…,σmin⁡(T,N))\Sigma=\operatorname{diag}(\sigma\_{1},\ldots,\sigma\_{\min(T,N)}).
The singular-value dynamics under SGD follow the multiplicative Dyson Brownian motion ([12](#S6.E12 "Equation 12 ‣ 6.4 The Transition: Marchenko–Pastur to Inverse-Wishart ‣ 6 Timescale Regimes and Spectral Transitions ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")):

|  |  |  |
| --- | --- | --- |
|  | d​σid​t=g​(σi)⏟signal+bN​∑j≠iσi​σjσi−σj⏟repulsion+bN​σi​ξi⏟noise,\frac{\mathrm{d}\sigma\_{i}}{\mathrm{d}t}=\underbrace{g(\sigma\_{i})}\_{\text{signal}}+\underbrace{\frac{b}{N}\sum\_{j\neq i}\frac{\sigma\_{i}\sigma\_{j}}{\sigma\_{i}-\sigma\_{j}}}\_{\text{repulsion}}+\underbrace{\sqrt{\frac{b}{N}}\,\sigma\_{i}\,\xi\_{i}}\_{\text{noise}}, |  |

where g​(σi)g(\sigma\_{i}) encodes the gradient signal from the loss function.

*Step 1: Gradient rescaling.*
Under the isotropic perturbation ([28](#S11.E28 "Equation 28 ‣ 11.1 The Isotropic Condition ‣ 11 Isotropic Perturbations and Spectral Invariance ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")), ∇Wℒpost=k​∇Wℒpre\nabla\_{W}\mathcal{L}\_{\text{post}}=k\nabla\_{W}\mathcal{L}\_{\text{pre}}, so the signal term transforms as g→k​gg\to k\,g.
The repulsion term depends only on the spectral geometry of W⊤​WW^{\top}W and is independent of the loss; the noise term is determined by the learning rate and data covariance.
Both are unaffected.

*Step 2: Rescaling.*
Define σ~i=σi/k\tilde{\sigma}\_{i}=\sigma\_{i}/\sqrt{k}. By Itô’s lemma,

|  |  |  |
| --- | --- | --- |
|  | d​σ~id​t=g​(σ~i)+bN​∑j≠iσ~i​σ~jσ~i−σ~j+bN​σ~i​ξi,\frac{\mathrm{d}\tilde{\sigma}\_{i}}{\mathrm{d}t}=g(\tilde{\sigma}\_{i})+\frac{b}{N}\sum\_{j\neq i}\frac{\tilde{\sigma}\_{i}\tilde{\sigma}\_{j}}{\tilde{\sigma}\_{i}-\tilde{\sigma}\_{j}}+\sqrt{\frac{b}{N}}\,\tilde{\sigma}\_{i}\,\xi\_{i}, |  |

which is the original SDE. Hence σ~i\tilde{\sigma}\_{i} has the same stationary distribution as σipre\sigma\_{i}^{\text{pre}}.

*Step 3: Spectral invariants.*
The stationary density transforms as pσpost​(σ)=pσpre​(σ/k)/kp\_{\sigma}^{\text{post}}(\sigma)=p\_{\sigma}^{\text{pre}}(\sigma/\sqrt{k})/\sqrt{k}, confirming (5).
The tail exponent μ=1+2​m^/σ2\mu=1+2\hat{m}/\sigma^{2} depends on m^\hat{m} and σ2\sigma^{2} only through their ratio, which is scale-invariant.
The eigenportfolio directions vkv\_{k} (columns of VV) are determined by the angular part of the SVD, which is unchanged by a scalar rescaling of the loss.
The effective spectral rank reff=(∑σi)2/∑σi2r\_{\text{eff}}=(\sum\sigma\_{i})^{2}/\sum\sigma\_{i}^{2} is a ratio of homogeneous functions and is therefore scale-invariant.
∎

Since the portfolio weights are defined as wi=Wt​i/∑jWt​jw\_{i}=W\_{ti}/\sum\_{j}W\_{tj} (allocation proportion in state tt), scaling all of WW by a constant kk leaves the proportions unchanged:

|  |  |  |  |
| --- | --- | --- | --- |
|  | wpost=wpre.w^{\text{post}}=w^{\text{pre}}. |  | (30) |

The portfolio composition is invariant under any isotropic perturbation.

###### Corollary 1 (Tax Neutrality).

A proportional wealth tax satisfying conditions C1–C3 of Frøseth ([2026b](#bib.bib9))—tax liability depends only on total wealth (C1), the rate structure is smooth (C2), and all asset classes are assessed uniformly (C3)—is an isotropic perturbation with k=(1−τc)​(1−τd)k=(1-\tau\_{c})(1-\tau\_{d}).
By Theorem [1](#Thmtheorem1 "Theorem 1 (Spectral Invariance). ‣ 11.2 Spectral Consequences ‣ 11 Isotropic Perturbations and Spectral Invariance ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics"), such a tax preserves the spectral structure of the allocation matrix.
This recovers and generalises the neutrality result of Frøseth ([2026b](#bib.bib9)).

###### Proof.

Under a proportional wealth tax with capital-value rate τc\tau\_{c} and distribution rate τd\tau\_{d}, condition C3 (uniform assessment) ensures that the after-tax return on every asset ii is

|  |  |  |
| --- | --- | --- |
|  | ripost=(1−τd)​ripre−τc.r\_{i}^{\text{post}}=(1-\tau\_{d})\,r\_{i}^{\text{pre}}-\tau\_{c}. |  |

The portfolio loss function, which depends on returns through ∑iwi​ri\sum\_{i}w\_{i}r\_{i}, thus transforms as ℒpost=(1−τd)​ℒpre+c​(τc)\mathcal{L}\_{\text{post}}=(1-\tau\_{d})\,\mathcal{L}\_{\text{pre}}+c(\tau\_{c}), where c​(τc)c(\tau\_{c}) is a constant independent of WW.
This is the isotropic form ([28](#S11.E28 "Equation 28 ‣ 11.1 The Isotropic Condition ‣ 11 Isotropic Perturbations and Spectral Invariance ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) with k=(1−τc)​(1−τd)k=(1-\tau\_{c})(1-\tau\_{d}).
The result follows from Theorem [1](#Thmtheorem1 "Theorem 1 (Spectral Invariance). ‣ 11.2 Spectral Consequences ‣ 11 Isotropic Perturbations and Spectral Invariance ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics").
∎

## 12 Anisotropic Perturbations and Spectral Distortion

When a perturbation affects different assets differently, the loss landscape is modified *anisotropically*:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂ℒ∂Wt​i→∂ℒ∂Wt​i+δi​Wt​i,\frac{\partial\mathcal{L}}{\partial W\_{ti}}\to\frac{\partial\mathcal{L}}{\partial W\_{ti}}+\delta\_{i}\,W\_{ti}, |  | (31) |

where δi\delta\_{i} is the asset-specific perturbation strength.
This is the regime Olsen et al. ([2025](#bib.bib26)) identify (Proposition 6.17) as breaking their isotropic analysis and producing distorted spectra.

The consequences are:

* •

  Eigenportfolio directions vkv\_{k} rotate (portfolio tilt toward less-perturbed assets).
* •

  The repulsion structure changes (some factors compressed, others stretched).
* •

  The tail exponent becomes direction-dependent.

The portfolio weight distortion, to first order in the perturbation, is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​w∗=−1γ​V−1​(δ−δ¯⋅𝟏),\Delta w^{\*}=-\frac{1}{\gamma}V^{-1}(\delta-\bar{\delta}\cdot\mathbf{1}), |  | (32) |

where γ\gamma is risk aversion, VV is the return covariance matrix, δ=(δ1,…,δN)\delta=(\delta\_{1},\ldots,\delta\_{N}) is the vector of perturbation strengths, and δ¯\bar{\delta} is their mean.

###### Example 1 (Differential Taxation).

In the Norwegian wealth tax system, δi=τw​(1−αi)\delta\_{i}=\tau\_{w}(1-\alpha\_{i}) where αi\alpha\_{i} is the assessment fraction for asset class ii.
With αhousing=0.25\alpha\_{\text{housing}}=0.25, αshares=0.80\alpha\_{\text{shares}}=0.80, αdeposits=1.00\alpha\_{\text{deposits}}=1.00, the cross-asset variance Var⁡(αi)≈0.07\operatorname{Var}(\alpha\_{i})\approx 0.07 drives portfolio tilt toward housing.
Post-2017 discount changes (which changed αshares\alpha\_{\text{shares}} from 1.00 to 0.80 over several steps) should produce time-varying spectral distortions testable in SSB microdata.

###### Example 2 (Sector-Specific Regulation).

A financial regulation imposing different capital requirements on different sectors (e.g. Basel risk weights) enters as δi=ci\delta\_{i}=c\_{i} where cic\_{i} is the capital charge per unit of exposure to sector ii.
The spectral distortion is proportional to Var⁡(c1,…,cN)\operatorname{Var}(c\_{1},\ldots,c\_{N}).

###### Example 3 (Differential Transaction Costs).

Market microstructure costs that vary across asset classes (e.g. bid–ask spreads, brokerage fees) enter as δi=κi\delta\_{i}=\kappa\_{i} where κi\kappa\_{i} is the effective cost of trading asset ii.
Illiquid assets (high κi\kappa\_{i}) are underweighted relative to the frictionless optimum.

## 13 The Spectral Invariance Conjecture

###### Conjecture 1 (Spectral Invariance).

Consider NN assets with returns observed over TT periods.
Let the allocation matrix W∈ℝT×NW\in\mathbb{R}^{T\times N} evolve under stochastic gradient descent on a portfolio objective ℒ​(W)\mathcal{L}(W) with isotropic noise of intensity DD.

1. (a)

   The stationary singular-value distribution has tail exponent T−N+1T-N+1, and the aggregate wealth distribution formed by x=‖W‖Fx=\|W\|\_{F} has Pareto tail exponent α=1+v/D\alpha=1+v/D where vv is the mean drift of ‖W‖F\|W\|\_{F}.
2. (b)

   Any isotropic perturbation to ℒ\mathcal{L} preserves the spectral shape: the singular-value distribution shifts in scale but does not change its tail exponent or eigenportfolio directions.
3. (c)

   Any anisotropic perturbation to ℒ\mathcal{L} with asset-specific weights δi\delta\_{i} rotates the eigenportfolio directions and changes the tail exponent in a direction-dependent way.
   The magnitude of distortion is proportional to the cross-asset variance:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | distortion∝Var⁡(δ1,…,δN).\textup{distortion}\propto\operatorname{Var}(\delta\_{1},\ldots,\delta\_{N}). |  | (33) |

Status.
Parts (a) and (b) follow from combining Olsen et al. ([2025](#bib.bib26))’s theorems with the isotropic rescaling argument of Theorem [1](#Thmtheorem1 "Theorem 1 (Spectral Invariance). ‣ 11.2 Spectral Consequences ‣ 11 Isotropic Perturbations and Spectral Invariance ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics").
Part (c) requires extending Olsen et al. ([2025](#bib.bib26))’s analysis to the anisotropic case; their Proposition 6.17 is a starting point but does not give the full spectral distortion.

###### Corollary 2 (Tax Neutrality).

Setting δi=τw​(1−αi)\delta\_{i}=\tau\_{w}(1-\alpha\_{i}), part (b) recovers the neutrality conditions C1–C3 of Frøseth ([2026b](#bib.bib9)) and part (c) quantifies the cost of violating condition C3.

Interpretation.
The Conjecture provides a unified criterion for evaluating any environmental perturbation—tax, regulation, transaction cost, or fee structure—in terms of its spectral signature.
Part (a) connects spectral and Pareto exponents; part (b) characterises benign (isotropic) perturbations; part (c) quantifies distortion from differential treatment.

## 14 The Loss Function and Utility Correspondence

The loss function ℒ​(W)\mathcal{L}(W) encodes the portfolio objective.
Different loss functions (MLE, score matching, denoising score matching) encode different utility assumptions.

### 14.1 Maximum Likelihood Estimation

For maximum likelihood estimation of a drift function, the loss is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒMLE​(W)=−1T​∑t=1Tlog⁡p​(xt+1∣xt;W).\mathcal{L}\_{\text{MLE}}(W)=-\frac{1}{T}\sum\_{t=1}^{T}\log p(x\_{t+1}\mid x\_{t};W). |  | (34) |

Under the SDE model d​x=v^​(x;W)​d​t+2​D​d​Bdx=\hat{v}(x;W)\,dt+\sqrt{2D}\,dB, the transition density is approximately Gaussian:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒMLE​(W)=14​D​T​Δ​t​∑t(xt+1−xt−v^​(xt;W)​Δ​t)2+const.\mathcal{L}\_{\text{MLE}}(W)=\frac{1}{4DT\Delta t}\sum\_{t}\bigl(x\_{t+1}-x\_{t}-\hat{v}(x\_{t};W)\,\Delta t\bigr)^{2}+\text{const}. |  | (35) |

This is a quadratic loss in the residuals—a mean-squared-error objective.
Minimizing this is equivalent to maximizing expected utility in a quadratic (CRRA with γ=2\gamma=2) utility framework.

### 14.2 Score Matching and Denoising Score Matching

Score matching (Hyvärinen, [2005](#bib.bib16)) minimizes

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒSM​(θ)=𝔼x∼pdata​[12​‖sθ​(x)−∇xlog⁡pdata​(x)‖2],\mathcal{L}\_{\text{SM}}(\theta)=\mathbb{E}\_{x\sim p\_{\text{data}}}\bigl[\tfrac{1}{2}\|s\_{\theta}(x)-\nabla\_{x}\log p\_{\text{data}}(x)\|^{2}\bigr], |  | (36) |

where sθs\_{\theta} is the parametric score function.
At steady state, v​(x)=D⋅s​(x)v(x)=D\cdot s(x), so learning the score is equivalent to learning the drift.

Denoising score matching (DSM) adds Gaussian noise x~=x+σ​ϵ\tilde{x}=x+\sigma\epsilon and regresses sθ​(x~)s\_{\theta}(\tilde{x}) onto −ϵ/σ-\epsilon/\sigma.
The noise structure is isotropic by construction, which is exactly the regime where Olsen et al. ([2025](#bib.bib26))’s spectral theory applies cleanly.

Key observation: score matching loss is quadratic in the score residual, just as MLE loss is quadratic in the drift residual.
The SGD dynamics on the network weights therefore have the same mathematical structure regardless of whether we use MLE or score matching.

###### Proposition 1 (Loss–Utility Correspondence).

Let ℒ​(W)=1T​∑t‖rt​(W)‖2\mathcal{L}(W)=\frac{1}{T}\sum\_{t}\|r\_{t}(W)\|^{2} be any loss function that is quadratic in a residual vector rtr\_{t} (encompassing MLE ([35](#S14.E35 "Equation 35 ‣ 14.1 Maximum Likelihood Estimation ‣ 14 The Loss Function and Utility Correspondence ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")), score matching, and denoising score matching).
If the residuals satisfy 𝔼​[rt​rt⊤]=Σr\mathbb{E}[r\_{t}r\_{t}^{\top}]=\Sigma\_{r} with Σr\Sigma\_{r} full rank, then:

1. 1.

   The SGD gradient covariance takes the form C=4T​∑t(rt​rt⊤)⊗(xt​xt⊤)C=\frac{4}{T}\sum\_{t}(r\_{t}r\_{t}^{\top})\otimes(x\_{t}x\_{t}^{\top}), which has the Kronecker structure required by Olsen et al. ([2025](#bib.bib26)).
2. 2.

   The stationary spectral density of WW falls in the universality class characterised by the free log-normal ([11](#S6.E11 "Equation 11 ‣ 6.4 The Transition: Marchenko–Pastur to Inverse-Wishart ‣ 6 Timescale Regimes and Spectral Transitions ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) with parameters determined by the signal-to-noise ratio ‖vtrue‖2/D\|v\_{\text{true}}\|^{2}/D.
3. 3.

   The spectral tail exponent encodes the Pareto exponent of the target distribution via ([21](#S8.E21 "Equation 21 ‣ 8 Aggregation: From Matrix to Scalar via Itô’s Lemma ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")).

###### Proof sketch.

For a linear network v^​(x;W)=W​x\hat{v}(x;W)=Wx, the gradient is ∇Wℒ=−2T​∑trt​xt⊤\nabla\_{W}\mathcal{L}=-\frac{2}{T}\sum\_{t}r\_{t}\,x\_{t}^{\top}, and the gradient covariance factors as C=4​Σr⊗Σx/TC=4\,\Sigma\_{r}\otimes\Sigma\_{x}/T.
This Kronecker structure is the input assumption of Olsen et al. ([2025](#bib.bib26)), Theorem 3.2 (spectral characterisation of SGD stationary distributions).
The resulting spectral density of WW follows a gamma-type distribution with tail exponent m−n+1m-n+1, which maps to a Pareto exponent α=1+f​(m,n,β1/η​D)\alpha=1+f(m,n,\beta\_{1}/\eta D) via ([21](#S8.E21 "Equation 21 ‣ 8 Aggregation: From Matrix to Scalar via Itô’s Lemma ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")).

For a nonlinear network, the gradient is ∇Wℒ=−2T​∑trt​(∂v^/∂W)⊤\nabla\_{W}\mathcal{L}=-\frac{2}{T}\sum\_{t}r\_{t}\,(\partial\hat{v}/\partial W)^{\top}.
The Jacobian ∂v^/∂W\partial\hat{v}/\partial W introduces input-dependent curvature.
However, at each layer, the effective gradient covariance retains the Kronecker structure Cl≈Σr,l⊗Σa,lC\_{l}\approx\Sigma\_{r,l}\otimes\Sigma\_{a,l}, where Σa,l\Sigma\_{a,l} is the covariance of layer-ll activations.
This per-layer factorisation is empirically well-established and is the basis for natural gradient methods (KFAC).
Under this factorisation, the spectral analysis of Olsen et al. ([2025](#bib.bib26)) applies layer-by-layer.
∎

###### Remark.

The remaining gap for a fully rigorous result is the per-layer Kronecker approximation Cl≈Σr,l⊗Σa,lC\_{l}\approx\Sigma\_{r,l}\otimes\Sigma\_{a,l}, which holds exactly for linear networks and approximately for networks with smooth activations in the large-width regime.
Establishing this rigorously for finite-width networks with standard activations (ReLU, GELU) remains open.

## 15 Applications

The spectral portfolio framework applies to several domains.
We develop four here, emphasising that the general results of Part III specialise differently in each context.

### 15.1 Portfolio Design and Factor Structure

The core–satellite structure of the stationary spectral distribution (Definition [1](#Thmdefinition1 "Definition 1 (Core–Satellite Portfolio). ‣ 4 The Stationary Portfolio: Bulk and Tail ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) provides a principled decomposition of any portfolio.
The bulk of the singular-value distribution corresponds to broad, diversified market exposure; the power-law tail corresponds to concentrated factor bets.
The effective spectral rank reffr\_{\text{eff}} (Definition [2](#Thmdefinition2 "Definition 2 (Effective Spectral Rank). ‣ 4 The Stationary Portfolio: Bulk and Tail ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) measures portfolio complexity and is directly computable from allocation data.

For portfolio construction, the three forces (Section [3](#S3 "3 Portfolio Dynamics: The Three Forces of SGD ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) provide new micro-foundations: the gradient signal identifies high-return factors, the survival constraint prevents premature abandonment of underperforming positions, and eigenvalue repulsion enforces diversification without explicit constraints.
In deep networks with LL layers, the hierarchical SVD decomposes the allocation into primary factors, combinations of factors, and final output—a fund-of-funds architecture.

### 15.2 Wealth Inequality and Power Laws

The aggregation result (Section [8](#S8 "8 Aggregation: From Matrix to Scalar via Itô’s Lemma ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) establishes that the Pareto exponent of the wealth distribution is determined by the spectral exponent of the allocation matrix via the radial projection α=1+f​(m,n,β1/η​D)\alpha=1+f(m,n,\beta\_{1}/\eta D).
The Bouchaud–Mézard unification (Section [10](#S10 "10 The Bouchaud–Mézard Unification ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) shows that the same eigenvalue repulsion mechanism that prevents portfolio concentration also prevents wealth condensation.
The matrix Kesten problem (Section [6.4](#S6.SS4 "6.4 The Transition: Marchenko–Pastur to Inverse-Wishart ‣ 6 Timescale Regimes and Spectral Transitions ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) provides the explicit link: the inverse-Wishart spectrum of the multiplicative regime maps to the Pareto tail of the wealth distribution under λ→1/λ\lambda\to 1/\lambda.

These results connect the observable spectral structure of portfolio allocations to the shape of the wealth distribution, offering a new diagnostic for inequality: the spectral tail exponent is directly measurable from microdata without parametric assumptions about the wealth distribution itself.

### 15.3 Tax Policy: Neutrality as Spectral Invariance

The Spectral Invariance Theorem (Theorem [1](#Thmtheorem1 "Theorem 1 (Spectral Invariance). ‣ 11.2 Spectral Consequences ‣ 11 Isotropic Perturbations and Spectral Invariance ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) has a direct application to wealth tax design.
The identification between weight matrices and portfolio allocations enables a dictionary between the domains:

| SGD (Olsen et al.) | Portfolio | Tax Context |
| --- | --- | --- |
| Weight matrix WW | Allocation matrix | Wealth composition |
| Loss function ℒ​(W)\mathcal{L}(W) | Negative expected utility | Tax-adjusted returns |
| Learning rate η\eta | Rebalancing speed | Adjustment speed to tax |
| Diffusion constant DD | Information noise | Market microstructure |
| Singular values σk\sigma\_{k} | Factor concentrations | Sector concentration |
| Repulsion term | Diversification pressure | Tendency away from concentration |

Table 2: Dictionary linking SGD weight dynamics, portfolio optimization, and tax design.

Under conditions C1–C3 of Frøseth ([2026b](#bib.bib9))—tax liability depends only on total wealth (C1), rates are smooth (C2), and all asset classes are assessed uniformly (C3)—the post-tax loss satisfies ℒpost=k⋅ℒpre+const\mathcal{L}\_{\text{post}}=k\cdot\mathcal{L}\_{\text{pre}}+\text{const} with k=(1−τc)​(1−τd)k=(1-\tau\_{c})(1-\tau\_{d}), which is an isotropic perturbation.
By Corollary [1](#Thmcorollary1 "Corollary 1 (Tax Neutrality). ‣ 11.2 Spectral Consequences ‣ 11 Isotropic Perturbations and Spectral Invariance ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics"), such a tax preserves the spectral structure.

When C3 is violated, the Norwegian system provides a concrete test case.
With αhousing=0.25\alpha\_{\text{housing}}=0.25, αshares=0.80\alpha\_{\text{shares}}=0.80, αdeposits=1.00\alpha\_{\text{deposits}}=1.00, the cross-asset variance Var⁡(αi)≈0.07\operatorname{Var}(\alpha\_{i})\approx 0.07 drives spectral distortion aligned with the assessment differentials.
The post-2017 changes to αshares\alpha\_{\text{shares}} should produce time-varying spectral shifts testable in wealth register data.

### 15.4 Neural Network Diagnostics

The spectral theory predicts that the singular-value distribution of trained weight matrices should reflect the complexity of the target distribution.
For neural networks trained on stochastic processes—such as neural SDEs learning drift or score functions—the weight spectrum serves as a convergence diagnostic: deviation from the predicted spectral shape indicates incomplete learning.

Denoising score matching should produce weight matrices with cleaner spectral structure than MLE training, because DSM’s noise is isotropic by construction and thus falls squarely within the universality class of Olsen et al. ([2025](#bib.bib26)).
This prediction is testable by comparing weight spectra across training objectives on the same data.

## 16 Testable Predictions

The framework yields predictions at three levels.

### 16.1 General Spectral Predictions

1. 1.

   Spectral tail exponent from portfolio data.
   Compute the SVD of wealth portfolios (e.g. from Norwegian SSB microdata).
   The tail exponent of the singular-value distribution should be T−N+1T-N+1 where TT is the observation window and NN the number of asset classes.
2. 2.

   Cross-sectional variation by investor horizon.
   Long-horizon investors (low effective DD) should have fatter spectral tails (more concentrated factor exposures) than short-horizon investors.
   Testable by segmenting wealth-holders by holding period.
3. 3.

   Weight spectrum of trained networks.
   After training a neural network on wealth or return data, the weight spectrum should reflect the Pareto exponent of the target distribution.
   Deviation signals incomplete convergence.
4. 4.

   DSM vs. MLE spectral comparison.
   Denoising score matching should produce weight matrices with cleaner spectral structure (closer to Olsen et al. ([2025](#bib.bib26))’s predictions) than MLE training, because DSM’s noise is isotropic by construction.
5. 5.

   Computational cost vs. spectral complexity.
   Training networks on data with high intrinsic dimensionality (fat spectral tails, large reffr\_{\text{eff}}) requires more computation.
   Testable by comparing training time across datasets with known spectral structure.
6. 6.

   Finite-width effects.
   Olsen et al. ([2025](#bib.bib26))’s results hold in the large-rr limit.
   The predicted spectral exponent should hold approximately for finite-width networks, with deviations decreasing as width increases.

### 16.2 Tax-Specific Predictions

1. 7.

   Spectral shift around Norwegian tax reforms.
   The introduction and variation of the verdsettelsesrabatt (valuation discount) changed αshares\alpha\_{\text{shares}} from 1.00 to 0.80 over several steps.
   The anisotropic perturbation should produce measurable rotation of eigenportfolio directions and direction-dependent tail distortion.
2. 8.

   Distortion proportional to Var⁡(αi)\operatorname{Var}(\alpha\_{i}).
   The magnitude of portfolio distortion should be proportional to the cross-asset variance of assessment fractions.
   Norway’s system (Var≈0.07\operatorname{Var}\approx 0.07) provides a quantitative benchmark.

## 17 Open Questions and Future Work

Several important questions remain open:

1. 1.

   Anisotropic extension.
   Part (c) of Conjecture [1](#Thmconjecture1 "Conjecture 1 (Spectral Invariance). ‣ 13 The Spectral Invariance Conjecture ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics") requires extending Olsen et al. ([2025](#bib.bib26))’s analysis to anisotropic noise.
   Their Proposition 6.17 begins this, but the full spectral distortion (eigenportfolio rotation, tail exponent change) remains to be derived.
2. 2.

   Finite-width corrections.
   Olsen et al. ([2025](#bib.bib26))’s results are asymptotic.
   What are the correction terms for finite-width networks?
   How large do m,nm,n need to be for the predictions to hold?
3. 3.

   Budget constraints.
   In practice, investors face constraints (∑iwi=1\sum\_{i}w\_{i}=1).
   The unconstrained Olsen SDE does not enforce this.
   How do constraints modify the spectral evolution?
4. 4.

   Nonlinear activations.
   We assume linear output (network is a linear projection of hidden units).
   How do nonlinear final layers (softmax, sigmoid) change the spectral dynamics?
5. 5.

   Compute ff for intermediate regimes.
   The single-factor ([22](#S8.E22 "Equation 22 ‣ 8 Aggregation: From Matrix to Scalar via Itô’s Lemma ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) and large-NN ([23](#S8.E23 "Equation 23 ‣ 8 Aggregation: From Matrix to Scalar via Itô’s Lemma ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) limits are now explicit.
   Extend to finite p>1p>1 with eigenvalue repulsion corrections, and verify numerically against simulated spectra.
6. 6.

   Policy optimization.
   Given a target Pareto exponent (e.g., α=2\alpha=2 as observed in Norway), what perturbation structure minimizes spectral distortion while achieving the desired distributional shift?
   This inverse problem applies to tax design, regulation, and fee structures alike.

## 18 Relation to Existing Literature

We position this work relative to six major research areas.

### 18.1 Random Matrix Theory in Finance

Laloux et al. ([1999](#bib.bib18)) and Ledoit and Wolf ([2004](#bib.bib19)) apply RMT to estimate asset covariance matrices.
Our contribution: RMT also describes the structure of portfolio weight matrices (not just return covariances), and this structure is directly observable in trained neural networks.
The connection to Pareto wealth distributions is new.

### 18.2 Deep Learning and Portfolio Optimization

Heaton et al. ([2017](#bib.bib14)); Zhang et al. ([2021](#bib.bib33)); Buehler et al. ([2019](#bib.bib4)) develop neural network methods for portfolio optimization.
Our framework provides a spectral lens on why these networks learn specific factor structures, and predicts their spectra from the data distribution.

### 18.3 Ergodicity Economics

Peters ([2019](#bib.bib28)); Peters and Gell-Mann ([2016](#bib.bib29)); Berman et al. ([2020](#bib.bib1)) distinguish ensemble and time averages in wealth dynamics.
Our contribution: the spectral gap (Section [7](#S7 "7 The Ergodicity Gap as Spectral Observable ‣ Spectral Portfolio Theory: From SGD Weight Matrices to Wealth Dynamics")) is a measurable proxy for non-ergodicity, and spectral-preserving perturbations minimize it.

### 18.4 SGD Spectral Theory

Martin and Mahoney ([2021](#bib.bib23)); Pennington and Worah ([2017](#bib.bib27)); Gunasekar et al. ([2018](#bib.bib13)) develop spectral theory of SGD in deep learning.
Olsen et al. ([2025](#bib.bib26)) extend this to matrix-valued weight evolution.
Our contribution: we show this theory has direct portfolio and wealth-distribution interpretations.

### 18.5 Classical Portfolio Theory

Merton ([1969](#bib.bib24), [1971](#bib.bib25)) define optimal portfolio choice via mean–variance analysis.
Cover ([1991](#bib.bib6)) develops universal portfolio theory.
Our framework extends these: the spectral decomposition reveals factor structure emerging from learning data, and spectral invariance provides a new rationale for neutral policy design.

### 18.6 Wealth Dynamics and Power Laws

Drăgulescu and Yakovenko ([2000](#bib.bib7)); Yakovenko and Rosser ([2009](#bib.bib32)); Gabaix and Koijen ([2022](#bib.bib11)) study mechanisms generating power-law wealth distributions.
Kesten ([1973](#bib.bib17)) develops the Kesten recursion, central to our multiplicative regime.
Our contribution: we connect these scalar mechanisms to the matrix spectral theory via the matrix Kesten problem and the free log-normal interpolation.

## 19 Conclusion

This paper establishes spectral portfolio theory as a unified framework connecting random matrix theory, portfolio dynamics, and wealth distribution.

The core results are:

1. 1.

   Neural network weight matrices are portfolio allocation matrices, and their spectral structure encodes factor decompositions faithful to the underlying data.
2. 2.

   The three forces in the singular-value evolution—gradient signal, survival constraint, and eigenvalue repulsion—translate directly into portfolio economics: smart money, information-driven survival, and endogenous diversification.
3. 3.

   The stationary spectral distribution exhibits a core–satellite structure (bulk plus power-law tail) that matches empirical wealth and institutional portfolio data.
4. 4.

   The spectral transition from additive (Marchenko–Pastur) to multiplicative (inverse-Wishart) regimes, mediated by the free log-normal, explains how daily return statistics relate to long-run wealth concentration.
5. 5.

   The Bouchaud–Mézard cross-sectional model, the Olsen within-portfolio model, and the scalar Fokker–Planck framework all emerge from the same underlying spectral dynamics, unified via common power-law mechanisms.
6. 6.

   The Spectral Invariance Theorem establishes that isotropic perturbations preserve spectral shape, while anisotropic perturbations produce distortion proportional to their cross-asset variance.
   This general result specialises to tax neutrality, regulatory impact assessment, and transaction cost analysis.

The framework is testable: portfolio SVDs can be computed from microdata, spectral exponents can be compared against wealth Pareto exponents, and spectral shifts around policy reforms can be measured directly.
Applications span portfolio construction, inequality measurement, tax design, and neural network diagnostics.

Future work should: (1) extend the theory to anisotropic noise; (2) derive finite-width corrections; (3) handle budget constraints and nonlinear activations; (4) explicitly compute the spectral-to-Pareto mapping; and (5) solve the inverse problem of perturbation design—choosing the structure that achieves a distributional target while minimizing spectral distortion.

### Acknowledgements

The author acknowledges the use of Claude (Anthropic) for assistance with
literature review, LaTeX typesetting, mathematical exposition, and
editorial refinement, and Lemma (Axiomatic AI) for review and proof
checking. All substantive arguments, economic reasoning, and conclusions
are the author’s own.

## References

* Berman et al. (2020)

  Yonatan Berman, Ole Peters, and Alexander Adamou.
  Far from the madding crowd: Collective wisdom in prediction markets.
  *arXiv preprint*, 2020.
* Bouchaud and Mézard (2000)

  Jean-Philippe Bouchaud and Marc Mézard.
  Wealth condensation in a simple model of economy.
  *Physica A*, 282(3–4):536–545, 2000.
* Bouchaud and Potters (2003)

  Jean-Philippe Bouchaud and Marc Potters.
  *Theory of Financial Risk and Derivative Pricing: From
  Statistical Physics to Risk Management*.
  Cambridge University Press, 2nd edition, 2003.
  doi: 10.1017/CBO9780511753893.
* Buehler et al. (2019)

  Hans Buehler, Lukas Gonon, Josef Teichmann, and Ben Wood.
  Deep hedging.
  *Quantitative Finance*, 19(8):1271–1291,
  2019.
  doi: 10.1080/14697688.2019.1571683.
* Cont (2001)

  Rama Cont.
  Empirical properties of asset returns: Stylized facts and statistical
  issues.
  *Quantitative Finance*, 1(2):223–236, 2001.
  doi: 10.1080/713665670.
* Cover (1991)

  Thomas M. Cover.
  Universal portfolios.
  *Mathematical Finance*, 1(1):1–29, 1991.
  doi: 10.1111/j.1467-9965.1991.tb00002.x.
* Drăgulescu and Yakovenko (2000)

  Adrian Drăgulescu and Victor M. Yakovenko.
  Statistical mechanics of money.
  *European Physical Journal B*, 17(4):723–729, 2000.
* Frøseth (2026a)

  Anders G. Frøseth.
  Extensions to the wealth tax neutrality framework.
  2026a.
  arXiv:[2603.05277](https://arxiv.org/abs/2603.05277)
  [physics.soc-ph].
* Frøseth (2026b)

  Anders G. Frøseth.
  Asset returns, portfolio choice, and proportional wealth taxation.
  2026b.
  arXiv:[2603.05264](https://arxiv.org/abs/2603.05264)
  [physics.soc-ph].
* Frøseth (2026c)

  Anders G. Frøseth.
  Wealth taxation as a drift modification: A Fokker–Planck approach
  to tax neutrality.
  2026c.
  arXiv:[2603.05283](https://arxiv.org/abs/2603.05283)
  [physics.soc-ph].
* Gabaix and Koijen (2022)

  Xavier Gabaix and Ralph S. J. Koijen.
  In search of the origins of financial fluctuations: The inelastic
  markets hypothesis.
  Working paper, Harvard University and University of Chicago, 2022.
* Gruber (1996)

  Martin J. Gruber.
  Another puzzle: The growth in actively managed mutual funds.
  *The Journal of Finance*, 51(3):783–810,
  1996.
  doi: 10.1111/j.1540-6261.1996.tb02707.x.
* Gunasekar et al. (2018)

  Suriya Gunasekar, Jason Lee, Daniel Soudry, and Nathan Srebro.
  Implicit regularization in matrix sensing.
  In *Advances in Neural Information Processing Systems*,
  volume 31, 2018.
* Heaton et al. (2017)

  J. B. Heaton, N. G. Polson, and J. H. Witte.
  Deep learning for finance: Deep portfolios.
  *Applied Stochastic Models in Business and Industry*,
  33(1):3–12, 2017.
  doi: 10.1002/asmb.2209.
* Heston (1993)

  Steven L. Heston.
  A closed-form solution for options with stochastic volatility with
  applications to bond and currency options.
  *The Review of Financial Studies*, 6(2):327–343, 1993.
  doi: 10.1093/rfs/6.2.327.
* Hyvärinen (2005)

  Aapo Hyvärinen.
  Estimation of non-normalized statistical models by score matching.
  *Journal of Machine Learning Research*, 6:695–709,
  2005.
* Kesten (1973)

  Harry Kesten.
  Random difference equations and renewal theory for products of random
  matrices.
  *Acta Mathematica*, 131:207–248, 1973.
* Laloux et al. (1999)

  Laurent Laloux, Pierre Cizeau, Jean-Philippe Bouchaud, and Marc Potters.
  Noise dressing of financial correlation matrices.
  *Physical Review Letters*, 83(7):1467–1470,
  1999.
  doi: 10.1103/PhysRevLett.83.1467.
* Ledoit and Wolf (2004)

  Olivier Ledoit and Michael Wolf.
  Honey, I shrunk the sample covariance matrix.
  *The Journal of Portfolio Management*, 30(4):110–119, 2004.
  doi: 10.3905/jpm.2004.110.
* Lo (2004)

  Andrew W. Lo.
  The adaptive markets hypothesis: Market efficiency from an
  evolutionary perspective.
  *The Journal of Portfolio Management*, 30(5):15–29, 2004.
  doi: 10.3905/jpm.2004.442611.
* Lo (2017)

  Andrew W. Lo.
  *Adaptive Markets: Financial Evolution at the Speed of Thought*.
  Princeton University Press, Princeton, 2017.
* Markowitz (1952)

  Harry Markowitz.
  Portfolio selection.
  *Journal of Finance*, 7(1):77–91, 1952.
* Martin and Mahoney (2021)

  Charles H. Martin and Michael W. Mahoney.
  Implicit self-regularization in deep neural networks: Evidence from
  random matrix theory and implications for training.
  In *Journal of Machine Learning Research*, volume 22, pages
  1–73, 2021.
* Merton (1969)

  Robert C. Merton.
  Lifetime portfolio selection under uncertainty: The continuous-time
  case.
  *Review of Economics and Statistics*, 51(3):247–257, 1969.
  doi: 10.2307/1926560.
* Merton (1971)

  Robert C. Merton.
  Optimum consumption and portfolio rules in a continuous-time model.
  *Journal of Economic Theory*, 3(4):373–413,
  1971.
  doi: 10.1016/0022-0531(71)90038-X.
* Olsen et al. (2025)

  Thijs Olsen, Mona Fatehmanesh, James Lim, and Roger Grosse.
  From SGD to spectra: The matrix and spectral geometry of neural
  network training.
  In *Proceedings of the 42nd International Conference on Machine
  Learning*, 2025.
  arXiv:2507.12709.
* Pennington and Worah (2017)

  Jeffrey Pennington and Pratik Worah.
  Nonlinear random matrix theory for deep learning.
  In *Advances in Neural Information Processing Systems*,
  volume 30, pages 2637–2646, 2017.
* Peters (2019)

  Ole Peters.
  The ergodicity problem in economics.
  *Nature Physics*, 15:1216–1221, 2019.
* Peters and Gell-Mann (2016)

  Ole Peters and Murray Gell-Mann.
  Evaluating gambles using dynamics.
  *Chaos*, 26:023103, 2016.
  doi: 10.1063/1.4940236.
* Potters and Bouchaud (2021)

  Marc Potters and Jean-Philippe Bouchaud.
  *A First Course in Random Matrix Theory: For Physicists,
  Engineers and Data Scientists*.
  Cambridge University Press, 2021.
  doi: 10.1017/9781108768900.
* Roy (1952)

  A. D. Roy.
  Safety first and the holding of assets.
  *Econometrica*, 20(3):431–449, 1952.
  doi: 10.2307/1907413.
* Yakovenko and Rosser (2009)

  Victor M. Yakovenko and J. Barkley Rosser, Jr.
  Colloquium: Statistical mechanics of money, wealth, and income.
  *Reviews of Modern Physics*, 81(4):1703–1725, 2009.
* Zhang et al. (2021)

  Zihao Zhang, Stefan Zohren, and Stephen Roberts.
  Deep learning for portfolio optimization.
  *The Journal of Financial Data Science*, 3(2):8–20, 2021.
  doi: 10.3905/jfds.2020.1.052.

BETA