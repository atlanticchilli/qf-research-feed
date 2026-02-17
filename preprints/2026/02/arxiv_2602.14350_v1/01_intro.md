---
authors:
- Noura El Hassan
- Bacel Maddah
- Nassim N. Taleb
doc_id: arxiv:2602.14350v1
family_id: arxiv:2602.14350
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Hidden Risks and Optionalities in American Options
url_abs: http://arxiv.org/abs/2602.14350v1
url_html: https://arxiv.org/html/2602.14350v1
venue: arXiv q-fin
version: 1
year: 2026
---


Noura El Hassan1,
Bacel Maddah2,
Nassim Nicholas Taleb23

###### Abstract

We develop a practical framework for identifying and quantifying the hidden layers of risks and optionality embedded in American options by introducing stochasticity into one or more of their underlying determinants. The heuristic approach remedies the problems of conventional pricing systems, which treat some key inputs deterministically, hence systematically underestimate the flexibility and convexity inherent in early-exercise features.

## I Unaccounted Optionality

### I-A A note on model nonlinearity as fragility

Fragility to model error has been mapped in terms of convexity [[1](https://arxiv.org/html/2602.14350v1#bib.bib1)], and its heuristic testing presented below applied among others by the IMF to gauge portfolio risks of banks, see [[2](https://arxiv.org/html/2602.14350v1#bib.bib2)].

The logic is as follows. Having the right model, but being subjected to parameter uncertainty will invariably lead to an expected increase in model error in the presence of convexity and nonlinearities, particularly when the second order effect is not negligible. Assume f(.)f(.) an estimated function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x∣a),f(x\mid a), |  | (1) |

where aa is fixed, assumed to be the average or expected parameter, taking uu as the distribution of aa over its domain 𝒜\mathcal{A}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | a¯=∫𝒜a​u​(a)​𝑑a.\bar{a}\;=\;\int\_{\mathcal{A}}a\,u(a)\,da. |  | (6) |

The mere fact that aa is uncertain (since it is estimated) might lead to a bias if we perturbate from the outside (of the integral), i.e. stochasticize the parameter deemed fixed. Accordingly, fragility to model error πA\pi\_{A} is easily measured as the difference between (a) ff integrated across values of potential aa and (b) ff estimated for a single value of aa deemed to be its average. The convexity bias π\pi becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | πA=∫𝒳∫𝒜f​(x∣a)​u​(a)​𝑑a​𝑑x−∫𝒳f(x|∫𝒜au(a)da)dx.\pi\_{A}\;=\;\int\_{\mathcal{X}}\int\_{\mathcal{A}}f(x\mid a)\,u(a)\,da\,dx\;-\\ \int\_{\mathcal{X}}f\!\left(x\,\middle|\,\int\_{\mathcal{A}}a\,u(a)\,da\right)\!dx. |  | (2) |

This can be approximated by an interpolated estimate obtained with two values of aa separated from a mid-point by Δ​a\Delta a, the mean deviation of aa, and estimating the convexity bias πΔ​a\pi\_{\Delta a}

|  |  |  |  |
| --- | --- | --- | --- |
|  | πΔ​a≈∫−∞K12(f(x∣a¯+Δa)+f(x∣a¯−Δa))dx−∫−∞Kf(x∣a¯)dx.\pi\_{\Delta a}\;\approx\;\int\_{-\infty}^{K}\frac{1}{2}\Big(f(x\mid\bar{a}+\Delta a)\\ +f(x\mid\bar{a}-\Delta a)\Big)\,dx\;-\;\int\_{-\infty}^{K}f(x\mid\bar{a})\,dx. |  | (3) |

Furthermore, particularly in the case of options, even if a pricing approximation is used, the result may not illuminate us on option valuation but will give us a degree of model risk. Under the principle in [[1](https://arxiv.org/html/2602.14350v1#bib.bib1)], a bad ruler might not give us the precise height of a growing child, but will inform us whether the child is growing. As we are looking for fragilities, this allows us some approximations that work well with otherwise computationally onerous American options.

### I-B Application to American Options

American options differ from their European counterparts in allowing early exercise. This single feature introduces a set of nonlinearities and latent exposures that remain largely invisible to conventional risk systems.

A standard option O(.)O(.) is a function

|  |  |  |  |
| --- | --- | --- | --- |
|  | O​(S,K,σ,T,r1,r2),O(S,K,\sigma,T,r\_{1},r\_{2}), |  | (4) |

where SS is the underlying security price at time 0, KK the strike price, σ\sigma the volatility, TT the time to nominal expiration, r1r\_{1} the funding rate, and r2r\_{2} the “carry” of the underlying (which could be the discrete dividend or continuous foreign rate).

Under conventional pricing models (starting with [[3](https://arxiv.org/html/2602.14350v1#bib.bib3)] ), only SS is stochastic. In further refinements and adaptations, σ\sigma is treated as stochastic, with a rich literature [[4](https://arxiv.org/html/2602.14350v1#bib.bib4), [5](https://arxiv.org/html/2602.14350v1#bib.bib5), [6](https://arxiv.org/html/2602.14350v1#bib.bib6)], see [[8](https://arxiv.org/html/2602.14350v1#bib.bib8)] for a review. We note that stochasticity of an additional variable entails additional parameters, particularly the centering and scale of the stochastic variable.

European Options do not heed the stochasticity of r2r\_{2}, or, rather the differential between r1−r2r\_{1}-r\_{2} as it is entirely inherited in the volatility of the forward F=S​er1−r2​tF=Se^{r\_{1}-r\_{2}}t, where tt is the time period, which can be captured by expert operators who typically use the volatility of the latter (at the nominal maturity) instead of that of the spot. However American options are specially –and seriously– affected by both r1r\_{1} and r2r\_{2}. In what follows, after discussing some empirical episodes, we will focus on injecting the dynamics of r1r\_{1} and r2r\_{2}.

\*\*

The remaining part of this article is organized as follows. We present the real world problems as encountered by option operators in section [II](https://arxiv.org/html/2602.14350v1#S2 "II Illustrative Practitioner Episodes ‣ Hidden Risks and Optionalities in American Options"), discuss their typology in section [III](https://arxiv.org/html/2602.14350v1#S3 "III Differential Valuation Cases ‣ Hidden Risks and Optionalities in American Options"), briefly link model error to fragility in section [I-A](https://arxiv.org/html/2602.14350v1#S1.SS1 "I-A A note on model nonlinearity as fragility ‣ I Unaccounted Optionality ‣ Hidden Risks and Optionalities in American Options"), present the master equation and the various possible dynamics and probability distributions for pricing in section in section [IV](https://arxiv.org/html/2602.14350v1#S4 "IV Pricing Implementations ‣ Hidden Risks and Optionalities in American Options"). We perform a broad set of calculations under different models showing the robustness of our findings in the final sections.

## II Illustrative Practitioner Episodes

Practitioner Episode 1: The Currency Interest Rate Flip:

Not only the sign of (r1−r2)(r\_{1}-r\_{2}) can vary, but it can flip from positive to negative –and the tradition for option pricing and hedging systems is to use a flag to price either the put or the call as if they were European since the early exercise feature can be ignored.

During the 1980s, German interest rates were generally lower than those in the United States. In such a configuration–where the foreign rate is below the domestic rate–standard pricing systems value the American put on a currency pair higher than its European counterpart, while assigning identical values to the corresponding calls.

When interest rates later converged, and subsequently reversed following the post-reunification rise in German yields, many believed they were executing an arbitrage-free trade by selling the American option and buying the European one. Initially, their mark-to-model valuations appeared profitable, as the systems treated both options as equivalent. However, when interest rate differentials inverted, the mark-to-market values diverged dramatically. The models, which had ignored the early-exercise possibility of such options, failed to capture the exposure. Several trading desks incurred significant losses before realizing that the American call carried embedded optionality on the path of the rate differential.

Similar opportunities reappeared during subsequent currency crises and devaluations, whenever interest rates became unstable. The pattern was recurrent: volatility in the rate differential would amplify the hidden optionality of the American instrument, while the European remained constrained by its terminal payoff structure.

Option operators were unaware of the risks since both the academic literature and option software designers (an overlapping community) did not count for it –even stochastic volatility wasn’t even implemented then prior to the late 1990s [[9](https://arxiv.org/html/2602.14350v1#bib.bib9)].

Practitioner Episode 2: The Stock Squeeze:
In the early 2000s, the corresponding author was confronted a problematic position: his desk was long listed American calls on an Argentinian stock and short the corresponding delta amount (hedge ratio) in the underlying shares. The stock, an obscure ADR, was delisted unexpectedly, forcing an urgent buy-in. No liquidity was available, and attempts to borrow the stock–ironically through the firm Bear Stearns at the time–proved futile.

The resolution was conceptually simple yet operationally decisive: exercise the calls up to the amount of the short (by the hedge ratio). By doing so, the trader obtained the shares and neutralized the squeeze. Had the options been European, early exercise would have been impossible, and the losses potentially catastrophic. The episode demonstrated that the American call possesses not only market optionality but also “model error optionality”–the ability to adapt to unexpected discontinuities in the underlying or in the market microstructure. We note that such optionality can be modeled with a jump in the financing rate.

Practitioner Episode 3: The Equity Index Squeeze:
A related mispricing witnessed by the corresponding author occurred in the period covering 1998-1999 (in the wake of the failure of the hedge fund Long Term Management). It concerned long-dated, over-the-counter European call options on an equity index. These instruments traded at prices corresponding to volatility levels far below any plausible historical measure. Traders were long the calls and short the index futures, continuously rebalancing as the market rose slowly but substantially. The problem is that the rebalancing led to an increase of short futures. They lost on the futures (which for these contracts were to be settled daily with an outflow of cash), but were unable to monetize gains on the options, which remained heavily discounted.

At one point, the options were offered below their intrinsic value relative to the forward (at a standard funding rate)–an apparent market inefficiency. Yet, capital constraints prevented arbitrage, as carrying the long position required margin and funding, not available to risky positions during that period. Earlier, during the crash of 1987, similar distortions were observed when the cash-futures discount widened to nearly 10% –an arbitrage that failed to attract operators owing to the stress on the financial system.

With European options, such dislocations can become terminal to a trading desk, that is, they threaten extinction. By contrast, the American contract provides a lower bound to adverse mark-to-market movements (and an option on funding rates): its early-exercise right effectively caps the degree of mispricing to which the holder can be exposed. This feature embodies an additional, often unrecognized, layer of convexity.

## III Differential Valuation Cases

Case 1: Convexity to Changes in the Carry:
Consider an underlying forward and spot both initially at 100, and a one-year at-the-money European and American call. Under conventional pricing systems, both instruments will be marked identically.

If the underlying rallies to 140, both options converge to parity, each worth $40. However, assume that interest rates rise to 10%. The European option’s value becomes the discounted intrinsic value–approximately $36.36–while the American option, which can be exercised immediately, retains a value of $40.

Thus, a change in the carry–here, the discounting environment–benefits the American option disproportionately. The European price is anchored to a fixed maturity, while the American’s exercise flexibility preserves nominal value under higher rates.

Case 1B: Asymmetric Rate Shifts:
Assume now that only the domestic rate increases to 10%, with the spot unchanged at 140. The forward declines to roughly 126. The European call, valued off this forward, drops to approximately the present value of 26, or $23.64. The American call, which may be exercised immediately, remains worth $26.

In both scenarios, the American option systematically outperforms the European because it benefits from convexity to the interest rate differential. Any model that prices the two identically under changing carry assumptions is misspecified.

From this, a general principle follows: if option A is worth at least as much as option B in all scenarios, and strictly more in some, it is suboptimal to sell option A and buy option B at equal prices. Yet this qualitative inequality still leaves open the quantitative question–how much more should one pay for the flexibility?

Case 2: Sensitivity to Changes in the Foreign or Dividend Rate:
Let S=F=140S=F=140 with both domestic and foreign rates initially at zero. Again, the European and American options start at the same model price. Suppose the foreign rate rises sharply to 20%. The forward now appreciates to roughly S​e(rd−rf)​T≈1.16​SSe^{(r\_{d}-r\_{f})T}\approx 1.16S.

The European call, lacking early exercise, is now worth only about $16 (its discounted intrinsic value). The American call, however, retains the full intrinsic value of $40. The rationale is straightforward: the American option dynamically selects the more favorable exercise basis–cash or forward–depending on which maximizes its immediate payoff. It "chooses" the superior underlying, adapting endogenously to the change in rate environment.

Case 3: Sensitivity to the Yield Curve Slope:
Consider now a non-flat term structure, such as those frequently observed around year-end or policy rollovers. When the yield curve contains inflection points, the conventional valuation using only the terminal forward rate FTF\_{T} becomes unreliable.

Intermediate fluctuations in the carry can significantly affect the American option’s value, as the optimal exercise point may occur precisely at one of those kinks. A pricing or risk-management system that collapses the full term structure into a single terminal forward will therefore misprice the American option–often marking it equal to the European, when in fact it should be higher.

The intuition is clear: an American option allows the holder to "lock in" the forward at any intermediate date, capturing transient peaks in synthetic carry. The European option, constrained to final maturity, lacks such adaptability.

## IV Pricing Implementations

The preceding examples illustrate that the value differential between American and European options grows with the volatility of interest rates and the curvature of the term structure. The greater the uncertainty in the path of the carry, the larger the unpriced optionality embedded in the American contract.

First, using the earlier notation in eq. [4](https://arxiv.org/html/2602.14350v1#S1.E4 "In I-B Application to American Options ‣ I Unaccounted Optionality ‣ Hidden Risks and Optionalities in American Options") we write down the price of an American option at time 0 and underlying price SS

|  |  |  |  |
| --- | --- | --- | --- |
|  | OA(S,K,σ,t,r1,r2),=supτ∈𝒯0,T𝔼ℚ[e−r1​τg(Sτ)]O\_{A}(S,K,\sigma,t,r\_{1},r\_{2}),=\sup\_{\tau\in\mathcal{T}\_{0,T}}\mathbb{E}^{\mathbb{Q}}\Bigl[e^{-r\_{1}\tau}\,g(S\_{\tau})\Bigm] |  | (5) |

where g​(S)g(S) is the payoff function (intrinsic value) at exercise:
g​(S)=max⁡(Φ​(S−K),0)g(S)=\max\bigl(\Phi(S-K),0\bigr)
where Φ=+1\Phi=+1 for a call option and Φ=−1\Phi=-1 for a put option,
𝒯t,T\mathcal{T}\_{t,T} is the set of all stopping times τ\tau such that t≤τ≤Tt\leq\tau\leq T almost surely,
𝔼ℚ​[⋅]\mathbb{E}^{\mathbb{Q}}[\,\cdot] is the conditional expectation under the risk-neutral probability measure ℚ\mathbb{Q}, given the information available at time tt and, finally, ℚ\mathbb{Q} is the risk-neutral (equivalent martingale) measure.
Now eq. [5](https://arxiv.org/html/2602.14350v1#S4.E5 "In IV Pricing Implementations ‣ Hidden Risks and Optionalities in American Options"), the "master" equation does not specify methodologies.

Owing to the path dependence of American options, their pricing has always been fraught with difficulties, even in the very standard situation when only SS is stochastic.

Note that conventional Monte Carlo methods are ill-suited to capturing this additional stochasticity, as the stopping time is path-dependent and endogenous. More sophisticated numerical approaches–such as least-squares Monte Carlo or hybrid analytical methods–are required to quantify the magnitude of this latent premium. In practice, however, even ordinal (directional) comparisons can reveal substantial model risk when early-exercise rights are ignored.

Some complexity arises from the uncertainty of the hedge horizon for the underlying. The effective forward hedge of an American option is unknown, since the exercise time is stochastic. The situation resembles that of a barrier option with an uncertain trigger: termination depends on multiple stochastic variables, including volatility, the base rate, and the rate differential.

A hidden risk arises from the following. Intuitively, the "smart" American option positions itself, in principle, at the point on the forward curve that maximizes its discounted value. A risk-management system that allocates all forward delta exposure to the terminal maturity–treating the forward as if exercise can occur only at TT–commits a structural error. Such systems underestimate the embedded additional optionality and misstate both value and hedge sensitivities.

In summary, American options possess multiple layers of unaccounted convexity beyond their explicit early-exercise feature. These include sensitivity to stochastic rates, curvature in the term structure, model error, and liquidity constraints. Properly accounting for these requires stochasticizing the underlying rate processes and evaluating expected value under the distribution of exercise times–a problem intimately linked to the concept of the fugit.

{remark}

The difference between various methods should be minor compared to parameter uncertainty. We are looking for the first order effect of the stochasticity in rates, largely to gauge the magnitude of the hidden risk ignored so far.

Risk management is about scenario analyses across a parameter set, not precise pricing; our approach allows parametrization.

## V Integrating an American Option across Stochastic Rates

In short, in what follows, we try the following simplified heuristics to grasp the hidden exposure. All are based on a separation of OAO\_{A} using a separation of the sort used in eq. [2](https://arxiv.org/html/2602.14350v1#S1.E2 "In I-A A note on model nonlinearity as fragility ‣ I Unaccounted Optionality ‣ Hidden Risks and Optionalities in American Options"), that is integrating OAO\_{A} across r1r\_{1} or r2r\_{2}.


•

Method 1- One single integration OAO\_{A} across stochastic rates at a distribution of optimal stopping times, the " fugit based heuristic".
•

Method 2- Multiple integrations of OAO\_{A} across stochastic rates at a given optimal stopping time τ\tau, the "fugit".

Let us use the shortcut OA​(r1,r2,t)O\_{A}(r\_{1},r\_{2},t) to denote the price of an American option computed under a deterministic carry and foreign or dividend rates r2r\_{2} using any standard numerical method (binomial, lattice, or PDE). We wish to approximate the price of the same option when either r1r\_{1} or r2r\_{2} is stochastic, by integrating over the distribution of the stochastic rate(s) at the effective exercise time.
We note that perturbations for r1r\_{1} can cover squeezes of financing (in section [III](https://arxiv.org/html/2602.14350v1#S3 "III Differential Valuation Cases ‣ Hidden Risks and Optionalities in American Options")), while r2r\_{2} can cover changes in the security yield, which includes dividends.

### V-A Various stopping times methodologies

We first proceed by assuming that one of the rates is stochastic, then expand for both assuming either independence or some correlation between the rates.

#### V-A1 Single expected Stopping Time

The "Fugit"-based Heuristic, see [[9](https://arxiv.org/html/2602.14350v1#bib.bib9)], is as follows. Let τ∗\tau^{\*} be the expected discounted stopping time of the American option, measured in risk-neutral time units. If τ\tau denotes the random stopping time (optimal exercise), then the fugit is defined as

|  |  |  |
| --- | --- | --- |
|  | τ∗​(S0,t0)=𝔼Q​[∫t0τe−r​(u−t0)​𝑑u],\tau^{\*}(S\_{0},t\_{0})=\mathbb{E}^{Q}\left[\int\_{t\_{0}}^{\tau}e^{-r(u-t\_{0})}\,du\right], |  |

which can be interpreted as the "effective maturity" or the time-to-exercise that discounts equivalently to the American payoff. For European options, τ∗=T−t0\tau^{\*}=T-t\_{0}; for deep-in-the-money Americans, τ∗\tau^{\*} is substantially shorter.

This quantity can be estimated directly from a binomial or finite-difference grid as the expectation of discounted time spent before exercise.

A trick is proposed by [[9](https://arxiv.org/html/2602.14350v1#bib.bib9)] as a "shortcut method… to find the right duration (i.e., expected time to termination) for an American option". Taleb terms this result "Omega". The formula is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ω=t​ρ2​Aρ2​E,\Omega=t\frac{\rho\_{2A}}{\rho\_{2E}}, |  | (6) |

where tt is the nominal time to expiration, ρ2​A\rho\_{2A} and ρ2​E\rho\_{2E} are "Rhos", the sensitivities of the American and European options to changes in the underlying nominal carry yield.

#### V-A2 The Stochastic Fugit: Distribution of Exercise Times

A deterministic-rate American pricer (binomial, finite-difference, or least-squares Monte Carlo) naturally yields:

* •

  a discrete set of candidate exercise times t1,…,tKt\_{1},\ldots,t\_{K},
* •

  the corresponding exercise probabilities pk=ℙ​(τ=tk)p\_{k}=\mathbb{P}(\tau=t\_{k}).

This defines the *stochastic fugit*:

|  |  |  |
| --- | --- | --- |
|  | T~∈{t1,…,tK},ℙ​(T~=tk)=pk.\tilde{T}\in\{t\_{1},\ldots,t\_{K}\},\qquad\mathbb{P}(\tilde{T}=t\_{k})=p\_{k}. |  |

The classical deterministic fugit is merely the expectation

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ∗=𝔼​[T~]=∑k=1Kpk​tk.\tau^{\*}=\mathbb{E}[\tilde{T}]=\sum\_{k=1}^{K}p\_{k}t\_{k}. |  | (7) |

By retaining the full distribution (tk,pk)(t\_{k},p\_{k}), we preserve the time convexity inherent in the early-exercise feature.

The fugit provides a principled estimate of the expected exercise horizon for use in the rate distribution. It adjusts automatically to the option’s moneyness. This heuristic captures first-order effects of rate uncertainty without solving a full two-factor PDE. It can be extended by integrating over a discrete distribution of fugit times tkt\_{k} from a Bermudan exercise histogram,

|  |  |  |  |
| --- | --- | --- | --- |
|  | OA≈∑kpk​∫OA​(r,t)​fr​(tk)​(r)​𝑑r,O\_{A}\approx\sum\_{k}p\_{k}\int O\_{A}(r,t)\,f\_{r(t\_{k})}(r)\,dr, |  | (8) |

where pk=ℙ​(τ∗=tk)p\_{k}=\mathbb{P}(\tau^{\*}=t\_{k}).

#### V-A3 Fugit-weighted integration heuristic

We define the fugit-weighted American price under rate stochasticity as

|  |  |  |  |
| --- | --- | --- | --- |
|  | OA,τ∗=∫𝔻rOA​(r,t)​fr​(τ∗)​(r)​𝑑r,O\_{A,\tau^{\*}}=\int\_{\mathbb{D}\_{r}}O\_{A}(r,t)\,f\_{r(\tau^{\*})}(r)\,dr, |  | (9) |

where fr​(τ∗)f\_{r(\tau^{\*})} is the density of the stochastic rate evaluated at the expected stopping time τ∗\tau^{\*}. This represents a weighted average of deterministic-rate American prices, with the weights given by the probability distribution of the relevant rate at the fugit time.

### V-B Extension to Two Stochastic Rates

When both rates r1​(t)r\_{1}(t) and r2​(t)r\_{2}(t) are stochastic, possibly correlated, the extension is immediate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | OA(stoch-fugit)=∑l=1Lpl​∬ℝ2OA​(r1,r2,tl)​f(r1,r2)​(tl)​(r1,r2)​𝑑r1​𝑑r2.O\_{A}^{(\text{stoch-fugit})}=\\ \sum\_{l=1}^{L}p\_{l}\iint\_{\mathbb{R}^{2}}O\_{A}(r\_{1},r\_{2},t\_{l})\,f\_{(r\_{1},r\_{2})(t\_{l})}(r\_{1},r\_{2})\,dr\_{1}\,dr\_{2}. |  | (10) |

If independence is assumed,

|  |  |  |
| --- | --- | --- |
|  | f(r1,r2)​(tk)​(r1,r2)=fr1​(tk)​(r1)​fr2​(tk)​(r2).f\_{(r\_{1},r\_{2})(t\_{k})}(r\_{1},r\_{2})=f\_{r\_{1}(t\_{k})}(r\_{1})\,f\_{r\_{2}(t\_{k})}(r\_{2}). |  |

### V-C Various distribution of rates

Let the funding rate r1​(t)r\_{1}(t) or carry rate r2​(t)r\_{2}(t) follow one of the canonical short-rate dynamics:

a) Bachelier or normal world.:

|  |  |  |
| --- | --- | --- |
|  | d​r=μr​d​t+σr​d​Wtdr=\mu\_{r}\,dt+\sigma\_{r}\,dW\_{t} |  |

|  |  |  |
| --- | --- | --- |
|  | ⇒rτ∗∼𝒩​(r0+μr​τ∗,σr2​τ∗).\Rightarrow\quad r\_{\tau^{\*}}\sim\mathcal{N}(r\_{0}+\mu\_{r}\tau^{\*},\,\sigma\_{r}^{2}\tau^{\*}). |  |

b) Vasicek / Hull–White world.:

|  |  |  |
| --- | --- | --- |
|  | d​r=κr​(θr−r)​d​t+σr​d​Wtdr=\kappa\_{r}(\theta\_{r}-r)\,dt+\sigma\_{r}\,dW\_{t} |  |

|  |  |  |
| --- | --- | --- |
|  | ⇒{𝔼​[rτ∗]=θr+(r0−θr)​e−κr​τ∗,Var​[rτ∗]=σr22​κr​(1−e−2​κr​τ∗).\Rightarrow\begin{cases}\mathbb{E}[r\_{\tau^{\*}}]=\theta\_{r}+(r\_{0}-\theta\_{r})e^{-\kappa\_{r}\tau^{\*}},\\ \mathrm{Var}[r\_{\tau^{\*}}]=\dfrac{\sigma\_{r}^{2}}{2\kappa\_{r}}(1-e^{-2\kappa\_{r}\tau^{\*}}).\end{cases} |  |

c) Lognormal world.:

|  |  |  |
| --- | --- | --- |
|  | d​r2r=μr​d​t+σr​d​Wt\frac{dr\_{2}}{r}=\mu\_{r}\,dt+\sigma\_{r}\,dW\_{t} |  |

|  |  |  |
| --- | --- | --- |
|  | ⇒rτ∗=r20​exp⁡((μr−12​σr2)​τ∗+σr​τ∗​Z),Z∼𝒩​(0,1).\Rightarrow\quad r\_{\tau^{\*}}=r\_{20}\exp\!\left((\mu\_{r}-\tfrac{1}{2}\sigma\_{r}^{2})\tau^{\*}+\sigma\_{r}\sqrt{\tau^{\*}}\,Z\right),\\ \qquad Z\sim\mathcal{N}(0,1). |  |

\*\*

The end result for us is testing , where .~​(r)\widetilde{.}(r) denotes stochasticity over parameter rr, OA​(r)~−OA​(r)\widetilde{O\_{A}(r)}-O\_{A}(r), the extra optionality, after clearing a few hurdles.

We will perform tests to establish whether the fugit shortcut represents a good enough an approximation and whether various rate dynamics (presented in the next section) make a difference for the convexity bias.

![Refer to caption](sigma1.png)


Figure 1: Optionality versus standard deviation for a an equity put option under a normally distributed local interest rate with O​A​(r∗)=14.3184OA(r^{\*})=14.3184, S/K=1.00S/K=1.00

![Refer to caption](sigma2.png)


Figure 2: Optionality versus standard deviation for a currency put option under a lognormally distributed local interest rate with O​A​(r∗)=15.1700OA(r^{\*})=15.1700 and S/K=1.00S/K=1.00

![Refer to caption](sigma3.png)


Figure 3: Optionality versus standard deviation for a currency call option under a Hull-White distributed local interest rate with O​A​(r∗)=12.7779OA(r^{\*})=12.7779 and S/K=1.00S/K=1.00

## VI Main Numerical Implementation

We work throughout these simulations with options with –to normalize –a maturity of one year, hence no loss of generality. We consider equity puts, currency puts, and currency calls with stochastic local rate.

In our base example, we consider a generic at-the-money American equity put option on a high volatility stock, with the following common parameters, volatility (put on the upper end of common values), σ=40%\sigma=40\%, maturity, T=12T=12 months, initial underlying asset value, S0=100S\_{0}=100, strike price, K=100K=100, and a stochastic interest rate with an initial value r0=1%r\_{0}=1\%. (With respect to the notation in Section I of this paper, this is an American option with r1=rr\_{1}=r and r2=0r\_{2}=0.) For the stochastic rate, we assume that it follows a Bachelier process (that is, normally distributed as defined in Section [V-C](https://arxiv.org/html/2602.14350v1#S5.SS3 "V-C Various distribution of rates ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options")), with mean r¯=4.18%\bar{r}=4.18\% and standard deviation σr=1.28%\sigma\_{r}=1.28\% at maturity, as described in Section [V-C](https://arxiv.org/html/2602.14350v1#S5.SS3 "V-C Various distribution of rates ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options") of this paper. These parameters align with recent values of the 1-year US treasury rate. Specifically, we consider the 1-year treasury yield over the past three years [[14](https://arxiv.org/html/2602.14350v1#bib.bib14)], where the yield is reported at the end of every month from January 2022 until March 2025.

We start by computing the stopping time using expectation of the classical deterministic fugit using ([7](https://arxiv.org/html/2602.14350v1#S5.E7 "In V-A2 The Stochastic Fugit: Distribution of Exercise Times ‣ V-A Various stopping times methodologies ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options")). Accordingly, we compute the American option value, O~A​(r)\widetilde{O}\_{A}(r), under a normal interest rate using ([9](https://arxiv.org/html/2602.14350v1#S5.E9 "In V-A3 Fugit-weighted integration heuristic ‣ V-A Various stopping times methodologies ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options")). The parameters of the interest rate process are determined based on matching the first two moments of the rate at maturity, rTr\_{T}, with r¯\bar{r} and σr\sigma\_{r}. For instance, under a normally distributed interest rate, the drift and volatility are obtained by moment matching as μ=r¯−r0T\mu=\frac{\bar{r}-r\_{0}}{T} and σ=σr/T\sigma=\sigma\_{r}/\sqrt{T}. The binomial lattice is used to compute the American option price for a fixed interest rate, taking into consideration the early exercise feature. Then, using the Gauss-Hermite quadrature we approximates the expectation of this price with respect to the stochastic interest rate by evaluating the lattice-based price at a finite number of carefully chosen interest rate realizations and aggregating them using predetermined weights. More details about the approach can be found in section LABEL:further.

We compare the results with the corresponding deterministic price of an American option, with the local rate being equal to the average interest rate at the expected fugit τ∗\tau^{\*}, OA​(r∗)O\_{A}(r^{\*}). We then estimate

|  |  |  |  |
| --- | --- | --- | --- |
|  | πA=O~A​(r)−OA​(r∗),\pi\_{A}=\widetilde{O}\_{A}(r)-O\_{A}(r^{\*}), |  | (11) |

as a measure of the gain from the hidden optionality of the American option. We compute πA\pi\_{A} and present the results in Table [I](https://arxiv.org/html/2602.14350v1#S6.T1 "TABLE I ‣ VI Main Numerical Implementation ‣ Hidden Risks and Optionalities in American Options"). To investigate the impact of interest-rate uncertainty, we vary the standard deviation parameter of the interest-rate process σr\sigma\_{r}. As expected, the difference πA\pi\_{A} increases with the variability of the interest rate. When the volatility is set to zero, the stochastic model converges to the deterministic case and the difference becomes exactly zero. This monotonic increase in πA\pi\_{A} as standard deviation rises is clearly observed in Figure [1](https://arxiv.org/html/2602.14350v1#S5.F1 "Figure 1 ‣ V-C Various distribution of rates ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options"). We repeat the same numerical experiments under a local rate following Geometric Brownian motion and Hull-White processes, as defined in Section [V-C](https://arxiv.org/html/2602.14350v1#S5.SS3 "V-C Various distribution of rates ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options"), and present the results in Figures [2](https://arxiv.org/html/2602.14350v1#S5.F2 "Figure 2 ‣ V-C Various distribution of rates ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options") and [3](https://arxiv.org/html/2602.14350v1#S5.F3 "Figure 3 ‣ V-C Various distribution of rates ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options"), respectively. We observe a similar behavior, as discussed in more details in section LABEL:further.

| σr\sigma\_{r} | O~A​(r)\widetilde{O}\_{A}(r) | πA\pi\_{A} |
| --- | --- | --- |
| 0.0000 | 14.3184 | 0.0000 |
| 0.0028 | 14.3190 | 0.0006 |
| 0.0078 | 14.3231 | 0.0048 |
| 0.0128 | 14.3314 | 0.0130 |
| 0.0178 | 14.3445 | 0.0261 |
| 0.0228 | 14.3629 | 0.0446 |
| 0.0278 | 14.3878 | 0.0694 |
| 0.0328 | 14.4162 | 0.0978 |
| 0.0378 | 14.4492 | 0.1308 |
| 0.0428 | 14.4892 | 0.1708 |
| 0.0478 | 14.5319 | 0.2136 |

TABLE I: Optionality as a function of the standard deviation of a normally distributed interest rate with O​A​(r∗)=14.3184OA(r^{\*})=14.3184, S/K=1.00S/K=1.00

## VII Further Numerical Results and Technical Details

In Section [VII-A](https://arxiv.org/html/2602.14350v1#S7.SS1 "VII-A Binomial Lattice and Fugit Distribution ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options"), we briefly discuss the binomial lattice method ([[16](https://arxiv.org/html/2602.14350v1#bib.bib16)]) used to compute the integration and to obtain the expected fugit. In Section [VII-B](https://arxiv.org/html/2602.14350v1#S7.SS2 "VII-B Expected Sopping Time Ω ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options"), we investigate the proposed heuristics in ([6](https://arxiv.org/html/2602.14350v1#S5.E6 "In V-A1 Single expected Stopping Time ‣ V-A Various stopping times methodologies ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options")) and then compare the results with the expected fugit estimated from the lattice in Section [VII-A](https://arxiv.org/html/2602.14350v1#S7.SS1 "VII-A Binomial Lattice and Fugit Distribution ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options"), which can be seen as the “exact" baseline. In Section [VII-C](https://arxiv.org/html/2602.14350v1#S7.SS3 "VII-C Different Rate Dynamics and Moneyness Levels ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options"), we study how changes in the dynamics of interest rate, under alternative distributional assumptions, affect our results. Finally, In Section [VII-D](https://arxiv.org/html/2602.14350v1#S7.SS4 "VII-D Optionality of American vs European ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options"), we briefly exhibit an alternative approach of measure optionality by comparing the American option value to a European counterpart.

### VII-A Binomial Lattice and Fugit Distribution

This section presents the numerical framework used throughout the paper. The starting point is the computation of τ∗=𝔼​[T~]\tau^{\*}=\mathbb{E}[\tilde{T}] in ([7](https://arxiv.org/html/2602.14350v1#S5.E7 "In V-A2 The Stochastic Fugit: Distribution of Exercise Times ‣ V-A Various stopping times methodologies ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options")), the expected optimal stopping time of an American option using the classical deterministic fugit. Then, we employ the binomial lattice to compute the value of an American option with stochastic local rate, O~​A​(r)\widetilde{O}A(r) , through numerical integration.

Following the notation described in [[15](https://arxiv.org/html/2602.14350v1#bib.bib15)], we briefly recall the elements of the lattice that are required for the computation of the expected fugit and the subsequent numerical valuation. Let the maturity TT be divided into nn time steps of length δ​t=T/ns\delta t=T/n\_{s}. In accordance with [[15](https://arxiv.org/html/2602.14350v1#bib.bib15)], we set n=2000n=2000, which provides stable and accurate numerical results. The stock price evolves on the lattice according to the multipliers u=eσ​δ​tu=e^{\sigma\sqrt{\delta t}} and d=1ud=\frac{1}{u}, with a risk–neutral probability q=e(rf−δ)​δ​t−du−dq=\frac{e^{(r\_{f}-\delta)\delta t}-d}{u-d}, where rfr\_{f} denotes the continuously compounded risk–free rate and δ\delta the dividend yield (or foreign rate in the currency case). Starting with S​(i,j)S(i,j), the stock price at time step ii and state jj, and by P​(i,j)P(i,j) the American option value can be obtained through backward recursion. At maturity, i=ni=n, the final payoff is P​(ns,j)=max⁡(K−S​(ns,j), 0)P(n\_{s},j)=\max(K-S(n\_{s},j),\,0) for a put option (with an analogous expression for a call). For i<ni<n, the value of the option is the maximum between the exercise payoff and the continuation value, P​(i,j)=max⁡{K−S​(i,j),Vc​(i,j)}P(i,j)=\max\!\bigl\{K-S(i,j),\;V\_{c}(i,j)\bigr\}, where the continuation value is given by Vc​(i,j)=e−rf​δ​t​[q​P​(i+1,j+1)+(1−q)​P​(i+1,j)]V\_{c}(i,j)=e^{-r\_{f}\delta t}\Bigl[q\,P(i+1,j+1)+(1-q)\,P(i+1,j)\Bigr]. The backward recursion simultaneously determines the optimal exercise region. Accordingly, we can define an early exercise indicator

|  |  |  |
| --- | --- | --- |
|  | I​(i,j)={1,if ​K−S​(i,j)≥Vc​(i,j),0,otherwise.I(i,j)=\begin{cases}1,&\text{if }K-S(i,j)\geq V\_{c}(i,j),\\ 0,&\text{otherwise}.\end{cases} |  |

The optimal stopping time is therefore the first index

|  |  |  |
| --- | --- | --- |
|  | τ=min⁡{i≥0:I​(i,ji)=1},\tau=\min\{i\geq 0:I(i,j\_{i})=1\}, |  |

with corresponding point in time t∗=τ​δ​tt^{\*}=\tau\,\delta t.

To compute the distribution of τ\tau, the probability mass function is propagated forward through the lattice while enforcing the optimal stopping rule. Let π​(i,j)\pi(i,j) denote the probability of reaching node (i,j)(i,j) without
prior exercise, with initialization π​(0,0)=1\pi(0,0)=1. For each time step i=0,…,ns−1i=0,\dots,n\_{s}-1, the below strategy is followed

* •

  If I​(i,j)=1I(i,j)=1, the probability π​(i,j)\pi(i,j) is recorded as stopping at time index ii and is not propagated further.
* •

  If I​(i,j)=0I(i,j)=0, the probability evolves according to the risk–neutral dynamics,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | π​(i+1,j+1)=π​(i+1,j+1)+q​π​(i,j),π​(i+1,j)=π​(i+1,j)+(1−q)​π​(i,j).\pi(i+1,j+1)=\pi(i+1,j+1)+q\,\pi(i,j),\\ \pi(i+1,j)=\pi(i+1,j)+(1-q)\,\pi(i,j). |  | (12) |

Denoting by Pf​(i)P\_{f}(i) the probability of optimal exercise at step ii, the expected fugit conditional on exercise is

|  |  |  |
| --- | --- | --- |
|  | τ∗=𝔼​[t∗∣exercise]=∑i=0ns(i​δ​t)​Pf​(i)∑i=0nsPf​(i).\tau^{\*}=\mathbb{E}[t^{\*}\mid\text{exercise}]=\frac{\sum\_{i=0}^{n\_{s}}(i\,\delta t)\,P\_{f}(i)}{\sum\_{i=0}^{n\_{s}}P\_{f}(i)}. |  |

A complete algorithm to compute the fugit pmf Pf​(i)P\_{f}(i) and expected value τ∗\tau^{\*} is presented next. While the algorithm is straightforward, we could not identify any similar approaches in the literature. There are some online forums hinting to it without enough details. The following complete algorithm can be seen as a side-contribution of this paper.

Algorithm for the fugit distribution.

Step 1
  
Input the values for S0S\_{0}, KK, TT, nn, RR, δ\delta, and σ\sigma.
  
Set δ​t=T/ns\delta t=T/n\_{s}. Construct the CRR parameters uu, dd, and qq (see [[15](https://arxiv.org/html/2602.14350v1#bib.bib15)].

Step 2
  
Build the recombining stock-price lattice {S​(i,j)}0≤i≤n, 0≤j≤i\{S(i,j)\}\_{0\leq i\leq n,\,0\leq j\leq i}.

Step 3
  
Initialize the terminal option values at maturity:
  
   For j=0,…,nj=0,\dots,n, set P​(n,j)=Φ​(S​(n,j))P(n,j)=\Phi(S(n,j)), where Φ​(S)=K−S\Phi(S)=K-S.

Step 4
  
Backward recursion (pricing + exercise indicator):
  
   For i=n−1,…,0i=n-1,\dots,0:
  
     For j=0,…,ij=0,\dots,i:
  
       Set Vc​(i,j)=1R​(q​P​(i+1,j+1)+(1−q)​P​(i+1,j))V\_{c}(i,j)=\frac{1}{R}\Big(q\,P(i+1,j+1)+(1-q)\,P(i+1,j)\Big).
  
       Set P​(i,j)=max⁡{Φ​(S​(i,j)),Vc​(i,j)}P(i,j)=\max\{\Phi(S(i,j)),\,V\_{c}(i,j)\}.
  
       If Φ​(S​(i,j))≥Vc​(i,j)\Phi(S(i,j))\geq V\_{c}(i,j) set I​(i,j)=1I(i,j)=1, else set I​(i,j)=0I(i,j)=0.

Step 5
  
Forward recursion (probabilities of reachable nodes and stopping distribution):
  
   Create an empty matrix π\pi of size (n+1)×(ns+1)(n+1)\times(n\_{s}+1) and set π​(0,0)=1\pi(0,0)=1.
  
   Create an empty vector PfP\_{f} of length (ns+1)(n\_{s}+1) and set Pf​(i)=0P\_{f}(i)=0 for all ii.
  
   For i=0,…,n−1i=0,\dots,n-1:
  
     For j=0,…,ij=0,\dots,i:
  
       If π​(i,j)=0\pi(i,j)=0, continue.
  
       If I​(i,j)=1I(i,j)=1, set Pf​(i)=Pf​(i)+π​(i,j)P\_{f}(i)=P\_{f}(i)+\pi(i,j) (stop here).
  
       Otherwise propagate:
  
        π​(i+1,j+1)=π​(i+1,j+1)+q​π​(i,j)\pi(i+1,j+1)=\pi(i+1,j+1)+q\,\pi(i,j),
  
        π​(i+1,j)=π​(i+1,j)+(1−q)​π​(i,j)\pi(i+1,j)=\pi(i+1,j)+(1-q)\,\pi(i,j).

Step 6
  
Maturity handling:
  
   For j=0,…,nj=0,\dots,n, if π​(n,j)>0\pi(n,j)>0 and Φ​(S​(n,j))>0\Phi(S(n,j))>0,
  
     set Pf​(n)=Pf​(n)+π​(n,j)P\_{f}(n)=P\_{f}(n)+\pi(n,j).

Step 7
  
Expected fugit (conditional on exercise):
  
   Set ti=i​δ​tt\_{i}=i\,\delta t for i=0,…,ni=0,\dots,n.
  
   Set Et=∑i=0nti​Pf​(i)∑i=0nPf​(i)E\_{t}=\dfrac{\sum\_{i=0}^{n}t\_{i}\,P\_{f}(i)}{\sum\_{i=0}^{n}P\_{f}(i)}.

Output
  
Return the stopping distribution {Pf​(i)}i=0n\{P\_{f}(i)\}\_{i=0}^{n} and the expected fugit EtE\_{t}.

Once the expected fugit has been obtained, the same binomial lattice is used to evaluate the optimality measure πA\pi\_{A}. First, a deterministic benchmark is computed by evaluating the lattice with an interest rate r∗=E​[r​(t∗)]r^{\*}={E}[r(t^{\*})], . For instance, under a normally distributed interest rate, the deterministic benchmark rate is simply E​[r​(t∗)]=r0+μ​τ∗{E}[r(t^{\*})]=r\_{0}+\mu\tau^{\*}.
Having defined the deterministic value O​A​(r∗)OA(r^{\*}), the optimality measure πA\pi\_{A} is obtained by comparing O​A​(r∗)OA(r^{\*}) with the option value that accounts for a stochastic interest rate, O~​A​(r)\widetilde{O}A(r). Accordingly, O~​A​(r)\widetilde{O}A(r) is obtained using the obtained expected fugit and the integration in ([9](https://arxiv.org/html/2602.14350v1#S5.E9 "In V-A3 Fugit-weighted integration heuristic ‣ V-A Various stopping times methodologies ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options")), which is evaluated numerically using the Gauss-Hermite quadrature (e.g. [[13](https://arxiv.org/html/2602.14350v1#bib.bib13)]). This numerical integration method approximates the expectation by a weighted sum of lattice prices evaluated at optimally chosen rate nodes.

### VII-B Expected Sopping Time Ω\Omega

In this section, we compare the effective stopping time developed by Taleb [[9](https://arxiv.org/html/2602.14350v1#bib.bib9)] using ([6](https://arxiv.org/html/2602.14350v1#S5.E6 "In V-A1 Single expected Stopping Time ‣ V-A Various stopping times methodologies ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options")) and using the expectation of the classical deterministic fugit in ([7](https://arxiv.org/html/2602.14350v1#S5.E7 "In V-A2 The Stochastic Fugit: Distribution of Exercise Times ‣ V-A Various stopping times methodologies ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options")), for an equity put, currency put, and currency call.

#### B.II.1 Equity Put

We consider an equity put option with the input parameters mentioned in Table [I](https://arxiv.org/html/2602.14350v1#S6.T1 "TABLE I ‣ VI Main Numerical Implementation ‣ Hidden Risks and Optionalities in American Options").
We estimate OA​(r)O\_{A}(r) from the binomial lattice method, at the deterministic benchmark, as explained in Section B.I. The European call OE​(r)O\_{E}(r) is valuated based on the Black-Scholes-Merton formula ([[17](https://arxiv.org/html/2602.14350v1#bib.bib17)]). We first estimate the American and European option sensitivities with respect to the interest rate, ρ2​A=∂OA​(r)∂r\rho\_{2A}=\frac{\partial O\_{A}(r)}{\partial r} and ρ2​E=∂OE​(r)∂r\rho\_{2E}=\frac{\partial O\_{E}(r)}{\partial r}, using a common heuristic based on central difference method,

|  |  |  |
| --- | --- | --- |
|  | ρ2​J=|OA​(r+0.01,t)−OA​(r,t)|+|OA​(r−0.01,t)−OA​(r,t)|2,J=A,E.\rho\_{2J}=\\ \frac{|O\_{A}(r+0.01,t)-O\_{A}(r,t)|+|O\_{A}(r-0.01,t)-O\_{A}(r,t)|}{2},\\ J=A,E. |  |

We use the values of ρ2​A\rho\_{2A} and ρ2​E\rho\_{2E} to obtain the effective stopping time associated with the early exercise feature of an American option using ([6](https://arxiv.org/html/2602.14350v1#S5.E6 "In V-A1 Single expected Stopping Time ‣ V-A Various stopping times methodologies ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options")). We also compute compute the stopping time using expectation of the classical deterministic fugit using ([7](https://arxiv.org/html/2602.14350v1#S5.E7 "In V-A2 The Stochastic Fugit: Distribution of Exercise Times ‣ V-A Various stopping times methodologies ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options")). We obtain close results, as shown in Table [II](https://arxiv.org/html/2602.14350v1#S7.T2 "TABLE II ‣ B.II.1 Equity Put ‣ VII-B Expected Sopping Time Ω ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options"), which confirm the validity of the heuristics approached suggested by Taleb [[9](https://arxiv.org/html/2602.14350v1#bib.bib9)]. The results also show how τ∗\tau^{\*} changes with moneyness. As expected, a lower moneyness level implies an earlier exercise time, i.e., the expected fugit is increasing in the moneyness. Figure [4](https://arxiv.org/html/2602.14350v1#S7.F4 "Figure 4 ‣ B.II.1 Equity Put ‣ VII-B Expected Sopping Time Ω ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options") also demonstrates this graphically.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| S/KS/K | ρA\rho\_{A} | ρE\rho\_{E} | τ∗=Ω\tau^{\*}=\Omega | τ∗=𝔼​[T~]\tau^{\*}=\mathbb{E}[\tilde{T}] |
| 0.80000.8000 | 0.299310.29931 | 0.48000.4800 | 7.48337.4833 | 6.69546.6954 |
| 0.90000.9000 | 0.32040.3204 | 0.43530.4353 | 8.83358.8335 | 7.79247.7924 |
| 1.00001.0000 | 0.30470.3047 | 0.38040.3804 | 9.61179.6117 | 8.87818.8781 |
| 1.10001.1000 | 0.27280.2728 | 0.32300.3230 | 10.134910.1349 | 9.47859.4785 |
| 1.20001.2000 | 0.23480.2348 | 0.26820.2682 | 10.503310.5033 | 9.92599.9259 |
| 1.30001.3000 | 0.19640.1964 | 0.21900.2190 | 10.764110.7641 | 10.228810.2288 |
| 1.40001.4000 | 0.16110.1611 | 0.17640.1764 | 10.962210.9622 | 10.482110.4821 |

TABLE II: Effective stopping time τ∗\tau^{\*}, in months, for an equity put option.

![Refer to caption](image1.png)


Figure 4: Effective sopping time τ∗\tau^{\*} versus moneyness for an equity put option.

#### VII-B1 Currency Put

In this section, we consider a currency put with base parameter values similar to those in section LABEL:, with a foreign rate r2=2.8%r\_{2}=2.8\%. These parameters are given in Table [III](https://arxiv.org/html/2602.14350v1#S7.T3 "TABLE III ‣ VII-B1 Currency Put ‣ VII-B Expected Sopping Time Ω ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options") for completeness.

| KK | SS | TT | σ\sigma | r2r\_{2} | r10r\_{10} | r1¯\bar{r\_{1}} | σr1\sigma\_{r\_{1}} |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | 80 | 1y | 40% | 2.8000% | 1% | 4.18% | 1.28% |

TABLE III: Input parameters for the base example on interest stochasticity for a currency put

Similar to equity puts, we determine the effective stopping time τ∗\tau^{\*} for the American currency put using ([6](https://arxiv.org/html/2602.14350v1#S5.E6 "In V-A1 Single expected Stopping Time ‣ V-A Various stopping times methodologies ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options")) and ([7](https://arxiv.org/html/2602.14350v1#S5.E7 "In V-A2 The Stochastic Fugit: Distribution of Exercise Times ‣ V-A Various stopping times methodologies ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options")). The results are presented in Figure [5](https://arxiv.org/html/2602.14350v1#S7.F5 "Figure 5 ‣ VII-B1 Currency Put ‣ VII-B Expected Sopping Time Ω ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options") for different moneyness levels. We obtain again similar results as in the case of an equity put option confirming the validity of Taleb’s heuristic in ([6](https://arxiv.org/html/2602.14350v1#S5.E6 "In V-A1 Single expected Stopping Time ‣ V-A Various stopping times methodologies ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options")).

| S/KS/K | ρA\rho\_{A} | ρE\rho\_{E} | τ∗=Ω\tau^{\*}=\Omega | τ∗=𝔼​[T~]\tau^{\*}=\mathbb{E}[\tilde{T}] |
| --- | --- | --- | --- | --- |
| 0.80000.8000 | 0.47440.4744 | 0.48760.4876 | 8.48168.4816 | 7.6977 |
| 0.90000.9000 | 0.43800.4380 | 0.44770.4477 | 9.42929.4292 | 8.7379 |
| 1.00001.0000 | 0.39040.3904 | 0.39600.3960 | 10.037910.0379 | 9.4770 |
| 1.10001.1000 | 0.33710.3371 | 0.34040.3404 | 10.448710.4487 | 9.9653 |
| 1.20001.2000 | 0.28410.2841 | 0.28590.2859 | 10.738710.7387 | 10.3291 |
| 1.30001.3000 | 0.23490.2349 | 0.23590.2359 | 10.952110.9521 | 10.5744 |
| 1.40001.4000 | 0.19150.1915 | 0.192150.19215 | 11.103611.1036 | 10.7799 |

TABLE IV: Effective sopping time τ∗\tau^{\*} versus moneyness for a currency put option.

![Refer to caption](image3.png)


Figure 5: Effective sopping time τ∗\tau^{\*} versus moneyness for an American currency put

#### VII-B2 Currency Call

We study a currency call option with parameters similar to those of the currency put above but with a foreign rate r2=10%r\_{2}=10\%. The observations we make here are also applicable to call options with dividends, which have a similar pricing structure.111Optionality in the context of non-dividend paying equity calls is not relevant as it is not optimal to exercise these options before maturity, e.g. Hull [[10](https://arxiv.org/html/2602.14350v1#bib.bib10)]. The results in
Figure [6](https://arxiv.org/html/2602.14350v1#S7.F6 "Figure 6 ‣ VII-B2 Currency Call ‣ VII-B Expected Sopping Time Ω ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options"), which again validates the heuristic ([6](https://arxiv.org/html/2602.14350v1#S5.E6 "In V-A1 Single expected Stopping Time ‣ V-A Various stopping times methodologies ‣ V Integrating an American Option across Stochastic Rates ‣ Hidden Risks and Optionalities in American Options")).

| KK | SS | TT | σ\sigma | rfr\_{f} | r0r\_{0} | r¯\bar{r} | σr\sigma\_{r} |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | 80 | 1y | 40% | 10% | 3% | 4.18% | 1.28% |

TABLE V: Input parameters for the base case for currency call option under stochastic local rate



| S/KS/K | ρA\rho\_{A} | ρE\rho\_{E} | τ∗=Ω\tau^{\*}=\Omega | τ∗=𝔼​[T~]\tau^{\*}=\mathbb{E}[\tilde{T}] |
| --- | --- | --- | --- | --- |
| 0.80000.8000 | 0.19000.1900 | 0.22260.2226 | 10.2419610.24196 | 9.8729 |
| 0.90000.9000 | 0.27190.2719 | 0.33990.3399 | 9.600749.60074 | 9.2454 |
| 1.00001.0000 | 0.34700.3470 | 0.47220.4722 | 8.81808.8180 | 8.4378 |
| 1.10001.1000 | 0.40110.4011 | 0.61230.6123 | 7.86087.8608 | 7.4642 |
| 1.20001.2000 | 0.42260.4226 | 0.75480.7548 | 6.71866.7186 | 6.3336 |
| 1.30001.3000 | 0.40130.4013 | 0.89550.8955 | 5.37695.3769 | 5.0576 |
| 1.40001.4000 | 0.32900.3290 | 1.03221.0322 | 3.82503.8250 | 3.5660 |

TABLE VI: Effective stopping time τ∗\tau^{\*} for an American currency call option

![Refer to caption](image5.png)


Figure 6: Effective sopping time τ∗\tau^{\*} versus moneyness for an American currency call

### VII-C Different Rate Dynamics and Moneyness Levels

In this section, we evaluate the hidden optionality of American equity puts, currency puts, and currency calls, under different rate dynamics. Similar to section [VI](https://arxiv.org/html/2602.14350v1#S6 "VI Main Numerical Implementation ‣ Hidden Risks and Optionalities in American Options"), we start by considering a normally distributed interest rate, and then extend the analysis to a lognormally and Hull-White distributed rate.

#### VII-C1 Equity Put

In this section, we consider the American equity put with the same parameters as before. We begin by extending the normal interest rate framework through additional experiments, using two other fixed values of S/KS/K, and we present the corresponding results in Figure [7](https://arxiv.org/html/2602.14350v1#S7.F7 "Figure 7 ‣ VII-C1 Equity Put ‣ VII-C Different Rate Dynamics and Moneyness Levels ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options"). We observe that, the lower the moneyness levels, the greater is the optionality.

![Refer to caption](moneyness.png)


Figure 7: Optionality versus standard deviation for an equity put under a normally distributed local interest rate for different moneyness levels

Then, we consider a stochastic rate that is Hulll-White and lognormally distributed, with the results reported in
Figure [8](https://arxiv.org/html/2602.14350v1#S7.F8 "Figure 8 ‣ VII-C1 Equity Put ‣ VII-C Different Rate Dynamics and Moneyness Levels ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options"). We observe a behavior similar to that under a normal distribution, as the standard deviation σr\sigma\_{r} increases, the level of hidden optionality becomes more pronounced. Again, the results show consistent monotone optionality values, πA\pi\_{A}, as a function of the interest rate volatility.

![Refer to caption](distributions1.png)


Figure 8: Optionality versus standard deviation for a an equity put option under different rate dynamics with S/K=1.00S/K=1.00

#### VII-C2 Currency Put

In this section, we further study the optionality of the American currency put, with the base parameters listed in Table [III](https://arxiv.org/html/2602.14350v1#S7.T3 "TABLE III ‣ VII-B1 Currency Put ‣ VII-B Expected Sopping Time Ω ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options"). For S/K=1S/K=1 and under a local rate, r1r\_{1} which is (i) normally, (ii) log-normally and (iii) Hull-White distributed, the optionality metric πA\pi\_{A} is computed similar to the case equity puts in section [VI](https://arxiv.org/html/2602.14350v1#S6 "VI Main Numerical Implementation ‣ Hidden Risks and Optionalities in American Options"). We vary again the standard deviation of the interest rate σr\sigma\_{r} and evaluate the resulting πA\pi\_{A}, which increases with σr\sigma\_{r}, as illustrated in
Figure [9](https://arxiv.org/html/2602.14350v1#S7.F9 "Figure 9 ‣ VII-C2 Currency Put ‣ VII-C Different Rate Dynamics and Moneyness Levels ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options"). Moreover, we compute the optionality measure πA\pi\_{A} for three different moneyness levels and we present the results in Figure [10](https://arxiv.org/html/2602.14350v1#S7.F10 "Figure 10 ‣ VII-C2 Currency Put ‣ VII-C Different Rate Dynamics and Moneyness Levels ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options"). The results confirm once again that the deeper the option is in the money, the greater is the optionality.

![Refer to caption](distributions2.png)


Figure 9: Optionality versus standard deviation for currency put option under different rate dynamics with S/K=1.00S/K=1.00

![Refer to caption](moneyness2.png)


Figure 10: Optionality versus standard deviation for a currency put under a normally distributed local interest rate for different moneyness levels

#### VII-C3 Currency Call

Next, we explore currency call options using similar parameters to those in Section [VII-B2](https://arxiv.org/html/2602.14350v1#S7.SS2.SSS2 "VII-B2 Currency Call ‣ VII-B Expected Sopping Time Ω ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options"), and under various local rate distributions. The results are shown in
and Figure [11](https://arxiv.org/html/2602.14350v1#S7.F11 "Figure 11 ‣ VII-C3 Currency Call ‣ VII-C Different Rate Dynamics and Moneyness Levels ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options") confirm a consistent monotonic behavior of the optionality metric as a function of the rate volatility. Then, we consider three different moneyness levels and repeat the same experiments. The results in Figure [12](https://arxiv.org/html/2602.14350v1#S7.F12 "Figure 12 ‣ VII-C3 Currency Call ‣ VII-C Different Rate Dynamics and Moneyness Levels ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options") reveal again that deep in the money currency calls (with high values of the moneyness S/KS/K) exhibit higher optionality.

![Refer to caption](distributions3.png)


Figure 11: Optionality versus standard deviation for a currency put option under different rate dynamics with S/K=1.00S/K=1.00

![Refer to caption](moneyness3.png)


Figure 12: Optionality versus standard deviation for a currency call under a normally distributed local interest rate for different moneyness levels

### VII-D Optionality of American vs European

As an alternative measure of hidden optionality, we can compute the stochasticized American option value, O~​A​(r)\widetilde{O}A(r), under a normal interest rate, and compare it with the corresponding European price, estimated as

|  |  |  |
| --- | --- | --- |
|  | O~​E​(r)=∫DrO​E​(r)​frT​(r)​𝑑r,\widetilde{O}E(r)=\int\_{D\_{r}}OE(r)f\_{r\_{T}}(r)dr, |  |

where frT​(r)f\_{r\_{T}}(r) is the density of the interest rate at the option maturity, TT. We then estimate

|  |  |  |
| --- | --- | --- |
|  | πA(2)=O~​A​(r)−O~​E​(r),\pi\_{A}^{(2)}=\widetilde{O}A(r)-\widetilde{O}E(r), |  |

as a measure of the gain from the hidden optionality of the American option. We compute πA(2)\pi\_{A}^{(2)} for various moneyness levels for (i) an equity put, (ii) a currency put, and (iii) a currency call. We present the results in Figures [13](https://arxiv.org/html/2602.14350v1#S7.F13 "Figure 13 ‣ VII-D Optionality of American vs European ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options")-[15](https://arxiv.org/html/2602.14350v1#S7.F15 "Figure 15 ‣ VII-D Optionality of American vs European ‣ VII Further Numerical Results and Technical Details ‣ Hidden Risks and Optionalities in American Options").
The results show again consistent positive πA(2)\pi\_{A}^{(2)} values, indicating that the American option is less vulnerable to interest rate stochasticity than the European one. In addition, we observe that the lower the moneyness level, the greater is the optionality (and implicitly the robustness) of the American option over the European one. Such results have been observed, sporadically, in the literature, e.g., [[18](https://arxiv.org/html/2602.14350v1#bib.bib18)] and [[12](https://arxiv.org/html/2602.14350v1#bib.bib12)].

![Refer to caption](image2.png)


Figure 13: πA(2)\pi\_{A}^{(2)} versus moneyness for equity put options under a normally distributed interest rate

![Refer to caption](image4.png)


Figure 14: πA(2)\pi\_{A}^{(2)} versus moneyness for currency put options under a normally distributed interest rate

![Refer to caption](image6.png)


Figure 15: πA(2)\pi\_{A}^{(2)} versus moneyness for currency call options under a normally distributed local interest rate

## VIII Discussion

This paper uncovered significant hidden convexity in American options and presented a technique for pricing and uncovering hidden risks so far ignored in the literature. While our approach was near-exhaustive, by focusing on one single interest rate, even simpler techniques can be applied on the fly, see Eq. [3](https://arxiv.org/html/2602.14350v1#S1.E3 "In I-A A note on model nonlinearity as fragility ‣ I Unaccounted Optionality ‣ Hidden Risks and Optionalities in American Options") as πΔ​a\pi\_{\Delta a} could be immediately computed by moving either rate.

## References

* [1]

  Taleb, N.N. and Douady, R. (2013). Mathematical definition, mapping, and detection of (anti) fragility.Quantitative Finance.
* [2]

  Taleb, N.N., Canetti, E., Kinda, T., Loukoianova, E., and Schmieder, C.
  (2018).
  A new heuristic measure of fragility and tail risks: application to
  stress testing.
  International Monetary Fund.
* [3]

  Bachelier L. Théorie de la spéculation. Ann Sci Éc Norm Supér. 1900;17:21–86.
* [4]

  Dupire B. Pricing with a smile. Risk. 1994;7(1):18–20.
* [5]

  Dupire B. A unified theory of volatility. In: Derivatives pricing and credit exposures. London: Risk Publications; 1997.
* [6]

  Derman E, Kani I. The volatility smile and its implied tree. Quantitative Strategies Research Notes. New York (NY): Goldman Sachs; 1994.
* [7]

  Hull J, White A. The pricing of options on assets with stochastic volatilities. J Finance. 1987;42(2):281–300.
* [8]

  Gatheral J. The volatility surface: a practitioner’s guide. Hoboken (NJ): John Wiley & Sons; 2006.
* [9]

  Taleb N. N. Dynamic hedging: managing vanilla and exotic options. New York (NY): John Wiley & Sons; 1997.
* [10]

  Hull JC. Options, futures, and other derivatives. 10th ed. Harlow: Pearson; 2017.
* [11]

  Garman MB, Kohlhagen SW. Foreign currency option values. J Int Money Finance. 1983;2(3):231–7.
* [12]

  Medvedev A, Scaillet O. Pricing American options under stochastic volatility and stochastic interest rates. J Financ Econ. 2010;98(1):145–68.
* [13]

  Stoer J, Bulirsch R. Introduction to numerical analysis. 3rd ed. New York (NY): Springer Science & Business Media; 2013 Mar 9. Chapter 3, Topics in integration.
* [14]

  FRED, Federal Reserve Bank of St. Louis, 2025. Market yield on U.S. Treasury securities at 1-year constant maturity, quoted on an investment basis [DGS1].
  Available at: https://fred.stlouisfed.org/series/DGS1
* [15]

  Hassan NE, Maddah B. Power approximation for pricing American options, 2026. Int Trans Oper Res. 2024 Jan;33(1), :117–1-42.
* [16]

  Cox, J. C., Ross, S. A. and Rubinstein, M., 1979. Option pricing: a simplified approach.
  Journal of Financial Economics, 7(3), pp.229–263.
* [17]

  Black, F. and Scholes, M., 1973. The pricing of options and corporate liabilities.
  Journal of Political Economy, 81(3), pp.637–654.
* [18]

  Garman, M. B. and Kohlhagen, S. W., 1983. Foreign currency option values.
  Journal of International Money and Finance, 2(3), pp.231–237.