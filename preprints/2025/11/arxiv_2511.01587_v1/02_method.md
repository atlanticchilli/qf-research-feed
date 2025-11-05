---
authors:
- Mustapha Regragui
- Karel J. in 't Hout
- Michèle Vanmaele
- Fred Espen Benth
doc_id: arxiv:2511.01587v1
family_id: arxiv:2511.01587
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Numerical methods for solving PIDEs arising in swing option pricing under a
  two-factor mean-reverting model with jumps
url_abs: http://arxiv.org/abs/2511.01587v1
url_html: https://arxiv.org/html/2511.01587v1
venue: arXiv q-fin
version: 1
year: 2025
---


Mustapha Regragui, 
Karel J. in ’t Hout, 
Michèle Vanmaele, 
Fred Espen Benth
Department of Mathematics, Computer Science and Statistics, Ghent University, 9000 Ghent, Belgium. Email: mustapha.regragui@ugent.beDepartment of Mathematics, University of Antwerp, Middelheimlaan 1, 2020 Antwerp, Belgium. Email: karel.inthout@uantwerpen.beDepartment of Mathematics, Computer Science and Statistics, Ghent University, 9000 Ghent, Belgium. Email: michele.vanmaele@ugent.beDepartment of Data Science and Analytics, BI Norwegian Business School, N-0484 Oslo, Norway. Email: fred.e.benth@bi.no

###### Abstract

This paper concerns the numerical valuation of swing options with discrete action times under a linear two-factor mean-reverting model with jumps. The resulting sequence of two-dimensional partial integro-differential equations (PIDEs) are convection-dominated and possess a nonlocal integral term due to the presence of jumps. Further, the initial function is nonsmooth. We propose various second-order numerical methods that can adequately handle these challenging features. The stability and convergence of these numerical methods are analysed theoretically. By ample numerical experiments, we confirm their second-order convergence behaviour.

## 1 Introduction

Electricity is traded through several types of financial derivatives contracts, such as forwards, futures, swaps and swing options. This paper deals with the valuation of swing options. This type of contract gives the holder the right to buy electricity multiple times at a fixed price under some constraints, for example the holder cannot buy more than a certain amount of energy during the entire life time of the option and also during each exercise period of the option.

