---
authors:
- Elisa Alòs
- Michael Coulon
doc_id: arxiv:1807.05396v1
family_id: arxiv:1807.05396
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: '[1807.05396] On the optimal choice of strike conventions in exchange option
  pricing'
url_abs: http://arxiv.org/abs/1807.05396v1
url_html: https://ar5iv.org/html/1807.05396v1
venue: arXiv q-fin
version: 1
year: 2018
---


Elisa Alòs
  
Dpt. d’Economia i Empresa
  
Universitat Pompeu Fabra
  
and Barcelona GSE
  
c/Ramon Trias Fargas, 25-27
  
08005 Barcelona, Spain
  
Email: elisa.alos@upf.edu
  
Supported by grants ECO2014-59885-P and MTM2013-40782-P
  
Michael Coulon
  
Department of Business and Management
  
University of Sussex
  
Brighton BN1 9SL, UK
  
Email: m.coulon@sussex.ac.uk

###### Abstract

An important but rarely-addressed option pricing question is how to choose appropriate strikes for implied volatility inputs when pricing more exotic multi-asset derivatives. By means of Malliavin Calculus we construct an optimal log-linear strike
convention for exchange options under stochastic volatility models. This
novel approach allows us to minimize the difference between the corresponding Margrabe computed price and the true option price.
We show that this optimal convention does not depend on the
specific stochastic volatility model chosen. Numerical examples are given which provide strong support to the new methodology.

Keywords: Exchange option, Margrabe formula, Malliavin calculus.

AMS subject classification: 91G99, 60H07

## 1 Introduction

Spread options are recognized as important contracts in many financial
markets, and have been widely studied both by practitioners and academic
researchers. In particular, although also traded in other markets, spread options on commodities are closely linked to
the physical markets and the hedging or valuation needs of producers and
consumers, due to their parallels with physical assets like power plants,
refineries, storage facilities or pipelines. Such assets all have an
option-like nature with operational decisions and corresponding payoffs
depending predominantly on the spread between two commodity spot or forward
prices. While a variety of different considerations affect different spread
option types (ranging from calendar spreads to locational spreads to
input/output spreads like crack or spark), the dominant derivative pricing
challenges remain the same.

In particular, the commonly-used lognormal assumption (e.g. the Geometric
Brownian Motion model) for underlying prices StXsuperscriptsubscript𝑆𝑡𝑋S\_{t}^{X} and StYsuperscriptsubscript𝑆𝑡𝑌S\_{t}^{Y}
leads to a convenient closed-form pricing formula known as Margrabe’s
formula (see Margrabe (1978)) given an ‘exchange option’ payoff (SX1−StY)+superscriptsuperscriptsubscript𝑆𝑋1superscriptsubscript𝑆𝑡𝑌(S\_{X}^{1}-S\_{t}^{Y})^{+}. In the context of stochastic volatility models, we do not have an explicit closed-form expression for the corresponding option price. Some approximations can be found for example in Demspter and Hong (2000), Antonelli, Ramponi and Scarlatti (2009), Borovkova, Permana and van der Weide (2007), Alòs and León (2016) or Alòs and Rheinländer (2016)). All of these approaches require the previous calibration of the corresponding model parameters. In some cases, prices can only be found by simulation or other numerical methods. Computation time can be particularly
onerous for physical asset valuation or hedging, whereby strings of hourly
or daily spread options over many years or even decades are required. For such reasons, Margrabe’s formula is frequently employed
for useful and fast benchmark approximations to spread option prices.

Despite the prominence of such tools, relatively little attention has been
paid to the key question of how to choose an appropriate pair of constant
volatility inputs σXsubscript𝜎𝑋\sigma\_{X} and σYsubscript𝜎𝑌\sigma\_{Y} for Margrabe formula,
ideally maintaining consistency both with market data and modeling
preferences. A natural starting point is the implied volatility of the two
legs of the spread, typically observable from more liquidly traded single
asset vanilla calls or puts. However, a significant implied volatility skew
or smile (as well as term structure) exists in most markets, meaning that
there are many possible choices for both σXsubscript𝜎𝑋\sigma\_{X} and σYsubscript𝜎𝑌\sigma\_{Y} and
no obvious rule for which pair is most appropriate. Indeed, there is also no
standard yardstick for measuring which so-called ‘strike convention’ rule is
best in this setting. In Swindle (2014), this important issue is highlighted
and discussed, along with some numerical examples which indicate that the
common industry solution (described as a ‘volatility look-up heuristic’) can
lead to significant pricing differences compared to Monte Carlo values in a
simple jump diffusion model.

In this paper, we aim to answer this crucial question by developing
a new theory for an optimal short-time strike convention, defined as the choice
of implied volatilities such that the resulting estimated option price (obtained from Margrabe’s formula) matches the true option price
as closely as possible. This is equivalent to the choice such that the corresponding implied correlation (backed out from Margrabe’s formula) matches the model
correlation ρ𝜌\rho. It is interesting to note that both Swindle (2014) and
Alexander and Venkatramanan (2011) comment on how the choice of strike convention can impact the implied
correlation skew, smile or frown observed across different moneyness spread
options. As the underlying assets’ returns correlation is clearly unrelated
to contract moneyness, Swindle (2014) describes this as *“purely an
artifact of the interaction of skew with the Margrabe formulation”*,
explaining that *“skew risk can manifest itself as spurious
correlation risk simply due to the look-up heuristic”*.

In order to investigate such effects and recommend a strike convention for
consistent spread option pricing, we rely on tools from Malliavin calculus that allow us
to derive the short-time limit of the sensitivity of implied volatilities to
moneyness, in the context of stochastic volatility models. Our proposed optimal strike convention is, to our knowledge, the first systematic approach to this problem. Moreover, it is model-independent since it depends only on the at-the-money
implied volatilty levels and skews of the corresponding vanilla options. Thus, it can serve as a very useful and practical ‘financial engineering’ tool to improve option pricing accuracy within the financial industry.

The paper is organized as follow. Section 2 is devoted to introducing the main problem and notations. In Section 3 we make use of Malliavin calculus techniques to derive an equation for our strike convention proposal. In Section 4 we determine explicitly this optimal convention in the class of log-linear strike conventions. Section 5
provides a range of numerical examples and tests to investigate the theory
presented in the paper and its implications in practice.

## 2 The objective, the price model and notation

Assume, for the sake of simplicity, that the interest rate r=0.𝑟0r=0. Consider a two-asset stochastic volatility model of the form

|  |  |  |
| --- | --- | --- |
|  | d​StXStX=σtX​d​WtX𝑑subscriptsuperscript𝑆𝑋𝑡superscriptsubscript𝑆𝑡𝑋subscriptsuperscript𝜎𝑋𝑡𝑑subscriptsuperscript𝑊𝑋𝑡\displaystyle\frac{dS^{X}\_{t}}{S\_{t}^{X}}=\sigma^{X}\_{t}dW^{X}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StYStY=σtY​d​WtY,𝑑subscriptsuperscript𝑆𝑌𝑡superscriptsubscript𝑆𝑡𝑌subscriptsuperscript𝜎𝑌𝑡𝑑subscriptsuperscript𝑊𝑌𝑡\displaystyle\frac{dS^{Y}\_{t}}{S\_{t}^{Y}}=\sigma^{Y}\_{t}dW^{Y}\_{t}, |  | (1) |

under a risk-neutral probability P𝑃P. WX,WY

superscript𝑊𝑋superscript𝑊𝑌W^{X},W^{Y} are Brownian motions and σtX,σtY

subscriptsuperscript𝜎𝑋𝑡subscriptsuperscript𝜎𝑌𝑡\sigma^{X}\_{t},\sigma^{Y}\_{t}
are non-negative, right-continuous and square integrable processes adapted to the filtration
generated by another Brownian motion Z𝑍Z. We will use the notation

|  |  |  |
| --- | --- | --- |
|  | ⟨WtX,Z⟩=ρX,⟨WtY,Z⟩=ρY,⟨WtX,WtY⟩=ρ.formulae-sequence  superscriptsubscript𝑊𝑡𝑋𝑍 subscript𝜌𝑋formulae-sequence  superscriptsubscript𝑊𝑡𝑌𝑍 subscript𝜌𝑌  superscriptsubscript𝑊𝑡𝑋superscriptsubscript𝑊𝑡𝑌 𝜌\left\langle W\_{t}^{X},Z\right\rangle=\rho\_{X},\left\langle\;W\_{t}^{Y},Z\right\rangle=\rho\_{Y},\left\langle\;W\_{t}^{X},W\_{t}^{Y}\right\rangle=\rho. |  |

Itô’s representation theorem gives us that, for any fixed s𝑠s

|  |  |  |
| --- | --- | --- |
|  | σsi=E​(σsi)+∫0sai​(s,u)​𝑑Zu,i=X,Y.formulae-sequencesuperscriptsubscript𝜎𝑠𝑖𝐸superscriptsubscript𝜎𝑠𝑖superscriptsubscript0𝑠superscript𝑎𝑖𝑠𝑢differential-dsubscript𝑍𝑢𝑖  𝑋𝑌\sigma\_{s}^{i}=E\left(\sigma\_{s}^{i}\right)+\int\_{0}^{s}a^{i}(s,u)dZ\_{u},\quad i=X,Y. |  |

for some square integrable processes ai​(s,⋅)superscript𝑎𝑖𝑠⋅a^{i}(s,\cdot) adapted to the filtration generated by Z𝑍Z.

Now we describe some basic notation that is used in this article. For this,
we assume that the reader is familiar with the elementary results of the
Malliavin calculus, as given for instance in Nualart (2006).

The set 𝔻Z1,2superscriptsubscript𝔻𝑍

12\mathbb{D}\_{Z}^{1,2} will denote the domain of the derivative operator D𝐷D with respect to the Brownian Motion Z𝑍Z. It is well-known that 𝔻Z1,2superscriptsubscript𝔻𝑍

12\mathbb{D}\_{Z}^{1,2} is a dense subset of L2​(Ω)superscript𝐿2ΩL^{2}(\Omega) and that D𝐷D is a closed and unbounded operator from L2​(Ω)superscript𝐿2ΩL^{2}(\Omega) into L2​([0,T]×Ω).superscript𝐿20𝑇ΩL^{2}([0,T]\times\Omega). We will also consider the
iterated derivatives Dn,superscript𝐷𝑛D^{n}, for n>1,𝑛1n>1, whose domains will be denoted by
𝔻Zn,2.superscriptsubscript𝔻𝑍

𝑛2\mathbb{D}\_{Z}^{n,2}. We will also make use of the notation 𝕃n,2:=L2​([0,T];𝔻Zn,2).assignsuperscript𝕃

𝑛2superscript𝐿2

0𝑇superscriptsubscript𝔻𝑍

𝑛2\mathbb{L}^{n,2}:=L^{2}([0,T];\mathbb{D}\_{Z}^{n,2}).

We notice that, if σ2∈superscript𝜎2absent\sigma^{2}\in 𝕃1,2superscript𝕃

12\mathbb{L}^{1,2} the
Clark-Ocone formula gives us that

|  |  |  |
| --- | --- | --- |
|  | ai​(s,u)=Eu​(Du​(σsi)2),i=X,Y.formulae-sequencesuperscript𝑎𝑖𝑠𝑢subscript𝐸𝑢subscript𝐷𝑢superscriptsubscriptsuperscript𝜎𝑖𝑠2𝑖  𝑋𝑌a^{i}(s,u)=E\_{u}\left(D\_{u}(\sigma^{i}\_{s})^{2}\right),\quad i=X,Y. |  |

Then, under suitable integrability conditions the change rule for the Malliavin derivative operator (see for example Nualart (2006)) gives us that

|  |  |  |
| --- | --- | --- |
|  | ai​(s,u)=2​Eu​(σsi​Du​σsi),i=X,Y.formulae-sequencesuperscript𝑎𝑖𝑠𝑢2subscript𝐸𝑢subscriptsuperscript𝜎𝑖𝑠subscript𝐷𝑢subscriptsuperscript𝜎𝑖𝑠𝑖  𝑋𝑌a^{i}(s,u)=2E\_{u}\left(\sigma^{i}\_{s}D\_{u}\sigma^{i}\_{s}\right),\quad i=X,Y. |  |

We will also make use of the following notation:

* •

  B​S​(t,x,k,σ)𝐵𝑆𝑡𝑥𝑘𝜎BS\left(t,x,k,\sigma\right) denotes the classical Black-Scholes
  call price with time to maturity T−t,𝑇𝑡T-t, log stock price x𝑥x, log
  strike price k𝑘k and volatility σ𝜎\sigma.
* •

  ℒB​S=∂t+12​σ2​(∂x2x−∂x)subscriptℒ𝐵𝑆subscript𝑡12superscript𝜎2subscriptsuperscript2𝑥𝑥subscript𝑥\mathcal{L}\_{BS}=\partial\_{t}+\frac{1}{2}\sigma^{2}\left(\partial^{2}\_{x}x-\partial\_{x}\right) denotes the classical Black-Scholes operator. Notice that (ℒB​S​B​S)​(t,x,k,σ)=0subscriptℒ𝐵𝑆𝐵𝑆𝑡𝑥𝑘𝜎0(\mathcal{L}\_{BS}BS)(t,x,k,\sigma)=0.
* •

  Xt:=log⁡StX,Yt:=log⁡StYformulae-sequenceassignsubscript𝑋𝑡subscriptsuperscript𝑆𝑋𝑡assignsubscript𝑌𝑡subscriptsuperscript𝑆𝑌𝑡X\_{t}:=\log S^{X}\_{t},Y\_{t}:=\log S^{Y}\_{t}.
