---
authors:
- Takayuki Sakuma
doc_id: arxiv:2603.07600v1
family_id: arxiv:2603.07600
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Differential Machine Learning for 0DTE Options with Stochastic Volatility and
  Jumps
url_abs: http://arxiv.org/abs/2603.07600v1
url_html: https://arxiv.org/html/2603.07600v1
venue: arXiv q-fin
version: 1
year: 2026
---


Takayuki Sakuma111e-mail: tsakuma@soka.ac.jp. 
  
Faculty of Economics, Soka University

(March 8, 2026)

###### Abstract

We present a differential machine learning method for zero-days-to-expiry (0DTE) options under a stochastic-volatility jump-diffusion model that computes prices and Greeks in a single network evaluation.
To handle the ultra-short-maturity regime, we represent the price in Black–Scholes form with a maturity-gated variance correction, and combine supervision on prices and Greeks with a PIDE-residual penalty.
To make the jump contribution identifiable, we introduce a separate jump-operator network and train it with a three-stage procedure.
In Bates-model simulations, the method improves jump-term approximation relative to one-stage baselines, keeps price errors close to one-stage alternatives while improving Greeks accuracy, produces stable one-day delta hedges, and is substantially faster than a Fourier-based pricing benchmark.

## 1 Introduction

Zero-days-to-expiry (0DTE) options have grown rapidly over the past few years and account for a large fraction of trading volume.
Recent empirical work finds elevated intraday jump activity and large gamma exposures around the at-the-money (ATM) region [[Bandi et al.(2023)](#bib.bibx2), [Bozovic(2025)](#bib.bibx6), [Dim et al.(2024)](#bib.bibx8)]. These features raise two practical challenges:
(i) the underlying dynamics are better captured by a diffusion model with jumps, and
(ii) the very short maturities and frequent intraday rebalancing require fast computation of option prices and Greeks.

We apply differential machine learning (DML)[[Huge and Savine(2020)](#bib.bibx14)] to 0DTE options under the stochastic-volatility jump-diffusion (SVJD) model. Learning-based models can reduce pricing cost: once trained, prices and Greeks are obtained from a single network evaluation. However, the numerically most unstable region is near the money, where Greeks can become very large for 0DTE options with jumps.

A common approach in machine-learning PDE solvers is to enforce the governing PDE by penalizing its residual at sampled state points, together with terminal/boundary conditions [[Raissi et al.(2019)](#bib.bibx16)]. Several recent studies apply this residual-penalty approach to option pricing with jumps by including a PIDE-residual term in the training objective [[Fu and Hirsa(2020)](#bib.bibx11), [Sun et al.(2025)](#bib.bibx17), [Bansal et al.(2026)](#bib.bibx3)]. Three design choices in our scheme are central:

1. 1.

   We adopt DML which trains a single price network on both option values and Greeks. Greeks are computed by automatic differentiation of the network output with respect to its inputs and are included directly in the training loss function.
2. 2.

   Instead of predicting prices directly, the network learns a variance correction in a Black–Scholes formula[[Black and Scholes(1973)](#bib.bibx5)], scaled so that the correction vanishes as τ→0\tau\to 0.
   This ensures the correct short-maturity limit (payoff) and reduces the approximation difficulty faced by the network in the near-singular regime. The approach is common in learning-based volatility surface models [[Liu et al.(2019)](#bib.bibx15), [Ackerer et al.(2020)](#bib.bibx1)].
3. 3.

   We introduce a second neural network to represent the compensated jump operator. When the jump component is identified only through a PIDE-residual penalty, the optimizer can trade off errors between the diffusion and jump terms while keeping the overall residual small. As a result, a small residual does not imply that the learned jump operator matches the model-implied jump integral. Therefore we use the second network to make the residual penalty informative about the jump term.

#### Paper organization.

Section [2](#S2 "2 Bates model ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") presents the Bates model. Section [3](#S3 "3 DML for PIDEs ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") introduces the DML-based neural network and the three-stage training scheme. Section [4](#S4 "4 Neural network and training ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") specifies the loss functions and constraints. Section [5](#S5 "5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") reports numerical experiments, and the appendix provides additional results. All quantitative results in this paper are based on simulated data generated from the specified stochastic models.

## 2 Bates model

We work under the Bates stochastic-volatility jump-diffusion model, which combines a Heston-type variance process with Merton-style lognormal price jumps [[Merton(1976)](#bib.bibx13), [Heston(1993)](#bib.bibx12), [Bates(1996)](#bib.bibx4)].
Under the risk-neutral measure let StS\_{t} denote the underlying asset, VtV\_{t} the instantaneous variance, rr the risk-free rate, and qq the dividend.
The dynamics are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​StSt−\displaystyle\frac{dS\_{t}}{S\_{t^{-}}} | =(r−q−λ​κJ)​d​t+Vt​d​WtS+(eY−1)​d​Nt,\displaystyle=(r-q-\lambda\kappa\_{J})\,dt+\sqrt{V\_{t}}\,dW^{S}\_{t}+(e^{Y}-1)\,dN\_{t}, |  | (1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Vt\displaystyle dV\_{t} | =κ​(θ−Vt)​d​t+σv​Vt​d​WtV,\displaystyle=\kappa(\theta-V\_{t})\,dt+\sigma\_{v}\sqrt{V\_{t}}\,dW^{V}\_{t}, |  | (2) |

where (WtS,WtV)(W^{S}\_{t},W^{V}\_{t}) is a two-dimensional Brownian motion with correlation ρ\rho, NtN\_{t} is a Poisson process with intensity λ\lambda, and the jump sizes are i.i.d. with Y∼𝒩​(μJ,σJ2)Y\sim\mathcal{N}(\mu\_{J},\sigma\_{J}^{2}).
Here κ\kappa is the variance mean-reversion speed in ([2](#S2.E2 "In 2 Bates model ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")) and κJ=𝔼​[eY−1]=exp⁡(μJ+12​σJ2)−1\kappa\_{J}=\mathbb{E}[e^{Y}-1]=\exp(\mu\_{J}+\tfrac{1}{2}\sigma\_{J}^{2})-1.

For a European call option with maturity τ\tau and strike KK, the risk-neutral call price CC solves the following PIDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂C∂τ\displaystyle\frac{\partial C}{\partial\tau} | =(r−q)​S​∂C∂S+κ​(θ−V)​∂C∂V+12​V​S2​∂2C∂S2+12​σv2​V​∂2C∂V2+ρ​σv​V​S​∂2C∂S​∂V−r​C+λ​𝒥​[C],\displaystyle=(r-q)S\frac{\partial C}{\partial S}+\kappa(\theta-V)\frac{\partial C}{\partial V}+\frac{1}{2}VS^{2}\frac{\partial^{2}C}{\partial S^{2}}+\frac{1}{2}\sigma\_{v}^{2}V\frac{\partial^{2}C}{\partial V^{2}}+\rho\sigma\_{v}VS\frac{\partial^{2}C}{\partial S\partial V}-rC+\lambda\,\mathcal{J}[C], |  | (3) |

with terminal condition C​(S,V,0)=(S−K)+C(S,V,0)=(S-K)^{+}.
The compensated jump operator is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥​[C]​(S,V,τ)=∫ℝ[C​(S​ey,V,τ)−C​(S,V,τ)−(ey−1)​S​CS​(S,V,τ)]​fY​(y)​𝑑y,\mathcal{J}[C](S,V,\tau)=\int\_{\mathbb{R}}\Big[C(Se^{y},V,\tau)-C(S,V,\tau)-(e^{y}-1)S\,C\_{S}(S,V,\tau)\Big]f\_{Y}(y)\,dy, |  | (4) |

where fYf\_{Y} denotes the density of the logarithmic jump size YY.
We use the dimensionless log-moneyness

|  |  |  |
| --- | --- | --- |
|  | x:=log⁡(S/K),τ:=T−tx:=\log(S/K),\qquad\tau:=T-t |  |

and the diffusion part of the operator is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒdiff​u\displaystyle\mathcal{L}\_{\mathrm{diff}}u | =ut+(r−q)​ux+κ​(θ−V)​uV+12​V​(ux​x−ux)+ρ​σv​V​ux​V+12​σv2​V​uV​V−r​u,\displaystyle=u\_{t}+(r-q)u\_{x}+\kappa(\theta-V)u\_{V}+\tfrac{1}{2}V(u\_{xx}-u\_{x})+\rho\sigma\_{v}V\,u\_{xV}+\tfrac{1}{2}\sigma\_{v}^{2}Vu\_{VV}-ru, |  | (5) |

where ut=−uτu\_{t}=-u\_{\tau} since τ\tau is time-to-maturity.
We define the residual

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​(𝐱):=ℒdiff​uϕ​(𝐱)+λ​Jψ​(𝐱),R(\mathbf{x}):=\mathcal{L}\_{\mathrm{diff}}u\_{\phi}(\mathbf{x})+\lambda\,J\_{\psi}(\mathbf{x}), |  | (6) |

where JψJ\_{\psi} denotes a neural approximation to the normalized compensated jump operator

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jψ​(𝐱):=∫ℝ[u​(x+y,V,τ)−u​(x,V,τ)−(ey−1)​ux​(x,V,τ)]​fY​(y)​𝑑y.J\_{\psi}(\mathbf{x}):=\int\_{\mathbb{R}}\Big[u(x+y,V,\tau)-u(x,V,\tau)-(e^{y}-1)u\_{x}(x,V,\tau)\Big]f\_{Y}(y)\,dy. |  | (7) |

In the architecture below, the second network outputs JψJ\_{\psi} directly and is supervised against a numerical quadrature proxy for Jψ​(𝐱)J\_{\psi}(\mathbf{x}).

## 3 DML for PIDEs

Figure [1](#S3.F1 "Figure 1 ‣ 3 DML for PIDEs ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") summarizes our neural-network model. The solid arrows correspond to forward evaluations while dashed arrows indicate computations derived from these outputs. The input is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱=(x,τ,V,κ,θ,σv,ρ,λ,μJ,σJ)∈ℝ10.\mathbf{x}=(x,\tau,V,\kappa,\theta,\sigma\_{v},\rho,\lambda,\mu\_{J},\sigma\_{J})\in\mathbb{R}^{10}. |  | (8) |

Rather than predicting prices directly, the first network outputs a variance correction Δ​Vϕ​(𝐱)\Delta V\_{\phi}(\mathbf{x}).
We define an effective variance

|  |  |  |  |
| --- | --- | --- | --- |
|  | Veff​(𝐱)=max⁡{V+g​(τ)​Δ​Vϕ​(𝐱),ε},g​(τ)=1−exp⁡(−τ/τ0),V\_{\mathrm{eff}}(\mathbf{x})=\max\big\{V+g(\tau)\,\Delta V\_{\phi}(\mathbf{x}),\,\varepsilon\big\},\qquad g(\tau)=1-\exp(-\tau/\tau\_{0}), |  | (9) |

and return a Black–Scholes call price with volatility σeff=Veff\sigma\_{\mathrm{eff}}=\sqrt{V\_{\mathrm{eff}}}. The g​(τ)g(\tau) forces the learned variance correction to vanish near expiry, which stabilizes training and preserves the payoff limit.
Since we work in log-moneyness, we normalize the strike to K=1K=1:

|  |  |  |
| --- | --- | --- |
|  | uϕ​(𝐱):=CBS​(S=ex,K=1,r=0.01,q=0,τ,σeff)u\_{\phi}(\mathbf{x}):=C\_{\mathrm{BS}}\!\big(S=e^{x},\,K=1,\,r=0.01,\,q=0,\,\tau,\,\sigma\_{\mathrm{eff}}\big) |  |

and Greeks are obtained by automatic differentiation of uϕu\_{\phi}. In parallel, a jump-operator network approximates the compensated jump operator Jψ​(𝐱)J\_{\psi}(\mathbf{x}), and the two networks are coupled through the jump-PIDE residual.
Because the jump term is not identifiable from a residual loss alone, we supervise JψJ\_{\psi} and use the three-stage schedule described in Subsection [3.2](#S3.SS2 "3.2 Three-stage training with jump supervision ‣ 3 DML for PIDEs ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps").

Inputs
𝐱\mathbf{x}
Variance-correction networkΔ​Vϕ​(𝐱)\Delta V\_{\phi}(\mathbf{x})Jump-operator network


BS with a variance adjustment
  
g​(τ)=1−exp⁡(−τ/τ0)g(\tau)=1-\exp(-\tau/\tau\_{0})\;\;
  
Veff=max⁡{V+g​(τ)​Δ​Vϕ​(𝐱),ε}V\_{\mathrm{eff}}=\max\{V+g(\tau)\,\Delta V\_{\phi}(\mathbf{x}),\,\varepsilon\}
  
uϕ​(𝐱)=CBS​(S=ex,K=1,τ,Veff)u\_{\phi}(\mathbf{x})=C\_{\mathrm{BS}}(S=e^{x},K=1,\tau,\sqrt{V\_{\mathrm{eff}}})

Compensated
jump term
Jψ​(𝐱)J\_{\psi}(\mathbf{x})

Greeks
(d​e​l​t​a,g​a​m​m​a,v​e​g​a)(delta,gamma,vega)

PIDE residual:
R​(𝐱)=ℒdiff​uϕ​(𝐱)+λ​Jψ​(𝐱)R(\mathbf{x})=\mathcal{L}\_{\mathrm{diff}}u\_{\phi}(\mathbf{x})+\lambda\,J\_{\psi}(\mathbf{x})

Stage 1
train ϕ\phi
freeze ψ\psi

Stage 2
train ψ\psi
freeze ϕ\phi

Stage 3
joint fine-tune ϕ,ψ\phi,\psi
+ PIDE residual penalty
+ self-consistency

Figure 1: Architecture and training procedure. Stages 1–3 describe the three-stage training scheme. A variance-correction network returns Δ​Vϕ​(𝐱)\Delta V\_{\phi}(\mathbf{x}), multiplied by a deterministic maturity function g​(τ)g(\tau) so that the correction vanishes as τ→0\tau\to 0. Prices are produced by substituting the resulting effective variance into the Black–Scholes call formula, yielding uϕ​(𝐱)u\_{\phi}(\mathbf{x}) (not the plain BS price unless Δ​Vϕ≡0\Delta V\_{\phi}\equiv 0). A separate network outputs the compensated jump contribution Jψ​(𝐱)J\_{\psi}(\mathbf{x}). Greeks are obtained by automatic differentiation of uϕu\_{\phi}. The jump-PIDE residual R​(𝐱)R(\mathbf{x}) is computed and penalized at randomly sampled points. Stages 1–3 depict the three-stage training scheme used for jump-term identifiability.

### 3.1 Twin-network

A standard model fits a network uϕ​(𝐱)u\_{\phi}(\mathbf{x}) by

|  |  |  |
| --- | --- | --- |
|  | minϕ⁡𝔼​[(uϕ​(𝐱)−u​(𝐱))2].\min\_{\phi}\;\mathbb{E}\big[(u\_{\phi}(\mathbf{x})-u(\mathbf{x}))^{2}\big]. |  |

DML augments this objective by adding supervised targets for selected Greeks ∂u/∂xi\partial u/\partial x\_{i}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minϕ⁡𝔼​[(uϕ−u)2+∑i∈ℐωi​(∂xiuϕ−∂xiu)2],\min\_{\phi}\;\mathbb{E}\Big[(u\_{\phi}-u)^{2}+\sum\_{i\in\mathcal{I}}\omega\_{i}\big(\partial\_{x\_{i}}u\_{\phi}-\partial\_{x\_{i}}u\big)^{2}\Big], |  | (10) |

where ∂xiuϕ\partial\_{x\_{i}}u\_{\phi} are computed by automatic differentiation and ℐ\mathcal{I} indexes the Greeks of interest (e.g., delta, gamma, and vega). Following Huge and Savine (2020), we refer to this as a “twin network”, meaning one price network with Greeks computed by automatic differentiation.
Because the same parameters ϕ\phi must explain both values and derivatives, derivative supervision supplies shape information and improves accuracy.

Training can be further regularized by adding a PDE-residual penalty computed from the same automatic-differentiation derivatives. But if we approximate the nonlocal jump operator J​[u]J[u] by a separate network Jψ​(𝐱)J\_{\psi}(\mathbf{x}) and use it only through the residual

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​(𝐱)=ℒdiff​uϕ​(𝐱)+λ​Jψ​(𝐱),R(\mathbf{x})\;=\;\mathcal{L}\_{\mathrm{diff}}u\_{\phi}(\mathbf{x})+\lambda\,J\_{\psi}(\mathbf{x}), |  | (11) |

uϕu\_{\phi} and JψJ\_{\psi} are not separately identifiable: in principle, for any uϕu\_{\phi} one can set
Jψ=−ℒdiff​uϕ/λJ\_{\psi}=-\mathcal{L}\_{\mathrm{diff}}u\_{\phi}/\lambda and obtain R≡0R\equiv 0.
This mechanism can lead to a degenerate solution in which the jump network cancels diffusion-operator errors and reduces the residual without learning a meaningful jump contribution. We therefore supervise the jump operator explicitly.
Using the reference price urefu^{\text{ref}}, we construct a numerical proxy for the jump term and train JψJ\_{\psi} to match it.

### 3.2 Three-stage training with jump supervision

As noted in Section [3.1](#S3.SS1 "3.1 Twin-network ‣ 3 DML for PIDEs ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps"), JψJ\_{\psi} can act as a residual-cancelling degree of freedom, absorbing diffusion-operator errors without approximating the jump operator.
We therefore use a three-stage schedule:

1. 1.

   Stage 1 (price and Greeks). Train the price network (freeze JψJ\_{\psi}) using the price and Greek terms plus the no-arbitrage penalties.
2. 2.

   Stage 2 (jump reference). Freeze the price network and train the jump network to match a numerical proxy of the compensated jump term computed from the reference prices:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Jref​(x,V,τ):=𝔼​[uref​(x+Y,V,τ)−uref​(x,V,τ)]−κJ​uxref​(x,V,τ).J^{\text{ref}}(x,V,\tau):=\mathbb{E}\big[u^{\text{ref}}(x+Y,V,\tau)-u^{\text{ref}}(x,V,\tau)\big]-\kappa\_{J}\,u^{\text{ref}}\_{x}(x,V,\tau). |  | (12) |

   On randomly sampled state points we approximate the expectation in ([12](#S3.E12 "In item 2 ‣ 3.2 Three-stage training with jump supervision ‣ 3 DML for PIDEs ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")) with a Gauss–Hermite rule applied to uref​(x+Y,V,τ)u^{\text{ref}}(x+Y,V,\tau) and penalize Jψ−Jref​(x,V,τ)J\_{\psi}-J^{\text{ref}}(x,V,\tau) using a Huber loss function.
3. 3.

   Stage 3 (joint refinement). Train both networks jointly. We also include a *self-consistency* regularizer that penalizes the mismatch between JψJ\_{\psi} and Jref​(x,V,τ)J^{\text{ref}}(x,V,\tau).

## 4 Neural network and training

We use two fully-connected feedforward networks, each with width 192, depth 4, and SiLU activation functions (152,834 parameters in total).

### 4.1 Loss function, constraints, and weights

Let u^=uϕ​(𝐱)\widehat{u}=u\_{\phi}(\mathbf{x}) and (Δ^,Γ^,ν^)(\widehat{\Delta},\widehat{\Gamma},\widehat{\nu}) be Greeks.
We minimize the weighted objective

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(ϕ,ψ)\displaystyle\mathcal{L}(\phi,\psi) | =𝔼​[w​(𝐱)​(u^−u)2]+ωG​𝔼​[w​(𝐱)​m​(𝐱)​∑g∈{Δ,Γ,ν}ωg​(λg​(g^−g))2]\displaystyle=\mathbb{E}\Big[w(\mathbf{x})(\widehat{u}-u)^{2}\Big]+\omega\_{G}\,\mathbb{E}\Big[w(\mathbf{x})\,m(\mathbf{x})\sum\_{g\in\{\Delta,\Gamma,\nu\}}\omega\_{g}\,(\lambda\_{g}(\widehat{g}-g))^{2}\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +ωR​𝔼​[w​(𝐱)​R​(𝐱)2]+ωcol​𝔼​[(u^−uref)2]+ωNA​𝔼​[𝒫NA​(𝐱)],\displaystyle\quad+\omega\_{R}\,\mathbb{E}\Big[w(\mathbf{x})\,R(\mathbf{x})^{2}\Big]+\omega\_{\text{col}}\,\mathbb{E}\Big[(\widehat{u}-u^{\text{ref}})^{2}\Big]+\omega\_{\text{NA}}\,\mathbb{E}\big[\mathcal{P}\_{\text{NA}}(\mathbf{x})\big], |  | (13) |

with:

* •

  w​(𝐱)w(\mathbf{x}) upweights the ATM region and short maturities,

  |  |  |  |
  | --- | --- | --- |
  |  | w​(𝐱)=1+WATM​𝕀​(|x|<0.1)+WSHORT​𝕀​(τ<0.02)+WATM&SHORT​𝕀​(|x|<0.1,τ<0.02).w(\mathbf{x})=1+W\_{\text{ATM}}\,\mathbb{I}(|x|<0.1)+W\_{\text{SHORT}}\,\mathbb{I}(\tau<0.02)+W\_{\text{ATM\&SHORT}}\,\mathbb{I}(|x|<0.1,\tau<0.02). |  |
* •

  m​(𝐱)=𝕀​(uref​(𝐱)>10−4)m(\mathbf{x})=\mathbb{I}(u^{\text{ref}}(\mathbf{x})>10^{-4}) drops Greek-loss contributions in deep OTM regions.
* •

  𝒫NA\mathcal{P}\_{\text{NA}} encodes simple static no-arbitrage constraints:
  delta bounds (0≤Δ≤10\leq\Delta\leq 1), convexity (ux​x−ux≥0u\_{xx}-u\_{x}\geq 0), and vega monotonicity (ν≥0\nu\geq 0), implemented as squared positive-part penalties (⋅)+2(\cdot)\_{+}^{2}, where (z)+=max⁡{z,0}(z)\_{+}=\max\{z,0\}.
* •

  Greek scaling uses λg≈1/𝔼​[g2]\lambda\_{g}\approx 1/\sqrt{\mathbb{E}[g^{2}]} estimated once from the training set.

#### Self-consistency penalty.

During joint training we augment ([13](#S4.E13 "In 4.1 Loss function, constraints, and weights ‣ 4 Neural network and training ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")) with a penalty that encourages the learned jump network to agree with a low-order numerical evaluation of the compensated operator applied to the current price network:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒSC\displaystyle\mathcal{L}\_{\mathrm{SC}} | :=ωSC​𝔼res​[∥Jψ​(𝐱)−J^​[uϕ]​(𝐱)∥2],\displaystyle:=\omega\_{\mathrm{SC}}\,\mathbb{E}\_{\text{res}}\Big[\big\lVert J\_{\psi}(\mathbf{x})-\widehat{J}[u\_{\phi}](\mathbf{x})\big\rVert^{2}\Big], |  | (14) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J^​[uϕ]​(𝐱)\displaystyle\widehat{J}[u\_{\phi}](\mathbf{x}) | :=∑i=1nSCwi​(uϕ​(x+μJ+σJ​zi,V,τ)−uϕ​(x,V,τ))−κJ​uϕ,x​(x,V,τ),\displaystyle:=\sum\_{i=1}^{n\_{\mathrm{SC}}}w\_{i}\Big(u\_{\phi}(x+\mu\_{J}+\sigma\_{J}z\_{i},V,\tau)-u\_{\phi}(x,V,\tau)\Big)-\kappa\_{J}\,u\_{\phi,x}(x,V,\tau), |  | (15) |

where (zi,wi)i=1nSC(z\_{i},w\_{i})\_{i=1}^{n\_{\mathrm{SC}}} are nodes/weights of a Gauss–Hermite rule for Z∼𝒩​(0,1)Z\sim\mathcal{N}(0,1) and we use ωSC=0.05,nSC=16\omega\_{\mathrm{SC}}=0.05,n\_{\mathrm{SC}}=16.

#### Robust Γ\Gamma (gamma) loss and numerical filtering.

For the most sensitive derivative targets we may replace the squared error in ([13](#S4.E13 "In 4.1 Loss function, constraints, and weights ‣ 4 Neural network and training ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")) with a robust Huber loss and ignore samples where the reference violates convexity due to numerical quadrature error. We adopt a Huber loss to reduce the impact of isolated quadrature-induced outliers, which is especially relevant for Γ\Gamma and the jump-term. For Γ\Gamma this takes the form

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒΓ\displaystyle\mathcal{L}\_{\Gamma} | :=𝔼data​[w​(𝐱)​m​(𝐱)​𝕀​(Γref​(𝐱)≥0)​Huberδ​(λΓ​(Γ^​(𝐱)−Γref​(𝐱)))].\displaystyle:=\mathbb{E}\_{\text{data}}\Big[w(\mathbf{x})\,m(\mathbf{x})\,\mathbb{I}(\Gamma^{\text{ref}}(\mathbf{x})\geq 0)\,\mathrm{Huber}\_{\delta}\big(\lambda\_{\Gamma}(\widehat{\Gamma}(\mathbf{x})-\Gamma^{\text{ref}}(\mathbf{x}))\big)\Big]. |  | (16) |

The training stages correspond to different restrictions of the full objective:

* •

  Stage 1: minimize ([13](#S4.E13 "In 4.1 Loss function, constraints, and weights ‣ 4 Neural network and training ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")) using only the price and Greek terms and 𝒫NA\mathcal{P}\_{\text{NA}} (i.e. set ωR=ωcol=0\omega\_{R}=\omega\_{\text{col}}=0 and freeze ψ\psi).
* •

  Stage 2: freeze ϕ\phi and minimize a Huber loss on the jump network, 𝔼​[Huber​(Jψ−Jref​(x,V,τ))]\mathbb{E}[\mathrm{Huber}(J\_{\psi}-J^{\text{ref}}(x,V,\tau))], where JrefJ^{\text{ref}} is computed from the reference Fourier pricer (Section [3.2](#S3.SS2 "3.2 Three-stage training with jump supervision ‣ 3 DML for PIDEs ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")).
* •

  Stage 3: jointly refine both networks with the full loss ([13](#S4.E13 "In 4.1 Loss function, constraints, and weights ‣ 4 Neural network and training ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")) (small ωR\omega\_{R}) plus weak jump supervision and the self-consistency penalty ([14](#S4.E14 "In Self-consistency penalty. ‣ 4.1 Loss function, constraints, and weights ‣ 4 Neural network and training ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")). For the Γ\Gamma target we use the robust variant ([16](#S4.E16 "In Robust Γ (gamma) loss and numerical filtering. ‣ 4.1 Loss function, constraints, and weights ‣ 4 Neural network and training ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")).

## 5 Numerical experiments

Our experiments address two questions:
How much do DML and residual regularization improve 0DTE price/Greek accuracy, and do the resulting prices and Greeks remain reliable in simple hedging tests?
Additional model-choice robustness checks (BS/Merton baselines and an SVCJ extension) are in Appendix [A](#A1 "Appendix A Model comparison ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps").

### 5.1 Setting

Benchmark prices and Greeks are generated by a Fourier-transform pricer for the Bates SVJD model (1024-point quadrature; cutoff umax=1000u\_{\max}=1000) [[Carr and Madan(1999)](#bib.bibx7)].
Reference Greeks are computed by automatic differentiation of the same implementation.

* •

  Log-moneyness:
    
  with probability pcore=0.7p\_{\text{core}}=0.7 we draw from a near-ATM band x∼Unif​[−0.1,0.1]x\sim\mathrm{Unif}[-0.1,0.1] (“ATM core”);
    
  otherwise x∼Unif​[−0.5,0.5]x\sim\mathrm{Unif}[-0.5,0.5].
* •

  Maturity (strict 0DTE):
    
  with probability pshort=0.7p\_{\text{short}}=0.7 we draw very short maturities τ∼Unif​[10−4,1/504]\tau\sim\mathrm{Unif}[10^{-4},1/504];
    
  otherwise τ∼Unif​[1/504,1/252]\tau\sim\mathrm{Unif}[1/504,1/252].
  Here pshortp\_{\text{short}} is the mixture weight used to oversample the shortest maturities.
* •

  Parameters are sampled uniformly over the following ranges:

  |  |  |  |
  | --- | --- | --- |
  |  | v0∈[0.01,0.2],κ∈[1,5],θ∈[0.02,0.1],\displaystyle v\_{0}\in[0.01,0.2],\;\kappa\in[1,5],\;\theta\in[0.02,0.1], |  |
  |  |  |  |
  | --- | --- | --- |
  |  | σv∈[0.1,1.0],ρ∈[−0.9,−0.3],λ∈[0.1,2.0],\displaystyle\sigma\_{v}\in[0.1,1.0],\;\rho\in[-0.9,-0.3],\;\lambda\in[0.1,2.0], |  |
  |  |  |  |
  | --- | --- | --- |
  |  | μJ∈[−0.2,0.0],σJ∈[0.05,0.5].\displaystyle\mu\_{J}\in[-0.2,0.0],\;\sigma\_{J}\in[0.05,0.5]. |  |

To stabilize jump-term training, we add additional state points by pushing data points through the jump map x↦x+Yx\mapsto x+Y and clamping to |x|≤6|x|\leq 6.
We compute reference prices on these jump-shifted (“margin”) points and add a small auxiliary price-consistency loss. This extends supervision beyond |x|≤0.5|x|\leq 0.5 to the region visited by the jump integral.
Deep OTM options have tiny prices and noisy Greeks, so we ignore Greek targets when the reference price is below 10−410^{-4}.

We use ωG=0.7\omega\_{G}=0.7, ωR=0.01\omega\_{R}=0.01, ωcol=0.1\omega\_{\text{col}}=0.1, ωNA=0.05\omega\_{\text{NA}}=0.05, and (ωΔ,ωΓ,ων)=(1.0,0.3,0.5)(\omega\_{\Delta},\omega\_{\Gamma},\omega\_{\nu})=(1.0,0.3,0.5). We also set the self-consistency weight ωSC=0.05\omega\_{\mathrm{SC}}=0.05 with nSC=16n\_{\mathrm{SC}}=16. We set (WATM,WSHORT,WATM&SHORT)=(1.0,1.0,1.0)(W\_{\text{ATM}},W\_{\text{SHORT}},W\_{\text{ATM\&SHORT}})=(1.0,1.0,1.0).

In the ultra-short regime, second derivatives are numerically unstable. We therefore (i) ignore deep-OTM Greek targets, (ii) use robust losses and/or clipping for sensitive targets (Γ\Gamma and the jump term), and (iii) add no-arbitrage shape penalties, particularly convexity (ux​x−ux≥0)(u\_{xx}-u\_{x}\geq 0).

### 5.2 Accuracy across models

We compare four models:

1. 1.

   A (price-only): train on prices only (no Greek loss, no residual penalty).
2. 2.

   B (DML): train on prices and Greeks (via automatic differentiation), with no residual penalty.
3. 3.

   C (DML+residual): train on prices, Greeks, and the residual penalty ([13](#S4.E13 "In 4.1 Loss function, constraints, and weights ‣ 4 Neural network and training ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")).
4. 4.

   D (three-stage): three-stage training with jump supervision (Section [3.2](#S3.SS2 "3.2 Three-stage training with jump supervision ‣ 3 DML for PIDEs ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")).

We train the one-stage variants (Models A–C) for 100 epochs with Adam (learning rate 10−310^{-3}) and batch size 64. The three-stage model uses 100 epochs (Stage 1), 60 epochs (Stage 2), and 30 epochs (Stage 3).
Table [1](#S5.T1 "Table 1 ‣ 5.2 Accuracy across models ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") reports RMSE and Table [2](#S5.T2 "Table 2 ‣ 5.2 Accuracy across models ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") reports RMSE in a region |x|<0.05|x|<0.05 and τ≤1/252\tau\leq 1/252. Residual statistics are in Table [3](#S5.T3 "Table 3 ‣ 5.2 Accuracy across models ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps").

Table 1: RMSE (price and Greeks) on the validation set (N=500N=500; seed=42).

| Model | Price RMSE | Δ\Delta RMSE | Γ\Gamma RMSE | Vega RMSE |
| --- | --- | --- | --- | --- |
| A (price-only) | 0.000190 | 0.00853 | 3.28 | 0.001155 |
| B (DML) | 0.000234 | 0.00553 | 3.11 | 0.000328 |
| C (DML+residual) | 0.000234 | 0.00554 | 3.11 | 0.000334 |
| D (three-stage) | 0.000231 | 0.00548 | 3.11 | 0.000321 |




Table 2: RMSE in the strict-short ATM bucket (|x|<0.05|x|<0.05, τ≤1/252\tau\leq 1/252), computed on the validation sample (N=500N=500; seed=42).

| Model | Price RMSE | Δ\Delta RMSE | Γ\Gamma RMSE |
| --- | --- | --- | --- |
| A (price-only) | 0.000185 | 0.01272 | 4.14 |
| B (DML) | 0.000280 | 0.00770 | 3.82 |
| C (DML+residual) | 0.000280 | 0.00770 | 3.82 |
| D (three-stage) | 0.000274 | 0.00761 | 3.81 |




Table 3: Residual statistics of the PIDE check: mean absolute residual 𝔼​|R|\mathbb{E}|R| and sd(RR).

| Model | 𝔼​|R|\mathbb{E}|R| | sd(RR) |
| --- | --- | --- |
| A (price-only) | 0.0339 | 0.0960 |
| B (DML) | 0.0040 | 0.0112 |
| C (DML+residual) | 0.0050 | 0.0118 |
| D (three-stage) | 0.0746 | 0.0680 |




Table 4: Normalised RMSEs and tail absolute errors (validation sample; N=500N=500, seed=42).

| Model | nRMSEP | relRMSEP | nRMSEΔ | nRMSEΓ | |eP|90|e\_{P}|\_{90} | |eP|99|e\_{P}|\_{99} | |eΓ|90|e\_{\Gamma}|\_{90} | |eΓ|99|e\_{\Gamma}|\_{99} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A (price-only) | 0.0015 | 0.0027 | 0.0123 | 0.2525 | 0.000379 | 0.000696 | 1.100 | 7.794 |
| B (DML) | 0.0018 | 0.0034 | 0.0079 | 0.2378 | 0.000459 | 0.000906 | 0.3532 | 3.628 |
| C (DML+residual) | 0.0018 | 0.0034 | 0.0079 | 0.2378 | 0.000458 | 0.000902 | 0.3504 | 3.628 |
| D (three-stage) | 0.0018 | 0.0033 | 0.0078 | 0.2376 | 0.000458 | 0.000879 | 0.2503 | 3.628 |

We additionally report scale-invariant metrics and tail error quantiles in Table [4](#S5.T4 "Table 4 ‣ 5.2 Accuracy across models ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") with two scale-free versions of the price RMSE:

|  |  |  |
| --- | --- | --- |
|  | nRMSEP:=RMSEP𝔼​[(uref)2],relRMSEP:=RMSEP𝔼​[uref].\mathrm{nRMSE}\_{P}:=\frac{\mathrm{RMSE}\_{P}}{\sqrt{\mathbb{E}[(u^{\mathrm{ref}})^{2}]}},\qquad\mathrm{relRMSE}\_{P}:=\frac{\mathrm{RMSE}\_{P}}{\mathbb{E}[u^{\mathrm{ref}}]}. |  |

For Greeks we use

|  |  |  |
| --- | --- | --- |
|  | nRMSEΔ:=RMSEΔ𝔼​[(Δref)2],nRMSEΓ:=RMSEΓ𝔼​[(Γref)2].\mathrm{nRMSE}\_{\Delta}:=\frac{\mathrm{RMSE}\_{\Delta}}{\sqrt{\mathbb{E}[(\Delta^{\mathrm{ref}})^{2}]}},\qquad\mathrm{nRMSE}\_{\Gamma}:=\frac{\mathrm{RMSE}\_{\Gamma}}{\sqrt{\mathbb{E}[(\Gamma^{\mathrm{ref}})^{2}]}}. |  |

The tail metrics |eP|p|e\_{P}|\_{p} and |eΓ|p|e\_{\Gamma}|\_{p} denote the pp-th percentile of the absolute price and gamma errors, respectively.
Tables [1](#S5.T1 "Table 1 ‣ 5.2 Accuracy across models ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")–[4](#S5.T4 "Table 4 ‣ 5.2 Accuracy across models ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") suggest three points. First, Model B improves delta accuracy (first-order risk) and vega accuracy relative to the price-only fit (Model A) (Table [1](#S5.T1 "Table 1 ‣ 5.2 Accuracy across models ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")). For gamma Γ\Gamma, improvements are clearer in tail error quantiles than in global RMSE (Table [4](#S5.T4 "Table 4 ‣ 5.2 Accuracy across models ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")). Second, the one-stage PIDE residual penalty (Model C) does not improve prices or Greeks relative to Model B. This is consistent with jump settings, where the residual can be reduced via cancellation between the differential and jump terms rather than by learning an interpretable jump operator. Third, the three-stage model (Model D) yields the best overall Δ\Delta and vega RMSE among the Greek-supervised models and slightly improves Γ\Gamma tail error quantiles, although Γ\Gamma remains the most delicate target in the region (|x|<0.05,τ≤1/252)(|x|<0.05,\,\tau\leq 1/252).

Figure [2](#S5.F2 "Figure 2 ‣ 5.2 Accuracy across models ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") visualizes true vs predicted prices and Greeks for Model D. In the ultra-short maturity regime (τ→0\tau\to 0), Γ\Gamma is extremely localised around the money: for the majority of (deep ITM/OTM) evaluation points the true Γ\Gamma is numerically close to zero, so the scatter plots naturally show a dense cluster at Γ≈0\Gamma\approx 0.

![Refer to caption](2603.07600v1/figures/Pred_1222.png)


Figure 2: Three-stage model: true vs predicted (price, delta, gamma, vega) on validation.

### 5.3 Jump-term comparison

This subsection clarifies why a small PIDE residual is not evidence that the learned jump component represents the intended compensated jump integral.
We first report error distributions for the final three-stage model (Figure [3](#S5.F3 "Figure 3 ‣ 5.3 Jump-term comparison ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")), and then directly test whether the learned compensated jump contribution JψJ\_{\psi} matches a numerical proxy computed from the reference pricer (Figure [4](#S5.F4 "Figure 4 ‣ 5.3 Jump-term comparison ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")).

![Refer to caption](2603.07600v1/figures/Presidual_1222.png)


(a) Price residuals u^−u\widehat{u}-u.

![Refer to caption](2603.07600v1/figures/PIDEresidual_1222.png)


(b) PIDE residual R​(𝐱)R(\mathbf{x}) (three-stage).

Figure 3: Error distributions for the three-stage model.

We focus on the domain |x|≤0.5|x|\leq 0.5. Despite its small PIDE residual, the residual-regularized model C (DML+residual) without jump supervision shows a large mismatch between JψJ\_{\psi} and JrefJ^{\text{ref}} (RMSE =9.34×10−2=9.34\times 10^{-2}).
The three-stage model yields a smaller jump-term error (RMSE =1.35×10−2=1.35\times 10^{-2}).
Price RMSE on the same points is comparable (C: 7.17×10−37.17\times 10^{-3}, D: 5.89×10−35.89\times 10^{-3}). Therefore, residual magnitude alone is not sufficient for model selection when diffusion and jump terms can offset each other.

![Refer to caption](2603.07600v1/figures/Jump_sanity_1222_1.png)


(a) C (DML+residual)

![Refer to caption](2603.07600v1/figures/Jump_sanity_1222_2.png)


(b) D (three-stage)

Figure 4: Jump-term check in the data domain (|x|≤0.5|x|\leq 0.5): predicted compensated jump term vs numeric integral proxy.

This indicates that when the jump contribution is a free network output, it can absorb approximation errors from the diffusion part and still drive the residual toward zero.
Supervising JψJ\_{\psi} against a numerical proxy (three-stage schedule) improves identification of the jump contribution.

### 5.4 Comparison: Fourier pricer vs DML model

We compare wall-clock times for batch pricing of NN European call options, holding model parameters fixed.
Table [5](#S5.T5 "Table 5 ‣ 5.4 Comparison: Fourier pricer vs DML model ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") reports relative speedups and price RMSE against the Fourier benchmark.
Over this range, the computational scaling is close to linear in NN.

Table 5: Speed comparison between the Fourier pricer and the DML pricer. We report speedup (Fourier wall-clock time divided by DML time) to reduce hardware dependence; absolute timings and benchmarking code are provided in the reproducibility bundle.

| NN | Speedup (Fourier / DML) | Price RMSE |
| --- | --- | --- |
| 10310^{3} | 6.3×6.3\times | 2.15×10−42.15\times 10^{-4} |
| 10410^{4} | 34.7×34.7\times | 2.25×10−42.25\times 10^{-4} |
| 5×1045\times 10^{4} | 47.4×47.4\times | 2.20×10−42.20\times 10^{-4} |

### 5.5 One-day delta-hedging

The data-generating process is the Bates SVJD model and we simulate npaths=5000n\_{\text{paths}}=5000 paths of (St,Vt)(S\_{t},V\_{t}) over one trading day T=1/252T=1/252 using an Euler scheme with nsteps=24n\_{\text{steps}}=24.
Jumps are simulated by a Bernoulli approximation with step probability p≈λ​Δ​tp\approx\lambda\,\Delta t.
To avoid unrealistically large per-step jump probabilities when λ​Δ​t\lambda\,\Delta t is not very small, we cap this probability at 0.20.2, i.e. we use p=min⁡(λ​Δ​t,0.2)p=\min(\lambda\,\Delta t,0.2).
We use a stressed parameter set

|  |  |  |
| --- | --- | --- |
|  | (v0,κ,θ,σv,ρ,λ,μJ,σJ)=(0.04,3.0,0.04,1.0,−0.8,2.0,−0.05,0.20),(v\_{0},\kappa,\theta,\sigma\_{v},\rho,\lambda,\mu\_{J},\sigma\_{J})=(0.04,3.0,0.04,1.0,-0.8,2.0,-0.05,0.20), |  |

chosen to amplify jump activity and gamma effects.
First we conduct stock-only Δ\Delta hedges: the hedge portfolio contains the underlying and a cash account. We run the hedge separately for each strike K∈{0.9,1.0,1.1}K\in\{0.9,1.0,1.1\} on the same set of simulated (St,Vt)(S\_{t},V\_{t}) paths, which produces 5000 P&L outcomes per strike. At t=0t=0 we short one call with strike K∈{0.9,1.0,1.1}K\in\{0.9,1.0,1.1\} and maturity TT.
At each time tkt\_{k} we compute delta from either the Fourier pricer (true) or the model (DML), rebalance the stock position, and carry the residual in a cash account accruing at rate rr. At maturity we record hedging P&L as final portfolio value minus option payoff.
Aggregating across strikes (1500015000 paths total), we report the summary statistics in
Table [6](#S5.T6 "Table 6 ‣ 5.5 One-day delta-hedging ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps"). Figure [5](#S5.F5 "Figure 5 ‣ 5.5 One-day delta-hedging ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") plots P&L histograms which show that the distributional difference between true and model delta hedges is small.

Table 6: One-day Δ\Delta-hedging P&L summary.

| Model | Mean | Std | 5% | Median | 95% |
| --- | --- | --- | --- | --- | --- |
| True Δ\Delta | −1.40×10−4-1.40\times 10^{-4} | 9.92×10−39.92\times 10^{-3} | −5.60×10−4-5.60\times 10^{-4} | +3.20×10−4+3.20\times 10^{-4} | +1.63×10−3+1.63\times 10^{-3} |
| DML Δ\Delta | −1.30×10−4-1.30\times 10^{-4} | 9.92×10−39.92\times 10^{-3} | −5.00×10−4-5.00\times 10^{-4} | +3.50×10−4+3.50\times 10^{-4} | +1.59×10−3+1.59\times 10^{-3} |

![Refer to caption](2603.07600v1/figures/Hedge1_1222.png)


Figure 5: One-day Δ\Delta-hedging P&L (True vs DML delta), stressed Bates SVJD parameter regime.

Conditioning on whether at least one price jump occurs along the underlying path yields
sd​(P&LDML)≈0.02263\mathrm{sd}(\mathrm{P\&L}\_{\text{DML}})\approx 0.02263 on jump samples (N=150N=150 pooled path–strike observations) versus ≈0.00971\approx 0.00971 on no-jump samples (N=14,850N=14{,}850).
These results show that realized jumps substantially thicken the one-day hedge-P&L tails in this stressed experiment.

Second we compare three one-option second-order hedges:
(i) a ratio-type Δ+Γ\Delta+\Gamma hedge
(ii) a weighted ridge least-squares (LS) hedge that fits (Δ,Γ)(\Delta,\Gamma) jointly across stock and one hedge option, and
(iii) a P&L-increment regression hedge (PL-LS) that learns state-dependent hedge ratios with ridge regularization.

Here “ratio-type” means that the hedge-option position is chosen from an explicit gamma ratio with ridge regularization, and the stock position is then set to neutralize the remaining delta. Such a hedge, using only one additional option, can be ill-conditioned when the hedge option’s gamma is small, because the hedge weight effectively scales like a ratio of gammas.

The LS and PL-LS hedges use the same instrument set but choose the positions jointly from a penalized fitting criterion or from a regression on price increments.

Concretely, for a given hedge strike KHK\_{\mathrm{H}}, let CtmainC^{\mathrm{main}}\_{t} and CtHC^{\mathrm{H}}\_{t} denote the prices of the liability option and the hedge option, and let (Δtmain,Γtmain)(\Delta^{\mathrm{main}}\_{t},\Gamma^{\mathrm{main}}\_{t}) and (ΔtH,ΓtH)(\Delta^{\mathrm{H}}\_{t},\Gamma^{\mathrm{H}}\_{t}) denote their spot Greeks.
For the self-financing portfolio

|  |  |  |
| --- | --- | --- |
|  | Πt=−Ctmain+wH,t​CtH+wS,t​St+Bt,\Pi\_{t}=-C^{\mathrm{main}}\_{t}+w\_{\mathrm{H},t}C^{\mathrm{H}}\_{t}+w\_{S,t}S\_{t}+B\_{t}, |  |

the ratio-type Δ+Γ\Delta+\Gamma implementation updates the hedge-option position at each rebalance date by the ridge-stabilized gamma match

|  |  |  |
| --- | --- | --- |
|  | wH,t=Γtmain​ΓtH(ΓtH)2+ηΓ,w\_{\mathrm{H},t}=\frac{\Gamma^{\mathrm{main}}\_{t}\,\Gamma^{\mathrm{H}}\_{t}}{(\Gamma^{\mathrm{H}}\_{t})^{2}+\eta\_{\Gamma}}, |  |

which approximates Γtmain/ΓtH\Gamma^{\mathrm{main}}\_{t}/\Gamma^{\mathrm{H}}\_{t} when |ΓtH||\Gamma^{\mathrm{H}}\_{t}| is not too small.
The stock position is then chosen as

|  |  |  |
| --- | --- | --- |
|  | wS,t=Δtmain−wH,t​ΔtH,w\_{S,t}=\Delta^{\mathrm{main}}\_{t}-w\_{\mathrm{H},t}\Delta^{\mathrm{H}}\_{t}, |  |

so that the portfolio is approximately both delta- and gamma-neutral.
At inception we set

|  |  |  |
| --- | --- | --- |
|  | B0=C0main−wH,0​C0H−wS,0​S0,B\_{0}=C^{\mathrm{main}}\_{0}-w\_{\mathrm{H},0}C^{\mathrm{H}}\_{0}-w\_{S,0}S\_{0}, |  |

and at each rebalance date update (wH,t,wS,t)(w\_{\mathrm{H},t},w\_{S,t}) and the cash account so that the strategy remains self-financing.
The weighted ridge LS hedge uses the same instrument pair (St,CtH)(S\_{t},C^{\mathrm{H}}\_{t}), but chooses (wS,wH)(w\_{S},w\_{\mathrm{H}}) by minimising

|  |  |  |
| --- | --- | --- |
|  | minwS,wH⁡wΔ​(Δtmain−wS−wH​ΔtH)2+wΓ​(Γtmain−wH​ΓtH)2+λ​(wS2+wH2).\min\_{w\_{S},w\_{\mathrm{H}}}\;w\_{\Delta}(\Delta^{\mathrm{main}}\_{t}-w\_{S}-w\_{\mathrm{H}}\Delta^{\mathrm{H}}\_{t})^{2}+w\_{\Gamma}(\Gamma^{\mathrm{main}}\_{t}-w\_{\mathrm{H}}\Gamma^{\mathrm{H}}\_{t})^{2}+\lambda(w\_{S}^{2}+w\_{\mathrm{H}}^{2}). |  |

PL-LS estimates time-dependent coefficient vectors (Ak,Bk)(A\_{k},B\_{k}) from a ridge regression of option price increments Δ​Cmain\Delta C\_{\text{main}} on basis-weighted (Δ​S,Δ​Chedge)(\Delta S,\Delta C\_{\text{hedge}}), and then sets the hedge with wS=ϕ⊤​Akw\_{S}=\phi^{\top}A\_{k} and wH=ϕ⊤​Bkw\_{\mathrm{H}}=\phi^{\top}B\_{k} (with ϕ=[1,log⁡m,(log⁡m)2,V,τ]⊤\phi=[1,\log m,(\log m)^{2},V,\tau]^{\top}).

We consider an option fixed at a one-day ATM call with Kmain=1.00K\_{\mathrm{main}}=1.00 and T=1/252T=1/252. We then run four separate hedging experiments, each using the stock plus one additional same-maturity call with hedge strike KH∈{0.99,1.00,1.01,1.02}K\_{\mathrm{H}}\in\{0.99,1.00,1.01,1.02\}. Figure [6](#S5.F6 "Figure 6 ‣ 5.5 One-day delta-hedging ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") pools the resulting P&L observations across these four separate KHK\_{\mathrm{H}} choices.

Figure [6](#S5.F6 "Figure 6 ‣ 5.5 One-day delta-hedging ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") summarizes the comparison: the left column shows the central-region P&L density for ratio-type Δ+Γ\Delta+\Gamma, LS, and PL-LS, plotted separately for (top) true Greeks and (bottom) DML Greeks.
The two central-density panels are visually similar at this scale, consistent with the close agreement between DML Greeks and benchmark Greeks. In addition, our DML pricer outputs (u,Δ,Γ)(u,\Delta,\Gamma) in a single forward pass, so these risk measures can be computed without re-pricing loops or finite differences.

The right panel shows the tail of the ratio-type Δ+Γ\Delta+\Gamma hedge via the CCDF of |P&L||\mathrm{P\&L}|.
LS/PL-LS are omitted on the right because their tails collapse near zero at this scale.

![Refer to caption](2603.07600v1/figures/Hedge2_fixed_1222.png)


Figure 6: Δ+Γ\Delta+\Gamma hedging illustration for a one-day ATM liability call (Kmain=1.00K\_{\mathrm{main}}=1.00). In each run the hedge portfolio contains the stock and one additional one-day call at a single strike KH∈{0.99,1.00,1.01,1.02}K\_{\mathrm{H}}\in\{0.99,1.00,1.01,1.02\}; the four KHK\_{\mathrm{H}} choices are run separately and the plotted distributions pool the resulting outcomes across them. Left: central-region density of hedging P&L for ratio-type Δ+Γ\Delta+\Gamma, LS, and PL-LS, shown separately for (top) true Greeks and (bottom) DML Greeks. The two central-density panels are almost indistinguishable at this scale, reflecting that the DML Greeks are close to the benchmark. Right: tail behaviour of the ratio-type Δ+Γ\Delta+\Gamma hedge, shown as the CCDF of |P&L||\mathrm{P\&L}| (true vs. DML) on log scales; a one-option gamma-based ratio hedge can become unstable when the hedge option’s gamma is near zero.

Appendix [A](#A1 "Appendix A Model comparison ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") reports additional model-choice checks.
In particular, a Merton jump-diffusion baseline improves substantially over Black–Scholes when prices are generated under the Bates SVJD model, while an SVCJ extension with contemporaneous variance jumps is almost indistinguishable from the Bates model.

## 6 Conclusion

We present a differential machine learning method for 0DTE options under a stochastic-volatility jump-diffusion model.
Prices are expressed in Black–Scholes form with a maturity-gated variance adjustment; training combines price-and-Greeks supervision with a PIDE-residual penalty.
Across our numerical experiments, the method is substantially faster while keeping delta/vega errors low and price errors comparable.
Our hedging experiment indicates that deltas produced by the network remain reliable even under stressed parameters, while gamma remains the most delicate target in the strict-short ATM regime.
Moving from simulation to market data will require addressing microstructure noise and bid–ask spreads, while incorporating transaction costs and operational constraints.

## References

* [Ackerer et al.(2020)]

  Ackerer, D., Tagasovska, N., and Vatter, T. (2020).
  Deep smoothing of the implied volatility surface.
  *Advances in Neural Information Processing Systems*, 33.
* [Bandi et al.(2023)]

  Bandi, F. M., Fusari, N., and Renò, R. (2023).
  0DTE Option Pricing.
  *Working paper*. Available at SSRN: <https://ssrn.com/abstract=4503344> (doi:10.2139/ssrn.4503344).
* [Bansal et al.(2026)]

  Bansal, S., Boro, P., and Natesan, S. (2026).
  Application of physics informed neural networks to partial integro-differential equations in financial modeling and decision making.
  *Applied Soft Computing*, 186:114208.
* [Bates(1996)]

  Bates, D. S. (1996).
  Jumps and stochastic volatility: Exchange rate processes implicit in Deutsche mark options.
  *The Review of Financial Studies*, 9(1):69–107.
* [Black and Scholes(1973)]

  Black, F. and Scholes, M. (1973).
  The pricing of options and corporate liabilities.
  *Journal of Political Economy*, 81(3):637–654.
* [Bozovic(2025)]

  Bozovic, M. (2025).
  Intraday Jumps and 0DTE Options: Pricing and Hedging Implications.
  *Working paper*. Available at SSRN: <https://ssrn.com/abstract=5223127> (doi:10.2139/ssrn.5223127).
* [Carr and Madan(1999)]

  Carr, P., and Madan, D. B. (1999).
  Option valuation using the fast Fourier transform.
  *Journal of Computational Finance*, 2(4):61–73.
* [Dim et al.(2024)]

  Dim, C., Eraker, B., and Vilkov, G. (2024).
  0DTEs: Trading, Gamma Risk and Volatility Propagation.
  *Working paper*. Available at SSRN: <https://ssrn.com/abstract=4692190> (doi:10.2139/ssrn.4692190).
* [Duffie et al.(2000)]

  Duffie, D., Pan, J., and Singleton, K. (2000).
  Transform analysis and asset pricing for affine jump-diffusions.
  *Econometrica*, 68(6):1343–1376.
* [Frandsen et al.(2022)]

  Frandsen, M. G., Pedersen, T. C., and Poulsen, R. (2022).
  Delta force: option pricing with differential machine learning.
  *Digital Finance*, 4(1):1–15.
* [Fu and Hirsa(2020)]

  Fu, W. and Hirsa, A. (2020).
  An unsupervised deep learning approach in solving partial integro-differential equations.
  arXiv preprint arXiv:2006.15012.
* [Heston(1993)]

  Heston, S. L. (1993).
  A closed-form solution for options with stochastic volatility with applications to bond and currency options.
  *The Review of Financial Studies*, 6(2):327–343.
* [Merton(1976)]

  Merton, R. C. (1976).
  Option pricing when underlying stock returns are discontinuous.
  *Journal of Financial Economics*, 3(1–2):125–144.
* [Huge and Savine(2020)]

  Huge, B. and Savine, A. (2020).
  Differential machine learning.
  *arXiv preprint arXiv:2005.02347*.
* [Liu et al.(2019)]

  Liu, S., Oosterlee, C. W., and Bohte, S. M. (2019).
  Pricing options and computing implied volatilities using neural networks.
  *Risks*, 7(1):16.
* [Raissi et al.(2019)]

  Raissi, M., Perdikaris, P., and Karniadakis, G. E. (2019).
  Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations.
  *Journal of Computational Physics*, 378:686–707.
* [Sun et al.(2025)]

  Sun, Q., Huang, H., Yang, X., and Zhang, Y. (2025).
  Stochastic jump diffusion process informed neural networks for accurate American option pricing under data scarcity.
  *Applied Soft Computing*, 176:113164.

## Appendix A Model comparison

Because 0DTE options are extremely short-dated, it is natural to ask whether simpler dynamics would suffice for the pricing and hedging checks considered in this paper.
This appendix reports two model-comparison checks:
(i) Black–Scholes and Merton jump-diffusion baselines versus a Bates SVJD benchmark, and
(ii) an extension with contemporaneous jumps in price and variance (SVCJ) [[Duffie et al.(2000)](#bib.bibx9)].

### A.1 Black–Scholes and Merton vs a Bates benchmark

We use the Bates SVJD Fourier pricer as a benchmark and compare two analytic baselines:
(i) Black–Scholes with constant volatility σ=v0\sigma=\sqrt{v\_{0}} and no jumps, and
(ii) Merton’s lognormal jump-diffusion [[Merton(1976)](#bib.bibx13)] with the *same* jump parameters (λ,μJ,σJ)(\lambda,\mu\_{J},\sigma\_{J}) and constant diffusion volatility v0\sqrt{v\_{0}}.
The parameter set is the stressed regime used in the hedging experiment in the main text:

|  |  |  |
| --- | --- | --- |
|  | (v0,κ,θ,σv,ρ,λ,μJ,σJ)=(0.04,3.0,0.04,1.0,−0.8,2.0,−0.05,0.20),(v\_{0},\kappa,\theta,\sigma\_{v},\rho,\lambda,\mu\_{J},\sigma\_{J})=(0.04,3.0,0.04,1.0,-0.8,2.0,-0.05,0.20), |  |

with r=1%r=1\% and q=0q=0.

Table 7: Pricing error of Black–Scholes and Merton relative to Bates SVJD benchmark prices, evaluated on a 164-point (x,τ)(x,\tau) grid. The second column reports RMSE on the core short-dated bucket (|x|<0.05,τ≤1/252)(|x|<0.05,\ \tau\leq 1/252) (92 grid points, including repeated endpoints).

| Model | Price RMSE (global) | Price RMSE (|x|<0.05,τ≤1/252)(|x|<0.05,\ \tau\leq 1/252) |
| --- | --- | --- |
| Black–Scholes | 0.000303 | 0.000297 |
| Merton | 0.000182 | 0.000121 |

Merton’s jump-diffusion substantially reduces pricing error relative to Black–Scholes (Table [7](#A1.T7 "Table 7 ‣ A.1 Black–Scholes and Merton vs a Bates benchmark ‣ Appendix A Model comparison ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")), indicating that even overnight options load on jump risk.

We also run a one-day discrete-time Δ\Delta hedge under simulated Bates dynamics (same setup as Section [5.5](#S5.SS5 "5.5 One-day delta-hedging ‣ 5 Numerical experiments ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps")) and compute hedge deltas using BS, Merton, and Bates.
Table [8](#A1.T8 "Table 8 ‣ A.1 Black–Scholes and Merton vs a Bates benchmark ‣ Appendix A Model comparison ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") reports summary statistics, both unconditionally and conditional on whether at least one jump occurs along the path.
Jump realisations dominate tail outcomes and cannot be hedged away by delta hedging; differences across delta models are therefore small relative to jump-driven tail risk in this setup.

Table 8: One-day discrete-time Δ\Delta-hedging P&L under simulated Bates dynamics. “jump” means the path contains at least one price jump during the day; “no-jump” means no price jump occurs. The last column reports a nonparametric 95% bootstrap CI for CVaR1%.

| Model | Subset | nn | mean | sd | q01 | CVaR01 [95% CI] |
| --- | --- | --- | --- | --- | --- | --- |
| BS | all | 30,000 | 0.000084 | 0.007247 | -0.001641 | -0.0339 [-0.042,-0.026] |
| BS | jump | 237 | -0.040952 | 0.070066 | -0.293528 | -0.3683 [-0.456,-0.251] |
| BS | no-jump | 29,763 | 0.000411 | 0.000568 | -0.001274 | -0.0020 [-0.0021,-0.0019] |
| Bates | all | 30,000 | 0.000075 | 0.007254 | -0.001728 | -0.0340 [-0.043,-0.026] |
| Bates | jump | 237 | -0.041152 | 0.069999 | -0.287896 | -0.3677 [-0.456,-0.248] |
| Bates | no-jump | 29,763 | 0.000403 | 0.000616 | -0.001473 | -0.0021 [-0.0021,-0.0020] |
| Merton | all | 30,000 | 0.000083 | 0.007238 | -0.001651 | -0.0339 [-0.042,-0.026] |
| Merton | jump | 237 | -0.040979 | 0.069925 | -0.292678 | -0.3680 [-0.456,-0.250] |
| Merton | no-jump | 29,763 | 0.000410 | 0.000574 | -0.001304 | -0.0020 [-0.0021,-0.0019] |

### A.2 SVCJ vs Bates: do volatility jumps matter for 0DTE?

To assess whether volatility jumps matter for 0DTE options, we consider an SVCJ extension (stochastic volatility with contemporaneous jumps in price and variance) in which price and variance jump simultaneously at Poisson times.
The log-price jump is Y∼𝒩​(μJ,σJ2)Y\sim\mathcal{N}(\mu\_{J},\sigma\_{J}^{2}) and the variance jump is Z∼Exp​(mean=μv​J)Z\sim\mathrm{Exp}(\text{mean}=\mu\_{vJ}), independent of YY but arriving with the same intensity λ\lambda [[Duffie et al.(2000)](#bib.bibx9)].
We set μv​J=0.02\mu\_{vJ}=0.02 (a positive variance-jump mean), and keep (v0,κ,θ,σv,ρ,λ,μJ,σJ)(v\_{0},\kappa,\theta,\sigma\_{v},\rho,\lambda,\mu\_{J},\sigma\_{J}) equal to the stressed regime above.
Table [9](#A1.T9 "Table 9 ‣ A.2 SVCJ vs Bates: do volatility jumps matter for 0DTE? ‣ Appendix A Model comparison ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") shows that the incremental pricing effect of adding variance jumps is small. For very short maturities, vega exposure is limited; variance jumps can therefore be weakly identified unless longer expiries are included in calibration/training.
The evaluation grid here uses four same-day maturity slices, τ∈{0.25,0.50,0.75,1.00}×(1/252)\tau\in\{0.25,0.50,0.75,1.00\}\times(1/252).
Accordingly, the metric “ATM” aggregates all grid points with |x|<0.1|x|<0.1 across all four slices, whereas “ATM+short” additionally imposes τ<1/252\tau<1/252, i.e. it retains only the first three slices.

Table 9: Incremental pricing effect of adding variance jumps, reported as the price difference CSVCJ−CBatesC^{\mathrm{SVCJ}}-C^{\mathrm{Bates}} and summarized by its RMSE over several evaluation subsets (μv​J=0.02\mu\_{vJ}=0.02). All metrics are evaluated on the same 164-point (x,τ)(x,\tau) grid.

| Metric | global | ATM | short | ATM+short |
| --- | --- | --- | --- | --- |
| Price RMSE | 3.16×10−73.16\times 10^{-7} | 3.47×10−73.47\times 10^{-7} | 1.93×10−71.93\times 10^{-7} | 2.11×10−72.11\times 10^{-7} |

We conduct the one-day delta-hedging under simulated SVCJ dynamics and compare hedges based on Bates vs SVCJ deltas. Table [10](#A1.T10 "Table 10 ‣ A.2 SVCJ vs Bates: do volatility jumps matter for 0DTE? ‣ Appendix A Model comparison ‣ Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps") shows that the P&L distributions are very similar at the reported precision.

Table 10: One-day Δ\Delta-hedging P&L under simulated SVCJ dynamics: summary statistics comparing deltas from Bates vs SVCJ (negative is profit). The last column reports a nonparametric 95% bootstrap CI for CVaR1%.

| Model | Subset | nn | mean | sd | q01 | CVaR01 [95% CI] |
| --- | --- | --- | --- | --- | --- | --- |
| Bates | all | 9,000 | -0.000316 | 0.012868 | -0.002961 | -0.0734 [-0.103,-0.054] |
| Bates | jump | 108 | -0.058557 | 0.101288 | -0.358808 | -0.4407 [-0.521,-0.301] |
| Bates | no-jump | 8,892 | 0.000392 | 0.001140 | -0.002165 | -0.0028 [-0.0029,-0.0026] |
| SVCJ | all | 9,000 | -0.000316 | 0.012868 | -0.002961 | -0.0734 [-0.101,-0.047] |
| SVCJ | jump | 108 | -0.058557 | 0.101288 | -0.358808 | -0.4407 [-0.521,-0.301] |
| SVCJ | no-jump | 8,892 | 0.000392 | 0.001140 | -0.002165 | -0.0028 [-0.0029,-0.0026] |

BETA