---
authors:
- Ziheng Chen
- Minxuan Hu
- Jiayu Yi
- Wenxi Sun
doc_id: arxiv:2601.01709v1
family_id: arxiv:2601.01709
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus
  Shortfall-Aware Performance'
url_abs: http://arxiv.org/abs/2601.01709v1
url_html: https://arxiv.org/html/2601.01709v1
venue: arXiv q-fin
version: 1
year: 2026
---


Ziheng Chen
[stokes615@utexas.edu](mailto:stokes615@utexas.edu)

Minxuan Hu
[mh2229@cornell.edu](mailto:mh2229@cornell.edu)

Jiayu Yi
[sophiayi97@gmail.com](mailto:sophiayi97@gmail.com)

Wenxi Sun
[wsun41@alumni.jh.edu](mailto:wsun41@alumni.jh.edu)

###### Abstract

We extend the Q-learner in Black-Scholes (QLBS) framework by incorporating risk aversion and trading costs, and propose a novel Replication Learning of Option Pricing (RLOP) approach.
Both methods are fully compatible with standard reinforcement learning algorithms and operate under market frictions.
Using SPY and XOP option data, we evaluate performance along static and dynamic dimensions.
Adaptive-QLBS achieves higher static pricing accuracy in implied volatility space, while RLOP delivers superior dynamic hedging performance by reducing shortfall probability.
These results highlight the importance of evaluating option pricing models beyond static fit, emphasizing realized hedging outcomes.

###### keywords:

Option pricing , Reinforcement learning , Dynamic hedging , Shortfall risk

###### MSC:

91G20 , 68T05

††journal: Finance Research Letter

\affiliation

[label1]
organization=Department of Mathematics, University of Texas at Austin,
addressline=2515 Speedway,
city=Austin,
state=TX,
country=USA

\affiliation

[label2]
organization=Cornell Ann S. Bowers College of Computing and Information Science, Cornell University,
addressline=105 Campus Rd,
city=Ithaca,
state=NY,
country=USA

\affiliation

[label3]
organization=School of Social Sciences, Nanyang Technological University,
addressline=48 Nanyang Avenue,
country=Singapore

\affiliation

[label4]
organization=Krieger School of Arts and Sciences, Johns Hopkins University,
addressline=3400 N Charles St,
city=Baltimore,
state=MD,
country=USA

## 1 Introduction

Option pricing and hedging remain core challenges in quantitative finance.
black1973pricing provide a foundational option valuation model where perfect replication is achieved under frictionless markets with continuous-time trading, and subsequent research has extended BSM to adapt to more complex market realities (fan2022empirical; li2025analytic; golbabai2013superconvergence). Nevertheless, real-world markets involve transaction costs and discrete-time trading.

In this setting, reinforcement learning (RL) provides a more flexible framework for optimizing hedging strategies under transaction costs and tail-risk management, while also supporting robustness and stress testing via synthetic market scenarios (stutz2025jdapp). halperin2020qlbs; halperin2019qlbs
introduced the Q-Learner in Black-Scholes (QLBS) framework to unify option pricing and hedging into a discrete-time Markov Decision Process (MDP), while ignoring transaction costs.
Subsequently, buehler2019deep introduce the “Deep Hedging” framework, using neural networks to optimize hedging strategies under convex risk measures and market frictions. However, these methodologies primarily focus on symmetric or expectation-based risk metrics that capture large losses. According to follmer2000efficient , when perfect replication is impracticable due to market frictions, hedging should minimize “shortfall risk”-the probability of underperforming the option payoff.

To bridge methodological gaps, this paper addresses the decoupling between pricing-model calibration and real-world hedging performance. We shift the hedging objective from traditional error-minimization to shortfall-probability optimization to better manage transaction costs and tail risks. Using a neural-network-based RL agent within modified QLBS and novel RLOP frameworks, we compare optimal strategies against the Black-Scholes benchmark, which explicitly incorporates risk aversion and market frictions. The study investigates that under high transaction costs, the two RL-based approaches exhibit fundamentally divergent hedging behaviors. the modified QLBS agent optimizes for cost-aware stability, while the RLOP agent mitigates margin pressure and liquidity demand by systematically reducing exposure during extreme stress.

This paper delivers three primary research contributions: (1) This paper extends the QLBS framework by operationalizing its latter computational stage and embedding shortfall probability into its reward structure, resolving the decoupling between IV-fitting and hedging performance and transitioning the agent from simple loss-minimization to a survival-centric hedging strategy. (2) The novel RLOP model is introduced for superior tail-risk resilience and computational efficiency, which prioritizes minimizing hedging failure frequency over loss magnitude, as empirically validated during the COVID-19 crash. (3) This paper offers a selection framework through a bidirectional computational architecture, where the backward-operating QLBS acts as a cost-aware stabilizer for volatile assets, and the forward-calculating RLOP serves capital-constrained desks by minimizing turnover and tail losses, together yielding more robust hedging outputs.

The remainder of this paper is structured as follows: Section 2 and 3 introduce the modified QLBS model and the novel RLOP model, Section 4 and 5 present their empirical analysis under varying risk and cost scenarios, and Section 6 concludes this paper.

## 2 Replication Pricing and Reinforcement Learning Framework

Replication-based pricing constructs a self-financing portfolio whose terminal value matches the option payoff.
In the classical framework by black1973pricing, this is achieved through dynamic rebalancing of a hedge portfolio.
Given a price process {St}\left\{S\_{t}\right\}
adapted to a filtration {ℱt}\left\{\mathcal{F}\_{t}\right\}, the portfolio consists of utu\_{t} units of the underlying asset and a risk-free deposit BtB\_{t}, with value
Πt:=ut​St+Bt.\Pi\_{t}:=u\_{t}S\_{t}+B\_{t}.
The self-financing condition requires that rebalancing does not inject or withdraw capital, yielding

