---
authors:
- Siqi Shao
- Arshia Ghasemi
- Hamed Farahani
- R. A. Serota
doc_id: arxiv:2512.23640v1
family_id: arxiv:2512.23640
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution
url_abs: http://arxiv.org/abs/2512.23640v1
url_html: https://arxiv.org/html/2512.23640v1
venue: arXiv q-fin
version: 1
year: 2025
---


Siqi Shao

Arshia Ghasemi

Hamed Farahani

R. A. Serota111serota@ucmail.uc.edu
Department of Physics, University of Cincinnati, Cincinnati, Ohio 45221-0011

###### Abstract

We argue that negative skew and positive mean of the distribution of stock returns are largely due to the broken symmetry of stochastic volatility governing gains and losses. Starting with stochastic differential equations for stock returns and for stochastic volatility we argue that the distribution of stock returns can be effectively split in two - for gains and losses - assuming difference in parameters of their respective stochastic volatilities. A modified Jones-Faddy skew t-distribution utilized here allows to reflect this in a single organic distribution which tends to meaningfully capture this asymmetry. We illustrate its application on distribution of daily S&P500 returns, including analysis of its tails.

###### keywords:

Student’s t-Distribution , Jones-Fadddy Skew t-Distribution , Stock Returns Gains and Losses , Stochastic Volatility , Power-Law Tails

††journal: arXiv

## 1 Introduction

