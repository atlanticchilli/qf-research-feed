---
authors:
- Valerii Kremnev
doc_id: arxiv:2601.01269v1
family_id: arxiv:2601.01269
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Critical Volatility Threshold for Log-Normal to Power-Law Transition
url_abs: http://arxiv.org/abs/2601.01269v1
url_html: https://arxiv.org/html/2601.01269v1
venue: arXiv q-fin
version: 1
year: 2026
---


Valerii Kremnev

(January 2026)

## Critical Volatility Threshold for Log-Normal to Power-Law Transition: Iterated Options Model

### Abstract

Random walk models with log-normal outcomes fit local market
observations remarkably well. Yet interconnected or recursive structures
- layered derivatives, leveraged positions, iterative funding rounds -
periodically produce power-law distributed events. We show that the
transition from log-normal to power-law dynamics requires only three
conditions: randomness in the underlying process, rectification of
payouts, and iterative feed-forward of expected values. Using an
infinite option-on-option chain as an illustrative model, we derive a
critical volatility threshold at
σ∗=2​π≈250.66%\sigma^{\*}=\sqrt{2\pi}\approx 250.66\% for the unconditional case.
With selective survival - where participants require minimum returns to
continue - the critical threshold drops discontinuously to
σth∗=π/2≈125.3%\sigma\_{\text{th}}^{\*}=\sqrt{\pi/2}\approx 125.3\%, and can
decrease further with higher survival thresholds. The resulting outcomes
follow what we term the Critical Volatility (V\*) Distribution - a
power-law whose exponent admits closed-form expression in terms of
survival pressure and conditional expected growth. The result suggests
that fat tails may be an emergent property of iterative log-normal
processes with selection rather than an exogenous feature.

### Preface

Financial systems are built on rectified payoffs. An investment in a
high-risk project returns either something or nothing - you cannot lose
more than you put in. An option pays max⁡(S−K,0)\max(S-K,0). Even limited
liability is a form of rectification.

These rectified structures often feed into one another. A successful
project enables others built on top of it. A successful trade becomes
the capital for the next trade. Derivative products reference other
derivative products. It would be useful to know how such iterations
behave - whether they remain stable or exhibit qualitatively different
dynamics.

To answer this, we analyze the limiting case: an infinite chain of
options, each written on the expected payout of the one before. The
result depends on three conditions - randomness in the underlying
process, rectification of payouts, and feed-forward of expected values.
These are sufficient to produce a critical threshold at
σ∗=2​π≈250.66%\sigma^{\*}=\sqrt{2\pi}\approx 250.66\%. Below this, cumulative
optionality remains bounded. Above it, the system diverges. With
selective survival - participants requiring minimum returns to continue
- the threshold drops to
σth∗=π/2≈125.3%\sigma\_{\text{th}}^{\*}=\sqrt{\pi/2}\approx 125.3\%. The divergent
outcomes follow what we term the V\* Distribution - a power-law whose
exponent depends on the specific volatility and participants’
willingness to make the next bet.

We also identify a self-similar regime at exactly the critical
threshold, where each iteration reproduces the statistical structure of
the previous one.

The conditions are minimal: randomness, bounded downside, and iteration.
These are not exotic assumptions, suggesting the mechanism may apply
broadly to dynamic systems with compounding behavior.

As for the infinite derivative tower itself: to our knowledge, no one
has built one. This is probably wise. But should financial engineering
continue its march toward increasingly layered products, at least the
location of the cliff is now known.

### 1. Introduction and Motivation

The Black-Scholes framework provides a foundational model for pricing
European options. Under risk-neutral valuation, the price of a call
option reflects the expected value of its payoff max⁡(ST−K,0)\max(S\_{T}-K,0),
discounted appropriately. This “rectification” - the maximum of a
potentially negative quantity and zero - is the essential nonlinearity
that gives options their asymmetric payoff structure.

A natural question arises: what happens when we write an option on an
option? And then an option on that? In principle, one could construct an
arbitrarily deep tower of such instruments, each layer deriving its
value from the expected payout of the layer below.

This paper analyzes the mathematical structure of such iterated
rectified expectations. We find that:

1. 1.

   The system exhibits a phase transition at a critical volatility of
   σ∗=2​π≈250.66%\sigma^{\*}=\sqrt{2\pi}\approx 250.66\% annualized for the
   unconditional ATM case. This assumes the perfect case, where pricing
   has no errors and volatility doesn’t amplify between derivative layers
   but stays perfectly correlated to asset price at a constant ratio.
   Real systems, if built, will diverge much faster.
2. 2.

   Below criticality (σ<σ∗\sigma<\sigma^{\*}), the total value of an
   infinite option chain converges to a finite sum, meaning optionality
   is “bounded” no matter how many layers are added.
3. 3.

   Above criticality (σ>σ∗\sigma>\sigma^{\*}), the chain diverges - the
   cumulative value of optionality exceeds the underlying asset itself.
   This is not merely a mathematical curiosity; it implies that in
   extreme volatility regimes, the optionality can dominate the
   fundamental value of the product. This leads to amplification of
   expected payout at each consecutive step, making the expected payouts
   follow power-law dynamics.
4. 4.

   At criticality (σ=σ∗\sigma=\sigma^{\*}), the system becomes
   self-similar, with each iteration reproducing the statistical
   structure of the previous one.
5. 5.

   With selective survival - where participants require minimum returns
   to continue - the critical threshold drops to
   σth∗=π/2≈125.3%\sigma\_{\text{th}}^{\*}=\sqrt{\pi/2}\approx 125.3\%. Power-law
   dynamics (the V\* Distribution) emerge when βeff>1\beta\_{\text{eff}}>1,
   where βeff\beta\_{\text{eff}} is the conditional expected growth given
   survival.

These findings have implications for understanding volatility regimes
during market stress, the pricing of compound options, and the
theoretical limits of derivative layering.

### 2. The Black-Scholes Setup

#### 2.1 Standard Framework

Under the Black-Scholes model, the underlying asset follows geometric
Brownian motion:

|  |  |  |
| --- | --- | --- |
|  | d​St=μ​St​d​t+σ​St​d​WtdS\_{t}=\mu S\_{t}\,dt+\sigma S\_{t}\,dW\_{t} |  |

The Black-Scholes formula for a European call option is:

|  |  |  |
| --- | --- | --- |
|  | C​(St,t)=N​(d+)​St−N​(d−)​K​e−r​(T−t)C(S\_{t},t)=N(d\_{+})S\_{t}-N(d\_{-})Ke^{-r(T-t)} |  |

where:

|  |  |  |
| --- | --- | --- |
|  | d+=1σ​T−t​[ln⁡(StK)+(r+σ22)​(T−t)]d\_{+}=\frac{1}{\sigma\sqrt{T-t}}\left[\ln\left(\frac{S\_{t}}{K}\right)+\left(r+\frac{\sigma^{2}}{2}\right)(T-t)\right] |  |

|  |  |  |
| --- | --- | --- |
|  | d−=d+−σ​T−td\_{-}=d\_{+}-\sigma\sqrt{T-t} |  |

and N​(⋅)N(\cdot) is the standard normal CDF.

#### 2.2 ATM Special Case

For an at-the-money option where St=KS\_{t}=K, we have
ln⁡(St/K)=0\ln(S\_{t}/K)=0, so:

|  |  |  |
| --- | --- | --- |
|  | d+=r+σ2/2σ​T−td\_{+}=\frac{r+\sigma^{2}/2}{\sigma}\sqrt{T-t} |  |

|  |  |  |
| --- | --- | --- |
|  | d−=r−σ2/2σ​T−td\_{-}=\frac{r-\sigma^{2}/2}{\sigma}\sqrt{T-t} |  |

In the r≪σr\ll\sigma limit (which holds for high-volatility regimes
where σ>100%\sigma>100\% and r≈5%r\approx 5\%):