In the literature, there are different formalisations of swing options. In Kjaer ([2008](https://arxiv.org/html/2511.01587v1#bib.bib19)), the contract is seen as a multi-exercise Bermudan option where the holder can exercise at multiple, predetermined dates and the option price is the solution of a sequence of parabolic partial integro-differential equations. In Dahlgren ([2005](https://arxiv.org/html/2511.01587v1#bib.bib7)), the contract is formalised as a multi-exercise American option, where the holder can exercise at any time as long as a certain waiting time between two successive exercise times is respected, and the option valuation is about solving partial integro-differential complementarity problems. Next, the contract can be formalised such that the holder can exercise in continuous time, see Benth et al. ([2011](https://arxiv.org/html/2511.01587v1#bib.bib3)), Eriksson et al. ([2014](https://arxiv.org/html/2511.01587v1#bib.bib10)), which leads to the study of a Hamilton–Jacobi–Bellman (HJB) type equation. In this paper, we will focus on the formalisation where we have a finite number of fixed, predetermined exercise dates.

There are several ways of pricing swing options. Lattice-based methods, see Jaillet et al. ([2004](https://arxiv.org/html/2511.01587v1#bib.bib17)), and Monte Carlo type simulations, see Ibáñez ([2004](https://arxiv.org/html/2511.01587v1#bib.bib14)), have been used. Also, considering an expansion of the density of the underlying price process in terms of convenient basis functions, several methods have been derived for this kind of options, see Zhang and Oosterlee ([2013](https://arxiv.org/html/2511.01587v1#bib.bib27)), Kirkby and Deng ([2019](https://arxiv.org/html/2511.01587v1#bib.bib18)). Another approach, which forms the focus of this work, is to solve a sequence of parabolic partial integro-differential equations (PIDEs) as in, e.g., Kjaer ([2008](https://arxiv.org/html/2511.01587v1#bib.bib19)) and Calvo-Garrido et al. ([2016](https://arxiv.org/html/2511.01587v1#bib.bib4), [2019](https://arxiv.org/html/2511.01587v1#bib.bib5)). One of the advantages of using a PIDE approach is that one can compute the option price for a whole set of spot prices at once, while Monte Carlo and lattice-based methods can only provide the option price for one spot price.

The electricity price possesses a mean reversion property with spikes and (daily, weekly and annually) seasonal patterns. One of the first models for this price was proposed by Lucia and Schwartz ([2002](https://arxiv.org/html/2511.01587v1#bib.bib21)) in the form of a geometric Ornstein–Uhlenbeck process which has a mean-reverting property. However, this model has the disadvantage of not incorporating spikes. In Benth et al. ([2007](https://arxiv.org/html/2511.01587v1#bib.bib2)), the electricity spot price is modelled as a linear combination of an Ornstein–Uhlenbeck process and pure mean-reverting jump processes. Hambly et al. ([2009](https://arxiv.org/html/2511.01587v1#bib.bib12)) considered an exponential form of this model. In this paper, we follow the approach of Eriksson et al. ([2014](https://arxiv.org/html/2511.01587v1#bib.bib10)) and consider an affine two-factor model with finite activity jumps. The choice of an affine model is motivated by the fact that the electricity market exhibits negative prices, especially in the recent years.

Under the affine two-factor spot model, the pertinent two-dimensional PIDEs are convection-dominated in the first direction and have pure convection and a nonlocal integral part in the second direction.
For its numerical solution, the method of lines is employed, consisting of a discretisation in space followed by a discretisation in time. When the PIDEs are discretised in the spatial domain by finite difference schemes, this results in a large semidiscrete system of ordinary differential equations (ODEs). This system of ODEs is subsequently discretised in the temporal domain using a time-stepping scheme of the operator splitting kind, where the partial differential part is treated implicitly and the integral part is treated explicitly.

The first contribution of this paper is the design and analysis of efficient and robust numerical methods that adequately address two key challenges: (i) the handling of the convection-dominated nature of the problem combined with the nonsmooth initial function, and (ii) the treatment of the nonlocal integral term.

To handle the convection-dominated feature together with the nonsmooth payoff function, we consider two approaches. The first approach is to apply the semi-Lagrangian method. The second approach is to discretise the convection term by carefully chosen finite difference schemes. It is well-known that classical second-order central schemes can lead to spurious oscillatory behaviour. Accordingly, in this paper, we shall explore and compare various second-order upwind schemes, notably the QUICK scheme.

For the integral term, we consider a second-order spatial discretisation. Next, we present two temporal discretisation schemes that handle the integral part explicitly through a fixed-point iteration.

The second contribution of this paper is a theoretical analysis of the stability and convergence of the proposed numerical methods.

The third contribution of this paper consists of ample numerical experiments to assess the robustness and accuracy and study the order of convergence of the proposed numerical methods.

This paper is organised in the following way. Section [2](https://arxiv.org/html/2511.01587v1#S2 "2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") presents the electricity spot price model under consideration and the formulation of the option pricing problem as a sequence of two-dimensional PIDEs. Section [3](https://arxiv.org/html/2511.01587v1#S3 "3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") concerns the spatial discretisation with special attention for the convection and integral parts.
Section [4](https://arxiv.org/html/2511.01587v1#S4 "4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") presents the temporal discretisation schemes. These schemes are all second-order and treat the integral term in an explicit way by means of a fixed-point iteration. Section [5](https://arxiv.org/html/2511.01587v1#S5 "5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") is devoted to the theoretical analysis of the stability and convergence properties of the schemes. In Section [6](https://arxiv.org/html/2511.01587v1#S6 "6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"), we present ample numerical experiments, especially to study the observed order of convergence.
Finally, Section 7 gives our conclusions.

## 2 Swing option price modelling

### 2.1 The electricity spot price

Let (Ω,ℱ,(ℱt)t,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t},\mathbb{P}) be a complete filtered probability space satisfying the usual conditions, with ℙ\mathbb{P} the historical or real world probability measure. We assume that there exists an equivalent pricing measure ℚ∼ℙ\mathbb{Q}\sim\mathbb{P}.

As in Eriksson et al. ([2014](https://arxiv.org/html/2511.01587v1#bib.bib10)) we consider the following linear two-factor model for the electricity spot price, SS, adapted to the filtration (ℱt)t(\mathcal{F}\_{t})\_{t} but with dynamics modelled directly under ℚ\mathbb{Q}111We could have started, as, e.g., in Kjaer ([2008](https://arxiv.org/html/2511.01587v1#bib.bib19)), with the ℙ\mathbb{P}-dynamics and then considered a measure change to get the corresponding ℚ\mathbb{Q}-dynamics. But as we are interested in the numerical valuation of derivatives we work directly under the measure ℚ\mathbb{Q}.:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | St\displaystyle S\_{t} | =Xt+Yt,\displaystyle=X\_{t}+Y\_{t}, |  | (2.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Xt\displaystyle dX\_{t} | =α​(μ−Xt)​d​t+σ​d​Wt,\displaystyle=\alpha(\mu-X\_{t})dt+\sigma dW\_{t}, |  | (2.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Yt\displaystyle dY\_{t} | =−β​Yt​d​t+Jt​d​Nλ,t.\displaystyle=-\beta Y\_{t}dt+J\_{t}dN\_{\lambda,t}. |  | (2.3) |

XX is an Ornstein–Uhlenbeck process with mean reversion level μ\mu and mean
reversion speed α\alpha which depicts the mean reversion property of the electricity
price, WW represents a standard Brownian motion. To incorporate the spikes in
the prices, YY is a mean-reverting process with a jump component where
NλN\_{\lambda} is a Poisson process with constant intensity λ\lambda and JJ
is the jump size process. The jump size distribution is given by a bounded density function
ff. We assume JJ, NλN\_{\lambda} and WW to be mutually independent. The mean
reversion speeds α\alpha and β\beta and the volatility σ\sigma are positive constants, while the mean reversion
level μ\mu can be either a constant or a time-dependent periodic deterministic
function characterising the seasonality of the energy price. For ease of presentation, we will assume in this paper that μ\mu is constant.

The electricity spot price could be modelled in exponential form, i.e., St=exp⁡(Xt+Yt)S\_{t}=\exp(X\_{t}+Y\_{t}), see, e.g., Hambly et al. ([2009](https://arxiv.org/html/2511.01587v1#bib.bib12)), Calvo-Garrido et al. ([2016](https://arxiv.org/html/2511.01587v1#bib.bib4), [2019](https://arxiv.org/html/2511.01587v1#bib.bib5)). However, we
prefer the affine form, i.e., St=Xt+YtS\_{t}=X\_{t}+Y\_{t}, which allows the price to
become negative.
The occurrence of negative prices was observed in the day-ahead market and
it is generally due to oversupply combined with low demand, inflexible power
stations (e.g., nuclear reactors) and cheap renewable power. A study by the
Belgian Federal Commission for Electricity and Gas Regulation (CREG), see Tirez et al. ([2023](https://arxiv.org/html/2511.01587v1#bib.bib24)), indicated
that, in 2020, the cumulative number of hours with negative prices reached 136 hours in Belgium, 102 hours in France,
319 hours in Germany and 97 hours in the Netherlands.

### 2.2 Formulation of the problem

We consider a Bermudan swing option with a predetermined finite number NaN\_{a} of discrete action times (c.f., Kjaer ([2008](https://arxiv.org/html/2511.01587v1#bib.bib19))).

We assume that the swing option has the following properties:

1. 1.

   The fixed strike price is KK and the maturity time is TT.
2. 2.

   Swing action times are in the form Tn=n​Δ​TT\_{n}=n\Delta T (n=1,…,Nan=1,\ldots,N\_{a}) with Δ​T=TNa\Delta T=\frac{T}{N\_{a}}.
3. 3.

   (Local constraint) At each swing action time, the holder has the
   right to buy at most LL units of energy for
   the price KK.
4. 4.

   (Volume constraint) The total amount of units bought should not exceed
   a predetermined global upper bound MM over the lifetime [0,T][0,T] of the
   option.

We model the option value as a solution to an optimal stochastic control problem with multiple stopping times.
  
Let 𝒜Na\mathcal{A}^{N\_{a}} be a class of *admissible strategies* consisting of all 𝔽\mathbb{F}-adapted processes (ut)0≤t≤T∈L2​(Ω×[0,T])(u\_{t})\_{0\leq t\leq T}\in L^{2}(\Omega\times[0,T]) that admit the representation

|  |  |  |
| --- | --- | --- |
|  | ut=∑n=1Na−1an​1[Tn,Tn+1[​(t)+aNa​δt,TNa,u\_{t}=\sum\_{n=1}^{N\_{a}-1}a\_{n}1\_{[T\_{n},T\_{n+1}[}(t)+a\_{N\_{a}}\delta\_{t,T\_{N\_{a}}}, |  |

where δ\delta denotes the Kronecker symbol, and the ℱTn\mathcal{F}\_{T\_{n}}-measurable random variables ana\_{n}, n=1,…,Nan=1,\ldots,N\_{a}, represent the number of units bought at action time TnT\_{n} satisfying the constraints an∈{0,1,…,L}a\_{n}\in\{0,1,\ldots,L\} and

|  |  |  |
| --- | --- | --- |
|  | ∑n=1NauTn=∑n=1Naan≤M.\sum\_{n=1}^{N\_{a}}u\_{T\_{n}}=\sum\_{n=1}^{N\_{a}}a\_{n}\leq M. |  |

Denote by ZZ the process of the amount
ZtZ\_{t} of energy bought up to time tt (where time tt is not included).
The option value function at a swing action time TiT\_{i}, i∈{1,…,Na}i\in\{1,\ldots,N\_{a}\}, can be expressed as the conditional expected
present value of the payoff given a control process u∈𝒜Nau\in\mathcal{A}^{N\_{a}} from the swing action time TiT\_{i} up to maturity time TT, and given
that the two factors XX and YY and the amount of energy ZZ at the swing
action time TiT\_{i} have values xx, yy and zz respectively:

|  |  |  |
| --- | --- | --- |
|  | v​(x,y,z,Ti)=supu∈𝒜Na𝔼ℚ​[∑n=iNae−r​(Tn−Ti)​(XTn+YTn−K)​uTn∣XTi=x,YTi=y,ZTi=z],v(x,y,z,T\_{i})=\sup\_{u\in\mathcal{A}^{N\_{a}}}\mathbb{E}\_{\mathbb{Q}}\big[\,\sum\_{n=i}^{N\_{a}}e^{-r(T\_{n}-T\_{i})}(X\_{T\_{n}}+Y\_{T\_{n}}-K)u\_{T\_{n}}\mid X\_{T\_{i}}=x,Y\_{T\_{i}}=y,Z\_{T\_{i}}=z\,\big], |  |

where rr is the risk-free interest rate.
At T0=0T\_{0}=0, the amount of purchased energy is zero. Then, the option value can also be expressed as:

|  |  |  |
| --- | --- | --- |
|  | v​(x,y,0,0)=supu∈𝒜Na𝔼ℚ​[∑n=1Nae−r​(Tn−T0)​(XTn+YTn−K)​uTn∣XT0=x,YT0=y,ZT0=0].v(x,y,0,0)=\sup\_{u\in\mathcal{A}^{N\_{a}}}\mathbb{E}\_{\mathbb{Q}}\big[\,\sum\_{n=1}^{N\_{a}}e^{-r(T\_{n}-T\_{0})}(X\_{T\_{n}}+Y\_{T\_{n}}-K)u\_{T\_{n}}\mid X\_{T\_{0}}=x,Y\_{T\_{0}}=y,Z\_{T\_{0}}=0\,\big]. |  |

Using the dynamic programming principle together with the Feynman–Kac theorem as in, e.g., Kjaer ([2008](https://arxiv.org/html/2511.01587v1#bib.bib19)), the option value function satisfies a sequence of PIDEs coupled with conditions at the exercise dates:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∂tv​(x,y,z,t)+σ22​∂x​xv​(x,y,z,t)+α​(μ−x)​∂xv​(x,y,z,t)−β​y​∂yv​(x,y,z,t)−(r+λ)​v​(x,y,z,t)+λ​∫ℝv​(x,y+ξ,z,t)​f​(ξ)​𝑑ξ=0,Ti−1<t<Ti,v​(x,y,z,Ti)=supu∈𝒜Na∑n=iNae−r​(Tn−Ti)​𝔼ℚ​[(XTn+YTn−K)​uTn∣XTi=x,YTi=y,ZTi=z],\begin{cases}\displaystyle\partial\_{t}v(x,y,z,t)+\frac{\sigma^{2}}{2}\partial\_{xx}v(x,y,z,t)+\alpha(\mu-x)\partial\_{x}v(x,y,z,t)-\beta y\partial\_{y}v(x,y,z,t)-(r+\lambda)v(x,y,z,t)\\[8.53581pt] \displaystyle\qquad\qquad\qquad\qquad\qquad+\lambda\int\_{\mathbb{R}}v(x,y+\xi,z,t)f(\xi)d\xi=0,\qquad T\_{i-1}<t<T\_{i},\\[8.53581pt] \displaystyle v(x,y,z,T\_{i})=\sup\_{u\in\mathcal{A}^{N\_{a}}}\sum\_{n=i}^{N\_{a}}e^{-r(T\_{n}-T\_{i})}\mathbb{E}\_{\mathbb{Q}}\big[(X\_{T\_{n}}+Y\_{T\_{n}}-K)u\_{T\_{n}}\mid X\_{T\_{i}}=x,Y\_{T\_{i}}=y,Z\_{T\_{i}}=z\big],\\ \end{cases} |  | (2.4) |

for i∈{1,…,Na}i\in\{1,\ldots,N\_{a}\} and (x,y,z)∈ℝ×ℝ×{0,1,…,M}(x,y,z)\in\mathbb{R}\times\mathbb{R}\times\{0,1,\ldots,M\}.

Between any two successive swing action times Ti−1T\_{i-1} and TiT\_{i}, the option value
function is the solution of a parabolic PIDE with a terminal condition at
time TiT\_{i}. As this PIDE is the same in each interval ]Ti−1,Ti[]T\_{i-1},T\_{i}[, we start our numerical solution approach for ([2.4](https://arxiv.org/html/2511.01587v1#S2.E4 "In 2.2 Formulation of the problem ‣ 2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) by considering the simpler problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∂tv​(x,y,t)=σ22​∂x​xv​(x,y,t)+α​(μ−x)​∂xv​(x,y,t)−β​y​∂yv​(x,y,t)−(r+λ)​v​(x,y,t)+λ​∫ℝv​(x,y+ξ,t)​f​(ξ)​𝑑ξ,t>0,v​(x,y,0)=max⁡(x+y−K,0).\begin{cases}\displaystyle\partial\_{t}v(x,y,t)=\frac{\sigma^{2}}{2}\partial\_{xx}v(x,y,t)+\alpha(\mu-x)\partial\_{x}v(x,y,t)-\beta y\partial\_{y}v(x,y,t)-(r+\lambda)v(x,y,t)\\[8.53581pt] \displaystyle\qquad\qquad\qquad\qquad\qquad+\lambda\int\_{\mathbb{R}}v(x,y+\xi,t)f(\xi)d\xi,\qquad t>0,\\[8.53581pt] v(x,y,0)=\max(x+y-K,0).\end{cases} |  | (2.5) |

In ([2.5](https://arxiv.org/html/2511.01587v1#S2.E5 "In 2.2 Formulation of the problem ‣ 2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) time has been reversed, as it is preferred to have an initial condition instead
of a terminal condition for the PIDE. Note that herein the maximum function is used as it is suboptimal to exercise when the payoff is negative. Further, the variable zz, that
represents the amount of energy, is dropped from the option value function vv because we
are only interested in one interval between exercise dates and zz stays constant in such interval.

## 3 Spatial discretisation

For the numerical solution of problem ([2.5](https://arxiv.org/html/2511.01587v1#S2.E5 "In 2.2 Formulation of the problem ‣ 2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")), we apply the method of
lines, consisting of a discretisation in space followed by a discretisation in time. This
section deals with the spatial discretisation. We successively consider the diffusion-reaction part, the integral part and the convection part of ([2.5](https://arxiv.org/html/2511.01587v1#S2.E5 "In 2.2 Formulation of the problem ‣ 2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")). The temporal
discretisation will be discussed in the next section.

### 3.1 Diffusion-reaction part

The spatial domain ℝ2\mathbb{R}^{2} is truncated to a bounded set [xmin,xmax]×[ymin,ymax][x\_{\min},x\_{\max}]\times[y\_{\min},y\_{\max}], where xmax>0x\_{\rm max}>0 and ymax>0y\_{\rm max}>0 and xmin<0x\_{\rm min}<0 and ymin<0y\_{\rm min}<0 are all taken sufficiently large in absolute value.
For the xx-direction and yy-direction, we impose linear boundary conditions:

|  |  |  |
| --- | --- | --- |
|  | ∂2v∂x2|x=xmin=∂2v∂x2|x=xmax=0and∂2v∂y2|y=ymin=∂2v∂y2|y=ymax=0.\frac{\partial^{2}v}{\partial x^{2}}|\_{x=x\_{\min}}=\frac{\partial^{2}v}{\partial x^{2}}|\_{x=x\_{\max}}=0\qquad\text{and}\qquad\frac{\partial^{2}v}{\partial y^{2}}|\_{y=y\_{\min}}=\frac{\partial^{2}v}{\partial y^{2}}|\_{y=y\_{\max}}=0. |  |

These conditions, which are common in computational finance, are also natural in our present application.

Let integers m1,m2≥1m\_{1},m\_{2}\geq 1 and the parameter d>0d>0 be given. We use a smooth nonuniform Cartesian grid {(xi,yj)∈[xmin,xmax]×[ymin,ymax]∣0≤i≤m1,0≤j≤m2}\{(x\_{i},y\_{j})\in[x\_{\min},x\_{\max}]\times[y\_{\min},y\_{\max}]\mid 0\leq i\leq m\_{1},0\leq j\leq m\_{2}\} such that
a large portion of grid points is contained in a region of (financial and numerical) interest, see, e.g., in ’t Hout and Lamotte ([2023](https://arxiv.org/html/2511.01587v1#bib.bib16)).
  
In the xx-direction, a smooth nonuniform mesh
xmin=x0<x1<⋯<xm1=xmaxx\_{\min}=x\_{0}<x\_{1}<\cdots<x\_{m\_{1}}=x\_{\max} is defined by

|  |  |  |
| --- | --- | --- |
|  | xi={−12​K+d⋅sinh⁡(ξx,i−ξx,1,int),whenever ​ξx,i≤ξx,1,int,xi−1+d⋅Δ​ξx,whenever ​ξx,1,int<ξx,i<ξx,2,int,32​K+d⋅sinh⁡(ξx,i−ξx,2,int),whenever ​ξx,2,int≤ξx,i,x\_{i}=\begin{cases}-\frac{1}{2}K+d\cdot\sinh(\xi\_{x,i}-\xi\_{x,1,\text{int}}),&\text{whenever\ }\xi\_{x,i}\leq\xi\_{x,1,\text{int}},\\[5.69054pt] x\_{i-1}+d\cdot\Delta\xi\_{x},&\text{whenever\ }\xi\_{x,1,\text{int}}<\xi\_{x,i}<\xi\_{x,2,\text{int}},\\[5.69054pt] \frac{3}{2}K+d\cdot\sinh(\xi\_{x,i}-\xi\_{x,2,\text{int}}),&\text{whenever\ }\xi\_{x,2,\text{int}}\leq\xi\_{x,i},\end{cases} |  |

where ξx,min=ξx,0<⋯<ξx,m1=ξx,max\xi\_{x,\min}=\xi\_{x,0}<\cdots<\xi\_{x,m\_{1}}=\xi\_{x,\max} are
equidistant points, Δ​ξx=ξx,1−ξx,0\Delta\xi\_{x}=\xi\_{x,1}-\xi\_{x,0}, ξx,1,int=−K2​d\xi\_{x,1,\text{int}}=-\frac{K}{2d}, ξx,2,int=3​K2​d\xi\_{x,2,\text{int}}=\frac{3K}{2d}, ξx,min=ξx,1,int+sinh−1⁡(xmind−ξx,1,int)\xi\_{x,\min}=\xi\_{x,1,\text{int}}+\sinh^{-1}(\frac{x\_{\min}}{d}-\xi\_{x,1,\text{int}}) and ξx,max=ξx,2,int+sinh−1⁡(xmaxd−ξx,2,int).\xi\_{x,\max}=\xi\_{x,2,\text{int}}+\sinh^{-1}(\frac{x\_{\max}}{d}-\xi\_{x,2,\text{int}})\,.
  
In the yy-direction, a smooth nonuniform mesh ymin=y0<y1<⋯<ym2=ymaxy\_{\min}=y\_{0}<y\_{1}<\cdots<y\_{m\_{2}}=y\_{\max} is defined by

|  |  |  |
| --- | --- | --- |
|  | yj={−K+d⋅sinh⁡(ξy,j−ξy,1,int),whenever ​ξy,j≤ξy,1,int,yj−1+d⋅Δ​ξy,whenever ​ξy,1,int<ξy,j<ξy,2,int,K+d⋅sinh⁡(ξy,j−ξy,2,int),whenever ​ξy,2,int≤ξy,j,y\_{j}=\begin{cases}-K+d\cdot\sinh(\xi\_{y,j}-\xi\_{y,1,\text{int}}),&\text{whenever\ }\xi\_{y,j}\leq\xi\_{y,1,\text{int}},\\[5.69054pt] y\_{j-1}+d\cdot\Delta\xi\_{y},&\text{whenever\ }\xi\_{y,1,\text{int}}<\xi\_{y,j}<\xi\_{y,2,\text{int}},\\[5.69054pt] K+d\cdot\sinh(\xi\_{y,j}-\xi\_{y,2,\text{int}}),&\text{whenever\ }\xi\_{y,2,\text{int}}\leq\xi\_{y,j},\end{cases} |  |

where ξy,min=ξy,0<⋯<ξy,m2=ξy,max\xi\_{y,\min}=\xi\_{y,0}<\cdots<\xi\_{y,m\_{2}}=\xi\_{y,\max} are
equidistant points, Δ​ξy=ξy,1−ξy,0\Delta\xi\_{y}=\xi\_{y,1}-\xi\_{y,0}, ξy,1,int=−Kd\xi\_{y,1,\text{int}}=-\frac{K}{d}, ξy,2,int=Kd\xi\_{y,2,\text{int}}=\frac{K}{d}, ξy,min=ξy,1,int+sinh−1⁡(ymind−ξy,1,int)\xi\_{y,\min}=\xi\_{y,1,\text{int}}+\sinh^{-1}(\frac{y\_{\min}}{d}-\xi\_{y,1,\text{int}}) and ξy,max=ξy,2,int+sinh−1⁡(ymaxd−ξy,2,int).\xi\_{y,\max}=\xi\_{y,2,\text{int}}+\sinh^{-1}(\frac{y\_{\max}}{d}-\xi\_{y,2,\text{int}})\,.

The grid is uniform with a relatively small spatial mesh width inside the *region of financial interest* [−12​K,32​K]×[−K,K][-\frac{1}{2}K,\frac{3}{2}K]\times[-K,K] and nonuniform outside. The parameter dd controls the fraction of points (xi,yj)(x\_{i},y\_{j}) inside [−12​K,32​K]×[−K,K][-\frac{1}{2}K,\frac{3}{2}K]\times[-K,K]. In this paper, we heuristically choose d=K5d=\frac{K}{5}.
Figure [1](https://arxiv.org/html/2511.01587v1#S3.F1 "Figure 1 ‣ 3.1 Diffusion-reaction part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") shows a sample spatial grid for m1=m2=50,K=50,xmin=−50,xmax=200,ymin=−150,ymax=150m\_{1}=m\_{2}=50,K=50,x\_{\min}=-50,x\_{\max}=200,y\_{\min}=-150,y\_{\max}=150.

![Refer to caption](x1.png)


Figure 1: Sample spatial grid for the parameter values m1=m2=50,K=50,xmin=−50,xmax=200,ymin=−150,ymax=150m\_{1}=m\_{2}=50,K=50,x\_{\min}=-50,x\_{\max}=200,y\_{\min}=-150,y\_{\max}=150, d=10d=10.

We denote the semidiscrete approximation of v​(xi,yj,t)v(x\_{i},y\_{j},t) by
Vi,j​(t)V\_{i,j}(t) and define the corresponding vector

|  |  |  |
| --- | --- | --- |
|  | V​(t)=(V0,0​(t),V0,1​(t),…,Vm1,m2−1​(t),Vm1,m2​(t))∈ℝ(m1+1)​(m2+1).V(t)=(V\_{0,0}(t),V\_{0,1}(t),\ldots,V\_{m\_{1},m\_{2}-1}(t),V\_{m\_{1},m\_{2}}(t))\in\mathbb{R}^{(m\_{1}+1)(m\_{2}+1)}. |  |

The diffusion term in ([2.5](https://arxiv.org/html/2511.01587v1#S2.E5 "In 2.2 Formulation of the problem ‣ 2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) is approximated by the second-order central finite difference formula:

|  |  |  |
| --- | --- | --- |
|  | ∂x​xv​(xi,yj,t)≈ωi,−1​Vi−1,j​(t)+ωi,0​Vi,j​(t)+ωi,1​Vi+1,j​(t),1≤i≤m1−1, 0≤j≤m2\partial\_{xx}v(x\_{i},y\_{j},t)\approx\omega\_{i,-1}V\_{i-1,j}(t)+\omega\_{i,0}V\_{i,j}(t)+\omega\_{i,1}V\_{i+1,j}(t),\quad 1\leq i\leq m\_{1}-1,\;0\leq j\leq m\_{2} |  |

with coefficients

|  |  |  |
| --- | --- | --- |
|  | ωi,−1=2Δ​xi−1​(Δ​xi−1+Δ​xi),ωi,0=−2Δ​xi−1​Δ​xi,ωi,1=2Δ​xi​(Δ​xi−1+Δ​xi),\omega\_{i,-1}=\frac{2}{\Delta x\_{i-1}(\Delta x\_{i-1}+\Delta x\_{i})}\;,\;\omega\_{i,0}=\frac{-2}{\Delta x\_{i-1}\Delta x\_{i}}\;,\;\omega\_{i,1}=\frac{2}{\Delta x\_{i}(\Delta x\_{i-1}+\Delta x\_{i})}, |  |

and Δ​xi\Delta x\_{i} is the mesh width in the xx-direction: Δ​xi=xi+1−xi\Delta x\_{i}=x\_{i+1}-x\_{i}.

The discretisation matrix corresponding to the diffusion-reaction part in ([2.5](https://arxiv.org/html/2511.01587v1#S2.E5 "In 2.2 Formulation of the problem ‣ 2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) can be written
as a Kronecker product:

|  |  |  |  |
| --- | --- | --- | --- |
|  | AD=(σ22D2−(r+λ)I1)⊗I2.A^{D}=\Bigl(\frac{\sigma^{2}}{2}D\_{2}-(r+\lambda)I\_{1}\Bigl)\otimes I\_{2}. |  | (3.1) |

Here, I1,I2I\_{1},I\_{2} are identity matrices of sizes (m1+1)×(m1+1)(m\_{1}+1)\times(m\_{1}+1) and (m2+1)×(m2+1)(m\_{2}+1)\times(m\_{2}+1), respectively.
D2:=trid​[ωi,−1,ωi,0,ωi,1]D\_{2}:=\mbox{trid}\,[\omega\_{i,-1},\omega\_{i,0},\omega\_{i,1}] is a (m1+1)×(m1+1)(m\_{1}+1)\times(m\_{1}+1) tridiagonal
matrix that represents the numerical differentiation of order two in the xx-direction.
In view of the linear boundary conditions, the elements in the top and bottom rows of the
matrix D2D\_{2} are all equal to zero, i.e., ω0,⋅=ωm1,⋅=0\omega\_{0,\cdot}=\omega\_{m\_{1},\cdot}=0.

### 3.2 Integral part

To approximate the integral part in ([2.5](https://arxiv.org/html/2511.01587v1#S2.E5 "In 2.2 Formulation of the problem ‣ 2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")), we truncate the integration
domain ℝ\mathbb{R} to [ymin,ymax][y\_{\min},y\_{\max}] and use linear interpolation
for the semidiscrete approximation between any given two consecutive grid points in the yy-direction. Hence,
starting from the integral at the grid point (xi,yj)(x\_{i},y\_{j}), 0≤i≤m10\leq i\leq m\_{1}, 0≤j≤m20\leq j\leq m\_{2}, we get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​∫−∞+∞v​(xi,yj+ξ,t)​f​(ξ)​𝑑ξ\displaystyle\lambda\int\_{-\infty}^{+\infty}v(x\_{i},y\_{j}+\xi,t)f(\xi)d\xi | =λ​∫−∞+∞v​(xi,ξ,t)​f​(ξ−yj)​𝑑ξ\displaystyle=\lambda\int\_{-\infty}^{+\infty}v(x\_{i},\xi,t)f(\xi-y\_{j})d\xi |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≈λ​∫y0ym2v​(xi,ξ,t)​f​(ξ−yj)​𝑑ξ\displaystyle\approx\lambda\int\_{y\_{0}}^{y\_{m\_{2}}}v(x\_{i},\xi,t)f(\xi-y\_{j})d\xi |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≈λ∑ℓ=0m2−1∫yℓyℓ+1(yℓ+1−ξΔ​yℓVi,ℓ(t)+ξ−yℓΔ​yℓVi,ℓ+1(t))f(ξ−yj)dξ\displaystyle\approx\lambda\sum\_{\ell=0}^{m\_{2}-1}\int\_{y\_{\ell}}^{y\_{\ell+1}}\Bigl(\frac{y\_{\ell+1}-\xi}{\Delta y\_{\ell}}V\_{i,\ell}(t)+\frac{\xi-y\_{\ell}}{\Delta y\_{\ell}}V\_{i,\ell+1}(t)\Bigl)f(\xi-y\_{j})d\xi |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =λ​∑ℓ=0m2B~j,ℓ​Vi,ℓ​(t)\displaystyle=\lambda\sum\_{\ell=0}^{m\_{2}}\tilde{B}\_{j,\ell}V\_{i,\ell}(t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =:𝒥i,j(t),\displaystyle=:\mathcal{J}\_{i,j}(t), |  |

where Δ​yℓ\Delta y\_{\ell} is the mesh width
Δ​yℓ=yℓ+1−yℓ\Delta y\_{\ell}=y\_{\ell+1}-y\_{\ell}, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | {B~j,0=y1​F0,j,0−F1,j,0Δ​y0B~j,ℓ=F1,j,ℓ−1−yℓ−1​F0,j,ℓ−1Δ​yℓ−1+yℓ+1​F0,j,ℓ−F1,j,ℓΔ​yℓ,1≤ℓ≤m2−1,B~j,m2=F1,j,m2−1−ym2−1​F0,j,m2−1Δ​ym2−1\begin{cases}\tilde{B}\_{j,0}=\dfrac{y\_{1}F\_{0,j,0}-F\_{1,j,0}}{\Delta y\_{0}}\\[5.69054pt] \tilde{B}\_{j,\ell}=\dfrac{F\_{1,j,\ell-1}-y\_{\ell-1}F\_{0,j,\ell-1}}{\Delta y\_{\ell-1}}+\dfrac{y\_{\ell+1}F\_{0,j,\ell}-F\_{1,j,\ell}}{\Delta y\_{\ell}},\quad 1\leq\ell\leq m\_{2}-1,\\[5.69054pt] \tilde{B}\_{j,m\_{2}}=\dfrac{F\_{1,j,m\_{2}-1}-y\_{m\_{2}-1}F\_{0,j,m\_{2}-1}}{\Delta y\_{m\_{2}-1}}\end{cases} |  | (3.2) |

with F0,j,ℓ=∫yℓyℓ+1f​(ξ−yj)​𝑑ξ,F1,j,ℓ=∫yℓyℓ+1ξ​f​(ξ−yj)​𝑑ξF\_{0,j,\ell}=\displaystyle\int\_{y\_{\ell}}^{y\_{\ell+1}}f(\xi-y\_{j})d\xi,\,F\_{1,j,\ell}=\int\_{y\_{\ell}}^{y\_{\ell+1}}\xi f(\xi-y\_{j})d\xi.
  
Let B=I1⊗λ​B~B=I\_{1}\otimes\lambda\tilde{B} be the semidiscrete jump matrix with B~=(B~j,ℓ)0≤j,ℓ≤m2\tilde{B}=(\tilde{B}\_{j,\ell})\_{0\leq j,\ell\leq m\_{2}}. Then, B​VBV denotes the
approximation of the integral where the value of the vector B​VBV at the entry
i⋅(m2+1)+ji\cdot(m\_{2}+1)+j is exactly 𝒥i,j​(t)\mathcal{J}\_{i,j}(t).
To obtain a more accurate approximation of the integral term in our numerical experiments, we account for the contribution of the integrand outside the truncated spatial domain [ymin,ymax][y\_{\min},y\_{\max}]. For the approximation of the option value function outside this domain, we apply linear extrapolation.
This approach improves the accuracy of the numerical quadrature used to evaluate the integral term.
The computational complexity of the above approximation is m1​m22m\_{1}m\_{2}^{2}. We remark, however, that in the special case of the Kou-type jump model the integral can approximated with linear complexity m1​m2m\_{1}m\_{2} by an algorithm due to Toivanen ([2008](https://arxiv.org/html/2511.01587v1#bib.bib25)).

### 3.3 Convection part

Aside from the nonlocal integral term in ([2.5](https://arxiv.org/html/2511.01587v1#S2.E5 "In 2.2 Formulation of the problem ‣ 2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")), a significant challenge arises due to the nature of the asset price model: the problem is convection-dominated in the xx-direction and exhibits pure convection in the yy-direction. This feature is attributed to the electricity price dynamics, which exhibits fast mean reversion characterised by large values of the parameters α\alpha and, especially, β\beta. These values, detailed in the parameter sets provided in Table [1](https://arxiv.org/html/2511.01587v1#S6.T1 "Table 1 ‣ 6.1 Financial parameter values ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") of Section [6.1](https://arxiv.org/html/2511.01587v1#S6.SS1 "6.1 Financial parameter values ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"), result in a highly convection-dominated problem as the diffusion coefficient, σ22\frac{\sigma^{2}}{2}, is constant and relatively small in comparison to the convection coefficients.

Moreover, the presence of nonsmooth initial data coupled with a convection-dominated problem leads to the formation of a region of nonsmoothness of the solution, characterised by sharp gradients. This poses difficulties for central finite difference formulas, which may suffer from spurious oscillations.

To address the convection dominance behaviour, we explore two numerical strategies: a semi-Lagrangian method and a suitable semidiscretisation method. Both techniques require effective interpolation or discretisation schemes that ensure adequate accuracy while maintaining numerical stability.

#### 3.3.1 Semi-Lagrangian method

The semi-Lagrangian method is a well-known and powerful numerical
tool for solving transport and convection-dominated problems.
One employs the characteristic curve (x​(t),y​(t),t)(x(t),y(t),t) such that:

* •

  x​(t)x(t) satisfies:

  |  |  |  |
  | --- | --- | --- |
  |  | ∂v​(x​(t),y,t)∂t=∂v∂t​(x​(t),y,t)−α​(μ−x)​∂v∂x​(x​(t),y,t)\frac{\partial v(x(t),y,t)}{\partial t}=\frac{\partial v}{\partial t}(x(t),y,t)-\alpha(\mu-x)\frac{\partial v}{\partial x}(x(t),y,t) |  |

  which holds if x​(t)=μ​(1−e−α​(s−t))+x​(s)​e−α​(s−t)x(t)=\mu(1-e^{-\alpha(s-t)})+x(s)e^{-\alpha(s-t)} whenever t≤st\leq s.
* •

  y​(t)y(t) satisfies:

  |  |  |  |
  | --- | --- | --- |
  |  | ∂v​(x,y​(t),t)∂t=∂v∂t​(x,y​(t),t)+β​y​∂v∂y​(x,y​(t),t)\frac{\partial v(x,y(t),t)}{\partial t}=\frac{\partial v}{\partial t}(x,y(t),t)+\beta y\frac{\partial v}{\partial y}(x,y(t),t) |  |

  which holds if y​(t)=y​(s)​exp⁡{−β​(s−t)}y(t)=y(s)\exp\{-\beta(s-t)\} whenever t≤st\leq s.

Thus, on the characteristic curve, the PIDE ([2.5](https://arxiv.org/html/2511.01587v1#S2.E5 "In 2.2 Formulation of the problem ‣ 2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) can be rewritten as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂tv​(x​(t),y​(t),t)=σ22​∂x​xv​(x​(t),y​(t),t)−(r+λ)​v​(x​(t),y​(t),t)+λ​∫ℝv​(x​(t),y​(t)+ξ,t)​f​(ξ)​𝑑ξ.\partial\_{t}v(x(t),y(t),t)=\frac{\sigma^{2}}{2}\partial\_{xx}v(x(t),y(t),t)-(r+\lambda)v(x(t),y(t),t)+\lambda\int\_{\mathbb{R}}v(x(t),y(t)+\xi,t)f(\xi)d\xi. |  | (3.3) |

We refer to Section [4.1](https://arxiv.org/html/2511.01587v1#S4.SS1 "4.1 Temporal scheme for the semi-Lagrangian approach ‣ 4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") for its temporal discretisation.

#### 3.3.2 Semidiscrete approximation

Instead of using a semi-Lagrangian method, we can directly approximate
the convection terms ∂v∂x\frac{\partial v}{\partial x} and ∂v∂y\frac{\partial v}{\partial y} at the grid points (xi,yj)(x\_{i},y\_{j}), 0≤i≤m10\leq i\leq m\_{1}, 0≤j≤m20\leq j\leq m\_{2}, using one of the following schemes:

Second-order upwind scheme
:   By Taylor expansion, one obtains the formula for the second-order upwind scheme in the case of nonuniform spatial grids. It is a second-order finite difference approximation of the first-order
    derivative with three-point stencils:

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | ∂v∂x​(xi,yj,t)≈{Δ​xi−2+Δ​xi−1Δ​xi−2​Δ​xi−1​(Vi,j−Vi−1,j)−Δ​xi−1Δ​xi−2​(Δ​xi−2+Δ​xi−1)​(Vi,j−Vi−2,j)if​α​(μ−xi)<0,Δ​xi+Δ​xi+1Δ​xi​Δ​xi+1​(Vi+1,j−Vi,j)−Δ​xiΔ​xi+1​(Δ​xi+Δ​xi+1)​(Vi+2,j−Vi,j)if​α​(μ−xi)>0\begin{split}&\frac{\partial v}{\partial x}(x\_{i},y\_{j},t)\\ &\approx\begin{cases}\dfrac{\Delta x\_{i-2}+\Delta x\_{i-1}}{\Delta x\_{i-2}\Delta x\_{i-1}}(V\_{i,j}-V\_{i-1,j})-\dfrac{\Delta x\_{i-1}}{\Delta x\_{i-2}(\Delta x\_{i-2}+\Delta x\_{i-1})}(V\_{i,j}-V\_{i-2,j})&\;\text{if}\;\alpha(\mu-x\_{i})<0,\\[8.53581pt] \dfrac{\Delta x\_{i}+\Delta x\_{i+1}}{\Delta x\_{i}\Delta x\_{i+1}}(V\_{i+1,j}-V\_{i,j})-\dfrac{\Delta x\_{i}}{\Delta x\_{i+1}(\Delta x\_{i}+\Delta x\_{i+1})}(V\_{i+2,j}-V\_{i,j})&\;\text{if}\;\alpha(\mu-x\_{i})>0\\ \end{cases}\end{split} |  | (3.4) |

    and

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | ∂v∂y​(xi,yj,t)≈{Δ​yj−2+Δ​yj−1Δ​yj−2​Δ​yj−1​(Vi,j−Vi,j−1)−Δ​yj−1Δ​yj−2​(Δ​yj−2+Δ​yj−1)​(Vi,j−Vi,j−2)if−β​yj<0,Δ​yj+Δ​yj+1Δ​yj​Δ​yj+1​(Vi,j+1−Vi,j)−Δ​yjΔ​yj+1​(Δ​yj+Δ​yj+1)​(Vi,j+2−Vi,j)if−β​yj>0.\begin{split}&\frac{\partial v}{\partial y}(x\_{i},y\_{j},t)\\ &\approx\begin{cases}\dfrac{\Delta y\_{j-2}+\Delta y\_{j-1}}{\Delta y\_{j-2}\Delta y\_{j-1}}(V\_{i,j}-V\_{i,j-1})-\dfrac{\Delta y\_{j-1}}{\Delta y\_{j-2}(\Delta y\_{j-2}+\Delta y\_{j-1})}(V\_{i,j}-V\_{i,j-2})&\;\;\text{if}\;-\beta y\_{j}<0,\\[8.53581pt] \dfrac{\Delta y\_{j}+\Delta y\_{j+1}}{\Delta y\_{j}\Delta y\_{j+1}}(V\_{i,j+1}-V\_{i,j})-\dfrac{\Delta y\_{j}}{\Delta y\_{j+1}(\Delta y\_{j}+\Delta y\_{j+1})}(V\_{i,j+2}-V\_{i,j})&\;\;\text{if}\;-\beta y\_{j}>0\,.\\ \end{cases}\end{split} |  | (3.5) |

    Here, for ease of presentation, we omitted the argument tt of VV.

QUICK scheme
:   The QUICK (Quadratic Upstream Interpolation for Convective Kinematics) scheme, see Leonard ([1979](https://arxiv.org/html/2511.01587v1#bib.bib20)), is a second-order method based on quadratic interpolation. It is commonly used in computational fluid dynamics (CFD) for solving convection-diffusion equations. For clarity, the QUICK scheme employed in this paper is formulated using the finite difference approach, although it was originally introduced and is more commonly applied within the finite volume framework. Let quadratic polynomials px,i,jp\_{x,i,j} and py,i,jp\_{y,i,j} be defined by:

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | px,i,j​(x)\displaystyle p\_{x,i,j}(x) | =(x−xi)​(x−xi+1)Δ​xi−1​(Δ​xi−1+Δ​xi)​Vi−1,j−(x−xi−1)​(x−xi+1)Δ​xi−1​Δ​xi​Vi,j+(x−xi−1)​(x−xi)(Δ​xi−1+Δ​xi)​Δ​xi​Vi+1,j,\displaystyle=\frac{(x\!-\!x\_{i})(x\!-\!x\_{i+1})}{\Delta x\_{i-1}(\Delta x\_{i-1}+\Delta x\_{i})}V\_{i-1,j}\!-\!\frac{(x\!-\!x\_{i-1})(x\!-\!x\_{i+1})}{\Delta x\_{i-1}\Delta x\_{i}}V\_{i,j}\!+\!\frac{(x\!-\!x\_{i-1})(x\!-\!x\_{i})}{(\Delta x\_{i-1}+\Delta x\_{i})\Delta x\_{i}}V\_{i+1,j}, |  |
    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | py,i,j​(y)\displaystyle p\_{y,i,j}(y) | =(y−yj)​(y−yj+1)Δ​yj−1​(Δ​yj−1+Δ​yj)​Vi,j−1−(y−yj−1)​(y−yj+1)Δ​yj−1​Δ​yj​Vi,j+(y−yj−1)​(y−yj)(Δ​yj−1+Δ​yj)​Δ​yj​Vi,j+1.\displaystyle=\frac{(y\!-\!y\_{j})(y\!-\!y\_{j+1})}{\Delta y\_{j-1}(\Delta y\_{j-1}+\Delta y\_{j})}V\_{i,j-1}\!-\!\frac{(y\!-\!y\_{j-1})(y\!-\!y\_{j+1})}{\Delta y\_{j-1}\Delta y\_{j}}V\_{i,j}\!+\!\frac{(y\!-\!y\_{j-1})(y\!-\!y\_{j})}{(\Delta y\_{j-1}+\Delta y\_{j})\Delta y\_{j}}V\_{i,j+1}. |  |

    Then, the QUICK scheme for the first-order derivative is given by:

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | ∂v∂x​(xi,yj,t)≈{px,i,j​(xi+1/2)−px,i−1,j​(xi−1/2)xi+1/2−xi−1/2if​α​(μ−xi)<0,px,i+1,j​(xi+1/2)−px,i,j​(xi−1/2)xi+1/2−xi−1/2if​α​(μ−xi)>0,\begin{split}\frac{\partial v}{\partial x}(x\_{i},y\_{j},t)\approx\begin{cases}\dfrac{p\_{x,i,j}(x\_{i+1/2})-p\_{x,i-1,j}(x\_{i-1/2})}{x\_{i+1/2}-x\_{i-1/2}}&\;\text{if}\;\alpha(\mu-x\_{i})<0,\\[8.53581pt] \dfrac{p\_{x,i+1,j}(x\_{i+1/2})-p\_{x,i,j}(x\_{i-1/2})}{x\_{i+1/2}-x\_{i-1/2}}&\;\text{if}\;\alpha(\mu-x\_{i})>0,\\ \end{cases}\end{split} |  | (3.6) |

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | ∂v∂y​(xi,yj,t)≈{py,i,j​(yj+1/2)−py,i,j−1​(yj−1/2)yj+1/2−yj−1/2if−β​yj<0,py,i,j+1​(yj+1/2)−py,i,j​(yj−1/2)yj+1/2−yj−1/2if−β​yj>0,\begin{split}\frac{\partial v}{\partial y}(x\_{i},y\_{j},t)\approx\begin{cases}\dfrac{p\_{y,i,j}(y\_{j+1/2})-p\_{y,i,j-1}(y\_{j-1/2})}{y\_{j+1/2}-y\_{j-1/2}}&\;\text{if}\;-\beta y\_{j}<0,\\[8.53581pt] \dfrac{p\_{y,i,j+1}(y\_{j+1/2})-p\_{y,i,j}(y\_{j-1/2})}{y\_{j+1/2}-y\_{j-1/2}}&\;\text{if}\;-\beta y\_{j}>0,\\ \end{cases}\end{split} |  | (3.7) |

    where xi+1/2=xi+1+xi2x\_{i+1/2}=\frac{x\_{i+1}+x\_{i}}{2} and yj+1/2=yj+1+yj2y\_{j+1/2}=\frac{y\_{j+1}+y\_{j}}{2}.

The above semidiscretisation schemes, second-order upwind and QUICK, can be assembled in matrix form. The values at ghost points, for example Vm1+1,jV\_{m\_{1}+1,j} and Vm1+2,jV\_{m\_{1}+2,j}, are defined by linear extrapolation of values inside the truncated domain, for instance Vm1+1,j=2​Vm1,j−Vm1−1,jV\_{m\_{1}+1,j}=2V\_{m\_{1},j}-V\_{m\_{1}-1,j} and Vm1+2,j=3​Vm1,j−2​Vm1−1,jV\_{m\_{1}+2,j}=3V\_{m\_{1},j}-2V\_{m\_{1}-1,j}. The matrices can be expressed in the following way:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ax=Dx​A~x⊗I2,A\_{x}=D\_{x}\tilde{A}\_{x}\otimes I\_{2}, |  | (3.8) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ay=I1⊗Dy​A~y,A\_{y}=I\_{1}\otimes D\_{y}\tilde{A}\_{y}, |  | (3.9) |

where A~x\tilde{A}\_{x} and A~y\tilde{A}\_{y} represent the matrices of numerical differentiation of order one in the xx- respectively yy-direction stemming from either the second-order upwind scheme or the QUICK scheme. Next, DxD\_{x} and DyD\_{y} are diagonal matrices with Dx,i,i=α​(μ−xi)D\_{x,i,i}=\alpha(\mu-x\_{i}) and Dy,j,j=−β​yjD\_{y,j,j}=-\beta y\_{j} for 0≤i≤m10\leq i\leq m\_{1} and 0≤j≤m20\leq j\leq m\_{2}.

The spatial discretisation of ([2.5](https://arxiv.org/html/2511.01587v1#S2.E5 "In 2.2 Formulation of the problem ‣ 2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) defined in this section leads to the system of ODEs

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vd​t​(t)=(A+B)​V​(t),\frac{dV}{dt}(t)=(A+B)V(t), |  | (3.10) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | A=AD+Ax+Ay.A=A^{D}+A\_{x}+A\_{y}. |  | (3.11) |

The initial vector is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(0)=max⁡(x^⊗ey+ex⊗y^−K⋅ex⊗ey,0),V(0)=\max(\hat{x}\otimes e\_{y}+e\_{x}\otimes\hat{y}-K\cdot e\_{x}\otimes e\_{y},0), |  | (3.12) |

where x^=(x0,…,xm1)\hat{x}=(x\_{0},\ldots,x\_{m\_{1}}) and y^=(y0,…,ym2)\hat{y}=(y\_{0},\ldots,y\_{m\_{2}}), and ex,eye\_{x},e\_{y} denote vectors of ones of size m1+1m\_{1}+1 and m2+1m\_{2}+1 respectively.

## 4 Temporal discretisation

In this section we present different schemes for the temporal discretisation of the semidiscrete problem.
Note that for the semi-Lagrangian approach as well as the semidiscrete approach the jump matrix BB derived from the spatial discretisation in Section [3.2](https://arxiv.org/html/2511.01587v1#S3.SS2 "3.2 Integral part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") is a full matrix. Thus, we will avoid using a temporal
scheme where one needs to solve a linear system involving this matrix.
We consider the temporal discretisation schemes described in the subsections below. Let integer N≥1N\geq 1 be given and the step size Δ​t=TN\Delta t=\frac{T}{N}. Let VnV^{n} denote
the approximation of V​(tn)V(t\_{n}) at the temporal grid point
tn=n​Δ​tt\_{n}=n\Delta t (n=1,2,…,Nn=1,2,\ldots,N) with V0=V​(0)V^{0}=V(0). Let I=I1⊗I2I=I\_{1}\otimes I\_{2}.

### 4.1 Temporal scheme for the semi-Lagrangian approach

The Crank–Nicolson scheme with fixed-point iteration combined with the semi-Lagrangian
approach was proposed in d’Halluin et al. ([2005a](https://arxiv.org/html/2511.01587v1#bib.bib8)) for the numerical
valuation of Asian options. Applied to our case, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | (I−12​Δ​t​AD)​Yℓ=ℐ​[Vn]+12​Δ​t​ℐ​[AD​Vn]+12​Δ​t​ℐ​[B​Vn]+12​Δ​t​B​Yℓ−1,(I-\tfrac{1}{2}\Delta tA^{D})Y\_{\ell}=\mathcal{I}[V^{n}]+\tfrac{1}{2}\Delta t\mathcal{I}[A^{D}V^{n}]+\tfrac{1}{2}\Delta t\mathcal{I}[BV^{n}]+\tfrac{1}{2}\Delta tBY\_{\ell-1}, |  | (4.1) |

for ℓ=1,…,ℓm​a​x\ell=1,\ldots,\ell\_{max} and Vn+1=Yℓm​a​xV^{n+1}=Y\_{\ell\_{max}}. Here, Y0=2​Vn−Vn−1Y\_{0}=2V^{n}-V^{n-1} if n≥1n\geq 1 and Y0=V0Y\_{0}=V^{0} if n=0n=0. The following stopping criterion is used for the fixed-point iteration:

|  |  |  |
| --- | --- | --- |
|  | max𝑘​∣Yℓ,k−Yℓ−1,k∣max⁡(1,∣Yℓ,k∣)<10−7.\underset{k}{\max}\frac{\mid Y\_{\ell,k}-Y\_{\ell-1,k}\mid}{\max(1,\mid Y\_{\ell,k}\mid)}<10^{-7}. |  |

In the scheme ([4.1](https://arxiv.org/html/2511.01587v1#S4.E1 "In 4.1 Temporal scheme for the semi-Lagrangian approach ‣ 4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")),
the operator ℐ\mathcal{I} denotes the two-dimensional cubic spline interpolation,
which yields approximations at the departure points (μ​(1−e−α​Δ​t)+xi​e−α​Δ​t,yj​e−β​Δ​t)(\mu(1-e^{-\alpha\Delta t})+x\_{i}e^{-\alpha\Delta t},y\_{j}e^{-\beta\Delta t}),
using known approximations at the grid points (xi,yj)(x\_{i},y\_{j}) for 0≤i≤m10\leq i\leq m\_{1} and 0≤j≤m20\leq j\leq m\_{2}. Hereafter, the scheme ([4.1](https://arxiv.org/html/2511.01587v1#S4.E1 "In 4.1 Temporal scheme for the semi-Lagrangian approach ‣ 4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) is referred to as the semi-Lagrangian Crank–Nicolson scheme with fixed-point iteration (SLCNFI).

### 4.2 Temporal schemes for the semidiscretisation approach

We consider two temporal discretisation schemes for the semidiscrete system ([3.10](https://arxiv.org/html/2511.01587v1#S3.E10 "In 3.3.2 Semidiscrete approximation ‣ 3.3 Convection part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")):

Crank–Nicolson scheme with fixed-point iteration (CNFI)
:   The combination of the Crank–Nicolson scheme for the convection-diffusion-reaction
    part with a fixed-point iteration for the integral part was proposed in Tavella and Randall ([2000](https://arxiv.org/html/2511.01587v1#bib.bib23)) and analysed in
    d’Halluin et al. ([2005b](https://arxiv.org/html/2511.01587v1#bib.bib9)):

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | (I−12​Δ​t​A)​Yℓ=(I+12​Δ​t​A)​Vn+12​Δ​t​(B​Vn+B​Yℓ−1),(I-\tfrac{1}{2}\Delta tA)Y\_{\ell}=(I+\tfrac{1}{2}\Delta tA)V^{n}+\tfrac{1}{2}\Delta t(BV^{n}+BY\_{\ell-1})\,, |  | (4.2) |

    for ℓ=1,…,ℓmax\ell=1,\ldots,\ell\_{\max}. We use the same starting vector and stopping criterion as in the semi-Lagrangian
    approach. We apply Rannacher time-stepping for the first two steps using half time steps 12​Δ​t\frac{1}{2}\Delta t by computing V1V^{1} and V2V^{2} using the backward Euler scheme with fixed-point iteration on the integral part. This technique is a well known remedy for the adverse impact of the nonsmoothness of the initial function on the convergence of the Crank–Nicolson scheme due to its lack of LL-stability (see Rannacher ([1984](https://arxiv.org/html/2511.01587v1#bib.bib22))).

Diagonally implicit Runge-Kutta scheme with fixed-point iteration (DIRKFI)
:   This scheme, studied by in ’t Hout ([2025](https://arxiv.org/html/2511.01587v1#bib.bib15)), combines the DIRK scheme with a penalty/fixed-point iteration for the numerical valuation for American-style options under the two-asset Kou-type jump-diffusion model. In our case, we obtain.

    |  |  |  |  |
    | --- | --- | --- | --- |
    |  | {W1=Vn+(1−θ)​Δ​t​(A​Vn+B​Vn),(I−θ​Δ​t​A)​Yℓ=W1+θ​Δ​t​B​Yℓ−1(ℓ=1,…,ℓmax),Y^=Yℓmax,W2=Vn+12​Δ​t​(A​Vn+B​Vn)+(12−θ)​Δ​t​(A​Y^+B​Y^),(I−θ​Δ​t​A)​Zℓ=W2+θ​Δ​t​B​Zℓ−1(ℓ=1,…,ℓmax),Vn+1=Zℓmax.\left\{\begin{array}[]{lll}W\_{1}=V^{n}+(1-\theta)\Delta t(AV^{n}+BV^{n}),\\ (I-\theta\Delta tA)Y\_{\ell}=W\_{1}+\theta\Delta tBY\_{\ell-1}\quad(\ell=1,\ldots,\ell\_{\max}),\\ \widehat{Y}=Y\_{\ell\_{\max}},\\ W\_{2}=V^{n}+\tfrac{1}{2}\Delta t(AV^{n}+BV^{n})+(\tfrac{1}{2}-\theta)\Delta t(A\widehat{Y}+B\widehat{Y}),\\ (I-\theta\Delta tA)Z\_{\ell}=W\_{2}+\theta\Delta tBZ\_{\ell-1}\quad(\ell=1,\ldots,\ell\_{\max}),\\ V^{n+1}=Z\_{\ell\_{\max}}.\end{array}\right. |  | (4.3) |

    At each time step, there are two fixed-point iteration processes. For the starting vectors, Y0=2​Vn−Vn−1Y\_{0}=2V^{n}-V^{n-1} if n≥1n\geq 1, Y0=V0Y\_{0}=V^{0} if n=0n=0 and Z0=Y^Z\_{0}=\hat{Y}. For both processes, the same stopping criterion as in the SLCNFI scheme is used. The scheme has a second-order consistency for any θ\theta and is LL-stable if and only if θ=1±22\theta=1\pm\frac{\sqrt{2}}{2}, see Cash ([1984](https://arxiv.org/html/2511.01587v1#bib.bib6)). The choice θ=1−22\theta=1-\frac{\sqrt{2}}{2} yields a smaller error constant as observed in in ’t Hout ([2025](https://arxiv.org/html/2511.01587v1#bib.bib15)).

## 5 Convergence and stability analysis for the semidiscretisation approach

This section deals with the convergence and stability analysis of some of the numerical schemes above. In Section [5.1](https://arxiv.org/html/2511.01587v1#S5.SS1 "5.1 Convergence of CNFI and DIRKFI ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"), the convergence in the ℓ∞\ell\_{\infty}-norm of the CNFI scheme ([4.2](https://arxiv.org/html/2511.01587v1#S4.E2 "In item Crank–Nicolson scheme with fixed-point iteration (CNFI) ‣ 4.2 Temporal schemes for the semidiscretisation approach ‣ 4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"))
to the Crank–Nicolson scheme is studied and similarly the DIRKFI scheme. Then, in Section [5.2](https://arxiv.org/html/2511.01587v1#S5.SS2 "5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"), we study the stability and convergence in the ℓ2\ell\_{2}-norm of the Crank–Nicolson and DIRK schemes under Dirichlet boundary conditions. Throughout this section,
we consider a uniform grid with mesh width Δ​x\Delta x in the xx-direction and Δ​y\Delta y in the yy-direction.

For the semidiscretisation of the convection terms in ([2.5](https://arxiv.org/html/2511.01587v1#S2.E5 "In 2.2 Formulation of the problem ‣ 2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) we consider the following general finite difference scheme

|  |  |  |  |
| --- | --- | --- | --- |
|  | ai​∂v∂x​(xi,yj,t)≈ai+​w2​Vi+2,j+w1​Vi+1,j+w0​Vi,j+w−1​Vi−1,jΔ​x+ai−​−w−1​Vi+1,j−w0​Vi,j−w1​Vi−1,j−w2​Vi−2,jΔ​x,bj​∂v∂y​(xi,yj,t)≈bj+​w2​Vi,j+2+w1​Vi,j+1+w0​Vi,j+w−1​Vi,j−1Δ​y+bj−​−w−1​Vi,j+1−w0​Vi,j−w1​Vi,j−1−w2​Vi,j−2Δ​y,\begin{split}a\_{i}\frac{\partial v}{\partial x}(x\_{i},y\_{j},t)&\approx a^{+}\_{i}\frac{w\_{2}V\_{i+2,j}+w\_{1}V\_{i+1,j}+w\_{0}V\_{i,j}+w\_{-1}V\_{i-1,j}}{\Delta x}\\ &\quad+a^{-}\_{i}\frac{-w\_{-1}V\_{i+1,j}-w\_{0}V\_{i,j}-w\_{1}V\_{i-1,j}-w\_{2}V\_{i-2,j}}{\Delta x},\\[11.38109pt] b\_{j}\frac{\partial v}{\partial y}(x\_{i},y\_{j},t)&\approx b^{+}\_{j}\frac{w\_{2}V\_{i,j+2}+w\_{1}V\_{i,j+1}+w\_{0}V\_{i,j}+w\_{-1}V\_{i,j-1}}{\Delta y}\\ &\quad+b^{-}\_{j}\frac{-w\_{-1}V\_{i,j+1}-w\_{0}V\_{i,j}-w\_{1}V\_{i,j-1}-w\_{2}V\_{i,j-2}}{\Delta y},\end{split} |  | (5.1) |

for 0≤i≤m10\leq i\leq m\_{1} and 0≤j≤m20\leq j\leq m\_{2}. Here, ai=α​(μ−xi)a\_{i}=\alpha(\mu-x\_{i}) and bj=−β​yjb\_{j}=-\beta y\_{j} and for any real number cc we denote c+=max⁡(c,0)c^{+}=\max(c,0) and c−=min⁡(c,0)c^{-}=\min(c,0). The coefficients w−1,w0,w1,w2w\_{-1},w\_{0},w\_{1},w\_{2} satisfy the following conditions

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑k=−12wk=0,∑k=−12k​wk=1,∑k=−12k2​wk=0,w2≤0.\sum\_{k=-1}^{2}w\_{k}=0,\quad\sum\_{k=-1}^{2}kw\_{k}=1,\quad\sum\_{k=-1}^{2}k^{2}w\_{k}=0,\quad w\_{2}\leq 0. |  | (5.2) |

The three equalities in ([5.2](https://arxiv.org/html/2511.01587v1#S5.E2 "In 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")), which can be derived using Taylor expansion, are sufficient and necessary conditions for the finite difference scheme to be at least of second-order. Schemes of interest that belong to the above family of schemes ([5.1](https://arxiv.org/html/2511.01587v1#S5.E1 "In 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"))-([5.2](https://arxiv.org/html/2511.01587v1#S5.E2 "In 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) are:

* •

  The second-order upwind scheme ([3.4](https://arxiv.org/html/2511.01587v1#S3.E4 "In item Second-order upwind scheme ‣ 3.3.2 Semidiscrete approximation ‣ 3.3 Convection part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"))-([3.5](https://arxiv.org/html/2511.01587v1#S3.E5 "In item Second-order upwind scheme ‣ 3.3.2 Semidiscrete approximation ‣ 3.3 Convection part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) with w2=−12w\_{2}=-\frac{1}{2}, w1=2,w0=−32w\_{1}=2,w\_{0}=-\frac{3}{2} and w−1=0w\_{-1}=0.
* •

  The second-order QUICK scheme ([3.6](https://arxiv.org/html/2511.01587v1#S3.E6 "In item QUICK scheme ‣ 3.3.2 Semidiscrete approximation ‣ 3.3 Convection part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"))-([3.7](https://arxiv.org/html/2511.01587v1#S3.E7 "In item QUICK scheme ‣ 3.3.2 Semidiscrete approximation ‣ 3.3 Convection part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) with w2=−18w\_{2}=-\frac{1}{8}, w1=78w\_{1}=\frac{7}{8} and w0=w−1=−38w\_{0}=w\_{-1}=-\frac{3}{8}.
* •

  The third-order upwind scheme with w2=−16w\_{2}=-\frac{1}{6}, w1=1w\_{1}=1, w0=−36w\_{0}=-\frac{3}{6} and w−1=−26w\_{-1}=-\frac{2}{6}.
* •

  The second-order central scheme with w2=0w\_{2}=0, w1=12w\_{1}=\frac{1}{2}, w0=0w\_{0}=0 and w−1=−12w\_{-1}=-\frac{1}{2}.

Without loss of generality, we assume that the functions aa and bb with a​(x)=α​(μ−x)a(x)=\alpha(\mu-x) and b​(y)=−β​yb(y)=-\beta y change sign within the truncated domain.
Near the boundary, if a numerical stencil extends outside the domain – e.g., requiring values such as V−1,jV\_{-1,j} – linear extrapolation is employed, see Section [3.3.2](https://arxiv.org/html/2511.01587v1#S3.SS3.SSS2 "3.3.2 Semidiscrete approximation ‣ 3.3 Convection part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"). This extrapolation is consistent with the imposed linear boundary conditions. We note that, in Section [5.2](https://arxiv.org/html/2511.01587v1#S5.SS2 "5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"), Dirichlet boundary conditions are prescribed, eliminating the need to address extrapolation at the boundaries in that context, in particular that the convection coefficients aa and bb are positive near xmin,yminx\_{\min},y\_{\min} and negative near xmax,ymaxx\_{\max},y\_{\max}.

### 5.1 Convergence of CNFI and DIRKFI

The theorem below deals with the convergence in the ℓ∞\ell\_{\infty}-norm of the CNFI scheme ([4.2](https://arxiv.org/html/2511.01587v1#S4.E2 "In item Crank–Nicolson scheme with fixed-point iteration (CNFI) ‣ 4.2 Temporal schemes for the semidiscretisation approach ‣ 4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) to the Crank–Nicolson scheme:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (I−12​Δ​t​A)​Vn+1=(I+12​Δ​t​A)​Vn+12​Δ​t​(B​Vn+B​Vn+1).(I-\tfrac{1}{2}\Delta tA)V^{n+1}=(I+\tfrac{1}{2}\Delta tA)V^{n}+\tfrac{1}{2}\Delta t(BV^{n}+BV^{n+1}). |  | (5.3) |

###### Theorem 5.1.

Let εℓ=Vn+1−Yℓ\varepsilon\_{\ell}=V^{n+1}-Y\_{\ell} where Vn+1V^{n+1} is given by ([5.3](https://arxiv.org/html/2511.01587v1#S5.E3 "In 5.1 Convergence of CNFI and DIRKFI ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) and YℓY\_{\ell} is given by ([4.2](https://arxiv.org/html/2511.01587v1#S4.E2 "In item Crank–Nicolson scheme with fixed-point iteration (CNFI) ‣ 4.2 Temporal schemes for the semidiscretisation approach ‣ 4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")). Let

|  |  |  |
| --- | --- | --- |
|  | κx=(|w2|+|w1|+|w−1|+w0)​maxi⁡|ai|andκy=(|w2|+|w1|+|w−1|+w0)​maxj⁡|bj|,\kappa\_{x}=(|w\_{2}|+|w\_{1}|+|w\_{-1}|+w\_{0})\max\_{i}|a\_{i}|\quad\text{and}\quad\kappa\_{y}=(|w\_{2}|+|w\_{1}|+|w\_{-1}|+w\_{0})\max\_{j}|b\_{j}|, |  |

where the weights w−1,w0,w1,w2w\_{-1},w\_{0},w\_{1},w\_{2} satisfy ([5.2](https://arxiv.org/html/2511.01587v1#S5.E2 "In 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")). If κx​Δ​t2​Δ​x+κy​Δ​t2​Δ​y<1+Δ​t2​r\kappa\_{x}\frac{\Delta t}{2\Delta x}+\kappa\_{y}\frac{\Delta t}{2\Delta y}<1+\frac{\Delta t}{2}r, then the CNFI scheme ([4.2](https://arxiv.org/html/2511.01587v1#S4.E2 "In item Crank–Nicolson scheme with fixed-point iteration (CNFI) ‣ 4.2 Temporal schemes for the semidiscretisation approach ‣ 4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) converges to the Crank–Nicolson scheme ([5.3](https://arxiv.org/html/2511.01587v1#S5.E3 "In 5.1 Convergence of CNFI and DIRKFI ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) in the ℓ∞\ell\_{\infty}-norm and

|  |  |  |
| --- | --- | --- |
|  | ‖εℓ‖∞≤Θ​‖εℓ−1‖∞with​Θ=Δ​t2​λ1+Δ​t2​(r+λ)−(κx​Δ​t2​Δ​x+κy​Δ​t2​Δ​y)<1.||\varepsilon\_{\ell}||\_{\infty}\leq\Theta\,||\varepsilon\_{\ell-1}||\_{\infty}\quad\textrm{with}~~\Theta=\dfrac{\frac{\Delta t}{2}\lambda}{1+\frac{\Delta t}{2}(r+\lambda)-(\kappa\_{x}\frac{\Delta t}{2\Delta x}+\kappa\_{y}\frac{\Delta t}{2\Delta y})}<1. |  |

###### Proof.

From ([4.2](https://arxiv.org/html/2511.01587v1#S4.E2 "In item Crank–Nicolson scheme with fixed-point iteration (CNFI) ‣ 4.2 Temporal schemes for the semidiscretisation approach ‣ 4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) and ([5.3](https://arxiv.org/html/2511.01587v1#S5.E3 "In 5.1 Convergence of CNFI and DIRKFI ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")), we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖εℓ‖∞=‖Vn+1−Yℓ‖∞\displaystyle||\varepsilon\_{\ell}||\_{\infty}=||V^{n+1}-Y\_{\ell}||\_{\infty} | =12​Δ​t​‖(I−12​Δ​t​A)−1​B​(Vn+1−Yℓ−1)‖∞\displaystyle=\tfrac{1}{2}\Delta t||(I-\tfrac{1}{2}\Delta tA)^{-1}B(V^{n+1}-Y\_{\ell-1})||\_{\infty} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤12​Δ​t​‖(I−12​Δ​t​A)−1‖∞​‖B​εℓ−1‖∞.\displaystyle\leq\tfrac{1}{2}\Delta t||(I-\tfrac{1}{2}\Delta tA)^{-1}||\_{\infty}||B\varepsilon\_{\ell-1}||\_{\infty}. |  |

If the matrix I−12​Δ​t​AI-\frac{1}{2}\Delta tA is diagonally dominant, then one has the following bound by Varah ([1975](https://arxiv.org/html/2511.01587v1#bib.bib26)):

|  |  |  |
| --- | --- | --- |
|  | ‖(I−12​Δ​t​A)−1‖∞≤1mini⁡{|ci​i|−∑j≠i|ci​j|},||(I-\tfrac{1}{2}\Delta tA)^{-1}||\_{\infty}\leq\frac{1}{\min\_{i}\{|c\_{ii}|-\sum\_{j\neq i}|c\_{ij}|\}}, |  |

where ci,jc\_{i,j} denote the elements of I−12​Δ​t​AI-\tfrac{1}{2}\Delta tA.

For any given i∈{0,1,…,(m1+1)⋅(m2+1)−1}i\in\{0,1,\ldots,(m\_{1}+1)\cdot(m\_{2}+1)-1\}, there exists a tuple (ki,li)∈{0,1,…,m1}×{0,1,…,m2}(k\_{i},l\_{i})\in\{0,1,\ldots,m\_{1}\}\times\{0,1,\ldots,m\_{2}\} such that

|  |  |  |
| --- | --- | --- |
|  | |ci,i|=|1+12Δt(δiσ2Δ​x2+(r+λ)−|aki|Δ​xw0−|bli|Δ​yw0)|,\displaystyle|c\_{i,i}|=\Bigl|1+\tfrac{1}{2}\Delta t\Bigl(\delta\_{i}\frac{\sigma^{2}}{\Delta x^{2}}+(r+\lambda)-\frac{|a\_{k\_{i}}|}{\Delta x}w\_{0}-\frac{|b\_{l\_{i}}|}{\Delta y}w\_{0}\Bigl)\Bigl|, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ∑j≠i|ci​j|≤12Δt(δiσ2Δ​x2+|aki|Δ​x(|w2|+|w1|+|w−1|)+|bli|Δ​y(|w2|+|w1|+|w−1|)),\displaystyle\sum\_{j\neq i}|c\_{ij}|\leq\tfrac{1}{2}\Delta t\Bigl(\delta\_{i}\frac{\sigma^{2}}{\Delta x^{2}}+\frac{|a\_{k\_{i}}|}{\Delta x}(|w\_{2}|+|w\_{1}|+|w\_{-1}|)+\frac{|b\_{l\_{i}}|}{\Delta y}(|w\_{2}|+|w\_{1}|+|w\_{-1}|)\Bigl), |  |

where δi=1\delta\_{i}=1 if i∈{m2+1,…,m1​(m2+1)−1}i\in\{m\_{2}+1,\ldots,m\_{1}(m\_{2}+1)-1\} and δi=0\delta\_{i}=0 otherwise, which corresponds to the linear boundary condition.

Noting that |w2|+|w1|+|w−1|+w0≥∑k=−12wk=0|w\_{2}|+|w\_{1}|+|w\_{-1}|+w\_{0}\geq\sum\_{k=-1}^{2}w\_{k}=0 and |ci,i|≥ci,i|c\_{i,i}|\geq c\_{i,i}, it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ci,i|−∑j≠i|ci​j|\displaystyle|c\_{i,i}|-\sum\_{j\neq i}|c\_{ij}| | ≥1+12Δt(r+λ)−12Δt(|aki|Δ​x(|w2|+|w1|+|w−1|)+|aki|Δ​xw0)\displaystyle\geq 1+\tfrac{1}{2}\Delta t(r+\lambda)-\tfrac{1}{2}\Delta t\Bigl(\frac{|a\_{k\_{i}}|}{\Delta x}(|w\_{2}|+|w\_{1}|+|w\_{-1}|)+\frac{|a\_{k\_{i}}|}{\Delta x}w\_{0}\Bigl) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −12Δt(|bli|Δ​y(|w2|+|w1|+|w−1|)+|bli|Δ​yw0)\displaystyle\ \qquad\qquad-\tfrac{1}{2}\Delta t\Bigl(\frac{|b\_{l\_{i}}|}{\Delta y}(|w\_{2}|+|w\_{1}|+|w\_{-1}|)+\frac{|b\_{l\_{i}}|}{\Delta y}w\_{0}\Bigl) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥1+12Δt(r+λ)−(κxΔ​t2​Δ​x+κyΔ​t2​Δ​y).\displaystyle\geq 1+\tfrac{1}{2}\Delta t(r+\lambda)-\Bigl(\kappa\_{x}\frac{\Delta t}{2\Delta x}+\kappa\_{y}\frac{\Delta t}{2\Delta y}\Bigl). |  |

If κx​Δ​t2​Δ​x+κy​Δ​t2​Δ​y<1+Δ​t2​r\kappa\_{x}\frac{\Delta t}{2\Delta x}+\kappa\_{y}\frac{\Delta t}{2\Delta y}<1+\frac{\Delta t}{2}r, the matrix I−12​Δ​t​AI-\frac{1}{2}\Delta tA is diagonally dominant and thus

|  |  |  |
| --- | --- | --- |
|  | ‖(I−12​Δ​t​A)−1‖∞≤11+12​Δ​t​(r+λ)−(κx​Δ​t2​Δ​x+κy​Δ​t2​Δ​y).||(I-\tfrac{1}{2}\Delta tA)^{-1}||\_{\infty}\leq\frac{1}{1+\tfrac{1}{2}\Delta t(r+\lambda)-(\kappa\_{x}\frac{\Delta t}{2\Delta x}+\kappa\_{y}\frac{\Delta t}{2\Delta y})}. |  |

By ([3.2](https://arxiv.org/html/2511.01587v1#S3.E2 "In 3.2 Integral part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑ℓ=0m2|B~j,ℓ|\displaystyle\sum\_{\ell=0}^{m\_{2}}|\tilde{B}\_{j,\ell}| | =∑ℓ=0m2−1yℓ+1−yℓΔ​y​∫yℓyℓ+1f​(ξ−yj)​𝑑ξ\displaystyle=\sum\_{\ell=0}^{m\_{2}-1}\frac{y\_{\ell+1}-y\_{\ell}}{\Delta y}\int\_{y\_{\ell}}^{y\_{\ell+1}}f(\xi-y\_{j})d\xi |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑ℓ=0m2−1∫yℓyℓ+1f​(ξ−yj)​𝑑ξ\displaystyle=\sum\_{\ell=0}^{m\_{2}-1}\int\_{y\_{\ell}}^{y\_{\ell+1}}f(\xi-y\_{j})d\xi |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∫−∞∞f​(ξ)​𝑑ξ=1,\displaystyle\leq\int\_{-\infty}^{\infty}f(\xi)d\xi=1, |  |

whenever 0≤j≤m20\leq j\leq m\_{2}, which implies that ‖B‖∞≤λ||B||\_{\infty}\leq\lambda and, hence, ‖B​εℓ−1‖∞≤λ​‖εℓ−1‖∞||B\varepsilon\_{\ell-1}||\_{\infty}\leq\lambda||\varepsilon\_{\ell-1}||\_{\infty}.
  
Combining the above inequalities, we get the stated bound on the error ‖εℓ‖∞||\varepsilon\_{\ell}||\_{\infty}.
∎

In Theorem [5.1](https://arxiv.org/html/2511.01587v1#Thmtheorem1 "Theorem 5.1. ‣ 5.1 Convergence of CNFI and DIRKFI ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"), the sufficient condition for the convergence of the fixed-point iteration takes a CFL-like form, imposing constraints on the time step Δ​t\Delta t and the spatial mesh widths Δ​x\Delta x and Δ​y\Delta y. However, in our numerical experiments in Section [6](https://arxiv.org/html/2511.01587v1#S6 "6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"), no restriction on Δ​t\Delta t was observed for the convergence of the fixed-point iteration.

We remark that for the convergence of the DIRKFI scheme ([4.3](https://arxiv.org/html/2511.01587v1#S4.E3 "In item Diagonally implicit Runge-Kutta scheme with fixed-point iteration (DIRKFI) ‣ 4.2 Temporal schemes for the semidiscretisation approach ‣ 4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) to the DIRK scheme a completely similar result is obtained. For the sake of brevity, we omit the details.

### 5.2 Stability and convergence study

For the purpose of this theoretical investigation, we impose on the PIDE ([2.5](https://arxiv.org/html/2511.01587v1#S2.E5 "In 2.2 Formulation of the problem ‣ 2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) Dirichlet boundary conditions in both directions, thus for some given functions u1u\_{1}, u2u\_{2} and v1v\_{1}, v2v\_{2}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(x−1,y,t)\displaystyle v(x\_{-1},y,t) | =u1​(y,t),v​(xm1+1,y,t)=u2​(y,t),\displaystyle=u\_{1}(y,t),\quad v(x\_{m\_{1}+1},y,t)=u\_{2}(y,t), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v​(x,y−1,t)\displaystyle v(x,y\_{-1},t) | =v1​(x,t),v​(x,ym2+1,t)=v2​(x,t),\displaystyle=v\_{1}(x,t),\quad v(x,y\_{m\_{2}+1},t)=v\_{2}(x,t), |  | (5.4) |

where x−1,xm1+1,y−1,ym2+1x\_{-1},x\_{m\_{1}+1},y\_{-1},y\_{m\_{2}+1} are introduced to be on the boundary of the domain such that xmin=x−1<x0<⋯<xm1<xm1+1=xmaxx\_{\min}=x\_{-1}<x\_{0}<\cdots<x\_{m\_{1}}<x\_{m\_{1}+1}=x\_{\max} and ymin=y−1<y0<⋯<ym2<ym2+1=ymaxy\_{\min}=y\_{-1}<y\_{0}<\cdots<y\_{m\_{2}}<y\_{m\_{2}+1}=y\_{\max} are uniform meshes in the xx- and yy- direction respectively.

Now, the semidiscrete system takes the form

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Vd​t​(t)\displaystyle\frac{dV}{dt}(t) | =(A+B)​V​(t)+g​(t),t>0\displaystyle=(A+B)V(t)+g(t),\quad t>0 |  | (5.5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V​(0)\displaystyle V(0) | =max⁡(x^⊗ey+ex⊗y^−K⋅ex⊗ey,0),\displaystyle=\max(\hat{x}\otimes e\_{y}+e\_{x}\otimes\hat{y}-K\cdot e\_{x}\otimes e\_{y},0), |  | (5.6) |

where x^,y^,ex,ey\hat{x},\hat{y},e\_{x},e\_{y} are defined in Section [3.3.2](https://arxiv.org/html/2511.01587v1#S3.SS3.SSS2 "3.3.2 Semidiscrete approximation ‣ 3.3 Convection part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") and AA and BB are the matrices defined in ([3.11](https://arxiv.org/html/2511.01587v1#S3.E11 "In 3.3.2 Semidiscrete approximation ‣ 3.3 Convection part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) and ([3.2](https://arxiv.org/html/2511.01587v1#S3.E2 "In 3.2 Integral part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) respectively but taking into account the Dirichlet boundary conditions instead of the linear boundary conditions. The vector g​(t)g(t) contains the contribution of the Dirichlet boundary.
  
For the stability study, consider the scaled Euclidean product of two vectors UU and VV of equal size defined by ⟨U,V⟩=Δ​x​Δ​y​∑Uk​Vk\langle U,V\rangle=\Delta x\Delta y\sum U\_{k}V\_{k}
with corresponding ℓ2\ell\_{2}-norm ‖V‖2=⟨V,V⟩||V||\_{2}=\sqrt{\langle V,V\rangle} and recall the formula of the logarithmic norm for an m×mm\times m-matrix BB induced by the ℓ2\ell\_{2}-norm:

|  |  |  |
| --- | --- | --- |
|  | μ2[B]=max{⟨B​V,V⟩⟨V,V⟩∣V∈ℝm,V≠0}.\mu\_{2}[B]=\max\Bigl\{\frac{\langle BV,V\rangle}{\langle V,V\rangle}\mid V\in\mathbb{R}^{m},\;V\neq 0\Bigl\}. |  |

First, three lemmas are stated before the main results of stability and convergence are derived.

###### Lemma 5.2.

For the jump matrix BB, the bound ‖B‖2≤λ​Ly​‖f‖∞||B||\_{2}\leq\lambda\sqrt{L\_{y}||f||\_{\infty}} holds with Ly=ymax−yminL\_{y}=y\_{\max}-y\_{\min}, implying that μ2​[B]≤λ​Ly​‖f‖∞\mu\_{2}[B]\leq\lambda\sqrt{L\_{y}||f||\_{\infty}} where ‖f‖∞=supξ∈ℝ|f​(ξ)|<∞||f||\_{\infty}=\sup\_{\xi\in\mathbb{R}}|f(\xi)|<\infty.

###### Proof.

We recall B=I1⊗λ​B~B=I\_{1}\otimes\lambda\tilde{B} with A~\tilde{A} defined in ([3.2](https://arxiv.org/html/2511.01587v1#S3.E2 "In 3.2 Integral part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")). Using that ‖B~‖∞≤1||\tilde{B}||\_{\infty}\leq 1 (see the proof of Theorem [5.1](https://arxiv.org/html/2511.01587v1#Thmtheorem1 "Theorem 5.1. ‣ 5.1 Convergence of CNFI and DIRKFI ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")), there follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖B‖22=ρ​((B)⊤​B)=λ2​ρ​((B~)⊤​B~)≤λ2​‖B~‖1​‖B~‖∞≤λ2​‖B~‖1.||B||^{2}\_{2}=\rho((B)^{\top}B)\\ =\lambda^{2}\rho((\tilde{B})^{\top}\tilde{B})\\ \leq\lambda^{2}||\tilde{B}||\_{1}||\tilde{B}||\_{\infty}\\ \leq\lambda^{2}||\tilde{B}||\_{1}. |  | (5.7) |

For 0≤j≤m20\leq j\leq m\_{2}, 1≤ℓ≤m2−11\leq\ell\leq m\_{2}-1, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |B~j,ℓ|\displaystyle|\tilde{B}\_{j,\ell}| | =1Δ​y​∫yℓ−1yℓ(ξ−yℓ−1)​f​(ξ−yj)​𝑑ξ+1Δ​y​∫yℓyℓ+1(yℓ+1−ξ)​f​(ξ−yj)​𝑑ξ\displaystyle=\frac{1}{\Delta y}\int\_{y\_{\ell-1}}^{y\_{\ell}}(\xi-y\_{\ell-1})f(\xi-y\_{j})d\xi+\frac{1}{\Delta y}\int\_{y\_{\ell}}^{y\_{\ell+1}}(y\_{\ell+1}-\xi)f(\xi-y\_{j})d\xi |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​‖f‖∞​Δ​y​∫01ξ​𝑑ξ\displaystyle\leq 2||f||\_{\infty}\Delta y\int\_{0}^{1}\xi d\xi |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Δ​y​‖f‖∞.\displaystyle=\Delta y||f||\_{\infty}. |  |

Similarly, we find |B~j,0|≤12​Δ​y​‖f‖∞|\tilde{B}\_{j,0}|\leq\frac{1}{2}\Delta y||f||\_{\infty} and |B~j,m2|≤12​Δ​y​‖f‖∞|\tilde{B}\_{j,m\_{2}}|\leq\frac{1}{2}\Delta y||f||\_{\infty}, leading to
∑j=0m2|B~j,ℓ|≤Ly​‖f‖∞\sum\_{j=0}^{m\_{2}}|\tilde{B}\_{j,\ell}|\leq L\_{y}||f||\_{\infty}. Taking the maximum over ℓ\ell yields ‖B~‖1≤Ly​‖f‖∞||\tilde{B}||\_{1}\leq L\_{y}||f||\_{\infty}. Substitution of the latter bound in the inequality ([5.7](https://arxiv.org/html/2511.01587v1#S5.E7 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) gives the stated result, noticing that μ2​[B]≤‖B‖2\mu\_{2}[B]\leq||B||\_{2}.
∎

###### Lemma 5.3.

Let a~,b~\tilde{a},\tilde{b} be any given real numbers. Let DxD\_{x} be the diagonal matrix given by Dx,i,i=a~−b~​xiD\_{x,i,i}=\tilde{a}-\tilde{b}x\_{i}. Consider any given finite difference scheme of the form ([5.1](https://arxiv.org/html/2511.01587v1#S5.E1 "In 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"))-([5.2](https://arxiv.org/html/2511.01587v1#S5.E2 "In 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) and let A~x\tilde{A}\_{x} denote the corresponding differentiation matrix for the xx-direction, defined analogously to before. Then, the following bound holds:

|  |  |  |
| --- | --- | --- |
|  | μ2​[Dx​A~x]≤(|w−1|−10​w2)​b~\mu\_{2}[D\_{x}\tilde{A}\_{x}]\leq(|w\_{-1}|-10w\_{2})\tilde{b} |  |

The same bound applies in the case of the yy-direction.

###### Proof.

The technical proof of this lemma can be found in Appendix [A](https://arxiv.org/html/2511.01587v1#A1 "Appendix A Proof of Lemma 5.3 ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps").
∎

Denote

|  |  |  |  |
| --- | --- | --- | --- |
|  | C~=(|w−1|−10​w2)​(α+β)−(r+λ)andC^=C~+λ​Ly​‖f‖∞.\widetilde{C}=(|w\_{-1}|-10w\_{2})(\alpha+\beta)-(r+\lambda)\quad\text{and}\quad\widehat{C}=\widetilde{C}+\lambda\sqrt{L\_{y}||f||\_{\infty}}. |  | (5.8) |

###### Lemma 5.4.

The logarithmic ℓ2\ell\_{2}-norm of the matrix AA in ([3.11](https://arxiv.org/html/2511.01587v1#S3.E11 "In 3.3.2 Semidiscrete approximation ‣ 3.3 Convection part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) satisfies the following bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ2​[A]≤C~.\mu\_{2}[A]\leq\widetilde{C}. |  | (5.9) |

###### Proof.

From the formulas ([3.1](https://arxiv.org/html/2511.01587v1#S3.E1 "In 3.1 Diffusion-reaction part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")), ([3.8](https://arxiv.org/html/2511.01587v1#S3.E8 "In 3.3.2 Semidiscrete approximation ‣ 3.3 Convection part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")), ([3.9](https://arxiv.org/html/2511.01587v1#S3.E9 "In 3.3.2 Semidiscrete approximation ‣ 3.3 Convection part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")), ([3.11](https://arxiv.org/html/2511.01587v1#S3.E11 "In 3.3.2 Semidiscrete approximation ‣ 3.3 Convection part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) and properties of the logarithmic norm we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ2​[A]\displaystyle\mu\_{2}[A] | ≤μ2[(σ22D2−(r+λ)I1)⊗I2]+μ2[DxA~x⊗I2]+μ2[I1⊗DyA~y]\displaystyle\leq\mu\_{2}[\Bigl(\frac{\sigma^{2}}{2}D\_{2}-(r+\lambda)I\_{1}\Bigl)\otimes I\_{2}]+\mu\_{2}[D\_{x}\tilde{A}\_{x}\otimes I\_{2}]+\mu\_{2}[I\_{1}\otimes D\_{y}\tilde{A}\_{y}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤σ22​μ2​[D2]−(r+λ)+μ2​[Dx​A~x]+μ2​[Dy​A~y].\displaystyle\leq\frac{\sigma^{2}}{2}\mu\_{2}[D\_{2}]-(r+\lambda)+\mu\_{2}[D\_{x}\tilde{A}\_{x}]+\mu\_{2}[D\_{y}\tilde{A}\_{y}]. |  |

It is easily seen that μ2​[D2]≤0\mu\_{2}[D\_{2}]\leq 0. Thus, by invoking Lemma [5.3](https://arxiv.org/html/2511.01587v1#Thmtheorem3 "Lemma 5.3. ‣ 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"),

|  |  |  |
| --- | --- | --- |
|  | μ2​[A]≤(|w−1|−10​w2)​(α+β)−(r+λ)=C~.\mu\_{2}[A]\leq(|w\_{-1}|-10w\_{2})(\alpha+\beta)-(r+\lambda)=\widetilde{C}. |  |

∎

The CNFI scheme ([4.2](https://arxiv.org/html/2511.01587v1#S4.E2 "In item Crank–Nicolson scheme with fixed-point iteration (CNFI) ‣ 4.2 Temporal schemes for the semidiscretisation approach ‣ 4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) adapted to the case of Dirichlet boundary conditions reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | (I−12​Δ​t​A)​Yℓ=(I+12​Δ​t​A)​Vn+12​Δ​t​(B​Vn+B​Yℓ−1)+12​Δ​t​(gn+gn+1).\big(I-\tfrac{1}{2}\Delta tA\big)Y\_{\ell}=(I+\tfrac{1}{2}\Delta tA)V^{n}+\tfrac{1}{2}\Delta t(BV^{n}+BY\_{\ell-1})+\tfrac{1}{2}\Delta t(g\_{n}+g\_{n+1}). |  | (5.10) |

where gn=g​(n​Δ​t)g\_{n}=g(n\Delta t).
The Crank–Nicolson scheme is given in this case by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (I−12​Δ​t​A)​Vn+1=(I+12​Δ​t​A)​Vn+12​Δ​t​(B​Vn+B​Vn+1)+12​Δ​t​(gn+gn+1).\big(I-\tfrac{1}{2}\Delta tA\big)V^{n+1}=(I+\tfrac{1}{2}\Delta tA)V^{n}+\tfrac{1}{2}\Delta t(BV^{n}+BV^{n+1})+\tfrac{1}{2}\Delta t(g\_{n}+g\_{n+1}). |  | (5.11) |

###### Theorem 5.5.

Let εℓ=Vn+1−Yℓ\varepsilon\_{\ell}=V^{n+1}-Y\_{\ell} where Vn+1V^{n+1} is given by ([5.11](https://arxiv.org/html/2511.01587v1#S5.E11 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) and YℓY\_{\ell} is given by ([5.10](https://arxiv.org/html/2511.01587v1#S5.E10 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")). If C^​Δ​t<2\widehat{C}\Delta t<2, then the CNFI scheme ([5.10](https://arxiv.org/html/2511.01587v1#S5.E10 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) converges to the Crank–Nicolson scheme ([5.11](https://arxiv.org/html/2511.01587v1#S5.E11 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) in the ℓ2\ell\_{2}-norm and

|  |  |  |
| --- | --- | --- |
|  | ‖εℓ‖2≤Θ​‖εℓ−1‖2with​Θ=12​Δ​t​λ​Ly​‖f‖∞1−12​Δ​t​C~<1.||\varepsilon\_{\ell}||\_{2}\leq\Theta\,||\varepsilon\_{\ell-1}||\_{2}\quad\textrm{with}~~\Theta=\frac{\tfrac{1}{2}\Delta t\lambda\sqrt{L\_{y}||f||\_{\infty}}}{1-\tfrac{1}{2}\Delta t\widetilde{C}}<1. |  |

###### Proof.

Subtracting ([5.10](https://arxiv.org/html/2511.01587v1#S5.E10 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) from ([5.11](https://arxiv.org/html/2511.01587v1#S5.E11 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖εℓ‖2=‖Vn+1−Yℓ‖2\displaystyle||\varepsilon\_{\ell}||\_{2}=||V^{n+1}-Y\_{\ell}||\_{2} | =12​Δ​t​‖(I−12​Δ​t​A)−1​B​(Vn+1−Yℓ−1)‖2\displaystyle=\tfrac{1}{2}\Delta t||(I-\tfrac{1}{2}\Delta tA)^{-1}B(V^{n+1}-Y\_{\ell-1})||\_{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤12​Δ​t​‖(I−12​Δ​t​A)−1‖2​‖B‖2​‖εℓ−1‖2.\displaystyle\leq\tfrac{1}{2}\Delta t||(I-\tfrac{1}{2}\Delta tA)^{-1}||\_{2}||B||\_{2}||\varepsilon\_{\ell-1}||\_{2}. |  |

By Lemma [5.4](https://arxiv.org/html/2511.01587v1#Thmtheorem4 "Lemma 5.4. ‣ 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"), we have Δ​t2​μ2​[A]≤Δ​t2​C~<1\frac{\Delta t}{2}\mu\_{2}[A]\leq\frac{\Delta t}{2}\widetilde{C}<1. Hence, by von Neumann theorem, see Hairer and Wanner [1996](https://arxiv.org/html/2511.01587v1#bib.bib11), Section IV.11,

|  |  |  |
| --- | --- | --- |
|  | ‖(I−12​Δ​t​A)−1‖2≤11−12​Δ​t​μ2​[A]≤11−12​Δ​t​C~.||(I-\tfrac{1}{2}\Delta tA)^{-1}||\_{2}\leq\frac{1}{1-\tfrac{1}{2}\Delta t\mu\_{2}[A]}\leq\frac{1}{1-\tfrac{1}{2}\Delta t\widetilde{C}}. |  |

Combining this with the bound of Lemma [5.2](https://arxiv.org/html/2511.01587v1#Thmtheorem2 "Lemma 5.2. ‣ 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") for ‖B‖2||B||\_{2} and using ([5.8](https://arxiv.org/html/2511.01587v1#S5.E8 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")), we arrive at the stated result.
∎

The theorem above addresses the convergence of the fixed-point iteration in the ℓ2\ell\_{2}-norm and differs from Theorem [5.1](https://arxiv.org/html/2511.01587v1#Thmtheorem1 "Theorem 5.1. ‣ 5.1 Convergence of CNFI and DIRKFI ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"), which deals with its convergence in the ℓ∞\ell\_{\infty}-norm.
Since convergence in the ℓ∞\ell\_{\infty}-norm is a stronger requirement, it leads to a more restrictive CFL-like condition involving both the time step Δ​t\Delta t and spatial mesh widths Δ​x\Delta x and Δ​y\Delta y. On the other hand, the ℓ2\ell\_{2}-norm analysis guarantees convergence under a milder condition, imposing a restriction only on the time step Δ​t\Delta t.
We remark again that for the convergence of the DIRKFI scheme ([4.3](https://arxiv.org/html/2511.01587v1#S4.E3 "In item Diagonally implicit Runge-Kutta scheme with fixed-point iteration (DIRKFI) ‣ 4.2 Temporal schemes for the semidiscretisation approach ‣ 4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) to the DIRK scheme a completely similar result is obtained.

We focus now on the stability and convergence of the Crank–Nicolson scheme ([5.11](https://arxiv.org/html/2511.01587v1#S5.E11 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")). The stability function of the Crank–Nicolson scheme is

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​(z)=1+12​z1−12​z(z∈ℂ).R(z)=\frac{1+\frac{1}{2}z}{1-\frac{1}{2}z}\quad(z\in\mathbb{C}). |  | (5.12) |

Let G​(x)=supR​e​(z)≤x|R​(z)|G(x)=\sup\_{Re(z)\leq x}|R(z)| be the so-called error growth function. It is known that, see Hairer and Wanner ([1996](https://arxiv.org/html/2511.01587v1#bib.bib11)),

|  |  |  |
| --- | --- | --- |
|  | G​(x)≤{1if ​x≤01+2​xif ​0≤x≤1.G(x)\leq\begin{cases}1&\text{if }x\leq 0\\ 1+2x&\text{if }0\leq x\leq 1.\end{cases} |  |

###### Theorem 5.6.

Let C^+=max⁡(C^,0)\widehat{C}^{+}=\max(\widehat{C},0). The Crank–Nicolson scheme in ([5.11](https://arxiv.org/html/2511.01587v1#S5.E11 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) is unconditionally stable in the ℓ2\ell\_{2}-norm:

|  |  |  |
| --- | --- | --- |
|  | ‖R​(Δ​t​(A+B))‖2n≤e2​T​C^+​whenevern=0,1,2,…,with​n​Δ​t≤T,C^​Δ​t≤1.||R(\Delta t(A+B))||^{n}\_{2}\leq e^{2T\widehat{C}^{+}}\;\text{whenever}\quad n=0,1,2,\ldots,\;\text{with}\;n\Delta t\leq T,\;\;\hat{C}\Delta t\leq 1. |  |

###### Proof.

From Lemmas [5.2](https://arxiv.org/html/2511.01587v1#Thmtheorem2 "Lemma 5.2. ‣ 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") and [5.4](https://arxiv.org/html/2511.01587v1#Thmtheorem4 "Lemma 5.4. ‣ 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"), we get μ2​[Δ​t​(A+B)]≤Δ​t​C^\mu\_{2}[\Delta t(A+B)]\leq\Delta t\widehat{C}. Then, by von Neumann theorem, see Hairer and Wanner [1996](https://arxiv.org/html/2511.01587v1#bib.bib11), Section IV.11,

|  |  |  |
| --- | --- | --- |
|  | ‖R​(Δ​t​(A+B))‖2≤G​(C^​Δ​t)≤G​(C^+​Δ​t).||R(\Delta t(A+B))||\_{2}\leq G(\hat{C}\Delta t)\leq G(\hat{C}^{+}\Delta t). |  |

Thus,

|  |  |  |
| --- | --- | --- |
|  | ‖R​(Δ​t​(A+B))‖2n≤(1+2​Δ​t​C^+)n≤e2​T​C^+.||R(\Delta t(A+B))||^{n}\_{2}\leq(1+2\Delta t\widehat{C}^{+})^{n}\leq e^{2T\widehat{C}^{+}}. |  |

∎

Theorem [5.6](https://arxiv.org/html/2511.01587v1#Thmtheorem6 "Theorem 5.6. ‣ 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") establishes the stability of the Crank–Nicolson scheme in the ℓ2\ell\_{2}-norm. In the following, we turn to the study of its convergence under the assumption of sufficient smoothness of the exact solution. The proof of the subsequent theorem follows along the lines of Hundsdorfer and Verwer ([2003](https://arxiv.org/html/2511.01587v1#bib.bib13)). A convergence analysis without the smoothness assumption typically requires monotonicity of the scheme and relies upon the framework of viscosity solutions, see Barles and Souganidis ([1991](https://arxiv.org/html/2511.01587v1#bib.bib1)). This aspect will be addressed in future research.

Denote

|  |  |  |
| --- | --- | --- |
|  | vΔ​x,Δ​y​(t)=(v​(x0,y0,t),v​(x0,y1,t),…,v​(xm1,ym2−1,t),v​(xm1,ym2,t))∈ℝ(m1+1)​(m2+1).v\_{\Delta x,\Delta y}(t)=(v(x\_{0},y\_{0},t),v(x\_{0},y\_{1},t),\ldots,v(x\_{m\_{1}},y\_{m\_{2}-1},t),v(x\_{m\_{1}},y\_{m\_{2}},t))\in\mathbb{R}^{(m\_{1}+1)(m\_{2}+1)}. |  |

###### Theorem 5.7.

Under sufficient smoothness of vΔ​x,Δ​yv\_{\Delta x,\Delta y} and second-order consistency of the semidiscretisation, the Crank–Nicolson scheme ([5.11](https://arxiv.org/html/2511.01587v1#S5.E11 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) applied to the semidiscrete system ([5.5](https://arxiv.org/html/2511.01587v1#S5.E5 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) is convergent in the ℓ2\ell\_{2}-norm. Moreover, the global spatial-temporal error ϵ^n=vΔ​x,Δ​y​(tn)−Vn\hat{\epsilon}\_{n}=v\_{\Delta x,\Delta y}(t\_{n})-V^{n} satisfies the following bound for some positive constant CC:

|  |  |  |
| --- | --- | --- |
|  | ‖ϵ^n‖2≤C​(Δ​t2+Δ​x2+Δ​y2)​whenevern=0,1,2,…,with​n​Δ​t≤T,C^​Δ​t≤1.||\hat{\epsilon}\_{n}||\_{2}\leq C(\Delta t^{2}+\Delta x^{2}+\Delta y^{2})\;\text{whenever}\quad n=0,1,2,\ldots,\;\text{with}\;n\Delta t\leq T,\;\;\hat{C}\Delta t\leq 1. |  |

###### Proof.

The Crank–Nicolson scheme ([5.11](https://arxiv.org/html/2511.01587v1#S5.E11 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) can be written as:

|  |  |  |
| --- | --- | --- |
|  | Vn+1=R​(Δ​t​(A+B))​Vn+12​Δ​t​(I−12​Δ​t​(A+B))−1​(gn+gn+1).V^{n+1}=R(\Delta t(A+B))V^{n}+\tfrac{1}{2}\Delta t(I-\tfrac{1}{2}\Delta t(A+B))^{-1}(g\_{n}+g\_{n+1}). |  |

Let the local spatial-temporal error δ^n+1\hat{\delta}\_{n+1} be defined by

|  |  |  |
| --- | --- | --- |
|  | vΔ​x,Δ​y​(tn+1)=R​(Δ​t​(A+B))​vΔ​x,Δ​y​(tn)+12​Δ​t​(I−12​Δ​t​(A+B))−1​(gn+gn+1)+δ^n+1.v\_{\Delta x,\Delta y}(t\_{n+1})=R(\Delta t(A+B))v\_{\Delta x,\Delta y}(t\_{n})+\tfrac{1}{2}\Delta t(I-\tfrac{1}{2}\Delta t(A+B))^{-1}(g\_{n}+g\_{n+1})+\hat{\delta}\_{n+1}. |  |

Subtracting the two equalities and noting that ϵ^0=0\hat{\epsilon}\_{0}=0 leads to

|  |  |  |
| --- | --- | --- |
|  | ϵ^n+1=R​(Δ​t​(A+B))​ϵ^n+δ^n+1=⋯=∑i=1n+1R​(Δ​t​(A+B))n+1−i​δ^i.\hat{\epsilon}\_{n+1}=R(\Delta t(A+B))\hat{\epsilon}\_{n}+\hat{\delta}\_{n+1}=\cdots=\sum\_{i=1}^{n+1}R(\Delta t(A+B))^{n+1-i}\hat{\delta}\_{i}. |  |

Then, by virtue of Theorem [5.6](https://arxiv.org/html/2511.01587v1#Thmtheorem6 "Theorem 5.6. ‣ 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ϵ^n+1‖2≤e2​T​C^+​(n+1)​max1≤i≤n+1​‖δ^i‖2.||\hat{\epsilon}\_{n+1}||\_{2}\leq e^{2T\widehat{C}^{+}}(n+1)\max\_{1\leq i\leq n+1}||\hat{\delta}\_{i}||\_{2}. |  | (5.13) |

For any integer i≥0i\geq 0 with (i+1)​Δ​t≤T(i+1)\Delta t\leq T, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ^i+1\displaystyle\hat{\delta}\_{i+1} | =12​Δ​t​(I−12​Δ​t​(A+B))−1​(δ​(ti)+δ​(ti+1))\displaystyle=\tfrac{1}{2}\Delta t(I-\tfrac{1}{2}\Delta t(A+B))^{-1}(\delta(t\_{i})+\delta(t\_{i+1})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(I−12Δt(A+B))−1(vΔ​x,Δ​y(ti+1)−vΔ​x,Δ​y(ti)−12Δt(d​vΔ​x,Δ​yd​t(ti+1)+d​vΔ​x,Δ​yd​t(ti))),\displaystyle\quad+(I-\tfrac{1}{2}\Delta t(A+B))^{-1}\Bigl(v\_{\Delta x,\Delta y}(t\_{i+1})-v\_{\Delta x,\Delta y}(t\_{i})-\tfrac{1}{2}\Delta t\Bigl(\frac{dv\_{\Delta x,\Delta y}}{dt}(t\_{i+1})+\frac{dv\_{\Delta x,\Delta y}}{dt}(t\_{i})\Bigl)\Bigl), |  |

where

|  |  |  |
| --- | --- | --- |
|  | δ​(t)=d​vΔ​x,Δ​yd​t​(t)−(A+B)​vΔ​x,Δ​y​(t)−g​(t)\delta(t)=\frac{dv\_{\Delta x,\Delta y}}{dt}(t)-(A+B)v\_{\Delta x,\Delta y}(t)-g(t) |  |

denotes the local spatial error.
  
By the smoothness assumption on vΔ​x,Δ​yv\_{\Delta x,\Delta y}, Taylor expansion yields for some positive constant C1C\_{1} (independent of ii, Δ​t\Delta t, Δ​x\Delta x, Δ​y\Delta y) that

|  |  |  |
| --- | --- | --- |
|  | ‖vΔ​x,Δ​y​(ti+1)−vΔ​x,Δ​y​(ti)−12​Δ​t​(d​vΔ​x,Δ​yd​t​(ti+1)+d​vΔ​x,Δ​yd​t​(ti))‖2≤C1​Δ​t3.\|v\_{\Delta x,\Delta y}(t\_{i+1})-v\_{\Delta x,\Delta y}(t\_{i})-\tfrac{1}{2}\Delta t\Bigl(\frac{dv\_{\Delta x,\Delta y}}{dt}(t\_{i+1})+\frac{dv\_{\Delta x,\Delta y}}{dt}(t\_{i})\Bigr)\|\_{2}\leq C\_{1}\Delta t^{3}. |  |

The semidiscretisation is consistent of second-order, i.e., by definition there exists a positive constant C2C\_{2} (independent of ii, Δ​x\Delta x, Δ​y\Delta y) such that

|  |  |  |
| --- | --- | --- |
|  | ‖δ​(ti+1)‖2<C2​(Δ​x2+Δ​y2).||\delta(t\_{i+1})||\_{2}<C\_{2}(\Delta x^{2}+\Delta y^{2}). |  |

It follows that there exists a positive constant C3C\_{3} (independent of ii, Δ​t\Delta t, Δ​x\Delta x, Δ​y\Delta y) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖δ^i+1‖2≤C3​Δ​t​‖(I−12​Δ​t​(A+B))−1‖2​(Δ​t2+Δ​x2+Δ​y2).||\hat{\delta}\_{i+1}||\_{2}\leq C\_{3}\Delta t||(I-\tfrac{1}{2}\Delta t(A+B))^{-1}||\_{2}(\Delta t^{2}+\Delta x^{2}+\Delta y^{2}). |  | (5.14) |

From Lemmas [5.2](https://arxiv.org/html/2511.01587v1#Thmtheorem2 "Lemma 5.2. ‣ 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") and [5.4](https://arxiv.org/html/2511.01587v1#Thmtheorem4 "Lemma 5.4. ‣ 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"), we have: μ2​[12​Δ​t​(A+B)]≤12​Δ​t​C^\mu\_{2}[\tfrac{1}{2}\Delta t(A+B)]\leq\tfrac{1}{2}\Delta t\widehat{C}. Thus, if C^​Δ​t≤1\widehat{C}\Delta t\leq 1, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖(I−12​Δ​t​(A+B))−1‖2≤11−12​Δ​t​C^≤2.||(I-\tfrac{1}{2}\Delta t(A+B))^{-1}||\_{2}\leq\frac{1}{1-\frac{1}{2}\Delta t\widehat{C}}\leq 2. |  | (5.15) |

Combining the bounds ([5.13](https://arxiv.org/html/2511.01587v1#S5.E13 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")), ([5.14](https://arxiv.org/html/2511.01587v1#S5.E14 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) and ([5.15](https://arxiv.org/html/2511.01587v1#S5.E15 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) gives

|  |  |  |
| --- | --- | --- |
|  | ‖ϵ^n‖2≤2​T​e2​T​C^+​C3​(Δ​t2+Δ​x2+Δ​y2).||\hat{\epsilon}\_{n}||\_{2}\leq 2Te^{2T\widehat{C}^{+}}C\_{3}(\Delta t^{2}+\Delta x^{2}+\Delta y^{2}). |  |

∎

Our next step is the study of the stability of the DIRK scheme:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {W1=Vn+(1−θ)​Δ​t​(A​Vn+B​Vn),(I−θ​Δ​t​A)​V^n+1=W1+θ​Δ​t​B​V^n+1+Δ​t​((1−θ)​gn+θ​gn+1),W2=Vn+12​Δ​t​(A​Vn+B​Vn)+(12−θ)​Δ​t​(A​V^n+1+B​V^n+1),(I−θ​Δ​t​A)​Vn+1=W2+θ​Δ​t​B​Vn+1+12​Δ​t​(gn+gn+1).\begin{cases}W\_{1}=V^{n}+(1-\theta)\Delta t(AV^{n}+BV^{n}),\\ (I-\theta\Delta tA)\hat{V}^{n+1}=W\_{1}+\theta\Delta tB\hat{V}^{n+1}+\Delta t((1-\theta)g\_{n}+\theta g\_{n+1}),\\ W\_{2}=V^{n}+\tfrac{1}{2}\Delta t(AV^{n}+BV^{n})+(\tfrac{1}{2}-\theta)\Delta t(A\hat{V}^{n+1}+B\hat{V}^{n+1}),\\ (I-\theta\Delta tA)V^{n+1}=W\_{2}+\theta\Delta tBV^{n+1}+\tfrac{1}{2}\Delta t(g\_{n}+g\_{n+1}).\end{cases} |  | (5.16) |

The stability function of the DIRK scheme is

|  |  |  |
| --- | --- | --- |
|  | Rθ​(z)=1+(1−2​θ)​z+(12−2​θ+θ2)​z2(1−θ​z)2(z∈ℂ),R\_{\theta}(z)=\frac{1+(1-2\theta)z+(\frac{1}{2}-2\theta+\theta^{2})z^{2}}{(1-\theta z)^{2}}\quad(z\in\mathbb{C}), |  |

which is AA-stable whenever θ≥14\theta\geq\frac{1}{4} (see, e.g., Cash ([1984](https://arxiv.org/html/2511.01587v1#bib.bib6))).
The following lemma is key to the proof of the stability of the scheme.
Define the error growth function of the DIRK scheme by Gθ​(x)=supR​e​(z)≤x|Rθ​(z)|G\_{\theta}(x)=\sup\_{Re(z)\leq x}|R\_{\theta}(z)|.

###### Lemma 5.8.

Let θ∈[14,12]\theta\in[\frac{1}{4},\frac{1}{2}] and ν∈]0,1θ[\nu\in\,]0,\frac{1}{\theta}[. Then,

|  |  |  |
| --- | --- | --- |
|  | {Gθ​(x)≤1if ​x≤0,Gθ​(x)=Rθ​(x)if ​ 0≤x<1θ.\begin{cases}G\_{\theta}(x)\leq 1&\text{if }\,x\leq 0,\\ G\_{\theta}(x)=R\_{\theta}(x)&\text{if }\,0\leq x<\frac{1}{\theta}.\end{cases} |  |

Moreover,

|  |  |  |
| --- | --- | --- |
|  | Gθ​(x)≤1+Rθ​(ν)−1ν​x for ​ 0≤x≤ν<1θ.G\_{\theta}(x)\leq 1+\frac{R\_{\theta}(\nu)-1}{\nu}\,x\quad\text{ for }\,0\leq x\leq\nu<\frac{1}{\theta}. |  |

###### Proof.

The technical proof of this lemma is given in Appendix [B](https://arxiv.org/html/2511.01587v1#A2 "Appendix B Proof of Lemma 5.8 ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps").
∎

Now, we can derive the following stability result for the DIRK scheme.

###### Theorem 5.9.

Let θ∈[14,12]\theta\in[\frac{1}{4},\frac{1}{2}] and ν∈]0,1θ[\nu\in\,]0,\frac{1}{\theta}[. The DIRK scheme ([5.16](https://arxiv.org/html/2511.01587v1#S5.E16 "In 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) is unconditionally stable in the ℓ2\ell\_{2}-norm:

|  |  |  |
| --- | --- | --- |
|  | ‖Rθ​(Δ​t​(A+B))‖2n≤eγ​T​C^+​whenevern=0,1,2,…,with​n​Δ​t≤T,C^​Δ​t≤ν,||R\_{\theta}(\Delta t(A+B))||\_{2}^{n}\leq e^{\gamma T\widehat{C}^{+}}\;\text{whenever}\quad n=0,1,2,\ldots,\;\text{with}\;n\Delta t\leq T,\;\;\widehat{C}\Delta t\leq\nu, |  |

where γ\gamma is a constant independent of Δ​t\Delta t, Δ​x\Delta x and Δ​y\Delta y.

###### Proof.

There holds

|  |  |  |
| --- | --- | --- |
|  | ‖Rθ​(Δ​t​(A+B))‖2≤Gθ​(C^​Δ​t)≤Gθ​(C^+​Δ​t).||R\_{\theta}(\Delta t(A+B))||\_{2}\leq G\_{\theta}(\widehat{C}\Delta t)\leq G\_{\theta}(\widehat{C}^{+}\Delta t). |  |

Let γ=Rθ​(ν)−1ν\gamma=\frac{R\_{\theta}(\nu)-1}{\nu}. Applying Lemma [5.8](https://arxiv.org/html/2511.01587v1#Thmtheorem8 "Lemma 5.8. ‣ 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") yields ‖Rθ​(Δ​t​(A+B))‖2n≤(1+γ​C^+​Δ​t)n≤eγ​T​C^+||R\_{\theta}(\Delta t(A+B))||\_{2}^{n}\leq(1+\gamma\widehat{C}^{+}\Delta t)^{n}\leq e^{\gamma T\widehat{C}^{+}}.
∎

## 6 Numerical experiments

In this section, we present a series of numerical experiments for the case of European call and swing options.
The main objective is to experimentally validate the proposed numerical schemes. For the European call option, we investigate the convergence behaviour of the total and temporal errors, see Section [6.2](https://arxiv.org/html/2511.01587v1#S6.SS2 "6.2 Convergence behaviour: European call option ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"), which gives us an indication of the convergence behaviour for swing options. The study for swing options will be focused on the convergence behaviour of the temporal error, see Section [6.4](https://arxiv.org/html/2511.01587v1#S6.SS4 "6.4 Convergence behaviour: swing options ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps").
The parameter sets employed in the numerical experiments are detailed in Section [6.1](https://arxiv.org/html/2511.01587v1#S6.SS1 "6.1 Financial parameter values ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps").

We apply cell averaging in the definition of the initial vector V​(0)=V0V(0)=V^{0} corresponding to the option payoff, because relying fully on its pointwise evaluation can lead to a deteriorated spatial convergence behaviour. Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi+1/2=12​(xi+xi+1)\displaystyle x\_{i+1/2}=\frac{1}{2}(x\_{i}+x\_{i+1}) | andyj+1/2=12​(yj+yj+1)\displaystyle\quad\text{and}\quad y\_{j+1/2}=\frac{1}{2}(y\_{j}+y\_{j+1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​xi+1/2=xi+1/2−xi−1/2\displaystyle\Delta x\_{i+1/2}=x\_{i+1/2}-x\_{i-1/2} | andΔ​yj+1/2=xj+1/2−xj−1/2,\displaystyle\quad\text{and}\quad\Delta y\_{j+1/2}=x\_{j+1/2}-x\_{j-1/2}, |  |

with x−1/2=2​x0−x1/2x\_{-1/2}=2x\_{0}-x\_{1/2}, xm1+1/2=xm1x\_{m\_{1}+1/2}=x\_{m\_{1}} and y−1/2=2​y0−y1/2y\_{-1/2}=2y\_{0}-y\_{1/2}, ym2+1/2=ym2y\_{m\_{2}+1/2}=y\_{m\_{2}}. Then, we define

|  |  |  |
| --- | --- | --- |
|  | Vi,j​(0)=1Δ​xi+1/2​Δ​yj+1/2​∫xi−1/2xi+1/2∫yj−1/2yj+1/2max⁡{x+y−K,0}​𝑑x​𝑑yV\_{i,j}(0)=\frac{1}{\Delta x\_{i+1/2}\Delta y\_{j+1/2}}\int\_{x\_{i-1/2}}^{x\_{i+1/2}}\int\_{y\_{j-1/2}}^{y\_{j+1/2}}\max\{x+y-K,0\}dxdy |  |

whenever the cell [xi−1/2,xi+1/2[×[yj−1/2,yj+1/2[[x\_{i-1/2},x\_{i+1/2}[\times[y\_{j-1/2},y\_{j+1/2}[ has a non-empty intersection with the line segment x+y=Kx+y=K.

To solve the linear systems arising in each time step of the temporal discretisation schemes, we adopt different strategies, depending on the approach. In the semi-Lagrangian approach, the resulting linear system involves the simple tridiagonal matrix I−12​Δ​t​ADI-\tfrac{1}{2}\Delta tA^{D}, which allows for an efficient direct solution via LU factorisation. In contrast, in the semidiscretisation approach, we use the BiCGSTAB iterative method to solve the pertinent linear systems. To enhance its convergence, an incomplete LU threshold pivoting (ILUTP) preconditioner is applied. The initial guess for the BiCGSTAB iteration corresponding to the solution at time level nn is taken as Vn−1V^{n-1} from the previous time level.
All the computations have been made using Matlab version R2024b, on an Intel 13th Gen Intel(R) Core(TM) i7-1370P 1.90 GHz with 16 GB memory.

### 6.1 Financial parameter values

For the numerical experiments, the parameter values in the PIDEs ([2.4](https://arxiv.org/html/2511.01587v1#S2.E4 "In 2.2 Formulation of the problem ‣ 2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) and ([2.5](https://arxiv.org/html/2511.01587v1#S2.E5 "In 2.2 Formulation of the problem ‣ 2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) are chosen to reflect reasonable electricity price behaviour. Every parameter value corresponds to a yearly time scale.

In this section, the mean reversion level μ\mu is assumed to be constant and equal to 8080. This value is close to the average electricity price over the year 2024 in the Belgian market (EUR/MWh).
The half-life of the processes X−μX-\mu and YY, defined as the time required for them to revert to half of their values, can reasonably be estimated as 30/365 years and 2/365 years, respectively. Using the half-life formula Hα=ln⁡(2)αH\_{\alpha}=\frac{\ln(2)}{\alpha} and Hβ=ln⁡(2)βH\_{\beta}=\frac{\ln(2)}{\beta} leads to α≈8\alpha\approx 8 and β≈126\beta\approx 126.
For the volatility σ\sigma, we assume that the stationary variance of the process XX, given by σ22​α​(1−e−2​α)≈σ22​α\frac{\sigma^{2}}{2\alpha}(1-e^{-2\alpha})\approx\frac{\sigma^{2}}{2\alpha}, is approximately 10%10\% of the average price μ\mu. Hence, σ=μ​α5≈11\sigma=\sqrt{\frac{\mu\alpha}{5}}\approx 11.
Next, assuming an average of one jump per week, we set λ=52\lambda=52.

To test the numerical robustness of the schemes and to check that they perform well also for more extreme market values, we consider additional sets of parameters where there is a higher volatility σ\sigma and more frequent occurrences of jumps (larger λ\lambda) as well as lower volatility combined with fewer occurrences of jumps (smaller λ\lambda).
We deal with two finite activity jump models characterised by the following jump density functions:

* •

  Merton-type jump, with a normally distributed jump size:

  |  |  |  |
  | --- | --- | --- |
  |  | f​(y)=1σJ​2​π​exp⁡(−(y−μJ)22​σJ2)(y∈ℝ),f(y)=\frac{1}{\sigma\_{J}\sqrt{2\pi}}\exp\left(-\frac{(y-\mu\_{J})^{2}}{2\sigma\_{J}^{2}}\right)\quad(y\in\mathbb{R}), |  |

  where μJ\mu\_{J} and σJ\sigma\_{J} denote the mean and standard deviation of the jump sizes, respectively.
* •

  Kou-type jump, with a double-exponential distribution:

  |  |  |  |
  | --- | --- | --- |
  |  | f​(y)=p​η1​e−η1​y​𝟏{y≥0}+(1−p)​η2​eη2​y​𝟏{y<0}(y∈ℝ),f(y)=p\eta\_{1}e^{-\eta\_{1}y}\mathbf{1}\_{\{y\geq 0\}}+(1-p)\eta\_{2}e^{\eta\_{2}y}\mathbf{1}\_{\{y<0\}}\quad(y\in\mathbb{R}), |  |

  where p∈[0,1]p\in[0,1] is the probability of an upward jump, and η1,η2>0\eta\_{1},\eta\_{2}>0 control the decay rates of the jump sizes in the positive and negative directions, respectively.

The jump parameter values are selected to allow for significant spikes in the asset price. Accordingly, the truncation of the domain in the yy-direction is taken to be sufficiently large to accurately capture the influence of such large jumps.

Table 1: Parameter sets for the Merton-type jump case. The time is measured in years.

| parameters | μ\mu | α\alpha | β\beta | σ\sigma | rr | λ\lambda | μJ\mu\_{J} | σJ\sigma\_{J} | KK | xminx\_{\min} | xmaxx\_{\max} | yminy\_{\min} | ymaxy\_{\max} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Set 1 | 80 | 8 | 126 | 11 | 0.03 | 52 | 20 | 60 | 50 | -2KK | 5KK | -15KK | 15KK |
| Set 2 | 80 | 8 | 126 | 20 | 0.03 | 100 | 20 | 60 | 50 | -2KK | 5KK | -15KK | 15KK |
| Set 3 | 80 | 8 | 126 | 2 | 0.03 | 10 | 20 | 60 | 50 | -2KK | 5KK | -15KK | 15KK |




Table 2: Parameter sets with Kou-type jump case. The time is measured in years.

| parameters | μ\mu | α\alpha | β\beta | σ\sigma | rr | λ\lambda | pp | η1\eta\_{1} | η2\eta\_{2} | KK | xminx\_{\min} | xmaxx\_{\max} | yminy\_{\min} | ymaxy\_{\max} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Set 4 | 80 | 8 | 126 | 11 | 0.03 | 52 | 0.6 | 0.01 | 0.02 | 50 | -2KK | 5KK | -20KK | 20KK |
| Set 5 | 80 | 8 | 126 | 20 | 0.03 | 100 | 0.6 | 0.01 | 0.02 | 50 | -2KK | 5KK | -20KK | 20KK |
| Set 6 | 80 | 8 | 126 | 2 | 0.03 | 10 | 0.6 | 0.01 | 0.02 | 50 | -2KK | 5KK | -20KK | 20KK |

### 6.2 Convergence behaviour: European call option

In this section, we numerically examine the convergence behaviour of the three schemes formulated in Section [4](https://arxiv.org/html/2511.01587v1#S4 "4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") in the case of a European call option for the six different parameter sets given by Tables [1](https://arxiv.org/html/2511.01587v1#S6.T1 "Table 1 ‣ 6.1 Financial parameter values ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") and [2](https://arxiv.org/html/2511.01587v1#S6.T2 "Table 2 ‣ 6.1 Financial parameter values ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"). We take the number of the spatial grid points m1=m2=mm\_{1}=m\_{2}=m and consider two types of discretisation errors:

* •

  The *total discretisation error* on the region of interest defined by

  |  |  |  |
  | --- | --- | --- |
  |  | ET​(N,m)=max⁡{|Vi,jN−v​(xi,yj,T)|∣(xi,yj)∈[−12​K,32​K]×[−K,K]}.E\_{T}(N,m)=\max\{|V^{N}\_{i,j}-v(x\_{i},y\_{j},T)|\mid(x\_{i},y\_{j})\in[-\frac{1}{2}K,\frac{3}{2}K]\times[-K,K]\}. |  |

  We will study this error for a sequence of values NN and mm that are directly proportional to each other. More precisely, we take N=⌈m2⌉N=\left\lceil{\frac{m}{2}}\right\rceil and consider the total error for 2020 different values of mm between 5050 and 500500. The reference solution for v​(⋅,⋅,T)v(\cdot,\cdot,T) is computed by applying the CNFI scheme ([4.2](https://arxiv.org/html/2511.01587v1#S4.E2 "In item Crank–Nicolson scheme with fixed-point iteration (CNFI) ‣ 4.2 Temporal schemes for the semidiscretisation approach ‣ 4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) with N=m=1500N=m=1500.
* •

  The *temporal discretisation error* defined by

  |  |  |  |
  | --- | --- | --- |
  |  | E​(N,m)=max⁡{|Vi,jN−Vi,j​(T)|∣0≤i,j≤m}.E(N,m)=\max\{|V^{N}\_{i,j}-V\_{i,j}(T)|\mid 0\leq i,j\leq m\}. |  |

  For this discretisation error, we consider only the semidiscretisation approach, excluding the semi-Lagrangian approach, as for the latter the temporal error is not clearly defined. A reference solution for V​(T)V(T) is computed by applying the CNFI scheme with N=6000N=6000 time steps. The temporal error is considered for 2020 different values of NN between 100100 and 10001000. For the number of spatial grid points, m=200m=200 is taken.

The maturity time for the European call option is set to T=110T=\frac{1}{10} in agreement with the small interval between two consecutive action times in the case of swing options.

The results for the total and temporal errors are displayed in Figures [2](https://arxiv.org/html/2511.01587v1#S6.F2 "Figure 2 ‣ 6.2 Convergence behaviour: European call option ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") and [4](https://arxiv.org/html/2511.01587v1#S6.F4 "Figure 4 ‣ 6.2 Convergence behaviour: European call option ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") for the Merton-type jump model and in Figures [3](https://arxiv.org/html/2511.01587v1#S6.F3 "Figure 3 ‣ 6.2 Convergence behaviour: European call option ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") and [5](https://arxiv.org/html/2511.01587v1#S6.F5 "Figure 5 ‣ 6.2 Convergence behaviour: European call option ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") for the Kou-type jump model. The numerical schemes considered are SLCNFI ([4.1](https://arxiv.org/html/2511.01587v1#S4.E1 "In 4.1 Temporal scheme for the semi-Lagrangian approach ‣ 4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")), CNFI ([4.2](https://arxiv.org/html/2511.01587v1#S4.E2 "In item Crank–Nicolson scheme with fixed-point iteration (CNFI) ‣ 4.2 Temporal schemes for the semidiscretisation approach ‣ 4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")), and DIRKFI ([4.3](https://arxiv.org/html/2511.01587v1#S4.E3 "In item Diagonally implicit Runge-Kutta scheme with fixed-point iteration (DIRKFI) ‣ 4.2 Temporal schemes for the semidiscretisation approach ‣ 4 Temporal discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) with θ=1−22\theta=1-\frac{\sqrt{2}}{2}. In the semidiscretisation approach, we choose the QUICK scheme ([3.6](https://arxiv.org/html/2511.01587v1#S3.E6 "In item QUICK scheme ‣ 3.3.2 Semidiscrete approximation ‣ 3.3 Convection part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"))-([3.7](https://arxiv.org/html/2511.01587v1#S3.E7 "In item QUICK scheme ‣ 3.3.2 Semidiscrete approximation ‣ 3.3 Convection part ‣ 3 Spatial discretisation ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) for the convection terms.

Figures [2](https://arxiv.org/html/2511.01587v1#S6.F2 "Figure 2 ‣ 6.2 Convergence behaviour: European call option ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") and [3](https://arxiv.org/html/2511.01587v1#S6.F3 "Figure 3 ‣ 6.2 Convergence behaviour: European call option ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") show that, for all schemes and all parameters sets, the total error decreases monotonically as NN and mm increase in a directly proportional way.
For the parameter sets 1, 2, 4, 5, a favourable second-order convergence behaviour is observed.
Further, for each of these four sets, CNFI and DIRKFI are seen to have about the same error constants, which is always smaller than that for SLCNFI, and hence, CNFI and DIRKFI are to be preferred over SLCNFI.

The sets 3 and 6 represent highly convection-dominated problems as the volatility σ\sigma is small and the jump intensity λ\lambda is low. These characteristics lead to the emergence of a region of nonsmoothness where the solution vv has steep gradients. In this situation, the convergence order for the total error of CNFI and DIRKFI reduces: it is (asymptotically) equal to 1.6.
On the other hand, for SLCNFI the convergence order remains (asymptotically) equal to two. Further, its error constant is smaller than that for CNFI and DIRKFI.
Hence, for these two sets, SLCNFI is to preferred.
We remark, however, that sets 3 and 6 are less representative of realistic market situations, since electricity prices typically experience significant fluctuations and frequent jumps, which are not captured well by a small volatility and low jump intensity.

Figures [4](https://arxiv.org/html/2511.01587v1#S6.F4 "Figure 4 ‣ 6.2 Convergence behaviour: European call option ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") and [5](https://arxiv.org/html/2511.01587v1#S6.F5 "Figure 5 ‣ 6.2 Convergence behaviour: European call option ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") display the temporal errors for the CNFI and DIRKFI schemes for, respectively, the Merton- and Kou-type jump models. The favourable result is observed that, for all six parameter sets, second-order convergence holds.
Additional experiments have been carried out with larger numbers of spatial grid points (m=300,400m=300,400) and the obtained temporal errors are found to be essentially unaffected.
This is a desirable property of the temporal error and is often referred to in the literature as convergence in the stiff sense.

Concerning the temporal error constant, this is seen to be noticeably smaller for DIRKFI than for CNFI. We note here that DIRKFI involves two fixed-point iteration processes per time step, thus requiring approximately twice the computational effort of CNFI per time step.

Additional experiments reveal that CNFI may show, however, unstable behaviour for larger time steps, even when Rannacher time-stepping (backward Euler damping) is applied.
Such unstable behaviour has not been observed in our experiments with SLCNFI and DIRKFI, which forms a favourable property of the latter schemes.

![Refer to caption](x2.png)

![Refer to caption](x3.png)

![Refer to caption](x4.png)

Figure 2: European call option in the Merton-type jump model. Total discretisation errors of the SLCNFI, CNFI and DIRKFI schemes for N=⌈m2⌉N=\left\lceil{\frac{m}{2}}\right\rceil and set 1 (top), set 2 (middle), set 3 (bottom). Added: dashed reference line for convergence order 2.

![Refer to caption](x5.png)

![Refer to caption](x6.png)

![Refer to caption](x7.png)

Figure 3: European call option in the Kou-type jump model. Total discretisation errors of the SLCNFI, CNFI and DIRKFI schemes for N=⌈m2⌉N=\left\lceil{\frac{m}{2}}\right\rceil and set 1 (top), set 2 (middle), set 3 (bottom). Added: dashed reference line for convergence order 2.

![Refer to caption](x8.png)

![Refer to caption](x9.png)

![Refer to caption](x10.png)

Figure 4: European call option in the Merton-type jump model. Temporal discretisation errors of the CNFI and DIRKFI schemes for m=200m=200 and set 1 (top), set 2 (middle), set 3 (bottom). Added: dashed reference line for convergence order 2.

![Refer to caption](x11.png)

![Refer to caption](x12.png)

![Refer to caption](x13.png)

Figure 5: European call option in the Kou-type jump model. Temporal discretisation errors of the CNFI and DIRKFI schemes for m=200m=200 and set 1 (top), set 2 (middle), set 3 (bottom). Added: dashed reference line for convergence order 2.

### 6.3 Numerical valuation of swing options

For the numerical valuation of swing options, we combine the numerical method proposed for the European call option case with the dynamic programming principle to find the optimal exercise at each action time. As before, we reverse the time to obtain an initial condition instead of a terminal condition. The action time τn\tau\_{n} in reversed time is T−TNa−n+1T-T\_{N\_{a}-n+1} (n=1,2,…,Nan=1,2,\ldots,N\_{a}) and the sequence of PIDEs ([2.4](https://arxiv.org/html/2511.01587v1#S2.E4 "In 2.2 Formulation of the problem ‣ 2 Swing option price modelling ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) then becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∂tv​(x,y,z,t)=σ22​∂x​xv​(x,y,z,t)+α​(μ−x)​∂xv​(x,y,z,t)−β​y​∂yv​(x,y,z,t)−(r+λ)​v​(x,y,z,t)+λ​∫ℝv​(x,y+ξ,z,t)​f​(ξ)​𝑑ξ,τn<t<τn+1,v​(x,y,z,τn)=max⁡{bn​(x+y−K)+v​(x,y,z+bn,τn−):bn∈{0,1,…,L},z+bn≤M}\begin{cases}\displaystyle\partial\_{t}v(x,y,z,t)=\frac{\sigma^{2}}{2}\partial\_{xx}v(x,y,z,t)+\alpha(\mu-x)\partial\_{x}v(x,y,z,t)-\beta y\partial\_{y}v(x,y,z,t)-(r+\lambda)v(x,y,z,t)\\[8.53581pt] \displaystyle\qquad\qquad\qquad\qquad\qquad+\lambda\int\_{\mathbb{R}}v(x,y+\xi,z,t)f(\xi)d\xi,\qquad\tau\_{n}<t<\tau\_{n+1},\\[8.53581pt] \displaystyle v(x,y,z,\tau\_{n})=\max\big\{b\_{n}(x+y-K)+v(x,y,z+b\_{n},\tau\_{n}^{-}):b\_{n}\in\{0,1,\ldots,L\},z+b\_{n}\leq M\big\}\\ \end{cases} |  | (6.1) |

for (x,y,z)∈ℝ×ℝ×{0,1,…,M−1}(x,y,z)\in\mathbb{R}\times\mathbb{R}\times\{0,1,\ldots,M-1\} and 1≤n≤Na1\leq n\leq N\_{a}. Here v​(⋅,⋅,⋅,τ1−)=0v(\cdot,\cdot,\cdot,\tau\_{1}^{-})=0, v​(⋅,⋅,M,⋅)=0v(\cdot,\cdot,M,\cdot)=0 and τNa+1=T\tau\_{N\_{a}+1}=T.

The valuation procedure is outlined in Algorithm [1](https://arxiv.org/html/2511.01587v1#alg1 "Algorithm 1 ‣ 6.3 Numerical valuation of swing options ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps").
At the first action time, τ1=0\tau\_{1}=0, the holder buys the maximal allowable amount.
Given the option value at τ1\tau\_{1}, the PIDE is solved to obtain the option value up to the second action time, τ2\tau\_{2}. It is then considered whether it is optimal to exercise or not by maximizing the option value at τ2\tau\_{2}. This process is repeated for each subsequent action time up to and including τNa\tau\_{N\_{a}}. At each action time, the option value is determined by optimizing over all feasible exercise amounts b∈{0,1,…,L}b\in\{0,1,\ldots,L\}, while ensuring that the cumulative purchased amount does not exceed the global constraint MM. Finally, the PIDE is solved over the interval (τNa,τNa+1](\tau\_{N\_{a}},\tau\_{N\_{a}+1}] to arrive at the desired option value function v​(⋅,⋅,0,T)v(\cdot,\cdot,0,T).

Algorithm 1  Dynamic Programming for Swing Option Valuation

1:Input: NaN\_{a} (number of action times), LL (local constraint), MM (global constraint), NN (number of time steps between two successive action times), strike KK

2:Initialise: V←0V\leftarrow 0, optimal policy bn,l,i,j∗←0b^{\*}\_{n,l,i,j}\leftarrow 0

3:for n=1n=1 to NaN\_{a} do ⊳\triangleright nn-th swing action time

4:  for l=0l=0 to M−1M-1 do ⊳\triangleright ll: cumulative purchased amount

5:   for b=0b=0 to min⁡(L,M−l)\min(L,M-l) do

6:     Vl,i,j(n−1)​N←max⁡(b​(xi+yj−K)+Vl+b,i,j(n−1)​N,Vl,i,j(n−1)​N)V^{(n-1)N}\_{l,i,j}\leftarrow\max\left(b(x\_{i}+y\_{j}-K)+V^{(n-1)N}\_{l+b,i,j},\;V^{(n-1)N}\_{l,i,j}\right)

7:   end for

8:   Store optimal bn,l,i,j∗b^{\*}\_{n,l,i,j} that yields the maximum

9:   for k=1k=1 to NN do

10:     Compute Vl(n−1)​N+kV^{(n-1)N+k}\_{l} by the time-stepping scheme

11:   end for

12:  end for

13:end for




Algorithm 2  Tracking back the cumulative optimal exercise path

1:Input: Number of swing times NaN\_{a}, global constraint MM, policy array b∗b^{\*}

2:Initialize: path←0\texttt{path}\leftarrow 0 ⊳\triangleright cumulative optimal path

3:for n=1n=1 to NaN\_{a} do

4:  for each grid point (i,j)(i,j) do

5:   if n=1n=1 then

6:     l←0l\leftarrow 0 ⊳\triangleright zero units of energy at the start

7:   else

8:     l←path​[i,j,n−1]l\leftarrow\texttt{path}[i,j,n-1]

9:   end if

10:   if l<Ml<M then

11:     δ←bNa−n+1,l,i,j∗\delta\leftarrow b^{\*}\_{N\_{a}-n+1,l,i,j}

12:     path​[i,j,n]←l+δ\texttt{path}[i,j,n]\leftarrow l+\delta

13:   else

14:     path​[i,j,n]←l\texttt{path}[i,j,n]\leftarrow l

15:   end if

16:  end for

17:end for

18:Output: path

Figure [6](https://arxiv.org/html/2511.01587v1#S6.F6 "Figure 6 ‣ 6.3 Numerical valuation of swing options ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") displays the graph of the swing option value function for z=0z=0 at t=Tt=T (reversed time). Here the number of swing action times is set to Na=20N\_{a}=20, with local constraint specified by L=1L=1 and global constraint by M=10M=10. Both Merton- and Kou-type jump models are considered, for the parameter sets 1 and 4 given by the Tables [1](https://arxiv.org/html/2511.01587v1#S6.T1 "Table 1 ‣ 6.1 Financial parameter values ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") and [2](https://arxiv.org/html/2511.01587v1#S6.T2 "Table 2 ‣ 6.1 Financial parameter values ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"), respectively, with maturity time T=1T=1.
Table [3](https://arxiv.org/html/2511.01587v1#S6.T3 "Table 3 ‣ 6.3 Numerical valuation of swing options ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") provides corresponding reference values obtained with the CNFI scheme and N=100N=100 time steps between each two successive action times.

![Refer to caption](x14.png)

![Refer to caption](x15.png)

Figure 6: Swing option value functions with z=0z=0 and t=T=1t=T=1 for set 1 (top) and set 4 (bottom) where Na=20N\_{a}=20, L=1L=1, M=10M=10.




Table 3: Swing option values with z=0z=0 and t=T=1t=T=1 for sets 1 and 4 where Na=20N\_{a}=20, L=1L=1, M=10M=10 and using the CNFI scheme m1=m2=N=100m\_{1}=m\_{2}=N=100.

Set 1

|  |  |  |  |
| --- | --- | --- | --- |
|  | x=40x=40 | x=60x=60 | x=80x=80 |
| y=5y=5 | 500.8962500.8962 | 512.5631512.5631 | 527.9123527.9123 |
| y=−100y=-100 | 500.8664500.8664 | 512.5167512.5167 | 527.8260527.8260 |
| y=100y=100 | 500.9234500.9234 | 512.6054512.6054 | 527.9915527.9915 |

Set 4

|  |  |  |  |
| --- | --- | --- | --- |
|  | x=40x=40 | x=60x=60 | x=80x=80 |
| y=5y=5 | 686.5660686.5660 | 699.2691699.2691 | 714.7266714.7266 |
| y=−100y=-100 | 686.5246686.5246 | 699.2137699.2137 | 714.6424714.6424 |
| y=100y=100 | 686.6036686.6036 | 699.3196699.3196 | 714.8036714.8036 |

### 6.4 Convergence behaviour: swing options

In this section, we numerically study the temporal discretisation error for the CNFI and DIRKFI schemes in the context of swing options.
Here again Na=20N\_{a}=20, L=1L=1, M=10M=10 and the parameter sets 1 and 4 are considered with T=1T=1.

![Refer to caption](x16.png)

![Refer to caption](x17.png)

Figure 7: Swing option with Na=20,L=1,M=10N\_{a}=20,\,L=1,\,M=10. Temporal discretisation errors of the CNFI and DIRKFI schemes for m=100m=100 and set 1 (top) and set 4 (bottom). Added: dashed reference line for convergence order 2.

Figure [7](https://arxiv.org/html/2511.01587v1#S6.F7 "Figure 7 ‣ 6.4 Convergence behaviour: swing options ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") displays the temporal errors for 20 different values of NN
ranging from 50 to 500 and m=100m=100. Notice that the total number of time steps over [0,T][0,T] then ranges from 10310^{3} and 10410^{4}. A reference solution has been computed by applying the CNFI scheme with N=4000N=4000.

As in the European case (see Section [6.2](https://arxiv.org/html/2511.01587v1#S6.SS2 "6.2 Convergence behaviour: European call option ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")), the temporal errors for both the CNFI and DIRKFI schemes decrease monotonically as the time step is refined. Figure [7](https://arxiv.org/html/2511.01587v1#S6.F7 "Figure 7 ‣ 6.4 Convergence behaviour: swing options ‣ 6 Numerical experiments ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps") reveals that both methods exhibit a favourable, second-order convergence behaviour. Additional experiments with larger numbers of spatial grid points (m=200,300m=200,300) further show that the temporal errors are essentially unaffected, as desired.

We note that, unlike the European case, the temporal errors for CNFI and DIRKFI are nearly identical. This is attributed to the structure of the swing option, which involves discrete action times where the option price is updated, in addition to the continuation phase. These updates apparently reduce the distinction between the two schemes in terms of temporal accuracy.

## 7 Conclusions

In this paper, we investigated the numerical valuation of swing options with discrete action times under an affine two-factor mean-reverting model with jumps.
For the numerical solution of the pertinent sequence of two-dimensional PIDEs, we studied three methods: SLCNFI, CNFI and DIRKFI.
The first method is based on the semi-Lagrangian approach, whereas the second and third methods are based on a full semidiscretisation approach by suitable finite differences.
For the time-stepping, the Crank-Nicolson scheme and an LL-stable DIRK scheme are considered.
Here, the nonlocal integral has been effectively treated by a fixed-point iteration.

Ample numerical experiments demonstrate that all three methods possess a desirable second-order convergence behaviour notwithstanding the convection-dominated property of the PIDE and the nonsmooth initial function and the presence of the nonlocal integral term. Our theoretical analysis confirms that the CNFI and DIRKFI methods are stable and second-order convergent under a smoothness condition. A theoretical convergence analysis of the semi-Lagrangian method is not undertaken in this work and forms an interesting topic for future research.

A main topic for our future research is the extension of the present numerical solution approach towards more advanced swing option types, such as considered in Dahlgren ([2005](https://arxiv.org/html/2511.01587v1#bib.bib7)).

### Acknowledgements

The authors acknowledge the support of the Research Foundation - Flanders (FWO) under grant G0B5623N and the FWO Scientific
Research Network ModSimFIE (FWO WOG W001021N). The third author also acknowledges the financial support of the Research Foundation - Flanders (FWO) through FWO SAB K803124.

## References

* Barles and Souganidis [1991]

  G. Barles and P. E. Souganidis.
  Convergence of approximation schemes for fully nonlinear second order
  equations.
  *Asymptotic Analysis*, 4(3):271–283, 1991.
  doi: 10.3233/ASY-1991-4305.
* Benth et al. [2007]

  F. E. Benth, J. Kallsen, and T. Meyer-Brandis.
  A non-Gaussian Ornstein–Uhlenbeck process for electricity spot
  price modeling and derivatives pricing.
  *Applied Mathematical Finance*, 14(2):153–169, 2007.
* Benth et al. [2011]

  F. E. Benth, J. Lempa, and T. K. Nilssen.
  On the optimal exercise of swing options in electricity markets.
  *The Journal of Energy Markets*, 4:3–28, 2011.
  doi: 10.21314/JEM.2011.065.
* Calvo-Garrido et al. [2016]

  M. C. Calvo-Garrido, M. Ehrhardt, and C. Vázquez.
  Pricing swing options in electricity markets with two stochastic
  factors using a partial differential equation approach.
  *Journal of Computational Finance*, 20:1–27, 2016.
* Calvo-Garrido et al. [2019]

  M. C. Calvo-Garrido, M. Ehrhardt, and C. Vázquez.
  Jump-diffusion models with two stochastic factors for pricing swing
  options in electricity markets with partial-integro differential equations.
  *Applied Numerical Mathematics*, 139:77–92, 2019.
  doi: 10.1016/j.apnum.2019.01.001.
* Cash [1984]

  J. R. Cash.
  Two new finite difference schemes for parabolic equations.
  *SIAM Journal on Numerical Analysis*, 21(3):433–446, 1984.
  doi: 10.1137/0721032.
* Dahlgren [2005]

  M. Dahlgren.
  A continuous time model to price commodity-based swing options.
  *Review of Derivatives Research*, 8(1):27–47, June 2005.
  doi: 10.1007/s11147-005-1006-9.
* d’Halluin et al. [2005a]

  Y. d’Halluin, P. A. Forsyth, and G. Labahn.
  A semi-Lagrangian approach for American Asian options under
  jump diffusion.
  *SIAM Journal on Scientific Computing*, 27(1):315–331, 2005a.
  doi: 10.1137/030602630.
* d’Halluin et al. [2005b]

  Y. d’Halluin, P. A. Forsyth, and K. R. Vetzal.
  Robust numerical methods for contingent claims under jump diffusion
  processes.
  *IMA Journal of Numerical Analysis*, 25(1):87–112, 01 2005b.
  doi: 10.1093/imanum/drh011.
* Eriksson et al. [2014]

  M. Eriksson, J. Lempa, and T. K. Nilssen.
  Swing options in commodity markets: a multidimensional Lévy
  diffusion model.
  *Mathematical Methods of Operations Research*, 79(1):31–67, 2014.
  doi: 10.1007/s00186-013-0452-7.
* Hairer and Wanner [1996]

  E. Hairer and G. Wanner.
  *Solving Ordinary Differential Equations II. Stiff and
  Differential-Algebraic Problems*, volume 14 of *Springer Series in
  Computational Mathematics*.
  Springer Berlin, Heidelberg, 01 1996.
  doi: 10.1007/978-3-662-09947-6.
* Hambly et al. [2009]

  B. Hambly, S. Howison, and T. Kluge.
  Modelling spikes and pricing swing options in electricity markets.
  *Quantitative Finance*, 9(8):937–949, 2009.
  doi: 10.1080/14697680802596856.
* Hundsdorfer and Verwer [2003]

  W. H. Hundsdorfer and J. G. Verwer.
  *Numerical Solution of Time-Dependent
  Advection-Diffusion-Reaction Equations*, volume 33 of *Springer Series
  in Computational Mathematics*.
  Springer Berlin, Heidelberg, 2003.
  doi: 10.1007/978-3-662-09017-6.
* Ibáñez [2004]

  A. Ibáñez.
  Valuation by simulation of contingent claims with multiple early
  exercise opportunities.
  *Mathematical Finance*, 14(2):223–248,
  2004.
  doi: 10.1111/j.0960-1627.2004.00190.x.
* in ’t Hout [2025]

  K. J. in ’t Hout.
  An efficient numerical method for American options and their
  Greeks under the two-asset Kou jump-diffusion model.
  *Journal of Computational Finance*, to appear, 2025.
* in ’t Hout and Lamotte [2023]

  K. J. in ’t Hout and P. Lamotte.
  Efficient numerical valuation of European options under the
  two-asset Kou jump-diffusion model.
  *Journal of Computational Finance*, 26(4):101–137, 2023.
  doi: 10.21314/JCF.2023.001.
* Jaillet et al. [2004]

  P. Jaillet, E. I. Ronn, and S. Tompaidis.
  Valuation of commodity-based swing options.
  *Management Science*, 50(7):909–921, 2004.
  doi: 10.1287/mnsc.1040.0240.
* Kirkby and Deng [2019]

  J. Kirkby and S. Deng.
  Swing option pricing by dynamic programming with B-spline density
  projection.
  *International Journal of Theoretical and Applied Finance*, 10
  2019.
  doi: 10.1142/S0219024919500389.
* Kjaer [2008]

  M. Kjaer.
  Pricing of swing options in a mean reverting model with jumps.
  *Applied Mathematical Finance*, 15(5):479–502, 2008.
  doi: 10.1080/13504860802170556.
* Leonard [1979]

  B. P. Leonard.
  A stable and accurate convective modelling procedure based on
  quadratic upstream interpolation.
  *Computer Methods in Applied Mechanics and Engineering*,
  19(1):59–98, 1979.
  ISSN 0045-7825.
* Lucia and Schwartz [2002]

  J. J. Lucia and E. S. Schwartz.
  Electricity prices and power derivatives: Evidence from the
  Nordic Power Exchange.
  *Review of Derivatives Research*, 5:5–50, 2002.
  doi: 10.1023/A:1013846631785.
* Rannacher [1984]

  R. Rannacher.
  Finite element solution of diffusion problems with irregular data.
  *Numerische Mathematik*, 43:309–328, 1984.
  doi: 10.1007/BF01390130.
* Tavella and Randall [2000]

  D. Tavella and C. Randall.
  *Pricing Financial Instruments: The Finite Difference Method*.
  New York (N.Y.): Wiley, 01 2000.
* Tirez et al. [2023]

  A. Tirez, L. Jacquet, and K. Locquet.
  Study on the occurrence and impact of negative prices in the
  day-ahead market.
  Technical report, Commission for Electricity and Gas Regulation,
  2023.
* Toivanen [2008]

  J. Toivanen.
  Numerical valuation of European and American options under
  Kou’s jump-diffusion model.
  *SIAM Journal on Scientific Computing*, 30(4):1949–1970, 2008.
  doi: 10.1137/060674697.
* Varah [1975]

  J. M. Varah.
  A lower bound for the smallest singular value of a matrix.
  *Linear Algebra and its Applications*, 11(1):3–5, 1975.
  doi: 10.1016/0024-3795(75)90112-3.
* Zhang and Oosterlee [2013]

  B. Zhang and C. W. Oosterlee.
  An efficient pricing algorithm for swing options based on Fourier
  cosine expansions.
  *Journal of Computational Finance*, 16(4):3–34, 2013.
  doi: 10.21314/JCF.2013.268.

## Appendix A Proof of Lemma [5.3](https://arxiv.org/html/2511.01587v1#Thmtheorem3 "Lemma 5.3. ‣ 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")

###### Proof.

Without loss of generality, we assume that b~>0\tilde{b}>0.
  
For the ease of presentation, write Dx,i,i=giD\_{x,i,i}=g\_{i} and assume there is index i0i\_{0} such that gi0=0g\_{i\_{0}}=0. Let P0P\_{0} denote the part of the inner product ⟨Dx​A~x​V,V⟩\langle D\_{x}\tilde{A}\_{x}V,V\rangle corresponding to the case i<i0i<i\_{0}.
We have by ([5.1](https://arxiv.org/html/2511.01587v1#S5.E1 "In 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps"))

|  |  |  |
| --- | --- | --- |
|  | P0=∑i=0i0−1gi​∑k=−12wk​Vi+k​Vi−w−1​g0​V−1​V0.P\_{0}=\sum\_{i=0}^{i\_{0}-1}g\_{i}\sum\_{k=-1}^{2}w\_{k}V\_{i+k}V\_{i}-w\_{-1}g\_{0}V\_{-1}V\_{0}. |  |

The term w−1​g0​V−1​V0w\_{-1}g\_{0}V\_{-1}V\_{0} is subtracted because the inner product does not contain V−1V\_{-1} due to the Dirichlet boundary conditions. For the first term of P0P\_{0}, we obtain using ([5.2](https://arxiv.org/html/2511.01587v1#S5.E2 "In 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) and the relation 2​a​b=a2+b2−(a−b)22ab=a^{2}+b^{2}-(a-b)^{2}:

|  |  |  |
| --- | --- | --- |
|  | ∑i=0i0−1gi​∑k=−12wk​Vi+k​Vi\displaystyle\sum\_{i=0}^{i\_{0}-1}g\_{i}\sum\_{k=-1}^{2}w\_{k}V\_{i+k}V\_{i} |  |
|  |  |  |
| --- | --- | --- |
|  | =12​∑i=0i0−1gi​∑k=−12wk​Vi+k2⏟=⁣:A+12​∑i=0i0−1gi​∑k=−12wk⏟=0​Vi2​−12​∑i=0i0−1gi​∑k=−12wk​(Vi+k−Vi)2⏟=⁣:B.\displaystyle=\underbrace{\frac{1}{2}\sum\_{i=0}^{i\_{0}-1}g\_{i}\sum\_{k=-1}^{2}w\_{k}V^{2}\_{i+k}}\_{=:A}+\frac{1}{2}\sum\_{i=0}^{i\_{0}-1}g\_{i}\underbrace{\sum\_{k=-1}^{2}w\_{k}}\_{=0}V^{2}\_{i}\underbrace{-\frac{1}{2}\sum\_{i=0}^{i\_{0}-1}g\_{i}\sum\_{k=-1}^{2}w\_{k}(V\_{i+k}-V\_{i})^{2}}\_{=:B}. |  |

Interchanging the summations, invoking again ([5.2](https://arxiv.org/html/2511.01587v1#S5.E2 "In 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) and noting that gi−k−gi=k​b~​Δ​xg\_{i-k}-g\_{i}=k\tilde{b}\Delta x and gi0−1+i−k=gi0−1+i−k−gi0=(1−i+k)​b~​Δ​xg\_{i\_{0}-1+i-k}=g\_{i\_{0}-1+i-k}-g\_{i\_{0}}=(1-i+k)\tilde{b}\Delta x we derive

|  |  |  |  |
| --- | --- | --- | --- |
|  | A\displaystyle A | =12​∑k=−12wk​∑i=ki0−1+kgi−k​Vi2\displaystyle=\frac{1}{2}\sum\_{k=-1}^{2}w\_{k}\sum\_{i=k}^{i\_{0}-1+k}g\_{i-k}V^{2}\_{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​∑k=−12wk​∑i=2i0−2(gi−k−gi)​Vi2+12​∑k=−11wk​∑i=k1gi−k​Vi2+12​∑k=02wk​∑i=i0−1i0−1+kgi−k​Vi2\displaystyle=\frac{1}{2}\sum\_{k=-1}^{2}w\_{k}\sum\_{i=2}^{i\_{0}-2}(g\_{i-k}-g\_{i})V^{2}\_{i}+\frac{1}{2}\sum\_{k=-1}^{1}w\_{k}\sum\_{i=k}^{1}g\_{i-k}V^{2}\_{i}+\frac{1}{2}\sum\_{k=0}^{2}w\_{k}\sum\_{i=i\_{0}-1}^{i\_{0}-1+k}g\_{i-k}V^{2}\_{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​b~​Δ​x​∑k=−12k​wk​∑i=2i0−2Vi2+12​∑i=−11∑k=−1iwk​gi−k​Vi2+12​b~​Δ​x​∑i=02∑k=i2(1−i+k)​wk​Vi0−1+i2\displaystyle=\frac{1}{2}\tilde{b}\Delta x\sum\_{k=-1}^{2}kw\_{k}\sum\_{i=2}^{i\_{0}-2}V^{2}\_{i}+\frac{1}{2}\sum\_{i=-1}^{1}\sum\_{k=-1}^{i}w\_{k}g\_{i-k}V^{2}\_{i}+\frac{1}{2}\tilde{b}\Delta x\sum\_{i=0}^{2}\sum\_{k=i}^{2}(1-i+k)w\_{k}V\_{i\_{0}-1+i}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−(w−1+w2)​b~​Δ​x​∑i=2i0−2Vi2+12​∑i=−11∑k=−1iwk​gi−k​Vi2+12​b~​Δ​x​∑i=02∑k=i2(1−i+k)​wk​Vi0−1+i2.\displaystyle=-(w\_{-1}+w\_{2})\tilde{b}\Delta x\sum\_{i=2}^{i\_{0}-2}V^{2}\_{i}+\frac{1}{2}\sum\_{i=-1}^{1}\sum\_{k=-1}^{i}w\_{k}g\_{i-k}V^{2}\_{i}+\frac{1}{2}\tilde{b}\Delta x\sum\_{i=0}^{2}\sum\_{k=i}^{2}(1-i+k)w\_{k}V\_{i\_{0}-1+i}^{2}. |  |

As gi≥0g\_{i}\geq 0 for i<i0i<i\_{0} it holds that
12​gi​(Vi+2−Vi)2≤gi​(Vi+1−Vi)2+gi​(Vi+2−Vi+1)2\frac{1}{2}g\_{i}(V\_{i+2}-V\_{i})^{2}\leq g\_{i}(V\_{i+1}-V\_{i})^{2}+g\_{i}(V\_{i+2}-V\_{i+1})^{2}. Then, recalling the properties ([5.2](https://arxiv.org/html/2511.01587v1#S5.E2 "In 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) and gi−k−gi=k​b~​Δ​xg\_{i-k}-g\_{i}=k\tilde{b}\Delta x, and defining w−1+=max⁡(w−1,0)w\_{-1}^{+}=\max(w\_{-1},0) the term BB can be bounded as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | B\displaystyle B | =−12​w−1​∑i=0i0−1gi​((Vi−1−Vi)2−(Vi+1−Vi)2)−12​(w−1+w1)⏟=−4​w2​∑i=0i0−1gi​(Vi+1−Vi)2−12​w2​∑i=0i0−1gi​(Vi+2−Vi)2\displaystyle=-\frac{1}{2}w\_{-1}\sum\_{i=0}^{i\_{0}-1}g\_{i}\Big((V\_{i-1}-V\_{i})^{2}-(V\_{i+1}-V\_{i})^{2}\Big)-\frac{1}{2}\underbrace{(w\_{-1}+w\_{1})}\_{=-4w\_{2}}\sum\_{i=0}^{i\_{0}-1}g\_{i}(V\_{i+1}-V\_{i})^{2}-\frac{1}{2}w\_{2}\sum\_{i=0}^{i\_{0}-1}g\_{i}(V\_{i+2}-V\_{i})^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤−12​w−1​∑i=0i0−1gi​((Vi−1−Vi)2−(Vi+1−Vi)2)+2​w2​∑i=0i0−1gi​(Vi+1−Vi)2\displaystyle\leq-\frac{1}{2}w\_{-1}\sum\_{i=0}^{i\_{0}-1}g\_{i}\Big((V\_{i-1}-V\_{i})^{2}-(V\_{i+1}-V\_{i})^{2}\Big)+2w\_{2}\sum\_{i=0}^{i\_{0}-1}g\_{i}(V\_{i+1}-V\_{i})^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −w2​∑i=0i0−1gi​((Vi+2−Vi+1)2+(Vi+1−Vi)2)\displaystyle\qquad-w\_{2}\sum\_{i=0}^{i\_{0}-1}g\_{i}\Big((V\_{i+2}-V\_{i+1})^{2}+(V\_{i+1}-V\_{i})^{2}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​w−1​b~​Δ​x​∑i=0i0−1(Vi+1−Vi)2−w2​b~​Δ​x​∑i=0i0−1(Vi+2−Vi+1)2−12​w−1​g0​(V0−V−1)2+w2​g0​(V1−V0)2\displaystyle=\frac{1}{2}w\_{-1}\tilde{b}\Delta x\sum\_{i=0}^{i\_{0}-1}(V\_{i+1}-V\_{i})^{2}-w\_{2}\tilde{b}\Delta x\sum\_{i=0}^{i\_{0}-1}(V\_{i+2}-V\_{i+1})^{2}-\frac{1}{2}w\_{-1}g\_{0}(V\_{0}-V\_{-1})^{2}+w\_{2}g\_{0}(V\_{1}-V\_{0})^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤w−1+​b~​Δ​x​∑i=0i0−1(Vi+12+Vi2)−2​w2​b~​Δ​x​∑i=0i0−1(Vi+22+Vi+12)−12​w−1​g0​(V0−V−1)2+w2​g0​(V1−V0)2\displaystyle\leq w\_{-1}^{+}\tilde{b}\Delta x\sum\_{i=0}^{i\_{0}-1}(V^{2}\_{i+1}+V\_{i}^{2})-2w\_{2}\tilde{b}\Delta x\sum\_{i=0}^{i\_{0}-1}(V\_{i+2}^{2}+V\_{i+1}^{2})-\frac{1}{2}w\_{-1}g\_{0}(V\_{0}-V\_{-1})^{2}+w\_{2}g\_{0}(V\_{1}-V\_{0})^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(2​w−1+−4​w2)​b~​Δ​x​∑i=2i0−2Vi2+w−1+​b~​Δ​x​(V02+2​V12+2​Vi0−12+Vi02)−2​w2​b~​Δ​x​(V12+2​Vi0−12+2​Vi02+Vi0+12)\displaystyle=(2w\_{-1}^{+}-4w\_{2})\tilde{b}\Delta x\sum\_{i=2}^{i\_{0}-2}V\_{i}^{2}+w\_{-1}^{+}\tilde{b}\Delta x(V\_{0}^{2}+2V^{2}\_{1}+2V\_{i\_{0}-1}^{2}+V\_{i\_{0}}^{2})-2w\_{2}\tilde{b}\Delta x(V\_{1}^{2}+2V\_{i\_{0}-1}^{2}+2V\_{i\_{0}}^{2}+V\_{i\_{0}+1}^{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −12​w−1​g0​(V0−V−1)2+w2​g0​(V1−V0)2.\displaystyle\qquad-\frac{1}{2}w\_{-1}g\_{0}(V\_{0}-V\_{-1})^{2}+w\_{2}g\_{0}(V\_{1}-V\_{0})^{2}. |  |

Combination of the expression for AA and the bound for BB while noting that 2​w−1+−w−1=|w−1|2w\_{-1}^{+}-w\_{-1}=|w\_{-1}| gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | A+B\displaystyle A+B | ≤(|w−1|−5​w2)​b~​Δ​x​∑i=2i0−2Vi2+12​b~​Δ​x​∑i=02∑k=i2(1−i+k)​wk​Vi0−1+i2\displaystyle\leq(|w\_{-1}|-5w\_{2})\tilde{b}\Delta x\sum\_{i=2}^{i\_{0}-2}V\_{i}^{2}+\frac{1}{2}\tilde{b}\Delta x\sum\_{i=0}^{2}\sum\_{k=i}^{2}(1-i+k)w\_{k}V\_{i\_{0}-1+i}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +w−1+​b~​Δ​x​(V02+2​V12+2​Vi0−12+Vi02)−2​w2​b~​Δ​x​(V12+2​Vi0−12+2​Vi02+Vi0+12)\displaystyle\qquad+w\_{-1}^{+}\tilde{b}\Delta x(V\_{0}^{2}+2V^{2}\_{1}+2V\_{i\_{0}-1}^{2}+V\_{i\_{0}}^{2})-2w\_{2}\tilde{b}\Delta x(V\_{1}^{2}+2V\_{i\_{0}-1}^{2}+2V\_{i\_{0}}^{2}+V\_{i\_{0}+1}^{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​∑i=−11∑k=−1iwk​gi−k​Vi2−12​w−1​g0​(V0−V−1)2+w2​g0​(V1−V0)2⏟=⁣:C.\displaystyle\qquad+\underbrace{\frac{1}{2}\sum\_{i=-1}^{1}\sum\_{k=-1}^{i}w\_{k}g\_{i-k}V^{2}\_{i}-\frac{1}{2}w\_{-1}g\_{0}(V\_{0}-V\_{-1})^{2}+w\_{2}g\_{0}(V\_{1}-V\_{0})^{2}}\_{=:C}. |  |

Estimating further the term CC using w0=3​w2w\_{0}=3w\_{2} and the inequality 12​a2≤(a−b)2+b2\frac{1}{2}a^{2}\leq(a-b)^{2}+b^{2} leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | C\displaystyle C | =12​w−1​g0​V−12+12​(w0​g0+w−1​g1)​V02−12​w2​g0​V12−12​(w0+2​w−1)​b~​Δ​x​V12\displaystyle=\frac{1}{2}w\_{-1}g\_{0}V\_{-1}^{2}+\frac{1}{2}(w\_{0}g\_{0}+w\_{-1}g\_{1})V\_{0}^{2}-\frac{1}{2}w\_{2}g\_{0}V\_{1}^{2}-\frac{1}{2}(w\_{0}+2w\_{-1})\tilde{b}\Delta xV\_{1}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −12​w−1​g0​(V0−V−1)2+w2​g0​(V1−V0)2\displaystyle\qquad-\frac{1}{2}w\_{-1}g\_{0}(V\_{0}-V\_{-1})^{2}+w\_{2}g\_{0}(V\_{1}-V\_{0})^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤12​w−1​g0​(V−12−(V0−V−1)2)+12​(w2​g0+w−1​g1)​V02+w2​g0​V02−w2​g0​(V1−V0)2−w2​g0​V02\displaystyle\leq\frac{1}{2}w\_{-1}g\_{0}\Big(V\_{-1}^{2}-(V\_{0}-V\_{-1})^{2}\Big)+\frac{1}{2}(w\_{2}g\_{0}+w\_{-1}g\_{1})V\_{0}^{2}+w\_{2}g\_{0}V\_{0}^{2}-w\_{2}g\_{0}(V\_{1}-V\_{0})^{2}-w\_{2}g\_{0}V\_{0}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −12​(w0+2​w−1)​b~​Δ​x​V12+w2​g0​(V1−V0)2\displaystyle\qquad-\frac{1}{2}(w\_{0}+2w\_{-1})\tilde{b}\Delta xV\_{1}^{2}+w\_{2}g\_{0}(V\_{1}-V\_{0})^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​w−1​g0​(V−12−(V0−V−1)2)+12​(w2​g0+w−1​g1)​V02−12​(3​w2+2​w−1)​b~​Δ​x​V12.\displaystyle=\frac{1}{2}w\_{-1}g\_{0}\Big(V\_{-1}^{2}-(V\_{0}-V\_{-1})^{2}\Big)+\frac{1}{2}(w\_{2}g\_{0}+w\_{-1}g\_{1})V\_{0}^{2}-\frac{1}{2}(3w\_{2}+2w\_{-1})\tilde{b}\Delta xV\_{1}^{2}. |  |

Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | C−w−1​g0​V−1​V0\displaystyle C-w\_{-1}g\_{0}V\_{-1}V\_{0} | =C+12​w−1​g0​(V−1−V0)2−12​w−1​g0​V−12−12​w−1​g0​V02\displaystyle=C+\frac{1}{2}w\_{-1}g\_{0}(V\_{-1}-V\_{0})^{2}-\frac{1}{2}w\_{-1}g\_{0}V\_{-1}^{2}-\frac{1}{2}w\_{-1}g\_{0}V\_{0}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤12​w2​g0​V02−12​(3​w2+2​w−1)​b~​Δ​x​V12−12​w−1​b~​Δ​x​V02\displaystyle\leq\frac{1}{2}w\_{2}g\_{0}V\_{0}^{2}-\frac{1}{2}(3w\_{2}+2w\_{-1})\tilde{b}\Delta xV\_{1}^{2}-\frac{1}{2}w\_{-1}\tilde{b}\Delta xV\_{0}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤−12​(3​w2+2​w−1)​b~​Δ​x​V12−12​w−1​b~​Δ​x​V02.\displaystyle\leq-\frac{1}{2}(3w\_{2}+2w\_{-1})\tilde{b}\Delta xV\_{1}^{2}-\frac{1}{2}w\_{-1}\tilde{b}\Delta xV\_{0}^{2}. |  |

Substituting these bounds into P0P\_{0} and using the properties ([5.2](https://arxiv.org/html/2511.01587v1#S5.E2 "In 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")) we find

|  |  |  |  |
| --- | --- | --- | --- |
|  | P0\displaystyle P\_{0} | ≤(|w−1|−5​w2)​b~​Δ​x​∑i=2i0−2Vi2+12​|w−1|​b~​Δ​x​V02+(|w−1|−72​w2)​b~​Δ​x​V12\displaystyle\leq(|w\_{-1}|-5w\_{2})\tilde{b}\Delta x\sum\_{i=2}^{i\_{0}-2}V\_{i}^{2}+\frac{1}{2}|w\_{-1}|\tilde{b}\Delta xV\_{0}^{2}+(|w\_{-1}|-\frac{7}{2}w\_{2})\tilde{b}\Delta xV\_{1}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(|w−1|−5​w2)​b~​Δ​x​Vi0−12+(12​|w−1|−5​w2)​b~​Δ​x​Vi02−32​w2​b~​Δ​x​Vi0+12\displaystyle\quad+(|w\_{-1}|-5w\_{2})\tilde{b}\Delta xV\_{i\_{0}-1}^{2}+(\frac{1}{2}|w\_{-1}|-5w\_{2})\tilde{b}\Delta xV\_{i\_{0}}^{2}-\frac{3}{2}w\_{2}\tilde{b}\Delta xV\_{i\_{0}+1}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(|w−1|−5​w2)​b~​Δ​x​∑i=0i0−2Vi2+(|w−1|−5​w2)​b~​Δ​x​Vi0−12+(12​|w−1|−5​w2)​b~​Δ​x​Vi02−32​w2​b~​Δ​x​Vi0+12.\displaystyle\leq(|w\_{-1}|-5w\_{2})\tilde{b}\Delta x\sum\_{i=0}^{i\_{0}-2}V\_{i}^{2}+(|w\_{-1}|-5w\_{2})\tilde{b}\Delta xV\_{i\_{0}-1}^{2}+(\frac{1}{2}|w\_{-1}|-5w\_{2})\tilde{b}\Delta xV\_{i\_{0}}^{2}-\frac{3}{2}w\_{2}\tilde{b}\Delta xV\_{i\_{0}+1}^{2}. |  |

Let g~i=−gm−i=−gm−i​b~​Δ​x\tilde{g}\_{i}=-g\_{m-i}=-g\_{m}-i\tilde{b}\Delta x (notice that g~m−i0=0\tilde{g}\_{m-i\_{0}}=0) and V~i=Vm−i\tilde{V}\_{i}=V\_{m-i}.
By a change of indices, we get

|  |  |  |
| --- | --- | --- |
|  | ∑i=i0+1mgi​(−w−1​Vi+1−w0​Vi−w1​Vi−1−w2​Vi−2)​Vi+gm​w−1​Vm​Vm+1\displaystyle\sum\_{i=i\_{0}+1}^{m}g\_{i}(-w\_{-1}V\_{i+1}-w\_{0}V\_{i}-w\_{1}V\_{i-1}-w\_{2}V\_{i-2})V\_{i}+g\_{m}w\_{-1}V\_{m}V\_{m+1} |  |
|  |  |  |
| --- | --- | --- |
|  | =∑i=0m−i0−1gi~​(w−1​V~i−1+w0​V~i+w1​V~i+1+w2​V~i+2)​V~i−g0~​w−1​V~−1​V~0\displaystyle=\sum\_{i=0}^{m-i\_{0}-1}\tilde{g\_{i}}(w\_{-1}\tilde{V}\_{i-1}+w\_{0}\tilde{V}\_{i}+w\_{1}\tilde{V}\_{i+1}+w\_{2}\tilde{V}\_{i+2})\tilde{V}\_{i}-\tilde{g\_{0}}w\_{-1}\tilde{V}\_{-1}\tilde{V}\_{0} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤(|w−1|−5​w2)​b~​Δ​x​∑i=i0+2mVi2−32​w2​b~​Δ​x​Vi0−12+(12​|w−1|−5​w2)​b~​Δ​x​Vi02+(|w−1|−5​w2)​b~​Δ​x​Vi0+12.\displaystyle\leq(|w\_{-1}|-5w\_{2})\tilde{b}\Delta x\sum\_{i=i\_{0}+2}^{m}V\_{i}^{2}-\frac{3}{2}w\_{2}\tilde{b}\Delta xV\_{i\_{0}-1}^{2}+(\frac{1}{2}|w\_{-1}|-5w\_{2})\tilde{b}\Delta xV\_{i\_{0}}^{2}+(|w\_{-1}|-5w\_{2})\tilde{b}\Delta xV\_{i\_{0}+1}^{2}. |  |

Adding up the sums for i<i0i<i\_{0} and i>i0i>i\_{0}, it follows that ⟨Dx​A~x​V,V⟩≤(|w−1|−10​w2)​b~​⟨V,V⟩\langle D\_{x}\tilde{A}\_{x}V,V\rangle\leq(|w\_{-1}|-10w\_{2})\tilde{b}\,\langle V,V\rangle for all vectors VV, which yields the bound on μ2​[Dx​A~x]\mu\_{2}[D\_{x}\tilde{A}\_{x}].
∎

## Appendix B Proof of Lemma [5.8](https://arxiv.org/html/2511.01587v1#Thmtheorem8 "Lemma 5.8. ‣ 5.2 Stability and convergence study ‣ 5 Convergence and stability analysis for the semidiscretisation approach ‣ Numerical methods for solving PIDEs arising in swing option pricing under a two-factor mean-reverting model with jumps")

###### Proof.

Let θ∈[14,12]\theta\in[\frac{1}{4},\frac{1}{2}].
We focus on the case where 0≤x<1θ0\leq x<\frac{1}{\theta}, since the result for the case x≤0x\leq 0 is known, see Cash [[1984](https://arxiv.org/html/2511.01587v1#bib.bib6)].
  
For any given x∈[0,1θ[x\in[0,\frac{1}{\theta}[ there holds

|  |  |  |
| --- | --- | --- |
|  | |Rθ​(x+i​y)|2=fθ​(y)gθ​(y)(y∈ℝ),|R\_{\theta}(x+iy)|^{2}=\frac{f\_{\theta}(y)}{g\_{\theta}(y)}\quad(y\in\mathbb{R}), |  |

where

|  |  |  |
| --- | --- | --- |
|  | fθ​(y)=(1+(1−2​θ)​x+(12−2​θ+θ2)​(x2−y2))2+((1−2​θ)​y+2​(12−2​θ+θ2)​x​y)2f\_{\theta}(y)=\big(1+(1-2\theta)x+(\frac{1}{2}-2\theta+\theta^{2})(x^{2}-y^{2})\big)^{2}+\big((1-2\theta)y+2(\frac{1}{2}-2\theta+\theta^{2})xy\big)^{2} |  |

and

|  |  |  |
| --- | --- | --- |
|  | gθ​(y)=((1−θ​x)2+(θ​y)2)2.g\_{\theta}(y)=\big((1-\theta x)^{2}+(\theta y)^{2}\big)^{2}. |  |

Note that gθ​(y)>0g\_{\theta}(y)>0 since 0≤θ​x<10\leq\theta x<1. We will prove that

|  |  |  |
| --- | --- | --- |
|  | fθ​(y)gθ​(y)≤fθ​(0)gθ​(0)\frac{f\_{\theta}(y)}{g\_{\theta}(y)}\leq\frac{f\_{\theta}(0)}{g\_{\theta}(0)} |  |

or, equivalently,

|  |  |  |
| --- | --- | --- |
|  | Hθ​(y):=fθ​(y)​gθ​(0)−gθ​(y)​fθ​(0)≤0.H\_{\theta}(y):=f\_{\theta}(y)g\_{\theta}(0)-g\_{\theta}(y)f\_{\theta}(0)\leq 0. |  |

Obviously, Hθ​(0)=0H\_{\theta}(0)=0. After some straightforward calculations, it follows that the first derivative of Hθ​(y)H\_{\theta}(y) can be written as

|  |  |  |
| --- | --- | --- |
|  | d​Hθd​y​(y)=2​y​Kθ​(y),\frac{dH\_{\theta}}{dy}(y)=2yK\_{\theta}(y), |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kθ​(y)\displaystyle K\_{\theta}(y) | ={−2(1+(1−2θ)x+(12−2θ+θ2)(x2−y2))(12−2θ+θ2)\displaystyle=\big\{-2\big(1+(1-2\theta)x+(\frac{1}{2}-2\theta+\theta^{2})(x^{2}-y^{2})\big)(\frac{1}{2}-2\theta+\theta^{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−2θ+2(12−2θ+θ2)x)2}(1−θx)4\displaystyle\quad+\big(1-2\theta+2(\frac{1}{2}-2\theta+\theta^{2})x\big)^{2}\big\}(1-\theta x)^{4} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −2​(1+(1−2​θ)​x+(12−2​θ+θ2)​x2)2​((1−θ​x)2+(θ​y)2)​θ2.\displaystyle\quad-2\big(1+(1-2\theta)x+(\frac{1}{2}-2\theta+\theta^{2})x^{2}\big)^{2}\big((1-\theta x)^{2}+(\theta y)^{2}\big)\theta^{2}. |  |

If it can be shown that Kθ​(y)≤0K\_{\theta}(y)\leq 0 (y∈ℝ)(y\in\mathbb{R}), then one obtains the desired result.
It is clear that Kθ​(y)K\_{\theta}(y) can be expressed as

|  |  |  |
| --- | --- | --- |
|  | Kθ​(y)=2​Kθ,1​(x)​y2+Kθ,2​(x)K\_{\theta}(y)=2K\_{\theta,1}(x)y^{2}+K\_{\theta,2}(x) |  |

with certain terms Kθ,1​(x)K\_{\theta,1}(x) and Kθ,2​(x)K\_{\theta,2}(x).
We will prove in the following that Kθ,1​(x)≤0K\_{\theta,1}(x)\leq 0 and Kθ,2​(x)≤0K\_{\theta,2}(x)\leq 0.

For Kθ,1​(x)K\_{\theta,1}(x) there holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kθ,1​(x)\displaystyle K\_{\theta,1}(x) | =Pθ,1​(x)2−Pθ,2​(x)2=(Pθ,1​(x)+Pθ,2​(x))​(Pθ,1​(x)−Pθ,2​(x)),\displaystyle=P\_{\theta,1}(x)^{2}-P\_{\theta,2}(x)^{2}=(P\_{\theta,1}(x)+P\_{\theta,2}(x))(P\_{\theta,1}(x)-P\_{\theta,2}(x)), |  |

where

|  |  |  |
| --- | --- | --- |
|  | Pθ,1​(x)=(12−2​θ+θ2)​(1−θ​x)2P\_{\theta,1}(x)=(\frac{1}{2}-2\theta+\theta^{2})(1-\theta x)^{2} |  |

and

|  |  |  |
| --- | --- | --- |
|  | Pθ,2​(x)=θ2​(1+(1−2​θ)​x+(12−2​θ+θ2)​x2).P\_{\theta,2}(x)=\theta^{2}\big(1+(1-2\theta)x+(\frac{1}{2}-2\theta+\theta^{2})x^{2}\big). |  |

We have

|  |  |  |
| --- | --- | --- |
|  | Pθ,1​(x)+Pθ,2​(x)=2​(θ−12)2+θ​x​Lθ​(x)\displaystyle P\_{\theta,1}(x)+P\_{\theta,2}(x)=2(\theta-\frac{1}{2})^{2}+\theta xL\_{\theta}(x) |  |

with

|  |  |  |
| --- | --- | --- |
|  | Lθ​(x)=4​(θ−14)​(1−θ)+2​(θ2−2​θ+12)​θ​x.L\_{\theta}(x)=4(\theta-\frac{1}{4})(1-\theta)+2(\theta^{2}-2\theta+\frac{1}{2})\theta x. |  |

It is easily seen that Lθ​(0)≥0L\_{\theta}(0)\geq 0 and Lθ​(1θ)≥0L\_{\theta}(\frac{1}{\theta})\geq 0. Since LθL\_{\theta} is linear in xx, it follows that Lθ​(x)≥0L\_{\theta}(x)\geq 0 and, hence, that

|  |  |  |
| --- | --- | --- |
|  | Pθ,1​(x)+Pθ,2​(x)≥0.P\_{\theta,1}(x)+P\_{\theta,2}(x)\geq 0. |  |

Next, one readily verifies that

|  |  |  |
| --- | --- | --- |
|  | Pθ,1​(x)−Pθ,2​(x)=−2​(θ−14)−θ​(1−3​θ)​x≤0.P\_{\theta,1}(x)-P\_{\theta,2}(x)=-2(\theta-\frac{1}{4})-\theta(1-3\theta)x\leq 0. |  |

Consequently, Kθ,1​(x)≤0K\_{\theta,1}(x)\leq 0.

For Kθ,2​(x)K\_{\theta,2}(x) we obtain after some tedious but straightforward calculations that

|  |  |  |
| --- | --- | --- |
|  | Kθ,2​(x)=12​x​(1−θ​x)2​Qθ​(x)K\_{\theta,2}(x)=\frac{1}{2}x(1-\theta x)^{2}Q\_{\theta}(x) |  |

with

|  |  |  |
| --- | --- | --- |
|  | Qθ​(x)=x2​(12​θ4−28​θ3+14​θ2−2​θ)+x​(−24​θ3+36​θ2−12​θ+1)+12​θ2−12​θ+2.Q\_{\theta}(x)=x^{2}\left(12\theta^{4}-28\theta^{3}+14\theta^{2}-2\theta\right)+x\left(-24\theta^{3}+36\theta^{2}-12\theta+1\right)+12\theta^{2}-12\theta+2. |  |

If θ∉{1−22,13}\theta\not\in\{1-\frac{\sqrt{2}}{2},\frac{1}{3}\}, then QθQ\_{\theta} is a second-degree polynomial in xx and its two roots are given by

|  |  |  |
| --- | --- | --- |
|  | 24​θ3−36​θ2+12​θ−1±(2​θ−1)​48​(θ+36)​(θ−14)​(θ−36)24​θ​(θ−(1−22))​(θ−13)​(θ−(1+22)).\frac{24\theta^{3}-36\theta^{2}+12\theta-1\pm(2\theta-1)\sqrt{48(\theta+\frac{\sqrt{3}}{6})(\theta-\frac{1}{4})(\theta-\frac{\sqrt{3}}{6})}}{24\theta(\theta-(1-\frac{\sqrt{2}}{2}))(\theta-\frac{1}{3})(\theta-(1+\frac{\sqrt{2}}{2}))}. |  |

We distinguish the following five cases, including that of the first-degree polynomial when θ∈{1−22,13}\theta\in\{1-\frac{\sqrt{2}}{2},\frac{1}{3}\}:

* •

  If θ∈{14,36}\theta\in\{\frac{1}{4},\frac{\sqrt{3}}{6}\}, then QθQ\_{\theta} has a double root that is real and negative and the graph of QθQ\_{\theta} is a downward parabola. Thus, Qθ​(x)≤0Q\_{\theta}(x)\leq 0.
* •

  If θ∈]14,36[\theta\in]\frac{1}{4},\frac{\sqrt{3}}{6}[, then the roots are not real numbers and the graph of QθQ\_{\theta} is a downward parabola. Thus, Qθ​(x)≤0Q\_{\theta}(x)\leq 0.
* •

  If θ∈]36,1−22[\theta\in]\frac{\sqrt{3}}{6},1-\frac{\sqrt{2}}{2}[, then both roots are real and negative and the graph of QθQ\_{\theta} is a downward parabola. Thus, Qθ​(x)≤0Q\_{\theta}(x)\leq 0.
* •

  If θ∈[1−22,13]\theta\in[1-\frac{\sqrt{2}}{2},\frac{1}{3}], then 12​θ4−28​θ3+14​θ2−2​θ≥012\theta^{4}-28\theta^{3}+14\theta^{2}-2\theta\geq 0 and, together with x<1θx<\frac{1}{\theta}, this yields

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Qθ​(x)\displaystyle Q\_{\theta}(x) | ≤x​(−12​θ3+8​θ2+2​θ−1)+12​θ2−12​θ+2.\displaystyle\leq x(-12\theta^{3}+8\theta^{2}+2\theta-1)+12\theta^{2}-12\theta+2. |  |

  Since 12​θ2−12​θ+2≤012\theta^{2}-12\theta+2\leq 0, there holds Qθ​(x)≤0Q\_{\theta}(x)\leq 0 whenever −12​θ3+8​θ2+2​θ−1≤0-12\theta^{3}+8\theta^{2}+2\theta-1\leq 0. Otherwise,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Qθ​(x)\displaystyle Q\_{\theta}(x) | ≤1θ​(−12​θ3+8​θ2+2​θ−1)+12​θ2−12​θ+2=−4​θ+4−1θ=−1θ​(2​θ−1)2≤0.\displaystyle\leq\frac{1}{\theta}(-12\theta^{3}+8\theta^{2}+2\theta-1)+12\theta^{2}-12\theta+2=-4\theta+4-\frac{1}{\theta}=-\frac{1}{\theta}(2\theta-1)^{2}\leq 0. |  |
* •

  If θ∈]13,12]\theta\in]\frac{1}{3},\frac{1}{2}], then it can be seen that Qθ​(1θ)≤0Q\_{\theta}(\frac{1}{\theta})\leq 0. Next, the graph of QθQ\_{\theta} is a downward parabola that attains its maximum at xtop=24​θ3−36​θ2+12​θ−14​θ​(6​θ3−14​θ2+7​θ−1)x\_{\text{top}}=\frac{24\theta^{3}-36\theta^{2}+12\theta-1}{4\theta\left(6\theta^{3}-14\theta^{2}+7\theta-1\right)}. It can be verified that xtop≥1θx\_{\text{top}}\geq\frac{1}{\theta}. Thus, Qθ​(x)≤0Q\_{\theta}(x)\leq 0.

Since Qθ​(x)≤0Q\_{\theta}(x)\leq 0, we have Kθ,2​(x)≤0K\_{\theta,2}(x)\leq 0. Combined with Kθ,1​(x)≤0K\_{\theta,1}(x)\leq 0, this gives the bound Kθ​(y)≤0K\_{\theta}(y)\leq 0.

The rational function RθR\_{\theta} is holomorphic on R​e​(z)<1θRe(z)<\frac{1}{\theta}. Thus, by the maximum modulus principle, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gθ​(x)\displaystyle G\_{\theta}(x) | =supR​e​(z)≤x|Rθ​(z)|=supR​e​(z)=x|Rθ​(z)|=Rθ​(x).\displaystyle=\sup\_{Re(z)\leq x}|R\_{\theta}(z)|=\sup\_{Re(z)=x}|R\_{\theta}(z)|=R\_{\theta}(x). |  |

Finally, it is easily seen for the second derivative of RθR\_{\theta} one has

|  |  |  |
| --- | --- | --- |
|  | d2​Rθd​x2​(x)=1+2​θ​(1−3​θ)​x(1−θ​x)2≥0(0≤x<1θ).\frac{d^{2}R\_{\theta}}{dx^{2}}(x)=\frac{1+2\theta(1-3\theta)x}{(1-\theta x)^{2}}\geq 0\quad(0\leq x<\frac{1}{\theta}). |  |

Thus RθR\_{\theta} is convex on [0,1θ[[0,\frac{1}{\theta}[ and consequently, if 0<ν<1θ0<\nu<\frac{1}{\theta}, then

|  |  |  |
| --- | --- | --- |
|  | Rθ​(x)≤1+Rθ​(ν)−1ν​x(0≤x≤ν).R\_{\theta}(x)\leq 1+\frac{R\_{\theta}(\nu)-1}{\nu}\,x\;\quad(0\leq x\leq\nu). |  |

∎