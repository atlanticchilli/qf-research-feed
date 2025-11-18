---
authors:
- Lóránt Nagy
- Miklós Rásonyi
doc_id: arxiv:2511.12093v1
family_id: arxiv:2511.12093
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: On the utility problem in a market where price impact is transient
url_abs: http://arxiv.org/abs/2511.12093v1
url_html: https://arxiv.org/html/2511.12093v1
venue: arXiv q-fin
version: 1
year: 2025
---


Lóránt Nagy
HUN-REN Alfréd Rényi Institute of Mathematics, Budapest, Hungary
  
Miklós
Rásonyi
HUN-REN Alfréd Rényi Institute of Mathematics and Eötvös Loránd University, Budapest,
Hungary; E-mail: rasonyi@renyi.hu

(November 15, 2025)

###### Abstract

We consider a discrete-time model of a financial market where a risky asset is bought and sold with transactions having
a transient price impact. It is shown that the corresponding utility maximization problem admits a solution. We manage to remove
some unnatural restrictions on the market depth and resilience processes that were present in earlier work. A non-standard
feature of the problem is that the set of attainable portfolio values may fail the convexity property.

Keywords: price impact; market friction; optimal investment; dynamic programming;
nonconvex domain of optimization

MSC 2020: Primary: 93E20, 91B70, 91B16; secondary: 91G10, 28B20

## 1 Introduction

Investors’ actions move market prices and make large position changes costly. More or less realistic models for
this *price impact* phenomenon have been worked out in the mathematical finance literature.
One of the principal questions is the study of optimal investment in the presence of these (nonlinear)
transaction costs.