|  |  |  |
| --- | --- | --- |
|  | d+≈σ2/2σ​T−t=σ2​T−td\_{+}\approx\frac{\sigma^{2}/2}{\sigma}\sqrt{T-t}=\frac{\sigma}{2}\sqrt{T-t} |  |

|  |  |  |
| --- | --- | --- |
|  | d−≈−σ2/2σ​T−t=−σ2​T−td\_{-}\approx\frac{-\sigma^{2}/2}{\sigma}\sqrt{T-t}=-\frac{\sigma}{2}\sqrt{T-t} |  |

Since d−≈−d+d\_{-}\approx-d\_{+}, we have N​(d−)=N​(−d+)=1−N​(d+)N(d\_{-})=N(-d\_{+})=1-N(d\_{+}),
and the option price simplifies to:

|  |  |  |
| --- | --- | --- |
|  | C=K​[N​(d+)−N​(d−)]=K​[2​N​(σ​T−t2)−1]C=K\left[N(d\_{+})-N(d\_{-})\right]=K\left[2N\left(\frac{\sigma\sqrt{T-t}}{2}\right)-1\right] |  |

The ATM option price reduces to a single Gaussian CDF minus a constant.
Let us analyze its behavior.

#### 2.3 The Gaussian Structure

The Gaussian distribution appears explicitly in Black-Scholes through
N​(d+)N(d\_{+}) and N​(d−)N(d\_{-}), and simplifies to a single Gaussian CDF under
the high-volatility ATM assumption. We observe that the option payoff
max⁡(ST−K,0)\max(S\_{T}-K,0) cannot be negative by definition - the option
structure rectifies the underlying returns at zero.

The expected value of a rectified Gaussian is the mathematical core of
option pricing. We now analyze the general case of
𝔼​[max⁡(X,0)]\mathbb{E}[\max(X,0)] for X∼𝒩​(μ,σ2)X\sim\mathcal{N}(\mu,\sigma^{2}).

In the following mathematical derivation, σ\sigma denotes the
standard deviation of the distribution
X∼𝒩​(μ,σ2)X\sim\mathcal{N}(\mu,\sigma^{2}), following standard statistical
convention, not the scale-less volatility.

#### 2.4 Rectified Gaussian Expectations

Let Y=max⁡(X,0)Y=\max(X,0) where X∼𝒩​(μ,σ2)X\sim\mathcal{N}(\mu,\sigma^{2}). We
seek 𝔼​[Y]\mathbb{E}[Y].

The expectation splits into two regions:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Y]=𝔼​[X⋅𝟏X>0]=∫0∞x⋅1σ​2​π​e−(x−μ)2/2​σ2​𝑑x\mathbb{E}[Y]=\mathbb{E}[X\cdot\mathbf{1}\_{X>0}]=\int\_{0}^{\infty}x\cdot\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^{2}/2\sigma^{2}}dx |  |

Substituting u=(x−μ)/σu=(x-\mu)/\sigma:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Y]=∫−μ/σ∞(μ+σ​u)⋅12​π​e−u2/2​𝑑u\mathbb{E}[Y]=\int\_{-\mu/\sigma}^{\infty}(\mu+\sigma u)\cdot\frac{1}{\sqrt{2\pi}}e^{-u^{2}/2}du |  |

This separates into:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Y]=μ​∫−μ/σ∞ϕ​(u)​𝑑u+σ​∫−μ/σ∞u⋅ϕ​(u)​𝑑u\mathbb{E}[Y]=\mu\int\_{-\mu/\sigma}^{\infty}\phi(u)\,du+\sigma\int\_{-\mu/\sigma}^{\infty}u\cdot\phi(u)\,du |  |

The first integral is μ⋅Φ​(μ/σ)\mu\cdot\Phi(\mu/\sigma). For the second,
note that u⋅ϕ​(u)=−ϕ′​(u)u\cdot\phi(u)=-\phi^{\prime}(u), so:

|  |  |  |
| --- | --- | --- |
|  | ∫−μ/σ∞u⋅ϕ​(u)​𝑑u=[−ϕ​(u)]−μ/σ∞=ϕ​(μ/σ)\int\_{-\mu/\sigma}^{\infty}u\cdot\phi(u)\,du=\left[-\phi(u)\right]\_{-\mu/\sigma}^{\infty}=\phi(\mu/\sigma) |  |

Therefore:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Y]=μ​Φ​(μσ)+σ​ϕ​(μσ)\mathbb{E}[Y]=\mu\Phi\left(\frac{\mu}{\sigma}\right)+\sigma\phi\left(\frac{\mu}{\sigma}\right) |  |

where Φ​(⋅)\Phi(\cdot) is the standard normal CDF and ϕ​(⋅)\phi(\cdot) is
the standard normal PDF.

#### 2.5 The Function g(z)

Normalizing by σ\sigma and letting z=μ/σz=\mu/\sigma:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Y]σ=z​Φ​(z)+ϕ​(z)\frac{\mathbb{E}[Y]}{\sigma}=z\Phi(z)+\phi(z) |  |

Expanding using the integral forms of Φ\Phi and ϕ\phi:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Y]σ=12​π​(z​∫−∞ze−t2/2​𝑑t+e−z2/2)\frac{\mathbb{E}[Y]}{\sigma}=\frac{1}{\sqrt{2\pi}}\left(z\int\_{-\infty}^{z}e^{-t^{2}/2}dt+e^{-z^{2}/2}\right) |  |

We define:

|  |  |  |
| --- | --- | --- |
|  | g​(z)=z​∫−∞ze−t2/2​𝑑t+e−z2/2g(z)=z\int\_{-\infty}^{z}e^{-t^{2}/2}dt+e^{-z^{2}/2} |  |

so that the expected value of the rectified Gaussian becomes:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Y]=σ2​π​g​(z)\mathbb{E}[Y]=\frac{\sigma}{\sqrt{2\pi}}g(z) |  |

This form will be essential for analyzing iterations.

### 3. Iterated Options: The Mathematical Structure

#### 3.1 The Iteration Scheme

Consider a chain of options where each option is written on the expected
payout of the previous one. In a simplified model of such chain, we
would be putting a new derivative instrument with the price of expected
payout of the previous one, and calculate new parameters. Since the
strike price from previous option would be just a constant multiplier,
we can focus on analyzing the rectified Gaussian behavior as a
simplified model.

Let μn\mu\_{n} denote the expected value at stage nn, and suppose each
stage has volatility σn\sigma\_{n}.

From Section 2.5, the expected value of the rectified Gaussian at stage
nn is:

|  |  |  |
| --- | --- | --- |
|  | 𝔼n​[Y]=σn2​π​g​(zn)\mathbb{E}\_{n}[Y]=\frac{\sigma\_{n}}{\sqrt{2\pi}}g(z\_{n}) |  |

where zn=μn/σnz\_{n}=\mu\_{n}/\sigma\_{n}.

If we let the output of one rectification become the mean of the next
(i.e., μn+1=𝔼n​[Y]\mu\_{n+1}=\mathbb{E}\_{n}[Y]), we obtain:

|  |  |  |
| --- | --- | --- |
|  | μn+1=σn2​π​g​(zn)\mu\_{n+1}=\frac{\sigma\_{n}}{\sqrt{2\pi}}g(z\_{n}) |  |

#### 3.2 General Recursion

From Section 2.5:

|  |  |  |
| --- | --- | --- |
|  | 𝔼1​[Y]=σ12​π​g​(z1)\mathbb{E}\_{1}[Y]=\frac{\sigma\_{1}}{\sqrt{2\pi}}g(z\_{1}) |  |

Let the output become the mean of the next stage:
μ2=𝔼1​[Y]\mu\_{2}=\mathbb{E}\_{1}[Y].

The next price is:

