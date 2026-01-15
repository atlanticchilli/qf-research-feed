---
authors:
- L. J. Espinosa González
- Erick Treviño Aguilar
doc_id: arxiv:2601.09074v1
family_id: arxiv:2601.09074
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'The Fourier estimator of spot volatility: Unbounded coefficients and jumps
  in the price process'
url_abs: http://arxiv.org/abs/2601.09074v1
url_html: https://arxiv.org/html/2601.09074v1
venue: arXiv q-fin
version: 1
year: 2026
---


L.J. Espinosa González
Instituto de Matemáticas, Unidad Cuernavaca, Universidad Nacional Autónoma de México, México
  
Erick Treviño-Aguilar
Instituto de Matemáticas, Unidad Cuernavaca, Universidad Nacional Autónoma de México, México.

###### Abstract

In this paper we study the Fourier estimator of Malliavin and Mancino for the spot volatility. We establish the convergence of the trigonometric polynomial to the volatility’s path in a setting that includes the following aspects. First, the volatility is required to satisfy a mild integrability condition, but otherwise allowed to be unbounded. Second, the price process is assumed to have cadlag paths, not necessarily continuous. We obtain convergence rates for the probability of a bad approximation in estimated coefficients, with a speed that allow to obtain an almost sure convergence and not just in probability in the estimated reconstruction of the volatility’s path. This is a new result even in the setting of continuous paths.
We prove that a rescaled trigonometric polynomial approximate the quadratic jump process.

Keywords. Fourier analysis; Fourier estimator of volatility; Itô processes.
  
  
AMS subject classification codes.

## 1 Introduction

