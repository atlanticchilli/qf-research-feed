---
authors:
- Alexey Meteykin
doc_id: arxiv:2512.20850v1
family_id: arxiv:2512.20850
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational
  Inequality in the Optimal Market-Making Problem with Alpha Signal
url_abs: http://arxiv.org/abs/2512.20850v1
url_html: https://arxiv.org/html/2512.20850v1
venue: arXiv q-fin
version: 1
year: 2025
---


Alexey Meteykin

Abstract: We address the problem of combined stochastic and impulse control for a market maker operating in a limit order book. The problem is formulated as a Hamilton–Jacobi–Bellman quasi-variational inequality (HJBQVI). We propose an implicit time-discretization scheme coupled with a policy iteration algorithm. This approach removes time-step restrictions typical of explicit methods and ensures unconditional stability. Convergence to the unique viscosity solution is established by verifying monotonicity, stability, and consistency conditions and applying the comparison principle.

Keywords: Hamilton–Jacobi–Bellman equation, combined stochastic and impulse control, implicit numerical scheme, policy iteration, viscosity solution.

## 1 Introduction

Optimal control problems play an important role in modern financial mathematics. One such problem is the optimal market making problem in a limit order book, which naturally arises in high-frequency trading on electronic exchanges.

A market maker, as a market participant, can submit two types of orders:

* •

  Limit order — an instruction to buy or sell an asset at a given or more favorable price. Such an order is posted to the limit order book and is executed when it matches an opposite market order.
* •

  Market order — an instruction to immediately buy or sell an asset at the best available price in the limit order book. Market orders enable rapid position adjustments but are executed at less favorable prices compared to limit orders.

The market maker provides liquidity to the market by placing limit buy and sell orders, and, when necessary, uses market orders to manage risk. The profit of the market maker arises from the spread between the buy and sell prices. The main source of risk is the potential loss in inventory value due to adverse price movements, known as inventory risk. To mitigate this risk, the market maker aims to maintain a near-zero inventory position.

