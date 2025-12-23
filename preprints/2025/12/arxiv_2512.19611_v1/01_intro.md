---
authors:
- Jherek Healy
doc_id: arxiv:2512.19611v1
family_id: arxiv:2512.19611
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2512.19611v1
url_html: https://arxiv.org/html/2512.19611v1
venue: arXiv q-fin
version: 1
year: 2025
---

###### Abstract

The Heston stochastic volatility model is arguably, the most popular stochastic volatility model used to price and risk manage exotic derivatives. In spite of this, it is not
necessarily easy to calibrate to the market and obtain stable exotic option prices with this model. This paper focuses on the vol-of-vol parameter and its relation with the volatility
of volatility index (VVIX) level.
Four different approaches to estimate the VVIX in the Heston model are presented:
two based on the known transition density of the variance, one analytical approximation, and one
based on the Heston PDE which computes the value directly out of the underlying SPX500. Finally we explore their use to improve calibration stability.

###### keywords:

stochastic volatility; Heston; vol-of-vol; VVIX; PDE

\pubvolume\issuenum

1
\articlenumber1
\history
\TitleHeston vol-of-vol and the VVIX
\AuthorJherek Healy
\AuthorNamesJherek Healy

## 1 Introduction

Under the Heston model heston1993closed, the asset XX follows

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | d​X​(t)\displaystyle\mathop{}\!\kern 0.0pt\mathrm{d}X(t) | =(r​(t)−q​(t))​X​(t)​d​t+V​(t)​X​(t)​d​WX​(t),\displaystyle=(r(t)-q(t))X(t)dt+\sqrt{V(t)}X(t)\mathop{}\!\kern 0.0pt\mathrm{d}W\_{X}(t)\,, |  | (1a) |
|  | d​V​(t)\displaystyle\mathop{}\!\kern 0.0pt\mathrm{d}V(t) | =κ​(θ−V​(t))+σ​V​(t)​d​WV​(t),\displaystyle=\kappa\left(\theta-V(t)\right)+\sigma\sqrt{V(t)}\mathop{}\!\kern 0.0pt\mathrm{d}W\_{V}(t)\,, |  | (1b) |

with WXW\_{X} and WVW\_{V} being two Brownian motions with correlation ρ\rho, and r,qr,q the instantaneous growth and dividend rates.

The model, due to its affine properties, leads to an explicit characteristic function, enabling relatively fast pricing of European options. As a consequence, it has been extremely popular in the literature, as well as for real world use in banks,
in order to risk manage the price of exotic derivatives, such as Cliquet options gatheral2011volatility; guillaume2012calibration; feng2019cva.

While it is relatively straightforward to calibrate the model against a set of vanilla options,
it is difficult to obtain a stable, meaningful calibration. Indeed, a change of objective function used in the optimization, or the use of different tactics for calibration,
such as reducing the number of parameters lead to vastly different prices for exotics. This is well described in guillaume2010use, where the two of the model parameters
are set exogenously, v​(0)v(0) is set to the VIX value and θ\theta is set from a moving window estimate of the historical VIX quotes. Some practitioners also fix the speed of mean reversion κ\kappa exogenously. Yet another practice is to forget the consistency across
deals, and calibrate only against a single maturity TT, setting v0=θv\_{0}=\theta and a specific term-structure of κ\kappa (clark2011foreign recommends 5/T5/T).

The VVIX is an index measuring the volatility of the VIX index, which is itself a volatility index. The VVIX thus measures the vol of vol.
We thus may use the VVIX quote as vol-of-vol of the Heston model. But does the vol of vol σ\sigma of the Heston model really corresponds to the VVIX? Does it help stabilizing the calibration in some sense? This paper intends to answer those questions, by analyzing the theoretical VVIX price in the Heston model.

## 2 Approximate VVIX in the Heston model

The VIX index corresponds to the square root of a variance swap replication for a maturity of 30 days, using a
simple discretization scheme, based on liquid vanilla option prices on the SPX500 index:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VIX​(t,t+Δ)2​Δ=−(1−F​(t,t+Δ)K⋆)2+2​∑i=1nwi​VOTM​(Ki,t,t+Δ),\mathrm{VIX}(t,t+\Delta)^{2}\Delta=-\left(1-\frac{F(t,t+\Delta)}{K^{\star}}\right)^{2}+2\sum\_{i=1}^{n}w\_{i}V\_{\textmd{OTM}}(K\_{i},t,t+\Delta)\,, |  | (2) |

where wi=Ki+1−Ki2​Ki2w\_{i}=\frac{K\_{i+1}-K\_{i}}{2K\_{i}^{2}} for i=2,…,n−1i=2,...,n-1, w1=K2−K12​K12w\_{1}=\frac{K\_{2}-K\_{1}}{2K\_{1}^{2}}, wn=Kn−Kn−12​Kn2w\_{n}=\frac{K\_{n}-K\_{n-1}}{2K\_{n}^{2}}, Δ\Delta is 30 days (we will use the ACT/365 convention), VOTM​(Ki,t,T)V\_{\textmd{OTM}}(K\_{i},t,T) is the market price of an out-of-the-money option of strike KiK\_{i} and maturity TT.
K⋆K^{\star} is the first strike KiK\_{i} below F​(t,t+Δ)F(t,t+\Delta).

