---
authors:
- Òscar Burés
doc_id: arxiv:2510.15423v1
family_id: arxiv:2510.15423
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS
url_abs: http://arxiv.org/abs/2510.15423v1
url_html: https://arxiv.org/html/2510.15423v1
venue: arXiv q-fin
version: 1
year: 2025
---


Òscar Burés
Universitat de Barcelona, Departament de Matemàtica Econòmica, Financera i Actuarial.
  
Diagonal 690–696, 08034 Barcelona, Spain.

(October 17, 2025)

###### Abstract

In this paper we study the short-maturity asymptotics of up-and-in barrier options under a broad class of stochastic volatility models. Our approach uses Malliavin calculus techniques, typically used for linear stochastic partial differential equations, to analyse the law of the supremum of the log-price process. We derive a concentration inequality and explicit bounds on the density of the supremum in terms of the time to maturity. These results yield an upper bound on the asymptotic decay rate of up-and-in barrier option prices as maturity vanishes. We further demonstrate the applicability of our framework to the rough Bergomi model and validate the theoretical results with numerical experiments.

Keywords: barrier Options, Malliavin calculus, Stochastic volatility.

MSC Classification: 60G70; 60H07; 60H30; 91G20.

## 1 Introduction

A key problem in Quantitative Finance is the pricing of financial derivatives—contracts between a buyer and a seller whose value depends on an underlying asset. Among all types of derivatives, particular attention from both academics and practitioners has been drawn to options. These contracts give the holder the right, but not the obligation, to exercise the contract if market conditions at maturity are favourable.

There are several types of options, with European call and put options being among the most prominent. For these instruments, the price is typically computed as the expected value, under a risk-neutral probability measure, of the positive difference between the asset’s value at maturity and the strike price. Since these options depend only on the terminal value of the underlying asset, they allow for analytical pricing under simple modeling assumptions, such as the Black-Scholes framework.

However, real-world financial markets offer a much broader variety of options that are more complex to analyze. Among these are path-dependent options, whose payoff depends on the entire trajectory of the underlying asset up to maturity. Notable examples include Asian options, lookback options, Bermuda options, and barrier options—the latter being the focus of this article.

