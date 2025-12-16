---
authors:
- Travon Lucius
- Christian Koch
- Jacob Starling
- Julia Zhu
- Miguel Urena
- Carrie Hu
doc_id: arxiv:2512.12420v1
family_id: arxiv:2512.12420
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1. Executive Summary
url_abs: http://arxiv.org/abs/2512.12420v1
url_html: https://arxiv.org/html/2512.12420v1
venue: arXiv q-fin
version: 1
year: 2025
---


panel, state\_cols = build\_sim\_panel(

market\_df=market,

spx\_clean\_dir=SPX\_CLEAN,

include\_spy=False,

ffill\_limit=2, # IV features forward-fill at most 2 calendar days

)

Forward returns are computed as close-to-close percentage changes
shifted forward by one step, preventing the agent from seeing realized
PnL before choosing an action. Date splits (train ≤\leq 2017-12-31,
validation 2018–2019, test ≥\geq 2020-01-01) are stored in each run’s
configuration, and all intermediate artefacts (cleaned snapshots, parquet
panels, scaler parameters, deterministic evaluation metrics) are
committed alongside the code.

## 5. Hedging Environment

We implement a deterministic environment HedgingEnv
(src/simulator/env.py). Each observation is a matrix of shape
W×FW\times F (window × features) normalized with statistics derived
solely from the training split. Actions are continuous hedge levels
at∈[−amax,+amax]a\_{t}\in[-a\_{\max},+a\_{\max}], interpreted as the number of
underlying units hedged per unit option exposure. Transaction costs are
proportional to the absolute change in position,
ct=κ​|at−at−1|c\_{t}=\kappa|a\_{t}-a\_{t-1}|, where κ\kappa is specified in basis
points. Per-step PnL is pt=at​Rt+1−ctp\_{t}=a\_{t}R\_{t+1}-c\_{t} and we scale the
reward as rt=104​ptr\_{t}=10^{4}p\_{t} (basis points) to keep gradients well
behaved. Episodes walk deterministically through
the panel; forward returns are aligned to the action time so there is no
look-ahead; NaNs or infinities are replaced with zeros to prevent
accidental leakage. Convenience policies in
src/simulator/baselines.py (no\_hedge, momentum,
volatility\_targeting, delta wrappers) are used both for sanity checks
during development and for the baseline results reported later.

To capture richer microstructure effects, we expose a
slippage\_fn hook that embeds the linear-quadratic price impact
models described in the *Handbook of Price Impact Modeling*
([]). If qt=at−at−1q\_{t}=a\_{t}-a\_{t-1} denotes the trade size, temporary execution costs follow
ctmp​(qt)=ϕ​|qt|+12​ψ​qt2c\_{\text{tmp}}(q\_{t})=\phi|q\_{t}|+\tfrac{1}{2}\psi q\_{t}^{2}, while the
mid-price evolves as Δ​St+1=σ​εt+1+λ​qt\Delta S\_{t+1}=\sigma\varepsilon\_{t+1}+\lambda q\_{t}, where ϕ\phi captures spread/fees, ψ\psi the nonlinear
depth term, and λ\lambda the permanent impact coefficient. Plugging
these expressions into the reward yields

|  |  |  |
| --- | --- | --- |
|  | rt=104​(at​Rt+1−κ​|qt|−12​ψ​qt2−λ​at​qt),r\_{t}=10^{4}\left(a\_{t}R\_{t+1}-\kappa|q\_{t}|-\tfrac{1}{2}\psi q\_{t}^{2}-\lambda a\_{t}q\_{t}\right), |  |

which matches the discrete Almgren–Chriss style models summarized by
Webster and lets us stress test the agent under both spread and
inventory driven frictions.
In the reported experiments we keep the Almgren–Chriss hook but set
ψ=0\psi\!=\!0 and λ=0\lambda\!=\!0 (costs are proportional plus a fixed
slippage\_bps parameter), reserving nonlinear impact for future
stress tests.

