---
authors:
- Keyuan Wu
- Tenghan Zhong
- Yuxuan Ouyang
doc_id: arxiv:2510.19126v1
family_id: arxiv:2510.19126
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: An Efficient Calibration Framework for Volatility Derivatives under Rough Volatility
  with Jumps
url_abs: http://arxiv.org/abs/2510.19126v1
url_html: https://arxiv.org/html/2510.19126v1
venue: arXiv q-fin
version: 1
year: 2025
---


Keyuan Wu 111Department of Mathematics, University of Southern California. Email: <keyuanwu@usc.edu>.
  
Tenghan Zhong 222Department of Mathematics, University of Southern California. Email: <tenghanz@usc.edu>.
  
Yuxuan Ouyang 333Department of Mathematics, University of Southern California. Email: <yuxuanou@usc.edu>.

(2025)

###### Abstract

We present a fast and robust calibration method for stochastic volatility models that admit Fourier-analytic transform-based pricing via characteristic functions. The design is structure-preserving: we keep the original pricing transform and (i) split the pricing formula into data-independent integrals and a market-dependent remainder; (ii) precompute those data-independent integrals with GPU acceleration; and (iii) approximate only the remaining, market-dependent pricing map with a small neural network. We instantiate the workflow on a rough volatility model with tempered-stable jumps tailored to power-type volatility derivatives and calibrate it to VIX options with a global-to-local search. We verify that a pure-jump rough volatility model adequately captures the VIX dynamics, consistent with prior empirical findings, and demonstrate that our calibration method achieves high accuracy and speed.

Keywords: Rough volatility, VIX options, Volatility jumps, Option Calibration, Neural network, Cupy

## 1 Introduction

### 1.1 Literature Review

Stochastic volatility modeling has evolved to capture two key empirical features of financial markets: the highly irregular (“rough”) behavior of volatility over short horizons, and the prevalence of jumps rather than smooth diffusion.

