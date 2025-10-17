---
authors:
- Rohan Shenoy
- Peter Kempthorne
doc_id: arxiv:2510.14108v1
family_id: arxiv:2510.14108
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: On Time-subordinated Brownian Motion Processes for Financial Markets
url_abs: http://arxiv.org/abs/2510.14108v1
url_html: https://arxiv.org/html/2510.14108v1
venue: arXiv q-fin
version: 1
year: 2025
---


Rohan Shenoy
Department of Mathematics, Imperial College London, rohan.shenoy22@imperial.ac.uk

Peter Kempthorne
Department of Mathematics, Massachusetts Institute of Technology, kemp2@mit.edu

(October 15, 2025)

###### Abstract

The key purpose of this paper is to present Fourier method to model the stochastic time-change in this context of time-subordinated Brownian motion models. We review Gaussian Variance-Mean mixtures and time-subordinated models with a key example of the Gamma process. A non-parametric characteristic function decomposition of subordinated Brownian motion is presented. This allows one to characterise and study the stochastic time-change directly from the full process. Finally we provide an example empirical decomposition of S&\&P log-returns. We explore the Variance Gamma process as a key example throughout.

Keywords. Subordinator process; time-subordinated models; stochastic time-change; empirical characteristic function; variance-gamma process.

## 1 Introduction