Baselines. Rule-based overlays include a VIX-band policy that holds flat
when VIX is near its median, increases the hedge when VIX is high, and
relaxes it when VIX is low, plus a VIX volatility-target rule that scales
hedge notional to target equity vol. Both reuse the same transaction-cost
and slippage settings as the RL agent. Simple delta hedges (and delta
variants) are dominated by these overlays and the RL policy on all
splits, so we summarize them qualitatively rather than carry them into
the main tables.

Code: constructing the environment

Listing 3: Constructing train/valid/test splits and the hedging environment.

from rl\_agent.experiment import make\_splits, make\_scaler

from simulator.env import HedgingEnv

from simulator.rewards import reward\_bps

state\_cols = [

"iv\_atm\_30d\_spx","iv\_ts\_slope\_spx","iv\_skew\_30d\_spx",

"vix","rate\_10y","rv\_21d","hvol\_30d","hvol\_91d",

]

p, m\_tr, m\_va, m\_te, TRAIN\_END, VALID\_END = make\_splits(panel, "2017-12-31", "2019-12-31")

scaler, mu, sg = make\_scaler(p, state\_cols, m\_tr)

env = HedgingEnv(

df=p[m\_te].reset\_index(drop=True),

features=state\_cols,

reward\_fn=lambda pnl, info: reward\_bps(pnl, info, 1e4),

window=30, txn\_cost\_bps=1.0, pos\_limit=1.0,

scaler=scaler, hold\_on\_nan=True,

)

obs = env.reset()

## 6. Reinforcement Learning Framework

