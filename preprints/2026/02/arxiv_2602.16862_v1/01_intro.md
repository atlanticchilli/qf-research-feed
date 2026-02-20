---
authors:
- Andy Au
doc_id: arxiv:2602.16862v1
family_id: arxiv:2602.16862
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Entropy Regularization as Robustness under Bayesian Drift Uncertainty
url_abs: http://arxiv.org/abs/2602.16862v1
url_html: https://arxiv.org/html/2602.16862v1
venue: arXiv q-fin
version: 1
year: 2026
---


Andy Au
  
Department of Mathematics and Statistics
  
Boston University
  
aa314@bu.edu

###### Abstract

We study entropy-regularized mean-variance portfolio optimization under Bayesian drift uncertainty. Gaussian policies remain optimal under partial information, the value function is quadratic in wealth, and belief-dependent coefficients admit closed-form solutions. The mean control is identical to deterministic Bayesian Markowitz feedback; entropy regularization affects only the policy variance. Additionally, this variance does not affect information gain, and instead provides belief-dependent robustness. Notably, optimal policy variance increases with posterior conviction |mt||m\_{t}|, forcing greater action randomization when mean position is most aggressive.

## 1 Introduction

Portfolio optimization under parameter uncertainty is a fundamental problem in finance. The classical mean-variance framework of Markowitz ([1952](https://arxiv.org/html/2602.16862v1#bib.bib1 "Portfolio selection")) produces clean solutions when parameters are known, but real markets have unknown drift. The difficulty of estimating expected returns (Merton, [1980](https://arxiv.org/html/2602.16862v1#bib.bib2 "On estimating the expected return on the market: an exploratory investigation")) leads to unstable allocations when one naively plugs in estimated means.

Two recent lines of work address this from different angles:

1. 1.

   Bayesian learning: De Franco et al. ([2018](https://arxiv.org/html/2602.16862v1#bib.bib5 "Bayesian learning for the Markowitz portfolio selection problem")) solve the continuous-time Markowitz problem when drift is unknown. Using Kalman–Bucy filtering, they reduce the problem to a semilinear PDE in the belief state and obtain closed-form solutions for Gaussian priors. The optimal control is deterministic.
2. 2.

   Entropy-regularized control: Wang and Zhou ([2019](https://arxiv.org/html/2602.16862v1#bib.bib6 "Continuous-time mean–variance portfolio selection: a reinforcement learning framework")) study mean-variance optimization with known drift but replace deterministic controls with stochastic policies. Adding an entropy bonus yields tractable Gaussian solutions and connects to relaxed stochastic control. The problem closes through Riccati ODEs.

These two lines sit within broader literature. Optimal investment under partial information on drift was started by Lakner ([1998](https://arxiv.org/html/2602.16862v1#bib.bib3 "Optimal trading strategy for an investor: the case of partial information")) and extended to different utility by Brendle ([2006](https://arxiv.org/html/2602.16862v1#bib.bib7 "Portfolio selection under incomplete information")) and Bäuerle and Rieder ([2004](https://arxiv.org/html/2602.16862v1#bib.bib8 "Portfolio optimization with Markov-modulated stock prices and interest rates")); De Franco et al. ([2018](https://arxiv.org/html/2602.16862v1#bib.bib5 "Bayesian learning for the Markowitz portfolio selection problem")) is the mean-variance instance. Entropy-regularized control in RL traces to Ziebart ([2010](https://arxiv.org/html/2602.16862v1#bib.bib10 "Modeling purposeful adaptive behavior with the principle of maximum causal entropy")) in discrete time and Haarnoja et al. ([2018](https://arxiv.org/html/2602.16862v1#bib.bib9 "Soft actor-critic: off-policy maximum entropy deep reinforcement learning with a stochastic actor")) (Soft Actor–Critic) in practice; Wang and Zhou ([2019](https://arxiv.org/html/2602.16862v1#bib.bib6 "Continuous-time mean–variance portfolio selection: a reinforcement learning framework")) provides the continuous-time theory. Our finding that entropy regularization acts as a robustness mechanism connects to the robust portfolio optimization literature (Garlappi et al., [2007](https://arxiv.org/html/2602.16862v1#bib.bib11 "Portfolio selection with parameter and model uncertainty: a multi-prior approach"); Hansen and Sargent, [2001](https://arxiv.org/html/2602.16862v1#bib.bib12 "Robust control and model uncertainty")), where agents hedge against model misspecification. Our robustness comes from the entropy penalty rather than explicit minimax over a model set.

This paper considers the intersection: entropy-regularized control when drift is unknown. The interaction produces behavior absent from either model individually. In this framework, entropy regularization and Bayesian learning are orthogonal, yet the combination creates a counterintuitive belief-dependent policy variance.

### 1.1 Main Results

1. 1.

   Gaussian policies remain optimal. Under partial information, the optimal policy is Gaussian with mean and variance determined by value function derivatives (Lemma [3.1](https://arxiv.org/html/2602.16862v1#S3.Thmtheorem1 "Lemma 3.1 (Optimal policy is Gaussian). ‣ 3.3 Gaussian Optimality ‣ 3 HJB Equation and Optimal Policy ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")).
2. 2.

   Quadratic-in-wealth structure survives. A value function quadratic in wealth reduces the HJB to a semilinear PDE system. Following De Franco et al. ([2018](https://arxiv.org/html/2602.16862v1#bib.bib5 "Bayesian learning for the Markowitz portfolio selection problem")), exponential substitution gives closed-form solutions for Gaussian priors.
3. 3.

   Consistency with limiting cases. When prior uncertainty vanishes (P0→0P\_{0}\to 0), we recover Wang and Zhou ([2019](https://arxiv.org/html/2602.16862v1#bib.bib6 "Continuous-time mean–variance portfolio selection: a reinforcement learning framework")). When entropy regularization vanishes (τ→0\tau\to 0), we recover De Franco et al. ([2018](https://arxiv.org/html/2602.16862v1#bib.bib5 "Bayesian learning for the Markowitz portfolio selection problem")).
4. 4.

   Orthogonality of entropy and learning. Posterior dynamics are policy independent, so entropy regularization cannot accelerate learning about ρ\rho. The mean control is identical to the deterministic Bayesian Markowitz feedback of De Franco et al. ([2018](https://arxiv.org/html/2602.16862v1#bib.bib5 "Bayesian learning for the Markowitz portfolio selection problem")); entropy regularization affects only the policy variance.
5. 5.

   Conviction driven policy variance. The optimal policy variance increases with posterior conviction |mt||m\_{t}| (the magnitude of the drift estimate, not the posterior precision PtP\_{t}). The entropy penalty forces greater action randomization when the mean position is most aggressive, acting as a robustness mechanism against aggressive positioning under model risk (Proposition [6.1](https://arxiv.org/html/2602.16862v1#S6.Thmtheorem1 "Proposition 6.1 (Belief-dependent variance). ‣ 6.1 Conviction Driven Variance ‣ 6 Belief-dependent Policy Variance ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")).

###### Remark 1.1 (Role of Entropy Regularization).

Like in Wang and Zhou ([2019](https://arxiv.org/html/2602.16862v1#bib.bib6 "Continuous-time mean–variance portfolio selection: a reinforcement learning framework")), entropy regularization yields explicit Gaussian policies and connects to relaxed stochastic control. The weight τ\tau controls the degree of policy randomization; larger τ\tau favors softer (more spread out) controls.

|  | Known drift (P0=0P\_{0}=0) | Unknown drift (P0>0P\_{0}>0) |
| --- | --- | --- |
| Deterministic (τ=0\tau=0) | Classical MV | De Franco et al. ([2018](https://arxiv.org/html/2602.16862v1#bib.bib5 "Bayesian learning for the Markowitz portfolio selection problem")) |
| Entropy-regularized (τ>0\tau>0) | Wang and Zhou ([2019](https://arxiv.org/html/2602.16862v1#bib.bib6 "Continuous-time mean–variance portfolio selection: a reinforcement learning framework")) | This paper |

### 1.2 Notation

| Market | |
| --- | --- |
| StS\_{t} | Risky asset price |
| μ,σ,r\mu,\sigma,r | Drift (unknown), volatility (known), risk-free rate |
| ρ\rho | Sharpe ratio (μ−r)/σ(\mu-r)/\sigma (unknown) |
| WtW\_{t} | Brownian motion driving prices |
| TT | Investment horizon |
| Filtering | |
| mtm\_{t} | Posterior mean of ρ\rho given observations up to time tt |
| PtP\_{t} | Posterior variance of ρ\rho given observations up to time tt |
| m0,P0m\_{0},P\_{0} | Prior mean and variance of ρ\rho |
| W^t\widehat{W}\_{t} | Innovation process (Brownian motion adapted to observations) |
| Control | |
| XtX\_{t} | Discounted wealth |
| utu\_{t} | Position in risky asset (discounted dollars) |
| πt\pi\_{t} | Policy: probability distribution over positions at time tt |
| u¯,ς2\bar{u},\varsigma^{2} | Mean and variance of policy π\pi |
| ww | Target wealth level |
| τ\tau | Entropy weight (regularization parameter) |
| H​(π)H(\pi) | Negative of differential entropy: ∫π​(u)​log⁡π​(u)​𝑑u\int\pi(u)\log\pi(u)\,du |
| Value Function | |
| VV | Value function V​(t,x,m,P)V(t,x,m,P) |
| A,B,CA,B,C | Coefficients in ansatz V=A​x2+B​x+CV=Ax^{2}+Bx+C |
| α,γ\alpha,\gamma | Functions of tt in closed-form A=eα​m2+γA=e^{\alpha m^{2}+\gamma} |

## 2 Problem Formulation

### 2.1 Market Model

Consider a market with a risk-free asset earning rate rr and a risky asset with price dynamics

|  |  |  |
| --- | --- | --- |
|  | d​StSt=μ​d​t+σ​d​Wt,\frac{dS\_{t}}{S\_{t}}=\mu\,dt+\sigma\,dW\_{t}, |  |

where σ>0\sigma>0 is known and μ\mu is unknown. We parameterize the unknown drift by the Sharpe ratio ρ:=μ−rσ\rho:=\frac{\mu-r}{\sigma}.

###### Assumption 2.1.

The Sharpe ratio ρ\rho is independent of WW and has Gaussian prior: ρ∼𝒩​(m0,P0)\rho\sim\mathcal{N}(m\_{0},P\_{0}).

We work under the physical measure and model the excess drift μ−r\mu-r as constant but unknown. The investor’s uncertainty is captured by the prior on ρ\rho.

### 2.2 Bayesian Filtering

The investor observes prices but not ρ\rho directly. Define the *whitened* cumulative excess return

|  |  |  |
| --- | --- | --- |
|  | Yt:=∫0t1σ​(d​SsSs−r​d​s),Y\_{t}:=\int\_{0}^{t}\frac{1}{\sigma}\left(\frac{dS\_{s}}{S\_{s}}-r\,ds\right), |  |

which satisfies d​Yt=ρ​d​t+d​WtdY\_{t}=\rho\,dt+dW\_{t}. Let ℱt:=σ(Ys:s≤t)\mathcal{F}\_{t}:=\sigma(Y\_{s}:s\leq t) be the observation filtration, and define the posterior moments

|  |  |  |
| --- | --- | --- |
|  | mt:=𝔼​[ρ∣ℱt],Pt:=Var⁡(ρ∣ℱt).m\_{t}:=\mathbb{E}[\rho\mid\mathcal{F}\_{t}],\qquad P\_{t}:=\operatorname{Var}(\rho\mid\mathcal{F}\_{t}). |  |

###### Proposition 2.2 (Posterior dynamics).

The posterior remains Gaussian: ρ∣ℱt∼𝒩​(mt,Pt)\rho\mid\mathcal{F}\_{t}\sim\mathcal{N}(m\_{t},P\_{t}), with dynamics

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​mt\displaystyle dm\_{t} | =Pt​d​W^t,\displaystyle=P\_{t}\,d\widehat{W}\_{t}, |  | (1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Pt\displaystyle dP\_{t} | =−Pt2​d​t,\displaystyle=-P\_{t}^{2}\,dt, |  | (2) |

where the innovation d​W^t:=d​Yt−mt​d​td\widehat{W}\_{t}:=dY\_{t}-m\_{t}\,dt is a Brownian motion in ℱt\mathcal{F}\_{t}. The posterior variance has closed-form Pt=P01+P0​tP\_{t}=\frac{P\_{0}}{1+P\_{0}t}.

This result follows from standard Kalman–Bucy filtering. Three features stand out:

1. 1.

   PtP\_{t} is deterministic (uncertainty decays at rate O​(1t)O(\frac{1}{t}) regardless of observations).
2. 2.

   mtm\_{t} is a martingale converging a.s. to ρ\rho.
3. 3.

   Posterior dynamics ([1](https://arxiv.org/html/2602.16862v1#S2.E1 "In Proposition 2.2 (Posterior dynamics). ‣ 2.2 Bayesian Filtering ‣ 2 Problem Formulation ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"))–([2](https://arxiv.org/html/2602.16862v1#S2.E2 "In Proposition 2.2 (Posterior dynamics). ‣ 2.2 Bayesian Filtering ‣ 2 Problem Formulation ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) depend on the observation process YY, not the control policy π\pi. Learning is policy independent.

### 2.3 Wealth Dynamics and Bilinear Structure

Let Xt:=e−r​t​X¯tX\_{t}:=e^{-rt}\bar{X}\_{t} be discounted wealth and utu\_{t} the discounted dollar position in the risky asset. Using the innovation decomposition d​Wt=d​W^t−(ρ−mt)​d​tdW\_{t}=d\widehat{W}\_{t}-(\rho-m\_{t})\,dt:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=σ​ut​(mt​d​t+d​W^t).dX\_{t}=\sigma u\_{t}(m\_{t}\,dt+d\widehat{W}\_{t}). |  | (3) |

The drift σ​mt​ut\sigma m\_{t}u\_{t} is bilinear, a product of belief and control. This is the break from classical LQG, where drift is affine in state and control separately. The bilinear structure has two consequences: it prevents the HJB equation from closing into Riccati ODEs (see Proposition [4.1](https://arxiv.org/html/2602.16862v1#S4.Thmtheorem1 "Proposition 4.1 (Polynomial impossibility). ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")), and thus requires the exponential substitution of Section [4.2](https://arxiv.org/html/2602.16862v1#S4.SS2 "4.2 Closed-form Solution ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty").

Under the observation filtration, the pair (Xt,mt)(X\_{t},m\_{t}) is Markov, with PtP\_{t} as a deterministic time-dependent parameter. Through filtering, we have gone from partial information to a fully observed Markov control problem.

### 2.4 Entropy-Regularized Objective

Following Wang and Zhou ([2019](https://arxiv.org/html/2602.16862v1#bib.bib6 "Continuous-time mean–variance portfolio selection: a reinforcement learning framework")), we replace the pointwise control utu\_{t} with a stochastic policy πt\pi\_{t}, a probability distribution over positions.

###### Definition 2.3 (Admissible policy).

An admissible policy is a progressively measurable family {πt}t∈[0,T]\{\pi\_{t}\}\_{t\in[0,T]} of probability densities on ℝ\mathbb{R} satisfying 𝔼​[∫0T∫ℝu2​πt​(u)​𝑑u​𝑑t]<∞\mathbb{E}\!\left[\int\_{0}^{T}\int\_{\mathbb{R}}u^{2}\pi\_{t}(u)\,du\,dt\right]<\infty.

We work at the generator level, where the controlled dynamics depend on π\pi only through its moments; this is the relaxed control formulation of Wang and Zhou ([2019](https://arxiv.org/html/2602.16862v1#bib.bib6 "Continuous-time mean–variance portfolio selection: a reinforcement learning framework")).

The entropy-regularized value function is

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,x,m,P)=infπ𝔼​[(XT−w)2+τ​∫tTH​(πs)​𝑑s|Xt=x,mt=m,Pt=P],V(t,x,m,P)=\inf\_{\pi}\mathbb{E}\!\left[(X\_{T}-w)^{2}+\tau\int\_{t}^{T}H(\pi\_{s})\,ds\;\Big|\;X\_{t}=x,m\_{t}=m,P\_{t}=P\right], |  | (4) |

where w∈ℝw\in\mathbb{R} is the target wealth level, τ>0\tau>0 is the entropy weight, and H​(π):=∫π​(u)​log⁡π​(u)​𝑑uH(\pi):=\int\pi(u)\log\pi(u)\,du is the negative of differential entropy. Following the classical embedding of Zhou and Li ([2000](https://arxiv.org/html/2602.16862v1#bib.bib4 "Continuous-time mean-variance portfolio selection: a stochastic LQ framework")), ww plays the role of a Lagrange multiplier for the mean constraint 𝔼​[XT]=z\mathbb{E}[X\_{T}]=z, and sweeping ww traces the efficient frontier.

The entropy term penalizes concentrated policies. As τ→0\tau\to 0, we recover the deterministic Bayesian Markowitz problem of De Franco et al. ([2018](https://arxiv.org/html/2602.16862v1#bib.bib5 "Bayesian learning for the Markowitz portfolio selection problem")).

## 3 HJB Equation and Optimal Policy

### 3.1 Generator

Under policy πt\pi\_{t} with mean u¯\bar{u} and variance ς2\varsigma^{2}, the generator of any smooth φ​(t,x,m,P)\varphi(t,x,m,P) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒπ​φ=σ​u¯​m​φx+σ22​(u¯2+ς2)​φx​x+σ​u¯​P​φx​m+P22​φm​m−P2​φP.\mathcal{L}^{\pi}\varphi=\sigma\bar{u}m\,\varphi\_{x}+\frac{\sigma^{2}}{2}(\bar{u}^{2}+\varsigma^{2})\varphi\_{xx}+\sigma\bar{u}P\,\varphi\_{xm}+\frac{P^{2}}{2}\varphi\_{mm}-P^{2}\varphi\_{P}. |  | (5) |

The policy only enters through its first two moments. The φx​x\varphi\_{xx} term involves 𝔼π​[u2]=u¯2+ς2\mathbb{E}\_{\pi}[u^{2}]=\bar{u}^{2}+\varsigma^{2} because (d​X)2=σ2​u2​d​t(dX)^{2}=\sigma^{2}u^{2}\,dt, and averaging over π\pi retains both moments. The mixed term φx​m\varphi\_{xm} involves u¯\bar{u} only, because d​X​d​m=σ​u​Pt​d​tdX\,dm=\sigma uP\_{t}\,dt is linear in uu, so averaging over π\pi only sees the mean. Randomizing the control introduces additional diffusion in wealth that is conditionally independent of the innovation d​W^td\widehat{W}\_{t}, contributing to (d​X)2(dX)^{2} but not to the covariance d​X​d​mdX\,dm.

### 3.2 HJB Equation

Since (Xt,mt,Pt)(X\_{t},m\_{t},P\_{t}) is Markov under the observation filtration (with PtP\_{t} deterministic), the dynamic programming principle applies. The HJB equation is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tV+infπ{ℒπ​V+τ​H​(π)}=0,V​(T,x,m,P)=(x−w)2.\partial\_{t}V+\inf\_{\pi}\left\{\mathcal{L}^{\pi}V+\tau H(\pi)\right\}=0,\qquad V(T,x,m,P)=(x-w)^{2}. |  | (6) |

### 3.3 Gaussian Optimality

###### Lemma 3.1 (Optimal policy is Gaussian).

Suppose V∈C1,2V\in C^{1,2} with Vx​x>0V\_{xx}>0. The optimal policy is π∗=𝒩​(u¯∗,ς∗2)\pi^{\*}=\mathcal{N}(\bar{u}^{\*},\varsigma^{\*2}) with

|  |  |  |  |
| --- | --- | --- | --- |
|  | u¯∗=−m​Vx+P​Vx​mσ​Vx​x,ς∗2=τσ2​Vx​x.\bar{u}^{\*}=-\frac{mV\_{x}+PV\_{xm}}{\sigma V\_{xx}},\qquad\varsigma^{\*2}=\frac{\tau}{\sigma^{2}V\_{xx}}. |  | (7) |

###### Proof.

The π\pi-dependent terms in ℒπ​V+τ​H​(π)\mathcal{L}^{\pi}V+\tau H(\pi) are

|  |  |  |
| --- | --- | --- |
|  | Φ​(π):=σ​u¯​(m​Vx+P​Vx​m)+σ22​(u¯2+ς2)​Vx​x+τ​H​(π).\Phi(\pi):=\sigma\bar{u}(mV\_{x}+PV\_{xm})+\frac{\sigma^{2}}{2}(\bar{u}^{2}+\varsigma^{2})V\_{xx}+\tau H(\pi). |  |

Taking the first variation under ∫π=1\int\pi=1 gives

|  |  |  |
| --- | --- | --- |
|  | log⁡π∗​(u)+1+1τ​(σ​u​(m​Vx+P​Vx​m)+σ2​u22​Vx​x)=const.\log\pi^{\*}(u)+1+\frac{1}{\tau}\left(\sigma u(mV\_{x}+PV\_{xm})+\frac{\sigma^{2}u^{2}}{2}V\_{xx}\right)=\text{const}. |  |

The exponent is quadratic in uu, so π∗\pi^{\*} is Gaussian. Completing the square gives the stated mean and variance.

□\square

###### Remark 3.2 (Mean-variance separation).

The optimal policy separates cleanly: the mean u¯∗\bar{u}^{\*} depends on beliefs and value gradients, while the variance ς∗2\varsigma^{\*2} depends only on the curvature Vx​xV\_{xx} and the entropy weight τ\tau. The coupling term P​Vx​mPV\_{xm} in the mean is new relative to Wang and Zhou ([2019](https://arxiv.org/html/2602.16862v1#bib.bib6 "Continuous-time mean–variance portfolio selection: a reinforcement learning framework")) and reflects the influence of drift uncertainty on the optimal position. Notably, the mean control is independent of τ\tau; entropy regularization affects only the policy variance, not the optimal mean action.

### 3.4 Reduced HJB

Substituting the Gaussian optimizer into ([6](https://arxiv.org/html/2602.16862v1#S3.E6 "In 3.2 HJB Equation ‣ 3 HJB Equation and Optimal Policy ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=Vt+P22​Vm​m−P2​VP−(m​Vx+P​Vx​m)22​Vx​x−τ2​log⁡(2​π​τσ2​Vx​x),0=V\_{t}+\frac{P^{2}}{2}V\_{mm}-P^{2}V\_{P}-\frac{(mV\_{x}+PV\_{xm})^{2}}{2V\_{xx}}-\frac{\tau}{2}\log\!\left(\frac{2\pi\tau}{\sigma^{2}V\_{xx}}\right), |  | (8) |

with terminal condition V​(T,x,m,P)=(x−w)2V(T,x,m,P)=(x-w)^{2}.

## 4 Value Function Structure

In classical LQG and Wang and Zhou ([2019](https://arxiv.org/html/2602.16862v1#bib.bib6 "Continuous-time mean–variance portfolio selection: a reinforcement learning framework")), the value function is polynomial
in the state and the HJB closes into Riccati ODEs. The bilinear drift
σ​mt​ut\sigma m\_{t}u\_{t} prevents this here; the nonlinear term
(m​Vx+P​Vx​m)2Vx​x\frac{(mV\_{x}+PV\_{xm})^{2}}{V\_{xx}} increases the degree in mm faster
than the linear PDE terms can cancel.

###### Proposition 4.1 (Polynomial impossibility).

No polynomial ansatz in (x,m)(x,m) of finite degree satisfies the reduced HJB ([8](https://arxiv.org/html/2602.16862v1#S3.E8 "In 3.4 Reduced HJB ‣ 3 HJB Equation and Optimal Policy ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")). (See Appendix [A](https://arxiv.org/html/2602.16862v1#A1 "Appendix A Proof of Polynomial Impossibility ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty") for the full proof.)

Intuitively, the nonlinear term G2Vx​x\frac{G^{2}}{V\_{xx}} squares the belief-weighted gradient, so each attempt to cap the degree in mm at a finite level is defeated by the HJB nonlinearity.

We therefore seek a solution quadratic in wealth but nonpolynomial in belief.

### 4.1 Quadratic-in-Wealth Ansatz

The terminal condition is quadratic in just xx. Following De Franco et al. ([2018](https://arxiv.org/html/2602.16862v1#bib.bib5 "Bayesian learning for the Markowitz portfolio selection problem")), we seek a solution of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,x,m,P)=A​(t,m,P)​x2+B​(t,m,P)​x+C​(t,m,P),V(t,x,m,P)=A(t,m,P)x^{2}+B(t,m,P)x+C(t,m,P), |  | (9) |

where coefficients depend on beliefs but need not be polynomial in mm. We verify below that this ansatz satisfies the HJB.

###### Proposition 4.2 (Coefficient system).

The ansatz ([9](https://arxiv.org/html/2602.16862v1#S4.E9 "In 4.1 Quadratic-in-Wealth Ansatz ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) satisfies ([8](https://arxiv.org/html/2602.16862v1#S3.E8 "In 3.4 Reduced HJB ‣ 3 HJB Equation and Optimal Policy ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) if and only if (A,B,C)(A,B,C) solve

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =At+P22​Am​m−P2​AP−Γ2A,\displaystyle=A\_{t}+\frac{P^{2}}{2}A\_{mm}-P^{2}A\_{P}-\frac{\Gamma^{2}}{A}, |  | (10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =Bt+P22​Bm​m−P2​BP−Γ​ΛA,\displaystyle=B\_{t}+\frac{P^{2}}{2}B\_{mm}-P^{2}B\_{P}-\frac{\Gamma\Lambda}{A}, |  | (11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =Ct+P22​Cm​m−P2​CP−Λ24​A−τ2​log⁡(π​τσ2​A),\displaystyle=C\_{t}+\frac{P^{2}}{2}C\_{mm}-P^{2}C\_{P}-\frac{\Lambda^{2}}{4A}-\frac{\tau}{2}\log\!\left(\frac{\pi\tau}{\sigma^{2}A}\right), |  | (12) |

where Γ:=m​A+P​Am\Gamma:=mA+PA\_{m} and Λ:=m​B+P​Bm\Lambda:=mB+PB\_{m}, with terminal conditions A​(T)=1A(T)=1, B​(T)=−2​wB(T)=-2w, C​(T)=w2C(T)=w^{2}.

The system is triangular: ([10](https://arxiv.org/html/2602.16862v1#S4.E10 "In Proposition 4.2 (Coefficient system). ‣ 4.1 Quadratic-in-Wealth Ansatz ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) is closed in AA; given AA, ([11](https://arxiv.org/html/2602.16862v1#S4.E11 "In Proposition 4.2 (Coefficient system). ‣ 4.1 Quadratic-in-Wealth Ansatz ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) is linear in BB; given (A,B)(A,B), ([12](https://arxiv.org/html/2602.16862v1#S4.E12 "In Proposition 4.2 (Coefficient system). ‣ 4.1 Quadratic-in-Wealth Ansatz ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) is linear in CC.

###### Proposition 4.3 (ww-separation).

Within the system ([10](https://arxiv.org/html/2602.16862v1#S4.E10 "In Proposition 4.2 (Coefficient system). ‣ 4.1 Quadratic-in-Wealth Ansatz ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"))–([12](https://arxiv.org/html/2602.16862v1#S4.E12 "In Proposition 4.2 (Coefficient system). ‣ 4.1 Quadratic-in-Wealth Ansatz ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")): (i) AA is independent of ww; (ii) B=−2​w​AB=-2wA; (iii) writing C=w2​A+DC=w^{2}A+D, the function DD is independent of ww and satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=Dt+P22​Dm​m−P2​DP−τ2​log⁡(π​τσ2​A),D​(T)=0.0=D\_{t}+\frac{P^{2}}{2}D\_{mm}-P^{2}D\_{P}-\frac{\tau}{2}\log\!\left(\frac{\pi\tau}{\sigma^{2}A}\right),\qquad D(T)=0. |  | (13) |

So the problem reduces to solving ([10](https://arxiv.org/html/2602.16862v1#S4.E10 "In Proposition 4.2 (Coefficient system). ‣ 4.1 Quadratic-in-Wealth Ansatz ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) for AA, then ([13](https://arxiv.org/html/2602.16862v1#S4.E13 "In Proposition 4.3 (𝑤-separation). ‣ 4.1 Quadratic-in-Wealth Ansatz ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) for DD.

### 4.2 Closed-form Solution

Since Pt=P01+P0​tP\_{t}=\frac{P\_{0}}{1+P\_{0}t} is deterministic, we can write A​(t,m):=A​(t,m,Pt)A(t,m):=A(t,m,P\_{t}) along the characteristic d​P=−P2​d​tdP=-P^{2}\,dt, reducing the coefficient system to two dimensions (t,m)(t,m). Following De Franco et al. ([2018](https://arxiv.org/html/2602.16862v1#bib.bib5 "Bayesian learning for the Markowitz portfolio selection problem")), Section 4.3.2, the exponential substitution A=eRA=e^{R} transforms ([10](https://arxiv.org/html/2602.16862v1#S4.E10 "In Proposition 4.2 (Coefficient system). ‣ 4.1 Quadratic-in-Wealth Ansatz ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) into a semilinear PDE which admits a quadratic solution R​(t,m)=α​(t)​m2+γ​(t)R(t,m)=\alpha(t)m^{2}+\gamma(t).

###### Proposition 4.4 (Closed-form solution).

For Gaussian priors, A​(t,m)=eα​(t)​m2+γ​(t)A(t,m)=e^{\alpha(t)m^{2}+\gamma(t)} with

|  |  |  |  |
| --- | --- | --- | --- |
|  | α​(t)=−(1+P0​t)​(T−t)1+P0​(2​T−t),\alpha(t)=-\frac{(1+P\_{0}t)(T-t)}{1+P\_{0}(2T-t)}, |  | (14) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ​(t)=∫tTPs2​α​(s)​𝑑s=12​log⁡((1+P0​t)​(1+P0​(2​T−t))(1+P0​T)2).\gamma(t)=\int\_{t}^{T}P\_{s}^{2}\alpha(s)\,ds=\frac{1}{2}\log\!\left(\frac{(1+P\_{0}t)(1+P\_{0}(2T-t))}{(1+P\_{0}T)^{2}}\right). |  | (15) |

###### Proof sketch.

With A=eα​m2+γA=e^{\alpha m^{2}+\gamma} and P=PtP=P\_{t} deterministic, the AA-PDE reduces to matching coefficients:

|  |  |  |  |
| --- | --- | --- | --- |
|  | m2​-terms:\displaystyle m^{2}\text{-terms:} | α′=1+4​Pt​α+2​Pt2​α2,α​(T)=0,\displaystyle\quad\alpha^{\prime}=1+4P\_{t}\alpha+2P\_{t}^{2}\alpha^{2},\quad\alpha(T)=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | m0​-terms:\displaystyle m^{0}\text{-terms:} | γ′=−Pt2​α,γ​(T)=0.\displaystyle\quad\gamma^{\prime}=-P\_{t}^{2}\alpha,\quad\gamma(T)=0. |  |

The α\alpha-equation is a Riccati ODE solved by the stated formula. Integrating γ′=−Pt2​α\gamma^{\prime}=-P\_{t}^{2}\alpha from tt to TT with terminal condition γ​(T)=0\gamma(T)=0 gives γ​(t)=∫tTPs2​α​(s)​𝑑s\gamma(t)=\int\_{t}^{T}P\_{s}^{2}\alpha(s)\,ds. The closed-form follows by direct integration.

□\square

###### Remark 4.5 (τ\tau independence of AA).

The entropy weight τ\tau does not appear in AA or α\alpha; it enters in the DD equation only. This is because AA determines the value function curvature Vx​x=2​AV\_{xx}=2A, but AA itself is determined by the underlying Bayesian Markowitz problem, not by the choice to randomize. Since α​(t)<0\alpha(t)<0 and γ​(t)<0\gamma(t)<0 for t<Tt<T, we have A​(t,m)<1A(t,m)<1 whenever m≠0m\neq 0. Drift uncertainty reduces the value function curvature Vx​x=2​AV\_{xx}=2A relative
to the terminal condition.

The formula for α\alpha becomes more interpretable when written in terms of current posterior variance:

|  |  |  |
| --- | --- | --- |
|  | α​(t)=−T−t1+2​Pt​(T−t),\alpha(t)=-\frac{T-t}{1+2P\_{t}(T-t)}, |  |

which makes the dependence on time-to-go and current uncertainty explicit.

### 4.3 The Entropy Premium

Proposition [4.3](https://arxiv.org/html/2602.16862v1#S4.Thmtheorem3 "Proposition 4.3 (𝑤-separation). ‣ 4.1 Quadratic-in-Wealth Ansatz ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty") reduced the problem to solving ([13](https://arxiv.org/html/2602.16862v1#S4.E13 "In Proposition 4.3 (𝑤-separation). ‣ 4.1 Quadratic-in-Wealth Ansatz ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) for DD. Since PtP\_{t} is deterministic, we work along the characteristic and write D~​(t,m):=D​(t,m,Pt)\tilde{D}(t,m):=D(t,m,P\_{t}). Using d​Ptd​t=−Pt2\frac{dP\_{t}}{dt}=-P\_{t}^{2}, the PDE becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=D~t+Pt22​D~m​m−τ2​log⁡(π​τσ2​A​(t,m)),D~​(T,m)=0.0=\tilde{D}\_{t}+\frac{P\_{t}^{2}}{2}\tilde{D}\_{mm}-\frac{\tau}{2}\log\!\left(\frac{\pi\tau}{\sigma^{2}A(t,m)}\right),\qquad\tilde{D}(T,m)=0. |  | (16) |

Substituting A=eα​m2+γA=e^{\alpha m^{2}+\gamma}, the source term becomes

|  |  |  |
| --- | --- | --- |
|  | log⁡(π​τσ2​A)=log⁡π​τσ2−α​(t)​m2−γ​(t),\log\!\left(\frac{\pi\tau}{\sigma^{2}A}\right)=\log\frac{\pi\tau}{\sigma^{2}}-\alpha(t)m^{2}-\gamma(t), |  |

which is quadratic in mm. This motivates the ansatz D~​(t,m)=η​(t)​m2+ζ​(t)\tilde{D}(t,m)=\eta(t)m^{2}+\zeta(t).

###### Proposition 4.6 (Entropy premium).

The function D​(t,m,Pt)=η​(t)​m2+ζ​(t)D(t,m,P\_{t})=\eta(t)m^{2}+\zeta(t) where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | η​(t)\displaystyle\eta(t) | =τ2​∫tTα​(s)​𝑑s,\displaystyle=\frac{\tau}{2}\int\_{t}^{T}\alpha(s)\,ds, |  | (17) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ζ​(t)\displaystyle\zeta(t) | =−∫tT(τ2​[log⁡π​τσ2−γ​(s)]−Ps2​η​(s))​𝑑s.\displaystyle=-\int\_{t}^{T}\left(\frac{\tau}{2}\left[\log\frac{\pi\tau}{\sigma^{2}}-\gamma(s)\right]-P\_{s}^{2}\,\eta(s)\right)ds. |  | (18) |

Since α​(t)<0\alpha(t)<0 for t<Tt<T, we have η​(t)<0\eta(t)<0 for t<Tt<T.

###### Proof.

Substituting D~=η​m2+ζ\tilde{D}=\eta m^{2}+\zeta into ([16](https://arxiv.org/html/2602.16862v1#S4.E16 "In 4.3 The Entropy Premium ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) and matching coefficients:

|  |  |  |  |
| --- | --- | --- | --- |
|  | m2​-terms:\displaystyle m^{2}\text{-terms:} | η′​(t)=−τ2​α​(t),η​(T)=0,\displaystyle\quad\eta^{\prime}(t)=-\frac{\tau}{2}\alpha(t),\quad\eta(T)=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | m0​-terms:\displaystyle m^{0}\text{-terms:} | ζ′​(t)=τ2​[log⁡π​τσ2−γ​(t)]−Pt2​η​(t),ζ​(T)=0.\displaystyle\quad\zeta^{\prime}(t)=\frac{\tau}{2}\left[\log\frac{\pi\tau}{\sigma^{2}}-\gamma(t)\right]-P\_{t}^{2}\,\eta(t),\quad\zeta(T)=0. |  |

Integrating backward from TT gives ([17](https://arxiv.org/html/2602.16862v1#S4.E17 "In Proposition 4.6 (Entropy premium). ‣ 4.3 The Entropy Premium ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"))–([18](https://arxiv.org/html/2602.16862v1#S4.E18 "In Proposition 4.6 (Entropy premium). ‣ 4.3 The Entropy Premium ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")).

□\square

The complete value function is thus

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,x,m)=eα​(t)​m2+γ​(t)​(x−w)2+η​(t)​m2+ζ​(t).V(t,x,m)=e^{\alpha(t)m^{2}+\gamma(t)}(x-w)^{2}+\eta(t)m^{2}+\zeta(t). |  | (19) |

###### Remark 4.7 (Policy independence of entropy premium).

The entropy premium D=η​m2+ζD=\eta m^{2}+\zeta is independent of wealth xx. Since the optimal policy ([7](https://arxiv.org/html/2602.16862v1#S3.E7 "In Lemma 3.1 (Optimal policy is Gaussian). ‣ 3.3 Gaussian Optimality ‣ 3 HJB Equation and Optimal Policy ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) depends only on VxV\_{x} and Vx​xV\_{xx}, which involve only AA, the function DD does not affect optimal behavior. It captures the expected cost of entropy regularization, not a guide to action.

### 4.4 Optimal Policy in closed-form

Using Lemma [3.1](https://arxiv.org/html/2602.16862v1#S3.Thmtheorem1 "Lemma 3.1 (Optimal policy is Gaussian). ‣ 3.3 Gaussian Optimality ‣ 3 HJB Equation and Optimal Policy ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty") with Vx​x=2​AV\_{xx}=2A and B=−2​w​AB=-2wA:

|  |  |  |  |
| --- | --- | --- | --- |
|  | u¯∗=−m​(1+2​Pt​α)σ​(x−w),ς∗2=τ2​σ2​A.\bar{u}^{\*}=-\frac{m(1+2P\_{t}\alpha)}{\sigma}(x-w),\qquad\varsigma^{\*2}=\frac{\tau}{2\sigma^{2}A}. |  | (20) |

The mean control is linear in tracking error (x−w)(x-w) with belief-dependent gain. The policy variance depends on (t,m)(t,m) through A​(t,m)A(t,m), but is independent of wealth xx and target ww.

###### Remark 4.8 (Verification).

The candidate value function ([19](https://arxiv.org/html/2602.16862v1#S4.E19 "In 4.3 The Entropy Premium ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) is a classical solution to the HJB equation ([8](https://arxiv.org/html/2602.16862v1#S3.E8 "In 3.4 Reduced HJB ‣ 3 HJB Equation and Optimal Policy ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")). Standard verification arguments (see Pham ([2009](https://arxiv.org/html/2602.16862v1#bib.bib13 "Continuous-time stochastic control and optimization with financial applications")), Theorem 3.5.2); apply Itô’s formula to V​(t,Xt,mt)V(t,X\_{t},m\_{t}) and confirm that VV is a supermartingale under any admissible policy and a martingale under the optimal one. Then confirm that it equals the value function ([4](https://arxiv.org/html/2602.16862v1#S2.E4 "In 2.4 Entropy-Regularized Objective ‣ 2 Problem Formulation ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")), given the optimal wealth process satisfies the integrability condition in Definition [2.3](https://arxiv.org/html/2602.16862v1#S2.Thmtheorem3 "Definition 2.3 (Admissible policy). ‣ 2.4 Entropy-Regularized Objective ‣ 2 Problem Formulation ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"). The Gaussian form of the optimal policy and the exponential-quadratic structure of AA ensure this holds for finite TT.

## 5 Limiting Cases

We verify consistency with existing results in two limits.

### 5.1 Known Drift: P0→0P\_{0}\to 0

When P0→0P\_{0}\to 0, the posterior collapses: Pt≡0P\_{t}\equiv 0 and mt≡m0=:ρm\_{t}\equiv m\_{0}=:\rho. From ([14](https://arxiv.org/html/2602.16862v1#S4.E14 "In Proposition 4.4 (Closed-form solution). ‣ 4.2 Closed-form Solution ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")), α​(t)→−(T−t)\alpha(t)\to-(T-t). From ([15](https://arxiv.org/html/2602.16862v1#S4.E15 "In Proposition 4.4 (Closed-form solution). ‣ 4.2 Closed-form Solution ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")), γ​(t)→0\gamma(t)\to 0 since Ps→0P\_{s}\to 0. Thus A​(t)→e−(T−t)​ρ2A(t)\to e^{-(T-t)\rho^{2}}.

The reduced HJB becomes

|  |  |  |
| --- | --- | --- |
|  | 0=Vt−ρ2​Vx22​Vx​x−τ2​log⁡(2​π​τσ2​Vx​x),0=V\_{t}-\frac{\rho^{2}V\_{x}^{2}}{2V\_{xx}}-\frac{\tau}{2}\log\!\left(\frac{2\pi\tau}{\sigma^{2}V\_{xx}}\right), |  |

and the optimal policy is

|  |  |  |
| --- | --- | --- |
|  | u¯∗=−ρσ​(x−w),ς∗2=τ2​σ2​eρ2​(T−t),\bar{u}^{\*}=-\frac{\rho}{\sigma}(x-w),\qquad\varsigma^{\*2}=\frac{\tau}{2\sigma^{2}}e^{\rho^{2}(T-t)}, |  |

recovering Wang and Zhou ([2019](https://arxiv.org/html/2602.16862v1#bib.bib6 "Continuous-time mean–variance portfolio selection: a reinforcement learning framework")), Theorem 1.

### 5.2 Deterministic Control: τ→0\tau\to 0

When τ→0\tau\to 0, the policy variance ς∗2=τ2​σ2​A→0\varsigma^{\*2}=\frac{\tau}{2\sigma^{2}A}\to 0. The policy collapses to deterministic feedback:

|  |  |  |
| --- | --- | --- |
|  | u∗=u¯∗=−m​(1+2​Pt​α)σ​(x−w).u^{\*}=\bar{u}^{\*}=-\frac{m(1+2P\_{t}\alpha)}{\sigma}(x-w). |  |

This matches the deterministic feedback control in De Franco et al. ([2018](https://arxiv.org/html/2602.16862v1#bib.bib5 "Bayesian learning for the Markowitz portfolio selection problem")), and the framework consistently interpolates between the two known cases.

## 6 Belief-dependent Policy Variance

Sections [3](https://arxiv.org/html/2602.16862v1#S3 "3 HJB Equation and Optimal Policy ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")–[4](https://arxiv.org/html/2602.16862v1#S4 "4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty") established that entropy regularization leaves the mean control and value function curvature unchanged; it enters only through the policy variance and the additive entropy premium DD. Particularly, the posterior dynamics ([1](https://arxiv.org/html/2602.16862v1#S2.E1 "In Proposition 2.2 (Posterior dynamics). ‣ 2.2 Bayesian Filtering ‣ 2 Problem Formulation ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"))–([2](https://arxiv.org/html/2602.16862v1#S2.E2 "In Proposition 2.2 (Posterior dynamics). ‣ 2.2 Bayesian Filtering ‣ 2 Problem Formulation ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) are functions of the observation process alone, so randomizing the control policy cannot accelerate learning about ρ\rho. The mean action is identical to De Franco et al. ([2018](https://arxiv.org/html/2602.16862v1#bib.bib5 "Bayesian learning for the Markowitz portfolio selection problem")); entropy regularization adds only a policy variance and an additive value correction.

Then why entropy regularization? We now turn to the structure of the policy variance, which is the primary contribution of the combined model.

### 6.1 Conviction Driven Variance

Recall from ([20](https://arxiv.org/html/2602.16862v1#S4.E20 "In 4.4 Optimal Policy in closed-form ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) that the optimal policy variance is ς∗2​(t,m)=τ2​σ2​A​(t,m)\varsigma^{\*2}(t,m)=\frac{\tau}{2\sigma^{2}A(t,m)} with A=eα​(t)​m2+γ​(t)A=e^{\alpha(t)m^{2}+\gamma(t)}.

###### Proposition 6.1 (Belief-dependent variance).

Under Assumption [2.1](https://arxiv.org/html/2602.16862v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2.1 Market Model ‣ 2 Problem Formulation ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty") with τ>0\tau>0 and T<∞T<\infty, the optimal policy variance ς∗2​(t,m)\varsigma^{\*2}(t,m) is: symmetric in mm, minimized at m=0m=0, and strictly increasing in |m||m| for |m|>0|m|>0 at each fixed t<Tt<T.

Stronger posterior conviction (larger |m||m|, the magnitude of the drift estimate, not posterior precision PtP\_{t}) implies greater policy randomization.

###### Proof.

From ([20](https://arxiv.org/html/2602.16862v1#S4.E20 "In 4.4 Optimal Policy in closed-form ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")),

|  |  |  |
| --- | --- | --- |
|  | ς∗2​(t,m)=τ2​σ2​e−α​(t)​m2−γ​(t).\varsigma^{\*2}(t,m)=\frac{\tau}{2\sigma^{2}}\,e^{-\alpha(t)m^{2}-\gamma(t)}. |  |

This depends on mm only through m2m^{2}, giving symmetry. Differentiating in mm:

|  |  |  |
| --- | --- | --- |
|  | ∂ς∗2∂m=−2​α​(t)​m​ς∗2​(t,m).\frac{\partial\,\varsigma^{\*2}}{\partial m}=-2\alpha(t)\,m\,\varsigma^{\*2}(t,m). |  |

By Proposition [4.4](https://arxiv.org/html/2602.16862v1#S4.Thmtheorem4 "Proposition 4.4 (Closed-form solution). ‣ 4.2 Closed-form Solution ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"), α​(t)<0\alpha(t)<0 for t<Tt<T, so −2​α​(t)>0-2\alpha(t)>0. The derivative has the same sign as mm; negative for m<0m<0, zero at m=0m=0, positive for m>0m>0. Hence ς∗2\varsigma^{\*2} is minimized at m=0m=0 and strictly increasing in |m||m| for |m|>0|m|>0.

□\square

### 6.2 Comparison with RL

| Framework | Policy variance | Belief dependence |
| --- | --- | --- |
| Entropy-regularized RL | Decreases with certainty | Uncertainty driven |
| This paper | τ2​σ2​e−α​(t)​m2−γ​(t)\displaystyle\frac{\tau}{2\sigma^{2}}\,e^{-\alpha(t)m^{2}-\gamma(t)} | Increases with |m||m| |

In standard RL, randomization decreases as the agent becomes more certain about the environment, because the purpose of randomization is to gather information. Here the relation is reversed; the agent randomizes more when it is more convinced about the drift direction.

### 6.3 Economic Interpretation

When |m||m| is large, the certainty-equivalent mean control u¯∗∝m​(x−w)\bar{u}^{\*}\propto m(x-w) prescribes an aggressive position. And structurally:

|  |  |  |
| --- | --- | --- |
|  | |m|​ large⇒|u¯∗|​ large⇒A​(t,m)​ small (​α<0​)⇒ς∗2=τ2​σ2​A​ large.|m|\text{ large}\;\Rightarrow\;|\bar{u}^{\*}|\text{ large}\;\Rightarrow\;A(t,m)\text{ small (}\alpha<0\text{)}\;\Rightarrow\;\varsigma^{\*2}=\frac{\tau}{2\sigma^{2}A}\text{ large.} |  |

Entropy regularization forces greater action randomization when the mean position is most aggressive; softening the consequences of acting too strongly on a posterior that may be wrong. This is a robustness mechanism, not an information seeking one. We use robustness here in the informal sense; entropy regularization spreads probability mass across actions when our model prescribes aggressive positions, softening exposure to model error. A formal connection to minimax robustness with KL-ball duality (Hansen and Sargent, [2001](https://arxiv.org/html/2602.16862v1#bib.bib12 "Robust control and model uncertainty")) lies beyond the present scope.

### 6.4 Numerical Illustration

Figure [1](https://arxiv.org/html/2602.16862v1#S6.F1 "Figure 1 ‣ 6.4 Numerical Illustration ‣ 6 Belief-dependent Policy Variance ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty") illustrates the phenomenon with simulated filter paths. We fix the true Sharpe ratio ρ=1.0\rho=1.0 and draw the prior ρ∼𝒩​(0,1)\rho\sim\mathcal{N}(0,1), with T=1T=1, σ=0.2\sigma=0.2, and τ=1.0\tau=1.0. Panel (a) shows five sample paths of the posterior mean mtm\_{t}, which drift toward ρ\rho as observations accumulate. Panel (b) shows the corresponding policy variance ς∗2​(t,mt)\varsigma^{\*2}(t,m\_{t}) along each path. Paths where the filter possesses strong conviction (large |mt||m\_{t}|) have higher policy variance. All paths converge to a common variance at t=Tt=T, where α​(T)=0\alpha(T)=0 and the belief dependence vanishes.

![Refer to caption](x1.png)


Figure 1: (a) Sample posterior mean paths mtm\_{t} under Kalman–Bucy filtering. (b) Optimal policy variance ς∗2​(t,mt)\varsigma^{\*2}(t,m\_{t}) along each path. Stronger conviction (larger |mt||m\_{t}|) produces greater policy randomization. Parameters: P0=1P\_{0}=1, T=1T=1, τ=1\tau=1, σ=0.2\sigma=0.2, ρ=1\rho=1.

Figure [2](https://arxiv.org/html/2602.16862v1#S6.F2 "Figure 2 ‣ 6.4 Numerical Illustration ‣ 6 Belief-dependent Policy Variance ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty") displays the policy variance as a function of (t,m)(t,m) over the full state space. The contour structure is symmetric in mm and confirms that variance is maximized at large |m||m| and early tt, where the combination of strong conviction and long time-to-go makes the mean control most aggressive.

![Refer to caption](x2.png)


Figure 2: Heatmap of optimal policy variance ς∗2​(t,m)\varsigma^{\*2}(t,m) over the (t,m)(t,m) plane. Contour lines are in white. The variance is symmetric in mm, minimized along m=0m=0 (dashed line), increasing with |m||m| at each fixed t<Tt<T, and collapsing to a common value at TT.

## 7 Conclusion

We solved the entropy-regularized mean-variance problem under Bayesian drift uncertainty, obtaining closed-form solutions consistent with both De Franco et al. ([2018](https://arxiv.org/html/2602.16862v1#bib.bib5 "Bayesian learning for the Markowitz portfolio selection problem")) and Wang and Zhou ([2019](https://arxiv.org/html/2602.16862v1#bib.bib6 "Continuous-time mean–variance portfolio selection: a reinforcement learning framework")) as limiting cases. The principal finding is that entropy regularization, though orthogonal to learning in this framework, generates a belief-dependent policy variance that increases with posterior conviction. This acts as a robustness mechanism against aggressive positioning under model risk rather than an information-seeking tool.

Our model is minimal: one risky asset, Gaussian prior, constant volatility, no transaction costs, and no position constraints. These simplifications are what allow us to obtain closed-form solutions, however, they limit direct applicability.

Several extensions are then natural. In the multi-asset setting, all the structure remains, as shown by De Franco et al. ([2018](https://arxiv.org/html/2602.16862v1#bib.bib5 "Bayesian learning for the Markowitz portfolio selection problem")). As noted by Wang and Zhou ([2019](https://arxiv.org/html/2602.16862v1#bib.bib6 "Continuous-time mean–variance portfolio selection: a reinforcement learning framework")) the Gaussian optimal policy means that model-free RL algorithms can be restricted to learn efficiently. Non-Gaussian priors would break the closed-form filtering and require numerical PDE / particle filtering methods; what survives remains an open question.

## References

* N. Bäuerle and U. Rieder (2004)
  Portfolio optimization with Markov-modulated stock prices and interest rates.
  IEEE Transactions on Automatic Control 49 (3),  pp. 442–447.
  External Links: [Document](https://dx.doi.org/10.1109/TAC.2004.824471)
  Cited by: [§1](https://arxiv.org/html/2602.16862v1#S1.p3.1 "1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty").
* S. Brendle (2006)
  Portfolio selection under incomplete information.
  Stochastic Processes and their Applications 116 (5),  pp. 701–723.
  External Links: [Document](https://dx.doi.org/10.1016/j.spa.2005.11.010)
  Cited by: [§1](https://arxiv.org/html/2602.16862v1#S1.p3.1 "1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty").
* C. De Franco, J. Nicolle, and H. Pham (2018)
  Bayesian learning for the Markowitz portfolio selection problem.
  arXiv preprint arXiv:1811.06893.
  Note: Published version: International Journal of Theoretical and Applied Finance, 22(07), 1950037 (2019), DOI: 10.1142/S0219024919500377
  External Links: [Document](https://dx.doi.org/10.48550/arXiv.1811.06893)
  Cited by: [item 1](https://arxiv.org/html/2602.16862v1#S1.I1.i1.p1.1 "In 1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [item 2](https://arxiv.org/html/2602.16862v1#S1.I2.i2.p1.1 "In 1.1 Main Results ‣ 1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [item 3](https://arxiv.org/html/2602.16862v1#S1.I2.i3.p1.2 "In 1.1 Main Results ‣ 1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [item 4](https://arxiv.org/html/2602.16862v1#S1.I2.i4.p1.1 "In 1.1 Main Results ‣ 1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§1.1](https://arxiv.org/html/2602.16862v1#S1.SS1.3.3.3.3 "1.1 Main Results ‣ 1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§1](https://arxiv.org/html/2602.16862v1#S1.p3.1 "1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§2.4](https://arxiv.org/html/2602.16862v1#S2.SS4.p4.1 "2.4 Entropy-Regularized Objective ‣ 2 Problem Formulation ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§4.1](https://arxiv.org/html/2602.16862v1#S4.SS1.p1.1 "4.1 Quadratic-in-Wealth Ansatz ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§4.2](https://arxiv.org/html/2602.16862v1#S4.SS2.p1.6 "4.2 Closed-form Solution ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§5.2](https://arxiv.org/html/2602.16862v1#S5.SS2.p1.3 "5.2 Deterministic Control: 𝜏→0 ‣ 5 Limiting Cases ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§6](https://arxiv.org/html/2602.16862v1#S6.p1.2 "6 Belief-dependent Policy Variance ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§7](https://arxiv.org/html/2602.16862v1#S7.p1.1 "7 Conclusion ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§7](https://arxiv.org/html/2602.16862v1#S7.p3.1 "7 Conclusion ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty").
* L. Garlappi, R. Uppal, and T. Wang (2007)
  Portfolio selection with parameter and model uncertainty: a multi-prior approach.
  The Review of Financial Studies 20 (1),  pp. 41–81.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/hhl003)
  Cited by: [§1](https://arxiv.org/html/2602.16862v1#S1.p3.1 "1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty").
* T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine (2018)
  Soft actor-critic: off-policy maximum entropy deep reinforcement learning with a stochastic actor.
  In Proceedings of the 35th International Conference on Machine Learning (ICML),
   pp. 1861–1870.
  Cited by: [§1](https://arxiv.org/html/2602.16862v1#S1.p3.1 "1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty").
* L. P. Hansen and T. J. Sargent (2001)
  Robust control and model uncertainty.
  American Economic Review 91 (2),  pp. 60–66.
  External Links: [Document](https://dx.doi.org/10.1257/aer.91.2.60)
  Cited by: [§1](https://arxiv.org/html/2602.16862v1#S1.p3.1 "1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§6.3](https://arxiv.org/html/2602.16862v1#S6.SS3.p1.3 "6.3 Economic Interpretation ‣ 6 Belief-dependent Policy Variance ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty").
* P. Lakner (1998)
  Optimal trading strategy for an investor: the case of partial information.
  Stochastic Processes and their Applications 76 (1),  pp. 77–97.
  External Links: [Document](https://dx.doi.org/10.1016/S0304-4149%2898%2900032-5)
  Cited by: [§1](https://arxiv.org/html/2602.16862v1#S1.p3.1 "1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty").
* H. Markowitz (1952)
  Portfolio selection.
  The Journal of Finance 7 (1),  pp. 77–91.
  External Links: [Document](https://dx.doi.org/10.1111/j.1540-6261.1952.tb01525.x)
  Cited by: [§1](https://arxiv.org/html/2602.16862v1#S1.p1.1 "1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty").
* R. C. Merton (1980)
  On estimating the expected return on the market: an exploratory investigation.
  Journal of Financial Economics 8 (4),  pp. 323–361.
  External Links: [Document](https://dx.doi.org/10.1016/0304-405X%2880%2990007-0)
  Cited by: [§1](https://arxiv.org/html/2602.16862v1#S1.p1.1 "1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty").
* H. Pham (2009)
  Continuous-time stochastic control and optimization with financial applications.
  Stochastic Modelling and Applied Probability, Vol. 61, Springer.
  External Links: [Document](https://dx.doi.org/10.1007/978-3-540-89500-8)
  Cited by: [Remark 4.8](https://arxiv.org/html/2602.16862v1#S4.Thmtheorem8.p1.4 "Remark 4.8 (Verification). ‣ 4.4 Optimal Policy in closed-form ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty").
* H. Wang and X. Y. Zhou (2019)
  Continuous-time mean–variance portfolio selection: a reinforcement learning framework.
  arXiv preprint arXiv:1904.11392.
  Note: v2, May 2019
  External Links: [Document](https://dx.doi.org/10.48550/arXiv.1904.11392)
  Cited by: [item 2](https://arxiv.org/html/2602.16862v1#S1.I1.i2.p1.1 "In 1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [item 3](https://arxiv.org/html/2602.16862v1#S1.I2.i3.p1.2 "In 1.1 Main Results ‣ 1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§1.1](https://arxiv.org/html/2602.16862v1#S1.SS1.4.4.4.2 "1.1 Main Results ‣ 1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [Remark 1.1](https://arxiv.org/html/2602.16862v1#S1.Thmtheorem1.p1.2 "Remark 1.1 (Role of Entropy Regularization). ‣ 1.1 Main Results ‣ 1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§1](https://arxiv.org/html/2602.16862v1#S1.p3.1 "1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§2.4](https://arxiv.org/html/2602.16862v1#S2.SS4.p1.2 "2.4 Entropy-Regularized Objective ‣ 2 Problem Formulation ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§2.4](https://arxiv.org/html/2602.16862v1#S2.SS4.p2.1 "2.4 Entropy-Regularized Objective ‣ 2 Problem Formulation ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [Remark 3.2](https://arxiv.org/html/2602.16862v1#S3.Thmtheorem2.p1.6 "Remark 3.2 (Mean-variance separation). ‣ 3.3 Gaussian Optimality ‣ 3 HJB Equation and Optimal Policy ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§4](https://arxiv.org/html/2602.16862v1#S4.p1.3 "4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§5.1](https://arxiv.org/html/2602.16862v1#S5.SS1.p2.3 "5.1 Known Drift: 𝑃₀→0 ‣ 5 Limiting Cases ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§7](https://arxiv.org/html/2602.16862v1#S7.p1.1 "7 Conclusion ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty"),
  [§7](https://arxiv.org/html/2602.16862v1#S7.p3.1 "7 Conclusion ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty").
* X. Y. Zhou and D. Li (2000)
  Continuous-time mean-variance portfolio selection: a stochastic LQ framework.
  Applied Mathematics and Optimization 42 (1),  pp. 19–33.
  External Links: [Document](https://dx.doi.org/10.1007/s002450010003)
  Cited by: [§2.4](https://arxiv.org/html/2602.16862v1#S2.SS4.p3.6 "2.4 Entropy-Regularized Objective ‣ 2 Problem Formulation ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty").
* B. D. Ziebart (2010)
  Modeling purposeful adaptive behavior with the principle of maximum causal entropy.
  Ph.D. Thesis, Carnegie Mellon University.
  Cited by: [§1](https://arxiv.org/html/2602.16862v1#S1.p3.1 "1 Introduction ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty").

## Appendix A Proof of Polynomial Impossibility

###### Proof of Proposition [4.1](https://arxiv.org/html/2602.16862v1#S4.Thmtheorem1 "Proposition 4.1 (Polynomial impossibility). ‣ 4 Value Function Structure ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty").

Fix (t,P)(t,P) and suppose V​(t,⋅,⋅,P)V(t,\cdot,\cdot,P) is polynomial of finite degree in (x,m)(x,m) with Vx​x≢0V\_{xx}\not\equiv 0. Write V=∑k=0pak​(t,m,P)​xkV=\sum\_{k=0}^{p}a\_{k}(t,m,P)x^{k} where p=degx⁡V≥2p=\deg\_{x}V\geq 2.

Define G:=m​Vx+P​Vx​mG:=mV\_{x}+PV\_{xm}. The leading term is G=p​(m​ap+P​ap,m)​xp−1+O​(xp−2)G=p(ma\_{p}+Pa\_{p,m})x^{p-1}+O(x^{p-2}). Thus

|  |  |  |
| --- | --- | --- |
|  | G22​Vx​x=p2​(p−1)​(m​ap+P​ap,m)2ap​xp+O​(xp−1).\frac{G^{2}}{2V\_{xx}}=\frac{p}{2(p-1)}\frac{(ma\_{p}+Pa\_{p,m})^{2}}{a\_{p}}x^{p}+O(x^{p-1}). |  |

Dividing ([8](https://arxiv.org/html/2602.16862v1#S3.E8 "In 3.4 Reduced HJB ‣ 3 HJB Equation and Optimal Policy ‣ Entropy Regularization as Robustness under Bayesian Drift Uncertainty")) by xpx^{p} and taking x→∞x\to\infty:

|  |  |  |
| --- | --- | --- |
|  | 0=∂tap+P22​∂m​map−P2​∂Pap−p2​(p−1)​(m​ap+P​ap,m)2ap.0=\partial\_{t}a\_{p}+\frac{P^{2}}{2}\partial\_{mm}a\_{p}-P^{2}\partial\_{P}a\_{p}-\frac{p}{2(p-1)}\frac{(ma\_{p}+Pa\_{p,m})^{2}}{a\_{p}}. |  |

Let r=degm⁡apr=\deg\_{m}a\_{p}. The final term grows like mr+2m^{r+2} as |m|→∞|m|\to\infty, while linear terms grow at most like mrm^{r}. Contradiction.

□\square