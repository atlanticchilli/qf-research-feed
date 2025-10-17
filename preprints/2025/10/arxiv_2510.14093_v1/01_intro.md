---
authors:
- Rohan Shenoy
- Peter Kempthorne
doc_id: arxiv:2510.14093v1
family_id: arxiv:2510.14093
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: The Variance Gamma Process for Option Pricing
url_abs: http://arxiv.org/abs/2510.14093v1
url_html: https://arxiv.org/html/2510.14093v1
venue: arXiv q-fin
version: 1
year: 2025
---


Rohan Shenoy
Department of Mathematics, Imperial College London, rohan.shenoy22@imperial.ac.uk

Peter Kempthorne
Department of Mathematics, Massachusetts Institute of Technology, kemp2@mit.edu

(August 2024)

###### Abstract

This paper explores the concept of random-time subordination in modelling stock-price dynamics, and
We first present results on the Laplace distribution as a Gaussian variance-mixture, in particular a more efficient volatility estimation procedure through the absolute moments. We generalise the Laplace model to characterise the powerful variance gamma model of Madan et al [[1](https://arxiv.org/html/2510.14093v1#bib.bib1)] as a Gamma time-subordinated Brownian motion to price European call options via an Esscher transform method. We find that the Variance Gamma model is able to empirically explain excess kurtosis found in log-returns data, rejecting a Black-Scholes assumption in a hypothesis test.

Keywords. Laplace distribution; Gaussian variance-mixture; time-subordinated models; stochastic time-change; variance-gamma process; Esscher transform.

## 1 Introduction

Under many simple market models, one assumes the returns from an asset follow a log-Normal distribution - the celebrated Black-Scholes option pricing mechanism [[2](https://arxiv.org/html/2510.14093v1#bib.bib2)] is borne out of this assumption for example.111”Ideal condition” b) of the Black-Scholes formulation: ‘The stock price follows a random walk in continuous time with a variance proportional to the square of the stock price. Thus the distribution of possible stock prices at the end of any finite interval is log-Normal. The variance rate of the return on the stock is constant.’ The literature for Normal (Gaussian) distributions is extensive which has enabled well-grounded research into analytical solutions and closed-form formulas to different problems when an underlying Gaussian assumption is appropriate (often when large sample settings are being considered and the Central Limit Theorem applies).

However, there are many instances where one cannot reasonably assume that underlying distribution is Gaussian and indeed, in the case of daily log returns data the assumption appears inappropriate.

![Refer to caption](Figures/R_plots/Normal_daily_returns.png)


(a)

![Refer to caption](Figures/R_plots/Laplace_daily_returns.png)


(b)

Figure 1: Fitted Gaussian vs fitted Laplace for daily log returns from the S&\&P500 January 2022 to January 2024

The distribution of log returns from the S&\&P500 index from January 2022 to January 2024 appears to exhibit greater kurtosis than that admitted by a Gaussian. There is a visible difference - the log returns data has heavier tails and a sharper peak at 0 compared to the fitted Gaussian. Many authors have proposed alternate distributions (such as the Student-t [[3](https://arxiv.org/html/2510.14093v1#bib.bib3)], or Cauchy [[4](https://arxiv.org/html/2510.14093v1#bib.bib4)]) to the Gaussian to account for these observations.

Here, we first propose the Laplace distribution as an alternative, related to the Gaussian through the generalised Gaussian family (GGD). This GGD family includes an additional shape parameter β\beta so that X∼G​G​D​(μ,σ,β)X\sim GGD(\mu,\sigma,\beta) has density

|  |  |  |  |
| --- | --- | --- | --- |
|  | fX​(x)=β2​σ​Γ​(1/β)​e−(|x−μ|/σ)β.f\_{X}(x)={\frac{\beta}{2\sigma\Gamma(1/\beta)}}\;e^{-(|x-\mu|/\sigma)^{\beta}}. |  | (1) |

For β=2\beta=2 one recovers the Gaussian family, but β=1\beta=1 gives rise to the Laplace family - a family symmetric about μ\mu, exhibiting sharper peaks and heavier tails which better matches the log returns data. This initially suggests a possible need for alternative estimators of distribution parameters. With a Gaussian assumption, the distribution variance is estimated with the sample variance, the maximum-likelihood estimator with its square root measuring the realized volatility. We will see that sample mean absolute deviation from the sample median provides a more precise volatility estimator when the return distribution satisfies a Laplace assumption.

However, the Laplace distribution may also be expressed as a Gaussian with stochastic variance, and it is this characterisation as a Gaussian variance-mixture which we seek to explore and draw further inference from. Modelling the evolution of the stock price as a geometric Lévy process motivates a generalisation from the Laplace family to the Variance-Gamma family. We explore the Variance Gamma process as a time-subordinated Brownian motion composed as a Brownian motion with Gamma-distributed time increments, as considered in Madan and Milne [[5](https://arxiv.org/html/2510.14093v1#bib.bib5)].

It is common to use market-day counts to index price observations - this assumes unit time increments over all successive price observations. Alternatively, the time-subordination characterisation gives weight to the possibility that we can improve on the use of market-day counts, instead implementing a stochastic index. Many authors have proposed possible alternative deterministic indices to market-day counts, such as trading volume or volume of profits; however, it is the works of Madan and Milne (1991) [[5](https://arxiv.org/html/2510.14093v1#bib.bib5)] and Madan, Carr and Chang (1998) [[6](https://arxiv.org/html/2510.14093v1#bib.bib6)] which have highlighted the applications of a stochastic alternative of this form.

Under such a model, one infers that the economically relevant time in a market is itself a stochastic process, independent of other random processes affecting market dynamics222In their paper of 1990, Madan and Seneta comment on this idea, stating: More informally, one may think of G​(t)G(t) [the stochastic index] as a formal statement of the remark, ”Didn’t have much of a year this year,” by allowing for an interpretation of how much of a year one actually had.. We study the mathematical model of log returns when the time increments follow a Gamma process and the log price increments are attributed to Brownian motion on the stochastic time scale.

Geometric Brownian motion can be viewed as a sub-model of the Variance Gamma model (where there is no time-subordination) which allows us to observe the benefits of implementing a time-subordination. The Variance Gamma’s additional parameters can account for the excess kurtosis observed when modelling the log-return distribution of the S&\&P500 Index, improving on the Gaussian in this instance. However, we also consider the European option price under a general Variance Gamma model, and compare the pricing performance to that of the Black-Scholes benchmark. It is well-documented that the Black-Scholes formulation leads to known biases - notably the existence of an implied volatility smile upon estimating the volatility parameter. This is often attributed to the observation that log-returns have a risk neutral density with kurtosis above that of a Gaussian; this discrepancy leads to the presence of volatility smiles in the pricing of options under Black-Scholes [[7](https://arxiv.org/html/2510.14093v1#bib.bib7)], [[8](https://arxiv.org/html/2510.14093v1#bib.bib8)]. With the ability to obtain excess kurtosis over the Gaussian, the Variance Gamma density can be expected to correct these biases and propose a causal explanation. Additionally, while the risk-neutral under Black-Scholes model loses the drift term, the Variance Gamma risk neutral density preserves the drift term - it appears the inclusion of this drift term provides significant improvement for option pricing models.

We refer to the work of Madan, Carr and Chang [[6](https://arxiv.org/html/2510.14093v1#bib.bib6)], who test the performance of both the statistical and risk-neutral V​GVG processes on S&\&P500 market data, rejecting their respective geometric Brownian motion and Black-Scholes null hypotheses in favour of the V​GVG in the data. The authors are able to demonstrate that the V​GVG model is capable of correcting moneyness biases in pricing errors.

The paper follows the given outline. In section [2](https://arxiv.org/html/2510.14093v1#S2 "2 The Laplace Distribution ‣ The Variance Gamma Process for Option Pricing") we explore the Laplace distribution as an alternative to the Gaussian for fitting daily log returns. We then generalise the Laplace and consider the Variance Gamma distribution in section [3](https://arxiv.org/html/2510.14093v1#S3 "3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing"), as well as the corresponding Variance Gamma process. In section 4 we explore the European option pricing mechanism under the Variance Gamma model, obtaining a risk-neutral measure from an Esscher transform method. Section 5 deals with observing the differences between the more general V​GVG model and the nested Black-Scholes model. Section 6 concludes the results and the Appendix details the proofs deferred from the main sections.

## 2 The Laplace Distribution

### 2.1 Initial characterisation

We first explore the properties of the Laplace distribution as an alternative to the Gaussian.

###### Definition 1.

A random variable XX is said to have a Classical Laplace distribution C​L​(θ,s)CL(\theta,s) with mean θ∈ℝ\theta\in\mathbb{R} and scale s>0s>0 if it has real support with density

|  |  |  |  |
| --- | --- | --- | --- |
|  | fX​(x;θ,s)=12​s​e−|x−θ|s,x∈ℝ.f\_{X}(x;\theta,s)=\frac{1}{2s}e^{-\frac{|x-\theta|}{s}},\hskip 14.22636ptx\in\mathbb{R}. |  | (2) |

We refer to a standard Classical Laplace random variable for θ=0,s=1\theta=0,s=1.

The graph of this density can be interpreted as a graph of two exponential densities, one for positive deviations and one for negative deviations from the mean θ\theta, both with rate 1/s1/s (normalized to integrate to 11). One computes the characteristic function of a Laplace random variable XX from elementary integration (integrating on semi-infinite intervals about θ\theta).

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψX​(t)=ei​t​θ1+s2​t2,t∈ℝ.\psi\_{X}(t)=\frac{e^{it\theta}}{1+s^{2}t^{2}},\hskip 14.22636ptt\in\mathbb{R}. |  | (3) |

We can similarly find the moment generating function and it will be useful to write down the Taylor expansion for θ=0\theta=0 to obtain the central moments of the distribution.

|  |  |  |  |
| --- | --- | --- | --- |
|  | MX​(t)=11−s2​t2=∑k=0∞s2​k​(2​k)!​t2​k(2​k)!,−1s<t<1s⟹𝔼​((X−θ)n)={0n oddsn​n!n even.M\_{X}(t)=\dfrac{1}{1-s^{2}t^{2}}=\sum\_{k=0}^{\infty}s^{2k}(2k)!\frac{t^{2k}}{(2k)!},\hskip 7.11317pt-\frac{1}{s}<t<\frac{1}{s}\implies\mathbb{E}\left((X-\theta)^{n}\right)=\begin{cases}0&\text{$n$ odd}\\ s^{n}n!&\text{$n$ even.}\end{cases} |  | (4) |

One could alternatively note that the distribution is symmetric so the
odd central moments are 0, and the absolute value of an C​L​(0,s)CL(0,s) variable is an Exp​(1/s)\text{Exp}(1/s) variable so that the even central moments coincide. So we also find

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|X−θ|n]=sn​n!.\mathbb{E}\left[|X-\theta|^{n}\right]=s^{n}n!. |  | (5) |

We may now immediately compute the kurtosis,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kurt​(X):=𝔼​[(X−θ)4](𝔼​[(X−θ)2])2=24​s44​s4=6.\text{Kurt}(X):=\dfrac{\mathbb{E}\left[\left(X-\theta\right)^{4}\right]}{\left(\mathbb{E}\left[\left(X-\theta\right)^{2}\right]\right)^{2}}=\frac{24s^{4}}{4s^{4}}=6. |  | (6) |

###### Remark 1.

The excess kurtosis of a distribution is defined as the additional kurtosis over that of a Gaussian (=3=3) so in this case the excess kurtosis is 33. For a probability distribution, an excess kurtosis is attributed to greater weight in the tails of the distribution.

### 2.2 Parameter estimation

We first construct the likelihood function based on a random sample X1,…,Xn∼i.i.dC​L​(θ,s)X\_{1},\dots,X\_{n}\mathrel{\overset{i.i.d}{\scalebox{1.5}[1.0]{$\sim$}}}CL(\theta,s),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ=f​(X1,…,Xn;θ,s)=∏i=1nf​(Xi,θ,s)=(12​s)n​exp⁡(−1s​∑i=1n|Xi−θ|)\mathcal{L}=f(X\_{1},\dots,X\_{n};\theta,s)=\prod\_{i=1}^{n}f(X\_{i},\theta,s)=\left(\frac{1}{2s}\right)^{n}\exp\left(-\frac{1}{s}\sum\_{i=1}^{n}|X\_{i}-\theta|\right) |  | (7) |

and obtain the log-likelihood,

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡ℒ=l​(X1,…,Xn;θ,s)=−n​log⁡(2)−n​log⁡(s)−1s​∑i=1n|Xi−θ|.\log\mathcal{L}=l(X\_{1},\dots,X\_{n};\theta,s)=-n\log(2)-n\log(s)-\frac{1}{s}\sum\_{i=1}^{n}|X\_{i}-\theta|. |  | (8) |

It is evident that we can minimise the sum for any fixed ss to find θ^\hat{\theta} and then maximise the expression with respect to ss with θ\theta fixed at θ^\hat{\theta}. We begin with minimising the sum to find θ^\hat{\theta}.

###### Lemma 1.

For a sample X1,…,XnX\_{1},\dots,X\_{n}, the sum s​(θ)=∑i=1n|Xi−θ|s(\theta)=\sum\_{i=1}^{n}|X\_{i}-\theta| is minimised by the sample median.

The proof follows upon ordering the realisations xix\_{i} left to right as xkix\_{k\_{i}} and considering the value of the sum when θ\theta lies in different intervals [xki,xki+1][x\_{k\_{i}},x\_{k\_{i+1}}]. For an odd sample size, the minimising θ\theta is unique, while for an even sample size this θ\theta can lie within the closed interval between the middle two values (typically taking the midpoint of these).

We conclude that θ^\hat{\theta} is given by the sample median. The variance of this estimator cannot be computed easily, but is given explicitly in Asrabadi [[9](https://arxiv.org/html/2510.14093v1#bib.bib9)] (eq. 8) where the midpoint median is used for even sample sizes. With the explicit variances, we can generate a plot in Figure ([2](https://arxiv.org/html/2510.14093v1#S2.F2 "Figure 2 ‣ 2.2 Parameter estimation ‣ 2 The Laplace Distribution ‣ The Variance Gamma Process for Option Pricing")) of the variances proportional to s2/ns^{2}/n. The difference in calculation between odd and even sample sizes causes even sample sizes to be estimated more precisely than closeby odd sample sizes.

![Refer to caption](Figures/R_plots/Median_Variance.png)


Figure 2: Variance of Laplace sample median proportional to s2/ns^{2}/n

It is shown in Prop 2.6.2 of Kotz et al. [[10](https://arxiv.org/html/2510.14093v1#bib.bib10)] that the estimator θ^\hat{\theta} is unbiased, consistent and asymptotically Gaussian with n​(θ^−θ)​→𝑑​N​(0,s2)\sqrt{n}(\hat{\theta}-\theta)\overset{d}{\to}N\left(0,s^{2}\right).

Having found θ^\hat{\theta}, we can now maximise the log-likelihood with respect to ss.

###### Lemma 2.

Assuming θ\theta is known, s^\hat{s} is given by the sample mean absolute deviation from θ\theta .

|  |  |  |  |
| --- | --- | --- | --- |
|  | s^=1n​∑i=1n|Xi−θ|.\hat{s}=\frac{1}{n}\sum\_{i=1}^{n}|X\_{i}-\theta|. |  | (9) |

Further, the variance of this estimator is equal to s2n\frac{s^{2}}{n}, the Cramér-Rao lower bound for the variance.

The proof follows from the standard method, partially differentiating the log-likelihood w.r.t ss to obtain s^\hat{s} and then differentiating again to verify the Cramér-Rao lower bound. We leave the full calculation to the Appendix [8.1](https://arxiv.org/html/2510.14093v1#S8.SS1 "8.1 Proof of Lemma 2 ‣ 8 Appendix ‣ The Variance Gamma Process for Option Pricing") but summarise the findings below.

###### Proposition 1.

The maximum likelihood estimator of a random sample from a Classical Laplace C​L​(θ,s)CL(\theta,s) variable has an MLE pair given by θ^\hat{\theta}, the sample median and s^=1n​∑i=1n|xi−θ^|\hat{s}=\frac{1}{n}\sum\_{i=1}^{n}|x\_{i}-\hat{\theta}|.

It can be shown (as in Thm 2.6.1 of Kotz et al. [[10](https://arxiv.org/html/2510.14093v1#bib.bib10)] I) that the pair of estimators (θ^,s^)(\hat{\theta},\hat{s}) for (θ,s)(\theta,s) is consistent, asymptotically Gaussian and efficient (achieving their respective Cramér-Rao lower bounds) with an asymptotic covariance matrix,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝚺=(s200s2).\boldsymbol{\Sigma}=\begin{pmatrix}s^{2}&0\\ 0&s^{2}\end{pmatrix}. |  | (10) |

If we model log-returns with a Laplace distribution, we should ideally choose this pair of estimators. However, one typically uses a moment estimation method (estimating the sample mean and variance) from the data - these are motivated by their optimality when the log-return distribution is assumed to be Gaussian.

Suppose we instead assume a Laplace distribution but choose to estimate the parameters through moment estimation. We expect a lack of efficiency and this is indeed case. First, consider estimating θ\theta by the sample mean.

###### Lemma 3.

Given a sample X1,…,XnX\_{1},\dots,X\_{n}, the estimator for θ\theta given by the sample mean θ~=1n​∑i=1nXi\tilde{\theta}=\frac{1}{n}\sum\_{i=1}^{n}X\_{i} is unbiased, consistent and asymptotically Gaussian with n​(θ~−θ)​→𝑑​N​(0,2​s2).\sqrt{n}(\tilde{\theta}-\theta)\overset{d}{\to}N\left(0,2s^{2}\right).

###### Proof.

The estimator being unbiased follows immediately from the linearity of expectation. Consistency and asymptotic normality are given by the strong law of large numbers and central limit theorem respectively (noting from ([4](https://arxiv.org/html/2510.14093v1#S2.E4 "In 2.1 Initial characterisation ‣ 2 The Laplace Distribution ‣ The Variance Gamma Process for Option Pricing")) that the variance of each XiX\_{i} is indeed 2​s22s^{2}).
∎

We immediately note the relative asymptotic efficiency - the asymptotic variance of the sample mean is twice that of the asymptotic variance of the sample median under the Laplace assumption. Further the variance of the sample mean for finite samples is 2​s2/n2s^{2}/n, and while there is no simple closed form for θ^\hat{\theta}, the plot above in Figure ([2](https://arxiv.org/html/2510.14093v1#S2.F2 "Figure 2 ‣ 2.2 Parameter estimation ‣ 2 The Laplace Distribution ‣ The Variance Gamma Process for Option Pricing")) does confirm that the variance of θ^\hat{\theta} is always less than θ~\tilde{\theta} for sufficiently large samples.

We now consider the scaled sample standard deviation estimate for ss.

###### Lemma 4.

The estimator for ss given by,

|  |  |  |  |
| --- | --- | --- | --- |
|  | s~=12​n​∑i=1nXi\tilde{s}=\sqrt{\frac{1}{2n}\sum\_{i=1}^{n}X\_{i}} |  | (11) |

is consistent and asymptotically Gaussian with n​(s~−s)​→𝑑​N​(0,54​s2)\sqrt{n}(\tilde{s}-s)\overset{d}{\to}N\left(0,\frac{5}{4}s^{2}\right).

Consistency follows from the strong law of large numbers while the asymptotic normality follows upon recalling the Laplace central moments from ([4](https://arxiv.org/html/2510.14093v1#S2.E4 "In 2.1 Initial characterisation ‣ 2 The Laplace Distribution ‣ The Variance Gamma Process for Option Pricing")) and applying the delta method - the full calculation can be found in the Appendix [8.2](https://arxiv.org/html/2510.14093v1#S8.SS2 "8.2 Proof of Lemma 4 ‣ 8 Appendix ‣ The Variance Gamma Process for Option Pricing").

###### Remark 2.

It is important to note that, unlike for the Gaussian, ss does not represent the standard deviation of the Laplace distribution (rather the standard deviation of the Laplace is 2​s\sqrt{2}s). For the Laplace, ss represents a scale parameter - we consider estimating ss instead of the standard deviation directly to simplify calculations.

Again note the asymptotic relative efficiency - s~\tilde{s} has 5/45/4 times greater asymptotic variance than s^\hat{s} under the Laplace assumption. For the variance of finite samples, there is no simple closed form for s~\tilde{s} (as the square root presents complexity in calculations), but the Monte Carlo estimates in Figure ([3](https://arxiv.org/html/2510.14093v1#S2.F3 "Figure 3 ‣ 2.2 Parameter estimation ‣ 2 The Laplace Distribution ‣ The Variance Gamma Process for Option Pricing")) do confirm that the variance of s^\hat{s} is less than s~\tilde{s} for suitably large sample sizes 333For smaller sample sizes, the median is more susceptible to leverage from outliers in comparison to the mean, contrasting to the reverse effect for larger sample sizes.

![Refer to caption](Figures/R_plots/Simulated_sample_variance_Laplace.png)


Figure 3: Monte Carlo estimates of the relative efficiency between estimators for the scale parameter ss

###### Remark 3.

If we model the log-return distribution as Laplace instead of Gaussian, we should ideally consider different parameter estimators for our centre and spread of the underlying distribution. Importantly, if we estimate the log-return volatility and assume Laplace, the sample median absolute deviation presents a more efficient estimator for ss (which governs the volatility) than the scaled sample standard deviation and represents a more precise statistic for inference and decision analysis (e.g. option pricing) depending on the true parameter (e.g. volatility) of the return distribution.

### 2.3 Laplace distribution as a Gaussian variance-mixture

We have until now presented the Laplace distribution as an alternative to the Gaussian; however, the distributions are related beyond the generalised Gaussian family. We now explore the Gaussian variance-mixture characterisation from 2.2.1 of Kotz et al. [[10](https://arxiv.org/html/2510.14093v1#bib.bib10)].

Suppose that for some known and fixed θ\theta and σ2\sigma^{2}, XX is Gaussian with some mean θ\theta but with an independent random variance σ2​V\sigma^{2}V where VV is a non-negative random variable. This is known as a Gaussian variance-mixture and may be represented

|  |  |  |  |
| --- | --- | --- | --- |
|  | X=θ+σ​V​ZX=\theta+\sigma\sqrt{V}Z |  | (12) |

where Z∼N​(0,1)Z\sim N(0,1), and VV is a random variable independent of ZZ. Intuitively one understands this by conditioning on VV, re-scaling the standard Gaussian to determine the variance, and ultimately shifting the mean. Suppose we now centralise XX with θ=0\theta=0, specify VV to be a standard exponential random variable with rate 11, and let σ=2\sigma=\sqrt{2} so that X=2​V​ZX=\sqrt{2V}Z.
We will see that leads to a standard Laplace distribution.

###### Proposition 2.

Let ZZ have a standard Gaussian and VV be an independent a standard exponential random variable. Then the random variable X=2​V​ZX=\sqrt{2V}Z has a standard Laplace distribution.

###### Remark 4.

Before providing the proof, we reflect on the Gaussian variance-mixture characterisation of XX. When encountering such a mixture, we can first condition on the random variance to reduce the setup to Normality - something we understand well - then deal with the random variance separately. We will return to this idea throughout.

###### Proof.

Here, we appeal to the identity theorem for the characteristic functions of probability distributions. For VV a standard exponential with density fV​(v)=e−vf\_{V}(v)=e^{-v}, we have MV​(t)=(1−t)−1M\_{V}(t)=({1-t})^{-1}. For ZZ a standard Gaussian variable, we have ψZ​(t)=e−t2/2\psi\_{Z}(t)=e^{-t^{2}/2}. With these in hand, we calculate the characteristic function of XX by conditioning on the value of the (non-negative) variance VV,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ei​t​X]\displaystyle\mathbb{E}\left[e^{itX}\right] | =𝔼​[ei​t​2​V​Z]=𝔼V​[𝔼Z​[ei​t​2​V​Z|V]]=𝔼V​[ψX​(t​2​V)]\displaystyle=\mathbb{E}\left[e^{it\sqrt{2V}Z}\right]=\mathbb{E}\_{V}\left[\mathbb{E}\_{Z}\left[e^{it\sqrt{2V}Z}\Big|V\right]\right]=\mathbb{E}\_{V}\left[\psi\_{X}\left(t\sqrt{2V}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼V​[e−t2​V]=MV​(−t2)=11+t2,\displaystyle=\mathbb{E}\_{V}\left[e^{-t^{2}V}\right]=M\_{V}\left(-t^{2}\right)=\frac{1}{1+t^{2}}, |  |

which indeed coincides with the characteristic function of the standard Laplace random variable.
∎

If we generalise to X=θ+σ​V​ZX=\theta+\sigma\sqrt{V}Z, for fixed θ\theta and σ\sigma, ZZ a standard Gaussian r.v but V∼exp⁡(λ)V\sim\exp(\lambda) one employs a similar method to show that X∼C​L​(θ,σ/2​λ)X\sim CL(\theta,\sigma/\sqrt{2\lambda}). We aim to generalise this Gaussian variance-mixture further in section [3](https://arxiv.org/html/2510.14093v1#S3 "3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing").

###### Remark 5.

This is a particularly useful characterisation of the Laplace distribution, as we will see in later sections. However, there are alternate characterisations of the Laplace distribution which provide a different interpretation if one models a log-return distribution with a Laplace distribution.

For example, the distribution can also be represented as a difference of two i.i.d. Exponential distributions (this can be seen by splitting the characteristic function (1+t2)−1=(1+i​t)​(1−i​t)(1+t^{2})^{-1}=(1+it)(1-it) for the standard Laplace, and similar for general Laplace). One can find further implications of considering the general Classical Laplace and later the variance gamma model as this difference in Fischer et al. [[11](https://arxiv.org/html/2510.14093v1#bib.bib11)].

One can also characterise the Laplace as a maximum entropy distribution. The maximum entropy principle states that considering all distributions satisfying certain constraints, one should select the one with the largest entropy as characterising this distribution maximises randomness subject to the constraint - this idea is explored in detail by Rényi [[12](https://arxiv.org/html/2510.14093v1#bib.bib12)]. As a result, finding a maximum entropy distribution presents a suitable procedure for robust inference, detailed in Jaynes [[13](https://arxiv.org/html/2510.14093v1#bib.bib13)]. If one specifies the first absolute central moment, the maximum entropy family with real support is the corresponding Laplace family, shown in the Appendix [8.3](https://arxiv.org/html/2510.14093v1#S8.SS3 "8.3 Maximum Entropy distributions ‣ 8 Appendix ‣ The Variance Gamma Process for Option Pricing")).

For our study, we seek to explore inference from the random variance representation which allows us to consider a stochastic time change for a time-subordinated Brownian motion, and the corresponding interpretation for the model.

## 3 The Variance Gamma Process

### 3.1 The symmetric Variance Gamma distribution

If one assumes the log-return distribution for an asset is Gaussian, geometric Brownian motion arises as the associated Lévy process to describe the evolution of the stock price. The fact that the sum of independent Gaussians is still Gaussian greatly helps in the characterisation of Brownian motion as a Lévy process with Gaussian distributed increments. If we consider an equivalent under a Laplace assumption, we need to understand sums of Laplace distributions and in doing this we will see that weakening the Laplace assumption to be slightly more general aids the description of the associated Lévy process.

Suppose that Xi=Vi​ZiX\_{i}=\sqrt{V\_{i}}Z\_{i} for i=1,…,ni=1,\dots,n where Vi∼i.i.dexp⁡(λ)V\_{i}\mathrel{\overset{i.i.d}{\scalebox{1.5}[1.0]{$\sim$}}}\exp(\lambda) and Zi∼i.i.dN​(0,1)Z\_{i}\mathrel{\overset{i.i.d}{\scalebox{1.5}[1.0]{$\sim$}}}N(0,1) are independent of the ViV\_{i}’s. From the generalisation of Prop. ([2](https://arxiv.org/html/2510.14093v1#Thmprop2 "Proposition 2. ‣ 2.3 Laplace distribution as a Gaussian variance-mixture ‣ 2 The Laplace Distribution ‣ The Variance Gamma Process for Option Pricing")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψXi​(t)=(1+t22​λ)−1,\psi\_{X\_{i}}(t)=\left({1+\frac{t^{2}}{2\lambda}}\right)^{-1}, |  | (13) |

so that for Sn:=∑i=1nXiS\_{n}:=\sum\_{i=1}^{n}X\_{i},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψSn​(t)=(1+t22​λ)−n.\psi\_{S\_{n}}(t)=\left({1+\frac{t^{2}}{2\lambda}}\right)^{-n}. |  | (14) |

###### Remark 6.

We recognise a strong resemblance with the characteristic function of a Gamma distribution (given below) - one with shape nn and rate λ\lambda, only here the argument tt has been replaced with −t2/2-t^{2}/2. We saw this arise in a similar manner with the Exponential characteristic function in the proof of Prop. ([2](https://arxiv.org/html/2510.14093v1#Thmprop2 "Proposition 2. ‣ 2.3 Laplace distribution as a Gaussian variance-mixture ‣ 2 The Laplace Distribution ‣ The Variance Gamma Process for Option Pricing")) and this hints at a nice form for the more general Gaussian variance-mixture.

Intuitively one might expect a connection with the Gamma distribution - as the variance of a sum of independent Gaussians is the sum of their variances (which are Exponentially distributed here), and a sum of independent Exponential distributions is a Gamma distribution. We formalise this notion below.

###### Definition 2.

Let XX be a Gamma distributed random variable with shape α>0\alpha>0, rate β>0\beta>0, denoted X∼Gamma​(α,β)X\sim\text{Gamma}(\alpha,\beta). Then the density gX​(x)g\_{X}(x) for XX is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | gX​(x)=βαΓ​(α)​xα−1​e−β​x,x>0.g\_{X}(x)=\dfrac{\beta^{\alpha}}{\Gamma(\alpha)}x^{\alpha-1}e^{-\beta x},\hskip 14.22636ptx>0. |  | (15) |

The characteristic and moment-generating functions are obtained from integration (employing the integral definition of the Gamma function).

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψX​(t)=(1−i​tβ)−α,MX​(t)=(1−tβ)−α.\psi\_{X}(t)=\left(1-{\frac{it}{\beta}}\right)^{-\alpha},\hskip 5.69046ptM\_{X}(t)=\left(1-{\frac{t}{\beta}}\right)^{-\alpha}. |  | (16) |

We are now in place to define the Symmetric Variance Gamma distribution as a Gaussian variance-mixture.

###### Definition 3.

Let X=θ+σ​V​ZX=\theta+\sigma\sqrt{V}Z where θ∈ℝ,σ>0\theta\in\mathbb{R},\sigma>0 are fixed, ZZ has a standard Gaussian, and VV is an independent Gamma​(α,β)\text{Gamma}(\alpha,\beta) distribution. Then X∼S​V​G​(θ,σ,α,β)X\sim SVG(\theta,\sigma,\alpha,\beta) is said to have a Symmetric Variance Gamma distribution.

###### Remark 7.

Under this definition XX is a symmetric distribution about θ\theta, and so 𝔼​[X]=θ\mathbb{E}[X]=\theta. Importantly, one observes (e.g. from the characteristic function below) that σ\sigma and β\beta are not-identifiable. However, this actually provides flexibility in interpreting properties of the distribution across different settings.

If we restrict VV to have expectation μ=α/β=1\mu=\alpha/\beta=1, then σ\sigma becomes a volatility parameter. This can be seen by using the independence of VV and ZZ,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var ​[X]=𝔼​[(σ​V​Z)2]=σ2​𝔼​[V​Z2]=σ2​𝔼​[V]​𝔼​[Z2]=σ2.\text{Var }[X]=\mathbb{E}\left[\left(\sigma\sqrt{V}Z\right)^{2}\right]=\sigma^{2}\mathbb{E}\left[{V}Z^{2}\right]=\sigma^{2}\mathbb{E}[V]\mathbb{E}\left[Z^{2}\right]=\sigma^{2}. |  | (17) |

This is a particularly useful notion which we will employ in section [3.3](https://arxiv.org/html/2510.14093v1#S3.SS3 "3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing") to define the Variance Gamma process.

Alternatively, we could fix σ=1\sigma=1 and directly observe changes to VV across different settings e.g. over different time periods in the Variance Gamma process. This is another valuable notion one can use for modelling stochastic volatility.

For α=1\alpha=1, we recover a Laplace distribution as the Gamma-distributed variance is simply Exponential. However, in general there is no closed form for the density of the S​V​GSVG distribution, and so we write through a Radon-Nikodym derivative (effectively conditioning on the Gamma-distributed variance). For a standard Gaussian density ϕ​(x)\phi(x) and Gamma​(α,β)\text{Gamma}(\alpha,\beta) density g​(x)g(x), one writes

|  |  |  |  |
| --- | --- | --- | --- |
|  | fX​(x)=∫0∞ϕ​(x−θσ​v)​g​(v)​𝑑v=∫0∞12​π​σ2​v​e−(x−θ)2/(2​σ2​v)​βαΓ​(α)​vα−1​e−β​v​𝑑v.f\_{X}(x)=\int\_{0}^{\infty}\phi\left(\dfrac{x-\theta}{\sigma\sqrt{v}}\right)g(v)dv=\int\_{0}^{\infty}\frac{1}{\sqrt{2\pi\sigma^{2}v}}e^{-(x-\theta)^{2}/{(2\sigma^{2}v)}}\dfrac{\beta^{\alpha}}{\Gamma(\alpha)}v^{\alpha-1}e^{-\beta v}dv. |  | (18) |

As before, it will be useful to find the characteristic function of XX for future analysis. It has a generalised form of the Laplace characteristic function, as hinted in Remark ([6](https://arxiv.org/html/2510.14093v1#Thmremark6 "Remark 6. ‣ 3.1 The symmetric Variance Gamma distribution ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")).

###### Proposition 3.

Let ZZ be a standard Gaussian and VV be an independent Gamma​(α,β)\text{Gamma}(\alpha,\beta) variable. In addition, let σ>0\sigma>0 be known and fixed. Then the characteristic function of the Symmetric V​GVG variable X=σ​V​ZX=\sigma\sqrt{V}Z is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψX​(t)=(1+t2​σ22​β)−α.\psi\_{X}(t)=\left(1+\dfrac{t^{2}\sigma^{2}}{2\beta}\right)^{-\alpha}. |  | (19) |

###### Proof.

As before, we will show this by conditioning on the value of the variance VV. We first note that for V∼Γ​(α,β)V\sim\Gamma(\alpha,\beta) we have MV​(t)=(1−t/β)−αM\_{V}(t)=({1-{t}/{\beta}})^{-\alpha} and again for ZZ, a standard Gaussian variable we have ψZ​(t)=e−t2/2\psi\_{Z}(t)=e^{-t^{2}/2}. Then proceeding as before,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ei​t​X]\displaystyle\mathbb{E}\left[e^{itX}\right] | =𝔼​[ei​t​σ​V​Z]=𝔼V​[𝔼Z​[ei​t​σ​V​Z|V]]=𝔼V​[ψZ​(t​σ​V)]=𝔼V​[e−t2​σ2​V/2]\displaystyle=\mathbb{E}\left[e^{it\sigma\sqrt{V}Z}\right]=\mathbb{E}\_{V}\left[\mathbb{E}\_{Z}\left[e^{it\sigma\sqrt{V}Z}\hskip 2.84544pt\Big|V\right]\right]=\mathbb{E}\_{V}\left[\psi\_{Z}\left(t\sigma\sqrt{V}\right)\right]=\mathbb{E}\_{V}\left[e^{-t^{2}\sigma^{2}V/2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =MV​(−t2​σ2/2)=(1+t2​σ22​β)−α.\displaystyle=M\_{V}\left(-t^{2}\sigma^{2}/2\right)=\left(1+\dfrac{t^{2}\sigma^{2}}{2\beta}\right)^{-\alpha}. |  |

∎

### 3.2 The Variance Gamma distribution

Having motivated and explored a generalisation from the symmetric Laplace distribution to the symmetric Variance Gamma, we now consider the full Variance Gamma distribution which can be represented as a Gaussian with both stochastic variance and stochastic mean. This generalisation enables the inclusion of a drift term in the associated Lévy process, accounting for possible asymmetry in the statistical and risk-neutral log return distributions.

###### Definition 4.

Let X=c+θ​V+σ​V​ZX=c+\theta V+\sigma\sqrt{V}Z where c,θ∈ℝ,σ>0c,\theta\in\mathbb{R},\sigma>0 are fixed, ZZ has a standard Gaussian, and VV is an independent Gamma​(α,β)\text{Gamma}(\alpha,\beta) distribution. Then X∼V​G​(c,θ,σ,α,β)X\sim VG(c,\theta,\sigma,\alpha,\beta) is said to have a Variance Gamma distribution.

###### Remark 8.

Under this new definition if θ≠0\theta\neq 0, XX is no longer a symmetric distribution due to the θ​V\theta V term. For θ≠0\theta\neq 0, σ\sigma no longer represents the volatility as Var​[X]=θ2​Var​[V]+σ2​𝔼​[V]\text{Var}[X]=\theta^{2}\text{Var}[V]+\sigma^{2}\mathbb{E}[V]. However, as in Remark [7](https://arxiv.org/html/2510.14093v1#Thmremark7 "Remark 7. ‣ 3.1 The symmetric Variance Gamma distribution ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing"), if we let 𝔼​[V]=μ=1\mathbb{E}[V]=\mu=1 and denote Var​[V]=ν\text{Var}[V]=\nu then the volatility is given by θ2​ν+σ2\theta^{2}\nu+\sigma^{2}.

This motivates a reparametrisation which we will use to define the Gamma Process in section [3.3](https://arxiv.org/html/2510.14093v1#S3.SS3 "3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing"). We can alternatively define a Gamma-distributed random variable X∼Gamma​(α,β)X\sim\text{Gamma}(\alpha,\beta) in terms of its positive mean μ=α/β\mu=\alpha/\beta and variance ν=α/β2\nu=\alpha/\beta^{2} so that under a re-parametrisation, we write X∼Γμ,νX\sim\Gamma\_{\mu,\nu} with

|  |  |  |  |
| --- | --- | --- | --- |
|  | fX​(x)=(μν)μ2/νΓ​(μ2/ν)​xμ2/ν−1​e−μ/ν​x,ψX​(t)=(11−i​νμ​t)μ2/ν,MX​(t)=(11−νμ​t)μ2/ν.f\_{X}(x)=\dfrac{\left(\frac{\mu}{\nu}\right)^{\mu^{2}/\nu}}{\Gamma\left(\mu^{2}/\nu\right)}x^{\mu^{2}/\nu-1}e^{-\mu/\nu x},\hskip 14.22636pt\psi\_{X}(t)=\left(\dfrac{1}{1-\frac{i\nu}{\mu}t}\right)^{\mu^{2}/\nu},\hskip 14.22636ptM\_{X}(t)=\left(\dfrac{1}{1-\frac{\nu}{\mu}t}\right)^{\mu^{2}/\nu}. |  | (20) |

We may again write the density of a V​GVG variable in terms of a Radon-Nikodym density, similar to ([18](https://arxiv.org/html/2510.14093v1#S3.E18 "In 3.1 The symmetric Variance Gamma distribution ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")), using the original parametrisation in terms of Gamma​(α,β)\text{Gamma}(\alpha,\beta),

|  |  |  |  |
| --- | --- | --- | --- |
|  | fX​(x)=∫0∞ϕ​(x−c−θ​vσ​v)​g​(v)​𝑑v=∫0∞12​π​σ2​v​e−(x−c−θ​v)2/(2​σ2​v)​βαΓ​(α)​vα−1​e−β​v​𝑑v,f\_{X}(x)=\int\_{0}^{\infty}\phi\left(\dfrac{x-c-\theta v}{\sigma\sqrt{v}}\right)g(v)dv=\int\_{0}^{\infty}\frac{1}{\sqrt{2\pi\sigma^{2}v}}e^{-(x-c-\theta v)^{2}/{(2\sigma^{2}v)}}\dfrac{\beta^{\alpha}}{\Gamma(\alpha)}v^{\alpha-1}e^{-\beta v}dv, |  | (21) |

and compute the characteristic function in a similar manner to Prop. ([3](https://arxiv.org/html/2510.14093v1#Thmprop3 "Proposition 3. ‣ 3.1 The symmetric Variance Gamma distribution ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")).

###### Proposition 4.

Let ZZ be a standard Gaussian and VV be an independent Gamma​(α,β)\text{Gamma}(\alpha,\beta) variable. Further, let θ∈ℝ,σ>0\theta\in\mathbb{R},\sigma>0 be known and fixed. Then the characteristic function of the V​GVG variable X=θ​V+σ​V​ZX=\theta V+\sigma\sqrt{V}Z is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψX​(t)=(1−i​θ​tβ+t2​σ22​β)−α.\psi\_{X}(t)=\left(1-\frac{i\theta t}{\beta}+\dfrac{t^{2}\sigma^{2}}{2\beta}\right)^{-\alpha}. |  | (22) |

###### Proof.

Proceeding as in the proof of Prop. ([3](https://arxiv.org/html/2510.14093v1#Thmprop3 "Proposition 3. ‣ 3.1 The symmetric Variance Gamma distribution ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")) by conditioning on the value of VV, we find

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[ei​t​X]\displaystyle\mathbb{E}\left[e^{itX}\right] | =𝔼​[ei​t​(θ​V+σ​V​Z)]=𝔼V​[𝔼Z​[ei​t​(θ​V+σ​V​Z)|V]]=𝔼V​[ei​t​θ​V​ψZ​(t​σ​V)]\displaystyle=\mathbb{E}\left[e^{it(\theta V+\sigma\sqrt{V}Z)}\right]=\mathbb{E}\_{V}\left[\mathbb{E}\_{Z}\left[e^{it(\theta V+\sigma\sqrt{V}Z)}\hskip 2.84544pt\Big|V\right]\right]=\mathbb{E}\_{V}\left[e^{it\theta V}\psi\_{Z}\left(t\sigma\sqrt{V}\right)\right] |  | (23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼V​[ei​t​θ​V−t2​σ2​V/2]=𝔼V​[e(i​t​θ−t2​σ2/2)​V]\displaystyle=\mathbb{E}\_{V}\left[e^{it\theta V-t^{2}\sigma^{2}V/2}\right]=\mathbb{E}\_{V}\left[e^{(it\theta-t^{2}\sigma^{2}/2)V}\right] |  | (24) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫0∞e(i​t​θ−t2​σ2/2)​v​βαΓ​(α)​vα−1​e−β​v​𝑑v=∫0∞βαΓ​(α)​vα−1​e−(β−i​t​θ+t2​σ2/2)​v​𝑑v,\displaystyle=\int\_{0}^{\infty}e^{(it\theta-t^{2}\sigma^{2}/2)v}\dfrac{\beta^{\alpha}}{\Gamma(\alpha)}v^{\alpha-1}e^{-\beta v}dv=\int\_{0}^{\infty}\dfrac{\beta^{\alpha}}{\Gamma(\alpha)}v^{\alpha-1}e^{-(\beta-it\theta+t^{2}\sigma^{2}/2)v}dv, |  | (25) |

from which the result follows upon applying the definition of the Gamma function (noting β+t2​σ2/2>0\beta+t^{2}\sigma^{2}/2>0),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0∞βαΓ​(α)​vα−1​e−(β−i​t​θ+t2​σ2/2)​v​𝑑v=βαΓ​(α)​Γ​(α)(β−i​t​θ+t2​σ2/2)α=(1−i​θ​tβ+t2​σ22​β)−α\int\_{0}^{\infty}\dfrac{\beta^{\alpha}}{\Gamma(\alpha)}v^{\alpha-1}e^{-(\beta-it\theta+t^{2}\sigma^{2}/2)v}dv=\dfrac{\beta^{\alpha}}{\Gamma(\alpha)}\dfrac{\Gamma(\alpha)}{\left(\beta-it\theta+t^{2}\sigma^{2}/2\right)^{\alpha}}=\left(1-\frac{i\theta t}{\beta}+\dfrac{t^{2}\sigma^{2}}{2\beta}\right)^{-\alpha} |  | (26) |

as desired.
∎

### 3.3 The Variance Gamma process

We have characterised the V​GVG distribution and now turn to the associated V​GVG process. This will follow a similar analysis, considering the Lévy process as a composition mixture of a Gaussian process (a Brownian motion) and a Gamma process as described in 4.2 of Kotz et al. [[10](https://arxiv.org/html/2510.14093v1#bib.bib10)]. First, we clarify our definition of a Brownian motion.

###### Definition 5.

Let (Wt)t≥0(W\_{t})\_{t\geq 0} be a standard Wiener process where W0=0W\_{0}=0 a.s. , WtW\_{t} has stationary Gaussian increments so that Wt+h−Wt∼N​(0,h)W\_{t+h}-W\_{t}\sim N(0,h) where the distributions are independent over non-overlapping time intervals, and WtW\_{t} is continuous a.s.a.s. . Then the process (bt)t≥0(b\_{t})\_{t\geq 0} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | bt=b​(t;θ,σ)=θ​t+σ​Wtb\_{t}=b(t;\theta,\sigma)=\theta t+\sigma W\_{t} |  | (27) |

is a Brownian motion with drift θ∈ℝ\theta\in\mathbb{R} and volatility σ>0\sigma>0.

It is useful to recall the characteristic function for a Brownian motion,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψb​(t;θ,σ)​(u)=exp⁡(i​θ​t​u−12​σ2​t​u2).\psi\_{b(t;\theta,\sigma)}(u)=\exp\left(i\theta tu-\frac{1}{2}\sigma^{2}tu^{2}\right). |  | (28) |

Our V​GVG distribution was characterised as a Gaussian with a random Gamma distributed mean and variance. In a Brownian motion, the increments have a mean and variance proportional to the size of the time increment, so to create an analogue we seek a way of transforming the time increments randomly using a Gamma distribution and then evaluating the Brownian motion at the resulting transformed time - this is known as a time-subordinated Brownian motion where the Gamma process is the time-subordinator. We define this below (employing the re-parametrisation of remark [8](https://arxiv.org/html/2510.14093v1#Thmremark8 "Remark 8. ‣ 3.2 The Variance Gamma distribution ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")).

###### Definition 6.

Let (γt)t≥0=γ​(t;μ,ν)(\gamma\_{t})\_{t\geq 0}=\gamma(t;\mu,\nu) be a Gamma process for μ∈ℝ,ν≥0\mu\in\mathbb{R},\nu\geq 0.444The degenerate case ν=0\nu=0 is included and viewed as a deterministic limit process μ​t\mu t as ν→0.\nu\to 0. Then γ0=0\gamma\_{0}=0 a.s.a.s. , γt\gamma\_{t} has stationary Gamma distributed increments s.t. γt+h−γt∼Γμ​h,ν​h\gamma\_{t+h}-\gamma\_{t}\sim\Gamma\_{\mu h,\nu h} where the distributions are independent over non-overlapping time intervals, and γt\gamma\_{t} is continuous a.s. .

Again it will be useful to have the characteristic and moment generating functions,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψγ​(t;μ,ν)​(u)=(11−i​νμ​u)μ2​t/ν,Mγ​(t;μ,ν)​(u)=(11−νμ​u)μ2​t/ν\psi\_{\gamma(t;\mu,\nu)}(u)=\left(\dfrac{1}{1-\frac{i\nu}{\mu}u}\right)^{\mu^{2}t/\nu},\hskip 14.22636ptM\_{\gamma(t;\mu,\nu)}(u)=\left(\dfrac{1}{1-\frac{\nu}{\mu}u}\right)^{\mu^{2}t/\nu} |  | (29) |

Now let μ=1\mu=1 so that the mean rate of the Gamma process is 11. This is a helpful characterisation as it means that at time TT, the expectation of our random Gamma distributed time 𝔼​[γ​(T;1,ν)]=T\mathbb{E}\left[\gamma(T;1,\nu)\right]=T and we have random fluctuation only about the deterministic time.

###### Remark 9.

For our purposes, we may think of the Gamma process as a map (Tt)t≥0↦(γt)t≥0(T\_{t})\_{t\geq 0}\mapsto(\gamma\_{t})\_{t\geq 0} from the ‘deterministic time clock’ Tt=tT\_{t}=t onto a new ‘Gamma time clock’ γt\gamma\_{t}.

Figure [4](https://arxiv.org/html/2510.14093v1#S3.F4 "Figure 4 ‣ 3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing") provides examples for some of the possible properties of the Gamma subordinator process. We can think of the original clock being slowed in regions of low gradient and sped up up for high gradient. The markers correspond to unit time intervals on the new clock, and demonstrate instances of this time dilation - regions in which the markers are more spread out correspond to time being dilated and slowed, whereas regions with clusters of markers correspond to time being contracted and sped up.

The mean rate of the time change is null, in that on average 1 unit of deterministic time corresponds to 1 unit of Gamma-changed time (as shown by the y=xy=x line).

![Refer to caption](Figures/R_plots/Gamma_process.png)


Figure 4: Simulated Gamma process: γ(t;μ=1,ν=0.3)\gamma(t;\mu=1,\nu=0.3)

We can finally characterise our V​GVG process as Gamma subordinated Brownian motion.

###### Definition 7.

Let (bt)t≥0=b​(t;θ,σ)(b\_{t})\_{t\geq 0}=b(t;\theta,\sigma) be a Brownian motion as in definition ([5](https://arxiv.org/html/2510.14093v1#Thmdefinition5 "Definition 5. ‣ 3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")), and let (γt)t≥0=γ​(t;1,ν)(\gamma\_{t})\_{t\geq 0}=\gamma(t;1,\nu) be a Gamma process as in definition ([6](https://arxiv.org/html/2510.14093v1#Thmdefinition6 "Definition 6. ‣ 3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")). Then the time-subordinated process (Xt)t≥0(X\_{t})\_{t\geq 0} given by the composition

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Xt=X​(t;θ,σ,ν)\displaystyle X\_{t}=X(t;\theta,\sigma,\nu) | =b​(γ​(t;1,ν);θ,σ)\displaystyle=b\big(\gamma(t;1,\nu);\theta,\sigma\big) |  | (30) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =θ​γt+σ​Wγt,\displaystyle=\theta\gamma\_{t}+\sigma W\_{\gamma\_{t}}, |  | (31) |

is known as a Variance Gamma process denoted V​G​(t;θ,σ,ν)VG(t;\theta,\sigma,\nu).

###### Remark 10.

Breaking down this definition, there are two sources of randomness. First is the Wiener process which acts the same as in the Brownian motion, creating Gaussian noise about the drift θ​t\theta t. However, there is also the Gamma time-subordination, so that we think of the process as first randomly mapping deterministic time onto a Gamma-changed time as in remark [9](https://arxiv.org/html/2510.14093v1#Thmremark9 "Remark 9. ‣ 3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing") and then evaluating the Brownian motion at the Gamma time change 555We have chosen the time-changed Brownian motion as our characterisation of the V​GVG process. Similar to the comments in section 2.4.2, there are alternate characterisations of the V​GVG process e.g. as a difference of independent Gamma processes or as the limit of a compound poisson approximation. We do not cover these here, as we seek to explore inferences based on the random time-change characterisation. The alternate characterisations are detailed 4.2.3 of Kotz et al. [[10](https://arxiv.org/html/2510.14093v1#bib.bib10)].. For a more detailed review of time-subordinated processes, see section 1.3 of Applebaum [[14](https://arxiv.org/html/2510.14093v1#bib.bib14)].

A Brownian motion is simulated in Figure [5](https://arxiv.org/html/2510.14093v1#S3.F5 "Figure 5 ‣ 3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")(a) and mapped onto the VG process in Figure [5](https://arxiv.org/html/2510.14093v1#S3.F5 "Figure 5 ‣ 3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")(b) through the Gamma time-subordination of Figure [4](https://arxiv.org/html/2510.14093v1#S3.F4 "Figure 4 ‣ 3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing"). I.e. b​(t)↦b​(γ​(t))b(t)\mapsto b(\gamma(t)). Through the time-transformation, the markers in the Brownian motion are mapped onto the VG process in the Figure via (t,b(t))↦(γ(t),b(γ(t))(t,b(t))\mapsto(\gamma(t),b(\gamma(t)).

These demonstrate the effect of the time-subordination - while the general shape of the motion is mostly preserved, one observes the dilation and contraction of the Brownian motion along the time-axis caused by the time-subordination.

![Refer to caption](Figures/R_plots/Brownian_Motion.png)


(a)

![Refer to caption](Figures/R_plots/VG_process.png)


(b)

Figure 5: Realised components of a V​GVG process: VG(t;θ=0.1,σ=0.1,ν=0.3)VG(t;\theta=0.1,\sigma=0.1,\nu=0.3)

Using this idea we can obtain the density function of the process at time tt by conditioning on a realisation of the Gamma time-subordinator (giving a Brownian motion density), and integrating against the Gamma density. Similar to ([21](https://arxiv.org/html/2510.14093v1#S3.E21 "In 3.2 The Variance Gamma distribution ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | fXt​(x)=∫ϕ​(x−θ​gσ​g)​fγt​(g)​𝑑g=∫0∞12​π​σ2​g​exp⁡(−(x−θ​g)22​σ2​g)​gtν−1​exp⁡(−gν)νtν​Γ​(tν)​𝑑g.f\_{X\_{t}}(x)=\int\phi\left(\dfrac{x-\theta g}{\sigma\sqrt{g}}\right)f\_{\gamma\_{t}}(g)dg=\int\_{0}^{\infty}\dfrac{1}{\sqrt{2\pi\sigma^{2}g}}\exp\left(-\frac{(x-\theta g)^{2}}{2\sigma^{2}g}\right)\dfrac{g^{\frac{t}{\nu}-1}\exp\left(-\frac{g}{\nu}\right)}{\nu^{\frac{t}{\nu}}\Gamma\left(\frac{t}{\nu}\right)}dg. |  | (32) |

We may also obtain the characteristic function for the process. Again, we condition on realisation of the Gamma time-subordinator with a similar method to the proof of Prop. ([3](https://arxiv.org/html/2510.14093v1#Thmprop3 "Proposition 3. ‣ 3.1 The symmetric Variance Gamma distribution ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")), using the characteristic functions in ([28](https://arxiv.org/html/2510.14093v1#S3.E28 "In 3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")) and ([29](https://arxiv.org/html/2510.14093v1#S3.E29 "In 3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")). We then find

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψXt​(u)=(11−i​θ​ν​u+σ22​ν​u2)tν.\psi\_{X\_{t}}(u)=\left(\dfrac{1}{1-i\theta\nu u+\frac{\sigma^{2}}{2}\nu u^{2}}\right)^{\frac{t}{\nu}}. |  | (33) |

###### Remark 11.

Taking the limit as ν↓0\nu\downarrow 0 in the V​GVG process, we obtain weak convergence to a Brownian motion b​(t;θ,σ)b(t;\theta,\sigma) as in ([27](https://arxiv.org/html/2510.14093v1#S3.E27 "In Definition 5. ‣ 3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")) - this is shown in Appendix [8.4](https://arxiv.org/html/2510.14093v1#S8.SS4 "8.4 Brownian motion as a degenerate Variance Gamma process ‣ 8 Appendix ‣ The Variance Gamma Process for Option Pricing") using the characteristic function above. This should be expected, as the Gamma process subordinating the time becomes degenerate with 0 variance about the mean tt, and there is no time-change for the Brownian motion. This shows that the V​GVG model still contains Brownian motion as a sub-model - this is a particularly useful property if one employs a hypothesis test which nests a Brownian motion model null inside a more general V​GVG model alternative.

One could compute the central moments of the V​GVG process from the characteristic function ([33](https://arxiv.org/html/2510.14093v1#S3.E33 "In 3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")); however, employing the form ([31](https://arxiv.org/html/2510.14093v1#S3.E31 "In Definition 7. ‣ 3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")) simplifies calculations. Conditioning on the Gamma time-subordinator as γt=g\gamma\_{t}=g, so that the conditional V​GVG process is a Brownian motion and we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | X​(t;θ,σ|γt=g)=θ​g+σ​Wg.X\left(t;\theta,\sigma\big|\gamma\_{t}=g\right)=\theta g+\sigma W\_{g}. |  | (34) |

We can then take the expectation over the Wiener process, and then the expectation over g=γtg=\gamma\_{t} as in A4 of Madan et al. [[6](https://arxiv.org/html/2510.14093v1#bib.bib6)]).
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

If we consider the case θ=0\theta=0, then we have no skewness as the third central moment becomes 0. Furthermore, the kurtosis would then be given by 3​(1+ν/t)3(1+\nu/t) so that ν\nu represents the percentage excess kurtosis over the Brownian motion process over a unit time increment (where over longer time increments the excess kurtosis decreases to 0 linearly in tt).

However, for θ≠0\theta\neq 0 the variance of the process is higher than that of the Brownian motion - this increase in average variation stems from additional variance contributions from the random drift component under the time-subordination (being deterministic, the drift component in a Brownian motion does not contribute to the variance). As a result, the Variance-Gamma typically values options higher due to this increase in volatility.

## 4 Option Pricing

### 4.1 Physical process

We are now suitably placed to begin exploring the dynamics of a stock price under a V​GVG model, and the associated European call option pricing mechanism. Our exploration follows a similar method to that of the Black-Scholes formulation for European call options, now extending geometric Brownian motion assumption to a more general geometric V​GVG process.

Consider a continuous-time economy where a stock, a money market account and European options for the stock for all strikes and maturities are traded in a given time frame. Further suppose that there is a constant continuously compounded interest rate of rr with corresponding money market account value of er​te^{rt} at time tt following a unit deposit at time 0.

Under a geometric V​GVG model, the price of the underlying asset (St)t≥0(S\_{t})\_{t\geq 0} is given by St=S0​em​t+X​(t;θ,σ,ν)+ω​(t)S\_{t}=S\_{0}e^{mt+X(t;\theta,\sigma,\nu)+\omega(t)}, where X​(t;θ,σ,ν)X(t;\theta,\sigma,\nu) is a V​GVG process, and ω​(t)=tν​log⁡(1−ν​θ−ν​σ2/2)\omega(t)=\frac{t}{\nu}\log\left(1-\nu\theta-\nu{\sigma^{2}}/{2}\right), so that the mean return rate is em​te^{mt} for some m∈ℝm\in\mathbb{R} (this can be verified by evaluating the expectation of StS\_{t}) Writing the process in this form allows one to easily identify the mean return rate.

We detail the pricing of European options under the V​GVG model. Specifically we use an Equivalent Martingale Measure (EMM) under which the discounted process (e−r​t​St)t≥0(e^{-rt}S\_{t})\_{t\geq 0} is a Martingale quantity - this encompasses an appropriate change of measure from the physical measure to a risk-neutral measure outlined through the Esscher transform method below (first developed by Frederik Esscher in 1932 [[15](https://arxiv.org/html/2510.14093v1#bib.bib15)]). By finding such a measure, we use the risk-neutral valuation principle to find the price of European call option is given by the expected payoff of the option with respect to the process under the risk-neutral measure.

### 4.2 Esscher transform

We first provide a definition of the Esscher transform (as presented in section 2 of Gerber and Shiu [[16](https://arxiv.org/html/2510.14093v1#bib.bib16)]).

###### Definition 8.

Let f​(x,t)f(x,t) be the density for a Lévy process (Xt)t≥0(X\_{t})\_{t\geq 0} at time tt. One defines the Esscher transform of f​(x,t)f(x,t) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | f^​(x,t,h)=eh​x​f​(x,t)M​(h,t),\hat{f}(x,t,h)=\dfrac{e^{hx}f(x,t)}{M(h,t)}, |  | (35) |

where M​(⋅,t)M(\cdot,t) is the moment generating function of XtX\_{t} at time tt.

###### Remark 12.

The Esscher transform of a probability density is itself a new probability density (as the m.g.f. in the denominator normalises the function to integrate to 1) and this associated Esscher transformed measure is equivalent (mutually absolutely continuous) to the original. Denoting the c.d.f. of XtX\_{t}, FX​(x,t)F\_{X}(x,t),

|  |  |  |  |
| --- | --- | --- | --- |
|  | FX​(x,t)=∫−∞xf​(ξ,t)​𝑑ξ,F\_{X}(x,t)=\int\_{-\infty}^{x}f(\xi,t)d\xi, |  | (36) |

where f​(x,t)f(x,t) is the density of XtX\_{t}. Then the Esscher transformed variable denoted XthX\_{t}^{h}, has a cumulative function given by,

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^​(x,t,h)=∫−∞xf^​(ξ,t,h)​𝑑ξ=∫−∞xeh​ξ​f​(ξ,t)M​(h,t)​𝑑ξ.\hat{F}(x,t,h)=\int\_{-\infty}^{x}\hat{f}(\xi,t,h)d\xi=\int\_{-\infty}^{x}\dfrac{e^{h\xi}f(\xi,t)}{M(h,t)}d\xi. |  | (37) |

From this, we can obtain an EMM for the process XtX\_{t} 666Note that an EMM is not necessarily unique, and indeed when (Xt)t≥0(X\_{t})\_{t\geq 0} follows a V​GVG process we do not have uniqueness. Indeed for geometric Lévy processes, only Brownian motion and compensated Poisson processes have a unique EMM as shown in Théorème 1 of [[17](https://arxiv.org/html/2510.14093v1#bib.bib17)]. This means that there are a range of no-arbitrage prices for the V​GVG process.
This is commented on by Andrusiv and Engelbert [[18](https://arxiv.org/html/2510.14093v1#bib.bib18)] who show that for general Lévy financial markets, the minimal entropy martingale measure coincides with the Esscher martingale measure, and argue that it is an optimal EMM for various utility maximisation problems.
.
Letting the physical measure be ℙ\mathbb{P} and the Esscher transformed measure be ℚh\mathbb{Q}^{h}, we may write the corresponding Radon-Nikodym derivative as,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℚhd​ℙ=eh​XtM​(h,t)\dfrac{d\mathbb{Q}^{h}}{d\mathbb{P}}=\frac{e^{hX\_{t}}}{M(h,t)} |  | (38) |

where we need to choose hh appropriately to ensure ℚh\mathbb{Q}^{h} is a Martingale measure for the discounted process (e−r​t​St)t≥0(e^{-rt}S\_{t})\_{t\geq 0} where St=S0​eXtS\_{t}=S\_{0}e^{X\_{t}}.

###### Lemma 5.

The value of h=h∗h=h^{\*} which makes the discounted process a Martingale quantity under the corresponding transformed measure is determined implicitly through

|  |  |  |  |
| --- | --- | --- | --- |
|  | er​t=M​(h∗+1,t)M​(h∗,t).e^{rt}=\dfrac{M(h^{\*}+1,t)}{M(h^{\*},t)}. |  | (39) |

###### Proof.

Consider the process (e−r​t​St)t≥0(e^{-rt}S\_{t})\_{t\geq 0} with filtration (ℱt)t≥0(\mathcal{F}\_{t})\_{t\geq 0}. We seek some h∗h^{\*} such that for the measure ℚ:=ℚh∗\mathbb{Q}:=\mathbb{Q}^{h^{\*}}, we satisfy the Martingale equation, 𝔼ℚ​[e−r​t​St|ℱ0]=S0\mathbb{E}^{\mathbb{Q}}\left[e^{-rt}S\_{t}\hskip 2.84544pt\big|\mathcal{F}\_{0}\right]=S\_{0}.
We must then satisfy

|  |  |  |
| --- | --- | --- |
|  | S0=𝔼ℚ​[e−r​t​St|ℱ0]=𝔼ℙ​[d​ℚd​ℙ​e−r​t​St|ℱ0]=S0​e−r​t​𝔼ℙ​[e(1+h∗)​XtM​(h∗,t)|ℱ0]=S0​e−r​t​M​(h∗+1,t)M​(h∗,t),\displaystyle S\_{0}=\mathbb{E}^{\mathbb{Q}}\left[e^{-rt}S\_{t}\hskip 2.84544pt\big|\mathcal{F}\_{0}\right]=\mathbb{E}^{\mathbb{P}}\left[\dfrac{d\mathbb{Q}}{d\mathbb{P}}e^{-rt}S\_{t}\hskip 2.84544pt\Big|\mathcal{F}\_{0}\right]=S\_{0}e^{-rt}\mathbb{E}^{\mathbb{P}}\left[\dfrac{e^{(1+h^{\*})X\_{t}}}{M(h^{\*},t)}\hskip 2.84544pt\Big|\mathcal{F}\_{0}\right]=S\_{0}e^{-rt}\dfrac{M(h^{\*}+1,t)}{M(h^{\*},t)}, |  |

so that h∗h^{\*} is indeed determined implicitly through the relation ([39](https://arxiv.org/html/2510.14093v1#S4.E39 "In Lemma 5. ‣ 4.2 Esscher transform ‣ 4 Option Pricing ‣ The Variance Gamma Process for Option Pricing")).
∎

We employ the transform in the context of our V​GVG process. Let M​(⋅,t)M(\cdot,t) be the moment generating function of the V​GVG model X​(t;θ,σ,ν)X(t;\theta,\sigma,\nu). Then, from integration,

|  |  |  |  |
| --- | --- | --- | --- |
|  | M​(h,t)=(11−ν​θ​h−ν​σ22​h2)tν,h1<h<h2M(h,t)=\left(\dfrac{1}{1-\nu\theta h-\nu\frac{\sigma^{2}}{2}h^{2}}\right)^{\frac{t}{\nu}},\hskip 14.22636pth\_{1}<h<h\_{2} |  | (40) |

where (considering the region for which the quadratic denominator is non-zero)

|  |  |  |  |
| --- | --- | --- | --- |
|  | h1=−θσ2−θ2σ4+2ν​σ2,h2=−θσ2+θ2σ4+2ν​σ2h\_{1}=-\frac{\theta}{\sigma^{2}}-\sqrt{\frac{\theta^{2}}{\sigma^{4}}+\frac{2}{\nu\sigma^{2}}}\hskip 7.11317pt,\hskip 7.11317pth\_{2}=-\frac{\theta}{\sigma^{2}}+\sqrt{\frac{\theta^{2}}{\sigma^{4}}+\frac{2}{\nu\sigma^{2}}} |  | (41) |

###### Remark 13.

The existence and uniqueness of such a h∗h^{\*} in the V​GVG case is shown in the Appendix [8.5](https://arxiv.org/html/2510.14093v1#S8.SS5 "8.5 Proof of remark 13 ‣ 8 Appendix ‣ The Variance Gamma Process for Option Pricing").
As relation ([39](https://arxiv.org/html/2510.14093v1#S4.E39 "In Lemma 5. ‣ 4.2 Esscher transform ‣ 4 Option Pricing ‣ The Variance Gamma Process for Option Pricing")) for the V​GVG process,

|  |  |  |  |
| --- | --- | --- | --- |
|  | er​t=(1−ν​θ​h∗−ν​σ22​h∗21−νθ(h∗+1)−νσ22(h∗+1)2)tνe^{rt}=\left(\dfrac{1-\nu\theta h^{\*}-\nu\frac{\sigma^{2}}{2}{h^{\*}}^{2}}{1-\nu\theta(h\*+1)-\nu\frac{\sigma^{2}}{2}(h\*+1)^{2}}\right)^{\frac{t}{\nu}} |  | (42) |

can be expressed as a quadratic in h∗h^{\*} (by multiplying the numerator on both sides), one can compute a formula for h∗h^{\*} in terms of the other parameters; however, the resulting formula is very complicated and we omit this here.

In the case of a Brownian motion b​(t;θ,σ)b(t;\theta,\sigma) (or considering a degenerate V​GVG process with ν=0\nu=0) one finds h∗=(r−θ)/σ2−1/2h^{\*}=(r-\theta)/\sigma^{2}-1/2. Furthermore, as all contingent claims can be replicated in the Black-Scholes market, there is a unique EMM for the Brownian motion model, and
the Esscher transformed measure with this h∗h^{\*} gives this unique EMM exactly when we restrict to this case.

Consider the set of measures {ℚh:h∈(h1,h2)}\{\mathbb{Q}^{h}:h\in(h\_{1},h\_{2})\} for the V​GVG process. Computing the m.g.f. of the V​GVG model M​(⋅,t,h)M(\cdot,t,h) with respect to the measure ℚh\mathbb{Q}^{h},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | M​(z,t,h)\displaystyle M(z,t,h) | =𝔼ℚh​[ez​Xt]=∫ez​Xt​ℚh​(d​Xt)=∫−∞∞ez​x​f^​(x,t,h)​𝑑x=∫−∞∞e(h+z)​x​f​(x,t)M​(h,t)​𝑑x\displaystyle=\mathbb{E}^{\mathbb{Q}^{h}}\left[e^{zX\_{t}}\right]=\int e^{zX\_{t}}\mathbb{Q}^{h}(dX\_{t})=\int\_{-\infty}^{\infty}e^{zx}\hat{f}(x,t,h)dx=\int\_{-\infty}^{\infty}\dfrac{e^{(h+z)x}f(x,t)}{M(h,t)}dx |  | (43) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =M​(h+z,t)M​(h,t)=(1−ν​θ​h−ν​σ22​h21−ν​θ​(h+z)−ν​σ22​(h+z)2)tν.\displaystyle=\dfrac{M(h+z,t)}{M(h,t)}=\left(\dfrac{1-\nu\theta h-\nu\frac{\sigma^{2}}{2}h^{2}}{1-\nu\theta(h+z)-\nu\frac{\sigma^{2}}{2}(h+z)^{2}}\right)^{\frac{t}{\nu}}. |  | (44) |

Having established the moment generating function of the process under ℚh\mathbb{Q}^{h}, we may give the following Proposition.

###### Proposition 5.

The Esscher transform of the V​GVG process X​(t;σ,ν,θ)X(t;\sigma,\nu,\theta) is also a V​GVG process X~​(t;σ,ν~,θ~)\tilde{X}(t;\sigma,\tilde{\nu},\tilde{\theta}) where

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ~=θ+h​σ2,ν~=ν1−ν​θ​h−ν​σ22​h2.\tilde{\theta}=\theta+h\sigma^{2},\hskip 14.22636pt\tilde{\nu}=\dfrac{\nu}{1-\nu\theta h-\nu\frac{\sigma^{2}}{2}h^{2}}. |  | (45) |

The values are obtained upon rearranging ([44](https://arxiv.org/html/2510.14093v1#S4.E44 "In 4.2 Esscher transform ‣ 4 Option Pricing ‣ The Variance Gamma Process for Option Pricing")) (effectively dividing the numerator and denominator in ([44](https://arxiv.org/html/2510.14093v1#S4.E44 "In 4.2 Esscher transform ‣ 4 Option Pricing ‣ The Variance Gamma Process for Option Pricing")) by the numerator) to find

|  |  |  |  |
| --- | --- | --- | --- |
|  | M​(z,t,h)=(11−ν~​θ~​z−ν~​σ22​z2)tν,M(z,t,h)=\left(\dfrac{1}{1-\tilde{\nu}\tilde{\theta}z-\tilde{\nu}\frac{\sigma^{2}}{2}z^{2}}\right)^{\frac{t}{\nu}}, |  | (46) |

where θ~,ν~\tilde{\theta},\tilde{\nu} are as above, which is indeed the moment generating function of a V​GVG process with the new parameters. The full calculation can be found in the Appendix [8.6](https://arxiv.org/html/2510.14093v1#S8.SS6 "8.6 Proof of proposition 5 ‣ 8 Appendix ‣ The Variance Gamma Process for Option Pricing").

###### Remark 14.

For the case h=h∗h=h^{\*}, one labels the transformed parameters the risk-neutral parameters. In the V​GVG model, we have three risk-neutral parameters as above; however, for a Brownian motion b​(t;θ,σ)b(t;\theta,\sigma) the risk neutral parameters are independent of θ\theta, with θ~=r−σ2/2\tilde{\theta}=r-\sigma^{2}/2 and σ~=σ\tilde{\sigma}=\sigma is unchanged.

Intuitively this is to be expected - a deterministic drift θ​t\theta t should have no affect on the risk-neutral measure (one can formalise this notion with a portfolio replication argument). The fact that there is only one parameter governing the risk-neutral density for a Brownian motion means that the option pricing dynamics are constrained to only vary with one variable σ\sigma which, as shown in the empirical results of Madan et al. [[6](https://arxiv.org/html/2510.14093v1#bib.bib6)], proves restrictive.

However, the V​GVG risk-neutral measure maintains a drift term. In particular, the stochastic time change of the V​GVG process affects the drift term meaning that the drift is now also stochastic - a faster time change causing greater drift, and slower time change causing weaker drift. Empirically, it appears the inclusion of the drift term in the V​GVG model this gives significant reduction in mean squared error over Black-Scholes when comparing the prices S&\&P500 European options on the CBOE with each model.

### 4.3 Variance Gamma European call option price

Having found our desired EMM ℚ\mathbb{Q}, we explore the call option pricing mechanism for a V​GVG process, following a similar analysis to Nzokem (2023) [[19](https://arxiv.org/html/2510.14093v1#bib.bib19)].

###### Theorem 1.

Suppose we model the value of an underlying asset through a process (St)t≥0(S\_{t})\_{t\geq 0} with filtration (ℱt)t≥0(\mathcal{F}\_{t})\_{t\geq 0}. From the risk-neutral valuation principle, given a spot price S0S\_{0} at time 0, the price of a European call option 𝒞​(S0;K,t)\mathcal{C}(S\_{0};K,t) for a strike price KK and maturity tt is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞​(S0;K,t)=e−r​t​𝔼ℚ​[(St−K)+|ℱ0],\mathcal{C}(S\_{0};K,t)=e^{-rt}\mathbb{E}^{\mathbb{Q}}\left[\left(S\_{t}-K\right)\_{+}\hskip 2.84544pt\big|\mathcal{F}\_{0}\right], |  | (47) |

where the expectation is taken under the risk neutral measure ℚ\mathbb{Q}. If the price StS\_{t} follows a geometric V​GVG process such that St=S0​eXtS\_{t}=S\_{0}e^{X\_{t}} for Xt=X​(t;θ,σ,ν)X\_{t}=X(t;\theta,\sigma,\nu), the European call option price is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞​(S0;K,t)=S0​[1−F^​(log⁡(KS0),t,h∗+1)]−K​e−r​t​[1−F^​(log⁡(KS0),t,h∗)],\mathcal{C}(S\_{0};K,t)=S\_{0}\left[1-\hat{F}\left(\log\left(\frac{K}{S\_{0}}\right),t,h^{\*}+1\right)\right]-Ke^{-rt}\left[1-\hat{F}\left(\log\left(\frac{K}{S\_{0}}\right),t,h^{\*}\right)\right], |  | (48) |

where F^​(x,t,h)\hat{F}{(x,t,h)} is the cumulative function of the Esscher transformed V​G​(t;θ,σ,ν)VG(t;\theta,\sigma,\nu) process,

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^​(x,t,h)=∫−∞xf^​(ξ,t,h)​𝑑ξ.\hat{F}(x,t,h)=\int\_{-\infty}^{x}\hat{f}(\xi,t,h)d\xi. |  | (49) |

###### Proof.

From equation ([47](https://arxiv.org/html/2510.14093v1#S4.E47 "In Theorem 1. ‣ 4.3 Variance Gamma European call option price ‣ 4 Option Pricing ‣ The Variance Gamma Process for Option Pricing")) we may write

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞​(S0;K,t)=e−r​t​𝔼ℚ​[(St−K)+|ℱ0]=e−r​t​𝔼ℚ​[(S0​eXt−K)+|ℱ0].\mathcal{C}(S\_{0};K,t)=e^{-rt}\mathbb{E}^{\mathbb{Q}}\left[\left(S\_{t}-K\right)\_{+}\hskip 2.84544pt\big|\mathcal{F}\_{0}\right]=e^{-rt}\mathbb{E}^{\mathbb{Q}}\left[\left(S\_{0}e^{X\_{t}}-K\right)\_{+}\hskip 2.84544pt\big|\mathcal{F}\_{0}\right]. |  | (50) |

Our risk-neutral measure ℚ\mathbb{Q} has a density f^​(x,t,h∗)\hat{f}(x,t,h^{\*}) and we write

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞​(S0;K,t)=e−r​t​∫(S0​eXt−K)+​ℚ​(d​Xt)=e−r​t​∫−∞∞(S0​eξ−K)+​f^​(ξ,t,h∗)​𝑑ξ.\mathcal{C}(S\_{0};K,t)=e^{-rt}\int(S\_{0}e^{X\_{t}}-K)\_{+}\mathbb{Q}(dX\_{t})=e^{-rt}\int\_{-\infty}^{\infty}(S\_{0}e^{\xi}-K)\_{+}\hat{f}(\xi,t,h^{\*})d\xi. |  | (51) |

Considering the integrand is non-zero for ξ∈(log⁡k,∞)\xi\in\left(\log k,\infty\right) where k=K/S0k=K/S\_{0}, we may split the integral.

|  |  |  |  |
| --- | --- | --- | --- |
|  | e−r​t​∫−∞∞(S0​eξ−K)+​f^​(ξ,t,h∗)​𝑑ξ=e−r​t​S0​∫log⁡k∞eξ​f^​(ξ,t,h∗)​𝑑ξ−K​e−r​t​∫log⁡k∞f^​(ξ,t,h∗)​𝑑ξ.e^{-rt}\int\_{-\infty}^{\infty}(S\_{0}e^{\xi}-K)\_{+}\hat{f}(\xi,t,h^{\*})d\xi=e^{-rt}S\_{0}\int\_{\log k}^{\infty}e^{\xi}\hat{f}(\xi,t,h^{\*})d\xi-Ke^{-rt}\int\_{\log k}^{\infty}\hat{f}(\xi,t,h^{\*})d\xi. |  | (52) |

The second integral term is already in the desired form, but the first integrates eξe^{\xi} against the risk-neutral density. We employ our results on the moment generating function and the implicit relation for h∗h^{\*} from Lemma ([5](https://arxiv.org/html/2510.14093v1#Thmlemma5 "Lemma 5. ‣ 4.2 Esscher transform ‣ 4 Option Pricing ‣ The Variance Gamma Process for Option Pricing")). From the definition of the Esscher transform f^\hat{f},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫log⁡k∞eξ​f^​(ξ,t,h∗)​𝑑ξ=∫log⁡k∞eξ​eh∗​ξ​f​(ξ,t)M​(h∗,t)​𝑑ξ=M​(h∗+1,t)M​(h∗,t)​∫log⁡k∞e(h∗+1)​ξ​f​(ξ,t)M​(h∗+1,t)​𝑑ξ.\int\_{\log k}^{\infty}e^{\xi}\hat{f}(\xi,t,h^{\*})d\xi=\int\_{\log k}^{\infty}e^{\xi}\dfrac{e^{h^{\*}\xi}f(\xi,t)}{M(h^{\*},t)}d\xi=\dfrac{M(h^{\*}+1,t)}{M(h^{\*},t)}\int\_{\log k}^{\infty}\dfrac{e^{(h^{\*}+1)\xi}f(\xi,t)}{M(h^{\*}+1,t)}d\xi. |  | (53) |

Recall from the implicit definition for h∗h^{\*} from ([39](https://arxiv.org/html/2510.14093v1#S4.E39 "In Lemma 5. ‣ 4.2 Esscher transform ‣ 4 Option Pricing ‣ The Variance Gamma Process for Option Pricing")) that the factor outside the integral is equal to er​te^{rt}. The integrand is now exactly f^​(ξ,t,h∗+1)\hat{f}(\xi,t,h^{\*}+1), and so

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫log⁡k∞eξ​f^​(ξ,t,h∗)​𝑑ξ=er​t​∫log⁡k∞f^​(ξ,t,h∗+1)​𝑑ξ.\int\_{\log k}^{\infty}e^{\xi}\hat{f}(\xi,t,h^{\*})d\xi=e^{rt}\int\_{\log k}^{\infty}\hat{f}(\xi,t,h^{\*}+1)d\xi. |  | (54) |

Then indeed

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞​(S0;K,t)=S0​∫log⁡k∞f^​(ξ,t,h∗+1)​𝑑ξ−K​e−r​t​∫log⁡k∞f^​(ξ,t,h∗)​𝑑ξ,\mathcal{C}(S\_{0};K,t)=S\_{0}\int\_{\log k}^{\infty}\hat{f}(\xi,t,h^{\*}+1)d\xi-Ke^{-rt}\int\_{\log k}^{\infty}\hat{f}(\xi,t,h^{\*})d\xi, |  | (55) |

which yields the result upon integration.
∎

###### Remark 15.

The formula demonstrates strong resemblance with the equivalent Black-Scholes European call option pricing formula. The first term represents the present value S0S\_{0} of holding the stock if the option is exercised, weighted against the probability that the future value StS\_{t} finishes in the money. The second term represents the cost K​e−r​tKe^{-rt} of exercising the option weighted against the probability that the future value StS\_{t} exceeds the strike.

## 5 Comparison with Black-Scholes

Having obtained an option pricing mechanism, we explore properties of the V​GVG call option price and compare with the well-documented Black-Scholes approach

Suppose that the price of an underlying asset follows a geometric V​GVG process, with a fixed strike price of 100100 for a range of European call options with a fixed 2 week maturity. The corresponding call option price for each spot price of the underlying is given in Figure ([6](https://arxiv.org/html/2510.14093v1#S5.F6 "Figure 6 ‣ 5 Comparison with Black-Scholes ‣ The Variance Gamma Process for Option Pricing")) below, varying σV​G\sigma\_{VG}.

![Refer to caption](Figures/R_plots/RNVG_options.png)


Figure 6: Option prices under a V​GVG model. r=0.05,θ=−0.1,ν=0.2r=0.05,\theta=-0.1,\nu=0.2, time to maturity 2 weeks.

###### Remark 16.

We obtain the familiar hockey stick shape for the call option price with greater call option values for greater volatility (caused by a greater σ\sigma parameter). This agrees with our expectation - for out of the money spot prices, the probability that the option will be exercised is low and the corresponding option has lower value. The reverse applies for in the money spot prices where there is greater probability that the option will be exercised. A higher volatility (through greater σ\sigma) corresponds to greater expected fluctuation in the stock price and so greater expected returns from the option.

We now compare with the Black-Scholes sub-model price for the equivalent option in Figure ([7](https://arxiv.org/html/2510.14093v1#S5.F7 "Figure 7 ‣ 5 Comparison with Black-Scholes ‣ The Variance Gamma Process for Option Pricing")) (where the V​GVG parameters are the same while varying σV​G\sigma\_{VG}). The Black-Scholes model volatility σB​S\sigma\_{BS} is chosen to match the volatilities of the corresponding V​GVG model using the moment calculations of section [3.3](https://arxiv.org/html/2510.14093v1#S3.SS3 "3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing"), so that θV​G2​νV​G+σV​G2=σB​S2\theta\_{VG}^{2}\nu\_{VG}+\sigma^{2}\_{VG}=\sigma^{2}\_{BS}. Recall θV​G\theta\_{VG} represents the average drift of the V​GVG process, while νV​G\nu\_{VG} represents the variance of the Gamma process subordinating the Brownian motion for the V​GVG process.

Figure [7](https://arxiv.org/html/2510.14093v1#S5.F7 "Figure 7 ‣ 5 Comparison with Black-Scholes ‣ The Variance Gamma Process for Option Pricing")(a) demonstrates that the Variance Gamma and Black-Scholes models tend to generally price options in a similar manner, following the typical hockey stick shape. However, Figure [7](https://arxiv.org/html/2510.14093v1#S5.F7 "Figure 7 ‣ 5 Comparison with Black-Scholes ‣ The Variance Gamma Process for Option Pricing")(b) demonstrates a clear trend to the difference in the option prices between the two models. For spot prices further in or out of the money, the Variance Gamma option price is significantly higher than the Black-Scholes, whereas for spot prices close to at the money the Black-Scholes option price is much higher, with increasing volatility exaggerating the difference in both cases.

![Refer to caption](Figures/R_plots/RNVG_vs_Black-Scholes.png)


(a)

![Refer to caption](Figures/R_plots/RNVG_diff_Black-Scholes.png)


(b)

Figure 7: Variance Gamma - Black-Scholes difference in call option price.

###### Remark 17.

Once again this is expected - as explained in the previous sections, the more general Variance Gamma distribution is leptokurtic exhibiting greater kurtosis than the Gaussian with sharper peaks about the median and heavier tails.

For spot prices close to at the money, one would not expect the price of the underlying asset to deviate as much under a Variance Gamma model compared to Black-Scholes - the sharper peak around the centre of the density function attributes greater probability to the price deviating minimally. However, the Variance Gamma model assigns greater probability to a larger price deviation than Black-Scholes thereby increasing the value of the corresponding option for spot prices far in or out of the money.

![Refer to caption](Figures/R_plots/RNVG_Implied_Volatility.png)


Figure 8: Implied Black-Scholes volatility from Variance Gamma simulated prices

From this result, one may question whether fitting a Black-Scholes implied volatility to prices simulated from a general Variance Gamma model with ν\nu significantly greater than 0 will lead to a volatility smile, as the phenomenon is often attributed to greater kurtosis in log-returns data. Figure ([8](https://arxiv.org/html/2510.14093v1#S5.F8 "Figure 8 ‣ 5 Comparison with Black-Scholes ‣ The Variance Gamma Process for Option Pricing")) shows that this is exactly the case - we invert the Black Scholes formula at each strike for V​GVG calculated prices to calculate the implied volatility. The spot price for Figure ([8](https://arxiv.org/html/2510.14093v1#S5.F8 "Figure 8 ‣ 5 Comparison with Black-Scholes ‣ The Variance Gamma Process for Option Pricing")) is fixed at 100 units, and the other Variance Gamma parameters are as above (notably ν=0.2\nu=0.2 significantly greater than 0). We also observe that increasing the volatility of the Variance Gamma model exaggerates the smile.

Empirically, it does appear that the V​GVG model demonstrates significant improvement over the nested Black-Scholes when fitted to options data. This is shown in section 5 of Madan et al. [[6](https://arxiv.org/html/2510.14093v1#bib.bib6)] where the authors fit both V​GVG and Black-Scholes models on a weekly basis for 143 weeks of S&\&P500 data, rejecting a Black-Scholes null hypothesis at the 5%\% level for 93.7%93.7\% of weeks, and at the 1%\% level for 91.6%91.6\% of weeks.

It also appears that the V​GVG model’s additional parameters are capable of flattening the empirical implied volatility smile - this is shown in section 6 of Madan et al. [[6](https://arxiv.org/html/2510.14093v1#bib.bib6)] which deals with the pricing performance of the V​GVG model against the nested Black-Scholes. The authors employ regression analysis through orthogonality tests for both models - these test whether there are any consistent patterns in pricing errors due to variables such as moneyness, maturity, and the interest rate. The authors find that for the Black-Scholes and symmetric V​GVG models, the pricing error has a high moneyness dependency for the options in the data (the symmetric V​GVG does still perform better than Black-Scholes); however, the pricing error for the general V​GVG model (with drift) is mostly free of this dependency.

## 6 Empirical Results

### 6.1 Data for the study

For our study we have used S&\&P500 futures traded at the Chicago Board Options Exchange (CBOE). The S&\&P 500 futures options we consider are European call options traded with a 7-day maturity between August 2022 and August 2023.

The data for the study were obtained from the Wharton Research Data Services and include all transaction option prices from August 31, 2022 to August 31 2023. Closing prices on index futures and the level of the spot index were also available from the Federal Reserve Economic Data. All options contracts were viewed as written on the underlying spot index. There were 46135 options prices over the 1 year period considered in the analysis.

### 6.2 Daily Log Returns

We begin the analysis by estimating the parameter values of the statistical densities for daily log returns over the period above for the V​GVG model and the nested Gaussian sub-model. The data employed were the 262 daily observations of log spot price of the S&\&P500 Index covering the period. For the stock price dynamics under the V​GVG model, we employ the density in equation [18](https://arxiv.org/html/2510.14093v1#S3.E18 "In 3.1 The symmetric Variance Gamma distribution ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing") while the stock price dynamics underlying the Gaussian sub-model is of course a Gaussian density with mean θ\theta and standard deviation σ\sigma. Recall from Remark ([11](https://arxiv.org/html/2510.14093v1#Thmremark11 "Remark 11. ‣ 3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")) that this Gaussian sub-model is nested in the V​GVG model through the degenerate case where ν=0\nu=0 which permits us to perform an approximate likelihood ratio test on the results. We employ maximum likelihood estimation for all parameters and present the estimated parameter values in Table ([1](https://arxiv.org/html/2510.14093v1#S6.T1 "Table 1 ‣ 6.2 Daily Log Returns ‣ 6 Empirical Results ‣ The Variance Gamma Process for Option Pricing")).

|  |  |  |
| --- | --- | --- |
| Estimated Parameter | Gaussian Model | V​GVG Model |
| θ\theta | 0.0005925507 | -0.001323872 |
| σ\sigma | 0.01141282 | 0.01201207 |
| ν\nu | ⋅\cdot | 0.02942378 |
| log⁡ℒ\log\mathcal{L} | 1004.44275 | 1012.215 |
| NOBS | 252 | 252 |

Table 1: Fitted S&\&P500 daily log returns

The estimated ν\nu parameter of the V​GVG model ν=0.02942378\nu=0.02942378 appears to be significantly different from zero which suggests we should expect to reject a Gaussian null hypothesis in favour of a V​GVG alternative. Indeed, with the use of Wilks’ theorem we can perform an approximate chi-squared test, in that under the null hypothesis, the statistic

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​(log⁡ℒV​G−log⁡ℒGaussian)2\left(\log\mathcal{L}\_{VG}-\log\mathcal{L}\_{\text{Gaussian}}\right) |  | (56) |

is approximately chi-squared distributed with 1 degree of freedom (as the V​GVG model has one additional parameter). Here the statistic is equal to 15.5445 which strongly rejects777this gives a p-value less than 0.0001 under the χ12\chi^{2}\_{1} distribution. the Gaussian hypothesis in favour of the V​GVG model.

### 6.3 Option pricing

For our theoretical V​GVG option pricing mechanism, we made use of the Esscher transform to obtain the risk-neutral measure for the V​GVG model. We employ the density of this measure for a similar parameter estimation, this time estimating the parameters of both the risk-neutral Black-Scholes density and risk-neutral V​GVG density used to appropriately price options. We fit both densities to the option price data on a weekly basis via a maximum-likelihood method.

We present the average estimated parameter values of the risk neutral densities, along with
their standard deviation across 52 weeks, as well as the minimum and maximum estimated values over the period in Table ([2](https://arxiv.org/html/2510.14093v1#S6.T2 "Table 2 ‣ 6.3 Option pricing ‣ 6 Empirical Results ‣ The Variance Gamma Process for Option Pricing")). We also include the log-likelihood statistics for each model, again showing the average and standard deviation across the weeks, as well as the minimum and maximum values over the period.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Parameter | Mean | Standard deviation | Minimum | Maximum |
| *Black Scholes* | | | | |
| σ\sigma | 0.18010 | 0.03643 | 0.03128 | 0.28604 |
| log⁡ℒ\log\mathcal{L} | 0.00422 | 0.00239 | 0.00182 | 0.01723 |
| *Variance Gamma* | | | | |
| σ\sigma | 0.1793376 | 0.0505 | 0.02983 | 0.30049 |
| θ\theta | 0.03015743 | 0.51320 | -1.57233 | 1.65062 |
| ν\nu | 0.01231924 | 0.01698 | 0.00528 | 0.02093 |
| log⁡ℒ\log\mathcal{L} | 0.00523 | 0.00301 | 0.00191 | 0.01799 |

Table 2: Weekly parameter estimation of Black-Scholes and V​GVG model S&\&P500 options

For each week we construct an approximate chi-squared test in the same form as equation ([56](https://arxiv.org/html/2510.14093v1#S6.E56 "In 6.2 Daily Log Returns ‣ 6 Empirical Results ‣ The Variance Gamma Process for Option Pricing")), though this time under a Black-Scholes null hypothesis the statistic in ([56](https://arxiv.org/html/2510.14093v1#S6.E56 "In 6.2 Daily Log Returns ‣ 6 Empirical Results ‣ The Variance Gamma Process for Option Pricing")) now follows a χ22\chi^{2}\_{2} distribution, as the risk-neutral V​GVG density has 2 further degrees of freedom (θ,ν\theta,\nu) over the risk-neutral Black-Scholes. From the data, the Black Scholes model is rejected at the 5%\% level888noting that the χ22\chi^{2}\_{2} has a critical value of 0.000110.00011 at the 5%5\% level, and 0.020100.02010 at the 1%1\% level for 4848 out of the 5252 weeks (92.3%92.3\%) in favour of the V​GVG model, and rejected at the 1%1\% level for 4545 out of the 5252 weeks (86.5%86.5\%) in favour of the V​GVG model.

## 7 Summary

This paper explores the concept of stochastic volatility in modelling stock-price dynamics, first presenting results on the Laplace distribution as a Gaussian variance-mixture and generalising this idea to find the powerful variance gamma model as a Gamma time-subordinated Brownian motion to price European call options.

We propose a more efficient form of volatility estimation when one assumes that the log-returns from an underlying follow a Laplace distribution. Notably, the mean absolute absolute deviation about the median proves a more efficient estimator for the volatility parameter.

The Laplace distribution is generalised to consider the V​GVG distribution as a Gaussian with gamma distributed variance. We then characterise the V​GVG process as a time-subordinated Brownian motion with a Gamma process subordinator.

A general European call option pricing mechanism is formulated via the use of the Esscher transform to find a corresponding EMM measure, and we investigate the properties of the EMM measure for the V​GVG model. This allows us to compute the European call option price under the V​GVG model.

The theoretical differences between the more general V​GVG model and the nested Black-Scholes are explored - the extra degrees of freedom for the V​GVG allow the more general model to better capture the excess kurtosis of returns data, and provide a possible explanation for the presence of implied volatility smiles when fitting the Black-Scholes model. Referring to works comparing the empirical performance of the V​GVG model against the Black-Scholes both in modelling daily log returns and the appropriate pricing of options for various markets, a majority of studies find that the Black-Scholes model is strongly rejected in favour of the more general V​GVG model.

## Acknowledgements

We would like to acknowledge the Imperial-MIT International Research Opportunities Programme without which this research collaboration would not have been possible. Rohan Shenoy would like to acknowledge the financial support provided by the Mathematics Department at Imperial College London, the Imperial International Relations Office, and the UK Government’s Turing Scheme.

## References

* [1]

  Dilip Madan and Eugene Seneta.
  The variance gamma (v.g.) model for share market returns.
  The Journal of Business, 1990.
* [2]

  Fischer Black and Myron Scholes.
  The pricing of options and corporate liabilities.
  Journal of political economy, 81(3):637, 1973.
* [3]

  Peter D. Praetz.
  The distribution of share price changes.
  The Journal of Business, 1972.
* [4]

  Fima C. Klebaner and Zinoviy Landsman.
  Option pricing for log-symmetric distributions of returns.
  Methodology and Computing in Applied Probability, 2009.
* [5]

  Frank Milne and Dilip Madan.
  Option pricing with v. g. martingale components.
  Queen’s University, 1991.
* [6]

  Dilip Madan, Peter Carr, and Eric Chang.
  The variance gamma process and option pricing.
  European Finance Review, page 79–105, 1998.
* [7]

  Patrick Boyle and Jesse McDougall.
  Chapter 11. Volatility Smiles, pages 127–136.
  De Gruyter, Berlin, Boston, 2019.
* [8]

  Ignacio Peña, Gonzalo Rubio, and Gregorio Serna.
  Why do we smile? on the determinants of the implied volatility function.
  Journal of Banking &\& Finance, Volume 23, Issue 8, pages 1151–1179, 1999.
* [9]

  Badiollah R. Asrabadi.
  The exact confidence interval for the scale parameter and the mvue of the laplace distribution.
  Communications in Statistics - Theory and Methods, 14(3):713–733, 1985.
* [10]

  Samuel Kotz, Tomaz J. Kozubowski, and Krzysztof Podgórski.
  The Laplace Distribution and Generalizations.
  Birkhäuser Boston, MA, 2001.
* [11]

  Adrian Fischer, Robert E. Gaunt, and Andrey Sarantsev.
  The variance-gamma distribution: A review, 2023.
* [12]

  Alfréd Rényi.
  On measures of entropy and information, 1961.
* [13]

  E. T. Jaynes.
  Information theory and statistical mechanics.
  Phys. Rev., 106:620–630, May 1957.
* [14]

  David Applebaum.
  Lévy Processes and Stochastic Calculus.
  Cambridge Studies in Advanced Mathematics. Cambridge University Press, 2004.
* [15]

  Frederik Esscher.
  On the probability function in the collective theory of risk.
  Scandinavian Actuarial Journal, 1932(3):175–195, 1932.
* [16]

  Hans U. Gerber and Shiu E.S.W.
  Option pricing by Esscher transforms.
  Insurance Mathematics & Economics, 3:287, 1995.
* [17]

  Marc Yor and José de Sam Lazaro.
  Sous-espaces denses dans l1l^{1} ou h1h^{1} et représentation des martingales.
  Séminaire de probabilités de Strasbourg, 12:265–309, 1978.
* [18]

  Andrii Andrusiv and Hans-Jürgen Engelbert.
  On the minimal entropy martingale measure for lévy processes.
  Stochastics, 92(8):1223–1243, 2020.
* [19]

  Aubain Hilaire Nzokem.
  Pricing european options under stochastic volatility models: Case of five-parameter variance-gamma process.
  Journal of Risk and Financial Management, 2023.
* [20]

  A. M. Kagan, I.U. V. Linnik, and C. Radhakrishna Rao.
  Characterization problems in mathematical statistics.
  Wiley series in probability and mathematical statistics. Wiley, 1973.
* [21]

  B. Fristedt and L. Gray.
  A Modern Approach to Probability Theory.
  Birkhauser, Boston, MA, 1997.

## 8 Appendix

### 8.1 Proof of Lemma [2](https://arxiv.org/html/2510.14093v1#Thmlemma2 "Lemma 2. ‣ 2.2 Parameter estimation ‣ 2 The Laplace Distribution ‣ The Variance Gamma Process for Option Pricing")

###### Proof.

Assuming θ\theta is given, we differentiate the log-likelihood with respect to ss,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂∂s​l​(x1,…,xn;s,θ)=−ns+1s2​∑i=1n|xi−θ|.\frac{\partial}{\partial s}l(x\_{1},\dots,x\_{n};s,\theta)=-\frac{n}{s}+\frac{1}{s^{2}}\sum\_{i=1}^{n}|x\_{i}-\theta|. |  | (57) |

Setting this equal to 0 we do find s^\hat{s} is given by ([9](https://arxiv.org/html/2510.14093v1#S2.E9 "In Lemma 2. ‣ 2.2 Parameter estimation ‣ 2 The Laplace Distribution ‣ The Variance Gamma Process for Option Pricing")). Finding the variance of the estimator,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var ​s^=Var​[1n​∑i=1n|xi−θ|]=1n​(𝔼​[|Xi−θ|2]−(𝔼​[|Xi−θ|])2)=1n​(2​s2−s2)=s2n.\text{Var }\hat{s}=\text{Var}\left[\frac{1}{n}\sum\_{i=1}^{n}|x\_{i}-{\theta}|\right]=\frac{1}{n}\left(\mathbb{E}\left[|X\_{i}-\theta|^{2}\right]-\left(\mathbb{E}\left[|X\_{i}-\theta|\right]\right)^{2}\right)\\ =\frac{1}{n}(2s^{2}-s^{2})=\frac{s^{2}}{n}. |  | (58) |

This corresponds with the Cramér-Rao lower bound - indeed, calculating the Fisher information

|  |  |  |
| --- | --- | --- |
|  | 𝕀n​(f)=−n​𝔼​[∂2∂s2​log⁡f​(x)]=−n​𝔼​[1s2−2​|X−θ|s3]=−n​(1s2−2​ss3)=ns2,\displaystyle\mathbb{I}\_{n}(f)=-n\mathbb{E}\left[\frac{\partial^{2}}{\partial s^{2}}\log f(x)\right]=-n\mathbb{E}\left[\frac{1}{s^{2}}-\frac{2|X-\theta|}{s^{3}}\right]=-n\left(\frac{1}{s^{2}}-\frac{2s}{s^{3}}\right)=\frac{n}{s^{2}}, |  |

(where we have used ([5](https://arxiv.org/html/2510.14093v1#S2.E5 "In 2.1 Initial characterisation ‣ 2 The Laplace Distribution ‣ The Variance Gamma Process for Option Pricing")) for the central absolute moment) giving the result on taking inverses.
∎

### 8.2 Proof of Lemma [4](https://arxiv.org/html/2510.14093v1#Thmlemma4 "Lemma 4. ‣ 2.2 Parameter estimation ‣ 2 The Laplace Distribution ‣ The Variance Gamma Process for Option Pricing")

###### Proof.

From the strong law of large numbers, 1n​∑i=1n(Xi−θ)2​→𝑝​𝔼​((X−θ)2)=2​σ2\frac{1}{n}\sum\_{i=1}^{n}(X\_{i}-\theta)^{2}\overset{p}{\to}\mathbb{E}\left((X-\theta)^{2}\right)=2\sigma^{2}
so that by a continuity theorem,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​(1n​∑i=1n(Xi−θ)2)​→𝑝​12​(2​σ2)=σ\sqrt{\frac{1}{2}\left(\frac{1}{n}\sum\_{i=1}^{n}(X\_{i}-\theta)^{2}\right)}\overset{p}{\to}\sqrt{\frac{1}{2}\left(2\sigma^{2}\right)}=\sigma |  | (59) |

demonstrating the consistency. To establish asymptotic normality, we first note

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[(X−θ)2]=2σ2,Var[(X−θ)2]=𝔼[X4]−𝔼[X2]2=20σ4,\mathbb{E}\left[(X-\theta)^{2}\right]=2\sigma^{2}\hskip 14.22636pt,\hskip 14.22636pt\text{Var}\left[(X-\theta)^{2}\right]=\mathbb{E}[X^{4}]-\mathbb{E}[X^{2}]^{2}=20\sigma^{4}, |  | (60) |

where the moments are calculated from ([4](https://arxiv.org/html/2510.14093v1#S2.E4 "In 2.1 Initial characterisation ‣ 2 The Laplace Distribution ‣ The Variance Gamma Process for Option Pricing")). Then from the central limit theorem,

|  |  |  |  |
| --- | --- | --- | --- |
|  | n​(σ~−σ)​→𝑑​N​(0,20​σ4).\sqrt{n}(\tilde{\sigma}-\sigma)\overset{d}{\to}N(0,20\sigma^{4}). |  | (61) |

Applying the delta method for g​(x)=x/2g(x)=\sqrt{x/2} so that g′​(x)=12​2​xg^{\prime}(x)=\frac{1}{2\sqrt{2x}},

|  |  |  |  |
| --- | --- | --- | --- |
|  | n​(σ~−σ)​→𝑑​N​(0,g′​(2​σ2)​20​σ4)​=𝑑​N​(0,54​σ2).\sqrt{n}(\tilde{\sigma}-\sigma)\overset{d}{\to}N\left(0,g^{\prime}(2\sigma^{2})20\sigma^{4}\right)\overset{d}{=}N\left(0,\frac{5}{4}\sigma^{2}\right). |  | (62) |

∎

### 8.3 Maximum Entropy distributions

For a random variable XX with density ff, one defines the entropy of XX as H​(X)=𝔼​[−log⁡f​(X)]H(X)=\mathbb{E}\left[-\log{f(X)}\right].
The following theorem from Kagan et al. [[20](https://arxiv.org/html/2510.14093v1#bib.bib20)] provides a framework for finding the density of the maximum entropy distribution, which maximises this expectation.

###### Theorem 2.

Let XX be a random variable with density p​(x)p(x) and support (a,b)(a,b) (where a,ba,b can be ±∞\pm\infty). Let h1,…,hnh\_{1},\dots,h\_{n} be integrable functions on (a,b)(a,b) satisfying for different some constants gig\_{i},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫abhi​(x)​p​(x)​𝑑x=gi.\int\_{a}^{b}h\_{i}(x)p(x)dx=g\_{i}. |  | (63) |

Then the maximum entropy distribution is attained for densities of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(x)=ea0+a1​h1​(x)+⋯​an​hn​(x)p(x)=e^{a\_{0}+a\_{1}h\_{1}(x)+\cdots a\_{n}h\_{n}(x)} |  | (64) |

where the above constraints are all satisfied.

The result follows from the use of Lagrange multipliers to find −log⁡(p)+∑i=1nai​hi≡0-\log(p)+\sum\_{i=1}^{n}a\_{i}h\_{i}\equiv 0.
The full proof can be found in Kagan et al. [[20](https://arxiv.org/html/2510.14093v1#bib.bib20)].

We now see the power of this theorem. One observes that a Gaussian arises as the maximum entropy distribution where the support is the real line, and h1=x,h2=x2h\_{1}=x,h\_{2}=x^{2} so that the first and second moment (or equivalently mean and variance) are specified. The exponent in ([64](https://arxiv.org/html/2510.14093v1#S8.E64 "In Theorem 2. ‣ 8.3 Maximum Entropy distributions ‣ 8 Appendix ‣ The Variance Gamma Process for Option Pricing")) becomes a quadratic which yields the Gaussian density (we require a2>0a\_{2}>0 but this is easily shown).

But instead specifying the first absolute moment through h1​(x)=|x|h\_{1}(x)=|x|, so that ∫ℝ|x|​p​(x)​𝑑x=g1\int\_{\mathbb{R}}|x|p(x)dx=g\_{1}
we find that the density p​(x)p(x) is of the form ea0+a1​|x|e^{a\_{0}+a\_{1}|x|}, a centralised Laplace density. So the Laplace distribution is the maximum entropy distribution when the first absolute moment is specified.

However, it also arises as the maximum entropy distribution of a Gaussian variance-mixture with specified mean, and the specified mean of its random variance VV.
If we specify the mean of VV, then from theorem ([2](https://arxiv.org/html/2510.14093v1#Thmthm2 "Theorem 2. ‣ 8.3 Maximum Entropy distributions ‣ 8 Appendix ‣ The Variance Gamma Process for Option Pricing")) we have
p​(v)=ea0+a1​xp(v)=e^{a\_{0}+a\_{1}x}
which is an exponential distribution. As we have seen, a Gaussian variance-mixture distribution with exponential variance is a Laplace distribution, and so the Laplace distribution arises as the maximum entropy distribution of a Gaussian variance-mixture with specified mean, and specified mean of some random variance VV.

This provides additional motivation for the initial consideration of the Laplace distribution.

### 8.4 Brownian motion as a degenerate Variance Gamma process

Consider taking ν↓0\nu\downarrow 0 with in ([33](https://arxiv.org/html/2510.14093v1#S3.E33 "In 3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing"))

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limν↓0ψXt​(u)\displaystyle\lim\_{\nu\downarrow 0}\psi\_{X\_{t}}(u) | =limν↓0(11−i​θ​ν​u+σ22​ν​u2)tν=limν↓0(1−ν​(i​θ​u+σ22​u2))−tν\displaystyle=\lim\_{\nu\downarrow 0}\left(\dfrac{1}{1-i\theta\nu u+\frac{\sigma^{2}}{2}\nu u^{2}}\right)^{\frac{t}{\nu}}=\lim\_{\nu\downarrow 0}\left({1-\nu\left(i\theta u+\frac{\sigma^{2}}{2}u^{2}\right)}\right)^{\frac{-t}{\nu}} |  | (65) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =limR↑∞((1+−i​θ​u+σ22​u2R)R)−t=(exp⁡(−i​θ​u+σ22​u2))−t=exp⁡(i​θ​t​u−12​σ2​t​u2).\displaystyle=\lim\_{R\uparrow\infty}\left({\left({1+\frac{-i\theta u+\frac{\sigma^{2}}{2}u^{2}}{R}}\right)^{R}}\right)^{-t}=\left(\exp\left(-i\theta u+\frac{\sigma^{2}}{2}u^{2}\right)\right)^{-t}=\exp\left(i\theta tu-\frac{1}{2}\sigma^{2}tu^{2}\right). |  | (66) |

which is indeed the characteristic function of a Brownian motion ([28](https://arxiv.org/html/2510.14093v1#S3.E28 "In 3.3 The Variance Gamma process ‣ 3 The Variance Gamma Process ‣ The Variance Gamma Process for Option Pricing")) (where we have used the complex exponential limit in the penultimate equality). Clearly this is continuous at 0, and so we employ Lévy’s continuity theorem (Theorem 15, section 14.7 of Fristedt and Gray [[21](https://arxiv.org/html/2510.14093v1#bib.bib21)]) to conclude convergence in distribution to the Brownian motion. As discussed, this is intuitive as the Gamma process subordinating the time becomes degenerate with 0 variance about the mean tt, and there is no time-change for the Brownian motion in the limit ν↓0\nu\downarrow 0.

### 8.5 Proof of remark [13](https://arxiv.org/html/2510.14093v1#Thmremark13 "Remark 13. ‣ 4.2 Esscher transform ‣ 4 Option Pricing ‣ The Variance Gamma Process for Option Pricing")

Let H​(h)H(h) be equal to inverse of the RHS of ([39](https://arxiv.org/html/2510.14093v1#S4.E39 "In Lemma 5. ‣ 4.2 Esscher transform ‣ 4 Option Pricing ‣ The Variance Gamma Process for Option Pricing")) without the exponent t/νt/\nu so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(h)=1−ν​θ​h−ν​σ22​h21−ν​θ​(h+1)−ν​σ22​(h+1)2.H(h)=\dfrac{1-\nu\theta h-\nu\frac{\sigma^{2}}{2}h^{2}}{1-\nu\theta(h+1)-\nu\frac{\sigma^{2}}{2}(h+1)^{2}}. |  | (67) |

Then we find,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Hd​h​(h)=ν2​σ42​h2+θ​ν2​(σ22+θ)​h+θ​ν2​(σ22+θ)+ν​σ2(1−ν​θ​(h+1)−ν​σ22​(h+1)2)2,\frac{dH}{dh}(h)=\dfrac{\frac{\nu^{2}\sigma^{4}}{2}h^{2}+\theta\nu^{2}(\frac{\sigma^{2}}{2}+\theta)h+\theta\nu^{2}(\frac{\sigma^{2}}{2}+\theta)+\nu\sigma^{2}}{\left(1-\nu\theta(h+1)-\frac{\nu\sigma^{2}}{2}(h+1)^{2}\right)^{2}}, |  | (68) |

so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Hd​h​(h)>0,h1<h<h2−1,limh→h1g​(h)=0,limh→h2−1−g​(h)=+∞\frac{dH}{dh}(h)>0,h\_{1}<h<h\_{2}-1,\hskip 28.45274pt\lim\_{h\to h\_{1}}g(h)=0,\hskip 28.45274pt\lim\_{h\to h\_{2}-1^{-}}g(h)=+\infty |  | (69) |

so that HH is a bijection from (h1,h2−1)(h\_{1},h\_{2}-1) to ℝ+\mathbb{R^{+}} and there is a unique h∗h^{\*} which satisfies ([39](https://arxiv.org/html/2510.14093v1#S4.E39 "In Lemma 5. ‣ 4.2 Esscher transform ‣ 4 Option Pricing ‣ The Variance Gamma Process for Option Pricing")).

### 8.6 Proof of proposition [5](https://arxiv.org/html/2510.14093v1#Thmprop5 "Proposition 5. ‣ 4.2 Esscher transform ‣ 4 Option Pricing ‣ The Variance Gamma Process for Option Pricing")

Consider the inverse of the term inside the bracket in ([44](https://arxiv.org/html/2510.14093v1#S4.E44 "In 4.2 Esscher transform ‣ 4 Option Pricing ‣ The Variance Gamma Process for Option Pricing")) as suggested. Then the denominator becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1−ν​θ​(h+z)−ν​12​σ2​(h+z)21−ν​θ​h−ν​12​σ2​h2=1−ν​θ​h−ν​θ​z−ν​σ22​(h2+2​h​z+z2)1−ν​θ​h−ν​12​σ2​h2\dfrac{1-\nu\theta(h+z)-\nu\frac{1}{2}\sigma^{2}(h+z)^{2}}{1-\nu\theta h-\nu\frac{1}{2}\sigma^{2}h^{2}}=\dfrac{1-\nu\theta h-\nu\theta z-\nu\frac{\sigma^{2}}{2}(h^{2}+2hz+z^{2})}{1-\nu\theta h-\nu\frac{1}{2}\sigma^{2}h^{2}} |  | (70) |

which we may expand as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1−ν​θ​h−ν​σ22​h2−ν​(θ+h​σ2)​z−ν​σ22​z21−ν​θ​h−ν​12​σ2​h2=1−ν​(θ+h​σ2)​z−ν​σ22​z21−ν​θ​h−ν​12​σ2​h2\dfrac{1-\nu\theta h-\nu\frac{\sigma^{2}}{2}h^{2}-\nu(\theta+h\sigma^{2})z-\nu\frac{\sigma^{2}}{2}z^{2}}{1-\nu\theta h-\nu\frac{1}{2}\sigma^{2}h^{2}}=1-\dfrac{\nu(\theta+h\sigma^{2})z-\nu\frac{\sigma^{2}}{2}z^{2}}{1-\nu\theta h-\nu\frac{1}{2}\sigma^{2}h^{2}} |  | (71) |

rewriting the fraction gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1−ν1−ν​θ​h−ν​12​σ2​h2​(θ+h​σ2)​z−ν1−ν​θ​h−ν​12​σ2​h2​(σ22​z2)1-\dfrac{\nu}{{1-\nu\theta h-\nu\frac{1}{2}\sigma^{2}h^{2}}}(\theta+h\sigma^{2})z-\dfrac{\nu}{{1-\nu\theta h-\nu\frac{1}{2}\sigma^{2}h^{2}}}\left(\frac{\sigma^{2}}{2}z^{2}\right) |  | (72) |

so we can conclude by letting θ~,ν~\tilde{\theta},\tilde{\nu} be as given in the proposition.