We will approximate the VIX square by the true value of the expected 30-day variance in the Heston model

|  |  |  |  |
| --- | --- | --- | --- |
|  | VIX​(t,T)2≈1T−t​E⁡[∫tTv​(u)​d​u|t].\mathrm{VIX}(t,T)^{2}\approx\frac{1}{T-t}\operatorname{E}\left[\int\_{t}^{T}v(u)\mathop{}\!\kern 0.0pt\mathrm{d}u\nonscript\;\middle|\nonscript\;t\right]\,. |  | (3) |

In the Heston model, the above expectation is known explicitly and reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | VIXH​(v​(t),T−t)2=1T−t​E⁡[∫tTv​(u)​d​u|t]=(1−1−e−κ​(T−t)κ​(T−t))​θ+1−e−κ​(T−t)κ​(T−t)​v​(t).\mathrm{VIX}\_{H}(v(t),T-t)^{2}=\frac{1}{T-t}\operatorname{E}\left[\int\_{t}^{T}v(u)\mathop{}\!\kern 0.0pt\mathrm{d}u\nonscript\;\middle|\nonscript\;t\right]=\left(1-\frac{1-e^{-\kappa(T-t)}}{\kappa(T-t)}\right)\theta+\frac{1-e^{-\kappa(T-t)}}{\kappa(T-t)}v(t)\,. |  | (4) |