|  |  |  |
| --- | --- | --- |
|  | z2=μ2σ2=σ1σ2⋅12​π​g​(z1)z\_{2}=\frac{\mu\_{2}}{\sigma\_{2}}=\frac{\sigma\_{1}}{\sigma\_{2}}\cdot\frac{1}{\sqrt{2\pi}}g(z\_{1}) |  |

Let r=σ1/σ2r=\sigma\_{1}/\sigma\_{2} and w=g​(z1)w=g(z\_{1}). Then:

|  |  |  |
| --- | --- | --- |
|  | z2=r2​π​wz\_{2}=\frac{r}{\sqrt{2\pi}}w |  |

The next expectation:

|  |  |  |
| --- | --- | --- |
|  | 𝔼2​[Y]=σ22​π​g​(z2)\mathbb{E}\_{2}[Y]=\frac{\sigma\_{2}}{\sqrt{2\pi}}g(z\_{2}) |  |

More generally, letting wn=g​(zn)w\_{n}=g(z\_{n}) and
α=r2​π\alpha=\frac{r}{\sqrt{2\pi}}:

|  |  |  |
| --- | --- | --- |
|  | wn+1=g​(α⋅wn)w\_{n+1}=g(\alpha\cdot w\_{n}) |  |

Explicitly:

|  |  |  |
| --- | --- | --- |
|  | wn+1=α​wn​∫−∞α​wne−t2/2​𝑑t+e−α2​wn2/2w\_{n+1}=\alpha w\_{n}\int\_{-\infty}^{\alpha w\_{n}}e^{-t^{2}/2}\,dt+e^{-\alpha^{2}w\_{n}^{2}/2} |  |

This is a nonlinear recursion whose behavior depends critically on
α\alpha.

#### 3.3 The Self-Similar Case

When α=1\alpha=1 (equivalently, r=2​πr=\sqrt{2\pi}, i.e.,
σ1=σ2​2​π\sigma\_{1}=\sigma\_{2}\sqrt{2\pi}), the recursion simplifies to:

|  |  |  |
| --- | --- | --- |
|  | wn+1=g​(wn)w\_{n+1}=g(w\_{n}) |  |

This is pure iteration of gg - the process becomes self-similar. The
ratio:

|  |  |  |
| --- | --- | --- |
|  | wnwn+1=wng​(wn)\frac{w\_{n}}{w\_{n+1}}=\frac{w\_{n}}{g(w\_{n})} |  |

suggests that the sequence will have its own convergence/divergence
behavior depending on wnw\_{n} (or equivalently α\alpha). The
parameter α\alpha controls how the recursion scales, determining
whether iterated expectations grow, shrink, or stabilize.

### 4. The Recentered (ATM) Case

#### 4.1 Introducing the Shift

In practice, options are often struck at-the-money (ATM), where the
strike equals the current expected value. We model this by introducing a
shift parameter sns\_{n} that recenters the distribution at each step:

|  |  |  |
| --- | --- | --- |
|  | zns=μn−snσn=zn−snσnz\_{n}^{s}=\frac{\mu\_{n}-s\_{n}}{\sigma\_{n}}=z\_{n}-\frac{s\_{n}}{\sigma\_{n}} |  |

Setting sn=μns\_{n}=\mu\_{n} (the ATM condition) forces zns=0z\_{n}^{s}=0 at
every iteration.

The intuition for this shift is the following: each new option is
written ATM at inception, with strike equal to the current underlying
price (which is the expected value from the previous stage). The
underlying then fluctuates around this strike with its own volatility
over the holding period. Since the strike equals the mean, the
payoff-relevant distribution is centered at zero.

#### 4.2 Evaluation at Zero

Since g​(0)=0+e0=1g(0)=0+e^{0}=1, the shifted expectation simplifies
dramatically:

|  |  |  |
| --- | --- | --- |
|  | 𝔼ns​[Y]=σn2​π\mathbb{E}\_{n}^{s}[Y]=\frac{\sigma\_{n}}{\sqrt{2\pi}} |  |

This is the well-known result that an ATM option’s expected payout
(before discounting and without market price multiplier) is proportional
to volatility. It connects directly to the well-known practitioner’s
approximation:

|  |  |  |
| --- | --- | --- |
|  | C≈S⋅σ​T2​π≈0.4⋅S⋅σ​TC\approx\frac{S\cdot\sigma\sqrt{T}}{\sqrt{2\pi}}\approx 0.4\cdot S\cdot\sigma\sqrt{T} |  |

#### 4.3 The Geometric Regime

In financial contexts, we frequently assume that volatility is a
percentage related to the price - a stock with higher price has
proportionally higher absolute volatility. We use a similar definition
which scales with expected values.

We now return to the finance convention where σ\sigma denotes
percentage volatility (coefficient of variation, σn/μn\sigma\_{n}/\mu\_{n}).
Assuming constant percentage volatility (absolute volatility scales
proportionally with price):

|  |  |  |
| --- | --- | --- |
|  | μn+1=σ⋅μn2​π=β⋅μn\mu\_{n+1}=\frac{\sigma\cdot\mu\_{n}}{\sqrt{2\pi}}=\beta\cdot\mu\_{n} |  |

where β=σ/2​π\beta=\sigma/\sqrt{2\pi}.

This yields the closed form:

|  |  |  |
| --- | --- | --- |
|  | μn=μ1⋅βn−1\mu\_{n}=\mu\_{1}\cdot\beta^{n-1} |  |

The expected value at each stage forms a geometric sequence.

### 5. Convergence and the Critical Threshold

#### 5.1 Sum of the Infinite Chain

The total expected value across an infinite chain of ATM options is:

|  |  |  |
| --- | --- | --- |
|  | ∑n=1∞μn=μ1​∑n=0∞βn=μ11−β\sum\_{n=1}^{\infty}\mu\_{n}=\mu\_{1}\sum\_{n=0}^{\infty}\beta^{n}=\frac{\mu\_{1}}{1-\beta} |  |

This converges if and only if β<1\beta<1.

#### 5.2 The Critical Volatility

The convergence condition β<1\beta<1 translates to:

|  |  |  |
| --- | --- | --- |
|  | σ2​π<1⟹σ<2​π≈2.5066\frac{\sigma}{\sqrt{2\pi}}<1\implies\sigma<\sqrt{2\pi}\approx 2.5066 |  |

In percentage terms, the critical volatility is
σ∗≈250.66%\sigma^{\*}\approx 250.66\% annualized.

#### 5.3 Closed Form for the Sum

When σ<2​π\sigma<\sqrt{2\pi}:

|  |  |  |
| --- | --- | --- |
|  | ∑n=1∞μn=μ1​2​π2​π−σ\sum\_{n=1}^{\infty}\mu\_{n}=\frac{\mu\_{1}\sqrt{2\pi}}{\sqrt{2\pi}-\sigma} |  |

### 6. Divergence and Power-Law Beyond the Critical Threshold

#### 6.1 Exponential Growth in the Supercritical Regime

When σ>2​π\sigma>\sqrt{2\pi}, we have
β=σ/2​π>1\beta=\sigma/\sqrt{2\pi}>1, and the expected values grow
exponentially:

|  |  |  |
| --- | --- | --- |
|  | μn=μ1⋅βn−1\mu\_{n}=\mu\_{1}\cdot\beta^{n-1} |  |

Each iteration amplifies the previous expected value. The total sum
diverges - there is no finite bound on cumulative optionality.

#### 6.2 Survival Condition and Power-Law Emergence

On the real market, participants do not receive the expected value -
they receive a realized draw from the distribution. The ability of
players to continue playing depends on their outcomes and risk
tolerance.

