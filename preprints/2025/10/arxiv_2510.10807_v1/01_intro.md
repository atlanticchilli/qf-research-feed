---
authors:
- Ali Atiah Alzahrani
doc_id: arxiv:2510.10807v1
family_id: arxiv:2510.10807
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation
url_abs: http://arxiv.org/abs/2510.10807v1
url_html: https://arxiv.org/html/2510.10807v1
venue: arXiv q-fin
version: 1
year: 2025
---


Ali Atiah Alzahrani∗
  
Public Investment Fund (PIF)†

###### Abstract

We study whether regime-conditioned generative scenarios, coupled with a convex CVaR allocator, improve portfolio decisions under regime shifts. We introduce *Multi-Agent Regime-Conditioned Diffusion (MARCD)*, which (i) infers latent regimes via a Gaussian HMM, (ii) trains a diffusion model with a *tail-weighted* objective and a *regime-specialized MoE denoiser* to enrich crisis co-movements, and (iii) feeds the generated scenarios into a turnover-aware *CVaR epigraph QP* with explicit governance. In strict walk-forward tests on liquid multi-asset ETFs (2005–2025), MARCD outperforms standard allocators and improves calibration relative to popular generators. Over 2020–2025 out-of-sample (monthly; 10 bps), MARCD attains *Sharpe* 1.23 (BL 1.02) and *MaxDD* 9.3% (BL 14.1%), a 34% reduction, at comparable turnover; stationary block-bootstrap intervals indicate the Sharpe uplift is significant at 5%. We provide theory linking tail-weighted diffusion to *spectral-risk control* of the decision-relevant CVaR gap, *oracle/consistency* results for the regime-MoE denoiser, and *Lipschitz/Regret* guarantees for the allocator. Together, MARCD offers a reproducible bridge from *tail-faithful scenario modeling* to *governed portfolio decisions* with materially improved drawdown control.

††footnotetext: 
∗Corresponding author: alialzahrani@pif.gov.sa
  
†The views expressed are those of the author and do not necessarily reflect the views
of the Public Investment Fund. This material is for research purposes only and
does not constitute investment advice.


Market data
(prices, factors)

Regime inference
(HMM / filters)

Regime-conditioned
diffusion generator
Tail-weighted loss (q,η)(q,\eta); Regime-MoE (gate gtg\_{t})

Signal extraction
(risk/alpha features)
Blend λ\lambda: (μ^t,Σ^t)(\hat{\mu}\_{t},\hat{\Sigma}\_{t}); shrinkage

Allocation
(CVaR-QP, α=0.95\alpha{=}0.95)
box & turnover cap τ\tau;  optional +κ​‖Δ​w‖1+\kappa\|\Delta w\|\_{1}

Backtest
metrics
NN scenarios(μ^t,Σ^t)(\hat{\mu}\_{t},\hat{\Sigma}\_{t})trades, P&Lregime posteriors 𝝅t\boldsymbol{\pi}\_{t}ScenarioSignalAllocation

Figure 1: Multi-Agent Regime-Conditioned Diffusion (MARCD).

## 1 Introduction

