---
authors:
- Hamza Virk
- Yihren Wu
- Majnu John
doc_id: arxiv:2512.15071v1
family_id: arxiv:2512.15071
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Arbitrage-Free Pricing with Diffusion-Dependent Jumps
url_abs: http://arxiv.org/abs/2512.15071v1
url_html: https://arxiv.org/html/2512.15071v1
venue: arXiv q-fin
version: 1
year: 2025
---


Hamza Virk
Hamza Virk: Department of Mathematics, Hofstra University, Hempstead, NY 11549, USA
[hvirk2@pride.hofstra.edu](mailto:hvirk2@pride.hofstra.edu)
, 
Yihren Wu
Yihren Wu: Department of Mathematics, Hofstra University, Hempstead, NY 11549, USA
[yihren.wu@hofstra.edu](mailto:yihren.wu@hofstra.edu)
 and 
Majnu John
Majnu John: Department of Mathematics, Hofstra University, Hempstead, NY 11549, USA
[majnu.john@hofstra.edu](mailto:majnu.john@hofstra.edu)

###### Abstract.

Standard jump-diffusion models assume independence between jumps and diffusion components. We develop a multi-type jump-diffusion model where jump occurrence and magnitude depend on contemporaneous diffusion movements. Unlike previous one-sided models that create arbitrage opportunities, our framework includes upward and downward jumps triggered by both large upward and large downward diffusion increments. We derive the explicit no-arbitrage condition linking the physical drift to model parameters and market risk premia by constructing an Equivalent Martingale Measure using Girsanov’s theorem and a normalized Esscher transform. This condition provides a rigorous foundation for arbitrage-free pricing in models with diffusion-dependent jumps.

###### Key words and phrases:

Jump-Diffusion Process, Path-Dependent Jumps, Arbitrage-Free Pricing, Equivalent Martingale Measure

###### 2010 Mathematics Subject Classification:

Primary 91G30; Secondary 60G44, 46B22

\* Corresponding Author

## 1. Introduction

