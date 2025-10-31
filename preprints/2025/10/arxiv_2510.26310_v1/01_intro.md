---
authors:
- Elisa Alos
- Frido Rolloos
- Kenichiro Shiraya
doc_id: arxiv:2510.26310v1
family_id: arxiv:2510.26310
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Estimating the Hurst parameter from the zero vanna implied volatility and its
  dual
url_abs: http://arxiv.org/abs/2510.26310v1
url_html: https://arxiv.org/html/2510.26310v1
venue: arXiv q-fin
version: 1
year: 2025
---


Elisa Alòs  Frido Rolloos  Kenichiro Shiraya
Department of Economics and Business, University Pompeu Fabra, and Barcelona GSE. Supported by grant MEC MTM 2016-76420-PGraduate School of Economics, The University of Tokyo. Supported by CARF.

###### Abstract

The covariance between the return of an asset and its realized volatility can be approximated as the difference between two specific implied volatilities. In this paper it is proved that in the small time-to-maturity limit the approximation error tends to zero. In addition a direct relation between the short time-to-maturity covariance and slope of the at-the-money implied volatility is established. The limit theorems are valid for stochastic volatility models with Hurst parameter H∈(0,1)H\in(0,1). An application of the results is to accurately approximate the Hurst parameter using only a discrete set of implied volatilities. Numerical examples under the rough Bergomi model are presented.

Keywords: Malliavin calculus, fractional volatility models, implied volatility, skew, covariance.

AMS subject classification: 91G99

## 1 Introduction

