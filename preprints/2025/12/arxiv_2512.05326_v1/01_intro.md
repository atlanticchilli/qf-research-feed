---
authors:
- Xiang Gao
- Cody Hyndman
doc_id: arxiv:2512.05326v1
family_id: arxiv:2512.05326
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Convolution-FFT for option pricing in the Heston model
url_abs: http://arxiv.org/abs/2512.05326v1
url_html: https://arxiv.org/html/2512.05326v1
venue: arXiv q-fin
version: 1
year: 2025
---


Xiang Gao
111Department of Mathematics and Statistics,
Concordia University,
1455 Boulevard de Maisonneuve Ouest,
Montréal, Québec,
Canada H3G 1M8.
and
Cody Hyndman11footnotemark: 1 222Corresponding Author: cody.hyndman@concordia.ca

(November 3, 2025)

###### Abstract

We propose a convolution–FFT method for pricing European options under the Heston model that leverages a continuously differentiable representation of the joint characteristic function. Unlike existing Fourier-based methods that rely on branch-cut adjustments or empirically tuned damping parameters, our approach yields a stable integrand even under large frequency oscillations. Crucially, we derive fully analytical error bounds that quantify both truncation error and discretization error in terms of model parameters and grid settings. To the best of our knowledge, this is the first work to provide such explicit, closed-form error estimates for an FFT-based convolution method specialized to the Heston model. Numerical experiments confirm the theoretical rates and illustrate robust, high-accuracy option pricing at modest computational cost.

Keywords:
Option pricing; Numerical methods; Fast Fourier transform; Convolution; Heston model; Carr and Madan method.

Mathematics Subject Classification (2020): Primary: 65T50, 91G60; Secondary: 60H30, 60E10

## 1 Introduction

A variety of numerical integration methods are used to efficiently value complex contracts and calibrate financial models. For option pricing models with a closed-form characteristic function, such as the Heston model, it is natural to formulate valuation directly in the Fourier domain. The computational efficiency of the fast Fourier transform (FFT) makes such integration methods particularly attractive for calibration to large sets of plain vanilla options. A widely used approach is the FFT method of carr1999option, which applies a damping factor to the modified payoff in the log-strike domain.

heston1993closed proposed a two-factor asset-pricing model with stochastic volatility, derived the characteristic function in closed form, and provided a semi-closed-form solution for pricing vanilla options. In practice, however, the standard representation of the Heston characteristic function is problematic: discontinuities arising from complex logarithms and branch cuts may lead to unreliable numerical integration. Several theoretical and numerical schemes have been introduced to address this discontinuity problem, including the rotation-counting method of kahl2005not and the approaches of lord2010complex and levendorskiui2012efficient.

The seminal work of carr1999option introduced an FFT-based framework for option valuation by applying a damping factor to a modified payoff function, enabling efficient numerical integration in the Fourier domain. While widely used, this approach requires careful tuning of the damping exponent and suffers from boundary effects when the transform is applied to non-periodic payoffs. The COS method of lord2008fast improves accuracy by expanding the characteristic function in a Fourier-cosine series, but it also relies on finite-interval truncation and requires analytical expressions for characteristic functions. Both methods depend on continuity properties of the Heston characteristic function, which, as noted by lord2010complex, can exhibit branch discontinuities and complex-logarithm ambiguities.

In contrast, we derive a differentiable and numerically stable representation of the joint characteristic function for the Heston model that eliminates the discontinuity problem. This representation yields a smoother Fourier integrand and removes the branch-cut ambiguities associated with the standard Heston formulation. This facilitates a convolution-based FFT (CFFT) approach that operates directly in the log-stock domain rather than the log-strike domain. The resulting formulation avoids damping-parameter tuning, reduces boundary artifacts, and provides a natural probabilistic interpretation by convolving the payoff with the transition kernel of the log-price process. It also decouples damping and shifting from the characteristic function itself, which is advantageous for numerical stability.

We note that the term convolution method has also been used in lord2008fast, but in a different sense. Their CONV approach rewrites the discretized Carr and Madan valuation formula as a convolution in the strike variable under a Lévy-process framework. The convolution method developed here arises directly from the conditional density of the Heston log-price process and expresses the option value as the analytical convolution of the payoff with the transition kernel. This density-based formulation leads to a structurally different Fourier integrand and underpins the error analysis that follows.

We derive explicit analytical bounds for both truncation and discretization errors of our convolution–FFT schemes under the Heston model. These bounds specialize and sharpen the general transform-method error analyses of lee2004option and crocce2017error, and, to the best of our knowledge, have not previously been worked out explicitly in this Heston-specific FFT setting. In this paper we provide an explicit analytical treatment of the truncation and discretization errors that arise in this setting, and develop a convolution–FFT valuation method that incorporates these results in a numerically stable manner.