Soon after the celebrated Black-Scholes asset pricing model [[1](https://arxiv.org/html/2512.15071v1#bib.bib1)], Merton introduced a jump-diffusion model [[7](https://arxiv.org/html/2512.15071v1#bib.bib7)] to deal with stylized facts from market data. In this model, the jumps are assumed independent from the diffusion term. This independence assumption provided a simple enough setting for one to find a risk-neutral measure for the asset price, and Merton was able to produce an analytic solution to the option prices based on this measurement.

Market data suggests that jumps and diffusion processes are not independent. To this end, the authors in [[8](https://arxiv.org/html/2512.15071v1#bib.bib8)] proposed a model in which jumps are triggered by recent market activities. Roughly, when the market drops by a predetermined amount over a certain time window, an upward jump is triggered. The authors refer to this jump-diffusion model as a market recovery model, it consists of only upward jumps to recover the market drop. They were able to compute the risk neutral rate and the resulting option prices are substantially different from the Black-Scholes prices.

In addition to the upward jump following a drop in the market proposed in [[8](https://arxiv.org/html/2512.15071v1#bib.bib8)], there are three other types of jumps. A downward jump following a drop in the market, an upward or downward jump following a rise in the market.
The jumps proposed in [[8](https://arxiv.org/html/2512.15071v1#bib.bib8)] result in behavior commonly referred to as buy-on-the-dip. There are similar phrases to describe the other types of jumps: rush to exit, chasing after the market, and taking profit off the table. In a separate paper, when the market data is analyzed using the hidden Markov model [[6](https://arxiv.org/html/2512.15071v1#bib.bib6)], the distribution of these four types of jumps in various states will be shown to explain the transition of the market between these states.

The purpose of this paper is to present the risk-neutral measure for the jump-diffusion model where all four types of jumps are included.

We achieve this by:

1. (1)

   Formalizing a Multi-Type Jump Model: We extend the previous framework to include four distinct jump scenarios with explicit trigger conditions, state-dependent jump probabilities, and jump size distributions under the physical measure ℙ\mathbb{P}.
2. (2)

   Constructing an Equivalent Martingale Measure (EMM): We leverage the Fundamental Theorem of Asset Pricing [[5](https://arxiv.org/html/2512.15071v1#bib.bib5)] by constructing an EMM ℚ\mathbb{Q} through Girsanov’s theorem [[4](https://arxiv.org/html/2512.15071v1#bib.bib4)] for diffusion and a normalized Esscher transform [[2](https://arxiv.org/html/2512.15071v1#bib.bib2), [3](https://arxiv.org/html/2512.15071v1#bib.bib3)] for state-dependent jumps.
3. (3)

   Deriving the Explicit No-Arbitrage Condition: By enforcing the martingale property under the EMM ℚ\mathbb{Q}, we derive a precise condition relating the physical drift μ\mu to the risk-free rate rr, volatility σ\sigma, jump parameters, and market prices of diffusion and jump risks.

[Section 2](https://arxiv.org/html/2512.15071v1#S2 "2. The Model under the Physical Measure (ℙ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") details the model under the physical measure. [Section 3](https://arxiv.org/html/2512.15071v1#S3 "3. The No-Arbitrage Framework ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") introduces the no-arbitrage framework and change of measure. [Section 4](https://arxiv.org/html/2512.15071v1#S4 "4. The Model under the Risk-Neutral Measure (ℚ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") describes dynamics under the risk-neutral measure. [Section 5](https://arxiv.org/html/2512.15071v1#S5 "5. The No-Arbitrage Condition ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") presents the main no-arbitrage condition with detailed proof. [Section 6](https://arxiv.org/html/2512.15071v1#S6 "6. Discussion ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") discusses implications and [Section 7](https://arxiv.org/html/2512.15071v1#S7 "7. Conclusion ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") concludes.

## 2. The Model under the Physical Measure (ℙ\mathbb{P})

We begin by constructing the asset price model in a discrete-time framework, similar to [[8](https://arxiv.org/html/2512.15071v1#bib.bib8)], under the physical (real-world) probability measure ℙ\mathbb{P}.

### 2.1. Setup and Assumptions

Let (Ω,ℱ,(ℱt)t≥0,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\geq 0},\mathbb{P}) be a filtered probability space, where Ω\Omega is the sample space, ℱ\mathcal{F} is the sigma-algebra of events, ℙ\mathbb{P} is the physical probability measure, and (ℱt)t≥0(\mathcal{F}\_{t})\_{t\geq 0} is a filtration representing the flow of information over time, satisfying the usual conditions (right-continuity and completeness). We consider a discrete set of time points tk=k​τt\_{k}=k\tau, where k∈ℕ0k\in\mathbb{N}\_{0} and τ>0\tau>0 is a small, fixed time interval. For simplicity, we denote tkt\_{k} by tt, for a general kk and the next time step as t+τt+\tau.

We assume the existence of a risk-free asset with its price denoted by BtB\_{t} growing at a constant rate r≥0r\geq 0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bt+τ=Bt​er​τB\_{t+\tau}=B\_{t}e^{r\tau} |  | (2.1) |

Without loss of generality, we set B0=1B\_{0}=1.

The risky asset’s price StS\_{t} is driven by a standard ℙ\mathbb{P}-Brownian motion WtW\_{t}. Its price dynamics over one interval [t,t+τ][t,t+\tau] are given by a jump-diffusion process. Let Xt=ln⁡(St)X\_{t}=\ln(S\_{t}) be the log-price. The change in log-price is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt+τ−Xt=(μ−12​σ2)​τ+σ​Δ​Wt,τ+Jt+τX\_{t+\tau}-X\_{t}=(\mu-\tfrac{1}{2}\sigma^{2})\tau+\sigma\Delta W\_{t,\tau}+J\_{t+\tau} |  | (2.2) |

where:

* •

  μ∈ℝ\mu\in\mathbb{R} is the constant expected rate of return (drift) of the asset StS\_{t}.
* •

  σ>0\sigma>0 is the constant volatility of the diffusion component.
* •

  Δ​Wt,τ=Wt+τ−Wt\Delta W\_{t,\tau}=W\_{t+\tau}-W\_{t} is the increment of the standard Brownian motion over [t,t+τ][t,t+\tau]. Under ℙ\mathbb{P}, given ℱt\mathcal{F}\_{t}, Δ​Wt,τ∼𝒩​(0,τ)\Delta W\_{t,\tau}\sim\mathcal{N}(0,\tau).
* •

  Jt+τJ\_{t+\tau} is the random jump component, whose occurrence and size depend on the realization of Δ​Wt,τ\Delta W\_{t,\tau}.

The asset price StS\_{t} evolves as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | St+τ=St​exp⁡[(μ−12​σ2)​τ+σ​Δ​Wt,τ+Jt+τ]S\_{t+\tau}=S\_{t}\exp\left[(\mu-\tfrac{1}{2}\sigma^{2})\tau+\sigma\Delta W\_{t,\tau}+J\_{t+\tau}\right] |  | (2.3) |

### 2.2. Diffusion-Dependent Jumps

We define the jump component Jt+τJ\_{t+\tau} based on the contemporaneous diffusion increment Δ​W=Δ​Wt,τ\Delta W=\Delta W\_{t,\tau}. We define two thresholds, bd<0b\_{d}<0 and bu>0b\_{u}>0. These thresholds partition the possible outcomes of Δ​W\Delta W into three regions:

* •

  Region 1 (Large Downward Diffusion): Δ​W<bd​τ\Delta W<b\_{d}\sqrt{\tau} (Index j=1j=1)
* •

  Region 2 (Large Upward Diffusion): Δ​W>bu​τ\Delta W>b\_{u}\sqrt{\tau} (Index j=2j=2)
* •

  Region 0 (Normal Diffusion): bd​τ≤Δ​W≤bu​τb\_{d}\sqrt{\tau}\leq\Delta W\leq b\_{u}\sqrt{\tau} (Index j=0j=0)

###### Assumption 2.1 (Jump Structure under ℙ\mathbb{P}).

Let Δ​W=Δ​Wt,τ\Delta W=\Delta W\_{t,\tau}. The jump Jt+τJ\_{t+\tau} is determined as follows:

1. (1)

   If Δ​W\Delta W is in Region j∈{1,2}j\in\{1,2\}:

   * •

     With probability pj​u​(Δ​W)p\_{ju}(\Delta W), an upward jump Jj​uJ\_{ju} occurs, where Jj​u∼𝒩​(νj​u,δj​u2)J\_{ju}\sim\mathcal{N}(\nu\_{ju},\delta\_{ju}^{2}).
   * •

     With probability pj​d​(Δ​W)p\_{jd}(\Delta W), a downward jump Jj​dJ\_{jd} occurs, where Jj​d∼𝒩​(νj​d,δj​d2)J\_{jd}\sim\mathcal{N}(\nu\_{jd},\delta\_{jd}^{2}).
   * •

     With probability pj​0​(Δ​W)=1−pj​u​(Δ​W)−pj​d​(Δ​W)p\_{j0}(\Delta W)=1-p\_{ju}(\Delta W)-p\_{jd}(\Delta W), no jump occurs (Jt+τ=0J\_{t+\tau}=0).
2. (2)

   If Δ​W\Delta W is in Region 0:

   * •

     With probability 11, no jump occurs (Jt+τ=0J\_{t+\tau}=0).

We assume that the jump probabilities pj​k​(Δ​W)p\_{jk}(\Delta W) are nonnegative and sum to 1 within each scenario (i.e., pj​u​(Δ​W)+pj​d​(Δ​W)+pj​0​(Δ​W)=1p\_{ju}(\Delta W)+p\_{jd}(\Delta W)+p\_{j0}(\Delta W)=1 if Δ​W\Delta W is in Region j∈{1,2}j\in\{1,2\}). We also assume that for k=u,d,0k=u,d,0, pj​k​(Δ​W)p\_{jk}(\Delta W) are ℱt+τ\mathcal{F}\_{t+\tau}-measurable. For tractability and clarity in this initial theoretical framework, we assume that pj​k​(Δ​W)=pj​kp\_{jk}(\Delta W)=p\_{jk} (constants within their respective trigger regions), and that the jump parameters νj​k​(Δ​W)=νj​k\nu\_{jk}(\Delta W)=\nu\_{jk} and δj​k​(Δ​W)=δj​k\delta\_{jk}(\Delta W)=\delta\_{jk} are also constants. The framework can be extended to state-dependent parameters, though it would increase complexity. We require δj​k2>0\delta\_{jk}^{2}>0.

###### Assumption 2.2 (Integrability).

For all jump types j=1,2,0,and​k=u,d,0j=1,2,0,\;\mathrm{and}\;k=u,d,0, jump sizes Jj​kJ\_{jk} have finite exponential moments under ℙ\mathbb{P}. That is, 𝔼ℙ​[ec​Jj​k]<∞\mathbb{E}\_{\mathbb{P}}[e^{cJ\_{jk}}]<\infty for any c∈ℝc\in\mathbb{R}. Since we assume Jj​k∼𝒩​(νj​k,δj​k2)J\_{jk}\sim\mathcal{N}(\nu\_{jk},\delta\_{jk}^{2}), this condition is always satisfied, as the Moment Generating Function (MGF) of a Normal distribution exists for all real arguments. This ensures the existence of the Cumulant Generating Function (CGF) and MGF used later.

###### Assumption 2.3 (Temporal Independence).

The increments (Δ​Wt,τ,Jt+τ)(\Delta W\_{t,\tau},J\_{t+\tau}) are independent across time steps t=0,τ,2​τ,…t=0,\tau,2\tau,\dots. That is, the pair (Δ​Wt,τ,Jt+τ)(\Delta W\_{t,\tau},J\_{t+\tau}) (whose structure depends on Δ​Wt,τ\Delta W\_{t,\tau}) is independent of (Δ​Ws,τ,Js+τ)(\Delta W\_{s,\tau},J\_{s+\tau}) for all s<t−τs<t-\tau. This is a simplifying assumption, common in discrete-time models, crucial for constructing the multi-period Radon-Nikodym derivative and applying the Fundamental Theorem of Asset Pricing (FTAP) over the full horizon.

### 2.3. Physical Measure Dynamics Formally Stated

###### Theorem 2.4 (Asset Price Dynamics under ℙ\mathbb{P}).

Let StS\_{t} be the asset price at time tt. Under [2.1](https://arxiv.org/html/2512.15071v1#S2.Thmtheorem1 "Assumption 2.1 (Jump Structure under ℙ). ‣ 2.2. Diffusion-Dependent Jumps ‣ 2. The Model under the Physical Measure (ℙ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"), the asset price at time t+τt+\tau is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | St+τ=St​exp⁡[(μ−12​σ2)​τ+σ​Δ​Wt,τ]×Yt+τS\_{t+\tau}=S\_{t}\exp\left[(\mu-\tfrac{1}{2}\sigma^{2})\tau+\sigma\Delta W\_{t,\tau}\right]\times Y\_{t+\tau} |  | (2.4) |

where Yt+τ=exp⁡(Jt+τ)Y\_{t+\tau}=\exp(J\_{t+\tau}) is the jump size factor, and Jt+τJ\_{t+\tau} is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jt+τ={J1​uwith probability ​p1​u​ if ​Δ​Wt,τ<bd​τJ1​dwith probability ​p1​d​ if ​Δ​Wt,τ<bd​τ0with probability ​p10​ if ​Δ​Wt,τ<bd​τJ2​uwith probability ​p2​u​ if ​Δ​Wt,τ>bu​τJ2​dwith probability ​p2​d​ if ​Δ​Wt,τ>bu​τ0with probability ​p20​ if ​Δ​Wt,τ>bu​τ0with probability ​1​ if ​bd​τ≤Δ​Wt,τ≤bu​τ\displaystyle J\_{t+\tau}=\begin{cases}J\_{1u}&\text{with probability }p\_{1u}\text{ if }\Delta W\_{t,\tau}<b\_{d}\sqrt{\tau}\\ J\_{1d}&\text{with probability }p\_{1d}\text{ if }\Delta W\_{t,\tau}<b\_{d}\sqrt{\tau}\\ 0&\text{with probability }p\_{10}\text{ if }\Delta W\_{t,\tau}<b\_{d}\sqrt{\tau}\\ J\_{2u}&\text{with probability }p\_{2u}\text{ if }\Delta W\_{t,\tau}>b\_{u}\sqrt{\tau}\\ J\_{2d}&\text{with probability }p\_{2d}\text{ if }\Delta W\_{t,\tau}>b\_{u}\sqrt{\tau}\\ 0&\text{with probability }p\_{20}\text{ if }\Delta W\_{t,\tau}>b\_{u}\sqrt{\tau}\\ 0&\text{with probability }1\text{ if }b\_{d}\sqrt{\tau}\leq\Delta W\_{t,\tau}\leq b\_{u}\sqrt{\tau}\end{cases} |  | (2.5) |

The jumps Jj​k∼𝒩​(νj​k,δj​k2)J\_{jk}\sim\mathcal{N}(\nu\_{jk},\delta\_{jk}^{2}) are drawn independently of other randomness, conditional on being in the specified region and the specific jump type occurring.

###### Proof.

This follows directly by exponentiating the log-price dynamics Xt+τ−XtX\_{t+\tau}-X\_{t} from [Eq. 2.2](https://arxiv.org/html/2512.15071v1#S2.E2 "In 2.1. Setup and Assumptions ‣ 2. The Model under the Physical Measure (ℙ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | St+τ\displaystyle S\_{t+\tau} | =St​exp⁡(Xt+τ−Xt)\displaystyle=S\_{t}\exp(X\_{t+\tau}-X\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =St​exp⁡((μ−12​σ2)​τ+σ​Δ​Wt,τ+Jt+τ)\displaystyle=S\_{t}\exp\left((\mu-\tfrac{1}{2}\sigma^{2})\tau+\sigma\Delta W\_{t,\tau}+J\_{t+\tau}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =St​exp⁡((μ−12​σ2)​τ+σ​Δ​Wt,τ)​exp⁡(Jt+τ)\displaystyle=S\_{t}\exp\left((\mu-\tfrac{1}{2}\sigma^{2})\tau+\sigma\Delta W\_{t,\tau}\right)\exp(J\_{t+\tau}) |  | (2.6) |

We identify Yt+τ=exp⁡(Jt+τ)Y\_{t+\tau}=\exp(J\_{t+\tau}). The probabilistic structure of Jt+τJ\_{t+\tau} is explicitly given by [2.1](https://arxiv.org/html/2512.15071v1#S2.Thmtheorem1 "Assumption 2.1 (Jump Structure under ℙ). ‣ 2.2. Diffusion-Dependent Jumps ‣ 2. The Model under the Physical Measure (ℙ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") for constant probabilities pj​kp\_{jk}.
∎

## 3. The No-Arbitrage Framework

To ensure our model is economically viable, we must impose conditions that prevent arbitrage opportunities. The cornerstone of this is the Fundamental Theorem of Asset Pricing (FTAP).

### 3.1. The Fundamental Theorem of Asset Pricing (FTAP)

###### Theorem 3.1 (FTAP for Discrete Time - [[5](https://arxiv.org/html/2512.15071v1#bib.bib5)]).

In a discrete-time financial market model with a finite number of assets and time periods, satisfying certain conditions (like the absence of redundant assets, which our single risky asset model satisfies), the condition of No Arbitrage (NA) is equivalent to the existence of a probability measure ℚ\mathbb{Q}, which is equivalent to the physical measure ℙ\mathbb{P} (i.e., ℙ​(A)=0⇔ℚ​(A)=0\mathbb{P}(A)=0\iff\mathbb{Q}(A)=0 for all A∈ℱA\in\mathcal{F}), such that the discounted prices of all traded assets are martingales under ℚ\mathbb{Q}.

For our model with one risky asset StS\_{t} and a risk-free asset BtB\_{t}, this implies there exists an EMM ℚ∼ℙ\mathbb{Q}\sim\mathbb{P} such that the discounted price process Std​i​s​c=St/Bt=St​e−r​tS\_{t}^{disc}=S\_{t}/B\_{t}=S\_{t}e^{-rt} is a ℚ\mathbb{Q}-martingale:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​[St+τd​i​s​c|ℱt]=Std​i​s​c\mathbb{E}\_{\mathbb{Q}}\left[S\_{t+\tau}^{disc}|\mathcal{F}\_{t}\right]=S\_{t}^{disc} |  | (3.1) |

which is equivalent to stating that the expected return under ℚ\mathbb{Q} is the risk-free rate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​[St+τSt|ℱt]=er​τ\mathbb{E}\_{\mathbb{Q}}\left[\frac{S\_{t+\tau}}{S\_{t}}\bigg|\mathcal{F}\_{t}\right]=e^{r\tau} |  | (3.2) |

### 3.2. Constructing the Equivalent Martingale Measure (ℚ\mathbb{Q})

To find ℚ\mathbb{Q}, we define its Radon-Nikodym derivative with respect to ℙ\mathbb{P}. Due to our temporal independence assumption ([2.3](https://arxiv.org/html/2512.15071v1#S2.Thmtheorem3 "Assumption 2.3 (Temporal Independence). ‣ 2.2. Diffusion-Dependent Jumps ‣ 2. The Model under the Physical Measure (ℙ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps")), the multi-period Radon-Nikodym derivative LT=d​ℚd​ℙ|ℱTL\_{T}=\left.\frac{\,\mathrm{d}\mathbb{Q}}{\,\mathrm{d}\mathbb{P}}\right|\_{\mathcal{F}\_{T}} can be constructed as a product of one-step kernels LτL\_{\tau}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lt=∏k=0t/τ−1Lk​τ​(Δ​Wk​τ,τ,J(k+1)​τ)L\_{t}=\prod\_{k=0}^{t/\tau-1}L\_{k\tau}(\Delta W\_{k\tau,\tau},J\_{(k+1)\tau}) |  | (3.3) |

The one-step kernel LτL\_{\tau} (which we denote as Lτ​(Δ​W,J)L\_{\tau}(\Delta W,J) omitting tt for brevity when referring to a generic step) changes the measure for both diffusion and jump risks.

###### Definition 3.2 (Cumulant Generating Function & Normalizers).

Let ηj​k\eta\_{jk} be the (constant) market price of risk associated with jump type indexed j​kjk.
The Cumulant Generating Function (CGF) for Jj​k∼𝒩​(νj​k,δj​k2)J\_{jk}\sim\mathcal{N}(\nu\_{jk},\delta\_{jk}^{2}) is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | κj​k​(η)=ln⁡𝔼ℙ​[eη​Jj​k]=η​νj​k+12​η2​δj​k2\kappa\_{jk}(\eta)=\ln\mathbb{E}\_{\mathbb{P}}[e^{\eta J\_{jk}}]=\eta\nu\_{jk}+\tfrac{1}{2}\eta^{2}\delta\_{jk}^{2} |  | (3.4) |

This exists because Jj​kJ\_{jk} is Normally distributed ([2.2](https://arxiv.org/html/2512.15071v1#S2.Thmtheorem2 "Assumption 2.2 (Integrability). ‣ 2.2. Diffusion-Dependent Jumps ‣ 2. The Model under the Physical Measure (ℙ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps")).
We define region-specific normalizers Zj​(Δ​W)Z\_{j}(\Delta W). Given our assumption of constant pj​kp\_{jk}, these become constants ZjZ\_{j}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Z1\displaystyle Z\_{1} | =p1​u​eκ1​u​(η1​u)+p1​d​eκ1​d​(η1​d)+p10\displaystyle=p\_{1u}e^{\kappa\_{1u}(\eta\_{1u})}+p\_{1d}e^{\kappa\_{1d}(\eta\_{1d})}+p\_{10} |  | (3.5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Z2\displaystyle Z\_{2} | =p2​u​eκ2​u​(η2​u)+p2​d​eκ2​d​(η2​d)+p20\displaystyle=p\_{2u}e^{\kappa\_{2u}(\eta\_{2u})}+p\_{2d}e^{\kappa\_{2d}(\eta\_{2d})}+p\_{20} |  | (3.6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Z0\displaystyle Z\_{0} | =1\displaystyle=1 |  | (3.7) |

We define Z​(Δ​W)=ZjZ(\Delta W)=Z\_{j} if Δ​W\Delta W is in Region jj. This Z​(Δ​W)Z(\Delta W) represents the expected value of the unnormalized Esscher kernel for jumps within each region, conditional on Δ​W\Delta W being in that region, under ℙ\mathbb{P}.

###### Definition 3.3 (Radon-Nikodym Derivative LτL\_{\tau}).

Let Δ​W=Δ​Wt,τ\Delta W=\Delta W\_{t,\tau} and J=Jt+τJ=J\_{t+\tau}. Let γD\gamma\_{D} be the market price of diffusion risk. The one-step Radon-Nikodym derivative kernel Lτ​(Δ​W,J)L\_{\tau}(\Delta W,J) is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lτ​(Δ​W,J)=exp⁡(−γD​σ​Δ​W−12​(γD​σ)2​τ)⏟LD​(Δ​W)×Ψ​(J,Δ​W)⏟Jump KernelL\_{\tau}(\Delta W,J)=\underbrace{\exp\left(-\gamma\_{D}\sigma\Delta W-\frac{1}{2}(\gamma\_{D}\sigma)^{2}\tau\right)}\_{L\_{D}(\Delta W)}\times\underbrace{\Psi(J,\Delta W)}\_{\text{Jump Kernel}} |  | (3.8) |

where LD​(Δ​W)L\_{D}(\Delta W) is the Girsanov kernel for diffusion, and Ψ​(J,Δ​W)\Psi(J,\Delta W) is the normalized Esscher kernel for jumps:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψ​(J,Δ​W)=1Z​(Δ​W)×{eηj​k​Jif jump ​Jj​k​ occurs in Region ​j1if no jump occurs (in Region j or 0)\Psi(J,\Delta W)=\frac{1}{Z(\Delta W)}\times\begin{cases}e^{\eta\_{jk}J}&\text{if jump }J\_{jk}\text{ occurs in Region }j\\ 1&\text{if no jump occurs (in Region $j$ or $0$)}\end{cases} |  | (3.9) |

More explicitly, if Δ​W\Delta W is in Region j∈{1,2}j\in\{1,2\}:

* •

  If jump Jj​uJ\_{ju} occurs, Ψ​(Jj​u,Δ​W)=eηj​u​Jj​uZj\Psi(J\_{ju},\Delta W)=\frac{e^{\eta\_{ju}J\_{ju}}}{Z\_{j}}.
* •

  If jump Jj​dJ\_{jd} occurs, Ψ​(Jj​d,Δ​W)=eηj​d​Jj​dZj\Psi(J\_{jd},\Delta W)=\frac{e^{\eta\_{jd}J\_{jd}}}{Z\_{j}}.
* •

  If no jump occurs, Ψ​(0,Δ​W)=1Zj\Psi(0,\Delta W)=\frac{1}{Z\_{j}}.

If Δ​W\Delta W is in Region 0, Z​(Δ​W)=Z0=1Z(\Delta W)=Z\_{0}=1, and no jump occurs (J=0J=0), so Ψ​(0,Δ​W)=11×1=1\Psi(0,\Delta W)=\frac{1}{1}\times 1=1.

###### Lemma 3.4 (Validity of LτL\_{\tau}).

The Radon-Nikodym derivative LτL\_{\tau} defined in [Definition 3.3](https://arxiv.org/html/2512.15071v1#S3.Thmtheorem3 "Definition 3.3 (Radon-Nikodym Derivative 𝐿_𝜏). ‣ 3.2. Constructing the Equivalent Martingale Measure (ℚ) ‣ 3. The No-Arbitrage Framework ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") satisfies 𝔼ℙ​[Lτ|ℱt]=1\mathbb{E}\_{\mathbb{P}}[L\_{\tau}|\mathcal{F}\_{t}]=1.

###### Proof.

Since the structure of LτL\_{\tau} depends only on Δ​Wt,τ\Delta W\_{t,\tau} and Jt+τJ\_{t+\tau}, which are independent of ℱt\mathcal{F}\_{t} by [2.3](https://arxiv.org/html/2512.15071v1#S2.Thmtheorem3 "Assumption 2.3 (Temporal Independence). ‣ 2.2. Diffusion-Dependent Jumps ‣ 2. The Model under the Physical Measure (ℙ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") (given parameters), 𝔼ℙ​[Lτ|ℱt]=𝔼ℙ​[Lτ]\mathbb{E}\_{\mathbb{P}}[L\_{\tau}|\mathcal{F}\_{t}]=\mathbb{E}\_{\mathbb{P}}[L\_{\tau}]. We use the Law of Total Expectation by conditioning on Δ​W=x\Delta W=x:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[Lτ]=𝔼ℙ​[𝔼ℙ​[Lτ|Δ​W]]=∫−∞∞𝔼ℙ​[Lτ|Δ​W=x]​fℙ​(x)​dx\mathbb{E}\_{\mathbb{P}}[L\_{\tau}]=\mathbb{E}\_{\mathbb{P}}\left[\mathbb{E}\_{\mathbb{P}}[L\_{\tau}|\Delta W]\right]=\int\_{-\infty}^{\infty}\mathbb{E}\_{\mathbb{P}}[L\_{\tau}|\Delta W=x]f\_{\mathbb{P}}(x)\,\mathrm{d}x |  | (3.10) |

where fℙ​(x)f\_{\mathbb{P}}(x) is the PDF of 𝒩​(0,τ)\mathcal{N}(0,\tau). First, we calculate the inner conditional expectation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[Lτ|Δ​W=x]=𝔼ℙ​[LD​(x)​Ψ​(J,x)|Δ​W=x]\mathbb{E}\_{\mathbb{P}}[L\_{\tau}|\Delta W=x]=\mathbb{E}\_{\mathbb{P}}[L\_{D}(x)\Psi(J,x)|\Delta W=x] |  | (3.11) |

Since LD​(x)L\_{D}(x) depends only on xx, it can be factored out of the conditional expectation over JJ:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[Lτ|Δ​W=x]=LD​(x)​𝔼ℙ​[Ψ​(J,x)|Δ​W=x]\mathbb{E}\_{\mathbb{P}}[L\_{\tau}|\Delta W=x]=L\_{D}(x)\mathbb{E}\_{\mathbb{P}}[\Psi(J,x)|\Delta W=x] |  | (3.12) |

Now we calculate 𝔼ℙ​[Ψ​(J,x)|Δ​W=x]\mathbb{E}\_{\mathbb{P}}[\Psi(J,x)|\Delta W=x]. We consider the three regions for xx:

* •

  If x<bd​τx<b\_{d}\sqrt{\tau} (Region 1): Here Z​(x)=Z1Z(x)=Z\_{1}.

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | 𝔼ℙ​[Ψ​(J,x)|x]\displaystyle\mathbb{E}\_{\mathbb{P}}[\Psi(J,x)|x] | =p1​u​𝔼ℙ​[eη1​u​J1​uZ1|x]+p1​d​𝔼ℙ​[eη1​d​J1​dZ1|x]+p10​𝔼ℙ​[1Z1|x]\displaystyle=p\_{1u}\mathbb{E}\_{\mathbb{P}}\left[\frac{e^{\eta\_{1u}J\_{1u}}}{Z\_{1}}\bigg|x\right]+p\_{1d}\mathbb{E}\_{\mathbb{P}}\left[\frac{e^{\eta\_{1d}J\_{1d}}}{Z\_{1}}\bigg|x\right]+p\_{10}\mathbb{E}\_{\mathbb{P}}\left[\frac{1}{Z\_{1}}\bigg|x\right] |  | (3.13) |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  |  | =1Z1​(p1​u​𝔼ℙ​[eη1​u​J1​u]+p1​d​𝔼ℙ​[eη1​d​J1​d]+p10⋅1)\displaystyle=\frac{1}{Z\_{1}}\left(p\_{1u}\mathbb{E}\_{\mathbb{P}}[e^{\eta\_{1u}J\_{1u}}]+p\_{1d}\mathbb{E}\_{\mathbb{P}}[e^{\eta\_{1d}J\_{1d}}]+p\_{10}\cdot 1\right) |  | (3.14) |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  |  | =1Z1​(p1​u​eκ1​u​(η1​u)+p1​d​eκ1​d​(η1​d)+p10)\displaystyle=\frac{1}{Z\_{1}}\left(p\_{1u}e^{\kappa\_{1u}(\eta\_{1u})}+p\_{1d}e^{\kappa\_{1d}(\eta\_{1d})}+p\_{10}\right) |  | (3.15) |
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  |  | =Z1Z1=1(using [Eq. 3.5](https://arxiv.org/html/2512.15071v1#S3.E5 "In Definition 3.2 (Cumulant Generating Function & Normalizers). ‣ 3.2. Constructing the Equivalent Martingale Measure (ℚ) ‣ 3. The No-Arbitrage Framework ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"))\displaystyle=\frac{Z\_{1}}{Z\_{1}}=1\quad\text{(using \lx@cref{creftype~refnum}{eq:Z1\_def})} |  | (3.16) |

  In [Eq. 3.14](https://arxiv.org/html/2512.15071v1#S3.E14 "In 1st item ‣ 3.2. Constructing the Equivalent Martingale Measure (ℚ) ‣ 3. The No-Arbitrage Framework ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"), we use the linearity of expectation and that Jj​kJ\_{jk} is independent of the specific value of xx once we are in Region 1. In [Eq. 3.15](https://arxiv.org/html/2512.15071v1#S3.E15 "In 1st item ‣ 3.2. Constructing the Equivalent Martingale Measure (ℚ) ‣ 3. The No-Arbitrage Framework ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"), we use the definition of the CGF κj​k​(ηj​k)=ln⁡𝔼ℙ​[eηj​k​Jj​k]\kappa\_{jk}(\eta\_{jk})=\ln\mathbb{E}\_{\mathbb{P}}[e^{\eta\_{jk}J\_{jk}}], so 𝔼ℙ​[eηj​k​Jj​k]=eκj​k​(ηj​k)\mathbb{E}\_{\mathbb{P}}[e^{\eta\_{jk}J\_{jk}}]=e^{\kappa\_{jk}(\eta\_{jk})}.
* •

  If x>bu​τx>b\_{u}\sqrt{\tau} (Region 2): By an identical argument, using Z2Z\_{2} and p2​kp\_{2k}, we find 𝔼ℙ​[Ψ​(J,x)|x]=1\mathbb{E}\_{\mathbb{P}}[\Psi(J,x)|x]=1.
* •

  If bd​τ≤x≤bu​τb\_{d}\sqrt{\tau}\leq x\leq b\_{u}\sqrt{\tau} (Region 0): Here Z​(x)=Z0=1Z(x)=Z\_{0}=1. No jump occurs (J=0J=0), so by [Eq. 3.9](https://arxiv.org/html/2512.15071v1#S3.E9 "In Definition 3.3 (Radon-Nikodym Derivative 𝐿_𝜏). ‣ 3.2. Constructing the Equivalent Martingale Measure (ℚ) ‣ 3. The No-Arbitrage Framework ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"), Ψ​(0,x)=11×1=1\Psi(0,x)=\frac{1}{1}\times 1=1. Thus, 𝔼ℙ​[Ψ​(J,x)|x]=1\mathbb{E}\_{\mathbb{P}}[\Psi(J,x)|x]=1.

Since 𝔼ℙ​[Ψ​(J,Δ​W)|Δ​W]=1\mathbb{E}\_{\mathbb{P}}[\Psi(J,\Delta W)|\Delta W]=1 for all possible values of Δ​W\Delta W, the full expectation becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[Lτ]=𝔼ℙ​[LD​(Δ​W)×1]=𝔼ℙ​[exp⁡(−γD​σ​Δ​W−12​(γD​σ)2​τ)]\mathbb{E}\_{\mathbb{P}}[L\_{\tau}]=\mathbb{E}\_{\mathbb{P}}[L\_{D}(\Delta W)\times 1]=\mathbb{E}\_{\mathbb{P}}\left[\exp\left(-\gamma\_{D}\sigma\Delta W-\frac{1}{2}(\gamma\_{D}\sigma)^{2}\tau\right)\right] |  | (3.17) |

Let A=−γD​σA=-\gamma\_{D}\sigma. Then we are calculating 𝔼ℙ​[eA​Δ​W−12​A2​τ]\mathbb{E}\_{\mathbb{P}}\left[e^{A\Delta W-\frac{1}{2}A^{2}\tau}\right]. Since Δ​W∼𝒩​(0,τ)\Delta W\sim\mathcal{N}(0,\tau), A​Δ​W∼𝒩​(0,A2​τ)A\Delta W\sim\mathcal{N}(0,A^{2}\tau). The MGF of Δ​W\Delta W is MΔ​W​(s)=𝔼ℙ​[es​Δ​W]=es2​τ/2M\_{\Delta W}(s)=\mathbb{E}\_{\mathbb{P}}\left[e^{s\Delta W}\right]=e^{s^{2}\tau/2}.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼ℙ​[Lτ]\displaystyle\mathbb{E}\_{\mathbb{P}}[L\_{\tau}] | =e−12​(γD​σ)2​τ​𝔼ℙ​[e−γD​σ​Δ​W]\displaystyle=e^{-\frac{1}{2}(\gamma\_{D}\sigma)^{2}\tau}\mathbb{E}\_{\mathbb{P}}\left[e^{-\gamma\_{D}\sigma\Delta W}\right] |  | (3.18) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =e−12​(γD​σ)2​τ​MΔ​W​(−γD​σ)\displaystyle=e^{-\frac{1}{2}(\gamma\_{D}\sigma)^{2}\tau}M\_{\Delta W}(-\gamma\_{D}\sigma) |  | (3.19) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =e−12​(γD​σ)2​τ​exp⁡((−γD​σ)2​τ2)\displaystyle=e^{-\frac{1}{2}(\gamma\_{D}\sigma)^{2}\tau}\exp\left(\frac{(-\gamma\_{D}\sigma)^{2}\tau}{2}\right) |  | (3.20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =e−12​(γD​σ)2​τ​exp⁡(γD2​σ2​τ2)=e0=1\displaystyle=e^{-\frac{1}{2}(\gamma\_{D}\sigma)^{2}\tau}\exp\left(\frac{\gamma\_{D}^{2}\sigma^{2}\tau}{2}\right)=e^{0}=1 |  | (3.21) |

Thus, LτL\_{\tau} is a valid one-step Radon-Nikodym density.
∎

## 4. The Model under the Risk-Neutral Measure (ℚ\mathbb{Q})

Using LτL\_{\tau}, we find the dynamics under the risk-neutral measure ℚ\mathbb{Q}.

### 4.1. Diffusion under ℚ\mathbb{Q}

###### Proposition 4.1 (Diffusion under ℚ\mathbb{Q}).

Under the measure ℚ\mathbb{Q} defined by LτL\_{\tau}, the process Wtℚ=Wt+γD​σ​tW\_{t}^{\mathbb{Q}}=W\_{t}+\gamma\_{D}\sigma t is a standard ℚ\mathbb{Q}-Brownian motion. Consequently, the original increment Δ​Wt,τ\Delta W\_{t,\tau} has the following distribution under ℚ\mathbb{Q}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Wt,τ∼𝒩​(−γD​σ​τ,τ)\Delta W\_{t,\tau}\sim\mathcal{N}(-\gamma\_{D}\sigma\tau,\tau) |  | (4.1) |

###### Proof.

This is a standard result from Girsanov’s theorem. We explicitly calculate the mean of Δ​Wt,τ\Delta W\_{t,\tau} under ℚ\mathbb{Q}. For any random variable XX, 𝔼ℚ​[X]=𝔼ℙ​[Lτ​X]\mathbb{E}\_{\mathbb{Q}}[X]=\mathbb{E}\_{\mathbb{P}}[L\_{\tau}X].

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼ℚ​[Δ​Wt,τ]\displaystyle\mathbb{E}\_{\mathbb{Q}}[\Delta W\_{t,\tau}] | =𝔼ℙ​[Lτ​Δ​Wt,τ]\displaystyle=\mathbb{E}\_{\mathbb{P}}[L\_{\tau}\Delta W\_{t,\tau}] |  | (4.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼ℙ​[LD​(Δ​Wt,τ)​Ψ​(J,Δ​Wt,τ)​Δ​Wt,τ]\displaystyle=\mathbb{E}\_{\mathbb{P}}\left[L\_{D}(\Delta W\_{t,\tau})\Psi(J,\Delta W\_{t,\tau})\Delta W\_{t,\tau}\right] |  | (4.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼ℙ​[Δ​Wt,τ​LD​(Δ​Wt,τ)​𝔼ℙ​[Ψ​(J,Δ​Wt,τ)|Δ​Wt,τ]]\displaystyle=\mathbb{E}\_{\mathbb{P}}\left[\Delta W\_{t,\tau}L\_{D}(\Delta W\_{t,\tau})\mathbb{E}\_{\mathbb{P}}[\Psi(J,\Delta W\_{t,\tau})|\Delta W\_{t,\tau}]\right] |  | (4.4) |

which is the Law of Total Expectation. As shown in the proof of [Lemma 3.4](https://arxiv.org/html/2512.15071v1#S3.Thmtheorem4 "Lemma 3.4 (Validity of 𝐿_𝜏). ‣ 3.2. Constructing the Equivalent Martingale Measure (ℚ) ‣ 3. The No-Arbitrage Framework ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"), 𝔼ℙ​[Ψ​(J,Δ​Wt,τ)|Δ​Wt,τ]=1\mathbb{E}\_{\mathbb{P}}[\Psi(J,\Delta W\_{t,\tau})|\Delta W\_{t,\tau}]=1.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼ℚ​[Δ​Wt,τ]\displaystyle\mathbb{E}\_{\mathbb{Q}}[\Delta W\_{t,\tau}] | =𝔼ℙ​[Δ​Wt,τ​LD​(Δ​Wt,τ)]\displaystyle=\mathbb{E}\_{\mathbb{P}}\left[\Delta W\_{t,\tau}L\_{D}(\Delta W\_{t,\tau})\right] |  | (4.5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼ℙ​[Δ​Wt,τ​exp⁡(−γD​σ​Δ​Wt,τ−12​(γD​σ)2​τ)]\displaystyle=\mathbb{E}\_{\mathbb{P}}\left[\Delta W\_{t,\tau}\exp\left(-\gamma\_{D}\sigma\Delta W\_{t,\tau}-\frac{1}{2}(\gamma\_{D}\sigma)^{2}\tau\right)\right] |  | (4.6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫−∞∞x​exp⁡(−γD​σ​x−12​(γD​σ)2​τ)​12​π​τ​exp⁡(−x22​τ)​dx\displaystyle=\int\_{-\infty}^{\infty}x\exp\left(-\gamma\_{D}\sigma x-\frac{1}{2}(\gamma\_{D}\sigma)^{2}\tau\right)\frac{1}{\sqrt{2\pi\tau}}\exp\left(-\frac{x^{2}}{2\tau}\right)\,\mathrm{d}x |  | (4.7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =12​π​τ​exp⁡(−12​(γD​σ)2​τ)​∫−∞∞x​exp⁡(−x2+2​γD​σ​τ​x2​τ)​dx\displaystyle=\frac{1}{\sqrt{2\pi\tau}}\exp\left(-\frac{1}{2}(\gamma\_{D}\sigma)^{2}\tau\right)\int\_{-\infty}^{\infty}x\exp\left(-\frac{x^{2}+2\gamma\_{D}\sigma\tau x}{2\tau}\right)\,\mathrm{d}x |  | (4.8) |

To evaluate the integral, we complete the square in the exponent: x2+2​γD​σ​τ​x=(x+γD​σ​τ)2−(γD​σ​τ)2x^{2}+2\gamma\_{D}\sigma\tau x=(x+\gamma\_{D}\sigma\tau)^{2}-(\gamma\_{D}\sigma\tau)^{2} and simplify:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​[Δ​Wt,τ]=12​π​τ​exp⁡(−12​(γD​σ)2​τ)×∫−∞∞x​exp⁡(−(x+γD​σ​τ)2−(γD​σ​τ)22​τ)​dx=12​π​τ​∫−∞∞x​exp⁡(−(x+γD​σ​τ)22​τ)​dx\begin{split}\mathbb{E}\_{\mathbb{Q}}[\Delta W\_{t,\tau}]&=\frac{1}{\sqrt{2\pi\tau}}\exp\left(-\frac{1}{2}(\gamma\_{D}\sigma)^{2}\tau\right)\quad\times\\ &\qquad\qquad\int\_{-\infty}^{\infty}x\exp\left(-\frac{(x+\gamma\_{D}\sigma\tau)^{2}-(\gamma\_{D}\sigma\tau)^{2}}{2\tau}\right)\,\mathrm{d}x\\ &=\frac{1}{\sqrt{2\pi\tau}}\int\_{-\infty}^{\infty}x\exp\left(-\frac{(x+\gamma\_{D}\sigma\tau)^{2}}{2\tau}\right)\,\mathrm{d}x\end{split} |  | (4.9) |

Let y=x+γD​σ​τy=x+\gamma\_{D}\sigma\tau. Then x=y−γD​σ​τx=y-\gamma\_{D}\sigma\tau, and d​x=d​y\,\mathrm{d}x=\,\mathrm{d}y. The limits of integration remain (−∞,∞)(-\infty,\infty).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼ℚ​[Δ​Wt,τ]\displaystyle\mathbb{E}\_{\mathbb{Q}}[\Delta W\_{t,\tau}] | =12​π​τ​∫−∞∞(y−γD​σ​τ)​exp⁡(−y22​τ)​dy\displaystyle=\frac{1}{\sqrt{2\pi\tau}}\int\_{-\infty}^{\infty}(y-\gamma\_{D}\sigma\tau)\exp\left(-\frac{y^{2}}{2\tau}\right)\,\mathrm{d}y |  | (4.10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =12​π​τ​[∫−∞∞y​exp⁡(−y22​τ)​dy−γD​σ​τ​∫−∞∞exp⁡(−y22​τ)​dy]\displaystyle=\frac{1}{\sqrt{2\pi\tau}}\left[\int\_{-\infty}^{\infty}y\exp\left(-\frac{y^{2}}{2\tau}\right)\,\mathrm{d}y-\gamma\_{D}\sigma\tau\int\_{-\infty}^{\infty}\exp\left(-\frac{y^{2}}{2\tau}\right)\,\mathrm{d}y\right] |  | (4.11) |

The first integral ∫−∞∞y​exp⁡(−y22​τ)​dy=0\int\_{-\infty}^{\infty}y\exp\left(-\frac{y^{2}}{2\tau}\right)\,\mathrm{d}y=0 because the integrand is an odd function (yy is odd, exp⁡(−y2/(2​τ))\exp(-y^{2}/(2\tau)) is even).
The second integral ∫−∞∞exp⁡(−y22​τ)​dy=2​π​τ\int\_{-\infty}^{\infty}\exp\left(-\frac{y^{2}}{2\tau}\right)\,\mathrm{d}y=\sqrt{2\pi\tau} (this is the integral of the kernel of a Normal PDF N​(0,τ)N(0,\tau)).

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​[Δ​Wt,τ]=12​π​τ​[0−γD​σ​τ​2​π​τ]=−γD​σ​τ\mathbb{E}\_{\mathbb{Q}}[\Delta W\_{t,\tau}]=\frac{1}{\sqrt{2\pi\tau}}[0-\gamma\_{D}\sigma\tau\sqrt{2\pi\tau}]=-\gamma\_{D}\sigma\tau |  | (4.12) |

The variance calculation Varℚ​(Δ​Wt,τ)=𝔼ℚ​[(Δ​Wt,τ)2]−(𝔼ℚ​[Δ​Wt,τ])2\mathrm{Var}\_{\mathbb{Q}}(\Delta W\_{t,\tau})=\mathbb{E}\_{\mathbb{Q}}[(\Delta W\_{t,\tau})^{2}]-(\mathbb{E}\_{\mathbb{Q}}[\Delta W\_{t,\tau}])^{2} would similarly show that Varℚ​(Δ​Wt,τ)=τ\mathrm{Var}\_{\mathbb{Q}}(\Delta W\_{t,\tau})=\tau.
Thus, under ℚ\mathbb{Q}, Δ​Wt,τ∼𝒩​(−γD​σ​τ,τ)\Delta W\_{t,\tau}\sim\mathcal{N}(-\gamma\_{D}\sigma\tau,\tau).
The statement Wtℚ=Wt+γD​σ​tW\_{t}^{\mathbb{Q}}=W\_{t}+\gamma\_{D}\sigma t being a ℚ\mathbb{Q}-Brownian motion is the standard Girsanov theorem statement for this drift change.
∎

### 4.2. Jumps under ℚ\mathbb{Q}

###### Proposition 4.2 (Jumps under ℚ\mathbb{Q}).

Under the measure ℚ\mathbb{Q}, the jump probabilities qj​k​(Δ​W)q\_{jk}(\Delta W) and jump size distributions Jj​kℚJ\_{jk}^{\mathbb{Q}} are given as follows, conditional on Δ​W=x\Delta W=x:

1. (1)

   Probabilities: Let ZjZ\_{j} be the normalizer for Region jj from [Definition 3.2](https://arxiv.org/html/2512.15071v1#S3.Thmtheorem2 "Definition 3.2 (Cumulant Generating Function & Normalizers). ‣ 3.2. Constructing the Equivalent Martingale Measure (ℚ) ‣ 3. The No-Arbitrage Framework ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps").

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | qj​u​(x)\displaystyle q\_{ju}(x) | =pj​u​eκj​u​(ηj​u)Zj(if ​Δ​W=x​ in Region ​j)\displaystyle=\frac{p\_{ju}e^{\kappa\_{ju}(\eta\_{ju})}}{Z\_{j}}\quad(\text{if }\Delta W=x\text{ in Region }j) |  | (4.13) |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | qj​d​(x)\displaystyle q\_{jd}(x) | =pj​d​eκj​d​(ηj​d)Zj(if ​Δ​W=x​ in Region ​j)\displaystyle=\frac{p\_{jd}e^{\kappa\_{jd}(\eta\_{jd})}}{Z\_{j}}\quad(\text{if }\Delta W=x\text{ in Region }j) |  | (4.14) |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | qj​0​(x)\displaystyle q\_{j0}(x) | =pj​0Zj(if ​Δ​W=x​ in Region ​j​ and no jump specified by Esscher)\displaystyle=\frac{p\_{j0}}{Z\_{j}}\quad(\text{if }\Delta W=x\text{ in Region }j\text{ and no jump specified by Esscher}) |  | (4.15) |

   For Region 0 (where j=0j=0), Z0=1Z\_{0}=1, p00=1p\_{00}=1, so q00​(x)=1q\_{00}(x)=1. These qj​k​(x)q\_{jk}(x) are the risk-neutral probabilities.
2. (2)

   Distributions: The log-jump size Jj​kℚJ\_{jk}^{\mathbb{Q}} under ℚ\mathbb{Q}, given that a jump of type j​kjk occurs, is:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Jj​kℚ∼𝒩​(νj​k+ηj​k​δj​k2,δj​k2)≡𝒩​(νj​kℚ,δj​k2)J\_{jk}^{\mathbb{Q}}\sim\mathcal{N}(\nu\_{jk}+\eta\_{jk}\delta\_{jk}^{2},\delta\_{jk}^{2})\equiv\mathcal{N}(\nu\_{jk}^{\mathbb{Q}},\delta\_{jk}^{2}) |  | (4.16) |

   where νj​kℚ=νj​k+ηj​k​δj​k2\nu\_{jk}^{\mathbb{Q}}=\nu\_{jk}+\eta\_{jk}\delta\_{jk}^{2}.

###### Proof.

1. Probabilities qj​k​(x)q\_{jk}(x):
The probability of a specific jump Jj​kJ\_{jk} occurring, conditional on Δ​W=x\Delta W=x, under ℚ\mathbb{Q} is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qj​k​(x)=ℚ​(J=Jj​k|Δ​W=x)=ℚ​(J=Jj​k​ and ​Δ​W∈d​x)ℚ​(Δ​W∈d​x)q\_{jk}(x)=\mathbb{Q}(J=J\_{jk}|\Delta W=x)=\frac{\mathbb{Q}(J=J\_{jk}\text{ and }\Delta W\in dx)}{\mathbb{Q}(\Delta W\in dx)} |  | (4.17) |

The numerator: ℚ​(J=Jj​k​ and ​Δ​W∈d​x)=𝔼ℙ​[Lτ​𝟏J=Jj​k,Δ​W∈d​x]\mathbb{Q}(J=J\_{jk}\text{ and }\Delta W\in dx)=\mathbb{E}\_{\mathbb{P}}[L\_{\tau}\mathbf{1}\_{J=J\_{jk},\Delta W\in dx}] where d​xdx is an infinitesimal interval around xx.
If Δ​W=x\Delta W=x and jump Jj​kJ\_{jk} occurs, then Lτ=LD​(x)​eηj​k​Jj​kZj​(x)L\_{\tau}=L\_{D}(x)\frac{e^{\eta\_{jk}J\_{jk}}}{Z\_{j}(x)} (assuming xx is in Region jj).
So, the density for the numerator is:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​ℚ​(J=Jj​k,Δ​W=x)d​x\displaystyle\frac{\,\mathrm{d}\mathbb{Q}(J=J\_{jk},\Delta W=x)}{\,\mathrm{d}x} | =𝔼ℙ​[LD​(x)​eηj​k​Jj​kZj​(x)​𝟏J=Jj​k|Δ​W=x]​fℙ​(x)\displaystyle=\mathbb{E}\_{\mathbb{P}}\left[L\_{D}(x)\frac{e^{\eta\_{jk}J\_{jk}}}{Z\_{j}(x)}\mathbf{1}\_{J=J\_{jk}}|\Delta W=x\right]f\_{\mathbb{P}}(x) |  | (4.18) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =LD​(x)​pj​k​(x)​𝔼ℙ​[eηj​k​Jj​k]Zj​(x)​fℙ​(x)\displaystyle=L\_{D}(x)\frac{p\_{jk}(x)\mathbb{E}\_{\mathbb{P}}[e^{\eta\_{jk}J\_{jk}}]}{Z\_{j}(x)}f\_{\mathbb{P}}(x) |  | (4.19) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =LD​(x)​pj​k​(x)​eκj​k​(ηj​k)Zj​(x)​fℙ​(x)\displaystyle=L\_{D}(x)\frac{p\_{jk}(x)e^{\kappa\_{jk}(\eta\_{jk})}}{Z\_{j}(x)}f\_{\mathbb{P}}(x) |  | (4.20) |

The denominator: ℚ​(Δ​W∈d​x)\mathbb{Q}(\Delta W\in dx). The density d​ℚ​(Δ​W=x)d​x\frac{\,\mathrm{d}\mathbb{Q}(\Delta W=x)}{\,\mathrm{d}x} is 𝔼ℙ​[Lτ|Δ​W=x]​fℙ​(x)\mathbb{E}\_{\mathbb{P}}[L\_{\tau}|\Delta W=x]f\_{\mathbb{P}}(x).
From the proof of [Lemma 3.4](https://arxiv.org/html/2512.15071v1#S3.Thmtheorem4 "Lemma 3.4 (Validity of 𝐿_𝜏). ‣ 3.2. Constructing the Equivalent Martingale Measure (ℚ) ‣ 3. The No-Arbitrage Framework ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"), 𝔼ℙ​[Lτ|Δ​W=x]=LD​(x)​𝔼ℙ​[Ψ​(J,x)|x]=LD​(x)×1=LD​(x)\mathbb{E}\_{\mathbb{P}}[L\_{\tau}|\Delta W=x]=L\_{D}(x)\mathbb{E}\_{\mathbb{P}}[\Psi(J,x)|x]=L\_{D}(x)\times 1=L\_{D}(x).
So, d​ℚ​(Δ​W=x)d​x=LD​(x)​fℙ​(x)\frac{\,\mathrm{d}\mathbb{Q}(\Delta W=x)}{\,\mathrm{d}x}=L\_{D}(x)f\_{\mathbb{P}}(x).
Dividing the numerator density by the denominator density gives the conditional probability qj​k​(x)q\_{jk}(x):

|  |  |  |  |
| --- | --- | --- | --- |
|  | qj​k​(x)=LD​(x)​pj​k​(x)​eκj​k​(ηj​k)Zj​(x)​fℙ​(x)LD​(x)​fℙ​(x)=pj​k​(x)​eκj​k​(ηj​k)Zj​(x)q\_{jk}(x)=\frac{L\_{D}(x)\frac{p\_{jk}(x)e^{\kappa\_{jk}(\eta\_{jk})}}{Z\_{j}(x)}f\_{\mathbb{P}}(x)}{L\_{D}(x)f\_{\mathbb{P}}(x)}=\frac{p\_{jk}(x)e^{\kappa\_{jk}(\eta\_{jk})}}{Z\_{j}(x)} |  | (4.21) |

This matches [Eq. 4.13](https://arxiv.org/html/2512.15071v1#S4.E13 "In Item 1 ‣ Proposition 4.2 (Jumps under ℚ). ‣ 4.2. Jumps under ℚ ‣ 4. The Model under the Risk-Neutral Measure (ℚ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") and [Eq. 4.14](https://arxiv.org/html/2512.15071v1#S4.E14 "In Item 1 ‣ Proposition 4.2 (Jumps under ℚ). ‣ 4.2. Jumps under ℚ ‣ 4. The Model under the Risk-Neutral Measure (ℚ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") (assuming pj​k​(x)=pj​kp\_{jk}(x)=p\_{jk}).
For the case of no jump occurring in Region jj (where specific jumps Jj​uJ\_{ju} or Jj​dJ\_{jd} could have occurred), if it happens with probability pj​0p\_{j0} under ℙ\mathbb{P}:
The Esscher kernel for no jump (J=0J=0) is Ψ​(0,x)=eη⋅0Zj​(x)=1Zj​(x)\Psi(0,x)=\frac{e^{\eta\cdot 0}}{Z\_{j}(x)}=\frac{1}{Z\_{j}(x)}. So, eκ​(η)e^{\kappa(\eta)} term is effectively e0=1e^{0}=1.
Then qj​0​(x)=pj​0​(x)⋅1Zj​(x)q\_{j0}(x)=\frac{p\_{j0}(x)\cdot 1}{Z\_{j}(x)}, matching [Eq. 4.15](https://arxiv.org/html/2512.15071v1#S4.E15 "In Item 1 ‣ Proposition 4.2 (Jumps under ℚ). ‣ 4.2. Jumps under ℚ ‣ 4. The Model under the Risk-Neutral Measure (ℚ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps").
These probabilities sum to 1 within each region jj under ℚ\mathbb{Q}:

|  |  |  |
| --- | --- | --- |
|  | ∑k∈{u,d,0}qj​k​(x)=1Zj​(x)​(pj​u​eκj​u+pj​d​eκj​d+pj​0)=Zj​(x)Zj​(x)=1\sum\_{k\in\{u,d,0\}}q\_{jk}(x)=\frac{1}{Z\_{j}(x)}(p\_{ju}e^{\kappa\_{ju}}+p\_{jd}e^{\kappa\_{jd}}+p\_{j0})=\frac{Z\_{j}(x)}{Z\_{j}(x)}=1 |  |

2. Distributions of Jj​kℚJ\_{jk}^{\mathbb{Q}}:
The Esscher transform implies that the PDF of Jj​kJ\_{jk} under ℚ\mathbb{Q}, denoted fℚ​(jj​k)f\_{\mathbb{Q}}(j\_{jk}), is related to its PDF under ℙ\mathbb{P}, fℙ​(jj​k)f\_{\mathbb{P}}(j\_{jk}), by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fℚ​(jj​k|J​ is type ​j​k)=eηj​k​jj​k​fℙ​(jj​k)𝔼ℙ​[eηj​k​Jj​k]=eηj​k​jj​k​fℙ​(jj​k)eκj​k​(ηj​k)f\_{\mathbb{Q}}(j\_{jk}|J\text{ is type }jk)=\frac{e^{\eta\_{jk}j\_{jk}}f\_{\mathbb{P}}(j\_{jk})}{\mathbb{E}\_{\mathbb{P}}[e^{\eta\_{jk}J\_{jk}}]}=\frac{e^{\eta\_{jk}j\_{jk}}f\_{\mathbb{P}}(j\_{jk})}{e^{\kappa\_{jk}(\eta\_{jk})}} |  | (4.22) |

Given Jj​k∼𝒩​(νj​k,δj​k2)J\_{jk}\sim\mathcal{N}(\nu\_{jk},\delta\_{jk}^{2}) under ℙ\mathbb{P}, fℙ​(jj​k)=12​π​δj​k​exp⁡(−(jj​k−νj​k)22​δj​k2)f\_{\mathbb{P}}(j\_{jk})=\frac{1}{\sqrt{2\pi}\delta\_{jk}}\exp\left(-\frac{(j\_{jk}-\nu\_{jk})^{2}}{2\delta\_{jk}^{2}}\right).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | fℚ​(jj​k)\displaystyle f\_{\mathbb{Q}}(j\_{jk}) | =eηj​k​jj​k−κj​k​(ηj​k)​12​π​δj​k​exp⁡(−(jj​k−νj​k)22​δj​k2)\displaystyle=e^{\eta\_{jk}j\_{jk}-\kappa\_{jk}(\eta\_{jk})}\frac{1}{\sqrt{2\pi}\delta\_{jk}}\exp\left(-\frac{(j\_{jk}-\nu\_{jk})^{2}}{2\delta\_{jk}^{2}}\right) |  | (4.23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =12​π​δj​k​exp⁡(ηj​k​jj​k−(ηj​k​νj​k+12​ηj​k2​δj​k2)−jj​k2−2​jj​k​νj​k+νj​k22​δj​k2)\displaystyle=\frac{1}{\sqrt{2\pi}\delta\_{jk}}\exp\left(\eta\_{jk}j\_{jk}-(\eta\_{jk}\nu\_{jk}+\tfrac{1}{2}\eta\_{jk}^{2}\delta\_{jk}^{2})-\frac{j\_{jk}^{2}-2j\_{jk}\nu\_{jk}+\nu\_{jk}^{2}}{2\delta\_{jk}^{2}}\right) |  | (4.24) |

The term in the exponent is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​δj​k2​ηj​k​jj​k−2​δj​k2​ηj​k​νj​k−ηj​k2​δj​k4−(jj​k2−2​jj​k​νj​k+νj​k2)2​δj​k2\displaystyle\frac{2\delta\_{jk}^{2}\eta\_{jk}j\_{jk}-2\delta\_{jk}^{2}\eta\_{jk}\nu\_{jk}-\eta\_{jk}^{2}\delta\_{jk}^{4}-(j\_{jk}^{2}-2j\_{jk}\nu\_{jk}+\nu\_{jk}^{2})}{2\delta\_{jk}^{2}} |  | (4.25) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =−12​δj​k2​[jj​k2−2​jj​k​νj​k−2​δj​k2​ηj​k​jj​k+νj​k2+2​δj​k2​ηj​k​νj​k+ηj​k2​δj​k4]\displaystyle=-\frac{1}{2\delta\_{jk}^{2}}\left[j\_{jk}^{2}-2j\_{jk}\nu\_{jk}-2\delta\_{jk}^{2}\eta\_{jk}j\_{jk}+\nu\_{jk}^{2}+2\delta\_{jk}^{2}\eta\_{jk}\nu\_{jk}+\eta\_{jk}^{2}\delta\_{jk}^{4}\right] |  | (4.26) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =−12​δj​k2​[jj​k2−2​jj​k​(νj​k+ηj​k​δj​k2)+(νj​k2+2​νj​k​ηj​k​δj​k2+(ηj​k​δj​k2)2)]\displaystyle=-\frac{1}{2\delta\_{jk}^{2}}\left[j\_{jk}^{2}-2j\_{jk}(\nu\_{jk}+\eta\_{jk}\delta\_{jk}^{2})+(\nu\_{jk}^{2}+2\nu\_{jk}\eta\_{jk}\delta\_{jk}^{2}+(\eta\_{jk}\delta\_{jk}^{2})^{2})\right] |  | (4.27) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =−12​δj​k2​[jj​k2−2​jj​k​(νj​k+ηj​k​δj​k2)+(νj​k+ηj​k​δj​k2)2]\displaystyle=-\frac{1}{2\delta\_{jk}^{2}}\left[j\_{jk}^{2}-2j\_{jk}(\nu\_{jk}+\eta\_{jk}\delta\_{jk}^{2})+(\nu\_{jk}+\eta\_{jk}\delta\_{jk}^{2})^{2}\right] |  | (4.28) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =−(jj​k−(νj​k+ηj​k​δj​k2))22​δj​k2\displaystyle=-\frac{(j\_{jk}-(\nu\_{jk}+\eta\_{jk}\delta\_{jk}^{2}))^{2}}{2\delta\_{jk}^{2}} |  | (4.29) |

Let νj​kℚ=νj​k+ηj​k​δj​k2\nu\_{jk}^{\mathbb{Q}}=\nu\_{jk}+\eta\_{jk}\delta\_{jk}^{2}. Then the exponent is −(jj​k−νj​kℚ)22​δj​k2-\frac{(j\_{jk}-\nu\_{jk}^{\mathbb{Q}})^{2}}{2\delta\_{jk}^{2}}.
So, fℚ​(jj​k)=12​π​δj​k​exp⁡(−(jj​k−νj​kℚ)22​δj​k2)f\_{\mathbb{Q}}(j\_{jk})=\frac{1}{\sqrt{2\pi}\delta\_{jk}}\exp\left(-\frac{(j\_{jk}-\nu\_{jk}^{\mathbb{Q}})^{2}}{2\delta\_{jk}^{2}}\right). This is the PDF of a 𝒩​(νj​kℚ,δj​k2)\mathcal{N}(\nu\_{jk}^{\mathbb{Q}},\delta\_{jk}^{2}) distribution.
∎

### 4.3. Risk-Neutral Dynamics and Multi-Period Martingale

###### Theorem 4.3 (Asset Price Dynamics under ℚ\mathbb{Q}).

Under the risk-neutral measure ℚ\mathbb{Q}, the asset price evolves as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | St+τ=St​exp⁡[(μ−12​σ2)​τ+σ​(Δ​Wt,τℚ−γD​σ​τ)+Jt+τℚ]S\_{t+\tau}=S\_{t}\exp\left[(\mu-\tfrac{1}{2}\sigma^{2})\tau+\sigma(\Delta W\_{t,\tau}^{\mathbb{Q}}-\gamma\_{D}\sigma\tau)+J\_{t+\tau}^{\mathbb{Q}}\right] |  | (4.30) |

where Δ​Wt,τℚ=Δ​Wt,τ+γD​σ​τ∼𝒩​(0,τ)\Delta W\_{t,\tau}^{\mathbb{Q}}=\Delta W\_{t,\tau}+\gamma\_{D}\sigma\tau\sim\mathcal{N}(0,\tau) under ℚ\mathbb{Q}, and Jt+τℚJ\_{t+\tau}^{\mathbb{Q}} is the jump component whose occurrence and distribution follow [Proposition 4.2](https://arxiv.org/html/2512.15071v1#S4.Thmtheorem2 "Proposition 4.2 (Jumps under ℚ). ‣ 4.2. Jumps under ℚ ‣ 4. The Model under the Risk-Neutral Measure (ℚ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"), triggered by x=Δ​Wt,τ=Δ​Wt,τℚ−γD​σ​τx=\Delta W\_{t,\tau}=\Delta W\_{t,\tau}^{\mathbb{Q}}-\gamma\_{D}\sigma\tau.

###### Proof.

This follows by substituting the ℚ\mathbb{Q}-distributions for the diffusion increment from [Proposition 4.1](https://arxiv.org/html/2512.15071v1#S4.Thmtheorem1 "Proposition 4.1 (Diffusion under ℚ). ‣ 4.1. Diffusion under ℚ ‣ 4. The Model under the Risk-Neutral Measure (ℚ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") (expressed in terms of the ℚ\mathbb{Q}-Brownian motion Δ​Wℚ\Delta W^{\mathbb{Q}}) and the jump characteristics (probabilities and distributions) from [Proposition 4.2](https://arxiv.org/html/2512.15071v1#S4.Thmtheorem2 "Proposition 4.2 (Jumps under ℚ). ‣ 4.2. Jumps under ℚ ‣ 4. The Model under the Risk-Neutral Measure (ℚ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") into the general asset price evolution equation [Eq. 2.3](https://arxiv.org/html/2512.15071v1#S2.E3 "In 2.1. Setup and Assumptions ‣ 2. The Model under the Physical Measure (ℙ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"). The key is that the structure of jump triggering remains dependent on the actual path of Δ​Wt,τ\Delta W\_{t,\tau}, which is now understood in terms of its ℚ\mathbb{Q}-distribution. ∎

###### Lemma 4.4 (Exponential Martingale).

Let Lt=∏i=0t/τ−1Li​τ​(Δ​Wi​τ,τ,J(i+1)​τ)L\_{t}=\prod\_{i=0}^{t/\tau-1}L\_{i\tau}(\Delta W\_{i\tau,\tau},J\_{(i+1)\tau}) be the multi-period Radon-Nikodym derivative for ℱt\mathcal{F}\_{t}. Under the assumption of temporal independence ([2.3](https://arxiv.org/html/2512.15071v1#S2.Thmtheorem3 "Assumption 2.3 (Temporal Independence). ‣ 2.2. Diffusion-Dependent Jumps ‣ 2. The Model under the Physical Measure (ℙ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps")), LtL\_{t} is an (ℱt,ℙ)(\mathcal{F}\_{t},\mathbb{P})-martingale with 𝔼ℙ​[Lt]=1\mathbb{E}\_{\mathbb{P}}[L\_{t}]=1.

###### Proof.

We prove this by induction on tk=k​τt\_{k}=k\tau.
Base case (k=0,t0=0k=0,t\_{0}=0): L0=1L\_{0}=1 (empty product). So 𝔼ℙ​[L0]=1\mathbb{E}\_{\mathbb{P}}[L\_{0}]=1.
Inductive step: Assume LtkL\_{t\_{k}} is an (ℱtk,ℙ)(\mathcal{F}\_{t\_{k}},\mathbb{P})-martingale with 𝔼ℙ​[Ltk]=1\mathbb{E}\_{\mathbb{P}}[L\_{t\_{k}}]=1.
Consider Ltk+1=Ltk⋅Ltk​τ​(Δ​Wtk,τ,J(tk+1)​τ)L\_{t\_{k+1}}=L\_{t\_{k}}\cdot L\_{t\_{k}\tau}(\Delta W\_{t\_{k},\tau},J\_{(t\_{k}+1)\tau}).
We want to show 𝔼ℙ​[Ltk+1|ℱtk]=Ltk\mathbb{E}\_{\mathbb{P}}[L\_{t\_{k+1}}|\mathcal{F}\_{t\_{k}}]=L\_{t\_{k}}.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼ℙ​[Ltk+1|ℱtk]\displaystyle\mathbb{E}\_{\mathbb{P}}[L\_{t\_{k+1}}|\mathcal{F}\_{t\_{k}}] | =𝔼ℙ​[Ltk⋅Ltk​τ​(Δ​Wtk,τ,J(tk+1)​τ)|ℱtk]\displaystyle=\mathbb{E}\_{\mathbb{P}}[L\_{t\_{k}}\cdot L\_{t\_{k}\tau}(\Delta W\_{t\_{k},\tau},J\_{(t\_{k}+1)\tau})|\mathcal{F}\_{t\_{k}}] |  | (4.31) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Ltk​𝔼ℙ​[Ltk​τ​(Δ​Wtk,τ,J(tk+1)​τ)|ℱtk],\displaystyle=L\_{t\_{k}}\mathbb{E}\_{\mathbb{P}}[L\_{t\_{k}\tau}(\Delta W\_{t\_{k},\tau},J\_{(t\_{k}+1)\tau})|\mathcal{F}\_{t\_{k}}], |  | (4.32) |

since LtkL\_{t\_{k}} is ℱtk−\mathcal{F}\_{t\_{k}}-measurable. By [2.3](https://arxiv.org/html/2512.15071v1#S2.Thmtheorem3 "Assumption 2.3 (Temporal Independence). ‣ 2.2. Diffusion-Dependent Jumps ‣ 2. The Model under the Physical Measure (ℙ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"), the increment (Δ​Wtk,τ,J(tk+1)​τ)(\Delta W\_{t\_{k},\tau},J\_{(t\_{k}+1)\tau}) and thus Ltk​τL\_{t\_{k}\tau} (which is a function of this increment) is independent of ℱtk\mathcal{F}\_{t\_{k}}. Therefore:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[Ltk​τ​(Δ​Wtk,τ,J(tk+1)​τ)|ℱtk]=𝔼ℙ​[Ltk​τ​(Δ​Wtk,τ,J(tk+1)​τ)]\mathbb{E}\_{\mathbb{P}}[L\_{t\_{k}\tau}(\Delta W\_{t\_{k},\tau},J\_{(t\_{k}+1)\tau})|\mathcal{F}\_{t\_{k}}]=\mathbb{E}\_{\mathbb{P}}[L\_{t\_{k}\tau}(\Delta W\_{t\_{k},\tau},J\_{(t\_{k}+1)\tau})] |  | (4.33) |

From [Lemma 3.4](https://arxiv.org/html/2512.15071v1#S3.Thmtheorem4 "Lemma 3.4 (Validity of 𝐿_𝜏). ‣ 3.2. Constructing the Equivalent Martingale Measure (ℚ) ‣ 3. The No-Arbitrage Framework ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"), we know that the expectation of the one-step kernel is 1:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[Ltk​τ​(Δ​Wtk,τ,J(tk+1)​τ)]=1\mathbb{E}\_{\mathbb{P}}[L\_{t\_{k}\tau}(\Delta W\_{t\_{k},\tau},J\_{(t\_{k}+1)\tau})]=1 |  | (4.34) |

Substituting this back:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[Ltk+1|ℱtk]=Ltk×1=Ltk\mathbb{E}\_{\mathbb{P}}[L\_{t\_{k+1}}|\mathcal{F}\_{t\_{k}}]=L\_{t\_{k}}\times 1=L\_{t\_{k}} |  | (4.35) |

Thus, LtL\_{t} is a martingale with respect to (ℱt,ℙ)(\mathcal{F}\_{t},\mathbb{P}). By the tower property of conditional expectation, 𝔼ℙ​[Lt]=𝔼ℙ​[𝔼ℙ​[Lt|ℱ0]]=𝔼ℙ​[L0]=1\mathbb{E}\_{\mathbb{P}}[L\_{t}]=\mathbb{E}\_{\mathbb{P}}[\mathbb{E}\_{\mathbb{P}}[L\_{t}|\mathcal{F}\_{0}]]=\mathbb{E}\_{\mathbb{P}}[L\_{0}]=1.
∎

This lemma is essential as it ensures that the measure ℚ\mathbb{Q} defined by LTL\_{T} is a valid probability measure equivalent to ℙ\mathbb{P} over the entire horizon [0,T][0,T].

## 5. The No-Arbitrage Condition

We now derive the explicit condition on the physical drift μ\mu.

### 5.1. Deriving the Condition in Full Detail

The no-arbitrage condition from [Theorem 3.1](https://arxiv.org/html/2512.15071v1#S3.Thmtheorem1 "Theorem 3.1 (FTAP for Discrete Time - [5]). ‣ 3.1. The Fundamental Theorem of Asset Pricing (FTAP) ‣ 3. The No-Arbitrage Framework ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") is 𝔼ℚ​[St+τ/St|ℱt]=er​τ\mathbb{E}\_{\mathbb{Q}}[S\_{t+\tau}/S\_{t}|\mathcal{F}\_{t}]=e^{r\tau}. Using the definition of expectation under an EMM, this is equivalent to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[Lτ​St+τSt|ℱt]=er​τ\mathbb{E}\_{\mathbb{P}}\left[L\_{\tau}\frac{S\_{t+\tau}}{S\_{t}}\bigg|\mathcal{F}\_{t}\right]=e^{r\tau} |  | (5.1) |

Since LτL\_{\tau} and St+τ/StS\_{t+\tau}/S\_{t} (which depend on Δ​Wt,τ\Delta W\_{t,\tau} and Jt+τJ\_{t+\tau}) are independent of ℱt\mathcal{F}\_{t} given [2.3](https://arxiv.org/html/2512.15071v1#S2.Thmtheorem3 "Assumption 2.3 (Temporal Independence). ‣ 2.2. Diffusion-Dependent Jumps ‣ 2. The Model under the Physical Measure (ℙ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"), the conditioning on ℱt\mathcal{F}\_{t} can be dropped for the expectation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[Lτ​St+τSt]=er​τ\mathbb{E}\_{\mathbb{P}}\left[L\_{\tau}\frac{S\_{t+\tau}}{S\_{t}}\right]=e^{r\tau} |  | (5.2) |

Substitute the expressions for LτL\_{\tau} from [Definition 3.3](https://arxiv.org/html/2512.15071v1#S3.Thmtheorem3 "Definition 3.3 (Radon-Nikodym Derivative 𝐿_𝜏). ‣ 3.2. Constructing the Equivalent Martingale Measure (ℚ) ‣ 3. The No-Arbitrage Framework ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") and St+τ/StS\_{t+\tau}/S\_{t} from [Eq. 2.3](https://arxiv.org/html/2512.15071v1#S2.E3 "In 2.1. Setup and Assumptions ‣ 2. The Model under the Physical Measure (ℙ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[LD​(Δ​W)​Ψ​(J,Δ​W)​exp⁡((μ−12​σ2)​τ+σ​Δ​W+J)]=er​τ\mathbb{E}\_{\mathbb{P}}\left[L\_{D}(\Delta W)\Psi(J,\Delta W)\exp\left((\mu-\tfrac{1}{2}\sigma^{2})\tau+\sigma\Delta W+J\right)\right]=e^{r\tau} |  | (5.3) |

where Δ​W=Δ​Wt,τ\Delta W=\Delta W\_{t,\tau} and J=Jt+τJ=J\_{t+\tau}.
We can group the terms that do not depend on JJ (given Δ​W\Delta W) outside the conditional expectation on JJ:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[LD​(Δ​W)​exp⁡((μ−12​σ2)​τ+σ​Δ​W)​𝔼ℙ​[Ψ​(J,Δ​W)​eJ|Δ​W]]=er​τ\mathbb{E}\_{\mathbb{P}}\left[L\_{D}(\Delta W)\exp\left((\mu-\tfrac{1}{2}\sigma^{2})\tau+\sigma\Delta W\right)\mathbb{E}\_{\mathbb{P}}[\Psi(J,\Delta W)e^{J}|\Delta W]\right]=e^{r\tau} |  | (5.4) |

Let’s analyze the inner conditional expectation 𝔼ℙ​[Ψ​(J,x)​eJ|Δ​W=x]\mathbb{E}\_{\mathbb{P}}[\Psi(J,x)e^{J}|\Delta W=x]. Let xx be in Region jj.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼ℙ​[Ψ​(J,x)​eJ|x]\displaystyle\mathbb{E}\_{\mathbb{P}}[\Psi(J,x)e^{J}|x] | =pj​u​𝔼ℙ​[eηj​u​Jj​uZj​eJj​u]+pj​d​𝔼ℙ​[eηj​d​Jj​dZj​eJj​d]+pj​0​𝔼ℙ​[1Zj​e0]\displaystyle=p\_{ju}\mathbb{E}\_{\mathbb{P}}\left[\frac{e^{\eta\_{ju}J\_{ju}}}{Z\_{j}}e^{J\_{ju}}\right]+p\_{jd}\mathbb{E}\_{\mathbb{P}}\left[\frac{e^{\eta\_{jd}J\_{jd}}}{Z\_{j}}e^{J\_{jd}}\right]+p\_{j0}\mathbb{E}\_{\mathbb{P}}\left[\frac{1}{Z\_{j}}e^{0}\right] |  | (5.5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1Zj​(pj​u​𝔼ℙ​[e(1+ηj​u)​Jj​u]+pj​d​𝔼ℙ​[e(1+ηj​d)​Jj​d]+pj​0)\displaystyle=\frac{1}{Z\_{j}}\left(p\_{ju}\mathbb{E}\_{\mathbb{P}}[e^{(1+\eta\_{ju})J\_{ju}}]+p\_{jd}\mathbb{E}\_{\mathbb{P}}[e^{(1+\eta\_{jd})J\_{jd}}]+p\_{j0}\right) |  | (5.6) |

For Jj​k∼𝒩​(νj​k,δj​k2)J\_{jk}\sim\mathcal{N}(\nu\_{jk},\delta\_{jk}^{2}), its moment generating function is

|  |  |  |
| --- | --- | --- |
|  | MJj​k​(s)=exp⁡(s​νj​k+12​s2​δj​k2).M\_{J\_{jk}}(s)=\exp(s\nu\_{jk}+\tfrac{1}{2}s^{2}\delta\_{jk}^{2}). |  |

So, 𝔼ℙ​[e(1+ηj​k)​Jj​k]=exp⁡((1+ηj​k)​νj​k+12​(1+ηj​k)2​δj​k2)\mathbb{E}\_{\mathbb{P}}[e^{(1+\eta\_{jk})J\_{jk}}]=\exp((1+\eta\_{jk})\nu\_{jk}+\tfrac{1}{2}(1+\eta\_{jk})^{2}\delta\_{jk}^{2}).

Let’s expand the exponent:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (1+ηj​k)​νj​k+12​(1+ηj​k)2​δj​k2\displaystyle(1+\eta\_{jk})\nu\_{jk}+\tfrac{1}{2}(1+\eta\_{jk})^{2}\delta\_{jk}^{2} | =νj​k+ηj​k​νj​k+12​(1+2​ηj​k+ηj​k2)​δj​k2\displaystyle=\nu\_{jk}+\eta\_{jk}\nu\_{jk}+\tfrac{1}{2}(1+2\eta\_{jk}+\eta\_{jk}^{2})\delta\_{jk}^{2} |  | (5.7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =νj​k+ηj​k​νj​k+12​δj​k2+ηj​k​δj​k2+12​ηj​k2​δj​k2\displaystyle=\nu\_{jk}+\eta\_{jk}\nu\_{jk}+\tfrac{1}{2}\delta\_{jk}^{2}+\eta\_{jk}\delta\_{jk}^{2}+\tfrac{1}{2}\eta\_{jk}^{2}\delta\_{jk}^{2} |  | (5.8) |

Recall νj​kℚ=νj​k+ηj​k​δj​k2\nu\_{jk}^{\mathbb{Q}}=\nu\_{jk}+\eta\_{jk}\delta\_{jk}^{2}. The exponent can be rewritten as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (νj​k+ηj​k​δj​k2)+12​δj​k2+ηj​k​νj​k+12​ηj​k2​δj​k2=νj​kℚ+12​δj​k2+κj​k​(ηj​k)(\nu\_{jk}+\eta\_{jk}\delta\_{jk}^{2})+\tfrac{1}{2}\delta\_{jk}^{2}+\eta\_{jk}\nu\_{jk}+\tfrac{1}{2}\eta\_{jk}^{2}\delta\_{jk}^{2}=\nu\_{jk}^{\mathbb{Q}}+\tfrac{1}{2}\delta\_{jk}^{2}+\kappa\_{jk}(\eta\_{jk}) |  | (5.9) |

So, 𝔼ℙ​[e(1+ηj​k)​Jj​k]=exp⁡(νj​kℚ+12​δj​k2)​exp⁡(κj​k​(ηj​k))\mathbb{E}\_{\mathbb{P}}[e^{(1+\eta\_{jk})J\_{jk}}]=\exp(\nu\_{jk}^{\mathbb{Q}}+\tfrac{1}{2}\delta\_{jk}^{2})\exp(\kappa\_{jk}(\eta\_{jk})).
Therefore, using [Eqs. 4.13](https://arxiv.org/html/2512.15071v1#S4.E13 "In Item 1 ‣ Proposition 4.2 (Jumps under ℚ). ‣ 4.2. Jumps under ℚ ‣ 4. The Model under the Risk-Neutral Measure (ℚ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"), [4.14](https://arxiv.org/html/2512.15071v1#S4.E14 "Equation 4.14 ‣ Item 1 ‣ Proposition 4.2 (Jumps under ℚ). ‣ 4.2. Jumps under ℚ ‣ 4. The Model under the Risk-Neutral Measure (ℚ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") and [4.15](https://arxiv.org/html/2512.15071v1#S4.E15 "Equation 4.15 ‣ Item 1 ‣ Proposition 4.2 (Jumps under ℚ). ‣ 4.2. Jumps under ℚ ‣ 4. The Model under the Risk-Neutral Measure (ℚ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼ℙ​[Ψ​(J,x)​eJ|x]\displaystyle\mathbb{E}\_{\mathbb{P}}[\Psi(J,x)e^{J}|x] | =1Zj​(pj​u​eκj​u​(ηj​u)​eνj​uℚ+δj​u2/2+pj​d​eκj​d​(ηj​d)​eνj​dℚ+δj​d2/2+pj​0)\displaystyle=\frac{1}{Z\_{j}}\left(p\_{ju}e^{\kappa\_{ju}(\eta\_{ju})}e^{\nu\_{ju}^{\mathbb{Q}}+\delta\_{ju}^{2}/2}+p\_{jd}e^{\kappa\_{jd}(\eta\_{jd})}e^{\nu\_{jd}^{\mathbb{Q}}+\delta\_{jd}^{2}/2}+p\_{j0}\right) |  | (5.10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =qj​u​(x)​eνj​uℚ+δj​u2/2+qj​d​(x)​eνj​dℚ+δj​d2/2+qj​0​(x)\displaystyle=q\_{ju}(x)e^{\nu\_{ju}^{\mathbb{Q}}+\delta\_{ju}^{2}/2}+q\_{jd}(x)e^{\nu\_{jd}^{\mathbb{Q}}+\delta\_{jd}^{2}/2}+q\_{j0}(x) |  | (5.11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Mℚ​(x)\displaystyle=M\_{\mathbb{Q}}(x) |  | (5.12) |

where Mℚ​(x)=𝔼ℚ​[eJℚ|Δ​W=x]M\_{\mathbb{Q}}(x)=\mathbb{E}\_{\mathbb{Q}}[e^{J^{\mathbb{Q}}}|\Delta W=x] is the conditional MGF of the jump factor exp⁡(Jℚ)\exp(J^{\mathbb{Q}}) under ℚ\mathbb{Q}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mℚ​(x)={q1​u​(x)​eν1​uℚ+δ1​u2/2+q1​d​(x)​eν1​dℚ+δ1​d2/2+q10​(x)x<bd​τq2​u​(x)​eν2​uℚ+δ2​u2/2+q2​d​(x)​eν2​dℚ+δ2​d2/2+q20​(x)x>bu​τ1bd​τ≤x≤bu​τM\_{\mathbb{Q}}(x)=\begin{cases}q\_{1u}(x)e^{\nu\_{1u}^{\mathbb{Q}}+\delta\_{1u}^{2}/2}+q\_{1d}(x)e^{\nu\_{1d}^{\mathbb{Q}}+\delta\_{1d}^{2}/2}+q\_{10}(x)&x<b\_{d}\sqrt{\tau}\\ q\_{2u}(x)e^{\nu\_{2u}^{\mathbb{Q}}+\delta\_{2u}^{2}/2}+q\_{2d}(x)e^{\nu\_{2d}^{\mathbb{Q}}+\delta\_{2d}^{2}/2}+q\_{20}(x)&x>b\_{u}\sqrt{\tau}\\ 1&b\_{d}\sqrt{\tau}\leq x\leq b\_{u}\sqrt{\tau}\end{cases} |  | (5.13) |

Substituting [Eq. 5.12](https://arxiv.org/html/2512.15071v1#S5.E12 "In 5.1. Deriving the Condition in Full Detail ‣ 5. The No-Arbitrage Condition ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") back into the main expectation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[LD​(Δ​W)​exp⁡((μ−12​σ2)​τ+σ​Δ​W)​Mℚ​(Δ​W)]=er​τ\mathbb{E}\_{\mathbb{P}}\left[L\_{D}(\Delta W)\exp\left((\mu-\tfrac{1}{2}\sigma^{2})\tau+\sigma\Delta W\right)M\_{\mathbb{Q}}(\Delta W)\right]=e^{r\tau} |  | (5.14) |

Now, substitute LD​(Δ​W)=exp⁡(−γD​σ​Δ​W−12​(γD​σ)2​τ)L\_{D}(\Delta W)=\exp\left(-\gamma\_{D}\sigma\Delta W-\frac{1}{2}(\gamma\_{D}\sigma)^{2}\tau\right):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[exp⁡(−γD​σ​Δ​W−(γD​σ)2​τ2)​exp⁡((μ−12​σ2)​τ+σ​Δ​W)​Mℚ​(Δ​W)]=er​τ\mathbb{E}\_{\mathbb{P}}\left[\exp\left(-\gamma\_{D}\sigma\Delta W-\frac{(\gamma\_{D}\sigma)^{2}\tau}{2}\right)\exp\left((\mu-\tfrac{1}{2}\sigma^{2})\tau+\sigma\Delta W\right)M\_{\mathbb{Q}}(\Delta W)\right]=e^{r\tau} |  | (5.15) |

Combine the arguments of the exponential functions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −γD​σ​Δ​W−γD2​σ2​τ2+(μ−12​σ2)​τ+σ​Δ​W\displaystyle-\gamma\_{D}\sigma\Delta W-\frac{\gamma\_{D}^{2}\sigma^{2}\tau}{2}+(\mu-\tfrac{1}{2}\sigma^{2})\tau+\sigma\Delta W |  | (5.16) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =(μ−12​σ2−12​γD2​σ2)​τ+(σ−γD​σ)​Δ​W\displaystyle=(\mu-\tfrac{1}{2}\sigma^{2}-\tfrac{1}{2}\gamma\_{D}^{2}\sigma^{2})\tau+(\sigma-\gamma\_{D}\sigma)\Delta W |  | (5.17) |

So the expectation becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ​[exp⁡((μ−12​σ2−12​γD2​σ2)​τ+(σ−γD​σ)​Δ​W)​Mℚ​(Δ​W)]=er​τ\mathbb{E}\_{\mathbb{P}}\left[\exp\left((\mu-\tfrac{1}{2}\sigma^{2}-\tfrac{1}{2}\gamma\_{D}^{2}\sigma^{2})\tau+(\sigma-\gamma\_{D}\sigma)\Delta W\right)M\_{\mathbb{Q}}(\Delta W)\right]=e^{r\tau} |  | (5.18) |

Let K=(μ−12​σ2−12​γD2​σ2)​τK=(\mu-\tfrac{1}{2}\sigma^{2}-\tfrac{1}{2}\gamma\_{D}^{2}\sigma^{2})\tau and G=σ​(1−γD)G=\sigma(1-\gamma\_{D}).
Let fℙ​(x)f\_{\mathbb{P}}(x) denote the PDF of Δ​W∼𝒩​(0,τ)\Delta W\sim\mathcal{N}(0,\tau), which is fℙ​(x)=12​π​τ​exp⁡(−x2/(2​τ))f\_{\mathbb{P}}(x)=\frac{1}{\sqrt{2\pi\tau}}\exp(-x^{2}/(2\tau)).

The expectation in [Eq. 5.18](https://arxiv.org/html/2512.15071v1#S5.E18 "In 5.1. Deriving the Condition in Full Detail ‣ 5. The No-Arbitrage Condition ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") can be written as an integral:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫−∞∞exp⁡(K+G​x)​Mℚ​(x)​fℙ​(x)​dx=er​τ\int\_{-\infty}^{\infty}\exp\left(K+Gx\right)M\_{\mathbb{Q}}(x)f\_{\mathbb{P}}(x)\,\mathrm{d}x=e^{r\tau} |  | (5.19) |

Since KK does not depend on xx, we can factor eKe^{K} out of the integral:

|  |  |  |  |
| --- | --- | --- | --- |
|  | eK​∫−∞∞eG​x​Mℚ​(x)​12​π​τ​exp⁡(−x22​τ)​dx=er​τe^{K}\int\_{-\infty}^{\infty}e^{Gx}M\_{\mathbb{Q}}(x)\frac{1}{\sqrt{2\pi\tau}}\exp\left(-\frac{x^{2}}{2\tau}\right)\,\mathrm{d}x=e^{r\tau} |  | (5.20) |

Combine the exponential terms involving xx inside the integral:

|  |  |  |  |
| --- | --- | --- | --- |
|  | eK​∫−∞∞Mℚ​(x)​12​π​τ​exp⁡(G​x−x22​τ)​dx=er​τe^{K}\int\_{-\infty}^{\infty}M\_{\mathbb{Q}}(x)\frac{1}{\sqrt{2\pi\tau}}\exp\left(Gx-\frac{x^{2}}{2\tau}\right)\,\mathrm{d}x=e^{r\tau} |  | (5.21) |

We complete the square for the term G​x−x22​τGx-\frac{x^{2}}{2\tau} in the exponent:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G​x−x22​τ\displaystyle Gx-\frac{x^{2}}{2\tau} | =−12​τ​(x2−2​G​τ​x)\displaystyle=-\frac{1}{2\tau}(x^{2}-2G\tau x) |  | (5.22) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−12​τ​(x2−2​G​τ​x+(G​τ)2−(G​τ)2)(add and subtract ​(G​τ)2​)\displaystyle=-\frac{1}{2\tau}(x^{2}-2G\tau x+(G\tau)^{2}-(G\tau)^{2})\quad\text{(add and subtract }(G\tau)^{2}\text{)} |  | (5.23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−12​τ​((x−G​τ)2−(G​τ)2)\displaystyle=-\frac{1}{2\tau}\left((x-G\tau)^{2}-(G\tau)^{2}\right) |  | (5.24) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−(x−G​τ)22​τ+(G​τ)22​τ=−(x−G​τ)22​τ+G2​τ2\displaystyle=-\frac{(x-G\tau)^{2}}{2\tau}+\frac{(G\tau)^{2}}{2\tau}=-\frac{(x-G\tau)^{2}}{2\tau}+\frac{G^{2}\tau}{2} |  | (5.25) |

Substitute this back into the integral:

|  |  |  |  |
| --- | --- | --- | --- |
|  | eK​∫−∞∞Mℚ​(x)​12​π​τ​exp⁡(−(x−G​τ)22​τ+G2​τ2)​dx=er​τe^{K}\int\_{-\infty}^{\infty}M\_{\mathbb{Q}}(x)\frac{1}{\sqrt{2\pi\tau}}\exp\left(-\frac{(x-G\tau)^{2}}{2\tau}+\frac{G^{2}\tau}{2}\right)\,\mathrm{d}x=e^{r\tau} |  | (5.26) |

The term exp⁡(G2​τ/2)\exp(G^{2}\tau/2) does not depend on xx and can be factored out of the integral:

|  |  |  |  |
| --- | --- | --- | --- |
|  | eK​exp⁡(G2​τ2)​∫−∞∞Mℚ​(x)​12​π​τ​exp⁡(−(x−G​τ)22​τ)​dx=er​τe^{K}\exp\left(\frac{G^{2}\tau}{2}\right)\int\_{-\infty}^{\infty}M\_{\mathbb{Q}}(x)\frac{1}{\sqrt{2\pi\tau}}\exp\left(-\frac{(x-G\tau)^{2}}{2\tau}\right)\,\mathrm{d}x=e^{r\tau} |  | (5.27) |

This can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | eK+G2​τ/2​𝔼P∗​[Mℚ​(X)]=er​τe^{K+G^{2}\tau/2}\mathbb{E}\_{P^{\*}}[M\_{\mathbb{Q}}(X)]=e^{r\tau} |  | (5.28) |

where 𝔼P∗​[⋅]\mathbb{E}\_{P^{\*}}[\cdot] denotes the expectation with respect to a random variable XX that follows a Normal distribution with mean G​τG\tau and variance τ\tau, i.e., X∼𝒩​(G​τ,τ)X\sim\mathcal{N}(G\tau,\tau).
Now, take the natural logarithm of both sides of [Eq. 5.28](https://arxiv.org/html/2512.15071v1#S5.E28 "In 5.1. Deriving the Condition in Full Detail ‣ 5. The No-Arbitrage Condition ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | K+G2​τ2+ln⁡(𝔼P∗​[Mℚ​(X)])=r​τK+\frac{G^{2}\tau}{2}+\ln\left(\mathbb{E}\_{P^{\*}}[M\_{\mathbb{Q}}(X)]\right)=r\tau |  | (5.29) |

Substitute back the expressions for K=(μ−12​σ2−12​γD2​σ2)​τK=(\mu-\tfrac{1}{2}\sigma^{2}-\tfrac{1}{2}\gamma\_{D}^{2}\sigma^{2})\tau and G=σ​(1−γD)G=\sigma(1-\gamma\_{D}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | (μ−12​σ2−12​γD2​σ2)​τ+(σ​(1−γD))2​τ2+ln⁡(𝔼P∗​[Mℚ​(X)])=r​τ(\mu-\tfrac{1}{2}\sigma^{2}-\tfrac{1}{2}\gamma\_{D}^{2}\sigma^{2})\tau+\frac{(\sigma(1-\gamma\_{D}))^{2}\tau}{2}+\ln\left(\mathbb{E}\_{P^{\*}}[M\_{\mathbb{Q}}(X)]\right)=r\tau |  | (5.30) |

Expand the term (σ​(1−γD))2​τ2\frac{(\sigma(1-\gamma\_{D}))^{2}\tau}{2}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ2​(1−γD)2​τ2=σ2​(1−2​γD+γD2)​τ2=(12​σ2−γD​σ2+12​γD2​σ2)​τ\frac{\sigma^{2}(1-\gamma\_{D})^{2}\tau}{2}=\frac{\sigma^{2}(1-2\gamma\_{D}+\gamma\_{D}^{2})\tau}{2}=\left(\tfrac{1}{2}\sigma^{2}-\gamma\_{D}\sigma^{2}+\tfrac{1}{2}\gamma\_{D}^{2}\sigma^{2}\right)\tau |  | (5.31) |

Substitute this into the equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (μ−12​σ2−12​γD2​σ2)​τ+(12​σ2−γD​σ2+12​γD2​σ2)​τ+ln⁡(𝔼P∗​[Mℚ​(X)])=r​τ(\mu-\tfrac{1}{2}\sigma^{2}-\tfrac{1}{2}\gamma\_{D}^{2}\sigma^{2})\tau+(\tfrac{1}{2}\sigma^{2}-\gamma\_{D}\sigma^{2}+\tfrac{1}{2}\gamma\_{D}^{2}\sigma^{2})\tau+\ln\left(\mathbb{E}\_{P^{\*}}[M\_{\mathbb{Q}}(X)]\right)=r\tau |  | (5.32) |

Combine the terms involving τ\tau:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ​τ−12​σ2​τ−12​γD2​σ2​τ+12​σ2​τ−γD​σ2​τ+12​γD2​σ2​τ+ln⁡(𝔼P∗​[Mℚ​(X)])=r​τ\displaystyle\mu\tau-\tfrac{1}{2}\sigma^{2}\tau-\tfrac{1}{2}\gamma\_{D}^{2}\sigma^{2}\tau+\tfrac{1}{2}\sigma^{2}\tau-\gamma\_{D}\sigma^{2}\tau+\tfrac{1}{2}\gamma\_{D}^{2}\sigma^{2}\tau+\ln\left(\mathbb{E}\_{P^{\*}}[M\_{\mathbb{Q}}(X)]\right)=r\tau |  | (5.33) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | μ​τ+(−12​σ2​τ+12​σ2​τ)+(−12​γD2​σ2​τ+12​γD2​σ2​τ)−γD​σ2​τ+ln⁡(𝔼P∗​[Mℚ​(X)])=r​τ\displaystyle\mu\tau+(-\tfrac{1}{2}\sigma^{2}\tau+\tfrac{1}{2}\sigma^{2}\tau)+(-\tfrac{1}{2}\gamma\_{D}^{2}\sigma^{2}\tau+\tfrac{1}{2}\gamma\_{D}^{2}\sigma^{2}\tau)-\gamma\_{D}\sigma^{2}\tau+\ln\left(\mathbb{E}\_{P^{\*}}[M\_{\mathbb{Q}}(X)]\right)=r\tau |  | (5.34) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | μ​τ+0+0−γD​σ2​τ+ln⁡(𝔼P∗​[Mℚ​(X)])=r​τ\displaystyle\mu\tau+0+0-\gamma\_{D}\sigma^{2}\tau+\ln\left(\mathbb{E}\_{P^{\*}}[M\_{\mathbb{Q}}(X)]\right)=r\tau |  | (5.35) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (μ−γD​σ2)​τ+ln⁡(𝔼P∗​[Mℚ​(X)])=r​τ\displaystyle(\mu-\gamma\_{D}\sigma^{2})\tau+\ln\left(\mathbb{E}\_{P^{\*}}[M\_{\mathbb{Q}}(X)]\right)=r\tau |  | (5.36) |

Now, solve for μ\mu:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ​τ=r​τ+γD​σ2​τ−ln⁡(𝔼P∗​[Mℚ​(X)])\mu\tau=r\tau+\gamma\_{D}\sigma^{2}\tau-\ln\left(\mathbb{E}\_{P^{\*}}[M\_{\mathbb{Q}}(X)]\right) |  | (5.37) |

Divide by τ\tau (assuming τ>0\tau>0):

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ=r+γD​σ2−1τ​ln⁡(𝔼P∗​[Mℚ​(X)])\mu=r+\gamma\_{D}\sigma^{2}-\frac{1}{\tau}\ln\left(\mathbb{E}\_{P^{\*}}[M\_{\mathbb{Q}}(X)]\right) |  | (5.38) |

The expectation 𝔼P∗​[Mℚ​(X)]\mathbb{E}\_{P^{\*}}[M\_{\mathbb{Q}}(X)] is taken with respect to X∼𝒩​(G​τ,τ)X\sim\mathcal{N}(G\tau,\tau), where G​τ=σ​(1−γD)​τG\tau=\sigma(1-\gamma\_{D})\tau.

###### Theorem 5.1 (The No-Arbitrage Condition).

For the asset price model defined in [Section 2](https://arxiv.org/html/2512.15071v1#S2 "2. The Model under the Physical Measure (ℙ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") to be free of arbitrage, given a set of market prices of risk γD\gamma\_{D} (for diffusion) and ηj​k\eta\_{jk} (for jumps), the physical drift μ\mu of the asset StS\_{t} must satisfy the following condition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ=r+γD​σ2−1τ​ln⁡(𝔼N​(σ​(1−γD)​τ,τ)​[Mℚ​(X)])\mu=r+\gamma\_{D}\sigma^{2}-\frac{1}{\tau}\ln\left(\mathbb{E}\_{N(\sigma(1-\gamma\_{D})\tau,\tau)}[M\_{\mathbb{Q}}(X)]\right) |  | (5.39) |

where Mℚ​(x)=𝔼ℚ​[eJℚ|Δ​W=x]M\_{\mathbb{Q}}(x)=\mathbb{E}\_{\mathbb{Q}}[e^{J^{\mathbb{Q}}}|\Delta W=x] is the conditional Moment Generating Function (MGF) of the jump factor exp⁡(Jℚ)\exp(J^{\mathbb{Q}}) under the risk-neutral measure ℚ\mathbb{Q}, evaluated at Δ​W=x\Delta W=x:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mℚ​(x)={q1​u​(x)​eν1​uℚ+δ1​u2/2+q1​d​(x)​eν1​dℚ+δ1​d2/2+q10​(x)if ​x<bd​τq2​u​(x)​eν2​uℚ+δ2​u2/2+q2​d​(x)​eν2​dℚ+δ2​d2/2+q20​(x)if ​x>bu​τ1if ​bd​τ≤x≤bu​τM\_{\mathbb{Q}}(x)=\begin{cases}q\_{1u}(x)e^{\nu\_{1u}^{\mathbb{Q}}+\delta\_{1u}^{2}/2}+q\_{1d}(x)e^{\nu\_{1d}^{\mathbb{Q}}+\delta\_{1d}^{2}/2}+q\_{10}(x)&\text{if }x<b\_{d}\sqrt{\tau}\\ q\_{2u}(x)e^{\nu\_{2u}^{\mathbb{Q}}+\delta\_{2u}^{2}/2}+q\_{2d}(x)e^{\nu\_{2d}^{\mathbb{Q}}+\delta\_{2d}^{2}/2}+q\_{20}(x)&\text{if }x>b\_{u}\sqrt{\tau}\\ 1&\text{if }b\_{d}\sqrt{\tau}\leq x\leq b\_{u}\sqrt{\tau}\end{cases} |  | (5.40) |

with the risk-neutral jump probabilities qj​k​(x)q\_{jk}(x) and risk-neutral jump means νj​kℚ\nu\_{jk}^{\mathbb{Q}} defined in [Proposition 4.2](https://arxiv.org/html/2512.15071v1#S4.Thmtheorem2 "Proposition 4.2 (Jumps under ℚ). ‣ 4.2. Jumps under ℚ ‣ 4. The Model under the Risk-Neutral Measure (ℚ) ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"). The expectation 𝔼N​(σ​(1−γD)​τ,τ)​[⋅]\mathbb{E}\_{N(\sigma(1-\gamma\_{D})\tau,\tau)}[\cdot] is taken with respect to a random variable XX distributed as 𝒩​(σ​(1−γD)​τ,τ)\mathcal{N}(\sigma(1-\gamma\_{D})\tau,\tau), which means:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼N​(σ​(1−γD)​τ,τ)​[Mℚ​(X)]=∫−∞∞Mℚ​(x)​12​π​τ​exp⁡(−(x−σ​(1−γD)​τ)22​τ)​dx\mathbb{E}\_{N(\sigma(1-\gamma\_{D})\tau,\tau)}[M\_{\mathbb{Q}}(X)]=\int\_{-\infty}^{\infty}M\_{\mathbb{Q}}(x)\frac{1}{\sqrt{2\pi\tau}}\exp\left(-\frac{(x-\sigma(1-\gamma\_{D})\tau)^{2}}{2\tau}\right)\,\mathrm{d}x |  | (5.41) |

###### Proof.

The detailed derivation provided above, from [Eq. 5.1](https://arxiv.org/html/2512.15071v1#S5.E1 "In 5.1. Deriving the Condition in Full Detail ‣ 5. The No-Arbitrage Condition ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") to [Eq. 5.38](https://arxiv.org/html/2512.15071v1#S5.E38 "In 5.1. Deriving the Condition in Full Detail ‣ 5. The No-Arbitrage Condition ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps"), constitutes the proof of this theorem. The core of the proof lies in relating the martingale condition under ℚ\mathbb{Q} back to an expectation under ℙ\mathbb{P} via LτL\_{\tau}, and then evaluating this ℙ\mathbb{P}-expectation. The derivation shows that if μ\mu satisfies the stated condition, then 𝔼ℙ​[Lτ​St+τ/St]=er​τ\mathbb{E}\_{\mathbb{P}}[L\_{\tau}S\_{t+\tau}/S\_{t}]=e^{r\tau}, which is equivalent to 𝔼ℚ​[St+τ/St]=er​τ\mathbb{E}\_{\mathbb{Q}}[S\_{t+\tau}/S\_{t}]=e^{r\tau}, thus ensuring no arbitrage by [Theorem 3.1](https://arxiv.org/html/2512.15071v1#S3.Thmtheorem1 "Theorem 3.1 (FTAP for Discrete Time - [5]). ‣ 3.1. The Fundamental Theorem of Asset Pricing (FTAP) ‣ 3. The No-Arbitrage Framework ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps").
∎

###### Remark 5.2 (The Guarantee of No Arbitrage).

[Theorem 5.1](https://arxiv.org/html/2512.15071v1#S5.Thmtheorem1 "Theorem 5.1 (The No-Arbitrage Condition). ‣ 5.1. Deriving the Condition in Full Detail ‣ 5. The No-Arbitrage Condition ‣ Arbitrage-Free Pricing with Diffusion-Dependent Jumps") provides the explicit ”guarantee” against arbitrage. If the parameters of the model under the physical measure ℙ\mathbb{P} and the chosen market prices of risk are such that the equation for μ\mu holds, then the constructed measure ℚ\mathbb{Q} is an EMM, ensuring by FTAP that the model is arbitrage-free. Different choices of risk premia would lead to different (but still arbitrage-free) physical drifts μ\mu or, if μ\mu is fixed, imply certain market prices of risk.

## 6. Discussion

The no-arbitrage condition decomposes the required physical drift into three components:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ=r⏟Risk-free rate+γD​σ2⏟Diffusion risk premium−1τ​ln⁡(𝔼N​(σ​(1−γD)​τ,τ)​[Mℚ​(X)])⏟Jump risk adjustment\mu=\underbrace{r}\_{\text{Risk-free rate}}+\underbrace{\gamma\_{D}\sigma^{2}}\_{\text{Diffusion risk premium}}-\underbrace{\frac{1}{\tau}\ln\left(\mathbb{E}\_{N(\sigma(1-\gamma\_{D})\tau,\tau)}[M\_{\mathbb{Q}}(X)]\right)}\_{\text{Jump risk adjustment}} |  | (6.1) |

The jump risk adjustment captures the complex impact of state-dependent jumps:

* •

  If 𝔼​[Mℚ​(X)]>1\mathbb{E}[M\_{\mathbb{Q}}(X)]>1, risk-neutralized jumps have positive expected impact, reducing required drift
* •

  If 𝔼​[Mℚ​(X)]<1\mathbb{E}[M\_{\mathbb{Q}}(X)]<1, jumps have negative expected impact, requiring higher drift compensation
* •

  Different ηj​k\eta\_{jk} allow differentiated pricing of various jump risks

This framework enables:

1. (1)

   Model Consistency: Ensuring that any specific parameterization of the model under the physical measure ℙ\mathbb{P} is internally consistent and does not admit trivial arbitrage strategies.
2. (2)

   Derivative Pricing: By establishing the EMM ℚ\mathbb{Q}, derivative securities can be priced using the principle of risk-neutral valuation, i.e., Pricet=𝔼ℚ​[e−r​(T−t)​PayoffT|ℱt]\text{Price}\_{t}=\mathbb{E}\_{\mathbb{Q}}[e^{-r(T-t)}\text{Payoff}\_{T}|\mathcal{F}\_{t}].
3. (3)

   Risk Management: Providing a deeper understanding of how diffusion and state-dependent jump risks interact and how they are priced by the market. This is essential for developing effective hedging strategies and for accurate risk assessment.

The discrete-time approach facilitates direct implementation while building upon established no-arbitrage principles. Extension to continuous time remains an important avenue for future research.

## 7. Conclusion

This paper rigorously addresses the theoretical challenge of constructing arbitrage-free models with diffusion-dependent jumps. We have formalized and extended previous work into a comprehensive multi-type jump framework that eliminates arbitrage concerns in one-sided models.

The central achievement is deriving the explicit no-arbitrage condition that precisely links the physical drift to all model parameters and market risk premia. This condition provides a guarantee: any model whose parameters satisfy this relationship is, by construction, arbitrage-free.

Future research directions include investigating the continuous-time limit, developing efficient numerical methods for option pricing and calibration, empirical testing against market data, and extensions to multi-asset scenarios or stochastic volatility models.

## References

* [1]

  Black, F. and Scholes, M.:
  The pricing of options and corporate liabilities,
  Journal of Political Economy
  81 (1973), no. 3, 637–654.
* [2]

  Esscher, F.:
  On the probability function in the collective theory of risk,
  Skandinavisk Aktuarietidskrift
  15 (1932), no. 3, 175–195.
* [3]

  Gerber, H. U. and Shiu, E. S. W.:
  Option pricing by Esscher transforms,
  Transactions of the Society of Actuaries
  46 (1994), 99–191.
* [4]

  Girsanov, I. V.:
  On transforming a certain class of stochastic processes by absolutely continuous substitution of measures,
  Theory of Probability & Its Applications
  5 (1960), no. 3, 285–301.
* [5]

  Harrison, J. M. and Pliska, S. R.:
  Martingales and stochastic integrals in the theory of continuous trading,
  Stochastic Processes and their Applications
  11 (1981), no. 3, 215–260
* [6]

  Hassan, M. R. and Nath, B.:
  Stock market forecasting using hidden Markov model: a new approach,
  in: 5th International Conference on Intelligent Systems Design and Applications (ISDA’05), (2005) 192–196.
* [7]

  Merton, R. C.:
  Option pricing when underlying stock returns are discontinuous,
  Journal of Financial Economics
  3 (1976), no. 1-2, 125–144.
* [8]

  Wu, Y. and John, M.:
  A jump-diffusion process for asset price with non-independent jumps,
  Journal of Stochastic Analysis
  3 (2022), no. 4, Article 5.