Price impact may be assumed *instantaneous* if it affects the investor only at the moment of his/her portfolio rebalancing.
This assumption leads to a relatively simple market dynamics,
see [[5](https://arxiv.org/html/2511.12093v1#bib.bib5), [2](https://arxiv.org/html/2511.12093v1#bib.bib2)]. At the other extreme, price impact may be *permanent*, in which case
the investor’s action pushes the price in a direction and this effect pertains to the whole future.
The most accurate description of reality is probably in between: price impact should
be *transient*, with a gradually fading effect for the future, see [[1](https://arxiv.org/html/2511.12093v1#bib.bib1), [3](https://arxiv.org/html/2511.12093v1#bib.bib3)].
The speed at which these effects disappear is characterized by *market resilience*: if rr is
resilience then the bid-ask spread is diminished by a factor of e−re^{-r} in one unit of time. The
size of the disturbance
caused by trading a unit amount of the asset is described by *market depth*: if
δ\delta is market depth then 1/δ1/\delta is the effect on the bid-ask spread of trading one unit of the risky asset.

In the present article we prove that the uility maximization problem in discrete time for an agent
trading with transient price impact is well-posed: it admits a solution.
The problem under consideration has a complex, non-linear dynamics involving
all previous strategies at a given time. Moreover, the domain of optimization
is *non-convex*, which is a highly unusual feature.

A continuous-time model with *instantaneous* price impact was considered in [[5](https://arxiv.org/html/2511.12093v1#bib.bib5)]:
they proved in their Theorem 5.1 that the utility maximization problem (with a concave utility function) admits
a solution under mild conditions.

In [[3](https://arxiv.org/html/2511.12093v1#bib.bib3)] a more advanced model with *transient*
price impact was treated where the markets’ resiliance and depth were both assumed constant.
Theorem 3.3 of [[3](https://arxiv.org/html/2511.12093v1#bib.bib3)] proved the existence of an optimal investment strategy in such a setting.

In [[1](https://arxiv.org/html/2511.12093v1#bib.bib1)] market resilience and depth were both allowed to be stochastic processes
but a related monotonicity condition was imposed in their Assumption 2.4 which implies
that the set of attainable portfolio values is convex. That condition holds for
constant resilience and depth but otherwise it is rather restrictive. The paper [[1](https://arxiv.org/html/2511.12093v1#bib.bib1)] did not
provide a general existence theorem for optimizers but a superreplication result (Theorem 3.2 in [[1](https://arxiv.org/html/2511.12093v1#bib.bib1)])
with a dual characterization of contingent claims that can be superhedged from a given initial
position. They also proved a verification result (Corollary 3.5 in [[1](https://arxiv.org/html/2511.12093v1#bib.bib1)]): a sufficient condition
implying that a given strategy is optimal.

In the present work we are dealing with the discrete-time version of the model of
[[1](https://arxiv.org/html/2511.12093v1#bib.bib1)]. Our purpose is to prove the existence of an optimal strategy for
a utility maximizer while removing the stringent monotonicity assumption of [[1](https://arxiv.org/html/2511.12093v1#bib.bib1)]
on market resilience and market depth, see Theorem [2.4](https://arxiv.org/html/2511.12093v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2 Setup and results ‣ On the utility problem in a market where price impact is transient") and Remark [2.6](https://arxiv.org/html/2511.12093v1#S2.Thmtheorem6 "Remark 2.6. ‣ 2 Setup and results ‣ On the utility problem in a market where price impact is transient") below.

Section [2](https://arxiv.org/html/2511.12093v1#S2 "2 Setup and results ‣ On the utility problem in a market where price impact is transient") presents the technical details of our model, the main result (Theorem [2.4](https://arxiv.org/html/2511.12093v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2 Setup and results ‣ On the utility problem in a market where price impact is transient")) and some discussions
about the lack of convexity and its implications. Proofs will
then be provided starting with Section [3](https://arxiv.org/html/2511.12093v1#S3 "3 Preparation for the proof ‣ On the utility problem in a market where price impact is transient"). Section [4](https://arxiv.org/html/2511.12093v1#S4 "4 Single step case ‣ On the utility problem in a market where price impact is transient") deals with the one-step case while Section [5](https://arxiv.org/html/2511.12093v1#S5 "5 The generic step, dynamic programming ‣ On the utility problem in a market where price impact is transient")
provides the dynamic programming argument.
Further reflections are given in Section [6](https://arxiv.org/html/2511.12093v1#S6 "6 Conclusion ‣ On the utility problem in a market where price impact is transient").

## 2 Setup and results

For x∈ℝx\in\mathbb{R} we denote by x+,x−x^{+},x^{-} the positive and negative parts of xx.
Fix a probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) once and for all, together with a discrete-time
filtration ℱt\mathcal{F}\_{t}, t=0,…,Tt=0,\ldots,T where ℱ0\mathcal{F}\_{0} coincides with ℙ\mathbb{P}-null sets.
Mathematical expectation with respect to ℙ\mathbb{P} will be denoted by 𝔼​[⋅]\mathbb{E}[\,\cdot\,],
𝔼t​[⋅]\mathbb{E}\_{t}[\,\cdot\,] stands for ℱt\mathcal{F}\_{t}-conditional expectation. L0L^{0} is the set of all
real-valued random variables. 𝟏A\mathbf{1}\_{A} denotes the indicator function of a set AA.

We now present the discrete-time version of the model in [[1](https://arxiv.org/html/2511.12093v1#bib.bib1)].
The time horizon of the investor will be some T∈ℕT\in\mathbb{N}. In the TTth step the investor
must liquidate her position in the risky asset hence genuine decisions are made only at
the previous times t=1,…,T−1t=1,\ldots,T-1. To have a nontrivial problem we thus need to assume T≥2T\geq 2.

The risky asset’s midprice (that is, the middle point of the bid-ask spread)
is described by an adapted real-valued process PtP\_{t}, t=0,…,Tt=0,\ldots,T.
This is the price followed when there is no trading from the part of the investor in consideration.

Position in the risky asset at time tt is denoted by XtX\_{t}, t=0,…,Tt=0,\ldots,T, we assume X0:=0X\_{0}:=0.
At each time tt the investor makes a portfolio adjustment based on previous information (before the new price PtP\_{t}
is revealed) hence XtX\_{t} is assumed ℱt−1\mathcal{F}\_{t-1} measurable, that is, the strategy process
XtX\_{t}, 1≤t≤T1\leq t\leq T is predictable. We follow the convention X−1:=0X\_{-1}:=0.
The set of all strategies is denoted by 𝒜\mathcal{A}. We define

|  |  |  |
| --- | --- | --- |
|  | 𝒜0:={X∈𝒜:XT=0},\mathcal{A}\_{0}:=\{X\in\mathcal{A}:X\_{T}=0\}, |  |

the set of strategies that liquidate the position in the risky asset by the end of the time horizon.
We note here, that due to the dynamics utilized in the paper, presented below, maximization of the utility of the terminal wealth ξTX\xi\_{T}^{X} in XX is economically meaningful only
over the set of strategies 𝒜0\mathcal{A}\_{0}. Outside of 𝒜0\mathcal{A}\_{0}, an investor could attain a position in the bank account with favourable expected utility while having large negative positions, and we would need to deal with liquidation value: such scenarios will be excluded.

We model liquidity with two primitives, resilience rate, and market depth: market resilience is described by a non-negative adapted process denoted by rt≥0r\_{t}\geq 0, t=0,…,T−1t=0,\ldots,T-1, and market depth is a positive adapted process δt>0\delta\_{t}>0, t=1,…,Tt=1,\ldots,T. The *half-spread* follows a linear dynamics, namely

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζt+1X=e−rt​ζtX+1δt+1​|Xt+1−Xt|, 0≤t≤T−1,\zeta^{X}\_{t+1}=e^{-r\_{t}}\zeta^{X}\_{t}+\frac{1}{\delta\_{t+1}}|X\_{t+1}-X\_{t}|,\ 0\leq t\leq T-1, |  | (1) |

starting from an initial value ζ0X:=ζ0≥0\zeta\_{0}^{X}:=\zeta\_{0}\geq 0.
Finally, the cash account at time t=1,…,Tt=1,\ldots,T, considering that the investor pays the spread when trading, is calculated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξt+1X−ξtX=−Pt+1​(Xt+1−Xt)−ζt+1X​|Xt+1−Xt|, 0≤t≤T−1.\xi^{X}\_{t+1}-\xi\_{t}^{X}=-P\_{t+1}(X\_{t+1}-X\_{t})-\zeta^{X}\_{t+1}|X\_{t+1}-X\_{t}|,\ 0\leq t\leq T-1. |  | (2) |

Setting ξ0X:=0\xi^{X}\_{0}:=0 for simplicity, with initial capital z∈ℝz\in\mathbb{R}, the investor has a wealth of z+ξTXz+\xi\_{T}^{X} at time TT. The above model is the discrete-time counterpart of the model introduced in [[1](https://arxiv.org/html/2511.12093v1#bib.bib1)]: except that in our setup only transient impact is modeled.

We further assume that the investor may possibly receive a random endowment during the trading period,
described by an ℱT\mathcal{F}\_{T}-measurable ℝ\mathbb{R}-valued
random variable BB. Negative BB means that the investor has certain
payment obligations during the period considered.

The investor aims to maximize her expected utility from terminal wealth, hence we fix a *utility function* u:ℝ→ℝu:\mathbb{R}\to\mathbb{R}.

###### Assumption 2.1.

The function uu is non-decreasing, continuous, limx→−∞u​(x)=−∞\lim\_{x\to-\infty}u(x)=-\infty, and uu is bounded from above.
We furthermore assume that for all x,y,z∈ℝx,y,z\in\mathbb{R} and for all t=1,…,T−1t=1,\ldots,T-1,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[u​(x+y​Pt+z​PT−B)]>−∞\mathbb{E}[u(x+yP\_{t}+zP\_{T}-B)]>-\infty |  | (3) |

holds.

###### Remark 2.2.

If uu is concave then ([3](https://arxiv.org/html/2511.12093v1#S2.E3 "In Assumption 2.1. ‣ 2 Setup and results ‣ On the utility problem in a market where price impact is transient")) is implied by the simpler condition

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[u​(x+y​Pt−B)]>−∞,t=1,…,T.\mathbb{E}[u(x+yP\_{t}-B)]>-\infty,\ t=1,\ldots,T. |  |

Indeed, by concavity of the mapping v→u​(x+v−B)v\to u(x+v-B),

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[u​(x+y​Pt+z​PT−B)]≥𝔼​[u​(x+2​y​Pt−B)]+𝔼​[u​(x+2​z​PT−B)]2.\mathbb{E}\left[u(x+yP\_{t}+zP\_{T}-B)\right]\geq\frac{\mathbb{E}\left[u(x+2yP\_{t}-B)\right]+\mathbb{E}\left[u(x+2zP\_{T}-B)\right]}{2}. |  |

Our next hypothesis stipulates that market depth is always above a fixed threshold.

###### Assumption 2.3.

There is a constant δ>0\delta>0 such that δt≥δ\delta\_{t}\geq\delta almost surely, for all t=1,…,Tt=1,\ldots,T.

Our main result asserts that an investor with an arbitrary initial capital z∈ℝz\in\mathbb{R} may
find an optimal portfolio strategy X∗​(z)X^{\*}(z).

###### Theorem 2.4.

Let Assumption [2.1](https://arxiv.org/html/2511.12093v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2 Setup and results ‣ On the utility problem in a market where price impact is transient") and Assumption [2.3](https://arxiv.org/html/2511.12093v1#S2.Thmtheorem3 "Assumption 2.3. ‣ 2 Setup and results ‣ On the utility problem in a market where price impact is transient") be in force.
Then, for each z∈ℝz\in\mathbb{R} there exists X∗​(z)∈𝒜0X^{\*}(z)\in\mathcal{A}\_{0} such that

|  |  |  |
| --- | --- | --- |
|  | u¯​(z):=𝔼​[u​(z+ξTX∗​(z)−B)]=supX∈𝒜0𝔼​[u​(z+ξTX−B)].\bar{u}(z):=\mathbb{E}\left[u\left(z+\xi^{X^{\*}(z)}\_{T}-B\right)\right]=\sup\_{X\in\mathcal{A}\_{0}}\mathbb{E}\left[u\left(z+\xi^{X}\_{T}-B\right)\right]. |  |

Theorem [2.4](https://arxiv.org/html/2511.12093v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2 Setup and results ‣ On the utility problem in a market where price impact is transient") shows that, despite the possible lack of convexity for the set of attainable values
(see Example [2.5](https://arxiv.org/html/2511.12093v1#S2.Thmtheorem5 "Example 2.5. ‣ 2 Setup and results ‣ On the utility problem in a market where price impact is transient") below), the utility maximization
problem admits an optimal strategy. We will present the proof of Theorem [2.4](https://arxiv.org/html/2511.12093v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2 Setup and results ‣ On the utility problem in a market where price impact is transient")
in the coming sections, using
a customized dynamic programming procedure.

From now on, for any stochastic process ZtZ\_{t}, we denote its increments by
Δ​Zt:=Zt−Zt−1\Delta Z\_{t}:=Z\_{t}-Z\_{t-1}, 0≤t≤T0\leq t\leq T with the convention Z−1:=0Z\_{-1}:=0.
It is convenient to use another parametrization for strategies: for a given real-valued
process HtH\_{t}, 1≤t≤T1\leq t\leq T such that HtH\_{t} is ℱt−1\mathcal{F}\_{t-1}-measurable,
we may assign a unique strategy XtX\_{t} such that X0=0X\_{0}=0, Δ​Xt=Ht\Delta X\_{t}=H\_{t},
1≤t≤T1\leq t\leq T. For such strategies we will also use the alternative notations
ζH,ξH\zeta^{H},\xi^{H} for the corresponding half-spread and portfolio value processes.
With a slight abuse of notation we will also write H∈𝒜0H\in\mathcal{A}\_{0} when
we really mean that the corresponding XX is in 𝒜0\mathcal{A}\_{0}. Note that H∈𝒜0H\in\mathcal{A}\_{0}
implies that HT=−∑j=1T−1HjH\_{T}=-\sum\_{j=1}^{T-1}H\_{j}, in particular, HTH\_{T} is ℱT−2\mathcal{F}\_{T-2}-measurable.

Introduce the notation ρj,t:=exp⁡[−∑i=jt−1ri]\rho\_{j,t}:=\exp\left[-\sum\_{i=j}^{t-1}r\_{i}\right], 1≤t≤T1\leq t\leq T,
0≤j≤t0\leq j\leq t. Note that ρt,t=1\rho\_{t,t}=1.
From ([1](https://arxiv.org/html/2511.12093v1#S2.E1 "In 2 Setup and results ‣ On the utility problem in a market where price impact is transient")) and ([2](https://arxiv.org/html/2511.12093v1#S2.E2 "In 2 Setup and results ‣ On the utility problem in a market where price impact is transient")) we derive the explicit formula

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξTX=−∑t=1TPt​Ht−∑t=1T|Ht|​(ρ0,t​ζ0+∑j=1tρj,tδj​|Hj|).\xi\_{T}^{X}=-\sum\_{t=1}^{T}P\_{t}H\_{t}-\sum\_{t=1}^{T}|H\_{t}|\left(\rho\_{0,t}\zeta\_{0}+\sum\_{j=1}^{t}\frac{\rho\_{j,t}}{\delta\_{j}}|H\_{j}|\right). |  | (4) |

###### Example 2.5.

Let T=3T=3, rt=0r\_{t}=0 for all 0≤t≤30\leq t\leq 3, P0=ζ0=0P\_{0}=\zeta\_{0}=0 and let
P1,P2,P3P\_{1},P\_{2},P\_{3} be independent standard Gaussian.
Let ℱt\mathcal{F}\_{t}, 0≤t≤30\leq t\leq 3 be the natural filtration of the process PP.
Let δ1=1\delta\_{1}=1, δ2=δ3=10\delta\_{2}=\delta\_{3}=10. We claim that the set

|  |  |  |
| --- | --- | --- |
|  | 𝒮:={Y∈L0:∃X∈𝒜0​ such that ​ξTX≥Y}\mathcal{S}:=\{Y\in L^{0}:\exists X\in\mathcal{A}\_{0}\mbox{ such that }\xi^{X}\_{T}\geq Y\} |  |

fails convexity. We argue by contradiction.
Convexity would imply, in particular, that for arbitrary *non-negative deterministic*
strategies Hi,GiH\_{i},G\_{i},
i=1,2i=1,2 such that H3:=−H1−H2H\_{3}:=-H\_{1}-H\_{2}, G3=−G1−G2G\_{3}=-G\_{1}-G\_{2}, there would exist some H¯i\bar{H}\_{i}, i=1,2,3i=1,2,3 such that

|  |  |  |
| --- | --- | --- |
|  | ξTH¯≥ξTH+ξTG2\xi^{\bar{H}}\_{T}\geq\frac{\xi^{H}\_{T}+\xi^{G}\_{T}}{2} |  |

almost surely. In view of ([4](https://arxiv.org/html/2511.12093v1#S2.E4 "In 2 Setup and results ‣ On the utility problem in a market where price impact is transient")), this inequality can be rewritten as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | 12​[H12+H2​H1+110​H22+(H1+H2)​H1+110​(H1+H2)​H2+110​(H1+H2)2]\displaystyle\frac{1}{2}\left[H\_{1}^{2}+H\_{2}H\_{1}+\frac{1}{10}H\_{2}^{2}+(H\_{1}+H\_{2})H\_{1}+\frac{1}{10}(H\_{1}+H\_{2})H\_{2}+\frac{1}{10}(H\_{1}+H\_{2})^{2}\right] |  |
|  |  | +\displaystyle+ | 12​[G12+G2​G1+110​G22+(G1+G2)​G1+110​(G1+G2)​G2+110​(G1+G2)2]\displaystyle\frac{1}{2}\left[G\_{1}^{2}+G\_{2}G\_{1}+\frac{1}{10}G\_{2}^{2}+(G\_{1}+G\_{2})G\_{1}+\frac{1}{10}(G\_{1}+G\_{2})G\_{2}+\frac{1}{10}(G\_{1}+G\_{2})^{2}\right] |  |
|  |  | −\displaystyle- | [H¯12+H¯2​H¯1+110​H¯12+(H¯1+H¯2)​H¯1+110​(H¯1+H¯2)​H¯2+110​(H¯1+H¯2)2]\displaystyle\left[\bar{H}\_{1}^{2}+\bar{H}\_{2}\bar{H}\_{1}+\frac{1}{10}\bar{H}\_{1}^{2}+(\bar{H}\_{1}+\bar{H}\_{2})\bar{H}\_{1}+\frac{1}{10}(\bar{H}\_{1}+\bar{H}\_{2})\bar{H}\_{2}+\frac{1}{10}(\bar{H}\_{1}+\bar{H}\_{2})^{2}\right] |  |
|  |  | ≥\displaystyle\geq | (H¯3−H32−G32)​P3+(H¯2−H22−G22)​P2+(H¯1−H12−G12)​P1.\displaystyle{}\left(\bar{H}\_{3}-\frac{H\_{3}}{2}-\frac{G\_{3}}{2}\right)P\_{3}+\left(\bar{H}\_{2}-\frac{H\_{2}}{2}-\frac{G\_{2}}{2}\right)P\_{2}+\left(\bar{H}\_{1}-\frac{H\_{1}}{2}-\frac{G\_{1}}{2}\right)P\_{1}. |  |

Notice that the ℱ2\mathcal{F}\_{2}-conditional law of (H¯3−H3/2−G3/2)​P3(\bar{H}\_{3}-H\_{3}/2-G\_{3}/2)P\_{3}
is nondegenerate Gaussian on the set {H¯3−H3/2−G3/2≠0}\{\bar{H}\_{3}-H\_{3}/2-G\_{3}/2\neq 0\}. Also, the left-hand
side and the last two terms of the right-hand side are ℱ2\mathcal{F}\_{2} measurable. Hence
the above inequality necessarily implies that ℙ​(H¯3−H3/2−G3/2≠0)=0\mathbb{P}(\bar{H}\_{3}-H\_{3}/2-G\_{3}/2\neq 0)=0.
By an analogous argument, also H¯i−Hi/2−Gi/2=0\bar{H}\_{i}-H\_{i}/2-G\_{i}/2=0, i=1,2i=1,2. But then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | 12​[2110​H12+310​H22+2310​H1​H2+2110​G12+310​G22+2310​G1​G2]\displaystyle\frac{1}{2}\left[\frac{21}{10}H\_{1}^{2}+\frac{3}{10}H\_{2}^{2}+\frac{23}{10}H\_{1}H\_{2}+\frac{21}{10}G\_{1}^{2}+\frac{3}{10}G\_{2}^{2}+\frac{23}{10}G\_{1}G\_{2}\right] |  |
|  |  | ≥\displaystyle\geq | 2110​H¯12+310​H¯22+2310​H¯1​H¯2.\displaystyle\frac{21}{10}\bar{H}\_{1}^{2}+\frac{3}{10}\bar{H}\_{2}^{2}+\frac{23}{10}\bar{H}\_{1}\bar{H}\_{2}. |  |

The latter property, however, badly fails. Take, for instance, H1=H2=1H\_{1}=H\_{2}=1 and G1=1.5G\_{1}=1.5, G2=0G\_{2}=0.
We conclude that 𝒮\mathcal{S} is *not* a convex set.

###### Remark 2.6.

The paper [[1](https://arxiv.org/html/2511.12093v1#bib.bib1)] made a monotonicity
assumption. In the current discrete-time context it would require that the process ρ0,t2​δt\rho\_{0,t}^{2}\delta\_{t} is a.s.
strictly decreasing in tt.
Under this hypothesis, [[1](https://arxiv.org/html/2511.12093v1#bib.bib1)] showed that 𝒮\mathcal{S} is convex. The novel
contribution of our work is to drop such monotonicity assumptions and nevertheless to prove the existence
of optimal strategies.

We finally point out in a simple example why
non-convexity of the domain of optimization may cause trouble in optimal investment problems.

###### Example 2.7.

We consider a one-step frictionless market model.
Let the family of permitted strategies be Φ:={0,1}\Phi:=\{0,1\}. That is, the investor
may take either a unit position in the risky asset or no position at all. Let us consider the utility function
u​(x):=ln⁡(x)u(x):=\ln(x) for x>0x>0.
Let the investor have initial capital z>1z>1. Assume that the return on his investment is
a random variable RR with ℙ​(R=2)=1/2=ℙ​(R=−1)\mathbb{P}(R=2)=1/2=\mathbb{P}(R=-1). His indirect utility is then

|  |  |  |
| --- | --- | --- |
|  | u¯​(z):=supϕ∈Φ𝔼​[u​(z+ϕ​R)]=max⁡{ln⁡(z),ln⁡(z+2)+ln⁡(z−1)2},z>1.\bar{u}(z):=\sup\_{\phi\in\Phi}\mathbb{E}[u(z+\phi R)]=\max\left\{\ln(z),{}\frac{\ln(z+2)+\ln(z-1)}{2}\right\},\ z>1. |  |

This function fails concavity: it is non-differentiable
at 22 with the right-hand derivative being strictly larger than the left-hand derivative.

We conclude that even if the investor’s utility is risk-averse (concave), his/her *indirect* utility
may well fail this property when the family of permitted strategies is non-convex. Hence
in related multistep optimization problems
one needs to deal with a dynamic programming procedure involving *non-concave*
functions, as in [[4](https://arxiv.org/html/2511.12093v1#bib.bib4)].

## 3 Preparation for the proof

Recall from ([2](https://arxiv.org/html/2511.12093v1#S2.E2 "In 2 Setup and results ‣ On the utility problem in a market where price impact is transient")) and ([1](https://arxiv.org/html/2511.12093v1#S2.E1 "In 2 Setup and results ‣ On the utility problem in a market where price impact is transient")) that

|  |  |  |
| --- | --- | --- |
|  | Δ​ξtH=−Pt​Ht−|Ht|​(ρ0,t​ζ0+∑j=1tρj,tδj​|Hj|).\Delta\xi\_{t}^{H}=-P\_{t}H\_{t}-|H\_{t}|\left(\rho\_{0,t}\zeta\_{0}+\sum\_{j=1}^{t}\frac{\rho\_{j,t}}{\delta\_{j}}|H\_{j}|\right). |  |

Inspired by this formula, for 1≤t≤T1\leq t\leq T and h=(h1,…,ht)h=(h\_{1},\ldots,h\_{t}) we introduce the random functions

|  |  |  |  |
| --- | --- | --- | --- |
|  | κt​(h):=−Pt​ht−|ht|​(ρ0,t​ζ0+∑j=1tρj,tδj​|hj|)\kappa\_{t}(h):=-P\_{t}h\_{t}-|h\_{t}|\left(\rho\_{0,t}\zeta\_{0}+\sum\_{j=1}^{t}\frac{\rho\_{j,t}}{\delta\_{j}}|h\_{j}|\right) |  | (5) |

for all h1,…,ht∈ℝh\_{1},\ldots,h\_{t}\in\mathbb{R}. Note that the mapping, describing the innovation corresponding to a deterministic action of the trader,

|  |  |  |
| --- | --- | --- |
|  | ht→κt​((h1,…,ht−1,ht)),h\_{t}\to\kappa\_{t}((h\_{1},\ldots,h\_{t-1},h\_{t})), |  |

is *concave* for every fixed (h1,…,ht−1)(h\_{1},\ldots,h\_{t-1}),
but κt\kappa\_{t}, as a function of tt variables, has no reason to be concave.
Note also that innovation has an ”action-independent” market bound, namely the quantity

|  |  |  |  |
| --- | --- | --- | --- |
|  | κt​((h1,…,ht))≤λt​(ht):=−Pt​ht−ht2δt≤Pt2​δt4.\kappa\_{t}((h\_{1},\ldots,h\_{t}))\leq\lambda\_{t}(h\_{t}):=-P\_{t}h\_{t}-\frac{h\_{t}^{2}}{\delta\_{t}}\leq\frac{P\_{t}^{2}\delta\_{t}}{4}. |  | (6) |

We recall Lemma 6.8 of [[4](https://arxiv.org/html/2511.12093v1#bib.bib4)].

###### Lemma 3.1.

Let (Ω,ℋ,P)(\Omega,{\cal H},P) be a complete probability space. Let Ξd\Xi^{d} be the set of
ℋ\mathcal{H}-measurable dd-dimensional random variables.
Let F:Ω×ℝd→ℝF:\Omega\times\mathbb{R}^{d}\to\mathbb{R} be a function such that for almost all ω∈Ω\omega\in\Omega,
F​(ω,⋅)F(\omega,\cdot) is continuous and for each y∈ℝdy\in\mathbb{R}^{d}, F​(⋅,y)F(\cdot,y) is ℋ{\cal H}-measurable. Let K>0K>0 be
an ℋ{\cal H}-measurable random variable.

Set f​(ω)=ess.supξ∈Ξd,|ξ|≤KF​(ω,ξ​(ω))f(\omega)=\mathrm{ess.}\sup\_{\xi\in\Xi^{d},|\xi|\leq K}F(\omega,\xi(\omega)). Then,
for almost all ω\omega,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | f​(ω)\displaystyle f(\omega) | =\displaystyle= | supy∈ℝd,|y|≤K​(ω)F​(ω,y).\displaystyle\sup\_{y\in\mathbb{R}^{d},|y|\leq K(\omega)}F(\omega,y). |  | (7) |

□\square

A compactness result involving random subsequences comes next, this is Lemma 2 of [[6](https://arxiv.org/html/2511.12093v1#bib.bib6)].

###### Lemma 3.2.

Let ℋ⊂ℱ\mathcal{H}\subset\mathcal{F} be a sigma-algebra.
Let XnX\_{n} be a sequence of ℋ\mathcal{H}-measurable dd-dimensional random variables such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim infn→∞|Xn|<∞\liminf\_{n\to\infty}|X\_{n}|<\infty |  | (8) |

almost surely. Then there exist
ℋ\mathcal{H}-measurable random variables
nk:Ω→ℕn\_{k}:\Omega\to\mathbb{N}, k∈ℕk\in\mathbb{N} with nk​(ω)<nk+1​(ω)n\_{k}(\omega)<n\_{k+1}(\omega) for all ω∈Ω\omega\in\Omega
and k∈ℕk\in\mathbb{N} and an ℋ\mathcal{H}-measurable
random variable XX such that Xnk→XX\_{n\_{k}}\to X a.s. In such a case we write that
*there exists an ℋ\mathcal{H}-measurable
random subsequence*. □\square

The following lemma uses the same idea as Lemma A.3 of [[8](https://arxiv.org/html/2511.12093v1#bib.bib8)]; it provides continuous versions
for certain random fields.

###### Lemma 3.3.

Let ℋ⊂ℱ\mathcal{H}\subset\mathcal{F} be a sigma-algebra.
Define 𝒦:=[−N,N]n\mathcal{K}:=[-N,N]^{n}.
Let L:Ω×𝒦→ℝL:\Omega\times\mathcal{K}\to\mathbb{R} be such that for a.e. ω∈Ω\omega\in\Omega,
L​(ω,⋅)L(\omega,\cdot) is continuous and for all x∈𝒦x\in\mathcal{K}, L​(⋅,x)L(\cdot,x) is
measurable such that supz∈𝒦|L​(ω,z)|\sup\_{z\in\mathcal{K}}|L(\omega,z)| is integrable.
Then there is l:Ω×𝒦→ℝl:\Omega\times\mathcal{K}\to\mathbb{R} such that for a.e. ω∈Ω\omega\in\Omega,
l​(ω,⋅)l(\omega,\cdot) is continuous and for all k∈𝒦k\in\mathcal{K}, E​(L​(k)|ℋ)=l​(k)E(L(k)|\mathcal{H})=l(k) a.s.

###### Proof.

Consider the separable Banach space
𝔹:=C​([−N,N]n)\mathbb{B}:=C([-N,N]^{n}) of continuous functions on [−N,N]n[-N,N]^{n} with the supremum norm. Clearly, L:Ω→𝔹L:\Omega\to\mathbb{B} and
for all μ\mu in the dual space 𝔹′\mathbb{B}^{\prime} (which can be represented as a Borel signed measure),
μ​(L)=∫𝒦L​(ω,x)​μ​(d​x)\mu(L)=\int\_{\mathcal{K}}L(\omega,x)\mu(dx)
is a measurable function on (Ω,ℱ)(\Omega,\mathcal{F}): indeed, this is clear for
μ\mu with finite support and then follows for general μ\mu by approximation.
Note that, for each k∈𝒦k\in\mathcal{K}, the linear functional
fk​(x):=x​(k)f\_{k}(x):=x(k), x∈𝔹x\in\mathbb{B} is continuous (w.r.t. the norm of 𝔹\mathbb{B}) so
fk∈𝔹′f\_{k}\in\mathbb{B}^{\prime}. Now it follows
from Proposition V.2.5. of [[7](https://arxiv.org/html/2511.12093v1#bib.bib7)] that there is a measurable l:Ω→𝔹l:\Omega\to\mathbb{B}
such that

|  |  |  |
| --- | --- | --- |
|  | l​(k)=fk​(l)=E​(fk​(L)|ℋ)=E​(L​(k)|ℋ),l(k)=f\_{k}(l)=E(f\_{k}(L)|\mathcal{H})=E(L(k)|\mathcal{H}), |  |

for each k∈𝒦k\in\mathcal{K}, as claimed.
∎

Now we turn to a set of Lemmas that ensure that we can perform a backward iteration,
and produce a series of actions that forms a candidate strategy of optimal execution.

## 4 Single step case

Let t≥1t\geq 1 be an integer and let 𝒢,ℋ\mathcal{G},\mathcal{H} be ℙ\mathbb{P}-complete sigma-algebras
over Ω\Omega such that ℋ⊂𝒢⊂ℱ\mathcal{H}\subset\mathcal{G}\subset\mathcal{F} holds, and denote the set of ℋ\mathcal{H}-measurable
ℝ\mathbb{R}-valued random variables by Ξ\Xi. We will consider functions

|  |  |  |
| --- | --- | --- |
|  | G0:Ω×ℝ×ℝt→ℝ,(x,v)↦G0​(x,v),G\_{0}:\Omega\times\mathbb{R}\times\mathbb{R}^{t}\to\mathbb{R},\ (x,v)\mapsto G\_{0}(x,v), |  |

and

|  |  |  |
| --- | --- | --- |
|  | V:Ω×ℝ×ℝt−1×ℝ→ℝ,(x,j,h)↦G0​(x+κt​((j,h)),(j,h)),V:\Omega\times\mathbb{R}\times\mathbb{R}^{t-1}\times\mathbb{R}\to\mathbb{R},\ (x,j,h)\mapsto G\_{0}(x+\kappa\_{t}((j,h)),(j,h)), |  |

where (j,h)=(j1,…,jt−1,h)(j,h)=(j\_{1},\ldots,j\_{t-1},h), and the κt\kappa\_{t} is as in ([5](https://arxiv.org/html/2511.12093v1#S3.E5 "In 3 Preparation for the proof ‣ On the utility problem in a market where price impact is transient")). Below we introduce assumptions that serve as a basis
for the iterative arguments later.

###### Assumption 4.1.

The function G0G\_{0} is
𝒢⊗ℬ​(ℝ)⊗ℬ​(ℝt)\mathcal{G}\otimes\mathcal{B}(\mathbb{R})\otimes\mathcal{B}(\mathbb{R}^{t})-measurable, the mapping G0​(ω,⋅,⋅)G\_{0}(\omega,\cdot,\cdot), is jointly continuous
and non-decreasing in its first variable, ℙ\mathbb{P}-almost surely.

###### Assumption 4.2.

There exists a function G¯0:Ω×ℝ↦ℝ\bar{G}\_{0}:\Omega\times\mathbb{R}\mapsto\mathbb{R}, and a constant C>0C>0, such that for all x∈ℝx\in\mathbb{R} there exists a zero measure set outside of which

|  |  |  |
| --- | --- | --- |
|  | G¯0​(x)→−∞\bar{G}\_{0}(x)\to-\infty |  |

holds as x→−∞x\to-\infty. Furthermore, G0​(ω,⋅)G\_{0}(\omega,\cdot) is non-decreasing almost surely, and for all pairs (x,v)∈ℝ×ℝt(x,v)\in\mathbb{R}\times\mathbb{R}^{t} we have that the inequalities

|  |  |  |
| --- | --- | --- |
|  | G0​(x,v)≤G¯0​(x)≤CG\_{0}(x,v)\leq\bar{G}\_{0}(x)\leq C |  |

hold, again outside a set of measure zero.

###### Assumption 4.3.

Assume that for any m∈ℕm\in\mathbb{N} and for all 1≤t′≤t1\leq t^{{}^{\prime}}\leq t, there exists an integrable random variable M=M​(m,t′)M=M(m,t^{{}^{\prime}}) so that

|  |  |  |
| --- | --- | --- |
|  | M≤G0​(x+κt′​((v1,…,vt′)),v)M\leq G\_{0}(x+\kappa\_{t^{{}^{\prime}}}((v\_{1},\ldots,v\_{t^{{}^{\prime}}})),v) |  |

holds for every x∈[−m,m]x\in[-m,m], v∈[−m,m]tv\in[-m,m]^{t}, and for almost every ω∈Ω\omega\in\Omega.

Throughout Section [4](https://arxiv.org/html/2511.12093v1#S4 "4 Single step case ‣ On the utility problem in a market where price impact is transient") we postulate that the conditions prescribed by Assumption [4.1](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem1 "Assumption 4.1. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), Assumption [4.2](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem2 "Assumption 4.2. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), and Assumption [4.3](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem3 "Assumption 4.3. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") hold.

###### Lemma 4.4.

There exists L:Ω×ℝ×ℝt−1×ℝ→ℝL:\Omega\times\mathbb{R}\times\mathbb{R}^{t-1}\times\mathbb{R}\to\mathbb{R} so that for all (x,j,h)∈ℝ×ℝt−1×ℝ(x,j,h)\in\mathbb{R}\times\mathbb{R}^{t-1}\times\mathbb{R} we have

|  |  |  |
| --- | --- | --- |
|  | E​[V​(x,j,h)|ℋ]=L​(x,j,h)E[V(x,j,h)|\mathcal{H}]=L(x,j,h) |  |

almost surely, and furthermore, L​(⋅,⋅,⋅)L(\cdot,\cdot,\cdot) is continuous in all its variables for almost all ω∈Ω\omega\in\Omega.

###### Proof.

Under Assumption [4.1](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem1 "Assumption 4.1. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), Assumption [4.2](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem2 "Assumption 4.2. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), and Assumption [4.3](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem3 "Assumption 4.3. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") the proof is a direct consequence of Lemma [3.3](https://arxiv.org/html/2511.12093v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3 Preparation for the proof ‣ On the utility problem in a market where price impact is transient").

∎

###### Lemma 4.5.

Let LL be as in Lemma [4.4](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), G¯0\bar{G}\_{0} be as in Assumption [4.2](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem2 "Assumption 4.2. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"),
λt\lambda\_{t} be as in ([6](https://arxiv.org/html/2511.12093v1#S3.E6 "In 3 Preparation for the proof ‣ On the utility problem in a market where price impact is transient")), and let x∈ℝx\in\mathbb{R}. As |h|→−∞|h|\to-\infty we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supj∈ℝt−1L​(x,j,h)→−∞\displaystyle\sup\_{j\in\mathbb{R}^{t-1}}L(x,j,h)\to-\infty |  | (9) |

almost surely. (In the case t=1t=1 we mean that LL does not depend on jj and there is no supremum.)

###### Proof.

Without loss of generality we assume t=2t=2, the case of t>2t>2 being only notationally more cumbersome.
By Assumption [4.2](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem2 "Assumption 4.2. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), the definition of LL and using ([6](https://arxiv.org/html/2511.12093v1#S3.E6 "In 3 Preparation for the proof ‣ On the utility problem in a market where price impact is transient")), we have for all x,j,h∈ℝx,j,h\in\mathbb{R} that

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(x,j,h)\displaystyle L(x,j,h) | =E​[V​(x,j,h)|ℋ]\displaystyle=E[V(x,j,h)|\mathcal{H}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤E​[G¯0​(x+κ2​(j,h))|ℋ]\displaystyle\leq E[\bar{G}\_{0}(x+\kappa\_{2}(j,h))|\mathcal{H}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤E​[G¯0​(x+λ2​(h))|ℋ]\displaystyle\leq E[\bar{G}\_{0}(x+\lambda\_{2}(h))|\mathcal{H}] |  |

almost surely. Apply Fatou’s reverse lemma to the inequalities above.
Considering ([6](https://arxiv.org/html/2511.12093v1#S3.E6 "In 3 Preparation for the proof ‣ On the utility problem in a market where price impact is transient")) and the absence of dependence on the variable jj, continuity of G¯0\bar{G}\_{0} shows ([9](https://arxiv.org/html/2511.12093v1#S4.E9 "In Lemma 4.5. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient")).
∎

###### Lemma 4.6.

The inequality

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | L​(x1,j,h)≤L​(x2,j,h),\displaystyle\begin{split}&L(x\_{1},j,h)\leq L(x\_{2},j,h),\end{split} | |  | (10) |

holds for all x1,x2,h∈ℝx\_{1},x\_{2},h\in\mathbb{R} with x1<x2x\_{1}<x\_{2}, for all j∈ℝt−1j\in\mathbb{R}^{t-1}, and for almost every ω∈Ω\omega\in\Omega.

###### Proof.

Without loss of generality we can assume t=2t=2. let Ω′\Omega^{\prime} be a ℙ\mathbb{P}-full measure set such that ([10](https://arxiv.org/html/2511.12093v1#S4.E10 "In Lemma 4.6. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient")) holds for all x1,x2,j,h∈ℚx\_{1},x\_{2},j,h\in\mathbb{Q}
on Ω′\Omega^{\prime}. Let Ω′′\Omega^{\prime\prime} be the full measure set on which LL is continuous. Then on Ω′∩Ω′′\Omega^{\prime}\cap\Omega^{\prime\prime} ([10](https://arxiv.org/html/2511.12093v1#S4.E10 "In Lemma 4.6. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient")) holds
for *all* x1,x2,j,h∈ℝx\_{1},x\_{2},j,h\in\mathbb{R}, by continuity.

∎

###### Lemma 4.7.

Fix l∈ℤl\in\mathbb{Z} and m∈ℕm\in\mathbb{N}. There exits an ℋ\mathcal{H}-measurable K=K​(l,m)K=K(l,m) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(x,j,h)≤L​(x,j,h​𝟏{|h|≤K}),L(x,j,h)\leq L(x,j,h\mathbf{1}\_{\{|h|\leq K\}}), |  | (11) |

for all x∈[l,l+1]x\in[l,l+1], j∈[−m,m]t−1⊂ℝt−1j\in[-m,m]^{t-1}\subset\mathbb{R}^{t-1}, h∈ℝh\in\mathbb{R}, and for almost every ω∈Ω\omega\in\Omega.

###### Proof.

Without loss of generality assume t=2t=2, and let Ω¯\bar{\Omega} denote the full measure set
where the conclusion of Lemma [4.4](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") and Lemma [4.6](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem6 "Lemma 4.6. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") hold.
For every ω∈Ω¯\omega\in\bar{\Omega} choose a (measurable) m+​(h)=m+​(ω,l,h)m^{+}(h)=m^{+}(\omega,l,h) such that

|  |  |  |
| --- | --- | --- |
|  | L​(l+1,j,h)​(ω)≤L​(l+1,m+​(h),h)​(ω)\displaystyle L(l+1,j,h)(\omega)\leq L(l+1,m^{+}(h),h)(\omega) |  |

holds for all j∈[−m,m]j\in[-m,m] and h∈ℝh\in\mathbb{R}, this is possible by continuity of LL. Likewise, for every ω∈Ω¯\omega\in\bar{\Omega} choose m−=m−​(ω,l)m^{-}=m^{-}(\omega,l) such that

|  |  |  |
| --- | --- | --- |
|  | L​(l,m−,0)​(ω)≤L​(l,j,0)​(ω)\displaystyle L(l,m^{-},0)(\omega)\leq L(l,j,0)(\omega) |  |

holds for all j∈[−m,m]j\in[-m,m].
Fix l∈ℤl\in\mathbb{Z} and m∈ℕm\in\mathbb{N}. Using Lemma [4.5](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem5 "Lemma 4.5. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") for all ω∈Ω¯\omega\in\bar{\Omega} there exists K​(ω)=K​(ω,l,m)K(\omega)=K(\omega,l,m) so that for all h∈ℝh\in\mathbb{R} it holds that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |h|>K​(ω)⟹L​(l+1,m+​(h),h)​(ω)≤L​(l,m−,0)​(ω).\displaystyle\begin{split}|h|>K(\omega)\implies L(l+1,m^{+}(h),h)(\omega)\leq L(l,m^{-},0)(\omega).\end{split} | |  | (12) |

Now note, that ω→K​(ω)\omega\to K(\omega) can be chosen in a way that it is ℋ\mathcal{H}-measurable as a random variable. On the event {|h|>K}∩Ω¯\{|h|>K\}\cap\bar{\Omega}, using Lemma [4.6](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem6 "Lemma 4.6. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), and the statement in ([12](https://arxiv.org/html/2511.12093v1#S4.E12 "In 4 Single step case ‣ On the utility problem in a market where price impact is transient")), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | L​(x,j,h)≤L​(l+1,j,h)≤L​(l+1,m+​(h),h),≤L​(l,m−,0)≤L​(l,j,0)≤L​(x,j,0),\displaystyle\begin{split}&L(x,j,h)\leq L(l+1,j,h)\leq L(l+1,m^{+}(h),h),\\ &\leq L(l,m^{-},0)\leq L(l,j,0)\leq L(x,j,0),\end{split} | |  | (13) |

for every x∈[l,l+1]x\in[l,l+1], j∈[−m,m]j\in[-m,m], h∈ℝh\in\mathbb{R}, and for all ω∈Ω¯\omega\in\bar{\Omega}: completing the argument.
∎

###### Lemma 4.8.

There exists an ℋ⊗ℬ​(ℝ)\mathcal{H}\otimes\mathcal{B}(\mathbb{R})-measurable function

|  |  |  |
| --- | --- | --- |
|  | G:Ω×ℝ×ℝt−1↦ℝ,G:\Omega\times\mathbb{R}\times\mathbb{R}^{t-1}\mapsto\mathbb{R}, |  |

such that GG is
continuous almost surely, GG is non-decreasing in its first variable for almost all
ω∈Ω\omega\in\Omega, furthermore, for all xx, and for all j∈ℝt−1j\in\mathbb{R}^{t-1} we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G​(x,j)=ess.supH∈ΞL​(x,j,H),\displaystyle\begin{split}G(x,j)=\mathrm{ess.}\sup\_{H\in\Xi}L(x,j,H),\end{split} | |  | (14) |

almost surely.

###### Proof.

We follow arguments of Lemma 3.17 in [[4](https://arxiv.org/html/2511.12093v1#bib.bib4)].
Let x,j∈ℝx,j\in\mathbb{R}, and without loss of generality assume t=2t=2 and set l∈ℤl\in\mathbb{Z}
and m∈ℕm\in\mathbb{N} so that x∈[l,l+1]x\in[l,l+1] and j∈[−m,m]j\in[-m,m] holds. We will
work out the statement in consideration elementwise on Ω\Omega, and to this end – out of the usual – we
do not omit to display dependence on ω∈Ω\omega\in\Omega throughout the proof, until further notice.
Denote with Ω¯\bar{\Omega} the full measure set for which the conclusions of Lemma [4.4](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"),
[4.6](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem6 "Lemma 4.6. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), [4.7](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") hold, and let ω∈Ω¯\omega\in\bar{\Omega}. Let us define

|  |  |  |
| --- | --- | --- |
|  | B​(ω,x,j)=suph∈ℚ,|h|≤K​(ω)L​(ω,x,j,h)=suph∈ℝ,|h|≤K​(ω)L​(ω,x,j,h),\displaystyle B(\omega,x,j)=\sup\_{h\in\mathbb{Q},|h|\leq K(\omega)}L(\omega,x,j,h)=\sup\_{h\in\mathbb{R},|h|\leq K(\omega)}L(\omega,x,j,h), |  |

where K​(ω)=K​(ω,l,m)=K​(l,m)K(\omega)=K(\omega,l,m)=K(l,m) is as in Lemma [4.7](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient").
This is measurable, being the supremum of countably many measurable functions. Let us fix furthermore a sequence
(xn,jn)n∈ℕ⊂([l,l+1]×[−m,m])∩ℝ2(x\_{n},j\_{n})\_{n\in\mathbb{N}}\subset([l,l+1]\times[-m,m])\cap\mathbb{R}^{2} for which (xn,jn)→(x,j)(x\_{n},j\_{n})\to(x,j).
Observe, that by definition of BB, for every k∈ℕk\in\mathbb{N} there exists hk​(ω,x,j)h\_{k}(\omega,x,j), with
hk​(ω,x,j)≤K​(ω)h\_{k}(\omega,x,j)\leq K(\omega), so that B​(ω,x,j)−1/k≤L​(ω,x,j,hk​(ω,x,j))B(\omega,x,j)-1/k\leq L(\omega,x,j,h\_{k}(\omega,x,j)).
The fact that for all n∈ℕn\in\mathbb{N} we have B​(ω,xn,jn)≥L​(ω,xn,jn,hk​(ω,x,j))B(\omega,x\_{n},j\_{n})\geq L(\omega,x\_{n},j\_{n},h\_{k}(\omega,x,j)), along with continuity of LL yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim infnB​(ω,xn,jn)≥\displaystyle\liminf\_{n}B(\omega,x\_{n},j\_{n})\geq | L​(ω,x,j,hk​(ω,x,j))\displaystyle L(\omega,x,j,h\_{k}(\omega,x,j)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥B​(ω,x,j)−1/k,\displaystyle\geq B(\omega,x,j)-1/k, |  |

which in the limiting case of k→∞k\to\infty means lim infnB​(ω,xn,jn)≥B​(ω,x,j)\liminf\_{n}B(\omega,x\_{n},j\_{n})\geq B(\omega,x,j).

Take a sequence {nk,k∈ℕ}⊂ℕ\{n\_{k},\ k\in\mathbb{N}\}\subset\mathbb{N} so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supnB​(ω,xn,jn)=limkB​(ω,xnk,jnk).\displaystyle\limsup\_{n}B(\omega,x\_{n},j\_{n})=\lim\_{k}B(\omega,x\_{n\_{k}},j\_{n\_{k}}). |  | (15) |

Since {h:h∈ℚ,|h|≤K​(ω)}\{h:h\in\mathbb{Q},\ |h|\leq K(\omega)\} is a precompact set in ℝ\mathbb{R}, for every
k∈ℕk\in\mathbb{N} there exists ℝ∋hnk∗​(ω)≤K​(ω)\mathbb{R}\ni h\_{n\_{k}}^{\*}(\omega)\leq K(\omega) so that
B​(ω,xnk,jnk)=L​(ω,xnk,jnk,hnk∗​(ω))B(\omega,x\_{n\_{k}},j\_{n\_{k}})=L(\omega,x\_{n\_{k}},j\_{n\_{k}},h\_{n\_{k}}^{\*}(\omega)). Using the compactness of the
closure there exists ℝ∋h∗​(ω)≤K​(ω)\mathbb{R}\ni h^{\*}(\omega)\leq K(\omega) and a subsequence
(ak)k∈ℕ(a\_{k})\_{k\in\mathbb{N}} of {nk:k∈ℕ}\{n\_{k}:k\in\mathbb{N}\} so
that hak∗​(ω)→h∗​(ω)h^{\*}\_{a\_{k}}(\omega)\to h^{\*}(\omega), k→∞k\to\infty. These, and ([15](https://arxiv.org/html/2511.12093v1#S4.E15 "In 4 Single step case ‣ On the utility problem in a market where price impact is transient")) imply

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supn\displaystyle\limsup\_{n} | B​(ω,xn,jn)=limkB​(ω,xnk,jnk)=limkB​(ω,xak,jak)\displaystyle B(\omega,x\_{n},j\_{n})=\lim\_{k}B(\omega,x\_{n\_{k}},j\_{n\_{k}})=\lim\_{k}B(\omega,x\_{a\_{k}},j\_{a\_{k}}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =limkL​(ω,xak,jak,hak∗​(ω))=L​(ω,x,j,h∗​(ω))≤B​(ω,x,j),\displaystyle=\lim\_{k}L(\omega,x\_{a\_{k}},j\_{a\_{k}},h\_{a\_{k}}^{\*}(\omega))=L(\omega,x,j,h^{\*}(\omega))\leq B(\omega,x,j), |  |

establishing the continuity of BB.

As far as monotonicity is concerned, the mapping x→B​(ω,x,j)x\to B(\omega,x,j) inherits the
non-decreasing property from LL (stated in Lemma [4.6](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem6 "Lemma 4.6. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient")) naturally.

From Lemma [3.1](https://arxiv.org/html/2511.12093v1#S3.Thmtheorem1 "Lemma 3.1. ‣ 3 Preparation for the proof ‣ On the utility problem in a market where price impact is transient") it follows that

|  |  |  |
| --- | --- | --- |
|  | B​(ω,x,j)=ess.supH​(ω)≤K​(ω)​L​(ω,x,j,H​(ω)).\displaystyle B(\omega,x,j)=\mbox{ess.sup}\_{H(\omega)\leq K(\omega)}L(\omega,x,j,H(\omega)). |  |

In the discussion above ω∈Ω¯\omega\in\bar{\Omega} was arbitrary, and returning to the usual practice of not displaying the dependence on it, Lemma [4.7](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") shows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ess.supH∈Ξ​L​(x,j,H)≤ess.supΞ∋H≤K\displaystyle\mbox{ess.sup}\_{H\in\Xi}L(x,j,H)\leq\mbox{ess.sup}\_{\Xi\ni H\leq K} | L​(x,j,H)=B​(x,j)\displaystyle L(x,j,H)=B(x,j) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ess.supH∈Ξ​L​(x,j,H)\displaystyle\leq\mbox{ess.sup}\_{H\in\Xi}L(x,j,H) |  |

holds almost surely, finishing the argument.

∎

###### Lemma 4.9.

Let X,H1,…,Ht−1X,H\_{1},\ldots,H\_{t-1} be ℋ\mathcal{H}-measurable random variables, and let GG be as in Lemma [4.7](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"). Then, the quantity G​(X,(H1,…,Ht−1))G(X,(H\_{1},\ldots,H\_{t-1})) is a version of the essential supremum

|  |  |  |  |
| --- | --- | --- | --- |
|  | ess.supH∈Ξt−1L​(X,(H1,…,Ht−1),H).\displaystyle\begin{split}\mathrm{ess.}\sup\_{H\in\Xi\_{t-1}}L(X,(H\_{1},\ldots,H\_{t-1}),H).\end{split} | |  |

###### Proof.

Without loss of generality we assume that t=2t=2, and that XX and H1H\_{1} take values in [l,l+1][l,l+1] and [−m,m][-m,m]
respectively. Let XnX\_{n} and H1(n)H\_{1}^{(n)} be ℋ\mathcal{H}-measurable random variables, taking values in [l,l+1]∩ℚ[l,l+1]\cap\mathbb{Q} and
[−m,m]∩ℚ[-m,m]\cap\mathbb{Q}, respectively, for all n∈ℕn\in\mathbb{N}, and possessing also
the limiting properties Xn→XX\_{n}\to X and H1(n)→H1H\_{1}^{(n)}\to H\_{1}.

Observe that for all n∈ℕn\in\mathbb{N}, on a full measure set, we have that

|  |  |  |
| --- | --- | --- |
|  | ess.supH∈Ξt−1​L​(Xn,H1(n),H)=G​(Xn,H1(n)),\mathrm{ess.sup}\_{H\in\Xi\_{t-1}}L(X\_{n},H\_{1}^{(n)},H)=G(X\_{n},H\_{1}^{(n)}), |  |

and furthermore, as a consequence, for all n∈ℕn\in\mathbb{N} there exists HnH\_{n} so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(Xn,H1(n),Hn)≥G​(Xn,H1(n))−1/n\displaystyle L(X\_{n},H\_{1}^{(n)},H\_{n})\geq G(X\_{n},H\_{1}^{(n)})-1/n |  | (16) |

almost surely. According to Lemma [4.7](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") there exists an ℋ\mathcal{H}-measurable K=K​(l,m)=K​(ω,l,m)K=K(l,m)=K(\omega,l,m) so that

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(Xn,H1(n),Hn​𝟏{|Hn|≤K})≥L​(Xn,H1(n),Hn).\displaystyle L(X\_{n},H\_{1}^{(n)},H\_{n}\mathbf{1}\_{\{|H\_{n}|\leq K\}})\geq L(X\_{n},H\_{1}^{(n)},H\_{n}). |  | (17) |

Note that the KK does not depend on the integer nn in any way. Putting together ([16](https://arxiv.org/html/2511.12093v1#S4.E16 "In 4 Single step case ‣ On the utility problem in a market where price impact is transient")) and ([17](https://arxiv.org/html/2511.12093v1#S4.E17 "In 4 Single step case ‣ On the utility problem in a market where price impact is transient")) gives, for all n∈ℕn\in\mathbb{N} the almost sure inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(Xn,H1(n),Hn​𝟏{|Hn|≤K})≥G​(Xn,H1(n))−1/n.\displaystyle L(X\_{n},H\_{1}^{(n)},H\_{n}\mathbf{1}\_{\{|H\_{n}|\leq K\}})\geq G(X\_{n},H\_{1}^{(n)})-1/n. |  | (18) |

Now using Lemma [3.2](https://arxiv.org/html/2511.12093v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3 Preparation for the proof ‣ On the utility problem in a market where price impact is transient"), there exists an ℋ\mathcal{H}-measurable subsequence kn=kn​(ω),k∈ℕk\_{n}=k\_{n}(\omega),\ k\in\mathbb{N} and an ℋ\mathcal{H}-measurable H¯\bar{H} so that Hkn​𝟏{|Hkn|≤K}→H¯H\_{k\_{n}}\mathbf{1}\_{\{|H\_{k\_{n}}|\leq K\}}\to\bar{H} holds almost surely. In ([18](https://arxiv.org/html/2511.12093v1#S4.E18 "In 4 Single step case ‣ On the utility problem in a market where price impact is transient")) taking the limit as n→∞n\to\infty along the sequence kn,n∈ℕk\_{n},\ n\in\mathbb{N}, and utilizing continuity of LL and GG yields

|  |  |  |
| --- | --- | --- |
|  | L​(X,H1,H¯)≥G​(X,H1),\displaystyle L(X,H\_{1},\bar{H})\geq G(X,H\_{1}), |  |

which in return implies ess.supH∈Ξt−1​L​(X,H1,H)≥G​(X,H1)\mathrm{ess.sup}\_{H\in\Xi\_{t-1}}L(X,H\_{1},H)\geq G(X,H\_{1}).

On the other hand, by definition of GG, for every ℋ\mathcal{H}-measurable HH we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | L​(X,H1,H)=\displaystyle L(X,H\_{1},H)= | limnL​(Xn,H1(n),H)≤limness.supH​L​(Xn,H1(n),H)\displaystyle\lim\_{n}L(X\_{n},H\_{1}^{(n)},H)\leq\lim\_{n}\mbox{ess.sup}\_{H}L(X\_{n},H\_{1}^{(n)},H) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =limnG​(Xn,H1(n))=G​(X,H1).\displaystyle=\lim\_{n}G(X\_{n},H\_{1}^{(n)})=G(X,H\_{1}). |  |

Taking the essential supremum of both sides yields the inequality

|  |  |  |
| --- | --- | --- |
|  | ess.supH∈Ξt−1​L​(X,H1,H)≤G​(X,H1)\displaystyle\mathrm{ess.sup}\_{H\in\Xi\_{t-1}}L(X,H\_{1},H)\leq G(X,H\_{1}) |  |

on a full measure set: finishing the proof.
∎

###### Lemma 4.10.

Let GG be as in Lemma [4.8](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem8 "Lemma 4.8. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"). Let X,H1,…,Ht−1X,H\_{1},\ldots,H\_{t-1} be ℋ\mathcal{H}-measurable random variables. Then, there exists an ℋ\mathcal{H}-measurable H∗H^{\*} so that

|  |  |  |
| --- | --- | --- |
|  | G​(X,(H1,…,Ht−1))=L​(X,(H1,…,Ht−1),H∗)\displaystyle G(X,(H\_{1},\ldots,H\_{t-1}))=L(X,(H\_{1},\ldots,H\_{t-1}),H^{\*}) |  |

holds almost surely.

###### Proof.

Without loss of generality assume that t=2t=2, XX almost surely takes values in the closed interval [l,l+1][l,l+1], H1H\_{1} takes values in the closed interval [−m,m][-m,m] for some l∈ℤl\in\mathbb{Z} and for some m∈ℕm\in\mathbb{N}. Let us define

|  |  |  |
| --- | --- | --- |
|  | 𝒪={L​(X,H1,H),H∈Ξ​(ℋ)}.\mathcal{O}=\Big\{L(X,H\_{1},H),\ \ H\in\Xi(\mathcal{H})\Big\}. |  |

This set is upward directed in terms of the almost sure sense of the usual ”less than or equal” relation. Thus, using Proposition VI.1.1. of [[7](https://arxiv.org/html/2511.12093v1#bib.bib7)] we have that there exists a sequence {Hn,n∈ℕ}⊂Ξ​(ℋ)\{H\_{n},\ n\in\mathbb{N}\}\subset\Xi(\mathcal{H}) for which the limiting property

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | L​(X,H1,Hn)→G​(X,H1)\displaystyle\begin{split}L(X,H\_{1},H\_{n})\to G(X,H\_{1})\end{split} | |  | (19) |

holds almost surely as n→∞n\to\infty. Utilizing Lemma [4.7](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), and the K=K​(l,m)K=K(l,m) within, we have for each n∈ℕn\in\mathbb{N} that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | L(X,H1,Hn)≤L​(X,H1,Hn​𝟏{|Hn|≤K}),\displaystyle\begin{split}L&(X,H\_{1},H\_{n})\leq L(X,H\_{1},H\_{n}\mathbf{1}\_{\{|H\_{n}|\leq K\}}),\end{split} | |  | (20) |

almost surely. Then, again using Lemma [3.2](https://arxiv.org/html/2511.12093v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3 Preparation for the proof ‣ On the utility problem in a market where price impact is transient"), there exists an ℋ\mathcal{H}-measurable subsequence,
say kn,n∈ℕk\_{n},\ n\in\mathbb{N}, and there exists an ℋ\mathcal{H}-measurable H∗H^{\*} so that

|  |  |  |
| --- | --- | --- |
|  | Hkn​𝟏{|Hkn|≤K}→H∗H\_{k\_{n}}\mathbf{1}\_{\{|H\_{k\_{n}}|\leq K\}}\to H^{\*} |  |

in the almost sure sense. Continuity of LL, ([19](https://arxiv.org/html/2511.12093v1#S4.E19 "In 4 Single step case ‣ On the utility problem in a market where price impact is transient")), and ([20](https://arxiv.org/html/2511.12093v1#S4.E20 "In 4 Single step case ‣ On the utility problem in a market where price impact is transient")) together guarantees

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(X,H1)=limn→∞L​(X,H1,Hkn)≤limn→∞L​(X,Hkn​𝟏{|Hkn|≤K})=L​(X,H1,H∗).\displaystyle\begin{split}G(X,H\_{1})&=\lim\_{n\to\infty}L(X,H\_{1},H\_{k\_{n}})\\ \leq&\lim\_{n\to\infty}L(X,H\_{k\_{n}}\mathbf{1}\_{\{|H\_{k\_{n}}|\leq K\}})=L(X,H\_{1},H^{\*}).\end{split} | |  |

The proof is complete.
∎

###### Lemma 4.11.

Let GG be as in Lemma [4.8](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem8 "Lemma 4.8. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"). There exists G¯:ℝ→ℝ\bar{G}:\mathbb{R}\to\mathbb{R}, and C>0C>0 such that the
following requirements are met: as x→−∞x\to-\infty we have

|  |  |  |
| --- | --- | --- |
|  | G¯​(x)→−∞,\bar{G}(x)\to-\infty, |  |

almost surely and, for all x∈ℝx\in\mathbb{R}, j∈ℝt−1j\in\mathbb{R}^{t-1} we have

|  |  |  |
| --- | --- | --- |
|  | G​(x,j)≤G¯​(x)≤CG(x,j)\leq\bar{G}(x)\leq C |  |

in the almost sure sense.

###### Proof.

Let GG and H∗H^{\*} be as in Lemma [4.8](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem8 "Lemma 4.8. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") and Lemma [4.10](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem10 "Lemma 4.10. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") respectively. Without loss of generality we
can assume t=2t=2. Let H∗H^{\*} be as in Lemma [4.10](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem10 "Lemma 4.10. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), and let us choose a sequence of rational-valued random variables Hn∗H\_{n}^{\*} increasing to it. Using the market bound for the innovations κ⋅\kappa\_{\cdot} in ([6](https://arxiv.org/html/2511.12093v1#S3.E6 "In 3 Preparation for the proof ‣ On the utility problem in a market where price impact is transient")), Assumption [4.3](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem3 "Assumption 4.3. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), and Fatous’ reverse Lemma, we have for x,j∈ℝx,j\in\mathbb{R} that

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(x,j)=\displaystyle G(x,j)= | L​(x,j,H∗)=limnL​(x,j,Hn∗)≤lim supnE​[V​(x,j,Hn∗)|ℋ]\displaystyle L(x,j,H^{\*})=\lim\_{n}L(x,j,H^{\*}\_{n})\leq\limsup\_{n}E[V(x,j,H\_{n}^{\*})|\mathcal{H}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤lim supnE​[G¯0​(x+κ2​(j,Hn∗))|ℋ]≤E​[G¯0​(x+κ2​(j,H∗))|ℋ]\displaystyle\leq\limsup\_{n}E[\bar{G}\_{0}(x+\kappa\_{2}(j,H^{\*}\_{n}))|\mathcal{H}]\leq E[\bar{G}\_{0}(x+\kappa\_{2}(j,H^{\*}))|\mathcal{H}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤E[G¯0(x+Pt2δt/4)|ℋ]=:G′(x)\displaystyle\leq E[\bar{G}\_{0}(x+P\_{t}^{2}\delta\_{t}/4)|\mathcal{H}]=:G^{{}^{\prime}}(x) |  |

almost surely.

Fix some v0∈ℝv\_{0}\in\mathbb{R} and note that we have G0​(x,v0)≤G¯0​(x)G\_{0}(x,v\_{0})\leq\bar{G}\_{0}(x). With Assumption [4.3](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem3 "Assumption 4.3. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") in mind,
take a continuous version of G′G^{{}^{\prime}} using Lemma [3.3](https://arxiv.org/html/2511.12093v1#S3.Thmtheorem3 "Lemma 3.3. ‣ 3 Preparation for the proof ‣ On the utility problem in a market where price impact is transient"), and denote it by G′′G^{{}^{\prime\prime}}. By construction for a.e. ω∈Ω\omega\in\Omega we have G​(⋅,⋅)≤CG(\cdot,\cdot)\leq C and G′′​(⋅)<CG^{{}^{\prime\prime}}(\cdot)<C, and observe that by the reverse Fatou lemma we have G′′​(x)→−∞G^{{}^{\prime\prime}}(x)\to-\infty and x→−∞x\to-\infty. The function G′′​(⋅)G^{{}^{\prime\prime}}(\cdot) inherits monotonicity from G¯0\bar{G}\_{0}. The former fact can be seen with similar reasoning given in the proof of Lemma [4.6](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem6 "Lemma 4.6. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"). The choice G¯=G′′\bar{G}=G^{{}^{\prime\prime}} completes the proof.
∎

###### Lemma 4.12.

Let GG be as in Lemma [4.8](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem8 "Lemma 4.8. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), and let t′∈{1,…,t−1}t^{{}^{\prime}}\in\{1,\ldots,t-1\}. For any m∈ℕm\in\mathbb{N} there exists an integrable random variable M1=M1​(m,t′)M\_{1}=M\_{1}(m,t^{{}^{\prime}}) so that

|  |  |  |
| --- | --- | --- |
|  | M1≤G​(x+κt′​((j1,…,jt′)),j)M\_{1}\leq G(x+\kappa\_{t^{{}^{\prime}}}((j\_{1},\ldots,j\_{t^{{}^{\prime}}})),j) |  |

for every x∈ℝx\in\mathbb{R}, j∈[−m,m]t−1j\in[-m,m]^{t-1}, and for almost every ω∈Ω\omega\in\Omega.

###### Proof.

Let m∈ℕm\in\mathbb{N} and t′∈{1,…,t−1}t^{{}^{\prime}}\in\{1,\ldots,t-1\}. Using Assumption [4.3](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem3 "Assumption 4.3. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") there exists and integrable, 𝒢\mathcal{G}-measurable M0=M0​(m,t′)M\_{0}=M\_{0}(m,t^{{}^{\prime}}) so that with with the notation (j,0)=(j1,…,jt−1,0)(j,0)=(j\_{1},\ldots,j\_{t-1},0) we have

|  |  |  |
| --- | --- | --- |
|  | G0​(x+κt′​((j1,…,jt′)),(j,0))≥M0\displaystyle G\_{0}(x+\kappa\_{t^{{}^{\prime}}}((j\_{1},\ldots,j\_{t^{{}^{\prime}}})),(j,0))\geq M\_{0} |  |

for all x∈[−m,m]x\in[-m,m], for all j∈[−m,m]t−1j\in[-m,m]^{t-1}, and for almost every ω∈Ω\omega\in\Omega. For fixed j=(j1,…,jt−1)∈[−m,m]t−1j=(j\_{1},\ldots,j\_{t-1})\in[-m,m]^{t-1} and x∈[−m,m]x\in[-m,m], we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G(x+κt′((j1,…,jt′)),j)≥L(x+κt′((j1,…,jt′)),j,0)=E​[V​(x+κt′​((j1,…,jt′)),j,0)|ℋ]=E​[G0​(x+κt′​((j1,…,jt′))+κt​((j,0)),(j,0))|ℋ]=E​[G0​(x+κt′​((j1,…,jt′)),(j,0))|ℋ]=E​[M0|ℋ]\displaystyle\begin{split}G(x+&\kappa\_{t^{{}^{\prime}}}((j\_{1},\ldots,j\_{t^{{}^{\prime}}})),j)\geq L(x+\kappa\_{t^{{}^{\prime}}}((j\_{1},\ldots,j\_{t^{{}^{\prime}}})),j,0)\\ &=E[V(x+\kappa\_{t^{{}^{\prime}}}((j\_{1},\ldots,j\_{t^{{}^{\prime}}})),j,0)|\mathcal{H}]\\ &=E[G\_{0}(x+\kappa\_{t^{{}^{\prime}}}((j\_{1},\ldots,j\_{t^{{}^{\prime}}}))+\kappa\_{t}((j,0)),(j,0))|\mathcal{H}]\\ &=E[G\_{0}(x+\kappa\_{t^{{}^{\prime}}}((j\_{1},\ldots,j\_{t^{{}^{\prime}}})),(j,0))|\mathcal{H}]=E[M\_{0}|\mathcal{H}]\end{split} | |  | (21) |

almost surely. Since GG is continuous the relation established in ([21](https://arxiv.org/html/2511.12093v1#S4.E21 "In 4 Single step case ‣ On the utility problem in a market where price impact is transient")) above holds for all x∈[−m,m]x\in[-m,m], for all j∈[−m,m]t−1j\in[-m,m]^{t-1}, and for almost every ω∈Ω\omega\in\Omega. The choice M1=E​[M0|ℋ]M\_{1}=E[M\_{0}|\mathcal{H}] gives a desired lower bound.

∎

## 5 The generic step, dynamic programming

First, in a phase of *bakcward induction* we construct actions that – depending parametrically on
previous decisions and accumulated wealth – are optimal in an instantaneous sense. These actions however would
only be optimal in one-step markets.

Then, we use these actions to build a strategy for the entire interval of trading, and this strategy
will serve as a *candidate strategy* for optimal trading.

Second, with a *forward iteration* we show that the *candidate* indeed represents a
series of actions that dominates all admissible executions in terms of expected utility: arriving to the conclusion of the paper.

Assumptions [2.1](https://arxiv.org/html/2511.12093v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2 Setup and results ‣ On the utility problem in a market where price impact is transient") and [2.3](https://arxiv.org/html/2511.12093v1#S2.Thmtheorem3 "Assumption 2.3. ‣ 2 Setup and results ‣ On the utility problem in a market where price impact is transient") will be in force from now on. Fix Cu≥0C\_{u}\geq 0 such that u​(x)≤Cuu(x)\leq C\_{u} for
all x∈ℝx\in\mathbb{R}. We denote with Ξt\Xi\_{t} the ℱt\mathcal{F}\_{t}-measurable random variables.

###### Proof of Theorem [2.4](https://arxiv.org/html/2511.12093v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2 Setup and results ‣ On the utility problem in a market where price impact is transient").

Define G~T:Ω×ℝ×ℝT→ℝ\tilde{G}\_{T}:\Omega\times\mathbb{R}\times\mathbb{R}^{T}\to\mathbb{R} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | G~T​(ω,x,h1,…,hT):=u​(x−B​(ω)),ω∈Ω,x,h1,…,hT∈ℝ.\tilde{G}\_{T}(\omega,x,h\_{1},\ldots,h\_{T}):=u(x-B(\omega)),\ \omega\in\Omega,\ x,h\_{1},\ldots,h\_{T}\in\mathbb{R}. |  | (22) |

Note that h1,…,hTh\_{1},\ldots,h\_{T} are dummy variables here, and G~T\tilde{G}\_{T} is continuous and nondecreasing in xx almost surely.

The first step of the *backward induction* is different from the other steps
since hT=−h1−…−hT−1h\_{T}=-h\_{1}-\ldots-h\_{T-1} due to the constraint on liquidation.
We thus consider G~T−1:Ω×ℝ×ℝT−1→ℝ\tilde{G}\_{T-1}:\Omega\times\mathbb{R}\times\mathbb{R}^{T-1}\to\mathbb{R} with the definition

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G~T−1​(ω,x,h1,…,hT−1)=E​[G~T​(x+κT​(h1,…,hT−1,−∑k=1T−1hk),h1,…,hT−1,−∑k=1T−1hk)|ℱT−1].\displaystyle\begin{split}&\tilde{G}\_{T-1}(\omega,x,h\_{1},\ldots,h\_{T-1})\\ &=E\left[\tilde{G}\_{T}\left(x+\kappa\_{T}\left(h\_{1},\ldots,h\_{T-1},-\sum\_{k=1}^{T-1}h\_{k}\right),h\_{1},\ldots,h\_{T-1},-\sum\_{k=1}^{T-1}h\_{k}\right)\left|\mathcal{F}\_{T-1}\right.\right].\end{split} | |  | (23) |

To start the *backward induction* one has to examine whether the conditions prescribed by Assumption [4.1](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem1 "Assumption 4.1. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"),
Assumption [4.2](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem2 "Assumption 4.2. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), and Assumption [4.3](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem3 "Assumption 4.3. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") hold with the choice G0=G~T−1G\_{0}=\tilde{G}\_{T-1}. To this end, we note that
the function G~T−1\tilde{G}\_{T-1} is jointly continuous in its real variables, it is non-decreasing in the first
real variable almost surely. Using the bound in ([6](https://arxiv.org/html/2511.12093v1#S3.E6 "In 3 Preparation for the proof ‣ On the utility problem in a market where price impact is transient")) we define G^T−1:Ω×ℝ→ℝ\hat{G}\_{T-1}:\Omega\times\mathbb{R}\to\mathbb{R} as

|  |  |  |
| --- | --- | --- |
|  | G^T−1​(ω,x)=E​[u​(x+PT2​(ω)​δT​(ω)4)|ℱT−1],\hat{G}\_{T-1}(\omega,x)=E\left[u\left(x+\frac{P\_{T}^{2}(\omega)\delta\_{T}(\omega)}{4}\right)|\mathcal{F}\_{T-1}\right], |  |

and we note that – due to Assumption [2.1](https://arxiv.org/html/2511.12093v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2 Setup and results ‣ On the utility problem in a market where price impact is transient") – for all
x∈ℝx\in\mathbb{R} it holds that G^T−1​(x)≤Cu\hat{G}\_{T-1}(x)\leq C\_{u}, and as x→−∞x\to-\infty the quantity G^T−1​(x)\hat{G}\_{T-1}(x) tends to
−∞-\infty as x→−∞x\to-\infty, in the ℙ\mathbb{P}-almost sure sense:
uu does so by assumption and due to boundedness from above the reverse Fatou Lemma is applicable.
Moreover, for all x,h1,…,hT−1x,h\_{1},\ldots,h\_{T-1}, we have

|  |  |  |
| --- | --- | --- |
|  | G~T−1​(ω,x,h1,…,hT−1)≤G^T−1​(ω,x)\tilde{G}\_{T-1}(\omega,x,h\_{1},\ldots,h\_{T-1})\leq\hat{G}\_{T-1}(\omega,x) |  |

almost surely, leading us to the choice G¯0=G^T−1\bar{G}\_{0}=\hat{G}\_{T-1} (again following notation of Section [4](https://arxiv.org/html/2511.12093v1#S4 "4 Single step case ‣ On the utility problem in a market where price impact is transient")).

We will establish the following claim after the present proof.

###### Claim 5.1.

For any m>0m>0 there exists
an ℱT−1\mathcal{F}\_{T-1}-measurable and integrable M=M​(m)M=M(m) such that for all 1≤t≤T−11\leq t\leq T-1 and for all
(x,h1,…,hT−1)∈[−m,m]T(x,h\_{1},\ldots,h\_{T-1})\in[-m,m]^{T}
we have

|  |  |  |
| --- | --- | --- |
|  | M​(m)≤GT−1​(x+κt​(h1,…,ht),h1,…,hT−1)M(m)\leq G\_{T-1}(x+\kappa\_{t}(h\_{1},\ldots,h\_{t}),h\_{1},\ldots,h\_{T-1}) |  |

almost surely.

One can thus conclude that Assumption [4.1](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem1 "Assumption 4.1. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), Assumption [4.2](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem2 "Assumption 4.2. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), and Assumption [4.3](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem3 "Assumption 4.3. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") of Section [4](https://arxiv.org/html/2511.12093v1#S4 "4 Single step case ‣ On the utility problem in a market where price impact is transient")
are satisfied and we are ready to perform the first step of the *backward induction*: the
lemmas of Section [4](https://arxiv.org/html/2511.12093v1#S4 "4 Single step case ‣ On the utility problem in a market where price impact is transient"), for the first step, will be utilized with the choice t=T−1t=T-1 and G0=G~T−1G\_{0}=\tilde{G}\_{T-1},
G¯0:=G^T−1\bar{G}\_{0}:=\hat{G}\_{T-1}.

Lemmas [4.4](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem4 "Lemma 4.4. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), [4.5](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem5 "Lemma 4.5. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), [4.6](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem6 "Lemma 4.6. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), [4.7](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"),
and [4.8](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem8 "Lemma 4.8. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") produce a mapping – denoted by GG in the their own context –
which, in our notation will take the form G~T−2:Ω×ℝT−1→ℝ\tilde{G}\_{T-2}:\Omega\times\mathbb{R}^{T-1}\to\mathbb{R} with the following properties.
The G~T−2\tilde{G}\_{T-2} is ℱT−2⊗ℬ​(ℝT−1)\mathcal{F}\_{T-2}\otimes\mathcal{B}(\mathbb{R}^{T-1})-measurable, non-decreasing in its first real variable,
jointly continuous in all its real variables, and for all x,h1,…,hT−2∈ℝx,h\_{1},\ldots,h\_{T-2}\in\mathbb{R} it almost surely satisfies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G~T−2​(x,h1,…,hT−2)=ess.supH∈ΞT−2​E​[G~T−1​(x+κT−1​(h1,…,hT−2,H),h1,…,hT−2,H)|ℱT−2].\displaystyle\begin{split}&\tilde{G}\_{T-2}(x,h\_{1},\ldots,h\_{T-2})\\ &=\mbox{ess.sup}\_{H\in\Xi\_{T-2}}E\left[\tilde{G}\_{T-1}(x+\kappa\_{T-1}(h\_{1},\ldots,h\_{T-2},H),h\_{1},\ldots,h\_{T-2},H)|\mathcal{F}\_{T-2}\right].\end{split} | |  | (24) |

Furthermore, Lemmas [4.9](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem9 "Lemma 4.9. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), and [4.10](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem10 "Lemma 4.10. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") ensure the existence of a mapping
HT−1∗:Ω×ℝT−1→ℝH^{\*}\_{T-1}:\Omega\times\mathbb{R}^{T-1}\to\mathbb{R} that is Ω⊗ℬ​(ℝT−1)\Omega\otimes\mathcal{B}(\mathbb{R}^{T-1})-measurable,
and is such that for all random variables X,H1,…,HT−2X,H\_{1},\ldots,H\_{T-2} that are measurable with respect to
ℱT−2\mathcal{F}\_{T-2}, with the notation HT−1∗=HT−1∗​(X,H1,…,HT−2)H^{\*}\_{T-1}=H^{\*}\_{T-1}(X,H\_{1},\ldots,H\_{T-2}), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G~T−2​(X,H1,…,HT−2)=E​[G~T−1​(X+κT−1​(H1,…,HT−2,HT−1∗),H1,…,HT−2,HT−1∗)|ℱT−1],\displaystyle\begin{split}&\tilde{G}\_{T-2}(X,H\_{1},\ldots,H\_{T-2})\\ &=E\left[\tilde{G}\_{T-1}(X+\kappa\_{T-1}(H\_{1},\ldots,H\_{T-2},H^{\*}\_{T-1}),H\_{1},\ldots,H\_{T-2},H^{\*}\_{T-1})|\mathcal{F}\_{T-1}\right],\end{split} | |  | (25) |

ℙ\mathbb{P}-almost surely.

Lemmas [4.11](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem11 "Lemma 4.11. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), and [4.12](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem12 "Lemma 4.12. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient") imply that there exists an action-independent bound
G^T−2\hat{G}\_{T-2}, with properties analogous to the G^T−1\hat{G}\_{T-1} presented above, and thus finally,
we arrive to the conclusion that the quantity G~T−2\tilde{G}\_{T-2} is such that it again satisfies
Assumption [4.1](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem1 "Assumption 4.1. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), Assumption [4.2](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem2 "Assumption 4.2. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"), and Assumption [4.3](https://arxiv.org/html/2511.12093v1#S4.Thmtheorem3 "Assumption 4.3. ‣ 4 Single step case ‣ On the utility problem in a market where price impact is transient"). That is, in
the next step of iteration, the choice G0=G~T−2G\_{0}=\tilde{G}\_{T-2}, G¯0:=G^T−2\bar{G}\_{0}:=\hat{G}\_{T-2} can be made.

Iterating backwards in this manner goes with the usual mechanics of induction. Take G~T−2\tilde{G}\_{T-2}
as a starting point.

When G~t′,…,G~T\tilde{G}\_{t^{{}^{\prime}}},\ldots,\tilde{G}\_{T}
(and Ht′−1∗,…,HT−1∗H^{\*}\_{t^{{}^{\prime}}-1},\ldots,H^{\*}\_{T-1}) are given for some t′≤T−2t^{{}^{\prime}}\leq T-2, applying the lemmas of Section
[4](https://arxiv.org/html/2511.12093v1#S4 "4 Single step case ‣ On the utility problem in a market where price impact is transient") with the choice G0=G~t′G\_{0}=\tilde{G}\_{t^{{}^{\prime}}}, G¯0:=G^t′\bar{G}\_{0}:=\hat{G}\_{t^{\prime}} and t=t′t=t^{{}^{\prime}}
yield G~t′−1\tilde{G}\_{t^{{}^{\prime}}-1}, and with this procedure we construct the pairs

|  |  |  |  |
| --- | --- | --- | --- |
|  | (HT−1∗,G~T−2),(HT−2∗,G~T−3),…,(H1∗,G~0)(H^{\*}\_{T-1},\tilde{G}\_{T-2}),(H^{\*}\_{T-2},\tilde{G}\_{T-3}),\ldots,(H^{\*}\_{1},\tilde{G}\_{0}) |  | (26) |

with the properties shown below.

For t∈{0,1,…,T−2}t\in\{0,1,\ldots,T-2\}, G~t:Ω×ℝt+1→ℝ\tilde{G}\_{t}:\Omega\times\mathbb{R}^{t+1}\to\mathbb{R} is
ℱt⊗ℬ​(ℝt+1)\mathcal{F}\_{t}\otimes\mathcal{B}(\mathbb{R}^{t+1})-measurable, non-decreasing in its first
real variable, jointly continuous in its real variables, and for all x,h1,…,ht∈ℝx,h\_{1},\ldots,h\_{t}\in\mathbb{R},
in the almost sure sense we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | G~t(x,h1,…,ht)=ess.supH∈Ξt​E​[G~t+1​(x+κt+1​(h1,…,ht,H),h1,…,ht,H)|ℱt].\displaystyle\begin{split}\tilde{G}\_{t}(x,h\_{1},&\ldots,h\_{t})\\ =&\mbox{ess.sup}\_{H\in\Xi\_{t}}E\left[\tilde{G}\_{t+1}(x+\kappa\_{t+1}(h\_{1},\ldots,h\_{t},H),h\_{1},\ldots,h\_{t},H)|\mathcal{F}\_{t}\right].\end{split} | |  |

The mapping Ht+1∗:Ω×ℝt→ℝH^{\*}\_{t+1}:\Omega\times\mathbb{R}^{t}\to\mathbb{R} is Ω⊗ℬ​(ℝt)\Omega\otimes\mathcal{B}(\mathbb{R}^{t})-measurable
and for all ℱt\mathcal{F}\_{t}-measurable random variables X,H1,…,HtX,H\_{1},\ldots,H\_{t} we have for
H~t+1∗=Ht+1∗​(X,H1,…,Ht)\tilde{H}^{\*}\_{t+1}=H^{\*}\_{t+1}(X,H\_{1},\ldots,H\_{t}) that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G~t(X,H1,…,Ht)=E​[G~t+1​(X+κt+1​(H1,…,Ht,H~t+1∗),H1,…,Ht,H~t+1∗)|ℱt],\displaystyle\begin{split}\tilde{G}\_{t}&(X,H\_{1},\ldots,H\_{t})\\ =&E\left[\tilde{G}\_{t+1}(X+\kappa\_{t+1}(H\_{1},\ldots,H\_{t},\tilde{H}^{\*}\_{t+1}),H\_{1},\ldots,H\_{t},\tilde{H}^{\*}\_{t+1})|\mathcal{F}\_{t}\right],\end{split} | |  | (27) |

holds in the ℙ\mathbb{P}-almost sure sense.

Introducing notation, for any admissible trading strategy H=(Ht)t∈{1,…,T}H=(H\_{t})\_{t\in\{1,\ldots,T\}}, we denote by
Γt​(H)\Gamma\_{t}(H) the strategy (Hs)s∈{1,…,t}(H\_{s})\_{s\in\{1,\ldots,t\}}, the same trading strategy as HH, but without liquidation,
and corresponding to the trading interval up to tt.

Now we construct the *candidate strategy* using the mapping in ([26](https://arxiv.org/html/2511.12093v1#S5.E26 "In 5 The generic step, dynamic programming ‣ On the utility problem in a market where price impact is transient")). Let H^1=H1∗​(z)\hat{H}\_{1}=H^{\*}\_{1}(z).
We define the optimal steps using a forward recursion. That is, when the H^t\hat{H}\_{t} is constructed for
some T−1≥t≥1T-1\geq t\geq 1, with accumulated wealth X^t=ξtΓt​(H^)\hat{X}\_{t}=\xi\_{t}^{\Gamma\_{t}(\hat{H})}, the
next action H^t+1\hat{H}\_{t+1} is given as

|  |  |  |  |
| --- | --- | --- | --- |
|  | H^t+1=Ht+1∗​(X^t,H^1,…,H^t).\hat{H}\_{t+1}=H^{\*}\_{t+1}(\hat{X}\_{t},\hat{H}\_{1},\ldots,\hat{H}\_{t}). |  | (28) |

Then, we set H^T=−H^T−1−…−H^1\hat{H}\_{T}=-\hat{H}\_{T-1}-\ldots-\hat{H}\_{1}.

We proceed with the *forward iteration*, giving an upper bound for all expected payoffs which –
as we shell see – equals the expected payoff associated with the *candidate strategy* H^\hat{H}.

Letting H1,…,HT−1,HTH\_{1},\ldots,H\_{T-1},H\_{T} denote an arbitrary series of admissible actions. Iterating with the rule in ([27](https://arxiv.org/html/2511.12093v1#S5.E27 "In 5 The generic step, dynamic programming ‣ On the utility problem in a market where price impact is transient")) yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | E​[u​(z+ξTH+B)]=E[E[u(z+ξT−1ΓT−1​(H)+κT(H1,…,HT−1,−∑k=1T−1Hk)+B)]|ℱT−1]]=E​[G~T−1​(z+ξT−2ΓT−2​(H)+κT−1​(H1,…,HT−1),H1,…,HT−1)]≤E​[E​[G~T−2​(z+ξT−3ΓT−3​(H)+κT−2​(H1,…,HT−2),H1,…,HT−2)|ℱT−2]]⋮≤E​[G~0​(z)].\displaystyle\begin{split}&E[u(z+\xi\_{T}^{H}+B)]\\ &=E[E[u(z+\xi\_{T-1}^{\Gamma\_{T-1}(H)}+\kappa\_{T}(H\_{1},\ldots,H\_{T-1},-\sum\_{k=1}^{T-1}H\_{k})+B)]|\mathcal{F}\_{T-1}]]\\ &=E[\tilde{G}\_{T-1}(z+\xi\_{T-2}^{\Gamma\_{T-2}(H)}+\kappa\_{T-1}(H\_{1},\ldots,H\_{T-1}),H\_{1},\ldots,H\_{T-1})]\\ &\leq E[E[\tilde{G}\_{T-2}(z+\xi\_{T-3}^{\Gamma\_{T-3}(H)}+\kappa\_{T-2}(H\_{1},\ldots,H\_{T-2}),H\_{1},\ldots,H\_{T-2})|\mathcal{F}\_{T-2}]]\\ &\vdots\\ &\phantom{}\leq E[\tilde{G}\_{0}(z)].\end{split} | |  | (29) |

Furthermore, as a result of ([22](https://arxiv.org/html/2511.12093v1#S5.E22 "In 5 The generic step, dynamic programming ‣ On the utility problem in a market where price impact is transient")), ([23](https://arxiv.org/html/2511.12093v1#S5.E23 "In 5 The generic step, dynamic programming ‣ On the utility problem in a market where price impact is transient")), ([24](https://arxiv.org/html/2511.12093v1#S5.E24 "In 5 The generic step, dynamic programming ‣ On the utility problem in a market where price impact is transient")), and ([25](https://arxiv.org/html/2511.12093v1#S5.E25 "In 5 The generic step, dynamic programming ‣ On the utility problem in a market where price impact is transient")) we have that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G~0​(z)=E​[G~1​(z+κ1​(H^1),H^1)]=E​[G~2​(z+κ1​(H^1)+κ2​(H^1,H^2),H^1,H^2)]⋮=E​[G~T−1​(z+∑i=1T−1κi​(H^1,…,H^i),H^1,…,H^T−1)]=E​[u​(z+ξTH^+B)].\displaystyle\begin{split}\tilde{G}\_{0}(z)=&E[\tilde{G}\_{1}(z+\kappa\_{1}(\hat{H}\_{1}),\hat{H}\_{1})]\\ =&E[\tilde{G}\_{2}(z+\kappa\_{1}(\hat{H}\_{1})+\kappa\_{2}(\hat{H}\_{1},\hat{H}\_{2}),\hat{H}\_{1},\hat{H}\_{2})]\\ \vdots&\\ =&E[\tilde{G}\_{T-1}(z+\sum\_{i=1}^{T-1}\kappa\_{i}(\hat{H}\_{1},\ldots,\hat{H}\_{i}),\hat{H}\_{1},\ldots,\hat{H}\_{T-1})]\\ =&E[u(z+\xi\_{T}^{\hat{H}}+B)].\end{split} | |  | (30) |

Thus, we can conclude, due to ([30](https://arxiv.org/html/2511.12093v1#S5.E30 "In 5 The generic step, dynamic programming ‣ On the utility problem in a market where price impact is transient")) and ([29](https://arxiv.org/html/2511.12093v1#S5.E29 "In 5 The generic step, dynamic programming ‣ On the utility problem in a market where price impact is transient")), that the candidate
strategy given with trading actions (H^t)t=1,…,T(\hat{H}\_{t})\_{t=1,\ldots,T}, defined in ([28](https://arxiv.org/html/2511.12093v1#S5.E28 "In 5 The generic step, dynamic programming ‣ On the utility problem in a market where price impact is transient")), is indeed optimal.
Theorem [2.4](https://arxiv.org/html/2511.12093v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2 Setup and results ‣ On the utility problem in a market where price impact is transient") is now shown.
∎

###### Proof of Claim [5.1](https://arxiv.org/html/2511.12093v1#S5.Thmtheorem1 "Claim 5.1. ‣ 5 The generic step, dynamic programming ‣ On the utility problem in a market where price impact is transient").

For h1,…,hT−1∈[−m,m]h\_{1},\ldots,h\_{T-1}\in[-m,m] we clearly have

|  |  |  |
| --- | --- | --- |
|  | κt​(h1,…,ht)≥−m​ζ0−t​m2/δ+min⁡{m​Pt,−m​Pt}.\kappa\_{t}(h\_{1},\ldots,h\_{t})\geq-m\zeta\_{0}-tm^{2}/\delta+\min\{mP\_{t},-mP\_{t}\}. |  |

Similarly,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  | κT​(h1,…,hT−1,−∑k=1T−1hk)\displaystyle\kappa\_{T}\left(h\_{1},\ldots,h\_{T-1},-\sum\_{k=1}^{T-1}h\_{k}\right) |  |
|  |  | ≥\displaystyle\geq | −(T−1)​m​ζ0−(T−1)​m2​(2​T−2)/δ+min⁡{m​(T−1)​PT,−m​(T−1)​PT}\displaystyle-(T-1)m\zeta\_{0}-(T-1)m^{2}(2T-2)/\delta+\min\{m(T-1)P\_{T},-m(T-1)P\_{T}\} |  |

Define the constant

|  |  |  |
| --- | --- | --- |
|  | Dm:=−(2​T−2)​ζ0−(T−1)​m2​(2​T−1)/δ.D\_{m}:=-(2T-2)\zeta\_{0}-(T-1)m^{2}(2T-1)/\delta. |  |

We can thus see that

|  |  |  |
| --- | --- | --- |
|  | G~T−1​(x+κt​(h1,…,ht),h1,…,hT−1)≥𝔼​[min⁡{J1,J2,J3,J4}|ℱT−1]\tilde{G}\_{T-1}(x+\kappa\_{t}(h\_{1},\ldots,h\_{t}),h\_{1},\ldots,h\_{T-1})\geq\mathbb{E}\left[{}\min\{J\_{1},J\_{2},J\_{3},J\_{4}\}\left|\mathcal{F}\_{T-1}\right.\right] |  |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J1\displaystyle J\_{1} | =\displaystyle= | u​(x+Dm+m​Pt+m​(T−1)​PT−B),\displaystyle u(x+D\_{m}+mP\_{t}+m(T-1)P\_{T}-B), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J2\displaystyle J\_{2} | =\displaystyle= | u​(x+Dm−m​Pt+m​(T−1)​PT−B),\displaystyle u(x+D\_{m}-mP\_{t}+m(T-1)P\_{T}-B), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J3\displaystyle J\_{3} | =\displaystyle= | u​(x+Dm+m​Pt−m​(T−1)​PT−B),\displaystyle u(x+D\_{m}+mP\_{t}-m(T-1)P\_{T}-B), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | J4\displaystyle J\_{4} | =\displaystyle= | u​(x+Dm−m​Pt−m​(T−1)​PT−B).\displaystyle u(x+D\_{m}-mP\_{t}-m(T-1)P\_{T}-B). |  |

Now ([3](https://arxiv.org/html/2511.12093v1#S2.E3 "In Assumption 2.1. ‣ 2 Setup and results ‣ On the utility problem in a market where price impact is transient")) implies our statement.
∎

## 6 Conclusion

One could add a solvency constraint (that is, z+ξtX≥0z+\xi^{X}\_{t}\geq 0 for all tt) with minimal modifications
in the arguments. Setting B:=0B:=0, utility maximization for uu defined on the positive real axis
could be treated in this way.

It is unclear whether (and how) results of the present paper could be transferred to continuous-time models.
We rely, in an essential way, on the fact that the treated portfolio optimization problem can be broken down into one-step
problems. In continuous time such an approach is out of question.

Acknowledgments. Both authors gratefully
acknowledge the support of
the National Research, Development and Innovation Office (NKFIH) through grant K 143529
and also within the framework of the Thematic Excellence Program 2021 (National Research subprogramme
“Artificial intelligence, large networks, data security: mathematical foundation and applications”).
The second author also thanks for the support of NKFIH grant KKP 137490.

## References

* [1]
   P. Bank and Y. Dolinsky.
  Continuous-time duality for super-replication with transient price impact.
  *Ann. Appl. Probab.*, 29:3893–3917, 2019.
* [2]
   P. Bank, Y. Dolinsky, M. Rásonyi.
  What if we knew what the future brings? Optimal investment for a frontrunner with price impact.
  *Appl. Math. Opt.*, vol. 86, paper no. 25, 1–24, 2022.
* [3]
   P. Bank and M. Voß.
  Optimal investment with transient price impact.
  *SIAM J. Finan. Math.*, 10:723–768, 2019.
* [4]
   L. Carassus and M. Rásonyi.
  Maximization of non-concave utility functions in
  discrete-time financial market models.
  *Math. Oper. Res.*, 41:146–173, 2016.
* [5]
   P. Guasoni and M. Rásonyi.
  Hedging, arbitrage and optimality under superlinear friction.
  *Ann. Appl. Probab.*, 25:2066–2095, 2015.
* [6]
   Yu. M. Kabanov and Ch. Stricker.
  A teacher’s note on no-arbitrage criteria.
  *In:
  Séminaire de Probabilités, vol. XXXV*, 149–152, Springer-Verlag, 2001.
* [7]

  J. Neveu
  Discrete parameter martingales.
  North-Holland, Amsterdam,1975.
* [8]
   M. Rásonyi and L. Stettner.
  On utility maximization
  in discrete-time market models.
  Ann. Appl. Probab., 15:1367–1395, 2005.