We can take simplified option-like model which scales payoff with the
bet, and assume payoff is max⁡(X,0)\max(X,0) where
X∼𝒩​(0,σ​w)X\sim\mathcal{N}(0,\sigma w) - a zero-centered Gaussian.
Participants require a minimum return to justify continued risk-taking.
Let kthk\_{\text{th}} be the threshold multiplier: participants survive
only if their payoff exceeds kth⋅wk\_{\text{th}}\cdot w.

Since the payoff must be positive and exceed the threshold, survival
requires X≥kth⋅wX\geq k\_{\text{th}}\cdot w. Standardizing to
Z=X/(σ​w)Z=X/(\sigma w) where Z∼𝒩​(0,1)Z\sim\mathcal{N}(0,1):

|  |  |  |
| --- | --- | --- |
|  | P​(survive)=P​(Z≥kthσ)=1−Φ​(kthσ)P(\text{survive})=P\left(Z\geq\frac{k\_{\text{th}}}{\sigma}\right)=1-\Phi\left(\frac{k\_{\text{th}}}{\sigma}\right) |  |

For example, with σ=3\sigma=3 and kth=2.5k\_{\text{th}}=2.5, we have
kth/σ≈0.833k\_{\text{th}}/\sigma\approx 0.833, giving p≈0.20p\approx 0.20 (20%
survival rate per round).

The probability of surviving nn consecutive stages is:

|  |  |  |
| --- | --- | --- |
|  | P​(survive ​n​ stages)=pnP(\text{survive }n\text{ stages})=p^{n} |  |

Among survivors, the expected wealth multiplier per stage is the
conditional expectation given survival. For the zero-centered
truncated normal:

|  |  |  |
| --- | --- | --- |
|  | βeff=𝔼​[Xw|X≥kth​w]=σ⋅ϕ​(kth/σ)1−Φ​(kth/σ)=σ⋅ϕ​(kth/σ)p\beta\_{\text{eff}}=\mathbb{E}\left[\frac{X}{w}\,\Big|\,X\geq k\_{\text{th}}w\right]=\sigma\cdot\frac{\phi(k\_{\text{th}}/\sigma)}{1-\Phi(k\_{\text{th}}/\sigma)}=\sigma\cdot\frac{\phi(k\_{\text{th}}/\sigma)}{p} |  |

where ϕ\phi is the standard normal PDF.

The V\* Critical Threshold. The phase transition to power-law
behavior occurs when βeff=1\beta\_{\text{eff}}=1. Setting
z=kth/σz=k\_{\text{th}}/\sigma, this condition gives:

|  |  |  |
| --- | --- | --- |
|  | σcritical=1−Φ​(z)ϕ​(z)\sigma\_{\text{critical}}=\frac{1-\Phi(z)}{\phi(z)} |  |

This is the inverse Mills ratio. As z→0+z\to 0^{+} (threshold approaching
zero from above):

|  |  |  |
| --- | --- | --- |
|  | σth∗=limz→0+1−Φ​(z)ϕ​(z)=0.51/2​π=π2≈1.253≈125.3%\sigma\_{\text{th}}^{\*}=\lim\_{z\to 0^{+}}\frac{1-\Phi(z)}{\phi(z)}=\frac{0.5}{1/\sqrt{2\pi}}=\sqrt{\frac{\pi}{2}}\approx 1.253\approx 125.3\% |  |

This reveals a second critical constant: the moment any positive
survival threshold is introduced, the critical volatility drops from
σ∗=2​π≈250.66%\sigma^{\*}=\sqrt{2\pi}\approx 250.66\% to
σth∗=π/2≈125.3%\sigma\_{\text{th}}^{\*}=\sqrt{\pi/2}\approx 125.3\%. This happens
because filtering out participants with X<0X<0 (approximately half
the population) doubles the conditional growth rate of survivors.

For higher thresholds (z>0z>0), the critical volatility decreases
further. The critical curve in (σ,kth)(\sigma,k\_{\text{th}}) space is
parameterized by:

|  |  |  |
| --- | --- | --- |
|  | σcritical​(z)=1−Φ​(z)ϕ​(z),kth, critical​(z)=z⋅1−Φ​(z)ϕ​(z)\sigma\_{\text{critical}}(z)=\frac{1-\Phi(z)}{\phi(z)},\quad k\_{\text{th, critical}}(z)=z\cdot\frac{1-\Phi(z)}{\phi(z)} |  |

The number of surviving processes decays exponentially (pnp^{n}), but
when βeff>1\beta\_{\text{eff}}>1, the value of each survivor grows
exponentially (βeffn\beta\_{\text{eff}}^{n}). This combination produces
power-law distributed outcomes.

#### 6.3 The V\* Distribution (Critical Volatility Distribution)

If NN independent processes start, after nn iterations
approximately N⋅pnN\cdot p^{n} survive, each with value proportional to
βeffn\beta\_{\text{eff}}^{n}.

Setting v=βeffnv=\beta\_{\text{eff}}^{n} (the value), we have
n=log⁡(v)/log⁡(βeff)n=\log(v)/\log(\beta\_{\text{eff}}), so:

|  |  |  |
| --- | --- | --- |
|  | Number with value>v∝pn=plog⁡(v)/log⁡(βeff)=vlog⁡(p)/log⁡(βeff)\text{Number with value}>v\propto p^{n}=p^{\log(v)/\log(\beta\_{\text{eff}})}=v^{\log(p)/\log(\beta\_{\text{eff}})} |  |

This is a power-law with exponent:

|  |  |  |
| --- | --- | --- |
|  | α=−log⁡(p)log⁡(βeff)\alpha=-\frac{\log(p)}{\log(\beta\_{\text{eff}})} |  |

Since p<1p<1 (survival is not guaranteed) and
βeff>1\beta\_{\text{eff}}>1 (supercritical with conditional growth), we
have α>0\alpha>0: a proper power-law tail.

The V\* Distribution is thus:

|  |  |  |
| --- | --- | --- |
|  | P​(V>v)∝(1−Φ​(kthσ))log⁡vlog⁡(σ⋅ϕ​(kth/σ)1−Φ​(kth/σ))P(V>v)\propto\left(1-\Phi\left(\frac{k\_{\text{th}}}{\sigma}\right)\right)^{\frac{\log v}{\log\left(\sigma\cdot\frac{\phi(k\_{\text{th}}/\sigma)}{1-\Phi(k\_{\text{th}}/\sigma)}\right)}} |  |

where:

* ∙\bullet

  kthk\_{\text{th}} is the threshold multiplier (minimum payoff as
  multiple of wealth)
* ∙\bullet

  σ\sigma is the volatility parameter
* ∙\bullet

  ϕ\phi, Φ\Phi are the standard normal PDF and CDF

This can be written as P​(V>v)∝v−αP(V>v)\propto v^{-\alpha} where
α=−log⁡(p)/log⁡(βeff)\alpha=-\log(p)/\log(\beta\_{\text{eff}}).

#### 6.4 At The Value: Extending to Negative Thresholds

The survival condition in Section 6.2 requires
X≥kth⋅wX\geq k\_{\text{th}}\cdot w, where XX is the underlying return
(before rectification) and kthk\_{\text{th}} is the threshold
multiplier. While the payoff remains max⁡(X,0)\max(X,0), the survival
condition is evaluated on XX itself.

For kth>0k\_{\text{th}}>0, participants require positive returns above a
threshold - a natural constraint for investors seeking real gains. For
kth=0k\_{\text{th}}=0, participants continue if X>0X>0; the option
paid something.

Mathematically, nothing prevents kth<0k\_{\text{th}}<0. This models a
different game: participants accept losses to their wealth to continue
playing. If X=−0.5​wX=-0.5w, the option pays zero, but a participant with
kth=−1k\_{\text{th}}=-1 survives - they absorb the loss from reserves and
enter the next round.

This is no longer option-like behavior. With negative thresholds,
participants have linear exposure to losses up to
|kth|⋅w|k\_{\text{th}}|\cdot w. We call this regime At The Value
(ATV): participants commit to continue through adverse outcomes,
accepting wealth destruction for the chance to remain in the game.