The outline of the paper is as follows. In Section [2](https://arxiv.org/html/2512.05326v1#S2 "2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model"), we briefly review the Heston model and provide a differentiable expression for the two-dimensional characteristic function. In Section [3](https://arxiv.org/html/2512.05326v1#S3 "3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model"), we introduce the CFFT method for option valuation and provide an error analysis. We also present an efficient modification involving damping and shifting schemes for the option function, which, as our analysis shows, can substantially reduce boundary error. In Section [4](https://arxiv.org/html/2512.05326v1#S4 "4 Numerical results ‣ Convolution-FFT for option pricing in the Heston model"), we present numerical results. To illustrate the advantages of our method, we compare it both to the semi-closed-form solution of heston1993closed and to the FFT method of carr1999option. Section [5](https://arxiv.org/html/2512.05326v1#S5 "5 Conclusion ‣ Convolution-FFT for option pricing in the Heston model") concludes and an appendix contains proofs.

## 2 Heston model with characteristic function

The Black-Scholes-Merton model assumes that volatility is constant over time. The volatility smile refers to the pattern obtained when plotting implied volatility against strike price under the Black–Scholes model. The volatility smile demonstrates that implied volatility actually varies with strike price. Restricted by these assumptions, the Black–Scholes model is unrealistic in capturing key features of asset returns, including the volatility smile and skewness in the return distribution. Many empirical studies indicate that volatility is driven by a mean-reverting stochastic process rather than remaining constant; see fouque2000derivatives. Therefore, various stochastic volatility models have been proposed to capture such properties. A popular example is the model of heston1993closed, who derived a semi-closed-form solution for pricing vanilla options. Throughout this section we use the notation (Xt,Vt)(X\_{t},V\_{t}) for the log-price and variance processes. The Heston model parameters are denoted by κ>0\kappa>0 (mean reversion rate), θ>0\theta>0 (long-run variance), σ>0\sigma>0 (volatility of variance), and ρ∈(−1,1)\rho\in(-1,1) (instantaneous correlation). The term ηt\eta\_{t} will be used for the drift of the log-price process when convenient.

### 2.1 Heston’s stochastic volatility model

We assume the stock price StS\_{t} obeys a diffusion process on a filtered probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}). The filtration {ℱt}t≥0\{\mathcal{F}\_{t}\}\_{t\geq 0} is generated by two independent Wiener processes satisfying the usual conditions of completeness and right continuity.
Under the Heston model [heston1993closed], the log-price XtX\_{t} and variance VtV\_{t} satisfy

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Xt\displaystyle\mathrm{d}X\_{t} | =(r−12​Vt)​d​t+Vt​d​Wt(1),\displaystyle=\left(r-\tfrac{1}{2}V\_{t}\right)\mathrm{d}t+\sqrt{V\_{t}}\,\mathrm{d}W^{(1)}\_{t}, |  | (2.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Vt\displaystyle\mathrm{d}V\_{t} | =κ​(θ−Vt)​d​t+σ​Vt​d​Wt(2),\displaystyle=\kappa(\theta-V\_{t})\mathrm{d}t+\sigma\sqrt{V\_{t}}\,\mathrm{d}W^{(2)}\_{t}, |  | (2.2) |

with d​⟨W(1),W(2)⟩t=ρ​d​t\mathrm{d}\langle W^{(1)},W^{(2)}\rangle\_{t}=\rho\,\mathrm{d}t.

feller1951two classifies the boundaries for a one-dimensional parabolic diffusion equation and shows that the stochastic volatility process VtV\_{t} in equation ([2.2](https://arxiv.org/html/2512.05326v1#S2.E2 "In 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")) has the following properties:

* (i)

  if 2​κ​θ≥σ22\kappa\theta\geq\sigma^{2}, then zero is unattainable and Vt>0V\_{t}>0,
* (ii)

  if 2​κ​θ<σ22\kappa\theta<\sigma^{2}, then zero is a regular, attainable and reflecting boundary, which means that VtV\_{t} can touch 0, but does not spend time there.

We assume the market price of risk scheme Λ~=(Λ1,Λ2)\tilde{\Lambda}=\left(\Lambda\_{1},\Lambda\_{2}\right) associated with (W1,W2)\left(W\_{1},W\_{2}\right) satisfies the following condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ−rvt=ρ​Λ1+1−ρ2​Λ2.\frac{\mu-r}{\sqrt{v\_{t}}}=\rho\Lambda\_{1}+\sqrt{1-\rho^{2}}\Lambda\_{2}. |  | (2.3) |

and we define an equivalent measure ℚΛ\mathbb{Q}^{\Lambda} on ℱt\mathcal{F}\_{t} by

|  |  |  |
| --- | --- | --- |
|  | d​ℚΛd​ℙ|ℱt=exp⁡(−12​∫0t(Λ12+Λ22)​𝑑s+∫0tΛ1​𝑑W1​(s)+∫0tΛ2​𝑑W2​(s)).\frac{d\mathbb{Q}^{\Lambda}}{d\mathbb{P}}\Bigg|\_{\mathcal{F}\_{t}}=\exp\left(-\frac{1}{2}\int\_{0}^{t}{\left(\Lambda\_{1}^{2}+\Lambda\_{2}^{2}\right)}ds+\int\_{0}^{t}\Lambda\_{1}dW\_{1}(s)+\int\_{0}^{t}{\Lambda\_{2}}dW\_{2}(s)\right). |  |

We have that ℚΛ\mathbb{Q}^{\Lambda} is equivalent to ℙ\mathbb{P} provided that 𝔼​[d​ℚΛd​ℙ|ℱt]=1\mathbb{E}\left[\frac{d\mathbb{Q}^{\Lambda}}{d\mathbb{P}}|\_{\mathcal{F}\_{t}}\right]=1 for all t∈[0,T]t\in[0,T]. Though the market price of risk Λ~\tilde{\Lambda} can be chosen arbitrarily, to obtain a complete Heston model we follow Heston’s suggestion and let Λ1​(vt)=Λ​vt\Lambda\_{1}(v\_{t})=\Lambda\sqrt{v\_{t}} for some positive constant Λ\Lambda such that Λ2\Lambda\_{2} is uniquely determined by equation ([2.3](https://arxiv.org/html/2512.05326v1#S2.E3 "In 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")). Further, by Girsanov’s theorem, we define two independent Wiener processes under ℚΛ\mathbb{Q}^{\Lambda}

|  |  |  |
| --- | --- | --- |
|  | {d​W1Λ​(t)=d​W1​(t)+Λ​vt​d​t,d​W2Λ​(t)=d​W2​(t)+μ−r−Λ​ρ​vt(1−ρ2)​vt​d​t,\left\{\begin{aligned} dW^{\Lambda}\_{1}(t)&=dW\_{1}(t)+\Lambda\sqrt{v\_{t}}dt,\\ dW^{\Lambda}\_{2}(t)&=dW\_{2}(t)+\frac{\mu-r-\Lambda\rho v\_{t}}{\sqrt{(1-\rho^{2})v\_{t}}}dt,\end{aligned}\right. |  |

which gives the risk-neutral dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​St=r​St​d​t+vt​St​(ρ​d​W1​tΛ+1−ρ2​d​W2​tΛ),d​vt=κ¯​(θ¯−vt)​d​t+σ​vt​d​W1​tΛ,\left\{\begin{aligned} &dS\_{t}=rS\_{t}dt+\sqrt{v\_{t}}S\_{t}\left(\rho d{W}^{\Lambda}\_{1t}+\sqrt{1-\rho^{2}}d{W}^{\Lambda}\_{2t}\right),\\ &dv\_{t}=\bar{\kappa}\left(\bar{\theta}-v\_{t}\right)dt+\sigma\sqrt{v\_{t}}d{W}^{\Lambda}\_{1t},\end{aligned}\right. |  | (2.4) |

where κ¯=(κ+σ​Λ)\bar{\kappa}=\left(\kappa+\sigma\Lambda\right), θ¯=κ​θ/κ¯\bar{\theta}=\kappa\theta/\bar{\kappa}, provided that κ¯≠0\bar{\kappa}\neq 0.

Define the log-stock process, with initial value x0=0x\_{0}=0

|  |  |  |
| --- | --- | --- |
|  | xt=log⁡(StS0).x\_{t}=\log\left(\frac{S\_{t}}{S\_{0}}\right). |  |

Introducing parameter ρ~=(ρ,1−ρ2)\tilde{\rho}=\left(\rho,\sqrt{1-\rho^{2}}\right) and the joint process d​WtΛ=(d​W1Λ​(t),d​W2Λ​(t))⊤dW\_{t}^{\Lambda}=\left(dW^{\Lambda}\_{1}(t),dW^{\Lambda}\_{2}(t)\right)^{\top}, we find the dynamics of xtx\_{t} is given by

|  |  |  |
| --- | --- | --- |
|  | d​xt=(r−12​vt)​d​t+vt​ρ~​d​WtΛ.dx\_{t}=\left(r-\frac{1}{2}v\_{t}\right)dt+\sqrt{v\_{t}}\tilde{\rho}dW^{\Lambda}\_{t}. |  |

The joint process Xt=(xt,vt)⊤{X}\_{t}=\left(x\_{t},v\_{t}\right)^{\top} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=η​(vt,t)​d​t+vt​ξ​d​WtΛ,d{X}\_{t}=\eta(v\_{t},t)dt+\sqrt{v\_{t}}\xi dW^{\Lambda}\_{t}, |  | (2.5) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | η​(vt,t)\displaystyle\eta(v\_{t},t) | =(r−12​vtκ¯​(θ¯−vt)), and ​ξ=(ρ1−ρ2σ0).\displaystyle=\left(\begin{smallmatrix}r-\frac{1}{2}v\_{t}\\ \bar{\kappa}\left(\bar{\theta}-v\_{t}\right)\end{smallmatrix}\right),\text{ and }\xi=\left(\begin{smallmatrix}\rho&\sqrt{1-\rho^{2}}\\ \sigma&0\end{smallmatrix}\right). |  |

A central component of Fourier-based pricing methods is the joint characteristic function of (XT,VT)(X\_{T},V\_{T}) conditional on (Xt,Vt)(X\_{t},V\_{t}). The classical expression derived by Heston [heston1993closed] is widely used in semi-analytical pricing formulas, but direct numerical implementation may suffer from discontinuities due to complex logarithms and branch cuts [kahl2005not, lord2010complex]. For convolution-based methods these discontinuities can lead to instability. In this subsection we present an equivalent formulation of the characteristic function that is continuous in its arguments and differentiable with respect to the model parameters, making it more suitable for numerical integration.

###### Definition 2.1.

The characteristic function of the joint variable Xt=(xt,vt)⊤X\_{t}=(x\_{t},v\_{t})^{\top} under measure ℙ\mathbb{P} with initial state X=(x,v)⊤X=(x,v)^{\top} and frequency components U=(p,q)⊤U=(p,q)^{\top}, is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ​(U,X,t)=𝔼ℙ​[ei​U⊤​XT|Xt=(x,v)⊤],\varphi(U,X,t)=\mathbb{E}^{\mathbb{P}}\left[e^{\mathrm{i}\mkern 1.0muU^{\top}X\_{T}}|X\_{t}=(x,v)^{\top}\right], |  | (2.6) |

with terminal condition φ​(U,X,T)=ei​U⊤​X\varphi(U,X,T)=e^{\mathrm{i}\mkern 1.0muU^{\top}X}.

Under a different measure, the form of the characteristic function ([2.6](https://arxiv.org/html/2512.05326v1#S2.E6 "In Definition 2.1. ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")) would be different. Similar to the Black-Scholes model, we obtain the following expression of the Heston call with two probability measures

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ct=\displaystyle C\_{t}= | e−r​τ​𝔼ℚ​[(ST−K)+|St,vt]\displaystyle e^{-r\tau}\mathbb{E}^{\mathbb{Q}}\left[(S\_{T}-K)^{+}\left|S\_{t},v\_{t}\right.\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | e−r​τ​(𝔼ℚ​[ST​𝟏ST>K|St,vt]−K​𝔼ℚ​[𝟏ST>K|St,vt])\displaystyle e^{-r\tau}\left(\mathbb{E}^{\mathbb{Q}}\left[S\_{T}\mathbf{1}\_{S\_{T}>K}\left|S\_{t},v\_{t}\right.\right]-K\mathbb{E}^{\mathbb{Q}}\left[\mathbf{1}\_{S\_{T}>K}\left|S\_{t},v\_{t}\right.\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | St​𝔼ℚ​[STF​(t,T)​𝟏ST>K|St,vt]−K​e−r​τ​𝔼ℚ​[𝟏ST>K|St,vt]\displaystyle S\_{t}\mathbb{E}^{\mathbb{Q}}\left[\frac{S\_{T}}{F(t,T)}\mathbf{1}\_{S\_{T}>K}\left|S\_{t},v\_{t}\right.\right]-Ke^{-r\tau}\mathbb{E}^{\mathbb{Q}}\left[\mathbf{1}\_{S\_{T}>K}\left|S\_{t},v\_{t}\right.\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | St​𝔼𝕊​[𝟏ST>K|St,vt]−K​e−r​τ​𝔼ℚ​[𝟏ST>K|St,vt],\displaystyle S\_{t}\mathbb{E}^{\mathbb{S}}\left[\mathbf{1}\_{S\_{T}>K}\left|S\_{t},v\_{t}\right.\right]-Ke^{-r\tau}\mathbb{E}^{\mathbb{Q}}\left[\mathbf{1}\_{S\_{T}>K}\left|S\_{t},v\_{t}\right.\right], |  |

where F​(t,T)=er​(T−t)​StF(t,T)=e^{r\left(T-t\right)}S\_{t} is the forward price, as seen from t, and τ=T−t\tau=T-t. We define the measure change from the risk neutral measure ℚ\mathbb{Q} to the equivalent martingale measure 𝕊\mathbb{S} which can be seen as an invariant measurement

|  |  |  |
| --- | --- | --- |
|  | d​𝕊d​ℚ=STF​(t,T).\frac{d\mathbb{S}}{d\mathbb{Q}}=\frac{S\_{T}}{F(t,T)}. |  |

For simplicity, we denote ℙ1=𝕊\mathbb{P}\_{1}=\mathbb{S} and ℙ2=ℚ\mathbb{P}\_{2}=\mathbb{Q}, under which

|  |  |  |  |
| --- | --- | --- | --- |
|  | P1​(ST,K)=\displaystyle P\_{1}(S\_{T},K)= | ℙ1​(ST≥K),\displaystyle\mathbb{P}\_{1}(S\_{T}\geq K), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | P2​(ST,K)=\displaystyle P\_{2}(S\_{T},K)= | ℙ2​(ST≥K),\displaystyle\mathbb{P}\_{2}(S\_{T}\geq K), |  |

and the pricing formula becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ct=St​P1​(ST,K)−K​e−r​τ​P2​(ST,K).C\_{t}=S\_{t}P\_{1}\left(S\_{T},K\right)-Ke^{-r\tau}P\_{2}\left(S\_{T},K\right). |  | (2.7) |

According to arbitrage pricing theory, the Heston call option C​(S,v,t)C\left(S,v,t\right) satisfies the following PDE (see heston1993closed and black1973pricing):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​v​S2\displaystyle\frac{1}{2}vS^{2} | ∂2C∂S2+ρ​σ​v​S​∂2C∂S​∂v+12​σ2​v​∂2C∂v2+r​S​∂C∂S+[κ¯​(θ¯−v)−σ​Λ​v]​∂C∂v+∂C∂t−r​C=0.\displaystyle\frac{\partial^{2}C}{\partial S^{2}}+\rho\sigma vS\frac{\partial^{2}C}{\partial S\partial v}+\frac{1}{2}\sigma^{2}v\frac{\partial^{2}C}{\partial v^{2}}+rS\frac{\partial C}{\partial S}+\left[\bar{\kappa}\left(\bar{\theta}-v\right)-\sigma\Lambda v\right]\frac{\partial C}{\partial v}+\frac{\partial C}{\partial t}-rC=0. |  |

Due to the similar structure to the Black-Scholes model, P1P\_{1} and P2P\_{2} must satisfy the following PDE in terms of x=ln⁡SKx=\ln\frac{S}{K}

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​v​∂2Pi∂x2+ρ​σ​v​∂2Pi∂x​∂v+12​σ2​v​∂2Pi∂v2+(r+ci​v)​∂Pi∂x+(a−bi​v)​∂Pi∂v+∂Pi∂t=0,\frac{1}{2}v\frac{\partial^{2}P\_{i}}{\partial x^{2}}+\rho\sigma v\frac{\partial^{2}P\_{i}}{\partial x\partial v}+\frac{1}{2}\sigma^{2}v\frac{\partial^{2}P\_{i}}{\partial v^{2}}+\left(r+c\_{i}v\right)\frac{\partial P\_{i}}{\partial x}+\left(a-b\_{i}v\right)\frac{\partial P\_{i}}{\partial v}+\frac{\partial P\_{i}}{\partial t}=0, |  | (2.8) |

where
c1=12c\_{1}=\frac{1}{2},c2=−12c\_{2}=-\frac{1}{2}, a=κ¯​θ¯a=\bar{\kappa}\bar{\theta}, b1=κ¯+Λ​σ−ρ​σb\_{1}=\bar{\kappa}+\Lambda\sigma-\rho\sigma, b2=κ¯+Λ​σb\_{2}=\bar{\kappa}+\Lambda\sigma for i=1,2i=1,2.

By the Feynman-Kac representation theorem, the characteristic functions φi\varphi\_{i} defined by ([2.6](https://arxiv.org/html/2512.05326v1#S2.E6 "In Definition 2.1. ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")) under measures PiP\_{i} satisfying ([2.8](https://arxiv.org/html/2512.05326v1#S2.E8 "In 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")) are the unique bounded solutions to the PDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂φi∂t+(r+ci​v)​∂φi∂x+(a−bi​v)​∂φi∂v+12​v​∂2φi∂x2+σ22​v​∂2φi∂v2+ρ​σ​v​∂2φi∂x​∂v=0,\frac{\partial\varphi\_{i}}{\partial t}+\left(r+c\_{i}v\right)\frac{\partial\varphi\_{i}}{\partial x}+\left(a-b\_{i}v\right)\frac{\partial\varphi\_{i}}{\partial v}+\frac{1}{2}v\frac{\partial^{2}\varphi\_{i}}{\partial x^{2}}+\frac{\sigma^{2}}{2}v\frac{\partial^{2}\varphi\_{i}}{\partial v^{2}}+\rho\sigma v\frac{\partial^{2}\varphi\_{i}}{\partial x\partial v}=0, |  | (2.9) |

with boundary condition φ=ei​(p​x+q​v)\varphi=e^{\mathrm{i}\mkern 1.0mu\left(px+qv\right)}.

The discontinuity problem in Heston’s characteristic function has been studied and solved by other authors such as kahl2005not using phase rotation counting and cui2017full splitting the term that causes the phase shift, however, their solutions are not easy to implement in calibration. Therefore, we propose another simple representation of the joint characteristic function. The next result provides a differentiable representation of the joint characteristic function under the Heston model. This form avoids discontinuities found in the standard expression and will be used in our convolution–FFT method.

###### Theorem 2.1.

(Joint characteristic function)
The characteristic function of the joint process Xt=(xt,vt)⊤X\_{t}=(x\_{t},v\_{t})^{\top} under PiP\_{i}, with initial condition X=(x,v)⊤X=(x,v)^{\top} and Fourier variables U=(p,q)U=(p,q), is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | φi​(p,q)=exp⁡(i​p​(x+r​τ)+i​q​(v+a​τ)+γ+λσ2​(1−ζ)​v−γ−λσ2​a​τ+2​aσ2​ln⁡ζ),\varphi\_{i}\left(p,q\right)=\exp\left(\mathrm{i}\mkern 1.0mup\left(x+r\tau\right)+\mathrm{i}\mkern 1.0muq\left(v+a\tau\right)+\frac{\gamma+\lambda}{\sigma^{2}}\left(1-\zeta\right)v-\frac{\gamma-\lambda}{\sigma^{2}}a\tau+\frac{2a}{\sigma^{2}}\ln\zeta\right), |  | (2.10) |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γ=\displaystyle\gamma= | σ2​(p2−2​i​ci​p)+(bi−i​σ​ρ​p)2,\displaystyle\sqrt{\sigma^{2}\left(p^{2}-2\mathrm{i}\mkern 1.0muc\_{i}p\right)+\left(b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p\right)^{2}}, |  | (2.11) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λ=\displaystyle\lambda= | bi−i​σ​ρ​p−i​σ2​q,\displaystyle b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p-\mathrm{i}\mkern 1.0mu\sigma^{2}q, |  | (2.12) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ζ=\displaystyle\zeta= | 2​γγ+λ+(γ−λ)​e−γ​τ.\displaystyle\frac{2\gamma}{\gamma+\lambda+(\gamma-\lambda)e^{-\gamma\tau}}. |  | (2.13) |

The proof is given in Appendix [A.1](https://arxiv.org/html/2512.05326v1#A1.SS1 "A.1 Proof of Theorem 2.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model").

This representation is fully equivalent to the standard form of Heston’s characteristic function, but its continuous differentiability and removal of complex–logarithm ambiguities make it more stable for numerical computation. In particular, this form is advantageous for the convolution–FFT approach developed in Section [3](https://arxiv.org/html/2512.05326v1#S3 "3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model"), where smoothness with respect to the spatial variables plays a key role in controlling truncation and discretization errors. In the estimation, we use the following kernel function obtained from the joint characteristic function of the increment XT−XtX\_{T}-X\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψi​(p,q)=\displaystyle\psi\_{i}(p,q)= | 𝔼​[ei​U⊤​(XT−Xt)|Xt=X]=e−i​U⊤​X​φi​(p,q)\displaystyle\mathbb{E}\left[e^{\mathrm{i}\mkern 1.0muU^{\top}\left(X\_{T}-X\_{t}\right)}\big|X\_{t}=X\right]=e^{-\mathrm{i}\mkern 1.0muU^{\top}X}\varphi\_{i}(p,q) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | exp⁡(i​p​r​τ+i​q​a​τ+γ+λσ2​(1−ζ)​v−γ−λσ2​a​τ+2​aσ2​ln⁡ζ).\displaystyle\exp\left(\mathrm{i}\mkern 1.0mupr\tau+\mathrm{i}\mkern 1.0muqa\tau+\frac{\gamma+\lambda}{\sigma^{2}}\left(1-\zeta\right)v-\frac{\gamma-\lambda}{\sigma^{2}}a\tau+\frac{2a}{\sigma^{2}}\ln\zeta\right). |  | (2.14) |

The characteristic function is used to calculate the values of PiP\_{i} by letting q=0q=0

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pi=12+1π​∫0∞Re​[ψi​(p)p​i]​𝑑p.\displaystyle P\_{i}=\frac{1}{2}+\frac{1}{\pi}\int\_{0}^{\infty}\text{Re}\left[\frac{\psi\_{i}\left(p\right)}{p\mathrm{i}\mkern 1.0mu}\right]dp. |  | (2.15) |

The original characteristic function solution given by heston1993closed is

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ^i​(p)=exp⁡{C​(T−t,p)+D​(T−t,p)+i​p​x},\hat{\varphi}\_{i}(p)=\exp\left\{C\left(T-t,p\right)+D\left(T-t,p\right)+\mathrm{i}\mkern 1.0mupx\right\}, |  | (2.16) |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | C​(τ,p)\displaystyle C\left(\tau,p\right) | =r​p​τ​i+aσ2​{(bi−ρ​σ​p​i+γ)​τ−2​ln⁡[1−g​eγ​r1−g]},\displaystyle=rp\tau\mathrm{i}\mkern 1.0mu+\frac{a}{\sigma^{2}}\left\{\left(b\_{i}-\rho\sigma p\mathrm{i}\mkern 1.0mu+\gamma\right)\tau-2\ln\left[\frac{1-ge^{\gamma r}}{1-g}\right]\right\}, |  | (2.17) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | D​(τ,p)\displaystyle D\left(\tau,p\right) | =bi−ρ​σ​p​i+γσ2​[1−eγ​r1−g​eγ​r],\displaystyle=\frac{b\_{i}-\rho\sigma p\mathrm{i}\mkern 1.0mu+\gamma}{\sigma^{2}}\left[\frac{1-e^{\gamma r}}{1-ge^{\gamma r}}\right], |  | (2.18) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g\displaystyle g | =bi−ρ​σ​p​i+γbi−ρ​σ​p​i−γ.\displaystyle=\frac{b\_{i}-\rho\sigma p\mathrm{i}\mkern 1.0mu+\gamma}{b\_{i}-\rho\sigma p\mathrm{i}\mkern 1.0mu-\gamma}. |  | (2.19) |

The term gg in equations ([2.17](https://arxiv.org/html/2512.05326v1#S2.E17 "In 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model"))-([2.19](https://arxiv.org/html/2512.05326v1#S2.E19 "In 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")) can encounter a zero denominator, and when this occurs, large values of pp cause the argument of the logarithm to rotate rapidly. This effect can be seen from the asymptotic behavior for large |p||p|,

|  |  |  |
| --- | --- | --- |
|  | eγ​τ∼eσ​1−ρ2​|p|​τ,e^{\gamma\tau}\sim e^{\sigma\sqrt{1-\rho^{2}}\,|p|\tau}, |  |

which induces rapid phase variation in the logarithm and produces the apparent discontinuity shown in Figure [2.1](https://arxiv.org/html/2512.05326v1#S2.F1 "Figure 2.1 ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model"). A detailed discussion of the singularity in the original Heston characteristic function can be found in MR3375192. The logarithmic term in the joint characteristic function ([2.10](https://arxiv.org/html/2512.05326v1#S2.E10 "In Theorem 2.1. ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")) has no singularities. Therefore, the representation in ([2.10](https://arxiv.org/html/2512.05326v1#S2.E10 "In Theorem 2.1. ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")) does not suffer from the discontinuity problem. Other representations of the characteristic function appear in kahl2005not, where an adjustment of the phase rotation is introduced, and in cui2017full, where hyperbolic functions are used. In Figure [2.1](https://arxiv.org/html/2512.05326v1#S2.F1 "Figure 2.1 ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model") we present the original characteristic function of heston1993closed, and in Figure [2.2](https://arxiv.org/html/2512.05326v1#S2.F2 "Figure 2.2 ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model") we present the characteristic function given by ([2.10](https://arxiv.org/html/2512.05326v1#S2.E10 "In Theorem 2.1. ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")). The integrands shown in Figures [2.1](https://arxiv.org/html/2512.05326v1#S2.F1 "Figure 2.1 ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model") and [2.2](https://arxiv.org/html/2512.05326v1#S2.F2 "Figure 2.2 ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model") show the values of ψi/(p​i)\psi\_{i}/(p\mathrm{i}\mkern 1.0mu) that appear in the integral ([2.15](https://arxiv.org/html/2512.05326v1#S2.E15 "In 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")).

Figure 2.1: Heston’s characteristic function

![Refer to caption](x1.png)


Λ=1\Lambda=1, r=0.03r=0.03, ρ=−0.8\rho=-0.8, κ=3\kappa=3, θ=0.1\theta=0.1, σ=0.25\sigma=0.25, τ=5\tau=5




Figure 2.2: Joint characteristic function

![Refer to caption](x2.png)


Λ=1\Lambda=1, r=0.03r=0.03, ρ=−0.8\rho=-0.8, κ=3\kappa=3, θ=0.1\theta=0.1, σ=0.25\sigma=0.25, τ=5\tau=5

To obtain a simple expression of the derivative of ([2.1](https://arxiv.org/html/2512.05326v1#S2.Ex14 "2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")), we introduce the following notation

|  |  |  |
| --- | --- | --- |
|  | α=γ+λσ2,β=γ−λσ2,\alpha=\frac{\gamma+\lambda}{\sigma^{2}},~~\beta=\frac{\gamma-\lambda}{\sigma^{2}}, |  |

and rewrite equation ([2.1](https://arxiv.org/html/2512.05326v1#S2.Ex14 "2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψi​(p,q)=exp⁡(i​p​r​τ+i​q​a​τ+α​(1−ζ)​v−β​a​τ+2​aσ2​ln⁡ζ), for ​ζ=α+βα+β​e−γ​τ.\psi\_{i}(p,q)=\exp\left(\mathrm{i}\mkern 1.0mupr\tau+\mathrm{i}\mkern 1.0muqa\tau+\alpha\left(1-\zeta\right)v-\beta a\tau+\frac{2a}{\sigma^{2}}\ln\zeta\right),\text{ for }~\zeta=\frac{\alpha+\beta}{\alpha+\beta e^{-\gamma\tau}}. |  | (2.20) |

We obtain the first-order derivative from ([2.20](https://arxiv.org/html/2512.05326v1#S2.E20 "In 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")) as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂ψi∂p=\displaystyle\frac{\partial\psi\_{i}}{\partial p}= | φ​(i​r​τ+(αp​(1−ζ)−α​ζp)​v−βp​a​τ+2​aσ2​ζ1),\displaystyle\varphi\left(\mathrm{i}\mkern 1.0mur\tau+\left(\alpha\_{p}\left(1-\zeta\right)-\alpha\zeta\_{p}\right)v-\beta\_{p}a\tau+\frac{2a}{\sigma^{2}}\zeta\_{1}\right), |  | (2.21) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂ψi∂q=\displaystyle\frac{\partial\psi\_{i}}{\partial q}= | φ​((αq​(1−ζ)−α​ζq)​v+2​aσ2​ζ2),\displaystyle\varphi\left(\left(\alpha\_{q}\left(1-\zeta\right)-\alpha\zeta\_{q}\right)v+\frac{2a}{\sigma^{2}}\zeta\_{2}\right), |  | (2.22) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | γp\displaystyle\gamma\_{p} | =σ2​(1−ρ2)​p−i​(σ2​ci+σ​ρ​bi)γ,αp=γp−i​σ​ρσ2,βp=γp+i​σ​ρσ2,\displaystyle=\frac{\sigma^{2}(1-\rho^{2})p-\mathrm{i}\mkern 1.0mu(\sigma^{2}c\_{i}+\sigma\rho b\_{i})}{\gamma},\qquad\alpha\_{p}=\frac{\gamma\_{p}-\mathrm{i}\mkern 1.0mu\sigma\rho}{\sigma^{2}},\quad\beta\_{p}=\frac{\gamma\_{p}+\mathrm{i}\mkern 1.0mu\sigma\rho}{\sigma^{2}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ζp\displaystyle\zeta\_{p} | =αp+βpα+β​ζ−αp+βp​e−γ​τα+β​ζ2+γp​τ​(1−α​ζα+β)​ζ,ζq=1−e−γ​τα+β​ζ2​i,\displaystyle=\frac{\alpha\_{p}+\beta\_{p}}{\alpha+\beta}\zeta-\frac{\alpha\_{p}+\beta\_{p}e^{-\gamma\tau}}{\alpha+\beta}\zeta^{2}+\gamma\_{p}\tau\left(1-\frac{\alpha\zeta}{\alpha+\beta}\right)\zeta,\qquad\zeta\_{q}=\frac{1-e^{-\gamma\tau}}{\alpha+\beta}\zeta^{2}\mathrm{i}\mkern 1.0mu, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ζ1\displaystyle\zeta\_{1} | =αp+βpα+β−αp+βp​e−γ​τα+β​ζ+γp​τ​(1−α​ζα+β),ζ2=1−e−γ​τα+β​ζ​i.\displaystyle=\frac{\alpha\_{p}+\beta\_{p}}{\alpha+\beta}-\frac{\alpha\_{p}+\beta\_{p}e^{-\gamma\tau}}{\alpha+\beta}\zeta+\gamma\_{p}\tau\left(1-\frac{\alpha\zeta}{\alpha+\beta}\right),\qquad\zeta\_{2}=\frac{1-e^{-\gamma\tau}}{\alpha+\beta}\zeta\mathrm{i}\mkern 1.0mu. |  |

The representation obtained in Theorem [2.1](https://arxiv.org/html/2512.05326v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model") is continuously differentiable in all parameters and avoids the branch–cut discontinuities in the classical Heston characteristic function. This smooth form is particularly advantageous for numerical work, since it ensures stable evaluation of Fourier transforms and facilitates both pricing and calibration. In the next section we incorporate this representation into a convolution–FFT method for option valuation under the Heston model.

## 3 Convolution-FFT method

In this section we apply the differentiable characteristic function obtained in Section [2](https://arxiv.org/html/2512.05326v1#S2 "2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model") to the convolution method for option valuation. The value of a European option can be written as the convolution of the payoff with the transition density of the log-price process. When the convolution is evaluated on a truncated interval using the discrete Fourier transform, the FFT can be used to compute the option value efficiently on a uniform spatial grid. The use of the smooth characteristic function developed above improves the numerical stability of these Fourier-based calculations.

We use the following conventions for the Fourier transform. For a function f:ℝd→ℝf:\mathbb{R}^{d}\to\mathbb{R}, the Fourier transform and its inverse are defined by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | F​(u)=F​[f​(x)]​(u)\displaystyle F(u)=F[f(x)](u) | =∫ℝde−i​u⊤​x​f​(x)​𝑑x,\displaystyle=\int\_{\mathbb{R}^{d}}e^{-iu^{\top}x}f(x)\,dx, |  | (3.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f​(x)=F−1​[F​(u)]​(x)\displaystyle f(x)=F^{-1}[F(u)](x) | =1(2​π)d​∫ℝdei​x⊤​u​F​(u)​𝑑u.\displaystyle=\frac{1}{(2\pi)^{d}}\int\_{\mathbb{R}^{d}}e^{ix^{\top}u}F(u)\,du. |  | (3.2) |

We also use the convolution theorem, which states that for functions
f,g:ℝd→ℝf,g:\mathbb{R}^{d}\to\mathbb{R},

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​[f∗g]​(u)=F​[f]​(u)​F​[g]​(u),F[f\*g](u)=F[f](u)\,F[g](u), |  | (3.3) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | (f∗g)​(x)=∫ℝdf​(x−y)​g​(y)​𝑑y.(f\*g)(x)=\int\_{\mathbb{R}^{d}}f(x-y)g(y)\,dy. |  | (3.4) |

This identity underlies the convolution method developed in this paper, since the option value can be written as the convolution of the payoff function with the transition density of the log-price process, following the formulation introduced in hyndman2017convolution.

We consider two implementations of the convolution method. In the first, which we refer to as CFFT-I, the convolution is applied directly to the option function using the characteristic function of the log-price increment. In the second, CFFT-II, we use the two-dimensional characteristic function of (Xt,Vt)(X\_{t},V\_{t}) and integrate out the variance analytically. Both methods use the FFT to evaluate the convolution efficiently, but CFFT-II can offer improved stability for certain parameter values.

The premise of the convolution method is that the conditional probability density ϕ​(xt∣x,v)\phi(x\_{t}\mid x,v) depends only on the increment xt−xx\_{t}-x,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(xt∣x,v)=ϕ​(xt−x∣v),\phi(x\_{t}\mid x,v)=\phi(x\_{t}-x\mid v), |  | (3.5) |

as an approximation valid for short time increments Δ​t\Delta t, consistent with the locally Gaussian behavior of the Heston transition density.
Although the notation in ([3.5](https://arxiv.org/html/2512.05326v1#S3.E5 "In 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")) resembles the translation-invariance assumption used in the CONV method of lord2008fast, the underlying meaning is different. In their setting, the relation f​(y∣x)=f​(y−x)f(y\mid x)=f(y-x) arises from a Lévy-process representation and holds globally in maturity, leading to a convolution in the strike variable within the Carr and Madan framework. In our setting, ([3.5](https://arxiv.org/html/2512.05326v1#S3.E5 "In 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")) is understood in the short-time Gaussian limit of the Heston model and is used to express the option value as an analytical convolution of the payoff with the transition density. This density-based formulation differs fundamentally from the strike-space convolution in lord2008fast and plays a distinct role in the development of the CFFT methods introduced below.

In the Heston model, the short-time behavior of the transition density can be studied using the Fokker–Planck equation (see risken1996fokker). As shown by dragulescu2002probability, over a small time step Δ​t\Delta t the conditional distribution of xtx\_{t} is well approximated by a Gaussian with variance vv:

|  |  |  |
| --- | --- | --- |
|  | ϕ​(xt∣x,v)=12​π​v​Δ​t​exp⁡(−(xt−x−(r−12​v)​Δ​t)22​v​Δ​t)=ϕ​(xt−x∣v).\phi(x\_{t}\mid x,v)=\frac{1}{\sqrt{2\pi v\Delta t}}\exp\!\left(-\frac{(x\_{t}-x-(r-\tfrac{1}{2}v)\Delta t)^{2}}{2v\Delta t}\right)=\phi(x\_{t}-x\mid v). |  |

This convolution structure holds exactly under the short-time Gaussian approximation and numerically provides the basis for evaluating the conditional probabilities PiP\_{i}.

Applying the Fourier transform to PiP\_{i} and using the convolution theorem on the target function and the density function, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​[Pi​(x)]​(p)=\displaystyle F\left[P\_{i}(x)\right](p)= | F​[𝔼i​[𝟏ST≥K|x=ln⁡(S/K)]]​(p)=F​[∫ℝδ​(y)​ϕi​(y|x)​𝑑y]​(p)\displaystyle F\left[\mathbb{E}\_{i}\left[\mathbf{1}\_{S\_{T}\geq K}\left|x=\ln{({S}/{K})}\right.\right]\right](p)=F\left[\int\_{\mathbb{R}}\delta(y)\phi\_{i}(y|x)dy\right](p) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | F​[(δ​(y)∗ϕi​(y−x))​(x)]​(p)\displaystyle F\left[\left(\delta(y)\*\phi\_{i}(y-x)\right)(x)\right](p) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | F​[(δ​(y)∗ϕi​(−y))​(x)]​(p)\displaystyle F\left[\left(\delta(y)\*\phi\_{i}(-y)\right)(x)\right](p) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | F​[δ​(y)]​(p)​F​[ϕi​(−y)]​(p),\displaystyle F\left[\delta(y)\right](p)F\left[\phi\_{i}(-y)\right](p), |  | (3.6) |

where the δ​(⋅)\delta(\cdot) denotes the indicator function

|  |  |  |
| --- | --- | --- |
|  | δ​(x)={1,if ​x≥00,otherwise.\delta(x)=\begin{cases}1,&\text{if }\ x\geq 0\\ 0,&\text{otherwise}.\end{cases} |  |

The Fourier transform of the density function in ([3.6](https://arxiv.org/html/2512.05326v1#S3.E6 "In 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​[ϕi​(−y)]​(p)=\displaystyle F\left[\phi\_{i}(-y)\right](p)= | ∫ℝe−i​p​y​ϕ​(−y)​𝑑y=∫ℝei​p​(y−x)​ϕi​(y−x)​𝑑y\displaystyle\int\_{\mathbb{R}}e^{-\mathrm{i}\mkern 1.0mupy}\phi(-y)dy=\int\_{\mathbb{R}}e^{\mathrm{i}\mkern 1.0mup(y-x)}\phi\_{i}(y-x)dy |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | e−i​p​x​∫ℝei​p​y​ϕi​(y|x)​𝑑y=e−i​p​x​𝔼i​[ei​p​xT|x]\displaystyle e^{-\mathrm{i}\mkern 1.0mupx}\int\_{\mathbb{R}}e^{\mathrm{i}\mkern 1.0mupy}\phi\_{i}(y\left|x\right.)dy=e^{-\mathrm{i}\mkern 1.0mupx}\mathbb{E}\_{i}\left[e^{\mathrm{i}\mkern 1.0mupx\_{T}}\left|x\right.\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | e−i​p​x​φi​(p)=ψi​(p).\displaystyle e^{-\mathrm{i}\mkern 1.0mupx}\varphi\_{i}(p)=\psi\_{i}(p). |  | (3.7) |

We simplify ([3.6](https://arxiv.org/html/2512.05326v1#S3.E6 "In 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")) as

|  |  |  |
| --- | --- | --- |
|  | F​[Pi​(x)]​(p)=F​[δ​(x)]​(p)​ψi​(p),F\left[P\_{i}(x)\right](p)=F\left[\delta(x)\right](p)\psi\_{i}(p), |  |

and recover PiP\_{i} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pi​(x)=F−1​[F​[δ​(x)]​(p)​ψi​(p)].P\_{i}(x)=F^{-1}\left[F\left[\delta(x)\right](p)\psi\_{i}(p)\right]. |  | (3.8) |

We apply the change of variables to x=ln⁡SKx=\ln\frac{S}{K} with varying SS and obtain the pricing formula to ([2.7](https://arxiv.org/html/2512.05326v1#S2.E7 "In 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")) by the discrete Fourier transform:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(S,K,v,t)=\displaystyle C(S,K,v,t)= | S​P1​(S,K)−K​e−r​τ​P2​(S,K)\displaystyle SP\_{1}\left(S,K\right)-Ke^{-r\tau}P\_{2}\left(S,K\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | S​F−1​[F​[δ​(x)]​(p)​ψ1​(p)]​(x)−K​e−r​τ​F−1​[F​[δ​(x)]​(p)​ψ2​(p)]​(x)\displaystyle SF^{-1}\left[F\left[\delta(x)\right](p)\psi\_{1}(p)\right](x)-Ke^{-r\tau}F^{-1}\left[F\left[\delta(x)\right](p)\psi\_{2}(p)\right](x) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≈\displaystyle\approx | S​P~1−K​e−r​τ​P~2,\displaystyle S\tilde{P}\_{1}-Ke^{-r\tau}\tilde{P}\_{2}, |  | (3.9) |

where the discretization of the real space is

|  |  |  |
| --- | --- | --- |
|  | xn=(n−N2)​Δ​x, for ​n=0,1,⋯,N−1, and ​Δ​x=LN,x\_{n}=\left(n-\frac{N}{2}\right)\Delta x,\text{ for }n=0,1,\cdots,N-1,\text{ and }\Delta x=\frac{L}{N}, |  |

and the discretization of the frequency space is

|  |  |  |
| --- | --- | --- |
|  | pn=(n−N2)​Δ​p, for ​n=0,1,⋯,N−1, and ​Δ​p=2​πL.p\_{n}=\left(n-\frac{N}{2}\right)\Delta p,\text{ for }n=0,1,\cdots,N-1,\text{ and }\Delta p=\frac{2\pi}{L}. |  |

For a grid function f​(xn,ym)f(x\_{n},y\_{m}) defined on an N×MN\times M uniform lattice,
the discrete Fourier transform (DFT) and its inverse are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒟​[f]​(ui,vj)\displaystyle\mathcal{D}[f](u\_{i},v\_{j}) | =∑k=0N−1∑l=0M−1e−i​(k​iN+l​jM)​f​(xk,yl),\displaystyle=\sum\_{k=0}^{N-1}\sum\_{l=0}^{M-1}e^{-i\left(\frac{ki}{N}+\frac{lj}{M}\right)}f(x\_{k},y\_{l}), |  | (3.10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒟−1​[F]​(xk,yl)\displaystyle\mathcal{D}^{-1}[F](x\_{k},y\_{l}) | =1N​M​∑i=0N−1∑j=0M−1ei​(k​iN+l​jM)​F​(ui,vj).\displaystyle=\frac{1}{NM}\sum\_{i=0}^{N-1}\sum\_{j=0}^{M-1}e^{i\left(\frac{ki}{N}+\frac{lj}{M}\right)}F(u\_{i},v\_{j}). |  | (3.11) |

The CFFT estimation of P~i\tilde{P}\_{i} using the formula given in equation ([3.8](https://arxiv.org/html/2512.05326v1#S3.E8 "In 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | P~i=(−1)n​𝒟−1​[{wk​𝒟​[{wn​(−1)n​δ​(xn)}n=0N−1]​(pk)​ψi​(pk)}k=0N−1]n,\tilde{P}\_{i}=(-1)^{n}\mathcal{D}^{-1}\left[\left\{w\_{k}\mathcal{D}\left[\left\{w\_{n}(-1)^{n}\delta(x\_{n})\right\}\_{n=0}^{N-1}\right](p\_{k})\psi\_{i}\left(p\_{k}\right)\right\}\_{k=0}^{N-1}\right]\_{n}, |  | (3.12) |

where wnw\_{n} denotes the standard trapezoidal weights on the interval [−L/2,L/2][-L/2,L/2]. Here 𝒟\mathcal{D} and 𝒟−1\mathcal{D}^{-1} in to represent application of these discrete transforms to the spatial grid.

###### Remark 3.1.

The option price given by ([3.9](https://arxiv.org/html/2512.05326v1#S3.E9 "In 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")) is similar to the Black-Scholes model except that the probability terms P~1\tilde{P}\_{1} and P~2\tilde{P}\_{2} do not have explicit formulas. In our numerical approach, we use ([3.12](https://arxiv.org/html/2512.05326v1#S3.E12 "In 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")) to estimate the value of the probability terms. We denote this approach as the CFFT-I method.

Although the convolution method is efficient, the use of a truncated spatial domain introduces boundary error when the payoff is unbounded or nonperiodic on [−L/2,L/2][-L/2,L/2]. This typically appears as oscillations near the boundaries of the interval and can degrade the accuracy of FFT-based convolution. To mitigate this effect, we adopt the damping and shifting transformations introduced in [hyndman2017convolution] and adapt them to the Heston model. These transformations reduce boundary error and improve the numerical stability of both CFFT-I and CFFT-II.

Next, we introduce the CFFT-II method. To make the target function bounded and integrable, we introduce a damping parameter and write the Fourier transform of the convolution as a product

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​[eα​x​C​(x)]​(p)=\displaystyle F\left[e^{\alpha x}C(x)\right](p)= | e−r​τ​∫ℝe−i​p​x​eα​x​𝔼ℚ​[(K​exT−K)+∣x]​𝑑x\displaystyle e^{-r\tau}\int\_{\mathbb{R}}e^{-ipx}e^{\alpha x}\,\mathbb{E}^{\mathbb{Q}}\!\left[(Ke^{x\_{T}}-K)^{+}\mid x\right]dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | e−r​τ​∫ℝe−i​p​x​eα​x​∫ℝg​(y)​ϕ2​(y−x)​𝑑y​𝑑x\displaystyle e^{-r\tau}\int\_{\mathbb{R}}e^{-\mathrm{i}\mkern 1.0mupx}e^{\alpha x}\int\_{\mathbb{R}}g(y)\phi\_{2}(y-x)\,dy\,dx |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | e−r​τ​F​[eα​x​g​(x)]​(p)​ψ2​(p+α​i),\displaystyle e^{-r\tau}\,F\left[e^{\alpha x}g(x)\right](p)\,\psi\_{2}(p+\alpha\mathrm{i}\mkern 1.0mu), |  | (3.13) |

where g​(x)=(ex−K)+g(x)=\left(e^{x}-K\right)^{+}.

The call option pricing function is obtained by inverting and undamping ([3](https://arxiv.org/html/2512.05326v1#S3.Ex13 "3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(x)=e−r​τ−α​x​F−1​[F​[eα​x​g​(x)]​ψ2​(p+α​i)]​(x).C(x)=e^{-r\tau-\alpha x}\,F^{-1}\left[F\left[e^{\alpha x}g(x)\right]\psi\_{2}(p+\alpha\mathrm{i}\mkern 1.0mu)\right](x). |  | (3.14) |

We denote the approach based on equation ([3.14](https://arxiv.org/html/2512.05326v1#S3.E14 "In 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")) as the CFFT-II method. In the next sections, we first present the error analysis and then introduce two methods to improve the boundary error of the CFFT method.

### 3.1 Error analysis

Let C~=S​P~1−K​e−r​τ​P~2\tilde{C}=S\tilde{P}\_{1}-Ke^{-r\tau}\tilde{P}\_{2} denote the convolution based approximation to the call option, with remining life τ\tau, using the convolution result in ([3.9](https://arxiv.org/html/2512.05326v1#S3.E9 "In 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")).
To analyze the associated truncation and discretization errors, we first examine the Fourier series expansion and the decay properties of the characteristic function. Firstly, we investigate the Fourier expansion of a piece-wise smooth function ff with finite limiting point on [−L2,L2][-\frac{L}{2},\frac{L}{2}]

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x)=∑j=−∞∞Fj​e−i​j​2​π​xL,f(x)=\sum\_{j=-\infty}^{\infty}F\_{j}e^{-\mathrm{i}\mkern 1.0muj\frac{2\pi x}{L}}, |  | (3.15) |

with the coefficients FjF\_{j}

|  |  |  |
| --- | --- | --- |
|  | Fj=1L​∫−L2L2f​(x)​ei​j​2​π​xL​𝑑x.F\_{j}=\frac{1}{L}\int\_{-\frac{L}{2}}^{\frac{L}{2}}f(x)e^{\mathrm{i}\mkern 1.0muj\frac{2\pi x}{L}}dx. |  |

The Fourier coefficients Fj→0F\_{j}\rightarrow 0 as |j|→±∞|j|\rightarrow\pm\infty and |Fj|≤f¯|F\_{j}|\leq\bar{f}
when ff is bounded on [−L2,L2][-\frac{L}{2},\frac{L}{2}].
Thus we can bound the modulus of FjF\_{j} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Fj|≤min⁡(f¯,ϵ​(L)|j|),\left|F\_{j}\right|\leq\min\left(\bar{f},\frac{\epsilon(L)}{\left|j\right|}\right), |  | (3.16) |

for a positive bounding constant ϵ​(L)\epsilon(L), depending only on LL.

Usually, the characteristic function of the Black-Scholes model decays as exp⁡(−c​x2)\exp\left(-cx^{2}\right) and that of the Heston model has exponential decays as exp⁡(−c​|x|)\exp(-c|x|) for some constant value of cc as discussed in lord2007optimal. We summarize the asymptotic behavior of the characteristic function ([2.10](https://arxiv.org/html/2512.05326v1#S2.E10 "In Theorem 2.1. ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")) in the following proposition.

###### Proposition 3.1 (Asymptotic characteristic function).

Assume that κ\kappa, θ\theta, σ\sigma, vv, and τ\tau are positive and that ρ∈(−1,1)\rho\in(-1,1). Then the kernel function ([3.7](https://arxiv.org/html/2512.05326v1#S3.E7 "In 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")) satisfies the asymptotic relation

|  |  |  |
| --- | --- | --- |
|  | ψi​(p)≈A∞​ei​B∞​exp⁡(−D​|p|),p→∞,\psi\_{i}(p)\approx A\_{\infty}\,e^{\mathrm{i}\mkern 1.0muB\_{\infty}}\,\exp\!\left(-D|p|\right),\qquad p\to\infty, |  |

where

|  |  |  |
| --- | --- | --- |
|  | A∞=(4​(1−ρ2))a/σ2,B∞=2​aσ2​arcsin⁡(sign⁡(p)​ρ)−ρσ​(v+sign⁡(p)​a​τ)​p,D=1−ρ2σ​(v+a​τ)>0.A\_{\infty}=\left(4(1-\rho^{2})\right)^{a/\sigma^{2}},\qquad B\_{\infty}=\frac{2a}{\sigma^{2}}\arcsin\!\left(\operatorname{sign}(p)\rho\right)-\frac{\rho}{\sigma}\left(v+\operatorname{sign}(p)a\tau\right)p,\qquad D=\frac{\sqrt{1-\rho^{2}}}{\sigma}\left(v+a\tau\right)>0. |  |

The proof is given in Appendix [A.2](https://arxiv.org/html/2512.05326v1#A1.SS2 "A.2 Proof of Proposition 3.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model").

By Proposition [3.1](https://arxiv.org/html/2512.05326v1#S3.Thmproposition1 "Proposition 3.1 (Asymptotic characteristic function). ‣ 3.1 Error analysis ‣ 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model"), we can bound the modulus of the characteristic function by

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ψi​(p)|≤ϵ​A∞​e−D​|p|,|\psi\_{i}(p)|\leq\epsilon A\_{\infty}e^{-D|p|}, |  | (3.17) |

for some positive constant ϵ\epsilon. The exponential decay of |ψi​(p)||\psi\_{i}(p)| implies that the Fourier integrand becomes negligible outside a finite truncation interval, which justifies the CFFT truncation. Using ([3.17](https://arxiv.org/html/2512.05326v1#S3.E17 "In 3.1 Error analysis ‣ 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")) together with the boundary estimate ([3.16](https://arxiv.org/html/2512.05326v1#S3.E16 "In 3.1 Error analysis ‣ 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")), we next derive bounds for both the truncation error and the discretization error. The following theorem provides an error bound for |C−C~||C-\tilde{C}|.

###### Theorem 3.1 (Error of the convolution method).

Let ff be an integrable function that is bounded by f¯\bar{f} on
[−L2,L2][-\tfrac{L}{2},\tfrac{L}{2}]. Under the measure PiP\_{i}, the error between the true value

|  |  |  |
| --- | --- | --- |
|  | E(x)=𝔼Pi[f(xT)|x0=x],E(x)=\mathbb{E}^{P\_{i}}\!\left[f(x\_{T})\,\middle|\,x\_{0}=x\right], |  |

and its CFFT approximation

|  |  |  |
| --- | --- | --- |
|  | E~​(xn)=(−1)n​𝒟−1​[{wk​𝒟​[{wn​(−1)n​f​(xn)}n=0N−1]​(uk)​ψi​(pk)}k=0N−1]n,\tilde{E}(x\_{n})=(-1)^{n}\,\mathcal{D}^{-1}\left[\left\{w\_{k}\,\mathcal{D}\left[\left\{w\_{n}(-1)^{n}f(x\_{n})\right\}\_{n=0}^{N-1}\right](u\_{k})\psi\_{i}(p\_{k})\right\}\_{k=0}^{N-1}\right]\_{n}, |  |

on the truncation interval [−L2,L2][-\tfrac{L}{2},\tfrac{L}{2}] with discretization parameters

|  |  |  |
| --- | --- | --- |
|  | xn=(n−N2)​Δ​x,n=0,…,N−1,Δ​x=LN,x\_{n}=\left(n-\tfrac{N}{2}\right)\Delta x,\quad n=0,\dots,N-1,\qquad\Delta x=\tfrac{L}{N}, |  |

|  |  |  |
| --- | --- | --- |
|  | pn=(n−N2)​Δ​p,n=0,…,N−1,Δ​p=2​πL,p\_{n}=\left(n-\tfrac{N}{2}\right)\Delta p,\quad n=0,\dots,N-1,\qquad\Delta p=\tfrac{2\pi}{L}, |  |

is bounded by

|  |  |  |
| --- | --- | --- |
|  | |E−E~|≤ϵ1​e−π​DL​N+ϵ2​N−m,|E-\tilde{E}|\leq\epsilon\_{1}\,e^{-\frac{\pi D}{L}N}+\epsilon\_{2}\,N^{-m}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | ϵ1=L​A∞​f¯​e2​π​DLπ​D​ϵv,τ,ϵ2=L​A∞π​D​ϵL​ϵv,τ,\epsilon\_{1}=\frac{LA\_{\infty}\bar{f}\,e^{\frac{2\pi D}{L}}}{\pi D}\,\epsilon\_{v,\tau},\qquad\epsilon\_{2}=\frac{LA\_{\infty}}{\pi D}\,\epsilon\_{L}\,\epsilon\_{v,\tau}, |  |

for some positive constants ϵv,τ\epsilon\_{v,\tau} and ϵL\epsilon\_{L}.

The proof is given in Appendix [A.3](https://arxiv.org/html/2512.05326v1#A1.SS3 "A.3 Proof of Theorem 3.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model").

Applying Theorem [3.1](https://arxiv.org/html/2512.05326v1#S3.Thmtheorem1 "Theorem 3.1 (Error of the convolution method). ‣ 3.1 Error analysis ‣ 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model"), we obtain the following bound for
|Pi−P~i||P\_{i}-\tilde{P}\_{i}|:

|  |  |  |
| --- | --- | --- |
|  | |ei|=|Pi−P~i|≤L​A∞​f¯​e2​π​DLπ​D​ϵv,τ​e−π​DL​N+L​A∞π​D​ϵL​ϵv,τ​N−m.|e\_{i}|=|P\_{i}-\tilde{P}\_{i}|\leq\frac{LA\_{\infty}\bar{f}\,e^{\frac{2\pi D}{L}}}{\pi D}\,\epsilon\_{v,\tau}\,e^{-\frac{\pi D}{L}N}+\frac{LA\_{\infty}}{\pi D}\,\epsilon\_{L}\,\epsilon\_{v,\tau}\,N^{-m}. |  |

Using this estimate for i=1,2i=1,2, we obtain an error bound for the pricing error of a call option in the Heston model under the CFFT-I method:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |e​(x)|\displaystyle|e(x)| | =|C​(x)−C~​(x)|\displaystyle=|C(x)-\tilde{C}(x)| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =|K​ex​(P1​(x)−P~1​(x))−K​e−r​τ​(P2​(x)−P~2​(x))|\displaystyle=\left|Ke^{x}\left(P\_{1}(x)-\tilde{P}\_{1}(x)\right)-Ke^{-r\tau}\left(P\_{2}(x)-\tilde{P}\_{2}(x)\right)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K​ex​|e1|+K​e−r​τ​|e2|\displaystyle\leq Ke^{x}\,|e\_{1}|+Ke^{-r\tau}\,|e\_{2}| |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤K​(ex+e−r​τ)​(L​A∞​f¯​e2​π​DLπ​D​ϵv,τ​e−π​DL​N+L​A∞π​D​ϵL​ϵv,τ​N−m).\displaystyle\leq K\left(e^{x}+e^{-r\tau}\right)\left(\frac{LA\_{\infty}\bar{f}\,e^{\frac{2\pi D}{L}}}{\pi D}\,\epsilon\_{v,\tau}\,e^{-\frac{\pi D}{L}N}+\frac{LA\_{\infty}}{\pi D}\,\epsilon\_{L}\,\epsilon\_{v,\tau}\,N^{-m}\right). |  | (3.18) |

A similar bound can be derived for the CFFT-II method. We summarize the resulting error estimate for |e||e| in the following corollary.

###### Corollary 3.1.

For the Heston call option, the CFFT-I and CFFT-II methods satisfy the error estimate

|  |  |  |
| --- | --- | --- |
|  | |e|≤𝒪​(e−π​DL​N)+𝒪​(N−m),|e|\leq\mathcal{O}\!\left(e^{-\frac{\pi D}{L}N}\right)+\mathcal{O}\!\left(N^{-m}\right), |  |

for any m≥2m\geq 2.

###### Note 3.1.

We observe that the discretization error is at least second order, consistent with the findings of lord2008fast, while the truncation error decays exponentially with the frequency. Equation ([3.1](https://arxiv.org/html/2512.05326v1#S3.Ex25 "3.1 Error analysis ‣ 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")) also indicates that the boundary errors increase as xx approaches ±L/2\pm L/2, which motivates the boundary-control schemes introduced in the next subsection.

Unlike the Carr and Madan and COS methods, for which truncation errors are typically assessed empirically, we obtain an explicit analytical error bound for the convolution approximation. The bound shows exponential decay of the truncation error and second-order convergence of the discretization error, providing a rigorous theoretical foundation for the proposed CFFT method.

### 3.2 Boundary control for the CFFT method

Our first consideration when applying the Fourier transform to option pricing is the feasibility of the transform.
Sufficient conditions for successfully applying Fourier transform require the target function to be L1L\_{1}-integrable.
However, the call option payoff is not L1L\_{1}-integrable with respect to either the log-price or the log-strike.
Nevertheless, we can still apply the Fourier transform to the target function on a truncated region by introducing a damping parameter, which attenuates the nonintegrable tail toward zero. Equation ([3.14](https://arxiv.org/html/2512.05326v1#S3.E14 "In 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")) is well-defined provided that the (α+1)th(\alpha+1)^{\text{th}} moment of StS\_{t} exists, as pointed out by lord2007optimal

|  |  |  |
| --- | --- | --- |
|  | |φ​(p−(α+1)​i)|≤φ​(−(α+1)​i)=𝔼​[ST(α+1)]≤∞.\left|\varphi(p-(\alpha+1)\mathrm{i}\mkern 1.0mu)\right|\leq\varphi(-(\alpha+1)\mathrm{i}\mkern 1.0mu)=\mathbb{E}\left[S\_{T}^{(\alpha+1)}\right]\leq\infty. |  |

After ensuring feasibility, we next consider periodicity effects introduced by the Fourier transform. Our second consideration concerns the periodicity effects introduced by the Fourier transform, since the inverse transform may distort a nonperiodic target function. Comparing the truncation on logarithms of the strike price in lord2007optimal, our truncation on the logarithm of the stock price could lead to large boundary errors when the option is exponentially increasing as the underlying asset moves to deep in-the-money. Such problems can be found in hyndman2017convolution, however, they introduced a shifting method on the target function to address the boundary error. The basic idea of shifting the target function is to map it from non-periodic to a periodic function which would be considered as a real signal. The shifting method requires a function h​(x)h(x) with explicit expectation 𝔼​[h​(xt)|x]\mathbb{E}\left[h(x\_{t})\left|x\right.\right]. Thus the candidate for shifting function h​(x)h(x) can be chosen from polynomial and exponential functions. hyndman2017convolution suggest the first order polynomial as the shifting function h​(x)=A​x+Bh(x)=Ax+B such that the damping of the shifted target function f~α​(x)=eα​x​(f​(x)−h​(x))\tilde{f}^{\alpha}(x)=e^{\alpha x}\left(f(x)-h(x)\right) is smoothly connected at the boundaries

|  |  |  |  |
| --- | --- | --- | --- |
|  | f~α​(x0)=\displaystyle\tilde{f}^{\alpha}(x\_{0})= | f~α​(xn),\displaystyle\tilde{f}^{\alpha}(x\_{n}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​f~αd​x​(x0)=\displaystyle\frac{d\tilde{f}^{\alpha}}{dx}(x\_{0})= | d​f~αd​x​(xn).\displaystyle\frac{d\tilde{f}^{\alpha}}{dx}(x\_{n}). |  |

In our implementation, shifting the call option by a linear function generates a kink at the money and does not perform well. We therefore propose an exponential shift function h2=A​ex+Bh\_{2}=Ae^{x}+B to ensure smooth damping near the boundaries. In CFFT-I we choose a linear function h1=A​x+Bh\_{1}=Ax+B to shift the δ\delta function and in CFFT-II we choose an exponential function h2=A​ex+Bh\_{2}=Ae^{x}+B to shift the call option which can also be applied in BSDE-based numerical methods. For CFFT-I, for α=0\alpha=0, we have a linear-shift scheme:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(x)=A​x+B,f~α​(x)=f​(x)−h​(x),h(x)=Ax+B,\qquad\tilde{f}^{\alpha}(x)=f(x)-h(x), |  | (3.19) |

where

|  |  |  |
| --- | --- | --- |
|  | A=f​(xN)−f​(x0)xN−x0,B=xN​f​(x0)−x0​f​(xN)xN−x0.A=\frac{f(x\_{N})-f(x\_{0})}{x\_{N}-x\_{0}},\qquad B=\frac{x\_{N}f(x\_{0})-x\_{0}f(x\_{N})}{x\_{N}-x\_{0}}. |  |

For CFFT-II, for α<−1\alpha<-1, we have an exponential-shift scheme:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(x)=A​ex+B,f~α​(x)=eα​x​(f​(x)−h​(x)),h(x)=Ae^{x}+B,\qquad\tilde{f}^{\alpha}(x)=e^{\alpha x}\left(f(x)-h(x)\right), |  | (3.20) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | f0′=\displaystyle f^{\prime}\_{0}= | −3​f​(x0)+4​f​(x1)−f​(x2)2​Δ​x,fN′=3​f​(xN)−4​f​(xN−1)+f​(xN−2)2​Δ​x,\displaystyle\frac{-3f(x\_{0})+4f(x\_{1})-f(x\_{2})}{2\Delta x},\qquad f^{\prime}\_{N}=\frac{3f(x\_{N})-4f(x\_{N-1})+f(x\_{N-2})}{2\Delta x}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | A=\displaystyle A= | eα​xN​fN′−eα​x0​f0′e(α+1)​xN−e(α+1)​x0, and B=xN​f​(x0)−x0​f​(xN)xN−x0.\displaystyle\frac{e^{\alpha x\_{N}}f^{\prime}\_{N}-e^{\alpha x\_{0}}f^{\prime}\_{0}}{e^{(\alpha+1)x\_{N}}-e^{(\alpha+1)x\_{0}}},\qquad\text{ and }\qquad B=\frac{x\_{N}f(x\_{0})-x\_{0}f(x\_{N})}{x\_{N}-x\_{0}}. |  |

These transformations ensure continuity and smoothness of the damped target function at domain boundaries, significantly improving numerical stability.

We can recover CFFT-I by reversing the shifting scheme ([3.19](https://arxiv.org/html/2512.05326v1#S3.E19 "In 3.2 Boundary control for the CFFT method ‣ 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙi​[f​(xT)|x]=\displaystyle\mathbb{E}^{\mathbb{P}\_{i}}\left[f(x\_{T})\left|x\right.\right]= | 𝔼ℙi​[f~​(xT)|x]+𝔼ℙi​[h​(xT)|x]\displaystyle\mathbb{E}^{\mathbb{P}\_{i}}\left[\tilde{f}(x\_{T})\left|x\right.\right]+\mathbb{E}^{\mathbb{P}\_{i}}\left[h(x\_{T})\left|x\right.\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | F−1​[F​[f~​(x)]​(p)​ψi​(p)]​(x)+A​𝔼​[xT|x]+B\displaystyle F^{-1}\left[F\left[\tilde{f}(x)\right](p)\psi\_{i}(p)\right](x)+A\mathbb{E}\left[x\_{T}\left|x\right.\right]+B |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | F−1​[F​[f~​(x)]​(p)​ψi​(p)]​(x)−i​A​∂φi∂p​(0)+B,\displaystyle F^{-1}\left[F\left[\tilde{f}(x)\right](p)\psi\_{i}(p)\right](x)-\mathrm{i}\mkern 1.0muA\frac{\partial\varphi\_{i}}{\partial p}(0)+B, |  |

and recover CFFT-II by reversing the shifting scheme ([3.20](https://arxiv.org/html/2512.05326v1#S3.E20 "In 3.2 Boundary control for the CFFT method ‣ 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ2​[f​(xT)|x]=\displaystyle\mathbb{E}^{\mathbb{P}\_{2}}\left[f(x\_{T})\left|x\right.\right]= | 𝔼ℙ2​[f~​(xT)|x]+𝔼ℙ2​[h​(xT)|x]=e−α​x​F−1​[F​[eα​x​f~​(x)]​(p)​ψ2​(p)]​(x)+A​𝔼​[exT|x]+B\displaystyle\mathbb{E}^{\mathbb{P}\_{2}}\left[\tilde{f}(x\_{T})\left|x\right.\right]+\mathbb{E}^{\mathbb{P}\_{2}}\left[h(x\_{T})\left|x\right.\right]=e^{-\alpha x}F^{-1}\left[F\left[e^{\alpha x}\tilde{f}(x)\right](p)\psi\_{2}(p)\right](x)+A\mathbb{E}\left[e^{x\_{T}}\left|x\right.\right]+B |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | e−α​x​F−1​[F​[eα​x​f~​(x)]​(p)​ψ2​(p)]​(x)+A​φ2​(−i)+B.\displaystyle e^{-\alpha x}F^{-1}\left[F\left[e^{\alpha x}\tilde{f}(x)\right](p)\psi\_{2}(p)\right](x)+A\varphi\_{2}(-\mathrm{i}\mkern 1.0mu)+B. |  |

In the next section, we present the numerical results of the CFFT-I and CFFT-II methods applied to pricing problems in the Heston model.

## 4 Numerical results

We assess the accuracy of the proposed methods by comparing numerical results to the semi-closed-form Heston solution ([2.15](https://arxiv.org/html/2512.05326v1#S2.E15 "In 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")), and evaluate computational efficiency relative to the Carr and Madan FFT method. We first present the results of the CFFT-I method applied to the estimation of the probabilities in the Heston model. We then apply CFFT-II to price the European call option and illustrate the effect of the boundary control schemes.
We then summarize the performance of CFFT-II across a set of representative strikes. The comparison between the CFFT and FFT methods is conducted on both the log-stock and log-strike domains.

The truncated spatial domain is centered at log⁡(S/K)\log(S/K), with NN grid points
on the interval [x0,xN]=log⁡(S/K)+[−L/2,L/2][x\_{0},x\_{N}]=\log(S/K)+[-L/2,L/2]. Similarly, the interval [x0,xN]=log⁡(K/S)+[−L/2,L/2][x\_{0},x\_{N}]=\log(K/S)+[-L/2,L/2] is used for the log-strike domain. The parameters used are r=0.03r=0.03, v=0.1v=0.1, Λ=1\Lambda=1, ρ=−0.8\rho=-0.8, κ=3\kappa=3, θ=0.1\theta=0.1, σ=0.25\sigma=0.25, T=1T=1, L=10L=10, and N=2000N=2000.

Figure 4.3: Comparison of CFFT-I probabilities P1P\_{1} and P2P\_{2} with and without the shifting scheme.

![Refer to caption](x3.png)

Figure [4.3](https://arxiv.org/html/2512.05326v1#S4.F3 "Figure 4.3 ‣ 4 Numerical results ‣ Convolution-FFT for option pricing in the Heston model") illustrates the effect of the shifting scheme. The left panel shows the raw CFFT-I probabilities, and the right panel shows the results with shifting applied. The shifting scheme eliminates boundary oscillations near the truncation endpoints and improves numerical stability. We observe that the boundary values at x0x\_{0} and xNx\_{N} are accurately controlled when the shifting scheme is used: P1​(x0)=0P\_{1}(x\_{0})=0, P2​(x0)=0P\_{2}(x\_{0})=0, P1​(xN)=0.99999844P\_{1}(x\_{N})=0.99999844, and P2​(xN)=0.99999839P\_{2}(x\_{N})=0.99999839.
Inclusion of the shifting scheme clearly improves numerical stability and accuracy at the boundaries.

Figure [4.4](https://arxiv.org/html/2512.05326v1#S4.F4 "Figure 4.4 ‣ 4 Numerical results ‣ Convolution-FFT for option pricing in the Heston model") examines the accuracy of the CFFT-I method by comparing the results with both the FFT method and a numerical integration benchmark (denoted as “NUM”). The solid lines represent the error between the CFFT-I method and the numerical integration method, and the dashed lines represent the error between the FFT method and the numerical integration method. The CFFT-I method outperforms the FFT method except at the money, where the FFT method retains slightly higher precision.

Figure 4.4: Error of CFFT-I

![Refer to caption](x4.png)


r=0.03r=0.03, v=0.1v=0.1, Λ=1\Lambda=1, ρ=−0.8\rho=-0.8, κ=3\kappa=3, θ=0.1\theta=0.1, σ=0.25\sigma=0.25, T=1T=1, L=10L=10, N=2000N=2000




Figure 4.5: Error of CFFT-II

![Refer to caption](x5.png)


r=0.03r=0.03, v=0.1v=0.1, Λ=1\Lambda=1, ρ=−0.8\rho=-0.8, κ=3\kappa=3, θ=0.1\theta=0.1, σ=0.25\sigma=0.25, T=1T=1, L=10L=10, N=2000N=2000, α=−2\alpha=-2




Figure 4.6: CFFT-II error with different damping and shifting schemes.

![Refer to caption](x6.png)


r=0.03r=0.03, v=0.1v=0.1, Λ=1\Lambda=1, ρ=−0.8\rho=-0.8, κ=3\kappa=3, θ=0.1\theta=0.1, σ=0.25\sigma=0.25, T=1T=1, L=10L=10




Table 4.1: CPU time, call option values, and absolute errors relative to the semi-closed-form Heston solution for strikes K=80,100,120K=80,100,120.

CPU time (ms)
S=100,K=80
S=100,K=100
S=100,K=120


CFFT-II
FFT
call
error
call
error
call
error


N=2000
0.124
0.155
25.77846
5.93e-05
13.45867
2.60e-04
5.97903
1.40e-04

N=4000
0.175
0.294
25.77841
8.04E-06
13.45887
6.50e-05
5.97885
4.29e-05

N=8000
0.251
0.544
25.77841
4.60e-06
13.45892
1.63e-05
5.97889
4.73e-06

r=0.03r=0.03, v=0.1v=0.1, Λ=1\Lambda=1, ρ=−0.8\rho=-0.8, κ=3\kappa=3, θ=0.1\theta=0.1, σ=0.25\sigma=0.25, T=1T=1, L=10L=10, α=−2\alpha=-2

The CFFT-II method achieves comparable accuracy to the FFT benchmark with less than half the computational cost. The convergence behavior observed across increasing N aligns with the theoretical error analysis from Section 3.1. Similar to Figure [4.4](https://arxiv.org/html/2512.05326v1#S4.F4 "Figure 4.4 ‣ 4 Numerical results ‣ Convolution-FFT for option pricing in the Heston model"), Figure [4.5](https://arxiv.org/html/2512.05326v1#S4.F5 "Figure 4.5 ‣ 4 Numerical results ‣ Convolution-FFT for option pricing in the Heston model") shows the log-error for the CFFT-II method. The CFFT-II method is faster than CFFT-I, but boundary errors are more pronounced, particularly when the shifting scheme is omitted. The left panel of Figure [4.6](https://arxiv.org/html/2512.05326v1#S4.F6 "Figure 4.6 ‣ 4 Numerical results ‣ Convolution-FFT for option pricing in the Heston model") shows that the accuracy increases as the discretization NN increases, and that the boundary error is controlled by the damping and shifting schemes, consistent with the error analysis. The right panel of Figure [4.6](https://arxiv.org/html/2512.05326v1#S4.F6 "Figure 4.6 ‣ 4 Numerical results ‣ Convolution-FFT for option pricing in the Heston model") illustrates the effect of combining damping and shifting. Without these schemes, the error grows rapidly near both boundaries, while the combined approach yields stable and accurate results across the domain. The comparison among different choices of damping and shifting parameters in Figure [4.6](https://arxiv.org/html/2512.05326v1#S4.F6 "Figure 4.6 ‣ 4 Numerical results ‣ Convolution-FFT for option pricing in the Heston model") indicates that the damping parameter primarily reduces the left-boundary error, while the shifting parameter reduces the right-boundary error when the Fourier transform is applied to an unbounded and nonperiodic function.

Table [4.1](https://arxiv.org/html/2512.05326v1#S4.T1 "Table 4.1 ‣ 4 Numerical results ‣ Convolution-FFT for option pricing in the Heston model") presents numerical results for the CFFT-II and FFT methods on the log-stock domain with different values of NN. The option values for strikes K=80K=80, K=100K=100, and K=120K=120 are 25.7784025.77840, 13.4589313.45893, and 5.978895.97889, respectively. The FFT method, which behaves like an enhanced numerical integration method, is relatively insensitive to NN, and the errors remain on the order of 2.06×10−72.06\times 10^{-7} for all cases. In contrast, the CFFT-II method converges as NN increases and requires less computation time. The CPU times in Table [4.1](https://arxiv.org/html/2512.05326v1#S4.T1 "Table 4.1 ‣ 4 Numerical results ‣ Convolution-FFT for option pricing in the Heston model") indicate that CFFT-II has a significant computational speed advantage over FFT.

Numerically, the CFFT method achieves comparable or superior accuracy with smaller grids and reduced computation time, while eliminating the need for damping-parameter calibration required in the Carr and Madan approach. Furthermore, unlike the COS method, the CFFT method handles discontinuous or non-smooth payoffs without oscillatory artifacts near the truncation boundaries.

## 5 Conclusion

In this paper we developed a convolution–FFT method for option valuation under the Heston model. The key ingredients are a continuously differentiable representation of the characteristic function and an efficient convolution formulation on a truncated spatial domain. This approach eliminates the discontinuity issues of the classical Heston characteristic function and improves numerical stability in Fourier-based valuation. The availability of closed-form truncation and discretization error bounds further distinguishes the method from previous Heston FFT formulations, which rely primarily on empirical or heuristic error assessment.

We presented two implementations, CFFT-I and CFFT-II, and analyzed the boundary errors introduced by truncation. A combination of damping and shifting transformations was introduced to reduce these errors, with numerical experiments demonstrating that both methods provide accurate valuations and that the CFFT-II variant is particularly efficient for large-scale computations.

The convolution–FFT framework therefore offers a stable and mathematically justified alternative to existing Fourier-based pricing methods for the Heston model. By combining a smooth characteristic function with explicit analytical error bounds, the method provides both numerical reliability and practical guidance for parameter selection. These features make the convolution method a promising foundation for extensions to multi-factor volatility models, early-exercise features, and other complex derivative structures.

## Appendix A Appendix

In this appendix we provide the proofs of the technical results that would otherwise disrupt the flow of the paper.

### A.1 Proof of Theorem [2.1](https://arxiv.org/html/2512.05326v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")

###### Proof.

We solve the PDE ([2.9](https://arxiv.org/html/2512.05326v1#S2.E9 "In 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")) by substituting the exponential affine expression introduced in Section [2](https://arxiv.org/html/2512.05326v1#S2 "2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model") and matching coefficients of the terms in pp and qq. This reduces the PDE to a system of ordinary differential equations for the functions appearing in the characteristic-function representation. We may write

|  |  |  |
| --- | --- | --- |
|  | ∂Pi∂t+(r+ci​v)​∂Pi∂x+(a−bi​v)​∂Pi∂v+12​v​∂2Pi∂x2+σ22​v​∂2Pi∂v2+ρ​σ​v​∂2Pi∂x​∂v=0,\frac{\partial P\_{i}}{\partial t}+\left(r+c\_{i}v\right)\frac{\partial P\_{i}}{\partial x}+(a-b\_{i}v)\frac{\partial P\_{i}}{\partial v}+\frac{1}{2}v\frac{\partial^{2}P\_{i}}{\partial x^{2}}+\frac{\sigma^{2}}{2}v\frac{\partial^{2}P\_{i}}{\partial v^{2}}+\rho\sigma v\frac{\partial^{2}P\_{i}}{\partial x\partial v}=0, |  |

with boundary conditions

|  |  |  |
| --- | --- | --- |
|  | Pi​(T,𝑼,𝑿)=ei​𝑼⊤​𝑿=ei​(p​x+q​v)P\_{i}(T,\boldsymbol{U},\boldsymbol{X})=e^{\mathrm{i}\mkern 1.0mu\boldsymbol{U}^{\top}\boldsymbol{X}}=e^{\mathrm{i}\mkern 1.0mu\left(px+qv\right)} |  |

for i=1,2i=1,2 where U=(p,q)⊤U=(p,q)^{\top} and X=(x,v)⊤X=(x,v)^{\top}.
We make an ansatz for ψ​(t,p,q,x,v)\psi(t,p,q,x,v) in the following form

|  |  |  |
| --- | --- | --- |
|  | Pi​(t,p,q,x,v)=exp⁡(Ai​(t)​x+Bi​(t)​v+Ci​(t)),P\_{i}(t,p,q,x,v)=\exp\left(A\_{i}(t)x+B\_{i}(t)v+C\_{i}(t)\right), |  |

where functions A​(t)A(t), B​(t)B(t) and C​(t)C(t) depend only on tt and satisfy boundary conditions A​(T)=i​pA(T)=\mathrm{i}\mkern 1.0mup, B​(T)=i​qB(T)=\mathrm{i}\mkern 1.0muq and C​(T)=0C(T)=0.

Applying the ansatz to the PDE, we obtain the following ordinary differential equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ai′​(t)​x+(Bi′​(t)+12​Ai2+ci​Ai−bi​Bi+12​σ2​Bi2+ρ​σ​Ai​Bi)​v+Ci′​(t)+r​Ai​(t)+a​Bi​(t)=0.A\_{i}^{\prime}(t)x+\left(B\_{i}^{\prime}(t)+\frac{1}{2}A\_{i}^{2}+c\_{i}A\_{i}-b\_{i}B\_{i}+\frac{1}{2}\sigma^{2}B\_{i}^{2}+\rho\sigma A\_{i}B\_{i}\right)v+C\_{i}^{\prime}(t)+rA\_{i}(t)+aB\_{i}(t)=0. |  | (A.1) |

If equation ([A.1](https://arxiv.org/html/2512.05326v1#A1.E1 "In A.1 Proof of Theorem 2.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")) holds for all x∈ℝx\in\mathbb{R}, v∈(0,∞)v\in(0,\infty) and t∈[0,T]t\in[0,T], then we must have

|  |  |  |  |
| --- | --- | --- | --- |
|  | A′​(t)=0,\displaystyle A^{\prime}(t)=0, |  | (A.2) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | B′​(t)+12​A​(t)2+ci​A​(t)−bi​B​(t)+σ22​B​(t)2+ρ​σ​A​(t)​B​(t)=0,\displaystyle B^{\prime}(t)+\frac{1}{2}A(t)^{2}+c\_{i}A(t)-b\_{i}B(t)+\frac{\sigma^{2}}{2}B(t)^{2}+\rho\sigma A(t)B(t)=0, |  | (A.3) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | C′​(t)+r​A​(t)+a​B​(t)=0,\displaystyle C^{\prime}(t)+rA(t)+aB(t)=0, |  | (A.4) |

so we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(t)=i​p.A(t)=\mathrm{i}\mkern 1.0mup. |  | (A.5) |

Substituting equation ([A.5](https://arxiv.org/html/2512.05326v1#A1.E5 "In A.1 Proof of Theorem 2.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")) into equation ([A.3](https://arxiv.org/html/2512.05326v1#A1.E3 "In A.1 Proof of Theorem 2.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")) and simplifying, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | B′​(t)+12​σ2​B2​(t)−(bi−i​σ​ρ​p)​B​(t)−p2−2​i​ci​p2=0.B^{\prime}(t)+\frac{1}{2}\sigma^{2}B^{2}(t)-\left(b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p\right)B(t)-\frac{p^{2}-2\mathrm{i}\mkern 1.0muc\_{i}p}{2}=0. |  | (A.6) |

Equation ([A.6](https://arxiv.org/html/2512.05326v1#A1.E6 "In A.1 Proof of Theorem 2.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")), with boundary value B​(T)=i​qB(T)=\mathrm{i}\mkern 1.0muq, is Riccati equation with constant coefficients and has solution

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | B​(t)=\displaystyle B(t)= | i​γσ2​tan⁡(i​γ2​(T−t)+ϑ)+bi−i​σ​ρ​pσ2,\displaystyle\frac{\mathrm{i}\mkern 1.0mu\gamma}{\sigma^{2}}\tan\left(\frac{\mathrm{i}\mkern 1.0mu\gamma}{2}(T-t)+\vartheta\right)+\frac{b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p}{\sigma^{2}}, |  | (A.7) |

where ϑ=arctan⁡(i​λ/γ)\vartheta=\arctan\left({\mathrm{i}\mkern 1.0mu\lambda}/{\gamma}\right),
γ=σ2​(p2−2​i​ci​p)+(bi−i​σ​ρ​p)2\gamma=\sqrt{\sigma^{2}\left(p^{2}-2\mathrm{i}\mkern 1.0muc\_{i}p\right)+\left(b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p\right)^{2}}, and
λ=(bi−i​σ​ρ​p−i​σ2​q)\lambda=(b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p-\mathrm{i}\mkern 1.0mu\sigma^{2}q).
The solution of ([A.4](https://arxiv.org/html/2512.05326v1#A1.E4 "In A.1 Proof of Theorem 2.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")) with boundary C​(T)=0C(T)=0 can be obtained by integration. With τ=T−t\tau=T-t, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(t)=\displaystyle C(t)= | ∫tT(i​p​r+a​B​(s))​𝑑s=i​p​r​(T−t)+a​(bi−i​p​ρ​σ)σ2​(T−t)−2​aσ2​ln⁡cos⁡(i​γ2​(T−t)+ϑ)cos⁡(ϑ)\displaystyle\int\_{t}^{T}\left(\mathrm{i}\mkern 1.0mupr+aB(s)\right)ds=\mathrm{i}\mkern 1.0mupr(T-t)+\frac{a\left(b\_{i}-\mathrm{i}\mkern 1.0mup\rho\sigma\right)}{\sigma^{2}}(T-t)-\frac{2a}{\sigma^{2}}\ln\frac{\cos\left(\frac{\mathrm{i}\mkern 1.0mu\gamma}{2}(T-t)+\vartheta\right)}{\cos\left(\vartheta\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | i​p​r​τ+a​(bi−i​p​ρ​σ)σ2​τ−2​aσ2​ln⁡cos⁡(i​γ​τ2)​cos⁡(ϑ)−sin⁡(i​γ​τ2)​sin⁡(ϑ)cos⁡(ϑ)\displaystyle\mathrm{i}\mkern 1.0mupr\tau+\frac{a\left(b\_{i}-\mathrm{i}\mkern 1.0mup\rho\sigma\right)}{\sigma^{2}}\tau-\frac{2a}{\sigma^{2}}\ln\frac{\cos\left(\frac{\mathrm{i}\mkern 1.0mu\gamma\tau}{2}\right)\cos\left(\vartheta\right)-\sin\left(\frac{\mathrm{i}\mkern 1.0mu\gamma\tau}{2}\right)\sin\left(\vartheta\right)}{\cos\left(\vartheta\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | i​p​r​τ+a​(bi−i​p​ρ​σ)σ2​τ−2​aσ2​ln⁡(cos⁡(i​γ​τ2)−sin⁡(i​γ​τ2)​tan⁡(ϑ))\displaystyle\mathrm{i}\mkern 1.0mupr\tau+\frac{a\left(b\_{i}-\mathrm{i}\mkern 1.0mup\rho\sigma\right)}{\sigma^{2}}\tau-\frac{2a}{\sigma^{2}}\ln\left(\cos\left(\frac{\mathrm{i}\mkern 1.0mu\gamma\tau}{2}\right)-\sin\left(\frac{\mathrm{i}\mkern 1.0mu\gamma\tau}{2}\right)\tan\left(\vartheta\right)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | i​p​r​τ+a​(bi−i​p​ρ​σ)σ2​τ−2​aσ2​ln⁡(cosh⁡(γ​τ2)−i​sinh⁡(γ​τ2)​i​λγ)\displaystyle\mathrm{i}\mkern 1.0mupr\tau+\frac{a\left(b\_{i}-\mathrm{i}\mkern 1.0mup\rho\sigma\right)}{\sigma^{2}}\tau-\frac{2a}{\sigma^{2}}\ln\left(\cosh\left(\frac{\gamma\tau}{2}\right)-\mathrm{i}\mkern 1.0mu\sinh\left(\frac{\gamma\tau}{2}\right)\frac{\mathrm{i}\mkern 1.0mu\lambda}{\gamma}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | i​p​r​τ+a​(bi−i​p​ρ​σ)σ2​τ−2​aσ2​ln⁡(eγ​τ2+e−γ​τ22+λγ⋅eγ​τ2−e−γ​τ22)\displaystyle\mathrm{i}\mkern 1.0mupr\tau+\frac{a\left(b\_{i}-\mathrm{i}\mkern 1.0mup\rho\sigma\right)}{\sigma^{2}}\tau-\frac{2a}{\sigma^{2}}\ln\left(\frac{e^{\frac{\gamma\tau}{2}}+e^{-\frac{\gamma\tau}{2}}}{2}+\frac{\lambda}{\gamma}\cdot\frac{e^{\frac{\gamma\tau}{2}}-e^{-\frac{\gamma\tau}{2}}}{2}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | i​p​r​τ+a​(bi−i​p​ρ​σ)σ2​τ−2​aσ2​ln⁡e−γ​τ2​γ​(eγ​τ+1)+λ​(eγ​τ−1)2​γ\displaystyle\mathrm{i}\mkern 1.0mupr\tau+\frac{a\left(b\_{i}-\mathrm{i}\mkern 1.0mup\rho\sigma\right)}{\sigma^{2}}\tau-\frac{2a}{\sigma^{2}}\ln e^{-\frac{\gamma\tau}{2}}\frac{\gamma\left(e^{\gamma\tau}+1\right)+\lambda\left(e^{\gamma\tau}-1\right)}{2\gamma} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | i​p​r​τ+a​(bi−i​σ​ρ​p+γ)σ2​τ+2​aσ2​ln⁡2​γ(γ+λ)​eγ​τ+γ−λ.\displaystyle\mathrm{i}\mkern 1.0mupr\tau+\frac{a\left(b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p+\gamma\right)}{\sigma^{2}}\tau+\frac{2a}{\sigma^{2}}\ln\frac{2\gamma}{\left(\gamma+\lambda\right)e^{\gamma\tau}+\gamma-\lambda}. |  |

Equation ([A.7](https://arxiv.org/html/2512.05326v1#A1.E7 "In A.1 Proof of Theorem 2.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")) may be simplified further as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​(t)=\displaystyle B(t)= | i​γσ2​tan⁡(i​γ​τ2+ϑ)+bi−i​σ​ρ​pσ2=i​γσ2​(tan⁡(i​γ​τ2)+tan⁡(ϑ)1−tan⁡(i​γ​τ2)​tan⁡(ϑ))+bi−i​σ​ρ​pσ2\displaystyle\frac{\mathrm{i}\mkern 1.0mu\gamma}{\sigma^{2}}\tan\left(\frac{\mathrm{i}\mkern 1.0mu\gamma\tau}{2}+\vartheta\right)+\frac{b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p}{\sigma^{2}}=\frac{\mathrm{i}\mkern 1.0mu\gamma}{\sigma^{2}}\left(\frac{\tan\left(\frac{\mathrm{i}\mkern 1.0mu\gamma\tau}{2}\right)+\tan\left(\vartheta\right)}{1-\tan\left(\frac{\mathrm{i}\mkern 1.0mu\gamma\tau}{2}\right)\tan\left(\vartheta\right)}\right)+\frac{b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p}{\sigma^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | i​γσ2​(i​tanh⁡(γ​τ2)+i​λγ1−i​λγ​i​tanh⁡(γ​τ2))+bi−i​σ​ρ​pσ2=i​γσ2​(i​eγ​τ2−e−γ​τ2eγ​τ2+e−γ​τ2+i​λγ)/(1+λγ​eγ​τ2−e−γ​τ2eγ​τ2+e−γ​τ2)+bi−i​σ​ρ​pσ2\displaystyle\frac{\mathrm{i}\mkern 1.0mu\gamma}{\sigma^{2}}\left(\frac{\mathrm{i}\mkern 1.0mu\tanh\left(\frac{\gamma\tau}{2}\right)+\mathrm{i}\mkern 1.0mu\frac{\lambda}{\gamma}}{1-\mathrm{i}\mkern 1.0mu\frac{\lambda}{\gamma}\mathrm{i}\mkern 1.0mu\tanh\left(\frac{\gamma\tau}{2}\right)}\right)+\frac{b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p}{\sigma^{2}}=\frac{\mathrm{i}\mkern 1.0mu\gamma}{\sigma^{2}}\left({\mathrm{i}\mkern 1.0mu\frac{e^{\frac{\gamma\tau}{2}}-e^{-\frac{\gamma\tau}{2}}}{e^{\frac{\gamma\tau}{2}}+e^{-\frac{\gamma\tau}{2}}}+\mathrm{i}\mkern 1.0mu\frac{\lambda}{\gamma}}\right)\left/\left({1+\frac{\lambda}{\gamma}\frac{e^{\frac{\gamma\tau}{2}}-e^{-\frac{\gamma\tau}{2}}}{e^{\frac{\gamma\tau}{2}}+e^{-\frac{\gamma\tau}{2}}}}\right)\right.+\frac{b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p}{\sigma^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | −γσ2​(eγ​τ2−e−γ​τ2+λγ​(eγ​τ2+e−γ​τ2)eγ​τ2+e−γ​τ2+λγ​(eγ​τ2−e−γ​τ2))+bi−i​σ​ρ​pσ2=−γσ2​(γ​(eγ​τ−1)+λ​(eγ​τ+1)γ​(eγ​τ+1)+λ​(eγ​τ−1))+bi−i​σ​ρ​pσ2\displaystyle-\frac{\gamma}{\sigma^{2}}\left(\frac{e^{\frac{\gamma\tau}{2}}-e^{-\frac{\gamma\tau}{2}}+\frac{\lambda}{\gamma}\left(e^{\frac{\gamma\tau}{2}}+e^{-\frac{\gamma\tau}{2}}\right)}{e^{\frac{\gamma\tau}{2}}+e^{-\frac{\gamma\tau}{2}}+\frac{\lambda}{\gamma}\left(e^{\frac{\gamma\tau}{2}}-e^{-\frac{\gamma\tau}{2}}\right)}\right)+\frac{b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p}{\sigma^{2}}=-\frac{\gamma}{\sigma^{2}}\left(\frac{\gamma\left(e^{\gamma\tau}-1\right)+\lambda\left(e^{\gamma\tau}+1\right)}{\gamma\left(e^{\gamma\tau}+1\right)+\lambda\left(e^{\gamma\tau}-1\right)}\right)+\frac{b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p}{\sigma^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | −γσ2​((γ+λ)​eγ​τ+λ−γ(γ+λ)​eγ​τ+γ−λ)+bi−i​σ​ρ​pσ2=−γσ2​(1+2​(λ−γ)(γ+λ)​eγ​τ+γ−λ)+bi−i​σ​ρ​pσ2\displaystyle-\frac{\gamma}{\sigma^{2}}\left(\frac{\left(\gamma+\lambda\right)e^{\gamma\tau}+\lambda-\gamma}{\left(\gamma+\lambda\right)e^{\gamma\tau}+\gamma-\lambda}\right)+\frac{b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p}{\sigma^{2}}=-\frac{\gamma}{\sigma^{2}}\left(1+\frac{2\left(\lambda-\gamma\right)}{\left(\gamma+\lambda\right)e^{\gamma\tau}+\gamma-\lambda}\right)+\frac{b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p}{\sigma^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 2​γ​(γ−λ)σ2​((γ+λ)​eγ​τ+γ−λ)+bi−i​σ​ρ​p−γσ2.\displaystyle\frac{2\gamma\left(\gamma-\lambda\right)}{\sigma^{2}\left(\left(\gamma+\lambda\right)e^{\gamma\tau}+\gamma-\lambda\right)}+\frac{b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p-\gamma}{\sigma^{2}}. |  |

Denoting ζ~=2​γ/((γ+λ)​exp⁡(γ​τ)+γ−λ)\tilde{\zeta}=2\gamma/{\left((\gamma+\lambda)\exp{(\gamma\tau)}+\gamma-\lambda\right)}, we have that the characteristic function is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(p,q)=\displaystyle\psi(p,q)= | exp⁡(A​(t)​x+B​(t)​v+C​(t))\displaystyle\exp\left(A(t)x+B(t)v+C(t)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | exp⁡(i​p​x+(2​γ​(γ−λ)σ2​((γ+λ)​eγ​τ+γ−λ)+bi−i​σ​ρ​p−γσ2)​v+i​p​r​τ+a​(bi−i​σ​ρ​p+γ)σ2​τ+2​aσ2​ln⁡2​γ(γ+λ)​eγ​τ+γ−λ)\displaystyle\exp\left(\mathrm{i}\mkern 1.0mupx+\left(\tfrac{2\gamma\left(\gamma-\lambda\right)}{\sigma^{2}\left(\left(\gamma+\lambda\right)e^{\gamma\tau}+\gamma-\lambda\right)}+\tfrac{b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p-\gamma}{\sigma^{2}}\right)v+\mathrm{i}\mkern 1.0mupr\tau+\tfrac{a\left(b\_{i}-\mathrm{i}\mkern 1.0mu\sigma\rho p+\gamma\right)}{\sigma^{2}}\tau+\tfrac{2a}{\sigma^{2}}\ln\tfrac{2\gamma}{\left(\gamma+\lambda\right)e^{\gamma\tau}+\gamma-\lambda}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | exp⁡(i​p​(x+r​τ)+((γ−λ)​ζ~σ2+λ−γσ2+i​q)​v+λ+γσ2​a​τ+i​q​a​τ+2​aσ2​ln⁡ζ~)\displaystyle\exp\left(\mathrm{i}\mkern 1.0mup\left(x+r\tau\right)+\left(\frac{\left(\gamma-\lambda\right)\tilde{\zeta}}{\sigma^{2}}+\frac{\lambda-\gamma}{\sigma^{2}}+\mathrm{i}\mkern 1.0muq\right)v+\frac{\lambda+\gamma}{\sigma^{2}}a\tau+\mathrm{i}\mkern 1.0muqa\tau+\frac{2a}{\sigma^{2}}\ln\tilde{\zeta}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | exp⁡(i​p​(x+r​τ)+i​q​(v+a​τ)+γ−λσ2​(ζ~−1)​v+γ+λσ2​a​τ+2​aσ2​ln⁡(ζ~)).\displaystyle\exp\left(\mathrm{i}\mkern 1.0mup\left(x+r\tau\right)+\mathrm{i}\mkern 1.0muq\left(v+a\tau\right)+\frac{\gamma-\lambda}{\sigma^{2}}\left(\tilde{\zeta}-1\right)v+\frac{\gamma+\lambda}{\sigma^{2}}a\tau+\frac{2a}{\sigma^{2}}\ln(\tilde{\zeta})\right). |  |

The logarithm term, ln⁡(ζ~)\ln(\tilde{\zeta}), may have a discontinuity as pp increases. We can see that for p→∞p\rightarrow\infty, we have
Re​(γ)→∞\text{Re}(\gamma)\rightarrow\infty,
Im​(γ)→∞\text{Im}(\gamma)\rightarrow\infty,
and
ζ~→0\tilde{\zeta}\rightarrow 0.
Though the value of ζ~\tilde{\zeta} is bounded, the value of of ln⁡(ζ~)\ln(\tilde{\zeta}) will change very fast when ζ~\tilde{\zeta} approaches 0 and shifts phase eventually. To avoid the value of the logarithm term approaching either zero or infinity, we make the following change of variables:

|  |  |  |
| --- | --- | --- |
|  | ζ=2​γγ+λ+(γ−λ)​e−γ​τ;ζ~=ζ​e−γ​τ;ln⁡ζ~=−γ​τ+ln⁡ζ;and γ−λσ2​(ζ~−1)=γ+λσ2​(1−ζ).\zeta=\frac{2\gamma}{\gamma+\lambda+(\gamma-\lambda)e^{-\gamma\tau}};\quad\tilde{\zeta}=\zeta e^{-\gamma\tau};\quad\ln\tilde{\zeta}=-\gamma\tau+\ln\zeta;\quad\text{and }\quad\frac{\gamma-\lambda}{\sigma^{2}}(\tilde{\zeta}-1)=\frac{\gamma+\lambda}{\sigma^{2}}(1-\zeta). |  |

Therefore, our characteristic function is given as

|  |  |  |
| --- | --- | --- |
|  | ψ​(p,q)=exp⁡(i​p​(x+r​τ)+i​q​(v+a​τ)+γ+λσ2​(1−ζ)​v−γ−λσ2​a​τ+2​aσ2​ln⁡ζ).\psi(p,q)=\exp\left(\mathrm{i}\mkern 1.0mup\left(x+r\tau\right)+\mathrm{i}\mkern 1.0muq\left(v+a\tau\right)+\frac{\gamma+\lambda}{\sigma^{2}}\left(1-\zeta\right)v-\frac{\gamma-\lambda}{\sigma^{2}}a\tau+\frac{2a}{\sigma^{2}}\ln\zeta\right). |  |

This completes the derivation of the joint characteristic function as given in Theorem [2.1](https://arxiv.org/html/2512.05326v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model").
∎

### A.2 Proof of Proposition [3.1](https://arxiv.org/html/2512.05326v1#S3.Thmproposition1 "Proposition 3.1 (Asymptotic characteristic function). ‣ 3.1 Error analysis ‣ 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")

###### Proof.

We investigate the limiting behavior of the characteristic function given by ([2.1](https://arxiv.org/html/2512.05326v1#S2.Ex14 "2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")) and the parameters γ\gamma, λ\lambda and ζ\zeta as defined in equations ([2.11](https://arxiv.org/html/2512.05326v1#S2.E11 "In Theorem 2.1. ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model"))-([2.13](https://arxiv.org/html/2512.05326v1#S2.E13 "In Theorem 2.1. ‣ 2.1 Heston’s stochastic volatility model ‣ 2 Heston model with characteristic function ‣ Convolution-FFT for option pricing in the Heston model")). We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | limp→∞γp=\displaystyle\lim\limits\_{p\rightarrow\infty}\frac{\gamma}{p}= | σ​1−ρ2​sign⁡(p),\displaystyle\sigma\sqrt{1-\rho^{2}}\operatorname{sign}(p), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limp→∞λp=\displaystyle\lim\limits\_{p\rightarrow\infty}\frac{\lambda}{p}= | −σ​ρ​i, and\displaystyle-\sigma\rho\mathrm{i}\mkern 1.0mu,\mbox{ and} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limp→∞ζ=\displaystyle\lim\limits\_{p\rightarrow\infty}\zeta= | 2​1−ρ2​(1−ρ2+sign⁡(p)​ρ​i).\displaystyle 2\sqrt{1-\rho^{2}}\left(\sqrt{1-\rho^{2}}+\operatorname{sign}(p)\rho\mathrm{i}\mkern 1.0mu\right). |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | limp→∞ln⁡ζ=ln⁡(2​1−ρ2)+ln⁡(1−ρ2+sign⁡(p)​ρ​i).\lim\limits\_{p\rightarrow\infty}\ln\zeta=\ln\left(2\sqrt{1-\rho^{2}}\right)+\ln\left(\sqrt{1-\rho^{2}}+\operatorname{sign}(p)\rho\mathrm{i}\mkern 1.0mu\right). |  | (A.8) |

Further, note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limp→∞1p​γ+λσ2​(1−ζ)​v=\displaystyle\lim\limits\_{p\rightarrow\infty}\frac{1}{p}\frac{\gamma+\lambda}{\sigma^{2}}\left(1-\zeta\right)v= | limp→∞γ+λσ2​p​(1−2​γγ+λ+(γ−λ)​e−γ​τ)\displaystyle\lim\limits\_{p\rightarrow\infty}\frac{\gamma+\lambda}{\sigma^{2}p}\left(1-\frac{2\gamma}{\gamma+\lambda+(\gamma-\lambda)e^{-\gamma\tau}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =limp→∞γ+λσ2​p​(λ−γ+(γ−λ)​e−γ​τγ+λ+(γ−λ)​e−γ​τ)=limp→∞λ−γσ2​p\displaystyle=\lim\limits\_{p\rightarrow\infty}\frac{\gamma+\lambda}{\sigma^{2}p}\left(\frac{\lambda-\gamma+(\gamma-\lambda)e^{-\gamma\tau}}{\gamma+\lambda+(\gamma-\lambda)e^{-\gamma\tau}}\right)=\lim\limits\_{p\rightarrow\infty}\frac{\lambda-\gamma}{\sigma^{2}p} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−1−ρ2σ​v​sign⁡(p)−ρσ​v​i,\displaystyle=-\frac{\sqrt{1-\rho^{2}}}{\sigma}v\operatorname{sign}(p)-\frac{\rho}{\sigma}v\mathrm{i}\mkern 1.0mu, |  | (A.9) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | limp→∞1p​γ−λσ2​a​τ=1−ρ2σ​a​τ​sign⁡(p)−a​τσ​i.\displaystyle\lim\limits\_{p\rightarrow\infty}\frac{1}{p}\frac{\gamma-\lambda}{\sigma^{2}}a\tau=\frac{\sqrt{1-\rho^{2}}}{\sigma}a\tau\operatorname{sign}(p)-\frac{a\tau}{\sigma}\mathrm{i}\mkern 1.0mu. |  | (A.10) |

Let ϑ=arcsin⁡(ρ​sign⁡(p))\vartheta=\arcsin\left(\rho\operatorname{sign}(p)\right) and transform ([A.8](https://arxiv.org/html/2512.05326v1#A1.E8 "In A.2 Proof of Proposition 3.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | limp→∞ln⁡ζ​(p)=ln⁡(2​1−ρ2)+ϑ​i.\lim\limits\_{p\rightarrow\infty}\ln\zeta(p)=\ln\left(2\sqrt{1-\rho^{2}}\right)+\vartheta\mathrm{i}\mkern 1.0mu. |  | (A.11) |

Combining ([A.2](https://arxiv.org/html/2512.05326v1#A1.Ex25 "A.2 Proof of Proposition 3.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")), ([A.10](https://arxiv.org/html/2512.05326v1#A1.E10 "In A.2 Proof of Proposition 3.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")) and ([A.11](https://arxiv.org/html/2512.05326v1#A1.E11 "In A.2 Proof of Proposition 3.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")), we finalize the proof

|  |  |  |
| --- | --- | --- |
|  | limp→∞ψi​(p)≈A∞​ei​B∞​exp⁡(−1−ρ2σ​(v+a​τ)​|p|).\lim\limits\_{p\rightarrow\infty}\psi\_{i}(p)\approx A\_{\infty}e^{\mathrm{i}\mkern 1.0muB\_{\infty}}\exp\left(-\frac{\sqrt{1-\rho^{2}}}{\sigma}\left(v+a\tau\right)\left|p\right|\right). |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | A∞=\displaystyle A\_{\infty}= | (4​(1−ρ2))aσ2,\displaystyle\left(4\left(1-\rho^{2}\right)\right)^{\frac{a}{\sigma^{2}}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | B∞=\displaystyle B\_{\infty}= | 2​aσ2​arcsin⁡(ρ​sign⁡(p))−ρσ​(v+a​τ​sign⁡(p))​p.\displaystyle\frac{2a}{\sigma^{2}}\arcsin\left(\rho\operatorname{sign}(p)\right)-\frac{\rho}{\sigma}\left(v+a\tau\operatorname{sign}(p)\right)p. |  |

This completes the proof of Proposition [3.1](https://arxiv.org/html/2512.05326v1#S3.Thmproposition1 "Proposition 3.1 (Asymptotic characteristic function). ‣ 3.1 Error analysis ‣ 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model").
∎

### A.3 Proof of Theorem [3.1](https://arxiv.org/html/2512.05326v1#S3.Thmtheorem1 "Theorem 3.1 (Error of the convolution method). ‣ 3.1 Error analysis ‣ 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")

We next consider the truncation and discretization error bounds of the CFFT methods given in Theorem [3.1](https://arxiv.org/html/2512.05326v1#S3.Thmtheorem1 "Theorem 3.1 (Error of the convolution method). ‣ 3.1 Error analysis ‣ 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model").

###### Proof.

We see that

|  |  |  |
| --- | --- | --- |
|  | Ei​(x)=∫ℝf​(y)​hi​(x−y)​𝑑y,E\_{i}(x)=\int\_{\mathbb{R}}f(y)h\_{i}(x-y)dy, |  |

with f​(y)f(y) replaced by its Fourier expansion given in ([3.15](https://arxiv.org/html/2512.05326v1#S3.E15 "In 3.1 Error analysis ‣ 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pi​(x)=\displaystyle P\_{i}(x)= | ∫ℝ∑j=−∞∞Fj​e−i​j​2​π​yL​hi​(x−y)​d​y\displaystyle\int\_{\mathbb{R}}\sum\_{j=-\infty}^{\infty}F\_{j}e^{-\mathrm{i}\mkern 1.0muj\frac{2\pi y}{L}}h\_{i}(x-y)dy |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑j=−∞∞Fj​e−i​j​2​π​xL​∫ℝei​j​2​π​(x−y)L​hi​(x−y)​𝑑y\displaystyle\sum\_{j=-\infty}^{\infty}F\_{j}e^{-\mathrm{i}\mkern 1.0muj\frac{2\pi x}{L}}\int\_{\mathbb{R}}e^{\mathrm{i}\mkern 1.0muj\frac{2\pi(x-y)}{L}}h\_{i}(x-y)dy |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | ∑j=−∞∞Fj​e−i​j​2​π​xL​∫ℝei​j​2​π​yL​ϕi​(y)​𝑑y.\displaystyle\sum\_{j=-\infty}^{\infty}F\_{j}e^{-\mathrm{i}\mkern 1.0muj\frac{2\pi x}{L}}\int\_{\mathbb{R}}e^{\mathrm{i}\mkern 1.0muj\frac{2\pi y}{L}}\phi\_{i}(y)dy. |  | (A.12) |

Replace the integral in equation ([A.3](https://arxiv.org/html/2512.05326v1#A1.Ex31 "A.3 Proof of Theorem 3.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")) by the kernel function ([3.7](https://arxiv.org/html/2512.05326v1#S3.E7 "In 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pi​(x)=∑j=−∞∞Fj​e−i​j​2​π​xL​ψi​(2​π​jL).P\_{i}(x)=\sum\_{j=-\infty}^{\infty}F\_{j}e^{-\mathrm{i}\mkern 1.0muj\frac{2\pi x}{L}}\psi\_{i}\left(\frac{2\pi j}{L}\right). |  | (A.13) |

We truncate the infinite summation in equation ([A.13](https://arxiv.org/html/2512.05326v1#A1.E13 "In A.3 Proof of Theorem 3.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")) from −N2-\frac{N}{2} to N2−1\frac{N}{2}-1

|  |  |  |  |
| --- | --- | --- | --- |
|  | P˙i​(x)=∑j=−N2N2−1Fj​e−i​j​2​π​xL​ψi​(2​π​jL),\dot{P}\_{i}(x)=\sum\_{j=-\frac{N}{2}}^{\frac{N}{2}-1}F\_{j}e^{-\mathrm{i}\mkern 1.0muj\frac{2\pi x}{L}}\psi\_{i}\left(\frac{2\pi j}{L}\right), |  | (A.14) |

and denote the truncation error as ei,1e\_{i,1}

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ei,1|=\displaystyle\left|e\_{i,1}\right|= | |Pi​(x)−P˙i​(x)|=|∑j=−N2−1−∞Fj​e−i​j​2​π​xL​ψi​(2​π​jL)+∑j=N2∞Fj​e−i​j​2​π​xL​ψi​(2​π​jL)|≤∑|j|=N2∞|Fj|​|ψi​(2​π​jL)|.\displaystyle\left|P\_{i}(x)-\dot{P}\_{i}(x)\right|=\left|\sum\_{j=-\frac{N}{2}-1}^{-\infty}F\_{j}e^{-\mathrm{i}\mkern 1.0muj\frac{2\pi x}{L}}\psi\_{i}\left(\frac{2\pi j}{L}\right)+\sum\_{j=\frac{N}{2}}^{\infty}F\_{j}e^{-\mathrm{i}\mkern 1.0muj\frac{2\pi x}{L}}\psi\_{i}\left(\frac{2\pi j}{L}\right)\right|\leq\sum\_{\left|j\right|=\frac{N}{2}}^{\infty}\left|F\_{j}\right|\left|\psi\_{i}\left(\frac{2\pi j}{L}\right)\right|. |  |

By Proposition [3.1](https://arxiv.org/html/2512.05326v1#S3.Thmproposition1 "Proposition 3.1 (Asymptotic characteristic function). ‣ 3.1 Error analysis ‣ 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model"), there exists a positive constant ϵv,τ\epsilon\_{v,\tau} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ψi​(p)|≤ϵv,τ​A∞​exp⁡(−1−ρ2σ​(v+a​τ)​|p|), for all ​p.\left|\psi\_{i}(p)\right|\leq\epsilon\_{v,\tau}A\_{\infty}\exp\left(-\frac{\sqrt{1-\rho^{2}}}{\sigma}\left(v+a\tau\right)\left|p\right|\right),\text{ for all }p. |  | (A.15) |

Denote

|  |  |  |
| --- | --- | --- |
|  | D=1−ρ2σ​(v+a​τ).D=\frac{\sqrt{1-\rho^{2}}}{\sigma}\left(v+a\tau\right). |  |

Combining ([A.15](https://arxiv.org/html/2512.05326v1#A1.E15 "In A.3 Proof of Theorem 3.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")) and ([3.16](https://arxiv.org/html/2512.05326v1#S3.E16 "In 3.1 Error analysis ‣ 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ei,1|≤\displaystyle\left|e\_{i,1}\right|\leq | 2​ϵv,τ​f¯​A∞​∑j=N2∞exp⁡(−D​|2​π​jL|)≤ 2​ϵv,τ​f¯​A∞​L2​π​∫π​(N−2)L∞exp⁡(−D​u)​𝑑u\displaystyle\,2\epsilon\_{v,\tau}\bar{f}\,A\_{\infty}\sum\_{j=\frac{N}{2}}^{\infty}\exp\left({-D\left|\frac{2\pi j}{L}\right|}\right)\leq\,2\epsilon\_{v,\tau}\bar{f}\,A\_{\infty}\frac{L}{2\pi}\int\_{\frac{\pi(N-2)}{L}}^{\infty}\exp\left({-Du}\right)du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ϵv,τ​f¯​L​A∞π​exp⁡(−D​π​(N−2)/L)=ϵ1​exp⁡(−π​D​N/L),\displaystyle\frac{\epsilon\_{v,\tau}\bar{f}LA\_{\infty}}{\pi}\exp{\left({-D\pi(N-2)}/{L}\right)}=\epsilon\_{1}\exp{(-\pi DN/L)}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | ϵ1=L​A∞​e2​π​DLπ​D​ϵv,τ​f¯.\epsilon\_{1}=\frac{LA\_{\infty}e^{\frac{2\pi D}{L}}}{\pi D}\epsilon\_{v,\tau}\bar{f}. |  |

Next, we consider the discretization error arising from the DFT ([3.12](https://arxiv.org/html/2512.05326v1#S3.E12 "In 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model")) which is equivalent to the following calculation

|  |  |  |
| --- | --- | --- |
|  | P~i​(x)=∑j=−N2N2−1F~j​e−i​j​2​π​xL​ψi​(2​π​jL),\tilde{P}\_{i}(x)=\sum\_{j=-\frac{N}{2}}^{\frac{N}{2}-1}\tilde{F}\_{j}e^{-\mathrm{i}\mkern 1.0muj\frac{2\pi x}{L}}\psi\_{i}\left(\frac{2\pi j}{L}\right), |  |

by approximating the Fourier coefficients FjF\_{j} in ([A.14](https://arxiv.org/html/2512.05326v1#A1.E14 "In A.3 Proof of Theorem 3.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")) with

|  |  |  |
| --- | --- | --- |
|  | F~j=Δ​xL​∑k=0N−1f​(xk)​ei​j​2​π​xkL.\tilde{F}\_{j}=\frac{\Delta x}{L}\sum\_{k=0}^{N-1}f(x\_{k})e^{\mathrm{i}\mkern 1.0muj\frac{2\pi x\_{k}}{L}}. |  |

We denote the discretization error as ei,2e\_{i,2}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |ei,2|=\displaystyle\left|e\_{i,2}\right|= | |P˙i​(x)−P~i​(x)|≤∑j=−N2N2−1|Fj−F~j|​|ψj​(2​π​jL)|.\displaystyle\left|\dot{P}\_{i}(x)-\tilde{P}\_{i}(x)\right|\leq\sum\_{j=-\frac{N}{2}}^{\frac{N}{2}-1}\left|F\_{j}-\tilde{F}\_{j}\right|\left|\psi\_{j}\left(\frac{2\pi j}{L}\right)\right|. |  | (A.16) |

Assuming that the discretization error of |Fj−F~j|\left|F\_{j}-\tilde{F}\_{j}\right| is of O​(N−m)O\left(N^{-m}\right), we can bound it with a positive bounding constant ϵL\epsilon\_{L} depending only on LL

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Fj−F~j|≤ϵL​N−m.\left|F\_{j}-\tilde{F}\_{j}\right|\leq\epsilon\_{L}N^{-m}. |  | (A.17) |

It is easy to see that under the trapezoidal rule for wnw\_{n}, we can apply m≥2m\geq 2 in ([A.17](https://arxiv.org/html/2512.05326v1#A1.E17 "In A.3 Proof of Theorem 3.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")). Using the fact that uj=2​π​jLu\_{j}=\frac{2\pi j}{L} for j=−N2,⋯,N2−1j=-\frac{N}{2},\cdots,\frac{N}{2}-1, we finalize the approximation in ([A.16](https://arxiv.org/html/2512.05326v1#A1.E16 "In A.3 Proof of Theorem 3.1 ‣ Appendix A Appendix ‣ Convolution-FFT for option pricing in the Heston model")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ei,2|≤\displaystyle\left|e\_{i,2}\right|\leq | ∑j=−N2N2−1|Fj−F~j|​|ψj​(2​π​jL)|≤ϵL​ϵv,τ​A∞​N−m​∑j=−N2N2−1exp⁡(−D​|2​π​jL|)\displaystyle\sum\_{j=-\frac{N}{2}}^{\frac{N}{2}-1}\left|F\_{j}-\tilde{F}\_{j}\right|\left|\psi\_{j}\left(\frac{2\pi j}{L}\right)\right|\leq\,\epsilon\_{L}\epsilon\_{v,\tau}A\_{\infty}N^{-m}\sum\_{j=-\frac{N}{2}}^{\frac{N}{2}-1}\exp\left(-D\left|\frac{2\pi j}{L}\right|\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ϵL​ϵv,τ​A∞​N−m​L2​π​∫−N​πLN​πLexp⁡(−D​|u|)​𝑑u≤ϵL​ϵv,τ​L​A∞​N−mπ​∫0∞exp⁡(−D​u)​𝑑u\displaystyle\,\epsilon\_{L}\epsilon\_{v,\tau}A\_{\infty}N^{-m}\frac{L}{2\pi}\int\_{-\frac{N\pi}{L}}^{\frac{N\pi}{L}}\exp\left(-D\left|u\right|\right)du\leq\frac{\epsilon\_{L}\epsilon\_{v,\tau}LA\_{\infty}N^{-m}}{\pi}\int\_{0}^{\infty}\exp\left(-Du\right)du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ϵL​ϵv,τ​L​A∞​N−mπ​D=ϵ2​N−m,\displaystyle\frac{\epsilon\_{L}\epsilon\_{v,\tau}LA\_{\infty}N^{-m}}{\pi D}=\epsilon\_{2}N^{-m}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | ϵ2=ϵL​ϵv,τ.L​A∞π​D\epsilon\_{2}=\frac{\epsilon\_{L}\epsilon\_{v,\tau}.LA\_{\infty}}{\pi D} |  |

Therefore, the absolute error of the approximation of PiP\_{i} can be summarized as

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ei|=\displaystyle\left|e\_{i}\right|= | |Pi​(x)−P~i​(x)|≤|Pi​(x)−P˙i​(x)|+|P˙i​(x)−P~i​(x)|\displaystyle\left|P\_{i}(x)-\tilde{P}\_{i}(x)\right|\leq\left|P\_{i}(x)-\dot{P}\_{i}(x)\right|+\left|\dot{P}\_{i}(x)-\tilde{P}\_{i}(x)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | |ei,1|+|ei,2|≤ϵ1​exp⁡(−π​D​N/L)+ϵ2​N−m,\displaystyle\left|e\_{i,1}\right|+\left|e\_{i,2}\right|\leq\epsilon\_{1}\exp{\left(-\pi DN/L\right)}+\epsilon\_{2}N^{-m}, |  |

where the first component gives the upper bound of the truncation error and the second component gives the upper bound of the discretization error. This completes the proof of Theorem [3.1](https://arxiv.org/html/2512.05326v1#S3.Thmtheorem1 "Theorem 3.1 (Error of the convolution method). ‣ 3.1 Error analysis ‣ 3 Convolution-FFT method ‣ Convolution-FFT for option pricing in the Heston model").
∎