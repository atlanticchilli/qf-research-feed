---
authors:
- Jutta G. Kurth
- Jean-Philippe Bouchaud
doc_id: arxiv:2511.13277v1
family_id: arxiv:2511.13277
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Stationary Distributions of the Mode-switching Chiarella Model
url_abs: http://arxiv.org/abs/2511.13277v1
url_html: https://arxiv.org/html/2511.13277v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jutta G. Kurth
CFM Chair of Econophysics and Complex Systems, École polytechnique, 91128 Palaiseau Cedex, France
LadHyX UMR CNRS 7646, École polytechnique, 91128 Palaiseau Cedex, France
  
Jean-Philippe Bouchaud
Capital Fund Management, 23 Rue de l’Université, 75007 Paris, France
CFM Chair of Econophysics and Complex Systems, École polytechnique, 91128 Palaiseau Cedex, France
Académie des Sciences, 23 Quai de Conti, 75006 Paris, France

(November 17, 2025)

###### Abstract

We derive the stationary distribution in various regimes of the extended Chiarella model of financial markets. This model is a stochastic nonlinear dynamical system that encompasses dynamical competition between a (saturating) trending and a mean-reverting component. We find the so-called mispricing distribution and the trend distribution to be unimodal Gaussians in the small noise, small feedback limit. Slow trends yield Gaussian-cosh mispricing distributions that allow for a P-bifurcation: unimodality occurs when mean-reversion is fast, bimodality when it is slow. The critical point of this bifurcation is established and refutes previous ad-hoc reports and differs from the bifurcation condition of the dynamical system itself. For fast, weakly coupled trends, deploying the Furutsu-Novikov theorem reveals that the result is again unimodal Gaussian. For the same case with higher coupling we disprove another claim from the literature: bimodal trend distributions do not generally imply bimodal mispricing distributions. The latter becomes bimodal only for stronger trend feedback. The exact solution in this last regime remains unfortunately beyond our proficiency.

Chiarella model, bimodality, multimodality, stationary distribution, Fokker-Planck, mispricing, trend, momentum, value

## I Introduction

The Chiarella model is a nonlinear, stochastic dynamical system encompassing both negative (mean-reversion) and positive (trend following) feedback loops chiarella1992dynamics. It was introduced in the context of financial markets to describe the dynamical interplay between value investors and trend followers. It is indeed empirically well established that (normalised) price increments, a.k.a. returns, are positively auto-correlated on short to medium time scales (weeks up to several months) – observable as financial bubbles or trends – while they are negatively auto-correlated on longer times scales (months to few years) – observable as price mean reversion or corrections – see e.g. the discussion and references in bouchaud2017black; majewski2020co.

The model was later extended to allow for a time dependent fundamental value, which is the dynamic mean-reversion level around which the price is anchored. This level is modeled as a drift-diffusion process, which may be regarded as the fair or rationally justifiable price according to, e.g., company fundamentals in the case of stocks, or other economic indicators for other asset classes, such as indices, bonds, or derivatives majewski2020co. Such a fundamental value only changes because of unpredictable news or “shocks”. Devotees of the Efficient Market Hypothesis (EMH) believe that prices usually reflect all publicly available information, and that this information is instantaneously digested by the capital markets, suggesting that price and fundamental value should usually be in very close proximity. If this were true, returns should be serially uncorrelated and not exhibit the complex auto-correlation structures mentioned above, which, as many believe, heavily damage the credibility of the EMH for all major asset classes.

In a very recent paper, we amended some analytical shortcomings of the modified Chiarella model proposed in majewski2020co. In particular, we allowed for an arbitrary time-dependent drift for the value process kurth2025revisiting. The model was deployed and calibrated on individual assets’ (log-)prices belonging to four different asset classes. What all these variations around the initial Chiarella model have in common is the existence of two distinct dynamical behaviours (in the absence of noise):

1. 1.

   Attraction/convergence of price towards fundamental value;
2. 2.

   Oscillation of price around the fundamental value.

It is common belief that in the presence of noise the distribution of mispricings (i.e. the difference between price and value) is unimodal in case 1 and bimodal in case 2, when the price stochastically quasi-oscillates around the fundamental value chiarella2011stoch\_bif; majewski2020co; chiarella2008stochastic\_bifurc. This means that the phenomenological P-bifurcation condition – dictating uni- vs. bimodality – should coincide with the bifurcation condition predicting the transition from convergence to oscillation. While this has been argued in chiarella2011stoch\_bif and is correct in some limiting cases, the present paper disproves the result in general and provides the correct stationary mispricing distributions in many possible scenarios. The dynamical mechanisms that lead to either uni- or bimodality are clearly established.

Several extensions to the Chiarella model and other financial agent-based models have been discussed; see, e.g., majewski2020co; Goldman1980; lux1998; lux1999scaling and references therein. A first numerical study of the stationary measure in the Chiarella model was carried out in chiarella2008stochastic\_bifurc and later in chiarella2011stoch\_bif.