The ATV regime characterizes patient capital:

* ∙\bullet

  Venture funds that continue supporting portfolio companies through
  down rounds
* ∙\bullet

  Strategic investors with long time horizons
* ∙\bullet

  Any participant with reserves who values continuation over immediate
  returns

The phase diagrams that follow extend into this negative
kthk\_{\text{th}} region, revealing how the critical boundary behaves
when participants tolerate losses.

#### 6.5 Phase Space Characterization

The V\* Distribution exists in a two-dimensional parameter space
(σ,kth)(\sigma,k\_{\text{th}}). Figure 1 shows this space with the critical
boundary βeff=1\beta\_{\text{eff}}=1 separating two regimes:

* ∙\bullet

  Subcritical region (upper-left, blue):
  βeff<1\beta\_{\text{eff}}<1. Conditional growth does not compensate for
  attrition. Outcomes are thin-tailed.
* ∙\bullet

  Supercritical region (lower-right, red/orange):
  βeff>1\beta\_{\text{eff}}>1. Conditional growth exceeds attrition.
  Outcomes follow the V\* Distribution with power-law tails.

![V* Phase Transition in (\sigma, k_{\text{th}}) space. Color indicates conditional growth factor \beta_{\text{eff}}. The critical boundary (solid curve) where \beta_{\text{eff}} = 1 separates subcritical (thin-tailed) from supercritical (V* power-law) regimes. Vertical lines mark \sigma_{\text{th}}ˆ{*} = \sqrt{\pi/2} and \sigmaˆ* = \sqrt{2\pi}.](phase_transition.png)

Figure 1: V\* Phase Transition in (σ,kth)(\sigma,k\_{\text{th}}) space. Color
indicates conditional growth factor βeff\beta\_{\text{eff}}. The critical
boundary (solid curve) where βeff=1\beta\_{\text{eff}}=1 separates
subcritical (thin-tailed) from supercritical (V\* power-law) regimes.
Vertical lines mark σth∗=π/2\sigma\_{\text{th}}^{\*}=\sqrt{\pi/2} and
σ∗=2​π\sigma^{\*}=\sqrt{2\pi}.

Figure 2 decomposes the phase space into its constituent quantities. The
left panel shows survival probability
p=1−Φ​(kth/σ)p=1-\Phi(k\_{\text{th}}/\sigma), which decreases as the threshold
becomes more selective (higher kthk\_{\text{th}}) or volatility
decreases (lower σ\sigma). The right panel shows the power-law
exponent α=−log⁡(p)/log⁡(βeff)\alpha=-\log(p)/\log(\beta\_{\text{eff}}) in the
supercritical region, with lower α\alpha indicating heavier tails.

![Phase space components. Left: Survival probability p per iteration. Right: V* power-law exponent \alpha in the supercritical region. Lower \alpha corresponds to heavier tails and more extreme wealth concentration.](phase_components.png)

Figure 2: Phase space components. Left: Survival probability pp per
iteration. Right: V\* power-law exponent α\alpha in the supercritical
region. Lower α\alpha corresponds to heavier tails and more extreme
wealth concentration.

The shape of the critical boundary reflects a fundamental tradeoff. High
volatility generates large values among survivors; high selection
pressure concentrates growth among fewer participants. Both mechanisms
can produce βeff>1\beta\_{\text{eff}}>1:

* ∙\bullet

  At low σ\sigma, strong selection (high kthk\_{\text{th}}) is
  required to achieve supercriticality
* ∙\bullet

  At high σ\sigma, weaker selection (lower kthk\_{\text{th}})
  suffices because volatility alone drives growth

The boundary curves through the parameter space accordingly, extending
into the risk-tolerant region (kth<0k\_{\text{th}}<0) at sufficiently
high volatility.

#### 6.6 Divergence versus Power-Law: The Role of Selection

It is important to distinguish two phenomena that the framework reveals.

Divergence of expected values occurs when
β=σ/2​π>1\beta=\sigma/\sqrt{2\pi}>1, i.e., when σ>2​π\sigma>\sqrt{2\pi}.
In this regime, the expected value at each iteration exceeds the
previous: μn+1=β⋅μn\mu\_{n+1}=\beta\cdot\mu\_{n}. The sum of an infinite
chain diverges. This is the result derived in Section 5 for the
unconditional ATM case.

Power-law distribution requires selection. The V\* Distribution
emerges from the combination of two exponential processes:

* ∙\bullet

  The number of surviving participants decays as pnp^{n}
* ∙\bullet

  The value of each survivor grows as βeffn\beta\_{\text{eff}}^{n}

The power-law exponent α=−log⁡(p)/log⁡(βeff)\alpha=-\log(p)/\log(\beta\_{\text{eff}}) is
well-defined only when both p<1p<1 (selection occurs) and
βeff>1\beta\_{\text{eff}}>1 (conditional growth exceeds unity). Without
selection (p=1p=1), there is no distribution of outcomes - all
participants follow the same trajectory.

These phenomena are related but distinct:

* ∙\bullet

  Divergence concerns the total expected value of the system
* ∙\bullet

  Power-law concerns the shape of the outcome distribution under
  selection

The critical volatility σ∗=2​π\sigma^{\*}=\sqrt{2\pi} marks where expected
values begin to diverge. But power-law behavior can emerge at any
volatility, provided selection is strong enough to achieve
βeff>1\beta\_{\text{eff}}>1. Conversely, even above σ∗\sigma^{\*},
insufficient selection can fail to produce power-law tails if the
survival pool is too large.

#### 6.7 The Critical Intersection Point

The phase diagram reveals where these two thresholds intersect: the
point at which the unconditional divergence threshold
σ=2​π\sigma=\sqrt{2\pi} meets the critical boundary
βeff=1\beta\_{\text{eff}}=1.

At σ=2​π\sigma=\sqrt{2\pi}, how much selection is required to produce
power-law behavior?

Setting βeff=1\beta\_{\text{eff}}=1:

|  |  |  |
| --- | --- | --- |
|  | σ⋅ϕ​(z)1−Φ​(z)=1⇒σ=1−Φ​(z)ϕ​(z)=M​(z)\sigma\cdot\frac{\phi(z)}{1-\Phi(z)}=1\quad\Rightarrow\quad\sigma=\frac{1-\Phi(z)}{\phi(z)}=M(z) |  |

where M​(z)M(z) is the Mills ratio and z=kth/σz=k\_{\text{th}}/\sigma.
Substituting σ=2​π\sigma=\sqrt{2\pi}:

|  |  |  |
| --- | --- | --- |
|  | M​(z∗)=2​πM(z^{\*})=\sqrt{2\pi} |  |

With ϕ​(z)=12​π​e−z2/2\phi(z)=\frac{1}{\sqrt{2\pi}}e^{-z^{2}/2}, this simplifies to:

|  |  |  |
| --- | --- | --- |
|  | 1−Φ​(z∗)=e−z∗2/21-\Phi(z^{\*})=e^{-z^{\*2}/2} |  |

The solution is z∗≈0.7286z^{\*}\approx 0.7286, corresponding to
kth∗=−z∗​2​π≈−1.83k\_{\text{th}}^{\*}=-z^{\*}\sqrt{2\pi}\approx-1.83.

Interpretation. At σ=2​π\sigma=\sqrt{2\pi}, the system
exhibits:

| Selection | Regime | Behavior |
| --- | --- | --- |
| kth>−1.83k\_{\text{th}}>-1.83 | βeff>1\beta\_{\text{eff}}>1 | Power-law (V\*) |
| kth=−1.83k\_{\text{th}}=-1.83 | βeff=1\beta\_{\text{eff}}=1 | Critical |
| kth<−1.83k\_{\text{th}}<-1.83 | βeff<1\beta\_{\text{eff}}<1 | Thin-tailed |