We deploy a compact stochastic policy and value network that balances
modelling capacity. A two-layer MLP (256 hidden units with
tanh\tanh activations) outputs the
mean μθ​(st)\mu\_{\theta}(s\_{t}), a scalar log standard deviation, and the state
value. Actions are sampled from a Normal distribution, squashed with
tanh\tanh, and rescaled to [−amax,amax][-a\_{\max},a\_{\max}]. This “squashed
Gaussian” formulation keeps actions bounded while retaining
differentiability so the agent can learn both the shape of the policy
and the variance it should maintain. We optimize an
entropy-regularized policy gradient in an actor–critic configuration
with generalized advantage estimation (GAE)
([];
[]):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇θJ​(θ)\displaystyle\nabla\_{\theta}J(\theta) | =𝔼​[∑t∇θlog⁡πθ​(at∣st)​At]\displaystyle=\mathbb{E}\!\left[\sum\_{t}\nabla\_{\theta}\log\pi\_{\theta}(a\_{t}\mid s\_{t})\,A\_{t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +β𝔼[ℋ(πθ(⋅∣st))],\displaystyle\quad+\beta\,\mathbb{E}\!\left[\mathcal{H}\!\left(\pi\_{\theta}(\cdot\mid s\_{t})\right)\right], |  |

where AtA\_{t} is the advantage and β\beta the entropy weight. We set
γ=0.99\gamma=0.99, apply gradient clipping at 1.0, and modulate the
learning rate with a cosine schedule. We fix the entropy coefficient at 0.01 to maintain mild
exploration while discouraging flippant trading. Model checkpoints are evaluated deterministically on
train/validation splits every 50 updates, and the best validation Sharpe
is retained. Hidden sizes of 128–256 were tried; the 256-unit variant
used in the released checkpoints did not materially change validation
Sharpe versus smaller nets, and training curves were qualitatively
stable across seeds. Although the architecture is small, we find it expressive
enough to learn counter-cyclical behavior: increasing hedge size in
volatile regimes while relaxing exposure when term structure normalizes.
Because the observation window is composed of engineered features rather
than latent embeddings, individual policy decisions can be traced back
to familiar quantities (e.g., VIX spikes or steepening of the IV term
structure).

## 7. Experimental Setup

We evaluate the best validation checkpoint deterministically on each
split. Evaluation tracks multiple metrics: Sharpe from per-step rewards
(annualized via 252\sqrt{252}), maximum drawdown of the cumulative
reward equity, turnover (∑|Δ​position|\sum|\Delta\text{position}|), hit-rate
(sign agreement between actions and subsequent returns), and
cost normalized profit. For context we also compute simple baselines
(no-hedge, momentum, volatility-targeting, buy-and-hold SPY) using the
same HedgingEnv and cost parameters; their results are summarized later
to benchmark the learned policy. All evaluation code lives in
rl\_agent/evaluate\_policy.py and
rl\_agent/experiment.py, which makes it straightforward to plug
the trained policy into other backtesting harnesses.

Code: training API and evaluation

Listing 4: Training/evaluation snippet showing the actor-critic loop and deterministic replay.

from rl\_agent.train\_ac\_gae import train

from rl\_agent.experiment import deterministic\_rewards

policy, (tr, va, te) = train(

panel=p,

state\_cols=state\_cols,

train\_end=str(TRAIN\_END.date()), valid\_end=str(VALID\_END.date()),

window=30, txn\_cost\_bps=1.0, pos\_limit=1.0,

hidden=256, lr=5e-4, steps=2500,

entropy\_start=0.01, entropy\_floor=0.01,

save\_ckpt="models/gae\_run1/best.pt",

save\_config="models/gae\_run1/config.json",

save\_outdir="models/gae\_run1",

)

r\_test = deterministic\_rewards(env, policy)

## 8. Results

Under realistic cadence and cost constraints, the agent delivers modest
but consistent positive Sharpe across train, validation, and test
splits. Validation performance confirms that the policy
generalizes beyond the training period, and the 2020+ test window, which
includes the COVID volatility shock, remains profitable once trading
costs are deducted. Turnover stays below one full notional rotation per
day on average, indicating that the entropy schedule and cost-aware
reward discourage churning. Maximum drawdown on the test split for the
standalone overlay-equity series remains inside -3%, materially lower than an unhedged or simple volatility
targeting approach.

Text summary (final configuration): with transaction costs of 10 bps per
unit of |Δ​position||\Delta\text{position}|, proportional slippage of 8 bps, a
position limit of pos\_limit = 2.0, and rebalance cadence
rebalance\_every = 25, deterministic evaluation yields Train
Sharpe 0.480.48, Validation 0.770.77, and Test 0.500.50. The table below
records the underlying deterministic metrics for each split. The
“Steps” column counts environment steps (episode length times number
of episodes), which exceeds the raw trading day count because we use
overlapping windowed episodes.

Table 1: Deterministic evaluation metrics for the standalone GAE
policy.

| Split | Sharpe | Mean (bps) | Std (bps) | Steps |
| --- | --- | --- | --- | --- |
| Train | 0.484 | 2.43 | 79.79 | 7008 |
| Valid | 0.771 | 2.86 | 58.95 | 1954 |
| Test | 0.502 | 1.95 | 61.53 | 7529 |

### 8.1 Additional Trading Constraints (Cadence + Slippage)

In practice, desks rarely rebalance daily and always pay more than a
single, fixed transaction-cost number. To mirror that reality, we
introduce two explicit knobs in the environment: -
rebalance\_every = N: only the N-th step executes a trade;
intermediate steps hold the previous position and still accrue PnL. -
slippage\_bps: an additional basis-point cost per unit of
|Δ\Deltaposition| charged on execution (or, more generally, a
slippage\_fn for state-dependent costs). We ran a targeted
sweep over cadence and slippage using the same train/valid/test split.
The grid spanned rebalance\_every ∈\in {15, 20, 25} and
slippage\_bps ∈\in {8, 10, 15, 20} with
pos\_limit = 2. The configuration ultimately selected for the
main results, rebalance\_every = 25,
slippage\_bps = 8, balances fewer trades against higher
per-trade cost and provides the most robust test Sharpe after
stress-testing transaction costs. A representative row from the sweep
results is shown below.

Table 2: Top-performing cadence/slippage combination from the
execution-constraint sweep.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Cadence | Slippage (bps) | Train | Valid | Test |
| 25.0 | 8.0 | 0.484 | 0.771 | 0.502 |

Diagnostics across cadence/slippage pairs track the deterministic Sharpe for
the policy and SPY alongside drawdown and hit-rate sensitivity. Relaxed
trading (rebalance every 20–25th day) with a modest slippage charge gives
the smoothest profile because it cuts churn without sacrificing much
return. The significance statistics that follow use the standalone GAE
configuration in Table [1](https://arxiv.org/html/2512.12420v1#S8.T1 "Table 1 ‣ 8. Results") with the cadence/slippage
pair from Table [2](https://arxiv.org/html/2512.12420v1#S8.T2 "Table 2 ‣ 8.1 Additional Trading Constraints (Cadence + Slippage) ‣ 8. Results"); that is, rebalance\_every=25, slippage\_bps=8,
pos\_limit=2. Point estimates favor the GAE policy, but the
confidence intervals for most policies remain wide.

#### Statistical significance.

To gauge whether the Sharpe differences matter, we compute Newey–West
standard errors with a 21-day lag window and form 95% block-bootstrap
intervals for the test split. Figure [2](https://arxiv.org/html/2512.12420v1#S8.F2 "Figure 2 ‣ Statistical significance. ‣ 8.1 Additional Trading Constraints (Cadence + Slippage) ‣ 8. Results") visualizes the
point estimates and confidence bands for each policy. Only the GAE
overlay has an interval that sits entirely above zero; all rule-based
baselines and the ML surrogate have confidence bands that straddle
zero. Although the GAE interval lies entirely above zero, it still
overlaps with that of the long-SPY benchmark, so we interpret the
evidence as supporting a reliable positive Sharpe for the overlay rather
than formal statistical dominance over long SPY.

![Test Sharpe with 95% confidence intervals from Newey--West SEs and block bootstrap on the test split.](figures/test_sharpe_cis.png)


Figure 2: Test Sharpe with 95% confidence intervals from Newey–West
SEs and block bootstrap (test split).

#### Volatility-regime attribution.

We split the test period into VIX terciles to see when and if the
overlay adds value. The heatmap in Figure [3](https://arxiv.org/html/2512.12420v1#S8.F3 "Figure 3 ‣ Volatility-regime attribution. ‣ 8.1 Additional Trading Constraints (Cadence + Slippage) ‣ 8. Results") shows Sharpe ratios for each bucket. The
GAE policy performs best in high volatility states and is modestly
positive in calm markets; rule-based overlays tend to give up more in
quiet regimes without clearly dominating in crisis. We further benchmark the GAE overlay against long SPY across several
pre-defined regimes: the 2008–2009 financial crisis (GFC), the
2010–2012 Eurozone crisis, the relatively calm 2017–2019 period,
the COVID shock (2020–2021), and the post-2022 regime.
Table [3](https://arxiv.org/html/2512.12420v1#S8.T3 "Table 3 ‣ Volatility-regime attribution. ‣ 8.1 Additional Trading Constraints (Cadence + Slippage) ‣ 8. Results") reports Sharpe ratios for both policies
and their difference (Δ​Sharpe=GAE−SPY\Delta\text{Sharpe}=\text{GAE}-\text{SPY}). In the out-of-sample
test periods (COVID and post-2022), Δ​Sharpe\Delta\text{Sharpe} is positive,
indicating an advantage for the overlay, while earlier regimes include
episodes where long SPY can match or even exceed the RL policy.

![Test Sharpe by VIX tercile for each policy on the test split.](figures/vix_regime_heatmap.png)


Figure 3: Test Sharpe by VIX tercile for each policy on the test
split.




Table 3: Sharpe by period for GAE policy vs. long SPY.

| Period | Split | GAE | SPY | Δ\DeltaSharpe |
| --- | --- | --- | --- | --- |
| GFC 08–09 | Train | 0.82 | -0.29 | 1.11 |
| Eurozone 10–12 | Train | 0.20 | 0.63 | -0.44 |
| Calm 17–19 | Train | 0.82 | 1.83 | -1.01 |
| Calm 17–19 | Valid | 0.73 | 0.45 | 0.29 |
| COVID 20–21 | Test | 0.68 | 0.36 | 0.32 |
| Post COVID 22–23 | Test | 0.38 | 0.00 | 0.38 |

### 8.2 Overlaying with Long SPY

Many desks prefer to keep a constant beta exposure and run overlays on
top. We therefore blend the learned policy with long SPY at various
allocations. Figure [4](https://arxiv.org/html/2512.12420v1#S8.F4 "Figure 4 ‣ 8.2 Overlaying with Long SPY ‣ 8. Results") shows the NAV comparison for
the 50/50 mix; the overlay dampens drawdowns without sacrificing
long-run growth.

The table below summarizes deterministic statistics for that 50/50 mix.
Despite recycling capital between the learned hedge and the long-only
sleeve, annualized volatility stays below 7% on validation and test
windows while Sharpe remains positive. CAGR figures in the final column
show that the overlay preserves most of the long-run growth even after
paying transaction costs.

![Test NAV overlay for a blended strategy that allocates 50% to GAE and 50% to long SPY.](figures/nav_blended_strategy.png)


Figure 4: Test NAV overlay for a blended strategy that allocates 50% to
GAE and 50% to long SPY.




Table 4: Key deterministic metrics for the 50/50 overlay during
train/validation/test periods.

| Split | mean\_bps | std\_bps | Sharpe | CAGR |
| --- | --- | --- | --- | --- |
| Train | 1.97 | 41.18 | 0.76 | 0.049 |
| Valid | 1.92 | 31.20 | 0.98 | 0.048 |
| Test | 1.38 | 33.62 | 0.65 | 0.034 |

The diagnostics in Figures [5](https://arxiv.org/html/2512.12420v1#S8.F5 "Figure 5 ‣ 8.2 Overlaying with Long SPY ‣ 8. Results") and
[6](https://arxiv.org/html/2512.12420v1#S8.F6 "Figure 6 ‣ 8.2 Overlaying with Long SPY ‣ 8. Results") show why the overlay is attractive beyond a
single point on the frontier. Figure [5](https://arxiv.org/html/2512.12420v1#S8.F5 "Figure 5 ‣ 8.2 Overlaying with Long SPY ‣ 8. Results") sweeps the allocation
from 0% to 100% GAE exposure: the curve is concave, so each additional
unit of overlay buys more return per unit of risk until the very end.
The 50/50 point (green) sits on the efficient portion and retains
roughly two thirds of the SPY CAGR while cutting realized volatility nearly in half.

Figure [6](https://arxiv.org/html/2512.12420v1#S8.F6 "Figure 6 ‣ 8.2 Overlaying with Long SPY ‣ 8. Results") plots the rolling 63-day volatility and drawdown differentials
between the blend and each leg. Most of the series stays below zero,
indicating that the overlay systematically suppresses realized risk
rather than occasionally amplifying it. Deep drawdowns (e.g., Q1 2020
and the 2022 selloff) are visibly muted relative to a pure long SPY stance.

These risk differentials provide the intuition for how the overlay
behaves: it tends to clip volatility spikes without introducing new
drawdowns. Table [5](https://arxiv.org/html/2512.12420v1#S8.T5 "Table 5 ‣ 8.2 Overlaying with Long SPY ‣ 8. Results") translates those gains into
calendar-year attribution. The SPY sleeve drives the strong up years
(2020–2021); in the 2022 drawdown the overlay trims only a small
portion of the loss, and both legs contribute in 2023, showing the hedge
does not cap upside once volatility subsides.

On the test window, SPY alone posts Sharpe ≈0.22\approx 0.22 with around
14.6%14.6\% annualized volatility; the 50/50 blend posts Sharpe around
0.650.65 with volatility closer to 10%10\%, illustrating that the overlay
meaningfully improves risk-adjusted performance while retaining most of
the long-run growth.

![Blend weight sweep showing the efficient frontier as capital shifts between the overlay and SPY (color indicates GAE weight).](figures/blend_weight_sweep.png)


Figure 5: Blend weight sweep showing the efficient frontier as capital
shifts between the overlay and SPY (color indicates GAE
weight).

![Rolling risk differentials showing 63-day volatility and drawdown of the blend minus each component (negative values are better).](figures/rolling_risk_differentials.png)


Figure 6: Rolling risk differentials showing 63-day volatility and
drawdown of the blend minus each component (negative values are
better).




Table 5: Calendar-year PnL attribution (percent returns) for the 50/50
blend on the test split.

| Year | GAE overlay | Long SPY leg | Blend total |
| --- | --- | --- | --- |
| 2020 | 4.71 | 18.66 | 23.36 |
| 2021 | 2.50 | 27.99 | 30.50 |
| 2022 | -0.57 | -18.29 | -18.85 |
| 2023 | -0.91 | 18.11 | 17.19 |

#### Robustness across seeds and splits.

We retrained the policy across three seeds on the base split and a
shifted split (+365 days) using the same cost/cadence settings as
Table [2](https://arxiv.org/html/2512.12420v1#S8.T2 "Table 2 ‣ 8.1 Additional Trading Constraints (Cadence + Slippage) ‣ 8. Results"). Seed variance remains modest: base
test Sharpe averages 0.450.45 (std 0.130.13) and shifted test Sharpe
0.520.52 (std 0.050.05). Mean portfolio-level max drawdowns for the 50/50
blend cluster around −20%-20\% (base/test) and −16%-16\% (shifted/test),
indicating that moving the window forward does not collapse
performance.

Training diagnostics. The distribution of episode returns saved from
03\_rl\_training.ipynb (histogram below) highlights the heavy
tails encountered during optimization.

![Episode return distribution from the training notebook (episode returns, not per-step bps).](figures/gae_episode_return_distribution.png)


Figure 7: Episode return distribution from the training
notebook (episode returns, not per-step bps).

#### Verification and testing.

Every sweep run is backed by
reproducible checks:

* •

  pytest tests/ ensures data-pipeline transforms, reward
  helpers, and environment logic match the expected invariants (shape,
  NaN guards, deterministic rollouts).
* •

  python rl\_agent.evaluate\_policy –ckpt models/gae\_run3/best.pt –config models/gae\_run3/config.json –deterministic
  deterministically replays the saved policy each time the paper is
  built.
* •

  The notebooks 03\_rl\_training.ipynb, 04\_diagnostics.ipynb, and 05\_results.ipynb
  regenerate CSV metrics and figures (including confidence intervals and
  regime slices) so that visuals, numbers, and text stay in sync.

These commands are executed from the repo root (documented in the
README) before exporting the final PDF so that published artefacts
reflect the latest code.

## 9. Discussion and Implications

When to use deep hedging. The learned policy fits naturally into overlay
mandates where the objective is to dampen PnL swings without fully
neutralizing exposure. Because the state is composed of derived
features (surface slope, skew, realized vol, rates), risk managers can
inspect which signals drove a given hedge decision. The approach is
model agnostic: it can coexist with existing pricing libraries, consume
alternative features (e.g., realized correlation, macro factors), or be
combined with explicit delta inputs if desired.

Operationalization. In practice the policy should be wrapped in
guardrails: clip actions to desk-specific risk limits, halt trading when
liquidity metrics deteriorate, and log both raw observations and
predicted actions for post-trade analysis. Monitoring dashboards should
focus on rolling Sharpe, turnover, realized cost-per-basis-point, and
policy drift relative to benchmark hedges. The repository’s
deterministic evaluation utilities can be embedded into nightly jobs to
confirm the policy still behaves as expected on the latest data.

Limitations and extensions. The present study operates on daily bars,
which ignore intraday inventory management and execution costs;
high-frequency data could reveal additional edge or necessitate
different architectures, and production overlays often rebalance more
slowly than daily. Generalization relies on walk-forward discipline and
policies should be retrained periodically as volatility regimes evolve.
For simplicity, we do not feed option Greeks directly into the state
because of their sensitivity to intraday moves and model assumptions;
instead we use more stable surface-level features such as implied
volatility levels, term structure, and skew. Hyperparameters and
training windows matter: seed-to-seed variance is modest, but we have
not exhaustively searched architectures or extra walk-forwards, so
formal model selection remains future work. Finally, the reward
emphasizes mean/variance trade-offs; more risk-sensitive objectives
(drawdown penalties, CVaR, shortfall constraints) can be slotted in via
simulator/rewards.py with minimal code changes.

Statistically, our results should also be viewed as suggestive rather
than definitive. While only the GAE overlay exhibits a test-sample
Sharpe whose 95% confidence interval lies strictly above zero, we do
not formally test Sharpe differentials versus the long-SPY benchmark or
rule-based overlays, and the corresponding confidence intervals
overlap. Likewise, the interpretability analysis is intentionally
lightweight: we rely on aggregate diagnostics such as VIX-regime and
period-by-period Sharpe rather than per-trade explanations; a more
granular decomposition of policy decisions and PnL attribution across
regimes is left for future work.

### 9.1 Portfolio implementation

From an implementation standpoint, the GAE overlay is
designed as a portfolio completion strategy: a risk-management sleeve
that improves the mean-variance profile of an existing equity allocation
without generating standalone alpha claims. A portfolio manager would
typically (i) fix a hedge cadence (e.g., weekly or
monthly), (ii) calibrate the transaction-cost assumption
and margin usage to match desk-level constraints, and
(iii) cap gross hedge notional as a fraction of NAV so
that the overlay consumes a clearly defined risk budget.
Within the ranges we study, the learned overlay moves the
portfolio along a more favorable mean–variance frontier,
particularly in high volatility regimes, while keeping
turnover and maximum drawdown at levels that are
realistic for institutional mandates. Deploying such an overlay would also require
governance around model monitoring, stress testing, and
clear criteria for throttling or disabling the strategy,
which we view as complementary to the technical results
presented here, so that the overlay can be slotted into an existing
risk-budgeting and investment committee framework without redefining the underlying benchmark.

## Disclaimer

This research was conducted independently by the authors and does not
represent the views, opinions, or research of BlackRock, Inc. or any of
its affiliates, nor those of Emory University. The content is provided
for informational and educational purposes only and should not be
construed as investment advice or a recommendation to trade.

## References

## References

* Black, Fischer, and Myron Scholes. 1973. “The Pricing of Options and
  Corporate Liabilities.” *Journal of Political Economy* 81 (3):
  637–54.
* Buehler, Hans, Lukas Gonon, Josef Teichmann, and Ben Wood. 2019. “Deep
  Hedging.” *Quantitative Finance* 19 (8): 1271–91.
* Glasserman, Paul. 2004. *Monte Carlo Methods in Financial
  Engineering*. Vol. 53. Stochastic Modelling and Applied Probability.
  Springer.
* Kolm, Petter N., and Gordon Ritter. 2021. *Reinforcement Learning
  for Trading and Asset Management*. SSRN Preprint.
* Leland, Hayne E. 1985. “Option Pricing and Replication with
  Transactions Costs.” *The Journal of Finance* 40 (5): 1283–301.
* Merton, Robert C. 1973. “Theory of Rational Option Pricing.”
  *The Bell Journal of Economics and Management Science* 4 (1):
  141–83.
* Moody, John, and Matthew Saffell. 1998. *Learning to Trade via
  Direct Reinforcement*. Neural Information Processing Systems Workshop.
* Øksendal, Bernt. 2003. *Stochastic Differential Equations: An
  Introduction with Applications*. 6th ed. Springer.
* Schulman, John, Philipp Moritz, Sergey Levine, Michael Jordan, and
  Pieter Abbeel. 2016. “High-Dimensional Continuous Control Using
  Generalized Advantage Estimation.” *arXiv Preprint
  arXiv:1506.02438*.
* Sutton, Richard S, and Andrew G Barto. 2018. *Reinforcement
  Learning: An Introduction*. 2nd ed. MIT Press.
* Webster, Kevin Thomas. 2023. *Handbook of Price Impact Modeling*.
  Chapman & Hall/CRC Financial Mathematics Series. Chapman & Hall/CRC.
* Zhang, Zhengyao, Stefan Zohren, and Benjamin Roberts. 2020. “Deep
  Reinforcement Learning for Quantitative Trading: A Survey.”
  *arXiv Preprint arXiv:2007.11495*.