A well-known upward trend in stock prices is illustrated in Fig. [1](https://arxiv.org/html/2512.23640v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") for S&P500. Here StS\_{t} is price on day tt. The best linear fit μ​t\mu t of rt=log⁡(St/S0)r\_{t}=\log(S\_{t}/S\_{0}) corresponds to roughly 12%12\% annual growth. De-trended plot of returns xt=rt−μ​tx\_{t}=r\_{t}-\mu t is shown in Fig. [2](https://arxiv.org/html/2512.23640v1#S1.F2 "Figure 2 ‣ 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") and the fluctuations of xtx\_{t} are attributed to market volatility. The simplest of models attempting to describe these fluctuations implies that de-trended returns are governed by a stochastic differential equation (SDE)

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​xt=log⁡(St+d​tSt)−μ​d​t=σt​d​W(1)dx\_{t}=\log\left(\frac{S\_{t+\mathrm{d}t}}{S\_{t}}\right)-\mu\mathrm{d}t=\sigma\_{t}\mathrm{d}W^{(1)} |  | (1) |

where σt\sigma\_{t} is the stochastic volatility and d​W=W​(t+d​t)−W​(t)\mathrm{d}W=W\left(t+\mathrm{d}t\right)-W(t) is the normally distributed Wiener process, d​W∼N​(0,d​t)\mathrm{d}W\sim\mathrm{N(}0,\,\mathrm{d}t\mathrm{)}, (d​W)2=d​t(\mathrm{d}W)^{2}=\mathrm{d}t.

![Refer to caption](x1.png)


Figure 1: S&P500; rt=log⁡(St/S0)r\_{t}=\log(S\_{t}/S\_{0}), StS\_{t} is price on day tt, tt changes in daily increments (τ=1\tau=1 in text).

![Refer to caption](x2.png)


Figure 2: S&P500; xt=rt−μ1​tx\_{t}=r\_{t}-\mu\_{1}t where index in μ1\mu\_{1} reflects daily increments of tt (τ=1\tau=1 in text).

Stochastic volatility, in turn, is believed to be described by the mean-reverting SDE for stochastic variance v=σt2v=\sigma\_{t}^{2}

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​vt=−γ​(vt−θ)​d​t+g​(vt)​d​W(2)\mathrm{d}v\_{t}=-\gamma(v\_{t}-\theta)\mathrm{d}t+g(v\_{t})\mathrm{d}W^{(2)} |  | (2) |

implying that stochastic variance - and hence volatility - tends to revert to its mean value, ⟨vt⟩=θ\left<v\_{t}\right>=\theta. One of the important implications of the latter is that for returns accumulated over τ\tau days, d​t=τ\mathrm{d}t=\tau, average variance of returns grows linearly with τ\tau, ⟨d​x2⟩=θ​τ\left<dx^{2}\right>=\theta\tau. Since we are not concerned here with quantities such as leverage [perello2003stochastic, dashti2021distributions] and study distribution of returns, in what follows we will neglect correlations between d​W(1)\mathrm{d}W^{(1)} and d​W(2)\mathrm{d}W^{(2)} [dragulescu2002probability, liu2019distributions] and will largely concentrate on daily returns τ=1\tau=1.

Numerous models exist for g​(vt)g(v\_{t}), such as Cox-Ingersoll-Ross [cox1985theory, heston1993closed, dragulescu2002probability, liu2019distributions], multiplicative [praetz1972distribution, nelson1990arch, fuentes2009universal, liu2019distributions], and the combination of the two [dashti2021combined]. Here we will concentrate on multiplicative model since it is the simplest model that predicts power-law tails of the distribution of returns and is the easiest to handle analytically. While power-law tails in returns are not universally agreed upon, there is a strong case for them at least for daily returns, while for accumulated returns power law may persist for a large portion of the tail (see e.g. [farahani2025asymmetry] and below).

In multiplicative model

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(vt)=κ​vtg(v\_{t})=\kappa v\_{t} |  | (3) |

which yields an Inverse Gamma [wolfram2025inverse] steady-state distribution (probability density function) for variance

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(vt)=IGa​(vt;αθ+1,α)f(v\_{t})=\mathrm{IGa(}v\_{t};\,\frac{\alpha}{\theta}+1,\,\alpha\mathrm{)} |  | (4) |

which, in turn, translates into the following distribution for volatility [liu2019distributions]

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(σt)=2​σt⋅IGa​(σt2;αθ+1,α)f(\sigma\_{t})=2\sigma\_{t}\cdot\mathrm{IGa(}\sigma\_{t}^{2};\,\frac{\alpha}{\theta}+1,\,\alpha\mathrm{)} |  | (5) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | α=2​γ​θκ2\alpha=\frac{2\gamma\theta}{\kappa^{2}} |  | (6) |

From eqs. ([1](https://arxiv.org/html/2512.23640v1#S1.E1 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) and ([5](https://arxiv.org/html/2512.23640v1#S1.E5 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) the distribution of stock returns can be found as a product distribution [ma2014model] of inverse Gamma and normal distribution and the result is a Student t-distribution [praetz1972distribution, fuentes2009universal, liu2019distributions]

|  |  |  |  |
| --- | --- | --- | --- |
|  | fS​t​(x)=Γ​(αθ+32)π​Γ​(αθ+1)​12​α​τ​(x22​α​τ+1)−(αθ+32)f\_{St}(x)=\frac{\Gamma(\frac{\alpha}{\theta}+\frac{3}{2})}{\sqrt{\pi}\Gamma(\frac{\alpha}{\theta}+1)}\frac{1}{\sqrt{2\alpha\tau}}\left(\frac{x^{2}}{2\alpha\tau}+1\right)^{-(\frac{\alpha}{\theta}+\frac{3}{2})} |  | (7) |

Clearly this distribution is even 222In this particular case it is a consequence of normal distribution being even in the product distribution in ([1](https://arxiv.org/html/2512.23640v1#S1.E1 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")). It is also obvious that the product distribution will be even regardless of a specific form of g(vt))g(v\_{t})) and thus establishes symmetry between gains and losses. This, of course, also applies to the power-law tails, whose exponent is −(2​αθ+3)-\left(\frac{2\alpha}{\theta}+3\right). However this symmetry is clearly broken for actual data. To wit, the distribution of S&P500 returns has [farahani2025asymmetry]:

* 1.

  positive mean
* 2.

  negative skew
* 3.

  greater number of points for gains than for losses
* 4.

  slower power-law exponent for losses than for gains

The motivation for this work was therefore to model this symmetry breaking while, ideally, still remaining within SDE framework. The first and fairly obvious idea would be that stochastic volatility eqs. ([2](https://arxiv.org/html/2512.23640v1#S1.E2 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) and ([3](https://arxiv.org/html/2512.23640v1#S1.E3 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) are governed by a different set of parameters for gains and losses, that is to say that their parameters α\alpha and θ\theta are different. In other words, this implies that gains and losses should be fitted separately by weighted Student t-distributions ([7](https://arxiv.org/html/2512.23640v1#S1.E7 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) in a manner that weights add up to unity and their ratio is the ratio of points under respective distributions. For brevity, we call the final distribution “half Student-t”.

While still having SDE underpinning “half Student-t” is obviously not an organic distribution. Additionally, it predicts a negative mean contrary to the empirical evidence above. Consequently, we adopted yet another approach based on a skew extension of Student t-distribution by Jones and Faddy. [jones2001skew, jones2003skew]. Unfortunately, modified Jones-Faddy (mJF) distributions that we use are not cleanly derived from SDE formalism but on the other hand they are close in spirit and yield good fits to the full distribution of returns.

This paper is organized as follows. In Section [2](https://arxiv.org/html/2512.23640v1#S2 "2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") we provide expressions for the probability density function (PDF) and cumulative distribution function (CDF) of mJF distributions as well as their statistical parameters, such as mean, mode, variance and skewness. In Section [3](https://arxiv.org/html/2512.23640v1#S3 "3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") we present results of fitting the full distribution of returns. Finally, we summarize and discuss our results in Section [4](https://arxiv.org/html/2512.23640v1#S4 "4 Conclusions and Discussion ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution").

## 2 Analytical Framework

In this section we give analytical expressions for PDF, CDF, mean m1m\_{1}, variance m2m\_{2} (m21/2m\_{2}^{1/2} being standard deviation), and mode m¯\overline{m} for four distributions described in this section. We use first and second Pearson coefficients of skewness

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζ1=(m1−m¯)m21/2,ζ2=(m1−m~)m21/2\zeta\_{1}=\frac{\left(m\_{1}-\overline{m}\right)}{m\_{2}^{1/2}},\qquad\zeta\_{2}=\frac{\left(m\_{1}-\widetilde{m}\right)}{m\_{2}^{1/2}} |  | (8) |

to characterize the skew of the distribution, where m~\widetilde{m} is the median, which is evaluated numerically. 333The standard Fisher-Pearson coefficient can not be analytically obtained in this case since the third moment diverges due to slow power-law decays of the tails [farahani2025asymmetry]. We will consider CDF appropriate for gains and losses separately per, respectively,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fg​(x)=∫−∞xf​(y)​dyF\_{g}(x)=\int\_{-\infty}^{x}f(y)\mathrm{d}y |  | (9) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fl​(x)=∫x∞f​(y)​dyF\_{l}(x)=\int\_{x}^{\infty}f(y)\mathrm{d}y |  | (10) |

where f​(x)f(x) is the PDF of returns. Complementary CDF, CCDF, appropriate for gains and losses are, respectively, 1−Fg​(x)1-F\_{g}(x) and 1−Fl​(x)1-F\_{l}(x).

### 2.1 Student t-Distribution

PDF of Student t-distribution is given by ([7](https://arxiv.org/html/2512.23640v1#S1.E7 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) implying that the tails of PDF scale as x−(2​α/θ+3)x^{-\left(2\alpha/\theta+3\right)} and of CDF as x−2​(α/θ+1)x^{-2\left(\alpha/\theta+1\right)}. Due to symmetry CDF for both gains and losses is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | FS​t​(x)=12​(1+I​(x2x2+2​α​τ;12, 1+αθ))F\_{St}(x)=\frac{1}{2}\left(1+I\!\left(\frac{x^{2}}{x^{2}+2\alpha\tau};\,\frac{1}{2},\,1+\frac{\alpha}{\theta}\right)\right) |  | (11) |

where I​(x;a,b)I(x;a,b) is a regularized incomplete beta function [nist2025digital] and, obviously, m1=m¯=m~=ζ1,2=0m\_{1}=\overline{m}=\widetilde{m}=\zeta\_{1,2}=0 and

|  |  |  |  |
| --- | --- | --- | --- |
|  | m2=θ​τm\_{2}=\theta\tau |  | (12) |

### 2.2 Half Student-t Distribution

In effect, it is a mixture distribution whose PDF of gains and losses are given, respectively, by

|  |  |  |  |
| --- | --- | --- | --- |
|  | fg​\_​h​S​t​(x)=2​Γ​(αgθg+32)π​Γ​(αgθg+1)​12​αg​τ​(x22​αg​τ+1)−(αgθg+32),x≥0f\_{g\\_hSt}(x)=\frac{2\,\Gamma\!\left(\frac{\alpha\_{g}}{\theta\_{g}}+\frac{3}{2}\right)}{\sqrt{\pi}\,\Gamma\!\left(\frac{\alpha\_{g}}{\theta\_{g}}+1\right)}\frac{1}{\sqrt{2\alpha\_{g}\tau}}\left(\frac{x^{2}}{2\alpha\_{g}\tau}+1\right)^{-\left(\frac{\alpha\_{g}}{\theta\_{g}}+\frac{3}{2}\right)},\qquad x\geq 0 |  | (13) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | fl​\_​h​S​t​(x)=2​Γ​(αlθl+32)π​Γ​(αlθl+1)​12​αl​τ​(x22​αl​τ+1)−(αlθl+32),x≤0f\_{l\\_hSt}(x)=\frac{2\,\Gamma\!\left(\frac{\alpha\_{l}}{\theta\_{l}}+\frac{3}{2}\right)}{\sqrt{\pi}\,\Gamma\!\left(\frac{\alpha\_{l}}{\theta\_{l}}+1\right)}\frac{1}{\sqrt{2\alpha\_{l}\tau}}\left(\frac{x^{2}}{2\alpha\_{l}\tau}+1\right)^{-\left(\frac{\alpha\_{l}}{\theta\_{l}}+\frac{3}{2}\right)},\qquad x\leq 0 |  | (14) |

so that the full distribution is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | fh​S​t=wg​fg​\_​h​S​t+wl​fl​\_​h​S​t​(x)f\_{hSt}=w\_{g}f\_{g\\_hSt}+w\_{l}f\_{l\\_hSt}(x) |  | (15) |

where wg+wl=1w\_{g}+w\_{l}=1 and wg/wlw\_{g}/w\_{l} is the ratio of points under gains and losses [farahani2025asymmetry]. Generally speaking a mixture distribution is not a preferable venue from a physicist’s point of view since it does not follow form a first–principles model. However fg​\_​h​S​tf\_{g\\_hSt} and fl​\_​h​S​tf\_{l\\_hSt} marginally do.

CDF of gains and losses are given, respectively, by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fg​\_​h​S​t​(x)=wl+wg​I​(x2x2+2​αg​τ;12, 1+αgθg)F\_{g\\_hSt}(x)=w\_{l}+w\_{g}I\!\left(\frac{x^{2}}{x^{2}+2\alpha\_{g}\tau};\,\frac{1}{2},\,1+\frac{\alpha\_{g}}{\theta\_{g}}\right) |  | (16) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fl​\_​h​S​t​(x)=wg+wl​I​(x2x2+2​αl​τ;12, 1+αlθl)F\_{l\\_hSt}(x)=w\_{g}+w\_{l}I\!\left(\frac{x^{2}}{x^{2}+2\alpha\_{l}\tau};\,\frac{1}{2},\,1+\frac{\alpha\_{l}}{\theta\_{l}}\right) |  | (17) |

Using ([13](https://arxiv.org/html/2512.23640v1#S2.E13 "In 2.2 Half Student-t Distribution ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution"))-([15](https://arxiv.org/html/2512.23640v1#S2.E15 "In 2.2 Half Student-t Distribution ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) we find the following expressions for the mean and variance respectively

|  |  |  |  |
| --- | --- | --- | --- |
|  | m1=2π​(wg​αg​τ​Γ​(12+αgθg)Γ​(1+αgθg)−wl​αl​τ​Γ​(12+αlθl)Γ​(1+αlθl))m\_{1}=\sqrt{\frac{2}{\pi}}\left(\frac{w\_{g}\sqrt{\alpha\_{g}\tau}\,\Gamma\!\left(\tfrac{1}{2}+\tfrac{\alpha\_{g}}{\theta\_{g}}\right)}{\Gamma\!\left(1+\tfrac{\alpha\_{g}}{\theta\_{g}}\right)}-\frac{w\_{l}\sqrt{\alpha\_{l}\tau}\,\Gamma\!\left(\tfrac{1}{2}+\tfrac{\alpha\_{l}}{\theta\_{l}}\right)}{\Gamma\!\left(1+\tfrac{\alpha\_{l}}{\theta\_{l}}\right)}\right) |  | (18) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | m2\displaystyle m\_{2} | =τ(wgθg+wlθl\displaystyle=\tau\Bigg(w\_{g}\theta\_{g}+w\_{l}\theta\_{l} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +2​(−2+wg+wl)​(wl2​αl​Γ​(1+αgθg)2​Γ​(12+αlθl)2−2​wg​wl​αg​αl​Γ​(12+αgθg)​Γ​(1+αgθg)​Γ​(12+αlθl)​Γ​(1+αlθl)+wg2​αg​Γ​(12+αgθg)2​Γ​(1+αlθl)2)π​Γ​(1+αgθg)2​Γ​(1+αlθl)2)\displaystyle\quad+\frac{2(-2+w\_{g}+w\_{l})\Big(\scriptstyle w\_{l}^{2}\alpha\_{l}\Gamma\!\left(1+\frac{\alpha\_{g}}{\theta\_{g}}\right)^{2}\Gamma\!\left(\frac{1}{2}+\frac{\alpha\_{l}}{\theta\_{l}}\right)^{2}-2w\_{g}w\_{l}\sqrt{\alpha\_{g}\alpha\_{l}}\Gamma\!\left(\frac{1}{2}+\frac{\alpha\_{g}}{\theta\_{g}}\right)\Gamma\!\left(1+\frac{\alpha\_{g}}{\theta\_{g}}\right)\Gamma\!\left(\frac{1}{2}+\frac{\alpha\_{l}}{\theta\_{l}}\right)\Gamma\!\left(1+\frac{\alpha\_{l}}{\theta\_{l}}\right)+w\_{g}^{2}\alpha\_{g}\Gamma\!\left(\frac{1}{2}+\frac{\alpha\_{g}}{\theta\_{g}}\right)^{2}\Gamma\!\left(1+\frac{\alpha\_{l}}{\theta\_{l}}\right)^{2}\Big)}{\scriptstyle\pi\Gamma\!\left(1+\frac{\alpha\_{g}}{\theta\_{g}}\right)^{2}\Gamma\!\left(1+\frac{\alpha\_{l}}{\theta\_{l}}\right)^{2}}\Bigg) |  | (19) |

where Γ​(x)\Gamma(x) is a Gamma function [nist2025digital]. Clearly, m¯=0\overline{m}=0 in this model so the sign of the skew ζ1\zeta\_{1} will be that of m1m\_{1}. Another observation is that the number of parameters in half Student-t, aside from τ\tau, is double that of Student t-distribution. One possible simplification of this model is to assume that the mean stochastic volatility governing gains and losses is the same, θg=θl=θ\theta\_{g}=\theta\_{l}=\theta so that the difference between gains and losses, including power-law exponents, reduces solely to difference between αg\alpha\_{g} and αl\alpha\_{l}.

### 2.3 Modified Jones-Faddy Distribution mJF1

PDF of the first of modified Jones-Faddy distributions (mJF1) introduced here for characterization of distribution of stock returns is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x)=C​(1−x−μ(x−μ)2+(αg+αl)​τ)αgθ+32​(1+x−μ(x−μ)2+(αg+αl)​τ)αlθ+32f(x)=C\left(1-\frac{x-\mu}{\sqrt{(x-\mu)^{2}+(\alpha\_{g}+\alpha\_{l})\tau}}\right)^{\frac{\alpha\_{g}}{\theta}+\frac{3}{2}}\left(1+\frac{x-\mu}{\sqrt{(x-\mu)^{2}+(\alpha\_{g}+\alpha\_{l})\tau}}\right)^{\frac{\alpha\_{l}}{\theta}+\frac{3}{2}} |  | (20) |

where the normalization factor CC is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | C=12αlθ+1+αgθ​B​(αlθ+1,αgθ+1)​1(αg+αl)​τC=\frac{1}{2^{\frac{\alpha\_{l}}{\theta}+1+\frac{\alpha\_{g}}{\theta}}\text{B}(\frac{\alpha\_{l}}{\theta}+1,\frac{\alpha\_{g}}{\theta}+1)}\frac{1}{\sqrt{(\alpha\_{g}+\alpha\_{l})\tau}} |  | (21) |

CDF for gains and losses are given, respectively, by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fg​\_​m​J​F​1​(x)=I​(1+x−μ(x−μ)2+(αg+αl)​τ;αgθ+1,αlθ+1)F\_{g\\_mJF1}(x)=I\left(1+\frac{x-\mu}{\sqrt{(x-\mu)^{2}+(\alpha\_{g}+\alpha\_{l})\tau}};\frac{\alpha\_{g}}{\theta}+1,\frac{\alpha\_{l}}{\theta}+1\right) |  | (22) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fl​\_​m​J​F​1​(x)=I​(1−x−μ(x−μ)2+(αg+αl)​τ;αgθ+1,αlθ+1)F\_{l\\_mJF1}(x)=I\left(1-\frac{x-\mu}{\sqrt{(x-\mu)^{2}+(\alpha\_{g}+\alpha\_{l})\tau}};\frac{\alpha\_{g}}{\theta}+1,\frac{\alpha\_{l}}{\theta}+1\right) |  | (23) |

mJF1 is a direct descendent of the distribution ([7](https://arxiv.org/html/2512.23640v1#S1.E7 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) with one minor and one significant variation. First, as in standard Student distribution [wolfram2025student], a location parameter μ\mu can be introduced and is introduced here. Obviously it does not affect ([1](https://arxiv.org/html/2512.23640v1#S1.E1 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) since the variable can always be shifted by a constant. The second variation introduces a skew (skew t distribution [jones2001skew, jones2003skew]), via αg\alpha\_{g} and αl\alpha\_{l} here. In particular, power-law tails scale as x−(2​αg/θ+3)x^{-\left(2\alpha\_{g}/\theta+3\right)} at +∞+\infty and x−(2​αg/θ+3)x^{-\left(2\alpha\_{g}/\theta+3\right)} at −∞-\infty. This brakes a construct based on ([1](https://arxiv.org/html/2512.23640v1#S1.E1 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) and ([2](https://arxiv.org/html/2512.23640v1#S1.E2 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) which treats volatility of gains and losses uniformly: substituition αg=αl=α\alpha\_{g}=\alpha\_{l}=\alpha in ([20](https://arxiv.org/html/2512.23640v1#S2.E20 "In 2.3 Modified Jones-Faddy Distribution mJF1 ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) leads back to ([7](https://arxiv.org/html/2512.23640v1#S1.E7 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) (with non-zero location parameter μ\mu). At this point we are unaware of an SDE-based formulation which would result in a distribution ([20](https://arxiv.org/html/2512.23640v1#S2.E20 "In 2.3 Modified Jones-Faddy Distribution mJF1 ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")).

Turning now to mean, variance and mode of mJF1 we find, respectively,

|  |  |  |  |
| --- | --- | --- | --- |
|  | m1=μ+(αg+αl)​τ(αg/θ+1)+(αl/θ+1)​(αlθ−αgθ)​αg+αlθ+22​π​B​(αgθ+12,12)​B​(αlθ+12,12)m\_{1}=\mu+\sqrt{\frac{(\alpha\_{g}+\alpha\_{l})\tau}{(\alpha\_{g}/\theta+1)+(\alpha\_{l}/\theta+1)}}\frac{\left(\frac{\alpha\_{l}}{\theta}-\frac{\alpha\_{g}}{\theta}\right)\sqrt{\frac{\alpha\_{g}+\alpha\_{l}}{\theta}+2}}{2\pi\,\mathrm{B}\!\left(\frac{\alpha\_{g}}{\theta}+\frac{1}{2},\frac{1}{2}\right)\mathrm{B}\!\left(\frac{\alpha\_{l}}{\theta}+\frac{1}{2},\frac{1}{2}\right)}\\ |  | (24) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | m2=θ​τ​(αg+αl)24​αg​αl+(αg+αl)​(αg−αl)2​τ4​θ2​[θ2αg​αl−(πB​(αgθ,12)​B​(αlθ,12))2].m\_{2}=\theta\tau\frac{(\alpha\_{g}+\alpha\_{l})^{2}}{4\alpha\_{g}\alpha\_{l}}+\frac{(\alpha\_{g}+\alpha\_{l})(\alpha\_{g}-\alpha\_{l})^{2}\tau}{4\theta^{2}}\left[\frac{\theta^{2}}{\alpha\_{g}\alpha\_{l}}-\left(\frac{\pi}{\mathrm{B}\!\left(\frac{\alpha\_{g}}{\theta},\frac{1}{2}\right)\mathrm{B}\!\left(\frac{\alpha\_{l}}{\theta},\frac{1}{2}\right)}\right)^{2}\right]. |  | (25) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | m¯=μ−r21−r2​(αg+αl)​τ,r=αl−αgαg+αl+3​θ.\overline{m}=\mu-\sqrt{\frac{r^{2}}{1-r^{2}}(\alpha\_{g}+\alpha\_{l})\tau},\qquad r=\frac{\alpha\_{l}-\alpha\_{g}}{\alpha\_{g}+\alpha\_{l}+3\theta}. |  | (26) |

### 2.4 Modified Jones-Faddy Distribution mJF2

The second modified Jones-Faddy distribution mJF2 is a simple generalization of mJF1 in that instead of a single θ\theta we now have θg\theta\_{g} and θl\theta\_{l}, just as for half Student-t in Sec. [2.2](https://arxiv.org/html/2512.23640v1#S2.SS2 "2.2 Half Student-t Distribution ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution"). At this point we believe that assumption of the same mean stochastic volatility for gains and losses, as is the case for mJF1, makes more sense. Additionally, introduction of an extra fitting parameter in mJF2 only minimally improves fitting. Therefore, we present mJF2 results largely for completeness.

PDF of mJF2 is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x)=C​(1−x−μ(z−μ)2+(αg+αl)​τ)αgθg+32​(1+x−μ(x−μ)2+(αg+αl)​τ)αlθl+32f(x)=C\left(1-\frac{x-\mu}{\sqrt{(z-\mu)^{2}+(\alpha\_{g}+\alpha\_{l})\tau}}\right)^{\frac{\alpha\_{g}}{\theta\_{g}}+\frac{3}{2}}\left(1+\frac{x-\mu}{\sqrt{(x-\mu)^{2}+(\alpha\_{g}+\alpha\_{l})\tau}}\right)^{\frac{\alpha\_{l}}{\theta\_{l}}+\frac{3}{2}} |  | (27) |

where normalization factor is

|  |  |  |  |
| --- | --- | --- | --- |
|  | C=12αlθl+1+αgθg​B​(αlθl+1,αgθg+1)​1(αg+αl)​τC=\frac{1}{2^{\frac{\alpha\_{l}}{\theta\_{l}}+1+\frac{\alpha\_{g}}{\theta\_{g}}}\text{B}(\frac{\alpha\_{l}}{\theta\_{l}}+1,\frac{\alpha\_{g}}{\theta\_{g}}+1)}\frac{1}{\sqrt{(\alpha\_{g}+\alpha\_{l})\tau}} |  | (28) |

CDF for gains and losses are given, respectively, by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fg​\_​m​J​F​2​(x)=I​(1+x−μ(x−μ)2+(αg+αl)​τ;αgθg+1,αlθl+1)F\_{g\\_mJF2}(x)=I\left(1+\frac{x-\mu}{\sqrt{(x-\mu)^{2}+(\alpha\_{g}+\alpha\_{l})\tau}};\frac{\alpha\_{g}}{\theta\_{g}}+1,\frac{\alpha\_{l}}{\theta\_{l}}+1\right) |  | (29) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fl​\_​m​J​F​2​(x)=I​(1−x−μ(x−μ)2+(αg+αl)​τ;αgθg+1,αlθl+1)F\_{l\\_mJF2}(x)=I\left(1-\frac{x-\mu}{\sqrt{(x-\mu)^{2}+(\alpha\_{g}+\alpha\_{l})\tau}};\frac{\alpha\_{g}}{\theta\_{g}}+1,\frac{\alpha\_{l}}{\theta\_{l}}+1\right) |  | (30) |

Mean, variance and mode of mJF2 are given, respectively, by

|  |  |  |  |
| --- | --- | --- | --- |
|  | m1=μ+(αg+αl)​τ(αg/θg+1)+(αl/θl+1)​(αlθl−αgθg)​αgθg+αlθl+22​π​B​(αgθg+12,12)​B​(αlθl+12,12)m\_{1}=\mu+\sqrt{\frac{(\alpha\_{g}+\alpha\_{l})\tau}{(\alpha\_{g}/\theta\_{g}+1)+(\alpha\_{l}/\theta\_{l}+1)}}\frac{\left(\frac{\alpha\_{l}}{\theta\_{l}}-\frac{\alpha\_{g}}{\theta\_{g}}\right)\sqrt{\frac{\alpha\_{g}}{\theta\_{g}}+\frac{\alpha\_{l}}{\theta\_{l}}+2}}{2\pi\,\mathrm{B}\!\left(\frac{\alpha\_{g}}{\theta\_{g}}+\frac{1}{2},\frac{1}{2}\right)\mathrm{B}\!\left(\frac{\alpha\_{l}}{\theta\_{l}}+\frac{1}{2},\frac{1}{2}\right)}\\ |  | (31) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | m2=(θl​αg+θg​αl)​τ​αg+αl4​αg​αl+(αg+αl)​τ4​(αgθg−αlθl)2​[θg​θlαg​αl−(πB​(αgθg,12)​B​(αlθl,12))2]m\_{2}=(\theta\_{l}\alpha\_{g}+\theta\_{g}\alpha\_{l})\tau\frac{\alpha\_{g}+\alpha\_{l}}{4\alpha\_{g}\alpha\_{l}}+\frac{(\alpha\_{g}+\alpha\_{l})\tau}{4}\left(\frac{\alpha\_{g}}{\theta\_{g}}-\frac{\alpha\_{l}}{\theta\_{l}}\right)^{2}\left[\frac{\theta\_{g}\theta\_{l}}{\alpha\_{g}\alpha\_{l}}-\left(\frac{\pi}{\mathrm{B}\!\left(\frac{\alpha\_{g}}{\theta\_{g}},\frac{1}{2}\right)\mathrm{B}\!\left(\frac{\alpha\_{l}}{\theta\_{l}},\frac{1}{2}\right)}\right)^{2}\right] |  | (32) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | m¯=μ−(αg+αl)​τ​αlθl−αgθg2​(αgθg+32)​(αlθl+32).\overline{m}=\mu-\sqrt{(\alpha\_{g}+\alpha\_{l})\tau}\,\frac{\frac{\alpha\_{l}}{\theta\_{l}}-\frac{\alpha\_{g}}{\theta\_{g}}}{2\sqrt{\left(\frac{\alpha\_{g}}{\theta\_{g}}+\frac{3}{2}\right)\left(\frac{\alpha\_{l}}{\theta\_{l}}+\frac{3}{2}\right)}}. |  | (33) |

## 3 Numerical Results

Table [1](https://arxiv.org/html/2512.23640v1#S3.T1 "Table 1 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") shows parameters of distributions in Sec. [2](https://arxiv.org/html/2512.23640v1#S2 "2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") obtained by Bayesian fitting of 1980-2025 S&P500 returns. Table [2](https://arxiv.org/html/2512.23640v1#S3.T2 "Table 2 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") gives the values of mean m1m\_{1}, variance m2m\_{2}, and mode m¯\overline{m} from equations obtained in that section for each of the distributions. m~\widetilde{m} is evaluated numerically. First and second Pearson coefficients of skewness, ζ1\zeta\_{1} and ζ2\zeta\_{2} are then computed using ([8](https://arxiv.org/html/2512.23640v1#S2.E8 "In 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")). Exponents of power-law tails of the distributions’ CCDF are computed as −2​(αiθi+1)-2\left(\frac{\alpha\_{i}}{\theta\_{i}}+1\right), where αi=α,αg,αl\alpha\_{i}=\alpha,\alpha\_{g},\alpha\_{l} and θi=θ,θg,θl\theta\_{i}=\theta,\theta\_{g},\theta\_{l}. Tail exponents of S&P500 returns are obtained by linear fitting of the tails.

| Simulations | θ\theta | θg\theta\_{g} | θl\theta\_{l} | α\alpha | αg\alpha\_{g} | αl\alpha\_{l} | μ\mu |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Student-t | 1.407×10−41.407\times 10^{-4} | - | - | 7.347×10−57.347\times 10^{-5} | - | - | - |
| Half Student-t | - | 1.182×10−41.182\times 10^{-4} | 1.803×10−41.803\times 10^{-4} | - | 8.512×10−58.512\times 10^{-5} | 6.134×10−56.134\times 10^{-5} | - |
| mJF1 | 1.412×10−41.412\times 10^{-4} | - | - | - | 7.873×10−57.873\times 10^{-5} | 6.371×10−56.371\times 10^{-5} | 1.168×10−31.168\times 10^{-3} |
| mJF2 | - | 1.187×10−41.187\times 10^{-4} | 1.782×10−41.782\times 10^{-4} | - | 6.386×10−56.386\times 10^{-5} | 7.634×10−57.634\times 10^{-5} | 1.142×10−31.142\times 10^{-3} |

Table 1: Fitting parameters of distributions ([7](https://arxiv.org/html/2512.23640v1#S1.E7 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")), ([15](https://arxiv.org/html/2512.23640v1#S2.E15 "In 2.2 Half Student-t Distribution ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")), ([20](https://arxiv.org/html/2512.23640v1#S2.E20 "In 2.3 Modified Jones-Faddy Distribution mJF1 ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")), and ([27](https://arxiv.org/html/2512.23640v1#S2.E27 "In 2.4 Modified Jones-Faddy Distribution mJF2 ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")).



|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Simulations | m1m\_{1} | m2m\_{2} | m¯\overline{m} | ζ1\zeta\_{1} | m~\widetilde{m} | ζ2\zeta\_{2} | Gains | Losses |
| Student-t | 0 | 1.41×10−41.41\times 10^{-4} | 0 | 0 | 0 | 0 | -3.04 | -3.04 |
| Half Student-t | −2.47×10−4-2.47\times 10^{-4} | 1.48×10−41.48\times 10^{-4} | 0 | −2.03×10−2-2.03\times 10^{-2} | 6.047×10−66.047\times 10^{-6} | 2.08×10−22.08\times 10^{-2} | -3.04 | -2.95 |
| mJF1 | 4.57×10−54.57\times 10^{-5} | 1.45×10−41.45\times 10^{-4} | 5.22×10−45.22\times 10^{-4} | −3.96×10−2-3.96\times 10^{-2} | 3.211×10−43.211\times 10^{-4} | 2.29×10−22.29\times 10^{-2} | -3.12 | -2.90 |
| mJF2 | 3.7×10−53.7\times 10^{-5} | 1.3×10−41.3\times 10^{-4} | 5.49×10−45.49\times 10^{-4} | −4.49×10−2-4.49\times 10^{-2} | 3.395×10−43.395\times 10^{-4} | 2.65×10−22.65\times 10^{-2} | -3.07 | -2.76 |
| S&P500 | 4.38×10−54.38\times 10^{-5} | 1.28×10−41.28\times 10^{-4} | 1.32×10−41.32\times 10^{-4} | −7.70×10−3-7.70\times 10^{-3} | 2.733×10−42.733\times 10^{-4} | 2.03×10−22.03\times 10^{-2} | -3.14 | -2.91 |

Table 2: Mean, variance, mode, first Fisher skewness coefficient, median, second Fisher skewness coefficient, and exponents of power-law tails of distributions in Table [1](https://arxiv.org/html/2512.23640v1#S3.T1 "Table 1 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") and S&P500 returns.

Clearly, half Student-t, which does not allow for location parameter, fails to capture positive sign of m1m\_{1}. We point out that positive values of m1m\_{1} in Table [2](https://arxiv.org/html/2512.23640v1#S3.T2 "Table 2 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") are roughly an order of magnitude smaller than μ1\mu\_{1} of the linear fit in Fig. [1](https://arxiv.org/html/2512.23640v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") but are still noon-zero, as illustrated in Fig. [3](https://arxiv.org/html/2512.23640v1#S3.F3 "Figure 3 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution"). Also, the second Fisher coefficients of skewness ζ2\zeta\_{2} of fitted distribution are much closer to S&P500 returns than the first Fisher coefficients ζ1\zeta\_{1}. Specifically for mJF1 and mJF2 it is due to the large discrepancy in the value of the mode m¯\overline{m}. The reason for that is difficulty in identifying the value of the mode in empirical data, as is obvious from Fig. [5](https://arxiv.org/html/2512.23640v1#S3.F5 "Figure 5 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") below (see next paragraph for explanation). In this particular case we used a smoothing procedure to obtain the value of m¯\overline{m} for S&P500.

![Refer to caption](x3.png)


Figure 3: left: xtx\_{t} ([2](https://arxiv.org/html/2512.23640v1#S1.F2 "Figure 2 ‣ 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) for S&P daily returns (τ=1\tau=1) – centered on m1m\_{1}; right: xt−m1x\_{t}-m\_{1}(τ=1\tau=1) – centered on 0.

Figs. [4](https://arxiv.org/html/2512.23640v1#S3.F4 "Figure 4 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")-[7](https://arxiv.org/html/2512.23640v1#S3.F7 "Figure 7 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") show fits of the PDF of the distribution of S&P500 returns using PDF of four distributions described in Sec. [2](https://arxiv.org/html/2512.23640v1#S2 "2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution"). These fits render parameters listed in Table [1](https://arxiv.org/html/2512.23640v1#S3.T1 "Table 1 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution"). Figs. [8](https://arxiv.org/html/2512.23640v1#S3.F8 "Figure 8 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")-[11](https://arxiv.org/html/2512.23640v1#S3.F11 "Figure 11 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") show CCDF of S&P500 returns and CCDF of the four fitting distributions derived in Sec. [2](https://arxiv.org/html/2512.23640v1#S2 "2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") with parameters from Table [1](https://arxiv.org/html/2512.23640v1#S3.T1 "Table 1 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution"). Linear fits of tail areas are also shown in Figs. [9](https://arxiv.org/html/2512.23640v1#S3.F9 "Figure 9 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") and [11](https://arxiv.org/html/2512.23640v1#S3.F11 "Figure 11 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution"). Clearly, visually all four distributions exhibit very close tail behavior, which also only slightly differs from S&P500 tail and its linear fit. This is confirmed by closeness of power-law exponents in Table [2](https://arxiv.org/html/2512.23640v1#S3.T2 "Table 2 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution"). We point out, however, that the distributions of Sec. [2](https://arxiv.org/html/2512.23640v1#S2 "2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") approach power-law behavior only asymptotically and their own linear fits in Figs. [9](https://arxiv.org/html/2512.23640v1#S3.F9 "Figure 9 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") and [11](https://arxiv.org/html/2512.23640v1#S3.F11 "Figure 11 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")would not generally speaking produce exponents listed in Table [2](https://arxiv.org/html/2512.23640v1#S2 "2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution").

Figs. [12](https://arxiv.org/html/2512.23640v1#S3.F12 "Figure 12 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")-[19](https://arxiv.org/html/2512.23640v1#S3.F19 "Figure 19 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") demonstrate the results of statistical tests meant to probe goodness of fit. Figs. [12](https://arxiv.org/html/2512.23640v1#S3.F12 "Figure 12 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") and [14](https://arxiv.org/html/2512.23640v1#S3.F14 "Figure 14 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") show confidence intervals of linear fits and Figs. [16](https://arxiv.org/html/2512.23640v1#S3.F16 "Figure 16 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") and [18](https://arxiv.org/html/2512.23640v1#S3.F18 "Figure 18 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") show confidence intervals of mJF1 fits. Confidence intervals are obtained using inversion of the binomial distribution [janczura2012black] and we specifically focused on mJF1 as the most transparent and minimal generalization of Student t-distribution. Figs. [13](https://arxiv.org/html/2512.23640v1#S3.F13 "Figure 13 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") and [15](https://arxiv.org/html/2512.23640v1#S3.F15 "Figure 15 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") show p-values of order-statistics-based U-test [pisarenko2012robust] 444We are using eq. (14) in [liu2023dragon] for evaluation of p-values. for linear fits and Figs. [17](https://arxiv.org/html/2512.23640v1#S3.F17 "Figure 17 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") and [19](https://arxiv.org/html/2512.23640v1#S3.F19 "Figure 19 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") show p-values for mJF1 fits. It should be noted that both approaches were developed for detections of outliers, such as Dragon Kings and negative Dragon Kings, in the tails of the distributions. For instance values p<0.05p<0.05 and p>0.95p>0.95 would signal a 95% probability of having, respectively, a Dragon King and a negative Dragon King. In simpler terms, if a data point falls outside the confidence interval and/or if its p-value or (1-p)-value is very small, then it most likely does not belong to the fitting distribution (linear fit being the tail of Pareto distribution).

![Refer to caption](x4.png)


Figure 4: PDF of stocks returns and fits with distributions ([7](https://arxiv.org/html/2512.23640v1#S1.E7 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")), ([15](https://arxiv.org/html/2512.23640v1#S2.E15 "In 2.2 Half Student-t Distribution ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")), ([20](https://arxiv.org/html/2512.23640v1#S2.E20 "In 2.3 Modified Jones-Faddy Distribution mJF1 ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")), and ([27](https://arxiv.org/html/2512.23640v1#S2.E27 "In 2.4 Modified Jones-Faddy Distribution mJF2 ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")).

![Refer to caption](x5.png)


Figure 5: Expanded view of the area around the mode of the distribution in Fig. [4](https://arxiv.org/html/2512.23640v1#S3.F4 "Figure 4 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution").

![Refer to caption](x6.png)


Figure 6: Expanded view of the tail area of Fig. [4](https://arxiv.org/html/2512.23640v1#S3.F4 "Figure 4 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") for gains.

![Refer to caption](x7.png)


Figure 7: Expanded view of the tail area of Fig. [4](https://arxiv.org/html/2512.23640v1#S3.F4 "Figure 4 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution") for losses.

![Refer to caption](x8.png)


Figure 8: CCDF of gains with CCDF of fitting distributions.

![Refer to caption](x9.png)


Figure 9: Expanded view of the tail area of Fig. [8](https://arxiv.org/html/2512.23640v1#S3.F8 "Figure 8 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution").

![Refer to caption](x10.png)


Figure 10: CCDF of losses with CCDF of fitting distributions.

![Refer to caption](x11.png)


Figure 11: Expanded view of the tail area of Fig. [10](https://arxiv.org/html/2512.23640v1#S3.F10 "Figure 10 ‣ 3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution").

![Refer to caption](x12.png)


Figure 12:  Linear fit, with its confidence interval, of the tail of the S&P500 distribution of daily gains; mJF1 and mJF2 fits are shown for comparison.

![Refer to caption](x13.png)


Figure 13: p-values of statistical U-test for the linear fit of the S&P500 distribution of daily gains.

![Refer to caption](x14.png)


Figure 14: Linear fit, with its confidence interval, of the tail of the S&P500 distribution of daily losses; mJF1 and mJF2 fits are shown for comparison.

![Refer to caption](x15.png)


Figure 15: p-values of statistical U-test for the linear fit of the S&P500 distribution of daily losses.

![Refer to caption](x16.png)


Figure 16: mJF1 fit, with its confidence interval, of the tail of the S&P500 distribution of daily gains.

![Refer to caption](x17.png)


Figure 17: p-values of statistical U-test for mJF1 fit of the S&P500 distribution of daily gains.

![Refer to caption](x18.png)


Figure 18: mJF1 fit, with its confidence interval, of the tail of the S&P500 distribution of daily losses.

![Refer to caption](x19.png)


Figure 19: p-values of statistical U-test for mJF1 fit of the S&P500 distribution of daily losses.

## 4 Conclusions and Discussion

The purpose of this work was to glean insight into and to try to analytically describe key empirical findings about S&P500 1980-2025 returns: heavier tails of losses, leading to the negative skew of the distribution, and positive mean of the distribution, which cannot be entirely attributed to the larger numbers of gains than losses. Our main conclusion is that a modified Jones-Faddy skew t-distribution, ([20](https://arxiv.org/html/2512.23640v1#S2.E20 "In 2.3 Modified Jones-Faddy Distribution mJF1 ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution"))-([23](https://arxiv.org/html/2512.23640v1#S2.E23 "In 2.3 Modified Jones-Faddy Distribution mJF1 ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) is most likely the best candidate for the stated purpose, even though it is currently unknown how to derive it from first-principles stochastic differential equations.

The main idea behind symmetry breaking of Student t-distribution [7](https://arxiv.org/html/2512.23640v1#S1.E7 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution"), which is based on ([1](https://arxiv.org/html/2512.23640v1#S1.E1 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) and ([2](https://arxiv.org/html/2512.23640v1#S1.E2 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")), is that the latter equation for stochastic volatility is governed by a different set of parameters for gains and losses. In this particular case we operated on the basis of multiplicative model of stochastic volatility ([3](https://arxiv.org/html/2512.23640v1#S1.E3 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution"))-([6](https://arxiv.org/html/2512.23640v1#S1.E6 "In 1 Introduction ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) and so main culprit for explaining heavier power-law dependence of losses is assuming that resulting parameter for losses, αl\alpha\_{l}, is smaller than that for gains, αg\alpha\_{g}, hence the modified Jones-Faddy skew t-distribution mJF1, ([20](https://arxiv.org/html/2512.23640v1#S2.E20 "In 2.3 Modified Jones-Faddy Distribution mJF1 ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")). An additional innocuous introduction of the location parameter helps to explain the positive mean of the distribution. The location parameter seems to account not only for larger number of gains than losses but also for larger values of gains in the bulk of the distribution which offsets the heavier negative tails.

mJF1 still implies that the mean stochastic volatility θ\theta is the same for gains and losses. To account for the possibility to the contrary we introduced two other distributions with different mean volatilities for gains and losses, θg\theta\_{g} and θl\theta\_{l}: a mixture half Student-t distribution, ([15](https://arxiv.org/html/2512.23640v1#S2.E15 "In 2.2 Half Student-t Distribution ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution"))-([17](https://arxiv.org/html/2512.23640v1#S2.E17 "In 2.2 Half Student-t Distribution ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")) and its simplified form with θg=θg=θ\theta\_{g}=\theta\_{g}=\theta, and the second modified Jones-Faddy distribution mJF2, ([27](https://arxiv.org/html/2512.23640v1#S2.E27 "In 2.4 Modified Jones-Faddy Distribution mJF2 ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution"))-([30](https://arxiv.org/html/2512.23640v1#S2.E30 "In 2.4 Modified Jones-Faddy Distribution mJF2 ‣ 2 Analytical Framework ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution")). The advantage of the former is that it is still rooted in the stochastic differential equation framework. However, due to its structure, it fails to account for the positive mean of actual returns – daily S&P500 returns in this case. mJF2, despite and extra parameter, showed virtually no difference relative to mJF1 in fitting the empirical data, both visually and based on statistical tests described in Sec. [3](https://arxiv.org/html/2512.23640v1#S3 "3 Numerical Results ‣ Broken Symmetry of Stock Returns - a Modified Jones-Faddy Skew t-Distribution"). Consequently we believe that mJF1 is the cleanest and most transparent generalization of Student-t for describing daily S&P500 returns.

There are a number of possible future directions of this work. The most obvious is to consider other market indices. From our previous experience, we expect that DOW will not exhibit significant difference with S&P500, both in overall behavior and values of parameters. However other long-lasting US indices, such as Russel and NASDAQ, are worth looking into, as well as European and Asian ones. Also overall market returns, reflected by key indices, versus individual companies is a rather challenging question [albuquerque2012skewnwss]. Yet another important avenue is the study of accumulated returns versus dailies: most importantly realized volatility, which shows linear behavior as the function of the number of days of accumulation, and rather abrupt drop off in the tails for longer accumulations. Of course, the most challenging task is finding first-principles explanation of symmetry breaking described in this work.

## 5 Data Availability

We obtained S&P500 data at Yahoo! Finance. Our datasets are available upon request.

## 6 Acknoledgments

We used MathWorks Matlab for numerical work and Wolfram Mathematica for analytical calculations.

## 7 Conflicts of Interest

The authors declare no conflicts of interest.