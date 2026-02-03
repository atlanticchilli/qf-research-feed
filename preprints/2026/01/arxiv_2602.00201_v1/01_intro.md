---
authors:
- Neetu Garg
- A. S. V. Ravi Kanth
doc_id: arxiv:2602.00201v1
family_id: arxiv:2602.00201
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Numerical Simulations for Time-Fractional Black Scholes Equations
url_abs: http://arxiv.org/abs/2602.00201v1
url_html: https://arxiv.org/html/2602.00201v1
venue: arXiv q-fin
version: 1
year: 2026
---


Neetu Garg
  
A.S.V. Ravi Kanth

###### Abstract

This paper implements an efficient numerical algorithm for the time-fractional Black-Scholes model governing European options. The proposed method comprises the Crank-Nicolson approach to discretize time variable and exponential B-spline approximation for space variable. The implemented method is unconditionally stable. We present few numerical examples to confirm the theory. Numerical simulations with comparisons exhibit the supremacy of the proposed approach.

###### keywords:

Caputo fractional derivative, Exponential B-spline, Black-Scholes equation, Stability

## 1 Introduction

Option pricing is a significantly crucial concept in the financial market. Black [[1](https://arxiv.org/html/2602.00201v1#bib.bib1)] and Merton [[2](https://arxiv.org/html/2602.00201v1#bib.bib2)] came up with the idea of the Black-Scholes equation for option pricing. There has been an enormous research activity in financial mathematics after the publication of the Black-Scholes model. Many researchers developed a huge interest in studying both theoretical and practical aspects of European options.

Recently, fractional calculus has gained huge attention as it provides an excellent instrument to characterize the memory phenomena due to the non-locality of fractional derivative [[3](https://arxiv.org/html/2602.00201v1#bib.bib3)]. The time-fractional Black-Scholes model (TFBSM) has received enormous popularity because of its ability to capture significant jumps during small time durations. At first, the European call option was priced by Wyss [[4](https://arxiv.org/html/2602.00201v1#bib.bib4)] via fractional model. In the literature, several analytical and numerical methods had been reported including, finite difference method, implicit finite difference method, compact difference scheme, integral discretization method, meshless method, residual power series method, moving least square method, radial basis functions, quintic B-spline method, finite element method [[5](https://arxiv.org/html/2602.00201v1#bib.bib5), [6](https://arxiv.org/html/2602.00201v1#bib.bib6), [7](https://arxiv.org/html/2602.00201v1#bib.bib7), [8](https://arxiv.org/html/2602.00201v1#bib.bib8), [9](https://arxiv.org/html/2602.00201v1#bib.bib9), [10](https://arxiv.org/html/2602.00201v1#bib.bib10), [11](https://arxiv.org/html/2602.00201v1#bib.bib11), [12](https://arxiv.org/html/2602.00201v1#bib.bib12), [13](https://arxiv.org/html/2602.00201v1#bib.bib13)].
This paper focuses on the following TFBSM:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂μ𝒲​(ζ,t)∂tμ+12​σ2​ζ2​∂2𝒲​(ζ,t)∂ζ2+(𝔯−𝔇)​ζ​∂𝒲​(ζ,t)∂ζ=𝔯​𝒲​(ζ,t),\displaystyle\frac{\partial^{\mu}\mathcal{W}(\zeta,t)}{\partial t^{\mu}}+\frac{1}{2}\sigma^{2}\zeta^{2}\frac{\partial^{2}\mathcal{W}(\zeta,t)}{\partial\zeta^{2}}+(\mathfrak{r}-\mathfrak{D})\zeta\frac{\partial\mathcal{W}(\zeta,t)}{\partial\zeta}=\mathfrak{r}\mathcal{W}(\zeta,t), |  | (1) |
|  |  |  |
| --- | --- | --- |
|  | (ζ,t)∈(0,∞)×(0,𝒯),0<μ≤1,\displaystyle(\zeta,t)\in(0,\infty)\times(0,\mathcal{T}),~0<\mu\leq 1, |  |

along with conditions

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒲​(ζ,𝒯)=𝒲​(ζ),𝒲​(0,t)=h1​(t),𝒲​(∞,t)=h2​(t),\mathcal{W}(\zeta,\mathcal{T})=\mathcal{W}(\zeta),\\ \mathcal{W}(0,t)=h\_{1}(t),\mathcal{W}(\infty,t)=h\_{2}(t), |  | (2) |

where 𝒲​(ζ,t)\mathcal{W}(\zeta,t) is the European option price with stock price ζ\zeta and current time tt, 𝔯\mathfrak{r} is the risk-free interest rate, 𝔇\mathfrak{D} is the dividend rate, σ\sigma is volatility and 𝒯\mathcal{T} is the expiry time. Here, the modified Riemann-Liouville fractional derivative ∂μ𝒲​(ζ,t)∂tμ\frac{\partial^{\mu}\mathcal{W}(\zeta,t)}{\partial t^{\mu}} is given as

|  |  |  |
| --- | --- | --- |
|  | ∂μ𝒲​(ζ,t)∂tμ={Γ​(1−μ)−1​dd​t​∫t𝒯𝒲​(ζ,α)−𝒲​(ζ,𝒯)(α−t)μ​𝑑α,0<μ<1∂𝒲​(ζ,t)∂t,μ=1\frac{\partial^{\mu}\mathcal{W}(\zeta,t)}{\partial t^{\mu}}=\left\{\begin{matrix}{\Gamma(1-\mu)}^{-1}\frac{d}{dt}\int\_{t}^{\mathcal{T}}\frac{\mathcal{W}(\zeta,\alpha)-\mathcal{W}(\zeta,\mathcal{T})}{(\alpha-t)^{\mu}}d\alpha,&0<\mu<1\\ \frac{\partial\mathcal{W}(\zeta,t)}{\partial t},&\mu=1\end{matrix}\right. |  |

Using the transformation t=𝒯−τt=\mathcal{T}-\tau (0<μ<10<\mu<1), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂μ𝒲​(ζ,t)∂tμ=−Γ​(1−μ)−1​dd​τ​∫0τ𝒲​(ζ,𝒯−β)−𝒲​(ζ,𝒯)(τ−β)μ​𝑑β.\displaystyle\frac{\partial^{\mu}\mathcal{W}(\zeta,t)}{\partial t^{\mu}}=-{\Gamma(1-\mu)}^{-1}\frac{d}{d\tau}\int\_{0}^{\tau}\frac{\mathcal{W}(\zeta,\mathcal{T}-\beta)-\mathcal{W}(\zeta,\mathcal{T})}{(\tau-\beta)^{\mu}}d\beta. |  | (3) |

Assuming y=ln⁡ζy=\ln\zeta and u​(y,τ)=𝒲​(ey,𝒯−τ)u(y,\tau)=\mathcal{W}(e^{y},\mathcal{T}-\tau), the model ([1](https://arxiv.org/html/2602.00201v1#S1.E1 "In 1 Introduction ‣ Numerical Simulations for Time-Fractional Black Scholes Equations"))-([2](https://arxiv.org/html/2602.00201v1#S1.E2 "In 1 Introduction ‣ Numerical Simulations for Time-Fractional Black Scholes Equations")) turns into

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Dτμ0​u​(y,τ)=σ22​∂2u​(y,τ)∂y2+(𝔯−σ22−𝔇)​∂u​(y,τ)∂y−𝔯​u​(y,τ)u​(−∞,τ)=h1​(τ),u​(∞,τ)=h2​(τ),u​(y,0)=u0​(y),\left\{\begin{matrix}{}\_{0}\textrm{D}\_{\tau}^{\mu}u(y,\tau)=\frac{\sigma^{2}}{2}\frac{\partial^{2}u(y,\tau)}{\partial y^{2}}+\left(\mathfrak{r}-\frac{\sigma^{2}}{2}-\mathfrak{D}\right)\frac{\partial u(y,\tau)}{\partial y}-\mathfrak{r}u(y,\tau)\\ u(-\infty,\tau)=h\_{1}(\tau),~u(\infty,\tau)=h\_{2}(\tau),\\ u(y,0)=u\_{0}(y),\end{matrix}\right. |  | (4) |

where Dτμ0​u​(y,τ){}\_{0}\textrm{D}\_{\tau}^{\mu}u(y,\tau) denotes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0Dτμu(y,τ)=Γ(1−μ)−1dd​τ∫0τu​(y,β)−u​(y,0)(τ−β)μdβ,0<μ<1.\displaystyle\_{0}\textrm{D}\_{\tau}^{\mu}u(y,\tau)={\Gamma(1-\mu)}^{-1}\frac{d}{d\tau}\int\_{0}^{\tau}\frac{u(y,\beta)-u(y,0)}{(\tau-\beta)^{\mu}}d\beta,0<\mu<1. |  | (5) |

For solving ([4](https://arxiv.org/html/2602.00201v1#S1.E4 "In 1 Introduction ‣ Numerical Simulations for Time-Fractional Black Scholes Equations")) numerically, the unbounded domain is truncated to a finite domain (ya,yb)(y\_{a},y\_{b}), for details see [[14](https://arxiv.org/html/2602.00201v1#bib.bib14)]. Thus we have the dimensionless model as [[15](https://arxiv.org/html/2602.00201v1#bib.bib15)]

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Dτμ​u​(y,τ)=κ1​∂2u​(y,τ)∂y2+κ2​∂u​(y,τ)∂y−κ3​u​(y,τ)+g​(y,τ),u​(ya,τ)=h1​(τ),u​(yb,τ)=h2​(τ),u​(y,0)=u0​(y),ya<y<yb,\displaystyle\left\{\begin{matrix}\textrm{D}\_{\tau}^{\mu}u(y,\tau)=\kappa\_{1}\frac{\partial^{2}u(y,\tau)}{\partial y^{2}}+\kappa\_{2}\frac{\partial u(y,\tau)}{\partial y}-\kappa\_{3}u(y,\tau)+g(y,\tau),\\ u(y\_{a},\tau)=h\_{1}(\tau),~u(y\_{b},\tau)=h\_{2}(\tau),\\ u(y,0)=u\_{0}(y),y\_{a}<y<y\_{b},\end{matrix}\right. |  | (6) |

where κ1=σ22>0\kappa\_{1}=\frac{\sigma^{2}}{2}>0, κ2=𝔯−𝔇−κ1\kappa\_{2}=\mathfrak{r}-\mathfrak{D}-\kappa\_{1}, κ3=𝔯>0\kappa\_{3}=\mathfrak{r}>0. Here we add the smooth force term g​(y,t)g(y,t) for validation purpose in section 5.

In this work, we present an efficient technique for the TFBSM. We first employ a Crank-Nicolson approach for discretizing time variable [[16](https://arxiv.org/html/2602.00201v1#bib.bib16)] and then exponential B-spline functions are used for approximating the resulting equation. We validate the proposed method via numerical experiments. To exhibit the efficiency of the proposed algorithm, we also carry out comparisons with the existing results.
It is noteworthy that the exponential B-spline method is one of the most robust numerical methods based on piecewise non-polynomial basis functions of class 𝒞2\mathcal{C}^{2} with compact support [[17](https://arxiv.org/html/2602.00201v1#bib.bib17)]. In contrast to the finite element method, it saves us from the computation of quadratures. In literature, the exponential B-spline method has contributed in solving a wide range of problems [[18](https://arxiv.org/html/2602.00201v1#bib.bib18), [19](https://arxiv.org/html/2602.00201v1#bib.bib19)].
The article is planned as follows. Section 2 develops the exponential B-spline approximation to TFBSM. Section 3 discusses stability analysis. In section 4, we study numerical results to assess the validity and accuracy of the proposed scheme. Finally, the main conclusions are summarized.

## 2 Methodology

In this section, we derive a numerical method by comprising a Crank-Nicolson approach for time variable and exponential B-spline approximation for the space variable.
To start, we first partition the solution domain [ya,yb]×[0,𝒯][y\_{a},y\_{b}]\times[0,\mathcal{T}] as

|  |  |  |
| --- | --- | --- |
|  | yj=j​Δ​y​(0≤j≤J),τn=n​Δ​τ​(0≤n≤𝒩)\displaystyle y\_{j}=j\Delta y~(0\leq j\leq J),~\tau\_{n}=n\Delta\tau~(0\leq n\leq\mathcal{N}) |  |

with space and time steps Δ​y=yb−yaJ\Delta y=\frac{y\_{b}-y\_{a}}{J} and Δ​τ=𝒯𝒩\Delta\tau=\frac{\mathcal{T}}{\mathcal{N}}, respectively.
  
Let u​(y,τ)∈𝒞(1)u(y,\tau)\in\mathcal{C}^{(1)} about time, the modified Riemann-Liouville derivative

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | Dτμ0​u​(y,τ)=Γ​(1−μ)−1​∫0τd​u​(y,β)d​β​(τ−β)−μ​𝑑β=0CDτμ​u​(y,τ){}\_{0}\textrm{D}\_{\tau}^{\mu}u(y,\tau)={\Gamma(1-\mu)}^{-1}\int\_{0}^{\tau}\frac{du(y,\beta)}{d\beta}(\tau-\beta)^{-\mu}d\beta=\_{0}^{C}\textrm{D}\_{\tau}^{\mu}u(y,\tau) |  | (7) |

Then, the Caputo derivative Dτμ0C​u{}\_{0}^{C}\textrm{D}\_{\tau}^{\mu}u at the node (y,τn+12)(y,\tau\_{n+\frac{1}{2}}) can be discretized as [[16](https://arxiv.org/html/2602.00201v1#bib.bib16)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Dτμ0C​u​(y,τn+12)=ϖ​(un+1​(y)−un​(y))+ν1​un​(y)−νn​u0​(y){}\_{0}^{C}\textrm{D}\_{\tau}^{\mu}u(y,\tau\_{n+\frac{1}{2}})=\varpi\left(u^{n+1}(y)-u^{n}(y)\right)+\nu\_{1}u^{n}(y)-\nu\_{n}u^{0}(y) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∑q=1n−1(νn−q+1−νn−q)​uq​(y)+O​(Δ​τ2−μ),0<μ<1\displaystyle+\sum\_{q=1}^{n-1}(\nu\_{n-q+1}-\nu\_{n-q})u^{q}(y)+O(\Delta\tau^{2-\mu}),~0<\mu<1 |  | (8) |

where

|  |  |  |
| --- | --- | --- |
|  | un+1​(y)=u​(y,τn+1),ϖ=2μ−1​Δ​τ−μ​Γ​(2−μ)−1,\displaystyle u^{n+1}(y)=u(y,\tau\_{n+1}),\varpi={2^{\mu-1}\Delta\tau^{-\mu}}{\Gamma(2-\mu)}^{-1}, |  |
|  |  |  |
| --- | --- | --- |
|  | νi=Δ​τμ​Γ​(2−μ)−1​((i+0.5)1−μ−(i−0.5)1−μ),(1≤i≤n).\displaystyle\nu\_{i}={\Delta\tau^{\mu}\Gamma(2-\mu)}^{-1}\left((i+0.5)^{1-\mu}-(i-0.5)^{1-\mu}\right),(1\leq i\leq n). |  |

  

Employing the Crank-Nicolson approach to ([6](https://arxiv.org/html/2602.00201v1#S1.E6 "In 1 Introduction ‣ Numerical Simulations for Time-Fractional Black Scholes Equations")) at (y,τn+12)(y,\tau\_{n+\frac{1}{2}}) and substituting ([2](https://arxiv.org/html/2602.00201v1#S2.Ex4 "2 Methodology ‣ Numerical Simulations for Time-Fractional Black Scholes Equations")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −κ1​∂2𝒰n+1​(y)∂y2−κ2​∂𝒰n+1​(y)∂y+(2​ϖ+κ3)​𝒰n+1​(y)\displaystyle-\kappa\_{1}\frac{\partial^{2}\mathcal{U}^{n+1}(y)}{\partial y^{2}}-\kappa\_{2}\frac{\partial\mathcal{U}^{n+1}(y)}{\partial y}+(2\varpi+\kappa\_{3})\mathcal{U}^{n+1}(y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =κ1​∂2𝒰n​(y)∂y2+κ2​∂𝒰n​(y)∂y+(2​ϖ−κ3)​𝒰n​(y)+2​gn+12\displaystyle=\kappa\_{1}\frac{\partial^{2}\mathcal{U}^{n}(y)}{\partial y^{2}}+\kappa\_{2}\frac{\partial\mathcal{U}^{n}(y)}{\partial y}+(2\varpi-\kappa\_{3})\mathcal{U}^{n}(y)+2g^{n+\frac{1}{2}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +2​(νn​𝒰0​(y)−ν1​𝒰n​(y)+∑q=1n−1(νn−q−νn−q+1)​𝒰q​(y)).\displaystyle+2\left(\nu\_{n}\mathcal{U}^{0}(y)-\nu\_{1}\mathcal{U}^{n}(y)+\sum\_{q=1}^{n-1}(\nu\_{n-q}-\nu\_{n-q+1})\mathcal{U}^{q}(y)\right). |  | (9) |

where gn+12=g​(y,τn+12)g^{n+\frac{1}{2}}=g(y,\tau\_{n+\frac{1}{2}}) for n=0,1,…,𝒩−1n=0,1,...,\mathcal{N}-1 and 𝒰n​(y)\mathcal{U}^{n}(y) as approximate solution of un​(y)u^{n}(y).
  
Next, we discretize the equation ([2](https://arxiv.org/html/2602.00201v1#S2.Ex7 "2 Methodology ‣ Numerical Simulations for Time-Fractional Black Scholes Equations")) using the exponential B-spline functions E​𝔅j​(y)E\mathfrak{B}\_{j}(y) (j=−1,0,…,J+1j=-1,0,...,J+1) defined in [[17](https://arxiv.org/html/2602.00201v1#bib.bib17)].
Clearly, the basis functions E​𝔅j​(y)E\mathfrak{B}\_{j}(y) are twice continuously differentiable and vanish outside [yj−2,yj+2][y\_{j-2},y\_{j+2}].
We approximate in space via B-spline functions as [[17](https://arxiv.org/html/2602.00201v1#bib.bib17)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒰​(y,τ)=∑j=−1J+1δj​(τ)​E​𝔅j​(y),\mathcal{U}(y,\tau)=\sum\_{j=-1}^{J+1}\delta\_{j}(\tau)E\mathfrak{B}\_{j}(y), |  | (10) |

where δj​(τ)\delta\_{j}(\tau) are undetermined coefficients to be computed. Using ([10](https://arxiv.org/html/2602.00201v1#S2.E10 "In 2 Methodology ‣ Numerical Simulations for Time-Fractional Black Scholes Equations")), E​𝔅j​(y)E\mathfrak{B}\_{j}(y) and its first two derivatives at the nodes yjy\_{j}’s  (j=0,1,…,J)(j=0,1,...,J) can be tabulated as follows:

Table 1: Values of exponential B-splines

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | yj−2y\_{j-2} | yj−1y\_{j-1} | yjy\_{j} | yj+1y\_{j+1} | yj+2y\_{j+2} |
| E​𝔅j​(y)E\mathfrak{B}\_{j}(y) | 0 | γ1\gamma\_{1} | 1 | γ1\gamma\_{1} | 0 |
| E​𝔅j′​(y)E\mathfrak{B}\_{j}^{{}^{\prime}}(y) | 0 | γ2\gamma\_{2} | 0 | -γ2\gamma\_{2} | 0 |
| E​𝔅j′′​(y)E\mathfrak{B}\_{j}^{{}^{\prime\prime}}(y) | 0 | γ3\gamma\_{3} | -2γ3\gamma\_{3} | γ3\gamma\_{3} | 0 |

where

|  |  |  |
| --- | --- | --- |
|  | γ1=s−𝔭​Δ​y2​(𝔭​Δ​y​c−s),γ2=𝔭​(1−c)2​(𝔭​Δ​y​c−s),γ3=𝔭2​s2​(𝔭​Δ​y​c−s).\gamma\_{1}=\frac{s-\mathfrak{p}\Delta y}{2(\mathfrak{p}\Delta yc-s)},\gamma\_{2}=\frac{\mathfrak{p}(1-c)}{2(\mathfrak{p}\Delta yc-s)},\gamma\_{3}=\frac{\mathfrak{p}^{2}s}{2(\mathfrak{p}\Delta yc-s)}. |  |

Here s=sinh⁡(𝔭​Δ​y),c=cosh⁡(𝔭​Δ​y)s=\sinh(\mathfrak{p}\Delta y),c=\cosh(\mathfrak{p}\Delta y) and 𝔭\mathfrak{p} is a non-negative parameter.
Using ([10](https://arxiv.org/html/2602.00201v1#S2.E10 "In 2 Methodology ‣ Numerical Simulations for Time-Fractional Black Scholes Equations")) and Table [1](https://arxiv.org/html/2602.00201v1#S2.T1 "Table 1 ‣ 2 Methodology ‣ Numerical Simulations for Time-Fractional Black Scholes Equations") in ([2](https://arxiv.org/html/2602.00201v1#S2.Ex7 "2 Methodology ‣ Numerical Simulations for Time-Fractional Black Scholes Equations")) at yjy\_{j}’s gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℑ1⁡δj−1n+1+ℑ2⁡δjn+1+ℑ3⁡δj+1n+1=φjn,0≤j≤J,0≤n≤𝒩−1,\displaystyle\Im\_{1}\delta\_{j-1}^{n+1}+\Im\_{2}\delta\_{j}^{n+1}+\Im\_{3}\delta\_{j+1}^{n+1}=\varphi\_{j}^{n},~0\leq j\leq J,~0\leq n\leq\mathcal{N}-1, |  | (11) |

where

|  |  |  |
| --- | --- | --- |
|  | φjn=ℑ4⁡δj−1n+ℑ5⁡δjn+ℑ6⁡δj+1n\displaystyle\varphi\_{j}^{n}=\Im\_{4}\delta\_{j-1}^{n}+\Im\_{5}\delta\_{j}^{n}+\Im\_{6}\delta\_{j+1}^{n} |  |
|  |  |  |
| --- | --- | --- |
|  | +2​(νn​𝒢j0−ν1​𝒢jn−∑q=1n−1(νn−q+1−νn−q)​𝒢jq)+2​gjn+12,\displaystyle+2\left(\nu\_{n}\mathcal{G}\_{j}^{0}-\nu\_{1}\mathcal{G}\_{j}^{n}-\sum\_{q=1}^{n-1}(\nu\_{n-q+1}-\nu\_{n-q})\mathcal{G}\_{j}^{q}\right)+2g\_{j}^{n+\frac{1}{2}}, |  |
|  |  |  |
| --- | --- | --- |
|  | ℑ1=γ1​(2​ϖ+κ3)−γ2​κ2−γ3​κ1,\displaystyle\Im\_{1}=\gamma\_{1}(2\varpi+\kappa\_{3})-\gamma\_{2}\kappa\_{2}-\gamma\_{3}\kappa\_{1}, |  |
|  |  |  |
| --- | --- | --- |
|  | ℑ2=2​ϖ+κ3+2​γ3​κ1,\displaystyle\Im\_{2}=2\varpi+\kappa\_{3}+2\gamma\_{3}\kappa\_{1}, |  |
|  |  |  |
| --- | --- | --- |
|  | ℑ3=γ1​(2​ϖ+κ3)+γ2​κ2−γ3​κ1,\displaystyle\Im\_{3}=\gamma\_{1}(2\varpi+\kappa\_{3})+\gamma\_{2}\kappa\_{2}-\gamma\_{3}\kappa\_{1}, |  |
|  |  |  |
| --- | --- | --- |
|  | ℑ4=γ1​(2​ϖ−κ3)+γ2​κ2+γ3​κ1,\displaystyle\Im\_{4}=\gamma\_{1}(2\varpi-\kappa\_{3})+\gamma\_{2}\kappa\_{2}+\gamma\_{3}\kappa\_{1}, |  |
|  |  |  |
| --- | --- | --- |
|  | ℑ5=2​ϖ−κ3−2​γ3​κ1,\displaystyle\Im\_{5}=2\varpi-\kappa\_{3}-2\gamma\_{3}\kappa\_{1}, |  |
|  |  |  |
| --- | --- | --- |
|  | ℑ6=γ1​(2​ϖ−κ3)−γ2​κ2+γ3​κ1\displaystyle\Im\_{6}=\gamma\_{1}(2\varpi-\kappa\_{3})-\gamma\_{2}\kappa\_{2}+\gamma\_{3}\kappa\_{1} |  |
|  |  |  |
| --- | --- | --- |
|  | 𝒢jm=γ1​δj−1m+δjm+γ1​δj+1m,m=0,1,…,n.\displaystyle\mathcal{G}\_{j}^{m}=\gamma\_{1}\delta\_{j-1}^{m}+\delta\_{j}^{m}+\gamma\_{1}\delta\_{j+1}^{m},m=0,1,...,n. |  |

To make system ([11](https://arxiv.org/html/2602.00201v1#S2.E11 "In 2 Methodology ‣ Numerical Simulations for Time-Fractional Black Scholes Equations")) solvable, we need two more equations in the form of following discretized boundary conditions

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | γ1​δ−1n+1+δ0n+1+γ1​δ1n+1=h1n+1,\displaystyle\gamma\_{1}\delta\_{-1}^{n+1}+\delta\_{0}^{n+1}+\gamma\_{1}\delta\_{1}^{n+1}=h\_{1}^{n+1}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | γ1​δJ−1n+1+δJn+1+γ1​δJ+1n+1=h2n+1.\displaystyle\gamma\_{1}\delta\_{J-1}^{n+1}+\delta\_{J}^{n+1}+\gamma\_{1}\delta\_{J+1}^{n+1}=h\_{2}^{n+1}. |  | (12) |

Eliminating δ−1\delta\_{-1} and δJ+1\delta\_{J+1} from ([2](https://arxiv.org/html/2602.00201v1#S2.Ex19 "2 Methodology ‣ Numerical Simulations for Time-Fractional Black Scholes Equations")) and together with ([11](https://arxiv.org/html/2602.00201v1#S2.E11 "In 2 Methodology ‣ Numerical Simulations for Time-Fractional Black Scholes Equations")), we get the system of J+1J+1 constrains in J+1J+1 variables which can be solved easily.

## 3 Stability Analysis

###### Theorem 3.1.

The proposed scheme ([11](https://arxiv.org/html/2602.00201v1#S2.E11 "In 2 Methodology ‣ Numerical Simulations for Time-Fractional Black Scholes Equations")) is stable unconditionally.

Remark The proof of the above theorem is on the similar lines as in [[18](https://arxiv.org/html/2602.00201v1#bib.bib18), [19](https://arxiv.org/html/2602.00201v1#bib.bib19)].

## 4 Numerical results and discussion

Consider the following model (c.f. [[9](https://arxiv.org/html/2602.00201v1#bib.bib9)]):

|  |  |  |
| --- | --- | --- |
|  | Dτμ0​u​(y,τ)=κ1​∂2u​(y,τ)∂y2+κ2​∂u​(y,τ)∂y−κ3​u​(y,τ)+g​(y,τ),{}\_{0}\textrm{D}\_{\tau}^{\mu}u(y,\tau)=\kappa\_{1}\frac{\partial^{2}u(y,\tau)}{\partial y^{2}}+\kappa\_{2}\frac{\partial u(y,\tau)}{\partial y}-\kappa\_{3}u(y,\tau)+g(y,\tau), |  |
|  |  |  |
| --- | --- | --- |
|  | u​(0,τ)=u​(1,τ)=0,\displaystyle u(0,\tau)=u(1,\tau)=0, |  |
|  |  |  |
| --- | --- | --- |
|  | u​(y,0)=y2​(1−y)\displaystyle u(y,0)=y^{2}(1-y) |  |

where

|  |  |  |
| --- | --- | --- |
|  | g​(y,τ)=(2​τ2−μΓ​(3−μ)+2​τ1−μΓ​(2−μ))​y2​(1−y)−(τ+1)2​[κ1​(2−6​y)+κ2​(2​y−3​y2)−κ3​y2​(1−y)].\displaystyle g(y,\tau)=\left(\frac{2\tau^{2-\mu}}{\Gamma(3-\mu)}+\frac{2\tau^{1-\mu}}{\Gamma(2-\mu)}\right)y^{2}(1-y)-(\tau+1)^{2}\left[\kappa\_{1}(2-6y)+\kappa\_{2}(2y-3y^{2})-\kappa\_{3}y^{2}(1-y)\right]. |  |

The exact solution is u​(y,τ)=(τ+1)2​y2​(1−y)u(y,\tau)=(\tau+1)^{2}y^{2}(1-y). We choose parameters as 𝔯=0.05,σ=0.25,𝔇=0,κ1=0.5​σ2,κ2=𝔯−a,κ3=𝔯\mathfrak{r}=0.05,\sigma=0.25,\mathfrak{D}=0,\kappa\_{1}=0.5\sigma^{2},\kappa\_{2}=\mathfrak{r}-a,\kappa\_{3}=\mathfrak{r} and 𝒯=1\mathcal{T}=1.
  
The computed errors and corresponding rate of convergence are listed in tables [2](https://arxiv.org/html/2602.00201v1#S4.T2 "Table 2 ‣ 4 Numerical results and discussion ‣ Numerical Simulations for Time-Fractional Black Scholes Equations") and [3](https://arxiv.org/html/2602.00201v1#S4.T3 "Table 3 ‣ 4 Numerical results and discussion ‣ Numerical Simulations for Time-Fractional Black Scholes Equations"). It is clearly seen from these tables that the proposed method is 2−μ2-\mu order accurate in time and obtains second order accuracy in space for different fractional orders. Table [4](https://arxiv.org/html/2602.00201v1#S4.T4 "Table 4 ‣ 4 Numerical results and discussion ‣ Numerical Simulations for Time-Fractional Black Scholes Equations")-[6](https://arxiv.org/html/2602.00201v1#S4.T6 "Table 6 ‣ 4 Numerical results and discussion ‣ Numerical Simulations for Time-Fractional Black Scholes Equations") yields comparison results that are in accordance with the results in [[9](https://arxiv.org/html/2602.00201v1#bib.bib9), [10](https://arxiv.org/html/2602.00201v1#bib.bib10), [20](https://arxiv.org/html/2602.00201v1#bib.bib20)].
Figure [1](https://arxiv.org/html/2602.00201v1#S4.F1 "Figure 1 ‣ 4 Numerical results and discussion ‣ Numerical Simulations for Time-Fractional Black Scholes Equations") plot 3-D graphs of numerical and exact solution for μ=0.5\mu=0.5. This figure clearly indicates the close proximity between the numerical and exact solutions. Figure [2](https://arxiv.org/html/2602.00201v1#S4.F2 "Figure 2 ‣ 4 Numerical results and discussion ‣ Numerical Simulations for Time-Fractional Black Scholes Equations") portrays exact and numerical solution profiles at different times for μ=0.5\mu=0.5 and 0.90.9. This figure presents how time affects the option pricing.

Table 2:

𝔏2\mathfrak{L}\_{2} error estimate with 𝔭=0.01\mathfrak{p}=0.01 and J=200J=200



𝒩\mathcal{N}
μ=0.9\mu=0.9
μ=0.7\mu=0.7
μ=0.5\mu=0.5
μ=0.3\mu=0.3


20
2.1966e-03
−-
8.8682e-04
−-
3.1351e-04
−-
9.2986e-05
−-

40
1.0204e-03
1.1061
3.5957e-04
1.3024
1.1134e-04
1.4935
2.9166e-05
1.6727

80
4.7504e-04
1.1030
1.4594e-04
1.3009
3.9499e-05
1.4951
9.1103e-06
1.6787

160
2.2138e-04
1.1015
5.9252e-05
1.3004
1.3997e-05
1.4967
2.8330e-06
1.6852

320
1.0322e-04
1.1008
2.4059e-05
1.3003
4.9530e-06
1.4987
8.7453e-07
1.6958

640
4.8138e-05
1.1005
9.7665e-06
1.3007
1.7482e-06
1.5024
2.6513e-07
1.7218

1280
2.2450e-05
1.1005
3.9620e-06
1.3016
6.1329e-07
1.5112
7.6072e-08
1.8013




Table 3:

𝔏2\mathfrak{L}\_{2} error estimate with 𝔭=1\mathfrak{p}=1 and Δ​τ=Δ​y2\Delta\tau={\Delta y}^{2}



JJ
μ=0.75\mu=0.75
μ=0.5\mu=0.5
μ=0.25\mu=0.25


8
3.6649e-04
−-
1.8191e-04
−-
1.5034e-04
−-

16
7.3066e-05
2.3265
3.9173e-05
2.2153
3.6042e-05
2.0605

32
1.5023e-05
2.2820
9.0355e-06
2.1162
8.8757e-06
2.0217

64
3.1943e-06
2.2336
2.1672e-06
2.0598
2.2074e-06
2.0075

128
7.0180e-07
2.1864
5.3059e-07
2.0302
5.5085e-07
2.0026




Table 4:

Results of comparison with 𝔭=0.1\mathfrak{p}=0.1, μ=0.7\mu=0.7 and J=150J=150



𝒩\mathcal{N}
Present method
Method in [[9](https://arxiv.org/html/2602.00201v1#bib.bib9)]
Method in [[20](https://arxiv.org/html/2602.00201v1#bib.bib20)]


𝔏∞\mathfrak{L}\_{\infty}
Rate
𝔏∞\mathfrak{L}\_{\infty}
Rate
𝔏∞\mathfrak{L}\_{\infty}
Rate


10
3.1579e-03
−-
5.8210e-03
−-
3.5000e-03
−-

20
1.2766e-03
1.3067
2.3040e-03
1.3372
1.4400e-03
1.3300

40
5.1746e-04
1.3028
9.0810e-04
1.3421
5.9000e-04
1.3150

80
2.0999e-04
1.3011
3.5720e-04
1.3461
2.4000e-04
1.3400

160
8.5257e-05
1.3004
1.4110e-04
1.3400
9.5000e-05
1.3600

320
3.4624e-05
1.3000
5.3870e-05
1.3892
3.8000e-05
1.3800




Table 5:

Results of comparison with 𝔭=0.01\mathfrak{p}=0.01 and J=100J=100




μ=0.9\mu=0.9
μ=0.5\mu=0.5

𝒩\mathcal{N}
Present method
Method in [[10](https://arxiv.org/html/2602.00201v1#bib.bib10)]
Present method
Method in [[10](https://arxiv.org/html/2602.00201v1#bib.bib10)]


256
1.9023e-04
−-
2.3339e-04
−-
9.9829e-06
−-
1.3091e-05
−-

512
8.8714e-05
1.1005
1.0896e-04
1.0989
3.5353e-06
1.4976
4.6540e-06
1.4920

1024
4.1380e-05
1.1002
5.0853e-05
1.0994
1.2518e-06
1.4978
1.6518e-06
1.4944

2048
1.9303e-05
1.1001
2.3729e-05
1.0997
4.4338e-07
1.4974
5.8557e-07
1.4961

4096
9.0050e-06
1.1000
1.1064e-05
1.1008
1.5731e-07
1.4949
2.0715e-07
1.4991




Table 6:

Results of comparison with 𝔭=0.1\mathfrak{p}=0.1




μ=0.2\mu=0.2
μ=0.7\mu=0.7

(J,𝒩)(J,\mathcal{N})
Present method
Method in [[9](https://arxiv.org/html/2602.00201v1#bib.bib9)]
Present method
Method in [[9](https://arxiv.org/html/2602.00201v1#bib.bib9)]


(4,4)
8.0178e-04
3.1280e-02
1.0060e-02
2.0560e-02

(8,64)
1.0281e-05
6.7910e-04
2.7454e-04
4.1590e-04

(16,1024)
6.4780e-07
2.5030e-05
7.9848e-06
1.6720e-05

(8,8)
1.9037e-04
1.3810e-02
4.1197e-03
1.0160e-02

(16,128)
2.9444e-06
5.2460e-04
1.1409e-04
3.2180e-04

(32,2048)
1.6358e-07
2.3070e-05
3.1896e-06
1.2730e-05



![Refer to caption](x1.png)


(a) Numerical solution

![Refer to caption](x2.png)


(b) Exact solution

Figure 1: Solution profiles with 𝔭=1\mathfrak{p}=1, 𝒩=J=50\mathcal{N}=J=50 and μ=0.5\mu=0.5



![Refer to caption](x3.png)


(a) μ=0.5\mu=0.5

![Refer to caption](x4.png)


(b) μ=0.9\mu=0.9

Figure 2: Numerical solution (+) and exact solution (solid) at different time levels with 𝔭=1\mathfrak{p}=1 and 𝒩=J=100\mathcal{N}=J=100

## 5 Conclusion

This work proposed an efficient computational technique incorporating the Crank-Nicolson approach in time and exponential B-splines in the space for solving TFBSM. The developed algorithm is unconditionally stable with second order space accuracy and 2−μ2-\mu order time accuracy. We have presented numerical simulations to indicate the supremacy of the proposed scheme for solving pricing problems. The influence of the fractional orders on option pricings is highlighted through various plots. The numerical results produced via the exponential B-spline method are in good accordance with the methods available in the literature.

## Acknowledgments

The authors would like to extend their gratitude to anonymous editors and reviewers for their suggestions.

## Financial disclosure

Dr. Neetu Garg is supported by Faculty Research Grant by National Institute of Technology Calicut.

## References

* [1]

  Black F., Scholes M.: The pricing of options and corporate liabilities. J Polit. Econ. 81:637–654 (1973).
* [2]

  Merton R.C.: Theory of rational option pricing. Bell. J. Econ. Manage. Sci. 4(1):141–183 (1973).
* [3]

  Podlubny I.: Fractional differential equations. Academic press, San Diego (1999).
* [4]

  Wyss W.: The fractional Black-Scholes equation. Fract. Calc. Appl. Anal. 3(3):51–-61 (2000).
* [5]

  Song L., Wang W.: Solution of the fractional Black-Scholes option pricing model by finite difference method. Abstr. Appl. Anal. (1-2):194286 (2013).doi:
* [6]

  Zhang H.,Liu F.,Turner I.,Yang Q.: Numerical solution of the time fractional Black-Scholes model governing European options. Comput. Math. Appl. 71(1-4):1771–1783 (2016).
* [7]

  Cen Z., Huang J., Xu A., Le A.: Numerical approximation of a time-fractional Black-Scholes equation. Comput. Math. Appl. 75:2874–-2887 (2018).
* [8]

  Haq S., Hussain M.: Selection of shape parameter in radial basis functions for solution of time-fractional Black-Scholes models. Appl. Math. Comput. 335:248–-263 (2018).
* [9]

  Golbabai A., Nikan O.: A computational method based on the moving least-squares approach for pricing double barrier options
  in a time-fractional Black-Scholes model. Comput. Econ. 79:479–497 (2019).
* [10]

  Roul P.: A high accuracy numerical method and its convergence for time-fractional Black-Scholes equation governing European options. Appl. Numer. Math. 151:472–493 (2020).
* [11]

  Ankur, Ram J., Naresh K.: Analysis and simulation of Korteweg-de Vries-Rosenau-regularised long-wave model via Galerkin finite element method. Comput. Math. Appl. 135:134–148 (2023).
* [12]

  Ankur, Ram J., Akil N.: Conformal Finite Element Methods for Nonlinear Rosenau-Burgers-Biharmonic Models. arXiv preprint, https://arxiv.org/abs/2402.08926.
* [13]

  Ankur, Ram J.: A new error estimates of finite element method for (2+ 1)-dimensional nonlinear advection-diffusion model. Appl. Numer. Math. 198:22–42 (2024).
* [14]
   Ankur, Ram J.: New multiple analytic solitonary solutions and simulation of (2+1)-dimensional generalized Benjamin-Bona-Mahony-Burgers model, Nonlinear Dynamics, Pages 13297–13325,(2023).
* [15]

  Zhang X., Yang J., Zhao Y.: Numerical Solution of Time Fractional Black–Scholes Model Based on Legendre Wavelet Neural Network with Extreme Learning Machine. Fractal Fract. 6:401 (2022).
* [16]

  Karatay I., Kale N., Bayramoglu S.R.: A new difference scheme for time fractional heat equations based on the Crank-Nicolson method. Frac. Calc. Appl. Anal. 16(4):892–910 (2013).
* [17]

  McCartin B.J.: Theory of exponential splines. J. Approx. Theory 66(1):1–23 (1991).
* [18]
  Ravi Kanth ASV, Neetu G.: An unconditionally stable algorithm for multiterm time fractional advection–diffusion equation with variable coefficients and convergence analysis. Numer Meth Part D E. 37(3) 1928–1945 (2020)
* [19]
  Ravi Kanth ASV, Neetu G.: A computational procedure and analysis for multi-term time-fractional Burgers-type equation. Numer Meth Part D E. 45(16) 9218-9232 (2022).
* [20]

  De Staelen R.H., Hendy A.S.: Numerically pricing double barrier options in a time-fractional Black-Scholes model. Comput. Math. Appl. 74:1166–1175 (2017).