At the unconditional divergence threshold, expected values grow without
bound. Yet this divergence alone does not guarantee power-law outcomes.
If selection pressure is too weak (kth<−1.83k\_{\text{th}}<-1.83), the
survival pool includes too many participants, diluting conditional
growth below unity. The distribution remains thin-tailed despite
divergent expectations.

The constant z∗z^{\*} thus marks the minimum selection pressure required
to convert divergent growth into power-law distribution at
σ=2​π\sigma=\sqrt{2\pi}. Above this point, selection concentrates
growth sufficiently for V\* dynamics to emerge. Below it, dilution
dominates.

#### 6.8 Four Constants of Gaussian Rectification

The framework yields four characteristic constants:

| Constant | Value | Interpretation |
| --- | --- | --- |
| σ∗\sigma^{\*} | 2​π≈2.507\sqrt{2\pi}\approx 2.507 | Divergence threshold: expected values unbounded |
| σth∗\sigma^{\*}\_{\text{th}} | π/2≈1.253\sqrt{\pi/2}\approx 1.253 | Power-law threshold at kth→0+k\_{\text{th}}\to 0^{+} |
| z∗z^{\*} | ≈0.7286\approx 0.7286 | Standardized selection threshold at σ=σ∗\sigma=\sigma^{\*} |
| kth∗k^{\*}\_{\text{th}} | −z∗​2​π≈−1.83-z^{\*}\sqrt{2\pi}\approx-1.83 | Selection threshold in parameter space |

The ratio σ∗/σth∗=2\sigma^{\*}/\sigma^{\*}\_{\text{th}}=2 reflects the doubling of
conditional growth when the survival filter excludes negative outcomes.
The constant z∗z^{\*}, defined by 1−Φ​(z∗)=e−z∗2/21-\Phi(z^{\*})=e^{-z^{\*2}/2}, is
the standardized selection parameter at which power-law behavior first
emerges when volatility reaches the divergence threshold;
kth∗k^{\*}\_{\text{th}} expresses this in the units of the phase diagram.

These constants arise from the geometry of Gaussian rectification - the
interplay of tail probability, local density, and the normalization
factor 2​π\sqrt{2\pi}.

#### 6.9 Implications

The power-law exponent α=−log⁡(p)/log⁡(βeff)\alpha=-\log(p)/\log(\beta\_{\text{eff}})
depends on both survival probability and conditional growth. Near
criticality (βeff≈1\beta\_{\text{eff}}\approx 1), even modest selection
pressure produces heavy tails. Deep in the supercritical regime
(βeff≫1\beta\_{\text{eff}}\gg 1), the distribution becomes increasingly
extreme - a few massive winners among many losers.

The phase diagrams reveal that V\* dynamics are accessible across a wide
range of volatilities, provided selection is appropriately tuned.
Systems with moderate volatility (σ≈100−200%\sigma\approx 100-200\%) can
exhibit power-law behavior if participants impose sufficient selectivity
on continuation. Systems with extreme volatility can exhibit power-law
behavior even with weak selection.

This mechanism requires no exotic assumptions: iterated rectification of
a Gaussian process with selective continuation based on outcomes. The
fat tails emerge from the mathematics itself - specifically, from the
tension between exponential attrition and exponential conditional growth
that selection creates.

### 7. Numerical Simulations for V\*

To validate the theoretical predictions, we simulate a simplified model
which we call ATV (At The Value) where participants repeatedly bet their
entire wealth on an at-the-money option with payoff max⁡(X,0)\max(X,0) where
X∼𝒩​(0,σ​w)X\sim\mathcal{N}(0,\sigma w).

#### 7.1 Simulation Setup

We simulate N=10,000,000N=10{,}000{,}000 participants over T=15T=15 periods,
each starting with wealth w0=$​20,000w\_{0}=\mathdollar 20{,}000. At each period,
participants in the high-risk game receive payoff max⁡(X,0)\max(X,0) where
X∼𝒩​(0,σ​w)X\sim\mathcal{N}(0,\sigma w). Participants drop out and switch to
a safe alternative (10% volatility with in the money structure) if
their payoff falls below 2.5×2.5\times their current wealth -
representing the requirement that returns must justify continued
risk-taking in situations where bankruptcy risk is ~50%
per turn.

The model tests volatilities ranging from σ=0.1\sigma=0.1 (10%) to
σ=4.0\sigma=4.0 (400%), spanning the critical threshold at
σ∗=2​π≈2.507\sigma^{\*}=\sqrt{2\pi}\approx 2.507 (251%).

The simulation algorithm:

def simulate\_atv\_model(n=10\_000\_000, t=15, w0=20\_000, sigma=2.5, threshold\_k=2.5): w = np.full(n, w0, dtype=float) in\_high\_risk = np.ones(n, dtype=bool) sigma\_low = 0.1 for year in range(t): x\_high = np.random.randn(n) \* sigma \* w payoff\_high = np.maximum(x\_high, 0) payoff\_low = w \* (1 + np.random.randn(n) \* sigma\_low) payoff\_low = np.maximum(payoff\_low, 0) threshold = threshold\_k \* w dropout = in\_high\_risk & (payoff\_high < threshold) w = np.where(in\_high\_risk, payoff\_high, payoff\_low) in\_high\_risk = in\_high\_risk & ~dropout return w

#### 7.2 Results

Figure 3 shows the rank-wealth distribution from simulation across all
volatility regimes on a log-log scale, with the V\* theoretical
prediction overlaid (purple dashed line). The transition from curved
(log-normal) to linear (power-law) behavior is clearly visible as
volatility crosses the critical threshold. Figure 4 compares the wealth
distributions in subcritical and supercritical regimes, with the V\*
theoretical power-law slope shown for comparison. Table 1 presents
detailed statistics for each volatility level.

![Simulation vs V* Theory: Rank-wealth distribution across volatility regimes. Colored lines show simulation results from \sigma=0.1 (blue) to \sigma=4.0 (red). The purple dashed line shows the V* theoretical prediction (\alpha = -\log(p)/\log(\beta_{\text{eff}})) for \sigma=3.0. Above criticality (\sigmaˆ* \approx 2.507), simulated distributions converge to the theoretical power-law slope.](atv_transition.png)

Figure 3: Simulation vs V\* Theory: Rank-wealth distribution across
volatility regimes. Colored lines show simulation results from
σ\sigma=0.1 (blue) to σ\sigma=4.0 (red). The purple dashed line
shows the V\* theoretical prediction
(α=−log⁡(p)/log⁡(βeff)\alpha=-\log(p)/\log(\beta\_{\text{eff}})) for σ\sigma=3.0.
Above criticality (σ∗≈2.507\sigma^{\*}\approx 2.507), simulated distributions
converge to the theoretical power-law slope.



![Simulation vs V* Theory: Subcritical (\sigma=2.0, blue) vs supercritical (\sigma=3.0, red) wealth distributions. Left: Probability density on log-log scale. Right: Rank-wealth plot with V* theoretical prediction (purple dashed) showing close agreement with supercritical simulation.](regime_comparison.png)

Figure 4: Simulation vs V\* Theory: Subcritical (σ\sigma=2.0, blue) vs
supercritical (σ\sigma=3.0, red) wealth distributions. Left:
Probability density on log-log scale. Right: Rank-wealth plot with V\*
theoretical prediction (purple dashed) showing close agreement with
supercritical simulation.



