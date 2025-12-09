---
authors:
- Priyanshu Tiwari
- Sourav Majumdar
doc_id: arxiv:2512.07154v1
family_id: arxiv:2512.07154
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Asian option valuation under price impact
url_abs: http://arxiv.org/abs/2512.07154v1
url_html: https://arxiv.org/html/2512.07154v1
venue: arXiv q-fin
version: 1
year: 2025
---


Priyanshu Tiwari
tiwari.priyanshu.iitk@gmail.com
Department of Materials Science And Engineering, Indian Institute of Technology Kanpur, India & BNY, Pune

Sourav Majumdar
souravm@iitk.ac.in
Department of Management Sciences, Indian Institute of Technology Kanpur, India

###### Abstract

We study the valuation of Asian options in a binomial market with permanent price impact, extending the Cox–Ross–Rubinstein framework under a modified risk–neutral probability. We obtain an exact pathwise representation for geometric Asian options and derive two–sided bounds for arithmetic Asian options. Our analysis identifies the no–arbitrage region in terms of hedging volumes and shows that permanent price impact systematically raises Asian option prices. Numerical examples illustrate the effect of the impact parameter and hedging volumes on the resulting prices.

Keywords:
Asian options, price impact, binomial models, derivative pricing, path-dependent derivatives, hedging volumes

## 1 Introduction

Each time a trader places a buy (sell) order, the transaction pushes the asset price upward (downward). The magnitude of this movement, known as price impact, is of substantial interest because once trading is understood to influence prices, it constitutes an inherent cost to the trader. In this work, we examine how such price impact alters option valuation. Our focus is on Asian options, whose payoffs depend on the entire price trajectory. This path dependence makes them particularly sensitive to market impact. The effect of each trade propagates through time and influences the average price, thereby affecting its fair value. We seek to obtain tractable numerical procedures for computing Asian option price under price impact. We study the problem under a binomial option pricing formulation.

The binomial option pricing model is a discrete time approach to pricing options proposed by [Cox1979]. This approach is also referred to as the CRR model after the initials of the authors of the paper. It was shown that in the limiting case the CRR model converges to the closed form solution for the price of the European call option as arrived by Black-Scholes-Merton ([Black1973-ec, Merton1973-ji]). The CRR model serves as a numerical approach for pricing of contingent claims where analytical solution of the price is not always possible to achieve. Unlike the Black-Scholes-Merton formulation for the European call option, in the CRR model it is assumed trading takes place at discrete time periods. Asian option is an option contract whose payoff depends on the average value of the price of the underlying till the expiry. Unlike the vanilla call or put option whose payoff is dependent only on the terminal value of the asset price, the price of the Asian option depends on the entire price path. The Asian option is therefore a path-dependent option. Formally, the Asian call option has the following payoffs, where V0V\_{0} denotes the price of the option at period 0 and KK denotes the strike price,

1. 1.

   Geometric Asian option:
   V\_0=max((∏\_i=0^n S\_i )^1n+1-K,0)
2. 2.

   Arithmetic Asian option:
   V\_0=max((∑i=0nSin+1)-K,0)

The binomial option pricing model has been studied previously in the context of pricing Asian options ([chalasani1998accurate, chalasani1999refined, Kim2007-fm, Hsu2011, Dai2003-as]). In particular the exact analytical pricing of Arithmetic Asian options has been realised to be a difficult problem even under the simplifying Black-Scholes assumptions ([Milevsky1998-aj]). Several bounds for Arithmetic Asian options have been reported ([Albrecher2008-co, Fusai2008, Choe2021-tq, Chung2014-cz, Nielsen2003]). Other analytical and numerical approaches to pricing Arithmetic Asian options include, [kemna1990pricing, Linetsky2004-ia, Kirkby2016-al, Mudzimbabwe2012-ww, vecer2001new, Chung2014, Sun2013-pv, Choi2018-hn, Ding2023-nc].

Price impact, as defined by [bouchaud2009price], is the correlation between an incoming order and the subsequent price change. This implies that an increase in buy orders pushes prices upward, while an increase in sell orders pushes prices downward. The empirical presence of price impact is well documented ([hasbrouck2001common, madhavan1997security, webster2023handbook, Said2021-rp]), motivating the need to incorporate its effects into option pricing models. [Gueant2017-gq] formulates the pricing problem under market impact as a stochastic control problem. [Loeper2018-fs] also studies the problem of pricing under a linear market impact. To the best of our knowledge there is no article studying Asian option valuation under price impact.