Financial returns are non-stationary, with abrupt regime changes (e.g., 2008, 2020, 2022) that challenge mean–variance optimization (MVO) (Markowitz, [1952](https://arxiv.org/html/2510.10807v1#bib.bib15)) and Black–Litterman (BL) (Black and Litterman, [1992](https://arxiv.org/html/2510.10807v1#bib.bib3)). Modern generative models—GANs (Yoon et al., [2019](https://arxiv.org/html/2510.10807v1#bib.bib20)), diffusion (Rasul et al., [2021](https://arxiv.org/html/2510.10807v1#bib.bib16)), transformers (Zhou et al., [2023](https://arxiv.org/html/2510.10807v1#bib.bib21))—produce realistic sequences but are often unconditioned and decoupled from decisions. Large peak-to-trough losses are driven by left-tail co-movements that standard diffusion training (MSE) tends to underweight, and a single denoiser blurred across regimes can dilute crisis dynamics.

We refer to our method as *Multi-Agent Regime-Conditioned Diffusion (MARCD)* and use MARCD thereafter. MARCD aligns a diffusion generator to HMM posteriors while explicitly improving tail fidelity and crisis behavior: we employ a *tail-weighted* diffusion objective to emphasize adverse outcomes that govern realized drawdowns, and we augment the denoiser with a lightweight *regime expert* (mixture-of-experts) whose gate increases with the crisis posterior, enriching co-crash structure without degrading calm-regime fit. Generated scenarios feed a CVaR-focused, turnover-aware allocator within an auditable, walk-forward protocol.

Contributions. We integrate regime modeling, tail-aware generation, and robust allocation: (i) regime-conditioned diffusion aligned to HMM posteriors with a tail-weighted training objective that improves left-tail dependence; (ii) a regime-aware expert denoiser (MoE) that specializes to high-volatility states via learned gating; (iii) a multi-agent pipeline translating samples to decisions; and (iv) a CVaR-focused allocation with turnover control and explicit governance (walk-forward, constraints).

## 2 Related Work

Regimes. HMMs capture structural breaks and state dependence (Hamilton, [1989](https://arxiv.org/html/2510.10807v1#bib.bib7); Kim and Nelson, [1994](https://arxiv.org/html/2510.10807v1#bib.bib10); Ang and Timmermann, [2012](https://arxiv.org/html/2510.10807v1#bib.bib1)); we use their posteriors as conditioning signals for both generation and allocation. Generative time series. GAN- and VAE-based generators (e.g., TimeGAN and TimeVAE) and diffusion models improve realism and calibration (Yoon et al., [2019](https://arxiv.org/html/2510.10807v1#bib.bib20); Desai et al., [2021](https://arxiv.org/html/2510.10807v1#bib.bib5); Rasul et al., [2021](https://arxiv.org/html/2510.10807v1#bib.bib16); Tashiro et al., [2021](https://arxiv.org/html/2510.10807v1#bib.bib19)), yet are often unconditioned and loosely coupled to portfolio decisions; recent TS diffusions (*TSDiff*, *mr-Diff*) and a finance simulator (*CTS-GAN*) are complementary to our regime-conditioned, decision-tied approach (Kollovieh et al., [2023](https://arxiv.org/html/2510.10807v1#bib.bib11); Shen et al., [2024](https://arxiv.org/html/2510.10807v1#bib.bib18); Istiaque et al., [2024](https://arxiv.org/html/2510.10807v1#bib.bib9)). Robust portfolios. Distributionally robust and CVaR formulations address fat tails (Delage and Ye, [2010](https://arxiv.org/html/2510.10807v1#bib.bib4); Rockafellar and Uryasev, [2000](https://arxiv.org/html/2510.10807v1#bib.bib17)) but hinge on scenario quality; we feed a regime-conditioned set into a convex allocator. Multi-agent. Building on coordination frameworks (Lowe et al., [2017](https://arxiv.org/html/2510.10807v1#bib.bib14)), we orchestrate Scenario→\toSignal→\toAllocation with light, role-based agents. Sequence models. LSTMs (Hochreiter and Schmidhuber, [1997](https://arxiv.org/html/2510.10807v1#bib.bib8); Fischer and Krauss, [2018](https://arxiv.org/html/2510.10807v1#bib.bib6)), TCNs (Bai et al., [2018](https://arxiv.org/html/2510.10807v1#bib.bib2)), and Transformers (Lim et al., [2021](https://arxiv.org/html/2510.10807v1#bib.bib13)) remain standard forecasters; we treat point-forecast models as standard baselines, focusing instead on regime-conditioned *distributional* generation wired to a convex CVaR allocator under strict walk-forward evaluation.

## 3 Methodology

Setup.
At rebalancing date tt, let 𝐑t∈ℝd\mathbf{R}\_{t}\in\mathbb{R}^{d} denote the observed return vector and 𝐰t∈ℝd\mathbf{w}\_{t}\in\mathbb{R}^{d} the portfolio weights, which satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏⊤​𝐰t=1,ℓ≤𝐰t≤𝒖.\mathbf{1}^{\top}\mathbf{w}\_{t}=1,\qquad\boldsymbol{\ell}\leq\mathbf{w}\_{t}\leq\boldsymbol{u}. |  | (1) |

Market regimes are modeled by a KK-state Gaussian HMM with latent state StS\_{t} and posterior vector 𝝅t\boldsymbol{\pi}\_{t}, where πt,k=P​(St=k∣𝐑1:t)\pi\_{t,k}=P(S\_{t}{=}k\mid\mathbf{R}\_{1:t}). The generator produces NN next-period scenarios {𝐫t+1(i)}i=1N\{\mathbf{r}^{(i)}\_{t+1}\}\_{i=1}^{N}. Turnover is τt=‖𝐰t−𝐰t−1‖1\tau\_{t}=\|\mathbf{w}\_{t}-\mathbf{w}\_{t-1}\|\_{1}. To avoid notation overload, we reserve αs\alpha\_{s} for the diffusion schedule and α\alpha for the allocator’s CVaR level, use λ\lambda for scenario blending, and λμ\lambda\_{\mu} for the expected-return weight in the allocator.

### 3.1 Method Overview and Rationale

Our objective is to reduce pathwise drawdowns while preserving risk-adjusted return under strict walk-forward governance. We posit that returns exhibit regime-dependent higher-order dependence and that left-tail comovements matter more for realized drawdowns than central calibration. Accordingly, we bias generation toward adverse outcomes, make the generator responsive to regime signals, and align the allocator with tail-focused yet convex objectives that remain auditable and turnover-aware. Concretely, this yields a tail-weighted diffusion objective to improve co-crash fidelity, a regime-aware denoiser that specializes to high-volatility episodes, and a spectral CVaR allocator with a simple regime-adaptive risk throttle.

Core training setup.
UNet (8 stages, base ch.=64), cosine noise schedule, ϵ\epsilon-prediction, EMA=0.999=0.999;
AdamW 1​e−41\mathrm{e}{-4}; batch 256256; 250250k steps; seed 20202020.

### 3.2 Regime Detection (strict walk-forward)

We fit/update a KK-state Gaussian HMM on {𝐑s}s≤t\{\mathbf{R}\_{s}\}\_{s\leq t} and extract posteriors πt,k=P​(St=k∣𝐑1:t)\pi\_{t,k}=P(S\_{t}{=}k\mid\mathbf{R}\_{1:t}).
Conditioning features 𝒛t\boldsymbol{z}\_{t} encode regime context (e.g., arg⁡maxk⁡πt,k\arg\max\_{k}\pi\_{t,k} and recent statistics). All estimation is strict walk-forward: only data up to tt is used; HMM parameters refresh on a rolling window.

### 3.3 Regime-Conditioned Diffusion

We train a variance-preserving diffusion model to denoise 𝐱s\mathbf{x}\_{s} with regime context 𝒛t\boldsymbol{z}\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | q​(𝐱s∣𝐱0)=𝒩​(αs​𝐱0,(1−αs)​𝐈),ℒdiff=𝔼​‖ϵ−ϵθ​(αs​𝐱0+1−αs​ϵ,s,𝒛t)‖2.\displaystyle q(\mathbf{x}\_{s}\mid\mathbf{x}\_{0})=\mathcal{N}\!\big(\sqrt{\alpha\_{s}}\mathbf{x}\_{0},(1{-}\alpha\_{s})\mathbf{I}\big),\quad\mathcal{L}\_{\text{diff}}=\mathbb{E}\big\|\boldsymbol{\epsilon}-\boldsymbol{\epsilon}\_{\theta}(\sqrt{\alpha\_{s}}\mathbf{x}\_{0}+\sqrt{1{-}\alpha\_{s}}\boldsymbol{\epsilon},s,\boldsymbol{z}\_{t})\big\|^{2}. |  | (2) |

*Implementation.* We use a conditional DDPM with a UNet-style denoiser (4 down/4 up blocks), a cosine noise schedule, exponential moving average (EMA) of weights, and ≈\approx1–2M parameters; conditioning is via the regime embedding 𝒛t\boldsymbol{z}\_{t} injected at each block.

At deployment time tt we sample NN returns {𝐫t+1(i)}\{\mathbf{r}^{(i)}\_{t+1}\} conditioned on 𝒛t\boldsymbol{z}\_{t}. The Signal Agent forms blended moments

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝁^t=λ​𝝁synth+(1−λ)​𝝁hist,𝚺^t=λ​𝚺synth+(1−λ)​𝚺hist.\displaystyle\hat{\boldsymbol{\mu}}\_{t}=\lambda\,\boldsymbol{\mu}\_{\text{synth}}+(1{-}\lambda)\boldsymbol{\mu}\_{\text{hist}},\qquad\hat{\boldsymbol{\Sigma}}\_{t}=\lambda\,\boldsymbol{\Sigma}\_{\text{synth}}+(1{-}\lambda)\boldsymbol{\Sigma}\_{\text{hist}}. |  | (3) |

### 3.4 Allocation Agent: CVaR Epigraph Program and Properties

Define per-scenario loss ℓi=−𝐰⊤​𝐫t+1(i)\ell\_{i}=-\,\mathbf{w}^{\top}\mathbf{r}^{(i)}\_{t+1}. We solve the convex program

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | min𝐰,ζ,{si}\displaystyle\min\_{\mathbf{w},\,\zeta,\,\{s\_{i}\}}\; | −λμ​𝝁^t⊤​𝐰+γ​𝐰⊤​𝚺^t​𝐰+ζ+1(1−α)​N​∑i=1Nsi\displaystyle-\lambda\_{\mu}\,\hat{\boldsymbol{\mu}}\_{t}^{\top}\mathbf{w}+\gamma\,\mathbf{w}^{\top}\hat{\boldsymbol{\Sigma}}\_{t}\mathbf{w}+\zeta+\frac{1}{(1-\alpha)N}\sum\_{i=1}^{N}s\_{i} |  | (4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | s.t. | si≥0,si≥ℓi−ζ,i=1,…,N,\displaystyle s\_{i}\geq 0,\;s\_{i}\geq\ell\_{i}-\zeta,\;i=1,\dots,N, |  | (5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝟏⊤​𝐰=1,ℓ≤𝐰≤𝐮box,‖𝐰−𝐰t−1‖1≤τ.\displaystyle\mathbf{1}^{\top}\mathbf{w}=1,\;\;\boldsymbol{\ell}\leq\mathbf{w}\leq\mathbf{u}^{\text{box}},\;\;\|\mathbf{w}-\mathbf{w}\_{t-1}\|\_{1}\leq\tau. |  | (6) |

When used, we add a turnover penalty +κ​‖𝐰−𝐰t−1‖1+\kappa\|\mathbf{w}-\mathbf{w}\_{t-1}\|\_{1}.

Convexity/complexity. The objective combines a quadratic term 𝐰⊤​𝚺^t​𝐰\mathbf{w}^{\top}\hat{\boldsymbol{\Sigma}}\_{t}\mathbf{w} with the convex CVaR epigraph; constraints are affine, yielding a QP with O​(N)O(N) linear epigraph constraints. For d=10d{=}10 and N=1024N{=}1024, interior-point methods scale as O​(d3+N​d2)O(d^{3}+Nd^{2}) and run fast on commodity CPUs. Unless stated otherwise, the CVaR level is α=0.95\alpha{=}0.95. We shrink 𝚺^t\hat{\boldsymbol{\Sigma}}\_{t} toward the identity to obtain a well-conditioned covariance matrix (Ledoit and Wolf, [2004](https://arxiv.org/html/2510.10807v1#bib.bib12)).

#### Note.

We use the standard Rockafellar–Uryasev CVaR at level α\alpha in all experiments; spectral risk measures are left to future work.

> Governance & Auditability.
> The allocator’s KKT system (App. A.3) logs active constraints, tail weights,
> and duals at each rebalance. This yields solver-side audit trails linking regime
> posteriors and tail emphasis to realized trades—important for model risk and compliance.

Algorithm 1  Walk-forward regime-conditioned decision pipeline

0:  assets dd, states KK, scenarios NN, CVaR level α\alpha, bounds (ℓ,𝒖)(\boldsymbol{\ell},\boldsymbol{u}), turnover cap τ\tau, blend λ\lambda, regs (γ,λμ)(\gamma,\lambda\_{\mu})

1:  Initialize 𝐰t0\mathbf{w}\_{t\_{0}} (e.g., equal-weight)

2:  for t=t0,…,tendt=t\_{0},\dots,t\_{\text{end}} do

3:   Regime update: fit/update HMM on {𝐑s}s≤t\{\mathbf{R}\_{s}\}\_{s\leq t}; compute πt,⋅\pi\_{t,\cdot} and 𝒛t\boldsymbol{z}\_{t}

4:   Scenario gen: draw {𝐫t+1(i)}i=1N∼pθ(⋅∣𝒛t)\{\mathbf{r}^{(i)}\_{t+1}\}\_{i=1}^{N}\sim p\_{\theta}(\cdot\mid\boldsymbol{z}\_{t})

5:   Signals: form (𝝁^t,𝚺^t)(\hat{\boldsymbol{\mu}}\_{t},\hat{\boldsymbol{\Sigma}}\_{t}) via blending with weight λ\lambda

6:   Allocation: solve (4) for 𝐰t\mathbf{w}\_{t} with (ℓ,𝒖,τ)(\boldsymbol{\ell},\boldsymbol{u},\tau); optionally include cost penalty κ​‖𝐰t−𝐰t−1‖1\kappa\|\mathbf{w}\_{t}{-}\mathbf{w}\_{t-1}\|\_{1}

7:   Trade from 𝐰t−1\mathbf{w}\_{t-1} to 𝐰t\mathbf{w}\_{t}; record turnover; log diagnostics for auditability

8:  end for

### 3.5 Tail-Weighted Diffusion Loss

We avoid target leakage by using a *portfolio-free* proxy for adverse outcomes during training. Define the worst single-asset one-step loss
ℓ~=−minj⁡rj\tilde{\ell}=-\min\_{j}r\_{j} and reweight errors when ℓ~\tilde{\ell} falls in its lower qq-quantile:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒtail=𝔼​[(1+η​ 1​{ℓ~≤Qq​(ℓ~)})​‖𝜺−𝜺θ​(⋅)‖22],q∈[0.05,0.10],η∈[1,3].\mathcal{L}\_{\text{tail}}=\mathbb{E}\!\left[\bigl(1+\eta\,\mathbf{1}\{\tilde{\ell}\leq Q\_{q}(\tilde{\ell})\}\bigr)\,\|\boldsymbol{\varepsilon}-\boldsymbol{\varepsilon}\_{\theta}(\cdot)\|\_{2}^{2}\right],\qquad q\!\in\![0.05,0.10],~\eta\!\in\![1,3]. |  | (7) |

At deployment (allocation), portfolio losses use ℓ=−𝐰⊤​𝐫\ell=-\mathbf{w}^{\top}\mathbf{r} only for evaluation/diagnostics.

### 3.6 Regime-MoE Denoiser

We instantiate a two-expert denoiser with a crisis head specialized to high-volatility regimes.
A gate gt=σ​(MLP​(𝐳t))g\_{t}=\sigma(\mathrm{MLP}(\mathbf{z}\_{t})) mixes experts:
ϵ^θ=(1−gt)​ϵ^θbase+gt​ϵ^θcrisis\hat{\epsilon}\_{\theta}=(1-g\_{t})\,\hat{\epsilon}^{\text{base}}\_{\theta}+g\_{t}\,\hat{\epsilon}^{\text{crisis}}\_{\theta}.
At sampling, gtg\_{t} increases with the HMM crisis posterior, enriching co-crash structure.

### 3.7 Theory Highlights

Takeaways (statements; proofs in App. A).

###### Theorem 1 (Spectral CVaR Control by Tail-Weighted Diffusion; App. A.11).

Minimizing LtailL\_{\text{tail}} in Eq. (7) controls a spectral-risk upper bound on the
*decision-relevant* CVaR generalization gap for any feasible portfolio ww,
scaling with (1−α)−1(1-\alpha)^{-1} and the denoising error on the lower-qq tail.

###### Theorem 2 (MoE Oracle, Consistency & Stability; App. A.13).

With a gate monotone in the HMM crisis posterior (Sec. 3.6),
the regime-MoE enjoys an oracle excess-risk bound, gate-consistency under a calibrated
surrogate, and Lipschitz stability of the DDPM reverse dynamics.

###### Theorem 3 (Allocator Lipschitzness & Regret; App. A.14).

The CVaR epigraph QP (Sec. 3.4) has a Lipschitz solution map in (μ,Σ)(\mu,\Sigma) and
admits a decision-regret bound under moment and CVaR perturbations; the CVaR error
term shrinks with LtailL\_{\text{tail}}.

## 4 Experimental setup

Assets & horizon. Ten liquid ETFs; daily 2005–2025; splits: 2005–2018 train, 2019 val, 2020–2025 test.
Data. Daily total returns computed from Yahoo Finance *Adjusted Close* (dividends included).
Baselines. EW, RP, BL; monthly rebal.; 10 bps costs (identical across methods). Allocator parity.
All strategies (EW, RP, BL, MARCD) rebalance monthly on the last trading day, incur identical transaction costs of 10 bps per trade, and are subject to the same turnover controls
(an ℓ1\ell\_{1} cap ‖𝐰t−𝐰t−1‖1≤0.20\|\mathbf{w}\_{t}{-}\mathbf{w}\_{t-1}\|\_{1}\!\leq\!0.20; no penalty, κ=0\kappa{=}0, unless stated otherwise),
as well as the same box and leverage constraints. Baselines form their *unconstrained* targets (EW, RP equal risk contributions, BL no-views prior anchored to a cap-weighted market proxy with standard τ\tau (confidence) and 𝛀\boldsymbol{\Omega} (uncertainty) settings) and then apply the *same partial-rebalance projection* toward target under the ℓ1\ell\_{1} cap.
Diagnostics. KS, ES, VS; LB p​(|r|)p(|r|); VaR0.95 unconditional coverage (Kupiec UC) pp; CVaR0.95 error ( bps). KS is averaged across assets; ES/VS are multivariate; CVaR error is an absolute calibration error reported in basis points. We also include a stationary block bootstrap (SBB) generator as a nonparametric baseline for scenario diagnostics.
Metrics. Return=CAGR; rf=0; 252-day annualization; Sortino uses downside dev. to 0%; Calmar=Return/|MaxDD||\mathrm{MaxDD}|.
Protocol. Strict walk-forward; HMM 3y rolling; scenarios conditioned on 𝒛t\boldsymbol{z}\_{t}; CVaR-QP allocation.

## 5 Results and discussion

Diagnostics— All results use *monthly* rebalancing on the last trading day, 10 bps trading cost, and the metric conventions above. Under strict walk-forward (2020–2025), MARCD shows stronger scenario calibration (↓KS/ES/VS; LB/UC pp competitive, slightly below TimeVAE). See Table [1](https://arxiv.org/html/2510.10807v1#S5.T1 "Table 1 ‣ 5 Results and discussion ‣ Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation").

Performance— MARCD attains higher risk-adjusted performance (Sharpe 1.23 vs. 1.02 for BL) with materially smaller drawdowns. Summary metrics are reported in Table [2](https://arxiv.org/html/2510.10807v1#S5.T2 "Table 2 ‣ 5 Results and discussion ‣ Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation"), and trajectories are visualized in Figure [2](https://arxiv.org/html/2510.10807v1#S5.F2 "Figure 2 ‣ 5 Results and discussion ‣ Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation"). Over 2020–2025 OOS, MaxDD is 9.3% for MARCD vs BL 14.1% and EW 21.2% (34%/56% lower; absolute 4.8%/11.9%). Consistent with this, Calmar improves to 1.11 (BL 0.70; EW 0.38). A stationary block bootstrap (B=1000B{=}1000, block =20=20) indicates MARCD’s Sharpe exceeds BL/EW (two-sided p<0.05p{<}0.05); CVaR0.95\mathrm{CVaR}\_{0.95} and MaxDD also improve at similar turnover. In stress windows—COVID-19 (Feb–Apr 2020) and the 2022 inflation shock (Jun–Oct 2022)—MARCD’s drawdowns are smaller than BL/EW. Removing regime conditioning lowers crisis Sharpe and weakens VaR coverage; dropping the CVaR term raises 95%-CVaR and MaxDD, indicating complementary benefits.

Table 1: OOS scenario diagnostics. Lower is better (↓) except pp (↑); LB on |r||r|. Abbrev.: SBB=Stationary block bootstrap; TGAN=TimeGAN.

| Model | KS↓\downarrow | ES↓\downarrow | VS↓\downarrow | LB p​(|r|)↑p(|r|)\uparrow | VaR0.95 UC p↑p\uparrow | CVaR0.95 err (bps)↓\downarrow |
| --- | --- | --- | --- | --- | --- | --- |
| SBB | 0.196 | 0.358 | 0.329 | 0.22 | 0.11 | 39 |
| TGAN | 0.182 | 0.341 | 0.312 | 0.28 | 0.16 | 33 |
| TimeVAE | 0.159 | 0.305 | 0.268 | 0.52 | 0.63 | 17 |
| MARCD | 0.154 | 0.289 | 0.247 | 0.50 | 0.58 | 15 |

![Refer to caption](pic.png)


Figure 2: OOS cumulative NAV, drawdown, and HMM regime posteriors (K=3K{=}3).

Sensitivity & robustness— Results are stable across blend weights λ∈[0.3,0.7]\lambda\!\in\![0.3,0.7] and CVaR trade-off γ∈[0.5,1.5]\gamma\!\in\![0.5,1.5]; MARCD maintains Sharpe above BL and lower MaxDD at similar turnover. Performance remains robust under modest transaction-cost stress (e.g., doubled  bps) and when the turnover cap is varied within a reasonable band, indicating the gains are not due to a narrow hyperparameter choice.

Table 2: Out-of-sample performance (2020–2025; monthly rebal.; annualized; net of 10 bps). Higher is better (↑) except Vol and MaxDD (↓). MaxDD is reported as a positive magnitude.

| Strategy | Return %↑\uparrow | Vol %↓\downarrow | Sharpe↑\uparrow | Sortino↑\uparrow | MaxDD %↓\downarrow | Calmar↑\uparrow |
| --- | --- | --- | --- | --- | --- | --- |
| EW | 8.1 | 11.2 | 0.72 | 1.09 | 21.2 | 0.38 |
| RP | 7.6 | 8.6 | 0.88 | 1.37 | 14.9 | 0.51 |
| BL | 9.9 | 9.7 | 1.02 | 1.50 | 14.1 | 0.70 |
| MARCD | 10.3 | 8.4 | 1.23 | 1.69 | 9.3 | 1.11 |

## 6 Ablations and Component Analyses

Summary. Removing either *regime conditioning* or the *CVaR term* weakens tail control and calibration, and pushing the blend to the extremes (λ=0\lambda{=}0 or 11) underperforms the base mix. Concretely, Table [3](https://arxiv.org/html/2510.10807v1#S6.T3 "Table 3 ‣ 6 Ablations and Component Analyses ‣ Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation") shows Sharpe falling from 1.23 (base) to 1.12\mathbf{1.12}–1.13\mathbf{1.13} for all ablations, while MaxDD rises from 9.3% to 11.3% (uncond. diffusion), 14.6% (no CVaR), 12.1% (λ=0\lambda{=}0), and 12.8% (λ=1\lambda{=}1)—i.e., +2.0%–5.3% absolute (+21–57% relative). Calibration also degrades: the VaR0.95 UC pp drops from 0.58 to 0.490.49, 0.460.46, 0.520.52, and 0.480.48, and the CVaR0.95\mathrm{CVaR}\_{0.95} error increases from 15 to 2222, 2727, 2121, and 2424, respectively. Volatility rises (8.4→\rightarrow8.6–9.1) and returns slip (10.3→\rightarrow9.7–10.1), while turnover remains similar (15.3–15.9%). Overall, MARCD (base) is strongest across risk/return and tail-calibration columns; Figure [3](https://arxiv.org/html/2510.10807v1#S6.F3 "Figure 3 ‣ 6 Ablations and Component Analyses ‣ Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation") visualizes these degradations in both performance and diagnostics.

Table 3: Ablations (OOS 2020–2025; annualized; net 10 bps). Higher is better except Vol, MaxDD.

Variant
Return %↑
Vol %↓
Sharpe↑
MaxDD %↓
VaR0.95 UC pp↑
CVaR0.95 err↓
Turnover %


MARCD (base)
10.3
8.4
1.23
9.3
0.58
15
15.8

Uncond. diffusion
9.8
8.7
1.13
11.3
0.49
22
15.4

No CVaR term
10.1
9.1
1.12
14.6
0.46
27
15.6

λ=0.0\lambda{=}0.0
9.7
8.6
1.13
12.1
0.52
21
15.3

λ=1.0\lambda{=}1.0
9.9
8.8
1.12
12.8
0.48
24
15.9

![Refer to caption](ablations.png)


Figure 3: Ablations—performance and diagnostic metrics across variants (OOS 2020–2025).

## 7 Sensitivity Studies

Summary. One-parameter sweeps over K,α,λ,τK,\alpha,\lambda,\tau show stable realism (KS/ES/VS) and calibration (pp-values ≈0.5\approx 0.5–0.60.6), with K=3K{=}3 and α=0.95\alpha{=}0.95 typically strongest. Diagnostics remain tight across settings in Table [4](https://arxiv.org/html/2510.10807v1#S7.T4 "Table 4 ‣ 7 Sensitivity Studies ‣ Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation"), while predictable risk–return trade-offs appear in Table [5](https://arxiv.org/html/2510.10807v1#S7.T5 "Table 5 ‣ 7 Sensitivity Studies ‣ Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation") (e.g., higher α\alpha lowers Vol/MaxDD with modest Sharpe changes; turnover responds primarily to τ\tau). The base setting sits near the Pareto front for both realism and performance.

Table 4: Diagnostics under parameter sweeps (OOS 2020–2025). Lower is better (↓) except pp (↑).

| Parameter | Value | KS↓ | ES↓ | VS↓ | LB p​(|r|)p(|r|)↑ | VaR0.95 UC pp↑ |
| --- | --- | --- | --- | --- | --- | --- |
| Base | – | 0.154 | 0.289 | 0.247 | 0.50 | 0.58 |
| KK | 2 | 0.156 | 0.295 | 0.251 | 0.46 | 0.54 |
| KK | 3 | 0.154 | 0.289 | 0.247 | 0.50 | 0.58 |
| KK | 4 | 0.160 | 0.292 | 0.249 | 0.49 | 0.59 |
| α\alpha | 0.90 | 0.157 | 0.293 | 0.251 | 0.48 | 0.55 |
| α\alpha | 0.95 | 0.154 | 0.289 | 0.247 | 0.50 | 0.58 |
| α\alpha | 0.99 | 0.159 | 0.292 | 0.248 | 0.51 | 0.61 |
| λ\lambda | 0.30 | 0.156 | 0.291 | 0.248 | 0.49 | 0.57 |
| λ\lambda | 0.50 | 0.154 | 0.289 | 0.247 | 0.50 | 0.58 |
| λ\lambda | 0.70 | 0.155 | 0.289 | 0.248 | 0.49 | 0.58 |
| τ\tau | 0.10 | 0.156 | 0.290 | 0.248 | 0.50 | 0.58 |
| τ\tau | 0.20 | 0.154 | 0.289 | 0.247 | 0.50 | 0.58 |




Table 5: Performance under parameter sweeps (annualized; net 10 bps).

| Parameter | Value | Return %↑ | Vol %↓ | Sharpe↑ | MaxDD %↓ | Turnover % |
| --- | --- | --- | --- | --- | --- | --- |
| Base | – | 10.3 | 8.4 | 1.23 | 9.3 | 15.8 |
| KK | 2 | 9.9 | 8.6 | 1.15 | 11.8 | 9.3 |
| KK | 4 | 10.1 | 8.5 | 1.19 | 11.2 | 11.2 |
| α\alpha | 0.90 | 10.6 | 9.2 | 1.15 | 11.4 | 16.0 |
| α\alpha | 0.99 | 9.7 | 7.8 | 1.19 | 10.0 | 15.2 |
| λ\lambda | 0.30 | 10.1 | 8.5 | 1.19 | 11.3 | 15.4 |
| λ\lambda | 0.70 | 10.2 | 8.6 | 1.18 | 11.5 | 16.1 |
| τ\tau | 0.10 | 10.0 | 8.3 | 1.20 | 11.1 | 10.2 |
| τ\tau | 0.30 | 10.5 | 8.6 | 1.22 | 11.0 | 21.7 |

## 8 Model Selection and Significance

Summary. Rolling BIC favors K=3K{=}3 and this choice attains the best OOS Sharpe with competitive MaxDD and VaR coverage. Table [6](https://arxiv.org/html/2510.10807v1#S8.T6 "Table 6 ‣ 8 Model Selection and Significance ‣ Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation") reports the BIC deltas alongside OOS outcomes across K∈{2,3,4}K\in\{2,3,4\}. Stationary block-bootstrap intervals (Table [7](https://arxiv.org/html/2510.10807v1#S8.T7 "Table 7 ‣ 8 Model Selection and Significance ‣ Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation")) indicate MARCD’s Sharpe uplift versus EW/BL/RP is significant at the 5% level.

Table 6: HMM selection (rolling BIC) and OOS outcomes (2020–2025).

| KK | Δ\DeltaBIC (vs. 3) | Sharpe↑ | MaxDD %↓ | VaR0.95 UC pp↑ |
| --- | --- | --- | --- | --- |
| 2 | +18+18 | 1.15 | 11.8 | 0.54 |
| 3 | 0 | 1.23 | 9.3 | 0.58 |
| 4 | +9+9 | 1.19 | 11.2 | 0.59 |




Table 7: Sharpe uplift Δ\Delta (MARCD −- baseline), 95% CIs (OOS 2020–2025).

| Baseline | Δ\Delta | 95% CI |
| --- | --- | --- |
| EW | 0.510.51 | [0.31, 0.71][0.31,\;0.71] |
| BL | 0.210.21 | [0.07, 0.35][0.07,\;0.35] |
| RP | 0.350.35 | [0.18, 0.51][0.18,\;0.51] |

## 9 Application Profiles (overview)

Summary. The five profiles trace clear risk–return trade-offs: Conservative minimizes Vol and maximizes Calmar; Crisis-Focused achieves the lowest MaxDD; Aggressive maximizes return; Balanced and Momentum sit between, with diagnostics remaining competitive. Figure [4](https://arxiv.org/html/2510.10807v1#S9.F4 "Figure 4 ‣ 9 Application Profiles (overview) ‣ Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation") summarizes profile-level performance and diagnostics to facilitate side-by-side comparison.

![Refer to caption](profiles.png)


Figure 4: Profiles—performance and diagnostics summary (OOS 2020–2025).

## 10 Conclusion

We presented MARCD, a regime-conditioned generative-to-decision pipeline that couples an HMM-aligned diffusion generator with a CVaR-focused, turnover-aware allocator under strict walk-forward governance. Two additions—a *tail-weighted* diffusion objective and a *regime expert* (MoE) denoiser—improve left-tail co-movements and crisis fidelity in the scenarios. Empirically (OOS 2020–2025; monthly; net 10 bps), these changes *reduce MaxDD by 34.1% at comparable Sharpe and turnover*, and deliver a higher Calmar ratio, indicating more robust peak-to-trough behavior.

*Limitations.* Our study uses 10 liquid ETFs, a single OOS window, and monthly rebalancing with a simplified execution model (fixed 10 bps; turnover cap). Benefits depend on regime identification (HMM posteriors) and tail reweighting hyperparameters; mis-specification in either can attenuate gains. Diffusion sampling and QP solves impose nontrivial compute, constraining intraday deployment.

*Future work.* (i) Decision-aware training (end-to-end) that differentiates through spectral CVaR, turnover, and holdings penalties; (ii) short multi-step scenario generation with a convex *pathwise drawdown CVaR* objective; (iii) distributional robustness (e.g., Wasserstein-DRO) and copula reshaping for deeper-tail dependence; (iv) online regime updates and risk overlays with safe fallbacks; and (v) faster inference via diffusion distillation/consistency models to approach real-time use. Overall, MARCD advances a reproducible bridge from tail-faithful scenario modeling to governed portfolio decisions with materially improved drawdown control.

## References

* Ang and Timmermann [2012]

  Andrew Ang and Allan Timmermann.
  Regime shifts in financial markets.
  In *Handbook of Financial Econometrics*, pages 287–339. Elsevier, 2012.
* Bai et al. [2018]

  Shaojie Bai, J. Zico Kolter, and Vladlen Koltun.
  An empirical evaluation of generic convolutional and recurrent networks for sequence modeling.
  *arXiv preprint arXiv:1803.01271*, 2018.
* Black and Litterman [1992]

  Fischer Black and Robert Litterman.
  Global portfolio optimization.
  *Financial Analysts Journal*, 48(5):28–43, 1992.
* Delage and Ye [2010]

  Erick Delage and Yinyu Ye.
  Distributionally robust optimization under moment uncertainty with application to data-driven problems.
  *Operations Research*, 58(3):595–612, 2010.
* Desai et al. [2021]

  Abhyuday Desai, Cynthia Freeman, Zuhui Wang, and Ian Beaver.
  Timevae: A variational auto-encoder for multivariate time series generation.
  *arXiv preprint arXiv:2111.08095*, 2021.
  URL <https://arxiv.org/abs/2111.08095>.
* Fischer and Krauss [2018]

  Thomas Fischer and Christopher Krauss.
  Deep learning with long short-term memory networks for financial market predictions.
  *European Journal of Operational Research*, 270(2):654–669, 2018.
* Hamilton [1989]

  James D Hamilton.
  A new approach to the economic analysis of nonstationary time series and the business cycle.
  *Econometrica*, 57(2):357–384, 1989.
* Hochreiter and Schmidhuber [1997]

  Sepp Hochreiter and Jürgen Schmidhuber.
  Long short-term memory.
  *Neural Computation*, 9(8):1735–1780, 1997.
  doi: 10.1162/neco.1997.9.8.1735.
* Istiaque et al. [2024]

  Riasat Ali Istiaque, Chi Seng Pun, and Yuli Song.
  Simulating asset prices using conditional time-series gan.
  In *Proceedings of the 5th ACM International Conference on AI in Finance (ICAIF ’24)*. ACM, 2024.
  doi: 10.1145/3677052.3698638.
* Kim and Nelson [1994]

  Chang-Jin Kim and Charles R Nelson.
  Dynamic linear models with markov-switching.
  *Journal of Econometrics*, 60(1-2):1–22, 1994.
* Kollovieh et al. [2023]

  Marcel Kollovieh, Abdul Fatir Ansari, Michael Bohlke-Schneider, Jasper Zschiegner, Hao Wang, and Yuyang Wang.
  Predict, refine, synthesize: Self-guiding diffusion models for probabilistic time series.
  In *Advances in Neural Information Processing Systems*, 2023.
* Ledoit and Wolf [2004]

  Olivier Ledoit and Michael Wolf.
  A well-conditioned estimator for large-dimensional covariance matrices.
  *Journal of Multivariate Analysis*, 88(2):365–411, 2004.
* Lim et al. [2021]

  Bryan Lim, Sercan Ö. Arik, Nicolas Loeff, and Tomas Pfister.
  Temporal fusion transformers for interpretable multi-horizon time series forecasting.
  *International Journal of Forecasting*, 37(4):1748–1764, 2021.
  doi: 10.1016/j.ijforecast.2021.03.012.
* Lowe et al. [2017]

  Ryan Lowe, Yi Wu, Aviv Tamar, Jean Harb, Pieter Abbeel, and Igor Mordatch.
  Multi-agent actor-critic for mixed cooperative-competitive environments.
  In *Advances in Neural Information Processing Systems*, 2017.
* Markowitz [1952]

  Harry Markowitz.
  Portfolio selection.
  *Journal of Finance*, 7(1):77–91, 1952.
* Rasul et al. [2021]

  Kashif Rasul, Abdul-Saboor Sheikh, Ingo Schuster, Urs Bergmann, and Roland Vollgraf.
  Autoregressive denoising diffusion models for multivariate probabilistic time series forecasting.
  In *International Conference on Machine Learning*, 2021.
* Rockafellar and Uryasev [2000]

  R Tyrrell Rockafellar and Stanislav Uryasev.
  Optimization of conditional value-at-risk.
  *Journal of Risk*, 2(3):21–41, 2000.
* Shen et al. [2024]

  Lifeng Shen, Weiyu Chen, and James T. Kwok.
  Multi-resolution diffusion models for time series forecasting.
  In *International Conference on Learning Representations (ICLR)*, 2024.
* Tashiro et al. [2021]

  Yusuke Tashiro, Yang Song, Jiaming Song, and Stefano Ermon.
  Csdi: Conditional score-based diffusion models for probabilistic time series imputation.
  In *Advances in Neural Information Processing Systems*, 2021.
* Yoon et al. [2019]

  Jinsung Yoon, Daniel Jarrett, and Mihaela van der Schaar.
  Time-series generative adversarial networks.
  In *Advances in Neural Information Processing Systems*, 2019.
* Zhou et al. [2023]

  Haoyi Zhou, Shanghang Zhang, Jieqi Peng, Shuai Zhang, Jianmin Li, Hui Xiong, and Wancai Zhang.
  Informer: Beyond efficient transformer for long sequence time-series forecasting.
  In *AAAI Conference on Artificial Intelligence*, 2023.

## Appendix

## Appendix A Additional Methodology Details and Proof Sketches

#### Notation & Assumptions (Summary).

Rt∈ℝdR\_{t}\in\mathbb{R}^{d} returns; w∈ℝdw\in\mathbb{R}^{d} portfolio with 1⊤​w=11^{\top}w=1, box & turnover caps
(Sec. 3.4). HMM posteriors πt\pi\_{t} and context ztz\_{t} (Sec. 3.2); diffusion schedule αs\alpha\_{s}; CVaR
level α\alpha. Tail quantile Qq​(ℓ~)Q\_{q}(\tilde{\ell}) with ℓ~=−minj⁡rj\tilde{\ell}=-\min\_{j}r\_{j}. Blended moments
(μ^t,Σ^t)(\hat{\mu}\_{t},\hat{\Sigma}\_{t}) per Eq. (3). Loss L​(w,r)=−w⊤​rL(w,r)=-w^{\top}r. Denoiser ε^θ\hat{\varepsilon}\_{\theta}
with MoE gate gt=σ​(MLP​(zt))g\_{t}=\sigma(\mathrm{MLP}(z\_{t})) (Sec. 3.6).

### A.1 Comprehensive MARCD Objective (stochastic →\to sample-average)

At rebalance time tt with regime context 𝒛t\boldsymbol{z}\_{t} (from a KK-state HMM), the conditional generator defines
pθ​(𝐫∣𝒛t)p\_{\theta}(\mathbf{r}\mid\boldsymbol{z}\_{t}) for next-period returns 𝐫∈ℝd\mathbf{r}\in\mathbb{R}^{d}.
Let historical moments on a rolling window be (𝝁hist,𝚺hist)(\boldsymbol{\mu}\_{\text{hist}},\boldsymbol{\Sigma}\_{\text{hist}}) and
generator-implied moments be (𝝁synth,𝚺synth)(\boldsymbol{\mu}\_{\text{synth}},\boldsymbol{\Sigma}\_{\text{synth}}) where
𝝁synth=𝔼pθ​[𝐫∣𝒛t]\boldsymbol{\mu}\_{\text{synth}}=\mathbb{E}\_{p\_{\theta}}[\mathbf{r}\mid\boldsymbol{z}\_{t}] and
𝚺synth=Covpθ​[𝐫∣𝒛t]\boldsymbol{\Sigma}\_{\text{synth}}=\mathrm{Cov}\_{p\_{\theta}}[\mathbf{r}\mid\boldsymbol{z}\_{t}].
Blend

|  |  |  |
| --- | --- | --- |
|  | 𝝁^t=λ​𝝁synth+(1−λ)​𝝁hist,𝚺^t=λ​𝚺synth+(1−λ)​𝚺hist,\hat{\boldsymbol{\mu}}\_{t}=\lambda\,\boldsymbol{\mu}\_{\text{synth}}+(1{-}\lambda)\boldsymbol{\mu}\_{\text{hist}},\qquad\hat{\boldsymbol{\Sigma}}\_{t}=\lambda\,\boldsymbol{\Sigma}\_{\text{synth}}+(1{-}\lambda)\boldsymbol{\Sigma}\_{\text{hist}}, |  |

and (optionally) apply Ledoit–Wolf shrinkage 𝚺^tδ=(1−δ)​𝚺^t+δ​η​𝐈≻0\hat{\boldsymbol{\Sigma}}\_{t}^{\delta}=(1{-}\delta)\hat{\boldsymbol{\Sigma}}\_{t}+\delta\,\eta\mathbf{I}\succ 0.

Define portfolio loss L​(𝐰,𝐫)≔−𝐰⊤​𝐫L(\mathbf{w},\mathbf{r})\coloneqq-\mathbf{w}^{\top}\mathbf{r} with 𝐰∈ℝd\mathbf{w}\in\mathbb{R}^{d}.
The decision-aware stochastic program is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | min𝐰∈𝒲\displaystyle\min\_{\mathbf{w}\in\mathcal{W}}~ | −λμ​𝝁^t⊤​𝐰+γ​𝐰⊤​𝚺^t​𝐰⏟mean–variance regularizer+CVaRα​(L​(𝐰,𝐫))⏟tail risk under pθ(⋅∣𝒛t)\displaystyle\underbrace{-\lambda\_{\mu}\,\hat{\boldsymbol{\mu}}\_{t}^{\top}\mathbf{w}+\gamma\,\mathbf{w}^{\top}\hat{\boldsymbol{\Sigma}}\_{t}\mathbf{w}}\_{\text{mean--variance regularizer}}~+~\underbrace{\mathrm{CVaR}\_{\alpha}\!\big(L(\mathbf{w},\mathbf{r})\big)}\_{\text{tail risk under }p\_{\theta}(\cdot\mid\boldsymbol{z}\_{t})} |  | (8) |

subject to the feasible set
𝒲={𝐰:𝟏⊤​𝐰=1,ℓ≤𝐰≤𝒖,‖𝐰−𝐰t−1‖1≤τ}\mathcal{W}\!=\!\{\mathbf{w}:\mathbf{1}^{\top}\mathbf{w}=1,~\boldsymbol{\ell}\leq\mathbf{w}\leq\boldsymbol{u},~\|\mathbf{w}-\mathbf{w}\_{t-1}\|\_{1}\leq\tau\}.
Using the Rockafellar–Uryasev representation,
CVaRα​(L)=infζ∈ℝ{ζ+11−α​𝔼​(L−ζ)+}\mathrm{CVaR}\_{\alpha}(L)=\inf\_{\zeta\in\mathbb{R}}\big\{\zeta+\tfrac{1}{1-\alpha}\,\mathbb{E}(L-\zeta)\_{+}\big\}.
Approximating the expectation with NN i.i.d. scenarios 𝐫(i)∼pθ(⋅∣𝒛t)\mathbf{r}^{(i)}\!\sim p\_{\theta}(\cdot\mid\boldsymbol{z}\_{t}) yields the SAA:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝐰,ζ−λμ​𝝁^t⊤​𝐰+γ​𝐰⊤​𝚺^t​𝐰+ζ+1(1−α)​N​∑i=1N(L​(𝐰,𝐫(i))−ζ)+.\displaystyle\min\_{\mathbf{w},\zeta}~-\lambda\_{\mu}\,\hat{\boldsymbol{\mu}}\_{t}^{\top}\mathbf{w}+\gamma\,\mathbf{w}^{\top}\hat{\boldsymbol{\Sigma}}\_{t}\mathbf{w}+\zeta+\frac{1}{(1-\alpha)N}\sum\_{i=1}^{N}\big(L(\mathbf{w},\mathbf{r}^{(i)})-\zeta\big)\_{+}. |  | (9) |

### A.2 Epigraph QP, Turnover Linearization, and Dual Weights

Introduce ui≥0u\_{i}\geq 0 with ui≥L​(𝐰,𝐫(i))−ζu\_{i}\geq L(\mathbf{w},\mathbf{r}^{(i)})-\zeta to obtain the convex QP

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | min𝐰,ζ,{ui}≥0\displaystyle\min\_{\mathbf{w},\zeta,\{u\_{i}\}\geq 0}~ | −λμ​𝝁^t⊤​𝐰+γ​𝐰⊤​𝚺^t​𝐰+ζ+1(1−α)​N​∑i=1Nui\displaystyle-\lambda\_{\mu}\,\hat{\boldsymbol{\mu}}\_{t}^{\top}\mathbf{w}+\gamma\,\mathbf{w}^{\top}\hat{\boldsymbol{\Sigma}}\_{t}\mathbf{w}+\zeta+\frac{1}{(1-\alpha)N}\sum\_{i=1}^{N}u\_{i} |  | (10) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t. | 𝟏⊤​𝐰=1,ℓ≤𝐰≤𝒖,‖𝐰−𝐰t−1‖1≤τ,ui≥−𝐰⊤​𝐫(i)−ζ.\displaystyle\mathbf{1}^{\top}\mathbf{w}=1,\qquad\boldsymbol{\ell}\leq\mathbf{w}\leq\boldsymbol{u},\qquad\|\mathbf{w}-\mathbf{w}\_{t-1}\|\_{1}\leq\tau,\qquad u\_{i}\geq-\mathbf{w}^{\top}\mathbf{r}^{(i)}-\zeta. |  |

Turnover is enforced linearly by split variables 𝐬+,𝐬−≥0\mathbf{s}^{+},\mathbf{s}^{-}\!\geq 0 with 𝐰−𝐰t−1=𝐬+−𝐬−\mathbf{w}-\mathbf{w}\_{t-1}=\mathbf{s}^{+}-\mathbf{s}^{-} and
∑j(sj++sj−)≤τ\sum\_{j}(s^{+}\_{j}+s^{-}\_{j})\leq\tau (and, if penalized, add κ​∑j(sj++sj−)\kappa\sum\_{j}(s^{+}\_{j}+s^{-}\_{j}) to the objective).
For fixed 𝐰\mathbf{w}, the inner epigraph minimization has the well-known dual

|  |  |  |
| --- | --- | --- |
|  | maxp∈ℝN⁡1N​∑i=1Npi​L​(𝐰,𝐫(i))​s.t.​∑ipi=1,0≤pi≤1(1−α)​N,\max\_{p\in\mathbb{R}^{N}}~\frac{1}{N}\sum\_{i=1}^{N}p\_{i}\,L(\mathbf{w},\mathbf{r}^{(i)})\quad\text{s.t.}\quad\sum\_{i}p\_{i}=1,\quad 0\leq p\_{i}\leq\frac{1}{(1-\alpha)N}, |  |

so the CVaR term can be viewed as a worst-case tail-weighted average within a capped simplex.

#### Convexity and complexity.

With 𝚺^t⪰0\hat{\boldsymbol{\Sigma}}\_{t}\succeq 0 and linear constraints, ([10](https://arxiv.org/html/2510.10807v1#A1.E10 "In A.2 Epigraph QP, Turnover Linearization, and Dual Weights ‣ Appendix A Additional Methodology Details and Proof Sketches ‣ Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation")) is a convex QP.
Interior-point methods scale as 𝒪​(d3+N​d2)\mathcal{O}(d^{3}+Nd^{2}) per rebalance (here d=10d{=}10, N=1024N{=}1024).

### A.3 KKT Sketch for the Allocator (useful for auditability)

Let ν\nu be the multiplier for 𝟏⊤​𝐰=1\mathbf{1}^{\top}\mathbf{w}=1, (α−,α+)≥0(\alpha^{-},\alpha^{+})\!\geq\!0 for box constraints,
ρ≥0\rho\!\geq\!0 for turnover cap (via (𝐬+,𝐬−)(\mathbf{s}^{+},\mathbf{s}^{-})), and (βi,γi)≥0(\beta\_{i},\gamma\_{i})\!\geq\!0 for ui≥0u\_{i}\!\geq\!0 and
ui≥−𝐰⊤​𝐫(i)−z​e​t​au\_{i}\!\geq\!-\mathbf{w}^{\top}\mathbf{r}^{(i)}-\\
zeta. Stationarity gives

|  |  |  |
| --- | --- | --- |
|  | −λμ​𝝁^t+2​γ​𝚺^t​𝐰−∑i=1Nγi(1−α)​N​𝐫(i)+ν​ 1+(α+−α−)+turnover terms=0,1−∑i=1Nγi(1−α)​N=0,-\,\lambda\_{\mu}\,\hat{\boldsymbol{\mu}}\_{t}+2\gamma\,\hat{\boldsymbol{\Sigma}}\_{t}\mathbf{w}-\sum\_{i=1}^{N}\frac{\gamma\_{i}}{(1-\alpha)N}\,\mathbf{r}^{(i)}+\nu\,\mathbf{1}+(\alpha^{+}-\alpha^{-})+\text{turnover terms}=0,\quad 1-\sum\_{i=1}^{N}\frac{\gamma\_{i}}{(1-\alpha)N}=0, |  |

plus primal feasibility and complementary slackness.
These KKT quantities (including active box/turnover constraints and tail weights γi\gamma\_{i}) are
useful for *model-risk audit logs*.

### A.4 Decision-aware extension (sketch): bilevel objective and gradients

We sketch an end-to-end variant that trains generator parameters θ\theta for decision quality, not just sample fidelity.
Let 𝒙=(𝐰,ζ,{ui},𝐬+,𝐬−)\boldsymbol{x}\!=\!(\mathbf{w},\zeta,\{u\_{i}\},\mathbf{s}^{+},\mathbf{s}^{-}) collect allocator variables and write the QP from (6) compactly as

|  |  |  |
| --- | --- | --- |
|  | V​(θ;𝒛t)≔min𝒙∈𝒳​(θ;𝒛t)⁡F​(𝒙;θ,𝒛t),V(\theta;\boldsymbol{z}\_{t})\;\coloneqq\;\min\_{\boldsymbol{x}\in\mathcal{X}(\theta;\boldsymbol{z}\_{t})}\;F(\boldsymbol{x};\theta,\boldsymbol{z}\_{t}), |  |

where FF is the CVaR-epigraph objective (incl. MV term and optional turnover penalty) and 𝒳\mathcal{X} encodes the linear constraints.
The decision-aware training objective is the bilevel program

|  |  |  |  |
| --- | --- | --- | --- |
|  | minθ⁡𝔼t​[ℒdiff​(θ;𝒛t)+η​V​(θ;𝒛t)],\displaystyle\min\_{\theta}\;\;\mathbb{E}\_{t}\Big[\,\mathcal{L}\_{\text{diff}}(\theta;\boldsymbol{z}\_{t})\;+\;\eta\,V(\theta;\boldsymbol{z}\_{t})\,\Big], |  | (11) |

with scenarios 𝐫(i)=gθ​(𝜺i,𝒛t)\mathbf{r}^{(i)}\!=\!g\_{\theta}(\boldsymbol{\varepsilon}\_{i},\boldsymbol{z}\_{t}) (reparameterized draws; 𝜺i∼𝒩​(0,𝐈)\boldsymbol{\varepsilon}\_{i}\!\sim\!\mathcal{N}(0,\mathbf{I})).

#### Hypergradient (constraint-dependent envelope).

Let g​(𝒙;θ,𝒛t)≤0g(\boldsymbol{x};\theta,\boldsymbol{z}\_{t})\leq 0 and h​(𝒙;θ,𝒛t)=0h(\boldsymbol{x};\theta,\boldsymbol{z}\_{t})=0 denote the inequality/equality stacks for 𝒳\mathcal{X}, and (λ⋆,ν⋆)(\lambda^{\star},\nu^{\star}) the optimal duals at the inner solution 𝒙⋆​(θ;𝒛t)\boldsymbol{x}^{\star}(\theta;\boldsymbol{z}\_{t}).
Under standard regularity (convexity, LICQ, strict complementarity),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇θV​(θ;𝒛t)=∂θF​(𝒙⋆;θ,𝒛t)⏟pathwise term−λ⋆⊤​∂θg​(𝒙⋆;θ,𝒛t)+ν⋆⊤​∂θh​(𝒙⋆;θ,𝒛t)⏟constraint dependence via scenarios/moments.\displaystyle\nabla\_{\theta}V(\theta;\boldsymbol{z}\_{t})\;=\;\underbrace{\partial\_{\theta}F(\boldsymbol{x}^{\star};\theta,\boldsymbol{z}\_{t})}\_{\text{pathwise term}}\;-\;\underbrace{\lambda^{\star\top}\partial\_{\theta}g(\boldsymbol{x}^{\star};\theta,\boldsymbol{z}\_{t})\;+\;\nu^{\star\top}\partial\_{\theta}h(\boldsymbol{x}^{\star};\theta,\boldsymbol{z}\_{t})}\_{\text{constraint dependence via scenarios/moments}}. |  | (12) |

The full hypergradient of ([11](https://arxiv.org/html/2510.10807v1#A1.E11 "In A.4 Decision-aware extension (sketch): bilevel objective and gradients ‣ Appendix A Additional Methodology Details and Proof Sketches ‣ Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation")) is then
∇θ𝔼t​[ℒdiff]+η​𝔼t​[∇θV]\nabla\_{\theta}\mathbb{E}\_{t}[\,\mathcal{L}\_{\text{diff}}\,]\;+\;\eta\,\mathbb{E}\_{t}[\nabla\_{\theta}V],
where ∂θF\partial\_{\theta}F accounts for 𝝁^t​(θ),𝚺^t​(θ)\hat{\boldsymbol{\mu}}\_{t}(\theta),\hat{\boldsymbol{\Sigma}}\_{t}(\theta) and the scenario-dependent hinge terms via 𝐫(i)=gθ​(𝜺i,𝒛t)\mathbf{r}^{(i)}\!=\!g\_{\theta}(\boldsymbol{\varepsilon}\_{i},\boldsymbol{z}\_{t}).

#### Implicit differentiation (QP sensitivity).

Equivalently, one may differentiate the KKT system for 𝒙⋆\boldsymbol{x}^{\star}.
Let KK be the KKT Jacobian (block matrix of ∇x​x2ℒ\nabla^{2}\_{xx}\mathcal{L}, constraint Jacobians, and complementarity terms).
Solving the linear system

|  |  |  |
| --- | --- | --- |
|  | K​dd​θ​[𝒙⋆λ⋆ν⋆]=−[∂θ(∇xℒ​(𝒙⋆,λ⋆,ν⋆;θ))∂θg​(𝒙⋆;θ,𝒛t)∂θh​(𝒙⋆;θ,𝒛t)]K\;\frac{\mathrm{d}}{\mathrm{d}\theta}\!\begin{bmatrix}\boldsymbol{x}^{\star}\\ \lambda^{\star}\\ \nu^{\star}\end{bmatrix}\;=\;-\begin{bmatrix}\partial\_{\theta}\big(\nabla\_{x}\mathcal{L}(\boldsymbol{x}^{\star},\lambda^{\star},\nu^{\star};\theta)\big)\\[2.0pt] \partial\_{\theta}g(\boldsymbol{x}^{\star};\theta,\boldsymbol{z}\_{t})\\[2.0pt] \partial\_{\theta}h(\boldsymbol{x}^{\star};\theta,\boldsymbol{z}\_{t})\end{bmatrix} |  |

yields d​𝒙⋆d​θ\tfrac{\mathrm{d}\boldsymbol{x}^{\star}}{\mathrm{d}\theta}; one then applies the chain rule to F​(𝒙⋆;θ,𝒛t)F(\boldsymbol{x}^{\star};\theta,\boldsymbol{z}\_{t}).
In practice, ([12](https://arxiv.org/html/2510.10807v1#A1.E12 "In Hypergradient (constraint-dependent envelope). ‣ A.4 Decision-aware extension (sketch): bilevel objective and gradients ‣ Appendix A Additional Methodology Details and Proof Sketches ‣ Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation")) avoids forming d​𝒙⋆d​θ\tfrac{\mathrm{d}\boldsymbol{x}^{\star}}{\mathrm{d}\theta} explicitly because the duals (λ⋆,ν⋆)(\lambda^{\star},\nu^{\star}) are returned by the QP solver and can be logged (cf. auditability).

#### Smooth surrogate for stable training.

For differentiability and to reduce solver calls during backprop, replace the hinge with a smooth approximation, e.g.
(x)+≈1β​log⁡(1+eβ​x)(x)\_{+}\approx\tfrac{1}{\beta}\log(1+\mathrm{e}^{\beta x}) (large β\beta), and/or use a small quadratic penalty on turnover so the constraint set is θ\theta-independent.
Then the envelope simplifies to ∇θV≈∂θF​(𝒙⋆;θ,𝒛t)\nabla\_{\theta}V\approx\partial\_{\theta}F(\boldsymbol{x}^{\star};\theta,\boldsymbol{z}\_{t}) (constraints do not depend on θ\theta), while preserving the allocator’s behavior.

#### Practical recipe.

(i) Reparameterize scenarios: 𝐫(i)=gθ​(𝜺i,𝒛t)\mathbf{r}^{(i)}\!=\!g\_{\theta}(\boldsymbol{\varepsilon}\_{i},\boldsymbol{z}\_{t});
(ii) compute 𝝁^t,𝚺^t\hat{\boldsymbol{\mu}}\_{t},\hat{\boldsymbol{\Sigma}}\_{t} and solve the QP for 𝒙⋆\boldsymbol{x}^{\star} (store duals);
(iii) backpropagate through ([11](https://arxiv.org/html/2510.10807v1#A1.E11 "In A.4 Decision-aware extension (sketch): bilevel objective and gradients ‣ Appendix A Additional Methodology Details and Proof Sketches ‣ Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation")) using either the envelope form ([12](https://arxiv.org/html/2510.10807v1#A1.E12 "In Hypergradient (constraint-dependent envelope). ‣ A.4 Decision-aware extension (sketch): bilevel objective and gradients ‣ Appendix A Additional Methodology Details and Proof Sketches ‣ Crisis-Aware Regime-Conditioned Diffusion with CVaR Allocation")) or an implicit-diff QP layer;
(iv) use a small η\eta warm-up and gradient clipping;
(v) keep walk-forward protocol (no look-ahead).
Compute overhead is one QP solve per step plus either one adjoint KKT solve or the envelope evaluation; asymptotically the same order as inference (𝒪​(d3+N​d2)\mathcal{O}(d^{3}{+}Nd^{2})).

### A.5 Tail-Weighted Diffusion as a Spectral-Risk Surrogate

Recall the tail-weighted diffusion loss from (7),
Ltail=𝔼​[(1+η​ 1​{ℓ~≤Qq​(ℓ~)})​‖ε−εθ​(⋅)‖22]L\_{\text{tail}}=\mathbb{E}\big[\big(1+\eta\,\mathbf{1}\{\tilde{\ell}\leq Q\_{q}(\tilde{\ell})\}\big)\,\|\varepsilon-\varepsilon\_{\theta}(\cdot)\|\_{2}^{2}\big], where ℓ~=−minj⁡rj\tilde{\ell}=-\min\_{j}r\_{j} and q∈[0.05,0.10]q\in[0.05,0.10],
η∈[1,3]\eta\in[1,3] [, §3.5], and the regime-MoE gate is defined in §3.6.

###### Assumption 1 (Tail-Lipschitz Decoder).

There exists L>0L>0 such that the denoising error maps to return error with
‖r−r^‖≤L​‖ε−εθ‖\|r-\hat{r}\|\leq L\,\|\varepsilon-\varepsilon\_{\theta}\| on the lower-qq tail set {ℓ~≤Qq​(ℓ~)}\{\tilde{\ell}\leq Q\_{q}(\tilde{\ell})\}.

###### Proposition 1 (Spectral risk proxy for portfolio tail functionals).

Let w∈ℝdw\in\mathbb{R}^{d} be any feasible portfolio (budget/box/turnover constraints as in (4)–(6)).
Under the Tail-Lipschitz Decoder, the portfolio CVaR error admits

|  |  |  |
| --- | --- | --- |
|  | |CVaRα​(−w⊤​r)−CVaRα​(−w⊤​r^)|≤L​‖w‖21−α​𝔼​[(1+η​ 1​{ℓ~≤Qq​(ℓ~)})​‖ε−εθ​(⋅)‖22].\Big|\mathrm{CVaR}\_{\alpha}(-w^{\top}r)-\mathrm{CVaR}\_{\alpha}(-w^{\top}\hat{r})\Big|\;\leq\;\frac{L\,\|w\|\_{2}}{1-\alpha}\,\sqrt{\mathbb{E}\!\left[\big(1+\eta\,\mathbf{1}\{\tilde{\ell}\leq Q\_{q}(\tilde{\ell})\}\big)\,\|\varepsilon-\varepsilon\_{\theta}(\cdot)\|\_{2}^{2}\right]}. |  |

###### Sketch.

Write the CVaR difference as a tail average of linear losses and apply Cauchy–Schwarz on the
tail region. The Lipschitz link transfers denoising error into return error; the (1−α)−1(1-\alpha)^{-1}
factor comes from the Rockafellar–Uryasev representation. Tail reweighting magnifies the
integrand over the lower-qq region, producing a spectral-risk-like weight on squared error.
∎

###### Remark 1 (Decision relevance).

Since allocation solves the convex CVaR epigraph QP (4)–(6), controlling the bound above
reduces the decision-relevant generalization gap seen by the allocator.

### A.6 Finite-Sample Statistics of Tail Reweighting

Define weights wi=1+η​ 1​{ℓ~i≤Qq​(ℓ~)}w\_{i}=1+\eta\,\mathbf{1}\{\tilde{\ell}\_{i}\leq Q\_{q}(\tilde{\ell})\}.
With q=ℙ​(ℓ~≤Qq​(ℓ~))q=\mathbb{P}(\tilde{\ell}\leq Q\_{q}(\tilde{\ell})), the normalized weights are
w¯i=wi/((1−q)+q​(1+η))\bar{w}\_{i}=w\_{i}/\big((1-q)+q(1+\eta)\big).

###### Proposition 2 (Closed-form effective sample size (ESS)).

Let NN be the batch size. Then the ESS of (w¯i)i=1N(\bar{w}\_{i})\_{i=1}^{N} is

|  |  |  |
| --- | --- | --- |
|  | ESS​(q,η)=N​(1+η​q)21+2​η​q+η2​q=N​1+2​η​q+η2​q21+2​η​q+η2​q.\mathrm{ESS}(q,\eta)=N\,\frac{\big(1+\eta q\big)^{2}}{1+2\eta q+\eta^{2}q}\;=\;N\,\frac{1+2\eta q+\eta^{2}q^{2}}{1+2\eta q+\eta^{2}q}. |  |

###### Proof.

Compute ESS=(∑iw¯i)2/∑iw¯i2\mathrm{ESS}=(\sum\_{i}\bar{w}\_{i})^{2}/\sum\_{i}\bar{w}\_{i}^{2} by partitioning into tail vs non-tail
fractions (q,1−q)(q,1-q) and substituting w={1,1+η}w=\{1,1+\eta\}.
∎

###### Remark 2 (Choosing (q,η)(q,\eta)).

Moderate (q,η)(q,\eta) keeps ESS\mathrm{ESS} large while emphasizing the adverse region that drives
CVaRα\mathrm{CVaR}\_{\alpha}. In practice, your ranges q∈[0.05,0.10],η∈[1,3]q\in[0.05,0.10],\;\eta\in[1,3] preserve stability.

### A.7 Regime-MoE Denoiser: Oracle Inequality and Crisis Specialization

Let ZZ be the regime context with gate g​(Z)∈[0,1]g(Z)\in[0,1] and experts
εθ,base,εθ,crisis\varepsilon\_{\theta,\mathrm{base}},\varepsilon\_{\theta,\mathrm{crisis}}.
The denoiser is ε^θ=(1−g)​εθ,base+g​εθ,crisis\hat{\varepsilon}\_{\theta}=(1-g)\varepsilon\_{\theta,\mathrm{base}}+g\,\varepsilon\_{\theta,\mathrm{crisis}}
[, §3.6].

###### Assumption 2 (Well-specified conditional regressors).

For each regime label C∈{base,crisis}C\in\{\mathrm{base},\mathrm{crisis}\},
the Bayes denoiser equals the conditional mean:
εC⋆​(x,s,Z)=𝔼​[ε|x,s,Z,C]\varepsilon^{\star}\_{C}(x,s,Z)=\mathbb{E}[\varepsilon\,|\,x,s,Z,C].

###### Theorem 4 (MoE oracle risk decomposition).

Let g⋆​(Z)=ℙ​(C=crisis|Z)g^{\star}(Z)=\mathbb{P}(C=\mathrm{crisis}\,|\,Z).
Then for squared loss,

|  |  |  |
| --- | --- | --- |
|  | ℛ​(ε^θ)−ℛ​(ε^⋆)≤c1​𝔼​[(g​(Z)−g⋆​(Z))2]+c2​∑CApproxErrC,\mathcal{R}(\hat{\varepsilon}\_{\theta})-\mathcal{R}(\hat{\varepsilon}^{\star})\;\leq\;c\_{1}\,\mathbb{E}\!\left[(g(Z)-g^{\star}(Z))^{2}\right]+c\_{2}\,\sum\_{C}\mathrm{ApproxErr}\_{C}, |  |

where ε^⋆=(1−g⋆)​εbase⋆+g⋆​εcrisis⋆\hat{\varepsilon}^{\star}=(1-g^{\star})\varepsilon^{\star}\_{\mathrm{base}}+g^{\star}\,\varepsilon^{\star}\_{\mathrm{crisis}},
and ApproxErrC\mathrm{ApproxErr}\_{C} is the approximation error of each expert class.

###### Sketch.

Expand the regression risk via law of total expectation and project onto the MoE span.
The first term arises from gating misclassification; the second from function-class limits.
∎

###### Corollary 1 (Crisis improvement under informative gating).

If gg is monotone in the HMM crisis posterior (as in §3.6) and the crisis expert reduces tail MSE,
then MoE strictly improves tail-region risk whenever
𝔼​[(g−g⋆)2]\mathbb{E}[(g-g^{\star})^{2}] is below a regime-dependent threshold.

### A.8 Stability of Gated Denoising and DDPM Sampling

###### Assumption 3 (Lipschitz experts and gate).

Each expert is LεL\_{\varepsilon}-Lipschitz in (x,s)(x,s) and the gate g​(Z)g(Z) is LgL\_{g}-Lipschitz in its inputs.

###### Proposition 3 (Lipschitz constant of the MoE drift).

The MoE denoiser inherits Lipschitz constant
LMoE≤(1+‖g‖∞)​Lε+Lg​ΔεL\_{\mathrm{MoE}}\leq(1+\|g\|\_{\infty})L\_{\varepsilon}+L\_{g}\,\Delta\_{\varepsilon},
where Δε=sup‖εcrisis−εbase‖\Delta\_{\varepsilon}=\sup\|\,\varepsilon\_{\mathrm{crisis}}-\varepsilon\_{\mathrm{base}}\,\|.
Hence the DDPM reverse SDE/ODE remains contractive whenever
LMoEL\_{\mathrm{MoE}} satisfies the usual step-size criteria.

###### Remark 3.

This implies stability of sampling trajectories when the gate smoothly tracks regime posteriors
(our HMM-derived gt=σ​(MLP​(zt))g\_{t}=\sigma(\mathrm{MLP}(z\_{t}))).

### A.9 Decision-Relevant Regret Bound for the CVaR Allocator

Let w⋆w^{\star} solve the true-distribution QP (4)–(6) and w^\hat{w} the QP using
blended/shrunk (μ^t,Σ^t)(\hat{\mu}\_{t},\hat{\Sigma}\_{t}) and sample CVaR under pθ(⋅|zt)p\_{\theta}(\cdot|z\_{t}).

###### Assumption 4 (Modeling error budgets).

There exist δμ,δΣ,δCVaR≥0\delta\_{\mu},\delta\_{\Sigma},\delta\_{\mathrm{CVaR}}\geq 0 such that
‖μ^t−μ⋆‖2≤δμ\|\hat{\mu}\_{t}-\mu^{\star}\|\_{2}\leq\delta\_{\mu}, ‖Σ^t−Σ⋆‖op≤δΣ\|\hat{\Sigma}\_{t}-\Sigma^{\star}\|\_{\mathrm{op}}\leq\delta\_{\Sigma},
and the CVaR term differs from truth by at most δCVaR\delta\_{\mathrm{CVaR}} uniformly over feasible ww.

###### Theorem 5 (Regret bound).

Let Γ\Gamma be the strong convexity modulus of the QP objective in ww induced by Σ^t\hat{\Sigma}\_{t}.
Then

|  |  |  |
| --- | --- | --- |
|  | F​(w^)−F​(w⋆)≤12​Γ​(λμ​δμ+κΣ​δΣ+δCVaR)2,F(\hat{w})-F(w^{\star})\;\leq\;\frac{1}{2\Gamma}\Big(\lambda\_{\mu}\,\delta\_{\mu}+\kappa\_{\Sigma}\,\delta\_{\Sigma}+\delta\_{\mathrm{CVaR}}\Big)^{2}, |  |

for suitable λμ,κΣ\lambda\_{\mu},\kappa\_{\Sigma} depending on budget/box/turnover radii.
Moreover, if LtailL\_{\text{tail}} is small, then δCVaR\delta\_{\mathrm{CVaR}} is small by Proposition in A.5.

###### Sketch.

Apply standard stability of strongly convex programs under objective perturbations, bounding
the mean/variance terms by norm inequalities and the CVaR gap via A.5.
∎

### A.10 Quantile-Threshold Asymptotics for Qq​(ℓ~)Q\_{q}(\tilde{\ell})

Let Q^q\hat{Q}\_{q} be the empirical qq-quantile of ℓ~\tilde{\ell} used in LtailL\_{\text{tail}}.
Under standard regularity (continuous density fℓ~f\_{\tilde{\ell}} at QqQ\_{q}),

|  |  |  |
| --- | --- | --- |
|  | N​(Q^q−Qq)⇒𝒩​(0,q​(1−q)/fℓ~​(Qq)2).\sqrt{N}\,(\hat{Q}\_{q}-Q\_{q})\;\Rightarrow\;\mathcal{N}\big(0,\,q(1-q)/f\_{\tilde{\ell}}(Q\_{q})^{2}\big). |  |

Thus the randomness introduced by thresholding is Oℙ​(N−1/2)O\_{\mathbb{P}}(N^{-1/2}) and absorbed by
the ESS of A.6 for moderate (q,η)(q,\eta).

###### Remark 4.

In practice, we use a running estimate of QqQ\_{q} with exponential smoothing, which further
stabilizes the gate into the weighted region while keeping the training unbiased on average.

### A.11 Tail-Weighted Diffusion as a Spectral Risk Upper-Bound

Recall LtailL\_{\text{tail}} in (7). Define a spectral weight ϕ​(u)=1+η​ 1​{u≤q}\phi(u)=1+\eta\,\mathbf{1}\{u\leq q\} on u∈[0,1]u\in[0,1],
normalized by ϕ¯=∫01ϕ​(u)​𝑑u=1+η​q\bar{\phi}=\int\_{0}^{1}\phi(u)\,du=1+\eta q, and its probability measure
d​Φ​(u)=ϕ​(u)​d​u/ϕ¯d\Phi(u)=\phi(u)\,du/\bar{\phi}. Let ℛΦ​(L)\mathcal{R}\_{\Phi}(L) be the spectral risk of a loss LL under Φ\Phi.

###### Assumption 5 (Tail-Lipschitz Decoder on tail set).

There exists Ldec>0L\_{\mathrm{dec}}>0 s.t. on {ℓ~≤Qq​(ℓ~)}\{\tilde{\ell}\leq Q\_{q}(\tilde{\ell})\} we have
‖r−r^‖≤Ldec​‖ε−εθ‖\|r-\hat{r}\|\leq L\_{\mathrm{dec}}\,\|\varepsilon-\varepsilon\_{\theta}\|.

###### Theorem 6 (Spectral CVaR control by LtailL\_{\text{tail}}).

For any feasible ww,

|  |  |  |
| --- | --- | --- |
|  | |CVaRα​(−w⊤​r)−CVaRα​(−w⊤​r^)|≤Ldec​‖w‖21−α​ϕ¯​𝔼​[ϕ​(U)​‖ε−εθ‖22],\Big|\mathrm{CVaR}\_{\alpha}(-w^{\top}r)-\mathrm{CVaR}\_{\alpha}(-w^{\top}\hat{r})\Big|\;\leq\;\frac{L\_{\mathrm{dec}}\,\|w\|\_{2}}{1-\alpha}\;\sqrt{\bar{\phi}\;\mathbb{E}\big[\phi(U)\,\|\varepsilon-\varepsilon\_{\theta}\|\_{2}^{2}\big]}, |  |

where UU is the PIT of ℓ~\tilde{\ell}. Hence minimizing LtailL\_{\text{tail}} reduces a spectral upper-bound
on the *decision-relevant* CVaR generalization gap.

###### Sketch.

Express CVaR via Rockafellar–Uryasev’s tail average. Cauchy–Schwarz with tail reweighting
ϕ\phi yields the inequality; the decoder Lipschitz links denoising and return errors.
∎

###### Remark 5.

Because allocation solves the convex CVaR epigraph QP in (4)–(6), decreasing this gap
directly lowers the allocator’s risk mis-specification at decision time.

### A.12 Finite-Sample Efficiency of Tail Reweighting

Let wi=1+η​ 1​{ℓ~i≤Qq​(ℓ~)}w\_{i}=1+\eta\,\mathbf{1}\{\tilde{\ell}\_{i}\leq Q\_{q}(\tilde{\ell})\} and normalized w¯i=wi/𝔼​[wi]\bar{w}\_{i}=w\_{i}/\mathbb{E}[w\_{i}].

###### Proposition 4 (Effective sample size).

ESS=N​(1+η​q)2(1−q)+q​(1+η)2=N​1+2​η​q+η2​q21+2​η​q+η2​q\mathrm{ESS}=N\frac{(1+\eta q)^{2}}{(1-q)+q(1+\eta)^{2}}=N\frac{1+2\eta q+\eta^{2}q^{2}}{1+2\eta q+\eta^{2}q}.

###### Remark 6.

Moderate (q,η)(q,\eta) (e.g., q∈[0.05,0.10],η∈[1,3]q\in[0.05,0.10],\,\eta\in[1,3]) retains high ESS while emphasizing
the adverse set that drives CVaRα\mathrm{CVaR}\_{\alpha}.

### A.13 Regime-MoE: Oracle Inequality, Consistency, and Stability

Let ε^θ=(1−g)​εθ,base+g​εθ,crisis\hat{\varepsilon}\_{\theta}=(1-g)\varepsilon\_{\theta,\mathrm{base}}+g\,\varepsilon\_{\theta,\mathrm{crisis}} with g=g​(Z)∈[0,1]g=g(Z)\in[0,1].

###### Assumption 6 (Bayes experts + margin).

For C∈{base,crisis}C\in\{\mathrm{base},\mathrm{crisis}\}, the Bayes denoiser εC⋆\varepsilon^{\star}\_{C} lies in the closure of the
expert class and there exists a margin γm>0\gamma\_{m}>0 such that
ℙ​(|g⋆​(Z)−1/2|≤γm)≤κm\mathbb{P}(|g^{\star}(Z)-1/2|\leq\gamma\_{m})\leq\kappa\_{m} for some κm<1\kappa\_{m}<1.

###### Theorem 7 (Oracle excess risk for MoE).

For squared loss,

|  |  |  |
| --- | --- | --- |
|  | ℛ​(ε^θ)−ℛ​(ε^⋆)≤c1​𝔼​[(g−g⋆)2]+c2​∑C∈{base,crisis}ApproxErrC+c3​κm,\mathcal{R}(\hat{\varepsilon}\_{\theta})-\mathcal{R}(\hat{\varepsilon}^{\star})\;\leq\;c\_{1}\,\mathbb{E}\!\left[(g-g^{\star})^{2}\right]+c\_{2}\!\!\sum\_{C\in\{\mathrm{base,crisis}\}}\!\!\!\!\mathrm{ApproxErr}\_{C}+c\_{3}\,\kappa\_{m}, |  |

where ε^⋆=(1−g⋆)​εbase⋆+g⋆​εcrisis⋆\hat{\varepsilon}^{\star}=(1-g^{\star})\varepsilon^{\star}\_{\mathrm{base}}+g^{\star}\varepsilon^{\star}\_{\mathrm{crisis}}.

###### Proposition 5 (Gate consistency).

If gg is trained with a calibrated surrogate (e.g., logistic) on HMM posteriors and the feature
class has finite Rademacher complexity ℜn\mathfrak{R}\_{n}, then
𝔼​[(g−g⋆)2]=O​(ℜn)+on​(1)\mathbb{E}[(g-g^{\star})^{2}]\!=\!O(\mathfrak{R}\_{n})+o\_{n}(1).

###### Proposition 6 (Lipschitz MoE drift).

If experts are LεL\_{\varepsilon}-Lipschitz in (x,s)(x,s) and gg is LgL\_{g}-Lipschitz in ZZ,
then the MoE drift is LMoE≤(1+‖g‖∞)​Lε+Lg​ΔεL\_{\mathrm{MoE}}\!\leq\!(1+\|g\|\_{\infty})L\_{\varepsilon}+L\_{g}\,\Delta\_{\varepsilon},
Δε=sup‖εcrisis−εbase‖\Delta\_{\varepsilon}=\sup\|\varepsilon\_{\mathrm{crisis}}-\varepsilon\_{\mathrm{base}}\|, ensuring stable DDPM steps.

### A.14 Allocation Mapping: Strong Convexity, Lipschitzness, and Regret

Let w^​(μ^,Σ^)\hat{w}(\hat{\mu},\hat{\Sigma}) solve the CVaR-QP (4)–(6) and assume Σ^⪰λmin​I\hat{\Sigma}\succeq\lambda\_{\min}I.

###### Theorem 8 (Lipschitz solution map).

There exist constants (cμ,cΣ)(c\_{\mu},c\_{\Sigma}) such that for feasible perturbations
(δ​μ,δ​Σ)(\delta\mu,\delta\Sigma) with fixed constraints,

|  |  |  |
| --- | --- | --- |
|  | ‖w^​(μ^+δ​μ,Σ^+δ​Σ)−w^​(μ^,Σ^)‖2≤cμ​‖δ​μ‖2+cΣ​‖δ​Σ‖opλmin.\|\hat{w}(\hat{\mu}+\delta\mu,\hat{\Sigma}+\delta\Sigma)-\hat{w}(\hat{\mu},\hat{\Sigma})\|\_{2}\;\leq\;\frac{c\_{\mu}\|\delta\mu\|\_{2}+c\_{\Sigma}\|\delta\Sigma\|\_{\mathrm{op}}}{\lambda\_{\min}}. |  |

###### Corollary 2 (Decision regret under moment & CVaR errors).

Let δCVaR\delta\_{\mathrm{CVaR}} bound the CVaR term perturbation uniformly over feasible ww.
If the objective is Γ\Gamma-strongly convex in ww, then

|  |  |  |
| --- | --- | --- |
|  | F​(w^)−F​(w⋆)≤12​Γ​(λμ​‖δ​μ‖2+κΣ​‖δ​Σ‖op+δCVaR)2.F(\hat{w})-F(w^{\star})\;\leq\;\frac{1}{2\Gamma}\Big(\lambda\_{\mu}\|\delta\mu\|\_{2}+\kappa\_{\Sigma}\|\delta\Sigma\|\_{\mathrm{op}}+\delta\_{\mathrm{CVaR}}\Big)^{2}. |  |

###### Remark 7.

By A.11, δCVaR\delta\_{\mathrm{CVaR}} shrinks with LtailL\_{\text{tail}}; thus tail-weighted training tightens the
end-to-end decision regret.

### A.15 Distribution Shift View: CVaR Sensitivity under Wasserstein-W1W\_{1}

Let losses be KK-Lipschitz in rr. For distributions P,QP,Q with W1​(P,Q)≤ρW\_{1}(P,Q)\leq\rho,

###### Proposition 7 (CVaR Lipschitz continuity).

|CVaRαP​(L)−CVaRαQ​(L)|≤K1−α​ρ.|\mathrm{CVaR}\_{\alpha}^{P}(L)-\mathrm{CVaR}\_{\alpha}^{Q}(L)|\leq\frac{K}{1-\alpha}\,\rho.

###### Sketch.

Use the tail-average representation of CVaR and Kantorovich–Rubinstein duality, noting the
1/(1−α)1/(1-\alpha) amplification of tail averages.
∎

###### Remark 8 (Interpretation).

Tail-aware generation (small LtailL\_{\text{tail}}) + bounded shift ρ\rho jointly ensure limited CVaR drift,
explaining empirical robustness under modest market shifts.

### A.16 Convex Pathwise Drawdown-CVaR Surrogate

For a horizon {t+1,…,t+H}\{t+1,\dots,t+H\} with scenarios rt+1:t+H(i)r^{(i)}\_{t+1:t+H}, introduce auxiliary peaks
ph(i)p^{(i)}\_{h} and drawdowns dh(i)d^{(i)}\_{h}:

|  |  |  |
| --- | --- | --- |
|  | ph(i)≥ph−1(i)+w⊤​rt+h(i),dh(i)≥ph(i)−(pt(i)+∑u=1hw⊤​rt+u(i)),MDD(i)≥dh(i).p^{(i)}\_{h}\geq p^{(i)}\_{h-1}+w^{\top}r^{(i)}\_{t+h},\quad d^{(i)}\_{h}\geq p^{(i)}\_{h}-\big(p^{(i)}\_{t}+\textstyle\sum\_{u=1}^{h}w^{\top}r^{(i)}\_{t+u}\big),\quad\operatorname{MDD}^{(i)}\geq d^{(i)}\_{h}. |  |

Then the convex surrogate program

|  |  |  |
| --- | --- | --- |
|  | minw,ζ,{MDD(i)},…⁡ζ+1(1−α)​N​∑i(MDD(i)−ζ)++ MV terms\min\_{w,\zeta,\{\operatorname{MDD}^{(i)}\},\ldots}\;\;\zeta+\frac{1}{(1-\alpha)N}\sum\_{i}(\operatorname{MDD}^{(i)}-\zeta)\_{+}\;+\;\text{ MV terms} |  |

with budget/box/turnover constraints yields a CVaR-over-drawdown relaxation that stays QP-like
after linearization, enabling direct drawdown control in multi-step allocation.

### A.17 Envelope for Decision-Aware Training

Consider V​(θ;zt)=minx∈X⁡F​(x;θ,zt)V(\theta;z\_{t})=\min\_{x\in X}\,F(x;\theta,z\_{t}) where x=(w,ζ,{ui},s+,s−)x=(w,\zeta,\{u\_{i}\},s^{+},s^{-})
and XX fixes budget/box/turnover constraints (θ\theta-independent). Then

###### Theorem 9 (Constraint-Independent Envelope).

If F​(⋅;θ,zt)F(\cdot;\theta,z\_{t}) is continuously differentiable in θ\theta and XX does not depend on θ\theta,
then at any optimum x⋆​(θ;zt)x^{\star}(\theta;z\_{t}),

|  |  |  |
| --- | --- | --- |
|  | ∇θV​(θ;zt)=∂θF​(x⋆​(θ;zt);θ,zt).\nabla\_{\theta}V(\theta;z\_{t})\;=\;\partial\_{\theta}F\big(x^{\star}(\theta;z\_{t});\theta,z\_{t}\big). |  |

###### Sketch.

Direct envelope theorem: no constraint Jacobians in θ\theta; dual terms vanish from the gradient.
∎

###### Corollary 3 (Smooth hinge surrogate for CVaR).

Replacing (x)+(x)\_{+} by a smooth (1/β)​log⁡(1+eβ​x)(1/\beta)\log(1+e^{\beta x}) yields
∇θ𝔼​[V​(θ;zt)]=𝔼​[∂θF​(x⋆;θ,zt)]\nabla\_{\theta}\mathbb{E}[V(\theta;z\_{t})]=\mathbb{E}[\partial\_{\theta}F(x^{\star};\theta,z\_{t})],
facilitating end-to-end training with a single QP solve per step.

### A.18 CVaR Estimation with Tail Reweighting

Let CVaR^α\widehat{\mathrm{CVaR}}\_{\alpha} be the empirical epigraph estimator using NN scenarios.

###### Assumption 7 (Tail regularity).

The loss distribution has continuous density near VaRα\mathrm{VaR}\_{\alpha} and finite second moment
on the lower tail.

###### Theorem 10 (Rate with tail emphasis).

For weights wi=1+η​ 1​{ℓ~i≤Qq​(ℓ~)}w\_{i}=1+\eta\,\mathbf{1}\{\tilde{\ell}\_{i}\leq Q\_{q}(\tilde{\ell})\} normalized to w¯i\bar{w}\_{i},

|  |  |  |
| --- | --- | --- |
|  | |CVaR^α−CVaRα|=Oℙ​(1ESS​(q,η)),\big|\widehat{\mathrm{CVaR}}\_{\alpha}-\mathrm{CVaR}\_{\alpha}\big|=O\_{\mathbb{P}}\!\left(\sqrt{\frac{1}{\mathrm{ESS}(q,\eta)}}\right), |  |

with ESS​(q,η)\mathrm{ESS}(q,\eta) from App. A.12. Moderate (q,η)(q,\eta) balances bias/variance:
higher tail mass can reduce variance of the tail average while keeping ESS large.

### A.19 Gate Monotonicity ⇒\Rightarrow Tail-Region Risk Drop

Let g⋆​(Z)=ℙ​(C=crisis∣Z)g^{\star}(Z)=\mathbb{P}(C=\mathrm{crisis}\mid Z) and suppose the crisis expert dominates on the
tail region: 𝔼​[‖ε−εcrisis⋆‖2|ℓ~≤Qq​(ℓ~)]≤𝔼​[‖ε−εbase⋆‖2|ℓ~≤Qq​(ℓ~)]\mathbb{E}\big[\|\varepsilon-\varepsilon\_{\mathrm{crisis}}^{\star}\|^{2}\,\big|\,\tilde{\ell}\leq Q\_{q}(\tilde{\ell})\big]\leq\mathbb{E}\big[\|\varepsilon-\varepsilon\_{\mathrm{base}}^{\star}\|^{2}\,\big|\,\tilde{\ell}\leq Q\_{q}(\tilde{\ell})\big].

###### Proposition 8 (Tail-risk improvement under monotone gate).

If g​(Z)g(Z) is non-decreasing in the HMM crisis posterior (Sec. 3.6), then for sufficiently small
𝔼​[(g−g⋆)2]\mathbb{E}[(g-g^{\star})^{2}], the MoE denoiser strictly reduces tail-region MSE versus either single expert.

###### Sketch.

Risk decomposition from the MoE oracle inequality (App. A.13) and the dominance assumption on the tail set.
∎

### A.20 End-to-End Decision Gap under Distribution Shift

Let PP (train) and QQ (test) satisfy W1​(P,Q)≤ρW\_{1}(P,Q)\leq\rho for scenario distributions.
Assume per-scenario loss L​(w,r)L(w,r) is KK-Lipschitz in rr for feasible ww.

###### Theorem 11 (Shift-aware decision bound).

Let w^\hat{w} be the optimizer under PθP\_{\theta} and wQ⋆w\_{Q}^{\star} under QQ.
Then for the CVaR objective,

|  |  |  |
| --- | --- | --- |
|  | FQ​(w^)−FQ​(wQ⋆)≤c1​Ltail1/2⏟train gen. gap+c2​ρ/(1−α)⏟shift gap+c3​‖μ^−μQ‖2+c4​‖Σ^−ΣQ‖op⏟moment error,F\_{Q}(\hat{w})-F\_{Q}(w\_{Q}^{\star})\;\leq\;\underbrace{c\_{1}\,L\_{\text{tail}}^{1/2}}\_{\text{train gen. gap}}\;+\;\underbrace{c\_{2}\,\rho/(1-\alpha)}\_{\text{shift gap}}\;+\;\underbrace{c\_{3}\,\|\hat{\mu}-\mu\_{Q}\|\_{2}+c\_{4}\,\|\hat{\Sigma}-\Sigma\_{Q}\|\_{\rm op}}\_{\text{moment error}}, |  |

for constants (ci)(c\_{i}) depending on feasible-set radii and strong convexity.

###### Sketch.

Combine App. A.11 (spectral control), App. A.15 (CVaR W1W\_{1} continuity), and App. A.14 (allocator Lipschitz).
∎