Barrier options are similar to European options in that their payoff structure is identical, but with the crucial distinction that the payoff is contingent upon the underlying asset reaching a predefined level, known as the barrier. Among barrier options, we distinguish between "In" options, which are activated only if the asset price hits the barrier during the contract’s life, and "Out" options, which are deactivated if the barrier is breached. In this article, we focus specifically on the asymptotic behaviour of up-and-in barrier call options, which are call options that can only be exercised if the asset price reaches a barrier level that lies above its initial value. We focus on up-and-in barrier options for two main reasons. The first one, since Malliavin calculus allows us to deal with the supremum of a stochastic process, we can apply those techniques to "up" barrier options (which depend on the maximum value of the stock price on a time window). Then, we choose to focus on up-and-in barrier options because, as we will show in the paper, the premium of these options tend to zero as the maturity attains small values regardless of the strike value. The asymptotic behaviour for up-and-out barrier options can be deduced combining the main result of this paper, Theorem [4.1](https://arxiv.org/html/2510.15423v1#S4.Thmteo1 "Theorem 4.1. ‣ 4 Main Result ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS") and the main result from Jafari et al., ([2025](https://arxiv.org/html/2510.15423v1#bib.bib16)).

Closed-form pricing formulas for up-and-in barrier call options exist under the Black-Scholes model. However, empirical evidence shows that the assumption of constant volatility is often insufficient to capture certain behaviors of the underlying asset, such as volatility clustering, leverage effects, or smile/skew phenomena as it is shown in e.g. Hull and White, ([1987](https://arxiv.org/html/2510.15423v1#bib.bib15)), Wiggins, ([1987](https://arxiv.org/html/2510.15423v1#bib.bib26)), Stein and Stein, ([1991](https://arxiv.org/html/2510.15423v1#bib.bib24)), and Heston, ([1993](https://arxiv.org/html/2510.15423v1#bib.bib13)). Moreover, the work of authors in Comte and Renault, ([1998](https://arxiv.org/html/2510.15423v1#bib.bib6)), Alòs et al., ([2007](https://arxiv.org/html/2510.15423v1#bib.bib1)), and Fukasawa, ([2017](https://arxiv.org/html/2510.15423v1#bib.bib11)), Gatheral et al., ([2018](https://arxiv.org/html/2510.15423v1#bib.bib12)) and Bayer et al., ([2016](https://arxiv.org/html/2510.15423v1#bib.bib3)) show that the asset price dynamics is more compatible with rough volatility models. When stochastic volatility is introduced, the analytical treatment of barrier options becomes considerably more challenging. Nevertheless, it is still possible to study the properties of such options using tools such as stochastic calculus, Malliavin calculus, and computational methods like Monte Carlo simulations. The research on barrier option focuses on their pricing and hedging (see, for instance Zvan et al., ([2000](https://arxiv.org/html/2510.15423v1#bib.bib27)), Brown et al., ([2001](https://arxiv.org/html/2510.15423v1#bib.bib4)) or Kou, ([2003](https://arxiv.org/html/2510.15423v1#bib.bib19))). Previous work on the asymptotic behavior of barrier options can be found in the literature. In Carrada-Herrera et al., ([2013](https://arxiv.org/html/2510.15423v1#bib.bib5)) the authors develop an expansion for double barrier options with constant volatility and discontinuities coming from a compound Poisson process. Regarding the analysis of the asymptotic behaviour under stochastic volatility, the work of the authors in Hu and Knessl, ([2010](https://arxiv.org/html/2510.15423v1#bib.bib14)) and Kato et al., ([2013](https://arxiv.org/html/2510.15423v1#bib.bib17)) provides asymptotic expansions of barrier options under specific stochastic volatility models such as the CEV or SABR volatility models.

The difficulty of analysing the supremum of a stochastic process that is not Gaussian makes it difficult to extend the papers previously cited to a general stochastic volatility framework. Using Malliavin calculus we are able to show that the probability of attaining the Barrier (and therefore, the price of an up-and-in Barrier call option) decays faster than any polynomial of the maturity.

In Jafari et al., ([2025](https://arxiv.org/html/2510.15423v1#bib.bib16)), it is shown that for European options in the out-of-the-money (OTM) and at-the-money (ATM) cases, the option price tends to zero as maturity T→0T\to 0, whereas in the in-the-money (ITM) case, the price tends to the difference between the initial asset price and the strike. Moreover, it is proven that this convergence rate is, at most, polynomial in TT. Since the exercise condition of an up-and-in barrier call option is more restrictive than that of a standard European call option, it follows that its price is always lower. Consequently, in the OTM and ATM cases, the price of an up-and-in barrier call option also vanishes as
T→0T\to 0. In this paper, we address the problem of determining the limit value of an ITM up-and-in barrier call option as maturity vanishes, and we further show that the rate at which this limit is reached is faster than any polynomial in TT, thus reaching its limit value in a faster rate as the observed for European options.

To study the asymptotic behaviour of up-and-in barrier call options, we employ Malliavin calculus to analyse the probability that the underlying asset hits the barrier. Specifically, we derive two types of bounds for this probability. The first is a direct bound on the probability that the supremum of the underlying process exceeds the barrier, using a concentration inequality. The second involves estimating the CDF of the supremum by first obtaining estimates of its density function. In both cases, the approach is far from straightforward. Indeed, the supremum of the underlying process does not satisfy the regularity conditions typically required to apply Malliavin-based concentration inequalities or density criteria.

To overcome this difficulty, we rely on the work of Nualart and Vives, ([1988](https://arxiv.org/html/2510.15423v1#bib.bib22)), which provides a framework for computing the Malliavin derivative of the supremum. This allows us to apply a suitable concentration inequality to our setting. Furthermore, we draw upon techniques similar to those in Florit and Nualart, ([1995](https://arxiv.org/html/2510.15423v1#bib.bib10)) to prove the existence of a density for the supremum and derive estimates for it. The problem of analysing the density of the supremum of a process has been previously studied in the context of solutions to stochastic differential equations—for instance, in Pu, ([2018](https://arxiv.org/html/2510.15423v1#bib.bib23)) or Dalang and Pu, ([2020](https://arxiv.org/html/2510.15423v1#bib.bib9)), where the authors derive density estimates for the supremum of the solution to the stochastic heat equation with additive noise. In our case, the noise is not additive, as we assume the presence of stochastic volatility. However, we manage to treat the problem in a way that is effectively equivalent to having additive noise, provided that the volatility process is not completely correlated with the driving noise of the stock price.

This paper is organized as follows. Section [2](https://arxiv.org/html/2510.15423v1#S2 "2 The Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS") introduces the model assumed for the underlying asset. Section [3](https://arxiv.org/html/2510.15423v1#S3 "3 Malliavin Calculus Tools ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS") presents the Malliavin calculus tools used to study the density of the asset price supremum over [0,T][0,T]. In Section [4](https://arxiv.org/html/2510.15423v1#S4 "4 Main Result ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS"), we state the main result: up-and-in barrier call option prices vanish as T→0T\to 0, with a convergence rate faster than any polynomial. Section [5](https://arxiv.org/html/2510.15423v1#S5 "5 Short-Time Behaviour Of An Up-And-In Barrier Call Option ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS") proves this limit by introducing an auxiliary random variable controlling the supremum, inspired by techniques from Florit and Nualart, ([1995](https://arxiv.org/html/2510.15423v1#bib.bib10)). Section [6](https://arxiv.org/html/2510.15423v1#S6 "6 A First Asymptotic Result ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS") provides a first estimate for the barrier-hitting probability using a concentration inequality, for which we verify the required Malliavin differentiability conditions as in Nourdin and Viens, ([2009](https://arxiv.org/html/2510.15423v1#bib.bib20)) using techniques similar to the ones in Nualart and Vives, ([1988](https://arxiv.org/html/2510.15423v1#bib.bib22)). In Section [7](https://arxiv.org/html/2510.15423v1#S7 "7 Estimation Of The Density Of 𝑀_𝑇 ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS"), we prove the existence of a density for the supremum using a local criterion, derive estimates for it, and obtain a bound for its CDF—confirming the faster-than-polynomial decay. Finally, Section [8](https://arxiv.org/html/2510.15423v1#S8 "8 Application To The Rough Bergomi Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS") applies our results to the Rough Bergomi model, illustrating the decay rate both theoretically and numerically.

## 2 The Model

We assume the following model for the log-price process, under a risk-neutral measure given by the market and under the assumption of null interest rate r=0r=0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=x−12​∫0tσs2​𝑑s+∫0tσs​(ρ​d​Ws+1−ρ2​d​Bs),t∈[0,T],\displaystyle X\_{t}=x-\frac{1}{2}\int^{t}\_{0}\sigma^{2}\_{s}ds+\int^{t}\_{0}\sigma\_{s}(\rho dW\_{s}+\sqrt{1-\rho^{2}}dB\_{s}),\,\,t\in[0,T], |  | (2.1) |

where X0X\_{0} is the current log price, WW and BB are independent standard Brownian motions and ρ∈(−1,1)\rho\in(-1,1). The volatility process σ\sigma is assumed to be a square-integrable process, adapted to the filtration generated by WW. Throughout the paper we will use the notation Z:=ρ​W+1−ρ2​BZ:=\rho W+\sqrt{1-\rho^{2}}B, so Model ([2.1](https://arxiv.org/html/2510.15423v1#S2.E1 "In 2 The Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS")) can also be written as

|  |  |  |
| --- | --- | --- |
|  | Xt=x−12​∫0tσs2​𝑑s+∫0tσs​𝑑Zs,t∈[0,T].X\_{t}=x-\frac{1}{2}\int^{t}\_{0}\sigma^{2}\_{s}ds+\int^{t}\_{0}\sigma\_{s}dZ\_{s},\,\,t\in[0,T]. |  |

We denote by 𝔽W={ℱtW;t∈[0,T]}{\mathbb{F}}^{W}=\{\mathcal{F}\_{t}^{W};t\in[0,T]\} and 𝔽B={ℱtB;t∈[0,T]}{\mathbb{F}}^{B}=\{\mathcal{F}^{B}\_{t};t\in[0,T]\} the natural filtrations generated by the independent processes WW, BB. Moreover, we denote by 𝔽={ℱt;t∈[0,T]}\mathbb{F}=\{\mathcal{F}\_{t};t\in[0,T]\} the filtration generated by both WW and BB, that is, ℱt=ℱtW∨ℱtB\mathcal{F}\_{t}=\mathcal{F}^{W}\_{t}\vee\mathcal{F}^{B}\_{t} for all t∈[0,T]t\in[0,T]. It is well known that the pricing formula for a European call option with a strike price KK under Model ([2.1](https://arxiv.org/html/2510.15423v1#S2.E1 "In 2 The Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS")) is given by

|  |  |  |
| --- | --- | --- |
|  | Ct=E​[(eXT−K)+|ℱt].C\_{t}=E\left[(e^{X\_{T}}-K)\_{+}|{\cal F}\_{t}\right]. |  |

Given a real number B>S0B>S\_{0}, an up-and-in barrier call option with underlying asset SS, strike KK, maturity TT and barrier BB is a financial derivative with payoff (ST−K)+​𝟏{supt∈[0,T]St≥B}(S\_{T}-K)\_{+}\mathbf{1}\_{\{\sup\_{t\in[0,T]}S\_{t}\geq B\}}. In other words, the price of an up-and-in barrier call option under this configuration at time t=0t=0 is given by

|  |  |  |
| --- | --- | --- |
|  | C0b=𝔼​[(ST−K)+​𝟏{supt∈[0,T]St≥B}].C\_{0}^{b}=\mathbb{E}\left[(S\_{T}-K)\_{+}\mathbf{1}\_{\{\sup\_{t\in[0,T]}S\_{t}\geq B\}}\right]. |  |

We are interested in the short-time behaviour of C0bC\_{0}^{b}, so we can assume without loss of generality that T≤1T\leq 1. Since St=exp⁡(Xt)S\_{t}=\exp(X\_{t}) and the exponential function is increasing, we can rewrite the premium of the barrier option in terms of the log-price. I.e. the price of such barrier option at time t=0t=0 can be written as

|  |  |  |
| --- | --- | --- |
|  | C0b=𝔼​[(eXT−K)+​𝟏{MT≥b}],MT=supt∈[0,T]Xt,b=log⁡B.C\_{0}^{b}=\mathbb{E}\left[(e^{X\_{T}}-K)\_{+}\mathbf{1}\_{\{M\_{T}\geq b\}}\right],\quad M\_{T}=\sup\_{t\in[0,T]}X\_{t},\quad b=\log B. |  |

From the fact that 0≤𝟏{MT≥b}≤10\leq\mathbf{1}\_{\{M\_{T}\geq b\}}\leq 1 it is clear that C0b≤C0C^{b}\_{0}\leq C\_{0}. This also can be interpreted in a financial sense: since the conditions for an up-and-in barrier call option to be exercised are more restrictive than the conditions for an European call option, one potentially gets more benefit from the European call option than from the barrier option, so the European call option must be more expensive. Notice that a simple application of Hölder’s inequality shows that

|  |  |  |
| --- | --- | --- |
|  | C0b≤‖(ST−K)+‖Lp​(Ω)​ℙ​(MT≥b)1/q,1p+1q=1.C\_{0}^{b}\leq||(S\_{T}-K)\_{+}||\_{L^{p}(\Omega)}\mathbb{P}\left(M\_{T}\geq b\right)^{1/q},\quad\frac{1}{p}+\frac{1}{q}=1. |  |

So, if we manage to prove that limT→0C0b=0\lim\_{T\to 0}C\_{0}^{b}=0, then, an analysis of the speed of convergence of the term ℙ​(MT≥b)\mathbb{P}\left(M\_{T}\geq b\right) to zero will give us an upper bound for speed of convergence of C0bC\_{0}^{b} to zero. Hence, the objectives of this paper are the following:

* •

  Show that limT→0C0b=0\lim\_{T\to 0}C\_{0}^{b}=0.
* •

  Using a concentration inequality we will show an a-priori upper bound for ℙ​(MT≥b)\mathbb{P}(M\_{T}\geq b).
* •

  Using more involved Malliavin calculus techniques, we will give an upper bound for the density function of MTM\_{T} in order to estimate the cummulative distribution function of MTM\_{T} and derive and alternative upper bound for ℙ​(MT≥b)\mathbb{P}(M\_{T}\geq b).

## 3 Malliavin Calculus Tools

In this section we will introduce all the notions from Malliavin Calculus needed in order to cover the problem of estimating the law of the supremum of a stochastic process of the form ([2.1](https://arxiv.org/html/2510.15423v1#S2.E1 "In 2 The Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS")). Let ℋ=L2​([0,T])\mathcal{H}=L^{2}([0,T]) and let B:={B​(h);h∈ℋ}B:=\{B(h);h\in\mathcal{H}\} the associated isonormal Gaussian process. We denote by 𝒮\mathcal{S} the class of smooth random variables of the form

|  |  |  |
| --- | --- | --- |
|  | F=f​(B​(h1),…,B​(hn))F=f(B(h\_{1}),\dots,B(h\_{n})) |  |

where hi∈ℋh\_{i}\in\mathcal{H} for all i∈{1,…,n}i\in\{1,\dots,n\} and f∈𝒞b∞​(ℝn)f\in\mathcal{C}^{\infty}\_{b}(\mathbb{R}^{n}). Given a random variable F∈𝒮F\in\mathcal{S}, we define the Malliavin derivative of FF as the ℋ\mathcal{H}-valued stochastic process D​F={Dt​F;t∈[0,T]}DF=\{D\_{t}F;t\in[0,T]\} where

|  |  |  |
| --- | --- | --- |
|  | Dt​F=∑i=1n∂if​(B​(h1),…,B​(hn))​hi​(t).D\_{t}F=\sum\_{i=1}^{n}\partial\_{i}f(B(h\_{1}),\dots,B(h\_{n}))h\_{i}(t). |  |

We can also define higher order derivatives in a similar manner. Indeed, for any natural number k≥1k\geq 1 we define the kk-th order Malliavin derivative of FF as the ℋ⊗k\mathcal{H}^{\otimes k}-valued stochastic process Dk​F={Dz​F;z∈[0,T]k}D^{k}F=\{D\_{z}F;z\in[0,T]^{k}\} where

|  |  |  |
| --- | --- | --- |
|  | Dzk​F=∑i=1n∂∂z1​⋯​∂∂zk​f​(B​(h1),…,B​(hn))​(h1⊗⋯⊗hk)​(z),z=(z1,…,zk).D^{k}\_{z}F=\sum\_{i=1}^{n}\frac{\partial}{\partial z\_{1}}\cdots\frac{\partial}{\partial z\_{k}}f(B(h\_{1}),\dots,B(h\_{n}))(h\_{1}\otimes\cdots\otimes h\_{k})(z),\quad z=(z\_{1},\dots,z\_{k}). |  |

It is well known that the operators DkD^{k} are closable from Lp​(Ω)L^{p}(\Omega) to Lp​(Ω;ℋ⊗k)L^{p}(\Omega;\mathcal{H}^{\otimes k}) for all p≥1p\geq 1, k≥1k\geq 1. This allows to define the spaces 𝔻k,p\mathbb{D}^{k,p} as the closure of 𝒮\mathcal{S} with respect to the semi-norm ||⋅||k,p||\cdot||\_{k,p} defined by

|  |  |  |
| --- | --- | --- |
|  | ‖F‖k,p={𝔼​[|F|p]+∑j=1k𝔼​[‖D​F‖ℋ⊗jp]}1/p.||F||\_{k,p}=\left\{\mathbb{E}[|F|^{p}]+\sum\_{j=1}^{k}\mathbb{E}[||DF||\_{\mathcal{H}^{\otimes j}}^{p}]\right\}^{1/p}. |  |

We define also 𝔻∞:=⋂k≥1⋂p≥1𝔻k,p\mathbb{D}^{\infty}:=\bigcap\_{k\geq 1}\bigcap\_{p\geq 1}\mathbb{D}^{k,p}.

The Malliavin derivative DD on the space L2​(Ω)L^{2}(\Omega) has an adjoint operator called the divergence operator or Skorohod integral and it is represented by δ\delta. For any process u∈L2​(Ω;ℋ)u\in L^{2}(\Omega;\mathcal{H}), the element δ​(u)\delta(u) is uniquely determined by the duality relationship

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[F​δ​(u)]=𝔼​[∫0TDt​F⋅ut​𝑑t], for all ​F∈𝔻1,2.\mathbb{E}[F\delta(u)]=\mathbb{E}\left[\int\_{0}^{T}D\_{t}F\cdot u\_{t}dt\right],\quad\text{ for all }F\in\mathbb{D}^{1,2}. |  |

Among all the properties of the Skorohod integral, we will be using the following relationship in Section [7](https://arxiv.org/html/2510.15423v1#S7 "7 Estimation Of The Density Of 𝑀_𝑇 ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS").

###### Proposition 3.1.

Let F∈𝔻1,2F\in\mathbb{D}^{1,2} and let u∈Dom⁡(δ)u\in\operatorname{Dom}(\delta). Then,

|  |  |  |
| --- | --- | --- |
|  | δ​(F​u)=F​δ​(u)−⟨D​F,u⟩,\delta(Fu)=F\delta(u)-\langle DF,u\rangle, |  |

where ⟨⋅,⋅⟩\langle\cdot,\cdot\rangle denotes the usual scalar product in L2​([0,T])L^{2}([0,T]).

One of the main applications of the Malliavin calculus to probability theory is the existence of criteria for checking the absolute continuity of the law of random variables and deciding whether the density function of FF is smooth. The most classical criterion in order to prove that the density of a random vector is smooth is the following.

###### Theorem 3.2.

Let F=(F1,…,Fd)F=(F\_{1},\dots,F\_{d}) be a random vector whose components are in 𝔻∞\mathbb{D}^{\infty}. Assume that the Malliavin matrix γi,j:=⟨D​Fi,D​Fj⟩\gamma\_{i,j}:=\langle DF^{i},DF^{j}\rangle satisfies |detγ|−1∈Lp​(Ω)|\det\gamma|^{-1}\in L^{p}(\Omega) for all p≥1p\geq 1. Then, the random vector FF is absolutely continuous with respect to the Lebesgue measure and FF possesses an infinitely differentiable density.

###### Proof.

See Nualart, ([2006](https://arxiv.org/html/2510.15423v1#bib.bib21)).
∎

This result is widely applied in the study of the density of solutions to SDEs and SPDEs since, under the assumption that the coefficients of the differential equations are infinitely many times differentiable, one can prove in most cases that the solution belongs to 𝔻∞\mathbb{D}^{\infty} and under ellipticity conditions on the diffusion coefficient one can check that the determinant of the inverse of the Malliavin matrix has moments of all orders, concluding that the density of the solution is smooth.

In this paper, we study the supremum of the stock price process SS over the time interval [0,T][0,T]. It is well known that the functional

|  |  |  |
| --- | --- | --- |
|  | MT:=supt∈[0,T]XtM\_{T}:=\sup\_{t\in[0,T]}X\_{t} |  |

belongs to 𝔻1,2\mathbb{D}^{1,2}, but does not exhibit higher regularity. Although MTM\_{T} lacks the smoothness required to directly apply the previously stated criterion, a localized version of the result is available and well-suited for this setting.

###### Theorem 3.3.

Let F=(F1,…,Fd)F=(F^{1},\dots,F^{d}) be a random vector whose components are in 𝔻1,2\mathbb{D}^{1,2}. Let AA be an open set of ℝd\mathbb{R}^{d}. Assume that there exist ℋ\mathcal{H}-valued random variables uAu\_{A} and a d×dd\times d random matrix γA=(γi,j)1≤i,j≤d\gamma\_{A}=(\gamma\_{i,j})\_{1\leq i,j\leq d} such that

* 1.

  uAj∈𝔻∞​(ℋ)u^{j}\_{A}\in\mathbb{D}^{\infty}(\mathcal{H}) for all j∈{1,…,d}j\in\{1,\dots,d\}.
* 2.

  γi,j∈𝔻∞\gamma\_{i,j}\in\mathbb{D}^{\infty} for all (i,j)∈{1,…,d}2(i,j)\in\{1,\dots,d\}^{2} and |detγA|−1∈Lp​(Ω)|\det\gamma\_{A}|^{-1}\in L^{p}(\Omega) for all p≥1p\geq 1.
* 3.

  ⟨D​Fi,uAj⟩=γAi,j\langle DF^{i},u\_{A}^{j}\rangle=\gamma\_{A}^{i,j} on the set {F∈A}\{F\in A\} for all (i,j)∈{1,…,d}2(i,j)\in\{1,\dots,d\}^{2}.

Then, the random vector FF possesses an infinitely differentiable density on the open set AA.

###### Proof.

See Florit and Nualart, ([1995](https://arxiv.org/html/2510.15423v1#bib.bib10)).
∎

## 4 Main Result

In this section we will state the main result of this paper, which describes the short-time behaviour of the price of an up-and-in barrier call option. The following assumptions for the volatility process σ\sigma are needed.

###### Hypothesis 1.

There exist 0<α<β0<\alpha<\beta such that

|  |  |  |
| --- | --- | --- |
|  | α≤σt≤β\alpha\leq\sigma\_{t}\leq\beta |  |

for almost every t∈[0,T]t\in[0,T].

###### Hypothesis 2.

For all p≥2p\geq 2, σ∈𝕃W1,p\sigma\in\mathbb{L}^{1,p}\_{W}.

From now on, we will assume that the volatility process always satisfies Hypotheses ([1](https://arxiv.org/html/2510.15423v1#Thmhyp1 "Hypothesis 1. ‣ 4 Main Result ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS")) and ([2](https://arxiv.org/html/2510.15423v1#Thmhyp2 "Hypothesis 2. ‣ 4 Main Result ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS")). Hence, when we assume that XX follows Model ([2.1](https://arxiv.org/html/2510.15423v1#S2.E1 "In 2 The Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS")) we are also implying the previous hypotheses on the volatility process.

In the present work, we apply Malliavin calculus techniques in order to understand the asymptotic behaviour of the probability that the barrier is achieved in order to give an upper bound for the asymptotic behaviour of C0bC\_{0}^{b}. The main result is stated as follows.

###### Theorem 4.1.

Let XX be the log-price of an asset SS with dynamics given by ([2.1](https://arxiv.org/html/2510.15423v1#S2.E1 "In 2 The Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS")). Let B>S0B>S\_{0} and let KK be the strike price. Then, an up-and-in barrier call option of the form

|  |  |  |
| --- | --- | --- |
|  | C0b=𝔼​[(ST−K)+​𝟏{supt∈[0,T]St≥B}]C\_{0}^{b}=\mathbb{E}\left[(S\_{T}-K)\_{+}\mathbf{1}\_{\{\sup\_{t\in[0,T]}S\_{t}\geq B\}}\right] |  |

exhibits the following short-time behaviour:

* (i)

  limT→0C0b=0\lim\_{T\to 0}C\_{0}^{b}=0.
* (ii)

  There exists T0>0T\_{0}>0 and constants c1,c2,c3>0c\_{1},c\_{2},c\_{3}>0 such that the probability of reaching the barrier satisfies

  |  |  |  |
  | --- | --- | --- |
  |  | ℙ​(supt∈[0,T]St≥B)≤min⁡{exp⁡(−(b−x)2c1​T),∫b∞c2T​exp⁡(−(z−x)22​c3​T)​𝑑z}\mathbb{P}\left(\sup\_{t\in[0,T]}S\_{t}\geq B\right)\leq\min\left\{\exp\left(-\frac{(b-x)^{2}}{c\_{1}T}\right),\int\_{b}^{\infty}\frac{c\_{2}}{\sqrt{T}}\exp\left(-\frac{(z-x)^{2}}{2c\_{3}T}\right)dz\right\} |  |

  for T≤T0T\leq T\_{0}.

In particular, C0b=o​(Tα)C\_{0}^{b}=o(T^{\alpha}) for every α>0\alpha>0.

Observe that Theorem [4.1](https://arxiv.org/html/2510.15423v1#S4.Thmteo1 "Theorem 4.1. ‣ 4 Main Result ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS") states that the price of an up-and-in barrier option decays faster than any polynomial as T→0T\to 0. In Jafari et al., ([2025](https://arxiv.org/html/2510.15423v1#bib.bib16)), one can deduce that the price of a European call option tends to zero at least at a polynomial speed depending on HH. In this paper we explicitly prove that up-and-in barrier options tend to zero faster than any polynomial.

From now on, we will use CC to denote a positive real constant not depending on TT that may differ from line to line but its specific value is not important for the main conclusion of this article.

## 5 Short-Time Behaviour Of An Up-And-In Barrier Call Option

In this section we aim to cover the first of the objectives regarding the study of the asymptotic behaviour of an up-and-in barrier call option. We will follow closely the ideas in Dalang and Pu, ([2020](https://arxiv.org/html/2510.15423v1#bib.bib9)) and we adapt them for a process of the form ([2.1](https://arxiv.org/html/2510.15423v1#S2.E1 "In 2 The Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS")). We follow the arguments from Nualart and Vives, ([1988](https://arxiv.org/html/2510.15423v1#bib.bib22)), Florit and Nualart, ([1995](https://arxiv.org/html/2510.15423v1#bib.bib10)) and Nualart, ([2006](https://arxiv.org/html/2510.15423v1#bib.bib21)). The strategy is based on the fact that even it is not true that supt∈[0,T]Xt∈𝔻∞\sup\_{t\in[0,T]}X\_{t}\in\mathbb{D}^{\infty}, there exist a random variable defined via the Hölder norm of XX that belongs to 𝔻∞\mathbb{D}^{\infty} and controls supt∈[0,T]Xt\sup\_{t\in[0,T]}X\_{t}. We will rely on this random variable to show that limT→0ℙ​(MT≥b)=0\lim\_{T\to 0}\mathbb{P}(M\_{T}\geq b)=0 and conclude from there that limT→0C0b=0\lim\_{T\to 0}C\_{0}^{b}=0. Then, once we know that every up-and-in barrier call option tends to zero, we can focus on the speed of convergence.

In order to prove the first objective, that is, proving that limT→0ℙ​(MT≥b)=0\lim\_{T\to 0}\mathbb{P}(M\_{T}\geq b)=0 we need to know the Hölder regularity of the sample paths of XtX\_{t} in order to define the auxiliary random variables controlling the supremum of XX. The regularity of the paths of XX can be easily derived applying Kolmogorov’s continuity criterion, as it is shown in the following result.

###### Lemma 5.1.

Let XX be defined as in ([2.1](https://arxiv.org/html/2510.15423v1#S2.E1 "In 2 The Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS")). The sample paths of XX are γ\gamma-Hölder continuous for γ∈(0,12)\gamma\in\left(0,\frac{1}{2}\right). In particular, for every p≥1p\geq 1 there exists a constant Cp>0C\_{p}>0 not depending on TT such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|Xt−Xs|p]≤Cp​|t−s|p/2\mathbb{E}[|X\_{t}-X\_{s}|^{p}]\leq C\_{p}|t-s|^{p/2} |  |

###### Proof.

Notice that, since σ\sigma is a process with continuous sample paths, the map

|  |  |  |
| --- | --- | --- |
|  | t↦−12​∫0tσs2​𝑑st\mapsto-\frac{1}{2}\int\_{0}^{t}\sigma\_{s}^{2}ds |  |

is indeed 𝒞1​([0,T])\mathcal{C}^{1}([0,T]) almost surely. Moreover,

|  |  |  |
| --- | --- | --- |
|  | |12​∫stσu2​𝑑u|p≤C​|t−s|p≤C​|t−s|p/2\left|\frac{1}{2}\int\_{s}^{t}\sigma\_{u}^{2}du\right|^{p}\leq C|t-s|^{p}\leq C|t-s|^{p/2} |  |

because T≤1T\leq 1. Hence, the Hölder continuity of the paths of XX is inherited from the Hölder continuity of the paths of

|  |  |  |
| --- | --- | --- |
|  | ∫0tσs​𝑑Zs.\int\_{0}^{t}\sigma\_{s}dZ\_{s}. |  |

Now, Burkholder’s inequality shows that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|∫stσu​𝑑Zu|p]≤cp​𝔼​[(∫stσu2​𝑑u)p/2]≤c​|t−s|p/2.\mathbb{E}\left[\left|\int\_{s}^{t}\sigma\_{u}dZ\_{u}\right|^{p}\right]\leq c\_{p}\mathbb{E}\left[\left(\int\_{s}^{t}\sigma\_{u}^{2}du\right)^{p/2}\right]\leq c|t-s|^{p/2}. |  |

Kolmogorov’s continuity criterion shows that the sample paths of the stochastic integral of σ\sigma with respect to ZZ are of γ\gamma-Hölder continuous with γ∈(0,12−1p)\gamma\in\left(0,\frac{1}{2}-\frac{1}{p}\right) for all p≥1p\geq 1. Letting p→∞p\to\infty we conclude the result.
∎

Notice that up to this point, one can show that limT→0ℙ​(MT≥b)=0\lim\_{T\to 0}\mathbb{P}(M\_{T}\geq b)=0 using a continuity argument. Nevertheless, since the definition of the auxiliary random variables controlling MTM\_{T} is not only useful to prove that limT→0ℙ​(MT≥b)=0\lim\_{T\to 0}\mathbb{P}(M\_{T}\geq b)=0 but it is also key in the estimation of the density of MTM\_{T} we will prove that limT→0ℙ​(MT≥b)=0\lim\_{T\to 0}\mathbb{P}(M\_{T}\geq b)=0 in a more involved way that uses the Hölder norm of XX. The definition of the random variable that controls MTM\_{T} is the following.

###### Definition 5.2.

Consider p0∈ℕp\_{0}\in\mathbb{N} and let γ0∈ℝ\gamma\_{0}\in\mathbb{R} such that p0−2>γ0>4p\_{0}-2>\gamma\_{0}>4. We define Y={Yr;r∈[0,T]}Y=\{Y\_{r};r\in[0,T]\} as

|  |  |  |
| --- | --- | --- |
|  | Yr:=∫[0,r]2(Xt−Xs)2​p0|t−s|γ0​𝑑t​𝑑s.Y\_{r}:=\int\_{[0,r]^{2}}\frac{(X\_{t}-X\_{s})^{2p\_{0}}}{|t-s|^{\gamma\_{0}}}dtds. |  |

Before discussing the relation between YY and MTM\_{T} we shall check that indeed the process YY is well defined.

###### Lemma 5.3.

For any r∈[0,T]r\in[0,T], Yr∈⋂p≥1Lp​(Ω)Y\_{r}\in\bigcap\_{p\geq 1}L^{p}(\Omega). In particular, for every p≥1p\geq 1 there exists a constant C>0C>0 not depending on TT such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|Yr|p]≤C​r2​p​T(p0−γ0)​p.\mathbb{E}[|Y\_{r}|^{p}]\leq Cr^{2p}T^{(p\_{0}-\gamma\_{0})p}. |  |

###### Proof.

Hölder’s inequality applied to p≥1p\geq 1 shows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|Yr|p]≤\displaystyle\mathbb{E}[|Y\_{r}|^{p}]\leq | r2​(p−1)​∫[0,r]2𝔼[|(Xt−Xs)2​p0​p]|t−s|γ0​p​𝑑t​𝑑s\displaystyle r^{2(p-1)}\int\_{[0,r]^{2}}\frac{\mathbb{E}[|(X\_{t}-X\_{s})^{2p\_{0}p}]}{|t-s|^{\gamma\_{0}p}}dtds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​r2​(p−1)​∫[0,r]2|t−s|p0​p|t−s|γ0​p​𝑑t​𝑑s\displaystyle Cr^{2(p-1)}\int\_{[0,r]^{2}}\frac{|t-s|^{p\_{0}p}}{|t-s|^{\gamma\_{0}p}}dtds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​r2​p​T(p0−γ0)​p,\displaystyle Cr^{2p}T^{(p\_{0}-\gamma\_{0})p}, |  |

as desired.
∎

The relation between the process YY and the supremum of XX relies on the fact that the cumulative distribution function of YTY\_{T} is bounded by the cumulative distribution function of MTM\_{T}. Moreover, since YTY\_{T} is more regular than MTM\_{T}, it is easier to deduce properties on YTY\_{T} and transfer them to MTM\_{T}. The relation between the cumulative distribution function of both random variables is a consequence of the Garsia-Rodemich-Rumsey lemma.

###### Proposition 5.4.

For every β>0\beta>0 there exists a constant C>0C>0 such that if

|  |  |  |
| --- | --- | --- |
|  | Yr≤C​β2​p0​T4−γ02,Y\_{r}\leq C\beta^{2p\_{0}}T^{\frac{4-\gamma\_{0}}{2}}, |  |

then

|  |  |  |
| --- | --- | --- |
|  | supt∈[0,r]|Xt−x|≤β.\sup\_{t\in[0,r]}|X\_{t}-x|\leq\beta. |  |

###### Proof.

We apply the Garsia-Rodemich-Rumsey lemma as in (Nualart,, [2006](https://arxiv.org/html/2510.15423v1#bib.bib21), Lemma A.3.1) or ([Dalang et al., 2009b,](https://arxiv.org/html/2510.15423v1#bib.bib8) , Proposition A.1) with the following configuration

|  |  |  |
| --- | --- | --- |
|  | S=[0,r],ρ​(t,s)=|t−s|1/2,μ​(d​t)=d​t\displaystyle S=[0,r],\quad\rho(t,s)=|t-s|^{1/2},\quad\mu(dt)=dt |  |
|  |  |  |
| --- | --- | --- |
|  | Ψ​(x)=x2​p0,p​(x)=xγ0/2​p0,f=X\displaystyle\Psi(x)=x^{2p\_{0}},\quad p(x)=x^{\gamma\_{0}/2p\_{0}},\quad f=X |  |

in order to obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Xt−Xs|≤\displaystyle|X\_{t}-X\_{s}|\leq | 8​supx∈[0,r]∫02​ρ​(t,s)Ψ−1​(Yrμ​(Bρ​(x,u/2))2)​p​(d​u)\displaystyle 8\sup\_{x\in[0,r]}\int\_{0}^{2\rho(t,s)}\Psi^{-1}\left(\frac{Y\_{r}}{\mu(B\_{\rho}(x,u/2))^{2}}\right)p(du) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 8​∫02​ρ​(t,s)Y1/2​p0μ​(Bρ​(s,u/2))2/p0​uγ02​p0−1​𝑑u\displaystyle 8\int\_{0}^{2\rho(t,s)}\frac{Y^{1/2p\_{0}}}{\mu(B\_{\rho}(s,u/2))^{2/p\_{0}}}u^{\frac{\gamma\_{0}}{2p\_{0}}-1}du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​Yr12​p0​∫02​ρ​(t,s)u−2p0​uγ02​p0−1​𝑑u\displaystyle CY\_{r}^{\frac{1}{2p\_{0}}}\int\_{0}^{2\rho(t,s)}u^{\frac{-2}{p\_{0}}}u^{\frac{\gamma\_{0}}{2p\_{0}}-1}du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​Yr12​p0​|t−s|γ0−44​p0.\displaystyle CY\_{r}^{\frac{1}{2p\_{0}}}|t-s|^{\frac{\gamma\_{0}-4}{4p\_{0}}}. |  |

Therefore, if we let Yr≤C−2​p0​β2​p0​T4−γ02Y\_{r}\leq C^{-2p\_{0}}{\beta}^{2p\_{0}}T^{\frac{4-\gamma\_{0}}{2}} then

|  |  |  |
| --- | --- | --- |
|  | |Xt−Xs|≤C⋅C−1​β​T4−γ04​p0​|t−s|γ0−44​p0≤β.|X\_{t}-X\_{s}|\leq C\cdot C^{-1}\beta T^{\frac{4-\gamma\_{0}}{4p\_{0}}}|t-s|^{\frac{\gamma\_{0}-4}{4p\_{0}}}\leq\beta. |  |

The result now follows from taking s=0s=0 and supremums on both sides of the previous inequality.
∎

We can also deduce the following immediate consequence.

###### Corollary 5.5.

For every β>x\beta>x there exists a constant C>0C>0 such that if

|  |  |  |
| --- | --- | --- |
|  | Yr≤RT​(β):=C​(β−x)2​p0​T4−γ02Y\_{r}\leq R\_{T}(\beta):=C(\beta-x)^{2p\_{0}}T^{\frac{4-\gamma\_{0}}{2}} |  |

then

|  |  |  |
| --- | --- | --- |
|  | supt∈[0,r]Xt≤β.\sup\_{t\in[0,r]}X\_{t}\leq\beta. |  |

###### Proof.

Let C>0C>0 the constant such that if Yr≤C​(β−x)2​p0​T4−γ02Y\_{r}\leq C(\beta-x)^{2p\_{0}}T^{\frac{4-\gamma\_{0}}{2}} then supt∈[0,r]|Xt−x|≤β−x\sup\_{t\in[0,r]}|X\_{t}-x|\leq\beta-x. Its existence is ensured by the previous proposition. Now, if Yr≤C​(β−x)2​p0​T4−γ02Y\_{r}\leq C(\beta-x)^{2p\_{0}}T^{\frac{4-\gamma\_{0}}{2}} then supt∈[0,r]Xt≤β\sup\_{t\in[0,r]}X\_{t}\leq\beta as claimed.
∎

The dynamics of both XX and MTM\_{T} are hard to study, however, the sample paths of YY are monotonically increasing. This, together with Corollary [5.5](https://arxiv.org/html/2510.15423v1#S5.Thmteo5 "Corollary 5.5. ‣ 5 Short-Time Behaviour Of An Up-And-In Barrier Call Option ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS") allows us to find the limit as the maturity tends to zero of an up-and-in barrier call option.

###### Proposition 5.6.

Let C0bC\_{0}^{b} a an up-and-in barrier call option with underlying SS, strike KK, maturity TT and barrier B>S0B>S\_{0}. Then,

|  |  |  |
| --- | --- | --- |
|  | limT→0C0b=0.\lim\_{T\to 0}C\_{0}^{b}=0. |  |

###### Proof.

On the one hand, if the associated European call option is Out-The-Money (OTM) then, its premium C0C\_{0} tends to zero as TT tends to zero and therefore the result is deduced from the fact that C0b≤C0C\_{0}^{b}\leq C\_{0}. For the ATM and ITM cases we will study ℙ​(MT≥b)\mathbb{P}(M\_{T}\geq b) where b=log⁡Bb=\log B denotes the log-barrier. On the one hand, Corollary [5.5](https://arxiv.org/html/2510.15423v1#S5.Thmteo5 "Corollary 5.5. ‣ 5 Short-Time Behaviour Of An Up-And-In Barrier Call Option ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS") shows that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(MT≥b)≤ℙ​(YT≥RT)=ℙ​(YT−RT≥0).\mathbb{P}(M\_{T}\geq b)\leq\mathbb{P}(Y\_{T}\geq R\_{T})=\mathbb{P}(Y\_{T}-R\_{T}\geq 0). |  |

On the one hand, the sample paths of YY are continuous and monotonically decreasing with Y0=0Y\_{0}=0. On the other hand, since RT​(b)=C​(b−x)2​p0​T4−γ02R\_{T}(b)=C(b-x)^{2p\_{0}}T^{\frac{4-\gamma\_{0}}{2}} then it holds that RT​(b)→∞R\_{T}(b)\to\infty as T→0T\to 0. Hence, limT→0YT−RT​(b)=−∞\lim\_{T\to 0}Y\_{T}-R\_{T}(b)=-\infty almost surely (and therefore, the limit also holds in probability) concluding that

|  |  |  |
| --- | --- | --- |
|  | limT→0ℙ​(YT≥RT)=0.\lim\_{T\to 0}\mathbb{P}(Y\_{T}\geq R\_{T})=0. |  |

Consider now the random variable 𝟏{MT≥b}\mathbf{1}\_{\{M\_{T}\geq b\}}. Since ℙ​(MT≥b)→0\mathbb{P}(M\_{T}\geq b)\to 0 then 𝟏{MT≥b}→0\mathbf{1}\_{\{M\_{T}\geq b\}}\to 0 in L1​(Ω)L^{1}(\Omega). Thus, 𝟏{MT≥b}→0\mathbf{1}\_{\{M\_{T}\geq b\}}\to 0 in probability. Moreover, since MTM\_{T} is increasing in TT, one has that for T1≤T2T\_{1}\leq T\_{2}

|  |  |  |
| --- | --- | --- |
|  | 𝟏{MT1≥b}≤𝟏{MT2≥b}\mathbf{1}\_{\{M\_{T\_{1}}\geq b\}}\leq\mathbf{1}\_{\{M\_{T\_{2}}\geq b\}} |  |

so the sequence of random variables 𝟏{MT≥b}\mathbf{1}\_{\{M\_{T}\geq b\}} is decreasing as T→0T\to 0. Thus, the convergence 𝟏{MT≥b}→0\mathbf{1}\_{\{M\_{T}\geq b\}}\to 0 also holds almost surely. Since (ST−K)+∈L1​(Ω)(S\_{T}-K)\_{+}\in L^{1}(\Omega) and (ST−K)+​𝟏{MT≥b}→0(S\_{T}-K)\_{+}\mathbf{1}\_{\{M\_{T}\geq b\}}\to 0 almost surely we can conclude by the dominated convergence theorem that

|  |  |  |
| --- | --- | --- |
|  | limT→0𝔼​[(ST−K)+​𝟏{MT≥b}]=limT→0C0b=0\lim\_{T\to 0}\mathbb{E}[(S\_{T}-K)\_{+}\mathbf{1}\_{\{M\_{T}\geq b\}}]=\lim\_{T\to 0}C\_{0}^{b}=0 |  |

as we wanted to show.
∎

## 6 A First Asymptotic Result

Now that we know that limT→0C0b=0\lim\_{T\to 0}C\_{0}^{b}=0 we want to analyse how fast does ℙ​(MT≥b)\mathbb{P}(M\_{T}\geq b) tend to zero as T→0T\to 0. A first and direct way to estimate the speed of convergence of this term is via a concentration inequality. In other words, given z∈(x,∞)z\in(x,\infty) we want to get an estimate of the tail probability

|  |  |  |
| --- | --- | --- |
|  | ℙ​(MT≥z)\mathbb{P}(M\_{T}\geq z) |  |

and apply it to z=bz=b. The literature on concentration inequalities is wide so we can easily find results in the literature that adapt to our situation. The result we will rely on in order to estimate the tail probability of MTM\_{T} is the following.

###### Lemma 6.1.

Let F∈𝔻1,2F\in\mathbb{D}^{1,2} such that ‖D​F‖ℋ≤C||DF||\_{\mathcal{H}}\leq C for some constant C>0C>0 almost surely. Then, for every θ≥0\theta\geq 0,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[eθ​F]≤e𝔼​[F]​θ+(1/2)​C2​θ2.\mathbb{E}\left[e^{\theta F}\right]\leq e^{\mathbb{E}[F]\theta+(1/2)C^{2}\theta^{2}}. |  |

In particular, for every λ≥0\lambda\geq 0,

|  |  |  |
| --- | --- | --- |
|  | ℙ​(F−𝔼​[F]≥λ)≤exp⁡(−λ22​C2).\mathbb{P}(F-\mathbb{E}[F]\geq\lambda)\leq\exp\left(-\frac{\lambda^{2}}{2C^{2}}\right). |  |

###### Proof.

See for instance Nourdin and Viens, ([2009](https://arxiv.org/html/2510.15423v1#bib.bib20)) or Üstünel, ([2010](https://arxiv.org/html/2510.15423v1#bib.bib25)) (Theorem 9.1.1).
∎

In order to apply this generic concentration inequality to MTM\_{T} we have to show that MT∈𝔻1,2M\_{T}\in\mathbb{D}^{1,2} and ‖D​MT‖ℋ≤C||DM\_{T}||\_{\mathcal{H}}\leq C for some constant C>0C>0 almost surely. The following technical results deal with the Malliavin regularity of MTM\_{T} and the computation of its Malliavin derivative. From now on, we will make use of the fact that ρ∈(−1,1)\rho\in(-1,1) and we will perform all the Malliavin calculus techniques with respect to the Brownian motion BB that, recall, is independent from the Brownian motion WW that drives the volatility, and therefore BB is independent of the volatility process σ\sigma. Hence, without loss of generality we will denote by DD the Malliavin derivative with respect to BB, δ\delta the Skorohod integral with respect to BB and 𝔻k,p\mathbb{D}^{k,p} the Malliavin spaces under the operator DD.

The following lemma will help us to prove the regularity of MTM\_{T} and find an almost explicit expression of its Malliavin derivative.

###### Lemma 6.2.

The process XX attains its maximum in the interval [0,T][0,T] at a unique random point τ∈[0,T]\tau\in[0,T].

###### Proof.

The argument uses Lemma 2.6 in Kim and Pollard, ([1990](https://arxiv.org/html/2510.15423v1#bib.bib18)), which states that if {Zt;t∈[0,T]}\{Z\_{t};t\in[0,T]\} is a Gaussian process with V​a​r​(Zt−Zs)≠0Var(Z\_{t}-Z\_{s})\neq 0 for s≠ts\neq t then the supremum of ZZ is attained at a unique point almost surely. In particular, it is shown that for two pair of distinct points t1,t2∈[0,T]t\_{1},t\_{2}\in[0,T] then

|  |  |  |
| --- | --- | --- |
|  | ℙ​(supt∈N1Zt=supt∈N2Zt)=0\mathbb{P}\left(\sup\_{t\in N\_{1}}Z\_{t}=\sup\_{t\in N\_{2}}Z\_{t}\right)=0 |  |

for every two neighbourhoods N1,N2N\_{1},N\_{2} of t1t\_{1} and t2t\_{2} respectively. Now, observe that the process XX conditioned to WW is a Gaussian process, so

|  |  |  |
| --- | --- | --- |
|  | ℙ​(supt∈N1Xt=supt∈N2Xt|ℱTW)=0.\mathbb{P}\left(\sup\_{t\in N\_{1}}X\_{t}=\sup\_{t\in N\_{2}}X\_{t}\bigg|\mathcal{F}^{W}\_{T}\right)=0. |  |

which implies that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(supt∈N1Xt=supt∈N2Xt)=0\mathbb{P}\left(\sup\_{t\in N\_{1}}X\_{t}=\sup\_{t\in N\_{2}}X\_{t}\right)=0 |  |

for all possible neighbourhoods N1N\_{1} and N2N\_{2} of t1t\_{1}, t2t\_{2} and every couple of points t1≠t2t\_{1}\neq t\_{2}, concluding this way that the supremum is attained with probability 1 at a unique point.
∎

The fact that the supremum is attained at a unique point allows us to compute the Malliavin derivative of MTM\_{T} as a function of the almost sure supremum.

###### Lemma 6.3.

The random variable MTM\_{T} belongs to 𝔻1,2\mathbb{D}^{1,2} and

|  |  |  |
| --- | --- | --- |
|  | D⋅​MT=σ⋅​1−ρ2​𝟏[0,τ]​(⋅).D\_{\cdot}M\_{T}=\sigma\_{\cdot}\sqrt{1-\rho^{2}}\mathbf{1}\_{[0,\tau]}(\cdot). |  |

###### Proof.

Consider {tn;n≥1}\{t\_{n};n\geq 1\} a dense subset of [0,T][0,T]. Define

|  |  |  |
| --- | --- | --- |
|  | MTn=max⁡{Xt1,…,Xtn}.M\_{T}^{n}=\max\{X\_{t\_{1}},\dots,X\_{t\_{n}}\}. |  |

Then, limn→∞MTn=MT\lim\_{n\to\infty}M\_{T}^{n}=M\_{T} and limn→∞τn=τ\lim\_{n\to\infty}\tau\_{n}=\tau almost surely. Using that the operator DD is local, as it is shown in Nualart, ([2006](https://arxiv.org/html/2510.15423v1#bib.bib21)), (Section 1.3.5), we have that

|  |  |  |
| --- | --- | --- |
|  | D​MTn=σ⋅​1−ρ2​𝟏[0,τn]​(⋅)DM\_{T}^{n}=\sigma\_{\cdot}\sqrt{1-\rho^{2}}\mathbf{1}\_{[0,\tau\_{n}]}(\cdot) |  |

where τn\tau\_{n} is such that MTn=XτnM\_{T}^{n}=X\_{\tau\_{n}}. On the one hand, since |MTn−MT|2→0|M\_{T}^{n}-M\_{T}|^{2}\to 0 almost surely and the sequence |MT−MTn|2|M\_{T}-M\_{T}^{n}|^{2} is monotonically decreasing we find, by the monotone convergence theorem that MTn→MTM\_{T}^{n}\to M\_{T} in L2​(Ω)L^{2}(\Omega). Moreover,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖D​MTn‖ℋ2]=𝔼​[∫0τnσt2​(1−ρ2)​𝑑t]\mathbb{E}\left[||DM\_{T}^{n}||^{2}\_{\mathcal{H}}\right]=\mathbb{E}\left[\int\_{0}^{\tau\_{n}}\sigma^{2}\_{t}(1-\rho^{2})dt\right] |  |

Hence, since τn≤T\tau\_{n}\leq T we have that

|  |  |  |
| --- | --- | --- |
|  | supn≥1𝔼​[‖D​MTn‖ℋ2]<∞.\sup\_{n\geq 1}\mathbb{E}\left[||DM\_{T}^{n}||^{2}\_{\mathcal{H}}\right]<\infty. |  |

Finally, let ℳ⋅=σ⋅​1−ρ2​𝟏[0,τ]​(⋅)\mathcal{M}\_{\cdot}=\sigma\_{\cdot}\sqrt{1-\rho^{2}}\mathbf{1}\_{[0,\tau]}(\cdot). for every u∈L2​(Ω;ℋ)u\in L^{2}(\Omega;\mathcal{H}) we find using the dominated convergence theorem that

|  |  |  |
| --- | --- | --- |
|  | limn→∞𝔼​[∫0τn1−ρ2​σt​ut​𝑑t]=𝔼​[∫0τ1−ρ2​σt​ut​𝑑t]\lim\_{n\to\infty}\mathbb{E}\left[\int\_{0}^{\tau\_{n}}\sqrt{1-\rho^{2}}\sigma\_{t}u\_{t}dt\ \right]=\mathbb{E}\left[\int\_{0}^{\tau}\sqrt{1-\rho^{2}}\sigma\_{t}u\_{t}dt\ \right] |  |

so D​MTnDM^{n}\_{T} converges to ℳ\mathcal{M} in the weak topology of L2​(Ω;ℋ)L^{2}(\Omega;\mathcal{H}). This allows us to conclude, thanks to Nualart, ([2006](https://arxiv.org/html/2510.15423v1#bib.bib21)) (Lemma 1.2.3) that MT∈𝔻B1,2M\_{T}\in\mathbb{D}^{1,2}\_{B} and D⋅​MT=σ⋅​1−ρ2​𝟏[0,τ]​(⋅).D\_{\cdot}M\_{T}=\sigma\_{\cdot}\sqrt{1-\rho^{2}}\mathbf{1}\_{[0,\tau]}(\cdot). as desired.
∎

From this lemmas we are able to construct a tail estimate of the probability of reaching the barrier.

###### Theorem 6.4 (Tail estimate).

Let MT=supt∈[0,T]XtM\_{T}=\sup\_{t\in[0,T]}X\_{t}. Then there exists T0T\_{0} such that for T≤T0T\leq T\_{0} the following tail estimate holds:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(MT≥b)≤exp⁡(−(b−x)2C2​T).\mathbb{P}\left(M\_{T}\geq b\right)\leq\exp\left(-\frac{(b-x)^{2}}{C^{2}T}\right). |  |

###### Proof.

We want to apply the concentration inequality result to F=MT.F=M\_{T}. Recall that we have proved that MT∈𝔻1,2M\_{T}\in\mathbb{D}^{1,2} and

|  |  |  |
| --- | --- | --- |
|  | D​MT=σ​1−ρ2​𝟏[0,τ].DM\_{T}=\sigma\sqrt{1-\rho^{2}}\mathbf{1}\_{[0,\tau]}. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | ‖D​MT‖ℋ=∫0τ(1−ρ2)​σt2​𝑑t≤C​T.||DM\_{T}||\_{\mathcal{H}}=\sqrt{\int\_{0}^{\tau}(1-\rho^{2})\sigma\_{t}^{2}dt}\leq C\sqrt{T}. |  |

If we define mT=𝔼​[MT]m\_{T}=\mathbb{E}[M\_{T}] we obtain

|  |  |  |
| --- | --- | --- |
|  | P​(MT−mT≥λ)≤exp⁡(−λ2C2​T).P(M\_{T}-m\_{T}\geq\lambda)\leq\exp\left(-\frac{\lambda^{2}}{C^{2}T}\right). |  |

Therefore, if bb denotes the log-barrier we find that

|  |  |  |
| --- | --- | --- |
|  | P​(MT≥b)≤exp⁡(−(b−mT)2C2​T).P(M\_{T}\geq b)\leq\exp\left(-\frac{(b-m\_{T})^{2}}{C^{2}T}\right). |  |

Finally, since limT→0mT=x\lim\_{T\to 0}m\_{T}=x we find that there exists T0T\_{0} such that

|  |  |  |
| --- | --- | --- |
|  | (b−mT)2≥12​(b−x)2.(b-m\_{T})^{2}\geq\frac{1}{2}(b-x)^{2}. |  |

Renaming the constants, we find that for T≤T0T\leq T\_{0}

|  |  |  |
| --- | --- | --- |
|  | ℙ​(MT≥b)≤exp⁡(−(b−x)2C2​T)\mathbb{P}\left(M\_{T}\geq b\right)\leq\exp\left(-\frac{(b-x)^{2}}{C^{2}T}\right) |  |

as claimed.
∎

## 7 Estimation Of The Density Of MTM\_{T}

In the previous section we have derived an estimation of the probability of attaining the barrier using an estimation of the cumulative distribution function of MTM\_{T}. In this section we will proceed with more involved Malliavin calculus tools in order to explore if the previous bound can be improved. The objective of this section will be exploring the density function of MTM\_{T} and approximate the cumulative distribution function of MTM\_{T} using its density. Hence, we shall first show that the density exists and it is smooth. In order to check this property we will rely on the local criterion of existence and smoothness of densities for 𝔻1,2\mathbb{D}^{1,2} random variables stated in Section [3](https://arxiv.org/html/2510.15423v1#S3 "3 Malliavin Calculus Tools ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS").

To be able to apply this criterion we need to find a set AA, a stochastic process uA∈𝔻∞u\_{A}\in\mathbb{D}^{\infty} and a random variable γA∈𝔻∞\gamma\_{A}\in\mathbb{D}^{\infty} such that the equality ⟨D​MT,uA⟩=γA\langle DM\_{T},u\_{A}\rangle=\gamma\_{A} holds on the set AA. We will rely on the process YY to construct such uAu\_{A} and γA\gamma\_{A}, since its behaviour is closely related to MTM\_{T} and it is Malliavin regular, as the following two results shows:

###### Lemma 7.1.

For any r∈[0,T]r\in[0,T], Yr∈𝔻∞Y\_{r}\in\mathbb{D}^{\infty} and

|  |  |  |
| --- | --- | --- |
|  | Dk​Yr=∫[0,r]22​p0​(2​p0−1)​⋯​(2​p0−k+1)​(Xt−Xs)2​p0−k|t−s|γ0​Dk​(Xt−Xs)​𝑑t​𝑑s.D^{k}Y\_{r}=\int\_{[0,r]^{2}}\frac{2p\_{0}(2p\_{0}-1)\cdots(2p\_{0}-k+1)(X\_{t}-X\_{s})^{2p\_{0}-k}}{|t-s|^{\gamma\_{0}}}D^{k}(X\_{t}-X\_{s})dtds. |  |

###### Proof.

The proof follows the same ideas as in Pu, ([2018](https://arxiv.org/html/2510.15423v1#bib.bib23)).
∎

We can in fact go further on the study of the regularity of YY. Indeed, not only the moments of YrY\_{r} and its derivatives are finite for every r∈[0,T]r\in[0,T], but they are uniformly bounded in r∈[0,T]r\in[0,T] as we show in the upcoming lemma.

###### Lemma 7.2.

For any p≥1p\geq 1 and for every integer kk,

|  |  |  |
| --- | --- | --- |
|  | supr∈[0,T]𝔼​[‖Dk​Yr‖ℋ⊗kp]<∞.\sup\_{r\in[0,T]}\mathbb{E}\left[||D^{k}Y\_{r}||^{p}\_{\mathcal{H}^{\otimes k}}\right]<\infty. |  |

###### Proof.

We give the proof for k=1k=1. The proof for a general k≥1k\geq 1 uses Lemma [7.1](https://arxiv.org/html/2510.15423v1#S7.Thmteo1 "Lemma 7.1. ‣ 7 Estimation Of The Density Of 𝑀_𝑇 ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS") and follows the same lines as with the case k=1k=1. For the first order derivative we have

|  |  |  |
| --- | --- | --- |
|  | D​Yr=∫[0,r]22​p0​(Xt−Xs)2​p0−1|t−s|γ0​D​(Xt−Xs)​𝑑t​𝑑s.DY\_{r}=\int\_{[0,r]^{2}}\frac{2p\_{0}(X\_{t}-X\_{s})^{2p\_{0}-1}}{|t-s|^{\gamma\_{0}}}D(X\_{t}-X\_{s})dtds. |  |

Hence, Hölder’s inequality for p≥1p\geq 1 shows that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖D​Yr‖ℋp]≤cp​r2​(p−1)​∫[0,r]2𝔼​[|Xt−Xs|(2​p0−1)​p]|t−s|γ0​p​‖D​(Xt−Xs)‖ℋp.\displaystyle\mathbb{E}\left[||DY\_{r}||\_{\mathcal{H}}^{p}\right]\leq c\_{p}r^{2(p-1)}\int\_{[0,r]^{2}}\frac{\mathbb{E}[|X\_{t}-X\_{s}|^{(2p\_{0}-1)p}]}{|t-s|^{\gamma\_{0}p}}||D(X\_{t}-X\_{s})||^{p}\_{\mathcal{H}}. |  |

Now, observe that

|  |  |  |
| --- | --- | --- |
|  | Ds​σt=σs​1−ρ2​𝟏[0,t]​(s),D\_{s}\sigma\_{t}=\sigma\_{s}\sqrt{1-\rho^{2}}\mathbf{1}\_{[0,t]}(s), |  |

so

|  |  |  |
| --- | --- | --- |
|  | Du​(Xt−Xs)=σu​1−ρ2​𝟏[t∧s,t∨s]​(u).D\_{u}(X\_{t}-X\_{s})=\sigma\_{u}\sqrt{1-\rho^{2}}\mathbf{1}\_{[t\wedge s,t\vee s]}(u). |  |

This implies that

|  |  |  |
| --- | --- | --- |
|  | ∫0T(Du​(Xt−Xs))2​𝑑u=(1−ρ2)​∫t∧st∨sσu2​𝑑u≤C​(1−ρ2)​|t−s|\int\_{0}^{T}(D\_{u}(X\_{t}-X\_{s}))^{2}du=(1-\rho^{2})\int\_{t\wedge s}^{t\vee s}\sigma\_{u}^{2}du\leq C(1-\rho^{2})|t-s| |  |

and therefore there exists a constant C>0C>0 such that

|  |  |  |
| --- | --- | --- |
|  | ‖D​(Xt−Xs)‖ℋp≤C​|t−s|p||D(X\_{t}-X\_{s})||^{p}\_{\mathcal{H}}\leq C|t-s|^{p} |  |

This estimate shows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖D​Yr‖ℋp]≤\displaystyle\mathbb{E}\left[||DY\_{r}||\_{\mathcal{H}}^{p}\right]\leq | cp​r2​(p−1)​∫[0,r]2|t−s|(p0−1/2)​p+p−γ0​p​𝑑t​𝑑s\displaystyle c\_{p}r^{2(p-1)}\int\_{[0,r]^{2}}|t-s|^{(p\_{0}-1/2)p+p-\gamma\_{0}p}dtds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | cp​r2​(p−1)​∫[0,r]2|t−s|p​(p0−γ0+1/2)​𝑑t​𝑑s\displaystyle c\_{p}r^{2(p-1)}\int\_{[0,r]^{2}}|t-s|^{p(p\_{0}-\gamma\_{0}+1/2)}dtds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | cp​r2​(p−1)​rp0​p−p​γ0+p/2+2\displaystyle c\_{p}r^{2(p-1)}r^{p\_{0}p-p\gamma\_{0}+p/2+2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | cp​r5​p/2+p0​p−p​γ0\displaystyle c\_{p}r^{5p/2+p\_{0}p-p\gamma\_{0}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | cp​rp​(p0−γ0+5/2).\displaystyle c\_{p}r^{p(p\_{0}-\gamma\_{0}+5/2)}. |  |

The result follows from applying supremums to both sides of the inequality.
∎

We can now construct the setting in order to prove the existence and smoothness of the density. For all z∈(x,∞)z\in(x,\infty) let a=x+z2a=\frac{x+z}{2} and A=(a,∞)A=\left(a,\infty\right). Let RT:=RT​(a)R\_{T}:=R\_{T}(a) be the radius such that

|  |  |  |
| --- | --- | --- |
|  | Yr≤RT​(a)⇒supt∈[0,r]Xt≤a.Y\_{r}\leq R\_{T}(a)\Rightarrow\sup\_{t\in[0,r]}X\_{t}\leq a. |  |

Let ψ0​(x)\psi\_{0}(x) be a smooth function such that ψ0​(x)=0\psi\_{0}(x)=0 if x>1x>1, ψ0​(x)=0\psi\_{0}(x)=0 if x≤12x\leq\frac{1}{2} and ψ0​(x)∈[0,1]\psi\_{0}(x)\in[0,1] if x∈[12,1]x\in\left[\frac{1}{2},1\right]. We define ψ​(x)\psi(x) as

|  |  |  |
| --- | --- | --- |
|  | ψ​(x)=ψ0​(xRT).\psi(x)=\psi\_{0}\left(\frac{x}{R\_{T}}\right). |  |

Notice that ‖ψ′‖∞≤c​RT−1||\psi^{\prime}||\_{\infty}\leq cR^{-1}\_{T}. We define

|  |  |  |
| --- | --- | --- |
|  | uA=ψ​(Y⋅)σ⋅​1−ρ2,γA=∫0Tψ​(Yr)​𝑑r.u\_{A}=\frac{\psi(Y\_{\cdot})}{\sigma\_{\cdot}\sqrt{1-\rho^{2}}},\quad\gamma\_{A}=\int\_{0}^{T}\psi(Y\_{r})dr. |  |

Now that we have the candidates of AA, uAu\_{A} and γA\gamma\_{A} we have to prove that the criterion holds.

###### Lemma 7.3.

We have uA∈𝔻∞​(ℋ)u\_{A}\in\mathbb{D}^{\infty}(\mathcal{H}), γA∈𝔻∞\gamma\_{A}\in\mathbb{D}^{\infty} and ⟨D​MT,uA⟩=γA\langle DM\_{T},u\_{A}\rangle=\gamma\_{A} in the set AA. In conclusion, MTM\_{T} has a smooth density.

###### Proof.

The proof of the fact uA∈𝔻∞​(ℋ)u\_{A}\in\mathbb{D}^{\infty}(\mathcal{H}) follows from the fact that σ\sigma is independent of BB, Y∈𝔻∞​(ℋ)Y\in\mathbb{D}^{\infty}(\mathcal{H}), the smoothness of ψ\psi and the chain rule of the Malliavin calculus. Similarly, the fact that γA∈𝔻∞\gamma\_{A}\in\mathbb{D}^{\infty} follows directly from the fact that Yr∈𝔻∞Y\_{r}\in\mathbb{D}^{\infty}, supr∈[0,T]‖Dk​Yr‖ℋ⊗kp<∞\sup\_{r\in[0,T]}||D^{k}Y\_{r}||\_{\mathcal{H}^{\otimes k}}^{p}<\infty for all k≥1k\geq 1 and for all p≥1p\geq 1 and the chain rule of Malliavin calculus.

Now, observe that

|  |  |  |
| --- | --- | --- |
|  | ⟨D​MT,uA⟩=∫0τσt​1−ρ2​ψ​(Yt)σt​1−ρ2​𝑑t=∫0τψ​(Yt)​𝑑t.\langle DM\_{T},u\_{A}\rangle=\int\_{0}^{\tau}\sigma\_{t}\sqrt{1-\rho^{2}}\frac{\psi(Y\_{t})}{\sigma\_{t}\sqrt{1-\rho^{2}}}dt=\int\_{0}^{\tau}\psi(Y\_{t})dt. |  |

We now need to prove that

|  |  |  |
| --- | --- | --- |
|  | ∫0τψ​(Yt)​𝑑t=∫0Tψ​(Yt)​𝑑t\int\_{0}^{\tau}\psi(Y\_{t})dt=\int\_{0}^{T}\psi(Y\_{t})dt |  |

or, equivalently, ψ​(Yr)=0\psi(Y\_{r})=0 if r∈[τ,T]r\in[\tau,T]. Notice that if ψ​(Yr)>0\psi(Y\_{r})>0 if r>τr>\tau then we would have Yr≤RTY\_{r}\leq R\_{T} and therefore, the following holds:

|  |  |  |
| --- | --- | --- |
|  | MT=Xτ=supt∈[0,T]Xt=supt∈[0,r]Xt≤a.M\_{T}=X\_{\tau}=\sup\_{t\in[0,T]}X\_{t}=\sup\_{t\in[0,r]}X\_{t}\leq a. |  |

However, on the set {MT∈A}\{M\_{T}\in A\} we have MT>aM\_{T}>a so we arrive at a contradiction, proving like this that

|  |  |  |
| --- | --- | --- |
|  | ∫0τψ​(Yt)​𝑑t=∫0Tψ​(Yt)​𝑑t\int\_{0}^{\tau}\psi(Y\_{t})dt=\int\_{0}^{T}\psi(Y\_{t})dt |  |

and therefore ⟨D​MT,uA⟩=γA\langle DM\_{T},u\_{A}\rangle=\gamma\_{A}.
∎

This result, even though it’s technical and does not tell us an explicit expression of the density function of MTM\_{T}, it allows us to obtain a representation that we will use later on to obtain an estimate.

###### Proposition 7.4.

The probability density function of MTM\_{T} at the point z∈(x,∞)z\in(x,\infty) is given by

|  |  |  |
| --- | --- | --- |
|  | p​(z)=𝔼​[𝟏{MT>z}​δ​(uAγA)]p(z)=\mathbb{E}\left[\mathbf{1}\_{\{M\_{T}>z\}}\delta\left(\frac{u\_{A}}{\gamma\_{A}}\right)\right] |  |

###### Proof.

Let κ:ℝ→[0,1]\kappa:\mathbb{R}\to[0,1] be an infinitely differentiable function such that

|  |  |  |
| --- | --- | --- |
|  | κ​(r)={0r≤x+z2,1r≥x+3​z4.\kappa(r)=\begin{cases}0&r\leq\frac{x+z}{2},\\ 1&r\geq\frac{x+3z}{4}.\end{cases} |  |

We define also the random variable G=κ​(MT)G=\kappa(M\_{T}). Observe that G=0G=0 on the set {MT∉A}\{M\_{T}\notin A\}. Let f∈𝒞0∞​(ℝ)f\in\mathcal{C}^{\infty}\_{0}(\mathbb{R}) and let φ​(x)=∫−∞xf​(y)​𝑑y\varphi(x)=\int\_{-\infty}^{x}f(y)dy. On the set {MT∈A}\{M\_{T}\in A\} we have

|  |  |  |
| --- | --- | --- |
|  | ⟨D​φ​(MT),uA⟩=φ′​(MT)​⟨D​MT,uA⟩=φ′​(MT)​γA\langle D\varphi(M\_{T}),u\_{A}\rangle=\varphi^{\prime}(M\_{T})\langle DM\_{T},u\_{A}\rangle=\varphi^{\prime}(M\_{T})\gamma\_{A} |  |

and therefore

|  |  |  |
| --- | --- | --- |
|  | G​φ′​(MT)=⟨D​φ​(MT),G​uAγA⟩G\varphi^{\prime}(M\_{T})=\langle D\varphi(M\_{T}),\frac{Gu\_{A}}{\gamma\_{A}}\rangle |  |

Therefore, if we take expectations on both sides and we use the duality relationship between the Malliavin derivative and the divergence operator we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[G​φ′​(MT)]=𝔼​[φ​(MT)​δ​(G​uAγA)].\mathbb{E}[G\varphi^{\prime}(M\_{T})]=\mathbb{E}\left[\varphi(M\_{T})\delta\left(\frac{Gu\_{A}}{\gamma\_{A}}\right)\right]. |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[G​φ′​(MT)]=∫ℝf​(y)​𝔼​[𝟏{MT>y}​δ​(G​uAγA)]​𝑑y.\mathbb{E}[G\varphi^{\prime}(M\_{T})]=\int\_{\mathbb{R}}f(y)\mathbb{E}\left[\mathbf{1}\_{\{M\_{T}>y\}}\delta\left(\frac{Gu\_{A}}{\gamma\_{A}}\right)\right]dy. |  |

Finally, since φ′=f\varphi^{\prime}=f we find that for every y∈(x+3​z4,∞)y\in(\frac{x+3z}{4},\infty) it is satisfied that G=1G=1 and therefore the density at the point z∈(x+3​z4,∞)z\in(\frac{x+3z}{4},\infty) is given by

|  |  |  |
| --- | --- | --- |
|  | p​(z)=𝔼​[𝟏{MT>z}​δ​(uAγA)].p(z)=\mathbb{E}\left[\mathbf{1}\_{\{M\_{T}>z\}}\delta\left(\frac{u\_{A}}{\gamma\_{A}}\right)\right]. |  |

∎

The Cauchy-Schwartz inequality provides a direct upper bound for p​(z)p(z). Indeed,

|  |  |  |
| --- | --- | --- |
|  | p​(z)≤ℙ​(MT≥z)1/2​‖δ​(uA​γA−1)‖L2​(Ω).p(z)\leq\mathbb{P}(M\_{T}\geq z)^{1/2}||\delta(u\_{A}\gamma\_{A}^{-1})||\_{L^{2}(\Omega)}. |  |

The tail estimate obtained in the previous section allows us to deal with the ℙ​(MT≥z)1/2\mathbb{P}(M\_{T}\geq z)^{1/2} term, so the analysis of the density of MTM\_{T} is focused on the analysis of the term ‖δ​(uA​γA−1)‖L2​(Ω)||\delta(u\_{A}\gamma\_{A}^{-1})||\_{L^{2}(\Omega)}. Let’s break down the strategy to analyse this latter term. Proposition [3.1](https://arxiv.org/html/2510.15423v1#S3.Thmteo1 "Proposition 3.1. ‣ 3 Malliavin Calculus Tools ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS") allows us to write

|  |  |  |
| --- | --- | --- |
|  | δ​(uAγA)=δ​(uA)γA+⟨D​γA,uA⟩γA2=I1+I2,\delta\left(\frac{u\_{A}}{\gamma\_{A}}\right)=\frac{\delta(u\_{A})}{\gamma\_{A}}+\frac{\langle D\gamma\_{A},u\_{A}\rangle}{\gamma\_{A}^{2}}=I\_{1}+I\_{2}, |  |

so

|  |  |  |
| --- | --- | --- |
|  | ‖δ​(uAγA)‖L2​(Ω)≤‖I1‖L2​(Ω)+‖I2‖L2​(Ω).\left|\left|\delta\left(\frac{u\_{A}}{\gamma\_{A}}\right)\right|\right|\_{L^{2}(\Omega)}\leq||I\_{1}||\_{L^{2}(\Omega)}+||I\_{2}||\_{L^{2}(\Omega)}. |  |

The following sequence of lemmas provide an analysis of the moments of the terms involved.

###### Lemma 7.5.

There exists a constant C>0C>0 depending on ψ\psi, pp, σ\sigma and ρ\rho such that

|  |  |  |
| --- | --- | --- |
|  | ‖δ​(uA)‖Lp​(Ω)≤C​T||\delta(u\_{A})||\_{L^{p}(\Omega)}\leq C\sqrt{T} |  |

###### Proof.

It is clear that

|  |  |  |
| --- | --- | --- |
|  | δ​(uA)=∫0Tψ​(Yr)σr​1−ρ2​𝑑Br\delta(u\_{A})=\int\_{0}^{T}\frac{\psi(Y\_{r})}{\sigma\_{r}\sqrt{1-\rho^{2}}}dB\_{r} |  |

so Burkholder’s inequality, the definition of ψ\psi and the hypotheses on σ\sigma show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|δ​(uA)|p]≤\displaystyle\mathbb{E}[|\delta(u\_{A})|^{p}]\leq | cp​𝔼​[(∫0Tψ​(Yr)2σr2​(1−ρ2)​𝑑r)p/2]\displaystyle c\_{p}\mathbb{E}\left[\left(\int\_{0}^{T}\frac{\psi(Y\_{r})^{2}}{\sigma\_{r}^{2}(1-\rho^{2})}dr\right)^{p/2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​𝔼​[(∫0Tψ​(Yr)2​𝑑r)p/2]\displaystyle C\mathbb{E}\left[\left(\int\_{0}^{T}\psi(Y\_{r})^{2}dr\right)^{p/2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​Tp/2\displaystyle CT^{p/2} |  |

so

|  |  |  |
| --- | --- | --- |
|  | ‖δ​(uA)‖Lp​(Ω)≤C​T.||\delta(u\_{A})||\_{L^{p}(\Omega)}\leq C\sqrt{T}. |  |

∎

###### Lemma 7.6.

There exists a constant C>0C>0 depending on ψ\psi, ρ\rho and σ\sigma such that

|  |  |  |
| --- | --- | --- |
|  | ‖uA‖ℋ≤C​T.||u\_{A}||\_{\mathcal{H}}\leq C\sqrt{T}. |  |

###### Proof.

Applying the definition of uAu\_{A} we see that

|  |  |  |
| --- | --- | --- |
|  | ‖uA‖ℋ2=∫0Tψ​(Yr)2σr2​1−ρ2​𝑑r||u\_{A}||\_{\mathcal{H}}^{2}=\int\_{0}^{T}\frac{\psi(Y\_{r})^{2}}{\sigma\_{r}^{2}\sqrt{1-\rho^{2}}}dr |  |

so the conclusion follows using the same estimations as in the previous lemma.
∎

###### Lemma 7.7.

There exists a constant C>0C>0 depending on ψ\psi, ρ\rho and σ\sigma such that

|  |  |  |
| --- | --- | --- |
|  | ‖⟨D​γA,uA⟩ℋ‖Lp​(Ω)≤C​T4||\langle D\gamma\_{A},u\_{A}\rangle\_{\mathcal{H}}||\_{L^{p}(\Omega)}\leq CT^{4} |  |

for some constant C>0C>0 not depending on TT.

###### Proof.

Since Dt​γA=∫0Tψ′​(Yr)​Du​Yr​𝑑rD\_{t}\gamma\_{A}=\int\_{0}^{T}\psi^{\prime}(Y\_{r})D\_{u}Y\_{r}dr we have that

|  |  |  |
| --- | --- | --- |
|  | ⟨D​γA,uA⟩=∫0T∫0Tψ′​(Yr)​Dt​Yr​uA​(t)​𝑑r​𝑑t=∫0Tψ′​(Yr)​⟨D​Yr,uA⟩​𝑑r.\langle D\gamma\_{A},u\_{A}\rangle=\int\_{0}^{T}\int\_{0}^{T}\psi^{\prime}(Y\_{r})D\_{t}Y\_{r}u\_{A}(t)drdt=\int\_{0}^{T}\psi^{\prime}(Y\_{r})\langle DY\_{r},u\_{A}\rangle dr. |  |

Now, Hölder’s inequality for p≥1p\geq 1 shows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|⟨D​γA,uA⟩|p]≤\displaystyle\mathbb{E}[|\langle D\gamma\_{A},u\_{A}\rangle|^{p}]\leq | Tp−1​‖ψ′‖∞p​∫0T𝔼​[|⟨D​Yr,uA⟩|p]​𝑑r\displaystyle T^{p-1}||\psi^{\prime}||\_{\infty}^{p}\int\_{0}^{T}\mathbb{E}[|\langle DY\_{r},u\_{A}\rangle|^{p}]dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​Tp−1​RT​(a)−p​∫0T𝔼​[‖D​Yr‖ℋp​‖uA‖ℋp]​𝑑r\displaystyle CT^{p-1}R\_{T}(a)^{-p}\int\_{0}^{T}\mathbb{E}[||DY\_{r}||\_{\mathcal{H}}^{p}||u\_{A}||\_{\mathcal{H}}^{p}]dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​T3​p/2−1​RT​(a)−p​∫0T𝔼​[‖D​Yr‖ℋp]​𝑑r\displaystyle CT^{3p/2-1}R\_{T}(a)^{-p}\int\_{0}^{T}\mathbb{E}[||DY\_{r}||\_{\mathcal{H}}^{p}]dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​RT​(a)−p​T3​p/2−1​∫0Trp​(p0−γ0+5/2)​𝑑r\displaystyle CR\_{T}(a)^{-p}T^{3p/2-1}\int\_{0}^{T}r^{p(p\_{0}-\gamma\_{0}+5/2)}dr |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​RT​(a)−p​T4​p+p​p0−p​γ0−2​p+p​γ02\displaystyle CR\_{T}(a)^{-p}T^{4p+pp\_{0}-p\gamma\_{0}-2p+\frac{p\gamma\_{0}}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​Tp​(2+p0−γ02)\displaystyle CT^{p(2+p\_{0}-\frac{\gamma\_{0}}{2})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​T4​p\displaystyle CT^{4p} |  |

where we have applied the bound for 𝔼​[‖D​Yr‖ℋp]\mathbb{E}[||DY\_{r}||\_{\mathcal{H}}^{p}], the definition of RT​(a)R\_{T}(a) and the fact that p0>6p\_{0}>6.
∎

###### Lemma 7.8.

The random variable γA\gamma\_{A} has negative moments of all orders- Furthermore, if we assume z≥x+T1/4z\geq x+T^{1/4} then there exists a constant C>0C>0 not depending on TT such that

|  |  |  |
| --- | --- | --- |
|  | ‖γA−1‖Lp​(Ω)≤CT||\gamma\_{A}^{-1}||\_{L^{p}(\Omega)}\leq\frac{C}{T} |  |

###### Proof.

Since

|  |  |  |
| --- | --- | --- |
|  | γA=∫0Tψ(Yr)dr≥∫0T𝟏{Yr≤RT​(a)2}dr=:ΓA.\gamma\_{A}=\int\_{0}^{T}\psi(Y\_{r})dr\geq\int\_{0}^{T}\mathbf{1}\_{\{Y\_{r}\leq\frac{R\_{T}(a)}{2}\}}dr=:\Gamma\_{A}. |  |

Let 0<ε<T0<\varepsilon<T. We find that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(ΓA<ε)≤ℙ​(Yε≥RT​(a)/2)≤2q​𝔼​[Yεq]RT​(a)q≤Cq​ε2​q​RT​(a)−q​T(p0−γ0)​q.\mathbb{P}(\Gamma\_{A}<\varepsilon)\leq\mathbb{P}(Y\_{\varepsilon}\geq R\_{T}(a)/2)\leq\frac{2^{q}\mathbb{E}[Y\_{\varepsilon}^{q}]}{R\_{T}(a)^{q}}\leq C\_{q}\varepsilon^{2q}R\_{T}(a)^{-q}T^{(p\_{0}-\gamma\_{0})q}. |  |

This allows us to conclude, thanks to [Dalang et al., 2009a](https://arxiv.org/html/2510.15423v1#bib.bib7)  (Chapter 3, Lemma 4.4), that ΓA\Gamma\_{A} has negative moments of all orders and therefore so does γA\gamma\_{A}. We can make a further analysis to show that for every 2​q>p2q>p we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ΓA−p]=\displaystyle\mathbb{E}[\Gamma\_{A}^{-p}]= | p​∫0∞yp−1​ℙ​(ΓA−1>y)​𝑑y\displaystyle p\int\_{0}^{\infty}y^{p-1}\mathbb{P}(\Gamma\_{A}^{-1}>y)dy |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | p​∫0T−1yp−1​ℙ​(ΓA−1>y)​𝑑y+p​∫T−1∞yp−1​ℙ​(ΓA−1>y)​𝑑y\displaystyle p\int\_{0}^{T^{-1}}y^{p-1}\mathbb{P}(\Gamma\_{A}^{-1}>y)dy+p\int\_{T^{-1}}^{\infty}y^{p-1}\mathbb{P}(\Gamma\_{A}^{-1}>y)dy |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​T−p+C​RT​(a)−q​T(p0−γ0)​q​∫T−1∞yp−2​q−1​𝑑y.\displaystyle CT^{-p}+CR\_{T}(a)^{-q}T^{(p\_{0}-\gamma\_{0})q}\int\_{T^{-1}}^{\infty}y^{p-2q-1}dy. |  |

Since

|  |  |  |
| --- | --- | --- |
|  | RT​(a)=C​(a−x)−2​p0​T4−γ02R\_{T}(a)=C(a-x)^{-2p\_{0}}T^{\frac{4-\gamma\_{0}}{2}} |  |

and a−x>T1/42a-x>\frac{T^{1/4}}{2} because z>x+T1/4z>x+T^{1/4}, then

|  |  |  |
| --- | --- | --- |
|  | RT​(a)−q≤T−q​p02​T−(4−γ0)​q2.R\_{T}(a)^{-q}\leq T^{-\frac{qp\_{0}}{2}}T^{\frac{-(4-\gamma\_{0})q}{2}}. |  |

This implies that

|  |  |  |
| --- | --- | --- |
|  | RT​(a)−q​T(p0−γ0)​q​∫T−1∞yp−2​q−1​𝑑y≤T−q​p02​T−(4−γ0)​q2​T(p0−γ0)​q​T2​q−p.R\_{T}(a)^{-q}T^{(p\_{0}-\gamma\_{0})q}\int\_{T^{-1}}^{\infty}y^{p-2q-1}dy\leq T^{-\frac{qp\_{0}}{2}}T^{\frac{-(4-\gamma\_{0})q}{2}}T^{(p\_{0}-\gamma\_{0})q}T^{2q-p}. |  |

We gather together the exponents as

|  |  |  |  |
| --- | --- | --- | --- |
|  | −q​p02−2​q+γ0​q2+q​p0−γ0​q+2​q−p=\displaystyle-\frac{qp\_{0}}{2}-2q+\frac{\gamma\_{0}q}{2}+qp\_{0}-\gamma\_{0}q+2q-p= | q​p02−q​γ02−p\displaystyle\frac{qp\_{0}}{2}-\frac{q\gamma\_{0}}{2}-p |  |

to obtain that

|  |  |  |
| --- | --- | --- |
|  | C​T−p+C​RT​(a)−q​T(p0−γ0)​q​∫T−1∞yp−2​q−1​𝑑y≤C​T−p​(1+Tp0−γ02).CT^{-p}+CR\_{T}(a)^{-q}T^{(p\_{0}-\gamma\_{0})q}\int\_{T^{-1}}^{\infty}y^{p-2q-1}dy\leq CT^{-p}(1+T^{\frac{p\_{0}-\gamma\_{0}}{2}}). |  |

Finally, using the relationships p0−2>γ0>4p\_{0}-2>\gamma\_{0}>4 we conclude that the exponent p0−γ02\frac{p\_{0}-\gamma\_{0}}{2} is positive. Consequently, there exists C>0C>0 such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ΓA−p]≤C​T−p.\mathbb{E}[\Gamma\_{A}^{-p}]\leq CT^{-p}. |  |

since γA≥ΓA\gamma\_{A}\geq\Gamma\_{A} we conclude the result.
∎

We are now ready to prove the upper bound for the density of MTM\_{T}.

###### Theorem 7.9.

There exists T0>0T\_{0}>0 such that for all T≤T0T\leq T\_{0}, the density function p​(z)p(z) of the random variable MTM\_{T} satisfies the following upper bound:

|  |  |  |
| --- | --- | --- |
|  | p​(z)≤2​C​1T​exp⁡(−(z−x)22​C2​T)p(z)\leq 2C\frac{1}{\sqrt{T}}\exp\left(-\frac{(z-x)^{2}}{2C^{2}T}\right) |  |

for a constant C>0C>0 not depending on TT.

###### Proof.

As it was shown,

|  |  |  |
| --- | --- | --- |
|  | p0​(z)≤ℙ​(MT≥z)1/2​(‖I1‖L2​(Ω)+‖I2‖L2​(Ω)).p\_{0}(z)\leq\mathbb{P}(M\_{T}\geq z)^{1/2}(||I\_{1}||\_{L^{2}(\Omega)}+||I\_{2}||\_{L^{2}(\Omega)}). |  |

Now, using Hölder’s inequality we see that

|  |  |  |
| --- | --- | --- |
|  | ‖I1‖L2​(Ω)≤C​T1/2​T−1=C​T−1/2,‖I2‖L2​(Ω)≤C​T4​T−2≤C​T2.||I\_{1}||\_{L^{2}(\Omega)}\leq CT^{1/2}T^{-1}=CT^{-1/2},\quad||I\_{2}||\_{L^{2}(\Omega)}\leq CT^{4}T^{-2}\leq CT^{2}. |  |

Hence, plugging all the estimates obtained in Lemmas [7.6](https://arxiv.org/html/2510.15423v1#S7.Thmteo6 "Lemma 7.6. ‣ 7 Estimation Of The Density Of 𝑀_𝑇 ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS"), [7.7](https://arxiv.org/html/2510.15423v1#S7.Thmteo7 "Lemma 7.7. ‣ 7 Estimation Of The Density Of 𝑀_𝑇 ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS") and [7.8](https://arxiv.org/html/2510.15423v1#S7.Thmteo8 "Lemma 7.8. ‣ 7 Estimation Of The Density Of 𝑀_𝑇 ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS") we are able to show that there exist c1,c2>0c\_{1},c\_{2}>0 such that

|  |  |  |
| --- | --- | --- |
|  | p​(z)≤c1​(1T+T2)​exp⁡(−(z−mT)22​c22​T)≤2​c1​1T​exp⁡(−(z−mT)22​c22​T).p(z)\leq c\_{1}\left(\frac{1}{\sqrt{T}}+T^{2}\right)\exp\left(-\frac{(z-m\_{T})^{2}}{2c\_{2}^{2}T}\right)\leq 2c\_{1}\frac{1}{\sqrt{T}}\exp\left(-\frac{(z-m\_{T})^{2}}{2c\_{2}^{2}T}\right). |  |

Using again that mT→xm\_{T}\to x as T→0T\to 0 and renaming the constants we obtain the claimed statement.
∎

This result is the key to understand the asymptotic behaviour of the Call price C0bC\_{0}^{b}.

###### Theorem 7.10.

Let C0bC\_{0}^{b} be an up-and-in barrier call option with log-barrier b>x=log⁡S0b>x=\log S\_{0}. Then, the probability of reaching the barrier satisfies the upper bound

|  |  |  |
| --- | --- | --- |
|  | ℙ​(MT≥b)≤∫b∞c1T​exp⁡(−(z−x)22​c2​T)​𝑑z\mathbb{P}(M\_{T}\geq b)\leq\int\_{b}^{\infty}\frac{c\_{1}}{\sqrt{T}}\exp\left(-\frac{(z-x)^{2}}{2c\_{2}T}\right)dz |  |

and, in particular, C0bC\_{0}^{b} approaches zero faster than any polynomial of TT.

###### Proof.

The fact that

|  |  |  |
| --- | --- | --- |
|  | ℙ​(MT≥b)≤∫b∞c1T​exp⁡(−(z−x)22​c2​T)​𝑑z\mathbb{P}(M\_{T}\geq b)\leq\int\_{b}^{\infty}\frac{c\_{1}}{\sqrt{T}}\exp\left(-\frac{(z-x)^{2}}{2c\_{2}T}\right)dz |  |

comes directly from Theorem [7.9](https://arxiv.org/html/2510.15423v1#S7.Thmteo9 "Theorem 7.9. ‣ 7 Estimation Of The Density Of 𝑀_𝑇 ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS"). As a direct consequence we find that, for every α>0\alpha>0,

|  |  |  |
| --- | --- | --- |
|  | limT→0ℙ​(MT≥b)Tα=0.\lim\_{T\to 0}\frac{\mathbb{P}(M\_{T}\geq b)}{T^{\alpha}}=0. |  |

The result now follows from applying Hölder’s inequality in C0bC\_{0}^{b}.
∎

## 8 Application To The Rough Bergomi Model

One of the main drawbacks of the main result we have given is that we are assuming that there exist two constants α,β\alpha,\beta such that α<σt<β\alpha<\sigma\_{t}<\beta and we have heavily relied on this hypothesis in order to derive the upper bound for ℙ​(supt∈[0,T]St≥B)\mathbb{P}(\sup\_{t\in[0,T]}S\_{t}\geq B). However, using an approximation argument, we aim to show that ℙ​(supt∈[0,T]St≥B)\mathbb{P}(\sup\_{t\in[0,T]}S\_{t}\geq B) approaches zero faster than any polynomial even though we don’t have an explicit estimation of such probability.

It is difficult to construct an approximation argument that works model-independently. Indeed, it is also hard to construct general approximation arguments even when studying European call options. We aim, therefore, to extend the result for one of the most popular rough volatility models. In this section we will apply the main result of this paper to prove that the faster-than-polynomial speed of convergence holds for the Rough Bergomi model. In this specific scenario we are assuming that the log-price is of the form

|  |  |  |
| --- | --- | --- |
|  | Xt=x−12​∫0tσs2​𝑑s+∫0tσs​𝑑ZsX\_{t}=x-\frac{1}{2}\int\_{0}^{t}\sigma\_{s}^{2}ds+\int\_{0}^{t}\sigma\_{s}dZ\_{s} |  |

where Zt=ρ​Wt+1−ρ2​BtZ\_{t}=\rho W\_{t}+\sqrt{1-\rho^{2}}B\_{t} and σ\sigma has the form

|  |  |  |
| --- | --- | --- |
|  | σt2=σ02​exp⁡(ν​WtH−ν2​t2​H2),WtH=2​H​∫0t(t−s)H−1/2​𝑑Ws.\sigma\_{t}^{2}=\sigma\_{0}^{2}\exp\left(\nu W^{H}\_{t}-\frac{\nu^{2}t^{2H}}{2}\right),\quad W^{H}\_{t}=\sqrt{2H}\int\_{0}^{t}(t-s)^{H-1/2}dW\_{s}. |  |

Notice that in this case we can’t apply the main result of this paper directly to σ\sigma because it is not true that there exist two constants α,β>0\alpha,\beta>0 such that α<σt<β\alpha<\sigma\_{t}<\beta almost surely. However, we can use a truncation argument to show that the speed of convergence of the probability of reaching the barrier is still faster than any polynomial. In order to do so, we consider the truncated log-price

|  |  |  |
| --- | --- | --- |
|  | Xtn=x−12​∫0t(σsn)2​𝑑s+∫0tσsn​𝑑ZsX\_{t}^{n}=x-\frac{1}{2}\int\_{0}^{t}(\sigma\_{s}^{n})^{2}ds+\int\_{0}^{t}\sigma\_{s}^{n}dZ\_{s} |  |

where

|  |  |  |
| --- | --- | --- |
|  | σtn=ϕn​(ν​WtH−ν2​t2​H2)\sigma^{n}\_{t}=\phi\_{n}\left(\nu W^{H}\_{t}-\frac{\nu^{2}t^{2H}}{2}\right) |  |

and ϕn​(x)\phi\_{n}(x) is defined as follows: consider ϕ​(x)=σ0​exp⁡(x)\phi(x)=\sigma\_{0}\exp(x). For every n>1n>1 we consider ϕn∈𝒞b2\phi\_{n}\in\mathcal{C}^{2}\_{b} satisfying ϕn​(x)=ϕ​(x)\phi\_{n}(x)=\phi(x) for all x∈[−n,n]x\in[-n,n], ϕn​(x)∈[ϕ​(−2​n)∨ϕ​(x),ϕ​(−n)]\phi\_{n}(x)\in[\phi(-2n)\vee\phi(x),\phi(-n)] for all x≤−nx\leq-n and ϕn​(x)∈[ϕ​(n),ϕ​(x)∨ϕ​(2​n)]\phi\_{n}(x)\in[\phi(n),\phi(x)\vee\phi(2n)] if x≥nx\geq n. We also define Stn=exp⁡(Xtn)S^{n}\_{t}=\exp(X\_{t}^{n}). Notice that for every fixed ε>0\varepsilon>0

|  |  |  |
| --- | --- | --- |
|  | ℙ(supt∈[0,T]St≥B)≤ℙ(supt∈[0,T]Stn≥B−ε)+ℙ(supt∈[0,T]|Stn−St|≥ε)=:A1+A2.\mathbb{P}(\sup\_{t\in[0,T]}S\_{t}\geq B)\leq\mathbb{P}(\sup\_{t\in[0,T]}S\_{t}^{n}\geq B-\varepsilon)+\mathbb{P}(\sup\_{t\in[0,T]}|S\_{t}^{n}-S\_{t}|\geq\varepsilon)=:A\_{1}+A\_{2}. |  |

We aim to show that for every fixed m>0m>0, limT→0T−m​ℙ​(supt∈[0,T]St≥B)=0\lim\_{T\to 0}T^{-m}\mathbb{P}(\sup\_{t\in[0,T]}S\_{t}\geq B)=0. Notice that, due to the main result of this paper, we have that

|  |  |  |
| --- | --- | --- |
|  | limT→0T−m​A1=limT→0T−m​ℙ​(supt∈[0,T]Stn≥B)=0.\lim\_{T\to 0}T^{-m}A\_{1}=\lim\_{T\to 0}T^{-m}\mathbb{P}(\sup\_{t\in[0,T]}S^{n}\_{t}\geq B)=0. |  |

Regarding A2A\_{2}, we use Chebyshev’s inequality and Doob’s martingale inequality to show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | A2≤\displaystyle A\_{2}\leq | 𝔼​[|supt∈[0,T]St−supt∈[0,T]Stn|p]εp\displaystyle\frac{\mathbb{E}\left[|\sup\_{t\in[0,T]}S\_{t}-\sup\_{t\in[0,T]}S\_{t}^{n}|^{p}\right]}{\varepsilon^{p}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼​[supt∈[0,T]|St−Stn|p]εp\displaystyle\frac{\mathbb{E}\left[\sup\_{t\in[0,T]}|S\_{t}-S\_{t}^{n}|^{p}\right]}{\varepsilon^{p}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 1εp​(pp−1)p​𝔼​[|ST−STn|p].\displaystyle\frac{1}{\varepsilon^{p}}\left(\frac{p}{p-1}\right)^{p}\mathbb{E}[|S\_{T}-S\_{T}^{n}|^{p}]. |  |

Finally, using the same argument as in Alòs and Shiraya, ([2019](https://arxiv.org/html/2510.15423v1#bib.bib2)), we can find p≥2p\geq 2 large enough such that limT→0T−m​A2=0\lim\_{T\to 0}T^{-m}A\_{2}=0. Therefore, for every fixed m>0m>0 we find that

|  |  |  |
| --- | --- | --- |
|  | limT→0ℙ​(supt∈[0,T]St≥B)Tm=0\lim\_{T\to 0}\frac{\mathbb{P}(\sup\_{t\in[0,T]}S\_{t}\geq B)}{T^{m}}=0 |  |

so C0bC\_{0}^{b} approaches zero faster than any polynomial even though the bound for ℙ​(supt∈[0,T]St≥B)\mathbb{P}(\sup\_{t\in[0,T]}S\_{t}\geq B) does not necessarily hold if the hypothesis α<σt<β\alpha<\sigma\_{t}<\beta fails.

In order to numerically visualize the difference between the asymptotic behaviours of both European call options and up-and-in barrier call options under the Rough Bergomi model, we will perform three different simulations: one in the In-The-Money case (ITM), one in the At-The-Money case (ATM) and the last one in the Out-The-Money case (OTM).

###### Example 8.1.

Consider SS following Model ([2.1](https://arxiv.org/html/2510.15423v1#S2.E1 "In 2 The Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS")) with S0=10S\_{0}=10 and K=9.5K=9.5, where the parameters of the model are ρ=−0.3\rho=-0.3, ν=0.5\nu=0.5 and H=0.2H=0.2. In this case, asymptotic behaviour of both options are displayed in Figure [1](https://arxiv.org/html/2510.15423v1#S8.F1 "Figure 1 ‣ Example 8.1. ‣ 8 Application To The Rough Bergomi Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS").

![Refer to caption](comparison_ITM.png)


Figure 1: ITM European and up-and-in call options

Notice that the price of the up-and-in barrier option tends to zero, while the price of the European call option tends to S0−K=0.5S\_{0}-K=0.5. Hence, the numerics are consistent with Jafari et al., ([2025](https://arxiv.org/html/2510.15423v1#bib.bib16)) and Theorem [4.1](https://arxiv.org/html/2510.15423v1#S4.Thmteo1 "Theorem 4.1. ‣ 4 Main Result ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS").

###### Example 8.2.

Consider SS following Model ([2.1](https://arxiv.org/html/2510.15423v1#S2.E1 "In 2 The Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS")) with S0=K=10S\_{0}=K=10 where the parameters of the model are ρ=−0.3\rho=-0.3, ν=0.5\nu=0.5 and H=0.2H=0.2. In this case, the asymptotic behaviour of both options are displayed in Figure [2](https://arxiv.org/html/2510.15423v1#S8.F2 "Figure 2 ‣ Example 8.2. ‣ 8 Application To The Rough Bergomi Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS").

![Refer to caption](comparison_ATM.png)


Figure 2: ATM European and up-and-in call options

###### Example 8.3.

Consider SS following Model ([2.1](https://arxiv.org/html/2510.15423v1#S2.E1 "In 2 The Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS")) with S0=10S\_{0}=10, K=11K=11 where the parameters of the model are ρ=−0.3\rho=-0.3, ν=0.5\nu=0.5 and H=0.2H=0.2. In this case, the asymptotic behaviour of both options are displayed in Figure [3](https://arxiv.org/html/2510.15423v1#S8.F3 "Figure 3 ‣ Example 8.3. ‣ 8 Application To The Rough Bergomi Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS").

![Refer to caption](comparison_OTM.png)


Figure 3: ATM European and up-and-in call options

Observe that in both Examples [8.2](https://arxiv.org/html/2510.15423v1#S8.Thmteo2 "Example 8.2. ‣ 8 Application To The Rough Bergomi Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS") and [8.3](https://arxiv.org/html/2510.15423v1#S8.Thmteo3 "Example 8.3. ‣ 8 Application To The Rough Bergomi Model ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS") both options converge to zero as T→0T\to 0 as it is stated in Jafari et al., ([2025](https://arxiv.org/html/2510.15423v1#bib.bib16)) and Theorem [4.1](https://arxiv.org/html/2510.15423v1#S4.Thmteo1 "Theorem 4.1. ‣ 4 Main Result ‣ ON THE SHORT-TIME BEHAVIOUR OF UP-AND-IN BARRIER OPTIONS USING MALLIAVIN CALCULUS"). Moreover, it is clearly visible that the speed of convergence of the up-and-in barrier call option is faster than the European one.

## 9 Conclusions

In this paper, we employed Malliavin calculus techniques to analyse the asymptotic behaviour of up-and-in barrier call options under a general stochastic volatility model. Drawing inspiration from the methodologies developed in Nualart and Vives, ([1988](https://arxiv.org/html/2510.15423v1#bib.bib22)) and Florit and Nualart, ([1995](https://arxiv.org/html/2510.15423v1#bib.bib10)) for Gaussian processes, as well as Dalang and Pu, ([2020](https://arxiv.org/html/2510.15423v1#bib.bib9)) and Pu, ([2018](https://arxiv.org/html/2510.15423v1#bib.bib23)) for the stochastic heat equation with additive noise, we studied the distribution of the supremum of an asset price governed by a general stochastic volatility process. These probabilistic insights were then applied to characterize the behaviour of up-and-in barrier call option prices, concluding in this way that the rate of convergence to zero of up-and-in barrier call options is faster than any polynomial of the time to maturity TT. In particular, under the Rough Bergomi model, we quantified the rate of decay and provided numerical evidence highlighting the faster convergence of barrier option prices compared to their European counterparts.

## Acknowledgements

I would like to express my sincere gratitude to Elisa Alòs and Josep Vives for their valuable discussions, insightful suggestions and careful reading of the manuscript. This work is supported by the program AGAUR-FI ajuts (2025 FI-1 00580).

## References

* Alòs et al., (2007)

  Alòs, E., León, J. A., and Vives, J. (2007).
  On the short-time behavior of the implied volatility for jump-diffusion models with stochastic volatility.
  Finance and Stochastics, 11(4):571–589.
* Alòs and Shiraya, (2019)

  Alòs, E. and Shiraya, K. (2019).
  Estimating the Hurst parameter from short term volatility swaps: a Malliavin calculus approach.
  Finance and Stochastics, 23(2):423–447.
* Bayer et al., (2016)

  Bayer, C., Friz, P., and Gatheral, J. (2016).
  Pricing under rough volatility.
  Quantitative Finance, 16(6):887–904.
* Brown et al., (2001)

  Brown, H., Hobson, D., and Rogers, L. C. G. (2001).
  Robust hedging of barrier options.
  Mathematical Finance. An International Journal of Mathematics, Statistics and Financial Economics, 11(3):285–314.
* Carrada-Herrera et al., (2013)

  Carrada-Herrera, R., Grudsky, S., Palomino-Jiménez, C., and Porter, R. M. (2013).
  Asymptotics of European double-barrier option with compound Poisson component.
  Communications in Mathematical Analysis, 14(2):40–66.
* Comte and Renault, (1998)

  Comte, F. and Renault, E. (1998).
  Long memory in continuous-time stochastic volatility models.
  Mathematical Finance, 8(04):291–323.
* (7)

  Dalang, R., Khoshnevisan, D., Mueller, C., Nualart, D., and Xiao, Y. (2009a).
  A minicourse on stochastic partial differential equations, volume 1962 of Lecture Notes in Mathematics.
  Springer-Verlag, Berlin.
  Held at the University of Utah, Salt Lake City, UT, May 8–19, 2006, Edited by Khoshnevisan and Firas Rassoul-Agha.
* (8)

  Dalang, R. C., Khoshnevisan, D., and Nualart, E. (2009b).
  Hitting probabilities for systems of non-linear stochastic heat equations with multiplicative noise.
  Probability Theory and Related Fields, 144(3):371–427.
* Dalang and Pu, (2020)

  Dalang, R. C. and Pu, F. (2020).
  On the density of the supremum of the solution to the linear stochastic heat equation.
  Stochastics and Partial Differential Equations. Analysis and Computations, 8(3):461–508.
* Florit and Nualart, (1995)

  Florit, C. and Nualart, D. (1995).
  A local criterion for smoothness of densities and application to the supremum of the Brownian sheet.
  Statistics & Probability Letters, 22(1):25–31.
* Fukasawa, (2017)

  Fukasawa, M. (2017).
  Short-time at-the-money skew and rough fractional volatility.
  Quantitative Finance, 17(02):189–198.
* Gatheral et al., (2018)

  Gatheral, J., Jaisson, T., and Rosenbaum, M. (2018).
  Volatility is rough.
  Quantitative Finance, 18(6):933–949.
* Heston, (1993)

  Heston, S. L. (1993).
  A closed-form solution for options with stochastic volatility with applications to bond and currency options.
  The Review of Financial Studies, 6(2):327–343.
* Hu and Knessl, (2010)

  Hu, F. and Knessl, C. (2010).
  Asymptotics of barrier option pricing under the CEV process.
  Applied Mathematical Finance, 17(3):261–300.
* Hull and White, (1987)

  Hull, J. and White, A. (1987).
  The pricing of options on assets with stochastic volatilities.
  Journal of Finance, 42:281–300.
* Jafari et al., (2025)

  Jafari, H., Burés, O., Vives, J., and Zhao, Y. Q. (2025).
  Option price asymptotics under a stochastic volatility Lévy model with infinite activity jumps.
  International Journal of Theoretical and Applied Finance, 28(1-2):Paper No. 2550006, 29.
* Kato et al., (2013)

  Kato, T., Takahashi, A., and Yamada, T. (2013).
  An asymptotic expansion formula for up-and-out barrier option price under stochastic volatility model.
  JSIAM Letters, 5:17–20.
* Kim and Pollard, (1990)

  Kim, J. and Pollard, D. (1990).
  Cube root asymptotics.
  The Annals of Statistics, 18(1):191–219.
* Kou, (2003)

  Kou, S. G. (2003).
  On pricing of discrete barrier options.
  Statistica Sinica, pages 955–964.
* Nourdin and Viens, (2009)

  Nourdin, I. and Viens, F. G. (2009).
  Density formula and concentration inequalities with Malliavin calculus.
  Electronic Journal of Probability, 14:no. 78, 2287–2309.
* Nualart, (2006)

  Nualart, D. (2006).
  The Malliavin calculus and related topics.
  Probability and its Applications (New York). Springer-Verlag, Berlin, second edition.
* Nualart and Vives, (1988)

  Nualart, D. and Vives, J. (1988).
  Continuité absolue de la loi du maximum d’un processus continu.
  Comptes Rendus des Séances de l’Académie des Sciences. Série I. Mathématique, 307(7):349–354.
* Pu, (2018)

  Pu, F. (2018).
  The stochastic heat equation: hitting probabilities and the probability density function of the supremum via Malliavin calculus.
  PhD thesis, EPFL.
* Stein and Stein, (1991)

  Stein, E. M. and Stein, J. C. (1991).
  Stock price distributions with stochastic volatility: An analytic approach.
  The Review of Financial Studies, 4:727–752.
* Üstünel, (2010)

  Üstünel, A. S. (2010).
  Analysis on Wiener space and applications.
  arXiv preprint arXiv:1003.1649.
* Wiggins, (1987)

  Wiggins, J. (1987).
  Option values under stochastic volatilities.
  Journal of Financial Economics, 19:351–372.
* Zvan et al., (2000)

  Zvan, R., Vetzal, K. R., and Forsyth, P. A. (2000).
  PDE methods for pricing barrier options.
  Journal of Economic Dynamics and Control, 24(11-12):1563–1590.