* •

  Vt=Et​(STX−STY)+subscript𝑉𝑡subscript𝐸𝑡superscriptsuperscriptsubscript𝑆𝑇𝑋superscriptsubscript𝑆𝑇𝑌V\_{t}=E\_{t}(S\_{T}^{X}-S\_{T}^{Y})^{+} is the exchange option price under the model ([1](#S2.E1 "In 2 The objective, the price model and notation ‣ On the optimal choice of strike conventions in exchange option pricing")).
* •

  For every 0<t<T0𝑡𝑇0<t<T and x,k>0,IX​(t,x,z)formulae-sequence
  𝑥𝑘0subscript𝐼𝑋𝑡𝑥𝑧x,k>0,I\_{X}(t,x,z) is the implied volatility of an
  option with payoff (STX−exp⁡(z))+superscriptsuperscriptsubscript𝑆𝑇𝑋𝑧(S\_{T}^{X}-\exp\left(z\right))^{+} with Xt=x.subscript𝑋𝑡𝑥X\_{t}=x. That is,

  |  |  |  |
  | --- | --- | --- |
  |  | B​S​(t,x,k,IX​(t,x,z))=Et​(STX−exp⁡(z))+.𝐵𝑆𝑡𝑥𝑘subscript𝐼𝑋𝑡𝑥𝑧subscript𝐸𝑡superscriptsuperscriptsubscript𝑆𝑇𝑋𝑧BS\left(t,x,k,I\_{X}(t,x,z)\right)=E\_{t}(S\_{T}^{X}-\exp\left(z\right))^{+}. |  |

  Analogously, IY​(t,y,z)subscript𝐼𝑌𝑡𝑦𝑧I\_{Y}(t,y,z) is the implied volatility of an option with
  payoff (STY−exp⁡(z))+superscriptsuperscriptsubscript𝑆𝑇𝑌𝑧\left(S\_{T}^{Y}-\exp\left(z\right)\right)^{+} with Yt=y.subscript𝑌𝑡𝑦Y\_{t}=y.
* •

  v~t:=1T−t​(∫tTσ~s2​𝑑s)assignsubscript~𝑣𝑡1𝑇𝑡superscriptsubscript𝑡𝑇superscriptsubscript~𝜎𝑠2differential-d𝑠\tilde{v}\_{t}:=\sqrt{\frac{1}{T-t}\left(\int\_{t}^{T}\tilde{\sigma}\_{s}^{2}ds\right)}
* •

  Mti:=Et​∫0T(σsi)2​𝑑s,i=X,Y.formulae-sequenceassignsubscriptsuperscript𝑀𝑖𝑡subscript𝐸𝑡superscriptsubscript0𝑇superscriptsubscriptsuperscript𝜎𝑖𝑠2differential-d𝑠𝑖
  𝑋𝑌M^{i}\_{t}:=E\_{t}\int\_{0}^{T}(\sigma^{i}\_{s})^{2}ds,\quad i=X,Y.
* •

  σ~t:=(σtX)2+(σtY)2−2​ρ​σX​σYassignsubscript~𝜎𝑡superscriptsubscriptsuperscript𝜎𝑋𝑡2superscriptsubscriptsuperscript𝜎𝑌𝑡22𝜌superscript𝜎𝑋superscript𝜎𝑌\tilde{\sigma}\_{t}:=\sqrt{(\sigma^{X}\_{t})^{2}+(\sigma^{Y}\_{t})^{2}-2\rho\sigma^{X}\sigma^{Y}}
* •

  M~t:=Et​∫0T(σ~s)2​𝑑sassignsubscript~𝑀𝑡subscript𝐸𝑡superscriptsubscript0𝑇superscriptsubscript~𝜎𝑠2differential-d𝑠\tilde{M}\_{t}:=E\_{t}\int\_{0}^{T}(\tilde{\sigma}\_{s})^{2}ds

For the sake of simplicity, we will take t=0𝑡0t=0 and we will denote IX​(x,z)=IX​(0,x,z)subscript𝐼𝑋𝑥𝑧subscript𝐼𝑋0𝑥𝑧I\_{X}(x,z)=I\_{X}(0,x,z) and IY​(y,z)=IY​(0,y,z)subscript𝐼𝑌𝑦𝑧subscript𝐼𝑌0𝑦𝑧I\_{Y}(y,z)=I\_{Y}(0,y,z). Moreover, we denote x=X0𝑥subscript𝑋0x=X\_{0} and y=Y0𝑦subscript𝑌0y=Y\_{0}.

It is well known that, under the Black-Scholes model, σtX=σXsubscriptsuperscript𝜎𝑋𝑡subscript𝜎𝑋\sigma^{X}\_{t}=\sigma\_{X} and σtY=σYsubscriptsuperscript𝜎𝑌𝑡subscript𝜎𝑌\sigma^{Y}\_{t}=\sigma\_{Y}, for all t∈[0,T]𝑡0𝑇t\in[0,T] and for some positive constants σXsubscript𝜎𝑋\sigma\_{X} and σYsubscript𝜎𝑌\sigma\_{Y}. In this case, the option price V0subscript𝑉0V\_{0} can be computed analytically by means of Margrabe’s formula. More precisely, in this case, the price is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​S​(0,x,y,σX2+σY2−2​ρ​σX​σY)𝐵𝑆0𝑥𝑦superscriptsubscript𝜎𝑋2superscriptsubscript𝜎𝑌22𝜌subscript𝜎𝑋subscript𝜎𝑌\displaystyle BS\left(0,x,y,\sqrt{\sigma\_{X}^{2}+\sigma\_{Y}^{2}-2\rho\sigma\_{X}\sigma\_{Y}}\right) |  | (2) |

In the general stochastic volatility case, there is no analytical formula for this option price. One common strategy is to substitute σXsubscript𝜎𝑋\sigma\_{X} and σYsubscript𝜎𝑌\sigma\_{Y} by the vanilla implied volatilities IX​(x,kX)subscript𝐼𝑋𝑥subscript𝑘𝑋I\_{X}(x,k\_{X}) and IY​(y,kY)subscript𝐼𝑌𝑦subscript𝑘𝑌I\_{Y}(y,k\_{Y}), for some log strikes kX,kY

subscript𝑘𝑋subscript𝑘𝑌k\_{X},k\_{Y}. But notice that, as these implied volatilities are not constant as a function of the strike, the corresponding price estimation

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​S​(0,x,y,IX2​(x,kX)+IY2​(y,kY)−2​ρ​IX​(x,kX)​IY​(y,kY))𝐵𝑆0𝑥𝑦superscriptsubscript𝐼𝑋2𝑥subscript𝑘𝑋superscriptsubscript𝐼𝑌2𝑦subscript𝑘𝑌2𝜌subscript𝐼𝑋𝑥subscript𝑘𝑋subscript𝐼𝑌𝑦subscript𝑘𝑌BS\left(0,x,y,\sqrt{I\_{X}^{2}(x,k\_{X})+I\_{Y}^{2}(y,k\_{Y})-2\rho I\_{X}(x,k\_{X})I\_{Y}(y,k\_{Y})}\right) |  | (3) |

will depend strongly on the choice of the log strikes kXsubscript𝑘𝑋k\_{X} and kYsubscript𝑘𝑌k\_{Y}.
Despite of the relevance of this problem, there is currently no standard rule for choosing kXsubscript𝑘𝑋k\_{X} and kYsubscript𝑘𝑌k\_{Y} (see for example Swindle (2014)). Our aim in this paper is to develop a standard rule that will allow us to choose these strikes in such a way that the approximation ([3](#S2.E3 "In 2 The objective, the price model and notation ‣ On the optimal choice of strike conventions in exchange option pricing")) will be as close as possible to the true option price V0subscript𝑉0V\_{0} for a range of moneyness cases. More precisely, we want to find the pair kX:=kX​(x,y)assignsubscript𝑘𝑋subscript𝑘𝑋𝑥𝑦k\_{X}:=k\_{X}(x,y) and kY:=kY​(x,y)assignsubscript𝑘𝑌subscript𝑘𝑌𝑥𝑦k\_{Y}:=k\_{Y}(x,y) that minimizes the difference

|  |  |  |  |
| --- | --- | --- | --- |
|  | |V0−B​S​(0,x,y,γ​(x,y))|,subscript𝑉0𝐵𝑆0𝑥𝑦𝛾𝑥𝑦|V\_{0}-BS\left(0,x,y,\gamma(x,y)\right)|, |  | (4) |

for short-time and near-the-money (x≈y𝑥𝑦x\approx y) options, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ​(x,y):=IX2​(x,kX)+IY2​(y,kY)−2​ρ​IX​(x,kX)​IY​(y,kY).assign𝛾𝑥𝑦superscriptsubscript𝐼𝑋2𝑥subscript𝑘𝑋superscriptsubscript𝐼𝑌2𝑦subscript𝑘𝑌2𝜌subscript𝐼𝑋𝑥subscript𝑘𝑋subscript𝐼𝑌𝑦subscript𝑘𝑌\gamma(x,y):=\sqrt{I\_{X}^{2}(x,k\_{X})+I\_{Y}^{2}(y,k\_{Y})-2\rho I\_{X}(x,k\_{X})I\_{Y}(y,k\_{Y})}. |  | (5) |

Notice that, if we define γ^​(x,y)^𝛾𝑥𝑦\hat{\gamma}\left(x,y\right) as the quantity
such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | V0=B​S​(0,x,y,γ^​(x,y)),subscript𝑉0𝐵𝑆0𝑥𝑦^𝛾𝑥𝑦V\_{0}=BS(0,x,y,\hat{\gamma}\left(x,y\right)), |  | (6) |

to minimize ([4](#S2.E4 "In 2 The objective, the price model and notation ‣ On the optimal choice of strike conventions in exchange option pricing")) it is sufficient to minimize

|  |  |  |
| --- | --- | --- |
|  | γ^​(x,y)−γ​(x,y).^𝛾𝑥𝑦𝛾𝑥𝑦{\hat{\gamma}}(x,y)-\gamma(x,y). |  |

###### Remark 1

Note that it is also sufficient to minimize the quantity ρ−ρ^𝜌^𝜌\rho-\hat{\rho}, where ρ^^𝜌\hat{\rho} denotes the implied correlation, defined by the equality

|  |  |  |
| --- | --- | --- |
|  | γ^​(x,y):=IX2​(x,kX)+IY2​(y,kY)−2​ρ^​IX​(x,kX)​IY​(y,kY).assign^𝛾𝑥𝑦superscriptsubscript𝐼𝑋2𝑥subscript𝑘𝑋superscriptsubscript𝐼𝑌2𝑦subscript𝑘𝑌2^𝜌subscript𝐼𝑋𝑥subscript𝑘𝑋subscript𝐼𝑌𝑦subscript𝑘𝑌{\hat{\gamma}}(x,y):=\sqrt{I\_{X}^{2}(x,k\_{X})+I\_{Y}^{2}(y,k\_{Y})-2\hat{\rho}I\_{X}(x,k\_{X})I\_{Y}(y,k\_{Y})}. |  |

In the following section we will develop a methodology to choose the pair (kX,kY)subscript𝑘𝑋subscript𝑘𝑌(k\_{X},k\_{Y}). As we have no explicit expressions for γ𝛾\gamma and γ^^𝛾\hat{\gamma}, the main idea is to approximate these two quantities and to find the pair (kX,kY)subscript𝑘𝑋subscript𝑘𝑌(k\_{X},k\_{Y}) that makes these approximations equal. Towards this end, we will consider for any fixed x𝑥x the short-time limit of the Taylor expansion of the function γ​(x,⋅)−γ^​(x,⋅)𝛾𝑥⋅^𝛾𝑥⋅\gamma(x,\cdot)-\hat{\gamma}(x,\cdot). This motivates the following definition of strike conventions of any order.

###### Definition 2

Assume the model ([1](#S2.E1 "In 2 The objective, the price model and notation ‣ On the optimal choice of strike conventions in exchange option pricing")). We will say that a pair (k1,k2)∈L2​(ℝ2;ℝ2)subscript𝑘1subscript𝑘2superscript𝐿2

superscriptℝ2superscriptℝ2(k\_{1},k\_{2})\in L^{2}(\mathbb{R}^{2};\mathbb{R}^{2}) is a short-time optimal strike convention of order n𝑛n (a n𝑛n-STOSC) if

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0∂iγ∂iy​(x,x)=limT→0∂γ^i∂iy​(x,x),subscript→𝑇0superscript𝑖𝛾superscript𝑖𝑦𝑥𝑥subscript→𝑇0superscript^𝛾𝑖superscript𝑖𝑦𝑥𝑥\lim\_{T\to 0}\frac{\partial^{i}\gamma}{\partial^{i}y}(x,x)=\lim\_{T\to 0}\frac{\partial\hat{\gamma}^{i}}{\partial^{i}y}(x,x), |  | (7) |

for any i=0,…,n𝑖

0…𝑛i=0,...,n, and where γ𝛾\gamma and γ^^𝛾\hat{\gamma} are defined as in [5](#S2.E5 "In 2 The objective, the price model and notation ‣ On the optimal choice of strike conventions in exchange option pricing") and [6](#S2.E6 "In 2 The objective, the price model and notation ‣ On the optimal choice of strike conventions in exchange option pricing"), respectively.

###### Remark 3

Notice that, as n𝑛n increases, γ^^𝛾\hat{\gamma} is expected to be closer to γ𝛾\gamma (and ρ^^𝜌\hat{\rho} closer to ρ𝜌\rho) for short-term and near-the-money options.

## 3 The construction of optimal strike conventions

We will make use of the following hypotheses.

(H1)
:   For any x∈ℝ𝑥ℝx\in\mathbb{R}, kX​(x,x)=kY​(x,x)=xsubscript𝑘𝑋𝑥𝑥subscript𝑘𝑌𝑥𝑥𝑥k\_{X}(x,x)=k\_{Y}(x,x)=x.

(H2)
:   σ∈𝕃2,4𝜎superscript𝕃

    24\sigma\in\mathbb{L}^{2,4}.

(H3)
:   There exist two positive constants a𝑎a and b𝑏b such that, for any t∈[0,T]𝑡0𝑇t\in[0,T], a<σt<b𝑎subscript𝜎𝑡𝑏a<\sigma\_{t}<b.

(H4)
:   Hypothesis (H2) holds and there exists a positive constant C>0𝐶0C>0 such that, for any 0<r<s<T0𝑟𝑠𝑇0<r<s<T,

    |  |  |  |
    | --- | --- | --- |
    |  | Er​[Dr​(σsi)2]≤C,i=X,Y.formulae-sequencesubscript𝐸𝑟delimited-[]subscript𝐷𝑟superscriptsubscriptsuperscript𝜎𝑖𝑠2𝐶𝑖  𝑋𝑌E\_{r}\left[D\_{r}(\sigma^{i}\_{s})^{2}\right]\leq C,\quad i=X,Y. |  |

(H5)
:   Hypotheses (H2) and (H4) hold and, for any t∈[0,T]𝑡0𝑇t\in[0,T], there exists a constant D+​σ0isuperscript𝐷subscriptsuperscript𝜎𝑖0D^{+}\sigma^{i}\_{0} such that as T→0→𝑇0T\rightarrow 0,

    |  |  |  |
    | --- | --- | --- |
    |  | supr,s∈[0,T]Et​|Ds​σri−D+​σ0i|→0,i=X,Y.formulae-sequence→subscriptsupremum  𝑟𝑠 0𝑇subscript𝐸𝑡subscript𝐷𝑠subscriptsuperscript𝜎𝑖𝑟superscript𝐷subscriptsuperscript𝜎𝑖00𝑖  𝑋𝑌\sup\_{r,s\in[0,T]}E\_{t}|D\_{s}\sigma^{i}\_{r}-D^{+}\sigma^{i}\_{0}|\to 0,\quad i=X,Y. |  |

We note that we choose (H3) and (H4) for the sake of simplicity, but these hypotheses can be substituted by adequate integrability conditions. On the other hand, (H2) and (H5) are satisfied by the classical stochastic volatility models, where the volatility is assumed to be a diffussion process (see for example Alòs and Ewald (2008) for the Heston case). In the case of fractional volatility models with H<12𝐻12H<\frac{1}{2} (see for example Alòs, León and Vives (2007), Fukasawa (2011) or Bayer, Friz and Gatheral (2016)), (H5) is not satisfied. Adapting our results to these models is left for future research.

Our first result establishes that all the strike conventions satisfying hypotheses (H1)-(H5) are 00-STOSCs.

###### Proposition 4

Consider the model ([1](#S2.E1 "In 2 The objective, the price model and notation ‣ On the optimal choice of strike conventions in exchange option pricing")) and assume that (kX,kY)subscript𝑘𝑋subscript𝑘𝑌(k\_{X},k\_{Y}) is a strike convention such that hypotheses (H1)-(H5) hold. Then (kX,kY)subscript𝑘𝑋subscript𝑘𝑌(k\_{X},k\_{Y}) is a 00-STOSC.

Proof. It suffices to see that limT→0γ​(x,x)=limT→0γ^​(x,x)subscript→𝑇0𝛾𝑥𝑥subscript→𝑇0^𝛾𝑥𝑥\lim\_{T\to 0}\gamma(x,x)=\lim\_{T\to 0}\hat{\gamma}(x,x). This proof will be decomposed into two steps.

Step 1 Let us prove that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0γ​(x,x)=σ~0subscript→𝑇0𝛾𝑥𝑥subscript~𝜎0\lim\_{T\to 0}\gamma(x,x)=\tilde{\sigma}\_{0} |  | (8) |

It is well known (see for example Durrleman (2008)) that the vanilla at-the-money implied volatilities IX,IY

subscript𝐼𝑋subscript𝐼𝑌I\_{X},I\_{Y} tend to the corresponding spot volatility. That is,

|  |  |  |
| --- | --- | --- |
|  | limT→0(Ii​(x,x)−E​(σ0i))=0,i=X,Y.formulae-sequencesubscript→𝑇0subscript𝐼𝑖𝑥𝑥𝐸subscriptsuperscript𝜎𝑖00𝑖  𝑋𝑌\lim\_{T\to 0}\left(I\_{i}(x,x)-E\left(\sigma^{i}\_{0}\right)\right)=0,\hskip 5.69046pti=X,Y. |  |

Now, taking into account (H1) and the fact that σXsuperscript𝜎𝑋\sigma^{X} and σYsuperscript𝜎𝑌\sigma^{Y} are right-continuous processes it follows that

|  |  |  |
| --- | --- | --- |
|  | limT→0Ii​(x,ki)=σ0i,i=X,Y,formulae-sequencesubscript→𝑇0subscript𝐼𝑖𝑥subscript𝑘𝑖subscriptsuperscript𝜎𝑖0𝑖  𝑋𝑌\lim\_{T\to 0}I\_{i}(x,k\_{i})=\sigma^{i}\_{0},\hskip 5.69046pti=X,Y, |  |

where ki=ki​(x,x)subscript𝑘𝑖subscript𝑘𝑖𝑥𝑥k\_{i}=k\_{i}(x,x). Now, as

|  |  |  |
| --- | --- | --- |
|  | γ​(x,y):=IX2​(x,kX)+IY2​(y,kY)−2​ρ​IX​(x,kX)​IY​(y,kY),assign𝛾𝑥𝑦superscriptsubscript𝐼𝑋2𝑥subscript𝑘𝑋superscriptsubscript𝐼𝑌2𝑦subscript𝑘𝑌2𝜌subscript𝐼𝑋𝑥subscript𝑘𝑋subscript𝐼𝑌𝑦subscript𝑘𝑌\gamma(x,y):=\sqrt{I\_{X}^{2}(x,k\_{X})+I\_{Y}^{2}(y,k\_{Y})-2\rho I\_{X}(x,k\_{X})I\_{Y}(y,k\_{Y})}, |  |

([8](#S3.E8 "In 3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing")) follows.

Step 2 Let us see that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0γ^​(x,x)=σ~0.subscript→𝑇0^𝛾𝑥𝑥subscript~𝜎0\lim\_{T\to 0}\hat{\gamma}(x,x)=\tilde{\sigma}\_{0}. |  | (9) |

By its definition, we have that

|  |  |  |
| --- | --- | --- |
|  | γ^​(x,x)=B​S−1​(0,x,y,V0),^𝛾𝑥𝑥𝐵superscript𝑆10𝑥𝑦subscript𝑉0\hat{\gamma}(x,x)=BS^{-1}(0,x,y,V\_{0}), |  |

where B​S−1𝐵superscript𝑆1BS^{-1} is the inverse of the Black-Scholes function in the sense that

|  |  |  |
| --- | --- | --- |
|  | V0=B​S​(0,x,y,B​S−1​(0,x,y,V0)).subscript𝑉0𝐵𝑆0𝑥𝑦𝐵superscript𝑆10𝑥𝑦subscript𝑉0V\_{0}=BS(0,x,y,BS^{-1}(0,x,y,V\_{0})). |  |

Then, Theorem 5 in Alòs and León (2016) gives us that

|  |  |  |
| --- | --- | --- |
|  | V0=E​(B​S​(0,x,x,v~0))+o​(1),subscript𝑉0𝐸𝐵𝑆0𝑥𝑥subscript~𝑣0𝑜1V\_{0}=E\left(BS(0,x,x,\tilde{v}\_{0})\right)+o(1), |  |

which implies that

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ^​(x,x)=B​S−1​(E​(B​S​(0,x,x,v~0))+o​(1)).^𝛾𝑥𝑥𝐵superscript𝑆1𝐸𝐵𝑆0𝑥𝑥subscript~𝑣0𝑜1\hat{\gamma}(x,x)=BS^{-1}\left(E\left(BS(0,x,x,\tilde{v}\_{0})\right)+o(1)\right). |  | (10) |

Moreover, the martingale representation theorem gives us that

|  |  |  |
| --- | --- | --- |
|  | E​(B​S​(0,x,x,v~0))=B​S​(0,x,x,v~0)+∫0TA​(T,s)​𝑑Zs,𝐸𝐵𝑆0𝑥𝑥subscript~𝑣0𝐵𝑆0𝑥𝑥subscript~𝑣0superscriptsubscript0𝑇𝐴𝑇𝑠differential-dsubscript𝑍𝑠E\left(BS(0,x,x,\tilde{v}\_{0})\right)=BS(0,x,x,\tilde{v}\_{0})+\int\_{0}^{T}A(T,s)dZ\_{s}, |  |

for some adapted and square integrable process A​(T,⋅)𝐴𝑇⋅A(T,\cdot).
This, jointly with ([10](#S3.E10 "In 3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing")) gives us that

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | limT→0γ^​(x,x)subscript→𝑇0^𝛾𝑥𝑥\displaystyle\lim\_{T\to 0}\hat{\gamma}(x,x) | =\displaystyle= | limT→0B​S−1​(0,x,x,(B​S​(0,x,x,v~0)+∫0TA​(T,s)​𝑑Zs+o​(1)))subscript→𝑇0𝐵superscript𝑆10𝑥𝑥𝐵𝑆0𝑥𝑥subscript~𝑣0superscriptsubscript0𝑇𝐴𝑇𝑠differential-dsubscript𝑍𝑠𝑜1\displaystyle\lim\_{T\to 0}BS^{-1}\left(0,x,x,\left(BS(0,x,x,\tilde{v}\_{0})+\int\_{0}^{T}A(T,s)dZ\_{s}+o(1)\right)\right) |  | (11) |
|  |  | =\displaystyle= | limT→0BS−1(0,x,x,(BS(0,x,x,v~0))\displaystyle\lim\_{T\to 0}BS^{-1}\left(0,x,x,\left(BS(0,x,x,\tilde{v}\_{0}\right)\right) |  |
|  |  | =\displaystyle= | limT→0v~0subscript→𝑇0subscript~𝑣0\displaystyle\lim\_{T\to 0}\tilde{v}\_{0} |  |
|  |  | =\displaystyle= | σ~0,subscript~𝜎0\displaystyle\tilde{\sigma}\_{0}, |  |

and this allows us to complete the proof

In order to identify the strike conventions that are 111-STOCs, we will need the following result (see Alòs, León and Vives (2007)).

###### Theorem 5

Consider the model ([1](#S2.E1 "In 2 The objective, the price model and notation ‣ On the optimal choice of strike conventions in exchange option pricing")) and assume that hypotheses (H1)-(H5) hold. Then, for i=X,Y𝑖

𝑋𝑌i=X,Y,

|  |  |  |
| --- | --- | --- |
|  | limT→0∂Ii∂z=ρi​D+​σti2​σti=14​σ03​limT→0⟨log⁡Si,Mi⟩T−⟨log⁡Si,Mi⟩Tsubscript→𝑇0subscript𝐼𝑖𝑧subscript𝜌𝑖superscript𝐷subscriptsuperscript𝜎𝑖𝑡2subscriptsuperscript𝜎𝑖𝑡14subscriptsuperscript𝜎30subscript→𝑇0subscript  superscript𝑆𝑖superscript𝑀𝑖 𝑇  superscript𝑆𝑖superscript𝑀𝑖𝑇\lim\_{T\to 0}\frac{\partial I\_{i}}{\partial z}=\frac{\rho\_{i}D^{+}\sigma^{i}\_{t}}{2\sigma^{i}\_{t}}=\frac{1}{4\sigma^{3}\_{0}}\lim\_{T\to 0}\frac{\langle\log S^{i},M^{i}\rangle\_{T}-\langle\log S^{i},M^{i}\rangle}{T} |  |

Proof. Theorem 6.3 in Alòs, León and Vives (2007) gives us that

|  |  |  |
| --- | --- | --- |
|  | ∂Ii∂y=−ρi​D+​σ0i2​σ0i.subscript𝐼𝑖𝑦subscript𝜌𝑖superscript𝐷subscriptsuperscript𝜎𝑖02subscriptsuperscript𝜎𝑖0\frac{\partial I\_{i}}{\partial y}=-\frac{\rho\_{i}D^{+}\sigma^{i}\_{0}}{2\sigma^{i}\_{0}}. |  |

for i=X,Y𝑖

𝑋𝑌i=X,Y. Now, as ∂Ii∂z=−∂Ii∂zsubscript𝐼𝑖𝑧subscript𝐼𝑖𝑧\frac{\partial I\_{i}}{\partial z}=-\frac{\partial I\_{i}}{\partial z}, the first equality follows. For the second one, notice that Clark-Ocone formula (see for example Nualart (2005)) gives us that

|  |  |  |
| --- | --- | --- |
|  | (σti)2=E​((σti)2)+∫0tEr​(Dr​(σti)2)​𝑑Zr,i=X,Y,formulae-sequencesuperscriptsubscriptsuperscript𝜎𝑖𝑡2𝐸superscriptsubscriptsuperscript𝜎𝑖𝑡2superscriptsubscript0𝑡subscript𝐸𝑟subscript𝐷𝑟superscriptsubscriptsuperscript𝜎𝑖𝑡2differential-dsubscript𝑍𝑟𝑖  𝑋𝑌(\sigma^{i}\_{t})^{2}=E\left((\sigma^{i}\_{t})^{2}\right)+\int\_{0}^{t}E\_{r}\left(D\_{r}(\sigma^{i}\_{t})^{2}\right)dZ\_{r},\quad i=X,Y, |  |

from where we can easily deduce that

|  |  |  |
| --- | --- | --- |
|  | d​Mti=(∫tTEt​(Dt​(σui)2)​𝑑u)​d​Zt=2​(∫tTEt​(σui​Dt​σui)​𝑑u)​d​Zt,i=X,Y,formulae-sequence𝑑superscriptsubscript𝑀𝑡𝑖superscriptsubscript𝑡𝑇subscript𝐸𝑡subscript𝐷𝑡superscriptsubscriptsuperscript𝜎𝑖𝑢2differential-d𝑢𝑑subscript𝑍𝑡2superscriptsubscript𝑡𝑇subscript𝐸𝑡subscriptsuperscript𝜎𝑖𝑢subscript𝐷𝑡subscriptsuperscript𝜎𝑖𝑢differential-d𝑢𝑑subscript𝑍𝑡𝑖  𝑋𝑌dM\_{t}^{i}=\left(\int\_{t}^{T}E\_{t}\left(D\_{t}(\sigma^{i}\_{u})^{2}\right)du\right)dZ\_{t}=2\left(\int\_{t}^{T}E\_{t}(\sigma^{i}\_{u}D\_{t}\sigma^{i}\_{u})du\right)dZ\_{t},\quad i=X,Y, |  |

from where the second equality holds.

###### Remark 6

The above result gives us that the derivatives ∂Ii∂z,i=X,Yformulae-sequence

subscript𝐼𝑖𝑧𝑖
𝑋𝑌\frac{\partial I\_{i}}{\partial z},i=X,Y depend only on the quadratic covariation between M𝑀M and logSisuperscriptsubscript𝑆𝑖\log\_{S}^{i} and on the volatility σisuperscript𝜎𝑖\sigma^{i}.

Define d​P^d​P=eYT−Y0𝑑^𝑃𝑑𝑃superscript𝑒subscript𝑌𝑇subscript𝑌0\frac{d\hat{P}}{dP}=e^{Y\_{T}-Y\_{0}}. The set 𝔻Z^1,2superscriptsubscript𝔻^𝑍

12\mathbb{D}\_{\hat{Z}}^{1,2} will denote the domain of the derivative operator D^^𝐷\hat{D} under P^^𝑃\hat{P}, with respect to Z^^𝑍\hat{Z}. We will write 𝕃Z^1,2=L2​([0,T],𝔻Z^1,2)superscriptsubscript𝕃^𝑍

12superscript𝐿20𝑇superscriptsubscript𝔻^𝑍

12\mathbb{L}\_{\hat{Z}}^{1,2}=L^{2}([0,T],\mathbb{D}\_{\hat{Z}}^{1,2}). Notice that as T→0→𝑇0T\to 0, supr,s∈[0,T]E^t​|D^s​σi−D+​σ0i|→0→subscriptsupremum

𝑟𝑠
0𝑇subscript^𝐸𝑡subscript^𝐷𝑠superscript𝜎𝑖superscript𝐷subscriptsuperscript𝜎𝑖00\sup\_{r,s\in[0,T]}\hat{E}\_{t}|\hat{D}\_{s}\sigma^{i}-D^{+}\sigma^{i}\_{0}|\to 0, for i=X,Y𝑖

𝑋𝑌i=X,Y, where D+​σ0isuperscript𝐷superscriptsubscript𝜎0𝑖D^{+}\sigma\_{0}^{i} are defined as in (H5) and E^tsubscript^𝐸𝑡\hat{E}\_{t} is the conditional expectation with respect to P^^𝑃\hat{P}.

###### Theorem 7

Consider the model ([1](#S2.E1 "In 2 The objective, the price model and notation ‣ On the optimal choice of strike conventions in exchange option pricing")) and assume that σ~∈𝕃Z^1,2~𝜎superscriptsubscript𝕃^𝑍

12\tilde{\sigma}\in\mathbb{L}\_{\hat{Z}}^{1,2}.
Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0∂γ^∂y​(x,x)=ρX​σ0X−ρY​σ0Y2​σ~3​[D+​σ0X​(σ0X−ρ​σ0Y)+D+​σ0Y​(σ0Y−ρ​σ0X)].subscript→𝑇0^𝛾𝑦𝑥𝑥subscript𝜌𝑋superscriptsubscript𝜎0𝑋subscript𝜌𝑌superscriptsubscript𝜎0𝑌2superscript~𝜎3delimited-[]superscript𝐷superscriptsubscript𝜎0𝑋superscriptsubscript𝜎0𝑋𝜌superscriptsubscript𝜎0𝑌superscript𝐷superscriptsubscript𝜎0𝑌superscriptsubscript𝜎0𝑌𝜌superscriptsubscript𝜎0𝑋\lim\_{T\to 0}\frac{\partial\hat{\gamma}}{\partial y}(x,x)=\frac{\rho\_{X}\sigma\_{0}^{X}-\rho\_{Y}\sigma\_{0}^{Y}}{2\tilde{\sigma}^{3}}\left[D^{+}\sigma\_{0}^{X}(\sigma\_{0}^{X}-\rho\sigma\_{0}^{Y})+D^{+}\sigma\_{0}^{Y}(\sigma\_{0}^{Y}-\rho\sigma\_{0}^{X})\right]. |  | (12) |

Proof. We have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | V0=B​S​(0,x,y,γ^).subscript𝑉0𝐵𝑆0𝑥𝑦^𝛾V\_{0}=BS(0,x,y,\hat{\gamma}). |  | (13) |

On the one hand, a direct computation gives us that

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​S​(0,x,y,γ^)=ey​B​S​(0,x−y,0,γ^)𝐵𝑆0𝑥𝑦^𝛾superscript𝑒𝑦𝐵𝑆0𝑥𝑦0^𝛾BS(0,x,y,\hat{\gamma})=e^{y}BS(0,x-y,0,\hat{\gamma}) |  | (14) |

On the other hand

|  |  |  |
| --- | --- | --- |
|  | V0=E​(eXT−eYT)+subscript𝑉0𝐸superscriptsuperscript𝑒subscript𝑋𝑇superscript𝑒subscript𝑌𝑇\displaystyle V\_{0}=E\left(e^{X\_{T}}-e^{Y\_{T}}\right)^{+} |  |
|  |  |  |
| --- | --- | --- |
|  | =eY0​E^​(eXT−YT−1)+absentsuperscript𝑒subscript𝑌0^𝐸superscriptsuperscript𝑒subscript𝑋𝑇subscript𝑌𝑇1\displaystyle=e^{Y\_{0}}\hat{E}\left(e^{X\_{T}-Y\_{T}}-1\right)^{+} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =ey​E^​(eXT−YT−1)+absentsuperscript𝑒𝑦^𝐸superscriptsuperscript𝑒subscript𝑋𝑇subscript𝑌𝑇1\displaystyle=e^{y}\hat{E}\left(e^{X\_{T}-Y\_{T}}-1\right)^{+} |  | (15) |

where E^^𝐸\hat{E} denotes the expectation with respect to the probability measure P^^𝑃\hat{P}. Notice that, under P^^𝑃\hat{P}, the process Ut:=eXt−Ytassignsubscript𝑈𝑡superscript𝑒subscript𝑋𝑡subscript𝑌𝑡U\_{t}:=e^{X\_{t}-Y\_{t}} satisfies

|  |  |  |
| --- | --- | --- |
|  | d​Ut=Ut​(σtX​d​W^tX−σtY​d​W^tY),𝑑subscript𝑈𝑡subscript𝑈𝑡subscriptsuperscript𝜎𝑋𝑡𝑑superscriptsubscript^𝑊𝑡𝑋subscriptsuperscript𝜎𝑌𝑡𝑑superscriptsubscript^𝑊𝑡𝑌dU\_{t}=U\_{t}(\sigma^{X}\_{t}d\hat{W}\_{t}^{X}-\sigma^{Y}\_{t}d\hat{W}\_{t}^{Y}), |  |

where W^X,W^Y

superscript^𝑊𝑋superscript^𝑊𝑌\hat{W}^{X},\hat{W}^{Y} are P^^𝑃\hat{P}-Brownian motions.
Then, ([14](#S3.E14 "In 3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing")) and ([3](#S3.Ex25 "3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing")) gives us that ([13](#S3.E13 "In 3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing")) is equivalent to

|  |  |  |
| --- | --- | --- |
|  | E^​(UT−1)+=B​S​(0,x−y,0,γ^).^𝐸superscriptsubscript𝑈𝑇1𝐵𝑆0𝑥𝑦0^𝛾\hat{E}(U\_{T}-1)^{+}=BS(0,x-y,0,\hat{\gamma}). |  |

Notice that γ^^𝛾\hat{\gamma} is the implied volatility of a vanilla option with strike 1 on an underlying Utsubscript𝑈𝑡U\_{t}, with volatility σ~~𝜎\tilde{\sigma}.
Then Theorem [5](#Thmtheorem5 "Theorem 5 ‣ 3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing") gives us that

|  |  |  |
| --- | --- | --- |
|  | limT→0∂γ^∂z​(x,x)=14​σ~03​T​limT→0⟨U,M~⟩TT.subscript→𝑇0^𝛾𝑧𝑥𝑥14superscriptsubscript~𝜎03𝑇subscript→𝑇0subscript  𝑈~𝑀 𝑇𝑇\lim\_{T\to 0}\frac{\partial\hat{\gamma}}{\partial z}(x,x)=\frac{1}{4\tilde{\sigma}\_{0}^{3}T}\lim\_{T\to 0}\frac{\langle U,\tilde{M}\rangle\_{T}}{T}. |  |

Now, as

|  |  |  |
| --- | --- | --- |
|  | d​M~t=(∫tTE^r​(D^r​σ~t2)​𝑑r)​d​Z^t𝑑subscript~𝑀𝑡superscriptsubscript𝑡𝑇subscript^𝐸𝑟subscript^𝐷𝑟superscriptsubscript~𝜎𝑡2differential-d𝑟𝑑subscript^𝑍𝑡d\tilde{M}\_{t}=\left(\int\_{t}^{T}\hat{E}\_{r}(\hat{D}\_{r}\tilde{\sigma}\_{t}^{2})dr\right)d\hat{Z}\_{t} |  |

and

|  |  |  |
| --- | --- | --- |
|  | D^r​σ~t2=2​σtX​D^r​σtX+2​σtY​D^r​σtY−2​ρ​σtX​D^r​σtY−2​ρ​σtY​D^r​σtX.subscript^𝐷𝑟superscriptsubscript~𝜎𝑡22superscriptsubscript𝜎𝑡𝑋subscript^𝐷𝑟superscriptsubscript𝜎𝑡𝑋2superscriptsubscript𝜎𝑡𝑌subscript^𝐷𝑟superscriptsubscript𝜎𝑡𝑌2𝜌superscriptsubscript𝜎𝑡𝑋subscript^𝐷𝑟superscriptsubscript𝜎𝑡𝑌2𝜌superscriptsubscript𝜎𝑡𝑌subscript^𝐷𝑟superscriptsubscript𝜎𝑡𝑋\hat{D}\_{r}\tilde{\sigma}\_{t}^{2}=2\sigma\_{t}^{X}\hat{D}\_{r}\sigma\_{t}^{X}+2\sigma\_{t}^{Y}\hat{D}\_{r}\sigma\_{t}^{Y}-2\rho\sigma\_{t}^{X}\hat{D}\_{r}\sigma\_{t}^{Y}-2\rho\sigma\_{t}^{Y}\hat{D}\_{r}\sigma\_{t}^{X}. |  |

we get that

|  |  |  |
| --- | --- | --- |
|  | 14​σ~03​T​limT→0⟨U,M~⟩=ρX​σ0X−ρY​σ0Y2​σ~03​[D+​σ0X​(σ0X−ρ​σ0Y)+D+​σ0Y​(σ0Y−ρ​σ0X)].14superscriptsubscript~𝜎03𝑇subscript→𝑇0  𝑈~𝑀subscript𝜌𝑋superscriptsubscript𝜎0𝑋subscript𝜌𝑌superscriptsubscript𝜎0𝑌2superscriptsubscript~𝜎03delimited-[]superscript𝐷superscriptsubscript𝜎0𝑋superscriptsubscript𝜎0𝑋𝜌superscriptsubscript𝜎0𝑌superscript𝐷superscriptsubscript𝜎0𝑌superscriptsubscript𝜎0𝑌𝜌superscriptsubscript𝜎0𝑋\frac{1}{4\tilde{\sigma}\_{0}^{3}T}\lim\_{T\to 0}\langle U,\tilde{M}\rangle=\frac{\rho\_{X}\sigma\_{0}^{X}-\rho\_{Y}\sigma\_{0}^{Y}}{2\tilde{\sigma}\_{0}^{3}}\left[D^{+}\sigma\_{0}^{X}(\sigma\_{0}^{X}-\rho\sigma\_{0}^{Y})+D^{+}\sigma\_{0}^{Y}(\sigma\_{0}^{Y}-\rho\sigma\_{0}^{X})\right]. |  |

This completes the proof.

In the next theorem we establish a condition for a strike convention to be a 111-STOSC. This is the main result of this paper.

###### Theorem 8

Consider the model ([1](#S2.E1 "In 2 The objective, the price model and notation ‣ On the optimal choice of strike conventions in exchange option pricing")) and assume that hypotheses (H1)-(H5) hold. Then, a strike covention (k1,k2)subscript𝑘1subscript𝑘2(k\_{1},k\_{2}) is a 111-STOSC if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρX​σ0X−ρY​σ0Y2​σ~03​[D+​σ0X​(σ0X−ρ​σ0Y)+D+​σ0Y​(σ0Y−ρ​σ0X)]subscript𝜌𝑋superscriptsubscript𝜎0𝑋subscript𝜌𝑌superscriptsubscript𝜎0𝑌2superscriptsubscript~𝜎03delimited-[]superscript𝐷superscriptsubscript𝜎0𝑋superscriptsubscript𝜎0𝑋𝜌superscriptsubscript𝜎0𝑌superscript𝐷superscriptsubscript𝜎0𝑌superscriptsubscript𝜎0𝑌𝜌superscriptsubscript𝜎0𝑋\displaystyle\frac{\rho\_{X}\sigma\_{0}^{X}-\rho\_{Y}\sigma\_{0}^{Y}}{2\tilde{\sigma}\_{0}^{3}}\left[D^{+}\sigma\_{0}^{X}(\sigma\_{0}^{X}-\rho\sigma\_{0}^{Y})+D^{+}\sigma\_{0}^{Y}(\sigma\_{0}^{Y}-\rho\sigma\_{0}^{X})\right] |  | (16) |
|  |  |  |
| --- | --- | --- |
|  | =limT→0{1γ[IX∂IX∂z∂kX∂y+IY(∂IY∂z∂kY∂y+∂IY∂y)\displaystyle\quad=\lim\_{T\to 0}\left\{\frac{1}{\gamma}\left[I\_{X}\frac{\partial I\_{X}}{\partial z}\frac{\partial k\_{X}}{\partial y}+I\_{Y}\left(\frac{\partial I\_{Y}}{\partial z}\frac{\partial k\_{Y}}{\partial y}+\frac{\partial I\_{Y}}{\partial y}\right)\right.\right. |  |
|  |  |  |
| --- | --- | --- |
|  | −ρIX(∂IY∂z∂kY∂y+∂IY∂y)−ρIY∂IX∂z∂kX∂y](x,x)}\displaystyle\qquad\qquad\qquad\left.\left.-\rho I\_{X}\left(\frac{\partial I\_{Y}}{\partial z}\frac{\partial k\_{Y}}{\partial y}+\frac{\partial I\_{Y}}{\partial y}\right)-\rho I\_{Y}\frac{\partial I\_{X}}{\partial z}\frac{\partial k\_{X}}{\partial y}\right](x,x)\right\} |  |

Proof. We have to prove that

|  |  |  |
| --- | --- | --- |
|  | limT→0(∂γ∂y−∂γ^∂y)​(x,x)=0.subscript→𝑇0𝛾𝑦^𝛾𝑦𝑥𝑥0\lim\_{T\to 0}\left(\frac{\partial\gamma}{\partial y}-\frac{\partial\hat{\gamma}}{\partial y}\right)(x,x)=0. |  |

Theorems [5](#Thmtheorem5 "Theorem 5 ‣ 3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing") and [7](#Thmtheorem7 "Theorem 7 ‣ 3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing") directly give us the desired result.

###### Remark 9

If ρX≠0subscript𝜌𝑋0\rho\_{X}\neq 0 and ρY≠0subscript𝜌𝑌0\rho\_{Y}\neq 0, then D+​σ0i=σ0iρi​limT→0∂Ii∂zsuperscript𝐷superscriptsubscript𝜎0𝑖superscriptsubscript𝜎0𝑖subscript𝜌𝑖subscript→𝑇0subscript𝐼𝑖𝑧D^{+}\sigma\_{0}^{i}=\frac{\sigma\_{0}^{i}}{\rho\_{i}}\lim\_{T\to 0}\frac{\partial I\_{i}}{\partial z} for i=X,Y𝑖

𝑋𝑌i=X,Y. Then the left hand side in ([19](#S3.E19 "In Corollary 10 ‣ 3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing")) can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0ρX​IX−ρY​IYγ3​[∂IX∂z​IXρX​(IX−ρ​IY)+∂IY∂z​IYρY​(IY−ρ​IX)]​(x,x).subscript→𝑇0subscript𝜌𝑋subscript𝐼𝑋subscript𝜌𝑌subscript𝐼𝑌superscript𝛾3delimited-[]subscript𝐼𝑋𝑧subscript𝐼𝑋subscript𝜌𝑋subscript𝐼𝑋𝜌subscript𝐼𝑌subscript𝐼𝑌𝑧subscript𝐼𝑌subscript𝜌𝑌subscript𝐼𝑌𝜌subscript𝐼𝑋𝑥𝑥\lim\_{T\to 0}\frac{\rho\_{X}I\_{X}-\rho\_{Y}I\_{Y}}{\gamma^{3}}\left[\frac{\partial I\_{X}}{\partial z}\frac{I\_{X}}{\rho\_{X}}(I\_{X}-\rho I\_{Y})+\frac{\partial I\_{Y}}{\partial z}\frac{I\_{Y}}{\rho\_{Y}}(I\_{Y}-\rho I\_{X})\right](x,x). |  | (17) |

This gives us a model-free condition for a 111-STOSC, in the sense that a specific model for the volatility processes is not needed.

While various different cases of the general rule above may be considered, a convenient particular case of a strike convention is obtained if σtX=λX​σtsubscriptsuperscript𝜎𝑋𝑡subscript𝜆𝑋subscript𝜎𝑡\sigma^{X}\_{t}=\lambda\_{X}\sigma\_{t} and σtY=λY​σtsubscriptsuperscript𝜎𝑌𝑡subscript𝜆𝑌subscript𝜎𝑡\sigma^{Y}\_{t}=\lambda\_{Y}\sigma\_{t}, where λXsubscript𝜆𝑋\lambda\_{X} and λYsubscript𝜆𝑌\lambda\_{Y} are positive constants and σtsubscript𝜎𝑡\sigma\_{t} is a non-negative, right-continuous and square integrable process adapted to the filtration generated by Ztsubscript𝑍𝑡Z\_{t}. We note that this case of a single volatility process shifted by a constant for each of the two assets is a generalization of the model introduced for correlation options in Bakshi and Madan (2000) and also for spread options in Dempster and Hong (2000). For convenience we shall refer to this model as the one-volatility two-levels (1V2L) model. The following corollary demonstrates that for the 1V2L model a strike convention can be derived either in terms of model parameters or market observables, namely the short-time limits of the corresponding vanilla implied volatility levels and skews.

###### Corollary 10

Assume the 1V2L model. Then, a strike covention (k1,k2)subscript𝑘1subscript𝑘2(k\_{1},k\_{2}) is a 111-STOSC if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0[(1−ρIYIX)∂IX∂z∂kX∂y+(IYIX−ρ)(∂IY∂z∂kY∂y+∂IY∂y)\displaystyle\lim\_{T\to 0}\left[\left(1-\rho\frac{I\_{Y}}{I\_{X}}\right)\frac{\partial I\_{X}}{\partial z}\frac{\partial k\_{X}}{\partial y}+\left(\frac{I\_{Y}}{I\_{X}}-\rho\right)\left(\frac{\partial I\_{Y}}{\partial z}\frac{\partial k\_{Y}}{\partial y}+\frac{\partial I\_{Y}}{\partial y}\right)\right. |  | (18) |
|  |  |  |
| --- | --- | --- |
|  | −∂IX∂z+IYIX∂IY∂z](x,x)=0.\displaystyle\qquad-\left.\frac{\partial I\_{X}}{\partial z}+\frac{I\_{Y}}{I\_{X}}\frac{\partial I\_{Y}}{\partial z}\right](x,x)=0. |  |

or equivalently (in terms of model parameters):

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−ρ​λYλX)​ρXρY​∂kX∂y+(λYλX−ρ)​(∂kY∂y−1)=ρXρY−λYλX1𝜌subscript𝜆𝑌subscript𝜆𝑋subscript𝜌𝑋subscript𝜌𝑌subscript𝑘𝑋𝑦subscript𝜆𝑌subscript𝜆𝑋𝜌subscript𝑘𝑌𝑦1subscript𝜌𝑋subscript𝜌𝑌subscript𝜆𝑌subscript𝜆𝑋\left(1-\rho\frac{\lambda\_{Y}}{\lambda\_{X}}\right)\frac{\rho\_{X}}{\rho\_{Y}}\frac{\partial k\_{X}}{\partial y}+\left(\frac{\lambda\_{Y}}{\lambda\_{X}}-\rho\right)\left(\frac{\partial k\_{Y}}{\partial y}-1\right)=\frac{\rho\_{X}}{\rho\_{Y}}-\frac{\lambda\_{Y}}{\lambda\_{X}} |  | (19) |

Proof. In the 1V2L model (with σtX=λX​σtsuperscriptsubscript𝜎𝑡𝑋subscript𝜆𝑋subscript𝜎𝑡\sigma\_{t}^{X}=\lambda\_{X}\sigma\_{t}, σtY=λY​σtsuperscriptsubscript𝜎𝑡𝑌subscript𝜆𝑌subscript𝜎𝑡\sigma\_{t}^{Y}=\lambda\_{Y}\sigma\_{t}), Theorem [5](#Thmtheorem5 "Theorem 5 ‣ 3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing") implies that

|  |  |  |
| --- | --- | --- |
|  | ∂IY∂z=ρYρX​∂IX∂z.subscript𝐼𝑌𝑧subscript𝜌𝑌subscript𝜌𝑋subscript𝐼𝑋𝑧\frac{\partial I\_{Y}}{\partial z}=\frac{\rho\_{Y}}{\rho\_{X}}\frac{\partial I\_{X}}{\partial z}. |  |

Expanding the expression in ([17](#S3.E17 "In Remark 9 ‣ 3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing")) and substituting for ∂IY∂zsubscript𝐼𝑌𝑧\frac{\partial I\_{Y}}{\partial z} we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =\displaystyle= | limT→0[1γ3​(ρX​IX−ρY​IY)​∂IX∂z​1ρX​(IX​(IX−ρ​IY)+IY​(IY−ρ​IX))]​(x,x)subscript→𝑇0delimited-[]1superscript𝛾3subscript𝜌𝑋subscript𝐼𝑋subscript𝜌𝑌subscript𝐼𝑌subscript𝐼𝑋𝑧1subscript𝜌𝑋subscript𝐼𝑋subscript𝐼𝑋𝜌subscript𝐼𝑌subscript𝐼𝑌subscript𝐼𝑌𝜌subscript𝐼𝑋𝑥𝑥\displaystyle\lim\_{T\to 0}\left[\frac{1}{\gamma^{3}}\left(\rho\_{X}I\_{X}-\rho\_{Y}I\_{Y}\right)\frac{\partial I\_{X}}{\partial z}\frac{1}{\rho\_{X}}\left(I\_{X}(I\_{X}-\rho I\_{Y})+I\_{Y}(I\_{Y}-\rho I\_{X})\right)\right](x,x) |  |
|  |  | =\displaystyle= | limT→0[1γ3​(IX​∂IX∂z−IY​ρYρX​∂IX∂z)​(IX​(IX−ρ​IY)+IY​(IY−ρ​IX))]​(x,x)subscript→𝑇0delimited-[]1superscript𝛾3subscript𝐼𝑋subscript𝐼𝑋𝑧subscript𝐼𝑌subscript𝜌𝑌subscript𝜌𝑋subscript𝐼𝑋𝑧subscript𝐼𝑋subscript𝐼𝑋𝜌subscript𝐼𝑌subscript𝐼𝑌subscript𝐼𝑌𝜌subscript𝐼𝑋𝑥𝑥\displaystyle\lim\_{T\to 0}\left[\frac{1}{\gamma^{3}}\left(I\_{X}\frac{\partial I\_{X}}{\partial z}-I\_{Y}\frac{\rho\_{Y}}{\rho\_{X}}\frac{\partial I\_{X}}{\partial z}\right)\left(I\_{X}(I\_{X}-\rho I\_{Y})+I\_{Y}(I\_{Y}-\rho I\_{X})\right)\right](x,x) |  |
|  |  | =\displaystyle= | limT→0[1γ3​(IX​∂IX∂z−IY​∂IY∂z)​γ2]​(x,x)subscript→𝑇0delimited-[]1superscript𝛾3subscript𝐼𝑋subscript𝐼𝑋𝑧subscript𝐼𝑌subscript𝐼𝑌𝑧superscript𝛾2𝑥𝑥\displaystyle\lim\_{T\to 0}\left[\frac{1}{\gamma^{3}}\left(I\_{X}\frac{\partial I\_{X}}{\partial z}-I\_{Y}\frac{\partial I\_{Y}}{\partial z}\right)\gamma^{2}\right](x,x) |  |
|  |  | =\displaystyle= | limT→0[1γ​(IX​∂IX∂z−IY​∂IY∂z)]​(x,x)subscript→𝑇0delimited-[]1𝛾subscript𝐼𝑋subscript𝐼𝑋𝑧subscript𝐼𝑌subscript𝐼𝑌𝑧𝑥𝑥\displaystyle\lim\_{T\to 0}\left[\frac{1}{\gamma}\left(I\_{X}\frac{\partial I\_{X}}{\partial z}-I\_{Y}\frac{\partial I\_{Y}}{\partial z}\right)\right](x,x) |  |

Equating this with the right hand side of ([16](#S3.E16 "In Theorem 8 ‣ 3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing")) and rearranging gives the desired result. The equivalent result in terms of model parameters ρX,ρY,λX,λY

subscript𝜌𝑋subscript𝜌𝑌subscript𝜆𝑋subscript𝜆𝑌\rho\_{X},\rho\_{Y},\lambda\_{X},\lambda\_{Y} can be found by Theorem [5](#Thmtheorem5 "Theorem 5 ‣ 3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing") and the fact that the at-the-money (ATM) implied volatility tends to the corresponding spot volatilty at time zero.

## 4 Optimal linear log-strike conventions

Several strike conventions have been proposed in the literature. Some
classical examples (see for example Alexander and Venkatramanan (2011)
and Swindle (2014)) are of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | {kX​(x,y)=(1−a)​x+a​ykY​(x,y)=a​x+(1−a)​y,casessubscript𝑘𝑋𝑥𝑦1𝑎𝑥𝑎𝑦subscript𝑘𝑌𝑥𝑦𝑎𝑥1𝑎𝑦\left\{\begin{array}[]{c}k\_{X}(x,y)=(1-a)x+ay\\ k\_{Y}(x,y)=ax+(1-a)y\end{array}\right., |  | (20) |

for some real number a𝑎a. For example, in Swindle (2014) the authors
suggest to take kX=ln⁡StYsubscript𝑘𝑋superscriptsubscript𝑆𝑡𝑌k\_{X}=\ln S\_{t}^{Y} and kY=ln⁡StX.subscript𝑘𝑌superscriptsubscript𝑆𝑡𝑋k\_{Y}=\ln S\_{t}^{X}. This choice
corresponds to ([20](#S4.E20 "In 4 Optimal linear log-strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing")) in the case a=1.𝑎1a=1.
On the other hand, in Alexander and Venkatramanan (2011) the authors
mostly study the strike convention kX=ln⁡StXsubscript𝑘𝑋superscriptsubscript𝑆𝑡𝑋k\_{X}=\ln S\_{t}^{X} and kY=ln⁡StYsubscript𝑘𝑌superscriptsubscript𝑆𝑡𝑌k\_{Y}=\ln S\_{t}^{Y}, which is the case a=0𝑎0a=0.
In this section we will find an optimal linear log-strike option of the form
([20](#S4.E20 "In 4 Optimal linear log-strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing")). Given two strikes kX,kY

subscript𝑘𝑋subscript𝑘𝑌k\_{X},k\_{Y} of the form ([20](#S4.E20 "In 4 Optimal linear log-strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing")), we have

|  |  |  |
| --- | --- | --- |
|  | ∂kX∂y=a,∂kY∂y=1−a,formulae-sequencesubscript𝑘𝑋𝑦𝑎subscript𝑘𝑌𝑦1𝑎\frac{\partial k\_{X}}{\partial y}=a,\quad\frac{\partial k\_{Y}}{\partial y}=1-a, |  |

and thus equation ([19](#S3.E19 "In Corollary 10 ‣ 3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing")) reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | a​[ρXρY​(1−ρ​λYλX)−(λYλX−ρ)]=ρXρY−λYλX.𝑎delimited-[]subscript𝜌𝑋subscript𝜌𝑌1𝜌subscript𝜆𝑌subscript𝜆𝑋subscript𝜆𝑌subscript𝜆𝑋𝜌subscript𝜌𝑋subscript𝜌𝑌subscript𝜆𝑌subscript𝜆𝑋a\left[\frac{\rho\_{X}}{\rho\_{Y}}\left(1-\frac{\rho\lambda\_{Y}}{\lambda\_{X}}\right)-\left(\frac{\lambda\_{Y}}{\lambda\_{X}}-\rho\right)\right]=\frac{\rho\_{X}}{\rho\_{Y}}-\frac{\lambda\_{Y}}{\lambda\_{X}}. |  | (21) |

or, alternatively,

|  |  |  |
| --- | --- | --- |
|  | a​[ρX​(λX−ρ​λY)−ρY​(λY−ρ​λX)]=λX​ρX−ρY​λY.𝑎delimited-[]subscript𝜌𝑋subscript𝜆𝑋𝜌subscript𝜆𝑌subscript𝜌𝑌subscript𝜆𝑌𝜌subscript𝜆𝑋subscript𝜆𝑋subscript𝜌𝑋subscript𝜌𝑌subscript𝜆𝑌a\left[\rho\_{X}(\lambda\_{X}-\rho\lambda\_{Y})-\rho\_{Y}(\lambda\_{Y}-\rho\lambda\_{X})\right]=\lambda\_{X}\rho\_{X}-\rho\_{Y}\lambda\_{Y}. |  |

Then, if

|  |  |  |
| --- | --- | --- |
|  | [ρX(λX−ρλY)−ρY(λY−ρλX)≠0[\rho\_{X}(\lambda\_{X}-\rho\lambda\_{Y})-\rho\_{Y}(\lambda\_{Y}-\rho\lambda\_{X})\neq 0 |  |

there exists a unique 111-STOSC, given by a=a⋆𝑎superscript𝑎⋆a=a^{\star}, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | a⋆=ρX​λX−ρY​λYρX​(λX−ρ​λY)−ρY​(λY−ρ​λX)superscript𝑎⋆subscript𝜌𝑋subscript𝜆𝑋subscript𝜌𝑌subscript𝜆𝑌subscript𝜌𝑋subscript𝜆𝑋𝜌subscript𝜆𝑌subscript𝜌𝑌subscript𝜆𝑌𝜌subscript𝜆𝑋a^{\star}=\frac{\rho\_{X}\lambda\_{X}-\rho\_{Y}\lambda\_{Y}}{\rho\_{X}(\lambda\_{X}-\rho\lambda\_{Y})-\rho\_{Y}(\lambda\_{Y}-\rho\lambda\_{X})} |  | (22) |

###### Remark 11

We note several interesting special cases related to this result:

1. 1.

   The underlying prices SXsuperscript𝑆𝑋S^{X} and SYsuperscript𝑆𝑌S^{Y} are uncorrelated (ρ=0𝜌0\rho=0):

   |  |  |  |
   | --- | --- | --- |
   |  | a⋆=ρX​λX−ρY​λYρX​λX−ρY​λY=1superscript𝑎⋆subscript𝜌𝑋subscript𝜆𝑋subscript𝜌𝑌subscript𝜆𝑌subscript𝜌𝑋subscript𝜆𝑋subscript𝜌𝑌subscript𝜆𝑌1a^{\star}=\frac{\rho\_{X}\lambda\_{X}-\rho\_{Y}\lambda\_{Y}}{\rho\_{X}\lambda\_{X}-\rho\_{Y}\lambda\_{Y}}=1 |  |

   Intuitively, thinking of an exchange option as a regular option with floating strike, if the strike is uncorrelated, then it is optimal to use the implied volatility corresponding to that floating strike (to the opposite leg of the spread), the ‘volatility look-up heuristic’ of Swindle (2014).
2. 2.

   The two volatilities have the same level (λX=λYsubscript𝜆𝑋subscript𝜆𝑌\lambda\_{X}=\lambda\_{Y}):

   |  |  |  |
   | --- | --- | --- |
   |  | a⋆=ρX−ρYρX​(1−ρ)−ρY​(1−ρ)=11−ρsuperscript𝑎⋆subscript𝜌𝑋subscript𝜌𝑌subscript𝜌𝑋1𝜌subscript𝜌𝑌1𝜌11𝜌a^{\star}=\frac{\rho\_{X}-\rho\_{Y}}{\rho\_{X}(1-\rho)-\rho\_{Y}(1-\rho)}=\frac{1}{1-\rho} |  |

   Notice that in this case a⋆superscript𝑎⋆a^{\star} is no longer dependent on ρX,ρY,λX,λY
   subscript𝜌𝑋subscript𝜌𝑌subscript𝜆𝑋subscript𝜆𝑌\rho\_{X},\rho\_{Y},\lambda\_{X},\lambda\_{Y}.
3. 3.

   The two asset to volatility correlations are equal (ρX=ρYsubscript𝜌𝑋subscript𝜌𝑌\rho\_{X}=\rho\_{Y}):

   |  |  |  |
   | --- | --- | --- |
   |  | a⋆=λX−λYλX−ρλY−λY+ρλX)=11+ρa^{\star}=\frac{\lambda\_{X}-\lambda\_{Y}}{\lambda\_{X}-\rho\lambda\_{Y}-\lambda\_{Y}+\rho\lambda\_{X})}=\frac{1}{1+\rho} |  |

   Again, here a⋆superscript𝑎⋆a^{\star} no longer depends on correlations ρX,ρY
   subscript𝜌𝑋subscript𝜌𝑌\rho\_{X},\rho\_{Y} or levels λX,λY
   subscript𝜆𝑋subscript𝜆𝑌\lambda\_{X},\lambda\_{Y}.
4. 4.

   Asset to volatility correlation is zero ( ρY=0subscript𝜌𝑌0\rho\_{Y}=0):

   |  |  |  |
   | --- | --- | --- |
   |  | a⋆=λX​ρXρX​(λX−ρ​λY)=λXλX−ρ​λYsuperscript𝑎⋆subscript𝜆𝑋subscript𝜌𝑋subscript𝜌𝑋subscript𝜆𝑋𝜌subscript𝜆𝑌subscript𝜆𝑋subscript𝜆𝑋𝜌subscript𝜆𝑌a^{\star}=\frac{\lambda\_{X}\rho\_{X}}{\rho\_{X}(\lambda\_{X}-\rho\lambda\_{Y})}=\frac{\lambda\_{X}}{\lambda\_{X}-\rho\lambda\_{Y}} |  |

   Similarly, if ρX=0subscript𝜌𝑋0\rho\_{X}=0, then a⋆=λYλY−ρ​λXsuperscript𝑎⋆subscript𝜆𝑌subscript𝜆𝑌𝜌subscript𝜆𝑋a^{\star}=\frac{\lambda\_{Y}}{\lambda\_{Y}-\rho\lambda\_{X}}. In these cases we can also conclude (since λX,λY>0
   subscript𝜆𝑋subscript𝜆𝑌0\lambda\_{X},\lambda\_{Y}>0) that ρ>0𝜌0\rho>0 corresponds to a⋆>1superscript𝑎⋆1a^{\star}>1 (and ρ<0𝜌0\rho<0 to a⋆<1superscript𝑎⋆1a^{\star}<1), intuitive for a floating strike option in which the strike tends to move away as S𝑆S moves towards it.

###### Remark 12

Similarly to the equivalence expressions within Corollary [10](#Thmtheorem10 "Corollary 10 ‣ 3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing"), we note that since λYλX=limT→0IYIXsubscript𝜆𝑌subscript𝜆𝑋subscript→𝑇0subscript𝐼𝑌subscript𝐼𝑋\frac{\lambda\_{Y}}{\lambda\_{X}}=\lim\_{T\to 0}\frac{I\_{Y}}{I\_{X}} and ρYρX=limT→0∂IY/∂z∂IX/∂zsubscript𝜌𝑌subscript𝜌𝑋subscript→𝑇0subscript𝐼𝑌𝑧subscript𝐼𝑋𝑧\frac{\rho\_{Y}}{\rho\_{X}}=\lim\_{T\to 0}\frac{\partial I\_{Y}/\partial z}{\partial I\_{X}/\partial z},
our results can be transformed from model parameters to market observables. Thus, the optimal strke convention can be computed from equation ([21](#S4.E21 "In 4 Optimal linear log-strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing")), needing only to know ρ𝜌\rho (often estimated from price histories) and the short-time limits of the corresponding vanilla implied volatility levels and skews.

## 5 Numerical examples

In order to investigate the performance of the optimal log-linear strike convention given by ([22](#S4.E22 "In 4 Optimal linear log-strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing")), we consider a number of numerical examples of spread option pricing with different assumptions for parameter values. In each case we compare our optimal choice of a⋆superscript𝑎⋆a^{\star} to results from using the other common strike conventions of ‘at-the-money’ (ATM) implied volatilities for each asset (i.e. a=0𝑎0a=0) or the volatility look-up heuristic (i.e. a=1𝑎1a=1). As a simple and commonly-used benchmark, we use the Heston Model throughout, but conduct tests under a large variety of different parameter sets.

Volatility dynamics are given by:

|  |  |  |
| --- | --- | --- |
|  | d​σt2=κ​(θ−σt2)​d​t+ν​σt2​d​Zt(3),𝑑superscriptsubscript𝜎𝑡2𝜅𝜃superscriptsubscript𝜎𝑡2𝑑𝑡𝜈superscriptsubscript𝜎𝑡2𝑑superscriptsubscript𝑍𝑡3d\sigma\_{t}^{2}=\kappa\left(\theta-\sigma\_{t}^{2}\right)dt+\nu\sqrt{\sigma\_{t}^{2}}dZ\_{t}^{(3)}, |  |

within the 1V2L model, a version of model ([1](#S2.E1 "In 2 The objective, the price model and notation ‣ On the optimal choice of strike conventions in exchange option pricing")) introduced before Corollary [10](#Thmtheorem10 "Corollary 10 ‣ 3 The construction of optimal strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing").

### 5.1 Test Cases

For now, we consider two test cases with parameters as described below, varying only ρYsubscript𝜌𝑌\rho\_{Y} between cases:

* •

  option maturity: T=0.05𝑇0.05T=0.05 (a few weeks)
* •

  volatility process (σtsubscript𝜎𝑡\sigma\_{t}) parameters: κ=1.5,θ=0.15,ν=0.5,σ0=0.15formulae-sequence𝜅1.5formulae-sequence𝜃0.15formulae-sequence𝜈0.5subscript𝜎00.15\kappa=1.5,\theta=0.15,\nu=0.5,\sigma\_{0}=0.15
* •

  volatility scaling factors: λX=1.5,λY=1formulae-sequencesubscript𝜆𝑋1.5subscript𝜆𝑌1\lambda\_{X}=1.5,\lambda\_{Y}=1
* •

  correlation parameters: ρ=0.5,ρX=−0.4formulae-sequence𝜌0.5subscript𝜌𝑋0.4\rho=0.5,\rho\_{X}=-0.4, and ρY=−0.6subscript𝜌𝑌0.6\rho\_{Y}=-0.6 or ρY=0.4subscript𝜌𝑌0.4\rho\_{Y}=0.4

Note that Test Case 1 with ρY=−0.6subscript𝜌𝑌0.6\rho\_{Y}=-0.6 corresponds to two downward-sloping implied volatility skews for the two assets, while Test Case 2 with ρY=0.4subscript𝜌𝑌0.4\rho\_{Y}=0.4 produces an upwards skew for the second asset. The top row of Figure [1](#S5.F1 "Figure 1 ‣ 5.1 Test Cases ‣ 5 Numerical examples ‣ On the optimal choice of strike conventions in exchange option pricing") shows these implied volatility plots, generated by pricing single asset options under the Heston model. We then use these saved implied volatilities to price an exchange option with payoff (STX−STY)+superscriptsubscriptsuperscript𝑆𝑋𝑇subscriptsuperscript𝑆𝑌𝑇(S^{X}\_{T}-S^{Y}\_{T})^{+} across a range of moneyness, with S0X=100subscriptsuperscript𝑆𝑋0100S^{X}\_{0}=100 fixed and S0Y∈[80,120]subscriptsuperscript𝑆𝑌080120S^{Y}\_{0}\in[80,120]. Margrabe’s formula with the three different strike conventions (choices of a𝑎a) is compared against an ‘exact solution’ using 1,000,000 simulated paths (with the constant volatility solution as a control variate).

![Refer to caption](/html/1807.05396/assets/x1.png)

![Refer to caption](/html/1807.05396/assets/x2.png)

![Refer to caption](/html/1807.05396/assets/x3.png)

![Refer to caption](/html/1807.05396/assets/x4.png)

![Refer to caption](/html/1807.05396/assets/x5.png)

![Refer to caption](/html/1807.05396/assets/x6.png)

![Refer to caption](/html/1807.05396/assets/x7.png)

![Refer to caption](/html/1807.05396/assets/x8.png)

Figure 1: Test case results against moneyness: implied volatility skews (first row), implied correlations (second row), spread option price ratios (third row) and price differences (fourth row). Left column is Test Case 1 (ρY=−0.6subscript𝜌𝑌0.6\rho\_{Y}=-0.6) and right column is Test Case 2 (ρY=0.4subscript𝜌𝑌0.4\rho\_{Y}=0.4).

Rows 2-4 of Figure [1](#S5.F1 "Figure 1 ‣ 5.1 Test Cases ‣ 5 Numerical examples ‣ On the optimal choice of strike conventions in exchange option pricing") provide three alternative ways of visualizing the performance of our optimal strike convention (the darkest line) across moneyness compared with the other approaches:
(i) by converting spread option prices back to implied correlations ρ^^𝜌\hat{\rho} in order to compare with the model correlation of ρ=0.5𝜌0.5\rho=0.5, recalling Remark [1](#S2.Ex8 "Remark 1 ‣ 2 The objective, the price model and notation ‣ On the optimal choice of strike conventions in exchange option pricing");
(ii) by plotting the ratio of Margrabe price to exact price;
(iii) by plotting the difference between Margrabe and exact.
Note that the ATM values (S0Y=100subscriptsuperscript𝑆𝑌0100S^{Y}\_{0}=100) are equal across strike conventions since they all coincide at this point, and ρ≈ρ^𝜌^𝜌\rho\approx\hat{\rho}. However, moving away from the ATM point (S0Y=100subscriptsuperscript𝑆𝑌0100S^{Y}\_{0}=100), we can clearly see that the optimal a⋆superscript𝑎⋆a^{\star} performs significantly better than the other contenders.

On Test Case 1 (left column) we see that a=0𝑎0a=0 significantly overprices the spread option (ρ^<ρ^𝜌𝜌\hat{\rho}<\rho) when S0Y<S0Xsubscriptsuperscript𝑆𝑌0subscriptsuperscript𝑆𝑋0S^{Y}\_{0}<S^{X}\_{0} (the ‘in the money’, or ITM, case) and underprices (ρ^>ρ^𝜌𝜌\hat{\rho}>\rho) when S0Y>S0Xsubscriptsuperscript𝑆𝑌0subscriptsuperscript𝑆𝑋0S^{Y}\_{0}>S^{X}\_{0} (the ‘out of the money’, or OTM, case), while a=1𝑎1a=1 does the opposite. It might therefore appear that a rather arbitrary midpoint convention of a=1/2𝑎12a=1/2 could work as a compromise between the other rules, but this is not surprising considering that a⋆=0.429superscript𝑎⋆0.429a^{\star}=0.429 is optimal in this case. In contrast, on Test Case 2 (right column), a⋆=1.917superscript𝑎⋆1.917a^{\star}=1.917 is optimal, and thus both the other strike conventions overprice ITM and underprice OTM, sometimes by a large amount. Our approach keeps absolute errors in Case 1 below 0.01 and in Case 2 below 0.03 across different S0Ysubscriptsuperscript𝑆𝑌0S^{Y}\_{0} values. This consistent pricing of options at different moneyness levels is a major advantage. In practice an indicative quote on a different spread option in the market could therefore more accurately be used to price another contract.

Although dominated by skew, the implied correlation plots in Figure [1](#S5.F1 "Figure 1 ‣ 5.1 Test Cases ‣ 5 Numerical examples ‣ On the optimal choice of strike conventions in exchange option pricing") reveal a slight ‘frown’ in the first test case, as sometimes witnessed in the market. Ideally we would like to observe a flat line at ρ^=0.5^𝜌0.5\hat{\rho}=0.5, as the theory dictates should hold with short enough T𝑇T and near the money, but our results are nonetheless encouraging. Note that when looking at relative pricing errors in the third row of plots, errors unsurprisingly dominate for OTM options which always have zero intrinsic value and much lower prices than ITM. It is more interesting to note the patterns in the case of absolute errors just below, in particular that deep ITM and OTM options show less pricing error than moderately ITM and OTM. This effect can be explained by the fact that there is less (model-dependent) extrinsic value to accurately price.

### 5.2 Extensive Numerical Investigations

Instead of considering individual cases of parameter sets as above, we now test the approach across a wide range of different parameter values and in particular correlation structures. We use the following ranges for our parameters:111Note that sometimes round numbers (and zeros) are specifically avoided due to the unrealistically large values of |a⋆|superscript𝑎⋆|a^{\star}| they can produce in ([22](#S4.E22 "In 4 Optimal linear log-strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing")). This is not unreasonable considering that data fitting rarely produces round numbers!

* •

  T∈[0.05,0.1,0.25,0.5,1]𝑇
  0.050.10.250.51T\in[0.05,0.1,0.25,0.5,1]
* •

  S0X=100superscriptsubscript𝑆0𝑋100S\_{0}^{X}=100, S0Y∈[80,84,…,100,…,116,120]superscriptsubscript𝑆0𝑌
  8084…100…116120S\_{0}^{Y}\in[80,84,\ldots,100,\ldots,116,120]
* •

  λX=1subscript𝜆𝑋1\lambda\_{X}=1, λY=1.24subscript𝜆𝑌1.24\lambda\_{Y}=1.24 (note: tests for different λ𝜆\lambdas perform similarly)
* •

  Heston parameters (as before): κ=1.5,θ=0.15,ν=0.5,σ0=0.15formulae-sequence𝜅1.5formulae-sequence𝜃0.15formulae-sequence𝜈0.5subscript𝜎00.15\kappa=1.5,\theta=0.15,\nu=0.5,\sigma\_{0}=0.15
* •

  ρ∈[−0.9,−0.7,−0.5,−0.3,−0.1,0.1,0.3,0.5,0.7,0.9]𝜌
  0.90.70.50.30.10.10.30.50.70.9\rho\in[-0.9,-0.7,-0.5,-0.3,-0.1,0.1,0.3,0.5,0.7,0.9]
* •

  ρX∈[−0.72,−0.42,−0.12,0.18,0.48]subscript𝜌𝑋
  0.720.420.120.180.48\rho\_{X}\in[-0.72,-0.42,-0.12,0.18,0.48]
* •

  ρY∈[−0.61,−0.31,−0.01,0.29,0.59]subscript𝜌𝑌
  0.610.310.010.290.59\rho\_{Y}\in[-0.61,-0.31,-0.01,0.29,0.59]

We shall compare results using a variety of commonly-used pricing errors such as Mean Absolute Error (MAE), Mean Absolute Percentage Error (MAPE), Root Mean Squared Error (RMSE), Maximum Absolute Error (MaxAE, i.e. worst case), as well as considering the mean standard deviation (MStd) of errors across moneyness (S0Ysuperscriptsubscript𝑆0𝑌S\_{0}^{Y} grid). The first two correspond to the price ratio and price difference plots in Figure [1](#S5.F1 "Figure 1 ‣ 5.1 Test Cases ‣ 5 Numerical examples ‣ On the optimal choice of strike conventions in exchange option pricing") while the last of these is a way to assess the methodology’s aim of pricing consistently across moneyness, or in other words flattening the implied correlation skew or frown we would otherwise observe.

Table [1](#S5.T1 "Table 1 ‣ 5.2 Extensive Numerical Investigations ‣ 5 Numerical examples ‣ On the optimal choice of strike conventions in exchange option pricing") shows the MAE (between simulated prices and Margrabe prices), averaging over the S0Ysuperscriptsubscript𝑆0𝑌S\_{0}^{Y}, ρXsubscript𝜌𝑋\rho\_{X} and ρYsubscript𝜌𝑌\rho\_{Y} grids222Each number in the table is thus an average of 11×5×5=275115527511\times 5\times 5=275 cases (gridpoints)., for the different choices of ρ𝜌\rho, T𝑇T and of course a𝑎a. We only show half of our ρ𝜌\rho values here as a reasonable sample. When calculating average errors, we first exclude parameter sets which lead to a non-valid (non positive definite) correlation matrix. This is 19.6% of the cases overall, and around half of the cases for the most extreme values of ρ=±0.9𝜌plus-or-minus0.9\rho=\pm 0.9. We also exclude a very small number of OTM cases where Monte Carlo prices are less than 1 cent. While columns 1 to 3 of the table compare the alternative strike conventions of a=0𝑎0a=0 and a=1𝑎1a=1 with our optimal a⋆superscript𝑎⋆a^{\star}, the final column shows the ‘at-the-money (ATM) error’, meaning the error averaged over only the cases where S0Y=S0X=100superscriptsubscript𝑆0𝑌superscriptsubscript𝑆0𝑋100S\_{0}^{Y}=S\_{0}^{X}=100. Recall from Figure [1](#S5.F1 "Figure 1 ‣ 5.1 Test Cases ‣ 5 Numerical examples ‣ On the optimal choice of strike conventions in exchange option pricing") that ATM prices agree across all strike conventions (for any a𝑎a) since they all collapse onto the same choice of kX,kY

subscript𝑘𝑋subscript𝑘𝑌k\_{X},k\_{Y}. As discussed in Section 2, ATM error is zero as T→0→𝑇0T\to 0, but is non-zero here since T≥0.05𝑇0.05T\geq 0.05. In some sense, ATM error is thus the best we could hope for our strike convention to reach when averaging across all moneyness values.

|  | ρ𝜌\rho | a=0𝑎0a=0 | a=1𝑎1a=1 | a⋆superscript𝑎⋆a^{\star} | bounded a⋆superscript𝑎⋆a^{\star} | ATM error |
| --- | --- | --- | --- | --- | --- | --- |
| T=0.05𝑇0.05T=0.05 | -0.7 | 0.0646 | 0.053 | 0.0069 | 0.0069 | 0.0036 |
| -0.3 | 0.0591 | 0.0241 | 0.0066 | 0.0066 | 0.0048 |
| 0.1 | 0.0567 | 0.0064 | 0.0107 | 0.01 | 0.005 |
| 0.5 | 0.0408 | 0.0189 | 0.0193 | 0.0117 | 0.0039 |
| 0.9 | 0.0147 | 0.0121 | 0.005 | 0.0052 | 0.0018 |
| T=0.1𝑇0.1T=0.1 | -0.7 | 0.1108 | 0.0838 | 0.0117 | 0.0117 | 0.01 |
| -0.3 | 0.1064 | 0.0395 | 0.0132 | 0.0132 | 0.012 |
| 0.1 | 0.1093 | 0.0159 | 0.0217 | 0.0203 | 0.0121 |
| 0.5 | 0.091 | 0.0439 | 0.0426 | 0.0277 | 0.0102 |
| 0.9 | 0.0369 | 0.0304 | 0.0126 | 0.0138 | 0.004 |
| T=0.25𝑇0.25T=0.25 | -0.7 | 0.1943 | 0.1413 | 0.039 | 0.039 | 0.0426 |
| -0.3 | 0.1932 | 0.0787 | 0.0465 | 0.0465 | 0.0487 |
| 0.1 | 0.2074 | 0.0497 | 0.0561 | 0.0536 | 0.0441 |
| 0.5 | 0.1933 | 0.1004 | 0.095 | 0.0681 | 0.0345 |
| 0.9 | 0.1145 | 0.0948 | 0.0434 | 0.0465 | 0.0181 |
| T=1𝑇1T=1 | -0.7 | 0.3634 | 0.3097 | 0.2243 | 0.2243 | 0.2252 |
| -0.3 | 0.3976 | 0.2855 | 0.2632 | 0.2632 | 0.2724 |
| 0.1 | 0.4134 | 0.2436 | 0.2519 | 0.2488 | 0.2398 |
| 0.5 | 0.3898 | 0.2575 | 0.2464 | 0.2195 | 0.1856 |
| 0.9 | 0.3246 | 0.2735 | 0.1471 | 0.156 | 0.102 |

Table 1: Comparison of strike conventions by Mean Absolute Error (MAE) averaged across ρXsubscript𝜌𝑋\rho\_{X}, ρYsubscript𝜌𝑌\rho\_{Y} and S0Ysubscriptsuperscript𝑆𝑌0S^{Y}\_{0} grids, varying ρ𝜌\rho and T𝑇T as labelled on left.

As we see in Table [1](#S5.T1 "Table 1 ‣ 5.2 Extensive Numerical Investigations ‣ 5 Numerical examples ‣ On the optimal choice of strike conventions in exchange option pricing"), the optimal a⋆superscript𝑎⋆a^{\star} outperforms the other strike conventions in the vast majority of cases, often cuts MAE by more than 50% versus a=0𝑎0a=0 or a=1𝑎1a=1, and comes much closer to the ATM error. Interestingly, a=1𝑎1a=1 is much more competitive than a=0𝑎0a=0 and seems to slightly outperform a⋆superscript𝑎⋆a^{\star} as a convention when ρ𝜌\rho is near zero. However this is not so surprising considering that a⋆superscript𝑎⋆a^{\star} is often near 1 anyway in such cases, in line with the first special case in Remark [11](#Thmtheorem11 "Remark 11 ‣ 4 Optimal linear log-strike conventions ‣ On the optimal choice of strike conventions in exchange option pricing") earlier. Furthermore, the weakest cases of performance can often be attributed to unusually large (or very negative) values of a⋆superscript𝑎⋆a^{\star}, since they imply picking implied volatilities from deep ITM or OTM vanilla options, especially when |S0X−S0Y|superscriptsubscript𝑆0𝑋superscriptsubscript𝑆0𝑌\left|S\_{0}^{X}-S\_{0}^{Y}\right| is not small. This is of course also impractical in the real world. As a possible improvement, in the final column of the table we show the average pricing errors for when bounding a⋆superscript𝑎⋆a^{\star} in the range [−1,2]12[-1,2]. The extreme a⋆superscript𝑎⋆a^{\star} situation is more common for cases of positive and fairly high ρ𝜌\rho. For example, for ρ=0.5𝜌0.5\rho=0.5 here, a⋆superscript𝑎⋆a^{\star} happens to reach as high as 7.6 and as low as -3.7 at some gridpoints. Therefore, while the bounding of a⋆superscript𝑎⋆a^{\star} in [−1,2]12[-1,2] does not affect all rows, for ρ=0.5𝜌0.5\rho=0.5 it narrows the gap between a⋆superscript𝑎⋆a^{\star} and ATM error by about 50%. Tests on data would be required to better assess the impact of this point, but we leave this for further studies.

![Refer to caption](/html/1807.05396/assets/x9.png)


Figure 2: Comparison of strike conventions by Mean Absolute Percentage Errors (MAPE) for various T𝑇T (incl. ATM error and bounding / excluding high |a⋆|superscript𝑎⋆|a^{\star}|)

In addition to our earlier parameter set with very short maturity T=0.05𝑇0.05T=0.05, we are also interested in investigating the performance of the approach for larger T𝑇T. Moving down Table [1](#S5.T1 "Table 1 ‣ 5.2 Extensive Numerical Investigations ‣ 5 Numerical examples ‣ On the optimal choice of strike conventions in exchange option pricing"), results for longer maturity reveal that even without bounding (or excluding) trickier cases of high |a⋆|superscript𝑎⋆|a^{\star}|, our approach continues to perform well, always substantially outperforming a=0𝑎0a=0 and often significantly outperforming a=1𝑎1a=1 especially for higher |ρ|𝜌|\rho|. Interestingly, although the theory for a⋆superscript𝑎⋆a^{\star} was derived for short time to maturity, we see that the approach maintains a competitive advantage for large T𝑇T, even T=1𝑇1T=1. Overall MAE levels are higher in all cases when T𝑇T increases, but the increase stems from option prices being higher and from ATM error increasing, while the gap between a⋆superscript𝑎⋆a^{\star} and ATM error narrows to near zero. Since larger T𝑇T clearly implies larger option prices, it is insightful here to also consider MAPE. Figure [2](#S5.F2 "Figure 2 ‣ 5.2 Extensive Numerical Investigations ‣ 5 Numerical examples ‣ On the optimal choice of strike conventions in exchange option pricing") reveals the average MAPE across all cases (including the 10 values of ρ𝜌\rho) split by T𝑇T this time. Seen in percentage terms, ATM error grows steadily with T𝑇T, but error from all strike conventions actually falls. Our strike convention a⋆superscript𝑎⋆a^{\star} maintains a 0.5%-1.0% advantage over a=1𝑎1a=1 across maturities, and the bounded version improves this slightly. Moreover, if we exclude the more challenging gridpoints with a⋆∉[−1,2]superscript𝑎⋆12a^{\star}\notin[-1,2], the plot shows that MAPE falls significantly to be very close to ATM error especially for larger T𝑇T.

|  |  | No exclusions (normal case) | | | | | a⋆∉[−1,2]superscript𝑎⋆12a^{\star}\notin[-1,2] excluded | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | ρ𝜌\rho | a=0𝑎0a=0 | a=1𝑎1a=1 | a⋆superscript𝑎⋆a^{\star} | bounded | ATM | a=0𝑎0a=0 | a=1𝑎1a=1 | a⋆superscript𝑎⋆a^{\star} | ATM |
| T=0.1𝑇0.1T=0.1 | MAE | 0.0982 | 0.0502 | 0.022 | 0.0177 | 0.01 | 0.0949 | 0.0453 | 0.013 | 0.01 |
| MAPE | 4.23% | 2.76% | 1.78% | 1.48% | 0.14% | 3.18% | 1.89% | 0.62% | 0.15% |
| RMSE | 0.1288 | 0.0649 | 0.038 | 0.0248 | 0.0121 | 0.1235 | 0.0588 | 0.016 | 0.0122 |
| MaxAE | 0.3616 | 0.1768 | 0.2338 | 0.1041 | 0.0245 | 0.3445 | 0.1563 | 0.0408 | 0.0244 |
| MStd | 0.1137 | 0.0567 | 0.0169 | 0.0149 | n/a | 0.1098 | 0.051 | 0.0098 | n/a |
| T=0.25𝑇0.25T=0.25 | MAE | 0.1908 | 0.1029 | 0.0586 | 0.0512 | 0.0381 | 0.1806 | 0.0908 | 0.04 | 0.0381 |
| MAPE | 3.99% | 2.77% | 1.93% | 1.73% | 0.36% | 2.53% | 1.51% | 0.63% | 0.37% |
| RMSE | 0.2499 | 0.1307 | 0.0897 | 0.0688 | 0.0459 | 0.2356 | 0.1154 | 0.0481 | 0.0455 |
| MaxAE | 0.7359 | 0.3678 | 0.4695 | 0.274 | 0.0914 | 0.6899 | 0.3145 | 0.119 | 0.0881 |
| MStd | 0.2188 | 0.1067 | 0.0365 | 0.0336 | n/a | 0.2078 | 0.0928 | 0.0205 | n/a |

Table 2: Comparison of all results for five different error measures with all points included (left) and excluding a⋆<−1,a⋆>2formulae-sequencesuperscript𝑎⋆1superscript𝑎⋆2a^{\star}<-1,a^{\star}>2 cases (right). Results shown for all T=0.05𝑇0.05T=0.05 scenarios (top) and all T=0.25𝑇0.25T=0.25 scenarios (bottom).

We focused more on MAE above primarily due to the observation in Figure 1 that relative errors show a clear asymmetry between ITM and OTM which could distort strike convention comparisons in different cases. However, Table [2](#S5.T2 "Table 2 ‣ 5.2 Extensive Numerical Investigations ‣ 5 Numerical examples ‣ On the optimal choice of strike conventions in exchange option pricing") illustrates how our 1-STOSC approach compares to the other conventions across all our different error measures when averaging over all the scenarios for T=0.1𝑇0.1T=0.1 and T=0.25𝑇0.25T=0.25. The left half of the table includes all cases of a⋆superscript𝑎⋆a^{\star} (as in Table [1](#S5.T1 "Table 1 ‣ 5.2 Extensive Numerical Investigations ‣ 5 Numerical examples ‣ On the optimal choice of strike conventions in exchange option pricing")), while the right half simply excludes cases where a⋆<−1superscript𝑎⋆1a^{\star}<-1 or a⋆>2superscript𝑎⋆2a^{\star}>2, as mentioned above in Figure [2](#S5.F2 "Figure 2 ‣ 5.2 Extensive Numerical Investigations ‣ 5 Numerical examples ‣ On the optimal choice of strike conventions in exchange option pricing"). The fourth column also shows the middle-ground of a ‘bounded’ a⋆superscript𝑎⋆a^{\star} within this range instead of excluding these gridpoints.333Note that the a=0𝑎0a=0, a=1𝑎1a=1 and ATM columns also change slightly (often improve a little) when excluding these more extreme cases from the average error. Throughout the table the optimal strike convention performs very well again, and depending on the error measure used, bounding a⋆superscript𝑎⋆a^{\star} can cut the gap to ATM error in half, while exclusions may bring us almost all the way. However, what is especially crucial is the clear benefit a⋆superscript𝑎⋆a^{\star} already provides relative to a commonly-used choice such as ATM implied vols (a=0𝑎0a=0), often reducing error by a factor of about 3 or 4.

![Refer to caption](/html/1807.05396/assets/x10.png)


Figure 3: Comparison of average errors against moneyness for all T=0.1𝑇0.1T=0.1 cases, using four different error measures

Finally, before concluding we return to the question of consistency across moneyness, a key strength of the approach which is captured well by the impressive final row of the table called ‘MStd’ (maximum standard deviation), but is also visually striking in Figure [3](#S5.F3 "Figure 3 ‣ 5.2 Extensive Numerical Investigations ‣ 5 Numerical examples ‣ On the optimal choice of strike conventions in exchange option pricing"). Here we plot average errors across moneyness (against S0Ysuperscriptsubscript𝑆0𝑌S\_{0}^{Y} again) average over all the T=0.1𝑇0.1T=0.1 grids. Backing up the theory derived in earlier sections, the stability of errors across moneyness is very prominent, especially in comparison with a=0𝑎0a=0 or a=1𝑎1a=1, the commonly-used alternatives. Indeed, to our knowledge there is no other approach which adapts the strike convention to different scenarios in order to achieve such clear-cut error reduction.

## 6 Conclusion

We have presented a new and systematic methodology to construct an optimal strike convention for spread option pricing in the context of stochastic volatility models. Although its derivation is rather technical, this approach is simple to use and is based on the computation of the corresponding vanilla implied volatility levels and skews. Thus, market observables can be taken as inputs in a model-independent setting, strengthening the appeal of the technique. The obtained numerical results in Section 5 confirm its strong performance, especially compared to the limited alternatives commonly used in industry. There is more interesting work to be done in this direction, for example extending from exchange options to any spread options or to three-asset spreads. Data analysis and further numerical investigations would also be useful, including adapting to other stochastic volatility processes such as fractional models. We thus see this paper as the starting point to a broadly-applicable and valuable new pricing tool designed to complement nicely existing practice in the financial markets.

## References

* [1]
   C. Alexander and A. Venkatramanan (2011). Closed form approximations
  for spread options. *Applied Mathematical Finance, 18(5)*, 447-472.
* [2]
   Alòs, E., Ewald, C. (2008). Malliavin differentiability of the Heston volatility and applications to option pricing. *Advances in Applied Probability, 40(1)*, 144-162.
* [3]
   E. Alòs, J. A. León (2016). On the short-maturity behaviour of the implied volatility skew for random strike options and applications to option pricing approximation. *Quantitative Finance, 16(1)* 31-42.
* [4]
   E. Alòs, J. A. León, and J. Vives. (2007). On the short-time
  behavior of the implied volatility for jump-diffusion models with stochastic
  volatility. *Finance and Stochastics, 11.4*, 571-589.
* [5]
   Elisa Alòs and Thorsten Rheinländer (2015). On Margrabe
  options written on stochastic volatility models. *UPF Working paper 1475.*
* [6]
   Antonelli, F., A. Ramponi, and S. Scarlatti. (2010). Exchange option pricing under stochastic volatility: a correlation expansion. *Review of Derivatives Research, 13.1*, 45-73.
* [7]
   Bakshi, G., and Madan, D., Spanning and derivative-security valuation (2000). *Journal of Financial Economics, 55*, 205-238.
* [8]
   Borovkova, S., F. Permana, and H. van der Weide. (2007). A closed form approach to the valuation and hedging of basket and spread options *The Journal of Derivatives, 14(4)*, 8-24.
* [9]
   Carmona, R. and Durrleman, V. (2003). Pricing and hedging spread options, *Siam Review, 45(4),* 627-687.
* [10]
   Comte, Fabienne, and Eric Renault. Long memory in continuous‐time stochastic volatility models. (1998). *Mathematical Finance, 8.4*, 291-323.
* [11]
   V. Durrleman. (2008). Convergence of at-the-money implied volatilities to the spot volatility. *Journal of Applied Probability*, 542-550.
* [12]
   Dempster, M.A.H. and Hong, S.S.G. (2002). Spread option valuation and the fast fourier transform, In: Geman H., Madan D., Pliska S.R., Vorst T. (eds) *Mathematical Finance — Bachelier Congress 2000*. Springer Finance. Springer, Berlin, Heidelberg.
* [13]
   Fukasawa, Masaaki. (2011). Asymptotic analysis for stochastic volatility: martingale expansion. *Finance and Stochastics, 15.4*, 635-654.
* [14]
   Gatheral, Jim, Thibault Jaisson, and Mathieu Rosenbaum. (2014). Volatility is rough. *arXiv preprint* arXiv:1410.3394.
* [15]
   W. Margrabe. (1978). The value of an option to exchange one asset for another. *Journal of Finance, 33(1),* 177-186.
* [16]
   D. Nualart. (2006). *The Malliavin calculus and related topics*. Vol. 1995. Berlin: Springer.
* [17]
   G. Swindle. (2014). *Valuation and Risk Management in Energy Markets*. Cambridge University Press.

[◄](javascript: void(0))
[![ar5iv homepage](/assets/ar5iv.png)](/)
[Feeling  
lucky?](/feeling_lucky)

[Conversion  
report](/log/1807.05396)
[Report  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1807.05396)
[View original  
on arXiv](https://arxiv.org/abs/1807.05396)[►](javascript: void(0))