The paper is structured as follows. In Section [2](https://arxiv.org/html/2512.07154v1#S2 "2 CRR model with price impact ‣ Asian option valuation under price impact") we describe the Cox-Ross-Rubinstein (CRR) model and its extension under price impact. We derive the risk-neutral probability under market impact and the no-arbitrage conditions. In Section [3](https://arxiv.org/html/2512.07154v1#S3 "3 Application to Geometric Asian Options ‣ Asian option valuation under price impact") we use this model to price geometric Asian options and obtain an exact representation for its price. In Section [4](https://arxiv.org/html/2512.07154v1#S4 "4 Bounds for the Arithmetic Asian Option Price ‣ Asian option valuation under price impact") we obtain two sided bounds for the arithmetic Asian options. In Section [5](https://arxiv.org/html/2512.07154v1#S5 "5 Numerical Illustration ‣ Asian option valuation under price impact") we check the numerical accuracy of the model against a benchmark approach without impac. We next use the model to illustrate the effect of price impact on the prices. In Section [6](https://arxiv.org/html/2512.07154v1#S6 "6 Conclusion ‣ Asian option valuation under price impact") we conclude the article and mention some potential extensions that can be considered.

## 2 CRR model with price impact

In the standard CRR (binomial) pricing model, time is divided into n∈ℕn\in\mathbb{N} discrete periods. For some m∈ℕm\in\mathbb{N} with m+1<nm+1<n, let the stock price at period mm be SmS\_{m}. The price evolves according to,

|  |  |  |
| --- | --- | --- |
|  | Sm+1={u​Sm,with probability ​q,d​Sm,with probability ​1−q.S\_{m+1}=\begin{cases}uS\_{m},&\text{with probability }q,\\[6.0pt] dS\_{m},&\text{with probability }1-q.\end{cases} |  |

where qq denotes the probability of an upward movement by factor uu, and 1−q1-q the probability of a downward movement by factor dd. Since the stock can take two possible values at each step, the model is referred to as the binomial option pricing model.

Incorporating price impact into this framework requires modifying the transition dynamics. We consider a linear and permanent impact specification following [bouchaud2009price], which itself is motivated by the seminal model of [kyle1985continuous]. In the Kyle model, trades from informed and noise traders are cleared by a market maker, and the execution of volume vv shares produces a predictable shift in the asset price. When hedging an option, the market maker must trade vv shares, generating an impact of the form,

|  |  |  |
| --- | --- | --- |
|  | Δ​S=λ​v\Delta S=\lambda v |  |

where λ>0\lambda>0 is the price-impact coefficient, vbv\_{b} and vsv\_{s} denote buy and sell volumes, respectively, and v=vb−vsv=v\_{b}-v\_{s} is the net traded volume.

The Kyle specification assumes that impact is linear in trade size and permanent in its effect on the price. Although empirical studies suggest that market impact is typically concave in volume and partially transient (see [bouchaud2009price]), the linear and permanent formulation offers analytical tractability and lends itself to incorporation within the CRR framework. For these reasons, we adopt this specification in what follows.

We can rewrite the Kyle impact model as follows,

|  |  |  |
| --- | --- | --- |
|  | Δ​pnpn−1=λ​vnpn−1\frac{\Delta p\_{n}}{p\_{n-1}}=\frac{\lambda v\_{n}}{p\_{n-1}} |  |

For small relative changes,

|  |  |  |
| --- | --- | --- |
|  | pnpn−1=1+λ​vnpn−1\frac{p\_{n}}{p\_{n-1}}=1+\frac{\lambda v\_{n}}{p\_{n-1}} |  |

For small impacts where λ​ϵn​vnpn−1≪1\frac{\lambda\epsilon\_{n}v\_{n}}{p\_{n-1}}\ll 1,

|  |  |  |
| --- | --- | --- |
|  | log⁡(1+λ​ϵn​vnpn−1)≈λ​ϵn​vnpn−1\log\left(1+\frac{\lambda\epsilon\_{n}v\_{n}}{p\_{n-1}}\right)\approx\frac{\lambda\epsilon\_{n}v\_{n}}{p\_{n-1}} |  |

Define a parameter λ~\tilde{\lambda} such that,

|  |  |  |
| --- | --- | --- |
|  | λ​vnpn−1=λ~​vn\frac{\lambda v\_{n}}{p\_{n-1}}=\tilde{\lambda}v\_{n} |  |

This gives us,

|  |  |  |
| --- | --- | --- |
|  | log⁡(pn)=log⁡(pn−1)+λ~​vn\log(p\_{n})=\log(p\_{n-1})+\tilde{\lambda}v\_{n} |  |

and we obtain,

|  |  |  |
| --- | --- | --- |
|  | pn=pn−1⋅eλ~​vnp\_{n}=p\_{n-1}\cdot e^{\tilde{\lambda}v\_{n}} |  |

We shall use λ\lambda instead of λ~\tilde{\lambda} from henceforth. Under price impact, the binomial model therefore becomes,

|  |  |  |
| --- | --- | --- |
|  | Sm+1={Su=u​Sm​eλ​vu,with probability ​q,Sd=d​Sm​e−λ​vd,with probability ​1−q.S\_{m+1}=\begin{cases}S\_{u}=uS\_{m}e^{\lambda v^{u}},&\text{with probability }q,\\[6.0pt] S\_{d}=dS\_{m}e^{-\lambda v^{d}},&\text{with probability }1-q.\end{cases} |  |

where vuv^{u} and vdv^{d} are the net trading volume in the up and down movements respectively. The adjusted up (u~\tilde{u}) and adjusted down (d~\tilde{d}) factors are,

|  |  |  |  |
| --- | --- | --- | --- |
|  | u~\displaystyle\tilde{u} | =u​eλ​vu\displaystyle=ue^{\lambda v^{u}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d~\displaystyle\tilde{d} | =d​e−λ​vd\displaystyle=de^{-\lambda v^{d}} |  |

The binomial transitions can therefore be rewritten as,

|  |  |  |
| --- | --- | --- |
|  | Sm+1={Su=u~​Sm,with probability ​q,Sd=d~​Sm,with probability ​1−q.S\_{m+1}=\begin{cases}S\_{u}=\tilde{u}S\_{m},&\text{with probability }q,\\[6.0pt] S\_{d}=\tilde{d}S\_{m},&\text{with probability }1-q.\end{cases} |  |

At any node of the binomial tree, the value of the option may be replicated by constructing a portfolio consisting of Δ\Delta shares of the underlying asset and a position BB in the risk-free bond. The central replication requirement is that this portfolio must match the option value in both possible successor states. Denoting the option values in the up and down states by VuV\_{u} and VdV\_{d}, respectively, and letting rr denote the gross risk-free return, the replication conditions are

|  |  |  |
| --- | --- | --- |
|  | Δ​Su+B​r=Vu,Δ​Sd+B​r=Vd.\Delta S\_{u}+Br=V\_{u},\qquad\Delta S\_{d}+Br=V\_{d}. |  |

In the presence of price impact, the underlying transitions are given by Su=u~​SmS\_{u}=\tilde{u}S\_{m} and Sd=d~​SmS\_{d}=\tilde{d}S\_{m}, where u~\tilde{u} and d~\tilde{d} denote the impact-adjusted multipliers.

Subtracting the two replication equations eliminates BB and yields an expression for the hedge ratio,

|  |  |  |
| --- | --- | --- |
|  | Δ=Vu−VdSu−Sd=Vu−VdSm​(u~−d~).\Delta=\frac{V\_{u}-V\_{d}}{S\_{u}-S\_{d}}=\frac{V\_{u}-V\_{d}}{S\_{m}(\tilde{u}-\tilde{d})}. |  |

This quantity represents the number of shares that must be held in order to replicate the instantaneous change in the option value at the node.

Once Δ\Delta is determined, the bond position BB follows immediately from either replication equation. Using the down-state relation, we obtain

|  |  |  |
| --- | --- | --- |
|  | B=Vd−Δ​Sdr=Vd−Δ​S​d~r.B=\frac{V\_{d}-\Delta S\_{d}}{r}=\frac{V\_{d}-\Delta S\tilde{d}}{r}. |  |

An analogous expression follows from the up-state value, and both necessarily agree. The current value of the option is then the cost of establishing this replicating portfolio,

|  |  |  |
| --- | --- | --- |
|  | V=Δ​Sm+B,V=\Delta S\_{m}+B, |  |

which constitutes the unique no-arbitrage price at the node.

The replication relations allow us to rewrite the option value in risk-neutral form. Substituting the expressions for Δ\Delta and BB into V=Δ​S+BV=\Delta S+B and simplifying yields,

|  |  |  |
| --- | --- | --- |
|  | V=1r​[r−d~u~−d~​Vu+u~−ru~−d~​Vd].V=\frac{1}{r}\left[\frac{r-\tilde{d}}{\tilde{u}-\tilde{d}}V\_{u}+\frac{\tilde{u}-r}{\tilde{u}-\tilde{d}}V\_{d}\right]. |  |

This motivates the definition of the adjusted risk-neutral probability

|  |  |  |
| --- | --- | --- |
|  | padj=r−d~u~−d~,1−padj=u~−ru~−d~,p^{\text{adj}}=\frac{r-\tilde{d}}{\tilde{u}-\tilde{d}},\qquad 1-p^{\text{adj}}=\frac{\tilde{u}-r}{\tilde{u}-\tilde{d}}, |  |

so that the option value takes the familiar binomial pricing form

|  |  |  |
| --- | --- | --- |
|  | V=1r​[padj​Vu+(1−padj)​Vd].V=\frac{1}{r}\left[p^{\text{adj}}V\_{u}+(1-p^{\text{adj}})V\_{d}\right]. |  |

###### Lemma 2.1.

|  |  |  |
| --- | --- | --- |
|  | 𝔼padj​[Sm+1Sm]=r,\mathbb{E}^{p^{\text{adj}}}\left[\frac{S\_{m+1}}{S\_{m}}\right]=r, |  |

The no-arbitrage condition requires that, under the effective risk-neutral probability, the expected gross return on the underlying equals the risk-free rate. Lemma [2.1](https://arxiv.org/html/2512.07154v1#S2.Thmtheorem1 "Lemma 2.1. ‣ 2 CRR model with price impact ‣ Asian option valuation under price impact") shows the consistency of the pricing measure.

The adjusted risk-neutral probability can be written explicitly as

|  |  |  |
| --- | --- | --- |
|  | padj=r−d​e−λ​vdu​eλ​vu−d​e−λ​vd.p^{\text{adj}}=\frac{r-de^{-\lambda v^{d}}}{ue^{\lambda v^{u}}-de^{-\lambda v^{d}}}. |  |

When the volumes vuv^{u} and vdv^{d} are constant across time and nodes, the effective risk-neutral probability remains constant throughout the tree. This property greatly simplifies numerical valuation and plays an important role in enabling tractable pricing in the presence of permanent linear price impact.

In the classical CRR model without price impact, the risk-neutral probability,

|  |  |  |
| --- | --- | --- |
|  | p=r−du−dp=\frac{r-d}{u-d} |  |

is determined by the requirement that the expected return of the stock under the risk-neutral measure equals the risk-free rate. Importantly, this probability does not represent the real-world likelihood of an upward movement, it is a probability chosen to enforce the no-arbitrage condition that discounted asset prices must evolve as martingales.

When price impact is introduced, the stock no longer moves according to the factors uu and dd but rather according to the adjusted multipliers
u~\tilde{u} and d~\tilde{d}. Since hedging trades now affect future prices, the replication strategy changes, and so does the probability that ensures the martingale property of the discounted stock price. The adjusted probability

|  |  |  |
| --- | --- | --- |
|  | padj=r−d~u~−d~p^{\text{adj}}=\frac{r-\tilde{d}}{\tilde{u}-\tilde{d}} |  |

therefore incorporates the additional cost and distortion induced by permanent price impact. In the limit λ→0\lambda\to 0 (no price impact), we recover the standard CRR expression, illustrating that the classical model is a special case of the impact-adjusted framework.

![Refer to caption](geometric_probability_comparison.png)


Figure 1: Risk–neutral probabilities in the classical CRR model (blue) and
in the impact–adjusted model (orange).

Figure [1](https://arxiv.org/html/2512.07154v1#S2.F1 "Figure 1 ‣ 2 CRR model with price impact ‣ Asian option valuation under price impact") illustrates how permanent linear price impact
modifies the risk–neutral measure. The blue curves show the classical CRR
probability pp, while the orange curves display the
impact–adjusted probability padjp^{\text{adj}}.

### 2.1 No-arbitrage region and admissible hedging volumes

The impact-adjusted CRR model remains arbitrage-free only if the adjusted
risk-neutral probability padjp^{\text{adj}} lies in [0,1][0,1]. From the
replicating portfolio construction above, we have,

|  |  |  |
| --- | --- | --- |
|  | padj=r−d~u~−d~,p^{\text{adj}}=\frac{r-\tilde{d}}{\tilde{u}-\tilde{d}}, |  |

For padjp^{\text{adj}} to define a valid risk-neutral probability,
we require,

|  |  |  |
| --- | --- | --- |
|  | 0≤padj≤1.0\leq p^{\text{adj}}\leq 1. |  |

Since we are in a binomial setting, we assume u~>d~\tilde{u}>\tilde{d}, so that
the denominator u~−d~\tilde{u}-\tilde{d} is strictly positive. The lower bound
padj≥0p^{\text{adj}}\geq 0 then reduces to

|  |  |  |
| --- | --- | --- |
|  | r−d~u~−d~≥0⟺r−d~≥0⟺r≥d~.\frac{r-\tilde{d}}{\tilde{u}-\tilde{d}}\geq 0\quad\Longleftrightarrow\quad r-\tilde{d}\geq 0\quad\Longleftrightarrow\quad r\geq\tilde{d}. |  |

Similarly, the upper bound padj≤1p^{\text{adj}}\leq 1 is equivalent to

|  |  |  |
| --- | --- | --- |
|  | r−d~u~−d~≤1⟺r−d~≤u~−d~⟺r≤u~.\frac{r-\tilde{d}}{\tilde{u}-\tilde{d}}\leq 1\quad\Longleftrightarrow\quad r-\tilde{d}\leq\tilde{u}-\tilde{d}\quad\Longleftrightarrow\quad r\leq\tilde{u}. |  |

Combining these two inequalities yields the familiar no-arbitrage restriction from the CRR model,
now expressed in terms of the impact-adjusted factors:

|  |  |  |
| --- | --- | --- |
|  | d~≤r≤u~.\tilde{d}\leq r\leq\tilde{u}. |  |

In words, the risk-free return must lie between the effective down and up
multipliers. If r≤d~r\leq\tilde{d}, the stock almost surely dominates the bond,
leading to an arbitrage by going long the stock and short the bond. If
r≥u~r\geq\tilde{u}, the bond dominates the stock, and an arbitrage arises by
shorting the stock and lending at the risk-free rate. The condition
d~<r<u~\tilde{d}<r<\tilde{u} is therefore the impact-adjusted analogue of the
standard CRR no-arbitrage condition d<r<ud<r<u.

Substituting the explicit expressions for u~\tilde{u} and d~\tilde{d},

|  |  |  |
| --- | --- | --- |
|  | d~=d​e−λ​vd,u~=u​eλ​vu,\tilde{d}=de^{-\lambda v^{d}},\qquad\tilde{u}=ue^{\lambda v^{u}}, |  |

we can rewrite the no-arbitrage inequalities as constraints on the hedging
volumes:

|  |  |  |
| --- | --- | --- |
|  | d​e−λ​vd≤r≤u​eλ​vu.de^{-\lambda v^{d}}\leq r\leq ue^{\lambda v^{u}}. |  |

These may be rearranged to give minimal admissible volumes,

|  |  |  |
| --- | --- | --- |
|  | vd≥−1λln(rd)=:vmind,vu≥1λln(ru)=:vminu.v^{d}\;\geq\;-\frac{1}{\lambda}\,\ln\!\left(\frac{r}{d}\right)\;=\mathrel{\mathop{\ordinarycolon}}\;v^{d}\_{\min},\qquad v^{u}\;\geq\;\frac{1}{\lambda}\,\ln\!\left(\frac{r}{u}\right)\;=\mathrel{\mathop{\ordinarycolon}}\;v^{u}\_{\min}. |  |

The “no-arbitrage region” in (vu,vd)(v^{u},v^{d})-space is thus described by the set of
pairs satisfying

|  |  |  |
| --- | --- | --- |
|  | vd≥vmind,vu≥vminu.v^{d}\geq v^{d}\_{\min},\qquad v^{u}\geq v^{u}\_{\min}. |  |

Under the standard CRR assumption d<r<ud<r<u, we have
ln⁡(r/d)>0\ln(r/d)>0 and ln⁡(r/u)<0\ln(r/u)<0, so that
vmind<0v^{d}\_{\min}<0 and vminu<0v^{u}\_{\min}<0. If, in addition, hedging volumes are
constrained to be non-negative, vu,vd≥0v^{u},v^{d}\geq 0, these inequalities are
automatically satisfied. In this case, every non-negative choice of hedging
volumes is compatible with an arbitrage-free, impact-adjusted binomial model,
and the condition 0≤padj≤10\leq p^{\text{adj}}\leq 1 holds without further
restriction.

## 3 Application to Geometric Asian Options

In this section we apply the impact-adjusted binomial framework to the valuation of geometric Asian call options. We consider an underlying asset following the impacted binomial dynamics described above, with impact-adjusted up and down factors u~\tilde{u} and d~\tilde{d} and adjusted risk-neutral probability padjp^{\text{adj}}.

A geometric Asian call option with maturity at time nn has payoff

|  |  |  |
| --- | --- | --- |
|  | Vn=max⁡(0,Gn−K),V\_{n}=\max\left(0,G\_{n}-K\right), |  |

where KK denotes the strike price and

|  |  |  |
| --- | --- | --- |
|  | Gn=(∏i=0nSi)1/(n+1)G\_{n}=\left(\prod\_{i=0}^{n}S\_{i}\right)^{1/(n+1)} |  |

is the geometric average of the underlying prices along the path up to maturity. In contrast to a standard European call option, whose payoff depends only on the terminal value SnS\_{n}, the geometric Asian payoff depends on the entire price path (S0,…,Sn)(S\_{0},\dots,S\_{n}) and is therefore path-dependent. In particular, two paths that lead to the same terminal value SnS\_{n} may nevertheless generate different geometric averages and hence different payoffs.

For a fixed horizon nn, a path can be represented by a word in {U,D}n\{U,D\}^{n}, such as U​D​UUDU, indicating the succession of up and down transitions. For any given path, we write G​(path)G(\text{path}) for the associated geometric average, V​(path)V(\text{path}) for the corresponding payoff

|  |  |  |
| --- | --- | --- |
|  | V​(path)=max⁡(0,G​(path)−K),V(\text{path})=\max\left(0,G(\text{path})-K\right), |  |

and P​(path)P(\text{path}) for its risk-neutral probability under the adjusted measure. Since the dynamics are binomial, the probability depends only on the number of up and down moves:

|  |  |  |
| --- | --- | --- |
|  | P​(path)=(padj)#​U​(path)​(1−padj)#​D​(path),P(\text{path})=\big(p^{\text{adj}}\big)^{\#U(\text{path})}\big(1-p^{\text{adj}}\big)^{\#D(\text{path})}, |  |

where #​U​(path)\#U(\text{path}) and #​D​(path)\#D(\text{path}) denote the number of up and down moves in the path, with #​U​(path)+#​D​(path)=n\#U(\text{path})+\#D(\text{path})=n.

### 3.1 The case n=1n=1

S0S\_{0}S0​u~S\_{0}\tilde{u}Path UGU=S0​u~G^{U}=S\_{0}\sqrt{\tilde{u}}US0​d~S\_{0}\tilde{d}Path DGD=S0​d~G^{D}=S\_{0}\sqrt{\tilde{d}}D

We begin with the simplest non-trivial case n=1n=1, where the option is defined over two dates t=0,1t=0,1. There are exactly two paths, UU and DD. Starting from S0S\_{0}, the terminal stock prices are

|  |  |  |
| --- | --- | --- |
|  | S1U=S0​u~,S1D=S0​d~,S\_{1}^{U}=S\_{0}\tilde{u},\qquad S\_{1}^{D}=S\_{0}\tilde{d}, |  |

with corresponding geometric averages

|  |  |  |
| --- | --- | --- |
|  | GU=(S0⋅S0​u~)1/2=S0​u~,GD=(S0⋅S0​d~)1/2=S0​d~.G^{U}=(S\_{0}\cdot S\_{0}\tilde{u})^{1/2}=S\_{0}\sqrt{\tilde{u}},\qquad G^{D}=(S\_{0}\cdot S\_{0}\tilde{d})^{1/2}=S\_{0}\sqrt{\tilde{d}}. |  |

The pathwise payoffs are therefore

|  |  |  |
| --- | --- | --- |
|  | VU=max⁡(0,S0​u~−K),VD=max⁡(0,S0​d~−K),V^{U}=\max\left(0,S\_{0}\sqrt{\tilde{u}}-K\right),\qquad V^{D}=\max\left(0,S\_{0}\sqrt{\tilde{d}}-K\right), |  |

and the associated risk-neutral probabilities are

|  |  |  |
| --- | --- | --- |
|  | P​(U)=padj,P​(D)=1−padj.P(U)=p^{\text{adj}},\qquad P(D)=1-p^{\text{adj}}. |  |

Discounting one period at the risk-free rate rr, the option value at time 0 is

|  |  |  |
| --- | --- | --- |
|  | V0=1r​[padj​VU+(1−padj)​VD]=1r​[padj​max⁡(0,S0​u~−K)+(1−padj)​max⁡(0,S0​d~−K)].V\_{0}=\frac{1}{r}\bigl[p^{\text{adj}}V^{U}+(1-p^{\text{adj}})V^{D}\bigr]=\frac{1}{r}\left[p^{\text{adj}}\max\left(0,S\_{0}\sqrt{\tilde{u}}-K\right)+(1-p^{\text{adj}})\max\left(0,S\_{0}\sqrt{\tilde{d}}-K\right)\right]. |  |

In this case the geometric feature of the payoff is fully captured by the two effective averages S0​u~S\_{0}\sqrt{\tilde{u}} and S0​d~S\_{0}\sqrt{\tilde{d}}, so the structure remains close to that of a standard one-period binomial model.

### 3.2 The case n=2n=2

S0S\_{0}S0​u~S\_{0}\tilde{u}S0​u~2S\_{0}\tilde{u}^{2}UUUS0​u~​d~S\_{0}\tilde{u}\tilde{d}UDDUS0​d~S\_{0}\tilde{d}S0​d~​u~S\_{0}\tilde{d}\tilde{u}DUUS0​d~2S\_{0}\tilde{d}^{2}DDDD

For n=2n=2 there are four possible paths: U​UUU, U​DUD, D​UDU and D​DDD. The corresponding terminal prices are

|  |  |  |
| --- | --- | --- |
|  | S2U​U=S0​u~2,S2U​D=S2D​U=S0​u~​d~,S2D​D=S0​d~2.S\_{2}^{UU}=S\_{0}\tilde{u}^{2},\quad S\_{2}^{UD}=S\_{2}^{DU}=S\_{0}\tilde{u}\tilde{d},\quad S\_{2}^{DD}=S\_{0}\tilde{d}^{2}. |  |

Although U​DUD and D​UDU share the same terminal value, they generate distinct sequences of intermediate prices and hence distinct geometric averages. Denoting the geometric average associated with a given path by GpathG^{\text{path}}, a straightforward calculation shows that

|  |  |  |
| --- | --- | --- |
|  | GU​U=S0​u~,GU​D=S0​(u~2​d~)1/3,GD​U=S0​(d~2​u~)1/3,GD​D=S0​d~.G^{UU}=S\_{0}\tilde{u},\qquad G^{UD}=S\_{0}(\tilde{u}^{2}\tilde{d})^{1/3},\qquad G^{DU}=S\_{0}(\tilde{d}^{2}\tilde{u})^{1/3},\qquad G^{DD}=S\_{0}\tilde{d}. |  |

The corresponding payoffs are

|  |  |  |
| --- | --- | --- |
|  | Vpath=max⁡(0,Gpath−K),for path∈{U​U,U​D,D​U,D​D},V^{\text{path}}=\max\left(0,G^{\text{path}}-K\right),\qquad\text{for }\text{path}\in\{UU,UD,DU,DD\}, |  |

and the path probabilities under padjp^{\text{adj}} are given by the usual binomial expressions,

|  |  |  |
| --- | --- | --- |
|  | P​(U​U)=(padj)2,P​(U​D)=P​(D​U)=padj​(1−padj),P​(D​D)=(1−padj)2.P(UU)=(p^{\text{adj}})^{2},\quad P(UD)=P(DU)=p^{\text{adj}}(1-p^{\text{adj}}),\quad P(DD)=(1-p^{\text{adj}})^{2}. |  |

Discounting over two periods, the time–0 value is therefore

|  |  |  |
| --- | --- | --- |
|  | V0=1r2​∑path∈{U​U,U​D,D​U,D​D}P​(path)​Vpath.V\_{0}=\frac{1}{r^{2}}\sum\_{\text{path}\in\{UU,UD,DU,DD\}}P(\text{path})\,V^{\text{path}}. |  |

This case already illustrates a key qualitative feature: the stock-price tree itself recombines, but the geometric average does not, so paths that meet at the same terminal stock price can yield different option values.

### 3.3 The case n=3n=3 and the general pattern

S0S\_{0}S0​u~S\_{0}\tilde{u}S0​u~2S\_{0}\tilde{u}^{2}S0​u~3S\_{0}\tilde{u}^{3}UUUUS0​u~2​d~S\_{0}\tilde{u}^{2}\tilde{d}UUDDUS0​u~​d~S\_{0}\tilde{u}\tilde{d}S0​u~2​d~S\_{0}\tilde{u}^{2}\tilde{d}UDUUS0​u~​d~2S\_{0}\tilde{u}\tilde{d}^{2}UDDDDUS0​d~S\_{0}\tilde{d}S0​d~​u~S\_{0}\tilde{d}\tilde{u}S0​d~​u~2S\_{0}\tilde{d}\tilde{u}^{2}DUUUS0​d~2​u~S\_{0}\tilde{d}^{2}\tilde{u}DUDDUS0​d~2S\_{0}\tilde{d}^{2}S0​d~2​u~S\_{0}\tilde{d}^{2}\tilde{u}DDUUS0​d~3S\_{0}\tilde{d}^{3}DDDDDD

For n=3n=3 the number of possible paths increases to 23=82^{3}=8. Each path induces a sequence of stock prices (S0,S1,S2,S3)(S\_{0},S\_{1},S\_{2},S\_{3}) and hence a geometric average

|  |  |  |
| --- | --- | --- |
|  | G​(path)=(∏i=03Si)1/4,G(\text{path})=\left(\prod\_{i=0}^{3}S\_{i}\right)^{1/4}, |  |

with payoff V​(path)=max⁡(0,G​(path)−K)V(\text{path})=\max\left(0,G(\text{path})-K\right) and probability P​(path)P(\text{path}) determined by the number of up and down moves. The time–0 value is obtained by discounting the pathwise expectation:

|  |  |  |
| --- | --- | --- |
|  | V0=1r3​∑all 8 pathsP​(path)​V​(path).V\_{0}=\frac{1}{r^{3}}\sum\_{\text{all 8 paths}}P(\text{path})\,V(\text{path}). |  |

Already at this horizon, explicit enumeration becomes unwieldy, and it is more instructive to describe the general combinatorial structure.

The pattern for general nn can be characterised as follows. At time ii, the stock price can be written as

|  |  |  |
| --- | --- | --- |
|  | Si=S0​u~ai​d~bi,S\_{i}=S\_{0}\tilde{u}^{a\_{i}}\tilde{d}^{b\_{i}}, |  |

where aia\_{i} and bib\_{i} denote the cumulative numbers of up and down moves up to time ii, satisfying ai+bi=ia\_{i}+b\_{i}=i. For a given path, define

|  |  |  |
| --- | --- | --- |
|  | A​(path)=∑i=0nai,B​(path)=∑i=0nbi.A(\text{path})=\sum\_{i=0}^{n}a\_{i},\qquad B(\text{path})=\sum\_{i=0}^{n}b\_{i}. |  |

Since ai+bi=ia\_{i}+b\_{i}=i for each ii, we have the identity

|  |  |  |
| --- | --- | --- |
|  | A​(path)+B​(path)=∑i=0ni=n​(n+1)2.A(\text{path})+B(\text{path})=\sum\_{i=0}^{n}i=\frac{n(n+1)}{2}. |  |

The geometric average along that path can then be expressed as

|  |  |  |
| --- | --- | --- |
|  | G​(path)=(∏i=0nSi)1/(n+1)=S0​(u~A​(path)​d~B​(path))1/(n+1)=S0​u~A​(path)/(n+1)​d~B​(path)/(n+1).G(\text{path})=\left(\prod\_{i=0}^{n}S\_{i}\right)^{1/(n+1)}=S\_{0}\left(\tilde{u}^{A(\text{path})}\tilde{d}^{B(\text{path})}\right)^{1/(n+1)}=S\_{0}\tilde{u}^{A(\text{path})/(n+1)}\tilde{d}^{B(\text{path})/(n+1)}. |  |

The time 0 price of the geometric Asian option can therefore be written in the general form as,

|  |  |  |
| --- | --- | --- |
|  | V0=1rn​∑all ​2n​ paths(padj)#​U​(path)​(1−padj)n−#​U​(path)​max⁡(0,S0​u~A​(path)/(n+1)​d~B​(path)/(n+1)−K).V\_{0}=\frac{1}{r^{n}}\sum\_{\text{all }2^{n}\text{ paths}}\big(p^{\text{adj}}\big)^{\#U(\text{path})}\big(1-p^{\text{adj}}\big)^{n-\#U(\text{path})}\max\left(0,S\_{0}\tilde{u}^{A(\text{path})/(n+1)}\tilde{d}^{B(\text{path})/(n+1)}-K\right). |  |

We summarise this representation in the following theorem,

###### Theorem 3.1 (Geometric Asian option under price impact).

Consider an underlying asset following the impact adjusted binomial stock price model with up and down factors u~\tilde{u} and d~\tilde{d} and the impact adjusted risk-neutral probability padjp^{\text{adj}}. Let n∈ℕn\in\mathbb{N} denote the expiry in discrete periods, and let K>0K>0 be the strike price of a geometric Asian call option written on this asset. Then the time 0 price of the option is given by,

|  |  |  |
| --- | --- | --- |
|  | V0=1rn​∑ω∈{U,D}n(padj)#​U​(ω)​(1−padj)#​D​(ω)​max⁡(0,G​(ω)−K),V\_{0}=\frac{1}{r^{n}}\sum\_{\omega\in\{U,D\}^{n}}(p^{\text{adj}})^{\#U(\omega)}(1-p^{\text{adj}})^{\#D(\omega)}\max\left(0,G(\omega)-K\right), |  |

where r>0r>0 denotes the gross risk-free rate, and G​(ω)G(\omega) is the geometric average of the underlying prices along the path ω\omega.

More precisely, each path ω=(ω1,…,ωn)∈{U,D}n\omega=(\omega\_{1},\dots,\omega\_{n})\in\{U,D\}^{n} induces a sequence of stock prices (S0,S1,…,Sn)(S\_{0},S\_{1},\dots,S\_{n}) with,

|  |  |  |
| --- | --- | --- |
|  | Si=S0​u~ai​(ω)​d~bi​(ω),i=0,…,n,S\_{i}=S\_{0}\tilde{u}^{a\_{i}(\omega)}\tilde{d}^{b\_{i}(\omega)},\qquad i=0,\dots,n, |  |

where ai​(ω)a\_{i}(\omega) and bi​(ω)b\_{i}(\omega) denote the cumulative numbers of up and down moves up to time ii, satisfying ai​(ω)+bi​(ω)=ia\_{i}(\omega)+b\_{i}(\omega)=i. Define,

|  |  |  |
| --- | --- | --- |
|  | A​(ω)=∑i=0nai​(ω),B​(ω)=∑i=0nbi​(ω),A(\omega)=\sum\_{i=0}^{n}a\_{i}(\omega),\qquad B(\omega)=\sum\_{i=0}^{n}b\_{i}(\omega), |  |

so that,

|  |  |  |
| --- | --- | --- |
|  | A​(ω)+B​(ω)=∑i=0ni=n​(n+1)2.A(\omega)+B(\omega)=\sum\_{i=0}^{n}i=\frac{n(n+1)}{2}. |  |

Then the geometric average along the path ω\omega can be written as,

|  |  |  |
| --- | --- | --- |
|  | G​(ω)=(∏i=0nSi)1/(n+1)=S0​(u~A​(ω)​d~B​(ω))1/(n+1).G(\omega)=\left(\prod\_{i=0}^{n}S\_{i}\right)^{1/(n+1)}=S\_{0}\bigl(\tilde{u}^{A(\omega)}\tilde{d}^{B(\omega)}\bigr)^{1/(n+1)}. |  |

Here #​U​(ω)\#U(\omega) and #​D​(ω)\#D(\omega) denote the total numbers of up and down moves in the path ω\omega, with #​U​(ω)+#​D​(ω)=n\#U(\omega)+\#D(\omega)=n.

## 4 Bounds for the Arithmetic Asian Option Price

The valuation of an arithmetic Asian option in the CRR framework is well known to be analytically challenging, even in the absence of price impact. The difficulty stems from the fact that the arithmetic average does not preserve the multiplicative structure of the binomial model, and therefore does not admit recombination in the same way as the geometric average. Under price impact, this complexity is exacerbated by the dependence of the effective up and down multipliers on hedging trades. In this section we develop tractable bounds for the arithmetic Asian call price by exploiting convexity properties of the average, namely the classical AM–GM inequality and a reverse AM–GM inequality due to [BudimirDragomirPecaric2001].

Let ω∈{U,D}n\omega\in\{U,D\}^{n} denote a path of up/down moves and let {Si​(ω)}i=0n\{S\_{i}(\omega)\}\_{i=0}^{n} be the corresponding sequence of stock prices under the impact-adjusted CRR dynamics. Define the arithmetic and geometric averages

|  |  |  |
| --- | --- | --- |
|  | An​(ω)=1n+1​∑i=0nSi​(ω),Gn​(ω)=(∏i=0nSi​(ω))1/(n+1),A\_{n}(\omega)=\frac{1}{n+1}\sum\_{i=0}^{n}S\_{i}(\omega),\qquad G\_{n}(\omega)=\left(\prod\_{i=0}^{n}S\_{i}(\omega)\right)^{1/(n+1)}, |  |

and the pathwise call payoffs

|  |  |  |
| --- | --- | --- |
|  | VA​(ω)=max⁡(0,An​(ω)−K),VG​(ω)=max⁡(0,Gn​(ω)−K).V\_{A}(\omega)=\max\left(0,A\_{n}(\omega)-K\right),\qquad V\_{G}(\omega)=\max\left(0,G\_{n}(\omega)-K\right). |  |

We denote by V0AV\_{0}^{A} and V0GV\_{0}^{G} the corresponding option prices at time 0 obtained by discounting risk-neutral expectations under the adjusted probability measure QQ.

### 4.1 A lower bound

The first inequality follows immediately from Jensen-type arguments. Because the arithmetic mean always dominates the geometric mean, the arithmetic Asian payoff is pathwise larger than the geometric one, and this relation is preserved under discounting.

###### Proposition 4.1 (Lower bound via AM–GM).

For every maturity nn,

|  |  |  |
| --- | --- | --- |
|  | V0A≥V0G.V\_{0}^{A}\geq V\_{0}^{G}. |  |

###### Proof.

Since An​(ω)≥Gn​(ω)A\_{n}(\omega)\geq G\_{n}(\omega) for all paths ω\omega, it follows that
VA​(ω)≥VG​(ω)V\_{A}(\omega)\geq V\_{G}(\omega). Taking risk-neutral expectations and
discounting yields the result.
∎

This lower bound is tight and requires no structural assumptions on the price-impact parameters. It also illustrates a general phenomenon: price impact affects both the arithmetic and geometric averages, but their ordering remains preserved.

### 4.2 Upper bounds

While the geometric average provides a natural lower bound, obtaining an upper bound requires more delicate control. A key observation is that the discrepancy between arithmetic and geometric averages can be dominated by the range of stock prices along the path. Let

|  |  |  |
| --- | --- | --- |
|  | Sm​(ω)=min0≤i≤n⁡Si​(ω),SM​(ω)=max0≤i≤n⁡Si​(ω)S\_{m}(\omega)=\min\_{0\leq i\leq n}S\_{i}(\omega),\qquad S\_{M}(\omega)=\max\_{0\leq i\leq n}S\_{i}(\omega) |  |

be the extremal prices along the path. A reverse AM-GM inequality due to
[BudimirDragomirPecaric2001], Proposition 1, yields a multiplicative bound relating the two averages.

###### Proposition 4.2 (Upper bound via reverse AM-GM inequality).

For any path ω∈{U,D}n\omega\in\{U,D\}^{n},

|  |  |  |
| --- | --- | --- |
|  | An​(ω)≤Gn​(ω)​ρ​(ω),A\_{n}(\omega)\leq G\_{n}(\omega)\,\rho(\omega), |  |

where

|  |  |  |
| --- | --- | --- |
|  | ρ​(ω)=exp⁡[14⋅(SM​(ω)−Sm​(ω))2Sm​(ω)​SM​(ω)].\rho(\omega)=\exp\!\left[\frac{1}{4}\cdot\frac{(S\_{M}(\omega)-S\_{m}(\omega))^{2}}{S\_{m}(\omega)\,S\_{M}(\omega)}\right]. |  |

Combining this bound with the structure of the payoff allows us to control the difference between the arithmetic and geometric Asian payoffs. The next result provides a pathwise comparison.

###### Proposition 4.3 (Pathwise control of payoff differences).

For every path ω∈{U,D}n\omega\in\{U,D\}^{n},

|  |  |  |
| --- | --- | --- |
|  | VA​(ω)−VG​(ω)≤Gn​(ω)​(ρ​(ω)−1).V\_{A}(\omega)-V\_{G}(\omega)\leq G\_{n}(\omega)\,(\rho(\omega)-1). |  |

###### Proof.

The inequality follows from Proposition [4.2](https://arxiv.org/html/2512.07154v1#S4.Thmprop2 "Proposition 4.2 (Upper bound via reverse AM-GM inequality). ‣ 4.2 Upper bounds ‣ 4 Bounds for the Arithmetic Asian Option Price ‣ Asian option valuation under price impact") together with a simple case distinction on whether An​(ω)A\_{n}(\omega) and Gn​(ω)G\_{n}(\omega) lie above or below the strike KK.
∎

Taking expectations yields a pathwise upper bound for the arithmetic Asian price, which is sharp but depends on the path-dependent quantity ρ​(ω)\rho(\omega).

###### Proposition 4.4 (Pathwise upper bound).

The arithmetic Asian call price satisfies

|  |  |  |
| --- | --- | --- |
|  | V0A−V0G≤1rn​∑ω∈{U,D}nP​(ω)​(ρ​(ω)−1)​Gn​(ω),V\_{0}^{A}-V\_{0}^{G}\leq\frac{1}{r^{n}}\sum\_{\omega\in\{U,D\}^{n}}P(\omega)\,\bigl(\rho(\omega)-1\bigr)\,G\_{n}(\omega), |  |

where P​(ω)P(\omega) denotes the impact-adjusted risk-neutral path probability.

This bound is always tighter than any global bound obtained by replacing ρ​(ω)\rho(\omega) with a uniform constant, but its computation requires summation over all 2n2^{n} paths.

To obtain a more tractable bound, we observe that the extremal prices along any path are themselves bounded by the largest and smallest values attainable in the tree. Under the impact-adjusted CRR dynamics,

|  |  |  |
| --- | --- | --- |
|  | Sm​(ω)≥S0​d~n,SM​(ω)≤S0​u~n,S\_{m}(\omega)\geq S\_{0}\tilde{d}^{\,n},\qquad S\_{M}(\omega)\leq S\_{0}\tilde{u}^{\,n}, |  |

so that ρ​(ω)\rho(\omega) is uniformly dominated by

|  |  |  |
| --- | --- | --- |
|  | ρ∗=exp⁡[14⋅(u~n−d~n)2u~n​d~n].\rho^{\*}=\exp\!\left[\frac{1}{4}\cdot\frac{(\tilde{u}^{\,n}-\tilde{d}^{\,n})^{2}}{\tilde{u}^{\,n}\tilde{d}^{\,n}}\right]. |  |

This leads to the following global upper bound.

###### Proposition 4.5 (Global upper bound).

The arithmetic Asian call price satisfies

|  |  |  |
| --- | --- | --- |
|  | V0A−V0G≤ρ∗−1rn​𝔼Q​[Gn],V\_{0}^{A}-V\_{0}^{G}\leq\frac{\rho^{\*}-1}{r^{n}}\,\mathbb{E}^{Q}[G\_{n}], |  |

where GnG\_{n} is the geometric average along a random path under the adjusted risk-neutral measure.

The global bound is weaker but computationally simple, depending only on the impact-adjusted factors u~\tilde{u} and d~\tilde{d}. As λ\lambda increases, the spread between u~n\tilde{u}^{n} and d~n\tilde{d}^{n} widens, making ρ∗\rho^{\*} larger and the bound looser. Likewise, as nn grows, extremal path dispersion increases, causing ρ∗\rho^{\*} to diverge. These effects reflect a fundamental property of arithmetic averaging: the longer the horizon or the larger the impact-induced price variation, the more the arithmetic average can exceed the geometric one.

###### Theorem 4.1 (Two-sided bounds).

For the arithmetic Asian call option under the impact-adjusted CRR model,

|  |  |  |
| --- | --- | --- |
|  | V0G≤V0A≤V0G+ρ∗−1rn​𝔼Q​[Gn].V\_{0}^{G}\;\leq\;V\_{0}^{A}\;\leq\;V\_{0}^{G}+\frac{\rho^{\*}-1}{r^{n}}\,\mathbb{E}^{Q}[G\_{n}]. |  |

Finally, we note that the pathwise bound in Proposition [4.4](https://arxiv.org/html/2512.07154v1#S4.Thmprop4 "Proposition 4.4 (Pathwise upper bound). ‣ 4.2 Upper bounds ‣ 4 Bounds for the Arithmetic Asian Option Price ‣ Asian option valuation under price impact") always improves on the global bound.

###### Proposition 4.6 (Tightness).

Let

|  |  |  |
| --- | --- | --- |
|  | A:=1rn∑ωP(ω)(ρ(ω)−1)Gn(ω),B:=ρ∗−1rn𝔼Q[Gn].A\mathrel{\mathop{\ordinarycolon}}=\frac{1}{r^{n}}\sum\_{\omega}P(\omega)\,(\rho(\omega)-1)G\_{n}(\omega),\qquad B\mathrel{\mathop{\ordinarycolon}}=\frac{\rho^{\*}-1}{r^{n}}\,\mathbb{E}^{Q}[G\_{n}]. |  |

Then A≤BA\leq B.

###### Proof.

Since ρ​(ω)≤ρ∗\rho(\omega)\leq\rho^{\*} for every path and Gn​(ω)≥0G\_{n}(\omega)\geq 0, summing against P​(ω)P(\omega) gives the desired inequality.
∎

Taken together, these results show that the geometric Asian price provides a natural and tight lower bound for the arithmetic Asian price, while a family of tractable upper bounds can be obtained by combining reverse Jensen-type inequalities with extremal path bounds. Pathwise bounds are sharper but computationally expensive, whereas global bounds are coarser but fully explicit in the price-impact parameters.

## 5 Numerical Illustration

In this section we present numerical illustrations highlighting the
approximation quality of the impact–adjusted CRR scheme when applied to Asian options.

### 5.1 Baseline case with no price impact

Although the model admits no closed-form price in the
presence of price impact, the frictionless case provides a natural benchmark via
the Kemna–Vorst formula ([kemna1990pricing]), which yields an exact price in continuous time for
geometric averages under lognormal dynamics. To assess accuracy, we compute the
CRR price for increasing numbers of time steps nn, keeping the effective
up and down factors fixed, and report its deviation from the Kemna–Vorst
benchmark.

Table [1](https://arxiv.org/html/2512.07154v1#S5.T1 "Table 1 ‣ 5.1 Baseline case with no price impact ‣ 5 Numerical Illustration ‣ Asian option valuation under price impact") summarizes the results. The CRR
approximation converges towards the benchmark as the number of time
subdivisions increases. The absolute error decreases steadily, and the relative
percentage error stabilizes around 6%6\%–7%7\% for moderate values of
nn.

| n | CRR Price | Kemna-Vorst Price | Absolute Difference | % Error |
| --- | --- | --- | --- | --- |
| 2 | 7.14 | 7.58 | 0.43 | 5.73 |
| 4 | 9.15 | 9.92 | 0.76 | 7.68 |
| 6 | 10.74 | 11.61 | 0.87 | 7.49 |
| 8 | 12.03 | 12.98 | 0.95 | 7.29 |
| 10 | 13.13 | 14.13 | 0.99 | 7.03 |
| 12 | 14.08 | 15.12 | 1.04 | 6.89 |
| 14 | 14.92 | 15.99 | 1.07 | 6.71 |
| 16 | 15.67 | 16.77 | 1.11 | 6.60 |
| 18 | 16.34 | 17.48 | 1.14 | 6.50 |
| 20 | 16.96 | 18.11 | 1.16 | 6.40 |

Table 1: Numerical comparison between the CRR model with no impact and the Kemna-Vorst pricing formula for geometric Asian call options, with CRR parameters as S0=100S\_{0}=100, K=100K=100, r=1.05r=1.05, u=1.2u=1.2, d=0.8d=0.8.

Table [2](https://arxiv.org/html/2512.07154v1#S5.T2 "Table 2 ‣ 5.1 Baseline case with no price impact ‣ 5 Numerical Illustration ‣ Asian option valuation under price impact") summarizes the results for arithmetic Asian call options. For arithmetic Asian options we report the upper bounds given in [4.1](https://arxiv.org/html/2512.07154v1#S4.Thmtheorem1 "Theorem 4.1 (Two-sided bounds). ‣ 4.2 Upper bounds ‣ 4 Bounds for the Arithmetic Asian Option Price ‣ Asian option valuation under price impact"). We use the pathwise upper bound from Proposition [4.4](https://arxiv.org/html/2512.07154v1#S4.Thmprop4 "Proposition 4.4 (Pathwise upper bound). ‣ 4.2 Upper bounds ‣ 4 Bounds for the Arithmetic Asian Option Price ‣ Asian option valuation under price impact"). We find that for smaller values of nn, the upper bound is closer to the benchmark price, which suggests bounds may be tighter for small values of nn.

| n | Lower Bound Price | Upper Bound Price | Kemna-Vorst Price |
| --- | --- | --- | --- |
| 2 | 7.14 | 9.71 | 8.14 |
| 4 | 9.15 | 16.09 | 10.87 |
| 6 | 10.74 | 22.93 | 12.95 |
| 8 | 12.03 | 30.43 | 14.67 |
| 10 | 13.13 | 38.90 | 16.20 |
| 12 | 14.08 | 48.85 | 17.57 |
| 14 | 14.92 | 61.26 | 18.79 |
| 16 | 15.67 | 78.95 | 19.91 |
| 18 | 16.34 | 138.15 | 21.01 |
| 20 | 16.96 | 12961.48 | 21.99 |

Table 2: Numerical comparison between the CRR model with no impact and the Kemna-Vorst pricing formula for arithmetic Asian call options, with CRR parameters as S0=100S\_{0}=100, K=100K=100, r=1.05r=1.05, u=1.2u=1.2, d=0.8d=0.8.

### 5.2 Sensitivity to price impact

We will now illustrate the sensitivity of our model to price impact.

Table [3](https://arxiv.org/html/2512.07154v1#S5.T3 "Table 3 ‣ 5.2 Sensitivity to price impact ‣ 5 Numerical Illustration ‣ Asian option valuation under price impact") reports geometric Asian prices together with
the lower and upper bounds for the arithmetic Asian call derived. First, the
geometric price grows steadily with λ\lambda in both regimes, reflecting the
convexity of the payoff in response to increasingly dispersed price paths.
Second, the lower bound remains tight (as expected), while the upper bound
expands extremely rapidly with λ\lambda. This behaviour is consistent with the
structure of the reverse AM-GM inequality, where the multiplicative factor
ρ​(ω)\rho(\omega) depends exponentially on the spread between the pathwise extrema
SmS\_{m} and SMS\_{M}. Because price impact widens this spread, the bounds deteriorate
sharply for moderate to large λ\lambda. Finally, the up and down biased cases
track each other closely for small impact levels, but diverge as impact grows.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Up-biased | | | Down-biased | | |
| λ\lambda | Geom. | LB(A) | UB(A) | Geom. | LB(A) | UB(A) |
| 0.00 | 10.74 | 10.74 | 22.93 | 10.74 | 10.74 | 22.93 |
| 0.05 | 12.92 | 12.92 | 35.01 | 12.94 | 12.94 | 34.98 |
| 0.10 | 14.94 | 14.94 | 52.66 | 14.91 | 14.91 | 52.71 |
| 0.15 | 16.67 | 16.67 | 82.17 | 16.65 | 16.65 | 82.62 |
| 0.20 | 18.11 | 18.11 | 145.61 | 18.14 | 18.14 | 151.49 |
| 0.25 | 19.30 | 19.30 | 358.53 | 19.40 | 19.40 | 484.07 |
| 0.30 | 20.24 | 20.24 | 2049.94 | 20.44 | 20.44 | 6693.71 |
| 0.35 | 21.01 | 21.01 | 54863.30 | 21.25 | 21.25 | 657809.09 |

Table 3: Sensitivity of geometric Asian prices (Geom.) and arithmetic Asian bounds (LB(A) denotes the lower bound and UB(A) denotes the upper bound) to the
price impact magnitude λ\lambda, with parameters S0=100,K=100,r=1.05,n=6S\_{0}=100,K=100,r=1.05,n=6. We consider two different hedging volume regimes which are up-biased (vu=1.3,vd=1v\_{u}=1.3,v\_{d}=1) and down-biased (vu=1,vd=1.3v\_{u}=1,v\_{d}=1.3).

Figure [2](https://arxiv.org/html/2512.07154v1#S5.F2 "Figure 2 ‣ 5.2 Sensitivity to price impact ‣ 5 Numerical Illustration ‣ Asian option valuation under price impact") illustrates two experiments. In the first (solid red curve), we vary vdv^{d} while keeping vuv^{u} fixed. In the second (dashed blue curve), we vary vuv^{u} while keeping vdv^{d} fixed. The behaviour in both cases is similar for small and moderate
volumes. Increasing vdv^{d} continues to raise the option value, whereas increasing
vuv^{u} eventually produces a mild decline.

This asymmetry arises because upward and downward effective moves enter the
geometric mean multiplicatively but with opposite signs in the price‐impact
adjustment. Larger vuv^{u} boosts u~\tilde{u}, steepening the upside branch of
the tree, whereas larger vdv^{d} strengthens the contraction in down moves.

![Refer to caption](price_impact_asymmetric_combined.png)


Figure 2: 
Sensitivity of the geometric Asian call price to hedging volumes.
The solid red curve varies vdv^{d} while holding vu=2.5v^{u}=2.5 fixed,
and the dashed blue curve varies vuv^{u} while holding vd=2.5v^{d}=2.5 fixed. Parameter values are S0=100S\_{0}=100, K=100K=100,
u=1.2u=1.2, d=0.8d=0.8, r=1.05r=1.05, λ=0.1\lambda=0.1, n=15n=15.

We now examine how the geometric Asian option price varies with moneyness
(K/S0K/S\_{0}) under different hedging regimes and different levels of permanent
price impact. Figure [3](https://arxiv.org/html/2512.07154v1#S5.F3 "Figure 3 ‣ 5.2 Sensitivity to price impact ‣ 5 Numerical Illustration ‣ Asian option valuation under price impact") reports option values for
three representative configurations- down-biased hedging (vd>vuv^{d}>v^{u}),
symmetric hedging (vd=vuv^{d}=v^{u}), and up-biased hedging (vu>vdv^{u}>v^{d}).

Across all regimes, option values decrease as the strike increases, reflecting the monotonicity in moneyness. However, the presence of price impact
induces a systematic upward shift in the level of option prices.

The magnitude of this effect depends critically on the hedging asymmetry.
Under down-biased hedging, where the market maker trades more aggressively in
down states, the effective down factor d~\tilde{d} becomes smaller, producing
greater curvature in the lower branch of the tree. This magnifies path
variability and results in the largest sensitivity to λ\lambda, especially
for near-the-money strikes. Symmetric hedging exhibits an intermediate
response, while up-biased hedging generates a smaller sensitivity, as the
impact predominantly steepens the upper branch of the tree. Interestingly,
for high strikes, the three regimes converge, illustrating that extreme
out-of-the-money options are less sensitive to the interaction between
hedging asymmetry and market impact.

![Refer to caption](price_impact_moneyness_weak.png)


Figure 3: 
Geometric Asian option prices across moneyness levels (K/S0K/S\_{0}) under
three hedging regimes- down-biased (vd>vuv^{d}>v^{u}), symmetric
(vd=vuv^{d}=v^{u}), and up-biased (vu>vdv^{u}>v^{d}). Each curve corresponds to
a different price-impact coefficient λ\lambda. The parameters are, up-biased (vu=1.3,vd=1v\_{u}=1.3,v\_{d}=1), down-biased (vu=1,vd=1.3v\_{u}=1,v\_{d}=1.3) and symmetric (vu=vd=1v\_{u}=v\_{d}=1), with S0=100S\_{0}=100, K=100K=100,
u=1.2u=1.2, d=0.8d=0.8, r=1.05r=1.05, n=15n=15.

## 6 Conclusion

This paper develops a tractable framework for valuing Asian options in a binomial market with permanent price impact. By embedding Kyle linear market impact into the Cox–Ross–Rubinstein model, we obtain impact-adjusted up and down factors and a corresponding modified risk–neutral probability. Within this framework, we derived an exact pathwise representation for geometric Asian call options.

For arithmetic Asian options, whose exact valuation is intractable even without impact, we obtain two-sided bounds. The geometric Asian price yields a tight and model-free lower bound, while an explicit upper bound follows from a reverse AM–GM inequality combined with extremal path analysis. Our analysis also characterises the no-arbitrage region of the impact-adjusted CRR model in terms of admissible hedging volumes.

The numerical illustrations demonstrates several qualitative features of the model. First, geometric Asian prices increase monotonically with the impact parameter, consistent with the convexity of the payoff. Second, the arithmetic bounds behave well for small and moderate maturities but become increasingly loose as either the impact parameter or the horizon grows. Finally, the comparative analysis with respect to hedging volumes shows an asymmetry between up and down biased regimes.

Overall, our results provide a computationally tractable approach to pricing path-dependent options under permanent price impact. Several extensions could be considered including transient or nonlinear impact specifications, multi-asset settings, and optimisation of hedging volumes in the presence of execution costs. The binomial structure developed here could be considered for these extensions.