Classical market making models, such as [[1](https://arxiv.org/html/2512.20850v1#bib.bib1)] and [[6](https://arxiv.org/html/2512.20850v1#bib.bib6)], assume that price dynamics contain no predictable components and that the market maker has no predictive information about future price movements. In [[5](https://arxiv.org/html/2512.20850v1#bib.bib5)], this classical setup is extended by introducing an alpha signal, a stochastic process representing the predictable component of price dynamics. This generalization allows for the possibility of extracting additional profit from predictable price trends.

In [[5](https://arxiv.org/html/2512.20850v1#bib.bib5)], the authors formulate the market making problem with an alpha signal, derived from the information contained in the flow of market orders, as a combined stochastic and impulse control problem. They show that the optimal market making strategy satisfies a Hamilton–Jacobi–Bellman Quasi-Variational Inequality (HJBQVI), which is solved numerically using an explicit time discretization scheme. However, the explicit scheme imposes natural restrictions on the time step due to stability constraints, which in turn increase the computational cost of the numerical solution.

In this paper, we propose an alternative numerical approach to solving the above HJBQVI. The main idea of the proposed method is to use an implicit time discretization scheme combined with a policy iteration algorithm. The implicit scheme is unconditionally stable and therefore eliminates restrictions on the time step size, while the policy iteration algorithm efficiently solves the discrete equation at each time step.

We establish convergence of the proposed implicit numerical scheme to the unique viscosity solution of the HJBQVI by applying the general framework developed in [[4](https://arxiv.org/html/2512.20850v1#bib.bib4)]. Specifically, we verify the conditions of monotonicity, stability, and consistency, as well as the validity of the comparison principle for the original equation. The convergence of the policy iteration algorithm is justified using the results of [[2](https://arxiv.org/html/2512.20850v1#bib.bib2)], which provide sufficient conditions for convergence in terms of diagonal dominance of the associated matrices and the connectivity properties of the graph induced by the impulse control component.

## 2 Model

Let (Ω,ℱ,𝐅,ℙ)(\Omega,{{\mathcal{F}}},\bf F,{\mathds{P}}) be a stochastic basis, where the filtration 𝐅={ℱt}t∈[0,T]{\bf F}=\{{\mathcal{F}}\_{t}\}\_{t\in[0,T]} is generated by the processes WW, M¯a\bar{M}^{\operatorname{a}}, and M¯b\bar{M}^{\operatorname{b}} introduced below. The market maker operates over the interval [0,T][0,T] with a fixed trading horizon T>0T>0.

The midprice in the order book is defined as the average of the best bid and best ask prices. Let the midprice S=(St)t≥0S=(S\_{t})\_{t\geq 0} of the asset evolve as

|  |  |  |
| --- | --- | --- |
|  | d​St=σ​(d​Jt↑−d​Jt↓),dS\_{t}=\sigma(dJ^{\uparrow}\_{t}-dJ^{\downarrow}\_{t}), |  |

where σ>0\sigma>0 denotes the minimum price increment (tick size) in the order book. Here J↑J^{\uparrow} and J↓J^{\downarrow} are doubly stochastic Poisson processes with intensities

|  |  |  |
| --- | --- | --- |
|  | μt↑=αt++θ​and​μt↓=αt−+θ,\mu^{\uparrow}\_{t}=\alpha\_{t}^{+}+\theta\qquad\text{and}\qquad\mu^{\downarrow}\_{t}=\alpha\_{t}^{-}+\theta, |  |

where θ>0\theta>0 is a constant and α=(αt)t≥0\alpha=(\alpha\_{t})\_{t\geq 0} is a process, referred to as the alpha signal and capturing information about the directional component of price dynamics, will be specified below.

The market maker may submit both limit and market orders, all having unit size.

The control for limit sell orders is an 𝐅{\bf F}-predictable process la=(lta)t∈[0,T]l^{\operatorname{a}}=(l\_{t}^{\operatorname{a}})\_{t\in[0,T]} with values in {0,1}\{0,1\}. A limit sell order is posted at time tt if lta=1l\_{t}^{\operatorname{a}}=1 and is not posted otherwise. Limit sell orders are placed at the best ask price St+ΔS\_{t}+\Delta, where Δ≥0\Delta\geq 0 represents half of the bid–ask spread. Analogously, the process lb=(ltb)t∈[0,T]l^{\operatorname{b}}=(l\_{t}^{\operatorname{b}})\_{t\in[0,T]} controls limit buy orders, which are placed at the best bid price St−ΔS\_{t}-\Delta.

Let Na=(Nta)t≥0N^{\text{a}}=(N^{\text{a}}\_{t})\_{t\geq 0} and Nb=(Ntb)t≥0N^{\text{b}}=(N^{\text{b}}\_{t})\_{t\geq 0} denote the counting processes for executed limit sell and buy orders of the market maker, respectively.

A limit sell (buy) order posted by the market maker is assumed to be executed with probability one whenever a market buy (sell) order arrives in the market.

The control governing market orders is specified by a double sequence

|  |  |  |
| --- | --- | --- |
|  | ζ=(τ1,τ2,…;z1,z2,…),\zeta=(\tau\_{1},\tau\_{2},\dotsc;z\_{1},z\_{2},\dotsc), |  |

where 0≤τ1≤τ2≤⋯0\leq\tau\_{1}\leq\tau\_{2}\leq\cdots are 𝐅{\bf F}-stopping times, and z1,z2,…∈{1,−1}z\_{1},z\_{2},\dotsc\in\{1,-1\} are impulses corresponding to these times. At time τi\tau\_{i}, the market maker submits a market buy order if zi=1z\_{i}=1, and a market sell order if zi=−1z\_{i}=-1. Market buy orders are executed at St+ΥS\_{t}+\Upsilon, and market sell orders at St−ΥS\_{t}-\Upsilon, where Υ=Δ+ε\Upsilon=\Delta+{\varepsilon} denotes the total cost of taking liquidity, with ε>0{\varepsilon}>0 being the market order fee. Let Ma=(Mta)t≥0M^{\operatorname{a}}=(M^{\operatorname{a}}\_{t})\_{t\geq 0} and Mb=(Mtb)t≥0M^{\operatorname{b}}=(M^{\operatorname{b}}\_{t})\_{t\geq 0} denote the counting processes for the market maker’s buy and sell market orders, respectively.

Other participants also submit market orders. Let M¯a=(M¯ta)t≥0\bar{M}^{\operatorname{a}}=(\bar{M}^{\operatorname{a}}\_{t})\_{t\geq 0} denote the Poisson process counting external market buy orders with intensity λa\lambda^{\operatorname{a}}, and M¯b=(M¯tb)t≥0\bar{M}^{\operatorname{b}}=(\bar{M}^{\operatorname{b}}\_{t})\_{t\geq 0} the Poisson process counting external market sell orders with intensity λb\lambda^{\operatorname{b}}.

The alpha signal α=(αt)t≥0\alpha=(\alpha\_{t})\_{t\geq 0} evolves as an Ornstein–Uhlenbeck process between jump times of the processes M¯ta,Mta,M¯tb,Mtb\bar{M}\_{t}^{\operatorname{a}},M\_{t}^{\operatorname{a}},\bar{M}\_{t}^{\operatorname{b}},M\_{t}^{\operatorname{b}}:

|  |  |  |
| --- | --- | --- |
|  | d​αt=−k​αt​d​t+ρ​d​Wt+γa​(d​M¯ta+d​Mta)−γb​(d​M¯tb+d​Mtb),α0=0,d\alpha\_{t}=-k\alpha\_{t}dt+\rho dW\_{t}+\gamma^{\operatorname{a}}(d\bar{M}\_{t}^{\operatorname{a}}+dM\_{t}^{\operatorname{a}})-\gamma^{\operatorname{b}}(d\bar{M}\_{t}^{\operatorname{b}}+dM\_{t}^{\operatorname{b}}),\qquad\alpha\_{0}=0, |  |

where W=(Wt)t≥0W=(W\_{t})\_{t\geq 0} is a Brownian motion, and k,ρ,γa,γb>0k,\rho,\gamma^{\operatorname{a}},\gamma^{\operatorname{b}}>0 are constants. Each market buy order arrival increases αt\alpha\_{t} by γa\gamma^{\operatorname{a}}, while each market sell order decreases it by γb\gamma^{\operatorname{b}}. Thus, the alpha signal reflects the imbalance between buy and sell market order flows.

We denote the market maker’s control by ν=(la,lb,ζ)\nu=(l^{\operatorname{a}},l^{\operatorname{b}},\zeta).

The controlled inventory process Qν=(Qtν)t≥0Q^{\nu}=(Q^{\nu}\_{t})\_{t\geq 0} is given by the relation

|  |  |  |
| --- | --- | --- |
|  | Qtν=Nb−Na+Mta−Mtb;Q^{\nu}\_{t}=N^{\text{b}}-N^{\text{a}}+M^{\text{a}}\_{t}-M^{\text{b}}\_{t}; |  |

the controlled cash process Xν=(Xtν)t≥0X^{\nu}=(X^{\nu}\_{t})\_{t\geq 0} evolves as

|  |  |  |
| --- | --- | --- |
|  | d​Xtν=(St+Δ)​d​Nta−(St−Δ)​d​Ntb−(St+Υ)​d​Mta+(St−Υ)​d​Mtb.dX^{\nu}\_{t}=(S\_{t}+\Delta)dN^{\text{a}}\_{t}-(S\_{t}-\Delta)dN^{\text{b}}\_{t}-(S\_{t}+\Upsilon)dM^{\text{a}}\_{t}+(S\_{t}-\Upsilon)dM^{\text{b}}\_{t}. |  |

The set of admissible controls 𝒜{\mathcal{A}} includes all ν=(la,lb,ζ)\nu=(l^{\operatorname{a}},l^{\operatorname{b}},\zeta) such that the inventory remains bounded, that is Qtν∈[−Q¯,Q¯]Q^{\nu}\_{t}\in[-\overline{Q},\overline{Q}] for all t∈[0,T]t\in[0,T] for some integer Q¯>0\overline{Q}>0, and the impulse control ζ\zeta does not trigger simultaneous buy and sell market orders.

We define the state process Yν={(Xtν,St,αt,Qtν)}t∈[0,T]Y^{\nu}=\big\{(X\_{t}^{\nu},S\_{t},\alpha\_{t},Q\_{t}^{\nu})\big\}\_{t\in[0,T]}, and use the shorthand y=(x,s,α,q)y=(x,s,\alpha,q). The performance is measured by the functional

|  |  |  |
| --- | --- | --- |
|  | Jν​(t,y)=𝔼t,y​[∫tTf​(r,Yrν)​𝑑r+g​(T,YTν)],\displaystyle J^{\nu}(t,y)={\mathbb{E}}^{t,y}\bigg[\int\_{t}^{T}f(r,Y\_{r}^{\nu})dr+g(T,Y\_{T}^{\nu})\bigg], |  |
|  |  |  |
| --- | --- | --- |
|  | f​(t,y)=−ϕ​q2,g​(t,y)=x+q​(s−Υ​signq)−ψ​q2,\displaystyle f(t,y)=-\phi q^{2},\qquad g(t,y)=x+q(s-\Upsilon\mathop{\text{sign}}q)-\psi q^{2}, |  |

where 𝔼t,y​[⋅]{\mathbb{E}}^{t,y}[\cdot] denotes conditional expectation given Xt−ν=xX^{\nu}\_{t\_{-}}=x, St−=sS\_{t\_{-}}=s, αt−ν=α\alpha^{\nu}\_{t\_{-}}=\alpha, Qt−ν=qQ^{\nu}\_{t\_{-}}=q, and ψ,ϕ>0\psi,\phi>0 are constants.

The running cost f​(t,y)=−ϕ​q2f(t,y)=-\phi q^{2} penalizes nonzero inventory levels, reflecting the exposure to adverse price movements. The terminal reward g​(t,y)g(t,y) represents the liquidation value at the terminal date, consisting of the current cash balance xx and the proceeds q​(s−Υ​signq)−ψ​q2q(s-\Upsilon\mathop{\text{sign}}q)-\psi q^{2} obtained upon liquidating the remaining position with a market order. The quadratic term −ψ​q2-\psi q^{2} accounts for additional costs due to insufficient liquidity at the best available quote in the order book.

The optimization problem is formulated as a combined stochastic and impulse maximization problem with the value function

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(t,y)=supν∈𝒜Jν​(t,y).u(t,y)=\sup\_{\nu\in{\mathcal{A}}}J^{\nu}(t,y). |  | (1) |

The dimension of the problem can be reduced to three variables by applying the substitution

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(t,x,s,α,q)=x+q​s+v​(t,α,q),u(t,x,s,\alpha,q)=x+qs+v(t,\alpha,q), |  | (2) |

where the value function u​(t,x,s,α,q)u(t,x,s,\alpha,q) decomposes into three components: the accumulated cash xx, the current mark-to-market value q​sqs of the inventory, and the residual function v​(t,α,q)v(t,\alpha,q) representing the expected additional profit generated on [t,T][t,T] under the optimal strategy.

As shown in [[5](https://arxiv.org/html/2512.20850v1#bib.bib5)], the value function ([1](https://arxiv.org/html/2512.20850v1#S2.E1 "In 2 Model ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")) is the unique viscosity solution to the corresponding Hamilton–Jacobi–Bellman Quasi-Variational Inequality (HJBQVI), which, under substitution ([2](https://arxiv.org/html/2512.20850v1#S2.E2 "In 2 Model ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")), takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | {max⁡(suplta,ltb∈{0,1}(∂v∂t+Lla,lb​v+f~la,lb),supz∈{1,−1}(ℳz​v−v))=0,t∈[0,T),v​(T,α,q)=g~​(T,α,q),\begin{cases}\max\Bigg(\sup\limits\_{l\_{t}^{\operatorname{a}},l\_{t}^{\operatorname{b}}\in\{0,1\}}\Big(\frac{\partial v}{\partial t}+L^{l^{\operatorname{a}},l^{\operatorname{b}}}v+\tilde{f}^{l^{\operatorname{a}},l^{\operatorname{b}}}\Big),\sup\limits\_{z\in\{1,-1\}}\Big({\mathcal{M}}^{z}v-v\Big)\Bigg)=0,&t\in[0,T),\\ v(T,\alpha,q\big)=\tilde{g}(T,\alpha,q\big),\end{cases} |  | (3) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lla,lb​v​(t,α,q)\displaystyle L^{l^{\operatorname{a}},l^{\operatorname{b}}}v(t,\alpha,q\big) | =−k​α​∂v∂α​(t,α,q)+12​ρ2​∂2v∂α2​(t,α,q)\displaystyle=-k\alpha\frac{\partial v}{\partial\alpha}(t,\alpha,q\big)+\frac{1}{2}\rho^{2}\frac{\partial^{2}v}{\partial\alpha^{2}}(t,\alpha,q\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λa​(𝟙{lta=0}​v​(t,α+γa,q)+𝟙{lta=1}​v​(t,α+γa,q−1)−v​(t,α,q))\displaystyle+\lambda^{\operatorname{a}}\bigg({\mathbb{1}}\_{\{l^{\operatorname{a}}\_{t}=0\}}v(t,\alpha+\gamma^{\operatorname{a}},q\big)+{\mathbb{1}}\_{\{l^{\operatorname{a}}\_{t}=1\}}v(t,\alpha+\gamma^{\operatorname{a}},q-1\big)-v(t,\alpha,q\big)\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λb​(𝟙{ltb=0}​v​(t,α−γb,q)+𝟙{ltb=1}​v​(t,α−γb,q+1)−v​(t,α,q)),\displaystyle+\lambda^{\operatorname{b}}\bigg({\mathbb{1}}\_{\{l^{\operatorname{b}}\_{t}=0\}}v(t,\alpha-\gamma^{\operatorname{b}},q\big)+{\mathbb{1}}\_{\{l^{\operatorname{b}}\_{t}=1\}}v(t,\alpha-\gamma^{\operatorname{b}},q+1\big)-v(t,\alpha,q\big)\bigg), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳz​v​(t,α,q)\displaystyle{\mathcal{M}}^{z}v(t,\alpha,q\big) | ={v​(t,α,q+1)−Υ,z=1,v​(t,α,q−1)−Υ,z=−1,\displaystyle=\begin{cases}v(t,\alpha,q+1\big)-\Upsilon,&z=1,\\ v(t,\alpha,q-1\big)-\Upsilon,&z=-1,\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | f~la,lb​(t,α,q)\displaystyle\tilde{f}^{l^{\operatorname{a}},l^{\operatorname{b}}}(t,\alpha,q\big) | =α​σ​q−ϕ​q2+𝟙{lta=1}​λa​Δ+𝟙{ltb=1}​λb​Δ,\displaystyle=\alpha\sigma q-\phi q^{2}+{\mathbb{1}}\_{\{l^{\operatorname{a}}\_{t}=1\}}\lambda^{\operatorname{a}}\Delta+{\mathbb{1}}\_{\{l^{\operatorname{b}}\_{t}=1\}}\lambda^{\operatorname{b}}\Delta, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | g~​(t,α,q)\displaystyle\tilde{g}(t,\alpha,q\big) | =−Υ​q​signq−ψ​q2.\displaystyle=-\Upsilon q\mathop{\text{sign}}q-\psi q^{2}. |  |

## 3 Numerical scheme

Let {tn}n=0N\{t\_{n}\}\_{n=0}^{N} be a uniform time grid with step size δ​t>0\delta t>0 on the interval [0,T][0,T], and let {αi}i=−NαNα\{\alpha\_{i}\}\_{i=-N\_{\alpha}}^{N\_{\alpha}} be a uniform grid with step size δ​α>0\delta\alpha>0 on [−A,A][-A,A] for some A>0A>0. The inventory variable qq takes values in the grid with unit spacing {qj}j=−NqNq=[−Q¯,Q¯]∩ℤ\{q\_{j}\}\_{j=-N\_{q}}^{N\_{q}}=[-\overline{Q},\overline{Q}]\cap\mathbb{Z}.

Since the shifted values α+γa\alpha+\gamma^{\operatorname{a}} and α−γb\alpha-\gamma^{\operatorname{b}} may not coincide with grid points in α\alpha, the value v​(t,α,q)v(t,\alpha,q) for α∈[−A,A]∖{αi}i=−NαNα\alpha\in[-A,A]\setminus\{\alpha\_{i}\}\_{i=-N\_{\alpha}}^{N\_{\alpha}} is linearly interpolated between the nearest grid points. For α>A\alpha>A, the value v​(t,α,q)v(t,\alpha,q) is linearly extrapolated using v​(t,A−δ​α,q)v(t,A-\delta\alpha,q) and v​(t,A,q)v(t,A,q), and analogously for α<−A\alpha<-A. In equation ([3](https://arxiv.org/html/2512.20850v1#S2.E3 "In 2 Model ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")), the process α\alpha is replaced with its truncated version

|  |  |  |
| --- | --- | --- |
|  | α¯t=min⁡{A,max⁡{−A,αt}}.\overline{\alpha}\_{t}=\min\{A,\max\{-A,\alpha\_{t}\}\}. |  |

The partial derivatives are approximated by finite differences as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂v∂t​(t,α,q)\displaystyle\frac{\partial v}{\partial t}(t,\alpha,q) | ∼v​(t+δ​t,α,q)−v​(t,α,q)δ​t,\displaystyle\sim\frac{v(t+\delta t,\alpha,q)-v(t,\alpha,q)}{\delta t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | −k​α​∂v∂α​(t,α,q)\displaystyle-k\alpha\frac{\partial v}{\partial\alpha}(t,\alpha,q) | ∼{−k​α​v​(t,α+δ​α,q)−v​(t,α,q)δ​α,α≤0,−k​α​v​(t,α,q)−v​(t,α−δ​α,q)δ​α,α≥0,\displaystyle\sim\begin{cases}-k\alpha\frac{v(t,\alpha+\delta\alpha,q)-v(t,\alpha,q)}{\delta\alpha},&\alpha\leq 0,\\ -k\alpha\frac{v(t,\alpha,q)-v(t,\alpha-\delta\alpha,q)}{\delta\alpha},&\alpha\geq 0,\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂2v∂α2​(t,α,q)\displaystyle\frac{\partial^{2}v}{\partial\alpha^{2}}(t,\alpha,q) | ∼v​(t,α+δ​α,q)−2​v​(t,α,q)+v​(t,α−δ​α,q)δ​α2.\displaystyle\sim\frac{v(t,\alpha+\delta\alpha,q)-2v(t,\alpha,q)+v(t,\alpha-\delta\alpha,q)}{\delta\alpha^{2}}. |  |

The boundary condition on the second derivative with respect to α\alpha is given by

|  |  |  |
| --- | --- | --- |
|  | ∂2v∂α2​(t,−A,q)=0​and​∂2v∂α2​(t,A,q)=0.\frac{\partial^{2}v}{\partial\alpha^{2}}(t,-A,q)=0\qquad\text{and}\qquad\frac{\partial^{2}v}{\partial\alpha^{2}}(t,A,q)=0. |  |

For convenience, denote lna=ltnal^{\operatorname{a}}\_{n}=l^{\operatorname{a}}\_{t\_{n}}, lnb=ltnbl^{\operatorname{b}}\_{n}=l^{\operatorname{b}}\_{t\_{n}}, vn=v​(tn,α,q)v^{n}=v(t\_{n},\alpha,q), and f~la,lb,n=f~la,lb​(tn,α,q)\tilde{f}^{l^{\operatorname{a}},l^{\operatorname{b}},n}=\tilde{f}^{l^{\operatorname{a}},l^{\operatorname{b}}}(t\_{n},\alpha,q).

The discrete form of the HJBQVI ([3](https://arxiv.org/html/2512.20850v1#S2.E3 "In 2 Model ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")) reads:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {max⁡(suplna,lnb∈{0,1}(vn+1−vnδ​t+Lδla,lb​vn+f~la,lb,n),supz∈{1,−1}(Bδz​vn−Υ))=0,n<N,v​(T,α,q)=g~​(T,α,q),\begin{cases}\max\Bigg(\sup\limits\_{l\_{n}^{\operatorname{a}},l\_{n}^{\operatorname{b}}\in\{0,1\}}\Big(\frac{v^{n+1}-v^{n}}{\delta t}+L\_{\delta}^{l^{\operatorname{a}},l^{\operatorname{b}}}v^{n}+\tilde{f}^{l^{\operatorname{a}},l^{\operatorname{b}},n}\Big),\sup\limits\_{z\in\{1,-1\}}\Big(B\_{\delta}^{z}v^{n}-\Upsilon\Big)\Bigg)=0,&n<N,\\ v(T,\alpha,q\big)=\tilde{g}(T,\alpha,q\big),\end{cases} |  | (4) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lδla,lb​v​(t,α,q)\displaystyle L\_{\delta}^{l^{\operatorname{a}},l^{\operatorname{b}}}v(t,\alpha,q) | =k​α¯−​v​(t,α+δ​α,q)−v​(t,α,q)δ​α−k​α¯+​v​(t,α,q)−v​(t,α−δ​α,q)δ​α\displaystyle=k\overline{\alpha}\_{-}\frac{v(t,\alpha+\delta\alpha,q)-v(t,\alpha,q)}{\delta\alpha}-k\overline{\alpha}\_{+}\frac{v(t,\alpha,q)-v(t,\alpha-\delta\alpha,q)}{\delta\alpha} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ρ22​v​(t,α+δ​α,q)−2​v​(t,α,q)+v​(t,α−δ​α,q)δ​α2\displaystyle+\frac{\rho^{2}}{2}\frac{v(t,\alpha+\delta\alpha,q)-2v(t,\alpha,q)+v(t,\alpha-\delta\alpha,q)}{\delta\alpha^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λa​(𝟙{lna=0}​ℐ+​v​(t,α,q)+𝟙{lna=1}​ℐ+​v​(t,α,q−1)−v​(t,α,q))\displaystyle+\lambda^{\operatorname{a}}\bigg({\mathbb{1}}\_{\{l^{\operatorname{a}}\_{n}=0\}}{\mathcal{I}}^{+}v(t,\alpha,q)+{\mathbb{1}}\_{\{l^{\operatorname{a}}\_{n}=1\}}{\mathcal{I}}^{+}v(t,\alpha,q-1)-v(t,\alpha,q)\bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +λb​(𝟙{lnb=0}​ℐ−​v​(t,α,q)+𝟙{lnb=1}​ℐ−​v​(t,α,q+1)−v​(t,α,q)),\displaystyle+\lambda^{\operatorname{b}}\bigg({\mathbb{1}}\_{\{l^{\operatorname{b}}\_{n}=0\}}{\mathcal{I}}^{-}v(t,\alpha,q)+{\mathbb{1}}\_{\{l^{\operatorname{b}}\_{n}=1\}}{\mathcal{I}}^{-}v(t,\alpha,q+1)-v(t,\alpha,q)\bigg), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Bδz​v​(t,α,q)\displaystyle B\_{\delta}^{z}v(t,\alpha,q) | ={v​(t,α,q+1)−v​(t,α,q),z=1,v​(t,α,q−1)−v​(t,α,q),z=−1.\displaystyle=\begin{cases}v(t,\alpha,q+1)-v(t,\alpha,q),&z=1,\\ v(t,\alpha,q-1)-v(t,\alpha,q),&z=-1.\end{cases} |  |

The operators ℐ+{\mathcal{I}}^{+} and ℐ−{\mathcal{I}}^{-} perform linear interpolation with respect to α\alpha:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ+​v​(t,α,q)=v​(t,α+⌊γaδ​α⌋​δ​α,q)+(γaδ​α−⌊γaδ​α⌋)​(v​(t,α+⌈γaδ​α⌉​δ​α,q)−v​(t,α+⌊γaδ​α⌋​δ​α,q)),\displaystyle\begin{split}{\mathcal{I}}^{+}v(t,\alpha,q)&=v\bigg(t,\alpha+\bigg\lfloor\frac{\gamma^{\operatorname{a}}}{\delta\alpha}\bigg\rfloor\delta\alpha,q\bigg)\\ &+\bigg(\frac{\gamma^{\operatorname{a}}}{\delta\alpha}-\bigg\lfloor\frac{\gamma^{\operatorname{a}}}{\delta\alpha}\bigg\rfloor\bigg)\Bigg(v\bigg(t,\alpha+\bigg\lceil\frac{\gamma^{\operatorname{a}}}{\delta\alpha}\bigg\rceil\delta\alpha,q\bigg)-v\bigg(t,\alpha+\bigg\lfloor\frac{\gamma^{\operatorname{a}}}{\delta\alpha}\bigg\rfloor\delta\alpha,q\bigg)\Bigg),\end{split} | |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℐ−​v​(t,α,q)=v​(t,α−⌊γbδ​α⌋​δ​α,q)+(γbδ​α−⌊γbδ​α⌋)​(v​(t,α−⌈γbδ​α⌉​δ​α,q)−v​(t,α−⌊γbδ​α⌋​δ​α,q)).\displaystyle\begin{split}{\mathcal{I}}^{-}v(t,\alpha,q)&=v\bigg(t,\alpha-\bigg\lfloor\frac{\gamma^{\operatorname{b}}}{\delta\alpha}\bigg\rfloor\delta\alpha,q\bigg)\\ &+\bigg(\frac{\gamma^{\operatorname{b}}}{\delta\alpha}-\bigg\lfloor\frac{\gamma^{\operatorname{b}}}{\delta\alpha}\bigg\rfloor\bigg)\Bigg(v\bigg(t,\alpha-\bigg\lceil\frac{\gamma^{\operatorname{b}}}{\delta\alpha}\bigg\rceil\delta\alpha,q\bigg)-v\bigg(t,\alpha-\bigg\lfloor\frac{\gamma^{\operatorname{b}}}{\delta\alpha}\bigg\rfloor\delta\alpha,q\bigg)\Bigg).\end{split} | |  |

## 4 Policy iteration

To solve the discrete equation ([4](https://arxiv.org/html/2512.20850v1#S3.E4 "In 3 Numerical scheme ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")), we use the policy iteration algorithm. This algorithm addresses problems of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | supP∈𝒫{−A​(P)​v+b​(P)}=0,\sup\_{P\in{\mathcal{P}}}\bigg\{-A(P)v+b(P)\bigg\}=0, |  | (5) |

where A​(P)A(P) is an M×MM\times M matrix, b​(P)b(P) and vv are vectors of length MM, and 𝒫{\mathcal{P}} denotes the set of admissible policies.

Algorithm 1  Policy Iteration

1:r>0r>0 — tolerance level

2:v0v^{0} — initial guess

3:for k=0,1,2,…k=0,1,2,\dots do

4:  Pk=arg​maxP∈𝒫⁡{−A​(P)​vk+b​(P)}P^{k}=\operatorname\*{arg\,max}\limits\_{P\in{\mathcal{P}}}\Big\{-A(P)v^{k}+b(P)\Big\}

5:  Solve the linear system A​(Pk)​vk+1=b​(Pk)A(P^{k})v^{k+1}=b(P^{k})

6:  if maxi⁡|vik+1−vikvik+1|<r\max\limits\_{i}\bigg|\dfrac{v^{k+1}\_{i}-v^{k}\_{i}}{v^{k+1}\_{i}}\bigg|<r then

7:   break

8:  end if

9:end for

The terminal condition v​(T,α,q)=g~​(T,α,q)v(T,\alpha,q)=\tilde{g}(T,\alpha,q) of equation ([4](https://arxiv.org/html/2512.20850v1#S3.E4 "In 3 Numerical scheme ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")) is specified at t=Tt=T. Proceeding backward in time, for each n∈{N−1,N−2,…,1}n\in\{N-1,N-2,\dots,1\}, the solution vnv^{n} is obtained by solving problem ([5](https://arxiv.org/html/2512.20850v1#S4.E5 "In 4 Policy iteration ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")) with the corresponding matrices A​(P)A(P) and vectors b​(P)b(P).

Fix n∈{N−1,N−2,…,1}n\in\{N-1,N-2,\dots,1\} and set M=(2​Nα+1)​(2​Nq+1)M=(2N\_{\alpha}+1)(2N\_{q}+1).

The set of admissible policies 𝒫{\mathcal{P}} in the present problem is given by

|  |  |  |
| --- | --- | --- |
|  | 𝒫=𝒲×𝒵×𝒟,{\mathcal{P}}={\mathcal{W}}\times{\mathcal{Z}}\times{\mathcal{D}}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | 𝒲⊂∏i=1M({0,1}×{0,1}),𝒵⊂∏i=1M{1,−1},𝒟=∏i=1M{0,1}.{\mathcal{W}}\subset\prod\_{i=1}^{M}\Big(\{0,1\}\times\{0,1\}\Big),\qquad{\mathcal{Z}}\subset\prod\_{i=1}^{M}\{1,-1\},\qquad{\mathcal{D}}=\prod\_{i=1}^{M}\{0,1\}. |  |

Therefore, a policy P=(w,z,d)∈𝒫P=(w,z,d)\in{\mathcal{P}} consists of three components. Namely, the vector w=(w1,…,wM)∈𝒲w=(w\_{1},\dots,w\_{M})\in{\mathcal{W}} corresponds to the stochastic control (lna,lnb)(l^{\operatorname{a}}\_{n},l^{\operatorname{b}}\_{n}) at each grid point, the vector z=(z1,…,zM)∈𝒵z=(z\_{1},\dots,z\_{M})\in{\mathcal{Z}} represents the impulses, and the components of the vector d=(d1,…,dM)∈𝒟d=(d\_{1},\dots,d\_{M})\in{\mathcal{D}} are indicators of impulse application. Let DD denote the diagonal matrix with d=(d1,…,dM)d=(d\_{1},\dots,d\_{M}) on the diagonal.

To express equation ([4](https://arxiv.org/html/2512.20850v1#S3.E4 "In 3 Numerical scheme ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")) in the form ([5](https://arxiv.org/html/2512.20850v1#S4.E5 "In 4 Policy iteration ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")), we write A​(P)A(P) and b​(P)b(P) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​(P)\displaystyle A(P) | =(I−D)​(I−L​(w))+D​(I−B​(z)),\displaystyle=\big(I-D\big)\Big(I-L(w)\Big)+D\Big(I-B(z)\Big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | b​(P)\displaystyle b(P) | =(I−D)​c​(w)+D​k​(z),\displaystyle=\big(I-D\big)c(w)+Dk(z), |  |

where

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | L​(w)\displaystyle L(w) | =Lδla,lb​δ​t,\displaystyle=L\_{\delta}^{l^{\operatorname{a}},l^{\operatorname{b}}}\delta t, | c​(w)\displaystyle c(w) | =vn+1+f~la,lb,n​δ​t,\displaystyle=v^{n+1}+\tilde{f}^{l^{\operatorname{a}},l^{\operatorname{b}},n}\delta t, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | B​(z)\displaystyle B(z) | =I+Bδz,\displaystyle=I+B\_{\delta}^{z}, | k​(z)\displaystyle k(z) | =−Υ.\displaystyle=-\Upsilon. |  |

To prove convergence of the policy iteration algorithm to the unique solution of equation ([4](https://arxiv.org/html/2512.20850v1#S3.E4 "In 3 Numerical scheme ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")), we use the theorem from [[2](https://arxiv.org/html/2512.20850v1#bib.bib2)]. For this purpose, several definitions are introduced below.

Let A=(ai​j)∈ℝM×MA=(a\_{ij})\in\mathbb{R}^{M\times M} be a real matrix.

###### Definition.

The graph of a matrix AA is a graph with vertices {1,…,M}\{1,\dots,M\}, where vertices ii and jj are connected by an edge if ai​j≠0a\_{ij}\neq 0.

###### Definition.

A matrix AA is a ZZ-matrix if ai​j≤0a\_{ij}\leq 0 for all i≠ji\neq j.

###### Definition.

A matrix AA is strictly (weakly) diagonally dominant if |ai​i|>∑j≠i|ai​j||a\_{ii}|>\sum\_{j\neq i}|a\_{ij}| (|ai​i|≥∑j≠i|ai​j||a\_{ii}|\geq\sum\_{j\neq i}|a\_{ij}|) for all ii.

###### Theorem 4.1 (Convergence of policy iteration).

Assume that the following conditions hold:

1. 1.

   P↦A​(P)−1P\mapsto A(P)^{-1} is bounded.
2. 2.

   AA and bb are bounded, and for every x∈ℝMx\in\mathbb{R}^{M} there exists a policy Px∈𝒫P\_{x}\in{\mathcal{P}} such that −A​(Px)​x+b​(Px)=supP∈𝒫{−A​(P)​x+b​(P)}-A(P\_{x})x+b(P\_{x})=\sup\_{P\in{\mathcal{P}}}\{-A(P)x+b(P)\}.
3. 3.

   For each P=(w,z,d)∈𝒫P=(w,z,d)\in{\mathcal{P}} and vertex ii with di=1d\_{i}=1, there exists a path in the graph of the matrix B​(z)B(z) from ii to a vertex jj with dj=0d\_{j}=0.
4. 4.

   For each P=(w,z,d)∈𝒫P=(w,z,d)\in{\mathcal{P}}, the matrices I−L​(w)I-L(w) and I−B​(z)I-B(z) are ZZ-matrices with nonnegative diagonal elements. The matrix I−L​(w)I-L(w) is strictly diagonally dominant, and the matrix I−B​(z)I-B(z) is weakly diagonally dominant.

Then the sequence (vk)k=0∞(v^{k})\_{k=0}^{\infty} produced by the policy iteration algorithm (Algorithm [1](https://arxiv.org/html/2512.20850v1#alg1 "Algorithm 1 ‣ 4 Policy iteration ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")) is nondecreasing and converges to the unique solution vv of problem ([5](https://arxiv.org/html/2512.20850v1#S4.E5 "In 4 Policy iteration ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")). Moreover, if 𝒫{\mathcal{P}} is finite, convergence occurs in at most |𝒫||{\mathcal{P}}| iterations (v|𝒫|=v|𝒫|+1=⋯v^{|{\mathcal{P}}|}=v^{|{\mathcal{P}}|+1}=\cdots).

In the context of the present problem, conditions (1) and (2) hold because the set of admissible policies 𝒫{\mathcal{P}} is finite.

To verify condition (3), note that by admissibility of the control, the inventory satisfies q∈[−Q¯,Q¯]q\in[-\overline{Q},\overline{Q}], and simultaneous buy and sell market orders are not allowed.

Consider a state i∈{1,…,M}i\in\{1,\dots,M\} in the graph of the matrix B​(z)B(z) such that di=1d\_{i}=1. Suppose zi=1z\_{i}=1, which corresponds to a market buy order. Then there is an edge between nodes ii and i+1i+1, and either di+1=0d\_{i+1}=0, in which case the required path is found, or di+1=1d\_{i+1}=1 and zi+1=1z\_{i+1}=1. As we move from ii to i+1i+1, the inventory qq increases by one. Repeating this argument, we eventually reach a vertex jj with dj=0d\_{j}=0, where q=Q¯q=\overline{Q} and a further increase in inventory is impossible.

The case zi=−1z\_{i}=-1, corresponding to a market sell order, is treated symmetrically.

To verify condition (4), we regroup the terms in the operator Lδla,lbL\_{\delta}^{l^{\operatorname{a}},l^{\operatorname{b}}}:

|  |  |  |
| --- | --- | --- |
|  | Lδla,lb=v​(t,α,q)​(−k​α¯−δ​α−k​α¯+δ​α−ρ2δ​α2−λa−λb)\displaystyle L\_{\delta}^{l^{\operatorname{a}},l^{\operatorname{b}}}=v(t,\alpha,q)\bigg(-\frac{k\overline{\alpha}\_{-}}{\delta\alpha}-\frac{k\overline{\alpha}\_{+}}{\delta\alpha}-\frac{\rho^{2}}{\delta\alpha^{2}}-\lambda^{\operatorname{a}}-\lambda^{\operatorname{b}}\bigg) |  |
|  |  |  |
| --- | --- | --- |
|  | +v​(t,α+δ​α,q)​(k​α¯−δ​α+ρ22​δ​α2)+v​(t,α−δ​α,q)​(k​α¯+δ​α+ρ22​δ​α2)\displaystyle+v(t,\alpha+\delta\alpha,q)\bigg(\frac{k\overline{\alpha}\_{-}}{\delta\alpha}+\frac{\rho^{2}}{2\delta\alpha^{2}}\bigg)+v(t,\alpha-\delta\alpha,q)\bigg(\frac{k\overline{\alpha}\_{+}}{\delta\alpha}+\frac{\rho^{2}}{2\delta\alpha^{2}}\bigg) |  |
|  |  |  |
| --- | --- | --- |
|  | +λa​(𝟙{lna=0}​ℐ+​v​(t,α,q)+𝟙{lna=1}​ℐ+​v​(t,α,q−1))\displaystyle+\lambda^{\operatorname{a}}\bigg({\mathbb{1}}\_{\{l^{\operatorname{a}}\_{n}=0\}}{\mathcal{I}}^{+}v(t,\alpha,q)+{\mathbb{1}}\_{\{l^{\operatorname{a}}\_{n}=1\}}{\mathcal{I}}^{+}v(t,\alpha,q-1)\bigg) |  |
|  |  |  |
| --- | --- | --- |
|  | +λb​(𝟙{lnb=0}​ℐ−​v​(t,α,q)+𝟙{lnb=1}​ℐ−​v​(t,α,q+1)).\displaystyle+\lambda^{\operatorname{b}}\bigg({\mathbb{1}}\_{\{l^{\operatorname{b}}\_{n}=0\}}{\mathcal{I}}^{-}v(t,\alpha,q)+{\mathbb{1}}\_{\{l^{\operatorname{b}}\_{n}=1\}}{\mathcal{I}}^{-}v(t,\alpha,q+1)\bigg). |  |

Hence, the diagonal entry of the matrix I−L​(w)I-L(w) has the form

|  |  |  |
| --- | --- | --- |
|  | 1+δ​t​(k​α¯−δ​α+k​α¯+δ​α+ρ2δ​α2+λa+λb)>0,1+\delta t\bigg(\frac{k\overline{\alpha}\_{-}}{\delta\alpha}+\frac{k\overline{\alpha}\_{+}}{\delta\alpha}+\frac{\rho^{2}}{\delta\alpha^{2}}+\lambda^{\operatorname{a}}+\lambda^{\operatorname{b}}\bigg)>0, |  |

and thus I−L​(w)I-L(w) is indeed a strictly diagonally dominant ZZ-matrix with nonnegative diagonal elements.

The matrix I−B​(z)I-B(z) also satisfies the required properties, since its rows are either zero or contain a diagonal element equal to one and one adjacent element equal to −1-1, with all other entries equal to zero.

Therefore, the sufficient conditions of Theorem [4.1](https://arxiv.org/html/2512.20850v1#S4.Thmtheorem1 "Theorem 4.1 (Convergence of policy iteration). ‣ 4 Policy iteration ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal") are satisfied, and the policy iteration algorithm numerically yields the unique solution vnv^{n} of equation ([4](https://arxiv.org/html/2512.20850v1#S3.E4 "In 3 Numerical scheme ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")) for each n∈{N−1,N−2,…,1}n\in\{N-1,N-2,\dots,1\}.

## 5 Convergence of the numerical scheme

To prove convergence of the solution of the discrete equation ([4](https://arxiv.org/html/2512.20850v1#S3.E4 "In 3 Numerical scheme ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")) to the viscosity solution of equation ([3](https://arxiv.org/html/2512.20850v1#S2.E3 "In 2 Model ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")), we employ the general framework for proving convergence of finite-difference approximations to viscosity solutions of partial differential equations, developed in [[4](https://arxiv.org/html/2512.20850v1#bib.bib4)].

We rewrite the numerical scheme ([4](https://arxiv.org/html/2512.20850v1#S3.E4 "In 3 Numerical scheme ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")) using the notation introduced in [[4](https://arxiv.org/html/2512.20850v1#bib.bib4), [3](https://arxiv.org/html/2512.20850v1#bib.bib3)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​(δ,x,vδ​(x),[vδ]x)=0,x∈Ω¯,S(\delta,x,v^{\delta}(x),[v^{\delta}]\_{x})=0,\qquad x\in\overline{\Omega}, |  | (6) |

where Ω¯=[0,T]×ℝ×([−Q¯,Q¯]∩ℤ)\overline{\Omega}=[0,T]\times\mathbb{R}\times([-\overline{Q},\overline{Q}]\cap\mathbb{Z}),
S:ℝ+×Ω¯×ℝ×Cb1,2​(Ω¯)→ℝS:\mathbb{R}^{+}\times\overline{\Omega}\times\mathbb{R}\times C^{1,2}\_{b}(\overline{\Omega})\rightarrow\mathbb{R},
δ=(δ​t,δ​α)\delta=(\delta t,\delta\alpha) is the grid step,
vδ:Ω¯→ℝv^{\delta}:\overline{\Omega}\rightarrow\mathbb{R} denotes the solution of ([6](https://arxiv.org/html/2512.20850v1#S5.E6 "In 5 Convergence of the numerical scheme ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")) and an approximation of vv,
and [vδ]x[v^{\delta}]\_{x} coincides with vδv^{\delta} at all points except xx,

|  |  |  |
| --- | --- | --- |
|  | [vδ]x​(x¯):={vδ​(x¯),x¯≠x,0,x¯=x.[v^{\delta}]\_{x}(\overline{x}):=\begin{cases}v^{\delta}(\overline{x}),&\overline{x}\neq x,\\ 0,&\overline{x}=x.\end{cases} |  |

###### Proposition 5.1 (Monotonicity).

Let u,w∈Cb1,2​(Ω¯)u,w\in C^{1,2}\_{b}\left(\overline{\Omega}\right) be such that u≥wu\geq w. Then, for all δ=(δ​t,δ​α)∈ℝ+×ℝ+\delta=(\delta t,\delta\alpha)\in\mathbb{R}^{+}\times\mathbb{R}^{+}, x∈Ω¯x\in\overline{\Omega}, and r∈ℝr\in\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | S​(δ,x,r,u)≥S​(δ,x,r,w).S(\delta,x,r,u)\geq S(\delta,x,r,w). |  |

###### Proof.

Consider a grid point xi​jn=(tn,αi,qj)x^{n}\_{ij}=(t\_{n},\alpha\_{i},q\_{j}).
Let u,w∈Cb1,2​(Ω¯)u,w\in C^{1,2}\_{b}(\overline{\Omega}) be such that u≥wu\geq w and ui​jn=wi​jn=ru^{n}\_{ij}=w^{n}\_{ij}=r, where ui​jn=u​(tn,αi,qj)u^{n}\_{ij}=u(t\_{n},\alpha\_{i},q\_{j}) and wi​jn=w​(tn,αi,qj)w^{n}\_{ij}=w(t\_{n},\alpha\_{i},q\_{j}).
Denote [u]i​jn:=[u]xi​jn[u]^{n}\_{ij}:=[u]\_{x^{n}\_{ij}}.
If tn=Tt\_{n}=T, then

|  |  |  |
| --- | --- | --- |
|  | S​(δ,xi​jn,ui​jn,[u]i​jn)−S​(δ,xi​jn,wi​jn,[w]i​jn)=g~​(T,αi,qj)−g~​(T,αi,qj)=0.S(\delta,x^{n}\_{ij},u^{n}\_{ij},[u]^{n}\_{ij})-S(\delta,x^{n}\_{ij},w^{n}\_{ij},[w]^{n}\_{ij})=\tilde{g}(T,\alpha\_{i},q\_{j})-\tilde{g}(T,\alpha\_{i},q\_{j})=0. |  |

If tn<Tt\_{n}<T, then

|  |  |  |
| --- | --- | --- |
|  | S​(δ,xi​jn,ui​jn,[u]i​jn)−S​(δ,xi​jn,wi​jn,[w]i​jn)=max⁡{suplna,lnb∈{0,1}(ui​jn+1−wi​jn+1δ​t+(Lδla,lb​(u−w)n)i​j),supz∈{1,−1}((Bδz​(u−w)n)i​j)}≥0,S(\delta,x^{n}\_{ij},u^{n}\_{ij},[u]^{n}\_{ij})-S(\delta,x^{n}\_{ij},w^{n}\_{ij},[w]^{n}\_{ij})\\ =\max\bigg\{\sup\limits\_{l\_{n}^{\operatorname{a}},l\_{n}^{\operatorname{b}}\in\{0,1\}}\bigg(\frac{u^{n+1}\_{ij}-w^{n+1}\_{ij}}{\delta t}+\big(L\_{\delta}^{l^{\operatorname{a}},l^{\operatorname{b}}}(u-w)^{n}\big)\_{ij}\bigg),\sup\limits\_{z\in\{1,-1\}}\Big(\big(B\_{\delta}^{z}(u-w)^{n}\big)\_{ij}\Big)\bigg\}\geq 0, |  |

because

|  |  |  |
| --- | --- | --- |
|  | (Lδla,lb​(u−w)n)i​j=(u​(tn,αi+δ​α,qj)−w​(tn,αi+δ​α,qj))​(k​α¯−δ​α+ρ22)\displaystyle\big(L\_{\delta}^{l^{\operatorname{a}},l^{\operatorname{b}}}(u-w)^{n}\big)\_{ij}=\Big(u(t\_{n},\alpha\_{i}+\delta\alpha,q\_{j})-w(t\_{n},\alpha\_{i}+\delta\alpha,q\_{j})\Big)\bigg(\frac{k\overline{\alpha}\_{-}}{\delta\alpha}+\frac{\rho^{2}}{2}\bigg) |  |
|  |  |  |
| --- | --- | --- |
|  | +(u​(tn,αi−δ​α,qj)−w​(tn,αi−δ​α,qj))​(k​α¯+δ​α+ρ22)\displaystyle+\Big(u(t\_{n},\alpha\_{i}-\delta\alpha,q\_{j})-w(t\_{n},\alpha\_{i}-\delta\alpha,q\_{j})\Big)\bigg(\frac{k\overline{\alpha}\_{+}}{\delta\alpha}+\frac{\rho^{2}}{2}\bigg) |  |
|  |  |  |
| --- | --- | --- |
|  | +λa​[𝟙{lta=0}​ℐ+​(u−w)​(tn,αi,qj)+𝟙{lta=1}​ℐ+​(u−w)​(tn,αi,qj−1)]\displaystyle+\lambda^{\operatorname{a}}\bigg[{\mathbb{1}}\_{\{l^{\operatorname{a}}\_{t}=0\}}{\mathcal{I}}^{+}(u-w)(t\_{n},\alpha\_{i},q\_{j})+{\mathbb{1}}\_{\{l^{\operatorname{a}}\_{t}=1\}}{\mathcal{I}}^{+}(u-w)(t\_{n},\alpha\_{i},q\_{j}-1)\bigg] |  |
|  |  |  |
| --- | --- | --- |
|  | +λb​[𝟙{ltb=0}​ℐ−​(u−w)​(tn,αi,qj)+𝟙{ltb=1}​ℐ−​(u−w)​(tn,αi,qj+1)]≥0.\displaystyle+\lambda^{\operatorname{b}}\bigg[{\mathbb{1}}\_{\{l^{\operatorname{b}}\_{t}=0\}}{\mathcal{I}}^{-}(u-w)(t\_{n},\alpha\_{i},q\_{j})+{\mathbb{1}}\_{\{l^{\operatorname{b}}\_{t}=1\}}{\mathcal{I}}^{-}(u-w)(t\_{n},\alpha\_{i},q\_{j}+1)\bigg]\geq 0. |  |

∎

###### Proposition 5.2 (Stability).

For any δ=(δ​t,δ​α)∈ℝ+×ℝ+\delta=(\delta t,\delta\alpha)\in\mathbb{R}^{+}\times\mathbb{R}^{+}, there exists a solution vδ​(t,α,q)v^{\delta}(t,\alpha,q) of equation ([6](https://arxiv.org/html/2512.20850v1#S5.E6 "In 5 Convergence of the numerical scheme ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")). Moreover, the following uniform bound holds:

|  |  |  |
| --- | --- | --- |
|  | U1​(t)≤vδ​(t,α,q)≤U2​(t),U\_{1}(t)\leq v^{\delta}(t,\alpha,q)\leq U\_{2}(t), |  |

where

|  |  |  |
| --- | --- | --- |
|  | U1​(t)=−Υ​Q¯−ψ​Q¯2−(T−t)​(σ​A​Q¯+ϕ​Q¯2),\displaystyle U\_{1}(t)=-\Upsilon\overline{Q}-\psi\overline{Q}^{2}-(T-t)(\sigma A\overline{Q}+\phi\overline{Q}^{2}), |  |
|  |  |  |
| --- | --- | --- |
|  | U2​(t)=(T−t)​(Δ​(λa+λb)+σ​A​Q¯).\displaystyle U\_{2}(t)=(T-t)(\Delta(\lambda^{\operatorname{a}}+\lambda^{\operatorname{b}})+\sigma A\overline{Q}). |  |

###### Proof.

Existence follows from Theorem [4.1](https://arxiv.org/html/2512.20850v1#S4.Thmtheorem1 "Theorem 4.1 (Convergence of policy iteration). ‣ 4 Policy iteration ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal").

Let tn<Tt\_{n}<T and select a grid point (αi,qj)(\alpha\_{i},q\_{j}) where at t=tnt=t\_{n} the value of vδv^{\delta} attains its minimum:

|  |  |  |
| --- | --- | --- |
|  | vi​jn=vδ​(tn,αi,qj)=mink,m⁡vδ​(tn,αk,qm).v^{n}\_{ij}=v^{\delta}(t\_{n},\alpha\_{i},q\_{j})=\min\_{k,m}v^{\delta}(t\_{n},\alpha\_{k},q\_{m}). |  |

Since (Lδla,lb​vn)i​j≥0\big(L\_{\delta}^{l^{\operatorname{a}},l^{\operatorname{b}}}v^{n}\big)\_{ij}\geq 0 for all lna,lnb∈{0,1}l^{\operatorname{a}}\_{n},l^{\operatorname{b}}\_{n}\in\{0,1\},

|  |  |  |
| --- | --- | --- |
|  | 0=max⁡{vi​jn+1−vi​jnδ​t+suplna,lnb∈{0,1}((Lδla,lb​vn)i​j+f~i​jla,lb,n),supz∈{1,−1}((Bδz​vn)i​j−Υ)}≥\displaystyle 0=\max\Bigg\{\frac{v\_{ij}^{n+1}-v\_{ij}^{n}}{\delta t}+\sup\limits\_{l\_{n}^{\operatorname{a}},l\_{n}^{\operatorname{b}}\in\{0,1\}}\Big(\big(L\_{\delta}^{l^{\operatorname{a}},l^{\operatorname{b}}}v^{n}\big)\_{ij}+\tilde{f}\_{ij}^{l^{\operatorname{a}},l^{\operatorname{b}},n}\Big),\sup\limits\_{z\in\{1,-1\}}\Big(\big(B\_{\delta}^{z}v^{n}\big)\_{ij}-\Upsilon\Big)\Bigg\}\geq |  |
|  |  |  |
| --- | --- | --- |
|  | ≥vi​jn+1−vi​jnδ​t−σ​A​Q¯−ϕ​Q¯2.\displaystyle\geq\frac{v\_{ij}^{n+1}-v\_{ij}^{n}}{\delta t}-\sigma A\overline{Q}-\phi\overline{Q}^{2}. |  |

Inductively in nn we obtain

|  |  |  |
| --- | --- | --- |
|  | vi​jn≥vi​jn+1−σ​A​Q¯−ϕ​Q¯2≥mink,m⁡vδ​(tn+1,αk,qm)−σ​A​Q¯−ϕ​Q¯2.\displaystyle v\_{ij}^{n}\geq v\_{ij}^{n+1}-\sigma A\overline{Q}-\phi\overline{Q}^{2}\geq\min\_{k,m}v^{\delta}(t\_{n+1},\alpha\_{k},q\_{m})-\sigma A\overline{Q}-\phi\overline{Q}^{2}. |  |

Since vδ​(T,α,q)=g~​(T,α,q)≥−Υ​Q¯−ψ​Q¯2v^{\delta}(T,\alpha,q)=\tilde{g}(T,\alpha,q)\geq-\Upsilon\overline{Q}-\psi\overline{Q}^{2}, we get the lower bound

|  |  |  |
| --- | --- | --- |
|  | vδ​(t,α,q)≥−Υ​Q¯−ψ​Q¯2−(T−t)​(σ​A​Q¯+ϕ​Q¯2)=U1​(t).v^{\delta}(t,\alpha,q)\geq-\Upsilon\overline{Q}-\psi\overline{Q}^{2}-(T-t)(\sigma A\overline{Q}+\phi\overline{Q}^{2})=U\_{1}(t). |  |

The lower bound corresponds to the case where the market maker holds the extreme position ±Q¯\pm\overline{Q} during the entire period [t,T][t,T], while the asset price follows a strong adverse trend, producing the largest running and terminal penalties.

Similarly, for the upper bound let tn<Tt\_{n}<T and take (αi,qj)(\alpha\_{i},q\_{j}) where vδ​(tn,αi,qj)v^{\delta}(t\_{n},\alpha\_{i},q\_{j}) attains its maximum:

|  |  |  |
| --- | --- | --- |
|  | vi​jn=vδ​(tn,αi,qj)=maxk,m⁡vδ​(tn,αk,qm).v^{n}\_{ij}=v^{\delta}(t\_{n},\alpha\_{i},q\_{j})=\max\_{k,m}v^{\delta}(t\_{n},\alpha\_{k},q\_{m}). |  |

Then (Lδla,lb​vn)i​j≤0\big(L\_{\delta}^{l^{\operatorname{a}},l^{\operatorname{b}}}v^{n}\big)\_{ij}\leq 0 for lna,lnb∈{0,1}l\_{n}^{\operatorname{a}},l\_{n}^{\operatorname{b}}\in\{0,1\}, and

|  |  |  |
| --- | --- | --- |
|  | (Bδz​vn)i​j−Υ≤−Υ<0​for all ​z∈{1,−1}.\big(B\_{\delta}^{z}v^{n}\big)\_{ij}-\Upsilon\leq-\Upsilon<0\qquad\text{for all }z\in\{1,-1\}. |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | 0=max⁡{vi​jn+1−vi​jnδ​t+suplna,lnb∈{0,1}((Lδla,lb​vn)i​j+f~i​jla,lb,n),supz∈{1,−1}((Bδz​vn)i​j−Υ)}\displaystyle 0=\max\Bigg\{\frac{v\_{ij}^{n+1}-v\_{ij}^{n}}{\delta t}+\sup\limits\_{l\_{n}^{\operatorname{a}},l\_{n}^{\operatorname{b}}\in\{0,1\}}\Big(\big(L\_{\delta}^{l^{\operatorname{a}},l^{\operatorname{b}}}v^{n}\big)\_{ij}+\tilde{f}\_{ij}^{l^{\operatorname{a}},l^{\operatorname{b}},n}\Big),\sup\limits\_{z\in\{1,-1\}}\Big(\big(B\_{\delta}^{z}v^{n}\big)\_{ij}-\Upsilon\Big)\Bigg\} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤vi​jn+1−vi​jnδ​t+Δ​(λa+λb)+σ​A​Q¯.\displaystyle\leq\frac{v\_{ij}^{n+1}-v\_{ij}^{n}}{\delta t}+\Delta(\lambda^{\operatorname{a}}+\lambda^{\operatorname{b}})+\sigma A\overline{Q}. |  |

This gives the induction step

|  |  |  |
| --- | --- | --- |
|  | vi​jn≤vi​jn+1+Δ​(λa+λb)+σ​A​Q¯≤maxk,m⁡vδ​(tn+1,αk,qm)+Δ​(λa+λb)+σ​A​Q¯.v\_{ij}^{n}\leq v\_{ij}^{n+1}+\Delta(\lambda^{\operatorname{a}}+\lambda^{\operatorname{b}})+\sigma A\overline{Q}\leq\max\_{k,m}v^{\delta}(t\_{n+1},\alpha\_{k},q\_{m})+\Delta(\lambda^{\operatorname{a}}+\lambda^{\operatorname{b}})+\sigma A\overline{Q}. |  |

Since vδ​(T,α,q)=g~​(T,α,q)≤0v^{\delta}(T,\alpha,q)=\tilde{g}(T,\alpha,q)\leq 0, we obtain the upper bound

|  |  |  |
| --- | --- | --- |
|  | vδ​(t,α,q)≤(T−t)​(Δ​(λa+λb)+σ​A​Q¯)=U2​(t).v^{\delta}(t,\alpha,q)\leq(T-t)(\Delta(\lambda^{\operatorname{a}}+\lambda^{\operatorname{b}})+\sigma A\overline{Q})=U\_{2}(t). |  |

The upper bound U2​(t)U\_{2}(t) can be interpreted as the accumulation of two maximum gains over [t,T][t,T]: from the spread and from exploiting predictable price movements.
∎

###### Proposition 5.3 (Consistency).

For all (t,α,q)∈Ω¯(t,\alpha,q)\in\overline{\Omega} and φ∈Cb1,2​(Ω¯)\varphi\in C^{1,2}\_{b}(\overline{\Omega}),

|  |  |  |
| --- | --- | --- |
|  | lim(δ​t,δ​α)→(0,0)(t′,α′)→(t,α)ξ→0S​((δ​t,δ​α),(t′,α′,q),φδ​(t′,α′,q)+ξ,[φδ+ξ](t′,α′,q))=max⁡(suplna,lnb∈{0,1}(∂φ∂t+Lla,lb​φ+f~la,lb),supz∈{1,−1}(ℳz​φ−φ)).\lim\_{\begin{subarray}{c}(\delta t,\delta\alpha)\to(0,0)\\ (t^{\prime},\alpha^{\prime})\to(t,\alpha)\\ \xi\to 0\end{subarray}}S\Big((\delta t,\delta\alpha),(t^{\prime},\alpha^{\prime},q),\varphi^{\delta}(t^{\prime},\alpha^{\prime},q)+\xi,[\varphi^{\delta}+\xi]\_{(t^{\prime},\alpha^{\prime},q)}\Big)\\ =\max\Bigg(\sup\limits\_{l\_{n}^{\operatorname{a}},l\_{n}^{\operatorname{b}}\in\{0,1\}}\bigg(\frac{\partial\varphi}{\partial t}+L^{l^{\operatorname{a}},l^{\operatorname{b}}}\varphi+\tilde{f}^{l^{\operatorname{a}},l^{\operatorname{b}}}\bigg),\sup\limits\_{z\in\{1,-1\}}\Big({\mathcal{M}}^{z}\varphi-\varphi\Big)\Bigg). |  |

###### Proof.

From the definition of the numerical scheme and the continuity of φ\varphi, we obtain

|  |  |  |
| --- | --- | --- |
|  | lim(δ​t,δ​α)→(0,0)(t′,α′)→(t,α)suplna,lnb∈{0,1}(φ​(t′+δ​t,α′,q)−φ​(t′,α′,q)δ​t+Lδla,lb​φ​(t′,α′,q)+f~la,lb​(t′,α′,q))\displaystyle\lim\_{\begin{subarray}{c}(\delta t,\delta\alpha)\to(0,0)\\ (t^{\prime},\alpha^{\prime})\to(t,\alpha)\end{subarray}}\sup\limits\_{l\_{n}^{\operatorname{a}},l\_{n}^{\operatorname{b}}\in\{0,1\}}\bigg(\frac{\varphi(t^{\prime}+\delta t,\alpha^{\prime},q)-\varphi(t^{\prime},\alpha^{\prime},q)}{\delta t}+L\_{\delta}^{l^{\operatorname{a}},l^{\operatorname{b}}}\varphi(t^{\prime},\alpha^{\prime},q)+\tilde{f}^{l^{\operatorname{a}},l^{\operatorname{b}}}(t^{\prime},\alpha^{\prime},q)\bigg) |  |
|  |  |  |
| --- | --- | --- |
|  | =suplna,lnb∈{0,1}(∂φ∂t​(t,α,q)+Lla,lb​φ​(t,α,q)+f~la,lb​(t,α,q)),\displaystyle=\sup\limits\_{l\_{n}^{\operatorname{a}},l\_{n}^{\operatorname{b}}\in\{0,1\}}\bigg(\frac{\partial\varphi}{\partial t}(t,\alpha,q)+L^{l^{\operatorname{a}},l^{\operatorname{b}}}\varphi(t,\alpha,q)+\tilde{f}^{l^{\operatorname{a}},l^{\operatorname{b}}}(t,\alpha,q)\bigg), |  |

and

|  |  |  |
| --- | --- | --- |
|  | lim(δ​t,δ​α)→(0,0)(t′,α′)→(t,α)supz∈{1,−1}(Bδz​φ​(t′,α′,q)−Υ)=supz∈{1,−1}(ℳz​φ​(t,α,q)−φ​(t,α,q)).\lim\_{\begin{subarray}{c}(\delta t,\delta\alpha)\to(0,0)\\ (t^{\prime},\alpha^{\prime})\to(t,\alpha)\end{subarray}}\sup\limits\_{z\in\{1,-1\}}\Big(B\_{\delta}^{z}\varphi(t^{\prime},\alpha^{\prime},q)-\Upsilon\Big)=\sup\limits\_{z\in\{1,-1\}}\Big({\mathcal{M}}^{z}\varphi(t,\alpha,q)-\varphi(t,\alpha,q)\Big). |  |

∎

We rely on the comparison principle from [[5](https://arxiv.org/html/2512.20850v1#bib.bib5), Theorem 2].

###### Theorem 5.1 (Comparison principle).

Let v1v\_{1} and v2v\_{2} be bounded subsolution and supersolution of equation ([3](https://arxiv.org/html/2512.20850v1#S2.E3 "In 2 Model ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")), respectively, and assume that v1​(T)≤v2​(T)v\_{1}(T)\leq v\_{2}(T). Then v1≤v2v\_{1}\leq v\_{2}.

###### Theorem 5.2 (Convergence).

As (δ​t,δ​α)→(0,0)(\delta t,\delta\alpha)\to(0,0), the solution vδ​(t,α,q)v^{\delta}(t,\alpha,q) of equation ([6](https://arxiv.org/html/2512.20850v1#S5.E6 "In 5 Convergence of the numerical scheme ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")) converges locally uniformly to the unique viscosity solution v​(t,α,q)v(t,\alpha,q) of equation ([3](https://arxiv.org/html/2512.20850v1#S2.E3 "In 2 Model ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")).

###### Proof.

For (t,α,q)∈Ω¯(t,\alpha,q)\in\overline{\Omega}, define

|  |  |  |
| --- | --- | --- |
|  | v¯​(t,α,q)=lim inf(δ​t,δ​α)→(0,0)(t′,α′)→(t,α)vδ​t,δ​α​(t′,α′,q),v¯​(t,α,q)=lim sup(δ​t,δ​α)→(0,0)(t′,α′)→(t,α)vδ​t,δ​α​(t′,α′,q).\underline{v}(t,\alpha,q)=\liminf\_{\begin{subarray}{c}(\delta t,\delta\alpha)\to(0,0)\\ (t^{\prime},\alpha^{\prime})\to(t,\alpha)\end{subarray}}v^{\delta t,\delta\alpha}(t^{\prime},\alpha^{\prime},q),\qquad\overline{v}(t,\alpha,q)=\limsup\_{\begin{subarray}{c}(\delta t,\delta\alpha)\to(0,0)\\ (t^{\prime},\alpha^{\prime})\to(t,\alpha)\end{subarray}}v^{\delta t,\delta\alpha}(t^{\prime},\alpha^{\prime},q). |  |

By definition, v¯≤v¯\underline{v}\leq\overline{v}. Moreover, v¯​(T,α,q)=v¯​(T,α,q)\underline{v}(T,\alpha,q)=\overline{v}(T,\alpha,q) for all α,q∈ℝ×([−Q¯,Q¯]∩ℤ)\alpha,q\in\mathbb{R}\times([-\overline{Q},\overline{Q}]\cap\mathbb{Z}).
The boundedness of these functions follows from the stability result (Proposition [5.2](https://arxiv.org/html/2512.20850v1#S5.Thmproposition2 "Proposition 5.2 (Stability). ‣ 5 Convergence of the numerical scheme ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")).
Hence, to establish the reverse inequality v¯≥v¯\underline{v}\geq\overline{v}, it suffices—by applying the comparison principle—to verify that v¯\underline{v} is a viscosity supersolution and that v¯\overline{v} is a viscosity subsolution.
We prove the first statement; the second follows by symmetry.

Let φ∈Cb1,2​(Ω¯)\varphi\in C\_{b}^{1,2}\big(\overline{\Omega}\big) and suppose that (t~,α~,q~)(\tilde{t},\tilde{\alpha},\tilde{q}) is a global minimum point of v¯−φ\underline{v}-\varphi.
Without loss of generality, assume that the minimum is strict and that v¯​(t~,α~,q~)=φ​(t~,α~,q~)\underline{v}(\tilde{t},\tilde{\alpha},\tilde{q})=\varphi(\tilde{t},\tilde{\alpha},\tilde{q}).

Then there exist sequences δk=(δ​tk,δ​αk)∈ℝ+×ℝ+\delta\_{k}=(\delta t\_{k},\delta\alpha\_{k})\in\mathbb{R}^{+}\times\mathbb{R}^{+} and (tk,αk,qk)∈Ω¯(t\_{k},\alpha\_{k},q\_{k})\in\overline{\Omega} such that, as k→∞k\to\infty,

|  |  |  |
| --- | --- | --- |
|  | (δ​tk,δ​αk)→(0,0),(tk,αk,qk)→(t~,α~,q~),vδk​(tk,αk,qk)→v¯​(t~,α~,q~),(\delta t\_{k},\delta\alpha\_{k})\to(0,0),\qquad(t\_{k},\alpha\_{k},q\_{k})\to(\tilde{t},\tilde{\alpha},\tilde{q}),\qquad v^{\delta\_{k}}(t\_{k},\alpha\_{k},q\_{k})\to\underline{v}(\tilde{t},\tilde{\alpha},\tilde{q}), |  |

and vδk−φv^{\delta\_{k}}-\varphi attains a global minimum at (tk,αk,qk)(t\_{k},\alpha\_{k},q\_{k}).

Let ξk=vδk​(tk,αk,qk)−φ​(tk,αk,qk)\xi\_{k}=v^{\delta\_{k}}(t\_{k},\alpha\_{k},q\_{k})-\varphi(t\_{k},\alpha\_{k},q\_{k}).
Then vδk​(t,α,q)≥φ​(t,α,q)+ξkv^{\delta\_{k}}(t,\alpha,q)\geq\varphi(t,\alpha,q)+\xi\_{k} for all points (t,α,q)∈Ω¯(t,\alpha,q)\in\overline{\Omega}, with ξk→0\xi\_{k}\to 0 as k→∞k\to\infty.

By monotonicity (Proposition [5.1](https://arxiv.org/html/2512.20850v1#S5.Thmproposition1 "Proposition 5.1 (Monotonicity). ‣ 5 Convergence of the numerical scheme ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")) of the scheme SS, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =\displaystyle= | S​(δk,(tk,αk,qk),vδk​(tk,αk,qk),[vδk](tk,αk,qk))\displaystyle S\Big(\delta\_{k},(t\_{k},\alpha\_{k},q\_{k}),v^{\delta\_{k}}(t\_{k},\alpha\_{k},q\_{k}),[v^{\delta\_{k}}]\_{(t\_{k},\alpha\_{k},q\_{k})}\Big) |  |
|  |  | ≥\displaystyle\geq | S​(δk,(tk,αk,qk),vδk​(tk,αk,qk),[φ+ξk](tk,αk,qk))\displaystyle S\Big(\delta\_{k},(t\_{k},\alpha\_{k},q\_{k}),v^{\delta\_{k}}(t\_{k},\alpha\_{k},q\_{k}),[\varphi+\xi\_{k}]\_{(t\_{k},\alpha\_{k},q\_{k})}\Big) |  |
|  |  | =\displaystyle= | S​(δk,(tk,αk,qk),φ​(tk,αk,qk)+ξk,[φ+ξk](tk,αk,qk)).\displaystyle S\Big(\delta\_{k},(t\_{k},\alpha\_{k},q\_{k}),\varphi(t\_{k},\alpha\_{k},q\_{k})+\xi\_{k},[\varphi+\xi\_{k}]\_{(t\_{k},\alpha\_{k},q\_{k})}\Big). |  |

Thus,

|  |  |  |
| --- | --- | --- |
|  | S​(δk,(tk,αk,qk),φ​(tk,αk,qk)+ξk,[φ+ξk](tk,αk,qk))≤0.S\Big(\delta\_{k},(t\_{k},\alpha\_{k},q\_{k}),\varphi(t\_{k},\alpha\_{k},q\_{k})+\xi\_{k},[\varphi+\xi\_{k}]\_{(t\_{k},\alpha\_{k},q\_{k})}\Big)\leq 0. |  |

Applying the consistency property (Proposition [5.3](https://arxiv.org/html/2512.20850v1#S5.Thmproposition3 "Proposition 5.3 (Consistency). ‣ 5 Convergence of the numerical scheme ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")) and taking the limit as k→∞k\to\infty, we obtain

|  |  |  |
| --- | --- | --- |
|  | max⁡(suplna,lnb∈{0,1}(∂φ∂t+Lla,lb​φ+f~la,lb),supz∈{1,−1}(ℳz​φ−φ))≤0.\max\Bigg(\sup\limits\_{l\_{n}^{\operatorname{a}},l\_{n}^{\operatorname{b}}\in\{0,1\}}\bigg(\frac{\partial\varphi}{\partial t}+L^{l^{\operatorname{a}},l^{\operatorname{b}}}\varphi+\tilde{f}^{l^{\operatorname{a}},l^{\operatorname{b}}}\bigg),\sup\limits\_{z\in\{1,-1\}}\Big({\mathcal{M}}^{z}\varphi-\varphi\Big)\Bigg)\leq 0. |  |

Therefore, v¯\underline{v} is a viscosity supersolution and v¯\overline{v} is a viscosity subsolution.
By the comparison principle and the definitions of v¯\underline{v} and v¯\overline{v}, it follows that v¯≡v¯\underline{v}\equiv\overline{v}, and this common function is the unique viscosity solution of equation ([3](https://arxiv.org/html/2512.20850v1#S2.E3 "In 2 Model ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal")).
∎

## 6 Numerical experiment

We solve the Hamilton–Jacobi–Bellman Quasi-Variational Inequality numerically with the following parameter values:

|  |  |  |
| --- | --- | --- |
|  | T=10,A=300,Q¯=4,σ=0.01,θ=0.1,\displaystyle T=10,\ A=300,\ \overline{Q}=4,\ \sigma=0.01,\ \theta=0.1, |  |
|  |  |  |
| --- | --- | --- |
|  | Δ=0.005,ε=0.005,λa=λb=1,k=200,\displaystyle\Delta=0.005,\ {\varepsilon}=0.005,\ \lambda^{\operatorname{a}}=\lambda^{\operatorname{b}}=1,\ k=200, |  |
|  |  |  |
| --- | --- | --- |
|  | ρ=1,γa=γb=60,ϕ=10−6,ψ=0.\displaystyle\rho=1,\ \gamma^{\operatorname{a}}=\gamma^{\operatorname{b}}=60,\ \phi=10^{-6},\ \psi=0. |  |

Let the uniform grid in α\alpha consist of Nα=101N\_{\alpha}=101 points, and let the uniform time grid contain N=200N=200 points.

![Refer to caption](value_function.png)


Figure 1: Surface of the value function vv at time t=0t=0.

![Refer to caption](optimal_control.png)


Figure 2: Optimal control at time t=0t=0.

Figure [2](https://arxiv.org/html/2512.20850v1#S6.F2 "Figure 2 ‣ 6 Numerical experiment ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal") shows the computed surface of the value function vv at the initial time.
The corresponding optimal control is displayed in Figure [2](https://arxiv.org/html/2512.20850v1#S6.F2 "Figure 2 ‣ 6 Numerical experiment ‣ Implicit Numerical Scheme for the Hamilton–Jacobi–Bellman Quasi-Variational Inequality in the Optimal Market-Making Problem with Alpha Signal").
From these results it can be observed that when the alpha signal is close to zero, the market maker quotes both bid and ask limit orders.
As the alpha signal increases (or decreases), the market maker begins to trade only on the buy (or sell) side.
For large values of the alpha signal, the market maker uses both limit and market orders to exploit predictable price movements efficiently.

## 7 Conclusion

This work investigates an implicit numerical method for solving the Hamilton–Jacobi–Bellman Quasi-Variational Inequality arising in combined stochastic and impulse control problem for a market maker.
The proposed approach avoids time-step restrictions due to its unconditional stability.

We established the convergence of the policy iteration algorithm to the solution of the discrete scheme at each time step.
Furthermore, the convergence of the implicit numerical solution to the unique viscosity solution of the Hamilton–Jacobi–Bellman Quasi-Variational Inequality was proved.
To this end, we verified the monotonicity, stability, and consistency properties of the numerical scheme.

A numerical experiment was conducted, and the results illustrate the shape of the value function and the structure of the optimal control at the initial time.

## Acknowledgements

The author is thankful to Yuri Kabanov for the attention to his work.

## References

* [1]

  Avellaneda, M. and Stoikov, S. 2008. High Frequency Trading in a Limit Order Book. Quantitative Finance 8:217–224. doi: 10.1080/14697680701381228.
* [2]

  Azimzadeh, P. and Forsyth, P. A. 2016. Weakly Chained Matrices, Policy Iteration, and Impulse Control. SIAM Journal on Numerical Analysis 54(3):1341–
  1364. doi: 10.1137/15M1043431.
* [3]

  Barles, G. and Jakobsen, E. R. 2002. On the convergence rate of approximation schemes for Hamilton-Jacobi-Bellman Equations. ESAIM: M2AN 36(1):33–54. doi: 10.1051/m2an:2002002.
* [4]

  G. Barles and P.E. Souganidis. 1991. Convergence of approximation schemes for fully nonlinear second order equations. Asymptotic Analysis 4(3):271–283.
  doi: 10.3233/ASY-1991-4305.
* [5]

  Cartea, Á. and Wang, Y. 2020. Market making with alpha signals. International Journal of Theoretical and Applied Finance 23(03):2050016. doi: 10.1142/S0219024920500168.
* [6]

  Guйant, O. and Lehalle, C.-A. and Fernandez-Tapia, J. 2011. Dealing with the Inventory Risk: A Solution to the Market Making Problem. Mathematics and Financial Economics 7. doi: 10.1007/s11579-012-0087-0.