In Rolloos [[10](https://arxiv.org/html/2510.26310v1#bib.bib10)] an approximation is derived that relates the covariance between price returns and realized volatility to the difference between two specific implied volatilities:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Et​[(STSt−1)​1T−t​∫tTσu2​𝑑u]≈I​(kt,T+)−I​(kt,T−)≈I2​(kt,T∗)​(T−t)​∂I​(kt,T∗)∂kE\_{t}\left[\left(\frac{S\_{T}}{S\_{t}}-1\right)\sqrt{\frac{1}{T-t}\int\_{t}^{T}\sigma\_{u}^{2}du}\,\right]\approx I(k\_{t,T}^{+})-I(k\_{t,T}^{-})\approx I^{2}(k\_{t,T}^{\*})(T-t)\frac{\partial I(k\_{t,T}^{\*})}{\partial k} |  | (1.1) |

Here StS\_{t} denotes the asset price, σt\sigma\_{t} its instantaneous volatility, I​(kt,T−)I(k\_{t,T}^{-}) the implied volatility (IV) corresponding to the (log)strike where the Black-Scholes-Merton (BS) vanna and volga of a vanilla option with maturity date TT is zero, I​(kt,T+)I(k\_{t,T}^{+}) the IV corresponding to the strike where the BS volga is zero but the BS vanna is nonzero, and I​(kt,T∗)I(k\_{t,T}^{\*}) is the at-the-money forward (ATM) IV. Notice that the strikes kt,T±,kt,T∗k\_{t,T}^{\pm},k\_{t,T}^{\*} are floating strikes, not fixed strikes.

The approximations ([1.1](https://arxiv.org/html/2510.26310v1#S1.E1 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) are of use to the practitioner for several reasons. For example, in contrast to other more ad-hoc measures of skew such as the difference between the IVs of 90% and 110% moneyness, the difference between I​(kt,T+)I(k\_{t,T}^{+}) and I​(kt,T−)I(k\_{t,T}^{-}) has a clear link to covariance. This means that by observing the difference between the two implied volatilities I​(kt,T±)I(k\_{t,T}^{\pm}) the practitioner can obtain an estimate for the implied covariance between price return and realized volatility. They can then compare the implied measure to subsequent realized covariance and infer whether on average the skew contains a premium. Furthermore, since for small times to maturity the covariance is directly proportional to the ATM slope the approximation complements other results that relates the ATM skew to statistical measures. One such result was obtained by Backus et al. [[3](https://arxiv.org/html/2510.26310v1#bib.bib3)] which states that for short times to maturity the ATM skew is approximately the skewness of the distribution of the asset log returns.

As we shall demonstrate the approximations ([1.1](https://arxiv.org/html/2510.26310v1#S1.E1 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) also enable accurate approximation of the Hurst parameter HH using only a discrete set of IVs. To see this recall that as has been shown by Alòs et al. [[1](https://arxiv.org/html/2510.26310v1#bib.bib1)] and Fukasawa [[5](https://arxiv.org/html/2510.26310v1#bib.bib5), [6](https://arxiv.org/html/2510.26310v1#bib.bib6)] the short time-to-maturity (T−t≪1)(T-t\ll 1) ATM skew has the following property:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂I​(kt,T∗)∂k∝(T−t)H−12.\frac{\partial I(k\_{t,T}^{\*})}{\partial k}\propto(T-t)^{H-\frac{1}{2}}. |  | (1.2) |

It follows from the above and ([1.1](https://arxiv.org/html/2510.26310v1#S1.E1 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | H≈−12+ln⁡(I​(kt,T1+)−I​(kt,T1−)I​(kt,T2+)−I​(kt,T2−)​I2​(kt,T2∗)I2​(kt,T1∗))ln⁡(T1−tT2−t)H\approx-\frac{1}{2}+\frac{\ln\left(\frac{I(k\_{t,T\_{1}}^{+})-I(k\_{t,T\_{1}}^{-})}{I(k\_{t,T\_{2}}^{+})-I(k\_{t,T\_{2}}^{-})}\frac{I^{2}(k\_{t,T\_{2}}^{\*})}{I^{2}(k\_{t,T\_{1}}^{\*})}\right)}{\ln\left(\frac{T\_{1}-t}{T\_{2}-t}\right)} |  | (1.3) |

This approximation for the Hurst parameter is appealing because it does not depend on specific model parameters. Hence, it can be used without first calibrating a specific stochastic volatility model. If volatility is indeed driven by fractional noise, as put forward by among others Comte and Renault [[4](https://arxiv.org/html/2510.26310v1#bib.bib4)] for H>1/2H>1/2 and Gatheral et al. [[7](https://arxiv.org/html/2510.26310v1#bib.bib7)] for H<1/2H<1/2, then the approximation ([1.3](https://arxiv.org/html/2510.26310v1#S1.E3 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) provides a straightforward way to estimate the Hurst parameter from the IV surface. Note also that our estimation of HH is easier to carry out than using short-dated volatility swaps (Alòs and Shiraya [[2](https://arxiv.org/html/2510.26310v1#bib.bib2)]) since volatility swaps are illiquid.

In spite of the practical usefulness of the approximations, Rolloos does not give any insight into the approximation errors. This is due to the fact that the approximations were derived by Taylor expansions of the ‘mixing’ formula due to Hull and White [[8](https://arxiv.org/html/2510.26310v1#bib.bib8)], Romano and Touzi [[11](https://arxiv.org/html/2510.26310v1#bib.bib11)], and Willard [[12](https://arxiv.org/html/2510.26310v1#bib.bib12)]. Even though a Taylor expansion is straightforward, in this particular case it is unable to give information on the approximation errors. In contrast, techniques from Malliavin calculus have been shown to be quite powerful in proving limit theorems and providing error bounds. This is the main contribution of our paper: by using techniques from Malliavin calculus we will prove limit theorems for the approximations ([1.1](https://arxiv.org/html/2510.26310v1#S1.E1 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")).

The paper is structured as follows. In Section 2 the main assumptions are stated and notation introduced. This is followed by Section 3 in which the main limit theorems concerning the difference between an arbitrary IV and the volatility swap strike, and the difference between I​(kt,T+)I(k\_{t,T}^{+}) and I​(kt,T−)I(k\_{t,T}^{-}) are proved. The approximations stated above then follow from the main theorems. In Section 4 we present numerical examples where the rough Bergomi model is taken as benchmark skew generating model. The accuracy of approximations ([1.1](https://arxiv.org/html/2510.26310v1#S1.E1 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) and ([1.3](https://arxiv.org/html/2510.26310v1#S1.E3 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) are then examined. The final section concludes.

## 2 The main problem and notations

This paper assumes a stochastic volatility model for a log asset price Xt:=log⁡StX\_{t}:=\log S\_{t} under the risk-neutral probability measure PP.
The dynamics is described by the following stochastic differential equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=X0−12​∫0tσs2​𝑑s+∫0tσs​(ρ​d​Ws+1−ρ2​d​Bs),t∈[0,T].X\_{t}=X\_{0}-\frac{1}{2}\int\_{0}^{t}{\sigma\_{s}^{2}}ds+\int\_{0}^{t}\sigma\_{s}\left(\rho dW\_{s}+\sqrt{1-\rho^{2}}dB\_{s}\right),\quad t\in[0,T]. |  | (2.1) |

In this formulation X0X\_{0} represents the initial log asset price and the dynamics are driven by two independent standard Brownian motions, WW and BB, on a complete probability space (Ω,𝒢,P)(\Omega,\mathcal{G},P).
The filtrations generated by WW and BB are denoted by ℱW\mathcal{F}^{W} and ℱB\mathcal{F}^{B}, respectively, with ℱ\mathcal{F} representing their joint filtration, ℱ:=ℱW∨ℱB\mathcal{F}:=\mathcal{F}^{W}\vee\mathcal{F}^{B}.
The volatility component, σ\sigma, is a square-integrable and right-continuous stochastic process that is adapted to ℱW\mathcal{F}^{W}.
For the sake of analytical simplicity, we assume a zero interest rate (r=0r=0). However, the core arguments of this study remain valid even when r≠0r\neq 0.

Under this framework the value of a European call option with strike price KK is determined by its conditional expectation, as expressed by the following equality:

|  |  |  |
| --- | --- | --- |
|  | Vt=Et​[(eXT−K)+],V\_{t}=E\_{t}[(e^{X\_{T}}-K)\_{+}], |  |

where EtE\_{t} signifies the ℱt\mathcal{F}\_{t}-conditional expectation with respect to measure PP.

The quantity vt=1T−t​∫tTσu2​𝑑uv\_{t}=\sqrt{\frac{1}{T-t}\int\_{t}^{T}\sigma\_{u}^{2}du} s the future average volatility over the time to maturity of the option, and this process is not adapted.
Its conditional expectation, Et​[vt]E\_{t}\left[v\_{t}\right], is known as the fair strike of a volatility swap with maturity TT.

The price of a European call option in the Black-Scholes model is given by the function B​S​(t,T,x,k,σ)BS(t,T,x,k,\sigma), assuming constant volatility σ\sigma, an initial asset price exe^{x}, a time to maturity T−tT-t, and a strike price K=exp⁡(k)K=\exp(k).
For the special case of zero interest rate we recall that the formula is:

|  |  |  |
| --- | --- | --- |
|  | B​S​(t,T,x,k,σ)=ex​N​(d1​(k,σ))−ek​N​(d2​(k,σ)),BS(t,T,x,k,\sigma)=e^{x}N(d\_{1}(k,\sigma))-e^{k}N(d\_{2}(k,\sigma)), |  |

Here, NN is the cumulative distribution function for a standard normal variable, with the parameters d1d\_{1} and d2d\_{2} defined as:

|  |  |  |
| --- | --- | --- |
|  | d1​(k,σ):=x−kσ​T−t+σ2​T−t,d2​(k,σ):=x−kσ​T−t−σ2​T−t.d\_{1}\left(k,\sigma\right):=\frac{x-k}{\sigma\sqrt{T-t}}+\frac{\sigma}{2}\sqrt{T-t},\hskip 11.38092ptd\_{2}\left(k,\sigma\right):=\frac{x-k}{\sigma\sqrt{T-t}}-\frac{\sigma}{2}\sqrt{T-t}. |  |

For convenience we occasionally simplify the notation by writing

|  |  |  |
| --- | --- | --- |
|  | B​S​(k,σ):=B​S​(t,T,Xt,k,σ).BS(k,\sigma):=BS(t,T,X\_{t},k,\sigma). |  |

We also define the inverse Black-Scholes function, B​S−1​(t,T,x,k,⋅)BS^{-1}(t,T,x,k,\cdot), with respect to the volatility parameter such that

|  |  |  |
| --- | --- | --- |
|  | B​S​(t,T,x,k,B​S−1​(t,T,x,k,λ))=λ,BS(t,T,x,k,BS^{-1}(t,T,x,k,\lambda))=\lambda, |  |

for all λ>0\lambda>0.
On occasion we use the following compact notation:

|  |  |  |
| --- | --- | --- |
|  | B​S−1​(k,λ):=B​S−1​(t,T,Xt,k,λ).BS^{-1}(k,\lambda)\ :=BS^{-1}(t,T,X\_{t},k,\lambda). |  |

The implied volatility I​(t,T,Xt,k)I(t,T,X\_{t},k) is defined for any fixed set of parameters t,T,Xt,kt,T,X\_{t},k as the unique volatility value that equates the Black-Scholes price to the market price:

|  |  |  |
| --- | --- | --- |
|  | B​S​(t,T,Xt,k,I​(t,T,Xt,k))=Vt.BS(t,T,X\_{t},k,I(t,T,X\_{t},k))=V\_{t}. |  |

It follows directly that

|  |  |  |
| --- | --- | --- |
|  | I​(t,T,Xt,k)=B​S−1​(t,T,Xt,k,Vt).I(t,T,X\_{t},k)=BS^{-1}(t,T,X\_{t},k,V\_{t}). |  |

We define kt∗:=Xtk\_{t}^{\*}:=X\_{t} is the ATM strike at time tt and I​(t,T,Xt,kt∗)I(t,T,X\_{t},k^{\*}\_{t}) the ATM IV. When interest rate is nonzero then the ATM strike depends on time to maturity TT as well. However, under our assumptions there is no dependence on TT.

The zero vanna strike at time tt for maturity date TT is the strike kt,T−k^{-}\_{t,T} for which the Black-Scholes vanna vanishes, i.e.,

|  |  |  |
| --- | --- | --- |
|  | d2​(kt,T−,I​(t,T,Xt,kt,T−))=0.d\_{2}(k^{-}\_{t,T},I(t,T,X\_{t},k^{-}\_{t,T}))=0. |  |

The Black-Scholes vanna is defined as the first-order partial derivative of the option’s delta with respect to the implied volatility and is proportional to d2d\_{2}.
The implied volatility I​(t,T,Xt,kt,T−)I(t,T,X\_{t},k^{-}\_{t,T}) is referred to as the zero vanna implied volatility. A similar definition applies to I​(t,T,Xt,kt,T+)I(t,T,X\_{t},k^{+}\_{t,T}) and kt,T+k^{+}\_{t,T}, where d1​(kt,T+,I​(t,T,Xt,kt,T+))=0d\_{1}(k^{+}\_{t,T},I(t,T,X\_{t},k^{+}\_{t,T}))=0. The strike kt,T+k^{+}\_{t,T} is called the dual zero vanna strike and the corresponding implied volatility I​(t,T,Xt,kt,T+)I(t,T,X\_{t},k^{+}\_{t,T}) is the dual zero vanna implied volatility.

Even when interest rate and dividend yield are zero the zero vanna strike and its dual depend on time to maturity TT. For the sake of notational economy, when not considering multiple maturities we shall henceforth drop the dependence of these strikes on TT and only reintroduce it in the section on numerical results.

We introduce also the following notations:

|  |  |  |
| --- | --- | --- |
|  | Λr−:=Er​[B​S​(t,T,Xt,kt,T−,vt)],Λr+:=Er​[B​S​(t,T,Xt,kt,T+,vt)].\Lambda^{-}\_{r}:=E\_{r}\left[BS(t,T,X\_{t},k^{-}\_{t,T},v\_{t})\right],\hskip 11.38092pt\Lambda^{+}\_{r}:=E\_{r}\left[BS(t,T,X\_{t},k^{+}\_{t,T},v\_{t})\right]. |  |

We also define Θr​(k):=B​S−1​(k,Λr)\Theta\_{r}(k):=BS^{-1}(k,\Lambda\_{r}), and note that

|  |  |  |
| --- | --- | --- |
|  | Θt​(kt,T)=I​(t,Xt,kt,T,Vt),ΘT​(kt,T±)=vt.\Theta\_{t}(k\_{t,T})=I(t,X\_{t},k\_{t,T},V\_{t}),\hskip 11.38092pt\Theta\_{T}(k^{\pm}\_{t,T})=v\_{t}. |  |

Finally, we define the following operators on the Black-Scholes function:

|  |  |  |
| --- | --- | --- |
|  | G​(t,T,x,k,σ):=(∂2∂x2−∂∂x)​B​S​(t,T,x,k,σ),H​(t,T,x,k,σ):=(∂3∂x3−∂2∂x2)​B​S​(t,T,x,k,σ).G(t,T,x,k,\sigma):=\left(\frac{\partial^{2}}{\partial x^{2}}-\frac{\partial}{\partial x}\right)BS(t,T,x,k,\sigma),\hskip 11.38092ptH(t,T,x,k,\sigma):=\left(\frac{\partial^{3}}{\partial x^{3}}-\frac{\partial^{2}}{\partial x^{2}}\right)BS(t,T,x,k,\sigma). |  |

The methodology for the remainder of this paper is grounded in Malliavin calculus. The domain of the Malliavin derivative operator DWD^{W} with respect to the Brownian motion WW is denoted by 𝔻W1,2\mathbb{D}\_{W}^{1,2}. For n>1n>1, the domains for the iterated derivatives Dn,WD^{n,W} is denoted by 𝔻Wn,2\mathbb{D}\_{W}^{n,2}. We also utilize the notation 𝕃Wn,2=L2​([0,T];𝔻Wn,2)\mathbb{L}\_{W}^{n,2}=L^{2}\left(\left[0,T\right];\mathbb{D}\_{W}^{n,2}\right).

## 3 Limit theorems

In this section the main assumptions and theorems are stated. Due to the length of the proofs of the theorems they have been placed in the appendix. The proofs of the corollaries are sufficiently short to be kept in the main text. Let us then first state our hypotheses:

(H1)
:   There exist two positive constants a,ba,b such that a≤σt≤b,a\leq\sigma\_{t}\leq b, for all t∈[0,T].t\in\left[0,T\right].

(H2)
:   σ∈𝕃W3,2\sigma\in\mathbb{L}^{3,2}\_{W} and there exists two constants ν>0\nu>0 and H∈(0,1)H\in(0,1) such that, for all 0<r<u,s,θ<T0<r<u,s,\theta<T

    |  |  |  |
    | --- | --- | --- |
    |  | |Er​[DrW​σs2]|≤ν​(s−r)H−12,|Er​[DθW​DrW​σs2]|≤ν2​(s−r)H−12​(s−θ)H−12,|E\_{r}[D\_{r}^{W}\sigma\_{s}^{2}]|\leq\nu(s-r)^{H-\frac{1}{2}},\hskip 8.5359pt|E\_{r}[D\_{\theta}^{W}D\_{r}^{W}\sigma\_{s}^{2}]|\leq\nu^{2}(s-r)^{H-\frac{1}{2}}(s-\theta)^{H-\frac{1}{2}}, |  |

    and

    |  |  |  |
    | --- | --- | --- |
    |  | |Er​[DuW​DθW​DrW​σs2]|≤ν3​(s−r)H−12​(s−θ)H−12​(s−u)H−12.|E\_{r}[D\_{u}^{W}D\_{\theta}^{W}D\_{r}^{W}\sigma\_{s}^{2}]|\leq\nu^{3}(s-r)^{H-\frac{1}{2}}(s-\theta)^{H-\frac{1}{2}}(s-u)^{H-\frac{1}{2}}. |  |

(H3)
:   Hypotheses (H1), (H2’), hold and the terms

    |  |  |  |
    | --- | --- | --- |
    |  | 1(T−t)3+2​H​Et​[(∫tT∫sTDsW​σr2​𝑑r​𝑑s)2],\frac{1}{(T-t)^{3+2H}}E\_{t}\left[\left(\int\_{t}^{T}\int\_{s}^{T}D\_{s}^{W}\sigma\_{r}^{2}drds\right)^{2}\right], |  |

    |  |  |  |
    | --- | --- | --- |
    |  | 1(T−t)2+2​H​Et​[∫tT∫sTDsW​σr​∫rTDrW​σu2​𝑑u​𝑑r​𝑑s],\frac{1}{(T-t)^{2+2H}}E\_{t}\left[\int\_{t}^{T}\int\_{s}^{T}D\_{s}^{W}\sigma\_{r}\int\_{r}^{T}D\_{r}^{W}\sigma\_{u}^{2}dudrds\right], |  |

    |  |  |  |
    | --- | --- | --- |
    |  | 1(T−t)2+2​H​Et​[∫tT∫sT∫rTDsW​DrW​σu2​𝑑u​𝑑r​𝑑s]\frac{1}{(T-t)^{2+2H}}E\_{t}\left[\int\_{t}^{T}\int\_{s}^{T}\int\_{r}^{T}D\_{s}^{W}D\_{r}^{W}\sigma\_{u}^{2}dudrds\right] |  |

    have a finite limit as T→t.T\rightarrow t.

The following result follows from the same argument as Proposition 4.1 in Alòs and Shiraya (2019) and serves as the main tool in this section.

###### Proposition 1.

Consider the model ([2.1](https://arxiv.org/html/2510.26310v1#S2.E1 "In 2 The main problem and notations ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) and assume
that hypotheses (H1), (H2) and hold for some H∈(0,1)H\in(0,1). Then,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | I​(t,T,Xt,k)\displaystyle I\left(t,T,X\_{t},{k}\right) | =\displaystyle= | I0​(t,T,Xt,k)\displaystyle I^{0}\left(t,T,X\_{t},{k}\right) |  | (3.1) |
|  |  |  | +ρ2​Et​[∫tT(B​S−1)′​(k,Γs)​H​(s,T,Xs,k,vs)​Φs​𝑑s]\displaystyle+\frac{\rho}{2}E\_{t}\left[\int\_{t}^{T}(BS^{-1})^{\prime}(k,\Gamma\_{s})H(s,T,X\_{s},{k},v\_{s})\Phi\_{s}ds\right] |  |

where I0​(t,T,Xt,k)I^{0}(t,T,X\_{t},k) denotes the implied
volatility in the uncorrelated case ρ=0\rho=0,

|  |  |  |
| --- | --- | --- |
|  | Γs:=Et​[B​S​(t,T,Xt,k,vt)]+ρ2​Et​[∫tsH​(r,T,Xr,k,vr)​Φr​𝑑r],\Gamma\_{s}:=E\_{t}[BS(t,T,X\_{t},k,v\_{t})]+\frac{\rho}{2}E\_{t}\left[\int\_{t}^{s}H(r,T,X\_{r},k,v\_{r})\Phi\_{r}dr\right], |  |

and Φt:=σt​∫tTDtW​σr2​𝑑r.\Phi\_{t}:=\sigma\_{t}\int\_{t}^{T}D\_{t}^{W}\sigma\_{r}^{2}dr.

By making use of Proposition [1](https://arxiv.org/html/2510.26310v1#Thmtheorem1 "Proposition 1. ‣ 3 Limit theorems ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual") we can prove the following.

###### Proposition 2.

Consider the model ([2.1](https://arxiv.org/html/2510.26310v1#S2.E1 "In 2 The main problem and notations ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) and assume
that hypotheses (H1), (H2’) and (H3) hold for some H∈(0,1)H\in(0,1). Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I​(t,T,Xt,k)−Et​(vt)\displaystyle I\left(t,T,X\_{t},k\right)-E\_{t}\left(v\_{t}\right) | | |  |
|  |  | =\displaystyle= | I0​(t,T,Xt,k)−Et​[vt]\displaystyle I^{0}\left(t,T,X\_{t},k\right)-E\_{t}\left[v\_{t}\right] |  |
|  |  |  | +ρ2Et[H(t,Xt,k,vt)Ut(k)\displaystyle+\frac{\rho}{2}E\_{t}\left[H(t,X\_{t},k,v\_{t})U\_{t}(k)\right. |  |
|  |  |  | +ρ24Et[∫tT∂∂x(∂2∂x2−∂∂x)H(s,Xs,k,vs)σs(∫sTDsWσr2dr)Us(k)ds\displaystyle+\frac{\rho^{2}}{4}E\_{t}\left[\int\_{t}^{T}\frac{\partial}{\partial x}\left(\frac{\partial^{2}}{\partial x^{2}}-\frac{\partial}{\partial x}\right)H(s,X\_{s},k,v\_{s})\sigma\_{s}\left(\int\_{s}^{T}D\_{s}^{W}\sigma\_{r}^{2}dr\right)U\_{s}(k)ds\right. |  |
|  |  |  | +∫tT∂∂xH(s,Xs,k,vs)(∫sT(BS−1)′(k,Γr)(DsWΦr)dr)σsds]\displaystyle\left.+\int\_{t}^{T}\frac{\partial}{\partial x}H(s,X\_{s},k,v\_{s})\left(\int\_{s}^{T}\left(BS^{-1}\right)^{\prime}\left(k,\Gamma\_{r}\right)\left(D\_{s}^{W}\Phi\_{r}\right)dr\right)\sigma\_{s}ds\right] |  |

where Ut​(k)=∫tT(B​S−1)′​(k,Γs)​Φs​𝑑sU\_{t}(k)=\int\_{t}^{T}\left(BS^{-1}\right)^{\prime}\left(k,\Gamma\_{s}\right)\Phi\_{s}ds.

We can now state and prove our main theorem.

###### Theorem 3.

Consider the model ([2.1](https://arxiv.org/html/2510.26310v1#S2.E1 "In 2 The main problem and notations ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) and assume that hypotheses (H1), (H2’) and (H3) hold for some H∈(0,1)H\in(0,1). Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | limT→tI​(t,T,Xt,kt,T+)−I​(t,T,Xt,kt,T−)(T−t)H+12\displaystyle\lim\_{T\rightarrow t}\frac{I(t,T,X\_{t},k^{+}\_{t,T})-I(t,T,X\_{t},k^{-}\_{t,T})}{(T-t)^{H+\frac{1}{2}}} | =\displaystyle= | ρ2​limT→t1(T−t)H+32​∫tT(∫sTDsW​σr2​𝑑r)​𝑑s.\displaystyle\frac{\rho}{2}\lim\_{T\rightarrow t}\frac{1}{(T-t)^{H+\frac{3}{2}}}\int\_{t}^{T}\left(\int\_{s}^{T}D\_{s}^{W}\sigma\_{r}^{2}dr\right)ds. |  |

From the main theorem the following set of corollaries easily follow. The corollaries contain the results that we will be looking at in the section on numerics.

###### Corollary 4.

In the short time-to-maturity limit

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→tI​(t,T,Xt,kt,T+)−I​(t,T,Xt,kt,T−)(T−t)H+12=σt2​limT→t1(T−t)H−12​∂I∂k​(kt,T∗).\lim\_{T\rightarrow t}\frac{I(t,T,X\_{t},k^{+}\_{t,T})-I(t,T,X\_{t},k^{-}\_{t,T})}{(T-t)^{H+\frac{1}{2}}}=\sigma\_{t}^{2}\lim\_{T\to t}\frac{1}{(T-t)^{H-\frac{1}{2}}}\frac{\partial I}{\partial k}(k^{\*}\_{t,T}). |  | (3.2) |

Thus, for short time-to-maturity the following approximation holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(t,T,Xt,kt,T+)−I​(t,T,Xt,kt,T−)≈σt2​(T−t)​∂I∂k​(kt,T∗).I(t,T,X\_{t},k^{+}\_{t,T})-I(t,T,X\_{t},k^{-}\_{t,T})\approx\sigma\_{t}^{2}(T-t)\frac{\partial I}{\partial k}(k^{\*}\_{t,T}). |  | (3.3) |

###### Proof.

Notice that, from the results in Alòs et al. [[1](https://arxiv.org/html/2510.26310v1#bib.bib1)] we know that

|  |  |  |
| --- | --- | --- |
|  | limT→t(T−t)12−H​∂I∂k​(kt,T∗)=ρ2​σt2​limT→t1(T−t)H+32​∫tT(∫sTDsW​σr2​𝑑r)​𝑑s.\lim\_{T\to t}(T-t)^{\frac{1}{2}-H}\frac{\partial I}{\partial k}(k^{\*}\_{t,T})=\frac{\rho}{2\sigma\_{t}^{2}}\lim\_{T\rightarrow t}\frac{1}{(T-t)^{H+\frac{3}{2}}}\int\_{t}^{T}\left(\int\_{s}^{T}D\_{s}^{W}\sigma\_{r}^{2}dr\right)ds. |  |

Jointly with Theorem [3](https://arxiv.org/html/2510.26310v1#Thmtheorem3 "Theorem 3. ‣ 3 Limit theorems ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual") gives us the result.
∎

###### Corollary 5.

In the small time-to-maturity limit

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→tI​(t,T,Xt,kt,T+)−I​(t,T,Xt,kt,T−)(T−t)H+12=12​σt​limT→t1(T−t)H+12​Et​[(ST−StSt)​1(T−t)​∫tTσr2​𝑑r].\lim\_{T\rightarrow t}\frac{I(t,T,X\_{t},k^{+}\_{t,T})-I(t,T,X\_{t},k^{-}\_{t,T})}{(T-t)^{H+\frac{1}{2}}}=\frac{1}{2\sigma\_{t}}\lim\_{T\to t}\frac{1}{(T-t)^{H+\frac{1}{2}}}E\_{t}\left[\left(\frac{S\_{T}-S\_{t}}{S\_{t}}\right)\frac{1}{(T-t)}\int\_{t}^{T}\sigma\_{r}^{2}dr\right]. |  | (3.4) |

Thus, for short time-to-maturity the following approximation holds:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(t,T,Xt,kt,T+)−I​(t,T,Xt,kt,T−)≈12​σt​Et​[(ST−StSt)​1(T−t)​∫tTσr2​𝑑r].I(t,T,X\_{t},k^{+}\_{t,T})-I(t,T,X\_{t},k^{-}\_{t,T})\approx\frac{1}{2\sigma\_{t}}E\_{t}\left[\left(\frac{S\_{T}-S\_{t}}{S\_{t}}\right)\frac{1}{(T-t)}\int\_{t}^{T}\sigma\_{r}^{2}dr\right]. |  | (3.5) |

###### Proof.

Assume the model ([2.1](https://arxiv.org/html/2510.26310v1#S2.E1 "In 2 The main problem and notations ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")). Then

|  |  |  |
| --- | --- | --- |
|  | ST=St+∫tTσr​Sr​(ρ​d​Wr+1−ρ2​d​Br).S\_{T}=S\_{t}+\int\_{t}^{T}\sigma\_{r}S\_{r}\left(\rho dW\_{r}+\sqrt{1-\rho^{2}}dB\_{r}\right). |  |

On the other hand, a direct application of the Clark-Ocone-Haussman theorem gives us that (see for example Alòs and García-Lorite (2024))

|  |  |  |
| --- | --- | --- |
|  | ∫tTσr2​𝑑r=Et​[∫tTσr2​𝑑r]+∫tT∫rTEr​[DrW​σu2]​𝑑u​𝑑Wr.\int\_{t}^{T}\sigma\_{r}^{2}dr=E\_{t}\left[\int\_{t}^{T}\sigma\_{r}^{2}dr\right]+\int\_{t}^{T}\int\_{r}^{T}E\_{r}[D\_{r}^{W}\sigma\_{u}^{2}]dudW\_{r}. |  |

Then,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Et​[(ST−StSt)​1T−t​∫tTσr2​𝑑r]\displaystyle E\_{t}\left[\left(\frac{S\_{T}-S\_{t}}{S\_{t}}\right)\frac{1}{T-t}\int\_{t}^{T}\sigma\_{r}^{2}dr\right] | | |  | (3.6) |
|  |  | =\displaystyle= | ρSt​Et​[(∫tTσr​Sr​𝑑Wr)​1T−t​(∫tT∫rTEr​(DrW​σu2)​𝑑u​𝑑Wr)]\displaystyle\frac{\rho}{S\_{t}}E\_{t}\left[\left(\int\_{t}^{T}\sigma\_{r}S\_{r}dW\_{r}\right)\frac{1}{T-t}\left(\int\_{t}^{T}\int\_{r}^{T}E\_{r}(D\_{r}^{W}\sigma\_{u}^{2})dudW\_{r}\right)\right] |  |
|  |  | =\displaystyle= | ρSt​Et​[∫tTσr​Sr​1T−t​(∫rTEr​[DrW​σu2]​𝑑u)​𝑑r].\displaystyle\frac{\rho}{S\_{t}}E\_{t}\left[\int\_{t}^{T}\sigma\_{r}S\_{r}\frac{1}{T-t}\left(\int\_{r}^{T}E\_{r}[D\_{r}^{W}\sigma\_{u}^{2}]du\right)dr\right]. |  |

Together with Theorem [3](https://arxiv.org/html/2510.26310v1#Thmtheorem3 "Theorem 3. ‣ 3 Limit theorems ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual") this proves the corollary.
∎

###### Corollary 6.

In the small time-to-maturity limit

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→tI​(t,T,Xt,kt,T+)−I​(t,T,Xt,kt,T−)(T−t)H+12=limT→t1(T−t)H+12​Et​[ST−StSt​1T−t​∫tTσr2​𝑑r].\lim\_{T\rightarrow t}\frac{I(t,T,X\_{t},k^{+}\_{t,T})-I(t,T,X\_{t},k^{-}\_{t,T})}{(T-t)^{H+\frac{1}{2}}}=\lim\_{T\to t}\frac{1}{(T-t)^{H+\frac{1}{2}}}E\_{t}\left[\frac{S\_{T}-S\_{t}}{S\_{t}}\sqrt{\frac{1}{T-t}\int\_{t}^{T}\sigma\_{r}^{2}dr}\right]. |  | (3.7) |

That is, for short times to maturity

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(t,T,Xt,kt,T+)−I​(t,T,Xt,kt,T−)(T−t)H+12≈1(T−t)H+12​Et​[ST−StSt​1T−t​∫tTσr2​𝑑r].\frac{I(t,T,X\_{t},k^{+}\_{t,T})-I(t,T,X\_{t},k^{-}\_{t,T})}{(T-t)^{H+\frac{1}{2}}}\approx\frac{1}{(T-t)^{H+\frac{1}{2}}}E\_{t}\left[\frac{S\_{T}-S\_{t}}{S\_{t}}\sqrt{\frac{1}{T-t}\int\_{t}^{T}\sigma\_{r}^{2}dr}\right]. |  | (3.8) |

###### Proof.

A direct application of the Clark-Ocone-Haussman theorem gives us that

|  |  |  |
| --- | --- | --- |
|  | ∫tTσr2​𝑑r=Et​[∫tTσr2​𝑑r]+∫tT∫rTEr​[DrW​σu22​∫tTσr2​𝑑r]​𝑑u​𝑑Wr.\sqrt{\int\_{t}^{T}\sigma\_{r}^{2}dr}=E\_{t}\left[\sqrt{\int\_{t}^{T}\sigma\_{r}^{2}dr}\right]+\int\_{t}^{T}\int\_{r}^{T}E\_{r}\left[\frac{D\_{r}^{W}\sigma\_{u}^{2}}{2\sqrt{\int\_{t}^{T}\sigma\_{r}^{2}dr}}\right]dudW\_{r}. |  |

A similar argument as in the previous corollary allow us to deduce the result.
∎

## 4 Numerical examples

In this section, we examine the accuracy of the approximation derived in Corollary [6](https://arxiv.org/html/2510.26310v1#Thmtheorem6 "Corollary 6. ‣ 3 Limit theorems ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual") (which is equivalent to approximation ([1.1](https://arxiv.org/html/2510.26310v1#S1.E1 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual"))) and approximation ([1.3](https://arxiv.org/html/2510.26310v1#S1.E3 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) for ρ≠0\rho\neq 0 using the Monte Carlo method under the rough Bergomi model:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | St\displaystyle S\_{t} | =\displaystyle= | exp⁡(X0−12​∫0tσs2​𝑑s+∫0tσs​𝑑Bs),\displaystyle\exp\left(X\_{0}-\frac{1}{2}\int\_{0}^{t}\sigma\_{s}^{2}ds+\int\_{0}^{t}\sigma\_{s}dB\_{s}\right), |  | (4.1) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | σt2\displaystyle\sigma\_{t}^{2} | =\displaystyle= | σ02​exp⁡(α​WtH−12​α2​t2​H)\displaystyle\sigma\_{0}^{2}\exp\left(\alpha W\_{t}^{H}-\frac{1}{2}\alpha^{2}t^{2H}\right) |  | (4.2) |

where WtH:=2​H​∫0t(t−s)H−12​𝑑WsW\_{t}^{H}:=\sqrt{2H}\int\_{0}^{t}(t-s)^{H-\frac{1}{2}}dW\_{s}, and for 0≤s<t0\leq s<t and ρ∈[−1,1]\rho\in[-1,1],

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | E​[WtH​WsH]\displaystyle E[W\_{t}^{H}W\_{s}^{H}] | =\displaystyle= | s2​H​∫012​H(1−x)12−H​(t/s−x)12−H​𝑑x\displaystyle s^{2H}\int^{1}\_{0}\frac{2H}{(1-x)^{\frac{1}{2}-H}(t/s-x)^{\frac{1}{2}-H}}dx |  | (4.3) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | E​[WtH​Bs]\displaystyle E[W\_{t}^{H}B\_{s}] | =\displaystyle= | ρ​2​HH+12​(tH+12−(t−min⁡(t,s))H+12).\displaystyle\frac{\rho\sqrt{2H}}{H+\frac{1}{2}}\left(t^{H+\frac{1}{2}}-(t-\min(t,s))^{H+\frac{1}{2}}\right). |  | (4.4) |

The model parameters are set as S0=100S\_{0}=100, σ0=0.2\sigma\_{0}=0.2, α=0.8\alpha=0.8, the correlations are ρ=−0.2\rho=-0.2, −0.4-0.4, −0.6-0.6, −0.8-0.8, the Hurst indices are H=0.1H=0.1, 0.30.3, 0.50.5, 0.70.7, 0.90.9, and the maturities are set to T=0.0025T=0.0025, 0.0050.005, 0.010.01, 0.0250.025, 0.050.05, 0.10.1, 0.250.25, 0.50.5, 11, 22 and 33.
The number of time steps in the Monte Carlo method is set to max⁡{500​T,100}\max\{500T,100\}, and the number of simulations is set to 20 million.

Tables [1](https://arxiv.org/html/2510.26310v1#S4.T1 "Table 1 ‣ 4 Numerical examples ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual") to [4](https://arxiv.org/html/2510.26310v1#S4.T4 "Table 4 ‣ 4 Numerical examples ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual") contains the approximation of Corollary [6](https://arxiv.org/html/2510.26310v1#Thmtheorem6 "Corollary 6. ‣ 3 Limit theorems ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual"), or equivalently ([1.1](https://arxiv.org/html/2510.26310v1#S1.E1 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")), for various values of HH, ρ\rho and T−tT-t. Times to maturity less than 0.050.05 have not been included to save space. However, as can also be seen in the tables the accuracy increases as T−tT-t decreases. In the tables “Cov” denotes the covariance between ST/St−1S\_{T}/S\_{t}-1 and vtv\_{t}

| H index | Maturity | 0.050.05 | 0.10.1 | 0.250.25 | 0.50.5 | 11 | 22 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.10.1 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1977 | 0.1974 | 0.1969 | 0.1963 | 0.1958 | 0.1952 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1975 | 0.1970 | 0.1963 | 0.1954 | 0.1945 | 0.1931 |
|  | Cov | -0.0002 | -0.0004 | -0.0006 | -0.0009 | -0.0014 | -0.0022 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0014 | -0.0014 | -0.0014 | -0.0014 | -0.0014 | -0.0013 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0015 | -0.0014 | -0.0015 | -0.0014 | -0.0014 | -0.0014 |
| 0.30.3 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1990 | 0.1985 | 0.1975 | 0.1961 | 0.1941 | 0.1911 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1989 | 0.1983 | 0.1969 | 0.1952 | 0.1926 | 0.1885 |
|  | Cov | -0.0002 | -0.0003 | -0.0006 | -0.0010 | -0.0017 | -0.0029 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0017 | -0.0017 | -0.0016 | -0.0016 | -0.0015 | -0.0015 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0017 | -0.0017 | -0.0017 | -0.0017 | -0.0017 | -0.0016 |
| 0.50.5 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1997 | 0.1995 | 0.1987 | 0.1973 | 0.1946 | 0.1893 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1997 | 0.1993 | 0.1983 | 0.1965 | 0.1932 | 0.1867 |
|  | Cov | -0.0001 | -0.0002 | -0.0004 | -0.0008 | -0.0016 | -0.0030 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0016 | -0.0016 | -0.0015 | -0.0015 | -0.0014 | -0.0013 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0016 | -0.0016 | -0.0016 | -0.0016 | -0.0016 | -0.0015 |
| 0.70.7 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1999 | 0.1998 | 0.1993 | 0.1982 | 0.1954 | 0.1881 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1999 | 0.1997 | 0.1991 | 0.1976 | 0.1941 | 0.1855 |
|  | Cov | 0.0000 | -0.0001 | -0.0003 | -0.0006 | -0.0014 | -0.0031 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0014 | -0.0014 | -0.0014 | -0.0014 | -0.0013 | -0.0011 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0014 | -0.0014 | -0.0014 | -0.0014 | -0.0014 | -0.0013 |
| 0.90.9 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.2000 | 0.1999 | 0.1997 | 0.1989 | 0.1961 | 0.1869 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.2000 | 0.1999 | 0.1995 | 0.1984 | 0.1949 | 0.1845 |
|  | Cov | 0.0000 | -0.0001 | -0.0002 | -0.0005 | -0.0012 | -0.0031 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0012 | -0.0012 | -0.0013 | -0.0012 | -0.0012 | -0.0009 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0013 | -0.0013 | -0.0013 | -0.0013 | -0.0012 | -0.0012 |

Table 1: Approximate error of covariance in ρ=−0.2\rho=-0.2



| H index | Maturity | 0.050.05 | 0.10.1 | 0.250.25 | 0.50.5 | 11 | 22 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.10.1 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1975 | 0.1971 | 0.1966 | 0.1960 | 0.1954 | 0.1947 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1970 | 0.1964 | 0.1954 | 0.1942 | 0.1927 | 0.1907 |
|  | Cov | -0.0005 | -0.0007 | -0.0013 | -0.0019 | -0.0028 | -0.0042 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0028 | -0.0028 | -0.0027 | -0.0027 | -0.0027 | -0.0026 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0029 | -0.0029 | -0.0029 | -0.0029 | -0.0028 | -0.0028 |
| 0.30.3 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1989 | 0.1984 | 0.1972 | 0.1957 | 0.1936 | 0.1902 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1986 | 0.1979 | 0.1962 | 0.1939 | 0.1905 | 0.1852 |
|  | Cov | -0.0003 | -0.0005 | -0.0011 | -0.0019 | -0.0033 | -0.0056 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0033 | -0.0033 | -0.0032 | -0.0032 | -0.0030 | -0.0029 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0034 | -0.0034 | -0.0034 | -0.0033 | -0.0033 | -0.0032 |
| 0.50.5 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1997 | 0.1994 | 0.1985 | 0.1970 | 0.1941 | 0.1883 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1996 | 0.1991 | 0.1978 | 0.1955 | 0.1913 | 0.1833 |
|  | Cov | -0.0002 | -0.0003 | -0.0008 | -0.0016 | -0.0031 | -0.0059 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0031 | -0.0031 | -0.0031 | -0.0030 | -0.0028 | -0.0025 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0032 | -0.0032 | -0.0032 | -0.0031 | -0.0031 | -0.0030 |
| 0.70.7 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1999 | 0.1998 | 0.1993 | 0.1981 | 0.1950 | 0.1870 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1998 | 0.1996 | 0.1988 | 0.1969 | 0.1924 | 0.1821 |
|  | Cov | -0.0001 | -0.0002 | -0.0005 | -0.0012 | -0.0028 | -0.0060 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0028 | -0.0028 | -0.0028 | -0.0027 | -0.0026 | -0.0022 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0028 | -0.0028 | -0.0028 | -0.0028 | -0.0028 | -0.0026 |
| 0.90.9 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.2000 | 0.1999 | 0.1997 | 0.1988 | 0.1958 | 0.1858 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1999 | 0.1998 | 0.1993 | 0.1978 | 0.1935 | 0.1810 |
|  | Cov | 0.0000 | -0.0001 | -0.0004 | -0.0009 | -0.0025 | -0.0060 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0025 | -0.0025 | -0.0025 | -0.0025 | -0.0023 | -0.0018 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0025 | -0.0025 | -0.0025 | -0.0025 | -0.0025 | -0.0023 |

Table 2: Approximate error of covariance in ρ=−0.4\rho=-0.4



| H index | Maturity | 0.050.05 | 0.10.1 | 0.250.25 | 0.50.5 | 11 | 22 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.10.1 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1971 | 0.1967 | 0.1961 | 0.1954 | 0.1948 | 0.1939 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1964 | 0.1957 | 0.1943 | 0.1928 | 0.1908 | 0.1881 |
|  | Cov | -0.0007 | -0.0011 | -0.0019 | -0.0028 | -0.0042 | -0.0062 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0042 | -0.0042 | -0.0041 | -0.0040 | -0.0040 | -0.0039 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0043 | -0.0043 | -0.0043 | -0.0043 | -0.0042 | -0.0041 |
| 0.30.3 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1988 | 0.1982 | 0.1968 | 0.1952 | 0.1927 | 0.1889 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1983 | 0.1974 | 0.1952 | 0.1925 | 0.1882 | 0.1816 |
|  | Cov | -0.0005 | -0.0008 | -0.0017 | -0.0029 | -0.0049 | -0.0082 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0050 | -0.0050 | -0.0048 | -0.0047 | -0.0045 | -0.0042 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0051 | -0.0051 | -0.0050 | -0.0050 | -0.0049 | -0.0047 |
| 0.50.5 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1997 | 0.1993 | 0.1983 | 0.1966 | 0.1933 | 0.1868 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1994 | 0.1989 | 0.1972 | 0.1944 | 0.1892 | 0.1794 |
|  | Cov | -0.0002 | -0.0005 | -0.0012 | -0.0023 | -0.0046 | -0.0086 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0047 | -0.0047 | -0.0046 | -0.0045 | -0.0042 | -0.0037 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0047 | -0.0047 | -0.0047 | -0.0047 | -0.0046 | -0.0043 |
| 0.70.7 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1999 | 0.1998 | 0.1992 | 0.1978 | 0.1944 | 0.1854 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1998 | 0.1995 | 0.1984 | 0.1961 | 0.1906 | 0.1782 |
|  | Cov | -0.0001 | -0.0003 | -0.0008 | -0.0018 | -0.0041 | -0.0087 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0042 | -0.0042 | -0.0042 | -0.0041 | -0.0038 | -0.0032 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0043 | -0.0042 | -0.0042 | -0.0042 | -0.0041 | -0.0038 |
| 0.90.9 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.2000 | 0.1999 | 0.1996 | 0.1986 | 0.1953 | 0.1842 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1999 | 0.1998 | 0.1991 | 0.1972 | 0.1919 | 0.1771 |
|  | Cov | -0.0001 | -0.0002 | -0.0005 | -0.0014 | -0.0036 | -0.0087 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0038 | -0.0038 | -0.0037 | -0.0037 | -0.0034 | -0.0027 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0038 | -0.0038 | -0.0038 | -0.0038 | -0.0036 | -0.0033 |

Table 3: Approximate error of covariance in ρ=−0.6\rho=-0.6



| H index | Maturity | 0.050.05 | 0.10.1 | 0.250.25 | 0.50.5 | 11 | 22 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.10.1 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1966 | 0.1961 | 0.1954 | 0.1946 | 0.1939 | 0.1929 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1957 | 0.1948 | 0.1931 | 0.1912 | 0.1887 | 0.1853 |
|  | Cov | -0.0010 | -0.0014 | -0.0025 | -0.0037 | -0.0056 | -0.0082 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0056 | -0.0055 | -0.0054 | -0.0053 | -0.0052 | -0.0050 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0058 | -0.0057 | -0.0057 | -0.0056 | -0.0056 | -0.0054 |
| 0.30.3 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1986 | 0.1979 | 0.1963 | 0.1943 | 0.1915 | 0.1871 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1980 | 0.1968 | 0.1942 | 0.1908 | 0.1856 | 0.1778 |
|  | Cov | -0.0006 | -0.0011 | -0.0022 | -0.0038 | -0.0064 | -0.0107 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0067 | -0.0066 | -0.0064 | -0.0062 | -0.0059 | -0.0054 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0068 | -0.0067 | -0.0067 | -0.0066 | -0.0064 | -0.0061 |
| 0.50.5 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1996 | 0.1992 | 0.1981 | 0.1961 | 0.1923 | 0.1848 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1993 | 0.1986 | 0.1965 | 0.1932 | 0.1868 | 0.1753 |
|  | Cov | -0.0003 | -0.0006 | -0.0016 | -0.0031 | -0.0060 | -0.0112 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0063 | -0.0062 | -0.0061 | -0.0059 | -0.0055 | -0.0048 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0063 | -0.0063 | -0.0063 | -0.0062 | -0.0060 | -0.0056 |
| 0.70.7 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.1999 | 0.1997 | 0.1991 | 0.1975 | 0.1935 | 0.1833 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1997 | 0.1994 | 0.1980 | 0.1952 | 0.1885 | 0.1739 |
|  | Cov | -0.0002 | -0.0004 | -0.0011 | -0.0024 | -0.0054 | -0.0114 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0057 | -0.0056 | -0.0056 | -0.0054 | -0.0050 | -0.0041 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0057 | -0.0057 | -0.0056 | -0.0056 | -0.0054 | -0.0049 |
| 0.90.9 | I​(kt,T−)I(k\_{t,T}^{-}) | 0.2000 | 0.1999 | 0.1996 | 0.1984 | 0.1945 | 0.1819 |
|  | I​(kt,T+)I(k\_{t,T}^{+}) | 0.1999 | 0.1997 | 0.1988 | 0.1966 | 0.1901 | 0.1728 |
|  | Cov | -0.0001 | -0.0002 | -0.0007 | -0.0019 | -0.0048 | -0.0113 |
|  | I​(kt,T+)−I​(kt,T−)(T−t)H+1/2\frac{I(k\_{t,T}^{+})-I(k\_{t,T}^{-})}{(T-t)^{H+1/2}} | -0.0050 | -0.0050 | -0.0050 | -0.0049 | -0.0045 | -0.0034 |
|  | Cov(T−t)H+1/2\frac{\mathrm{Cov}}{(T-t)^{H+1/2}} | -0.0050 | -0.0050 | -0.0050 | -0.0050 | -0.0048 | -0.0043 |

Table 4: Approximate error of covariance in ρ=−0.8\rho=-0.8

In addition to the tables, in Figure [1](https://arxiv.org/html/2510.26310v1#S4.F1 "Figure 1 ‣ 4 Numerical examples ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual") we plot the ratios (I​(kt,T+)−I​(kt,T−))/Cov(I(k\_{t,T}^{+})-I(k\_{t,T}^{-}))/\mathrm{Cov} for various values of HH and T−tT-t while keeping correlation fixed at ρ=−0.8\rho=-0.8. In Figure ([2](https://arxiv.org/html/2510.26310v1#S4.F2 "Figure 2 ‣ 4 Numerical examples ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) the Hurst parameter is fixed H=0.3H=0.3 and T−tT-t and ρ\rho are varied. We observe that the Hurst parameter and time to maturity has a larger impact on accuracy than correlation. The sensitivity of the accuracy to the Hurst parameter is consistent with the fact that the error of the approximation in Corollary [6](https://arxiv.org/html/2510.26310v1#Thmtheorem6 "Corollary 6. ‣ 3 Limit theorems ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual") is O​((T−t)2​H+1)O((T-t)^{2H+1}) (see proof of Theorem [3](https://arxiv.org/html/2510.26310v1#Thmtheorem3 "Theorem 3. ‣ 3 Limit theorems ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual") in Appendix). For small values of HH the error is less for T−t>1T-t>1 but converges slower for T−t<1T-t<1.

00.50.5111.51.5222.52.5330.750.750.800.800.850.850.900.900.950.951.001.00T−tT-t(I​(kt,T+)−I​(kt,T−))/Cov(I(k\_{t,T}^{+})-I(k\_{t,T}^{-}))/\mathrm{Cov}ρ=−0.8\rho=-0.8H=0.1H=0.1H=0.3H=0.3H=0.5H=0.5


Figure 1: Impact of HH and T−tT-t on covariance estimate accuracy

00.50.5111.51.5222.52.5330.750.750.800.800.850.850.900.900.950.951.001.00T−tT-t(I​(kt,T+)−I​(kt,T−))/Cov(I(k\_{t,T}^{+})-I(k\_{t,T}^{-}))/\mathrm{Cov}H=0.3H=0.3ρ=−0.8\rho=-0.8ρ=−0.6\rho=-0.6ρ=−0.4\rho=-0.4


Figure 2: Impact of ρ\rho and T−tT-t on covariance estimate accuracy

Lastly we examine the accuracy of approximation ([1.3](https://arxiv.org/html/2510.26310v1#S1.E3 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) by plotting the estimated value of HH as given by expression ([1.3](https://arxiv.org/html/2510.26310v1#S1.E3 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) divided by its exact value. Equation ([1.3](https://arxiv.org/html/2510.26310v1#S1.E3 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) requires two value for time to maturity. In the plots we have fixed T1=0.0025T\_{1}=0.0025 and let T2∈{0.005,0.01,0.025,0.05,0.1,0.25,0.5,1,2,3}T\_{2}\in\{0.005,0.01,0.025,0.05,0.1,0.25,0.5,1,2,3\}. In figure [3](https://arxiv.org/html/2510.26310v1#S4.F3 "Figure 3 ‣ 4 Numerical examples ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual") the accuracy is shown for ρ=−0.8\rho=-0.8 and various values for HH and T2−tT\_{2}-t. In figure [4](https://arxiv.org/html/2510.26310v1#S4.F4 "Figure 4 ‣ 4 Numerical examples ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual") we fix H=0.3H=0.3 and plot the ratio for different ρ\rho and T2−tT\_{2}-t. We observe that for especially for short maturities the simple approximation ([1.3](https://arxiv.org/html/2510.26310v1#S1.E3 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) is accurate.

00.50.5111.51.5222.52.5330.900.900.920.920.940.940.960.960.980.981.001.00T−tT-tEq. ([1.3](https://arxiv.org/html/2510.26310v1#S1.E3 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual"))/Exact valueρ=−0.8\rho=-0.8H=0.1H=0.1H=0.3H=0.3H=0.5H=0.5


Figure 3: Impact of HH and T−tT-t on HH estimate accuracy

00.50.5111.51.5222.52.5330.900.900.920.920.940.940.960.960.980.981.001.00T−tT-tEq. ([1.3](https://arxiv.org/html/2510.26310v1#S1.E3 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual"))/Exact valueH=0.3H=0.3ρ=−0.8\rho=-0.8ρ=−0.6\rho=-0.6ρ=−0.4\rho=-0.4


Figure 4: Impact of ρ\rho and T−tT-t on HH estimate accuracy

## 5 Conclusion

In this paper we have derived rigorous limit theorems for the approximation ([1.1](https://arxiv.org/html/2510.26310v1#S1.E1 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")). In addition we have noted that it can be used to estimate the value of the Hurst parameter as given by expression ([1.3](https://arxiv.org/html/2510.26310v1#S1.E3 "In 1 Introduction ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")). Numerical runs have confirmed, under the rough Bergomi model, that the approximations are accurate for short times to maturity for different values of the Hurst parameter and correlation. The results are not only of theoretical interest, but also of practical interest. They can, for instance, be used to calibrate or estimate the Hurst parameter from a limited number of short dated options.

## References

* [1]
   Alòs, E., León, J. A. and Vives, J., “On the short-time behavior of the implied volatility for jump-diffusion models with stochastic volatility”, Finance and Stochastics, (2007).
* [2]
   Alòs, E. and Shiraya, K., “Estimating the Hurst parameter from short term volatility swaps: a Malliavin calculus approach”, Finance and Stochastics, (2019).
* [3]
   Backus, D., Foresi, S. and Wu, L., “Accounting for biases in Black-Scholes”, Available at SSRN: https://ssrn.com/abstract=585623.
* [4]
   Comte, F. and Renault, E., “Long memory in continuous-time stochastic volatility models”, Mathematical Finance, (1998).
* [5]
   Fukasawa, M., “Asymptotic analysis for stochastic volatility: martingale expansion”, Finance and Stochastics, (2011).
* [6]
   Fukasawa, M., “Short-time at-the-money skew and rough fractional volatility”, Quantitative Finance, (2017).
* [7]
   Gatheral, J., Jaisson, T. and Rosenbaum, M., “Volatility is rough”, Quantitative Finance, (2018).
* [8]
   Hull, J. and White, A., “The pricing of options on assets with stochastic volatilities”, Journal of Finance, (1987).
* [9]
   Renault, E. and Touzi, N., “Option hedging and implied volatilities in a stochastic volatility model”, Mathematical Finance, (1996).
* [10]
   Rolloos, F., “The future of skew”, Risk, (2022).
* [11]
   Romano, M. and Touzi, N., “Contingent claims and market completeness in a stochastic volatility model”, Mathematical Finance, (1997).
* [12]
   Willard, G.A., “Calculating prices and sensitivities for path-independent securities in multifactor models”, Journal of Derivatives, (1997).

## Appendix A Greeks

This section shows the proofs of Propositions and Theorems in Section [3](https://arxiv.org/html/2510.26310v1#S3 "3 Limit theorems ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual").
Firstly, we give some Greeks of Black-Scholes formula.

A direct calculation gives us that k∈ℝk\in\mathbb{R} and all u>0u>0:

|  |  |  |
| --- | --- | --- |
|  | (B​S−1)′​(k,u)=1∂B​S∂σ​(k,B​S−1​(k,u)).(BS^{-1})^{\prime}(k,u)=\frac{1}{\frac{\partial BS}{\partial\sigma}(k,BS^{-1}(k,u))}. |  |

Then it follows that

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | (B​S−1)′′​(k,u)\displaystyle(BS^{-1})^{\prime\prime}(k,u) | =\displaystyle= | −1(∂B​S∂σ​(k,B​S−1​(k,u)))2​∂2B​S∂σ2​(k,B​S−1​(k,u))​1∂B​S∂σ​(k,B​S−1​(k,u))\displaystyle-\frac{1}{(\frac{\partial BS}{\partial\sigma}(k,BS^{-1}(k,u)))^{2}}\frac{\partial^{2}BS}{\partial\sigma^{2}}(k,BS^{-1}(k,u))\frac{1}{\frac{\partial BS}{\partial\sigma}(k,BS^{-1}(k,u))} |  | (A.1) |
|  |  | =\displaystyle= | −1(∂B​S∂σ​(k,B​S−1​(k,u)))3​∂2B​S∂σ2​(k,B​S−1​(k,u)).\displaystyle-\frac{1}{(\frac{\partial BS}{\partial\sigma}(k,BS^{-1}(k,u)))^{3}}\frac{\partial^{2}BS}{\partial\sigma^{2}}(k,BS^{-1}(k,u)). |  |

Now, the classical relationship between the Vomma and the Vega

|  |  |  |
| --- | --- | --- |
|  | ∂2B​S∂σ2​(k,σ)=∂B​S∂σ​(k,σ)​d1​(k,σ)​d2​(k,σ)σ\frac{\partial^{2}BS}{\partial\sigma^{2}}(k,\sigma)=\frac{\partial BS}{\partial\sigma}(k,\sigma)\frac{d\_{1}(k,\sigma)d\_{2}(k,\sigma)}{\sigma} |  |

allows us to write

|  |  |  |
| --- | --- | --- |
|  | (B​S−1)′′​(k,u)=1(∂B​S∂σ​(k,B​S−1​(k,u)))2​(B​S−1​(k,u))4​(T−t)2−4​(Xt−k)24​(B​S−1​(k,u))3​(T−t).(BS^{-1})^{\prime\prime}(k,u)=\frac{1}{(\frac{\partial BS}{\partial\sigma}(k,BS^{-1}(k,u)))^{2}}\frac{(BS^{-1}(k,u))^{4}(T-t)^{2}-4(X\_{t}-k)^{2}}{4(BS^{-1}(k,u))^{3}(T-t)}. |  |

Finally, as

|  |  |  |
| --- | --- | --- |
|  | ∂B​S∂σ​(k,B​S−1​(k,u))=exp⁡(Xt)​N′​(d1​(k,B​S−1​(k,u)))​T−t,\frac{\partial BS}{\partial\sigma}(k,BS^{-1}(k,u))=\exp(X\_{t})N^{\prime}(d\_{1}\left(k,BS^{-1}(k,u)\right))\sqrt{T-t}, |  |

the above equality reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | (B​S−1)′′​(k,u)=(B​S−1​(k,u))4​(T−t)2−4​(Xt−k)24​(exp⁡(Xt)​N′​(d1​(k,B​S−1​(k,u)))​(T−t))2​(B​S−1​(k,u))3.(BS^{-1})^{\prime\prime}(k,u)=\frac{(BS^{-1}(k,u))^{4}(T-t)^{2}-4(X\_{t}-k)^{2}}{4(\exp(X\_{t})N^{\prime}(d\_{1}\left(k,BS^{-1}(k,u)\right))(T-t))^{2}(BS^{-1}(k,u))^{3}}. |  | (A.2) |

## Appendix B Proofs

###### Proof of Proposition [2](https://arxiv.org/html/2510.26310v1#Thmtheorem2 "Proposition 2. ‣ 3 Limit theorems ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual").

Proposition [1](https://arxiv.org/html/2510.26310v1#Thmtheorem1 "Proposition 1. ‣ 3 Limit theorems ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual") gives us that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | I​(t,T,Xt,k)−Et​[vt]\displaystyle I\left(t,T,X\_{t},k\right)-E\_{t}\left[v\_{t}\right] | | |  |
|  |  | =\displaystyle= | I0​(t,T,Xt,k)−Et​[vt]\displaystyle I^{0}\left(t,T,X\_{t},k\right)-E\_{t}\left[v\_{t}\right] |  |
|  |  |  | +ρ2​Et​∫tT(B​S−1)′​(k,Γs)​H​(s,Xs,k,vs)​Φs​𝑑s\displaystyle+\frac{\rho}{2}E\_{t}\int\_{t}^{T}\left(BS^{-1}\right)^{\prime}\left(k,\Gamma\_{s}\right)H(s,X\_{s},k,v\_{s})\Phi\_{s}ds |  |
|  |  | =\displaystyle= | T1+T2.\displaystyle T\_{1}+T\_{2}. |  |

Now we
apply the anticipating Itô’s formula (see for example Nualart (2005)) to
the process

|  |  |  |
| --- | --- | --- |
|  | H​(t,Xt,k,vt)​Ut​(k),H(t,X\_{t},k,v\_{t})U\_{t}(k), |  |

and we get

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =\displaystyle= | Et[H(t,Xt,k,vt)Ut(k)\displaystyle E\_{t}\Bigg[H(t,X\_{t},k,v\_{t})U\_{t}(k) |  |
|  |  |  | −∫tTH​(s,Xs,k,vs)​(B​S−1)′​(k,Γs)​Φs​𝑑s\displaystyle-\int\_{t}^{T}H(s,X\_{s},k,v\_{s})\left(BS^{-1}\right)^{\prime}\left(k,\Gamma\_{s}\right)\Phi\_{s}ds |  |
|  |  |  | +∫tT∂H∂s​(s,Xs,k,vs)​Us​(k)​𝑑s\displaystyle+\int\_{t}^{T}\frac{\partial H}{\partial s}(s,X\_{s},k,v\_{s})U\_{s}(k)ds |  |
|  |  |  | +ρ2​∫tTDsW​(∂H∂x​(s,Xs,k,vs)​Us​(k))​σs​𝑑s\displaystyle+\frac{\rho}{2}\int\_{t}^{T}D\_{s}^{W}\left(\frac{\partial H}{\partial x}(s,X\_{s},k,v\_{s})U\_{s}(k)\right)\sigma\_{s}ds |  |
|  |  |  | +12​∫tT∂2H∂x2​(s,Xs,k,vs)​σs2​Us​(k)​𝑑s\displaystyle+\frac{1}{2}\int\_{t}^{T}\frac{\partial^{2}H}{\partial x^{2}}(s,X\_{s},k,v\_{s})\sigma\_{s}^{2}U\_{s}(k)ds |  |
|  |  |  | +12∫tT(∂2∂x2−∂∂x)H(s,Xs,k,vs)(vs2−σs2)Us(k)ds],\displaystyle+\frac{1}{2}\int\_{t}^{T}\left(\frac{\partial^{2}}{\partial x^{2}}-\frac{\partial}{\partial x}\right)H(s,X\_{s},k,v\_{s})\left(v\_{s}^{2}-\sigma\_{s}^{2}\right)U\_{s}(k)ds\Bigg], |  |

which implies that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | T2\displaystyle T\_{2} | =\displaystyle= | ρ2Et[H(t,Xt,k,vt)Ut\displaystyle\frac{\rho}{2}E\_{t}\Bigg[H(t,X\_{t},k,v\_{t})U\_{t} |  |
|  |  |  | +ρ2∫tTDsW(∂H∂x(s,Xs,k,vs)Us(k))σsds]\displaystyle+\frac{\rho}{2}\int\_{t}^{T}D\_{s}^{W}\left(\frac{\partial H}{\partial x}(s,X\_{s},k,v\_{s})U\_{s}(k)\right)\sigma\_{s}ds\Bigg] |  |
|  |  | =\displaystyle= | T21+T22.\displaystyle T\_{2}^{1}+T\_{2}^{2}. |  |

Now, notice that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | T22\displaystyle T\_{2}^{2} | =\displaystyle= | ρ24Et[∫tT∂∂x(∂2∂x2−∂∂x)H(s,Xs,k,vs)σs(∫sTDsWσr2dr)Us(k)ds\displaystyle\frac{\rho^{2}}{4}E\_{t}\left[\int\_{t}^{T}\frac{\partial}{\partial x}\left(\frac{\partial^{2}}{\partial x^{2}}-\frac{\partial}{\partial x}\right)H(s,X\_{s},k,v\_{s})\sigma\_{s}\left(\int\_{s}^{T}D\_{s}^{W}\sigma\_{r}^{2}dr\right)U\_{s}(k)ds\right. |  |
|  |  |  | +∫tT∂∂xH(s,Xs,k,vs)(∫sT(BS−1)′(k,Γr)(DsWΦr)dr)σsds].\displaystyle\left.+\int\_{t}^{T}\frac{\partial}{\partial x}H(s,X\_{s},k,v\_{s})\left(\int\_{s}^{T}\left(BS^{-1}\right)^{\prime}\left(k,\Gamma\_{r}\right)\left(D\_{s}^{W}\Phi\_{r}\right)dr\right)\sigma\_{s}ds\right]. |  |

Now the proof is complete.
∎

###### Proof of Theorem [3](https://arxiv.org/html/2510.26310v1#Thmtheorem3 "Theorem 3. ‣ 3 Limit theorems ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual").

Proposition [2](https://arxiv.org/html/2510.26310v1#Thmtheorem2 "Proposition 2. ‣ 3 Limit theorems ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual") allows us to write

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | I​(t,T,Xt,kt,T+)−I​(t,T,Xt,kt,T−)\displaystyle I\left(t,T,X\_{t},k^{+}\_{t,T}\right)-I\left(t,T,X\_{t},k^{-}\_{t,T}\right) | | |  | (B.1) |
|  |  | =\displaystyle= | I0​(t,T,Xt,kt,T+)−I0​(t,T,Xt,kt,T−)\displaystyle I^{0}(t,T,X\_{t},k^{+}\_{t,T})-I^{0}(t,T,X\_{t},k^{-}\_{t,T}) |  |
|  |  |  | +ρ2​Et​[H​(t,Xt,kt,T+,vt)​Ut​(kt+)−H​(t,Xt,kt,T−,vt)​Ut​(kt−)]\displaystyle+\frac{\rho}{2}E\_{t}\left[H(t,X\_{t},k^{+}\_{t,T},v\_{t})U\_{t}(k\_{t}^{+})-H(t,X\_{t},k^{-}\_{t,T},v\_{t})U\_{t}(k\_{t}^{-})\right] |  |
|  |  |  | +ρ24Et[∫tT∂∂x(∂2∂x2−∂∂x)H(s,Xs,kt,T+,vs)σs(∫sTDsWσr2dr)Us(kt,T+)ds\displaystyle+\frac{\rho^{2}}{4}E\_{t}\left[\int\_{t}^{T}\frac{\partial}{\partial x}\left(\frac{\partial^{2}}{\partial x^{2}}-\frac{\partial}{\partial x}\right)H(s,X\_{s},k^{+}\_{t,T},v\_{s})\sigma\_{s}\left(\int\_{s}^{T}D\_{s}^{W}\sigma\_{r}^{2}dr\right)U\_{s}(k^{+}\_{t,T})ds\right. |  |
|  |  |  | −∫tT∂∂x​(∂2∂x2−∂∂x)​H​(s,Xs,kt,T−,vs)​σs​(∫sTDsW​σr2​𝑑r)​Us​(kt,T−)​𝑑s\displaystyle-\int\_{t}^{T}\frac{\partial}{\partial x}\left(\frac{\partial^{2}}{\partial x^{2}}-\frac{\partial}{\partial x}\right)H(s,X\_{s},k^{-}\_{t,T},v\_{s})\sigma\_{s}\left(\int\_{s}^{T}D\_{s}^{W}\sigma\_{r}^{2}dr\right)U\_{s}(k^{-}\_{t,T})ds |  |
|  |  |  | +2​∫tT∂∂x​H​(s,Xs,kt,T+,vs)​(∫sT(B​S−1)′​(kt,T+,Γr)​(DsW​Φr)​𝑑r)​σs​𝑑s\displaystyle+2\int\_{t}^{T}\frac{\partial}{\partial x}H(s,X\_{s},k^{+}\_{t,T},v\_{s})\left(\int\_{s}^{T}\left(BS^{-1}\right)^{\prime}\left(k^{+}\_{t,T},\Gamma\_{r}\right)\left(D\_{s}^{W}\Phi\_{r}\right)dr\right)\sigma\_{s}ds |  |
|  |  |  | −2∫tT∂∂xH(s,Xs,kt,T−,vs)(∫sT(BS−1)′(kt,T−,Γr)(DsWΦr)dr)σsds].\displaystyle\left.-2\int\_{t}^{T}\frac{\partial}{\partial x}H(s,X\_{s},k^{-}\_{t,T},v\_{s})\left(\int\_{s}^{T}\left(BS^{-1}\right)^{\prime}\left(k^{-}\_{t,T},\Gamma\_{r}\right)\left(D\_{s}^{W}\Phi\_{r}\right)dr\right)\sigma\_{s}ds\right]. |  |

Now the proof is decomposed into several steps.

Step 1 By making use of Proposition 3.1 from Renault and Touzi [[9](https://arxiv.org/html/2510.26310v1#bib.bib9)] it can readily be seen that when ρ=0\rho=0:

|  |  |  |
| --- | --- | --- |
|  | I0​(t,T,Xt,kt,T+)=I0​(t,T,Xt,kt,T−).I^{0}(t,T,X\_{t},k^{+}\_{t,T})=I^{0}(t,T,X\_{t},k^{-}\_{t,T}). |  |

Step 2 As

|  |  |  |
| --- | --- | --- |
|  | H​(t,Xt,k,vt)=eXt​N′​(d+​(k,vt))vt​T−t​(1−d+​(k,vt)vt​T−t).H(t,X\_{t},k,v\_{t})=\frac{e^{X\_{t}}N^{\prime}(d\_{+}\left(k,v\_{t}\right))}{v\_{t}\sqrt{T-t}}\left(1-\frac{d\_{+}\left(k,v\_{t}\right)}{v\_{t}\sqrt{T-t}}\right). |  |

it follows that

|  |  |  |
| --- | --- | --- |
|  | H​(t,Xt,kt,T+,vt)=eXt​N′​(d+​(kt,T+,vt))2​vt​T−t​(1vt2​(T−t)​(vt2+I​(kt,T+)2)​(T−t)),H(t,X\_{t},k^{+}\_{t,T},v\_{t})=\frac{e^{X\_{t}}N^{\prime}(d\_{+}\left(k^{+}\_{t,T},v\_{t}\right))}{2v\_{t}\sqrt{T-t}}\left(\frac{1}{v\_{t}^{2}(T-t)}\left(v\_{t}^{2}+I(k^{+}\_{t,T})^{2}\right)(T-t)\right), |  |

and

|  |  |  |
| --- | --- | --- |
|  | H​(t,Xt,kt,T−,vt)=eXt​N′​(d+​(kt,T−,vt))2​vt​T−t​(1vt2​(T−t)​(vt2−I​(kt,T−)2)​(T−t)).H(t,X\_{t},k^{-}\_{t,T},v\_{t})=\frac{e^{X\_{t}}N^{\prime}(d\_{+}\left(k^{-}\_{t,T},v\_{t}\right))}{2v\_{t}\sqrt{T-t}}\left(\frac{1}{v\_{t}^{2}(T-t)}\left(v\_{t}^{2}-I(k^{-}\_{t,T})^{2}\right)(T-t)\right). |  |

Moreover,

|  |  |  |
| --- | --- | --- |
|  | (B​S−1)′​(k,u)=1∂B​S∂σ​(k,B​S−1​(k,u))=1exp⁡(Xt)​N′​(d+​(k,B​S−1​(k,u)))​T−t.(BS^{-1})^{\prime}(k,u)=\frac{1}{\frac{\partial BS}{\partial\sigma}(k,BS^{-1}(k,u))}=\frac{1}{\exp(X\_{t})N^{\prime}(d\_{+}\left(k,BS^{-1}(k,u)\right))\sqrt{T-t}}. |  |

Then

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | limT→tρ2​H​(t,Xt,kt,T+,vt)​Ut​(kt,T+)(T−t)H+12\displaystyle\lim\_{T\to t}\frac{\rho}{2}\frac{H(t,X\_{t},k^{+}\_{t,T},v\_{t})U\_{t}(k^{+}\_{t,T})}{(T-t)^{H+\frac{1}{2}}} | | |  | (B.2) |
|  |  | =\displaystyle= | limT→tρ2​eXs​N′​(d+​(kt,T+,vt))2​vt​T−t​(1vt2​(T−t)​(vt2+I​(kt,T+)2)​(T−t))\displaystyle\lim\_{T\to t}\frac{\rho}{2}\frac{e^{X\_{s}}N^{\prime}(d\_{+}\left(k^{+}\_{t,T},v\_{t}\right))}{2v\_{t}\sqrt{T-t}}\left(\frac{1}{v\_{t}^{2}(T-t)}\left(v\_{t}^{2}+I(k^{+}\_{t,T})^{2}\right)(T-t)\right) |  |
|  |  |  | ×∫tT(BS−1)′(kt,T+,Γs)Φsds\displaystyle\times\int\_{t}^{T}\left(BS^{-1}\right)^{\prime}\left(k^{+}\_{t,T},\Gamma\_{s}\right)\Phi\_{s}ds |  |
|  |  | =\displaystyle= | ρ2​limT→t1(T−t)H+32​∫tT1vs​(σs​∫sTDsW​σr2​𝑑r)​𝑑s\displaystyle\frac{\rho}{2}\lim\_{T\rightarrow t}\frac{1}{(T-t)^{H+\frac{3}{2}}}\int\_{t}^{T}\frac{1}{v\_{s}}\left(\sigma\_{s}\int\_{s}^{T}D\_{s}^{W}\sigma\_{r}^{2}dr\right)ds |  |
|  |  | =\displaystyle= | ρ2​limT→t1(T−t)H+32​∫tT(∫sTDsW​σr2​𝑑r)​𝑑s\displaystyle\frac{\rho}{2}\lim\_{T\rightarrow t}\frac{1}{(T-t)^{H+\frac{3}{2}}}\int\_{t}^{T}\left(\int\_{s}^{T}D\_{s}^{W}\sigma\_{r}^{2}dr\right)ds |  |

while

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→tρ2​H​(t,Xt,kt,T−,vt)​Ut​(kt,T−)(T−t)H+12=0.\displaystyle\lim\_{T\to t}\frac{\rho}{2}\frac{H(t,X\_{t},k^{-}\_{t,T},v\_{t})U\_{t}(k^{-}\_{t,T})}{(T-t)^{H+\frac{1}{2}}}=0. |  | (B.3) |

Step 3 A direct computation gives us that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂∂x​(∂2∂x2−∂∂x)​H​(t,Xt,kt,T+,vt)\displaystyle\frac{\partial}{\partial x}\left(\frac{\partial^{2}}{\partial x^{2}}-\frac{\partial}{\partial x}\right)H(t,X\_{t},k^{+}\_{t,T},v\_{t}) | | |  |
|  |  | =\displaystyle= | ex16​N′​(d+​(kt,T+,vs))vt9​(T−t)52\displaystyle\frac{e^{x}}{16}\frac{N^{\prime}(d\_{+}\left(k^{+}\_{t,T},v\_{s}\right))}{v\_{t}^{9}(T-t)^{\frac{5}{2}}} |  |
|  |  | ×\displaystyle\times | ((T−t)2​(I​(kt,T+)8+2​I​(kt,T+)6​vt2−2​I​(kt,T+)2​vt6−vt8)−24​(T−t)​(I​(kt,T+)4​vt2+I​(kt,T+)2​vt4)+48​vt4),\displaystyle\left((T-t)^{2}(I(k^{+}\_{t,T})^{8}+2I(k^{+}\_{t,T})^{6}v\_{t}^{2}-2I(k^{+}\_{t,T})^{2}v\_{t}^{6}-v\_{t}^{8})-24(T-t)(I(k^{+}\_{t,T})^{4}v\_{t}^{2}+I(k^{+}\_{t,T})^{2}v\_{t}^{4})+48v\_{t}^{4}\right), |  |

and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂∂x​(∂2∂x2−∂∂x)​H​(t,Xt,kt,T−,vt)\displaystyle\frac{\partial}{\partial x}\left(\frac{\partial^{2}}{\partial x^{2}}-\frac{\partial}{\partial x}\right)H(t,X\_{t},k^{-}\_{t,T},v\_{t}) | | |  |
|  |  | =\displaystyle= | ex16​N′​(d−​(kt,T−,vt))vt9​(T−t)52\displaystyle\frac{e^{x}}{16}\frac{N^{\prime}(d\_{-}\left(k^{-}\_{t,T},v\_{t}\right))}{v\_{t}^{9}(T-t)^{\frac{5}{2}}} |  |
|  |  | ×\displaystyle\times | ((T−t)2​(I​(kt,T−)8−2​I​(kt,T−)6​vt2+2​I​(kt,T−)2​vt6−vt8)+24​(T−t)​(I​(kt,T−)4​vt2−I​(kt,T−)2​vt4)+48​vt4).\displaystyle\left((T-t)^{2}(I(k^{-}\_{t,T})^{8}-2I(k^{-}\_{t,T})^{6}v\_{t}^{2}+2I(k^{-}\_{t,T})^{2}v\_{t}^{6}-v\_{t}^{8})+24(T-t)(I(k^{-}\_{t,T})^{4}v\_{t}^{2}-I(k^{-}\_{t,T})^{2}v\_{t}^{4})+48v\_{t}^{4}\right). |  |

Notice that the leading term as T→tT\to t is the same in both expressions. Moreover, they appear in ([B.1](https://arxiv.org/html/2510.26310v1#A2.E1 "In Appendix B Proofs ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) with different sign. Then straightforward computations allow us to see that the sum of the third and the fourth terms in ([B.1](https://arxiv.org/html/2510.26310v1#A2.E1 "In Appendix B Proofs ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) is of order O​(T−t)2​H+1O(T-t)^{2H+1}.

Step 4 Notice that

|  |  |  |
| --- | --- | --- |
|  | ∂H∂x​(t,Xt,kt,T+,vt)=14​eXt​N′​(d−​(kt,T+,vt))vt5​(T−t)3​((vt2−I​(kt,T+)2)2​(T−t)−4​vt2),\frac{\partial H}{\partial x}(t,X\_{t},k^{+}\_{t,T},v\_{t})=\frac{1}{4}\frac{e^{X\_{t}}N^{\prime}(d\_{-}\left(k^{+}\_{t,T},v\_{t}\right))}{v\_{t}^{5}\left(\sqrt{T-t}\right)^{3}}\left((v\_{t}^{2}-I(k^{+}\_{t,T})^{2})^{2}(T-t)-4v\_{t}^{2}\right), |  |

and

|  |  |  |
| --- | --- | --- |
|  | ∂H∂x​(t,Xt,kt,T−,vt)=14​eXt​N′​(d−​(kt,T−,vt))vt5​(T−t)3​((vt2+I​(kt,T−)2)2​(T−t)−4​vt2).\frac{\partial H}{\partial x}(t,X\_{t},k^{-}\_{t,T},v\_{t})=\frac{1}{4}\frac{e^{X\_{t}}N^{\prime}(d\_{-}\left(k^{-}\_{t,T},v\_{t}\right))}{v\_{t}^{5}\left(\sqrt{T-t}\right)^{3}}\left((v\_{t}^{2}+I(k^{-}\_{t,T})^{2})^{2}(T-t)-4v\_{t}^{2}\right). |  |

Notice that, as in Step 3, the leading terms are the same, and they appear in ([B.1](https://arxiv.org/html/2510.26310v1#A2.E1 "In Appendix B Proofs ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) with different sign. This allows us to see that the last two terms in ([B.1](https://arxiv.org/html/2510.26310v1#A2.E1 "In Appendix B Proofs ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) are of order O​(T−t)2​H+1O(T-t)^{2H+1}.

Step 5 Finally, the results in Steps 1, 2, and 3, together with ([B.1](https://arxiv.org/html/2510.26310v1#A2.E1 "In Appendix B Proofs ‣ Estimating the Hurst parameter from the zero vanna implied volatility and its dual")) allow us to complete the proof.
∎