Under many simple market models, the price returns of a financial asset are assumed to follow a log-Normal distribution. The celebrated Black-Scholes-Merton option pricing model [[1](https://arxiv.org/html/2510.14108v1#bib.bib1)], assumes that a stock’s log price follows a random walk in continuous time with a variance proportional to the square of the stock price, the Geometric Brownian Motion (GBM) model.
For any finite time interval, the distribution of price increments (i.e. "steps" in the random walk) is log-Normal and the distribution of the log return of stock prices over the time interval is Normal with variance a constant proportion of the length of the interval.

In empirical modelling of asset price dynamics, time series of asset prices are readily available. Commonly, the time frequency of such series is daily, but can be lower with weekly or monthly prices, or higher with time bars which have fixed-length time intervals (e.g. 30, 5, 1 minutes). With higher frequencies, the market micro-structure at the transaction level plays a significant role with possible prices determined by bid and offer prices of market makers that are constrained to discrete price levels, and variation in trading activity over a trading day in terms of trade counts and trade volume.

In this paper, we focus on models of time series of closing prices of an asset with daily or lower frequency. Such time series are well-suited to applying the Geometric Brownian Motion model and extensions without the need to accommodate micro-structure issues of higher frequency data. Indeed, generalized Central Limit Theorems might apply to model daily log-price increments as Normal since they are the sums of large-sample log-price increments at higher frequencies.

It is common to index daily price observations by market-day counts and assume unit time increments over all successive price observations. Assuming the GBM model for such time series, the time series of daily prices is transformed to a daily time series of log returns which is equivalent to a random sample (independent and identically distributed) from a Normal distribution with mean equal to the daily drift rate and variance equal to the daily variance rate. However goodness-of-fit tests and diagnostics (e.g., Shapiro Wilk Normality Test [[2](https://arxiv.org/html/2510.14108v1#bib.bib2)] and Normal QQ Plots) of Normal model fits to daily log return time series often reject the Normal distribution assumption due to "heavy-tailed" empirical distributions that are not consistent with the Normal distribution shape.

To maintain use of the GBM model, many authors have proposed possible alternative time indices to market-day counts, such as shares traded or transaction counts (e.g. Clark(1973) [[3](https://arxiv.org/html/2510.14108v1#bib.bib3)]). Making the time increments between price observations conform with a progress indicator is known as a time-subordination: a change of the original time-scale (cumulative count of market days) to an alternate basis. This new time-scale is often labelled as "business time" [[4](https://arxiv.org/html/2510.14108v1#bib.bib4)].

Significantly, the works of Madan and Milne (1991) [[5](https://arxiv.org/html/2510.14108v1#bib.bib5)] and Madan, Carr and Chang (1998) [[6](https://arxiv.org/html/2510.14108v1#bib.bib6)] have highlighted the possibility of improving upon the use of observable indices by implementing a stochastic index through a random time-subordination. The authors demonstrate that the Variance Gamma model, a random time-subordinated model, provides more accurate pricing performance of call options than Geometric Brownian motion. Specifically it values options higher, particularly for out-of-the-money options with long maturity on stocks with high kurtosis.

Under a random time-subordination model, one infers that the economically relevant time in a market is itself a stochastic process, independent of other random processes affecting market dynamics. This model allows the distribution of price movements itself on different market days to differ randomly because some days are "longer" and other days are "shorter"111In their paper of 1990, Madan and Seneta comment on this idea, stating: More informally, one may think of G​(t)G(t) [the stochastic index] as a formal statement of the remark, ”Didn’t have much of a year this year,” by allowing for an interpretation of how much of a year one actually had.. The results of Skorokhod [[7](https://arxiv.org/html/2510.14108v1#bib.bib7)] and Monroe [[8](https://arxiv.org/html/2510.14108v1#bib.bib8)] (as highlighted in Veraart and Winkel [[4](https://arxiv.org/html/2510.14108v1#bib.bib4)]) demonstrate that in fact any arbitrage free model can be represented as a Brownian motion with random time change, providing more concrete motivation for studying such models as they represent a valuable change of viewpoint.

We study the mathematical model of log returns where the time increments follow a subordinator process and the log price increments are attributed to Brownian motion on the stochastic time scale. Due to a theorem of Dubins and Schwarz [[9](https://arxiv.org/html/2510.14108v1#bib.bib9)], one can express any continuous local martingale MM as a time-changed Brownian motion where the time-change is given by the continuous quadratic variation of MM. However, we find that the full process has a closer relationship with the subordinator process in Fourier space which could provide more insight. To this end we develop an alternate, Fourier method which enables us to directly transform a time-changed Brownian motion process into its subordinator process. This is formulated as the time-change transform and allows one to reduce the study of the full process to studying just the stochastic time-change in isolation. We define the Fourier transform of the subordinator process from the Fourier transform of data from the full process and apply an inversion back into real space we obtain the probability distribution of the subordinator process.
Empirically, one can then characterise the underlying random subordinator process straight from price observations over market-day counts.

Empirical modelling of the subordinator process directly enables evaluation of its characteristics. A key running example in this paper is the Variance Gamma model of Madan et al. [[5](https://arxiv.org/html/2510.14108v1#bib.bib5)], [[6](https://arxiv.org/html/2510.14108v1#bib.bib6)] which assumes the Gamma process for the time subordinator of log-transformed daily price time series. For this case, the time subordinator process has stationary increments which are independent over non-overlapping time intervals, properties satisfied by Lévy processes. A significant contribution of this paper is the theory and methods for estimation and hypothesis testing of Gaussian variance-mean mixture distributions for which the Variance-Gamma process is a special case.

Section [2](https://arxiv.org/html/2510.14108v1#S2 "2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets") characterises Gaussian variance-mean mixtures for modelling daily log returns - the special case of these models when the variance distribution is Gamma corresponds to the Variance-Gamma process. We then consider the extension into continuous time-subordinated Brownian motion processes in Section [3](https://arxiv.org/html/2510.14108v1#S3 "3 Time-Subordinated Brownian Motion Processes ‣ On Time-subordinated Brownian Motion Processes for Financial Markets"). This allows the formulation of the time-change transform in Section [4](https://arxiv.org/html/2510.14108v1#S4 "4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets"). Section [5](https://arxiv.org/html/2510.14108v1#S5 "5 Example Empirical Analysis of a Decomposed Time-Change Process ‣ On Time-subordinated Brownian Motion Processes for Financial Markets") presents a brief example of applying the time-change transform to the S&\&P500 index with the, including evaluating its consistency with the Variance-Gamma process for fixed and varied holding periods of log-returns (varying the number of days in holding periods 1,5,10,15,20 days). Section [6](https://arxiv.org/html/2510.14108v1#S6 "6 Discussion ‣ On Time-subordinated Brownian Motion Processes for Financial Markets") concludes the results.

## 2 Gaussian Variance-Mean Mixtures

We begin with defining the Gaussian variance-mean mixture distribution, which arises as the distribution of the increment of a Brownian motion process with drift θ\theta and volatility σ\sigma over a stochastic time increment.

Let {Yt,t≥0}\{Y\_{t},t\geq 0\} denote the Brownian motion process with drift θ\theta and volatility σ\sigma. For initial time tt and a time increment of deterministic length v≥0v\geq 0, the increment of the Brownian motion:
X=Yt+v−YtX=Y\_{t+v}-Y\_{t}
is a N​(μX,σX2)N(\mu\_{X},\sigma\_{X}^{2}) random variable with mean μX=θ​v\mu\_{X}=\theta v and variance σX2=σ2​v.\sigma\_{X}^{2}=\sigma^{2}v. It will be convenient to represent this distribution as an affine transformation of a standard Gaussian random variable, Z∼N​(0,1)Z\sim N(0,1):
X=θ​v+σ​v​Z.X=\theta v+\sigma\sqrt{v}Z.

###### Definition 1 (Gaussian variance-mean mixture).

The Gaussian variance-mean mixture distribution is the distribution of the increment of the Brownian motion process {Yt,t≥0}\{Y\_{t},t\geq 0\} (with drift θ\theta and volatility σ2\sigma^{2} ) realized over a stochastic time increment VV, a non-negative random variable independent of the Brownian motion process. The random variable

|  |  |  |  |
| --- | --- | --- | --- |
|  | X=θ​V+σ​V​ZX=\theta V+\sigma\sqrt{V}Z |  | (1) |

is known as a Gaussian variance-mean mixture with mixing distribution VV, denoted G​V​M​(θ,σ,V).GVM(\theta,\sigma,V).

The distribution of XX is fully characterized by the characteristic functions of VV and ZZ, which we explore in section [4](https://arxiv.org/html/2510.14108v1#S4 "4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets"). Proposition [1](https://arxiv.org/html/2510.14108v1#Thmprop1 "Proposition 1. ‣ 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets") below details this for subordinated Brownian motion. The mean of the Gaussian variance-mean mixture distribution is

|  |  |  |
| --- | --- | --- |
|  | 𝔼[X]=𝔼V[𝔼X∣V[X]]]=𝔼V[θV]=θ𝔼[V].\mathbb{E}[X]=\mathbb{E}\_{V}[\mathbb{E}\_{X\mid V}[X]]]=\mathbb{E}\_{V}[\theta V]=\theta\mathbb{E}[V]. |  |

When θ=0\theta=0, the distribution is symmetric and is a simple variance mixture of Gaussian distributions with constant zero mean. When θ≠0\theta\not=0, the symmetry of the distribution will depend on the symmetry of the mixing distribution of VV. The mean and variance of XX each depend on the distribution VV with their scales being linear functions of V.V. When modelling daily log prices of stocks with annual units of time, the VV distribution corresponds to very small time increments ≈1/365\approx 1/365 or 1/2521/252. For such cases, the mean θ​V\theta V will be second order to the V​Z\sqrt{V}Z (hence relatively negligible) and the distribution will be nearly symmetric.

Gaussian variance-mean mixtures can be applied in empirical modelling of the price dynamics of financial assets or indices. Consider a discrete time series of asset prices:
{p0,p1,p2,…,pn}\{p\_{0},p\_{1},p\_{2},\dots,p\_{n}\}\,
where {t0,t1,…,tn}\{t\_{0},t\_{1},\dots,t\_{n}\} are the time points of the respective prices. With low frequency data, the time points are calendar dates and the prices are end-of-day prices. If yj=log⁡(pj)y\_{j}=\log(p\_{j}), j=0,…,nj=0,\dots,n represents the time series of log prices then

|  |  |  |
| --- | --- | --- |
|  | yj=y0+∑i=0jxj,y\_{j}=y\_{0}+\sum\_{i=0}^{j}x\_{j}, |  |

where xjx\_{j} is the log price return
over the time interval (tj−1,tj](t\_{j-1},t\_{j}]: xj=log⁡(pj/pj−1),j=1,…,n.x\_{j}=\log(p\_{j}/p\_{j-1}),\ j=1,\dots,n.

It is common to let jj index the market days, weeks, or months depending on the frequency of the time series. Empirical modelling of the price dynamics of an asset treats the observed log price returns as realizations of random variables
{Xj}j=0n.\{X\_{j}\}\_{j=0}^{n}. The simplest models assume that the XjX\_{j} log price returns are independent and identically distributed. A special case of this definition introduced by Barndorff-Nielsen et al. [[10](https://arxiv.org/html/2510.14108v1#bib.bib10)] assumes further that VV is an infinitely divisible random variable. With this assumption, the discrete time stochastic process model can be embedded in a continuous-time model which has consistent specifications for alternate observation frequencies.

We would like to use the Gaussian variance-mean mixtures to be able to define time-subordinated Brownian motion processes

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=θ​τt+σ​Wτt,X\_{t}=\theta\tau\_{t}+\sigma W\_{\tau\_{t}}, |  | (2) |

where τt\tau\_{t} is a subordinator process independent of the Wiener process WtW\_{t}. Our mixing distribution VV above will later characterise the stationary increments for the subordinating process τt\tau\_{t}.
In this manner, the asymmetry term θ​V\theta V relates to the random drift term θ​τt\theta\tau\_{t}, and the variance-mixing term σ​V\sigma\sqrt{V} relates to the random noise term σ​Wτt\sigma W\_{\tau\_{t}}. This will be explored in depth in section [3](https://arxiv.org/html/2510.14108v1#S3 "3 Time-Subordinated Brownian Motion Processes ‣ On Time-subordinated Brownian Motion Processes for Financial Markets").

###### Remark 1.

First consider the case θ=0\theta=0. Here XX becomes a symmetric distribution. Many of the potential VV distributions one considers are often 2+ parameter distributions making the parameters for the distribution XX non-identifiable if no further restrictions are imposed. However, this actually provides flexibility in interpreting properties of the distribution across different settings by choosing different restrictions.

* •

  If we restrict VV to have expectation μ=1\mu=1, then σ\sigma becomes a volatility parameter. This can be seen by using the independence of VV and ZZ,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Var ​[X]=𝔼​[(σ​V​Z)2]=σ2​𝔼​[V​Z2]=σ2​𝔼​[V]​𝔼​[Z2]=σ2.\text{Var }[X]=\mathbb{E}\left[\left(\sigma\sqrt{V}Z\right)^{2}\right]=\sigma^{2}\mathbb{E}\left[{V}Z^{2}\right]=\sigma^{2}\mathbb{E}[V]\mathbb{E}\left[Z^{2}\right]=\sigma^{2}. |  | (3) |

  This is a particularly useful notion which we will employ in section [3](https://arxiv.org/html/2510.14108v1#S3 "3 Time-Subordinated Brownian Motion Processes ‣ On Time-subordinated Brownian Motion Processes for Financial Markets") to define time-subordinated Brownian motion processes.
* •

  Alternatively, we could fix σ\sigma (e.g σ=1\sigma=1) and directly observe changes to VV across different settings e.g. over different time periods for the process XtX\_{t}.

For the case θ≠0\theta\neq 0, XX is no longer a symmetric distribution due to the θ​V\theta V term. Further, σ\sigma no longer represents the volatility as Var​[X]=θ2​Var​[V]+σ2​𝔼​[V]\text{Var}[X]=\theta^{2}\text{Var}[V]+\sigma^{2}\mathbb{E}[V]. However, if we let 𝔼​[V]=μ=1\mathbb{E}[V]=\mu=1 and denote Var​[V]=ν\text{Var}[V]=\nu then the volatility is given by θ2​ν+σ2\theta^{2}\nu+\sigma^{2}. So the inclusion of the stochastic drift term determines the expectation just as a deterministic drift would, but additionally provides a further contribution to the variance above σ2\sigma^{2} unlike a deterministic drift.

###### Examples.

Specifying different distributions for VV gives rise to various different Gaussian variance-mean mixture variables.

* •

  Variance-Gamma (VV is Gamma distributed): We will refer back to this example throughout
* •

  Normal Inverse Gaussian (VV is Inverse Gaussian distributed)
* •

  Generalised Hyperbolic (VV is Generalised Inverse Gaussian distributed)

In general there are no closed forms for the densities of these distributions, though there are special cases e.g. the Laplace distribution as a special case Variance Gamma distribution (with exponentially distributed VV as a special case of the Gamma distribution). In the general case we can condition the density on the distribution of VV: for a standard Gaussian density ϕ​(x)\phi(x) and stochastic variance density fV​(v)f\_{V}(v), one writes

|  |  |  |  |
| --- | --- | --- | --- |
|  | fX​(x)=∫ϕ​(x−θ​vσ​v)​fV​(v)​𝑑v.f\_{X}(x)=\int\phi\left(\dfrac{x-\theta v}{\sigma\sqrt{v}}\right)f\_{V}(v)dv. |  | (4) |

For example, in the case of the Variance gamma distribution where V∼Gamma​(α,β)V\sim\text{Gamma}(\alpha,\beta), this becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | fX​(x)=∫0∞12​π​σ2​v​e−(x−θ​v)2/(2​σ2​v)​βαΓ​(α)​vα−1​e−β​v​𝑑v.f\_{X}(x)=\int\_{0}^{\infty}\frac{1}{\sqrt{2\pi\sigma^{2}v}}e^{-(x-\theta v)^{2}/{(2\sigma^{2}v)}}\dfrac{\beta^{\alpha}}{\Gamma(\alpha)}v^{\alpha-1}e^{-\beta v}dv. |  | (5) |

Alternatively, the characteristic function has a much nicer form and, as we will explore, has strong applications.

###### Proposition 1.

Let X=θ​V+σ​V​ZX=\theta V+\sigma\sqrt{V}Z be a Gaussian variance-mean mixture as in Definition [1](https://arxiv.org/html/2510.14108v1#Thmdefinition1 "Definition 1 (Gaussian variance-mean mixture). ‣ 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets"). Then the characteristic function of the XX, ψX\psi\_{X} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψX​(t)=𝔼V​[e(i​t​θ−t2​σ2/2)​V].\psi\_{X}(t)=\mathbb{E}\_{V}\left[e^{(it\theta-t^{2}\sigma^{2}/2)V}\right]. |  | (6) |

###### Remark 2.

Before providing the proof, we reflect on the Gaussian variance-mixture characterisation of XX. When encountering such a mixture, we can first condition on the random variance to reduce the setup to Normality - something we understand well - then deal with the random variance separately. We will return to this idea throughout, later motivating the definitions of the variance-mixing transform and time-subordinator transform.

###### Proof.

By conditioning on the value of VV, we find for t∈ℝt\in\mathbb{R},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψX​(t)\displaystyle\psi\_{X}(t) | =𝔼​[ei​t​X]=𝔼​[ei​t​(θ​V+σ​V​Z)]=𝔼V​[𝔼Z​[ei​t​(θ​V+σ​V​Z)|V]]\displaystyle=\mathbb{E}\left[e^{itX}\right]=\mathbb{E}\left[e^{it(\theta V+\sigma\sqrt{V}Z)}\right]=\mathbb{E}\_{V}\left[\mathbb{E}\_{Z}\left[e^{it(\theta V+\sigma\sqrt{V}Z)}\hskip 2.84544pt\Big|V\right]\right] |  | (7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼V​[ei​t​θ​V​ψZ​(t​σ​V)]=𝔼V​[ei​t​θ​V−t2​σ2​V/2]=𝔼V​[e(i​t​θ−t2​σ2/2)​V]\displaystyle=\mathbb{E}\_{V}\left[e^{it\theta V}\psi\_{Z}\left(t\sigma\sqrt{V}\right)\right]=\mathbb{E}\_{V}\left[e^{it\theta V-t^{2}\sigma^{2}V/2}\right]=\mathbb{E}\_{V}\left[e^{(it\theta-t^{2}\sigma^{2}/2)V}\right] |  | (8) |

where the last line follows from recalling that the characteristic function of a standard Gaussian is given by ψZ​(t)=e−t2/2\psi\_{Z}(t)=e^{-t^{2}/2}.
∎

###### Corollary 1.

In the case that V∼Gamma​(α,β)V\sim\text{Gamma}(\alpha,\beta), we can complete the calculation to find

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼V​[e(i​t​θ−t2​σ2/2)​V]\displaystyle\mathbb{E}\_{V}\left[e^{(it\theta-t^{2}\sigma^{2}/2)V}\right] | =∫0∞e(i​t​θ−t2​σ2/2)​v​βαΓ​(α)​vα−1​e−β​v​𝑑v=∫0∞βαΓ​(α)​vα−1​e−(β−i​t​θ+t2​σ2/2)​v​𝑑v,\displaystyle=\int\_{0}^{\infty}e^{(it\theta-t^{2}\sigma^{2}/2)v}\dfrac{\beta^{\alpha}}{\Gamma(\alpha)}v^{\alpha-1}e^{-\beta v}dv=\int\_{0}^{\infty}\dfrac{\beta^{\alpha}}{\Gamma(\alpha)}v^{\alpha-1}e^{-(\beta-it\theta+t^{2}\sigma^{2}/2)v}dv, |  | (9) |

after which we apply the definition of the Gamma function (noting β+t2​σ2/2>0\beta+t^{2}\sigma^{2}/2>0),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0∞βαΓ​(α)​vα−1​e−(β−i​t​θ+t2​σ2/2)​v​𝑑v=βαΓ​(α)​Γ​(α)(β−i​t​θ+t2​σ2/2)α=(1−i​θ​tβ+t2​σ22​β)−α.\int\_{0}^{\infty}\dfrac{\beta^{\alpha}}{\Gamma(\alpha)}v^{\alpha-1}e^{-(\beta-it\theta+t^{2}\sigma^{2}/2)v}dv=\dfrac{\beta^{\alpha}}{\Gamma(\alpha)}\dfrac{\Gamma(\alpha)}{\left(\beta-it\theta+t^{2}\sigma^{2}/2\right)^{\alpha}}=\left(1-\frac{i\theta t}{\beta}+\dfrac{t^{2}\sigma^{2}}{2\beta}\right)^{-\alpha}. |  | (10) |

###### Remark 3.

From Proposition [1](https://arxiv.org/html/2510.14108v1#Thmprop1 "Proposition 1. ‣ 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets"), we can find a useful relation between the characteristic functions of XX and VV above. This provides potential to find a general reverse direction: in particular, from a distribution XX, we may find a VV satisfying X​=𝑑​θ​V+V​ZX\overset{d}{=}\theta V+\sqrt{V}Z (fixing σ=1\sigma=1 in accordance with remark [1](https://arxiv.org/html/2510.14108v1#Thmremark1 "Remark 1. ‣ 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")).

If we wish to consider the class of Gaussian variance-mean mixtures, it is natural to ask how the properties of the mixing distribution affect the full distribution.

Suppose the distribution of XX is known. Consider defining the distribution of VV implicitly through X​d=​θ​V+V​Z,X{d\over=}\theta V+\sqrt{V}Z, with VV and ZZ independent. Proposition [1](https://arxiv.org/html/2510.14108v1#Thmprop1 "Proposition 1. ‣ 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets") yields a candidate for the characteristic function of VV which could specify distribution of VV by the Levi continuity theorem for characteristic functions.

Define the characteristic function of VV by ψV​(ω)=𝔼​[ei​ω​V]\psi\_{V}(\omega)=\mathbb{E}[e^{i\omega V}], ω∈R.\omega\in R. For fixed ω0∈ℝ\omega\_{0}\in\mathbb{R} consider informally finding the argument t0∈ℂt\_{0}\in\mathbb{C} of ψX​(t)\psi\_{X}(t) for which
"ψV​(ω0)=ψX​(t0)\psi\_{V}(\omega\_{0})=\psi\_{X}(t\_{0})". For this to hold we must have
(i​ω0)=(i​t​θ−t2/2)(i\omega\_{0})=(it\theta-t^{2}/2), a quadratic equation for tt with solutions:

|  |  |  |
| --- | --- | --- |
|  | t0=i​θ±(−1)​(θ2+2​i​ω0)=i​(θ±θ2+2​i​ω0).t\_{0}=i\theta\pm\sqrt{(-1)(\theta^{2}+2i\omega\_{0})}=i\left(\theta\pm\sqrt{\theta^{2}+2i\omega\_{0}}\right). |  |

From Proposition [1](https://arxiv.org/html/2510.14108v1#Thmprop1 "Proposition 1. ‣ 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets"), we have that ψX​(t)=𝔼​[ei​t​X]=𝔼​[e(i​t​θ−t2/2)​V]\psi\_{X}(t)=\mathbb{E}[e^{itX}]=\mathbb{E}[e^{(it\theta-t^{2}/2)V}]. We can then write

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψV​(ω)\displaystyle\psi\_{V}(\omega) | =𝔼​[ei​ω​V]=𝔼​[e(−θ+θ2+2​i​ω)​X],ω∈ℝ\displaystyle=\mathbb{E}[e^{i\omega V}]=\mathbb{E}\left[e^{(-\theta+\sqrt{\theta^{2}+2i\omega})X}\right],\hskip 14.22636pt\omega\in\mathbb{R} |  | (11) |

Either solution works and we consider using the principal root for θ2+2​i​ω0\sqrt{\theta^{2}+2i\omega\_{0}}. This equality is intuitive but not immediate as the domain of ψX​(⋅)\psi\_{X}(\cdot) as a characteristic function is ℝ\mathbb{R}, whereas t0t\_{0} is complex - it remains to justify the existence of this expectation in ([11](https://arxiv.org/html/2510.14108v1#S2.E11 "In 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")). A proof of the existence of this expectation is given in Proposition [2](https://arxiv.org/html/2510.14108v1#Thmprop2 "Proposition 2. ‣ 4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets") in Section [4](https://arxiv.org/html/2510.14108v1#S4 "4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets").

If we want to calculate a density fV​(v)f\_{V}(v) for VV from fX​(x)f\_{X}(x), we can compute ψV​(t)\psi\_{V}(t) through relation ([11](https://arxiv.org/html/2510.14108v1#S2.E11 "In 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")) and then apply the characteristic function inversion formula,

|  |  |  |  |
| --- | --- | --- | --- |
|  | fY​(x)=ψ−1​{ψY​(ω)}​(x)=12​π​limR→∞∫−RRe−ω2/(2​R2)​e−i​ω​x​ψY​(ω)​𝑑ω,f\_{Y}(x)=\psi^{-1}\left\{\psi\_{Y}(\omega)\right\}(x)=\frac{1}{2\pi}\lim\_{R\to\infty}\int\_{-R}^{R}e^{-\omega^{2}/(2R^{2})}e^{-i\omega x}\psi\_{Y}(\omega)d\omega, |  | (12) |

which can be simplified in the case that ψY\psi\_{Y} is itself ℒ1\mathcal{L}^{1} integrable or fYf\_{Y} is sufficiently smooth (i.e. satisfies the Dini criterion, see Katznelson [[11](https://arxiv.org/html/2510.14108v1#bib.bib11)] Thm 2.5 for details),

|  |  |  |  |
| --- | --- | --- | --- |
|  | fY​(x)=ψ−1​{ψY​(ω)}​(x)=12​π​limR→∞∫−RRe−i​ω​x​ψY​(ω)​𝑑ω.f\_{Y}(x)=\psi^{-1}\left\{\psi\_{Y}(\omega)\right\}(x)=\frac{1}{2\pi}\lim\_{R\to\infty}\int\_{-R}^{R}e^{-i\omega x}\psi\_{Y}(\omega)d\omega. |  | (13) |

The method outlines the formulation of an appropriate transform which encompasses the composition mapping fX​(x)↦ψX​(ω)↦ψV​(ω)↦fv​(x)f\_{X}(x)\mapsto\psi\_{X}(\omega)\mapsto\psi\_{V}(\omega)\mapsto f\_{v}(x) .

###### Definition 2 (Variance-mixing transform).

Let XX be a Gaussian variance-mixture such that X=θ​V+V​ZX=\theta V+\sqrt{V}Z for θ∈ℝ\theta\in\mathbb{R}. We define the generalised variance-mixing transform 𝒱θ​[X]\mathcal{V}^{\theta}[X] as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱θ​[X]​(ξ):=ψ−1​{𝔼​[e(−θ+θ2+2​i​ω)​X]}​(ξ)\mathcal{V}^{\theta}\left[X\right](\xi):=\psi^{-1}\left\{\mathbb{E}\left[e^{\left(-\theta+\sqrt{\theta^{2}+2i\omega}\right)X}\right]\right\}(\xi) |  | (14) |

In particular, 𝒱θ​[X]\mathcal{V}^{\theta}\left[X\right] gives the density of the random variable VV in the mixture.

###### Remark 4.

Employing 𝒱θ​[X]\mathcal{V}^{\theta}[X] empirically enables one to infer the stochastic volatility distribution VV directly from the log-return distribution XX: rather than simply testing different distributions for VV and fitting to the data, we can directly infer VV from the price observations XX via a semi-parametric approach which does not rely on the quadratic variation.

To calculate an empirical density for fV​(v)f\_{V}(v) based on a sample of XX, one can map the sample onto the (empirical) characteristic function of VV through equation ([11](https://arxiv.org/html/2510.14108v1#S2.E11 "In 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")) and then apply a DFT to invert this characteristic function back into real space (for a review of empirical characteristic functions, the reader is directed towards Yu [[12](https://arxiv.org/html/2510.14108v1#bib.bib12)])

For the empirical transform 𝒱θ​[X]\mathcal{V}^{\theta}[X], θ\theta is a hyper-parameter - one can scan a range of θ\theta values, infer the distribution of VV and optimise the value of θ\theta using the reconstruction error as the optimisation criterion. Alternatively, one could explore suitable values of θ\theta such as θ=0\theta=0 (so that the transform infers VV through the symmetric case X=V​ZX=\sqrt{V}Z).
We carry out the calculation of 𝒱0​[X]\mathcal{V}^{0}[X] for S&\&P500 log-returns data (January 2022 to January 2024) showing the results in Figure [1](https://arxiv.org/html/2510.14108v1#S2.F1 "Figure 1 ‣ 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets"). The resulting density function appears to be relatively consistent with a Gamma distribution, and justifies the consideration of the Gamma distribution as our example stochastic variance VV.

It is possible that a further study can be carried out by tuning θ\theta appropriately - this would be particularly valuable for cases when the skewness is significantly different from 0, and one cannot reasonably assume a symmetric log-return distribution.

![Refer to caption](Figures/R_plots/ECF_Density.png)


(a)

![Refer to caption](Figures/R_plots/ECF_QQ.png)


(b)

Figure 1: Gamma distribution fit for the stochastic variance V=𝒱0​[X]V=\mathcal{V}^{0}[X] for S&\&P500 daily log returns data XX (January 2022 to January 2024)

## 3 Time-Subordinated Brownian Motion Processes

We have characterised Gaussian variance-mean mixture distributions and now turn to the associated time-subordinated Brownian motion processes. This will follow a similar analysis, considering the Lévy process as a composition mixture of a Gaussian process (a Brownian motion) and a subordinator process as described in Section 1.3 of Applebaum [[13](https://arxiv.org/html/2510.14108v1#bib.bib13)]. First, we clarify our definition of a Brownian motion, as given in 1.2 of Pitman and Yor [[14](https://arxiv.org/html/2510.14108v1#bib.bib14)].

###### Definition 3 (Brownian motion).

Let (Wt)t≥0(W\_{t})\_{t\geq 0} be a standard Wiener process where W0=0W\_{0}=0 a.s. , WtW\_{t} has stationary Gaussian increments Wt+h−Wt∼N​(0,h)W\_{t+h}-W\_{t}\sim N(0,h) where the distributions are independent over non-overlapping time intervals, and WtW\_{t} is continuous a.s.a.s. . Then the process (bt)t≥0(b\_{t})\_{t\geq 0} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | bt=b​(t;θ,σ)=θ​t+σ​Wtb\_{t}=b(t;\theta,\sigma)=\theta t+\sigma W\_{t} |  | (15) |

is a Brownian motion with drift θ∈ℝ\theta\in\mathbb{R} and volatility σ>0\sigma>0.

It is useful to recall the characteristic function for a Brownian motion,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψb​(t;θ,σ)​(u)=exp⁡(i​θ​t​u−12​σ2​t​u2).\psi\_{b(t;\theta,\sigma)}(u)=\exp\left(i\theta tu-\frac{1}{2}\sigma^{2}tu^{2}\right). |  | (16) |

We a characterised variance-mean mixture as a Gaussian with a stochastic mean and variance. In a Brownian motion, the increments have a mean and variance proportional to the size of the time increment, so to create an analogue we seek a way of evaluating the Brownian motion at stochastic, VV distributed time-increments - this is known as a time-subordinated Brownian motion.

###### Definition 4 (Subordinator process).

Suppose VV is an infinitely divisible non-negative distribution. Let (τt)t≥0(\tau\_{t})\_{t\geq 0} be a subordinator process with increments VhV\_{h}. Then τ0=0\tau\_{0}=0 a.s.a.s. , τt\tau\_{t} has stationary VV distributed increments τt+h−τt∼Vh\tau\_{t+h}-\tau\_{t}\sim V\_{h} where the distributions are independent over non-overlapping time intervals, and τt\tau\_{t} is continuous a.s. .

###### Example 1.

We can specify the Gamma process (γt)t≥0(\gamma\_{t})\_{t\geq 0}. It is useful to employ the parametrisation of the Gamma Process in terms of the mean and variance μ=α/β,ν=α/β2\mu=\alpha/\beta,\nu=\alpha/\beta^{2} resp. so that we write Gamma​(α,β)∼Γμ,ν\text{Gamma}(\alpha,\beta)\sim\Gamma\_{\mu,\nu}. The Gamma process then has increments γt+h−γt∼Γμ​h,ν​h\gamma\_{t+h}-\gamma\_{t}\sim\Gamma\_{\mu h,\nu h} so that the cumulative value at time t=Tt=T has distribution
γT∼Γμ​T,ν​T\gamma\_{T}\sim\Gamma\_{\mu T,\nu T}.

Now, we specify VV so that 𝔼​[τt]=t\mathbb{E}[\tau\_{t}]=t. Recall from remark [1](https://arxiv.org/html/2510.14108v1#Thmremark1 "Remark 1. ‣ 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets") that this does not cause a loss of generality in characterising time-subordinated processes below. This is a helpful characterisation as it means that at time TT, the expectation of our random Gamma distributed time 𝔼​[τT]=T\mathbb{E}[\tau\_{T}]=T and we have random fluctuation only about the deterministic time.

We can finally characterise time-subordinated Brownian processes as a composition of a Brownian motion and a subordinator process.

###### Definition 5 (Time-subordinated Brownian motion).

Let (bt)t≥0=b​(t;θ,σ)(b\_{t})\_{t\geq 0}=b(t;\theta,\sigma) be a Brownian motion as in Definition [3](https://arxiv.org/html/2510.14108v1#Thmdefinition3 "Definition 3 (Brownian motion). ‣ 3 Time-Subordinated Brownian Motion Processes ‣ On Time-subordinated Brownian Motion Processes for Financial Markets"), and let (τt)t≥0(\tau\_{t})\_{t\geq 0} be an independent subordinator process as in Definition [4](https://arxiv.org/html/2510.14108v1#Thmdefinition4 "Definition 4 (Subordinator process). ‣ 3 Time-Subordinated Brownian Motion Processes ‣ On Time-subordinated Brownian Motion Processes for Financial Markets"). Then the time-subordinated process (Xt)t≥0(X\_{t})\_{t\geq 0} given by the composition

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Xt=bτt\displaystyle X\_{t}=b\_{\tau\_{t}} | =θ​τt+σ​Wτt,\displaystyle=\theta\tau\_{t}+\sigma W\_{\tau\_{t}}, |  | (17) |

is known as a time-subordinated Brownian motion process.

###### Remark 5.

Breaking down this definition, there are two sources of randomness. First is the Wiener process which acts the same as in the Brownian motion, creating Gaussian noise about the drift θ​t\theta t. However, there is also the random time-subordination, so that we think of the process as first randomly mapping deterministic time onto a subordinated time and then evaluating the Brownian motion at the time change.
Note that one could equivalently understand the process as observing a Brownian motion at randomly distributed times, those times given by τt\tau\_{t}.
For a more detailed review of time-subordinated processes, see section 1.3 of Applebaum [[13](https://arxiv.org/html/2510.14108v1#bib.bib13)].

Figure [2](https://arxiv.org/html/2510.14108v1#S3.F2 "Figure 2 ‣ Remark 5. ‣ 3 Time-Subordinated Brownian Motion Processes ‣ On Time-subordinated Brownian Motion Processes for Financial Markets") illustrates a simulation
22210610^{6} points used to simulate b​(t)b(t) and τ​(t)\tau(t) over 10 units of time i.e. a discretization grid 𝕋\mathbb{T} with Δ​t=10−5\Delta t=10^{-5}.
b​(τ​(t))b(\tau(t)) is evaluated by interpolation: first evaluate τ​(t)\tau(t) for each point t∈𝕋t\in\mathbb{T}, τ​(t)\tau(t) then lies between t−,t+∈𝕋t\_{-},t\_{+}\in\mathbb{T} and b​(τ​(t))b(\tau(t)) is given via interpolation between b​(t−)b(t\_{-}) and b​(t+)b(t\_{+}).
of a time-subordinated Brownian motion - specifically a Variance Gamma process. The original realisation of the Brownian motion b​(t)b(t) is given in the top left, and the realisation of an independent Gamma process τ​(t)\tau(t) is given in the top right. The Subordinated Brownian motion in the two lower sub-figures is given by evaluating the original motion with the time change i.e. (t,b​(t))↦(t,b​(τ​(t)))(t,b(t))\mapsto(t,b(\tau(t))).

* •

  The shading on the left plots demonstrate the effect of the time-subordination. Each band in the Brownian motion plot is mapped onto the corresponding band in the Subordinated motion plot through the time change (i.e. the endpoints of the bands in the top plot are mapped onto the endpoints of the bands on the bottom plot via t↦τ​(t)t\mapsto\tau(t)).
* •

  While the general shape of the motion is mostly preserved, one observes the dilation and contraction of the Brownian motion along the time-axis caused by the time-subordination.
* •

  The colour on the right plots demonstrate the ‘speed’ of the time change over different increments. This is calculated as the mean rate of the Gamma process realised over the increment (i.e. the ratio of the gamma increment to the length of the increment). ‘Speed’ 1 indicates there is no time change on average, ‘speed’ 2 indicates that the time change moves twice as fast as normal time, ‘speed’ 0.5 indicates that the time change is half as fast.
* •

  We see that periods of extreme volatility occur where there is a contraction in the time axis and a higher ‘speed’ of time change (in red). Alternatively, periods of lower volatility correspond to instances of time dilation and a slower ‘speed’ of time change (in blue)

![Refer to caption](Figures/R_plots/TSB_Simulation.png)


Figure 2: Realised components of a Time-subordinated Brownian motion process: VG(t;θ=0.1,σ=0.05,ν=0.05)VG(t;\theta=0.1,\sigma=0.05,\nu=0.05)

We can obtain the density function of the process at time tt by conditioning on a realisation of the time-subordinator (giving a Brownian motion density), and integrating against the subordinator density. Similar to ([4](https://arxiv.org/html/2510.14108v1#S2.E4 "In 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | fXt​(x)=∫ϕ​(x−θ​ξσ​ξ)​fτt​(ξ)​𝑑ξ.f\_{X\_{t}}(x)=\int\phi\left(\dfrac{x-\theta\xi}{\sigma\sqrt{\xi}}\right)f\_{\tau\_{t}}(\xi)d\xi. |  | (18) |

We may also obtain the characteristic function for the process. Again, we condition on realisation of the time-subordinator with a similar method to the proof of Prop. ([2](https://arxiv.org/html/2510.14108v1#S2 "2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")), using the Brownian motion characteristic function ([16](https://arxiv.org/html/2510.14108v1#S3.E16 "In 3 Time-Subordinated Brownian Motion Processes ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")). We then find

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψXt​(u)=𝔼τt​[e(i​u​θ−u2​σ2/2)​τt].\psi\_{X\_{t}}(u)=\mathbb{E}\_{\tau\_{t}}\left[e^{(iu\theta-u^{2}\sigma^{2}/2)\tau\_{t}}\right]. |  | (19) |

###### Example 2.

Specifying the Gamma subordinator process we have the pair,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | fXt​(x)\displaystyle f\_{X\_{t}}(x) | =∫0∞12​π​σ2​g​exp⁡(−(x−θ​g)22​σ2​g)​gtν−1​exp⁡(−gν)νtν​Γ​(tν)​𝑑g\displaystyle=\int\_{0}^{\infty}\dfrac{1}{\sqrt{2\pi\sigma^{2}g}}\exp\left(-\frac{(x-\theta g)^{2}}{2\sigma^{2}g}\right)\dfrac{g^{\frac{t}{\nu}-1}\exp\left(-\frac{g}{\nu}\right)}{\nu^{\frac{t}{\nu}}\Gamma\left(\frac{t}{\nu}\right)}dg |  | (20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ψXt​(u)\displaystyle\psi\_{X\_{t}}(u) | =(1−i​θ​ν​u+σ22​ν​u2)−tν.\displaystyle=\left({1-i\theta\nu u+\frac{\sigma^{2}}{2}\nu u^{2}}\right)^{-\frac{t}{\nu}}. |  | (21) |

Taking the limit as ν↓0\nu\downarrow 0 in the V​GVG process, we obtain weak convergence to a Brownian motion b​(t;θ,σ)b(t;\theta,\sigma) as in ([15](https://arxiv.org/html/2510.14108v1#S3.E15 "In Definition 3 (Brownian motion). ‣ 3 Time-Subordinated Brownian Motion Processes ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")) - one concludes this by observing the characteristic function above converges to that of a Brownian motion and applying Lévy’s continuity Theorem. This should be expected, as the Gamma process subordinating the time becomes degenerate with 0 variance about the mean tt, and there is no time-change for the Brownian motion. This shows that the V​GVG model still contains Brownian motion as a sub-model - this is a particularly useful property if one employs a hypothesis test which nests a Brownian motion model null inside a more general V​GVG model alternative, observing whether ν\nu is significantly greater than 0. This result can similarly be generalised for other subordinator processes parametrised in terms of their variance ν\nu, and taking the limit ν→0\nu\to 0 appropriately.

One could compute the central moments of the V​GVG process from the characteristic function ([19](https://arxiv.org/html/2510.14108v1#S3.E19 "In 3 Time-Subordinated Brownian Motion Processes ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")); however, employing the form ([17](https://arxiv.org/html/2510.14108v1#S3.E17 "In Definition 5 (Time-subordinated Brownian motion). ‣ 3 Time-Subordinated Brownian Motion Processes ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")) simplifies calculations. Conditioning on the Gamma time-subordinator as γt=g\gamma\_{t}=g, the conditional V​GVG process is a Brownian motion and we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | X​(t;θ,σ|γt=g)=θ​g+σ​Wg.X\left(t;\theta,\sigma\big|\gamma\_{t}=g\right)=\theta g+\sigma W\_{g}. |  | (22) |

We can then take the expectation over the Wiener process, and then the expectation over g=γtg=\gamma\_{t} as in A4 of Madan et al. [[6](https://arxiv.org/html/2510.14108v1#bib.bib6)]).
We obtain,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Xt]=θ​t,\displaystyle\mathbb{E}\left[X\_{t}\right]=\theta t,\hskip 5.69046pt |  |
|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(Xt−𝔼​[Xt])2]=(θ2​ν+σ2)​t,\displaystyle\mathbb{E}\left[\left(X\_{t}-\mathbb{E}[X\_{t}]\right)^{2}\right]=(\theta^{2}\nu+\sigma^{2})t,\hskip 5.69046pt |  |
|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(Xt−𝔼​[Xt])3]=(2​θ3​ν2+3​σ2​θ​ν)​t,\displaystyle\mathbb{E}\left[\left(X\_{t}-\mathbb{E}[X\_{t}]\right)^{3}\right]=(2\theta^{3}\nu^{2}+3\sigma^{2}\theta\nu)t, |  |
|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(Xt−𝔼​[Xt])4]=(3​σ4​ν+12​σ2​θ2​ν2+6​θ4​ν3)​t+(3​σ4+6​σ2​θ2​ν+3​θ4​ν2)​t2.\displaystyle\mathbb{E}\left[\left(X\_{t}-\mathbb{E}[X\_{t}]\right)^{4}\right]=(3\sigma^{4}\nu+12\sigma^{2}\theta^{2}\nu^{2}+6\theta^{4}\nu^{3})t+(3\sigma^{4}+6\sigma^{2}\theta^{2}\nu+3\theta^{4}\nu^{2})t^{2}. |  |

If we consider the case θ=0\theta=0, then we have no skewness as the third central moment becomes 0. Furthermore, the kurtosis would then be given by 3​(1+ν/t)3(1+\nu/t) so that ν\nu represents the percentage excess kurtosis over the Brownian motion process over a unit time increment (where over longer time increments the excess kurtosis decreases to 0 linearly in tt - an expected result considering the central limit theorem).

However, for θ≠0\theta\neq 0 the variance of the process is higher than that of the Brownian motion - this increase in average quadratic variation stems from additional variance contributions from the random drift component under the time-subordination (being deterministic, the drift component in a Brownian motion does not contribute to the variance). This is key to differences in option prices under a regular GBM model and a time-subordinated model - in particular, long volatility options are often priced higher under a time-subordinated model.

## 4 Time-Change Decomposition

In a similar manner to the variance-mixing transform through which one can transform a Gaussian mean-variance mixture X=θ​V+V​ZX=\theta V+\sqrt{V}Z into its stochastic variance VV, one can transform a subordinated Brownian motion directly into its subordinating time-change process. This follows the same procedure as the variance-mixture transform in Definition [2](https://arxiv.org/html/2510.14108v1#Thmdefinition2 "Definition 2 (Variance-mixing transform). ‣ 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets"). Here, we observe the evolution of the distribution for the subordinating time-change process over time-increments of varying size.

Suppose we have a time-changed Brownian motion (Xt)t≥0(X\_{t})\_{t\geq 0} such that ∀t≥0\forall t\geq 0, Xt=θ​τt+WτtX\_{t}=\theta\tau\_{t}+W\_{\tau\_{t}} for some θ∈ℝ\theta\in\mathbb{R} where (Wt)t≥0(W\_{t})\_{t\geq 0} is a standard Wiener process and (τt)t≥0(\tau\_{t})\_{t\geq 0} is the independent time-change. If we want to compute the density fτ​(ξ,t)f\_{\tau}(\xi,t) of the time-change, we can use the time-change transform defined below. This is motivated by a combination of Definition [2](https://arxiv.org/html/2510.14108v1#Thmdefinition2 "Definition 2 (Variance-mixing transform). ‣ 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets") and the theory of Laplace exponents for Lévy processes, which take a similar form, characterising a Lévy process in terms of its Laplace transform (see 1.3.2 of Applebaum [[13](https://arxiv.org/html/2510.14108v1#bib.bib13)]).

It is particularly important to highlight case that θ=0\theta=0, i.e. the no-drift case where Xt=WτtX\_{t}=W\_{\tau\_{t}} through the following theorem of Skorokhod [[7](https://arxiv.org/html/2510.14108v1#bib.bib7)], translated in [[15](https://arxiv.org/html/2510.14108v1#bib.bib15)], which asserts that any probability distribution can be represented as a stopped Brownian motion.

###### Theorem 1.

For a given probability measure μ\mu on ℝ\mathbb{R} such that

|  |  |  |
| --- | --- | --- |
|  | ∫ℝ|x|​𝑑μ​(x)<∞,∫ℝx​𝑑μ​(x)=0,\int\_{\mathbb{R}}|x|d\mu(x)<\infty,\hskip 14.22636pt\int\_{\mathbb{R}}xd\mu(x)=0, |  |

there exists a stopping time TT such that WT∼μW\_{T}\sim\mu and the stopped process (Bt∧T)t≥0(B\_{t\wedge T})\_{t\geq 0} is a uniformly integrable martingale.

There is a vast literature of different solutions constructing the stopping time TT in the Theorem, as summarised by Obłój [[16](https://arxiv.org/html/2510.14108v1#bib.bib16)]. Extending the result, Monroe [[8](https://arxiv.org/html/2510.14108v1#bib.bib8)] showed the following key Theorem.

###### Theorem 2.

A process (Xs,ℱs)(X\_{s},\mathcal{F}\_{s}) can be embedded in Brownian motion if and only if (Xs,ℱs)(X\_{s},\mathcal{F}\_{s}) is a local semi-martingale. To embed a process in Brownian motion is to find a Wiener process (Wt,𝒢s)(W\_{t},\mathcal{G}\_{s}) and an increasing family of 𝒢s\mathcal{G}\_{s} stopping times TsT\_{s}, such that WTsW\_{T\_{s}} has the same joint distributions as XsX\_{s}.

This means that any semi-martingale XtX\_{t} can be represented as WτtW\_{\tau\_{t}} for some increasing process τt\tau\_{t} 333It is however important to note that the stopping times TsT\_{s} do not necessarily have to correspond to a Lévy subordinator process. For our study, as explained by Veraart and Winkel [[4](https://arxiv.org/html/2510.14108v1#bib.bib4)]: ‘In the light of the Fundamental Theorem of Asset Pricing, this means that every arbitrage-free model can be viewed as time-changed Brownian motion’ which provides a strong justification for considering this inverse problem for the cases we model the time-change with a subordinator. The transform below represents an alternate characterisation of the subordinator without computing the quadratic variation.

###### Definition 6.

Let X=(Xt)t≥0X=(X\_{t})\_{t\geq 0} be a time-changed Brownian motion where Xt=θ​τt+WτtX\_{t}=\theta\tau\_{t}+W\_{\tau\_{t}} for θ∈ℝ\theta\in\mathbb{R}. We define the time-change transform 𝒮θ​[X]\mathcal{S}^{\theta}[X] as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮θ​[X]​(ξ,t):=ψ−1​{𝔼​[e(−θ+θ2+2​i​ω)​Xt]}​(ξ).\mathcal{S}^{\theta}\left[X\right](\xi,t):=\psi^{-1}\left\{\mathbb{E}\left[e^{\left(-\theta+\sqrt{\theta^{2}+2i\omega}\right)X\_{t}}\right]\right\}(\xi). |  | (23) |

In particular, 𝒮θ​[X]\mathcal{S}^{\theta}\left[X\right] gives the density for the subordinator τt\tau\_{t}.

###### Remark 6.

Fixing the value of tt, this definition is identical to that of the variance-mixture transform (Definition [2](https://arxiv.org/html/2510.14108v1#Thmdefinition2 "Definition 2 (Variance-mixing transform). ‣ 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")): The inner expectation represents relation ([11](https://arxiv.org/html/2510.14108v1#S2.E11 "In 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")) mapping XtX\_{t} onto the characteristic function of τt\tau\_{t}, while ψ−1\psi^{-1} represents the characteristic function inversion. The transform encompasses the composition mapping fX​(x,t)↦ψXt​(u)↦ψτt​(u)↦fτt​(τ)f\_{X}(x,t)\mapsto\psi\_{X\_{t}}(u)\mapsto\psi\_{\tau\_{t}}(u)\mapsto f\_{\tau\_{t}}(\tau) as shown in Figure [3](https://arxiv.org/html/2510.14108v1#S4.F3 "Figure 3 ‣ Remark 6. ‣ 4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets") below.

fXt​(x)\textstyle f\_{X\_{t}}(x)

ψXt​(ω)\textstyle\psi\_{X\_{t}}(\omega)

ψτt​(ω)\textstyle\psi\_{\tau\_{t}}(\omega)

fτt​(τ)\textstyle f\_{\tau\_{t}}(\tau)
ψ​(⋅)\color[rgb]{.75,.75,.75}\definecolor[named]{pgfstrokecolor}{rgb}{.75,.75,.75}\pgfsys@color@gray@stroke{.75}\pgfsys@color@gray@fill{.75}\psi(\cdot)

ω↦−i​(θ+θ2+2​i​ω)\color[rgb]{.75,.75,.75}\definecolor[named]{pgfstrokecolor}{rgb}{.75,.75,.75}\pgfsys@color@gray@stroke{.75}\pgfsys@color@gray@fill{.75}\omega\mapsto-i\left(\theta+\sqrt{\theta^{2}+2i\omega}\right)

ψ−1​(⋅)\color[rgb]{.75,.75,.75}\definecolor[named]{pgfstrokecolor}{rgb}{.75,.75,.75}\pgfsys@color@gray@stroke{.75}\pgfsys@color@gray@fill{.75}\psi^{-1}(\cdot)

𝒮θ​[⋅]\textstyle\mathcal{S}^{\theta}[\cdot]


Figure 3: Components of 𝒮θ​[⋅]\mathcal{S}^{\theta}[\cdot]

As discussed above, this allows us to transform the full process (Xt)t≥0(X\_{t})\_{t\geq 0} directly into its subordinator process (τt)t≥0(\tau\_{t})\_{t\geq 0} via a semi-parametric approach. This transform allows one to explore properties of the hidden subordinating process (γt)t≥0(\gamma\_{t})\_{t\geq 0} by observing only the price evolution process (Xt)t≥0(X\_{t})\_{t\geq 0}. In effect, one reduces the study of the composition of two random objects (the Brownian motion and the subordinator) into the study of just one (the subordinator).

The reader may question the existence of the transform 𝒮θ​[X]\mathcal{S}^{\theta}\left[X\right] as this is not an obvious result. The central issue lies in verifying that the expectation ([25](https://arxiv.org/html/2510.14108v1#S4.E25 "In 4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")) below exists - this will be resolved by employing a conditional expectation and extending the notion of the characteristic function to have a complex domain as in Lukacs [[17](https://arxiv.org/html/2510.14108v1#bib.bib17)].

###### Proposition 2.

Suppose X=θ​V+V​ZX=\theta V+\sqrt{V}Z is a Gaussian variance-mean mixture. Then the transform 𝒱θ​[X]\mathcal{V}^{\theta}[X] given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱θ​[X]​(ξ):=ψ−1​{𝔼​[e(−θ+θ2+2​i​ω)​X]}​(ξ)\mathcal{V}^{\theta}\left[X\right](\xi):=\psi^{-1}\left\{\mathbb{E}\left[e^{\left(-\theta+\sqrt{\theta^{2}+2i\omega}\right)X}\right]\right\}(\xi) |  | (24) |

exists and equals fV​(ξ)f\_{V}(\xi), the density of VV.

We first want to verify the existence of the inner expectation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[e(−θ+θ2+2​i​ω)​X]=𝔼​[e(−θ+θ2+2​i​ω)​(θ​V+V​Z)]\mathbb{E}\left[e^{\left(-\theta+\sqrt{\theta^{2}+2i\omega}\right)X}\right]=\mathbb{E}\left[e^{\left(-\theta+\sqrt{\theta^{2}+2i\omega}\right)\left(\theta V+\sqrt{V}Z\right)}\right] |  | (25) |

for all ω∈ℝ\omega\in\mathbb{R}, and show that it is equal to ψV​(ω)\psi\_{V}(\omega) which must exist as the characteristic function of a real random variable VV. We can then conclude that the transform exists with the characteristic function inverse.

This expectation ([25](https://arxiv.org/html/2510.14108v1#S4.E25 "In 4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")) has a similar form to the characteristic and moment generating functions; however, these cannot be applied directly as their domains only cover the imaginary and real axes respectively, while the necessary domain of integration in ([25](https://arxiv.org/html/2510.14108v1#S4.E25 "In 4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")) is ℐ={−θ+θ2+2​i​ω|ω∈ℝ}\mathcal{I}=\{-\theta+\sqrt{\theta^{2}+2i\omega}\hskip 2.84544pt\big|\hskip 2.84544pt\omega\in\mathbb{R}\}. This leads us to consider an extended characteristic function which extends the domain of the characteristic function into the complex plane. For a more detailed review of analytic characteristic functions and their applications, the reader is directed to Chapter 7 of Lukacs [[17](https://arxiv.org/html/2510.14108v1#bib.bib17)].

###### Definition 7.

Let YY be a real-valued random variable with density fY​(y)f\_{Y}(y), and 𝒟⊃ℝ\mathcal{D}\supset\mathbb{R} be a region in the complex plane containing the real line such that the Fourier integral

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΨY​(z)=∫ℝei​y​z​fY​(y)​𝑑y\Psi\_{Y}(z)=\int\_{\mathbb{R}}e^{iyz}f\_{Y}(y)dy |  | (26) |

is analytic in 𝒟\mathcal{D}. Then ΨY\Psi\_{Y} is the analytic continuation of ψY\psi\_{Y} in the domain 𝒟\mathcal{D}.

In general, it is not possible to analytically extend the characteristic function to the entire complex plane. Indeed, any distribution with a moment-generating function which is undefined for some parts of the real line (such as the Variance-Gamma) cannot be extended to the entire complex plane, as there will be a point on the imaginary axis where the Fourier integral is undefined 444As a simple example, the standard Laplace distribution (as a special case of the Variance Gamma) has density fL​(x)=e−|x|/2f\_{L}(x)=e^{-|x|}/2 and characteristic function ψL​(z)=(1+z2)−1\psi\_{L}(z)=(1+z^{2})^{-1} which has singularities at ±i\pm i, and so there is no analytic continuation to the entire plane.. To this end, Lukacs shows that analytic characteristic functions are regular in a horizontal strip (the strip of regularity), where there are singularities on the intersection of the boundary and the imaginary axis (though in some cases this strip is the entire plane, and there are no singularities). The characteristic function is represented by the integral ([26](https://arxiv.org/html/2510.14108v1#S4.E26 "In Definition 7. ‣ 4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")) inside this domain. Lukacs remarks that analytic characteristic functions can often be continued analytically beyond this strip of regularity if the singularities are suitably avoided, as we will require for our transform - we show that the Fourier integral is is well-defined on ℐ={−θ+θ2+2​i​ω|ω∈ℝ}\mathcal{I}=\{-\theta+\sqrt{\theta^{2}+2i\omega}\hskip 2.84544pt\big|\hskip 2.84544pt\omega\in\mathbb{R}\} as well as ℝ\mathbb{R}.

Lukacs also shows that for distributions with moment-generating functions defined on the entire real line, the characteristic function can be extended to the entire complex plane. In particular, the Gaussian has this property - we show explicitly the existence of an analytic continuation of the Gaussian characteristic function in the lemma below. This provides a particularly useful step towards our goal.

###### Lemma 1.

Let ZZ be a standard Gaussian. Then ΨZ\Psi\_{Z} is entire in the complex plane ℂ\mathbb{C} with ΨZ​(z)=e−z2/2\Psi\_{Z}(z)=e^{-z^{2}/2}.

###### Proof.

Fix z∈ℂz\in\mathbb{C}. We begin by completing the square in the Fourier integral ([26](https://arxiv.org/html/2510.14108v1#S4.E26 "In Definition 7. ‣ 4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ℝei​x​z​e−x2/22​π​𝑑x=e−z2/2​∫ℝ12​π​e−(x−i​z)2/2​𝑑x.\int\_{\mathbb{R}}e^{ixz}\dfrac{e^{-x^{2}/2}}{\sqrt{2\pi}}dx=e^{-z^{2}/2}\int\_{\mathbb{R}}\dfrac{1}{\sqrt{2\pi}}e^{-(x-iz)^{2}/2}dx. |  | (27) |

This already has the desired form - once we show that the integral on the RHS is equal to 11 we may conclude. Let L>|z|L>|z| and consider the finite integral,

|  |  |  |  |
| --- | --- | --- | --- |
|  | IL=∫−LL12​π​e−(x−i​z)2/2​𝑑x=∫𝒞112​π​e−ξ2/2​𝑑ξ,I\_{L}=\int\_{-L}^{L}\dfrac{1}{\sqrt{2\pi}}e^{-(x-iz)^{2}/2}dx=\int\_{\mathcal{C}\_{1}}\dfrac{1}{\sqrt{2\pi}}e^{-\xi^{2}/2}d\xi, |  | (28) |

where 𝒞1\mathcal{C}\_{1} is the straight line segment −L−i​z→L−i​z-L-iz\to L-iz.
Letting L→∞L\to\infty, I∞I\_{\infty} is the integral we want to evaluate (the integral RHS of ([27](https://arxiv.org/html/2510.14108v1#S4.E27 "In 4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets"))). Let 𝒞\mathcal{C} be the closed loop contour 𝒞=𝒞1∪𝒞2∪𝒞3∪𝒞4\mathcal{C}=\mathcal{C}\_{1}\cup\mathcal{C}\_{2}\cup\mathcal{C}\_{3}\cup\mathcal{C}\_{4} encompassing the four line segments (a parallelogram)

|  |  |  |
| --- | --- | --- |
|  | −L−i​z​⟶𝒞1​L−i​z​⟶𝒞2​L​⟶𝒞3−L​⟶𝒞4−L−i​z.-L-iz\overset{\mathcal{C}\_{1}}{\longrightarrow}L-iz\overset{\mathcal{C}\_{2}}{\longrightarrow}L\overset{\mathcal{C}\_{3}}{\longrightarrow}-L\overset{\mathcal{C}\_{4}}{\longrightarrow}-L-iz. |  |

We bound the integrals over 𝒞2\mathcal{C}\_{2} and 𝒞4\mathcal{C}\_{4} using the M-L inequality,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∫𝒞212​π​e−ξ2/2​𝑑ξ|≤|z|2​π​supξ∈𝒞2|e−ξ2/2|≤|z|2​π​e−(L−|z|)2/2,\displaystyle\left|\int\_{\mathcal{C}\_{2}}\dfrac{1}{\sqrt{2\pi}}e^{-\xi^{2}/2}d\xi\right|\leq\dfrac{|z|}{\sqrt{2\pi}}\sup\_{\xi\in\mathcal{C}\_{2}}\left|e^{-\xi^{2}/2}\right|\leq\dfrac{|z|}{\sqrt{2\pi}}e^{-(L-|z|)^{2}/2}, |  | (29) |

with the same bound for the integral over 𝒞4\mathcal{C}\_{4}. Taking the limit as L→∞L\to\infty, the bound goes to 0 so that the integrals over 𝒞2\mathcal{C}\_{2} and 𝒞4\mathcal{C}\_{4} vanish as L→∞L\to\infty. As ϕ​(ξ)=e−ξ2/2/2​π\phi(\xi)=e^{-\xi^{2}/2}/\sqrt{2\pi} is entire, its integral over the closed loop 𝒞\mathcal{C} is 0 for all |L|>z|L|>z. This means that in the limit L→∞L\to\infty,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫𝒞112​π​e−ξ2/2​𝑑ξ⏟=I∞+0+∫𝒞312​π​e−ξ2/2​𝑑ξ+0=0.\underbrace{\int\_{\mathcal{C}\_{1}}\dfrac{1}{\sqrt{2\pi}}e^{-\xi^{2}/2}d\xi}\_{=I\_{\infty}}+0+\int\_{\mathcal{C}\_{3}}\dfrac{1}{\sqrt{2\pi}}e^{-\xi^{2}/2}d\xi+0=0. |  | (30) |

But for L→∞L\to\infty the integral over 𝒞3\mathcal{C}\_{3} is just the Gaussian integral (in the reverse direction),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫𝒞312​π​e−ξ2/2​𝑑ξ=∫∞−∞12​π​e−ξ2/2​𝑑ξ=−1.\int\_{\mathcal{C}\_{3}}\dfrac{1}{\sqrt{2\pi}}e^{-\xi^{2}/2}d\xi=\int\_{\infty}^{-\infty}\dfrac{1}{\sqrt{2\pi}}e^{-\xi^{2}/2}d\xi=-1. |  | (31) |

So indeed I∞=1I\_{\infty}=1 and we conclude.
∎

With this in hand, we can return to the proof of Proposition [2](https://arxiv.org/html/2510.14108v1#Thmprop2 "Proposition 2. ‣ 4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets").

###### Proof.

Fix ω∈ℝ\omega\in\mathbb{R}. First, we condition555Clearly this assumes the original expectation exists. We argue this a posteriori. the expectation on VV,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[e(−θ+θ2+2​i​ω)​(θ​V+V​Z)]\displaystyle\mathbb{E}\left[e^{\left(-\theta+\sqrt{\theta^{2}+2i\omega}\right)\left(\theta V+\sqrt{V}Z\right)}\right] | =𝔼V​[𝔼Z​[e(−θ+θ2+2​i​ω)​(θ​V+V​Z)|V]]\displaystyle=\mathbb{E}\_{V}\left[\mathbb{E}\_{Z}\left[e^{\left(-\theta+\sqrt{\theta^{2}+2i\omega}\right)\left(\theta V+\sqrt{V}Z\right)}\big|V\right]\right] |  | (32) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼V​[e(−θ2+θ​θ2+2​i​ω)​V​𝔼Z​[e(−θ+θ2+2​i​ω)​V​Z|V]].\displaystyle=\mathbb{E}\_{V}\left[e^{\left(-\theta^{2}+\theta\sqrt{\theta^{2}+2i\omega}\right)V}\mathbb{E}\_{Z}\left[e^{\left(-\theta+\sqrt{\theta^{2}+2i\omega}\right)\sqrt{V}Z}\big|V\right]\right]. |  | (33) |

Using Lemma [1](https://arxiv.org/html/2510.14108v1#Thmlemma1 "Lemma 1. ‣ 4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets"), the inner conditional expectation exists and is given by,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼Z​[e(−θ+θ2+2​i​ω)​V​Z|V]\displaystyle\mathbb{E}\_{Z}\left[e^{\left(-\theta+\sqrt{\theta^{2}+2i\omega}\right)\sqrt{V}Z}\big|V\right] | =ΨZ​(−i​(−θ+θ2+2​i​ω)​V)=e−(−i)2​(−θ+θ2+2​i​ω)2​V/2\displaystyle=\Psi\_{Z}\left(-i\left(-\theta+\sqrt{\theta^{2}+2i\omega}\right)\sqrt{V}\right)=e^{-(-i)^{2}\left(-\theta+\sqrt{\theta^{2}+2i\omega}\right)^{2}V/2} |  | (34) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =e(θ2+θ2+2​i​ω−2​θ​θ2+2​i​ω)​V/2=ei​ω​V​e−(−θ2+θ​θ2+2​i​ω)​V,\displaystyle=e^{\left(\theta^{2}+\theta^{2}+2i\omega-2\theta\sqrt{\theta^{2}+2i\omega}\right)V/2}=e^{i\omega V}e^{-\left(-\theta^{2}+\theta\sqrt{\theta^{2}+2i\omega}\right)V}, |  | (35) |

so that ([33](https://arxiv.org/html/2510.14108v1#S4.E33 "In 4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")) reduces down perfectly to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼V​[e(−θ2+θ​θ2+2​i​ω)​V​𝔼Z​[e(−θ+θ2+2​i​ω)​V​Z|V]]=𝔼​[ei​ω​V].\mathbb{E}\_{V}\left[e^{\left(-\theta^{2}+\theta\sqrt{\theta^{2}+2i\omega}\right)V}\mathbb{E}\_{Z}\left[e^{\left(-\theta+\sqrt{\theta^{2}+2i\omega}\right)\sqrt{V}Z}\big|V\right]\right]=\mathbb{E}\left[e^{i\omega V}\right]. |  | (36) |

As VV is a real random variable this expectation (the characteristic function of VV) must exist so we have indeed verified that ([25](https://arxiv.org/html/2510.14108v1#S4.E25 "In 4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")) exists for all ω∈ℝ\omega\in\mathbb{R} as desired. We conclude the existence of the transform with the existence of the characteristic function inverse

|  |  |  |  |
| --- | --- | --- | --- |
|  | fV​(x)=ψ−1​{E​[ei​ω​V]}​(x)=12​π​limR→∞∫−RRe−ω2/(2​R2)​e−i​ω​x​ψY​(ω)​𝑑ω.f\_{V}(x)=\psi^{-1}\left\{E\left[e^{i\omega V}\right]\right\}(x)=\frac{1}{2\pi}\lim\_{R\to\infty}\int\_{-R}^{R}e^{-\omega^{2}/(2R^{2})}e^{-i\omega x}\psi\_{Y}(\omega)d\omega. |  | (37) |

∎

As discussed after Remark [3](https://arxiv.org/html/2510.14108v1#Thmremark3 "Remark 3. ‣ 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets"), the inversion can be simplified in the case that fYf\_{Y} is smooth or satisfies the (weaker) Dini criterion at xx:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫−11|fY​(x+t)−fY​(x)t|​𝑑t<∞,\int\_{-1}^{1}\left|\dfrac{f\_{Y}(x+t)-f\_{Y}(x)}{t}\right|dt<\infty, |  | (38) |

(see Katznelson [[11](https://arxiv.org/html/2510.14108v1#bib.bib11)] Theorem 2.5 for a justification), or ψY\psi\_{Y} is itself ℒ1\mathcal{L}^{1} integrable. If any of these criteria are met, then we can recover the density with the simplified inversion formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | fY​(x)=ψ−1​{ψY​(ω)}​(x)=12​π​limR→∞∫−RRe−i​ω​x​ψY​(ω)​𝑑ω.f\_{Y}(x)=\psi^{-1}\left\{\psi\_{Y}(\omega)\right\}(x)=\frac{1}{2\pi}\lim\_{R\to\infty}\int\_{-R}^{R}e^{-i\omega x}\psi\_{Y}(\omega)d\omega. |  | (39) |

## 5 Example Empirical Analysis of a Decomposed Time-Change Process

Empirically, we observe the full distribution XX (the log returns data) and we wish to understand the subordinating, time-change process. We can fix a vector containing different values of time increments tt (holding periods), and then apply this transform as in remark ([4](https://arxiv.org/html/2510.14108v1#Thmremark4 "Remark 4. ‣ 2 Gaussian Variance-Mean Mixtures ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")) to data across each time increment size to study the evolution of the subordinator process as the size of the time increment increases (e.g. for a log-return process, observing the evolution of the process over periods of 1 day, multiple days, or a week). This allows one to: a) characterise the subordinator process and b) observe whether the Lévy process assumptions are justified. Assuming that the value of θ\theta is given (e.g. θ=0\theta=0 for a semi-martingale assumption in accordance with Theorem [2](https://arxiv.org/html/2510.14108v1#Thmthm2 "Theorem 2. ‣ 4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")), this directly provides an explicit form for the evolution of the time-change.

We show the results of naïvely applying the transform to daily S&\&P500 log returns data by fixing θ=0\theta=0 in Figure [4](https://arxiv.org/html/2510.14108v1#S5.F4 "Figure 4 ‣ 5 Example Empirical Analysis of a Decomposed Time-Change Process ‣ On Time-subordinated Brownian Motion Processes for Financial Markets"). This is done by calculating the empirical characteristic function of VV, ψ^V​(t)\hat{\psi}\_{V}(t) from sample log returns {xj}j=0N−1\{x\_{j}\}\_{j=0}^{N-1} and passing this through a DFT to return f^V​(v)\hat{f}\_{V}(v).

![Refer to caption](Figures/R_plots/Gamma_Fits_1-20.png)


(a)

![Refer to caption](Figures/R_plots/Gamma_QQ_1-20.png)


(b)

Figure 4: Fit of Gamma process as the subordinator process for S&\&P500 daily log returns (January 2022 to January 2024) under the time-subordinator transform

The resulting distributions appear relatively consistent with a Gamma distribution, and justify the consideration of the Gamma process as the subordinator process (though there is still room for improvement). Figure (a) also appears to show an increase in the mean and variance of the distributions as the size of the time-increments increases. We visualise the evolution of the empirical time-change process, and the fitted Gamma process over different sized time-increments in Figure [5](https://arxiv.org/html/2510.14108v1#S5.F5 "Figure 5 ‣ 5 Example Empirical Analysis of a Decomposed Time-Change Process ‣ On Time-subordinated Brownian Motion Processes for Financial Markets").

![Refer to caption](Figures/R_plots/Empirical_Periods.png)


(a)

![Refer to caption](Figures/R_plots/Gamma_Periods.png)


(b)

Figure 5: Evolution of (a) the empirical time-change process and (b) the fitted Gamma process for S&\&P500 daily log returns (January 2022 to January 2024) from the time-change transform

Analysing this Figure, the mean does indeed increase with the size of the time-increments (days) of the process, and the variance around the mean increases similarly too. This is confirmed by evaluating μ\mu and ν\nu over the different time-periods in Figure [6](https://arxiv.org/html/2510.14108v1#S5.F6 "Figure 6 ‣ 5 Example Empirical Analysis of a Decomposed Time-Change Process ‣ On Time-subordinated Brownian Motion Processes for Financial Markets").

![Refer to caption](Figures/R_plots/Mu_periods.png)


(a)

![Refer to caption](Figures/R_plots/Nu_periods.png)


(b)

Figure 6: The mean and variance of the fitted Gamma process for θ=0\theta=0

However, the assumption that the mean and variance of the distribution of γt\gamma\_{t} increase linearly with time (i.e γt+h−γt∼Γμ​h,ν​h\gamma\_{t+h}-\gamma\_{t}\sim\Gamma\_{\mu h,\nu h}) is not quite true - the rates of increase appear to slow over time. This suggests that simple Lévy subordinator assumptions may not be entirely appropriate as these would imply a linear trend in both variables over time, and that the true time-change dynamics (in correspondence with Theorem [2](https://arxiv.org/html/2510.14108v1#Thmthm2 "Theorem 2. ‣ 4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")) are more nuanced.

These findings present good scope for future study. For example if we drop the semi-martingale assumption (and so cannot refer to Theorem [2](https://arxiv.org/html/2510.14108v1#Thmthm2 "Theorem 2. ‣ 4 Time-Change Decomposition ‣ On Time-subordinated Brownian Motion Processes for Financial Markets")) and don’t assume the value of the hyper-parameter θ\theta, one again needs to tune this value as in the case for the variance-mixture transform (here the interested reader is directed towards Masuda (2014) [[18](https://arxiv.org/html/2510.14108v1#bib.bib18)]). As the drift term interacts with both the mean and variance of the time-subordinator, perhaps we can expect improvement over longer time periods where the Lévy process assumptions may be more appropriate. One could even try to include time series dependence for these parameters as in Mercuri and Bellini [[19](https://arxiv.org/html/2510.14108v1#bib.bib19)] (2010); however, for our study we wish to consider inference based on a simpler time-subordination mapping (i.e. modelling the economically relevant market ‘business time’ as stochastic), and introducing time-series dependence complicates this viewpoint dramatically.

## 6 Discussion

This paper explores the concept of stochastic time change in modelling stock-price dynamics, first presenting results on Gaussian variance-mean mixtures and generalising to the class of continuous time-subordinated Brownian motion models. We explore the Variance Gamma process as a key example throughout.

We detail a Fourier method to consider the appropriate variance distribution in the Gaussian variance-mixture and formulate the time-subordinator transform which reduces the study of a subordinated Brownian motion process to the more focused study of its subordinating process by yielding an estimate for the subordinating distribution without using the quadratic variation. We ultimately prove the theoretical existence of this transform for application.

A brief empirical study of log-returns data from the S&\&P500 market using this transform follows - we find the Gamma process appears to be an appropriate subordinator process for the Brownian motion for the data; however, the Lévy subordinator assumptions appear too restrictive, providing scope for future study into model extensions.

## Acknowledgements

We would like to acknowledge the Imperial-MIT International Research Opportunities Programme without which this research collaboration would not have been possible. Rohan Shenoy would like to acknowledge the financial support provided by the Mathematics Department at Imperial College London, the Imperial International Relations Office, and the UK Government’s Turing Scheme.

## References

* [1]

  Fischer Black and Myron Scholes.
  The pricing of options and corporate liabilities.
  Journal of political economy, 81(3):637, 1973.
* [2]

  S. S. Shapiro and M. B. Wilk.
  An analysis of variance test for normality (complete samples).
  Biometrika, 52(3/4):591–611, 1965.
* [3]

  Peter K. Clark.
  A subordinated stochastic process model with finite variance for speculative prices.
  Econometrica, 41(1):135–155, 1973.
* [4]

  Almut Veraart and Matthias Winkel.
  Time change, volume 4, pages 1812–1816.
  John Wiley & Sons Ltd, 2010.
* [5]

  Frank Milne and Dilip Madan.
  Option pricing with v. g. martingale components.
  Queen’s University, 1991.
* [6]

  Dilip Madan, Peter Carr, and Eric Chang.
  The variance gamma process and option pricing.
  European Finance Review, page 79–105, 1998.
* [7]

  Anatoliy Skorokhod.
  Issledovaniya po teorii sluchainykh protsessov, 1961.
* [8]

  Itrel Monroe.
  On embedding right continuous martingales in brownian motion.
  The Annals of Mathematical Statistics, 43(4):1293–1311, 1972.
* [9]

  Gideon Schwarz Lester Dubins.
  On continuous martingales.
  Proceedings of the National Academy of Sciences of the United States of America, 53, 1965.
* [10]

  J. Kent O. Barndorff-Nielsen and M. Sørensen.
  Normal variance-mean mixtures and z distributions.
  International Statistical Review Vol. 50, No. 2, pages 145–159, 1982.
* [11]

  Yitzhak Katznelson.
  An Introduction to Harmonic Analysis.
  Cambridge Mathematical Library. Cambridge University Press, 3 edition, 2004.
* [12]

  Jun Yu.
  Empirical characteristic function estimation and its applications.
  Econometric Reviews, 23(2):93–123, 2004.
* [13]

  David Applebaum.
  Lévy Processes and Stochastic Calculus.
  Cambridge Studies in Advanced Mathematics. Cambridge University Press, 2004.
* [14]

  Jim Pitman and Marc Yor.
  A guide to brownian motion and related stochastic processes, 2018.
* [15]

  Anatoliy Skorokhod.
  Studies in the theory of random processes. (translated from the russian by scripta technica, inc), 1965.
* [16]

  Jan Obłój.
  The skorokhod embedding problem and its offspring.
  Probability Surveys, 1(none), January 2004.
* [17]

  Eugene Lukacs.
  Characteristic functions.
  Griffin, 1970.
* [18]

  Hiroki Masuda.
  Parametric estimation of Lévy processes, 2014.
* [19]

  Lorenzo Mercuri and Fabio Bellini.
  Option pricing in a dynamic variance-gamma model.
  Dipartimento di Metodi Quantitativi, Università di Milano Bicocca, Italy, 03 2010.