| σ\sigma | β\beta | Bankrupt | Heavy Loss | $2k-20k | >$20k | >$50k | >$100k | >$1M | >$10M | >$100M | >$1B | Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.10 | 0.04 | 5,229,613 | 3,313,805 | 1,456,562 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | ∞\infty |
| 0.50 | 0.20 | 5,045,879 | 862,558 | 3,759,334 | 332,229 | 4,878 | 20 | 0 | 0 | 0 | 0 | ∞\infty |
| 1.00 | 0.40 | 5,054,141 | 436,565 | 3,093,118 | 1,416,176 | 134,222 | 4,702 | 0 | 0 | 0 | 0 | ∞\infty |
| 1.50 | 0.60 | 5,267,191 | 295,832 | 2,421,761 | 2,015,216 | 360,722 | 53,688 | 134 | 0 | 0 | 0 | ∞\infty |
| 2.00 | 0.80 | 5,603,627 | 225,395 | 1,960,344 | 2,210,634 | 562,968 | 158,609 | 2,672 | 34 | 1 | 0 | 78.6 |
| 2.51 | 1.00 | 5,957,643 | 181,984 | 1,632,383 | 2,227,990 | 707,131 | 275,089 | 12,076 | 553 | 17 | 1 | 21.8 |
| 3.00 | 1.20 | 6,277,439 | 153,424 | 1,398,570 | 2,170,567 | 794,856 | 371,871 | 28,760 | 2,234 | 175 | 8 | 12.9 |
| 3.50 | 1.40 | 6,564,826 | 132,271 | 1,217,426 | 2,085,477 | 845,480 | 444,779 | 50,506 | 5,647 | 674 | 54 | 8.9 |
| 4.00 | 1.60 | 6,818,493 | 116,154 | 1,075,393 | 1,989,960 | 870,073 | 497,072 | 73,912 | 10,648 | 1,602 | 224 | 6.9 |

Table 1: Simulation results showing wealth distribution across
volatility regimes. “Bankrupt” = wealth < $100, “Heavy
Loss” = $100-$2,000, “Ratio” = count($1M+) / count($10M+).

#### 7.3 Key Observations

The Low-Volatility Trap. At σ=0.1\sigma=0.1, where
β=0.04\beta=0.04, an astonishing 85% of participants are either
bankrupt or suffer heavy losses. This occurs because the expected payoff
per period is only 0.04​w0.04w - a 96% loss rate per iteration. Low
volatility provides insufficient upside to compensate for the inherent
bankruptcy risk of the ATV structure. Zero millionaires emerge from 10
million participants.

Critical Transition. At σ=2.507≈σ∗\sigma=2.507\approx\sigma^{\*}, we
observe β=1.00\beta=1.00 - the break-even point where expected payoff
equals current wealth. The ratio of millionaires to decamillionaires
drops sharply to 21.8, indicating the emergence of heavy tails. The
first billionaire appears in the simulation.

Supercritical Power-Law. For σ>σ∗\sigma>\sigma^{\*}, the ratio
stabilizes (21.8 → 12.9 → 8.9 → 6.9), the hallmark of power-law behavior
where the proportion between consecutive magnitude classes becomes
constant. At σ=4.0\sigma=4.0, despite 70% bankruptcy or heavy loss,
224 billionaires emerge - a clear demonstration of the
few-massive-winners, many-losers distribution characteristic of power
laws.

### 8. Interpretation and Market Implications

#### 8.1 Three Regimes

Unconditional ATM Case. When all participants continue
regardless of outcomes, the parameter β=σ/2​π\beta=\sigma/\sqrt{2\pi}
defines three regimes:

| Regime | Condition | Behavior |
| --- | --- | --- |
| Subcritical | σ<2​π≈250.66%\sigma<\sqrt{2\pi}\approx 250.66\% | Convergent: Each payoff expected value is lower than previous and the total payoff is bounded. Produces thin-tailed distribution of outcomes. |
| Critical | σ≈2​π\sigma\approx\sqrt{2\pi} | Self-similar: Each layer reproduces the previous. |
| Supercritical | σ>2​π\sigma>\sqrt{2\pi} | Divergent: Each payoff expected value is higher than previous and the total payoff goes to infinity. |

V\* Case with Survival Threshold. When participants require
minimum returns kthk\_{\text{th}} to continue, the conditional growth
factor
βeff=σ⋅ϕ​(kth/σ)/p\beta\_{\text{eff}}=\sigma\cdot\phi(k\_{\text{th}}/\sigma)/p
determines the regime:

| Regime | Condition | Behavior |
| --- | --- | --- |
| Subcritical | βeff<1\beta\_{\text{eff}}<1 | Convergent: Survivors do not grow fast enough to compensate for attrition. Produces thin-tailed distribution. |
| Critical | βeff≈1\beta\_{\text{eff}}\approx 1 | Self-similar: Conditional growth exactly balances survival probability. V\* behavior emerges. |
| Supercritical | βeff>1\beta\_{\text{eff}}>1 | Divergent: Survivors grow faster than the population decays. Produces V\* Distribution with exponent α=−log⁡(p)/log⁡(βeff)\alpha=-\log(p)/\log(\beta\_{\text{eff}}). |

The V\* framework generalizes the ATM result: with any positive survival
threshold, the critical volatility drops to
σth∗=π/2≈125.3%\sigma\_{\text{th}}^{\*}=\sqrt{\pi/2}\approx 125.3\%, and decreases
further as kthk\_{\text{th}} increases. Power-law dynamics can thus
emerge at volatilities far below σ∗\sigma^{\*}.

#### 8.2 Volatility of Options on Options

An important real-world consideration: the volatility of an option’s
value is generally *higher* than the volatility of the underlying.
This is due to the convexity (gamma) of the option payoff. For a
compound option (option on an option), this effect compounds.

If we denote the volatility of the nn-th layer as σn\sigma\_{n},
empirically we observe:

|  |  |  |
| --- | --- | --- |
|  | σn>σn−1\sigma\_{n}>\sigma\_{n-1} |  |

This means that in practice, iterated option structures tend to
*accelerate* toward the supercritical regime. The
constant-percentage-volatility assumption in our geometric regime is
thus conservative; real compound structures may diverge faster than our
model predicts.

#### 8.3 Time to Criticality

In Black-Scholes, the relevant volatility parameter is
σ​T\sigma\sqrt{T}, where σ\sigma is the annualized volatility and
TT is time to expiration in years. For the unconditional case, the
critical threshold σ​T=2​π\sigma\sqrt{T}=\sqrt{2\pi} gives:

|  |  |  |
| --- | --- | --- |
|  | T∗=2​πσ2T^{\*}=\frac{2\pi}{\sigma^{2}} |  |

For the V\* case with survival threshold, the critical threshold drops to
σ​T=π/2\sigma\sqrt{T}=\sqrt{\pi/2}, giving:

|  |  |  |
| --- | --- | --- |
|  | Tth∗=π/2σ2T\_{\text{th}}^{\*}=\frac{\pi/2}{\sigma^{2}} |  |

| Annualized Vol σ\sigma | T∗T^{\*} (unconditional) | Tth∗T\_{\text{th}}^{\*} (V\* with threshold) |
| --- | --- | --- |
| 10% | 628 years | 157 years |
| 20% | 157 years | 39 years |
| 50% | 25 years | 6.3 years |
| 100% | 6.3 years | 1.6 years |
| 150% | 2.8 years | 8.4 months |
| 200% | 1.6 years | 4.7 months |
| 250% | 1.0 year | 3.0 months |
| 300% | 8.4 months | 2.1 months |
| 400% | 4.7 months | 1.2 months |
| 500% | 3.0 months | 3.3 weeks |
| 800% | 1.2 months | 1.3 weeks |

For typical equity volatilities (15-30%), the unconditional critical
threshold is centuries away. But with survival thresholds - which are
ubiquitous in real markets - criticality arrives four times faster. For
meme stocks and distressed names exhibiting 400-800% implied
volatility, V\* criticality occurs within weeks.

This means a 3-month ATM option on a 500% vol underlying is already at
the critical regime - its expected payoff structure exhibits the
self-similar properties described in Section 3.3. A 6-month option on
the same underlying is supercritical.

