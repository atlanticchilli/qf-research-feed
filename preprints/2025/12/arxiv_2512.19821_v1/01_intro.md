---
authors:
- Fabien Le Floc'h
doc_id: arxiv:2512.19821v1
family_id: arxiv:2512.19821
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 The major stochastic (local) volatility models
url_abs: http://arxiv.org/abs/2512.19821v1
url_html: https://arxiv.org/html/2512.19821v1
venue: arXiv q-fin
version: 1
year: 2025
---

###### Abstract

Based on the existing literature, this article presents the different ways of choosing the parameters of stochastic volatility models in general, in the context of pricing financial derivative contracts. This includes the use of stochastic volatility inside stochastic local volatility models.

###### keywords:

implied volatility, stochastic volatility, stochastic local volatility, model calibration

\pubvolume

xx
\issuenum1
\articlenumber1
\history
\TitleHow to choose my stochastic volatility parameters? A review
\AuthorFabien Le Floc’h
\AuthorNamesFabien Le Floc’h
\corresCorrespondence: fabien@2ipi.com

## 1 The major stochastic (local) volatility models

The calibration practices presented in this paper are applicable to the most common stochastic volatility model. Let us recap the main models:

* •

  In the Heston stochastic local volatility model, an asset FF is described by the following system of stochastic differential equations Heston ([1993](https://arxiv.org/html/2512.19821v1#bib.bib17)):

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | | | | |
  |  | d​FF\displaystyle\frac{\mathop{}\!\kern 0.0pt\mathrm{d}F}{F} | =v​L​(F,t)​d​WF,\displaystyle=\sqrt{v}L(F,t)\mathop{}\!\kern 0.0pt\mathrm{d}W\_{F}\,, |  | (1a) |
  |  | d​v\displaystyle\mathop{}\!\kern 0.0pt\mathrm{d}v | =κ​(θ−v)​d​t+σ​v​d​Wv\displaystyle=\kappa(\theta-v)\mathop{}\!\kern 0.0pt\mathrm{d}t+\sigma\sqrt{v}\mathop{}\!\kern 0.0pt\mathrm{d}W\_{v} |  | (1b) |

  with d​WF​d​Wv=ρ​d​t\mathop{}\!\kern 0.0pt\mathrm{d}W\_{F}\mathop{}\!\kern 0.0pt\mathrm{d}W\_{v}=\rho\mathop{}\!\kern 0.0pt\mathrm{d}t. For an equity of spot SS, and maturity TT, FF represents the forward to maturity F​(t)=S​(t)​e(r−q)​(T−t)F(t)=S(t)e^{(r-q)(T-t)} with rr the relevant interest rate, and qq the dividend yield. The function L​(S,t)L(S,t) is an additional local volatility component (also called leverage function). In the pure stochastic volatility model, L=1L=1. Some issues of the Heston model are the not so realistic variance distribution when the Feller condition is not verified (which is common when applied with L=1L=1 in practice), the relatively poor fit due to the limited number of parameters, and the lack of flexibility in the forward variance dynamic. Its main advantage is to have an affine characteristic function, which allows for an efficient calculation of vanilla option prices. The pure stochastic volatility fit can be greatly increased through the use of piecewise-constant vol-of-variance σ\sigma and correlation ρ\rho in time, which is usually accompanied by the choice v​(0)=1=θv(0)=1=\theta and some exogenously fixed speed of mean reversion κ\kappa (Hagan et al., [2018](https://arxiv.org/html/2512.19821v1#bib.bib15)).
* •

  The Double-Heston model of Christoffersen et al. ([2009](https://arxiv.org/html/2512.19821v1#bib.bib7)) is more flexible with regards to the fit and the dynamic. The asset follows

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | | | | |
  |  | d​FF\displaystyle\frac{\mathop{}\!\kern 0.0pt\mathrm{d}F}{F} | =v1​L​(F,t)​d​WF1+v2​L​(F,t)​d​WF2,\displaystyle=\sqrt{v\_{1}}L(F,t)\mathop{}\!\kern 0.0pt\mathrm{d}W\_{F\_{1}}+\sqrt{v\_{2}}L(F,t)\mathop{}\!\kern 0.0pt\mathrm{d}W\_{F\_{2}}\,, |  | (2a) |
  |  | d​v1\displaystyle\mathop{}\!\kern 0.0pt\mathrm{d}v\_{1} | =κ1​(θ1−v1)​d​t+σ1​v1​d​Wv1,\displaystyle=\kappa\_{1}(\theta\_{1}-v\_{1})\mathop{}\!\kern 0.0pt\mathrm{d}t+\sigma\_{1}\sqrt{v\_{1}}\mathop{}\!\kern 0.0pt\mathrm{d}W\_{v\_{1}}\,, |  | (2b) |
  |  | d​v2\displaystyle\mathop{}\!\kern 0.0pt\mathrm{d}v\_{2} | =κ2​(θ2−v2)​d​t+σ2​v2​d​Wv2,\displaystyle=\kappa\_{2}(\theta\_{2}-v\_{2})\mathop{}\!\kern 0.0pt\mathrm{d}t+\sigma\_{2}\sqrt{v\_{2}}\mathop{}\!\kern 0.0pt\mathrm{d}W\_{v\_{2}}\,, |  | (2c) |

  where WF1W\_{F\_{1}},Wv1W\_{v\_{1}} are two Brownian motions correlated with correlation ρ1\rho\_{1}, WF2W\_{F\_{2}},Wv2W\_{v\_{2}} are two Brownian motions correlated with correlation ρ2\rho\_{2} and each pair (Wv1,Wv2)(W\_{v\_{1}},W\_{v\_{2}}), (WF1,WF2)(W\_{F\_{1}},W\_{F\_{2}}), (Wv1,WF2)(W\_{v\_{1}},W\_{F\_{2}}), (WF1,Wv2)(W\_{F\_{1}},W\_{v\_{2}}) is uncorrelated. Because of the added dimension, the particle method of Guyon and Henry-Labordere ([2011](https://arxiv.org/html/2512.19821v1#bib.bib13)) may be necessary to obtain the local volatility component from the standard Dupire local volatility and price exotics. When used as pure stochastic volatility model, in this classic formulation, obtaining stable parameters over time is challenging.
* •

  In the Bates model, a jump component is added, and we have

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | | | | |
  |  | d​FF\displaystyle\frac{\mathop{}\!\kern 0.0pt\mathrm{d}F}{F} | =−λ​k¯​d​t+v​d​WF+d​Z,\displaystyle=-\lambda\bar{k}\mathop{}\!\kern 0.0pt\mathrm{d}t+\sqrt{v}\mathop{}\!\kern 0.0pt\mathrm{d}W\_{F}+\mathop{}\!\kern 0.0pt\mathrm{d}Z\,, |  | (3a) |
  |  | d​v\displaystyle\mathop{}\!\kern 0.0pt\mathrm{d}v | =κ​(θ−v)​d​t+σ​v​d​Wv,\displaystyle=\kappa(\theta-v)\mathop{}\!\kern 0.0pt\mathrm{d}t+\sigma\sqrt{v}\mathop{}\!\kern 0.0pt\mathrm{d}W\_{v}\,, |  | (3b) |

  where WFW\_{F} and WvW\_{v} are Brownian motions correlated with correlation ρ\rho, λ\lambda is the annual frequency of jumps, kk is the random percentage jump conditional on a jump occurring, and ZZ is a Poisson process with intensity λ\lambda and log-normal distribution of jumps sizes kk such that ln⁡(1+k)∼N​(ln⁡(1+k¯)−12​δ2,δ2)\ln(1+k)\sim N(\ln(1+\bar{k})-\frac{1}{2}\delta^{2},\delta^{2}).
* •

  The Schobel-Zhu model is another type of affine model where the volatility vv is a mean-reverting Ornstein-Uhlenbeck process Schöbel and Zhu ([1999](https://arxiv.org/html/2512.19821v1#bib.bib26)):

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | | | | |
  |  | d​FF\displaystyle\frac{\mathop{}\!\kern 0.0pt\mathrm{d}F}{F} | =v​L​(F,t)​d​WF,\displaystyle=vL(F,t)\mathop{}\!\kern 0.0pt\mathrm{d}W\_{F}\,, |  | (4a) |
  |  | d​v\displaystyle\mathop{}\!\kern 0.0pt\mathrm{d}v | =κ​(θ−v)​d​t+σ​d​Wv,\displaystyle=\kappa(\theta-v)\mathop{}\!\kern 0.0pt\mathrm{d}t+\sigma\mathop{}\!\kern 0.0pt\mathrm{d}W\_{v}\,, |  | (4b) |

  with d​WF​d​Wv=ρ​d​t\mathop{}\!\kern 0.0pt\mathrm{d}W\_{F}\mathop{}\!\kern 0.0pt\mathrm{d}W\_{v}=\rho\mathop{}\!\kern 0.0pt\mathrm{d}t. In this model, the volatility process can become negative. While it is not a mathematical issue, as this means that the correlation sign is simply flipped, the flipping of the correlation sign is more of a concern from an economic perspective. Fortunately, the probability of it being negative is very low in practice, has a negligible effect on the price of derivatives (Zhu, [2009](https://arxiv.org/html/2512.19821v1#bib.bib31)). Still, on paths where the stochastic volatility is negative, it is stays negative for an unrealistic period of time (Healy, [2025](https://arxiv.org/html/2512.19821v1#bib.bib16)).
* •

  The exponential Ornstein-Uhlenbeck model of Scott ([1987](https://arxiv.org/html/2512.19821v1#bib.bib27))

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | | | | |
  |  | d​FF\displaystyle\frac{\mathop{}\!\kern 0.0pt\mathrm{d}F}{F} | =v​L​(F,t)​d​WF,\displaystyle=vL(F,t)\mathop{}\!\kern 0.0pt\mathrm{d}W\_{F}\,, |  | (5a) |
  |  | d​ln⁡v\displaystyle\mathop{}\!\kern 0.0pt\mathrm{d}\ln v | =κ​(θ−ln⁡v)​d​t+σ​d​Wv,\displaystyle=\kappa(\theta-\ln v)\mathop{}\!\kern 0.0pt\mathrm{d}t+\sigma\mathop{}\!\kern 0.0pt\mathrm{d}W\_{v}\,, |  | (5b) |

  The model is not affine but European options may be priced via a one dimensional Monte-Carlo simulation (Overhaus et al., [2007](https://arxiv.org/html/2512.19821v1#bib.bib23), Section 2.1.3). The price process is not a martingale anymore if ρ>0\rho>0. In the context of the SLV model, Ren et al. ([2007](https://arxiv.org/html/2512.19821v1#bib.bib25)) use a specific time-dependent θ\theta, function of κ,σ\kappa,\sigma, such that the conditional expected variance is unity and the correlation ρ\rho is set to zero. Note that the direct volatility process reads d​v=v​[κ​(θ−ln⁡v)−σ2/2]​d​t+σ​v​d​Wv\mathop{}\!\kern 0.0pt\mathrm{d}v=v\left[\kappa(\theta-\ln v)-\sigma^{2}/2\right]\mathop{}\!\kern 0.0pt\mathrm{d}t+\sigma v\mathop{}\!\kern 0.0pt\mathrm{d}W\_{v}.
* •

  The lognormal volatility model of Tataru and Fisher ([2010](https://arxiv.org/html/2512.19821v1#bib.bib28)) is very similar to the Scott model, except that the mean reversion is on vv instead of ln⁡v\ln v:

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | | | | |
  |  | d​FF\displaystyle\frac{\mathop{}\!\kern 0.0pt\mathrm{d}F}{F} | =v​L​(F,t)​d​WF,\displaystyle=vL(F,t)\mathop{}\!\kern 0.0pt\mathrm{d}W\_{F}\,, |  | (6a) |
  |  | d​v\displaystyle\mathop{}\!\kern 0.0pt\mathrm{d}v | =κ​(θ−v)​d​t+σ​v​d​Wv,\displaystyle=\kappa(\theta-v)\mathop{}\!\kern 0.0pt\mathrm{d}t+\sigma v\mathop{}\!\kern 0.0pt\mathrm{d}W\_{v}\,, |  | (6b) |

  This corresponds to the mean-reverting SABR model with β=1\beta=1 and to the regular SABR model when κ=0\kappa=0. Again, martingality imposes ρ≤0\rho\leq 0. In Tataru and Fisher ([2010](https://arxiv.org/html/2512.19821v1#bib.bib28)), the parameters κ,θ,σ,ρ\kappa,\theta,\sigma,\rho are allowed to be piecewise-constant in time, although in practice, the choice θ=v​(0)=1\theta=v(0)=1 and κ=1\kappa=1 is made. The model is not affine, and short time expansions may be used to approximate the vanilla option prices for calibration. The stochastic volatility parameters are however not necessarily calibrated to vanilla options, as the volatility process is only supposed to capture the market behavior. While the volatility process may have some infinite moments, it is not an issue in practice, as the local volatility component will annihilate the explosion in practice.

## 2 Classical implied parameters

### 2.1 Textbook approach

The textbook approach to stochastic volatility calibration is to find the parameters which minimize the error in weighted vanilla option prices of various maturities and strikes.
The options chosen are typically the ones used to build the volatility surface, that is, the ones used for hedging the trader’s book. Those parameters are then used to price various exotics, typically by Monte-Carlo simulation. For the Heston model, the five parameters are calibrated to all the vanilla options as described in (Overhaus et al., [2007](https://arxiv.org/html/2512.19821v1#bib.bib23), Section 2.1.1), as well as in (Zhu, [2009](https://arxiv.org/html/2512.19821v1#bib.bib31), Section 4.7) and also in (Mikhailov and Nögel, [2004](https://arxiv.org/html/2512.19821v1#bib.bib22); Le Floc’h, [2014](https://arxiv.org/html/2512.19821v1#bib.bib19)). They thus represent the full volatility surface. In context of FX options Griebsch and Pilz ([2010](https://arxiv.org/html/2512.19821v1#bib.bib11)) also calibrate the Heston model to the relevant set of options of various strikes and maturities to price a barrier option. For the barrier option with maturity 18 months (18M) considered, this means the cross product of the 1M, 2M, 3M, 6M, 9M, 1Y, 2Y tenors and 10-d put/call, 25-delta put/call, ATM vanilla market implied volatilities.
A single set of Heston parameters is produced as output.

### 2.2 Fixing one parameter

A small practical refinement consists in not calibrating one of the parameters, typically the speed of mean reversion κ\kappa to vanilla options, but have it set exogenously. This has the advantage to stabilize the calibration (Zhu, [2009](https://arxiv.org/html/2512.19821v1#bib.bib31), Section 4.7.2), because the long term variance θ\theta and the speed of mean reversion κ\kappa play a similar role (Buehler, [2004](https://arxiv.org/html/2512.19821v1#bib.bib4)). Bergomi ([2004](https://arxiv.org/html/2512.19821v1#bib.bib3)) lets κ=2\kappa=2 because the dynamics of the variance is mostly reflected in that of short vols, corresponding to maturities TT such that T≪1κT\ll\frac{1}{\kappa}. Zhu ([2009](https://arxiv.org/html/2512.19821v1#bib.bib31)) also chooses the relatively large value κ=2\kappa=2, with the idea that the Feller condition 2​κ​θ≥σ22\kappa\theta\geq\sigma^{2} is more likely to hold. In the context of his variance curve model, Buehler ([2006](https://arxiv.org/html/2512.19821v1#bib.bib5), Proposition 3.1) proves that the Heston model is not free of dynamic arbitrage if κ\kappa is not kept constant.

Another important motivation to fix some of the parameters lies in the fact that vanilla option prices do not capture the forward volatility dynamic at all. And thus calibrating the model only on the vanilla option prices may lead to the wrong dynamic. Instead, one may fix the speed of mean reversion or the vol of vol based on exotic options or forward starting options prices.

It is not uncommon to set the initial volatility (or variance for Heston) v0v\_{0} from the implied volatility of the ATM vanilla option of maturity 1M (Zhu, [2009](https://arxiv.org/html/2512.19821v1#bib.bib31), Section 4.7.3). This further speeds up and stabilizes the calibration.

### 2.3 Further stabilization

When the Heston model is recalibrated, for example every business day, the Heston parameters will change each time. Frequent large variations increase the risk of bad hedges and mean that the model is somewhat unstable. Andersen and Piterbarg ([2010](https://arxiv.org/html/2512.19821v1#bib.bib1)); Buehler ([2004](https://arxiv.org/html/2512.19821v1#bib.bib4)) propose to add a penalty to the minimization, such that the parameters do not deviate too much from their previously calibrated values. The challenge is to choose the correct penalty value.

Buehler ([2004](https://arxiv.org/html/2512.19821v1#bib.bib4)) suggests to compute firstly the error of the unpenalized calibration and then to add a penalty such that the total error is twice the unpenalized error. This is not necessarily always appropriate, for example if the unpenalized calibration error is large then the penalty allowed is large and we force the parameters to stay close to their previous values. If the unpenalized error is small, the new parameters may move far from their previous values. Furthermore, in the case of a disruptive market event, the parameters must be able to move far.

Alternatively, one may perform a local minimization starting from the previously calibrated parameters (except possibly the initial variance). It is of course not guaranteed that the result does not end up too far in some cases, unless we impose box constraints on the parameters. Similarly, the local minimization may start from a geometrical initial guess, based purely on the implied volatilities at a three different strikes and two maturities, typically using a small time, or near-moneyness approximation (Forde et al., [2012](https://arxiv.org/html/2512.19821v1#bib.bib10)).

### 2.4 In the context of the SLV model

In reality, the calibration towards the full implied volatility surface is rarely used in the context of an SLV model for several reasons:

* •

  The local volatility component already offers a perfect fit to the vanilla options.
* •

  The set of parameters is often reduced as a consequence of the first point and the stochastic volatility part is there to capture the dynamic, which is not necessarily visible in vanilla option prices.
* •

  The mixing weight is usually a maturity dependent term-structure. And thus, some of the effective stochastic volatility parameters are actually different for each maturity.

It may however still makes sense if the stochastic volatility model uses time varying parameters in its volatility process, although this is explicitly not how the model of Tataru and Fisher ([2010](https://arxiv.org/html/2512.19821v1#bib.bib28)) is calibrated.
The calibration towards the full implied volatility surface may also be used when the calibration view is global, i.e. not specific to certain products such as barrier options or cliquets (Qu, [2016](https://arxiv.org/html/2512.19821v1#bib.bib24)).

### 2.5 Variance swap calibration

The variance swap term-structure offers another interesting way to calibrate some of the stochastic volatility parameters. For example, in the Heston model, the expected total variance is known in closed-form, and depends only on the speed of mean reversion κ\kappa, the mean reversion value θ\theta and the initial variance v0v\_{0}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1T​𝔼​[v​(T)]=θ+v0−θκ​T​(1−e−κ​T).\frac{1}{T}\mathbb{E}\left[v(T)\right]=\theta+\frac{v\_{0}-\theta}{\kappa T}\left(1-e^{-\kappa T}\right)\,. |  | (7) |

We may thus calibrate those parameters either to the term structure of quoted variance swaps, or to the term-structure of (at least three) variance swap prices implied by the vanilla options, using the replication formula of Carr and Madan ([2001](https://arxiv.org/html/2512.19821v1#bib.bib6)). Guillaume and Schoutens ([2014](https://arxiv.org/html/2512.19821v1#bib.bib12)) use those parameters as initial guess for a calibration towards all vanilla options prices, and this may help to stabilize such a calibration. It may however make more sense, especially in the context of SLV models, to let those parameters fixed by the variance swap term-structure. The practice is applicable to most stochastic volatility models, and is reminiscent of the forward variance curve approach (see Section LABEL:sec:variance\_curve).
There is however a major issue that arises in practice: models like the classic Heston with constant parameters can not always fit the term-structure of variance swaps, as its shape is very constrained, and may thus lead to financially nonsensical parameters (Le Floc’h, [2025](https://arxiv.org/html/2512.19821v1#bib.bib20)). The two factors Heston model fares better in this regard. And the Heston model with piecewise-constant parameters and 𝔼​[v​(T)]=1\mathbb{E}[v(T)]=1 is essentially a variance curve model, and may be perfectly calibrated through L​(T)L(T) (although it may be more judicious to calibrate it to vanillas directly).

## 3 Maturity dependent parameters

The basic idea behind maturity dependent parameters is to use the Heston model like the Black-Scholes model. In the Black-Scholes model, the implied volatility is a function of time and strike. Practitioners price exotic contracts such as barrier options, with a single volatility, chosen to be the at-the-money volatility at the time to maturity. This allows the use of the closed-form formulas (with many caveats obviously). In similar fashion, the parameters of the Heston model may be considered as a five dimensional implied volatility. The difference is that for a given maturity, the parameters are the same for any option strike. Thus the model is used with parameters that vary per maturity, but the model itself consists of constant parameters. This is not very consistent, akin to the varying implied volatility used in the Black-Scholes model. Maturity dependent parameters are common in the interest rate derivatives world, for example, this is how the market-standard SABR model of Hagan et al. ([2002](https://arxiv.org/html/2512.19821v1#bib.bib14)) is used for swaption pricing. In general, the SABR model is however used this way only for smile interpolation, and rarely to price strongly path-dependent exotics.

In the Black-Scholes world, a slightly more elaborate practice is to consider the term-structure of at-the-money volatilities (often at the cost of being able to use analytical formulas). This would be akin to the use of a time-dependent Heston model, where, typically, the parameters are piecewise-constant and are calibrated in a bootstrap manner to all option maturities. The model itself takes into account internally the time-dependence in the stochastic volatility process evolution. This is not what we describe in this section.

In (Clark, [2011](https://arxiv.org/html/2512.19821v1#bib.bib8), Tables 6.3 and 6.5), the Heston model is calibrated to vanilla FX options, option tenor by option tenor letting the initial variance v0v\_{0} be equal to the mean reversion level θ\theta (called mm in the tables). We give an excerpt in Table [1](https://arxiv.org/html/2512.19821v1#S3.T1 "Table 1 ‣ 3 Maturity dependent parameters").

Table 1: FX volatilities and calibrated Heston parameters as of 16 September 2008, excerpt of Clark ([2011](https://arxiv.org/html/2512.19821v1#bib.bib8), Table 6.3). The Heston Feller ratio β<1\beta<1 shows that the Feller condition does not hold.

| ccypair | tenor | ATM | 25-d-MS | 25-d-RR | v0v\_{0} | ρ\rho | σ\sigma | κ\kappa | θ\theta | β\beta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EURUSD | 3M | 12.70% | 0.28% | -0.55% | 0.02 | -0.13 | 0.49 | 6.02 | 0.02 | 0.90 |
| EURUSD | 6M | 11.87% | 0.38% | -0.55% | 0.02 | -0.13 | 0.41 | 3.02 | 0.02 | 0.59 |
| EURUSD | 1Y | 11.50% | 0.40% | -0.55% | 0.02 | -0.13 | 0.31 | 1.50 | 0.02 | 0.49 |
| EURUSD | 2Y | 11.45% | 0.40% | -0.55% | 0.02 | -0.14 | 0.20 | 0.75 | 0.02 | 0.56 |
| EURUSD | 3Y | 11.30% | 0.40% | -0.55% | 0.02 | -0.15 | 0.16 | 0.50 | 0.02 | 0.55 |
| EURUSD | 4Y | 11.13% | 0.40% | -0.56% | 0.01 | -0.16 | 0.14 | 0.38 | 0.01 | 0.54 |
| EURUSD | 5Y | 10.75% | 0.38% | -0.55% | 0.01 | -0.17 | 0.12 | 0.30 | 0.01 | 0.56 |

In particular, for each tenor, κ\kappa is set using the rule of thumb κ=1.5/T\kappa=1.5/T, and the three remaining parameters v0,ρ,σv\_{0},\rho,\sigma are calibrated to the at-the-money (ATM), 25 delta strangle (25-d-MS), 25 delta risk reversal (25-d-RR) market quotes as of September 16, 2008. Clark ([2011](https://arxiv.org/html/2512.19821v1#bib.bib8), Section 7.3) provides different rules for the level and the speed of mean reversion: θ=σATM2​(T)\theta=\sigma\_{\textsf{ATM}}^{2}(T) (the tables of (Clark, [2011](https://arxiv.org/html/2512.19821v1#bib.bib8), Section 6) show θ=v0\theta=v\_{0} instead), κ=2.75/T\kappa=2.75/T. In practice, the speed of mean reversion κ\kappa will be an exogenous tenor-dependent parameter, adjusted by the trader or quant.

A similar approach is described in (Janek et al., [2011](https://arxiv.org/html/2512.19821v1#bib.bib18)): for a given vanilla option maturity, the speed of mean reversion κ\kappa and the initial variance v0v\_{0} are fixed, and the three remaining parameters are calibrated to the set of implied volatilities corresponding to a set of delta pillars. Then exotic options, such as one-touch are priced with the parameters of the corresponding maturity.
Somewhat interestingly, the authors precise that the prices obtained are remarkably close to the market prices in practice, while in (Wystup, [2020](https://arxiv.org/html/2512.19821v1#bib.bib30)), Uwe Wystup asserts that the Heston model does not perform satisfactorily for any product. This is perhaps not as contradictory as it seems since the markets may have changed their practices significantly since 2011.

Austing ([2014](https://arxiv.org/html/2512.19821v1#bib.bib2), Section 7.7) gives the example of calibrating the SABR model using three vanilla options of same maturity as the exotic contract, including the ATM option, see also (Le Floc’h and Kennedy, [2014](https://arxiv.org/html/2512.19821v1#bib.bib21)). The SABR α\alpha is set such that the ATM option price is exactly reproduced.

In the context of the Tremor SLV model (Wystup, [2011](https://arxiv.org/html/2512.19821v1#bib.bib29)), which consists of the Heston stochastic volatility model augmented with a quadratic local volatility function, the mean reversion parameters are again fixed such that κ=1\kappa=1 and θ=v0\theta=v\_{0}. For a given maturity, The three stochastic volatility parameters are calibrated to 10-delta put/call, and ATM options market quotes. The local component parameters are calibrated to all options at this maturity after the mixing weight has been applied to the vol of vol σ\sigma.

## 4 Term-structure of parameters

With an affine stochastic volatility model, it is still possible to price vanilla options with piecewise-constant parameters in time as shown in (Mikhailov and Nögel, [2004](https://arxiv.org/html/2512.19821v1#bib.bib22); Elices, [2009](https://arxiv.org/html/2512.19821v1#bib.bib9)). The stochastic volatility process takes into account the variation of those parameters in time. The resulting pricing formula is very similar, the additional complexity lies in the recursive form of the characteristic function, which is then also more costly to evaluate, with a cost linear in the number of terms in the structure.

For non affine models, the parameter averaging technique of (Andersen and Piterbarg, [2010](https://arxiv.org/html/2512.19821v1#bib.bib1), Section 9.3) provides ways to approximate vanilla option prices of stochastic volatility models with a term-structure of parameters.

This obviously provides a better fit, without a full blown SLV model. The term-structure of parameters is appealing but we end up with a lot of parameters, which increases the chance of instabilities of the model in a day to day usage (Overhaus et al., [2007](https://arxiv.org/html/2512.19821v1#bib.bib23)): aren’t we overfitting? how stable are those parameters from day to day? how would you hedge against the variation of all those parameters?

In reality, a term-structure of parameters may be more relevant to SLV models, as the mixing weight will introduce such a term-structure.

## 5 SLV practices and the mixing parameter

In Ren et al. ([2007](https://arxiv.org/html/2512.19821v1#bib.bib25)), the two free stochastic volatility parameters of the model, the vol of vol and the speed of mean reversion, are set exogenously (not calibrated to vanillas). The mean reversion is implicit in the model and the correlation is zero. The stochastic volatility is thus not calibrated to vanilla options at all, and is only there to add an interesting dynamic to the local volatility. This makes this SLV model simpler to understand and risk manage. There is no need for a mixing parameter as the two stochastic volatility parameters are in effect the mixing. The two parameters may be captured as a term-structure (although in the stochastic volatility process, they are constant), to allow for a fine grained control over exotic prices across various maturities or tenors.

In the context of the equity derivatives market, Qu ([2016](https://arxiv.org/html/2512.19821v1#bib.bib24)) recommends against setting the correlation to zero, even if the local volatility component already contains the spot dependence, because the spot and volatility correlation is economically apparent. The correlation would then be set from a historical analysis. In practice, this is not so obvious: the stochastic volatility is not observable and a proxy must be used to estimate the correlation. The proxy may be the VIX (the SPX500 volatility index) price or the short term realized volatility of the underlying asset. It is however only a proxy. Such an historical correlation does not directly correspond to the stochastic volatility model correlation and must be adjusted accordingly. Furthermore, if we use the SLV model to generate the SPX index paths, the local volatility part will also generate a correlation between a (virtual) VIX index and the SPX index.

In Tataru and Fisher ([2010](https://arxiv.org/html/2512.19821v1#bib.bib28)), only the two stochastic volatility parameters σ\sigma and ρ\rho are term-structures of piecewise-constant values (along the time to maturity). They are set together through a mixing factor λ\lambda, following the rule σ=λ​σmax\sigma=\lambda\sigma\_{\max}, ρ=λ​ρmax\rho=\lambda\rho\_{\max} where σmax,ρmax\sigma\_{\max},\rho\_{\max} are constants (maximally stochastic parameters). The mixing factor is also piecewise-constant in time and is effectively the only time-varying parameter the user of this SLV model sets. The stochastic volatility parameters are calibrated infrequently to the market, not to vanilla options, but to the historical dynamic of the volatility skew and spot. As the stochastic volatility parameters are not calibrated to vanillas, it does not matter if, in the model, vanilla options are priced either with slow numerical methods or fast but not so accurate approximations.

For the Heston SLV model Clark ([2011](https://arxiv.org/html/2512.19821v1#bib.bib8)) applies a mixing weight to mark down strangles and risk reversals of the maturity considered (the corresponding market quotes are multiplied by the mixing weight) to reduce the convexity of the pure stochastic volatility part. The stochastic volatility parameters are then directly calibrated to those marked-down quotes. This translates to a lower vol of variance σ\sigma but also to a lower correlation ρ\rho, and a slight change of the initial variance v0v\_{0}. When the mixing weight is zero, we expect the correlation and the vol of variance to be zero as well, the model will behave like a pure local volatility model. The mixing weight is tuned such that the price of double no touch options are close to the market prices for a given tenor.

For the Tremor SLV model, the mixing weight is used to adjust the vol of vol σ\sigma, after the pure Heston stochastic volatility parameters v0,ρ,σv\_{0},\rho,\sigma have been calibrated to vanilla options.

Austing ([2014](https://arxiv.org/html/2512.19821v1#bib.bib2)) shows that the correlation ρ\rho has little impact on the price of barrier options, and may be set to zero as the local volatility component will compensate for it. Furthermore the price of barrier options is mostly dependent on the vol of vol parameter. As a consequence, in the lognormal SLV model, for a given maturity, only the vol of vol is tuned to match the market prices of barrier options, such as one-touch contracts, via a mixing parameter λ\lambda and the effective vol of vol used in the full-blown SLV model is (1−λ)​σ(1-\lambda)\sigma (Austing, [2014](https://arxiv.org/html/2512.19821v1#bib.bib2), Section 9.6). The stochastic volatility parameters are calibrated (approximately) to vanilla options of a given maturity.

In general, the mixing weight can not be constant for all maturities in order to fit the quoted prices of various barrier options (such as touch, no-touch).

## 6 Live calibration vs. up-front calibration

When does the stochastic volatility model calibration occurs?
There are two practices.

The first one, perhaps more traditional is the up-front calibration where the model is calibrated once a day or less. The parameters are stored, and then used to price exotics of various maturities during the day. This may also be applied more generally to SLV models.

The second practice, which may also motivate the choice of maturity dependent parameters, is to calibrate (some of) the stochastic volatility parameters at each valuation time. The parameters do not need to be stored and will be different at a later valuation time. When maturity-dependent parameters are used, only one maturity is calibrated, the one relevant for the exotic contract. In the context of the Heston model, the usual practice is to only calibrate the three parameters v0,ρ,σv\_{0},\rho,\sigma (see Section [3](https://arxiv.org/html/2512.19821v1#S3 "3 Maturity dependent parameters")). In the context of a first generation SLV model with a parametric LV function, the LV parameters are also calibrated at the same time (but typically just after the SV parameters have been calibrated). This approach allows for a fast calibration.

It is perfectly possible to perform a live calibration towards a set of option contracts (not necessarily of the same maturity) although, those would typically be vanilla option contracts. The choice of vanilla (hedging) options may be different for different exotic trades. This makes a priori more sense: for example a two year exotic contract paying every 6 months will not be hedged only with the two year vanilla options.

In the end, while the up-front approach may seem more consistent during the day, it will lose this consistency the next day, when the parameters are recalibrated. When the parameters are calibrated towards the full set of vanilla options (classical implied calibration), there is however no good reason to perform a live calibration as long as the set of reference vanilla options quotes has not moved. When embedded in an SLV model, the SV parameters may be kept constant for a longer period of time.

\funding

This research received no external funding.
\conflictsofinterestThe authors declare no conflict of interest.
\externalbibliographyyes

## References

* Andersen and Piterbarg (2010)

  Andersen, Leif and Vladimir Piterbarg. 2010.
  Interest rate modeling–volume i.
  Atlantic Financial Press 1.
* Austing (2014)

  Austing, Peter. 2014.
  Smile pricing explained.
  Springer.
* Bergomi (2004)

  Bergomi, Lorenzo. 2004.
  Smile dynamics i.
  Available at SSRN 1493294.
* Buehler (2004)

  Buehler, Hans. 2004.
  Stochastic volatility models and products.
  Presentation at the Risk Training Course, Hong Kong.
* Buehler (2006)

  Buehler, Hans. 2006.
  Consistent variance curve models.
  Finance and Stochastics 10(2), 178–203.
* Carr and Madan (2001)

  Carr, Peter and Dilip Madan. 2001.
  Towards a theory of volatility trading.
  Option Pricing, Interest Rates and Risk Management, Handbooks in Mathematical Finance, 458–476.
* Christoffersen et al. (2009)

  Christoffersen, Peter, Steven Heston, and Kris Jacobs. 2009.
  The shape and term structure of the index option smirk: Why multifactor stochastic volatility models work so well.
  Management Science 55(12), 1914–1932.
* Clark (2011)

  Clark, Iain J. 2011.
  Foreign exchange option pricing: a practitioner’s guide.
  John Wiley & Sons.
* Elices (2009)

  Elices, Alberto. 2009.
  Affine concatenation.
  Wilmott Journal: The International Journal of Innovative Quantitative Finance Research 1(3), 155–162.
* Forde et al. (2012)

  Forde, Martin, Antoine Jacquier, and Roger Lee. 2012.
  The small-time smile and term structure of implied volatility under the heston model.
  SIAM Journal on Financial Mathematics 3(1), 690–708.
* Griebsch and Pilz (2010)

  Griebsch, Susanne A and Kay F Pilz. 2010.
  Stochastic volatility models: Foreign exchange.
  Encyclopedia of Quantitative Finance.
* Guillaume and Schoutens (2014)

  Guillaume, Florence and Wim Schoutens. 2014.
  Heston model: the variance swap calibration.
  Journal of Optimization Theory and Applications 161(1), 76–89.
* Guyon and Henry-Labordere (2011)

  Guyon, Julien and Pierre Henry-Labordere. 2011.
  The smile calibration problem solved.
  Available at SSRN 1885032.
* Hagan et al. (2002)

  Hagan, Patrick S, Deep Kumar, Andrew S Lesniewski, and Diana E Woodward. 2002.
  Managing smile risk.
  Wilmott magazine.
* Hagan et al. (2018)

  Hagan, Patrick S, Andrew S Lesniewski, and Diana E Woodward. 2018.
  Implied volatility formulas for heston models.
  Wilmott 2018(98), 44–57.
* Healy (2025)

  Healy, Jherek. 2025.
  Applied Quantitative Finance for Equity Derivatives (Fifth ed.).
  available Amazon.com and other online stores.
  ISBN: 979-8289924087.
* Heston (1993)

  Heston, Steven L. 1993.
  A closed-form solution for options with stochastic volatility with applications to bond and currency options.
  Review of financial studies 6(2), 327–343.
* Janek et al. (2011)

  Janek, Agnieszka, Tino Kluge, Rafał Weron, and Uwe Wystup. 2011.
  Fx smile in the heston model.
  In Statistical tools for finance and insurance, pp. 133–162. Springer.
* Le Floc’h (2014)

  Le Floc’h, Fabien. 2014.
  Fourier integration and stochastic volatility calibration.
  Available at SSRN 2362968 <https://ssrn.com/abstract=2362968>.
* Le Floc’h (2025)

  Le Floc’h, Fabien. 2025.
  Calibrating Heston to variance swaps - a bad idea?
  <https://chasethedevil.github.io/post/heston_variance_swap_calibration/> [Online; accessed 12-February-2025].
* Le Floc’h and Kennedy (2014)

  Le Floc’h, Fabien and Gary J Kennedy. 2014.
  Explicit SABR calibration through simple expansions.
  Available at SSRN 2467231.
* Mikhailov and Nögel (2004)

  Mikhailov, Sergei and Ulrich Nögel. 2004.
  Heston’s stochastic volatility model: Implementation, calibration and some extensions.
  John Wiley and Sons.
* Overhaus et al. (2007)

  Overhaus, Marcus, Ana Bermúdez, Hans Buehler, Andrew Ferraris, Christopher Jordinson, and Aziz Lamnouar. 2007.
  Equity hybrid derivatives, Volume 374.
  John Wiley & Sons.
* Qu (2016)

  Qu, Dong. 2016.
  Manufacturing and managing customer-driven derivatives.
  The Wiley finance series.
* Ren et al. (2007)

  Ren, Yong, Dilip Madan, and M Qian Qian. 2007.
  Calibrating and pricing with embedded local volatility models.
  RISK-LONDON-RISK MAGAZINE LIMITED- 20(9), 138.
* Schöbel and Zhu (1999)

  Schöbel, Rainer and Jianwei Zhu. 1999.
  Stochastic volatility with an Ornstein–Uhlenbeck process: an extension.
  European Finance Review 3(1), 23–46.
* Scott (1987)

  Scott, Louis O. 1987.
  Option pricing when the variance changes randomly: Theory, estimation, and an application.
  Journal of Financial and Quantitative analysis 22(4), 419–438.
* Tataru and Fisher (2010)

  Tataru, Grigore and Travis Fisher. 2010.
  Stochastic local volatility.
  Quantitative Development Group, Bloomberg Version 1(February 5).
* Wystup (2011)

  Wystup, Uwe. 2011.
  The tremor stochastic-local-volatility model: Independent validation by math-finance.
  In 2011 Global Derivatives USA Conference.
* Wystup (2020)

  Wystup, Uwe. 2020.
  Mixed local volatility boosts distribution of exotics.
  Wilmott 2020(110), 34–37.
* Zhu (2009)

  Zhu, Jianwei. 2009.
  Applications of Fourier transform to smile modeling: Theory and implementation.
  Springer Science & Business Media.

\appendixtitles

no