Todorov and Tauchen ([2011](https://arxiv.org/html/2510.19126v1#bib.bib1)) provide compelling nonparametric evidence—using high‐frequency VIX data—that volatility is best described as a pure‐jump process with infinitely many small jumps and occasional large spikes. In their framework the estimated activity index is strictly below 2, ruling out any continuous Brownian component and demonstrating that even the smallest fluctuations are jump‐driven.

Gatheral et al. ([2018](https://arxiv.org/html/2510.19126v1#bib.bib2)) document that realized volatility time series exhibit a Hurst exponent well below 0.5, giving rise to the “rough volatility” paradigm in which volatility paths have very short‐memory dependence reminiscent of fractional Brownian motion with Hurst around 0.1.

Integrating these strands, Wang and Xia ([2022](https://arxiv.org/html/2510.19126v1#bib.bib3)) introduce a unified model that drives instantaneous variance by a generalized fractional Ornstein–Uhlenbeck process (to capture roughness) alongside a tempered‐stable Lévy subordinator and an independent sinusoidal jump component (to capture infinite‐activity jumps). Thanks to this construction, the characteristic function of the 30‐day average‐forward variance admits a semi‐closed‐form expression, enabling Fourier‐based pricing of a general class of power‐type volatility derivatives. Empirical calibrations to VIX option data—both before and during the 2020 COVID‐19 crisis—show that this pure‐jump rough model fits market prices accurately across a wide range of maturities and strikes.

However, the nested Volterra and Lévy integrals in these models render direct calibration computationally intensive, prompting Ruijter and Oosterlee ([2015](https://arxiv.org/html/2510.19126v1#bib.bib4)) to adapt the Fourier‐cosine expansion for efficient transform inversion, and Bennedsen et al. ([2017](https://arxiv.org/html/2510.19126v1#bib.bib5)) to propose a hybrid scheme blending Gauss–Laguerre quadrature with FFT for rough models. More recently, Horvath et al. ([2021](https://arxiv.org/html/2510.19126v1#bib.bib6)) demonstrated that neural‐network surrogates can learn the pricing map offline and deliver implied volatilities over entire surfaces in milliseconds, effectively bypassing repeated integral evaluations.

Our work builds on these advances by developing a bespoke calibration algorithm for the rough‐OU jump model of Wang and Xia. Instead of relying on generic machine‐learning surrogates, we exploit the semi‐analytical characteristic‐function formulas to pre‐tabulate key integrals, leverage mpmath for high‐precision quadrature, and then train a lightweight neural surrogate for the remaining map—thereby reducing end‐to‐end VIX calibration times by over an order of magnitude without sacrificing interpretability.

## 2 Mathematical Models

In this section, we will introduce underlying models first, then show how we transform them and implement “mpmath” to make them computable in calibration.

### 2.1 Underlying Theoretic Model Formulation

To model VIX, this paper starts from an instantaneous variance process, denoted as V≡(VtV\equiv(V\_{t}), by assuming the following quasi‐Ornstein–Uhlenbeck structure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt∘=V0∘​e−κ​t+V¯​(1−e−κ​t)+Xt(h),Vt=Vt∘+ς​(cos⁡Zt+1),t≥0.V\_{t}^{\circ}=V\_{0}^{\circ}e^{-\kappa t}+\bar{V}\bigl(1-e^{-\kappa t}\bigr)+X\_{t}^{(h)},\quad V\_{t}=V\_{t}^{\circ}+\varsigma\bigl(\cos Z\_{t}+1\bigr),\quad t\geq 0. |  | (1) |

where V¯\bar{V} is a universal reversion level, XX is a Lévy subordinator, with Lévy–Khintchine representation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡ϕX1​(l):=log⁡𝔼​[ei​l​X1]=∫0∞(ei​l​z−1)​νX​(d​z),l∈ℝ,\log\phi\_{X\_{1}}(l)\;:=\;\log\mathbb{E}\bigl[e^{ilX\_{1}}\bigr]\;=\;\int\_{0}^{\infty}\bigl(e^{ilz}-1\bigr)\,\nu\_{X}(dz),\quad l\in\mathbb{R}, |  | (2) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξ1:=𝔼​[X1]> 0\xi\_{1}\;:=\;\mathbb{E}[X\_{1}]\;>\;0 |  | (3) |

leading to the following characteristic exponent:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡ϕX1​(l)=a​Γ​(−c)​((b−i​l)c−bc),l∈ℝ,\log\phi\_{X\_{1}}(l)\;=\;a\,\Gamma(-c)\bigl((b-i\,l)^{c}-b^{c}\bigr),\quad l\in\mathbb{R}, |  | (4) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξ1=a​Γ​(1−c)b 1−c.\xi\_{1}\;=\;\frac{a\,\Gamma(1-c)}{b^{\,1-c}}. |  | (5) |

Expresses VV as a Volterra-type stochastic integral:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt=Vt∘​e−κ​t+V¯​(1−e−κ​t)+∫0t0h​(t,s)​𝑑Xs+∫t0th​(t,s)​𝑑Xs+ζ​(cos⁡(Zt−Zt0)​cos⁡Zt0−sin⁡(Zt−Zt0)​sin⁡Zt0+1)V\_{t}=V\_{t}^{\circ}e^{-\kappa t}+\bar{V}\bigl(1-e^{-\kappa t}\bigr)+\int\_{0}^{t\_{0}}h(t,s)\,dX\_{s}+\int\_{t\_{0}}^{t}h(t,s)\,dX\_{s}+\zeta\bigl(\cos(Z\_{t}-Z\_{t\_{0}})\cos Z\_{t\_{0}}-\sin(Z\_{t}-Z\_{t\_{0}})\sin Z\_{t\_{0}}+1\bigr) |  | (6) |

where h​(t,s)h(t,s) is the kernel, we have tried the Ornstein-Uhlenbeck type II kernel, but due to computational complexity, we use the type III piecewise kernel for our calibration to avoid incomplete Gamma, for the d∈(0.5,1)d\in(0.5,1) type III kernel:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(t−s)={(t−s)d−1−(1−dκ)d−1Γ​(d)−κ1−d(1−d)2−d​Γ​(d−1),t−s<1−dκ,−(e​κ)1−d​e−κ​(t−s)(1−d)2−d​Γ​(d−1),t−s≥1−dκh(t-s)\;=\;\begin{cases}\displaystyle\frac{(t-s)^{d-1}-\Bigl(\frac{1-d}{\kappa}\Bigr)^{d-1}}{\Gamma(d)}\;-\;\frac{\kappa^{1-d}}{(1-d)^{2-d}\,\Gamma(d-1)},&t-s<\frac{1-d}{\kappa},\\[11.99998pt] \displaystyle-\;\frac{(\mathrm{e}\,\kappa)^{1-d}\,e^{-\kappa(t-s)}}{(1-d)^{2-d}\,\Gamma(d-1)},&t-s\geq\frac{1-d}{\kappa}\end{cases} |  | (7) |

  

And the delta-forward integrated kernel we use is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | HΔ​(t,s):=1Δ​∫0Δh​(t+u,s)​𝑑uH\_{\Delta}(t,s)\;:=\;\frac{1}{\Delta}\int\_{0}^{\Delta}h\bigl(t+u,s\bigr)\,du |  | (8) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | HΔ​(t,s)=HΔ​(t−s)={(t−s+Δ)d−(t−s)dΔ​Γ​(d+1),t−s+Δ<1−dκ,(1−dκ)d−(t−s)dΔ​Γ​(d+1)+e−κ​(t−s+Δ)+1−d−1κd​Δ​(1−d)2−d​Γ​(d−1),t−s<1−dκ≤t−s+Δ,−e−κ​(t−s+Δ)+1−d​(eκ​Δ−1)κd​Δ​(1−d)2−d​Γ​(d−1),t−s≥1−dκ.H\_{\Delta}(t,s)\;=\;H\_{\Delta}(t-s)\;=\;\begin{cases}\displaystyle\frac{(t-s+\Delta)^{d}-(t-s)^{d}}{\Delta\,\Gamma(d+1)},&t-s+\Delta<\frac{1-d}{\kappa},\\[10.00002pt] \displaystyle\frac{\bigl(\tfrac{1-d}{\kappa}\bigr)^{d}-(t-s)^{d}}{\Delta\,\Gamma(d+1)}\;+\;\frac{e^{-\kappa(t-s+\Delta)+1-d}-1}{\kappa^{d}\,\Delta\,(1-d)^{2-d}\,\Gamma(d-1)},&t-s<\frac{1-d}{\kappa}\;\leq\;t-s+\Delta,\\[10.00002pt] \displaystyle-\;\frac{e^{-\kappa(t-s+\Delta)+1-d}\,\bigl(e^{\kappa\Delta}-1\bigr)}{\kappa^{d}\,\Delta\,(1-d)^{2-d}\,\Gamma(d-1)},&t-s\geq\frac{1-d}{\kappa}.\end{cases} |  | (9) |

Then based on instantaneous variance, we express forward variance curve structure as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V~t​(u):=𝔼​[Vt+u∣ℱt],u>0,t≥0.\widetilde{V}\_{t}(u)\;:=\;\mathbb{E}\bigl[V\_{t+u}\mid\mathcal{F}\_{t}\bigr],\quad u>0,\;t\geq 0. |  | (10) |

With stochastic representation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V~t​(u)=V~t∘​(u)+Ut​(u),u>0,t≥0.\widetilde{V}\_{t}(u)=\widetilde{V}\_{t}^{\circ}(u)+U\_{t}(u),\quad u>0,\;t\geq 0. |  | (11) |

where forward variance rising from the generalized fractional Ornstein–Uhlenbeck process V0V^{0} is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V~t∘​(u)=V0∘​e−κ​(t+u)+V¯​(1−e−κ​(t+u))+∫0th​(t+u,s)​𝑑Xs+ξ1​∫tt+uh​(t+u,s)​𝑑s\widetilde{V}\_{t}^{\circ}(u)=V\_{0}^{\circ}e^{-\kappa(t+u)}+\bar{V}\bigl(1-e^{-\kappa(t+u)}\bigr)+\int\_{0}^{t}h\bigl(t+u,s\bigr)\,dX\_{s}+\xi\_{1}\int\_{t}^{\,t+u}h\bigl(t+u,s\bigr)\,ds |  | (12) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ut​(u)=ς​(𝔼​[cos⁡Zu]​cos⁡Zt−𝔼​[sin⁡Zu]​sin⁡Zt+ 1).U\_{t}(u)=\varsigma\Bigl(\mathbb{E}[\cos Z\_{u}]\,\cos Z\_{t}\;-\;\mathbb{E}[\sin Z\_{u}]\,\sin Z\_{t}\;+\;1\Bigr). |  | (13) |

comes from the composite‐sinusoidal Lévy process.
  
Then, we can get average-forward volatility process, which is square root of the delta-running average of the forward variance process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | It​(Δ):=1Δ​∫0ΔV~t​(u)​du,t≥0.I\_{t}(\Delta)\;:=\;\sqrt{\;\frac{1}{\Delta}\int\_{0}^{\Delta}\widetilde{V}\_{t}(u)\,\mathrm{d}u\;},\quad t\geq 0. |  | (14) |

by Fubini-Tonelli theorem:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | It2​(Δ)\displaystyle I\_{t}^{2}(\Delta) | :=1Δ​∫0ΔV~t​(u)​du\displaystyle=\frac{1}{\Delta}\int\_{0}^{\Delta}\widetilde{V}\_{t}(u)\,\mathrm{d}u |  | (15) |
|  |  | =V0∘​e−κ​t−e−κ​(t+Δ)κ​Δ+V¯​(1−e−κ​t−e−κ​(t+Δ)κ​Δ)+Xt(H​Δ)+ξ1​YΔ​(t)\displaystyle=V\_{0}^{\circ}\frac{e^{-\kappa t}-e^{-\kappa(t+\Delta)}}{\kappa\,\Delta}+\bar{V}\Bigl(1-\frac{e^{-\kappa t}-e^{-\kappa(t+\Delta)}}{\kappa\,\Delta}\Bigr)+X\_{t}^{(H\Delta)}+\xi\_{1}\,Y\_{\Delta}(t) |  |
|  |  | +ςΔ​(∫0Δ𝔼​[cos⁡Zu]​du​cos⁡Zt−∫0Δ𝔼​[sin⁡Zu]​du​sin⁡Zt+Δ)\displaystyle\quad+\frac{\varsigma}{\Delta}\Bigl(\int\_{0}^{\Delta}\mathbb{E}[\cos Z\_{u}]\,\mathrm{d}u\;\cos Z\_{t}-\int\_{0}^{\Delta}\mathbb{E}[\sin Z\_{u}]\,\mathrm{d}u\;\sin Z\_{t}+\Delta\Bigr)\, |  |

At this point, based on Rough‐OU Volterra driven by tempered‐stable subordinator, we have all the necessary tools to give an integral formula for the conditional characteristic function of the average‐forward variance:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ϕIt2​(Δ)∣t0​(l)\displaystyle\phi\_{I\_{t}^{2}(\Delta)\mid t\_{0}}(l) | :=𝔼​[ei​l​It2​(Δ)∣ℱt0]\displaystyle=\mathbb{E}\bigl[e^{i\,l\,I\_{t}^{2}(\Delta)}\mid\mathcal{F}\_{t\_{0}}\bigr] |  | (16) |
|  |  | =1π​exp⁡{i​l​J​(t,t0,Δ)+∫t0tlog⁡ϕX1​(l​HΔ​(t,s))​𝑑s}\displaystyle=\frac{1}{\pi}\exp\!\Bigl\{\,i\,l\,J(t,t\_{0},\Delta)+\int\_{t\_{0}}^{t}\!\log\phi\_{X\_{1}}\bigl(l\,H\_{\Delta}(t,s)\bigr)\,ds\Bigr\} |  |
|  |  | ×∫ℝψ(l,x;t0,Δ)∫0∞ℜ[e−i​ℓ​xϕZ1t−t0(ℓ)]dℓdx,l∈ℝ.\displaystyle\quad\times\int\_{\mathbb{R}}\psi\bigl(l,x;t\_{0},\Delta\bigr)\int\_{0}^{\infty}\Re\bigl[e^{-i\,\ell\,x}\,\phi\_{Z\_{1}}^{\,t-t\_{0}}(\ell)\bigr]\,d\ell\,dx,\quad l\in\mathbb{R}. |  |

Finally, we use equation ([24](https://arxiv.org/html/2510.19126v1#S2.E24 "In 2.2 Calibration Framework: Equation Transformations and mpmath Implementation ‣ 2 Mathematical Models ‣ An Efficient Calibration Framework for Volatility Derivatives under Rough Volatility with Jumps")) to price call options and calibrate based on the optimization of equation ([34](https://arxiv.org/html/2510.19126v1#S4.E34 "In 4.5 Option Calibration ‣ 4 Calibration Methodology ‣ An Efficient Calibration Framework for Volatility Derivatives under Rough Volatility with Jumps"))

### 2.2 Calibration Framework: Equation Transformations and mpmath Implementation

In the conditional characteristic function, we set ζ=0.01\zeta=0.01, and:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ(l,x;t0,Δ):=exp(i​l​ζΔ(ℜ[ϕZ1Δ​(1)−1log⁡ϕZ1​(1)](cosxcosZt0−sinxsinZt0)−ℑ[ϕZ1Δ​(1)−1log⁡ϕZ1​(1)](sinxcosZt0+cosxsinZt0)+Δ)).\psi\bigl(l,x;\,t\_{0},\Delta\bigr):=\exp\Biggl(\frac{i\,l\,\zeta}{\Delta}\,\Biggr(\Re\!\Bigl[\frac{\phi^{\Delta}\_{Z\_{1}}(1)-1}{\log\phi\_{Z\_{1}}(1)}\Bigr]\bigl(\cos x\cos Z\_{t\_{0}}-\sin x\sin Z\_{t\_{0}}\bigr)-\Im\!\Bigl[\frac{\phi^{\Delta}\_{Z\_{1}}(1)-1}{\log\phi\_{Z\_{1}}(1)}\Bigr]\bigl(\sin x\cos Z\_{t\_{0}}+\cos x\sin Z\_{t\_{0}}\bigr)+\Delta\Biggr)\Biggr). |  | (17) |

and JJ is kernel-modulated forward variance quantity which contains all information about spot prices:

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,t0,Δ):=1Δ​∫t−t0t−t0+ΔV~t0∘​(u)​du−ξ1​∫t0tHΔ​(t,s)​ds> 0.J(t,t\_{0},\Delta):=\frac{1}{\Delta}\int\_{\,t-t\_{0}}^{\,t-t\_{0}+\Delta}\widetilde{V}\_{t\_{0}}^{\circ}(u)\,\mathrm{d}u\;-\;\xi\_{1}\int\_{\,t\_{0}}^{\,t}H\_{\Delta}(t,s)\,\mathrm{d}s\;>\;0. |  | (18) |

Then as we cannot compute VV in the offline step, we employ an expansion argument to transform JJ into a linear combination of square spot price to avoid all VV:

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,t0,Δ)=It02​(Δ)−ξ1​∫t0tHΔ​(t,s)​ds+r​(t0,t).J(t,t\_{0},\Delta)\;=\;I\_{t\_{0}}^{2}(\Delta)\;-\;\xi\_{1}\int\_{t\_{0}}^{t}H\_{\Delta}(t,s)\,\mathrm{d}s\;+\;r(t\_{0},t)\,. |  | (19) |

Now we have everything computable:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ΦIt2​(Δ)∣t0​(l)\displaystyle\Phi\_{I\_{t}^{2}(\Delta)\mid t\_{0}}(l) | =1π​exp⁡{i​l​[It02​(Δ)−ξ1​∫t0tHΔ​(t,s)​ds+r​(t0,t)]+∫t0tlog⁡ϕX1​(l​HΔ​(t,s))​ds}\displaystyle=\frac{1}{\pi}\,\exp\Biggl\{\,i\,l\Bigl[I\_{t\_{0}}^{2}(\Delta)-\xi\_{1}\int\_{t\_{0}}^{t}H\_{\Delta}(t,s)\,\mathrm{d}s+r(t\_{0},t)\Bigr]+\int\_{t\_{0}}^{t}\!\log\phi\_{X\_{1}}\bigl(l\,H\_{\Delta}(t,s)\bigr)\,\mathrm{d}s\Biggr\} |  | (20) |
|  |  | ×∫ℝψ(l,x;t0,Δ)∫0∞ℜ[e−i​x​ℓϕZ1t−t0(ℓ)]dℓdx,l∈ℝ.\displaystyle\quad\times\int\_{\mathbb{R}}\psi\bigl(l,x;\,t\_{0},\Delta\bigr)\int\_{0}^{\infty}\Re\bigl[e^{-i\,x\,\ell}\,\phi\_{Z\_{1}}^{\,t-t\_{0}}(\ell)\bigr]\,\mathrm{d}\ell\,\mathrm{d}x,\quad l\in\mathbb{R}. |  |

where ZZ is symmetric 1.715 - stable auxiliary Lévy process, and the value of α\alpha is updated and we will illustrate in section 3:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕZ1​(l)=e−|l|α,α≈1.715.\phi\_{Z\_{1}}(l)=e^{-|l|^{\alpha}},\qquad\alpha\approx 1.715. |  | (21) |

Then, we mainly implement ’mpmath’ to numerically compute equations and simulate integrations because of its arbitrary-precision arithmetic, adaptive numerical integration for both real and complex integrands (mpmath.quad) and implementations of incomplete Gamma functions.
  
To numerically compute infinite integral, we set different limits for different functions to accelerate calibration, in the integral:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0∞ℜ⁡[e−i​ℓ​x​ϕZ1t−t0​(ℓ)]​𝑑ℓ\int\_{0}^{\infty}\Re\bigl[e^{-i\,\ell\,x}\,\phi\_{Z\_{1}}^{\,t-t\_{0}}(\ell)\bigr]\,d\ell |  | (22) |

We set the upper limit to 30 because of the exponential term of  ϕZ1t−t0\phi\_{Z\_{1}}^{\,t-t\_{0}} converges quickly.
  
For the double integral,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝψ​(l,x;t0,Δ)​∫0∞ℜ⁡[e−i​x​ℓ​ϕZ1t−t0​(ℓ)]​dℓ​dx\int\_{\mathbb{R}}\psi\bigl(l,x;\,t\_{0},\Delta\bigr)\int\_{0}^{\infty}\Re\bigl[e^{-i\,x\,\ell}\,\phi\_{Z\_{1}}^{\,t-t\_{0}}(\ell)\bigr]\,\mathrm{d}\ell\,\mathrm{d}x |  | (23) |

We set the lower limit to -30 and the upper limit to 30 due to s​i​nsin and c​o​scos term of ψ​(l,x;t0,Δ)\psi\bigl(l,x;\,t\_{0},\Delta\bigr) converges quickly.
  
And set all other limits of infinite integrals from -10000 to 10000 via Simpson’s rule .
  
Then, after computing the conditional characteristic function, we model asymmetric power-type options with:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P0(1,1,(a))=K2−1π​∫0∞ℜ⁡[(K​e−i​K2​l+π/2−Γ​(32,i​K2​l)i​l)​ΦIt2​(Δ)∣t0​(l)i​l]​dl.P\_{0}^{(1,1,(a))}=\;\frac{K}{2}-\;\frac{1}{\pi}\int\_{0}^{\infty}\Re\!\Biggl[\Bigl(K\,e^{-iK^{2}l}+\frac{\sqrt{\pi}/2\;-\;\Gamma\!\bigl(\tfrac{3}{2},\,iK^{2}l\bigr)}{\sqrt{i\,l}}\Bigr)\frac{\Phi\_{I\_{t}^{2}(\Delta)\mid t\_{0}}(l)}{i\,l}\Biggr]\,\mathrm{d}l. |  | (24) |

Incomplete Gamma functions and complex numbers in this equation are numerically inefficient to compute and are the main reasons for us to use mpmath.

## 3 Data

### 3.1 Data Description

We evaluate the model’s performance by calibrating on real VIX index data. These data were collected from the Bloomberg terminal. We use VIX option quotes from a single trading day, January 2, 2025—the first trading day of the new year following the presidential election.

The dataset comprises 96 observations of VIX put options at four maturities, T∈{20,48,100,258}T\in\{20,48,100,258\} days. The spot price is I=0.1793I=0.1793, and strikes range from K=0.09K=0.09 to 0.280.28. A summary appears in Table [1](https://arxiv.org/html/2510.19126v1#S3.T1 "Table 1 ‣ 3.1 Data Description ‣ 3 Data ‣ An Efficient Calibration Framework for Volatility Derivatives under Rough Volatility with Jumps").

Table 1: Summary of original VIX put‐option data.

| Column | Non-Null Rows |
| --- | --- |
| Strike | 96 |
| IVM\_call | 96 |
| Volm\_call | 96 |
| TTM\_year | 96 |
| mid\_price\_call | 96 |
| IVM\_Put | 96 |
| Volm\_Put | 96 |
| mid\_price\_put | 96 |
| spot\_price | 96 |
| Bid | 96 |
| Ask | 96 |
| Bid\_Put | 96 |
| Ask\_Put | 96 |

### 3.2 Implied Volatility

Although implied volatility is not a direct input parameter, it still guides our parameter intuition. Figure [1](https://arxiv.org/html/2510.19126v1#S3.F1 "Figure 1 ‣ 3.2 Implied Volatility ‣ 3 Data ‣ An Efficient Calibration Framework for Volatility Derivatives under Rough Volatility with Jumps") shows Figure 2 shows how the implied volatility of put option changes over strike price KK under different time to maturity TT.

![Refer to caption](IVM.png)


Figure 1: Implied volatility of VIX put options versus strike price for different maturities.

It shows that shorter TT yield steeper smiles (more jump risk in the short term), while the long‐term curve is uneven—suggesting data noise or low liquidity.

### 3.3 Arbitrage Testing

The option pricing model is based on the assumption of risk‐neutral condition, so we conduct 2 data cleaning method to remove the arbitrage prices:

##### Monotonicity Test

For European VIX put options, price must be non‐decreasing in the strike:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ki≤Ki+1⟹P​(Ki)≤P​(Ki+1).K\_{i}\leq K\_{i+1}\quad\Longrightarrow\quad P(K\_{i})\leq P(K\_{i+1}). |  | (25) |

##### Convexity Test

To avoid butterfly arbitrage, for each triple (Ki−1,Ki,Ki+1)(K\_{i-1},K\_{i},K\_{i+1}) we check

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(Ki)≤Ki+1−KiKi+1−Ki−1​P​(Ki−1)+Ki−Ki−1Ki+1−Ki−1​P​(Ki+1).P(K\_{i})\;\leq\;\frac{K\_{i+1}-K\_{i}}{K\_{i+1}-K\_{i-1}}\,P(K\_{i-1})\;+\;\frac{K\_{i}-K\_{i-1}}{K\_{i+1}-K\_{i-1}}\,P(K\_{i+1}). |  | (26) |

If P​(Ki)P(K\_{i}) exceeds this interpolated value, we record a convexity violation (butterfly arbitrage).We drop any observations failing these two tests (see Appendix LABEL:app:mono-conv). After filtering, we will apply the remaining 35 pairs of observations to the calibration.

### 3.4 VIX Activity Index

In the previous section, the modeling of average-forward volatility is based on the assumption that the VIX index is a pure jump process. According to Todorov and Tauchen (2011), we validate this assumption by calculating the volatility activity index β\beta.
β\beta generalizes the classical Blumenthal–Getoor index the Blumenthal–Getoor index (Blumenthal and Getoor, 1961) to arbitrary semimartingales and quantifies the pathwise “vibrancy” of a stochastic process. According to Todorov and Tauchen (2011), higher values of β\beta reflect more frequent or finer-scale fluctuations. Their empirical analysis reveals that the volatility process lacks a Brownian diffusion component but exhibits intense jump activity, with β\beta approaching 2—indicative of behavior close to that of a continuous martingale. This dynamic, characterized by numerous small jumps and occasional large ones, aligns with a Lévy-type pure-jump process of infinite variation. Accordingly, when
β∈[1,2)\beta\in[1,2),the estimated beta is best characterized as a pure-jump process of infinite variation. Such result can be verified by the underlying calculation process

### Power Variation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt​(X,p,Δn)={∑i=1[1Δn]|Δ​Xi|p⋅𝕀​(|Δ​Xi|≤L),if ​p<2∑i=1[1Δn]|Δ​Xi|p,if ​p≥2V\_{t}(X,p,\Delta\_{n})=\begin{cases}\sum\_{i=1}^{\left[\frac{1}{\Delta\_{n}}\right]}|\Delta X\_{i}|^{p}\cdot\mathbb{I}(|\Delta X\_{i}|\leq L),&\text{if }p<2\\ \sum\_{i=1}^{\left[\frac{1}{\Delta\_{n}}\right]}|\Delta X\_{i}|^{p},&\text{if }p\geq 2\end{cases} |  | (27) |

### Activity Signature Function

|  |  |  |  |
| --- | --- | --- | --- |
|  | bX,t​(p)=ln⁡2⋅pln⁡2+ln⁡Vt​(X,p,2​Δn)−ln⁡Vt​(X,p,Δn)b\_{X,t}(p)=\frac{\ln 2\cdot p}{\ln 2+\ln V\_{t}(X,p,2\Delta\_{n})-\ln V\_{t}(X,p,\Delta\_{n})} |  | (28) |

Components:

* •

  Vt​(X,p,Δn)V\_{t}(X,p,\Delta\_{n}): Power variation at base frequency
* •

  Vt​(X,p,2​Δn)V\_{t}(X,p,2\Delta\_{n}): Power variation at doubled frequency

### Activity Index Estimation

|  |  |  |  |
| --- | --- | --- | --- |
|  | β^=solution to ​b​(p)=p\hat{\beta}=\text{solution to }b(p)=p |  | (29) |

Estimation Method:

* •

  Numerically solve b​(p)−p=0b(p)-p=0 using Brent’s method
* •

  Fallback: Select pp that minimizes |b​(p)−p||b(p)-p| if no root found

This approach estimates β\beta by analyzing how quickly power variations decay across sampling intervals. A high decay rate suggests high small-jump activity. The value of β\beta that makes b​(p)=pb(p)=p reflects the true activity level of the process. If β<2\beta<2, a Brownian component is ruled out; if β>1\beta>1, low-activity or finite variation models are excluded.

Table 2: Summary of Parameters and Variables

| Code Variable | Symbol | Meaning | Default/Range |
| --- | --- | --- | --- |
| X | XtX\_{t} | VIX time series | 1-minute frequency |
| L | LL | Truncation threshold | 0.5 (VIX units) |
| Delta | Δn\Delta\_{n} | Base sampling interval | 1 minute |
| p | pp | Power parameter | Scan 0.05–1.95 |
| dX1 | Δ​Xi\Delta X\_{i} | 1-min increments |  |
| dX2 | Δ​Xi(2)\Delta X\_{i}^{(2)} | 2-min increments |  |

As presented in Table 2, the data we use is the high-frequency VIX data XtX\_{t} on January 2nd, 2025, with frequency Δn=1\Delta\_{n}=1 min. Parameter LL is used as a truncation threshold to filter extreme jump observations. As shown in Table [3](https://arxiv.org/html/2510.19126v1#S3.T3 "Table 3 ‣ Activity Index Estimation ‣ 3 Data ‣ An Efficient Calibration Framework for Volatility Derivatives under Rough Volatility with Jumps"), after inputting different LL, we find that the estimate of β\beta becomes stable at 1.715 as LL increases.

Table 3: Truncation analysis (ℓ=0.5\ell=0.5) and activity index summary.

| Absolute 1-min increment statistics | |
| --- | --- |
| Median | 0.0200 |
| 95th percentile | 0.1400 |
| Maximum | 0.3200 |
| Truncated share (|Δ​X|>0.5|\Delta X|>0.5) | 0.00% |

| Activity Index Result | |
| --- | --- |
| Estimated β\beta | 1.715 |
| Method | Root-finding |

| Sensitivity to LL (for β≈1.7\beta\!\approx\!1.7–1.81.8 target) | |
| --- | --- |
| L=0.2L=0.2 | trunc = 1.7% |
| L=0.3L=0.3 | trunc = 0.3% |
| L=0.4L=0.4 | trunc = 0.0% |
| L=0.5L=0.5 | trunc = 0.0% |

LL denotes the truncation threshold (filters extreme jumps).
Δ\Delta denotes the base sampling interval.

Hence, when Todorov and Tauchen empirically estimate β∈(1.7,1.8)\beta\in(1.7,1.8) for the VIX index, they conclude that the volatility process is a pure-jump process of infinite variation. Combining this with our result β^=1.715\hat{\beta}=1.715, we conclude that the VIX index on January 2, 2025, satisfies the pure-jump model assumption.

In Equation ([4](https://arxiv.org/html/2510.19126v1#S2.E4 "In 2.1 Underlying Theoretic Model Formulation ‣ 2 Mathematical Models ‣ An Efficient Calibration Framework for Volatility Derivatives under Rough Volatility with Jumps")) of the previous section, the parameter cc controls the degree of jump activity in the Lévy subordinator. For parameter c in Equation ([21](https://arxiv.org/html/2510.19126v1#S2.E21 "In 2.2 Calibration Framework: Equation Transformations and mpmath Implementation ‣ 2 Mathematical Models ‣ An Efficient Calibration Framework for Volatility Derivatives under Rough Volatility with Jumps")), it represents fractional dynamics of volatility, which controls the memory and regularity of the volatility process.
The instantaneous variance is driven by a generalized fractional Ornstein–Uhlenbeck (OU) process, which has infinite activity but finite variation. Therefore, c should be between 0 and 1. Since c controls the process type in similar way of β\beta and the example raised in Wang and Xia(2022) that c=1/2 yields exactly inverse Gaussian‐driven OU process, which in Todorov and Tauchen (2011) should be classified as β\beta near 1. So in our research, for simplicity, we just set c=β^\hat{\beta}/2 in our following calibration.

## 4 Calibration Methodology

In this section, we explain how we accelerate the process of option calibration. First, we generate a large synthetic dataset of option prices using the analytical model with randomly sampled parameters. Next, we train a feedforward neural network to learn the mapping from model parameters to option prices. Finally, we apply this trained network in a two-stage calibration workflow: a global search via a Genetic Algorithm, followed by a local refinement using L-BFGS-B, enabling fast and accurate parameter estimation on real market data.

### 4.1 Offline Step

In the offline stage, we construct a high-quality training dataset by simulating option prices from an analytical pricing model implemented with high-precision numerical libraries (e.g., mpmath). The input model parameters are sampled from predefined, economically reasonable ranges using the Latin Hypercube Sampling (LHS) technique. The overall process is as follows:

1. 1.

   Parameter Sampling:
   Use Latin Hypercube Sampling to draw parameter vectors {θi}i=1N\{\theta\_{i}\}\_{i=1}^{N} from the joint distribution defined by the chosen bounds.
2. 2.

   Price Simulation:
   For each sampled θi\theta\_{i}, compute the corresponding option price PiP\_{i} via the analytical pricing function, ensuring high numerical accuracy with mpmath.
3. 3.

   Dataset Assembly:
   Aggregate the input–output pairs {(θi,Pi)}i=1N\{(\theta\_{i},P\_{i})\}\_{i=1}^{N} into the training set 𝒟train\mathcal{D}\_{\text{train}}.

![Refer to caption](image1.png)


Figure 2: Latin Hypercube Sampling

To construct the offline dataset for training our neural network, we simulate put option prices under the Proposition-2 analytical pricing framework. This involves evaluating the characteristic function using high-precision quadrature implemented with CuPy and mpmath.

We consider a seven-dimensional parameter space:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜽=(a,b,c,d,κ,r,t)\boldsymbol{\theta}=(a,b,c,d,\kappa,r,t) |  | (30) |

where (a,b,c,d,κ,r)(a,b,c,d,\kappa,r) are model parameters and tt denotes time-to-maturity ratio (i.e., Time to maturity / 365/\,365). Each parameter is sampled within mathematically meaningful ranges.

| Parameter | Value / Range |
| --- | --- |
| aa | [0, 5][0,\ 5] |
| bb | [0, 5][0,\ 5] |
| cc | 0.85750.8575 |
| dd | [0.5, 0.999][0.5,\ 0.999] |
| κ\kappa | [0, 10][0,\ 10] |
| rr | [−0.25, 0.25][-0.25,\ 0.25] |

Table 4: Parameter values and ranges used in the offline simulation.

Then we employ Latin Hypercube Sampling (LHS) with N=5,000N=5{,}000 samples to ensure efficient and stratified coverage across the high-dimensional space. Compared to simple random sampling, LHS offers better uniformity and variance reduction in function evaluations.

For each sampled parameter set, we compute option prices under four distinct maturities:

|  |  |  |  |
| --- | --- | --- | --- |
|  | T∈{258365,100365,48365,20365}T\in\left\{\frac{258}{365},\ \frac{100}{365},\ \frac{48}{365},\ \frac{20}{365}\right\} |  | (31) |

which represent realistic short- to medium-term contracts.

The pricing is evaluated across a discrete set of strike prices Kj∈𝒦K\_{j}\in\mathcal{K}, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒦={0.09, 0.10,…, 0.28}\mathcal{K}=\{0.09,\ 0.10,\ \ldots,\ 0.28\} |  | (32) |

totaling 34 strikes, selected to span both in-the-money and out-of-the-money regimes.

For each tuple, the put option price is computed. The entire pricing loop is parallelized using Python’s multiprocessing Pool.The resulting dataset consists of N=5,000N=5{,}000 parameter sets ×\times 4 maturities ×\times 34 strikes =𝟔𝟖𝟎,𝟎𝟎𝟎=\mathbf{680{,}000} rows, stored in efficient columnar format (Parquet) for downstream neural network training.

### 4.2 Numerical validation: CuPy vs. mpmath

Before generating the offline dataset, we verify that the CUDA/CuPy implementation
of the characteristic–function integrals matches a high–precision mpmath baseline.
On a grid of 600,000600{,}000 evaluations across (θ,T,K,nodes)(\theta,T,K,\text{nodes}), only
4242 points exceed a 10−510^{-5} absolute–error tolerance; the bulk errors concentrate
near machine precision (Fig. [3](https://arxiv.org/html/2510.19126v1#S4.F3 "Figure 3 ‣ 4.2 Numerical validation: CuPy vs. mpmath ‣ 4 Calibration Methodology ‣ An Efficient Calibration Framework for Volatility Derivatives under Rough Volatility with Jumps")).

Table 5: CuPy vs. mpmath (baseline) — summary metrics over 600,000600{,}000 evaluations.

| Metric | Value |
| --- | --- |
| Max |Δ​ϕ||\Delta\phi| | 6.577​e−036.577\mathrm{e}{-03} |
| Mean |Δ​ϕ||\Delta\phi| | 3.954​e−063.954\mathrm{e}{-06} |
| Max relative error | 5.942​e+015.942\mathrm{e}{+01} |
| Mean relative error | 3.153​e−013.153\mathrm{e}{-01} |
| Rows out of tol. (10−5)(10^{-5}) | 4242   (of 600,000600{,}000) |

![Refer to caption](comparision.png)


Figure 3: Histogram of log10⁡|Δ​ϕ|\log\_{10}|\Delta\phi| (CuPy −- mpmath). Most mass lies near −30-30, i.e., machine-precision agreement; the few outliers occur at extreme quadrature points.

### 4.3 Online Step

In the online stage, we train a feedforward neural network (FNN) to approximate the mapping from model parameters and option features to the corresponding put option price. Specifically, the neural network learns a function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(a,b,c,d,κ,r,t,K)→Option pricef(a,b,c,d,\kappa,r,t,K)\rightarrow\text{Option price} |  | (33) |

Neural Network Architecture:

* •

  Input Layer: 8 nodes, corresponding to the model parameters a,b,c,d,κ,ra,b,c,d,\kappa,r, time-to-maturity tt, and strike price KK.
* •

  Hidden Layers: 3 fully connected layers with ELU (Exponential Linear Unit) activation:

  + –

    Layer 1: 64 neurons
  + –

    Layer 2: 32 neurons
  + –

    Layer 3: 32 neurons
* •

  Output Layer: 1 neuron, representing the predicted put option price.

![Refer to caption](image.png)


Figure 4: Structure of Neural Network

This architecture was implemented in PyTorch. Before training, the input and output features are standardized using StandardScaler. The dataset is stratified and split into training (90%), validation (5%), and testing (5%) sets based on the (⋅)(\cdot) combination.

The model is trained to minimize the mean squared error (MSE) loss using the Adam optimizer. To enhance convergence and generalization, we apply:

* •

  Early Stopping: Training is terminated if the validation loss does not improve for 25 consecutive epochs.
* •

  Learning Rate Scheduler: We apply ReduceLROnPlateau, which reduces the learning rate by a factor of 0.5 when the validation loss plateaus, with a minimum learning rate threshold.

### 4.4 Online Training Results

Figure 6 shows the training and validation RMSE curves over epochs, where we observe convergence and stabilization. The best-performing epoch is marked in red.

![Refer to caption](image2.png)


Figure 5: Training and Validation RMSE Curves

The model’s predictions on a held-out test set (100 randomly selected samples) are shown in Figure [6](https://arxiv.org/html/2510.19126v1#S4.F6 "Figure 6 ‣ 4.4 Online Training Results ‣ 4 Calibration Methodology ‣ An Efficient Calibration Framework for Volatility Derivatives under Rough Volatility with Jumps"), demonstrating strong generalization capability, with predicted values closely matching the true option prices.

![Refer to caption](3.png)


Figure 6: Neural network predictions vs. true option prices on the test set

### 4.5 Option Calibration

To find the underlying model parameters from observed market option prices, we adopt a two-stage calibration procedure combining global and local optimization techniques.

Given that the pricing model includes a term structure of interest rates, we allow for four different rir\_{i} (1≤i≤41\leq i\leq 4) to correspond with the four maturities T∈{258,100,48,20}T\in\{258,100,48,20\}.

For each sample in the panel dataset on Jan 2nd, the appropriate rir\_{i} is assigned based on the nearest maturity, and the corresponding model parameters (a,b,c,d,κ,ri)(a,b,c,d,\kappa,r\_{i}) are mapped accordingly. This forms the full input set for calibration.

|  |  |  |  |
| --- | --- | --- | --- |
|  | (a,b,c,d,κ,{r​(Tn)}n=14)=arg⁡mina>0,b>0,c=0.8575,d∈(0.5,1),κ>0,r​(Tn)∈[−0.25,0.25]n∈{1,2,3,4},α=1.78,ζ=0.01​∑n((Market Prices)−(C,P)0(1,1,(a)))2\left(a,b,c,d,\kappa,\{r(T\_{n})\}\_{n=1}^{4}\right)=\underset{\begin{subarray}{c}a>0,\,b>0,\,c=0.8575,\,d\in(0.5,1),\,\kappa>0,\,r(T\_{n})\in[-0.25,0.25]\\ n\in\{1,2,3,4\},\,\alpha=1.78,\,\zeta=0.01\end{subarray}}{\arg\min}\sum\_{n}\left(\text{(Market Prices)}-(C,P)^{(1,1,(a))}\_{0}\right)^{2} |  | (34) |

#### 4.5.1 Global Optimization

We first apply the Genetic Algorithm (GA) to perform a global search over the parameter space. The objective is to minimize the mean squared error (MSE) between market-observed option prices and model-implied prices generated by a pretrained neural network surrogate.

The GA is implemented using the PyGAD library, with a population size of 600 and a maximum of 3000 generations. The fitness function is defined as the negative MSE between the neural network’s predicted option prices and the observed market prices, ensuring compatibility with PyGAD’s maximization framework.

#### 4.5.2 Local Refinement

The best solution identified by the genetic algorithm is used as the starting point for local refinement via the L-BFGS-B algorithm. This second-stage optimization employs the same loss function to fine-tune the parameter vector with high precision, ensuring convergence to a local minimum. The optimizer is constrained to the same parameter bounds to ensure economic plausibility.

By combining them in a two-stage calibration strategy, we exploit GA’s global exploration ability to provide a robust initial guess, followed by L-BFGS-B’s fast local convergence to refine the solution. This hybrid approach is particularly effective in high-dimensional calibration settings, where the loss surface may exhibit multiple local minima, and the gradients may be unreliable or hard to compute analytically due to surrogate models (e.g., neural networks). It ensures both robustness and precision, leading to more stable and interpretable parameter fitting.

Calibration results are shown below:

![Refer to caption](image4.png)


Figure 7: Calibration curve



| Parameter | Value |  | Parameter | Value |
| --- | --- | --- | --- | --- |
| a | 0.049762 |  | r1 (20 d) | 0.00198 |
| b | 0.849782 |  | r2 (48 d) | -0.001292 |
| c | 0.8575 |  | r3 (100 d) | -0.006008 |
| d | 0.769302 |  | r4 (258 d) | -0.012427 |
| κ\kappa | 7.798968 |  | — | — |

Table 6: Calibrated Parameters and Term Structure of Interest Rates

### 4.6 Times Series Analysis

In this section, we conduct a time series analysis using a near-the-money VIX put option with a given strike and expiration on February 19, 2025. For each of the next 31 trading days, we record the option market mid-quote and value the contract using the GPU-parallel pricer introduced earlier.

The pricing engine relies on a fixed parameter vector that was calibrated using market data from January 2, 2025.

![Refer to caption](image5.png)


Figure 8: VIX Put Option Pricing Over Time: Market vs. Model

The figure above compares the model estimates (orange) with the observed market prices (blue). The model exhibits a persistent upward bias, although it captures the general trend of the market data.

Quantitatively, the prediction errors are summarized below:

| Metric | Value |
| --- | --- |
| Mean Absolute Error (MAE) | 0.0329 |
| Root Mean Squared Error (RMSE) | 0.0330 |
| Mean Absolute Percentage Error (MAPE) | 86.96% |

Table 7: Error metrics for model-predicted VIX put option prices

Although the absolute mispricing is only about 0.03, the market prices lie in the $0.03–$0.04 range, causing the relative error to swell to nearly 87%. This distortion is mainly due to the calibration snapshot: on that day, many quoted strikes violated basic arbitrage bounds and exhibited extremely low trading volume, making the calibrated surface strongly fragile.

## 5 Conclusion and Future Directions

##### Conclusion

This study introduces a GPU-powered, neural-network–assisted calibration pipeline for power-type derivatives under rough-volatility dynamics with jumps.

Our main contributions are:

1. 1.

   GPU-accelerated pricing with CuPy.
   High-precision quadrature executed on the GPU reduces a single price evaluation from seconds to milliseconds, enabling the generation of large synthetic datasets.
2. 2.

   NN-based two-stage calibration.
   A feed-forward surrogate trained on N=5,000N=5{,}000 Latin-Hypercube samples accurately replicates the analytical pricer, achieving a validation RMSE of 3.1×10−43.1\times 10^{-4}.
   This neural network enables a much faster calibration process: combined with a Genetic Algorithm for global search and L-BFGS-B for local refinement, it recovers model parameters from real VIX-put quotes in under 20 minutes.

   By contrast, the original calibration pipeline based on direct evaluation via mpmath quadrature required over 24 hours, even with significantly reduced population sizes and iteration counts.
   The speed-up from using the neural network surrogate allows for larger population sizes and more generations in the GA stage, facilitating better convergence and more accurate parameter recovery.
3. 3.

   Empirical validation.
   Parameters calibrated on 2 Jan 2025 reproduce a 31-day price path with MAE=0.0329\text{MAE}=0.0329 and RMSE=0.0330\text{RMSE}=0.0330.
   Although the model slightly over-prices low-premium contracts—pushing MAPE≈87%\text{MAPE}\approx 87\%—it captures the overall trend and demonstrates strong out-of-sample robustness.

##### Limitation and Future Directions

1. 1.

   At present, the calibration pools all maturities. A worthwhile extension is to group the data by time-to-maturity and calibrate each maturity slice independently.
2. 2.

   We fail to filter the data using rough arbitrage checking method of put-call parity. Referring to Madan et al. (2019), we applied:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | bidEC​(K,T)−askEP​(K,T)≤S0−K≤askEC​(K,T)−bidEP​(K,T)\text{bidEC}(K,T)-\text{askEP}(K,T)\leq S\_{0}-K\leq\text{askEC}(K,T)-\text{bidEP}(K,T) |  | (35) |

   * •

     bidEC(K,T)(K,T) is the bid price of a European call option with strike KK and maturity TT.
   * •

     askEC(K,T)(K,T) is the ask price of the European call option with the same strike and maturity.
   * •

     bidEP(K,T)(K,T) is the bid price of the corresponding European put option.
   * •

     askEP(K,T)(K,T) is the ask price of the European put option.

   This inequality reflects the no-arbitrage bounds for the call–put parity relationship in the presence
   of bid–ask spreads. If violated, it may signal a potential arbitrage opportunity. However, all of the
   observation pairs are not in this range. The results can be seen in
   Appendix [A.1.1](https://arxiv.org/html/2510.19126v1#A1.SS1.SSS1 "A.1.1 Parity filter outcomes ‣ A.1 Arbitrage filters and data quality ‣ Appendix A Supplementary Analyses and Details ‣ An Efficient Calibration Framework for Volatility Derivatives under Rough Volatility with Jumps"). The possible causes of such a situation can be:
   Insufficient Liquidity, Stale Quotes, or Spot Price Mismatch.

## Appendix A Supplementary Analyses and Details

### A.1 Arbitrage filters and data quality

##### Call–put parity test (summary).

As discussed in Section 5 (Conclusion & Future Directions; limitation #2), our call–put parity screen flagged *systematic* inconsistencies between quoted calls, puts, and the contemporaneous spot/discount inputs. The detailed outcomes and diagnostics are consolidated here for archival completeness.

> Finding. No observation in the raw panel passes the parity check; all rows exhibit nonzero parity gaps of economically meaningful size.

Likely drivers include: (i) *insufficient liquidity* (wide, non‐synchronous quotes), (ii) *stale prints* in the vendor feed, and (iii) *spot/forward misalignment* (timing mismatch between options and spot/carry inputs). For reproducibility, we keep this section as a reference point for downstream filtering.

#### A.1.1 Parity filter outcomes

For each maturity–strike tuple we compute the standard forward‐adjusted parity residual and retain rows with residuals inside a one‐tick band. In our dataset, *no* row meets this criterion. Consequently, we proceed with structural no‐arbitrage screens that are more robust to microstructure noise.

##### Monotonicity and convexity screens (Section 3.3).

We enforce (i) decreasing price in strike and (ii) convexity in strike for each maturity slice. These shape constraints eliminate obvious data glitches while tolerating small bid/ask frictions. After applying these two filters, 35 observations remain; all subsequent calibrations in the paper use precisely this filtered subset.

### A.2 Jump‐activity index β\beta and the VIX modeling rationale

##### Method (Section 3.4).

Following Todorov and Tauchen ([2011](https://arxiv.org/html/2510.19126v1#bib.bib1)), we estimate the activity index β\beta from 1-minute VIX increments using power variations and truncation. This identifies whether the driving semimartingale possesses a continuous Brownian component and whether its jumps are of finite or infinite variation.

##### Empirical findings.

Our estimate from the VIX panel is

|  |  |  |
| --- | --- | --- |
|  | β^=1.715.\hat{\beta}=1.715. |  |

This implies:

1. 1.

   Absence of a Brownian component. Since β^<2\hat{\beta}<2, we reject a continuous diffusion term in VIX dynamics.
2. 2.

   Infinite‐variation jumps. Because β^>1\hat{\beta}>1, the jump component exhibits *infinite variation*, driven by a high intensity of small jumps.

The pure‐jump infinite‐variation interpretation matches the guidance in Todorov and Tauchen ([2011](https://arxiv.org/html/2510.19126v1#bib.bib1)), which anticipates β\beta close to but strictly below 2 (empirically ≈1.7\approx 1.7–1.81.8).

##### Link to the model’s stability index.

In the main text (see Equation ([21](https://arxiv.org/html/2510.19126v1#S2.E21 "In 2.2 Calibration Framework: Equation Transformations and mpmath Implementation ‣ 2 Mathematical Models ‣ An Efficient Calibration Framework for Volatility Derivatives under Rough Volatility with Jumps"))), the stability index α\alpha of the pure‐jump Lévy driver is the same conceptual object as the activity index β\beta. Prior work (e.g., Wang and Xia ([2022](https://arxiv.org/html/2510.19126v1#bib.bib3))) fixes α=1.78\alpha=1.78; our data‐driven estimate β^=1.715\hat{\beta}=1.715 is consistent with that regime and supports modeling VIX as a *pure‐jump, infinite‐activity, infinite‐variation* process.

### A.3 Economic interpretation of calibrated parameters

| Symbol | Model detail | Economic interpretation |
| --- | --- | --- |
| a>0a>0 | νX​(d​z)=a​e−b​z​z−1−c​𝟏{z>0}​d​z,log⁡φX1​(u)=ac​Γ​(−c)​[(b−i​u)c−bc]\nu\_{X}(dz)=a\,e^{-bz}z^{-1-c}\mathbf{1}\_{\{z>0\}}dz,\;\;\log\varphi\_{X\_{1}}(u)=\frac{a}{c}\Gamma(-c)\!\left[(b-iu)^{c}-b^{c}\right] | Baseline intensity of the tempered‐stable subordinator XX; scales the overall frequency of variance jumps across sizes. |
| b>0b>0 | Tempering parameter in e−b​ze^{-bz} and (b−i​u)c(b-iu)^{c}. | Controls the exponential tail decay of jump sizes in XX; larger bb suppresses very large volatility shocks (lower tail risk). |
| c∈(0,1)c\in(0,1) | Power‐law weight z−1−cz^{-1-c} in νX\nu\_{X} and exponent in (b−i​u)c(b-iu)^{c}. | Jump‐activity index of the Lévy subordinator; governs the intensity of small jumps (higher c⇒c\Rightarrow thicker small‐jump cloud). |
| d∈(0.5,1)d\in(0.5,1) | Kernel g​(t−s)=(t−s)d−1/Γ​(d)g(t-s)=(t-s)^{d-1}/\Gamma(d). | Roughness of volatility paths with Hurst H=d−12<0.5H=d-\tfrac{1}{2}<0.5. |
| κ>0\kappa>0 | Exponential temper e−κ​te^{-\kappa t} in the kernel h​(t,s)h(t,s). | Speed of mean‐reversion in volatility. |
| {r​(Tn)}\{r(T\_{n})\} | Remainder in J​(t,t0,Δ)=It02​(Δ)−ξ1t​∫t0tHΔ​(t,s)​ds+r​(t0,t).J(t,t\_{0},\Delta)=I\_{t\_{0}}^{2}(\Delta)-\xi\_{1}^{t}\int\_{t\_{0}}^{t}H\_{\Delta}(t,s)\,\mathrm{d}s+r(t\_{0},t). | Maturity‐specific level shifts tied to spot variance at t0t\_{0}; captures residual term‐structure offsets. |

Table 8: Economic interpretations of key calibrated parameters.

### A.4 Neural–network pricer: error diagnostics and remedies

Table 9: Error diagnostics under unified–dollar target standardisation.

| Metric | Value | Comment |
| --- | --- | --- |
| Target s.d. σy\sigma\_{y} | 7.69×10−27.69\times 10^{-2} | Standard deviation after scaling |
| Train abs–RMSE | 1.06×10−31.06\times 10^{-3} | Error on training set |
| Test abs–RMSE | 1.10×10−31.10\times 10^{-3} | Error on hold‐out test set |
| Val rel–RMSE (%) | 6.36×1036.36\times 10^{3} | Pathologically inflated |
| Val MAPE (%) | 3.80×1023.80\times 10^{2} | Large percentage bias |

##### Relative–error pathology.

Absolute errors are uniformly small (∼10−3\sim 10^{-3}), but percentage metrics explode because many OTM options have pennies‐level premiums. A $0.01 miss on a $0.02 option is a 50%50\% relative error; aggregating many such cases dominates rel–RMSE/MAPE.

##### Remedies.

We recommend two practical fixes:

1. 1.

   Inverse–premium reweighting.
   Replace plain MSE by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ℒw=1N​∑i=1Nwi​(y^i−yi)2,wi=(yi+ε)−α,α∈[0,1],\mathcal{L}\_{\mathrm{w}}=\frac{1}{N}\sum\_{i=1}^{N}w\_{i}\,(\hat{y}\_{i}-y\_{i})^{2},\qquad w\_{i}=(y\_{i}+\varepsilon)^{-\alpha},\quad\alpha\in[0,1], |  | (36) |

   with ε\varepsilon set to one tick. This upweights low‐premium OTM contracts without letting the loss blow up. A robust starting choice is α=0.5\alpha=0.5; tune on a *log* grid.
2. 2.

   Log–price target.
   Transform premiums via

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | zi=log⁡(yi+ε),ℒlog=1N​∑i=1N(z^i−zi)2,z\_{i}=\log\!\bigl(y\_{i}+\varepsilon\bigr),\qquad\mathcal{L}\_{\log}=\frac{1}{N}\sum\_{i=1}^{N}\bigl(\hat{z}\_{i}-z\_{i}\bigr)^{2}, |  | (37) |

   which compresses the dynamic range and stabilises training across ITM/OTM regimes.

### A.5 Extension: two–factor rough–jump model (Proposition 8)

##### Concept.

Motivated by evidence that volatility‐of‐volatility can itself be rough Da Fonseca and Zhang ([2019](https://arxiv.org/html/2510.19126v1#bib.bib12)), augment the baseline (rough–jump) factor with an independent Lévy‐driven mean‐reverting process YtY\_{t} (kernel η\eta) that modulates the average forward variance. Structurally this mirrors two–factor Heston: one factor for volatility, another for its variability. Pricing remains tractable through characteristic functions, at the cost of deeper numerics.

##### Computation.

Evaluating the Proposition 8 characteristic function is currently the bottleneck:
(i) nested quadratures, (ii) repeated evaluations of log⁡ϕY1​(⋅)\log\phi\_{Y\_{1}}(\cdot) inside the integrand, and (iii) accumulation of discretisation error. Even with CuPy/GPU parallelism, wall‐clock is prohibitive for full calibration. A complete empirical study is therefore deferred.

### A.6 Code repository

The full implementation for offline data generation, neural network training, and two–stage option calibration is publicly available:

<https://github.com/TenghanZhong/GPU-NN-Option-Calibration>

## References

* Todorov and Tauchen (2011)

  Todorov, V. and Tauchen, G.
  Volatility jumps.
  *Journal of Business & Economic Statistics*, 29(3): 356–371, 2011.
* Gatheral et al. (2018)

  Gatheral, J., Jaisson, T., and Rosenbaum, M.
  Volatility is rough.
  *Quantitative Finance*, 18(6): 933–949, 2018.
* Wang and Xia (2022)

  Wang, L. and Xia, W.
  Power-type derivatives for rough volatility with jumps.
  *Journal of Futures Markets*, 42(10): 1369–1406, 2022.
* Ruijter and Oosterlee (2015)

  Ruijter, M. J. and Oosterlee, C. W.
  The Fourier-cosine method for option pricing revisited.
  *SIAM Journal on Financial Mathematics*, 6(1): 189–210, 2015.
* Bennedsen et al. (2017)

  Bennedsen, M., Friz, P., and Rosenbaum, M.
  Hybrid schemes for Brownian semistationary processes.
  *Finance and Stochastics*, 21(4): 931–965, 2017.
* Horvath et al. (2021)

  Horvath, B., Muguruza, A., and Tomas, M.
  Deep learning volatility: a deep neural network perspective on pricing and calibration in (rough) volatility models.
  *Quantitative Finance*, 21(1): 11–27, 2021.
* Blumenthal and Getoor (1961)

  Blumenthal, R. and Getoor, R.
  Sample functions of stochastic processes with independent increments.
  *Journal of Mathematics and Mechanics*, 10: 493–516, 1961.
* Madan et al. (2019)

  Madan, D. B., Reyners, S., and Schoutens, W.
  Advanced model calibration on bitcoin options.
  *Digital Finance*, 1: 117–137, 2019.
  doi:10.1007/s42521-019-00002-1.
* McKay et al. (1979)

  McKay, M. D., Beckman, R. J., and Conover, W. J.
  A comparison of three methods for selecting values of input variables in the analysis of output from a computer code.
  *Technometrics*, 21(2): 239–245, 1979.
* Goldberg (1989)

  Goldberg, D. E.
  *Genetic Algorithms in Search, Optimization, and Learning*.
  Addison-Wesley, 1989.
* Zhu et al. (1997)

  Zhu, C., Byrd, R. H., Lu, P., and Nocedal, J.
  Algorithm 778: L-BFGS-B: Fortran subroutines for large-scale bound-constrained optimization.
  *ACM Transactions on Mathematical Software*, 23(4): 550–560, 1997.
* Da Fonseca and Zhang (2019)

  Da Fonseca, J. and Zhang, W.
  Volatility of volatility is (also) rough.
  *Journal of Futures Markets*, 39(5): 600–611, 2019.