This paper is organised as follows: Sec. [II](https://arxiv.org/html/2511.13277v1#S2 "II A Generalised Chiarella Model ‣ Stationary Distributions of the Mode-switching Chiarella Model") introduces the Chiarella model formally and presents the crucial analytical results that are known about it. The heart of this work – the stationary distributions of the Chiarella model in most limiting cases – is in Secs. [III](https://arxiv.org/html/2511.13277v1#S3 "III The linear regime 𝛾→0 ‣ Stationary Distributions of the Mode-switching Chiarella Model"), [IV](https://arxiv.org/html/2511.13277v1#S4 "IV Slow Trends: the 𝜅≫𝛼 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model") and [V](https://arxiv.org/html/2511.13277v1#S5 "V Fast Trends: the 𝛼≫𝜅 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model"). Sec. [VI](https://arxiv.org/html/2511.13277v1#S6 "VI Conclusion ‣ Stationary Distributions of the Mode-switching Chiarella Model") summarises the results and concludes the main part of this paper, while additional derivations and proofs are given in Appendices.

## II A Generalised Chiarella Model

The Chiarella model is a stochastic dynamical system defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | dPt\displaystyle\differential P\_{t} | =κ​(Vt−Pt)​dt+β​tanh⁡(γ​Mt)​dt+gt​dt+σN​dWtN\displaystyle=\kappa(V\_{t}-P\_{t})\differential t+\beta\tanh(\gamma M\_{t})\differential t+g\_{t}\differential t+\sigma\_{N}\differential W\_{t}^{N} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dMt\displaystyle\differential M\_{t} | =−α​Mt​dt+α​(dPt−gt​dt)\displaystyle=-\alpha M\_{t}\differential t+\alpha(\differential P\_{t}-g\_{t}\differential t) |  | (1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | dVt\displaystyle\differential V\_{t} | =gt​dt+σV​dWtV,\displaystyle=g\_{t}\differential t+\sigma\_{V}\differential W\_{t}^{V}, |  |

where α\alpha, κ\kappa, β\beta, γ\gamma, σN/V\sigma\_{N/V} are all fixed positive parameters and WtN/VW^{N/V}\_{t} are standard Brownian Motions.

In the original context of the Chiarella model, PP is the (log-)price of a financial asset, MM is the trend signal, which is an exponential moving average of past drift-adjusted (log-) price increments, and VV is the fundamental value of the asset, modeled as a drift-diffusion process with time-dependent drift gg. However, this model may be understood as a general dynamical system exhibiting a dynamical interplay or competition between a mean-reverting force acting on PP, driving it towards VV through κ​(Vt−Pt)\kappa(V\_{t}-P\_{t}), which is an Ornstein-Uhlenbeck (OU) component with possibly time-dependent mean-reversion level VV, and a positive feedback term, β​tanh⁡(γ​M)\beta\tanh(\gamma M), accounting for the trending that gives rise to temporary, larger deviations of PP from VV but that are bounded to prevent divergence or run-aways.

In order to simplify the dynamical study of the system of Eqs.([II](https://arxiv.org/html/2511.13277v1#S2.Ex1 "II A Generalised Chiarella Model ‣ Stationary Distributions of the Mode-switching Chiarella Model")), the model dimensionality is reduced by one by considering the mispricing amplitude δ:=P−V\delta:=P-V instead of the two quantities separately without loss of generality. The model then reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | dδt\displaystyle\differential\delta\_{t} | =−κ​δt​dt+β​tanh⁡(γ​Mt)​dt+σN​dWtN−σV​dWtV\displaystyle=-\kappa\delta\_{t}\,\differential t+\beta\tanh(\gamma M\_{t})\,\differential t+\sigma\_{N}\differential W^{\textup{N}}\_{t}-\sigma\_{V}\differential W^{\textup{V}}\_{t} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dMt\displaystyle\differential M\_{t} | =−α​Mt​dt+α​(dδt+σV​dWtV).\displaystyle=-\alpha M\_{t}\differential t+\alpha(\differential\delta\_{t}+\sigma\_{V}\differential W^{\textup{V}}\_{t}). |  | (2) |

Note that since δ\delta is dimensionless, one has [t]=[γ]=[T][t]=[\gamma]=[T] and [α]=[κ]=[β]=[σ2]=[M]=[T]−1[\alpha]=[\kappa]=[\beta]=[\sigma^{2}]=[M]=[T]^{-1}.

A linear stability analysis of the deterministic counterpart (σN=σV=0\sigma\_{N}=\sigma\_{V}=0) of system ([II](https://arxiv.org/html/2511.13277v1#S2.Ex3 "II A Generalised Chiarella Model ‣ Stationary Distributions of the Mode-switching Chiarella Model")) reveals that it encompasses two different dynamical phases: the system undergoes a supercritical Hopf-bifurcation, in which the loss of stability of a formerly stable fix point located at (δ⋆,M⋆)=(0, 0)(\delta^{\star},\,M^{\star})=(0,\,0) when α​(1−β​γ)+κ>0\alpha(1-\beta\gamma)+\kappa>0 coincides with the emergence of a stable limit cycle in the δ\delta-MM-plane when α​(1−β​γ)+κ<0\alpha(1-\beta\gamma)+\kappa<0. This means that the deterministic PP no longer converges to the deterministic VV but moves around it periodically kurth2025revisiting.
Note that both limt→∞​𝔼​[δ]=0\underset{{t\to\infty}}{\lim}\mathbb{E}[\delta]=0 and limt→∞​𝔼​[M]=0\underset{{t\to\infty}}{\lim}\mathbb{E}[M]=0 whenever a stationary distribution p​(δ,M)p(\delta,M) exists, since both variables obey mean-reversion forces pulling them towards zero, the hyperbolic tangent is symmetric around zero and the noises are unbiased. This can also be seen by considering that the trajectories are either spiraling into the (stable) fixed point (δ⋆,M⋆)=(0, 0)(\delta^{\star},\,M^{\star})=(0,\,0) or oscillating around it.

In the following sections, the stationary distributions of the system of Eqs. ([II](https://arxiv.org/html/2511.13277v1#S2.Ex3 "II A Generalised Chiarella Model ‣ Stationary Distributions of the Mode-switching Chiarella Model")) will be derived in different parameter limits using different Fokker-Planck equation (FPE) ansätze.

## III The linear regime γ→0\gamma\to 0

In the limit where γ→0\gamma\to 0, the hyperbolic tangent may be linearised, corresponding to its first-order Taylor expansion. The region of validity of such an expansion will be determined a posteriori as γ​σM≪1\gamma\sigma\_{M}\ll 1, where σM\sigma\_{M} is given by Eq. ([11](https://arxiv.org/html/2511.13277v1#S3.E11 "In III The linear regime 𝛾→0 ‣ Stationary Distributions of the Mode-switching Chiarella Model")) below.

In matrix-form and defining 𝐱t:=(δt,Mt)T\mathbf{x}\_{t}:=(\delta\_{t},M\_{t})^{\textup{T}} and d𝐖t:=(dWtN,dWtV)T\differential\mathbf{W}\_{t}:=(\differential W^{\textup{N}}\_{t},\,\differential W^{\textup{V}}\_{t})^{\textup{T}}, the dynamics reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | d𝐱t=𝐀𝐱t​dt+𝐁​d𝐖t,\differential\mathbf{x}\_{t}=\mathbf{A}\mathbf{x}\_{t}\differential t+\mathbf{B}\,\differential\mathbf{W}\_{t}, |  | (3) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐀=(−κβ​γ−α​κα​(β​γ−1))\mathbf{A}=\begin{pmatrix}-\kappa&\beta\gamma\\ -\alpha\kappa&\alpha(\beta\gamma-1)\end{pmatrix} |  | (4) |

is the drift matrix of the linearised system and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐃=𝐁𝐁T=(σ2α​σN2α​σN2α2​σN2)​with​𝐁=(σN−σVα​σN0)\mathbf{D}=\mathbf{B}\mathbf{B}^{\textup{T}}=\begin{pmatrix}\sigma^{2}&\alpha\sigma\_{N}^{2}\\ \alpha\sigma\_{N}^{2}&\alpha^{2}\sigma\_{N}^{2}\end{pmatrix}\,\,\text{with}\,\,\,\mathbf{B}=\begin{pmatrix}\sigma\_{N}&-\sigma\_{V}\\ \alpha\sigma\_{N}&0\end{pmatrix} |  | (5) |

is the diffusion matrix with σ=σN2+σV2\sigma=\sqrt{\sigma\_{N}^{2}+\sigma\_{V}^{2}}.

The evolution of the joint probability density p​(δ,M,t)p(\delta,M,t) in time tt and the two space variables δ\delta and MM for such an Ito-process is given by its corresponding FPE. The stationary distribution p​(δ,M)p(\delta,M), for which ∂p∂t=0\frac{\partial p}{\partial t}=0, is defined via the stationary FPE,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=−∂∂δ​[(−κ​δ+β​γ​M)​p]−α​∂∂M​[(−M−κ​δ+β​γ​M)​p]+σ22​∂2p∂δ2+α​σN2​∂2p∂δ​∂M+α2​σN22​∂2p∂M2,0=-\frac{\partial}{\partial\delta}\left[(-\kappa\delta+\beta\gamma M)p\right]-\alpha\frac{\partial}{\partial M}\left[(-M-\kappa\delta+\beta\gamma M)p\right]\\ +\frac{\sigma^{2}}{2}\frac{\partial^{2}p}{\partial\delta^{2}}+\alpha\sigma\_{N}^{2}\frac{\partial^{2}p}{\partial\delta\partial M}+\frac{\alpha^{2}\sigma\_{N}^{2}}{2}\frac{\partial^{2}p}{\partial M^{2}}, |  | (6) |

where the left hand side of the equation is the time derivative equating zero.

Since the dynamical system is linear and its noise additive, the solution to this FPE is a (bivariate) Gaussian distribution,

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(δ,M)=12​π​|𝚺|​exp⁡(−12​𝐱T​𝚺−1​𝐱),p(\delta,M)=\frac{1}{2\pi\sqrt{|\mathbf{\Sigma}|}}\exp\left(-\frac{1}{2}\mathbf{x}^{T}\mathbf{\Sigma}^{-1}\mathbf{x}\right), |  | (7) |

where the covariance matrix 𝚺\mathbf{\Sigma} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺=(σδ2ρ​σδ​σMρ​σδ​σMσM2);\mathbf{\Sigma}=\begin{pmatrix}\sigma\_{\delta}^{2}&\rho\sigma\_{\delta}\sigma\_{M}\\ \rho\sigma\_{\delta}\sigma\_{M}&\sigma\_{M}^{2}\end{pmatrix}; |  | (8) |

σδ2\sigma\_{\delta}^{2} and σM2\sigma\_{M}^{2} are the variances of δ\delta and MM and ρ\rho is their correlation coefficient. The stationary distribution p​(δ,M)p(\delta,M) is centered in zero because both δ\delta and MM have vanishing mean in the stationary limit as discussed in Sec. [II](https://arxiv.org/html/2511.13277v1#S2 "II A Generalised Chiarella Model ‣ Stationary Distributions of the Mode-switching Chiarella Model").

The covariance matrix 𝚺\mathbf{\Sigma} in the stationary limit can be determined via the Lyapunov equation vankampen1992stochastic

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐀​𝚺+𝚺​𝐀T+𝐃=0.\mathbf{A}\mathbf{\Sigma}+\mathbf{\Sigma}\mathbf{A}^{\textup{T}}+\mathbf{D}=0. |  | (9) |

The solution to this linear system of equations yields the components of 𝚺\mathbf{\Sigma} (see also Appendix [A](https://arxiv.org/html/2511.13277v1#A1 "Appendix A Proof of the Stationary Distribution in the small-𝛽⁢𝛾-limit ‣ Stationary Distributions of the Mode-switching Chiarella Model")):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | σδ2=(κ+α​(β​γ−1)2)​σ2+α​β​γ​(2−β​γ)​σN22​κ​(α​(1−β​γ)+κ),\displaystyle\sigma\_{\delta}^{2}=\frac{(\kappa+\alpha(\beta\gamma-1)^{2})\sigma^{2}+\alpha\beta\gamma(2-\beta\gamma)\sigma\_{N}^{2}}{2\kappa(\alpha(1-\beta\gamma)+\kappa)}, |  | (10) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | σM2=α​(κ​σ2+(α−κ)​σN2)2​(α​(1−β​γ)+κ),\displaystyle\sigma\_{M}^{2}=\frac{\alpha(\kappa\sigma^{2}+(\alpha-\kappa)\sigma\_{N}^{2})}{2(\alpha(1-\beta\gamma)+\kappa)}, |  | (11) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ=α​κ​((β​γ−1)​σ2+(2−β​γ)​σN2)[(α​(β​γ−1)2+κ)​σ2+α​β​γ​(2−β​γ)​σN2]​[κ​σ2+(α−κ)​σN2].\rho=\frac{\sqrt{\alpha\kappa}((\beta\gamma-1)\sigma^{2}+(2-\beta\gamma)\sigma\_{N}^{2})}{\sqrt{[(\alpha(\beta\gamma-1)^{2}+\kappa)\sigma^{2}+\alpha\beta\gamma(2-\beta\gamma)\sigma\_{N}^{2}][\kappa\sigma^{2}+(\alpha-\kappa)\sigma\_{N}^{2}]}}. |  | (12) |

𝚺\mathbf{\Sigma} is positive semi-definite when κ>α​(β​γ−1)\kappa>\alpha(\beta\gamma-1), which is the bifurcation condition in the deterministic system (comp. Sec. [II](https://arxiv.org/html/2511.13277v1#S2 "II A Generalised Chiarella Model ‣ Stationary Distributions of the Mode-switching Chiarella Model")). This is always true in the considered limit. If it was not true, the drift matrix 𝐀\mathbf{A} would have positive eigenvalues, i.e. the system would diverge and no stationary distribution would exist.
From the joint probability distribution p​(δ,M)p(\delta,M), the mispricing distribution p​(δ)p(\delta) can be obtained through marginalisation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(δ)=∫−∞∞p​(δ,M)​dM=12​π​σδ2​e−δ22​σδ2,\displaystyle p(\delta)=\int\_{-\infty}^{\infty}p(\delta,M)\,\mathrm{d}M=\frac{1}{\sqrt{2\pi\sigma\_{\delta}^{2}}}\mathrm{e}^{-\frac{\delta^{2}}{2\sigma\_{\delta}^{2}}}, |  | (13) |

such that in this limit the mispricing distribution is Gaussian and thus unimodal. The stationary distribution of the trend signal MM is Gaussian, too, and can be obtained analogously. As anticipated above, these results hold provided the condition γ​σM≪1\gamma\sigma\_{M}\ll 1 is satisfied. For α≫κ\alpha\gg\kappa, this condition simplifies to

|  |  |  |
| --- | --- | --- |
|  | γ2​α​σN22​(1−β​γ)≪1,\frac{\gamma^{2}\alpha\sigma\_{N}^{2}}{2(1-\beta\gamma)}\ll 1, |  |

which breaks down as β​γ→1\beta\gamma\to 1. As we shall see later, this is indeed the condition for bimodality when α≫κ\alpha\gg\kappa.

The numerical confirmation of this result is provided in Fig. [1](https://arxiv.org/html/2511.13277v1#S3.F1 "Figure 1 ‣ III The linear regime 𝛾→0 ‣ Stationary Distributions of the Mode-switching Chiarella Model"), which shows the numerically obtained distribution p​(δ)p(\delta) (grey histogram) alongside the analytically derived distribution (coloured curves) for four orders of magnitude of γ\gamma. The stochastic integration (as well as all subsequent ones) was performed using the Euler-Maruyama scheme.

![Refer to caption](x1.png)


Figure 1: Grey: Numerical histograms of the stationary distribution in the case γ\gamma small. Simulation parameters are (κ,β,α,σN,σV)=(0.1, 0.2, 0.2, 0.2, 0.1)(\kappa,\,\beta,\,\alpha,\,\sigma\_{N},\,\sigma\_{V})=(0.1,\,0.2,\,0.2,\,0.2,\,0.1) and γ\gamma as detailed in the plot. T=γ×109T=\gamma\times 10^{9}, dt=γ/2t=\gamma/2 and g=0g=0. Coloured: Corresponding analytical stationary distributions p​(δ)p(\delta) according to Eq.([13](https://arxiv.org/html/2511.13277v1#S3.E13 "In III The linear regime 𝛾→0 ‣ Stationary Distributions of the Mode-switching Chiarella Model")). The distributions with γ>10−4\gamma>10^{-4} are shifted by multiples of 1 on the abscissa and of 0.5 on the ordinate.

We now turn to two solvable limits, where either the dynamics of δ\delta is much faster than that of MM (κ≫α\kappa\gg\alpha), or vice-versa.

## IV Slow Trends: the κ≫α\kappa\gg\alpha Limit

A change of variables x=δx=\delta and y=M−α​δy=M-\alpha\delta (comp. Appendix [B](https://arxiv.org/html/2511.13277v1#A2 "Appendix B Change of Variables ‣ Stationary Distributions of the Mode-switching Chiarella Model")) yields the following rephrasing of Eqs. ([II](https://arxiv.org/html/2511.13277v1#S2.Ex3 "II A Generalised Chiarella Model ‣ Stationary Distributions of the Mode-switching Chiarella Model")) (as before: σ2=σN2+σV2\sigma^{2}={\sigma\_{N}^{2}+\sigma\_{V}^{2}}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | dx\displaystyle\differential x | =−κ​x​dt+β​tanh⁡(γ​(y+α​x))​dt+σ​dWt\displaystyle=-\kappa x\,\differential t+\beta\tanh(\gamma(y+\alpha x))\,\differential t+\sigma\,\differential W\_{t} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dy\displaystyle\differential y | =−α​y​dt+α2​dx+α​σV​dWtV.\displaystyle=-\alpha y\,\differential t+\alpha^{2}\,\differential x+\alpha\sigma\_{V}\,\differential W\_{t}^{V}. |  | (14) |

Since xx is much faster than yy when α≪κ\alpha\ll\kappa, one can approximate yy as an OU-process, whose stationary distribution is known to be Gaussian, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(y)=12​π​Var​[y]​e−y22​V​a​r​[y],p(y)=\frac{1}{\sqrt{2\pi\mathrm{Var}[y]}}\mathrm{e}^{-\frac{y^{2}}{2\mathrm{Var}[y]}}, |  | (15) |

with, to first order in α\alpha, Var​[y]≈α2​σV2\mathrm{Var}[y]\approx\frac{\alpha}{2}\sigma\_{V}^{2}; the exact Var​[y]\mathrm{Var}[y] will cancel out from the expression of p​(x)p(x).

The conditional FPE of the dynamics of xx given yy reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂p​(x|y)∂t=\displaystyle\frac{\partial p(x|y)}{\partial t}= | −∂∂x​([−κ​x+β​tanh⁡(γ​(y+α​x))]​p​(x|y))\displaystyle-\frac{\partial}{\partial x}\big([-\kappa x+\beta\tanh(\gamma(y+\alpha x))]p(x|y)\big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +σ22​∂2∂x2​p​(x|y).\displaystyle+\frac{\sigma^{2}}{2}\frac{\partial^{2}}{\partial x^{2}}p(x|y). |  | (16) |

#### IV.0.1 The quasi-static equilibrium

In the case where xx evolves much faster than yy, a quasi-static approximation can be assumed, whereby the standard Maxwell-Boltzmann equilibrium is reached before yy has had time to vary much, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(x|y)=1A​(y)​e−κ​x2σ2​coshn⁡(γ​(α​x+y)),p(x|y)=\frac{1}{A(y)}\mathrm{e}^{-\frac{\kappa x^{2}}{\sigma^{2}}}\cosh^{n}(\gamma(\alpha x+y)), |  | (17) |

with n:=2​βα​γ​σ2n:={\frac{2\beta}{\alpha\gamma\sigma^{2}}} and the normalisation function A​(y)A(y) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(y)=∫−∞∞e−1σ2​κ​x2​coshn⁡(γ​(α​x+y))​dxA(y)=\int\_{-\infty}^{\infty}\mathrm{e}^{-\frac{1}{\sigma^{2}}\kappa x^{2}}\cosh^{n}(\gamma(\alpha x+y))\,\differential x |  | (18) |

This integral can only be calculated explicitly for integer exponents n∈ℕn\in\mathbb{N}. In this case, and defining an ϵn\epsilon\_{n} that is zero when nn is even and one when nn is odd, one finds using the Binomial Theorem that

|  |  |  |  |
| --- | --- | --- | --- |
|  | A(y)=σ2​πκ12n−1[(nn−ϵn2)⋅{12n​ evencosh⁡(γ​y)⋅e(α​γ​σ)24​κn​ odd+∑j=1⌊n/2⌋(nn−ϵn2−j)cosh(γ(2j+ϵn)y)e(α​γ​σ)24​κ​(2​j+ϵn)2];A(y)=\sqrt{\frac{\sigma^{2}\pi}{\kappa}}\frac{1}{2^{n-1}}\Bigg[\binom{n}{\frac{n-\epsilon\_{n}}{2}}\cdot\begin{cases}\frac{1}{2}&n\text{ even}\\ \cosh(\gamma y)\cdot\mathrm{e}^{\frac{(\alpha\gamma\sigma)^{2}}{4\kappa}}&n\text{ odd}\end{cases}\\ +\sum\_{j=1}^{\lfloor n/2\rfloor}\binom{n}{\frac{n-\epsilon\_{n}}{2}-j}\cosh\left(\gamma(2j+\epsilon\_{n})y\right)\mathrm{e}^{\frac{(\alpha\gamma\sigma)^{2}}{4\kappa}(2j+\epsilon\_{n})^{2}}\Bigg]; |  | (19) |

see also Appendix [C.1](https://arxiv.org/html/2511.13277v1#A3.SS1 "C.1 Normalisation Function 𝐴⁢(𝑦) ‣ Appendix C Additional Results in the limit 𝛼≪𝜅 ‣ Stationary Distributions of the Mode-switching Chiarella Model").
Knowing A​(y)A(y), the stationary distribution p​(x)p(x) can in principle be calculated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(x)=∫−∞∞p​(x|y)​p​(y)​dy;p(x)=\int\_{-\infty}^{\infty}p(x|y)p(y)\,\differential y; |  | (20) |

but the solution to this integral is not known for integer exponents n>1n>1 of the hyperbolic cosine.
The integral can however be solved when γ\gamma is sufficiently large.

![Refer to caption](x2.png)


Figure 2: Same as Fig. [1](https://arxiv.org/html/2511.13277v1#S3.F1 "Figure 1 ‣ III The linear regime 𝛾→0 ‣ Stationary Distributions of the Mode-switching Chiarella Model") but for α≪κ\alpha\ll\kappa, while γ\gamma large, with p​(δ)p(\delta) according to Eq.([22](https://arxiv.org/html/2511.13277v1#S4.E22 "In IV.0.2 Large-𝛾 limit ‣ IV Slow Trends: the 𝜅≫𝛼 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model")). Numerical parameters are (α,β,γ,σN,σV)=(2×10−5, 0.05, 5×104, 0.2, 0.1)(\alpha,\,\beta,\,\gamma,\,\sigma\_{N},\,\sigma\_{V})=(2\times 10^{-5},\,0.05,\,5\times 10^{4},\,0.2,\,0.1) and κ\kappa detailed in the plot. T=5×107T=5\times 10^{7}, dt=0.01t=0.01.

#### IV.0.2 Large-γ\gamma limit

In the limit γ→∞\gamma\to\infty, the leading exponential order of the cosh overwhelms all others, meaning that coshn⁡(γ​(α​x+y))≈cosh⁡(n​γ​(α​x+y))\cosh^{n}(\gamma(\alpha x+y))\approx\cosh(n\gamma(\alpha x+y)), such that the integrands can be simplified. In this limit one does not have to assume an integer nn. For the normalisation A​(y)A(y) this means

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(y)\displaystyle A(y) | ≈∫−∞∞e−κ​x2σ2​(cosh⁡(n​γ​(α​x+y)))​dx\displaystyle\approx\int\_{-\infty}^{\infty}\mathrm{e}^{-\frac{\kappa x^{2}}{\sigma^{2}}}\left(\cosh(n\gamma(\alpha x+y))\right)\,\differential x |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =π​σ2κ​en24​κ​(α​γ​σ)2​cosh⁡(n​γ​y).\displaystyle=\sqrt{\frac{\pi\sigma^{2}}{\kappa}}\mathrm{e}^{\frac{n^{2}}{4\kappa}(\alpha\gamma\sigma)^{2}}\cosh(n\gamma y). |  | (21) |

Therewith and reinserting n=2​βα​γ​σ2n=\frac{2\beta}{\alpha\gamma\sigma^{2}}, the stationary mispricing distribution can be inferred:

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(δ)=p​(x)\displaystyle p(\delta)=p(x) | =∫−∞∞p​(x|y)​p​(y)​dy\displaystyle=\int\_{-\infty}^{\infty}p(x|y)p(y)\,\differential y |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =κπ​σ2​e−β2κ​σ2​cosh⁡(2​βσ2​δ)​e−κ​δ2σ2,\displaystyle=\sqrt{\frac{\kappa}{\pi\sigma^{2}}}\mathrm{e}^{-\frac{\beta^{2}}{\kappa\sigma^{2}}}\cosh\left(\frac{2\beta}{\sigma^{2}}\delta\right)\mathrm{e}^{-\frac{\kappa\delta^{2}}{\sigma^{2}}}, |  | (22) |

which is independent of both α\alpha, γ\gamma; see also Appendix [C.2](https://arxiv.org/html/2511.13277v1#A3.SS2 "C.2 Large-𝛾-Limit Derivations: Normalisation and Stationary Distribution ‣ Appendix C Additional Results in the limit 𝛼≪𝜅 ‣ Stationary Distributions of the Mode-switching Chiarella Model"). This is the Gaussian-cosh distribution that will again show up in the case α≫κ\alpha\gg\kappa, see Appendix [E](https://arxiv.org/html/2511.13277v1#A5 "Appendix E Stationary Distribution for {𝛼,𝛽}≫𝜅 and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model"), Eq. ([158](https://arxiv.org/html/2511.13277v1#A5.E158 "In E.0.1 Quasi-static Assumption for 𝑥 ‣ Appendix E Stationary Distribution for {𝛼,𝛽}≫𝜅 and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model")). The (higher-order) Gaussian-cosh distribution has previously been discussed in the context of Gaussian-cosh beam propagation in optical systems zhou2011cosh-Gaussian.

#### IV.0.3 Uni- or bimodality

The stationary distribution in the large-γ\gamma limit, Eq.([22](https://arxiv.org/html/2511.13277v1#S4.E22 "In IV.0.2 Large-𝛾 limit ‣ IV Slow Trends: the 𝜅≫𝛼 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model")), has an extremum at x=δ=0x=\delta=0, which is either a unique maximum (unimodality) or a minimum accompanied by two maxima symmetrically placed around it (bimodality) at solutions to tanh⁡(2​β​x/σ2)=κ​x/β\tanh(2\beta x/\sigma^{2})=\kappa x/\beta as pp is even.
The modality-type can be investigated through the curvature at x=0x=0 for p′′​(0)≤0p^{\prime\prime}(0)\leq 0 implies unimodality and p′′​(0)>0p^{\prime\prime}(0)>0 bimodality, which can be summarised as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∙unimodality:κ≥2​β2σ2\displaystyle\bullet\text{unimodality:}\quad\kappa\geq\frac{2\beta^{2}}{\sigma^{2}} |  | (23) |
|  |  | ∙bimodality:κ<2​β2σ2.\displaystyle\bullet\text{bimodality:}\quad\,\,\,\,\kappa<\frac{2\beta^{2}}{\sigma^{2}}. |  |

This result should be compared with the condition κ=α​(β​γ−1)\kappa=\alpha(\beta\gamma-1) for the loss of stability of the fixed point (δ⋆,M⋆)=(0,0)(\delta^{\star},M^{\star})=(0,0) mentioned above. Hence we refute the claim in chiarella2011stoch\_bif that the P-bifurcation condition – the bifurcation in the modality of the stationary distribution – coincides with the bifurcation condition on the possible types of solutions to Eqs. ([II](https://arxiv.org/html/2511.13277v1#S2.Ex3 "II A Generalised Chiarella Model ‣ Stationary Distributions of the Mode-switching Chiarella Model")) (convergence vs. oscillation). Instead, we find that the criterion is more subtle and depends on both the noise of PP and VV through σ\sigma. Naturally, we confirm that the mean-reversion force ∼κ\sim\kappa works against bimodality and the trend component ∼β\sim\beta induces bimodality – albeit in a non-trivial quadratic way and not linearly as stated in chiarella2011stoch\_bif. Finally, it shows that strong enough noise can wipe out any bimodality, an intuitive result indeed.

Our claim is numerically confirmed in Fig. [2](https://arxiv.org/html/2511.13277v1#S4.F2 "Figure 2 ‣ IV.0.1 The quasi-static equilibrium ‣ IV Slow Trends: the 𝜅≫𝛼 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model"), which displays several distributions with the correct number of modes according to Eqs. ([23](https://arxiv.org/html/2511.13277v1#S4.E23 "In IV.0.3 Uni- or bimodality ‣ IV Slow Trends: the 𝜅≫𝛼 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model")). The center case of Fig. [2](https://arxiv.org/html/2511.13277v1#S4.F2 "Figure 2 ‣ IV.0.1 The quasi-static equilibrium ‣ IV Slow Trends: the 𝜅≫𝛼 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model") is a case where the condition by Chiarella et al. chiarella2011stoch\_bif would have falsely predicted p​(δ)p(\delta) to be unimodal via the Hopf-bifurcation condition of the dynamical system, while Eq.([23](https://arxiv.org/html/2511.13277v1#S4.E23 "In IV.0.3 Uni- or bimodality ‣ IV Slow Trends: the 𝜅≫𝛼 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model")) correctly predicts the bimodality, which has further been confirmed on edge cases.

![Refer to caption](x3.png)


Figure 3: Same as Fig. [1](https://arxiv.org/html/2511.13277v1#S3.F1 "Figure 1 ‣ III The linear regime 𝛾→0 ‣ Stationary Distributions of the Mode-switching Chiarella Model") but in the case α≫κ\alpha\gg\kappa with p​(δ)p(\delta) according to Eq.([25](https://arxiv.org/html/2511.13277v1#S5.E25 "In V.0.1 Weak coupling: Θ≪1 ‣ V Fast Trends: the 𝛼≫𝜅 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model")). Numerical parameters are (α,γ,σN,σV)=(500, 1, 0.8, 0.1)(\alpha,\,\gamma,\,\sigma\_{N},\,\sigma\_{V})=(500,\,1,\,0.8,\,0.1), while κ\kappa and β\beta are detailed in the plot. T=105T=10^{5}, dt=10−3t=10^{-3}.

## V Fast Trends: the α≫κ\alpha\gg\kappa Limit

Considering the Langevin equation corresponding to Eqs. ([14](https://arxiv.org/html/2511.13277v1#S4.E14 "In IV Slow Trends: the 𝜅≫𝛼 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model")), we see that yy tracks xx closely when α≫κ\alpha\gg\kappa. In this case, and assuming γ​σN2↛0\gamma\sigma\_{N}^{2}\nrightarrow 0, the hyperbolic tangent acts as an auto-correlated telegraphic noise ξttele∈{±1}\xi^{\textup{tele}}\_{t}\in\{\pm 1\}. In that case first yy and then xx can be integrated out, such that the second moment ⟨x2⟩\langle x^{2}\rangle may be derived (see Appendices [B](https://arxiv.org/html/2511.13277v1#A2 "Appendix B Change of Variables ‣ Stationary Distributions of the Mode-switching Chiarella Model"), [D](https://arxiv.org/html/2511.13277v1#A4 "Appendix D Stationary Distribution for 𝛼≫{𝜅,𝛽} and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model")). It turns out that sub-cases are determined by the a-dimensional parameter Θ:=β/(σN​α)\Theta:=\beta/(\sigma\_{N}\sqrt{\alpha}).

#### V.0.1 Weak coupling: Θ≪1\Theta\ll 1

The switching rate of the telegraphic noise ξtele\xi^{\textup{tele}} is proportional to α\alpha in this case. When α≫κ\alpha\gg\kappa, the distribution is then a unimodal Gaussian because the telegraphic noise switches sign much faster than any relaxation to a potential steady state at x≈±βeff /κeff x\approx\pm{\beta\_{\text{eff\,}}}/{\kappa\_{\text{eff\,}}} could take place (on a typical time scale 1/κeff 1/\kappa\_{\text{eff\,}}), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | κeff =κ​(1+2​Θπ)andβeff =β​(1+2​Θπ);\kappa\_{\text{eff\,}}=\kappa\left(1+\frac{2\Theta}{\sqrt{\pi}}\right)\quad\text{and}\quad\beta\_{\text{eff\,}}=\beta\left(1+\frac{2\Theta}{\sqrt{\pi}}\right); |  | (24) |

see also Appendix [D](https://arxiv.org/html/2511.13277v1#A4 "Appendix D Stationary Distribution for 𝛼≫{𝜅,𝛽} and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model"). The distribution in this limit reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(δ)=p​(x)=𝒩​(0,⟨x2⟩),p(\delta)=p(x)=\mathcal{N}(0,\langle x^{2}\rangle), |  | (25) |

where 𝒩\mathcal{N} refers to the Gaussian distribution; it has mean zero and variance

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨x2⟩=σ22​κeff +2​α​σN2π​κ​(α+κeff )​Θ+ln⁡(2)​σN2κ​Θ2+𝒪​(Θ3).\langle x^{2}\rangle=\frac{\sigma^{2}}{2\kappa\_{\text{eff\,}}}+\frac{2\alpha\sigma\_{N}^{2}}{\sqrt{\pi}\kappa(\alpha+\kappa\_{\text{eff\,}})}\Theta+\frac{\ln(2)\sigma\_{N}^{2}}{\kappa}\Theta^{2}+\mathcal{O}(\Theta^{3}). |  | (26) |

This is fully derived in Appendix [D](https://arxiv.org/html/2511.13277v1#A4 "Appendix D Stationary Distribution for 𝛼≫{𝜅,𝛽} and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model") using the Furutsu-Novikov theorem ishimaru1978wave and illustrated for different values of β\beta and κ\kappa in Fig. [3](https://arxiv.org/html/2511.13277v1#S4.F3 "Figure 3 ‣ IV.0.3 Uni- or bimodality ‣ IV Slow Trends: the 𝜅≫𝛼 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model").

Chiarella et al. derive an analytical distribution of the trend signal p​(M)p(M) for α≫κ\alpha\gg\kappa but only in the absence of noise traders (σN=0\sigma\_{N}=0). In this case Eq. ([25](https://arxiv.org/html/2511.13277v1#S5.E25 "In V.0.1 Weak coupling: Θ≪1 ‣ V Fast Trends: the 𝛼≫𝜅 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model")) does not hold as the condition γ​σN2↛0\gamma\sigma\_{N}^{2}\nrightarrow 0 is violated. They do not offer an analytical result for p​(δ)p(\delta) chiarella2011stoch\_bif.

#### V.0.2 Moderate to strong coupling: Θ∼1\Theta\sim 1

In the limit where α≫κ\alpha\gg\kappa, Θ≳1\Theta\gtrsim 1, we can disprove another claim from the literature (comp. chiarella2011stoch\_bif; majewski2020co; kurth2025revisiting), which is that bimodal trend distributions must co-occur with bimodal mispricing distributions. This claim only holds true in the absence of noise traders (σN=0\sigma\_{N}=0), which is the case regarded in chiarella2008stochastic\_bifurc. But in the presence of noise traders (which is the realistic case in the context of most physical systems, including financial markets, and our model), this result crumbles down.

Instead, we show that when α≫κ\alpha\gg\kappa, Θ≳1\Theta\gtrsim 1, a bimodal trend distribution p​(M)p(M) (again of the Gaussian-cosh type) does not imply a bimodal mispricing distribution p​(δ)p(\delta). From Eq. ([158](https://arxiv.org/html/2511.13277v1#A5.E158 "In E.0.1 Quasi-static Assumption for 𝑥 ‣ Appendix E Stationary Distribution for {𝛼,𝛽}≫𝜅 and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model")) in Appendix [E](https://arxiv.org/html/2511.13277v1#A5 "Appendix E Stationary Distribution for {𝛼,𝛽}≫𝜅 and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model"), our scenario is that as Θ\Theta increases, p​(M)p(M) becomes bimodal while p​(δ)p(\delta) remains unimodal before both become bimodal for Θ>Θc\Theta>\Theta\_{c} (and thus β\beta, the strength of the trend feedback, large enough).

This scenario is supported by Fig. [4](https://arxiv.org/html/2511.13277v1#S5.F4 "Figure 4 ‣ V.0.2 Moderate to strong coupling: Θ∼1 ‣ V Fast Trends: the 𝛼≫𝜅 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model") (top row), which shows that there indeed exists a parameter range, in which the stationary trend distribution p​(M)p(M) is bimodal, while the mispricing distribution p​(δ)p(\delta) is still unimodal; p​(δ)p(\delta) also becomes bimodal when β\beta is further increased as displayed in Fig. [4](https://arxiv.org/html/2511.13277v1#S5.F4 "Figure 4 ‣ V.0.2 Moderate to strong coupling: Θ∼1 ‣ V Fast Trends: the 𝛼≫𝜅 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model") (bottom row). The underlying mechanism, detailed in Appendix [E](https://arxiv.org/html/2511.13277v1#A5 "Appendix E Stationary Distribution for {𝛼,𝛽}≫𝜅 and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model"), is that for intermediate values of β≳1/γ\beta\gtrsim 1/\gamma the distribution p​(M)p(M) becomes bimodal (see Eq. ([158](https://arxiv.org/html/2511.13277v1#A5.E158 "In E.0.1 Quasi-static Assumption for 𝑥 ‣ Appendix E Stationary Distribution for {𝛼,𝛽}≫𝜅 and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model"))) but MM remains fast compared to δ\delta, so that the telegraphic noise ξtele\xi^{\textup{tele}} cannot “polarize” δ\delta long enough for p​(δ)p(\delta) to become bimodal. When β\beta increases further, the dynamics of MM abruptly slows down – in fact as α−1​eΘ2\alpha^{-1}e^{\Theta^{2}} –, so that β​tanh⁡(γ​M)\beta\tanh(\gamma M) pushes δ\delta up or down for long enough to make p​(δ)p(\delta) bimodal. But, by the same token, the equilibration of MM at fixed δ\delta ceases to be fast when Θ\Theta increases, even when α\alpha is large, and therefore one can no longer use the argument based on separation of time scales developed in Appendix [E](https://arxiv.org/html/2511.13277v1#A5 "Appendix E Stationary Distribution for {𝛼,𝛽}≫𝜅 and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model"). The critical value of Θc≈0.798\Theta\_{c}\approx 0.798 for which p​(δ)p(\delta) becomes bimodal is thus only indicative and, as argued in Appendix [E](https://arxiv.org/html/2511.13277v1#A5 "Appendix E Stationary Distribution for {𝛼,𝛽}≫𝜅 and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model"), possibly a lower bound to the true value. In fact, as shown in Fig. [4](https://arxiv.org/html/2511.13277v1#S5.F4 "Figure 4 ‣ V.0.2 Moderate to strong coupling: Θ∼1 ‣ V Fast Trends: the 𝛼≫𝜅 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model"), the distribution p​(δ)p(\delta) is still unimodal for Θ=1.01\Theta=1.01.

![Refer to caption]()


Figure 4: Same as Fig. [1](https://arxiv.org/html/2511.13277v1#S3.F1 "Figure 1 ‣ III The linear regime 𝛾→0 ‣ Stationary Distributions of the Mode-switching Chiarella Model") but for α,β≫κ\alpha,\,\beta\gg\kappa, and for both p​(M)p(M) (left) and p​(δ)p(\delta) (right). Top: Numerical parameters are (α,κ,γ,σN,σV)=(50, 0.05,1, 0.7, 0.2)(\alpha,\,\kappa,\,\gamma,\,\sigma\_{N},\,\sigma\_{V})=(50,\,0.05,1,\,0.7,\,0.2), β=5\beta=5 and drift g=0g=0, corresponding to Θ≈1.01\Theta\approx 1.01 and γ​σN​α≈5\gamma\sigma\_{N}\sqrt{\alpha}\approx 5. T=105T=10^{5}, dt=0.001t=0.001. We clearly see that for this set of parameters p​(M)p(M) is bimodal while p​(δ)p(\delta) is still unimodal. Bottom: same parameters as before except β=18\beta=18, such that Θ≈3.64\Theta\approx 3.64, in which case both distributions are bimodal. We have no exact analytical predictions to compare with in these cases.

## VI Conclusion

In this paper, we have obtained, either exactly or approximately, the stationary distribution of an extended Chiarella model in many dynamical regimes of interest. This has led to several falsifications of results from the literature, which we have been able to amend, especially regarding the classification of the stationary distribution by its number of modes.

First, it was found that the stationary distribution is always unimodal when the dynamical system and its corresponding Fokker-Planck equation can be linearised, leading to a Gaussian stationary distribution of both the trend signal, and the mispricing, as well as their joint distribution, which is bivariate Gaussian. The condition for this to hold was explicitly computed.

Second, the claim that the P-bifurcation (bimodality) condition coincides with the Hopf-bifurcation condition of the noiseless dynamical system has been disproved, both analytically and numerically. A corrected condition for the transition from uni- to bimodality was established when the trend time scale, α−1\alpha^{-1}, and the trend saturation parameter, γ\gamma, are both large. The condition 2​β2>κ​σ22\beta^{2}>\kappa\sigma^{2} is linear in the mean-reversion strength κ\kappa as is the Hopf-bifurcation condition but quadratic in the trend feedback parameter β\beta, which is different from the Hopf-bifurcation condition. Furthermore, the new condition depends on the strength of both sources of noise. This may be interpreted intuitively: strong noise wipes out the bimodality by overshadowing it.

Third, a stationary distribution in the case where the trend time scale α−1\alpha^{-1} is short compared to the typical mean-reversion time κ−1\kappa^{-1}, while the positive feedback term β\beta is not very strong, is found via the Furutsu-Novikov theorem. In this case the distribution is unimodal and Gaussian, too. If, in turn, the positive feedback is strong, we find – disproving another common claim in the literature – that bimodality in the trend distribution does not necessarily imply bimodality in the mispricing distribution when the price variable has its own noise source. Only when the feedback parameter β\beta is sufficiently strong do both distributions become bimodal.

We have unfortunately not been able to find an exact analytical solution for the stationary distribution in these last cases, for reasons that we explain in the text and in the corresponding Appendix. However, it might be possible to obtain approximate solutions in these cases as well, in particular when the trend distribution is bimodal and the trend remains polarized in the same direction for a very long time. In this case, we expect the mispricing distribution to become close to the sum of two Gaussian distributions centred around ±β/κ\pm\beta/\kappa.

## Acknowledgements

This research was conducted within the Econophysics & Complex Systems Research Chair under the aegis of the Fondation du Risque, the Fondation de l’Ecole polytechnique, the Ecole polytechnique, and Capital Fund Management.

## Appendix A Proof of the Stationary Distribution in the small-β​γ\beta\gamma-limit

In this appendix we proof that the bivariate Gaussian stationary distribution derived using the Lyapunov equation ansatz in Sec. [III](https://arxiv.org/html/2511.13277v1#S3 "III The linear regime 𝛾→0 ‣ Stationary Distributions of the Mode-switching Chiarella Model") solves the corresponding stationary Fokker-Planck equation.
The stationary distribution is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(δ,M)=12​π​|𝚺|​exp⁡(−12​𝐱T​𝚺−1​𝐱),with​𝐱=(δM).p(\delta,M)=\frac{1}{2\pi\sqrt{|\mathbf{\Sigma}|}}\exp\left(-\frac{1}{2}\mathbf{x}^{T}\mathbf{\Sigma}^{-1}\mathbf{x}\right),\quad\text{with}\,\,\mathbf{x}=\begin{pmatrix}\delta\\ M\end{pmatrix}. |  | (27) |

where the covariance matrix 𝚺\mathbf{\Sigma} and its inverse are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝚺\displaystyle\mathbf{\Sigma} | =12​(α​(1−β​γ)+κ)​(α​σ2​(β​γ−1)2+α​β​γ​σN2​(2−β​γ)+κ​σ2κα​(σ2​(1−β​γ)+σN2​(β​γ−2))α​(σ2​(1−β​γ)+σN2​(β​γ−2))α​(α​σN2+κ​(σ2−σN2))),\displaystyle=\frac{1}{2(\alpha(1-\beta\gamma)+\kappa)}\begin{pmatrix}\frac{\alpha\sigma^{2}(\beta\gamma-1)^{2}+\alpha\beta\gamma\sigma\_{N}^{2}(2-\beta\gamma)+\kappa\sigma^{2}}{\kappa}&\alpha(\sigma^{2}(1-\beta\gamma)+\sigma\_{N}^{2}(\beta\gamma-2))\\ \alpha(\sigma^{2}(1-\beta\gamma)+\sigma\_{N}^{2}(\beta\gamma-2))&\alpha(\alpha\sigma\_{N}^{2}+\kappa(\sigma^{2}-\sigma\_{N}^{2}))\\ \end{pmatrix}, |  | (28) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝚺−1\displaystyle\mathbf{\Sigma}^{-1} | =2​(α​(β​γ−1)−κ)σ2​σN2​(−α2​(β​γ−1)2+2​α​κ​(β​γ−2)+κ2)+α​σN4​(β​γ−2)​(α​β​γ−2​κ)−κ2​σ4×\displaystyle=\frac{2(\alpha(\beta\gamma-1)-\kappa)}{\sigma^{2}\sigma\_{N}^{2}\left(-\alpha^{2}(\beta\gamma-1)^{2}+2\alpha\kappa(\beta\gamma-2)+\kappa^{2}\right)+\alpha\sigma\_{N}^{4}(\beta\gamma-2)(\alpha\beta\gamma-2\kappa)-\kappa^{2}\sigma^{4}}\qquad\times |  | (29) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | (κ​(σN2​(α−κ)+κ​σ2)κ​(σ2​(1−β​γ)+σN2​(β​γ−2))κ​(σ2​(1−β​γ)+σN2​(β​γ−2))σ2​(α​(β​γ−1)2+κ)α+β​γ​σN2​(2−β​γ))=:(abbc).\displaystyle\qquad\qquad\qquad\qquad\qquad\qquad\qquad\begin{pmatrix}\kappa\left(\sigma\_{N}^{2}(\alpha-\kappa)+\kappa\sigma^{2}\right)&\kappa\left(\sigma^{2}(1-\beta\gamma)+\sigma\_{N}^{2}(\beta\gamma-2)\right)\\ \kappa\left(\sigma^{2}(1-\beta\gamma)+\sigma\_{N}^{2}(\beta\gamma-2)\right)&\frac{\sigma^{2}\left(\alpha(\beta\gamma-1)^{2}+\kappa\right)}{\alpha}+\beta\gamma\sigma\_{N}^{2}(2-\beta\gamma)\\ \end{pmatrix}=:\begin{pmatrix}a&b\\ b&c\end{pmatrix}. |  | (30) |

The partial derivatives of pp are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂δp\displaystyle\partial\_{\delta}p | =−(a​δ+b​M)​p,\displaystyle=-(a\delta+bM)p, |  | (31) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂Mp\displaystyle\partial\_{M}p | =−(b​δ+c​M)​p,\displaystyle=-(b\delta+cM)p, |  | (32) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂δ2p\displaystyle\partial\_{\delta}^{2}p | =[(a​δ+b​M)2−a]​p,\displaystyle=\left[(a\delta+bM)^{2}-a\right]p, |  | (33) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂M2p\displaystyle\partial\_{M}^{2}p | =[(b​δ+c​M)2−c]​p,\displaystyle=\left[(b\delta+cM)^{2}-c\right]p, |  | (34) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂δ∂Mp\displaystyle\partial\_{\delta}\partial\_{M}p | =[(a​δ+b​M)​(b​δ+c​M)−b]​p.\displaystyle=\left[(a\delta+bM)(b\delta+cM)-b\right]p. |  | (35) |

Next, we insert these into the following stationary FPE, which is equivalent to the linear FPE, Eq.([6](https://arxiv.org/html/2511.13277v1#S3.E6 "In III The linear regime 𝛾→0 ‣ Stationary Distributions of the Mode-switching Chiarella Model")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=κ​p+κ​δ​∂δp−β​γ​M​∂δp+α​(1−β​γ)​p+α​(1−β​γ)​M​∂Mp+α​κ​δ​∂Mp+σ22​∂δ2p+α​σN2​∂δ∂Mp+α2​σN22​∂M2p0=\kappa p+\kappa\delta\partial\_{\delta}p-\beta\gamma M\partial\_{\delta}p+\alpha(1-\beta\gamma)p+\alpha(1-\beta\gamma)M\partial\_{M}p+\alpha\kappa\delta\partial\_{M}p+\frac{\sigma^{2}}{2}\partial\_{\delta}^{2}p+\alpha\sigma\_{N}^{2}\partial\_{\delta}\partial\_{M}p+\frac{\alpha^{2}\sigma\_{N}^{2}}{2}\partial\_{M}^{2}p |  | (36) |

and collect the terms by order.
Since the joint stationary distribution holds for all δ,M\delta,\,M, each term must be zero.

Constant terms:

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ+α​(1−β​γ)−σ22​a−α​σN2​b−α2​σN22​c​=!​0\kappa+\alpha(1-\beta\gamma)-\frac{\sigma^{2}}{2}a-\alpha\sigma\_{N}^{2}b-\frac{\alpha^{2}\sigma\_{N}^{2}}{2}c\overset{!}{=}0 |  | (37) |

δ2\delta^{2}-terms:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −κ​a−α​κ​b+σ22​a2+α​σN2​a​b+α2​σN22​b2​=!​0-\kappa a-\alpha\kappa b+\frac{\sigma^{2}}{2}a^{2}+\alpha\sigma\_{N}^{2}ab+\frac{\alpha^{2}\sigma\_{N}^{2}}{2}b^{2}\overset{!}{=}0 |  | (38) |

M2M^{2}-terms:

|  |  |  |  |
| --- | --- | --- | --- |
|  | β​γ​b−α​(1−β​γ)​c+σ22​b2+α​σN2​b​c+α2​σN22​c2​=!​0\beta\gamma b-\alpha(1-\beta\gamma)c+\frac{\sigma^{2}}{2}b^{2}+\alpha\sigma\_{N}^{2}bc+\frac{\alpha^{2}\sigma\_{N}^{2}}{2}c^{2}\overset{!}{=}0 |  | (39) |

δ​M\delta M-terms:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −κ​b+β​γ​a−α​κ​c−α​(1−β​γ)​b+σ2​a​b+α​σN2​(a​c+b2)+α2​σN2​b​c​=!​0-\kappa b+\beta\gamma a-\alpha\kappa c-\alpha(1-\beta\gamma)b+\sigma^{2}ab+\alpha\sigma\_{N}^{2}(ac+b^{2})+\alpha^{2}\sigma\_{N}^{2}bc\overset{!}{=}0 |  | (40) |

The solution is confirmed, pp solves the FPE.

## Appendix B Change of Variables

Let us define x=δx=\delta and y=M−α​δ=M−α​xy=M-\alpha\delta=M-\alpha x.
Then in Langevin notation (ξtN/V\xi\_{t}^{N/V} are standard white noises):

|  |  |  |  |
| --- | --- | --- | --- |
|  | x˙\displaystyle\dot{x} | =−κ​x+β​tanh⁡(γ​M)+σN​ξtN−σV​ξtV\displaystyle=-\kappa x+\beta\tanh(\gamma M)+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−κ​x+β​tanh⁡(γ​(y+α​x))+σN​ξtN−σV​ξtV\displaystyle=-\kappa x+\beta\tanh(\gamma(y+\alpha x))+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V} |  | (41) |

And

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | y˙\displaystyle\dot{y} | =M˙−α​x˙\displaystyle=\dot{M}-\alpha\dot{x} |  | (42) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−α​M+α​(x˙+σV​ξtV)−α​x˙\displaystyle=-\alpha M+\alpha(\dot{x}+\sigma\_{V}\xi\_{t}^{V})-\alpha\dot{x} |  | (43) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−α​M+α​σV​ξtV\displaystyle=-\alpha M+\alpha\sigma\_{V}\xi\_{t}^{V} |  | (44) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−α​y−α2​x+α​σV​ξtV\displaystyle=-\alpha y-\alpha^{2}x+\alpha\sigma\_{V}\xi\_{t}^{V} |  | (45) |

So for α≪κ\alpha\ll\kappa this mean that yy is an approximate OU process and the derivation of the stationary distribution in Sec. [IV](https://arxiv.org/html/2511.13277v1#S4 "IV Slow Trends: the 𝜅≫𝛼 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model") holds true.

To solve for the stationary distribution in cases where α≫κ\alpha\gg\kappa, y˙\dot{y} first has to be solved, which can be done by multiplying both side with an integrating factor eα​t\mathrm{e}^{\alpha t}, and yields (t>st>s)

|  |  |  |  |
| --- | --- | --- | --- |
|  | y​(t)=e−α​t​y​(0)−α2​e−α​t​∫0teα​s​x​(s)​ds+α​σV​e−α​t​∫0teα​s​ξsV​ds;y(t)=\mathrm{e}^{-\alpha t}y(0)-\alpha^{2}\mathrm{e}^{-\alpha t}\int\_{0}^{t}\mathrm{e}^{\alpha s}x(s)\,\differential s+\alpha\sigma\_{V}\mathrm{e}^{-\alpha t}\int\_{0}^{t}\mathrm{e}^{\alpha s}\xi^{V}\_{s}\,\differential s; |  | (46) |

in the stationary limit, in which the inital condition is forgotten, this becomes (using integration by parts)

|  |  |  |  |
| --- | --- | --- | --- |
|  | y​(t)\displaystyle y(t) | =−α2​∫0te−α​(t−s)​x​(s)​ds+α​σV​∫0te−α​(t−s)​ξsV​ds\displaystyle=-\alpha^{2}\int\_{0}^{t}\mathrm{e}^{-\alpha(t-s)}x(s)\,\differential s+\alpha\sigma\_{V}\int\_{0}^{t}\mathrm{e}^{-\alpha(t-s)}\xi^{V}\_{s}\,\differential s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−α​x​(t)+α​∫0te−α​(t−s)​x˙​(s)​ds+α​σV​∫0te−α​(t−s)​ξsV​ds,\displaystyle=-\alpha x(t)+\alpha\int\_{0}^{t}\mathrm{e}^{-\alpha(t-s)}\dot{x}(s)\,\differential s+\alpha\sigma\_{V}\int\_{0}^{t}\mathrm{e}^{-\alpha(t-s)}\xi^{V}\_{s}\,\differential s, |  |

a convolution integral. Note also that the third term is the (stationary) solution to an Ornstein-Uhlenbeck (OU) process with mean reversion level zero, mean reversion strength α\alpha and a variance of α​σV2/2\alpha\sigma\_{V}^{2}/2.

Inserting this into x˙\dot{x} yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | x˙\displaystyle\dot{x} | =−κ​x+β​tanh⁡(γ​(y+α​x))+σN​ξtN−σV​ξtV\displaystyle=-\kappa x+\beta\tanh(\gamma(y+\alpha x))+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−κ​x+β​tanh⁡(γ​(α​∫0te−α​(t−s)​x˙​(s)​ds+α​σV​∫0te−α​(t−s)​ξsV​ds))+σN​ξtN−σV​ξtV.\displaystyle=-\kappa x+\beta\tanh(\gamma(\alpha\int\_{0}^{t}\mathrm{e}^{-\alpha(t-s)}\dot{x}(s)\,\differential s+\alpha\sigma\_{V}\int\_{0}^{t}\mathrm{e}^{-\alpha(t-s)}\xi^{V}\_{s}\,\differential s))+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V}. |  | (48) |

A special case of this Langevin equation will be further analysed in Appendix [D](https://arxiv.org/html/2511.13277v1#A4 "Appendix D Stationary Distribution for 𝛼≫{𝜅,𝛽} and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model").

## Appendix C Additional Results in the limit α≪κ\alpha\ll\kappa

### C.1 Normalisation Function A​(y)A(y)

In this section we derive the normalisation function A​(y)A(y) given in Sec. [IV](https://arxiv.org/html/2511.13277v1#S4 "IV Slow Trends: the 𝜅≫𝛼 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model"), Eq.([19](https://arxiv.org/html/2511.13277v1#S4.E19 "In IV.0.1 The quasi-static equilibrium ‣ IV Slow Trends: the 𝜅≫𝛼 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model")).
As detailed in the main text, Eq.([18](https://arxiv.org/html/2511.13277v1#S4.E18 "In IV.0.1 The quasi-static equilibrium ‣ IV Slow Trends: the 𝜅≫𝛼 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model")), the normalisation function reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(y)=∫−∞∞e−1σ2​κ​x2​cosh⁡(γ​(α​x+y))n​dxA(y)=\int\_{-\infty}^{\infty}\mathrm{e}^{-\frac{1}{\sigma^{2}}\kappa x^{2}}\cosh(\gamma(\alpha x+y))^{n}\,\differential x |  | (49) |

and can generally only be calculated for integer exponents n=2​βα​γ​σ2∈ℕn=\frac{2\beta}{\alpha\gamma\sigma^{2}}\in\mathbb{N} of the hyperbolic cosine. As before: σ=σN2+σV2\sigma=\sqrt{\sigma\_{N}^{2}+\sigma\_{V}^{2}}.

Using the binomial theorem and the exponential representation of the cosh, the integral can be rewritten as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∫−∞∞e−κ​x2σ2​12n​(e−γ​α​x​e−γ​y+eγ​α​x​eγ​y)n​dx\displaystyle\int\_{-\infty}^{\infty}\mathrm{e}^{-\frac{\kappa x^{2}}{\sigma^{2}}}\frac{1}{2^{n}}\left(\mathrm{e}^{-\gamma\alpha x}\mathrm{e}^{-\gamma y}+\mathrm{e}^{\gamma\alpha x}\mathrm{e}^{\gamma y}\right)^{n}\,\differential x |  | (50) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | ∫−∞∞e−κ​x2σ2​12n​(∑k=0n(nk)​e−γ​α​x​(n−k)​e−γ​y​(n−k)​eγ​α​x​k​eγ​y​k)​dx\displaystyle\int\_{-\infty}^{\infty}\mathrm{e}^{-\frac{\kappa x^{2}}{\sigma^{2}}}\frac{1}{2^{n}}\left(\sum\_{k=0}^{n}\binom{n}{k}\mathrm{e}^{-\gamma\alpha x(n-k)}\mathrm{e}^{-\gamma y(n-k)}\mathrm{e}^{\gamma\alpha xk}\mathrm{e}^{\gamma yk}\right)\,\differential x |  | (51) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 12n​∑k=0n(nk)​e−γ​(n−2​k)​y​∫−∞∞e−κ​x2σ2−α​γ​(n−2​k)​x​dx\displaystyle\frac{1}{2^{n}}\sum\_{k=0}^{n}\binom{n}{k}\mathrm{e}^{-\gamma(n-2k)y}\int\_{-\infty}^{\infty}\mathrm{e}^{-\frac{\kappa x^{2}}{\sigma^{2}}-\alpha\gamma(n-2k)x}\,\differential x |  | (52) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 12n​π​σ2κ​∑k=0n(nk)​e−γ​(n−2​k)​y+(α​γ​σ)24​κ​(n−2​k)2,\displaystyle\frac{1}{2^{n}}\sqrt{\frac{\pi\sigma^{2}}{\kappa}}\sum\_{k=0}^{n}\binom{n}{k}\mathrm{e}^{-\gamma(n-2k)y+\frac{(\alpha\gamma\sigma)^{2}}{4\kappa}(n-2k)^{2}}, |  | (53) |

where in the last step the Gaussian identity ∫−∞∞e−(a​x2+b​x)=πa​eb24​a\int\_{-\infty}^{\infty}\mathrm{e}^{-(ax^{2}+bx)}=\sqrt{\frac{\pi}{a}}\mathrm{e}^{\frac{b^{2}}{4a}} is used.

Now regard

|  |  |  |
| --- | --- | --- |
|  | 12n​∑k=0n(nk)​exp⁡[−γ​(n−2​k)​y+(α​γ​σ)24​κ​(n−2​k)2].\frac{1}{2^{n}}\sum\_{k=0}^{n}\binom{n}{k}\exp\left[-\gamma(n-2k)y+\frac{(\alpha\gamma\sigma)^{2}}{4\kappa}(n-2k)^{2}\right]. |  |

To simplify, a change of variables is performed. Define

|  |  |  |
| --- | --- | --- |
|  | mj:=2​j+ϵn,where ​ϵn={0if ​n​ is even1if ​n​ is odd.m\_{j}:=2j+\epsilon\_{n},\quad\text{where }\epsilon\_{n}=\begin{cases}0&\text{if }n\text{ is even}\\ 1&\text{if }n\text{ is odd.}\end{cases} |  |

Then jj runs over integers from −⌊n/2⌋-\lfloor n/2\rfloor to ⌊n/2⌋\lfloor n/2\rfloor, where ⌊.⌋\lfloor.\rfloor marks the floor-function for integer division, and the binomial coefficient becomes:

|  |  |  |
| --- | --- | --- |
|  | (nn−mj2)=(nn−(2​j+ϵn)2)=(nn−ϵn2−j)\binom{n}{\frac{n-m\_{j}}{2}}=\binom{n}{\frac{n-(2j+\epsilon\_{n})}{2}}=\binom{n}{\frac{n-\epsilon\_{n}}{2}-j} |  |

The sum then reads

|  |  |  |
| --- | --- | --- |
|  | 12n​∑j=−⌊n/2⌋⌊n/2⌋(nn−ϵn2−j)​exp⁡[−γ​(2​j+ϵn)​y+(α​γ​σ)24​κ​(2​j+ϵn)2]\frac{1}{2^{n}}\sum\_{j=-\lfloor n/2\rfloor}^{\lfloor n/2\rfloor}\binom{n}{\frac{n-\epsilon\_{n}}{2}-j}\exp\left[-\gamma(2j+\epsilon\_{n})y+\frac{(\alpha\gamma\sigma)^{2}}{4\kappa}(2j+\epsilon\_{n})^{2}\right] |  |

To further simplify the result, the symmetry of the sum may be exploited: The linear term in the exponent is odd in jj, while the quadratic term and the binomial coefficient are even in jj due to the identity:

|  |  |  |
| --- | --- | --- |
|  | (nn−ϵn2−j)=(nn−ϵn2+j).\binom{n}{\frac{n-\epsilon\_{n}}{2}-j}=\binom{n}{\frac{n-\epsilon\_{n}}{2}+j}. |  |

Thus, the overall sum is symmetric (for j≠0j\neq 0), and jj- and −j-j-terms can be grouped together:

|  |  |  |
| --- | --- | --- |
|  | exp⁡[−γ​mj​y+(α​γ​σ)24​κ​mj2]+exp⁡[+γ​mj​y+(α​γ​σ)24​κ​mj2]=2​cosh⁡(γ​mj​y)⋅exp⁡((α​γ​σ)24​κ​mj2).\exp\left[-\gamma m\_{j}y+\frac{(\alpha\gamma\sigma)^{2}}{4\kappa}m\_{j}^{2}\right]+\exp\left[+\gamma m\_{j}y+\frac{(\alpha\gamma\sigma)^{2}}{4\kappa}m\_{j}^{2}\right]=2\cosh(\gamma m\_{j}y)\cdot\exp\left(\frac{(\alpha\gamma\sigma)^{2}}{4\kappa}m\_{j}^{2}\right). |  |

Therefore, the final expression reads

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 12n​[(nn−ϵn2)​e(α​γ​σ)24​κ​ϵn2​[2​ϵn​cosh⁡(γ​y)+(1−ϵn)]+2​∑j=1⌊n/2⌋(nn−ϵn2−j)​cosh⁡(γ​(2​j+ϵn)​y)​e(α​γ​σ)24​κ​(2​j+ϵn)2]\displaystyle\frac{1}{2^{n}}\bigg[\binom{n}{\frac{n-\epsilon\_{n}}{2}}\mathrm{e}^{\frac{(\alpha\gamma\sigma)^{2}}{4\kappa}\epsilon\_{n}^{2}}\left[2\epsilon\_{n}\cosh(\gamma y)+(1-\epsilon\_{n})\right]+2\sum\_{j=1}^{\lfloor n/2\rfloor}\binom{n}{\frac{n-\epsilon\_{n}}{2}-j}\cosh\left(\gamma(2j+\epsilon\_{n})y\right)\mathrm{e}^{\frac{(\alpha\gamma\sigma)^{2}}{4\kappa}(2j+\epsilon\_{n})^{2}}\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 12n−1​[12​(nn−ϵn2)​(2​ϵn​cosh⁡(γ​y)​e(α​γ​σ)24​κ+(1−ϵn))+∑j=1⌊n/2⌋(nn−ϵn2−j)​cosh⁡(γ​(2​j+ϵn)​y)​e(α​γ​σ)24​κ​(2​j+ϵn)2].\displaystyle\frac{1}{2^{n-1}}\left[\frac{1}{2}\binom{n}{\frac{n-\epsilon\_{n}}{2}}\left(2\epsilon\_{n}\cosh(\gamma y)\mathrm{e}^{\frac{(\alpha\gamma\sigma)^{2}}{4\kappa}}+(1-\epsilon\_{n})\right)+\sum\_{j=1}^{\lfloor n/2\rfloor}\binom{n}{\frac{n-\epsilon\_{n}}{2}-j}\cosh\left(\gamma(2j+\epsilon\_{n})y\right)\mathrm{e}^{\frac{(\alpha\gamma\sigma)^{2}}{4\kappa}(2j+\epsilon\_{n})^{2}}\right]. |  |

This is the simplified and symmetrized form of the original sum, now including the binomial weights and expressed as a weighted sum of hyperbolic cosine functions. The first two terms are the case distinction for j=0j=0 (then ϵn=0\epsilon\_{n}=0 when nn is even but ϵn=1\epsilon\_{n}=1 when nn is odd), which is a cosh for odd nn as the index never becomes zero in that case such that the symmetry relation still holds. For even nn, the index goes through zero (as the decrements are in steps of 2), in which case there is only one summand and no pairing and the summand becomes 1∼e01\sim\mathrm{e}^{0}.

This concludes the proof of Eq.([19](https://arxiv.org/html/2511.13277v1#S4.E19 "In IV.0.1 The quasi-static equilibrium ‣ IV Slow Trends: the 𝜅≫𝛼 Limit ‣ Stationary Distributions of the Mode-switching Chiarella Model")), i.e.

|  |  |  |
| --- | --- | --- |
|  | A​(y)=12n−1​π​σ2κ​[(nn−ϵn2)⋅{12if ​n​ is evencosh⁡(γ​y)⋅e(α​γ​σ)24​κif ​n​ is odd+∑j=1⌊n/2⌋(nn−ϵn2−j)​cosh⁡(γ​(2​j+ϵn)​y)​e(α​γ​σ)24​κ​(2​j+ϵn)2].A(y)=\frac{1}{2^{n-1}}\sqrt{\frac{\pi\sigma^{2}}{\kappa}}\left[\binom{n}{\frac{n-\epsilon\_{n}}{2}}\cdot\begin{cases}\frac{1}{2}&\text{if }n\text{ is even}\\ \cosh(\gamma y)\cdot\mathrm{e}^{\frac{(\alpha\gamma\sigma)^{2}}{4\kappa}}&\text{if }n\text{ is odd}\end{cases}+\sum\_{j=1}^{\lfloor n/2\rfloor}\binom{n}{\frac{n-\epsilon\_{n}}{2}-j}\cosh\left(\gamma(2j+\epsilon\_{n})y\right)\mathrm{e}^{\frac{(\alpha\gamma\sigma)^{2}}{4\kappa}(2j+\epsilon\_{n})^{2}}\right]. |  |

### C.2 Large-γ\gamma-Limit Derivations: Normalisation and Stationary Distribution

In the limit γ→∞\gamma\to\infty, while α​γ=const.∈ℝ\alpha\gamma=\text{const.}\in\mathbb{R}, the stationary distribution can be derived. For that, A​(y)A(y) must first be determined. When the exponents in A​(y)A(y) are large, the leading order term substantially overwhelms all other terms. Therefore, taking the large-γ\gamma-limit (or the large-nn-limit), allows for the following approximations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (eα​γ​x​eγ​y+e−α​γ​x​e−γ​y)n\displaystyle(\mathrm{e}^{\alpha\gamma x}\mathrm{e}^{\gamma y}+\mathrm{e}^{-\alpha\gamma x}\mathrm{e}^{-\gamma y})^{n} | ≈{en​α​γ​x​en​γ​y,x>0e−n​α​γ​x​e−n​γ​y,x<0\displaystyle\approx\begin{cases}\mathrm{e}^{n\alpha\gamma x}\mathrm{e}^{n\gamma y},\,\,x>0\\ \mathrm{e}^{-n\alpha\gamma x}\mathrm{e}^{-n\gamma y},\,\,x<0\end{cases} |  | (54) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≈en​α​γ​x​en​γ​y+e−n​α​γ​x​e−n​γ​y≈2n​cosh⁡(n​γ​(α​x+y)),\displaystyle\approx\mathrm{e}^{n\alpha\gamma x}\mathrm{e}^{n\gamma y}+\mathrm{e}^{-n\alpha\gamma x}\mathrm{e}^{-n\gamma y}\approx 2^{n}\cosh(n\gamma(\alpha x+y)), |  | (55) |

where we have combined the cases x>0x>0 and x<0x<0 as one of the terms is asymptotically zero in either case and thus does not impact the asymptotic expansion. The same result could be obtained by performing the two integrals individually and adding the results back together for the full solution.
Thus, the normalisation is the following in this limit:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | A​(y)\displaystyle A(y) | ≈∫−∞∞e−κ​x2σ2​(cosh⁡(n​γ​(α​x+y)))​dx\displaystyle\approx\int\_{-\infty}^{\infty}\mathrm{e}^{-\frac{\kappa x^{2}}{\sigma^{2}}}\left(\cosh(n\gamma(\alpha x+y))\right)\,\differential x |  | (56) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =12​π​σ2κ​en24​κ​(α​γ​σ)2​e−n​γ​y​(1+e2​n​γ​y)\displaystyle=\frac{1}{2}\sqrt{\frac{\pi\sigma^{2}}{\kappa}}\mathrm{e}^{\frac{n^{2}}{4\kappa}(\alpha\gamma\sigma)^{2}}\mathrm{e}^{-n\gamma y}\left(1+\mathrm{e}^{2n\gamma y}\right) |  | (57) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =π​σ2κ​en24​κ​(α​γ​σ)2​cosh⁡(n​γ​y).\displaystyle=\sqrt{\frac{\pi\sigma^{2}}{\kappa}}\mathrm{e}^{\frac{n^{2}}{4\kappa}(\alpha\gamma\sigma)^{2}}\cosh(n\gamma y). |  | (58) |

Using the normalisation and the same asymptotic results above, the stationary distribution can be calculated

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | p​(x)\displaystyle p(x) | =∫−∞∞p​(x|y)​p​(y)​dy\displaystyle=\int\_{-\infty}^{\infty}p(x|y)p(y)\,\differential y |  | (59) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =12​π​V​a​r​[y]​e−κ​x2σ2​∫−∞∞1A​(y)​e−y22​V​a​r​[y]​cosh⁡(γ​(α​x+y))n​dy\displaystyle=\frac{1}{\sqrt{2\pi Var[y]}}\mathrm{e}^{-\frac{\kappa x^{2}}{\sigma^{2}}}\int\_{-\infty}^{\infty}\frac{1}{A(y)}\mathrm{e}^{\frac{-y^{2}}{2Var[y]}}\cosh(\gamma(\alpha x+y))^{n}\,\differential y |  | (60) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≈12​π​V​a​r​[y]​κπ​σ2​e−n24​κ​(α​γ​σ)2​e−κ​x2σ2​∫−∞∞1cosh⁡(n​γ​y)​e−y22​V​a​r​[y]​cosh⁡(n​γ​(α​x+y))​dy\displaystyle\approx\frac{1}{\sqrt{2\pi Var[y]}}\sqrt{\frac{\kappa}{\pi\sigma^{2}}}\mathrm{e}^{-\frac{n^{2}}{4\kappa}(\alpha\gamma\sigma)^{2}}\mathrm{e}^{-\frac{\kappa x^{2}}{\sigma^{2}}}\int\_{-\infty}^{\infty}\frac{1}{\cosh(n\gamma y)}\mathrm{e}^{\frac{-y^{2}}{2Var[y]}}\cosh(n\gamma(\alpha x+y))\,\differential y |  | (61) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =12​π​V​a​r​[y]​κπ​σ2​e−n24​κ​(α​γ​σ)2​e−κ​x2σ2​∫−∞∞e−y22​V​a​r​[y]cosh⁡(n​γ​y)​[cosh⁡(n​γ​α​x)​cosh⁡(n​γ​y)+sinh⁡(n​γ​α​x)​sinh⁡(n​γ​y)]​dy\displaystyle=\frac{1}{\sqrt{2\pi Var[y]}}\sqrt{\frac{\kappa}{\pi\sigma^{2}}}\mathrm{e}^{-\frac{n^{2}}{4\kappa}(\alpha\gamma\sigma)^{2}}\mathrm{e}^{-\frac{\kappa x^{2}}{\sigma^{2}}}\int\_{-\infty}^{\infty}\frac{\mathrm{e}^{\frac{-y^{2}}{2Var[y]}}}{\cosh(n\gamma y)}\left[\cosh(n\gamma\alpha x)\cosh(n\gamma y)+\sinh(n\gamma\alpha x)\sinh(n\gamma y)\right]\,\differential y |  | (62) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =12​π​V​a​r​[y]​κπ​σ2​e−n24​κ​(α​γ​σ)2​e−κ​x2σ2​[cosh⁡(n​α​γ​x)​∫−∞∞e−y22​V​a​r​[y]​dy+sinh⁡(n​α​γ​x)​∫−∞∞e−y22​V​a​r​[y]​tanh⁡(n​γ​y)​dy]\displaystyle=\frac{1}{\sqrt{2\pi Var[y]}}\sqrt{\frac{\kappa}{\pi\sigma^{2}}}\mathrm{e}^{-\frac{n^{2}}{4\kappa}(\alpha\gamma\sigma)^{2}}\mathrm{e}^{-\frac{\kappa x^{2}}{\sigma^{2}}}\left[\cosh(n\alpha\gamma x)\int\_{-\infty}^{\infty}\mathrm{e}^{\frac{-y^{2}}{2Var[y]}}\,\differential y+\sinh(n\alpha\gamma x)\int\_{-\infty}^{\infty}\mathrm{e}^{\frac{-y^{2}}{2Var[y]}}\tanh(n\gamma y)\,\differential y\right] |  | (63) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =κπ​σ2​e−n24​κ​(α​γ​σ)2​cosh⁡(n​α​γ​x)​e−κ​x2σ2,\displaystyle=\sqrt{\frac{\kappa}{\pi\sigma^{2}}}\mathrm{e}^{-\frac{n^{2}}{4\kappa}(\alpha\gamma\sigma)^{2}}\cosh(n\alpha\gamma x)\mathrm{e}^{-\frac{\kappa x^{2}}{\sigma^{2}}}, |  | (64) |

where the second integral equates zero because its integrand is odd over the symmetric integration domain.

Recalling n=2​βα​γ​σ2n=\frac{2\beta}{\alpha\gamma\sigma^{2}}, the stationary distribution in the large-γ\gamma(or nn)-limit finally reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(x)=κπ​σ2​e−β2κ​σ2​cosh⁡(2​βσ2​x)​e−κ​x2σ2.p(x)=\sqrt{\frac{\kappa}{\pi\sigma^{2}}}\mathrm{e}^{-\frac{\beta^{2}}{\kappa\sigma^{2}}}\cosh\left(\frac{2\beta}{\sigma^{2}}x\right)\mathrm{e}^{-\frac{\kappa x^{2}}{\sigma^{2}}}. |  | (65) |

Two things can be observed:

1. 1.

   The distribution lost its γ\gamma-dependence (as expected) but this leads to the stationary distribution being independent of the trend time scale α\alpha, too. Thus, whether the distribution is uni- or bimodal is independent of α\alpha and γ\gamma in this limit.
2. 2.

   There is always an extremum at x=0x=0, which is either unique and a maximum (unimodality), or a minimum accompanied by two maxima symmetrically placed around it (bimodality) for pp is even. In the bimodal case, interestingly, the position of the maxima will not only depend on β\beta and κ\kappa but also on the noise strength σ2\sigma^{2}. In particular they will be at solutions to the following equation: tanh⁡(2​β​x/σ2)=κ​x/β\tanh(2\beta x/\sigma^{2})=\kappa x/\beta, while x≠0x\neq 0.

#### C.2.1 Uni- and bimodality

The distribution is unimodal, when the extremum at x=0x=0 is a maximum, i.e. when p′′​(0)≤0p^{\prime\prime}(0)\leq 0, and bimodal in the complementary case.
The first derivative reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | p′​(x)=C​e−κ​x2σ2​[2​βσ2​sinh⁡(2​βσ2​x)−2​κσ2​x​cosh⁡(2​βσ2​x)],p^{\prime}(x)=C\mathrm{e}^{-\frac{\kappa x^{2}}{\sigma^{2}}}\left[\frac{2\beta}{\sigma^{2}}\sinh\left(\frac{2\beta}{\sigma^{2}}x\right)-\frac{2\kappa}{\sigma^{2}}x\cosh\left(\frac{2\beta}{\sigma^{2}}x\right)\right], |  | (66) |

(where CC is a positive constant factor) which clearly obeys p′​(0)=0p^{\prime}(0)=0.
The second derivative is

|  |  |  |  |
| --- | --- | --- | --- |
|  | p′′​(x)=C′​e−κ​x2σ2​[4​β2σ4​cosh⁡(2​βσ2​x)−4​β​κσ4​x​sinh⁡(2​βσ2​x)−2​κσ2​cosh⁡(2​βσ2​x)+4​κ2σ4​x2​cosh⁡(2​βσ2​x)].p^{\prime\prime}(x)=C^{\prime}\mathrm{e}^{-\frac{\kappa x^{2}}{\sigma^{2}}}\left[\frac{4\beta^{2}}{\sigma^{4}}\cosh\left(\frac{2\beta}{\sigma^{2}}x\right)-\frac{4\beta\kappa}{\sigma^{4}}x\sinh\left(\frac{2\beta}{\sigma^{2}}x\right)-\frac{2\kappa}{\sigma^{2}}\cosh\left(\frac{2\beta}{\sigma^{2}}x\right)+\frac{4\kappa^{2}}{\sigma^{4}}x^{2}\cosh\left(\frac{2\beta}{\sigma^{2}}x\right)\right]. |  | (67) |

Evaluated at x=0x=0, this leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | p′′​(x)=C′​(4​β2σ4−2​κσ2),p^{\prime\prime}(x)=C^{\prime}\left(\frac{4\beta^{2}}{\sigma^{4}}-\frac{2\kappa}{\sigma^{2}}\right), |  | (68) |

with constant C′>0C^{\prime}>0, which implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | unimodality:​κ≥2​β2σ2,\displaystyle\text{unimodality:}\qquad\kappa\geq\frac{2\beta^{2}}{\sigma^{2}}, |  | (69) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | bimodality:κ<2​β2σ2.\displaystyle\text{bimodality:}\qquad\,\,\,\,\kappa<\frac{2\beta^{2}}{\sigma^{2}}. |  | (70) |

## Appendix D Stationary Distribution for α≫κ,β\alpha\gg\kappa,\,\beta and γ​σN2↛0\gamma\sigma\_{N}^{2}\nrightarrow 0

Recall the following equation from Appendix [B](https://arxiv.org/html/2511.13277v1#A2 "Appendix B Change of Variables ‣ Stationary Distributions of the Mode-switching Chiarella Model"), where the third and fourth line are added anew here:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x˙\displaystyle\dot{x} | =−κ​x+β​tanh⁡(γ​(y+α​x))+σN​ξtN−σV​ξtV\displaystyle=-\kappa x+\beta\tanh(\gamma(y+\alpha x))+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−κ​x+β​tanh⁡(γ​(α​∫0te−α​(t−s)​x˙​(s)​ds+α​σV​∫0te−α​(t−s)​ξsV​ds))+σN​ξtN−σV​ξtV\displaystyle=-\kappa x+\beta\tanh(\gamma(\alpha\int\_{0}^{t}\mathrm{e}^{-\alpha(t-s)}\dot{x}(s)\,\differential s+\alpha\sigma\_{V}\int\_{0}^{t}\mathrm{e}^{-\alpha(t-s)}\xi^{V}\_{s}\,\differential s))+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V} |  | (71) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≈large𝛼−κ​x+β​tanh⁡(−γ​κ​x+γ​β​tanh⁡(γ​(y+α​x))+γ​α​σN​∫0te−α​(t−s)​ξsN​ds)+σN​ξtN−σV​ξtV\displaystyle\underset{\text{large}}{\overset{\alpha}{\approx}}-\kappa x+\beta\tanh(-\gamma\kappa x+\gamma\beta\tanh(\gamma(y+\alpha x))+\gamma\alpha\sigma\_{N}\int\_{0}^{t}\mathrm{e}^{-\alpha(t-s)}\xi\_{s}^{N}\,\differential s)+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V} |  | (72) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≈smallβ,κ−κ​x+β​tanh⁡(−γ​(κ​x−β​ξttele)+γ​α​σN​∫0te−α​(t−s)​ξsN​ds)+σN​ξtN−σV​ξtV+𝒪​(β3),\displaystyle\underset{\text{small}}{\overset{\beta,\,\kappa}{\approx}}-\kappa x+\beta\tanh(-\gamma(\kappa x-\beta\xi^{\textup{tele}}\_{t})+\gamma\alpha\sigma\_{N}\int\_{0}^{t}\mathrm{e}^{-\alpha(t-s)}\xi\_{s}^{N}\,\differential s)+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V}+\mathcal{O}(\beta^{3}), |  | (73) |

where in the third line it was used that α​e−α​(t−s)​⟶α→∞​δ​(t−s)​∀t>s\alpha\,\mathrm{e}^{-\alpha(t-s)}\overset{\alpha\to\infty}{\longrightarrow}\delta(t-s)\,\,\forall t>s, where δ​(t−s)\delta(t-s) is a Dirac-delta .
The encapsulated hyperbolic tangent may be approximated by auto-correlated telegraphic noise, ξtele∈{±1}\xi^{\textup{tele}}\in\{\pm 1\}, as all other correction terms would be ∼𝒪​(β3)\sim\mathcal{O}(\beta^{3}). Its auto-correlation structure and its effect are determined in the next subsection.
When κ\kappa, β\beta small, the hyperbolic tangent may be replaced by its (first order) Taylor expansion:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x˙​≈κ​γ​x≪1−κ​x−β​γ​(κ​x−β​ξttele)​1cosh2⁡(γ​α​σN​∫0te−α​(t−s)​ξsN​ds)+β​tanh⁡(γ​α​σN​∫0te−α​(t−s)​ξsN​ds)+σN​ξtN−σV​ξtV+𝒪​(β2).\dot{x}\overset{\kappa\gamma x\ll 1}{\approx}-\kappa x-\beta\gamma(\kappa x-\beta\xi^{\textup{tele}}\_{t})\frac{1}{\cosh^{2}(\gamma\alpha\sigma\_{N}\int\_{0}^{t}\mathrm{e}^{-\alpha(t-s)}\xi\_{s}^{N}\,\differential s)}+\beta\tanh(\gamma\alpha\sigma\_{N}\int\_{0}^{t}\mathrm{e}^{-\alpha(t-s)}\xi\_{s}^{N}\,\differential s)+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V}+\mathcal{O}(\beta^{2}). |  | (74) |

The term involving the hyperbolic cosine may be replaced by its average, owing to the fact that its argument is fast compared to xx. The expectation of said term is calculated in Eq. ([109](https://arxiv.org/html/2511.13277v1#A4.E109 "In D.2 Variance of the Process ‣ Appendix D Stationary Distribution for 𝛼≫{𝜅,𝛽} and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model")) later in this section via the Furutsu-Novikov Theorem and reads (XX is the argument of the cosh in the previous equation)

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨1cosh2⁡(X)⟩=2γ​σN​1π​α+𝒪​(1α3/2),\bigg\langle\frac{1}{\cosh^{2}(X)}\bigg\rangle=\frac{2}{\gamma\sigma\_{N}}\frac{1}{\sqrt{\pi\alpha}}+\mathcal{O}\left(\frac{1}{\alpha^{3/2}}\right), |  | (75) |

such that the equation can be approximated as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x˙\displaystyle\dot{x} | ≈−κ​x​(1+2​βσN​π​α)+2​β2σN​π​α​ξtele+β​tanh⁡(γ​α​σN​∫0te−α​(t−s)​ξsN​ds)+σN​ξtN−σV​ξtV\displaystyle\approx-\kappa x\left(1+\frac{2\beta}{\sigma\_{N}\sqrt{\pi\alpha}}\right)+\frac{2\beta^{2}}{\sigma\_{N}\sqrt{\pi\alpha}}\xi^{\textup{tele}}+\beta\tanh(\gamma\alpha\sigma\_{N}\int\_{0}^{t}\mathrm{e}^{-\alpha(t-s)}\xi\_{s}^{N}\,\differential s)+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V} |  | (76) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−κeff ​x+2​β2σN​π​α​ξtele+β​tanh⁡(γ​α​σN​∫0te−α​(t−s)​ξsN​ds)+σN​ξtN−σV​ξtV,where​κeff=κ​(1+2​Θπ),\displaystyle=-\kappa\_{\text{eff\,}}x+\frac{2\beta^{2}}{\sigma\_{N}\sqrt{\pi\alpha}}\xi^{\textup{tele}}+\beta\tanh(\gamma\alpha\sigma\_{N}\int\_{0}^{t}\mathrm{e}^{-\alpha(t-s)}\xi\_{s}^{N}\,\differential s)+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V},\,\,\text{where}\,\,\kappa\_{\text{eff}}=\kappa\left(1+\frac{2\Theta}{\sqrt{\pi}}\right), |  | (77) |

where we have introduced the notation Θ:=β/σN​α\Theta:=\beta/\sigma\_{N}\sqrt{\alpha}.

When γ​σN2↛0\gamma\sigma\_{N}^{2}\nrightarrow 0, while α≫κ>0\alpha\gg\kappa>0, the hyperbolic tangent term becomes an auto-correlated/coloured telegraphic noise, ξttele∈{±1}\xi^{\textup{tele}}\_{t}\in\{\pm 1\}. The auto-correlation decay will be inherited in a non-trivial way from the OU process, which is derived in the next subsection.

The mispricing Langevin equation, Eq.([D](https://arxiv.org/html/2511.13277v1#A4.Ex22 "Appendix D Stationary Distribution for 𝛼≫{𝜅,𝛽} and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model")), then reads

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x˙\displaystyle\dot{x} | =−κeff ​x+β​ξttele+2​β2σN​π​α​ξtele+σN​ξtN−σV​ξtV\displaystyle=-\kappa\_{\text{eff\,}}x+\beta\xi\_{t}^{\textup{tele}}+\frac{2\beta^{2}}{\sigma\_{N}\sqrt{\pi\alpha}}\xi^{\textup{tele}}+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V} |  | (78) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−κeff ​x+βeff ​ξttele+σN​ξtN−σV​ξtV,where​βeff =β​(1+2​Θπ).\displaystyle=-\kappa\_{\text{eff\,}}x+\beta\_{\text{eff\,}}\xi\_{t}^{\textup{tele}}+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V},\,\,\text{where}\,\,\beta\_{\text{eff\,}}=\beta\left(1+\frac{2\Theta}{\sqrt{\pi}}\right). |  | (79) |

This system has two potential steady states, x=±βeff κeff x=\pm\frac{\beta\_{\text{eff\,}}}{\kappa\_{\text{eff\,}}}, when disregarding white noise. So at x=±βeff κeff x=\pm\frac{\beta\_{\text{eff\,}}}{\kappa\_{\text{eff\,}}} the process (disregarding white noise) is stable when the telegraphic noise is ±βeff \pm\beta\_{\text{eff\,}} but it can get de-stabilised or perturbed by telegraphic noise of the opposite sign. Thus, the switching behaviour between the two possible states of the telegraphic process needs to be studied.

### D.1 Autocovariance Telegraphic Noise

In this section the autocovariance of the telegraphic noise will be derived.

First, let YtY\_{t} be the underlying OU-process. Henceforth, it is assumed that YY is stationary, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨Yt​Ys⟩∼e−α​|t−s|.\langle Y\_{t}Y\_{s}\rangle\sim\mathrm{e}^{-\alpha|t-s|}. |  | (80) |

Further, for the OU-process is a Gaussian process, Y∼𝒩​(0,σ22​α)Y\sim\mathcal{N}(0,\frac{\sigma^{2}}{2\alpha}), where in this section σ=γ​α​σN\sigma=\gamma\alpha\sigma\_{N} is the constant prefactor of the white noise within the hyperbolic tangent.
Further note that in this limit

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξttele=1⇔Yt>0.\xi\_{t}^{\textup{tele}}=1\quad\Leftrightarrow\quad Y\_{t}>0. |  | (81) |

Assuming t>0t>0 and ξstele=1\xi\_{s}^{\textup{tele}}=1, it follows that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨ξttele​ξstele⟩\displaystyle\langle\xi\_{t}^{\textup{tele}}\xi\_{s}^{\textup{tele}}\rangle | =ℙ​[ξttele=1|ξstele=1]−ℙ​[ξttele=1|ξstele=−1]\displaystyle=\mathbb{P}[\xi\_{t}^{\textup{tele}}=1|\xi\_{s}^{\textup{tele}}=1]-\mathbb{P}[\xi\_{t}^{\textup{tele}}=1|\xi\_{s}^{\textup{tele}}=-1] |  | (82) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =ℙ​[Yt>0​|Ys>​0]−ℙ​[Yt>0|Ys<0].\displaystyle=\mathbb{P}[Y\_{t}>0|Y\_{s}>0]-\mathbb{P}[Y\_{t}>0|Y\_{s}<0]. |  | (83) |

Using the result from the bivariate centered Gaussian distribution with correlation ρ\rho and variances σ1\sigma\_{1} and σ2\sigma\_{2}, that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​[Yt>0,Ys>0]=14+12​π​arcsin⁡(ρ)\displaystyle\mathbb{P}[Y\_{t}>0,\,Y\_{s}>0]=\frac{1}{4}+\frac{1}{2\pi}\arcsin(\rho) |  | (84) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​[Yt>0,Ys<0]=12​π​arccos⁡(ρ)\displaystyle\mathbb{P}[Y\_{t}>0,\,Y\_{s}<0]=\frac{1}{2\pi}\arccos(\rho) |  | (85) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​[Ys>0]=ℙ​[Ys<0]=12,\displaystyle\mathbb{P}[Y\_{s}>0]=\mathbb{P}[Y\_{s}<0]=\frac{1}{2}, |  | (86) |

and with arcsin⁡(x)−arccos⁡(x)=2​arcsin⁡(x)−π2\arcsin(x)-\arccos(x)=2\arcsin(x)-\frac{\pi}{2}, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ξttele​ξstele⟩=2​(14+12​π​(2​arcsin⁡(e−α​|t−s|)−π2))=2π​arcsin⁡(e−α​|t−s|).\langle\xi\_{t}^{\textup{tele}}\xi\_{s}^{\textup{tele}}\rangle=2\left(\frac{1}{4}+\frac{1}{2\pi}(2\arcsin(\mathrm{e}^{-\alpha|t-s|})-\frac{\pi}{2})\right)=\frac{2}{\pi}\arcsin(\mathrm{e}^{-\alpha|t-s|}). |  | (87) |

Thus, the switching rate between the two steady states scales ∼α/π\sim\alpha/\pi for large α\alpha. When κ≫λ\kappa\gg\lambda, where λ\lambda is the switching rate of the telegraphic noise, i.e. when the relaxation to the steady state is faster than the switching between the two modes, the dynamics
has enough time to relax to the steady states, resulting in two clearly distinguishable modes in distribution. In the opposite
case, when switching is in the same order of magnitude or even faster, the two modes of p​(x)p(x) become indistinguishable and are washed out by the noise. In the case where α≫κ∼λ\alpha\gg\kappa\sim\lambda, the distribution is thus unimodal and centered around x=0x=0 and Gaussian. Thus, we only need to calculate the second moment ⟨x2⟩\langle x^{2}\rangle to determine p​(x)p(x).

### D.2 Variance of the Process

The integrated version of the Langevin equation (using an integrating factor eκeff ​t\mathrm{e}^{\kappa\_{\text{eff\,}}t}) reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | x(t)=∫0te−κeff ​(t−s)[βeff ξstele+σNξsN−σVξsV]ds=:A(t)+B(t)+C(t),x(t)=\int\_{0}^{t}\mathrm{e}^{-\kappa\_{\text{eff\,}}(t-s)}\left[\beta\_{\text{eff\,}}\xi\_{s}^{\textup{tele}}+\sigma\_{N}\xi\_{s}^{N}-\sigma\_{V}\xi\_{s}^{V}\right]\,\differential s=:A(t)+B(t)+C(t), |  | (88) |

where the terms AA, BB, CC are defined by the three integrals.
The variance of the process is thus given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨x2⟩=⟨A2⟩+⟨B2⟩+⟨C2⟩+2​⟨A​B⟩=⟨A2⟩+σN2+σV22​κeff +2​⟨A​B⟩\langle x^{2}\rangle=\langle A^{2}\rangle+\langle B^{2}\rangle+\langle C^{2}\rangle+2\langle AB\rangle=\langle A^{2}\rangle+\frac{\sigma\_{N}^{2}+\sigma\_{V}^{2}}{2\kappa\_{\text{eff\,}}}+2\langle AB\rangle |  | (89) |

because all terms are centered.

Further, we know that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨A2⟩\displaystyle\langle A^{2}\rangle | =⟨∫0tβeff ​e−κeff ​(t−s)​ξstele​ds​∫0tβeff ​e−κeff ​(t−s′)​ξs′tele​ds′⟩\displaystyle=\langle\int\_{0}^{t}\beta\_{\text{eff\,}}\mathrm{e}^{-\kappa\_{\text{eff\,}}(t-s)}\xi\_{s}^{\textup{tele}}\,\differential s\int\_{0}^{t}\beta\_{\text{eff\,}}\mathrm{e}^{-\kappa\_{\text{eff\,}}(t-s^{\prime})}\xi\_{s^{\prime}}^{\textup{tele}}\,\differential s^{\prime}\rangle |  | (90) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫0t∫0tβeff 2​e−κeff ​(2​t−s−s′)​⟨ξstele​ξs′tele⟩​ds​ds′\displaystyle=\int\_{0}^{t}\int\_{0}^{t}\beta^{2}\_{\text{eff\,}}\mathrm{e}^{-\kappa\_{\text{eff\,}}(2t-s-s^{\prime})}\langle\xi\_{s}^{\textup{tele}}\xi\_{s^{\prime}}^{\textup{tele}}\rangle\,\differential s\differential s^{\prime} |  | (91) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫0t∫0tβeff 2​e−κeff ​(2​t−s−s′)​2π​arcsin⁡(e−α​|s′−s|)​ds​ds′.\displaystyle=\int\_{0}^{t}\int\_{0}^{t}\beta^{2}\_{\text{eff\,}}\mathrm{e}^{-\kappa\_{\text{eff\,}}(2t-s-s^{\prime})}\frac{2}{\pi}\arcsin(\mathrm{e}^{-\alpha|s^{\prime}-s|})\,\differential s\differential s^{\prime}. |  | (92) |

Defining u=t−su=t-s and u′=t−s′u^{\prime}=t-s^{\prime}, such that ds​ds′=du​du′\differential s\differential s^{\prime}=\differential u\differential u^{\prime}, the integral can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨A2⟩=2​βeff 2π​∫0t∫0te−κeff ​(u+u′)​arcsin⁡(e−α​|u′−u|)​du​du′,\langle A^{2}\rangle=\frac{2\beta^{2}\_{\text{eff\,}}}{\pi}\int\_{0}^{t}\int\_{0}^{t}\mathrm{e}^{-\kappa\_{\text{eff\,}}(u+u^{\prime})}\arcsin(\mathrm{e}^{-\alpha|u^{\prime}-u|})\,\differential u\,\differential u^{\prime}, |  | (93) |

which becomes the following in the long-time limit

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨A2⟩=2​βeff 2π​∫0∞∫0∞e−κeff ​(u+u′)​arcsin⁡(e−α​|u′−u|)​du​du′.\langle A^{2}\rangle=\frac{2\beta^{2}\_{\text{eff\,}}}{\pi}\int\_{0}^{\infty}\int\_{0}^{\infty}\mathrm{e}^{-\kappa\_{\text{eff\,}}(u+u^{\prime})}\arcsin(\mathrm{e}^{-\alpha|u^{\prime}-u|})\,\differential u\,\differential u^{\prime}. |  | (94) |

With new variables x=1/2​(u+u′)x=1/2(u+u^{\prime}) and y=1/2​(u−u′)y=1/2(u-u^{\prime}), such that u=x−yu=x-y, u′=x+yu^{\prime}=x+y and du​du′=2​dx​dy\differential u\,\differential u^{\prime}=2\differential x\,\differential y, the integral reads

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨A2⟩\displaystyle\langle A^{2}\rangle | =4​βeff 2π​∫0∞∫−xxe−2​κeff ​x​arcsin⁡(e−2​α​|y|)​dy​dx\displaystyle=\frac{4\beta^{2}\_{\text{eff\,}}}{\pi}\int\_{0}^{\infty}\int\_{-x}^{x}\mathrm{e}^{-2\kappa\_{\text{eff\,}}x}\arcsin(\mathrm{e}^{-2\alpha|y|})\,\differential y\,\differential x |  | (95) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =8​βeff 2π​∫0∞e−2​κeff ​x​(∫0xarcsin⁡(e−2​α​y)​dy)​dx,\displaystyle=\frac{8\beta^{2}\_{\text{eff\,}}}{\pi}\int\_{0}^{\infty}\mathrm{e}^{-2\kappa\_{\text{eff\,}}x}\left(\int\_{0}^{x}\arcsin(\mathrm{e}^{-2\alpha y})\,\differential y\right)\,\differential x, |  | (96) |

where the last step holds because the arcsine is even in yy. The integral bounds have changed because u,u′∈[0,∞)u,u^{\prime}\in[0,\,\infty), so u=x−y≥0u=x-y\geq 0 and u′=x+y≥0u^{\prime}=x+y\geq 0 requires |y|≤x|y|\leq x, such that finally x∈[0,∞)x\in[0,\,\infty) and y∈[−x,x]y\in[-x,x].
Changing the order of integration, one finds

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨A2⟩\displaystyle\langle A^{2}\rangle | =8​βeff 2π​∫0∞arcsin⁡(e−2​α​y)​(∫y∞e−2​κeff ​x​dx)​dy\displaystyle=\frac{8\beta^{2}\_{\text{eff\,}}}{\pi}\int\_{0}^{\infty}\arcsin(\mathrm{e}^{-2\alpha y})\left(\int\_{y}^{\infty}\mathrm{e}^{-2\kappa\_{\text{eff\,}}x}\,\differential x\right)\,\differential y |  | (97) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =4​βeff 2π​κeff ​∫0∞arcsin⁡(e−2​α​y)​e−2​κeff ​y​dy\displaystyle=\frac{4\beta^{2}\_{\text{eff\,}}}{\pi\kappa\_{\text{eff\,}}}\int\_{0}^{\infty}\arcsin(\mathrm{e}^{-2\alpha y})\mathrm{e}^{-2\kappa\_{\text{eff\,}}y}\,\differential y |  | (98) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =4​βeff 2π​κeff ​π4​κeff ​(π−Γ​(α+κeff 2​α)Γ​(2​α+κeff 2​α))=βeff 2π​κeff 2​(π−Γ​(α+κeff 2​α)Γ​(2​α+κeff 2​α)).\displaystyle=\frac{4\beta^{2}\_{\text{eff\,}}}{\pi\kappa\_{\text{eff\,}}}\frac{\sqrt{\pi}}{4\kappa\_{\text{eff\,}}}\left(\sqrt{\pi}-\frac{\Gamma(\frac{\alpha+\kappa\_{\text{eff\,}}}{2\alpha})}{\Gamma(\frac{2\alpha+\kappa\_{\text{eff\,}}}{2\alpha})}\right)=\frac{\beta^{2}\_{\text{eff\,}}}{\sqrt{\pi}\kappa\_{\text{eff\,}}^{2}}\left(\sqrt{\pi}-\frac{\Gamma(\frac{\alpha+\kappa\_{\text{eff\,}}}{2\alpha})}{\Gamma(\frac{2\alpha+\kappa\_{\text{eff\,}}}{2\alpha})}\right). |  | (99) |

The last outstanding term is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨A​B⟩=⟨∫0te−κeff ​(t−s)​βeff ​ξstele​ds​∫0te−κeff ​(t−s′)​σN​ξs′N​ds′⟩.\langle AB\rangle=\big\langle\int\_{0}^{t}\mathrm{e}^{-\kappa\_{\text{eff\,}}(t-s)}\beta\_{\text{eff\,}}\xi\_{s}^{\textup{tele}}\,\differential s\int\_{0}^{t}\mathrm{e}^{-\kappa\_{\text{eff\,}}(t-s^{\prime})}\sigma\_{N}\xi\_{s^{\prime}}^{N}\,\differential s^{\prime}\big\rangle. |  | (100) |

In order to calculate the covariance, we write the telegraphic noise again in its non-simplified form using the hyperbolic tangent:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨A​B⟩=∫0t∫0te−κeff ​(2​t−s−s′)​βeff ​σN​⟨tanh⁡(γ​α​σN​∫0se−α​(s−r)​ξrN​dr)​ξs′N⟩​ds′​ds\langle AB\rangle=\int\_{0}^{t}\int\_{0}^{t}\mathrm{e}^{-\kappa\_{\text{eff\,}}(2t-s-s^{\prime})}\beta\_{\text{eff\,}}\sigma\_{N}\langle\tanh(\gamma\alpha\sigma\_{N}\int\_{0}^{s}\mathrm{e}^{-\alpha(s-r)}\xi\_{r}^{N}\,\differential r)\xi\_{s^{\prime}}^{N}\rangle\,\differential s^{\prime}\,\differential s |  | (101) |

The expectation is over a functional of the white noise ξtN\xi\_{t}^{N} multiplied by the same noise. For such expectations, the Novikov theorem holds, which states for a functional ℱ​[η]\mathcal{F}[\eta] of some Gaussian noise ηt\eta\_{t} that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ℱ​[η]​ηt⟩=∫⟨δ​ℱδ​ηs⟩​⟨ηs​ηt⟩​ds,\langle\mathcal{F}[\eta]\eta\_{t}\rangle=\int\langle\frac{\delta\mathcal{F}}{\delta\eta\_{s}}\rangle\langle\eta\_{s}\eta\_{t}\rangle\,\differential s, |  | (102) |

where δ\delta in this expression refers to the functional derivative ishimaru1978wave.
In the case of Gaussian white noise, i.e. ⟨ηs​ηt⟩=δ​(s−t)\langle\eta\_{s}\eta\_{t}\rangle=\delta(s-t) (in this term δ\delta is the Dirac-delta), the theorem simplifies to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨ℱ​[η]​ηt⟩=⟨δ​ℱδ​ηt⟩.\langle\mathcal{F}[\eta]\eta\_{t}\rangle=\bigg\langle\frac{\delta\mathcal{F}}{\delta\eta\_{t}}\bigg\rangle. |  | (103) |

Let us define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xs​[ξN]=γ​α​σN​∫0se−α​(s−r)​ξrN​dr,X\_{s}[\xi^{N}]=\gamma\alpha\sigma\_{N}\int\_{0}^{s}\mathrm{e}^{-\alpha(s-r)}\xi\_{r}^{N}\,\differential r, |  | (104) |

such that ℱ​[ξN]=tanh⁡(Xs​[ξN])\mathcal{F}[\xi^{N}]=\tanh(X\_{s}[\xi^{N}]). The functional derivative then is

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​ℱ​[ξ]δ​ξs′N=dtanh⁡(Xs)dXs​δ​Xsδ​ξs′N=(1−tanh2⁡(Xs))​δ​Xsδ​ξs′N=1cosh2⁡(Xs)​α​γ​σN​e−α​(s−s′)​Θ​(s−s′).\frac{\delta\mathcal{F}[\xi]}{\delta\xi\_{s^{\prime}}^{N}}=\frac{\differential\tanh(X\_{s})}{\differential X\_{s}}\frac{\delta X\_{s}}{\delta\xi\_{s^{\prime}}^{N}}=(1-\tanh^{2}(X\_{s}))\frac{\delta X\_{s}}{\delta\xi\_{s^{\prime}}^{N}}=\frac{1}{\cosh^{2}(X\_{s})}\alpha\gamma\sigma\_{N}\mathrm{e}^{-\alpha(s-s^{\prime})}\Theta(s-s^{\prime}). |  | (105) |

Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨δ​ℱ​[ξ]δ​ξs′N⟩∼⟨1cosh2⁡(Xs)⟩\bigg\langle\frac{\delta\mathcal{F}[\xi]}{\delta\xi\_{s^{\prime}}^{N}}\bigg\rangle\sim\bigg\langle\frac{1}{\cosh^{2}(X\_{s})}\bigg\rangle |  | (106) |

and that XX is a Gaussian process, which converges to 𝒩​(0,w)\mathcal{N}(0,w) in distribution, where in the stationary limit w=γ2​α​σN22w=\frac{\gamma^{2}\alpha\sigma\_{N}^{2}}{2} is the stationary variance.
Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨1cosh2⁡(X)⟩=12​π​w​∫−∞∞e−X22​w​1cosh2⁡(X)​dX.\bigg\langle\frac{1}{\cosh^{2}(X)}\bigg\rangle=\frac{1}{\sqrt{2\pi w}}\int\_{-\infty}^{\infty}\mathrm{e}^{\frac{-X^{2}}{2w}}\frac{1}{\cosh^{2}(X)}\,\differential X. |  | (107) |

In the large-ww limit, which is the case considered in this section, the integral is dominated by X=𝒪​(1)X=\mathcal{O}(1) because of cosh−2⁡(X)\cosh^{-2}(X). Consequently X2/(2​w)≪1X^{2}/(2w)\ll 1, such that the exponential term may be approximated by its Taylor series:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨1cosh2⁡(Xs)⟩≈12​π​w​∫−∞∞(1−X22​w+…)​1cosh2⁡(Xs)​dX.\bigg\langle\frac{1}{\cosh^{2}(X\_{s})}\bigg\rangle\approx\frac{1}{\sqrt{2\pi w}}\int\_{-\infty}^{\infty}\left(1-\frac{X^{2}}{2w}+\dots\right)\frac{1}{\cosh^{2}(X\_{s})}\,\differential X. |  | (108) |

Keeping only the leading order, this results in

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨1cosh2⁡(Xs)⟩=12​π​w​∫−∞∞1cosh2⁡(X)​dX+𝒪​(1w3/2)=2π​w+𝒪​(1w3/2)=2γ​σN​1π​α+𝒪​(1w3/2).\bigg\langle\frac{1}{\cosh^{2}(X\_{s})}\bigg\rangle=\frac{1}{\sqrt{2\pi w}}\int\_{-\infty}^{\infty}\frac{1}{\cosh^{2}(X)}\,\differential X+\mathcal{O}\left(\frac{1}{w^{3/2}}\right)=\sqrt{\frac{2}{\pi w}}+\mathcal{O}\left(\frac{1}{w^{3/2}}\right)=\frac{2}{\gamma\sigma\_{N}}\frac{1}{\sqrt{\pi\alpha}}+\mathcal{O}\left(\frac{1}{w^{3/2}}\right). |  | (109) |

Consequently, the Furutsu-Novikov theorem yields approximately

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨δ​ℱ​[ξ]δ​ξs′N⟩≈2γ​σN​1π​α​α​γ​σN​e−α​(s−s′)​Θ​(s−s′)=2​απ​e−α​(s−s′)​Θ​(s−s′),\bigg\langle\frac{\delta\mathcal{F}[\xi]}{\delta\xi\_{s^{\prime}}^{N}}\bigg\rangle\approx\frac{2}{\gamma\sigma\_{N}}\frac{1}{\sqrt{\pi\alpha}}\alpha\gamma\sigma\_{N}\mathrm{e}^{-\alpha(s-s^{\prime})}\Theta(s-s^{\prime})=2\sqrt{\frac{\alpha}{\pi}}\mathrm{e}^{-\alpha(s-s^{\prime})}\Theta(s-s^{\prime}), |  | (110) |

which renders the cross-correlation to be

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨A​B⟩≈2​βeff ​σN​απ​∫0t∫0te−κeff ​(2​t−s−s′)​e−α​(s−s′)​Θ​(s−s′)​ds​ds′.\langle AB\rangle\approx 2\beta\_{\text{eff\,}}\sigma\_{N}\sqrt{\frac{\alpha}{\pi}}\int\_{0}^{t}\int\_{0}^{t}\mathrm{e}^{-\kappa\_{\text{eff\,}}(2t-s-s^{\prime})}\mathrm{e}^{-\alpha(s-s^{\prime})}\Theta(s-s^{\prime})\,\differential s\,\differential s^{\prime}. |  | (111) |

Using the same substitution for uu, u′u^{\prime} as for the term ⟨A2⟩\langle A^{2}\rangle and taking again the stationary limit t→∞t\to\infty, leads to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ⟨A​B⟩\displaystyle\langle AB\rangle | ≈2​βeff ​σN​απ​∫0∞∫0∞e−κeff ​(u+u′)​e−α​(u−u′)​Θ​(u−u′)​du′​du\displaystyle\approx 2\beta\_{\text{eff\,}}\sigma\_{N}\sqrt{\frac{\alpha}{\pi}}\int\_{0}^{\infty}\int\_{0}^{\infty}\mathrm{e}^{-\kappa\_{\text{eff\,}}(u+u^{\prime})}\mathrm{e}^{-\alpha(u-u^{\prime})}\Theta(u-u^{\prime})\,\differential u^{\prime}\,\differential u |  | (112) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2​βeff ​σN​απ​∫0∞∫0ue−u​(κeff +α)​eu′​(α−κeff )​du′​du\displaystyle=2\beta\_{\text{eff\,}}\sigma\_{N}\sqrt{\frac{\alpha}{\pi}}\int\_{0}^{\infty}\int\_{0}^{u}\mathrm{e}^{-u(\kappa\_{\text{eff\,}}+\alpha)}\mathrm{e}^{u^{\prime}(\alpha-\kappa\_{\text{eff\,}})}\,\differential u^{\prime}\,\differential u |  | (113) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2​βeff ​σN​απ​1α−κeff ​∫0∞e−u​(κeff +α)​(eu​(α−κeff )−1)​du\displaystyle=2\beta\_{\text{eff\,}}\sigma\_{N}\sqrt{\frac{\alpha}{\pi}}\frac{1}{\alpha-\kappa\_{\text{eff\,}}}\int\_{0}^{\infty}\mathrm{e}^{-u(\kappa\_{\text{eff\,}}+\alpha)}\left(\mathrm{e}^{u(\alpha-\kappa\_{\text{eff\,}})}-1\right)\,\differential u |  | (114) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2​βeff ​σN​απ​1α−κeff ​∫0∞(e−2​u​κeff −e−u​(α+κeff ))​du\displaystyle=2\beta\_{\text{eff\,}}\sigma\_{N}\sqrt{\frac{\alpha}{\pi}}\frac{1}{\alpha-\kappa\_{\text{eff\,}}}\int\_{0}^{\infty}\left(\mathrm{e}^{-2u\kappa\_{\text{eff\,}}}-\mathrm{e}^{-u(\alpha+\kappa\_{\text{eff\,}})}\right)\,\differential u |  | (115) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =2​βeff ​σN​απ​1α−κeff ​(12​κeff −1α+κeff )\displaystyle=2\beta\_{\text{eff\,}}\sigma\_{N}\sqrt{\frac{\alpha}{\pi}}\frac{1}{\alpha-\kappa\_{\text{eff\,}}}\left(\frac{1}{2\kappa\_{\text{eff\,}}}-\frac{1}{\alpha+\kappa\_{\text{eff\,}}}\right) |  | (116) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =βeff ​σN​απ​1κeff ​(α+κeff ).\displaystyle=\beta\_{\text{eff\,}}\sigma\_{N}\sqrt{\frac{\alpha}{\pi}}\frac{1}{\kappa\_{\text{eff\,}}(\alpha+\kappa\_{\text{eff\,}})}. |  | (117) |

Knowing this, the variance of the process xx is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨x2⟩=⟨A2⟩+⟨B2⟩+⟨C2⟩+2​⟨A​B⟩.\langle x^{2}\rangle=\langle A^{2}\rangle+\langle B^{2}\rangle+\langle C^{2}\rangle+2\langle AB\rangle. |  | (118) |

This concludes our derivation of the stationary distribution in the case where α​γ2​σN2\alpha\gamma^{2}\sigma\_{N}^{2} is large and α≫κ\alpha\gg\kappa, which reads

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | p​(x)\displaystyle p(x) | =𝒩​(0,⟨x2⟩)=𝒩​(0,σN2+σV22​κeff +βeff 2π​κeff 2​(π−Γ​(α+κeff 2​α)Γ​(2​α+κeff 2​α))+2​βeff ​σN​απ​1κeff ​(α+κeff ))\displaystyle=\mathcal{N}(0,\,\langle x^{2}\rangle)=\mathcal{N}\left(0,\,\frac{\sigma\_{N}^{2}+\sigma\_{V}^{2}}{2\kappa\_{\text{eff\,}}}+\frac{\beta\_{\text{eff\,}}^{2}}{\sqrt{\pi}\kappa\_{\text{eff\,}}^{2}}\left(\sqrt{\pi}-\frac{\Gamma(\frac{\alpha+\kappa\_{\text{eff\,}}}{2\alpha})}{\Gamma(\frac{2\alpha+\kappa\_{\text{eff\,}}}{2\alpha})}\right)+2\beta\_{\text{eff\,}}\sigma\_{N}\sqrt{\frac{\alpha}{\pi}}\frac{1}{\kappa\_{\text{eff\,}}(\alpha+\kappa\_{\text{eff\,}})}\right) |  | (119) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝒩​(0,σN2+σV22​κeff +β2π​κ2​(π−Γ​(α+κeff 2​α)Γ​(2​α+κeff 2​α))+2​β​σN​απ​1κ​(α+κeff )),\displaystyle=\mathcal{N}\left(0,\,\frac{\sigma\_{N}^{2}+\sigma\_{V}^{2}}{2\kappa\_{\text{eff\,}}}+\frac{\beta^{2}}{\sqrt{\pi}\kappa^{2}}\left(\sqrt{\pi}-\frac{\Gamma(\frac{\alpha+\kappa\_{\text{eff\,}}}{2\alpha})}{\Gamma(\frac{2\alpha+\kappa\_{\text{eff\,}}}{2\alpha})}\right)+2\beta\sigma\_{N}\sqrt{\frac{\alpha}{\pi}}\frac{1}{\kappa(\alpha+\kappa\_{\text{eff\,}})}\right), |  | (120) |

where 𝒩\mathcal{N} refers to the Gaussian distribution and, again,

|  |  |  |  |
| --- | --- | --- | --- |
|  | κeff =κ​(1+2​βσN​π​α)​and​βeff =β​(1+2​βσN​π​α).\kappa\_{\text{eff\,}}=\kappa\left(1+\frac{2\beta}{\sigma\_{N}\sqrt{\pi\alpha}}\right)\quad\text{and}\quad\beta\_{\text{eff\,}}=\beta\left(1+\frac{2\beta}{\sigma\_{N}\sqrt{\pi\alpha}}\right). |  | (121) |

Keeping only terms up to quadratic order in β\beta, this finally leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(x)\displaystyle p(x) | =𝒩​(0,σN2+σV22​κeff +β2π​κ2​(π−π​(1−ln⁡(2)​κα))+2​β​σN​απ​1κ​(α+κeff )+𝒪​(β3))\displaystyle=\mathcal{N}\left(0,\,\frac{\sigma\_{N}^{2}+\sigma\_{V}^{2}}{2\kappa\_{\text{eff\,}}}+\frac{\beta^{2}}{\sqrt{\pi}\kappa^{2}}\left(\sqrt{\pi}-\sqrt{\pi}(1-\frac{\ln(2)\kappa}{\alpha})\right)+2\beta\sigma\_{N}\sqrt{\frac{\alpha}{\pi}}\frac{1}{\kappa(\alpha+\kappa\_{\text{eff\,}})}+\mathcal{O}(\beta^{3})\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝒩​(0,σN2+σV22​κeff +ln⁡(2)​β2κ​α+2​β​σN​απ​1κ​(α+κeff )+𝒪​(β3)),\displaystyle=\mathcal{N}\left(0,\,\frac{\sigma\_{N}^{2}+\sigma\_{V}^{2}}{2\kappa\_{\text{eff\,}}}+\frac{\ln(2)\beta^{2}}{\kappa\alpha}+2\beta\sigma\_{N}\sqrt{\frac{\alpha}{\pi}}\frac{1}{\kappa(\alpha+\kappa\_{\text{eff\,}})}+\mathcal{O}(\beta^{3})\right), |  | (122) |

which is justified by the Taylor expansion involving the fractions of Gamma-functions in the following subsection.

### D.3 Leading orders of ⟨A2⟩\langle A^{2}\rangle

We have found (in the limit α≫κ\alpha\gg\kappa) the closed-form solution

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨A2⟩=β2π​κ2​(π−Γ​(α+κeff2​α)Γ​(2​α+κeff2​α)).\langle A^{2}\rangle=\frac{\beta^{2}}{\sqrt{\pi}\kappa^{2}}\left(\sqrt{\pi}-\frac{\Gamma(\frac{\alpha+\kappa\_{\text{eff}}}{2\alpha})}{\Gamma(\frac{2\alpha+\kappa\_{\text{eff}}}{2\alpha})}\right). |  | (123) |

Let us determine the leading order in Γ\Gamma when α≫κ\alpha\gg\kappa.

Defining ϵ=κ2​α\epsilon=\frac{\kappa}{2\alpha}, the argument of the Gamma-fuction in the numerator is 12+ϵ\frac{1}{2}+\epsilon and of the denominator 1+ϵ1+\epsilon. ϵ≪1\epsilon\ll 1 when α≫κ\alpha\gg\kappa, such that the expansions of the Gamma-function near 1 and 1/21/2 may be used:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Γ​(1+ϵ)\displaystyle\Gamma(1+\epsilon) | =1−γ~​ϵ+𝒪​(ϵ2),\displaystyle=1-\tilde{\gamma}\epsilon+\mathcal{O}(\epsilon^{2}), |  | (124) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Γ​(1/2+ϵ)\displaystyle\Gamma(1/2+\epsilon) | =Γ​(12)⏟=π​(1+Ψ​(12)​ϵ+𝒪​(ϵ2))=π​(1−(γ~+2​ln⁡(2))​ϵ+𝒪​(ϵ2)),\displaystyle=\underbrace{\Gamma(\frac{1}{2})}\_{=\sqrt{\pi}}\left(1+\Psi(\frac{1}{2})\epsilon+\mathcal{O}(\epsilon^{2})\right)=\sqrt{\pi}\left(1-(\tilde{\gamma}+2\ln(2))\epsilon+\mathcal{O}(\epsilon^{2})\right), |  | (125) |

where γ~\tilde{\gamma} is the Euler-Mascheroni constant and Ψ\Psi the digamma function. Ψ\Psi is connected to Γ\Gamma via its derivative: ddx​Γ​(x)=Γ​(x)​Ψ​(x)\frac{\differential}{\differential x}\Gamma(x)=\Gamma(x)\Psi(x). It is Ψ​(1)=−γ~\Psi(1)=-\tilde{\gamma} and Ψ​(1/2)=−γ~−2​ln⁡(2)\Psi(1/2)=-\tilde{\gamma}-2\ln(2).

Taking the ratio

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ​(1/2+ϵ)Γ​(1+ϵ)≈π​(1−(γ~+2​ln⁡(2))​ϵ)1−γ~​ϵ\frac{\Gamma(1/2+\epsilon)}{\Gamma(1+\epsilon)}\approx\frac{\sqrt{\pi}(1-(\tilde{\gamma}+2\ln(2))\epsilon)}{1-\tilde{\gamma}\epsilon} |  | (126) |

and using the first-order approximation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1−a​ϵ1−b​ϵ≈1+(b−a)​ϵ,\frac{1-a\epsilon}{1-b\epsilon}\approx 1+(b-a)\epsilon, |  | (127) |

leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ​(1/2+ϵ)Γ​(1+ϵ)=π​(1−2​ln⁡(2)​ϵ)+𝒪​(ϵ2)=π​(1−ln⁡(2)​κeffα)+𝒪​(ϵ2).\frac{\Gamma(1/2+\epsilon)}{\Gamma(1+\epsilon)}=\sqrt{\pi}\left(1-2\ln(2)\epsilon\right)+\mathcal{O}(\epsilon^{2})=\sqrt{\pi}\left(1-\frac{\ln(2)\kappa\_{\text{eff}}}{\alpha}\right)+\mathcal{O}(\epsilon^{2}). |  | (128) |

## Appendix E Stationary Distribution for α,β≫κ\alpha,\,\beta\gg\kappa and γ​σN2↛0\gamma\sigma\_{N}^{2}\nrightarrow 0

In this section, we motivate and derive another result in the limit, where both α≫κ\alpha\gg\kappa (as in the previous section) but also β≫κ\beta\gg\kappa (while γ​σN2↛0\gamma\sigma\_{N}^{2}\nrightarrow 0 for the calculation to hold). In this limit, because β≫κ\beta\gg\kappa, the trend signal distribution p​(M)p(M) is bimodal. However, unlike claims in the literature this does not automatically imply a bimodality of the mispricing distribution p​(δ)p(\delta). p​(M)p(M) in this limit is derived here and a motivation for the P-bifurcation of the mispricing distribution p​(δ)p(\delta) that is bimodal only ’later’, i.e. for even larger values of β\beta, is given.

Recall the change of variables stated in Appendix [B](https://arxiv.org/html/2511.13277v1#A2 "Appendix B Change of Variables ‣ Stationary Distributions of the Mode-switching Chiarella Model"), M=y+α​xM=y+\alpha x, from which it follows using eq. ([41](https://arxiv.org/html/2511.13277v1#A2.E41 "In Appendix B Change of Variables ‣ Stationary Distributions of the Mode-switching Chiarella Model")) and eq. ([45](https://arxiv.org/html/2511.13277v1#A2.E45 "In Appendix B Change of Variables ‣ Stationary Distributions of the Mode-switching Chiarella Model")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | x˙\displaystyle\dot{x} | =−κ​x+β​tanh⁡(γ​M)+σN​ξtN−σV​ξtV\displaystyle=-\kappa x+\beta\tanh(\gamma M)+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | M˙\displaystyle\dot{M} | =y˙+α​x˙\displaystyle=\dot{y}+\alpha\dot{x} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−α​M+α​σV​ξtV+α​(κ​x+β​tanh⁡(γ​M)+σN​ξtN−σV​ξtV)\displaystyle=-\alpha M+\alpha\sigma\_{V}\xi\_{t}^{V}+\alpha(\kappa x+\beta\tanh(\gamma M)+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−α​M+α​κ​x+α​β​tanh⁡(γ​M)+α​σN​ξtN\displaystyle=-\alpha M+\alpha\kappa x+\alpha\beta\tanh(\gamma M)+\alpha\sigma\_{N}\xi\_{t}^{N} |  | (129) |

#### E.0.1 Quasi-static Assumption for xx

Owing to the fact that α≫κ\alpha\gg\kappa, MM relaxes on time scales much faster than xx, such that a quasi-static assumption for xx is justified relative to MM (we will show in the next section, why and when this assumption breaks down when β\beta is increased). The following conditional Fokker-Planck equation can be written down:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂p​(M|x)∂t=−∂∂M​[(−α​M+α​κ​x+α​β​tanh⁡(γ​M))​p​(M|x)]+σN2​α22​∂2p​(M|x)∂M2.\frac{\partial p(M|x)}{\partial t}=-\frac{\partial}{\partial M}\left[(-\alpha M+\alpha\kappa x+\alpha\beta\tanh(\gamma M))p(M|x)\right]+\frac{\sigma\_{N}^{2}\alpha^{2}}{2}\frac{\partial^{2}p(M|x)}{\partial M^{2}}. |  | (130) |

The stationary solution (∂p​(M|x)∂t=0\frac{\partial p(M|x)}{\partial t}=0) is given through the Maxwell-Boltzmann ansatz and reads

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | p​(M|x)\displaystyle p(M|x) | =1A​(x)​exp⁡(2σN2​α2​(−α2​M2+α​κ​M​x+α​βγ​ln⁡(cosh⁡(γ​M))))\displaystyle=\frac{1}{A(x)}\exp\left(\frac{2}{\sigma\_{N}^{2}\alpha^{2}}(-\frac{\alpha}{2}M^{2}+\alpha\kappa Mx+\frac{\alpha\beta}{\gamma}\ln(\cosh(\gamma M)))\right) |  | (131) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1A​(x)​cosh⁡(γ​M)2​βσN2​α​γ​e−1σN2​α​M2+2​κσN2​α​M​x,\displaystyle=\frac{1}{A(x)}\cosh(\gamma M)^{\frac{2\beta}{\sigma\_{N}^{2}\alpha\gamma}}\,\mathrm{e}^{-\frac{1}{\sigma\_{N}^{2}\alpha}M^{2}+\frac{2\kappa}{\sigma\_{N}^{2}\alpha}Mx}, |  | (132) |

where A​(x)A(x) is the normalisation. Note that for x=0x=0, p​(M|x)p(M|x) becomes bimodal when β​γ>1\beta\gamma>1.

Assuming that this stationary distribution is reached very quickly, such that xx hardly moves, one can make progress and compute how the dynamics of xx itself is affected by the trend MM. Within this quasi-static assumption, we can replace the hyperbolic tangent term by its expectation in the Langevin evolution of xx:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x˙≈−κ​x+β​(𝔼​[tanh⁡(γ​M)|x]+ξ~ttele)+σN​ξtN−σV​ξtV,\dot{x}\approx-\kappa x+\beta(\mathbb{E}[\tanh(\gamma M)|x]+\tilde{\xi}\_{t}^{\text{tele}})+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V}, |  | (133) |

where the telegraphic noise ξttele\xi\_{t}^{\text{tele}} has been separated into its mean

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[tanh⁡(γ​M)|x]\displaystyle\mathbb{E}[\tanh(\gamma M)|x] | =∫−∞∞p​(M|x)​tanh⁡(γ​M)​dM\displaystyle=\int\_{-\infty}^{\infty}p(M|x)\tanh(\gamma M)\,\mathrm{d}M |  | (134) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1A​(x)​∫−∞∞cosh⁡(γ​M)2​βσN2​α​γ​exp⁡(−1σN2​α​M2+2​κσN2​α​M​x)​tanh⁡(γ​M)​dM.\displaystyle=\frac{1}{A(x)}\int\_{-\infty}^{\infty}\cosh(\gamma M)^{\frac{2\beta}{\sigma\_{N}^{2}\alpha\gamma}}\exp\left(-\frac{1}{\sigma\_{N}^{2}\alpha}M^{2}+\frac{2\kappa}{\sigma\_{N}^{2}\alpha}Mx\right)\tanh(\gamma M)\,\mathrm{d}M. |  | (135) |

and a mean-zero contribution ξ~ttele\tilde{\xi}\_{t}^{\text{tele}} with variance β2\beta^{2}.

The normalisation A​(x)A(x) reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(x)=∫−∞∞cosh⁡(γ​M)2​βσN2​α​γ​e−1σN2​α​M2+2​κσN2​α​M​x​dM.A(x)=\int\_{-\infty}^{\infty}\cosh(\gamma M)^{\frac{2\beta}{\sigma\_{N}^{2}\alpha\gamma}}\,\mathrm{e}^{-\frac{1}{\sigma\_{N}^{2}\alpha}M^{2}+\frac{2\kappa}{\sigma\_{N}^{2}\alpha}Mx}\,\mathrm{d}M. |  | (136) |

Now, after making the change of variable M=σN​α​uM=\sigma\_{N}\sqrt{\alpha}u one can see that when γ​σN​α≫1\gamma\sigma\_{N}\sqrt{\alpha}\gg 1, which we will assume henceforth,
one can replace in the integral cosh⁡(γ​M)\cosh(\gamma M) by exp⁡(γ​|M|)/2\exp(\gamma|M|)/2, up to a correction of order (γ​σN​α)−1(\gamma\sigma\_{N}\sqrt{\alpha})^{-1} in the final result:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(x)\displaystyle A(x) | ≈(12)2​βσN2​α​γ​∫−∞∞e2​βσN2​α​|M|​e−1σN2​α​M2+2​κσN2​α​M​x​dM\displaystyle\approx\left(\frac{1}{2}\right)^{\frac{2\beta}{\sigma\_{N}^{2}\alpha\gamma}}\int\_{-\infty}^{\infty}\mathrm{e}^{\frac{2\beta}{\sigma\_{N}^{2}\alpha}|M|}\,\mathrm{e}^{-\frac{1}{\sigma\_{N}^{2}\alpha}M^{2}+\frac{2\kappa}{\sigma\_{N}^{2}\alpha}Mx}\,\mathrm{d}M |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(12)2​βσN2​α​γ+1​α​σN2​π​[e(β+x​κ)2α​σN2​(1+erf⁡(β+x​κα​σN))+e(β−x​κ)2α​σN2​(1+erf⁡(β−x​κα​σN))]\displaystyle=\left(\frac{1}{2}\right)^{\frac{2\beta}{\sigma\_{N}^{2}\alpha\gamma}+1}\sqrt{\alpha\sigma\_{N}^{2}\pi}\left[\mathrm{e}^{\frac{(\beta+x\kappa)^{2}}{\alpha\sigma\_{N}^{2}}}\left(1+\erf(\frac{\beta+x\kappa}{\sqrt{\alpha}\sigma\_{N}})\right)+\mathrm{e}^{\frac{(\beta-x\kappa)^{2}}{\alpha\sigma\_{N}^{2}}}\left(1+\erf(\frac{\beta-x\kappa}{\sqrt{\alpha}\sigma\_{N}})\right)\right] |  | (137) |

Using the same approximations, the expectation 𝔼​[tanh⁡(γ​M)]\mathbb{E}[\tanh(\gamma M)] is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[tanh⁡(γ​M)|x]\displaystyle\mathbb{E}[\tanh(\gamma M)|x] | ≈1A​(x)​(12)2​βσN2​α​γ​∫−∞∞e2​βσN2​α​|M|​e−1σN2​α​M2+2​κσN2​α​M​x​sgn​(M)​dM\displaystyle\approx\frac{1}{A(x)}\left(\frac{1}{2}\right)^{\frac{2\beta}{\sigma\_{N}^{2}\alpha\gamma}}\int\_{-\infty}^{\infty}\mathrm{e}^{\frac{2\beta}{\sigma\_{N}^{2}\alpha}|M|}\,\mathrm{e}^{-\frac{1}{\sigma\_{N}^{2}\alpha}M^{2}+\frac{2\kappa}{\sigma\_{N}^{2}\alpha}Mx}\mathrm{sgn}(M)\,\mathrm{d}M |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1A​(x)​(12)2​βσN2​α​γ+1​α​σN2​π​[e(β+x​κ)2α​σN2​(1+erf⁡(β+x​κα​σN))−e(β−x​κ)2α​σN2​(1+erf⁡(β−x​κα​σN))]\displaystyle=\frac{1}{A(x)}\left(\frac{1}{2}\right)^{\frac{2\beta}{\sigma\_{N}^{2}\alpha\gamma}+1}\sqrt{\alpha\sigma\_{N}^{2}\pi}\left[\mathrm{e}^{\frac{(\beta+x\kappa)^{2}}{\alpha\sigma\_{N}^{2}}}\left(1+\erf(\frac{\beta+x\kappa}{\sqrt{\alpha}\sigma\_{N}})\right)-\mathrm{e}^{\frac{(\beta-x\kappa)^{2}}{\alpha\sigma\_{N}^{2}}}\left(1+\erf(\frac{\beta-x\kappa}{\sqrt{\alpha}\sigma\_{N}})\right)\right] |  | (138) |

Plugging in the normalisation, we find

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[tanh⁡(γ​M)|x]≈e2​x​β​κα​σN2​(1+erf⁡(β+x​κα​σN))−e−2​x​β​κα​σN2​(1+erf⁡(β−x​κα​σN))e2​x​β​κα​σN2​(1+erf⁡(β+x​κα​σN))+e−2​x​β​κα​σN2​(1+erf⁡(β−x​κα​σN))\mathbb{E}[\tanh(\gamma M)|x]\approx\frac{\mathrm{e}^{\frac{2x\beta\kappa}{\alpha\sigma\_{N}^{2}}}\left(1+\erf(\frac{\beta+x\kappa}{\sqrt{\alpha}\sigma\_{N}})\right)-\mathrm{e}^{-\frac{2x\beta\kappa}{\alpha\sigma\_{N}^{2}}}\left(1+\erf(\frac{\beta-x\kappa}{\sqrt{\alpha}\sigma\_{N}})\right)}{\mathrm{e}^{\frac{2x\beta\kappa}{\alpha\sigma\_{N}^{2}}}\left(1+\erf(\frac{\beta+x\kappa}{\sqrt{\alpha}\sigma\_{N}})\right)+\mathrm{e}^{-\frac{2x\beta\kappa}{\alpha\sigma\_{N}^{2}}}\left(1+\erf(\frac{\beta-x\kappa}{\sqrt{\alpha}\sigma\_{N}})\right)} |  | (139) |

For κ\kappa is small, the expectation is approximated by its (first-order) Taylor-expansion. Therefore, let

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​(z)=1+erf⁡(z)⇒E′​(z)=2π​e−z2E(z)=1+\erf(z)\quad\Rightarrow\quad E^{\prime}(z)=\frac{2}{\sqrt{\pi}}\mathrm{e}^{-z^{2}} |  | (140) |

and expand

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | e±2​x​β​κα​σN2\displaystyle\mathrm{e}^{\pm\frac{2x\beta\kappa}{\alpha\sigma\_{N}^{2}}} | =1±2​x​βα​σN2​κ+𝒪​(κ2)\displaystyle=1\pm\frac{2x\beta}{\alpha\sigma\_{N}^{2}}\kappa+\mathcal{O}(\kappa^{2}) |  | (141) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | E​(β±x​κα​σN)\displaystyle E(\frac{\beta\pm x\kappa}{\sqrt{\alpha}\sigma\_{N}}) | =E​(βα​σN)±xα​σN​κ​E′​(βα​σN)+𝒪​(κ2).\displaystyle=E(\frac{\beta}{\sqrt{\alpha}\sigma\_{N}})\pm\frac{x}{\sqrt{\alpha}\sigma\_{N}}\kappa E^{\prime}(\frac{\beta}{\sqrt{\alpha}\sigma\_{N}})+\mathcal{O}(\kappa^{2}). |  | (142) |

such that the products of the two terms scale as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | A1\displaystyle A\_{1} | :=e2​x​β​κα​σN2​E​(β+x​κα​σN)=E​(βα​σN)+κ​[2​x​βα​σN2​E​(βα​σN)+xα​σN​E′​(βα​σN)]+𝒪​(κ2)\displaystyle:=\mathrm{e}^{\frac{2x\beta\kappa}{\alpha\sigma\_{N}^{2}}}E(\frac{\beta+x\kappa}{\sqrt{\alpha}\sigma\_{N}})=E(\frac{\beta}{\sqrt{\alpha}\sigma\_{N}})+\kappa\left[\frac{2x\beta}{\alpha\sigma\_{N}^{2}}E(\frac{\beta}{\sqrt{\alpha}\sigma\_{N}})+\frac{x}{\sqrt{\alpha}\sigma\_{N}}E^{\prime}(\frac{\beta}{\sqrt{\alpha}\sigma\_{N}})\right]+\mathcal{O}(\kappa^{2}) |  | (143) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | A2\displaystyle A\_{2} | :=e−2​x​β​κα​σN2​E​(β−x​κα​σN)=E​(βα​σN)−κ​[2​x​βα​σN2​E​(βα​σN)+xα​σN​E′​(βα​σN)]+𝒪​(κ2).\displaystyle:=\mathrm{e}^{-\frac{2x\beta\kappa}{\alpha\sigma\_{N}^{2}}}E(\frac{\beta-x\kappa}{\sqrt{\alpha}\sigma\_{N}})=E(\frac{\beta}{\sqrt{\alpha}\sigma\_{N}})-\kappa\left[\frac{2x\beta}{\alpha\sigma\_{N}^{2}}E(\frac{\beta}{\sqrt{\alpha}\sigma\_{N}})+\frac{x}{\sqrt{\alpha}\sigma\_{N}}E^{\prime}(\frac{\beta}{\sqrt{\alpha}\sigma\_{N}})\right]+\mathcal{O}(\kappa^{2}). |  | (144) |

One then finds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | A1−A2A1+A2=2​κ​[2​x​βα​σN2​E​(βα​σN)+xα​σN​E′​(βα​σN)]2​E​(βα​σN)+𝒪​(κ3)=κ​(2​x​βα​σN2+xα​σN​E′​(βα​σN)E​(βα​σN))+𝒪​(κ3),\frac{A\_{1}-A\_{2}}{A\_{1}+A\_{2}}=\frac{2\kappa\left[\frac{2x\beta}{\alpha\sigma\_{N}^{2}}E(\frac{\beta}{\sqrt{\alpha}\sigma\_{N}})+\frac{x}{\sqrt{\alpha}\sigma\_{N}}E^{\prime}(\frac{\beta}{\sqrt{\alpha}\sigma\_{N}})\right]}{2E(\frac{\beta}{\sqrt{\alpha}\sigma\_{N}})}+\mathcal{O}(\kappa^{3})=\kappa\left(\frac{2x\beta}{\alpha\sigma\_{N}^{2}}+\frac{x}{\sqrt{\alpha}\sigma\_{N}}\frac{E^{\prime}(\frac{\beta}{\sqrt{\alpha}\sigma\_{N}})}{E(\frac{\beta}{\sqrt{\alpha}\sigma\_{N}})}\right)+\mathcal{O}(\kappa^{3}), |  | (145) |

where the correction term is of order κ3\kappa^{3} by symmetry. This implies that, with Θ:=β/α​σN2\Theta:=\beta/\sqrt{\alpha\sigma\_{N}^{2}},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[tanh⁡(γ​M)|x]=2​κβ​x​[Θ2+1π​Θ​e−Θ21+erf⁡(Θ)]+𝒪​(κ3).\mathbb{E}[\tanh(\gamma M)|x]=\frac{2\kappa}{\beta}x\left[\Theta^{2}+\frac{1}{\sqrt{\pi}}\Theta\frac{\mathrm{e}^{-\Theta^{2}}}{1+\erf(\Theta)}\right]+\mathcal{O}(\kappa^{3}). |  | (146) |

This finally means that an effective Langevin equation for a generalised OU-type process with a modified mean-reversion speed may be written down, which reads

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x˙\displaystyle\dot{x} | =−κ​x+β​(𝔼​[tanh⁡(γ​M)|x]+ξ~ttele)+σN​ξtN−σV​ξtV\displaystyle=-\kappa x+\beta(\mathbb{E}[\tanh(\gamma M)|x]+\tilde{\xi}\_{t}^{\text{tele}})+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V} |  | (147) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−κeff​x+β​ξ~ttele+σN​ξtN−σV​ξtV+𝒪​(κ3),\displaystyle=-\kappa\_{\text{eff}}x+\beta\tilde{\xi}\_{t}^{\text{tele}}+\sigma\_{N}\xi\_{t}^{N}-\sigma\_{V}\xi\_{t}^{V}+\mathcal{O}(\kappa^{3}), |  | (148) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | κeff:=κ​Z​(Θ),Z​(Θ):=(1−2​Θ2+2π​Θ​e−Θ21+erf⁡(Θ)).\kappa\_{\text{eff}}:=\kappa Z(\Theta),\qquad Z(\Theta):=\left(1-2\Theta^{2}+\frac{2}{\sqrt{\pi}}\Theta\frac{\mathrm{e}^{-\Theta^{2}}}{1+\erf(\Theta)}\right). |  | (149) |

In other words, the basic mechanism here is that a non-zero value of xx polarizes the trend MM in one direction, which in turn feeds back on xx itself and amplifies its bias. Note that Eq. ([149](https://arxiv.org/html/2511.13277v1#A5.E149 "In E.0.1 Quasi-static Assumption for 𝑥 ‣ Appendix E Stationary Distribution for {𝛼,𝛽}≫𝜅 and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model")) coincide with Eq. ([77](https://arxiv.org/html/2511.13277v1#A4.E77 "In Appendix D Stationary Distribution for 𝛼≫{𝜅,𝛽} and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model")) when Θ≪1\Theta\ll 1, as expected. Interestingly κeff\kappa\_{\text{eff}} first increases when Θ\Theta is small before decreasing and changing sign for Θ=Θc≈0.797999\Theta=\Theta\_{c}\approx 0.797999, see discussion below.

In order to write down the corresponding Fokker-Planck equation, the effective variance of the noise acting on xx is useful.
This can be computed as (for all three noise sources have mean zero)

|  |  |  |  |
| --- | --- | --- | --- |
|  | σx2\displaystyle\sigma\_{x}^{2} | :=2​κ​𝔼​[∫0t∫0te−κ​(2​t−s−s′)​(β​ξ~stele+σN​ξsN−σV​ξsV)​(β​ξ~s′tele+σN​ξs′N−σV​ξs′V)​ds​ds′].\displaystyle:=2\kappa\,\mathbb{E}\left[\int\_{0}^{t}\int\_{0}^{t}\mathrm{e}^{-\kappa(2t-s-s^{\prime})}\left(\beta\tilde{\xi}^{\text{tele}}\_{s}+\sigma\_{N}\xi^{N}\_{s}-\sigma\_{V}\xi^{V}\_{s}\right)\left(\beta\tilde{\xi}^{\text{tele}}\_{s^{\prime}}+\sigma\_{N}\xi^{N}\_{s^{\prime}}-\sigma\_{V}\xi^{V}\_{s^{\prime}}\right)\,\differential s\,\differential s^{\prime}\right]. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​κ​∫0t∫0te−κ​(2​t−s−s′)​(β2​𝔼​[ξ~stele​ξ~s′tele]⏟≈2​ln⁡(2)α​δ​(s−s′)+2​β​σN​𝔼​[ξ~stele​ξs′N]⏟=2​απ​e−α​(s−s′)​Θ​(s−s′)+σN2​𝔼​[ξsN​ξs′N]⏟=δ​(s−s′)+σV2​𝔼​[ξsV​ξs′V]⏟=δ​(s−s′))​ds​ds′\displaystyle=2\kappa\int\_{0}^{t}\int\_{0}^{t}\mathrm{e}^{-\kappa(2t-s-s^{\prime})}\left(\beta^{2}\underbrace{\mathbb{E}[\tilde{\xi}^{\textup{tele}}\_{s}\tilde{\xi}^{\textup{tele}}\_{s^{\prime}}]}\_{\approx\frac{2\ln(2)}{\alpha}\delta(s-s^{\prime})}+2\beta\sigma\_{N}\underbrace{\mathbb{E}[\tilde{\xi}^{\textup{tele}}\_{s}\xi^{N}\_{s^{\prime}}]}\_{=2\sqrt{\frac{\alpha}{\pi}}\mathrm{e}^{-\alpha(s-s^{\prime})}\Theta(s-s^{\prime})}+\sigma\_{N}^{2}\underbrace{\mathbb{E}[\xi^{N}\_{s}\xi^{N}\_{s^{\prime}}]}\_{=\delta(s-s^{\prime})}+\sigma\_{V}^{2}\underbrace{\mathbb{E}[\xi^{V}\_{s}\xi^{V}\_{s^{\prime}}]}\_{=\delta(s-s^{\prime})}\right)\,\differential s\,\differential s^{\prime} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≈σN2​(1+Ξ2+4π​Θ+2​ln⁡(2)​Θ2),(α≫κ),\displaystyle\approx{\sigma\_{N}^{2}}\left(1+\Xi^{2}+\frac{4}{\sqrt{\pi}}\Theta+{2\ln(2)\Theta^{2}}\right),\hskip 18.49988pt(\alpha\gg\kappa), |  | (150) |

where the last two summands are due to the results in Eq. ([122](https://arxiv.org/html/2511.13277v1#A4.E122 "In D.2 Variance of the Process ‣ Appendix D Stationary Distribution for 𝛼≫{𝜅,𝛽} and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model")) and the preceding steps, and Ξ2:=σV2/σN2\Xi^{2}:=\sigma\_{V}^{2}/\sigma\_{N}^{2} is the inverse of the well-known excess volatility ratio, see kurth2025revisiting.

Thus, the following Fokker-Planck equation may be written down:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂p​(x)∂t\displaystyle\frac{\partial p(x)}{\partial t} | =−∂∂x​[(−κ​x+β​𝔼​[tanh⁡(γ​M)|x])​p​(x)]+σx22​∂2∂x2​p​(x)\displaystyle=-\frac{\partial}{\partial x}[(-\kappa x+\beta\mathbb{E}[\tanh(\gamma M)|x])p(x)]+\frac{\sigma\_{x}^{2}}{2}\frac{\partial^{2}}{\partial x^{2}}p(x) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∂∂x​[−κeff​x​p​(x)]+σx22​∂2∂x2​p​(x).\displaystyle=-\frac{\partial}{\partial x}[-\kappa\_{\textup{eff}}x\,p(x)]+\frac{\sigma\_{x}^{2}}{2}\frac{\partial^{2}}{\partial x^{2}}p(x). |  | (151) |

The solution is derived with a Maxwell-Boltzmann ansatz as before

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | p​(x)\displaystyle p(x) | =1B​exp⁡(−Z​(Θ)​κσx2​x2),B:=π​σx2Z​(Θ)​κ.\displaystyle=\frac{1}{B}\exp\left(-\frac{Z(\Theta)\kappa}{\sigma\_{x}^{2}}x^{2}\right),\hskip 18.49988ptB:=\sqrt{\frac{\pi\sigma\_{x}^{2}}{Z(\Theta)\kappa}}. |  | (152) |

Assuming p​(x)p(x) is a good approximation of the stationary mispricing distribution, it immediately follows that p​(x)p(x) cannot remain unimodal whenever Z​(Θ)<0Z(\Theta)<0, i.e. for Θ>Θc≈0.797999\Theta>\Theta\_{c}\approx 0.797999.

However, the quasi-stationary assumption is only approximate and the above prediction is not expected to be exact. In particular, when β\beta/Θ\Theta increases, such an assumption is expected to be violated for two reasons: a) σx\sigma\_{x} increases, meaning that the dynamics of xx becomes more intense and “blurs” the distribution p​(M|x)p(M|x), lowering the feedback effect; b) as we show in the next section, the dynamics of MM slows down abruptly so that the separation of time scales becomes less and less warranted. Hence we expect that the above value of Θc\Theta\_{c} is a lower bound to the exact value.

Still, the above computation unveils the mathematical mechanism that leads to p​(x)p(x) becoming bimodal only for values of β\beta that are much larger than the ones that suffice for p​(M)p(M) to be bimodal. Indeed, the bimodality condition for p​(M)p(M), which can be calculated explicitly when κ\kappa is small by expanding the normalisation A​(x)A(x), Eq. ([E.0.1](https://arxiv.org/html/2511.13277v1#A5.Ex27 "E.0.1 Quasi-static Assumption for 𝑥 ‣ Appendix E Stationary Distribution for {𝛼,𝛽}≫𝜅 and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model")), of the conditional density p​(M|x)p(M|x) up to first order in κ\kappa:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | A​(x)\displaystyle A(x) | =(12)2​βσN2​α​γ​α​σN2​π​eβ2+κ2​x2α​σN2​E​(Θ)+𝒪​(κ2).\displaystyle=\left(\frac{1}{2}\right)^{\frac{2\beta}{\sigma\_{N}^{2}\alpha\gamma}}\sqrt{\alpha\sigma\_{N}^{2}\pi}\,\,\mathrm{e}^{\frac{\beta^{2}+\kappa^{2}x^{2}}{\alpha\sigma\_{N}^{2}}}E(\Theta)+\mathcal{O}(\kappa^{2}). |  | (153) |

Using this, the conditional density reads

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | p​(M|x)\displaystyle p(M|x) | ≈1A​(x)​cosh⁡(γ​M)2​βσN2​α​γ​e−M2α​σN2+2​κα​σN2​M​x\displaystyle\approx\frac{1}{A(x)}\cosh(\gamma M)^{\frac{2\beta}{\sigma\_{N}^{2}\alpha\gamma}}\,\mathrm{e}^{-\frac{M^{2}}{\alpha\sigma\_{N}^{2}}+\frac{2\kappa}{\alpha\sigma\_{N}^{2}}Mx} |  | (154) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =22​βσN2​α​γα​σN2​π​E​(Θ)​e−β2α​σN2​e−(M−κ​x)2α​σN2​cosh⁡(γ​M)2​βσN2​α​γ,\displaystyle=\frac{2^{\frac{2\beta}{\sigma\_{N}^{2}\alpha\gamma}}}{\sqrt{\alpha\sigma\_{N}^{2}\pi}E(\Theta)}\mathrm{e}^{-\frac{\beta^{2}}{\alpha\sigma\_{N}^{2}}}\mathrm{e}^{-\frac{(M-\kappa x)^{2}}{\alpha\sigma\_{N}^{2}}}\cosh(\gamma M)^{\frac{2\beta}{\sigma\_{N}^{2}\alpha\gamma}}, |  | (155) |

from which it follows that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | p​(M)\displaystyle p(M) | =∫−∞∞p​(M|x)​p​(x)​dx\displaystyle=\int\_{-\infty}^{\infty}p(M|x)p(x)\,\mathrm{d}x |  | (156) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1B​22​βσN2​α​γα​σN2​π​E​(Θ)​e−β2α​σN2​cosh⁡(γ​M)2​βσN2​α​γ​∫−∞∞e−(M−κ​x)2α​σN2​e−κ​Z​(Θ)σx2​x2​dx\displaystyle=\frac{1}{B}\frac{2^{\frac{2\beta}{\sigma\_{N}^{2}\alpha\gamma}}}{\sqrt{\alpha\sigma\_{N}^{2}\pi}E(\Theta)}\mathrm{e}^{-\frac{\beta^{2}}{\alpha\sigma\_{N}^{2}}}\cosh(\gamma M)^{\frac{2\beta}{\sigma\_{N}^{2}\alpha\gamma}}\int\_{-\infty}^{\infty}\mathrm{e}^{-\frac{(M-\kappa x)^{2}}{\alpha\sigma\_{N}^{2}}}\mathrm{e}^{-\frac{\kappa Z(\Theta)}{\sigma\_{x}^{2}}x^{2}}\,\mathrm{d}x |  | (157) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =22​Θ2β​γE​(Θ)​eΘ2​Z​(Θ)π​(σx2​κ+Z​(Θ)​α​σN2)​cosh⁡(γ​M)2​Θ2β​γ​e−M2​Z​(Θ)σx2​κ+Z​(Θ)​α​σN2,\displaystyle=\frac{2^{\frac{2\Theta^{2}}{\beta\gamma}}}{E(\Theta)e^{\Theta^{2}}}\sqrt{\frac{Z(\Theta)}{\pi(\sigma\_{x}^{2}\kappa+Z(\Theta)\alpha\sigma\_{N}^{2})}}\,\cosh(\gamma M)^{\frac{2\Theta^{2}}{\beta\gamma}}\,\mathrm{e}^{-M^{2}\frac{Z(\Theta)}{\sigma\_{x}^{2}\kappa+Z(\Theta)\alpha\sigma\_{N}^{2}}}, |  | (158) |

It is easy to see that p​(M)p(M) has an extremum at M=0M=0 because the first derivative of the cosh, (minus) the sinh, evaluated at M=0M=0 contributes a term equating zero and the derivative of the Gaussian contributes a term ∼M\sim M, which, of course, is also zero when M=0M=0; in total: p′​(M=0)=0p^{\prime}(M=0)=0.
The second derivative (disregarding the normalisation) evaluated at M=0M=0 is

|  |  |  |  |
| --- | --- | --- | --- |
|  | p′′​(M=0)∝(2​β​γα​σN2−2​Z​(Θ)σx2​κ+Z​(Θ)​α​σN2).p^{\prime\prime}(M=0)\propto\left(\frac{2\beta\gamma}{\alpha\sigma\_{N}^{2}}-\frac{2Z(\Theta)}{\sigma\_{x}^{2}\kappa+Z(\Theta)\alpha\sigma\_{N}^{2}}\right). |  | (159) |

The critical point Θ≡Θc\Theta\equiv\Theta\_{c} is the point where the mispricing distribution p​(x)p(x) becomes bimodal, and beyond which the Gaussian approximation for p​(x)p(x) breaks down entirely. Inserting this point into p′′​(M=0)p^{\prime\prime}(M=0) determines whether the trend distribution p​(M)p(M) is generally already bimodal when p​(x)p(x) just turns bimodal. Inserting the critical point yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | p′′​(M=0)|Θ=Θc∝2​β​γα​σN2>0p^{\prime\prime}(M=0)|\_{\Theta=\Theta\_{c}}\propto\frac{2\beta\gamma}{\alpha\sigma\_{N}^{2}}>0 |  | (160) |

because Z​(Θc)=0Z(\Theta\_{c})=0 and all parameters are positive. This shows that in this limit the trend distribution p​(M)p(M) always is bimodal before the trend distribution becomes bimodal. In fact, p​(M)p(M) becomes bimodal as soon as β>1/γ\beta>1/\gamma.

#### E.0.2 Quasi-static Assumption Break-down

In this section it will be shown why the quasi-static approximation from the previous section that works for small and moderate values of β\beta rapidly breaks down when β\beta is increased, such that no closed-form stationary distribution can be written down when β\beta becomes large – approximately large enough to induce bimodality in p​(x)p(x).

The demonstration in this section is performed on the example of fixed x=0x=0 for analytical tractability.
Note from the conditional FPE, Eq. ([130](https://arxiv.org/html/2511.13277v1#A5.E130 "In E.0.1 Quasi-static Assumption for 𝑥 ‣ Appendix E Stationary Distribution for {𝛼,𝛽}≫𝜅 and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model")), that MM moves like in an effective potential of 12​M2−βγ​ln⁡(cosh⁡(γ​M))\frac{1}{2}M^{2}-\frac{\beta}{\gamma}\ln(\cosh(\gamma M)), corresponding to a force α​M−α​β​tanh⁡(γ​M)\alpha M-\alpha\beta\tanh(\gamma M).
In the steady state one finds M−β​tanh⁡(γ​M)=0M-\beta\tanh(\gamma M)=0 for MM. This equation shows a bifurcation: beyond the critical point β​γ=1\beta\gamma=1, the equation admits three solution, where the existence of three solutions corresponds to bimodality. Those solutions are M=0M=0 and when β​γ>1\beta\gamma>1, as we have here, the other two solutions are M≈±βM\approx\pm\beta because the hyperbolic tangent will mostly be in its saturated regime, so at ±1\pm 1, as, again, γ​M\gamma M is large when β​γ\beta\gamma is large. For β​γ<1\beta\gamma<1, there is only one solution, M=0M=0.

Plugging the bimodal case, where there are three solutions, back into the effective potential, yields an effective potential of zero when M=0M=0 and an effective potential of

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​β2−βγ​ln⁡(cosh⁡(±β​γ))≈12​β2−βγ​|β​γ|=−12​β2,\frac{1}{2}\beta^{2}-\frac{\beta}{\gamma}\ln(\cosh(\pm\beta\gamma))\approx\frac{1}{2}\beta^{2}-\frac{\beta}{\gamma}|\beta\gamma|=-\frac{1}{2}\beta^{2}, |  | (161) |

for M=±βM=\pm\beta. The approximation is valid when ln⁡(cosh⁡(x))≈|x|\ln(\cosh(x))\approx|x|.

From the Arrhenius law it then follows that the expected time to switch states from M=−βM=-\beta to M=+βM=+\beta, i.e. the time T×T\_{\times} to cross the potential barrier, is of the order of hanggi1990reaction

|  |  |  |  |
| --- | --- | --- | --- |
|  | T×∼1α​eβ22​T=1α​eΘ2,T\_{\times}\sim\frac{1}{\alpha}\mathrm{e}^{\frac{\beta^{2}}{2T}}=\frac{1}{\alpha}\mathrm{e}^{\Theta^{2}}, |  | (162) |

where T=σN2​α2T=\frac{\sigma\_{N}^{2}\alpha}{2} is the ‘temperature’ parameter from statisitcal mechanics, which can be read off of the conditional FPE, Eq. ([130](https://arxiv.org/html/2511.13277v1#A5.E130 "In E.0.1 Quasi-static Assumption for 𝑥 ‣ Appendix E Stationary Distribution for {𝛼,𝛽}≫𝜅 and 𝛾⁢𝜎_𝑁²↛0 ‣ Stationary Distributions of the Mode-switching Chiarella Model")).

This showcases that MM is no longer a fast variable when Θ\Theta is increased; as a matter of fact MM swiftly becomes very slow and the expected time to switch from, e.g., +β+\beta to −β-\beta diverges as β\beta is increased. This means that while the analytical distribution is still bimodal and symmetric in MM, it will take exponentially longer to observe such a transition – numerically this can no longer be observed.

Further, when MM suddenly becomes slow compared to xx, the conditional FPE ansatz breaks down as MM no longer has the time to relax with respect to xx. In fine, this is because the dominating time scale of xx, κ−1\kappa^{-1}, is no longer much larger than α−1​eΘ2\alpha^{-1}e^{\Theta^{2}} – in fact κ−1\kappa^{-1} swiftly becomes much smaller, rendering the approximation invalid. Therefore, no closed-form solution can be derived in this way – but the mechanism for bimodality can be revealed.

Interestingly, the break-down of the approximation and the onset of bimodality happen around the same parameter values because both the exponent of the Arrhenius law and the expression giving the value of κeff\kappa\_{\rm eff} are functions of the very same combination of parameters Θ=β/α​σN2\Theta=\beta/\sqrt{\alpha\sigma\_{N}^{2}}.