An interesting observation: Early-stage startups exhibit annual
valuation volatility in the 100-250% range, with funding rounds
occurring every 12-24 months. Under the unconditional model, the
critical horizon is 1-6 years - placing startups below criticality for
typical funding cycles. However, with survival thresholds
(σth∗≈125%\sigma\_{\text{th}}^{\*}\approx 125\%), the critical horizon drops
to 3-19 months - squarely within typical funding cycles.

Venture capitalists impose implicit survival thresholds: startups must
demonstrate sufficient progress to secure the next funding round. This
selective continuation - where only companies exceeding some return
threshold kthk\_{\text{th}} survive to the next stage - creates
conditional growth βeff>1\beta\_{\text{eff}}>1 even when unconditional
β<1\beta<1. The famously power-law distributed VC returns may thus be
a natural consequence of the V\* mechanism: iterated optionality with
selective survival, where each funding stage represents both a survival
filter and a growth multiplier for those who pass.

#### 8.4 Connection to Real Instruments

Several existing instruments exhibit related dynamics:

* ∙\bullet

  Compound options (options on options): Used in corporate
  finance for staged investments and in FX markets.
* ∙\bullet

  Volatility derivatives: VIX options are options on a
  volatility index, which is itself derived from option prices - a form
  of second-order optionality.
* ∙\bullet

  Leveraged ETFs: Daily rebalancing creates path-dependent
  compounding effects related to iterated expectations.
* ∙\bullet

  Convertible bonds with call provisions: Multiple embedded
  options create layered optionality.

Instruments involving averaging over multiple options (such as VIX
derivatives) present an interesting direction for potential extension of
the framework. The aggregation may produce lower volatility compared to
individual instruments, which warrants additional modelling not covered
in this paper.

### 9. Conclusion

We have analyzed the behavior of iterated rectified Gaussian
expectations, illustrated by the theoretical construct of an infinite
chain of options-on-options. Our main findings:

1. 1.

   A critical volatility threshold exists at
   σ∗=2​π≈250.66%\sigma^{\*}=\sqrt{2\pi}\approx 250.66\%. Below this threshold, the
   cumulative value of an infinite option chain converges; above it, the
   chain diverges. This is the upper bound of stability under the
   idealized assumption of the system being maximally stable.
2. 2.

   The supercritical regime implies that optionality can exceed
   underlying value. This is practically relevant during market stress
   events when implied volatilities spike above 250%.
3. 3.

   Real compound structures tend toward supercriticality because option
   volatility exceeds underlying volatility due to convexity effects.
   Real-world volatility amplification, leverage, or imperfect pricing
   would result in a lower critical bound.
4. 4.

   With selective survival, the critical threshold drops discontinuously
   to σth∗=π/2≈125.3%\sigma\_{\text{th}}^{\*}=\sqrt{\pi/2}\approx 125.3\%. We term
   the resulting power-law the V\* Distribution, characterized by survival
   probability p=1−Φ​(kth/σ)p=1-\Phi(k\_{\text{th}}/\sigma) and conditional
   expected growth
   βeff=σ⋅ϕ​(kth/σ)/p\beta\_{\text{eff}}=\sigma\cdot\phi(k\_{\text{th}}/\sigma)/p.
   The power-law exponent α=−log⁡(p)/log⁡(βeff)\alpha=-\log(p)/\log(\beta\_{\text{eff}})
   admits closed-form expression.

The thresholds σ∗=2​π\sigma^{\*}=\sqrt{2\pi} and
σth∗=π/2\sigma\_{\text{th}}^{\*}=\sqrt{\pi/2} emerge purely from the
geometry of Gaussian rectification - non-obvious boundaries that
separate fundamentally different economic regimes.

The V\* Distribution provides a mechanism for power-law emergence that
requires no exotic assumptions. In repeated games with rectified
Gaussian payoffs, the number of surviving participants decays
exponentially as pnp^{n}, while the wealth of each survivor grows
exponentially as βeffn\beta\_{\text{eff}}^{n}. The conditional nature of
βeff\beta\_{\text{eff}} is essential: it measures the expected growth
*given survival*, not the unconditional expected payoff. This
interplay between exponential attrition and exponential conditional
growth produces fat tails with predictable exponents.

A final observation: While literal towers of
derivatives-on-derivatives are rare, our mathematical framework requires
a much weaker assumption - merely that expected returns propagate
through some iterative structure. Many common financial arrangements
satisfy this condition without being explicit derivative chains: loans
and credit facilities (where the borrower’s ability to repay depends on
asset values), margin accounts and leveraged positions (where
maintenance requirements create recursive dependencies), and tightly
coupled instrument prices (where one instrument’s value serves as
collateral or reference for another). The interaction of these
structures during stress events - when correlations spike and
volatilities exceed normal ranges - may exhibit dynamics similar to
those analyzed here, even without any formal options being written.

Furthermore, the framework does not require that all layers of the
derivative structure exist simultaneously. Consecutive dependent
instruments unfolding over time - where each stage’s payout becomes the
underlying for the next - satisfy the same mathematical recursion. As we
have shown in simulation, the V\* Distribution emerges reliably from this
process, with power-law exponents matching theoretical predictions. The
critical threshold we identify may thus be relevant not just for exotic
derivatives, but for understanding systemic behavior in leveraged,
interconnected financial systems evolving through time.

One might wonder if this model could help in predicting instability in
less exotic cases. Could black swans, fat tails, unexpected VC returns,
and volatility smiles have been predicted by feeding the random walk
back into itself and checking if it converges?

As a last note, we would like to emphasize that whether anyone should
actually construct an infinite derivative tower remains, we maintain,
inadvisable. But at least we now know where it would break.

### Appendix: Notation Summary

| Symbol | Definition |
| --- | --- |
| Φ​(z)\Phi(z) | Standard normal CDF |
| ϕ​(z)\phi(z) | Standard normal PDF |
| g​(z)g(z) | z​∫−∞ze−t2/2​𝑑t+e−z2/2z\int\_{-\infty}^{z}e^{-t^{2}/2}dt+e^{-z^{2}/2}, unnormalized expected rectified value |
| σ\sigma | Volatility parameter |
| β\beta | σ/2​π\sigma/\sqrt{2\pi}, unconditional geometric ratio |
| σ∗\sigma^{\*} | 2​π≈2.5066≈250.66%\sqrt{2\pi}\approx 2.5066\approx 250.66\%, critical volatility (unconditional) |
| σth∗\sigma\_{\text{th}}^{\*} | π/2≈1.2533≈125.3%\sqrt{\pi/2}\approx 1.2533\approx 125.3\%, critical volatility (with any survival threshold) |
| kthk\_{\text{th}} | Threshold multiplier (minimum payoff as multiple of wealth) |
| pp | Survival probability per stage, 1−Φ​(kth/σ)1-\Phi(k\_{\text{th}}/\sigma) |
| βeff\beta\_{\text{eff}} | Conditional expected growth factor, σ⋅ϕ​(kth/σ)/p\sigma\cdot\phi(k\_{\text{th}}/\sigma)/p |
| α\alpha | Power-law exponent, −log⁡(p)/log⁡(βeff)-\log(p)/\log(\beta\_{\text{eff}}) |
| V∗V^{\*} | V\* Distribution: P​(V>v)∝v−αP(V>v)\propto v^{-\alpha} |

### Code Availability

Simulation code and supplementary materials are available at:
[github.com/sci2sci-opensource/research](https://github.com/sci2sci-opensource/research/tree/master/critical-volatility-and-v*)

### References

Black, F., & Scholes, M. (1973). The pricing of options and corporate
liabilities. *Journal of Political Economy*, 81(3), 637-654.

Geske, R. (1979). The valuation of compound options. *Journal of
Financial Economics*, 7(1), 63-81.