In this paper we study the Fourier estimator of Malliavin and Mancino for the spot volatility introduced in the seminal papers [[9](https://arxiv.org/html/2601.09074v1#bib.bib9), [8](https://arxiv.org/html/2601.09074v1#bib.bib8)]. We establish the convergence of the trigonometric polynomial to the volatility’s path in a setting that includes the following aspects. First, the volatility is required to satisfy a mild integrability condition, but otherwise allowed to be unbounded. Second, the price process is assumed to have cadlag paths, not necessarily continuous. We obtain convergence rates for the probability of a bad approximation in estimated coefficients and paths, with a speed that allow to obtain an almost sure convergence and not just in probability. This is a new result even in the setting of continuous paths. Seemingly surprising, determining the effect of jumps in the price’s dynamic only requires additional mild integrability conditions. Not a real surprise, since a key first estimation is based on the Burkholder-Davis-Gundy inequality. We will prove that a minor “correction”, of rescaling type, allows to asymptotically recover the quadratic jump process. The effect of jumps in the Fourier estimator is indeed a question of practical relevance, since the presence of jumps in asset prices is a well recognized stylized fact. For example, the authors of the paper [[10](https://arxiv.org/html/2601.09074v1#bib.bib10)] present statistical evidence in which index returns “tend to be pure jump processes”. Thus, it is natural to ask: What is the effect of jumps in the Fourier estimator?, and this question has already been formulated by a few authors; see [[3](https://arxiv.org/html/2601.09074v1#bib.bib3), Remark 3.2] and [[6](https://arxiv.org/html/2601.09074v1#bib.bib6), p. 369]. In this paper we present progress in this direction.

We will focus in the one dimensional case, both in the number of assets and the number of stochastic sources. Mainly for notational simplicity and because the fundamental complications already appear in this setting.

The paper is organized as follows. In Section [2](https://arxiv.org/html/2601.09074v1#S2 "2 The price process ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process") we fix a model for a price process with continuous paths. In Section [3](https://arxiv.org/html/2601.09074v1#S3 "3 Preliminaries ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process") we give a few general preliminaries. In Section [4](https://arxiv.org/html/2601.09074v1#S4 "4 The Fourier coefficients of volatility ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process") we present the Fourier estimator of volatility due to Malliavin and Mancino [[8](https://arxiv.org/html/2601.09074v1#bib.bib8), [9](https://arxiv.org/html/2601.09074v1#bib.bib9)]. In Section [5](https://arxiv.org/html/2601.09074v1#S5 "5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process") we start with a continuous dynamic for the price process and prove the uniform convergence of Fourier-Fejér trigonometric polynomials constructed with two different systems of coefficients. The first one is estimated in the ideal situation of having information of the volatility’s path. This is a an unfeasible situation in a practical implementation but crucial as a benchmark. The second system is calculated through the so called Bohr-convolution of coefficients which is the essence of the Fourier estimator of Malliavin and Mancino. This is an admissible estimation in that it is constructed from “observable quantities”. We assume continuous observation of the price’s path, and in Section [6](https://arxiv.org/html/2601.09074v1#S6 "6 Discrete observation ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process") we develop the respective theory in the more realistic situation of a discrete observation and no access to the volatility’s path. In Section [7](https://arxiv.org/html/2601.09074v1#S7 "7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process") we extend previous results with continuous observation to a dynamic with jumps for the price process. We prove that in this setting, rescaled trigonometric polynomials obtained through Bohr convolution converge to the process of quadratic jumps. In Section [7.6](https://arxiv.org/html/2601.09074v1#S7.SS6 "7.6 Numerical illustrations: Poisson process ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process") we illustrate the results with numerical simulations.

## 2 The price process

We will work with Fourier series and therefore it is convenient to take as time index the interval [−π,π][-\pi,\pi]. Fix a probability space (,ℱ,F={ℱt}−π≤t≤π,P)(\Omega,\mathscr{F},\mathbb{F}=\{\mathscr{F}\_{t}\}\_{-\pi\leq t\leq\pi},P) satisfying the usual conditions, where a Brownian motion WW is defined. Denote by HH the stochastic process solving the SDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Ht\displaystyle dH\_{t} | =σt​d​Wt, with ​H−π=x∈R,\displaystyle=\sigma\_{t}dW\_{t},\text{ with }H\_{-\pi}=x\in\mathbb{R}, |  | (1) |

for σ\sigma a progressively measurable process with continuous paths. We interpret HH as the logarithmic price of a risky asset.

###### Remark 1.

We do not include a drift term in the dynamic ([1](https://arxiv.org/html/2601.09074v1#S2.E1 "In 2 The price process ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")), mainly for simplicity. Indeed, it is well known from the paper [[9](https://arxiv.org/html/2601.09074v1#bib.bib9)] that this term has zero contribution in the Fourier estimator.

Further integrability conditions are formulated in the following assumption.

###### Assumption 1.

For 𝗁>0\mathsf{h}>0, the process σ\sigma satisfies

|  |  |  |
| --- | --- | --- |
|  | E​[∫−ππσz𝗁​𝑑z]<∞.E\left[\intop\nolimits\_{-\pi}^{\pi}\sigma^{\mathsf{h}}\_{z}dz\right]<\infty. |  |

###### Remark 2.

More specific information of the exponent 𝗁\mathsf{h} in ?THM? LABEL:lab:integrabilityforsigma will be given in our results about convergence; see ?THM?s LABEL:labthm:coeffConvergence and LABEL:labthm:PathUC below.

The stochastic differential equation d​Ht=f​(t,Ht)​d​WtdH\_{t}=f(t,H\_{t})dW\_{t} has a strong unique solution under a mild condition on the measurable function ff; see ?THM? LABEL:labtheasydiffusions in the appendix. In this case the coefficient σt:=f​(t,Ht)\sigma\_{t}:=f(t,H\_{t}) will satisfy ?THM? LABEL:lab:integrabilityforsigma for an arbitrarily large exponent 𝗁\mathsf{h}; see ?THM? LABEL:labtheasydiffusionscorollaryintegrability.

The volatility process 𝗏:={𝗏t}−π≤t≤π\mathsf{v}:=\{\mathsf{v}\_{t}\}\_{-\pi\leq t\leq\pi}, is defined as the square of the diffusion coefficient:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝗏t\displaystyle\mathsf{v}\_{t} | :=σt2.\displaystyle:=\sigma^{2}\_{t}. |  | (2) |

## 3 Preliminaries

We start with some notation. Let a:={an}n∈Na:=\{a\_{n}\}\_{n\in\mathbb{N}} and b:={bn}n∈Nb:=\{b\_{n}\}\_{n\in\mathbb{N}} be two sequences of non negative real numbers. We write a=O​(b)a=O(b) if there exists a constant K>0K>0 such that an≤K​bna\_{n}\leq Kb\_{n} for n∈Nn\in\mathbb{N}. We denote by ı\imath the imaginary number, solution of x2=−1x^{2}=-1.

We denote by DN:[−π,π]→CD\_{N}:[-\pi,\pi]\to\mathbb{C} the Dirichlet kernel that includes 2​N+12N+1 harmonics. It is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | DN​(t):=∑|l|≤Nexp⁡(ı​l​t).D\_{N}(t):=\sumop\displaylimits\_{|l|\leq N}\exp(\imath lt). |  | (3) |

We also introduce the rescaled Dirichlet kernel:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D~N​(t):=12​N+1​DN​(t).\tilde{D}\_{N}(t):=\frac{1}{2N+1}D\_{N}(t). |  | (4) |

We denote by SN​[ϕ]S\_{N}[\phi] the partial sum of the Fourier series of a function ϕ\phi:

|  |  |  |
| --- | --- | --- |
|  | SN​[ϕ]​(t):=∑|n|≤Nℱ​[ϕ]​(n)​eı​n​t.S\_{N}[\phi](t):=\sumop\displaylimits\_{|n|\leq N}\mathscr{F}[\phi](n)e^{\imath nt}. |  |

The Dirichlet kernel allows to express the partial sums of Fourier series as a convolution:

|  |  |  |
| --- | --- | --- |
|  | SN​[ϕ]​(t)=ϕ∗DN​(t):=12​π​∫−ππϕ​(s)​DN​(t−s)​𝑑s;S\_{N}[\phi](t)=\phi\*D\_{N}(t):=\frac{1}{2\pi}\intop\nolimits\_{-\pi}^{\pi}\phi(s)D\_{N}(t-s)ds; |  |

see [[14](https://arxiv.org/html/2601.09074v1#bib.bib14), p. 44].

The Fejér kernel is defined by

|  |  |  |
| --- | --- | --- |
|  | 𝐅N​(t):=1N​∑j=0N−1DN​(t).{\mathbf{F}}\_{N}(t):=\frac{1}{N}\sumop\displaylimits\_{j=0}^{N-1}D\_{N}(t). |  |

Now we continue with a few basic concepts for martingales. For a process XX we denote, as usual, its running supremum by X∗X^{\*}, hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt∗:=sup−π≤s≤t|Xs|.X^{\*}\_{t}:=\sup\_{-\pi\leq s\leq t}|X\_{s}|. |  | (5) |

For KK a local martingale with cadlag paths, and K−π=0K\_{-\pi}=0 we denote by [K]\left[K\right] its quadratic variation. Recall the Burkholder-Davis-Gundy inequality (BDG inequality) in the following form. For p>1p>1 there exist positive constants cpc\_{p} and CpC\_{p} such that for a stopping time τ\tau

|  |  |  |
| --- | --- | --- |
|  | cp​E​[[K]τp/2]≤E​[(Kτ∗)p]≤Cp​E​[[K]τp/2];c\_{p}E[\left[K\right]\_{\tau}^{p/2}]\leq E[(K^{\*}\_{\tau})^{p}]\leq C\_{p}E[\left[K\right]\_{\tau}^{p/2}]; |  |

see [[13](https://arxiv.org/html/2601.09074v1#bib.bib13), Theorem 10.36].

Furthermore, if KK has continuous paths we consider the BDG inequality in the following form. Denote by ⟨K⟩\left\langle K\right\rangle the predictable quadratic variation of KK. For p>0p>0 there exist positive constants cpc\_{p} and CpC\_{p} such that for τ\tau a stopping time

|  |  |  |
| --- | --- | --- |
|  | cp​E​[⟨K⟩τp/2]≤E​[(Kτ∗)p]≤Cp​E​[⟨K⟩τp/2];c\_{p}E[\left\langle K\right\rangle\_{\tau}^{p/2}]\leq E[(K^{\*}\_{\tau})^{p}]\leq C\_{p}E[\left\langle K\right\rangle\_{\tau}^{p/2}]; |  |

see [[12](https://arxiv.org/html/2601.09074v1#bib.bib12), (4.1)].

We will also work with complex valued processes. For X=ℜ⁡X+ı​ℑ⁡XX=\Re X+\imath\Im X a complex valued process, we adapt the notation for the running supremum ([5](https://arxiv.org/html/2601.09074v1#S3.E5 "In 3 Preliminaries ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Xt∗\displaystyle X^{\*}\_{t} | :=sup−π≤s≤t|ℜ⁡Xs|+sup−π≤s≤t|ℑ⁡Xs|.\displaystyle:=\sup\_{-\pi\leq s\leq t}|\Re X\_{s}|+\sup\_{-\pi\leq s\leq t}|\Im X\_{s}|. |  | (6) |

Furthermore, for p≥2p\geq 2, we denote by |||X|||p\left\lvert\!\left\lvert\!\left\lvert X\right\rvert\!\right\rvert\!\right\rvert\_{p} the following norm

|  |  |  |  |
| --- | --- | --- | --- |
|  | |||X|||p:=E​[(sup−π≤s≤π|ℜ⁡Xs|)p]p+E​[(sup−π≤s≤π|ℑ⁡Xs|)p]p.\left\lvert\!\left\lvert\!\left\lvert X\right\rvert\!\right\rvert\!\right\rvert\_{p}:=\sqrt[p]{E\left[\left(\sup\_{-\pi\leq s\leq\pi}|\Re X\_{s}|\right)^{p}\right]}+\sqrt[p]{E\left[\left(\sup\_{-\pi\leq s\leq\pi}|\Im X\_{s}|\right)^{p}\right]}. |  | (7) |

Note the triangle inequality in this notation:

|  |  |  |
| --- | --- | --- |
|  | ‖Xt∗‖Lp≤|||X|||p.\left\|X^{\*}\_{t}\right\|\_{L\_{p}}\leq\left\lvert\!\left\lvert\!\left\lvert X\right\rvert\!\right\rvert\!\right\rvert\_{p}. |  |

## 4 The Fourier coefficients of volatility

### 4.1 Basic definitions on Fourier analysis

For q∈Zq\in\mathbb{Z}, the qq-th Fourier coefficient of a function ϕ:[−π,π]→R\phi:[-\pi,\pi]\to\mathbb{R} is denoted ℱ​[ϕ]​(q)\mathscr{F}[\phi](q). It is defined by

|  |  |  |
| --- | --- | --- |
|  | ℱ​[ϕ]​(q):=12​π​∫−ππe−ı​q​t​ϕ​(t)​𝑑t.\mathscr{F}[\phi](q):=\frac{1}{2\pi}\intop\nolimits\_{-\pi}^{\pi}e^{-\imath qt}\phi(t)dt. |  |

The Fourier coefficient of a differential is given by

|  |  |  |
| --- | --- | --- |
|  | ℱ​[d​ϕ]​(q):=12​π​∫−ππe−ı​q​t​𝑑ϕt, for ​q∈Z.\mathscr{F}[d\phi](q):=\frac{1}{2\pi}\intop\nolimits\_{-\pi}^{\pi}e^{-\imath qt}d\phi\_{t},\mbox{ for }q\in\mathbb Z. |  |

Clearly, further conditions on ϕ\phi are necessary for this definition to be correct. For Riemann-Stieltjes integration under a pathwise perspective it is sufficient that ϕ\phi is cadlag since the exponential is a smooth function. Indeed this follows by integration by parts; see [[1](https://arxiv.org/html/2601.09074v1#bib.bib1), Theorem 7.6]. For the stochastic complement see e.g., [[12](https://arxiv.org/html/2601.09074v1#bib.bib12), Proposition (2.13)] and [[11](https://arxiv.org/html/2601.09074v1#bib.bib11), Theorem II.17].

### 4.2 The Bohr convolution

Malliavin and Mancino [[9](https://arxiv.org/html/2601.09074v1#bib.bib9)] define the Bohr convolution and we recall it now. Let u,v:Z→Cu,v:\mathbb Z\to\mathbb{C} be two complex valued functions. The Bohr convolution of uu and vv denoted uvu\mathbin{\circledast}v is defined if the following limit exists for each q∈Zq\in\mathbb Z

|  |  |  |  |
| --- | --- | --- | --- |
|  | (uv)​(q):=limN→∞12​N+1​∑|l|≤Nu​(l)​v​(q−l).(u\mathbin{\circledast}v)(q):=\lim\_{N\to\infty}\frac{1}{2N+1}\sumop\displaylimits\_{|l|\leq N}u(l)v(q-l). |  | (8) |

In this case, the convolution is again a complex valued function with domain Z\mathbb{Z}. It will be useful to introduce the following notation for the partial sums in the Bohr convolution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (u​Nv)​(q):=12​N+1​∑|l|≤Nu​(l)​v​(q−l).(u\mathop{\circledast}\limits\_{N}v)(q):=\frac{1}{2N+1}\sumop\displaylimits\_{|l|\leq N}u(l)v(q-l). |  | (9) |

Hence,

|  |  |  |
| --- | --- | --- |
|  | (uv)​(q)=limN→∞(u​Nv)​(q).(u\mathbin{\circledast}v)(q)=\lim\_{N\to\infty}(u\mathop{\circledast}\limits\_{N}v)(q). |  |

## 5 Continuous observation of the price’s path

A fundamental observation in the papers [[8](https://arxiv.org/html/2601.09074v1#bib.bib8)] and [[9](https://arxiv.org/html/2601.09074v1#bib.bib9)] is that the system of Fourier coefficients ℱ​[𝗏]\mathscr{F}[\mathsf{v}] computed with information in the non observable spot volatility 𝗏\mathsf{v} decomposes into two parts, a first part given by ℱ​[𝗏]\mathscr{F}[\mathsf{v}], defined below, which is obtained through Bohr’s convolution of complex valued functions constructed with ‘observable information’ provided by d​HdH (rigorously through pathwise Itô integral), and a second part that under general conditions is a “remainder”, in that, under suitable conditions it converges to zero for N→∞N\to\infty. We formulate this as ?THM? LABEL:labth:fundamentalobservation below due to its fundamental importance. Before that, we introduce notation. For q∈Zq\in\mathbb{Z} we define the process (q)\Gamma(q) on [−π,π][-\pi,\pi] by

|  |  |  |
| --- | --- | --- |
|  | (q)z=[dH]z(q):=12​π∫−πze−ı​q​tdHt,(q)−π=0,z∈[−π,π].{}\_{z}(q)={}\_{z}[dH](q):=\frac{1}{2\pi}\intop\nolimits\_{-\pi}^{z}e^{-\imath qt}dH\_{t},\quad{}\_{-\pi}(q)=0,\quad z\in[-\pi,\pi]. |  |

###### Definition 1.

Let

|  |  |  |
| --- | --- | --- |
|  | ℱ[dH](q):=(q)π.\mathscr{F}[dH](q):={}\_{\pi}(q). |  |

The system of coefficients {ℱN​[𝗏]}N∈N\{\mathscr{F}\_{N}[\mathsf{v}]\}\_{N\in\mathbb{N}} is defined by

|  |  |  |
| --- | --- | --- |
|  | ℱN​[𝗏]​(q):=2​π​{ℱ​[d​H]​Nℱ​[d​H]}​(q),q∈Z.\mathscr{F}\_{N}[\mathsf{v}](q):=2\pi\left\{\mathscr{F}[dH]\mathop{\circledast}\limits\_{N}\mathscr{F}[dH]\right\}(q),\quad q\in\mathbb{Z}. |  |

Now we define the Fourier estimator of Malliavin and Mancino under continuous observation. The Fourier estimator of 𝗏\mathsf{v} is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯N,M​[𝗏]​(t):=∑|l|≤M(1−|l|M)​ℱN​[𝗏]​(l)​eı​l​t.\mathscr{T}\_{N,M}[\mathsf{v}](t):=\sumop\displaylimits\_{|l|\leq M}\left(1-\frac{|l|}{M}\right)\mathscr{F}\_{N}[\mathsf{v}](l)e^{\imath lt}. |  | (10) |

After preliminary notation now we have the following fundamental result.

###### Proposition 1.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱ​[𝗏]​(q)=ℱN​[𝗏]​(q)−𝖱π​(q,N),\mathscr{F}[\mathsf{v}](q)=\mathscr{F}\_{N}[\mathsf{v}](q)-\mathsf{R}\_{\pi}(q,N), |  | (11) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖱t(q,N):=2​π2​N+1∑|l|≤N{∫−πt(q−l)zd(l)z+∫−πt(l)zd(q−l)z}.\mathsf{R}\_{t}(q,N):=\frac{2\pi}{2N+1}\sumop\displaylimits\_{|l|\leq N}\left\{\intop\nolimits\_{-\pi}^{t}{}\_{z}(q-l)d{}\_{z}(l)+\intop\nolimits\_{-\pi}^{t}{}\_{z}(l)d{}\_{z}(q-l)\right\}. |  | (12) |

Equation ([11](https://arxiv.org/html/2601.09074v1#S5.E11 "In Proposition 1. ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) suggests that the Fourier coefficients ℱ​[𝗏]\mathscr{F}[\mathsf{v}] can be approximated by the sequence of Bohr convolutions {ℱN​[𝗏]}N∈N\{\mathscr{F}\_{N}[\mathsf{v}]\}\_{N\in\mathbb{N}}. This has been proved by [[9](https://arxiv.org/html/2601.09074v1#bib.bib9)] under suitable integrability conditions. In this section we prove that 𝖱π​(q,N)\mathsf{R}\_{\pi}(q,N) converges to zero a.s., generalizing to our setting this approximation. We give convergence rates that allow to obtain a uniform convergence, in a precise sense, for coefficients of order qq in a band of the form |q|≤N|q|\leq N. From this uniform convergence we derive that the corresponding trigonometric polynomial with Cesàro means of coefficients ℱN​[𝗏]\mathscr{F}\_{N}[\mathsf{v}] converge uniformly to the corresponding polynomial with coefficients ℱ​[𝗏]\mathscr{F}[\mathsf{v}]; see ?THM? LABEL:labthm:PathUC below.

### 5.1 Error’s representation

We denote by D~\tilde{D} the “rescaled” Dirichlet kernel 12​N+1​DN\frac{1}{2N+1}D\_{N}; see ([4](https://arxiv.org/html/2601.09074v1#S3.E4 "In 3 Preliminaries ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")). In this section we give a convenient representation for the remainder 𝖱π​(q,N)\mathsf{R}\_{\pi}(q,N).
For t∈[−π,π]t\in[-\pi,\pi], define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξz​(q,N,t)\displaystyle\xi\_{z}(q,N,t) | :=∫−πze−ı​q​s​D~N​(t−s)​𝑑Hs,ξ−π​(q,N,t)=0,z∈[−π,t],\displaystyle:=\intop\nolimits\_{-\pi}^{z}e^{-\imath q{s}}\tilde{D}\_{N}({t}-{s})dH\_{s},\quad\xi\_{-\pi}(q,N,t)=0,\quad z\in[-\pi,t], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt​(q,N)\displaystyle Y\_{t}(q,N) | :=∫−πtξs​(q,N,s)​𝑑Hs,Y−π​(q,N)=0,\displaystyle:=\intop\nolimits\_{-\pi}^{t}\xi\_{s}(q,N,s)dH\_{s},\quad Y\_{-\pi}(q,N)=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt​(q,N)\displaystyle Z\_{t}(q,N) | :=∫−πte−ı​q​s​𝑑Ys​(0,N),Z−π​(q,N)=0.\displaystyle:=\intop\nolimits\_{-\pi}^{t}e^{-\imath q{s}}dY\_{s}(0,N),\quad Z\_{-\pi}(q,N)=0. |  |

The proof of the next result is straightforward and we omit it.

###### Lemma 2.

We have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​π​𝖱π​(q,N)\displaystyle 2\pi\mathsf{R}\_{\pi}(q,N) | =∫−ππ𝑑Hz​∫−πze−ı​q​s​D~N​(s−z)​𝑑Hs+∫−ππe−ı​q​z​𝑑Hz​∫−πzD~N​(z−s)​𝑑Hs\displaystyle=\intop\nolimits\_{-\pi}^{\pi}dH\_{z}\intop\nolimits\_{-\pi}^{z}e^{-\imath qs}\tilde{D}\_{N}(s-z)dH\_{s}+\intop\nolimits\_{-\pi}^{\pi}e^{-\imath qz}dH\_{z}\intop\nolimits\_{-\pi}^{z}\tilde{D}\_{N}(z-s)dH\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Yπ​(q,N)+Zπ​(q,N).\displaystyle=Y\_{\pi}(q,N)+Z\_{\pi}(q,N). |  |

### 5.2 A key estimation: The remainder’s Lp\mathbb{L}\_{p}-norm

Let p>2p>2 and α,β∈(1,∞)\alpha,\beta\in(1,\infty) with 1α+1β=1\frac{1}{\alpha}+\frac{1}{\beta}=1. In this section we assume that σ\sigma satisfies the ?THM? LABEL:lab:integrabilityforsigma with exponent 𝗁=p​(α∨β)\mathsf{h}=p(\alpha\vee\beta). In this case, the following constant is finite:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (K~p,α,β)p:=2p​Cp​(2​π)p2−1​2​π​Cp​ββ​E​[∫−ππσsp​α​𝑑s]α​E​[(∫−ππσs2​α​𝑑s)p​β2​α]β,\left(\tilde{K}\_{p,\alpha,\beta}\right)^{p}:=2^{p}C\_{p}(2\pi)^{\frac{p}{2}-1}\sqrt[\beta]{2\pi C\_{p\beta}}\sqrt[\alpha]{E\left[\intop\nolimits\_{-\pi}^{\pi}\sigma^{p\alpha}\_{s}ds\right]}\sqrt[\beta]{E\left[\left(\intop\nolimits\_{-\pi}^{\pi}\sigma^{2\alpha}\_{s}ds\right)^{\frac{p\beta}{2\alpha}}\right]}, |  | (13) |

where CpC\_{p} and Cβ​pC\_{\beta p} are the constants in the BDG inequality with the obvious exponents, and B2​βB\_{2\beta} is the constant in ?THM? LABEL:labLemma:DirichletkernelEstimation below for r=2​βr=2\beta.

Recall the norm |||⋅|||p\left\lvert\!\left\lvert\!\left\lvert\cdot\right\rvert\!\right\rvert\!\right\rvert\_{p} for a complex valued process in ([7](https://arxiv.org/html/2601.09074v1#S3.E7 "In 3 Preliminaries ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")).

###### Theorem 3.

Let p>2p>2 and α,β∈(1,∞)\alpha,\beta\in(1,\infty) with 1α+1β=1\frac{1}{\alpha}+\frac{1}{\beta}=1. If σ\sigma satisfies the ?THM? LABEL:lab:integrabilityforsigma with exponent 𝗁=p​(α∨β)\mathsf{h}=p(\alpha\vee\beta), then

|  |  |  |  |
| --- | --- | --- | --- |
|  | |||Y​(q,N)|||p≤K~p,α,β​B2​β​N−12​β,\displaystyle\left\lvert\!\left\lvert\!\left\lvert Y(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p}\leq\tilde{K}\_{p,\alpha,\beta}B\_{2\beta}N^{-\frac{1}{2\beta}}, |  | (14) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |||Z​(q,N)|||p≤K~p,α,β​B2​β​N−12​β.\displaystyle\left\lvert\!\left\lvert\!\left\lvert Z(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p}\leq\tilde{K}\_{p,\alpha,\beta}B\_{2\beta}N^{-\frac{1}{2\beta}}. |  | (15) |

where B2​βB\_{2\beta} is the constant in ?THM? LABEL:labLemma:DirichletkernelEstimation for r=2​βr=2\beta.
Hence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |||𝖱​(q,N)|||p≤K~p,α,β​B2​β​N−12​β.\left\lvert\!\left\lvert\!\left\lvert\mathsf{R}(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p}\leq\tilde{K}\_{p,\alpha,\beta}B\_{2\beta}N^{-\frac{1}{2\beta}}. |  | (16) |

###### Proof.

Note that 2​π​|||𝖱​(q,N)|||p≤|||Y​(q,N)|||p+|||Z​(q,N)|||p2\pi\left\lvert\!\left\lvert\!\left\lvert\mathsf{R}(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p}\leq\left\lvert\!\left\lvert\!\left\lvert Y(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p}+\left\lvert\!\left\lvert\!\left\lvert Z(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p} so it suffices to prove ([14](https://arxiv.org/html/2601.09074v1#S5.E14 "In Theorem 3. ‣ 5.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) for Y​(q,N)Y(q,N), respectively ([15](https://arxiv.org/html/2601.09074v1#S5.E15 "In Theorem 3. ‣ 5.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) for Z​(q,N)Z(q,N) in order to establish ([16](https://arxiv.org/html/2601.09074v1#S5.E16 "In Theorem 3. ‣ 5.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")). The proof for Z​(q,N)Z(q,N) is similar to that of Y​(q,N)Y(q,N) so we omit it. Even more, we have |||Y​(q,N)|||p≤|||ℜ⁡Y​(q,N)|||p+|||ℑ⁡Y​(q,N)|||p\left\lvert\!\left\lvert\!\left\lvert Y(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p}\leq\left\lvert\!\left\lvert\!\left\lvert\Re Y(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p}+\left\lvert\!\left\lvert\!\left\lvert\Im Y(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p}. The construction of an upper bound for |||ℑ⁡Y​(q,N)|||p\left\lvert\!\left\lvert\!\left\lvert\Im Y(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p} is similar to that of |||ℜ⁡Y​(q,N)|||p\left\lvert\!\left\lvert\!\left\lvert\Re Y(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p} so we also omit it. Thus, we focus on the estimation of |||ℜ⁡Y​(q,N)|||p\left\lvert\!\left\lvert\!\left\lvert\Re Y(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p}.

For p>2p>2

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[(sup−π≤s≤π|ℜ⁡Ys​(q,N)|)p]\displaystyle E\left[\left(\sup\_{-\pi\leq s\leq\pi}|\Re Y\_{s}(q,N)|\right)^{p}\right] | ≤Cp​E​[⟨∫−π⋅ℜ⁡ξz​(q,N,z)​𝑑Hz⟩πp2]\displaystyle\leq C\_{p}E\left[\left\langle\intop\nolimits\_{-\pi}^{\cdot}\Re\xi\_{z}(q,N,z)dH\_{z}\right\rangle^{\frac{p}{2}}\_{\pi}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Cp​E​[(∫−ππ|ℜ⁡ξz​(q,N,z)|2​|σz|2​𝑑z)p2],\displaystyle=C\_{p}E\left[\left(\intop\nolimits\_{-\pi}^{\pi}\left|\Re\xi\_{z}(q,N,z)\right|^{2}|\sigma\_{z}|^{2}dz\right)^{\frac{p}{2}}\right], |  |

where the inequality holds true by the BDG-inequality for a positive constant Cp>0C\_{p}>0. Moreover

|  |  |  |
| --- | --- | --- |
|  | E​[(∫−ππ|σz|2​|ℜ⁡ξz​(q,N,z)|2​𝑑z)p2]\displaystyle E\left[\left(\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{z}|^{2}\left|\Re\xi\_{z}(q,N,z)\right|^{2}dz\right)^{\frac{p}{2}}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤(2​π)p2−1​E​[∫−ππ|σz|p​α​𝑑z]α​E​[∫−ππ|ℜ⁡ξz​(q,N,z)|p​β​𝑑z]β\displaystyle\leq(2\pi)^{\frac{p}{2}-1}\sqrt[\alpha]{E\left[{\intop\nolimits\_{-\pi}^{\pi}\left|\sigma\_{z}\right|^{p\alpha}dz}\right]}\sqrt[\beta]{E\left[{\intop\nolimits\_{-\pi}^{\pi}\left|\Re\xi\_{z}(q,N,z)\right|^{p\beta}dz}\right]} |  |
|  |  |  |
| --- | --- | --- |
|  | =(2​π)p2−1​E​[∫−ππ|σz|p​α​𝑑z]α​∫−ππE​[|ℜ⁡ξz​(q,N,z)|p​β]​𝑑zβ,\displaystyle=(2\pi)^{\frac{p}{2}-1}\sqrt[\alpha]{E\left[{\intop\nolimits\_{-\pi}^{\pi}\left|\sigma\_{z}\right|^{p\alpha}dz}\right]}\sqrt[\beta]{\intop\nolimits\_{-\pi}^{\pi}E\left[\left|\Re\xi\_{z}(q,N,z)\right|^{p{\beta}}\right]dz}, |  |

where the inequality is obtained from Hölder and Jensen inequalities, and the last equality holds true by Tonelli-Fubini’s Theorem.

Note that for t∈[−π,z]t\in[-\pi,z]

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℜ⁡ξt​(q,N,z)\displaystyle\Re\xi\_{t}(q,N,z) | =∫−πt(ℜ⁡e−ı​q​s)​D~N​(z−s)​𝑑Hs=∫−πtcos⁡(q​s)​D~N​(z−s)​𝑑Hs.\displaystyle=\intop\nolimits\_{-\pi}^{t}\left(\Re e^{-\imath q{s}}\right)\tilde{D}\_{N}(z-s)dH\_{s}=\intop\nolimits\_{-\pi}^{t}\cos(qs)\tilde{D}\_{N}(z-s)dH\_{s}. |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[sup−π≤t≤z|ℜ⁡ξt​(q,N,z)|p​β]\displaystyle E\left[\sup\_{-\pi\leq t\leq z}\left|\Re\xi\_{t}(q,N,z)\right|^{p\beta}\right] | ≤Cp​β​B2​βp​β​E​[(∫−ππ|σs|2​α​𝑑s)p​β2​α]​1Np2,\displaystyle\leq C\_{p\beta}B\_{2\beta}^{p\beta}E\left[\left(\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds\right)^{\frac{p\beta}{2\alpha}}\right]\frac{1}{N^{\frac{p}{2}}}, |  |

due to ?THM? LABEL:lablem:auxestiH with κ=p​β\kappa=p\beta.

Wrapping up all together:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[(sup−π≤s≤π|ℜ⁡Ys​(q,N)|)p]\displaystyle E\left[\left(\sup\_{-\pi\leq s\leq\pi}|\Re Y\_{s}(q,N)|\right)^{p}\right] | ≤Cp​(2​π)p2−1​E​[∫−ππ|σz|p​α​𝑑z]α​2​π​Cp​β​B2​βp​β​E​[(∫−ππ|σs|2​α​𝑑s)p​β2​α]​1Np2β\displaystyle\leq C\_{p}(2\pi)^{\frac{p}{2}-1}\sqrt[\alpha]{E\left[\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{z}|^{p\alpha}dz\right]}\sqrt[\beta]{2\pi C\_{p\beta}B\_{2\beta}^{p\beta}E\left[\left(\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds\right)^{\frac{p\beta}{2\alpha}}\right]\frac{1}{N^{\frac{p}{2}}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Cp​(2​π)p2−1​B2​βp​2​π​Cp​ββ​E​[∫−ππ|σz|p​α​𝑑z]α​E​[(∫−ππ|σs|2​α​𝑑s)p​β2​α]β​1Np2​β.\displaystyle=C\_{p}(2\pi)^{\frac{p}{2}-1}B\_{2\beta}^{p}\sqrt[\beta]{2\pi C\_{p\beta}}\sqrt[\alpha]{E\left[\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{z}|^{p\alpha}dz\right]}\sqrt[\beta]{E\left[\left(\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds\right)^{\frac{p\beta}{2\alpha}}\right]}\frac{1}{N^{\frac{p}{2\beta}}}. |  |

Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[(sup−π≤s≤π|ℜ⁡Ys​(q,N)|)p]p\displaystyle\sqrt[p]{E\left[\left(\sup\_{-\pi\leq s\leq\pi}|\Re Y\_{s}(q,N)|\right)^{p}\right]} | ≤12​B2​β​K~p,α,β​1N12​β.\displaystyle\leq\frac{1}{2}B\_{2\beta}\tilde{K}\_{p,\alpha,\beta}\frac{1}{N^{\frac{1}{2\beta}}}. |  |

Adding up the imaginary part we obtain ([14](https://arxiv.org/html/2601.09074v1#S5.E14 "In Theorem 3. ‣ 5.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) for YY. The proof of ([15](https://arxiv.org/html/2601.09074v1#S5.E15 "In Theorem 3. ‣ 5.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) is similar. The inequality ([16](https://arxiv.org/html/2601.09074v1#S5.E16 "In Theorem 3. ‣ 5.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) is consequence of ([14](https://arxiv.org/html/2601.09074v1#S5.E14 "In Theorem 3. ‣ 5.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) and ([15](https://arxiv.org/html/2601.09074v1#S5.E15 "In Theorem 3. ‣ 5.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")), due to ?THM? LABEL:labLemmaUpperbound, since |||⋅|||p\left\lvert\!\left\lvert\!\left\lvert\cdot\right\rvert\!\right\rvert\!\right\rvert\_{p} satisfies the triangle inequality.
∎

###### Remark 3.

A simpler formulation of ?THM? LABEL:labthmest1unbounded is that, for any exponent r∈(0,12)r\in(0,\frac{1}{2}), given sufficient integrability of σ\sigma depending on rr,

|  |  |  |
| --- | --- | --- |
|  | |||𝖱​(q,N)|||p=O​(N−r).\left\lvert\!\left\lvert\!\left\lvert\mathsf{R}(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p}=O\left(N^{-r}\right). |  |

Keeping track of the constant K~p,α,β\tilde{K}\_{p,\alpha,\beta} exhibit explicit dependence on the exponent pp in the constant appearing in the bit O notation O​(⋅)O(\cdot).

### 5.3 Coefficients’ convergence

The notation for the running supremum of a complex valued process was introduced in equation ([6](https://arxiv.org/html/2601.09074v1#S3.E6 "In 3 Preliminaries ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")). For the process 𝖱​(q,N)\mathsf{R}(q,N):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖱π​(q,N)∗\displaystyle\mathsf{R}\_{\pi}(q,N)^{\*} | =sup−π≤s≤π|ℜ⁡𝖱s​(q,N)|+sup−π≤s≤π|ℑ⁡𝖱s​(q,N)|.\displaystyle=\sup\_{-\pi\leq s\leq\pi}|\Re\mathsf{R}\_{s}(q,N)|+\sup\_{-\pi\leq s\leq\pi}|\Im\mathsf{R}\_{s}(q,N)|. |  |

Take the notation and conditions of ?THM? LABEL:labthmest1unbounded. Fix 𝗀∈(0,12​β)\mathsf{g}\in(0,\frac{1}{2\beta}). Given M∈NM\in\mathbb{N}, the ‘good event’ of a Small Error is defined by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​E​(N,M)\displaystyle SE(N,M) | :=⋂|q|≤M{𝖱π​(q,N)∗<6​B2​β​K~p,α,β​N𝗀−12​β}\displaystyle:=\bigcapop\displaylimits\_{|q|\leq M}\left\{\mathsf{R}\_{\pi}(q,N)^{\*}<6B\_{2\beta}{\tilde{K}\_{p,\alpha,\beta}}N^{\mathsf{g}-\frac{1}{2\beta}}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ={sup|q|≤M𝖱π​(q,N)∗<6​B2​β​K~p,α,β​N𝗀−12​β}.\displaystyle=\left\{\sup\_{|q|\leq M}\mathsf{R}\_{\pi}(q,N)^{\*}<6B\_{2\beta}{\tilde{K}\_{p,\alpha,\beta}}N^{\mathsf{g}-\frac{1}{2\beta}}\right\}. |  |

The complement of S​E​(M,N)SE(M,N) in which a Large Error is possible is given by

|  |  |  |
| --- | --- | --- |
|  | L​E​(N,M):=∖S​E​(N,M)=⋃|q|≤M{𝖱π​(q,N)∗≥6​B2​β​K~p,α,β​N𝗀−12​β}.LE(N,M):=\Omega\setminus SE(N,M)=\bigcupop\displaylimits\_{|q|\leq M}\left\{\mathsf{R}\_{\pi}(q,N)^{\*}\geq 6B\_{2\beta}{\tilde{K}\_{p,\alpha,\beta}}N^{\mathsf{g}-\frac{1}{2\beta}}\right\}. |  |

###### Lemma 4.

Take the notation and conditions of ?THM? LABEL:labthmest1unbounded. For 𝗀∈(0,12​β)\mathsf{g}\in(0,\frac{1}{2\beta}) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(S​E​(N,M))\displaystyle P\left(SE(N,M)\right) | ≥1−(2​M+1)​1N𝗀​p.\displaystyle\geq 1-(2M+1)\frac{1}{N^{\mathsf{g}p}}. |  |

###### Proof.

Let μ:=E​[𝖱π​(q,N)∗]\mu:=E\left[\mathsf{R}\_{\pi}(q,N)^{\*}\right]. For pp with p≥2p\geq 2, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[|𝖱π​(q,N)∗−μ|p]p\displaystyle\sqrt[p]{E\left[\left|\mathsf{R}\_{\pi}(q,N)^{\*}-\mu\right|^{p}\right]} | ≤2​|||𝖱​(q,N)|||p\displaystyle\leq 2\left\lvert\!\left\lvert\!\left\lvert\mathsf{R}(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​B2​β​K~p,α,β​N−12​β,\displaystyle\leq 2B\_{2\beta}{\tilde{K}\_{p,\alpha,\beta}}N^{-\frac{1}{2\beta}}, |  |

where the first inequality follows from the triangle inequality, and the second from the estimation in ?THM? LABEL:labthmest1unbounded.

For c>1c>1, the set inclusions

|  |  |  |  |
| --- | --- | --- | --- |
|  | {𝖱π​(q,N)∗≥c​6​B2​β​K~p,α,β​N−12​β}\displaystyle\left\{\mathsf{R}\_{\pi}(q,N)^{\*}\geq c6B\_{2\beta}{\tilde{K}\_{p,\alpha,\beta}}N^{-\frac{1}{2\beta}}\right\} | ⊆{𝖱π​(q,N)∗≥μ+c​E​[|𝖱π​(q,N)∗−μ|p]p}\displaystyle\subseteq\left\{\mathsf{R}\_{\pi}(q,N)^{\*}\geq\mu+c\sqrt[p]{E\left[\left|{\mathsf{R}\_{\pi}(q,N)^{\*}}-\mu\right|^{p}\right]}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⊆{|𝖱π​(q,N)∗−μ|≥c​E​[|𝖱π​(q,N)∗−μ|p]p}\displaystyle\subseteq\left\{|\mathsf{R}\_{\pi}(q,N)^{\*}-\mu|\geq c\sqrt[p]{E\left[\left|\mathsf{R}\_{\pi}(q,N)^{\*}-\mu\right|^{p}\right]}\right\} |  |

yields

|  |  |  |
| --- | --- | --- |
|  | P​({𝖱π​(q,N)∗≥c​6​B2​β​K~p,α,β​N−12​β})≤1cp,P\left(\left\{{\mathsf{R}\_{\pi}(q,N)^{\*}}\geq c6B\_{2\beta}{\tilde{K}\_{p,\alpha,\beta}}N^{-\frac{1}{2\beta}}\right\}\right)\leq\frac{1}{c^{p}}, |  |

due to Chebyshev’s inequality for higher moments; see ?THM? LABEL:labpro:Chebyshev below. In particular, for c=N𝗀c=N^{\mathsf{g}} with 𝗀∈(0,12​β)\mathsf{g}\in(0,\frac{1}{2\beta})

|  |  |  |
| --- | --- | --- |
|  | P​({𝖱π​(q,N)∗≥6​B2​β​K~p,α,β​N𝗀−12​β})≤1N𝗀​p.P\left(\left\{\mathsf{R}\_{\pi}(q,N)^{\*}\geq 6B\_{2\beta}{\tilde{K}\_{p,\alpha,\beta}}N^{\mathsf{g}-\frac{1}{2\beta}}\right\}\right)\leq\frac{1}{N^{\mathsf{g}p}}. |  |

As a consequence, the event L​E​(N,M)LE(N,M) has probability less than (2​M+1)​N−𝗀​p(2M+1)N^{-\mathsf{g}p} and
by taking set complement the result follows.
∎

###### Lemma 5.

Take 𝗀∈(0,12​β)\mathsf{g}\in(0,\frac{1}{2\beta}), p>2p>2 and r>0r>0. If 𝗀​p−r>1\mathsf{g}p-r>1 and the conditions of ?THM? LABEL:labthmest1unbounded hold true, then, for M=O​(Nr)M=O(N^{r})

|  |  |  |
| --- | --- | --- |
|  | P​(L​E​(N,M))=O​(Nr−𝗀​p).P(LE(N,M))=O(N^{r-\mathsf{g}p}). |  |

Moreover, in the complement of a null event

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup|q|≤M𝖱π​(q,N)∗<6​B2​β​K~p,α,β​N𝗀−12​β, eventually.\displaystyle\sup\_{|q|\leq M}\mathsf{R}\_{\pi}(q,N)^{\*}<6B\_{2\beta}{\tilde{K}\_{p,\alpha,\beta}}N^{\mathsf{g}-\frac{1}{2\beta}},\text{ eventually}. |  | (17) |

###### Proof.

The event L​E​(N,M)LE(N,M) has probability less than (2​M+1)​N−𝗀​p(2M+1)N^{-\mathsf{g}p} due to ?THM? LABEL:lablem:probGoodEvent. For M=O​(Nr)M=O(N^{r}) we have P​(L​E​(N,M))=O​(Nr−𝗀​p)P(LE(N,M))=O(N^{r-\mathsf{g}p}). Indeed, for M≤K​NrM\leq KN^{r}

|  |  |  |
| --- | --- | --- |
|  | P​(L​E​(N,M))≤(2​K​Nr+1)​1N𝗀​p≤2​K​1N𝗀​p−r+1N𝗀​p≤2​K+1N𝗀​p−r.\displaystyle P(LE(N,M))\leq(2KN^{r}+1)\frac{1}{N^{\mathsf{g}p}}\leq 2K\frac{1}{N^{\mathsf{g}p-r}}+\frac{1}{N^{\mathsf{g}p}}\leq\frac{2K+1}{N^{\mathsf{g}p-r}}. |  |

As a consequence

|  |  |  |
| --- | --- | --- |
|  | lim supM=O​(Nr),N→∞L​E​(N,M)\limsup\_{M=O(N^{r}),N\to\infty}LE(N,M) |  |

is a null event, due to Borel-Cantelli lemma.
∎

###### Remark 4.

In the second part of ?THM? LABEL:lablem:ucerrorhighprob the qualifier “eventually” means that for ω∈~\omega\in\tilde{\Omega}, where ~\tilde{\Omega} is an event with full measure, there exists I​(ω)∈NI(\omega)\in\mathbb{N} such that for any N≥I​(ω)N\geq I(\omega) the estimation ([17](https://arxiv.org/html/2601.09074v1#S5.E17 "In Lemma 5. ‣ 5.3 Coefficients’ convergence ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) holds true. How large must be I​(ω)I(\omega)?. Selecting a measurable index we can estimate its’ tail behavior as follows. Let K>0K>0 be such that M​(N)≤K​NrM(N)\leq KN^{r}. The event ~\tilde{\Omega} can be taken as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ~\displaystyle\tilde{\Omega} | =⋃j=1∞⋂N=j∞S​E​(N,M​(N)).\displaystyle=\bigcupop\displaylimits\_{j=1}^{\infty}\bigcapop\displaylimits\_{N=j}^{\infty}SE(N,M(N)). |  |

For a concrete index define I​(ω)=inf{j∈N∣ω∈S​E​(n,M​(n))​ for all ​n≥j}I(\omega)=\inf\{j\in\mathbb{N}\mid\omega\in SE(n,M(n))\text{ for all }n\geq j\}. Note that ⋂N=j∞S​E​(N,M​(N))⊂{I≤j}\bigcapop\displaylimits\_{N=j}^{\infty}SE(N,M(N))\subset\{I\leq j\} or equivalently {I>j}⊂⋃N=j∞L​E​(N,M​(N))\{I>j\}\subset\bigcupop\displaylimits\_{N=j}^{\infty}LE(N,M(N)). Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​({I>j})\displaystyle P\left(\{I>j\}\right) | ≤∑N=j∞P​(L​E​(N,M​(N)))\displaystyle\leq\sumop\displaylimits\_{N=j}^{\infty}P\left(LE(N,M(N))\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∑N=j∞2​K+1N𝗀​p−r\displaystyle\leq\sumop\displaylimits\_{N=j}^{\infty}\frac{2K+1}{N^{\mathsf{g}p-r}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​K+1𝗀​p−r−1​(j−1)1−𝗀​p+r.\displaystyle\leq\frac{2K+1}{\mathsf{g}p-r-1}(j-1)^{1-\mathsf{g}p+r}. |  |

As a consequence, P​({I>j})=O​((j−1)1−𝗀​p+r)P\left(\{I>j\}\right)=O((j-1)^{1-\mathsf{g}p+r}).

###### Theorem 6.

Take 𝗀∈(0,12​β)\mathsf{g}\in(0,\frac{1}{2\beta}), p≥2p\geq 2 and r>0r>0. If 𝗀​p−r>1\mathsf{g}p-r>1 and the conditions of ?THM? LABEL:labthmest1unbounded hold true, then, for M=O​(Nr)M=O(N^{r})

|  |  |  |
| --- | --- | --- |
|  | P​({sup|q|≤M|ℱ​[𝗏]​(q)−ℱN​[𝗏]​(q)|≥6​B2​β​K~p,α,β​N𝗀−12​β})=O​(1N𝗀​p−r).P\left(\left\{\sup\_{|q|\leq M}\left|\mathscr{F}[\mathsf{v}](q)-\mathscr{F}\_{N}[\mathsf{v}](q)\right|\geq 6B\_{2\beta}{\tilde{K}\_{p,\alpha,\beta}}N^{\mathsf{g}-\frac{1}{2\beta}}\right\}\right)=O\left(\frac{1}{N^{\mathsf{g}p-r}}\right). |  |

Hence, in the complement of a null event

|  |  |  |
| --- | --- | --- |
|  | sup|q|≤M{|ℱ​[𝗏]​(q)−ℱN​[𝗏]​(q)|}<6​B2​β​K~p,α,β​N𝗀−12​β,eventually.\displaystyle\sup\_{|q|\leq M}\left\{\left|\mathscr{F}[\mathsf{v}](q)-\mathscr{F}\_{N}[\mathsf{v}](q)\right|\right\}<6B\_{2\beta}{\tilde{K}\_{p,\alpha,\beta}}N^{\mathsf{g}-\frac{1}{2\beta}},\quad\text{eventually}. |  |

In particular

|  |  |  |
| --- | --- | --- |
|  | limN→∞ℱN​[𝗏]​(q)=ℱ​[𝗏]​(q),a.s.\lim\_{N\to\infty}\mathscr{F}\_{N}[\mathsf{v}](q)=\mathscr{F}[\mathsf{v}](q),\quad a.s. |  |

###### Proof.

This is a direct consequence of ?THM? LABEL:lablem:ucerrorhighprob since

|  |  |  |
| --- | --- | --- |
|  | |ℱ​[𝗏]​(q)−ℱN​[𝗏]​(q)|≤𝖱π​(q,N)∗.\left|\mathscr{F}[\mathsf{v}](q)-\mathscr{F}\_{N}[\mathsf{v}](q)\right|\leq\mathsf{R}\_{\pi}(q,N)^{\*}. |  |

∎

### 5.4 Uniform convergence of trigonometric polynomials

Let 𝒯M​[𝗏]\mathscr{T}\_{M}[\mathsf{v}] be the trigonometric polynomial of 𝗏\mathsf{v} determined by the system of ‘exact coefficients’ ℱ​[𝗏]\mathscr{F}[\mathsf{v}], that is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯M​[𝗏]​(t):=∑|l|≤M(1−|l|M)​ℱ​[𝗏]​(l)​eı​l​t.\mathscr{T}\_{M}[\mathsf{v}](t):=\sumop\displaylimits\_{|l|\leq M}\left(1-\frac{|l|}{M}\right)\mathscr{F}[\mathsf{v}](l)e^{\imath lt}. |  | (18) |

The next theorem establishes that the trigonometric polynomial 𝒯N,M​[𝗏]\mathscr{T}\_{N,M}[\mathsf{v}] defined in ([10](https://arxiv.org/html/2601.09074v1#S5.E10 "In Definition 1. ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) with coefficients ℱN​[𝗏]\mathscr{F}\_{N}[\mathsf{v}]
constructed with the Bohr convolution is an accurate approximation comparable with the trigonometric approximation ([18](https://arxiv.org/html/2601.09074v1#S5.E18 "In 5.4 Uniform convergence of trigonometric polynomials ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) determined by the ‘exact coefficients’ ℱ​[𝗏]\mathscr{F}[\mathsf{v}] under an appropriate growth regime for MM, the order of the trigonometric polynomials.

###### Theorem 7.

Take 𝗀∈(0,12​β)\mathsf{g}\in(0,\frac{1}{2\beta}), p>2p>2 and r>0r>0. If r<(12​β−𝗀)∧(𝗀​p−1)r<(\frac{1}{2\beta}-\mathsf{g})\wedge(\mathsf{g}p-1) and the conditions of ?THM? LABEL:labthmest1unbounded hold true, then, for M=O​(Nr)M=O(N^{r})

|  |  |  |  |
| --- | --- | --- | --- |
|  | limN,M→∞M=O​(Nr)supt∈[−π,π]|𝒯M​[𝗏]​(t)−𝒯N,M​[𝗏]​(t)|=0,a.s.\lim\_{\begin{subarray}{c}N,M\to\infty\\ M=O(N^{r})\end{subarray}}\sup\_{t\in[-\pi,\pi]}\left|\mathscr{T}\_{M}[\mathsf{v}](t)-\mathscr{T}\_{N,M}[\mathsf{v}](t)\right|=0,a.s. |  | (19) |

###### Proof.

Recall the definition of 𝒯N,M​[𝗏]\mathscr{T}\_{N,M}[\mathsf{v}] in ([10](https://arxiv.org/html/2601.09074v1#S5.E10 "In Definition 1. ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")). Assume that M≤K​NrM\leq KN^{r}. For t∈[−π,π]t\in[-\pi,\pi]

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝒯M​[𝗏]​(t)−𝒯N,M​[𝗏]​(t)|\displaystyle\left|\mathscr{T}\_{M}[\mathsf{v}](t)-\mathscr{T}\_{N,M}[\mathsf{v}](t)\right| | =|∑|l|≤M(1−|l|M)​{ℱ​[𝗏]​(l)−ℱN​[𝗏]​(l)}​eı​l​t|\displaystyle=\left|\sumop\displaylimits\_{|l|\leq M}\left(1-\frac{|l|}{M}\right)\left\{\mathscr{F}[\mathsf{v}](l)-\mathscr{F}\_{N}[\mathsf{v}](l)\right\}e^{\imath lt}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤M​sup|l|≤M|ℱ​[𝗏]​(l)−ℱN​[𝗏]​(l)|\displaystyle\leq M\sup\_{|l|\leq M}\left|\mathscr{F}[\mathsf{v}](l)-\mathscr{F}\_{N}[\mathsf{v}](l)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤M​6​B2​β​K~p,α,β​N𝗀−12​β​ eventually\displaystyle\leq M6B\_{2\beta}{\tilde{K}\_{p,\alpha,\beta}}N^{\mathsf{g}-\frac{1}{2\beta}}\textit{ eventually} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K​6​B2​β​K~p,α,β​Nr+𝗀−12​β,\displaystyle\leq K6B\_{2\beta}{\tilde{K}\_{p,\alpha,\beta}}N^{r+\mathsf{g}-\frac{1}{2\beta}}, |  |

where the second inequality holds true eventually in the complement of a null event due to ?THM? LABEL:labthm:coeffConvergence, since 𝗀​p−r>1\mathsf{g}p-r>1.
Thus, ([19](https://arxiv.org/html/2601.09074v1#S5.E19 "In Theorem 7. ‣ 5.4 Uniform convergence of trigonometric polynomials ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) holds true.
∎

###### Remark 5.

Flexibility in the exponents. In ?THM? LABEL:labthm:PathUC the exponent rr is strictly less than 12\frac{1}{2}. There is a trade-off for this exponent. Selecting rr close to 12\frac{1}{2} allows a better growth rate for MM, the number of harmonics in the trigonometric approximation. However, a larger rr worsens the rate at which the trigonometric polynomial 𝒯N,M​[𝗏]\mathscr{T}\_{N,M}[\mathsf{v}] constructed with coefficients estimated through Bohr convolution approximates the trigonometric polynomial 𝒯M​[𝗏]\mathscr{T}\_{M}[\mathsf{v}] constructed with ‘exact coefficients’. Hence, an optimal choice lies in some intermediate value.

Taking rr to its upper bound requires: β↘1\beta\searrow 1, 𝗀↘0\mathsf{g}\searrow 0 and p↗∞p\nearrow\infty. An exponent β\beta closer to its lower bound requires an exponent α\alpha arbitrarily large. Thus, demanding more integrability on the paths of 𝗏\mathsf{v}. As it was mentioned in ?THM? LABEL:labrem:easydiffusions, diffusions with Lipschitz coefficients and quadratic growth satisfy this requirement; see ?THM? LABEL:labtheasydiffusionscorollaryintegrability.
Thus, in specific models where integrability of σ\sigma with a high exponent is available, more flexibility is gained for a better choice of the exponents.

###### Remark 6.

An important property of the Fourier estimator of volatility is its capability of approximating the whole path {𝗏t​(ω)}−π≤t≤π\{\mathsf{v}\_{t}(\omega)\}\_{-\pi\leq t\leq\pi} in a given scenario ω\omega. In this regard,
?THM? LABEL:labthm:PathUC shows that the trigonometric polynomial 𝒯N,M​[𝗏]\mathscr{T}\_{N,M}[\mathsf{v}] will approximate the volatility 𝗏\mathsf{v} with similar precision as the trigonometric polynomial 𝒯M​[𝗏]\mathscr{T}\_{M}[\mathsf{v}]. This in turn will be the case in our present setting of a volatility with continuous paths. The approximation is uniform in compact intervals included in (−π,π)(-\pi,\pi). A quantitative formulation can be obtained from the modulus of continuity of 𝗏\mathsf{v}; see e.g., [[2](https://arxiv.org/html/2601.09074v1#bib.bib2), Corollary 1.6.5 p.82]. A general class of diffusions provides concrete instances of this uniform approximation; see ?THM? LABEL:labtheasydiffusionscorollarymodulusofcontinuity.

## 6 Discrete observation

Take a family of partitions {νn}n∈N\{\nu^{n}\}\_{n\in\mathbb{N}} of the interval [−π,π][-\pi,\pi] with

|  |  |  |
| --- | --- | --- |
|  | νn={t0n=−π≤t1n≤…≤tmnn=π}.\nu^{n}=\{t\_{0}^{n}=-\pi\leq t\_{1}^{n}\leq\ldots\leq t\_{m\_{n}}^{n}=\pi\}. |  |

Let ρ​(n):=supi=0,…,mn−1{|ti+1n−tin|}\rho(n):=\sup\_{i=0,\ldots,m\_{n}-1}\{|t^{n}\_{i+1}-t^{n}\_{i}|\} be the norm of the partition νn\nu\_{n} and assume that ρ​(n)→0\rho(n)\to 0.

In this section we develop the analogous results to those in Section [5](https://arxiv.org/html/2601.09074v1#S5 "5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process") under a discrete observation of the price process along the system of partitions {νn}n∈N\{\nu^{n}\}\_{n\in\mathbb{N}}. The steps and proofs to follow are quite similar and so, we only give statement of results and the parts of the proofs that need to be modified.

For the partition νn\nu^{n} we define a function that selects for a given time t∈[−π,π]t\in[-\pi,\pi] the closest element from the left of the partition:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒn​(t)\displaystyle\mathscr{L}^{n}(t) | :=sup{z∈νn∣z≤t}.\displaystyle:=\sup\{z\in\nu^{n}\mid z\leq t\}. |  | (20) |

For q∈Zq\in\mathbb{Z} we define the process (q,n)\Gamma(q,n) by

|  |  |  |
| --- | --- | --- |
|  | (q,n)z=[dH]z(q,n):=12​π∫−πze−ı​q​ℒn​(t)dHt,(q,n)−π=0,z∈[−π,π].{}\_{z}(q,n)={}\_{z}[dH](q,n):=\frac{1}{2\pi}\intop\nolimits\_{-\pi}^{z}e^{-\imath q\mathscr{L}^{n}(t)}dH\_{t},\quad{}\_{-\pi}(q,n)=0,\quad z\in[-\pi,\pi]. |  |

###### Definition 2.

Let

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℱn​[d​H]​(q)\displaystyle\mathscr{F}\_{n}[dH](q) | :=(q,n)π,q∈Z.\displaystyle:={}\_{\pi}(q,n),\quad q\in\mathbb{Z}. |  | (21) |

The convolution system of Fourier coefficients {ℱn,N​[𝗏]​(q)}q∈Z\{\mathscr{F}\_{n,N}[\mathsf{v}](q)\}\_{q\in\mathbb{Z}} of the volatility 𝗏\mathsf{v} under discrete observation is defined by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱn,N​[𝗏]​(q):=2​π​{ℱn​[d​H]​Nℱn​[d​H]}​(q).\mathscr{F}\_{n,N}[\mathsf{v}](q):=2\pi\left\{\mathscr{F}\_{n}[dH]\mathop{\circledast}\limits\_{N}\mathscr{F}\_{n}[dH]\right\}(q). |  | (22) |

The Fourier estimator of the spot volatility under discrete observation is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯n,N,M​[𝗏]​(t):=∑|l|≤M(1−|l|M)​ℱn,N​[𝗏]​(l)​eı​l​t.\mathscr{T}\_{n,N,M}[\mathsf{v}](t):=\sumop\displaylimits\_{|l|\leq M}\left(1-\frac{|l|}{M}\right)\mathscr{F}\_{n,N}[\mathsf{v}](l)e^{\imath lt}. |  | (23) |

It is clear that the convolution system of Fourier coefficients is an “approximate system” and it is known from the papers [[8](https://arxiv.org/html/2601.09074v1#bib.bib8)] and [[9](https://arxiv.org/html/2601.09074v1#bib.bib9)] that the error in the approximation is influenced by two procedures: truncating a series and replacing an integral by a sum. First, it is an approximation from the fact that coefficients are constructed from a truncated series in the Bohr convolution, and second, discrete observation of the price process yield approximate estimation of integrals.

The estimator 𝒯n,N,M​[𝗏]\mathscr{T}\_{n,N,M}[\mathsf{v}] is the discretized version of ([10](https://arxiv.org/html/2601.09074v1#S5.E10 "In Definition 1. ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")). The next result is the discretized version of ?THM? LABEL:labth:fundamentalobservation. We omit the proof.

###### Proposition 8.

We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱn​[𝗏]​(q)=ℱn,N​[𝗏]​(q)−𝖱π​(q,n,N),\mathscr{F}\_{n}[\mathsf{v}](q)=\mathscr{F}\_{n,N}[\mathsf{v}](q)-\mathsf{R}\_{\pi}(q,n,N), |  | (24) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖱π(q,n,N):=2​π2​N+1∑|l|≤N{∫−ππ(q−l,n)td(l,n)t+∫−ππ(l,n)td(q−l,n)t}.\mathsf{R}\_{\pi}(q,n,N):=\frac{2\pi}{2N+1}\sumop\displaylimits\_{|l|\leq N}\left\{\intop\nolimits\_{-\pi}^{\pi}{}\_{t}(q-l,n)d{}\_{t}(l,n)+\intop\nolimits\_{-\pi}^{\pi}{}\_{t}(l,n)d{}\_{t}(q-l,n)\right\}. |  | (25) |

### 6.1 Error representation

For t∈[−π,π]t\in[-\pi,\pi], define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξz​(q,n,N,t)\displaystyle\xi\_{z}(q,n,N,t) | :=∫−πze−ı​q​ℒn​(s)​D~N​(ℒn​(t)−ℒn​(s))​𝑑Hs,ξ−π​(q,n,N,t)=0,z∈[−π,t],\displaystyle:=\intop\nolimits\_{-\pi}^{z}e^{-\imath q\mathscr{L}^{n}(s)}\tilde{D}\_{N}(\mathscr{L}^{n}(t)-\mathscr{L}^{n}(s))dH\_{s},\quad\xi\_{-\pi}(q,n,N,t)=0,\quad z\in[-\pi,t], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt​(q,n,N)\displaystyle Y\_{t}(q,n,N) | :=∫−πtξs​(q,n,N,s)​𝑑Hs,Y−π​(q,N)=0,\displaystyle:=\intop\nolimits\_{-\pi}^{t}\xi\_{s}(q,n,N,s)dH\_{s},\quad Y\_{-\pi}(q,N)=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt​(q,n,N)\displaystyle Z\_{t}(q,n,N) | :=∫−πte−ı​q​ℒn​(s)​𝑑Ys​(0,n,N),Z−π​(q,n,N)=0.\displaystyle:=\intop\nolimits\_{-\pi}^{t}e^{-\imath q\mathscr{L}^{n}(s)}dY\_{s}(0,n,N),\quad Z\_{-\pi}(q,n,N)=0. |  |

The next result is the discretized version of ?THM? LABEL:labLemmaUpperbound, we omit the proof.

###### Lemma 9.

We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​π​𝖱π​(q,n,N)\displaystyle 2\pi\mathsf{R}\_{\pi}(q,n,N) | =Yπ​(q,n,N)+Zπ​(q,n,N).\displaystyle=Y\_{\pi}(q,n,N)+Z\_{\pi}(q,n,N). |  |

### 6.2 A key estimation: The remainder’s Lp\mathbb{L}\_{p}-norm

Take p>2p>2 and α,β∈(1,∞)\alpha,\beta\in(1,\infty) with 1α+1β=1\frac{1}{\alpha}+\frac{1}{\beta}=1. Let σ\sigma satisfy the ?THM? LABEL:lab:integrabilityforsigma with exponent 𝗁=p​(α∨β)\mathsf{h}=p(\alpha\vee\beta). Recall the definition of the constant K~p,α,β\tilde{K}\_{p,\alpha,\beta} in ([13](https://arxiv.org/html/2601.09074v1#S5.E13 "In 5.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")). It is given by

|  |  |  |
| --- | --- | --- |
|  | (K~p,α,β)p:=2p​Cp​(2​π)p2−1​2​π​Cp​ββ​E​[∫−ππσsp​α​𝑑s]α​E​[(∫−ππσs2​α​𝑑s)p​β2​α]β.\left(\tilde{K}\_{p,\alpha,\beta}\right)^{p}:=2^{p}C\_{p}(2\pi)^{\frac{p}{2}-1}\sqrt[\beta]{2\pi C\_{p\beta}}\sqrt[\alpha]{E\left[\intop\nolimits\_{-\pi}^{\pi}\sigma^{p\alpha}\_{s}ds\right]}\sqrt[\beta]{E\left[\left(\intop\nolimits\_{-\pi}^{\pi}\sigma^{2\alpha}\_{s}ds\right)^{\frac{p\beta}{2\alpha}}\right]}. |  |

We also define for r>1r>1 the constant

|  |  |  |  |
| --- | --- | --- | --- |
|  | A˙˙˙r:=5+2​πrr−1.\dddot{A}\_{r}:=5+\frac{2\pi^{r}}{r-1}. |  | (26) |

The next result is the discretized version of ?THM? LABEL:labthmest1unbounded.

###### Theorem 10.

Take p>2p>2 and α,β∈(1,∞)\alpha,\beta\in(1,\infty) with 1α+1β=1\frac{1}{\alpha}+\frac{1}{\beta}=1. If σ\sigma satisfies the ?THM? LABEL:lab:integrabilityforsigma with exponent 𝗁=p​(α∨β)\mathsf{h}=p(\alpha\vee\beta), then

|  |  |  |  |
| --- | --- | --- | --- |
|  | |||Y​(q,n,N)|||p≤K~p,α,β​(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)12​β,\displaystyle\left\lvert\!\left\lvert\!\left\lvert Y(q,n,N)\right\rvert\!\right\rvert\!\right\rvert\_{p}\leq\tilde{K}\_{p,\alpha,\beta}\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\frac{1}{2\beta}}, |  | (27) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |||Z​(q,n,N)|||p≤K~p,α,β​(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)12​β.\displaystyle\left\lvert\!\left\lvert\!\left\lvert Z(q,n,N)\right\rvert\!\right\rvert\!\right\rvert\_{p}\leq\tilde{K}\_{p,\alpha,\beta}\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\frac{1}{2\beta}}. |  | (28) |

Hence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |||𝖱​(q,n,N)|||p≤K~p,α,β​(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)12​β.\left\lvert\!\left\lvert\!\left\lvert\mathsf{R}(q,n,N)\right\rvert\!\right\rvert\!\right\rvert\_{p}\leq\tilde{K}\_{p,\alpha,\beta}\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\frac{1}{2\beta}}. |  | (29) |

###### Proof.

Similarly to ?THM? LABEL:labthmest1unbounded, in order to show ([27](https://arxiv.org/html/2601.09074v1#S6.E27 "In Theorem 10. ‣ 6.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 6 Discrete observation ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")), we only present how to obtain an upper bound for ‖sup−π≤s≤π|ℜ⁡Ys​(q,n,N)|‖Lp\left\|\sup\_{-\pi\leq s\leq\pi}|\Re Y\_{s}(q,n,N)|\right\|\_{\mathbb{L}\_{p}}. Moreover, since the proof requires similar arguments we only sketch the main steps.

For p>2p>2 and α,β∈(1,∞)\alpha,\beta\in(1,\infty) with 1α+1β=1\frac{1}{\alpha}+\frac{1}{\beta}=1, in a similar way as in ?THM? LABEL:labthmest1unbounded we get

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | E​[(sup−π≤s≤π|ℜ⁡Ys​(q,n,N)|)p]\displaystyle E\left[\left(\sup\_{-\pi\leq s\leq\pi}|\Re Y\_{s}(q,n,N)|\right)^{p}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | Cp​(2​π)p2−1​E​[∫−ππ|σz|p​α​𝑑z]α​∫−ππE​[|ℜ⁡ξz​(q,n,N,z)|p​β]​𝑑zβ.\displaystyle C\_{p}(2\pi)^{\frac{p}{2}-1}\sqrt[\alpha]{E\left[{\intop\nolimits\_{-\pi}^{\pi}\left|\sigma\_{z}\right|^{p\alpha}dz}\right]}\sqrt[\beta]{\intop\nolimits\_{-\pi}^{\pi}E\left[\left|\Re\xi\_{z}(q,n,N,z)\right|^{p{\beta}}\right]dz}. |  |

For z∈[−π,π]z\in[-\pi,\pi], the expected value E​[sup−π≤t≤z|ℜ⁡ξt​(q,n,N,z)|p​β]E\left[\sup\_{-\pi\leq t\leq z}\left|\Re\xi\_{t}(q,n,N,z)\right|^{p\beta}\right], hence
E​[|ℜ⁡ξz​(q,n,N,z)|p​β]E\left[\left|\Re\xi\_{z}(q,n,N,z)\right|^{p\beta}\right], can be estimated from above as follows:

|  |  |  |
| --- | --- | --- |
|  | E​[sup−π≤t≤z|ℜ⁡ξt​(q,n,N,z)|p​β]\displaystyle E\left[\sup\_{-\pi\leq t\leq z}\left|\Re\xi\_{t}(q,n,N,z)\right|^{p\beta}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Cp​β​E​[(∫−ππ|σs|2​α​𝑑s)p​β2​α]​(∫−πz|D~​(ℒn​(z)−ℒn​(s))|2​β​𝑑s)p​β2​β\displaystyle\leq C\_{p\beta}E\left[\left(\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds\right)^{\frac{p\beta}{2\alpha}}\right]\left(\intop\nolimits\_{-\pi}^{z}|\tilde{D}(\mathscr{L}^{n}(z)-\mathscr{L}^{n}(s))|^{2\beta}ds\right)^{\frac{p\beta}{2\beta}} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Cp​β​E​[(∫−ππ|σs|2​α​𝑑s)p​β2​α]​(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)p​β2​β,\displaystyle\leq C\_{p\beta}E\left[\left(\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds\right)^{\frac{p\beta}{2\alpha}}\right]\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\frac{p\beta}{2\beta}}, |  |

where the first inequality follows from BDG and Hölder’s inequalities, and the fact that D~\tilde{D} is deterministic. The second inequality follows from ?THM? LABEL:labLemma:DirichletkernelEstimationdiscretized. Wrapping up all together we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | E​[sup−π≤s≤π|ℜ⁡Ys​(q,n,N)|p]\displaystyle E\left[\sup\_{-\pi\leq s\leq\pi}\left|\Re Y\_{s}(q,n,N)\right|^{p}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | Cp​(2​π)p2−1​E​[∫−ππ|σz|p​α​𝑑z]α​2​π​Cp​β​E​[(∫−ππ|σs|2​α​𝑑s)p​β2​α]​(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)p2β.\displaystyle C\_{p}(2\pi)^{\frac{p}{2}-1}\sqrt[\alpha]{E\left[\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{z}|^{p\alpha}dz\right]}\sqrt[\beta]{2\pi C\_{p\beta}E\left[\left(\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds\right)^{\frac{p\beta}{2\alpha}}\right]\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\frac{p}{2}}}. |  |

Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[sup−π≤s≤π|ℜ⁡Ys​(q,n,N)|p]p\displaystyle\sqrt[p]{E\left[\sup\_{-\pi\leq s\leq\pi}\left|\Re Y\_{s}(q,n,N)\right|^{p}\right]} | ≤12​K~p,α,β​(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)12​β.\displaystyle\leq\frac{1}{2}\tilde{K}\_{p,\alpha,\beta}\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\frac{1}{2\beta}}. |  |

Adding up the imaginary part we obtain ([27](https://arxiv.org/html/2601.09074v1#S6.E27 "In Theorem 10. ‣ 6.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 6 Discrete observation ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) for Y​(q,n,N)Y(q,n,N). The proof of ([28](https://arxiv.org/html/2601.09074v1#S6.E28 "In Theorem 10. ‣ 6.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 6 Discrete observation ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) is similar. The inequality ([29](https://arxiv.org/html/2601.09074v1#S6.E29 "In Theorem 10. ‣ 6.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 6 Discrete observation ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) is consequence to ([27](https://arxiv.org/html/2601.09074v1#S6.E27 "In Theorem 10. ‣ 6.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 6 Discrete observation ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) and ([28](https://arxiv.org/html/2601.09074v1#S6.E28 "In Theorem 10. ‣ 6.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 6 Discrete observation ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")), due to ?THM? LABEL:labLemmaUpperbounddiscretized.
∎

### 6.3 Coefficients’ convergence

Take the notation and conditions of ?THM? LABEL:labthmest1unboundeddiscretized. Take 𝗀∈(0,12​β)\mathsf{g}\in(0,\frac{1}{2\beta}). We identify the ‘good event’ of a small error:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​E​(n,N,M)\displaystyle SE(n,N,M) | :=⋂|q|≤M{𝖱π​(q,n,N)∗<6​K~p,α,β​(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)12​β−𝗀}\displaystyle:=\bigcapop\displaylimits\_{|q|\leq M}\left\{\mathsf{R}\_{\pi}(q,n,N)^{\*}<6\tilde{K}\_{p,\alpha,\beta}\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\frac{1}{2\beta}-\mathsf{g}}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ={sup|q|≤M𝖱π​(q,n,N)∗<6​K~p,α,β​(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)12​β−𝗀}.\displaystyle=\left\{\sup\_{|q|\leq M}\mathsf{R}\_{\pi}(q,n,N)^{\*}<6\tilde{K}\_{p,\alpha,\beta}\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\frac{1}{2\beta}-\mathsf{g}}\right\}. |  |

The complement of S​E​(n,M,N)SE(n,M,N) is

|  |  |  |
| --- | --- | --- |
|  | L​E​(n,N,M):=∖S​E​(n,N,M)=⋃|q|≤M{𝖱π​(q,n,N)∗≥6​K~p,α,β​(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)12​β−𝗀}.LE(n,N,M):=\Omega\setminus SE(n,N,M)=\bigcupop\displaylimits\_{|q|\leq M}\left\{\mathsf{R}\_{\pi}(q,n,N)^{\*}\geq 6\tilde{K}\_{p,\alpha,\beta}\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\frac{1}{2\beta}-\mathsf{g}}\right\}. |  |

The next result is the discretized version of ?THM? LABEL:lablem:probGoodEvent.

###### Lemma 11.

Take the notation and conditions of ?THM? LABEL:labthmest1unboundeddiscretized. For 𝗀∈(0,12​β)\mathsf{g}\in(0,\frac{1}{2\beta}) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(S​E​(n,N,M))\displaystyle P\left(SE(n,N,M)\right) | ≥1−(2​M+1)​(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)𝗀​p.\displaystyle\geq 1-(2M+1)\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\mathsf{g}p}. |  |

###### Proof.

Take pp with p>2p>2. Denote E​[𝖱π​(q,n,N)∗]E[\mathsf{R}\_{\pi}(q,n,N)^{\*}] with μ\mu. We have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | E​[|𝖱π​(q,n,N)∗−μ|p]p\displaystyle\sqrt[p]{E\left[\left|\mathsf{R}\_{\pi}(q,n,N)^{\*}-\mu\right|^{p}\right]} | ≤2​|||𝖱π​(q,n,N)|||p\displaystyle\leq 2\left\lvert\!\left\lvert\!\left\lvert\mathsf{R}\_{\pi}(q,n,N)\right\rvert\!\right\rvert\!\right\rvert\_{p} | ≤2​K~p,α,β​(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)12​β,\displaystyle\leq 2\tilde{K}\_{p,\alpha,\beta}\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\frac{1}{2\beta}}, |  |

due to the triangle inequality, and ?THM? LABEL:labthmest1unboundeddiscretized.

For c>1c>1

|  |  |  |
| --- | --- | --- |
|  | P​({𝖱π​(q,n,N)≥c​6​K~p,α,β​(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)12​β})≤1cp,P\left(\left\{{\mathsf{R}\_{\pi}(q,n,N)}\geq c6\tilde{K}\_{p,\alpha,\beta}\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\frac{1}{2\beta}}\right\}\right)\leq\frac{1}{c^{p}}, |  |

due to Chebyshev’s inequality for higher moments; see ?THM? LABEL:labpro:Chebyshev below. In particular, for c=(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)−𝗀c=\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{-\mathsf{g}} with 𝗀∈(0,12​β)\mathsf{g}\in(0,\frac{1}{2\beta})

|  |  |  |
| --- | --- | --- |
|  | P​({𝖱π​(q,n,N)∗≥6​K~p,α,β​(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)12​β−𝗀})≤(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)𝗀​p.P\left(\left\{\mathsf{R}\_{\pi}(q,n,N)^{\*}\geq 6\tilde{K}\_{p,\alpha,\beta}\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\frac{1}{2\beta}-\mathsf{g}}\right\}\right)\leq\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\mathsf{g}p}. |  |

As a consequence, the event L​E​(n,N,M)LE(n,N,M) has probability less than (2​M+1)​(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)𝗀​p(2M+1)\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\mathsf{g}p} and by taking set complement the result follows.
∎

The next result is the discretized version of ?THM? LABEL:lablem:ucerrorhighprob. The proof is similar and we omit it.

###### Lemma 12.

Take 𝗀∈(0,12​β)\mathsf{g}\in(0,\frac{1}{2\beta}), p>2p>2 and r>0r>0 with 𝗀​p−r>1\mathsf{g}p-r>1. If the conditions of ?THM? LABEL:labthmest1unboundeddiscretized hold true, then, for M=O​((5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)−r)M=O\left(\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{-r}\right)

|  |  |  |
| --- | --- | --- |
|  | P​(L​E​(n,N,M))=O​((5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)𝗀​p−r).P(LE(n,N,M))=O\left(\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\mathsf{g}p-r}\right). |  |

If along a sequence N=NnN=N\_{n}

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)𝗀​p−r<∞,\sumop\displaylimits\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\mathsf{g}p-r}<\infty, |  | (30) |

then in the complement of a null event

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup|q|≤M𝖱π​(q,n,N)∗<6​K~p,α,β​(5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)12​β−𝗀,eventually.\displaystyle\sup\_{|q|\leq M}\mathsf{R}\_{\pi}(q,n,N)^{\*}<6\tilde{K}\_{p,\alpha,\beta}\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{\frac{1}{2\beta}-\mathsf{g}},\quad\text{eventually}. |  | (31) |

The next result is the discretized version of ?THM? LABEL:labthm:PathUC. The proof is similar and we omit it.

###### Theorem 13.

Take 𝗀∈(0,12​β)\mathsf{g}\in(0,\frac{1}{2\beta}), p>2p>2 and r>0r>0. If r<(12​β−𝗀)∧(𝗀​p−1)r<(\frac{1}{2\beta}-\mathsf{g})\wedge(\mathsf{g}p-1) and the conditions of ?THM? LABEL:lablem:ucerrorhighprobdiscretized hold true, then, for M=O​((5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)−r)M=O\left(\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{-r}\right)

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn,N→∞M=O​((5​ρ​(n)+A˙˙˙2​β​(2​N+1)−1)−r)supt∈[−π,π]|𝒯M​[𝗏]​(t)−𝒯n,N,M​[𝗏]​(t)|=0,a.s.\lim\_{\begin{subarray}{c}n,N\to\infty\\ M=O\left(\left(5\rho(n)+\dddot{A}\_{2\beta}(2N+1)^{-1}\right)^{-r}\right)\end{subarray}}\sup\_{t\in[-\pi,\pi]}\left|\mathscr{T}\_{M}[\mathsf{v}](t)-\mathscr{T}\_{n,N,M}[\mathsf{v}](t)\right|=0,a.s. |  | (32) |

Under the assumption of the growth regime ρ​(n)​N→0\rho(n)N\to 0, the condition 𝗀​p−r>1\mathsf{g}p-r>1 is sufficient for the general condition ([30](https://arxiv.org/html/2601.09074v1#S6.E30 "In Lemma 12. ‣ 6.3 Coefficients’ convergence ‣ 6 Discrete observation ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) in ?THM? LABEL:lablem:ucerrorhighprobdiscretized. Hence, ?THM? LABEL:labthm:PathUCdiscretized has the following corollary.

###### Corollary 14.

Take 𝗀∈(0,12​β)\mathsf{g}\in(0,\frac{1}{2\beta}), p>2p>2 and r>0r>0. Assume r<(12​β−𝗀)∧(𝗀​p−1)r<(\frac{1}{2\beta}-\mathsf{g})\wedge(\mathsf{g}p-1) and ρ​(n)​N→0\rho(n)N\to 0. Then for M=O​(Nr)M=O\left(N^{r}\right)

|  |  |  |  |
| --- | --- | --- | --- |
|  | limN→∞M=O​(Nr)supt∈[−π,π]|𝒯M​[𝗏]​(t)−𝒯n,N,M​[𝗏]​(t)|=0,a.s.\lim\_{\begin{subarray}{c}N\to\infty\\ M=O\left(N^{r}\right)\end{subarray}}\sup\_{t\in[-\pi,\pi]}\left|\mathscr{T}\_{M}[\mathsf{v}](t)-\mathscr{T}\_{n,N,M}[\mathsf{v}](t)\right|=0,a.s. |  | (33) |

## 7 Continuous observation of a cadlag price’s path

Recall that HH represents the logarithmic price process of a discounted stock price and it satisfies the stochastic equation ([1](https://arxiv.org/html/2601.09074v1#S2.E1 "In 2 The price process ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")):

|  |  |  |
| --- | --- | --- |
|  | d​Ht=σt​d​Wt, with ​H−π=x.dH\_{t}=\sigma\_{t}dW\_{t},\text{ with }H\_{-\pi}=x. |  |

In this section instead of HH we consider a process 𝖯\mathsf{P} that also includes jumps:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​𝖯t=d​Ht+d​Jt, with ​𝖯−π=x.d\mathsf{P}\_{t}=dH\_{t}+dJ\_{t},\text{ with }\mathsf{P}\_{-\pi}=x. |  | (34) |

where JJ satisfies the conditions of the next assumption with an exponent qq specified below.

###### Assumption 2.

The stochastic process JJ is a purely discontinuous local martingale. For t∈[−π,π]t\in[-\pi,\pi] and δ∈(0,π)\delta\in(0,\pi) let Mt​(δ)M\_{t}(\delta) be defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mt​(δ):=∑z∈[−π,π]∖{t}0<|t−z|<δJz2.M\_{t}(\delta):=\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi]\setminus\{t\}\\ 0<|t-z|<\delta\end{subarray}}\Delta J\_{z}^{2}. |  | (35) |

For 𝗊>1\mathsf{q}>1 there exists 𝗃>0\mathsf{j}>0, an exponent independent of δ\delta and tt, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[(Mt​(δ))𝗊]=O​(δ𝗊𝗃).E\left[\left(M\_{t}(\delta)\right)^{\mathsf{q}}\right]=O\left(\delta^{\mathsf{q}\mathsf{j}}\right). |  | (36) |

Moreover

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[(∑z∈[−π,π]Jz2)𝗊]<∞.E\left[\left(\sumop\displaylimits\_{z\in[-\pi,\pi]}\Delta J^{2}\_{z}\right)^{\mathsf{q}}\right]<\infty. |  | (37) |

###### Remark 7.

Processes satisfying ?THM? LABEL:labass:localpJumpsummability include processes with jumps of finite activity. In Section [7.5](https://arxiv.org/html/2601.09074v1#S7.SS5 "7.5 Case study: Compensated Poisson process ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process") we give a specific example.

In this section our goal is to extend the theory of Section [5](https://arxiv.org/html/2601.09074v1#S5 "5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process") but instead of the logarithmic price process HH that has continuous paths, we consider the process 𝖯\mathsf{P} that includes jumps. Again, as in Section [6](https://arxiv.org/html/2601.09074v1#S6 "6 Discrete observation ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process"), we follow the same steps of Section [5](https://arxiv.org/html/2601.09074v1#S5 "5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process"). Moreover, we will keep the same notation.

For q∈Zq\in\mathbb{Z} we keep the notation (q)\Gamma(q) for the process defined by

|  |  |  |
| --- | --- | --- |
|  | (q)−π=0,(q)z=[d𝖯]z(q):=12​π∫−πze−ı​q​td𝖯t,z∈[−π,π].{}\_{-\pi}(q)=0,\quad{}\_{z}(q)={}\_{z}[d\mathsf{P}](q):=\frac{1}{2\pi}\intop\nolimits\_{-\pi}^{z}e^{-\imath qt}d\mathsf{P}\_{t},\quad z\in[-\pi,\pi]. |  |

###### Definition 3.

Let

|  |  |  |
| --- | --- | --- |
|  | ℱ[d𝖯](q):=(q)π.\mathscr{F}[d\mathsf{P}](q):={}\_{\pi}(q). |  |

The system of coefficients {ℱN​[𝗏]}N∈N\{\mathscr{F}\_{N}[\mathsf{v}]\}\_{N\in\mathbb{N}} is defined by

|  |  |  |
| --- | --- | --- |
|  | ℱN​[𝗏]​(q):=2​π​{ℱ​[d​𝖯]​Nℱ​[d​𝖯]}​(q),q∈Z.\mathscr{F}\_{N}[\mathsf{v}](q):=2\pi\left\{\mathscr{F}[d\mathsf{P}]\mathop{\circledast}\limits\_{N}\mathscr{F}[d\mathsf{P}]\right\}(q),\quad q\in\mathbb{Z}. |  |

The ?THM? LABEL:labth:fundamentalobservation takes the following form.

###### Proposition 15.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​π​∑−π≤t≤πe−ı​q​t​Jt2+ℱ​[𝗏]​(q)=ℱN​[𝗏]​(q)−𝖱π​(q,N),\frac{1}{2\pi}\sumop\displaylimits\_{-\pi\leq t\leq\pi}e^{-\imath qt}\Delta J^{2}\_{t}+\mathscr{F}[\mathsf{v}](q)=\mathscr{F}\_{N}[\mathsf{v}](q)-\mathsf{R}\_{\pi}(q,N), |  | (38) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖱t(q,N):=2​π2​N+1∑|l|≤N{∫−πt(q−l)z−d(l)z+∫−πt(l)z−d(q−l)z}.\mathsf{R}\_{t}(q,N):=\frac{2\pi}{2N+1}\sumop\displaylimits\_{|l|\leq N}\left\{\intop\nolimits\_{-\pi}^{t}{}\_{z-}(q-l)d{}\_{z}(l)+\intop\nolimits\_{-\pi}^{t}{}\_{z-}(l)d{}\_{z}(q-l)\right\}. |  | (39) |

###### Remark 8.

Similar to how we did in Section [5](https://arxiv.org/html/2601.09074v1#S5 "5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process"), we will prove that 𝖱π​(q,N)\mathsf{R}\_{\pi}(q,N) converges to zero. But now, equation ([38](https://arxiv.org/html/2601.09074v1#S7.E38 "In Proposition 15. ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) shows that ℱN​[𝗏]\mathscr{F}\_{N}[\mathsf{v}] estimates the coefficient ℱ​[𝗏]​(q)\mathscr{F}[\mathsf{v}](q) plus an additional term 12​π​∑−π≤t≤πe−ı​q​t​Jt2\frac{1}{2\pi}\sumop\displaylimits\_{-\pi\leq t\leq\pi}e^{-\imath qt}\Delta J^{2}\_{t}. Hence, we do not recover the Fourier coefficients of the volatility 𝗏=σ2\mathsf{v}=\sigma^{2}. Yet, we will prove that under appropriate conditions, the trigonometric polynomial ([10](https://arxiv.org/html/2601.09074v1#S5.E10 "In Definition 1. ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")), properly rescaled, allows to pathwise recover the process of quadratic jumps J2\Delta J^{2}; see ?THM? LABEL:labthm:PathUCjumps and ?THM? LABEL:labcor:PathUCjumps; see also ?THM? LABEL:labthm:FFjumpfunction in Appendix [B](https://arxiv.org/html/2601.09074v1#A2 "Appendix B Fourier-Fejér inversion of a jump function ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process").

###### Remark 9.

Continuing with the above remark, we outline a possible approach to also obtain an indirect estimation of 𝗏\mathsf{v} from ℱN​[𝗏]\mathscr{F}\_{N}[\mathsf{v}]. Indeed, the trigonometric polynomial 2​πM​𝒯N,M​[𝗏]\frac{2\pi}{M}\mathscr{T}\_{N,M}[\mathsf{v}] approximates J2\Delta J^{2}. Hence, the Fourier coefficients of 2​πM​𝒯N,M​[𝗏]\frac{2\pi}{M}\mathscr{T}\_{N,M}[\mathsf{v}] approximate those of J2\Delta J^{2}, and discounting from ℱN​[𝗏]\mathscr{F}\_{N}[\mathsf{v}] one obtains a candidate to provide an approximation of ℱ​[𝗏]\mathscr{F}[\mathsf{v}]. We study this approach in future work.

### 7.1 Error’s representation

We define for t∈[−π,π]t\in[-\pi,\pi]

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξs​(q,N,t)\displaystyle\xi\_{s}(q,N,t) | :=∫−πse−ı​q​z​D~N​(t−z)​𝑑𝖯z,ξ−π​(q,N,t)=0,s∈[−π,t],\displaystyle:=\intop\nolimits\_{-\pi}^{s}e^{-\imath q{z}}\tilde{D}\_{N}({t}-{z})d\mathsf{P}\_{z},\quad\xi\_{-\pi}(q,N,t)=0,\quad s\in[-\pi,t], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt​(q,N)\displaystyle Y\_{t}(q,N) | :=12​π​∫−πtξs−​(q,N,s)​𝑑𝖯s,Y−π​(q,N)=0,\displaystyle:=\frac{1}{2\pi}\intop\nolimits\_{-\pi}^{t}\xi\_{s-}(q,N,s)d\mathsf{P}\_{s},\quad Y\_{-\pi}(q,N)=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt​(q,N)\displaystyle Z\_{t}(q,N) | :=12​π​∫−πte−ı​q​s​𝑑Ys​(0,N),Z−π​(q,N)=0.\displaystyle:=\frac{1}{2\pi}\intop\nolimits\_{-\pi}^{t}e^{-\imath q{s}}dY\_{s}(0,N),\quad Z\_{-\pi}(q,N)=0. |  |

?THM? LABEL:labLemmaUpperbound keeps its exact form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2​π​𝖱π​(q,N)\displaystyle 2\pi\mathsf{R}\_{\pi}(q,N) | =Yπ​(q,N)+Zπ​(q,N).\displaystyle=Y\_{\pi}(q,N)+Z\_{\pi}(q,N). |  |

### 7.2 A key estimation: The remainder’s Lp\mathbb{L}\_{p}-norm

In this section we fix p>2p>2 , α,β∈(1,∞)\alpha,\beta\in(1,\infty) with α−1+β−1=1\alpha^{-1}+\beta^{-1}=1, and a1,a2,a3>1a\_{1},a\_{2},a\_{3}>1 such that a1−1+a2−1+a3−1=1a\_{1}^{-1}+a\_{2}^{-1}+a\_{3}^{-1}=1. We use the convention that for an adapted process XX, X∞=0X\_{\infty}=0. Hence, if {τn}n∈N\{\tau\_{n}\}\_{n\in\mathbb{N}} is a sequence of stopping times taking values in [−π,π]∪{∞}[-\pi,\pi]\cup\{\infty\} that exhaust the jump times of JJ in [−π,π][-\pi,\pi] then Xτn=Xτn​1{τn<∞}=Xτn​1{τn≤π}X\_{\tau\_{n}}=X\_{\tau\_{n}}1\_{\{\tau\_{n}<\infty\}}=X\_{\tau\_{n}}1\_{\{\tau\_{n}\leq\pi\}}. For a complex valued process X=ℜ⁡X+ı​ℑ⁡XX=\Re X+\imath\Im X recall the norm |||X|||p\left\lvert\!\left\lvert\!\left\lvert X\right\rvert\!\right\rvert\!\right\rvert\_{p} in ([7](https://arxiv.org/html/2601.09074v1#S3.E7 "In 3 Preliminaries ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")).

?THM? LABEL:labthmest1unbounded takes the following form.

###### Theorem 16.

Let σ\sigma satisfy the ?THM? LABEL:lab:integrabilityforsigma with exponent 𝗁=p​(α∨β∨a2)\mathsf{h}=p(\alpha\vee\beta\vee a\_{2}), and let JJ satisfy ?THM? LABEL:labass:localpJumpsummability with exponents 𝗃>0\mathsf{j}>0 and 𝗊=p​(β∨a1∨a2)\mathsf{q}=p(\beta\vee a\_{1}\vee a\_{2}). Furthermore, assume that the jump times {τn}n∈N\{\tau\_{n}\}\_{n\in\mathbb{N}} of JJ are independent of the continuous part HH and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑n∈NE​[Jτn2​a3]a3<∞.\sumop\displaylimits\_{n\in\mathbb{N}}\sqrt[a\_{3}]{E\left[\Delta J\_{\tau\_{n}}^{2a\_{3}}\right]}<\infty. |  | (40) |

Then,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |||𝖱​(q,N)|||p=O​(1N12​(1∧𝗃2))+O​(1N12​β).\left\lvert\!\left\lvert\!\left\lvert\mathsf{R}(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p}=O\left(\frac{1}{N^{\frac{1}{2}(1\wedge\frac{\mathsf{j}}{2})}}\right)+O\left(\frac{1}{N^{\frac{1}{2\beta}}}\right). |  | (41) |

###### Proof.

Similar to ?THM? LABEL:labthmest1unbounded, in order to show ([41](https://arxiv.org/html/2601.09074v1#S7.E41 "In Theorem 16. ‣ 7.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")), we only present how to obtain an upper bound for ‖sup0≤s≤2​π|ℜ⁡Ys​(q,n,N)|‖Lp\left\|\sup\_{0\leq s\leq 2\pi}|\Re Y\_{s}(q,n,N)|\right\|\_{\mathbb{L}\_{p}}.
Thus, we focus on the estimation of |||ℜ⁡Y​(q,N)|||p\left\lvert\!\left\lvert\!\left\lvert\Re Y(q,N)\right\rvert\!\right\rvert\!\right\rvert\_{p}.

For t∈[−π,π]t\in[-\pi,\pi] let

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝖳t1:=\displaystyle\mathsf{T}^{1}\_{t}:= | ∫−πt(∫−πs−cos⁡(q​z)​D~N​(z−s)​𝑑Hz)​𝑑Hs\displaystyle\intop\nolimits\_{-\pi}^{t}\Bigl(\intop\nolimits\_{-\pi}^{s-}\cos(qz)\tilde{D}\_{N}(z-s)\,dH\_{z}\Bigr)dH\_{s} |  | (42) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝖳t2:=\displaystyle\mathsf{T}^{2}\_{t}:= | ∫−πt(∫−πs−cos⁡(q​z)​D~N​(z−s)​𝑑Jz)​𝑑Hs\displaystyle\intop\nolimits\_{-\pi}^{t}\Bigl(\intop\nolimits\_{-\pi}^{s-}\cos(qz)\tilde{D}\_{N}(z-s)\,dJ\_{z}\Bigr)dH\_{s} |  | (43) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝖳t3:=\displaystyle\mathsf{T}^{3}\_{t}:= | ∫−πt(∫−πs−cos⁡(q​z)​D~N​(z−s)​𝑑Hz)​𝑑Js\displaystyle\intop\nolimits\_{-\pi}^{t}\Bigl(\intop\nolimits\_{-\pi}^{s-}\cos(qz)\tilde{D}\_{N}(z-s)\,dH\_{z}\Bigr)dJ\_{s} |  | (44) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝖳t4:=\displaystyle\mathsf{T}^{4}\_{t}:= | ∫−πt(∫−πs−cos⁡(q​z)​D~N​(z−s)​𝑑Jz)​𝑑Js.\displaystyle\intop\nolimits\_{-\pi}^{t}\Bigl(\intop\nolimits\_{-\pi}^{s-}\cos(qz)\tilde{D}\_{N}(z-s)\,dJ\_{z}\Bigr)dJ\_{s}. |  | (45) |

We have

|  |  |  |
| --- | --- | --- |
|  | (ℜ⁡Yt​(q,N))∗=(𝖳1+𝖳2+𝖳3+𝖳4)∗≤(𝖳1)∗+(𝖳2)∗+(𝖳3)∗+(𝖳4)∗,\displaystyle(\Re Y\_{t}(q,N))^{\*}=(\mathsf{T}^{1}+\mathsf{T}^{2}+\mathsf{T}^{3}+\mathsf{T}^{4})^{\*}\leq(\mathsf{T}^{1})^{\*}+(\mathsf{T}^{2})^{\*}+(\mathsf{T}^{3})^{\*}+(\mathsf{T}^{4})^{\*}, |  |

where the supremum processes in the right-hand side are evaluated at t=πt=\pi. Hence

|  |  |  |
| --- | --- | --- |
|  | ‖(ℜ⁡Y​(q,N))t∗‖Lp≤‖(𝖳1)∗‖Lp+‖(𝖳2)∗‖Lp+‖(𝖳3)∗‖Lp+‖(𝖳4)∗‖Lp,\displaystyle\left\|(\Re Y(q,N))^{\*}\_{t}\right\|\_{L^{p}}\leq\left\|(\mathsf{T}^{1})^{\*}\right\|\_{L^{p}}+\left\|(\mathsf{T}^{2})^{\*}\right\|\_{L^{p}}+\left\|(\mathsf{T}^{3})^{\*}\right\|\_{L^{p}}+\left\|(\mathsf{T}^{4})^{\*}\right\|\_{L^{p}}, |  |

We have ‖(𝖳1)∗‖Lp=O​(1N12​β)\left\|(\mathsf{T}^{1})^{\*}\right\|\_{L^{p}}=O\left(\frac{1}{N^{\frac{1}{2\beta}}}\right) due to ?THM? LABEL:labthmest1unbounded, in Section [5](https://arxiv.org/html/2601.09074v1#S5 "5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process"). Moreover, ‖(𝖳2)∗‖Lp=O​(1N12∧𝗃4)\left\|(\mathsf{T}^{2})^{\*}\right\|\_{L^{p}}=O\left(\frac{1}{N^{\frac{1}{2}\wedge\frac{\mathsf{j}}{4}}}\right), due to ?THM? LABEL:labproJumps:estimationT2. The third term 𝖳3\mathsf{T}^{3} satisfies ‖(𝖳3)∗‖Lp=O​(1N12​β)\left\|(\mathsf{T}^{3})^{\*}\right\|\_{L^{p}}=O\left(\frac{1}{N^{\frac{1}{2\beta}}}\right), due to ?THM? LABEL:labproJumps:estimationT3. Finally, The last term 𝖳4\mathsf{T}^{4} satisfies ‖(𝖳4)∗‖Lp=O​(1N12​(1∧𝗃2))\left\|(\mathsf{T}^{4})^{\*}\right\|\_{L^{p}}=O\left(\frac{1}{N^{\frac{1}{2}(1\wedge\frac{\mathsf{j}}{2})}}\right), due to ?THM? LABEL:labproJumps:estimationT4.
∎

In the following proposition we obtain an upper bound for ‖(𝖳2)∗‖Lp\left\|(\mathsf{T}^{2})^{\*}\right\|\_{L^{p}} under the conditions of ?THM? LABEL:labass:localpJumpsummability for the jumps and ?THM? LABEL:lab:integrabilityforsigma for the diffusion coefficient.

###### Proposition 17.

Let 𝖳2\mathsf{T}^{2} be defined by ([43](https://arxiv.org/html/2601.09074v1#S7.E43 "In Proof. ‣ 7.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")). Assume the conditions of ?THM? LABEL:labthmest1unboundedJumps. Then

|  |  |  |
| --- | --- | --- |
|  | ‖(𝖳2)∗‖Lp=O​(1N12∧𝗃4).\left\|(\mathsf{T}^{2})^{\*}\right\|\_{L^{p}}=O\left(\frac{1}{N^{\frac{1}{2}\wedge\frac{\mathsf{j}}{4}}}\right). |  |

###### Proof.

Let Xs:=∫−πscos⁡(q​z)​D~N​(z−s)​𝑑JzX\_{s}:=\intop\nolimits\_{-\pi}^{s}\cos(qz)\tilde{D}\_{N}(z-s)\,dJ\_{z}. We have

|  |  |  |
| --- | --- | --- |
|  | ‖(𝖳2)∗‖Lp≤Cpp​E​[|∫−ππXs−2​d​[H]s|p2]p,\left\|(\mathsf{T}^{2})^{\*}\right\|\_{L^{p}}\leq\sqrt[p]{C\_{p}}\sqrt[p]{E\left[\left|\intop\nolimits\_{-\pi}^{\pi}X^{2}\_{s-}d[H]\_{s}\right|^{\frac{p}{2}}\right]}, |  |

due to BDG-inequality. Moreover

|  |  |  |
| --- | --- | --- |
|  | ∫−ππXs−2​σs2​𝑑s≤∫−ππ|σs|2​α​𝑑sα​∫−ππ|Xs−|2​β​𝑑sβ,\intop\nolimits\_{-\pi}^{\pi}X\_{s-}^{2}\sigma\_{s}^{2}ds\leq\sqrt[\alpha]{\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds}\sqrt[\beta]{\intop\nolimits\_{-\pi}^{\pi}|X\_{s-}|^{2\beta}ds}, |  |

due to Hölder inequality on [−π,π][-\pi,\pi] and then

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[|∫−ππXs−2​σs2​𝑑s|p2]≤\displaystyle E\left[\left|\intop\nolimits\_{-\pi}^{\pi}X\_{s-}^{2}\sigma\_{s}^{2}ds\right|^{\frac{p}{2}}\right]\leq | E​[|∫−ππ|σs|2​α​𝑑s|p2​α​|∫−ππ|Xs−|2​β​𝑑s|p2​β]\displaystyle E\left[\left|\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds\right|^{\frac{p}{2\alpha}}\left|\intop\nolimits\_{-\pi}^{\pi}\left|X\_{s-}\right|^{2\beta}ds\right|^{\frac{p}{2\beta}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | E​[|∫−ππ|σs|2​α​𝑑s|p2]α​E​[|∫−ππ|Xs−|2​β​𝑑s|p2]β\displaystyle\sqrt[\alpha]{E\left[\left|\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds\right|^{\frac{p}{2}}\right]}\sqrt[\beta]{E\left[\left|\intop\nolimits\_{-\pi}^{\pi}\left|X\_{s-}\right|^{2\beta}ds\right|^{\frac{p}{2}}\right]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | E​[|∫−ππ|σs|2​α​𝑑s|p2]α​(2​π)p−22​β​E​[∫−ππ|Xs−|p​β​𝑑s]β\displaystyle\sqrt[\alpha]{E\left[\left|\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds\right|^{\frac{p}{2}}\right]}(2\pi)^{\frac{p-2}{2\beta}}\sqrt[\beta]{E\left[\intop\nolimits\_{-\pi}^{\pi}\left|X\_{s-}\right|^{p\beta}ds\right]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | E​[|∫−ππ|σs|2​α​𝑑s|p2]α​(2​π)p−22​β​∫−ππE​[|Xs−|p​β]​𝑑sβ.\displaystyle\sqrt[\alpha]{E\left[\left|\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds\right|^{\frac{p}{2}}\right]}(2\pi)^{\frac{p-2}{2\beta}}\sqrt[\beta]{\intop\nolimits\_{-\pi}^{\pi}E\left[\left|X\_{s-}\right|^{p\beta}\right]ds}. |  |

Hence, the proof concludes taking κ=p​β\kappa=p\beta in ?THM? LABEL:lablem:auxestiJ.
∎

Now we obtain an upper bound for ‖(𝖳3)∗‖Lp\left\|(\mathsf{T}^{3})^{\*}\right\|\_{L^{p}} with 𝖳3\mathsf{T}^{3} defined in ([44](https://arxiv.org/html/2601.09074v1#S7.E44 "In Proof. ‣ 7.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")).

###### Proposition 18.

Assume the conditions of ?THM? LABEL:labthmest1unboundedJumps. Then

|  |  |  |
| --- | --- | --- |
|  | ‖(𝖳3)∗‖Lp=O​(1N12​β).\left\|(\mathsf{T}^{3})^{\*}\right\|\_{L^{p}}=O\left(\frac{1}{N^{\frac{1}{2\beta}}}\right). |  |

###### Proof.

Let Xs:=∫−πscos⁡(q​z)​D~N​(z−s)​𝑑HzX\_{s}:=\intop\nolimits\_{-\pi}^{s}\cos(qz)\tilde{D}\_{N}(z-s)\,dH\_{z}. We have

|  |  |  |
| --- | --- | --- |
|  | ‖(𝖳3)∗‖Lp≤Cpp​E​[|∫−ππXs−2​d​[J]s|p2]p,\left\|(\mathsf{T}^{3})^{\*}\right\|\_{L^{p}}\leq\sqrt[p]{C\_{p}}\sqrt[p]{E\left[\left|\intop\nolimits\_{-\pi}^{\pi}X^{2}\_{s-}d[J]\_{s}\right|^{\frac{p}{2}}\right]}, |  |

due to BDG-inequality. Moreover

|  |  |  |
| --- | --- | --- |
|  | |∫−ππXs−2​d​[J]s|p2≤[J]πp2−1​∫−ππ|Xs−|p​d​[J]s.\left|\intop\nolimits\_{-\pi}^{\pi}X\_{s-}^{2}\,d[J]\_{s}\right|^{\frac{p}{2}}\leq[J]\_{\pi}^{\,\frac{p}{2}-1}\intop\nolimits\_{-\pi}^{\pi}\left|X\_{s-}\right|^{p}\,d[J]\_{s}. |  |

Let {τn}\{\tau\_{n}\} exhaust the jump times of JJ. Taking expectation, and interchanging summation with expectation:

|  |  |  |
| --- | --- | --- |
|  | E​[|∫−ππXs−2​d​[J]s|p2]≤∑n∈NE​[[J]πp2−1​|Xτn|p​Jτn2].E\left[\left|\intop\nolimits\_{-\pi}^{\pi}X\_{s-}^{2}\,d[J]\_{s}\right|^{\frac{p}{2}}\right]\leq\sumop\displaylimits\_{n\in\mathbb{N}}E\left[[J]\_{\pi}^{\,\frac{p}{2}-1}|X\_{\tau\_{n}}|^{p}\Delta J\_{\tau\_{n}}^{2}\right]. |  |

Now take a1,a2,a3>1a\_{1},a\_{2},a\_{3}>1 such that a1−1+a2−1+a3−1=1a\_{1}^{-1}+a\_{2}^{-1}+a\_{3}^{-1}=1 then

|  |  |  |
| --- | --- | --- |
|  | E​[(∫−ππXs−2​d​[J]s)p2]≤E​[[J]πp−22​a1]a1​∑n∈NE​[|Xτn|p​a2]a2​E​[Jτn2​a3]a3.E\left[\left(\intop\nolimits\_{-\pi}^{\pi}X\_{s-}^{2}\,d[J]\_{s}\right)^{\frac{p}{2}}\right]\leq\sqrt[a\_{1}]{E\left[[J]\_{\pi}^{\frac{p-2}{2}a\_{1}}\right]}\sumop\displaylimits\_{n\in\mathbb{N}}\sqrt[a\_{2}]{E\left[|X\_{\tau\_{n}}|^{pa\_{2}}\right]}\sqrt[a\_{3}]{E\left[\Delta J\_{\tau\_{n}}^{2a\_{3}}\right]}. |  |

As a consequence, there exists a constant K>0K>0 such that

|  |  |  |
| --- | --- | --- |
|  | E​[(∫−ππXs−2​d​[J]s)p2]≤E​[[J]πp−22​a1]a1​KNp2​β​∑n∈NE​[Jτn2​a3]a3.E\left[\left(\intop\nolimits\_{-\pi}^{\pi}X\_{s-}^{2}\,d[J]\_{s}\right)^{\frac{p}{2}}\right]\leq\sqrt[a\_{1}]{E\left[[J]\_{\pi}^{\frac{p-2}{2}a\_{1}}\right]}\frac{K}{N^{\frac{p}{2\beta}}}\sumop\displaylimits\_{n\in\mathbb{N}}\sqrt[a\_{3}]{E\left[\Delta J\_{\tau\_{n}}^{2a\_{3}}\right]}. |  |

due to ?THM? LABEL:lablem:auxestiH and ?THM? LABEL:lablemmaindependentbound with exponent κ=p​a2\kappa=pa\_{2}.
∎

In the following proposition we obtain an upper bound for ‖(𝖳4)∗‖Lp\left\|(\mathsf{T}^{4})^{\*}\right\|\_{L^{p}} with 𝖳4\mathsf{T}^{4} defined in ([45](https://arxiv.org/html/2601.09074v1#S7.E45 "In Proof. ‣ 7.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")).

###### Proposition 19.

Assume the conditions of ?THM? LABEL:labthmest1unboundedJumps. Then

|  |  |  |
| --- | --- | --- |
|  | ‖(𝖳4)∗‖Lp=O​(1N12​(1∧𝗃2)).\left\|(\mathsf{T}^{4})^{\*}\right\|\_{L^{p}}=O\left(\frac{1}{N^{\frac{1}{2}(1\wedge\frac{\mathsf{j}}{2})}}\right). |  |

###### Proof.

Let Xs:=∫−πscos⁡(q​z)​D~N​(z−s)​𝑑JzX\_{s}:=\intop\nolimits\_{-\pi}^{s}\cos(qz)\tilde{D}\_{N}(z-s)\,dJ\_{z}. To start, we apply Jensen’s inequality:

|  |  |  |
| --- | --- | --- |
|  | (∫−ππXs−2​d​[J]s)p2≤[J]πp2−1​∫−ππXs−p​d​[J]s=[J]πp2−1​∑−π<s≤π|Xs−|p​Js2.\left(\intop\nolimits\_{-\pi}^{\pi}X\_{s-}^{2}\,d[J]\_{s}\right)^{\frac{p}{2}}\leq[J]\_{\pi}^{\,\frac{p}{2}-1}\intop\nolimits\_{-\pi}^{\pi}X\_{s-}^{p}\,d[J]\_{s}=[J]\_{\pi}^{\,\frac{p}{2}-1}\sumop\displaylimits\_{-\pi<s\leq\pi}|X\_{s-}|^{p}\Delta J\_{s}^{2}. |  |

Let {τn}\{\tau\_{n}\} exhaust the jump times of JJ. Taking expectation, and interchanging summation with expectation:

|  |  |  |
| --- | --- | --- |
|  | E​[|∫−ππXs−2​d​[J]s|p2]≤∑n∈NE​[[J]πp2−1​|Xτn−|p​Jτn2].E\left[\left|\intop\nolimits\_{-\pi}^{\pi}X\_{s-}^{2}\,d[J]\_{s}\right|^{\frac{p}{2}}\right]\leq\sumop\displaylimits\_{n\in\mathbb{N}}E\left[[J]\_{\pi}^{\,\frac{p}{2}-1}|X\_{\tau\_{n}-}|^{p}\Delta J\_{\tau\_{n}}^{2}\right]. |  |

Now take a1,a2,a3>1a\_{1},a\_{2},a\_{3}>1 such that a1−1+a2−1+a3−1=1a\_{1}^{-1}+a\_{2}^{-1}+a\_{3}^{-1}=1 then

|  |  |  |
| --- | --- | --- |
|  | E​[(∫−ππXs−2​d​[J]s)p2]≤E​[[J]πp−22​a1]a1​∑n∈NE​[|Xτn−|p​a2]a2​E​[Jτn2​a3]a3.E\left[\left(\intop\nolimits\_{-\pi}^{\pi}X\_{s-}^{2}\,d[J]\_{s}\right)^{\frac{p}{2}}\right]\leq\sqrt[a\_{1}]{E\left[[J]\_{\pi}^{\frac{p-2}{2}a\_{1}}\right]}\sumop\displaylimits\_{n\in\mathbb{N}}\sqrt[a\_{2}]{E\left[|X\_{\tau\_{n}-}|^{pa\_{2}}\right]}\sqrt[a\_{3}]{E\left[\Delta J\_{\tau\_{n}}^{2a\_{3}}\right]}. |  |

As a consequence, there exists a constant K>0K>0 such that

|  |  |  |
| --- | --- | --- |
|  | E​[(∫−ππXs−2​d​[J]s)p2]≤E​[[J]πp−22​a1]a1​KNp2​(1∧𝗃2)​∑n∈NE​[Jτn2​a3]a3.E\left[\left(\intop\nolimits\_{-\pi}^{\pi}X\_{s-}^{2}\,d[J]\_{s}\right)^{\frac{p}{2}}\right]\leq\sqrt[a\_{1}]{E\left[[J]\_{\pi}^{\frac{p-2}{2}a\_{1}}\right]}\frac{K}{N^{\frac{p}{2}(1\wedge\frac{\mathsf{j}}{2})}}\sumop\displaylimits\_{n\in\mathbb{N}}\sqrt[a\_{3}]{E\left[\Delta J\_{\tau\_{n}}^{2a\_{3}}\right]}. |  |

due to ?THM? LABEL:lablem:auxestiJ and ?THM? LABEL:lablemmaindependentbound with κ=p​a2\kappa=pa\_{2}.
∎

### 7.3 Coefficients’ convergence

Similarly as it was obtained in Section [5.3](https://arxiv.org/html/2601.09074v1#S5.SS3 "5.3 Coefficients’ convergence ‣ 5 Continuous observation of the price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process"), once we have the estimation in ?THM? LABEL:labthmest1unboundedJumps we deduce the convergence of coefficients. We state the theorem and omit the proof since the details are similar.

?THM? LABEL:labthm:coeffConvergence takes the following form.

###### Theorem 20.

Let l:=12​(𝗃2∨1β)l:=\frac{1}{2}\left(\frac{\mathsf{j}}{2}\vee\frac{1}{\beta}\right).
Take 𝗀∈(0,l)\mathsf{g}\in(0,l), p>2p>2 and r>0r>0. If 𝗀​p−r>1\mathsf{g}p-r>1 and the conditions of ?THM? LABEL:labthmest1unboundedJumps hold true, then for a constant K~>0\tilde{K}>0 and for M=O​(Nr)M=O(N^{r})

|  |  |  |
| --- | --- | --- |
|  | P​({sup|q|≤M|ℱ​[𝗏]​(q)+12​π​∑−π≤t≤πe−ı​q​t​Jt2−ℱN​[𝗏]​(q)|≥6​K~​N𝗀−l})=O​(1N𝗀​p−r).P\left(\left\{\sup\_{|q|\leq M}\left|\mathscr{F}[\mathsf{v}](q)+\frac{1}{2\pi}\sumop\displaylimits\_{-\pi\leq t\leq\pi}e^{-\imath qt}\Delta J^{2}\_{t}-\mathscr{F}\_{N}[\mathsf{v}](q)\right|\geq 6{\tilde{K}}N^{\mathsf{g}-l}\right\}\right)=O\left(\frac{1}{N^{\mathsf{g}p-r}}\right). |  |

Hence, in the complement of a null event

|  |  |  |
| --- | --- | --- |
|  | sup|q|≤M{|ℱ​[𝗏]​(q)+12​π​∑−π≤t≤πe−ı​q​t​Jt2−ℱN​[𝗏]​(q)|}<6​K~​N𝗀−l,eventually.\displaystyle\sup\_{|q|\leq M}\left\{\left|\mathscr{F}[\mathsf{v}](q)+\frac{1}{2\pi}\sumop\displaylimits\_{-\pi\leq t\leq\pi}e^{-\imath qt}\Delta J^{2}\_{t}-\mathscr{F}\_{N}[\mathsf{v}](q)\right|\right\}<6{\tilde{K}}N^{\mathsf{g}-l},\quad\text{eventually}. |  |

In particular

|  |  |  |
| --- | --- | --- |
|  | limN→∞ℱN​[𝗏]​(q)=ℱ​[𝗏]​(q)+12​π​∑−π≤t≤πe−ı​q​t​Jt2,a.s.\lim\_{N\to\infty}\mathscr{F}\_{N}[\mathsf{v}](q)=\mathscr{F}[\mathsf{v}](q)+\frac{1}{2\pi}\sumop\displaylimits\_{-\pi\leq t\leq\pi}e^{-\imath qt}\Delta J^{2}\_{t},\quad a.s. |  |

### 7.4 Uniform convergence of trigonometric polynomials

Let 𝒯M​[J2]\mathscr{T}\_{M}[\Delta J^{2}] be the trigonometric polynomial determined by the system of ‘exact coefficients’ of the quadratic jump process J2\Delta J^{2} , that is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒯M​[J2]​(t)\displaystyle\mathscr{T}\_{M}[\Delta J^{2}](t) | =∑|l|≤M(1−|l|M)​ℱ˙˙˙​[J2]​(l)​eı​l​t\displaystyle=\sumop\displaylimits\_{|l|\leq M}\left(1-\frac{|l|}{M}\right)\dddot{\mathscr{F}}[\Delta J^{2}](l)e^{\imath lt} |  | (46) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℱ˙˙˙​[J2]​(l)\displaystyle\dddot{\mathscr{F}}[\Delta J^{2}](l) | =12​π​∑z∈[−π,π]e−ı​l​z​Jz2.\displaystyle=\frac{1}{2\pi}\sumop\displaylimits\_{z\in[-\pi,\pi]}e^{-\imath lz}\Delta J\_{z}^{2}. |  | (47) |

Let moreover, 𝒯N,M\mathscr{T}\_{N,M} be the trigonometric polynomial constructed with the coefficients ℱ\mathscr{F} in ?THM? LABEL:labdef:FourierJumps.

The next theorem is the analogous result to ?THM? LABEL:labthm:PathUC. It establishes that, under an appropriate growth rate for MM, the trigonometric polynomial 1M​𝒯N,M\frac{1}{M}\mathscr{T}\_{N,M} is uniformly getting close to the trigonometric polynomial 1M​𝒯M​[J2]\frac{1}{M}\mathscr{T}\_{M}[\Delta J^{2}].

###### Theorem 21.

Let l:=12​(𝗃2∨1β)l:=\frac{1}{2}\left(\frac{\mathsf{j}}{2}\vee\frac{1}{\beta}\right).
Take 𝗀∈(0,l)\mathsf{g}\in(0,l), p>2p>2 and r>0r>0. If r<(l−𝗀)∧(𝗀​p−1)r<(l-\mathsf{g})\wedge(\mathsf{g}p-1) and the conditions of ?THM? LABEL:labthmest1unboundedJumps hold true, then, for M=O​(Nr)M=O(N^{r})

|  |  |  |  |
| --- | --- | --- | --- |
|  | limN,M→∞M=O​(Nr)supt∈[−π,π]1M​|𝒯M​[J2]​(t)−𝒯N,M​(t)|=0,a.s.\lim\_{\begin{subarray}{c}N,M\to\infty\\ M=O(N^{r})\end{subarray}}\sup\_{t\in[-\pi,\pi]}\frac{1}{M}\left|\mathscr{T}\_{M}[\Delta J^{2}](t)-\mathscr{T}\_{N,M}(t)\right|=0,a.s. |  | (48) |

###### Proof.

Assume that M≤K​NrM\leq KN^{r}. For t∈[−π,π]t\in[-\pi,\pi]

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝒯M​[J2]​(t)−𝒯N,M​(t)|\displaystyle\left|\mathscr{T}\_{M}[\Delta J^{2}](t)-\mathscr{T}\_{N,M}(t)\right| | =|∑|q|≤M(1−|q|M)​{ℱ˙˙˙​[J2]​(q)−ℱN​(q)}​eı​q​t|\displaystyle=\left|\sumop\displaylimits\_{|q|\leq M}\left(1-\frac{|q|}{M}\right)\left\{\dddot{\mathscr{F}}[\Delta J^{2}](q)-\mathscr{F}\_{N}(q)\right\}e^{\imath qt}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤|∑|q|≤M(1−|q|M)​{ℱ˙˙˙​[J2]​(q)+ℱ​[𝗏]​(q)−ℱN​(q)}​eı​q​t|\displaystyle\leq\left|\sumop\displaylimits\_{|q|\leq M}\left(1-\frac{|q|}{M}\right)\left\{\dddot{\mathscr{F}}[\Delta J^{2}](q)+\mathscr{F}[\mathsf{v}](q)-\mathscr{F}\_{N}(q)\right\}e^{\imath qt}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +|∑|q|≤M(1−|q|M)​ℱ​[𝗏]​(q)​eı​q​t|\displaystyle+\left|\sumop\displaylimits\_{|q|\leq M}\left(1-\frac{|q|}{M}\right)\mathscr{F}[\mathsf{v}](q)e^{\imath qt}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤M​sup|q|≤M|ℱ˙˙˙​[J2]​(q)+ℱ​[𝗏]​(q)−ℱN​[𝗏]​(q)|+B,\displaystyle\leq M\sup\_{|q|\leq M}\left|\dddot{\mathscr{F}}[\Delta J^{2}](q)+\mathscr{F}[\mathsf{v}](q)-\mathscr{F}\_{N}[\mathsf{v}](q)\right|+B, |  |

where BB is positive random variable that do not depend on time and B<∞B<\infty a.s. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1M​|𝒯M​[J2]​(t)−𝒯N,M​(t)|\displaystyle\frac{1}{M}\left|\mathscr{T}\_{M}[\Delta J^{2}](t)-\mathscr{T}\_{N,M}(t)\right| | ≤sup|q|≤M|ℱ˙˙˙​[J2]​(q)+ℱ​[𝗏]​(q)−ℱN​[𝗏]​(q)|+BM\displaystyle\leq\sup\_{|q|\leq M}\left|\dddot{\mathscr{F}}[\Delta J^{2}](q)+\mathscr{F}[\mathsf{v}](q)-\mathscr{F}\_{N}[\mathsf{v}](q)\right|+\frac{B}{M} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤6​K~​N𝗀−l+BM, eventually,\displaystyle\leq 6{\tilde{K}}N^{\mathsf{g}-l}+\frac{B}{M},\textit{ eventually}, |  |

where the second inequality holds true eventually in the complement of a null event due to ?THM? LABEL:labthm:coeffConvergencejumps.
∎

###### Corollary 22.

Under the conditions of ?THM? LABEL:labthm:PathUCjumps, for almost all ω\omega, the trigonometric polynomial 2​πM​𝒯N,M\frac{2\pi}{M}\mathscr{T}\_{N,M} converges pointwise to J2\Delta J^{2}.

###### Proof.

This is a consequence of ?THM? LABEL:labthm:PathUCjumps above, and of ?THM? LABEL:labthm:FFjumpfunction in Appendix [B](https://arxiv.org/html/2601.09074v1#A2 "Appendix B Fourier-Fejér inversion of a jump function ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process").
∎

### 7.5 Case study: Compensated Poisson process

Let 𝖭\mathsf{N} be a Poisson process with intensity λ~>0\tilde{\lambda}>0 constructed in the following form.
Let T1,T2,…T\_{1},T\_{2},\ldots be a sequence of independent, exponentially distributed random variables with parameter λ~>0\tilde{\lambda}>0. Let τ0=0\tau\_{0}=0 and τn:=T1+…+Tn\tau\_{n}:=T\_{1}+\ldots+T\_{n}. Define the Poisson process 𝖭\mathsf{N} by 𝖭t:=max⁡{n≥0∣τn≤t}\mathsf{N}\_{t}:=\max\{n\geq 0\mid\tau\_{n}\leq t\}. Let {Yn}n∈N\{Y\_{n}\}\_{n\in\mathbb{N}} be an i.i.d. sequence of random variables with ‖Y1‖∞=1\left\|Y\_{1}\right\|\_{\infty}=1. Let λ=λ~​E​[Y1]\lambda=\tilde{\lambda}E[Y\_{1}], and JJ be the purely discontinuous local martingale defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jt=∑n=1∞Yn​1[τn,∞)​(t)−λ​t.J\_{t}=\sumop\displaylimits\_{n=1}^{\infty}Y\_{n}1\_{[\tau\_{n},\infty)}(t)-\lambda t. |  | (49) |

Now we translate the definition of JJ so that it is indexed on the interval [−π,π][-\pi,\pi].

We verify that {Jt}−π≤t≤π\{J\_{t}\}\_{-\pi\leq t\leq\pi} satisfies the conditions of ?THM? LABEL:labass:localpJumpsummability and of ?THM? LABEL:labthmest1unboundedJumps. We start with ([36](https://arxiv.org/html/2601.09074v1#S7.E36 "In Assumption 2. ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) in ?THM? LABEL:labass:localpJumpsummability.

###### Proposition 23.

The process JJ defined in ([49](https://arxiv.org/html/2601.09074v1#S7.E49 "In 7.5 Case study: Compensated Poisson process ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) satisfies ([36](https://arxiv.org/html/2601.09074v1#S7.E36 "In Assumption 2. ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")). More precisely, for 𝗊∈N∖{1}\mathsf{q}\in\mathbb{N}\setminus\{1\}, and 0<δ<10<\delta<1,

|  |  |  |
| --- | --- | --- |
|  | E​[(Mt​(δ))𝗊]=O​(δ).E\left[\left(M\_{t}(\delta)\right)^{\mathsf{q}}\right]=O\left(\delta\right). |  |

###### Proof.

For δ∈(0,1)\delta\in(0,1) let ZZ be a random variable with distribution P​o​i​s​s​o​n​(2​λ~​δ)Poisson(2\tilde{\lambda}\delta). Then for any p∈Np\in\mathbb{N}, p>1p>1 we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[(Mt​(δ))p]=E​[(∑z∈[−π,π]∖{t}0<|t−z|<δJz2)p]≤E​[(∑z∈[−π,π]∖{t}0<|t−z|<δ𝖭z2)p]=\displaystyle E[(M\_{t}(\delta))^{p}]=E\left[\left(\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi]\setminus\{t\}\\ 0<|t-z|<\delta\end{subarray}}\Delta J\_{z}^{2}\right)^{p}\right]\leq E\left[\left(\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi]\setminus\{t\}\\ 0<|t-z|<\delta\end{subarray}}\Delta\mathsf{N}\_{z}^{2}\right)^{p}\right]= | E​[Zp].\displaystyle E[Z^{p}]. |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | E​[(Mt​(δ))p]≤∑k=1p{pk}​(2​λ~​δ)k≤δ​∑k=1p{pk}​(2​λ~)k,E[(M\_{t}(\delta))^{p}]\leq\sumop\displaylimits\_{k=1}^{p}\left\{\begin{matrix}p\\ k\end{matrix}\right\}(2\tilde{\lambda}\delta)^{k}\leq\delta\sumop\displaylimits\_{k=1}^{p}\left\{\begin{matrix}p\\ k\end{matrix}\right\}(2\tilde{\lambda})^{k}, |  |

where the coefficients in the sums are the Stirling numbers of the second kind.
∎

We continue with ([40](https://arxiv.org/html/2601.09074v1#S7.E40 "In Theorem 16. ‣ 7.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) in ?THM? LABEL:labthmest1unboundedJumps. From this property, condition ([37](https://arxiv.org/html/2601.09074v1#S7.E37 "In Assumption 2. ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) in ?THM? LABEL:labass:localpJumpsummability will follow.

###### Proposition 24.

For any κ>1\kappa>1

|  |  |  |
| --- | --- | --- |
|  | ∑n∈NE​[|Jτn​1{τn≤π}|2​κ]κ<∞.\sumop\displaylimits\_{n\in\mathbb{N}}\sqrt[\kappa]{E\left[|\Delta J\_{\tau\_{n}}1\_{\{\tau\_{n}\leq\pi\}}|^{2\kappa}\right]}<\infty. |  |

###### Proof.

For any 𝗀>1∨κ\mathsf{g}>1\vee\kappa we have P​(𝖭π≥n)=O​(n−𝗀)P(\mathsf{N}\_{\pi}\geq n)=O(n^{-\mathsf{g}}). Hence, there is a constant K𝗀>0K\_{\mathsf{g}}>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[|Jτn|2​κ​1{τn≤π}]κ\displaystyle\sqrt[\kappa]{E\left[|\Delta J\_{\tau\_{n}}|^{2\kappa}1\_{\{\tau\_{n}\leq\pi\}}\right]} | ≤P​({τn≤π})κ\displaystyle\leq\sqrt[\kappa]{P({\{\tau\_{n}\leq\pi\}})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K𝗀​n−𝗀κ.\displaystyle\leq K\_{\mathsf{g}}n^{-\frac{\mathsf{g}}{\kappa}}. |  |

Now the result follows from a simple comparison.
∎

### 7.6 Numerical illustrations: Poisson process

In this section we present a numerical exercise illustrating the approximation result in ?THM? LABEL:labcor:PathUCjumps. To this end, we simulate a logarithmic price process 𝖯\mathsf{P} and estimate the rescaled trigonometric polynomial 2​πM​𝒯N,M\frac{2\pi}{M}\mathscr{T}\_{N,M}. This numerical exercise will clearly illustrate the pointwise convergence to J2\Delta J^{2}. For concreteness we take the process

|  |  |  |
| --- | --- | --- |
|  | 𝖯t=∫−πtσ​(sin⁡(s)+2)​𝑑Ws+𝖭t−λ​t,λ=2,σ=1,\mathsf{P}\_{t}=\intop\nolimits\_{-\pi}^{t}\sigma(\sin(s)+2)dW\_{s}+\mathsf{N}\_{t}-\lambda t,\quad\lambda=2,\sigma=1, |  |

where 𝖭\mathsf{N} is a Poisson process with intensity λ\lambda.

Simulations of the diffusion process Ht=∫−πtσ​(sin⁡(s)+2)​𝑑WsH\_{t}=\intop\nolimits\_{-\pi}^{t}\sigma(\sin(s)+2)dW\_{s} and an independent compensated Poisson process Jt=𝖭t−λ​tJ\_{t}=\mathsf{N}\_{t}-\lambda t are illustrated in Figure [1(a)](https://arxiv.org/html/2601.09074v1#S7.F1.sf1 "In Figure 1 ‣ 7.6 Numerical illustrations: Poisson process ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process"). The partition is a regular grid with 10510^{5} points. In Figure [1(a)](https://arxiv.org/html/2601.09074v1#S7.F1.sf1 "In Figure 1 ‣ 7.6 Numerical illustrations: Poisson process ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process"), the red line corresponds to the purely discontinuous martingale JJ. A compensated Poisson process with parameter λ=2\lambda=2. In blue line, we see the continuous martingale part given by HH.

In Figure [1(b)](https://arxiv.org/html/2601.09074v1#S7.F1.sf2 "In Figure 1 ‣ 7.6 Numerical illustrations: Poisson process ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process") we see the resulting path of the logarithmic price process. The dashed green lines correspond to the jump times of the Poisson process.

In Figures [2(a)](https://arxiv.org/html/2601.09074v1#S7.F2.sf1 "In Figure 2 ‣ 7.6 Numerical illustrations: Poisson process ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process") to [3(b)](https://arxiv.org/html/2601.09074v1#S7.F3.sf2 "In Figure 3 ‣ 7.6 Numerical illustrations: Poisson process ‣ 7 Continuous observation of a cadlag price’s path ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process"), we see in blue line the rescaled trigonometric polynomial 2​πM​𝒯N,M\frac{2\pi}{M}\mathscr{T}\_{N,M},
the Fourier estimator of spot volatility, with degrees 10, 50, 100 and 700, respectively. Note that these figures visually illustrate, what we have proved about the pointwise convergence of the polynomials to the jump process J2\Delta J^{2}, which in this case coincides with 𝖭\Delta\mathsf{N}.

![Refer to caption](11Components.png)


(a) Simulated components of the logarithmic price process 𝖯\mathsf{P}.

![Refer to caption](11SimulatedPrice.png)


(b) Simulated logarithmic price process 𝖯\mathsf{P}.

Figure 1: Simulation of the logarithmic price process.



![Refer to caption](volatility_logprice10.png)


(a) The Fourier estimator of spot volatility with 10 degrees.

![Refer to caption](volatility_logprice50.png)


(b) The Fourier estimator of spot volatility with 50 degrees.

Figure 2: The rescaled trigonometric polynomial 2​πM​𝒯N,M\frac{2\pi}{M}\mathscr{T}\_{N,M}, degrees 10 and 50, respectively.



![Refer to caption](volatility_logprice100.png)


(a) The Fourier estimator of spot volatility with 100 degrees.

![Refer to caption](volatility_logprice700.png)


(b) The Fourier estimator of spot volatility with 700 degrees.

Figure 3: The rescaled trigonometric polynomial 2​πM​𝒯N,M\frac{2\pi}{M}\mathscr{T}\_{N,M}, degrees 100 and 700, respectively.

## Appendix A Few elementary facts on Fourier coefficients

### A.1 The Dirichlet kernel

Recall that the Dirichlet kernel was introduced in ([3](https://arxiv.org/html/2601.09074v1#S3.E3 "In 3 Preliminaries ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")). It is given by DN​(t):=∑|l|≤Nexp⁡(ı​l​t)D\_{N}(t):=\sumop\displaylimits\_{|l|\leq N}\exp(\imath lt). It is well known that

|  |  |  |
| --- | --- | --- |
|  | DN​(t)=sin⁡(N​t+t/2)sin⁡(t/2).D\_{N}(t)=\frac{\sin(Nt+t/2)}{\sin(t/2)}. |  |

Recall the rescaled Dirichlet kernel in equation ([4](https://arxiv.org/html/2601.09074v1#S3.E4 "In 3 Preliminaries ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")). It is given by D~N​(t):=12​N+1​DN​(t)\tilde{D}\_{N}(t):=\frac{1}{2N+1}D\_{N}(t).
In the proof of ?THM? LABEL:labthmest1unbounded we applied Lemma LABEL:labLemma:DirichletkernelEstimation below. The statement is just Exercise 3.1.6 of [[5](https://arxiv.org/html/2601.09074v1#bib.bib5)].

###### Lemma 25.

Take r>1r>1. For the Dirichlet kernel DND\_{N} there exists positive constants brb\_{r} and BrB\_{r} such that for every N∈NN\in\mathbb{N}, the following inequality holds true:

|  |  |  |
| --- | --- | --- |
|  | brr​(2​N+1)r−1≤∫−ππ|DN​(s)|r​𝑑s≤Brr​(2​N+1)r−1.b^{r}\_{r}(2N+1)^{r-1}\leq\intop\nolimits\_{-\pi}^{\pi}\left|D\_{N}(s)\right|^{r}ds\leq B^{r}\_{r}(2N+1)^{r-1}. |  |

### A.2 The Fejér kernel

Recall that the Fejér kernel is defined by

|  |  |  |
| --- | --- | --- |
|  | 𝐅N​(t):=1N​∑j=0N−1DN​(t).{\mathbf{F}}\_{N}(t):=\frac{1}{N}\sumop\displaylimits\_{j=0}^{N-1}D\_{N}(t). |  |

It satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝐅N​(t)=1N​(sin⁡(N​t/2)sin⁡(t/2))2.{\mathbf{F}}\_{N}(t)=\frac{1}{N}\left(\frac{\sin(Nt/2)}{\sin(t/2)}\right)^{2}. |  |

From this expression one easily obtains that for δ>0\delta>0 the following useful inequality holds true

|  |  |  |
| --- | --- | --- |
|  | supz∈[−π,π],|z|≥δ𝐅N​(z)≤π2δ2​N.\sup\_{\begin{subarray}{c}z\in[-\pi,\pi],\\ |z|\geq\delta\end{subarray}}{\mathbf{F}}\_{N}(z)\leq\frac{\pi^{2}}{\delta^{2}N}. |  |

We will use this inequality in the proof of ?THM? LABEL:labthm:FFjumpfunction below.

### A.3 The Dirichlet kernel in discrete time

In this section we give a discretized version of ?THM? LABEL:labLemma:DirichletkernelEstimation. For completeness we give full details in the proof. For r>1r>1 recall the constant
A˙˙˙r:=5+2​πrr−1\dddot{A}\_{r}:=5+\frac{2\pi^{r}}{r-1} defined in ([26](https://arxiv.org/html/2601.09074v1#S6.E26 "In 6.2 A key estimation: The remainder’s 𝐿_𝑝-norm ‣ 6 Discrete observation ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")).

###### Lemma 26.

Take a partition ν={−π=s0<s1<…<sl=π}\nu=\{-\pi=s\_{0}<s\_{1}<\ldots<s\_{l}=\pi\} of the interval [−π,π][-\pi,\pi] and let ρ\rho be its norm: ρ=maxi=0,…,l−1⁡|si+1−si|\rho=\max\_{i=0,\ldots,l-1}{|s\_{i+1}-s\_{i}|}. Define ℒ​(t):=max⁡{z∈ν∣z≤t}\mathscr{L}(t):=\max\{z\in\nu\mid z\leq t\}. Take r>1r>1. For t∈[−π,π]t\in[-\pi,\pi] we have the upper bound

|  |  |  |
| --- | --- | --- |
|  | ∫−πt|DN​(ℒ​(t)−ℒ​(s))|r​𝑑s≤5​(ρ+(2​N+1)−1)​(2​N+1)r+2​πrr−1​(2​N+1)r−1.\intop\nolimits\_{-\pi}^{t}\left|D\_{N}(\mathscr{L}(t)-\mathscr{L}(s))\right|^{r}ds\leq 5(\rho+(2N+1)^{-1})(2N+1)^{r}+2\frac{\pi^{r}}{r-1}(2N+1)^{r-1}. |  |

In particular

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫−πt|D~N​(ℒ​(t)−ℒ​(s))|r​𝑑s\displaystyle\intop\nolimits\_{-\pi}^{t}\left|\tilde{D}\_{N}(\mathscr{L}(t)-\mathscr{L}(s))\right|^{r}ds | ≤5​(ρ+(2​N+1)−1)+2​πrr−1​(2​N+1)−1\displaystyle\leq 5(\rho+(2N+1)^{-1})+2\frac{\pi^{r}}{r-1}(2N+1)^{-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =5​ρ+(2​N+1)−1​(2​πrr−1+5)\displaystyle=5\rho+(2N+1)^{-1}\left(\frac{2\pi^{r}}{r-1}+5\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤5​ρ+(2​N+1)−1​A˙˙˙r.\displaystyle\leq 5\rho+(2N+1)^{-1}\dddot{A}\_{r}. |  |

###### Proof.

For s∈[−π,π]s\in[-\pi,\pi] we define ℛ​(s):=inf{x∈ν∣x≥s}\mathscr{R}(s):=\inf\{x\in\nu\mid x\geq s\} with the convention inf∅=−∞\inf\emptyset=-\infty. The Dirichlet kernel admits on [−π,π][-\pi,\pi] the upper bound |DN​(⋅)|≤(2​N+1)∧f​(⋅)|D\_{N}(\cdot)|\leq(2N+1)\wedge f(\cdot), where

|  |  |  |
| --- | --- | --- |
|  | f​(s):={π|s|0<|s|≤π∞s=0.f(s):=\begin{cases}\frac{\pi}{|s|}&\quad 0<|s|\leq\pi\\ \infty&\quad s=0.\end{cases} |  |

Take t∈[−π,π]t\in[-\pi,\pi] and denote t0:=ℒ​(t)t\_{0}:=\mathscr{L}(t), δ:=(2​N+1)−1\delta:=(2N+1)^{-1}. We only do the proof for the case t0>0t\_{0}>0 since the case t0≤0t\_{0}\leq 0 is easier.

1. 1.

   Let t1:=ℒ​(t0−π−δ)t\_{1}:=\mathscr{L}(t\_{0}-\pi-\delta). Only the case t1≥−πt\_{1}\geq-\pi is non trivial in this part. We estimate the integral I1:=∫−πt1|DN​(ℒ​(t)−ℒ​(s))|r​𝑑sI\_{1}:=\intop\nolimits\_{-\pi}^{t\_{1}}\left|D\_{N}(\mathscr{L}(t)-\mathscr{L}(s))\right|^{r}ds. For s∈[−π,t1]s\in[-\pi,t\_{1}] we have π+δ≤t0−ℒ​(s)\pi+\delta\leq t\_{0}-\mathscr{L}(s). Hence 0≤2​π−(t0−ℒ​(s))≤π−δ0\leq 2\pi-(t\_{0}-\mathscr{L}(s))\leq\pi-\delta and

   |  |  |  |
   | --- | --- | --- |
   |  | |DN​(t0−ℒ​(s))|=|DN​(2​π−t0+ℒ​(s))|≤(2​N+1)∧π|2​π−t0+ℒ​(s)|.\left|D\_{N}(t\_{0}-\mathscr{L}(s))\right|=\left|D\_{N}(2\pi-t\_{0}+\mathscr{L}(s))\right|\leq(2N+1)\wedge\frac{\pi}{\left|2\pi-t\_{0}+\mathscr{L}(s)\right|}. |  |

   Thus, the integral I1I\_{1} is bounded from above by ∫−πt1(2​N+1)r∧πr|2​π−t0+ℒ​(s)|r​d​s\intop\nolimits\_{-\pi}^{t\_{1}}(2N+1)^{r}\wedge\frac{\pi^{r}}{\left|2\pi-t\_{0}+\mathscr{L}(s)\right|^{r}}ds and this last integral can be estimated as follows.

   Let tm∈νt\_{m}\in\nu be such that tm=ℛ​(δ−π+ρ)t\_{m}=\mathscr{R}(\delta-\pi+\rho). Consider the case tm≤t1t\_{m}\leq t\_{1}, otherwise the next estimations simplify. We have

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∫−πt1(2​N+1)r∧πr(2​π−t0+ℒ​(s))r​d​s\displaystyle\intop\nolimits\_{-\pi}^{t\_{1}}(2N+1)^{r}\wedge\frac{\pi^{r}}{(2\pi-t\_{0}+\mathscr{L}(s))^{r}}ds | ≤(tm+π)​(2​N+1)r+∫tmt1πr(2​π−t0+s−ρ)r​𝑑s\displaystyle\leq(t\_{m}+\pi)(2N+1)^{r}+\intop\nolimits\_{t\_{m}}^{t\_{1}}\frac{\pi^{r}}{(2\pi-t\_{0}+{s}-\rho)^{r}}ds |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ≤(δ+ρ)​(2​N+1)r+∫tmt1πr(2​π−t0+s−ρ)r​𝑑s,\displaystyle\leq(\delta+\rho)(2N+1)^{r}+\intop\nolimits\_{t\_{m}}^{t\_{1}}\frac{\pi^{r}}{(2\pi-t\_{0}+{s}-\rho)^{r}}ds, |  |

   where in the first inequality we used the fact that for s∈[tm,t1]s\in[t\_{m},t\_{1}]

   |  |  |  |
   | --- | --- | --- |
   |  | 2​π−t0+ℒ​(s)≥2​π−t0+s−ρ≥2​π−t0+tm−ρ≥δ.2\pi-t\_{0}+\mathscr{L}(s)\geq 2\pi-t\_{0}+{s}-\rho\geq 2\pi-t\_{0}+t\_{m}-\rho\geq\delta. |  |

   Moreover

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∫tmt1πr(2​π−t0+s−ρ)r​𝑑s\displaystyle\intop\nolimits\_{t\_{m}}^{t\_{1}}\frac{\pi^{r}}{(2\pi-t\_{0}+{s}-\rho)^{r}}ds | =πr1−r​[(2​π−t0+s−ρ)1−r]tmt1\displaystyle=\frac{\pi^{r}}{1-r}\left[(2\pi-t\_{0}+{s}-\rho)^{1-r}\right]\_{t\_{m}}^{t\_{1}} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ≤πrr−1​(2​π−t0+tm−ρ)1−r\displaystyle\leq\frac{\pi^{r}}{r-1}(2\pi-t\_{0}+t\_{m}-\rho)^{1-r} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ≤πrr−1​δ1−r.\displaystyle\leq\frac{\pi^{r}}{r-1}\delta^{1-r}. |  |

   Thus,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | I1\displaystyle I\_{1} | ≤(δ+ρ)​(2​N+1)r+πrr−1​δ1−r.\displaystyle\leq(\delta+\rho)(2N+1)^{r}+\frac{\pi^{r}}{r-1}\delta^{1-r}. |  |
2. 2.

   Let t2:=ℛ​(t0−π+δ)t\_{2}:=\mathscr{R}(t\_{0}-\pi+\delta). We estimate the integral I2:=∫t2t|DN​(t0−ℒ​(s))|r​𝑑sI\_{2}:=\intop\nolimits\_{t\_{2}}^{t}\left|D\_{N}(t\_{0}-\mathscr{L}(s))\right|^{r}ds. For s∈[t2,t]s\in[t\_{2},t] note that ℒ​(s)≥t2\mathscr{L}(s)\geq t\_{2} and then we have 0≤t0−ℒ​(s)≤π−δ0\leq t\_{0}-\mathscr{L}(s)\leq\pi-\delta. Let tk∈νt\_{k}\in\nu be such that tk=ℛ​(t0−δ)t\_{k}=\mathscr{R}(t\_{0}-\delta). Note that for s≤tk−1s\leq t\_{k-1}

   |  |  |  |
   | --- | --- | --- |
   |  | δ<t0−tk−1≤t0−s≤t0−ℒ​(s).\delta<t\_{0}-t\_{k-1}\leq t\_{0}-s\leq t\_{0}-\mathscr{L}(s). |  |

   Only the case tk−1≥t2t\_{k-1}\geq t\_{2} is interesting for the next estimations. We have

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | I2\displaystyle I\_{2} | ≤∫t2t(2​N+1)r∧πr(t0−ℒ​(s))r​d​s\displaystyle\leq\intop\nolimits\_{t\_{2}}^{t}(2N+1)^{r}\wedge\frac{\pi^{r}}{(t\_{0}-\mathscr{L}(s))^{r}}ds |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ≤∫t2tk−1πr(t0−ℒ​(s))r​𝑑s+∫tk−1t(2​N+1)r​𝑑s\displaystyle\leq\intop\nolimits\_{t\_{2}}^{t\_{k-1}}\frac{\pi^{r}}{(t\_{0}-\mathscr{L}(s))^{r}}ds+\intop\nolimits\_{t\_{k-1}}^{t}(2N+1)^{r}ds |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ≤∫t2tk−1πr(t0−s)r​𝑑s+(t−tk−1)​(2​N+1)r\displaystyle\leq\intop\nolimits\_{t\_{2}}^{t\_{k-1}}\frac{\pi^{r}}{(t\_{0}-{s})^{r}}ds+(t-t\_{k-1})(2N+1)^{r} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =πrr−1​[(t0−s)1−r]t2tk−1+(t−tk−1)​(2​N+1)r\displaystyle=\frac{\pi^{r}}{r-1}\left[(t\_{0}-{s})^{1-r}\right]\_{t\_{2}}^{t\_{k-1}}+(t-t\_{k-1})(2N+1)^{r} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ≤πrr−1​(t0−tk−1)1−r+(2​ρ+δ)​(2​N+1)r\displaystyle\leq\frac{\pi^{r}}{r-1}(t\_{0}-t\_{k-1})^{1-r}+(2\rho+\delta)(2N+1)^{r} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ≤πrr−1​δ1−r+2​(ρ+δ)​(2​N+1)r.\displaystyle\leq\frac{\pi^{r}}{r-1}\delta^{1-r}+2(\rho+\delta)(2N+1)^{r}. |  |
3. 3.

   Now we estimate the integral I3=∫t1t2|DN​(t0−ℒ​(s))|r​𝑑sI\_{3}=\intop\nolimits\_{t\_{1}}^{t\_{2}}\left|D\_{N}(t\_{0}-\mathscr{L}(s))\right|^{r}ds in the case t2>t1t\_{2}>t\_{1}. We have

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | t2−t1\displaystyle t\_{2}-t\_{1} | =t2−(t0−π+δ)+t0−π+δ−ℒ​(t0−π−δ)\displaystyle=t\_{2}-(t\_{0}-\pi+\delta)+t\_{0}-\pi+\delta-\mathscr{L}(t\_{0}-\pi-\delta) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ≤ρ+t0−π−δ−ℒ​(t0−π−δ)+2​δ\displaystyle\leq\rho+t\_{0}-\pi-\delta-\mathscr{L}(t\_{0}-\pi-\delta)+2\delta |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ≤2​ρ+2​δ.\displaystyle\leq 2\rho+2\delta. |  |

   Now

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∫t1t2|DN​(ℒ​(t)−ℒ​(s))|r​𝑑s\displaystyle\intop\nolimits\_{t\_{1}}^{t\_{2}}\left|D\_{N}(\mathscr{L}(t)-\mathscr{L}(s))\right|^{r}ds | ≤2​(δ+ρ)​(2​N+1)r.\displaystyle\leq 2(\delta+\rho)(2N+1)^{r}. |  |
4. 4.

   As a consequence

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∫−πt|DN​(ℒ​(t)−ℒ​(s))|r​𝑑s\displaystyle\intop\nolimits\_{-\pi}^{t}\left|D\_{N}(\mathscr{L}(t)-\mathscr{L}(s))\right|^{r}ds | ≤I1+I2+I3≤5​(2​N+1)r​(δ+ρ)+2​πrr−1​δ1−r.\displaystyle\leq I\_{1}+I\_{2}+I\_{3}\leq 5(2N+1)^{r}(\delta+\rho)+2\frac{\pi^{r}}{r-1}\delta^{1-r}. |  |

∎

## Appendix B Fourier-Fejér inversion of a jump function

Let :[−π,π]→R\mho:[-\pi,\pi]\to\mathbb{R} be a cadlag function with jump function :[−π,π]→R\Delta\mho:[-\pi,\pi]\to\mathbb{R} defined as usual by :=t−tt−\Delta{}\_{t}:={}\_{t}-{}\_{t-}. Assume that the sum of quadratic jumps is finite: []:=∑z∈[−π,π]<z2∞[\mho]:=\sumop\displaylimits\_{z\in[-\pi,\pi]}\Delta{}\_{z}^{2}<\infty.
In this section we develop a “Fourier-Fejér inversion theory” for . To this end, we start with the analogous definitions in this context. Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱ˙˙˙[]2(q)\displaystyle\dddot{\mathscr{F}}[\Delta{}^{2}](q) | :=12​π∑z∈[−π,π]e−ı​q​zz2\displaystyle:=\frac{1}{2\pi}\sumop\displaylimits\_{z\in[-\pi,\pi]}e^{-\imath qz}\Delta{}\_{z}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | SN[]2(t)\displaystyle S\_{N}[\Delta{}^{2}](t) | :=∑|q|≤Nℱ˙˙˙[]2(q)eı​q​t,and,\displaystyle:=\sumop\displaylimits\_{|q|\leq N}\dddot{\mathscr{F}}[\Delta{}^{2}](q)e^{\imath qt},and, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯N[]2\displaystyle\mathscr{T}\_{N}[\Delta{}^{2}] | :=1N∑j=0N−1Sj[]2.\displaystyle:=\frac{1}{N}\sumop\displaylimits\_{j=0}^{N-1}S\_{j}[\Delta{}^{2}]. |  |

For a function ff the “convolution” with the Fejér kernel is

|  |  |  |
| --- | --- | --- |
|  | f⋆𝐅N​(t):=12​π​∑z∈[−π,π]f​(z)​𝐅N​(t−z).f\star{\mathbf{F}}\_{N}(t):=\frac{1}{2\pi}\sumop\displaylimits\_{z\in[-\pi,\pi]}f(z){\mathbf{F}}\_{N}(t-z). |  |

Through this convolution, the trigonometric polynomial 𝒯N[]2\mathscr{T}\_{N}[\Delta{}^{2}] can be expressed as

|  |  |  |
| --- | --- | --- |
|  | 𝒯N[]2(t)=⋆2𝐅N(t).\mathscr{T}\_{N}[\Delta{}^{2}](t)=\Delta{}^{2}\star{\mathbf{F}}\_{N}(t). |  |

Now that we have the preliminary notation ready we establish the main result of this section.

###### Theorem 27.

Define for δ∈(0,π)\delta\in(0,\pi) and t∈[−π,π]t\in[-\pi,\pi]

|  |  |  |
| --- | --- | --- |
|  | Mt(δ):=∑z∈[−π,π]∖{t}0<|z−t|<δ.z2M\_{t}(\delta):=\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi]\setminus\{t\}\\ 0<|z-t|<\delta\end{subarray}}\Delta{}\_{z}^{2}. |  |

Take t∈[−π,π]t\in[-\pi,\pi] and assume that

|  |  |  |
| --- | --- | --- |
|  | limδ→0Mt​(δ)=0.\lim\_{\delta\to 0}M\_{t}(\delta)=0. |  |

Then,

|  |  |  |
| --- | --- | --- |
|  | limN→∞|2​πN𝒯N[]2(t)−|t2=0.\displaystyle\lim\_{N\to\infty}\left|\frac{2\pi}{N}\mathscr{T}\_{N}[\Delta{}^{2}](t)-\Delta{}^{2}\_{t}\right|=0. |  |

Moreover, for O⊂[−π,π]O\subset[-\pi,\pi] an open set with

|  |  |  |
| --- | --- | --- |
|  | limδ→0supt∈OMt​(δ)=0,\lim\_{\delta\to 0}\sup\_{t\in O}M\_{t}(\delta)=0, |  |

we have the uniform convergence

|  |  |  |  |
| --- | --- | --- | --- |
|  | limN→∞supt∈O|2​πN𝒯N[]2(t)−|t2\displaystyle\lim\_{N\to\infty}\sup\_{t\in O}\left|\frac{2\pi}{N}\mathscr{T}\_{N}[\Delta{}^{2}](t)-\Delta{}^{2}\_{t}\right| | =0.\displaystyle=0. |  |

###### Proof.

Take t∈[−π,π]t\in[-\pi,\pi]. We only do the proof in the case where there is a jump at time tt: >t20\Delta{}^{2}\_{t}>0, the case =t20\Delta{}^{2}\_{t}=0 is simpler. Note that

|  |  |  |
| --- | --- | --- |
|  | 2π𝒯N[]2(t)=𝐅Nt2(0)+∑z∈[−π,π]∖{t}0<|z−t|<δ𝐅Nz2(t−z)+∑z∈[−π,π]∖{t}|z−t|≥δ𝐅Nz2(t−z).2\pi\mathscr{T}\_{N}[\Delta{}^{2}](t)=\Delta{}^{2}\_{t}{\mathbf{F}}\_{N}(0)+\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi]\setminus\{t\}\\ 0<|z-t|<\delta\end{subarray}}\Delta{}^{2}\_{z}{\mathbf{F}}\_{N}(t-z)+\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi]\setminus\{t\}\\ |z-t|\geq\delta\end{subarray}}\Delta{}^{2}\_{z}{\mathbf{F}}\_{N}(t-z). |  |

We have

|  |  |  |
| --- | --- | --- |
|  | ∑z∈[−π,π]∖{t}0<|z−t|<δ𝐅Nz2​(t−z)≤N​Mt​(δ).\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi]\setminus\{t\}\\ 0<|z-t|<\delta\end{subarray}}\Delta{}^{2}\_{z}{\mathbf{F}}\_{N}(t-z)\leq NM\_{t}(\delta). |  |

Recall that for δ>0\delta>0 we have supz∈[−π,π]∖{t},|z−t|≥δ𝐅N​(t−z)≤π2δ2​N\sup\_{z\in[-\pi,\pi]\setminus\{t\},|z-t|\geq\delta}{\mathbf{F}}\_{N}(t-z)\leq\frac{\pi^{2}}{\delta^{2}N}. Hence

|  |  |  |
| --- | --- | --- |
|  | ∑z∈[−π,π]∖{t},|z−t|≥δ𝐅Nz2​(t−z)≤[]​supz∈[−π,π]∖{t},|z−t|≥δ𝐅N​(t−z)≤[]​π2δ2​N.\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi]\setminus\{t\},\\ |z-t|\geq\delta\end{subarray}}\Delta{}^{2}\_{z}{\mathbf{F}}\_{N}(t-z)\leq[\mho]\sup\_{\begin{subarray}{c}z\in[-\pi,\pi]\setminus\{t\},\\ |z-t|\geq\delta\end{subarray}}{\mathbf{F}}\_{N}(t-z)\leq[\mho]\frac{\pi^{2}}{\delta^{2}N}. |  |

As a consequence we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |2​πN𝒯N[]2(t)−|t2\displaystyle\left|\frac{2\pi}{N}\mathscr{T}\_{N}[\Delta{}^{2}](t)-\Delta{}^{2}\_{t}\right| | ≤Mt​(δ)+[]​π2δ2​N2.\displaystyle\leq M\_{t}(\delta)+[\mho]\frac{\pi^{2}}{\delta^{2}N^{2}}. |  |

In particular taking δ=N−12\delta=N^{-\frac{1}{2}} we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | |2​πN𝒯N[]2(t)−|t2\displaystyle\left|\frac{2\pi}{N}\mathscr{T}\_{N}[\Delta{}^{2}](t)-\Delta{}^{2}\_{t}\right| | ≤Mt​(N−12)+[]​π2N.\displaystyle\leq M\_{t}(N^{-\frac{1}{2}})+[\mho]\frac{\pi^{2}}{N}. |  |

This shows the pointwise convergence. For the uniform convergence we simply take supremum over t∈Ot\in O on both sides of the inequality and conclude with the assumption on supt∈OMt\sup\_{t\in O}M\_{t}.
∎

## Appendix C Auxiliary estimations

###### Lemma 28.

Take κ>2\kappa>2 and α,β∈(1,∞)\alpha,\beta\in(1,\infty) with 1α+1β=1\frac{1}{\alpha}+\frac{1}{\beta}=1. Let σ\sigma satisfy ?THM? LABEL:lab:integrabilityforsigma with exponent 𝗁=κ∨2​α\mathsf{h}=\kappa\vee 2\alpha. Take z∈[−π,π]z\in[-\pi,\pi]. Let Xt​(z):=∫−πtcos⁡(q​s)​D~N​(z−s)​𝑑HsX\_{t}(z):=\intop\nolimits\_{-\pi}^{t}\cos(qs)\tilde{D}\_{N}(z-s)\,dH\_{s}, for t∈[−π,z]t\in[-\pi,z], We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[|Xt​(z)|κ]≤Cκ​B2​βκ​E​[(∫−ππ|σs|2​α​𝑑s)κ2​α]​1Nκ2​β, for −π≤t≤z.E\left[\left|X\_{t}(z)\right|^{\kappa}\right]\leq C\_{\kappa}B\_{2\beta}^{\kappa}E\left[\left(\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds\right)^{\frac{\kappa}{2\alpha}}\right]\frac{1}{N^{\frac{\kappa}{2\beta}}},\text{ for }-\pi\leq t\leq z. |  | (50) |

###### Proof.

We have

|  |  |  |
| --- | --- | --- |
|  | E​[sup−π≤t≤z|Xt​(z)|κ]≤Cκ​E​[⟨X​(z)⟩zκ2],\displaystyle E\left[\sup\_{-\pi\leq t\leq z}\left|X\_{t}(z)\right|^{\kappa}\right]\leq C\_{\kappa}E\left[\left\langle X(z)\right\rangle\_{z}^{\frac{\kappa}{2}}\right], |  |

due to BDG-Inequality. Moreover

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[⟨X​(z)⟩tκ2]≤\displaystyle E\left[\left\langle X(z)\right\rangle\_{t}^{\frac{\kappa}{2}}\right]\leq | E​[(∫−πz|σs|2​α​𝑑sα​∫−πz|D~N​(z−s)|2​β​𝑑sβ)κ2]\displaystyle E\left[\left(\sqrt[\alpha]{\intop\nolimits\_{-\pi}^{z}|\sigma\_{s}|^{2\alpha}ds}\sqrt[\beta]{\intop\nolimits\_{-\pi}^{z}|\tilde{D}\_{N}(z-s)|^{2\beta}ds}\right)^{\frac{\kappa}{2}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | E​[(∫−ππ|σs|2​α​𝑑s)κ2​α]​(∫−ππ|D~N​(z−s)|2​β​𝑑s)κ2​β\displaystyle E\left[\left(\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds\right)^{\frac{\kappa}{2\alpha}}\right]\left(\intop\nolimits\_{-\pi}^{\pi}|\tilde{D}\_{N}(z-s)|^{2\beta}ds\right)^{\frac{\kappa}{2\beta}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | E​[(∫−ππ|σs|2​α​𝑑s)κ2​α]​(∫−ππ|D~N​(s)|2​β​𝑑s)κ2​β,\displaystyle E\left[\left(\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds\right)^{\frac{\kappa}{2\alpha}}\right]\left(\intop\nolimits\_{-\pi}^{\pi}|\tilde{D}\_{N}(s)|^{2\beta}ds\right)^{\frac{\kappa}{2\beta}}, |  |

the first inequality holds true due to Holder’s inequality. The second is clear since D~N\tilde{D}\_{N} is deterministic. The last inequality is clear.

The integral E​[(∫−ππ|σs|2​α​𝑑s)κ2​α]E\left[\left(\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds\right)^{\frac{\kappa}{2\alpha}}\right] is finite due to ?THM? LABEL:lab:integrabilityforsigma with exponent κ∨2​α\kappa\vee 2\alpha.
Moreover

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫−ππ|D~N​(s)|2​β​𝑑s\displaystyle\intop\nolimits\_{-\pi}^{\pi}|\tilde{D}\_{N}(s)|^{2\beta}ds | ≤B2​β2​β​(2​N+1)−1,\displaystyle\leq B\_{2\beta}^{2\beta}(2N+1)^{-1}, |  |

due to ?THM? LABEL:labLemma:DirichletkernelEstimation. Hence

|  |  |  |
| --- | --- | --- |
|  | E​[sup−π≤t≤z|Xt​(z)|κ]≤Cκ​E​[(∫−ππ|σs|2​α​𝑑s)κ2​α]​B2​βκ​(2​N+1)−κ2​β.\displaystyle E\left[\sup\_{-\pi\leq t\leq z}\left|X\_{t}(z)\right|^{\kappa}\right]\leq C\_{\kappa}E\left[\left(\intop\nolimits\_{-\pi}^{\pi}|\sigma\_{s}|^{2\alpha}ds\right)^{\frac{\kappa}{2\alpha}}\right]B\_{2\beta}^{\kappa}(2N+1)^{-\frac{\kappa}{2\beta}}. |  |

∎

###### Lemma 29.

Take κ>2\kappa>2 and let JJ be a process that satisfies ?THM? LABEL:labass:localpJumpsummability with q=κ2q=\frac{\kappa}{2} and C>0C>0, 𝗃>0\mathsf{j}>0. Let Xs:=∫−πscos⁡(q​z)​D~N​(z−s)​𝑑JzX\_{s}:=\intop\nolimits\_{-\pi}^{s}\cos(qz)\tilde{D}\_{N}(z-s)\,dJ\_{z}. We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[|Xs−|κ]≤Cκ​2κ2−1​(π​N−12)κ​E​[(∑z∈[−π,π]Jz2)κ2]+C​Cκ​2κ2−1​(N−12​𝗃)κ2.E\left[\left|X\_{s-}\right|^{\kappa}\right]\leq C\_{\kappa}2^{\frac{\kappa}{2}-1}\left({\pi}{N^{-\frac{1}{2}}}\right)^{\kappa}E\left[\left(\sumop\displaylimits\_{z\in[-\pi,\pi]}\Delta J^{2}\_{z}\right)^{\frac{\kappa}{2}}\right]+CC\_{\kappa}2^{\frac{\kappa}{2}-1}\left(N^{-\frac{1}{2}\mathsf{j}}\right)^{\frac{\kappa}{2}}. |  | (51) |

In particular:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[|Xs−|κ]=O​(1Nκ2)+O​(1Nκ2​𝗃2).E\left[\left|X\_{s-}\right|^{\kappa}\right]=O\left(\frac{1}{N^{\frac{\kappa}{2}}}\right)+O\left(\frac{1}{N^{\frac{\kappa}{2}\frac{\mathsf{j}}{2}}}\right). |  | (52) |

###### Proof.

We have for some Cκ>0C\_{\kappa}>0 by the Burkholder-Davis-Gundy inequality that

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[|Xs−|κ]\displaystyle E\left[\left|X\_{s-}\right|^{\kappa}\right] | ≤Cκ​E​[(∫−πs−D~N2​(z−s)​d​[J]z)κ2].\displaystyle\leq C\_{\kappa}E\left[\left(\intop\nolimits\_{-\pi}^{s-}\tilde{D}\_{N}^{2}(z-s)\,d[J]\_{z}\right)^{\frac{\kappa}{2}}\right]. |  |

We have for δ>0\delta>0

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | E​[(∫−πs−D~N2​(z−s)​d​[J]z)κ2]\displaystyle E\left[\left(\intop\nolimits\_{-\pi}^{s-}\tilde{D}\_{N}^{2}(z-s)\,d[J]\_{z}\right)^{\frac{\kappa}{2}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤2κ2−1\displaystyle\leq 2^{\frac{\kappa}{2}-1} | E​[(∑z∈[−π,π∧s)0<|z−s|<δD~N2​(z−s)​Jz2)κ2+(∑z∈[−π,π∧s)|z−s|≥δD~N2​(z−s)​Jz2)κ2],\displaystyle E\left[\left(\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi\wedge s)\\ 0<|z-s|<\delta\end{subarray}}\tilde{D}\_{N}^{2}(z-s)\Delta J^{2}\_{z}\right)^{\frac{\kappa}{2}}+\left(\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi\wedge s)\\ |z-s|\geq\delta\end{subarray}}\tilde{D}\_{N}^{2}(z-s)\Delta J^{2}\_{z}\right)^{\frac{\kappa}{2}}\right], |  |

due to the elementary inequality (a+b)r≤2r−1​(|a|r+|b|r)(a+b)^{r}\leq 2^{r-1}(|a|^{r}+|b|^{r}), for r=κ2>1r=\frac{\kappa}{2}>1.

The “distant jumps” E​[(∑z∈[−π,π∧s)|z−s|≥δD~N2​(z−s)​Jz2)κ2]E\left[\left(\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi\wedge s)\\
|z-s|\geq\delta\end{subarray}}\tilde{D}\_{N}^{2}(z-s)\Delta J^{2}\_{z}\right)^{\frac{\kappa}{2}}\right] are estimated as follows. For δ>0\delta>0 we have supz∈[−π,π∧s),|z−s|≥δDN​(z−s)≤πδ\sup\_{z\in[-\pi,\pi\wedge s),|z-s|\geq\delta}D\_{N}(z-s)\leq\frac{\pi}{\delta}. Hence, for the rescaled Dirichlet kernel D~N\tilde{D}\_{N} we have D~N2​(x)≤π2δ2​N2\tilde{D}\_{N}^{2}(x)\leq\frac{\pi^{2}}{\delta^{2}N^{2}} for |x|≥δ|x|\geq\delta. Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[(∑z∈[−π,π∧s)|z−s|≥δD~N2​(z−s)​Jz2)κ2]\displaystyle E\left[\left(\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi\wedge s)\\ |z-s|\geq\delta\end{subarray}}\tilde{D}\_{N}^{2}(z-s)\Delta J^{2}\_{z}\right)^{\frac{\kappa}{2}}\right] | ≤(πδ​N)κ​E​[(∑z∈[−π,π∧s)|z−s|≥δJz2)κ2].\displaystyle\leq\left(\frac{\pi}{\delta N}\right)^{\kappa}E\left[\left(\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi\wedge s)\\ |z-s|\geq\delta\end{subarray}}\Delta J^{2}\_{z}\right)^{\frac{\kappa}{2}}\right]. |  |

We continue with the “near located jumps” E​[(∑z∈[−π,π∧s),0<|z−s|<δD~N2​(z−s)​Jz2)κ2]E\left[\left(\sumop\displaylimits\_{z\in[-\pi,\pi\wedge s),0<|z-s|<\delta}\tilde{D}\_{N}^{2}(z-s)\Delta J^{2}\_{z}\right)^{\frac{\kappa}{2}}\right]. We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[(∑z∈[−π,π∧s)0<|z−s|<δD~N2​(z−s)​Jz2)κ2]\displaystyle E\left[\left(\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi\wedge s)\\ 0<|z-s|<\delta\end{subarray}}\tilde{D}\_{N}^{2}(z-s)\Delta J^{2}\_{z}\right)^{\frac{\kappa}{2}}\right] | ≤E​[(∑z∈[−π,π∧s)0<|z−s|<δJz2)κ2].\displaystyle\leq E\left[\left(\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi\wedge s)\\ 0<|z-s|<\delta\end{subarray}}\Delta J^{2}\_{z}\right)^{\frac{\kappa}{2}}\right]. |  |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[(∑z∈[−π,π∧s)0<|z−s|<δD~N2​(z−s)​Jz2)κ2]\displaystyle E\left[\left(\sumop\displaylimits\_{\begin{subarray}{c}z\in[-\pi,\pi\wedge s)\\ 0<|z-s|<\delta\end{subarray}}\tilde{D}\_{N}^{2}(z-s)\Delta J^{2}\_{z}\right)^{\frac{\kappa}{2}}\right] | ≤C​(δ𝗃)κ2,\displaystyle\leq C\left(\delta^{\mathsf{j}}\right)^{\frac{\kappa}{2}}, |  |

due to ?THM? LABEL:labass:localpJumpsummability, with q=κ2q=\frac{\kappa}{2}. As a consequence

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[|Xs−|κ]\displaystyle E\left[\left|X\_{s-}\right|^{\kappa}\right] | ≤Cκ​2κ2−1​(πδ​N)κ​E​[(∑z∈[−π,π]Jz2)κ2]+Cκ​2κ2−1​C​(δ𝗃)κ2.\displaystyle\leq C\_{\kappa}2^{\frac{\kappa}{2}-1}\left(\frac{\pi}{\delta N}\right)^{\kappa}E\left[\left(\sumop\displaylimits\_{z\in[-\pi,\pi]}\Delta J^{2}\_{z}\right)^{\frac{\kappa}{2}}\right]+C\_{\kappa}2^{\frac{\kappa}{2}-1}C\left(\delta^{\mathsf{j}}\right)^{\frac{\kappa}{2}}. |  |

In particular for δ=N−12\delta=N^{-\frac{1}{2}} we obtain ([51](https://arxiv.org/html/2601.09074v1#A3.E51 "In Lemma 29. ‣ Appendix C Auxiliary estimations ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) and ([52](https://arxiv.org/html/2601.09074v1#A3.E52 "In Lemma 29. ‣ Appendix C Auxiliary estimations ‣ The Fourier estimator of spot volatility: Unbounded coefficients and jumps in the price process")) is a direct consequence.
∎

###### Lemma 30.

Let X={Xs}s∈[−π,π]X=\{X\_{s}\}\_{s\in[-\pi,\pi]} be an adapted process with cadlag paths. Let τ\tau be a random time taking values in [−π,π][-\pi,\pi], independent of XX. Take κ>1\kappa>1.
Then

|  |  |  |
| --- | --- | --- |
|  | E​[|Xτ|κ]∨E​[|Xτ−|κ]≤sup−π≤s≤πE​[|Xs|κ].E[|X\_{\tau}|^{\kappa}]\vee E[|X\_{\tau-}|^{\kappa}]\leq\sup\_{-\pi\leq s\leq\pi}E[|X\_{s}|^{\kappa}]. |  |

###### Proof.

We first prove that E​[|Xτ|κ]≤sup−π≤s≤πE​[|Xs|κ]E[|X\_{\tau}|^{\kappa}]\leq\sup\_{-\pi\leq s\leq\pi}E[|X\_{s}|^{\kappa}].
For n∈Nn\in\mathbb{N}, let :={tin:=i2n​2​π−π}i=02n\Pi:=\{t^{n}\_{i}:=\frac{i}{2^{n}}2\pi-\pi\}\_{i=0}^{2^{n}} be a partition of the interval [−π,π][-\pi,\pi]. Define τn:=min{t∈:t≥τ}\tau\_{n}:=\min\{t\in\Pi:t\geq\tau\}. Then, τn\tau\_{n} takes values in the partition, so it is simple, and depends only on the partition and the stopping time τ\tau, so it is also independent of XX. Hence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[|Xτn|κ]\displaystyle E[|X\_{\tau\_{n}}|^{\kappa}] | =∑i=02nE​[|Xtin|κ​1{τn=tin}]\displaystyle=\sumop\displaylimits\_{i=0}^{2^{n}}E\left[|X\_{t^{n}\_{i}}|^{\kappa}1\_{\{\tau\_{n}=t^{n}\_{i}\}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=02nE​[|Xtin|κ]​P​({τn=tin})\displaystyle=\sumop\displaylimits\_{i=0}^{2^{n}}E\left[|X\_{t^{n}\_{i}}|^{\kappa}\right]P(\{\tau\_{n}=t^{n}\_{i}\}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤sup−π≤s≤πE​[|Xs|κ].\displaystyle\leq\sup\_{-\pi\leq s\leq\pi}E[|X\_{s}|^{\kappa}]. |  |

To conclude observe that

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[|Xτ|κ]\displaystyle E[|X\_{\tau}|^{\kappa}] | =E​[lim infn→∞|Xτn|κ]\displaystyle=E[\liminf\_{n\to\infty}|X\_{\tau\_{n}}|^{\kappa}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤lim infn→∞E​[|Xτn|κ].\displaystyle\leq\liminf\_{n\to\infty}E[|X\_{\tau\_{n}}|^{\kappa}]. |  |

The proof of the inequality E​[|Xτ−|κ]≤sup−π≤s≤πE​[|Xs|κ]E[|X\_{\tau-}|^{\kappa}]\leq\sup\_{-\pi\leq s\leq\pi}E[|X\_{s}|^{\kappa}] is similar by considering the sequence of random times θn:=max{t∈:t<τ}\theta\_{n}:=\max\{t\in\Pi:t<\tau\}.
∎

## Appendix D Chebyshev’s inequality for higher moments

The following is a form of Chebyshev’s inequality for higher moments and it follows from Markov’s inequality.

###### Proposition 31.

Let XX be an integrable random variable. For p>0p>0 and t>0t>0:

|  |  |  |
| --- | --- | --- |
|  | P​(|X−E​[X]|>t​E​[|X−E​[X]|p]p)≤1tp.P\left(|X-E[X]|>t\sqrt[p]{E\left[|X-E[X]|^{p}\right]}\right)\leq\frac{1}{t^{p}}. |  |

## Appendix E Diffusions

?THM? LABEL:labthmest1unbounded requires the integrability condition in ?THM? LABEL:lab:integrabilityforsigma. The quality of an approximation through trigonometric polynomials can be quantitatively described with the modulus of continuity as it was discussed in ?THM? LABEL:labrem:moduluscontinuity. In this section we present a large class of diffusions that provide many examples satisfying these conditions.

The next result follows from [[4](https://arxiv.org/html/2601.09074v1#bib.bib4), Theorems 2.3 and 2.4] as a particular case.

###### Theorem 32.

Take continuous functions a,b:[−π,π]×R→Ra,b:[-\pi,\pi]\times\mathbb{R}\to\mathbb{R}. Assume they are locally Lipschitz continuous: there exists LN>0L\_{N}>0

|  |  |  |
| --- | --- | --- |
|  | |a​(t,x)−a​(t,y)|+|b​(t,x)−b​(t,y)|≤LN​|x−y|,|a(t,x)-a(t,y)|+|b(t,x)-b(t,y)|\leq L\_{N}|x-y|, |  |

for |x|,|y|≤N|x|,|y|\leq N. They have at most quadratic growth

|  |  |  |
| --- | --- | --- |
|  | |a​(t,x)|2+|b​(t,x)|2≤K2​(1+|x|2).|a(t,x)|^{2}+|b(t,x)|^{2}\leq K^{2}(1+|x|^{2}). |  |

Then, there exists a unique strong solution to the stochastic differential equation

|  |  |  |
| --- | --- | --- |
|  | d​X=a​(t,Xt)​d​t+b​(t,Xt)​d​Wt,X−π=x∈R.dX=a(t,X\_{t})dt+b(t,X\_{t})dW\_{t},X\_{-\pi}=x\in\mathbb{R}. |  |

Moreover, there exists a constant C>0C>0 depending only on m,Km,K and 2​π2\pi for which

|  |  |  |
| --- | --- | --- |
|  | E​[Xt2​m]≤E​[1+x2​m]​eC​t,t∈[−π,π].E[X^{2m}\_{t}]\leq E[1+x^{2m}]e^{Ct},t\in[-\pi,\pi]. |  |

###### Corollary 33.

Under the conditions of ?THM? LABEL:labtheasydiffusions, we have for r>1r>1

|  |  |  |
| --- | --- | --- |
|  | E​[∫−ππbr​(z,Xz)​𝑑z]<∞.E\left[\intop\nolimits\_{-\pi}^{\pi}b^{r}(z,X\_{z})dz\right]<\infty. |  |

###### Proof.

We have the upper bound:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (|b​(t,Xt)|2)r\displaystyle\left(|b(t,X\_{t})|^{2}\right)^{r} | ≤K2​r​2r−1​(1+|Xt|2​r),\displaystyle\leq K^{2r}2^{r-1}\left(1+|X\_{t}|^{2r}\right), |  |

by assumption on the coefficient bb. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[∫−ππ|b​(t,Xt)|2​r​𝑑t]\displaystyle E\left[\intop\nolimits\_{-\pi}^{\pi}|b(t,X\_{t})|^{2r}dt\right] | ≤K2​r​2r−1​(2​π+E​[∫−ππ|Xt|2​r​𝑑t])\displaystyle\leq K^{2r}2^{r-1}\left(2\pi+E\left[\intop\nolimits\_{-\pi}^{\pi}|X\_{t}|^{2r}dt\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =K2​r​2r−1​(2​π+∫−ππE​[|Xt|2​r]​𝑑t)\displaystyle=K^{2r}2^{r-1}\left(2\pi+\intop\nolimits\_{-\pi}^{\pi}E\left[|X\_{t}|^{2r}\right]dt\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <∞,\displaystyle<\infty, |  |

where the equality holds true by Tonelli-Fubini theorem and the second inequality due to ?THM? LABEL:labtheasydiffusions.
∎

###### Corollary 34.

In addition to the conditions of ?THM? LABEL:labtheasydiffusions assume that the Lipschitz constants LNL\_{N} satisfy L:=supNLN<∞L:=\sup\_{N}L\_{N}<\infty. Then, the process σt:=b​(t,Xt)\sigma\_{t}:=b(t,X\_{t}) has locally γ\gamma-Hölder continuous paths with γ∈(0,12)\gamma\in(0,\frac{1}{2}).

###### Proof.

For α>2\alpha>2 and −π<s<t<π-\pi<s<t<\pi

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[|σt−σs|α]\displaystyle E\left[\left|\sigma\_{t}-\sigma\_{s}\right|^{\alpha}\right] | ≤Lα​E​[|Xt−Xs|α]\displaystyle\leq L^{\alpha}E\left[\left|X\_{t}-X\_{s}\right|^{\alpha}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Lα​E​[|∫stσz​𝑑Wz|α].\displaystyle=L^{\alpha}E\left[\left|\intop\nolimits\_{s}^{t}\sigma\_{z}dW\_{z}\right|^{\alpha}\right]. |  |

Hence, for p,q>1p,q>1 with 1p+1q=1\frac{1}{p}+\frac{1}{q}=1

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[|σt−σs|α]\displaystyle E\left[\left|\sigma\_{t}-\sigma\_{s}\right|^{\alpha}\right] | ≤Lα​Cα​E​[|∫stσz2​𝑑z|α/2]\displaystyle\leq L^{\alpha}C\_{\alpha}E\left[\left|\intop\nolimits\_{s}^{t}\sigma^{2}\_{z}dz\right|^{\alpha/2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Lα​Cα​|t−s|α/2​E​[|∫−ππσz2​q​𝑑zq|α/2].\displaystyle\leq L^{\alpha}C\_{\alpha}\left|t-s\right|^{\alpha/2}E\left[\left|\sqrt[q]{\intop\nolimits\_{-\pi}^{\pi}\sigma^{2q}\_{z}dz}\right|^{\alpha/2}\right]. |  |

As a consequence, the process {b​(t,Xt)}t∈[−π,π]\{b(t,X\_{t})\}\_{t\in[-\pi,\pi]} has a modification that is locally γ\gamma-Hölder continuous due to Kolmogorov-Čentsov continuity theorem; see e.g., [[7](https://arxiv.org/html/2601.09074v1#bib.bib7), 2.2.8]. The modification is actually indistinguishable since the process already has continuous paths.
∎

## Conflict of interest

All authors declare no conflicts of interest in this paper.

## References

* [1]

  T. M. Apostol.
  Mathematical Analysis.
  Addison-Wesley, 1974.
* [2]

  Paul L. Butzer and Rolf J. Nessel.
  Fourier Analysis and Approximation.
  Birkhäuser Basel, 1971.
* [3]

  Christa Cuchiero and Josef Teichmann.
  Fourier transform methods for pathwise covariance estimation in the
  presence of jumps.
  Stochastic Processes and their Applications, 125(1):116–160,
  2015.
* [4]

  I. I. Gihman and A. V. Skorohod.
  Stochastic Differential Equations.
  Springer, 1972.
* [5]

  L. Grafakos.
  Classical Fourier Analysis, volume 249 of Graduate texts
  in Mathematics.
  Springer, 3rd edition, 2014.
* [6]

  J. Jacod.
  Estimation of volatility in a high-frequency setting: a short review.
  Decisions in Economics and Finance, 42(2), 2019.
* [7]

  I. Karatzas and S. Shreve.
  Brownian Motion and Stochastic Calculus.
  Springer-Verlag, 1991.
* [8]

  Paul Malliavin and Maria Elvira Mancino.
  Fourier series method for measurement of multivariate volatilities.
  Finance and Stochastics, 6:49–61, 2002.
* [9]

  Paul Malliavin and Maria Elvira Mancino.
  A Fourier transform method for nonparametric estimation of
  multivariate volatility.
  The Annals of Statistics, 37(4):1983–2010, 2009.
* [10]

  Peter Carr and Hélyette Geman and Dilip B. Madan and Marc Yor.
  The fine structure of asset returns: An empirical investigation.
  The Journal of Business, 75(2):305–332, 2002.
* [11]

  P. Protter.
  Stochastic integration and differential equations.
  In Stochastic modelling and applied probability, volume 21.
  Springer, Berlin Heidelberg New York, version 2.1, second edition, 2005.
* [12]

  D. Revuz and M. Yor.
  Continuous martingales and Brownian motion.
  Springer, 3 edition, 2005.
* [13]

  J. G. Wang S. W. He and J. A. Yan.
  Semimartingale theory and stochastic calculus.
  Science Press, 1992.
* [14]

  E. M. Stein and R. Shakarchi.
  Fourier Analysis: An introduction.
  Princeton University Press, 2003.