|  |  |  |  |
| --- | --- | --- | --- |
|  | ut​St+1+er​Δ​t​Bt=ut+1​St+1+Bt+1+TC​(ut+1−ut,St+1)u\_{t}S\_{t+1}+e^{r\Delta t}B\_{t}=u\_{t+1}S\_{t+1}+B\_{t+1}+\text{TC}(u\_{t+1}-u\_{t},S\_{t+1}) |  | (1) |

where rr denotes the risk-free rate and TC​(⋅)\text{TC}(\cdot) represents the transaction cost.
[Equation 1](https://arxiv.org/html/2601.01709v1#S2.E1 "In 2 Replication Pricing and Reinforcement Learning Framework ‣ Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus Shortfall-Aware Performance") governs the portfolio evolution and determines the capital required to sustain trading.
Throughout, the underlying price is assumed to follow a geometric Brownian motion
d⁡St=μ​St​d⁡t+σ​St​d⁡Wt\operatorname{d}S\_{t}=\mu\,S\_{t}\operatorname{d}t+\sigma\,S\_{t}\operatorname{d}W\_{t}
with drift μ\mu, volatility σ\sigma, and Wiener process WtW\_{t}.

Reinforcement learning (RL) formulates sequential decision problems via a Markov decision process (MDP).
Per sutton2018reinforcement; bertsekas2019reinforcement,
an MDP is specified by a state space 𝒮\mathcal{S}, an action space 𝒜\mathcal{A}, a transition kernel p(⋅∣s,a)p(\cdot\mid s,a), and a reward function R​(s,a)R(s,a).
A policy π\pi maps the current state to an action; in our setting, the policy corresponds to a hedging rule that updates the position over time.
Motivated by the Girsanov transform liptser2013statistics, we cast option replication as an MDP with state (t,Xt)(t,X\_{t}), where the normalized price process is
Xt:=−(μ−σ22)​t+log⁡St.X\_{t}:=-\Bigl(\mu-\tfrac{\sigma^{2}}{2}\Bigr)t+\log S\_{t}.
The action ata\_{t} represents the hedge position selected from the normalized input XtX\_{t}.
The transition kernel pp (and hence the realized rewards) depends on the model construction (e.g., QLBS versus RLOP as discussed in later paragraphs).
To distinguish representations, we use ata\_{t} for the hedge chosen as a function of XtX\_{t}, while utu\_{t} denotes the hedge position when expressed on the original price scale StS\_{t}.

As established by halperin2020qlbs, the price from the Black-Scholes model can be characterized in discrete time as the expected value of the replicating portfolio Πt\Pi\_{t}.
This insight leads to the control problem where the fair option price is the maximum of the state value function
V~tπ​(Xt)=𝔼tπ​[−Πt​(Xt)−λ​∑τ=tTe−r​(τ−t)​Vart​[Πτ​(Xτ)]]\tilde{V}\_{t}^{\pi}\left(X\_{t}\right)=\mathbb{E}^{\pi}\_{t}\left[-\Pi\_{t}\left(X\_{t}\right)-\lambda\sum\_{\tau=t}^{T}e^{-r\left(\tau-t\right)}\text{Var}\_{t}\left[\Pi\_{\tau}\left(X\_{\tau}\right)\right]\right]
where λ\lambda is the risk-aversion coefficient and 𝔼t\mathbb{E}\_{t} is conditional expectation under ℱt\mathcal{F}\_{t}.
Under this formulation, the option price equals the negative of the optimal value function.

halperin2020qlbs derives a closed-form maximizer of
V~tπ\tilde{V}\_{t}^{\pi}
by exploiting its quadratic mean-variance structure,
which is feasible when the correlation between Πt+1\Pi\_{t+1} and Δ​S\Delta S is known.
However, this approach does not generalize beyond the stylized setting.
For a given payoff function hh, the portfolio value Πt\Pi\_{t} that satisfies the terminal condition ΠT=h​(ST)\Pi\_{T}=h(S\_{T}) is typically non-adapted under the self-financing condition ([eq. 1](https://arxiv.org/html/2601.01709v1#S2.E1 "In 2 Replication Pricing and Reinforcement Learning Framework ‣ Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus Shortfall-Aware Performance")), making direct application of standard RL algorithms nontrivial.

## 3 Two Reinforcement Learning Paradigms for Option Pricing

To overcome the limitations of the original QLBS formulation, two complementary strategies have been proposed.
The first approach extends the existing QLBS framework by redefining the value function VtπV\_{t}^{\pi} as an {ℱt}\{\mathcal{F}\_{t}\}-adapted process.
The second approach adopts a conceptually different perspective by constructing an adaptive portfolio value process and defining the reward in terms of the terminal hedging tracking error.
Both approaches explicitly account for transaction costs and are compatible with both value-based and policy-based reinforcement learning algorithms.

### 3.1 Adaptive QLBS: A Backward Value-Based RL Framework

###### Definition 1.

Let dT​(t):=(1−tT)d\_{T}(t):=\left(1-\frac{t}{T}\right) and γ:=e−r​Δ​t\gamma:=e^{-r\Delta t}.
The proposed value function reads

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vtπ​(Xt)\displaystyle V\_{t}^{\pi}\left(X\_{t}\right) | :=𝔼tπ​[−dT​(t)​Πt​(Xt)−λ​∑τ=tTγτ−t​Var​[Πτ​(Xτ)]],\displaystyle:=\mathbb{E}\_{t}^{\pi}\left[-d\_{T}(t)\Pi\_{t}\left(X\_{t}\right)-\lambda\sum\_{\tau=t}^{T}\gamma^{\tau-t}\sqrt{\text{Var}\left[\Pi\_{\tau}\left(X\_{\tau}\right)\right]}\right], |  | (2) |

with the reward function Rt+1​(Xt,at):=Vtπ​(Xt)−𝔼tπ​Vt+1π​(Xt+1)R\_{t+1}\left(X\_{t},a\_{t}\right):=V\_{t}^{\pi}(X\_{t})-\mathbb{E}\_{t}^{\pi}V\_{t+1}^{\pi}(X\_{t+1}) where Xt+1X\_{t+1} is implicitly determined by Xt,atX\_{t},a\_{t} and the self-financing condition [eq. 1](https://arxiv.org/html/2601.01709v1#S2.E1 "In 2 Replication Pricing and Reinforcement Learning Framework ‣ Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus Shortfall-Aware Performance")

Our modifications are twofold:
we introduce a diminishing factor dT​(t)d\_{T}(t) that weights the portfolio term from 11 at t=0t=0 to 0 at t=Tt=T, smoothing the contribution of the terminal payoff,
and we replace variance terms by their square roots to obtain a dimensionless and numerically more stable value estimate.
When transaction costs are included, the portfolio value process Πt\Pi\_{t} is computed backward using the self-financing condition [eq. 1](https://arxiv.org/html/2601.01709v1#S2.E1 "In 2 Replication Pricing and Reinforcement Learning Framework ‣ Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus Shortfall-Aware Performance").
A schematic illustration of the adaptive-QLBS model is provided in [fig. 2](https://arxiv.org/html/2601.01709v1#S3.F2 "In 3.1 Adaptive QLBS: A Backward Value-Based RL Framework ‣ 3 Two Reinforcement Learning Paradigms for Option Pricing ‣ Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus Shortfall-Aware Performance").

0ttTTSTS\_{T}Var​Πt\text{Var}\,\Pi\_{t}under[eq. 1](https://arxiv.org/html/2601.01709v1#S2.E1 "In 2 Replication Pricing and Reinforcement Learning Framework ‣ Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus Shortfall-Aware Performance")hedge utu\_{t}state (t,St)(t,S\_{t})terminal condition hh


Figure 1: The adaptive-QLBS method takes a backward, value-based approach.

012ttTT⋯\cdots⋯\cdotsportfolio#1#2#tt#TTu0(1)u^{(1)}\_{0}R1R\_{1}u0(2)u^{(2)}\_{0}u1(2)u^{(2)}\_{1}R2R\_{2}⋮\vdotsu0(t)u^{(t)}\_{0}u1(t)u^{(t)}\_{1}ut−1(t)u^{(t)}\_{t-1}⋯\cdotsRtR\_{t}⋮\vdotsu0(T)u^{(T)}\_{0}u1(T)u^{(T)}\_{1}uT−1(T)u^{(T)}\_{T-1}⋯\cdotsRTR\_{T}


Figure 2: The RLOP method takes a forward, replication-based approach.

The proposition below explains why the option price is increasing in the key parameters where higher risk aversion
λ\lambda and larger transaction friction both raise the price. We first prove monotonicity of the value function under any fixed policy, and then obtain monotonicity of the optimal value by maximization. The proof is in the supplementary materials.

###### Proposition 1.

For sufficiently large ϵ\epsilon that appears in the linear transaction cost assumption TC​(Δ​u,S)=ϵ​|Δ​u|​S\text{TC}(\Delta u,S)=\epsilon|\Delta u|\,S, the option price C​(S0):=−maxπ∈𝚷⁡V0πC(S\_{0}):=-\max\_{\pi\in\mathbf{\Pi}}V\_{0}^{\pi} is monotonically increasing in both λ\lambda and ϵ\epsilon.

### 3.2 RLOP: A Forward Replication Learning Framework

We propose Replication Learning of Option Pricing (RLOP) that takes a forward view.
The agent trades a self-financing portfolio and is rewarded based on how closely its terminal value matches the option payoff.
Compared with Deep Hedging (buehler2019deep), which can embed a speculative component (franccois2025difference), RLOP’s shortfall-probability objective encourages capital preservation and downside-aware hedging.
The reward shaping technique (sutton2018reinforcement; devlin2011theoretical) suggests stacking an ensemble of maturities: along a path {St}\{S\_{t}\} up to horizon TT, the agent simultaneously manages portfolios Πt(i)\Pi\_{t}^{(i)} for expiries i=1,…,Ti=1,\dots,T, choosing hedge positions ut(i)u\_{t}^{(i)} for all t<it<i.
This provides intermediate feedback and lets the policy learn from short horizons before scaling to the full maturity.
A formal definition of the RLOP problem is given as follows.

###### Definition 2.

The transitional probability density from Xt=(t,St)X\_{t}=\left(t,S\_{t}\right) to Xt+1X\_{t+1} is defined as
p​(Xt,Rt+1|Xt+1,ut(i))=ρ​(St,St+1)​𝟏t<ip\left(X\_{t},R\_{t+1}\big|X\_{t+1},u\_{t}^{\left(i\right)}\right)=\rho\left(S\_{t},S\_{t+1}\right)\boldsymbol{1}\_{t<i}
where ρ\rho is characterized by the discrete version geometric Brownian motion.
The associated reward function is Ri=H​(h​(Si),Πi(i))R\_{i}=H\left(h\left(S\_{i}\right),\Pi\_{i}^{\left(i\right)}\right)
where the penalty function HH measures how accurate
the portfolio value Πi(i)\Pi\_{i}^{\left(i\right)} replicates the option
payoff h​(Si)h\left(S\_{i}\right).

In practice, we take H​(x,y)=−|x−y|H(x,y)=-|x-y| or its squared variant, which directly penalizes terminal replication error.
The structure of the RLOP approach is illustrated in [fig. 2](https://arxiv.org/html/2601.01709v1#S3.F2 "In 3.1 Adaptive QLBS: A Backward Value-Based RL Framework ‣ 3 Two Reinforcement Learning Paradigms for Option Pricing ‣ Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus Shortfall-Aware Performance").

## 4 Learning Algorithms and Numerical Verification

We parametrize the hedging policy in both QLBS and RLOP with neural networks and train it in a simulated environment.
The environment generates geometric-Brownian price paths with parameters (r,μ,σ,T)(r,\mu,\sigma,T).
At each time tt, the agent observes the normalized state (t,Xt)(t,X\_{t}), outputs a hedge position ata\_{t}, and receives rewards computed from [1](https://arxiv.org/html/2601.01709v1#Thmdefn1 "Definition 1. ‣ 3.1 Adaptive QLBS: A Backward Value-Based RL Framework ‣ 3 Two Reinforcement Learning Paradigms for Option Pricing ‣ Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus Shortfall-Aware Performance"); performance is estimated by Monte Carlo rollouts.

We model the policy as a Gaussian π=𝒩​(μπ,σπ)\pi=\mathcal{N}(\mu\_{\pi},\sigma\_{\pi}), where μπ\mu\_{\pi} and σπ\sigma\_{\pi} are produced by a shared ResNet-style network (he2016deep). A separate value network with the same architecture provides a learned baseline for variance reduction. Training uses REINFORCE with a baseline (williams1992simple; sutton2018reinforcement), optimized by Adam at learning rate 10−410^{-4}.

Finally, we verify the monotonicity in [1](https://arxiv.org/html/2601.01709v1#Thmprop1a "Proposition 1. ‣ Appendix B Proof for Proposition 1. ‣ Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus Shortfall-Aware Performance") numerically. [Figures 3](https://arxiv.org/html/2601.01709v1#S4.F3 "In 4 Learning Algorithms and Numerical Verification ‣ Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus Shortfall-Aware Performance") and [4](https://arxiv.org/html/2601.01709v1#S4.F4 "Figure 4 ‣ 4 Learning Algorithms and Numerical Verification ‣ Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus Shortfall-Aware Performance") show that the learned prices vary consistently with σ\sigma, μ\mu, λ\lambda, and ϵ\epsilon, matching the theoretical trends and reproducing the implied-volatility skew patterns observed in practice.

![Refer to caption](x1.png)

![Refer to caption](x2.png)

Figure 3: Price under Adaptive-QLBS model (left) and RLOP model (right) given different parameters of volatility. The common setup uses maturity T=2T=2 months, strike K=1K=1, interest rate r=4%r=4\%.



![Refer to caption](x3.png)

![Refer to caption](x4.png)

![Refer to caption](x5.png)

Figure 4: Price under Adaptive-QLBS model given different levels of hyperparameters: drift μ\mu (left), risk aversion intensity λ\lambda (middle), and friction ϵ\epsilon (right).

## 5 Empirical Evaluation on Market Data

In this section we move from the simulated environments to market data. We study S&P 500 and energy-sector ETF calls (SPY and XOP), and compare the two RL models (QLBS and RLOP) with three standard parametric baselines:
black1973pricing (BS), merton1976discontinuous jump-diffusion (JD), and the heston1993closed stochastic-volatility model (SV).

### 5.1 Data Description and Experimental Design

#### Data

We use daily snapshots of SPY and XOP call options from two non-overlapping quarters: 2020Q1 (COVID crash, high-volatility regime) and 2025Q2 (calmer regime).
We construct synthetic European call prices Cmkt​(K,τ)C^{\mathrm{mkt}}(K,\tau) and retain contracts with 3 to 70 calendar days to maturity.

#### Bucketing and moneyness

Maturities are grouped into buckets centered at 14, 28, and 56 days. Within each bucket we define moneyness as K/FK/F, where FF is the forward corresponding to the option’s maturity. We focus on the 28-day bucket in the main analysis, and report the full maturity-by-moneyness breakdown in the appendix.

#### Daily calibration and fitting

On each trading day and for each maturity bucket, we calibrate the parametric baselines to that day’s cross-section by minimizing squared pricing errors. QLBS and RLOP are fit on the same slice using the procedure described in earlier sections.

#### Evaluation

We report two sets of outcomes.
(1) Static fit: we compare model-implied volatilities with market implied volatilities using equal-day IVRMSE reported on a 10310^{3} scale.
(2) Dynamic performance: we evaluate discrete-time Δ\Delta-hedging of a short call over the realized (“historical”) underlying path. Let
ΠT:=VT−(ST−K)+,\Pi\_{T}:=V\_{T}-(S\_{T}-K)^{+},
where VTV\_{T} is the terminal value of the self-financing hedging portfolio initialized with the option premium and including transaction costs. We report three metrics computed from ΠT\Pi\_{T}:

1. 1.

   Hedging RMSE: RMSE​(ΠT):=𝔼​[ΠT2]\mathrm{RMSE}(\Pi\_{T}):=\sqrt{\mathbb{E}[\Pi\_{T}^{2}]}, estimated by the root mean square of terminal ΠT\Pi\_{T} across hedges.
2. 2.

   Average trading cost: cumulative proportional transaction costs incurred by hedge rebalancing over the horizon, reported per option.
3. 3.

   Shortfall probability: ℙ​(ΠT<0)\mathbb{P}(\Pi\_{T}<0), estimated in the historical backtest as the empirical frequency of negative terminal ΠT\Pi\_{T} across hedges.

All reported numbers are equal-day averages: we compute each metric within a trading day and then average across days so that each day contributes one observation regardless of how many strikes are listed.

### 5.2 Static Pricing Accuracy: Implied Volatility Fit

Table [1](https://arxiv.org/html/2601.01709v1#S5.T1 "Table 1 ‣ 5.2 Static Pricing Accuracy: Implied Volatility Fit ‣ 5 Empirical Evaluation on Market Data ‣ Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus Shortfall-Aware Performance") reports equal-day IVRMSE for the 28-day maturity bucket (whole sample) for SPY and XOP in 2020Q1 and 2025Q2.
Three takeaways stand out.

| Moneyness, τ\tau | Period | Asset | BS | JD | SV | QLBS | RLOP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Whole sample, 28d | 2020Q1 | SPY | 76.50 | 17.62 | 42.08 | 102.65 | 82.47 |
| XOP | 120.18 | 91.63 | 88.34 | 109.92 | 188.07 |
| 2025Q2 | SPY | 127.95 | 94.90 | 74.02 | 92.54 | 73.43 |
| XOP | 106.10 | 64.83 | 73.30 | 111.23 | 163.62 |

Table 1: Equal-day IVRMSE for the whole sample at τ=28\tau=28d. Lower is better; bold marks the best value within each row.

1. 1.

   Parametric benchmarks fit the surface best, especially in stress.
   In SPY 2020Q1, JD substantially improves on BS and also beats SV, consistent with discontinuous moves mattering more in crash periods.
2. 2.

   In calmer markets, the ranking compresses and can be asset-specific.
   In SPY 2025Q2, SV and RLOP deliver very similar IVRMSE, while JD remains clearly ahead of BS. For XOP 2025Q2, JD is best with SV close behind, suggesting that energy-sector options can exhibit different cross-sectional features than broad-index options even within the same quarter.
3. 3.

   RL models are not designed as implied-volatility interpolators, yet QLBS can be competitive in IV fit.
   Across the four asset–period pairs, QLBS usually sits between BS and the best parametric model, and is near JD in SPY 2025Q2. RLOP varies more, consistent with a frictional hedging objective rather than same-day IV fit.

Full maturity and moneyness breakdowns are reported in
Appendix Tables A.1– A.3.
The supplementary tables convey a broadly consistent qualitative picture: JD/SV are typically strongest in IVRMSE, while the hedging-oriented RL models are more variable across assets and regimes.
We therefore turn next to realized-path Δ\Delta-hedging results.

### 5.3 Dynamic Hedging Performance

We backtest each model’s discrete-time Δ\Delta-hedging on the subsequent realized underlying path with proportional transaction costs, and summarize three desk-relevant diagnostics: RMSE of terminal hedging P&L, average cumulative trading cost per option, and shortfall probability.

#### ATM benchmark (Table [2](https://arxiv.org/html/2601.01709v1#S5.T2 "Table 2 ‣ ATM benchmark (Table 2) ‣ 5.3 Dynamic Hedging Performance ‣ 5 Empirical Evaluation on Market Data ‣ Reinforcement Learning for Option Hedging: Static Implied-Volatility Fit versus Shortfall-Aware Performance"))

| Moneyness, τ\tau | Period | Asset | Metric | BS | JD | SV | QLBS | RLOP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ATM, 28d | 2020Q1 | SPY | Hedging RMSE | 5.88 | 7.03 | 8.15 | 5.62 | 6.39 |
| Average trading cost | 2.21 | 2.62 | 3.52 | 2.09 | 1.95 |
| Shortfall probability | 1.00 | 0.96 | 0.96 | 1.00 | 0.91 |
| XOP | Hedging RMSE | 0.40 | 0.42 | 0.45 | 0.54 | 0.36 |
| Average trading cost | 0.10 | 0.10 | 0.11 | 0.09 | 0.11 |
| Shortfall probability | 1.00 | 1.00 | 1.00 | 1.00 | 0.96 |
| 2025Q2 | SPY | Hedging RMSE | 6.07 | 6.56 | 7.57 | 7.01 | 6.70 |
| Average trading cost | 3.58 | 3.77 | 4.69 | 3.91 | 3.09 |
| Shortfall probability | 0.97 | 0.53 | 0.55 | 0.92 | 0.76 |
| XOP | Hedging RMSE | 1.38 | 1.60 | 1.69 | 1.47 | 1.52 |
| Average trading cost | 0.85 | 0.87 | 1.05 | 0.80 | 0.83 |
| Shortfall probability | 0.58 | 0.40 | 0.42 | 0.60 | 0.39 |

Table 2: ATM (τ=28\tau=28d) delta-hedging performance under transaction costs.
Equal-day averages of hedging RMSE, average trading cost, and shortfall probability for a short call hedged over 28 days on SPY and XOP in 2020Q1 and 2025Q2. Shortfall probability is reported as a fraction in [0,1][0,1]; values of 1.001.00 indicate that, within that cell, essentially all hedges end with ΠT<0\Pi\_{T}<0. Lower is better; bold marks the best value within each row.

We first focus on ATM options as they are the standard benchmark for Δ\Delta-hedging comparisons. Three patterns emerge.

1. 1.

   QLBS prioritizes replication while keeping turnover near classical deltas.
   Empirically, in stress, it achieves the lowest hedging RMSE with trading costs that remain near the BS benchmark. In calmer markets, it can trade a small amount of RMSE optimality for execution efficiency.
2. 2.

   RLOP behaves like a friction- and downside-aware policy.
   On SPY, it is the lowest-cost hedge in both regimes (an ∼\sim14% reduction vs BS in 2025Q2), while also reducing shortfall probability relative to BS in both quarters.
   On XOP, it has the best RMSE in stress and the lowest shortfall in 2025Q2, with competitive costs.
3. 3.

   RL policies remain well-behaved in the 2020Q1 stress test.
   Rather than collapsing under the COVID crash dynamics, both RL hedges remain economically sensible.
   QLBS preserves replication performance without inflating turnover, while RLOP delivers a clear capital-efficiency and downside signature.

#### Near-OTM stress test (Appendix Table A.4)

We repeat the same exercise for a mildly OTM target (K/F=1.03K/F=1.03) at τ=28\tau=28d. The results reinforce RLOP’s downside-sensitive behavior under costs: in SPY 2025Q2 it lowers shortfall probability and trading cost with only a modest RMSE increase. For XOP, RLOP also improves RMSE and shortfall in 2020Q1, and both RL methods remain competitive in 2025Q2.

To summarize, RL policies improve economically relevant quantities even when they do not dominate every metric. In particular, the parametric models can be strong on one dimension (e.g., RMSE in calmer regimes), yet the RL policies often achieve meaningful reductions in trading cost and/or shortfall probability.

### 5.4 Static versus Dynamic Metrics: Robustness and Interpretation

Our result shows that static surface fit and dynamic hedging performance are weakly aligned under discrete rebalancing and trading costs. The parametric benchmarks (especially JD and SV) often deliver the lowest IVRMSE, yet they do not consistently dominate realized hedging outcomes. This disconnect arises because IVRMSE is a one-day cross-sectional diagnostic, while hedging P&L is shaped by realized price paths, re-hedging frequency, and turnover management under market frictions.

Therefore, the RL-based methods add a distinct and complementary value proposition. QLBS behaves like a cost-aware alternative to classical deltas: its hedging RMSE is typically in the same range as BS/JD/SV, while it often improves implementation cost and sometimes downside frequency, particularly outside the most extreme regions. RLOP prioritizes adverse outcome control. It frequently achieves lower shortfall probability and trading cost, even with higher dispersion of terminal hedging errors. By actively managing positions to strike an optimal balance between replication error (RMSE) and tail risk (shortfall probability), QLBS and RLOP computationally operationalizes the theoretical framework of follmer2000efficient.

Finally, the qualitative interpretation is stable across regimes and horizons. The crisis window (2020Q1) and the calmer period (2025Q2) differ sharply in volatility conditions, yet the roles above remain intact. In the supplementary materials, we report the same ATM and near-OTM diagnostics for τ=14\tau=14d (Appendix Table A.5 & A.6) and τ=56\tau=56d (Appendix Table A.7 & A.8).
The conclusions remain broadly consistent: QLBS stays close to classical deltas in replication error while often improving cost efficiency, and RLOP continues to deliver meaningful reductions in loss frequency in many slices, especially in the near-OTM stress tests, where downside-sensitive behavior is most visible.

## 6 Conclusion

This paper develops modified QLBS and novel RLOP environments for RL-based option pricing with transaction costs and risk aversion. Since pricing-model calibration and hedging performance are decoupled, this paper shifts the optimization objective toward shortfall probability to ensure tail-risk resilience to address the problem. We extend QLBS into a fully implemented algorithm, which acts as a cost-conscious hedge, and reduces shortfall probability and trading costs. RLOP prioritizes tail-risk resilience, accepting poorer IV fits for significant reductions in the probability and cost of extreme hedging losses and making it ideal for capital-constrained desks during market stress. Future work should incorporate computational complexity, path-dependent instruments, funding-spread jumps, and model risk to further improve pricing accuracy and execution efficiency.

## Data Availability

The option data used in this study are publicly available from the DoltHub repository [post-no-preference/options](https://www.dolthub.com/repositories/post-no-preference/options), which provides historical option records for SPY and XOP. The analyses in this paper use only these publicly accessible records, and no proprietary datasets were used. The data were accessed on Oct 15, 2025.

## Funding Statement

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## Author contributions (CRediT)

Ziheng Chen: Conceptualization; Formal analysis; Software (reinforcement learning training); Writing – original draft (mathematical derivations and proofs).

Minxuan Hu: Software (empirical data fitting and hedging-cost calibration); Data curation; Validation; Writing – original draft (tables, formatting, and interpretation).

Jiayu Yi: Writing – original draft (introduction); Writing – review & editing.

Wenxi Sun: Writing – original draft (literature review); Writing – review & editing.

## Appendix A Tables on Market Data Fit Results

| Moneyness, τ\tau | Period | Asset | BS | JD | SV | QLBS | RLOP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Whole sample, 28d | 2020Q1 | SPY | 76.50 | 17.62 | 42.08 | 102.65 | 82.47 |
| XOP | 120.18 | 91.63 | 88.34 | 109.92 | 188.07 |
| 2025Q2 | SPY | 127.95 | 94.90 | 74.02 | 92.54 | 73.43 |
| XOP | 106.10 | 64.83 | 73.30 | 111.23 | 163.62 |
| Moneyness <1<1, 28d | 2020Q1 | SPY | 88.35 | 16.13 | 41.32 | 133.86 | 95.27 |
| XOP | 140.94 | 98.03 | 102.23 | 124.84 | 195.22 |
| 2025Q2 | SPY | 169.37 | 114.23 | 75.53 | 107.61 | 75.46 |
| XOP | 123.68 | 75.07 | 86.06 | 134.59 | 137.33 |
| Moneyness >1>1, 28d | 2020Q1 | SPY | 54.65 | 17.52 | 32.06 | 54.55 | 63.70 |
| XOP | 76.38 | 53.47 | 45.76 | 66.05 | 164.72 |
| 2025Q2 | SPY | 39.65 | 53.59 | 59.29 | 65.22 | 63.61 |
| XOP | 79.44 | 43.28 | 49.46 | 65.95 | 182.29 |
| Moneyness >1.03>1.03, 28d | 2020Q1 | SPY | 61.90 | 20.16 | 37.02 | 41.66 | 55.93 |
| XOP | 81.38 | 56.35 | 49.15 | 69.93 | 166.67 |
| 2025Q2 | SPY | 40.44 | 59.41 | 65.79 | 67.61 | 61.19 |
| XOP | 85.40 | 46.07 | 52.92 | 66.93 | 191.37 |

Table 1: Equal-day IVRMSE for the τ=28\tau=28d maturity bucket across moneyness groups. Lower is better; bold marks the best value within each asset, period, and moneyness row.



| Moneyness, τ\tau | Period | Asset | BS | JD | SV | QLBS | RLOP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Whole sample, 14d | 2020Q1 | SPY | 91.49 | 55.27 | 74.74 | 126.16 | 107.38 |
| XOP | 187.68 | 163.92 | 188.65 | 203.85 | 249.38 |
| 2025Q2 | SPY | 164.35 | 135.95 | 108.14 | 118.28 | 94.86 |
| XOP | 151.73 | 95.57 | 123.06 | 151.55 | 201.01 |

Table 2: Equal-day IVRMSE for the whole sample at τ=14\tau=14d. Lower is better; bold marks the best value within each asset and period row.



| Moneyness, τ\tau | Period | Asset | BS | JD | SV | QLBS | RLOP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Whole sample, 56d | 2020Q1 | SPY | 65.52 | 12.26 | 22.68 | 87.32 | 84.13 |
| XOP | 59.44 | 33.43 | 31.80 | 60.07 | 199.07 |
| 2025Q2 | SPY | 92.69 | 60.61 | 43.59 | 74.41 | 70.51 |
| XOP | 68.77 | 37.90 | 37.56 | 72.08 | 147.40 |

Table 3: Equal-day IVRMSE for the whole sample at τ=56\tau=56d. Lower is better; bold marks the best value within each asset and period row.



| Moneyness, τ\tau | Period | Asset | Metric | BS | JD | SV | QLBS | RLOP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| K/F=1.03K/F=1.03, 28d | 2020Q1 | SPY | Hedging RMSE | 3.57 | 4.16 | 6.21 | 3.61 | 4.53 |
| Average trading cost | 0.88 | 0.96 | 1.84 | 0.86 | 1.19 |
| Shortfall probability | 1.00 | 1.00 | 0.96 | 1.00 | 1.00 |
| XOP | Hedging RMSE | 0.31 | 0.31 | 0.34 | 0.44 | 0.23 |
| Average trading cost | 0.07 | 0.08 | 0.08 | 0.07 | 0.07 |
| Shortfall probability | 1.00 | 1.00 | 1.00 | 1.00 | 0.78 |
| 2025Q2 | SPY | Hedging RMSE | 5.58 | 5.83 | 7.36 | 6.97 | 6.05 |
| Average trading cost | 3.57 | 4.08 | 4.86 | 3.48 | 2.96 |
| Shortfall probability | 0.84 | 0.76 | 0.84 | 0.87 | 0.55 |
| XOP | Hedging RMSE | 1.28 | 1.50 | 1.86 | 1.25 | 1.32 |
| Average trading cost | 0.81 | 0.85 | 0.98 | 0.71 | 0.79 |
| Shortfall probability | 0.53 | 0.51 | 0.49 | 0.39 | 0.33 |

Table 4: OTM (K/F=1.03K/F=1.03, τ=28\tau=28d) delta-hedging performance under transaction costs.
Equal-day averages of hedging RMSE, average trading cost, and shortfall probability for a short call hedged over 28 days on SPY and XOP in 2020Q1 and 2025Q2. Lower is better; bold marks the best value within each asset, period, and metric row.



| Moneyness, τ\tau | Period | Asset | Metric | BS | JD | SV | QLBS | RLOP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ATM, 14d | 2020Q1 | SPY | Hedging RMSE | 2.83 | 3.24 | 4.04 | 2.77 | 2.31 |
| Average trading cost | 1.42 | 1.67 | 2.24 | 1.39 | 1.16 |
| Shortfall probability | 1.00 | 0.97 | 0.97 | 1.00 | 0.94 |
| XOP | Hedging RMSE | 0.29 | 0.30 | 0.32 | 0.33 | 0.27 |
| Average trading cost | 0.07 | 0.07 | 0.08 | 0.07 | 0.07 |
| Shortfall probability | 1.00 | 1.00 | 1.00 | 1.00 | 0.96 |
| 2025Q2 | SPY | Hedging RMSE | 4.09 | 4.33 | 4.83 | 4.35 | 4.07 |
| Average trading cost | 2.04 | 2.12 | 2.59 | 2.26 | 1.92 |
| Shortfall probability | 0.97 | 0.67 | 0.72 | 0.91 | 0.72 |
| XOP | Hedging RMSE | 0.89 | 0.98 | 1.05 | 0.96 | 0.93 |
| Average trading cost | 0.50 | 0.51 | 0.60 | 0.49 | 0.48 |
| Shortfall probability | 0.62 | 0.51 | 0.52 | 0.57 | 0.43 |

Table 5: ATM (τ=14\tau=14d) delta-hedging performance under transaction costs.
Equal-day averages of hedging RMSE, average trading cost, and shortfall probability for a short call hedged over 14 days on SPY and XOP in 2020Q1 and 2025Q2. Lower is better; bold marks the best value within each asset, period, and metric row.



| Moneyness, τ\tau | Period | Asset | Metric | BS | JD | SV | QLBS | RLOP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| K/F=1.03K/F=1.03, 14d | 2020Q1 | SPY | Hedging RMSE | 2.06 | 2.23 | 2.89 | 2.07 | 2.24 |
| Average trading cost | 1.23 | 1.37 | 1.86 | 1.18 | 1.35 |
| Shortfall probability | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 |
| XOP | Hedging RMSE | 0.20 | 0.21 | 0.22 | 0.23 | 0.18 |
| Average trading cost | 0.05 | 0.06 | 0.06 | 0.05 | 0.05 |
| Shortfall probability | 1.00 | 1.00 | 1.00 | 1.00 | 0.88 |
| 2025Q2 | SPY | Hedging RMSE | 3.86 | 4.03 | 4.56 | 4.12 | 3.98 |
| Average trading cost | 1.92 | 2.00 | 2.49 | 2.07 | 1.84 |
| Shortfall probability | 0.88 | 0.74 | 0.76 | 0.85 | 0.72 |
| XOP | Hedging RMSE | 0.81 | 0.88 | 0.92 | 0.85 | 0.84 |
| Average trading cost | 0.46 | 0.48 | 0.56 | 0.43 | 0.45 |
| Shortfall probability | 0.56 | 0.55 | 0.55 | 0.44 | 0.48 |

Table 6: OTM (K/F=1.03K/F=1.03, τ=14\tau=14d) delta-hedging performance under transaction costs.
Equal-day averages of hedging RMSE, average trading cost, and shortfall probability for a short call hedged over 14 days on SPY and XOP in 2020Q1 and 2025Q2. Lower is better; bold marks the best value within each asset, period, and metric row.



| Moneyness, τ\tau | Period | Asset | Metric | BS | JD | SV | QLBS | RLOP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ATM, 56d | 2020Q1 | SPY | Hedging RMSE | 6.92 | 8.73 | 9.75 | 8.53 | 9.15 |
| Average trading cost | 2.67 | 3.05 | 3.95 | 2.88 | 2.84 |
| Shortfall probability | 0.85 | 0.79 | 0.76 | 0.82 | 0.62 |
| XOP | Hedging RMSE | 0.52 | 0.54 | 0.55 | 0.62 | 0.46 |
| Average trading cost | 0.11 | 0.11 | 0.12 | 0.10 | 0.11 |
| Shortfall probability | 0.95 | 0.95 | 0.95 | 0.86 | 0.95 |
| 2025Q2 | SPY | Hedging RMSE | 9.91 | 10.23 | 11.12 | 12.86 | 9.12 |
| Average trading cost | 5.61 | 5.68 | 7.10 | 5.86 | 4.54 |
| Shortfall probability | 0.46 | 0.45 | 0.44 | 0.60 | 0.28 |
| XOP | Hedging RMSE | 2.24 | 2.50 | 2.58 | 2.50 | 2.56 |
| Average trading cost | 1.07 | 1.05 | 1.35 | 1.11 | 0.89 |
| Shortfall probability | 0.51 | 0.44 | 0.46 | 0.52 | 0.38 |

Table 7: ATM (τ=56\tau=56d) delta-hedging performance under transaction costs.
Equal-day averages of hedging RMSE, average trading cost, and shortfall probability for a short call hedged over 56 days on SPY and XOP in 2020Q1 and 2025Q2. Lower is better; bold marks the best value within each asset, period, and metric row.



| Moneyness, τ\tau | Period | Asset | Metric | BS | JD | SV | QLBS | RLOP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| K/F=1.03K/F=1.03, 56d | 2020Q1 | SPY | Hedging RMSE | 4.61 | 5.35 | 6.25 | 6.13 | 6.06 |
| Average trading cost | 2.15 | 2.43 | 3.14 | 1.96 | 2.64 |
| Shortfall probability | 0.80 | 0.80 | 0.80 | 0.80 | 0.20 |
| XOP | Hedging RMSE | 0.40 | 0.40 | 0.40 | 0.47 | 0.29 |
| Average trading cost | 0.07 | 0.07 | 0.08 | 0.06 | 0.06 |
| Shortfall probability | 1.00 | 1.00 | 1.00 | 1.00 | 0.70 |
| 2025Q2 | SPY | Hedging RMSE | 8.09 | 8.09 | 9.63 | 12.14 | 9.47 |
| Average trading cost | 5.70 | 5.66 | 7.10 | 6.26 | 4.77 |
| Shortfall probability | 0.46 | 0.46 | 0.46 | 0.60 | 0.24 |
| XOP | Hedging RMSE | 1.87 | 1.88 | 2.03 | 2.12 | 2.02 |
| Average trading cost | 0.88 | 0.90 | 1.15 | 0.93 | 0.91 |
| Shortfall probability | 0.51 | 0.49 | 0.51 | 0.56 | 0.49 |

Table 8: OTM (K/F=1.03K/F=1.03, τ=56\tau=56d) delta-hedging performance under transaction costs.
Equal-day averages of hedging RMSE, average trading cost, and shortfall probability for a short call hedged over 56 days on SPY and XOP in 2020Q1 and 2025Q2. Lower is better; bold marks the best value within each asset, period, and metric row.

## Appendix B Proof for Proposition 1.

###### Proposition 1.

For sufficiently large ϵ\epsilon that appears in the linear transaction cost assumption TC​(Δ​u,S)=ϵ​|Δ​u|​S\text{TC}(\Delta u,S)=\epsilon|\Delta u|\,S, the option price C​(S0):=−maxπ∈𝚷⁡V0πC(S\_{0}):=-\max\_{\pi\in\mathbf{\Pi}}V\_{0}^{\pi} is monotonically increasing in both λ\lambda and ϵ\epsilon.

###### Proof.

Given any policy π\pi, the portfolio value at time tt may be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πt=ut​St+ϵ​𝔖t+γT−t​𝔈t,𝔖t:=∑j=0T−t−1γj+1​|Δ​ut+j|​St+j+1,𝔈t:=h​(ST)−uT−1​ST\displaystyle\Pi\_{t}=u\_{t}S\_{t}+\epsilon\mathfrak{S}\_{t}+\gamma^{T-t}\mathfrak{E}\_{t},\quad\mathfrak{S}\_{t}:=\sum\_{j=0}^{T-t-1}\gamma^{j+1}|\Delta u\_{t+j}|S\_{t+j+1},\quad\mathfrak{E}\_{t}:=h(S\_{T})-u\_{T-1}S\_{T} |  | (3) |

under the self-financing condition
(eq. 1)
.
This expression is affine in ϵ\epsilon and independent of λ\lambda.
Hence, the monotonicity of VtπV\_{t}^{\pi} with respect to λ\lambda follows immediately from
(eq. 2)
, since the discounted risk term is always non-positive.
For ϵ≫1\epsilon\gg 1, the monotonicity in ϵ\epsilon follows from the fact that Vart​Πt​(Xt)\text{Var}\_{t}\Pi\_{t}\left(X\_{t}\right) is a quadratic function of ϵ\epsilon with non-negative leading coefficient.

To establish that C​(S0,λ)C(S\_{0},\lambda) is increasing in λ\lambda, let π​(λ)\pi(\lambda) denote the maximizer of VtπV\_{t}^{\pi}.
For λ′>λ\lambda^{\prime}>\lambda, we have
Vtπ​(λ)​(St;λ)≥Vtπ​(λ′)​(St;λ)V\_{t}^{\pi(\lambda)}(S\_{t};\lambda)\geq V\_{t}^{\pi(\lambda^{\prime})}(S\_{t};\lambda)
because π​(λ)\pi(\lambda) maximizes the value function at level λ\lambda.
From the argument above, Vtπ​(λ′)​(St;λ′)≤Vtπ​(λ′)​(St;λ)V\_{t}^{\pi(\lambda^{\prime})}(S\_{t};\lambda^{\prime})\leq V\_{t}^{\pi(\lambda^{\prime})}(S\_{t};\lambda).
Combining these inequalities yields

|  |  |  |
| --- | --- | --- |
|  | C​(S0,λ′)=−V0π​(λ′)​(S0;λ′)≥−V0π​(λ′)​(S0;λ)≥−V0π​(λ)​(S0;λ)=C​(S0,λ).\displaystyle C(S\_{0},\lambda^{\prime})=-V\_{0}^{\pi(\lambda^{\prime})}(S\_{0};\lambda^{\prime})\geq-V\_{0}^{\pi(\lambda^{\prime})}(S\_{0};\lambda)\geq-V\_{0}^{\pi(\lambda)}(S\_{0};\lambda)=C(S\_{0},\lambda). |  |

Thus, CC is monotone in λ\lambda.
The argument for its monotonicity in ϵ\epsilon proceeds similarly.

∎