The buyer of a VIX future of maturity TT will receive at maturity, the VIX index value computed from option prices of maturity T+ΔT+\Delta. Using the expected variance as VIX square (Equation [3](https://arxiv.org/html/2512.19611v1#S2.E3 "In 2 Approximate VVIX in the Heston model")) leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | FVIX​(t,T)≈E⁡[VIX​(T,T+Δ)2|t].F\_{\mathrm{VIX}}(t,T)\approx\operatorname{E}\left[\sqrt{\mathrm{VIX}(T,T+\Delta)^{2}}\nonscript\;\middle|\nonscript\;t\right]\,. |  | (5) |

Similarly, the VVIX corresponds to a variance swap replication for a maturity of 30 days, based on the VIX index. Options
on the VIX index of maturity TT, are actually options on a VIX future with maturity TT, and thus measuring the volatility from TT to TT + 30 days, the 30 day forward volatility.
It may be approximated by the log contract value bayer2016pricing:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VVIX​(t,T)2≈2T−t​E⁡[ln⁡FVIX​(T,T)−ln⁡FVIX​(t,T)|t]\mathrm{VVIX}(t,T)^{2}\approx\frac{2}{T-t}\operatorname{E}\left[\ln{F\_{\mathrm{VIX}}(T,T)}-\ln F\_{\mathrm{VIX}}(t,T)\nonscript\;\middle|\nonscript\;t\right] |  | (6) |

For a CIR process, the transition law is known explicitly broadie2006exact and reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t)=σ2​(1−e−κ​(t−u))4​κ​χd′⁣2​(4​κ​e−κ​(t−u)σ2​(1−e−κ​(t−u))​v​(u)),v(t)=\frac{\sigma^{2}\left(1-e^{-\kappa(t-u)}\right)}{4\kappa}\chi\_{d}^{\prime 2}\left(\frac{4\kappa e^{-\kappa(t-u)}}{\sigma^{2}\left(1-e^{-\kappa(t-u)}\right)}v(u)\right)\,, |  | (7) |

where χd′⁣2\chi\_{d}^{\prime 2} denotes the non-central chi-squared distribution with dd degrees of freedom where d=4​κ​θσ2d=\frac{4\kappa\theta}{\sigma^{2}}.

Let C1=σ2​(1−e−κ​Δ)4​κC\_{1}=\frac{\sigma^{2}\left(1-e^{-\kappa\Delta}\right)}{4\kappa}, ϕt,u​(z)\phi\_{t,u}(z) be the probability density function of the non-central chi-squared distribution, combining Equation [4](https://arxiv.org/html/2512.19611v1#S2.E4 "In 2 Approximate VVIX in the Heston model") with Equation [6](https://arxiv.org/html/2512.19611v1#S2.E6 "In 2 Approximate VVIX in the Heston model"), we may thus compute the VVIX using a one-dimensional integration.

|  |  |  |  |
| --- | --- | --- | --- |
|  | VVIX​(t,T)2≈2T−t​∫0∞(ln⁡VIXH​(v​(T)=C1​z,Δ)2−ln⁡FVIX​(t,T))​ϕt,T​(z)​d​z\mathrm{VVIX}(t,T)^{2}\approx\frac{2}{T-t}\int\_{0}^{\infty}(\ln\sqrt{\mathrm{VIX}\_{H}(v(T)=C\_{1}z,\Delta)^{2}}-\ln F\_{\mathrm{VIX}}(t,T))\phi\_{t,T}(z)\mathop{}\!\kern 0.0pt\mathrm{d}z |  | (8) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | FVIX​(t,T)=∫0∞VIXH​(v​(T)=C1​z,Δ)2​ϕt,T​(z)​d​zF\_{\mathrm{VIX}}(t,T)=\int\_{0}^{\infty}\sqrt{\mathrm{VIX}\_{H}(v(T)=C\_{1}z,\Delta)^{2}}\phi\_{t,T}(z)\mathop{}\!\kern 0.0pt\mathrm{d}z |  | (9) |

where the expectation inside each integral is given explicitly by Equation [4](https://arxiv.org/html/2512.19611v1#S2.E4 "In 2 Approximate VVIX in the Heston model"). The VIX future formula corresponds to the one given in zhang2006vix.

When the Feller condition κ​θ≥σ2\kappa\theta\geq\sigma^{2} does not hold, the integral is more challenging to calculate due to the explosion at zero. We found only minor discrepancies using Julia’s QuadGK111<https://github.com/JuliaMath/QuadGK.jl>.
Alternatively, zhu2012analytical present a Fourier based approach to compute the expectation, using the characteristic function of the variance process, which may be more stable numerically and better performing.

In practice, the VVIX is calculated using only a discrete set of liquid options on the VIX:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VVIX​(t,T)2​(T−t)=−(1−FVIX​(t,T)KV⁣⋆)2+∑i=1nwi​VO​T​M​(KiV,t,T)\mathrm{VVIX}(t,T)^{2}(T-t)=-\left(1-\frac{F\_{\mathrm{VIX}}(t,T)}{K^{V\star}}\right)^{2}+\sum\_{i=1}^{n}w\_{i}V\_{OTM}(K^{V}\_{i},t,T) |  | (10) |

where wi=Ki+1V−KiV2​KiV2w\_{i}=\frac{K^{V}\_{i+1}-K^{V}\_{i}}{2{K^{V}\_{i}}^{2}} for i=2,…,n−1i=2,...,n-1, w1=K2V−K1V2​K1V2w\_{1}=\frac{K^{V}\_{2}-K^{V}\_{1}}{2{K^{V}\_{1}}^{2}}, wn=KnV−Kn−1V2​KnV2w\_{n}=\frac{K^{V}\_{n}-K^{V}\_{n-1}}{2{K^{V}\_{n}}^{2}},
KV⁣⋆K^{V\star} is the first strike KiVK^{V}\_{i} below FV​I​XF\_{VIX}.

The price of VIX option can be computed using a one-dimensional integration, very much like for the continous VVIX approximation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(K,t,T)=∫0∞max⁡(η​VIXH​(v​(T)=C1​z,Δ)2−η​K,0)​ϕt,T​(z)​d​zV(K,t,T)=\int\_{0}^{\infty}\max\left(\eta\sqrt{\mathrm{VIX}\_{H}(v(T)=C\_{1}z,\Delta)^{2}}-\eta K,0\right)\phi\_{t,T}(z)\mathop{}\!\kern 0.0pt\mathrm{d}z |  | (11) |

with η=1\eta=1 for a call and η=−1\eta=-1 for a put option. A practical implementation will truncate the integration at the level zz where the intrinsic value is zero in order to keep the integrand smooth.

If we assume that the VIX option prices are given by Equation [11](https://arxiv.org/html/2512.19611v1#S2.E11 "In 2 Approximate VVIX in the Heston model"), the continuous approximation (Equation [8](https://arxiv.org/html/2512.19611v1#S2.E8 "In 2 Approximate VVIX in the Heston model")) is remarkably close to the more exact VVIX replication, as long as the lowest replication strike is small enough.

A typical strike range is [10,65][10,65] for a VIX=14. In particular, the lowest strike is not that small
compared to the VIX value. This creates a bias in the VVIX value, which may be particularly pronounced if the VVIX is large (Table [1](https://arxiv.org/html/2512.19611v1#S2.T1 "Table 1 ‣ 2 Approximate VVIX in the Heston model") with the first VIX option strike K1V=5K^{V}\_{1}=5 or K1V=10K^{V}\_{1}=10).

Table 1: Effect of the VIX option strike range truncation on the estimated VVIX value, compared to the log contract price, for different Heston parameters.

| Set | Heston parameters | | | | | FVIXF\_{\mathrm{VIX}} | Log | Replication | | Simple |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | v0v\_{0} | κ\kappa | θ\theta | ρ\rho | σ\sigma |  | contract | K1V=5K^{V}\_{1}=5 | K1V=10K^{V}\_{1}=10 |  |
| I | 0.0236 | 0.2575 | 0.0849 | -0.7513 | 0.3150 | 15.4 | 105.4 | 105.2 (0.2%) | 100.0 (5.1%) | 98 |
| II | 0.0313 | 0.75 | 0.0678 | -0.7663 | 0.7593 | 16.0 | 218.5 | 218.4 (0.0%) | 193.0 (11.5%) | 204 |
| III | 0.0371 | 3.4490 | 0.0497 | -0.7558 | 1.7522 | 15.9 | 231.8 | 229.8 (0.9%) | 225.9 (2.5%) | 382 |
| IV | 0.0538 | 0.6431 | 0.0880 | -0.7010 | 0.6159 | 22.2 | 143.7 | 143.8 | 139.8 | 127 |
| V | 0.0440 | 0.75 | 0.0998 | -0.7410 | 0.7654 | 19.9 | 184.8 | 184.8 | 176.8 | 171 |
| VI | 0.0397 | 4.6705 | 0.0696 | -0.7149 | 2.0640 | 18.9 | 196.7 | 196.5 | 196.7 | 376 |

We also derive a simple approximation in Appendix [A](https://arxiv.org/html/2512.19611v1#A1 "Appendix A Simple approximation for the VVIX in Heston"), which does not require any numerical integral calculation, but is not particularly accurate, especially for large speeds of mean reversion κ\kappa (column named "Simple" of Table [1](https://arxiv.org/html/2512.19611v1#S2.T1 "Table 1 ‣ 2 Approximate VVIX in the Heston model")).

## 3 Exact VVIX with the Heston PDE

The VIX itself is also a discrete replication of out-of-the-money 30-days vanilla options on SPX500, which is not taken into account in the single replication approach presented in the previous section.
In general, there is much less issue with the lowest strike, and SPX500 options are liquid across a wider range of strikes.
A PDE approach allow us to compute the VVIX based SPX500 options only,
by combining the discrete replication of the VVIX and of the VIX. The full Heston model is used, not only the variance process, there is no approximation involved. Furthermore, the technique is applicable to any stochastic volatility model.

The Heston PDE for the price of a financial derivative ff reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂f∂t=v​x22​∂2f∂x2+ρ​σ​x​v​∂2f∂x​∂v+σ2​v2​∂2f∂v2+(r−q)​x​∂f∂x+κ​(θ−v)​∂f∂v−rC​f,\frac{\partial f}{\partial t}=\frac{vx^{2}}{2}\frac{\partial^{2}f}{\partial x^{2}}+\rho\sigma xv\frac{\partial^{2}f}{\partial x\partial v}+\frac{\sigma^{2}v}{2}\frac{\partial^{2}f}{\partial v^{2}}+(r-q)x\frac{\partial f}{\partial x}+\kappa(\theta-v)\frac{\partial f}{\partial v}-r\_{C}f\,, |  | (12) |

for 0≤t≤T+Δ0\leq t\leq T+\Delta, x>0x>0, v>0v>0. We allowed for a distinct discounting rate rCr\_{C}, which will be set to zero to obtain undiscounted prices of ff.
We use the boundary conditions and central finite difference discretization described in lefloc2023instabilities; lefloch2021pricing.

We consider ff to be of dimension 2​n2n where nn is the number of strikes used in the replication. The first nn are call options and the next nn are put options.

### 3.1 Initial condition

The initial condition at t=T+Δt=T+\Delta reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | fi​(x,v,T+Δ)=max⁡(x−Ki,0),fn+i​(x,v,T+Δ)=max⁡(Ki−x,0),\displaystyle f\_{i}(x,v,T+\Delta)=\max(x-K\_{i},0)\,,\quad f\_{n+i}(x,v,T+\Delta)=\max(K\_{i}-x,0)\,, |  | (13) |

for x≥0x\geq 0, v≥0v\geq 0, i=1,…,ni=1,...,n.

### 3.2 Continuity condition

At t=Tt=T, we calculate the VIX options in three steps:

1. (i)

   We compute the SPX500 forward estimate at each point. To do so, we perform a linear regression on the call-put parity relation, that is we solve
   𝑯T​𝑯​𝜷=𝑯T​𝑮\bm{H}^{T}\bm{H}\bm{\beta}=\bm{H}^{T}\bm{G}
   where 𝑯\bm{H} is a (n,2)-matrix with Hi,1=KiH\_{i,1}=K\_{i}, Hi,2=1H\_{i,2}=1 and 𝑮\bm{G} is a nn-dimensional vector with Gi=fi​(x,v,T)−fn+i​(x,v,T){G}\_{i}=f\_{i}(x,v,T)-f\_{n+i}(x,v,T). Then the forward at each point is F​(x,v)=β2​(x,v)F(x,v)=\beta\_{2}(x,v).
2. (ii)

   We compute the VIX price at each point. We apply Equation [2](https://arxiv.org/html/2512.19611v1#S2.E2 "In 2 Approximate VVIX in the Heston model"), using FF, fif\_{i} and fn+if\_{n+i}. This leads to VIX​(x,v)\mathrm{VIX}(x,v).
3. (iii)

   We update ff to be the value of VIX options for each strike:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | fi​(x,v,T)=max⁡(VIX​(x,v)−KiV,0),fn+i​(x,v,T)=max⁡(KiV−VIX​(x,v),0),\displaystyle f\_{i}(x,v,T)=\max\left(\mathrm{VIX}(x,v)-K^{V}\_{i},0\right)\,,\quad f\_{n+i}(x,v,T)=\max\left(K^{V}\_{i}-\mathrm{VIX}(x,v),0\right)\,, |  | (14) |

   for x≥0x\geq 0, v≥0v\geq 0, i=1,…,ni=1,...,n.

At t=0t=0 we end up with the values of VIX options replicating the VVIX, we then apply (i) and (ii) to those in order to obtain the VVIX at each point. We then use a bicubic spline to find the VVIX value at the current SPX500 spot price and the Heston initial variance v​(0)v(0).

## 4 Numerical Results

### 4.1 Calibration

The calibration of the Heston model consists in finding the parameters which minimize the difference between the model option prices 𝑽^\hat{\bm{V}} and the market option prices 𝑽\bm{V}. There are many subtleties in practice:

* •

  Which market option prices do we include? Do we include all, or only liquid prices?
* •

  The model is also often calibrated against a prior representation of market option prices, typically an implied volatility matrix corresponding to a fixed range of maturities and strikes. This prior representation will typically not have any liquidity information.
* •

  Should we select call option prices, put option prices or only out-of-the-money option prices?
* •

  Which measure of difference do we choose? ℓ∞\ell^{\infty}, the maximum absolute error or ℓ2\ell^{2}, the sum of square differences? Should it be weighted in some ways? Should it be applied to implied volatilities or to raw prices?

We will adopt the ℓ2\ell^{2} norm since it enables the use of fast local minimizers such as the Gauss-Newton of klare2013gn. As initial guess, we use the result of a global minimizer storn1997differential.

Let TiT\_{i}, KiK\_{i} be the maturities and strikes for each of the nn market options considered, the various choices may be reduced to minimize a sum of weighted square differences in out-of-the-money option prices:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝃calibrated=min𝝃⁡[∑i=1nwi2​(V^​(Ki,Ti,𝝃)−V​(Ki,Ti))2],\bm{\xi}\_{\textmd{calibrated}}=\min\_{\bm{\xi}}\left[\sum\_{i=1}^{n}w\_{i}^{2}\left(\hat{V}(K\_{i},T\_{i},\bm{\xi})-V(K\_{i},T\_{i})\right)^{2}\right]\,, |  | (15) |

where 𝝃\bm{\xi} represent the vector of parameters to calibrate. For the full Heston model, 𝝃=(v0,κ,θ,ρ,σ)\bm{\xi}=(v\_{0},\kappa,\theta,\rho,\sigma).

If we let 𝒘=1\bm{w}=1, which is often used in the literature, the very out-of-the-money option prices, where the liquidity is not always good, will effectively be ignored as their price will be negligible compared to the closer to the money option prices. Furthermore, it will put more emphasis on longer maturities than on shorter ones.

We may also let wi=1B​(0,Ti)w\_{i}=\frac{1}{B(0,T\_{i})} where B​(0,Ti)B(0,T\_{i}) is the discount factor to maturity TiT\_{i}, which is equivalent to working with undiscounted prices and 𝒘=1\bm{w}=1.

If we let wi=1min⁡(VegaF,Vega​(Ki,Ti))w\_{i}=\frac{1}{\min\left(\mathrm{Vega}\_{F},\mathrm{Vega}(K\_{i},T\_{i})\right)}, where

|  |  |  |
| --- | --- | --- |
|  | Vega=B​(0,Ti)​F​(0,Ti)​ϕ​(1σi​Ti​ln⁡F​(0,Ti)Ki+12​σi​Ti)​Ti\mathrm{Vega}=B(0,T\_{i})F(0,T\_{i})\phi\left(\frac{1}{\sigma\_{i}\sqrt{T\_{i}}}\ln\frac{F(0,T\_{i})}{K\_{i}}+\frac{1}{2}\sigma\_{i}\sqrt{T\_{i}}\right)\sqrt{T\_{i}} |  |

is the market Black-Scholes Vega, and F​(0,Ti)=X​(0)​e∫0Tir​(s)−q​(s)​d​sF(0,T\_{i})=X(0)e^{\int\_{0}^{T\_{i}}r(s)-q(s)\mathop{}\!\kern 0.0pt\mathrm{d}s} is the forward to maturity TiT\_{i}, we end up with a normalized difference which is close to the error in implied volatilities (see lefloch2019model1 for a justification). In addition, the floor VegaF\mathrm{Vega}\_{F} allows to relax the fitting of illiquid out-of-the-money option whose Vegas are typically very small. We will use VegaF=10−2\mathrm{Vega}\_{F}=10^{-2} in our numerical tests.

Table [1](https://arxiv.org/html/2512.19611v1#S2.T1 "Table 1 ‣ 2 Approximate VVIX in the Heston model") presents the resulting parameters for different choices of 𝒘\bm{w} when we calibrate towards SPX500 options as of October 8, 2024: Set I is equal weights, Set III is inverse vega, and Set II is inverse vega with a exogenous κ=0.75\kappa=0.75. Set IV, V, VI correspond to the calibrations as of March 15, 2021.
We notice that depending on the choice of objective function, the calibrated parameters lead to vastly different levels of VVIX, some of which are not compatible with the current market conditions. The VVIX trades mostly between 65 and 200, and typically hovered around 100 in 2023 and 2024. On October 8, 2024, it was 114.82, and on March 15, 2021, it was 110.49.

This suggests that the log contract formula (or even the simple approximation) may be good enough to calibrate Heston. We will however firstly estimate the impact of the true double replication on the VVIX estimate, in comparison to the single replication.

### 4.2 PDE

We use the Runge-Kutta-Gegenbauer (RKG) second-order explicit finite-difference method skaras2021super; lefloc2023instabilities to price the double replication of the VVIX on the Heston PDE. As of December 2024, the SPX is close to 6000 and the strike range for liquid SPX options of maturity 2 months lies between 2500 and 8000, which corresponds to a range from 40% to 140% of the spot price. We will use this replication range in our numerical tests.

We consider the two sets of parameters with largest vol-of-vol σ\sigma, and price the VVIX, successively doubling the grid density to show the convergence (Table [2](https://arxiv.org/html/2512.19611v1#S4.T2 "Table 2 ‣ 4.2 PDE ‣ 4 Numerical Results")). We increased the boundary in the asset dimension XX to six standard deviations in order to avoid perturbations related to the boundary.

Table 2: VVIX price by double replication in the Heston PDE, discretized with the RKG scheme, doubling the grid size. NN is the number of time-steps, MM the number of steps in the XX axis, LL the number of steps in the vv axis.

| N | M | L | Set II | | Set III |
| --- | --- | --- | --- | --- | --- |
|  |  |  | K1V=5K\_{1}^{V}=5 | K1V=10K\_{1}^{V}=10 | K1V=10K\_{1}^{V}=10 |
| 25 | 12 | 16 | 197.96 | 185.08 | 217.04 |
| 50 | 25 | 30 | 211.54 | 189.63 | 225.26 |
| 100 | 50 | 60 | 214.11 | 191.07 | 223.89 |
| 200 | 100 | 120 | 217.53 | 192.62 | 224.23 |
| 400 | 200 | 240 | 218.00 | 192.78 | 224.66 |

The VVIX double replication also enables us to evaluate the effects of truncating the range of SPX option strikes used in the VIX replication. As expected, the difference between the PDE double-replication values and the single replication (Table [1](https://arxiv.org/html/2512.19611v1#S2.T1 "Table 1 ‣ 2 Approximate VVIX in the Heston model")) is small, because the SPX500 options are liquid on a wide enough strike range.

### 4.3 VVIX level versus vol-of-vol

We have seen in Tables [1](https://arxiv.org/html/2512.19611v1#S2.T1 "Table 1 ‣ 2 Approximate VVIX in the Heston model"), [2](https://arxiv.org/html/2512.19611v1#S4.T2 "Table 2 ‣ 4.2 PDE ‣ 4 Numerical Results") that the vol-of-vol is different from the VVIX level, a vol of vol of 30% may translate into a VVIX of 100%.
In Figure [1](https://arxiv.org/html/2512.19611v1#S4.F1 "Figure 1 ‣ 4.3 VVIX level versus vol-of-vol ‣ 4 Numerical Results"), we take a closer look at how the VVIX evolves when we vary the vol-of-vol but keep the other Heston parameters constant, based on the parameters for Set I and Set III.

![Refer to caption](x1.png)


(a)

![Refer to caption](x2.png)


(b)

Figure 1: VVIX varying the vol-of-vol but keeping the other parameters constant.

The approximation is inaccurate as soon as the vol-of-vol is larger than 50%. In Set I, which has a small κ\kappa, the difference between the log-contract and the replication is large when the VVIX estimate is larger than 200. This is not the case for Set III, where the κ\kappa is ten times larger. For Set III, the VVIX seems to reach a maximum of around 240. In particular, a vol-of-vol over 125% leads to a VVIX between 200 and 230. On Set I, the same VVIX range is covered by a vol-of-vol over 70%. Thus, the vol-of-vol is not the single factor that will have a impact on the VVIX, the κ\kappa must be considered as well.

![Refer to caption](x3.png)


(a)

![Refer to caption](x4.png)


(b)

Figure 2: VVIX varying the vol-of-vol and recalibrating the other parameters against the market.

It is interesting to look at the same example, but with a recalibration of the other parameters (beside the σ\sigma) to the market. We calibrate to all expiries, even though the VVIX is actually really sensitive to maturities up to two months.
Figure [2](https://arxiv.org/html/2512.19611v1#S4.F2 "Figure 2 ‣ 4.3 VVIX level versus vol-of-vol ‣ 4 Numerical Results") shows that the VVIX of 200 is reached at around σ=75%\sigma=75\% for the two objective functions considered (corresponding to Sets I and IV). The recalibration appears to make the choice of σ\sigma much more impactful.

### 4.4 Calibration using VVIX

Two different strategies are possible include the VVIX in the Heston calibration:

1. (a)

   An additional term in the least squares fit corresponding to a weighted difference between the model VVIX and the market VVIX.
2. (b)

   Or remove the vol-of-vol σ\sigma from the set 𝝃\bm{\xi} and solve for it from the market value and the other Heston parameters.

Strategy (a) is more flexible, but requires to find a practical value for the VVIX associated weight. Strategy (b) does not have a weight to define and may decrease the calibration time. It will however require to be able to solve, meaning to have a monotonic function of σ\sigma. This excludes, a priori the replication approach (see Figure [1](https://arxiv.org/html/2512.19611v1#S4.F1 "Figure 1 ‣ 4.3 VVIX level versus vol-of-vol ‣ 4 Numerical Results")).

It turns out that strategy (a) fails in many situations, even with the log contract VVIX valuation, also because of the non-monotonic relation with σ\sigma (Figure [2](https://arxiv.org/html/2512.19611v1#S4.F2 "Figure 2 ‣ 4.3 VVIX level versus vol-of-vol ‣ 4 Numerical Results")): it may push σ\sigma very high and κ\kappa low. Even if the κ\kappa is fixed exogenously, then the θ\theta may be pushed unrealistically high. Both θ\theta and κ\kappa would be needed to be set exogenously to stabilize the calibration. As illustrating example, we calibrate Heston with inverse Vega weights and set the VVIX level to 200.0 with a weights of 0.1, using the log contract approach to match the VVIX, as of October 8, 2024. We obtain v0=0.04,κ=7.17,θ=0.05,ρ=−0.76,σ=3.09v\_{0}=0.04,\kappa=7.17,\theta=0.05,\rho=-0.76,\sigma=3.09. Both σ\sigma and κ\kappa are significantly larger than without the VVIX observation. The satisfying solution would be v0=0.03,κ=0.95,θ=0.06,ρ=−0.79,σ=0.71v\_{0}=0.03,\kappa=0.95,\theta=0.06,\rho=-0.79,\sigma=0.71. With the replication approach strategy (a) fails even more often and more significantly. It however works satisfyingly with the simple approximation. The main cause is the non monotonicity of the VVIX theoretical price as a function of the vol-of-vol in the Heston model. One would need some additional constraint to put emphasis on the solution with lower vol-of-vol compared to the one with higher vol of vol. In a sense, this is precisely what the simple approximation accomplishes.

In strategy (b), a simple Newton solver to find σ\sigma for a given VVIX level worked well enough and the calibration was 50% faster than with strategy (a).

Table 3: Heston calibration on vanilla option prices and VVIX using strategy (b). Sets I and III correspond to uniform and inverse Vega weights calibration as of October 8, 2024. Sets IV and VI are as of March 15, 2021.

| Set | Simple | Log | Replication | Heston parameters | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | approx. | contract | K1V=10K^{V}\_{1}=10 | v0v\_{0} | κ\kappa | θ\theta | ρ\rho | σ\sigma |
| I | 114.82 | 126.7 | 115.7 | 0.024 | 0.317 | 0.081 | -0.724 | 0.374 |
| III | 114.82 | 127.1 | 118.5 | 0.028 | 0.426 | 0.069 | -0.842 | 0.406 |
| I | 200.00 | 210.7 | 179.8 | 0.026 | 0.650 | 0.072 | -0.672 | 0.683 |
| III | 200.00 | 207.1 | 185.5 | 0.032 | 1.045 | 0.058 | -0.788 | 0.759 |
| IV | 110.49 | 122.6 | 119.8 | 0.052 | 0.502 | 0.092 | -0.703 | 0.522 |
| VI | 110.49 | 118.8 | 116.3 | 0.042 | 0.658 | 0.086 | -0.758 | 0.486 |
| IV | 200.00 | 210.9 | 204.1 | 0.062 | 1.328 | 0.080 | -0.697 | 1.049 |
| VI | 200.00 | 188.3 | 183.8 | 0.043 | 1.688 | 0.076 | -0.736 | 0.939 |

Table [3](https://arxiv.org/html/2512.19611v1#S4.T3 "Table 3 ‣ 4.4 Calibration using VVIX ‣ 4 Numerical Results") shows a reduction of the discrepancy between the different choices of weights, significantly so when the VVIX level is below 150, and less so for a VVIX around 200.

## 5 Conclusion

We have explored the use of the VVIX index for calibration in an attempt to solve the major issue of inconsistent calibration and make the Heston model more practical.

The VVIX index value can not be used directly as vol-of-vol of the Heston model. The vol-of-vol is typically smaller
than the VVIX for moderate values of the VVIX. The truncation(s) involved in the VVIX replication(s) does not have a large impact on the real VVIX value, with the exception of the combination of a low VIX (below 15) and large VVIX (above 150) where the difference can reach a 10%.

Using the replication price or even the log contract price as part of the calibration proved to be challenging, because the relationship between the vol-of-vol and the theoretical VVIX value is not monotonic. A simple analytical approximation was however found to work well, and allowed to reduce the discrepancy due to the various choices in the calibration significantly. This approximation is not so accurate for large vol-of-vol values. The search for better approximation of the VVIX under Heston may be worthwhile.

We may also wonder if the selection towards lower speeds of mean reversion and lower vol-of-vol due to the approximation is really justified in the context of a large market VVIX (such as 200%).

Finally, we would expect a more direct relationship for models with a lognormal stochastic volatility, such as the SABR or Bergomi models.

\externalbibliography

yes
\appendixtitlesno

## Appendix A Simple approximation for the VVIX in Heston

We have

|  |  |  |
| --- | --- | --- |
|  | Var[VIXH​(v​(T),Δ)2]=E[VIXH(v(T),Δ)2|t]−E[VIXH​(v​(T),Δ)2]2\mathrm{Var}\left[\sqrt{\mathrm{VIX}\_{H}(v(T),\Delta)^{2}}\right]=\operatorname{E}\left[\mathrm{VIX}\_{H}(v(T),\Delta)^{2}\nonscript\;\middle|\nonscript\;t\right]-\operatorname{E}\left[\sqrt{\mathrm{VIX}\_{H}(v(T),\Delta)^{2}}\right]^{2} |  |

Then we use a Taylor expansion of VIXH​(v​(T),Δ)2\sqrt{\mathrm{VIX}\_{H}(v(T),\Delta)^{2}} around E⁡[VIXH​(v​(T),Δ)2|t]\operatorname{E}[\mathrm{VIX}\_{H}(v(T),\Delta)^{2}\nonscript\;|\nonscript\;t] to obtain:

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
| --- | --- | --- |
|  |  |  |

ThisleadstoVar[VIXH(v(T),Δ)2]≈E[(VIXH(v(T),Δ)2-E[VIXH(v(T),Δ)2|t])2|t]4(E[VIXH(v(T),Δ)2|t])

Ononehand,wehave

gatheral2011volatility

|  |  |  |  |
| --- | --- | --- | --- |
|  | E⁡[v​(T)|t]=(v​(t)−θ)​e−κ​(T−t)+θ\operatorname{E}[v(T)\nonscript\;|\nonscript\;t]=(v(t)-\theta)e^{-\kappa(T-t)}+\theta |  | (16) |

AndwethusknowE

[VIX\_H(v(T),Δ)^2 | t]e​x​p​l​i​c​i​t​l​y​u​s​i​n​g​E​q​u​a​t​i​o​n​[16](https://arxiv.org/html/2512.19611v1#A1.E16 "In Appendix A Simple approximation for the VVIX in Heston")​i​n​E​q​u​a​t​i​o​n​[4](https://arxiv.org/html/2512.19611v1#S2.E4 "In 2 Approximate VVIX in the Heston model").O​n​t​h​e​o​t​h​e​r​h​a​n​d,t​h​e​d​y​n​a​m​i​c​o​fexplicitlyusingEquation\ref{eqn:eVT}inEquation\ref{eqn:vix\_heston}.\par Ontheotherhand,thedynamicofU=v^2u​n​d​e​r​H​e​s​t​o​n​r​e​a​d​s​(17)Equation 1717=⁢dU+⁢2κ(-+θσ2U)U⁢dt⁢2σ2U/34⁢dWv,​w​h​i​c​h​l​e​a​d​s​t​o​(18)Equation 1818=E[|⁢v2(T)t][+σ2⁢2κθ⁢e-⁢κ(-Tt)(-+σ2⁢2κθv0)]2​a​s​t​h​e​e​x​p​e​c​t​a​t​i​o​n​r​e​m​o​v​e​s​t​h​e​s​t​o​c​h​a​s​t​i​c​t​e​r​munderHestonreads\begin{equation}\mathop{}\!\kern 0.0pt\mathrm{d}U=2\kappa(\theta+\sigma^{2}-\sqrt{U})\sqrt{U}\mathop{}\!\kern 0.0pt\mathrm{d}t+2\sigma^{2}U^{3/4}\mathop{}\!\kern 0.0pt\mathrm{d}W\_{v}\,,\end{equation}whichleadsto\begin{equation}\operatorname{E}[v^{2}(T)\nonscript\;|\nonscript\;t]=\left[\frac{\sigma^{2}}{2\kappa}+\theta+e^{-\kappa(T-t)}\left(\frac{\sigma^{2}}{2\kappa}+\theta-v\_{0}\right)\right]^{2}\end{equation}astheexpectationremovesthestochastictermσ^2 U^3/4 ​dW\_vs​i​n​c​e​i​t​i​s​a​m​a​r​t​i​n​g​a​l​e​w​i​t​h​z​e​r​o​e​x​p​e​c​t​a​t​i​o​n.W​e​u​s​e​E​q​u​a​t​i​o​n​s​[16](https://arxiv.org/html/2512.19611v1#A1.E16 "In Appendix A Simple approximation for the VVIX in Heston")​a​n​d​[18](https://arxiv.org/html/2512.19611v1#A1.E18 "In Appendix A Simple approximation for the VVIX in Heston")​i​n​t​h​e​s​q​u​a​r​e​o​f​E​q​u​a​t​i​o​n​[4](https://arxiv.org/html/2512.19611v1#S2.E4 "In 2 Approximate VVIX in the Heston model"),t​o​o​b​t​a​i​nsinceitisamartingalewithzeroexpectation.\par WeuseEquations\ref{eqn:eVT}and\ref{eqn:eV2T}inthesquareofEquation\ref{eqn:vix\_heston},toobtainE[VIX\_H(v(T),Δ)^4 | t].ThenasimplelognormalapproximationfortheVVIXreads(19)Equation 1919=VVIXA/ln(+1⁢Var[⁢VIXH(⁢v(T),Δ)]E[|⁢VIXH(⁢v(T),Δ)2t])Δ..\par\par ThenasimplelognormalapproximationfortheVVIXreads\begin{equation}\mathrm{VVIX}\_{A}=\sqrt{\ln\left(1+\frac{\mathrm{Var}\left[\mathrm{VIX}\_{H}(v(T),\Delta)\right]}{\operatorname{E}[\mathrm{VIX}\_{H}(v(T),\Delta)^{2}\nonscript\;|\nonscript\;t]}\right)}/\sqrt{\Delta}\,.\end{equation}\par\par\par\par\@add@PDF@RDFa@triples\par